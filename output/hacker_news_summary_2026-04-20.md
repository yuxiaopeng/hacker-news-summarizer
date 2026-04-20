# Hacker News 热门文章摘要 (2026-04-20)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. M 7.4 earthquake – 100 km ENE of Miyako, Japan

**原文标题**: M 7.4 earthquake – 100 km ENE of Miyako, Japan

**原文链接**: [https://earthquake.usgs.gov/earthquakes/eventpage/us6000sri7/](https://earthquake.usgs.gov/earthquakes/eventpage/us6000sri7/)

生成摘要时出错

---

## 12. At Long Last, InfoWars Is Ours

**原文标题**: At Long Last, InfoWars Is Ours

**原文链接**: [https://theonion.info/](https://theonion.info/)

生成摘要时出错

---

## 13. Sauna effect on heart rate

**原文标题**: Sauna effect on heart rate

**原文链接**: [https://tryterra.co/research/sauna-effect-on-heart-rate](https://tryterra.co/research/sauna-effect-on-heart-rate)

生成摘要时出错

---

## 14. Chernobyl's last wedding

**原文标题**: Chernobyl's last wedding

**原文链接**: [https://www.bbc.com/news/articles/c0q92lx8q75o](https://www.bbc.com/news/articles/c0q92lx8q75o)

生成摘要时出错

---

## 15. Atlassian enables default data collection to train AI

**原文标题**: Atlassian enables default data collection to train AI

**原文链接**: [https://letsdatascience.com/news/atlassian-enables-default-data-collection-to-train-ai-f71343d8](https://letsdatascience.com/news/atlassian-enables-default-data-collection-to-train-ai-f71343d8)

生成摘要时出错

---

## 16. Larry Tesler: A Personal History of Modeless Text Editing and Cut/Copy-Paste (2012)

**原文标题**: Larry Tesler: A Personal History of Modeless Text Editing and Cut/Copy-Paste (2012)

**原文链接**: [https://dl.acm.org/doi/epdf/10.1145/2212877.2212896](https://dl.acm.org/doi/epdf/10.1145/2212877.2212896)

生成摘要时出错

---

## 17. WebUSB Extension for Firefox

**原文标题**: WebUSB Extension for Firefox

**原文链接**: [https://github.com/ArcaneNibble/awawausb](https://github.com/ArcaneNibble/awawausb)

生成摘要时出错

---

## 18. Kefir C17/C23 Compiler

**原文标题**: Kefir C17/C23 Compiler

**原文链接**: [https://sr.ht/~jprotopopov/kefir/](https://sr.ht/~jprotopopov/kefir/)

生成摘要时出错

---

## 19. All phones sold in the EU to have replaceable batteries from 2027

**原文标题**: All phones sold in the EU to have replaceable batteries from 2027

**原文链接**: [https://www.theolivepress.es/spain-news/2026/04/20/eu-to-force-replaceable-batteries-in-phones-and-tablets-from-2027/](https://www.theolivepress.es/spain-news/2026/04/20/eu-to-force-replaceable-batteries-in-phones-and-tablets-from-2027/)

生成摘要时出错

---

## 20. OpenClaw isn't fooling me. I remember MS-DOS

**原文标题**: OpenClaw isn't fooling me. I remember MS-DOS

**原文链接**: [https://www.flyingpenguin.com/build-an-openclaw-free-secure-always-on-local-ai-agent/](https://www.flyingpenguin.com/build-an-openclaw-free-secure-always-on-local-ai-agent/)

生成摘要时出错

---

## 21. Focused microwaves allow 3D printers to fuse circuits onto almost anything

**原文标题**: Focused microwaves allow 3D printers to fuse circuits onto almost anything

**原文链接**: [https://newatlas.com/electronics/meta-nfc-focused-microwaves-circuits/](https://newatlas.com/electronics/meta-nfc-focused-microwaves-circuits/)

生成摘要时出错

---

## 22. I prompted ChatGPT, Claude, Perplexity, and Gemini and watched my Nginx logs

**原文标题**: I prompted ChatGPT, Claude, Perplexity, and Gemini and watched my Nginx logs

**原文链接**: [https://surfacedby.com/blog/nginx-logs-ai-traffic-vs-referral-traffic](https://surfacedby.com/blog/nginx-logs-ai-traffic-vs-referral-traffic)

生成摘要时出错

---

## 23. I'm never buying another Kindle

**原文标题**: I'm never buying another Kindle

**原文链接**: [https://www.androidauthority.com/amazon-kindle-2026-3657863/](https://www.androidauthority.com/amazon-kindle-2026-3657863/)

生成摘要时出错

---

## 24. NSA is using Anthropic's Mythos despite blacklist

**原文标题**: NSA is using Anthropic's Mythos despite blacklist

**原文链接**: [https://www.axios.com/2026/04/19/nsa-anthropic-mythos-pentagon](https://www.axios.com/2026/04/19/nsa-anthropic-mythos-pentagon)

生成摘要时出错

---

## 25. Up to 8M Bees Are Living in an Underground Network Beneath This Cemetery

**原文标题**: Up to 8M Bees Are Living in an Underground Network Beneath This Cemetery

**原文链接**: [https://www.discovermagazine.com/up-to-8-million-bees-are-living-in-an-underground-network-beneath-this-cemetery-48977](https://www.discovermagazine.com/up-to-8-million-bees-are-living-in-an-underground-network-beneath-this-cemetery-48977)

生成摘要时出错

---

## 26. IPC medley: message-queue peeking, io_uring, and bus1

**原文标题**: IPC medley: message-queue peeking, io_uring, and bus1

**原文链接**: [https://lwn.net/Articles/1065490/](https://lwn.net/Articles/1065490/)

生成摘要时出错

---

## 27. AI chatbots could be making you stupider

**原文标题**: AI chatbots could be making you stupider

**原文链接**: [https://www.bbc.com/future/article/20260417-ai-chatbots-could-be-making-you-stupider](https://www.bbc.com/future/article/20260417-ai-chatbots-could-be-making-you-stupider)

生成摘要时出错

---

## 28. I Made the "Next-Level" Camera and I love it

**原文标题**: I Made the "Next-Level" Camera and I love it

**原文链接**: [https://thelibre.news/i-made-the-next-level-camera-and-i-love-it/](https://thelibre.news/i-made-the-next-level-camera-and-i-love-it/)

生成摘要时出错

---

## 29. SDF Public Access Unix System

**原文标题**: SDF Public Access Unix System

**原文链接**: [https://sdf.org/?ssh](https://sdf.org/?ssh)

生成摘要时出错

---

## 30. Claude Token Counter, now with model comparisons

**原文标题**: Claude Token Counter, now with model comparisons

**原文链接**: [https://simonwillison.net/2026/Apr/20/claude-token-counts/](https://simonwillison.net/2026/Apr/20/claude-token-counts/)

生成摘要时出错

---

## 31. Epicycles All the Way Down (2025)

**原文标题**: Epicycles All the Way Down (2025)

**原文链接**: [https://www.strangeloopcanon.com/p/epicycles-all-the-way-down](https://www.strangeloopcanon.com/p/epicycles-all-the-way-down)

生成摘要时出错

---

## 32. What if database branching was easy?

**原文标题**: What if database branching was easy?

**原文链接**: [https://xata.io/blog/what-if-database-branching-was-easy](https://xata.io/blog/what-if-database-branching-was-easy)

生成摘要时出错

---

## 33. Zero-copy protobuf and ConnectRPC for Rust

**原文标题**: Zero-copy protobuf and ConnectRPC for Rust

**原文链接**: [https://medium.com/@iainmcgin/zero-copy-protobuf-and-connectrpc-for-rust-69bda8ac0f02](https://medium.com/@iainmcgin/zero-copy-protobuf-and-connectrpc-for-rust-69bda8ac0f02)

生成摘要时出错

---

## 34. How Motorola’s 2N2222 and 2N3904 transistors became the default NPNs

**原文标题**: How Motorola’s 2N2222 and 2N3904 transistors became the default NPNs

**原文链接**: [https://www.allaboutcircuits.com/news/how-two-motorola-transistors-became-the-worlds-default-npns/](https://www.allaboutcircuits.com/news/how-two-motorola-transistors-became-the-worlds-default-npns/)

生成摘要时出错

---

## 35. Forbes Prediction Market Gamefies Story About Mass Shooting of 8 Children

**原文标题**: Forbes Prediction Market Gamefies Story About Mass Shooting of 8 Children

**原文链接**: [https://www.404media.co/forbes-prediction-market-gamefies-story-about-mass-shooting-of-8-children/](https://www.404media.co/forbes-prediction-market-gamefies-story-about-mass-shooting-of-8-children/)

生成摘要时出错

---

## 36. The Abstraction Fallacy: Why AI Can Simulate but Not Instantiate Consciousness

**原文标题**: The Abstraction Fallacy: Why AI Can Simulate but Not Instantiate Consciousness

**原文链接**: [https://deepmind.google/research/publications/231971/](https://deepmind.google/research/publications/231971/)

生成摘要时出错

---

## 37. Stop trying to engineer your way out of listening to people

**原文标题**: Stop trying to engineer your way out of listening to people

**原文链接**: [https://ashley.rolfmore.com/stop-trying-to-engineer-your-way-out-of-listening-to-people/](https://ashley.rolfmore.com/stop-trying-to-engineer-your-way-out-of-listening-to-people/)

生成摘要时出错

---

## 38. NASA Artemis Posters

**原文标题**: NASA Artemis Posters

**原文链接**: [https://www.nasa.gov/gallery/artemis/](https://www.nasa.gov/gallery/artemis/)

生成摘要时出错

---

## 39. Palantir Wants to Reinstate the Draft

**原文标题**: Palantir Wants to Reinstate the Draft

**原文链接**: [https://reason.com/2026/04/20/this-big-tech-firm-wants-to-reinstate-the-draft/](https://reason.com/2026/04/20/this-big-tech-firm-wants-to-reinstate-the-draft/)

生成摘要时出错

---

## 40. Monumental ship burial beneath ancient Norwegian mound predates the Viking Age

**原文标题**: Monumental ship burial beneath ancient Norwegian mound predates the Viking Age

**原文链接**: [https://phys.org/news/2026-04-monumental-ship-burial-beneath-ancient.html](https://phys.org/news/2026-04-monumental-ship-burial-beneath-ancient.html)

生成摘要时出错

---

## 41. Allbirds' Move to AI Has Echoes of the Dot-Com Frenzy

**原文标题**: Allbirds' Move to AI Has Echoes of the Dot-Com Frenzy

**原文链接**: [https://www.bloomberg.com/news/newsletters/2026-04-20/allbirds-pivot-to-ai-stirs-memory-of-dot-com-boom-and-bust](https://www.bloomberg.com/news/newsletters/2026-04-20/allbirds-pivot-to-ai-stirs-memory-of-dot-com-boom-and-bust)

生成摘要时出错

---

## 42. Stripe's Payment APIs: the first 10 years (2020)

**原文标题**: Stripe's Payment APIs: the first 10 years (2020)

**原文链接**: [https://stripe.dev/blog/payment-api-design](https://stripe.dev/blog/payment-api-design)

生成摘要时出错

---

## 43. Kimi K2.6: Advancing Open-Source Coding

**原文标题**: Kimi K2.6: Advancing Open-Source Coding

**原文链接**: [https://twitter.com/Kimi_Moonshot/status/2046249571882500354](https://twitter.com/Kimi_Moonshot/status/2046249571882500354)

生成摘要时出错

---

## 44. Mechanical Keyboard Sounds – A listening Museum

**原文标题**: Mechanical Keyboard Sounds – A listening Museum

**原文链接**: [https://sheets.works/data-viz/keyboard-sounds](https://sheets.works/data-viz/keyboard-sounds)

生成摘要时出错

---

## 45. Who Is Blake Whiting?

**原文标题**: Who Is Blake Whiting?

**原文链接**: [https://theamericanscholar.org/who-is-blake-whiting/](https://theamericanscholar.org/who-is-blake-whiting/)

生成摘要时出错

---

## 46. Cahokia

**原文标题**: Cahokia

**原文链接**: [https://en.wikipedia.org/wiki/Cahokia](https://en.wikipedia.org/wiki/Cahokia)

生成摘要时出错

---

## 47. Vercel April 2026 security incident

**原文标题**: Vercel April 2026 security incident

**原文链接**: [https://www.bleepingcomputer.com/news/security/vercel-confirms-breach-as-hackers-claim-to-be-selling-stolen-data/](https://www.bleepingcomputer.com/news/security/vercel-confirms-breach-as-hackers-claim-to-be-selling-stolen-data/)

生成摘要时出错

---

## 48. Scientific datasets are riddled with copy-paste errors

**原文标题**: Scientific datasets are riddled with copy-paste errors

**原文链接**: [https://www.sciencedetective.org/scientific-datasets-are-riddled-with-copy-paste-errors/](https://www.sciencedetective.org/scientific-datasets-are-riddled-with-copy-paste-errors/)

生成摘要时出错

---

## 49. Baltic nations brace for impact of Iran war delaying US weapons shipments

**原文标题**: Baltic nations brace for impact of Iran war delaying US weapons shipments

**原文链接**: [https://www.defensenews.com/global/europe/2026/04/20/baltic-nations-brace-for-impact-of-iran-war-delaying-us-weapons-shipments/](https://www.defensenews.com/global/europe/2026/04/20/baltic-nations-brace-for-impact-of-iran-war-delaying-us-weapons-shipments/)

生成摘要时出错

---

## 50. Turning a Chinese IoT camera into an owl livestream

**原文标题**: Turning a Chinese IoT camera into an owl livestream

**原文链接**: [https://blog.alexbeals.com/posts/owl-cam](https://blog.alexbeals.com/posts/owl-cam)

生成摘要时出错

---

## 51. EV sales soar in main European markets as drivers shun expensive petrol

**原文标题**: EV sales soar in main European markets as drivers shun expensive petrol

**原文链接**: [https://www.reuters.com/sustainability/climate-energy/ev-sales-soar-main-european-markets-drivers-shun-expensive-petrol-2026-04-19/](https://www.reuters.com/sustainability/climate-energy/ev-sales-soar-main-european-markets-drivers-shun-expensive-petrol-2026-04-19/)

生成摘要时出错

---

## 52. IEA: Solar overtakes all energy sources in a major global first

**原文标题**: IEA: Solar overtakes all energy sources in a major global first

**原文链接**: [https://electrek.co/2026/04/19/iea-solar-overtakes-all-energy-sources-in-a-major-global-first/](https://electrek.co/2026/04/19/iea-solar-overtakes-all-energy-sources-in-a-major-global-first/)

生成摘要时出错

---

## 53. Ben Lerner's Big Feelings

**原文标题**: Ben Lerner's Big Feelings

**原文链接**: [https://www.vulture.com/article/ben-lerner-transcription-interview.html](https://www.vulture.com/article/ben-lerner-transcription-interview.html)

生成摘要时出错

---

## 54. A cache-friendly IPv6 LPM with AVX-512 (linearized B+-tree, real BGP benchmarks)

**原文标题**: A cache-friendly IPv6 LPM with AVX-512 (linearized B+-tree, real BGP benchmarks)

**原文链接**: [https://github.com/esutcu/planb-lpm](https://github.com/esutcu/planb-lpm)

生成摘要时出错

---

## 55. Brave Origin

**原文标题**: Brave Origin

**原文链接**: [https://support.brave.app/hc/en-us/articles/38561489788173-What-is-Brave-Origin](https://support.brave.app/hc/en-us/articles/38561489788173-What-is-Brave-Origin)

生成摘要时出错

---

## 56. What we once had (at the height of the XMPP era of the Internet) (2023)

**原文标题**: What we once had (at the height of the XMPP era of the Internet) (2023)

**原文链接**: [https://www.kirsle.net/what-we-once-had-at-the-height-of-the-xmpp-era-of-the-internet](https://www.kirsle.net/what-we-once-had-at-the-height-of-the-xmpp-era-of-the-internet)

生成摘要时出错

---

## 57. Wife Acceptance Factor

**原文标题**: Wife Acceptance Factor

**原文链接**: [https://en.wikipedia.org/wiki/Wife_acceptance_factor](https://en.wikipedia.org/wiki/Wife_acceptance_factor)

生成摘要时出错

---

## 58. Users unable to load ChatGPT, Codex and API Platform

**原文标题**: Users unable to load ChatGPT, Codex and API Platform

**原文链接**: [https://status.openai.com/incidents/01KPNN2V2SMP3TAN3MCJK87W50](https://status.openai.com/incidents/01KPNN2V2SMP3TAN3MCJK87W50)

生成摘要时出错

---

## 59. Show HN: Faceoff – A terminal UI for following NHL games

**原文标题**: Show HN: Faceoff – A terminal UI for following NHL games

**原文链接**: [https://www.vincentgregoire.com/faceoff/](https://www.vincentgregoire.com/faceoff/)

生成摘要时出错

---

## 60. Hot-wiring the Lisp machine

**原文标题**: Hot-wiring the Lisp machine

**原文链接**: [https://scheatkode.com/blog/019d463d-38b3-7e63-80fd-6ed97bd8815e/hot-wiring-the-lisp-machine/](https://scheatkode.com/blog/019d463d-38b3-7e63-80fd-6ed97bd8815e/hot-wiring-the-lisp-machine/)

生成摘要时出错

---

## 61. No Lines, No 'Regular' People: Flying Ultra-Luxury from Paris

**原文标题**: No Lines, No 'Regular' People: Flying Ultra-Luxury from Paris

**原文链接**: [https://www.nytimes.com/2026/04/06/travel/first-class-luxury-flight-air-france-la-premiere.html](https://www.nytimes.com/2026/04/06/travel/first-class-luxury-flight-air-france-la-premiere.html)

生成摘要时出错

---

## 62. Game devs explain the tricks involved with letting you pause a game

**原文标题**: Game devs explain the tricks involved with letting you pause a game

**原文链接**: [https://kotaku.com/video-game-devs-explain-how-pausing-works-and-sometimes-it-gets-weird-2000686339](https://kotaku.com/video-game-devs-explain-how-pausing-works-and-sometimes-it-gets-weird-2000686339)

生成摘要时出错

---

## 63. Judge sides with ICE tracker creators in DHS/DOJ First Amendment lawsuit

**原文标题**: Judge sides with ICE tracker creators in DHS/DOJ First Amendment lawsuit

**原文链接**: [https://www.engadget.com/apps/judge-sides-with-creators-of-banned-ice-trackers-who-allege-dhs-and-doj-violated-their-first-amendment-rights-191701801.html](https://www.engadget.com/apps/judge-sides-with-creators-of-banned-ice-trackers-who-allege-dhs-and-doj-violated-their-first-amendment-rights-191701801.html)

生成摘要时出错

---

## 64. The creative software industry has declared war on Adobe

**原文标题**: The creative software industry has declared war on Adobe

**原文链接**: [https://www.theverge.com/tech/913765/adobe-rivals-free-creative-software-app-updates](https://www.theverge.com/tech/913765/adobe-rivals-free-creative-software-app-updates)

生成摘要时出错

---

## 65. Show HN: Shader Lab, like Photoshop but for shaders

**原文标题**: Show HN: Shader Lab, like Photoshop but for shaders

**原文链接**: [https://eng.basement.studio/tools/shader-lab](https://eng.basement.studio/tools/shader-lab)

生成摘要时出错

---

## 66. Interesting Map Geometry and Mathematics

**原文标题**: Interesting Map Geometry and Mathematics

**原文链接**: [https://www.markrjohnsongames.com/2026/04/11/ultima-ratio-regum-0-11-update-57-interesting-map-geometry-and-mathematics/](https://www.markrjohnsongames.com/2026/04/11/ultima-ratio-regum-0-11-update-57-interesting-map-geometry-and-mathematics/)

生成摘要时出错

---

## 67. Offshore tax tricks likely saved Tesla hundreds of millions

**原文标题**: Offshore tax tricks likely saved Tesla hundreds of millions

**原文链接**: [https://www.reuters.com/legal/transactional/musk-scorned-shady-loopholes-yet-offshore-tax-tricks-likely-saved-tesla-hundreds-2026-04-20/](https://www.reuters.com/legal/transactional/musk-scorned-shady-loopholes-yet-offshore-tax-tricks-likely-saved-tesla-hundreds-2026-04-20/)

生成摘要时出错

---

## 68. College instructor turns to typewriters to curb AI-written work

**原文标题**: College instructor turns to typewriters to curb AI-written work

**原文链接**: [https://sentinelcolorado.com/uncategorized/a-college-instructor-turns-to-typewriters-to-curb-ai-written-work-and-teach-life-lessons/](https://sentinelcolorado.com/uncategorized/a-college-instructor-turns-to-typewriters-to-curb-ai-written-work-and-teach-life-lessons/)

生成摘要时出错

---

## 69. The seven programming ur-languages (2022)

**原文标题**: The seven programming ur-languages (2022)

**原文链接**: [https://madhadron.com/programming/seven_ur_languages.html](https://madhadron.com/programming/seven_ur_languages.html)

生成摘要时出错

---

## 70. It's cool to care (2025)

**原文标题**: It's cool to care (2025)

**原文链接**: [https://alexwlchan.net/2025/cool-to-care/](https://alexwlchan.net/2025/cool-to-care/)

生成摘要时出错

---

## 71. WhatsApp Plus is rolling out new premium features

**原文标题**: WhatsApp Plus is rolling out new premium features

**原文链接**: [https://wabetainfo.com/whatsapp-plus-is-rolling-out-new-premium-features/](https://wabetainfo.com/whatsapp-plus-is-rolling-out-new-premium-features/)

生成摘要时出错

---

## 72. Advancing human gut microbiota research by considering gut transit time (2023)

**原文标题**: Advancing human gut microbiota research by considering gut transit time (2023)

**原文链接**: [https://gut.bmj.com/content/72/1/180](https://gut.bmj.com/content/72/1/180)

生成摘要时出错

---

## 73. PopOS Linux: Creating a Bootable Backup USB With Encryption

**原文标题**: PopOS Linux: Creating a Bootable Backup USB With Encryption

**原文链接**: [https://hajo.me/blog/2026/02/16/popos-linux-creating-bootable-backup-USB-with-encryption/](https://hajo.me/blog/2026/02/16/popos-linux-creating-bootable-backup-USB-with-encryption/)

生成摘要时出错

---

## 74. Archive of BYTE magazine, starting with issue #1 in 1975

**原文标题**: Archive of BYTE magazine, starting with issue #1 in 1975

**原文链接**: [https://archive.org/details/byte-magazine-1975-09](https://archive.org/details/byte-magazine-1975-09)

生成摘要时出错

---

## 75. NIST scientists create 'any wavelength' lasers

**原文标题**: NIST scientists create 'any wavelength' lasers

**原文链接**: [https://www.nist.gov/news-events/news/2026/04/any-color-you-nist-scientists-create-any-wavelength-lasers-tiny-circuits](https://www.nist.gov/news-events/news/2026/04/any-color-you-nist-scientists-create-any-wavelength-lasers-tiny-circuits)

生成摘要时出错

---

## 76. Reverse Engineering ME2's USB with a Heat Gun and a Knife

**原文标题**: Reverse Engineering ME2's USB with a Heat Gun and a Knife

**原文链接**: [https://github.com/coremaze/ME2-Writeup](https://github.com/coremaze/ME2-Writeup)

生成摘要时出错

---

## 77. Most people care about farm animals – our food system doesn't reflect that

**原文标题**: Most people care about farm animals – our food system doesn't reflect that

**原文链接**: [https://ourworldindata.org/most-people-care-about-farm-animals-our-food-system-doesnt-reflect-that](https://ourworldindata.org/most-people-care-about-farm-animals-our-food-system-doesnt-reflect-that)

生成摘要时出错

---

## 78. Anonymous request-token comparisons from Opus 4.6 and Opus 4.7

**原文标题**: Anonymous request-token comparisons from Opus 4.6 and Opus 4.7

**原文链接**: [https://tokens.billchambers.me/leaderboard](https://tokens.billchambers.me/leaderboard)

生成摘要时出错

---

## 79. What are skiplists good for?

**原文标题**: What are skiplists good for?

**原文链接**: [https://antithesis.com/blog/2026/skiptrees/](https://antithesis.com/blog/2026/skiptrees/)

生成摘要时出错

---

## 80. Why Japan has such good railways

**原文标题**: Why Japan has such good railways

**原文链接**: [https://worksinprogress.co/issue/why-japan-has-such-good-railways/](https://worksinprogress.co/issue/why-japan-has-such-good-railways/)

生成摘要时出错

---

## 81. Reading Input from an USB RFID Card Reader

**原文标题**: Reading Input from an USB RFID Card Reader

**原文链接**: [https://kevwe.com/blog/usb-rfid-reader](https://kevwe.com/blog/usb-rfid-reader)

生成摘要时出错

---

## 82. The electromechanical angle computer inside the B-52 bomber's star tracker

**原文标题**: The electromechanical angle computer inside the B-52 bomber's star tracker

**原文链接**: [https://www.righto.com/2026/04/B-52-star-tracker-angle-computer.html](https://www.righto.com/2026/04/B-52-star-tracker-angle-computer.html)

生成摘要时出错

---

## 83. Claude Design

**原文标题**: Claude Design

**原文链接**: [https://www.anthropic.com/news/claude-design-anthropic-labs](https://www.anthropic.com/news/claude-design-anthropic-labs)

生成摘要时出错

---

## 84. Giving RISC-V 1024 registers for zkVMs

**原文标题**: Giving RISC-V 1024 registers for zkVMs

**原文链接**: [https://leonardoalt.github.io/riscv-x](https://leonardoalt.github.io/riscv-x)

生成摘要时出错

---

## 85. Show HN: MDV – a Markdown superset for docs, dashboards, and slides with data

**原文标题**: Show HN: MDV – a Markdown superset for docs, dashboards, and slides with data

**原文链接**: [https://github.com/drasimwagan/mdv](https://github.com/drasimwagan/mdv)

生成摘要时出错

---

## 86. A Common MVP Evolution: Service to System Integration to Product (2017)

**原文标题**: A Common MVP Evolution: Service to System Integration to Product (2017)

**原文链接**: [https://www.skmurphy.com/blog/2017/08/07/a-common-evolution-service-to-system-integration-to-product/](https://www.skmurphy.com/blog/2017/08/07/a-common-evolution-service-to-system-integration-to-product/)

生成摘要时出错

---

## 87. Scientists discover “cleaner ants” that groom giant ants in Arizona desert

**原文标题**: Scientists discover “cleaner ants” that groom giant ants in Arizona desert

**原文链接**: [https://www.sciencedaily.com/releases/2026/04/260414075641.htm](https://www.sciencedaily.com/releases/2026/04/260414075641.htm)

生成摘要时出错

---

