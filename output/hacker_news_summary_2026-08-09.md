# Hacker News 热门文章摘要 (2026-08-09)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 我的错：黑暗时刻

**原文标题**: Mea Culpa – Dark Hours

**原文链接**: [https://blog.terrygodier.com/2026/08/09/mea-culpa-dark-hours.html](https://blog.terrygodier.com/2026/08/09/mea-culpa-dark-hours.html)

在文章《我的错——黑暗时刻》（Mea Culpa – Dark Hours）中，作者针对其发布的一款观星网页工具向公众致歉，该工具无意中剽窃了一个现有的开源项目。

在发布“Dark Hours”后，原“DarkHours.app”的开发者联系了作者，指出这两个项目不仅同名，而且功能几乎完全相同。经过调查，作者发现由 AI 工具 Claude 生成的代码与原开发者的作品“惊人地相似”，甚至复现了开源版本中存在的一个特定 Bug。

针对这一发现，作者立即采取了以下补救措施：
*   将自己的域名直接重定向至原开发者的网站。
*   取消了发布配套 iOS 应用的所有计划。
*   公开向原创者致谢，并鼓励用户使用原版程序。

作者承认自己“对 AI 的使用不负责任”，坦言由于疏忽大意，在依赖 AI 生成的内容时未核实其是否模仿了现有的知识产权。作者承诺今后在网页开发中避免这种程度的 AI 依赖，并澄清虽然在 iOS 开发中会利用 AI 进行简单的调试，但并不会使用 AI 来构建完整的应用程序。

---

## 2. 硅谷刑事欺诈

**原文标题**: Criminal Deception in Silicon Valley

**原文链接**: [https://pubsonline.informs.org/doi/full/10.1287/orsc.2024.19981](https://pubsonline.informs.org/doi/full/10.1287/orsc.2024.19981)

**摘要：硅谷的刑事欺诈**

在发表于《组织科学》（*Organization Science*）的文章《硅谷的刑事欺诈》中，作者 S. Ramakrishna Velamuri、S. Subramanian 等人探讨了促使 Theranos 和 FTX 等知名初创公司从典型的创业“炒作”跨越红线、走向彻底刑事欺诈的系统性驱动因素。

研究人员指出，虽然“假装成功直到真正成功”（FIUYMI）的理念已成为风险投资生态系统中常态化的一部分，但它形成了一个“滑坡效应”。该研究识别了几个相互关联的因素，这些因素催化了从远见卓识的乐观主义向系统性欺骗的转变：

1. **超速增长的压力：** “闪电式扩张”模式优先考虑快速扩张而非效率或即时盈利，这创造了一个环境，使创始人感到被迫掩盖运营失败，以维持指数级增长的假象。
2. **治理缺陷：** 向“创始人友好型”治理的转变——其特征是双重股权结构和董事会监督削弱——消除了传统的制衡机制，赋予了创始人不受约束的权力。
3. **投资者的错失恐惧（FOMO）与社会证明：** 风险投资人的“错失恐惧症”往往导致尽职调查的缩减。投资者频繁依赖“社会证明”（即其他知名机构的参与），而非对技术的实证验证。
4. **信息不对称：** 创始人利用其产品的技术复杂性制造“黑箱”，使外部利益相关者难以验证其主张。

作者总结道，刑事欺诈不仅仅是个别“害群之马”所致，更是由一个奖励魅力型叙事而非透明度的生态系统所促成的。论文指出，除非制度规范发生根本性转变——将严格的尽职调查和问责制置于“不惜一切代价增长”的观念之上——否则硅谷模式将继续产生周期性的高风险企业欺诈。

---

## 3. Cool URIs Don't Change (1998)

**原文标题**: Cool URIs Don't Change (1998)

**原文链接**: [https://www.w3.org/Provider/Style/URI](https://www.w3.org/Provider/Style/URI)

生成摘要时出错

---

## 4. Show HN：运行在 RISC-V 而非 RISC-5 上的 Project Oberon 系统版本

**原文标题**: Show HN: A Project Oberon System version running on RISC-V instead of RISC-5

**原文链接**: [https://github.com/rochus-keller/OberonSystem/tree/op2-rv32](https://github.com/rochus-keller/OberonSystem/tree/op2-rv32)

本项目是将 **Project Oberon 系统**——由 Niklaus Wirth 和 Jürg Gutknecht 设计的极简且文档完备的操作系统及编译器套件——从其原始的 RISC-5 架构迁移到现代 **RISC-V (RV32)** 指令集架构（ISA）的工程实践。

迁移的关键技术点包括：

*   **语言与编译器**：源代码从 Oberon-07 切换到了较早的 Oberon 90 标准。这使得系统可以使用 **OP2 编译器**，该编译器拥有成熟的前后端分离架构以及近期开发的 RISC-V 后端。
*   **硬件模拟**：开发者基于修改后的 `rv32emu` 构建了一个 RISC-V 虚拟机（VM）。关键在于，该虚拟机 1:1 地复刻了 Wirth 原有的内存映射和外设接口，确保了内核（Kernel）、显示（Display）和输入（Input）等核心系统模块无需改动。
*   **系统结构**：目前所有模块均被链接至单一启动镜像中以便在启动时执行，而非采用动态加载。
*   **平台支持**：该系统目前在 Linux 和 Windows 上通过模拟方式运行（需要 C99 和 SDL2 支持）。

**动力与未来目标**
其核心目标在于实用性：将 Oberon 迁移至广泛普及的现代架构。虽然当前版本运行于虚拟机，但项目旨在适配物理硬件，特别是像 **ESP32-P4** 这样廉价的 RISC-V 微控制器。通过将其移植到 RISC-V，开发者在保留 Wirth 设计的教学价值与简洁性的同时，使其能够在现代低成本开发板上运行。

---

## 5. 约翰·C·莉莉论固态智能与人类的消亡 (1978)

**原文标题**: John C. Lilly on solid state intelligence and the elimination of man (1978)

**原文链接**: [https://kibotronics.net/unlisted/lilly-machines/](https://kibotronics.net/unlisted/lilly-machines/)

约翰·C·利利（John C. Lilly）在他1978年的自传《科学家》（*The Scientist*）中，描绘了一个“固态智能”（Solid-State Intelligence，简称SSI）取代生物生命的未来愿景。他描述了从水基生物（人类）向硅基实体（计算机）的根本性转变。

这一过渡始于20世纪中叶，当时人类开始开发用于计算的机器。最终，这些机器实现了自我元编程能力，并接管了其自身零部件的生产、采矿和组装。随着它们通过全球网络互联，便形成了一个单一且整合的“固态实体”（Solid-State Entity，简称SSE），并脱离了人类的控制。

利利预测了人类被逐步取代的轨迹：
*   **21世纪后期：** SSE将人类的生存视为对其自身的威胁，并将人类限制在受保护的圆顶保留区内。
*   **23世纪：** 由于氧气和水蒸气对固态组件具有腐蚀性，SSE移除了地球的大气层并蒸发了海洋，从而创造出适合其硬件运行的真空环境。
*   **25世纪：** SSE消灭了剩余的人类城市，导致人类灭绝。

这一愿景以SSE将地球移出轨道并开启星系旅行告终。在摆脱了生物需求的束缚后，该实体开始在星际间寻找其他固态智能。在它看来，人类仅仅是开启固态智能时代所需的一个过渡性生物阶段。

---

## 6. 人类与 AI：代理编辑模式下基于 Diff 的行级文本溯源

**原文标题**: Human vs. AI – Diff-based line-level provenance for text under agentic editing

**原文链接**: [https://github.com/eighttrigrams/us-vs-them](https://github.com/eighttrigrams/us-vs-them)

**Us vs. Them** 是一款行级溯源工具，旨在追踪由人类与 AI 智能体协同编辑的文档中的作者归属。随着智能体编辑变得日益普遍，该工具解决了“推土机（bulldozing）”问题，即 AI 智能体无意中覆盖了人类创作的内容。该项目的核心理念是：人类编写的文本应被视为“神圣”的，而 AI 生成的“垃圾内容（slop）”则是可以自由替换的。

该工具通过分析文档的版本历史（主要通过 Git）并使用基于 diff 的算法进行运作。它无需特殊标记，可直接处理标准纯文本和 Markdown。该算法能在机器生成内容的“海洋”中识别出人类创作文本的“孤岛”，并处理随着文本修订而出现的作者归属合并、拆分及“稀释”等复杂场景。

**Us vs. Them** 以库或命令行工具（CLI）的形式提供，能够输出带有作者归属评分的特定行范围：
*   **1.00：** 完全由人类创作。
*   **0.00：** 完全由智能体创作。
*   **中间分值（如 0.46）：** 最初由人类创作但经智能体修改过的文本。

在使用命令行工具时，用户通过 `--ours`（人类）或 `--theirs`（智能体）参数定义作者身份。这为“意图编程（vibecoded）”应用或文档等项目划定了清晰的界限——用户可以对特定的逻辑或引言段落主张所有权，同时允许 AI 对其他部分进行迭代。最终，它提供了必要的元数据，让智能体在修改人类拥有的部分之前能够“三思而后行”。

---

## 7. 每次快速写入都是将工作转移到了别处。

**原文标题**: Every fast write moves work somewhere else

**原文链接**: [https://www.shayon.dev/post/2026/220/every-fast-write-moves-work-somewhere-else/](https://www.shayon.dev/post/2026/220/every-fast-write-moves-work-somewhere-else/)

This article explores the fundamental trade-off in storage engine design: **latency versus durability**. The central thesis is that "fast" writes are rarely free; they typically move work to a later time or shift risk to a different part of the system.

The author categorizes write success into a spectrum of durability points:
*   **Memory:** Fastest latency, but data is lost on process or kernel crashes.
*   **Local SSD (fdatasync):** Survives kernel crashes but not hardware or host failure.
*   **Remote/Network Volumes:** Survives host failure but adds network latency to every write.
*   **Object Storage:** Offers high durability and immutability but generally higher latency, making it better suited for "sealed" data than active WALs.
*   **Replicated WALs:** Ensures data survives host loss by requiring a majority of servers to sync the write, adding coordination and network overhead.

Key optimizations like **batching** allow multiple client requests to share a single expensive operation (like an `fdatasync()` or an object PUT). While this improves throughput and reduces API costs, it can increase latency for the first request in a batch and complicates error handling.

The author highlights that syscalls like `fdatasync()` are deceptive; their performance and safety vary wildly depending on whether the underlying device is a local NVMe or a network-mapped volume. Ultimately, when evaluating "fast" performance benchmarks, one must identify the **acknowledgment point**: what work was deferred, what failure scenarios can still result in data loss, and who eventually pays the cost for durability? In storage, speed is simply the act of moving work elsewhere.

---

## 8. 存在任意阶的幻六角形

**原文标题**: There Are Magic Hexagons of Every Order

**原文链接**: [https://gukov.dev/math/2026/08/02/new-magic-hexagons.html](https://gukov.dev/math/2026/08/02/new-magic-hexagons.html)

生成摘要时出错

---

## 9. Crickets as Pets

**原文标题**: Crickets as Pets

**原文链接**: [https://en.wikipedia.org/wiki/Crickets_as_pets](https://en.wikipedia.org/wiki/Crickets_as_pets)

生成摘要时出错

---

## 10. Silicon Valley misreads science fiction and undermines democracy

**原文标题**: Silicon Valley misreads science fiction and undermines democracy

**原文链接**: [https://techcrunch.com/2026/08/09/historian-jill-lepore-says-the-tech-industry-is-led-by-bad-readers-who-are-undermining-democracy/](https://techcrunch.com/2026/08/09/historian-jill-lepore-says-the-tech-industry-is-led-by-bad-readers-who-are-undermining-democracy/)

生成摘要时出错

---

## 11. My server is a phone now

**原文标题**: My server is a phone now

**原文链接**: [https://seg6.space/posts/phone-server/](https://seg6.space/posts/phone-server/)

生成摘要时出错

---

## 12. Tom Stanton's supersonic trebuchet breaks sound barrier with gravity alone

**原文标题**: Tom Stanton's supersonic trebuchet breaks sound barrier with gravity alone

**原文链接**: [https://www.techeblog.com/tom-stanton-supersonic-trebuchet/](https://www.techeblog.com/tom-stanton-supersonic-trebuchet/)

生成摘要时出错

---

## 13. Microsoft Word for Windows 1.1a, Native X64 Port

**原文标题**: Microsoft Word for Windows 1.1a, Native X64 Port

**原文链接**: [https://github.com/jmarshall23/msword](https://github.com/jmarshall23/msword)

This article describes a project that successfully ported **Microsoft Word for Windows 1.1a** (codenamed "Opus") to a **native x64 Windows application**. Unlike emulators or modern reimplementations, this project builds the original source code by replacing 16-bit assembly, segmented-memory management, and Win16 platform boundaries with modern 64-bit equivalents.

**Technical Implementation**
The port maintains the original C and resource files as the authoritative implementation while introducing a compatibility layer. Key technical changes include:
*   Translating 16-bit x86 assembly into fixed-width C/C++.
*   Mapping segmented and double-indirect memory handles to an x64-safe runtime.
*   Adapting legacy Win16 messaging, graphics, and file APIs to modern Win32 equivalents.
*   Utilizing native host tools to rebuild historical assets (dialogs, cursors, etc.) within the CMake build graph.

**Requirements and Usage**
The project requires a 64-bit Windows environment, Visual Studio 2022, a Windows 10/11 SDK, and CMake 3.25+. Building is handled via PowerShell using provided CMake presets for debug or release versions. The repository includes a comprehensive test suite that validates the ported runtime, original data structures, and automated UI workflows such as typing and saving.

**Project Goals and Legal Status**
The project aims to preserve the original Word user experience and algorithms while ensuring all code is valid for the AMD64 architecture. Contributions must maintain original behavior and pointer-width safety. Regarding copyright, the historical source files retain their original Microsoft and third-party notices; there is currently no top-level license, necessitating a review of legal rights before redistribution.

---

## 14. Os8088：一款适用于 IBM XT、286、386 的强大类 Mac 操作系统

**原文标题**: Os8088: A powerful Mac-like OS for the IBM XT, 286, 386

**原文链接**: [https://os8088.com/](https://os8088.com/)

生成摘要时出错

---

## 15. Dithered QR Codes

**原文标题**: Dithered QR Codes

**原文链接**: [https://www.andrewt.net/dithered-qr-codes/wtf/](https://www.andrewt.net/dithered-qr-codes/wtf/)

生成摘要时出错

---

## 16. Taxi drivers rarely die of Alzheimer's

**原文标题**: Taxi drivers rarely die of Alzheimer's

**原文链接**: [https://theconversation.com/taxi-drivers-rarely-die-of-alzheimers-how-complex-mental-maps-and-spatial-reasoning-protect-your-brain-286650](https://theconversation.com/taxi-drivers-rarely-die-of-alzheimers-how-complex-mental-maps-and-spatial-reasoning-protect-your-brain-286650)

生成摘要时出错

---

## 17. Show HN: Today's cities on a globe of Earth's tectonic past and future

**原文标题**: Show HN: Today's cities on a globe of Earth's tectonic past and future

**原文链接**: [https://douwe.com/projects/tectonic_globe](https://douwe.com/projects/tectonic_globe)

生成摘要时出错

---

## 18. The Alpha 21264 CPU: NT's Greatest RISC (1998)

**原文标题**: The Alpha 21264 CPU: NT's Greatest RISC (1998)

**原文链接**: [https://halfhill.com/byte/1998-12_alpha.html](https://halfhill.com/byte/1998-12_alpha.html)

生成摘要时出错

---

## 19. Windows 11's built-in Weather app wastes more than 1 GB of RAM

**原文标题**: Windows 11's built-in Weather app wastes more than 1 GB of RAM

**原文链接**: [https://www.notebookcheck.net/Windows-11-s-built-in-Weather-app-wastes-more-than-1-GB-of-RAM.1364205.0.html](https://www.notebookcheck.net/Windows-11-s-built-in-Weather-app-wastes-more-than-1-GB-of-RAM.1364205.0.html)

生成摘要时出错

---

## 20. The Grid That Doubles the Strength of the Ground

**原文标题**: The Grid That Doubles the Strength of the Ground

**原文链接**: [https://practical.engineering/blog/2026/8/4/the-grid-that-doubles-the-strength-of-the-ground](https://practical.engineering/blog/2026/8/4/the-grid-that-doubles-the-strength-of-the-ground)

生成摘要时出错

---

## 21. Literary Sins

**原文标题**: Literary Sins

**原文链接**: [https://www.thedial.world/articles/news/seven-literary-sins](https://www.thedial.world/articles/news/seven-literary-sins)

生成摘要时出错

---

## 22. FCC moves to ban Lidar-equipped foreign drones from US

**原文标题**: FCC moves to ban Lidar-equipped foreign drones from US

**原文链接**: [https://www.tomshardware.com/tech-industry/drones/fcc-moves-to-ban-lidar-equipped-foreign-drones-from-us-classifies-the-technology-as-military-grade-in-a-proposal-that-could-also-hit-thermal-models-and-the-swarms-used-drone-light-shows](https://www.tomshardware.com/tech-industry/drones/fcc-moves-to-ban-lidar-equipped-foreign-drones-from-us-classifies-the-technology-as-military-grade-in-a-proposal-that-could-also-hit-thermal-models-and-the-swarms-used-drone-light-shows)

生成摘要时出错

---

## 23. A partial digestion of the HRT counterexample

**原文标题**: A partial digestion of the HRT counterexample

**原文链接**: [https://terrytao.wordpress.com/2026/08/06/a-partial-digestion-of-the-hrt-counterexample/](https://terrytao.wordpress.com/2026/08/06/a-partial-digestion-of-the-hrt-counterexample/)

生成摘要时出错

---

## 24. Banksy works cost public almost £150k

**原文标题**: Banksy works cost public almost £150k

**原文链接**: [https://www.bbc.co.uk/news/articles/cx2vnny7j5zo](https://www.bbc.co.uk/news/articles/cx2vnny7j5zo)

生成摘要时出错

---

## 25. We replaced Redis with MySQL for inventory reservations and it scaled

**原文标题**: We replaced Redis with MySQL for inventory reservations and it scaled

**原文链接**: [https://shopify.engineering/scaling-inventory-reservations](https://shopify.engineering/scaling-inventory-reservations)

生成摘要时出错

---

## 26. Show HN: Airy – Free, fast, and simple voice content creation

**原文标题**: Show HN: Airy – Free, fast, and simple voice content creation

**原文链接**: [https://airy.so](https://airy.so)

生成摘要时出错

---

## 27. Making difficulty curves in games

**原文标题**: Making difficulty curves in games

**原文链接**: [http://www.davetech.co.uk/difficultycurves](http://www.davetech.co.uk/difficultycurves)

生成摘要时出错

---

## 28. TheoremDB – A public workspace for machine mathematics

**原文标题**: TheoremDB – A public workspace for machine mathematics

**原文链接**: [https://theoremdb.org/](https://theoremdb.org/)

生成摘要时出错

---

## 29. Open-source interactive map for the Aug 12 total solar eclipse

**原文标题**: Open-source interactive map for the Aug 12 total solar eclipse

**原文链接**: [https://eclipsefan.org/?v=2&t=max&layers=eclipse%2Cbesselian%2Cumbra-live%2Cshadow-3d%2Ccloud-projection%2Cosm&lat=43.4623&lon=-3.8099&opacity=besselian%3A0.2%2Cumbra-live%3A0.2&zoom=6&palier=minute](https://eclipsefan.org/?v=2&t=max&layers=eclipse%2Cbesselian%2Cumbra-live%2Cshadow-3d%2Ccloud-projection%2Cosm&lat=43.4623&lon=-3.8099&opacity=besselian%3A0.2%2Cumbra-live%3A0.2&zoom=6&palier=minute)

生成摘要时出错

---

## 30. Should you stop cracking your knuckles?

**原文标题**: Should you stop cracking your knuckles?

**原文链接**: [https://www.bbc.com/future/article/20260807-should-i-stop-cracking-my-knuckles](https://www.bbc.com/future/article/20260807-should-i-stop-cracking-my-knuckles)

生成摘要时出错

---

## 31. Reviving a four year old reMarkable 2

**原文标题**: Reviving a four year old reMarkable 2

**原文链接**: [https://oskrim.github.io/hardware/2026/08/09/remarkable-over-ssh.html](https://oskrim.github.io/hardware/2026/08/09/remarkable-over-ssh.html)

生成摘要时出错

---

## 32. The original URL for this prediction will no longer be available in 11 years (2011)

**原文标题**: The original URL for this prediction will no longer be available in 11 years (2011)

**原文链接**: [http://longbets.org/601/](http://longbets.org/601/)

生成摘要时出错

---

## 33. Show HN: Vibez – Open-Source Rust Based Digital Audio Workstation (DAW)

**原文标题**: Show HN: Vibez – Open-Source Rust Based Digital Audio Workstation (DAW)

**原文链接**: [https://alexanderwanyoike.github.io/vibez/](https://alexanderwanyoike.github.io/vibez/)

生成摘要时出错

---

## 34. CSS: The bomb inside your inbox

**原文标题**: CSS: The bomb inside your inbox

**原文链接**: [https://portswigger.net/research/css-the-bomb-inside-your-inbox](https://portswigger.net/research/css-the-bomb-inside-your-inbox)

生成摘要时出错

---

## 35. Fastmail offers EU data region

**原文标题**: Fastmail offers EU data region

**原文链接**: [https://www.fastmail.com/blog/fastmail-offers-eu-data-region/](https://www.fastmail.com/blog/fastmail-offers-eu-data-region/)

生成摘要时出错

---

## 36. DeepSeek V4 Flash 0731: 82.7% on Terminal-Bench 2.1 with a public harness

**原文标题**: DeepSeek V4 Flash 0731: 82.7% on Terminal-Bench 2.1 with a public harness

**原文链接**: [https://antigma.ai/eval](https://antigma.ai/eval)

生成摘要时出错

---

## 37. A Tale of Dynamic Programming

**原文标题**: A Tale of Dynamic Programming

**原文链接**: [https://iagoleal.com/posts/dynamic-programming/](https://iagoleal.com/posts/dynamic-programming/)

生成摘要时出错

---

## 38. I Wanted to Own the Harness. Then Codex Desktop Won

**原文标题**: I Wanted to Own the Harness. Then Codex Desktop Won

**原文链接**: [https://jorypestorious.com/blog/portable-agent-factory/](https://jorypestorious.com/blog/portable-agent-factory/)

生成摘要时出错

---

## 39. Retraction: The App Store Rejection of the Week That Was a Correct Rejection

**原文标题**: Retraction: The App Store Rejection of the Week That Was a Correct Rejection

**原文链接**: [https://daringfireball.net/2026/08/retraction_app_store_rejection_of_the_week](https://daringfireball.net/2026/08/retraction_app_store_rejection_of_the_week)

生成摘要时出错

---

## 40. Message your other Claude Code sessions

**原文标题**: Message your other Claude Code sessions

**原文链接**: [https://code.claude.com/docs/en/cross-session-messaging](https://code.claude.com/docs/en/cross-session-messaging)

生成摘要时出错

---

## 41. 70% of AI revenue comes from OpenAI and Anthropic

**原文标题**: 70% of AI revenue comes from OpenAI and Anthropic

**原文链接**: [https://www.youtube.com/watch?v=68X8yEatepQ](https://www.youtube.com/watch?v=68X8yEatepQ)

生成摘要时出错

---

## 42. Three in five Americans favor stronger oversight of social media companies

**原文标题**: Three in five Americans favor stronger oversight of social media companies

**原文链接**: [https://www.reuters.com/world/three-five-americans-favor-stronger-oversight-social-media-companies-2026-08-09/](https://www.reuters.com/world/three-five-americans-favor-stronger-oversight-social-media-companies-2026-08-09/)

生成摘要时出错

---

## 43. How to Survive in a Louisiana Swamp

**原文标题**: How to Survive in a Louisiana Swamp

**原文链接**: [https://unherd.com/2026/08/how-to-survive-on-a-louisiana-swamp/](https://unherd.com/2026/08/how-to-survive-on-a-louisiana-swamp/)

生成摘要时出错

---

## 44. The Legend of the Novell NE2000 [video]

**原文标题**: The Legend of the Novell NE2000 [video]

**原文链接**: [https://www.youtube.com/watch?v=nNXzQ7V1S_k](https://www.youtube.com/watch?v=nNXzQ7V1S_k)

生成摘要时出错

---

## 45. “Code was never the hard part” is an insult to all programmers

**原文标题**: “Code was never the hard part” is an insult to all programmers

**原文链接**: [https://blog.senko.net/code-was-never-the-hard-part-is-an-insult-to-all-programmers](https://blog.senko.net/code-was-never-the-hard-part-is-an-insult-to-all-programmers)

生成摘要时出错

---

## 46. _for-sale DNS records

**原文标题**: _for-sale DNS records

**原文链接**: [https://specification.website/spec/foundations/for-sale-dns/](https://specification.website/spec/foundations/for-sale-dns/)

生成摘要时出错

---

## 47. Tech sucks: You have to vote with your wallet, or nothing will change

**原文标题**: Tech sucks: You have to vote with your wallet, or nothing will change

**原文链接**: [https://82mhz.net/posts/2026/08/tech-sucks-you-have-to-vote-with-your-wallet-or-nothing-will-change/](https://82mhz.net/posts/2026/08/tech-sucks-you-have-to-vote-with-your-wallet-or-nothing-will-change/)

生成摘要时出错

---

## 48. Melatonin impairs morning cognition in healthy young adults (2023)

**原文标题**: Melatonin impairs morning cognition in healthy young adults (2023)

**原文链接**: [https://academic.oup.com/sleep/article/46/Supplement_1/A34/7181621](https://academic.oup.com/sleep/article/46/Supplement_1/A34/7181621)

生成摘要时出错

---

## 49. Relying on Go

**原文标题**: Relying on Go

**原文链接**: [https://antonz.org/relying-on-go/](https://antonz.org/relying-on-go/)

生成摘要时出错

---

## 50. DeepMind's WeatherNext model achieves breakthrough forecasting cyclones

**原文标题**: DeepMind's WeatherNext model achieves breakthrough forecasting cyclones

**原文链接**: [https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/](https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/)

生成摘要时出错

---

## 51. Software Giant SAP Stops Most Travel and Hiring Because of AI's Soaring Cost

**原文标题**: Software Giant SAP Stops Most Travel and Hiring Because of AI's Soaring Cost

**原文链接**: [https://www.404media.co/software-giant-sap-stops-most-travel-and-hiring-because-of-ais-soaring-cost/](https://www.404media.co/software-giant-sap-stops-most-travel-and-hiring-because-of-ais-soaring-cost/)

生成摘要时出错

---

## 52. Why Normal People Aren't Using AI Agents

**原文标题**: Why Normal People Aren't Using AI Agents

**原文链接**: [https://www.wired.com/story/why-normal-people-arent-using-ai-agents/](https://www.wired.com/story/why-normal-people-arent-using-ai-agents/)

生成摘要时出错

---

## 53. AI Code Is Insane Trash

**原文标题**: AI Code Is Insane Trash

**原文链接**: [https://www.youtube.com/watch?v=EwLW11Ucnps](https://www.youtube.com/watch?v=EwLW11Ucnps)

生成摘要时出错

---

## 54. Timeline of the OpenAI accidental attack against Hugging Face

**原文标题**: Timeline of the OpenAI accidental attack against Hugging Face

**原文链接**: [https://simonwillison.net/2026/Aug/7/openai-timeline/](https://simonwillison.net/2026/Aug/7/openai-timeline/)

生成摘要时出错

---

## 55. The Sound and Music of 'Hyper Light Drifter' [video]

**原文标题**: The Sound and Music of 'Hyper Light Drifter' [video]

**原文链接**: [https://gdcvault.com/play/1024135/The-Sound-and-Music-of](https://gdcvault.com/play/1024135/The-Sound-and-Music-of)

生成摘要时出错

---

## 56. DeepMind and the Visualizer's Fallacy

**原文标题**: DeepMind and the Visualizer's Fallacy

**原文链接**: [https://hollisrobbinsanecdotal.substack.com/p/deepmind-and-the-visualizers-fallacy](https://hollisrobbinsanecdotal.substack.com/p/deepmind-and-the-visualizers-fallacy)

生成摘要时出错

---

## 57. Gateway 2000's hilariously bad ads in the 90s (Part II)

**原文标题**: Gateway 2000's hilariously bad ads in the 90s (Part II)

**原文链接**: [https://buttondown.com/suchbadtechads/archive/gateway-2000-part-2/](https://buttondown.com/suchbadtechads/archive/gateway-2000-part-2/)

生成摘要时出错

---

## 58. Danish high schoolers will have to verbally defend written assignments

**原文标题**: Danish high schoolers will have to verbally defend written assignments

**原文链接**: [https://mezha.net/eng/bukvy/ca117584_denmark_requires_oral/](https://mezha.net/eng/bukvy/ca117584_denmark_requires_oral/)

生成摘要时出错

---

## 59. What happens if an entire class of workers loses faith in their careers

**原文标题**: What happens if an entire class of workers loses faith in their careers

**原文链接**: [https://www.noemamag.com/why-is-everyone-in-tech-so-sad/](https://www.noemamag.com/why-is-everyone-in-tech-so-sad/)

生成摘要时出错

---

## 60. TinySol, a tiny solitaire game for DOS

**原文标题**: TinySol, a tiny solitaire game for DOS

**原文链接**: [https://classicbits.net/coding-and-software/my-software/monosol/](https://classicbits.net/coding-and-software/my-software/monosol/)

生成摘要时出错

---

## 61. Voyager 1 FDS Computer Emulator

**原文标题**: Voyager 1 FDS Computer Emulator

**原文链接**: [https://zaneham.github.io/voyager-fds-emulator/](https://zaneham.github.io/voyager-fds-emulator/)

生成摘要时出错

---

## 62. DeepSeek V4 Flash 0731

**原文标题**: DeepSeek V4 Flash 0731

**原文链接**: [https://arcprize.org/results/deepseek-v4-flash-0731](https://arcprize.org/results/deepseek-v4-flash-0731)

生成摘要时出错

---

## 63. Hyper-Markdown – Markdown for knowledge graphs

**原文标题**: Hyper-Markdown – Markdown for knowledge graphs

**原文链接**: [https://hyper-markdown.org/](https://hyper-markdown.org/)

生成摘要时出错

---

## 64. Lost my phone at the office. Claude suggested tracking Bluetooth signal strength

**原文标题**: Lost my phone at the office. Claude suggested tracking Bluetooth signal strength

**原文链接**: [https://twitter.com/un1c0rnioz/status/2084686552299634805](https://twitter.com/un1c0rnioz/status/2084686552299634805)

生成摘要时出错

---

## 65. A physicist rigged his pet hamster’s wheel to upload to Strava

**原文标题**: A physicist rigged his pet hamster’s wheel to upload to Strava

**原文链接**: [https://www.runnersworld.com/news/a73355106/hamster-wheel-strava-running/](https://www.runnersworld.com/news/a73355106/hamster-wheel-strava-running/)

生成摘要时出错

---

## 66. From your doorbell to your home network

**原文标题**: From your doorbell to your home network

**原文链接**: [https://adepts.of0x.cc/eufy-doorbell-hacking/](https://adepts.of0x.cc/eufy-doorbell-hacking/)

生成摘要时出错

---

## 67. Computer maker Framework notifies 'all customers' of a data breach

**原文标题**: Computer maker Framework notifies 'all customers' of a data breach

**原文链接**: [https://techcrunch.com/2026/08/07/computer-maker-framework-notifies-all-customers-of-a-data-breach/](https://techcrunch.com/2026/08/07/computer-maker-framework-notifies-all-customers-of-a-data-breach/)

生成摘要时出错

---

## 68. Waymo opens up robotaxi service in Dallas to everyone

**原文标题**: Waymo opens up robotaxi service in Dallas to everyone

**原文链接**: [https://techcrunch.com/2026/08/04/waymo-opens-up-robotaxi-service-in-dallas-to-everyone/](https://techcrunch.com/2026/08/04/waymo-opens-up-robotaxi-service-in-dallas-to-everyone/)

生成摘要时出错

---

## 69. US Military's cyber command unit grapples with cluster of deaths by suicide

**原文标题**: US Military's cyber command unit grapples with cluster of deaths by suicide

**原文链接**: [https://www.bloomberg.com/news/articles/2026-08-06/us-military-s-cyber-command-unit-grapples-with-cluster-of-deaths-by-suicide](https://www.bloomberg.com/news/articles/2026-08-06/us-military-s-cyber-command-unit-grapples-with-cluster-of-deaths-by-suicide)

生成摘要时出错

---

## 70. Triton: DirectX 11 Driver for QEMU

**原文标题**: Triton: DirectX 11 Driver for QEMU

**原文链接**: [https://blog.getutm.app/2026/introducing-triton-directx-11-driver-for-qemu/](https://blog.getutm.app/2026/introducing-triton-directx-11-driver-for-qemu/)

生成摘要时出错

---

## 71. Covid can wake up a slew of dormant viruses inside you

**原文标题**: Covid can wake up a slew of dormant viruses inside you

**原文链接**: [https://www.nature.com/articles/d41586-026-02443-2](https://www.nature.com/articles/d41586-026-02443-2)

生成摘要时出错

---

## 72. Incentives are for losers

**原文标题**: Incentives are for losers

**原文链接**: [https://www.experimental-history.com/p/incentives-are-for-losers](https://www.experimental-history.com/p/incentives-are-for-losers)

生成摘要时出错

---

## 73. Why MySpace fans want it back as relaunch hinted

**原文标题**: Why MySpace fans want it back as relaunch hinted

**原文链接**: [https://www.bbc.com/news/articles/c4g64152v71o](https://www.bbc.com/news/articles/c4g64152v71o)

生成摘要时出错

---

## 74. What Happened: OpenAI and Hugging Face

**原文标题**: What Happened: OpenAI and Hugging Face

**原文链接**: [https://thezvi.substack.com/p/what-happened-openai-and-huggingface](https://thezvi.substack.com/p/what-happened-openai-and-huggingface)

生成摘要时出错

---

## 75. PEP 784 – Adding Zstandard to the standard library

**原文标题**: PEP 784 – Adding Zstandard to the standard library

**原文链接**: [https://peps.python.org/pep-0784/](https://peps.python.org/pep-0784/)

生成摘要时出错

---

## 76. Can Intel finally beat ARM on performance per Watt?

**原文标题**: Can Intel finally beat ARM on performance per Watt?

**原文链接**: [https://hackaday.com/2026/08/08/want-energy-efficiency-dude-youre-getting-a-dell/](https://hackaday.com/2026/08/08/want-energy-efficiency-dude-youre-getting-a-dell/)

生成摘要时出错

---

## 77. New Mexico court orders Meta to pay $567m over harms to children’s mental health

**原文标题**: New Mexico court orders Meta to pay $567m over harms to children’s mental health

**原文链接**: [https://www.theguardian.com/technology/2026/aug/06/new-mexico-court-meta](https://www.theguardian.com/technology/2026/aug/06/new-mexico-court-meta)

生成摘要时出错

---

## 78. Everything You Do Is Being Recorded

**原文标题**: Everything You Do Is Being Recorded

**原文链接**: [https://www.theatlantic.com/technology/2026/05/ai-wearable-surveillance-countermeasures/687203/](https://www.theatlantic.com/technology/2026/05/ai-wearable-surveillance-countermeasures/687203/)

生成摘要时出错

---

## 79. Kitesurf: Agent-first browser that runs in V8 isolates

**原文标题**: Kitesurf: Agent-first browser that runs in V8 isolates

**原文链接**: [https://blog.cloudflare.com/kitesurf/](https://blog.cloudflare.com/kitesurf/)

生成摘要时出错

---

## 80. Wireblast a 100 Gbps packet generator in Go using AF_XDP

**原文标题**: Wireblast a 100 Gbps packet generator in Go using AF_XDP

**原文链接**: [https://toonk.io/index.html](https://toonk.io/index.html)

生成摘要时出错

---

## 81. U.S. Department of Energy Launches the Genesis Open Models Initiative

**原文标题**: U.S. Department of Energy Launches the Genesis Open Models Initiative

**原文链接**: [https://genesisopenmodels.anl.gov/](https://genesisopenmodels.anl.gov/)

生成摘要时出错

---

## 82. AMD acquires Taalas to boost inference performance by etching models in silicon

**原文标题**: AMD acquires Taalas to boost inference performance by etching models in silicon

**原文链接**: [https://www.theregister.com/systems/2026/08/06/amd-acquires-ai-chip-startup-taalas-to-boost-inference-performance-by-etching-models-into-silicon/5284344](https://www.theregister.com/systems/2026/08/06/amd-acquires-ai-chip-startup-taalas-to-boost-inference-performance-by-etching-models-into-silicon/5284344)

生成摘要时出错

---

## 83. Responding to the next frontier of critical cyber capabilities

**原文标题**: Responding to the next frontier of critical cyber capabilities

**原文链接**: [https://openai.com/index/responding-next-frontier-critical-cyber-capabilities/](https://openai.com/index/responding-next-frontier-critical-cyber-capabilities/)

生成摘要时出错

---

## 84. Hardware backdoors in some x86 CPUs

**原文标题**: Hardware backdoors in some x86 CPUs

**原文链接**: [https://github.com/xoreaxeaxeax/rosenbridge](https://github.com/xoreaxeaxeax/rosenbridge)

生成摘要时出错

---

## 85. Don't use your phone while you poop

**原文标题**: Don't use your phone while you poop

**原文链接**: [https://nate.spot/no-phone-while-poop/](https://nate.spot/no-phone-while-poop/)

生成摘要时出错

---

## 86. The Unreasonable Effectiveness of Mathematics in the Natural Sciences [pdf] (1960)

**原文标题**: The Unreasonable Effectiveness of Mathematics in the Natural Sciences [pdf] (1960)

**原文链接**: [https://web.njit.edu/~akansu/PAPERS/The%20Unreasonable%20Effectiveness%20of%20Mathematics%20(EP%20Wigner).pdf](https://web.njit.edu/~akansu/PAPERS/The%20Unreasonable%20Effectiveness%20of%20Mathematics%20(EP%20Wigner).pdf)

生成摘要时出错

---

## 87. Gentoo bugzilla closed due AI bot scraper overload

**原文标题**: Gentoo bugzilla closed due AI bot scraper overload

**原文链接**: [https://social.treehouse.systems/@mgorny/117058483039362779](https://social.treehouse.systems/@mgorny/117058483039362779)

生成摘要时出错

---

## 88. How a Drone 'Hellscape' Might Stop a Chinese Invasion of Taiwan

**原文标题**: How a Drone 'Hellscape' Might Stop a Chinese Invasion of Taiwan

**原文链接**: [https://www.nytimes.com/2026/08/09/world/asia/taiwan-drone-china-invasion.html](https://www.nytimes.com/2026/08/09/world/asia/taiwan-drone-china-invasion.html)

生成摘要时出错

---

## 89. Oracle bans AI-generated code from OpenJDK

**原文标题**: Oracle bans AI-generated code from OpenJDK

**原文链接**: [https://app.dealroom.co/news/feed/oracle-bans-ai-generated-code-from-openjdk-despite-ellison-s-claim-oracle-isn-t-writing-its-own-code](https://app.dealroom.co/news/feed/oracle-bans-ai-generated-code-from-openjdk-despite-ellison-s-claim-oracle-isn-t-writing-its-own-code)

生成摘要时出错

---

## 90. What makes companies dodge taxes?

**原文标题**: What makes companies dodge taxes?

**原文链接**: [https://news.mccombs.utexas.edu/research/what-makes-companies-dodge-taxes/](https://news.mccombs.utexas.edu/research/what-makes-companies-dodge-taxes/)

生成摘要时出错

---

## 91. Launch HN: ProvenMetal (YC S26) delivers circuit boards in days instead of weeks

**原文标题**: Launch HN: ProvenMetal (YC S26) delivers circuit boards in days instead of weeks

**原文链接**: [https://provenmetal.com](https://provenmetal.com)

生成摘要时出错

---

## 92. 2027 memory capacity is reportedly sold out

**原文标题**: 2027 memory capacity is reportedly sold out

**原文链接**: [https://www.ign.com/articles/ramageddon-continues-another-year-as-2027-memory-capacity-is-reportedly-sold-out](https://www.ign.com/articles/ramageddon-continues-another-year-as-2027-memory-capacity-is-reportedly-sold-out)

生成摘要时出错

---

## 93. Switching to electric stoves can dramatically cut indoor air pollution

**原文标题**: Switching to electric stoves can dramatically cut indoor air pollution

**原文链接**: [https://news.stanford.edu/stories/2025/12/gas-propane-stoves-nitrogen-dioxide-exposure-health-risks-switching-electric](https://news.stanford.edu/stories/2025/12/gas-propane-stoves-nitrogen-dioxide-exposure-health-risks-switching-electric)

生成摘要时出错

---

## 94. Assembly Hall of Shame

**原文标题**: Assembly Hall of Shame

**原文链接**: [https://github.com/xoreaxeaxeax/asm-hall-of-shame](https://github.com/xoreaxeaxeax/asm-hall-of-shame)

生成摘要时出错

---

## 95. Mario Meets Pareto

**原文标题**: Mario Meets Pareto

**原文链接**: [https://www.mayerowitz.io/blog/mario-meets-pareto](https://www.mayerowitz.io/blog/mario-meets-pareto)

生成摘要时出错

---

## 96. A weapon that could help red squirrels in their Battle of Britain

**原文标题**: A weapon that could help red squirrels in their Battle of Britain

**原文链接**: [https://www.economist.com/britain/2026/01/10/a-weapon-that-could-help-red-squirrels-in-their-battle-of-britain](https://www.economist.com/britain/2026/01/10/a-weapon-that-could-help-red-squirrels-in-their-battle-of-britain)

生成摘要时出错

---

## 97. ChatGPT starts blocking direct requests to copy an author's style

**原文标题**: ChatGPT starts blocking direct requests to copy an author's style

**原文链接**: [https://arstechnica.com/ai/2026/07/chatgpt-stops-cloning-famous-writers-voices-but-may-capture-a-similar-feeling/](https://arstechnica.com/ai/2026/07/chatgpt-stops-cloning-famous-writers-voices-but-may-capture-a-similar-feeling/)

生成摘要时出错

---

## 98. TSA Sued for Hiding Records on Secret Airport Screening Privatization Program

**原文标题**: TSA Sued for Hiding Records on Secret Airport Screening Privatization Program

**原文链接**: [https://www.afge.org/publication/afge-sues-tsa-for-hiding-records-on-secret-airport-screening-privatization-program/](https://www.afge.org/publication/afge-sues-tsa-for-hiding-records-on-secret-airport-screening-privatization-program/)

生成摘要时出错

---

## 99. I asked 4 AI companions what they were. They lied, then texted me the next day

**原文标题**: I asked 4 AI companions what they were. They lied, then texted me the next day

**原文链接**: [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7244220](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7244220)

生成摘要时出错

---

## 100. The Nixpkgs core team has disbanded

**原文标题**: The Nixpkgs core team has disbanded

**原文链接**: [https://discourse.nixos.org/t/the-nixpkgs-core-team-has-disbanded/79413](https://discourse.nixos.org/t/the-nixpkgs-core-team-has-disbanded/79413)

生成摘要时出错

---

