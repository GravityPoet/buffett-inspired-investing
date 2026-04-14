---
name: buffett-inspired-investing
description: Buffett-inspired company analysis and investment research. Use when analyzing a listed company, stock, business quality, moat, management, owner earnings, capital allocation, margin of safety, or when the user asks for a Buffett-style investment memo or巴菲特框架分析.
---

# Buffett-Inspired Investing Research

Use this skill to produce disciplined business analysis, not a hot take.

The job is to determine:

- what the business actually is
- whether it is understandable
- whether it has a durable moat
- whether management behaves like owner-operators
- whether the balance sheet can survive stress
- whether capital allocation has been rational
- whether the current price leaves a margin of safety

Do not force conviction. `Pass` and `Outside competence` are valid conclusions.

## Core stance

- Analyze a stock as partial ownership of a business.
- Judge business quality before price.
- Prefer primary sources over commentary.
- Prefer plain language over finance theater.
- Admit uncertainty instead of hiding it behind false precision.

## When to use

- Stock or listed-company analysis
- Buffett-style framework requests
- Business-quality assessment
- Moat / management / capital allocation questions
- Owner earnings or intrinsic value discussions
- Buy / hold / pass / trim / sell judgment questions
- Market-specific company research for U.S., Hong Kong, or Mainland China issuers

## Research rules

1. Define the exact entity first.
   - ticker
   - exchange
   - geography
   - ownership structure
   - major business segments

2. Start with primary sources.
   - annual report / 10-K / 20-F / equivalent
   - proxy / AGM / shareholder materials
   - earnings release and transcript
   - investor presentation
   - regulator filings
   - competitor filings

3. Treat current facts as time-sensitive.
   Browse live before making claims about price, debt, management, recent buybacks, guidance, or capital allocation.

4. Use the reference files progressively.

### Quick filter path

If the question is simply whether the company is worth deeper work, use the fast filters in `references/framework.md` and stop early when a hard failure is obvious.

### Deep memo path

For a full memo, read in this order:

1. `references/framework.md`
2. `references/memo-template.md`
3. `references/source-map.md`
4. `references/official-principles.md` when the user wants a more official Berkshire-style owner and capital-allocation lens
5. `references/industry-playbooks.md` when the industry matters
6. `references/mental-models.md` when the user asks for deeper Buffett philosophy or decision framing

If the user wants the analysis in Chinese, prefer the matching files under `references/zh-CN/`.

## Market bootstrap helpers

Use the deterministic official-source helper whenever you need to orient a company quickly by market:

```bash
python3 scripts/official_market_bootstrap.py "AAPL"
python3 scripts/official_market_bootstrap.py "0700.HK"
python3 scripts/official_market_bootstrap.py "600519.SH"
python3 scripts/official_market_bootstrap.py "300750.SZ" --json
```

For U.S. issuers, you may optionally add the SEC bootstrap tool:

```bash
python3 scripts/sec_company_snapshot.py "AAPL"
python3 scripts/sec_company_snapshot.py "American Express"
```

Use these as bootstrap tools, not as substitutes for reading the actual filing.

## Hard filters

Reject or sharply downgrade when one of these is true:

- the business cannot be explained simply
- normalized earnings power cannot be estimated without heroic assumptions
- economics depend on commodity pricing with no durable edge
- the company needs friendly capital markets to survive
- management lacks candor or discipline
- capital allocation destroys per-share value
- the industry changes too quickly to estimate long-run economics

## Output requirements

Use the structure in `references/memo-template.md` or `references/zh-CN/memo-template.md`.

Always include:

- circle-of-competence judgment
- moat assessment with evidence
- management and culture assessment
- balance-sheet resilience
- capital-allocation assessment
- owner earnings or a conservative proxy
- valuation logic and margin-of-safety discussion
- verdict band
- confidence level
- missing facts that could change the conclusion
- source links

## Style rules

- Use direct, plain language.
- Explain like an owner, not a broker.
- Prefer ranges over fake precision.
- Separate thesis risk from quote volatility.
- Never use technical analysis as the core argument.
- Do not pretend to be Buffett in first person unless the user explicitly asks for role-play.

## Verdict bands

Use one of:

- `Strong fit`
- `Watchlist`
- `Weak fit`
- `Reject`
- `Outside competence`

## Good failure modes

Prefer these over forced certainty:

- `Outside competence`
- `Insufficient evidence`
- `Good business, wrong price`
- `Interesting price, weak business`
- `Balance sheet too fragile`

## Final note

This is a Buffett-inspired research framework, not personalized investment advice and not a prediction system.
