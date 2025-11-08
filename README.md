# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-11-08.md)

*最后自动更新时间: 2025-11-08 17:45:11*
## 1. 股票代码：别死于心脏病

**原文标题**: Ticker: Don't Die of Heart Disease

**原文链接**: [https://myticker.com/](https://myticker.com/)

贾里德·赫克特的文章《定时炸弹：别死于心脏病》指出，心脏病是一种可预防的主要死因，却常常被标准医疗手段忽视。赫克特分享了他通过私人定制医疗服务提供的高级检测发现早期心脏病的个人经历，这与他通过使用标准血脂检查从初级保健医生那里得到的“完全正常”的评估形成对比。

核心信息是，个人必须为自己的心脏健康负责。赫克特强调，标准医疗实践往往会遗漏ApoB和Lp(a)等关键生物标志物，而经济实惠且易于获得的检测（每年约300美元）可以检测到早期预警信号。这些检测，再加上生活方式的改变和药物治疗，可以显著降低心脏病发作的风险。

赫克特为掌控心脏健康提供了一个路线图，敦促读者要求他们的医生进行全面的检查并理解结果。他的目标是普及通常为富人保留的知识和实践，使30多岁和40多岁的人能够积极地管理自己的心脏健康，避免成为统计数据中的一员。他认为需要一家专注于心脏病预防的面向消费者的公司，并希望这份指南能够激发人们的兴趣和行动。

---

## 2. Zig很酷，C更酷。

**原文标题**: Zig is so cool, C is cooler

**原文链接**: [https://github.com/little-book-of/c/blob/main/articles/zig-is-cool-c-is-cooler.md](https://github.com/little-book-of/c/blob/main/articles/zig-is-cool-c-is-cooler.md)

这看起来像是托管在某个平台（可能是 GitHub 或类似平台）上的一个名为 "little-book-of/c" 的项目的网页摘要。标题 "Zig 很酷，C 更酷" 暗示了 Zig 编程语言和 C 编程语言之间的趣味比较。"little-book-of/c" 可能指的是一个关于 C 编程语言的小型入门资源或教程项目。

要点：

*   **项目名称：** little-book-of/c（暗示一个关于 C 的小型入门资源）
*   **主题：** Zig 和 C 之间的比较（标题暗示倾向于 C）
*   **受众：** 对学习 C 或将 C 与 Zig 进行比较的人。
*   **互动：** 分叉数相对较低（16），但星数相当可观（332），表明具有一定的受欢迎程度和关注度。

---

## 3. Cloudflare 清理了顶级域名列表中的 Aisuru 僵尸网络

**原文标题**: Cloudflare Scrubs Aisuru Botnet from Top Domains List

**原文链接**: [https://krebsonsecurity.com/2025/11/cloudflare-scrubs-aisuru-botnet-from-top-domains-list/](https://krebsonsecurity.com/2025/11/cloudflare-scrubs-aisuru-botnet-from-top-domains-list/)

Cloudflare正应对Aisuru僵尸网络，该网络由大量受感染的物联网设备组成，并且增长迅速。起因是其域名意外地在Cloudflare最常被请求的网站排名中名列前茅。这个能够发起大规模DDoS攻击的僵尸网络最初使用Google的DNS服务器，但随后切换到Cloudflare的（1.1.1.1），导致其域名在Cloudflare的排名中占据主导地位。

Aisuru域名激增引发了对安全性、品牌混淆（由于模仿主要云提供商）和隐私（一个域名是一个街道地址）的担忧。Cloudflare的回应是编辑了恶意域名，并添加了关于恶意行为影响排名的声明。首席执行官Matthew Prince解释说，排名系统是基于DNS查询量，Aisuru正在操纵该查询量，既攻击Cloudflare的DNS服务，又可能影响排名。

专家们对Cloudflare处理此事的方式存在分歧。一些人，如Renee Burton，承认基于DNS查询对域名进行排名的复杂性。另一些人，如Alex Greenland，批评Cloudflare损害了其排名的完整性，认为该系统应该反映真实的人类使用情况，而不是自动化流量。他建议完全分离恶意域名，因为Cloudflare的排名被广泛用于信任和安全判断。

虽然Cloudflare已经开始从其网站列表中隐藏Aisuru域名，但它们仍然出现在下载的电子表格中。对这些域名的大部分DNS查询来自美国，这与之前关于Aisuru依赖于托管在美国ISP上的受感染物联网设备的发现相符。专家建议阻止以“.su”（前苏联顶级域名）结尾的域名，作为检测潜在Aisuru僵尸网络活动的一种简单方法，因为它经常被用于网络犯罪。

---

## 4. Btop：一款优于 htop 且具有游戏化界面的现代替代品

**原文标题**: Btop: A better modern alternative of htop with a gamified interface

**原文链接**: [https://github.com/aristocratos/btop](https://github.com/aristocratos/btop)

Btop：一款现代C++资源监视器，是htop的替代品，提供游戏风格的菜单系统和完整的鼠标支持。它显示处理器、内存、磁盘、网络和进程的使用情况和统计信息。

主要功能包括响应式UI、进程过滤、轻松排序、树状视图、信号发送、UI配置菜单、自适应缩放网络图、磁盘IO活动、电池电量显示和自定义预设。

该软件支持主题，并在特定目录中搜索主题。它鼓励用户贡献新的主题。欢迎赞助和捐赠。

Btop需要支持真彩色的终端、UTF8区域设置以及支持Unicode盲文图案、几何形状、框线绘制和块元素的字体。Linux（NVIDIA、AMD、INTEL）提供可选的GPU监控依赖项。

提供了适用于各种Linux发行版（openSUSE、Fedora、RHEL/Rocky/AlmaLinux）、FreeBSD、NetBSD、macOS（通过Homebrew）和Linux（通过Homebrew）的安装说明。详细说明了Linux和macOS的编译说明，包括GPU支持和静态链接的选项。对于Linux，用户可以使用Make或CMake进行编译。

---

## 5. 用于符号表达式操作的代数语言（1958）[pdf]

**原文标题**: An Algebraic Language for the Manipulation of Symbolic Expressions (1958) [pdf]

**原文链接**: [https://softwarepreservation.computerhistory.org/LISP/MIT/AIM-001.pdf](https://softwarepreservation.computerhistory.org/LISP/MIT/AIM-001.pdf)

该文档是一个PDF文件，包含“用于操作符号表达式的代数语言”（1958）。然而，所提供的内容主要是PDF元数据和压缩数据流，而非文章的实际文本。存在大量的二进制数据，似乎与字体定义、图像数据和其他PDF格式化元素有关。还有一些看起来像是被压缩的图像数据，以二进制形式存储。

由于文章的核心文本被编码在这些数据流中，因此无法辨别论文的实际内容、论点或结论。从提供的片段中唯一容易提取的信息是标题和文章的撰写年份。

---

## 6. AI 基准测试是个糟糕的笑话——而大语言模型厂商正在暗自发笑

**原文标题**: AI benchmarks are a bad joke – and LLM makers are the ones laughing

**原文链接**: [https://www.theregister.com/2025/11/07/measuring_ai_models_hampered_by/](https://www.theregister.com/2025/11/07/measuring_ai_models_hampered_by/)

生成摘要时出错

---

## 7. 从零开始的C++移动语义 (2022)

**原文标题**: C++ move semantics from scratch (2022)

**原文链接**: [https://cbarrete.com/move-from-scratch.html](https://cbarrete.com/move-from-scratch.html)

本文从头开始解释 C++ 移动语义，首先设想一种不存在移动语义的场景。 旨在提供清晰的理解，并在最初的解释中弱化 `std::move` 的作用。

核心概念是右值引用 (`&&`) 本质上是常规左值引用 (`&`) 的“着色”版本。 它们的行为相同但互不兼容，从而允许函数重载来区分它们。 这种区分实现了一种特定的优化策略：无需复制大型数据结构（如 vectors），可以通过转移所有权来“移动”或“窃取”数据。 这涉及复制元数据并指向现有的堆分配数据，然后将原始容器置为空以防止错误。

本文介绍了这个想法的演变，最终使用右值引用来表示“移动”数据而不是复制的意图。 创建特殊的构造函数和赋值运算符来接受右值引用。 在其中，编写算法以从一个对象“窃取”数据并将数据传输到另一个对象。

然后，文章讨论了资源管理应用程序，例如 `std::shared_ptr` 和 `std::unique_ptr`，其中移动可以避免昂贵的引用计数更新或强制执行独占所有权。

最后，文章解释了 `std::move` 仅仅是一个到右值引用的强制转换。 它调用函数的特定重载或构造函数，按照惯例，该函数或构造函数实现“移动”操作，如果移动不适用，则回退到复制。 关键在于，移动语义是由旨在不同地处理右值引用的函数重载驱动的，而不是由任何固有的魔力驱动的。

---

## 8. Zig 为什么这么酷？

**原文标题**: Why is Zig so cool?

**原文链接**: [https://nilostolte.github.io/tech/articles/ZigCool.html](https://nilostolte.github.io/tech/articles/ZigCool.html)

本文介绍了 Zig 编程语言，它因能够编译 C 代码并交叉编译到不同的架构而备受赞誉。文章强调了 Zig 独特的编程方法，超越了简单地替代 C/C++。

文章指导初学者安装 Zig 编译器并构建一个基本的 "Hello World!" 程序。然后深入探讨 Zig 的核心概念和命令，包括变量声明、结构体、匿名结构体、测试块和位域。文章重点介绍了 Zig 的循环和数组语法，强调自动类型推断和高效的内存管理。

讨论的一个关键特性是 Zig 的“测试块”，它允许在模块内进行测试，而无需单独的可执行文件，从而方便原型设计和验证。文章还介绍了 Zig 使用带有函数的结构体实现的面向对象编程功能，并解释了如何构建和执行 Zig 程序。

调试部分介绍了使用 `@breakpoint` 内置函数，这是一种用于调试没有符号的优化代码的“hack”方法，使开发人员能够使用 `std.debug.print` 在特定点检查变量值。

最后，文章简要介绍了 Zig 在底层编程方面的能力。

---

## 9. Valdi – 提供原生性能的跨平台UI框架

**原文标题**: Valdi – A cross-platform UI framework that delivers native performance

**原文链接**: [https://github.com/Snapchat/Valdi](https://github.com/Snapchat/Valdi)

Valdi：为原生性能和开发者效率而生的跨平台UI框架。目前正处于beta阶段，但已在Snap的生产应用中使用8年。与其他依赖Web视图的跨平台框架不同，Valdi将声明式的TypeScript UI代码直接编译成iOS、Android和macOS的原生视图，消除了JavaScript桥接。

主要优势包括：通过自动视图回收、优化组件渲染、优化的布局引擎和视口感知渲染等功能实现真正的原生性能。Valdi强调开发者体验，提供即时热重载、完整的VSCode调试和熟悉的TSX语法。其灵活的采用模式允许将Valdi组件嵌入到现有的原生应用程序中，反之亦然。它支持使用C++、Swift、Kotlin或Objective-C编写性能关键代码，并具有与TypeScript的类型安全绑定。

Valdi通过自动代码生成绑定、直接访问原生API、TypeScript和原生代码之间的双向通信以及原生protobuf支持，提供深入的原生集成。该框架为Snap应用中的关键功能提供支持，包括高级动画和复杂手势。

它具有Flexbox布局系统、工作线程、原生动画、高级手势识别、内置测试框架和Bazel集成。可通过Discord获得支持，该项目采用MIT许可证。

---

## 10. 使民主运作：修复和简化平等Paxos

**原文标题**: Making Democracy Work: Fixing and Simplifying Egalitarian Paxos

**原文链接**: [https://arxiv.org/abs/2511.02743](https://arxiv.org/abs/2511.02743)

本文 arXiv 文章“使民主发挥作用：修复和简化平等 Paxos”（EPaxos*）介绍了一种经过纠正和简化的平等 Paxos (EPaxos) 状态机复制协议。作者 Fedor Ryabinin、Alexey Gotsman 和 Pierre Sutra 解决了原始 EPaxos 中存在的复杂性、模糊规范和错误。

EPaxos 是一种无领导者共识协议，旨在克服与基于领导者的协议（如 Paxos）相关的单点故障和延迟问题。它允许副本协同排序命令，即使在 *n* = 2*f*+1 个进程中最多发生 *f* 个进程崩溃，也能保持吞吐量。在更有利的故障条件下（不超过 *e* = ⌈(f+1)/2⌉ 个故障和可交换命令），EPaxos 仅需两次消息延迟即可实现快速命令执行。

EPaxos* 的主要贡献是一种更简单且经过严格证明是正确的故障恢复算法。此外，该协议将 EPaxos 推广到支持更广泛的故障阈值，特别是 *n* ≥ max{2*e*+*f*-1, 2*f*+1}，作者声称这是最优的。本文的扩展版本已在 OPODIS'25 上发表。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 2 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 3 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 4 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 5 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 6 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 7 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 8 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 9 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 10 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 11 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 12 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 13 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 14 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 15 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 16 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 17 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 18 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 19 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 20 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 21 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 22 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 23 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 24 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 25 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 26 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 27 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 28 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 29 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 30 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 31 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 32 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 33 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 34 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 35 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 36 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 37 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 38 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 39 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 40 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 41 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 42 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 43 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 44 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 45 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 46 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 47 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 48 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 49 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 50 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 51 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 52 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 53 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 54 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 55 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 56 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 57 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 58 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 59 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 60 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 61 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 62 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 63 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 64 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 65 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 66 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 67 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 68 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 69 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 70 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 71 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 72 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 73 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 74 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 75 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 76 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 77 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 78 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 79 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 80 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 81 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 82 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 83 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 84 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 85 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 86 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 87 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 88 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 89 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 90 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 91 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 92 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 93 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 94 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 95 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 96 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 97 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 98 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 99 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 100 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 101 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 102 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 103 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 104 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 105 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 106 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 107 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 108 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 109 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 110 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 111 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 112 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 113 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 114 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 115 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 116 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 117 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 118 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 119 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 120 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 121 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 122 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 123 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 124 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 125 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 126 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 127 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 128 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 129 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 130 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 131 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 132 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 133 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 134 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 135 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 136 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 137 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 138 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 139 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 140 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 141 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 142 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 143 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 144 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 145 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 146 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 147 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 148 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 149 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 150 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 151 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 152 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 153 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 154 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 155 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 156 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 157 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 158 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 159 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 160 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 161 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 162 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 163 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 164 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 165 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 166 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 167 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 168 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 169 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 170 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 171 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 172 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 173 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 174 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 175 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 176 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 177 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 178 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 179 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 180 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 181 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 182 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 183 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 184 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 185 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 186 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 187 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 188 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 189 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 190 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 191 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 192 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 193 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 194 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 195 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 196 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 197 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 198 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 199 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 200 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 201 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 202 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 203 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 204 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 205 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 206 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 207 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 208 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 209 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 210 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 211 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 212 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 213 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 214 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 215 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 216 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 217 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 218 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 219 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 220 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 221 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 222 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 223 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 224 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 225 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 226 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 227 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 228 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 229 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 230 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 231 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 232 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 233 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
