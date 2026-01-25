# Hacker News 热门文章摘要 (2026-01-25)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Show HN: TUI for managing XDG default applications

**原文标题**: Show HN: TUI for managing XDG default applications

**原文链接**: [https://github.com/mitjafelicijan/xdgctl](https://github.com/mitjafelicijan/xdgctl)

生成摘要时出错

---

## 12. Wine-Staging 11.1 Adds Patches for Enabling Recent Photoshop Versions on Linux

**原文标题**: Wine-Staging 11.1 Adds Patches for Enabling Recent Photoshop Versions on Linux

**原文链接**: [https://www.phoronix.com/news/Wine-Staging-11.1](https://www.phoronix.com/news/Wine-Staging-11.1)

生成摘要时出错

---

## 13. White House alters arrest photo of ICE protester, says "the memes will continue"

**原文标题**: White House alters arrest photo of ICE protester, says "the memes will continue"

**原文链接**: [https://arstechnica.com/tech-policy/2026/01/white-house-posts-altered-arrest-photo-to-make-it-appear-ice-critic-was-sobbing/](https://arstechnica.com/tech-policy/2026/01/white-house-posts-altered-arrest-photo-to-make-it-appear-ice-critic-was-sobbing/)

生成摘要时出错

---

## 14. Jurassic Park - Tablet device on Nedry's desk? (2012)

**原文标题**: Jurassic Park - Tablet device on Nedry's desk? (2012)

**原文链接**: [https://www.therpf.com/forums/threads/jurassic-park-tablet-device-on-nedrys-desk.169883/](https://www.therpf.com/forums/threads/jurassic-park-tablet-device-on-nedrys-desk.169883/)

生成摘要时出错

---

## 15. Bridging the Gap Between PLECS and SPICE

**原文标题**: Bridging the Gap Between PLECS and SPICE

**原文链接**: [https://erickschulz.dev/posts/plecs-spice/](https://erickschulz.dev/posts/plecs-spice/)

生成摘要时出错

---

## 16. Nango (YC W23, Dev Infrastructure) Is Hiring Remotely

**原文标题**: Nango (YC W23, Dev Infrastructure) Is Hiring Remotely

**原文链接**: [https://jobs.ashbyhq.com/Nango](https://jobs.ashbyhq.com/Nango)

生成摘要时出错

---

## 17. The Rebirth of Pennsylvania's Infamous Burning Town

**原文标题**: The Rebirth of Pennsylvania's Infamous Burning Town

**原文链接**: [https://www.atlasobscura.com/articles/centralia-pennsylvania-rebirth](https://www.atlasobscura.com/articles/centralia-pennsylvania-rebirth)

生成摘要时出错

---

## 18. I built a 2x faster lexer, then discovered I/O was the real bottleneck

**原文标题**: I built a 2x faster lexer, then discovered I/O was the real bottleneck

**原文链接**: [https://modulovalue.com/blog/syscall-overhead-tar-gz-io-performance/](https://modulovalue.com/blog/syscall-overhead-tar-gz-io-performance/)

生成摘要时出错

---

## 19. A Lament for Aperture

**原文标题**: A Lament for Aperture

**原文链接**: [https://ikennd.ac/blog/2026/01/old-man-yells-at-modern-software-design/](https://ikennd.ac/blog/2026/01/old-man-yells-at-modern-software-design/)

生成摘要时出错

---

## 20. Alarm overload is undermining safety at sea as crews face thousands of alerts

**原文标题**: Alarm overload is undermining safety at sea as crews face thousands of alerts

**原文链接**: [https://www.lr.org/en/knowledge/press-room/press-listing/press-release/2026/alarm-overload-is-undermining-safety-at-sea-as-new-research-shows-crews-face-tens-of-thousands-of-daily-alerts/](https://www.lr.org/en/knowledge/press-room/press-listing/press-release/2026/alarm-overload-is-undermining-safety-at-sea-as-new-research-shows-crews-face-tens-of-thousands-of-daily-alerts/)

生成摘要时出错

---

## 21. BU-808: How to Prolong Lithium-based Batteries (2023)

**原文标题**: BU-808: How to Prolong Lithium-based Batteries (2023)

**原文链接**: [https://www.batteryuniversity.com/article/bu-808-how-to-prolong-lithium-based-batteries/](https://www.batteryuniversity.com/article/bu-808-how-to-prolong-lithium-based-batteries/)

生成摘要时出错

---

## 22. Sony Data Discman

**原文标题**: Sony Data Discman

**原文链接**: [https://huguesjohnson.com/random/sony-ebook/](https://huguesjohnson.com/random/sony-ebook/)

生成摘要时出错

---

## 23. Show HN: LangGraph architecture that scales (hexagonal pattern, 110 tests)

**原文标题**: Show HN: LangGraph architecture that scales (hexagonal pattern, 110 tests)

**原文链接**: [https://github.com/cleverhoods/sagecompass](https://github.com/cleverhoods/sagecompass)

生成摘要时出错

---

## 24. Adoption of EVs tied to real-world reductions in air pollution: study

**原文标题**: Adoption of EVs tied to real-world reductions in air pollution: study

**原文链接**: [https://keck.usc.edu/news/adoption-of-electric-vehicles-tied-to-real-world-reductions-in-air-pollution-study-finds/](https://keck.usc.edu/news/adoption-of-electric-vehicles-tied-to-real-world-reductions-in-air-pollution-study-finds/)

生成摘要时出错

---

## 25. Back to Bellevue

**原文标题**: Back to Bellevue

**原文链接**: [https://theamericanscholar.org/back-to-bellevue/](https://theamericanscholar.org/back-to-bellevue/)

生成摘要时出错

---

## 26. Hands-On with Two Apple Network Server Prototype ROMs

**原文标题**: Hands-On with Two Apple Network Server Prototype ROMs

**原文链接**: [http://oldvcr.blogspot.com/2026/01/hands-on-with-two-apple-network-server.html](http://oldvcr.blogspot.com/2026/01/hands-on-with-two-apple-network-server.html)

生成摘要时出错

---

## 27. 150k lines of vibe coded Elixir: The Good, the Bad and the Ugly

**原文标题**: 150k lines of vibe coded Elixir: The Good, the Bad and the Ugly

**原文链接**: [https://getboothiq.com/blog/150k-lines-vibe-coded-elixir-good-bad-ugly](https://getboothiq.com/blog/150k-lines-vibe-coded-elixir-good-bad-ugly)

生成摘要时出错

---

## 28. Deutsche Telekom is throttling the internet

**原文标题**: Deutsche Telekom is throttling the internet

**原文链接**: [https://netzbremse.de/en/](https://netzbremse.de/en/)

生成摘要时出错

---

## 29. Challenges and Research Directions for Large Language Model Inference Hardware

**原文标题**: Challenges and Research Directions for Large Language Model Inference Hardware

**原文链接**: [https://arxiv.org/abs/2601.05047](https://arxiv.org/abs/2601.05047)

生成摘要时出错

---

## 30. Two Weeks Until Tapeout

**原文标题**: Two Weeks Until Tapeout

**原文链接**: [https://essenceia.github.io/projects/two_weeks_until_tapeout/](https://essenceia.github.io/projects/two_weeks_until_tapeout/)

生成摘要时出错

---

## 31. Postmortem: Our first VLEO satellite mission (with imagery and flight data)

**原文标题**: Postmortem: Our first VLEO satellite mission (with imagery and flight data)

**原文链接**: [https://albedo.com/post/clarity-1-what-worked-and-where-we-go-next](https://albedo.com/post/clarity-1-what-worked-and-where-we-go-next)

生成摘要时出错

---

## 32. GNU C Library 2.43 released

**原文标题**: GNU C Library 2.43 released

**原文链接**: [https://lwn.net/Articles/1055757/](https://lwn.net/Articles/1055757/)

生成摘要时出错

---

## 33. BirdyChat becomes first European chat app that is interoperable with WhatsApp

**原文标题**: BirdyChat becomes first European chat app that is interoperable with WhatsApp

**原文链接**: [https://www.birdy.chat/blog/first-to-interoperate-with-whatsapp](https://www.birdy.chat/blog/first-to-interoperate-with-whatsapp)

生成摘要时出错

---

## 34. Intrinsically stretchable 2D MoS2 transistors

**原文标题**: Intrinsically stretchable 2D MoS2 transistors

**原文链接**: [https://www.nature.com/articles/s41467-026-68504-2](https://www.nature.com/articles/s41467-026-68504-2)

生成摘要时出错

---

## 35. Show HN: AutoShorts – Local, GPU-accelerated AI video pipeline for creators

**原文标题**: Show HN: AutoShorts – Local, GPU-accelerated AI video pipeline for creators

**原文链接**: [https://github.com/divyaprakash0426/autoshorts](https://github.com/divyaprakash0426/autoshorts)

生成摘要时出错

---

## 36. Typography on Pencils (2023)

**原文标题**: Typography on Pencils (2023)

**原文链接**: [https://www.presentandcorrect.com/blogs/blog/typography-on-pencils-1-5](https://www.presentandcorrect.com/blogs/blog/typography-on-pencils-1-5)

生成摘要时出错

---

## 37. Raspberry Pi Drag Race: Pi 1 to Pi 5 – Performance Comparison

**原文标题**: Raspberry Pi Drag Race: Pi 1 to Pi 5 – Performance Comparison

**原文链接**: [https://the-diy-life.com/raspberry-pi-drag-race-pi-1-to-pi-5-performance-comparison/](https://the-diy-life.com/raspberry-pi-drag-race-pi-1-to-pi-5-performance-comparison/)

生成摘要时出错

---

## 38. We X-Rayed a Suspicious FTDI USB Cable

**原文标题**: We X-Rayed a Suspicious FTDI USB Cable

**原文链接**: [https://eclypsium.com/blog/xray-counterfeit-usb-cable/](https://eclypsium.com/blog/xray-counterfeit-usb-cable/)

生成摘要时出错

---

## 39. Article on the History of Spot Instances: Analyzing Spot Instance Pricing Change

**原文标题**: Article on the History of Spot Instances: Analyzing Spot Instance Pricing Change

**原文链接**: [https://spot.rackspace.com/blogs/history-of-spot-instances](https://spot.rackspace.com/blogs/history-of-spot-instances)

生成摘要时出错

---

## 40. Accept_language 2.2 – RFC 7231/4647 compliant Accept-Language parsing for Ruby

**原文标题**: Accept_language 2.2 – RFC 7231/4647 compliant Accept-Language parsing for Ruby

**原文链接**: [https://github.com/cyril/accept_language.rb](https://github.com/cyril/accept_language.rb)

生成摘要时出错

---

## 41. Maze Algorithms (2017)

**原文标题**: Maze Algorithms (2017)

**原文链接**: [http://www.jamisbuck.org/mazes/](http://www.jamisbuck.org/mazes/)

生成摘要时出错

---

## 42. Show HN: Sightline – Shodan-style search for real-world infra using OSM Data

**原文标题**: Show HN: Sightline – Shodan-style search for real-world infra using OSM Data

**原文链接**: [https://github.com/ni5arga/sightline](https://github.com/ni5arga/sightline)

生成摘要时出错

---

## 43. Genetic Data from over 20k U.S. Children Misused for 'Race Science'

**原文标题**: Genetic Data from over 20k U.S. Children Misused for 'Race Science'

**原文链接**: [https://www.nytimes.com/2026/01/24/us/children-genetics-race-science.html](https://www.nytimes.com/2026/01/24/us/children-genetics-race-science.html)

生成摘要时出错

---

## 44. Putting Rocks on the Moon

**原文标题**: Putting Rocks on the Moon

**原文链接**: [https://ahwoo.com/posts/019bd882-d104-7347-be7b-8e0a5ce13cb5](https://ahwoo.com/posts/019bd882-d104-7347-be7b-8e0a5ce13cb5)

生成摘要时出错

---

## 45. Memory layout in Zig with formulas

**原文标题**: Memory layout in Zig with formulas

**原文链接**: [https://raymondtana.github.io/math/programming/2026/01/23/zig-alignment-and-sizing.html](https://raymondtana.github.io/math/programming/2026/01/23/zig-alignment-and-sizing.html)

生成摘要时出错

---

## 46. Interview: Kim Stanley Robinson, Science Fiction Maestro and Utopian, in 2026

**原文标题**: Interview: Kim Stanley Robinson, Science Fiction Maestro and Utopian, in 2026

**原文链接**: [https://sammatey.substack.com/p/interview-kim-stanley-robinson-science-111](https://sammatey.substack.com/p/interview-kim-stanley-robinson-science-111)

生成摘要时出错

---

## 47. Wall Street braced for a private credit meltdown. The risk of one is rising

**原文标题**: Wall Street braced for a private credit meltdown. The risk of one is rising

**原文链接**: [https://www.cnbc.com/2026/01/23/wall-street-private-credit-risk-rising.html](https://www.cnbc.com/2026/01/23/wall-street-private-credit-risk-rising.html)

生成摘要时出错

---

## 48. Shared Claude: A website controlled by the public

**原文标题**: Shared Claude: A website controlled by the public

**原文链接**: [https://sharedclaude.com/](https://sharedclaude.com/)

生成摘要时出错

---

## 49. Small Kafka: Tansu and SQLite on a free t3.micro

**原文标题**: Small Kafka: Tansu and SQLite on a free t3.micro

**原文链接**: [https://blog.tansu.io/articles/broker-aws-free-tier](https://blog.tansu.io/articles/broker-aws-free-tier)

生成摘要时出错

---

## 50. Understanding Rust Closures

**原文标题**: Understanding Rust Closures

**原文链接**: [https://antoine.vandecreme.net/blog/rust-closures/](https://antoine.vandecreme.net/blog/rust-closures/)

生成摘要时出错

---

## 51. Show HN: C From Scratch – Learn safety-critical C with prove-first methodology

**原文标题**: Show HN: C From Scratch – Learn safety-critical C with prove-first methodology

**原文链接**: [https://github.com/SpeyTech/c-from-scratch](https://github.com/SpeyTech/c-from-scratch)

生成摘要时出错

---

## 52. 'Amelia': the AI-generated British schoolgirl, a far-right social media star

**原文标题**: 'Amelia': the AI-generated British schoolgirl, a far-right social media star

**原文链接**: [https://www.theguardian.com/politics/2026/jan/25/ai-generated-british-schoolgirl-becomes-far-right-social-media-meme](https://www.theguardian.com/politics/2026/jan/25/ai-generated-british-schoolgirl-becomes-far-right-social-media-meme)

生成摘要时出错

---

## 53. Agent orchestration for the timid

**原文标题**: Agent orchestration for the timid

**原文链接**: [https://substack.com/inbox/post/185649875](https://substack.com/inbox/post/185649875)

生成摘要时出错

---

## 54. 波兰电网遭到前所未见的擦除恶意软件攻击。

**原文标题**: Poland's energy grid was targeted by never-before-seen wiper malware

**原文链接**: [https://arstechnica.com/security/2026/01/wiper-malware-targeted-poland-energy-grid-but-failed-to-knock-out-electricity/](https://arstechnica.com/security/2026/01/wiper-malware-targeted-poland-energy-grid-but-failed-to-knock-out-electricity/)

生成摘要时出错

---

## 55. China Fertility Facts of the Day

**原文标题**: China Fertility Facts of the Day

**原文链接**: [https://marginalrevolution.com/marginalrevolution/2025/12/china-fertility-facts-of-the-day.html](https://marginalrevolution.com/marginalrevolution/2025/12/china-fertility-facts-of-the-day.html)

生成摘要时出错

---

## 56. Claude Code's new hidden feature: Swarms

**原文标题**: Claude Code's new hidden feature: Swarms

**原文链接**: [https://twitter.com/NicerInPerson/status/2014989679796347375](https://twitter.com/NicerInPerson/status/2014989679796347375)

生成摘要时出错

---

## 57. UN Declares That the World Has Entered an Era of 'Global Water Bankruptcy'

**原文标题**: UN Declares That the World Has Entered an Era of 'Global Water Bankruptcy'

**原文链接**: [https://www.smithsonianmag.com/smart-news/united-nations-declares-that-the-world-has-entered-an-era-of-global-water-bankruptcy-180988045/](https://www.smithsonianmag.com/smart-news/united-nations-declares-that-the-world-has-entered-an-era-of-global-water-bankruptcy-180988045/)

生成摘要时出错

---

## 58. Nvidia-smi hangs indefinitely after ~66 days

**原文标题**: Nvidia-smi hangs indefinitely after ~66 days

**原文链接**: [https://github.com/NVIDIA/open-gpu-kernel-modules/issues/971](https://github.com/NVIDIA/open-gpu-kernel-modules/issues/971)

生成摘要时出错

---

## 59. Doing gigabit Ethernet over my British phone wires

**原文标题**: Doing gigabit Ethernet over my British phone wires

**原文链接**: [https://thehftguy.com/2026/01/22/doing-gigabit-ethernet-over-my-british-phone-wires/](https://thehftguy.com/2026/01/22/doing-gigabit-ethernet-over-my-british-phone-wires/)

生成摘要时出错

---

## 60. I added a Bluesky comment section to my blog

**原文标题**: I added a Bluesky comment section to my blog

**原文链接**: [https://micahcantor.com/blog/bluesky-comment-section.html](https://micahcantor.com/blog/bluesky-comment-section.html)

生成摘要时出错

---

## 61. Many Small Queries Are Efficient in SQLite

**原文标题**: Many Small Queries Are Efficient in SQLite

**原文链接**: [https://www.sqlite.org/np1queryprob.html](https://www.sqlite.org/np1queryprob.html)

生成摘要时出错

---

## 62. “Let people help” – Advice that made a big difference to a grieving widow

**原文标题**: “Let people help” – Advice that made a big difference to a grieving widow

**原文链接**: [https://www.npr.org/2026/01/20/nx-s1-5683170/let-them-the-small-bit-of-advice-that-made-a-big-difference-to-a-grieving-widow](https://www.npr.org/2026/01/20/nx-s1-5683170/let-them-the-small-bit-of-advice-that-made-a-big-difference-to-a-grieving-widow)

生成摘要时出错

---

## 63. How I estimate work

**原文标题**: How I estimate work

**原文链接**: [https://www.seangoedecke.com/how-i-estimate-work/](https://www.seangoedecke.com/how-i-estimate-work/)

生成摘要时出错

---

## 64. I Like GitLab

**原文标题**: I Like GitLab

**原文链接**: [https://www.whileforloop.com/en/blog/2026/01/21/i-like-gitlab/](https://www.whileforloop.com/en/blog/2026/01/21/i-like-gitlab/)

生成摘要时出错

---

## 65. The Temporal Consistency Challenge in Video Restoration

**原文标题**: The Temporal Consistency Challenge in Video Restoration

**原文链接**: [https://blog.videowatermarkremove.com/the-temporal-consistency-challenge-from-optical-flow-to-spatiotemporal-ai-in-video-restoration](https://blog.videowatermarkremove.com/the-temporal-consistency-challenge-from-optical-flow-to-spatiotemporal-ai-in-video-restoration)

生成摘要时出错

---

## 66. Second Win11 emergency out of band update to address disastrous Patch Tuesday

**原文标题**: Second Win11 emergency out of band update to address disastrous Patch Tuesday

**原文链接**: [https://www.windowscentral.com/microsoft/windows-11/windows-11-second-emergency-out-of-band-update-kb5078127-released-address-outlook-bugs](https://www.windowscentral.com/microsoft/windows-11/windows-11-second-emergency-out-of-band-update-kb5078127-released-address-outlook-bugs)

生成摘要时出错

---

## 67. Show HN: Open-source Figma design to code

**原文标题**: Show HN: Open-source Figma design to code

**原文链接**: [https://github.com/vibeflowing-inc/vibe_figma](https://github.com/vibeflowing-inc/vibe_figma)

生成摘要时出错

---

## 68. Extracting verified C++ from the Rocq theorem prover at Bloomberg

**原文标题**: Extracting verified C++ from the Rocq theorem prover at Bloomberg

**原文链接**: [https://bloomberg.github.io/crane/](https://bloomberg.github.io/crane/)

生成摘要时出错

---

## 69. Show HN: StormWatch – Weather emergency dashboard with prep checklists

**原文标题**: Show HN: StormWatch – Weather emergency dashboard with prep checklists

**原文链接**: [https://jeisey.github.io/stormwatch/](https://jeisey.github.io/stormwatch/)

生成摘要时出错

---

## 70. 80386 Multiplication and Division

**原文标题**: 80386 Multiplication and Division

**原文链接**: [https://nand2mario.github.io/posts/2026/80386_multiplication_and_division/](https://nand2mario.github.io/posts/2026/80386_multiplication_and_division/)

生成摘要时出错

---

## 71. High-bandwidth flash progress and future

**原文标题**: High-bandwidth flash progress and future

**原文链接**: [https://blocksandfiles.com/2026/01/19/a-window-into-hbf-progress/](https://blocksandfiles.com/2026/01/19/a-window-into-hbf-progress/)

生成摘要时出错

---

## 72. Draig, a Welsh Programming Language

**原文标题**: Draig, a Welsh Programming Language

**原文链接**: [https://raku.land/zef:l10n/L10N::CY](https://raku.land/zef:l10n/L10N::CY)

生成摘要时出错

---

## 73. Show HN: VM-curator – a TUI alternative to libvirt and virt-manager

**原文标题**: Show HN: VM-curator – a TUI alternative to libvirt and virt-manager

**原文链接**: [https://github.com/mroboff/vm-curator](https://github.com/mroboff/vm-curator)

生成摘要时出错

---

## 74. Volvo EX60 Targets 400-Mile Range and Coffee-Stop Charging

**原文标题**: Volvo EX60 Targets 400-Mile Range and Coffee-Stop Charging

**原文链接**: [https://www.thedrive.com/news/volvo-ex60-targetes-400-mile-range-and-coffee-stop-charging](https://www.thedrive.com/news/volvo-ex60-targetes-400-mile-range-and-coffee-stop-charging)

生成摘要时出错

---

## 75. KAOS – The Kubernetes Agent Orchestration System

**原文标题**: KAOS – The Kubernetes Agent Orchestration System

**原文链接**: [https://github.com/axsaucedo/kaos](https://github.com/axsaucedo/kaos)

生成摘要时出错

---

## 76. The Kept and the Killed (2022)

**原文标题**: The Kept and the Killed (2022)

**原文链接**: [https://publicdomainreview.org/essay/the-kept-and-the-killed/](https://publicdomainreview.org/essay/the-kept-and-the-killed/)

生成摘要时出错

---

## 77. When employees feel slighted, they work less

**原文标题**: When employees feel slighted, they work less

**原文链接**: [https://penntoday.upenn.edu/news/penn-wharton-when-employees-feel-slighted-they-work-less](https://penntoday.upenn.edu/news/penn-wharton-when-employees-feel-slighted-they-work-less)

生成摘要时出错

---

## 78. JSON-render: LLM-based JSON-to-UI tool

**原文标题**: JSON-render: LLM-based JSON-to-UI tool

**原文链接**: [https://json-render.dev/](https://json-render.dev/)

生成摘要时出错

---

## 79. Tao Te Ching – Translated by Ursula K. Le Guin

**原文标题**: Tao Te Ching – Translated by Ursula K. Le Guin

**原文链接**: [https://github.com/nrrb/tao-te-ching/blob/master/Ursula%20K%20Le%20Guin.md](https://github.com/nrrb/tao-te-ching/blob/master/Ursula%20K%20Le%20Guin.md)

生成摘要时出错

---

## 80. The future of work when work is meaningless

**原文标题**: The future of work when work is meaningless

**原文链接**: [https://letters.thedankoe.com/p/the-future-of-work-when-work-is-meaningless](https://letters.thedankoe.com/p/the-future-of-work-when-work-is-meaningless)

生成摘要时出错

---

## 81. We are building a new browser from scratch, backed by a non-profit

**原文标题**: We are building a new browser from scratch, backed by a non-profit

**原文链接**: [https://ladybird.org/](https://ladybird.org/)

生成摘要时出错

---

## 82. Vortex Support in DuckDB

**原文标题**: Vortex Support in DuckDB

**原文链接**: [https://duckdb.org/2026/01/23/duckdb-vortex-extension](https://duckdb.org/2026/01/23/duckdb-vortex-extension)

生成摘要时出错

---

## 83. Adviser of Highest EU Court Backs VPN Neutrality in Anne Frank Copyright Battle

**原文标题**: Adviser of Highest EU Court Backs VPN Neutrality in Anne Frank Copyright Battle

**原文链接**: [https://torrentfreak.com/adviser-of-eus-highest-court-backs-vpn-neutrality-in-anne-frank-copyright-battle/](https://torrentfreak.com/adviser-of-eus-highest-court-backs-vpn-neutrality-in-anne-frank-copyright-battle/)

生成摘要时出错

---

## 84. The Concatative Language XY

**原文标题**: The Concatative Language XY

**原文链接**: [http://www.nsl.com/k/xy/xy.txt](http://www.nsl.com/k/xy/xy.txt)

生成摘要时出错

---

## 85. Alex Honnold completes Taipei 101 skyscraper climb without ropes or safety net

**原文标题**: Alex Honnold completes Taipei 101 skyscraper climb without ropes or safety net

**原文链接**: [https://www.cnn.com/sport/live-news/taiwan-alex-honnold-climb-taipei-101-01-25-26-intl-hnk](https://www.cnn.com/sport/live-news/taiwan-alex-honnold-climb-taipei-101-01-25-26-intl-hnk)

生成摘要时出错

---

## 86. Europe wants to end its dangerous reliance on US internet technology

**原文标题**: Europe wants to end its dangerous reliance on US internet technology

**原文链接**: [https://theconversation.com/europe-wants-to-end-its-dangerous-reliance-on-us-internet-technology-274042](https://theconversation.com/europe-wants-to-end-its-dangerous-reliance-on-us-internet-technology-274042)

生成摘要时出错

---

## 87. Unrolling the Codex agent loop

**原文标题**: Unrolling the Codex agent loop

**原文链接**: [https://openai.com/index/unrolling-the-codex-agent-loop/](https://openai.com/index/unrolling-the-codex-agent-loop/)

生成摘要时出错

---

## 88. ollama launch

**原文标题**: ollama launch

**原文链接**: [https://ollama.com/blog/launch](https://ollama.com/blog/launch)

生成摘要时出错

---

## 89. Bye Bye Gmail

**原文标题**: Bye Bye Gmail

**原文链接**: [https://m24tom.com/bye-bye-gmail/show](https://m24tom.com/bye-bye-gmail/show)

生成摘要时出错

---

## 90. JVIC: New web-based Commodore VIC 20 emulator

**原文标题**: JVIC: New web-based Commodore VIC 20 emulator

**原文链接**: [https://vic20.games/#/basic/24k](https://vic20.games/#/basic/24k)

生成摘要时出错

---

## 91. Bugs Apple loves

**原文标题**: Bugs Apple loves

**原文链接**: [https://www.bugsappleloves.com](https://www.bugsappleloves.com)

生成摘要时出错

---

## 92. December in Servo: multiple windows, proxy support, better caching, and more

**原文标题**: December in Servo: multiple windows, proxy support, better caching, and more

**原文链接**: [https://servo.org/blog/2026/01/23/december-in-servo/](https://servo.org/blog/2026/01/23/december-in-servo/)

生成摘要时出错

---

## 93. Proof of Corn

**原文标题**: Proof of Corn

**原文链接**: [https://proofofcorn.com/](https://proofofcorn.com/)

生成摘要时出错

---

## 94. Show HN: Semantic search engine for Studio Ghibli movie

**原文标题**: Show HN: Semantic search engine for Studio Ghibli movie

**原文链接**: [https://ghibli-search.anini.workers.dev/](https://ghibli-search.anini.workers.dev/)

生成摘要时出错

---

## 95. Internet Archive's Storage

**原文标题**: Internet Archive's Storage

**原文链接**: [https://blog.dshr.org/2026/01/internet-archives-storage.html](https://blog.dshr.org/2026/01/internet-archives-storage.html)

生成摘要时出错

---

## 96. Incident updates, interruptions and the 30 minute window

**原文标题**: Incident updates, interruptions and the 30 minute window

**原文链接**: [https://www.unixdaemon.net/sysadmin/incident-updates-and-interruptions/](https://www.unixdaemon.net/sysadmin/incident-updates-and-interruptions/)

生成摘要时出错

---

## 97. Emulator2000 – Seiko Digital Watch Emulator

**原文标题**: Emulator2000 – Seiko Digital Watch Emulator

**原文链接**: [https://github.com/azya52/Emulator2000](https://github.com/azya52/Emulator2000)

生成摘要时出错

---

## 98. Comma openpilot – Open source driver-assistance

**原文标题**: Comma openpilot – Open source driver-assistance

**原文链接**: [https://comma.ai](https://comma.ai)

生成摘要时出错

---

## 99. Anthropic Economic Index report: economic primitives

**原文标题**: Anthropic Economic Index report: economic primitives

**原文链接**: [https://www.anthropic.com/research/anthropic-economic-index-january-2026-report](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)

生成摘要时出错

---

## 100. Updates to our web search products and  Programmable Search Engine capabilities

**原文标题**: Updates to our web search products and  Programmable Search Engine capabilities

**原文链接**: [https://programmablesearchengine.googleblog.com/2026/01/updates-to-our-web-search-products.html](https://programmablesearchengine.googleblog.com/2026/01/updates-to-our-web-search-products.html)

生成摘要时出错

---

