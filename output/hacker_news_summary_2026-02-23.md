# Hacker News 热门文章摘要 (2026-02-23)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 年龄验证陷阱：年龄验证削弱了每个人的数据保护。

**原文标题**: The Age Verification Trap: Verifying age undermines everyone's data protection

**原文链接**: [https://spectrum.ieee.org/age-verification](https://spectrum.ieee.org/age-verification)

在《年龄验证陷阱》一文中，韦戴尔·D·卡瓦略（Waydell D. Carvalho）指出，政府强制执行的年龄验证（AV）系统虽然旨在保护未成年人免受有害内容侵害，但却给所有互联网用户带来了显著的隐私和安全风险。卡瓦略认为，这些强制令将数字环境从伪匿名状态转变为持续监控状态。

作者的核心观点总结如下：

*   **隐私侵蚀：** 年龄验证通常要求用户提供敏感信息，如政府颁发的身份证件或生物识别数据（面部扫描）。这迫使个人为了获得数字服务而放弃匿名性，从而形成了一个对黑客和身份窃贼极具吸引力的敏感数据“蜜罐”。
*   **伪匿名的终结：** 通过将个人的法律身份与其在线行为挂钩，年龄验证允许平台和第三方验证者追踪私人浏览习惯、兴趣和归属关系。这些数据可能被用于用户画像或政府监控。
*   **无效性与规避：** 卡瓦略指出，精通技术的未成年人经常利用 VPN 或“灰色市场”账户轻松绕过年龄验证。因此，这些系统未能保护其目标群体，却剥夺了守法成年人的隐私权。
*   **中心化风险：** 许多年龄验证解决方案依赖第三方供应商，导致了中心化的单点故障。如果主要的验证枢纽遭到入侵，数百万用户的个人身份信息都将面临泄露风险。

**结论：**
卡瓦略主张采用“安全源于设计”和去中心化的设备端控制，而非中心化的身份检查。他建议，重点应放在赋予家长权利以及利用浏览器或操作系统层面的技术信号上，而不是建立一套破坏数据保护基本权利的永久性监控基础设施。

---

## 2. Ladybird 浏览器采用 Rust

**原文标题**: Ladybird Browser adopts Rust

**原文链接**: [https://ladybird.org/posts/adopting-rust/](https://ladybird.org/posts/adopting-rust/)

Ladybird浏览器创始人Andreas Kling宣布，该项目正式采用Rust语言替换C++，以提升内存安全性。尽管团队此前曾调研过Swift，并对Rust与旧有Web对象模型的兼容性持保留意见，但最终因其成熟的系统编程生态和强大的贡献者支持而选择了Rust。

转型从Ladybird的JavaScript引擎**LibJS**开始。Kling利用Claude Code和Codex等AI工具在人工引导下进行转换，仅用两周时间就移植了约2.5万行代码，涵盖了词法分析器、解析器和字节码生成器。这一过程原本可能需要数月时间，其核心目标是确保输出与原有的C++管线保持字节级的一致。

**关键结果包括：**
*   **零回归：** Rust实现通过了全部52,898项test262测试和12,461项内部回归测试。
*   **性能持平：** 在JS基准测试中未记录到性能损失。
*   **兼容性：** 目前的Rust代码有意模仿C++模式，以确保生成相同的字节码，未来将逐步重构为更符合Rust规范的代码。

展望未来，Ladybird不会立即放弃C++，而是让两种语言通过明确的互操作边界共存。核心团队将分阶段管理子系统的移植以确保稳定性，并要求贡献者在任何涉及Rust的新工作中进行密切协作。Kling认为，这一转变是保障浏览器长期安全性和生命力的务实且必要的一步。

---

## 3. 我们拥有的简单网络

**原文标题**: A simple web we own

**原文链接**: [https://rsdoiel.github.io/blog/2026/02/21/a_simple_web_we_own.html](https://rsdoiel.github.io/blog/2026/02/21/a_simple_web_we_own.html)

在《我们拥有的简单网络》一文中，R. S. Doiel 指出，现代互联网已退化为由大公司和政府控制的“监控经济”，将用户降格为单纯的“租户和产品”。为了对抗这种“平台颓败”（enshittification），Doiel 提议向硬件和软件的个人及协作所有权转变，并认为广泛的个人所有权可以像工会影响工业政治经济那样重塑数字格局。

文章指出，实现这一转变的一个重大障碍是人们感知的网页发布复杂性。尽管“大科技公司”维持着只有大型平台才能提供易用性的神话，但 Doiel 强调，现代工具已经简化了这一过程。具体而言，作者提倡使用 Markdown（一种简单的超文本编写方式），并结合能自动生成 HTML、RSS 提要和站点地图的软件。这种“单速自行车”方案用轻量级的静态替代方案取代了 WordPress 等复杂且耗资源的系统，使作者无需开发者级别的技能即可进行管理。

作者强调，技术和资金准入门槛已经消失。像树莓派（Raspberry Pi）这样经济实惠的硬件，让个人只需花费智能手机一小部分的成本，就能拥有自己的计算能力。通过将“互联网”（internet）和“万维网”（web）视为普通名词——即去中心化的网络之网，而非单一的公司平台——用户可以利用现有协议（IPv4/IPv6）在私有或公共网络上托管自己的内容。

最终，Doiel 总结道，通过三个核心要素即可实现“简单的网络”：
1. 个人拥有并控制的计算设备。
2. 个人控制的网络。
3. 能够赋能用户读写超文本，且无需依赖中心化中间商的简单软件。

---

## 4. 五十万个“带空格的词”未被词典收录。

**原文标题**: Half million 'Words with Spaces' missing from dictionaries

**原文链接**: [https://www.linguabase.org/words-with-spaces.html](https://www.linguabase.org/words-with-spaces.html)

在《五十万个“带空格的词”未被词典收录》一文中，作者探讨了传统词典编纂学为何忽略了数十万个作为独立语义单位运作的“多词表达”（MWEs）。像“boiling water”（开水）、“Saturday night”（周六晚上）和“paper towel”（纸巾）这类短语常因含有空格且含义被视为“透明”或显而易见，而被主流词典拒之门外。

作者是一位词汇游戏设计师，他利用大语言模型（LLMs）识别出约 77.4 万个具有特定“概念权重”的多词表达。研究揭示了一个巨大的收录缺口：诸如《韦氏词典》和《牛津词典》等传统词典仅涵盖其中约 2% 的术语，而众包的维基词典（Wiktionary）则涵盖了约 30%。

文章将这些缺失的“带空格的词”分为以下几类：
*   **透明/半透明型：** 命名特定概念的短语（如“high school/高中”、“front door/前门”）。
*   **技术型：** 行话和科学术语（如“machine learning/机器学习”）。
*   **不透明型：** 含义并非字面意思的习语（如“hot dog/热狗”、“red tape/官僚作风”）。
*   **其他：** 短语动词、成对词（如“black and white/黑白”）以及机构化短语。

作者认为，历史上对单一“构词块”单词的偏爱是印刷时代空间限制的遗留产物。实际上，“命名功能”——即一个短语唤起特定概念或事物状态的能力——才是定义单词的真正核心。通过排除多词表达，词典收窄了我们的词汇感知。对于词汇游戏和语言学而言，这些短语构成了一个有效语言的“深层蓄水池”，其功能与单一单词完全一致。这表明，空格的存在不应成为一个术语被认定为合法词汇单元的障碍。

---

## 5. Show HN: PgDog – 无需修改应用即可扩展 Postgres

**原文标题**: Show HN: PgDog – Scale Postgres without changing the app

**原文链接**: [https://github.com/pgdogdev/pgdog](https://github.com/pgdogdev/pgdog)

PgDog 是一款由 Rust 编写的高性能 PostgreSQL 代理，旨在无需更改应用层代码的情况下实现数据库扩展。它提供三大核心功能：连接池、负载均衡和分片。

作为连接池工具，PgDog 同时支持会话级和事务级连接池。与 PgBouncer 不同，它通过解析 `SET` 语句和启动选项，在共享连接时能够正确维护会话状态。在负载均衡方面，它运行在应用层（L7），利用原生 PostgreSQL 解析器自动将写操作路由至主库，将读操作路由至从库。此外，它还包含实时健康检查功能，并通过监控复制状态支持故障转移编排。

该工具最显著的特性是其水平分片能力。它支持基于分区（哈希、列表、范围）和基于模式（Schema）的分片。PgDog 通过在内存中汇聚并转换结果来处理复杂的跨分片查询，从而向客户端呈现统一的视图。高级分片功能包括：

*   **二阶段提交 (2PC)：** 确保跨多个分片的原子写入。
*   **在线重分片：** 利用逻辑复制在不停机的情况下迁移或拆分数据。
*   **查询重写：** 自动处理分片键更新，并将多行插入语句拆分到不同的分片。
*   **唯一 ID 生成：** 提供一种基于时间戳的算法，无需跨分片序列即可生成唯一的 BIGINT 标识符。

PgDog 已达到生产级标准，可通过 Kubernetes (Helm)、AWS (ECS/EKS) 或 Docker 进行部署。它兼容标准 PostgreSQL 客户端，并通过 OpenMetrics 端点和类似 PgBouncer 的管理界面提供监控。其解析 SQL 的能力使其能够处理复杂的路由逻辑（例如识别只读事务），同时在通用硬件上保持极高的吞吐量。

---

## 6. 古DNA研究：“维京”是一种职业描述，而非血统问题。

**原文标题**: 'Viking' was a job description, not a matter of heredity: Ancient DNA study

**原文链接**: [https://www.science.org/content/article/viking-was-job-description-not-matter-heredity-massive-ancient-dna-study-shows](https://www.science.org/content/article/viking-was-job-description-not-matter-heredity-massive-ancient-dna-study-shows)

A massive DNA study of 442 ancient human genomes, published in *Nature*, reveals that "Viking" was a job description and cultural identity rather than a specific hereditary ethnic group. The research, spanning the Viking Age (c. 750–1050 C.E.), debunks the 19th-century myth of a genetically "pure" Viking race.

Key findings include:

*   **Genetic Diversity:** Viking identity was not restricted to people of Scandinavian ancestry. The study found individuals with Pictish and Saami heritage buried with Viking honors, indicating that outsiders could adopt the lifestyle and be fully integrated into the culture.
*   **Diverse Physical Traits:** Contrary to the "blonde-haired, blue-eyed" stereotype, many Vikings had brown hair and varied genetic backgrounds influenced by contact with Southern Europe and Asia. 
*   **Specific Migration Routes:** The study tracked distinct genetic "streams." Individuals from present-day Norway primarily migrated to Ireland, Iceland, and Greenland; those from Denmark largely headed to England; and Swedes moved eastward toward the Baltic regions and beyond.
*   **Internal Scandinavian Differences:** Genetics within Scandinavia were more diverse than previously thought. Coastal regions showed significant gene flow from outside sources due to trade, while inland populations remained more isolated.
*   **Social Structure:** Analysis of a famous burial in Estonia revealed that raiding parties often consisted of close kin, including a group of four brothers who died together.

Ultimately, the study redefines the Viking Age as a period of intense cross-cultural exchange. It demonstrates that the Viking phenomenon was driven by a mobile, maritime culture that attracted people from various genetic backgrounds, united by shared goals and a common way of life rather than shared bloodlines.

---

## 7. Elsevier shuts down its finance journal citation cartel

**原文标题**: Elsevier shuts down its finance journal citation cartel

**原文链接**: [https://www.chrisbrunet.com/p/elsevier-shuts-down-its-finance-journal](https://www.chrisbrunet.com/p/elsevier-shuts-down-its-finance-journal)

生成摘要时出错

---

## 8. Hadrius (YC W23) Is Hiring Designers Who Code

**原文标题**: Hadrius (YC W23) Is Hiring Designers Who Code

**原文链接**: [https://www.ycombinator.com/companies/hadrius/jobs/ObynDF9-senior-product-designer](https://www.ycombinator.com/companies/hadrius/jobs/ObynDF9-senior-product-designer)

生成摘要时出错

---

## 9. The peculiar case of Japanese web design (2022)

**原文标题**: The peculiar case of Japanese web design (2022)

**原文链接**: [https://sabrinas.space](https://sabrinas.space)

生成摘要时出错

---

## 10. Writing code is cheap now

**原文标题**: Writing code is cheap now

**原文链接**: [https://simonwillison.net/guides/agentic-engineering-patterns/code-is-cheap/](https://simonwillison.net/guides/agentic-engineering-patterns/code-is-cheap/)

生成摘要时出错

---

## 11. Show HN: Sowbot – open-hardware agricultural robot (ROS2, RTK GPS)

**原文标题**: Show HN: Sowbot – open-hardware agricultural robot (ROS2, RTK GPS)

**原文链接**: [https://sowbot.co.uk/](https://sowbot.co.uk/)

生成摘要时出错

---

## 12. Sub-$200 Lidar could reshuffle auto sensor economics

**原文标题**: Sub-$200 Lidar could reshuffle auto sensor economics

**原文链接**: [https://spectrum.ieee.org/solid-state-lidar-microvision-adas](https://spectrum.ieee.org/solid-state-lidar-microvision-adas)

生成摘要时出错

---

## 13. Magical Mushroom – Europe's first industrial-scale mycelium packaging producer

**原文标题**: Magical Mushroom – Europe's first industrial-scale mycelium packaging producer

**原文链接**: [https://magicalmushroom.com/index](https://magicalmushroom.com/index)

生成摘要时出错

---

## 14. What it means that Ubuntu is using Rust

**原文标题**: What it means that Ubuntu is using Rust

**原文链接**: [https://smallcultfollowing.com/babysteps/blog/2026/02/23/ubuntu-rustnation/](https://smallcultfollowing.com/babysteps/blog/2026/02/23/ubuntu-rustnation/)

生成摘要时出错

---

## 15. Emulating Goto in Scheme with Continuations

**原文标题**: Emulating Goto in Scheme with Continuations

**原文链接**: [https://terezi.pyrope.net/ccgoto/](https://terezi.pyrope.net/ccgoto/)

生成摘要时出错

---

## 16. 0 A.D. Release 28: Boiorix

**原文标题**: 0 A.D. Release 28: Boiorix

**原文链接**: [https://play0ad.com/new-release-0-a-d-release-28-boiorix/](https://play0ad.com/new-release-0-a-d-release-28-boiorix/)

生成摘要时出错

---

## 17. Anthropic Education the AI Fluency Index

**原文标题**: Anthropic Education the AI Fluency Index

**原文链接**: [https://www.anthropic.com/research/AI-fluency-index](https://www.anthropic.com/research/AI-fluency-index)

生成摘要时出错

---

## 18. femtolisp: A lightweight, robust, scheme-like Lisp implementation

**原文标题**: femtolisp: A lightweight, robust, scheme-like Lisp implementation

**原文链接**: [https://github.com/JeffBezanson/femtolisp](https://github.com/JeffBezanson/femtolisp)

生成摘要时出错

---

## 19. AI is destroying open source, and it's not even good yet [video]

**原文标题**: AI is destroying open source, and it's not even good yet [video]

**原文链接**: [https://www.youtube.com/watch?v=bZJ7A1QoUEI](https://www.youtube.com/watch?v=bZJ7A1QoUEI)

生成摘要时出错

---

## 20. Benchmarks for concurrent hash map implementations in Go

**原文标题**: Benchmarks for concurrent hash map implementations in Go

**原文链接**: [https://github.com/puzpuzpuz/go-concurrent-map-bench](https://github.com/puzpuzpuz/go-concurrent-map-bench)

生成摘要时出错

---

## 21. Large study finds link between cannabis use in teens and psychosis later

**原文标题**: Large study finds link between cannabis use in teens and psychosis later

**原文链接**: [https://text.npr.org/nx-s1-5719338](https://text.npr.org/nx-s1-5719338)

生成摘要时出错

---

## 22. SETI@home: Data Acquisition and Front-End Processing (2025)

**原文标题**: SETI@home: Data Acquisition and Front-End Processing (2025)

**原文链接**: [https://iopscience.iop.org/article/10.3847/1538-3881/ade5a7](https://iopscience.iop.org/article/10.3847/1538-3881/ade5a7)

生成摘要时出错

---

## 23. The Lighthouse: How extreme isolation transforms the body and mind

**原文标题**: The Lighthouse: How extreme isolation transforms the body and mind

**原文链接**: [https://www.newscientist.com/article/2231732-the-lighthouse-how-extreme-isolation-transforms-the-body-and-mind/](https://www.newscientist.com/article/2231732-the-lighthouse-how-extreme-isolation-transforms-the-body-and-mind/)

生成摘要时出错

---

## 24. Show HN: AI Timeline – 171 LLMs from Transformer (2017) to GPT-5.3 (2026)

**原文标题**: Show HN: AI Timeline – 171 LLMs from Transformer (2017) to GPT-5.3 (2026)

**原文链接**: [https://llm-timeline.com/](https://llm-timeline.com/)

生成摘要时出错

---

## 25. What Is a Centipawn Advantage?

**原文标题**: What Is a Centipawn Advantage?

**原文链接**: [https://win-vector.com/2026/02/19/what-is-a-centipawn-advantage/](https://win-vector.com/2026/02/19/what-is-a-centipawn-advantage/)

生成摘要时出错

---

## 26. Ed's Stratego Site

**原文标题**: Ed's Stratego Site

**原文链接**: [https://www.edcollins.com/stratego/index.html](https://www.edcollins.com/stratego/index.html)

生成摘要时出错

---

## 27. My journey to the microwave alternate timeline

**原文标题**: My journey to the microwave alternate timeline

**原文链接**: [https://www.lesswrong.com/posts/8m6AM5qtPMjgTkEeD/my-journey-to-the-microwave-alternate-timeline](https://www.lesswrong.com/posts/8m6AM5qtPMjgTkEeD/my-journey-to-the-microwave-alternate-timeline)

生成摘要时出错

---

## 28. I built Timeframe, our family e-paper dashboard

**原文标题**: I built Timeframe, our family e-paper dashboard

**原文链接**: [https://hawksley.org/2026/02/17/timeframe.html](https://hawksley.org/2026/02/17/timeframe.html)

生成摘要时出错

---

## 29. Microspeak: Escrow

**原文标题**: Microspeak: Escrow

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20260217-00/?p=112067](https://devblogs.microsoft.com/oldnewthing/20260217-00/?p=112067)

生成摘要时出错

---

## 30. VTT Test Donut Lab Battery Reaches 80% Charge in Under 10 Minutes [pdf]

**原文标题**: VTT Test Donut Lab Battery Reaches 80% Charge in Under 10 Minutes [pdf]

**原文链接**: [https://pub-fee113bb711e441db5c353d2d31abbb3.r2.dev/VTT_CR_00092_26.pdf](https://pub-fee113bb711e441db5c353d2d31abbb3.r2.dev/VTT_CR_00092_26.pdf)

生成摘要时出错

---

## 31. VTT Test Donut Lab Battery Reaches 80% Charge in Under 10 Minutes [pdf]

**原文标题**: VTT Test Donut Lab Battery Reaches 80% Charge in Under 10 Minutes [pdf]

**原文链接**: [https://pub-fee113bb711e441db5c353d2d31abbb3.r2.dev/VTT_CR_00092_26.pdf](https://pub-fee113bb711e441db5c353d2d31abbb3.r2.dev/VTT_CR_00092_26.pdf)

生成摘要时出错

---

## 32. Pope tells priests to use their brains, not AI, to write homilies

**原文标题**: Pope tells priests to use their brains, not AI, to write homilies

**原文链接**: [https://www.ewtnnews.com/vatican/pope-leo-xiv-tells-priests-to-use-their-brains-not-ai-to-write-homilies](https://www.ewtnnews.com/vatican/pope-leo-xiv-tells-priests-to-use-their-brains-not-ai-to-write-homilies)

生成摘要时出错

---

## 33. Decided to fly to the US to buy some hard drives

**原文标题**: Decided to fly to the US to buy some hard drives

**原文链接**: [https://old.reddit.com/r/DataHoarder/comments/1rb9ot4/decided_to_fly_to_the_us_to_buy_some_hard_drives](https://old.reddit.com/r/DataHoarder/comments/1rb9ot4/decided_to_fly_to_the_us_to_buy_some_hard_drives)

生成摘要时出错

---

## 34. Crawling a billion web pages in just over 24 hours, in 2025

**原文标题**: Crawling a billion web pages in just over 24 hours, in 2025

**原文链接**: [https://andrewkchan.dev/posts/crawler.html](https://andrewkchan.dev/posts/crawler.html)

生成摘要时出错

---

## 35. Why the EU's AI Act is about to become enterprises' biggest compliance challenge

**原文标题**: Why the EU's AI Act is about to become enterprises' biggest compliance challenge

**原文链接**: [https://techpinions.com/why-the-eus-ai-act-is-about-to-become-every-enterprises-biggest-compliance-challenge/](https://techpinions.com/why-the-eus-ai-act-is-about-to-become-every-enterprises-biggest-compliance-challenge/)

生成摘要时出错

---

## 36. ASML unveils EUV light source advance that could yield 50% more chips by 2030

**原文标题**: ASML unveils EUV light source advance that could yield 50% more chips by 2030

**原文链接**: [https://www.reuters.com/world/china/asml-unveils-euv-light-source-advance-that-could-yield-50-more-chips-by-2030-2026-02-23/](https://www.reuters.com/world/china/asml-unveils-euv-light-source-advance-that-could-yield-50-more-chips-by-2030-2026-02-23/)

生成摘要时出错

---

## 37. NASA uses Mars Helicopter's SoC for rover navigation upgrade

**原文标题**: NASA uses Mars Helicopter's SoC for rover navigation upgrade

**原文链接**: [https://www.theregister.com/2026/02/23/perseverance_rover_soc_navigation_upgrade/](https://www.theregister.com/2026/02/23/perseverance_rover_soc_navigation_upgrade/)

生成摘要时出错

---

## 38. Six Math Essentials

**原文标题**: Six Math Essentials

**原文链接**: [https://terrytao.wordpress.com/2026/02/16/six-math-essentials/](https://terrytao.wordpress.com/2026/02/16/six-math-essentials/)

生成摘要时出错

---

## 39. What I Learned After Building 3 TV Apps Coming from Mobile

**原文标题**: What I Learned After Building 3 TV Apps Coming from Mobile

**原文链接**: [https://dinkomarinac.dev/blog/what-i-learned-after-building-3-tv-apps-coming-from-mobile/](https://dinkomarinac.dev/blog/what-i-learned-after-building-3-tv-apps-coming-from-mobile/)

生成摘要时出错

---

## 40. Google restricting Google AI Pro/Ultra subscribers for using OpenClaw

**原文标题**: Google restricting Google AI Pro/Ultra subscribers for using OpenClaw

**原文链接**: [https://discuss.ai.google.dev/t/account-restricted-without-warning-google-ai-ultra-oauth-via-openclaw/122778](https://discuss.ai.google.dev/t/account-restricted-without-warning-google-ai-ultra-oauth-via-openclaw/122778)

生成摘要时出错

---

## 41. 自我去平台化

**原文标题**: Deplatform Yourself

**原文链接**: [https://pluralistic.net/2026/02/23/goodharts-lawbreaker/](https://pluralistic.net/2026/02/23/goodharts-lawbreaker/)

生成摘要时出错

---

## 42. Hetzner (European hosting provider) to increase prices by up to 38%

**原文标题**: Hetzner (European hosting provider) to increase prices by up to 38%

**原文链接**: [https://old.reddit.com/r/BuyFromEU/comments/1rce0lf/hetzner_european_hosting_provider_to_increase/](https://old.reddit.com/r/BuyFromEU/comments/1rce0lf/hetzner_european_hosting_provider_to_increase/)

生成摘要时出错

---

## 43. Loops is a federated, open-source TikTok

**原文标题**: Loops is a federated, open-source TikTok

**原文链接**: [https://joinloops.org/](https://joinloops.org/)

生成摘要时出错

---

## 44. Hey I almost got scammed by Google

**原文标题**: Hey I almost got scammed by Google

**原文链接**: [https://statmodeling.stat.columbia.edu/2026/02/21/hey-i-almost-got-scammed-by-google/](https://statmodeling.stat.columbia.edu/2026/02/21/hey-i-almost-got-scammed-by-google/)

生成摘要时出错

---

## 45. Show HN: CIA World Factbook Archive (1990–2025), searchable and exportable

**原文标题**: Show HN: CIA World Factbook Archive (1990–2025), searchable and exportable

**原文链接**: [https://cia-factbook-archive.fly.dev/](https://cia-factbook-archive.fly.dev/)

生成摘要时出错

---

## 46. How to train your program verifier

**原文标题**: How to train your program verifier

**原文链接**: [https://risemsr.github.io/blog/2026-02-16-halleyyoung-a3/](https://risemsr.github.io/blog/2026-02-16-halleyyoung-a3/)

生成摘要时出错

---

## 47. A NASA Engineer Discovered a World of Semi Truck Aerodynamics by Accident

**原文标题**: A NASA Engineer Discovered a World of Semi Truck Aerodynamics by Accident

**原文链接**: [https://www.thedrive.com/news/how-a-nasa-engineer-discovered-a-world-of-semi-truck-aerodynamics-by-accident](https://www.thedrive.com/news/how-a-nasa-engineer-discovered-a-world-of-semi-truck-aerodynamics-by-accident)

生成摘要时出错

---

## 48. Fix your tools

**原文标题**: Fix your tools

**原文链接**: [https://ochagavia.nl/blog/fix-your-tools/](https://ochagavia.nl/blog/fix-your-tools/)

生成摘要时出错

---

## 49. How did Joann Fabrics die while Best Buy survived? It wasn't Amazon

**原文标题**: How did Joann Fabrics die while Best Buy survived? It wasn't Amazon

**原文链接**: [https://www.governance.fyi/p/how-in-the-hell-did-joann-fabrics](https://www.governance.fyi/p/how-in-the-hell-did-joann-fabrics)

生成摘要时出错

---

## 50. The Musidex: A physical music library for the streaming era

**原文标题**: The Musidex: A physical music library for the streaming era

**原文链接**: [https://hannahilea.com/blog/musidex/](https://hannahilea.com/blog/musidex/)

生成摘要时出错

---

## 51. How close are we to a vision for 2010?

**原文标题**: How close are we to a vision for 2010?

**原文链接**: [https://shkspr.mobi/blog/2026/02/how-close-are-we-to-a-vision-for-2010/](https://shkspr.mobi/blog/2026/02/how-close-are-we-to-a-vision-for-2010/)

生成摘要时出错

---

## 52. Hello Worg, the Org-Mode Community

**原文标题**: Hello Worg, the Org-Mode Community

**原文链接**: [https://orgmode.org/worg/](https://orgmode.org/worg/)

生成摘要时出错

---

## 53. Pipelined Relational Query Language, Pronounced "Prequel"

**原文标题**: Pipelined Relational Query Language, Pronounced "Prequel"

**原文链接**: [https://prql-lang.org/](https://prql-lang.org/)

生成摘要时出错

---

## 54. What I learned designing a barebones UI engine

**原文标题**: What I learned designing a barebones UI engine

**原文链接**: [https://madebymohammed.com/miniui](https://madebymohammed.com/miniui)

生成摘要时出错

---

## 55. The JavaScript Oxidation Compiler

**原文标题**: The JavaScript Oxidation Compiler

**原文链接**: [https://oxc.rs/](https://oxc.rs/)

生成摘要时出错

---

## 56. Hacker News.love – 22 projects Hacker News didn't love

**原文标题**: Hacker News.love – 22 projects Hacker News didn't love

**原文链接**: [https://hackernews.love/](https://hackernews.love/)

生成摘要时出错

---

## 57. QRTape – Audio Playback from Paper Tape with Computer Vision (2021)

**原文标题**: QRTape – Audio Playback from Paper Tape with Computer Vision (2021)

**原文链接**: [http://www.theresistornetwork.com/2021/03/qrtape-audio-playback-from-paper-tape.html](http://www.theresistornetwork.com/2021/03/qrtape-audio-playback-from-paper-tape.html)

生成摘要时出错

---

## 58. Landlines are ringing in homes again. Why parents are happy about that

**原文标题**: Landlines are ringing in homes again. Why parents are happy about that

**原文链接**: [https://www.cnn.com/2026/02/23/health/kids-using-landlines-wellness](https://www.cnn.com/2026/02/23/health/kids-using-landlines-wellness)

生成摘要时出错

---

## 59. Linuxulator on FreeBSD Feels Like Magic

**原文标题**: Linuxulator on FreeBSD Feels Like Magic

**原文链接**: [https://hayzam.com/blog/02-linuxulator-is-awesome/](https://hayzam.com/blog/02-linuxulator-is-awesome/)

生成摘要时出错

---

## 60. Show HN: Local-First Linux MicroVMs for macOS

**原文标题**: Show HN: Local-First Linux MicroVMs for macOS

**原文链接**: [https://shuru.run](https://shuru.run)

生成摘要时出错

---

## 61. Emulated Windows 3.11 in the Browser

**原文标题**: Emulated Windows 3.11 in the Browser

**原文链接**: [https://pieter.com/](https://pieter.com/)

生成摘要时出错

---

## 62. Git's Magic Files

**原文标题**: Git's Magic Files

**原文链接**: [https://nesbitt.io/2026/02/05/git-magic-files.html](https://nesbitt.io/2026/02/05/git-magic-files.html)

生成摘要时出错

---

## 63. Scheme 9 from Empty Space (2014)

**原文标题**: Scheme 9 from Empty Space (2014)

**原文链接**: [https://t3x.org/s9book/index.html](https://t3x.org/s9book/index.html)

生成摘要时出错

---

## 64. Attention Media ≠ Social Networks

**原文标题**: Attention Media ≠ Social Networks

**原文链接**: [https://susam.net/attention-media-vs-social-networks.html](https://susam.net/attention-media-vs-social-networks.html)

生成摘要时出错

---

## 65. Using the new bridges of FreeBSD 15

**原文标题**: Using the new bridges of FreeBSD 15

**原文链接**: [https://blog.feld.me/posts/2026/02/using-new-bridges-freebsd-15/](https://blog.feld.me/posts/2026/02/using-new-bridges-freebsd-15/)

生成摘要时出错

---

## 66. Aqua: A CLI message tool for AI agents

**原文标题**: Aqua: A CLI message tool for AI agents

**原文链接**: [https://github.com/quailyquaily/aqua](https://github.com/quailyquaily/aqua)

生成摘要时出错

---

## 67. Man accidentally gains control of 7k robot vacuums

**原文标题**: Man accidentally gains control of 7k robot vacuums

**原文链接**: [https://www.popsci.com/technology/robot-vacuum-army/](https://www.popsci.com/technology/robot-vacuum-army/)

生成摘要时出错

---

## 68. Xweather Live – Interactive global vector weather map

**原文标题**: Xweather Live – Interactive global vector weather map

**原文链接**: [https://live.xweather.com/](https://live.xweather.com/)

生成摘要时出错

---

## 69. Dow drops 600 points as confusion grows after U.S. tariffs

**原文标题**: Dow drops 600 points as confusion grows after U.S. tariffs

**原文链接**: [https://www.cnbc.com/2026/02/22/stock-market-today-live-updates.html](https://www.cnbc.com/2026/02/22/stock-market-today-live-updates.html)

生成摘要时出错

---

## 70. Show HN: A geometric analysis of Chopin's Prelude No. 4 using 3D topology

**原文标题**: Show HN: A geometric analysis of Chopin's Prelude No. 4 using 3D topology

**原文链接**: [https://github.com/jimishol/cholidean-harmony-structure/blob/main/docs/03-case-study-chopin-prelude04.md](https://github.com/jimishol/cholidean-harmony-structure/blob/main/docs/03-case-study-chopin-prelude04.md)

生成摘要时出错

---

## 71. Fresh File Explorer – VS Code extension for navigating recent work

**原文标题**: Fresh File Explorer – VS Code extension for navigating recent work

**原文链接**: [https://github.com/FreHu/vscode-fresh-file-explorer](https://github.com/FreHu/vscode-fresh-file-explorer)

生成摘要时出错

---

## 72. The Tears of Donald Knuth (2015)

**原文标题**: The Tears of Donald Knuth (2015)

**原文链接**: [https://cacm.acm.org/opinion/the-tears-of-donald-knuth/](https://cacm.acm.org/opinion/the-tears-of-donald-knuth/)

生成摘要时出错

---

## 73. Dictionary Compression is finally here, and it's ridiculously good

**原文标题**: Dictionary Compression is finally here, and it's ridiculously good

**原文链接**: [https://httptoolkit.com/blog/dictionary-compression-performance-zstd-brotli/](https://httptoolkit.com/blog/dictionary-compression-performance-zstd-brotli/)

生成摘要时出错

---

## 74. Show HN: 3D Mahjong, Built in CSS

**原文标题**: Show HN: 3D Mahjong, Built in CSS

**原文链接**: [https://voxjong.com](https://voxjong.com)

生成摘要时出错

---

## 75. Pinterest is drowning in a sea of AI slop and auto-moderation

**原文标题**: Pinterest is drowning in a sea of AI slop and auto-moderation

**原文链接**: [https://www.404media.co/pinterest-is-drowning-in-a-sea-of-ai-slop-and-auto-moderation/](https://www.404media.co/pinterest-is-drowning-in-a-sea-of-ai-slop-and-auto-moderation/)

生成摘要时出错

---

## 76. Keep Android Open

**原文标题**: Keep Android Open

**原文链接**: [https://f-droid.org/2026/02/20/twif.html](https://f-droid.org/2026/02/20/twif.html)

生成摘要时出错

---

## 77. Coal plant owners say DOE 'emergency' order to run it violates Constitution

**原文标题**: Coal plant owners say DOE 'emergency' order to run it violates Constitution

**原文链接**: [https://www.utilitydive.com/news/doe-emergency-order-craig-colorado-coal-tri-state/811088/](https://www.utilitydive.com/news/doe-emergency-order-craig-colorado-coal-tri-state/811088/)

生成摘要时出错

---

## 78. What's the best way to learn a new language?

**原文标题**: What's the best way to learn a new language?

**原文链接**: [https://www.bbc.com/future/article/20260220-whats-the-best-way-to-learn-a-new-language](https://www.bbc.com/future/article/20260220-whats-the-best-way-to-learn-a-new-language)

生成摘要时出错

---

## 79. NanoClaw moved from Apple Containers to Docker

**原文标题**: NanoClaw moved from Apple Containers to Docker

**原文链接**: [https://twitter.com/Gavriel_Cohen/status/2025603982769410356](https://twitter.com/Gavriel_Cohen/status/2025603982769410356)

生成摘要时出错

---

## 80. Facebook's Fascination with My Robots.txt

**原文标题**: Facebook's Fascination with My Robots.txt

**原文链接**: [https://blog.nytsoi.net/2026/02/23/facebook-robots-txt](https://blog.nytsoi.net/2026/02/23/facebook-robots-txt)

生成摘要时出错

---

## 81. I verified my LinkedIn identity. Here's what I handed over

**原文标题**: I verified my LinkedIn identity. Here's what I handed over

**原文链接**: [https://thelocalstack.eu/posts/linkedin-identity-verification-privacy/](https://thelocalstack.eu/posts/linkedin-identity-verification-privacy/)

生成摘要时出错

---

## 82. Rhythms the Compendium: Life aboard an aircraft carrier (2021)

**原文标题**: Rhythms the Compendium: Life aboard an aircraft carrier (2021)

**原文链接**: [https://thelexicans.wordpress.com/2020/04/05/38223/](https://thelexicans.wordpress.com/2020/04/05/38223/)

生成摘要时出错

---

## 83. The Geometry of Tostitos Scoops

**原文标题**: The Geometry of Tostitos Scoops

**原文链接**: [https://chip-tech-rob.zocomputer.io/](https://chip-tech-rob.zocomputer.io/)

生成摘要时出错

---

## 84. Freemediaheckyeah – A collection of free stuff on the internet

**原文标题**: Freemediaheckyeah – A collection of free stuff on the internet

**原文链接**: [https://fmhy.net/](https://fmhy.net/)

生成摘要时出错

---

## 85. 面向人工智能重新定义软件工程职业

**原文标题**: Redefining the Software Engineering Profession for AI

**原文链接**: [https://dl.acm.org/doi/10.1145/3779312](https://dl.acm.org/doi/10.1145/3779312)

生成摘要时出错

---

## 86. Spain’s LaLiga has blocked access to freedom.gov

**原文标题**: Spain’s LaLiga has blocked access to freedom.gov

**原文链接**: [https://twitter.com/Pirat_Nation/status/2025643188321714642](https://twitter.com/Pirat_Nation/status/2025643188321714642)

生成摘要时出错

---

## 87. Black-White Array: fast, ordered and based on with O(log N) memory allocations

**原文标题**: Black-White Array: fast, ordered and based on with O(log N) memory allocations

**原文链接**: [https://github.com/dronnix/bwarr](https://github.com/dronnix/bwarr)

生成摘要时出错

---

## 88. Don't create .gitkeep files, use .gitignore instead (2023)

**原文标题**: Don't create .gitkeep files, use .gitignore instead (2023)

**原文链接**: [https://adamj.eu/tech/2023/09/18/git-dont-create-gitkeep/](https://adamj.eu/tech/2023/09/18/git-dont-create-gitkeep/)

生成摘要时出错

---

## 89. How far back in time can you understand English?

**原文标题**: How far back in time can you understand English?

**原文链接**: [https://www.deadlanguagesociety.com/p/how-far-back-in-time-understand-english](https://www.deadlanguagesociety.com/p/how-far-back-in-time-understand-english)

生成摘要时出错

---

## 90. Show HN: Implementing ping from the Ethernet layer (ARP,IPv4,ICMP in user space)

**原文标题**: Show HN: Implementing ping from the Ethernet layer (ARP,IPv4,ICMP in user space)

**原文链接**: [https://github.com/v420v/ping](https://github.com/v420v/ping)

生成摘要时出错

---

## 91. Using a Microwave to Reanimate Rats

**原文标题**: Using a Microwave to Reanimate Rats

**原文链接**: [https://pmc.ncbi.nlm.nih.gov/articles/PMC1365902/](https://pmc.ncbi.nlm.nih.gov/articles/PMC1365902/)

生成摘要时出错

---

## 92. How I launched 3 consoles and found true love at Babbage's store no. 9 (2013)

**原文标题**: How I launched 3 consoles and found true love at Babbage's store no. 9 (2013)

**原文链接**: [https://arstechnica.com/gadgets/2013/01/how-i-launched-3-consoles-and-found-true-love-at-babbages-store-no-9/](https://arstechnica.com/gadgets/2013/01/how-i-launched-3-consoles-and-found-true-love-at-babbages-store-no-9/)

生成摘要时出错

---

## 93. What is a database transaction?

**原文标题**: What is a database transaction?

**原文链接**: [https://planetscale.com/blog/database-transactions](https://planetscale.com/blog/database-transactions)

生成摘要时出错

---

## 94. Hickory-DNS: a Rust based DNS client, server, and resolver

**原文标题**: Hickory-DNS: a Rust based DNS client, server, and resolver

**原文链接**: [https://github.com/hickory-dns/hickory-dns](https://github.com/hickory-dns/hickory-dns)

生成摘要时出错

---

## 95. A bug is a bug, but a patch is a policy: The case for bootable containers

**原文标题**: A bug is a bug, but a patch is a policy: The case for bootable containers

**原文链接**: [https://tuananh.net/2026/02/20/patch-is-policy/](https://tuananh.net/2026/02/20/patch-is-policy/)

生成摘要时出错

---

## 96. ReferenceFinder: Find coordinates on a piece of paper with only folds

**原文标题**: ReferenceFinder: Find coordinates on a piece of paper with only folds

**原文链接**: [https://mutsuntsai.github.io/reference-finder/](https://mutsuntsai.github.io/reference-finder/)

生成摘要时出错

---

## 97. Procedural Tron

**原文标题**: Procedural Tron

**原文链接**: [https://www.tripgeo.com/huntforredoctangles](https://www.tripgeo.com/huntforredoctangles)

生成摘要时出错

---

## 98. AI uBlock Blacklist

**原文标题**: AI uBlock Blacklist

**原文链接**: [https://github.com/alvi-se/ai-ublock-blacklist](https://github.com/alvi-se/ai-ublock-blacklist)

生成摘要时出错

---

## 99. We hid backdoors in ~40MB binaries and asked AI + Ghidra to find them

**原文标题**: We hid backdoors in ~40MB binaries and asked AI + Ghidra to find them

**原文链接**: [https://quesma.com/blog/introducing-binaryaudit/](https://quesma.com/blog/introducing-binaryaudit/)

生成摘要时出错

---

## 100. Large US company came after me for releasing a free open-source alternative

**原文标题**: Large US company came after me for releasing a free open-source alternative

**原文链接**: [https://old.reddit.com/r/selfhosted/comments/1rbkx5e/large_us_company_came_after_me_for_releasing_a/](https://old.reddit.com/r/selfhosted/comments/1rbkx5e/large_us_company_came_after_me_for_releasing_a/)

生成摘要时出错

---

