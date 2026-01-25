# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-01-25.md)

*最后自动更新时间: 2026-01-25 17:46:29*
## 1. 一款在你驼背时模糊屏幕的 macOS 应用

**原文标题**: A macOS app that blurs your screen when you slouch

**原文链接**: [https://github.com/tldev/posturr](https://github.com/tldev/posturr)

**Posturr** 是一款注重隐私保护的 macOS 应用程序，旨在通过在用户坐姿不正时逐渐模糊屏幕来改善人体工程学。该应用利用 Apple 的 Vision 框架，通过 Mac 摄像头实时监测身体关键点（特别是鼻子和肩膀的位置）。当用户偏离校准后的“良好姿势”时，所有连接的显示器都会出现系统级的模糊效果并随之增强；一旦用户坐直，屏幕会立即恢复清晰。

**核心功能与特性：**
*   **实时检测：** 采用本地图像处理技术追踪姿势，无需上传数据至云端，也不需要注册账号。
*   **自定义控制：** 用户可通过 macOS 菜单栏管理应用，包括调节灵敏度、设置“死区”（容差范围）以及重新校准基准姿势。
*   **隐私与性能：** 应用轻便且在后台运行，所有摄像头素材均在本地处理，确保用户隐私安全。
*   **高级集成：** 包含一个基于文件的命令接口，用于外部控制（如手动设置模糊或触发分析）。

**安装与

通过提供温和而持久的视觉提醒，Posturr 为需要在电脑前长时间工作的开发者和专业人士提供了一个维护脊柱健康的实用工具。

---

## 2. 将 PostgreSQL 用作事件驱动系统的死信队列

**原文标题**: Using PostgreSQL as a Dead Letter Queue for Event-Driven Systems

**原文链接**: [https://www.diljitpr.net/blog-post-postgresql-dlq](https://www.diljitpr.net/blog-post-postgresql-dlq)

本文讨论了在事件驱动系统中使用 **PostgreSQL 作为死信队列 (DLQ)** 处理故障的战略方法。虽然 Kafka 在高吞吐量流处理方面表现卓越，但它缺乏管理、检查和选择性重新处理失败事件所需的内在可视化和可查询性。

**策略方案**
为了克服这些局限性，团队在 PostgreSQL 中实现了一个专门的 `dlq_events` 表。失败的消息不会被丢弃或发送到 Kafka 主题，而是与原始 JSONB 负载、错误堆栈跟踪和元数据（状态、重试次数和时间戳）一起存储。这种方法将故障转化为“一等公民”，允许工程师使用标准 SQL 来审计“失败的内容及原因”。

**技术实现**
该系统采用了包含两个核心组件的稳健重试机制：
*   **ShedLock：** 确保同一时间只有一个服务实例执行重试任务，防止分布式环境中的重复处理。
*   **`FOR UPDATE SKIP LOCKED`：** 这一 PostgreSQL 特性允许跨实例安全地并发选择并锁定不同的行进行处理，在不产生行竞争的情况下显著提高吞吐量。

**运维优势**
基于 PostgreSQL 的 DLQ 相比传统流式 DLQ 具有多项优势：
*   **可观测性：** 工程师可以轻松查询故障，以识别特定模式或 Schema 不匹配。
*   **可控性：** 通过可配置的批次和间隔管理重试，防止下游停机期间出现“重试风暴”。
*   **韧性：** 事件可以无限期存储，并仅在依赖项稳定时重新处理。

通过利用 PostgreSQL 的持久性和查询能力，同时保持 Kafka 作为摄取主干，该系统实现了一条“乏味”且可预测的故障处理路径。这种架构确保了错误是可观测且可管理的，而不再是隐蔽或具有破坏性的。

---

## 3. 《管理科学》中一篇有缺陷的论文已被引用超过6000次。

**原文标题**: A flawed paper in Management Science has been cited more than 6,000 times

**原文链接**: [https://statmodeling.stat.columbia.edu/2026/01/22/aking/](https://statmodeling.stat.columbia.edu/2026/01/22/aking/)

生成摘要时出错

---

## 4. 《毁灭战士》已被移植到耳机上。

**原文标题**: Doom has been ported to an earbud

**原文链接**: [https://doombuds.com](https://doombuds.com)

“DOOMBUDS”项目是一项技术壮举，成功将 1993 年的经典游戏《DOOM》移植到了 Pinebuds Pro 耳机上。由于这是唯一一款采用开源固件的耳机，开发者得以绕过标准限制，在内部硬件上运行游戏，并实现了通过 Web 浏览器进行远程游玩。

**技术实现：**
*   **视频与连接：** 由于耳机没有屏幕，开发者利用 UART 触点（提供 2.4mbps 速率）而非蓝牙来传输数据。为克服带宽限制，游戏的帧缓冲被压缩为 MJPEG 流。虽然硬件理论上可达 27 FPS，但由于 CPU 编码开销，目前最高仅为 **18 FPS**。
*   **处理能力：** Cortex-M4F CPU 从 100MHz 超频至 **300MHz**，并禁用了低功耗模式以处理高强度的 JPEG 编码。
*   **内存管理：** 《DOOM》通常需要 4MB RAM，但该耳机仅提供 992KB。开发者通过禁用缓存系统、预生成查找表以及将变量移至闪存，成功实现了内存缩减。
*   **存储：** 标准的 4.2MB DOOM WAD 文件超出了耳机 4MB 闪存的容量。该项目采用了“Squashware”（一个 1.7MB 的精简版游戏资源包）以适应存储限制。

**项目体验：**
该项目在线托管并设有排队系统。Web 服务器负责管理按键指令并处理流媒体：观众通过 Twitch 观看，而当前玩家则切换到低延迟的 MJPEG 流。代码已开源，耳机固件和基于 JavaScript 的 Web 界面均已提供代码仓库。

---

## 5. 谷歌确认 Android 将引入“高阻力”侧载流程。

**原文标题**: Google confirms 'high-friction' sideloading flow is coming to Android

**原文链接**: [https://www.androidauthority.com/google-sideloading-android-high-friction-process-3633468/](https://www.androidauthority.com/google-sideloading-android-high-friction-process-3633468/)

谷歌已确认将为 Android 引入一种“高摩擦”侧载流程，该公司将其称为“责任层”（Accountability Layer）。据 Google Play 产品管理总监 Matthew Forsyth 称，此次更新旨在让用户了解从未经核实的开发者处安装应用的潜在安全风险，而非完全禁止这一行为。

在新系统下，用户仍可通过选择“不经验证安装”选项来侧载应用。然而，这样做将涉及额外的步骤和更显眼的警告提示。最近在 Google Play 代码串中发现的这些警告，强调了缺乏开发者验证的情况以及与未经核实软件相关的潜在危险。

高级用户和开发者主要担心这种“摩擦”是会保持作为一种简单的教育工具，还是会演变成一种更具限制性的障碍，从而刻意增加侧载的难度。虽然目前的实施方式不需要外部工具或电脑即可完成安装，但此举标志着 Android 在其传统的开放生态系统中正转向加强监管。目前，谷歌坚称其目标是提高用户意识，确保那些绕过官方商店的用户能够充分了解相关风险。

---

## 6. Show HN：Bonsplit —— 为 macOS 原生应用提供标签页与分屏功能

**原文标题**: Show HN: Bonsplit – Tabs and splits for native macOS apps

**原文链接**: [https://bonsplit.alasdairmonk.com](https://bonsplit.alasdairmonk.com)

**Bonsplit** 是一款专为 SwiftUI 应用设计的原生 macOS 库，旨在引入先进的标签栏和拆分窗格功能。它提供专业级的 UI 体验，具备 120fps 动画、键盘导航，以及用于重排标签或在窗格间移动标签的强大拖放支持。

核心特性与功能包括：

*   **灵活布局：** 用户可以水平或垂直拆分窗格，以构建类似 IDE 的复杂界面。开发者可以通过编程方式创建、关闭和更新标签，并支持自定义图标以及未保存更改的“修改（dirty）”状态指示器。
*   **焦点管理：** 该库内置焦点管理，支持在不同窗格之间进行编程式导航和方向导航（上、下、左、右）。
*   **高度可定制性：** 通过 `BonsplitController` 和 `BonsplitConfiguration`，开发者可以开关标签重排、跨窗格移动和拆分按钮等功能。同时支持微调外观细节，如标签尺寸、间距和动画时长。
*   **生命周期控制：** `ContentViewLifecycle` 设置是优化性能的关键。开发者可以选择在切换标签时重新创建视图以节省内存，或保持视图存活以保留复杂的交互状态。
*   **事件处理：** `BonsplitDelegate` 协议为标签创建、窗格拆分和焦点变化等事件提供了一套全面的可选回调，确保该库能够与应用逻辑无缝集成。

Bonsplit 以 Swift Package 形式提供，为寻求在原生 macOS 应用中实现复杂窗口管理的开发者提供了一个高性能且高度可配置的解决方案。

---

## 7. Web-based image editor modeled after Deluxe Paint

**原文标题**: Web-based image editor modeled after Deluxe Paint

**原文链接**: [https://github.com/steffest/DPaint-js](https://github.com/steffest/DPaint-js)

生成摘要时出错

---

## 8. PostgreSQL 索引简介

**原文标题**: Introduction to PostgreSQL Indexes

**原文链接**: [https://dlt.github.io/blog/posts/introduction-to-postgresql-indexes/](https://dlt.github.io/blog/posts/introduction-to-postgresql-indexes/)

本文提供了 PostgreSQL 索引的技术概览，旨在帮助开发者理解其内部机制、性能影响及权衡。

**核心机制**
PostgreSQL 将表数据存储在划分为 8KB 页面的“堆”（heaps）中。每一行（或称元组）通过 `ctid`（元组 ID）进行标识，该 ID 充当物理磁盘地址。索引作为树形结构，将特定的列值映射到这些 `ctid`。通过使用索引，数据库可以直接跳转到所需数据，从而显著减少磁盘 I/O。在演示示例中，通过将读取的页面数量从 6,000 多个减少到仅 4 个，索引使查询时间从 265 毫秒降至 0.08 毫秒。

**权衡与成本**
索引并非“免费”的，它涉及多项开销：
*   **磁盘空间：** 索引会消耗额外的存储空间，有时甚至会比表本身还要大。
*   **写入性能：** 对索引列执行的每次 `INSERT`、`UPDATE` 或 `DELETE` 操作都需要同步更新索引。
*   **维护成本：** 索引越多，备份体积和复制流量就越大，且查询规划器评估执行策略所需的时间也会增加。
*   **内存占用：** 索引会竞争共享缓冲区（shared buffers）的空间；大型索引可能会挤出缓存的数据页。

**关键索引策略**
*   **B-Tree：** 默认的平衡树结构。它提供 O(log n) 的搜索效率，并支持排序、连接和唯一性约束。
*   **位图扫描 (Bitmap Scans)：** PostgreSQL 可以利用位图为单个查询组合多个单列索引。
*   **多列索引：** 适用于复杂过滤，但依赖于列的顺序；仅当查询利用了最左侧的列时才有效。
*   **部分索引：** 通过使用 `WHERE` 子句，仅对行的子集建立索引，从而减少特定用例下的体积和维护开销。

最终，只有当查询返回的数据量少于表中总数据的 15-20% 时，索引才最为有效；否则，查询规划器可能更倾向于使用顺序扫描。

---

## 9. ANN v3: 200ms p99 query latency over 100B vectors

**原文标题**: ANN v3: 200ms p99 query latency over 100B vectors

**原文链接**: [https://turbopuffer.com/blog/ann-v3](https://turbopuffer.com/blog/ann-v3)

生成摘要时出错

---

## 10. Show HN: Netfence – Like Envoy for eBPF Filters

**原文标题**: Show HN: Netfence – Like Envoy for eBPF Filters

**原文链接**: [https://github.com/danthegoodman1/netfence](https://github.com/danthegoodman1/netfence)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 2 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 3 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 4 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 5 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 6 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 7 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 8 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 9 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 10 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 11 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 12 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 13 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 14 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 15 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 16 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 17 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 18 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 19 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 20 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 21 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 22 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 23 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 24 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 25 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 26 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 27 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 28 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 29 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 30 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 31 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 32 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 33 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 34 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 35 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 36 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 37 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 38 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 39 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 40 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 41 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 42 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 43 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 44 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 45 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 46 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 47 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 48 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 49 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 50 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 51 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 52 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 53 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 54 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 55 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 56 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 57 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 58 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 59 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 60 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 61 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 62 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 63 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 64 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 65 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 66 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 67 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 68 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 69 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 70 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 71 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 72 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 73 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 74 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 75 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 76 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 77 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 78 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 79 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 80 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 81 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 82 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 83 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 84 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 85 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 86 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 87 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 88 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 89 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 90 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 91 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 92 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 93 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 94 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 95 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 96 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 97 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 98 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 99 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 100 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 101 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 102 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 103 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 104 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 105 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 106 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 107 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 108 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 109 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 110 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 111 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 112 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 113 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 114 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 115 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 116 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 117 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 118 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 119 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 120 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 121 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 122 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 123 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 124 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 125 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 126 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 127 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 128 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 129 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 130 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 131 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 132 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 133 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 134 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 135 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 136 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 137 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 138 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 139 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 140 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 141 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 142 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 143 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 144 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 145 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 146 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 147 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 148 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 149 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 150 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 151 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 152 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 153 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 154 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 155 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 156 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 157 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 158 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 159 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 160 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 161 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 162 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 163 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 164 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 165 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 166 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 167 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 168 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 169 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 170 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 171 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 172 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 173 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 174 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 175 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 176 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 177 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 178 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 179 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 180 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 181 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 182 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 183 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 184 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 185 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 186 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 187 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 188 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 189 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 190 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 191 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 192 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 193 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 194 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 195 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 196 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 197 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 198 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 199 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 200 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 201 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 202 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 203 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 204 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 205 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 206 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 207 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 208 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 209 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 210 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 211 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 212 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 213 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 214 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 215 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 216 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 217 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 218 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 219 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 220 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 221 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 222 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 223 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 224 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 225 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 226 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 227 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 228 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 229 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 230 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 231 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 232 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 233 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 234 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 235 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 236 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 237 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 238 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 239 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 240 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 241 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 242 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 243 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 244 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 245 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 246 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 247 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 248 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 249 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 250 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 251 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 252 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 253 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 254 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 255 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 256 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 257 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 258 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 259 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 260 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 261 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 262 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 263 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 264 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 265 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 266 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 267 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 268 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 269 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 270 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 271 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 272 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 273 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 274 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 275 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 276 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 277 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 278 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 279 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 280 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 281 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 282 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 283 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 284 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 285 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 286 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 287 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 288 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 289 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 290 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 291 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 292 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 293 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 294 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 295 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 296 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 297 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 298 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 299 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 300 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 301 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 302 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 303 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 304 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 305 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 306 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 307 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 308 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 309 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 310 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 311 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
