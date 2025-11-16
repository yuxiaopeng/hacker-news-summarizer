# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-11-16.md)

*最后自动更新时间: 2025-11-16 17:45:54*
## 1. 异端：语言模型的自动审查移除

**原文标题**: Heretic: Automatic censorship removal for language models

**原文链接**: [https://github.com/p-e-w/heretic](https://github.com/p-e-w/heretic)

Heretic：一种自动移除Transformer语言模型审查（“安全对齐”）的新型工具。它采用一种高级形式的定向消融，结合参数优化器，来识别“消除”模型内部拒绝方向的最佳设置。此过程抑制模型拒绝有害提示的倾向，同时保留其整体智能。

Heretic的主要特性和优势包括：

*   **自动化：** 无需手动干预或对Transformer内部结构的深入理解。
*   **性能：** 实现了与手动消融模型相当的拒绝抑制效果，同时具有显著更低的KL散度，表明更好地保留了原始模型的能力。
*   **灵活性：** 支持大多数密集模型，包括多模态和MoE架构。
*   **定制性：** 提供各种可配置参数，以便对去审查过程进行细粒度控制。
*   **创新性：** 引入了一种灵活的消融权重核、非积分拒绝方向索引和组件特定的消融参数，以提高性能。

Heretic通过识别并正交化Transformer层内的关键矩阵与从“有害”和“无害”提示之间的差异导出的“拒绝方向”来实现其结果。优化过程平衡了拒绝最小化与模型原始能力保留之间的关系，并通过KL散度来衡量。该软件在GNU Affero通用公共许可证下开源。

---

## 2. 基于FPGA的IBM-PC-XT

**原文标题**: FPGA Based IBM-PC-XT

**原文链接**: [https://bit-hack.net/2025/11/10/fpga-based-ibm-pc-xt/](https://bit-hack.net/2025/11/10/fpga-based-ibm-pc-xt/)

本文详细介绍了一个业余项目，该项目旨在使用正宗零件和现代技术的结合，重现 20 世纪 80 年代的 IBM-PC-XT，目标是完整功能地运行《猴岛小英雄 1》。该项目使用了低功耗的 NEC V20 CPU、1MB SRAM、一个 icesugar-pro FPGA 开发板、PS/2 接口、Micro SD 卡和一个正宗的 YM3014B DAC。

作者使用 EasyEDA 和 JLCPCB 设计了一个定制 PCB，专注于在 FPGA 内重现 XT 的功能。主要挑战包括为 V20 CPU 开发总线控制器，实现将 BIOS 加载到 FPGA 块 RAM 中的内存访问，以及创建一个基本的 CGA 适配器。磁盘访问通过 Verilog SPI 控制器和一个自定义选项 ROM 来处理 INT13H 调用实现。

一个重要的障碍是使用 PS/2 协议实现鼠标支持，这通过在 FPGA 中创建一个 PS/2 到串口鼠标的桥接来解决。这涉及到使用逻辑分析仪分析 PS/2 通信波形。音频功能通过 YM3812 实现（jtopl）并转换输出为 YM3014 DAC 所需的格式来增强。

该项目还包括对 CGA 和 EGA 图形的支持、一个用于文件传输的 USB 到 UART 桥接，以及用于保护的透明亚克力面板。源代码、原理图和 Gerber 文件可在 GitHub 上找到。

---

## 3. 德布鲁因数

**原文标题**: De Bruijn Numerals

**原文链接**: [https://text.marvinborner.de/2023-08-22-22.html](https://text.marvinborner.de/2023-08-22-22.html)

本文介绍了“de Bruijn 数”，这是一种使用嵌套 de Bruijn 索引在纯 lambda 演算中编码自然数的新方法。 该编码将数字 `n` 表示为 `λ^(S(n))n`，其中 `S(n)` 是皮亚诺后继函数。

作者承认 Wadsworth 定理，该定理指出，这种形式的数字系统（抽象的数量无限增加）都不可能是“充分的”，这意味着无法同时定义后继函数、前驱函数和零检查函数。 尽管存在这种限制，本文仍探讨了 de Bruijn 数的潜在效用。

本文介绍了直接对 de Bruijn 数编码进行操作的后继 (`succ`) 函数和前驱 (`pred`) 函数的 lambda 演算实现。 还演示了一个独立的加法函数 (`add`)，展示了该编码在利用 de Bruijn 索引移位方面的优雅性。

作者随后探讨了“混合”方法，将 de Bruijn 数与 Church 数结合使用。 提供了一个从 Church 数到 de Bruijn 数的转换函数。 最后，本文展示了 de Bruijn 数在实现 n 元组的投影方面的实际用途，与传统的 Church 元组表示相比，特别是在元素选择方面，它具有优势。 本文包括元组操作函数（如 push、pop 和 move）的实现，展示了它们在类似堆栈的数据结构中的用处。 这些实现的的代码可以在 bruijn 的标准库中找到。

---

## 4. 硫磺火：用Rust编写的ES2025 JavaScript引擎

**原文标题**: Brimstone: ES2025 JavaScript engine written in Rust

**原文链接**: [https://github.com/Hans-Halverson/brimstone](https://github.com/Hans-Halverson/brimstone)

硫磺石 (Brimstone)：一个力求完全符合 ECMAScript 标准的 Rust 编写的新 JavaScript 引擎。虽然仍在开发中，但它已展现出令人印象深刻的兼容性，通过了超过 97% 的 test262 测试。受到 V8 和 LibJS 的启发，硫磺石 (Brimstone) 基本上是从头构建的，最大限度地减少了依赖关系，除了 ICU4X。

主要特性包括一个模仿 V8 Ignition 的字节码 VM，一个用 unsafe Rust 实现的紧凑型垃圾回收器，一个自定义的 RegExp 引擎和一个自定义的解析器。 大部分内置 JavaScript 对象和函数都已根据 ECMAScript 规范实现。

硫磺石 (Brimstone) 可以使用标准的 Cargo 命令构建和运行。 JavaScript 文件通过编译后的 `bs` 可执行文件直接执行。 测试严重依赖于集成测试，特别是官方的 test262 套件，使用自定义的测试运行器。 单元测试和快照测试也通过 `cargo test` 支持。

该引擎目前支持 ES2024 之前的所有特性，以及截至 2025 年 2 月的所有 stage 4 提案，除了 SharedArrayBuffer 和 Atomics。 该项目尚未准备好投入生产，但展示了在构建完全符合规范的、基于 Rust 的 JavaScript 引擎方面取得的重大进展。

---

## 5. 运行“论信任的信任”编译器

**原文标题**: Running the "Reflections on Trusting Trust" Compiler

**原文链接**: [https://research.swtch.com/nih](https://research.swtch.com/nih)

本文深入探讨了肯·汤普森的图灵奖演讲“论信任信任”，重点介绍了如何对 C 编译器进行后门植入，从而将恶意代码插入到“login”程序中，且不留下源代码痕迹。

本文总结了汤普森的三步法：

1.  **编写自复制程序（Quine）：** 一个可以输出自身源代码的程序。
2.  **编译器学习：** 编译器可以在编译过程中学习到仅存在于二进制文件而非源代码中的细节。
3.  **学习后门：** 教会编译器识别并错误编译特定程序（如“login”），同时教会它将后门插入代码复制到未来的编译器二进制文件中。

作者随后讲述了如何获得汤普森的原始代码（`nih.a`），该代码实现了这项技术，并在 Research Unix 第六版 (V6) 的在线模拟器中演示了其执行过程。代码由两部分组成：`x.c`，一个修改编译器以注入后门的 C 程序；以及 `rc`，一个准备 `x.c` 的 shell 脚本。

`x.c` 修改编译器以：

*   在“login”程序中插入一个后门，以接受特定密码（“codenih”）。
*   插入代码，将自身（特别是 `codenih` 和 `repronih`）复制到后续编译的编译器版本中，从而有效地传播后门。

`rc` 是一个脚本，用于准备 `x.c` 以供编译器使用。本文展示了在 V6 模拟器中运行这些文件的过程，说明了如何创建后门编译器以及它将如何感染后续编译。

---

## 6. AirPods 脱离苹果生态

**原文标题**: AirPods libreated from Apple's ecosystem

**原文链接**: [https://github.com/kavishdevar/librepods](https://github.com/kavishdevar/librepods)

LibrePods 旨在解锁 Apple AirPods 在非 Apple 设备（特别是 Android 和 Linux）上的全部潜力。它使您能够访问通常锁定在 Apple 生态系统中的功能，例如噪声控制模式、入耳检测、电池状态和助听器功能。

该项目为不同的 AirPods 型号提供不同级别的支持，其中 AirPods Pro 2 代获得完全支持。虽然其他型号应提供基本功能，但由于测试有限，不能保证完全兼容。

主要功能包括可定制的噪声控制、用于音乐控制的自动入耳检测、准确的电池监控，甚至还有一些实验性功能，如头部手势和对话感知。在 Android 上，由于蓝牙堆栈问题，该项目需要具有 Xposed 的 root 设备，用户可以启用蓝牙 DID 钩子来解锁更多功能，包括多设备连接（最多两个设备）和高级辅助功能设置，例如使用听力图结果定制透明模式和助听器个性化。

Linux 版本是一个系统托盘应用程序，提供电池监控、入耳检测、噪声控制切换和设备重命名等核心功能。该项目在 GNU 通用公共许可证下开源，强调其对自由软件原则的承诺。

---

## 7. 垃圾回收很有用

**原文标题**: Garbage Collection Is Useful

**原文链接**: [https://dubroy.com/blog/garbage-collection-is-useful/](https://dubroy.com/blog/garbage-collection-is-useful/)

本次开发日志讨论了垃圾回收 (GC) 原理如何帮助作者在使用 Ohm 进行增量解析时解决问题。目标是在使用 Ohm 解析的文本文件和 ProseMirror 中的富文本表示之间创建双向更新。

挑战在于如何高效地识别旧的已解析文档中在小幅编辑后已不在更新文档中的节点，而无需遍历整个文档。作者最初实现了一种基于追踪的方法，类似于追踪垃圾回收，但事实证明效率低下，因为它需要访问每个节点。

该解决方案源于作者对论文《垃圾回收的统一理论》的回忆，该论文强调了追踪和引用计数的二元性。追踪侧重于存活对象，而引用计数侧重于已死对象。通过为 Ohm 解析文档中的节点实现引用计数机制，作者可以高效地识别未使用的节点。当创建新文档时，旧根节点的引用计数会递减，从而触发其子节点的计数的递归递减。这使得系统能够识别不再被引用的节点（已死对象），而无需遍历整个文档，从而提高性能并利用 Ohm 的增量解析功能。作者发现，理解 GC 的基本原理可以实现更高效和优化的解决方案。

---

## 8. Anthropic的报告闻起来很像胡说八道。

**原文标题**: Anthropic's report smells a lot like bullshit

**原文链接**: [https://djnn.sh/posts/anthropic-s-paper-smells-like-bullshit/](https://djnn.sh/posts/anthropic-s-paper-smells-like-bullshit/)

这篇博文批评了人工智能公司Anthropic最近发布的一份报告，该报告声称一个疑似中国政府支持的组织 (GTG-1002) 使用Anthropic的AI助手Claude自动化渗透测试，进行了一项复杂的网络间谍活动。作者djnn认为，该报告缺乏关键的技术细节和可验证的证据，这使得它对于旨在防御此类攻击的网络安全专业人员来说基本上毫无用处。

Djnn强调了报告中缺少入侵指标 (IoC)，例如域名、文件哈希或具体的攻击技术，而这些是来自CERT和安全公司的威胁情报报告中的标准配置。他质疑报告中无法验证的说法，例如人工智能代理独立执行了80-90%的战术操作的断言。

作者还质疑在没有提供佐证的情况下，将这次攻击归因于一个与中国政府有关联的组织，考虑到这可能带来的严重外交影响。他认为这份报告读起来像是一种营销手段，旨在鼓励安全团队采用人工智能驱动的安全解决方案。

Djnn总结说，该报告未能达到威胁情报的行业标准，缺乏道德考量，并且最终似乎旨在推广Anthropic的产品，而不是提供可操作的安全信息。他对缺乏透明度和基于事实的证据表示失望，并呼吁网络安全界要求科技公司在发布此类报告时做得更好。

---

## 9. 飞行中测量WWVB的多普勒频移

**原文标题**: Measuring the doppler shift of WWVB during a flight

**原文链接**: [https://greatscottgadgets.com/2025/10-31-receiving-wwvb-with-hackrf-pro/](https://greatscottgadgets.com/2025/10-31-receiving-wwvb-with-hackrf-pro/)

本文详细介绍了作者使用 HackRF Pro 软件无线电和自制的有源环形天线 Teewee 接收和利用 WWVB 时间信号（60 kHz）的项目。其动机源于希望获得一个稳定且可信赖的频率参考，以评估电子设备，特别是 HackRF 产品中振荡器的精度。从科罗拉多州广播的 WWVB 提供了 GPSDO 的替代方案，具有室内接收和更简单的接收器设计等优势。

作者描述了 Teewee 的设计和构造，强调了其使用仪表放大器来抑制电场噪声。由于来自 PC 的近场干扰造成的最初挫折通过重新安置天线得以克服。

本文解释了 WWVB 信号的特性，包括用于一天中时间的脉冲宽度调制 (PWM) 和用于额外数据流的二进制相移键控 (BPSK)。作者随后描述了一个成功的实验，他们在飞越加拿大期间测量了 WWVB 信号的多普勒频移。通过将接收到的频率与根据 ADSB 飞行数据计算出的预期多普勒频移进行比较，他们确认了多普勒效应，并识别出 HackRF Pro 的 TCXO 中存在轻微的频率误差（慢 15 mHz 或 250 ppb）。虽然由于干扰导致返程航班的捕获失败，但作者最后分享了 Teewee 的设计，供其他人尝试接收 WWVB 信号，甚至建议与 HackRF One 一起使用，尽管它存在局限性。

---

## 10. 伊朗启动人工增雨作业以应对旱情

**原文标题**: Iran begins cloud seeding operations as drought bites

**原文链接**: [https://www.arabnews.com/node/2622812/middle-east](https://www.arabnews.com/node/2622812/middle-east)

伊朗已开始在多个省份开展人工增雨作业，以应对影响该国的严重干旱。这项由国家气候变化中心发起的行动旨在增加缺水地区的降水量。人工增雨是将物质散布到空气中，作为云凝结核或冰核，改变云内的微物理过程并促进降雨。

这些作业正在包括查哈马哈勒和巴赫蒂亚里省、科吉卢耶和博耶-艾哈迈德省、伊斯法罕省、法尔斯省和克尔曼省等受干旱影响最严重的地区进行。飞机被用于散布增雨剂，但摘要中未明确说明使用的具体化合物。

尽管伊朗官员表示希望人工增雨能够缓解部分干旱的影响，但其有效性仍存在争议。批评人士认为，该技术的影响有限，需要更全面的水资源管理战略来解决长期水危机。文章表明，人工增雨是更广泛战略的一部分，但强调其在试图缓解当前干旱方面的直接作用。这些行动的成功与否尚未最终确定，但该计划表明伊朗致力于探索各种方法来对抗缺水。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 2 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 3 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 4 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 5 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 6 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 7 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 8 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 9 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 10 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 11 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 12 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 13 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 14 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 15 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 16 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 17 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 18 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 19 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 20 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 21 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 22 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 23 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 24 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 25 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 26 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 27 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 28 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 29 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 30 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 31 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 32 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 33 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 34 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 35 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 36 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 37 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 38 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 39 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 40 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 41 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 42 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 43 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 44 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 45 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 46 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 47 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 48 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 49 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 50 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 51 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 52 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 53 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 54 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 55 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 56 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 57 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 58 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 59 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 60 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 61 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 62 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 63 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 64 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 65 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 66 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 67 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 68 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 69 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 70 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 71 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 72 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 73 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 74 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 75 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 76 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 77 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 78 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 79 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 80 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 81 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 82 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 83 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 84 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 85 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 86 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 87 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 88 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 89 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 90 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 91 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 92 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 93 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 94 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 95 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 96 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 97 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 98 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 99 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 100 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 101 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 102 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 103 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 104 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 105 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 106 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 107 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 108 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 109 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 110 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 111 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 112 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 113 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 114 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 115 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 116 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 117 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 118 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 119 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 120 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 121 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 122 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 123 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 124 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 125 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 126 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 127 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 128 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 129 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 130 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 131 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 132 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 133 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 134 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 135 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 136 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 137 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 138 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 139 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 140 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 141 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 142 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 143 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 144 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 145 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 146 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 147 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 148 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 149 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 150 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 151 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 152 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 153 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 154 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 155 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 156 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 157 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 158 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 159 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 160 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 161 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 162 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 163 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 164 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 165 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 166 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 167 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 168 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 169 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 170 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 171 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 172 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 173 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 174 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 175 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 176 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 177 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 178 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 179 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 180 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 181 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 182 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 183 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 184 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 185 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 186 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 187 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 188 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 189 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 190 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 191 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 192 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 193 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 194 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 195 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 196 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 197 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 198 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 199 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 200 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 201 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 202 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 203 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 204 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 205 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 206 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 207 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 208 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 209 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 210 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 211 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 212 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 213 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 214 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 215 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 216 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 217 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 218 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 219 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 220 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 221 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 222 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 223 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 224 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 225 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 226 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 227 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 228 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 229 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 230 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 231 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 232 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 233 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 234 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 235 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 236 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 237 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 238 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 239 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 240 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 241 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
