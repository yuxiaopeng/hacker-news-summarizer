# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-07-25.md)

*最后自动更新时间: 2025-07-25 17:52:04*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 2 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 3 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 4 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 5 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 6 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 7 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 8 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 9 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 10 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 11 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 12 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 13 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 14 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 15 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 16 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 17 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 18 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 19 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 20 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 21 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 22 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 23 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 24 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 25 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 26 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 27 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 28 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 29 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 30 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 31 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 32 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 33 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 34 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 35 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 36 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 37 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 38 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 39 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 40 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 41 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 42 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 43 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 44 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 45 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 46 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 47 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 48 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 49 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 50 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 51 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 52 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 53 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 54 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 55 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 56 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 57 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 58 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 59 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 60 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 61 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 62 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 63 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 64 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 65 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 66 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 67 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 68 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 69 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 70 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 71 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 72 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 73 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 74 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 75 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 76 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 77 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 78 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 79 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 80 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 81 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 82 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 83 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 84 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 85 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 86 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 87 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 88 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 89 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 90 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 91 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 92 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 93 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 94 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 95 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 96 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 97 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 98 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 99 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 100 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 101 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 102 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 103 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 104 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 105 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 106 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 107 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 108 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 109 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 110 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 111 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 112 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 113 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 114 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 115 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 116 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 117 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 118 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 119 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 120 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 121 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 122 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 123 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 124 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 125 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 126 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 127 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 128 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
