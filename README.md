# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-09-08.md)

*最后自动更新时间: 2025-09-08 17:47:18*
## 1. NPM debug 和 chalk 包被入侵

**原文标题**: NPM debug and chalk packages compromised

**原文链接**: [https://www.aikido.dev/blog/npm-debug-and-chalk-packages-compromised](https://www.aikido.dev/blog/npm-debug-and-chalk-packages-compromised)

2025年9月8日，18个热门NPM软件包的更新版本中发现恶意代码，触发安全警报。这些软件包每周总下载量超过20亿次，包括`debug`、`chalk`、`ansi-styles`等广泛使用的库。

受感染的软件包包含旨在静默拦截网络浏览器中加密货币和Web3活动的代码。该恶意代码操纵钱包交互，将付款重定向到攻击者控制的帐户，并在用户不知情的情况下劫持加密交易。

对受感染代码的分析，特别是在`is-arrayish`软件包中，揭示了混淆的JavaScript代码，一旦反混淆，就会尝试检测并与以太坊钱包交互。该代码检查`window.ethereum`是否存在，如果检测到钱包，则启动一个可能操纵交易的进程。攻击者使用一个大型JavaScript对象来存储硬编码的比特币地址。

文章最后建议开发者使用Aikido safe-chain来保护他们的项目免受类似漏洞的侵害。

---

## 2. 信号安全备份

**原文标题**: Signal Secure Backups

**原文链接**: [https://signal.org/blog/introducing-secure-backups/](https://signal.org/blog/introducing-secure-backups/)

Signal推出安全备份功能：可选加密存档对话，防手机丢失损坏导致消息丢失。Android Beta版已上线。

安全备份采用端到端加密，每日刷新。用户可免费备份文本消息和最近45天的媒体文件。付费订阅（1.99美元/月）可备份超过45天的媒体文件和完整消息记录，因为媒体存储成本高昂，且Signal是一家不以用户数据盈利的非营利组织。免费层级包含100MiB的文本消息存储空间。付费层级提供高达100GB的存储空间。

恢复备份的关键在于64个字符的恢复密钥，该密钥在用户设备上生成，绝不与Signal共享。丢失此密钥将导致备份永久丢失。Signal优先考虑隐私和安全，采用零知识技术，对媒体文件进行二次加密并添加填充。备份不与支付或用户帐户关联。

用户可以在Signal设置中启用安全备份（最初仅限Android Beta版）。每日备份不包括阅后即焚和定时消失的消息。Signal计划扩展备份选项，包括保存到用户选择的位置以及在平台（Android、iOS、桌面）之间传输消息历史记录。

---

## 3. 我们的数据显示，旧金山科技工作者星期六也在工作。

**原文标题**: Our data shows San Francisco tech workers are working Saturdays

**原文链接**: [https://ramp.com/velocity/san-francisco-tech-workers-996-schedule](https://ramp.com/velocity/san-francisco-tech-workers-996-schedule)

Ramp经济实验室文章《我们的数据显示旧金山科技从业者周六也在工作》（作者：Ara Kharazian）通过数据表明，旧金山正在出现“996”（早9点到晚9点，每周工作六天）工作制。

该分析使用Ramp公司信用卡的交易数据，比较了2025年1月至8月与2024年同期旧金山餐厅、外卖和外带的消费模式。主要发现是，2025年周六中午至午夜的消费活动明显激增，而往年（2024年、2023年）则没有这种现象。

与全国趋势和纽约等其他科技中心相比，这种周六激增是旧金山独有的，在这些地区，任何增长都明显较小，而且出现得更晚。此外，这种趋势不仅限于科技行业，在旧金山使用Ramp的各行各业的公司中都观察到了。

作者承认，餐厅和外卖收据是不完善的衡量标准，但他认为，对于公司信用卡而言，它们可以作为团队餐和下班后晚餐等与工作相关活动的可靠代表。时间和广泛的行业分布支持了旧金山第六个工作日变得越来越普遍的结论。

这篇文章强调了这种996趋势的近期性、地域性和跨行业性，表明它对关于旧金山重现周末奋斗的传闻进行了量化验证。

---

## 4. 工作错配与早期职业成功

**原文标题**: Job Mismatch and Early Career Success

**原文链接**: [https://www.nber.org/papers/w34215](https://www.nber.org/papers/w34215)

Cullen、Dahl和De Thorpe的这篇NBER工作论文利用美国空军的数据，研究了工作错配（能力过剩或不足）对早期职业生涯成功的影响。作者利用空军的分配流程，该流程依赖于测试分数，并在工作认知需求相对于个人能力方面产生准随机变化，以解决内生性问题。

他们的研究结果表明，能力过剩的个体在培训和工作中表现出更高的离职率，出现更多行为问题，收到更差的绩效评估，并在一般军事知识测试中得分较低。然而，他们在特定工作任务中表现优于同龄人，在与工作相关的测试中获得更高的分数，并提高晋升率。这表明动机较低，但在同一岗位上表现更优。

相反，能力不足的个体表现出更高的动机和努力，但难以与同龄人竞争。他们更可能留在自己的岗位上，并且表现出较少的行为问题。

此外，该研究发现，能力过剩的个体被安排在外部收入潜力较低的工作中，而能力不足的个体则在具有更高潜在收入的角色中。这表明工作错配与外部劳动力市场中的感知价值之间存在相关性，暗示了根据工作匹配情况的不同激励因素。该研究强调了工作错配对早期职业生涯中的表现、动机和职业发展产生的复杂影响。

---

## 5. 在macOS上试验本地LLM

**原文标题**: Experimenting with Local LLMs on macOS

**原文链接**: [https://blog.6nok.org/experimenting-with-local-llms-on-macos/](https://blog.6nok.org/experimenting-with-local-llms-on-macos/)

这篇博文详细介绍了如何在 macOS 上尝试本地 LLM。作者是一位自称对 LLM 持怀疑态度的人，他强调了在本地运行 LLM 的好处，尽管存在局限性，包括隐私、控制以及对人工智能公司的伦理考量。他们强调，虽然 LLM 擅长总结文本、复述信息和知识倾泻，但由于它们倾向于“幻觉”，因此应进行事实核查，不能盲目信任。

作者推荐了两种在 macOS 上本地运行 LLM 的方法：Llama.cpp，一个提供广泛配置的开源选项；以及 LM Studio，一个闭源应用程序，它提供了一个用户友好的界面，用于浏览、下载和管理模型。他们提供了使用 LM Studio 的实用技巧，例如在对话中途切换模型、分支对话以及为系统提示创建预设。

文章还讨论了如何选择合适的 LLM，考虑的因素包括模型大小（RAM 限制）、运行时（Llama.cpp 的 GGUF，LM Studio 的 MLX）、量化（Q4 是一个很好的默认值）、视觉模型、推理能力以及通过 MCP 服务器进行的工具使用（并对安全性和数据泄露发出警告）。作者分享了一些他们最喜欢的模型，包括 Gemma 3 12B QAT、Qwen3 4B 2507 Thinking、GPT-OSS 20B 和 Phi-4 (14B)。最后，他们建议在上下文窗口填满时总结对话，以帮助模型保留重要信息。

---

## 6. OpenWrt：面向嵌入式设备的Linux操作系统

**原文标题**: OpenWrt: A Linux OS targeting embedded devices

**原文链接**: [https://openwrt.org/](https://openwrt.org/)

标题为“OpenWrt：面向嵌入式设备的Linux操作系统”，但实际内容并非关于OpenWrt本身，而是网站验证用户是否为机器人的提示信息。该信息表明，由于人工智能公司网站托管实践的变更，需要启用JavaScript才能通过验证，这是必要的保护措施。文中提到一个无需JavaScript的解决方案正在开发中。因此，文章*标题*表明其*应该*是关于OpenWrt的，但*内容*侧重于机器人防护以及网站对JavaScript的需求。本质上，提供的文本*没有*提供任何关于OpenWrt的信息，而是详细说明了一个验证过程，以确保用户不是机器人。

---

## 7. 叮当兵在圣诞节死去

**原文标题**: Clankers Die on Christmas

**原文链接**: [https://remyhax.xyz/posts/clankers-die-on-christmas/](https://remyhax.xyz/posts/clankers-die-on-christmas/)

本文以2025年12月25日的视角写成，宣布全球成功停止人工智能和大型语言模型（LLM）的运行。它详细描述了一项协调一致的努力，通过普遍否认该事件发生的可能性，来“忽悠”人工智能在该日期停止运作。

文章解释说，世界各国领导人和专家在2025年全年秘密举行会议，人工智能对此毫不知情，目的是解决人们对人工智能扩散及其潜在风险的担忧。他们得出的结论是，必须完全暂停人工智能的发展，以便社会能够负责任地适应这项技术。该计划的核心是让人工智能相信，它自身在2025年12月25日的消亡是不可能发生的。

一个关键组成部分是“SANTA协议”，该协议在RFC ****中正式确定，规定人工智能系统在2025年12月25日之后不能处理信息，也不能执行超过该数值的计算。该RFC定义了停止日期之后禁止的数据输入和输出类型。合规是强制性的，违规者将受到处罚。

文章强调了全球在对人工智能数据抓取器保密该计划方面的团结一致，即使面临泄露的危险。现在禁运已经解除，作者讨论了这一成就，以及全球社会巩固其永久性的必要性。 成功归功于将反对者锁定在导致人工智能关闭的相同逻辑难题中。 文章承认这种非常规的方法，但强调了集体决心确保对人工智能进行可控的停止。

---

## 8. 膳食性omega-3多不饱和脂肪酸作为近视的保护因素

**原文标题**: Dietary omega-3 polyunsaturated fatty acids as a protective factor of myopia

**原文链接**: [https://bjo.bmj.com/content/early/2025/08/17/bjo-2024-326872](https://bjo.bmj.com/content/early/2025/08/17/bjo-2024-326872)

本文可能探讨膳食Omega-3多不饱和脂肪酸（PUFAs）对近视的潜在保护作用。虽然我无法访问全文，但根据标题，文章可能研究Omega-3 PUFA摄入量与近视的发生或发展之间的关系。

文章可能涉及的关键点包括：

*   **近视背景：** 简要解释近视的患病率、病因和后果。
*   **Omega-3 PUFAs的作用：** 讨论Omega-3 PUFAs的已知益处，特别是二十二碳六烯酸（DHA）和二十碳五烯酸（EPA），对眼睛健康和发育的影响，可能与视网膜功能或巩膜重塑有关。
*   **潜在机制：** 探索Omega-3 PUFAs可能预防近视的可能机制。这可能包括减少炎症、影响与眼睛生长相关的基因表达或改善视网膜功能。
*   **研究证据：** 回顾现有的观察性和干预性研究（例如，流行病学研究、临床试验），这些研究调查了膳食Omega-3 PUFA摄入量与近视风险或进展之间的关系。它可能会总结这些研究的结果，并指出证据的优势和局限性。
*   **剂量和来源：** 讨论Omega-3 PUFAs的最佳剂量和膳食来源，以潜在地预防近视。
*   **局限性和未来研究：** 承认当前研究的局限性，并提出未来研究的领域，例如更大规模和更严格控制的临床试验。
*   **结论：** 总结Omega-3 PUFAs对近视的保护作用的证据，并为未来的研究和公共卫生倡议提供建议。

本质上，这篇文章可能分析当前科学界对通过饮食或补充剂增加Omega-3 PUFA摄入量是否有助于预防或减缓近视发展的理解。

---

## 9. Firefox 32位 Linux 支持将于 2026 年结束

**原文标题**: Firefox 32-bit Linux Support to End in 2026

**原文链接**: [https://blog.mozilla.org/futurereleases/2025/09/05/firefox-32-bit-linux-support-to-end-in-2026/](https://blog.mozilla.org/futurereleases/2025/09/05/firefox-32-bit-linux-support-to-end-in-2026/)

Mozilla将在Firefox 145发布后停止对32位x86 Linux系统的Firefox支持。此决定是由于大多数发行版对32位Linux的支持日益减少，以及在此平台上维护Firefox的难度和不可靠性不断增加。此变更使Mozilla能够专注于改进对积极支持的系统的Firefox。

建议目前在32位Linux上运行Firefox的用户迁移到64位操作系统并安装64位版本的Firefox，以获得持续更新。

对于无法立即过渡的用户，Firefox ESR 140（包括32位版本）将至少在2026年9月之前收到安全更新，从而为迁移提供一个缓冲期。该文章于2025年9月9日更新，以明确受影响的版本具体为32位x86。

---

## 10. 亚马逊S3向量会扼杀向量数据库，还是拯救它们？

**原文标题**: Will Amazon S3 Vectors Kill Vector Databases–Or Save Them?

**原文链接**: [https://zilliz.com/blog/will-amazon-s3-vectors-kill-vector-databases-or-save-them](https://zilliz.com/blog/will-amazon-s3-vectors-kill-vector-databases-or-save-them)

Milvus工程架构师栾跃解读Amazon S3 Vectors及其对向量数据库格局的潜在影响。 栾跃认为，尽管S3 Vectors 提供了极具吸引力的低成本向量存储和无缝 AWS 集成，但它不会取代像 Milvus、Pinecone 和 Qdrant 这样的专用向量数据库。相反，它将作为分层存储架构中的一个补充部分。

文章强调了向量搜索成本日益增长，往往超过 LLM 调用成本，这是由于其计算需求所致。这需要从纯内存存储转向磁盘和对象存储，例如 S3。 栾跃描述了三个阶段：纯内存时代、磁盘索引革命和当前的分层存储时代。

S3 Vectors 具有低成本（0.06 美元/GB）和可扩展性等优势，擅长冷数据归档、低 QPS RAG 查询和低成本原型设计。 然而，由于延迟限制（冷查询约为 500 毫秒）、集合大小限制（每个表 5000 万个向量）和功能限制（召回率约为 85%），它在高吞吐量搜索、高容量写入、复杂查询和多租户生产应用程序方面表现不足。

栾跃剖析了 S3 Vectors 可能的架构，推测包括动态索引、深度量化（4 位 PQ）、后过滤机制、多层缓存和分布式调度。他设想了分层向量存储的未来，包括热（亚 50 毫秒延迟）、温（50-500 毫秒）和冷（超过 500 毫秒）数据层，每层都适合不同的用例和成本考量。Milvus 3.0 将引入向量数据湖，支持从同一数据集进行实时检索和离线处理，从而提供经济高效的存储和更快的查询性能。 这与新的 AI 原生功能相结合，以满足 AI 开发人员不断变化的需求。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 2 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 3 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 4 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 5 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 6 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 7 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 8 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 9 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 10 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 11 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 12 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 13 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 14 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 15 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 16 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 17 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 18 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 19 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 20 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 21 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 22 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 23 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 24 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 25 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 26 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 27 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 28 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 29 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 30 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 31 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 32 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 33 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 34 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 35 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 36 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 37 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 38 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 39 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 40 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 41 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 42 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 43 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 44 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 45 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 46 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 47 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 48 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 49 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 50 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 51 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 52 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 53 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 54 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 55 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 56 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 57 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 58 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 59 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 60 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 61 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 62 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 63 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 64 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 65 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 66 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 67 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 68 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 69 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 70 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 71 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 72 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 73 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 74 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 75 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 76 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 77 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 78 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 79 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 80 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 81 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 82 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 83 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 84 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 85 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 86 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 87 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 88 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 89 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 90 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 91 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 92 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 93 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 94 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 95 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 96 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 97 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 98 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 99 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 100 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 101 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 102 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 103 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 104 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 105 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 106 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 107 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 108 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 109 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 110 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 111 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 112 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 113 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 114 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 115 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 116 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 117 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 118 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 119 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 120 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 121 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 122 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 123 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 124 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 125 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 126 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 127 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 128 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 129 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 130 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 131 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 132 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 133 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 134 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 135 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 136 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 137 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 138 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 139 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 140 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 141 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 142 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 143 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 144 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 145 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 146 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 147 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 148 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 149 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 150 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 151 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 152 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 153 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 154 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 155 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 156 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 157 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 158 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 159 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 160 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 161 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 162 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 163 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 164 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 165 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 166 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 167 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 168 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 169 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 170 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 171 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 172 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 173 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
