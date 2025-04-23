# Hacker News 热门文章摘要 (2025-04-23)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. GTA圣安地列斯20年老Bug如何在Windows 11 24H2中浮出水面

**原文标题**: How a 20 year old bug in GTA San Andreas surfaced in Windows 11 24H2

**原文链接**: [https://cookieplmonster.github.io/2025/04/23/gta-san-andreas-win11-24h2-bug/](https://cookieplmonster.github.io/2025/04/23/gta-san-andreas-win11-24h2-bug/)

本文详细调查了侠盗猎车手：圣安地列斯在Windows 11 24H2中出现的一个漏洞，该漏洞导致水上飞机Skimmer从游戏中消失或将玩家抛向空中。SilentPatch（一款修复游戏漏洞的模组）的作者最初对这些报告不以为然，但在Windows 11 24H2虚拟机上确认了该问题。

调查显示，该漏洞源于游戏中Skimmer的车辆数据文件（vehicles.ide）中未初始化的车轮比例值。由于疏忽，Skimmer的定义缺少车轮比例参数，导致游戏从堆栈中读取垃圾值，直到Windows 11 24H2，这些值巧合地导致了可用但不正确的游戏体验。

根本原因追溯到游戏加载车辆数据的方式。CFileLoader::LoadVehicleObject函数使用sscanf解析vehicles.ide文件，并假定所有参数始终存在。由于Skimmer的条目省略了车轮比例值，因此相关变量保持未初始化状态，并将在其位置读取垃圾数据。在Windows 11 24H2之前，未初始化数据产生的默认值导致了（不正确的）稳定游戏体验，而现在更新后产生数字导致了超出范围的物理计算和崩溃。

作者为SilentPatch提供了一个修复方案，该方案包括在文件加载过程中为缺少的车轮比例参数提供默认值，并解释了游戏如何错误地使用了上面车辆定义的先前车轮比例值，但这种行为在Windows 11 24H2之前仍然巧合地稳定。文章最后强调了该漏洞的异常性质，质疑为什么它在被特定的Windows更新触发之前隐藏了这么长时间。

---

## 2. 启动HN：Cua (YC X25) – 用于计算机使用代理的开源Docker容器

**原文标题**: Launch HN: Cua (YC X25) – Open-Source Docker Container for Computer-Use Agents

**原文链接**: [https://github.com/trycua/cua](https://github.com/trycua/cua)

Cua (计算机使用代理): 一个开源框架，允许 AI 代理在高性能虚拟容器中控制完整的操作系统。它利用 Apple 的 Virtualization.Framework，在 Apple Silicon 上实现高达 97% 的原生速度，并支持任何视觉语言模型。

主要特性包括：

*   **高性能虚拟化：** 创建并运行具有接近原生速度的 macOS/Linux 虚拟机。
*   **计算机使用接口与代理：** 使 AI 系统能够观察和控制这些虚拟环境，与应用程序交互、浏览、编码并执行复杂的工作流程。

使用 Cua 的优势：

*   **安全与隔离：** 在隔离环境中运行代理。
*   **性能：** 在 Apple Silicon 上接近原生速度。
*   **灵活性：** 支持 macOS 和 Linux。
*   **可复现性：** 创建一致的环境。
*   **LLM 集成：** 支持各种 LLM 提供商。

该框架提供不同的安装选项，包括仅用于虚拟机管理的 Lume CLI、用于代理功能的完整安装，以及用于夜间构建特性的从源代码构建选项。Monorepo 中提供了几个库：Lume、Computer 和 Agent。

Cua 鼓励贡献，并提供全面的文档和演示来方便使用。它采用 MIT 许可证。

---

## 3. 人工智能无人驾驶汽车

**原文标题**: AI Horseless Carriages

**原文链接**: [https://koomen.dev/essays/horseless-carriages/](https://koomen.dev/essays/horseless-carriages/)

人工智能无马马车：对自动驾驶汽车发展与影响的探讨

---

## 4. MinC并非Cygwin

**原文标题**: MinC Is Not Cygwin

**原文链接**: [https://minc.commandlinerevolution.nl/english/home.html](https://minc.commandlinerevolution.nl/english/home.html)

MinC：一款Windows下的Unix模拟器，专为职业教育学生设计，让他们无需复杂的虚拟化就能学习Linux。它利用OpenBSD 6.1代码，直接在Windows上运行小型内核（不包括Win95和Win98）。这使得OpenBSD软件在Windows机器上可以接近原生速度运行。本质上，MinC提供了一种在Windows上运行OpenBSD的方式，而无需虚拟机。

---

## 5. 焦油坑想法——什么是焦油坑想法以及如何避免它们（2023）[视频]

**原文标题**: Tarpit ideas – what are tarpit ideas and how to avoid them (2023) [video]

**原文链接**: [https://www.ycombinator.com/library/Ij-tarpit-ideas-what-are-tarpit-ideas-how-to-avoid-them](https://www.ycombinator.com/library/Ij-tarpit-ideas-what-are-tarpit-ideas-how-to-avoid-them)

这期Y Combinator关于“泥潭创业点子”的视频将其定义为表面上听起来不错，但本质上有缺陷，并且可能使创业者陷入漫长而徒劳的努力中的创业概念。 该视频强调，这些想法通常会吸引创业经验有限的人。

该视频可能概述了泥潭创业点子的常见特征。 这些可能包括：

*   **解决一个并不真正存在的问题，或者用户并不愿意为解决方案付费的痛点。** 它们可能解决已经被充分满足的需求，或者用户愿意容忍的问题。

*   **依赖未经证实或难以扩展的技术。** 需要技术突破或依赖快速变化领域的想法可能风险很高。

*   **面临激烈的竞争或监管障碍。** 进入饱和的市场或应对复杂的法规可能会严重阻碍增长。

*   **在验证想法之前需要大量的资本投资。** 在证明产品与市场契合度之前构建复杂的产品或获取庞大的用户群可能导致资源浪费。

为了避免泥潭创业点子，该视频可能建议：

*   **彻底的客户验证：** 在构建任何东西之前，与潜在客户交谈，了解他们的需求并验证问题。

*   **从小处着手并快速迭代：** 构建最小可行产品（MVP）来测试假设并收集反馈。

*   **专注于利基市场：** 针对具有针对性解决方案的特定用户群。

*   **乐于改变方向：** 愿意根据客户反馈和市场现实改变想法。

本质上，该视频建议创业者对其自身的想法持高度批判态度，尽早验证假设，并优先考虑为付费客户解决实际问题。

---

## 6. 基于进化算法的自动化天线设计 [pdf] (2006)

**原文标题**: Automated Antenna Design with Evolutionary Algorithms [pdf] (2006)

**原文链接**: [https://ntrs.nasa.gov/api/citations/20060024675/downloads/20060024675.pdf](https://ntrs.nasa.gov/api/citations/20060024675/downloads/20060024675.pdf)

这份PDF似乎是2006年一篇题为《利用进化算法的自动化天线设计》的文档的开头。遗憾的是，提供的内容主要是元数据和压缩图像数据(CCITTFaxDecode)，没有详细描述文章内容的任何可读文本。因此，无法根据实际研究内容提供恰当的摘要。只能从标题推断该文档讨论了使用进化算法（一种优化技术）来自动化天线设计。它可能涵盖天线设计中的挑战、进化算法在克服这些挑战中的应用，并可能展示这种自动化设计过程的具体示例或结果。

---

## 7. 悬秤

**原文标题**: The Danglepoise

**原文链接**: [https://www.sallery.co.uk/danglepoise](https://www.sallery.co.uk/danglepoise)

在2025年出版的《吊灯奇谭》中，作者详细描述了他们创造定制的、电动升降吊灯的旅程。由于对现代灯具的脆弱感到不满，并且无法找到合适的古董灯或配套灯，他们出于对电动机的热爱，开始了DIY项目。

作者最初的研究 направлено на изследване на плъзгащите пръстени за захранване на лампата, позволявайки ѝ да се движи, но високата цена на качествените плъзгащи пръстени, оценени за работа с електрическа мрежа, предизвика преосмисляне на дизайна. Те се спряха на система, използваща стоманен кабел, навит около задвижван от мотор барабан, с персонализирани 3D отпечатани скоби за управление на гъвкавия кабел на лампата в зигзагообразен модел.

机械设计采用了带有制动器的步进电机，用于精确定位和保持，尽管其能耗较高。 选择基于ESP32的TinyPICO微控制器进行电子控制，从而实现wifi控制和状态指示。

电子设计包括用于主电压组件（电源、继电器、保险丝）和低电压控制（电机驱动器、微控制器）的独立PCB。 该系统需要一个24V电源来为制动器供电，一个5V稳压器来为微控制器供电，以及一个电机驱动器芯片来实现平稳安静的步进电机控制。 作者优先考虑安全性，使用高质量的封装式主电源。

---

## 8. 我不再凭感觉编程了：一个菜鸟的视角

**原文标题**: I won't be vibe coding anymore: a noob's perspective

**原文链接**: [https://varunraghu.com/why-i-wont-be-vibe-coding-anymore/](https://varunraghu.com/why-i-wont-be-vibe-coding-anymore/)

本文写于2025年4月，表达了一位程序员对“氛围编码”——即过度依赖人工智能构建应用程序——的幻灭感。作者自称“菜鸟”，最初拥抱人工智能工具是为了克服编写糟糕代码和难以理解基本概念的挫败感。他们发现人工智能帮助他们快速构建功能性应用程序。

然而，作者在一个不眠之夜体验到顿悟。他们意识到，尽管构建了“有用的应用程序”，但几周来他们什么都没学到。这让他们得出结论：编码的核心价值不在于最终产品，而在于解决问题、批判性思维以及个人投入的过程。

作者将编码与写作进行类比，强调了创造过程和个人应对挑战方式的重要性。他们担心过度依赖人工智能会剥夺他们这些基本的学习体验。

最终，作者决定与“氛围编码”分手，回到自己编写代码的状态，即使代码“很烂”，速度很慢，需要深思熟虑。他们优先考虑学习过程和自身技能的发展，而不是人工智能生成的代码所带来的便利和速度。这篇文章赞扬了传统编码体验中固有的个人投入和学习。

---

## 9. ZGC 如何为 Java 堆分配内存

**原文标题**: How ZGC allocates memory for the Java heap

**原文链接**: [https://joelsiks.com/posts/zgc-heap-memory-allocation/](https://joelsiks.com/posts/zgc-heap-memory-allocation/)

本文深入探讨了OpenJDK中垃圾收集器ZGC如何为Java堆分配内存。堆被划分为称为页面的逻辑区域，分为小型（2MB）、中型（32MB）和大型（动态大小，超过4MB）三类。页面分配器管理这些页面，维护代表堆子集的多个分区。NUMA系统可以有多个分区，每个分区对应一个NUMA节点，以提高内存访问速度。

ZGC独特地分离了物理内存和虚拟内存，以对抗碎片化。虚拟内存被过度预留（最高可达最大堆大小的16倍或32倍），以增加找到连续内存范围的可能性。当页面被释放时，ZGC通过将物理内存重新映射到新的虚拟地址来主动整理堆。

映射缓存存储了未被任何页面使用的已映射内存范围，使用自平衡二叉搜索树进行高效管理。它使用侵入式存储来避免动态内存分配，并加快分配期间搜索连续内存的速度。

内存分配涉及声明容量、获取物理内存，并可能使用来自映射缓存的虚拟内存。分配过程优先从缓存中获取连续内存，然后增加容量（提交新内存），最后在必要时从缓存中收集较小的范围。如果无法增加容量，分配将优先收集可用的现有映射内存。

---

## 10. 考拉兹蚁

**原文标题**: Collatz's Ant

**原文链接**: [https://gbragafibra.github.io/2025/01/08/collatz_ant2.html](https://gbragafibra.github.io/2025/01/08/collatz_ant2.html)

本文探讨了使用改进的兰顿蚂蚁（称为“考拉兹蚂蚁”）可视化考拉兹序列的方法。蚂蚁的移动由考拉兹函数决定：如果数字为偶数，蚂蚁顺时针旋转90º；如果为奇数，蚂蚁逆时针旋转90º。蚂蚁每走一步前进一个单位。

作者最初使用了每步翻转单元格状态的版本，但后来提出了一个非翻转版本，该版本只是在每个访问的坐标处递增一个计数器，以便更清晰地可视化并避免歧义。

该研究揭示了考拉兹蚂蚁生成的视觉“地形”与相应序列的停止时间之间的相关性。相似的地形往往具有相似（或相同）的停止时间，尽管反之不一定成立。文章表明，具有共享子序列的序列（如提供的Python代码中的`intersect1d`函数所示）会产生相似的地形。

此外，本文还说明了在一定数量的考拉兹步骤后收敛的序列也会表现出地形相似性，通常伴随90º、180º或更大的旋转。随着收敛子轨迹之间步骤差异的增加，相似程度会降低，经过大量步骤（例如，300步）后，仅留下更大规模的共同特征。

---

## 11. MOS 6502非法操作码的工作原理 (2008)

**原文标题**: How MOS 6502 Illegal Opcodes Work (2008)

**原文链接**: [https://www.pagetable.com/?p=39](https://www.pagetable.com/?p=39)

本文通过研究MOS 6502处理器的内部架构和指令解码过程，解释了该处理器上非法操作码的工作原理。与使用微代码的CPU不同，6502使用一个130x21位的PLA（可编程逻辑阵列）来解释指令。PLA中的每一行都比较操作码和当前时钟周期（T1-T6），如果它们匹配，则触发并启动特定的CPU动作。

操作码的结构允许行为的泛化，这意味着某些PLA行可以为多个相似的操作码触发，执行诸如获取地址字节之类的共享任务。非法操作码的出现是因为这些未定义的指令仍然可以触发为有效指令设计的现有PLA行。

本文以操作码$AF（LAX绝对寻址）为例来说明这一点。$AF没有专用的PLA行，但它的位域在特定周期（T1、T2、T4）触发为$AD（LDA绝对寻址）和$AE（LDX绝对寻址）设计的行。在周期T3中，它会*同时*触发LDA和LDX行，导致处理器将获取的值同时加载到累加器（A）和X寄存器中，从而有效地创建“LAX”指令。

本文还解释了“KIL”（停止）操作码。当所有时钟周期（T1-T7）中都没有有效的指令行触发时，就会发生这种情况，从而阻止T位域复位。这会停止CPU并禁用中断，因为中断请求会被延迟到指令完成（T复位）为止，而这种情况永远不会发生。因此，了解非法操作码如何与6502的PLA交互可以揭示对CPU内部设计的见解，并可能发现其他未记录的行为。

---

## 12. 帆船时代的船上啤酒 (2017)

**原文标题**: Beer on Board in the Age of Sail (2017)

**原文链接**: [https://blog.library.si.edu/blog/2017/08/02/beer-board-age-sail/](https://blog.library.si.edu/blog/2017/08/02/beer-board-age-sail/)

朱莉娅·布莱克利的《风帆时代的船上啤酒》探讨了啤酒作为航海者主食饮料的历史意义，尤其是在风帆时代。 文章追溯了啤酒酿造的起源，可追溯到古代文明，并强调了啤酒在船只上的重要性，它提供了营养、卡路里，并且是潜在污染水的更安全替代品。

文章详细介绍了提供给水手的配给，参考了英国皇家海军的记录和塞缪尔·佩皮斯等人物。 它强调消费的啤酒通常是酒精含量低的“淡啤酒”。 文章还探讨了啤酒在预防坏血病中的作用，引用了詹姆斯·库克的海上航行以及使用云杉啤酒（一种源自美洲原住民的实践）作为维生素C的来源。

文章讨论了某些地区从啤酒到朗姆酒的转变、美国海军对酒精的禁令以及早期美国啤酒生产的历史背景。 文章重点介绍了路易斯·巴斯德通过巴氏消毒法对啤酒保鲜的贡献。 最后，作者谈到了某些常见英语短语的航海起源，并鼓励读者探索史密森尼学会图书馆的藏品，以进一步调查啤酒和海洋相互交织的历史。

---

## 13. Show HN: Moose – 用 ClickHouse 构建分析后端的开源框架

**原文标题**: Show HN: Moose – OSS framework to build analytical back ends with ClickHouse

**原文链接**: [https://docs.fiveonefour.com/moose](https://docs.fiveonefour.com/moose)

Moose是一个开源框架，旨在简化使用ClickHouse创建分析后端的过程。它允许开发者使用TypeScript或Python定义数据模型，自动生成必要的数据摄取、存储和API基础设施。这种方法旨在解决构建分析后端时常见的痛点，例如工具碎片化、模式漂移和复杂的开发工作流程。

使用Moose的主要优势包括类型安全的数据模型、简化的流式和批量摄取、实时流处理、数据库内转换以及简化的API创建。通过在代码中定义数据模型，Moose消除了手动更新数据库模式、API和消息格式的需求。

Moose还提供了一个本地开发环境，可以通过单个命令启动，从而实现快速迭代和测试。此本地环境镜像生产环境，最大限度地减少配置和设置。热重载等功能允许开发人员立即看到整个堆栈中反映的变化。

该框架是模块化和可配置的，以ClickHouse作为默认的OLAP数据库，并可选择集成Redpanda和Temporal用于事件流和工作流编排。计划中的扩展包括支持其他数据仓库，如Snowflake、Databricks和BigQuery，以及其他事件流平台。Moose专为用户界面分析、BI、数据仓库、数据迁移、事件流和ETL工作负载等应用而设计。

---

## 14. 展示HN：高级炼金术 – SQLAlchemy的与框架无关的库

**原文标题**: Show HN: Advanced-Alchemy – A framework agnostic library for SQLAlchemy

**原文链接**: [https://github.com/litestar-org/advanced-alchemy](https://github.com/litestar-org/advanced-alchemy)

高级炼金术 (Advanced Alchemy) 是一个 SQLAlchemy 伴侣库，旨在简化和优化 Python 应用程序中的数据库交互。它提供同步和异步仓库，具有常见的 CRUD 操作和优化的批量操作。它与流行的 Web 框架（如 Litestar、FastAPI、Flask、Starlette 和 Sanic）集成，提供助手和扩展程序以实现无缝集成。

主要功能包括：

*   具有常见 CRUD 和批量操作的仓库
*   简化仓库交互和类型转换的服务
*   Alembic 配置和 CLI 工具
*   具有审计列和主键的实用程序基类
*   内置文件对象数据类型，支持存储后端
*   优化的 JSON 类型，包括 Oracle JSON 类型
*   支持 UUID6/7 和 Nano ID
*   经过测试，支持多种数据库后端，如 SQLite、Postgres、MySQL、Oracle、Google Spanner、DuckDB 和 Microsoft SQL Server。

该库提供仓库和服务类，以简化数据访问和操作，并通过代码示例展示了诸如创建多个用户、分页数据检索和记录删除等操作。重点是提供一个强大而灵活的解决方案，用于将 SQLAlchemy 集成到各种 Python 项目（尤其是 Web 应用程序）中，同时改善开发人员体验和性能。该项目欢迎贡献，并通过 Discord 和 GitHub 讨论提供支持。

---

## 15. 操作 Petabyte 级 ClickHouse 集群的经验教训：第二部分

**原文标题**: Lessons learned operating petabyte-scale ClickHouse clusters: Part II

**原文链接**: [https://www.tinybird.co/blog-posts/what-i-learned-operating-clickhouse-part-ii](https://www.tinybird.co/blog-posts/what-i-learned-operating-clickhouse-part-ii)

本文是关于运营 PB 级 ClickHouse 集群系列文章的第二篇，重点介绍处理读取流量及相关运维挑战。文章强调了同时考虑读取和写入的重要性，因为摄取（写入）会通过表中的数据分片数量直接影响读取性能。

文章涵盖了处理不同流量类型（实时查询、长时间运行查询和回填），并提出了诸如使用不同副本和应用层负载均衡等策略，以避免影响实时查询延迟。查询设计至关重要；作者强调通过首先按排序键列进行过滤、使用 PREWHERE 以及延迟复杂操作来优化查询。文中还讨论了 `max_threads`、`max_memory` 和 `max_bytes_before_external_group_by` 等设置。

文章重点介绍了回填物化视图可能存在的问题，并建议不要使用 `POPULATE`，因为存在数据重复的风险。相反，建议使用 Null 表并调整批处理大小。

监控至关重要，重点是跟踪查询、ZooKeeper/S3 错误、复制延迟和队列长度。作者强调了关键系统表（`system.query_log`、`system.processes`、`system.part_log`）对于故障排除至关重要。

最后，作者还提到了诸如默认表删除行为、物化视图和特定列类型可能存在的问题以及谨慎管理 `ON CLUSTER` 操作的重要性等杂项。Altinity 的知识库被推荐为 ClickHouse 管理的宝贵资源。

---

## 16. 原生 visionOS 平台支持

**原文标题**: Native visionOS platform support

**原文链接**: [https://github.com/godotengine/godot/pull/105628](https://github.com/godotengine/godot/pull/105628)

本文讨论了一项拟议的对 Godot 游戏引擎的贡献：原生支持 Apple 的 visionOS 平台。这项贡献由 Apple 的 visionOS 工程团队主导，旨在让 Godot 游戏能够在 Vision Pro 上原生运行，无论是在平面窗口中，还是通过使用新的 visionOS VR 插件实现沉浸式 VR 体验。

这项贡献分为三个增量 PR：第一个 PR（本文详细介绍）添加了原生 visionOS 平台，主要通过创建共享的 "apple_embedded" 驱动程序来重用现有 iOS 平台的代码。后续的 PR 将添加对沉浸式场景的 Swift 编译支持，并引入 Vision Pro VR 插件。

作者强调了使用 Platformer 演示项目进行的大量测试，确认了在 iOS 和 visionOS 上使用 Metal 渲染的功能。他们还承认缺少一些功能，如动态 DPI 指标和自动 visionOS 图标创建，并邀请社区贡献。

本文提出了关于文档工具以及某些功能（如插件嵌入、archive/IPA 导出以及通过 ios_deploy 直接部署）的测试的问题。

社区成员对这项贡献表示热情，同时也对平台可能激增和维护负担表示担忧。建议包括将 iOS 衍生的平台统一在 Godot 代码库中的单个 "ios" 平台下，并使用宏来排除特定于平台的代码。

---

## 17. 像素是一种长度和面积的单位。

**原文标题**: Pixel is a unit of length and area

**原文链接**: [https://www.nayuki.io/page/pixel-is-a-unit-of-length-and-area](https://www.nayuki.io/page/pixel-is-a-unit-of-length-and-area)

本文探讨了数字成像中“像素”作为长度和面积单位使用时出现的不一致性，导致在应用量纲分析时产生数学矛盾。在计算面积时，像素长度乘以像素高度应得到平方像素（像素²），但口语习惯通常将像素视为无量纲单位，其中像素² = 像素 = 1。

作者提出了两个并不完美的解决方案来调和这种矛盾：

1.  **将像素定义为正方形：** 将像素定义为具有物理尺寸的正方形，该尺寸取决于设备，并引入“像素边长”或“√像素”作为表示其宽度和高度的线性单位。
2.  **将像素视为长度单位：** 在这种方法中，所有面积测量必须表示为平方像素，避免使用“百万像素”的缩写，而是写出平方像素的完整数字或使用诸如平方千像素之类的笨拙术语。

作者指出，像素的非公制性质以及其在复杂计算中参与程度有限减轻了这种不一致性的严重性。该问题主要突出了常见术语的不完善以及与科学计算中预期的一致单位行为的偏差。作者将此与磅作为质量和力单位的混淆进行类比，并将其与公制系统中千克和牛顿的明确分离进行对比。

---

## 18. Atuin Desktop: 可执行的行动手册

**原文标题**: Atuin Desktop: Runbooks That Run

**原文链接**: [https://blog.atuin.sh/atuin-desktop-runbooks-that-run/](https://blog.atuin.sh/atuin-desktop-runbooks-that-run/)

Atuin Desktop 旨在解决碎片化和不可靠的基础设施工作流程问题，它提供了一个本地优先的、可执行的终端工作流程手册编辑器。当前解决方案依赖于过时的文档、Slack 讨论串以及个人的 shell 历史记录，导致不一致性和任务重复执行的困难。

Atuin Desktop 允许用户通过将文档与可执行代码相结合，来创建可重复、可共享且可靠的工作流程。它在一个界面中提供了脚本块、嵌入式终端、数据库客户端和 Prometheus 图表等功能，消除了上下文切换。手册具有 Jinja 风格的模板进行动态更新，并且来自 shell 历史记录的自动完成功能可以实现即时调用。它是本地优先的，并由 CRDT 提供支持，通过 Atuin Hub 进行同步和共享。

Atuin 团队已经在使用 Atuin Desktop 来发布他们的 CLI、迁移基础设施、启动环境以及管理数据库查询。未来的计划包括用于增强协作的团队帐户，以及从 shell 历史记录自动生成手册。Atuin Desktop 承诺用一种有组织且高效的方式来管理基础设施和运营，从而取代从 Notion 和 Slack 复制粘贴的方式。

---

## 19. Solidjs: 构建用户界面的简单高性能响应式方案

**原文标题**: Solidjs: Simple and performant reactivity for building user interfaces

**原文链接**: [https://www.solidjs.com/](https://www.solidjs.com/)

无法访问文章链接。

---

## 20. 苹果和Meta因违反欧盟法律被处以数百万美元罚款

**原文标题**: Apple and Meta fined millions for breaching EU law

**原文链接**: [https://ca.finance.yahoo.com/news/apple-fined-570-million-meta-094701712.html](https://ca.finance.yahoo.com/news/apple-fined-570-million-meta-094701712.html)

欧盟因违反《数字市场法案》(DMA) 对苹果处以 5 亿欧元罚款，对 Meta 处以 2 亿欧元罚款。该法案旨在遏制大型科技公司的权力，是具有里程碑意义的立法。这是 2023 年推出 DMA 后的首次制裁。欧盟委员会发现，苹果限制应用程序开发商引导用户到 App Store 以外的更便宜的交易，并且 Meta 针对 Facebook 和 Instagram 用户的“付费或同意”模式违反了 DMA，因为该模式一直持续到 2024 年 11 月。

苹果和 Meta 批评了这些决定，并计划对罚款提出质疑。苹果辩称，欧盟对其进行不公平的针对，而 Meta 声称该决定不利于美国企业，并迫使其提供劣质服务。欧盟坚称，它正在执行明确的规则，所有在欧盟运营的公司都必须遵守其法律并尊重欧洲价值观。

与欧盟过去的反垄断处罚相比，这些罚款被认为是适度的。欧盟竞争监管机构表示，苹果必须取消实施的限制，Meta 的新版本将被评估以确定是否符合 DMA。两家公司有两个月的时间遵守规定，否则将面临进一步的罚款。虽然苹果在另一项浏览器选项调查中避免了罚款，但仍被指控阻碍侧载。Meta 的 Marketplace 也因用户数量低于所需阈值而取消了 DMA 认定。欧盟受到美国法院对谷歌广告技术行为判决的鼓舞，并被敦促继续调查谷歌和 X。

---

## 21. 六十年后，我们仍梦想着箭。

**原文标题**: Sixty Years On, We Still Dream of the Arrow

**原文链接**: [https://watershedmagazine.com/features/sixty-years-on-we-still-dream-of-the-arrow/](https://watershedmagazine.com/features/sixty-years-on-we-still-dream-of-the-arrow/)

无法访问文章链接。

---

## 22. 了解您的依赖关系

**原文标题**: Understand Your Dependencies

**原文链接**: [https://deps.dev/](https://deps.dev/)

这似乎是开源洞察工具的部分展示，表明其重点在于理解软件依赖关系。该工具可能帮助开发者和安全专业人员：

*   **可视化和分析软件依赖关系：** 开源洞察可能提供了一种查看软件项目中完整依赖链的方式，包括直接和传递依赖。
*   **识别潜在风险：** 这种分析允许用户识别潜在的安全漏洞、许可问题或与包含的开源组件相关的其他风险。
*   **管理和控制依赖关系：** 通过提供对这些依赖关系的洞察，该工具帮助用户在决定项目中包含哪些库和组件以及如何管理其版本时做出明智的决策。
*   **启用JavaScript是核心

在没有更多信息的情况下，很难详细说明，但开源洞察的主要目的是提供对项目中使用的开源依赖关系的全面理解，使使用者能够在安全性、许可和维护方面做出明智的决策。

---

## 23. 为什么我的eBPF程序在一个内核上工作却在另一个内核上失败？

**原文标题**: Why Does My eBPF Program Work on One Kernel but Fail on Another?

**原文链接**: [https://ebpfchirp.substack.com/p/why-does-my-ebpf-program-work-on](https://ebpfchirp.substack.com/p/why-does-my-ebpf-program-work-on)

无法访问文章链接。

---

## 24. 地理编码API对比：定价、免费额度和使用条款

**原文标题**: Geocoding APIs compared: Pricing, free tiers and terms of use

**原文链接**: [https://www.bitoff.org/geocoding-apis-comparison/](https://www.bitoff.org/geocoding-apis-comparison/)

本文对比了几种地理编码API，包括定价、免费层级和使用条款，旨在帮助读者为其项目选择最合适的选项。它考察了HERE、Google Maps Platform、Azure Maps、OpenCage、TomTom Maps、LocationIQ和Nominatim，重点关注免费请求数量、速率限制和每1000次请求的成本。作者强调该比较是中立的，因为其公司Superface提供一个通用的API客户端，可以与多个地理编码API配合使用，而不偏袒任何单一供应商。

文章强调了每种API在成本方面的优缺点。Azure Maps和Google Maps被认为是更昂贵的选择，而OpenCage和LocationIQ提供固定价格的月度计划，其中LocationIQ具有更慷慨的免费层级和更便宜的更高使用量计划。TomTom Maps被认为是适用于不均衡使用的具有成本效益的选项，每天提供大量免费请求，无需每月订阅。HERE适用于需要企业计划之前的大量使用。最后，Nominatim被认为是一个免费的、社区驱动的选项，最适合小型非商业项目。作者得出结论，LocationIQ在大规模使用时提供了极具竞争力的产品，TomTom非常适合低容量/不一致的使用，而HERE可能是以稳定的价格实现非常高使用量的理想选择。文章还包括供进一步研究的资源以及关于最近更新的说明。

---

## 25. 蓝宝石：基于 Rust 的 macOS 包管理器

**原文标题**: Sapphire: Rust based package manager for macOS

**原文链接**: [https://github.com/alexykn/sapphire](https://github.com/alexykn/sapphire)

Sapphire：macOS 平台的新型实验性软件包管理器，使用 Rust 编写，灵感来源于 Homebrew。目前处于 Alpha 阶段，可能不稳定，旨在管理命令行工具（Formulae）和桌面应用程序（Casks）。目前仅支持 ARM 架构，未来可能支持 x86 架构。

该项目由 `sapphire-core`（处理软件包管理逻辑的核心库）和 `sapphire-cli`（命令行界面）组成。

目前已实现的关键功能包括 bottle 和 cask 的安装/卸载、并行下载/安装、自动依赖关系解析，以及初步支持从源代码构建 Formulae。

路线图包括 `upgrade`、`cleanup`、`reinstall` 和 `init` 命令、前缀隔离以及持续的错误修复。

基本用法涉及 `sapphire --help`、`update`、`search`、`info`、`install` 和 `uninstall` 等命令。从源代码构建需要 Rust 工具链，包括克隆存储库并运行 `cargo build --release`。

欢迎贡献，尤其是在测试、错误报告、测试覆盖率和 CLI 改进方面。该项目采用 BSD-3-Clause 许可证。请注意，它是 Alpha 软件，不提供任何保证。

---

## 26. 格林效应席卷互联网

**原文标题**: The Gruen Transfer is consuming the internet

**原文链接**: [https://sebs.website/blog/the%20gruen-transfer-is-consuming-the-internet](https://sebs.website/blog/the%20gruen-transfer-is-consuming-the-internet)

塞巴斯蒂安·戴维·李斯博文“格鲁恩效应正在吞噬互联网”探讨了格鲁恩效应（即故意让消费者迷失方向以鼓励冲动消费）如何从实体店扩展到线上空间。他解释了诸如Facebook等最初旨在进行简单更新的平台，如何变得充斥着广告和无关内容，导致用户失去焦点并“末日滚动”。

这种现象超越了社交媒体，影响了网站设计，其中故意采用的复杂性和“UX黑暗模式”会阻碍用户完成特定任务，例如删除帐户或取消订阅。李斯认为，这种不必要的复杂性最终可能会产生不利影响，并提出了一个“网络设计的拉弗曲线”，其中摩擦力的增加会对用户体验产生负面影响。

他强调了欧盟立法要求订阅和取消订阅服务同样容易，并主张将“复杂性”作为立法保护消费者的衡量标准。李斯最后感叹格鲁恩效应的普遍性，希望类似的法规也能应用于日常生活中的体验，比如在实体店购物。

---

## 27. 物理学家设计出量子魔方并找到了最佳解法

**原文标题**: Physicists Designed a Quantum Rubik's Cube and Found the Best Way to Solve It

**原文链接**: [https://www.sciencealert.com/physicists-designed-a-quantum-rubiks-cube-and-found-the-best-way-to-solve-it](https://www.sciencealert.com/physicists-designed-a-quantum-rubiks-cube-and-found-the-best-way-to-solve-it)

科罗拉多大学博尔德分校的物理学家设计了一种“量子魔方”，这是一种置换谜题，与经典魔方有限的组合不同，它由于引入了量子叠加而具有无限可能的态。在这个量子版本中，一个方块可以同时处于移动和不移动的状态。

研究人员在一个简化的2x2蓝色和绿色方块拼图中测试了这个概念，他们要求经典、量子和组合求解器将方块排列成已解决的状态。经典求解器只能交换相邻的方块，量子求解器只能使用叠加态，而组合求解器可以使用两者。

不出所料，组合求解器的表现最好，平均步数更少。虽然经典求解器有时可以用比量子求解器更少的步数达到解决方案，但由于偶尔出现冗长的解决方案，其平均值更高。量子求解器表现出更一致，但稍长的解决方案。

关键的区别在于量子优势：经典求解器必须依赖于叠加态随机坍缩成已解决的状态，而量子求解器可以直接操纵这些叠加态。该团队还创建了一个3D版本的拼图。虽然实际的量子拼图可以使用超冷原子构建，但其主要目的是为数学家进行理论探索。

---

## 28. 恢复旧软件，保障儿童学习安全

**原文标题**: Restoring Old Software for Child Learning Safety

**原文链接**: [https://rietta.com/blog/child-learning-with-old-software/](https://rietta.com/blog/child-learning-with-old-software/)

本文探讨了作者致力于恢复旧软件的努力，特别是Windows 3.1和DOS时代的教育游戏，以供其子女学习。作者担心现代Web应用程序的风险以及过度接触互联网的问题，旨在提供一个更安全、独立于出版商的学习环境。

作者的方法包括在Linux主机上使用QEMU虚拟机，从原始介质或共享软件档案中恢复旧软件。他们强调了旧软件的用户界面优势，并以WordPerfect 6为例，说明其易发现性和专注性。

一个关键的例子是DOS游戏“1st Math”，作者的4岁孩子非常喜欢。作者赞赏该游戏如何通过键盘互动来促进计数、数字识别和精细运动技能，这与现代iPad游戏的点击和滑动特性形成鲜明对比。他们还讨论了“Freight Depot”在培养键盘技能方面的益处。

作者的长期目标是为孩子们创建一个专用的“旧电脑”设置，使其免受互联网、广告和网络欺凌的危害。他们还打算通过数字化和提供旧的教育内容，为软件保存工作做出贡献。作者最后邀请其他家长分享他们对儿童教育软件的方法，并幽默地提到了游戏SkiFree。

---

## 29. CSS 地狱

**原文标题**: CSS Hell

**原文链接**: [https://csshell.com/](https://csshell.com/)

提供的“CSS 地狱”内容似乎是一个占位符，表明 Web 应用程序存在问题。它仅将“CSS 地狱”作为标题，然后告知用户需要 JavaScript 才能运行该应用程序。

因此，没有实际的文章内容可供总结。该页面没有介绍 CSS 的陷阱或最佳实践。它仅仅是在发出一个信号，表明 JavaScript（许多 Web 应用程序的一项基本技术）在用户的浏览器中被禁用或未正常运行。

---

## 30. ClickHouse变得更懒更高效：引入延迟物化

**原文标题**: ClickHouse gets lazier and faster: Introducing lazy materialization

**原文链接**: [https://clickhouse.com/blog/clickhouse-gets-lazier-and-faster-introducing-lazy-materialization](https://clickhouse.com/blog/clickhouse-gets-lazier-and-faster-introducing-lazy-materialization)

本文介绍了延迟物化，ClickHouse 中的一项新的优化技术，它能显著提升查询性能，尤其是在 Top N 查询中。 延迟物化会延迟读取列数据，直到查询执行期间绝对必要时才读取。 这意味着 ClickHouse 只加载用于排序等即时操作所需的列，而推迟加载其余列。 这与 LIMIT 子句结合使用时尤其有效，因为较大列中的许多数据可能永远不需要读取。

本文重点介绍了 ClickHouse 现有的 I/O 优化堆栈，其中包括列式存储、稀疏主键索引、二级数据跳过索引、投影和 PREWHERE 子句。 这些技术通过跳过不必要的列和修剪不相关的数据粒度和行来减少 I/O。 延迟物化是对这些现有优化的补充，它可以确保即使在过滤之后，也只在每个步骤加载所需的最小列数据。

一个使用亚马逊客户评论数据集的真实示例展示了其影响。 一个检索排名最高的五星级电子书评论的查询，最初需要 219 秒才能完成完整扫描，但随着每个优化层的启用，其性能得到了显著提高。 延迟物化在最大限度地减少 I/O 方面发挥了关键作用，它将大型文本列（product_title、review_headline、review_body）的加载推迟到排序和应用 LIMIT 子句之后。 本文详细介绍了列式存储对于启用这种延迟 I/O 优化至关重要。

---

## 31. 揭秘装饰器：它们不必晦涩难懂

**原文标题**: Demystifying decorators: They don't need to be cryptic

**原文链接**: [https://www.thepythoncodingstack.com/p/demystifying-python-decorators](https://www.thepythoncodingstack.com/p/demystifying-python-decorators)

本文旨在通过将概念分解为易于理解的部分来揭开Python装饰器的神秘面纱，前两部分重点介绍闭包和装饰器入门。

第一部分解释了闭包，通过演示如何在不使用全局变量的情况下跟踪传递给函数 `print()` 的参数来说明。它展示了局部变量和全局变量的局限性，并介绍了闭包的概念：一个内部函数访问其封闭函数作用域中的变量。这使得函数可以访问在多次调用中持续存在的数据，从而实现调用之间的“通信”。文章展示了如何使用 `.__closure__` 属性访问封闭数据，尽管方式不太直接。

第二部分以对闭包的理解为基础，介绍装饰器。它强调了之前的代码已经体现了装饰器的各个方面，即增强函数的功能。然后，文章重构了代码，创建了一个可重用的装饰器，可以应用于任何函数，而不仅仅是 `print()`。这通过以下方式实现：将外部函数重命名为 `store_arguments()`，向外部函数添加一个 `func` 参数来表示要装饰的函数，并允许内部函数接受任意数量的参数。文章引导读者创建一个更通用和可重用的装饰器，为后续部分讨论更高级的装饰器特性铺平了道路。

---

## 32. WhatsApp 辩称无法关闭的“可选”人工智能工具

**原文标题**: WhatsApp defends 'optional' AI tool that cannot be turned off

**原文链接**: [https://www.bbc.com/news/articles/cd7vzw78gz9o](https://www.bbc.com/news/articles/cd7vzw78gz9o)

WhatsApp因其新的AI功能Meta AI而面临批评，该功能嵌入消息服务中但无法移除，尽管其被标记为“可选”。该功能在聊天屏幕上显示为一个蓝色圆圈，并提供由Llama 4驱动的聊天机器人来回答用户问题。

用户在社交媒体上表达了对无法禁用该功能的沮丧。像Kris Shrishak博士这样的隐私倡导者指责Meta利用其市场地位，并将人们用作AI的测试对象，声称AI模型由于数据抓取（包括潜在的盗版书籍）而侵犯隐私。

Meta为该功能辩护，称其“完全可选”，并表示正在考虑用户反馈。他们还澄清说，Meta AI只能读取直接与聊天机器人共享的消息，并且个人聊天仍然是端到端加密的。

然而，人们仍然担心数据隐私以及使用个人信息来训练AI模型的问题。信息专员办公室正在监控Meta AI的技术和数据使用情况，特别是关于儿童的数据。建议用户对与Meta AI共享的信息保持谨慎，因为它可能被AI保留和使用。文章还涉及了围绕Meta涉嫌使用盗版书籍来训练其AI模型的一项争议。

---

## 33. 机器编织的代数语义

**原文标题**: Algebraic Semantics for Machine Knitting

**原文链接**: [https://uwplse.org/2025/03/31/Algebraic-Knitting.html](https://uwplse.org/2025/03/31/Algebraic-Knitting.html)

Nat Hurtig的博文探讨了为电脑针织开发形式语义的挑战，旨在实现类似于传统编程语言中的自动化分析和优化。与传统语言不同，电脑针织缺乏严谨的语义，阻碍了编译器优化和程序等价性检查等任务。

该博文强调了针织的3D特性带来的复杂性，其中线段的上下交叉会产生依赖关系，并阻止操作交换，即使没有直接的数据依赖性。现有的基于纽结理论的语义，虽然在数学上很严谨，但由于其依赖于连续形变，计算机无法直接使用。

作者提出利用代数拓扑，特别是辫群，作为一种潜在的解决方案。辫群使用代数结构来表示拓扑对象，例如相互交叉的线段，以一种计算机可以处理的方式。辫群使用生成元和关系来定义何时两个辫子是等价的。

最终目标是创建一个系统，让计算机可以推理电脑针织程序的行为，从而实现自动化优化、错误检查以及其他与传统编程语言类似的优势。该博文将电脑针织、量子计算以及计算中关于空间关系推理的挑战进行了有趣的类比。

---

## 34. Onyx (YC W24) 招聘机器学习工程师

**原文标题**: Onyx (YC W24) Is Hiring for ML Engineer

**原文链接**: [https://www.ycombinator.com/companies/onyx/jobs/3Se5ptG-machine-learning-engineer](https://www.ycombinator.com/companies/onyx/jobs/3Se5ptG-machine-learning-engineer)

Onyx，一家由 Y Combinator (W24) 支持的初创公司，正在开发一个开源的 GenAI 平台，现于旧金山招聘机器学习工程师。Onyx 旨在成为“LLM 之上的知识层”，提升代理和知识检索能力，以解决复杂的 QA 和 RAG 问题。

该职位涉及评估和实施先进技术，如基于 LLM 的知识图谱、高级 RAG、LLM 代理和信息检索算法。工程师还将通过个性化搜索、SME 建议以及构建对组织优先事项的语义理解，为用户体验的提升做出贡献。与创始人和 AI 负责人的合作将在塑造产品方向和 AI/ML 工程战略方面发挥关键作用。

成功的候选人将拥有 3 年以上的 AI/ML 经验，精通 PyTorch/Tensorflow、NLP 模型，并具有扎实的软件工程背景，包括 Web 框架和关系数据库。 熟悉 Typescript/React/NextJS、Python 和 Postgres 者优先考虑，对技术博客感兴趣者亦佳。

面试流程包括电话面试、ML 面试、实际编码面试和有偿的现场工作试用。

Onyx 已获得由 Khosla Ventures 和 First Round Capital 领投的 1000 万美元种子轮融资，其客户包括 Netflix、Ramp 和 Applied Intuition，并拥有像 Roku、Zendesk 和 L3Harris 这样的强大的开源用户。他们正在构建一个连接到公司文档和应用程序的平台，为用户提供一个集中的提问场所。

---

## 35. Show HN: Rowboat – 多智能体系统的开源IDE

**原文标题**: Show HN: Rowboat – Open-source IDE for multi-agent systems

**原文链接**: [https://github.com/rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat)

Rowboat：简化多智能体系统创建和部署的开源IDE。它由OpenAI的Agents SDK驱动，使用户能够快速原型设计和构建这些系统，通常只需几分钟。其核心功能围绕着一个能将自然语言想法转化为功能性多智能体工作流程的副驾驶展开。

主要功能包括连接到MCP（多计算机程序）服务器和导入工具的能力，以及使用HTTP API或Python SDK的集成选项。这使开发人员能够无缝地将Rowboat创建的智能体集成到现有应用程序中。

快速入门指南提供了克隆GitHub存储库后使用Docker设置Rowboat的说明。该演示突出了使用MCP工具轻松创建多智能体助手的过程。提供的代码片段展示了HTTP API（使用`curl`）和Python SDK，用于与智能体交互，演示了如何发送消息和接收响应。Rowboat旨在通过提供用户友好的IDE和灵活的集成选项，简化通常复杂的多智能体系统构建过程。

---

## 36. 我如何使用 Obsidian、Hugo、GitHub 和 Cloudflare 搭建博客 —— 零成本，完全自主

**原文标题**: How I Blog with Obsidian, Hugo, GitHub, and Cloudflare – Zero Cost, Fully Owned

**原文链接**: [https://ingau.me/blog/how-i-write-my-blogs-in-obsidian-and-publish-instantly/](https://ingau.me/blog/how-i-write-my-blogs-in-obsidian-and-publish-instantly/)

本文详细介绍了一种使用Obsidian、Hugo、GitHub和Cloudflare Pages编写和发布博客文章的工作流程，重点强调零成本、完全自主的系统。作者描述了他们如何使用Obsidian进行写作，因为它采用本地优先模式和无干扰界面，并通过iCloud在设备间同步笔记。

发布过程涉及使用Hugo和Bear Blog主题来搭建快速且简洁的网站，并通过GitHub和Cloudflare Pages进行部署。这种设置提供了完全控制，避免了订阅、厂商锁定和平台依赖。

设置过程包括：

1. 安装Hugo并使用Bear Blog主题创建一个新站点。
2. 通过将Hugo站点的content/blog文件夹作为Obsidian库打开来连接Obsidian，允许直接写入Hugo目录。
3. 在Obsidian文章中使用一致的Front Matter模板，包括一个`draft`标志以便于切换。
4. 使用Hugo的服务器和草稿可见性(`hugo server -D`)在本地预览文章。
5. 将本地Hugo站点连接到GitHub存储库。
6. 设置Cloudflare Pages，将其连接到GitHub存储库，并配置构建设置（`hugo --minify`命令和`public`输出目录）。

发布工作流程包括在Obsidian中写作，准备就绪后将`draft: true`更改为`draft: false`，提交并推送到GitHub。Cloudflare Pages会自动检测更改并重建站点。作者强调了初始设置的投入，但赞扬了随后的无摩擦、免费且自主的工作流程。

---

## 37. 亚纳秒闪存

**原文标题**: Subnanosecond Flash Memory

**原文链接**: [https://www.nature.com/articles/s41586-025-08839-w](https://www.nature.com/articles/s41586-025-08839-w)

本文报道了一种利用二维狄拉克石墨烯通道和二维增强热载流子注入机制的亚纳秒闪存的开发。该研究旨在满足人工智能时代对更快非易失性存储器的需求，克服现有闪存的速度限制和SRAM的易失性。

主要创新在于利用二维材料的原子级薄特性来优化水平电场（Ey）分布，从而增强热载流子注入（2D-HCI）。研究表明，石墨烯和二硒化钨（WSe2）表现出材料依赖性的热载流子注入行为。由于其狄拉克特性，石墨烯促进电子和空穴的注入，而WSe2主要支持空穴注入。

基于石墨烯的闪存以5V的低编程电压实现了400皮秒的编程速度，并在超过5.5 × 10^6次循环中表现出强大的耐久性。改进的Ey辅助编程效率提高了注入电流。

该研究将二维热载流子注入机制与硅基闪存的局限性进行了对比，硅基闪存的电场加速效率较低。使用准二维模型来解释二维材料的薄体通道如何增强电场分布，从而实现卓越的注入效率。研究结果表明，闪存可以超越易失性SRAM的速度。

---

## 38. 布雷斯洛假设的证实：一种在液态水中稳定的卡宾

**原文标题**: Confirmation of Breslow's hypothesis: A carbene stable in liquid water

**原文链接**: [https://www.science.org/doi/10.1126/sciadv.adr9681](https://www.science.org/doi/10.1126/sciadv.adr9681)

无法访问文章链接。

---

## 39. π0.5：具有开放世界泛化能力的大规模视觉语言模型

**原文标题**: π0.5: A VLA with open-world generalization

**原文链接**: [https://pi.website/blog/pi05](https://pi.website/blog/pi05)

本文介绍π0.5，一种新型视觉-语言-动作(VLA)模型，旨在提高机器人领域中开放世界泛化能力。与先前在受控环境中表现良好的模型不同，π0.5展示了泛化到全新且“混乱”环境（如家庭）的能力，使机器人能够在未见过的地点执行清洁或整理等复杂任务。

π0.5背后的关键创新在于异构数据上的协同训练，结合了包括机器人演示、多模态网络数据（图像描述、物体检测）、口头指令和来自各种机器人类型的数据等多种来源。 这种方法使模型能够学习物理技能和对任务的语义理解。 文章强调，这些数据源的正确混合充当了一个“课程”，实现了跨不同抽象层次的泛化。

实验表明，π0.5优于未经过某些数据源训练的模型，尤其擅长识别新物体并在分布外环境中执行任务。 一项规模研究表明，性能随着训练环境数量的增加而提高，在接触约100个不同的训练地点后，性能达到了与直接在测试环境中训练的模型相当的水平。

π0.5采用分层方法，首先生成高级文本动作，然后使用流匹配动作专家选择适当的低级运动命令。 该模型的能力通过视频展示，视频展示了其在新家中执行长期任务、对环境变化和人为干扰的鲁棒性，以及遵循不同详细程度的语言命令的能力。

---

## 40. 展示HN：Morphik – 理解PDF图像且本地运行的开源RAG

**原文标题**: Show HN: Morphik – Open-source RAG that understands PDF images, runs locally

**原文链接**: [https://github.com/morphik-org/morphik-core](https://github.com/morphik-org/morphik-core)

Morphik：面向复杂视觉文档的开源RAG替代方案，专为PDF和视频等设计，允许开发者摄取、搜索、转换和管理非结构化数据。主要功能包括：由ColPali等技术驱动的多模态搜索，以理解视觉内容；为特定领域应用生成知识图谱；快速元数据提取（边界框、标签等）；以及与Google Suite、Slack和Confluence等工具的集成。它还提供缓存增强生成，以加快响应速度。

用户可以通过付费服务或自托管开源版本开始使用，免费层提供200页和100个查询。Python SDK和REST API简化了文档摄取和查询，并提供代码示例。Morphik控制台提供了一个基于Web的界面来与数据交互，也可以通过MCP访问。

欢迎通过错误报告、功能请求和Pull Request进行贡献。某些功能，特别是"ee"命名空间内的功能（如Morphik控制台），仅限于付费版本，不开源。

---

## 41. 我们尚未在通用人工智能方面取得任何进展

**原文标题**: We Have Made No Progress Toward AGI

**原文链接**: [https://www.mindprison.cc/p/no-progress-toward-agi-llm-braindead-unreliable](https://www.mindprison.cc/p/no-progress-toward-agi-llm-braindead-unreliable)

本文认为，尽管表面看来如此，大型语言模型（LLMs）在实现通用人工智能（AGI）方面并未取得实质性进展。文章声称，LLMs本质上是“脑死亡”的统计模型，而非推理机器。作者引用了Anthropic的研究，该研究使用“归因图”来窥探LLM的推理过程，揭示了一个由启发式和记忆模式组成的复杂网络，而非真正的算法理解。

关键点包括：

*   **LLMs的推理方式不像人类：** 内部过程不像人类推理，LLM对其输出的解释通常是捏造的（“幻觉”）。
*   **“思维链”不可靠：** 这些步骤是学习到的模式，并非模型内部思考的真实表征。
*   **人工智能代理并非解决方案：** LLMs可能会产生工具使用方面的幻觉，从而破坏整个数据管道。
*   **LLM架构调整是孤立的：** 改进可能会产生意想不到的负面副作用，较新的模型有时在特定任务上的表现更差。
*   **LLMs无法构建硬性规则：** 它们只能根据过去的数据来确定什么是“可能”正确的，需要不断地重新训练。
*   **进步仅仅是规模化：** 改进是通过大规模扩展统计模型来实现的，而不是通过真正的智能。
*   **当前的基准具有误导性：** 它们不能捕捉现实世界的表现。
*   **关注效率：** 衡量AGI的进展应该以能力相对于数据和训练工作的效率来衡量，数据和训练工作量的减少是一个积极的信号。封闭系统中没有模态崩溃。

作者的结论是，追求AGI需要从简单地扩展统计模型转向能够展示真正理解和推理能力的架构。

---

## 42. 鲸声提示：人工智能检测系统提醒船只注意航线上的鲸鱼

**原文标题**: Ping, You've Got Whale: AI detection system alerts ships of whales in their path

**原文链接**: [https://www.biographic.com/ping-youve-got-whale/](https://www.biographic.com/ping-youve-got-whale/)

鲸鱼观察者：利用人工智能的鲸鱼探测系统，旨在通过向船长提供实时警报，减少因船舶碰撞导致的鲸鱼死亡。该系统采用热感摄像机和机器学习技术来识别鲸鱼喷水，并将信息传递给专家，专家再将验证后的警报转发给船舶，使其能够改变航向。

该系统由伍兹霍尔海洋研究所的丹尼尔·齐特巴特开发，自2019年启动以来，鲸鱼观察者已显著改进，2024年探测到超过51,000次海洋哺乳动物。一个关键挑战在于装备大型集装箱船，这些船只是导致鲸鱼死亡的主要因素。通过改进技术，该系统现在能够可靠地探测到距离这些大型船只6公里以内的鲸鱼。

虽然尚未向集装箱船提供实时警报，但在夏威夷、阿拉斯加和美国西海岸的马逊航运公司的船舶上进行的测试已显示出可喜的成果。齐特巴特强调人工验证的重要性，以避免误报，因为该系统的目的是为了海洋保护，力求零误报以保持船长的注意力。虽然存在其他人工智能系统，但鲸鱼观察者因优先考虑人工监督而脱颖而出。

海洋生物学家约翰·卡拉姆博基迪斯强调实时探测是鲸鱼保护的一项关键但未被充分利用的策略。随着鲸鱼观察者的扩展，其开发人员希望更广泛的应用能够实现实时信息共享，最终使更多的鲸鱼免遭船舶撞击，特别是像北大西洋露脊鲸这样的濒危物种。

---

## 43. 意义机器 - 可视化大型语言模型如何分解和模拟意义

**原文标题**: Meaning Machine – Visualize how LLMs break down and simulate meaning

**原文链接**: [https://meaning-machine.streamlit.app](https://meaning-machine.streamlit.app)

无法访问文章链接。

---

## 44. 我本该也热爱生物学的。

**原文标题**: I should have loved biology too

**原文链接**: [https://nehalslearnings.substack.com/p/i-should-have-loved-biology-too](https://nehalslearnings.substack.com/p/i-should-have-loved-biology-too)

无法访问文章链接。

---

## 45. 开源项目获资助，以重塑公共互联网。

**原文标题**: Open Source Projects Receive Funding to Reclaim the Public Internet

**原文链接**: [https://nlnet.nl/news/2025/20250422-announcement-grants-CommonsFund.html](https://nlnet.nl/news/2025/20250422-announcement-grants-CommonsFund.html)

本文宣布，42个免费和开源项目已获得NGI Zero Commons基金的资助，以推进以公众为导向的互联网。这些项目涵盖了广泛的领域，从开放硬件和操作系统到教育工具和通信平台。

资助项目示例包括：

*   **硬件：**Solar FemtoTX主板（低功耗、太阳能供电主板），MNT Reform Touch（开放硬件平板电脑），FuseSoC兼容的Web目录（芯片设计软件包管理器）。
*   **操作系统/固件：**bcachefs（下一代Linux文件系统），KDE Plasma手势（Plasma桌面多点触控手势），Maemo Leste（安全移动Linux发行版）。
*   **教育：**ClassQuiz（学校隐私友好的测验），联合教学沉浸式体验&Flock XR（儿童增强现实）。
*   **通信/协作：**Podlibre（播客创作），PeerTube增强（去中心化视频平台），Livebook（交互式笔记本应用程序）。
*   **其他：**LiberaForms（端到端加密表单），Open Terms Archive（追踪条款和条件演变）。
* LLM2FPGA（在FPGA上本地运行LLM）

该基金旨在支持有助于重塑互联网公共属性的项目，重点关注透明度、隐私、安全性以及社区利益。本文还解释了申请人如何确定他们申请的资助轮次。

---

## 46. 迈克·伍德，跃蛙玩具创始人，启蒙一代人，去世，享年72岁

**原文标题**: Mike Wood, Whose LeapFrog Toys Taught a Generation, Dies at 72

**原文链接**: [https://www.nytimes.com/2025/04/19/business/michael-c-wood-dead.html](https://www.nytimes.com/2025/04/19/business/michael-c-wood-dead.html)

leapFrog Enterprises创始人迈克·伍德去世，享年72岁。受儿子早期阅读困难的启发，伍德发明了一种电子玩具，通过挤压塑料字母帮助孩子们学习字母发音。这个灵感源于音乐贺卡的创意，催生了LeapFrog及其旗舰产品LeapPad的诞生。 LeapPad于1999年推出，一炮而红，成为2000年假日季最畅销的玩具，并将LeapFrog转变为增长最快的玩具公司之一。伍德的发明产生了重大影响，教会了一代儿童阅读。

---

## 47. 旋转能解决哈勃难题吗？

**原文标题**: Can rotation solve the Hubble Puzzle?

**原文链接**: [https://academic.oup.com/mnras/article/538/4/3038/8090496?login=false](https://academic.oup.com/mnras/article/538/4/3038/8090496?login=false)

无法访问文章链接。

---

## 48. 最后的遗族

**原文标题**: The Last of Their Kind

**原文链接**: [https://nautil.us/the-last-of-their-kind-1204387/](https://nautil.us/the-last-of-their-kind-1204387/)

埃琳娜·卡扎米亚的文章《最后的物种》探讨了为复活北方白犀牛种群所做的绝望努力，该种群实际上已经功能性灭绝，仅存两只个体，分别是纳金和法图。文章详细介绍了北方白犀牛因偷猎而数量下降的历史以及动物园试图繁殖它们的努力。

文章主要关注由托马斯·希尔德布兰特领导的“生物救援”项目，该项目利用体外受精（IVF）和基因编辑等先进的生殖技术，从法图的卵子和已故雄性的冷冻精子中创造北方白犀牛胚胎。这些胚胎计划植入南方白犀牛代孕体内。

文章强调了所面临的挑战和挫折，包括一只携带北方白犀牛胎儿的代孕死亡。文章还讨论了与Colossal Biosciences公司的合作，该公司以利用古代DNA“复活”已灭绝物种而闻名，旨在增强胚胎的遗传多样性。

文章提出了伦理问题，即当其他保护工作和物种也迫切需要资源和保护时，关注复活一个物种是否值得。文章还谈到了北方白犀牛和南方白犀牛之间的差异，强调了将北方白犀牛恢复到其在北非特定生态位的的重要性。

---

## 49. 如何快速给智能手机充电：快充技术详解

**原文标题**: How to quickly charge your smartphone: fast charging technologies in detail

**原文链接**: [https://eb43.github.io/articles/fast-charging-technologies-in-detail.html](https://eb43.github.io/articles/fast-charging-technologies-in-detail.html)

《如何快速为智能手机充电：快充技术详解》（作者：Eugen Barilyuk，发表于2025年4月22日），旨在解释如何快速为智能手机充电，并可能深入探讨快充技术的技术层面。

虽然在无法访问全文的情况下无法获得确切的细节，但我们可以根据标题推断出可能涵盖的主题。文章可能讨论各种快速充电标准，或许会区分它们，并概述它们各自的充电速度、电压和电流能力。它可能会探讨常见的标准，如高通的 Quick Charge、USB 电源传输 (USB-PD) 以及来自三星自适应快速充电或 OnePlus Warp Charge 等制造商的专有解决方案。

文章也可能详细阐述快速充电背后的技术原理，例如设备如何与充电器通信以协商最佳充电参数。很可能涉及安全注意事项，包括温度控制和过压保护在防止快速充电期间损坏电池或设备方面的作用。最后，文章可能讨论不同充电器和设备的兼容性，解释某些充电器是否适用于特定智能手机，以及使用不兼容的充电器是否会影响充电速度甚至构成风险。

---

## 50. 让电脑杂志广告更精彩的浣熊们

**原文标题**: The raccoons who made computer magazine ads great

**原文链接**: [https://technologizer.com/home/2025/04/22/pc-connection-ads-raccoons/](https://technologizer.com/home/2025/04/22/pc-connection-ads-raccoons/)

本文探讨了PC Connection独特的营销策略。这家邮购电脑产品公司在20世纪80年代和90年代凭借以拟人化浣熊为特色的令人难忘的广告而声名鹊起。在充斥着目录式广告的市场中，PC Connection凭借Erick Ingraham的插图脱颖而出，这些插图描绘了浣熊从事日常活动，从经营面包店到打棒球，场景通常设置在新英格兰乡村。

这个想法源于让电脑不那么令人生畏的愿望，由PC Connection的创始人Patricia Gallup和David Hall带头，并由广告公司Church and Main执行。浣熊最初因其灵巧的爪子而被选中，后来成为公司的吉祥物，象征着适应性和创新。文案撰稿人David Blistein为这些插图配上了幽默的文字，强调了PC Connection的小镇价值观和客户服务。

这些广告出现在《PC Magazine》等流行的电脑杂志上，深受读者期待。PC Connection还向达到消费门槛的客户提供以浣熊角色为特色的赠品，进一步提高了品牌认知度。虽然浣熊广告在21世纪初从PC Connection的营销中淡出，但它们仍然是个人电脑早期创意广告的一个令人难忘且有效的例子。本文还提到了公司的创立及其对客户支持的关注，这为其成功做出了贡献。

---

## 51. 多项式特征是万恶之源吗？(2024)

**原文标题**: Are polynomial features the root of all evil? (2024)

**原文链接**: [https://alexshtf.github.io/2024/01/21/Bernstein.html](https://alexshtf.github.io/2024/01/21/Bernstein.html)

本文挑战了一种普遍的观点，即高阶多项式特征在机器学习中本质上是有问题的。文章认为，由于误解和不当使用，它们常常被不公平地诋毁。作者认为，如果使用得当，高阶多项式可以通过诸如正则化等标准的机器学习工具有效地控制。

首先要解决的误解是基的选择。标准多项式基（1, x, x^2, ...）被认为是导致不稳定和过拟合的关键原因。作者介绍了一些替代的多项式基，例如在逼近理论中常用的切比雪夫和勒让德多项式。然而，这些基针对插值进行了优化，而不是拟合噪声数据。

本文推崇伯恩斯坦基作为机器学习的更优选择。伯恩斯坦基多项式在计算机图形学中使用，具有几个优点：所有系数共享相同的“单位”，使其更容易正则化，并且多项式函数是这些系数的加权平均值。

第二个误解涉及维尔斯特拉斯逼近定理。该定理指出，多项式可以在一个区间内逼近连续函数，这意味着在使用多项式特征时，需要将输入特征归一化，使其位于特定范围内（例如[0, 1]）。

本文通过使用各种多项式基将正弦函数拟合到噪声数据来演示这些概念，突出了标准基、切比雪夫基和勒让德基的不稳定性，以及伯恩斯坦基的稳定性和易于正则化。文章最后得出结论，通过适当的表示和归一化，高阶多项式可以成为强大且可控的非线性特征。

---

## 52. 利用 DuckDB-WASM 通过 SQL 绘制 3D 图形（某种程度上）

**原文标题**: Abusing DuckDB-WASM by making SQL draw 3D graphics (Sort Of)

**原文链接**: [https://www.hey.earth/posts/duckdb-doom](https://www.hey.earth/posts/duckdb-doom)

本文详细介绍了一个实验，作者使用 DuckDB-WASM（一种分析型数据库）构建了一个简陋的 3D 游戏引擎，具体来说是一个基于文本的 Doom 克隆版，用于核心游戏逻辑，而非传统的 JavaScript。整个游戏世界，包括地图、玩家位置、敌人/子弹位置和游戏设置，都存储在 DuckDB 表格中。玩家移动、子弹物理和碰撞检测都通过 SQL 查询（UPDATE 和 DELETE 语句）来处理。

渲染是通过定义一个名为 `render_3d_frame` 的 SQL 视图来实现的，该视图使用递归 CTE 执行光线投射。此视图计算墙壁距离、高度，然后使用字符串聚合组装基于文本的 3D 场景。 JavaScript 用于将所有内容粘合在一起，处理键盘输入，运行游戏循环，从 SQL 视图获取背景帧，管理精灵（子弹、敌人），并执行 Z 缓冲区检查以确定精灵是否应在特定屏幕列上绘制在墙上。

作者讨论了遇到的几个挑战：正确加载 DuckDB-WASM、SQL 方言差异（AUTOINCREMENT 与 SEQUENCE）、使用表函数（generate_series）时的查询计划器限制、async/setInterval 竞争条件以及实现精灵的 Z 缓冲区逻辑。这些问题的解决方案包括重构 SQL 以使其对计划器更加友好，以及向异步主循环添加处理锁。

最终结果是一个可玩的，以大约 6-7 FPS 运行的游戏。虽然非常规，但该项目展示了 SQL 和 DuckDB-WASM 在其预期用途之外的任务方面的出人意料的能力。核心教训是，可以使用 SQL 执行复杂的状态管理和渲染，尽管需要考虑性能。

---

## 53. 玩具反斗城的兴衰 (2018)

**原文标题**: The Rise and Fall of Toys 'R' Us (2018)

**原文链接**: [https://www.history.com/articles/toys-r-us-closing-legacy](https://www.history.com/articles/toys-r-us-closing-legacy)

艾琳·布莱克莫尔的《玩具反斗城兴衰内幕》详细讲述了这家标志性玩具零售商从创立到最终倒闭的演变过程。它由查尔斯·拉扎勒斯于1948年创立，最初名为儿童廉价商品城，专门经营婴儿用品，后来随着拉扎勒斯意识到顾客的重复需求，转型为玩具销售。1957年，公司更名为玩具反斗城，开创了大型玩具商店的概念，采取超市式经营方式，以低廉的价格提供大量选择，有效地成为了第一个“品类杀手”。

玩具反斗城充分利用了战后婴儿潮和玩具行业的增长，并受到电视广告和芭比娃娃、土豆先生等标志性玩具的推动。该公司利用其规模优势来谈判更低的价格，将规模较小的竞争对手挤出市场，并占据了主导地位，在其鼎盛时期控制了全球玩具市场25%的份额。

然而，多种因素促成了它的衰落，包括电子商务的兴起、玩具偏好的演变、2005年的杠杆收购以及日益过时的门店。具有讽刺意味的是，它所帮助创建的大型商店模式也导致了它的 demise，沃尔玛和亚马逊等竞争对手以更低的价格提供类似的产品。该公司试图通过削减玩具选择和专注于价格来参与竞争，最终削弱了最初使玩具反斗城成功的魔力，导致其在2017年破产。

---

## 54. 超木 - 开源家具

**原文标题**: Hyperwood – Open-Source Furniture

**原文链接**: [https://hyperwood.org/](https://hyperwood.org/)

Hyperwood是一个开源家具系统，灵感来源于“小即是美”和Autoprogettazione，旨在让任何人都能用简单的木条，最少的工具和本地采购的材料创造出坚固的家具。它旨在赋能DIY爱好者、设计师和小制造商。

Hyperwood的核心在于个性化施工计划和优化材料清单的算法生成，从而促进家具制造的可及性、可持续性和减少浪费。虽然目前由于专业工具的原因，更适合具备编程知识的个人，但其长期愿景是创建图形用户界面（GUI），从而扩大其对更广泛受众的可访问性。本质上，Hyperwood提供了一种以可持续和高效的方式创建定制家具的方法，优先考虑本地资源和用户赋权。

---

## 55. 盖尔语的幽灵

**原文标题**: The Ghosts of Gaelic

**原文链接**: [https://www.historytoday.com/archive/behind-times/ghosts-gaelic](https://www.historytoday.com/archive/behind-times/ghosts-gaelic)

邓肯·斯内登的《盖尔语的幽灵》考察了苏格兰盖尔语语言和文化的现状，尤其是在2005年盖尔语语言法案和即将出台的苏格兰语言法案的背景下。虽然盖尔语的使用者占人口比例较小但正在增长，并且正在努力推广它，但由于英语的优势以及盖尔语社区面临的社会经济挑战，该语言面临着生存威胁。

这篇文章深入探讨了盖尔文化和英语之间复杂的关系，并以詹姆斯·麦克弗森的奥西安诗篇为例。麦克弗森对盖尔语传说的广受欢迎但备受争议的翻译，为苏格兰的传统带来了国际关注，但后来因其不真实性而受到批评。斯内登认为，奥西安虽然意义重大，但不应掩盖芬恩循环更广泛和更古老的盖尔语传统。这个口头传统，以芬恩·麦克库米尔和他的战士的叙述为特色，已被爱尔兰民间传说委员会和苏格兰研究学院等机构积极维护和记录。

斯内登强调需要摆脱以英语为中心的观点，让盖尔语社区用自己的语言保护和表达他们的文化。他认为，为了使苏格兰语言法案真正成功，它必须优先考虑盖尔语和苏格兰语社区的需求，特别是通过资金和基于社区的语言规划。虽然盖尔语教育和广播已经取得进展，但类似的支持对于社区发展至关重要，以确保盖尔语及其丰富的文化遗产的生存和未来活力。

---

## 56. 经典电脑复刻

**原文标题**: Classic Computer Replicas

**原文链接**: [https://obsolescence.dev/index.html](https://obsolescence.dev/index.html)

这篇短文摘录重点介绍了一款“经典计算机复制品”。要点如下：

*   它聚焦于一款特定的早期计算机。
*   这款计算机因是“第一台带有键盘的交互式计算机”而闻名。
*   该键盘被描述为“奇特的”，因为它没有使用标准的字母数字布局，表明它采用了一种独特或不寻常的输入方法。
*   “继续阅读”的号召性用语暗示这篇文章提供了更多关于这台计算机、它的键盘以及它的历史意义的细节。

本质上，这段摘录以一台使用非字母数字键盘的非常早期的交互式计算机的概念来吸引读者，邀请他们了解更多信息。

---

## 57. 适用于旧版 OS X 的项目

**原文标题**: Projects for Old OS X

**原文链接**: [https://jonathanalland.com/old-osx-projects.html](https://jonathanalland.com/old-osx-projects.html)

“旧版OS X项目”网站记录了作者重返旧版macOS的历程，以及他们为使这些系统在现代可用所做的努力。由于对现代macOS感到失望，作者提供了一系列项目，旨在修复损坏的功能、增强功能以及改善旧版OS X的整体体验。

这些项目分为几个领域：修复的Dashboard小部件（天气、单位转换器、翻译）、网页浏览和互联网（Chromium Legacy Downloader、Legacy Mac Proxy、Transmission、Apple Mail安全修复）、音频和视频（QuickTime调整、FFusion编解码器支持、用于打开各种视频和图像格式的辅助应用程序、视频下载器、媒体订阅首选项窗格）、游戏和模拟器（OpenEmu Lite、Dolphin for Legacy OS X、Steam API模拟器）、系统调整（SIMBL、Snow Leopard窗口控件、表情符号更新）、杂项应用程序（SyncThing、Side Button Enabler）以及针对他人应用程序的错误修复（Pages '09、CodeRunner）。

这些项目范围从使用新API更新小部件到修补安全漏洞以及提供与现代编解码器和文件格式的兼容性。作者经常提供现有软件的修改版本，以确保兼容性并解决旧版macOS的限制。每个项目都提供下载，并且通常包含源代码或应要求提供。目标操作系统版本通常为OS X 10.4至10.14，重点是OS X 10.9 (Mavericks)。

---

## 58. Supabase以20亿美元估值融资2亿美元D轮

**原文标题**: Supabase raises $200M Series D at $2B valuation

**原文链接**: [https://finance.yahoo.com/news/exclusive-supabase-raises-200-million-112154867.html](https://finance.yahoo.com/news/exclusive-supabase-raises-200-million-112154867.html)

开源应用开发平台Supabase在Accel领投的D轮融资中筹集了2亿美元，估值达20亿美元。Coatue、Y Combinator、Craft Ventures、Felicis以及著名天使投资人（如OpenAI的Kevin Weil、Vercel的Guillermo Rauch和Laravel的Taylor Otwell）也参与了本轮融资。

Accel为此进行了专门的努力，合伙人前往新西兰会见联合创始人兼首席执行官Paul Copplestone。Accel认为Supabase有潜力成为数据库层面的主导力量，支持流行的Postgres数据库系统，作为Firebase的替代方案。

Supabase旨在成为开发人员（包括使用人工智能工具的“vibe coders”）的全面后端解决方案，目前有两百万开发者使用它来管理超过350万个数据库。Vercel的首席执行官Guillermo Rauch强调了vibe coding与Supabase易于使用、易于访问的平台之间的协同作用。

Supabase成立于2020年，完全远程办公，积极培育全球社区，其很大一部分员工本身就是前创始人。该公司通过诸如发布周和全球城市线下聚会等活动来鼓励合作。“Supabase”这个名字的选择，部分原因是对Nicki Minaj歌曲“Super Bass”的戏仿。

---

## 59. 单个AI模型能推动任何科学领域的发展吗？

**原文标题**: Can a single AI model advance any field of science?

**原文链接**: [https://www.lanl.gov/media/publications/1663/1269-earl-lawrence-ai](https://www.lanl.gov/media/publications/1663/1269-earl-lawrence-ai)

无法访问文章链接。

---

## 60. 单个AI模型能否推动任何科学领域的发展？

**原文标题**: Can a single AI model advance any field of science?

**原文链接**: [https://www.lanl.gov/media/publications/1663/1269-earl-lawrence-ai](https://www.lanl.gov/media/publications/1663/1269-earl-lawrence-ai)

无法访问文章链接。

---

## 61. 家猫的复杂起源

**原文标题**: The complex origin story of domestic cats

**原文链接**: [https://phys.org/news/2025-04-complex-story-domestic-cats-tunisia.html](https://phys.org/news/2025-04-complex-story-domestic-cats-tunisia.html)

两项新大型研究挑战了先前关于欧洲家猫起源和传播的假设，表明其历史比先前认为的更为复杂和近期。两项研究都指向突尼斯作为可能的起源地。

一项由罗马第二大学领导的研究分析了来自欧洲和安纳托利亚的古代猫基因组。他们的发现表明，家猫直到公元1世纪左右才出现在欧洲，比之前认为的要晚得多。他们确定了两次引入浪潮：一次是公元前2世纪左右将非洲西北部的野猫带到撒丁岛，另一次是在罗马帝国时期引入与现代家猫品系基因相似的猫。

第二项由埃克塞特大学领导的研究分析了考古骨骼和遗传数据，得出结论认为，家猫在公元前一千年初就已经存在于欧洲，早于罗马扩张的鼎盛时期。他们还确定突尼斯为起源地。两项研究都强调了文化和宗教因素在猫的驯化和迁移中的作用，指出它们在古埃及受到崇拜，并且与希腊/罗马和挪威神话中的女神有关。

两项研究还记录了家猫对欧洲野猫种群的影响，表明由于竞争、疾病和杂交，数量有所下降。总的来说，这项研究表明，猫不仅仅是跟随早期农民而来，而是通过人类文化习俗、贸易和宗教信仰，分多个浪潮抵达欧洲，挑战了长期以来主要以共生关系为主的观点。这些研究强调了仅依靠线粒体DNA标记来理解猫科动物驯化的局限性。

---

## 62. 伦敦新建罗马巴西利卡博物馆更多细节披露

**原文标题**: More details for London's new Roman Basilica museum revealed

**原文链接**: [https://www.ianvisits.co.uk/articles/more-details-for-londons-new-roman-basilica-museum-revealed-80470/](https://www.ianvisits.co.uk/articles/more-details-for-londons-new-roman-basilica-museum-revealed-80470/)

伦敦市计划新建一座博物馆，展示罗马伦敦的历史。此前，在一座摩天大楼的施工前挖掘过程中，发现了重要的罗马巴西利卡遗址。开发商正在修改方案，将博物馆纳入大楼的地下室。

最初的开发计划包括一座位于公共大厅上方的塔楼，以及一个位于五楼的观景平台。罗马遗址的发现导致了内部的重新设计。最初计划用于设施和自行车停车的地下室，现在将容纳博物馆。这一改变需要将这些设施移至地面层，并由于混凝土核心的调整而降低塔楼的高度。

博物馆将通过电梯或楼梯从公共大厅进入。展览将以沉浸式的方式展示罗马巴西利卡遗迹及其历史背景。为了保护遗址，将在实际遗址上方安装玻璃地板，让游客可以从上方观看。还计划设置一个教育空间和一个用于展示文物的长走廊。

该博物馆与伦敦博物馆合作策划，将免费入场。博物馆的增加预计将有利于计划在大楼底层公共大厅开设的咖啡馆和餐厅。修订后的计划目前正在接受伦敦市的审查。

---

## 63. 逻辑中的惊喜 (2016)

**原文标题**: Surprises in Logic (2016)

**原文链接**: [https://math.ucr.edu/home/baez/surprises.html](https://math.ucr.edu/home/baez/surprises.html)

约翰·巴埃兹的《逻辑中的惊奇》探讨了数学证明的局限性，尤其是在复杂性方面。 文章以蔡廷不完备性定理为中心，该定理指出存在一个复杂性屏障，一个数字 L，使得我们无法证明任何特定的位串的柯尔莫哥洛夫复杂性（最短程序长度）超过 L。 文章指出，虽然任意复杂的事物存在，但证明它们的复杂性超过某个阈值是不可能的。

作者通过提供 L 的近似大小来讨论这个悖论，估计对于一个合理的编程语言和数学系统来说，L 大约是几千字节。 他提到了 Bruce Smith 的估计，并思考了一个小程序创建一个视频，描述计算的演变最终达到它本身的可能性。

巴埃兹解释了蔡廷定理的证明，强调了皮亚诺算术的作用以及程序 U 的概念，该程序 U 搜索超过给定数字的复杂性证明。 他探讨了 Smith 对用 C 实现此功能的保留意见，原因是缺乏关于机器大小的明确定义的语义。

最后，文章提到了 Kritchman-Raz 对哥德尔第二不完备性定理的证明，使用了惊喜考试悖论和蔡廷不完备性定理的严格版本。 这种方法表明，如果一个数学系统能够证明其自身的一致性，那么它实际上是不一致的。 这篇文章被简化，以使复杂的概念易于理解。

---

## 64. 美洲原住民名称延伸北美东北部地震历史

**原文标题**: Native American names extend earthquake history of northeastern North America

**原文链接**: [https://phys.org/news/2025-04-native-american-earthquake-history-northeastern.html](https://phys.org/news/2025-04-native-american-earthquake-history-northeastern.html)

地震学家约翰·埃贝尔建议结合美洲原住民的知识，特别是地名和口述历史，以扩展北美东北部有记录的地震历史，使其超出过去400年的书面记录范围。埃贝尔在美国地震学会年会上提出了他的想法，强调了更好地了解该地区地震灾害的潜力。

埃贝尔强调了一些例子，如康涅狄格州的穆杜斯（Moodus），这个名字源于阿尔冈昆语，意思是“噪音之地”，几个世纪以来，那里一直有无法解释的“巨响”报告，而现代地震学已经确定了地震群。另一个例子是波士顿附近的纳肖巴山（Mount Nashoba），在一种美洲原住民语言中，它的意思是“震动的山”，这与该地区经常发生的小地震活动相吻合。

埃贝尔提出，研究塞内卡、卡尤加、纳提克和米克马克等拥有“地震”一词的部落，可以表明其领土内频繁发生地震事件。他提倡地震学家和民族学家进行跨学科合作，分析美洲原住民的语言和叙事，从而有可能根据这些故事中的描述来估计地震烈度。通过这种合作，可以将地震记录扩展到欧洲记录的400年之外。

---

## 65. 展示一下HN：我开源了我的AI玩具公司，它基于ESP32和OpenAI实时运行

**原文标题**: Show HN: I open-sourced my AI toy company that runs on ESP32 and OpenAI realtime

**原文链接**: [https://github.com/akdeb/ElatoAI](https://github.com/akdeb/ElatoAI)

“Show HN”帖子介绍ElatoAI：一个开源AI玩具公司，由ESP32微控制器和OpenAI实时API驱动。它能够与全球定制AI代理进行实时、不间断的语音对话。

该项目由三个主要部分组成：用于代理创建和设备管理的Next.js前端，用于处理WebSocket通信和OpenAI API调用的Deno边缘服务器，以及用于音频处理和交互的ESP32 IoT客户端。主要功能包括定制代理创建、可定制的声音、安全的WebSocket、服务器端语音活动检测、Opus音频压缩和全球边缘性能。

该帖子详细介绍了DIY硬件设计，包括Supabase、Next.js前端、Deno服务器和ESP32 Arduino客户端的设置说明。它概述了技术栈、架构和PlatformIO配置。该项目具有亚秒级延迟，通过Opus编解码器实现高质量音频，以及长达10分钟的连续对话。通过安全的WebSocket、可选的API密钥加密和Supabase的身份验证和行级安全性来确保安全。

局限性包括3-4秒的冷启动、10分钟的对话限制以及ESP32上缺少语音中断检测。该项目鼓励大家贡献，重点是中断检测、Arduino IDE支持和工具调用。它以MIT许可证授权，欢迎贡献者。

---

## 66. 戴维·佟理论物理讲义

**原文标题**: David Tong Lectures on Theoretical Physics

**原文链接**: [https://www.damtp.cam.ac.uk/user/tong/books.html](https://www.damtp.cam.ac.uk/user/tong/books.html)

戴维·唐的理论物理学讲义广受欢迎，现已发展成剑桥大学出版社出版的一系列教科书。他鼓励购买这些书，尽管有免费的讲义可供使用，因为这些书提供了扩展的内容、改进的解释以及更正的细节（例如“Schwarzschild”的拼写）。值得注意的是，平装版价格实惠。目前有四本书可供选择。

这些书在物理学界广受好评。包括诺贝尔奖获得者弗兰克·维尔泽克、丽莎·蓝道尔、胡安·马尔达西纳、内森·塞伯格、桑迪普·特里维迪、肖恩·卡罗尔和拉杰什·戈帕库马尔等著名物理学家都给予了高度评价。他们称赞唐清晰、引人入胜的写作风格，他传达技术细节和基本原理的能力，以及这些书对本科生和研究生课程的全面覆盖。一些评论员将这些书与经典的朗道和栗弗席兹系列相提并论，认为唐的书籍可能同样具有影响力，对物理学家来说必不可少。评论强调了这些书提供指导、洞察力、乐趣以及揭示物理概念之间相互联系的能力。

---

## 67. 停用脸书和照片墙对用户情绪状态的影响

**原文标题**: The effect of deactivating Facebook and Instagram on users' emotional state

**原文链接**: [https://www.nber.org/papers/w33697](https://www.nber.org/papers/w33697)

停用Facebook和Instagram对用户情绪状态的影响
NBER工作论文《停用Facebook和Instagram对用户情绪状态的影响》研究了社交媒体停用对情绪健康的影响。该研究通过2020年美国大选前的两项大型随机实验进行，发现停用Facebook六周会导致衡量幸福感、抑郁和焦虑的指标比仅停用一周的对照组提高0.060个标准差。同样，停用Instagram六周导致该指标提高0.041个标准差。

探索性分析表明，Facebook停用的积极影响在35岁以上的人群中更为明显，而Instagram停用的积极影响主要在25岁以下的女性中观察到。

值得注意的是，该论文包含了大量的致谢和披露信息，表明许多作者通过以往的雇佣关系、咨询工作、研究经费、酬金、参加活动或股票所有权与Meta（Facebook的母公司）有关联。这引发了关于研究结果潜在的利益冲突考量。

---

## 68. Show HN: 持久化 Python 工作流

**原文标题**: Show HN: Durable Python Workflows

**原文链接**: [https://github.com/autokitteh/autokitteh](https://github.com/autokitteh/autokitteh)

AutoKitteh是一个工作流自动化和编排的开发者平台，提供了一种基于代码的替代方案，以取代无代码/低代码解决方案。它构建于Temporal之上，简化了Python、Starlark以及即将推出的JavaScript中的持久性工作流执行，抽象掉了许多底层基础设施的复杂性。它可以自托管或用作托管云iPaaS（目前处于测试阶段）。

主要功能包括可扩展的“无服务器”平台、API优先架构（gRPC/HTTP）以及与Slack、GitHub、Twilio、ChatGPT、Gemini和Gmail等服务的内置集成。

AutoKitteh处理构建可靠且可扩展的工作流的复杂性，使开发人员能够专注于业务逻辑。它提供安全API集成、用户友好的管理和调试、无状态丢失的自动恢复、内置持久性以及大规模部署准备等功能。

该平台提供CLI、VS Code扩展程序和Web UI来管理工作流。快速入门指南概述了如何开始，涵盖安装、服务器设置、项目创建和弹性演示。

开源的AutoKitteh服务器专为自托管环境而设计。要了解有关云iPaaS测试版的更多信息，用户可以联系meow@autokitteh.com。文档中详细说明了构建说明和要求。

---

## 69. Verus：用于底层系统代码的验证Rust

**原文标题**: Verus: Verified Rust for low-level systems code

**原文链接**: [https://github.com/secure-foundations/verus](https://github.com/secure-foundations/verus)

Verus 是一个工具，它使开发者能够通过编写规范来验证 Rust 代码的正确性，然后 Verus 使用强大的求解器静态地检查这些规范。这确保了代码始终满足规范，而无需运行时检查。虽然 Verus 支持 Rust 的一个子集，但它扩展了验证能力，尤其是在涉及原始指针的底层系统代码方面。

Verus 目前正在积极开发中，可能存在损坏或缺失的功能，且其文档尚不完整。我们鼓励用户在 Zulip 频道上寻求帮助。尽管 Verus 还在不断开发中，但它已被用于各种行业和学术项目中，并发表了相关的研究论文。

要开始使用，用户可以通过 Verus Playground 在浏览器中尝试 Verus，或者安装它以进行更复杂的开发。文档包括一个教程、API 文档和一个用于验证并发代码的指南。出版物、项目、教程材料和示例等资源可用于展示 Verus 的实际应用。

我们欢迎对 Verus 的贡献，用户可以在 GitHub 上报告问题或发起讨论，或者加入 Zulip 频道以获得实时帮助。Verus 使用 GitHub 讨论来处理功能请求，并使用 GitHub 问题来处理可操作的错误。该项目感谢 Zulip 赞助免费托管，并感谢 Johanna Polzin 对 Verus 徽标设计的贡献。

---

## 70. IAM角色信任策略：明目张胆的错误配置

**原文标题**: IAM Role Trust Policies: Misconfigurations Hiding in Plain Sight

**原文链接**: [https://www.token.security/blog/iam-role-trust-policies-misconfigurations-hiding-in-plain-sight](https://www.token.security/blog/iam-role-trust-policies-misconfigurations-hiding-in-plain-sight)

这篇博文强调了AWS中IAM角色信任策略经常被忽视且容易配置错误的特性，认为它们是权限提升风险的重要来源。作者指出，缺乏关于信任策略的清晰和全面的文档是导致这些配置错误的一个因素。该文章指出了两个常见且危险的错误：

1.  **信任角色账户内的所有主体：** 在信任策略中使用`arn:aws:iam::<account_id>:root`实际上授予了该账户内的 *任何* IAM主体（用户、角色、Lambda函数等）承担该角色的能力，绕过了限制访问的意图。如果攻击者获得账户中任何具有`sts:AssumeRole`权限的身份的访问权限，这将创建一个简单的权限提升路径。

2.  **假定多个主体之间是AND关系：** 当在同一“Principal”部分中组合不同的主体类型（例如，AWS账户和某个服务主体）时，AWS会将它们评估为逻辑OR，而不是AND。这意味着 *任何一个* 主体都可以独立承担该角色。例如，错误地认为信任策略仅允许特定账户中的EC2实例承担角色，而实际上它允许本地账户中的 *任何* EC2实例 *或* 指定账户中的 *任何* 主体承担该角色。

该文章强调，这些细微的错误可能会产生严重的安全性影响，并倡导更好地理解信任策略的细微差别，以正确保护IAM角色。作者承诺后续文章将重点关注跨账户信任关系中的常见错误。

---

## 71. 养成一个新习惯需要多久？(2015)

**原文标题**: How long does it take to create a new habit? (2015)

**原文链接**: [https://thelogicaloptimist.com/index.php/2015/10/25/the-21-day-myth-create-new-habit/](https://thelogicaloptimist.com/index.php/2015/10/25/the-21-day-myth-create-new-habit/)

本文（2015年）驳斥了广为流传的“养成一个新习惯需要21天”这一说法，并引用了发表在《欧洲社会心理学杂志》上的研究成果来证明其谬误。尽管“21天”的说法源于马克斯韦尔·马尔茨医生的观察，但它并非基于研究，且该说法常常被简化。

Lally等人发表的“习惯是如何形成的”的研究对96人进行了12周的跟踪，结果表明习惯的形成是一个更长的过程，从2个月到8个月不等，平均为66天。持续时间取决于习惯、个人及其所处环境。

重要的是，该研究发现，错过一次执行新行为的机会并不会显著阻碍习惯的形成过程。

作者反对固守像“21天规则”甚至“66天平均时间”这样的严格时间表。他们强调，个人经历各不相同，而对渴望改变的投入才是最重要的因素。作者建议关注习惯改变背后的“原因”，认为个人承诺和对自身行为的控制比坚持特定时间框架更重要。最终，培养新习惯应该由个人动机驱动，而不是任意设定的截止日期。

---

## 72. 委员会认定苹果和Meta违反《数字市场法》

**原文标题**: Commission Finds Apple and Meta in Breach of the Digital Markets Act

**原文链接**: [https://ec.europa.eu/commission/presscorner/detail/en/ip_25_1085](https://ec.europa.eu/commission/presscorner/detail/en/ip_25_1085)

欧盟委员会初步认定苹果和Meta违反了《数字市场法案》(DMA)，这是一项旨在遏制科技巨头市场力量的欧盟里程碑式法律。尽管具体细节仍在浮出水面，仍需进一步调查，但初步调查结果表明，苹果和Meta未能充分遵守DMA的要求。

DMA的重点是防止“看门人”（占主导地位的在线平台）从事反竞争行为。对苹果和Meta提出的具体违规指控可能与这些核心原则有关。例如，苹果可能被认定为限制应用程序开发者与用户自由沟通以及在App Store之外提供替代支付选项的能力。Meta的潜在违规行为可能涉及不公平的数据使用行为或限制与竞争性社交媒体平台的互操作性。

如果欧盟委员会最终认定苹果和Meta违反了DMA，它们可能面临巨额罚款，包括高达其全球年度营业额10%的罚款。更重要的是，它们可能被迫对其商业行为进行重大调整，以确保数字市场中的公平竞争和用户选择。调查仍在进行中，两家公司都有机会回应欧盟委员会的初步调查结果并为其辩护。这代表了欧盟监管大型科技公司并促进更具竞争力的数字环境方面迈出的重要一步。

---

## 73. 关税冲击电子产品的多重方式

**原文标题**: The many ways tarrifs will hit electronics

**原文链接**: [https://spectrum.ieee.org/tariffs-electronics-prices](https://spectrum.ieee.org/tariffs-electronics-prices)

关税冲击电子产品的多种方式：专访IPC首席经济学家肖恩·杜布拉瓦克

本文《关税冲击电子产品的多种方式》刊登于IEEE Spectrum，2025年4月16日。文章专访了IPC首席经济学家肖恩·杜布拉瓦克，探讨关税对消费电子行业的影响。专访预计将讨论关税影响电子产品生产和定价的多个方面。

虽然文章预览未提供关税影响电子产品的具体细节，但预示着访谈可能探讨以下内容：

*   **成本增加：** 关税作为对进口商品的税收，直接增加了零部件和成品的价格。
*   **供应链中断：** 关税会扰乱既定的供应链，迫使公司寻找替代来源或迁移生产。
*   **对消费者的影响：** 成本增加可能会以电子设备价格上涨的形式转嫁给消费者。
*   **竞争格局：** 关税会改变竞争格局，可能有利于国内生产商或位于未受关税影响的国家的公司。
*   **经济后果：** 还可能讨论更广泛的经济后果，例如贸易和投资减少。

本次专访旨在深入了解关税将如何重塑电子行业。

---

## 74. 亚特兰蒂斯真相 (2019)

**原文标题**: The Truth about Atlantis (2019)

**原文链接**: [https://talesoftimesforgotten.com/2019/03/26/the-truth-about-atlantis/](https://talesoftimesforgotten.com/2019/03/26/the-truth-about-atlantis/)

本文旨在驳斥关于亚特兰蒂斯存在的普遍说法，指出相当比例的美国人相信这个失落的文明。文章论证亚特兰蒂斯纯属虚构，起源于柏拉图的对话录，特别是《蒂迈欧篇》和《克里提亚斯篇》。

文章解释说，柏拉图通过克里提亚斯这个人物引入了亚特兰蒂斯的故事，克里提亚斯声称是从梭伦那里听说的，而梭伦又是从埃及祭司那里听说的。这个故事将亚特兰蒂斯描述为一个强大的岛国，它曾袭击欧洲和亚洲，最终被地震和洪水摧毁。

作者驳斥了柏拉图不会编造这种故事的观点，强调他倾向于使用虚构叙事来阐明哲学观点，并引用了《理想国》和《会饮篇》中的例子。他们认为，亚特兰蒂斯的故事与其他归因于柏拉图的虚构故事有着主题上的相似之处，例如都设定在极其古老的时代。

此外，作者质疑柏拉图所谓的信息来源的可信度。故事由三十僭主之一，一个残酷的寡头政权的成员克里提亚斯叙述，这引发了对其历史准确性的质疑。对话录的叙事背景也可能是虚构的。作者的结论是，对亚特兰蒂斯的信仰之所以持续存在，是因为它具有浪漫的吸引力，尽管它显然是柏拉图想象力的产物。

---

## 75. 攻击我房东的锅炉

**原文标题**: Attacking My Landlord's Boiler

**原文链接**: [https://blog.videah.net/attacking-my-landlords-boiler/](https://blog.videah.net/attacking-my-landlords-boiler/)

本文详细介绍了作者远程控制房东锅炉的项目，旨在克服现有温控器的局限性。由于对供暖不均和缺乏自动化感到沮丧，作者利用温控器和锅炉之间现有的无线电通信绕过了房东批准和电工的需求。

最初，作者研究了温控器的型号，发现它在 868MHz 范围内通信。在使用更便宜的微控制器逆向工程协议失败后，他们选择了“重放攻击”，记录并重新广播温控器的信号以直接控制锅炉。

他们使用 RTL-SDR 可视化无线电数据包，并使用 HackRF One（一款廉价购买的克隆产品）来传输记录的“开启”和“关闭”信号。通过记录温控器发送的信号，他们能够使用 HackRF“喊回去”命令，并打开和关闭锅炉。

然后，作者通过创建一个简单的 Web 服务器并使用 `curl` 命令发送记录的信号，将 HackRF 与他们的 Home Assistant 服务器集成。这使得他们能够根据房间温度、睡眠时间表和位置等因素自动控制供暖。

尽管作者认为 HackRF 对于一个简单的开关来说过于强大，但他们优先考虑了功能和可靠性。他们现在能够远程和自动控制他们公寓的供暖。最后，该博客解释了英国的《在线安全法案》以及作者决定删除评论区以避免潜在的灾难性罚款。

---

## 76. 展示HN: Dosidicus – 一款拥有简单神经网络的电子宠物

**原文标题**: Show HN: Dosidicus – A digital pet with a simple neural network

**原文链接**: [https://github.com/ViciousSquid/Dosidicus](https://github.com/ViciousSquid/Dosidicus)

Dosidicus：一款结合了简单神经网络的电子宠物“拓麻歌子”，使其能够学习并适应行为。这个开源于GitHub的研究项目，专注于神经网络和赫布学习的可视化与理解。该鱿鱼基于其需求（饥饿、困倦等）自主做出决策，并使用模拟的视觉锥体寻找食物。

其核心的神经网络使鱿鱼能够形成关联，并通过赫布学习调整权重。存储在短期和长期记忆中的经验也在决策中发挥作用。有趣的是，Dosidicus甚至可以根据环境生成新的神经元（神经发生）。

该项目包含一个全面的需求管理系统，追踪饥饿、困倦、快乐和清洁度等影响鱿鱼健康的因素。忽视这些需求会导致生病和死亡。此外，Dosidicus具有七种影响其行为的性格类型，并允许用户使用装饰品自定义环境。调试工具可用于直接查看和编辑鱿鱼的内部状态。

---

## 77. Pike – 一种语法类似于 Java 和 C 的动态编程语言

**原文标题**: Pike – a dynamic programming language with a syntax similar to Java and C

**原文链接**: [https://pike.lysator.liu.se/](https://pike.lysator.liu.se/)

本文介绍 Pike，一种具有 Java 和 C 类似语法的动态编程语言，它易于学习、数据处理速度快，并且由于其强大的内置数据类型而能够快速执行。它在 GNU GPL、GNU LGPL 和 MPL 许可下发布，几乎可以免费用于任何用途。

最新消息包括宣布将于 2025 年第一季度和第二季度在瑞典林雪平举行 Pike 开发者聚会。同时宣布发布 Pike 8.0 release 16（构建版本 8.0.1956），其源代码和适用于 MacOS、Linux 和 Windows 的二进制构建版本均可供下载。此外，Pike 2024 大会于 11 月初在林雪平举行。最后，宣布发布 Pike 9.0.9 Beta，即 Pike 9.0 系列的第二个 Beta 版本，旨在成为下一个稳定版本，并提供下载发行版的链接。

---

## 78. 101个基本电脑游戏

**原文标题**: 101 BASIC Computer Games

**原文链接**: [https://github.com/maurymarkowitz/101-BASIC-Computer-Games](https://github.com/maurymarkowitz/101-BASIC-Computer-Games)

本文档介绍了一系列来自1975年由Digital Equipment Corp.出版的David Ahl著作《101个BASIC电脑游戏》一书中的BASIC电脑游戏程序。需要注意的是，本合集与Ahl所著的更为著名的《BASIC电脑游戏》（BCG）一书*不同*，包含几个独特的游戏。

本文档重点介绍了该书中使用的BASIC方言的多样性。代码跨越了不兼容的版本，包括Dartmouth BASIC、HP BASIC、BASIC-PLUS和EduSystem BASIC。由于通常未指定，因此识别每个游戏的正确方言是一项挑战。

本合集是早期BASIC编程风格的一个宝贵例子，展示了语法、语句分隔和速记命令的差异。这些程序使用OCR和AI工具进行转换，由于原书的良好印刷质量，错误相对较少。

创建本合集的主要动机是为改进RetroBASIC提供示例代码，旨在使这些程序无需修改即可正确运行。

本文档提供了游戏的详细列表，包括游戏名称、描述、在书中的页码以及可能使用的BASIC方言。游戏涵盖了广泛的类型，从NIM和CHECKR等策略游戏到HMRABI和STOCK等模拟游戏，再到SLOTS和GUNNER等简单的街机游戏。这种多样性强调了早期电脑游戏开发者的智慧。

---

## 79. Libro：一个用于追踪书籍的命令行工具

**原文标题**: Libro: a command-line tool to track your books

**原文链接**: [https://github.com/mkaz/libro](https://github.com/mkaz/libro)

Libro是一个命令行工具，旨在追踪你的阅读历史，并将数据本地存储在SQLite数据库中。它提供添加书籍(`libro add`)、按年份显示已读书籍(`libro show --year` 或 `libro report`)、按ID显示书籍详情(`libro show`)，以及按年份或作者生成阅读习惯报告(`libro report --author`)等命令。该工具以格式化的表格和条形图形式呈现这些数据。

Libro支持从Goodreads导出CSV文件导入阅读历史。首次运行时，Libro会在一个由以下优先级决定的位置创建一个`libro.db`文件：命令行`--db`标志、当前目录、`LIBRO_DB`环境变量或平台的data目录。

数据库模式包含一个`Books`表，其中包含ID、标题、作者、页数、出版年份和类型（小说/非小说）等字段，以及一个`Reviews`表，其中包含ID、书籍ID、阅读日期、评分和评论等字段。

可以通过`pip install libro-book`或克隆GitHub仓库并使用`pip install -e .`来完成安装。

---

## 80. 强化学习能否激励大语言模型产生超出基础模型的推理能力？

**原文标题**: Does RL Incentivize Reasoning in LLMs Beyond the Base Model?

**原文链接**: [https://limit-of-rlvr.github.io/](https://limit-of-rlvr.github.io/)

杨越正在研究如何激励大型语言模型（LLMs）和多模态大型语言模型（MLLMs）进行推理。他的研究重点包括：

*   **开发激励推理的新范式：** 他正在探索鼓励LLMs/MLLMs更有效推理的新方法。
*   **广义世界模型：** 他致力于创建能够更好地理解和表示周围世界的模型。
*   **视觉语言对齐（VLA）的泛化：** 他的目标是改进LLMs连接视觉和文本信息的方式，使其更具鲁棒性和适应性。

杨越积极寻求与以下公司内的合作者：

*   **提供基础研究的自由：** 他渴望能够深入研究具有挑战性的基础问题。
*   **拥有丰富的资源：** 他需要获得必要的计算能力、数据和专业知识。
*   **具有强大的技术氛围：** 他重视与才华横溢的研究人员共事的环境。

他还对博士访问感兴趣。 这篇文章本质上是一份合作邀约，概述了他的研究兴趣和他所寻求的环境。

---

## 81. 让智能自行车变笨，让它重新运转

**原文标题**: Making a smart bike dumb so it works again

**原文链接**: [https://francisco.io/blog/making-a-smart-bike-dumb-work-again/](https://francisco.io/blog/making-a-smart-bike-dumb-work-again/)

弗朗西斯科继承了一辆带灯的“智能”自行车，但灯只能通过应用程序控制，而该公司已经破产，导致该应用程序毫无用处。他最初使用了一个廉价的、容易被盗的、商店购买的车灯。为了让自行车自带的灯重新亮起来，他决定自己动手破解。

他的目标是：避免永久性损坏、利用他的3D打印机、保留现有的灯、升级到USB-C充电、使组件更换变得容易，以及防止火灾隐患。他在自行车车架内找到了内部电池和灯的连接器。然后，他购买了一个用于3.7V锂聚合物电池的USB-C充电板，该充电板带有电池和负载的连接器。

他将电线焊接到现有的灯连接器和充电板上，创建了一个新的电路。这个新电路被放置在一个定制的3D打印外壳中。为了提高安全性，他用热缩管包裹了所有裸露的连接，用胶带固定了连接器，并增加了一个电阻。

这个破解方案将前后灯连接起来，现在只需按一下按钮即可同时激活前后灯。改装后的自行车现在可以通过USB-C充电。弗朗西斯科得出结论，有时最简单的解决方案就是最好的。

---

## 82. 第五巡回法院免除AT&T重大位置数据隐私违规责任

**原文标题**: 5th Circuit Lets AT&T Off the Hook for Major Location Data Privacy Violations

**原文链接**: [https://www.techdirt.com/2025/04/23/5th-circuit-obediently-lets-att-off-the-hook-for-major-location-data-privacy-violations/](https://www.techdirt.com/2025/04/23/5th-circuit-obediently-lets-att-off-the-hook-for-major-location-data-privacy-violations/)

本文批评第五巡回法院的一项判决，该判决实际上免除了AT&T对重大位置数据隐私侵犯的责任。作者表达了强烈的愤世嫉俗，认为考虑到AT&T长期以来被指控剥削美国公民的历史，以及政府多年来似乎对此行为的纵容甚至经济奖励，这一结果并不令人意外。文章暗示AT&T的行为模式在损害公民利益的同时，获得了政府的批准和经济激励。核心要点是对法律和监管体系的失望和不信任，这些体系被认为正在保护AT&T的利益，而牺牲了个人隐私。

---

## 83. 高级Python特性

**原文标题**: Advanced Python Features

**原文链接**: [https://blog.edward-li.com/tech/advanced-python-features/](https://blog.edward-li.com/tech/advanced-python-features/)

本文重点介绍14个超越常见技巧的高级Python特性，旨在通过探索被低估和“非Python式”的技术来提升Python代码。

1. **类型重载:** 使用`@overload`定义多个函数签名，根据参数类型增强类型检查，并确保特定返回类型。

2. **仅关键字和仅位置参数:** 使用`*`控制仅关键字参数，`/`控制仅位置参数，提高API清晰度。

3. **未来注解:** 探讨Python类型系统的历史以及`from __future__ import annotations`如何推迟类型评估，解决前向引用问题。

4. **泛型:** Python 3.5引入并在3.12中改进的泛型，为类和函数启用类型参数化，增强类型安全性和代码可重用性。

5. **协议:** 使用协议实现结构子类型（鸭子类型），定义期望的行为，无论类型如何，从而改进类型检查。

6. **上下文管理器:** 使用`contextlib.contextmanager`简化资源管理，为`with`代码块定义设置和清理代码。

文章承诺在完整版本中详细介绍另外8个高级Python特性。

---

## 84. 展示一下：我做了一个能把GitHub代码库变成简易教程的AI

**原文标题**: Show HN: I built an AI that turns GitHub codebases into easy tutorials

**原文链接**: [https://github.com/The-Pocket/Tutorial-Codebase-Knowledge](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge)

此“Show HN”帖子介绍了一个AI工具，它能从GitHub代码库自动生成初学者友好的教程。该AI基于一个100行的LLM框架Pocket Flow构建，通过爬取代码库，分析其代码，识别核心抽象，然后生成带有可视化的完整教程。

帖子强调了该AI分析复杂代码并创建易懂解释的能力。它提供了针对AutoGen、Celery、FastAPI和NumPy等热门代码库的AI生成教程示例。

帖子包含了如何使用该工具的说明。用户可以克隆代码库，安装依赖项，配置LLM API密钥（最好是Gemini Pro 2.5或类似版本），并运行`main.py`脚本来生成教程。该脚本可以分析GitHub存储库URL或本地目录。参数允许指定文件包含/排除、最大文件大小和输出语言。

作者还提到使用“Agentic Coding”和Pocket Flow，暗示了一种快速开发模式，其中AI代理（如Cursor AI）根据人类设计处理编码任务。帖子链接了一个YouTube教程，其中包含了更详细的循序渐进的开发指南。

---

## 85. Parcom：CL解析器组合子

**原文标题**: Parcom: CL Parser Combinators

**原文链接**: [https://github.com/fosskers/parcom](https://github.com/fosskers/parcom)

`parcom` 是一个简洁的 Common Lisp 库，用于使用解析器组合子创建解析器，其灵感来源于 Haskell 的 `parsec` 和 Rust 的 `nom`。它处理字符串，提供“零拷贝”子字符串提取，并且没有外部依赖。

该库提供了用于字符（`char`、`any`、`anybut`、`hex`、`eof`）、字符串（`string`）、数字（`unsigned`、`integer`、`float`）和空白字符（`newline`、`space`、`multispace`）的基本解析器。它还包括用于批量输入消耗的工具，如 `take`、`take-while` 和 `rest`。

`parcom` 的关键在于它的组合子，它们组合解析器以实现复杂的逻辑。这些组合子包括：`*>`、`<*`、`<$>`、`<$`、`alt`、`opt`、`between`、`many`、`sep`、`sep-end`、`skip`、`consume`、`peek`、`count` 和 `recognize`。这些组合子促进顺序解析、替代解析、可选解析和重复解析等功能。

`parcom` 提供了诸如 `empty?`、`digit?`、`fmap` 和 `const` 等实用程序。它还在可选的 `parcom/json` 系统中提供了一个 JSON 解析器，提供 `parse` 和 `json` 函数，以及 JSON 和 Lisp 数据结构之间的转换规则。

该文档指导用户编写自定义解析器，详细介绍了如何创建基本解析器、参数化解析器以及如何处理失败。该库旨在实现表达性和轻量级使用，以大约 10mb/s 的速度解析 JSON。

---

## 86. 易峰：E-ink 电子墨水屏 IBM XT 兼容机，电池续航 100+ 小时

**原文标题**: Evertop: E-ink IBM XT clone with 100+ hours of battery life

**原文链接**: [https://github.com/ericjenott/Evertop](https://github.com/ericjenott/Evertop)

Evertop：一款便携式、低功耗的IBM XT克隆机，专为极致电池续航而设计。它由ESP32微控制器驱动，模拟80186处理器，拥有1MB RAM，运行DOS、Minix和Windows 3.0及以下版本。其电子墨水屏和双10,000mAh电池，结合节能措施，单次充电可使用数百至数千小时，并配有内置太阳能板，可实现无限期的离网运行。

它配备了众多功能，包括内置且可拆卸的键盘、PS/2键盘/鼠标端口、完整的CGA/Hercules/MCGA图形支持、部分EGA/VGA支持、多种音频输出选项、串口、USB闪存盘端口、RJ45以太网、WiFi和LoRA无线电。蓝牙也已配备，用于未来的功能。

该设备提供多种充电选项：太阳能板、直流输入和Micro USB。它具有电压表，便于监控。它还提供用户启动或自动休眠到磁盘以及自动完全断电功能。

存储通过SD卡提供（已测试高达256GB），能够挂载多个软盘和硬盘映像。外壳采用3D打印。

一款更小、更具成本效益的版本“Evertop Min”删除了某些功能（键盘、太阳能板、以太网、可变电压充电、LoRA、电压表、一半的电池容量），以减小尺寸、重量和成本，同时保留了核心功能，如电子墨水屏、PS/2端口、内置扬声器、USB闪存盘端口、WiFi、蓝牙、TTL串口以及相同的固件。

文章还包含了大量示例视频和图像，展示了Evertop运行各种软件并演示其功能。

---

## 87. 约翰福音彩绘本

**原文标题**: The Illuminated Gospel of St John

**原文链接**: [https://www.cambridge.org/universitypress/bibles/illuminated-gospel-of-st-john](https://www.cambridge.org/universitypress/bibles/illuminated-gospel-of-st-john)

无法访问文章链接。

---

## 88. Prolog冒险游戏

**原文标题**: Prolog Adventure Game

**原文链接**: [https://github.com/stefanrodrigues2/Prolog-Adventure-game](https://github.com/stefanrodrigues2/Prolog-Adventure-game)

本文介绍了一款基于Prolog的冒险游戏，玩家的目标是在城堡内找到隐藏的宝藏。该游戏融合了经典的冒险游戏机制，创造引人入胜的体验。玩家以三条生命开始，必须在城堡中导航，解决谜题，并管理资源才能成功。

提到的主要特点包括：

*   **目标：** 找到隐藏的宝藏。
*   **语言：** 用Prolog实现。
*   **生命：** 玩家有三条生命。
*   **游戏机制：** 游戏具有交互式元素，例如锁着的门、隐藏的物品、需要完成的不完整物品、必须管理的有限资源以及物品栏系统。

该游戏旨在利用Prolog的逻辑编程能力，提供互动且具有挑战性的冒险体验。

---

## 89. 天文学家证实存在孤立黑洞

**原文标题**: Astronomers confirm the existence of a lone black hole

**原文链接**: [https://phys.org/news/2025-04-astronomers-lone-black-hole.html](https://phys.org/news/2025-04-astronomers-lone-black-hole.html)

天文学家确认了孤立黑洞的存在，这是此前未实现的壮举，原因是在没有伴星的情况下很难探测到。空间望远镜科学研究所的一个团队，利用哈勃和盖亚空间探测器的数据，证实了最初于2022年发现的“暗物质”确实是一个黑洞。

该天体位于人马座，最初的发现是由于其引力透镜效应，当它经过前方时，放大了远处背景恒星的位置并使其发生偏移。2011-2017年的早期观测结果得到了2021-2022年数据的补充。

最初，第二个研究团队提出该天体是一颗中子星，但他们在2023年修改了评估，同意最初的团队认为它是一个黑洞。最新的分析显示该天体大约是太阳质量的七倍，明确排除了中子星的可能性。这一确认标志着首次直接识别出孤立黑洞。研究人员计划使用计划于2027年发射的南希·格雷斯·罗曼太空望远镜来寻找更多的孤立黑洞。该研究结果发表在《天体物理学杂志》上。

---

## 90. 差异的价值：詹妮弗·林赛谈翻译的关注

**原文标题**: The Value of Differences: Jennifer Lindsay on Noticing Translation

**原文链接**: [https://sydneyreviewofbooks.com/essays/the-value-of-differences](https://sydneyreviewofbooks.com/essays/the-value-of-differences)

这段短文强调了布克奖和国际布克奖在认可和推广世界一流小说给英语读者方面的互补作用。布克奖侧重于最初用英语创作的小说，而国际布克奖则表彰翻译成英语的小说。这种对称的结构确保了原创英语作品和翻译成英语的作品都能获得重要的认可，并接触到更广泛的读者。本质上，这两个奖项加在一起，提供了对文学卓越性的全球视角。

---

## 91. 用于检测所有类型电离辐射的手持式探测器，提高辐射安全性

**原文标题**: Handheld detector for all types of ionizing radiation improves radiation safety

**原文链接**: [https://phys.org/news/2025-04-handheld-detector-ionizing-safety.html](https://phys.org/news/2025-04-handheld-detector-ionizing-safety.html)

于韦斯屈莱大学和芬兰辐射与核安全局(STUK) 联合开发了一种新型手持式多用途辐射探测器，可以探测所有四种类型的电离辐射：α射线、β射线、γ射线和中子辐射。这种辐射探测器的“瑞士军刀”通过将多种探测功能整合到一个轻巧（2公斤以下）的设备中，提高了安全性并简化了现场工作。

该探测器采用多层Phoswich技术，结合了五种不同的闪烁层，每层都充当独立的辐射探测器。这使得能够探测α射线和β射线造成的表面污染，对发射伽马射线的材料进行定向感应（对于这种尺寸的设备来说是一项新颖的功能），以及探测中子辐射，这对于识别含有钚的核材料至关重要。

该设备具有用于实时监控的集成屏幕，并且电池可以提供大约2小时的连续使用时间。它的通用应用领域包括工业、医疗、监管、核能、急救人员和军事用户。 该技术已获得专利，于韦斯屈莱大学正在积极寻找商业合作伙伴进行商业化，并计划开发更广泛的辐射探测仪器系列。这项研究发表在《核仪器与方法物理研究A部分》上。

---

## 92. 围棋中的死里逃生

**原文标题**: Cheating the Reaper in Go

**原文链接**: [https://mcyoung.xyz/2025/04/21/go-arenas/](https://mcyoung.xyz/2025/04/21/go-arenas/)

本文探讨了在Go中实现手动内存管理与垃圾回收（GC）协作的可能性，特别是构建一个非类型化的arena分配器。作者认为，尽管Go官方不支持这种做法，但该语言的设计以及对向后兼容性的承诺使其成为可行方案。

文章强调了在arena中分配包含指针的内存所面临的挑战。Go GC依赖于元数据（“指针位”）来识别已分配内存中的指针。最初设计的arena的`Alloc`方法不提供这种形状信息，导致arena中分配的指针被过早地垃圾回收。

为了解决这个问题，作者提出了一种策略：确保持有`Alloc`返回的任何指针都能够阻止整个arena被垃圾回收。如果arena本身被GC标记为“存活”，那么它管理的所有内存，包括其中的指针，也会被保持存活。这种方法利用了一个事实，即如果存储在arena中的数据需要被引用，那么整个arena的生命周期必须被保留。

文章提供了一个基准测试，比较了arena分配器与Go标准`new`函数的性能，显示出显著的性能提升，特别是对于较大的对象。核心思想是以这样一种方式设计arena，即只要它分配的任何东西也被认为是存活的，GC就认为它是存活的。

---

## 93. 通过线上唱歌，孤独的年长者找到了快乐和联系。

**原文标题**: Isolated older adults find joy and connection through virtual singing

**原文链接**: [https://news.northwestern.edu/stories/2025/04/virtual-singing-brings-connection-and-joy-to-isolated-older-adults-study-finds/](https://news.northwestern.edu/stories/2025/04/virtual-singing-brings-connection-and-joy-to-isolated-older-adults-study-finds/)

孤寡老人通过线上歌唱找到快乐和联系

---

## 94. 检测C语言表达式是否为常量

**原文标题**: Detecting if an expression is constant in C

**原文链接**: [https://nrk.neocities.org/articles/c-constexpr-macro](https://nrk.neocities.org/articles/c-constexpr-macro)

本文探讨了使用多种C宏实现方法，在编译时检测并验证常量表达式。目标是创建一个宏`C(x)`，该宏确保`x`是一个常量表达式，如果不是则抛出编译错误，并“返回”`x`的值（理想情况下保持原始类型）。

文中提出了几种方法，每种方法都有其优缺点：

*   **C23 `constexpr` 复合字面量：** 利用新的 C23 特性来强制执行对存储期初始化器的常量表达式要求，同时保留类型。缺点是编译器支持有限。
*   **`__builtin_constant_p`：** 利用 GNU 扩展来检查常量表达式，并使用 `__builtin_choose_expr` 和 `error` 属性触发编译错误。缺点：需要 GNU 扩展。
*   **`static_assert`：** 在结构体内部使用 `static_assert` 来验证常量表达式，但可能由于隐式转换而改变类型。
*   **sizeof + 具有数组类型的复合字面量：** 采用复合字面量中的变长数组来检测非常量表达式。类似于 `static_assert`，但早于 C11；它也会改变类型，并且不支持浮点表达式。
*   **sizeof + 枚举常量：** 使用枚举常量的要求来检查常量表达式，但存在“泄漏”枚举名称的问题，这可以通过在函数参数内部声明枚举来缓解（尽管这会生成警告）。
*   **逗号运算符：** 将 `sizeof` 与逗号运算符结合使用，以确保类型保留，但会生成“未使用”警告（通过将 `sizeof` 结果强制转换为 `void` 来解决）。

本文强调了在强制执行常量表达式要求的同时，保持原始类型并避免编译器警告的挑战。作者分享了对 GCC 行为的见解，并强调了为库的使用创建无警告宏的重要性。还提到了读者提交的关于使用 `_Generic` 处理整数常量表达式的解决方案。

---

## 95. 加入W3C探索兴趣组：标准由此启航

**原文标题**: Join the W3C Exploration Interest Group: where standards start

**原文链接**: [https://www.w3.org/blog/2025/join-the-w3c-exploration-interest-group-where-standards-start/](https://www.w3.org/blog/2025/join-the-w3c-exploration-interest-group-where-standards-start/)

W3C探索兴趣小组（IG）是Web上身份、认证和信任的早期研发实验室。与定义规范性规范的工作组不同，探索IG专注于将现实世界的挑战与标准世界联系起来，并在开发解决方案之前提出关键问题。

该小组致力于解决浏览器实现与Web规范之间的差距，探索新兴的钱包模型、身份凭证和联合流程。它还考虑跨多个信任框架、行业或司法管辖区的使用案例，识别碎片化风险，并评估需要技术响应的监管信号。

IG鼓励实施者、研究人员、政策制定者以及任何遇到Web开发问题的人参与。欢迎通过其公共GitHub存储库进行贡献。目标是发现被忽视的问题，并搭建可能导致未来工作组章程的桥梁。该小组每两周举行一次会议，重点讨论社区提出的议题，邀请提问，并促进合作。

---

## 96. 欢迎来到我们的1963年BBC MCR21 OB转播车网站

**原文标题**: Welcome to our website for the 1963 BBC MCR21 OB Van

**原文链接**: [https://mcr21.org.uk/](https://mcr21.org.uk/)

本网站提供有关1963年BBC MCR21 OB转播车的资料，重点介绍其技术方面和历史意义。MCR21由Pye公司建造，是十辆“主力扫描车”之一，代表了黑白户外转播技术的重大进步，为未来的彩色设备奠定了基础。

本网站重点介绍了该转播车的几个关键领域：

*   **声音系统：** 音频控制台配备了20通道混音器，具有三个群组、PA输出和广泛的监听功能。它具有平坦的响应，并且可以在电源故障时恢复为电池供电。工程经理拥有一张办公桌，配备15线手动电话交换机和对讲设施。

*   **监视器堆栈：** 七个监视器被认为是足够的，包括单独的摄像机监视器、工程和制作预览以及中央17英寸传输监视器。每个14英寸监视器都有一个BBC设计的波形监视器，上方有一个光学PPM，便于观看。该转播车还包括一个双标准无线广播接收器，用于405和625线广播。

*   **视频工程师控制台：** MCR21使用4台Pye Mk6摄像机，由带有操作控制面板 (OCP) 的两个控制台控制。每个控制台可容纳两名工程师，每台摄像机都有专用的图像和波形监视器。

该网站包含MCR21在建造过程中的图片和一张宣传照，突显了Pye公司在建造复杂OB转播车方面的能力。它还提到了该转播车的先进创新及其在为彩色广播铺平道路方面的作用。该网站还指向有关“今日比赛”60周年纪念和新闻通讯的信息。

---

## 97. 使用物理模拟寻找保龄球的击球策略

**原文标题**: Using physics simulations to find targeting strategies in tenpin bowling

**原文链接**: [https://pubs.aip.org/aip/adv/article/15/4/045222/3344017/Using-physics-simulations-to-find-targeting](https://pubs.aip.org/aip/adv/article/15/4/045222/3344017/Using-physics-simulations-to-find-targeting)

运用物理模拟寻找保龄球投球策略

---

## 98. 谷歌最终不会在Chrome浏览器中放弃第三方Cookie。

**原文标题**: Google won't ditch third-party cookies in Chrome after all

**原文链接**: [https://arstechnica.com/gadgets/2025/04/google-wont-ditch-third-party-cookies-in-chrome-after-all/](https://arstechnica.com/gadgets/2025/04/google-wont-ditch-third-party-cookies-in-chrome-after-all/)

谷歌已撤回在Chrome浏览器中逐步淘汰第三方Cookie的计划，实际上放弃了其隐私沙盒计划的核心目标。经过多年的开发和延误，谷歌将不再推出帮助用户禁用这些Cookie的功能。这一决定是在FLoC等最初的提案受到广泛批评，以及后来的计划被多次推迟之后做出的。

谷歌表示，广告行业对隐私日益关注影响了这一改变。然而，文章认为，谷歌近期反垄断案件带来的法律风险，特别是那些涉及其在搜索和广告技术领域主导地位的案件，是一个重要因素。通过Chrome的主导地位迫使广告行业采用谷歌的隐私沙盒替代方案，会产生不良影响。

虽然隐私沙盒项目并未完全消亡，但其作用已减弱。谷歌将继续开发隐私沙盒API，并致力于提高其采用率，但行业不太可能自行放弃Cookie。文章指出，Chrome的隐身模式仍然计划改进隐私功能，包括IP保护。

作者认为，虽然第三方Cookie不利于隐私，但普遍采用隐私沙盒可能会赋予谷歌更大的权力，而且考虑到谷歌对收入的关注，其隐私益处尚不确定。

---

## 99. M.2 HDMI 采集卡

**原文标题**: A M.2 HDMI capture card

**原文链接**: [https://interfacinglinux.com/2025/04/18/magewell-eco-m-2-hdmi-capture-card/](https://interfacinglinux.com/2025/04/18/magewell-eco-m-2-hdmi-capture-card/)

本文评测了美乐威Eco Capture Dual HDMI M.2采集卡，这是一款旨在安装在M.2插槽中的采集卡，它将通常用于存储的PCIe通道重新利用。作者强调了该采集卡对于PCIe插槽有限的系统的潜力。

评测涵盖了开箱体验，注意到包含了SHD-转-HDMI Type-A线缆，以及需要单独购买安装硬件。它详细介绍了x86和ARM（特别是使用Armbian的瑞芯微3588 SOC）系统的驱动程序安装过程，包括必要的依赖项和命令。作者表示惊讶Jetson TX2 ARM驱动程序可以在瑞芯微平台上工作。

评测证实了该采集卡与OBS和WebRTC应用程序（如Discord、Jitsi和Zoom）的兼容性，使其能够作为网络摄像头运行。作者将画面质量和延迟与Decklink Mini 4K Recorder进行了比较，发现它们不相上下。

总体的结论是积极的，赞扬了该采集卡的稳定性、24/7运行能力和M.2外形。然而，高昂的价格（建议零售价385美元）是一个显著的缺点，尽管作者注意到在eBay上找到了价格低得多的交易。评测最终给出了6.8/10的评分，强调了由于需要编译内核驱动程序而导致的安装困难，但赞扬了性能和外形。

---

## 100. 网络工程师的人工智能：理解流、流簇和基于数据包的负载均衡

**原文标题**: AI for Network Engineers: Understanding Flow, Flowlet, and Packet-Based LB

**原文链接**: [https://nwktimes.blogspot.com/2025/04/ai-for-network-engineers-understanding.html](https://nwktimes.blogspot.com/2025/04/ai-for-network-engineers-understanding.html)

面向网络工程师的人工智能：理解流、流簇和基于包的负载均衡

本文探讨了基于 RoCEv2 的 AI 后端网络中负载均衡面临的挑战，特别是 GPU 间通信产生的大量“大象流”。传统的基于流的、使用三层 ECMP 的负载均衡通常不足以应对，因为它无法适应拥塞，导致带宽使用不均衡和性能下降。

本文介绍了两种替代方法：基于流簇的自适应路由负载均衡和基于包的包喷洒负载均衡。自适应路由动态监控链路利用率并将流簇重定向到不那么拥塞的路径，从而减少缓冲区积压并提高链路利用率。

包喷洒将单个数据包分配到多个路径上。这种方法需要使用 RDMA Write Only 操作，该操作由较新的 NVIDIA 网卡（ConnectX-5 及更高版本）支持，并在每个数据包中包含 RDMA 扩展传输头 (RETH)。这种自包含的数据包允许进行基于每个数据包的负载均衡，而无需担心数据包重排序。

本文还提供了一个示例配置，用于在 Cisco Nexus 9000 系列云规模交换机上启用基于每个数据包的负载均衡（包喷洒），从 NX-OS Release 10.5(1)F 开始，使用动态负载均衡 (DLB)。关键在于 DLB MAC 地址，它将 MAC 地址与物理路径解耦。

---

