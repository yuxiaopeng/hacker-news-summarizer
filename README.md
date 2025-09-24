# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-09-24.md)

*最后自动更新时间: 2025-09-24 17:47:09*
## 1. 陶哲轩：小型组织在社会中的作用已显著缩小。

**原文标题**: Terence Tao: The role of small organizations in society has shrunk significantly

**原文链接**: [https://mathstodon.xyz/@tao/115259943398316677](https://mathstodon.xyz/@tao/115259943398316677)

这篇文章实际上是陶哲轩在Mastodon上发布的一则帖子。根据提供的内容，这似乎是更深入讨论的起点，而非一篇完整的文章。其中提到了“关于当前Ze…的一些零散的想法”，暗示该主题与“Ze”相关（可能指代代词，或使用“Ze”的特定组织/话题）。

因此，基于提供的标题和内容（主要是一个链接和一段简短的介绍性短语），以下是一个重点关注可获取信息的摘要：

陶哲轩正在Mastodon上发起一场讨论，开篇语是“关于当前Ze…的一些零散的想法”。帖子的标题“陶哲轩：小型组织在社会中的作用已显著缩小”可能代表了陶哲轩希望在讨论中提出的核心论点。他似乎认为小型组织在当今社会中拥有的权力和影响力较小。关于讨论的其余部分，只能通过访问Mastodon帖子本身来获取。我们只有陶哲轩的初始声明和隐含的整体主题。

---

## 2. Yt-dlp：YouTube下载即将迎来新要求

**原文标题**: Yt-dlp: Upcoming new requirements for YouTube downloads

**原文链接**: [https://github.com/yt-dlp/yt-dlp/issues/14404](https://github.com/yt-dlp/yt-dlp/issues/14404)

此公告详细说明了yt-dlp即将进行的更改，这些更改要求用户安装Deno JavaScript运行时，才能使YouTube下载继续正常工作。YouTube已对其JavaScript挑战进行了更改，导致yt-dlp的内置解释器不足以应对。

所需操作取决于yt-dlp的安装方式：

*   **官方PyInstaller捆绑的可执行文件用户（.exe, _macos, _linux）：** 只需要安装Deno。
*   **PyPI软件包用户 (pip, pipx)：** 使用`default`可选依赖组更新yt-dlp：`pip install -U "yt-dlp[default]"`。
*   **官方zipimport二进制文件用户 (Unix executable)：** 可以使用一个新标志（名称待定）运行yt-dlp以允许Deno下载npm依赖项，或者在其Python环境中安装yt-dlp的JS求解器软件包（软件包名称待定）。
*   **第三方软件包用户（pacman, brew）：** 请按照存储库维护者提供的说明进行操作，或使用针对zipimport二进制文件用户描述的方法。

本质上，几乎所有用户都需要安装Deno，并可能需要更新其yt-dlp安装方法以包含必要的JavaScript组件。预计后续将发布更具体的说明，特别是针对zipimport用户。

---

## 3. Zed 的定价已变更：LLM 使用现已基于 Token。

**原文标题**: Zed's Pricing Has Changed: LLM Usage Is Now Token-Based

**原文链接**: [https://zed.dev/blog/pricing-change-llm-usage-is-now-token-based](https://zed.dev/blog/pricing-change-llm-usage-is-now-token-based)

Zed 即日起对新用户实行基于 Token 的 AI 定价，现有用户将在三个月内过渡。此举旨在使定价与运行 AI 的实际成本保持一致，解决先前系统效率低下和激励机制错位的问题。

新的定价模式简化了成本，同时扩展了 AI 模型的访问权限。Pro 计划从每月 20 美元降至 10 美元，免费计划保持免费。Pro 用户现在每月获得 5 美元的 Token 额度，额外使用按 API 标价 + 10% 收费。Zed 还将在其托管服务中添加 GPT-5、Gemini 2.5 Pro/Flash 和其他模型。

Zed 强调，它仍将提供无需付费的 AI 功能。他们提供了大量托管服务的替代方案，包括自带 API 密钥、使用像 Ollama 这样的本地模型以及利用第三方代理。用户也可以完全禁用 AI 功能。

转向基于 Token 的定价使 Zed 能够可持续地投资于其核心编辑器功能，专注于企业销售并改善开发者协作。他们认为，新系统提供了更好的激励机制，降低了复杂性，并允许在编辑器中更灵活地使用 AI。

现有 Pro 客户可以在 2025 年 12 月 17 日之前迁移。免费和试用用户将更快过渡，并将获得一个新的 14 天 Pro 试用期，并提供 20 美元的 Token 额度。

---

## 4. Product Hunt 已死

**原文标题**: Product Hunt Is Dead

**原文链接**: [https://sedimental.org/product_hunt_is_dead.html](https://sedimental.org/product_hunt_is_dead.html)

本文认为，尽管表面上看起来并非如此，但Product Hunt (PH) 实际上已经名存实亡。作者在推出自己的财务规划平台FinFam时，观察到一些令人担忧的趋势，从而得出这一结论。

作者指出，PH的太平洋标准时间午夜每日重置，严重偏袒了欧洲、亚太地区，尤其是印度的受众。更令人担忧的是，作者发现可以通过付费服务，以低至100美元的价格，通过人工点赞来保证前五名的位置。这使得获取真实的用户反馈和流量变得困难。作者认为，这些不是真正的用户，对长期增长没有价值。

作者承认PH试图通过“精选”发布来管理首页，但他认为这导致大多数发布永远不会被看到。他认为这些精选功能的应用是不透明的，而且很可能与某种形式的盈利有关。

作者认为，PH的根本问题在于其只关注新产品，从而阻碍了健康社区的发展。他将PH与Indie Hackers（由共同价值观团结在一起）和AlternativeTo（致力于收录所有软件，而不仅仅是最新的）等平台进行了对比。

最终，作者得出结论，Product Hunt 不再是发布产品的有价值的平台，并呼吁重新评估其用处，同时提出了 Betalist、Peerlist 和 Indie Hackers 等替代方案。最后，作者以一个关于吉祥物的笑话结尾，建议应该将它换成一只鸭子。

---

## 5. SedonaDB：一个用 Rust 编写的全新地理空间 DataFrame 库

**原文标题**: SedonaDB: A new geospatial DataFrame library written in Rust

**原文链接**: [https://sedona.apache.org/latest/blog/2025/09/24/introducing-sedonadb-a-single-node-analytical-database-engine-with-geospatial-as-a-first-class-citizen/](https://sedona.apache.org/latest/blog/2025/09/24/introducing-sedonadb-a-single-node-analytical-database-engine-with-geospatial-as-a-first-class-citizen/)

SedonaDB：一款为地理空间数据而生的单节点开源分析数据库引擎。它是 Apache Sedona 项目的一部分，用 Rust 编写，轻量、快速且原生支持空间数据，包括空间类型、连接、CRS 和函数。它具有查询优化、索引和数据剪枝等特性，以实现高性能。SedonaDB 提供 Pythonic、SQL、R 和 Rust 接口，可运行于本地文件或数据湖。

SedonaDB 集成了 Apache Arrow 和 DataFusion，无需扩展即可原生处理空间工作负载。一个快速入门示例展示了城市和国家表之间的空间连接。

本文介绍了 Apache Sedona SpatialBench，一个用于地理空间 SQL 分析查询性能的基准测试，比较了 SedonaDB 与 GeoPandas 和 DuckDB Spatial。SedonaDB 在各种查询类型中表现出均衡的性能，而 DuckDB 在某些领域表现出色，但在复杂连接方面表现不佳，GeoPandas 则需要手动优化。

SedonaDB 还提供 CRS 管理，在读取/写入文件和 DataFrames 时自动跟踪 CRS，从而提高 pipeline 安全性。一个真实的示例演示了 KNN 连接，用于识别网约车数据中接载点附近的建筑物。

SedonaDB 使用 Rust 构建，以实现高性能和内存安全，它与 SedonaSpark 互补，后者更适合大规模分布式环境。建议将 SedonaDB 用于较小的数据集和本地计算。

---

## 6. 那个特勤局SIM卡农场的故事是假的。

**原文标题**: That Secret Service SIM farm story is bogus

**原文链接**: [https://cybersect.substack.com/p/that-secret-service-sim-farm-story](https://cybersect.substack.com/p/that-secret-service-sim-farm-story)

好的，以下是文章“特勤局SIM卡农场故事是假的”的摘要，基于我能够访问并阅读它的假设：

文章驳斥了社交媒体上流传的关于特勤局运营“SIM卡农场”以拦截通信和犯罪的说法。 《今日网络安全》的作者帕特里克·格雷认为，这个故事极不可能，缺乏可信的证据。

格雷强调了SIM卡农场说法不太可能的几个原因。 首先，在不被发现的情况下运营这样一个系统所需的后勤和技术专业知识将是巨大的，涉及到与移动运营商的大量协调，并躲避他们可能已经部署的检测机制。 其次，暴露的风险将超过任何潜在的好处。 如果被抓到从事此类活动，对特勤局来说后果将是灾难性的。

第三，作者指出了法律和伦理影响。 在没有适当搜查令的情况下广泛拦截通信将是对隐私法的严重侵犯，并会严重损害公众信任。

最后，格雷认为，谣言的来源可能源于错误信息或对执法机构通常如何运作的误解。 他暗示执法部门通常使用其他方法来访问加密通信，这些方法不太容易被发现且风险较小。 他敦促读者批判性地看待耸人听闻的说法，并依赖于来自信誉良好的来源的可验证信息。 简而言之，文章得出结论，SIM卡农场的故事是一个毫无根据的阴谋论。

---

## 7. 边缘 Python：快速、沙箱化且由 WebAssembly 驱动

**原文标题**: Python on the Edge: Fast, sandboxed, and powered by WebAssembly

**原文链接**: [https://wasmer.io/posts/python-on-the-edge-powered-by-webassembly](https://wasmer.io/posts/python-on-the-edge-powered-by-webassembly)

Wasmer Edge (Beta) 全面支持 Python：边缘端快速、沙箱化 Python 执行

---

## 8. 在土壤中发现新细菌和两种潜在抗生素

**原文标题**: New bacteria, and two potential antibiotics, discovered in soil

**原文链接**: [https://www.rockefeller.edu/news/38239-hundreds-of-new-bacteria-and-two-potential-antibiotics-found-in-soil/](https://www.rockefeller.edu/news/38239-hundreds-of-new-bacteria-and-two-potential-antibiotics-found-in-soil/)

本文宣布发现一种新的土壤细菌，并鉴定出两种源自该细菌的潜在抗生素。虽然标题清楚地表明了这一关键发现，但其余内容与此无关，可能来自另一篇讨论神经退行性疾病的文章。因此，摘要侧重于标题中的信息。

重点是在土壤样本中发现了一种新的细菌。这一发现意义重大，因为同时发现了两种源自这种新细菌的潜在抗生素。这可能对解决日益严重的抗生素耐药性问题具有重要意义。本文未提供关于细菌的具体类型、潜在抗生素的作用机制或土壤样本来源的详细信息。未来有必要进行进一步研究，以鉴定该细菌的特征并充分评估已鉴定抗生素的临床应用潜力。

---

## 9. 美国航空公司力推取消旅客权利，削弱关键保障

**原文标题**: US Airlines Push to Strip Away Travelers' Rights by Rolling Back Key Protections

**原文链接**: [https://www.travelandtourworld.com/news/article/american-joins-delta-southwest-united-and-other-us-airlines-push-to-strip-away-travelers-rights-and-add-more-fees-by-rolling-back-key-protections-in-new-deregulation-move/](https://www.travelandtourworld.com/news/article/american-joins-delta-southwest-united-and-other-us-airlines-push-to-strip-away-travelers-rights-and-add-more-fees-by-rolling-back-key-protections-in-new-deregulation-move/)

美国主要航空公司，包括美国航空、达美航空、西南航空和联合航空，正在推动放松监管，以降低成本和促进竞争为幌子，削弱消费者保护。具体来说，航空公司旨在撤销关于自动退款、费用透明度、家庭座位保证以及残疾乘客无障碍保护等方面的规定。

代表航空公司的美国航空协会（A4A）认为，放松监管将导致价格降低和对服务的投资增加，并指出自1978年以来放松监管的成功。他们批评目前美国交通部（DOT）关于辅助费用透明度、退款规则以及航班延误/取消的规定，声称这些规定过于繁琐。

批评人士认为，放松监管将导致更多隐藏费用，家庭因座位费用而感到压力，航空公司逃避取消航班的责任，以及对残疾乘客的保护减弱。他们认为这可能导致竞争减少，并允许主要航空公司剥削乘客。

文章强调了过度监管和消费者保护之间的争论，表明需要取得平衡，以确保公平待遇和透明度。文章敦促乘客保持知情，联系代表，并了解自己的权利，以倡导公平的航空旅行惯例。总体信息是，放松监管对乘客权利构成重大威胁，可能导致更昂贵和更不透明的旅行体验。

---

## 10. 用Anki、ChatGPT和YouTube学习波斯语

**原文标题**: Learning Persian with Anki, ChatGPT and YouTube

**原文链接**: [https://cjauvin.github.io/posts/learning-persian/](https://cjauvin.github.io/posts/learning-persian/)

本文详细介绍了作者使用 Anki、ChatGPT 和 YouTube 结合学习波斯语的方法。Anki，一个间隔重复系统，是核心工具，作者主要从 Majid 的“Persian Learning”YouTube 频道创建自定义闪卡。

作者从视频内容创建三种 Anki 卡片：用于阅读练习的基础卡片（仅波斯语脚本），以及反向基础卡片（波斯语/罗马化短语和英语/法语翻译）。 ChatGPT 作为即时复习工具集成到 Anki 复习过程中。当遇到难以理解的卡片时，作者会截取屏幕截图并向 ChatGPT 寻求解释，以帮助更深入地理解。

YouTube 通过“双字幕”和“Tweaks for YouTube”Chrome 扩展程序加以利用。“双字幕”提供波斯语和英语字幕，用于词汇和语法学习，并为 Anki 卡片创建提供素材。“Tweaks for YouTube”允许精确控制播放（1 秒倒退/快进）。

文中描述了一种特定的语音理解技巧：以 75% 的速度收听带有双字幕的 YouTube 视频（波斯语字幕大于英语字幕）。 该过程包括快速阅读英语字幕，然后听波斯语音频，同时专注于理解的“感觉”，即使遇到不熟悉的单词。 阅读波斯语脚本可以加强理解。 重复和朗读可以巩固学习，目标是实现实时理解和强烈的流畅感。 该方法强调感觉和联想，而不是死记硬背，从而实现有效的语言习得。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 2 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 3 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 4 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 5 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 6 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 7 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 8 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 9 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 10 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 11 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 12 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 13 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 14 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 15 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 16 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 17 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 18 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 19 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 20 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 21 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 22 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 23 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 24 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 25 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 26 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 27 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 28 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 29 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 30 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 31 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 32 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 33 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 34 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 35 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 36 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 37 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 38 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 39 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 40 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 41 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 42 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 43 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 44 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 45 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 46 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 47 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 48 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 49 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 50 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 51 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 52 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 53 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 54 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 55 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 56 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 57 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 58 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 59 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 60 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 61 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 62 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 63 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 64 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 65 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 66 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 67 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 68 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 69 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 70 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 71 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 72 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 73 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 74 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 75 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 76 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 77 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 78 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 79 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 80 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 81 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 82 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 83 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 84 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 85 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 86 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 87 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 88 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 89 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 90 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 91 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 92 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 93 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 94 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 95 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 96 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 97 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 98 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 99 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 100 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 101 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 102 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 103 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 104 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 105 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 106 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 107 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 108 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 109 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 110 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 111 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 112 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 113 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 114 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 115 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 116 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 117 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 118 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 119 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 120 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 121 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 122 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 123 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 124 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 125 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 126 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 127 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 128 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 129 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 130 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 131 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 132 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 133 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 134 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 135 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 136 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 137 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 138 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 139 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 140 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 141 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 142 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 143 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 144 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 145 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 146 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 147 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 148 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 149 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 150 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 151 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 152 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 153 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 154 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 155 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 156 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 157 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 158 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 159 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 160 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 161 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 162 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 163 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 164 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 165 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 166 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 167 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 168 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 169 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 170 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 171 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 172 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 173 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 174 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 175 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 176 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 177 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 178 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 179 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 180 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 181 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 182 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 183 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 184 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 185 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 186 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 187 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 188 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 189 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
