# Source Map

Use this file when deciding where to look first.

## Official Buffett Sources

- Berkshire Hathaway Owner's Manual
  https://www.berkshirehathaway.com/owners.html
- Berkshire Hathaway annual letters archive
  https://www.berkshirehathaway.com/letters/letters.html
- Berkshire Hathaway annual reports archive
  https://www.berkshirehathaway.com/reports.html
- Berkshire acquisition criteria
  included in several Berkshire annual reports such as:
  https://www.berkshirehathaway.com/2002ar/2002ar.pdf
- Recent Berkshire annual report
  https://www.berkshirehathaway.com/2024ar/2024ar.pdf
- Recent Berkshire shareholder letter
  https://www.berkshirehathaway.com/letters/2025ltr.pdf

## U.S. issuers

Start here:

- SEC EDGAR company search
  https://www.sec.gov/edgar/search/
- SEC submissions
  https://data.sec.gov/submissions/
- SEC company facts
  https://data.sec.gov/api/xbrl/companyfacts/
- company IR site
- annual report / 10-K / 10-Q / 20-F
- proxy statement
- earnings release and transcript

Optional local helper:

- `python3 scripts/sec_company_snapshot.py "AAPL"`

Secondary after primaries:

- rating-agency commentary
- industry trade sources
- high-quality financial press

## Hong Kong issuers

Start here:

- HKEXnews home
  https://www.hkexnews.hk/index.htm
- HKEXnews title search
  https://www1.hkexnews.hk/search/titlesearch.xhtml
- HKEXnews title-search guide
  https://www2.hkexnews.hk/-/media/HKEXnews/Homepage/Listed-Company-Publications/Search-Guide/TitleSearchGuide_e.pdf
- HKEXnews advanced-search guide
  http://www2.hkexnews.hk/-/media/HKEXnews/Homepage/Listed-Company-Publications/Search-Guide/AdvancedSearchGuide_e.pdf
- company IR site
- annual report / interim report
- announcements and circulars

Practical note:

- HKEX title search works best with stock code or stock name.
- Searches covering more than twelve months require Stock Code/Stock Name.

Then:

- peer filings
- regulator or exchange disclosures

## Mainland China A-share issuers

Start here:

- CNINFO
  https://www.cninfo.com.cn/
- SSE listed-company announcements
  https://english.sse.com.cn/markets/equities/announcements/
- SZSE company announcements
  https://investor.szse.cn/English/disclosures/announcements/index.html
- company IR site
- annual report / semiannual report / quarterly report
- board and shareholder announcements

Practical note:

- CNINFO explicitly states that it is the Shenzhen Stock Exchange legal information disclosure platform.
- Use CNINFO first even for Shanghai-listed companies, then cross-check on the relevant exchange announcement page when useful.

Then:

- peer filings
- regulator notices
- high-quality industry data

## Local helper

If you want a deterministic market entry point without scraping:

- `python3 scripts/official_market_bootstrap.py AAPL`
- `python3 scripts/official_market_bootstrap.py 0700.HK`
- `python3 scripts/official_market_bootstrap.py 600519.SH`

## What to distrust

Do not start with:

- influencer summaries
- recycled valuation dashboards
- unlabeled AI summaries
- price apps pretending to be research

## Practical order for a real analysis

1. identify the company correctly
2. route to the right official market sources
3. open the latest annual filing
4. open the latest proxy or governance filing
5. open the latest earnings release
6. check recent capital-allocation actions
7. read at least one competitor filing
8. only then read commentary
