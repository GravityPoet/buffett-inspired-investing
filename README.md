# buffett-inspired-investing

A Buffett-inspired investing research skill for Codex, OpenCode, Claude-style skill systems, and general long-form company analysis.

This repository is designed for one thing: producing disciplined investment research memos instead of fast opinions.

It blends the strongest parts of several Buffett-themed skill repos:

- primary-source-first workflow
- progressive disclosure and on-demand references
- multi-market source mapping
- practical industry playbooks
- Buffett-style plain language, humility, and elimination discipline

It also deliberately removes the parts that drift too far from Buffett:

- forced role-play as Warren Buffett
- technical-analysis-heavy outputs
- aggressive target prices, trading ranges, and position sizing theater
- false certainty when the answer should be `pass` or `outside competence`

## What This Repo Optimizes For

- Treating a stock as a partial ownership interest in a business
- Starting from filings and official materials instead of commentary
- Judging moat, management, balance-sheet resilience, and capital allocation before valuation
- Allowing `pass`, `watchlist`, and `outside competence` as honest conclusions
- Producing a repeatable memo that can survive re-reading later

## What Is Included

```text
.
├── SKILL.md
├── README.md
├── LICENSE
├── agents/
│   └── openai.yaml
├── references/
│   ├── framework.md
│   ├── industry-playbooks.md
│   ├── memo-template.md
│   ├── mental-models.md
│   ├── official-principles.md
│   ├── source-map.md
│   └── zh-CN/
│       ├── README.md
│       ├── framework.md
│       ├── industry-playbooks.md
│       ├── memo-template.md
│       ├── mental-models.md
│       ├── official-principles.md
│       └── source-map.md
├── scripts/
│   ├── official_market_bootstrap.py
│   └── sec_company_snapshot.py
├── examples/
│   └── example-prompts.md
└── evals/
    └── evals.json
```

## Best Features Kept

### From research-first skill repos

- hard filters before scoring attractive traits
- owner earnings and normalized economics over headline multiples
- capital allocation as a first-class judgment
- primary filings before secondary commentary

### From progressive-skill repos

- quick filter path
- deep analysis path
- topic-specific reference loading
- industry-specific playbooks instead of one generic checklist

### From market-coverage-oriented repos

- U.S. / Hong Kong / Mainland China source map
- official-source routing for each market
- example prompts and evaluation cases
- bootstrap helper commands that do not depend on brittle scraping

### From Buffett-perspective-style repos

- emphasis on plain language and simple explanations
- owner mindset
- humility around prediction
- willingness to say `too hard`

## Deliberate Design Choices

### 1. Buffett-inspired, not Buffett cosplay

The repo uses Buffett's framework and communication style, but it does not require pretending to be Buffett.

That keeps the output more honest and less theatrical.

### 2. Primary-source-first

The research flow pushes the model toward:

1. annual report / 10-K / 20-F / proxy
2. earnings release and transcript
3. investor relations materials
4. regulator filings
5. competitor filings
6. only then secondary analysis

### 3. Pass is a valid outcome

Many prompts force a bullish or bearish conclusion.

This repo treats the following as good outcomes when justified:

- `Strong fit`
- `Watchlist`
- `Weak fit`
- `Reject`
- `Outside competence`

### 4. No fake precision

The framework allows valuation ranges and scenario thinking, but it does not pretend that exact price targets or trading plans are core Buffett behavior.

## Use Cases

- Analyze a listed company with a Buffett-style lens
- Decide whether a business is inside your circle of competence
- Compare two companies on moat and capital allocation quality
- Turn messy research into a structured investment memo
- Challenge a superficially cheap stock that may be a value trap
- Judge whether management acts like owner-operators or empire builders

## Quick Start

### Install as a skill repo

Place this repository at:

```text
$CODEX_HOME/skills/buffett-inspired-investing
```

In many local setups that means:

```text
~/.codex/skills/buffett-inspired-investing
```

### Example prompts

See [examples/example-prompts.md](examples/example-prompts.md).

### Multi-market bootstrap helper

Use the deterministic market helper when you want the fastest official-source starting points without writing brittle scraping logic:

```bash
python3 scripts/official_market_bootstrap.py AAPL
python3 scripts/official_market_bootstrap.py 0700.HK
python3 scripts/official_market_bootstrap.py 600519.SH
python3 scripts/official_market_bootstrap.py 300750.SZ --json
```

The helper does not fetch filings. It standardizes where to start and which official search terms to use.

### SEC helper note

If you use the SEC helper script, set a meaningful `SEC_USER_AGENT` first:

```bash
export SEC_USER_AGENT="Your Name research@example.com"
python3 scripts/sec_company_snapshot.py AAPL
```

The script is a bootstrap helper, not a substitute for reading the filing itself.

## Chinese Reference Layer

The main reference files are written in English first.

For direct Chinese use, mirrored core references live under:

```text
references/zh-CN/
```

Start with [references/zh-CN/README.md](references/zh-CN/README.md) if the memo or discussion should stay in Chinese end to end.

## Research Flow

### A. Quick filter

Use when the user is asking:

- is this worth deeper work?
- does this clear a Buffett bar?
- should this be rejected immediately?

### B. Full memo

Use when the user wants a full investment write-up.

Read in this order:

1. [references/framework.md](references/framework.md)
2. [references/memo-template.md](references/memo-template.md)
3. [references/source-map.md](references/source-map.md) for market-specific primary sources
4. [references/official-principles.md](references/official-principles.md) when you want Berkshire's own owner and capital-allocation logic
5. [references/industry-playbooks.md](references/industry-playbooks.md) as needed
6. [references/mental-models.md](references/mental-models.md) when the user wants deeper philosophical context

If the user wants the analysis in Chinese, switch to the matching files in `references/zh-CN/` after step 1 or from the start.

### C. Topic question

Jump directly to the relevant reference file for:

- moat
- management
- owner earnings
- valuation discipline
- sell rules
- industry-specific analysis

## Official Sources That Informed This Repo

- Berkshire Hathaway Owner's Manual
- Berkshire Hathaway annual letters and annual reports
- Berkshire acquisition criteria
- Buffett's published comments on intrinsic value, owner earnings, management candor, and capital allocation
- official exchange and regulator portals for U.S., Hong Kong, and Mainland China issuers

See [references/source-map.md](references/source-map.md) for links.

## Inspirations

These repositories influenced the design direction:

- `will2025btc/buffett-perspective`
- `BruceLanLan/buffett-oracle-analyzer`
- `agi-now/buffett-skills`
- `MichaelRochonnn/buffett-investment-research`

This repository rewrites the material from scratch into a cleaner, more disciplined version with a narrower quality bar.

## Important Notes

- This is not personalized financial advice.
- This is a research framework, not a prediction engine.
- The safest honest answer is sometimes `pass`.
- A great business and a great stock are not the same thing.
