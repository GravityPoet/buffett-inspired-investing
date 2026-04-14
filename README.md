# 📉 Buffett-Inspired Investing Research

[🇬🇧 English](README.md) | [🇨🇳 简体中文](README_zh.md)

> *"Price is what you pay. Value is what you get."* — Warren Buffett

A Buffett-inspired investing research skill for Codex, Claude-style skill systems, and general long-form company analysis. **This repository is designed for one thing: producing disciplined, plain-language investment research memos instead of fast, noisy opinions.**

---

## 💎 What You Get (Example Output)

Stop settling for technical-analysis theater or false AI certainty. This framework forces the model to evaluate businesses like an owner.

> **🎯 Conclusion: WATCHLIST**
> 
> **Company:** Apple Inc. (AAPL)  
> **Moat:** 🟢 **Strong**. Exceptional pricing power and switching costs driven by the iOS ecosystem and services lock-in.  
> **Management:** 🟢 **Excellent Capital Allocators**. Consistent share repurchases below intrinsic value.  
> **Valuation:** 🔴 **No Margin of Safety**. Currently priced at ~30x owner earnings, pricing in aggressive terminal growth.  
> **Action:** Pass at current prices. Await a fat pitch or macro dislocation.

---

## 🌟 Core Value & Best Outcomes

This repository transforms your AI agent from a generic chatbot into a disciplined investment research associate. By embedding this framework, you gain:

- **Focus on Business Ownership, Not Stock Tickers:** The AI evaluates the durability of the moat, the candor of management, and the quality of capital allocation before ever discussing price.
- **Primary-Source First Methodology:** Bypasses noisy secondary opinions. Prompts explicitly route the AI to read 10-K/20-F filings, proxy statements, and earnings transcripts first.
- **High-Signal "Pass" Culture:** Saves you time and money by explicitly empowering the AI to say *`Pass`* or *`Outside Competence`* immediately, rapidly filtering out mediocre businesses.
- **Ready-to-use Industry Playbooks:** Loads specific mental models depending on the sector (e.g., assessing "float" for insurance, or "switching costs" for SaaS) instead of generic checklists.
- **Fast Multi-Market Bootstrapping:** Included Python scripts instantly generate the correct official exchange entry points (SEC, HKEX, SSE, SZSE) so you never pull the wrong materials.

<details>
<summary>📂 View Repository Structure</summary>

```text
.
├── SKILL.md
├── README.md
├── README_zh.md
├── agents/             # Pre-configured LLM execution profiles
├── references/         # Core framework, templates, and playbooks 
│   └── zh-CN/          # Chinese reference mirrors
├── scripts/            # Deterministic source-fetching tools
├── examples/           # Prompting examples
└── evals/              # CI/CD evaluation cases
```
</details>

## 🚀 Quick Start

### 1. Install as a Skill Repo
Place this repository in your skill directory:
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
