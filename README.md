# 📉 Buffett-Inspired AI Investing Framework

[🇬🇧 English](README.md) | [🇨🇳 简体中文](README_zh.md)

> Transform your LLM from a noisy stock-price predictor into a highly disciplined, Tier-1 investment associate.

---

## 🌟 Core Value: What does this give you?

1. **🔒 Zero Hallucination via "Primary-Source" Enforcement**:
   Built-in Python scripts instantly point the AI directly to official SEC, HKEX, and Mainland Exchange portals. Your AI reads 10-Ks, Proxy statements, and earnings transcripts first—not Reddit noise.
2. **🧠 Piercing the Financial Matrix**:
   Strips the AI of its obsession with P/E ratios and stock prices. Forces it to qualitatively evaluate **Moat Durability**, **Management Candor**, and **Capital Allocation** before anything else.
3. **⚔️ Industry-Specific Playbooks**:
   No generic checklist is used here. When analyzing SaaS, it scrutinizes switching costs; when looking at Insurance, it zeroes in on the cost of float. Real, targeted mental models.
4. **🛡️ The Power of the "Pass" Culture**:
   Empowers the AI to swiftly reject mediocre businesses or admit a company is *Outside its Competence*. Drastically increases your signal-to-noise ratio by only producing full memos for fat pitches.

---

## 💎 The "Aha!" Moment (Before & After)

**❌ Using a generic AI prompt:**
> *"Should I buy Apple stock?"*
> **AI Reply:** "Apple (AAPL) is currently trading around $180. The MACD looks bullish and recent iPhone sales are up. Wall Street analysts maintain a strong buy..." (Useless, secondary casino-thinking).

**✅ Using This Repository's Workflow:**
> *(The AI reads the latest 10-K, proxy filings, and applies rigorous mental models to produce a disciplined memo)*
> 
> **🍎 Case 1: Apple Inc. (AAPL)**
> **🎯 Final Decision: WATCHLIST (A wonderful business, poor price)**
> 
> - 🟢 **Business Moat (Exceptional Economic Franchise)**: This is not a tech company; it is a consumer products company with an unbelievable share of mind. The iOS ecosystem creates profound switching costs. When extreme brand loyalty meets digital ecosystem lock-in, it creates the ultimate economic franchise.
> - 🟢 **Capital Allocation (Masterful Owner-Operators)**: Tim Cook perfectly understands what to do when a colossus generates more cash than it can intelligently reinvest. Instead of pursuing value-destroying "diworsification" acquisitions, they have relentlessly and intelligently repurchased their own stock, massively compounding per-share intrinsic value.
> - 🔴 **Margin of Safety (Zero Error Tolerance)**: Paying over 30x earnings prices in flawless perpetual execution. A great business at a dreadful price becomes a mediocre investment. Do not swing at this pitch just because others are wildly swinging.
> 
> **📦 Case 2: Amazon.com (AMZN)**
> **🎯 Final Decision: WATCHLIST (Wait for a fat pitch)**
> 
> - 🟢 **Business Moat (Shared Economies of Scale)**: Retail operates on a classic moat akin to GEICO or Nebraska Furniture Mart—shared economies of scale that continuously lower costs to widen the moat against competitors. Meanwhile, AWS acts as an indispensable digital infrastructure (Utility) with astonishing switching costs.
> - 🟡 **Accounting vs Reality**: Most analysts obsess over GAAP net income, completely misunderstanding the business. From an owner's perspective, management voluntarily suppresses current accounting profits to continuously reinvest massive owner earnings back into widening their infrastructural moat.
> - 🔴 **Valuation (Priced for Perfection)**: You are currently paying full freight for future monopoly certainty. Waiting for a structural dislocation in the market is required to obtain a genuine margin of safety here.
>
> **🎮 Case 3: NVIDIA Corp (NVDA)**
> **🎯 Final Decision: THE "TOO HARD" PILE (Pass)**
> 
> - 🔴 **Outside the Circle of Competence**: This is exactly the type of business Charlie would immediately toss into the "too hard" pile. We simply cannot predict with high certainty the 10-year durability of its software moat against open-source silicon, nor the exact limits of the AI hardware replacement cycle. 
> - 🔴 **Cyclical CapEx Reliance**: Regardless of spectacular current top-line growth, this "pick and shovel" explosion is tied exclusively to a price-insensitive arms race among a very small handful of hyperscalers. When downstream revenue fails to justify upstream infrastructure spend, the resulting cyclical contraction will be brutal.
> - 💡 **Action**: Skip it. There are no called strikes in investing. You don't get bonus points for jumping over seven-foot hurdles; look for the one-foot hurdles where future free cash flow is highly predictable.

