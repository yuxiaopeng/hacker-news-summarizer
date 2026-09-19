# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-09-19.md)

*最后自动更新时间: 2026-09-19 19:39:30*
## 1. 一年前，我利用强化学习构建了非自回归决策模型。

**原文标题**: I built non-autoregressive decision models with RL a year ago

**原文链接**: [https://laya.convaiinnovations.com/](https://laya.convaiinnovations.com/)

Laya 是一个开源的“系统 1”决策模型系列，旨在取代缓慢且昂贵的自回归大语言模型，用于处理分类、路由和筛选等反射性任务。Laya 由一位在该领域早于 TypeSafe 的 Jev 等闭源竞争对手一年便开创此方法的作者开发，利用双向编码器和校准决策强化学习 (RLCD) 来提供近乎即时的结构化输出。

核心亮点包括：

*   **性能与速度：** Laya 的单次前向传播延迟仅为 32.8 毫秒，比同类闭源产品快约 8 倍，且通过私有化部署可实现零运行成本。
*   **三种决策基元：** 该模型不生成文本，而是使用 `choice`（多分类）、`score`（序数）和 `noul`（布尔概率）函数。这种架构从物理层面杜绝了幻觉和架构违规。
*   **多语言支持：** 系统包含一个亚毫秒级路由器，可检测 100 多种语言的脚本，自动将查询引导至最有效的专用检查点（例如用于英语的 ModernBERT-large 或用于多语言任务的 mmBERT-base）。
*   **卓越的校准：** Laya 的校准误差 (ECE) 显著低于闭源模型，能够提供反映实际准确率的“真实”概率。
*   **易用性：** 模型权重已在 Apache 2.0 协议下发布于 Hugging Face，并配有专门的 Python SDK（`pip install laya`）和用于微调的专业训练笔记本。

虽然 Laya 针对选项少于 20 个的架构进行了优化，且需要微调以实现最佳零样本性能，但它代表了向高速、可离网且具成本效益的 AI 决策方式的重大转变。

---

## 2. AI生成的海报不必如此糟糕

**原文标题**: AI-generated posters don’t have to be horrible

**原文链接**: [https://john.hartnup.uk/2026/06/07/ai-event-posters.html](https://john.hartnup.uk/2026/06/07/ai-event-posters.html)

文章**《AI生成的海报未必糟糕》**针对人们对“千篇一律”的AI海报——即常用于当地活动的重复、平庸的设计——日益增长的不满进行了探讨。作者认为，这种乏味并非AI本身的局限，而是由于用户接受了默认设置。

为了克服这种“默认感”，作者展示了特定的提示词如何开启更广泛、更高级的审美。核心要点包括：

*   **明确设计流派：** 与其让AI自行选择布局，用户应要求特定的风格，如**包豪斯（Bauhaus）、瑞士风格（Swiss Style）、日式极简主义（Japanese Minimalism）或孟菲斯设计（Memphis Design）**。这将使输出作品从“业余集市”水平提升至类似画廊海报或专业传单的质感。
*   **将AI视为设计顾问：** 如果你不熟悉艺术史，可以要求AI提供一份多样化风格的“菜单”。作者重点推荐了**孔版印刷（Risograph）、粗野主义（Brutalist）和90年代狂欢（90s Rave）审美**等选项，以使海报脱颖而出。
*   **管理上下文：** 作者指出，随着对话的深入，AI可能会根据此前的交互开始自行添加“创意”文本或元素。为了保持设计简洁，通常最好在选定风格后重新开启新对话。
*   **超越平面图像：** 虽然作者主要关注图像生成，但他也建议利用Claude或Gemini等工具生成可编辑的格式（如HTML或SVG）。这允许用户直接操作图层和文本，而不必受限于静态、不可编辑的图像。

最终的核心观点是，尽管目光敏锐的人或许仍能辨认出AI生成的痕迹，但只要用户运用特定的设计词汇，而非依赖通用的提示词，作品就能变得极具视觉冲击力且独具特色。

---

## 3. Btrfs/ZFS/bcachefs 实际工作负载：略过经典基准测试

**原文标题**: Btrfs/ZFS/bcachefs under workloads classic benchmarks skip

**原文链接**: [https://bartosz.fenski.pl/modern-fs-benchmark/](https://bartosz.fenski.pl/modern-fs-benchmark/)

Bartosz Fenski 的文章指出，传统的综合基准测试（如顺序读/写速度）无法准确反映现代写时复制 (CoW) 文件系统的性能。相反，他通过处理元数据密集型的真实工作负载，对 **Btrfs、ZFS 和 bcachefs** 进行了评估。

作者强调，虽然经典的基准测试更青睐 EXT4 等旧式文件系统，但用户选择现代文件系统是为了数据完整性（校验和）、快照和内置 RAID 等功能。该研究重点关注三个主要场景：**软件编译 (GCC)**、**数据库操作 (PostgreSQL)** 和 **软件包管理 (apt)**。

**主要观察结果：**

*   **ZFS：** 依然是最稳定且功能最完备的选择，提供了卓越的数据保护。然而，由于其高资源需求以及源自 Solaris 移植的开销，它在简单任务中通常表现出较高的延迟和较慢的性能。
*   **Btrfs：** 在面向桌面的任务中表现良好，但在沉重的随机写工作负载（如数据库）下性能下降明显。这主要是由其 CoW 特性导致的碎片化造成的，通常需要对特定文件进行手动调优（如使用 `nodatacow`）。
*   **bcachefs：** 这个较新的文件系统表现尤为出色。它弥合了传统文件系统的速度与 ZFS/Btrfs 先进功能集之间的差距，展现了令人印象深刻的效率和低延迟，预示着它将成为 Linux 生态系统中强有力的竞争者。

**结论：**
Fenski 总结道，文件系统的选择应基于特定的功能需求（如原生加密或多设备管理），而非单纯的 MB/s 吞吐量。他强调，虽然 ZFS 是关键数据“最安全”的选择，但对于那些需要 CoW 功能且不希望牺牲性能的用户来说，bcachefs 正被证明是一个高性能且现代的替代方案。

---

## 4. 斯坦福医学院领导的研究发现：人类大脑是两个独立的器官。

**原文标题**: Human brain is two separate organs, Stanford Medicine-led research finds

**原文链接**: [https://med.stanford.edu/news/all-news/2026/09/two-separate-brains.html](https://med.stanford.edu/news/all-news/2026/09/two-separate-brains.html)

由斯坦福医学院领导的最新研究颠覆了长期以来认为人类大脑是一个单一、统一器官的观点。研究表明，大脑实际上由两个不同的器官组成，它们独立进化且源自不同的发育起源。

几十年来，科学家们一直认为单个祖细胞产生了整个大脑。然而，研究人员发现，在原肠胚形成过程中，大脑是由两个互斥的祖细胞群体发育而来的。其中一个表达 *Otx2* 基因的群体形成了前脑和中脑（负责高级思维），而另一个表达 *Gbx2* 基因的群体则形成了后脑或脑干（负责呼吸和心率等基本生存功能）。这两个谱系通过截然不同的 DNA 包装（染色质）被锁定在各自的命运中，这意味着它们在平行轨道上运行，永不重叠。

这一发现解释了为何科学家此前难以在实验室中培养后脑神经元。利用这一新认知，斯坦福团队首次成功诱导人类干细胞转化为功能性后脑运动神经元。这一突破对于研究脊髓性肌萎缩症（SMA）和肌萎缩侧索硬化症（ALS）等影响脑干的毁灭性疾病至关重要。此外，由于后脑包含调节饥饿的回路，该研究也为肥胖研究开辟了新途径。

从进化角度看，这种双重起源模式可追溯至 5.5 亿多年前，并为从斑马鱼到柱头虫等多种物种所共有。研究结果表明，进化将两个古老且独立的神经系统合并到了同一个空间结构中。这项研究标志着神经科学领域的重大转变，为理解大脑发育以及开发针对复杂神经系统疾病的再生疗法提供了全新的框架。

---

## 5. 适用于 ZX Spectrum 的图形化桌面

**原文标题**: A graphical desktop for the ZX Spectrum

**原文链接**: [https://github.com/mindbox77/zxdesk](https://github.com/mindbox77/zxdesk)

**ZX Desk** 是一个专为 48K Sinclair ZX Spectrum 开发的图形桌面环境，完全采用 Z80 汇编语言编写。它在 1982 年的硬件上实现了类似 GEM 的操作体验，具备重叠窗口、下拉菜单、文件管理器以及多种桌面附件（记事本、时钟、日历）。尽管该机器仅搭载 3.5 MHz 的 CPU 且存在属性冲突（attribute-clash）显示限制，该系统仍能在 69,888 个 T 周期的单帧内实现窗口拖动。

该项目的文档侧重于实测数据而非“硬件传闻”。关键技术发现包括：

*   **ULA 争用：** 普遍观点认为屏幕渲染期间的内存访问会导致 50% 的性能损失，但实际测量显示，该成本仅约为 14.7%。
*   **性能瓶颈：** 绘制文本占窗口渲染耗时的 50%，而“填充”仅占 21%。开发者指出，在 Z80 处理器上，针对“每行开销”的优化比提升“每字节吞吐量”更为关键。
*   **中断管理：** 一项重要发现是，Spectrum 发出中断信号的持续时间仅为 32 个 T 周期。如果在该窗口期内禁用了中断（DI），中断将会**丢失**而非推迟。为此，开发者发明了一种名为“欠下最后一次压栈（owing the last push）”的新技术，允许高速屏幕填充程序在使用堆栈指针（SP）的同时保持中断开启，从而防止系统定时失效。

该系统采用自底向上的架构，利用专用设备层、事件队列和内存管理堆。它支持包括 RAM 磁盘和 esxDOS 在内的多种存储后端。作为一项“心血之作”，ZX Desk 既是 Spectrum 上的实用操作系统，也是 Z80 开发者研究内存争用和精确帧时序的详细技术资源。

---

## 6. Tin：Postgres 全文搜索

**原文标题**: Tin: full-text search for Postgres

**原文链接**: [https://planetscale.com/blog/introducing-tin](https://planetscale.com/blog/introducing-tin)

TIN (Text INdex) 是一款新发布的、适用于 Postgres 和 Neki 数据库的通用版 (GA) 全文搜索扩展。TIN 旨在解决 GIN、ParadeDB 和 pg_textsearch 等现有解决方案的局限性，提供了一个快速、可靠且功能丰富的搜索引擎，并与 Postgres 的事务可见性、复制及备份系统原生集成。

**核心特性与性能**
TIN 支持高级搜索功能，包括布尔表达式、短语和跨度查询、模糊匹配以及 BM25 评分排序。在使用 Stack Exchange 等大规模语料库（1.5 亿个文档）的基准测试中，TIN 展现了卓越的性能：
*   **吞吐量：** 在各种工作负载下，TIN 的每秒查询数 (QPS) 是 ParadeDB 和 GIN 的 10 到 57 倍。
*   **延迟：** 其 p99 延迟比竞争对手低多达 26 倍。
*   **并发性：** 不同于在高负载下会停滞或显著变慢的其他扩展，TIN 即使在密集的并发更新（如每秒 1,000 次更新）期间也能保持高读取吞吐量。
*   **效率：** 索引构建速度显著加快——仅需 8 分钟，而 ParadeDB 需要 19 分钟，GIN 则需要 2 小时以上。

**架构创新**
TIN 速度优势的核心在于它直接使用 Postgres 的 `ctid`（元组标识符）作为文档 ID。竞争扩展通常分配顺序标识符，且必须执行开销巨大的二次映射来定位 Postgres 中的行，而 TIN 完全避免了这种开销。这种“Postgres 原生”方法实现了 O(1) 的行查找。此外，TIN 采用专门的两级位图编码来高效压缩 48 位标识符，从而支持高度矢量化的 CPU 操作并减少磁盘 I/O。

通过优化数据的读取和索引方式，无论索引是存储在内存中还是需要磁盘访问，TIN 都能确保搜索性能“快得惊人”。

---

## 7. Show HN: CUA-S1 – A System One Model for Computer Use

**原文标题**: Show HN: CUA-S1 – A System One Model for Computer Use

**原文链接**: [https://github.com/trycua/cua](https://github.com/trycua/cua)

Cua is an open-source ecosystem designed to enable AI agents to interact with computers via graphical interfaces, APIs, and code—a concept the creators call "Computer-Use 2.0." The suite provides the infrastructure, models, and evaluation tools necessary to build and deploy desktop automation agents.

Key components of the ecosystem include:

*   **CUA-S1:** A family of small, specialized "System 1" models designed for fast, bounded decision-making, such as form-filling and UI element scoring. These research models are hosted on Hugging Face and focus on structured interface interaction rather than general-purpose reasoning.
*   **Cua Fleets:** A service for provisioning isolated cloud desktops. Developers can use the Sandbox SDK to claim Linux desktops, run commands, and interact with applications in a secure, scalable environment.
*   **Cua Driver:** A cross-platform tool (macOS, Windows, Linux) that allows agents to inspect and operate native desktop apps. Notably, it supports background delivery, enabling agents to work without moving the user's physical cursor or taking focus.
*   **Lume:** A utility for managing local macOS and Linux VMs on Apple Silicon, facilitating unattended setup and SSH connectivity.
*   **Cua Bench:** A benchmarking framework for building computer-use tasks, evaluating agent trajectories, and generating training data.

The project is largely MIT-licensed and integrates with popular agents like Claude Code and Cursor. By providing both the "driver" for execution and the specialized models for UI navigation, Cua offers a comprehensive stack for developers building the next generation of computer-use automation.

---

## 8. 苏珊·齐亚尼的 Buchla 食谱

**原文标题**: Suzanne Ciani's Buchla Cookbook

**原文链接**: [https://echo.orpheusinstituut.be/article/suzannes-buchla-cookbook](https://echo.orpheusinstituut.be/article/suzannes-buchla-cookbook)

生成摘要时出错

---

## 9. 电路的秘密生活

**原文标题**: The Secret Life of Circuits

**原文链接**: [https://blog.coredump.cx/p/the-secret-life-of-circuits-is-here](https://blog.coredump.cx/p/the-secret-life-of-circuits-is-here)

生成摘要时出错

---

## 10. Supabase (YC S20) Is Hiring for OrioleDB

**原文标题**: Supabase (YC S20) Is Hiring for OrioleDB

**原文链接**: [https://supabase.link/orioledbjob](https://supabase.link/orioledbjob)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 2 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 3 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 4 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 5 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 6 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 7 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 8 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 9 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 10 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 11 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 12 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 13 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 14 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 15 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 16 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 17 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 18 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 19 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 20 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 21 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 22 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 23 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 24 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 25 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 26 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 27 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 28 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 29 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 30 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 31 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 32 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 33 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 34 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 35 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 36 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 37 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 38 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 39 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 40 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 41 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 42 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 43 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 44 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 45 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 46 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 47 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 48 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 49 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 50 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 51 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 52 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 53 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 54 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 55 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 56 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 57 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 58 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 59 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 60 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 61 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 62 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 63 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 64 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 65 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 66 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 67 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 68 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 69 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 70 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 71 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 72 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 73 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 74 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 75 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 76 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 77 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 78 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 79 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 80 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 81 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 82 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 83 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 84 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 85 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 86 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 87 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 88 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 89 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 90 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 91 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 92 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 93 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 94 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 95 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 96 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 97 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 98 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 99 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 100 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 101 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 102 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 103 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 104 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 105 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 106 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 107 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 108 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 109 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 110 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 111 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 112 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 113 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 114 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 115 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 116 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 117 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 118 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 119 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 120 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 121 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 122 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 123 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 124 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 125 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 126 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 127 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 128 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 129 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 130 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 131 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 132 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 133 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 134 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 135 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 136 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 137 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 138 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 139 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 140 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 141 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 142 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 143 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 144 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 145 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 146 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 147 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 148 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 149 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 150 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 151 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 152 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 153 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 154 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 155 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 156 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 157 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 158 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 159 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 160 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 161 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 162 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 163 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 164 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 165 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 166 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 167 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 168 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 169 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 170 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 171 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 172 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 173 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 174 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 175 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 176 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 177 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 178 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 179 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 180 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 181 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 182 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 183 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 184 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 185 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 186 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 187 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 188 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 189 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 190 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 191 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 192 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 193 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 194 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 195 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 196 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 197 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 198 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 199 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 200 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 201 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 202 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 203 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 204 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 205 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 206 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 207 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 208 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 209 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 210 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 211 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 212 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 213 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 214 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 215 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 216 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 217 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 218 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 219 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 220 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 221 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 222 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 223 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 224 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 225 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 226 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 227 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 228 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 229 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 230 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 231 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 232 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 233 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 234 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 235 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 236 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 237 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 238 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 239 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 240 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 241 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 242 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 243 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 244 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 245 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 246 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 247 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 248 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 249 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 250 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 251 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 252 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 253 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 254 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 255 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 256 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 257 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 258 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 259 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 260 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 261 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 262 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 263 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 264 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 265 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 266 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 267 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 268 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 269 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 270 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 271 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 272 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 273 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 274 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 275 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 276 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 277 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 278 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 279 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 280 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 281 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 282 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 283 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 284 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 285 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 286 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 287 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 288 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 289 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 290 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 291 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 292 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 293 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 294 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 295 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 296 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 297 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 298 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 299 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 300 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 301 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 302 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 303 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 304 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 305 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 306 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 307 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 308 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 309 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 310 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 311 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 312 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 313 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 314 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 315 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 316 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 317 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 318 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 319 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 320 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 321 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 322 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 323 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 324 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 325 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 326 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 327 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 328 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 329 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 330 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 331 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 332 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 333 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 334 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 335 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 336 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 337 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 338 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 339 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 340 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 341 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 342 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 343 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 344 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 345 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 346 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 347 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 348 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 349 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 350 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 351 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 352 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 353 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 354 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 355 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 356 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 357 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 358 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 359 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 360 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 361 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 362 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 363 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 364 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 365 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 366 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 367 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 368 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 369 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 370 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 371 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 372 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 373 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 374 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 375 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 376 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 377 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 378 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 379 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 380 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 381 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 382 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 383 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 384 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 385 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 386 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 387 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 388 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 389 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 390 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 391 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 392 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 393 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 394 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 395 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 396 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 397 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 398 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 399 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 400 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 401 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 402 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 403 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 404 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 405 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 406 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 407 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 408 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 409 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 410 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 411 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 412 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 413 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 414 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 415 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 416 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 417 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 418 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 419 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 420 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 421 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 422 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 423 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 424 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 425 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 426 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 427 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 428 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 429 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 430 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 431 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 432 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 433 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 434 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 435 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 436 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 437 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 438 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 439 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 440 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 441 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 442 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 443 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 444 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 445 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 446 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 447 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 448 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 449 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 450 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 451 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 452 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 453 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 454 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 455 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 456 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 457 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 458 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 459 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 460 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 461 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 462 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 463 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 464 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 465 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 466 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 467 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 468 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 469 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 470 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 471 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 472 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 473 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 474 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 475 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 476 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 477 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 478 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 479 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 480 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 481 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 482 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 483 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 484 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 485 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 486 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 487 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 488 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 489 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 490 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 491 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 492 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 493 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 494 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 495 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 496 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 497 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 498 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 499 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 500 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 501 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 502 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 503 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 504 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 505 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 506 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 507 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 508 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 509 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 510 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 511 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 512 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 513 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 514 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 515 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 516 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 517 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 518 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 519 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 520 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 521 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 522 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 523 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 524 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 525 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 526 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 527 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 528 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 529 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 530 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 531 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 532 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 533 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 534 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 535 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 536 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 537 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 538 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 539 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 540 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 541 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 542 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 543 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 544 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 545 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 546 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
