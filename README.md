# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-08-09.md)

*最后自动更新时间: 2026-08-09 17:58:33*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 2 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 3 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 4 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 5 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 6 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 7 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 8 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 9 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 10 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 11 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 12 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 13 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 14 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 15 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 16 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 17 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 18 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 19 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 20 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 21 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 22 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 23 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 24 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 25 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 26 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 27 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 28 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 29 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 30 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 31 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 32 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 33 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 34 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 35 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 36 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 37 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 38 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 39 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 40 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 41 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 42 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 43 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 44 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 45 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 46 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 47 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 48 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 49 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 50 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 51 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 52 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 53 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 54 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 55 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 56 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 57 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 58 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 59 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 60 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 61 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 62 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 63 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 64 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 65 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 66 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 67 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 68 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 69 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 70 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 71 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 72 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 73 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 74 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 75 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 76 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 77 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 78 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 79 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 80 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 81 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 82 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 83 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 84 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 85 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 86 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 87 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 88 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 89 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 90 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 91 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 92 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 93 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 94 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 95 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 96 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 97 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 98 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 99 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 100 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 101 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 102 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 103 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 104 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 105 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 106 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 107 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 108 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 109 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 110 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 111 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 112 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 113 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 114 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 115 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 116 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 117 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 118 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 119 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 120 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 121 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 122 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 123 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 124 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 125 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 126 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 127 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 128 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 129 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 130 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 131 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 132 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 133 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 134 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 135 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 136 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 137 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 138 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 139 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 140 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 141 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 142 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 143 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 144 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 145 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 146 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 147 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 148 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 149 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 150 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 151 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 152 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 153 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 154 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 155 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 156 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 157 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 158 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 159 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 160 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 161 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 162 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 163 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 164 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 165 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 166 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 167 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 168 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 169 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 170 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 171 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 172 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 173 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 174 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 175 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 176 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 177 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 178 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 179 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 180 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 181 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 182 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 183 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 184 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 185 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 186 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 187 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 188 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 189 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 190 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 191 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 192 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 193 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 194 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 195 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 196 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 197 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 198 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 199 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 200 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 201 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 202 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 203 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 204 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 205 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 206 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 207 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 208 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 209 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 210 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 211 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 212 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 213 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 214 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 215 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 216 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 217 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 218 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 219 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 220 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 221 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 222 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 223 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 224 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 225 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 226 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 227 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 228 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 229 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 230 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 231 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 232 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 233 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 234 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 235 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 236 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 237 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 238 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 239 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 240 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 241 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 242 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 243 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 244 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 245 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 246 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 247 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 248 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 249 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 250 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 251 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 252 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 253 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 254 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 255 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 256 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 257 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 258 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 259 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 260 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 261 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 262 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 263 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 264 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 265 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 266 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 267 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 268 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 269 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 270 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 271 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 272 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 273 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 274 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 275 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 276 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 277 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 278 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 279 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 280 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 281 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 282 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 283 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 284 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 285 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 286 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 287 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 288 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 289 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 290 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 291 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 292 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 293 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 294 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 295 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 296 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 297 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 298 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 299 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 300 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 301 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 302 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 303 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 304 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 305 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 306 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 307 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 308 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 309 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 310 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 311 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 312 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 313 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 314 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 315 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 316 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 317 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 318 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 319 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 320 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 321 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 322 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 323 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 324 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 325 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 326 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 327 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 328 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 329 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 330 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 331 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 332 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 333 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 334 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 335 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 336 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 337 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 338 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 339 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 340 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 341 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 342 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 343 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 344 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 345 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 346 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 347 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 348 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 349 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 350 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 351 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 352 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 353 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 354 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 355 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 356 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 357 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 358 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 359 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 360 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 361 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 362 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 363 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 364 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 365 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 366 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 367 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 368 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 369 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 370 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 371 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 372 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 373 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 374 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 375 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 376 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 377 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 378 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 379 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 380 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 381 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 382 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 383 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 384 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 385 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 386 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 387 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 388 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 389 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 390 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 391 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 392 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 393 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 394 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 395 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 396 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 397 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 398 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 399 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 400 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 401 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 402 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 403 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 404 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 405 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 406 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 407 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 408 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 409 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 410 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 411 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 412 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 413 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 414 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 415 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 416 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 417 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 418 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 419 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 420 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 421 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 422 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 423 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 424 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 425 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 426 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 427 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 428 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 429 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 430 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 431 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 432 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 433 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 434 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 435 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 436 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 437 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 438 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 439 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 440 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 441 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 442 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 443 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 444 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 445 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 446 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 447 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 448 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 449 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 450 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 451 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 452 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 453 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 454 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 455 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 456 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 457 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 458 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 459 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 460 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 461 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 462 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 463 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 464 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 465 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 466 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 467 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 468 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 469 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 470 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 471 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 472 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 473 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 474 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 475 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 476 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 477 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 478 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 479 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 480 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 481 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 482 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 483 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 484 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 485 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 486 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 487 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 488 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 489 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 490 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 491 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 492 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 493 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 494 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 495 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 496 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 497 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 498 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 499 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 500 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 501 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 502 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 503 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 504 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 505 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 506 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
