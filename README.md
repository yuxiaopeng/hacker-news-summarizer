# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-07-03.md)

*最后自动更新时间: 2026-07-03 18:43:17*
## 1. Claude，请别再试图记那些乱七八糟的东西了。

**原文标题**: Claude, please stop trying to memorize random crap

**原文链接**: [https://12gramsofcarbon.com/p/agentics-memorizing-session-transcripts](https://12gramsofcarbon.com/p/agentics-memorizing-session-transcripts)

在《Claude，请停止记忆那些没用的废话》一文中，作者挑战了“存储并检索历史会话记录（基于会话的记忆）能提升 AI 编程智能体性能”的流行观点。尽管作者团队曾围绕“会话记录是新石油”这一理念构建产品，但他们发现这不仅没有带来性能提升，甚至还导致了模型退化。

文章强调了自动化会话记忆失败的几个原因：

1. **冗余与噪声**：有关意图和决策的有价值背景已提炼到 PR 消息、提交记录和文档等“编程产物”中。搜索原始记录会迫使智能体将 Token 浪费在“草稿纸”噪声和已被弃用的方案上，而这些方案的有效信息早已以更精炼的形式存在。
2. **缺乏“记忆修剪”**：智能体难以修剪或删除无关背景。由于模型被训练为将所有输入视为“事实”，它们无法区分经过人工审核的决策与历史会话中随机、未经审核的选择。这导致了“意图漂移”，使错误随时间累积。
3. **对齐约束**：当前模型如果假设输入数据是“错误”的，往往会受到惩罚。这使得智能体很难忽略“损坏”的记忆，或识别某次历史会话何时偏离了正确方向。

作者得出结论，智能体尚无法自主管理记忆。内部数据显示，当机器人根据公司活动建议更新记忆时，**80% 的建议在人工审核中被拒绝**。为了提高智能体的表现，作者建议应专注于高质量文档和“人工在环”验证，而非原始会话记录的索引。

---

## 2. Maxis 的前世今生 第一部：模拟万物

**原文标题**: The Life and Times of Maxis, Part 1: SimEverything

**原文链接**: [https://www.filfre.net/2026/07/the-life-and-times-of-maxis-part-1-simeverything/](https://www.filfre.net/2026/07/the-life-and-times-of-maxis-part-1-simeverything/)

本文探讨了 Maxis 软件公司的早期历史，以及其联合创始人威尔·赖特（Will Wright）对游戏行业的革命性影响。文章首先指出，“硬核”游戏历史与实际商业现实之间存在脱节，并注意到最成功的游戏——如《神秘岛》或《模拟城市》——通常吸引的是那些并不自诩为游戏玩家的主流受众。

1989 年推出的《模拟城市》摒弃了传统的“胜负”状态，转而采用“软件玩具”理念，从而成为一种文化现象。尽管赖特承认该游戏只是城市规划的“漫画式呈现”而非写实模拟，但其成就斐然。它确立了城市建设类游戏的地位，并引入了实时机制和“沙盒”模式，影响了包括席德·梅尔的《文明》在内的后世经典。

随后，文章详细阐述了赖特更宏大的“模拟一切”愿景——即各种模拟系统最终能互联成一个统一的游戏宇宙。在这一雄心的驱使下，1990 年《模拟地球》问世，将视角从城市规划转向了行星生态学。受当时关于全球变暖的公众讨论及詹姆斯·洛夫洛克“盖亚假说”的启发，《模拟地球》试图将地球建模为一个单一、互锁的有机体。赖特的作品受到了洛夫洛克本人“黛西世界”计算机模型的启发，该模型展示了生命与环境是如何相互作用的。

最终，本文将 Maxis 描绘为不仅是一家游戏开发商，更是一个先驱，它推动游戏媒介从小众幻想转向主流的、基于现实的模拟，永久地改变了现代游戏设计的基因。

---

## 3. 半成品

**原文标题**: Half-Baked Product

**原文链接**: [https://weli.dev/blog/half-baked-product/](https://weli.dev/blog/half-baked-product/)

在《半成品》（Half-Baked Product）一文中，作者探讨了产品开发中常见的陷阱，特别是区分了真正的“最小可行性产品”（MVP）与所谓的“半成品”之间的本质区别。

核心观点是：“最小”应当指代产品的范围，而非其质量。作者强调了以下几个关键点：

*   **对 MVP 的误解：** 许多团队将 MVP 标签当作发布漏洞百出、缺乏打磨或不完整软件的借口。这种“半成品”缺乏提供价值所需的核心功能或用户体验，会导致用户倍感挫败。
*   **纸杯蛋糕类比：** 作者倡导“纸杯蛋糕”式开发。与其做一个大而无味、并承诺以后再补上糖衣的大蛋糕，团队应该创造一个“纸杯蛋糕”——一个小而完整、高品质且“美味”的产品。把一件事做到完美，胜过把十件事做得平庸。
*   **声誉风险：** 发布平庸的产品会损害品牌信任。第一印象很难改变，挽回一个已有负面体验的用户，要比用一款精致的工具吸引新用户困难得多。
*   **最小受人喜爱的产品（MLP）：** 作者建议将关注点转向构建“最小受人喜爱的产品”。这意味着要确保核心功能不仅可用，而且能让用户感到愉悦。

归根结底，本文是对那种因追求“快速行动、打破陈规”而导致技术债和工艺粗糙的心态的批判。它鼓励开发人员和产品经理在扩展功能之前，优先在基础核心上追求卓越。

---

## 4. Jamesob 的本地运行 SOTA 大语言模型指南

**原文标题**: Jamesob's guide to running SOTA LLMs locally

**原文链接**: [https://github.com/jamesob/local-llm](https://github.com/jamesob/local-llm)

Jamesob’s guide provides a blueprint for running State-of-the-Art (SOTA) LLMs locally, offering solutions for two budget levels: a **$2,000 entry-level setup** and a **$46,000 high-end workstation**.

**The High-End Build ($46k)**
The flagship system centers on **4x NVIDIA RTX PRO 6000 Blackwell GPUs**, providing 384GB of VRAM. To keep costs manageable, the author uses a last-gen **AMD EPYC Milan** base system with DDR4 RAM. A standout feature is the use of **c-payne PCIe Gen4 switches**, which allow GPUs to communicate peer-to-peer (P2P) at wire speeds during tensor parallelism, bypassing the CPU root complex to reduce latency.

**Technical Optimization**
The guide emphasizes several critical hardware and software tweaks:
*   **BIOS/Kernel:** Disable ASPM to prevent link downgrades and IOMMU to prevent NCCL hangs. Enable Re-Size BAR for VRAM exposure.
*   **P2P Traffic:** Use `setpci` to disable ACS (Access Control Services), ensuring data stays within the switch fabric rather than bouncing through the CPU.
*   **Power Management:** To run the system on a standard 110V circuit, GPUs are power-limited to 350W each via systemd scripts.

**Software and Workflow**
Models (such as the 594B GLM-5.2) are served via **vLLM in Docker containers**, with weights stored on a ZFS filesystem. The author uses a sandboxed VM "clanker" for interaction, utilizing local tools like Gitea for code collaboration and SearXNG for web search to maintain privacy.

**The Budget Option ($2k)**
For those with less to spend, the author recommends **2x RTX 3090s** (48GB VRAM). This setup is capable of running **Qwen-27B** and high-quality local speech-to-text via **Whisper-large-v3**, providing a powerful entry point into local machine intelligence.

---

## 5. International chess federation sanctions Kramnik

**原文标题**: International chess federation sanctions Kramnik

**原文链接**: [https://www.fide.com/fide-ethics-disciplinary-commission-issues-a-decision-in-case-involving-gm-vladimir-kramnik/](https://www.fide.com/fide-ethics-disciplinary-commission-issues-a-decision-in-case-involving-gm-vladimir-kramnik/)

生成摘要时出错

---

## 6. Factories Are Just Rooms

**原文标题**: Factories Are Just Rooms

**原文链接**: [https://interconnected.org/home/2026/07/03/factories](https://interconnected.org/home/2026/07/03/factories)

生成摘要时出错

---

## 7. Hunting a 16-year-old SQLite WAL bug with TLA+

**原文标题**: Hunting a 16-year-old SQLite WAL bug with TLA+

**原文链接**: [https://ubuntu.com/blog/hunting-a-16-year-old-sqlite-bug-with-tla-is-dqlite-affected](https://ubuntu.com/blog/hunting-a-16-year-old-sqlite-bug-with-tla-is-dqlite-affected)

生成摘要时出错

---

## 8. AI saves about 3% of your hours, and almost none of it reaches the money

**原文标题**: AI saves about 3% of your hours, and almost none of it reaches the money

**原文链接**: [https://okaneland.com/study/ai-productivity-roi-at-work/](https://okaneland.com/study/ai-productivity-roi-at-work/)

生成摘要时出错

---

## 9. PostgreSQL and the OOM Killer: Why We Use Strict Memory Overcommit

**原文标题**: PostgreSQL and the OOM Killer: Why We Use Strict Memory Overcommit

**原文链接**: [https://www.ubicloud.com/blog/postgresql-and-the-oom-killer-why-we-use-strict-memory-overcommit](https://www.ubicloud.com/blog/postgresql-and-the-oom-killer-why-we-use-strict-memory-overcommit)

生成摘要时出错

---

## 10. My Dad Helped Build North America's Oat Supply Chain: Can It Be Remade?

**原文标题**: My Dad Helped Build North America's Oat Supply Chain: Can It Be Remade?

**原文链接**: [https://ambrook.com/offrange/perspective/how-we-lost-our-oats](https://ambrook.com/offrange/perspective/how-we-lost-our-oats)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 2 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 3 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 4 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 5 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 6 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 7 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 8 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 9 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 10 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 11 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 12 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 13 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 14 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 15 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 16 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 17 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 18 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 19 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 20 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 21 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 22 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 23 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 24 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 25 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 26 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 27 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 28 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 29 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 30 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 31 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 32 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 33 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 34 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 35 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 36 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 37 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 38 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 39 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 40 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 41 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 42 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 43 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 44 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 45 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 46 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 47 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 48 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 49 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 50 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 51 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 52 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 53 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 54 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 55 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 56 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 57 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 58 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 59 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 60 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 61 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 62 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 63 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 64 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 65 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 66 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 67 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 68 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 69 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 70 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 71 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 72 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 73 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 74 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 75 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 76 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 77 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 78 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 79 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 80 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 81 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 82 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 83 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 84 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 85 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 86 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 87 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 88 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 89 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 90 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 91 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 92 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 93 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 94 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 95 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 96 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 97 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 98 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 99 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 100 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 101 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 102 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 103 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 104 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 105 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 106 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 107 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 108 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 109 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 110 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 111 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 112 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 113 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 114 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 115 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 116 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 117 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 118 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 119 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 120 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 121 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 122 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 123 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 124 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 125 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 126 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 127 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 128 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 129 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 130 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 131 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 132 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 133 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 134 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 135 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 136 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 137 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 138 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 139 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 140 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 141 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 142 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 143 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 144 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 145 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 146 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 147 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 148 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 149 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 150 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 151 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 152 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 153 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 154 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 155 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 156 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 157 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 158 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 159 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 160 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 161 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 162 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 163 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 164 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 165 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 166 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 167 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 168 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 169 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 170 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 171 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 172 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 173 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 174 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 175 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 176 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 177 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 178 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 179 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 180 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 181 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 182 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 183 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 184 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 185 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 186 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 187 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 188 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 189 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 190 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 191 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 192 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 193 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 194 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 195 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 196 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 197 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 198 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 199 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 200 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 201 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 202 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 203 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 204 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 205 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 206 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 207 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 208 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 209 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 210 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 211 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 212 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 213 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 214 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 215 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 216 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 217 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 218 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 219 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 220 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 221 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 222 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 223 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 224 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 225 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 226 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 227 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 228 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 229 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 230 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 231 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 232 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 233 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 234 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 235 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 236 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 237 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 238 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 239 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 240 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 241 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 242 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 243 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 244 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 245 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 246 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 247 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 248 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 249 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 250 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 251 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 252 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 253 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 254 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 255 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 256 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 257 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 258 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 259 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 260 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 261 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 262 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 263 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 264 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 265 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 266 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 267 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 268 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 269 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 270 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 271 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 272 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 273 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 274 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 275 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 276 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 277 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 278 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 279 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 280 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 281 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 282 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 283 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 284 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 285 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 286 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 287 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 288 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 289 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 290 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 291 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 292 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 293 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 294 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 295 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 296 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 297 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 298 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 299 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 300 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 301 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 302 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 303 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 304 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 305 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 306 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 307 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 308 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 309 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 310 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 311 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 312 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 313 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 314 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 315 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 316 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 317 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 318 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 319 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 320 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 321 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 322 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 323 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 324 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 325 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 326 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 327 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 328 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 329 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 330 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 331 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 332 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 333 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 334 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 335 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 336 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 337 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 338 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 339 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 340 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 341 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 342 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 343 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 344 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 345 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 346 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 347 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 348 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 349 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 350 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 351 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 352 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 353 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 354 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 355 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 356 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 357 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 358 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 359 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 360 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 361 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 362 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 363 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 364 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 365 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 366 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 367 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 368 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 369 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 370 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 371 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 372 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 373 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 374 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 375 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 376 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 377 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 378 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 379 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 380 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 381 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 382 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 383 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 384 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 385 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 386 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 387 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 388 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 389 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 390 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 391 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 392 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 393 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 394 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 395 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 396 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 397 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 398 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 399 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 400 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 401 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 402 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 403 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 404 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 405 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 406 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 407 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 408 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 409 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 410 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 411 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 412 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 413 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 414 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 415 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 416 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 417 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 418 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 419 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 420 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 421 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 422 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 423 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 424 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 425 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 426 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 427 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 428 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 429 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 430 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 431 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 432 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 433 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 434 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 435 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 436 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 437 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 438 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 439 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 440 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 441 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 442 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 443 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 444 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 445 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 446 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 447 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 448 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 449 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 450 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 451 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 452 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 453 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 454 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 455 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 456 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 457 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 458 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 459 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 460 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 461 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 462 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 463 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 464 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 465 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 466 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 467 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 468 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 469 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 470 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
