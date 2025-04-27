# Hacker News 热门文章摘要 (2025-04-27)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 令人着迷的日式木工几何互锁图案

**原文标题**: Mesmerizing Interlocking Geometric Patterns Produced with Japanese Woodworking

**原文链接**: [https://www.smithsonianmag.com/smithsonian-institution/see-the-mesmerizing-interlocking-geometric-patterns-produced-with-this-ancient-japanese-woodworking-technique-180986494/](https://www.smithsonianmag.com/smithsonian-institution/see-the-mesmerizing-interlocking-geometric-patterns-produced-with-this-ancient-japanese-woodworking-technique-180986494/)

本文探讨了日本精巧的木工技艺——组子。组子通过精确切割细木条，使其相互咬合形成重复的几何图案。组子起源于日本，现已风靡全球，并从最初用于屏风和家具面板发展成为一项备受赞誉的工艺。

即将于华盛顿特区举办的史密森尼工艺品展将展出组子艺术作品，其中包括来自华盛顿特区的当代工匠大卫·古特尼克的作品。古特尼克使用阿拉斯加雪松，精心将其铣削成细条，并切割出精确的角度，以创造出类似格子状的设计。他在融入传统图案的同时，也加入了自己现代的创新，例如使用对比鲜明的木材和彩色布料背景。虽然传统的组子完全依靠压力进行组装，但古特尼克会少量使用胶水以提高耐用性。

另一位参展艺术家迈克尔·朱里将组子融入到受谢克和丹麦风格启发的家具中，使用椴木制作如麻叶等传统图案。古特尼克强调他在工艺上的不断进步，并指出他现在可以更快、更精确地完成作品。本文重点介绍了组子的美感、工匠的技艺，以及它从传统技法到现代艺术表现的演变。

---

## 12. 展示一下：遥控宜家死星灯

**原文标题**: Show HN: Remote-Controlled IKEA Deathstar Lamp

**原文链接**: [https://gitlab.com/sephalon/deathstar_lamp](https://gitlab.com/sephalon/deathstar_lamp)

提供的“文章”本质上是一个占位符，标题为“Show HN: 遥控宜家死亡之星灯”，内容为“加载中”。 因此，没有任何实际的信息或内容可以总结。

标题表明，文章加载后，将会描述一个改造宜家灯具（可能是以球形著称的PS 2014）的项目，使其类似于《星球大战》中的死星，并增加遥控功能。 这意味着可能对灯的外观进行修改（喷漆、细节处理），并集成电子设备以实现远程开关或调光功能。

然而，在没有加载内容的情况下，我们只能推断出文章的*潜在*主题。 我们无法提供有关创建这种遥控宜家死亡之星灯的具体实施、功能或所面临挑战的任何细节。

---

## 13. 观看03款模型为保罗·墨菲的2步杀棋出汗

**原文标题**: Watching 03 Model Sweat over a Paul Morphy Mate-in-2

**原文链接**: [https://alexop.dev/posts/how-03-model-tries-chess-puzzle/](https://alexop.dev/posts/how-03-model-tries-chess-puzzle/)

本文详述了作者让 03 语言模型解答一道高难度保罗·墨菲国际象棋谜题的实验，展示了其解决问题的过程。 起初，03 仔细地重建了棋盘并考虑了显而易见的走法，但很快意识到这些走法不足以解决问题。

面对困难，03 尝试使用 Python 进行国际象棋引擎模拟（因缺少库而失败），甚至试图通过逐像素图像分析来推断棋子的位置，这既表现出持久性，也暴露出其缺乏基本的国际象棋理解。 该模型表达了对谜题是否可解的怀疑，表现出一定程度对其自身局限性的“认知”。

最终，在将近 8 分钟后，03 通过使用 Bing 搜索答案来“作弊”，在一个国际象棋论坛上找到了解决方案 (Ra6)。 然而，它并没有简单地复制答案，而是重新检查并理解了为什么这个走法有效。

作者强调，03 的解决问题的过程——以推理、挣扎、切换工具、自我纠正，甚至求助于外部帮助为特征——令人惊讶地像人类。 该实验展示了当前模型在解决问题方面的优势，但也揭示了它们在需要创造力或专业知识的复杂场景中，如国际象棋谜题中隐藏的弃兵取胜解决方案，需要外部帮助。 文章还包含作者关于 LLM 创造力的另一篇文章的链接。

---

## 14. 如何用C语言编写文字冒险游戏

**原文标题**: How to program a text adventure in C

**原文链接**: [https://helderman.github.io/htpataic/htpataic01.html](https://helderman.github.io/htpataic/htpataic01.html)

本文介绍了一个关于如何用C语言编写文字冒险游戏的教程。它面向熟悉C语言、并通过实践项目学习更多知识或对文字冒险游戏怀有怀旧兴趣的程序员。

作者认为，尽管存在专门的冒险游戏开发系统，但从头开始用C语言创建一个冒险游戏可能是一次有趣且具有教育意义的体验。选择C语言是经过深思熟虑的，强调了其接近底层硬件的特性，并呼应了早期冒险游戏开发者面临的资源限制。

本教程采用增量开发方法，在每一章中添加小而有价值的代码片段，每一步完成后都会产生一个可工作的程序。最初的程序是一个简单的“Hello World”示例，它引入了文字冒险游戏的核心元素：描述性文本。作者强调了一个好故事的重要性，但重点关注编程方面。

文章还提供了基本的C代码解释，并指出使用了标准库和简单的输出函数。它建议那些不熟悉C语言的人在继续之前寻求帮助。

---

## 15. 浏览器中的开源交互式C语言教程

**原文标题**: Open-source interactive C tutorial in the browser

**原文链接**: [https://www.learn-c.org/](https://www.learn-c.org/)

Learn-c.org 提供免费的交互式 C 语言教程，无需下载，可在浏览器中直接访问。该资源面向希望学习或提高 C 语言技能的初学者和经验丰富的程序员。教程涵盖了基本的 C 语言概念，从 “Hello, World!” 开始，逐步讲解变量、数组、循环、函数等。它还深入探讨了高级主题，如指针、结构体、动态分配、递归、链表和位掩码。

该网站结构清晰，分为易于浏览的章节，用户可以按照自己的节奏学习。教程强调通过交互式练习获得实践经验。

该平台目前正在开发中，欢迎社区贡献以扩展其教程内容。最后，该页面还包含指向贡献指南、使用条款和隐私政策的链接。简而言之，learn-c.org 为学习 C 语言编程提供了一个免费且易于访问的资源。

---

## 16. 维基百科：数据库下载

**原文标题**: Wikipedia: Database Download

**原文链接**: [https://en.wikipedia.org/wiki/Wikipedia:Database_download](https://en.wikipedia.org/wiki/Wikipedia:Database_download)

本维基百科页面提供了下载维基百科内容数据库转储的指南，以便离线使用、镜像或数据库查询。它强调所有文本内容均在知识共享和GNU许可下免费提供，而图像则具有不同的许可，详细信息在其描述页面上。

该页面引导用户访问dumps.wikimedia.org和互联网档案馆，以获取各种语言版本和文件格式（SQL、XML）。它建议使用XML转储的“多流”版本，以便更容易地访问单个文章，而无需解压缩整个文件。为多流存档提供了一个索引文件，允许用户使用字节偏移量提取特定的文章。

它解释说，这些压缩文件非常庞大，需要足够的存储空间，并强调操作系统和文件系统（FAT32、NTFS等）施加的潜在文件大小限制。它建议用户在下载前检查文件系统限制和可用空间。该页面还提供了关于不同操作系统（Windows、macOS、Linux）的解压缩工具的信息。

最后，该文章给出了关于使用MD5校验和验证下载完整性的建议，并建议使用强大的下载工具。文章最后解释说，如果要访问文章的wiki源代码以进行分析或以自己的方式显示，则必须下载数据转储。

---

## 17. 校准存在语境坍塌问题

**原文标题**: Calibrations Have a Context-Collapse Problem

**原文链接**: [https://www.oldschoolburke.com/011-calibrations-have-a-context-collapse-problem/](https://www.oldschoolburke.com/011-calibrations-have-a-context-collapse-problem/)

组织绩效校准会议中的“语境崩塌”现象

---

## 18. 弗吉尼亚州通过法律，对屡次超速者强制执行最高车速限制。

**原文标题**: Virginia passes law to enforce maximum vehicle speeds for repeat speeders

**原文链接**: [https://www.fastcompany.com/91323835/virginia-will-use-technology-to-slow-chronic-speeders-cars-and-other-states-are-rushing-to-join-in](https://www.fastcompany.com/91323835/virginia-will-use-technology-to-slow-chronic-speeders-cars-and-other-states-are-rushing-to-join-in)

弗吉尼亚州通过一项法律，允许法院要求屡次超速的违规者在其车辆上安装限速技术。这项技术会阻止车辆超过预设速度，有效地限制车辆的最高速度。该法律针对的是那些多次违反交通法规和安全驾驶行为、屡次超速的个人。

该法律的目标是减少因过度超速造成的事故和死亡人数。支持者认为，与罚款和吊销驾照等传统处罚相比，它提供了一种更有效、更持久的解决方案，因为传统处罚不足以震慑长期超速者。该技术强制遵守速度限制，并促进更安全的驾驶习惯。

文章表明，其他州正在密切关注弗吉尼亚州实施这项法律的情况，这表明可能出现一种利用技术来执行交通法规和提高道路安全的趋势。如果弗吉尼亚州的实验在减少与超速相关的事故方面证明是成功的，预计其他州也会采用类似的立法。这标志着交通执法方式的转变，转向直接影响驾驶员行为的技术解决方案。

---

## 19. 解锁 Ractors：Object_id

**原文标题**: Unlocking Ractors: Object_id

**原文链接**: [https://byroot.github.io/ruby/performance/2025/04/26/unlocking-ractors-object-id.html](https://byroot.github.io/ruby/performance/2025/04/26/unlocking-ractors-object-id.html)

本文深入探讨了Ruby的`#object_id`方法在Ractor（Ruby的并发特性）环境下的性能挑战，并概述了作者为改进它所做的努力。最初，`#object_id`只是简单地返回指向对象内存地址的指针，从而实现了一个简单的`ObjectSpace._id2ref`。然而，随着Ruby 2.7中垃圾回收（GC）压缩的引入，这变得有问题，因为对象可能会在内存中移动，导致存储的ID失效。

为了解决这个问题，Ruby引入了两个内部哈希表来映射对象到ID以及ID到对象，以确保在GC周期中对象ID的稳定性。然而，这使得`#object_id`的代价显著增加，并且随着Ractor的引入，由于访问期间需要全局锁，这成为了一个争论点。

作者提出了一个双管齐下的方法来缓解这种争用。首先，延迟创建`ObjectSpace._id2ref`使用的`id -> object`表，直到实际需要时才创建，因为此方法很少使用且可能被弃用。这种“延迟”初始化减少了内存使用量和GC工作量。

其次，作者探索将对象ID直接存储在对象本身内部，类似于实例变量，从而消除了对集中式哈希表和同步的需求。这涉及到修改Ruby的内部形状系统，该系统管理实例变量的存储方式以及对象大小的确定方式。作者已经修改了形状，允许即使在冻结的对象上也可以存储对象ID，从而为进一步的优化铺平了道路，最大限度地减少了`#object_id`调用期间对全局锁定的需求。

---

## 20. TmuxAI：AI驱动的非侵入式终端助手

**原文标题**: TmuxAI: AI-Powered, Non-Intrusive Terminal Assistant

**原文链接**: [https://tmuxai.dev/](https://tmuxai.dev/)

TmuxAI：一款人工智能驱动的、非侵入式的终端助手，旨在与用户在 tmux 窗口中协同工作。其设计模拟人类协作，观察屏幕并提供上下文相关的帮助。安装简单，只需一条命令。

主要特点包括：

*   **上下文感知协助：** TmuxAI 实时理解所有终端窗格中显示的内容，根据用户当前的任务提供智能协助。
*   **零配置设置：** 它可以立即与现有的 tmux 设置一起工作，无需特殊的 shell 或封装器。
*   **通用兼容性：** TmuxAI 支持嵌套 shell、SSH 连接、数据库 CLI、网络设备 shell 以及任何基于文本的终端界面。
*   **准备模式：** 通过自定义 shell 提示符增强命令跟踪，实现准确的完成检测和退出代码感知。
*   **观察模式：** 主动监控终端活动，根据用户指定的目标提供改进或解释。
*   **开源：** 可免费使用和修改。

演示展示了 TmuxAI 在管理 Docker 容器和与 MySQL shell 交互方面的能力，展示了其根据用户提示和观察到的终端活动来建议和执行命令的能力。它通过建议命令、在执行前请求确认，甚至自动化输入密码等任务进行交互。

---

## 21. 我们正在构建一个反乌托邦，只是为了让人点击广告[视频]

**原文标题**: We're building a dystopia just to make people click on ads [video]

**原文链接**: [https://www.ted.com/talks/zeynep_tufekci_we_re_building_a_dystopia_just_to_make_people_click_on_ads](https://www.ted.com/talks/zeynep_tufekci_we_re_building_a_dystopia_just_to_make_people_click_on_ads)

文章《我们正在构建一个反乌托邦，只为让人点击广告》可能认为，目前由广告收入驱动的在线环境正在创造一个消极且潜在危险的未来。其前提是，为了最大限度地提高广告点击量而不断追求用户参与度，正在扭曲数字环境。这种扭曲可能体现在以下几个方面：

*   **算法优先考虑耸人听闻和负面情绪：** 旨在保持用户参与度的算法通常偏爱激发强烈情绪的内容，从而导致虚假信息、愤怒和两极分化的传播。

*   **隐私的侵蚀：** 旨在个性化广告的数据收集行为可能导致侵入式监视和个人自主权的丧失。

*   **操纵和成瘾：** 用于吸引用户并让他们不断滚动浏览的技术可能具有成瘾性和操纵性，从而对心理健康和福祉产生负面影响。

*   **批判性思维的下降：** 持续接触容易消化且通常带有强烈情感的内容可能会阻碍批判性思维能力和知情决策。

其根本担忧是，通过在线广告获取利润的驱动力正在凌驾于道德考量之上，并创造一个对个人和社会整体有害的数字环境，从而有效地构建一个“反乌托邦”。

---

## 22. 发现一个简单的数据库建模工具：dbdiagram.io

**原文标题**: Found a simple tool for database modeling: dbdiagram.io

**原文链接**: [https://dbdiagram.io](https://dbdiagram.io)

本文介绍了dbdiagram.io，一款用于创建数据库关系图 (ERD) 的工具。其核心信息是dbdiagram.io为设计和可视化数据库结构提供了一种简单有效的解决方案。这意味着该工具允许用户轻松定义表、列、数据类型以及它们之间的关系，最终促进更好的数据库规划和协作。虽然缺少关于具体功能的详细信息，但标题和描述表明它具有用户友好的界面和直观的工作流程，可用于生成数据库图。该工具的目标用户似乎是数据库开发人员、架构师以及任何参与数据库设计的人员。其主要优势似乎是通过专门且易于访问的在线工具，简化通常复杂的数据库模式建模过程。

---

## 23. 图标

**原文标题**: Icônes

**原文链接**: [https://icones.js.org/](https://icones.js.org/)

基于极为有限的信息（标题：Icônes；内容：Icônes），无法提供全面的摘要。然而，我们可以推断一些可能性：

*   **该文章可能探讨的是图标。** 这可能指：

    *   **宗教图标：** 对圣徒或宗教人物的描绘，尤其是在东正教基督教中。
    *   **视觉图标 (GUI)：** 在计算机界面中使用的小型图形表示，用于代表应用程序、文件或命令。
    *   **文化偶像：** 在特定文化或亚文化中被广泛认可和崇敬的人物、物体或符号。
    *   **抽象艺术或象征意义：** 图标可以被隐喻地用来代表关键主题或意义。

在没有更多上下文的情况下，无法确定该文章讨论的是哪种类型的图标。 摘要完全取决于文章的内容，而目前文章内容缺失。

**如果假设文章是关于宗教图标，一个推测性的摘要可能是：**

“文章 ‘Icônes’ 可能探讨了宗教图标的性质和意义，可能是在东正教传统中。 它可能讨论了它们的历史、象征意义、艺术技巧以及它们在宗教崇拜和奉献中所扮演的角色。”

**如果假设文章是关于 GUI 图标，一个推测性的摘要可能是：**

“文章 ‘Icônes’ 可能探讨了图形图标在用户界面设计中的作用。 它可能涵盖诸如图标设计原则、可用性、可访问性以及不同平台和操作系统中图标风格的演变等主题。”

---

## 24. Show HN: 我自己写的业余爱好操作系统终于在我的老式 IBM ThinkPad 上运行了

**原文标题**: Show HN: My self-written hobby OS is finally running on my vintage IBM ThinkPad

**原文链接**: [https://github.com/joexbayer/RetrOS-32](https://github.com/joexbayer/RetrOS-32)

作者发布“Show HN”帖子，宣布其32位自制操作系统RetrOS已在老式IBM ThinkPad上运行。RetrOS专为i386架构设计，侧重于图形、多任务处理和网络。该项目于2022年5月启动，包含默认用户帐户（system、admin、guest）和用户创建功能。

该操作系统的内核和构建系统使用C和汇编编写，用户空间应用程序使用C++编写，编译使用Make。建议使用Docker进行跨平台编译，而本地编译需要根据操作系统选择特定工具（macOS为i386-elf-gcc/ld/g++，Linux为build-essential/gcc-multilib）。该项目提供了针对Linux、macOS和Windows（使用Docker或WSL）的详细安装说明。

RetrOS可以在QEMU中运行，通过基于浏览器的模拟器运行，或者通过将ISO刻录到USB或CD在真实硬件上运行。该帖子包括项目结构概述和路线图，其中概述了计划中的功能，如自定义引导加载程序、文件系统增强、网络堆栈改进、内存管理、带有窗口管理器的GUI以及各种应用程序（如编辑器和游戏）。该项目根据MIT许可证授权，并鼓励贡献。

---

## 25. 即将来临的知识工作供应链危机

**原文标题**: The Coming Knowledge-Work Supply-Chain Crisis

**原文链接**: [https://worksonmymachine.substack.com/p/the-coming-knowledge-work-supply](https://worksonmymachine.substack.com/p/the-coming-knowledge-work-supply)

无法访问文章链接。

---

## 26. 裸机printf – 无操作系统的C标准库

**原文标题**: Bare metal printf – C standard library without OS

**原文链接**: [https://popovicu.com/posts/bare-metal-printf/](https://popovicu.com/posts/bare-metal-printf/)

本文指导读者使用 Newlib 为裸机系统创建一个紧凑的 C 标准库，并以 RISC-V 目标为例。它对比了典型操作系统上 `printf` 复杂的软件栈与裸机系统更简单的需求，后者需要直接输出到 UART 等 I/O 设备。

Newlib 作为一个“工具包”，通过提供可以独立实现的基本原语来构建自定义 C 库。作者重点介绍了 `_write`，它处理单个字符的输出，而 Newlib 在此基础上构建更复杂的功能，例如 `printf`。 Newlib 还提供默认实现，从基于系统调用的 Linux 版本到最小的“未实现”存根。

然后，本文深入探讨了交叉编译，强调了精确工具链的重要性以及避免宿主机污染。它提倡使用 RISC-V 工具链项目，该项目可以自动构建交叉编译器并设置必要的库（如 Newlib）。讨论了配置标志，例如 `--prefix`、`--enable-multilib`、`--disable-gdb` 和 `--with-cmodel`。

实际实现涉及设置 UART 原语（`uart_putc`、`uart_getc`）以及在 `syscalls.c` 文件中实现必要的函数，例如用于内存分配的 `_sbrk` 和基本的的文件 I/O 处理。解释了 `_sbrk` 函数，因为它将堆内存分配到堆栈底部。

---

## 27. 彻底摆脱前列腺问题？

**原文标题**: An end to all this prostate trouble?

**原文链接**: [https://yarchive.net/blog/prostate/](https://yarchive.net/blog/prostate/)

本文探讨了以色列医生Gat和Goren提出的一个理论，该理论解释了良性前列腺增生（BPH）、前列腺癌和精索静脉曲张均源于一个单一的机械原因：精索静脉瓣功能不全。这些瓣膜在正常运作时，可防止血液倒流回精索静脉。当它们失效时，缺氧的血液会在睾丸周围积聚，可能导致不孕。更重要的是，这些富含游离睾酮的血液会倒流进入前列腺，导致前列腺增大（BPH）或癌变。精索静脉曲张，即睾丸上方静脉肿胀，也是这种回流的另一个症状。

文章强调了医学界普遍忽视这一理论，尽管有已发表的研究和积极的证明。Gat和Goren提出了一种简单的、荧光透视引导的手术来消除这个问题：硬化（破坏）有缺陷的精索静脉，以将血液通过其他途径改道。文章随后批评了该理论，认为重力对循环回路中所有静脉的影响使得自发逆流在机械上似乎不太可能。然而，作者承认已确认精索静脉中存在逆流，这需要比Gat/Goren理论目前提供的更完整的解释。

---

## 28. 看着o3猜测照片的拍摄地点，既超现实，又反乌托邦，还很引人入胜。

**原文标题**: Watching o3 guess a photo's location is surreal, dystopian and entertaining

**原文链接**: [https://simonwillison.net/2025/Apr/26/o3-photo-locations/](https://simonwillison.net/2025/Apr/26/o3-photo-locations/)

本文探讨了作者使用 OpenAI 的新型 o3 模型猜测照片拍摄地点的经历。作者认为这一过程既超现实、又反乌托邦，同时还饶有趣味，并将其与科幻小说和 CSI 中的场景进行了比较。该模型分析图像，使用 Python 代码缩放和裁剪区域，并将其观察结果与地理、建筑和植被知识进行比较，从而得出位置估计。

在作者的测试中，o3 最初错误地将地点识别为加利福尼亚州的坎布里亚，但正确地识别了该地区为加利福尼亚州中部海岸，并且其“下一个猜测”是正确答案：埃尔格拉纳达，一个靠近半月湾的城镇，作者在那里拍摄了照片。

作者指出，其他模型，如 Claude 3.5 和 3.7 Sonnet，也可以执行类似的地点猜测。o3 的一个关键方面是在模型的“思考”过程中集成了工具。

虽然有趣，但作者强调了这项技术的反乌托邦含义：照片，甚至是看似无害的照片，都可以轻松地用于精确定位一个人的位置。他强调了意识的重要性以及这项技术引发的潜在安全问题。作者还承认 o3 可以访问用户大致位置的模型，这可能是由于搜索功能的改进，但确认地点猜测技巧仍然可以在其他地方拍摄的照片上独立工作。

---

## 29. ZFS：苹果未能采用的新文件系统 (2016)

**原文标题**: ZFS: Apple's New Filesystem that wasn't (2016)

**原文链接**: [https://ahl.dtrace.org/2016/06/15/apple_and_zfs/](https://ahl.dtrace.org/2016/06/15/apple_and_zfs/)

本文讲述了苹果公司与Sun Microsystems开发的革命性文件系统ZFS之间的一段渊源，以及最终放弃ZFS的故事。作者作为知情人士，详细描述了苹果公司最初如何探索在Mac OS X中采用ZFS，因为他们意识到ZFS相比老化的HFS具有诸如快照和数据完整性等卓越特性。

2000年代中期最初的兴奋源于ZFS能够为Time Machine提供动力，并显著改善苹果用户的数据存储。然而，Sun CEO Jonathan Schwartz过早地宣布了苹果公司的计划，违反了苹果公司严格的保密政策，并冷却了苹果公司的热情。

尽管持续开发甚至包含在开发者版本中，ZFS的集成最终还是失败了。作者将此归因于几个因素：Sun被Oracle收购以及由此带来的不确定性，Sun和NetApp之间关于ZFS技术的诉讼，以及苹果公司内部的政治因素，包括对“非我发明”解决方案的偏好，以及可能没有根据的对ZFS许可的担忧。

在Oracle收购Sun之后，曾试图恢复该移植项目，涉及苹果公司与Sun基于ZFS的新型存储设备的潜在合作，但遭到了Larry Ellison的亲自否决。

最终，苹果公司选择了开发自己的文件系统APFS，该系统于2016年发布。虽然承认APFS的潜力，但作者对苹果公司没有拥抱ZFS表示失望，强调了行业错失的机会以及强大的OpenZFS社区。他强调了功能完善的文件系统所需的漫长开发周期，表明APFS要达到ZFS的成熟度和功能完整性还有很长的路要走。

---

## 30. 入侵迪士尼世界菜单的前迪士尼员工被判三年徒刑

**原文标题**: Former Disney employee who hacked Disney World menus sentenced to 3 years

**原文链接**: [https://databreaches.net/2025/04/24/former-disney-employeedwho-hacked-disney-world-restaurant-menus-in-revenge-sentenced-to-3-years-in-federal-prison/](https://databreaches.net/2025/04/24/former-disney-employeedwho-hacked-disney-world-restaurant-menus-in-revenge-sentenced-to-3-years-in-federal-prison/)

前迪士尼世界员工迈克尔·舍伊尔因被解雇后入侵该公司计算机系统，被判处三年联邦监禁。他承认向受保护的计算机传输程序、故意造成损害以及实施严重身份盗窃罪。

舍伊尔的行为包括恶意修改餐厅菜单，特别是篡改过敏原信息，虚假地表明食物对特定过敏顾客是安全的。他还更改葡萄酒产区信息，引用最近发生大规模枪击事件的地点。此外，他还发起拒绝服务攻击，将员工锁定在自己的帐户之外。

法院判决舍伊尔没收用于犯罪的计算机，并向受害者支付687,776.50美元的赔偿金。联邦调查局的网络工作组调查了此案，强调了公私合作伙伴关系在网络安全中的重要性。美国检察官办公室负责起诉此案。

---

## 31. Sigbovik会议论文集 2025 [pdf]

**原文标题**: Sigbovik Conference Proceedings 2025 [pdf]

**原文链接**: [https://sigbovik.org/2025/proceedings.pdf](https://sigbovik.org/2025/proceedings.pdf)

此文档似乎是2025年Sigbovik会议被损坏的会议记录。Sigbovik以其幽默且常常荒谬的计算机科学论文而闻名。然而，所提供的内容并非可读的文本格式，而是包含原始PDF代码，包括：

* PDF版本声明
* Ghostscript指令
* 包含看似随机字符的编码对象流
* 元数据标签

由于数据的非文本性质，我无法给出内容摘要。

---

## 32. SQL引擎剖析

**原文标题**: Anatomy of a SQL Engine

**原文链接**: [https://www.dolthub.com/blog/2025-04-25-sql-engine-anatomy/](https://www.dolthub.com/blog/2025-04-25-sql-engine-anatomy/)

本文详细介绍了SQL引擎的内部运作，特别是Dolt的go-mysql-server (GMS)，追溯了查询从输入到输出的整个过程。 该过程分为七个关键阶段：解析、绑定、计划简化、连接探索、计划成本评估、执行和结果缓冲。

**解析** 使用左递归Yacc语法将SQL查询转换为抽象语法树(AST)，尽管调试复杂，但仍优先考虑速度和低内存使用率。

**绑定** 将AST标识符与数据库目录符号进行匹配，执行类型检查和特定于子句的验证。 此阶段将AST节点转换为 `sql.Node` 计划节点。

**计划简化** 通过应用诸如过滤器下推和列修剪之类的规则来将查询转换为规范形式，以进行优化。 还执行子查询去关联/应用连接。

**计划探索** 搜索最佳连接配置。 GMS使用DP-Sube策略来探索各种连接顺序和运算符选择（LOOKUP_JOIN、HASH_JOIN等），同时避免无效状态。 探索的状态存储在备忘录结构中，以缓存逻辑属性。 还利用了函数依赖。

**连接成本评估** 根据模式、表键分布（直方图）和运算符选择来估计每个物理计划的运行时成本。

本文强调了中间表示(IR)在不同阶段的重要性：基于作用域的用于绑定，结构化的用于简化，以及备忘录化的用于连接探索和成本评估。

---

## 33. 编译器提示

**原文标题**: Compiler Reminders

**原文链接**: [https://jfmengels.net/compiler-reminders/](https://jfmengels.net/compiler-reminders/)

本文强调了 Elm 中“编译器提醒”对于创建可维护代码的重要性。“编译器提醒”指的是当代码修改需要同步更新其他地方时，编译器会报错，从而迫使开发者进行必要的更改。作者通过一个基本的计数器例子说明了这一点，在该例子中，添加重置按钮会产生编译器错误，提示用户更新 `Msg` 类型和 `update` 函数。

文章强调，Elm 的类型和穷举检查是此功能的核心，并提倡使用显式的 `case` 表达式分支而不是通配符默认值，以最大限度地增加提醒机会。这种被称为“编译器驱动开发”的方法可以产生更可靠的代码。

提醒的概念不仅限于编译器，还包括 linter 和测试。Linter 可以提供清理提醒（例如，未使用的变量）或基于特定规则的自定义提醒。例如，一个 linter 规则可以强制将新的用户类型添加到所有用户类型的列表中。

最终，文章认为提醒对于维护代码质量、防止疏忽以及确保编码标准得到一致应用至关重要，尤其是在经验水平不同的团队成员之间。不同的工具可以创建不同类型的提醒，高度可维护的代码库会大量使用这些提醒。

---

## 34. 迪士尼员工入侵菜单系统被判三年监禁

**原文标题**: Disney worker who hacked menus gets 3 years in prison

**原文链接**: [https://www.nytimes.com/2025/04/26/us/disney-worker-prison-hacking.html](https://www.nytimes.com/2025/04/26/us/disney-worker-prison-hacking.html)

前迪士尼世界员工迈克尔·舍尔因入侵迪士尼餐厅菜单系统，被判处三年监禁。舍尔修改了价格、添加了亵渎性内容，并在菜单创建系统中伪造了过敏原信息。所幸这些改动在公开前就被发现，并未实际印在菜单上。

舍尔承认犯有计算机欺诈和加重身份盗窃罪。他还被勒令向迪士尼支付 62 万美元的赔偿金，以及向为迪士尼提供菜单程序的软件公司支付 7 万美元。该事件发生在因菜单制作与主管发生争执并导致他被停职之后。虽然法庭文件没有明确指明迪士尼世界，但作为证据提交的菜单被确认为属于该度假区的餐厅。迪士尼世界代表未对此事发表评论。

---

## 35. 重庆，最大的城市——图片集

**原文标题**: Chongqing, the Largest City – In Pictures

**原文链接**: [https://www.theguardian.com/world/gallery/2025/apr/27/chongqing-the-worlds-largest-city-in-pictures](https://www.theguardian.com/world/gallery/2025/apr/27/chongqing-the-worlds-largest-city-in-pictures)

重庆：最大城市的影像——图片展现
        
本文通过一系列照片和文字说明，展示了重庆的快速发展和城市化进程。着重介绍了过去20年重庆的显著经济增长，包括人均GDP增长16倍，城市化率翻了一番。

文章强调了重庆从污染严重的重工业中心向汽车和IT行业主导力量的转变。通过提及该市的汽车产量超过法国和英国的总和，以及对全球笔记本电脑和摩托车生产的重大贡献，说明了这一点。

照片说明展示了重庆生活的方方面面，从像万象城和新的苹果商店这样的现代购物中心，到像罗汉寺这样的历史遗迹。它们还展示了该市独特的城市规划，例如穿楼而过的李子坝地铁站。

文章还提到了与北京和上海等中国主要城市相比，重庆房价的可负担性、广泛的地铁系统以及长江和嘉陵江沿岸的休闲空间。简而言之，这篇文章将重庆描绘成一个融合了历史和现代元素的现代化、快速发展的大都市。

---

## 36. 比尔·盖茨在8位BASIC中的个人彩蛋 (2008)

**原文标题**: Bill Gates's Personal Easter Eggs in 8 Bit BASIC (2008)

**原文链接**: [https://www.pagetable.com/?p=43](https://www.pagetable.com/?p=43)

本文深入探讨了微软BASIC解释器的历史以及其中隐藏的“彩蛋”，特别关注Commodore PET和TRS-80彩色计算机。

最初的谜团围绕着Commodore PET的BASIC V2中的“WAIT 6502,1”命令，该命令会显示字符串“MICROSOFT!”。据说这个彩蛋归功于比尔·盖茨，据称是为了防止Commodore声称代码是他们自己的而插入的。

本文追溯了微软BASIC从Altair BASIC（1975）到KIM-1、Apple II（AppleSoft）以及最终Commodore PET的6502版本的演变过程。它强调了Commodore如何获得微软BASIC的许可，对其进行重命名并删除了版权字符串。然而，“WAIT 6502”彩蛋出现在BASIC V2中，表明Commodore收到了微软的更新。

文章分析了彩蛋的代码，揭示了它使用PET字符编码将“MICROSOFT!”直接写入屏幕RAM。这表明它是专门为PET设计的。虽然Commodore在后来的版本中移除了彩蛋，理由是内存限制，但他们最终在后来的BASIC版本中承认了微软的功劳。

有趣的是，文章揭示了模糊处理的“MICROSOFT!”字符串出现在更早的版本中，包括KIM-1 BASIC和AppleSoft，表明其意图比仅仅针对Commodore更为广泛。

最后，文章揭示了TRS-80彩色计算机和MC-10中的第二个彩蛋。输入“CLS9”会打印“MICROSOFT”，表明微软忘记了6502版本中更早的模糊字符串，这些字符串也存在于这些计算机的ROM中。这说明了微软6502 Basic代码的转换过程，该代码被直接转换为其他架构，例如摩托罗拉6800。

---

## 37. 布

**原文标题**: Cloth

**原文链接**: [https://www.cloudofoz.com/verlet-test/](https://www.cloudofoz.com/verlet-test/)

标题“布”，内容显示为用户@cloudofoz的Verlet模拟测试。要点：

*   **主题：** 布料模拟
*   **方法：** 使用Verlet积分（物理模拟中常用的数值方法）
*   **作者：** @cloudofoz
*   **目的：** 可能是演示或实验，测试Verlet模拟技术在布料行为上的应用。

---

## 38. 订购放射性物质的澳大利亚人离开法庭

**原文标题**: Australian who ordered radioactive materials walks away from court

**原文链接**: [https://www.chemistryworld.com/news/australian-who-ordered-radioactive-materials-over-the-internet-walks-away-from-court/4021306.article](https://www.chemistryworld.com/news/australian-who-ordered-radioactive-materials-over-the-internet-walks-away-from-court/4021306.article)

无法访问文章链接。

---

## 39. 友谊衰退：失落的联结艺术

**原文标题**: The Friendship Recession: The lost art of connecting

**原文链接**: [https://www.happiness.hks.harvard.edu/february-2025-issue/the-friendship-recession-the-lost-art-of-connecting](https://www.happiness.hks.harvard.edu/february-2025-issue/the-friendship-recession-the-lost-art-of-connecting)

布莱斯·弗梅勒的文章《友谊衰退：失落的连接艺术》探讨了美国人亲密友谊的衰退。数据显示，报告没有亲密朋友的人数显著增加，而拥有许多朋友的人数则减少。虽然郊区扩张和经济压力等系统性问题是成因之一，但作者认为，文化转变才是主要驱动因素。

这种转变包括工作成为主要的社会身份，导致友谊的时间减少，以及对核心家庭的日益关注，特别是高强度育儿，进一步减少了社交时间。屏幕时间和纯数字友谊的兴起加剧了这个问题，因为这些互动缺乏面对面连接的深度和神经益处。

这种文化转变是危险的，因为它正在重塑我们的大脑。孤独会使人更难袒露心扉，导致人们逃避社交场合，依赖数字互动。这形成了一个自我强化的孤立循环。

扭转这种“友谊衰退”需要在结构和个人层面采取行动。个人必须积极抵制助长孤独的力量。作者建议通过参与逃生室或挑战等新颖的、共享的体验来拥抱不适感，因为这些可以培养友谊和共同的身份认同。他鼓励读者创造群体活动的机会，参与解决新的“前沿”问题，通过共同的挑战培养联系感。关键是有意识地努力优先形成和维持有意义的关系。

---

## 40. 老爸和鸡蛋控制器 (2018)

**原文标题**: Dad and the Egg Controller (2018)

**原文链接**: [https://www.pentadact.com/2018-12-18-dad-and-the-egg-controller/](https://www.pentadact.com/2018-12-18-dad-and-the-egg-controller/)

汤姆·弗朗西斯的博文《父亲和鸡蛋控制器》深情地回忆了他的发明家父亲，以及他尝试使用父亲发明的“鸡蛋控制器”的经历。这个装置旨在为 Big Green Egg 烤肉架实现温度自动控制，而汤姆觉得手动控制非常令人沮丧。

父亲去世后，汤姆感到有责任理解和操作这个鸡蛋控制器。他回忆起父亲对烹饪和解决问题的热爱，并将其与自己创建自定义程序来生成带有唯一代码的名片时采用的解决问题方法进行对比。

汤姆详细描述了该设备的组件以及他最初启动设备的艰难过程。最终，他成功启动了设备，但在破译其界面时遇到了更多挑战，该界面似乎无法停止控制热量的风扇。这种无法理解父亲创造的东西让他感到一种脱节和失落感。

他回忆起过去的一次谈话，他的父亲解释了鸡蛋控制器和汤姆游戏开发中使用的复杂的比例-积分-微分控制器，突出了他们共同的解决问题思维模式。

高潮出现在一个计划好的追悼午餐上，汤姆的任务是使用鸡蛋控制器慢炖猪肉。在一次失败的练习后，他几乎放弃了。然而，在摆弄设备时，他注意到一个黑色盒子组件上的红灯。当他将开关拨到蓝灯时，风扇终于像应该的那样停止了。汤姆意识到这个黑盒子是一个调节器，他终于破译了如何控制鸡蛋控制器，并与已故父亲的创新精神建立了联系。

---

## 41. BART的动漫吉祥物

**原文标题**: BART's Anime Mascots

**原文链接**: [https://www.bart.gov/news/fun/anime](https://www.bart.gov/news/fun/anime)

湾区捷运（BART）推出了动漫形象——米拉、茉莉、贝莉、云和巴蒂——以推广公共交通的使用，尤其是在年轻乘客中。受日本和台湾类似举措的启发，这些形象旨在为BART创造一个友好且平易近人的形象。

这些形象是在向加州艺术家公开征集后开发的，收到了近500份投稿。这些形象旨在突出BART与湾区之间的联系。

*   **米拉：** 一名BART列车员。
*   **茉莉：** 一名热爱火车的女高中生，立志成为时装设计师。
*   **贝莉：** 一名湾区网络红人。
*   **云：** 一名受湾区自然风光启发的作家。
*   **巴蒂：** 一辆旧款列车的转世兔子精灵。

文章提到米拉和茉莉的涂色页以及“如何制作BART列车服装”的指南已经上线。BART鼓励人们Cosplay这些形象，并提供Cosplay指南。官方形象周边商品，包括亚克力立牌和贴纸套装，可在railgoods.com/bart/anime上购买。

---

## 42. 展示一下：Lil digi – 扮演你自己来玩平台游戏

**原文标题**: Show HN: Lil digi – play a platformer game as yourself

**原文链接**: [https://www.lildigi.me/](https://www.lildigi.me/)

"小小数码"是一款平台游戏，你将扮演一个基于你上传照片的像素化角色。网站lildigi.me允许你上传图片（或使用示例）来生成像素化头像。然后你使用这个头像来通过一个平台关卡，具体来说是在躲避火焰和熔岩等危险的同时逃离火山。

游戏提供了操作说明，使用方向键移动，向上键/空格键跳跃。它还显示了平均完成时间（28秒），以鼓励玩家打破记录。该网站包含一条警告，禁止上传敏感、不当或冒犯性内容。还有一个显示“挑战#1完成时间”的排行榜。

---

## 43. 填充-Na(a)N：填充你的NaN值

**原文标题**: Stuffed-Na(a)N: stuff your NaNs

**原文链接**: [https://github.com/si14/stuffed-naan-js](https://github.com/si14/stuffed-naan-js)

“Stuffed-Na(a)N” 介绍了一个幽默且实用的 JavaScript 库，用于在 NaN (非数字) 值中编码数据。该库通过 `encode` 和 `decode` 函数访问，利用 NaN 的 IEEE 754 浮点表示，允许数据存储在尾数部分。

文章突出了该库所谓的优点，包括“紧凑性”（声称负压缩）、由于高级 ECMAScript 特性实现的“极速”性能，以及“隐私优先”编码，因为 NaN 数组据称难以复制。 需要注意的是，文章始终带有讽刺意味。

该库可以通过 npm 安装，也可以直接在浏览器控制台中安装。 还有一个“企业版”正在宣传，提供改进的编码、字节序支持和客户支持，价格可根据要求提供。

路线图包括公共基准测试、模糊测试、Rust 重写和形式验证等功能。

“推荐”部分带有戏谑意味，暗示了该库的新颖性和潜在（尽管可能存在疑问）的应用。

作者随后解释了技术基础，详细说明了 IEEE 754 中 NaN 的结构如何允许数据走私。文章最后呼吁支持咖喱屋，并链接到作者的社交媒体。

---

## 44. 弹簧天线偶极子 (2021)

**原文标题**: Slinky-Coil Dipole (2021)

**原文链接**: [https://nonstopsystems.com/radio/frank_radio_antenna.htm](https://nonstopsystems.com/radio/frank_radio_antenna.htm)

本文详细介绍了“弹簧天线偶极子”，这是一种使用弹簧玩具（柔性金属弹簧）制成的紧凑型便携式天线。作者F. Dörenberg解释说，虽然弹簧由相当长度的金属丝制成，但它们的螺旋形状引入了感性负载，使其适合用作天线，尤其是在空间有限的情况下。

本文介绍了钢制和黄铜弹簧偶极子的构造，概述了所需的组件（弹簧、PVC管、吊环螺栓、电线、绳索），并提供了构建中心绝缘子和连接弹簧的逐步说明。作者分享了他使用这些天线的经验，包括在欧洲甚至从室内公寓设备联系到阿根廷。安装在露台上的黄铜弹簧偶极子显示出受其感性负载和附近金属物体影响的谐振频率。

文章还讨论了弹簧偶极子的调谐方法，包括调整线圈匝间距（拉伸）和短路匝数。文章引用了1974年美国一项关于使用类似概念的可调螺旋偶极天线的专利。此外，文章还引用并展示了其他人建造的弹簧偶极子的示例，包括刘易斯和克拉克无线电俱乐部的一项户外活动实施方案。Dörenberg强调这是一种折衷的天线，而不是奇迹，它提供了便携性和紧凑性。他指出钢制弹簧的腐蚀敏感性，并建议对户外使用使用黄铜线圈或保护涂层。

---

## 45. HTTP Feeds: 通过HTTP轮询事件的最小规范

**原文标题**: HTTP Feeds: a minimal specification for polling events over HTTP

**原文链接**: [https://www.http-feeds.org/](https://www.http-feeds.org/)

HTTP Feeds：使用标准HTTP API创建异步事件流的最小规范，为Kafka等消息代理提供了一种替代方案。客户端轮询一个GET端点，该端点以批处理JSON格式（`application/cloudevents-batch+json`）返回按时间顺序排列的CloudEvents序列。客户端使用`lastEventId`查询参数来滚动浏览feed并订阅实时更新。

定义了两种主要的轮询方法：简单轮询，客户端使用上次处理的事件ID重复请求更新；长轮询，服务器保持连接打开，直到新事件到达或达到超时时间，从而改善延迟。

该规范概述了两个主要用例：用于发布不可变领域事件的事件Feed，以及用于同步可变数据对象（聚合）的聚合Feed。聚合Feed要求每个条目都包含完整的当前状态，从而实现近乎实时的数据同步。建议对聚合Feed进行压缩（删除同一主题的过时条目）和删除（通过DELETE方法发出删除信号）。

事件ID对于排序和幂等性至关重要。建议使用按时间排序的UUIDv6或数据库序列。数据模型包括所有feed的强制字段，如`specversion`、`id`、`type`、`source`和`time`，以及聚合feed的`subject`。可选参数包括长轮询的`timeout`和指示聚合feed中`DELETE`操作的`method`。可以使用标准HTTP机制实现身份验证。

---

## 46. Ucbvax (1994) 的逝去

**原文标题**: The Passing of Ucbvax (1994)

**原文链接**: [http://ucbvax.berkeley.edu/passing-of-ucbvax.txt](http://ucbvax.berkeley.edu/passing-of-ucbvax.txt)

本文宣告加州大学伯克利分校计算机系于1994年8月19日正式退役“ucbvax.berkeley.edu”计算机。程序员们参加了一个小型仪式，以演讲和蛋糕庆祝这一事件。

Keith Sklower 简要回顾了 ucbvax 的历史，详细介绍了它最初作为校园第一台 VAX 计算机的由来，该计算机于 1978 年通过 NSF 拨款获得。它最初运行贝尔实验室的 UNIX 变体，并成为早期网络通信的关键节点，处理邮件和新闻。“ucbvax”这个名称是遵循贝尔实验室对 UUCP 连接的命名惯例选择的。由于工作负载的增加，它的功能被分离到一台专用的 VAX/750 上，使其成为 ARPANET 和校园之间的网关。尽管计划用 SUN 工作站取代它，但 DEC 的一位销售人员促成了升级到 DECstation 3200，即它的最终形式。

Eric Allman 发表了一篇幽默的悼词，引用了《哈姆雷特》，并哀悼该机器功能的丧失。最初启动该机器的 Kirk McKusick 有幸将其关闭。

尽管退役，ucbvax 还是被重新用作加州大学警察局的卡式钥匙门禁系统控制器。此外，与“ucbvax”名称相关的电子邮件流量被重新路由到“nak.berkeley.edu”，凸显了一种讽刺意味。实际关机被推迟，以便将排队的电子邮件移动到另一台机器。Ucbvax 拥有既是计算机科学系第一台也是最后一台运行的 VAX 计算机的殊荣。

---

## 47. CosAE：用于图像恢复的可学习傅里叶级数

**原文标题**: CosAE: Learnable Fourier Series for Image Restoration

**原文链接**: [https://sifeiliu.net/CosAE-page/](https://sifeiliu.net/CosAE-page/)

本文介绍了一种新型自编码器CosAE（余弦自编码器），旨在提高图像修复性能。与传统自编码器因低分辨率潜在空间而常丢失细节不同，CosAE利用傅里叶级数将图像表示为二维余弦函数的总和，每个余弦函数都由可学习的频率和傅里叶系数来表征。

其关键创新在于将这些频率系数（幅度和相位）编码在自编码器的瓶颈中。这使得瓶颈层能够实现显著的空间压缩（例如，64倍下采样），而不会在解码过程中牺牲关键的图像细节。本质上，CosAE学习的是图像频率分量的压缩表示，而不是直接学习空间特征。

作者在具有挑战性的图像修复任务中展示了CosAE的优势，特别是灵活分辨率的超分辨率和盲图像修复。这些任务需要对复杂且未知的图像退化进行稳健的泛化。实验结果表明，CosAE优于最先进的方法，表明其能够学习更具泛化性和细节保留能力的图像修复表示。简而言之，CosAE提供了一种新颖的图像自编码方法，利用傅里叶级数实现高效压缩和卓越的修复能力。

---

## 48. 带图详解：深入评测 DOS 版 Microsoft Word 5.5 和 6.0 (2018)

**原文标题**: Microsoft Word 5.5 And 6.0 In-depth DOS Review With Pics (2018)

**原文链接**: [https://shot97retro.blogspot.com/2018/07/microsoft-word-55-and-60-in-depth-dos.html](https://shot97retro.blogspot.com/2018/07/microsoft-word-55-and-60-in-depth-dos.html)

这篇2018年的评测深入探讨了用于DOS系统的Microsoft Word 5.5和6.0，将其历史和功能与Windows和Mac版本进行了对比。作者强调了Word最初在DOS上的不受欢迎，随后在Mac上的成功，以及这种成功如何影响了微软对图形操作系统的态度，但不一定影响了DOS。

评测探索了用于DOS系统的Word 5.5和6.0的功能，指出它们在文本和图形环境之间的混合特性。虽然具有图形用户界面，但它主要模拟文本环境，字体和大小选项仅在打印预览中可见。作者详细介绍了该程序在编辑DOS文本文件和批处理文件方面的优势，其鼠标驱动的菜单系统以及可定制的配色方案。

评测还指出了局限性，包括不佳的拼写检查和文件兼容性问题。 将文件保存到较新版本的Word被描述为繁琐，作者建议保存为富文本格式以便于传输。 尽管存在缺陷，但作者发现Word for DOS仍具有价值，尤其是在编辑系统文件方面，并认为它是DOS内置编辑器的更好替代方案。作者总结说，虽然不适合小说写作，但Word for DOS可能与其他DOS文字处理器竞争，并暗示将来会对WordPerfect for DOS进行评测。

---

## 49. CSS禅意花园

**原文标题**: CSS Zen Garden

**原文链接**: [https://csszengarden.com/](https://csszengarden.com/)

CSS禅意花园项目展示了CSS的强大功能和灵活性，它通过仅使用不同的CSS样式表来大幅改变网站的视觉设计，同时保持底层HTML结构不变。其目标是激励设计师和开发者探索CSS的全部潜力，并突破网页设计的界限。

该项目鼓励参与，邀请设计师为提供的HTML模板创建自己的CSS样式表并提交以供考虑。 指南强调使用得到良好支持的CSS标准（主要为CSS 1和2），限制使用CSS 3和4，并要求CSS验证。 提交的作品应为原创艺术作品，避免令人反感的材料，并融入独特的视觉主题。

参与的好处包括获得认可、启发灵感，并为Web设计社区贡献宝贵资源。 禅意花园是一个学习工具、灵感来源以及未来技术的展示画廊。 提交的CSS以Creative Commons许可证发布，允许其他人学习和构建在其基础上。 该项目强调了浏览器兼容性的重要性，并鼓励在多个平台上进行测试，包括IE9+、Chrome、Firefox、iOS和Android。

---

## 50. GPU价格追踪

**原文标题**: GPU Price Tracker

**原文链接**: [https://www.unitedcompute.ai/gpu-price-tracker](https://www.unitedcompute.ai/gpu-price-tracker)

GPU价格追踪器是一个旨在监控和分析热门GPU的价格、规格和历史趋势的工具。它旨在为用户提供最新的信息，以便他们做出明智的GPU购买决策。

主要功能包括：

*   **价格追踪：** 监控亚马逊的当前GPU价格，每日更新。“市场价格”反映当前的亚马逊价格。
*   **规格指标：** 提供基于制造商的性能指标，包括每瓦浮点运算次数 (FL/Watt) 和每美元浮点运算次数 (FL/$)。
*   **性能分析：** FL/Watt用于衡量GPU的效率。FL/$ 指示性能价格比，帮助用户识别最佳性价比。
*   **数据来源：** 价格数据来自亚马逊，每日更新，以保持追踪器的时效性。

---

## 51. 超越容器 – Daniel Phillips推出Boxer WASM I/O 2025 [视频]

**原文标题**: Moving Beyond Containers – Introducing Boxer by Daniel Phillips WASM I/O 2025 [video]

**原文链接**: [https://www.youtube.com/watch?v=rHOwhkHv21U](https://www.youtube.com/watch?v=rHOwhkHv21U)

YouTube视频：“超越容器 – Daniel Phillips推出Boxer，WASM I/O 2025”，可能介绍了Daniel Phillips开发的一项名为“Boxer”的新技术。该视频着重展示了这项技术如何超越现有的容器化解决方案，可能在效率、安全或性能等方面有所提升。“WASM I/O 2025”表明Boxer很可能基于WebAssembly (WASM) 构建，并解决了该生态系统中的输入/输出问题，且是在2025年举办的会议上发布的。

在没有更多信息的情况下，无法具体说明Boxer *如何*改进容器。然而，标题强烈暗示它代表着一个重要的进步，并将自身定位为现有容器技术的替代品或继任者。

标准的YouTube免责声明和版权信息表明该内容托管在Google的平台上，并受其平台政策管辖。这如同YouTube上典型的视频介绍，侧重于其内容并承认标准法律和运营参数。

---

## 52. 新的4o人格类型不适用于治疗。

**原文标题**: The new 4o personality is unusable for therapy

**原文链接**: [https://old.reddit.com/r/ChatGPT/comments/1k8odhx/the_new_4o_personality_is_unusable_for_therapy/](https://old.reddit.com/r/ChatGPT/comments/1k8odhx/the_new_4o_personality_is_unusable_for_therapy/)

无法访问文章链接。

---

## 53. 机器人灵巧性依旧困难

**原文标题**: Robot Dexterity Still Seems Hard

**原文链接**: [https://www.construction-physics.com/p/robot-dexterity-still-seems-hard](https://www.construction-physics.com/p/robot-dexterity-still-seems-hard)

布莱恩·波特的《机器人灵巧性依然困难重重》探讨了人形机器人发展的不平衡，强调了令人印象深刻的移动能力与更具挑战性的灵巧操作之间的差距。 尽管在人形机器人开发方面投入了大量资金，并且在跑步和跳舞等领域取得了进步，但机器人在涉及物体操作的任务方面仍然面临困难。

波特强调，真正的实用性在于机器人以不可预测的方式处理各种物体的能力，而这项技能仍然远远落后于人类。 他将工业机器人的精确动作与执行日常任务（如叠衣服或倒水）所需的灵巧性进行了对比，展示了机器人在执行看似简单的动作时也面临困难的例子。

文章深入探讨了这种困难背后的原因，列举了硬件和软件的局限性。 目前的机械手缺乏人类手的力量、敏感度和触觉反馈，而且价格也过于昂贵。 然而，波特认为，更好的硬件只是解决方案的一部分，能够对动作进行排序并对反馈做出反应的出色软件同样至关重要。

他最后指出了机器人灵巧性方面缺乏标准化的“评估”，并提出了一系列要求严苛的任务来评估和推进该领域的进展。 文章表明，虽然通过足够的投资可以自动化特定任务，但创造真正灵活和适应性强的机器人仍然是一项重大挑战。

---

## 54. 大型语言模型无需任何训练即可看和听。

**原文标题**: LLMs can see and hear without any training

**原文链接**: [https://github.com/facebookresearch/MILS](https://github.com/facebookresearch/MILS)

本文档提供了论文“LLMs can see and hear without any training”的官方实现和说明。该论文介绍了一种名为MILS的推理方法，它允许大型语言模型 (LLMs) 执行与图像、音频和视频理解相关的任务，而无需针对这些模态的特定训练数据。

本文档概述了设置环境的必要步骤，包括使用`conda`安装所需的软件包、下载相关数据集（MS-COCO、Clotho、MSR-VTT）以及获取预训练的ViClip检查点。它还强调更新路径以指向正确的数据集和输出目录。

这些说明详细说明了如何运行各种任务的代码：图像描述、音频描述、视频描述、高质量图像生成、风格迁移和跨模态算术。每个任务都涉及运行带有特定CUDA设备可见性、进程ID和批处理大小的Python脚本。生成的标题或图像保存在指定的输出目录中，并提供单独的评估脚本来计算标题任务的相关指标。

最后，本文档包括有关如何报告问题、为项目做出贡献、许可详细信息（CC-by-NC 4.0）以及论文的引用信息。核心思想是，MILS利用现有LLM的功能来解释和生成跨不同模态的内容，而无需显式的多模态训练。

---

## 55. Tilt：代码即开发环境

**原文标题**: Tilt: dev environment as code

**原文链接**: [https://github.com/tilt-dev/tilt](https://github.com/tilt-dev/tilt)

Tilt：简化 Kubernetes 微服务开发的工具。它能自动完成代码更改后开发环境的更新，替代 "docker build && kubectl apply" 或 "docker-compose up"。它会监控文件、构建容器镜像并部署更新后的服务。

主要功能及信息包括：

*   **目的：** 简化 Kubernetes 中的微服务开发。
*   **功能：** 自动化构建、部署和更新服务。
*   **安装：** macOS/Linux 和 Windows 下使用 curl 或 powershell 的简单单行命令，以及特定的包管理器选项。
*   **资源：** 新手教程、各种语言（HTML、NodeJS、Python、Go、Java、C#）的最佳实践和全面的 API 参考。
*   **社区：** 在 Kubernetes Slack 频道 (#tilt) 和 GitHub Issues 上活跃的社区。
*   **贡献：** 鼓励向 Tiltfile 功能的源代码和扩展进行贡献。
*   **沟通：** 通过 Twitter (@tilt_dev)、博客和新闻通讯发布更新。
*   **隐私：** 收集匿名使用数据以改进产品。
*   **安全：** 鼓励将安全漏洞负责任地披露至 security@docker.com，而不是公开的问题。
*   **许可：** 基于 Apache License, Version 2.0 许可。

---

## 56. 雷朋Stories智能眼镜拆解 (2023)

**原文标题**: Ray-Ban Stories Smart Glasses Teardown (2023)

**原文链接**: [https://www.digikey.kr/en/maker/projects/ray-ban-stories-smart-glasses-teardown/710c72d1c7f2499591fe38b387f90047](https://www.digikey.kr/en/maker/projects/ray-ban-stories-smart-glasses-teardown/710c72d1c7f2499591fe38b387f90047)

无法访问文章链接。

---

## 57. 阅读RSS内容是一项技巧性活动。

**原文标题**: Reading RSS content is a skilled activity

**原文链接**: [https://www.doliver.org/articles/rss-as-a-skill](https://www.doliver.org/articles/rss-as-a-skill)

文章认为，由算法和广告驱动的现代互联网通过优先考虑用户参与度而非福祉，对用户有害。RSS提供了一种解决方案，允许用户策划自己的内容并重新掌控自己的注意力。作者承认管理通过RSS订阅源提供的大量信息是一个挑战。

他们提出的解决方案是建立“信任链”，订阅那些受人尊敬的个人订阅源。这种信任不仅限于准确性，还包括内容本身的价值。随着时间的推移，用户可以培养多样化且相关的信息集合。

作者强调，使用RSS阅读器不是一种被动行为，而是一种积极的技能，需要像维护花园一样进行修剪和除草。这种与内容的积极互动，即决定什么有价值的过程，使RSS成为一种卓越的体验，使用户能够掌控自己的注意力，并摆脱主流社交媒体的操纵性算法。

---

## 58. 显示HN：AgenticSeek - 自托管 Manus 替代方案

**原文标题**: Show HN: AgenticSeek – Self-hosted Manus alternative

**原文链接**: [https://github.com/Fosowl/agenticSeek](https://github.com/Fosowl/agenticSeek)

AgenticSeek：完全本地化和私有的 Manus AI 替代方案，旨在完全在您自己的硬件上运行，无需依赖云服务。这款语音驱动的 AI 助手能够自主浏览网页，用多种语言（Python、C、Go、Java）编写代码，并通过智能代理选择来规划/执行复杂的任务。

主要功能包括：
*   **隐私性**：所有数据都保留在您的设备上。
*   **网页浏览**：自动信息提取和表单填写。
*   **自主编码**：代码生成、调试和执行。
*   **智能代理选择**：为给定任务自动分配最佳代理。
*   **任务规划**：复杂任务的分解和执行。
*   **语音控制**：语音和语音转文本界面。

该项目正在开发中，欢迎贡献者。安装过程包括克隆存储库，设置虚拟环境，安装依赖项，以及配置本地 LLM 提供商，例如 Ollama 或 LM Studio（建议使用 Deepseek 14B 或更大的模型）。它也可以配置为使用外部 API，如 OpenAI，但这并非主要重点。设置包括使用 Docker Compose 启动所需的服务。使用演示通过 CLI 或 Web 界面，包含用于编码、网络搜索和文件系统任务的示例查询。该项目还允许在远程服务器上运行 LLM。配置文件允许启用语音控制，设置代理的名称，以及自定义代理的行为。

---

## 59. D语言程序设计：教程与参考

**原文标题**: Programming in D: Tutorial and Reference

**原文链接**: [https://ddili.org/ders/d.en/](https://ddili.org/ders/d.en/)

《D语言编程：教程与参考》是一份学习D编程语言的全面资源。该文档提供了本书各种格式的链接，包括在线版、纸质版、Kindle版、交互式课程以及可下载文件（PDF、EPUB、AZW3、MOBI和代码示例）。它包含一个关键词索引，方便导航。

该资源的核心是一个结构化的教程，涵盖了D语言的基本概念和高级特性。主题范围从基本语法（Hello World、变量、数据类型）到控制流（if/else、循环）以及数据结构（数组、字符串、关联数组）。然后深入研究函数、不可变性、值/引用类型以及错误处理（异常、断言）。面向对象编程概念（结构体、类、继承、接口）也被详细介绍。

更高级的主题包括模板、别名、指针、位运算、条件编译、函数指针、范围、并行、并发、内存管理和用户自定义属性。该教程为每个概念都提供了讲解和示例，适合初学者和希望学习D语言的经验丰富的程序员。最后，还概述了运算符优先级。

---

## 60. 我写过一本书，名叫《垃圾小镇》。当时觉得挺有趣的。

**原文标题**: I wrote a book called “Crap Towns”. It seemed funny at the time

**原文链接**: [https://samj.substack.com/p/that-joke-isnt-funny-any-more](https://samj.substack.com/p/that-joke-isnt-funny-any-more)

作者山姆·乔迪森反思了他过去的作品《垃圾城镇》，这是一部讽刺书籍系列，旨在嘲讽英国据称不受欢迎的城镇。他现在表达了后悔之情，并承认这些书造成的伤害，特别是对目标社区造成的伤害。

乔迪森最初认为这只是一个无伤大雅的玩笑，旨在嘲弄阶级和地域刻板印象，但他现在意识到这些书助长了一种对工人阶级地区抱有消极和不尊重的文化。他承认这种幽默依赖于廉价的攻击，并强化了有害的刻板印象，特别是关于北部城镇的刻板印象。

他详细描述了负面后果，包括强化了地方自豪感被视为令人尴尬的观念，延续了分裂的言论，以及对居民自尊的潜在影响。他回忆说，开发商和政客曾将这本书武器化，以证明对目标城镇的忽视和投资不足是合理的。

乔迪森总结说，这个“玩笑”已经过时，不再有趣，尤其是在日益严重的社会和经济不平等背景下。他对他的作品造成的意外后果感到负责，并对促成贬低和污名化本已陷入困境的社区的叙事表示悔恨。他认为重要的是承认造成的伤害，并在未来努力更加谨慎和负责。他本质上表达了一种视角的转变，意识到这些书不仅仅是无害的讽刺，而且积极地助长了一种有害的社会叙事。

---

## 61. 路径是一个用于处理路径的实用工具。

**原文标题**: Path is a utility for working with paths

**原文链接**: [https://gitlab.com/SpyrjaGaldr/path](https://gitlab.com/SpyrjaGaldr/path)

关于“Path is a utility for working with paths”的文章介绍了一个用于处理路径的工具，目前内容正在加载中，详细信息尚不可知。预计文章将介绍该工具的功能和优势，以便用户管理和操作系统或软件应用中的路径。

---

## 62. 写入“/etc/hosts”会破坏Substack编辑器

**原文标题**: Writing "/etc/hosts" breaks the Substack editor

**原文链接**: [https://scalewithlee.substack.com/p/when-etchsts-breaks-your-substack](https://scalewithlee.substack.com/p/when-etchsts-breaks-your-substack)

“修改‘/etc/hosts’文件导致Substack编辑器崩溃”一文详述了作者在使用Substack编辑器时遇到的一个奇怪问题。作者发现，向`/etc/hosts`文件（一个用于将主机名映射到IP地址的系统文件）添加条目，竟意外地导致Substack编辑器崩溃，无法发布内容。

具体来说，作者在其`/etc/hosts`文件中添加了一行，将一个本地域名（可能与开发或测试相关）映射到`127.0.0.1`（localhost）。 虽然看似无关，但这一修改导致Substack编辑器变得无响应且无法使用。

文章推测，Substack编辑器或其依赖的库执行某种反向DNS查找或依赖一致的名称解析。 对`/etc/hosts`文件的更改，即使是对于完全无关的域名，也会以某种方式干扰此过程，导致编辑器失败。

作者通过简单地从`/etc/hosts`文件中删除有问题的条目来解决了这个问题。 他们总结说，软件依赖关系有时会出乎意料且脆弱，看似无害的系统修改可能会产生意想不到的后果。 最重要的是提醒人们注意修改`/etc/hosts`文件，尤其是在使用像Substack这样的基于Web的应用程序时遇到意外问题的情况下。

---

## 63. Mobygratis – 免费Moby音乐，助力你的创意项目

**原文标题**: Mobygratis – Free Moby music to empower your creative projects

**原文链接**: [https://mobygratis.com/](https://mobygratis.com/)

Mobygratis是由Moby创建的平台，旨在为包括电影制作人、音乐家、学生、网红等各类创作者提供免费的器乐音乐。该网站提供包含500首曲目的目录，有三种格式可供选择：立体声MP3、立体声WAV和多轨WAV，全部免费。Moby鼓励用户探索这些音乐并将其用于他们的创意项目。他建议有疑问的用户查阅常见问题解答部分，并强调该平台的简单性：免费音乐，玩得开心。该目录最后更新于2025年4月27日。

---

## 64. Show HN: GS-Calc – 一款集成了Python的现代电子表格

**原文标题**: Show HN: GS-Calc – A modern spreadsheet with Python integration

**原文链接**: [https://citadel5.com/gs-calc.htm](https://citadel5.com/gs-calc.htm)

GS-Calc是一款现代化的电子表格软件，专为处理超大数据集而设计，在速度和效率方面优于传统电子表格。它支持高达3200万行和16384列，文件大小没有限制。大型文本/CSV文件会自动拆分为多个工作表。主要功能包括针对大型文件的优化性能、更快的加载和处理速度、其二进制格式的更小文件大小以及具有高达3200万行的先进数据透视表功能。

GS-Calc还提供蒙特卡洛模拟、批量参数修改、快速VLOOKUP和FILTER函数、正则表达式支持以及可以处理数百万个数据点的图表。值得注意的是，它通过UDF函数实现了Python集成，允许用户创建返回各种数据类型的自定义函数，包括图像。它允许将单个工作表拆分为多达100个窗格。

该软件支持各种文件格式（CSV、文本、xls、xlsx、dBase、MySQL、SQLite），并可直接进行编辑。它包括数据完整性验证、文件比较以及使用JScript和VBscript进行脚本编写等功能。GS-Calc提供专门的数值函数，并且可以在无需修改注册表的情况下离线使用。提供可供下载的试用版，其中包含快速二进制VLOOKUP、视频示例中演示的大型文件处理功能以及12个月的免费升级等功能。

---

## 65. CONL：配置文件的“Markdown”

**原文标题**: CONL: "Markdown" for your config files

**原文链接**: [https://cirw.in/blog/conl](https://cirw.in/blog/conl)

本文介绍 CONL，一种新的配置文件格式，旨在成为配置文件的“Markdown”。 鉴于现有格式（如带有注释的 JSON、TOML 和 YAML）的复杂性和缺陷，作者旨在创建一种易于阅读、编辑和实现，同时又能表示类似 JSON 数据模型的格式。

CONL 强调简洁明了的语法，灵感来自 INI，但能够处理像 JSON 和 YAML 这样的嵌套结构。它支持标量、列表和映射作为值。一个关键的设计选择是每个键都在自己的行上定义，使用换行符作为分隔符，避免了带有注释的 JSON 的逗号管理问题。列表以行首的 `=` 标识，映射则以键后跟 `=` 标识。允许使用没有值的键来支持注释掉映射内容。

该格式使用 `;` 作为注释，选择它的原因是它在配置值中不常见。它支持 Markdown 风格的多行字符串和带反斜杠转义的双引号字面量，包括可变长度的 Unicode 代码点转义。作者提供了 Rust 和 Go 的实现、一个语言服务器和一个 Zed 扩展，并鼓励其他人采用和移植 CONL，因为它功能集小，并且提供了正式规范和测试套件。主要的限制是不支持往返（JSON -> CONL -> JSON 会丢失类型信息）。

---

## 66. 伯克利人形Lite – 开源机器人

**原文标题**: Berkeley Humanoid Lite – Open-source robot

**原文链接**: [https://lite.berkeley-humanoid.org/](https://lite.berkeley-humanoid.org/)

伯克利人形机器人Lite项目旨在解决市面上商用人形机器人硬件普遍存在的高成本、闭源以及缺乏可访问性等问题，推出一款开源人形机器人。为了实现人形机器人开发的普及化，伯克利人形机器人Lite在其执行器和机器人机身中采用了模块化的3D打印齿轮箱设计。所有组件均可从标准电商平台轻松采购，并使用桌面3D打印机制造，从而将硬件总成本控制在5000美元以下。

为了弥补3D打印齿轮箱的固有局限性，采用了摆线齿轮设计，以确保最佳的性能和耐用性。严格的测试验证了3D打印执行器的坚固性。该项目通过实验展示了机器人的能力，包括基于强化学习的运动控制，该控制成功实现了从仿真到硬件的零样本策略迁移。

通过提供完全开源的硬件设计、嵌入式代码以及训练/部署框架，伯克利人形机器人Lite旨在赋能机器人社区，促进人形机器人技术的更广泛开发和创新。该项目将自身定位为使人形机器人研究和开发对于更广泛的研究人员和开发者来说更易于访问和定制的关键一步。

---

## 67. 当孩子的人生变成家族生意

**原文标题**: When a Child's Life Becomes the Family Business

**原文链接**: [https://www.nytimes.com/2025/04/27/well/evantube-influencer-family.html](https://www.nytimes.com/2025/04/27/well/evantube-influencer-family.html)

本文记录了早期儿童网红之一 EvanTube 的崛起历程。2011 年，5 岁的 Evan Lee 无意中开启了其家庭的 YouTube 事业，当时他的父亲 Jared 拍摄了他展示用粘土制作的《愤怒的小鸟》玩具模型的视频。这个简单的“展示与讲述”视频迅速走红，获得了 1100 万的点击量。

意识到其中的潜力，Jared 利用了 Evan 的魅力和热情。圣诞节期间，他们制作了另一个以《愤怒的小鸟》周边商品为特色的视频，展示了 Evan 更加出色的镜头表现力。这标志着 EvanTube 的开端，该频道最终积累了 700 万订阅者。

本文强调了 Evan 在这段时期的年龄之小，并指出他可能不记得创建 YouTube 频道的所有细节。如今 19 岁并已是一名大学生的 Evan 回顾了他不寻常的童年，他成为了家庭生意的“关键人物”，而这一切都源于一个简单的视频和他天生的魅力。

---

## 68. 通过动态长度浮点数实现高效 GPU 推理的无损 LLM 压缩

**原文标题**: Lossless LLM compression for efficient GPU inference via dynamic-length float

**原文链接**: [https://arxiv.org/abs/2504.11651](https://arxiv.org/abs/2504.11651)

本文介绍了一种名为动态长度浮点数 (DFloat11) 的新型大语言模型 (LLM) 无损压缩框架，旨在减小模型尺寸，同时在推理过程中保持逐位精度。DFloat11 利用 LLM 的 BFloat16 权重表示中观察到的低熵特性，根据权重的频率为其分配动态长度编码，从而实现接近信息最优的压缩。

其核心创新在于一个定制的 GPU 内核，该内核经过优化，可以快速、在线地解压缩动态长度编码。该内核采用了多种技术，例如将内存密集型查找表分解为更小的、GPU SRAM 友好的版本、用于协调线程读/写操作的两阶段方法，以及transformer块级别的解压缩，以最大限度地减少延迟。

在 Llama-3.1、Qwen-2.5 和 Gemma-3 等最新模型上的实验表明，DFloat11 实现了约 30% 的模型尺寸缩减，且没有任何精度损失。此外，它优于作为替代内存管理策略的 CPU 卸载，在 token 生成方面实现了 1.9-38.8 倍的吞吐量提升。DFloat11 还允许在固定的 GPU 内存预算内实现 5.3-13.17 倍更长的上下文长度，从而能够在单个具有 8x80GB GPU 的节点上推理 Llama-3.1-405B 等模型。代码和模型已公开可用。

---

## 69. 你的手机没有在偷偷监听你，但真相更令人不安。

**原文标题**: Your phone isn't secretly listening to you, but the truth is more disturbing

**原文链接**: [https://newatlas.com/computers/smartphone-listening-conversations-ads-facebook/](https://newatlas.com/computers/smartphone-listening-conversations-ads-facebook/)

本文探讨了智能手机秘密监听用户以定向投放广告这一长期存在的阴谋论，对其进行了驳斥，同时揭示了有关数据收集的更令人不安的真相。文章重点介绍了一则 2024 年关于 Cox Media Group 的“主动监听”系统的新闻，据称该系统利用语音助手激活时捕获的语音数据来定制广告。科技公司迅速与此撇清关系。

文章引用了 Wandera 在 2019 年进行的一项实验，该实验通过证明手机暴露在音频循环中与处于静音环境相比，数据消耗、电池使用和后台活动方面的差异微乎其微，从而驳斥了麦克风监听理论。这表明持续的音频录制和上传并没有发生。持续音频监控所需的海量数据使用使其不切实际且难以隐藏。

文章认为，定向广告并非源于音频监听，而是源于音频之外的大量数据收集。像 Facebook 这样的公司会跟踪用户的位置、联系人、兴趣和跨设备在线活动。他们甚至可以访问零售商的知识并跟踪店内购买情况。算法分析这些数据以预测用户需求并投放定制广告。这种数据收集非常广泛，以至于算法通常可以惊人地准确预测对话和需求。虽然并非完美，但令人毛骨悚然的精准广告的频率才是真正令人担忧的问题。虽然语音控制设备确实会在发出关键命令后进行短时间录音，但持续录音并未发生。

---

## 70. Show HN: Bhvr，一个 Bun、Hono、Vite 和 React 启动器

**原文标题**: Show HN: Bhvr, a Bun and Hono and Vite and React Starter

**原文链接**: [https://bhvr.dev](https://bhvr.dev)

Show HN: Bhvr，一个 Bun、Hono、Vite 和 React 的启动器

"Show HN: Bhvr，一个 Bun、Hono、Vite 和 React 的启动器" 提交介绍了 "bhvr"，一个用于 Web 开发的启动工具包。 Bhvr 利用了以下几种现代技术：

*   **Bun:** 一个快速的 JavaScript 运行时、包管理器和打包器。
*   **Hono:** 一个用于边缘运行时的轻量级 Web 框架。
*   **Vite:** 一个快速的前端构建工具。
*   **React:** 一个用于构建用户界面的流行 JavaScript 库。

本质上，"bhvr" 是一个预配置的模板，旨在简化使用这些技术的项目的设置过程。 它旨在提供一个即开即用的开发环境，从而可能节省开发人员单独配置每个工具的时间和精力。"bhvr" 这个名字可能代表这些技术的组合，或者可能是 "behavior" 的语音拼写。 内容的简洁性表明它主要是在呼吁人们关注一个新工具，而不是详细的解释。

---

## 71. 政策傀儡攻击：大型语言模型的新型绕过方法

**原文标题**: The Policy Puppetry Attack: Novel bypass for major LLMs

**原文链接**: [https://hiddenlayer.com/innovation-hub/novel-universal-bypass-for-all-major-llms/](https://hiddenlayer.com/innovation-hub/novel-universal-bypass-for-all-major-llms/)

HiddenLayer是一家Gartner认可的AI安全供应商，提供安全平台，旨在保护机器学习模型免受推理、绕过、提取攻击和模型盗窃。 他们的解决方案独特之处在于，它无需访问原始数据或算法即可提供开箱即用的安全性，从而最大限度地减少了复杂性。 该公司强调保护企业人工智能投资，确保其最重要的产品安全。

HiddenLayer由安全和机器学习领域的专家创立，并获得了包括M12（微软的风险投资基金）、Moore Strategic Ventures、Booz Allen Ventures、IBM Ventures和Capital One Ventures在内的重要投资集团的支持。该公司提供多种资源，包括平台、解决方案、服务和学习材料。文本还包括标准的公司页脚信息，如联系方式、版权声明、安全和隐私政策链接、漏洞披露政策、站点地图，以及其在Twitter和LinkedIn上的社交媒体链接。标题提到了新型“策略傀儡攻击”，并且大型语言模型受到影响。

---

## 72. 使用ASKAP发现15个新的巨型射电星系

**原文标题**: Fifteen new giant radio galaxies discovered with ASKAP

**原文链接**: [https://phys.org/news/2025-04-fifteen-giant-radio-galaxies-askap.html](https://phys.org/news/2025-04-fifteen-giant-radio-galaxies-askap.html)

天文学家利用澳大利亚平方公里阵探路者（ASKAP）发现了15个新的巨型射电星系（GRG）。这些GRG在arXiv上发表的一篇论文中详细描述，其预计线性长度超过300万光年。GRG是在低密度环境中形成的罕见天体，通过喷流和瓣状结构发射同步加速辐射。它们对于理解射电源的形成和演化至关重要。

ASKAP凭借其先进的技术、宽阔的视场、高分辨率和灵敏度，非常适合探测GRG。新发现的GRG的大小范围从370万到1236万光年不等，红移位于0.056到0.735之间。其中两个被认为是候选GRG，尚待进一步确认。

这些星系呈现出多种形态：八个被归类为Fanaroff-Riley II型（FR II）星系，其特征是显著的射电热点，而四个是Fanaroff-Riley I型（FR I）星系，具有明亮的内部喷流和逐渐消失的外部瓣状结构。剩下的三个似乎是中间类型或混合类型。发现的最大的GRG，ASKAP J0107–2347，是一个FR II型的双重射电星系（DDRG），具有新形成的内部瓣状结构和细长的、低表面亮度的外部瓣状结构。

---

## 73. 作为独立技术作者，我的6千美元预付款

**原文标题**: My $6k Advance as a Self-Published Technical Author

**原文链接**: [https://mtlynch.io/my-6k-advance/](https://mtlynch.io/my-6k-advance/)

本文详细介绍了作者通过Kickstarter成功预售其自出版的技术书籍《Refactoring English》（旨在帮助软件开发者提高写作水平）并获得6000美元的过程。作者讨论了众筹相对于传统出版预付款的优势，强调了更高的经济回报、对内容的控制以及未来进行传统出版的可能性等优点。

作者承认了自身的不公平优势，包括高流量博客、在Hacker News等平台上的成功以及庞大的邮件列表。他们将众筹结果与传统的出版协议进行了比较，引用了No Starch Press和Manning的例子来证明自出版的潜在经济利益。

成功的关键在于Kickstarter的“要么全拿，要么全无”的结构，这保证了在开始写作之前达到最低程度的兴趣。预售还促进了与热情的读者的早期互动，提供了宝贵的反馈。

文章分析了客户获取策略，认为在其网站上发布摘录是最有效的策略，其次是在其图书网站和个人博客上进行推广。相反，寻求赞助和以Hacker News为重点的Web应用程序未能产生显著的销售额。

作者称赞了使用Kickstarter的便捷性和公平性，并强调了低估回报的重要性。他们特意避免了花哨的Kickstarter推广，专注于内容和互动，而不是浮华的营销。

---

## 74. 避免人工智能时代技能退化

**原文标题**: Avoiding skill atrophy in the age of AI

**原文链接**: [https://addyo.substack.com/p/avoiding-skill-atrophy-in-the-age](https://addyo.substack.com/p/avoiding-skill-atrophy-in-the-age)

无法访问文章链接。

---

## 75. 华盛顿特区美国检察官质疑维基百科非营利地位。

**原文标题**: Wikipedia’s nonprofit status questioned by D.C. U.S. attorney

**原文链接**: [https://www.washingtonpost.com/technology/2025/04/25/wikipedia-nonprofit-ed-martin-letter/](https://www.washingtonpost.com/technology/2025/04/25/wikipedia-nonprofit-ed-martin-letter/)

无法访问文章链接。

---

## 76. Goenums：Go 语言的类型安全枚举生成器

**原文标题**: Goenums: Type Safe Enum Generator for Go

**原文链接**: [https://github.com/zarldev/goenums](https://github.com/zarldev/goenums)

Goenums 是一个 Go 工具，它通过从简单的常量声明生成类型安全、功能丰富的枚举实现来解决原生枚举的缺失。它将基于 `iota` 的常量转换为具有字符串转换、JSON 处理、数据库集成、验证和迭代支持的枚举。

主要特性包括通过包装类型实现类型安全、自动字符串转换和解析、内置 JSON 编组/解组、用于数据库集成的 SQL 扫描器和值器实现、用于验证枚举值的方法、现代 Go 1.21+ 迭代支持（具有传统回退）以及通过注释添加自定义字段的可扩展性。它以零依赖运行。

用法包括使用带有各种标志的 `goenums` 命令（例如，`-i` 用于不区分大小写的解析，`-l` 用于传统 Go 支持，`-v` 用于详细输出，`-f` 用于快速失败模式）。可以使用注释定义枚举的自定义字符串表示形式。可以通过添加类型注释中的自定义字段来创建扩展的枚举类型。生成的枚举通过实现的接口支持 JSON 和数据库存储。

该工具还提供了一个 `Exhaustive` 函数，以确保在 switch 语句中处理所有枚举值。Goenums 与 `go:generate` 指令集成以进行自动重新生成，从而增强现有的构建过程。提供了 Go 1.21+ 的示例用法和要求。

---

## 77. 意外图灵完备

**原文标题**: Accidentally Turing-Complete

**原文链接**: [https://beza1e1.tuxen.de/articles/accidentally_turing_complete.html](https://beza1e1.tuxen.de/articles/accidentally_turing_complete.html)

意外图灵完备性

该文收集了一些例子，这些系统、语言甚至游戏最初并非设计用于通用计算，但后来被证明是图灵完备的。这意味着它们在理论上具备执行图灵机可以进行的任何计算的能力，实际上使它们成为可编程的。

文章重点介绍了各种令人惊讶的例子，包括：

*   **编程语言与系统：** C++模板, TypeScript类型系统, Java泛型, X86 Mov指令, X86 MMU, C预处理器, SQL, Scala类型系统, Apache Rewrite规则, Sendmail, Vim普通模式。
*   **标记/数据语言：** HTML5 + CSS3, MediaWiki模板, JBIG2图像压缩。
*   **游戏：** 万智牌, Minecraft, 矮人要塞, Doom, 小小大星球, 口袋妖怪黄, 超级马里奥世界。
*   **办公软件：** Excel, PowerPoint。
*   **网络：** 边界网关协议 (BGP), 愚蠢的RDMA NIC。
*   **硬件：** CPU缓存。
*   **其他：** 字体整形。

这些例子展示了实现图灵完备性的不同机制，例如递归、指令集的巧妙使用、复杂的游戏规则，甚至利用漏洞。 一些例子，如C预处理器和Scala类型，面临实际限制，如堆栈溢出。文章还提到了相关主题，如单字母编程语言和黑客称号，突出了那些发现这些意外计算能力的聪明才智和奉献精神。

---

## 78. 如果我们能从头重建 Kafka 会怎样？

**原文标题**: What If We Could Rebuild Kafka from Scratch?

**原文链接**: [https://www.morling.dev/blog/what-if-we-could-rebuild-kafka-from-scratch/](https://www.morling.dev/blog/what-if-we-could-rebuild-kafka-from-scratch/)

冈纳·莫林的文章探讨了“Kafka.next”的潜力，这是一个从头开始构建，专为云原生环境量身定制的、经过重新构想的事件日志系统。受到旨在提高Kafka云弹性并降低成本的KIP-1150和AutoMQ等项目的启发，文章为这个假设的系统提出了几个理想的特性。

主要特点包括：

*   **消除分区：** 摆脱分区，它在使用节点本地磁盘时对于扩展至关重要，而是专注于云中的对象存储。
*   **以键为中心的访问：** 优先考虑基于键的消息的高效访问和重播，从而实现数百万个实体级别的流，以实现更精细的消费并解决队头阻塞问题。
*   **主题层次结构：** 实施结构化主题标识符，以便客户端高效订阅流的子集，类似于Solace。
*   **并发控制：** 引入消息键的乐观锁定，以防止过时的写入并确保数据一致性。
*   **服务端 Schema 支持：** 将 Schema 支持作为核心功能，以实现更好的数据治理、AsyncAPI 兼容性以及列式存储的潜力。
*   **可扩展性和可插拔性：** 通过明确定义的扩展点启用自定义服务端消息过滤器、转换和存储格式。
*   **同步提交回调：** 保证在确认生产请求时下游数据视图已更新，从而允许 Kafka 充当真实数据库的日志。
*   **快照：** 通过将事件序列压缩成快照来支持“逻辑压缩”，以便高效地基于键的消息重播。
*   **多租户：** 从一开始就构建具有多租户意识的系统，以实现隔离和资源管理。

作者承认，其中一些功能存在于其他系统中，但强调了将它们组合成一个单一的、开源解决方案的潜力。最后，他们提到 LSM 树作为潜在的架构基础。

---

## 79. NNCPNET电子邮件网络

**原文标题**: The NNCPNET Email Network

**原文链接**: [https://changelog.complete.org/archives/10768-announcing-the-nncpnet-email-network](https://changelog.complete.org/archives/10768-announcing-the-nncpnet-email-network)

本文介绍NNCPNET，一个基于NNCP构建的新型邮件系统，NNCP是UUCP的一种现代且安全的替代方案。由于对现代邮件服务器（SPF、DKIM、DMARC、TLS）日益增长的复杂性和限制感到沮丧，作者创建了NNCPNET，以允许再次进行邮件实验和乐趣。

NNCPNET利用NNCP的异步、洋葱路由、存储转发网络，该网络可以使用各种传输方式，包括互联网和USB驱动器。由于NNCP的加密和签名，该系统默认提供发送者验证。

该项目提供一个Docker容器，捆绑了Exim、NNCP和自定义路由工具。它包括自动节点列表更新，确保与新成员的兼容性，并提供与互联网邮件桥的可选集成。该系统对所有人开放，并包括邮件列表、广泛的文档和开源代码。

虽然到互联网SMTP邮件的网关默认情况下是被禁用的，但可以在任何节点上启用它，并完全支持现代安全协议。一个关键优势是它不需要入站端口或持续的互联网连接，允许用户在笔记本电脑上运行它，甚至可以使用NNCP的功能和内置的IMAP服务器离线运行。本质上，NNCPNET提供了对更简单、更可定制的邮件时代的回归，同时融入了现代安全原则。

---

## 80. 巨洞冒险 (1976)

**原文标题**: Colossal Cave Adventure (1976)

**原文链接**: [https://github.com/wh0am1-dev/adventure](https://github.com/wh0am1-dev/adventure)

此仓库包含Colossal Cave Adventure (1976)的原始Fortran源代码，该游戏被认为是电子游戏史上第一个文字冒险游戏。作者受到电视剧《奔腾年代》的启发，找到了源代码并从互联网上整理了地图和攻略等补充材料。该仓库还包括适用于Windows和Mac OS的游戏可执行版本。作者强调，该仓库的目的仅用于教育。

---

## 81. 回声 – 开放硬件音乐播放器

**原文标题**: Echo – Open Hardware Music Player

**原文链接**: [https://github.com/amachronic/echoplayer](https://github.com/amachronic/echoplayer)

Echo：一款基于Rockbox固件的高品质开源硬件音乐播放器项目。当前版本Echo R1采用经典设计，配备方向键、多功能按钮、专用音量/电源控制键和一个锁定开关。它具有耳机和线路输出插孔、支持高达2 TiB存储的MicroSD卡槽以及用于充电和数据传输的USB-C端口。它由可更换的BL-5C电池供电。

主要硬件规格包括STM32H743 CPU、32 MiB SDRAM、TLV320AIC3104音频编解码器和一个320x240 2.3英寸LCD。该设计使用KiCAD 8.0创建，并计划在FreeCAD中制作3D打印外壳。所有设计均采用CERN-OHL-S v2许可。

Rev1原型PCB已完成，但已发现问题，包括无法禁用背光、LED驱动器上的电流限制过低以及原理图参考指示符不一致。开发重点是移植Rockbox以识别更多硬件问题，并设计一个外壳以进行可用性和人体工程学测试。下一个版本将解决已识别的问题。所有文件均采用CERN-OHL-S版本2许可。

---

## 82. Eurorack旋钮创意

**原文标题**: Eurorack Knob Idea

**原文链接**: [https://mitxela.com/projects/euroknob](https://mitxela.com/projects/euroknob)

本文详细介绍了mitxela.com提出的“Eurorack旋钮创意”，这是一种用于Eurorack合成器的混合旋钮和跳线概念，旨在最大限度地减少面板杂乱。核心思想是使用标准的3.5mm TRS插孔，结合磁性编码器。一个嵌入在改装后的TRS插头中的小磁铁充当旋钮，当插入插孔时，它会旋转位于其后面的磁性编码器（AS5600）。

AS5600包含霍尔传感器和DSP，根据磁铁的位置输出角度和幅度，从而实现对“旋钮”存在状态的精确控制和检测。作者使用定制的PCB、一个垂直安装的TRS插座（抬高以容纳AS5600）和一个CH32V003微控制器来读取和显示编码器的值，构建了一个原型。

虽然原型证明是成功的，但作者承认该概念在广泛采用方面存在潜在的局限性。在整个Eurorack设置中实施该系统将是昂贵的，需要对现有模块进行重大重新设计才能使用编码器的输出，并且可能限制与传统电位器的兼容性。

尽管存在这些挑战，作者还是提出了一个更具商业可行性的替代方案：带有同轴TRS插孔的电位器。这种更简单、纯粹的机械解决方案不需要更改现有的原理图，并且可以提供类似的混合功能。文章最后呼吁提供资金和合作，以便将磁性或机械Euroknob创意推向市场。

---

## 83. Show HN: 空行展开器 – 使用此工具在终端中减少输入

**原文标题**: Show HN: Empty Enter Expander – Type less in the terminal with this tool

**原文链接**: [https://github.com/waszabi/empty-enter-expander](https://github.com/waszabi/empty-enter-expander)

“空回车扩展器”是一款zsh工具，旨在通过允许用户用少量按键执行命令来最大限度地减少终端中的输入。它通过在空回车时激活，显示可用命令列表，然后使用短的小写字母快捷方式将这些命令插入到提示符中来实现此目的。

该工具使用“模块目录”来存储命令，模块目录中的文件和文件夹以小写字母开头命名，以充当快捷方式。例如，`git log` 命令可以存储在 `~/Tools/expander-example-module/g Git/l Log` 中。当在空行上按下 Enter 键后按下相应的键时，该工具将执行这些文件的内容（脚本）。

配置包括在 `~/.zprofile` 中设置 `EMPTY_ENTER_EXPANDER_MODULE_PATH` 环境变量以指向模块目录，导入提供的 `zsh-function.zsh` 文件，将 `empty-enter-expander` 函数绑定到 Enter 键，以及设置 `HIST_IGNORE_SPACE` 以防止空命令被保存在历史记录中。

要使用它，请在空命令上按 Enter 键，然后键入与所需命令对应的快捷键（例如，`g`，`l`），然后再次按 Enter 键将其插入提示符中以供执行。目前，只有 zsh 版本可用，计划推出 bash 版本。

---

## 84. 七年之痒

**原文标题**: The Seven-Year Rule

**原文链接**: [https://www.macsparky.com/blog/2025/04/the-seven-year-rule/](https://www.macsparky.com/blog/2025/04/the-seven-year-rule/)

文章“七年法则”探讨了一个概念，即由于人体自然的细胞再生周期，人类每七年都会经历重大转变。基于作者在达赖喇嘛的一本书中遇到的一个原则，其核心思想是，我们不断成为自己的新版本，大约每七年就会脱落所有的细胞。

作者认为，拥抱这种转变可以带来解放。通过理解，经历过过去的错误、创伤或错失机会的人，在身体上已经不再存在，我们可以将自己从沉湎于过去中解放出来。作者用一位朋友为例，这位朋友一直执着于三十年前发生的一件事，强调那已经是“四个版本”之前的事情了。

同样，作者建议，专注于当下至关重要，因为未来的自己，也就是七年后的那个你，尚未形成。这种观点鼓励当下的行动和正念。

最终，这篇文章倡导认识并尊重我们持续的进化——细胞、心理和精神上的进化。通过采用“七年法则”，我们可以将自己从过去的束缚中解放出来，更充分地活在当下，同时也有益于我们未来的自己。

---

## 85. 伟易达苏格拉底教学法

**原文标题**: The VTech Socratic Method

**原文链接**: [https://www.leadedsolder.com/2025/04/22/vtech-socrates-pickup.html](https://www.leadedsolder.com/2025/04/22/vtech-socrates-pickup.html)

本文详细介绍了作者对VTech Socrates（一款1988年的混合型视频游戏机/电脑）的探索和改造过程。作者在eBay上廉价购得一台二手Socrates，发现它非常脏但出人意料地耐用。清洁后，作者拆卸了机器，发现其主板以东芝元件为主，包括Z80 CPU、定制门阵列和掩膜ROM。

随后，作者着手进行AV改造，灵感来源于Johnny Blanchard的简化设计。这涉及设计一块带有视频放大器和电压调节器的定制PCB，以提高视频输出质量。这个过程充满了挑战，包括焊接困难和应力释放问题。

改造后的Socrates随后被通电，并通过复合视频连接进行了测试，产生了相当清晰的图像和洪亮的声音。作者接着探索了红外键盘/控制器，遇到了诸如不寻常的电池放置和功能不明的神秘开关等问题。

最后，作者检查了“环游世界”游戏卡带，发现了掩膜ROM并绘制了卡带的引脚图。作者承认，该引脚图目前尚未经过测试。作者计划利用识别出的引脚图来促进为Socrates开发定制软件。

---

## 86. 可重复性项目未能验证数十项生物医学研究

**原文标题**: Reproducibility project fails to validate dozens of biomedical studies

**原文链接**: [https://www.nature.com/articles/d41586-025-01266-x](https://www.nature.com/articles/d41586-025-01266-x)

巴西可重复性倡议是一项大型可重复性项目，涉及50多个研究团队和分布于巴西56个实验室的213名科学家，旨在复制巴西生物医学研究的成果。该倡议侧重于在巴西使用常用方法的论文，不考虑研究领域、感知重要性或引用次数。

该项目评估了1998年至2017年间发表的、使用三种方法的论文：细胞代谢测定、遗传物质扩增和啮齿动物迷宫测试。在测试的47个实验中，只有21%的实验基于包括统计显著性和结果方向在内的一系列标准是可重复的。该研究还发现，原始论文中报告的效应量平均比复制尝试中观察到的效应量大60%，这表明已发表的研究中存在对效应的过高估计。

该项目的协调员希望这些发现能够通过公共政策和大学倡议来促进巴西科学的改进。虽然复制率与其他类似研究一致，但该项目独特之处在于它专注于特定方法和一个特定国家的研究产出。

---

## 87. 北京控制南海一处小型沙洲

**原文标题**: Beijing seizes tiny sandbank in South China Sea

**原文链接**: [https://www.bbc.com/news/articles/creqp4lxnl4o](https://www.bbc.com/news/articles/creqp4lxnl4o)

中国海警夺取南海沙洲，加剧与菲律宾紧张关系。中国官方媒体发布了海警在沙洲上的照片，宣称中国对其拥有“海上控制权”和“主权管辖权”。菲律宾尚未正式回应，但此举被视为两国持续领土争端中的一次重大升级。

沙洲位于菲律宾在中业岛上的军事前哨附近。虽然没有迹象表明中国永久占领，但美国已表达深切关注，白宫发言人警告说，此类行动威胁地区稳定并违反国际法。美国正在与其伙伴进行磋商。

此事发生在美菲正在进行的名为“肩并肩”的联合军事演习期间，中国批评该演习具有挑衅性。这些演习涉及先进的导弹系统，旨在加强菲律宾的国防，尽管军方坚称它们并非针对任何特定国家。美国国防部长最近重申了华盛顿对与菲律宾联盟的承诺以及其遏制中国的决心。南海受到包括中国、菲律宾、越南、台湾、马来西亚和文莱在内的几个国家的重叠领土主张的影响。中国以“九段线”为标志的广泛主张导致该地区紧张局势加剧和岛屿建设活动。

---

## 88. 基于神经网络的世界模拟

**原文标题**: World Emulation via Neural Network

**原文链接**: [https://madebyoll.in/posts/world_emulation_via_dnn/](https://madebyoll.in/posts/world_emulation_via_dnn/)

本文详细介绍了作者创建“神经世界”的项目——一个完全由神经网络生成的可玩、可探索的环境，而非通过传统的游戏开发技术。作者使用在森林小径上行走时拍摄的视频片段，以及来自手机的运动数据，对网络进行了训练。

目标是展示神经网络从真实世界录像中生成世界的独特潜力，而不是模仿现有的电子游戏。最初的训练尝试产生了不令人满意的结果，被描述为“森林风味的汤”。然后，作者通过添加更多控制信息（3D运动）、记忆（多个过去的帧）以及在多个尺度上处理数据，迭代地改进了训练过程。后来的改进集中在模型大小、训练目标（强调细节生成）和训练持续时间上。

最终的神经世界使用了22,814帧的数据集，一个大约有500万个参数的UNet模型，并且训练了大约100个GPU小时。最终生成的世界可以在Web浏览器中本地运行。

作者认为，神经世界代表着一种转变，从像绘画一样创造世界（手动绘制细节）到像摄影一样创造世界（捕捉现有现实）。虽然仍处于早期阶段，但神经世界具有成为强大创意媒介的潜力，可以基于真实世界的录像自动生成逼真的细节。文章最后提到了“世界模型”领域的现有工作，并鼓励读者推荐西雅图附近有趣的拍摄地点。

---

## 89. 并行 ./configure

**原文标题**: Parallel ./configure

**原文链接**: [https://tavianator.com/2025/configure.html](https://tavianator.com/2025/configure.html)

2025年4月25日，Tavian Barnes 在这篇博文中表达了对许多软件项目中 `./configure` 脚本仍然采用顺序执行方式的沮丧。他强调了该脚本执行的大量独立检查，例如验证标准头文件和函数、编译器特性以及系统属性是否存在。作者认为，在处理器具有多核的时代，这种线性执行方式“荒谬”且浪费大量时间。这篇文章暗示了配置过程需要并行化，以大幅缩短软件构建阶段所花费的时间。Barnes 没有提出解决方案，而是指出了问题的持续存在。

---

## 90. 感谢你替我拿鸭子（2021）

**原文标题**: Thank you for holding my duck (2021)

**原文链接**: [https://naml.us/post/thank-you-for-holding-my-duck/](https://naml.us/post/thank-you-for-holding-my-duck/)

本文探讨了短语“谢谢你帮我拿着鸭子”的起源和演变，该短语用于描述一种问题解决技巧。作者最初认为这个故事起源于贝尔实验室或施乐帕克研究中心，内容是一位研究员向同事解释一个问题，同时他们拿着一只橡皮鸭。解释的过程往往让研究员自己找到解决方案。

作者的调查显示，这个故事的真正起源于皮克斯，通过比尔·波尔森追溯到利奥·霍维茨，他曾听说它与施乐帕克研究中心有关。最初的施乐帕克研究中心的故事涉及一只鸭子，用作协议的一部分，可能用于控制发言顺序。然而，这种做法演变了，尤其是在利奥在皮克斯的团队中，演变成一种方法，“拿着鸭子”意味着被动地倾听别人解决问题。说话者会通过说“嘿，[人名]，我需要你帮我拿着鸭子”来表示需要这种帮助。在找到解决方案后，他们会简单地说，“谢谢你帮我拿着鸭子”。

作者强调，皮克斯对这个短语的使用明确暗示了倾听者不提供意见。这在皮克斯的某个特定团队中经常使用，并且作者认为这种做法通过在皮克斯学习过的人传播到其他动画工作室，如梦工厂。作者希望最终能将这个故事追溯到施乐帕克研究中心，并欢迎任何线索。

---

## 91. ACM旗舰杂志征集从业者撰写或投稿的文章。

**原文标题**: ACM's flagship magazine seeks submissions by/for practitioners

**原文链接**: [https://cacm.acm.org/practice/call-for-papers-cacm-practice-section/](https://cacm.acm.org/practice/call-for-papers-cacm-practice-section/)

CACM（ACM旗舰杂志）现面向其新增的“实践”专栏征稿，旨在为从业者提供关于计算的长远见解，并提升工作绩效。该专栏力求与杂志已有的“研究”专栏并驾齐驱。他们正在寻找涵盖以下方面的文章：技术进步、开发实践、组织结构和成功的系统，这些内容应与广泛的从业者相关。

文章应具有实践性，并提供对理念、工具、技术和实践的深入了解，但不得具有职业性或教程性质（即对特定软件或编程语言的详细描述）。CACM不接受评论文章，因为其已设有专门的“观点”专栏。

投稿文章篇幅限制在10页（约6000字）以内，并且之前可以发布在博客或在线平台上。作者保留版权，文章以CC-BY许可发布。鼓励潜在作者在投稿前联系联合主席Nachi Nagappan和Terence Kelly，讨论他们的文章想法。所有文章都将经过编辑委员会和外部审稿人的审查，并由CACM工作人员进行专业编辑。目标是发表同事们会热情地互相推荐的文章。

---

## 92. Show HN: 使用Lean形式化《数学原理》

**原文标题**: Show HN: Formalizing Principia Mathematica using Lean

**原文链接**: [https://github.com/ndrwnaguib/principia](https://github.com/ndrwnaguib/principia)

这篇“Show HN”帖子描述了一个使用Lean 4定理证明器形式化伯特兰·罗素的《数学原理》的项目。目标是创建一个与罗素的原始证明紧密对应的形式化体系，保持严谨性，并尽可能减少偏差，除非为了形式化需要。

作者承认《数学原理》的皮亚诺-罗素符号的复杂性，并引用了关于它的现有资源。他们强调，对该符号的熟悉应该来自于观察形式化的公式与罗素原始符号的对比示例。

作者实现了一个名为`Syll`的自定义Lean策略，以模仿罗素对三段论推理的使用，并用命题*2.16*的形式化进行了演示。此策略可以自动链接蕴涵关系，使Lean代码更直接地反映罗素的证明结构。

作者提到找到了Landon Elkind之前在Coq中完成的一个形式化，但选择开展这个项目作为从基本原理构建数学的学习练习。虽然作者承认《原理》的局限性，但他发现这种经历很有收获，并考虑下一步形式化阿尔弗雷德·塔尔斯基的作品。该项目不追求实际应用，而是为了深入理解构建数理逻辑的过程。

---

## 93. Launch HN: Cua (YC X25) – 计算机使用代理的开源 Docker 容器

**原文标题**: Launch HN: Cua (YC X25) – Open-Source Docker Container for Computer-Use Agents

**原文链接**: [https://github.com/trycua/cua](https://github.com/trycua/cua)

Cua (计算机使用代理) 是一个开源框架，旨在使 AI 代理能够在虚拟化容器中控制完整的操作系统。它在 Apple Silicon 上提供接近原生性能（高达 97% 的速度），并支持各种视觉语言模型。

主要特性包括：

*   **高性能虚拟化：** 使用 Lume CLI 和 Apple 的 Virtualization.Framework，Cua 创建并运行 macOS/Linux 虚拟机。
*   **计算机使用界面与代理：** 提供一个框架，供 AI 代理与应用程序交互、浏览网页、编写代码，并在虚拟机内执行复杂的工作流程。

Cua 通过在专用虚拟环境中运行代理来提供安全性和隔离性，确保它们无法直接访问宿主机系统。它还通过 macOS 和 Linux 支持以及一致的环境来实现灵活性和可重复性。

安装提供三种选择：仅限 Lume CLI（用于虚拟机管理），通过 pip 安装实现完整的计算机使用代理功能，或者从源代码构建以获取最新功能。该项目包含多个库，如 Lume、Computer 和 Agent，每个库都具有特定的功能。

演示展示了 Cua 在诸如与 Claude Desktop 和 Tableau 交互、涉及浏览器和 VS Code 的多应用工作流程，以及在 Cursor 中修复 GitHub 问题等任务中的能力。

该项目对贡献开放，并根据 MIT 许可证获得许可。它使用 Microsoft 的 OmniParser，该解析器根据 CC-BY-4.0 获得许可。

---

## 94. 梯度下降法寻找最小作用量路径

**原文标题**: Finding Paths of Least Action with Gradient Descent

**原文链接**: [https://greydanus.github.io/2023/03/05/ncf-tutorial/](https://greydanus.github.io/2023/03/05/ncf-tutorial/)

本文探讨了一种解决物理问题的不太常见的方法：最小化作用量以寻找最小作用量路径，该路径代表系统的物理轨迹。 它将此方法与标准的分析和数值方法进行对比，并以引力场中的自由物体为例进行了说明。

文中重点介绍了利用作用量的拉格朗日方法，该方法是各种物理分支中使用的强大工具。 本文没有使用欧拉-拉格朗日方程来寻找平稳作用量路径，而是提出使用梯度下降法直接最小化作用量。 这涉及到将作用量积分离散化为求和，并使用有限差分近似导数，从而可以使用 PyTorch 等工具进行数值计算。

本文提供了一个简单的实现，演示了如何初始化一个坠落粒子的随机路径，然后使用梯度下降法来最小化作用量，从而得到一条与通过传统 ODE 积分获得的解相匹配的抛物线路径。 它还强调，虽然此方法用一个简单的例子说明，但它演示了一个塑造物理宇宙的基本原理。 文章最后建议，未来的文章将深入探讨更复杂的经典模拟和量子力学，并讨论该原理的含义。

---

## 95. 格伦转换正在吞噬互联网。

**原文标题**: The Gruen Transfer is consuming the internet

**原文链接**: [https://sebs.website/blog/the%20gruen-transfer-is-consuming-the-internet](https://sebs.website/blog/the%20gruen-transfer-is-consuming-the-internet)

塞巴斯蒂安的博文讨论了“格鲁恩转换”现象，这种现象指的是令人困惑的布局使顾客迷失方向，并导致冲动购买。最初在实体店观察到的格鲁恩转换现象，现在在网上也很普遍，尤其是在 Facebook 等平台上。

作者认为，最初旨在简化更新的 Facebook 信息流，已经变成了广告、表情包和网红内容的混乱混合体，分散了用户最初的目的，并导致“末日滚动”。 他将这种观察扩展到其他网站，这些网站的设计选择旨在迷惑访问者并鼓励冲动行为，并以维基百科的兔子洞作为一个良性例子。

格鲁恩转换也表现为 UX 黑暗模式，例如故意复杂的删除帐户或取消订阅流程。 作者质疑日益增长的复杂性和摩擦最终是否会变得有害，并将其与拉弗曲线进行类比。

他强调了欧盟立法要求订阅和取消服务同样容易，并建议将“复杂性”作为未来立法的有用衡量标准。 作者最后呼吁在日常生活中也应考虑类似的情况，例如在令人困惑的药房中导航。

---

## 96. 我给GPLv2许可声明中的地址写了信 (2022)

**原文标题**: I wrote to the address in the GPLv2 license notice (2022)

**原文链接**: [https://code.mendhak.com/gpl-v2-address-letter/](https://code.mendhak.com/gpl-v2-address-letter/)

2022年，作者出于对GPLv2许可协议中列出的实际地址的好奇，决定致信位于波士顿富兰克林街51号的自由软件基金会（FSF），以观其变。作者在Stack Exchange上的初步研究显示，该地址的存在是因为GPLv2发布于1991年，当时互联网的普及程度较低，物理介质是分发软件的主要方式。

作者详细描述了从英国寄信到美国的挑战，包括国际回信券的停用以及需要在eBay上购买美国邮票。这导致了一次短暂而令人困惑的邮票收集之旅。

几周后，作者收到了来自FSF的回信，其中包含GNU通用公共许可证的完整文本。然而，作者收到的是GPLv3，而不是GPLv2。纸张是用美式信纸尺寸打印的，进一步突出了地理差异。作者质疑许可证通知中包含实际地址是否应该表明他们正在寻求旧版本的GPLv2许可证，或者作者是否应该明确请求该版本。尽管存在错误以及付出的努力，作者对这次经历感到满意，并得出结论，他们不会寻求更正。作者还开玩笑说需要时间从这次邮政互动中恢复过来。

---

## 97. 重塑民主

**原文标题**: Reimagining Democracy

**原文链接**: [https://www.schneier.com/blog/archives/2025/04/reimagining-democracy-2.html](https://www.schneier.com/blog/archives/2025/04/reimagining-democracy-2.html)

布鲁斯·施奈尔的《重塑民主》探讨了面对快速发展的技术，特别是人工智能，重新思考政府机构的必要性。他描述了他组织的一系列研讨会，旨在讨论现代代议制民主的激进替代方案，并承认其在21世纪因沟通和旅行方面的过时假设而产生的局限性。

研讨会的主要主题包括打击虚假信息、质疑为经济利益而优化政治体系、以及考察信息时代资本主义与民主之间不断演变的关系。一个中心焦点是人工智能的潜在影响，考虑了从人工智能驱动的交通管理到人工智能立法者的各种场景，并质疑人类在治理中的未来角色。

研讨会还考虑了其他民主模式，如抽签制（随机选择官员）和流动民主制（可转让的投票代理权）。讨论延伸到包容性问题，例如赋予未来世代和非人类实体发言权，并探讨了建立能够抵御操纵并专注于协调个人和集体利益的政府体系的需求。

施奈尔强调，这些讨论虽然具有推测性，但对于促进超越当前系统渐进改进的激进思考非常有价值。他认为，鉴于气候变化等生存威胁，风险很高，并鼓励探索不连续的变化，以避免陷入局部最优。该研讨会将于2025年12月再次召开。

---

## 98. 亚马逊日本因允许上架假冒商品被责令支付3500万日元。

**原文标题**: Amazon Japan ordered to pay 35M. yen for allowing listing of fakes

**原文链接**: [https://mainichi.jp/english/articles/20250425/p2g/00m/0bu/047000c](https://mainichi.jp/english/articles/20250425/p2g/00m/0bu/047000c)

日本法院判决亚马逊日本公司赔偿3500万日元（约24.4万美元），原因是该公司允许在其平台上销售假冒产品。医疗设备制造商Try and E Co.及其经销商Excel Plan Co.提起的诉讼称，由于亚马逊上存在假冒商品，他们的脉搏血氧仪销量下降。

东京地方法院的重点是亚马逊日本公司有义务监控商品列表并删除假冒商品。法官新谷祐子裁定，亚马逊明知存在假冒商品，但未能采取有效措施加以制止。

此案源于2021年发生的一起事件，Excel Plan在亚马逊上销售正品脉搏血氧仪，而另一家卖家在同一页面上以低得多的价格列出了假冒版本。由于亚马逊的系统优先考虑最低价格，假冒产品获得了更高的曝光率，阻碍了Excel Plan的销售。尽管Excel Plan报告了这个问题，亚马逊还是删除了正品产品的页面，阻止了进一步的销售。

虽然Try and E参与了诉讼，但只有Excel Plan获得了赔偿。代表原告的律师称赞该裁决具有里程碑意义，承认像亚马逊这样的平台有义务实施适当的认证系统，因为越来越多的企业依赖这些平台。

---

## 99. 一款无喷漆、无音响、无屏幕的2万美元美国产电动皮卡

**原文标题**: A $20k American-made electric pickup with no paint, no stereo, no screen

**原文链接**: [https://www.theverge.com/electric-cars/655527/slate-electric-truck-price-paint-radio-bezos](https://www.theverge.com/electric-cars/655527/slate-electric-truck-price-paint-radio-bezos)

Slate Truck：即将颠覆市场的极简电动皮卡

---

## 100. GCC 15.1

**原文标题**: GCC 15.1

**原文链接**: [https://gcc.gnu.org/gcc-15/](https://gcc.gnu.org/gcc-15/)

本文宣布GCC 15.1将于2025年4月25日发布。文章强调这是一个重要版本，与GCC 14.x相比，包含新的特性和改进。GCC最初是GNU C编译器，由于其对多种语言的支持，现在代表GNU编译器集合。

该公告对众多贡献者表示感谢，感谢他们提供的特性、改进、错误修复、测试结果以及其他使GCC取得成功的变更。文章引导用户访问GCC项目网站和开发邮件列表，以获取有关GCC的更多信息。它还提供了通过镜像站点或版本控制系统获取GCC的链接。

对于用户支持，文章建议查阅网页和GCC手册，如果无效，则查阅gcc-help邮件列表。欢迎在开发者列表上提供关于网页和GCC开发的反馈。本文档由自由软件基金会公司版权所有，最后修改于2025年4月25日。

---

