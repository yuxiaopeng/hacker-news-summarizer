# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-02-23.md)

*最后自动更新时间: 2026-02-23 18:27:29*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 2 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 3 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 4 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 5 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 6 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 7 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 8 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 9 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 10 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 11 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 12 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 13 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 14 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 15 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 16 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 17 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 18 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 19 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 20 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 21 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 22 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 23 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 24 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 25 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 26 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 27 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 28 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 29 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 30 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 31 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 32 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 33 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 34 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 35 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 36 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 37 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 38 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 39 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 40 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 41 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 42 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 43 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 44 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 45 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 46 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 47 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 48 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 49 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 50 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 51 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 52 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 53 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 54 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 55 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 56 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 57 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 58 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 59 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 60 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 61 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 62 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 63 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 64 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 65 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 66 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 67 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 68 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 69 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 70 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 71 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 72 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 73 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 74 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 75 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 76 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 77 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 78 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 79 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 80 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 81 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 82 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 83 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 84 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 85 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 86 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 87 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 88 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 89 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 90 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 91 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 92 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 93 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 94 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 95 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 96 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 97 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 98 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 99 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 100 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 101 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 102 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 103 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 104 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 105 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 106 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 107 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 108 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 109 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 110 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 111 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 112 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 113 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 114 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 115 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 116 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 117 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 118 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 119 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 120 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 121 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 122 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 123 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 124 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 125 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 126 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 127 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 128 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 129 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 130 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 131 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 132 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 133 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 134 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 135 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 136 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 137 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 138 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 139 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 140 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 141 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 142 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 143 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 144 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 145 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 146 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 147 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 148 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 149 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 150 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 151 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 152 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 153 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 154 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 155 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 156 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 157 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 158 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 159 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 160 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 161 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 162 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 163 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 164 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 165 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 166 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 167 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 168 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 169 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 170 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 171 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 172 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 173 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 174 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 175 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 176 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 177 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 178 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 179 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 180 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 181 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 182 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 183 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 184 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 185 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 186 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 187 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 188 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 189 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 190 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 191 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 192 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 193 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 194 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 195 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 196 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 197 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 198 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 199 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 200 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 201 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 202 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 203 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 204 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 205 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 206 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 207 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 208 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 209 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 210 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 211 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 212 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 213 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 214 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 215 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 216 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 217 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 218 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 219 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 220 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 221 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 222 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 223 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 224 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 225 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 226 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 227 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 228 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 229 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 230 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 231 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 232 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 233 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 234 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 235 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 236 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 237 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 238 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 239 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 240 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 241 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 242 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 243 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 244 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 245 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 246 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 247 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 248 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 249 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 250 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 251 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 252 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 253 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 254 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 255 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 256 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 257 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 258 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 259 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 260 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 261 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 262 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 263 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 264 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 265 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 266 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 267 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 268 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 269 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 270 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 271 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 272 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 273 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 274 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 275 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 276 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 277 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 278 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 279 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 280 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 281 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 282 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 283 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 284 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 285 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 286 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 287 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 288 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 289 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 290 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 291 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 292 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 293 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 294 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 295 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 296 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 297 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 298 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 299 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 300 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 301 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 302 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 303 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 304 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 305 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 306 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 307 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 308 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 309 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 310 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 311 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 312 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 313 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 314 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 315 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 316 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 317 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 318 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 319 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 320 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 321 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 322 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 323 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 324 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 325 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 326 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 327 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 328 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 329 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 330 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 331 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 332 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 333 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 334 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 335 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 336 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 337 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 338 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 339 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 340 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
