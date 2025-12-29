# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-12-29.md)

*最后自动更新时间: 2025-12-29 17:47:32*
## 1. 使用 Zig 进行静态分配

**原文标题**: Static Allocation with Zig

**原文链接**: [https://nickmonad.blog/2025/static-allocation-with-zig-kv/](https://nickmonad.blog/2025/static-allocation-with-zig-kv/)

本文探讨了使用 Zig 语言编写的兼容 Redis 的键值服务器 **kv** 的实现，重点介绍了 “TigerStyle” **静态内存分配**。这种设计模式要求在启动时分配所有内存，在运行时消除动态分配或释放，以确保性能的可预测性，避免“释放后使用”（use-after-free）错误，并促使开发者更深入地理解系统限制。

作者将实现过程分为三个核心领域：

*   **连接处理：** 该服务器使用 `io_uring` 进行异步 I/O，并为连接结构和缓冲区预分配池。`std.heap.MemoryPool` 用于管理活动连接，而自定义的 `ByteArrayPool` 则处理固定大小的接收和发送缓冲区。如果池耗尽，新连接将被拒绝，从而确保系统永远不会超出其内存边界。
*   **命令解析：** 为了解析 RESP（Redis 序列化协议）格式，服务器使用了 `std.heap.FixedBufferAllocator`。它充当“堆栈分配器”（bump allocator），在每次请求后重置。通过创建直接指向请求缓冲区的切片（slice），它实现了一种零拷贝方法，其缓冲区大小由最大可能的命令长度决定。
*   **键值存储：** 系统利用了 Zig 的 `std.StringHashMapUnmanaged`。通过在启动时调用 `ensureTotalCapacity`，服务器可以在运行时使用 `putAssumeCapacity`，从而绕过对分配器的需求。实际的键值数据存储在预分配的 `ByteArrayPool` 中。

作者承认该方案存在重大挑战，例如处理列表时潜在的内存利用率低下，以及哈希表删除过程中管理“墓碑”（tombstones）的复杂性。尽管存在这些障碍，作者得出的结论是：静态分配通过迫使开发者预先考虑所有使用模式，构建出了一个更稳健、稳定且易于维护的系统。

---

## 2. GOG 将被其原联合创始人收购：这对你意味着什么

**原文标题**: GOG is getting acquired by its original co-founder: What it means for you

**原文链接**: [https://www.gog.com/blog/gog-is-getting-acquired-by-its-original-co-founder-what-it-means-for-you/](https://www.gog.com/blog/gog-is-getting-acquired-by-its-original-co-founder-what-it-means-for-you/)

GOG宣布，其原联合创始人Michał Kiciński已从CD PROJEKT手中将其收购。此次过渡标志着GOG转向独立运营，使其能够进一步强化其游戏保存和无DRM（数字版权管理）所有权的创始理念。

**此次收购的核心要点包括：**

*   **核心价值：** 平台将继续致力于无DRM模式，通过离线安装包和可选客户端（GOG GALAXY）确保用户拥有游戏的真实所有权。
*   **用户体验：** 用户账号、现有游戏库或数据隐私不会发生任何变化。GOG依然是用户数据的控制方。
*   **与CD PROJEKT RED的关系：** 尽管分家，两家公司仍将保持紧密的合作伙伴关系。CD PROJEKT RED所有现有及未来的作品将继续在GOG平台发布。
*   **财务状况与战略：** 此举并非源于财务不稳定——GOG报告了强劲的年度业绩——而是战略调整。CD PROJEKT旨在专注于开发高质量的RPG游戏，而Kiciński则意在拓展GOG“让游戏长存”的使命。
*   **未来计划：** GOG计划扩大其“保存计划”并加强对独立开发者的支持。来自“GOG赞助者”的资金和打赏将留在公司内部，用于资助针对经典游戏的“宏大救援任务”，并计划在2026年推出更多社区驱动的倡议。

总而言之，此次收购代表了GOG的“回归初心”，确保其在PC游戏市场中保持独立运营，并专注于非掠夺式、保存至上的经营理念。

---

## 3. 未经处理的照片是什么样子的

**原文标题**: What an unprocessed photo looks like

**原文链接**: [https://maurycyz.com/misc/raw_photo/](https://maurycyz.com/misc/raw_photo/)

生成摘要时出错

---

## 4. Libgodc：为世嘉 Dreamcast 编写 Go 语言程序

**原文标题**: Libgodc: Write Go Programs for Sega Dreamcast

**原文链接**: [https://github.com/drpaneas/libgodc](https://github.com/drpaneas/libgodc)

**Libgodc** 是专为世嘉 Dreamcast 设计的定制化 Go 运行时。它取代了标准的 Go 运行时，以适应游戏机独特的硬件限制，包括 16MB 内存、单核 SH-4 CPU 以及无操作系统的环境。尽管存在这些限制，libgodc 仍保留了 Go 的核心功能，支持 goroutine、channel 和垃圾回收。

该项目由 **godc** 命令行工具提供支持，通过处理工具链配置、项目初始化和二进制文件构建来简化开发流程。配套文档内容详尽，涵盖了运行时架构、“高效 Dreamcast Go” 最佳实践，以及用于从 Go 代码调用 C 函数的 KOS (KallistiOS) 封装。

在真实 SH-4 硬件上的性能基准测试证明了该运行时的效率：
*   **上下文切换：** 约 6.4 μs
*   **Goroutine 启动：** 约 31 μs
*   **GC 停顿：** 介于 72 μs 至 6 ms 之间

为了帮助开发者快速上手，仓库中提供了多个示例项目。这些项目涵盖了从基础的 “Hello World” 和 BIOS 字体渲染，到文件系统浏览器以及《乒乓球》(Pong) 和《打砖块》(Breakout) 等完整可玩的游戏。

Libgodc 采用 BSD 3-Clause 许可证发布，并要求 Go 版本为 1.25.3 或更高。

---

## 5. 被德铁绑架

**原文标题**: Kidnapped by Deutsche Bahn

**原文链接**: [https://www.theocharis.dev/blog/kidnapped-by-deutsche-bahn/](https://www.theocharis.dev/blog/kidnapped-by-deutsche-bahn/)

在《被德国铁路“绑架”》一文中，作者以讽刺且沮丧的笔调，记录了2024年平安夜的一次旅行灾难。讲述者原本只想进行一段从科隆到梅肯海姆、全长仅35公里的短途旅行，结果却演变成了一场荒诞的折磨，突显出德国国家铁路公司（DB）的系统性溃败。

旅程伊始，列车便因“波恩附近的故障”而延误并改道。讲述者原计划在特罗斯多夫下车与父亲汇合，但情况随后变得离奇：司机宣布列车无法在特罗斯多夫停靠，因为该列车在当时所行驶的轨道上未进行正确的停靠注册。结果，讲述者被迫留在车上，眼睁睁看着列车驶过多个车站，最终被带到了63公里外、位于另一个联邦州的诺伊维德。

作者以这次“绑架”为契机，批判了德铁的运营和企业文化。主要批评点包括：
*   **误导性的统计数据：** 作者指出，德铁将延误少于6分钟的列车视为“准点”，并将取消的班次完全排除在准点率指标之外。
*   **沟通不力：** 关于重大改道的广播通知仅使用德语，导致不懂德语的乘客对目的地一无所知。
*   **补偿不足：** 尽管发生了严重的改道和延误，作者计算出的补偿金仅为1.50欧元，远低于4欧元的最低支付门槛。

最后，这篇文章将德国铁路的出行体验描述为：乘客被视同“牲畜”或“货物”，不得不忍受不可预知的延误和官僚主义的冷漠。

---

## 6. Show HN：用 Claude Code 氛围编码一个书架

**原文标题**: Show HN: Vibe coding a bookshelf with Claude Code

**原文链接**: [https://balajmarius.com/writings/vibe-coding-a-bookshelf-with-claude-code/](https://balajmarius.com/writings/vibe-coding-a-bookshelf-with-claude-code/)

在这篇文章中，作者讲述了他们如何利用 “Claude Code” 最终完成了 500 多本个人藏书的编目工作。由于手动录入数据过于繁琐，该项目多年来一直被搁置在“待办清单”中。

由于传统的 ISBN 扫描仪无法识别罗马尼亚语书籍和生僻版本，作者拍摄了 470 张书脊照片，并使用 Claude 编写脚本，通过 OpenAI 的视觉 API 处理这些图像。这一流程实现了元数据提取、标题规范化以及图像缩放。作者强调了角色的转变：虽然 AI 达到了 90% 的准确率，但他选择通过“人类判断”来手动修复剩余的边缘案例，而不是过度设计一个完美的纯技术方案。

该项目的 UI 突破了传统的网格布局，重现了实体书架的美感。作者利用 Claude 实现了色彩量化以生成逼真的书脊，并将页数映射为相应的书脊宽度。他还通过“氛围编码”（vibe coding）精进了用户体验——反复迭代 Framer Motion 动画，直到书籍的“倾斜感”显得自然，并果断删除了像“无限滚动”这种虽然技术上可行但有碍体验的代码。

作者总结道，AI 大幅降低了执行成本，从根本上改变了开发者的角色。在这种新范式下，AI 负责机械性的实现，而人类则专注于**品味与方向**。项目的成功并非源于 AI 的完美，而是因为它让作者能够专注于塑造“氛围感”，以及那最后 10% 让项目变得真正有意义的关键工作。

---

## 7. Show HN：Z80-μLM，一个仅 40KB 的“对话式 AI”

**原文标题**: Show HN: Z80-μLM, a 'Conversational AI' That Fits in 40KB

**原文链接**: [https://github.com/HarryR/z80ai](https://github.com/HarryR/z80ai)

**Z80-μLM** 是一款专为复古计算设计的微型语言模型，针对仅有 64KB RAM 的 Z80 处理器 (4MHz) 进行了专门优化。该项目将整个“对话式 AI”系统——包括推理引擎、模型权重和聊天界面——全部集成到了一个仅 40KB 的 CP/M 系统 .COM 二进制文件中。

**技术架构**
为了在 20 世纪 70 年代的硬件上实现性能突破，该模型采用了几种极端的优化技术：
*   **三元组哈希编码 (Trigram Hash Encoding)：** 输入文本被哈希到 128 个桶中。这使得模型具有容错性（对拼写错误不敏感）且不依赖词序，尽管这限制了其对复杂句式的理解。
*   **2 比特量化：** 权重被限制为四个值（{-2, -1, 0, +1}），每个字节打包存储四个权重。
*   **整数推理：** 系统避开了浮点运算，利用 Z80 原生的 16 位寄存器对进行乘累加循环和定点缩放。
*   **量化感知训练 (QAT)：** 确保模型在严苛的数值限制下仍能保持稳定性和表达能力。

**功能与局限性**
虽然 Z80-μLM 不具备通用智能或深厚的语法功底，但它可以提供具有性格特征的自回归响应。它在模糊匹配和简短交互方面表现尤为出色。内置示例包括休闲聊天机器人 "tinychat" 和“二十个问题”风格的猜谜游戏 "guess"。

该项目证明，即使在 8 位硬件上，也可以创建一个能够根据人类输入“形态”做出响应的功能性“人格”引擎。该项目已开源（MIT/Apache-2.0 协议），并提供了使用 Claude 或 Ollama 等现代大模型训练自定义模型的工具。

---

## 8. You can make up HTML tags

**原文标题**: You can make up HTML tags

**原文链接**: [https://maurycyz.com/misc/make-up-tags/](https://maurycyz.com/misc/make-up-tags/)

This article highlights a standardized but often underutilized feature of web development: the ability to create and use **custom HTML tags**. 

Instead of nesting multiple generic `<div>` elements with various class names, developers can use descriptive, custom tags like `<main-article>` or `<article-quote>`. 

**Key takeaways include:**

*   **Browser Behavior:** Modern browsers treat unrecognized tags as generic elements. They carry no default styling, allowing developers to define their appearance entirely through CSS using the tag name as a selector.
*   **Future-Proofing:** By including a hyphen in the tag name (a convention associated with the Web Components standard), developers can guarantee that their custom tags will never conflict with future additions to the official HTML specification.
*   **Improved Readability:** Custom tags solve the problem of "div soup." When code is deeply nested, it is often difficult to identify which `</div>` closes which section. Descriptive tag names make the document structure clear and much easier to navigate.
*   **Best Practices:** While developers should still use built-in semantic tags (like `<nav>` or `<header>`) whenever appropriate, custom tags are a superior alternative to generic `<div>` or `<span>` tags when a specific semantic element does not exist.

Ultimately, the author argues that using custom tags leads to cleaner, more maintainable code by replacing confusing class-heavy structures with intuitive, readable elements.

---

## 9. Linux DAW: Help Linux musicians to quickly and easily find the tools they need

**原文标题**: Linux DAW: Help Linux musicians to quickly and easily find the tools they need

**原文链接**: [https://linuxdaw.org/](https://linuxdaw.org/)

生成摘要时出错

---

## 10. Feynman's Hughes Lectures: 950 pages of notes

**原文标题**: Feynman's Hughes Lectures: 950 pages of notes

**原文链接**: [https://thehugheslectures.info/the-lectures/](https://thehugheslectures.info/the-lectures/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 2 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 3 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 4 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 5 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 6 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 7 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 8 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 9 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 10 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 11 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 12 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 13 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 14 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 15 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 16 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 17 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 18 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 19 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 20 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 21 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 22 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 23 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 24 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 25 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 26 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 27 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 28 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 29 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 30 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 31 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 32 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 33 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 34 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 35 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 36 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 37 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 38 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 39 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 40 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 41 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 42 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 43 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 44 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 45 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 46 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 47 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 48 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 49 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 50 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 51 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 52 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 53 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 54 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 55 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 56 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 57 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 58 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 59 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 60 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 61 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 62 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 63 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 64 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 65 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 66 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 67 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 68 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 69 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 70 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 71 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 72 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 73 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 74 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 75 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 76 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 77 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 78 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 79 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 80 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 81 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 82 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 83 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 84 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 85 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 86 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 87 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 88 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 89 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 90 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 91 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 92 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 93 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 94 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 95 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 96 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 97 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 98 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 99 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 100 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 101 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 102 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 103 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 104 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 105 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 106 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 107 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 108 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 109 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 110 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 111 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 112 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 113 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 114 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 115 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 116 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 117 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 118 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 119 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 120 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 121 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 122 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 123 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 124 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 125 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 126 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 127 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 128 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 129 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 130 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 131 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 132 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 133 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 134 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 135 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 136 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 137 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 138 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 139 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 140 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 141 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 142 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 143 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 144 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 145 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 146 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 147 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 148 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 149 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 150 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 151 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 152 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 153 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 154 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 155 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 156 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 157 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 158 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 159 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 160 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 161 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 162 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 163 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 164 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 165 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 166 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 167 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 168 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 169 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 170 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 171 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 172 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 173 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 174 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 175 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 176 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 177 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 178 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 179 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 180 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 181 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 182 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 183 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 184 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 185 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 186 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 187 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 188 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 189 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 190 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 191 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 192 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 193 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 194 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 195 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 196 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 197 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 198 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 199 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 200 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 201 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 202 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 203 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 204 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 205 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 206 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 207 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 208 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 209 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 210 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 211 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 212 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 213 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 214 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 215 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 216 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 217 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 218 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 219 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 220 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 221 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 222 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 223 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 224 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 225 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 226 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 227 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 228 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 229 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 230 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 231 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 232 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 233 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 234 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 235 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 236 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 237 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 238 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 239 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 240 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 241 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 242 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 243 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 244 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 245 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 246 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 247 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 248 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 249 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 250 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 251 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 252 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 253 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 254 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 255 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 256 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 257 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 258 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 259 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 260 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 261 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 262 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 263 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 264 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 265 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 266 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 267 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 268 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 269 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 270 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 271 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 272 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 273 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 274 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 275 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 276 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 277 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 278 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 279 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 280 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 281 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 282 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 283 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 284 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
