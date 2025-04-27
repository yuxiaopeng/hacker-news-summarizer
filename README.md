# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-04-27.md)

*最后自动更新时间: 2025-04-27 17:47:15*
## 1. 激发创造力的秘诀：阅读讣告

**原文标题**: The Creativity Hack No One Told You About: Read the Obits

**原文链接**: [https://thereader.mitpress.mit.edu/the-creativity-hack-no-one-told-you-about-read-the-obits/](https://thereader.mitpress.mit.edu/the-creativity-hack-no-one-told-you-about-read-the-obits/)

基思·索耶认为阅读讣告，尤其是《纽约时报》上的小字讣告，能够显著提升创造力。他的依据是创造力研究表明，原创想法往往源于将看似不相关的概念联系起来。这是因为创造力依赖于先验知识，而知识越多样化，概念上越遥远，产生新颖想法的机会就越大。

索耶引用研究表明，富有创造力的人倾向于在他人可能认为不相关的想法之间建立联系。他举例说明了维可牢尼龙搭扣的发明，该发明源于观察到毛刺粘在狗的毛皮上。他强调了“结构映射”的重要性，即一个概念的关系结构被转移到另一个概念上，从而产生更深刻的创造性见解。

小字讣告充满了多样化且往往出人意料的生活故事，为遥远的概念提供了强大的来源。与强化现有知识的互联网搜索不同，讣告让读者接触到他们可能永远不会遇到的各种领域和经历。索耶建议慢慢阅读讣告，吸收细节，不要立即寻找大创意，并对所描述的生活提出问题。他强调要寻找每个生活故事中的基本原则和叙事，并寻求与自己生活的联系。通过这样做，读者可以激发他们的创造性思维，并增加意外突破的可能性。

---

## 2. 反向地理编码很难

**原文标题**: Reverse Geocoding Is Hard

**原文链接**: [https://shkspr.mobi/blog/2025/04/reverse-geocoding-is-hard/](https://shkspr.mobi/blog/2025/04/reverse-geocoding-is-hard/)

作者描述了为 OpenBenches（一个众包纪念长椅数据库）进行逆地理编码的挑战。将经纬度坐标转换为人类可读的地址比最初看起来更复杂。虽然存在用于此目的的 API，但它们通常会返回过于详细的地址，其中包含不相关的信息，例如邮政编码或过于具体的行政区划。

目标是提供长椅位置的粗略文本表示，以及允许用户浏览特定区域内长椅的可点击地址。这需要精确且相关的地点信息。

当长椅位于公园或街道上，而具体的街道地址不可用或不理想时，问题就出现了。使用附近的兴趣点 (POI) 作为替代方案也有其自身的问题，包括确定适当的地点名称、处理国际用户的本地化（例如，以英语显示地址）以及确保 POI 实际上是相关的附近地标。长椅可能在物理上靠近某个 POI，但在逻辑上与其不相关。

作者考虑使用 OpenCage 的地址格式化程序来简化地址，但这并不能解决非街道地址位置的问题。最终，提出的计划是使用 StadiaMaps 查找每张长椅最近的 POI，以英文显示 POI 名称和粗略位置，并将其保存为“地址”，承认这种方法可能会因其固有的局限性而导致用户投诉。

---

## 3. 5G终结了IMSI捕获器吗？

**原文标题**: Did 5G Kill the IMSI Catcher?

**原文链接**: [https://zetier.com/5g-imsi-catcher/](https://zetier.com/5g-imsi-catcher/)

Zetier文章：IMSI捕获器与5G网络安全

这篇Zetier文章由高级网络工程师Mark Santorello撰写，探讨了蜂窝网络易受IMSI捕获器攻击的漏洞，IMSI捕获器是用于拦截和窃取移动设备中唯一标识符（IMSI）的工具。GSM（2G）、UMTS（3G）和LTE（4G）协议容易受到这些攻击，而5G引入了改进，对IMSI进行了加密，现在称为SUPI，并创建了用于传输的SUCI。

文章解释了IMSI捕获器的工作原理，区分了主动（可检测且非法）和被动（不可检测）类型。被动IMSI捕获器利用设备切换基站时的注册过程，在初始连接、位置区代码更改或位置更新请求期间拦截未加密的IMSI。

虽然5G的SUCI解决了明文IMSI漏洞，但Santorello认为IMSI捕获器并未完全过时。他指出了几个可利用的机会，包括5G非独立组网（NSA）部署、允许降级到易受攻击的4G网络的配置错误的基站，以及移动运营商可能不使用SUCI功能的情况。文章的结论是，蜂窝移动通信始终存在内在漏洞，从技术挑战转变为地理挑战，为CNE开发人员提供了有趣而富有乐趣的工作。最后，它提供了一些保护个人数据的基本技巧，例如优先考虑5G-SA网络设置、在信号弱的区域使用飞行模式，或者使用法拉第袋。

---

## 4. Libogc (Wii自制程序库) 发现包含盗用自RTEMS的代码

**原文标题**: Libogc (Wii homebrew library) discovered to contain code stolen from RTEMS

**原文链接**: [https://github.com/fail0verflow/hbc/blob/80a80251f83f1993c272c58e471d040f3eb1dee9/README.md](https://github.com/fail0verflow/hbc/blob/80a80251f83f1993c272c58e471d040f3eb1dee9/README.md)

这份存档文档详细描述了围绕Wii自制程序库libogc的争议，该程序库被The Homebrew Channel等项目使用。The Homebrew Channel的开发者发现，libogc代码的很大一部分，包括其线程实现，是从RTEMS（一个实时操作系统）窃取的。在此之前，他们还发现任天堂SDK的专有代码被窃取并合并到libogc中。作者声称，libogc的开发者删除了RTEMS代码的所有署名和版权信息，这代表着蓄意的侵犯版权行为。

这个问题曾向libogc的开发者提出，但他们据称关闭了问题，以恶语回应并将其删除，表现出对解决版权问题或告知社区毫无兴趣。因此，作者认为使用libogc编译软件是非法的。

该文档批评了libogc的主要作者shagkur以及libogc团队的其他成员，指责他们盗用代码并进行后续掩盖，并指控他们欺骗Wii自制程序社区，隐瞒代码的来源。作者敦促开发者要求SDK和工具包提供商遵守法律和道德规范。

文档随后转入描述The Homebrew Channel源代码的公开发布，详细说明了包含哪些组件（The Homebrew Channel、reload stub、banner、PyWii、WiiPAX）以及不包含哪些组件（installer）。它概述了构建说明，包括所需的库和构建过程，并明确了代码在GNU通用公共许可证第2版或更高版本下的许可。

---

## 5. YC创始人指出，除了为警察国家工作外，还有其他工作机会。

**原文标题**: YC founder points out that jobs exist outside of working for police state

**原文链接**: [https://bird.makeup/users/paulg/statuses/1913338841068404903](https://bird.makeup/users/paulg/statuses/1913338841068404903)

一篇短文强调一位科技创始者对技术娴熟的程序员的鼓励，敦促他们寻找在那些助长他们所认为的“警察国家基础设施”之外的公司的工作机会。核心论点是，鉴于当前蓬勃发展的科技景象，高素质的程序员拥有大量选择，因此在选择雇主时应考虑道德影响。这位创始人特别建议不要为可能参与开发可能被当局用于监视或控制的技术的公司工作，暗示这些类型的公司正在助长警察国家环境。这篇文章来源于 Mastodon 帖子，表明技术工作者有道义上的必要性去考虑他们的工作对社会的影响，并选择符合他们价值观的公司。本质上，这是呼吁程序员负责任地利用他们的技能，并避免助长潜在的有害技术。

---

## 6. Show HN: 我创建了snapDOM，以极快的速度将DOM节点捕获为图像

**原文标题**: Show HN: I created snapDOM to capture DOM nodes as images with exceptional speed

**原文链接**: [https://github.com/zumerlab/snapdom](https://github.com/zumerlab/snapdom)

SnapDOM：一款快速、精确的高保真DOM捕获工具，专为复杂DOM结构设计。它为Zumly动画引擎开发，可将HTML元素转换为可缩放的SVG图像，保留样式、字体、阴影DOM和伪元素。

主要特性包括：完整DOM捕获、嵌入式样式和字体、导出为各种格式（SVG、PNG、JPG、WebP、canvas）、轻量级设计且无依赖项、以及依赖于标准Web API。

安装方式灵活，支持CDN、脚本标签和ES模块导入。API提供将元素捕获为SVG数据URL、HTMLImageElement、HTMLCanvasElement或不同图像格式的方法，并提供缩放和质量选项。

特殊功能涵盖阴影DOM、伪元素、图像内联、字体复制和占位符/排除功能。

局限性包括需要CORS可访问的外部图像、完全加载的字体以及不支持iframe捕获。

基准测试表明，snapDOM的性能优于modern-screenshot和html2canvas，尤其是在DOM大小增加时，使其非常适合捕获完整页面视图、模态窗口和复杂布局。该库以MIT许可证发布。

---

## 7. Extend (YC W23) 正在招聘工程师，构建 LLM 文档处理系统

**原文标题**: Extend (YC W23) is hiring engineers to build LLM document processing

**原文链接**: [https://jobs.ashbyhq.com/extend/9d4d8974-bd9b-432d-84ec-8268e5a8ed37](https://jobs.ashbyhq.com/extend/9d4d8974-bd9b-432d-84ec-8268e5a8ed37)

Extend (YC W23) 招聘高级/资深软件工程师，构建 LLM 驱动的文档处理解决方案。核心信息是 Extend 正在招聘工程师参与此项工作。由于全部内容仅为职位名称和注明需要 JavaScript 才能运行应用程序的提示，因此无法获取更多信息。我们可以推断，该职位涉及重要的软件开发工作，考虑到提到了 JavaScript，可能侧重于后端或全栈开发。LLM 开发的具体技术未提及，但候选人可能会使用 Python 和相关的机器学习库。

---

## 8. Shardines：基于 ActiveRecord 的每个租户一个 SQLite3 数据库

**原文标题**: Shardines: SQLite3 Database-per-Tenant with ActiveRecord

**原文链接**: [https://blog.julik.nl/2025/04/a-can-of-shardines](https://blog.julik.nl/2025/04/a-can-of-shardines)

本文探讨了在使用Rails实现基于SQLite3的每个租户一个数据库的多租户架构时所面临的挑战。作者认为，虽然这种方法具有隔离性、简化备份和易于调试等优点，但ActiveRecord的连接管理和历史设计选择使其实现起来异常困难。

文章将“每个租户一个数据库”的方法与其他多租户策略进行了对比，强调了SQLite3在这种背景下的优势，因为它具有轻量级和基于文件的存储特性。作者认为，Rails当前的多数据库功能是面向大型分片数据库的，而不是面向众多小型、隔离的数据库的，这导致在尝试动态管理每个租户的连接时会变得复杂。

主要问题包括ActiveRecord对持久连接的假设、其模式和查询缓存机制，以及缺乏为每个查询指定要使用的连接的直接API。作者还指出，其他引擎（如MySQL）对大型数据库的性能优化与SQLite3在处理许多小型数据库方面的优势相冲突。

最终，作者提倡使用自定义中间件解决方案来管理基于SQLite3的多租户Rails应用程序中的数据库连接，并强调这种方法比依赖为不同用例设计的现有Rails功能要有效得多、更合适。他们还提到，他们将提供一个中间件代码片段来实现此解决方案。

---

## 9. NASA如何利用图技术和大型语言模型构建人物知识图谱

**原文标题**: How NASA Is Using Graph Technology and LLMs to Build a People Knowledge Graph

**原文链接**: [https://memgraph.com/blog/nasa-memgraph-people-knowledge-graph](https://memgraph.com/blog/nasa-memgraph-people-knowledge-graph)

美国国家航空航天局利用图技术和大型语言模型（LLMs）创建一个人员知识图谱，彻底改变机构内部的人员分析。该项目由David Meza、Madison Ostermann和Katherine Knott领导，旨在连接员工、项目和技能，以改进专家发现、项目相似性分析和组织洞察力生成。

人员图使用Memgraph来实时管理复杂关系，克服了传统关系数据库的局限性。该解决方案在NASA安全的AWS云上运行，在EC2实例上的Docker中使用Memgraph，利用本地LLM服务器（Ollama），AWS S3用于数据存储，并使用GQLAlchemy通过Cypher进行数据摄取。数据来源包括人事数据、AI/ML项目信息以及使用Ollama从简历中提取的技能。

图模式包括员工、职位、组织、项目、技能和教育详情的节点，所有节点都被标记为“实体”，用于向量索引和GraphRAG。基于RAG的聊天机器人允许用户使用自然语言查询该图，嵌入直接存储在Memgraph中。

美国国家航空航天局计划将该图扩展到超过50万个节点和数百万条边，未来的增强功能将侧重于数据质量、管道自动化和提高RAG准确性。他们选择Memgraph而不是Neo4j的原因是其成本效益以及Python熟练团队易于过渡。该项目正在不断发展，以更好地连接和了解美国国家航空航天局的员工队伍。

---

## 10. Show HN: 一个正在开发的Common Lisp实现，支持ASDF

**原文标题**: Show HN: A Common Lisp implementation in development, supports ASDF

**原文链接**: [https://savannah.nongnu.org/p/alisp](https://savannah.nongnu.org/p/alisp)

此“Show HN”贴文宣布了“alisp”的开发，这是一个托管在 GNU Savannah 上的 Common Lisp 实现。 Alisp 主要由 Andrea Monaco 开发，目前是一个解释器，计划未来具备编译功能，旨在符合 Common Lisp 标准，同时保持灵活性。该实现采用 C89 编写，并可选择使用 GNU readline 和 GNU mp 进行行输入和任意精度算术运算。

该贴文强调 alisp 涵盖了 Common Lisp 的大部分内容，并包括诸如带有单步调试功能的分析器和调试器等特性，而这些特性在其他免费 CL 实现中通常是缺失的。 鼓励用户从 Git 克隆仓库以获取最新更新。

作者欢迎提交错误报告和建议，尽管由于该项目是个人努力，目前不鼓励直接的代码贡献（补丁）。 alisp 在 GPL 第 3 版或更高版本下发布。

最近发布的版本（1.1、1.0、0.999 和 0.99）包括对 LOOP、编译器特性、CLOS、路径名、调试工具和各种 Common Lisp 功能的增强，以及错误修复。该贴文包含指向 README 和 `test.pl` 文件的链接，以及支持该项目的捐赠链接。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 2 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 3 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 4 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 5 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 6 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 7 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 8 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 9 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 10 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 11 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 12 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 13 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 14 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 15 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 16 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 17 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 18 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 19 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 20 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 21 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 22 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 23 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 24 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 25 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 26 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 27 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 28 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 29 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 30 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 31 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 32 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 33 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 34 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 35 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 36 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 37 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 38 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 39 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
