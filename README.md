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
> **🎯 Final Decision: WATCHLIST (Do Not Buy at Current Prices)**
> 
> - 🟢 **Business Moat (Very Strong, but facing a paradigm shift)**: Apple possesses structural advantages others dream of—2B active devices, custom silicon, and "The Whole Widget" integration. However, as we enter the AI hardware era (akin to the PC industry in 1977), where categories like AirPods are redefined into "always-on personal AI interfaces," Apple's decade-long software stagnation ("Siri is shit") threatens their moat.
> - 🟡 **Management (Incredible Operators, Weak Product Vision)**: Tim Cook's team acts as masterful capital allocators, aggressively retiring shares below intrinsic value. But "Nice doesn't ship revolutionary products, and you can't hire taste." The organization excels at execution but fundamentally lacks the visionary product DNA necessary to lead the AI hardware revolution instead of following it.
> - 🔴 **Margin of Safety (None)**: The market is currently demanding a massive premium (~30x owner earnings), pricing in flawless perpetual growth. There is **zero room for error**. A wonderful business facing monumental shifts at a dreadful price.
>
> **📦 Case 2: Amazon.com (AMZN)**
> **🎯 Final Decision: BUY & HOLD**
> 
> - 🟢 **Business Moat (Unassailable Scale Economies)**: Bezos' ethos ("Your margin is my opportunity") is fully institutionalized. Between AWS's massive ecosystem lock-in and the retail network's insurmountable CapEx moat, new entrants face a multi-decade, hundred-billion-dollar barrier to entry.
> - 🟢 **Management (Absolute Long-term Focus)**: From Bezos to Jassy, management displays a rare willingness to suppress short-term accounting profits (Net Income) in favor of relentlessly reinvesting owner earnings into infrastructure and AWS capacity, trading short-term Wall Street optics for absolute long-term market dominance.
> - 🟡 **Margin of Safety (Fair to Attractive)**: Generic AI will scream about Amazon's "high P/E ratio." Our framework recognizes that by separating growth CapEx from maintenance CapEx, and isolating AWS's extreme return on capital, the massive underlying free cash flow generation is ultimately available at a highly attractive price.
>
> **🎮 Case 3: NVIDIA Corp (NVDA)**
> **🎯 Final Decision: WATCHLIST (Awaiting Cycle Dislocation)**
> 
> - 🟢 **Business Moat (Impregnable Hardware-Software Ecosystem)**: Conventional wisdom sees a chip designer. Our framework reveals an 18-year software monopoly—CUDA. This highly sticky developer ecosystem mirrors Windows' dominance in the PC era. Competitors trying to build a faster chip are fundamentally missing the point; Nvidia sells a full-stack data center platform with zero viable alternatives.
> - 🟢 **Management (Generational Vision & Execution)**: Jensen Huang is the rare founder-operator who combines decade-ahead architectural vision (betting the farm on deep learning long before ChatGPT) with ruthless execution. His taste and conviction established today's AI infrastructure throne.
> - 🔴 **Margin of Safety (Highly Fragile to Peak-Cycle CapEx)**: While forward P/E might seem "justifiable" to generic AI analysts, an owner's perspective warns that current hyper-earnings rely exclusively on the unrelenting, price-insensitive CapEx arms race among Hyperscalers (Meta, MSFT, Google). If downstream AI monetization falters and infrastructure spend decelerates, NVDA faces violent cyclical contraction. An era-defining business with completely non-existent margin of safety at peak-cycle pricing.

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
