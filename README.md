# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-01-12.md)

*最后自动更新时间: 2026-01-12 17:52:54*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 2 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 3 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 4 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 5 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 6 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 7 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 8 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 9 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 10 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 11 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 12 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 13 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 14 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 15 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 16 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 17 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 18 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 19 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 20 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 21 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 22 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 23 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 24 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 25 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 26 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 27 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 28 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 29 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 30 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 31 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 32 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 33 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 34 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 35 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 36 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 37 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 38 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 39 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 40 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 41 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 42 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 43 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 44 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 45 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 46 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 47 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 48 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 49 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 50 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 51 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 52 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 53 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 54 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 55 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 56 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 57 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 58 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 59 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 60 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 61 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 62 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 63 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 64 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 65 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 66 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 67 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 68 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 69 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 70 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 71 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 72 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 73 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 74 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 75 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 76 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 77 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 78 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 79 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 80 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 81 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 82 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 83 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 84 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 85 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 86 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 87 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 88 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 89 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 90 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 91 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 92 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 93 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 94 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 95 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 96 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 97 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 98 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 99 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 100 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 101 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 102 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 103 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 104 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 105 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 106 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 107 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 108 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 109 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 110 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 111 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 112 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 113 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 114 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 115 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 116 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 117 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 118 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 119 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 120 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 121 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 122 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 123 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 124 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 125 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 126 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 127 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 128 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 129 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 130 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 131 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 132 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 133 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 134 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 135 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 136 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 137 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 138 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 139 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 140 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 141 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 142 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 143 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 144 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 145 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 146 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 147 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 148 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 149 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 150 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 151 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 152 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 153 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 154 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 155 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 156 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 157 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 158 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 159 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 160 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 161 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 162 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 163 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 164 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 165 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 166 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 167 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 168 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 169 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 170 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 171 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 172 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 173 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 174 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 175 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 176 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 177 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 178 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 179 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 180 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 181 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 182 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 183 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 184 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 185 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 186 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 187 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 188 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 189 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 190 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 191 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 192 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 193 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 194 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 195 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 196 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 197 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 198 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 199 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 200 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 201 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 202 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 203 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 204 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 205 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 206 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 207 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 208 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 209 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 210 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 211 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 212 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 213 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 214 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 215 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 216 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 217 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 218 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 219 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 220 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 221 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 222 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 223 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 224 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 225 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 226 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 227 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 228 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 229 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 230 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 231 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 232 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 233 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 234 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 235 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 236 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 237 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 238 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 239 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 240 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 241 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 242 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 243 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 244 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 245 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 246 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 247 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 248 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 249 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 250 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 251 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 252 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 253 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 254 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 255 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 256 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 257 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 258 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 259 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 260 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 261 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 262 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 263 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 264 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 265 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 266 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 267 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 268 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 269 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 270 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 271 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 272 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 273 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 274 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 275 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 276 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 277 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 278 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 279 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 280 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 281 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 282 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 283 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 284 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 285 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 286 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 287 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 288 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 289 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 290 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 291 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 292 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 293 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 294 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 295 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 296 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 297 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 298 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
