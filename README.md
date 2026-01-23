# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-01-23.md)

*最后自动更新时间: 2026-01-23 17:55:33*
## 1. Gas Town 的智能体模式、设计瓶颈与大规模氛围感编码

**原文标题**: Gas Town's Agent Patterns, Design Bottlenecks, and Vibecoding at Scale

**原文链接**: [https://maggieappleton.com/gastown](https://maggieappleton.com/gastown)

Steve Yegge 的“Gas Town”是一个雄心勃勃的、“氛围感驱动”（vibecoded）的智能体编排器，能够同时运行数十个编程智能体。尽管作者将其批评为一个混乱、低效且昂贵的“烂摊子”，但他们认为这是一件至关重要的“设计虚构”（design fiction）作品，揭示了未来智能体软件开发所面临的约束。

文章强调了编程本质的两个主要转变：

1. **设计成为新瓶颈：** 当智能体几乎可以瞬间实现代码时，瓶颈便从开发转移到了高层设计和规划。如果没有人类的品味、远见和架构意图，智能体的高速产出将导致“氛围感设计”出的系统——即建立在糟糕抽象之上的、庞大且令人费解的“工业垃圾”。
2. **新兴的编排模式：** 尽管过程混乱，但 Gas Town 通过专业化、层级化的角色为未来的智能体系统勾勒了蓝图：
    * **市长 (The Mayor)：** 充当人类管家，负责协调工作而不直接编写代码。
    * **臭鼬 (Polecats)：** 负责孤立任务的临时底层苦力。
    * **见证者与精炼厂 (The Witness & Refinery)：** 负责排除故障并管理复杂合并队列的监管智能体。

为了解决“上下文腐烂”问题，Gas Town 引入了 “Beads”——以 JSON 格式存储在 Git 中的可追踪工作单元。这使得智能体的身份和任务即使在单个 LLM 会话终止并重启后仍能保持持久性，从而实现“永续”编排。

最终，Gas Town 表明工程开发的未来不仅在于更好的代码自动补全，更在于管理一个专业智能体的“动物园”。虽然 Gas Town 本身“用起来是一场噩梦”，但其层级化监管和持久化任务追踪的模式，很可能成为未来更成熟、专业的工具标准。

---

## 2. Radicle：主权锻造场

**原文标题**: Radicle: The Sovereign Forge

**原文链接**: [https://radicle.xyz](https://radicle.xyz)

Radicle 是一个去中心化的点对点 (P2P) 代码协作平台，旨在作为中心化托管服务的“主权”替代方案。它直接构建在 Git 之上，通过在独立节点网络中复制仓库，消除了对第三方中间机构的依赖，确保用户对其数据和工作流拥有完整的所有权。

该平台具有以下核心特征：
* **主权与自治：** 通过运行自己的节点，用户可以创建一个抗审查的环境。没有任何单一实体能够控制网络或其数据。
* **本地优先架构：** Radicle 提供全功能的离线能力。由于所有社交制品（Social Artifacts）都以 Git 对象的形式存储，数据所有权使迁移和备份变得简单。
* **加密安全性：** 该协议利用公钥加密技术对所有交互进行签名，允许系统验证代码和社交元数据的真实性与作者身份。
* **可扩展性：** 通过“协作对象”(COBs)，议题（Issues）、讨论和代码审查等社交功能被实现为 Git 对象。这种模块化设计允许开发者扩展平台，并更换命令行界面 (CLI)、Web 界面或终端用户界面 (TUI) 等组件。

Radicle 技术栈包括 Radicle 节点和 HTTP 守护进程。它目前兼容 Linux、macOS 和 BSD。自 2024 年底发布 1.0 版本以来，该项目保持着稳定的发布周期，并在 2026 年初达到 1.6.0 版本。Radicle 是采用 MIT 和 Apache 2.0 协议的免费开源软件，旨在培育一个具有韧性的社区驱动生态系统，以实现安全的代码协作。

---

## 3. 从黑胶唱片启动 (2020)

**原文标题**: Booting from a vinyl record (2020)

**原文链接**: [https://boginjr.com/it/sw/dev/vinyl-boot/](https://boginjr.com/it/sw/dev/vinyl-boot/)

在这个技术项目中，Jozef Bogin 展示了一项创意十足的复古计算壮举：使用黑胶唱片作为存储介质来启动一台 IBM PC（具体为原始的 Model 5150 型号）。

该项目利用了 IBM 5150 一个被很大程度上遗忘的功能——内置磁带接口。在软盘成为标准之前，早期个人电脑的设计初衷是使用标准音频磁带录音机来保存和加载数据。Bogin 意识到，既然 PC 将这些数据流视为简单的音频信号，那么理论上任何能够再现声音的模拟介质都可以承载数字数据。

为了实现这一目标，Bogin 使用频移键控（FSK）技术将一个小程序编码为音频音调，其中不同的频率代表二进制的 0 和 1。随后，这些“数据”被压制到黑胶唱片上。硬件连接方面，他使用一根自定义电缆将标准黑胶唱机连接到 PC 的磁带端口（5 针 DIN 接口），以确保信号电平匹配。

当 IBM PC 在没有软盘的情况下启动时，它会默认进入存储在 ROM 中的“磁带 BASIC”（Cassette BASIC）。通过输入 `LOAD` 命令并将唱针放在唱片上，PC 会将来自黑胶唱片的音频频率解析为数字代码，并将其直接加载到内存中。

尽管面临信噪比和黑胶唱片物理缺陷（可能导致数据损坏）等挑战，Bogin 仍成功加载并运行了一个“Hello World”程序和一个小型图形演示。该项目突显了 20 世纪 80 年代硬件的灵活性，并在模拟音乐文化与数字计算历史之间搭建了一座奇妙的桥梁。

---

## 4. AI是一匹马 (2024)

**原文标题**: AI is a horse (2024)

**原文链接**: [https://kconner.com/2024/08/02/ai-is-a-horse.html](https://kconner.com/2024/08/02/ai-is-a-horse.html)

《人工智能是马》（2024）利用马这一隐喻，定义了人工智能当前的能力与局限。该作品指出，虽然人工智能在速度和效率上超越了人类，但它缺乏像火车等工业系统那样的可靠性和结构性。

核心论点包括：
*   **资源密集型：** 像马一样，人工智能的维护成本高昂，且“消耗”大量资源。
*   **缺乏自主性：** 人工智能无法独立运行；它需要持续的人工引导和具体指令才能到达目的地或保持在正轨。
*   **人工监督：** 即使人工智能看似运行正常，用户也必须保持掌控，以防止其偏离目标。
*   **有限的能动性：** 作者指出，虽然你可以为人工智能提供数据或提示词（将其领到水边），但你无法强迫其产生特定的高质量产出或“思考”过程。
*   **响应性：** 高性能人工智能的特征在于其对细微提示或“鞭影”的敏感度。
*   **警惕拟人化：** 文章最后警告人们要警惕那些过度模仿人类语言或意识的人工智能（“会说话的那些”）。

总体而言，该摘要将人工智能描述为一种功能强大但性情多变的工具，它需要的是熟练的“骑手”，而非完全自主的智能体。

---

## 5. KORG phase8 – Acoustic Synthesizer

**原文标题**: KORG phase8 – Acoustic Synthesizer

**原文链接**: [https://www.korg.com/us/products/dj/phase8/](https://www.korg.com/us/products/dj/phase8/)

KORG推出了phase8，这是一款开创性的八复音“声学合成器”，架起了物理发声与电子控制之间的桥梁。利用KORG专有的声学合成技术，该乐器通过物理振动体而非传统的振荡器产生声音，从而打造出一种有机且灵敏的体验，能够对触摸和声学反馈做出实时响应。

phase8的核心是八个独立的机电声部，配备了可更换且可调律的钢制谐振器。该合成器随附13个按半音阶调律的谐振器，可同时安装其中8个，支持自定义音阶和音色。用户可以通过包络控制、模拟波形折叠和音高相关调制等电子参数来塑造声音。

phase8强调实时的物理交互。除了调节旋钮，音乐家还可以直接拨动、敲击或弹奏谐振器。内置的“AIR”滑块可用于增强或减弱这些物理交互的声学响应。在序列编排方面，该乐器配备了直观的多律动节奏序列器，支持步进编程、非量化实时录音以及跨8个存储槽的参数自动化。

接口配置十分强大，拥有MIDI、USB-MIDI、CV和Sync接口，可与外部设备无缝集成。这使得phase8既能由外部设备触发，也能作为控制器操控其他乐器。

KORG还提供预售专属礼包，其中包括三个限量版打击乐谐振器，专为实验性的触感声音探索而设计。phase8代表了对“模拟 vs 数字”界限的超越，提供了一种乐器仿佛具有“生命力”并能对环境做出独特响应的触觉体验。

---

## 6. Show HN: Zsweep – Play Minesweeper using only Vim motions

**原文标题**: Show HN: Zsweep – Play Minesweeper using only Vim motions

**原文链接**: [https://zsweep.com](https://zsweep.com)

**Zsweep** is a specialized version of the classic game Minesweeper designed for developers and power users who prefer keyboard-centric navigation. Its primary feature is the integration of **Vim motions**, allowing players to navigate the grid and interact with the game without using a mouse.

Key features and controls include:
*   **Grid Sizes:** Supports standard configurations, including 9x9, 16x16, and 30x16.
*   **Vim Integration:** Movement is handled via standard Vim directional keys.
*   **Action Commands:** Players use the **Spacebar** to reveal cells and the **forward slash (/)** to flag mines or perform "chords" (clearing surrounding non-mine squares).
*   **Game Management:** Quick shortcuts are available for restarting (Tab) and accessing settings (Esc).

By replacing traditional mouse clicks with efficient keyboard shortcuts, Zsweep offers a fast-paced, "mouse-free" experience tailored to the workflow of Vim enthusiasts.

---

## 7. Proton Spam and the AI Consent Problem

**原文标题**: Proton Spam and the AI Consent Problem

**原文链接**: [https://dbushell.com/2026/01/22/proton-spam/](https://dbushell.com/2026/01/22/proton-spam/)

生成摘要时出错

---

## 8. Show HN: Whosthere: A LAN discovery tool with a modern TUI, written in Go

**原文标题**: Show HN: Whosthere: A LAN discovery tool with a modern TUI, written in Go

**原文链接**: [https://github.com/ramonvermeulen/whosthere](https://github.com/ramonvermeulen/whosthere)

生成摘要时出错

---

## 9. I built a light that reacts to radio waves [video]

**原文标题**: I built a light that reacts to radio waves [video]

**原文链接**: [https://www.youtube.com/watch?v=moBCOEiqiPs](https://www.youtube.com/watch?v=moBCOEiqiPs)

生成摘要时出错

---

## 10. Three RCEs in Ilias Learning Management System

**原文标题**: Three RCEs in Ilias Learning Management System

**原文链接**: [https://srlabs.de/blog/breaking-ilias-part-2-three-to-rce](https://srlabs.de/blog/breaking-ilias-part-2-three-to-rce)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 2 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 3 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 4 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 5 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 6 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 7 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 8 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 9 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 10 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 11 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 12 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 13 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 14 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 15 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 16 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 17 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 18 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 19 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 20 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 21 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 22 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 23 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 24 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 25 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 26 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 27 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 28 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 29 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 30 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 31 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 32 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 33 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 34 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 35 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 36 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 37 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 38 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 39 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 40 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 41 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 42 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 43 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 44 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 45 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 46 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 47 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 48 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 49 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 50 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 51 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 52 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 53 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 54 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 55 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 56 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 57 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 58 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 59 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 60 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 61 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 62 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 63 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 64 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 65 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 66 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 67 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 68 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 69 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 70 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 71 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 72 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 73 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 74 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 75 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 76 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 77 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 78 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 79 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 80 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 81 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 82 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 83 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 84 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 85 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 86 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 87 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 88 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 89 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 90 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 91 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 92 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 93 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 94 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 95 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 96 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 97 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 98 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 99 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 100 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 101 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 102 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 103 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 104 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 105 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 106 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 107 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 108 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 109 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 110 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 111 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 112 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 113 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 114 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 115 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 116 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 117 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 118 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 119 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 120 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 121 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 122 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 123 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 124 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 125 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 126 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 127 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 128 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 129 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 130 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 131 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 132 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 133 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 134 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 135 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 136 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 137 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 138 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 139 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 140 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 141 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 142 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 143 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 144 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 145 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 146 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 147 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 148 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 149 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 150 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 151 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 152 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 153 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 154 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 155 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 156 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 157 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 158 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 159 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 160 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 161 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 162 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 163 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 164 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 165 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 166 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 167 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 168 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 169 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 170 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 171 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 172 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 173 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 174 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 175 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 176 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 177 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 178 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 179 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 180 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 181 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 182 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 183 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 184 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 185 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 186 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 187 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 188 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 189 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 190 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 191 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 192 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 193 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 194 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 195 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 196 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 197 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 198 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 199 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 200 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 201 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 202 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 203 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 204 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 205 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 206 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 207 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 208 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 209 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 210 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 211 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 212 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 213 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 214 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 215 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 216 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 217 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 218 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 219 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 220 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 221 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 222 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 223 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 224 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 225 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 226 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 227 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 228 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 229 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 230 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 231 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 232 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 233 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 234 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 235 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 236 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 237 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 238 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 239 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 240 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 241 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 242 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 243 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 244 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 245 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 246 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 247 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 248 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 249 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 250 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 251 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 252 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 253 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 254 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 255 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 256 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 257 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 258 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 259 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 260 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 261 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 262 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 263 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 264 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 265 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 266 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 267 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 268 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 269 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 270 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 271 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 272 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 273 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 274 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 275 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 276 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 277 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 278 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 279 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 280 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 281 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 282 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 283 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 284 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 285 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 286 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 287 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 288 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 289 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 290 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 291 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 292 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 293 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 294 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 295 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 296 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 297 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 298 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 299 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 300 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 301 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 302 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 303 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 304 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 305 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 306 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 307 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 308 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 309 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
