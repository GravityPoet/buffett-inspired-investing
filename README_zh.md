# 📉 Buffett-Inspired Investing Research (巴菲特启发式投资研究)

[🇬🇧 English](README.md) | [🇨🇳 简体中文](README_zh.md)

> *"Price is what you pay. Value is what you get." (价格是你付出的，价值是你得到的。)* — Warren Buffett

为 Codex、基于 Claude 的 Agent 系统以及任何长文本公司分析打造的“巴菲特启发式”研究技能库。
**本仓库只为一个目的而生：产出具有严密纪律的、基于白话的投资研究备忘录，而不是随口猜涨跌的噪音。**

---

## 💎 效果展示 (你能得到什么)

不要再容忍 AI 给你毫无依据的技术分析或者虚假的股价预测了。本框架强制大模型以“企业所有者”的视角来评估一门生意。

> **🎯 结论: WATCHLIST (加入观察池)**
> 
> **公司:** 苹果 (Apple Inc. - AAPL)  
> **护城河:** 🟢 **极强 (Strong)**。由 iOS 生态系统与服务绑定带来的极高转换成本与卓越定价权。  
> **管理层:** 🟢 **优秀的资本配置者**。持续不断地在低于内在价值时进行股票回购。  
> **估值:** 🔴 **无安全边际 (No Margin of Safety)**。当前价格约为所有者盈余的 30 倍，已经计入了激进的永续增长预期。  
> **结论行动:** 当前价格放弃买入 (Pass)。耐心等待击球区或宏观市场错杀。

---

## 🆚 为什么选择本框架？

大多数带“巴菲特”标签的提示词包（Prompt-packs），仅仅是让大模型进行“角色扮演”，或胡乱编造目标价。本仓库**去除了表演成分，保留了严格的投资纪律**。

| ❌ 普通 AI 投资研究 | ✅ 本库的巴菲特启发式框架 |
| :--- | :--- |
| 盯着表面 P/E 市盈率和 K 线图看 | 极其强调 **所有者盈余 (Owner Earnings)** 和 **资本配置** |
| 从二手新闻、评论员文章开始分析 | **第一手研报优先** (10-K, Proxy, 财报电话会) |
| 强行给出一个“看涨”或“看跌”的结论 | 允许结论为：**`放弃 (Pass)`**, **`观察池`**, 或 **`超出能力圈保护自己`** |
| 用通用的“金融分析模板”套用所有公司 | 针对特定行业建立专属分析 Playbooks |

<details>
<summary>📂 查看仓库树状结构</summary>

```text
.
├── SKILL.md
├── README.md
├── README_zh.md        # 中文说明
├── agents/             # 预配置的大语言模型执行配置
├── references/         # 核心框架、模板与行业手册
│   └── zh-CN/          # 完全本地化的中文参阅文档库
├── scripts/            # 确定性的信息源抓取工具
├── examples/           # 提示词使用范例
└── evals/              # 自动化评测用例
```
</details>

## 🚀 快速开始

### 1. 安装为本地技能库
将本仓库放置于你的 Agent 工作流技能目录：
```bash
# 典型的本地路径
$CODEX_HOME/skills/buffett-inspired-investing
```

### 2. 跨市场公司研报引导脚手架
使用极具确定性的 python 引导脚本，直接获取官方信源（美股/港股/A股）的阅读切入点，避免依赖大模型不稳定的网页搜索：

```bash
python3 scripts/official_market_bootstrap.py AAPL
python3 scripts/official_market_bootstrap.py 0700.HK
python3 scripts/official_market_bootstrap.py 600519.SH
python3 scripts/official_market_bootstrap.py 300750.SZ --json
```

> [!NOTE]
> **SEC 助手注意事项:** 在抓取 SEC 财报快照前请设置合规的 User Agent：
> `export SEC_USER_AGENT="Your Name research@example.com"`  
> `python3 scripts/sec_company_snapshot.py AAPL`

### 3. 给 AI 下达第一个指令
你可以在 [examples/example-prompts.md](examples/example-prompts.md) 中找到完整的提问灵感。推荐用以下方式开局：
> *"使用巴菲特启发式投资框架分析腾讯 (0700.HK)，并输出结构化的投资备忘录。请优先阅读本仓库中的 `references/zh-CN/framework.md`。"*

---

## 🧠 刻意的架构设计抉择

1. **巴菲特启发式，而非巴菲特角色扮演 (Cosplay)**。使用他的框架可以保持输出的诚实性，强迫 AI 说“你好，我是巴菲特”对分析深度毫无帮助。
2. **第一手来源优先**。此工作流强制模型走这条路线：`10-K/20-F -> 业绩电话会文字录 -> 投资者关系材料 -> 监管文件 -> 然后才是二手分析`。
3. **“放弃 (Pass)” 是一种非常优质的成功产出**。我们认为输出 `强力匹配`、`加入观察池`、`放弃`、`超出能力范围` 都是同样合理且成功的结论。
4. **拒绝虚假精确度**。我们允许给出估值区间范围或情境推演，但明令禁止 AI 编造精确的未来 12 个月目标价。

<details>
<summary>📚 研究工作流建议 (点击展开)</summary>

### A. 快速过滤 (Triage)
遇到以下情况时使用: *这门生意值得继续深挖吗？它能越过巴菲特的最底线门槛吗？*

### B. 完整备忘录 (Full Memo)
当需要撰写全面的投资备忘录时，请设定 AI 按以下顺序摄取上下文：
1. `references/zh-CN/framework.md` 
2. `references/zh-CN/memo-template.md`
3. `references/zh-CN/source-map.md` (跨市场官方信源映射)
4. `references/zh-CN/official-principles.md` (伯克希尔哈撒韦官方原则)
5. `references/zh-CN/industry-playbooks.md`
</details>

## 🏛 致敬的官方资料
- 伯克希尔·哈撒韦所有者手册 & 历年致股东信
- 官方对内在价值、所有者盈余、管理层坦诚度和资本配置的公开论述
- 美股 (SEC)、港股 (HKEX) 和上交所/深交所监管门户的获取规则

> [!WARNING]  
> **免责声明：** 这是一个研究框架与 AI 技能库，而不是自动化的行情预测引擎。不构成且不包含任何个性化的财务/投资建议。*一家极好的生意，不一定能成为一支在当前出价下极好的股票。*
