#!/usr/bin/env python3
"""Print deterministic official-source starting points for listed companies.

This helper does not fetch filings. It standardizes the first official links and
search terms for U.S., Hong Kong, and Mainland China issuers.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass


HKEX_HOME = "https://www.hkexnews.hk/index.htm"
HKEX_TITLE_SEARCH = "https://www1.hkexnews.hk/search/titlesearch.xhtml"
HKEX_TITLE_GUIDE = (
    "https://www2.hkexnews.hk/-/media/HKEXnews/Homepage/"
    "Listed-Company-Publications/Search-Guide/TitleSearchGuide_e.pdf"
)
HKEX_ADVANCED_GUIDE = (
    "http://www2.hkexnews.hk/-/media/HKEXnews/Homepage/"
    "Listed-Company-Publications/Search-Guide/AdvancedSearchGuide_e.pdf"
)
SEC_SEARCH = "https://www.sec.gov/edgar/search/"
SEC_SUBMISSIONS = "https://data.sec.gov/submissions/"
SEC_COMPANYFACTS = "https://data.sec.gov/api/xbrl/companyfacts/"
CNINFO_HOME = "https://www.cninfo.com.cn/"
SSE_ANNOUNCEMENTS = "https://english.sse.com.cn/markets/equities/announcements/"
SZSE_ANNOUNCEMENTS = "https://investor.szse.cn/English/disclosures/announcements/index.html"


@dataclass
class Link:
    label: str
    url: str


@dataclass
class BootstrapResult:
    input: str
    market: str
    normalized_identifier: str
    exchange: str
    primary_source_checklist: list[str]
    official_starting_points: list[Link]
    suggested_search_terms: list[str]
    local_helpers: list[str]
    notes: list[str]


def detect_market(identifier: str, override: str | None) -> str:
    if override:
        return override

    upper = identifier.upper()
    if re.fullmatch(r"\d{1,5}(?:\.HK)?", upper):
        return "hk"
    if re.fullmatch(r"\d{6}(?:\.(?:SH|SS|SZ))?", upper):
        return "cn"
    return "us"


def normalize_hk(identifier: str) -> str:
    upper = identifier.upper().replace(".HK", "")
    digits = re.sub(r"\D", "", upper)
    if not digits:
        raise ValueError("Hong Kong identifiers should contain a stock code.")
    return f"{digits.zfill(5)}.HK"


def infer_cn_suffix(digits: str) -> str:
    if digits[0] in {"5", "6", "9"}:
        return "SH"
    if digits[0] in {"0", "2", "3"}:
        return "SZ"
    raise ValueError(
        "Could not infer A-share exchange from the code. "
        "Use an explicit suffix like 600519.SH or 000001.SZ."
    )


def normalize_cn(identifier: str) -> str:
    upper = identifier.upper()
    match = re.fullmatch(r"(\d{6})(?:\.(SH|SS|SZ))?", upper)
    if not match:
        raise ValueError("A-share identifiers should look like 600519.SH or 000001.SZ.")
    digits = match.group(1)
    suffix = match.group(2) or infer_cn_suffix(digits)
    if suffix == "SS":
        suffix = "SH"
    return f"{digits}.{suffix}"


def normalize_us(identifier: str) -> str:
    compact = re.sub(r"\s+", " ", identifier.strip())
    return compact.upper() if compact and " " not in compact else compact


def us_result(identifier: str) -> BootstrapResult:
    normalized = normalize_us(identifier)
    search_terms = [normalized]
    if normalized and " " not in normalized:
        search_terms.extend(
            [
                f"{normalized} annual report",
                f"{normalized} proxy statement",
                f"{normalized} earnings release",
                f"{normalized} share repurchase",
            ]
        )

    return BootstrapResult(
        input=identifier,
        market="United States",
        normalized_identifier=normalized,
        exchange="SEC / primary U.S. listing",
        primary_source_checklist=[
            "Open the latest annual filing first.",
            "Open the latest proxy or governance filing next.",
            "Check the latest earnings release and any buyback or capital-allocation updates.",
            "Read one peer filing before absorbing commentary.",
        ],
        official_starting_points=[
            Link("SEC EDGAR company search", SEC_SEARCH),
            Link("SEC submissions directory", SEC_SUBMISSIONS),
            Link("SEC company facts API", SEC_COMPANYFACTS),
        ],
        suggested_search_terms=search_terms,
        local_helpers=[
            f'python3 scripts/sec_company_snapshot.py "{identifier}"',
        ],
        notes=[
            "Set SEC_USER_AGENT before making live SEC helper calls.",
            "Use official filings before transcripts, broker notes, or media commentary.",
        ],
    )


def hk_result(identifier: str) -> BootstrapResult:
    normalized = normalize_hk(identifier)
    code = normalized.split(".")[0]
    return BootstrapResult(
        input=identifier,
        market="Hong Kong",
        normalized_identifier=normalized,
        exchange="SEHK",
        primary_source_checklist=[
            "Open HKEXnews Title Search with the stock code or stock name.",
            "Read the latest annual report and latest results announcement.",
            "Check circulars, repurchase notices, dividend notices, and connected-transaction filings.",
            "Read the issuer IR page and one peer filing on HKEXnews.",
        ],
        official_starting_points=[
            Link("HKEXnews home", HKEX_HOME),
            Link("HKEXnews title search", HKEX_TITLE_SEARCH),
            Link("HKEXnews title-search guide", HKEX_TITLE_GUIDE),
            Link("HKEXnews advanced-search guide", HKEX_ADVANCED_GUIDE),
        ],
        suggested_search_terms=[
            code,
            normalized,
            f"{code} annual report",
            f"{code} results announcement",
            f"{code} repurchase",
            f"{code} connected transaction",
        ],
        local_helpers=[],
        notes=[
            "HKEX title search works best with Stock Code or Stock Name.",
            "Any HKEX search covering more than twelve months requires Stock Code or Stock Name.",
            "Use annual report, results announcement, circulars, and capital-allocation notices before commentary.",
        ],
    )


def cn_result(identifier: str) -> BootstrapResult:
    normalized = normalize_cn(identifier)
    code, suffix = normalized.split(".")
    exchange = "SSE" if suffix == "SH" else "SZSE"
    links = [Link("CNINFO", CNINFO_HOME)]
    if suffix == "SH":
        links.append(Link("SSE listed-company announcements", SSE_ANNOUNCEMENTS))
    else:
        links.append(Link("SZSE company announcements", SZSE_ANNOUNCEMENTS))

    return BootstrapResult(
        input=identifier,
        market="Mainland China A-share",
        normalized_identifier=normalized,
        exchange=exchange,
        primary_source_checklist=[
            "Open CNINFO first and locate the latest annual, interim, or quarterly filing.",
            "Check board, shareholder, dividend, repurchase, and risk announcements.",
            "Cross-check the exchange announcements page for the relevant market.",
            "Read the issuer IR site and one peer filing before commentary.",
        ],
        official_starting_points=links,
        suggested_search_terms=[
            code,
            normalized,
            f"{code} 年报",
            f"{code} 季报",
            f"{code} 回购",
            f"{code} 分红",
        ],
        local_helpers=[],
        notes=[
            "CNINFO states that it is the Shenzhen Stock Exchange legal information disclosure platform.",
            "Use CNINFO first even for Shanghai-listed companies, then cross-check on SSE or SZSE when useful.",
            "Read annual, semiannual, quarterly, board, and shareholder announcements before commentary.",
        ],
    )


def build_result(identifier: str, market: str | None) -> BootstrapResult:
    detected = detect_market(identifier, market)
    if detected == "hk":
        return hk_result(identifier)
    if detected == "cn":
        return cn_result(identifier)
    return us_result(identifier)


def render_text(result: BootstrapResult) -> str:
    lines = [
        f"Input: {result.input}",
        f"Market: {result.market}",
        f"Normalized identifier: {result.normalized_identifier}",
        f"Exchange: {result.exchange}",
        "",
        "Primary source checklist",
    ]
    for index, item in enumerate(result.primary_source_checklist, start=1):
        lines.append(f"{index}. {item}")

    lines.append("")
    lines.append("Official starting points")
    for item in result.official_starting_points:
        lines.append(f"- {item.label}: {item.url}")

    if result.suggested_search_terms:
        lines.append("")
        lines.append("Suggested search terms")
        for item in result.suggested_search_terms:
            lines.append(f"- {item}")

    if result.local_helpers:
        lines.append("")
        lines.append("Local helpers")
        for item in result.local_helpers:
            lines.append(f"- {item}")

    if result.notes:
        lines.append("")
        lines.append("Notes")
        for item in result.notes:
            lines.append(f"- {item}")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Print official-source bootstrap links for U.S., Hong Kong, and A-share issuers."
    )
    parser.add_argument("identifier", help="Ticker, stock code, or company hint")
    parser.add_argument(
        "--market",
        choices=["us", "hk", "cn"],
        help="Force the market if auto-detection would be ambiguous.",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text")
    args = parser.parse_args()

    try:
        result = build_result(args.identifier, args.market)
    except ValueError as exc:
        print(f"Input error: {exc}")
        return 1

    if args.json:
        print(json.dumps(asdict(result), indent=2, ensure_ascii=False))
        return 0

    print(render_text(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