---

## 🚀 Quick Start

### 1. Install as a Skill Repo
Place this repository in your workflow or skill directory:
```bash
# Typical local path
$CODEX_HOME/skills/buffett-inspired-investing
```

### 2. Multi-Market Bootstrap Helper
Use the deterministic market helper to quickly fetch official-source starting points across markets (U.S. / HK / Mainland China):

```bash
# Output official SEC / HKEX / SSE / SZSE entry points without brittle scraping:
python3 scripts/official_market_bootstrap.py AAPL
python3 scripts/official_market_bootstrap.py 0700.HK
python3 scripts/official_market_bootstrap.py 600519.SH
python3 scripts/official_market_bootstrap.py 300750.SZ --json
```

> [!NOTE]
> **Using the SEC Helper:** Set a meaningful user agent before pulling SEC snapshots:
> `export SEC_USER_AGENT="Your Name research@example.com"`  
> `python3 scripts/sec_company_snapshot.py AAPL`

### 3. Run Your First Prompt
Check out [examples/example-prompts.md](examples/example-prompts.md) for full ideas. 
Try starting with:
> *"Analyze Moody's with a Buffett-inspired investing framework and produce a structured memo. Read `references/framework.md` first."*

---

## 🧠 Deliberate Design Choices

1. **Buffett-inspired, not Buffett cosplay.** Using his framework keeps outputs honest. Forcing the AI to say *"Hi, I'm Warren"* adds zero analytical value.
2. **Primary-source-first.** The workflow strictly pushes the model down this path: `10-K/20-F -> Earnings Transcripts -> IR Materials -> Regulator Filings -> Secondary Analysis`.
3. **Pass is a valid outcome.** We treat `Strong fit`, `Watchlist`, `Reject`, and `Outside competence` as equally successful endpoints.
4. **No fake precision.** We allow valuation ranges but explicitly block the AI from pretending that exact 12-month target prices are a core Buffett behavior.

<details>
<summary>📚 Research Flow & Reference Usage (Click to expand)</summary>

### A. Quick filter (Triage)
Use when asking: *Is this worth deeper work? Does this clear a Buffett bar?*

### B. Full memo
For a comprehensive write-up, instruct the model to read in this order:
1. `references/framework.md`
2. `references/memo-template.md`
3. `references/source-map.md` (For primary source routing)
4. `references/official-principles.md` (For Berkshire's capital-allocation logic)
5. `references/industry-playbooks.md`
6. `references/mental-models.md`

*Note: For end-to-end Chinese analysis, point the LLM to `references/zh-CN/README.md` first.*
</details>

## 🏛 Official Informing Sources
- Berkshire Hathaway Owner's Manual & Annual Letters.
- Published comments on intrinsic value, owner earnings, and management candor.
- Official exchange portals (SEC, HKEX, Shanghai/Shenzhen).

> [!WARNING]  
> **Disclaimer:** This is a research framework, not an automated prediction engine. It does not constitute personalized financial advice. A great business and a great stock are not the same thing.

## 🤝 Inspirations
This repository is a disciplined, ground-up rewrite inspired by:
- `will2025btc/buffett-perspective`
- `BruceLanLan/buffett-oracle-analyzer`
- `agi-now/buffett-skills`
- `MichaelRochonnn/buffett-investment-research`
