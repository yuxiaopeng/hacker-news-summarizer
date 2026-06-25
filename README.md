# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-06-25.md)

*最后自动更新时间: 2026-06-25 19:29:59*
## 1. 赫库兰尼姆卷轴首次被成功解读

**原文标题**: A Herculaneum scroll has been read for the first time

**原文链接**: [https://scrollprize.org/firstscroll](https://scrollprize.org/firstscroll)

研究人员首次成功对一整卷碳化的赫库兰尼姆卷轴进行了虚拟展开与阅读，达成了历史性的里程碑。PHerc. 1667（卷轴4）自公元79年维苏威火山爆发以来一直处于密封状态，如今通过欧洲同步辐射装置（ESRF）的高分辨率X射线显微断层扫描技术，结合用于识别古代墨水的机器学习模型，实现了数字化重建。

修复后的文本长约1.4米，包含22栏希腊文字，是一部公元前2世纪的斯多葛学派伦理学著作。该作品探讨了人性与道德进步，并特别提到了哲学家克律西波斯的弟子阿里斯托克雷翁。

该项目还宣布了两项额外突破：
* **PHerc. Paris 4：** 新的3D墨水分割技术为先前的解读提供了独立验证。
* **PHerc. 139：** 研究人员成功阅读了卷轴的标题和作者——菲洛德穆的《论神》第8卷，证明了无需阅读正文即可识别卷轴内容。

这一成功是“维苏威挑战赛”（Vesuvius Challenge）的成果。该挑战赛是由Brent Seales教授、Nat Friedman和Daniel Gross共同发起的开放科学计划。其方法论依托于从项目公开竞赛中脱颖而出的全球研究人员和开发人员社区。为了推动进一步的发现，所有数据、代码和转录文本均已根据知识共享（Creative Commons）许可协议发布。这一成就证明，数百卷仍处于密封状态的卷轴是可以被修复的，为重现整座失落的古代哲学与文学图书馆提供了可能。

---

## 2. IBM发布1纳米以下芯片技术

**原文标题**: IBM debuts sub-1 nanometer chip technology

**原文链接**: [https://newsroom.ibm.com/2026-06-25-ibm-debuts-worlds-first-sub-1-nanometer-chip-technology](https://newsroom.ibm.com/2026-06-25-ibm-debuts-worlds-first-sub-1-nanometer-chip-technology)

2026年6月25日，IBM宣布了半导体技术的重大突破：推出全球首款亚1纳米（nm）芯片，具体为0.7纳米（7埃米）制程。这一里程碑由名为“nanostack”的新型3D晶体管架构驱动，标志着行业从纳米时代向原子级缩放的跨越。

nanostack架构基于IBM之前的纳米片（nanosheet）技术，通过垂直堆叠和交错排列晶体管实现。该设计使IBM能够在指甲盖大小的芯片上集成近1000亿个晶体管，其密度是2纳米技术的两倍。与2纳米制程相比，这款新芯片预计性能可提升50%，或能效提高70%。此外，它在SRAM缩放方面实现了40%的提升，这对于满足先进人工智能和云基础设施的高带宽需求至关重要。

该创新由位于纽约奥尔巴尼的IBM研究设施与ASML、泛林集团（Lam Research）以及东京电子（Tokyo Electron）等合作伙伴共同开发。该工艺利用高数值孔径（High NA）极紫外（EUV）光刻技术，实现了超高精度的电路印刷。

IBM预计该技术将使半导体缩放路线图至少再延长十年。公司预计nanostack架构将在未来五年内投入生产。此外，IBM还强调了其通过“Anderon”对未来计算的承诺——这是一家新成立的独立公司，也是全球首家纯代工模式的量子晶圆厂。

---

## 3. Oxide 计算机 3D 机架导览

**原文标题**: Oxide computer 3D rack guided tour

**原文链接**: [https://explorer.oxide.computer/](https://explorer.oxide.computer/)

Oxide Computer 的 “Explorer” 是一项交互式 3D 导览，展示了该公司垂直集成的机架级计算机。该系统旨在将超大规模云的效率引入本地数据中心，它将整个机架视为一个单一、统一的机器，而非零散服务器的集合。

**关键信息与设计特性：**

*   **集成机架架构：** 机架采用统一背板，消除了传统的乱糟糟布线。它使用盲插连接器，使计算节点能够直接滑入电源和数据织网，便于安装和维护。
*   **计算节点：** 这些高密度节点搭载 AMD EPYC 处理器，并配备大容量本地 NVMe 存储和内存。它们专为高性能工作负载设计，且完全无风扇，依靠机架的集中冷却系统散热。
*   **网络与电源：** 系统将基于 Tofino 的高速交换直接集成到机架架构中，无需外部机架顶置（ToR）交换机。电力通过高效直流母线分配，减少了能量转换损耗。
*   **垂直软件栈：** 核心优势在于协同设计的软件。Oxide 使用自研的开源固件（**Hubris**）、专用操作系统（**Helios**，基于 illumos）以及全面的控制平面（**Omicron**）。这实现了 API 驱动的硬件管理，提供了类似于公有云提供商的使用体验。

**主要结论：**
Oxide 机架旨在解决传统企业硬件的复杂性和可靠性问题。通过掌握从机械节点设计到底层固件再到管理软件的整个技术栈，Oxide 提供了一种“盒中云（cloud-in-a-box）”，在具备本地基础设施的控制力与安全性的同时，提供了公有云的自动化和可扩展性。

---

## 4. Zig 的新 bitCast 语义与 LLVM 后端改进

**原文标题**: Zig's new bitCast semantics and LLVM back end improvements

**原文链接**: [https://ziglang.org/devlog/2026/#2026-06-25](https://ziglang.org/devlog/2026/#2026-06-25)

2026 年中期的 Zig 开发日志重点介绍了在迈向 0.17.0 版本过程中，编译器性能、链接器能力以及构建系统架构方面取得的重大进展。

**新 @bitCast 语义与 LLVM 改进**
Matthew Lugg 针对 LLVM 后端实现了筹备已久的改进，涉及任意位宽整数（如 `u4`、`u40`）。这些类型在存储到内存时，现在会根据 ABI 大小进行零扩展或符号扩展，从而与 Clang 的行为保持一致并减少误编译。这一变化促使开发者对 `@bitCast` 进行了重新定义。`@bitCast` 此前是一种内存重新解释（因此依赖于字节序），现在则基于类型的“逻辑位布局”运行。这使得该内置函数与字节序无关，并在所有后端保持一致。这些优化为 Zig 编译器自身带来了 5% 的性能提升。

**ELF 链接器进展**
最初在 0.16.0 版本中引入的新 ELF 链接器，现在已经可以链接包含外部库（包括 libc 和 LLVM）的复杂项目。其核心优势在于高速增量编译；在 x86_64 Linux 上，某些项目的重新构建时间缩短至仅 30 毫秒。虽然目前尚不支持 Zig 代码的 DWARF 调试信息，但它显著加速了侧重于打印调试和快速迭代的开发周期。

**构建系统重构**
Andrew Kelley 宣布了构建系统的根本性架构转变，将“配置器 (configurer)”与“执行器 (maker)”分离。此前，整个构建系统会随 `build.zig` 一起重新编译。现在，`build.zig` 被编译成一个产生序列化二进制配置的小型“配置器”，而预编译且优化过的“执行器”负责执行实际的构建图。这一改变大幅降低了开销；`zig build -h` 的基准测试显示，总耗时（wall time）减少了 90%，CPU 周期减少了 95%。

---

## 5. OS9地图

**原文标题**: OS9Map

**原文链接**: [https://yllan.org/software/OS9Map/](https://yllan.org/software/OS9Map/)

**OS9Map** 是由 yllan 开发的一款软件应用，旨在为老旧的 Mac OS 9 操作系统引入 OpenStreetMap 功能。该工具于 2026 年 6 月 21 日发布，允许用户在复古硬件上浏览全球地图、搜索地标并管理地理位置。

**主要功能：**
*   **交互式地图画布：** 支持平滑滚动和平移，地图瓦片随用户移动动态加载。
*   **搜索功能：** 内置 Nominatim 查询功能，允许用户快速跳转至特定地址或地标。
*   **书签：** 用户可以将常用地点保存至专用菜单，以便快速访问。

**系统

该软件目前版本为 1.0.0，开发者提供了直接下载选项，并支持通过“Buy Me a Coffee”进行捐赠。

---

## 6. Show HN：受国际象棋启发的 Roguelike 游戏

**原文标题**: Show HN: Chess-Inspired Roguelike

**原文链接**: [https://princechazz.com](https://princechazz.com)

**CHAZZ** 是一款基于浏览器的回合制 Roguelike 游戏，它将国际象棋的战术深度与经典的地牢探险机制完美结合。这款由 Prince Chazz 开发的游戏，挑战玩家利用直接源自传统国际象棋棋子的移动和攻击模式，在一系列网格化的关卡中穿行。

核心玩法围绕着一名主角展开，其能力涵盖了兵（Pawn）、马（Knight）、象（Bishop）、车（Rook）和后（Queen）的特点。玩家必须运用策略，穿梭于布满同样遵循国际象棋规则的敌方单位的房间。胜利取决于谨慎的走位，在躲避敌人致命攻击线的同时“吃掉”对手。

秉承 Roguelike 类型的传统，游戏具有随机生成和永久死亡机制。随着玩家向更深层的关卡推进，遇到的敌人配置会愈发棘手。为了生存，玩家可以收集各种道具和强化物品来获得必要的增益，例如增加生命值、防御护甲或增强移动能力。这些元素使得每一局游戏都能产生多样的角色构建和不同的战略手段。

凭借极简的像素画风和直观的界面，*CHAZZ* 提供了独特的“易于上手，难于精通”的体验。它要求玩家提前预判数步走位，有效地将地牢探险转化为一场关乎空间布局与战术牺牲的高风险、快节奏谜题。

---

## 7. Apple raises prices of MacBooks, iPads

**原文标题**: Apple raises prices of MacBooks, iPads

**原文链接**: [https://www.reuters.com/world/asia-pacific/apple-raises-prices-macbooks-ipads-memory-costs-skyrocket-2026-06-25/](https://www.reuters.com/world/asia-pacific/apple-raises-prices-macbooks-ipads-memory-costs-skyrocket-2026-06-25/)

Unable to access the article link.

---

## 8. 品味无法通过单元测试。

**原文标题**: You can't unit test for taste

**原文链接**: [https://dev.karltryggvason.com/you-cant-unit-test-for-taste/](https://dev.karltryggvason.com/you-cant-unit-test-for-taste/)

In the blog post "You can't unit test for taste," the creator of the virtual running app **In the Long Run** details the development of a data pipeline designed to enrich global running routes with Points of Interest (POIs). 

Using **GeoNames** as a primary data source, the author collaborated with the AI agent **Claude** to build a processing stack featuring **Python, Apache Parquet, and DuckDB**. The pipeline filters millions of locations down to notable landmarks by using Wikipedia links and Wikidata language counts as signals for notoriety. 

A central theme of the article is the evolving role of AI in development. While the author initially intended for the LLM (Anthropic’s Haiku) to generate descriptive summaries and "solve" the feature, **hallucinations**—such as the AI misidentifying minor local parks as world-famous landmarks—forced a pivot. The LLM was ultimately relegated to a supporting role, providing subjective "significance scores" to help rank locations, while factual descriptions were pulled directly from Wikipedia.

The author also highlights the difficulty of automating "taste." Early iterations suffered from **geographical and linguistic biases**, often cluttering maps with every minor hamlet in English-speaking regions while overlooking significant sites elsewhere. To fix this, the author implemented per-route tuning and geographic radius filters to ensure a balanced mix of nature, history, and culture.

Ultimately, the author concludes that while AI is a powerful "senior mentor" for technical implementation, it cannot replace human judgment. Because there is no objective "ground truth" for what makes a landmark interesting, developers cannot rely on unit tests; instead, they must embrace manual iteration and subjective refinement to achieve a high-quality user experience.

---

## 9. Show HN: I made Google Trends for Hacker News by indexing 18 years of comments

**原文标题**: Show HN: I made Google Trends for Hacker News by indexing 18 years of comments

**原文链接**: [https://hackernewstrends.com](https://hackernewstrends.com)

生成摘要时出错

---

## 10. Besimple AI (YC P25) 正在招聘

**原文标题**: Besimple AI (YC P25) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/besimple-ai/jobs/yWfhhOR-strategic-projects-lead-audio-data](https://www.ycombinator.com/companies/besimple-ai/jobs/yWfhhOR-strategic-projects-lead-audio-data)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 2 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 3 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 4 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 5 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 6 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 7 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 8 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 9 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 10 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 11 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 12 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 13 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 14 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 15 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 16 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 17 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 18 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 19 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 20 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 21 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 22 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 23 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 24 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 25 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 26 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 27 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 28 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 29 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 30 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 31 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 32 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 33 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 34 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 35 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 36 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 37 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 38 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 39 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 40 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 41 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 42 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 43 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 44 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 45 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 46 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 47 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 48 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 49 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 50 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 51 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 52 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 53 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 54 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 55 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 56 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 57 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 58 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 59 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 60 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 61 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 62 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 63 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 64 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 65 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 66 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 67 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 68 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 69 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 70 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 71 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 72 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 73 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 74 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 75 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 76 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 77 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 78 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 79 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 80 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 81 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 82 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 83 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 84 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 85 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 86 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 87 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 88 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 89 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 90 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 91 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 92 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 93 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 94 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 95 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 96 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 97 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 98 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 99 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 100 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 101 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 102 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 103 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 104 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 105 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 106 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 107 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 108 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 109 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 110 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 111 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 112 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 113 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 114 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 115 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 116 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 117 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 118 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 119 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 120 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 121 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 122 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 123 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 124 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 125 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 126 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 127 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 128 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 129 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 130 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 131 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 132 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 133 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 134 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 135 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 136 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 137 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 138 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 139 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 140 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 141 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 142 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 143 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 144 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 145 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 146 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 147 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 148 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 149 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 150 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 151 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 152 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 153 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 154 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 155 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 156 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 157 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 158 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 159 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 160 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 161 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 162 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 163 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 164 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 165 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 166 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 167 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 168 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 169 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 170 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 171 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 172 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 173 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 174 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 175 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 176 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 177 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 178 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 179 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 180 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 181 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 182 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 183 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 184 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 185 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 186 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 187 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 188 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 189 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 190 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 191 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 192 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 193 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 194 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 195 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 196 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 197 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 198 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 199 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 200 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 201 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 202 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 203 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 204 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 205 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 206 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 207 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 208 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 209 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 210 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 211 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 212 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 213 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 214 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 215 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 216 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 217 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 218 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 219 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 220 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 221 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 222 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 223 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 224 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 225 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 226 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 227 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 228 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 229 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 230 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 231 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 232 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 233 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 234 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 235 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 236 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 237 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 238 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 239 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 240 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 241 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 242 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 243 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 244 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 245 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 246 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 247 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 248 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 249 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 250 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 251 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 252 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 253 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 254 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 255 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 256 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 257 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 258 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 259 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 260 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 261 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 262 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 263 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 264 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 265 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 266 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 267 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 268 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 269 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 270 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 271 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 272 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 273 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 274 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 275 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 276 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 277 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 278 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 279 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 280 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 281 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 282 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 283 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 284 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 285 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 286 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 287 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 288 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 289 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 290 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 291 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 292 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 293 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 294 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 295 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 296 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 297 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 298 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 299 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 300 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 301 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 302 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 303 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 304 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 305 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 306 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 307 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 308 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 309 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 310 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 311 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 312 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 313 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 314 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 315 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 316 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 317 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 318 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 319 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 320 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 321 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 322 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 323 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 324 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 325 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 326 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 327 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 328 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 329 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 330 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 331 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 332 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 333 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 334 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 335 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 336 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 337 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 338 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 339 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 340 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 341 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 342 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 343 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 344 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 345 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 346 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 347 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 348 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 349 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 350 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 351 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 352 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 353 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 354 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 355 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 356 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 357 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 358 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 359 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 360 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 361 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 362 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 363 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 364 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 365 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 366 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 367 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 368 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 369 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 370 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 371 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 372 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 373 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 374 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 375 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 376 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 377 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 378 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 379 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 380 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 381 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 382 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 383 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 384 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 385 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 386 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 387 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 388 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 389 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 390 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 391 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 392 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 393 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 394 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 395 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 396 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 397 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 398 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 399 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 400 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 401 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 402 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 403 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 404 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 405 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 406 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 407 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 408 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 409 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 410 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 411 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 412 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 413 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 414 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 415 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 416 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 417 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 418 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 419 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 420 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 421 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 422 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 423 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 424 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 425 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 426 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 427 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 428 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 429 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 430 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 431 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 432 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 433 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 434 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 435 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 436 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 437 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 438 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 439 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 440 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 441 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 442 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 443 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 444 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 445 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 446 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 447 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 448 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 449 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 450 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 451 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 452 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 453 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 454 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 455 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 456 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 457 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 458 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 459 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 460 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 461 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 462 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
