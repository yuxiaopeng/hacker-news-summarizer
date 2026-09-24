# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-09-24.md)

*最后自动更新时间: 2026-09-24 20:41:50*
## 1. F-Droid 2.0

**原文标题**: F-Droid 2.0

**原文链接**: [https://f-droid.org/2026/09/24/f-droid-2.0-a-new-chapter-for-android-freedom.html](https://f-droid.org/2026/09/24/f-droid-2.0-a-new-chapter-for-android-freedom.html)

经过一年多的开发，F-Droid 2.0 正式发布，标志着该项目十年来最重大的更新。该应用使用 Kotlin 和 Jetpack Compose 进行了完全重写，提供了现代化的“Material Design”界面，并为未来的贡献构建了更具可持续性的代码库。

**主要功能和改进包括：**
*   **精简导航：** 用户界面现划分为三个核心区域：发现、搜索和我的应用。设置和“附近”分享已移至顶层菜单，以减少界面杂乱。
*   **增强可发现性：** 类别显著扩展（例如包含 17 个特定的游戏流派），帮助用户查找相关软件。搜索引擎现在支持索引应用描述和翻译，并针对中日韩（CJK）语言进行了重大改进。
*   **无缝安装：** 利用现代 Android “Session” API 和欧盟《数字市场法案》带来的变化，F-Droid 2.0 提供了更流畅、更自动化的安装和后台更新体验，不再需要旧版的“特权扩展”（Privileged Extension）。
*   **现代化的隐私工具：** 更新现已默认自动化。Tor 集成已简化，转而优先支持 Tor VPN；“恐慌”（Panic）伪装功能现在通过更改图标和名称而非模仿计算器来实现，以便更透明地展示其局限性。
*   **技术转型：** 为减少技术债务，该应用现在要求 Android 7 或更高版本。为了采用现代标准，一些遗留功能（如 Ripple 集成和“特权扩展”）已被移除。

此次发布是由 NLnet 和开放技术基金会（OTF）等组织支持的协作成果，并经过了独立安全审计。未来的更新将专注于重新设计的“附近”分享功能以及进一步的性能优化。

---

## 2. Show HN: 制作像 Times New Bastard 这样的邪门字体

**原文标题**: Show HN: Make cursed fonts like Times New Bastard

**原文链接**: [https://bastardica.mitpit.com](https://bastardica.mitpit.com)

**Bastardica** is a web-based tool designed to create "cursed" or "bastard" fonts, inspired by projects like *Times New Bastard*. It allows users to blend a base font with one or more "mix-in" fonts, creating a chaotic yet functional typeface where specific characters are swapped at regular intervals.

**Key Features and Technical Details:**
*   **Mechanism:** The tool uses OpenType contextual substitutions (ligatures) to perform character swaps. This ensures the resulting fonts are compatible with any modern software that supports OpenType shaping, including web browsers, design tools, and print applications.
*   **Privacy and Performance:** Everything runs locally in the browser using Pyodide and fontTools. No fonts are uploaded to a server, ensuring user privacy and fast processing.
*   **Customization:** Users can upload their own fonts or choose from presets. Advanced options allow for adjustments to "strides" (the frequency of the swap), scaling, and Y-offsets to help mismatched glyphs align better. The creator suggests using prime numbers for strides to minimize collisions when mixing three or more fonts.
*   **Output:** The tool supports multiple industry-standard formats, including TTF, OTF, and WOFF2.
*   **Licensing:** Because the output is a derivative work, users are advised to check the licenses of their source fonts. Bastardica itself does not add any additional licensing conditions or restrictions.

Overall, Bastardica offers a simple, browser-based way to experiment with "glitched" typography for creative or experimental design projects.

---

## 3. Show HN: Whiteboard (YC W26) – An open-source IDE for thoughtful software design

**原文标题**: Show HN: Whiteboard (YC W26) – An open-source IDE for thoughtful software design

**原文链接**: [https://github.com/devdotfast/whiteboard](https://github.com/devdotfast/whiteboard)

生成摘要时出错

---

## 4. Rails World 2026 开幕主题演讲 [视频]

**原文标题**: Rails World 2026 Opening Keynote [video]

**原文链接**: [https://www.youtube.com/watch?v=vDjW_dRyKXY](https://www.youtube.com/watch?v=vDjW_dRyKXY)

所提供文本似乎是标题为“Rails World 2026 开幕主题演讲”的 YouTube 视频元数据和法律页脚。

文本的实际内容并不包含主题演讲本身的细节。相反，它列出了标准的 YouTube 导航和法律链接，包括：
*   有关新闻、版权和联系方式的信息。
*   面向创作者、广告商和开发者的资源。
*   YouTube 的服务条款、隐私政策和安全指南。
*   **2026 Google LLC** 的版权声明。

总之，虽然标题暗示了在 2026 年会议上关于 Ruby on Rails 框架未来的演讲，但所提供的文本并未包含关于主题演讲话题、软件更新或演讲者的实质性信息。它仅作为该视频内容的平台占位符。

---

## 5. 无畏 SIMD v1.0

**原文标题**: Fearless SIMD v1.0

**原文链接**: [https://linebender.org/blog/fearless-simd-1-0/](https://linebender.org/blog/fearless-simd-1-0/)

**Fearless SIMD v1.0** marks the stable release of a Rust crate designed to make SIMD (Single Instruction, Multiple Data) operations memory-safe and accessible. Developed over eight years by Shnatsel, the library aims to eliminate the "unsafe" code typically required for high-performance vectorization.

**Key Features:**
*   **Safety without Compromise:** The crate avoids thousands of ad-hoc `unsafe` blocks found in traditional SIMD abstractions. It achieves this using a `kernel!` macro (leveraging target feature v1.1) and a safe transmute module for load/store operations, leaving only a small, audited core.
*   **High Performance:** It provides portable abstractions with both "precise" and "fast" variants for edge-case operations. It supports native hardware vector sizes and allows safe access to platform-specific intrinsics, ensuring there is no "performance ceiling."
*   **Improved Ergonomics:** Alongside v1.0, the `fearless_simd_macros` crate introduces a `#[simd]` macro. This simplifies function multiversioning—a historically complex task—by automating inlining and boilerplate reduction. 
*   **Stability and Future-Proofing:** The developers commit to three years of security updates. The API is designed to be forward-compatible with upcoming technologies like the `f16` type, ARM’s SVE, and RISC-V Vector Extensions.
*   **Ecosystem Integration:** Fearless SIMD is intended to complement, rather than be replaced by, the eventual stabilization of `std::simd`. It is already widely adopted, serving as a dependency for over 1,000 crates in the Rust ecosystem.

Ultimately, Fearless SIMD provides a production-ready, stable, and ergonomic framework for writing high-performance vector code without the memory-safety risks historically associated with hardware intrinsics.

---

## 6. My weird new hobby: Wandering around Tokyo on Google Maps

**原文标题**: My weird new hobby: Wandering around Tokyo on Google Maps

**原文链接**: [https://ahmedhossamdev.com/writing/my-weird-new-hobby-wandering-around-tokyo/](https://ahmedhossamdev.com/writing/my-weird-new-hobby-wandering-around-tokyo/)

生成摘要时出错

---

## 7. 被遗忘的东兰辛战役

**原文标题**: The forgotten battle of East Lansing

**原文链接**: [https://eastlansinginfo.news/the-forgotten-battle-of-east-lansing/](https://eastlansinginfo.news/the-forgotten-battle-of-east-lansing/)

1937年6月7日，一场局部劳资纠纷升级为“东兰辛之战”，演变为密歇根州立学院（MSC）学生与美国汽车工人联合会（UAW）成员之间的肢体冲突。

冲突的导火索是首都城拆解公司（Capital City Wrecking Company）罢工后，几名 UAW 领导人及其妻子被捕。作为回应，UAW 领导人莱斯特·沃什伯恩宣布举行“兰辛劳动节假”，促使 15,000 名工人使兰辛的商业机构和工厂陷入停摆。当工会的“流动纠察队”进入东兰辛，强迫当地商户和餐馆停业时，局势变得动荡不安。

包括身着制服的预备役军官训练团（ROTC）成员在内的 MSC 学生，将这种强制停业视为对其主权和获取食物权利的侵犯。学生群体最终发起了反击，双方爆发了肉搏战并使用了简易武器。在混战中，学生们掀翻了至少一辆汽车，并将约 8 到 20 名工会成员扔进了红杉河。州长弗兰克·墨菲在附近的山丘上目睹了这场“战斗”，但他拒绝准许 ROTC 骑兵介入，称这种行为“太像哥萨克人”。

事后，媒体和州政界人士广泛赞扬这些学生是抵制激进主义的“热血美国人”。然而，劳工运动在更宏观的战术层面赢得了胜利：首都城拆解公司在当天签署了工会合同，被捕的领导人获释且所有指控均被撤销。尽管当时的冲突异常激烈且学生群体备受褒奖，但这一事件已在很大程度上成了密歇根历史上被遗忘的篇章。

---

## 8. 书评：并行编程难吗？如果难，该如何应对？

**原文标题**: Book review: Is parallel programming hard, and, if so, what can you do about it?

**原文链接**: [https://ahelwer.ca/post/2026-09-21-concurrency-textbook/](https://ahelwer.ca/post/2026-09-21-concurrency-textbook/)

本文评述了保罗·E·麦肯尼（Paul E. McKenney）编写的免费在线教科书《并行编程难吗？如果难，你能做什么？》。评述者是一位分布式系统和 TLA+ 专家，旨在通过阅读本书来弥补其在底层并发和无锁算法方面的知识空白。

**核心内容与见解：**
*   **硬件与编译器**：评述者强调了书中对现代 CPU 与编译器交互方式的深入探讨。第 3 章和第 4 章探讨了“共享变量的种种怪象”，解释了激进的优化（如加载/存储撕裂和重排序）如何导致并行程序中出现荒谬的行为。
*   **MESI 协议**：虽然主要在附录中详细说明，但评述者强调了 MESI 缓存一致性协议的重要性，因为它解释了为什么在单个缓存行上实际上不会发生“字面意义上的并发”写入。
*   **实践案例**：第 5 章（计数）被视为亮点。该章节分析了跨线程增加计数器的各种方法，展示了简单原子指令与更复杂、可扩展的方法（如统计型单线程计数器）之间巨大的性能差异。
*   **格式与易用性**：该书提供多种 PDF 格式。虽然评述者称赞了书中的“知识自测”框，但认为过多的内部链接给电子阅读器的导航带来了困扰。

**结论：**
评述者认为该教科书是一份极其优秀的资源（尽管内容以 Linux 内核为中心），成功弥合了高层并发概念与底层硬件现实之间的鸿沟。尽管评述者后来转而通过其他资料研究特定的无锁数据结构和 C++11 内存模型，但他们认为麦肯尼的书激发了其对内存排序和释放-获取语义等并行编程中“极其反直觉”的复杂性的浓厚兴趣。

---

## 9. 利用大语言模型追踪炼金术知识并解读17世纪书信

**原文标题**: Using LLMs to trace alchemical knowledge and decode 17th century letters

**原文链接**: [https://resobscura.substack.com/p/ai-labs-need-to-start-funding-historical](https://resobscura.substack.com/p/ai-labs-need-to-start-funding-historical)

生成摘要时出错

---

## 10. Stable (YC W20) Is Hiring Product Engineers

**原文标题**: Stable (YC W20) Is Hiring Product Engineers

**原文链接**: [https://www.usestable.com/careers/product-engineer](https://www.usestable.com/careers/product-engineer)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 2 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 3 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 4 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 5 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 6 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 7 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 8 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 9 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 10 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 11 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 12 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 13 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 14 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 15 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 16 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 17 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 18 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 19 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 20 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 21 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 22 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 23 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 24 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 25 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 26 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 27 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 28 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 29 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 30 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 31 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 32 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 33 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 34 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 35 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 36 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 37 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 38 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 39 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 40 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 41 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 42 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 43 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 44 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 45 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 46 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 47 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 48 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 49 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 50 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 51 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 52 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 53 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 54 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 55 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 56 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 57 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 58 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 59 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 60 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 61 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 62 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 63 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 64 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 65 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 66 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 67 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 68 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 69 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 70 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 71 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 72 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 73 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 74 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 75 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 76 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 77 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 78 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 79 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 80 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 81 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 82 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 83 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 84 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 85 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 86 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 87 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 88 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 89 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 90 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 91 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 92 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 93 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 94 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 95 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 96 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 97 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 98 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 99 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 100 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 101 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 102 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 103 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 104 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 105 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 106 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 107 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 108 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 109 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 110 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 111 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 112 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 113 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 114 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 115 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 116 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 117 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 118 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 119 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 120 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 121 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 122 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 123 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 124 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 125 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 126 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 127 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 128 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 129 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 130 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 131 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 132 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 133 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 134 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 135 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 136 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 137 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 138 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 139 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 140 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 141 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 142 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 143 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 144 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 145 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 146 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 147 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 148 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 149 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 150 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 151 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 152 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 153 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 154 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 155 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 156 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 157 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 158 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 159 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 160 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 161 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 162 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 163 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 164 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 165 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 166 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 167 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 168 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 169 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 170 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 171 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 172 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 173 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 174 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 175 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 176 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 177 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 178 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 179 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 180 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 181 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 182 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 183 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 184 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 185 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 186 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 187 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 188 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 189 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 190 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 191 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 192 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 193 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 194 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 195 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 196 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 197 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 198 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 199 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 200 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 201 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 202 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 203 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 204 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 205 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 206 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 207 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 208 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 209 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 210 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 211 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 212 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 213 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 214 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 215 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 216 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 217 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 218 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 219 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 220 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 221 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 222 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 223 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 224 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 225 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 226 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 227 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 228 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 229 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 230 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 231 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 232 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 233 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 234 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 235 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 236 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 237 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 238 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 239 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 240 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 241 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 242 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 243 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 244 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 245 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 246 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 247 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 248 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 249 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 250 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 251 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 252 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 253 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 254 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 255 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 256 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 257 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 258 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 259 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 260 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 261 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 262 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 263 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 264 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 265 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 266 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 267 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 268 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 269 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 270 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 271 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 272 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 273 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 274 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 275 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 276 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 277 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 278 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 279 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 280 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 281 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 282 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 283 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 284 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 285 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 286 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 287 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 288 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 289 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 290 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 291 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 292 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 293 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 294 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 295 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 296 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 297 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 298 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 299 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 300 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 301 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 302 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 303 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 304 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 305 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 306 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 307 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 308 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 309 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 310 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 311 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 312 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 313 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 314 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 315 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 316 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 317 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 318 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 319 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 320 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 321 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 322 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 323 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 324 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 325 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 326 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 327 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 328 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 329 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 330 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 331 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 332 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 333 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 334 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 335 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 336 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 337 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 338 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 339 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 340 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 341 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 342 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 343 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 344 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 345 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 346 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 347 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 348 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 349 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 350 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 351 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 352 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 353 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 354 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 355 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 356 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 357 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 358 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 359 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 360 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 361 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 362 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 363 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 364 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 365 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 366 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 367 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 368 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 369 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 370 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 371 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 372 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 373 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 374 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 375 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 376 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 377 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 378 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 379 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 380 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 381 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 382 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 383 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 384 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 385 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 386 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 387 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 388 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 389 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 390 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 391 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 392 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 393 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 394 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 395 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 396 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 397 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 398 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 399 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 400 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 401 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 402 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 403 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 404 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 405 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 406 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 407 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 408 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 409 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 410 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 411 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 412 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 413 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 414 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 415 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 416 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 417 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 418 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 419 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 420 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 421 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 422 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 423 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 424 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 425 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 426 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 427 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 428 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 429 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 430 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 431 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 432 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 433 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 434 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 435 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 436 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 437 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 438 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 439 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 440 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 441 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 442 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 443 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 444 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 445 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 446 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 447 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 448 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 449 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 450 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 451 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 452 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 453 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 454 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 455 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 456 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 457 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 458 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 459 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 460 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 461 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 462 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 463 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 464 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 465 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 466 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 467 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 468 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 469 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 470 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 471 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 472 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 473 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 474 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 475 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 476 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 477 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 478 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 479 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 480 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 481 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 482 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 483 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 484 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 485 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 486 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 487 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 488 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 489 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 490 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 491 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 492 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 493 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 494 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 495 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 496 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 497 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 498 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 499 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 500 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 501 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 502 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 503 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 504 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 505 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 506 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 507 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 508 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 509 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 510 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 511 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 512 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 513 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 514 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 515 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 516 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 517 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 518 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 519 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 520 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 521 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 522 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 523 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 524 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 525 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 526 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 527 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 528 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 529 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 530 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 531 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 532 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 533 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 534 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 535 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 536 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 537 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 538 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 539 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 540 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 541 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 542 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 543 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 544 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 545 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 546 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 547 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 548 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 549 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 550 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 551 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
