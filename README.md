# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-09.md)

*最后自动更新时间: 2026-04-09 18:24:04*
## 1. Show HN: 月球模拟器游戏，光线投射

**原文标题**: Show HN: Moon simulator game, ray-casting

**原文链接**: [https://mooncraft2000.com](https://mooncraft2000.com)

**Mooncraft** 是一款近期在 Hacker News 的 “Show HN” 栏目中亮相的网页端月球模拟器游戏。该项目利用名为 **光线投射 (ray-casting)** 的经典渲染技术，通过 HTML5 画布 (Canvas) 元素来构建其视觉环境。

这款游戏旨在为玩家提供探索月球景观的互动体验。加载完成后，用户会看到开始游戏的欢迎提示。虽然游戏可以免费游玩，但开发者也发出了号召，希望玩家能通过“请喝一杯清酒咖啡”来支持该项目。

总而言之，Mooncraft 是将光线投射技术应用于太空主题模拟的一场技术演示，用户可以直接通过现代网页浏览器进行体验。

---

## 2. Unity 2026 中的 C#：编写更现代的代码

**原文标题**: C# in Unity 2026: Writing more modern code

**原文链接**: [https://darkounity.com/blog/c-in-unity-2026-features-most-developers-still-dont-use](https://darkounity.com/blog/c-in-unity-2026-features-most-developers-still-dont-use)

随着 Unity 向 .NET 8 和 CoreCLR 运行时过渡，**Unity 2026** 引入了一系列现代 C# 特性（源自 C# 10、11 和 12），许多开发者尚未采用这些特性。本文强调应摆脱传统的“Mono 时代”编码模式，转向更高效、简洁且安全的替代方案。

**重点特性摘要：**

*   **通过 Span<T> 和 Memory<T> 提升性能：** 这些特性支持高性能内存操作，且无需堆分配开销。它们对于优化字符串解析、缓冲区管理和密集型数学运算至关重要，同时能有效减轻垃圾回收（GC）压力。
*   **记录（Records）和仅初始化 Setter（Init-Only Setters）：** 它们为 Unity 引入了“数据对象”概念。记录提供了内置的值相等性检查，非常适合网络通信、游戏状态快照和 DTO。`init` setter 确保对象在创建后保持不可变，增强了代码的可靠性。
*   **主构造函数（Primary Constructors）：** C# 12 引入的特性，允许开发者直接在声明中定义类或结构的参数。这极大地减少了依赖注入和简单数据容器的样板代码。
*   **高级模式匹配：** 现代模式匹配（包括关系模式和属性模式）超越了简单的“if”语句，使复杂逻辑更具表现力且易于阅读，例如在单个表达式中检查 GameObject 的多个状态。
*   **原始字符串字面量（Raw String Literals）：** 通过使用三引号 (`"""`)，简化了在脚本中嵌入多行字符串、JSON 或 XML 的方式，消除了对繁琐转义字符的需求。
*   **性能优化的内插字符串：** 现代 C# 更高效地处理字符串内插，减少了日志记录或 UI 更新期间的内存分配。

**结论：**
本文指出，采用这些特性对于充分利用新 Unity 运行时的性能优势至关重要。通过转向这些现代标准，开发者可以编写出更整洁、更易于维护且执行速度显著提升的代码。

---

## 3. 我将 Mac OS X 移植到了任天堂 Wii

**原文标题**: I ported Mac OS X to the Nintendo Wii

**原文链接**: [https://bryankeller.github.io/2026/04/08/porting-mac-os-x-nintendo-wii.html](https://bryankeller.github.io/2026/04/08/porting-mac-os-x-nintendo-wii.html)

在这篇技术深度解析中，作者详述了将 Mac OS X 10.0 (Cheetah) 成功移植到 Nintendo Wii 的过程，使其与 Linux 和 Windows NT 一样成为该主机的适配系统。

尽管社区存在质疑，但作者认定 Wii 的 PowerPC 750CL 处理器是早期 Mac 所使用的 G3 处理器的直接演进版本。虽然 Wii 的 88 MB 内存低于 Cheetah 官方要求的 128 MB，但测试确认该系统可以在更低内存下启动。

作者选择从零编写自定义引导加载程序（bootloader），而非移植苹果的 Open Firmware。该引导程序负责硬件初始化、加载 Mach-O 内核并构建设备树——这是内核运行所需的一种描述 Wii 硬件的数据结构。为了在视频或串口输出可用之前调试早期启动过程，作者采用了一个巧妙的手段：对内核进行二进制补丁，通过闪烁 Wii 前面板的 LED 灯来确认特定代码块的执行情况。

关键技术挑战包括：
*   **内核补丁：** 修改 XNU 内核源码以解决内存布局问题，特别是重新配置块地址转换（BATs）以匹配 Wii 独特的内存配置。
*   **开发环境：** 使用 QEMU 搭建陈旧的开发环境，以编译具有 25 年历史的 XNU 源码。
*   **驱动程序：** 实现 IOKit 驱动程序，以连接操作系统与 Wii 的特定硬件。

目前该项目已取得重大里程碑：内核已成功初始化并运行至“Still waiting for root device”（仍在等待根设备）阶段。这标志着核心操作系统已实现原生运行，后续仍需编写 SD 卡的 IOKit 驱动，以支持系统加载完整的桌面环境。

---

## 4. 通过简单雷达示例理解卡尔曼滤波

**原文标题**: Understanding the Kalman filter with a simple radar example

**原文链接**: [https://kalmanfilter.net](https://kalmanfilter.net)

卡尔曼滤波是一种最优估计算法，旨在测量噪声和外部“过程”因素引起的不确定性中，预测并估计系统的状态（如位置或速度）。该滤波器广泛应用于导航、机器人和金融领域，既能提供状态估计，也能提供该估计可靠性的数学度量。

本文通过一维雷达追踪飞机的案例来阐释这些概念。在这种场景下，系统状态由飞机的距离 ($r$) 和速度 ($v$) 组成。由于雷达测量存在误差，且飞机的运动可能受到风等不可预测因素的影响，卡尔曼滤波利用动态模型提供比单纯依靠测量值更准确的描述。

该过程包含两个主要阶段：
1. **初始化：** 滤波器利用首次获得的测量值来建立初始状态向量 ($\hat{x}$) 和测量协方差矩阵 ($R$)，后者代表了传感器的方差（不确定性）。
2. **预测（外推）：** 滤波器利用状态转移矩阵 ($F$)，基于运动模型（如匀速运动）将当前状态投射到未来。同时，它对外推状态协方差矩阵 ($P$)，以追踪预测步骤中不确定性的增长或变化。

通过运用线性代数，卡尔曼滤波有效地平衡了带噪声的现实数据与理论模型。它将状态估计的不确定性降至最低，使其成为任何在随机性环境下需要精确追踪与控制的应用中不可或缺的工具。

---

## 5. Show HN: 41 years sea surface temperature anomalies

**原文标题**: Show HN: 41 years sea surface temperature anomalies

**原文链接**: [https://ssta.willhelps.org](https://ssta.willhelps.org)

生成摘要时出错

---

## 6. Dr. Dobb's Developer Library DVD 6 (2010)

**原文标题**: Dr. Dobb's Developer Library DVD 6 (2010)

**原文链接**: [https://archive.org/details/DDJDVD6](https://archive.org/details/DDJDVD6)

生成摘要时出错

---

## 7. Improving storage efficiency in Magic Pocket, Dropbox's immutable blob store

**原文标题**: Improving storage efficiency in Magic Pocket, Dropbox's immutable blob store

**原文链接**: [https://dropbox.tech/infrastructure/improving-storage-efficiency-in-magic-pocket-our-immutable-blob-store](https://dropbox.tech/infrastructure/improving-storage-efficiency-in-magic-pocket-our-immutable-blob-store)

Dropbox’s Magic Pocket, an exabyte-scale immutable blob store, recently faced a storage efficiency challenge after a new service, "Live Coder," caused severe volume fragmentation. Many volumes were left significantly under-filled—some holding less than 5% live data—leading to a sharp rise in storage overhead. 

Because Magic Pocket is immutable, deleted data is not removed in place; instead, space is reclaimed through "compaction," where live data is rewritten into new volumes and old ones are retired. To resolve the fragmentation, Dropbox evolved its compaction strategy into a three-tiered approach:

1.  **L1 (Steady State):** The legacy strategy that "tops off" nearly-full host volumes using sparse donors. It is stable but inefficient at handling a large volume of severely under-filled disks.
2.  **L2 (Consolidation):** Designed for moderately under-filled volumes, L2 uses dynamic programming to group multiple sparse volumes into a single near-full destination. In production, L2 reclaimed space 2–3 times faster than L1.
3.  **L3 (Tail Reclamation):** Targets the sparsest volumes by streaming their remaining live blobs into a continuous erasure-coding pipeline. This allows the emptiest volumes to be reclaimed immediately with minimal rewriting.

To maintain system stability, Dropbox implemented dynamic control loops that adjust compaction thresholds based on fleet signals and rate-limited the pipeline to avoid impacting user traffic. By running L1, L2, and L3 concurrently, Dropbox successfully reduced storage overhead to levels below its original baseline. This transition highlights the necessity of flexible data reclamation strategies when storage distribution patterns shift at scale.

---

## 8. ML promises to be profoundly weird

**原文标题**: ML promises to be profoundly weird

**原文链接**: [https://aphyr.com/posts/411-the-future-of-everything-is-lies-i-guess](https://aphyr.com/posts/411-the-future-of-everything-is-lies-i-guess)

生成摘要时出错

---

## 9. Git commands I run before reading any code

**原文标题**: Git commands I run before reading any code

**原文链接**: [https://piechowski.io/post/git-commands-before-reading-code/](https://piechowski.io/post/git-commands-before-reading-code/)

生成摘要时出错

---

## 10. The Pentagon Threatened Pope Leo XIV's Ambassador with the Avignon Papacy

**原文标题**: The Pentagon Threatened Pope Leo XIV's Ambassador with the Avignon Papacy

**原文链接**: [https://www.thelettersfromleo.com/p/the-pentagon-threatened-pope-leo](https://www.thelettersfromleo.com/p/the-pentagon-threatened-pope-leo)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 2 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 3 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 4 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 5 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 6 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 7 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 8 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 9 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 10 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 11 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 12 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 13 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 14 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 15 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 16 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 17 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 18 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 19 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 20 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 21 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 22 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 23 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 24 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 25 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 26 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 27 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 28 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 29 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 30 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 31 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 32 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 33 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 34 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 35 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 36 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 37 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 38 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 39 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 40 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 41 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 42 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 43 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 44 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 45 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 46 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 47 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 48 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 49 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 50 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 51 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 52 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 53 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 54 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 55 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 56 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 57 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 58 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 59 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 60 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 61 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 62 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 63 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 64 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 65 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 66 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 67 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 68 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 69 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 70 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 71 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 72 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 73 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 74 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 75 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 76 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 77 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 78 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 79 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 80 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 81 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 82 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 83 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 84 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 85 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 86 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 87 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 88 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 89 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 90 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 91 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 92 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 93 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 94 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 95 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 96 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 97 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 98 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 99 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 100 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 101 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 102 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 103 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 104 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 105 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 106 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 107 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 108 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 109 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 110 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 111 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 112 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 113 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 114 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 115 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 116 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 117 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 118 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 119 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 120 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 121 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 122 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 123 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 124 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 125 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 126 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 127 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 128 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 129 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 130 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 131 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 132 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 133 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 134 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 135 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 136 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 137 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 138 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 139 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 140 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 141 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 142 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 143 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 144 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 145 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 146 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 147 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 148 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 149 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 150 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 151 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 152 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 153 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 154 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 155 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 156 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 157 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 158 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 159 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 160 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 161 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 162 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 163 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 164 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 165 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 166 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 167 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 168 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 169 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 170 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 171 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 172 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 173 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 174 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 175 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 176 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 177 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 178 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 179 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 180 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 181 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 182 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 183 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 184 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 185 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 186 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 187 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 188 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 189 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 190 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 191 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 192 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 193 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 194 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 195 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 196 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 197 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 198 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 199 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 200 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 201 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 202 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 203 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 204 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 205 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 206 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 207 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 208 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 209 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 210 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 211 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 212 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 213 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 214 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 215 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 216 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 217 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 218 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 219 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 220 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 221 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 222 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 223 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 224 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 225 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 226 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 227 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 228 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 229 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 230 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 231 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 232 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 233 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 234 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 235 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 236 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 237 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 238 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 239 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 240 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 241 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 242 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 243 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 244 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 245 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 246 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 247 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 248 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 249 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 250 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 251 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 252 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 253 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 254 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 255 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 256 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 257 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 258 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 259 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 260 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 261 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 262 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 263 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 264 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 265 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 266 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 267 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 268 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 269 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 270 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 271 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 272 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 273 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 274 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 275 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 276 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 277 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 278 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 279 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 280 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 281 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 282 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 283 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 284 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 285 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 286 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 287 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 288 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 289 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 290 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 291 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 292 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 293 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 294 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 295 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 296 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 297 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 298 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 299 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 300 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 301 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 302 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 303 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 304 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 305 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 306 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 307 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 308 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 309 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 310 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 311 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 312 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 313 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 314 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 315 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 316 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 317 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 318 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 319 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 320 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 321 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 322 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 323 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 324 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 325 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 326 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 327 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 328 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 329 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 330 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 331 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 332 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 333 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 334 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 335 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 336 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 337 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 338 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 339 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 340 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 341 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 342 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 343 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 344 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 345 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 346 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 347 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 348 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 349 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 350 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 351 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 352 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 353 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 354 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 355 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 356 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 357 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 358 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 359 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 360 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 361 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 362 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 363 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 364 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 365 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 366 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 367 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 368 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 369 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 370 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 371 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 372 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 373 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 374 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 375 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 376 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 377 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 378 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 379 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 380 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 381 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 382 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 383 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 384 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 385 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
