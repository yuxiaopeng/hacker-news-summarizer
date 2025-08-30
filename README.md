# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-08-30.md)

*最后自动更新时间: 2025-08-30 17:43:33*
## 1. 认知负荷至关重要

**原文标题**: Cognitive Load is what matters

**原文链接**: [https://github.com/zakirullin/cognitive-load](https://github.com/zakirullin/cognitive-load)

本文认为，**认知负荷**是影响代码可维护性和开发者生产力的一个基本因素，但它常常被忽视，取而代之的是流行但有时具有误导性的最佳实践。认知负荷是指理解和使用代码所需的脑力，过高的认知负荷会导致困惑、浪费时间和成本增加。

本文区分了两种类型的认知负荷：内在认知负荷（任务固有的难度）和外在认知负荷（由呈现方式和不必要的复杂性引起的）。重点是减少**外在认知负荷**。

几个代码示例说明了某些实践如何增加认知负荷，包括：

*   **复杂条件语句：** 使用冗长、嵌套的条件语句。 解决方案：引入具有意义名称的中间变量。
*   **嵌套 If 语句：** 深度嵌套的 if 语句。 解决方案：对前提条件使用提前返回，重点关注“happy path”。
*   **继承噩梦：** 深度继承层次结构。 解决方案：优先使用组合而不是继承。
*   **过多的小方法/微服务：** 导致复杂的交互和精神疲惫。 解决方案：目标是具有简单接口的深度模块/宏服务，封装复杂性。
*   **功能丰富的语言：** 避免仅仅因为可用而过度使用语言功能。 解决方案：限制选择的数量。
*   **业务逻辑和 HTTP 状态码：** 避免将业务逻辑编码到标准化的返回代码中。 解决方案：首选使用自描述代码。

本文强调，目标不一定是教条地遵循“小函数”或“单一职责”等严格规则。 相反，应优先考虑减少理解和修改代码所需的脑力。一个模块应该对一个利益相关者负责，而不是只做一件事。 最后，本文鼓励读者批判性地思考其设计决策的认知影响，并减少不必要的复杂性。

---

## 2. 秃鹰Cuzco RISC-V核心亮相2025年Hot Chips大会

**原文标题**: Condor's Cuzco RISC-V Core at Hot Chips 2025

**原文链接**: [https://chipsandcheese.com/p/condors-cuzco-risc-v-core-at-hot](https://chipsandcheese.com/p/condors-cuzco-risc-v-core-at-hot)

本文预览秃鹰计算（Condor Computing）的Cuzco RISC-V内核，这是一款高性能设计，将于2025年Hot Chips大会上展示。秃鹰计算是晶心科技（Andes Technology）的子公司，旨在可授权RISC-V内核市场与Arm和SiFive等公司竞争。

Cuzco内核是一款8路乱序设计，目标是在台积电5nm工艺上实现2-2.5 GHz的频率。一个关键特性是其“基于时间”的调度方案，其中重命名/分配阶段使用时间资源矩阵（TRM）来跟踪资源利用率，从而预测指令调度。这简化了后端调度，降低了功耗和复杂性。TRM方法允许静态调度，并使用重放机制来处理诸如缓存未命中之类的可变延迟操作。

该内核拥有一个复杂的前端，配备了TAGE-SC-L分支预测器和一个分层分支目标缓冲器（BTB）。它包括L2 TLB大小和L2/L3缓存容量等可配置选项。Cuzco内核以最多八个的集群排列，通过CHI总线连接以实现可扩展性。

乱序后端使用执行切片，每个切片都有一对可以执行所有受支持的RISC-V指令的流水线。在向量方面，Cuzco支持256/512位的VLEN。加载/存储单元具有一个64条目的加载队列、存储队列和数据缓存未命中队列，以及一个PIPT L1D缓存。它具有一个64条目的全相联数据TLB。L3缓存被切片以处理带宽需求，并可以64B/周期的加载带宽访问。

本文强调了秃鹰计算在已建立的乱序执行模型中进行创新的方法，旨在在性能和功耗效率之间取得平衡，而无需ISA更改或专用编译器。

---

## 3. AI模型需要虚拟机

**原文标题**: AI models need a virtual machine

**原文链接**: [https://blog.sigplan.org/2025/08/29/ai-models-need-a-virtual-machine/](https://blog.sigplan.org/2025/08/29/ai-models-need-a-virtual-machine/)

本文倡导开发一个标准化的“AI模型虚拟机”（MVM），以提高AI应用程序的安全性、可靠性和可移植性。随着AI模型越来越融入软件，与其交互的控制软件也日益复杂。作者提出，应将此软件层视为虚拟机，包含模型交互、工具访问和内存管理的指令。

MVM从Java虚拟机中汲取灵感，将强制执行安全策略、隔离模型并实现“一次编写，随处运行”的执行效果。这种关注点分离将允许轻松更换模型，并独立改进虚拟机的性能和安全性。

本文重点介绍了现有的工作，如OpenAI的结构化工具调用、Anthropic的模型上下文协议（MCP）以及FIDES和AC4A等强制执行运行时安全控制的项目。Langchain和Semantic Kernel等开源代理运行时也相关。虚拟机规范需要考虑训练数据以及协议和API。

一个精心设计的MVM的关键优势包括：

*   **关注点分离：** 可互换的模型和独立的虚拟机改进。
*   **内置的安全和治理：** 权限检查、审计日志和故障保护，以控制模型行为。
*   **透明的性能和资源跟踪：** 模型性能和资源消耗的可视性。
*   **模型输出的可验证性：** 用于验证模型行为的形式化方法的潜在集成。

作者得出结论，标准化的MVM对于解决构建强大AI软件的工程挑战，并解锁互操作性、安全性和信任至关重要。

---

## 4. 代理客户端协议

**原文标题**: Agent Client Protocol

**原文链接**: [https://agentclientprotocol.com/overview/introduction](https://agentclientprotocol.com/overview/introduction)

智能代理客户端协议 (ACP) 旨在标准化代码编辑器（IDE、文本编辑器）和 AI 编码代理之间的通信。目前正在开发中，它解决了编辑器和代理之间紧密耦合和互操作性有限的问题，即每个编辑器都需要定制集成才能兼容。

ACP 的主要优势包括减少集成开销、扩大编辑器和代理之间的兼容性以及消除开发者锁定。通过提供类似于语言服务器协议 (LSP) 的标准化协议，ACP 允许代理与任何兼容的编辑器一起工作，反之亦然。这种解耦促进了独立创新和用户选择。

该协议假设用户主要在其编辑器中，并希望利用代理来获得帮助。代理作为代码编辑器的子进程运行，并使用基于 stdio 的 JSON-RPC 进行通信。它在适用的情况下重用 MCP 中的 JSON 表示，并包含用于代理编码 UX 的自定义类型。Markdown 是用户可读文本的默认格式。

目前，Zed 和 neovim（通过 CodeCompanion 插件）是受支持的编辑器，而 Gemini 是受支持的代理，预计会有更多后续支持。

---

## 5. 新的解读认为“热寂”假说可能不成立（2023）

**原文标题**: New interpretations suggest the "heat death" hypothesis might not hold (2023)

**原文链接**: [https://www.noemamag.com/life-need-not-ever-end/](https://www.noemamag.com/life-need-not-ever-end/)

本文挑战了“热寂”假说，即宇宙不可避免地退化为最大熵和无序状态，导致所有生命和组织终结的观点。文章认为，对热力学定律，特别是第二定律的新解释，表明情况可能并非如此。

第二定律的传统观点认为，在一个封闭系统中，熵（无序）会随着时间的推移而增加，暗示着宇宙的黯淡未来。然而，文章指出，由于暗能量驱动的持续膨胀，宇宙可能并非一个封闭系统。

包括塞思·劳埃德、埃里克·蔡松和弗里曼·戴森在内的几位科学家被引述，他们质疑宇宙中的“无序”是否真的在增加。他们提出，在物理定律和进化动力学的驱动下，宇宙正在变得越来越复杂和有组织。

文章重点介绍了朱利安·巴伯的著作《雅努斯点》，该书认为，广为流传的第二定律并不适用于膨胀的宇宙。大卫·多伊奇也认为，知识创造没有根本的限制，这意味着生命不一定非要结束。

文章深入探讨了热力学的历史，追溯了其起源于萨迪·卡诺关于蒸汽机的工作。它解释了第二定律的经典和统计解释，并强调这些定律是在发现宇宙膨胀之前构想出来的。

最终，文章表明，在宇宙的故事中，智慧生命通过创造更多的复杂性和维持组织来对抗无序的趋势，从而发挥着关键作用。在一个无限膨胀的宇宙中，生命构建复杂秩序的能力可能不会像曾经认为的那样受到热力学定律的限制。

---

## 6. V编程语言

**原文标题**: The V Programming Language

**原文链接**: [https://vlang.io/](https://vlang.io/)

V 是一种简单、快速、安全且编译型的编程语言，旨在开发可维护的软件。主要特性包括：

*   **简单性和可读性：** 易于学习，关键词数量少，并通过 `vfmt` 强制执行一致的编码风格。Go 开发者会对 V 的语法感到熟悉。
*   **安全性：** 边界检查、默认不可变变量、强制性错误检查以及无未定义行为等特性增强了代码的可靠性。
*   **性能：** V 编译为原生二进制文件，并且可以与 C 代码互操作，而不会产生性能开销。它拥有极快的编译速度（8 万-40 万行代码/秒）。
*   **灵活的内存管理：** 提供多种内存管理策略选择：追踪 GC、自动释放（实验性）、手动管理和 Arena 分配。
*   **C 语言** 可以将整个 C 项目翻译成 V，从而利用其安全性和编译速度的优势。C++ 翻译尚处于早期阶段。
*   **跨平台开发：** 使用 `v -os windows` 等命令简化交叉编译。
*   **轻量级和无依赖：** 生成不含外部依赖的自包含二进制文件。
*   **GUI 开发：** 提供 V UI 库，用于构建原生跨平台 UI 应用程序。
*   **社区支持：** 不断增长的社区以及来自开发者的积极反馈突显了其易用性和生产力。

该语言旨在通过改进 Go 等语言的功能，提供高效且愉快的开发体验。

---

## 7. 做能用的最简单的事情。

**原文标题**: Do the simplest thing that could possibly work

**原文链接**: [https://www.seangoedecke.com/the-simplest-thing-that-could-possibly-work/](https://www.seangoedecke.com/the-simplest-thing-that-could-possibly-work/)

本文倡导在软件设计中优先考虑简洁，即“做最简单可行的事”。 文章反对为假想的未来需求过度设计系统，并强调在添加不必要的复杂性之前，要深刻理解当前系统。

作者认为，软件设计的精髓在于懂得何时少做，从而产生看似平淡但非常有效的解决方案。 他们以 Unicorn 和 Rails REST API 为例，说明通过简单方法实现重要保障的设计。

文章承认这种方法可能面临的批评，即创建缺乏灵活性的系统或“大泥球”，定义简洁的真正含义，以及无法构建可扩展的系统。 作者认为，权宜之计并非简单，而是增加复杂性。 他们将简洁定义为更少的活动部件和更少的内部连接，偏爱需要更少持续维护的稳定解决方案。

关于可扩展性，作者反对为未来的规模进行过早的优化，声称这通常会导致缺乏灵活性和不必要的复杂性。 他们建议专注于满足当前的需求并逐步扩展。 最终，作者认为，深刻理解当前系统对于良好的设计至关重要，并且努力追求简洁可以产生更易于维护和适应性更强的软件。

---

## 8. 从多头到隐注意力：注意力机制的演变

**原文标题**: From Multi-Head to Latent Attention: The Evolution of Attention Mechanisms

**原文链接**: [https://vinithavn.medium.com/from-multi-head-to-latent-attention-the-evolution-of-attention-mechanisms-64e3c0505f24](https://vinithavn.medium.com/from-multi-head-to-latent-attention-the-evolution-of-attention-mechanisms-64e3c0505f24)

本文追溯了神经网络中注意力机制的演变，重点关注它们在处理序列数据时通过选择性地关注相关上下文所发挥的作用。文章首先解释了注意力的核心概念：查询（Q）、键（K）、值（V）和注意力分数，强调它们在创建上下文感知表示中的应用，以及KV缓存对于效率的重要性。

接下来，文章详细介绍了不同注意力机制的发展，从多头注意力（MHA）开始，它使用多个并行注意力“头”，但随着上下文长度的增长，会遭受二次计算复杂度。多查询注意力（MQA）通过在多个查询头之间共享键和值向量来解决这个问题，从而减少了内存开销。分组查询注意力（GQA）通过将查询头分成组，每组共享键和值向量，从而在MHA和MQA之间取得了平衡。

最后，文章介绍了多头潜在注意力（MHLA），这是Deepseek等模型中使用的一项最新创新，它通过使用低秩投影将键和值表示压缩到较低维度的潜在空间中，从而显著减少了内存使用。MHLA旨在实现接近MHA的性能，同时提高推理速度。

文章最后提及了其他先进的注意力机制，如稀疏注意力和记忆增强注意力，强调了正在进行的研究，以提高注意力机制的可扩展性、速度和适应性。

---

## 9. Bcachefs 变为“外部维护”

**原文标题**: Bcachefs Goes to "Externally Maintained"

**原文链接**: [https://lwn.net/Articles/1035736/](https://lwn.net/Articles/1035736/)

这篇来自 LWN.net 2025 年 8 月的文章讨论了 Linux 内核中 bcachefs 维护者状态变更为“外部维护”，这标志着其在主线内核中的未来存在不确定性。虽然预计不会立即移除，但在短期内不太可能进一步整合变更。

文章探讨了这种变更可能出现的潜在情况。一个担忧是，如果新变更未被纳入，树内 bcachefs 代码可能会停滞不前。另一个建议是寻找一位新的维护者，一位更愿意接受内核开发流程的人，作为内核社区和原始开发者 Kent Overstreet 之间的联络人。

Kent Overstreet 表示不愿将维护工作委托给其他 bcachefs 开发者，担心他们会倦怠。他强调自己对稳定性和用户支持的承诺，并以 Debian 的 bcachefs-tools 打包问题为例，说明了发布流程中断可能引发的问题。

评论员 NYKevin 概述了三种可能的长期结果：1) Kent 指定某人以 Linus 的步调向上游推送补丁；2) Kent 脱离，内核最终移除 bcachefs；或者 3) 内核派生出 bcachefs 并维护一个稍旧或修改过的版本。NYKevin 强调，Kent 不再控制出现在主线内核中的内容。

另一位评论员 paravoid 指责 Kent 难以合作，这导致 bcachefs-tools 从 Debian 中移除。Kent 回应称，概述了软件包维护者行为引发的具体技术问题。总而言之，这篇文章突出了将复杂文件系统集成到 Linux 内核中所涉及的复杂治理和人际关系挑战。

---

## 10. 诺基亚的传奇字体是优秀的用户界面字体。

**原文标题**: Nokia’s legendary font makes for a great user interface font

**原文链接**: [https://www.osnews.com/story/143222/it-turns-out-nokias-legendary-font-makes-for-a-great-general-user-interface-font/](https://www.osnews.com/story/143222/it-turns-out-nokias-legendary-font-makes-for-a-great-general-user-interface-font/)

作者发现诺基亚 Sans 字体作为用户界面字体的意外惊喜。怀念 2002 年至 2013 年诺基亚设备上使用的字体，作者下载了各个变体，并在配备高 DPI 显示器的 KDE/Wayland 系统上进行了实验。

他们发现诺基亚 Sans 的“Wide”变体效果非常好，这与诺基亚之前声称它不适合 UI 的说法相反。作者引用了该字体的创作者 Erik Spiekermann 的话，他批评了诺基亚决定用一种平淡的字体取代它。

作者称赞 Nokia Sans Wide 的易读性、个性和整体美感，这使他们用它取代了之前最喜欢的 Inter 字体，作为他们首选的 UI 字体。他们承认字体偏好的主观性，并指出结果可能会因不同的操作系统或较低 DPI 的显示器而异。

文章还探讨了下载和分发字体的法律含义，表明个人非商业用途通常是可以接受的。评论区强化了作者的积极体验，其他人确认了它在 Xfce 等系统上的适用性，并分享了他们自己与诺基亚相关的怀旧之情。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 2 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 3 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 4 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 5 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 6 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 7 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 8 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 9 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 10 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 11 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 12 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 13 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 14 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 15 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 16 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 17 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 18 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 19 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 20 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 21 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 22 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 23 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 24 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 25 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 26 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 27 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 28 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 29 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 30 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 31 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 32 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 33 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 34 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 35 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 36 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 37 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 38 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 39 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 40 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 41 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 42 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 43 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 44 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 45 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 46 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 47 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 48 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 49 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 50 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 51 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 52 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 53 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 54 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 55 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 56 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 57 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 58 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 59 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 60 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 61 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 62 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 63 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 64 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 65 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 66 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 67 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 68 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 69 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 70 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 71 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 72 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 73 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 74 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 75 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 76 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 77 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 78 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 79 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 80 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 81 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 82 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 83 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 84 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 85 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 86 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 87 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 88 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 89 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 90 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 91 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 92 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 93 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 94 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 95 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 96 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 97 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 98 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 99 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 100 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 101 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 102 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 103 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 104 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 105 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 106 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 107 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 108 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 109 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 110 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 111 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 112 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 113 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 114 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 115 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 116 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 117 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 118 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 119 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 120 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 121 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 122 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 123 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 124 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 125 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 126 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 127 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 128 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 129 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 130 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 131 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 132 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 133 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 134 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 135 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 136 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 137 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 138 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 139 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 140 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 141 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 142 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 143 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 144 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 145 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 146 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 147 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 148 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 149 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 150 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 151 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 152 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 153 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 154 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 155 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 156 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 157 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 158 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 159 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 160 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 161 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 162 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 163 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 164 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
