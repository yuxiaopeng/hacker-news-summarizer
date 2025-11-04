# Hacker News 热门文章摘要 (2025-11-04)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Pg_lake：具有Iceberg和数据湖访问功能的Postgres

**原文标题**: Pg_lake: Postgres with Iceberg and data lake access

**原文链接**: [https://github.com/Snowflake-Labs/pg_lake](https://github.com/Snowflake-Labs/pg_lake)

Pg_lake 将数据湖功能引入 PostgreSQL，使用户能够将 Postgres 用作湖仓一体系统。它集成了 Iceberg，并允许直接查询存储在 S3 等对象存储中的数据湖文件（Parquet、CSV、JSON）。主要功能包括事务性地创建和修改 Iceberg 表、使用 COPY 命令导入/导出数据、读取地理空间格式、透明压缩以及在 SQL 查询中组合不同的数据源（堆、Iceberg、外部文件）。

pg_lake 利用 DuckDB 的查询引擎通过一个单独的进程 `pgduck_server` 来提高性能，该进程通过 PostgreSQL wire 协议进行通信。这避免了将 DuckDB 直接嵌入 Postgres 的限制。

设置包括使用 Docker 获取一个即用型环境，或从源代码构建。初始化包括创建所需的 PostgreSQL 扩展并运行 `pgduck_server`。配置需要设置云凭证和默认的 Iceberg 位置。

该架构包括带有 pg_lake 扩展的 PostgreSQL 和 `pgduck_server`。pg_lake 采用模块化设计，其扩展处理 Iceberg、外部数据包装器、COPY 操作等。组件包括：`pg_lake_iceberg`、`pg_lake_table`、`pg_lake_copy`、`pg_lake_engine`、`pg_extension_base`、`pg_extension_updater`、`pg_lake_benchmark`、`pg_map`、`pgduck_server` 和 `duckdb_pglake`。

该项目最初由 Crunchy Data 开发为 Crunchy Bridge for Analytics，后由 Snowflake 作为 pg_lake 开源。

---

## 2. Show HN: 纯CSS地形生成器

**原文标题**: Show HN: A CSS-Only Terrain Generator

**原文链接**: [https://terra.layoutit.com](https://terra.layoutit.com)

Show HN: Layoutit Terra - CSS地形生成器。这款工具允许用户直接使用CSS创建地形景观，无需JavaScript或图像。

界面提供多种控件来自定义地形，包括：

*   **重新生成:** 用户可以一键生成新的地形。
*   **撤销/重做:** 用于试验更改的基本编辑功能。
*   **导入/导出:** 能够导入自定义高度图，并以各种格式（CSS、VOX、TXT、PNG）导出生成的地形。
*   **代码导出:** 复制CSS代码、嵌入生成器、在Codepen中打开项目或下载整个代码的选项。
*   **地形操作:** 移动、升高和降低地形特征以及调整世界大小的工具。
*   **地形参数:** 大陆覆盖率（小、中、大）、地形类型（潘帕斯草原、丘陵、登山型）和生物群落（温带、北极、沙漠）的控件。
*   **相机设置:** 可调整的相机参数，如X轴旋转、Y轴倾斜、缩放、X轴平移和Y轴抬升，以及动画视图选项。
*   **可视化选项:** 地形的迷你地图、高度图和矩阵视图。

该工具似乎处于早期阶段（v0.0.1），专注于提供一种使用CSS生成地形的新颖方法，可能提供性能优势和独特的样式能力。 重点是直接操作和代码生成，使其对寻求在其Web项目中创建风格化3D景观的开发人员非常有用。

---

## 3. 针对GPU优化Datalog

**原文标题**: Optimizing Datalog for the GPU

**原文链接**: [https://danglingpointers.substack.com/p/optimizing-datalog-for-the-gpu](https://danglingpointers.substack.com/p/optimizing-datalog-for-the-gpu)

无法访问文章链接。

---

## 4. 什么是流形？

**原文标题**: What is a manifold?

**原文链接**: [https://www.quantamagazine.org/what-is-a-manifold-20251103/](https://www.quantamagazine.org/what-is-a-manifold-20251103/)

Paulina Rowińska 的文章《什么是流形？》介绍了流形的概念，这是现代几何学和物理学中的一个基本概念，由伯恩哈德·黎曼开创。流形是一种局部观察时呈现欧几里得空间（平坦）形态的空间，即使其整体结构更为复杂，如地球表面。

文章解释说，黎曼的工作将曲面研究推广到任何维度的空间，影响了拓扑学、几何学和相对论等领域。其核心思想是，流形可以分解为重叠的“图表”，每个图表都类似于一块欧几里得空间，使数学家能够应用熟悉的微积分技术。这些图表的集合称为图册。

文章通过实例说明了流形的用途。爱因斯坦的广义相对论将时空描述为一个四维流形。文章还展示了流形如何简化复杂问题，例如通过将双摆的可能状态表示为环面（一种甜甜圈形状的流形）上的点来分析双摆的运动。流形也用于分析高维数据集。文章强调了流形在科学中普遍存在的性质，将其重要性与数字的重要性相提并论。

---

## 5. 发布HN：Plexe (YC X25) – 从提示词构建生产级机器学习模型

**原文标题**: Launch HN: Plexe (YC X25) – Build production-grade ML models from prompts

**原文链接**: [https://www.plexe.ai/](https://www.plexe.ai/)

Plexe AI，一家YC X25创业公司，提供一个从自然语言提示构建生产级机器学习模型的平台，目标客户是希望利用人工智能但又不需要大量数据科学专业知识的企业。他们提供一个“代理机器学习工程团队”来将原始数据转化为工程化的AI解决方案。

Plexe的工作流程包括连接数据、自动检查数据质量并识别模式。用户可以用简单的语言描述他们想要的模型，指定预测任务和相关数据。Plexe构建一个为业务挑战量身定制的、可用于生产的模型，并通过清晰的性能指标、训练细节和解释来强调透明度。

该平台支持金融（欺诈检测、信贷承销、客户流失预测）、电子商务、物流和网络安全等各行业的各种用例。它提供数据仪表板、API端点、批处理作业以及文件上传/数据库连接器等功能。

Plexe强调可访问性和易用性，旨在使企业能够在数小时而不是数月内部署机器学习模型。他们强调对透明度和控制的承诺，让用户可以全面了解模型性能和训练情况。Plexe提供博客、文档和社区渠道等资源。

---

## 6. 展示一下：我做了一个iOS本地优先的每日计划应用

**原文标题**: Show HN: I built a local-first daily planner for iOS

**原文链接**: [https://apps.apple.com/ca/app/to-do-list-planner-zesfy/id6479947874](https://apps.apple.com/ca/app/to-do-list-planner-zesfy/id6479947874)

无法访问文章链接。

---

## 7. 1988年的今天，莫里斯蠕虫病毒在24小时内感染了10%的互联网。

**原文标题**: This Day in 1988, the Morris worm infected 10% of the Internet within 24 hours

**原文链接**: [https://www.tomshardware.com/tech-industry/cyber-security/on-this-day-in-1988-the-morris-worm-slithered-out-and-sparked-a-new-era-in-cybersecurity-10-percent-of-the-internet-was-infected-within-24-hours](https://www.tomshardware.com/tech-industry/cyber-security/on-this-day-in-1988-the-morris-worm-slithered-out-and-sparked-a-new-era-in-cybersecurity-10-percent-of-the-internet-was-infected-within-24-hours)

1988年，康奈尔大学研究生罗伯特·塔潘·莫里斯无意间释放了莫里斯蠕虫，在24小时内感染了大约10%的互联网。该蠕虫旨在衡量互联网的规模，利用了BSD UNIX系统中的漏洞，包括电子邮件系统中的后门和“finger”程序中的漏洞。与病毒不同，莫里斯蠕虫可以自我复制并自主传播。

虽然该蠕虫并非旨在破坏文件，但它导致了严重的系统减速、消息传递延迟和系统崩溃。伯克利、哈佛和美国宇航局等机构受到了影响，其中一些机构不得不完全擦除系统以消除蠕虫。

联邦调查局调查了这起事件，莫里斯被确认为罪魁祸首。他因违反1986年《计算机欺诈和滥用法案》而被起诉，在出庭后，他被处以罚款、缓刑和社区服务。

当时，互联网与今天的版本截然不同，NSFNET是其骨干。据估计，60,000个连接系统中有6,000个受到影响，造成的损失从10万美元到数百万美元不等。文章最后提到了最近的人工智能蠕虫，强调计算机蠕虫仍然是一个相关的威胁。

---

## 8. 使用浏览器代理链式调用FFmpeg

**原文标题**: Chaining FFmpeg with a Browser Agent

**原文链接**: [https://100x.bot/a/chaining-ffmpeg-with-browser-agent](https://100x.bot/a/chaining-ffmpeg-with-browser-agent)

本文片段极其简短，主要围绕标题“使用浏览器代理链接FFmpeg”以及AI平台“100X.Bot”的广告展开。

**概要：**

仅从标题来看，其核心思想是将强大的多媒体框架FFmpeg的功能与“浏览器代理”相结合。FFmpeg通常用于视频和音频的编码、解码、转码和流媒体处理。在此上下文中，浏览器代理可能指的是自动化Web浏览器内交互的程序或脚本。

预期的内容（尽管在提供的片段中没有）很可能会详细介绍如何集成这两种技术。这可能包括：

*   **使用浏览器代理触发FFmpeg进程：** 例如，抓取网站上的视频链接，然后使用FFmpeg下载并转换它们。
*   **使用FFmpeg处理由浏览器代理检索的媒体：** 浏览器代理可能会捕获流媒体视频，然后由FFmpeg处理以进行编辑或存档。
*   **使用浏览器代理控制或监控FFmpeg：** 例如，由浏览器代理控制的Web界面可能允许用户远程管理FFmpeg任务。

包含“100X.Bot | 100x一体化AI代理平台”表明，如果文章完整，可能会探讨如何使用AI代理技术在浏览器环境中协调这些FFmpeg工作流程。该平台可能旨在自动化和简化将FFmpeg与基于浏览器的操作相结合的过程。

---

## 9. 服务器DRAM价格飙升50%，AI引发的内存短缺冲击超大规模数据中心。

**原文标题**: Server DRAM prices surge 50% as AI-induced memory shortage hits hyperscalers

**原文链接**: [https://www.tomshardware.com/pc-components/storage/server-dram-prices-surge-50-percent](https://www.tomshardware.com/pc-components/storage/server-dram-prices-surge-50-percent)

AI需求激增推动服务器DRAM价格大幅上涨。超大规模厂商面临DRAM短缺，即使同意第四季度提价高达50%，也仅收到70%的订单。这是由于三星和SK海力士等主要DRAM制造商将产能转移到HBM和其他人工智能加速所需的内存类型。

因此，即使是最大的买家也在努力确保足够的内存，导致现货价格飙升，一些供应商已停止10月份的报价。DDR5 16GB 模组的价格自 9 月以来几乎翻了一番。较小的原始设备制造商和渠道商面临更大的挑战，交付率低至 35%-40%，迫使他们转向昂贵的现货市场或被迫等到 2026 年。

美光和集邦咨询已警告 DRAM 市场供应紧张，预测明年供应增长将滞后于需求，并可能出现报价冻结和转向每日定价的情况。这一趋势也导致零售 DDR5 价格上涨。虽然 DDR4 正在下降，不再是批量生产的重点，但文章总结说，除非需求减少或良率大幅提高，否则小型厂商的 DRAM 分配可能会持续受限至 2026 年。

---

## 10. 布隆过滤器适用于不扩展的搜索。

**原文标题**: Bloom filters are good for search that does not scale

**原文链接**: [https://notpeerreviewed.com/blog/bloom-filters/](https://notpeerreviewed.com/blog/bloom-filters/)

本文探讨了使用布隆过滤器进行全文搜索索引，特别关注了其可扩展性问题。虽然布隆过滤器在小型文档集（如静态网站）上具有空间效率，但作者调查了这种优势是否可以扩展到更大的语料库。

作者首先提出并否定了两个想法：排序布隆过滤器和将其构造成树。排序失败是因为一个简单的反例打破了假设，而树结构则由于文本文档之间的显著重叠而遭受“维度诅咒”，迫使每次查询都搜索几乎每个文档。

一个可行的解决方案是创建布隆过滤器的倒排索引。这类似于传统的倒排索引，但使用树来表示字典，从而可能减小索引大小，因为布隆过滤器使用比直接存储单词更少的位来表示单词。

尽管有这个解决方案，作者最终得出结论，基于布隆过滤器的索引不适合大型文档集。虽然布隆过滤器在少数过滤器中紧凑地表示大型字典，但随着文档数量的增加，其空间效率会降低。每个文档都需要自己的布隆过滤器，冗余地编码其单词，而倒排索引仅存储每个字典单词一次，并在所有文档之间共享它。仅在几千个文档之后，布隆过滤器方法的空间节省就会丢失，而传统的倒排索引变得更节省空间。

核心问题是布隆过滤器之间缺乏协同作用；每个都独立运作。作者将这种见解扩展到其他问题领域，强调在小规模上有效的（例如，使用布隆过滤器实现的全局阻止列表）可能在单个用户创建自己的实例时（例如，用户特定的阻止列表）无法很好地扩展。

---

## 11. 美国初创公司Substrate宣布推出芯片制造工具，声称将与阿斯麦竞争。

**原文标题**: US startup Substrate announces chipmaking tool that it says will rival ASML

**原文链接**: [https://www.reuters.com/world/asia-pacific/us-startup-substrate-announces-chipmaking-tool-that-it-says-will-rival-asml-2025-10-28/](https://www.reuters.com/world/asia-pacific/us-startup-substrate-announces-chipmaking-tool-that-it-says-will-rival-asml-2025-10-28/)

美国初创公司Substrate宣布开发一种芯片制造工具，声称将与荷兰公司阿斯麦（ASML）竞争，后者目前主导着先进光刻系统市场。尽管Substrate的技术细节仍然很少，但该公司声称其新工具可以在硅晶圆上生成高分辨率图案，这对于制造尖端半导体至关重要。

该公告发布之际，正值全球半导体行业竞争加剧，各国和公司都在寻求减少对阿斯麦的依赖。美国政府通过《芯片法案》等举措积极鼓励国内芯片制造，这使得Substrate的声明尤其重要。

文章强调了Substrate面临的挑战。阿斯麦在极紫外（EUV）光刻市场占据主导地位，这项技术对于生产最先进的芯片至关重要。构建一个具有竞争力的系统需要大量的资本投资和技术创新。

尽管存在未知数，但Substrate颠覆现有市场的潜力值得关注。如果成功，Substrate可以提供阿斯麦技术的替代方案，可能影响全球半导体供应链和地缘政治格局。该公司的声明需要通过进一步的技术演示和市场应用来验证。

---

## 12. 我的卡车办公桌

**原文标题**: My Truck Desk

**原文链接**: [https://www.theparisreview.org/blog/2025/10/29/truck-desk/](https://www.theparisreview.org/blog/2025/10/29/truck-desk/)

巴德·史密斯的《我的卡车书桌》是一篇幽默而深刻的散文，讲述了在石化厂当机械师和焊工时，如何寻找时间和空间进行创意写作。在一次裁员后重返工作岗位，史密斯发现他心爱的、破旧的F-150，也就是他的移动办公室，已经被报废了。F-150 的关键特征是他定制的“卡车书桌”，一块横跨方向盘和扶手的木板，使他能够在休息期间写作。

这篇散文记录了史密斯在工厂嘈杂和分散注意力的环境中不断寻找工作空间的过程。他最初在手机上写作，并短暂地尝试使用工资单拖车里一间未使用的隔间，但很快就被现场经理赶了出来。然后，他在机修车间搭建了一张桌子，但这张桌子经常被征用用于其他任务。

F-150 里的卡车书桌提供了一个完美的解决方案。史密斯强调了那些将汽车作为个人避难所，在其中进行“真正工作”的足智多谋的人们。在卡车报废后，史密斯进行调整，制作了一个简单的“卡车木板”，可以放在当天船员使用的任何卡车里，使他能够在休息期间继续用笔记本电脑写作。这篇文章强调了作者对创作的奉献，以及适应并“创造自己的条件”以追求创造性努力的重要性，即使在最不可能的环境中也是如此。

---

## 13. 自定义 Nano 文本编辑器

**原文标题**: Customize Nano Text Editor

**原文链接**: [https://shafi.ddns.net/blog/customize-nano-text-editor](https://shafi.ddns.net/blog/customize-nano-text-editor)

本文旨在介绍如何自定义 Nano 文本编辑器。根据标题和作者信息 (Rayhan Aziz Chowdhury Shafi) 可以推断，本文很可能会提供关于如何个性化配置 Nano 文本编辑器，使其更好地满足用户的偏好和工作流程的指导。虽然提供的内容片段很少，但核心重点显然是自定义 Nano。

本文可能涵盖以下主题：

*   **配置文件：** 解释 Nano 配置文件的位置和结构（`.nanorc` 或类似文件）。
*   **自定义语法高亮：** 启用或修改不同编程语言和文件类型的语法高亮。
*   **键盘快捷键：** 定义或更改常用编辑任务的键盘快捷键。
*   **其他选项：** 调整自动缩进、行号、拼写检查和其他功能的设置，以改善编辑体验。

本质上，本文是为用户个性化 Nano 环境的指南，使其在编码或一般文本编辑方面更高效和更有成效。由 DevOps 和全栈工程师撰写表明，自定义可能偏向于对软件开发有用的方面。

---

## 14. YouTube AI错误导致创作者频道因涉嫌关联日本账户而被封禁

**原文标题**: YouTube AI error costs creator his channel over alleged link to Japanese account

**原文链接**: [https://piunikaweb.com/2025/11/04/youtube-ai-error-terminates-enderman-channel/](https://piunikaweb.com/2025/11/04/youtube-ai-error-terminates-enderman-channel/)

无法访问文章链接。

---

## 15. Devtools如何将压缩后的JS代码映射回你的TypeScript源代码

**原文标题**: How devtools map minified JS code back to your TypeScript source code

**原文链接**: [https://www.polarsignals.com/blog/posts/2025/11/04/javascript-source-maps-internals](https://www.polarsignals.com/blog/posts/2025/11/04/javascript-source-maps-internals)

本文阐述了源映射如何通过将压缩后的 JavaScript 代码映射回原始 TypeScript 源代码，从而实现对压缩后代码的调试。当生产环境中发生错误时（例如，`bundle.min.js:1:27698`），源映射会将此位置转换为原始 TypeScript 文件中对应的行和列（例如，`src/index.ts:73:16`）。

本文详细介绍了 TypeScript 构建流程，包括转译、打包和压缩，源映射在每个阶段都保留与原始代码的连接。

本文深入探讨了源映射文件的结构（通常为 `.js.map`），其中包括 `version`、`file`、`sources`、`names` 等字段，最重要的是 `mappings` 字段。`mappings` 字段包含压缩的位置映射，使用变长数量 (VLQ) 编码将生成的 JavaScript 中的 token 链接到它们的原始位置。

VLQ 编码使用 Base64 字符有效地表示位置差异。映射字符串是一系列以逗号分隔的段，分号作为换行符。每个段表示从生成文件中位置到源文件中位置的映射，包含有关生成列、源文件索引、源行、源列和原始名称（如果适用）的信息。VLQ 通过编码符号位、拆分为 5 位组并将其转换为 Base64 来压缩此数据。它不是存储绝对位置，而是存储与先前位置的差异，从而使映射更加紧凑。

本质上，源映射弥合了优化后的生产代码和对开发者友好的源代码之间的差距，从而极大地帮助了调试。

---

## 16. 你无法用cURL获取边界。

**原文标题**: You can't cURL a Border

**原文链接**: [https://drobinin.com/posts/you-cant-curl-a-border/](https://drobinin.com/posts/you-cant-curl-a-border/)

本文详细介绍了作者创建名为“Residency”的应用程序的历程，该应用程序旨在追踪和预测因国际旅行引起的潜在移民和税务问题。 由于各种政府法规（申根、英国税务居民身份、签证要求）的复杂性和不透明性，作者感到沮丧，意识到仅仅依靠电子表格是不够的，因此构建了一个类似于linter的工具，以便在预订旅行*之前*主动识别问题。

核心问题在于，这些系统不会暴露您当前的状态，迫使旅行者手动穿梭于不同的规则、时区考虑和边缘情况（例如，英国公民身份申请的具体日期、机场过境期间“存在”的定义）迷宫之中。

“Residency”通过以下方式解决此问题：

*   使用精确的时间戳和存在理由跟踪旅行历史。
*   模拟未来旅行并应用特定于位置的规则（存储为版本化的“解释”）来预测潜在问题。
*   检查护照有效期、签证要求和其他相关文件约束。
*   出于隐私和性能原因，将数据保存在本地，避免服务器端责任。

该应用程序被呈现为一个实用的工具，适用于经常进行国际旅行的任何人，使他们能够通过预测未来问题来做出明智的决策并避免代价高昂的错误。 作者最后以预订廉价冰岛航班为例，说明了“Residency”如何帮助确保该航班不会违反任何旅行规则或影响他们即将到来的移居加拿大的英国税务居民身份。

---

## 17. The 512KB Club

**原文标题**: The 512KB Club

**原文链接**: [https://512kb.club/](https://512kb.club/)

生成摘要时出错

---

## 18. 二极管的妙用

**原文标题**: Things you can do with diodes

**原文链接**: [https://lcamtuf.substack.com/p/things-you-can-do-with-diodes](https://lcamtuf.substack.com/p/things-you-can-do-with-diodes)

无法访问文章链接。

---

## 19. 从索尼相机恢复我不小心删除的视频

**原文标题**: Recovering videos from my Sony camera that I stupidly deleted

**原文链接**: [https://www.jeffgeerling.com/blog/2025/recovering-videos-my-sony-camera-i-stupidly-deleted](https://www.jeffgeerling.com/blog/2025/recovering-videos-my-sony-camera-i-stupidly-deleted)

本文详细描述了作者在不小心从电脑和备份驱动器中删除索尼相机SD卡中的视频素材后，尝试恢复已删除视频的令人沮丧的经历。作者概述了他们通常的备份流程，以及一系列错误是如何导致数据丢失的。

最初，他们尝试使用PhotoRec，它恢复了许多文件，但文件名是随机的，并且有两种文件类型：.mp4 和 _moov.mov。即使使用脚本将这些文件组合起来，也无法生成可播放的视频。随后，作者创建了SD卡的完整磁盘镜像备份，以防止进一步的数据丢失。

接下来，作者尝试了untrunc，这是一种专门用于恢复截断的MP4文件（包括索尼XAVC文件）的工具。通过提供一个“良好”的参考MP4文件，untrunc生成了部分恢复的文件，其中包含短暂的可播放片段，但视频卡顿，音频失真。使用多个参考文件进一步尝试untrunc并没有产生明显的改进。

受一篇关于MP4文件结构的文章启发，作者推测_moov.mov文件可能需要在MP4文件的末尾，并尝试按此顺序将它们连接起来，但未成功。

最后，作者转向商业软件Disk Drill，希望能获得更好的结果。虽然Disk Drill的界面令人耳目一新，但恢复的文件仍然无法播放，并且需要与PhotoRec文件相同的局部恢复尝试。作者发现了Disk Drill的“高级相机恢复模块”，并重新扫描了SD卡。文章在作者揭示这最后一次尝试是否成功之前戛然而止。作者花费了大量的时间和磁盘空间进行恢复实验，因此决定很快停止。

---

## 20. 火柴人打架时

**原文标题**: When stick figures fought

**原文链接**: [https://animationobsessive.substack.com/p/when-stick-figures-fought](https://animationobsessive.substack.com/p/when-stick-figures-fought)

无法访问文章链接。

---

## 21. AI的拨号时代

**原文标题**: AI's Dial-Up Era

**原文链接**: [https://www.wreflection.com/p/ai-dial-up-era](https://www.wreflection.com/p/ai-dial-up-era)

本文将互联网早期（“拨号时代”）与当前的人工智能状态进行对比，认为我们正处于类似的炒作、不确定性和潜在过度投资阶段。

文章告诫人们不要对人工智能对就业的影响过于乐观或悲观。虽然有些人预测会大规模失业，但作者以放射学领域为例，指出由于杰文斯悖论，人工智能实际上*增加*了需求和就业：效率的提高导致更大的消费。然而，这种效应并非普遍适用。

文章认为，就业结果取决于一个行业中未被满足的市场需求与通过自动化实现的生产力提高速度之间的平衡。具有高未被满足需求的行业（如汽车行业）可能会看到持续甚至增长的就业，而需求饱和的行业（如纺织业）可能会经历失业。软件行业提出了一个独特的案例，如果人工智能能够显著降低开发成本，则可能存在巨大的潜在需求。

文章还分析了当前的人工智能繁荣是否是一个泡沫，并将其与互联网泡沫时代进行了比较。虽然承认对人工智能基础设施的大量投资以及OpenAI等公司的快速增长，但它认为需求是真实的，但存在过度建设和惊人失败的可能性。然而，与互联网泡沫类似，正在建设的基础设施可能会比炒作更持久，并促进未来的创新。

总而言之，作者提出了一个可预测的不可预测的未来：变革即将到来，但细节难以预见。人工智能将通过降低成本来解锁新的市场领域，从而实现以前负担不起的产品和服务。预计新的领域和行业将会出现，并以我们目前无法想象的方式受到人类创造力的塑造。

---

## 22. 美国农业部威胁向食品券受益者提供折扣的商店

**原文标题**: USDA Threatens Stores Giving Discounts to People on Food Stamps

**原文链接**: [https://newrepublic.com/post/202604/usda-threatens-grocery-stores-discounts-people-food-stamps](https://newrepublic.com/post/202604/usda-threatens-grocery-stores-discounts-people-food-stamps)

本文重点关注特朗普政府停摆对补充营养援助计划（SNAP），俗称食品券的影响。文章重点阐述了几个关键问题：

*   **折扣限制：** 美国农业部警告杂货店不得向受政府停摆影响的SNAP受益者提供折扣，理由是“平等待遇规则”。一些商店因此取消了折扣。
*   **SNAP资金危机：** 尽管法院下令使用应急资金用于SNAP，但政府尚未遵守，导致数百万受益者得不到援助。这也威胁到低收入地区的零售商。
*   **政治僵局：** 文章将政府停摆归咎于共和党，伯尼·桑德斯敦促民主党人坚决反对特朗普的要求。他将这种情况描述为总统以牺牲工薪家庭为代价的权力攫取。
*   **移民突袭：** 文章详细描述了在芝加哥进行的激进移民执法行动，联邦特工对居民使用武力。特朗普为这些突袭辩护，称行动还不够深入。
*   **应急基金争议：** 财政部长斯科特·贝森特声称，尽管已有裁决，政府仍需要法院对SNAP资金的指导。他指责民主党人造成政府停摆和资金问题。
*   **联邦调查局飞机滥用：** 联邦调查局局长卡什·帕特尔被指控使用政府飞机与女友进行私人旅行，导致争议和联邦调查局内部的人事变动。

---

## 23. Phomemo 热敏/标签打印机逆向工程 CUPS 驱动

**原文标题**: Reverse-engineered CUPS driver for Phomemo receipt/label printers

**原文链接**: [https://github.com/vivier/phomemo-tools](https://github.com/vivier/phomemo-tools)

本文档描述了一个逆向工程的 CUPS 驱动程序和工具，用于从 Linux 打印到 Phomemo M02、M110、M120 和 M220 热敏打印机。该驱动程序通过分析 Android 应用程序的蓝牙和 USB 通信开发而成。

本文档提供了通过蓝牙和 USB 连接到打印机的说明。对于蓝牙，它概述了使用 `bluetoothctl` 进行配对以及通过 `rfcomm` 进行连接的过程。对于 USB，它详细介绍了如何使用 `lsusb` 识别设备并通过 `/dev/usb/lp0` 或 `ttyACM0` 访问它。

文档的核心内容解释了如何安装和配置 CUPS 驱动程序。安装涉及使用 `make` 和 `make install` 从源代码构建驱动程序。可以通过 GUI 或使用 `lpadmin` 命令行进行配置。本文档提供了针对 M02、M110、M120 和 M220 打印机设置蓝牙和 USB 连接的特定 `lpadmin` 命令，并指定了相应的 PPD 文件。它解释了如何使用 `lpoptions` 验证打印机选项，并提供了使用 CUPS 打印文本和图像的示例命令，包括指定介质类型。

最后，本文档深入探讨了用于 M02 和 M110/M120/M220 打印机的逆向工程协议，详细介绍了基于 EPSON ESC/POS 命令的标头、块标记、页脚和图像数据格式。它概述了用于打印机初始化、对齐方式、光栅图像打印和介质类型选择的特定字节序列。

---

## 24. Aisuru僵尸网络从DDoS攻击转向住宅代理

**原文标题**: Aisuru botnet shifts from DDoS to residential proxies

**原文链接**: [https://krebsonsecurity.com/2025/10/aisuru-botnet-shifts-from-ddos-to-residential-proxies/](https://krebsonsecurity.com/2025/10/aisuru-botnet-shifts-from-ddos-to-residential-proxies/)

最初以打破记录的DDoS攻击而闻名的Aisuru僵尸网络，已将其重心转移到出租其庞大的受感染IoT设备网络作为住宅代理。这使得网络犯罪分子能够匿名化其流量，并使恶意活动更难追踪。专家认为，这种代理的涌入正在助长用于人工智能项目的大规模数据收集，使内容抓取者能够通过伪装成普通互联网用户来逃避检测。

Aisuru控制着至少70万台设备，由于大量的出站攻击流量，对ISP造成了重大破坏。虽然ISP正在共享黑名单，但Aisuru的运营者已经更新了他们的恶意软件，以方便将设备出租给代理服务。这些服务被用于合法目的，但经常被滥用于网络犯罪，包括广告欺诈和凭据填充。

住宅代理市场正经历“疯狂”增长，最近观察到数亿个独特的住宅代理IP。虽然像Luminati (Bright Data)和Oxylabs等一些供应商声称遵守“了解你的客户”政策，但许多其他供应商的运营方式更加隐蔽，通常充当带宽经销商或将SDK捆绑到应用程序中，这些应用程序悄悄地将用户的设备变成流量中继。总部位于中国的代理网络IPidea被认为是该生态系统中的主要参与者。

住宅代理的兴起与用于人工智能开发的积极内容抓取密切相关。公司正在使用这些代理来绕过限制并从网站收集数据，有时会使社区维护的基础设施过载。这导致了法律行动，例如Reddit对Oxylabs提起诉讼，指控其促成大规模抓取。像Cloudflare这样的公司甚至正在尝试对人工智能爬虫访问内容收费的方法。Aisuru是这种代理可用性的主要贡献者，但不是唯一的贡献者。

---

## 25. 坚韧 - 一款多轨音频编辑器/录音机

**原文标题**: Tenacity – a multi-track audio editor/recorder

**原文链接**: [https://tenacityaudio.org](https://tenacityaudio.org)

Tenacity是一款免费开源、跨平台的多音轨音频编辑和录制软件，适用于Windows、Linux和其他操作系统。它由志愿者开发，提供用户友好的界面和一系列功能，包括从各种音频设备录音、导入和导出多种音频格式（可通过FFmpeg扩展），以及支持高达32位浮点音频以获得高质量音频。

该软件支持VST、LV2和AU插件，允许扩展功能，并支持使用Nyquist、Python、Perl和其他语言进行脚本编写。用户可以执行任意采样和多音轨时间线编辑，并具有诸如键盘导航、屏幕阅读器支持和旁白辅助等辅助功能。该程序还提供音频信号分析工具。

预编译版本和源代码可在存储库中找到。用户可以通过Matrix频道（#tenacity2:matrix.org）寻求帮助，在Mastodon上关注项目的新闻和活动，或参与Lemmy社区的讨论。开发在Codeberg上进行，GitHub上有一个镜像以方便访问。欢迎遵循贡献指南进行贡献。该项目还提供邮件列表链接和关于旧版本、Audacium和Saucedacity的信息，供那些对项目历史和分支感兴趣的人参考。

---

## 26. 农民被取代 [视频]

**原文标题**: The Farmer Was Replaced [video]

**原文链接**: [https://www.youtube.com/watch?v=aP2WHQKJVsw](https://www.youtube.com/watch?v=aP2WHQKJVsw)

提供的文本并非文章，而是YouTube上常见的标准页脚信息。它包括指向YouTube各种资源和政策的链接，例如：

*   **版权信息：**与版权问题相关的链接。
*   **联系方式：**关于新闻和其他事项如何联系YouTube。
*   **创作者信息：**内容创作者的资源。
*   **广告：**关于在YouTube上投放广告的信息。
*   **法律：**指向服务条款、隐私政策和安全信息的链接。
*   **YouTube运作方式：**关于YouTube功能的信息。
*   **实验性功能：**关于正在测试的新功能的信息。
*   **NFL Sunday Ticket：**对YouTube提供的NFL Sunday Ticket服务的提及（© 2025 Google LLC）。

本质上，这是一段样板文字，提供了关于YouTube平台的基本法律和功能细节。它没有提供关于视频标题“The Farmer Was Replaced”（农民被取代）的任何信息，也没有包含任何相关或有意义的新闻内容。

---

## 27. Linux进程内存的友好导览

**原文标题**: A friendly tour of process memory on Linux

**原文链接**: [https://www.0xkato.xyz/linux-process-memory/](https://www.0xkato.xyz/linux-process-memory/)

Linux进程内存管理详解 (x86-64架构)

本文详细介绍了Linux上的进程内存管理，重点关注x86-64架构。它解释了Linux如何为程序创建连续内存的错觉，尽管物理RAM的现实是碎片化的。关键在于虚拟内存，它通过页表将虚拟地址映射到物理帧进行管理。当RAM已满时，磁盘充当扩展。

本文深入探讨了虚拟内存区域（VMA）的概念，它是具有统一权限和后备存储的连续地址范围。内存操作通过`mmap`（保留地址范围）、`mprotect`（更改权限）和`munmap`（删除映射）进行。实际的内存分配发生在首次访问页面时，如果缺少转换，则会触发页面错误。内核通过分配一个零填充的页面（匿名映射）或从存储读取（文件映射）来处理这些错误。

本文还解释了`fork()`期间的写时复制（CoW）行为以及`MAP_PRIVATE`的工作原理。 `mprotect`会因TLB失效而产生较小的性能损失。它展示了如何使用`/proc/<pid>/maps`、`/proc/<pid>/smaps`检查内存映射，以及使用更详细的工具（如`/proc/<pid>/pagemap`、`/proc/kpagecount`和`/proc/kpageflags`）获取逐页信息，并承认某些信息仅限于特权用户。

最后，本文介绍了透明大页（THP）和多尺寸THP（mTHP），并讨论了通过`/sys/kernel/mm/transparent_hugepage/`进行的配置选项。这些尝试通过使用更大的页面来减少错误计数和TLB压力。本文提供了确定THP是否工作的工具，并提到了权衡，例如碎片整理。

---

## 28. 雅达利艺术 (2016)

**原文标题**: The Art of Atari (2016)

**原文链接**: [http://www.artofatari.com](http://www.artofatari.com)

《雅达利艺术》，由Dynamite出版，是一部官方收藏集，展示了来自世界各地私人收藏的雅达利40多年来的独特艺术作品。本书收录了用于包装、广告和目录中的插图，旨在提升雅达利体验，并吸引儿童和成人进入电子娱乐世界。

本书全面回顾了游戏制作和概念艺术作品、照片和营销材料。读者将从雅达利历史上的关键人物那里获得见解，并了解包括《小行星》、《蜈蚣》和《导弹指挥官》等标志性游戏在内的众多雅达利游戏的构思、插图、批准（或拒绝）和创作的幕后细节。

作者蒂姆·拉佩蒂诺将雅达利描述为一种文化试金石，它让许多人首次接触到电子游戏。本书面向雅达利粉丝、收藏家、爱好者和新手，提供了有史以来最完整的雅达利艺术作品集。

本书可通过当地独立书店和漫画店购买。 Atari和Atari标志是Atari Interactive Inc.的注册商标。

---

## 29. 学习阅读亚瑟·惠特尼的C语言以变得聪明 (2024)

**原文标题**: Learning to read Arthur Whitney's C to become smart (2024)

**原文链接**: [https://needleful.net/blog/2024/01/arthur_whitney.html](https://needleful.net/blog/2024/01/arthur_whitney.html)

本文详细介绍了作者尝试理解Arthur Whitney为K语言解释器编写的高度精简的C代码的过程。Whitney以创建用于金融领域并需要最少代码的语言和数据库（A、K、Q、kdb、Shakti）而闻名。

作者分解了这个50行的C解释器，逐行解释每行代码和宏，强调了Whitney非常规编码风格带来的挑战，这种风格优先考虑简洁性并将逻辑置于单个屏幕上。作者赞赏这种方法，因为它有可能通过预先展示全部复杂性来提高代码的可理解性。

作者研究了用于函数定义、错误处理和常见操作的自定义宏。他们还深入研究了代码如何使用`char*`处理整数和指针，并解释了用于向量操作、算术运算和错误处理的函数。作者指出，Whitney的编程风格旨在通过使用小型、高度可重用的逻辑块来减少错误。

最终，作者赞赏这一挑战，并看到了学习阅读并可能采用Whitney风格的各个方面的潜在好处，即使最初令人望而生畏。他们更好地理解了如何用代码简洁性换取可读性，并将整个代码库显示在一个屏幕上。

---

## 30. 从数独解算器中学习 (2007)

**原文标题**: Learning from Sudoku Solvers (2007)

**原文链接**: [http://ravimohan.blogspot.com/2007/04/learning-from-sudoku-solvers.html](http://ravimohan.blogspot.com/2007/04/learning-from-sudoku-solvers.html)

本文《从数独解题器学习》以 Ron Jeffries 尝试构建数独解题器为例，旨在突出测试驱动开发（TDD）的潜在缺陷。它将 Jeffries 的方法与 Peter Norvig 成功的解题器进行了对比。

核心论点，辅以 Peter Seibel（《编程之美》作者）的评论，指出 Jeffries 从一开始就陷入了数据表示和底层实现细节的泥潭，不断地重构和调整测试，而没有在实际的解题算法上取得重大进展。Seibel 认为，当程序员对解决方案缺乏清晰的理解时，这是应用 TDD 时的常见模式。相比之下，Norvig 迅速建立了一个简洁的数据表示，并转向了更复杂的解决问题的逻辑。

本文强调，在早期数据结构设计上花费过多时间，尤其是在 TDD 框架内，可能会适得其反，并表明对底层问题缺乏理解。文章指出了 Norvig 所展示的更有效、精简的方法。进一步的更新包括对 TDD 局限性的讨论，表明 TDD 虽然有价值，但可能并不具有普遍适用性，并且有其自身的挑战。

---

## 31. 人工智能正在思考的案例

**原文标题**: The Case That A.I. Is Thinking

**原文链接**: [https://www.newyorker.com/magazine/2025/11/10/the-case-that-ai-is-thinking](https://www.newyorker.com/magazine/2025/11/10/the-case-that-ai-is-thinking)

人工智能正在思考的案例

---

## 32. Show HN: Yourshoesmells.com – 寻找最臭的抱石馆

**原文标题**: Show HN: Yourshoesmells.com – Find the most smelly boulder gym

**原文链接**: [https://yourshoesmells.com](https://yourshoesmells.com)

Yourshoesmells.com 是一个旨在根据攀岩鞋散发的“臭味”对抱石馆进行排名的网站。该网站设有一个排行榜，展示“五大最臭健身房”，并通过持续计算来确定“最臭健身房”和“最远健身房”。它追踪用户“访问的健身房数量”，并通过加载图表提供按地区划分的健身房地理信息。

用户可以通过投票来影响排名。该网站需要注册/登录才能参与，并提供请求功能、提供反馈以及通过“请我喝咖啡”以经济方式支持该项目的选项。还提供设置或重置密码的功能。

---

## 33. 马克超级泵浦车是一辆机车引擎消防车（2018年）

**原文标题**: The Mack Super Pumper was a locomotive engined fire fighter (2018)

**原文链接**: [https://bangshift.com/bangshiftxl/mack-super-pumper-system-locomotive-engine-powered-pumper-extinguish-hell-often/](https://bangshift.com/bangshiftxl/mack-super-pumper-system-locomotive-engine-powered-pumper-extinguish-hell-often/)

文章探讨了麦克超级泵浦消防车，一种强大的消防设备。评论建议对令人印象深刻的消防能力感兴趣的读者也应了解纽约市的消防船“消防员II号”。“消防员II号”因其每分钟5万加仑的卓越抽水能力而备受瞩目，超过其姊妹船“消防员I号” 2万加仑每分钟。

---

## 34. Pinecone内部：Slab架构

**原文标题**: Inside Pinecone: Slab Architecture

**原文链接**: [https://www.pinecone.io/learn/slab-architecture/](https://www.pinecone.io/learn/slab-architecture/)

本文深入探讨 Pinecone 的“slab架构”，该架构旨在为各种 AI 应用平衡准确性、新鲜度、可扩展性和可预测的性能。Pinecone 通过将数据组织成称为“slab”的不可变单元来实现这一点。

写入路径确保即时持久性：写入请求被记录、确认并放置在内存中的 memtable 中。此 memtable 定期刷新到对象存储，从而创建 slab。

对于查询，请求会被扇出到所有 slab（包括 memtable），然后合并结果。热门 slab 会被缓存以加快访问速度。

一个关键过程是“slab 压缩”，它在后台重新组织数据。较小的 L0 slab 合并为较大的 L1、L2 等 slab。这可以防止因过多小文件导致的查询速度下降，并允许进行渐进式索引优化。Tombstone 处理更新和删除，在压缩过程中过滤掉旧版本以确保结果的新鲜度。

读取路径优先考虑即时可搜索性。首先检查 memtable，然后将查询扇出到所有 slab。根据 slab 大小使用不同的搜索方法，并使用 roaring bitmap 优化元数据过滤。

这种 slab 架构使 Pinecone 能够提供即时新鲜度、大规模的查询性能、弹性可扩展性和自适应增长，从而有效地抽象出向量搜索的复杂性。

---

## 35. 反对PGVector的理由

**原文标题**: The Case Against PGVector

**原文链接**: [https://alex-jacobs.com/posts/the-case-against-pgvector/](https://alex-jacobs.com/posts/the-case-against-pgvector/)

本文反驳了在生产环境中使用pgvector进行向量搜索的常见建议，强调了简单演示与实际扩展之间的差距。虽然pgvector在Postgres中提供了向量相似度搜索，但与专门的向量数据库相比，它在几个关键领域存在不足。

作者批判了pgvector索引选项（IVFFlat和HNSW）的局限性，详细描述了它们的内存消耗、缓慢的构建时间和对数据库性能的影响，尤其是在索引更新期间。由于持续的向量插入会消耗资源并导致锁竞争，实时搜索成为一个挑战。

维护向量嵌入和相关元数据之间的一致性增加了操作复杂性，需要诸如临时表或副本索引构建等变通方法。由于Postgres对过滤向量搜索的查询计划不佳，查询性能受到影响，从而迫使手动优化并可能导致不准确的结果。结合向量相似度和全文搜索的混合搜索需要自定义实现。

虽然Timescale的pgvectorscale解决了其中一些问题，但它增加了另一层复杂性，并且并非普遍可用（例如，在AWS RDS上）。作者得出结论，托管向量数据库提供了卓越的功能，如智能查询计划、内置混合搜索、实时索引、水平扩展和专门的监控，与使pgvector达到生产就绪状态所需的资源和工程时间相比，通常具有具有竞争力的成本。

---

## 36. 瑞典大型软件供应商数据泄露，影响150万用户

**原文标题**: Data breach at major Swedish software supplier impacts 1.5M

**原文链接**: [https://www.bleepingcomputer.com/news/security/data-breach-at-major-swedish-software-supplier-impacts-15-million/](https://www.bleepingcomputer.com/news/security/data-breach-at-major-swedish-software-supplier-impacts-15-million/)

瑞典IT供应商Miljödata发生重大数据泄露事件，影响约150万人，瑞典隐私保护局 (IMY) 正在对此进行调查。Miljödata为瑞典约80%的市政当局提供服务，该公司于2025年8月报告了该事件，披露攻击者窃取了数据并勒索1.5个比特币。

此次泄露事件导致多个区域的运营中断。IMY 正在优先调查 Miljödata 的安全措施以及哥德堡市、埃尔姆胡尔特市和西曼兰区的数据处理实践，尤其关注儿童信息和受保护身份等敏感数据。

包含姓名、地址、电话号码、政府身份证件和出生日期在内的被盗数据，于2025年9月被Datacarry组织泄露在暗网上。“Have I Been Pwned”服务报告称，有87万人受到影响。IMY 旨在找出安全漏洞以防止未来发生类似事件。对市政当局的调查将涵盖他们如何处理与儿童、受保护身份人员和前雇员相关的数据。

---

## 37. 人类濒死大脑首次记录显示类似记忆闪回的脑电波 (2022)

**原文标题**: First recording of a dying human brain shows waves similar to memory flashbacks (2022)

**原文链接**: [https://louisville.edu/medicine/news/first-ever-recording-of-a-dying-human-brain-shows-waves-similar-to-memory-flashbacks](https://louisville.edu/medicine/news/first-ever-recording-of-a-dying-human-brain-shows-waves-similar-to-memory-flashbacks)

首次记录濒死人脑活动：揭示与记忆提取和做梦相关的脑电波模式

---

## 38. State of Terminal Emulators in 2025: The Errant Champions

**原文标题**: State of Terminal Emulators in 2025: The Errant Champions

**原文链接**: [https://www.jeffquast.com/post/state-of-terminal-emulation-2025/](https://www.jeffquast.com/post/state-of-terminal-emulation-2025/)

In his 2025 update on terminal emulator Unicode support, the author highlights ongoing challenges in accurately displaying diverse Unicode scripts within fixed-width terminal grids. The ucs-detect tool, used for testing, now assesses DEC Private Modes, sixel graphics, and pixel size.

Ghostty, a new terminal built from scratch in Zig by Mitchell Hashimoto, is lauded for its exceptional Unicode support and its potential to become a foundational alternative to libvte. Kovid Goyal's Kitty also performs exceptionally well, and Goyal's publication of a text-splitting algorithm aligns closely with the Python wcwidth specification. They are the only terminals to support Variation Selector 15.

The article details significant performance differences among terminals, with iTerm2 and VTE-based terminals exhibiting notably slow performance. Optimization efforts in Python wcwidth have proven effective, primarily relying on LRU caching due to the repetitive nature of human languages.

The author discusses issues observed in Terminology, iTerm2, Konsole, and Contour regarding DEC Private Mode support. Improvements in libvte, particularly concerning emoji support, are noted as positive developments.

The article concludes by addressing the limitations of fixed-width terminals in displaying complex languages and explores the potential of the newly published text sizing protocol to enable variable-sized text, improving legibility and accessibility. The author suggests that allowing font engines to drive text display, rather than meticulously managing cell and cursor movements, could offer a pathway to better support diverse scripts.


---

## 39. 具名颜色覆盖的RGB空间可视化

**原文标题**: A visualization of the RGB space covered by named colors

**原文链接**: [https://codepen.io/meodai/full/zdgXJj/](https://codepen.io/meodai/full/zdgXJj/)

无法访问文章链接。

---

## 40. Linux内核对WebAssembly (WASM)架构的支持

**原文标题**: WebAssembly (WASM) arch support for the Linux kernel

**原文链接**: [https://github.com/joelseverin/linux-wasm](https://github.com/joelseverin/linux-wasm)

本项目提供用于在 WebAssembly (WASM) 中原生构建和运行 Linux 系统的脚本。它利用了以下几个软件组件：LLVM (Clang, wasm-ld)、打过补丁的 Linux 内核（WASM 架构支持、WASM binfmt、Web 控制台驱动）、musl libc（支持 WASM 目标）、修改后的 BusyBox 内核头文件，以及带有 WASM defconfig 的 BusyBox 本身。使用 BusyBox 安装创建了一个最小的 initramfs，提供了一个 pty 和一个 shell。包含了一个示例 JavaScript WASM 主机运行时，用于演示和调试。

重点包括由于 WASM 的限制，必须以 NOMMU 配置构建 Linux，以及使用代理进行系统调用的替代方案。`linux-wasm.sh` 脚本可自动执行下载和构建过程。提到了针对 LLVM 构建系统错误和 Linux 内核构建系统中需要无空格路径的限制的解决方法。

通过两个容器提供 Docker 支持：`linux-wasm-base` (构建环境) 和 `linux-wasm-contained` (隔离构建)。这些容器简化了构建过程，并为开发和自动化构建服务器提供了选项。可以使用 `LW_WORKSPACE` 等环境变量来自定义 Docker 环境中的工作区文件夹。

---

## 41. Guideline已被Gusto收购

**原文标题**: Guideline has been acquired by Gusto

**原文链接**: [https://help.guideline.com/en/articles/12694322-guideline-has-joined-gusto-faqs-about-our-recent-acquisition](https://help.guideline.com/en/articles/12694322-guideline-has-joined-gusto-faqs-about-our-recent-acquisition)

401(k)提供商Guideline已被薪资、福利和人力资源解决方案公司Gusto收购。目标是为小型企业提供更集成的薪资和401(k)体验，使退休储蓄更简单、更容易。

此次过渡旨在无缝进行，尽量减少中断。用户可以期望当前的Guideline服务照常运行，包括移动应用程序、报表和教育资源的访问以及历史文档。Gusto用户现在可以使用单点登录(SSO)来访问他们的401(k)账户。

要点：

*   **无需立即采取行动：** 参与者的401(k)设置和供款保持不变。
*   **费用无变化：** 当前定价将保持不变。
*   **安全是首要任务：** 现有的安全措施将继续保护账户和个人信息。
*   **投资无变化：** 投资和资产配置将保持不变。
*   **交易将继续进行，不会延误：** 供款、分配和转账将及时处理。
*   **支持保持不变：** 客户可以继续联系clients@guideline.com，参与者可以继续联系support@guideline.com咨询401(k)问题。

预计此次收购将带来未来的增强功能，并在薪资和401(k)管理之间实现更加统一的体验，特别是对于已经使用Gusto薪资的公司。

---

## 42. 我们的小型热敏打印机收到的精彩图画作品集

**原文标题**: Gallery of wonderful drawings our little thermal printer received

**原文链接**: [https://guestbook.goodenough.us](https://guestbook.goodenough.us)

精彩涂鸦展：小小热敏打印机收集的迷人留言簿作品。欢迎大家“给我们画点什么！”，这些作品按时间顺序排列（从2024年12月10日到2024年10月23日），展现了游客们的无限创意。每幅作品都包含姓名（或笔名）、日期和IP地址。一些作品拥有古怪的标题，例如“机器人瑞内（自画像）”和“时间+压力=钻石”。留言簿收录了来自不同地区的贡献者，姓名和IP地址暗示了这一点。页面还显示，目前显示的条目之外还有更多图画可供查看：“正在加载更多精选作品...”

---

## 43. 一定程度的软件臃肿是可以接受的。

**原文标题**: Some software bloat is OK

**原文链接**: [https://waspdev.com/articles/2025-11-04/some-software-bloat-is-ok](https://waspdev.com/articles/2025-11-04/some-software-bloat-is-ok)

生成摘要时出错

---

## 44. Skyfall-GS – 从卫星图像合成沉浸式3D城市场景

**原文标题**: Skyfall-GS – Synthesizing Immersive 3D Urban Scenes from Satellite Imagery

**原文链接**: [https://skyfall-gs.jayinnn.dev/](https://skyfall-gs.jayinnn.dev/)

Skyfall-GS：利用卫星图像和扩散模型生成大规模可探索的3D城市场景，无需昂贵的3D标注，实现沉浸式实时3D探索。其核心是课程驱动的迭代优化策略，逐步提升几何完整性和照片级真实纹理。实验结果表明，与现有方法相比，该方法生成了更优异的跨视角一致几何体和更真实的纹理。

---

## 45. Isotemp OCXO107-10 恒温晶振内部结构

**原文标题**: Inside an Isotemp OCXO107-10 Oven Controlled Crystal Oscillator

**原文链接**: [https://tomverbeure.github.io/2025/10/26/Inside-an-Isotemp-OCXO107-10.html](https://tomverbeure.github.io/2025/10/26/Inside-an-Isotemp-OCXO107-10.html)

本文详细介绍了作者对以区区5美元购得的Isotemp OCXO107-10恒温晶振的探索。这款5 MHz的OCXO被描述为“大块头”，暗示其较大的尺寸意味着更高的稳定性，因为它允许更好的温度控制机制。

作者通过time-nuts邮件列表研究该OCXO，发现了它的历史成本（>1000美元）、朗讯公司之前的使用情况，以及OCXO107-16等变体的存在。他还发现EFC（电子频率控制）引脚有噪声Vref输出。 虽然存在OCXO107-3的数据表，但它与-10型号并不完全相同。

作者成功地为OCXO供电，观察了其在预热阶段的功耗。测量了输出功率和谐波失真。 该设备的标签提供了与EFC调谐相关的参考电压。

感谢联系人Ed Palmer，作者得以深入了解OCXO的内部设计。它采用杜瓦瓶（类似热水瓶）进行热隔离，这是早期高稳定性OCXO的标志。虽然现在存在现代的双层恒温设计，但作者注意到Quantic Wenzel仍然继续使用杜瓦瓶。 内部组件包括振荡器控制板、大晶体、用作加热元件的摩托罗拉达林顿晶体管，以及可能用于温度反馈的TL431电压基准。

作者计划构建一个专用的低噪声电源，以便在其家庭实验室中对OCXO进行长期比较测量，理由是需要更长的稳定期，并且希望摆脱当前嘈杂的台式电源。

---

## 46. 从生产环境中部署AI代理的访谈中得到的教训

**原文标题**: Lessons from interviews on deploying AI Agents in production

**原文链接**: [https://mmc.vc/research/state-of-agentic-ai-founders-edition/](https://mmc.vc/research/state-of-agentic-ai-founders-edition/)

本文探讨了在企业环境中部署人工智能代理所面临的挑战和策略，借鉴了对30多家欧洲代理人工智能初创公司创始人的调查以及对40多位从业者的访谈。它探讨了最初对人工智能代理的怀疑态度，将其与臭名昭著的“Clippy”相比较，并强调了成功部署的重要性。

主要挑战在于工作流程集成、员工抵制和数据隐私，而不是纯粹的技术问题。成功的策略强调“从小处着手”的方法，专注于低风险、高影响的任务，这些任务能够证明投资回报率并增强（而非取代）人类员工的能力。

本文揭示，62%的代理人工智能初创公司正在使用核心业务预算，这表明已经超越了实验阶段。混合定价和按任务定价模型最为常见，而基于结果的定价由于其复杂性仍然很少见。大多数初创公司正在内部构建代理基础设施。

准确性至关重要，超过 90% 的公司报告其解决方案的准确率至少达到 70%。然而，可接受的准确率因行业和用例而异。本文确定了三种配置：中等准确率/高自主性，高准确率/低自主性（在医疗保健领域常见），以及高准确率/高自主性（金融服务、网络安全、客户服务）。

本文还解释了人工智能代理的核心属性：目标导向、推理、自主性和持久性（记忆）。
最后提到，在多代理系统中，对准确性的需求只会增加。

---

## 47. 为什么 Nextcloud 用起来感觉很慢

**原文标题**: Why Nextcloud feels slow to use

**原文链接**: [https://ounapuu.ee/posts/2025/11/03/nextcloud-slow/](https://ounapuu.ee/posts/2025/11/03/nextcloud-slow/)

本文探讨了作者对 Nextcloud 性能缓慢的失望之情。Nextcloud 是一个用于文件存储、日历、联系人和其他服务的自托管平台。虽然作者欣赏 Nextcloud 广泛的功能集和便利性，但他发现即使在配置不错的硬件上，它的速度也一直很慢。

主要原因是即使是基本操作也需要大量的 Javascript。作者列举了几个例子，例如 4.71 MB 的 `core-common.js` 包，日历应用程序基本视图的 5.94 MB，以及 Notes 应用程序编辑器的 4.36 MB。这些大型 Javascript 文件导致加载时间过长，尤其是在较慢的连接和移动设备上。

作者认为，功能与捆绑包大小的比率严重失衡，表明存在架构问题和低效代码。这种糟糕的性能对用户体验产生了负面影响，使得在 Tasks 应用程序中访问购物清单等任务的速度慢得令人无法接受。

因此，作者已经开始用替代方案替换一些 Nextcloud 应用程序，例如使用 Vikunja 来处理任务，使用 Immich 来处理照片，因为这些替代方案提供了明显更小的 Javascript 体积和更高的性能。

作者承认该问题背后可能存在的原因，包括过度劳累的开发团队，但强调了由此产生的对用户体验和可访问性的负面影响。作者最后推荐了 Alex Russell 关于 Web 性能的研究，强调了在 Web 开发中考虑性能和可访问性的重要性。

---

## 48. 美国追踪到勒索软件攻击与两名在网络安全公司工作的人员有关

**原文标题**: US Traces Ransomware Attacks to 2 People Working for Cybersecurity Firms

**原文链接**: [https://www.pcmag.com/news/us-traces-ransomware-attacks-to-2-people-working-for-cybersecurity-firms](https://www.pcmag.com/news/us-traces-ransomware-attacks-to-2-people-working-for-cybersecurity-firms)

两名网络安全专家因涉嫌合谋传播ALPHV勒索软件而被起诉，受害者包括一家无人机制造商、一家工程公司和三家医疗机构。联邦调查人员称，凯文·泰勒·马丁（来自DigitalMint）和瑞安·克利福德·戈德堡（来自Sygnia Cybersecurity Services）二人于2023年5月左右开始实施该计划，感染了一家公司并勒索1000万美元的解密费用，最终获得120万美元。

在一名未透露姓名的同谋协助下，该计划持续到2025年4月，并涉及获得ALPHV/Blackcat勒索软件团伙的联盟账户。戈德堡向FBI供认，称债务是其动机，并表达了悔意。马丁拒不认罪。

DigitalMint和Sygnia均表示，涉事员工的行为是在公司不知情的情况下进行的，随后已被解雇。他们强调，这些攻击并未危及客户数据。联邦调查局正在继续调查。

---

## 49. MP3.com救援驳船

**原文标题**: The MP3.com Rescue Barge Barge

**原文链接**: [https://blog.somnolescent.net/2025/09/mp3-com-rescue-barge-barge/](https://blog.somnolescent.net/2025/09/mp3-com-rescue-barge-barge/)

在2025年9月10日的博客文章中，dotcomboom详细介绍了他们的项目“MP3.com拯救驳船”，旨在创建一个已倒闭的MP3.com音乐的全面档案。他们从互联网档案馆的拯救驳船和时光机下载了1.78TB的数据，其动机是在对互联网档案馆的法律纠纷的担忧中保存这些音乐。

作者遇到了存储挑战，最终使用了一个3TB的硬盘来存放整个集合。最初由于wget的文件夹创建方法造成的混乱，通过使用“Everything”文件索引工具得以解决。项目的核心是创建MP3元数据的数据库。

Winamp 5（通过WACUP）被证明非常擅长处理大型音乐库，可以流畅地浏览和索引标签。作者随后将数据导出为CSV文件，其中包括艺术家、曲目标题和URL等关键信息。然后，作者使用Excel将本地文件路径替换为原始来源URL。

最终的CSV/电子表格包含超过533,046首歌曲的数据，包括曲目和艺术家姓名以及原始mp3.com URL等信息。尽管CSV格式存在一些细微的缺陷，dotcomboom还是在其网站上发布了该数据库，希望它对其他有兴趣探索和保存MP3.com音乐遗产的人有用。

---

## 50. 瓢虫月刊 – 2025年10月

**原文标题**: This Month in Ladybird – October 2025

**原文链接**: [https://ladybird.org/newsletter/2025-10-31/](https://ladybird.org/newsletter/2025-10-31/)

瓢虫浏览器项目在2025年10月颇有成效，合并了来自43位贡献者的217个拉取请求。主要亮点包括欢迎新的赞助商Axeptio和Gravwell，显著提高了Web平台测试(WPT)分数，以及开始开发持久性HTTP磁盘缓存。

在各个领域都进行了性能改进，包括JavaScript字符串和对象属性处理，以及整数算术的优化。 Trusted Types支持已扩展到多个DOM API。添加了对XPath评估的初步支持，使htmx库能够工作。

媒体播放系统经过改进，以实现更好的音频/视频同步和多轨支持。 Ladybird现在支持macOS上的捏合缩放。无障碍DevTools已重新实现，并且在CSS Typed OM API方面取得了进展，包括支持使用大多数类型的CSSStyleValue设置样式以及实现`sibling-count()`和`sibling-index()`。

渲染方面的改进包括CSS和SVG渐变、CanvasPattern支持以及增强的WebGL2缓冲区和帧缓冲区支持。有针对性的WebGL修复改进了Google地图地球视图。

社区的努力仍在继续改进Windows支持，Ladybird现在可以在Windows上运行，并且Gamepad API可以正常工作。

---

## 51. 如何画四足动物

**原文标题**: How to Draw a Tetrapod

**原文链接**: [https://dotat.at/@/2025-10-24-tetrapod.html](https://dotat.at/@/2025-10-24-tetrapod.html)

本文详细介绍了一种绘制和建模混凝土四脚体的方,该结构用于海岸防御，重点介绍了一种源于令人惊讶的观察的新颖方法。作者首先参考了四脚体的原始专利，并注意到一个常见的设计元素：腿端粗短的倒角。

其核心思想是从一个包含四面体的立方体开始构建一个四脚体。通过试验与立方体表面和四面体边缘在公共顶点附近相切的圆，作者发现了一种令人满意的设计，其中腿的长度和宽度与初始立方体边长的一半非常匹配。这与原始四脚体专利中的规格相符。

这个“配方”包括选择一个尺寸（它既是腿的长度/直径，又是四脚体高度的一半），在立方体和四面体内定义四脚体，并从截锥体构建每条腿。关键步骤包括根据从立方体和四面体几何形状导出的锥度，计算四个圆（腰部、大腿、脚踝、鞋底）的半径和位置。作者提供了确定这些值的公式，确保了正确的比例和大约10度的锥角。

最后，创建单个腿，旋转到其适当的位置，并在特定平面上进行裁剪以避免重叠，从而得到完整的四脚体模型。作者最后指出导出设计的优雅性，并思考倒角的起源以及腿部相交处形成的椭圆。他们还提供了指向四脚体及其源代码的 three.js 动画的链接。

---

## 52. 修复泰克TDS220示波器LCD屏幕损坏

**原文标题**: Fixing LCD Screen Corruption of a Tektronix TDS220 Oscilloscope

**原文链接**: [https://tomverbeure.github.io/2025/11/03/TDS220-LCD-Corruption-Fix.html](https://tomverbeure.github.io/2025/11/03/TDS220-LCD-Corruption-Fix.html)

本文详细介绍了对一台在跳蚤市场以25美元购得的泰克TDS220示波器的维修过程，该示波器存在屏幕闪烁和电容问题。作者概述了TDS220的常见问题，包括电容漏液、BNC连接器接地不良以及LCD背光昏暗。

维修过程包括更换电源中的所有11个电解电容，原因是怀疑存在漏液。为方便起见，提供了Digikey零件清单。虽然这解决了电容漏液问题，但屏幕损坏仍然存在。

进一步调查发现，更换了LCD面板内部的三个专用3.3uF 35V电容，从而解决了间歇性屏幕损坏问题，彻底修复了屏幕。由于缺乏完全替代的元件，原始电容被普通电解电容所取代。

作者还更换了老化的CCFL背光灯，尽管亮度改善效果值得商榷，并讨论了LED转换的可能性。

最后，通过回流焊接主PCB上BNC连接器引脚上的焊点，修复了探头补偿产生的不准确方波输出。作者总结说，TDS220现在功能齐全，是其工作台上的一个有用补充。

---

## 53. Vim图

**原文标题**: VimGraph

**原文链接**: [https://resources.wolframcloud.com/FunctionRepository/resources/VimGraph/](https://resources.wolframcloud.com/FunctionRepository/resources/VimGraph/)

VimGraph是一个 Wolfram 语言资源函数，用于构建一个图，该图表示给定文本字符串中简单的 Vim 风格移动。文本中的每个字母都成为图中的一个顶点，边表示使用 Vim 命令（如“h”、“l”、“j”、“k”、“w”、“b”、“e”、“^”和“$”）在字母之间可能的移动。这些命令对应于向左/向右、向上/向下移动，移动到下一个/前一个单词的开头/结尾，或移动到行的开头/结尾。

该函数允许通过“IncludedVimMovements”选项进行自定义，允许用户将图限制为特定的 Vim 命令。“StringPattern”和“CustomPatterns”选项允许基于文本中的字符串匹配定义新的自定义移动模式。也支持标准图选项。

该函数可用于可视化文本中的 Vim 风格导航，计算字母之间的最小按键距离，并探索文本格式（如换行符）对导航效率的影响。一个示例演示了定义自定义移动，允许扩展到标准 Vim 命令集之外。

VimGraph 由 Pavel Hajek 开发，需要 Wolfram 语言 13.0 或更高版本，并根据 Creative Commons Attribution 4.0 International License 获得许可。相关函数包括 `StringPosition`。

---

## 54. 链接器 (2007)

**原文标题**: Linkers (2007)

**原文链接**: [https://www.airs.com/blog/archives/38](https://www.airs.com/blog/archives/38)

伊恩·兰斯·泰勒的博文“链接器第一部分”开启了一个探索链接器复杂性的系列，旨在为程序员揭秘链接过程。他首先进行个人介绍，回忆了自己编写链接器的经历，强调了一贯的目标是提高速度。他于1988年编写了他的第一个链接器，1993/94年编写了第二个，目前正在开发第三个，名为gold。

泰勒随后进行了技术介绍，解释说链接器将目标文件转换为可执行文件和共享库。他概述了典型的软件开发过程，从用C++等语言编写代码到编译成汇编代码，再到目标文件。他指出，由于子例程库的出现，链接器演变为将单独汇编的目标文件合并为单个可执行文件。共享库被提及为链接器职责的后来补充。

该帖子强调了链接器作为软件开发中至关重要但通常不引人注目的步骤的角色，主要侧重于速度。评论部分显示了对该系列未来帖子的期待，特别是关于模板实例化、链接时优化以及链接器不断发展的性质。泰勒暗示将在以后讨论这些主题。此外，还有关于现有链接器文献的讨论，其中提到了Sun的《链接器和库指南》以及John Levine的书，以及关于gold链接器未来的更新。

---

## 55. Show HN: MyTimers.app：离线优先PWA，零构建步骤，零依赖

**原文标题**: Show HN: MyTimers.app offline-first PWA with no build step and zero dependencies

**原文链接**: [https://mytimers.app/](https://mytimers.app/)

无法访问文章链接。

---

## 56. Tiny electric motor can produce more than 1,000 horsepower

**原文标题**: Tiny electric motor can produce more than 1,000 horsepower

**原文链接**: [https://supercarblondie.com/electric-motor-yasa-more-powerful-tesla-mercedes/](https://supercarblondie.com/electric-motor-yasa-more-powerful-tesla-mercedes/)

YASA, a UK-based company owned by Mercedes-Benz, has developed a groundbreaking tiny electric motor that surpasses existing technology in power and performance density. Weighing just 28 pounds, this axial flux motor delivers 750 kilowatts (1,005 horsepower), exceeding the output of four Tesla motors combined and outperforming YASA's previous record holder by 40%.

The motor's continuous power output ranges from 350 to 400 kilowatts (469–536 horsepower), showcasing its ability to sustain high performance. According to YASA, the design uses readily available materials, suggesting potential for scalable production.

This advancement is significant for the EV industry because a lighter motor contributes to a lighter vehicle, resulting in improved efficiency, acceleration, and range. YASA already supplies motors for high-end vehicles like the Mercedes-AMG GT XX concept and the Ferrari 296 GTB. While initially destined for luxury vehicles, the article suggests that with scaled production and reduced costs, this technology could eventually find its way into more affordable EVs, ultimately enhancing their performance and efficiency.


---

## 57. KaTeX – 网页上最快的数学公式排版库

**原文标题**: KaTeX – The fastest math typesetting library for the web

**原文链接**: [https://katex.org/](https://katex.org/)

KaTeX 是一个快速、轻量级且无依赖的 JavaScript 库，用于在网页上排版数学符号。它优先考虑速度，同步渲染数学公式，无需重排页面。其布局基于 TeX，确保打印质量的渲染效果，与数学排版的黄金标准相匹配。

主要特性和优势包括：

*   **速度：** KaTeX 渲染速度快，即使在包含大量公式的页面上也是如此。
*   **打印质量：** 遵循 TeX 标准，实现准确且专业的排版效果。
*   **自包含：** 无需外部依赖，简化了与 Web 项目的集成。
*   **服务器端渲染：** 在各种浏览器和环境中提供一致的输出，支持使用 Node.js 进行预渲染。

本文提供了安装说明、文档和 GitHub 存储库的链接。 它还提供了一个实时演示，用户可以在其中键入 LaTeX 表达式并查看 KaTeX 如何渲染它。

此外，该文档还列出了可用的 KaTeX 选项，例如 `displayMode`、`throwOnError` 和 `macros`，这些选项允许自定义渲染过程。它还提到了编辑器选项。

KaTeX 被认为是一种优于其他数学排版库（如 MathJax）的替代方案，尤其是在速度方面。该库由 Emily Eisenberg 和 Sophie Alpert 创建，采用 MIT 许可，并利用了许多个人的贡献。

---

## 58. 跨模态视觉特征：SVG与ASCII艺术的跨模态理解

**原文标题**: Visual Features Across Modalities: SVG and ASCII Art Cross-Modal Understanding

**原文链接**: [https://transformer-circuits.pub/2025/october-update/index.html#svg-cross-modal](https://transformer-circuits.pub/2025/october-update/index.html#svg-cross-modal)

Anthropic 可解释性团队的这篇文章探讨了大型语言模型 (LLM) 如何理解基于文本模态（如 SVG 和 ASCII 艺术）中的视觉特征。研究人员发现，LLM 发展出“跨模态特征”，可以识别不同文本表示形式（ASCII、SVG 甚至各种语言的散文描述）中的语义概念，例如“眼睛”、“嘴巴”、“狗”和“猫”。

这些特征具有上下文依赖性；例如，只有当 SVG 圆圈位于被识别为面部的更大结构中时，才会被识别为眼睛。这些特征还能抵抗颜色和半径等表面层次的变化。研究发现，这些跨模态特征存在于从 Haiku 3.5 到 Sonnet 4.5 的模型中，并在稀疏自编码器中被识别出来。

研究人员还研究了这些特征是否可以用于*生成*视觉描绘。他们发现，通过使用特定特征来引导模型，他们可以以语义上有意义的方式修改基于文本的艺术，例如将微笑变成皱眉或在脸上添加皱纹。与预测特定概念的标记相关的运动神经元特征，被证明比纯粹的感知神经元更有效地用于引导。

文章最后提出了更多问题，包括模型是否可以捕捉更高层次的语义（如美学），识别最适合引导的特征属性，将视觉输出与其他可解释性工具结合，以及理解特征激活背后的计算机制。

文章的第二个不相关的部分描述了用于训练字典模型的“数据点初始化”(DPI) 方法，该方法涉及用真实数据点的噪声版本初始化权重矩阵，以提高模型质量。

---

## 59. Agent-o-rama：在Java或Clojure中构建、追踪、评估和监控LLM代理

**原文标题**: Agent-o-rama: build, trace, evaluate, and monitor LLM agents in Java or Clojure

**原文链接**: [https://blog.redplanetlabs.com/2025/11/03/introducing-agent-o-rama-build-trace-evaluate-and-monitor-stateful-llm-agents-in-java-or-clojure/](https://blog.redplanetlabs.com/2025/11/03/introducing-agent-o-rama-build-trace-evaluate-and-monitor-stateful-llm-agents-in-java-or-clojure/)

Agent-o-rama 是一个新的开源库，用于在 JVM (Java 虚拟机) 上构建可扩展、有状态的 LLM 代理。它提供具有特性对等的 Java 和 Clojure API，旨在弥合目前主要集中在 Python 的 AI 工具方面的差距。该库借鉴了 LangGraph 和 LangSmith 的思想，例如结构化代理图、追踪、数据集、实验和评估，但它是 Java 和 Clojure 原生的。

Agent-o-rama 的核心优势在于促进对基于 LLM 的应用程序进行严格的测试和监控，以提高有用性、性能并最大限度地减少幻觉。代理被定义为并行执行的 Java 或 Clojure 函数图。该库捕获详细的追踪信息，并提供一个 Web UI 用于实验、评估和遥测。它支持流式传输，并通过与集群平台 Rama 的集成提供可扩展性。

与托管解决方案不同，Agent-o-rama 将所有数据和追踪信息保留在您的基础设施中，并与各种工具（如数据库和 API）集成。本文提供了一个研究代理的示例，演示了如何在本地运行它并将其部署到 Rama 集群。主要功能包括自动追踪模型调用以及添加自定义追踪信息的能力。Agent-o-rama 管理存储和部署，并提供一个 UI 来与代理交互和查看追踪信息。Rama 对于小型集群可以免费使用，并可进行商业扩展。

---

## 60. 罗伯特·胡克致戈特弗里德·莱布尼茨的“赛博朋克”信

**原文标题**: Robert Hooke's "Cyberpunk” Letter to Gottfried Leibniz

**原文链接**: [https://mynamelowercase.com/blog/robert-hookes-cyberpunk-letter-to-gottfried-leibniz/](https://mynamelowercase.com/blog/robert-hookes-cyberpunk-letter-to-gottfried-leibniz/)

本文认为，罗伯特·胡克，通常因其在弹簧领域的研究以及与艾萨克·牛顿的冲突而闻名，应被视为“赛博朋克的守护神”，因为他早期就拥抱了与该类型相似的理念。作者着重分析了胡克在 1681 年写给戈特弗里德·莱布尼茨的一封信，信中表达了对莱布尼茨“通用语言”的热情，这种通用语言旨在将科学推理机械化。

作者将莱布尼茨的项目与现代计算机编程语言进行了比较，并指出诺伯特·维纳将莱布尼茨描述为“控制论的守护神”，而“赛博朋克”正是源于控制论。然而，作者认为胡克的信不仅仅是控制论，它还展现了一种赛博朋克的敏感性，设想了这种早期编程语言如何赋予个人自由表达、探索和测试思想的能力，从而规避审查和来自不公正权威的干预。

作者指出胡克具有政治色彩的背景、亲身实践的科学方法以及与权威的冲突，作为他反主流文化心态的证据。文章认为，胡克预见到了控制论系统赋予个人自由的潜力，这是赛博朋克的一个关键主题。作者还提到了在皇家学会档案馆发现这封信的过程，以及转录胡克手稿的困难，并提供了一个部分转录的摘录。这篇文章在 Hacker News 上引起了关注，一位用户提供了完整的转录。

---

## 61. Pixi：机器人技术的可复现包管理

**原文标题**: Pixi: Reproducible Package Management for Robotics

**原文链接**: [https://prefix.dev/blog/reproducible-package-management-for-robotics](https://prefix.dev/blog/reproducible-package-management-for-robotics)

本文介绍Pixi，一种现代、跨平台的软件包管理器，旨在简化和提高ROS（机器人操作系统）开发环境的可复现性。它解决了Ubuntu锁定、发行版耦合、全局安装、多发行版维护以及Docker开销等长期困扰ROS开发的问题。

Pixi构建于Conda生态系统之上，允许开发者在Linux、macOS和Windows上安装ROS，无需Docker或Ubuntu。它创建具有精确依赖项的隔离环境，从而可以在单台机器上并行管理多个ROS发行版。环境可以通过`pixi.toml`文件轻松共享，确保团队和CI/CD管道的一致设置。

本文通过与基于APT的系统的比较，突出了Pixi的优势，展示了其卓越的跨平台支持、可复现性、多发行版处理以及更简便的CI/CD集成。它提供了一个快速入门指南，展示了如何初始化ROS环境和添加软件包。它还涵盖了高级用例，例如在同一工作空间中管理多个发行版、集成CUDA以及利用`package.xml`文件进行依赖项管理。

Pixi有助于在CI中针对多个ROS版本和平台进行测试，甚至可以在需要时与Docker无缝集成。作者鼓励社区参与扩展RoboStack软件包并为conda-forge做出贡献，强调使Pixi成为ROS社区的标准工具的目标。总体目标是使机器人开发者能够专注于机器人开发，而不是与软件包管理问题作斗争。

---

## 62. Oxy是Cloudflare基于Rust的下一代代理框架（2023）

**原文标题**: Oxy is Cloudflare's Rust-based next generation proxy framework (2023)

**原文链接**: [https://blog.cloudflare.com/introducing-oxy/](https://blog.cloudflare.com/introducing-oxy/)

Oxy：Cloudflare的下一代Rust代理框架，专为高负载、可定制的流量管理而设计。它被用于诸如Zero Trust Gateway和iCloud Private Relay等项目中，提供了一个功能丰富的代理服务器，与Cloudflare的基础设施紧密集成。Oxy允许对协议解封装、流量分析和路由等方面进行编程控制，使工程师能够调整每个组件以满足特定的应用需求。

其主要特性包括多功能的入口（HTTP、TCP、UDP、IP）和出口（HTTP、UDP、TCP、IP），具有内部DNS解析和地理出口选项。Oxy支持从L3到L7的多层流量处理，允许应用程序强制解封装并在不同级别分析流量。它处理TCP、UDP、QUIC和IP的状态隧道，并提供对HTTP请求和响应的完全控制，包括CONNECT-UDP和CONNECT-IP等高级隧道方法。

安全性至关重要，其密码学和TLS基于BoringSSL，提供符合FIPS标准和最新版本，并可选择动态切换。Oxy还提供全面的监控和分析功能，包括panic报告、Prometheus指标、Kibana日志和审计日志。

通过YAML配置文件和Rust代码钩子实现可扩展性，允许开发者自定义几乎所有流量处理方面。Rust的安全性与性能，结合使用hyper和tokio等开源依赖项，使Oxy成为构建高级网络应用的强大而高效的平台。

---

## 63. Google Cloud因三个不同原因三次暂停客户账户。

**原文标题**: Google Cloud suspended customer's account 3 times, for 3 different reasons

**原文链接**: [https://www.theregister.com/2025/11/04/google_cloud_suspended_customers_account/](https://www.theregister.com/2025/11/04/google_cloud_suspended_customers_account/)

SSLMate创始人Andrew Ayer因不同原因经历了三次Google Cloud账号停用，导致他对该平台生产环境工作负载的可靠性产生质疑。

SSLMate主要使用Google Cloud进行测试、实验，以及通过创建服务账号代表客户访问Cloud DNS和Cloud Domains来集成客户的Google Cloud账号。这种方法基于Google自己的文档，涉及模拟服务账号。

第一次停用发生在2024年5月，理由是违反政策，但Google没有提供关于原因或如何防止未来发生的明确信息。不久之后，又因另一个未指明的原因发生了第二次停用。最近又发生了一次停用，这次是因为违反服务条款，最终在Ayer在社交媒体上发帖后得到解决。尽管发生了停用，但一个客户集成仍然可以工作。

Ayer对缺乏透明度和对业务的影响感到沮丧。他提出了一个使用OpenID Connect（OIDC）的潜在解决方案，但发现实现过程过于复杂。他得出结论，Google的系统不可靠，并且难以摆脱长期有效的凭据。Ayer现在计划放弃Google Cloud用于生产用例。

---

## 64. 更硬、更好、更快、更强 - Rust 版 Uber H3

**原文标题**: Harder, Better, Faster, Stronger Version of Uber H3 in Rust

**原文链接**: [https://grim7reaper.github.io/blog/2023/01/09/the-hydronium-project/](https://grim7reaper.github.io/blog/2023/01/09/the-hydronium-project/)

本文介绍了 h3o，它是 Uber 的 H3 地理空间索引库的完全重写版本，使用 Rust 编写，旨在实现更轻松的集成、更安全的 API、与原始版本相当或更高的性能，以及对 H3 4.0 API 的全面覆盖。

为了确保正确性并防止回归，进行了广泛的测试，包括差异测试、集成测试、单元测试和模糊测试。一个包含 911 个测试用例的基准测试套件将 h3o 与 H3 进行了比较，结果表明 h3o 在许多领域都获得了显著的性能提升。虽然 H3 在少数特定情况下仍然更快（尤其是在粗略分辨率和某些 cellToLatLng 计算中），但 h3o 在许多场景中明显优于 H3，尤其是在涉及计算密集型任务的场景中，例如 `gridDiskDistancesSafe`、`h3SetToLinkedGeo`、`isPentagon`、`isValidCell`、`stringToH3` 和 `polygonToCells`。这些改进归功于算法优化，例如通过位操作实现的常数时间运算、优化的哈希表使用、用迭代实现代替递归，以及支持预付费计算成本的特殊几何类型。

文章还重点介绍了 “h3oh3o”，它是 h3o 的 C API 绑定，使已经使用原始 H3 库的项目更容易采用该库。基准测试表明，h3oh3o 保持了 h3o 相对于 H3 的性能优势。文章最后指出，作者的目标是与 H3 实现同等功能，但 h3oh3o 可能会检测到更多错误，返回不同的错误代码，或者干脆返回一个合理的默认值而不是错误。

---

## 65. 亚马逊对使用其市场API收取费用

**原文标题**: Amazon imposing fees on using their marketplace API

**原文链接**: [https://developer.amazonservices.com/spp-announcement](https://developer.amazonservices.com/spp-announcement)

亚马逊现要求其销售伙伴API (SP-API) 用户提供付款和税务信息以维持访问权限。此举通过解决方案提供商门户实施，用户必须提交其首选收费方式、账单地址和任何适用的税务信息。完成此步骤是激活SP-API订阅并避免API访问中断的强制性要求。本质上，依赖SP-API进行市场运营的用户现在将面临费用，并且需要配置其账单详细信息才能继续不间断地使用该服务。

---

## 66. 我们为什么从Python迁移到Node.js

**原文标题**: Why we migrated from Python to Node.js

**原文链接**: [https://blog.yakkomajuri.com/blog/python-to-node](https://blog.yakkomajuri.com/blog/python-to-node)

Skald在推出RAG API平台一周后，将其后端从Python (Django) 重写为 Node.js (Express + MikroORM)，主要原因是他们遇到了Python异步功能的复杂性和局限性。

作者是一位Django爱好者，他发现Python的异步实现困难、不直观，并且缺乏对异步文件I/O等关键功能的原生支持。 Django的ORM也缺乏完整的异步支持，需要变通方法。 这导致代码混乱，并引发了对可扩展性和可维护性的担忧。

他们考虑过FastAPI，一个具有更好异步支持的Python框架，但最终选择了Node.js来统一他们的代码库，因为他们的后台工作程序已经用Node编写。

迁移带来了约3倍的开箱即用吞吐量提升，并为更多的并发处理提供了机会。 虽然他们怀念Django的功能，特别是它的ORM，但他们对MikroORM感到满意。 统一的Node.js代码库使他们能够消除重复的逻辑并改进测试。

迁移花了三天时间，几乎没有使用AI代码生成。 作者对这个决定表示满意，并邀请大家对他们的开源项目提出反馈和贡献。

---

## 67. 为什么工程师不能理性看待编程语言

**原文标题**: Why engineers can't be rational about programming languages

**原文链接**: [https://spf13.com/p/the-hidden-conversation/](https://spf13.com/p/the-hidden-conversation/)

公司编程语言的选择常常是出于身份认同、情感和自我，而非理性的技术分析，这导致了巨大的隐性成本并阻碍了业务成功。作者通过个人经历，包括一家初创公司灾难性的Perl迁移和见证一个有缺陷的Rust采纳决策，来说明这一点。

核心论点是，语言讨论涉及两个层面：一个可见的技术辩论和一个围绕程序员身份认同和个人偏好的不可见对话。神经科学研究支持这一点，证明挑战基于身份认同的信念会在大脑中引发威胁反应，从而使客观评估变得困难。

作者批评了行业对可见技术辩论的关注，认为工程师们经常无意识地捍卫自己偏爱的语言，并且雇用具有特定语言专业知识的人员会预先决定语言的选择。文章断言，这些由身份驱动的决策通过增加技术债务和降低开发速度，会使开发成本膨胀（占总成本的40-60%）。

作者提出了一种视角的转变，敦促公司将语言选择视为经济决策，而不是技术或情感决策。他们提倡一种新的框架，该框架可以量化语言的真实成本，包括工资、开发速度、技术债务、招聘难度和运营复杂性等因素。下一篇文章将详细介绍这个“语言真实成本的9个因素”框架。

---

## 68. Win11Debloat – declutter and improve your Windows experience

**原文标题**: Win11Debloat – declutter and improve your Windows experience

**原文链接**: [https://github.com/Raphire/Win11Debloat](https://github.com/Raphire/Win11Debloat)

生成摘要时出错

---

## 69. Measuring characteristics of TCP connections at Internet scale

**原文标题**: Measuring characteristics of TCP connections at Internet scale

**原文链接**: [https://blog.cloudflare.com/measuring-network-connections-at-scale/](https://blog.cloudflare.com/measuring-network-connections-at-scale/)

生成摘要时出错

---

## 70. The Continual Learning Problem

**原文标题**: The Continual Learning Problem

**原文链接**: [https://jessylin.com/2025/10/20/continual-learning/](https://jessylin.com/2025/10/20/continual-learning/)

生成摘要时出错

---

## 71. Show HN: a Rust ray tracer that runs on any GPU – even in the browser

**原文标题**: Show HN: a Rust ray tracer that runs on any GPU – even in the browser

**原文链接**: [https://github.com/tchauffi/rust-rasterizer](https://github.com/tchauffi/rust-rasterizer)

生成摘要时出错

---

## 72. </> Htmx – The Fetch()ening

**原文标题**: </> Htmx – The Fetch()ening

**原文链接**: [https://htmx.org/essays/the-fetchening/](https://htmx.org/essays/the-fetchening/)

生成摘要时出错

---

## 73. FreakWAN: A floor-routing WAN implementing a chat over bare-LoRa (no LoRaWAN)

**原文标题**: FreakWAN: A floor-routing WAN implementing a chat over bare-LoRa (no LoRaWAN)

**原文链接**: [https://github.com/antirez/freakwan](https://github.com/antirez/freakwan)

生成摘要时出错

---

## 74. Draw high dimensional tensors as a matrix of matrices

**原文标题**: Draw high dimensional tensors as a matrix of matrices

**原文链接**: [https://blog.ezyang.com/2025/10/draw-high-dimensional-tensors-as-a-matrix-of-matrices/](https://blog.ezyang.com/2025/10/draw-high-dimensional-tensors-as-a-matrix-of-matrices/)

生成摘要时出错

---

## 75. The Arduino Uno Q is a weird hybrid SBC

**原文标题**: The Arduino Uno Q is a weird hybrid SBC

**原文链接**: [https://www.jeffgeerling.com/blog/2025/arduino-uno-q-weird-hybrid-sbc](https://www.jeffgeerling.com/blog/2025/arduino-uno-q-weird-hybrid-sbc)

生成摘要时出错

---

## 76. The Morals of Chess (1786)

**原文标题**: The Morals of Chess (1786)

**原文链接**: [https://americanliterature.com/author/benjamin-franklin/essay/the-morals-of-chess](https://americanliterature.com/author/benjamin-franklin/essay/the-morals-of-chess)

生成摘要时出错

---

## 77. Why AC is cheap, but AC repair is a luxury

**原文标题**: Why AC is cheap, but AC repair is a luxury

**原文链接**: [https://a16z.substack.com/p/why-ac-is-cheap-but-ac-repair-is](https://a16z.substack.com/p/why-ac-is-cheap-but-ac-repair-is)

生成摘要时出错

---

## 78. Show HN: Tamagotchi P1 for FPGAs

**原文标题**: Show HN: Tamagotchi P1 for FPGAs

**原文链接**: [https://github.com/agg23/fpga-tamagotchi](https://github.com/agg23/fpga-tamagotchi)

生成摘要时出错

---

## 79. Handwriting Programs in J (2017)

**原文标题**: Handwriting Programs in J (2017)

**原文链接**: [https://www.hillelwayne.com/handwriting-j/](https://www.hillelwayne.com/handwriting-j/)

生成摘要时出错

---

## 80. New prompt injection papers: Agents rule of two and the attacker moves second

**原文标题**: New prompt injection papers: Agents rule of two and the attacker moves second

**原文链接**: [https://simonwillison.net/2025/Nov/2/new-prompt-injection-papers/](https://simonwillison.net/2025/Nov/2/new-prompt-injection-papers/)

生成摘要时出错

---

## 81. OpenAI signs $38B cloud computing deal with Amazon

**原文标题**: OpenAI signs $38B cloud computing deal with Amazon

**原文链接**: [https://www.nytimes.com/2025/11/03/technology/openai-amazon-cloud-computing.html](https://www.nytimes.com/2025/11/03/technology/openai-amazon-cloud-computing.html)

生成摘要时出错

---

## 82. R interface to Apple's MLX library

**原文标题**: R interface to Apple's MLX library

**原文链接**: [https://hughjonesd.github.io/Rmlx/index.html](https://hughjonesd.github.io/Rmlx/index.html)

生成摘要时出错

---

## 83. A collection of links that existed about Anguilla as of 2003

**原文标题**: A collection of links that existed about Anguilla as of 2003

**原文链接**: [https://web.ai/](https://web.ai/)

生成摘要时出错

---

## 84. Searles's Chinese Room: Case study in philosophy of mind and cognitive science

**原文标题**: Searles's Chinese Room: Case study in philosophy of mind and cognitive science

**原文链接**: [https://cse.buffalo.edu/~rapaport/Papers/Papers.by.Others/reingold-on-searle.html](https://cse.buffalo.edu/~rapaport/Papers/Papers.by.Others/reingold-on-searle.html)

生成摘要时出错

---

## 85. When models manipulate manifolds: The geometry of a counting task

**原文标题**: When models manipulate manifolds: The geometry of a counting task

**原文链接**: [https://transformer-circuits.pub/2025/linebreaks/index.html](https://transformer-circuits.pub/2025/linebreaks/index.html)

生成摘要时出错

---

## 86. When models manipulate manifolds: The geometry of a counting task

**原文标题**: When models manipulate manifolds: The geometry of a counting task

**原文链接**: [https://transformer-circuits.pub/2025/linebreaks/index.html](https://transformer-circuits.pub/2025/linebreaks/index.html)

生成摘要时出错

---

## 87. How the Mayans were able to accurately predict solar eclipses for centuries

**原文标题**: How the Mayans were able to accurately predict solar eclipses for centuries

**原文链接**: [https://phys.org/news/2025-10-mayans-accurately-solar-eclipses-centuries.html](https://phys.org/news/2025-10-mayans-accurately-solar-eclipses-centuries.html)

生成摘要时出错

---

## 88. Israels top military lawyer arrested after she admitted leaking video of abuse

**原文标题**: Israels top military lawyer arrested after she admitted leaking video of abuse

**原文链接**: [https://www.theguardian.com/world/2025/nov/03/israels-top-military-lawyer-arrested-after-she-admitted-leaking-video-of-soldiers-abuse](https://www.theguardian.com/world/2025/nov/03/israels-top-military-lawyer-arrested-after-she-admitted-leaking-video-of-soldiers-abuse)

生成摘要时出错

---

## 89. No Socials November

**原文标题**: No Socials November

**原文链接**: [https://bjhess.com/posts/no-socials-november](https://bjhess.com/posts/no-socials-november)

生成摘要时出错

---

## 90. Paris had a moving sidewalk in 1900, and a Thomas Edison film captured it (2020)

**原文标题**: Paris had a moving sidewalk in 1900, and a Thomas Edison film captured it (2020)

**原文链接**: [https://www.openculture.com/2020/03/paris-had-a-moving-sidewalk-in-1900.html](https://www.openculture.com/2020/03/paris-had-a-moving-sidewalk-in-1900.html)

生成摘要时出错

---

## 91. Offline Math: Converting LaTeX to SVG with MathJax

**原文标题**: Offline Math: Converting LaTeX to SVG with MathJax

**原文链接**: [https://sigwait.org/~alex/blog/2025/10/07/3t8acq.html](https://sigwait.org/~alex/blog/2025/10/07/3t8acq.html)

生成摘要时出错

---

## 92. OSS Alternative to Open WebUI – ChatGPT-Like UI, API and CLI

**原文标题**: OSS Alternative to Open WebUI – ChatGPT-Like UI, API and CLI

**原文链接**: [https://github.com/ServiceStack/llms](https://github.com/ServiceStack/llms)

生成摘要时出错

---

## 93. Is Your Bluetooth Chip Leaking Secrets via RF Signals?

**原文标题**: Is Your Bluetooth Chip Leaking Secrets via RF Signals?

**原文链接**: [https://www.semanticscholar.org/paper/Is-Your-Bluetooth-Chip-Leaking-Secrets-via-RF-Ji-Dubrova/c1d3ceb47ea6f9cc4f29929e2f97d36862a260a2](https://www.semanticscholar.org/paper/Is-Your-Bluetooth-Chip-Leaking-Secrets-via-RF-Ji-Dubrova/c1d3ceb47ea6f9cc4f29929e2f97d36862a260a2)

生成摘要时出错

---

## 94. ECL Runs Maxima in a Browser

**原文标题**: ECL Runs Maxima in a Browser

**原文链接**: [https://mailman3.common-lisp.net/hyperkitty/list/ecl-devel@common-lisp.net/thread/T64S5EMVV6WHDPKWZ3AQHEPO3EQE2K5M/](https://mailman3.common-lisp.net/hyperkitty/list/ecl-devel@common-lisp.net/thread/T64S5EMVV6WHDPKWZ3AQHEPO3EQE2K5M/)

生成摘要时出错

---

## 95. The Nonprofit Feeding the Internet to AI Companies

**原文标题**: The Nonprofit Feeding the Internet to AI Companies

**原文链接**: [https://www.theatlantic.com/technology/2025/11/common-crawl-ai-training-data/684567/](https://www.theatlantic.com/technology/2025/11/common-crawl-ai-training-data/684567/)

生成摘要时出错

---

## 96. Python Steering Council unanimously accepts "PEP 810, Explicit lazy imports"

**原文标题**: Python Steering Council unanimously accepts "PEP 810, Explicit lazy imports"

**原文链接**: [https://discuss.python.org/t/pep-810-explicit-lazy-imports/104131?page=23](https://discuss.python.org/t/pep-810-explicit-lazy-imports/104131?page=23)

生成摘要时出错

---

## 97. Using FreeBSD to make self-hosting fun again

**原文标题**: Using FreeBSD to make self-hosting fun again

**原文链接**: [https://jsteuernagel.de/posts/using-freebsd-to-make-self-hosting-fun-again/](https://jsteuernagel.de/posts/using-freebsd-to-make-self-hosting-fun-again/)

生成摘要时出错

---

## 98. S1130 – IBM 1130 Emulator in C#

**原文标题**: S1130 – IBM 1130 Emulator in C#

**原文链接**: [https://github.com/semuhphor/S1130/tree/feature/web-frontend](https://github.com/semuhphor/S1130/tree/feature/web-frontend)

生成摘要时出错

---

## 99. Syllabi – Open-source agentic AI with tools, RAG, and multi-channel deploy

**原文标题**: Syllabi – Open-source agentic AI with tools, RAG, and multi-channel deploy

**原文链接**: [https://www.syllabi-ai.com/](https://www.syllabi-ai.com/)

生成摘要时出错

---

## 100. Writing FreeDOS Programs in C

**原文标题**: Writing FreeDOS Programs in C

**原文链接**: [https://www.freedos.org/books/cprogramming/](https://www.freedos.org/books/cprogramming/)

生成摘要时出错

---

