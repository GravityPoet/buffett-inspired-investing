# 中文来源地图

这一页解决的是：

不同市场的公司，第一步到底该去哪里看官方披露。

## Buffett / Berkshire 官方材料

- Berkshire Hathaway Owner's Manual
  https://www.berkshirehathaway.com/owners.html
- Berkshire 年度股东信归档
  https://www.berkshirehathaway.com/letters/letters.html
- Berkshire 年报归档
  https://www.berkshirehathaway.com/reports.html
- 收购标准示例
  https://www.berkshirehathaway.com/2002ar/2002ar.pdf
- 近年年报
  https://www.berkshirehathaway.com/2024ar/2024ar.pdf
- 近年股东信
  https://www.berkshirehathaway.com/letters/2025ltr.pdf

## 美股公司

优先顺序：

- SEC EDGAR 公司搜索
  https://www.sec.gov/edgar/search/
- SEC submissions
  https://data.sec.gov/submissions/
- SEC company facts
  https://data.sec.gov/api/xbrl/companyfacts/
- 公司 IR 网站
- 年报 / 10-K / 10-Q / 20-F
- Proxy
- 最新业绩公告

本地辅助：

- `python3 scripts/sec_company_snapshot.py "AAPL"`

## 港股公司

优先顺序：

- HKEXnews 首页
  https://www.hkexnews.hk/index.htm
- HKEXnews Title Search
  https://www1.hkexnews.hk/search/titlesearch.xhtml
- HKEXnews Title Search 指南
  https://www2.hkexnews.hk/-/media/HKEXnews/Homepage/Listed-Company-Publications/Search-Guide/TitleSearchGuide_e.pdf
- HKEXnews Advanced Search 指南
  http://www2.hkexnews.hk/-/media/HKEXnews/Homepage/Listed-Company-Publications/Search-Guide/AdvancedSearchGuide_e.pdf
- 公司 IR 网站
- 年报 / 中报 / 业绩公告 / 通函

实操提示：

- 港股搜索尽量直接用股票代码或股票简称
- 如果搜索范围超过 12 个月，HKEX 要求必须填 Stock Code 或 Stock Name

## A 股公司

优先顺序：

- 巨潮资讯网
  https://www.cninfo.com.cn/
- 上交所英文公告页
  https://english.sse.com.cn/markets/equities/announcements/
- 深交所英文公告页
  https://investor.szse.cn/English/disclosures/announcements/index.html
- 公司 IR 网站
- 年报 / 中报 / 季报
- 董事会、股东会、回购、分红、风险提示等公告

实操提示：

- 巨潮资讯网自己明确写了，它是“深圳证券交易所法定信息披露平台”
- 即使是沪市公司，也建议先在巨潮看，再按需要去上交所或深交所公告页交叉确认

## 本地多市场入口

如果你想先把市场和官方入口快速理顺：

- `python3 scripts/official_market_bootstrap.py AAPL`
- `python3 scripts/official_market_bootstrap.py 0700.HK`
- `python3 scripts/official_market_bootstrap.py 600519.SH`

## 不要一上来就看什么

- KOL 观点汇总
- 一堆二手估值看板
- 没标来源的 AI 摘要
- 把行情页当研究的应用

## 一套实用顺序

1. 先确认公司身份和市场没搞错
2. 先走到对应市场的官方入口
3. 打开最新年报
4. 打开治理 / 股东 / proxy 类材料
5. 看最新业绩公告
6. 看近期资本配置动作
7. 至少读一个同行披露
8. 最后再看二手评论
