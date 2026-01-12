# Hacker News 热门文章摘要 (2026-01-12)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. TimeCapsuleLLM：仅使用 1800-1875 年数据训练的大语言模型

**原文标题**: TimeCapsuleLLM: LLM trained only on data from 1800-1875

**原文链接**: [https://github.com/haykgrigo3/TimeCapsuleLLM](https://github.com/haykgrigo3/TimeCapsuleLLM)

**TimeCapsuleLLM** 是一个实验性人工智能项目，旨在构建能够模拟 19 世纪口吻、词汇和世界观的大语言模型。与在历史风格上进行微调的标准模型不同，TimeCapsuleLLM 采用了**选择性时间训练（STT）**——即完全使用 1800 年至 1875 年期间的数据（主要来自伦敦）进行从零开始的训练。这种方法确保了模型完全不受现代概念、偏见或信息的影响。

该项目经历了多个版本的迭代：
*   **v0 与 v0.5**：基于 Andrej Karpathy 的 nanoGPT 架构（1600 万至 1.23 亿参数）。这些早期版本捕捉到了维多利亚时代的语言风格，但在连贯性和事实准确性方面表现欠佳。
*   **v1**：基于微软 Phi 1.5 架构的 7 亿参数模型。它展示了将帕默斯顿勋爵（Lord Palmerston）等真实历史人物与当时特定事件联系起来的能力。
*   **v2**：目前正在开发中，拥有包含 136,344 份文档（涵盖书籍、法律文件和报纸）的 90GB 海量数据集。早期评估版本（v2mini）显示其上下文理解能力有所提升，但在分词（tokenization）方面仍面临挑战。

开发者强调，从零开始训练至关重要，因为预训练模型无法“忘记”现代数据。通过使用自定义分词器和精选的历史文本，该项目旨在构建一个不仅是“伪装”历史，而是真正作为那个时代“数字文物”而存在的模型。为了适应不断增长的数据集，训练硬件已从消费级设备（RTX 4060）升级为高性能 A100 GPU。最终，TimeCapsuleLLM 将作为探索历史推理和语言保护的有效工具。

---

## 2. LLVM：糟粕

**原文标题**: LLVM: The bad parts

**原文链接**: [https://www.npopov.com/2026/01/11/LLVM-The-bad-parts.html](https://www.npopov.com/2026/01/11/LLVM-The-bad-parts.html)

在本文中，LLVM 的首席维护者指出了项目中几个亟待改进的关键领域，并将这些“不足之处”视为成长的契机，而非根本性的缺陷。

**组织与工作流程挑战**
首要问题是**评审能力**不足；合格评审者的短缺导致了 PR 延迟和“走过场”现象。其 C++ API 和 IR 的**高频变动**加重了下游用户的负担，而庞大的代码库则导致了**构建缓慢**。此外，**CI 不稳定**和测试随机失败削弱了对贡献者的反馈信号，使得识别真正的回归问题变得困难。

**测试与架构**
尽管 LLVM 拥有强大的单元测试，但缺乏完善的**端到端可执行测试**。这导致了**后端分化**，开发人员为了避免跨目标验证的复杂性，往往倾向于实现特定目标的权宜之计（hacks），而非通用优化。此外，项目缺乏用于追踪**运行时性能**的官方基础设施，且**编译速度**（特别是 JIT 和未优化 (-O0) 构建）仍是一个隐忧。

**IR 设计与技术债务**
若干技术问题源于 LLVM 中间表示（IR）的设计：
*   **Undef 值：** 这些值难以推理且增加了优化的复杂性；项目正转向使用“poison”值。
*   **不健全性：** 理论上的误编译以及缺乏正式规范（特别是关于指针来源/provenance）的问题仍未解决。
*   **约束编码：** 不一致的方法（元数据、属性、assumes）使得在整个优化流水线中保留事实变得困难。
*   **浮点语义：** 处理非标准 IEEE 754 环境仍存在问题。

最后，作者指出了**部分迁移**的难度，例如长达十年的新 Pass 管理器过渡，并强调 LLVM 庞大的规模使得重大的架构演进变得异常缓慢且复杂。

---

## 3. 告别 Date，拥抱 Temporal

**原文标题**: Date is out, Temporal is in

**原文链接**: [https://piccalil.li/blog/date-is-out-and-temporal-is-in/](https://piccalil.li/blog/date-is-out-and-temporal-is-in/)

在本文中，Mat Marquis 指出 JavaScript 长期使用的 `Date` 对象存在根本性缺陷，并最终将被 **Temporal** API 所取代。

Marquis 强调了当前 `Date` 实现中的几个关键问题：
*   **不一致性**：`Date` 的行为令人困惑，例如月份从 0 开始计数而日期从 1 开始，以及不可预测的字符串解析（使用连字符与斜杠等不同分隔符会产生不同的结果）。
*   **设计糟糕**：`Date` 继承自一个已弃用的 Java 实现，缺乏对本地时间和 GMT 以外时区的强力支持，且不支持非公历历法。
*   **可变性**：作者“刻骨铭心”的槽点是 `Date` 是一个可变对象。与数字或字符串等不可变的原始值（Primitive values）不同，修改 `Date` 实例会更改内存中的底层数据。这会导致常见的 Bug：在程序的一处修改日期引用，会无意中改变其他地方的数值。

解决方案是 **Temporal** API，它是一个现代命名空间对象（类似于 `Math`）而非构造函数。`Temporal` 通过专门的类和方法提供了一种更细致、更具逻辑性的时间处理方式，例如：
*   **`Temporal.Now`**：用于获取当前时间或日期。
*   **专门的对象**：包括 `PlainDate`、`ZonedDateTime` 和 `Duration`，允许开发者处理带时区或不带时区的特定时间数据。

虽然从技术上讲 `Temporal` 仍然是对象，但该 API 的设计旨在解决过时的 `Date` 构造函数所导致的“开发体验”和性能问题，从而有效地通过一种更可靠的“Web 标准”模型使旧系统过时。

---

## 4. 软盘竟成了最适合孩子的电视遥控器

**原文标题**: Floppy disks turn out to be the greatest TV remote for kids

**原文链接**: [https://blog.smartere.dk/2026/01/floppy-disks-the-best-tv-remote-for-kids/](https://blog.smartere.dk/2026/01/floppy-disks-the-best-tv-remote-for-kids/)

在本文中，作者介绍了他如何利用老式软盘为三岁的儿子制作一个具有触感、实体化的电视遥控器。该项目源于对现代智能电视的批判，作者认为智能电视对儿童来说过于复杂，且自动播放等功能会助长被动观看。通过使用软盘，作者旨在提供一种有形的、“易于理解”的媒介，通过明确的操作起始感和机械反馈，赋予孩子独立做出选择的能力。

**技术实现：**
该设备使用了一个改装的软驱和双微控制器架构（ATmega负责软驱控制，ESP8266负责Wi-Fi连接）。核心技术亮点包括：
*   **硬件改装：** 由于软驱本身不会向操作系统发送插入磁盘的信号，作者增加了一个物理滚轮开关来触发系统。
*   **电源管理：** 为了实现遥控器的便携性，它采用18650电池供电。升压转换器提供驱动器所需的5V电压，而1000uF电容则用于应对磁盘启动时产生的高电流脉冲。
*   **软件：** 通过使用Arduino FDC Floppy库，ATmega从磁盘的FAT文件系统中读取一个微小的“autoexec”文件。这会触发一条指令，通过Wi-Fi发送给服务器端处理程序，进而控制Chromecast。

**功能与结果：**
系统将“插入磁盘”识别为播放，“弹出磁盘”识别为暂停。特定的磁盘被编程为播放特定的节目或随机音乐曲目。考虑到幼儿操作较为粗鲁，作者将程序设定为在读取后让磁头移动至20磁道，以保护0磁道上的关键数据免受物理损伤。该项目取得了成功，孩子通过软盘带来的机械感、听觉和感官体验，很快学会了独立操控媒体内容。

---

## 5. macOS Tahoe 调整窗口大小的困扰

**原文标题**: The struggle of resizing windows on macOS Tahoe

**原文链接**: [https://noheger.at/blog/2026/01/11/the-struggle-of-resizing-windows-on-macos-tahoe/](https://noheger.at/blog/2026/01/11/the-struggle-of-resizing-windows-on-macos-tahoe/)

文章指出，macOS Tahoe 中极大的窗口圆角半径造成了严重的可用性缺陷，阻碍了窗口的缩放操作。虽然许多人批评其“玩具化”的美学风格，但作者重点关注的是这一设计选择如何破坏了长久以来的用户直觉。

问题的核心在于缩放“触发区”——一个位于窗口角落的 19x19 像素区域。由于 Tahoe 的圆角弧度极大，该交互区域约有 75% 位于窗口可见边界之外。

这与人类的自然行为产生了冲突：用户会本能地尝试点击可见圆角的“内部”来抓取窗口。然而在 Tahoe 中，点击内部往往会落在指定的 19x19 像素目标区域之外，导致缩放失败。讽刺的是，缩放窗口最可靠的方法竟然是点击窗口圆角外的空白区域，这种操作违反直觉且极易导致误操作。作者总结道，macOS Tahoe 为了追求这种特定的美学，牺牲了功能的可靠性，违背了用户数十年来的计算机使用习惯。

---

## 6. 复现 DeepSeek 的 MHC：当残差连接爆炸时

**原文标题**: Reproducing DeepSeek's MHC: When Residual Connections Explode

**原文链接**: [https://taylorkolasinski.com/notes/mhc-reproduction/](https://taylorkolasinski.com/notes/mhc-reproduction/)

本文探讨了 DeepSeek 的“流形约束超连接”（mHC），这是对自 2016 年以来在 Transformer 架构中占据主导地位的传统残差连接（$x + F(x)$）的重新设计。

标准残差连接使用单一信息流，而超连接（HC）则利用受可学习混合矩阵（$H_{res}, H_{pre}, H_{post}$）控制的多个并行流。这种架构具有更强的表达能力，但也引入了一个致命缺陷：无约束的矩阵会导致信号呈指数级放大。在 1000 万（10M）参数规模的复现中，信号放大倍数（通过 $A_{max}$ 衡量）达到 9.2 倍，而 DeepSeek 报告称在 270 亿（27B）参数规模下峰值达到了 3000 倍，直接导致模型崩溃。

为解决这一问题，mHC 将混合矩阵约束为“双随机矩阵”（所有元素均为非负，且行之和与列之和均为 1）。这是通过 Sinkhorn-Knopp 算法实现的，该算法是一个可微过程，确保网络仅对信息流进行加权平均，从而在数学上消除了信号放大的可能性。

**核心实验发现：**
*   **稳定性 vs. 性能：** 在 10M 参数规模下，无约束的 HC 实现了更低的验证损失，但表现出高方差和混乱的信号增长。相比之下，mHC 在所有随机种子下都保持了 1.0 的完美 $A_{max}$。
*   **“稳定性税”：** 虽然 mHC 约束在小规模下略微限制了表达能力，但对于无约束增长会导致 NaN 的大规模模型来说，它充当了必要的“守恒定律”。
*   **深度扩展：** 随着模型深度的增加，HC 变得越来越不可预测，而 mHC 提供了一种“刚性约束”，确保了数学上的稳定性。

作者总结道，mHC 不仅仅是一个技巧，而是一种具有原则性的架构约束。它在保留并行信息流丰富性的同时，恢复了使原始残差连接取得成功的信号守恒特性。

---

## 7. Show HN：SolidWorks 中的 AI

**原文标题**: Show HN: AI in SolidWorks

**原文链接**: [https://www.trylad.com](https://www.trylad.com)

这篇“Show HN”帖子发布了专为 SolidWorks 设计的 AI 集成工具 1.1.0 版本更新（2026 年 11 月）。此次更新重点在于扩展 AI 的功能，并提升其与 CAD 环境的集成度。

本次发布的核心亮点包括：

*   **新增规划模式：** 旨在帮助用户梳理复杂设计任务结构的功能。
*   **宏自动化：** AI 现在可以编写并执行宏，从而实现更高级的工作流自动化。
*   **草图诊断：** 全新的诊断功能，可检测并报告草图中的问题，简化故障排除流程。
*   **优化：** 改进缓存效率以提升性能。
*   **增强 AI 上下文：** 全面升级 AI 对 SolidWorks 数据的理解能力，并修复了多项漏洞。

总体而言，此次发布旨在推动该工具在 SolidWorks 工作空间内实现更先进、更自主的任务管理和错误检测。

---

## 8. Message Queues: A Simple Guide with Analogies

**原文标题**: Message Queues: A Simple Guide with Analogies

**原文链接**: [https://www.cloudamqp.com/blog/message-queues-exaplined-with-analogies.html](https://www.cloudamqp.com/blog/message-queues-exaplined-with-analogies.html)

生成摘要时出错

---

## 9. Launch a Debugging Terminal into GitHub Actions

**原文标题**: Launch a Debugging Terminal into GitHub Actions

**原文链接**: [https://blog.gripdev.xyz/2026/01/10/actions-terminal-on-failure-for-debugging/](https://blog.gripdev.xyz/2026/01/10/actions-terminal-on-failure-for-debugging/)

生成摘要时出错

---

## 10. How problematic is resampling audio from 44.1 to 48 kHz?

**原文标题**: How problematic is resampling audio from 44.1 to 48 kHz?

**原文链接**: [https://kevinboone.me/sample48.html](https://kevinboone.me/sample48.html)

生成摘要时出错

---

## 11. Lightpanda migrate DOM implementation to Zig

**原文标题**: Lightpanda migrate DOM implementation to Zig

**原文链接**: [https://lightpanda.io/blog/posts/migrating-our-dom-to-zig](https://lightpanda.io/blog/posts/migrating-our-dom-to-zig)

生成摘要时出错

---

## 12. Ai, Japanese chimpanzee who counted and painted dies at 49

**原文标题**: Ai, Japanese chimpanzee who counted and painted dies at 49

**原文链接**: [https://www.bbc.com/news/articles/cj9r3zl2ywyo](https://www.bbc.com/news/articles/cj9r3zl2ywyo)

生成摘要时出错

---

## 13. Show HN: Pane – An agent that edits spreadsheets

**原文标题**: Show HN: Pane – An agent that edits spreadsheets

**原文链接**: [https://paneapp.com](https://paneapp.com)

生成摘要时出错

---

## 14. JRR Tolkien reads from The Hobbit for 30 Minutes (1952)

**原文标题**: JRR Tolkien reads from The Hobbit for 30 Minutes (1952)

**原文链接**: [https://www.openculture.com/2026/01/j-r-r-tolkien-reads-from-the-hobbit-for-30-minutes-1952.html](https://www.openculture.com/2026/01/j-r-r-tolkien-reads-from-the-hobbit-for-30-minutes-1952.html)

生成摘要时出错

---

## 15. Personal thoughts/notes from working on Zootopia 2

**原文标题**: Personal thoughts/notes from working on Zootopia 2

**原文链接**: [https://blog.yiningkarlli.com/2025/12/zootopia-2.html](https://blog.yiningkarlli.com/2025/12/zootopia-2.html)

生成摘要时出错

---

## 16. CLI agents make self-hosting on a home server easier and fun

**原文标题**: CLI agents make self-hosting on a home server easier and fun

**原文链接**: [https://fulghum.io/self-hosting](https://fulghum.io/self-hosting)

生成摘要时出错

---

## 17. The Manchester Garbage Collector and purple-garden's runtime

**原文标题**: The Manchester Garbage Collector and purple-garden's runtime

**原文链接**: [https://xnacly.me/posts/2026/manchester-garbage-collector/](https://xnacly.me/posts/2026/manchester-garbage-collector/)

生成摘要时出错

---

## 18. Zen-C: Write like a high-level language, run like C

**原文标题**: Zen-C: Write like a high-level language, run like C

**原文链接**: [https://github.com/z-libs/Zen-C](https://github.com/z-libs/Zen-C)

生成摘要时出错

---

## 19. 39c3: In-house electronics manufacturing from scratch: How hard can it be? [video]

**原文标题**: 39c3: In-house electronics manufacturing from scratch: How hard can it be? [video]

**原文链接**: [https://media.ccc.de/v/39c3-in-house-electronics-manufacturing-from-scratch-how-hard-can-it-be](https://media.ccc.de/v/39c3-in-house-electronics-manufacturing-from-scratch-how-hard-can-it-be)

生成摘要时出错

---

## 20. History's Attention Gap

**原文标题**: History's Attention Gap

**原文链接**: [https://kidopoly.com/research/attention-gap/](https://kidopoly.com/research/attention-gap/)

生成摘要时出错

---

## 21. Computational complexity of schema-guided document extraction

**原文标题**: Computational complexity of schema-guided document extraction

**原文链接**: [https://www.runpulse.com/blog/computational-complexity-of-schema](https://www.runpulse.com/blog/computational-complexity-of-schema)

生成摘要时出错

---

## 22. Apple picks Google's Gemini to power Siri

**原文标题**: Apple picks Google's Gemini to power Siri

**原文链接**: [https://www.cnbc.com/2026/01/12/apple-google-ai-siri-gemini.html](https://www.cnbc.com/2026/01/12/apple-google-ai-siri-gemini.html)

生成摘要时出错

---

## 23. Ireland fast tracks Bill to criminalise harmful voice or image misuse

**原文标题**: Ireland fast tracks Bill to criminalise harmful voice or image misuse

**原文链接**: [https://www.irishtimes.com/ireland/2026/01/07/call-to-fast-track-bill-targeting-ai-deepfakes-and-identity-hijacking/](https://www.irishtimes.com/ireland/2026/01/07/call-to-fast-track-bill-targeting-ai-deepfakes-and-identity-hijacking/)

生成摘要时出错

---

## 24. iCloud Photos Downloader

**原文标题**: iCloud Photos Downloader

**原文链接**: [https://github.com/icloud-photos-downloader/icloud_photos_downloader](https://github.com/icloud-photos-downloader/icloud_photos_downloader)

生成摘要时出错

---

## 25. Computers that used to be human

**原文标题**: Computers that used to be human

**原文链接**: [https://digitalseams.com/blog/computers-that-used-to-be-human](https://digitalseams.com/blog/computers-that-used-to-be-human)

生成摘要时出错

---

## 26. This game is a single 13 KiB file that runs on Windows, Linux and in the Browser

**原文标题**: This game is a single 13 KiB file that runs on Windows, Linux and in the Browser

**原文链接**: [https://iczelia.net/posts/snake-polyglot/](https://iczelia.net/posts/snake-polyglot/)

生成摘要时出错

---

## 27. Keychron's Nape Pro turns your keyboard into a laptop‑style trackball rig

**原文标题**: Keychron's Nape Pro turns your keyboard into a laptop‑style trackball rig

**原文链接**: [https://www.yankodesign.com/2026/01/08/keychrons-nape-pro-turns-your-mechanical-keyboard-into-a-laptop-style-trackball-rig-hands-on-at-ces-2026/](https://www.yankodesign.com/2026/01/08/keychrons-nape-pro-turns-your-mechanical-keyboard-into-a-laptop-style-trackball-rig-hands-on-at-ces-2026/)

生成摘要时出错

---

## 28. Statement from Federal Reserve Chair

**原文标题**: Statement from Federal Reserve Chair

**原文链接**: [https://www.federalreserve.gov/newsevents/speech/powell20260111a.htm?mod=ANLink](https://www.federalreserve.gov/newsevents/speech/powell20260111a.htm?mod=ANLink)

生成摘要时出错

---

## 29. Windows 8 Desktop Environment for Linux

**原文标题**: Windows 8 Desktop Environment for Linux

**原文链接**: [https://github.com/er-bharat/Win8DE](https://github.com/er-bharat/Win8DE)

生成摘要时出错

---

## 30. Open-Meteo is a free and open-source weather API for non-commercial use

**原文标题**: Open-Meteo is a free and open-source weather API for non-commercial use

**原文链接**: [https://open-meteo.com/](https://open-meteo.com/)

生成摘要时出错

---

## 31. XMPP and Metadata

**原文标题**: XMPP and Metadata

**原文链接**: [https://blog.mathieui.net/xmpp-and-metadata.html](https://blog.mathieui.net/xmpp-and-metadata.html)

生成摘要时出错

---

## 32. Conbini Wars – Map of Japanese convenience store ratios

**原文标题**: Conbini Wars – Map of Japanese convenience store ratios

**原文链接**: [https://conbini.kikkia.dev/](https://conbini.kikkia.dev/)

生成摘要时出错

---

## 33. I'm making a game engine based on dynamic signed distance fields (SDFs) [video]

**原文标题**: I'm making a game engine based on dynamic signed distance fields (SDFs) [video]

**原文链接**: [https://www.youtube.com/watch?v=il-TXbn5iMA](https://www.youtube.com/watch?v=il-TXbn5iMA)

生成摘要时出错

---

## 34. The next two years of software engineering

**原文标题**: The next two years of software engineering

**原文链接**: [https://addyosmani.com/blog/next-two-years/](https://addyosmani.com/blog/next-two-years/)

生成摘要时出错

---

## 35. Perfectly Replicating Coca Cola [video]

**原文标题**: Perfectly Replicating Coca Cola [video]

**原文链接**: [https://www.youtube.com/watch?v=TDkH3EbWTYc](https://www.youtube.com/watch?v=TDkH3EbWTYc)

生成摘要时出错

---

## 36. Uncrossy

**原文标题**: Uncrossy

**原文链接**: [https://uncrossy.com/](https://uncrossy.com/)

生成摘要时出错

---

## 37. FUSE is All You Need – Giving agents access to anything via filesystems

**原文标题**: FUSE is All You Need – Giving agents access to anything via filesystems

**原文链接**: [https://jakobemmerling.de/posts/fuse-is-all-you-need/](https://jakobemmerling.de/posts/fuse-is-all-you-need/)

生成摘要时出错

---

## 38. Ozempic reduced grocery spending by an average of 5.3% in the US

**原文标题**: Ozempic reduced grocery spending by an average of 5.3% in the US

**原文链接**: [https://news.cornell.edu/stories/2025/12/ozempic-changing-foods-americans-buy](https://news.cornell.edu/stories/2025/12/ozempic-changing-foods-americans-buy)

生成摘要时出错

---

## 39. Framework: Memory and Storage Pricing Updates

**原文标题**: Framework: Memory and Storage Pricing Updates

**原文链接**: [https://frame.work/at/en/blog/in-stock-on-framework-desktop-and-updates-on-the-industry-wide-silicon-crunch](https://frame.work/at/en/blog/in-stock-on-framework-desktop-and-updates-on-the-industry-wide-silicon-crunch)

生成摘要时出错

---

## 40. Zorgdomein Integration: A Guide to Secure .NET and Azure Architecture

**原文标题**: Zorgdomein Integration: A Guide to Secure .NET and Azure Architecture

**原文链接**: [https://plakhlani.in/healthcare/bidirectional-patient-data-exchange-with-zorgdomein/](https://plakhlani.in/healthcare/bidirectional-patient-data-exchange-with-zorgdomein/)

生成摘要时出错

---

## 41. Apple picks Google's Gemini AI for its big Siri upgrade

**原文标题**: Apple picks Google's Gemini AI for its big Siri upgrade

**原文链接**: [https://www.theverge.com/news/860521/apple-siri-google-gemini-ai-personalization](https://www.theverge.com/news/860521/apple-siri-google-gemini-ai-personalization)

生成摘要时出错

---

## 42. Sampling at negative temperature

**原文标题**: Sampling at negative temperature

**原文链接**: [https://cavendishlabs.org/blog/negative-temperature/](https://cavendishlabs.org/blog/negative-temperature/)

生成摘要时出错

---

## 43. Climbing the mountain: or, venturing into PL theory

**原文标题**: Climbing the mountain: or, venturing into PL theory

**原文链接**: [https://techne98.com/blog/climbing-the-mountain/](https://techne98.com/blog/climbing-the-mountain/)

生成摘要时出错

---

## 44. Don't fall into the anti-AI hype

**原文标题**: Don't fall into the anti-AI hype

**原文链接**: [https://antirez.com/news/158](https://antirez.com/news/158)

生成摘要时出错

---

## 45. Insights into Claude Opus 4.5 from Pokémon

**原文标题**: Insights into Claude Opus 4.5 from Pokémon

**原文链接**: [https://www.lesswrong.com/posts/u6Lacc7wx4yYkBQ3r/insights-into-claude-opus-4-5-from-pokemon](https://www.lesswrong.com/posts/u6Lacc7wx4yYkBQ3r/insights-into-claude-opus-4-5-from-pokemon)

生成摘要时出错

---

## 46. Show HN: Shellock, a real-time CLI flag explainer for fish shell

**原文标题**: Show HN: Shellock, a real-time CLI flag explainer for fish shell

**原文链接**: [https://github.com/ibehnam/shellock](https://github.com/ibehnam/shellock)

生成摘要时出错

---

## 47. Erich von Däniken has died

**原文标题**: Erich von Däniken has died

**原文链接**: [https://daniken.com/en/startseite-english/](https://daniken.com/en/startseite-english/)

生成摘要时出错

---

## 48. Elo – A data expression language which compiles to JavaScript, Ruby, and SQL

**原文标题**: Elo – A data expression language which compiles to JavaScript, Ruby, and SQL

**原文链接**: [https://elo-lang.org/](https://elo-lang.org/)

生成摘要时出错

---

## 49. A set of Idiomatic prod-grade katas for experienced devs transitioning to Go

**原文标题**: A set of Idiomatic prod-grade katas for experienced devs transitioning to Go

**原文链接**: [https://github.com/MedUnes/go-kata](https://github.com/MedUnes/go-kata)

生成摘要时出错

---

## 50. Poison Fountain

**原文标题**: Poison Fountain

**原文链接**: [https://rnsaffn.com/poison3/](https://rnsaffn.com/poison3/)

生成摘要时出错

---

## 51. Garbage collection is contrarian

**原文标题**: Garbage collection is contrarian

**原文链接**: [https://trynova.dev/blog/garbage-collection-is-contrarian](https://trynova.dev/blog/garbage-collection-is-contrarian)

生成摘要时出错

---

## 52. Code and Let Live

**原文标题**: Code and Let Live

**原文链接**: [https://fly.io/blog/code-and-let-live/](https://fly.io/blog/code-and-let-live/)

生成摘要时出错

---

## 53. Gadget Exposed a Spy Camera [video]

**原文标题**: Gadget Exposed a Spy Camera [video]

**原文链接**: [https://www.youtube.com/watch?v=1reman2waLs](https://www.youtube.com/watch?v=1reman2waLs)

生成摘要时出错

---

## 54. Palantir Crashes Out in Response to GN [video]

**原文标题**: Palantir Crashes Out in Response to GN [video]

**原文链接**: [https://www.youtube.com/watch?v=5Idb_D4Tdu8](https://www.youtube.com/watch?v=5Idb_D4Tdu8)

生成摘要时出错

---

## 55. Economists are facing a recession as a hiring crunch hits

**原文标题**: Economists are facing a recession as a hiring crunch hits

**原文链接**: [https://www.ft.com/content/eb080c14-e946-4806-ad66-81b2bb8c67ba](https://www.ft.com/content/eb080c14-e946-4806-ad66-81b2bb8c67ba)

生成摘要时出错

---

## 56. Moving Scratch generation to Python on browser

**原文标题**: Moving Scratch generation to Python on browser

**原文链接**: [https://kushaldas.in/posts/introducing-ektupy.html](https://kushaldas.in/posts/introducing-ektupy.html)

生成摘要时出错

---

## 57. Show HN: An LLM-optimized programming language

**原文标题**: Show HN: An LLM-optimized programming language

**原文链接**: [https://github.com/ImJasonH/ImJasonH/blob/main/articles/llm-programming-language.md](https://github.com/ImJasonH/ImJasonH/blob/main/articles/llm-programming-language.md)

生成摘要时出错

---

## 58. My Home Fibre Network Disintegrated

**原文标题**: My Home Fibre Network Disintegrated

**原文链接**: [https://alienchow.dev/post/fibre_disintegration/](https://alienchow.dev/post/fibre_disintegration/)

生成摘要时出错

---

## 59. Code is cheap now, but software isn't

**原文标题**: Code is cheap now, but software isn't

**原文链接**: [https://www.chrisgregori.dev/opinion/code-is-cheap-now-software-isnt](https://www.chrisgregori.dev/opinion/code-is-cheap-now-software-isnt)

生成摘要时出错

---

## 60. China applies to put 200K satellites in space after calling Starlink crash risk

**原文标题**: China applies to put 200K satellites in space after calling Starlink crash risk

**原文链接**: [https://www.scmp.com/news/china/science/article/3339493/china-applies-put-200000-satellites-space-after-calling-starlink-crash-risk](https://www.scmp.com/news/china/science/article/3339493/china-applies-put-200000-satellites-space-after-calling-starlink-crash-risk)

生成摘要时出错

---

## 61. I'd tell you a UDP joke…

**原文标题**: I'd tell you a UDP joke…

**原文链接**: [https://www.codepuns.com/post/805294580859879424/i-would-tell-you-a-udp-joke-but-you-might-not-get](https://www.codepuns.com/post/805294580859879424/i-would-tell-you-a-udp-joke-but-you-might-not-get)

生成摘要时出错

---

## 62. You are not required to close your <p>, <li>, <img>, or <br> tags in HTML

**原文标题**: You are not required to close your <p>, <li>, <img>, or <br> tags in HTML

**原文链接**: [https://blog.novalistic.com/archives/2017/08/optional-end-tags-in-html/](https://blog.novalistic.com/archives/2017/08/optional-end-tags-in-html/)

生成摘要时出错

---

## 63. Himalayas bare and rocky after reduced winter snowfall, scientists warn

**原文标题**: Himalayas bare and rocky after reduced winter snowfall, scientists warn

**原文链接**: [https://www.bbc.com/news/articles/clyndv7zd20o](https://www.bbc.com/news/articles/clyndv7zd20o)

生成摘要时出错

---

## 64. Gentoo Linux 2025 Review

**原文标题**: Gentoo Linux 2025 Review

**原文链接**: [https://www.gentoo.org/news/2026/01/05/new-year.html](https://www.gentoo.org/news/2026/01/05/new-year.html)

生成摘要时出错

---

## 65. Quake 1 Single-Player Map Design Theories (2001)

**原文标题**: Quake 1 Single-Player Map Design Theories (2001)

**原文链接**: [https://www.quaddicted.com/webarchive//teamshambler.planetquake.gamespy.com/theories1.html](https://www.quaddicted.com/webarchive//teamshambler.planetquake.gamespy.com/theories1.html)

生成摘要时出错

---

## 66. Show HN: stream-unzip – Python function to unZIP on the fly

**原文标题**: Show HN: stream-unzip – Python function to unZIP on the fly

**原文链接**: [https://github.com/uktrade/stream-unzip](https://github.com/uktrade/stream-unzip)

生成摘要时出错

---

## 67. 2025 marked a record-breaking year for Apple services

**原文标题**: 2025 marked a record-breaking year for Apple services

**原文链接**: [https://www.apple.com/newsroom/2026/01/2025-marked-a-record-breaking-year-for-apple-services/](https://www.apple.com/newsroom/2026/01/2025-marked-a-record-breaking-year-for-apple-services/)

生成摘要时出错

---

## 68. Vojtux – Unofficial Linux Distribution Aimed at Visually Impaired Users

**原文标题**: Vojtux – Unofficial Linux Distribution Aimed at Visually Impaired Users

**原文链接**: [https://github.com/vojtapolasek/vojtux](https://github.com/vojtapolasek/vojtux)

生成摘要时出错

---

## 69. Happy 50th Birthday KIM-1

**原文标题**: Happy 50th Birthday KIM-1

**原文链接**: [https://github.com/netzherpes/KIM1-Demo](https://github.com/netzherpes/KIM1-Demo)

生成摘要时出错

---

## 70. BYD's cheapest electric cars to have Lidar self-driving tech

**原文标题**: BYD's cheapest electric cars to have Lidar self-driving tech

**原文链接**: [https://thedriven.io/2026/01/11/byds-cheapest-electric-cars-to-have-lidar-self-driving-tech/](https://thedriven.io/2026/01/11/byds-cheapest-electric-cars-to-have-lidar-self-driving-tech/)

生成摘要时出错

---

## 71. BasiliskII Macintosh 68k Emulator Ported to ESP32-P4 / M5Stack Tab5

**原文标题**: BasiliskII Macintosh 68k Emulator Ported to ESP32-P4 / M5Stack Tab5

**原文链接**: [https://github.com/amcchord/M5Tab-Macintosh](https://github.com/amcchord/M5Tab-Macintosh)

生成摘要时出错

---

## 72. Xfce is great

**原文标题**: Xfce is great

**原文链接**: [https://rubenerd.com/xfce-is-great/](https://rubenerd.com/xfce-is-great/)

生成摘要时出错

---

## 73. Anthropic: Developing a Claude Code competitor using Claude Code is banned

**原文标题**: Anthropic: Developing a Claude Code competitor using Claude Code is banned

**原文链接**: [https://twitter.com/SIGKITTEN/status/2009697031422652461](https://twitter.com/SIGKITTEN/status/2009697031422652461)

生成摘要时出错

---

## 74. HTML-only conditional lazy loading (via preload and media)

**原文标题**: HTML-only conditional lazy loading (via preload and media)

**原文链接**: [https://orga.cat/blog/html-conditional-lazy-loading/](https://orga.cat/blog/html-conditional-lazy-loading/)

生成摘要时出错

---

## 75. Fossil versus Git

**原文标题**: Fossil versus Git

**原文链接**: [https://fossil-scm.org/home/doc/trunk/www/fossil-v-git.wiki](https://fossil-scm.org/home/doc/trunk/www/fossil-v-git.wiki)

生成摘要时出错

---

## 76. Most devs don't trust AI-generated code, but fail to check it anyway

**原文标题**: Most devs don't trust AI-generated code, but fail to check it anyway

**原文链接**: [https://www.theregister.com/2026/01/09/devs_ai_code/](https://www.theregister.com/2026/01/09/devs_ai_code/)

生成摘要时出错

---

## 77. Iran is likely jamming Starlink

**原文标题**: Iran is likely jamming Starlink

**原文链接**: [https://www.timesofisrael.com/iran-appears-to-jam-starlink-after-shutting-down-comms-networks/](https://www.timesofisrael.com/iran-appears-to-jam-starlink-after-shutting-down-comms-networks/)

生成摘要时出错

---

## 78. Max Payne – two decades later – Graphics Critique (2021)

**原文标题**: Max Payne – two decades later – Graphics Critique (2021)

**原文链接**: [https://darkcephas.blogspot.com/2021/07/max-payne-two-decades-later-graphics.html](https://darkcephas.blogspot.com/2021/07/max-payne-two-decades-later-graphics.html)

生成摘要时出错

---

## 79. I Cannot SSH into My Server Anymore (and That's Fine)

**原文标题**: I Cannot SSH into My Server Anymore (and That's Fine)

**原文链接**: [https://soap.coffee/~lthms/posts/i-cannot-ssh-into-my-server-anymore.html](https://soap.coffee/~lthms/posts/i-cannot-ssh-into-my-server-anymore.html)

生成摘要时出错

---

## 80. Show HN: 30k IKEA items in flat text

**原文标题**: Show HN: 30k IKEA items in flat text

**原文链接**: [https://huggingface.co/datasets/tsazan/ikea-us-commercetxt](https://huggingface.co/datasets/tsazan/ikea-us-commercetxt)

生成摘要时出错

---

## 81. Official TypeScript Cheat Sheets

**原文标题**: Official TypeScript Cheat Sheets

**原文链接**: [https://www.typescriptlang.org/cheatsheets/](https://www.typescriptlang.org/cheatsheets/)

生成摘要时出错

---

## 82. Anthropic made a big mistake

**原文标题**: Anthropic made a big mistake

**原文链接**: [https://archaeologist.dev/artifacts/anthropic](https://archaeologist.dev/artifacts/anthropic)

生成摘要时出错

---

## 83. Rare Iron Age war trumpet and boar standard found

**原文标题**: Rare Iron Age war trumpet and boar standard found

**原文链接**: [https://www.bbc.com/news/articles/cr7jvj8d39eo](https://www.bbc.com/news/articles/cr7jvj8d39eo)

生成摘要时出错

---

## 84. “Food JPEGs” in Super Smash Bros. and Kirby Air Riders

**原文标题**: “Food JPEGs” in Super Smash Bros. and Kirby Air Riders

**原文链接**: [https://sethmlarson.dev/food-jpegs-in-super-smash-bros-and-kirby-air-riders](https://sethmlarson.dev/food-jpegs-in-super-smash-bros-and-kirby-air-riders)

生成摘要时出错

---

## 85. More than one hundred years of Film Sizes

**原文标题**: More than one hundred years of Film Sizes

**原文链接**: [https://wichm.home.xs4all.nl/filmsize.html](https://wichm.home.xs4all.nl/filmsize.html)

生成摘要时出错

---

## 86. KaraDAV – Lightweight Nextcloud compatible WebDAV server

**原文标题**: KaraDAV – Lightweight Nextcloud compatible WebDAV server

**原文链接**: [https://github.com/kd2org/karadav](https://github.com/kd2org/karadav)

生成摘要时出错

---

## 87. C++ std::move doesn't move anything: A deep dive into Value Categories

**原文标题**: C++ std::move doesn't move anything: A deep dive into Value Categories

**原文链接**: [https://0xghost.dev/blog/std-move-deep-dive/](https://0xghost.dev/blog/std-move-deep-dive/)

生成摘要时出错

---

## 88. How to code Claude Code in 200 lines of code

**原文标题**: How to code Claude Code in 200 lines of code

**原文链接**: [https://www.mihaileric.com/The-Emperor-Has-No-Clothes/](https://www.mihaileric.com/The-Emperor-Has-No-Clothes/)

生成摘要时出错

---

## 89. Finding and fixing Ghostty's largest memory leak

**原文标题**: Finding and fixing Ghostty's largest memory leak

**原文链接**: [https://mitchellh.com/writing/ghostty-memory-leak-fix](https://mitchellh.com/writing/ghostty-memory-leak-fix)

生成摘要时出错

---

## 90. I dumped Windows 11 for Linux, and you should too

**原文标题**: I dumped Windows 11 for Linux, and you should too

**原文链接**: [https://www.notebookcheck.net/I-dumped-Windows-11-for-Linux-and-you-should-too.1190961.0.html](https://www.notebookcheck.net/I-dumped-Windows-11-for-Linux-and-you-should-too.1190961.0.html)

生成摘要时出错

---

## 91. Instagram data breach reportedly exposed the personal info of 17.5M users

**原文标题**: Instagram data breach reportedly exposed the personal info of 17.5M users

**原文链接**: [https://www.engadget.com/cybersecurity/an-instagram-data-breach-reportedly-exposed-the-personal-info-of-175-million-users-192105616.html](https://www.engadget.com/cybersecurity/an-instagram-data-breach-reportedly-exposed-the-personal-info-of-175-million-users-192105616.html)

生成摘要时出错

---

## 92. Which programming languages are most token-efficient?

**原文标题**: Which programming languages are most token-efficient?

**原文链接**: [https://martinalderson.com/posts/which-programming-languages-are-most-token-efficient/](https://martinalderson.com/posts/which-programming-languages-are-most-token-efficient/)

生成摘要时出错

---

## 93. iMessage-kit is an iMessage SDK for macOS

**原文标题**: iMessage-kit is an iMessage SDK for macOS

**原文链接**: [https://github.com/photon-hq/imessage-kit](https://github.com/photon-hq/imessage-kit)

生成摘要时出错

---

## 94. "There Are Two Possible Futures for American Science."

**原文标题**: "There Are Two Possible Futures for American Science."

**原文链接**: [https://issues.org/american-science-simons-spergel-interview/](https://issues.org/american-science-simons-spergel-interview/)

生成摘要时出错

---

## 95. Show HN: I used Claude Code to discover connections between 100 books

**原文标题**: Show HN: I used Claude Code to discover connections between 100 books

**原文链接**: [https://trails.pieterma.es/](https://trails.pieterma.es/)

生成摘要时出错

---

## 96. Musk: We will make the new X algorithm open source in 7 days

**原文标题**: Musk: We will make the new X algorithm open source in 7 days

**原文链接**: [https://twitter.com/elonmusk/status/2010062264976736482](https://twitter.com/elonmusk/status/2010062264976736482)

生成摘要时出错

---

## 97. ASCII-Driven Development

**原文标题**: ASCII-Driven Development

**原文链接**: [https://medium.com/@calufa/ascii-driven-development-850f66661351](https://medium.com/@calufa/ascii-driven-development-850f66661351)

生成摘要时出错

---

## 98. The Concise TypeScript Book

**原文标题**: The Concise TypeScript Book

**原文链接**: [https://github.com/gibbok/typescript-book](https://github.com/gibbok/typescript-book)

生成摘要时出错

---

## 99. Statement from Jerome Powell

**原文标题**: Statement from Jerome Powell

**原文链接**: [https://www.federalreserve.gov/newsevents/speech/powell20260111a.htm](https://www.federalreserve.gov/newsevents/speech/powell20260111a.htm)

生成摘要时出错

---

## 100. The Taming of Collection Scans

**原文标题**: The Taming of Collection Scans

**原文链接**: [https://www.scylladb.com/2026/01/06/the-taming-of-collection-scans/](https://www.scylladb.com/2026/01/06/the-taming-of-collection-scans/)

生成摘要时出错

---

