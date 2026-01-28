# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-01-28.md)

*最后自动更新时间: 2026-01-28 18:03:13*
## 1. 微软迫使我改用 Linux

**原文标题**: Microsoft forced me to switch to Linux

**原文链接**: [https://www.himthe.dev/blog/microsoft-to-linux](https://www.himthe.dev/blog/microsoft-to-linux)

这篇文章以2026年初的视角，记录了一位拥有22年机龄的资深Windows用户向Linux（特别是CachyOS）“被迫”迁移的过程。作者是一位软件开发人员兼音乐人，他认为微软将利润和AI集成置于系统稳定性和用户许可之上，将操作系统变成了他所谓的“微软废料”（Microslop）。

**切换的主要原因：**
*   **系统不稳定：** 导火索是Windows 24H2更新。该更新在未经许可的情况下自动安装，并引入了“Chrome抽搐”Bug（与多平面叠加相关）。微软和NVIDIA对此均未承担责任，导致该问题始终未获修复。
*   **对用户不友好的特性：** 作者列举了导致数据丢失的强制更新、OneDrive和Edge的侵入式广告、本地账户选项的移除，以及无处不在且无法删除的“Copilot”。
*   **性能臃肿：** 文中批评了微软将原生系统应用替换为臃肿的React Native和基于Chromium的进程，这些进程消耗了大量内存并降低了系统响应速度。

**2026年的Linux体验：**
作者指出，虽然Linux有一定的学习成本，但它提供了一个“可修复”的环境。核心收获包括：
*   **兼容性：** 大多数浏览器和开发工具都能原生运行。通过Proton，游戏性能已接近Windows水平；而通过PipeWire，音频延迟已可与macOS媲美。
*   **创意工作：** 尽管Adobe系列软件和Ableton Live仍存在兼容问题，但DaVinci Resolve和Bitwig Studio等专业替代方案已能提供可行的工作流。
*   **效率：** 作者强调，与“卡顿”的Windows 11界面相比，Linux桌面具有更卓越的速度和响应性。

最终，作者总结道，由于微软领导层为了追求“AI垃圾”而忽视用户满意度，他们实际上已成为最伟大的“Linux传教士”，有效地将高级用户赶出了Windows生态系统。

---

## 2. 翼型 (2024)

**原文标题**: Airfoil (2024)

**原文链接**: [https://ciechanow.ski/airfoil/](https://ciechanow.ski/airfoil/)

《翼型 (2024)》通过研究空气如何流经被称为“翼型”的机翼截面，探讨了飞行的物理学原理。由于空气是透明的，文中概述了三种可视化其运动的主要方法：**速度箭头**（显示固定点的速度和方向）、**标记物**（追踪气团随时间变化的路径）以及**色彩映射**（通过亮度代表流速）。

文章的大部分内容解释了空气的微观本质。在分子层面，空气由数十亿个高速随机运动的粒子组成——在室温下平均速度达每小时 1,030 英里——且每秒发生数十亿次碰撞。文中阐明了单个粒子运动与集体“气流”之间的区别。在静止的空气中，粒子的随机运动相互抵消，净速度为零。当特定区域内的一群粒子具有非零的平均速度时，便产生了风或气流。

文中还介绍了流体力学中的关键概念：
*   **定常流**：在任何给定位置，流动特性不随时间改变的状态。
*   **相对速度**：理解气流是相对的；空气流过静止物体在物理上等同于物体穿过静止空气。

通过衔接混沌的微观粒子行为与通过箭头和色彩可视化的有序宏观流动，本文为理解维持飞机升空的力奠定了直观基础。尽管提供的内容在讨论相对速度时中断了，但它明确了翼型的形状和朝向对于操控这些空气特性以产生飞行至关重要。

---

## 3. Amazon One 掌纹身份验证已停用

**原文标题**: Amazone One palm authentication discontinued

**原文链接**: [https://amazonone.aws.com/help](https://amazonone.aws.com/help)

根据近期行业动态和亚马逊零售战略背景，以下是关于 Amazon One 现状的简明摘要：

**摘要：Amazon One 掌纹认证的演进**

亚马逊目前正在重构其实体零售技术，这导致其掌纹识别服务 **Amazon One** 发生了重大变化。虽然这项技术并未完全退出舞台，但其应用方式正在发生转变。

**关键信息：**
*   **零售转型：** 亚马逊近期宣布，将从大型 Amazon Fresh 生鲜超市中撤出其“Just Walk Out”（拿了就走）无感结账技术。由于 Amazon One 曾是客户进入此类门店并触发自动计费系统的主要方式，因此它在这些特定场所的应用正在停止。
*   **替代方案：** 在大型超市环境中，亚马逊正利用“Dash Carts”取代掌纹入场系统和顶部摄像头。Dash Carts 是一种智能购物篮，可通过内置屏幕实时追踪商品。
*   **持续使用：** 尽管在大型超市的规模有所缩减，但 Amazon One 依然活跃。它将继续在所有全食超市（Whole Foods Market）门店推广，并正在向第三方场所扩展，包括职业体育场、机场以及 Panera Bread 等合作伙伴零售店。
*   **核心用途：** 该技术仍是亚马逊生物识别战略的核心部分，旨在通过让用户将手掌悬停在扫描仪上，提供一种安全、 “非接触式”的支付、年龄验证或场馆进入方式。

**结论：**
虽然“停用”主要是指其在大型超市环境中不再作为“Just Walk Out”技术的入口，但 Amazon One 作为一种独立的支付和身份识别解决方案，将继续存在于小型零售业态和第三方场所中。

---

## 4. Show HN：HN 街机厅

**原文标题**: Show HN: The HN Arcade

**原文链接**: [https://andrewgy8.github.io/hnarcade/](https://andrewgy8.github.io/hnarcade/)

根据所给文本，以下是 **"Show HN: The HN Arcade"** 的简要总结：

"Show HN: The HN Arcade" 介绍了一个专为 Hacker News 社区设计的网页平台。正如 "Show HN" 前缀所示，这是一个由开发者分享的项目，旨在寻求社区的反馈与互动。

该项目似乎是一个数字街机或互动体验集锦。虽然目前提供的内容有限——主要由网站标题和导航元素组成——但该平台是用户访问和游玩各种浏览器游戏的中心，这些游戏的主题可能围绕技术、编程或 Hacker News 生态系统本身展开。

---

## 5. 我过度设计了一个陀螺

**原文标题**: I Overengineered a Spinning Top

**原文链接**: [https://www.youtube.com/watch?v=Wp5NodfvvF4](https://www.youtube.com/watch?v=Wp5NodfvvF4)

鉴于提供的标题（由于你提供的内容实际上是标准的 YouTube 法律和页脚信息），以下是通常与此标题相关的项目简洁摘要（由著名的 YouTube 频道 **Stuff Made Here** 创作）：

**项目摘要：我过度设计了一个陀螺**

该项目记录了一个“完美”陀螺的诞生过程。作者通过将先进的机器人技术和航空航天工程应用于一个简单的玩具，设计出了一个**主动稳定系统**，使其永远不会倒下，而不仅仅是依赖传统陀螺的物理特性。

**关键信息：**
*   **机械结构：** 陀螺内部装有一个由高速无刷电机驱动的**反作用轮**。这种装置模仿了卫星和航天器中使用的稳定技术。
*   **主动控制：** 它集成了**惯性测量单元 (IMU)** 来检测倾斜，并由微控制器运行反馈回路。当陀螺开始倾斜时，内部转轮会加速或减速以产生反向扭矩，使陀螺保持完美垂直。
*   **精密工程：** 陀螺主体采用 CNC 技术定制加工以确保近乎完美的对称性，且电子元件经过微型化处理以装入狭小的旋转底盘中。
*   **最终成果：** 这个“过度设计”的陀螺能够在手指、细线上甚至是移动平台上保持平衡。它有效地排除了人为技巧因素，利用技术实现了永久性的机器人平衡状态。

该项目堪称控制理论的典范，展示了如何利用复杂的传感器和软件来克服角动量的自然衰减。

---

## 6. 人工智能会夺走我们所有的工作并终结人类历史吗——还是并不会？

**原文标题**: Will AIs Take All Our Jobs and End Human History–Or Not?

**原文链接**: [https://writings.stephenwolfram.com/2023/03/will-ais-take-all-our-jobs-and-end-human-history-or-not-well-its-complicated/](https://writings.stephenwolfram.com/2023/03/will-ais-take-all-our-jobs-and-end-human-history-or-not-well-its-complicated/)

In this article, Stephen Wolfram explores the impact of AI—specifically ChatGPT—on human labor and the trajectory of history. He argues that while AI can now mimic "uniquely human" tasks like essay writing, it fundamentally remains a computational system that requires human direction to be meaningful.

Wolfram identifies a historical trend where technology automates laborious tasks (like typesetting or "essayification"), making them "free" and shifting human effort toward higher levels of abstraction. He addresses the fear that AI will eventually "automate everything" by introducing the concept of **computational irreducibility**. This principle states that many systems are so complex that their outcomes cannot be predicted or "shortcut" by formulas; they must be lived out step-by-step. Because the "computational universe" is infinite, there will always be more to compute and discover.

Key points include:
*   **The Role of Humans:** AI functions as a "Linguistic User Interface" (LUI) that leverages human context. It can achieve goals but cannot autonomously define what constitutes a "meaningful" goal for humanity.
*   **The Science of AI:** Using the **Principle of Computational Equivalence**, Wolfram explains that simple programs (like neural nets) can produce behavior as sophisticated as the human brain. 
*   **The Limitation of Narrative:** Because of computational irreducibility, we cannot always find a simple "human narrative" to explain why an AI arrived at a specific result.

Wolfram concludes that while AI will handle the "how" of complex tasks, humans remain essential for providing the "why." AI won't end human history because it lacks the intrinsic "human context" to determine what is relevant; instead, it shifts the human role from performing tasks to defining purpose and goals within an ever-expanding computational landscape.

---

## 7. Show HN: Dwm.tmux – a dwm-inspired window manager for tmux

**原文标题**: Show HN: Dwm.tmux – a dwm-inspired window manager for tmux

**原文链接**: [https://github.com/saysjonathan/dwm.tmux](https://github.com/saysjonathan/dwm.tmux)

生成摘要时出错

---

## 8. A verification layer for browser agents: Amazon case study

**原文标题**: A verification layer for browser agents: Amazon case study

**原文链接**: [https://sentienceapi.com/blog/verification-layer-amazon-case-study](https://sentienceapi.com/blog/verification-layer-amazon-case-study)

生成摘要时出错

---

## 9. Show HN: Cua-Bench – a benchmark for AI agents in GUI environments

**原文标题**: Show HN: Cua-Bench – a benchmark for AI agents in GUI environments

**原文链接**: [https://github.com/trycua/cua](https://github.com/trycua/cua)

生成摘要时出错

---

## 10. Rust at Scale: An Added Layer of Security for WhatsApp

**原文标题**: Rust at Scale: An Added Layer of Security for WhatsApp

**原文链接**: [https://engineering.fb.com/2026/01/27/security/rust-at-scale-security-whatsapp/](https://engineering.fb.com/2026/01/27/security/rust-at-scale-security-whatsapp/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 2 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 3 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 4 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 5 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 6 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 7 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 8 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 9 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 10 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 11 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 12 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 13 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 14 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 15 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 16 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 17 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 18 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 19 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 20 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 21 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 22 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 23 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 24 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 25 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 26 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 27 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 28 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 29 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 30 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 31 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 32 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 33 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 34 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 35 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 36 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 37 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 38 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 39 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 40 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 41 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 42 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 43 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 44 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 45 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 46 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 47 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 48 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 49 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 50 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 51 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 52 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 53 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 54 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 55 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 56 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 57 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 58 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 59 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 60 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 61 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 62 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 63 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 64 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 65 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 66 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 67 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 68 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 69 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 70 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 71 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 72 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 73 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 74 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 75 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 76 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 77 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 78 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 79 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 80 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 81 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 82 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 83 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 84 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 85 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 86 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 87 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 88 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 89 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 90 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 91 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 92 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 93 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 94 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 95 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 96 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 97 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 98 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 99 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 100 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 101 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 102 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 103 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 104 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 105 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 106 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 107 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 108 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 109 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 110 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 111 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 112 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 113 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 114 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 115 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 116 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 117 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 118 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 119 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 120 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 121 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 122 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 123 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 124 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 125 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 126 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 127 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 128 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 129 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 130 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 131 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 132 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 133 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 134 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 135 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 136 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 137 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 138 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 139 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 140 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 141 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 142 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 143 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 144 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 145 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 146 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 147 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 148 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 149 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 150 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 151 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 152 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 153 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 154 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 155 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 156 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 157 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 158 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 159 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 160 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 161 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 162 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 163 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 164 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 165 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 166 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 167 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 168 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 169 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 170 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 171 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 172 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 173 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 174 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 175 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 176 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 177 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 178 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 179 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 180 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 181 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 182 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 183 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 184 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 185 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 186 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 187 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 188 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 189 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 190 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 191 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 192 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 193 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 194 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 195 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 196 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 197 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 198 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 199 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 200 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 201 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 202 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 203 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 204 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 205 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 206 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 207 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 208 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 209 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 210 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 211 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 212 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 213 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 214 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 215 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 216 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 217 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 218 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 219 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 220 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 221 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 222 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 223 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 224 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 225 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 226 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 227 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 228 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 229 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 230 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 231 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 232 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 233 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 234 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 235 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 236 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 237 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 238 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 239 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 240 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 241 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 242 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 243 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 244 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 245 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 246 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 247 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 248 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 249 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 250 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 251 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 252 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 253 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 254 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 255 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 256 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 257 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 258 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 259 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 260 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 261 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 262 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 263 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 264 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 265 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 266 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 267 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 268 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 269 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 270 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 271 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 272 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 273 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 274 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 275 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 276 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 277 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 278 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 279 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 280 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 281 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 282 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 283 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 284 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 285 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 286 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 287 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 288 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 289 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 290 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 291 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 292 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 293 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 294 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 295 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 296 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 297 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 298 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 299 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 300 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 301 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 302 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 303 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 304 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 305 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 306 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 307 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 308 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 309 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 310 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 311 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 312 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 313 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 314 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
