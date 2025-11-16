# Hacker News 热门文章摘要 (2025-11-16)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 互联网已不再是安全港湾

**原文标题**: The Internet Is No Longer a Safe Haven

**原文链接**: [https://brainbaking.com/post/2025/10/the-internet-is-no-longer-a-safe-haven/](https://brainbaking.com/post/2025/10/the-internet-is-no-longer-a-safe-haven/)

作者的网站 Brain Baking 最近遭受了来自阿里巴巴（美国）技术有限公司位于新加坡的服务器（IP段47.79）的爬虫攻击，导致 Gitea 和 Fail2ban 服务器的 CPU 使用率飙升。这些爬虫使用通用的 User-Agent，难以通过简单的方法识别和阻止。

作者不得不采取激进的 IP 屏蔽策略（使用 iptables）来缓解这次攻击。虽然有效，但这感觉像是一种被动的、最终令人不满意的解决方案。作者对不断需要这种干预措施感到沮丧，强调了这对他们的积极性和运行小型服务器的乐趣产生了负面影响。

作者考虑采取更强大的反爬虫措施，如 Anubis 或迁移到 CloudFlare，但对这些解决方案的复杂性和隐私影响感到不满。将 Gitea 实例迁移到 Codeberg 也是正在考虑的选项。

作者感叹，日益猖獗的爬虫和攻击使得业余爱好者越来越难以维护自己的服务器，迫使他们转向中心化解决方案，并恶化了整个互联网环境。作者还提到注意到来自信誉良好的网站的、带有欺骗性 Referer 标头的流量增加，其目的尚不清楚。尽管面临这些挑战，作者仍誓言继续托管自己的网站。

---

## 12. 使用 Podman Quadlets 的生产级容器部署 – Larvitz 博客

**原文标题**: Production-Grade Container Deployment with Podman Quadlets – Larvitz Blog

**原文链接**: [https://blog.hofstede.it/production-grade-container-deployment-with-podman-quadlets/index.html](https://blog.hofstede.it/production-grade-container-deployment-with-podman-quadlets/index.html)

Larvitz博客文章，题为“使用Podman Quadlets进行生产级容器部署”，可能讨论了在生产环境中使用Podman Quadlets来管理和部署容器。

然而，所提供的片段除了机器人验证信息外，不包含任何实际内容。 因此，无法进行真正的总结。

根据标题，我们可以**推断**该文章*可能*涵盖以下潜在要点：

*   **Podman Quadlets 简介：** 解释 Podman Quadlets 是什么及其功能。它们可能提供了一种声明式的方式来定义和管理容器部署。
*   **生产级重点：** 强调使用 Quadlets 进行真实、可靠的部署，解决诸如可扩展性、安全性和监控等方面的问题。
*   **Quadlets 的优势：** 讨论使用 Quadlets 优于传统容器管理方法的优势。 这可能包括更简单的配置管理、自动更新和改进的资源利用率。
*   **实际示例：** 提供有关如何在生产环境中使用 Quadlets 定义和部署容器的示例。
*   **与其他工具的比较：** 潜在地将 Quadlets 与其他容器编排工具（如 Docker Compose 或 Kubernetes）进行比较，突出其独特的优势。

在没有实际文章内容的情况下，这是仅基于标题的最佳可能摘要。

---

## 13. 傅里叶变换

**原文标题**: Fourier Transforms

**原文链接**: [https://www.continuummechanics.org/fourierxforms.html](https://www.continuummechanics.org/fourierxforms.html)

傅里叶变换常被误用和误解，导致错误的结论。本文指出，傅里叶变换本质上是对数据进行正弦和余弦函数曲线拟合，类似于多元线性回归，而非揭示隐藏真相的玄学工具。

文章通过一个简单的例子，将直线拟合到二次函数，展示了如何从回归结果中产生错误的解释。然后，作者解释了傅里叶变换的数学基础，并给出了计算正弦和余弦函数系数的公式。

文章强调了分析整数个信号周期重要性。在非整数个周期上执行傅里叶变换会产生复杂的频谱，包含许多谐波，即使原始信号很简单，比如一个单一的正弦波。这可能会产生误导，暗示原始信号中不存在的频率振动。

文章使用非整数周期正弦波和正弦波后接零的例子，演示了如何误解傅里叶变换。作者解释说，添加零会将相关1Hz分量的振幅减半。文章强调，傅里叶变换可以指示多个谐波的能量，但需要理解原始信号才能正确解释结果。本质上，作者警告不要盲目接受傅里叶变换的输出，而应进行批判性评估并理解其基本原理。

---

## 14. PgFirstAid：提升PostgreSQL稳定性和性能的函数

**原文标题**: PgFirstAid: PostgreSQL function for improving stability and performance

**原文链接**: [https://github.com/randoneering/pgFirstAid](https://github.com/randoneering/pgFirstAid)

pgFirstAid 是一个开源的 PostgreSQL 函数，旨在提供有关数据库稳定性和性能的可操作见解。它受到 SQL Server 的 FirstResponderKit 的启发，为所有技能水平的用户提供了一种快速简便的方法来识别潜在问题。

该函数执行一系列优先级的健康检查（目前为 12 项且数量不断增加），涵盖关键领域，例如缺失的主键、表膨胀和过时的统计信息。问题按严重程度（从 CRITICAL 到 INFO）进行排序，并包含具体的补救措施和指向 PostgreSQL 文档的链接。

安装很简单：将函数定义复制并粘贴到您的数据库中并运行它。该函数需要对系统目录的读取权限，并建议以尽可能高的权限运行以获得全面的结果。

用户可以按严重程度或类别过滤结果，以专注于特定关注领域。建议每天、部署前、重大更改后、性能故障排除期间以及容量规划期间运行 pgFirstAid。

该函数被设计为轻量级且对生产环境安全，使用只读操作和缓存的系统视图。它完全支持 PostgreSQL 10+，并且适用于大多数与 PostgreSQL 兼容的数据库。 欢迎提出贡献和对新健康检查的建议。 请记住在进行更改之前审查建议并在非生产环境中进行测试。

---

## 15. 教育科技的失败承诺：一个十二岁孩子的视角

**原文标题**: A twelve-year-old on the failed promise of educational technology

**原文链接**: [https://micahblachman.beehiiv.com/p/where-educational-technology-fails](https://micahblachman.beehiiv.com/p/where-educational-technology-fails)

七年级学生米卡·布莱克曼评论了旨在监控学生在线活动的教育技术的有效性。他认为，这些系统难以跟上精通技术的学生的步伐，他们能迅速发现漏洞。

米卡提供几个例子：解除对像麻省理工学院的Scratch这样的编程平台的封锁，就能访问该网站上托管的所有游戏；像Blooket和Gimkit这样的测验平台，原本用于教育目的，却能被学生操纵用于游戏；并且未屏蔽游戏链接的传播会通过学生电子邮件网络迅速发生。他提到之前未屏蔽的“Unblocked Games 66”作为一个被发现并随后被屏蔽的网站的例子，突出了屏蔽过程的被动性。

米卡还指出了一个解决方法，即利用为教师设计的教育工具，这些工具有时允许通过教师帐户访问像YouTube这样的被屏蔽内容。他总结说，仅仅依靠屏蔽网站是一种临时的解决方案，会鼓励学生寻找绕过限制的方法。

米卡建议学校应该优先考虑教授负责任的技术使用并信任学生，而不是专注于限制性措施。他承认屏蔽不当内容的必要性，但质疑与培养负责任的数字公民相比，纯粹的被动屏蔽策略的长期益处。

---

## 16. 复古大型语言模型

**原文标题**: Vintage Large Language Models

**原文链接**: [https://owainevans.github.io/talk-transcript.html](https://owainevans.github.io/talk-transcript.html)

本文介绍了“古董大语言模型”（LLMs）的概念，即使用特定历史日期之前的数据训练的LLMs。作者探讨了这些模型在科学、认知和人文方面的潜力。

在科学方面，古董LLMs可用于回溯测试预测方法，以及通过评估在特定时间可获得的信息上训练的LLM是否能重新发现已知的发明和概念，从而“重新发明”过去的思想。在人文方面，它们提供了一种独特的“时间旅行”形式，可以与来自不同时代的人的模拟进行互动对话，并探索反事实的知识历史。这些模型还可以用于评估历史性突破的惊奇性和原创性。

本文重点介绍了创建古董LLMs的挑战，即需要庞大的、未受污染的历史数据集以及高昂的训练成本。它提出了潜在的解决方案，包括利用合成数据来扩充现有数据集，以及采用分叉技术的按时间顺序训练来降低成本。合成数据将通过让现有LLMs释义和混合现有数据来扩充可用的训练数据。

最后，作者提出了高级概念，例如将功能外包给当前的LLMs（同时防止数据泄露），以及创建“分格化LLMs”，该模型使用所有数据进行训练，但带有日期注释，以允许提示特定时间段。目标是使用人工智能来提高预测准确性，调查科学文献，并帮助发明新思想。

---

## 17. 为何使用 OpenBSD？

**原文标题**: Why use OpenBSD?

**原文链接**: [https://www.tumfatig.net/2025/why-are-you-still-using-openbsd/](https://www.tumfatig.net/2025/why-are-you-still-using-openbsd/)

这并非一篇关于为何使用OpenBSD的文章。 而是告知用户正受到名为Anubis的系统挑战，该系统由网站管理员实施，旨在保护服务器免受AI驱动的网络爬虫侵害。 该消息解释说，网站认为该用户可能是机器人，因为其过度爬取行为旨在提取内容用于AI训练。

为应对这种情况，Anubis采用了一种工作量证明机制（类似于Hashcash），要求用户的浏览器执行少量计算工作。 对于单个用户来说，这只是一个小负担，但对于大规模爬虫来说，这将成为一项巨大的成本，从而增加了爬取的难度，并保护网站免受崩溃的影响。

该消息强调，这只是一个临时解决方案，开发人员正在研究更复杂的方法来识别和阻止无头浏览器，例如分析它们的字体渲染。 它还指出，Anubis验证需要Javascript，并建议禁用该域的Javascript阻止插件（如JShelter）。 因此，用户需要启用Javascript才能绕过验证并访问网站内容。 该消息最后声明，正在开发一种无需Javascript的解决方案。

---

## 18. 也许你没尽力。

**原文标题**: Maybe you’re not trying

**原文链接**: [https://usefulfictions.substack.com/p/maybe-youre-not-actually-trying](https://usefulfictions.substack.com/p/maybe-youre-not-actually-trying)

无法访问文章链接。

---

## 19. IDEmacs：Emacs 的 Visual Studio Code 克隆

**原文标题**: IDEmacs: A Visual Studio Code clone for Emacs

**原文链接**: [https://codeberg.org/IDEmacs/IDEmacs](https://codeberg.org/IDEmacs/IDEmacs)

无法访问文章链接。

---

## 20. 在 Kubernetes 中运行基于 Nix 的环境

**原文标题**: Run Nix Based Environments in Kubernetes

**原文链接**: [https://flox.dev/kubernetes/](https://flox.dev/kubernetes/)

本文介绍了 Flox，一个无需重建容器镜像即可在 Kubernetes 中运行基于 Nix 的环境的系统。Flox 允许用户定义在运行时拉取的声明式环境，而不是传输整个容器镜像，从而显著缩短部署时间并确保开发、CI 和生产环境的一致性。

主要优势包括：

*   **更快的部署：** 通过使用节点本地的哈希寻址软件包缓存，消除了镜像构建-推送-拉取周期。
*   **可重复性：** 保证 SDLC 所有阶段环境的一致性，减少偏差并支持原子回滚。
*   **增强的安全性：** 减少攻击面并默认提供 SBOM，确保只部署必要的依赖项。
*   **操作简易性：** 与现有的 Kubernetes 工作流程和工具集成，无需对基础设施进行重大更改。

Flox 使用 containerd shim，与 Kubernetes CRI 交互，在启动时在容器内激活 Flox 环境，使用最小的“占位符”容器镜像。这种方法使包括 AI/ML、数据科学、平台工程、安全和软件工程在内的各种团队受益。

本文还解答了有关 Flox 功能、其对现有工作流程的影响、调试能力以及 SBOM 可靠性的常见问题。它强调 Flox 通过用声明式环境定义替换镜像管道来简化 CI/CD 管道，从而使软件开发和部署更加高效和安全。

---

## 21. 解剖Flock Safety：追踪你的摄像头是一场安全噩梦 [视频]

**原文标题**: Dissecting Flock Safety: The Cameras Tracking You Are a Security Nightmare [video]

**原文链接**: [https://www.youtube.com/watch?v=uB0gr7Fh6lY](https://www.youtube.com/watch?v=uB0gr7Fh6lY)

解剖Flock Safety：追踪你的摄像头是一场安全噩梦， 这部YouTube视频很可能批判了Flock Safety公司，该公司专门生产执法部门和社区使用的车牌识别摄像头。核心论点似乎是Flock Safety的监控技术构成了重大的安全风险和潜在的隐私侵犯。

虽然提供的内容片段不足以完全理解视频的具体细节，但我们可以根据标题推断出以下内容：

* **重点：** 该视频以Flock Safety及其车牌识别摄像头系统为中心。
* **批评：** 该视频采取批判立场，将该系统称为“安全噩梦”。这表明数据安全方面存在潜在漏洞，存在滥用风险，或者对监控的广度和深度存在担忧。
* **隐私问题：** “追踪你的摄像头”一词暗示了对大规模监控和追踪个人行动的担忧。
* **论点：** 该视频很可能认为Flock Safety的益处，例如帮助执法部门破案，被对个人隐私和安全的风险所抵消。它很可能详细说明该系统的运作方式以及滥用或数据泄露的潜在可能性。

本质上，该视频很可能旨在揭露和批判Flock Safety技术的潜在弊端，将其定位为对隐私和安全的威胁，而不是纯粹对执法部门有益的工具。

---

## 22. 未尽其用的事物

**原文标题**: Things that aren't doing the thing

**原文链接**: [https://strangestloop.io/essays/things-that-arent-doing-the-thing](https://strangestloop.io/essays/things-that-arent-doing-the-thing)

本文强调了为行动做准备与实际行动本身之间的关键区别。文章指出，我们经常误认为是在取得进展的许多活动，实际上是避免真正“做这件事”的策略。

作者列举了各种常见行为，例如计划、安排、谈论、研究，甚至是对*没有*做某事而感到内疚，同时强调这些活动都不构成实际进展。社交媒体公告、嫉妒性的批评以及对未来成功的幻想同样被认为是不起作用的干扰。

最终，作者强调，实现预期结果的唯一方法是直接参与手头的任务。所有计划、准备和自我鞭挞，如果没有“做这件事”所需的专注努力，最终都是毫无意义的。核心要点是一个行动号召，敦促读者超越拖延，拥抱完成任务所需的努力。

---

## 23. 英国首个小型核电站将在北威尔士建造

**原文标题**: UK's first small nuclear power station to be built in north Wales

**原文链接**: [https://www.bbc.com/news/articles/c051y3d7myzo](https://www.bbc.com/news/articles/c051y3d7myzo)

英国首座小型核电站将在北威尔士安格尔西岛的维尔法（Wylfa）场址建造，目标是在2030年代中期发电。该项目采用劳斯莱斯设计的小型模块化反应堆（SMR），获得英国政府25亿英镑的投资，将由国有企业英国能源-核能公司承建。该电站可为约300万户家庭供电，并创造多达3000个就业岗位。

首相基尔·斯塔莫强调了该项目在重振英国核电和为安格尔西岛带来就业机会方面的重要性。首席部长埃卢内德·摩根也倡导维尔法的益处。该声明引发了不同的反应，支持者强调了创造就业和能源独立的潜力，而威尔士绿党等批评者则主张投资可再生能源。美国大使也表示失望，认为没有选择大型核电站。

英国能源-核能公司还负责为另一座大型核电站选址。长期核废料储存方案仍然是一项挑战。该项目被视为对威尔士就业、供应链和区域基础设施的重大推动，但成功取决于监管部门的批准、工厂建设和劳动力培训。此外，该声明还具有政治意义，因为今年晚些时候将举行地方选举。

---

## 24. 互动光谱图

**原文标题**: Interactive Spectrum Chart

**原文链接**: [http://www.potatofi.com/posts/spectrum-viewer/](http://www.potatofi.com/posts/spectrum-viewer/)

本文介绍了一个交互式频谱图，这是作者创建的一个网络应用程序，用于以可视化方式呈现无线电频谱。该图表允许用户平移、缩放和切换各种技术和监管领域，以了解无线电频谱的复杂性。

该图表的主要功能包括：

*   **交互式探索：** 用户可以浏览频谱，放大特定频段，并启用/禁用蓝牙、Wi-Fi 和 Zigbee 等技术。
*   **监管域过滤：** 用户可以根据选择的监管域查看信道。
*   **快捷方式：** 快速跳转到特定频段。
*   **可下载的快照：** 用户可以捕获并下载图表的当前视图。
*   **802.11ah 信道图：** 包含作者认为是首个公开可用的 802.11ah 信道图。

作者使用原生 HTML、CSS 和 JavaScript 构建了该应用程序。未来的开发计划包括添加更多技术（如 CBRS/专用蜂窝网络），增强用户界面，提高性能，以及整合通过 GitHub 提交的用户功能请求。作者鼓励用户将该图表用于参考、娱乐和教育目的。该应用程序可以在 [https://spectrum.potatofi.com](https://spectrum.potatofi.com) 找到。

---

## 25. 2019年编写DOS克隆

**原文标题**: Writing a DOS Clone in 2019

**原文链接**: [https://medium.com/@andrewimm/writing-a-dos-clone-in-2019-70eac97ec3e1](https://medium.com/@andrewimm/writing-a-dos-clone-in-2019-70eac97ec3e1)

2019年，作者出于对复古计算的热情，开展了一个个人项目，编写一个与DOS兼容的操作系统。目标不是构建PC模拟器，而是通过实现MS-DOS API来创建一个能够运行DOS软件的操作系统。

该项目成果是一个部分实现了DOS API的内核，磁盘驱动器、控制台和系统时钟的基本驱动程序，一个FAT-12文件系统，以及一个能够运行基本命令和执行COM程序的COMMAND.COM提示符。

作者特意选择在实模式下工作，这是原始DOS的一个约束，这与现代OS开发立即切换到保护模式不同。这带来了独特的挑战，例如内存分段，需要仔细管理段寄存器。

Rust被用作开发语言，由于DOS依赖于不安全行为，这带来了困难。作者通过最小化不安全代码和最大化地道的Rust来克服了这些问题。静态链接对于实模式至关重要，导致了构建挑战，这些挑战通过将内核编译为静态库来解决。内核依赖于静态mut变量来维护系统状态，模仿原始的DOS编程实践。

构建过程包括将Rust代码编译成静态程序，将它们与汇编结合，创建一个FAT-12软盘镜像，并将引导加载程序和系统文件加载到其上。然后，在QEMU中测试该系统。作者计划在获得批准后开源该代码。

---

## 26. 我们对 Archive.today 所受可疑压力的调查

**原文标题**: Our investigation into the suspicious pressure on Archive.today

**原文链接**: [https://adguard-dns.io/en/blog/archive-today-adguard-dns-block-demand.html](https://adguard-dns.io/en/blog/archive-today-adguard-dns-block-demand.html)

AdGuard DNS调查了来自法国新成立的组织Web Abuse Association Defense (WAAD) 的可疑施压，该组织声称Archive.today托管非法内容，要求封锁该网站。WAAD声称自2023年以来，Archive.today拒绝删除非法内容，并以法国法律 (LCEN) 为由威胁AdGuard DNS采取法律行动。

AdGuard认为情况蹊跷，联系了Archive.today，后者迅速删除了被举报的内容，并声称此前未收到相关通知。Archive.today还声称遭遇了“连环”投诉攻击。

AdGuard发现WAAD在线存在感极低，网站注册时间很短，并且使用的地址用于大规模公司注册。WAAD提供的作为证据的“执达主任报告”大多可追溯到2025年8月，而非其声称的2023年。2023年的两份报告并非由WAAD订购，而是由与Archive.today此前面临的类似投诉相关的个人订购，可能涉及冒充律师。

AdGuard怀疑WAAD故意隐藏其身份，并以LCEN法律中对虚假报告的处罚为由，向法国警方提起投诉，指控其潜在的犯罪行为。此次调查与有关FBI调查Archive.today所有者的报告同时进行，可能与托管儿童性虐待材料 (CSAM) 有关，这使得时机显得可疑。AdGuard强调，在受到法律诉讼威胁的情况下，不应由私人公司决定什么构成“非法”内容，并倡导法院监督。

---

## 27. libwifi：用C编写的802.11帧解析和生成库 (2023)

**原文标题**: libwifi: an 802.11 frame parsing and generation library written in C (2023)

**原文链接**: [https://libwifi.so/](https://libwifi.so/)

libwifi 是一个 C 共享库，旨在 Linux 和 macOS 上高效且直接地生成和解析 802.11 无线帧。它优先考虑易用性，允许开发者仅使用几行代码即可处理无线帧，同时提供高级功能。其关键设计原则包括简洁易读的代码、跨架构兼容性、无警告编译以及强大的错误检查。该库采用宽松的许可协议，促进其在各种项目中的使用。本质上，libwifi 旨在通过精心设计且易于访问的 API，简化开发者（无论经验水平如何）对 802.11 帧的操作。

---

## 28. 炼金术

**原文标题**: Alchemy

**原文链接**: [https://joshcollinsworth.com/blog/alchemy](https://joshcollinsworth.com/blog/alchemy)

本文探讨了利用人工智能生成艺术、音乐和视频的现代“炼金术”，将其与中世纪炼金术士试图点石成金的努力相提并论。作者认为，正如黄金过剩会使其贬值一样，人工智能生成内容的泛滥已经降低了其价值。

虽然人工智能最初引发了敬畏和兴趣，但它的普遍存在导致了公众的负面反应。人们越来越能够识别和规避人工智能生成的艺术，觉得它令人不快，并贬低与之相关的任何事物。这源于一个核心论点，即艺术的价值在于人类的创造，特别是其中蕴含的独特故事、挣扎和视角。人工智能艺术缺乏这种人文元素，感觉毫无灵魂且乏味。

作者强调，艺术是一种人际连接的形式，了解艺术家的创作过程和动机是欣赏作品本身不可或缺的一部分。虽然人工智能可能会取代一些工人，但它永远无法完全取代创意人员，因为通过人工智能大量生产创意作品的行为本身会使这些作品变得毫无价值。本质上，本文认为稀缺性和人文元素才是艺术价值的体现，而人工智能轻松生成内容的能力削弱了这种价值，这与炼金术士以无限量创造珍贵事物这一 flawed 逻辑如出一辙。

---

## 29. 纯客户端应用的政治

**原文标题**: The politics of purely client-side apps

**原文链接**: [https://pfrazee.leaflet.pub/3m5hwua4sh22v](https://pfrazee.leaflet.pub/3m5hwua4sh22v)

Paul Frazee的文章探讨了假想的去中心化社交网络“Atmosphere”中客户端-服务器交互的政治经济学。他重点关注在Atmosphere内的社交媒体平台Bluesky上，客户端发布内容的两种方式：

*   **方案一：PDS代理所有流量：** 客户端直接将数据发送到用户的个人数据服务器（PDS），然后由PDS将其转发到Bluesky服务器。这使PDS能够拦截和修改流量，赋予用户更多控制权，并制衡应用程序的力量。然而，这也意味着应用服务器无法在事务完成之前执行服务器端计算，并且用户可能无法立即看到他们的操作。

*   **方案二：应用服务器与PDS通信：** 客户端仅与应用服务器通信，然后由应用服务器与PDS交互。这允许即时操作反馈和更好的性能，但削弱了PDS的政治影响力和用户控制权。

Frazee承认Atmosphere社区需要就一种方法达成一致。虽然Bluesky目前使用方案一，但指导意见指向方案二，因为OAuth。他在这两种方案之间犹豫不决，承认纯客户端应用程序的吸引力和PDS控制的优势，但也认识到方案二的性能优势和直观性。

他建议Bluesky的服务器有可能成为一种云服务，以降低应用程序开发人员的成本，从而促进更多的第三方创新，并有可能将政治权力从PDS转移到应用程序。

---

## 30. 无需JavaScript阻止LLM爬虫

**原文标题**: Blocking LLM crawlers without JavaScript

**原文链接**: [https://www.owl.is/blogg/blocking-crawlers-without-javascript/](https://www.owl.is/blogg/blocking-crawlers-without-javascript/)

本文旨在介绍一种不依赖JavaScript拦截大型语言模型（LLM）爬虫的方法。该方法采用一种简单的技术来识别并可能阻止机器人（可能包括LLM）访问网站内容。

该方法利用了：

*   **短延时：** “Vänta i en sekund…”（请稍等一秒……）表明实施了短暂的暂停。 这种延迟很可能旨在扰乱自动爬取，因为人类不太可能受到如此短的等待时间的影响。

*   **蜜罐：** “Kryp in här om du är en robot”（如果你是机器人，就爬到这里）表明使用了蜜罐。 蜜罐是一种故意放置的链接或元素，对人类不可见，但对机器人很有吸引力。 通过包含此元素，该网站试图引诱机器人点击该链接，从而将它们识别为爬虫。

其主要目标是区分人类用户和自动爬虫（尤其是LLM），以防止未经授权的访问和抓取网站内容，并且无需基于JavaScript的解决方案的复杂性和潜在缺点。

---

## 31. Boa: 一个用 Rust 编写的、符合标准的嵌入式 JavaScript 引擎

**原文标题**: Boa: A standard-conforming embeddable JavaScript engine written in Rust

**原文链接**: [https://github.com/boa-dev/boa](https://github.com/boa-dev/boa)

Boa：用 Rust 编写的可嵌入 JavaScript 引擎，目标是完全符合 ECMAScript 标准（目前超过 90%）。它提供了一个实时的 WASM 演示和一个名为 `boa_cli` 的 CLI 工具。该项目是模块化的，由多个 crate 组成，包括 AST、CLI、引擎、垃圾回收、解析器、字符串驻留等等。

本文提供了一个快速入门指南，其中包含一个简单的代码示例，展示了 Boa 的用法。它重点介绍了 API 文档并提供了指向符合性测试结果的链接。鼓励贡献，相关指南可在 `CONTRIBUTING.md` 中找到。此外还解释了调试和 WebAssembly 的特定配置。

该文档概述了 Boa 的用法，包括命令行选项，例如严格模式、AST 转储、流程图生成和模块处理。提供了路线图（里程碑）、基准测试结果（与 V8 比较）和性能分析信息。变更日志详情在 `CHANGELOG.md` 中。

沟通渠道包括 Matrix 和 Discord，用于提问、讨论和贡献。 Boa 在 Unlicense 或 MIT 双重许可下发布。

---

## 32. 无用机器人的赞歌

**原文标题**: In Praise of Useless Robots

**原文链接**: [https://thereader.mitpress.mit.edu/in-praise-of-useless-robots/](https://thereader.mitpress.mit.edu/in-praise-of-useless-robots/)

对无用机器人的赞美：Laura Tripaldi认为，最引人入胜的机器人并非那些为实用任务而设计的，而是那些能激发我们想象力并帮助我们设想另类未来的机器人。文章将未来主义者视机器为进步和效率象征的观点，与当代艺术家对机器人作为“伴侣物种”的探索进行了对比。

Tripaldi用Anicka Yi的漂浮有氧生物和空山基的“性感机器人”等例子来说明机器人如何日益成为审美沉思的工具，而非纯粹的功能性工具。她强调了从僵硬的拟人机器人向柔软、适应性机器人转变的趋势，这种转变受到Cecilia Laschi等研究人员的拥护，他们从自然界，特别是章鱼中汲取灵感。这种转变反映了向“具身智能”的更广泛过渡，强调了机器人物理形态、与环境的互动及其行为的相互关联。

文章在专注于现代艺术的机器人和早期自动机之间建立了一种历史联系，这些自动机作为认识论装置，反映了世界的秩序。正如那些历史上的自动机反映了宇宙一样，Tripaldi认为，当代“无用”机器人反映了生态的连续性、深刻的异质性和共存的潜力。它们是“宇宙学之镜”，促使我们重新思考我们与技术和周围世界的关系，超越纯粹的功利主义视角。这些机器人的“无用”成为了它们的优势，使它们能够开启新的思考和想象方式。

---

## 33. 在富士通 Lifebook U729 上安装 Linux

**原文标题**: Linux on the Fujitsu Lifebook U729

**原文链接**: [https://borretti.me/article/linux-on-the-fujitsu-lifebook-u729](https://borretti.me/article/linux-on-the-fujitsu-lifebook-u729)

本文详细介绍了作者在一台翻新的富士通 Lifebook U729 上使用 Linux (特别是 NixOS) 的经验。作者在 MacBook 屏幕损坏且对 macOS 不满意后，一直在寻找一款小巧轻便的 Linux 笔记本电脑。他们发现 Lifebook U729 是一款性价比很高的选择，具有良好的配置 (16GB 内存，512GB SSD)。

作者强调了这款笔记本电脑的小尺寸、坚固的结构和良好的键盘等优点。他们报告说，所有硬件组件，包括 WiFi、蓝牙、声音、显示亮度控制、触摸屏和摄像头，都可以在 NixOS 上“开箱即用”。麦克风和指纹传感器未经测试。

主要的障碍是禁用安全启动以安装 Linux。标准的 BIOS 选项最初是灰色的。解决方案包括安装 Windows 11 (笔记本电脑自带)，通过 Windows Update 更新富士通专用驱动程序，然后使用 DeskUpdate 工具更新 BIOS。这更新了 BIOS，从而启用了安全启动禁用选项。

作者还提到在 BIOS 中发现并禁用了名为 Absolute Persistence 的企业间谍软件程序。他们强调在 BIOS 中禁用它就足够了，因为它需要一个操作系统代理才能运行。作者最后提供了访问 BIOS 和启动菜单的说明，以及指向富士通产品页面和数据表的链接。他们总体上拥有积极的体验，认为 U729 是一款合适且令人愉快的 Linux 笔记本电脑。

---

## 34. 人们何时倾向于组合而非继承？

**原文标题**: When did people favor composition over inheritance?

**原文链接**: [https://www.sicpers.info/2025/11/when-did-people-favor-composition-over-inheritance/](https://www.sicpers.info/2025/11/when-did-people-favor-composition-over-inheritance/)

Graham的博文深入探讨了“组合优于继承”原则，质疑其作为一种思维终结陈词滥调的地位。他追溯了该原则的起源，认为其出自“四人帮”的《设计模式》一书，该书将“黑盒”组合（使用对象的接口）置于“白盒”继承（访问实现细节）之上。

作者认为，黑盒与白盒的区别在历史上和语境上是相关的，受到诸如可见性属性和运行时自省等语言特性的影响。他认为，虽然继承是静态定义的，并且最初更容易使用，但组合提供了更多的运行时灵活性，并避免了实现依赖。然而，这种灵活性是以较少依赖编译器进行正确性检查为代价的。

Graham重点介绍了Barbara Liskov的工作，特别是Liskov替换原则，强调当一个类型不是真正的子类型时，组合提供了偏离超类型接口的自由。他进一步指出，组合和继承并非唯一的选择，并建议在某些情况下，头等过程（如lambda表达式）可能更可取。他总结说，在组合、继承和其他方法之间进行选择应该取决于具体的设计背景。

Ryan的评论强调了并发环境中的“继承异常”，在并发环境中，继承可能导致代码重复以处理并发。Graham反驳说，在并发集成到对象设计中的系统中（如Erlang或Eiffel的SCOOP），对象可以控制它们的并发机制，从而有可能缓解这种异常。

---

## 35. MCP：具身智能世界中的模型上下文陷阱

**原文标题**: MCP: Model Context Pitfalls in an agentic world

**原文链接**: [https://hiddenlayer.com/innovation-hub/mcp-model-context-pitfalls-in-an-agentic-world/](https://hiddenlayer.com/innovation-hub/mcp-model-context-pitfalls-in-an-agentic-world/)

HiddenLayer是一家获得Gartner认可的AI安全供应商，其AISec平台旨在解决生成式、预测式和代理式AI应用中涌现的安全挑战。该平台提供全面的安全保障，整合了供应链安全、运行时防御、态势管理和自动化红队测试，以保护AI模型。

该公司专注于帮助私营和公共部门的组织机构自信地采用AI，通过减轻风险、确保合规并防御诸如提示注入、对抗性操纵、模型窃取和供应链破坏等威胁。

HiddenLayer由网络安全和机器学习专家创立，利用专利技术和研究来主动防御AI系统。微软M12、Moore Strategic Ventures、Booz Allen Ventures、IBM Ventures和Capital One Ventures等战略投资者的支持进一步巩固了该公司的强大市场地位。

本质上，HiddenLayer为整个AI生命周期（从开发到部署）提供了一个整体安全解决方案，使组织机构能够在不损害安全性的前提下，充分利用AI的优势。以上内容是突出该公司能力和使命的营销材料。

---

## 36. 绕过分支预测器

**原文标题**: Bypassing the Branch Predictor

**原文链接**: [https://nicula.xyz/2025/03/10/bypassing-the-branch-predictor.html](https://nicula.xyz/2025/03/10/bypassing-the-branch-predictor.html)

当分支预测器的行为对性能产生负面影响时，特别是在大多数交易被放弃，但发送交易的速度至关重要的金融系统中，本文探讨了绕过分支预测器行为的技术。

作者研究了底层方法，发现硬编码分支预测规则（使用诸如`0x2E`和`0x3E`之类的x86指令前缀）仅在非常旧的（Pentium 4）处理器上可行，并且在现代系统上会被忽略。C++20的`[[likely]]`和`[[unlikely]]`属性主要重新排序代码，并不能直接影响现代x86架构上的分支预测。

面对底层方法的局限性，作者提出了一种更高层次的解决方案：使用模拟交易数据来 flooding 系统，对于这些数据，`should_send(t)`始终返回 true。 这会预先设置分支预测器，使其始终预测“发送”路径，从而提高实际发送操作的性能。 在生成模拟交易的同时，真实交易也将受益于预热的指令和数据缓存以及流水线。 然后，系统会在这些模拟交易到达外部服务器之前将其丢弃（例如，使用网卡过滤）。 作者引用了 Carl Cook 在 CppCon 上的演讲，指出该技术使 Cook 的交易系统加速了 5 微秒。 该解决方案不能保证有效，但效果显著。

---

## 37. Rust 中不可思议的类型：如何安全地进行自借用 (2024)

**原文标题**: The inconceivable types of Rust: How to make self-borrows safe (2024)

**原文链接**: [https://blog.polybdenum.com/2024/06/07/the-inconceivable-types-of-rust-how-to-make-self-borrows-safe.html](https://blog.polybdenum.com/2024/06/07/the-inconceivable-types-of-rust-how-to-make-self-borrows-safe.html)

本文提出了一种在Rust中安全地进行自借用的方法，认为当前的限制并非借用检查固有的。作者首先强调，尽管可以通过不安全代码或运行时检查来解决Rust的限制，但这些方法有损Rust安全和零成本抽象的核心原则。

核心思想围绕着启用安全的异步函数，因为异步函数本质上需要自借用。作者认为，主要的障碍是无法命名局部变量的类型，这阻碍了将异步函数手动解糖为安全的Rust代码。这种限制源于“不可命名类型”（闭包、异步函数、impl Trait）和函数局部生命周期。文章提出了一种使用`life 'a`和`end 'a`令牌显式命名生命周期的语法。

此外，文章还确定了“不可思议的类型”——这些类型存在于Rust的事实类型系统中，但不存在于其正式类型系统中，并且会遮蔽类型检查器。这些包括由部分移动/借用产生的类型和表示借用值的类型。文章提出了一种类似`Foo{bar, baz}`的语法来表示部分移动/借用的类型，以及`!'a mut String`来表示借用的类型。

作者认为，借用检查不仅仅是关于内存管理，而是关于防止别名错误。他们介绍了仿射类型（仅使用一次）的概念以及为了多次使用一个值而进行拆分的需求。总的来说，这篇文章提倡一种更全面的类型系统，其中包含这些“不可思议的类型”，以支持自借用和安全的异步函数，从而提高Rust的表达能力和功能。

---

## 38. AsciiMath

**原文标题**: AsciiMath

**原文链接**: [https://asciimath.org/](https://asciimath.org/)

AsciiMath 是一种标记语言，旨在以易读易写的方式书写数学公式。它提供了一种使用纯文本字符表示数学符号的方法，这些字符随后可以被渲染成视觉上吸引人的方程式。推荐使用 MathJax 渲染 AsciiMath，它是一种跨浏览器的 JavaScript 显示引擎，可以配置为将反引号解释为数学分隔符。或者，可以使用专门的 ASCIIMathML.js 文件进行渲染，但其浏览器兼容性有限（主要为 Firefox 和 Safari）。

AsciiMath 的语法包括用文本近似表示符号（例如，`oo` 表示无穷大），并且许多符号都有 TeX 替代方案。该语言支持运算、杂项符号、关系、逻辑符号、分组括号、箭头、重音符号、希腊字母和字体命令。它还处理特殊情况，如矩阵、列向量、增广矩阵、复杂下标、导数以及上/下花括号。

AsciiMath 的语法使用巴科斯范式定义，该范式描述了如何从符号、运算符、括号和函数构造表达式。一个核心原则是在“>”和“<”等字符周围使用空格，以避免与 HTML 解析冲突。总的来说，AsciiMath 提供了一种简单的语法，用于以适合网页显示的纯文本格式表示数学表达式。

---

## 39. 我不需要Steam主机。

**原文标题**: I don’t need a Steam Machine

**原文链接**: [https://brainbaking.com/post/2025/11/why-i-dont-need-a-steam-machine/](https://brainbaking.com/post/2025/11/why-i-dont-need-a-steam-machine/)

本文是一篇幽默的内心独白，讲述了作者纠结于是否购买 Valve 新发布的“Steam Machine”。 最初，作者对这种主机-PC 混合体感到兴奋，但随后试图通过列举诸多不必要和不切实际的理由来说服自己不要购买。

作者强调了自己对复古游戏的偏爱、缺少 4K 电视，以及对 Steam Machine 表面上能够支持的 AAA 游戏的普遍不感兴趣。 他们还承认自己玩游戏的时间有限，电视被其他家庭成员占用，以及已经拥有过多的游戏硬件。

其他原因包括作者对实体游戏的偏好、对 Steam 作为平台的规避（更喜欢 GOG）、长期未使用 Steam，以及不愿摆弄某些游戏控制所需的配置。 他们还指出，他们的 MacBook 能够充分处理 Windows 游戏模拟，并且很快会升级以获得更好的性能。 作者已经在努力应对大量的实体和数字游戏积压。

作者预计 Steam Machine 价格昂贵（超过 600 欧元），并且需要额外的成本，例如 HDMI 切换器和 Steam 控制器。 他们嘲笑了该设备诸如 LED 显示屏等表面特征的诱惑力。

尽管建立了一个看似令人信服的反对购买的理由，但文章结尾作者突然改变主意，宣布无论如何都要购买 Steam Machine，这表明热情最终战胜了逻辑和理性。

---

## 40. 跨代表观遗传：习得性回避的故事

**原文标题**: Transgenerational Epigenetic Inheritance: the story of learned avoidance

**原文链接**: [https://elifesciences.org/articles/109427](https://elifesciences.org/articles/109427)

莱斯利·T·麦克尼尔的这篇文章讨论了线虫*秀丽隐杆线虫*在暴露于致病细菌*铜绿假单胞菌*（PA14）时，习得性回避的跨代表观遗传现象。

该研究建立在科琳·墨菲小组的初步发现之上，该小组证明线虫可以学会避免PA14，并且这种回避行为可以在没有直接接触病原体的情况下传递给后代。

然而，克雷格·亨特及其同事随后的一项研究未能复制超过第一代（F1）的跨代遗传。这种差异引发了一场辩论，重点是实验方案的差异，特别是用于在回避试验中固定线虫的方法（叠氮化钠与温度转换）。

现在，安德烈斯·比达尔-加德亚及其同事提供了对墨菲最初发现的独立验证。他们的研究证实，对PA14的习得性回避确实传递给了F2代。这篇文章强调了方法细节的重要性，例如使用叠氮化钠，墨菲小组认为这捕捉了线虫的最初反应，并防止它们在分析过程中进行学习。这篇文章还涉及了P11的作用，P11是PA14产生的一种小RNA，它诱导跨代表观遗传并影响化学吸引。虽然研究之间存在差异的确切原因仍然复杂，但比达尔-加德亚小组的发现支持了*秀丽隐杆线虫*跨代习得性回避的最初观察的稳健性，并表明亨特小组的程序修改可能导致了他们不同的结果。

---

## 41. 阿基米德 - 用于硬件工程的Python工具包

**原文标题**: Archimedes – A Python toolkit for hardware engineering

**原文链接**: [https://pinetreelabs.github.io/archimedes/blog/2025/introduction.html](https://pinetreelabs.github.io/archimedes/blog/2025/introduction.html)

阿基米德是一个Python工具包，旨在弥合高级算法开发和用于控制系统的嵌入式硬件部署之间的差距。它的目标是提供Python的生产力，同时具备C的可部署性，就像PyTorch为机器学习所做的那样。

阿基米德的核心在于其从NumPy代码自动生成优化C代码的能力。这消除了手动翻译或供应商锁定的生态系统的需求。阿基米德利用非线性优化库CasADi，将NumPy代码转换为C++计算图，从而实现代码生成、导数计算等功能。

除了代码生成，阿基米德还提供以下功能：

*   **编译：** 将Python函数编译成C++计算图，以加快执行速度。
*   **仿真、优化和求根：** 提供用于ODE求解 (CVODES)、约束非线性优化 (IPOPT) 和求根的接口。
*   **自动微分：** 实现简单而精确的导数计算。
*   **结构化数据类型：** 支持分层数据结构，以更好地表示物理系统。

阿基米德促进了一个简化的工作流程：在Python中开发物理模型，用数据进行校准，设计和模拟控制逻辑，通过硬件在环测试进行验证，并充满信心地进行部署。它通过提供控制工程所需的工具，解决了将Python代码部署到嵌入式系统的挑战。

---

## 42. Windows总裁回应AI反弹后Windows 11现状

**原文标题**: Windows president addresses current state of Windows 11 after AI backlash

**原文链接**: [https://www.windowscentral.com/microsoft/windows-11/windows-president-addresses-current-state-of-windows-11-after-ai-backlash-we-know-we-have-a-lot-of-work-to-do](https://www.windowscentral.com/microsoft/windows-11/windows-president-addresses-current-state-of-windows-11-after-ai-backlash-we-know-we-have-a-lot-of-work-to-do)

Windows负责人Pavan Davuluri回应了近期用户对Windows 11发展方向的强烈不满，特别是关于AI集成和忽视核心用户需求的批评。Davuluri表示，微软正在倾听反馈，并意识到需要解决有关可靠性、性能、易用性和开发者体验的问题。他特别承认了对话框不一致等问题，以及对高级用户需求改进的必要性。

文章强调了用户对微软“持续创新”更新策略的失望，该策略频繁推送更新，但常常引入漏洞并扰乱用户体验。许多用户更喜欢发布频率较低、更稳定的大型更新，类似于苹果和谷歌的做法。

Davuluri的回应被视为令人安心，确认微软意识到了对其AI关注的批评，并计划解决操作系统的其他关键方面，如稳定性和面向高级用户的功能。虽然AI开发将继续，但微软计划专注于额外的改进。

---

## 43. “伊卡洛斯之陨”：太阳前坠落的跳伞者照片

**原文标题**: “The Fall of Icarus”: Photograph of a falling skydiver in front of the Sun

**原文链接**: [https://www.iflscience.com/the-fall-of-icarus-you-have-never-seen-an-astrophotography-picture-like-this-81570](https://www.iflscience.com/the-fall-of-icarus-you-have-never-seen-an-astrophotography-picture-like-this-81570)

天文学摄影师安德鲁·麦卡锡和跳伞运动员加布里埃尔·C·布朗合作创作了独特的图像“伊卡洛斯之陨”，展现了布朗在太阳前跳伞的景象。这张照片使用了氢阿尔法滤镜拍摄，突显了太阳湍流的氢层。

图像中，布朗的剪影映衬在太阳表面，完美地定格在太阳黑子之间。麦卡锡解释说，这个概念源于他与布朗关于结合跳伞和天体摄影的对话。

为了实现这一拍摄，需要周密的计划和协调。麦卡锡、布朗和一位动力滑翔伞飞行员互相沟通，以确保精确对齐。飞行员利用他的影子来衡量位置，而麦卡锡则提供了关于驾驶飞机的指示。经过六次尝试，布朗才得以与太阳黑子对齐并跳下。布朗指出，在前五次尝试中发生了一些故障。成功的成果被认为是杰作。麦卡锡在他的网站上出售他天体摄影的限量版作品。

---

## 44. 现代IONIQ 5 N车型刹车片更换需付费墙

**原文标题**: Hyundai Paywalls Brake Pads replacement on Ioniq 5 N

**原文链接**: [https://www.thedrive.com/news/replacing-brake-pads-on-a-hyundai-ioniq-5-n-requires-a-professional-mechanics-login](https://www.thedrive.com/news/replacing-brake-pads-on-a-hyundai-ioniq-5-n-requires-a-professional-mechanics-login)

现代车辆（如现代Ioniq 5 N）因电子驻车制动和软件限制，使得DIY爱好者即使进行更换刹车片等基本汽车维护也越来越困难。

一位Reddit用户的沮丧凸显了这个问题：现在更换刹车片需要专门的计算机设备来收回电子驻车制动。虽然电子驻车制动很常见，但在Ioniq 5 N上访问必要的控制功能并不简单。 现代的专有GDS系统价格昂贵，虽然该品牌支持J2534接口标准，但它推荐特定的（且昂贵的）设备。即使拥有正确的设备，访问刹车维修所需的双向测试也需要来自NASTF的“诊断专业人员”或“车辆安全专业人员”凭证，这实际上阻止了DIY爱好者。

作者承认需要对锁等敏感车辆系统进行安全保护，但认为更换刹车片等基本维修应仍然对车主开放。虽然现代在技术上遵守了维修权法律，并未专门限制访问其自己的设备，但实际效果是，由于这些额外的障碍和安全协议，DIY爱好者被拒之门外。 作者认为需要在安全性和车主对车辆维护的访问权限之间取得更好的平衡。

---

## 45. Trellis AI (YC W24) 招聘：简化获取救生疗法的途径

**原文标题**: Trellis AI (YC W24) Is Hiring: Streamline access to life-saving therapies

**原文链接**: [https://www.ycombinator.com/companies/trellis-ai/jobs/f4GWvH0-forward-deployed-engineer-full-time](https://www.ycombinator.com/companies/trellis-ai/jobs/f4GWvH0-forward-deployed-engineer-full-time)

Trellis AI (YC W24孵化企业) 招聘前线部署工程师，构建并部署AI代理，以简化医疗保健文书工作，助力患者获得拯救生命的疗法。他们的AI自动化处理文件录入、事前授权和申诉，每年处理跨美国所有50个州的数十亿美元疗法。可以将他们视为医疗保健账单领域的Stripe。

该公司是斯坦福大学人工智能实验室的分支机构，获得YC和General Catalyst等知名投资者的支持。该职位涉及设计和实施能够驾驭复杂报销逻辑的AI系统，开发充当护理团队数字队友的长期运行的AI代理，并确保生产就绪的性能。

要求包括全栈开发经验（Python、Go、ML/NLP库）、关系数据库（Postgres）、数据/ML基础设施以及积极学习。云平台经验（AWS、Azure、GCP）和容器化技能（Docker、Kubernetes）是加分项。

Trellis旨在缩短治疗时间、提高授权率并增强药物项目绩效。他们致力于解决医疗保健领域巨额的管理成本问题，这些成本会延误护理、耗尽收入并增加员工倦怠感。 凭借25人的团队和近期10倍的收入增长，他们正在正面应对这个问题。

---

## 46. 拒绝模糊测试：Windows内核中的Rust

**原文标题**: Denial of Fuzzing: Rust in the Windows Kernel

**原文链接**: [https://research.checkpoint.com/2025/denial-of-fuzzing-rust-in-the-windows-kernel/](https://research.checkpoint.com/2025/denial-of-fuzzing-rust-in-the-windows-kernel/)

本文题为《拒绝模糊测试：Windows内核中的Rust》，可能探讨了将模糊测试技术应用于在Windows内核环境中运行的Rust代码时遇到的挑战和局限性。

虽然具体内容未知，但标题暗示文章可能讨论：

*   **模糊测试：** 一种软件测试技术，涉及提供无效、意外或随机的数据作为程序的输入，以发现错误和漏洞。
*   **Rust：** 一种现代编程语言，以其内存安全特性及其在系统编程中日益增长的应用而闻名。
*   **Windows内核：** Windows操作系统的核心，负责管理系统资源并提供基本服务。

“拒绝模糊测试”一词暗示文章将侧重于：

*   **在内核中模糊测试Rust的困难：** 也许Rust的安全性使其更难通过模糊测试找到漏洞。也许内核环境施加了限制，阻碍了标准的模糊测试方法。
*   **造成这些困难的原因：** 文章可能会详细介绍具体的技术挑战，例如插桩问题、内核中的内存管理或现有模糊测试工具应用于Rust内核代码时的局限性。
*   **潜在的解决方案或变通方法：** 如果存在，作者可能会探索克服这些挑战并有效地模糊测试Windows内核中的Rust代码的方法。

本质上，这篇文章可能会深入探讨模糊测试技术、Rust的安全特性以及Windows内核环境的复杂性之间的交叉点，解释为什么模糊测试可能不如在其他环境中那样直接或有效。它可能还会介绍遇到的障碍，并可能提供更成功模糊测试的见解或方法。

---

## 47. 当UPS向我收取了684美元的关税，而这些复古电脑零件的价值仅为355美元时

**原文标题**: When UPS charged me a $684 tariff on $355 of vintage computer parts

**原文链接**: [http://oldvcr.blogspot.com/2025/11/when-ups-charged-me-684-tariff-on-355.html](http://oldvcr.blogspot.com/2025/11/when-ups-charged-me-684-tariff-on-355.html)

2025年11月，“ClassicHasClass”博客的作者详细描述了从欧盟卖家进口老式电脑零件时遇到的令人沮丧的 UPS 经历。 订单价值 355 美元，运费 48.10 美元，最初被征收了 684 美元的关税，远远超出基于卖家使用的协调关税制度编码 (8473.30) 的预期。

第一个危险信号是 UPS 要求提供关于钢铁和铝含量的 Section 232 表格。作者认真填写了表格，但在包裹即将到达时，UPS 要求支付超过 700 美元的费用，其中包括报关费。 作者不情愿地支付了这笔费用，以避免仓库存储费。

在经历了漫长的联系 UPS 客户支持和向其报关部门发送电子邮件的过程后，问题得到了解决。 UPS 提交了一份修改后的 Form 7501，将商品的全部价值归于略有不同的 HTSUS 编码 (8473.30.2000)，该编码是免税的，并对欧盟商品增加了 15% 的关税，总计 51.30 美元。

作者收到的老式电脑零件状况良好，但对 UPS 最初不正确的关税评估以及仅在货物即将交付时才透露最终成本表示不满。 他们建议读者支付有争议的关税以避免存储费，但应立即对费用提出上诉。 尽管存在政治观点，但作者强调每个人都有权获得公平和准确的对待。 作者正在等待 632.70 美元的退款，并批评 UPS 没有发现最初的大额关税，而且他们可能不是唯一遇到这种情况的人。

---

## 48. Show HN: Unflip – 一款关于正方形异或模式的益智游戏

**原文标题**: Show HN: Unflip – a puzzle game about XOR patterns of squares

**原文链接**: [https://unflipgame.com/](https://unflipgame.com/)

“Unflip”是一款在“Show HN”帖子中介绍的新型益智游戏。游戏目标是将所有方块变成白色。玩家通过选择正方形区域（至少2x2大小）进行“翻转”来实现。翻转方块会改变其颜色，将白色方块变成黑色，反之亦然。核心机制围绕理解和操纵网格内的异或模式，以实现完全白色的棋盘。

---

## 49. 我妈17岁时是个自由奔放的女孩，所以她被关了起来，并且陷入了昏迷。

**原文标题**: My mum was a 17-year-old free spirit so she was locked up and put in a coma

**原文链接**: [https://www.bbc.co.uk/news/articles/cr43vx0rrwvo](https://www.bbc.co.uk/news/articles/cr43vx0rrwvo)

本文讲述了马里奥娜·罗卡·托特令人痛心的故事，她是一位西班牙女性，因身为“叛逆”少女而在佛朗哥独裁统治下被关押在一所教养院。1968年，马里奥娜开始参与反佛朗哥活动，激怒了她保守的、极端天主教的父母。在短暂离家出走后，他们向当局举报了她，导致她被拘留在妇女保护协会（Patronato de Protección a la Mujer），这是一个专门关押被认为是“堕落”或不顺从的女性的机构网络。

马里奥娜遭受了严酷的待遇，包括与其他被拘留者有限的交流、强迫劳动和灌输。在试图逃跑后，她在一家精神病诊所接受了电击治疗和胰岛素昏迷疗法，她认为这损害了她的记忆。获释后，她发誓永远不再和父母住在一起。

几十年后，马里奥娜向她的女儿玛丽娜·弗雷克萨讲述了自己的故事，玛丽娜制作了一部名为《空白》（Els Buits）的纪录片，讲述了她母亲的经历。这部电影获得了奖项，并引发了人们呼吁正式承认妇女保护协会幸存者为独裁统治的受害者。玛丽娜和马里奥娜正在巡回放映这部电影，以提高人们的意识，并鼓励其他女性分享她们的故事，强调妇女保护协会并非孤立事件，而是西班牙历史的一个系统性组成部分。西班牙政府已表示愿意调查妇女保护协会幸存者的案件。

---

## 50. 磁富 (2024)

**原文标题**: Mag Wealth (2024)

**原文链接**: [https://saul.pw/mag/wealth/](https://saul.pw/mag/wealth/)

“财富量级 (2024)” 提出了一种理解财富不平等的新方法，即使用对数（量级）尺度将个人划分到“财富等级”中，而不是使用收入等级。文章强调，财富，定义为个人在危机中可以随时获得的资金，是比收入更根本的经济阶层衡量标准。

该尺度以 1980 年代的美元校准（通过除以 3 调整为 2024 年的通货膨胀美元），以保留对货币价值的熟悉感知。文章然后定义了从 ↑-1（赤贫）到 ↑11（巨型企业）的财富等级，每个等级代表可获取财富增加十倍。 每个等级都进行了详细描述，概述了该等级人群的生活条件、财务选择以及面临的典型挑战。

文章突出了每个财富等级内的明显差异和共同特征，表明在同一等级内进行精确的财富比较不如理解定义该等级的系统性因素更有价值。文章还通过将个人财富与各国的国民财富进行比较，提供了背景信息，说明了该尺度的应用和相对财富分配。

---

## 51. MP944是“真正”的第一款微处理器，但它是最高机密。

**原文标题**: The MP944 was the 'real' first microprocessor, but it was top secret

**原文链接**: [https://www.tomshardware.com/pc-components/cpus/the-mp944-was-the-real-worlds-first-microprocessor-and-key-to-the-flight-of-the-f-14-tomcat-but-it-lived-in-the-shadow-of-the-intel-4004-for-nearly-30-years](https://www.tomshardware.com/pc-components/cpus/the-mp944-was-the-real-worlds-first-microprocessor-and-key-to-the-flight-of-the-f-14-tomcat-but-it-lived-in-the-shadow-of-the-intel-4004-for-nearly-30-years)

Tom's Hardware文章指出，Garrett AiResearch为美国海军F-14雄猫战斗机设计的MP944才是“真正”的第一款微处理器，比英特尔4004早一年多。MP944用于F-14的中央大气数据计算机（CADC），于1970年6月开始服役，而英特尔4004于1971年11月才开始商业销售。

由Steve Geller和Ray Holt领导的25人团队开发的MP944性能显著更强，据报道比英特尔4004快八倍，因为它需要执行复杂的飞行参数计算。这款20位、流水线、并行多微处理器以375 kHz的频率运行，每秒执行9,375条指令。

MP944的令人印象深刻的统计数据还包括，它能够承受极端温度，并且具有冗余备份系统，可以在发生故障时在1/18秒内切换。

文章强调，MP944一直保密到1998年解密。如果Holt的研究论文早些发表，计算机行业的面貌可能会截然不同。虽然现在主要具有学术意义，但MP944提醒我们，关键的技术进步往往仍然隐藏，以看不见的方式影响着历史。

---

## 52. 报告：蒂姆·库克最早或于明年卸任苹果CEO

**原文标题**: Report: Tim Cook could step down as Apple CEO 'as soon as next year'

**原文链接**: [https://9to5mac.com/2025/11/14/tim-cook-step-down-as-apple-ceo-as-soon-as-next-year-report/](https://9to5mac.com/2025/11/14/tim-cook-step-down-as-apple-ceo-as-soon-as-next-year-report/)

据《金融时报》报道，苹果公司正在加速首席执行官的继任计划，蒂姆·库克可能“最早在明年”卸任。 报告并未说明加速时间表的具体原因，但强调这并非由于公司目前的业绩，预计业绩将表现强劲。

据报道，硬件工程高级副总裁约翰·特努斯是最有可能接替库克的候选人，但尚未做出最终决定。文章指出，在1月下旬的下一次财报发布之前，不太可能发布公告。

此前，前首席运营官杰夫·威廉姆斯最近从苹果公司退休。他的职责已经在其他高管（包括特努斯）之间重新分配。 苹果最近也经历了首席财务官的更迭。

克里斯蒂安·舒赫的评论强调了蒂姆·库克在领导方面的成功，尤其是在Apple Silicon方面，同时指出了他的继任者将面临的挑战，例如对中国的依赖以及在人工智能开发方面的摸索。 他认为库克对人工智能的谨慎态度可能被证明是明智的。

---

## 53. Show HN: 通过游戏手柄实时导航4D茱莉亚集合

**原文标题**: Show HN: Real-time 4D Julia set navigation via gamepad

**原文链接**: [https://banditcat.github.io/Atlas/Atlas.html](https://banditcat.github.io/Atlas/Atlas.html)

这个“Show HN”帖子介绍了一个使用Atlas编程语言实现的实时4D Julia集导航器，并通过游戏手柄控制。主要重点似乎是在四维空间中对复杂数学概念（Julia集）的交互式探索。使用游戏手柄表明其强调为导航这个抽象且难以可视化的空间提供用户友好和直观的界面。Atlas编程语言被用作实现技术，尽管此简短摘录未提供有关选择Atlas的原因或利用了Atlas的哪些功能的具体信息。“正在加载文件，请稍候……”消息表明该项目可能涉及交互式基于Web的渲染或计算，需要初始加载资源。 本质上，该项目提供了一个交互式工具，用于通过游戏手柄界面实时探索和可视化使用Atlas编程语言构建的4D Julia集。

---

## 54. JVM异常很奇怪：反编译器的视角

**原文标题**: JVM exceptions are weird: a decompiler perspective

**原文链接**: [https://purplesyringa.moe/blog/jvm-exceptions-are-weird-a-decompiler-perspective/](https://purplesyringa.moe/blog/jvm-exceptions-are-weird-a-decompiler-perspective/)

本文深入探讨了Java虚拟机(JVM)异常处理的反编译复杂性，揭示了为何一项看似简单的任务变得出人意料地复杂。作者重点介绍了由JVM设计、类文件格式，甚至是`javac`编译器中的怪异之处所导致的各种边缘情况。

核心问题是JVM的异常控制流是隐式的，并存储在一个与字节码分离的异常表中。此表定义了与异常处理程序关联的代码区域。然而，JVM允许非常规的区域嵌套，这违反了直觉假设，并使反编译器的任务复杂化。

文章进一步探讨了`javac`编译器在使用`try...finally`块时的特殊行为，其中`finally`代码块在每个退出路径（顺序执行、返回、异常）上都会被复制。由于`javac`中的一个遗留问题，这需要捕获所有异常的处理程序，有时其区域甚至包含处理程序本身的起始位置。

作者纠正了这样一种误解，即某些指令，例如`astore_1`，保证不会抛出异常，并强调任何JVM指令在理论上*都可能*抛出`VirtualMachineError`或`IllegalMonitorStateException`，这要求一个强大的反编译器考虑到这一点。

文章讨论了可达性以及JVM的双重类型检查系统，阐述了盲目扩展`try`范围可能导致的问题。文章最后解释说，一个`try...catch`块可以被编译成异常表中的多行，特别是在涉及`finally`块时，并强调需要正确解析这一点，以便在反编译的代码中表示正确的语义。本质上，本文展示了准确反编译Java异常处理机制所涉及的令人惊讶的深度和细微之处。

---

## 55. 使用 Quarto 编写书籍

**原文标题**: Writing a book with Quarto

**原文链接**: [https://blog.stephenturner.us/p/quarto-books](https://blog.stephenturner.us/p/quarto-books)

斯蒂芬·特纳详细介绍了他是如何使用Quarto将旧的RMarkdown课程网站转换为精美的电子书的。他强调了Quarto从单一来源生成各种输出格式（HTML、PDF、EPUB等）的多功能性，以及它与RMarkdown的兼容性。他的转换过程出乎意料地简单，只需对他现有的RMarkdown文件和配置进行最小的调整。他更新了`_quarto.yml`文件，利用GitHub Pages进行托管，并设置了一个自定义子域名。整个过程大约花费了一个小时。

最终的书籍《R语言生物数据科学》可在bdsr.stephenturner.us上找到。虽然内容基于2015-2018年的课程材料，并且因已弃用的函数而略显过时，但作者强调了他将旧网站转换为现代、易于访问的书籍的便捷性。特纳还指出了其他有趣的Quarto功能，重点介绍了Quarto Manuscripts（用于与代码笔记本一起进行叙事写作）和Quarto Dashboards。最后，他链接到资源，包括Quarto Books文档和图库中的示例，以促进公开学习和探索Quarto的功能。

---

## 56. EyesOff：我是如何构建屏幕接触检测模型的

**原文标题**: EyesOff: How I built a screen contact detection model

**原文链接**: [https://ym2132.github.io/building_EyesOff_part2_model_training](https://ym2132.github.io/building_EyesOff_part2_model_training)

作者详细介绍了EyesOff的构建过程，这是一款旨在通过检测有人注视屏幕来防止肩窥的应用。由于缺乏合适的现有数据集，作者着手创建了一个包含2万多张图片的自定义数据集。

作者首先探索了替代方法，例如使用现有的眼神接触检测模型(Eye-Contact-CNN)、MediaPipe地标和视线估计模型，但发现它们要么过于局限、脆弱，要么依赖于用户校准。

该项目的核心是手动标注图像，最初使用FFHQ和自拍数据集，然后过渡到视频会议数据集（VCD）。开发了一个标注框架以确保一致性，并使用YuNet进行人脸检测以简化流程。

EyesOff模型基于预训练的EfficientNetB0，采用类似于Eye-Contact-CNN论文的两阶段方法进行训练。第一阶段涉及使用OpenVino和MediaPipe生成的合成视线向量，在视线回归任务上进行预训练。第二阶段使用VCD数据集对屏幕接触分类任务进行微调，采用POS采样来解决类别不平衡问题。

该模型在模拟近距离和中距离的测试用例中进行了评估，达到了约71%的准确率。作者承认合成视线数据的局限性，未来的工作包括尝试替代模型、调整YuNet架构以及改进标注流程。

---

## 57. 与爬虫机器人作斗争

**原文标题**: Messing with scraper bots

**原文链接**: [https://herman.bearblog.dev/messing-with-bots/](https://herman.bearblog.dev/messing-with-bots/)

本文详细介绍了作者通过向恶意抓取机器人提供生成的垃圾数据来对抗它们的实验。由于机器人不断寻找敏感文件和潜在漏洞（如 .env、.aws 和 .php 路径），作者决定主动参与，而不是简单地阻止它们。

作者最初构建了一个基于马尔可夫链的胡言乱语生成器，使用 .php 文件进行训练，以生成看起来逼真但最终是虚假的 .php 代码。目的是浪费机器人的资源和时间，希望人工操作员能够尝试分析虚假代码中的漏洞。然而，提供大型生成文件对服务器来说资源消耗很大。

作者随后转向提供静态内容。他们创建了一个系统，从《弗兰肯斯坦》中提供随机段落来响应无休止的请求。这种“帖子胡言乱语生成器”非常高效。他们还创建了一个单独的服务器，根据请求提供随机的真实 .php 文件，专门针对搜索 .php 路径的机器人。

作者承认这种方法的风险，特别是对于依赖 Google 索引的网站。虽然使用了 `robots.txt`、`nofollow` 和 `noindex` 规则，但仍然存在搜索引擎爬虫被误导并将该网站标记为垃圾邮件的风险。因此，他们只在游乐场域名上运行“帖子胡言乱语生成器”。然而，他们认为 .php 胡言乱语生成器是安全的，因为 Googlebot 通常会忽略非 HTML 页面。

作者最后提出了一个折衷方案：在其他项目上添加一个指向胡言乱语生成器的隐藏 `nofollow` 链接，以引诱恶意抓取器，而不会冒 Google 惩罚的风险。总的来说，这个项目是一次学习经历，也是一种有趣的宣泄方式。

---

## 58. J.M.库切早期编程生涯中的计算机诗歌 (2017)

**原文标题**: The computer poetry of J. M. Coetzee's early programming career (2017)

**原文链接**: [https://sites.utexas.edu/ransomcentermagazine/2017/06/28/the-computer-poetry-of-j-m-coetzees-early-programming-career/](https://sites.utexas.edu/ransomcentermagazine/2017/06/28/the-computer-poetry-of-j-m-coetzees-early-programming-career/)

瑞贝卡·罗奇的文章探讨了J.M.库切早期作为一名计算机程序员，且在很大程度上被忽视的职业生涯，以及它对其后期文学作品的潜在影响。1962年至1965年，库切在英国从事先进的Atlas 2超级计算机项目。白天设计计算机的同时，他晚上还尝试“计算机诗歌”，编写程序通过从预定义词汇表中选择单词来生成重复的诗句。

罗奇在兰索姆中心查阅了库切的论文，包括二进制、十六进制、FORTRAN和FORTRAN“伪代码”的代码打印稿，以及从软盘中恢复的原始数字材料。这项调查帮助她确定了库切在其职业生涯中使用过的计算硬件和软件的时间线。

这项研究提出了关于阅读和保存代码、定义程序“文本”以及访问文学档案馆中的电子文件的关键问题。罗奇认为，考察库切的“另一项职业”可以阐明这些问题，这些问题随着越来越多的作家创作原始数字档案而变得越来越重要。她的工作是名为“机器对话”的更大项目的一部分，该项目探索数字文学中的交流与协作。

---

## 59. 5美元 PlanetScale 上线了

**原文标题**: $5 PlanetScale is live

**原文链接**: [https://planetscale.com/blog/5-dollar-planetscale-is-here](https://planetscale.com/blog/5-dollar-planetscale-is-here)

PlanetScale 推出 5 美元单节点 Postgres 数据库，为初创公司、业余项目和开发提供经济高效的选择。这些可用于生产环境的数据库具有 PlanetScale 的各项功能，如查询洞察、模式推荐、深度指标和分支。现在，开发分支的定价也为每月 5 美元。用户可以轻松地垂直扩展单节点数据库，通过添加副本来过渡到 HA 模式，并最终利用 PlanetScale 的分片 Postgres 解决方案 (Neki) 进行水平扩展，以满足其增长的需求。这消除了随着业务扩展而进行数据库迁移的需要。新用户可以注册 PlanetScale 账户，并在创建数据库时选择“单节点”选项，并可在定价页面查看详细定价。

---

## 60. 单手键盘

**原文标题**: One Handed Keyboard

**原文链接**: [https://github.com/htx-studio/One-Handed-Keyboard](https://github.com/htx-studio/One-Handed-Keyboard)

本文介绍一款开源单手机械键盘，旨在帮助单手活动受限的人士，特别是那些需要尽量减少键盘和鼠标之间手部移动的人士。该项目受一位用户为其失去右手功能的女儿定制键盘的请求启发，提供了三种键盘布局（左右手和小型左手），并集成了轨迹球。

该键盘采用 QMK 固件和开源硬件。本文重点介绍了所有必要设计文件的可用性，包括 PCB 布局（适用于不同的键盘型号和辅助组件，如轨迹球、滚轮和方向按钮）、VIA 键位重映射配置、编译后的固件和 3D 模型。

文章提供了详细的制造指南，包括 PCB 规格、推荐的打印材料（键帽、外壳等）以及硬件组件（如轨迹球、滚轮和螺丝）的规格。文章涵盖了组装过程，强调了在最终组装前测试组件的重要性，并提供了有关安装 PCB、连接小型电路板以及分层铺设棉花和阻尼器等材料的指导。

最后，项目作者强调这是他们的第一个开源项目，并欢迎反馈。他们感谢 QMK 社区，并引用了与轨迹球 ADNS-9800 传感器相关的存储库。

---

## 61. 内华达州长办公室掩盖了Boring公司安全违规行为

**原文标题**: Nevada Governor's office covered up Boring Co safety violations

**原文链接**: [https://fortune.com/2025/11/12/elon-musk-boring-company-tunnels-injuries-osha-citations-fines-rescinded-nevada-governor-office-documents-altered/](https://fortune.com/2025/11/12/elon-musk-boring-company-tunnels-injuries-osha-citations-fines-rescinded-nevada-governor-office-documents-altered/)

财富杂志调查显示，内华达州州长办公室曾介入帮助埃隆·马斯克的“无聊公司”避免内华达州职业安全与健康管理局（OSHA）因一起工作场所安全事故开出的巨额罚款。该事故导致两名消防员在“无聊公司”隧道内的一次训练演习中因接触有毒泥浆液而遭受化学烧伤。

在职业安全与健康管理局开出超过40万美元的罚款后不久，“无聊公司”总裁史蒂夫·戴维斯联系了州长乔·隆巴多的办公室。随后，高级州官员会见了“无聊公司”的高管，罚单被撤销。该会议的记录随后从公共文件中删除。

文章重点强调了该案件处理过程中涉嫌违规之处，包括文件缺失以及偏离职业安全与健康管理局的标准程序。内华达州职业安全与健康管理局内部人士对政治干预以及该机构执行安全法规的能力产生寒蝉效应表示担忧，特别是考虑到马斯克在内华达州日益增长的投资。

内华达州职业安全与健康管理局声称，撤销的罚单存在缺陷，州长办公室在处理雇主投诉时行事符合标准程序，但内华达州前监管人员声称，这种政治干预非常不寻常且不恰当。文章还详细介绍了“无聊公司”项目现场发生的其他安全事故，并将这些事故归因于一种“牛仔”文化，即优先考虑速度而非安全。

---

## 62. 美国人工智能泡沫让我想起中国房地产崩盘前夕

**原文标题**: The US AI Bubble Reminds Me of the Eve of China's Real Estate Collapse

**原文链接**: [https://jonathancc.substack.com/p/the-us-ai-bubble-reminds-me-of-the](https://jonathancc.substack.com/p/the-us-ai-bubble-reminds-me-of-the)

无法访问文章链接。

---

## 63. 横跨美国计算机之旅 (1983-1985)

**原文标题**: Computing Across America (1983-1985)

**原文链接**: [https://microship.com/winnebiko/](https://microship.com/winnebiko/)

史蒂文·K·罗伯茨的《计算横跨美国》讲述了他1983-1985年间开创性的技术游牧之旅，他骑着一辆名为Winnebiko的定制躺式自行车。出于对逃离郊区生活以及结合写作、技术和旅行热情的渴望，罗伯茨借助一台Radio Shack Model 100、一个CompuServe账户和太阳能，开始了长达17000英里的冒险。

文章详细描述了罗伯茨的移动设备，包括太阳能电池板、天线和躺式自行车，如何吸引了媒体的关注，并将他最初的高科技自行车之旅转变为一项事业。他写了一本书（《计算横跨美国》），为杂志撰写文章并接受采访，早在“随时随地工作”成为常态之前，他就拥抱了这个概念。

随着技术的快速发展，罗伯茨升级了他的设备，最终切换到惠普便携式电脑，并设计了一个骑行时写作的系统。在达到10000英里的里程碑后，他休息了一年，完成他的书并设计一个全新的系统。文章提供了涵盖他旅程的各种出版物和媒体露面的链接，以及最初的Winnebiko的技术规格。主要功能包括铬钼合金车架、18速传动系统以及诸如CB收音机、安全系统和太阳能电池板等基本电子设备。

---

## 64. 使用 Rust 在 AWS Lambda 上构建无服务器应用程序 – AWS 计算博客

**原文标题**: Building Serverless Applications with Rust on AWS Lambda – AWS Compute Blog

**原文链接**: [https://aws.amazon.com/blogs/compute/building-serverless-applications-with-rust-on-aws-lambda/](https://aws.amazon.com/blogs/compute/building-serverless-applications-with-rust-on-aws-lambda/)

本文宣布 AWS Lambda 现已全面支持 Rust，使开发者能够构建高性能、内存安全的 Serverless 应用，并享有 AWS 的支持和 SLA。 Rust 提供了与 C++ 相当的性能，同时具备更高级别语言的可靠性。

本文演示了如何使用第三方开源工具 Cargo Lambda 构建和部署基于 Rust 的 Lambda 函数。内容包括：

*   **安装和配置：** 安装 Cargo Lambda（Rust Cargo 工具的扩展），可简化 Rust Lambda 函数的构建和部署。
*   **函数创建和结构：** 创建基于 HTTP 的 Lambda 函数，重点介绍 `main.rs`（入口点）和 `http_handler.rs`（函数逻辑）文件。
*   **代码解释：** 详细说明代码的功能，包括处理请求、解析参数以及使用 `lambda_http` crate 返回响应。还涉及通过 Tracing 库进行日志记录。
*   **构建和测试：** 使用 `cargo lambda build` 构建函数，并使用 `cargo lambda watch` 和 `cargo lambda invoke` 或 `curl` 在本地进行测试。
*   **部署：** 使用 `cargo lambda deploy` 将函数部署到 AWS，并在远程进行测试。
*   **使用 AWS CDK 进行基础设施即代码：** 使用 AWS CDK 和 Cargo Lambda CDK Construct 创建一个 Serverless API，并在 Rust Lambda 函数前面放置 Amazon API Gateway。给出了关于设置 CDK 项目、安装 construct、更新 CDK 堆栈、引导和部署的说明。

最后，本文提供了清理说明以及指向 AWS Lambda 开发者指南、Cargo Lambda 文档、AWS CDK 文档、Serverless Patterns Collection 和 Serverless Land 等更多资源的链接。

---

## 65. 人工智能世界时钟

**原文标题**: AI World Clocks

**原文链接**: [https://clocks.brianmoore.com/](https://clocks.brianmoore.com/)

AI世界时钟是由Brian Moore创建的项目，灵感来自Matthew Rayfield。该网站每分钟展示一个全新的模拟时钟，由九种不同的人工智能模型生成。每个AI模型都会收到提示，以创建HTML/CSS代码，用于生成一个响应式模拟时钟，显示特定时间，包括数字和CSS动画的秒针等功能，所有这些都以白色背景为背景。人工智能模型的代码生成限制为2000个token，并指示仅返回HTML/CSS代码，不含Markdown格式。页面显示正在积极生成这些AI时钟。创建者还有一个Instagram账号。

---

## 66. 最小化方差的均值加权

**原文标题**: Weighting an average to minimize variance

**原文链接**: [https://www.johndcook.com/blog/2025/11/12/minimum-variance/](https://www.johndcook.com/blog/2025/11/12/minimum-variance/)

本文探讨了如何在多个独立资产之间优化投资分配，以最小化投资组合的波动性（方差）的问题。首先，从涉及两种资产X和Y的简化场景入手，目标是找到投资于X的最优比例(t)和投资于Y的(1-t)。假设X和Y是独立的，文章推导出使投资组合方差最小化的最优't'。该公式表明，对X的分配与X相对于Y的方差成反比。

然后，文章将这种方法推广到'n'个独立资产，X1到Xn。目标是最小化方差的加权和，约束条件是权重（ti）之和为1且非负。使用拉格朗日乘数法，文章得出了一个通用解：ti = (1/Variance(Xi)) / (所有j从1到n的 (1/Variance(Xj))之和)。该公式表明，对每种资产的最优分配与其方差的倒数成正比，分母与初等对称多项式相关。因此，资产的波动性越低，分配给它的资金比例就越高。

---

## 67. 设计一门语言 (2017)

**原文标题**: Designing a Language (2017)

**原文链接**: [https://cs.lmu.edu/~ray/notes/languagedesignnotes/](https://cs.lmu.edu/~ray/notes/languagedesignnotes/)

设计一门语言（2017）：本文为有志于创建自有编程语言的人士提供了全面的指导。它强调语言设计是一个迭代过程，涉及构思、规范、实现和评估。 丰富的经验以及对编程范式、语言概念和现有语言的了解对于成功至关重要。

文章建议研究各种不同的语言，从Python和Smalltalk到Haskell和Brainfuck，强调每种语言的独特优势和劣势。 它还指出，通过研究经典论文和在线资源，了解以往语言设计的成功和失败至关重要。

该指南提供了一个入门注意事项清单，包括确定目标受众、确定语言的用途（可用性与深奥性）以及选择编程范式。 它提出了许多关于潜在特性的问题，例如函数参数、类型系统、表达式求值、作用域、控制流和并发模型。 这些问题可以提示设计者对语言设计做出明智的决策。

最后，文章提到了抽象语法，强调定义AST节点及其关系以建立语言的结构化表示的重要性。 它以JavaScript的EsTree规范为例。 文章承认语言设计的复杂性并鼓励持续学习。

---

## 68. Is our death from a hydrogen sulfide event inevitable in climate warming? (2005)

**原文标题**: Is our death from a hydrogen sulfide event inevitable in climate warming? (2005)

**原文链接**: [https://www.psu.edu/news/research/story/global-warming-led-climatic-hydrogen-sulfide-and-permian-extinction](https://www.psu.edu/news/research/story/global-warming-led-climatic-hydrogen-sulfide-and-permian-extinction)

生成摘要时出错

---

## 69. I made a better DOM morphing algorithm

**原文标题**: I made a better DOM morphing algorithm

**原文链接**: [https://joel.drapper.me/p/morphlex/](https://joel.drapper.me/p/morphlex/)

生成摘要时出错

---

## 70. Ubiquiti Flex Mini 2.5G Review Ubiquiti Does a Cheap 5-Port 2.5GbE Switch

**原文标题**: Ubiquiti Flex Mini 2.5G Review Ubiquiti Does a Cheap 5-Port 2.5GbE Switch

**原文链接**: [https://www.servethehome.com/ubiquiti-flex-mini-2-5g-review-ubiquiti-does-a-cheap-5-port-2-5gbe-switch/](https://www.servethehome.com/ubiquiti-flex-mini-2-5g-review-ubiquiti-does-a-cheap-5-port-2-5gbe-switch/)

生成摘要时出错

---

## 71. AMD continues to chip away at Intel's x86 market share

**原文标题**: AMD continues to chip away at Intel's x86 market share

**原文链接**: [https://www.tomshardware.com/pc-components/cpus/amd-continues-to-chip-away-at-intels-x86-market-share-company-now-sells-over-25-percent-of-all-x86-chips-and-powers-33-percent-of-all-desktop-systems](https://www.tomshardware.com/pc-components/cpus/amd-continues-to-chip-away-at-intels-x86-market-share-company-now-sells-over-25-percent-of-all-x86-chips-and-powers-33-percent-of-all-desktop-systems)

生成摘要时出错

---

## 72. Why export templates would be useful in C++ (2010)

**原文标题**: Why export templates would be useful in C++ (2010)

**原文链接**: [http://warp.povusers.org/programming/export_templates.html](http://warp.povusers.org/programming/export_templates.html)

生成摘要时出错

---

## 73. History and use of the Estes AstroCam 110

**原文标题**: History and use of the Estes AstroCam 110

**原文链接**: [https://www.dembrudders.com/history-and-use-of-the-estes-astrocam-110.html](https://www.dembrudders.com/history-and-use-of-the-estes-astrocam-110.html)

生成摘要时出错

---

## 74. Aunt Mary's Storybook

**原文标题**: Aunt Mary's Storybook

**原文链接**: [https://cjtinc.org/projects/amsb/](https://cjtinc.org/projects/amsb/)

生成摘要时出错

---

## 75. Lawmakers want to ban VPNs

**原文标题**: Lawmakers want to ban VPNs

**原文链接**: [https://www.eff.org/deeplinks/2025/11/lawmakers-want-ban-vpns-and-they-have-no-idea-what-theyre-doing](https://www.eff.org/deeplinks/2025/11/lawmakers-want-ban-vpns-and-they-have-no-idea-what-theyre-doing)

生成摘要时出错

---

## 76. Meta Replaced the Native WhatsApp for Windows 11 with a Shitty Web App

**原文标题**: Meta Replaced the Native WhatsApp for Windows 11 with a Shitty Web App

**原文链接**: [https://daringfireball.net/2025/11/meta_whatsapp_windows_shitty_web_app](https://daringfireball.net/2025/11/meta_whatsapp_windows_shitty_web_app)

生成摘要时出错

---

## 77. How to write generics in C

**原文标题**: How to write generics in C

**原文链接**: [https://raphgl.github.io/blog/generics-in-c.html](https://raphgl.github.io/blog/generics-in-c.html)

生成摘要时出错

---

## 78. Meta's Yann LeCun to Launch Physical AI Startup After Declaring LLMs 'Dead End'

**原文标题**: Meta's Yann LeCun to Launch Physical AI Startup After Declaring LLMs 'Dead End'

**原文链接**: [https://observer.com/2025/11/yann-lecun-leave-meta-launch-world-models-startup/](https://observer.com/2025/11/yann-lecun-leave-meta-launch-world-models-startup/)

生成摘要时出错

---

## 79. TCP, the workhorse of the internet

**原文标题**: TCP, the workhorse of the internet

**原文链接**: [https://cefboud.com/posts/tcp-deep-dive-internals/](https://cefboud.com/posts/tcp-deep-dive-internals/)

生成摘要时出错

---

## 80. The Nature of the Beast: Charles Le Brun's Human-Animal Hybrids (1806)

**原文标题**: The Nature of the Beast: Charles Le Brun's Human-Animal Hybrids (1806)

**原文链接**: [https://publicdomainreview.org/collection/le-brun-human-animal-hybrids/](https://publicdomainreview.org/collection/le-brun-human-animal-hybrids/)

生成摘要时出错

---

## 81. Strap Rail

**原文标题**: Strap Rail

**原文链接**: [https://www.construction-physics.com/p/strap-rail](https://www.construction-physics.com/p/strap-rail)

生成摘要时出错

---

## 82. Launch HN: Tweeks (YC W25) – Browser extension to deshittify the web

**原文标题**: Launch HN: Tweeks (YC W25) – Browser extension to deshittify the web

**原文链接**: [https://www.tweeks.io/onboarding](https://www.tweeks.io/onboarding)

生成摘要时出错

---

## 83. Structured outputs on the Claude Developer Platform

**原文标题**: Structured outputs on the Claude Developer Platform

**原文链接**: [https://www.claude.com/blog/structured-outputs-on-the-claude-developer-platform](https://www.claude.com/blog/structured-outputs-on-the-claude-developer-platform)

生成摘要时出错

---

## 84. Löb and Möb: Loops in Haskell (2013)

**原文标题**: Löb and Möb: Loops in Haskell (2013)

**原文链接**: [https://github.com/quchen/articles/blob/master/loeb-moeb.md](https://github.com/quchen/articles/blob/master/loeb-moeb.md)

生成摘要时出错

---

## 85. Steam Machine

**原文标题**: Steam Machine

**原文链接**: [https://store.steampowered.com/sale/steammachine](https://store.steampowered.com/sale/steammachine)

生成摘要时出错

---

## 86. Windhawk Windows classic theme mod for Windows 11

**原文标题**: Windhawk Windows classic theme mod for Windows 11

**原文链接**: [https://windhawk.net/mods/classic-theme-enable](https://windhawk.net/mods/classic-theme-enable)

生成摘要时出错

---

## 87. No Leak, No Problem – Bypassing ASLR with a ROP Chain to Gain RCE

**原文标题**: No Leak, No Problem – Bypassing ASLR with a ROP Chain to Gain RCE

**原文链接**: [https://modzero.com/en/blog/no-leak-no-problem/](https://modzero.com/en/blog/no-leak-no-problem/)

生成摘要时出错

---

## 88. A new Google model is nearly perfect on automated handwriting recognition

**原文标题**: A new Google model is nearly perfect on automated handwriting recognition

**原文链接**: [https://generativehistory.substack.com/p/has-google-quietly-solved-two-of](https://generativehistory.substack.com/p/has-google-quietly-solved-two-of)

生成摘要时出错

---

## 89. Feature Extraction with KNN

**原文标题**: Feature Extraction with KNN

**原文链接**: [https://davpinto.github.io/fastknn/articles/knn-extraction.html](https://davpinto.github.io/fastknn/articles/knn-extraction.html)

生成摘要时出错

---

## 90. The disguised return of EU Chat Control

**原文标题**: The disguised return of EU Chat Control

**原文链接**: [https://reclaimthenet.org/the-disguised-return-of-the-eus-private-message-scanning-plot](https://reclaimthenet.org/the-disguised-return-of-the-eus-private-message-scanning-plot)

生成摘要时出错

---

## 91. Manganese is Lyme disease's double-edge sword

**原文标题**: Manganese is Lyme disease's double-edge sword

**原文链接**: [https://news.northwestern.edu/stories/2025/11/manganese-is-lyme-diseases-double-edge-sword](https://news.northwestern.edu/stories/2025/11/manganese-is-lyme-diseases-double-edge-sword)

生成摘要时出错

---

## 92. Show HN: Tiny Diffusion – A character-level text diffusion model from scratch

**原文标题**: Show HN: Tiny Diffusion – A character-level text diffusion model from scratch

**原文链接**: [https://github.com/nathan-barry/tiny-diffusion](https://github.com/nathan-barry/tiny-diffusion)

生成摘要时出错

---

## 93. Incus-OS: Immutable Linux OS to run Incus as a hypervisor

**原文标题**: Incus-OS: Immutable Linux OS to run Incus as a hypervisor

**原文链接**: [https://linuxcontainers.org/incus-os/](https://linuxcontainers.org/incus-os/)

生成摘要时出错

---

## 94. Streaming AI agent desktops with gaming protocols

**原文标题**: Streaming AI agent desktops with gaming protocols

**原文链接**: [https://blog.helix.ml/p/technical-deep-dive-on-streaming](https://blog.helix.ml/p/technical-deep-dive-on-streaming)

生成摘要时出错

---

## 95. Unofficial Microsoft Teams client for Linux

**原文标题**: Unofficial Microsoft Teams client for Linux

**原文链接**: [https://github.com/IsmaelMartinez/teams-for-linux](https://github.com/IsmaelMartinez/teams-for-linux)

生成摘要时出错

---

## 96. Major Bitcoin mining firm pivoting to AI

**原文标题**: Major Bitcoin mining firm pivoting to AI

**原文链接**: [https://www.tomshardware.com/tech-industry/cryptomining/major-bitcoin-mining-firm-pivoting-to-ai-plans-to-fully-abandon-crypto-mining-by-2027-bitfarm-to-leverage-341-megawatt-capacity-for-ai-following-usd46-million-q3-loss](https://www.tomshardware.com/tech-industry/cryptomining/major-bitcoin-mining-firm-pivoting-to-ai-plans-to-fully-abandon-crypto-mining-by-2027-bitfarm-to-leverage-341-megawatt-capacity-for-ai-following-usd46-million-q3-loss)

生成摘要时出错

---

## 97. How the Spoils of an Infamous Heist Traveled the World

**原文标题**: How the Spoils of an Infamous Heist Traveled the World

**原文链接**: [https://nautil.us/how-the-spoils-of-an-infamous-heist-traveled-the-world-1247307/](https://nautil.us/how-the-spoils-of-an-infamous-heist-traveled-the-world-1247307/)

生成摘要时出错

---

## 98. Operating Margins

**原文标题**: Operating Margins

**原文链接**: [https://fi-le.net/margin/](https://fi-le.net/margin/)

生成摘要时出错

---

## 99. Linear algebra explains why some words are effectively untranslatable

**原文标题**: Linear algebra explains why some words are effectively untranslatable

**原文链接**: [https://aethermug.com/posts/linear-algebra-explains-why-some-words-are-effectively-untranslatable](https://aethermug.com/posts/linear-algebra-explains-why-some-words-are-effectively-untranslatable)

生成摘要时出错

---

## 100. Android developer verification: Early access starts

**原文标题**: Android developer verification: Early access starts

**原文链接**: [https://android-developers.googleblog.com/2025/11/android-developer-verification-early.html](https://android-developers.googleblog.com/2025/11/android-developer-verification-early.html)

生成摘要时出错

---

