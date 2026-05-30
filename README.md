# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-05-30.md)

*最后自动更新时间: 2026-05-30 18:31:04*
## 1. OpenRouter完成1.13亿美元B轮融资

**原文标题**: OpenRouter raises $113M Series B

**原文链接**: [https://openrouter.ai/announcements/series-b](https://openrouter.ai/announcements/series-b)

OpenRouter 在由 CapitalG（Alphabet 旗下的独立成长基金）领投的 B 轮融资中筹集了 1.13 亿美元。本轮融资吸引了大量来自主要基础设施和平台公司的战略投资者，包括英伟达（NVentures）、ServiceNow、MongoDB、Snowflake 和 Databricks，以及现有股东 Andreessen Horowitz 和 Menlo Ventures。

该公司业务呈爆发式增长，每周 Token 处理量在短短六个月内从 5 万亿飙升至 25 万亿。OpenRouter 目前为超过 800 万名开发者提供服务，并支持访问 400 多种模型，致力于成为多模型 AI 时代不可或缺的“路由与网关层”。通过连接开发者与模型提供商，该平台负责管理生产级 AI 的复杂性，专注于可靠性、成本优化和合规性。

OpenRouter 的最新进展包括：
*   **多模态支持：** 从文本扩展到图像、音频、视频和转录模型。
*   **企业级控制：** 推出工作空间、支出管理和零数据保留政策等功能。
*   **智能路由：** 开发先进的故障转移和质量感知路由，针对成本和延迟进行优化。

新资金将用于扩展基础设施、深化企业级功能并增强智能路由工具，以帮助开发者应对日益复杂的 AI 模型及提供商格局。大型企业级云服务和数据公司的参与标志着市场已达成共识：专用路由层是现代 AI 技术栈的关键组成部分。

---

## 2. Zig ELF 链接器改进开发日志

**原文标题**: Zig ELF Linker Improvements Devlog

**原文链接**: [https://ziglang.org/devlog/2026/#2026-05-30](https://ziglang.org/devlog/2026/#2026-05-30)

2026 年 Zig 开发日志重点介绍了在项目迈向 0.17.0 版本之际，在编译器性能、构建系统和 I/O 处理方面取得的重大架构进展。

**核心编译器与链接器改进**
Matthew Lugg 引入了全新的 **ELF 链接器**，目前已支持使用 LLVM/LLD 库构建自举的 Zig 编译器。其核心特性是在 x86_64 Linux 上实现高速增量编译，使重新构建达到毫秒级。此外，**增量编译**已扩展至 LLVM 后端，加快了分析和错误报告的速度。Lugg 还完成了一项大规模的**类型解析重构**，使编译器更加延迟化（忽略命名空间中未使用的字段），并针对依赖循环提供更清晰、更详细的错误消息。

**构建系统重构**
Andrew Kelley 详细介绍了**构建系统**的基础性重构。通过将“配置器”进程（处理 `build.zig` 逻辑）与“执行器”进程（执行构建任务）分离，Zig 现在可以对构建图进行序列化和缓存。这一变化使系统能够完全跳过冗余逻辑，使常用命令的性能提升高达 90%，并为 ZLS 等第三方工具提供了更好的集成支持。

**标准库与 I/O**
标准库为 `std.Io.Evented` 增加了实验性的 **`io_uring` 和 Grand Central Dispatch** 实现。这些实现利用用户态栈切换（fiber），推动 Zig 迈向“应许之地”——即开发者可以毫不费力地在线程化和事件化 I/O 实现之间进行切换。

**影响总结**
总的来说，这些更新将开发者生产力放在首位。通过专注于极速增量重构、更高效的构建系统缓存以及更强大的类型解析引擎，Zig 团队在为更灵活的 I/O 和更好的平台支持奠定基础的同时，显著缩短了开发者的反馈周期。

---

## 3. 体素空间

**原文标题**: Voxel Space

**原文链接**: [https://s-macke.github.io/VoxelSpace/](https://s-macke.github.io/VoxelSpace/)

本文探讨了“Voxel Space”引擎，这是一种因1992年飞行模拟游戏《卡曼奇》（Comanche）而闻名的2.5D渲染技术。该引擎诞生于GPU尚未问世、CPU性能尚且低下的时代，因其能够渲染出细节丰富、带有纹理和阴影的地形而具有革命性意义，其效果领先于同时代技术多年。

该技术依赖于两个主要数据源：**高度图**和**颜色图**。由于光照和阴影已预烘焙在颜色图中，该引擎避开了实时光照带来的计算负担。其核心算法的原理是：根据观察者的距离和视野在这些2D地图上进行线条光栅化，然后将坐标投影到屏幕上以绘制垂直线。

文章详细介绍了该算法的几次迭代：
*   **基础渲染：** 使用“画家算法”，按由远及近的顺序进行渲染，以确保正确的遮挡关系。
*   **旋转：** 引入三角函数（正弦和余弦）以实现360度的相机移动。
*   **优化：** 引入了使用 **y-buffer** 的由近及远的渲染方式。该方法通过记录屏幕每一列已绘制的最高像素点来防止过度绘制。此外，它还利用了**多细节层次（LOD）**技术，通过增大远处物体的步长来显著提升性能。

尽管该引擎受限于“每个位置仅对应一个高度”——这意味着它难以表现建筑物或悬空树木等复杂的3D结构——但其简洁与高效使其成为了早期3D游戏史上的里程碑式成就。

---

## 4. Openrsync：由 OpenBSD 团队开发的 rsync 实现

**原文标题**: Openrsync: An implementation of rsync, by the OpenBSD team

**原文链接**: [https://github.com/kristapsdz/openrsync](https://github.com/kristapsdz/openrsync)

Openrsync 是 OpenBSD 原生的 rsync 协议实现，采用 BSD (ISC) 许可证分发。作为 `rpki-client` 项目的一部分，它旨在为原始的 GPL rsync 提供一个安全、可审计的替代方案。它兼容 rsync 协议 27（3.1.3 版本），但仅支持更精简的命令行参数子集。

该系统采用发送者-接收者架构，通过 SSH 或持久网络守护进程进行通信。与使用独立“生成器”进程的原始 rsync 不同，openrsync 将生成器和接收器整合在单个进程中。它利用事件循环和有限状态机来处理异步文件操作，从而提高了块交换过程中的响应速度。此交换过程采用两阶段哈希算法（Adler-32 和 MD4）来识别并仅传输文件的修改部分，块大小通常根据文件大小的平方根确定。

安全性是该项目的核心竞争力。Openrsync 利用 `pledge(2)` 等 OpenBSD 原生特性来限制系统调用，并使用 `unveil(2)` 将文件系统访问限制在特定的目标目录中。此外，它还通过使用 `arc4random(3)` 为哈希生成种子，进一步增强了加密安全性。

尽管 OpenBSD 是官方支持的平台，但 openrsync 也可以通过 `oconfigure` 工具移植到 Linux、macOS 和其他类 UNIX 系统。不过作者指出，OpenBSD 提供的强健安全保护在其他操作系统上难以完全复制。Openrsync 的 C 语言代码量约为 10,000 行，旨在保持代码简洁且易于审计，从而最大限度地减少漏洞。

---

## 5. Pandoc 模板

**原文标题**: Pandoc Templates

**原文链接**: [https://pandoc-templates.org/](https://pandoc-templates.org/)

本文提供了一份详尽的 Pandoc 模板清单，旨在将 Markdown 文件转换为包括 PDF、HTML、LaTeX、EPUB 和 DOCX 在内的各种专业格式。这些工具适用于广泛的用户群体，包括学者、学生、求职者和创意作家。

这些模板主要根据其用途进行分类：

*   **学术与教育：** 该类别包括博士论文、讲义（特别是备受欢迎的 *Eisvogel*）、试卷，以及针对 IEEE 或各类统计学期刊的特定投稿模板。
*   **职业与职场：** 提供了众多用于生成高质量简历、履历、发票和商务信函的工具，其中一些遵循德国 DIN 5008 等正式标准。
*   **网页与演示：** 该清单包含大量使用 CSS 实现响应式网站的模板（利用 Bootstrap、Tufte CSS 或类 GitHub 样式）以及幻灯片，甚至包括像 *patat* 这样独特的基于终端的演示工具。
*   **出版与特种应用：** 涵盖了创建电子书 (EPUB)、遵循行业标准格式的手稿，以及角色扮演游戏 (RPG) 活动指南和食谱集等分众化应用框架。

大多数模板利用 LaTeX 进行高质量排版，或利用 CSS 进行现代网页样式设计。它们通常使用 YAML 元数据来实现便捷的自定义，允许用户维持“单一源”工作流，将纯文本 Markdown 转换为精美的、可供出版的文档。该集合彰显了 Pandoc 生态系统的成熟度，及其在跨行业自动化处理复杂文档设计方面的能力。

---

## 6. 维尔纳·赫尔佐格与保罗·克罗宁对谈 (2014)

**原文标题**: Werner Herzog in conversation with Paul Cronin (2014)

**原文链接**: [https://fsgworkinprogress.com/2014/09/26/insignificant-bullets-evil-poachers-and-l-a-culture/](https://fsgworkinprogress.com/2014/09/26/insignificant-bullets-evil-poachers-and-l-a-culture/)

这段摘自保罗·克罗宁所著《赫尔佐格谈赫尔佐格》（*Werner Herzog: A Guide for the Perplexed*）的文字，直率地展现了这位电影人的生活、哲学和创作过程。赫尔佐格首先讲述了在接受BBC采访时发生的一起轻微枪击事件，他将其斥为“美国民俗”而付之一笑，这体现了他坚毅的世界观以及对现代“懦弱”的轻蔑。

赫尔佐格分享了他与洛杉矶之间复杂的关系，称赞其原始的文化活力和“充满生机的存在感”，同时痛斥其“惊人的愚蠢”，如新纪元狂热和心理分析。他认为自我剖析会摧毁“我们灵魂中伟大的奥秘”，并将强迫披露内心自我的行为比作西班牙宗教裁判所。他还反思了美学文化表征的变迁，表达了对安娜·尼科尔·史密斯等人物身上那种“重大的”且“庸俗的”特质的着迷。

对话的大部分篇幅集中在他的纪录片《灰熊人》上。赫尔佐格澄清说，这部电影是对人类境况的探索，而非自然纪录片。他将主人公提摩西·崔德威描述为一个“深受困扰的人”，试图通过熊来寻求救赎，以逃避内心的恶魔。虽然赫尔佐格承认崔德威身上带有妄想色彩的浪漫主义，但他称赞了崔德威自拍素材的原始力量和影像美感，认为那是好莱坞永远无法复制的。

最后，赫尔佐格讨论了他作为电影人的伦理底线，解释了他决定剔除崔德威遇难录音的原因。他将电影创作与窥淫癖区别开来，断言自己拒绝跨越界限去制作煽情露骨的“虐杀”媒体，认为比起公众的好奇心，他更看重“尊严死去的权利”。

---

## 7. Microcode inside the Intel 8087 floating-point chip: register exchange

**原文标题**: Microcode inside the Intel 8087 floating-point chip: register exchange

**原文链接**: [https://www.righto.com/2026/05/microcode-inside-intel-8087-floating.html](https://www.righto.com/2026/05/microcode-inside-intel-8087-floating.html)

The Intel 8087 floating-point co-processor, released in 1980, revolutionized computing by accelerating floating-point operations up to 100 times. Its complex functions are driven by microcode—a low-level instruction set stored in a 1,648-instruction ROM. This article explores the `FXCH` (Floating-point Exchange) instruction, which swaps the top-of-stack register (`ST(0)`) with another specified stack register (`ST(i)`).

While a swap might seem trivial, the 8087 requires 14 micro-instructions to handle the operation safely. Internally, the chip uses an 80-bit format and a stack-based architecture where each register has two "tag" bits indicating its status (valid, zero, special, or empty).

The `FXCH` microcode sequence follows these steps:
1.  **Buffering:** It moves the contents of `ST(0)` and `ST(i)` into temporary registers (`tmpA` and `tmpB`).
2.  **Validation:** It checks the tag bits. If either register is "empty," the microcode triggers an "invalid operation" exception.
3.  **Exception Handling:** If the exception is "masked," the microcode continues by replacing the empty values with a "Not a Number" (NaN) bit pattern. If unmasked, it stops to allow the CPU to handle the interrupt.
4.  **Completion:** It writes the buffered values back to the opposite stack positions and calls `RNI` (Run Next Instruction).

Reverse-engineering this microcode involves analyzing high-resolution microscope images of the chip’s die. To save space, Intel used a unique semi-analog ROM that stores two bits per transistor using four different transistor sizes. This analysis, conducted by the Opcode Collective, reveals the sophisticated interplay between hardware and microcode in early silicon to ensure mathematical accuracy and robust error management.

---

## 8. Navier-Stokes fluid simulation explained with Godot game engine

**原文标题**: Navier-Stokes fluid simulation explained with Godot game engine

**原文链接**: [https://myzopotamia.dev/navier-stokes-fluid-simulation-explained-with-godot](https://myzopotamia.dev/navier-stokes-fluid-simulation-explained-with-godot)

生成摘要时出错

---

## 9. It Takes Two Neurons to Ride a Bicycle

**原文标题**: It Takes Two Neurons to Ride a Bicycle

**原文链接**: [https://fermatslibrary.com/s/it-takes-two-neurons-to-ride-a-bicycle#email-newsletter](https://fermatslibrary.com/s/it-takes-two-neurons-to-ride-a-bicycle#email-newsletter)

生成摘要时出错

---

## 10. Downdetector and Speedtest sold to Accenture for $1.2B

**原文标题**: Downdetector and Speedtest sold to Accenture for $1.2B

**原文链接**: [https://www.theverge.com/tech/889234/downdetector-ookla-speedtest-sold-accenture](https://www.theverge.com/tech/889234/downdetector-ookla-speedtest-sold-accenture)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 2 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 3 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 4 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 5 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 6 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 7 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 8 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 9 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 10 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 11 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 12 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 13 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 14 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 15 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 16 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 17 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 18 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 19 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 20 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 21 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 22 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 23 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 24 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 25 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 26 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 27 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 28 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 29 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 30 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 31 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 32 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 33 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 34 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 35 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 36 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 37 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 38 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 39 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 40 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 41 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 42 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 43 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 44 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 45 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 46 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 47 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 48 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 49 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 50 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 51 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 52 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 53 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 54 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 55 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 56 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 57 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 58 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 59 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 60 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 61 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 62 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 63 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 64 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 65 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 66 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 67 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 68 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 69 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 70 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 71 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 72 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 73 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 74 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 75 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 76 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 77 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 78 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 79 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 80 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 81 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 82 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 83 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 84 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 85 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 86 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 87 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 88 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 89 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 90 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 91 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 92 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 93 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 94 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 95 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 96 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 97 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 98 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 99 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 100 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 101 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 102 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 103 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 104 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 105 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 106 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 107 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 108 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 109 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 110 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 111 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 112 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 113 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 114 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 115 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 116 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 117 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 118 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 119 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 120 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 121 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 122 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 123 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 124 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 125 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 126 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 127 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 128 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 129 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 130 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 131 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 132 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 133 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 134 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 135 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 136 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 137 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 138 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 139 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 140 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 141 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 142 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 143 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 144 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 145 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 146 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 147 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 148 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 149 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 150 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 151 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 152 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 153 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 154 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 155 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 156 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 157 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 158 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 159 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 160 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 161 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 162 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 163 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 164 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 165 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 166 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 167 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 168 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 169 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 170 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 171 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 172 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 173 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 174 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 175 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 176 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 177 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 178 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 179 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 180 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 181 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 182 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 183 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 184 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 185 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 186 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 187 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 188 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 189 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 190 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 191 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 192 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 193 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 194 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 195 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 196 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 197 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 198 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 199 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 200 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 201 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 202 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 203 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 204 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 205 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 206 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 207 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 208 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 209 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 210 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 211 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 212 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 213 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 214 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 215 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 216 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 217 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 218 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 219 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 220 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 221 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 222 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 223 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 224 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 225 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 226 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 227 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 228 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 229 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 230 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 231 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 232 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 233 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 234 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 235 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 236 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 237 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 238 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 239 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 240 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 241 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 242 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 243 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 244 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 245 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 246 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 247 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 248 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 249 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 250 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 251 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 252 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 253 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 254 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 255 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 256 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 257 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 258 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 259 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 260 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 261 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 262 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 263 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 264 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 265 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 266 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 267 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 268 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 269 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 270 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 271 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 272 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 273 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 274 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 275 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 276 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 277 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 278 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 279 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 280 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 281 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 282 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 283 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 284 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 285 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 286 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 287 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 288 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 289 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 290 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 291 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 292 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 293 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 294 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 295 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 296 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 297 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 298 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 299 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 300 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 301 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 302 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 303 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 304 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 305 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 306 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 307 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 308 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 309 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 310 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 311 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 312 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 313 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 314 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 315 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 316 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 317 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 318 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 319 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 320 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 321 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 322 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 323 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 324 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 325 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 326 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 327 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 328 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 329 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 330 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 331 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 332 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 333 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 334 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 335 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 336 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 337 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 338 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 339 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 340 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 341 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 342 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 343 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 344 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 345 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 346 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 347 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 348 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 349 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 350 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 351 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 352 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 353 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 354 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 355 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 356 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 357 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 358 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 359 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 360 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 361 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 362 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 363 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 364 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 365 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 366 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 367 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 368 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 369 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 370 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 371 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 372 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 373 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 374 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 375 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 376 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 377 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 378 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 379 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 380 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 381 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 382 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 383 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 384 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 385 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 386 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 387 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 388 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 389 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 390 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 391 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 392 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 393 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 394 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 395 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 396 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 397 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 398 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 399 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 400 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 401 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 402 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 403 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 404 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 405 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 406 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 407 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 408 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 409 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 410 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 411 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 412 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 413 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 414 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 415 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 416 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 417 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 418 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 419 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 420 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 421 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 422 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 423 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 424 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 425 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 426 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 427 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 428 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 429 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 430 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 431 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 432 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 433 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 434 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 435 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 436 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
