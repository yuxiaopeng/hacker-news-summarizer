# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-10-13.md)

*最后自动更新时间: 2025-10-13 17:50:38*
## 1. 环境变量是个历史遗留的烂摊子：让我们深入了解一下

**原文标题**: Environment variables are a legacy mess: Let's dive deep into them

**原文链接**: [https://allvpv.org/haotic-journey-through-envvars/](https://allvpv.org/haotic-journey-through-envvars/)

Przemysław Kusiak 的文章深入探讨了常常被忽视的环境变量（envvars）领域，揭示了它们的历史遗留特性和怪癖。他解释说，在 Linux 中，环境变量通过 `execve` 系统调用从父进程传递到子进程。该调用接受可执行文件路径、命令行参数和一个环境变量数组作为参数。

虽然大多数工具会继承环境变量，但有些工具（如 `login` 可执行文件）会创建全新的环境。内核将环境变量作为以 null 结尾的字符串转储到堆栈中，然后程序将其复制到自己的数据结构中。文章重点介绍了不同语言如何内部处理环境变量，重点介绍了 Bash（使用带有本地作用域和导出特性的哈希映射堆栈）、glibc（具有线性复杂度的 `getenv` 和 `putenv` 的动态数组）和 Python（与 C 库耦合，可能导致 `os.environ` 和实际环境之间的不一致）。

Kusiak 还介绍了内核允许的宽松格式，这可能导致诸如名称重复和没有等号的条目等问题。他解释了单个变量的大小限制（128 KiB）和总环境的大小限制（2 MiB）。他驳斥了 POSIX 强制要求大写环境变量的误解，澄清说它只是建议标准实用程序使用大写，并为应用程序保留小写名称。他建议使用带下划线的大写字母作为名称，并使用 UTF-8 作为值，以获得广泛的兼容性，但建议坚持使用可移植字符集以获得最大的安全性。他最后呼吁使用 RSS 进行独立博客写作。

---

## 2. Show HN: SQLite Online – 11年独立开发，日活用户1.1万

**原文标题**: Show HN: SQLite Online – 11 years of solo development, 11K daily users

**原文链接**: [https://sqliteonline.com/](https://sqliteonline.com/)

SQLite Online 是一个独立开发的基于网络的 SQLite 编辑器，拥有 11 年的开发历史和 11,000 名日活跃用户。它提供导入、导出和运行功能，以及语法高亮、表格视图、历史记录和数据科学图表功能。图表功能使用自定义查询语言，在 `SELECT` 前加上 `QLINE-`、`QAREA-`、`QBAR-`、`QPIE-` 和 `QBUBBLE-`，以实现数据的可视化表示。它利用了各种开源库，包括 Sql.js、DuckDB、PGLite、Font-Awesome、CodeMirror、Toastify 和 Chart.js。

该平台不断更新，详细的历史记录日志展示了随着时间的推移添加的功能，包括 DuckDB 和 PGLite 集成、虚拟表联合、改进的图表解析器和导出、Ai 帮助、XLSX 导出、OpFS 支持、云保存链接、定期 SQLite WASM 迁移、删除查询大小限制、添加 regexp 函数、改进的 UI/UX、颜色主题、SQLite 服务器共享、Docker 版本、智能导入等等。

用户可以配置设置，例如存储类型（内存、IndexDB、OpFS）、左侧菜单行为、编辑器首选项（自动完成、错误突出显示、AI 建议）、UI 皮肤、表格外观（悬停效果、数字格式）和旧按钮面板可见性。

该平台按“原样”提供，包含一般免责声明，并强调用户对上传内容以及遵守数据隐私的责任。

---

## 3. NanoChat - 100美元能买到的最佳ChatGPT

**原文标题**: NanoChat – The best ChatGPT that $100 can buy

**原文链接**: [https://github.com/karpathy/nanochat](https://github.com/karpathy/nanochat)

NanoChat：一个极简的全栈类ChatGPT大语言模型，旨在单台8XH100节点上以约100美元的成本运行。`speedrun.sh`脚本自动化整个流程，包括分词、预训练、微调、评估、推理和网络服务。大约4小时后，用户可以通过简单的Web界面与他们自己的大语言模型交互。

该项目旨在使大语言模型更易于访问，强调简洁性、可读性和可破解性，而不是详尽的配置。虽然100美元的预算只能产生一个基础模型，但该项目建议扩展到约300美元或1000美元，以获得更好的性能，与GPT-2相当。这可以通过下载更多数据并减少设备批量大小来管理内存来实现。

该存储库鼓励用户向代码库提问，可以通过将文件打包到大语言模型的提示中或使用DeepWiki来实现。对NanoChat的贡献侧重于改进在有限预算下可访问的微型模型，同时保持代码的最小化和易于理解。该项目受到nanoGPT和modded-nanoGPT的启发，并感谢HuggingFace、Lambda和Alec Radford的贡献。

---

## 4. JSON 河流 - 增量解析流式JSON数据

**原文标题**: JSON River – Parse JSON incrementally as it streams in

**原文链接**: [https://github.com/rictic/jsonriver](https://github.com/rictic/jsonriver)

`jsonriver` 是一个轻量级的 JavaScript 库，用于在 JSON 数据流式传输时对其进行增量解析，从而提供一系列逐渐完整的数值。这允许从网络请求或语言模型等来源处理 JSON，而无需等待整个文档加载完成。

主要特点：

*   **增量解析：** 提供 JSON 值的流，展示 JSON 对象在解析过程中的演变。
*   **轻量快速：** 体积小，无依赖，并利用标准 JavaScript 功能。它专为广泛的兼容性而设计。
*   **正确性：** 保证最终解析的值与 `JSON.parse` 的输出一致。经过广泛的测试，确保符合 JSONTestSuite 标准。
*   **不变性：** 在整个增量更新过程中保持数据类型的一致性，确保可预测的行为。数组会被追加或修改最后一个元素，对象会被添加或修改最近的属性。
*   **应用场景：** 在解析来自网络请求或语言模型等来源的数据流时非常有用。

虽然 `JSON.parse` 在处理完整的 JSON 字符串时速度更快，而 `stream-json` 提供了更多的功能，但 `jsonriver` 在速度和增量处理能力之间取得了平衡，使其适用于需要实时更新或对大型 JSON 文档进行内存高效解析的应用程序。

---

## 5. 聚焦pdfly：PDF文件的瑞士军刀

**原文标题**: Spotlight on pdfly, the Swiss Army knife for PDF files

**原文链接**: [https://chezsoi.org/lucas/blog/spotlight-on-pdfly.html](https://chezsoi.org/lucas/blog/spotlight-on-pdfly.html)

本文介绍pdfly，一个用Python编写的命令行工具，基于fpdf2 & pypdf库，用于处理PDF文件。pdfly由Lucas Cimon维护，提供一系列功能，堪称PDF任务的“瑞士军刀”。它可以显示元数据、合并PDF、删除页面、将图像转换为PDF、压缩文档以及创建小册子。它还包括提取图像和带注释文本的工具。

一个关键特性是`pdfly update-offsets`命令，它通过修复交叉引用表来修复手动编辑的PDF文件。本文宣布发布0.5.0版本，该版本引入了新功能，例如由@moormaster实现的用于签名和验证PDF签名的`pdfly sign`和`pdfly check-sign`。另一项新增功能是由Hal Wine实现的`pdfly extract-annotated-pages`，用于仅提取带有注释的页面。以及Subhajit Sahu实现的`pdfly rotate`，用于旋转特定页面。

本文强调了通过“up-for-grabs”问题进行贡献的机会，并鼓励用户反馈和功能建议，特别是扩展签名功能。目标是使pdfly成为一个更通用和用户友好的PDF文档管理工具。

---

## 6. 2025年 纪念阿尔弗雷德·诺贝尔瑞典国家银行经济学奖

**原文标题**: The Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel 2025

**原文链接**: [https://www.nobelprize.org/prizes/economic-sciences/2025/summary/](https://www.nobelprize.org/prizes/economic-sciences/2025/summary/)

2025年瑞典国家银行纪念阿尔弗雷德·诺贝尔经济学奖授予乔尔·莫基尔、菲利普·阿吉翁和彼得·豪伊特，以表彰他们对理解创新驱动型经济增长所做的贡献。

乔尔·莫基尔因其在识别技术进步推动持续经济增长的必要因素方面的工作而获得一半奖金。他探讨了促进创新的历史和文化条件，强调了思想开放、交流以及支持技术进步的机构的重要性。

菲利普·阿吉翁和彼得·豪伊特因共同发展了关于持续增长的“创造性破坏”理论而共同获得另一半奖金。该理论强调创新不可避免地会扰乱现有产业和技术，从而导致新产业和技术的产生。这种持续的破坏和创造的循环是长期经济繁荣的核心驱动力。

文章导航允许用户访问关于每位获奖者的详细信息，包括摘要、颁奖公告、新闻稿、大众信息和高级信息。它还提供获奖者的视觉呈现。“返回顶部”功能简化了页面内的导航。

---

## 7. Optery (YC W22) – 招聘有Node.js经验的技术主管（美国及拉丁美洲）

**原文标题**: Optery (YC W22) – Hiring Tech Lead with Node.js Experience (U.S. & Latin America)

**原文链接**: [https://www.optery.com/careers/](https://www.optery.com/careers/)

Optery (YC W22 孵化公司) 正在招聘一位具有 Node.js 经验的技术主管。 该职位面向美国和拉丁美洲的候选人开放。 这是关于 Optery 潜在工作机会的关键信息。 文章可能包含关于公司、职位职责、所需技能和福利的更多细节，但这些信息未包含在提供的文本中。

---

## 8. 最近学到的一些家庭实验室零碎知识

**原文标题**: More random home lab things I've recently learned

**原文链接**: [https://chollinger.com/blog/2025/10/more-homelab-things-ive-recently-learned/](https://chollinger.com/blog/2025/10/more-homelab-things-ive-recently-learned/)

本文详细介绍了作者最近在家用实验室中的经验和学习，该实验室包含 Proxmox、TrueNAS、Raspberry Pi 以及各种网络组件。他们遇到了一些问题，并分享了他们发现的解决方案。

首先，用作 Proxmox 节点的 Raspberry Pi 5 由于 SD 卡故障而出现严重减速。作者发现 Pi 5 支持通过适配器使用 NVMe SSD，从而显著提升性能。但是，在 SSD 上安装操作系统需要一种解决方法，即修改 Raspberry Pi OS 以启用 PCI-E。

接下来，Pi 5 上的 Proxmox 经历了虚拟机意外的 OOM（内存不足）终止，通过显式设置内核页面大小解决了该问题。他们还指出，ARM 虚拟机需要 OVMF (UEFI) BIOS 才能正常工作。一个有用的技巧是使用 `kpartx` 来挂载 QEMU 虚拟机磁盘以进行调试。

此外，当 ZFS 卷已满时，作者遇到了 Proxmox Backup Server (PBS) 的死锁问题。解决方案是删除 ZFS 快照以释放空间，防止垃圾回收失败。设置了配额以防止将来发生这种情况。

其他见解包括作者找到并使用了 CyberPower UPS 管理软件，在使用 Davis 进行 CALDAV 服务器托管方面获得了积极的体验，以及热衷于使用 Mealie 进行食谱管理，包括贡献了一个小型 PR。他们提倡使用 Mealie 而不是典型的食谱博客，赞扬其结构化格式和组织。

---

## 9. 美国太阳能农场

**原文标题**: American solar farms

**原文链接**: [https://tech.marksblogg.com/american-solar-farms.html](https://tech.marksblogg.com/american-solar-farms.html)

本文详细介绍了美国地面安装太阳能（GM-SEUS）数据集的创建和探索，该数据集全面收集了美国本土48州和哥伦比亚特区公用事业和商业级太阳能发电场的数据。该数据集由来自NOAA、NASA和USGS的研究人员创建，分为阵列和面板两部分。

作者描述了用于分析的强大工作站，包括其CPU、RAM、SSD和操作系统。然后，他们概述了安装必要先决条件的过程，如GDAL和DuckDB以及用于空间和数据操作的各种扩展。

文章的核心集中在使用DuckDB对GM-SEUS数据进行清理、转换和优化。这包括将数据转换为ZStandard压缩的、空间排序的Parquet文件，处理缺失值，以及为每个要素创建几何字段和边界框。作者提供了用于此过程的DuckDB命令。

文章随后探讨了阵列数据集，提供了一个示例记录，总结了每个字段的数据类型和统计信息，并使用H3地理空间索引和ArcGIS Pro生成了资产位置的热图。分析还考察了数据来源、安装年份、安装类型、组件类型和阵列容量之间的关系。最后，作者提供了面板数据集的示例记录和数据统计信息。

---

## 10. Linux 的 MPTCP

**原文标题**: MPTCP for Linux

**原文链接**: [https://www.mptcp.dev/](https://www.mptcp.dev/)

MPTCP (多径TCP) 是标准TCP (RFC 8684) 的扩展，允许设备同时使用多个网络接口进行单次连接，从而聚合带宽、优先选择低延迟路径并提供无缝故障转移。与使用单路径的TCP不同，MPTCP在不同的接口上创建多个“子流”（TCP连接）。

主要用例包括网络间的无缝切换（例如智能手机在Wi-Fi和蜂窝网络之间切换）、基于延迟或成本等因素选择最佳网络，以及聚合来自多个网络的带宽以获得更高的吞吐量。

从技术上讲，MPTCP套接字会创建初始子流，并且可以协商更多子流。TCP头中的 `MP_CAPABLE` 选项表示支持MPTCP。如果远程主机不支持MPTCP，则连接会回退到标准TCP。

该系统使用路径管理器来处理子流创建和地址通告（服务器端），并使用数据包调度器根据配置的策略将数据包分发到各个子流。Linux提供内核内（全局应用规则，通过 `ip mptcp` 管理）和用户空间路径管理器（由守护程序（如 `mptcpd`）管理，规则按连接应用）。数据包调度器负责在可用的子流之间分配数据包。

Linux v6.10 支持 IPPROTO_MPTCP 协议、回退到TCP、内核内/用户空间路径管理、套接字选项和调试功能。MPTCP社区维护的项目包括内核开发、mptcpd守护程序以及对诸如iproute2和Network Manager等工具的MPTCP增强功能。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 2 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 3 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 4 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 5 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 6 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 7 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 8 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 9 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 10 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 11 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 12 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 13 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 14 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 15 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 16 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 17 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 18 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 19 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 20 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 21 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 22 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 23 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 24 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 25 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 26 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 27 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 28 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 29 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 30 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 31 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 32 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 33 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 34 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 35 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 36 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 37 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 38 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 39 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 40 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 41 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 42 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 43 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 44 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 45 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 46 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 47 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 48 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 49 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 50 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 51 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 52 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 53 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 54 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 55 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 56 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 57 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 58 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 59 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 60 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 61 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 62 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 63 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 64 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 65 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 66 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 67 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 68 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 69 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 70 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 71 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 72 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 73 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 74 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 75 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 76 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 77 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 78 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 79 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 80 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 81 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 82 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 83 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 84 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 85 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 86 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 87 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 88 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 89 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 90 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 91 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 92 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 93 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 94 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 95 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 96 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 97 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 98 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 99 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 100 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 101 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 102 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 103 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 104 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 105 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 106 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 107 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 108 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 109 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 110 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 111 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 112 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 113 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 114 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 115 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 116 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 117 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 118 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 119 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 120 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 121 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 122 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 123 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 124 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 125 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 126 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 127 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 128 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 129 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 130 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 131 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 132 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 133 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 134 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 135 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 136 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 137 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 138 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 139 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 140 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 141 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 142 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 143 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 144 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 145 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 146 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 147 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 148 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 149 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 150 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 151 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 152 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 153 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 154 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 155 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 156 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 157 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 158 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 159 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 160 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 161 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 162 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 163 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 164 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 165 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 166 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 167 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 168 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 169 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 170 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 171 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 172 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 173 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 174 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 175 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 176 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 177 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 178 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 179 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 180 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 181 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 182 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 183 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 184 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 185 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 186 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 187 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 188 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 189 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 190 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 191 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 192 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 193 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 194 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 195 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 196 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 197 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 198 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 199 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 200 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 201 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 202 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 203 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 204 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 205 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 206 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 207 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 208 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
