# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-11-04.md)

*最后自动更新时间: 2025-11-04 17:48:36*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 2 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 3 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 4 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 5 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 6 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 7 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 8 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 9 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 10 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 11 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 12 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 13 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 14 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 15 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 16 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 17 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 18 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 19 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 20 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 21 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 22 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 23 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 24 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 25 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 26 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 27 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 28 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 29 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 30 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 31 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 32 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 33 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 34 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 35 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 36 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 37 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 38 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 39 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 40 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 41 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 42 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 43 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 44 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 45 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 46 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 47 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 48 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 49 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 50 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 51 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 52 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 53 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 54 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 55 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 56 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 57 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 58 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 59 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 60 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 61 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 62 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 63 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 64 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 65 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 66 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 67 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 68 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 69 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 70 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 71 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 72 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 73 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 74 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 75 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 76 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 77 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 78 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 79 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 80 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 81 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 82 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 83 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 84 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 85 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 86 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 87 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 88 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 89 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 90 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 91 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 92 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 93 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 94 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 95 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 96 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 97 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 98 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 99 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 100 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 101 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 102 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 103 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 104 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 105 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 106 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 107 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 108 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 109 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 110 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 111 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 112 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 113 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 114 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 115 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 116 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 117 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 118 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 119 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 120 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 121 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 122 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 123 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 124 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 125 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 126 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 127 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 128 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 129 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 130 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 131 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 132 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 133 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 134 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 135 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 136 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 137 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 138 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 139 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 140 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 141 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 142 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 143 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 144 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 145 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 146 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 147 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 148 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 149 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 150 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 151 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 152 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 153 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 154 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 155 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 156 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 157 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 158 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 159 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 160 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 161 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 162 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 163 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 164 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 165 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 166 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 167 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 168 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 169 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 170 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 171 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 172 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 173 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 174 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 175 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 176 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 177 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 178 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 179 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 180 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 181 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 182 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 183 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 184 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 185 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 186 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 187 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 188 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 189 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 190 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 191 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 192 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 193 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 194 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 195 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 196 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 197 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 198 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 199 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 200 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 201 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 202 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 203 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 204 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 205 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 206 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 207 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 208 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 209 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 210 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 211 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 212 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 213 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 214 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 215 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 216 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 217 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 218 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 219 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 220 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 221 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 222 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 223 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 224 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 225 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 226 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 227 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 228 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 229 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
