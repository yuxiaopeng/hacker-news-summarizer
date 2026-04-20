# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-20.md)

*最后自动更新时间: 2026-04-20 18:24:35*
## 1. Qwen3.6-Max-Preview：更智能、更敏锐、持续进化

**原文标题**: Qwen3.6-Max-Preview: Smarter, Sharper, Still Evolving

**原文链接**: [https://qwen.ai/blog?id=qwen3.6-max-preview](https://qwen.ai/blog?id=qwen3.6-max-preview)

所提供的文本不足以生成详细摘要，因为内容仅包含“Qwen”一词。然而，基于标题**“Qwen3.6-Max-Preview: Smarter, Sharper, Still Evolving”**（Qwen3.6-Max 预览版：更聪明、更敏锐、持续进化），以下是其隐含信息的简要总结：

本文宣布了 Qwen 系列新版本（即 **Qwen3.6-Max**）的预览版发布。标题强调了提升模型认知智能（“更聪明”）及其输出精准度或清晰度（“更敏锐”）的战略重点。通过将其定性为“仍在进化”的“预览版”，文本表明该版本是一个开发里程碑，旨在展示即将推出的功能，同时仍处于不断完善的过程中。

从本质上讲，该公告标志着 Qwen 家族向前迈出的进化性一步，旨在初步版本中优先实现性能的精进。

---

## 2. ggsql：SQL 图形语法

**原文标题**: ggsql: A Grammar of Graphics for SQL

**原文链接**: [https://opensource.posit.co/blog/2026-04-20_ggsql_alpha_release/](https://opensource.posit.co/blog/2026-04-20_ggsql_alpha_release/)

**ggsql** 是一款新发布的 alpha 版本工具，直接在 SQL 语法中实现了“图形语法”（grammar of graphics）。该工具由 **ggplot2** 背后的团队（包括 Thomas Lin Pedersen 和 Hadley Wickham）开发，允许用户在标准 SQL 查询中描述并生成复杂的各种可视化图表。

### 核心功能与语法
该工具通过特定的子句引入了一种声明式的、分层绘图的方法：
*   **VISUALIZE：** 将数据列映射到视觉属性（美学映射），如 x 轴、y 轴和颜色。
*   **DRAW/PLACE：** 添加图层（如散点、直方图、箱线图）或注释。
*   **SETTING/SCALE/LABEL：** 微调图层属性、调色板和文本元数据。

ggsql 的一大优势在于其与 SQL 后端的集成。与需要将数据导出并在本地实例化的 R 或 Python 库不同，ggsql 直接在数据库上执行计算（如直方图的分箱或密度计算）。这使得它在可视化海量数据集（如数十亿行数据）时效率极高，因为仅需传输最终的绘图坐标。

### 使用场景与动机
开发者强调了开发 ggsql 的几点初衷：
1.  **以 SQL 为中心的工作流：** 为主要使用 SQL 的分析师提供了一种强大的、基于代码的可视化替代方案，而无需配置 R 或 Python 环境。
2.  **轻量且安全：** 作为一个独立的可执行文件，与完整的编程语言相比，它更容易进行沙箱隔离，并能轻松嵌入到 **Quarto、Jupyter 和 VS Code** 等工具中。
3.  **AI 兼容性：** ggsql 的结构化、声明式特性非常适合大语言模型（LLM）。LLM 已经擅长生成 SQL，可以轻松通过训练来生成 ggsql 的可组合可视化代码。

通过将 R 生态系统 18 年的经验与 SQL 后端的性能相结合，ggsql 旨在为 SQL 社区提供一个现代、可重现且可扩展的可视化框架。

---

## 3. GitHub 的虚假 Star 经济

**原文标题**: GitHub's Fake Star Economy

**原文链接**: [https://awesomeagents.ai/news/github-fake-stars-investigation/](https://awesomeagents.ai/news/github-fake-stars-investigation/)

一项经过同行评审的研究（ICSE 2026）揭露了 GitHub 上一个职业化的“影子经济”，在 18,617 个代码仓库中识别出 600 万个虚假 Star。虽然区块链项目是早期采用者，但 AI 和大语言模型（LLM）初创公司已成为近期最大的违规群体，利用虚假指标操纵 GitHub 的发现算法并吸引投资者。

这些指标的交易市场公开且廉价。在专业网站、Fiverr 和 Telegram 上，每个 Star 的售价在 0.03 美元到 0.85 美元之间。除了 Star，该生态系统还提供带有虚假贡献记录和“北极代码库”（Arctic Code Vault）徽章的老账号，以绕过检测机制。

其核心驱动力来自风险投资链条。风投机构明确将 Star 数量作为筛选项目的信号；例如，红点创投（Redpoint）将约 2,850 个 Star 视为种子轮融资的中位数。初创公司只需花费几百美元购买 Star，就能制造出项目“受欢迎”的假象，从而骗取数百万美元的资金，实现惊人的投资回报率。

分析显示，这种操纵行为具有明显的特征。虽然像 Flask 或 LangChain 这样的真实项目具有极高的互动率，但被操纵的仓库则充斥着“僵尸账号”（关注者和仓库数均为零），且 Fork 与 Star 的比例以及关注者与 Star 的比例极低。Fork 与 Star 的比例低于 0.05 是判定一个项目只有“虚火”而无实际用户的主要指标。

违规后果正在升级，已不仅限于平台封禁。美国联邦贸易委员会（FTC）2024 年的一项法规禁止购买虚假社交影响力指标，单次违规罚款可达 53,088 美元。此外，美国证券交易委员会（SEC）已开始指控在融资过程中夸大增长指标的创始人涉嫌电信诈骗和证券欺诈。这种“造假”文化正蔓延至整个开发者生态系统，包括 npm 下载量和 VS Code 市场扩展插件，严重威胁着开源软件的诚信根基。

---

## 4. 终于，InfoWars 属于我们了。

**原文标题**: At long last, InfoWars is ours

**原文链接**: [https://theonion.com/at-long-last-infowars-is-ours/](https://theonion.com/at-long-last-infowars-is-ours/)

在这篇带有浓厚黑色幽默色彩的讽刺公告中，全球四面体公司（Global Tetrahedron，《洋葱新闻》旗下的虚构子公司）的虚构首席执行官布莱斯·P·泰特拉德（Bryce P. Tetraeder）庆祝了对 InfoWars.com 的成功收购。泰特拉德将此次接管描述为他儿时关于全球毁灭噩梦的实现，并为该平台的未来勾勒出一幅反乌托邦式的图景。

文中详细阐述了一项计划，旨在将 InfoWars 转型为一个专门用于诈骗、病理性谎言和“自由基误导信息”的“无限虚拟表面”。泰特拉德预想了一种混乱的数字景观：在那里，“恶魔般”的网红强行向用户推销无用产品，访客们则在“妄想的祭坛上自我牺牲”。该网站的新形态被描述为媒体并购与“易消化泥浆”交织的“旋转漩涡”，恐慌与资本在此相互滋养，映射出当今美国的现状。

归根结底，这篇文章是对网红经济、企业贪婪以及信息武器化的尖锐批判。泰特拉德在结尾欢迎“战士们”走向他所承诺的那个“漫长”且“糟糕”的未来，并嘲讽地宣称“既然我们掌管了一个网站，就没人能阻止我们了”。他鼓励用户在这片心理炼狱中安顿下来，并且——非常合时宜地——买一个帆布包。

---

## 5. 星际贸易理论 [pdf]

**原文标题**: The Theory of Interstellar Trade [pdf]

**原文链接**: [https://www.princeton.edu/~pkrugman/interstellar.pdf](https://www.princeton.edu/~pkrugman/interstellar.pdf)

在《星际贸易理论》（The Theory of Interstellar Trade）中，保罗·克鲁格曼（写于1978年，出版于2010年）扩展了标准经济贸易理论，将狭义相对论的影响纳入其中。该论文对货物以近光速运输时恒星系间的贸易运作方式进行了严谨而又带有调侃意味的分析。

克鲁格曼探讨的核心挑战是**时间膨胀**：即对于航天器船员而言，时间流逝（“飞船时间”）比出发地和目的地行星上的观察者（“行星时间”）更慢。这为计算利率和在途货物的现值带来了难题。

克鲁格曼确立了两条“星际贸易基本定理”：
1. **利率均等化：** 当贸易在处于同一惯性参考系的两个行星之间进行时，它们的利率必须通过套利实现均等。
2. **货物估值：** 竞争将确保在途货物的价格是根据行星惯性参考系中流逝的时间来计算的，而非飞船船员所经历的“固有时间”。

论文指出，如果不同惯性系之间的利率不同步，贸易商就可以利用相对论效应获取无限回报。克鲁格曼注意到，尽管船员经历的旅程较短，但货物所占用的资本在整个行星时间跨度内对行星经济而言是不可用的。因此，运输“成本”必须使用静止行星的利率来计算。

尽管该作品是对学术经济论文的戏仿，但它证明了套利和货币时间价值等基本经济原则，即使在星际旅行的极端物理约束下，在理论上依然成立。

---

## 6. 10 years ago, someone wrote a test for Servo that included an expiry in 2026

**原文标题**: 10 years ago, someone wrote a test for Servo that included an expiry in 2026

**原文链接**: [https://mastodon.social/@jdm_/116429380667467307](https://mastodon.social/@jdm_/116429380667467307)

Josh Matthews (jdm), a core developer for the **Servo** web engine project, recently shared a discovery on Mastodon regarding the project's long-term history. 

Roughly ten years ago, a contributor wrote a unit test for Servo that included a hardcoded expiration date set for the year **2026**. At the time the code was written, 2026 likely felt like a distant future, serving as a placeholder for a "far-off" date. However, as Servo has endured and evolved over the last decade, that deadline is now rapidly approaching.

The post highlights the unexpected longevity of software projects. Originally started by Mozilla as an experimental high-performance browser engine written in Rust, Servo is now a Linux Foundation project. This "expiry" serves as a humorous reminder of the staying power of the codebase and the inevitable reality that even the most distant-seeming hardcoded dates eventually catch up with developers.

---

## 7. We accepted surveillance as default

**原文标题**: We accepted surveillance as default

**原文链接**: [https://vivianvoss.net/blog/why-we-accepted-surveillance](https://vivianvoss.net/blog/why-we-accepted-surveillance)

生成摘要时出错

---

## 8. Bloom (YC P26) Is Hiring

**原文标题**: Bloom (YC P26) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/trybloom/jobs](https://www.ycombinator.com/companies/trybloom/jobs)

生成摘要时出错

---

## 9. Deezer says 44% of songs uploaded to its platform daily are AI-generated

**原文标题**: Deezer says 44% of songs uploaded to its platform daily are AI-generated

**原文链接**: [https://techcrunch.com/2026/04/20/deezer-says-44-of-songs-uploaded-to-its-platform-daily-are-ai-generated/](https://techcrunch.com/2026/04/20/deezer-says-44-of-songs-uploaded-to-its-platform-daily-are-ai-generated/)

生成摘要时出错

---

## 10. Kimi K2.6: Advancing Open-Source Coding

**原文标题**: Kimi K2.6: Advancing Open-Source Coding

**原文链接**: [https://www.kimi.com/blog/kimi-k2-6](https://www.kimi.com/blog/kimi-k2-6)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 2 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 3 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 4 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 5 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 6 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 7 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 8 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 9 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 10 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 11 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 12 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 13 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 14 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 15 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 16 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 17 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 18 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 19 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 20 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 21 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 22 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 23 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 24 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 25 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 26 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 27 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 28 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 29 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 30 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 31 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 32 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 33 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 34 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 35 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 36 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 37 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 38 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 39 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 40 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 41 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 42 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 43 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 44 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 45 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 46 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 47 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 48 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 49 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 50 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 51 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 52 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 53 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 54 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 55 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 56 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 57 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 58 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 59 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 60 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 61 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 62 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 63 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 64 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 65 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 66 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 67 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 68 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 69 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 70 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 71 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 72 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 73 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 74 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 75 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 76 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 77 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 78 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 79 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 80 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 81 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 82 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 83 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 84 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 85 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 86 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 87 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 88 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 89 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 90 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 91 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 92 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 93 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 94 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 95 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 96 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 97 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 98 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 99 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 100 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 101 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 102 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 103 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 104 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 105 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 106 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 107 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 108 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 109 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 110 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 111 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 112 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 113 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 114 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 115 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 116 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 117 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 118 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 119 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 120 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 121 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 122 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 123 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 124 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 125 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 126 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 127 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 128 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 129 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 130 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 131 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 132 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 133 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 134 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 135 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 136 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 137 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 138 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 139 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 140 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 141 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 142 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 143 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 144 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 145 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 146 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 147 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 148 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 149 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 150 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 151 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 152 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 153 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 154 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 155 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 156 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 157 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 158 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 159 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 160 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 161 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 162 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 163 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 164 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 165 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 166 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 167 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 168 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 169 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 170 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 171 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 172 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 173 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 174 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 175 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 176 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 177 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 178 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 179 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 180 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 181 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 182 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 183 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 184 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 185 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 186 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 187 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 188 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 189 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 190 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 191 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 192 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 193 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 194 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 195 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 196 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 197 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 198 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 199 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 200 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 201 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 202 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 203 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 204 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 205 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 206 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 207 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 208 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 209 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 210 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 211 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 212 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 213 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 214 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 215 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 216 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 217 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 218 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 219 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 220 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 221 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 222 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 223 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 224 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 225 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 226 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 227 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 228 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 229 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 230 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 231 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 232 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 233 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 234 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 235 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 236 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 237 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 238 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 239 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 240 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 241 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 242 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 243 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 244 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 245 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 246 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 247 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 248 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 249 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 250 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 251 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 252 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 253 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 254 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 255 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 256 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 257 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 258 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 259 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 260 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 261 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 262 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 263 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 264 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 265 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 266 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 267 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 268 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 269 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 270 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 271 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 272 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 273 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 274 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 275 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 276 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 277 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 278 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 279 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 280 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 281 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 282 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 283 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 284 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 285 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 286 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 287 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 288 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 289 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 290 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 291 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 292 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 293 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 294 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 295 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 296 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 297 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 298 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 299 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 300 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 301 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 302 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 303 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 304 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 305 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 306 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 307 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 308 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 309 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 310 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 311 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 312 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 313 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 314 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 315 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 316 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 317 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 318 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 319 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 320 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 321 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 322 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 323 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 324 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 325 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 326 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 327 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 328 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 329 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 330 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 331 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 332 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 333 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 334 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 335 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 336 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 337 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 338 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 339 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 340 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 341 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 342 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 343 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 344 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 345 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 346 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 347 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 348 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 349 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 350 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 351 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 352 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 353 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 354 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 355 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 356 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 357 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 358 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 359 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 360 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 361 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 362 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 363 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 364 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 365 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 366 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 367 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 368 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 369 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 370 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 371 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 372 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 373 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 374 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 375 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 376 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 377 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 378 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 379 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 380 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 381 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 382 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 383 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 384 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 385 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 386 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 387 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 388 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 389 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 390 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 391 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 392 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 393 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 394 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 395 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 396 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
