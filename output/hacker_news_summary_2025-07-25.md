# Hacker News 热门文章摘要 (2025-07-25)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 是DE9，不是DB9

**原文标题**: It's DE9, Not DB9

**原文链接**: [https://news.sparkfun.com/14298](https://news.sparkfun.com/14298)

这篇SparkFun文章澄清了一个关于9针串口连接器的常见误解，该连接器常被错误地称为“DB9”。 从技术上讲，正确的名称是“DE9”。 文章解释说，在D-sub微型连接器标准中，第一个字母(“D”)表示D形，第二个字母表示外壳尺寸。“B”表示25针外壳，而“E”表示9针外壳。 因此，“DB9”是一个用词不当的名称，因为它将25针外壳的标识与9针计数结合在一起。

这篇文章将“DB9”的广泛使用归因于一个历史性的偶然：最初的IBM PC使用DB25进行串行/并行传输，当引入较小的9针连接器时，人们只是简单地沿用了现有的术语。

尽管知道大多数人搜索“DB9”，SparkFun还是选择准确地命名他们的新DE9连接器分线板。 他们强调技术准确性的重要性，并希望通过他们的产品命名来教育社区。 他们认为使用“DE9”是纠正长期混淆的一小步。

---

## 2. 游戏中的车辆编程

**原文标题**: Programming Vehicles in Games

**原文链接**: [https://wassimulator.com/blog/programming/programming_vehicles_in_games.html](https://wassimulator.com/blog/programming/programming_vehicles_in_games.html)

本文探讨了游戏中车辆编程的基础知识，强调了逼真模拟和期望玩家体验之间的平衡。文章指出，游戏并非物理引擎，操纵现实是提供引人入胜的驾驶体验的关键，并对比了《马里奥赛车》和《iRacing》等游戏。

作者概述了一个车辆模拟的概念模型，将其分解为三个核心组件：引擎（和变速箱）、车轮和轮胎以及底盘。引擎充当扭矩计算器，受油门和换挡的影响，利用扭矩曲线根据RPM真实地改变功率输出。变速箱是一个简单的齿轮比查找表，对加速度产生重大影响。车轮和轮胎涉及复杂的物理原理，包括轮胎模型，该模型根据扭矩、刹车、转向、重量和摩擦力等因素确定纵向和横向力。底盘是刚体，对来自轮胎和外部因素的力做出反应。

文章强调，没有游戏能完全模拟车辆动力学的各个方面，开发者需要有意识地选择模拟、伪造和作弊的内容。作者分享了他们在AV Racer上的经验，这是一个早期尝试车辆模拟的项目，它依赖于各种技巧和窍门来唤起驾驶的感觉。他们了解到，虽然伪造可以让你走得很远，但理解真实的物理原理对于避免破碎的幻觉和突破模拟的极限至关重要。

---

## 3. LLM API 最新价格一览

**原文标题**: Up to date prices for LLM APIs all in one place

**原文链接**: [https://pricepertoken.com/](https://pricepertoken.com/)

本文提供OpenAI、Anthropic和Google等主要LLM（大型语言模型）API的最新定价信息。用户可以比较各种AI模型的输入和输出成本（每百万tokens），以找到最适合其特定用例的性价比最高的选择。定价图表显示了30种模型的输入和输出成本。该信息最后更新于2025年7月25日，由@aellman整理。读者还可以订阅新闻邮件，每周获取LLM定价变化和新模型发布的更新。文章强调了比较价格的重要性，因为存在基于提示长度的分级定价结构，特别指出显示的某些模型的价格适用于20万tokens或以下的提示。

---

## 4. 谁拥有最快的F1网站(2021)

**原文标题**: Who has the fastest F1 website (2021)

**原文链接**: [https://jakearchibald.com/2021/f1-perf-part-3/](https://jakearchibald.com/2021/f1-perf-part-3/)

本文是分析一级方程式车队网站加载性能系列文章的第三部分。 本期评估红牛本田车队的网站。 作者发现红牛的网站在图形方面内容丰富且引人入胜，与2019年的网站相比，性能有了显着提高，总加载时间为8.6秒。

然而，分析发现了一些需要改进的地方。 主要问题包括过度内联CSS（其中大部分未使用）导致的不必要的3秒延迟，以及由于使用JavaScript实现响应式图像而不是原生响应式图像实现导致的10秒延迟。 其他延迟归因于图像和字体的额外连接、糟糕的图像优化以及加载缓慢的Cookie模态框。

作者指出了一个大型主WebP图像和用JavaScript加载的覆盖图像的问题。 覆盖图像的alpha通道对WebP的优化效果不佳，作者建议使用AVIF以获得更好的效果。 作者还批评了用作预览的大型模糊内联图像，并建议使用其他替代方案以实现更好的优化和视觉准确性。

通过解决这些问题，作者估计红牛可以进一步缩短其网站的加载时间，可能实现4.6秒的优化加载时间。 截至本文发表时，红牛在所测试车队的网站性能方面处于领先地位。 作者将在接下来的文章中继续分析其他F1车队的网站。

---

## 5. 二氧化碳电池

**原文标题**: CO2 Battery

**原文链接**: [https://energydome.com/co2-battery/](https://energydome.com/co2-battery/)

能源穹顶的二氧化碳电池为长时储能提供了一种经济高效的解决方案，旨在取代锂离子电池。它通过封闭的热机械转化来实现这一点，通过操纵二氧化碳在其气态和液态之间转换来储存和释放能量。该过程包括蒸发和膨胀二氧化碳以驱动涡轮机并产生电力，拥有超过75%的往返效率，且在30年以上的使用寿命中性能不会下降。

二氧化碳电池的优势包括其全球可部署性，使用容易获得且环保的材料，如水、钢和二氧化碳，从而消除了对锂等稀有金属的依赖。它在环境温度下运行，与压缩空气储能相比，大大降低了成本，并且在运行过程中产生零二氧化碳排放。

能源穹顶强调了二氧化碳电池的可扩展性和模块化，强调其集成了标准的、现成的组件，以便于在全球范围内部署和降低成本。它提供各种电网服务，包括时间转移、物理惯性、频率控制和电压调节，使其成为电网稳定的多功能解决方案。该公司还宣布了包括与谷歌在内的战略合作伙伴关系，并正在通过在亚太地区设立新的总部来扩大其全球影响力。

---

## 6. 如何简单配置X11

**原文标题**: How to configure X11 in a simple way

**原文链接**: [https://eugene-andrienko.com/en/it/2025/07/24/x11-configuration-simple.html](https://eugene-andrienko.com/en/it/2025/07/24/x11-configuration-simple.html)

FreeBSD 上配置 X11 打造精简桌面环境：本文详述如何在 FreeBSD 上配置 X11，使用简单成熟的工具打造配置良好的桌面环境，避免臃肿的大型桌面环境。内容涵盖高 DPI 设置、键盘配置、指点设备、屏幕保护程序、合成器和默认应用程序分配等关键方面。

**高 DPI：** 避免使用环境变量，直接在 xorg.conf 中设置 "DisplaySize" 可影响整个系统的 DPI，解决缩放问题。针对 Librewolf 的特定修复包括在 `about:config` 中调整 `ui.textScaleFactor`。

**键盘：** 本文解释了如何使用 `setxkbmap` 和 `xmodmap` 配置键盘布局、切换键、组合键和 CapsLock 键重映射。然后将配置转换为 xorg.conf，以便在系统范围内应用。

**多媒体键：** 作者使用 `xev` 检测键码，然后在 WM 的配置文件（本例中为 StumpWM）中进行映射。

**指点设备：** 触摸板被禁用，Trackpoint 无需配置即可使用，Logitech Trackman Marble 轨迹球的按钮映射和滚动模拟在 xorg.conf 中进行自定义。

**屏幕保护程序：** 详细介绍了如何使用 XScreenSaver 以及如何使用 `xscreensaver-command` 为全屏视频禁用它。

**合成器：** 使用 `xcompmgr` 进行配置，实现透明和阴影效果。

**默认应用程序：** 本文讨论了如何配置 xdg-utils 以使用 Emacs Dired 进行文件管理，Emacs Compose 模式进行电子邮件，nSxiv 用于图像，MPV 用于视频/音频，以及 Emacs PDF-tools 用于 PDF 查看。

**美学：** 提供了通过编辑配置文件来更改光标主题、GTK 主题、Qt 主题、Librewolf 主题、字体和图标的说明。

---

## 7. Linux 上字体渲染的糟糕现状

**原文标题**: The sad state of font rendering on Linux

**原文链接**: [https://pandasauce.org/post/linux-fonts/](https://pandasauce.org/post/linux-fonts/)

本文批评了 Linux 上的字体渲染，认为由于亚像素渲染、微调和定位等方面的问题，其在可读性和美观性方面落后于 Windows。作者倾向于 Windows 的 ClearType 渲染，解释了基本的字体渲染概念，并比较了 Windows、macOS 和 Linux 上的实现。

Windows 因其先进的技术应用而受到赞扬，而 macOS 则因其模糊和不一致的渲染而受到批评，尤其是在放弃亚像素抗锯齿之后。

本文深入研究了 Linux 使用的 FreeType 库，探讨了不同的渲染引擎（v35、v38、v40）和自动微调器，强调了它们的权衡。作者偏爱 v38 引擎，在不太理想的条件下，v40 是第二选择。

无论使用何种引擎，Linux 上的核心问题都被认为是由于缺乏亚像素网格支持而导致的错误的字距调整和字母间距，从而导致字符之间出现视觉上不吸引人的间隙。虽然 Google 的 Skia 提供了亚像素定位的解决方案，但它尚未被广泛采用或默认启用。 Cairo 最近对亚像素定位的支持正在取得进展，这可能会改善 GTK 和其他应用程序中的文本渲染。 作者强调，一些 Windows 用户使用 MacType 在 Windows 上模拟模糊的 OS X 字体渲染，这具有讽刺意味。 文章最后阐述了与亚像素渲染相关的困难和挫败感，强调修复缺乏亚像素定位的问题非常复杂，需要付出巨大的努力。

---

## 8. 可空但非空

**原文标题**: nullable but not null

**原文链接**: [https://efe.me/posts/nullable-but-not-null/](https://efe.me/posts/nullable-but-not-null/)

本文探讨了在后端应用程序演进过程中常见的可空数据库字段实际上从不包含空值的问题。文章指出，虽然最初将字段设置为可空通常是为了方便迁移（例如，添加新列时），但开发人员经常忘记在回填现有数据后更新模式，使其变为不可空。

作者认为，模式与实际数据之间的这种不匹配可能导致混淆、约束缺失以及代码中不必要的复杂性。当字段实际上是必需的时，将其保留为可空会使数据模型更难信任，并错失了提高清晰度和安全性的机会。

为了解决这个问题，本文介绍了一个 Python 脚本（使用 Django ORM）来分析所有模型，并识别空值百分比为 0% 的可空字段。该脚本确定每个模型中每个可空字段的空值百分比，并提供一份报告，指出可能适合变为不可空的字段。

作者建议将此分析集成到命令行工具、管理报告或健康检查中。关键在于，旨在成为必需的字段应在数据库模式中反映出来，以确保数据完整性和更可靠的应用程序。纠正这些“可空但非空”字段有助于建立更清晰、更准确的数据模型，并使应用程序整体更加健康。

---

## 9. MIT为何从Scheme切换到Python (2009)

**原文标题**: Why MIT Switched from Scheme to Python (2009)

**原文链接**: [https://www.wisdomandwonder.com/link/2110/why-mit-switched-from-scheme-to-python](https://www.wisdomandwonder.com/link/2110/why-mit-switched-from-scheme-to-python)

本文阐述了麻省理工学院为何将其入门编程课程 6.001 从 Scheme 语言切换到 Python 语言。据 Gerald Sussman 称，这一转变反映了编程从一种深思熟虑的理论实践演变为一种更具经验性的“摸索”方法。

Sussman 解释说，在 20 世纪 80 年代，程序员通过对底层系统的深刻理解来设计高效、易懂的代码。6.001 旨在教导学生如何从完全理解的组件构建复杂的系统。

然而，到了 20 世纪 90 年代和 21 世纪 2000 年代，编程涉及到使用文档匮乏的库和不熟悉的代码。程序员需要通过实验和逆向工程来理解这些组件的工作原理。 这需要不同的技能组合，促使 6.001 需要一种新的方法。

重新设计的课程以机器人为中心，要求学生为机器人编程。这引入了在理想化系统中找不到的挑战，例如车轮打滑和环境可变性，这需要强大的系统设计。

切换到 Python 的主要原因是其现有的机器人接口库，使其成为新课程的实用选择。虽然 Scheme 强调理论理解，但 Python 促进了现代编程挑战所需的实用、实验性方法。

---

## 10. 展示 HN：蒙大拿迷你计算机

**原文标题**: Show HN: The Montana MiniComputer

**原文链接**: [https://mtmc.cs.montana.edu/](https://mtmc.cs.montana.edu/)

蒙大拿微型计算机 (MTMC-16) 是一款虚拟教育计算机，旨在直观地演示数字计算。它受 PDP-11、MIPS、Scott CPU、Game Boy 和 JVM 等架构的启发，是一款简化的 16 位计算机，能够执行基本的计算任务。

它通过一个 Web 界面访问，该界面具有控制台、显示器、代码编辑器和计算机内部状态的可视化表示，从而方便软件构建和调试。

主要规格包括：

*   16 位架构
*   字节寻址内存，容量为 4KB（4096 字节/地址，2048 字）
*   16 个寄存器
*   160x144 2 位灰度显示
*   基于文本的控制台 I/O
*   包含操作系统 (MTOS)

MTMC-16 使用带符号的 16 位整数和字节作为核心数据类型。

该项目在 GitHub 上提供，包括可下载的 JAR 文件、快速入门指南、计算机规格、汇编语言指南和常见问题解答。它需要一台装有 Java 21+ 和现代 Web 浏览器的台式电脑、虚拟机或服务器。它包含许多对现有架构、指南和相关技术的引用，突出了其教育目标。

---

## 11. 量子科学家构建了一种新的密码学数学

**原文标题**: Quantum Scientists Have Built a New Math of Cryptography

**原文链接**: [https://www.quantamagazine.org/quantum-scientists-have-built-a-new-math-of-cryptography-20250725/](https://www.quantamagazine.org/quantum-scientists-have-built-a-new-math-of-cryptography-20250725/)

本文探讨了一种新的量子密码学方法，旨在克服传统密码学的局限性。传统密码学依赖于某些数学难题的难度，一旦这些难题被解决，经典密码学就会崩溃。

研究人员正在探索量子物理学，以创建更安全的密码系统。最近的一篇论文详细介绍了一条通往量子密码学的路径，该路径绕过了对那些复杂数学难题的需求。这种由Dakshita Khurana和Kabir Tomer开发的新方法，侧重于单向函数的量子版本，并引入了一个名为“单向谜题”的概念。这些谜题涉及量子和经典属性的复杂混合，生成易于生成但难以打开的锁和密钥，即使使用密钥也是如此。

研究人员将这些单向谜题直接与一个潜在的更安全的数学基石联系起来：矩阵永久量问题，该问题以其极高的难度和缺乏简单的解法验证方法而闻名。通过将量子密码学的安全性与解决矩阵永久量问题的难度以及证明量子计算优于经典计算机的优势联系起来，他们创造了一个基础，该基础可能使量子密码学比当前的经典方法更加强大。虽然该技术尚未准备好立即实施，但这项研究为密码学更安全的未来迈出了重要一步。

---

## 12. Show HN: 一款在全屏编码或煲剧时保持可见的macOS时钟

**原文标题**: Show HN: A macOS clock that stays visible when coding or binging in fullscreen

**原文链接**: [https://cornertime.app/en](https://cornertime.app/en)

Corner Time：一款macOS实用工具，专为喜欢极简、无干扰工作空间的用户设计，它通过隐藏菜单栏来实现这一点。它解决了一直需要显示菜单栏才能查看时间的麻烦，在屏幕角落显示一个可自定义的时钟。

由于其“置于应用之上”的窗口层级设置，该应用即使在全屏模式下也保持可见。用户可以自定义时钟的外观，包括 12/24 小时制格式、秒、日期和星期显示、自定义格式以及各种字体（计划支持本地字体）。它还提供多显示器支持，允许用户在单个屏幕上启用或禁用时钟。时钟自动以用户系统语言显示时间，目前支持 10 种语言。

用户评价强调了 Corner Time 对那些为了获得简洁外观而隐藏菜单栏和 Dock 的用户的实用性，赞扬了它的简单性、功能性和周到的自定义选项。

该应用售价 1.99 美元，需要 macOS 13.0 或更高版本，并且下载文件很小，仅为 525 KB。它被定位为数字极简主义和不间断工作流程的解决方案，为始终可见的时间访问提供原生般的体验。开发者提供媒体资料包和联系信息以供查询。

---

## 13. 使用图归约实现函数式语言

**原文标题**: Implementing a Functional Language with Graph Reduction

**原文链接**: [https://thma.github.io/posts/2021-12-27-Implementing-a-functional-language-with-Graph-Reduction.html](https://thma.github.io/posts/2021-12-27-Implementing-a-functional-language-with-Graph-Reduction.html)

本文介绍了使用 Haskell 通过图归约实现小型函数式语言的过程。它将该过程分解为三个主要部分：解析、编译和图归约。

该语言基于无类型 lambda 演算，并扩展了整数和一个用于命名表达式的顶层环境。解析器源自“A Combinatory Compiler”，它使用 `Expr` 数据类型将源代码转换为内部表示形式。

编译器使用括号抽象将 lambda 表达式转换为组合子逻辑，通过使用 S、K 和 I 组合子（以及 B、C 用于优化）重写项来消除变量。本文重点介绍了组合子项大小的问题，并介绍了优化技术，包括简化表达式和提高效率的规则。

实现的核心是图归约器。组合子项表示为一个二叉图，使用可变引用 (`STRef`) 以启用节点共享和就地归约。本文解释了图归约，展示了它如何实现正规序（惰性）求值、避免冗余计算并隐式管理变量作用域。一个详细的例子说明了 `sqr` 函数的归约过程，通过多个步骤跟踪图的转换，其中应用了 S、I、MUL 和 ADD 组合子。代码示例提供了分配图结构的数据结构和函数。

---

## 14. 英伟达发布开放推理AI模型系列：OpenReasoning Nemotron

**原文标题**: Nvidia Launches Family of Open Reasoning AI Models: OpenReasoning Nemotron

**原文链接**: [https://nvidianews.nvidia.com/news/nvidia-launches-family-of-open-reasoning-ai-models-for-developers-and-enterprises-to-build-agentic-ai-platforms](https://nvidianews.nvidia.com/news/nvidia-launches-family-of-open-reasoning-ai-models-for-developers-and-enterprises-to-build-agentic-ai-platforms)

英伟达推出具备推理能力的开放Llama Nemotron系列AI模型，旨在帮助开发者和企业构建用于复杂任务的先进AI智能体。这些模型基于Llama模型构建，并通过英伟达的后训练进行增强，在数学、编码、推理和决策制定等领域有所改进，与其他开放推理模型相比，准确率提高了高达20%，推理速度提高了5倍。

Llama Nemotron系列提供Nano、Super和Ultra三种尺寸，以NVIDIA NIM微服务的形式交付，以满足不同的部署需求。其开发的关键在于使用高质量、精选的合成数据，用于优化的工具也将公开提供。

埃森哲、微软、SAP和ServiceNow等行业领导者已经与英伟达合作，将这些模型集成到他们的智能体AI平台中。例如，微软正在将它们整合到Azure AI Foundry中，而SAP正在使用它们来增强其AI助手Joule。

为了支持这些模型的采用，英伟达还在NVIDIA AI Enterprise平台中提供新的智能体AI工具和软件，包括用于将知识连接到AI智能体的NVIDIA AI-Q Blueprint、NVIDIA AI Data Platform以及新的NVIDIA NIM和NeMo微服务。

Llama Nemotron Nano和Super模型可通过build.nvidia.com和Hugging Face获取。NVIDIA AI-Q Blueprint预计将于4月发布。

---

## 15. 显示 HN：苹果健康 MCP 服务器

**原文标题**: Show HN: Apple Health MCP Server

**原文链接**: [https://github.com/neiltron/apple-health-mcp](https://github.com/neiltron/apple-health-mcp)

此“Show HN”介绍 `apple-health-mcp`，一个MCP（模型上下文协议）服务器，允许用户使用SQL查询他们的Apple Health数据。它基于DuckDB构建，可对从Simple Health Export CSV iOS应用导出的健康数据进行快速高效的分析。

主要功能包括自然语言查询支持（通过MCP客户端）、直接SQL查询执行、自动健康报告生成、具有可配置时间窗口的延迟数据加载以及查询结果缓存。

要使用它，用户需要安装Simple Health Export CSV应用，导出他们的Apple Health数据，并配置Claude Desktop（或其他MCP客户端）以指向该服务器，同时将`HEALTH_DATA_DIR`环境变量设置为导出的CSV文件所在的位置。可选的环境变量允许用户配置内存使用量 (`MAX_MEMORY_MB`) 和缓存大小 (`CACHE_SIZE`)。

该服务器期望特定的CSV文件命名模式（例如，`HKQuantityTypeIdentifier*.csv`）和列结构（类型、sourceName、startDate、endDate、value、unit）。可用工具包括 `health_schema`（表信息）、`health_query`（SQL执行）和 `health_report`（综合报告）。

该项目是开源的（MIT许可），欢迎贡献，请遵循代码风格、TypeScript类型、错误处理和性能注意事项的指导原则。该文档还提供了针对常见问题的故障排除技巧，例如数据加载、内存错误和慢查询。

---

## 16. 研究人员重视无效结果，但难以发表。

**原文标题**: Researchers value null results, but struggle to publish them

**原文链接**: [https://www.nature.com/articles/d41586-025-02312-4](https://www.nature.com/articles/d41586-025-02312-4)

本文讨论了一项调查，该调查揭示了研究人员对零结果的认知与他们的发表实践之间存在显著脱节。尽管98%的研究人员认识到零结果（未证实假设的结果）的价值，85%的人认为分享零结果很重要，但只有30%的人尝试在期刊上发表它们。

这项由施普林格·自然进行的调查，确定了这种不情愿的主要原因。很大一部分研究人员担心被拒稿，缺乏对合适期刊的认识，担心资金覆盖问题，并害怕负面的同行看法。这种不情愿造成了不完整且可能具有误导性的研究图景。

像马库斯·穆纳弗这样的专家强调，大多数科学研究都会产生零结果，因此发表零结果对于更准确的记录至关重要。此外，发表了零结果的研究人员报告了一些好处，例如激发了新的假设（39%）和防止了不必要的重复研究（28%）。本文强调需要提高对如何以及为何分享零结果的认识，并呼吁改变研究生产力评估方式，以鼓励发表零结果。一位匿名研究人员甚至感叹由于缺乏相关零结果的广泛传播而损失了两年研究时间。

---

## 17. 量化人工智能的进步需要准确和透明的评估

**原文标题**: Quantitative AI progress needs accurate and transparent evaluation

**原文链接**: [https://mathstodon.xyz/@tao/114910028356641733](https://mathstodon.xyz/@tao/114910028356641733)

量化人工智能进展需要准确透明的评估

这篇题为《量化人工智能进展需要准确透明的评估》的短文强调了在人工智能技术成熟过程中，严格且开放的评估的重要性。作者陶哲轩暗示，随着人工智能技术变得更加先进，重点应该从简单地展示进展转变为通过定量方法更精确地衡量和理解这种进展。

这篇文章，似乎是Mastodon上的一个帖子，表明人们越来越需要准确、透明和可量化的指标来评估人工智能系统的能力和局限性。这对于理解人工智能发展的真实状态、确定需要改进的领域以及确保该技术的负责任和有益的应用至关重要。引用的文本表明了陶哲轩的观点，即随着人工智能的成熟，重点应该转变。本质上，这篇文章提倡随着该领域的进步，采用更科学和数据驱动的方法进行人工智能评估。

---

## 18. Dwl: Wayland下的Dwm

**原文标题**: Dwl: Dwm for Wayland

**原文链接**: [https://codeberg.org/dwl/dwl](https://codeberg.org/dwl/dwl)

无法访问文章链接。

---

## 19. 互联网档案馆现在是联邦政府文件托存图书馆

**原文标题**: Internet Archive Is Now a Federal Depository Library

**原文链接**: [https://www.kqed.org/news/12049420/sf-based-internet-archive-is-now-a-federal-depository-library-what-does-that-mean](https://www.kqed.org/news/12049420/sf-based-internet-archive-is-now-a-federal-depository-library-what-does-that-mean)

互联网档案馆被加州参议员亚历克斯·帕迪利亚指定为联邦文献托存图书馆，加入了一个由1100多家图书馆组成的网络，该网络向公众提供政府文件。帕迪利亚称赞互联网档案馆的“数字化重点”及其在数字时代扩大政府出版物获取能力。

互联网档案馆创始人布鲁斯特·卡利强调，这一指定将促进与其他联邦文献托存图书馆的合作，加强互联网生态系统，并提供更好的政府资料获取途径。联邦文献托存图书馆计划始于1813年，旨在确保公众可以获取政府记录，包括地图、报告、国会记录和书籍。互联网档案馆的“民主图书馆”——一个免费的政府研究和出版物在线汇编——将受益于此次合作，从而提供更可靠的资料访问。

然而，互联网档案馆正面临着关于其存档实践的持续法律挑战，包括出版商和音乐公司因其开放图书馆和Great 78项目相关的版权问题提起的诉讼。这些诉讼威胁着该组织的生存。尽管面临法律诉讼，卡利坚称，互联网档案馆正在履行其保存和提供知识获取的使命，适应数字时代，并帮助教育公众。互联网档案馆还运营着Wayback Machine，用于存档网页和保存政府信息。

---

## 20. 庆祝 MDN 二十周年

**原文标题**: Celebrating 20 Years of MDN

**原文链接**: [https://developer.mozilla.org/en-US/blog/mdn-turns-20/](https://developer.mozilla.org/en-US/blog/mdn-turns-20/)

本文庆祝 MDN Web Docs 成立 20 周年，重点介绍了其从社区驱动的 Wiki 发展成为 Web 开发人员的综合资源的过程。最初，MDN 致力于应对日益复杂的 Web 并推广 Web 标准，如今，它拥有近 14,000 个文档页面、超过 33,000 篇本地化文章以及约 18,000 个功能的兼容性数据。

本文强调了 MDN 在帮助各种技能水平的开发人员构建更好的 Web 方面的影响。文章还描述了浏览器制造商交换蛋糕以庆祝里程碑的传统，突显了 Web 开发社区内的合作精神。特别感谢 web.dev 团队提供的 MDN 生日蛋糕。

本文肯定了 MDN 全球社区的重要作用，该社区包含数百万月度用户和超过 100,000 名 GitHub 贡献者。文章鼓励读者分享他们的 MDN 体验，并为平台的未来做出贡献，强调了塑造 MDN 下一个篇章的机会。最后，文章展望未来 20 年，继续赋能开发者并促进更好的 Web 发展。

---

## 21. 游戏画面不佳：HDR与色调映射 (2017)

**原文标题**: Games Look Bad: HDR and Tone Mapping (2017)

**原文链接**: [https://ventspace.wordpress.com/2017/10/20/games-look-bad-part-1-hdr-and-tone-mapping/](https://ventspace.wordpress.com/2017/10/20/games-look-bad-part-1-hdr-and-tone-mapping/)

Promit的文章《游戏画面不佳：HDR与色调映射（2017）》批判了视频游戏中高动态范围(HDR)和色调映射的过度使用和误用，认为这些旨在提高视觉保真度的技术，往往导致一种未能模仿电影或摄影的真实感的“游戏化”美学。

作者解释说，HDR用于存储照明计算的宽范围亮度，而色调映射则将此范围压缩以便在屏幕上显示。然而，游戏开发者经常使用具有激进对比度曲线、去饱和和有缺陷的亮度响应的“粗劣”色调映射。Promit认为，游戏通常盲目地使用相同的色调映射函数（如Reinhard、Hable或ACES RRT），而不了解它们的局限性或预期用途，从而导致游戏之间视觉上的统一性。

他将此与电影行业进行对比，后者会仔细考虑色彩科学和胶片选择，以实现特定的美学品质。Arri的Alexa相机在视觉吸引力上优先于纯技术规格（如分辨率）的成功，突出了这一点。

Promit提倡通过寻找不过度去饱和、改善对比度过渡并利用行业标准工具进行LUT创作来修复色调映射。他称赞了《生化危机7》（风格化对比度）、《杀出重围：人类分裂》（特定场景）和《极限竞速：地平线3》（低对比度，中色调焦点）等游戏，因为它们有效地处理了HDR。

最终，作者断言问题不仅在于技术，还在于美学。在渲染管线的输出阶段做出的错误选择正在对游戏的整体外观产生负面影响。他鼓励游戏开发者将色调映射视为视觉开发的基础要素，从一开始就专注于美学质量。

---

## 22. 女性约会安全App“Tea”遭泄露，用户ID被发布至4chan

**原文标题**: Women dating safety app 'Tea' breached, users' IDs posted to 4chan

**原文链接**: [https://www.404media.co/women-dating-safety-app-tea-breached-users-ids-posted-to-4chan/](https://www.404media.co/women-dating-safety-app-tea-breached-users-ids-posted-to-4chan/)

女性约会安全应用“Tea”遭数据泄露，用户数据（包括自拍照和潜在的驾驶执照）在4chan上曝光。4chan用户声称在谷歌Firebase平台上发现了一个不安全的数据库，并正在访问和分享Tea用户的个人信息。Tea是一款旨在让女性分享男性信息以保障安全的应用程序，通过要求自拍来验证用户身份。据报道，泄露的数据包括两年前的私信。这款最近登上App Store排行榜榜首并拥有超过160万用户的应用程序，目前正面临一场重大的隐私危机。4chan用户正在敦促其他人趁数据未被保护前访问数据。

---

## 23. Steam和Itch.io下架“色情”游戏，评论家称此举是危险的开端。

**原文标题**: Steam, Itch.io Are Pulling 'Porn' Games. Critics Say It's a Slippery Slope

**原文链接**: [https://www.wired.com/story/steam-itchio-are-pulling-porn-games-censorship/](https://www.wired.com/story/steam-itchio-are-pulling-porn-games-censorship/)

在集体呼喊组织（一个反对将女性物化和性化的组织）的压力下，Itch.io和Steam正在从其平台上移除或取消索引成人主题游戏。该组织针对Steam和Itch.io使用的支付处理商，敦促他们停止与这些平台开展业务，理由是它们托管的内容，这是一种被称为金融审查的策略。Steam移除了数百款包含据称虐待、强奸或乱伦内容的游戏，而Itch.io取消了所有成人NSFW游戏的索引，无论其标签原因如何。

批评者认为这构成了审查，对酷儿、女性和有色人种创作者造成了不成比例的影响，即使是那些拥有获奖作品的创作者。涉及心理健康、饮食失调和家庭暴力的游戏也受到了影响，而不仅仅是那些包含露骨性内容的游戏。开发者表示担心支付处理商对内容审核拥有过大的权力，允许反色情和反LGBTQ群体来决定可以销售什么。

集体呼喊组织为自己的行为辩护说，它并非普遍反对色情，而是反对描绘针对女性的暴力和虐待的内容。他们声称，以强奸和乱伦为主题的游戏不应在言论自由的幌子下受到保护。

这种情况引发了人们对审查滑坡效应、保守派将任何他们不喜欢的东西贴上“色情”标签的可能性的担忧，以及对依赖这些平台获取收入的创作者的影响。这两个平台都在努力遵守支付处理商的要求。

---

## 24. 摄影诞生之初，随之而来的是着迷、痴迷和危险。

**原文标题**: When photography was born, fascination, obsession, and danger followed

**原文链接**: [https://www.washingtonpost.com/books/2025/07/12/flashes-brilliance-history-early-photography-anika-burgess-review/](https://www.washingtonpost.com/books/2025/07/12/flashes-brilliance-history-early-photography-anika-burgess-review/)

无法访问文章链接。

---

## 25. 今日Lisp项目

**原文标题**: Lisp project of the day

**原文链接**: [https://40ants.com/lisp-project-of-the-day/index.html](https://40ants.com/lisp-project-of-the-day/index.html)

这是一份冗长的、编号的Lisp项目列表。它看起来像一个“每日Lisp项目”系列，每个条目代表一个特定的项目。每个条目包括：

*   一个数字，可能表示在该系列中的顺序。
*   项目的名称。
*   对项目功能的简明描述，按相关领域分类，如Web开发、数据结构、系统实用程序、文本处理、图形等。

这些项目涵盖了广泛的应用，包括Web框架、数据序列化、并发、系统管理工具、解析库、图形库、文档生成器和实用程序。重点在于扩展Common Lisp功能的库和工具。列表从项目#0220开始倒数至项目#0000，“零日”，该项目归功于“40Ants”。这表明这是一个持续进行的每日项目展示。文章表明可以通过捐款支持这些项目，并提供了一个项目赞助商的链接。

---

## 26. 通过 DKIM 重放攻击仿冒 Google：技术分析

**原文标题**: Google spoofed via DKIM replay attack: A technical breakdown

**原文链接**: [https://easydmarc.com/blog/google-spoofed-via-dkim-replay-attack-a-technical-breakdown/](https://easydmarc.com/blog/google-spoofed-via-dkim-replay-attack-a-technical-breakdown/)

名为“通过DKIM重放攻击欺骗谷歌：技术解析”的这篇短文，重点关注大型企业对DMARC（基于域的消息认证、报告和一致性）日益增长的采用率。具体而言，它对比了财富500强和Inc. 5000强公司中DMARC的采用率。该文章于2025年7月25日发表，突出了一个差异，可能表明最大型公司和快速增长的公司在电子邮件安全实施方面存在显着差异。核心含义是电子邮件安全实践中存在越来越大的差距。标题中提到的“DKIM重放攻击”表明，该文章可能解释了如何利用此类攻击来欺骗电子邮件并绕过安全措施。DMARC作为防御此类攻击的关键手段，因此至关重要。总的来说，该信息指向DMARC的采用作为一项关键安全措施的重要性，尤其是在复杂的欺骗技术面前，并强调其在不同规模和类型的组织中的实施并不普遍一致。

---

## 27. 巴西央行将于9月推出Pix分期付款功能

**原文标题**: Brazil central bank to launch Pix installment feature in September

**原文链接**: [https://www.reuters.com/technology/brazil-central-bank-launch-pix-installment-feature-september-2025-04-03/](https://www.reuters.com/technology/brazil-central-bank-launch-pix-installment-feature-september-2025-04-03/)

巴西央行计划于2024年9月为其即时支付系统Pix推出分期付款功能。这项名为“Pix Garantido”（有保障的Pix）的新功能将允许用户使用Pix系统分期支付商品和服务，类似于信用卡的工作方式。

“Pix Garantido”的目标是通过为较大额的消费提供信用卡替代方案，进一步扩大Pix的使用，Pix在巴西已经非常受欢迎。预计商家将受益于低于信用卡支付的交易费用，而消费者将获得一种方便且可能更便宜的分期付款选择。

央行预计分期付款的实施将增加企业的销售额，并为可能无法使用信用卡的消费者提供更大的金融包容性。虽然细节仍在最终确定中，但央行强调分期付款功能将优先考虑安全性和用户保护。

---

## 28. 茶App用户面部信息和ID据报在4chan上被泄露，涉及安全漏洞。

**原文标题**: Tea App Users' Faces and IDs Reportedly Posted to 4chan in Security Breach

**原文链接**: [https://www.cnet.com/tech/services-and-software/tea-app-users-faces-and-ids-reportedly-posted-to-4chan-in-security-breach/](https://www.cnet.com/tech/services-and-software/tea-app-users-faces-and-ids-reportedly-posted-to-4chan-in-security-breach/)

热门女性安全约会应用Tea据报遭遇重大安全漏洞。报告显示，由于数据库未受保护，用户面部照片和身份证件（包括驾照）已在4chan上泄露。这些源自Reddit和404 Media的报告声称，泄露的数据是由于Tea要求用户通过自拍或身份证件验证身份所致。

Tea尚未独立证实或评论此次据称的泄露事件。这款旨在让女性举报与男性约会过程中负面经历的应用，最近登上了苹果应用商店排行榜榜首，引发了关于男性潜在隐私侵犯的国际讨论。

据报的安全漏洞进一步引发了人们对在线身份和年龄验证流程相关风险的担忧。虽然Tea的网站声明他们采取了合理的安全措施，但也承认没有系统是完全坚不可摧的。如果确认属实，此次泄露事件凸显了收集和存储敏感用户数据所固有的潜在漏洞。

---

## 29. 实现4-Gbps通信的高速有机发光二极管

**原文标题**: High-speed organic light-emitting diodes achieving 4-Gbps communication

**原文链接**: [https://www.spiedigitallibrary.org/journals/advanced-photonics/volume-7/issue-03/036005/High-speed-organic-light-emitting-diodes-based-on-dinaphthylperylene-achieving/10.1117/1.AP.7.3.036005.full](https://www.spiedigitallibrary.org/journals/advanced-photonics/volume-7/issue-03/036005/High-speed-organic-light-emitting-diodes-based-on-dinaphthylperylene-achieving/10.1117/1.AP.7.3.036005.full)

无法访问文章链接。

---

## 30. Asciinema: 录制并分享你的终端会话

**原文标题**: Asciinema: Record and share your terminal sessions

**原文链接**: [https://asciinema.org](https://asciinema.org)

Asciinema 是一款免费开源的终端会话录制和分享工具。它提供了一种轻量级的、基于文本的替代传统屏幕录制方法，避免了模糊的视频并简化了录制过程。

用户可以通过运行 `asciinema rec [filename.cast]` 命令直接在终端中录制会话，并使用 `ctrl+d` 或 `exit` 结束录制。录制可以暂停，文本可以轻松复制和粘贴。

Asciinema 提供嵌入功能，可以轻松地将录制内容集成到博客文章、文档和演示文稿中。本文重点介绍了使用 Asciinema 录制的几个示例会话，展示了它的多功能性以及在各种上下文中的应用。

---

## 31. 3-JSON

**原文标题**: 3-JSON

**原文链接**: [https://rgbcu.be/blog/3-json/](https://rgbcu.be/blog/3-json/)

本文讨论了`tree`命令行实用程序的“3-JSON”特性，特别是它在文件描述符3 (stddata) 上输出无缩进JSON数据的能力。作者强调了一个有问题的初始实现，其中`tree`命令假定文件描述符3的存在，导致意外行为和“混乱”，因为许多脚本随机处理文件描述符。这个问题已在2.0.2版本中得到解决。

文章解释说，3-JSON特性现在依赖于`STDDATA_FD`环境变量。用户必须将`STDDATA_FD`设置为所需的文件描述符（例如，1代表stdout），才能生成JSON输出。一个例子演示了使用`STDDATA_FD=1 tree`将目录结构以JSON格式输出到stdout。文章随后展示了使用`STDDATA_FD=1 tree | from json`将此JSON输出通过管道传递给`nushell`，但是，来自`nushell`的输出格式未正确呈现。作者使用markdown表格来解决渲染花哨字符的webfont问题。关键在于，虽然3-JSON特性提供了结构化数据输出，但其初始实现存在缺陷，现在需要显式的环境变量配置。

---

## 32. 我的网站是一个二进制文件（2022）

**原文标题**: My website is one binary (2022)

**原文链接**: [https://j3s.sh/thought/my-website-is-one-binary.html](https://j3s.sh/thought/my-website-is-one-binary.html)

JES反对使用Hugo等静态网站生成器来搭建个人网站，尽管它们很流行，但他担心依赖外部项目、社区和不断发展的技术。作者重视他们能够完全理解和独立维护的系统，优先考虑可靠性和长期可用性。

他们偏好的解决方案是用Go构建并部署为单个二进制文件的网站。这种方法可以用最少的代码生成动态内容（例如显示用户IP地址），与通常需要JavaScript和外部依赖项的静态网站相比，简化了复杂的任务。部署通过简单的shell脚本和cron作业进行简化，确保以最小的依赖性自动更新。

JES提倡能够反映个性和实验性的个人网站。他们鼓励读者拥抱动态网站，因为它们具有灵活性、简单性以及构建它们的乐趣。他们强调从小处着手，专注于提供基本的HTML服务，然后再添加功能，并优先使用标准库而不是复杂的框架，以避免精疲力竭。目标是创建一个可维护、可理解且独具个性的网站。

---

## 33. Rapidus IIM-1开始2纳米环绕栅极原型生产

**原文标题**: Rapidus Starts 2nm Gate All Around Prototype Production at IIM-1

**原文链接**: [https://www.servethehome.com/rapidus-starts-2nm-gate-all-around-prototype-production-at-iim-1/](https://www.servethehome.com/rapidus-starts-2nm-gate-all-around-prototype-production-at-iim-1/)

Rapidus已在日本北海道千岁市新建的IIM-1工厂开始2纳米环绕栅极(GAA)晶体管的原型生产。此举旨在将尖端半导体制造技术带回日本。IIM-1工厂于2023年9月开始建设，洁净室于2024年竣工，EUV光刻机于2024年12月安装完毕。首次EUV曝光发生在2025年4月，目前该工厂拥有超过200台可运行的机器。

Rapidus计划在大约三个季度后开始与高端客户合作，目标是在2027年实现量产。文章强调了该工厂在建设中融入的抗震特性，包括钢制阻尼器和专门的柱子设计，使建筑物能够承受地震活动。

鉴于先进半导体的战略重要性，Rapidus IIM-1的开发对半导体行业和日本都具有重要意义。该公司似乎正在按计划实现其生产目标，文章表示有兴趣看到2纳米GAA工艺的实际应用。

---

## 34. 加沙市诊所报告称，五岁以下儿童营养不良情况增加两倍。

**原文标题**: Malnutrition in under-5s has tripled at Gaza City clinic, charity reports

**原文链接**: [https://www.theguardian.com/world/2025/jul/25/severe-malnutrition-under-5s-gaza-city--tripled-two-weeks-charity-msf](https://www.theguardian.com/world/2025/jul/25/severe-malnutrition-under-5s-gaza-city--tripled-two-weeks-charity-msf)

一份新报告显示加沙人道主义局势迅速恶化，过去两周加沙市一家诊所五岁以下儿童的严重营养不良病例增加了两倍。“无国界医生”报告称，自五月以来，需要营养不良护理的人数增加了四倍，四分之一接受筛查的幼儿和孕妇/哺乳期妇女被发现营养不良。

这场危机归因于以色列的“饥饿政策”，援助组织谴责对进入加沙的援助物资的严厉限制。世界粮食计划署报告称，近三分之一的加沙人已经几天没有吃饭，导致营养不良人数激增，影响了9万名妇女和儿童。至少有122人死于饥饿，并且每天都有更多死亡报告。

加沙的医生描述了可怕的状况，产科医生报告说孕妇中存在严重的营养不良，导致流产和婴儿体重不足。医疗用品稀缺，迫使医生使用不卫生的设备。

国际社会的谴责日益增加，联合国秘书长称其为“道德危机”，英国、法国和德国的领导人敦促以色列解除对援助物资的限制。尽管如此，停火谈判已经破裂，以色列和哈马斯互相指责。虽然约旦和阿联酋已经开始空投援助物资，但哈马斯批评这些援助物资不足。试图获得援助的巴勒斯坦人面临的危险使情况更加恶化，据报道，在分配地点有1000多人死亡。

---

## 35. PeteTimesSix的核反应堆模拟器

**原文标题**: Nuclear Reactor SIM by PeteTimesSix

**原文链接**: [https://petetimessix.itch.io/nuclear-reactors](https://petetimessix.itch.io/nuclear-reactors)

PeteTimesSix 的《核反应堆模拟》是一款用 Godot 引擎开发的简单模拟游戏，旨在作为一种教育工具，演示核反应堆的工作原理。该游戏为 Godot Wild Jam #80 而创建，允许玩家通过控制棒组（Q/A、W/S、E/D 键）和水流量（X/C 键）来管理反应堆。

该模拟器很大程度上基于外部视频资源。游戏使用了 Maaack 的游戏模板和来自 Pixabay 的 CC0 声音。

目前，它以原型形式在 HTML5、Windows、macOS 和 Linux 平台上提供。提供了各种版本的下载，包括 Windows、较新的 HTML5 版本和 Linux。

一位用户指出游戏中关于铀 235 的解释不准确（将其质量数误认为是中子数）。开发者 PeteTimesSix 承认了该错误，并已更正该声明。

---

## 36. 细胞也拥有记忆吗？

**原文标题**: Do cells also hold memories?

**原文链接**: [https://www.theglobeandmail.com/canada/article-cells-basic-unit-of-life-memories/](https://www.theglobeandmail.com/canada/article-cells-basic-unit-of-life-memories/)

细胞的记忆与智能：超越基因指令

要点包括：

*   细胞不仅仅是工厂；它们参与复杂的互动，并将自我维护和邻近细胞的福祉置于优先地位。
*   细胞通过微管网络（TNTs）、间隙连接和外泌体进行通讯，分享资源以帮助受压或受伤的细胞。
*   研究表明，组织保留了其胚胎起源的记忆，铭刻在DNA上，这种记忆可以在特定条件下恢复，可能为治疗疾病和理解癌症提供新的途径。
*   细胞被视为自创生系统，不断地自我重建和维护，甚至垂死的细胞也会保护邻近的细胞免于死亡。
*   环境DNA（eDNA），即生物体脱落的遗传物质，可以被提取以检索详细的医疗和祖先数据。
*   文章最后提出质疑，一些超自然体验和“集体无意识”的概念是否可能与人们“读取”eDNA的能力有关，其中包含来自过去的强烈情感体验的痕迹。

---

## 37. 我对微软忍无可忍了

**原文标题**: I've Had It with Microsoft

**原文链接**: [https://www.disconnect.blog/p/ive-had-it-with-microsoft](https://www.disconnect.blog/p/ive-had-it-with-microsoft)

帕里斯·马克表达了对微软在Microsoft 365订阅价格上涨方面欺骗行为的不满。马克指责微软以“成本上涨”和“新创新”为幌子提高价格，掩盖了真正的原因：为他们的生成式人工智能野心提供资金。

文章强调，微软自动将现有用户转移到一个包含他们未请求的人工智能功能、价格更高的新计划中。作者只有在试图取消订阅时才发现有更便宜的、不含人工智能的选项，这表明微软有意隐藏了这个选择。

马克批评这是对市场力量的公然滥用和一种欺骗性策略，目的是从客户那里榨取更多资金。他们认为，这种做法加剧了人们对科技垄断企业日益增长的不信任，以及对生成式人工智能是“一场巨大骗局”的看法。

作者感叹当前联邦贸易委员会领导下缺乏监管监督，暗示莉娜·汗本应调查此类滥用行为。马克最后表达了摆脱微软产品和服务的决心，并呼吁对那些对客户撒谎的公司追究责任，同时也指出微软已被列入抵制、撤资、制裁名单。

---

## 38. 好的文档描述，坏的文档规定。

**原文标题**: Good Docs Describe, Bad Docs Prescribe

**原文链接**: [https://rethinkingsoftware.substack.com/p/good-docs-describe-bad-docs-prescribe](https://rethinkingsoftware.substack.com/p/good-docs-describe-bad-docs-prescribe)

无法访问文章链接。

---

## 39. 使用 Kiro 进行开发：亚马逊的新型 Agentic IDE

**原文标题**: Developing with Kiro: Amazon's New Agentic IDE

**原文链接**: [https://yehudacohen.substack.com/p/developing-with-kiro-amazons-new](https://yehudacohen.substack.com/p/developing-with-kiro-amazons-new)

无法访问文章链接。

---

## 40. 谷歌Opal

**原文标题**: Google Opal

**原文链接**: [https://developers.googleblog.com/en/introducing-opal/](https://developers.googleblog.com/en/introducing-opal/)

Google Labs推出Opal：通过自然语言和可视化编辑构建并分享AI迷你应用的新实验工具。Opal简化了AI应用的创建过程，无需代码即可将提示词、AI模型和其他工具串联成可视化工作流。

Opal的主要功能包括：

*   **工作流创建：** 用户可以描述所需应用的逻辑，Opal将自动生成表示步骤序列的可视化工作流。
*   **轻松编辑：** 可视化编辑器可以对应用的功能进行精细控制。用户可以使用自然语言命令或直接在编辑器中进行操作，以调整提示词、添加新功能或调用工具。
*   **应用分享：** 应用完成后，可以与他人分享，并通过他们的Google帐户立即使用。

Opal目前仅在美国提供公开测试版，并包含一个演示库，其中包含入门模板以帮助用户开始使用。Google旨在通过将提示词转化为迷你应用，来赋能创作者和创新者构建AI工具。

---

## 41. 正电子 - 下一代数据科学 IDE

**原文标题**: Positron – A next-generation data science IDE

**原文链接**: [https://positron.posit.co/](https://positron.posit.co/)

Positron：一款由Posit PBC开发的免费、下一代数据科学IDE。它被设计为一款可扩展、支持多种编程语言的编码和数据探索工具，为可重复的创作和发布提供熟悉的环境。Positron构建于Code OSS之上，利用现有的VS Code功能进行命令、设置和源代码控制。

用户可以找到安装程序、用户指南（涵盖解释器选择和数据浏览器等主题）以及常见问题解答以开始使用。Posit鼓励用户在GitHub Discussions上提供反馈和提问，以不断改进。

Positron采用Elastic License 2.0（一种源码可用许可）进行授权，“Positron”和Positron图标均为Posit Software, PBC的商标。

---

## 42. Qwen3-235B-A22B-思考-2507

**原文标题**: Qwen3-235B-A22B-Thinking-2507

**原文链接**: [https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507)

基于所提供的信息，“Qwen3-235B-A22B-Thinking-2507” 似乎是某个资源（很可能是一个资源库）的标题。内容描述非常简短：

*   **标题：** Qwen3-235B-A22B-Thinking-2507 （暗示大型语言模型或类似的AI相关项目）
*   **项目数量：** 76 （可能是资源内的文件、代码片段或其他组件）
*   **更新状态：** 大约7小时前更新
*   **下载/浏览次数：** 916

**概要：**

此条目指的是 “Qwen3-235B-A22B-Thinking-2507”，这似乎是一个项目或集合（可能与基于 “Qwen” 前缀和 “Thinking” 后缀的大型语言模型相关）。它包含76个项目，并且最近在7小时前更新。该资源已获得916次下载或浏览，表明对其有一定的兴趣和活跃度。在没有更多上下文的情况下，很难确定该项目的确切性质，但名称和统计数据表明，这是人工智能或语言建模领域中一个相对重要且积极维护的资源。

---

## 43. 石墨烯操作系统：一个安全增强的安卓版本

**原文标题**: Graphene OS: a security-enhanced Android build

**原文链接**: [https://lwn.net/SubscriberLink/1030004/898017c7953c0946/](https://lwn.net/SubscriberLink/1030004/898017c7953c0946/)

这篇LWN.net文章评测了GrapheneOS，一个注重安全的Android重构版本，旨在增强用户隐私和安全。GrapheneOS构建于Android开放源代码项目之上，移除了不必要的代码并添加了安全增强功能，例如强化的`malloc()`库和控制流完整性特性。

安装仅限于最新的Google Pixel设备（6-9，对4-5有一些支持）。全新安装需要从头开始重新配置一切。GrapheneOS附带最少的预装应用程序，包括基于Chromium的浏览器（Vanadium）、一个默认剥离Exif信息的相机应用程序和一个最小化的应用商店。

文章讨论了应用商店选项。Accrescent提供了一小部分注重安全/隐私的应用程序。虽然F-Droid是一个选项，但它并没有受到GrapheneOS社区的高度评价。作者成功地使用了沙盒版本的Google Play商店，允许访问更广泛的应用程序，而无需授予它在原生Android中拥有的特权访问权限。GrapheneOS实现了Android的完整性API，但是，作为一个非官方版本，它未能通过其中一项测试，这可能导致某些应用程序拒绝运行。

GrapheneOS包含诸如阻止运营商强制执行的 tethering 限制、控制每个应用程序的网络访问、传感器权限以及存储/联系人范围等功能。它还提供带有暴力破解保护的指纹解锁和用于数据擦除的胁迫PIN码。系统会积极更新，并且默认配置会定期重启以确保安全。

文章指出了一些关于GrapheneOS开发社区的透明度以及对Daniel Micay的依赖性的担忧。尽管如此，作者已切换到GrapheneOS，并且对其安全性和隐私优势感到满意，最终认为所需的设置工作是值得的。

---

## 44. 反对支付处理商审查成人内容

**原文标题**: Against the censorship of adult content by payment processors

**原文链接**: [https://soatok.blog/2025/07/24/against-the-censorship-of-adult-content-by-payment-processors/](https://soatok.blog/2025/07/24/against-the-censorship-of-adult-content-by-payment-processors/)

一位毛茸茸的（furry）安全工程师Soatok反对将Visa和Mastercard等支付处理商武器化，以审查在线内容，特别是成人内容。他们强调，像Collective Shout和Exodus Cry这样的团体已成功向支付处理商施压，迫使Steam和itch.io等平台删除内容，这引发了人们对这些公司拥有不受约束的权力来决定在线可以购买和销售哪些商品的担忧。

作者批评了Collective Shout的方法，即使承认某些目标内容（如美化强奸的游戏）存在问题。他们担心这种策略会被其他团体采用，可能针对 LGBTQIA+ 内容，甚至针对作者自己的博客，因为其中包含毛茸茸的艺术。

Soatok强调，问题主要在于政治，而非技术，加密货币等解决方案并不足以解决问题。相反，他们提倡集体行动和政治解决方案，引用了Change.org上的请愿书，并提及了拟议的立法，同时告诫人们不要采取像“玩家门（GamerGate）”这样具有分裂性的行为。

作者还提出了欧盟的WERO和美国的FedNOW等替代支付系统的潜力，这些系统会将权力分配给更多的银行和支付提供商，从而减少Visa和Mastercard的控制。他们鼓励读者支持这些举措，并暗示未来将讨论GNU Taler。总之，本文旨在通过组织和政治行动来保护在线自由表达免受支付处理商的审查。

---

## 45. Meta因繁重的法规而效仿谷歌，怒退欧盟政治广告。

**原文标题**: Meta joins Google in ragequitting EU political ads over onerous regulations

**原文链接**: [https://www.theregister.com/2025/07/25/meta_eu_political_ads/](https://www.theregister.com/2025/07/25/meta_eu_political_ads/)

Meta效仿谷歌，因即将实施的政治广告透明化和定向规管(TTPA) ，将不再允许在欧盟投放政治广告。Meta声称，定于10月生效的TTPA施加了过度的义务和法律不确定性，使得合规对广告商来说过于困难和具有限制性。

TTPA要求广告商披露详细信息，如谁在做广告、所广告的公投内容、支付的金额以及使用的定向技术，并且需要用户明确同意定向广告。Meta认为这使其处于困难境地，迫使其提供无效的广告产品或完全停止政治广告。他们选择了后者，指责欧盟实际上将一项服务从市场上移除。

Meta强调，其平台上仍允许发布自然政治内容。谷歌在11月做出了类似的决定，理由是TTPA下的运营挑战和法律不确定性。与Meta一样，谷歌也批评欧盟在该法规中缺乏明确性。欧盟委员会未予置评。

---

## 46. Modernish – 用于为基于POSIX的Shell和实用程序编写程序的库

**原文标题**: Modernish – A library for writing programs for POSIX-based shells and utilities

**原文链接**: [https://github.com/modernish/modernish](https://github.com/modernish/modernish)

Modernish 是一个 Shell 脚本库，旨在增强和简化基于 POSIX 系统的 Shell 编程，提高可移植性和安全性。它通过提供更安全的变量扩展、新的循环结构和其他功能，解决常见的脚本问题，如引用复杂性和潜在错误。

该库完全用 Shell 编写，无需编译代码，并确保在各种类 Unix 系统上的兼容性。它支持两种主要的使用模式：一种简单模式，其中 modernish 在特定于 Shell 的脚本中被引入；另一种可移植模式，它使用特殊的 Hashbang 来使用用户的默认 Shell 执行具有 modernish 增强功能的脚本。

主要功能包括：用于安全模式的模块（防止常见的脚本错误）、增强的变量和循环结构（var/loop、var/local 等）、字符串操作工具（var/string）以及基本实用程序的现代化版本（sys/base），以确保跨系统的一致行为。它还提供用于强化外部命令、解析命令行选项以及管理 Shell 选项和 Trap 堆栈的工具。

Modernish 包括广泛的 Shell 功能检测，允许脚本适应不同的 Shell 实现。安装和卸载由可以交互或非交互运行的脚本处理。该库正在积极寻找测试人员和开发人员来为其开发做出贡献并识别潜在问题。

---

## 47. 谷歌的 goo.gl 短链接下个月将停止服务。

**原文标题**: Google's shortened goo.gl links will stop working next month

**原文链接**: [https://www.theverge.com/news/713125/google-url-shortener-links-shutdown-deadline](https://www.theverge.com/news/713125/google-url-shortener-links-shutdown-deadline)

谷歌 goo.gl 短网址将于2025年8月25日停止服务，并返回404错误。谷歌于2019年停止了该工具，理由是互联网内容发现方法不断发展，但保留了现有链接的功能至今。完全弃用这些链接的决定源于其使用量的大幅下降，谷歌报告称，在宣布之前的那个月，超过99%的短网址没有任何活动。点击这些链接的用户已经遇到关于即将关闭的警告。文章建议仍然依赖 goo.gl 链接的个人和组织在截止日期之前过渡到替代的URL缩短服务，以避免链接失效。该新闻强调了更新在线内容以确保持续可访问性的重要性。

---

## 48. Thunder Compute (YC S24) 正在招聘 C++ 系统工程师

**原文标题**: Thunder Compute (YC S24) Is Hiring a C++ Systems Engineer

**原文链接**: [https://www.ycombinator.com/companies/thunder-compute/jobs/DhML6Uf-c-systems-engineer](https://www.ycombinator.com/companies/thunder-compute/jobs/DhML6Uf-c-systems-engineer)

Thunder Compute (YC S24) 招聘 C++ 系统工程师，负责其 GPU 云平台的核心开发。该平台采用定制虚拟化技术，利润率比竞争对手高 5 倍。该公司是一家 4 人、种子轮融资的初创企业，收入每月增长 100% 以上，目前位于亚特兰大，但将在 6 个月内迁至旧金山或纽约。

核心技术挑战包括通过 TCP 将 GPU 连接到网络，以实现积极的硬件超额订阅。理想的候选人应具备顶尖的 C++ 能力，优化 NIC/GPU 性能的经验，对底层网络/编译器有深刻理解，以及在延迟敏感型环境中工作的经验。必备素质包括担任高级领导职务的巨大潜力，强大的沟通能力和积极主动的态度。首选资格包括美国顶尖大学的 CS 博士/硕士学位，以及在贸易公司或 NVIDIA 等硬件公司的工作经验。

该职位涉及性能优化、系统调试以及超额订阅和检查点研究。职位为全职，薪资（10 万美元 - 15 万美元）加上 0.5-1% 的股权，并向联合创始人/CTO 汇报。Thunder Compute 致力于成为世界上最便宜的 GPU 云平台，利用其专有的虚拟化堆栈来提高 GPU 利用率。他们正在积极寻找一位有才华的工程师来为这一使命做出贡献。

---

## 49. 瑞文戴尔自行车打造了世纪后拨。

**原文标题**: Rivendell Bikes Has Crafted the Rear Derailleur of the Century

**原文链接**: [https://www.outsideonline.com/outdoor-gear/bikes-and-biking/rivendell-bikes-rear-derailleur?scope=anon](https://www.outsideonline.com/outdoor-gear/bikes-and-biking/rivendell-bikes-rear-derailleur?scope=anon)

埃本·魏斯的文章赞扬了Rivendell Bicycle Works即将推出的Silver OM-1后拨，这是一款“低位普通”（LN）设计，为现代电子变速和定位变速系统提供了一个引人注目的替代方案。文章强调了Rivendell致力于创造“为普通人设计的普通自行车”，优先考虑简单、舒适和兼容性。

OM-1的主要优势在于其低位普通动作，即弹簧将链条拉到低速档（最大的飞轮片）。这与更常见的“高位普通”后拨形成对比，后者弹簧倾向于高速档。Rivendell认为，LN后拨提供更平滑的降档，与摩擦变速器搭配时提供更直观的变速体验，并且在电缆故障时默认降至较低档位——这是爬坡时的优势。

文章解释说，Rivendell并非低位普通后拨的发明者，并引用了Shimano的RapidRise作为过去的例子，但它承认其与摩擦变速器的完美兼容性。对于一家小公司来说，制造后拨是一项重要的事业，但Rivendell追求它，是为了创造一款符合其价值观的产品，并为寻求简单性和兼容性的骑手提供完整的摩擦传动系统。OM-1有望成为一个美观、功能强大的组件，与从复古到现代的各种自行车兼容，为那些欣赏摩擦变速的手感和灵活性的用户提供一个受欢迎的选择。

---

## 50. XMPP：一个25年历史的协议再次成为战略重点

**原文标题**: XMPP: When a 25-Year-Old Protocol Becomes Strategic Again

**原文链接**: [https://www.process-one.net/blog/xmpp-when-a-25-year-old-protocol-becomes-strategic-again/](https://www.process-one.net/blog/xmpp-when-a-25-year-old-protocol-becomes-strategic-again/)

XMPP：在数字时代依然重要的战略协议

---

## 51. 科学家或已找到消除与唐氏综合征相关染色体的方法

**原文标题**: Scientists may have found a way to eliminate chromosome linked to Down syndrome

**原文链接**: [https://academic.oup.com/pnasnexus/article/4/2/pgaf022/8016019](https://academic.oup.com/pnasnexus/article/4/2/pgaf022/8016019)

加州大学圣地亚哥分校的科学家可能开发出一种新型基因治疗方法，有望消除导致唐氏综合征的额外 21 号染色体。该研究发表在《PNAS Nexus》上，重点是利用基于 CRISPR 的技术在体外靶向并破坏 21 号染色体。

该团队设计了一种“基于 CRISPR-dCas9 的合成沉默系统”，专门用于靶向 21 号染色体上的重复序列。该系统不像传统的 CRISPR 那样切割 DNA；相反，它附着在染色体上，并招募蛋白质来有效地沉默或浓缩它，使染色体失活，并可能导致其在细胞分裂过程中被消除。

在他们使用源自唐氏综合征患者的诱导多能干细胞 (iPSCs) 的实验中，研究人员成功地证明了在部分细胞中 21 号染色体的沉默和随后的丢失。他们观察到携带额外染色体的细胞数量减少，表明该方法的可行性。

虽然这项研究是初步的，并且仅在体外（细胞培养物中）进行，但它为唐氏综合征提供了一种潜在的治疗途径。该技术有可能用于在发育早期纠正染色体异常，但在体内（在活生物体中）或在人类中应用之前，仍然存在重大挑战。这些挑战包括确保系统的特异性和效率、防止脱靶效应以及开发安全有效的递送方法。尽管如此，这项研究代表了在探索唐氏综合征基因治疗方面的重要一步。

---

## 52. 智能手机赌博是一场灾难

**原文标题**: Smartphone Gambling Is a Disaster

**原文链接**: [https://www.afterbabel.com/p/smartphone-gambling-is-a-disaster](https://www.afterbabel.com/p/smartphone-gambling-is-a-disaster)

科恩和罗斯-伯曼认为，智能手机赌博是一种独特的危险现象，尤其是对年轻男性而言，因为它具有易于访问性、无摩擦性以及促进成瘾的设计。与传统赌博不同，在线平台提供全天候访问、个性化投注选项以及模仿社交媒体的操纵性策略，以保持用户参与。

作者强调了在线体育博彩和网络博彩的爆炸式增长，这归功于积极的广告宣传和名人代言，使赌博正常化并提高了问题赌博率。他们引用统计数据表明，与赌博相关的危害（如破产、精神健康问题和成瘾）有所增加，尤其是在年轻男性中。

他们主张转变赌博监管方式，优先考虑玩家福祉而不是收入。具体而言，他们建议禁止在线赌场游戏，并实施更严格的法规，包括广告限制和对不合规运营商的严厉执法。作者还呼吁家长和老师们意识到赌博在年轻人中的普遍性。

---

## 53. 行星际网络特别兴趣小组

**原文标题**: Inter-Planetary Network Special Interest Group

**原文链接**: [https://www.ipnsig.org](https://www.ipnsig.org)

行星际网络特别兴趣小组（IPNSIG）旨在将互联网扩展到太空，实现互联网协会连接无人居住区域的目标，并确保“人人享有互联网”，即使在太空也是如此。IPNSIG由Vint Cerf和来自学术界及NASA/JPL的研究人员于1998年创立，现已成为互联网协会的正式分会。

他们的主要目标是使用延迟容忍网络（DTN）技术构建和管理太阳系互联网。他们正通过以下几项关键举措来实现这一目标：

*   **创建共同愿景：** 与利益相关者合作，为行星际网络建立共同愿景。
*   **叙述和路线图：** 通过为网络发展提供清晰的叙述和路线图，定义网络的未来。
*   **推广DTN技术：** 通过在陆地和太空环境中的应用，提高DTN技术的成熟度和采用率。

IPNSIG的总体愿景是将网络扩展到行星际空间，以造福人类。可用的关键资源包括他们的架构和治理报告以及他们的战略工作组报告，这两份报告都详细介绍了他们构建太阳系互联网的方法。

---

## 54. Meta将在欧盟停止投放Facebook和Instagram上的政治广告

**原文标题**: Meta to stop running political ads on Facebook and Instagram in the EU

**原文链接**: [https://www.euractiv.com/section/tech/news/meta-to-stop-running-political-ads-on-facebook-and-instagram/](https://www.euractiv.com/section/tech/news/meta-to-stop-running-political-ads-on-facebook-and-instagram/)

Meta将于10月起暂停欧盟地区Facebook和Instagram上的政治、选举和社会议题广告，理由是欧盟即将出台的政治广告透明度监管规定。 该规定旨在打击虚假信息和外国干预，要求在线平台披露政治广告赞助商以及是否使用了个人数据进行定向投放。

Meta声称该规定带来了“难以维持的复杂性和法律不确定性”。该公司强调，这一变化不会影响政客发布内容的能力，只会影响他们付费推广内容的能力。

欧盟监管报告员桑德罗·戈齐批评了Meta的决定，指责该公司将利润置于透明度和民主责任之上。

去年谷歌也做出了类似决定，理由是该法律对“政治广告”的广泛定义阻碍了合规。 两家公司的行为引发了对其广告审查系统有效性的质疑，即该系统在识别和阻止可能漏网的政治广告方面是否有效，这些广告可能会违反欧盟的透明度规则。 这并非Meta首次将改变广告行为归咎于欧盟法律，因为它还因其“付费或同意”的广告模式而面临《数字市场法案》的审查。

---

## 55. Anthropic 团队如何使用 Claude Code

**原文标题**: How Anthropic teams use Claude Code

**原文链接**: [https://www.anthropic.com/news/how-anthropic-teams-use-claude-code](https://www.anthropic.com/news/how-anthropic-teams-use-claude-code)

Anthropic各团队如何利用AI工具Claude Code提升工作效率

**主要应用场景：**

*   **数据基础设施：** 自动化数据工程任务，解决基础设施问题（如Kubernetes调试），为非技术用户（财务）创建纯文本工作流，为新员工提供代码库导航，以及记录工作会话。
*   **产品开发：** 利用自动接受模式进行快速原型设计，核心功能同步编码，测试生成，错误修复，以及代码库探索。
*   **安全工程：** 调试复杂的IT基础设施事件，Terraform代码审查和分析，文档生成（运维手册），测试驱动开发，以及项目入职培训。
*   **推理：** 代码库理解和入职培训，生成具有边缘情况覆盖的单元测试，机器学习概念解释，跨语言代码翻译，以及Kubernetes管理。

**主要优势：**

*   **提高效率：** 减少调试、编码和文档编写的时间。
*   **提升代码质量：** 自动化测试生成和错误修复。
*   **弥合技能差距：** 使非技术人员能够执行技术任务。
*   **加快入职速度：** 减少新员工理解复杂系统的时间。
*   **加强协作：** 改善沟通和共同理解。

**主要技巧：**

*   在Claude.md文件中广泛记录工作流和工具。
*   利用自动接受模式执行异步任务。
*   创建自给自足的循环，让Claude验证自己的工作。
*   编写清晰、详细的提示语。
*   使用自定义斜杠命令来简化任务。
*   利用Claude进行文档生成。
*   从代码生成开始，并验证其正确性。

---

## 56. 英特尔Clear Linux最终基准测试：比Ubuntu开箱即用快约48%

**原文标题**: Final Benchmarks of Clear Linux on Intel: ~48% Faster Than Ubuntu Out-of-the-Box

**原文链接**: [https://www.phoronix.com/review/clear-linux-48p-ubuntu](https://www.phoronix.com/review/clear-linux-48p-ubuntu)

迈克尔·拉拉贝尔 2025 年 7 月的文章对英特尔已停止维护的 Clear Linux 发行版与 Ubuntu 25.04 在 Intel Xeon Max (Sapphire Rapids) 服务器上的最终性能进行了基准测试。Clear Linux 以其激进的 x86_64 优化而闻名，但由于财务困难而被英特尔停止维护。

测试在一台 Supermicro Hyper SuperServer SYS-221H-TNR / X13DEM 上进行，该服务器配备了双 Xeon Max 9468 处理器、512GB 内存和一个 7.6TB NVMe SSD。Clear Linux 43760 采用了 Linux 6.15.5 内核、GCC 15.1.1 和 Python 3.13。Ubuntu 25.04 在其默认配置（带有“schedutil”调控器的 intel_cpufreq 缩放驱动程序）以及 CPU 频率缩放调控器切换到“performance”以匹配 Clear Linux 的情况下进行了测试。

该基准测试旨在展示 Clear Linux 的优化所实现的性能提升，即使是在超出英特尔最新一代（Granite Rapids，由于硬件不可用而无法测试）的系统上也是如此。在测试期间还监测了双 Xeon Max 9468 处理器的功耗，以评估 Clear Linux 的优化对 CPU 功耗的影响。该文章承诺比较各种工作负载的性能，包括 Java 服务器应用程序、视频编码、HPC 基准测试、数据库和深度学习任务。此外，还计划对 AMD 系统进行类似的分析，以展示英特尔的 Linux 软件优化在其竞争对手硬件上的优势。结论（在第 6 页）重点介绍了整体性能指标。

---

## 57. 使用你的类型系统

**原文标题**: Use Your Type System

**原文链接**: [https://www.dzombak.com/blog/2025/07/use-your-type-system/](https://www.dzombak.com/blog/2025/07/use-your-type-system/)

本文倡导利用类型系统来防止因在代码库中使用诸如整数、字符串和 UUID 等通用类型来表示不同的概念而产生的错误。作者观察到，传递原始 `int` 或 `string` 值通常会导致混淆和错误，例如在需要账户 ID 的地方使用了用户 ID。

解决方案是为每个领域特定的概念定义自定义类型，即使它们基于诸如 `uuid.UUID`、`float64` 或 `int` 之类的底层基元。 这样，当一个类型的值被意外地传递到需要另一个类型的地方时，编译器就可以捕获错误。本文通过基于 `uuid.UUID` 的 `AccountID` 和 `UserID` 类型的示例说明了这一点，展示了编译器如何防止将它们混淆。

作者还分享了来自其 `libwx` 天气库的一个实际示例，其中为各种测量值（如温度和湿度）定义了类型。 这可以防止诸如将华氏温度传递给期望摄氏温度的函数，或意外交换参数顺序等错误，因为编译器可以强制执行类型正确性。

核心信息是充分利用类型系统，为简单数据类型添加语义意义，从而提高代码的安全性和可靠性，即使在像 Go 这样类型系统相对简单的语言中也是如此。

---

## 58. VTuber事务所VShojo在人才流失后倒闭

**原文标题**: VTuber agency VShojo shuts down after talent exodus

**原文链接**: [https://www.theverge.com/news/713343/vshojo-shutting-down-ironmouse-missing-charity-donations](https://www.theverge.com/news/713343/vshojo-shutting-down-ironmouse-missing-charity-donations)

VTuber事务所VShojo因大量成员出走而倒闭，起因是头部艺人Ironmouse因未支付款项和50万美元慈善捐款失踪而离开。首席执行官Justin "Gunrun" Ignacio宣布关闭，并对管理不善和财务困难承担全部责任。他承认，尽管筹集了1100万美元，但该公司未能产生足够的收入来维持其“人才至上”的模式。Ignacio还承认，Ironmouse为慈善事业筹集的资金被公司花费，原因是他们相信能够筹集足够的投资来支付所有费用。由于13位创作者中有12位因工资未付而离开，该事务所无法恢复，现已关闭，首席执行官对此向艺人、员工和社区深感抱歉。

---

## 59. PSA：SQLite WAL 校验和静默失败可能导致数据丢失

**原文标题**: PSA: SQLite WAL checksums fail silently and may lose data

**原文链接**: [https://avi.im/blag/2025/sqlite-wal-checksum/](https://avi.im/blag/2025/sqlite-wal-checksum/)

本文重点介绍了SQLite的WAL（预写式日志）模式中潜在的数据丢失问题。尽管WAL使用校验和来确保数据完整性，但SQLite在检测到校验和错误时的行为存在问题。它不会引发错误，而是会默默地丢弃损坏的帧以及WAL中的所有后续帧，即使后面的帧有效并包含关键数据。这种情况发生在WAL索引重建过程中（.db-shm文件），通常是在非正常关机后或当.db-shm文件丢失时触发。

作者强调，这不是一个错误，而是有意为之的设计。当在WAL恢复过程中发生校验和不匹配时，SQLite会在损坏点停止处理WAL。由于SQLite会自动执行检查点并截断WAL，因此损失是永久性的。

本文批评了这种行为，因为它可能导致不必要的数据丢失。来自旧版本的页面或属于不重要索引的损坏帧可能会触发删除较新的有效数据。作者建议SQLite应该在检测到损坏时抛出错误，允许开发人员处理这种情况，而不是默默地丢失数据。替代行为可能包括忽略损坏并继续的选项，或更复杂的恢复机制。

作者承认了当前设计背后的可能原因——SQLite通常运行在嵌入式系统中，在这种情况下，崩溃不如带着可能损坏的数据勉强运行那么令人不快。然而，他们认为默默地丢失数据是不可接受的。

---

## 60. 帮助计算该用哪个GPU的GPU计算器

**原文标题**: A GPU Calculator That Helps Calculate What GPU to Use

**原文链接**: [https://calculator.inference.ai/](https://calculator.inference.ai/)

本文介绍一种“GPU计算器”，它很可能是一种工具或资源，旨在帮助用户确定哪种GPU（图形处理器）最适合他们的需求。该计算器的核心功能是根据用户输入提供建议。虽然本文本身很简短，但其含义是该计算器考虑了以下因素：

*   **预期用途：** GPU将用于的任务类型（游戏、视频编辑、3D渲染、AI/机器学习等）。
*   **预算：** 用户愿意花费的价格范围。
*   **性能

最终，GPU计算器旨在通过基于个人需求和约束提供数据驱动的建议，从而简化通常复杂的GPU选择过程。 它可以帮助用户避免过度消费在不必要的性能上，或者消费不足而无法获得足够的性能。

---

## 61. 一个帮你计算用哪个GPU的计算器

**原文标题**: A GPU Calculator That Helps Calculate What GPU to Use

**原文链接**: [https://calculator.inference.ai/](https://calculator.inference.ai/)

本文介绍了一种“GPU计算器”，该工具旨在帮助用户确定最适合他们需求的GPU。 其前提很简单：用户输入具体的需求或性能目标（可能与游戏、视频编辑、AI开发或其他GPU密集型任务相关），计算器会输出合适的GPU推荐。

这种计算器的可能好处是简化通常复杂的GPU选择过程。 性能特征、价格、功耗和兼容性都会影响购买决策。 一个设计良好的GPU计算器理想情况下会考虑这些因素。

本文的重点表明它对新手和有经验的用户都具有实际用途。 新用户可能会从指导中受益，从而在复杂的GPU市场中进行导航，而有经验的用户可能会使用该工具根据特定参数快速比较选项。

最终，本文重点介绍了一种资源，旨在通过提供基于用户定义标准的数据驱动建议来简化和消除GPU选择过程的神秘性。

---

## 62. 全新的Aarch64后端

**原文标题**: New Aarch64 Back End

**原文链接**: [https://ziglang.org/devlog/2025/#2025-07-23](https://ziglang.org/devlog/2025/#2025-07-23)

本文总结了 Zig 编程语言在 2025 年的主要进展，重点关注编译器后端和性能改进。

**Aarch64 后端：** 由 Andrew Kelley 和 Jacob Young 开发的全新 Aarch64 后端已推出。 虽然仍在开发中，但它在行为测试中表现良好，并且在某些基准测试中比 x86 后端更快。 该后端使用机器代码指令编码作为其内部 MIR 结构，并具有定制的两遍活性分析。

**并行代码生成：** x86_64 后端通过并行代码生成实现了显着的性能提升。 这允许多个代码生成作业同时运行，从而大大缩短了编译 Zig 项目的实际时间。

**自托管 x86 后端默认为：** 自托管 x86 后端现在是 Linux 和 macOS 上 Debug 构建的默认后端，与 LLVM 后端相比，提供了显着的速度提升。

**FreeBSD 和 NetBSD 交叉编译：** Zig 现在支持 FreeBSD 14.0.0+ 和 NetBSD 10.1+ 的交叉编译，采用的策略是从预构建的 libc 库中提取公共符号信息以创建存根库。

本文还提到一个关于 Zig 构建系统的入门视频以及正在进行的增量编译工作。 总的来说，在内部开发工作和社区贡献的推动下，Zig 在编译速度和后端功能方面取得了重大进展。

---

## 63. 干预系统的切入点

**原文标题**: Places to Intervene in a System

**原文链接**: [https://donellameadows.org/archives/leverage-points-places-to-intervene-in-a-system/](https://donellameadows.org/archives/leverage-points-places-to-intervene-in-a-system/)

这个由唐娜拉·梅多斯项目主办的网页，致力于保存和推广著名系统思想家、作家和教师唐娜拉·H·（达娜）·梅多斯的遗产。该项目旨在管理与其出版作品相关的知识产权，并提供一个易于访问的在线资料库。

该网站将达娜·梅多斯的作品分为几个主要部分：出版物（包括书籍、文章、“全球公民”专栏和“亲爱的朋友们”信件），系统思考资源（以其有影响力的作品，如《系统之美》、《杠杆点》和《与系统共舞》为特色，以及一份全面的资源列表）和多媒体（视频和照片）。它还包括一个语录集、致敬和用户可以提交他们最喜欢的达娜·梅多斯语录的部分。

本质上，唐娜拉·梅多斯项目是任何对学习或参与达娜·梅多斯关于系统思考及其在社会变革中的应用感兴趣的人的中心枢纽。该项目的使命是使她的思想能够被广泛的学生、从业者和领导者所访问，确保她的贡献继续激励和启发后代。

---

## 64. 每月铁塔

**原文标题**: Pylon of the Month

**原文链接**: [https://www.pylonofthemonth.org/](https://www.pylonofthemonth.org/)

无法访问文章链接。

---

## 65. Mwm – 最小可用的 X11 窗口管理器

**原文标题**: Mwm – The smallest usable X11 window manager

**原文链接**: [https://github.com/lslvr/mwm](https://github.com/lslvr/mwm)

Mwm是一个极简主义的X11窗口管理器，仅用20行代码设计，追求极致的简洁性和可 Hack 性。它刻意缺少其他窗口管理器常见的特性，例如鼠标控制、虚拟桌面、配置文件、标题栏、边框、菜单，并且只允许全屏窗口，一次只能显示一个。

其核心功能仅限于启动、切换和关闭窗口。用户可以使用`grab`和`map`宏自定义快捷键，如`mwm-custom.c`所示。作者强调在充斥着复杂臃肿应用程序的环境中，小型、可修改软件的重要性。构建过程被描述为“极其简单”，使用提供的`build.sh`脚本即可。该项目提倡易于理解和修改的软件，并声称真正的自由软件应该便于用户自定义。重点在于提供基本功能，并通过可 Hack 性来培养用户自主性。

---

## 66. 空军部队暂停使用西格绍尔手枪，此前发生空军士兵枪击死亡事件。

**原文标题**: Air Force unit suspends use of Sig Sauer pistol after shooting death of airman

**原文链接**: [https://www.nhpr.org/nh-news/2025-07-23/sig-sauer-pistol-air-force-shooting-death](https://www.nhpr.org/nh-news/2025-07-23/sig-sauer-pistol-air-force-shooting-death)

Following the fatal shooting of an airman at F.E. Warren Airforce Base in Wyoming, the U.S. Air Force Global Strike Command has suspended the use of the Sig Sauer M18 pistol pending a "comprehensive review." The airman, 21-year-old Brayden Tyriq Lovan, served in the 90th Security Forces Squadron.

The suspension comes amidst ongoing concerns about the safety of the Sig Sauer P320, the civilian model upon which the M18 is based. Both pistols have faced allegations of unintentional discharges, leading to numerous civil lawsuits. Sig Sauer has defended the P320, calling safety concerns "lies and misinformation."

The Air Force confirmed the review is related to the airman's death, but did not indicate if the investigation would expand to other units. The Global Strike Command will use alternative weapons during the investigation, and all bases within the command will conduct inspections of the M18. Sig Sauer has offered assistance to the U.S. Military during its investigation. The Global Strike Command oversees the Air Force's bomber fleet and nuclear command forces.


---

## 67. Does [MacOS] even matter anymore?

**原文标题**: Does [MacOS] even matter anymore?

**原文链接**: [https://www.macworld.com/article/2827504/does-the-mac-even-matter-anymore.html](https://www.macworld.com/article/2827504/does-the-mac-even-matter-anymore.html)

macOS是否正在失去苹果生态系统中的地位？

---

## 68. Show HN: Tsbro – 浏览器 TypeScript，无需构建步骤

**原文标题**: Show HN: Tsbro – TypeScript for the browser, no build step

**原文链接**: [https://github.com/stagas/tsbro](https://github.com/stagas/tsbro)

生成摘要时出错

---

## 69. Asif Aziz: The billionaire and the tax evading gift shops

**原文标题**: Asif Aziz: The billionaire and the tax evading gift shops

**原文链接**: [https://www.londoncentric.media/p/asf-aziz-london-candy-shops-gift-shop-unpaid-tax](https://www.londoncentric.media/p/asf-aziz-london-candy-shops-gift-shop-unpaid-tax)

生成摘要时出错

---

## 70. AMD CEO sees chips from TSMC's US plant costing 5%-20% more

**原文标题**: AMD CEO sees chips from TSMC's US plant costing 5%-20% more

**原文链接**: [https://www.bloomberg.com/news/articles/2025-07-23/amd-ceo-su-sees-chips-from-us-tsmc-plant-costing-5-to-20-more](https://www.bloomberg.com/news/articles/2025-07-23/amd-ceo-su-sees-chips-from-us-tsmc-plant-costing-5-to-20-more)

生成摘要时出错

---

## 71. Show HN: Nia – MCP server that gives more docs and repos to coding agents

**原文标题**: Show HN: Nia – MCP server that gives more docs and repos to coding agents

**原文链接**: [https://www.trynia.ai/](https://www.trynia.ai/)

生成摘要时出错

---

## 72. Neural biomarkers identified for obsessive-compulsive disorder symptoms in brain

**原文标题**: Neural biomarkers identified for obsessive-compulsive disorder symptoms in brain

**原文链接**: [https://medicalxpress.com/news/2025-07-neural-biomarkers-obsessive-compulsive-disorder.html](https://medicalxpress.com/news/2025-07-neural-biomarkers-obsessive-compulsive-disorder.html)

生成摘要时出错

---

## 73. The POSIX specification of vi

**原文标题**: The POSIX specification of vi

**原文链接**: [https://pubs.opengroup.org/onlinepubs/9799919799/utilities/vi.html](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/vi.html)

生成摘要时出错

---

## 74. There is no memory safety without thread safety

**原文标题**: There is no memory safety without thread safety

**原文链接**: [https://www.ralfj.de/blog/2025/07/24/memory-safety.html](https://www.ralfj.de/blog/2025/07/24/memory-safety.html)

生成摘要时出错

---

## 75. I wasted weeks hand optimizing assembly because I benchmarked on random data

**原文标题**: I wasted weeks hand optimizing assembly because I benchmarked on random data

**原文链接**: [https://www.vidarholen.net/contents/blog/?p=1160](https://www.vidarholen.net/contents/blog/?p=1160)

生成摘要时出错

---

## 76. Open Source Hackathon 2025

**原文标题**: Open Source Hackathon 2025

**原文链接**: [https://osshackathon.com](https://osshackathon.com)

生成摘要时出错

---

## 77. Visa and Mastercard: The global payment duopoly (2024)

**原文标题**: Visa and Mastercard: The global payment duopoly (2024)

**原文链接**: [https://quartr.com/insights/edge/visa-and-mastercard-the-global-payment-duopoly](https://quartr.com/insights/edge/visa-and-mastercard-the-global-payment-duopoly)

生成摘要时出错

---

## 78. Visualize Your Puppet Data in Grafana with the Observability Data Connector

**原文标题**: Visualize Your Puppet Data in Grafana with the Observability Data Connector

**原文链接**: [https://www.puppet.com/blog/tutorial-puppet-grafana-observability](https://www.puppet.com/blog/tutorial-puppet-grafana-observability)

This tutorial explains how to visualize Puppet data in Grafana using the Observability Data Connector, a feature of Puppet Enterprise Advanced. It guides users through the entire process, starting with module installation and ending with creating insightful Grafana dashboards.

The steps include:

1.  **Installing the Observability Data Connector module:** Adding the module to the control repository and deploying it.
2.  **Creating a Profile Class:** Developing a code-based profile class to configure module settings like stale time and drop zone.
3.  **Classifying the Puppet Server:** Using the Puppet Enterprise console to assign the profile class to the Puppet Server.
4.  **Verifying Data Collection:** Confirming that data is being written to the designated drop zone in Prometheus format.
5.  **Setting up a Prometheus Service:** Installing and configuring Prometheus to expose the Puppet data as metrics.
6.  **Integrating with Grafana:** Connecting Grafana to the Prometheus endpoint to visualize Puppet activity. Creating dashboards to monitor run durations, resource changes, and identify anomalies.
7.  **Scale and Customize:** Scale your configuration for different environments and tools.

The tutorial provides specific instructions, code examples, and screenshots to help users successfully integrate Puppet data with Grafana, enabling data-driven decisions for infrastructure management. This allows teams to monitor, troubleshoot, and optimize their infrastructure more effectively.


---

## 79. RE#: High performance derivative-based regular expression matching (2024)

**原文标题**: RE#: High performance derivative-based regular expression matching (2024)

**原文链接**: [https://arxiv.org/abs/2407.20479](https://arxiv.org/abs/2407.20479)

生成摘要时出错

---

## 80. UK: Phone networks down: EE, BT, Three, Vodafone, O2 not working in mass outage

**原文标题**: UK: Phone networks down: EE, BT, Three, Vodafone, O2 not working in mass outage

**原文链接**: [https://www.the-independent.com/tech/ee-bt-three-vodafone-o2-down-phone-networks-outage-latest-b2795260.html](https://www.the-independent.com/tech/ee-bt-three-vodafone-o2-down-phone-networks-outage-latest-b2795260.html)

生成摘要出错

---

## 81. The future is not self-hosted

**原文标题**: The future is not self-hosted

**原文链接**: [https://www.drewlyton.com/story/the-future-is-not-self-hosted/](https://www.drewlyton.com/story/the-future-is-not-self-hosted/)

Drew argues that self-hosting, while seemingly empowering, is not the solution to corporate control over our digital lives. He begins by highlighting Amazon's restricting access to purchased Kindle books, illustrating how users merely "rent" digital assets. He extends this concern to other cloud services like Dropbox and Google Photos, where corporations control access and data usage.

He details his own experiment in self-hosting, building a home server running open-source alternatives to popular cloud apps. While successful, he acknowledges the significant technical challenges and time commitment, making it impractical for most.

The core argument is that self-hosting, while granting individual control, is inherently isolating and inefficient. It replicates the internet as "suburbia" with everyone maintaining duplicate infrastructure and lacking the benefits of interconnected communities.

Instead, Drew advocates for "community-hosted" solutions: publicly funded, accessible, and at-cost cloud services, similar to libraries. He envisions services providing storage, photo sharing, and media streaming, emphasizing end-to-end encryption and standardized protocols to prevent vendor lock-in. He suggests these could be run by nonprofits or cooperatives as well.

He concludes that true freedom from corporate control requires solidarity, mutual aid, and shared, community-owned infrastructure, moving beyond the myth of self-reliance and individual empowerment. He wants the self-hosting community to apply its knowledge to build a better, shared cloud.


---

## 82. Why concatenative programming matters (2012)

**原文标题**: Why concatenative programming matters (2012)

**原文链接**: [http://evincarofautumn.blogspot.com/2012/02/why-concatenative-programming-matters.html](http://evincarofautumn.blogspot.com/2012/02/why-concatenative-programming-matters.html)

生成摘要时出错

---

## 83. Hulk Hogan Has Died

**原文标题**: Hulk Hogan Has Died

**原文链接**: [https://www.tmz.com/2025/07/24/hulk-hogan-dead/](https://www.tmz.com/2025/07/24/hulk-hogan-dead/)

生成摘要时出错

---

## 84. Revisiting Moneyball

**原文标题**: Revisiting Moneyball

**原文链接**: [https://djpardis.medium.com/revisiting-moneyball-074fc2435b07](https://djpardis.medium.com/revisiting-moneyball-074fc2435b07)

生成摘要时出错

---

## 85. Intel CEO Letter to Employees

**原文标题**: Intel CEO Letter to Employees

**原文链接**: [https://morethanmoore.substack.com/p/intel-ceo-letter-to-employees](https://morethanmoore.substack.com/p/intel-ceo-letter-to-employees)

生成摘要时出错

---

## 86. Alto turns Apple Notes into a website

**原文标题**: Alto turns Apple Notes into a website

**原文链接**: [https://alto.so/](https://alto.so/)

生成摘要时出错

---

## 87. CARA – High precision robot dog using rope

**原文标题**: CARA – High precision robot dog using rope

**原文链接**: [https://www.aaedmusa.com/projects/cara](https://www.aaedmusa.com/projects/cara)

生成摘要时出错

---

## 88. AI overviews cause massive drop in search clicks

**原文标题**: AI overviews cause massive drop in search clicks

**原文链接**: [https://arstechnica.com/ai/2025/07/research-shows-google-ai-overviews-reduce-website-clicks-by-almost-half/](https://arstechnica.com/ai/2025/07/research-shows-google-ai-overviews-reduce-website-clicks-by-almost-half/)

生成摘要时出错

---

## 89. When swiping supplants scissors: The hidden cost of touchscreens

**原文标题**: When swiping supplants scissors: The hidden cost of touchscreens

**原文链接**: [https://caseorganic.medium.com/when-swiping-supplants-scissors-the-hidden-cost-of-touchscreens-and-how-designers-can-help-dba0fa65f5b7](https://caseorganic.medium.com/when-swiping-supplants-scissors-the-hidden-cost-of-touchscreens-and-how-designers-can-help-dba0fa65f5b7)

生成摘要时出错

---

## 90. Breakneck: China's Quest to Engineer the Future

**原文标题**: Breakneck: China's Quest to Engineer the Future

**原文链接**: [https://danwang.co/breakneck/](https://danwang.co/breakneck/)

生成摘要时出错

---

## 91. Tap into the "Hemingway effect" to finish what you start

**原文标题**: Tap into the "Hemingway effect" to finish what you start

**原文链接**: [https://bigthinkmedia.substack.com/p/tap-into-the-hemingway-effect-to](https://bigthinkmedia.substack.com/p/tap-into-the-hemingway-effect-to)

生成摘要时出错

---

## 92. Open Source Maintenance Fee

**原文标题**: Open Source Maintenance Fee

**原文链接**: [https://github.com/wixtoolset/issues/issues/8974](https://github.com/wixtoolset/issues/issues/8974)

生成摘要时出错

---

## 93. Finding Robert Bogucki, the man who disappeared on purpose

**原文标题**: Finding Robert Bogucki, the man who disappeared on purpose

**原文链接**: [https://www.abc.net.au/news/2025-07-06/robert-bogucki-nowhere-man-on-his-43-days-in-the-desert/105234668](https://www.abc.net.au/news/2025-07-06/robert-bogucki-nowhere-man-on-his-43-days-in-the-desert/105234668)

生成摘要时出错

---

## 94. UK Gov Petition: Repeal the Online Safety Act

**原文标题**: UK Gov Petition: Repeal the Online Safety Act

**原文链接**: [https://petition.parliament.uk/petitions/722903](https://petition.parliament.uk/petitions/722903)

生成摘要时出错

---

## 95. Apache HTTP Server: 'RewriteCond expr' always evaluates to true

**原文标题**: Apache HTTP Server: 'RewriteCond expr' always evaluates to true

**原文链接**: [https://github.com/apache/httpd/commit/8abb3d06b23975705ebcf4bf4476464fd0b9bd0b](https://github.com/apache/httpd/commit/8abb3d06b23975705ebcf4bf4476464fd0b9bd0b)

生成摘要时出错

---

## 96. Major quantum computing advance made obsolete by teenager (2018)

**原文标题**: Major quantum computing advance made obsolete by teenager (2018)

**原文链接**: [https://www.quantamagazine.org/teenager-finds-classical-alternative-to-quantum-recommendation-algorithm-20180731/](https://www.quantamagazine.org/teenager-finds-classical-alternative-to-quantum-recommendation-algorithm-20180731/)

生成摘要时出错

---

## 97. Covers as a way of learning music and code

**原文标题**: Covers as a way of learning music and code

**原文链接**: [https://ntietz.com/blog/covers-as-a-way-of-learning/](https://ntietz.com/blog/covers-as-a-way-of-learning/)

生成摘要时出错

---

## 98. A valid HTML zip bomb

**原文标题**: A valid HTML zip bomb

**原文链接**: [https://ache.one/notes/html_zip_bomb](https://ache.one/notes/html_zip_bomb)

生成摘要时出错

---

## 99. Working on a Programming Language in the Age of LLMs

**原文标题**: Working on a Programming Language in the Age of LLMs

**原文链接**: [https://ryelang.org/blog/posts/programming-language-in-age-of-llms/](https://ryelang.org/blog/posts/programming-language-in-age-of-llms/)

生成摘要时出错

---

## 100. Lumo: Privacy-first AI assistant

**原文标题**: Lumo: Privacy-first AI assistant

**原文链接**: [https://proton.me/blog/lumo-ai](https://proton.me/blog/lumo-ai)

生成摘要时出错

---

