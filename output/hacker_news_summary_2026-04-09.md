# Hacker News 热门文章摘要 (2026-04-09)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. AI, Unemployment and Work

**原文标题**: AI, Unemployment and Work

**原文链接**: [https://marginalrevolution.com/marginalrevolution/2026/04/ai-unemployment-and-work.html](https://marginalrevolution.com/marginalrevolution/2026/04/ai-unemployment-and-work.html)

生成摘要时出错

---

## 12. Muse Spark: Scaling towards personal superintelligence

**原文标题**: Muse Spark: Scaling towards personal superintelligence

**原文链接**: [https://ai.meta.com/blog/introducing-muse-spark-msl/?_fb_noscript=1](https://ai.meta.com/blog/introducing-muse-spark-msl/?_fb_noscript=1)

生成摘要时出错

---

## 13. I imported the full Linux kernel git history into pgit

**原文标题**: I imported the full Linux kernel git history into pgit

**原文链接**: [https://oseifert.ch/blog/linux-kernel-pgit](https://oseifert.ch/blog/linux-kernel-pgit)

生成摘要时出错

---

## 14. Six (and a half) intuitions for KL divergence

**原文标题**: Six (and a half) intuitions for KL divergence

**原文链接**: [https://www.perfectlynormal.co.uk/blog-kl-divergence](https://www.perfectlynormal.co.uk/blog-kl-divergence)

生成摘要时出错

---

## 15. Show HN: Guruka.com – free guided mediations. No signup, private, works offline

**原文标题**: Show HN: Guruka.com – free guided mediations. No signup, private, works offline

**原文链接**: [https://guruka.com/](https://guruka.com/)

生成摘要时出错

---

## 16. Desalination Technology, by the Numbers

**原文标题**: Desalination Technology, by the Numbers

**原文链接**: [https://www.technologyreview.com/2026/04/09/1135495/desalination-technology-numbers/](https://www.technologyreview.com/2026/04/09/1135495/desalination-technology-numbers/)

生成摘要时出错

---

## 17. What does it mean to “write like you talk”?

**原文标题**: What does it mean to “write like you talk”?

**原文链接**: [https://arjunpanickssery.substack.com/p/what-does-it-mean-to-write-like-you](https://arjunpanickssery.substack.com/p/what-does-it-mean-to-write-like-you)

生成摘要时出错

---

## 18. FBI Extracted Deleted Signal Messages Saved in iPhone Notification Database

**原文标题**: FBI Extracted Deleted Signal Messages Saved in iPhone Notification Database

**原文链接**: [https://www.404media.co/fbi-extracts-suspects-deleted-signal-messages-saved-in-iphone-notification-database-2/](https://www.404media.co/fbi-extracts-suspects-deleted-signal-messages-saved-in-iphone-notification-database-2/)

生成摘要时出错

---

## 19. Understanding Traceroute

**原文标题**: Understanding Traceroute

**原文链接**: [https://tech.stonecharioteer.com/posts/2026/traceroute/](https://tech.stonecharioteer.com/posts/2026/traceroute/)

生成摘要时出错

---

## 20. Expanding Swift's IDE Support

**原文标题**: Expanding Swift's IDE Support

**原文链接**: [https://swift.org/blog/expanding-swift-ide-support/](https://swift.org/blog/expanding-swift-ide-support/)

生成摘要时出错

---

## 21. Teardown of unreleased LG Rollable shows why rollable phones aren't a thing

**原文标题**: Teardown of unreleased LG Rollable shows why rollable phones aren't a thing

**原文链接**: [https://arstechnica.com/gadgets/2026/04/teardown-of-unreleased-lg-rollable-shows-why-rollable-phones-arent-a-thing/](https://arstechnica.com/gadgets/2026/04/teardown-of-unreleased-lg-rollable-shows-why-rollable-phones-arent-a-thing/)

生成摘要时出错

---

## 22. They're made out of meat (1991)

**原文标题**: They're made out of meat (1991)

**原文链接**: [http://www.terrybisson.com/theyre-made-out-of-meat-2/](http://www.terrybisson.com/theyre-made-out-of-meat-2/)

生成摘要时出错

---

## 23. Union types in C# 15

**原文标题**: Union types in C# 15

**原文链接**: [https://devblogs.microsoft.com/dotnet/csharp-15-union-types/](https://devblogs.microsoft.com/dotnet/csharp-15-union-types/)

生成摘要时出错

---

## 24. Who is Satoshi Nakamoto? My quest to unmask Bitcoin's creator

**原文标题**: Who is Satoshi Nakamoto? My quest to unmask Bitcoin's creator

**原文链接**: [https://www.nytimes.com/2026/04/08/business/bitcoin-satoshi-nakamoto-identity-adam-back.html](https://www.nytimes.com/2026/04/08/business/bitcoin-satoshi-nakamoto-identity-adam-back.html)

生成摘要时出错

---

## 25. Today Is CSS Naked Day

**原文标题**: Today Is CSS Naked Day

**原文链接**: [https://css-naked-day.org/?](https://css-naked-day.org/?)

生成摘要时出错

---

## 26. Map Gesture Controls - Control maps with your hands

**原文标题**: Map Gesture Controls - Control maps with your hands

**原文链接**: [https://sanderdesnaijer.github.io/map-gesture-controls/](https://sanderdesnaijer.github.io/map-gesture-controls/)

生成摘要时出错

---

## 27. John Deere to pay $99M in right-to-repair settlement

**原文标题**: John Deere to pay $99M in right-to-repair settlement

**原文链接**: [https://www.thedrive.com/news/john-deere-to-pay-99-million-in-monumental-right-to-repair-settlement](https://www.thedrive.com/news/john-deere-to-pay-99-million-in-monumental-right-to-repair-settlement)

生成摘要时出错

---

## 28. US cities are axing Flock Safety surveillance technology

**原文标题**: US cities are axing Flock Safety surveillance technology

**原文链接**: [https://www.cnet.com/home/security/when-flock-comes-to-town-why-cities-are-axing-the-controversial-surveillance-technology/](https://www.cnet.com/home/security/when-flock-comes-to-town-why-cities-are-axing-the-controversial-surveillance-technology/)

生成摘要时出错

---

## 29. Sam Altman may control our future – can he be trusted?

**原文标题**: Sam Altman may control our future – can he be trusted?

**原文链接**: [https://www.newyorker.com/magazine/2026/04/13/sam-altman-may-control-our-future-can-he-be-trusted](https://www.newyorker.com/magazine/2026/04/13/sam-altman-may-control-our-future-can-he-be-trusted)

生成摘要时出错

---

## 30. Show HN: A (marginally) useful x86-64 ELF executable in 301 bytes

**原文标题**: Show HN: A (marginally) useful x86-64 ELF executable in 301 bytes

**原文链接**: [https://github.com/meribold/btry](https://github.com/meribold/btry)

生成摘要时出错

---

## 31. Veracrypt project update

**原文标题**: Veracrypt project update

**原文链接**: [https://sourceforge.net/p/veracrypt/discussion/general/thread/9620d7a4b3/](https://sourceforge.net/p/veracrypt/discussion/general/thread/9620d7a4b3/)

生成摘要时出错

---

## 32. Škoda DuoBell: A bicycle bell that penetrates noise-cancelling headphones

**原文标题**: Škoda DuoBell: A bicycle bell that penetrates noise-cancelling headphones

**原文链接**: [https://www.skoda-storyboard.com/en/skoda-world/skoda-duobell-a-bicycle-bell-that-outsmarts-even-smart-headphones/](https://www.skoda-storyboard.com/en/skoda-world/skoda-duobell-a-bicycle-bell-that-outsmarts-even-smart-headphones/)

生成摘要时出错

---

## 33. I've been waiting over a month for Anthropic to respond to my billing issue

**原文标题**: I've been waiting over a month for Anthropic to respond to my billing issue

**原文链接**: [https://nickvecchioni.github.io/thoughts/2026/04/08/anthropic-support-doesnt-exist/](https://nickvecchioni.github.io/thoughts/2026/04/08/anthropic-support-doesnt-exist/)

生成摘要时出错

---

## 34. Microsoft terminates VeraCrypt account, halting Windows updates

**原文标题**: Microsoft terminates VeraCrypt account, halting Windows updates

**原文链接**: [https://www.404media.co/microsoft-abruptly-terminates-veracrypt-account-halting-windows-updates/](https://www.404media.co/microsoft-abruptly-terminates-veracrypt-account-halting-windows-updates/)

生成摘要时出错

---

## 35. The Moon is on Google Maps–did Artemis II tell us anything new?

**原文标题**: The Moon is on Google Maps–did Artemis II tell us anything new?

**原文链接**: [https://arstechnica.com/space/2026/04/the-moon-is-already-on-google-maps-did-artemis-ii-really-tell-us-anything-new/](https://arstechnica.com/space/2026/04/the-moon-is-already-on-google-maps-did-artemis-ii-really-tell-us-anything-new/)

生成摘要时出错

---

## 36. Project Glasswing: Securing critical software for the AI era

**原文标题**: Project Glasswing: Securing critical software for the AI era

**原文链接**: [https://www.anthropic.com/glasswing](https://www.anthropic.com/glasswing)

生成摘要时出错

---

## 37. Your File System Is Already A Graph Database

**原文标题**: Your File System Is Already A Graph Database

**原文链接**: [https://rumproarious.com/2026/04/04/your-file-system-is-already-a-graph-database/](https://rumproarious.com/2026/04/04/your-file-system-is-already-a-graph-database/)

生成摘要时出错

---

## 38. Show HN: Orange Juice – Small UX improvements that make HN easier to read

**原文标题**: Show HN: Orange Juice – Small UX improvements that make HN easier to read

**原文链接**: [http://oj-hn.com/](http://oj-hn.com/)

生成摘要时出错

---

## 39. Binary obfuscation that doesn't kill LTO

**原文标题**: Binary obfuscation that doesn't kill LTO

**原文链接**: [https://blog.farzon.org/2026/04/binary-obfuscation-that-doesnt-kill-lto.html](https://blog.farzon.org/2026/04/binary-obfuscation-that-doesnt-kill-lto.html)

生成摘要时出错

---

## 40. Show HN: Is Hormuz open yet?

**原文标题**: Show HN: Is Hormuz open yet?

**原文链接**: [https://www.ishormuzopenyet.com/](https://www.ishormuzopenyet.com/)

生成摘要时出错

---

## 41. Lunar Flyby

**原文标题**: Lunar Flyby

**原文链接**: [https://www.nasa.gov/gallery/lunar-flyby/](https://www.nasa.gov/gallery/lunar-flyby/)

生成摘要时出错

---

## 42. MegaTrain: Full Precision Training of 100B+ Parameter LLMs on a Single GPU

**原文标题**: MegaTrain: Full Precision Training of 100B+ Parameter LLMs on a Single GPU

**原文链接**: [https://arxiv.org/abs/2604.05091](https://arxiv.org/abs/2604.05091)

生成摘要时出错

---

## 43. Slightly safer vibecoding by adopting old hacker habits

**原文标题**: Slightly safer vibecoding by adopting old hacker habits

**原文链接**: [http://addxorrol.blogspot.com/2026/03/slightly-safer-vibecoding-by-adopting.html](http://addxorrol.blogspot.com/2026/03/slightly-safer-vibecoding-by-adopting.html)

生成摘要时出错

---

## 44. 9 Mothers (YC P26) Is Hiring – Lead Robotics and More

**原文标题**: 9 Mothers (YC P26) Is Hiring – Lead Robotics and More

**原文链接**: [https://jobs.ashbyhq.com/9-mothers?utm_source=x8pZ4B3P3Q](https://jobs.ashbyhq.com/9-mothers?utm_source=x8pZ4B3P3Q)

生成摘要时出错

---

## 45. A Visual Guide to Gemma 4

**原文标题**: A Visual Guide to Gemma 4

**原文链接**: [https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-gemma-4](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-gemma-4)

生成摘要时出错

---

## 46. CDC delays publishing report showing Covid vaccine benefits

**原文标题**: CDC delays publishing report showing Covid vaccine benefits

**原文链接**: [https://www.washingtonpost.com/health/2026/04/09/covid-vaccine-report-delayed/](https://www.washingtonpost.com/health/2026/04/09/covid-vaccine-report-delayed/)

生成摘要时出错

---

## 47. Native Americans had dice 12k years ago

**原文标题**: Native Americans had dice 12k years ago

**原文链接**: [https://www.nbcnews.com/science/science-news/native-americans-dice-games-probability-study-rcna266426](https://www.nbcnews.com/science/science-news/native-americans-dice-games-probability-study-rcna266426)

生成摘要时出错

---

## 48. Show HN: Unicode Steganography

**原文标题**: Show HN: Unicode Steganography

**原文链接**: [https://steganography.patrickvuscan.com](https://steganography.patrickvuscan.com)

生成摘要时出错

---

## 49. You Can Just Print an Air Purifier

**原文标题**: You Can Just Print an Air Purifier

**原文链接**: [https://aftermath.site/3d-printing-air-purifier-corsi-rosenthal/](https://aftermath.site/3d-printing-air-purifier-corsi-rosenthal/)

生成摘要时出错

---

## 50. OpenAI pulls out of landmark £31B UK investment package

**原文标题**: OpenAI pulls out of landmark £31B UK investment package

**原文链接**: [https://www.theguardian.com/technology/2026/apr/09/openai-pulls-out-of-landmark-31bn-uk-investment](https://www.theguardian.com/technology/2026/apr/09/openai-pulls-out-of-landmark-31bn-uk-investment)

生成摘要时出错

---

## 51. Amazon Is Pulling Support for Kindles from 2012 or Earlier

**原文标题**: Amazon Is Pulling Support for Kindles from 2012 or Earlier

**原文链接**: [https://www.cnet.com/tech/computing/amazon-pulls-the-plug-on-older-kindle-models/](https://www.cnet.com/tech/computing/amazon-pulls-the-plug-on-older-kindle-models/)

生成摘要时出错

---

## 52. Show HN: Go-Bt: Minimalist Behavior Trees for Go

**原文标题**: Show HN: Go-Bt: Minimalist Behavior Trees for Go

**原文链接**: [https://github.com/rvitorper/go-bt](https://github.com/rvitorper/go-bt)

生成摘要时出错

---

## 53. Encrypted Client Hello: How it was blocked in Russia and next steps

**原文标题**: Encrypted Client Hello: How it was blocked in Russia and next steps

**原文链接**: [https://cdt.org/insights/do-not-stick-out-the-dynamics-of-the-ech-rollout/](https://cdt.org/insights/do-not-stick-out-the-dynamics-of-the-ech-rollout/)

生成摘要时出错

---

## 54. White-Collar Workers Are Rebelling Against AI – 80% Refuse Adoption Mandates

**原文标题**: White-Collar Workers Are Rebelling Against AI – 80% Refuse Adoption Mandates

**原文链接**: [https://fortune.com/2026/04/09/ai-backlash-quiet-quitting-fobo-obsolete-white-collar-rebellion/](https://fortune.com/2026/04/09/ai-backlash-quiet-quitting-fobo-obsolete-white-collar-rebellion/)

生成摘要时出错

---

## 55. We moved Railway's frontend off Next.js. Builds went from 10+ mins to under 2

**原文标题**: We moved Railway's frontend off Next.js. Builds went from 10+ mins to under 2

**原文链接**: [https://blog.railway.com/p/moving-railways-frontend-off-nextjs](https://blog.railway.com/p/moving-railways-frontend-off-nextjs)

生成摘要时出错

---

## 56. Claude Managed Agents Overview

**原文标题**: Claude Managed Agents Overview

**原文链接**: [https://platform.claude.com/docs/en/managed-agents/overview](https://platform.claude.com/docs/en/managed-agents/overview)

生成摘要时出错

---

## 57. Show HN: I pipe free sports streams into Jellyfin – no ads, just HLS

**原文标题**: Show HN: I pipe free sports streams into Jellyfin – no ads, just HLS

**原文链接**: [https://github.com/pcruz1905/hls-restream-proxy](https://github.com/pcruz1905/hls-restream-proxy)

生成摘要时出错

---

## 58. Virtual Mars Traverse: Every inch of Curiosity rover's path since 2012 landing

**原文标题**: Virtual Mars Traverse: Every inch of Curiosity rover's path since 2012 landing

**原文链接**: [https://www.rovers.land/](https://www.rovers.land/)

生成摘要时出错

---

## 59. Show HN: TUI-use: Let AI agents control interactive terminal programs

**原文标题**: Show HN: TUI-use: Let AI agents control interactive terminal programs

**原文链接**: [https://github.com/onesuper/tui-use](https://github.com/onesuper/tui-use)

生成摘要时出错

---

## 60. A database of analog cameras that can be 3D printed

**原文标题**: A database of analog cameras that can be 3D printed

**原文链接**: [https://printed.analogcamera.space/](https://printed.analogcamera.space/)

生成摘要时出错

---

## 61. Study found that young adults have grown less hopeful and more angry about AI

**原文标题**: Study found that young adults have grown less hopeful and more angry about AI

**原文链接**: [https://www.nytimes.com/2026/04/09/style/gen-z-ai-gallup-study.html](https://www.nytimes.com/2026/04/09/style/gen-z-ai-gallup-study.html)

生成摘要时出错

---

## 62. Show HN: Skrun – Deploy any agent skill as an API

**原文标题**: Show HN: Skrun – Deploy any agent skill as an API

**原文链接**: [https://github.com/skrun-dev/skrun](https://github.com/skrun-dev/skrun)

生成摘要时出错

---

## 63. Show HN: We built a camera only robot vacuum for less than 300$ (Well almost)

**原文标题**: Show HN: We built a camera only robot vacuum for less than 300$ (Well almost)

**原文链接**: [https://indraneelpatil.github.io/blog/2026/robot-vacuum/](https://indraneelpatil.github.io/blog/2026/robot-vacuum/)

生成摘要时出错

---

## 64. Exposing and Understanding Scrolling Transfer Functions (2012) [pdf]

**原文标题**: Exposing and Understanding Scrolling Transfer Functions (2012) [pdf]

**原文链接**: [https://direction.bordeaux.inria.fr/~roussel/publications/2012-UIST-scrolling-tf.pdf](https://direction.bordeaux.inria.fr/~roussel/publications/2012-UIST-scrolling-tf.pdf)

生成摘要时出错

---

## 65. Show HN: I built a navigation app that displays weather along the route

**原文标题**: Show HN: I built a navigation app that displays weather along the route

**原文链接**: [https://navimodo.com/](https://navimodo.com/)

生成摘要时出错

---

## 66. Apple signs meaningless deal to make some less-important parts in America

**原文标题**: Apple signs meaningless deal to make some less-important parts in America

**原文链接**: [https://www.theregister.com/2026/03/26/apple_expands_list_of_bits/](https://www.theregister.com/2026/03/26/apple_expands_list_of_bits/)

生成摘要时出错

---

## 67. Revision Demoparty 2026: Razor1911 [video]

**原文标题**: Revision Demoparty 2026: Razor1911 [video]

**原文链接**: [https://www.youtube.com/watch?v=Lw4W9V57SKs&t=5716s](https://www.youtube.com/watch?v=Lw4W9V57SKs&t=5716s)

生成摘要时出错

---

## 68. Liquid or solid? Oobleck droplets are both

**原文标题**: Liquid or solid? Oobleck droplets are both

**原文链接**: [https://www.nature.com/articles/d41586-026-01109-3](https://www.nature.com/articles/d41586-026-01109-3)

生成摘要时出错

---

## 69. Formal Verification in Any Language for Everybody (lean 4)

**原文标题**: Formal Verification in Any Language for Everybody (lean 4)

**原文链接**: [https://www.dev-log.me/formal_verification_in_any_language_for_everybody/](https://www.dev-log.me/formal_verification_in_any_language_for_everybody/)

生成摘要时出错

---

## 70. Betterbird. Simply Better

**原文标题**: Betterbird. Simply Better

**原文链接**: [https://www.betterbird.eu](https://www.betterbird.eu)

生成摘要时出错

---

## 71. US and Iran agree to provisional ceasefire

**原文标题**: US and Iran agree to provisional ceasefire

**原文链接**: [https://www.theguardian.com/us-news/2026/apr/07/trump-iran-war-ceasefire](https://www.theguardian.com/us-news/2026/apr/07/trump-iran-war-ceasefire)

生成摘要时出错

---

## 72. Code Is Cheap Now, and That Changes Everything

**原文标题**: Code Is Cheap Now, and That Changes Everything

**原文链接**: [https://perevillega.com/posts/2026-03-16-code-is-cheap-now/](https://perevillega.com/posts/2026-03-16-code-is-cheap-now/)

生成摘要时出错

---

## 73. System Card: Claude Mythos Preview [pdf]

**原文标题**: System Card: Claude Mythos Preview [pdf]

**原文链接**: [https://www-cdn.anthropic.com/53566bf5440a10affd749724787c8913a2ae0841.pdf](https://www-cdn.anthropic.com/53566bf5440a10affd749724787c8913a2ae0841.pdf)

生成摘要时出错

---

## 74. Has electricity decoupled from natural gas prices in Germany?

**原文标题**: Has electricity decoupled from natural gas prices in Germany?

**原文链接**: [https://has-electricity-decoupled-yet.strommarktberatung.de](https://has-electricity-decoupled-yet.strommarktberatung.de)

生成摘要时出错

---

## 75. Hackers exploiting Acrobat Reader zero-day flaw since December

**原文标题**: Hackers exploiting Acrobat Reader zero-day flaw since December

**原文链接**: [https://www.bleepingcomputer.com/news/security/hackers-exploiting-acrobat-reader-zero-day-flaw-since-december/](https://www.bleepingcomputer.com/news/security/hackers-exploiting-acrobat-reader-zero-day-flaw-since-december/)

生成摘要时出错

---

## 76. Xilem – An experimental Rust native UI framework

**原文标题**: Xilem – An experimental Rust native UI framework

**原文链接**: [https://github.com/linebender/xilem](https://github.com/linebender/xilem)

生成摘要时出错

---

## 77. Audio Reactive LED Strips Are Diabolically Hard

**原文标题**: Audio Reactive LED Strips Are Diabolically Hard

**原文链接**: [https://scottlawsonbc.com/post/audio-led](https://scottlawsonbc.com/post/audio-led)

生成摘要时出错

---

## 78. Launch HN: Freestyle – Sandboxes for Coding Agents

**原文标题**: Launch HN: Freestyle – Sandboxes for Coding Agents

**原文链接**: [https://www.freestyle.sh/](https://www.freestyle.sh/)

生成摘要时出错

---

## 79. Amazon to end support for older Kindles

**原文标题**: Amazon to end support for older Kindles

**原文链接**: [https://www.bbc.co.uk/news/articles/c98k91yy4z4o](https://www.bbc.co.uk/news/articles/c98k91yy4z4o)

生成摘要时出错

---

## 80. How Costco Won in Japan (2025)

**原文标题**: How Costco Won in Japan (2025)

**原文链接**: [https://www.readtrung.com/p/how-costco-won-in-japan](https://www.readtrung.com/p/how-costco-won-in-japan)

生成摘要时出错

---

## 81. The Clock

**原文标题**: The Clock

**原文链接**: [https://blog.senko.net/the-clock](https://blog.senko.net/the-clock)

生成摘要时出错

---

## 82. GLM-5.1: Towards Long-Horizon Tasks

**原文标题**: GLM-5.1: Towards Long-Horizon Tasks

**原文链接**: [https://z.ai/blog/glm-5.1](https://z.ai/blog/glm-5.1)

生成摘要时出错

---

## 83. App Store sees 84% surge in new apps as AI coding tools take off

**原文标题**: App Store sees 84% surge in new apps as AI coding tools take off

**原文链接**: [https://9to5mac.com/2026/04/06/app-store-sees-84-surge-in-new-apps-as-ai-coding-tools-take-off/](https://9to5mac.com/2026/04/06/app-store-sees-84-surge-in-new-apps-as-ai-coding-tools-take-off/)

生成摘要时出错

---

## 84. The Image Boards of Hayao Miyazaki

**原文标题**: The Image Boards of Hayao Miyazaki

**原文链接**: [https://animationobsessive.substack.com/p/the-image-boards-of-hayao-miyazaki](https://animationobsessive.substack.com/p/the-image-boards-of-hayao-miyazaki)

生成摘要时出错

---

## 85. Flatpak: Complete Sandbox Escape

**原文标题**: Flatpak: Complete Sandbox Escape

**原文链接**: [https://github.com/flatpak/flatpak/security/advisories/GHSA-cc2q-qc34-jprg](https://github.com/flatpak/flatpak/security/advisories/GHSA-cc2q-qc34-jprg)

生成摘要时出错

---

## 86. Every GPU That Mattered

**原文标题**: Every GPU That Mattered

**原文链接**: [https://sheets.works/data-viz/every-gpu](https://sheets.works/data-viz/every-gpu)

生成摘要时出错

---

## 87. Building a JavaScript runtime in one month

**原文标题**: Building a JavaScript runtime in one month

**原文链接**: [https://themackabu.dev/blog/js-in-one-month](https://themackabu.dev/blog/js-in-one-month)

生成摘要时出错

---

## 88. Show HN: Brutalist Concrete Laptop Stand (2024)

**原文标题**: Show HN: Brutalist Concrete Laptop Stand (2024)

**原文链接**: [https://sam-burns.com/posts/concrete-laptop-stand/](https://sam-burns.com/posts/concrete-laptop-stand/)

生成摘要时出错

---

