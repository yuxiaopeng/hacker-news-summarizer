# Hacker News 热门文章摘要 (2026-05-30)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Zig: Build System Reworked

**原文标题**: Zig: Build System Reworked

**原文链接**: [https://ziglang.org/devlog/2026/#2026-05-26](https://ziglang.org/devlog/2026/#2026-05-26)

生成摘要时出错

---

## 12. IXI's autofocusing lenses are almost ready to replace multifocal glasses

**原文标题**: IXI's autofocusing lenses are almost ready to replace multifocal glasses

**原文链接**: [https://www.engadget.com/wearables/ixis-autofocusing-lenses-multifocal-glasses-ces-2026-212608427.html](https://www.engadget.com/wearables/ixis-autofocusing-lenses-multifocal-glasses-ces-2026-212608427.html)

生成摘要时出错

---

## 13. Show HN: Helios – what plug-in solar could generate for any address in Britain

**原文标题**: Show HN: Helios – what plug-in solar could generate for any address in Britain

**原文链接**: [https://helios.southlondonscientific.com/](https://helios.southlondonscientific.com/)

生成摘要时出错

---

## 14. What Happened to the Locusts?

**原文标题**: What Happened to the Locusts?

**原文链接**: [https://explosion-scratch.github.io/locusts/](https://explosion-scratch.github.io/locusts/)

生成摘要时出错

---

## 15. SQLite is all you need for durable workflows

**原文标题**: SQLite is all you need for durable workflows

**原文链接**: [https://obeli.sk/blog/sqlite-is-all-you-need-for-durable-workflows/](https://obeli.sk/blog/sqlite-is-all-you-need-for-durable-workflows/)

生成摘要时出错

---

## 16. Testing the WWI concrete ships and WWII concrete barges

**原文标题**: Testing the WWI concrete ships and WWII concrete barges

**原文链接**: [https://thecretefleet.com/blog/f/testing-the-wwi-concrete-ships-and-wwii-concrete-barges](https://thecretefleet.com/blog/f/testing-the-wwi-concrete-ships-and-wwii-concrete-barges)

生成摘要时出错

---

## 17. Memory decline after menopause linked to loss of estrogen production in brain

**原文标题**: Memory decline after menopause linked to loss of estrogen production in brain

**原文链接**: [https://news.northwestern.edu/stories/2026/05/memory-decline-after-menopause-linked-to-loss-of-estrogen-production-in-brain-tissue](https://news.northwestern.edu/stories/2026/05/memory-decline-after-menopause-linked-to-loss-of-estrogen-production-in-brain-tissue)

生成摘要时出错

---

## 18. Stateless Actors

**原文标题**: Stateless Actors

**原文链接**: [https://www.massicotte.org/stateless-actors/](https://www.massicotte.org/stateless-actors/)

生成摘要时出错

---

## 19. Notes from the Mistral AI Now Summit

**原文标题**: Notes from the Mistral AI Now Summit

**原文链接**: [https://koenvangilst.nl/lab/mistral-ai-now-summit](https://koenvangilst.nl/lab/mistral-ai-now-summit)

生成摘要时出错

---

## 20. A Probabilistic Algorithm for Repairing All Roads in Lebanon via Papal Visits

**原文标题**: A Probabilistic Algorithm for Repairing All Roads in Lebanon via Papal Visits

**原文链接**: [https://sigbovik.org/2026/proceedings.pdf#%5B%7B%22num%22%3A13%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22XYZ%22%7D%2C72%2C720%2Cnull%5D](https://sigbovik.org/2026/proceedings.pdf#%5B%7B%22num%22%3A13%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22XYZ%22%7D%2C72%2C720%2Cnull%5D)

生成摘要时出错

---

## 21. MCP is dead?

**原文标题**: MCP is dead?

**原文链接**: [https://www.quandri.io/engineering-blog/mcp-is-dead](https://www.quandri.io/engineering-blog/mcp-is-dead)

生成摘要时出错

---

## 22. Snowboard Kids 2 is 100% Decompiled

**原文标题**: Snowboard Kids 2 is 100% Decompiled

**原文链接**: [https://blog.chrislewis.au/snowboard-kids-2-is-100-decompiled/](https://blog.chrislewis.au/snowboard-kids-2-is-100-decompiled/)

生成摘要时出错

---

## 23. Macsurf, "modern" web browser for macOS 9

**原文标题**: Macsurf, "modern" web browser for macOS 9

**原文链接**: [https://github.com/mplsllc/macsurf](https://github.com/mplsllc/macsurf)

生成摘要时出错

---

## 24. The Last Technical Interview

**原文标题**: The Last Technical Interview

**原文链接**: [https://steve-yegge.medium.com/the-last-technical-interview-bc13ddcf4564](https://steve-yegge.medium.com/the-last-technical-interview-bc13ddcf4564)

生成摘要时出错

---

## 25. Print with dozens of colors: Our new open-source ColorMix for PrusaSlicer

**原文标题**: Print with dozens of colors: Our new open-source ColorMix for PrusaSlicer

**原文链接**: [https://blog.prusa3d.com/our-new-open-source-colormix-model-in-prusaslicer-and-easyprint_136079/](https://blog.prusa3d.com/our-new-open-source-colormix-model-in-prusaslicer-and-easyprint_136079/)

生成摘要时出错

---

## 26. Floor and Ceil versus Denormals on CPU and GPU

**原文标题**: Floor and Ceil versus Denormals on CPU and GPU

**原文链接**: [https://asawicki.info/news_1802_floor_and_ceil_versus_denormals_on_cpu_and_gpu](https://asawicki.info/news_1802_floor_and_ceil_versus_denormals_on_cpu_and_gpu)

生成摘要时出错

---

## 27. The dead economy theory

**原文标题**: The dead economy theory

**原文链接**: [https://www.owenmcgrann.com/p/the-dead-economy-theory](https://www.owenmcgrann.com/p/the-dead-economy-theory)

生成摘要时出错

---

## 28. It's hard to justify buying a Framework 12

**原文标题**: It's hard to justify buying a Framework 12

**原文链接**: [https://www.jeffgeerling.com/blog/2026/its-hard-to-justify-framework-12/](https://www.jeffgeerling.com/blog/2026/its-hard-to-justify-framework-12/)

生成摘要时出错

---

## 29. Shift will clean homes for free to train future robots

**原文标题**: Shift will clean homes for free to train future robots

**原文链接**: [https://www.theverge.com/ai-artificial-intelligence/939765/ai-training-data-startup-shift-free-cleaning](https://www.theverge.com/ai-artificial-intelligence/939765/ai-training-data-startup-shift-free-cleaning)

生成摘要时出错

---

## 30. Liquid AI reveals 8B-A1B MoE trained on 38T

**原文标题**: Liquid AI reveals 8B-A1B MoE trained on 38T

**原文链接**: [https://www.liquid.ai/blog/lfm2-5-8b-a1b](https://www.liquid.ai/blog/lfm2-5-8b-a1b)

生成摘要时出错

---

## 31. Nikon weaponizes lower prices to break ASML's lithography monopoly

**原文标题**: Nikon weaponizes lower prices to break ASML's lithography monopoly

**原文链接**: [https://www.tomshardware.com/tech-industry/nikon-plans-to-undercut-asml-on-price-to-win-back-chipmaking-lithography-customers](https://www.tomshardware.com/tech-industry/nikon-plans-to-undercut-asml-on-price-to-win-back-chipmaking-lithography-customers)

生成摘要时出错

---

## 32. Leo's first encyclical attacks technological messianism

**原文标题**: Leo's first encyclical attacks technological messianism

**原文链接**: [https://www.economist.com/europe/2026/05/28/leos-first-encyclical-attacks-technological-messianism](https://www.economist.com/europe/2026/05/28/leos-first-encyclical-attacks-technological-messianism)

生成摘要时出错

---

## 33. Bijou64: A variable-length integer encoding

**原文标题**: Bijou64: A variable-length integer encoding

**原文链接**: [https://www.inkandswitch.com/tangents/bijou64/](https://www.inkandswitch.com/tangents/bijou64/)

生成摘要时出错

---

## 34. What It Takes to Preserve Floppy Disks

**原文标题**: What It Takes to Preserve Floppy Disks

**原文链接**: [https://spectrum.ieee.org/floppy-disk-data-preservation-archives](https://spectrum.ieee.org/floppy-disk-data-preservation-archives)

生成摘要时出错

---

## 35. Show HN: Tiny-vLLM – high performance LLM inference engine in C++ and CUDA

**原文标题**: Show HN: Tiny-vLLM – high performance LLM inference engine in C++ and CUDA

**原文链接**: [https://github.com/jmaczan/tiny-vllm](https://github.com/jmaczan/tiny-vllm)

生成摘要时出错

---

## 36. Show HN: Open-source private home security camera system (end-to-end encryption)

**原文标题**: Show HN: Open-source private home security camera system (end-to-end encryption)

**原文链接**: [https://github.com/secluso/core](https://github.com/secluso/core)

生成摘要时出错

---

## 37. Naphtha shortages in Japan

**原文标题**: Naphtha shortages in Japan

**原文链接**: [https://www.nippon.com/en/japan-data/h02783/](https://www.nippon.com/en/japan-data/h02783/)

生成摘要时出错

---

## 38. On Rendering Diffs

**原文标题**: On Rendering Diffs

**原文链接**: [https://pierre.computer/writing/on-rendering-diffs](https://pierre.computer/writing/on-rendering-diffs)

生成摘要时出错

---

## 39. Perry Compiles TypeScript directly to executables using SWC and LLVM

**原文标题**: Perry Compiles TypeScript directly to executables using SWC and LLVM

**原文链接**: [https://www.perryts.com/](https://www.perryts.com/)

生成摘要时出错

---

## 40. A new register allocator for ZJIT

**原文标题**: A new register allocator for ZJIT

**原文链接**: [https://railsatscale.com/2026-05-27-a-new-register-allocator-for-zjit/](https://railsatscale.com/2026-05-27-a-new-register-allocator-for-zjit/)

生成摘要时出错

---

## 41. OpenRCT2 v0.5.1 "Swamp Castle" released Last version to support Windows 7

**原文标题**: OpenRCT2 v0.5.1 "Swamp Castle" released Last version to support Windows 7

**原文链接**: [https://openrct2.io/blog/2026/05/openrct2-v0.5.1-released](https://openrct2.io/blog/2026/05/openrct2-v0.5.1-released)

生成摘要时出错

---

## 42. GTA 6 Developers Unionize

**原文标题**: GTA 6 Developers Unionize

**原文链接**: [https://rockstarintel.com/gta-6-developers-announce-rockstar-games-union/](https://rockstarintel.com/gta-6-developers-announce-rockstar-games-union/)

生成摘要时出错

---

## 43. Claude Opus 4.8

**原文标题**: Claude Opus 4.8

**原文链接**: [https://www.anthropic.com/news/claude-opus-4-8](https://www.anthropic.com/news/claude-opus-4-8)

生成摘要时出错

---

## 44. High Density Living, 2000 Years Ago: Inside the Roman Apartment Building

**原文标题**: High Density Living, 2000 Years Ago: Inside the Roman Apartment Building

**原文链接**: [https://commonedge.org/high-density-living-2000-years-ago-inside-the-roman-apartment-building/](https://commonedge.org/high-density-living-2000-years-ago-inside-the-roman-apartment-building/)

生成摘要时出错

---

## 45. We should be more tired than the model

**原文标题**: We should be more tired than the model

**原文链接**: [https://vickiboykis.com/2026/05/28/we-should-be-more-tired-than-the-model/](https://vickiboykis.com/2026/05/28/we-should-be-more-tired-than-the-model/)

生成摘要时出错

---

## 46. What Is a Dickover?

**原文标题**: What Is a Dickover?

**原文链接**: [https://daringfireball.net/2026/05/what_is_a_dickover](https://daringfireball.net/2026/05/what_is_a_dickover)

生成摘要时出错

---

## 47. Math-to-Manim

**原文标题**: Math-to-Manim

**原文链接**: [https://github.com/HarleyCoops/Math-To-Manim](https://github.com/HarleyCoops/Math-To-Manim)

生成摘要时出错

---

## 48. Adding Linux support back for the BASIC (free) version of Vivado

**原文标题**: Adding Linux support back for the BASIC (free) version of Vivado

**原文链接**: [https://adaptivesupport.amd.com/s/question/0D5Pd00001aT5IcKAK/adding-linux-support-back-for-the-basic-free-version-of-vivado?language=en_US](https://adaptivesupport.amd.com/s/question/0D5Pd00001aT5IcKAK/adding-linux-support-back-for-the-basic-free-version-of-vivado?language=en_US)

生成摘要时出错

---

## 49. Real-time LLM Inference on Standard GPUs: 3k tokens/s per request

**原文标题**: Real-time LLM Inference on Standard GPUs: 3k tokens/s per request

**原文链接**: [https://blog.kog.ai/real-time-llm-inference-on-standard-gpus-3-000-tokens-s-per-request/](https://blog.kog.ai/real-time-llm-inference-on-standard-gpus-3-000-tokens-s-per-request/)

生成摘要时出错

---

## 50. Cedana (YC S23) Is Hiring

**原文标题**: Cedana (YC S23) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/cedana/jobs/d1vYocG-forward-deployed-engineer-ai-hpc](https://www.ycombinator.com/companies/cedana/jobs/d1vYocG-forward-deployed-engineer-ai-hpc)

生成摘要时出错

---

## 51. Citing 'severe' math deficits, UC faculty demand a return to SAT tests for STEM

**原文标题**: Citing 'severe' math deficits, UC faculty demand a return to SAT tests for STEM

**原文链接**: [https://www.latimes.com/california/story/2026-05-27/uc-math-professors-demand-return-of-sat-for-stem-admissions](https://www.latimes.com/california/story/2026-05-27/uc-math-professors-demand-return-of-sat-for-stem-admissions)

生成摘要时出错

---

## 52. Bricks and Minifigs Stole a Man's $200k Lego Collection

**原文标题**: Bricks and Minifigs Stole a Man's $200k Lego Collection

**原文链接**: [https://mybricklog.com/blog/bricks-minifigs-corporate-stole-old-mans-200000-lego-collection](https://mybricklog.com/blog/bricks-minifigs-corporate-stole-old-mans-200000-lego-collection)

生成摘要时出错

---

## 53. Dynamic Workflows in Claude Code

**原文标题**: Dynamic Workflows in Claude Code

**原文链接**: [https://claude.com/blog/introducing-dynamic-workflows-in-claude-code](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)

生成摘要时出错

---

## 54. Let's talk about encrypted reasoning

**原文标题**: Let's talk about encrypted reasoning

**原文链接**: [https://blog.cryptographyengineering.com/2026/05/29/fooling-around-with-encrypted-reasoning-blobs/](https://blog.cryptographyengineering.com/2026/05/29/fooling-around-with-encrypted-reasoning-blobs/)

生成摘要时出错

---

## 55. Show HN: TV Explorer. Adding advanced UI to free online TV

**原文标题**: Show HN: TV Explorer. Adding advanced UI to free online TV

**原文链接**: [https://tvexplorer.live](https://tvexplorer.live)

生成摘要时出错

---

## 56. Algebraic Effects for the Rest of Us

**原文标题**: Algebraic Effects for the Rest of Us

**原文链接**: [https://overreacted.io/algebraic-effects-for-the-rest-of-us/](https://overreacted.io/algebraic-effects-for-the-rest-of-us/)

生成摘要时出错

---

## 57. Utiq – The ad tracking of your (European) ISP and how to avoid it

**原文标题**: Utiq – The ad tracking of your (European) ISP and how to avoid it

**原文链接**: [https://korben.info/utiq-identifiant-publicitaire-telcos.html](https://korben.info/utiq-identifiant-publicitaire-telcos.html)

生成摘要时出错

---

## 58. Corporate America Is Starting to Ration AI as Cost Skyrockets

**原文标题**: Corporate America Is Starting to Ration AI as Cost Skyrockets

**原文链接**: [https://www.wsj.com/tech/ai/corporate-america-is-starting-to-ration-ai-as-cost-skyrockets-1eb99d7a](https://www.wsj.com/tech/ai/corporate-america-is-starting-to-ration-ai-as-cost-skyrockets-1eb99d7a)

生成摘要时出错

---

## 59. Let's compile Quake like it's 1997

**原文标题**: Let's compile Quake like it's 1997

**原文链接**: [https://fabiensanglard.net/compile_like_1997/](https://fabiensanglard.net/compile_like_1997/)

生成摘要时出错

---

## 60. CAPTCHAs can still detect AI agents

**原文标题**: CAPTCHAs can still detect AI agents

**原文链接**: [https://research.roundtable.ai/captchas-detect-ai/](https://research.roundtable.ai/captchas-detect-ai/)

生成摘要时出错

---

## 61. Ember.js 7.0

**原文标题**: Ember.js 7.0

**原文链接**: [https://blog.emberjs.com/ember-released-7-0/](https://blog.emberjs.com/ember-released-7-0/)

生成摘要时出错

---

## 62. Toranj: Our Adventure Left Mid-Way inside a loud and grieving Iran

**原文标题**: Toranj: Our Adventure Left Mid-Way inside a loud and grieving Iran

**原文链接**: [https://medium.com/@alirezamd/toranj-an-adventure-left-mid-way-2da199493720](https://medium.com/@alirezamd/toranj-an-adventure-left-mid-way-2da199493720)

生成摘要时出错

---

## 63. Show HN: Zot – Yet another coding agent harness

**原文标题**: Show HN: Zot – Yet another coding agent harness

**原文链接**: [https://www.zot.sh](https://www.zot.sh)

生成摘要时出错

---

## 64. Someone used my open source project to phish people

**原文标题**: Someone used my open source project to phish people

**原文链接**: [https://andrej.sh/posts/phishing-through-my-open-source-project](https://andrej.sh/posts/phishing-through-my-open-source-project)

生成摘要时出错

---

## 65. Expertise in the age of AI

**原文标题**: Expertise in the age of AI

**原文链接**: [https://www.moderndescartes.com/essays/ai_and_expertise/](https://www.moderndescartes.com/essays/ai_and_expertise/)

This article explores the evolving role of junior engineers and the nature of expertise as AI coding agents become more capable. The author addresses the paradox of a cooling job market for new graduates alongside intense competition for elite junior talent.

Using the history of mathematics as an analogy, the author argues that while calculators (and now AI) automate execution, the "skills hypothesis" remains true: struggling through manual fundamentals builds a crucial "intuition." This intuition is what allows senior engineers to prompt AI more effectively and verify its output for correctness. Currently, the author estimates that the level of intuition needed to additively prompt AI effectively requires roughly five years of manual experience.

The article suggests several key takeaways for the AI era:

*   **The Bar for Entry is Rising:** Only junior engineers capable of reaching a high threshold of "coding intuition" within 2–3 years remain highly competitive. 
*   **Learning Stages:** Expertise is built in stages, moving from basic vocabulary (weeks) to knowing how and when to prompt (months), to verifying correctness (months), and finally to professional-grade mastery (5+ years).
*   **The Importance of Fundamentals:** Everyone should learn basic coding to understand how to leverage AI for automation. However, learners should avoid "speedrunning" their education with AI. 

The author concludes that "doing the work by hand" is essential for long-term mastery. Just as math students are forbidden from using calculators until they master the basics, developers should not rely on AI until they have performed the tasks manually, as the struggle itself is what builds the expertise required to command the tools of the future.

---

## 66. Quantum dot qubit using High NA EUV lithography

**原文标题**: Quantum dot qubit using High NA EUV lithography

**原文链接**: [https://www.imec-int.com/en/press/world-first-imec-presents-quantum-dot-qubit-device-using-high-na-euv-lithography](https://www.imec-int.com/en/press/world-first-imec-presents-quantum-dot-qubit-device-using-high-na-euv-lithography)

生成摘要时出错

---

## 67. You can just say it

**原文标题**: You can just say it

**原文链接**: [https://noperator.dev/posts/you-can-just-say-it/](https://noperator.dev/posts/you-can-just-say-it/)

生成摘要时出错

---

## 68. Letter from the Duke of Wellington to the British Foreign Office (1809)

**原文标题**: Letter from the Duke of Wellington to the British Foreign Office (1809)

**原文链接**: [https://wellsoc.org/society-member-pages/anecdotes-of-wellington/](https://wellsoc.org/society-member-pages/anecdotes-of-wellington/)

生成摘要时出错

---

## 69. Is AI causing a repeat of frontend’s lost decade?

**原文标题**: Is AI causing a repeat of frontend’s lost decade?

**原文链接**: [https://mastrojs.github.io/blog/2026-05-23-is-AI-causing-a-repeat-of-frontends-lost-decade/](https://mastrojs.github.io/blog/2026-05-23-is-AI-causing-a-repeat-of-frontends-lost-decade/)

生成摘要时出错

---

## 70. Social Animus

**原文标题**: Social Animus

**原文链接**: [https://justine.lol/animus/](https://justine.lol/animus/)

生成摘要时出错

---

## 71. The California state assembly has passed the 'Protect Our Games Act'

**原文标题**: The California state assembly has passed the 'Protect Our Games Act'

**原文链接**: [https://www.invenglobal.com/articles/22330/stop-killing-games-movement-gains-momentum-california-assembly-passes-game-protection-bill](https://www.invenglobal.com/articles/22330/stop-killing-games-movement-gains-momentum-california-assembly-passes-game-protection-bill)

生成摘要时出错

---

## 72. Anthropic surpasses OpenAI to become most valuable AI startup

**原文标题**: Anthropic surpasses OpenAI to become most valuable AI startup

**原文链接**: [https://qazinform.com/news/anthropic-surpasses-openai-to-become-worlds-most-valuable-ai-startup](https://qazinform.com/news/anthropic-surpasses-openai-to-become-worlds-most-valuable-ai-startup)

生成摘要时出错

---

## 73. Rothko for your current weather conditions

**原文标题**: Rothko for your current weather conditions

**原文链接**: [https://rothko.joonas.wtf/](https://rothko.joonas.wtf/)

生成摘要时出错

---

## 74. Probabilistic, Reformative Justice

**原文标题**: Probabilistic, Reformative Justice

**原文链接**: [https://www.lesswrong.com/posts/dqbhcm6g7CMWvhoid/probabilistic-reformative-justice](https://www.lesswrong.com/posts/dqbhcm6g7CMWvhoid/probabilistic-reformative-justice)

生成摘要时出错

---

## 75. Free full BGP feed. IPv4 and IPv6 (2020)

**原文标题**: Free full BGP feed. IPv4 and IPv6 (2020)

**原文链接**: [https://lukasz.bromirski.net/post/bgp-w-labie-3/](https://lukasz.bromirski.net/post/bgp-w-labie-3/)

生成摘要时出错

---

## 76. Danish pension fund excludes SpaceX citing governance and valuation

**原文标题**: Danish pension fund excludes SpaceX citing governance and valuation

**原文链接**: [https://www.reuters.com/legal/transactional/danish-pension-fund-excludes-spacex-citing-governance-valuation-2026-05-29/](https://www.reuters.com/legal/transactional/danish-pension-fund-excludes-spacex-citing-governance-valuation-2026-05-29/)

生成摘要时出错

---

## 77. I am retiring from tech to live offline

**原文标题**: I am retiring from tech to live offline

**原文链接**: [https://openpath.quest/2026/i-am-retiring-from-tech-to-live-offline/](https://openpath.quest/2026/i-am-retiring-from-tech-to-live-offline/)

生成摘要时出错

---

## 78. Orchestrating AI code review at scale

**原文标题**: Orchestrating AI code review at scale

**原文链接**: [https://blog.cloudflare.com/ai-code-review/](https://blog.cloudflare.com/ai-code-review/)

生成摘要时出错

---

## 79. Local Git remotes

**原文标题**: Local Git remotes

**原文链接**: [https://cblgh.org/posts/local-git-remotes/](https://cblgh.org/posts/local-git-remotes/)

生成摘要时出错

---

## 80. Microsoft 0-day feud escalates as researcher threatens another exploit dump

**原文标题**: Microsoft 0-day feud escalates as researcher threatens another exploit dump

**原文链接**: [https://www.theregister.com/security/2026/05/28/microsoft-0-day-feud-escalates-as-researcher-threatens-another-windows-exploit-dump/5248085](https://www.theregister.com/security/2026/05/28/microsoft-0-day-feud-escalates-as-researcher-threatens-another-windows-exploit-dump/5248085)

生成摘要时出错

---

## 81. Show HN: I built an Android OS in the browser

**原文标题**: Show HN: I built an Android OS in the browser

**原文链接**: [https://mobilegym.dev/](https://mobilegym.dev/)

生成摘要时出错

---

## 82. As floods get worse, Britain tries a new solution: beavers

**原文标题**: As floods get worse, Britain tries a new solution: beavers

**原文链接**: [https://www.npr.org/2026/05/21/nx-s1-5738979/beavers-britain-climate-change-flooding](https://www.npr.org/2026/05/21/nx-s1-5738979/beavers-britain-climate-change-flooding)

生成摘要时出错

---

## 83. Science sleuths find 100 suspicious images in Thermo Fisher antibody catalogue

**原文标题**: Science sleuths find 100 suspicious images in Thermo Fisher antibody catalogue

**原文链接**: [https://www.nature.com/articles/d41586-026-01706-2](https://www.nature.com/articles/d41586-026-01706-2)

生成摘要时出错

---

## 84. The mysterious Hy3 LLM is topping OpenRouter Model Rankings by a large margin

**原文标题**: The mysterious Hy3 LLM is topping OpenRouter Model Rankings by a large margin

**原文链接**: [https://minimaxir.com/2026/05/openrouter-hy3/](https://minimaxir.com/2026/05/openrouter-hy3/)

生成摘要时出错

---

## 85. Blue Origin's New Glenn blows up during static fire test

**原文标题**: Blue Origin's New Glenn blows up during static fire test

**原文链接**: [https://twitter.com/nasaspaceflight/status/2060164928472854821](https://twitter.com/nasaspaceflight/status/2060164928472854821)

生成摘要时出错

---

## 86. Finding Miscompiles for Fun, Not Profit

**原文标题**: Finding Miscompiles for Fun, Not Profit

**原文链接**: [https://newsletter.semianalysis.com/p/finding-miscompiles-for-fun-not-profit](https://newsletter.semianalysis.com/p/finding-miscompiles-for-fun-not-profit)

生成摘要时出错

---

## 87. Iron-rich immune cells help homing pigeons navigate

**原文标题**: Iron-rich immune cells help homing pigeons navigate

**原文链接**: [https://www.science.org/content/article/mind-blowing-iron-rich-immune-cells-help-homing-pigeons-navigate](https://www.science.org/content/article/mind-blowing-iron-rich-immune-cells-help-homing-pigeons-navigate)

生成摘要时出错

---

## 88. Inferno (Boards of Canada)

**原文标题**: Inferno (Boards of Canada)

**原文链接**: [https://en.wikipedia.org/wiki/Inferno_(Boards_of_Canada_album)](https://en.wikipedia.org/wiki/Inferno_(Boards_of_Canada_album))

生成摘要时出错

---

## 89. Durable execution, the hard way

**原文标题**: Durable execution, the hard way

**原文链接**: [https://github.com/hatchet-dev/durable-execution-the-hard-way](https://github.com/hatchet-dev/durable-execution-the-hard-way)

生成摘要时出错

---

## 90. Join the Independent Science Society! (A New Kinda Science Society)

**原文标题**: Join the Independent Science Society! (A New Kinda Science Society)

**原文链接**: [https://chillphysicsenjoyer.substack.com/p/join-the-independent-science-society](https://chillphysicsenjoyer.substack.com/p/join-the-independent-science-society)

生成摘要时出错

---

## 91. YouTube to automatically label AI-generated videos

**原文标题**: YouTube to automatically label AI-generated videos

**原文链接**: [https://blog.youtube/news-and-events/improving-ai-labels-viewers-creators/](https://blog.youtube/news-and-events/improving-ai-labels-viewers-creators/)

生成摘要时出错

---

## 92. Italians and Dutch share the same gestural instinct for teaching

**原文标题**: Italians and Dutch share the same gestural instinct for teaching

**原文链接**: [https://www.mpi.nl/news/italians-and-dutch-share-same-gestural-instinct-teaching](https://www.mpi.nl/news/italians-and-dutch-share-same-gestural-instinct-teaching)

生成摘要时出错

---

## 93. Volkswagen blocks Home Assistant by requiring client assertion

**原文标题**: Volkswagen blocks Home Assistant by requiring client assertion

**原文链接**: [https://github.com/robinostlund/homeassistant-volkswagencarnet/issues/967](https://github.com/robinostlund/homeassistant-volkswagencarnet/issues/967)

生成摘要时出错

---

## 94. The Kaiser and a "Mediocre Man" Theory of History

**原文标题**: The Kaiser and a "Mediocre Man" Theory of History

**原文链接**: [https://www.deadcarl.com/p/the-kaiser-and-a-mediocre-man-theory](https://www.deadcarl.com/p/the-kaiser-and-a-mediocre-man-theory)

生成摘要时出错

---

## 95. Where are the economies of scale in homebuilding?

**原文标题**: Where are the economies of scale in homebuilding?

**原文链接**: [https://www.construction-physics.com/p/where-are-the-economies-of-scale](https://www.construction-physics.com/p/where-are-the-economies-of-scale)

生成摘要时出错

---

## 96. Why I collect DLES

**原文标题**: Why I collect DLES

**原文链接**: [https://dles.gg/blog/dles-gg-manifesto](https://dles.gg/blog/dles-gg-manifesto)

生成摘要时出错

---

## 97. Robinhood now lets your AI agents trade stocks

**原文标题**: Robinhood now lets your AI agents trade stocks

**原文链接**: [https://techcrunch.com/2026/05/27/robinhood-now-lets-your-ai-agents-trade-stocks/](https://techcrunch.com/2026/05/27/robinhood-now-lets-your-ai-agents-trade-stocks/)

生成摘要时出错

---

## 98. HeidiSQL – Lightweight MariaDB, MySQL, SQL Server, PostgreSQL and SQLite Manager

**原文标题**: HeidiSQL – Lightweight MariaDB, MySQL, SQL Server, PostgreSQL and SQLite Manager

**原文链接**: [https://github.com/HeidiSQL/HeidiSQL](https://github.com/HeidiSQL/HeidiSQL)

生成摘要时出错

---

## 99. Tulip mania: when a single flower was worth more than a house (2025)

**原文标题**: Tulip mania: when a single flower was worth more than a house (2025)

**原文链接**: [https://dutchreview.com/culture/tulip-mania-netherlands/](https://dutchreview.com/culture/tulip-mania-netherlands/)

生成摘要时出错

---

## 100. Ho-scale slot car racing in the Santa Cruz Mountains

**原文标题**: Ho-scale slot car racing in the Santa Cruz Mountains

**原文链接**: [https://stewartraceway.org/](https://stewartraceway.org/)

生成摘要时出错

---

