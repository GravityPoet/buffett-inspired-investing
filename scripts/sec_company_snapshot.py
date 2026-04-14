#!/usr/bin/env python3
"""Fetch a conservative SEC snapshot for a U.S.-listed company.

Adapted in spirit from MIT-licensed Buffett research helpers and rewritten for this repo.
Uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import difflib
import json
import os
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any


TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"
SUBMISSIONS_URL = "https://data.sec.gov/submissions/CIK{cik}.json"
COMPANYFACTS_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
ANNUAL_FORMS = {"10-K", "10-K/A", "20-F", "20-F/A", "40-F", "40-F/A"}


@dataclass
class Match:
    title: str
    ticker: str
    cik: int


def user_agent() -> str:
    return os.environ.get(
        "SEC_USER_AGENT",
        "buffett-inspired-investing/1.0 (research workflow helper; set SEC_USER_AGENT for your contact info)",
    )


def fetch_json(url: str) -> Any:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": user_agent(),
            "Accept": "application/json,text/plain,*/*",
            "Accept-Encoding": "identity",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def pick_match(query: str, tickers: list[dict[str, Any]]) -> Match | None:
    query_upper = query.upper().strip()
    query_norm = normalize(query)

    for item in tickers:
        if item["ticker"].upper() == query_upper:
            return Match(item["title"], item["ticker"], int(item["cik_str"]))

    for item in tickers:
        if normalize(item["title"]) == query_norm:
            return Match(item["title"], item["ticker"], int(item["cik_str"]))

    partials: list[dict[str, Any]] = []
    for item in tickers:
        title_norm = normalize(item["title"])
        ticker_norm = normalize(item["ticker"])
        if query_norm and (query_norm in title_norm or query_norm in ticker_norm):
            partials.append(item)
    if partials:
        partials.sort(key=lambda item: (len(item["title"]), item["title"]))
        item = partials[0]
        return Match(item["title"], item["ticker"], int(item["cik_str"]))

    names = [item["title"] for item in tickers] + [item["ticker"] for item in tickers]
    close = difflib.get_close_matches(query, names, n=1, cutoff=0.75)
    if not close:
        return None
    target = close[0]
    for item in tickers:
        if item["title"] == target or item["ticker"] == target:
            return Match(item["title"], item["ticker"], int(item["cik_str"]))
    return None


def recent_filings(submissions: dict[str, Any], forms: set[str], limit: int) -> list[dict[str, str]]:
    recent = submissions.get("filings", {}).get("recent", {})
    if not recent:
        return []

    rows: list[dict[str, str]] = []
    count = len(recent.get("form", []))
    for index in range(count):
        form = recent["form"][index]
        if form not in forms:
            continue
        accession = recent["accessionNumber"][index]
        accession_nodash = accession.replace("-", "")
        primary = recent["primaryDocument"][index]
        filing_date = recent["filingDate"][index]
        cik = str(submissions["cik"]).zfill(10)
        url = (
            "https://www.sec.gov/Archives/edgar/data/"
            f"{int(cik)}/{accession_nodash}/{primary}"
        )
        rows.append(
            {
                "form": form,
                "filing_date": filing_date,
                "accession": accession,
                "url": url,
            }
        )
        if len(rows) >= limit:
            break
    return rows


def choose_fact(facts: dict[str, Any], tags: list[str], unit: str) -> dict[str, Any] | None:
    gaap = facts.get("facts", {}).get("us-gaap", {})
    candidates: list[dict[str, Any]] = []
    for tag in tags:
        entry = gaap.get(tag)
        if not entry:
            continue
        units = entry.get("units", {})
        for item in units.get(unit, []):
            if item.get("form") not in ANNUAL_FORMS:
                continue
            if "fy" not in item or "val" not in item:
                continue
            candidate = dict(item)
            candidate["tag"] = tag
            candidates.append(candidate)
    if not candidates:
        return None
    candidates.sort(
        key=lambda item: (
            int(item.get("fy", 0)),
            item.get("filed", ""),
            item.get("frame", ""),
        ),
        reverse=True,
    )
    return candidates[0]


def fmt_money(value: float | int | None) -> str:
    if value is None:
        return "n/a"
    sign = "-" if value < 0 else ""
    amount = abs(float(value))
    if amount >= 1_000_000_000:
        return f"{sign}${amount / 1_000_000_000:.2f}B"
    if amount >= 1_000_000:
        return f"{sign}${amount / 1_000_000:.2f}M"
    return f"{sign}${amount:,.0f}"


def build_summary(match: Match, submissions: dict[str, Any], facts: dict[str, Any]) -> dict[str, Any]:
    cik10 = str(match.cik).zfill(10)
    filings_page = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={match.ticker}"
    companyfacts_page = COMPANYFACTS_URL.format(cik=cik10)

    revenue = choose_fact(
        facts,
        [
            "RevenueFromContractWithCustomerExcludingAssessedTax",
            "RevenueFromContractWithCustomerIncludingAssessedTax",
            "SalesRevenueNet",
            "Revenues",
        ],
        "USD",
    )
    operating_income = choose_fact(facts, ["OperatingIncomeLoss"], "USD")
    net_income = choose_fact(facts, ["NetIncomeLoss", "ProfitLoss"], "USD")
    operating_cash_flow = choose_fact(facts, ["NetCashProvidedByUsedInOperatingActivities"], "USD")
    capex = choose_fact(
        facts,
        ["PaymentsToAcquirePropertyPlantAndEquipment", "PropertyPlantAndEquipmentAdditions"],
        "USD",
    )
    cash = choose_fact(facts, ["CashAndCashEquivalentsAtCarryingValue"], "USD")
    long_term_debt = choose_fact(
        facts,
        [
            "LongTermDebtAndFinanceLeaseObligations",
            "LongTermDebtAndCapitalLeaseObligations",
            "LongTermDebt",
            "LongTermBorrowings",
        ],
        "USD",
    )
    current_debt = choose_fact(
        facts,
        ["LongTermDebtCurrent", "ShortTermBorrowings", "ShortTermDebt"],
        "USD",
    )

    cfo_value = float(operating_cash_flow["val"]) if operating_cash_flow else None
    capex_value = abs(float(capex["val"])) if capex else None
    total_debt = None
    if long_term_debt or current_debt:
        total_debt = float(long_term_debt["val"]) if long_term_debt else 0.0
        total_debt += float(current_debt["val"]) if current_debt else 0.0

    owner_earnings_proxy = None
    if cfo_value is not None and capex_value is not None:
        owner_earnings_proxy = cfo_value - capex_value

    return {
        "company": {
            "name": match.title,
            "ticker": match.ticker,
            "cik": cik10,
            "filings_page": filings_page,
            "companyfacts_page": companyfacts_page,
        },
        "latest_filings": {
            "annual": recent_filings(submissions, {"10-K", "10-K/A", "20-F", "20-F/A", "40-F", "40-F/A"}, 2),
            "quarterly": recent_filings(submissions, {"10-Q", "10-Q/A", "6-K"}, 3),
            "proxy": recent_filings(submissions, {"DEF 14A", "DEFA14A"}, 2),
            "current": recent_filings(submissions, {"8-K"}, 3),
        },
        "high_level_facts": {
            "revenue": fmt_money(revenue["val"]) if revenue else "n/a",
            "operating_income": fmt_money(operating_income["val"]) if operating_income else "n/a",
            "net_income": fmt_money(net_income["val"]) if net_income else "n/a",
            "operating_cash_flow": fmt_money(cfo_value),
            "capex": fmt_money(capex_value),
            "owner_earnings_proxy": fmt_money(owner_earnings_proxy),
            "cash": fmt_money(float(cash["val"])) if cash else "n/a",
            "total_debt": fmt_money(total_debt),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch a conservative SEC company snapshot.")
    parser.add_argument("query", help="Ticker or company name")
    parser.add_argument("--json", action="store_true", help="Emit raw JSON")
    args = parser.parse_args()

    try:
        tickers_raw = fetch_json(TICKERS_URL)
        tickers = list(tickers_raw.values()) if isinstance(tickers_raw, dict) else tickers_raw
        match = pick_match(args.query, tickers)
        if match is None:
            print(f"No SEC match found for: {args.query}", file=sys.stderr)
            return 1

        cik10 = str(match.cik).zfill(10)
        submissions = fetch_json(SUBMISSIONS_URL.format(cik=cik10))
        facts = fetch_json(COMPANYFACTS_URL.format(cik=cik10))
        summary = build_summary(match, submissions, facts)
    except urllib.error.URLError as exc:
        if isinstance(exc, urllib.error.HTTPError) and exc.code == 403:
            print(
                "Network error: HTTP Error 403: Forbidden. "
                "The SEC may require a better SEC_USER_AGENT or may be throttling this environment.",
                file=sys.stderr,
            )
        else:
            print(f"Network error: {exc}", file=sys.stderr)
        return 2
    except Exception as exc:  # noqa: BLE001
        print(f"Unexpected error: {exc}", file=sys.stderr)
        return 3

    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
        return 0

    print(f"Company: {summary['company']['name']} ({summary['company']['ticker']})")
    print(f"CIK: {summary['company']['cik']}")
    print(f"Filings page: {summary['company']['filings_page']}")
    print(f"Company facts: {summary['company']['companyfacts_page']}")
    print("")
    print("High-level facts")
    for key, value in summary["high_level_facts"].items():
        label = key.replace("_", " ").title()
        print(f"- {label}: {value}")
    print("")
    print("Latest annual filings")
    for filing in summary["latest_filings"]["annual"]:
        print(f"- {filing['form']} {filing['filing_date']} {filing['url']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
