# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-06-27.md)

*最后自动更新时间: 2025-06-27 17:47:46*
## 1. 显示HN：我是航空公司飞行员 – 我构建了我的航班的交互式图表/地球仪

**原文标题**: Show HN: I'm an airline pilot – I built interactive graphs/globes of my flights

**原文链接**: [https://jameshard.ing/pilot](https://jameshard.ing/pilot)

此“Show HN”帖子详细介绍了空客A350飞行员对可视化飞行数据的热情。这位飞行员是英国航空公司的副驾驶，他使用 LogTen Pro 飞行日志的 SQL 查询来生成交互式图形和地球仪。

该帖子重点介绍了几个有趣的视觉效果，包括：

*   **目的地矩阵：** 一个圆形可视化图，显示国家之间的航班连接，揭示了由于定位飞行造成的差异。
*   **飞行日历：** 一个 GitHub 风格的“活动图”，描绘了每日飞行时间，说明了 Covid-19 大流行以及短途和长途航线之间过渡等事件的影响。
*   **3D 地球仪：** 展示按国家和机场划分的航班的交互式地球仪。
*   **年度小时数：** 按飞行员角色（PIC、PICUS、P2、Heavy）分类的年度飞行小时数细分。
*   **累计小时数：** 每种飞机类型（A320 系列和 A350）的总飞行时间。
*   **飞行时间与距离：** 比较飞行时间和距离的散点图，揭示了伦敦西部航班上盛行风的影响。

这位飞行员还提到了他们的培训经历，包括英国航空公司的学员计划和加拿大的飞行奖学金，最终获得了滑翔机飞行员执照和教练等级。 与同为空客 A350 机长的父亲一起飞行被认为是职业生涯的亮点。 总体目标是以引人入胜且富有洞察力的方式呈现飞行数据，展示飞行员的经验和对航空的热情。

---

## 2. Rust 中的奇怪表达

**原文标题**: Weird Expressions in Rust

**原文链接**: [https://www.wakunguma.com/blog/rust-weird-expr](https://www.wakunguma.com/blog/rust-weird-expr)

Rust中的“奇特表达式”探索

---

## 3. 十年果树水彩画

**原文标题**: 10 Years of Pomological Watercolors

**原文链接**: [https://parkerhiggins.net/2025/04/10-years-of-pomological-watercolors/](https://parkerhiggins.net/2025/04/10-years-of-pomological-watercolors/)

本文庆祝作者首次呼吁公开美国政府的植物学水彩画收藏（一个包含超过7000幅水果画作的图书馆）十周年。作者详细描述了他们的旅程，最初通过信息自由法案请求揭示该收藏已被数字化，但设置了昂贵的付费墙。

在成功倡导其公开发布后，作者并没有就此止步。他们构建了Python软件，将图像上传到维基共享资源，标志着他们编程生涯的开始。这促使他们创建了社交媒体机器人，在Twitter（现在的X）、Bluesky和Mastodon上展示该收藏。作者重点介绍了其他项目，如在国家档案馆的演讲、为音乐会制作的可视化视频以及数据贡献。

作者对看到该收藏被广泛欣赏感到高兴，并注意到它出现在咖啡桌书、学术研究、明信片、艺术版画以及《纽约时报》和Defector等媒体报道中。他们甚至在电视剧《富家穷路》中发现了一幅画作。

作者强调了追求他们对公共领域的兴趣，特别是对植物学水彩画收藏的好奇心所带来的意想不到的积极影响，并指出他们目前正在找工作。

---

## 4. Qwen VLo：从“理解”世界到“描绘”世界

**原文标题**: Qwen VLo: From "Understanding" the World to "Depicting" It

**原文链接**: [https://qwenlm.github.io/blog/qwen-vlo/](https://qwenlm.github.io/blog/qwen-vlo/)

Qwen VLo 是 Qwen 系列中一种新型统一多模态模型，专为理解和生成图像而设计。它建立在之前的 QwenVL 模型之上，从简单地“理解”图像内容，发展到基于这种理解创建高质量的重建图像。此预览版可通过 Qwen Chat 访问，允许用户通过文本提示生成图像（例如，“生成一张可爱猫咪的图片”）或修改现有图像（例如，上传一张猫的图片，并询问“在猫的头上加一顶帽子”）。

主要亮点包括：

*   **精确的内容理解与再现：** 改进了语义一致性和细节捕捉能力，以避免图像生成过程中的误解。
*   **开放式指令驱动的编辑：** 能够响应创造性的自然语言指令，进行风格转换、场景重建、精细润饰，甚至涉及物体、文本和背景的复杂修改。
*   **多语言指令支持：** 支持中文和英文。

该文档展示了 Qwen VLo 的各种用例，包括：

*   基于详细提示生成和修改图像，例如给柴犬添加配饰或更改背景。
*   风格转换，将图像转换为不同的艺术风格（吉卜力、海贼王、龙珠等）或转换为逼真的照片、3D 渲染，甚至毛绒玩具。
*   复杂的图像提示处理，例如生成包含多个角色和元素的场景。
*   使用特定视觉元素和文本创建海报。
*   感知和定位任务，例如边缘检测和对象分割。
*   多图输入以及涉及文本和图像输入的任务。
*   直接的文本到图像生成。

该模型旨在充当“人类艺术家”，通过增强的灵活性和控制力，将用户的想象力转化为现实。

---

## 5. 无需任何特殊设备，通过超声波传输数据

**原文标题**: Transmitting data via ultrasound without any special equipment

**原文链接**: [https://halcy.de/blog/2025/06/27/transmitting-data-via-ultrasound-without-any-special-equipment/](https://halcy.de/blog/2025/06/27/transmitting-data-via-ultrasound-without-any-special-equipment/)

本文（2025年6月27日撰写）探讨了使用标准计算机设备通过超声波传输数据的可能性。作者解释了超声波是指超出人类听觉范围的声音频率（高于20000 Hz）的概念，并证明即使是典型的笔记本电脑扬声器和麦克风也能够产生和检测这些频率。

核心思想是在超声波信号中编码数据并在设备之间传输。作者详细介绍了两种尝试的方法：摩尔斯电码和频移键控（FSK）。事实证明，FSK（数据被编码为音调变化）更为成功，并通过基于WebAudio的工具进行了演示。

该网站允许用户通过将消息转换为高频音频信号并在另一台设备上接收它们来发送消息。文章包含代码片段，展示了信号是如何被编码的（将比特转换为RTZ FSK音频）和解码的（分析频谱中的能量峰值）。

作者承认存在局限性，包括易受干扰、缺乏纠错和传输速度慢。他们鼓励读者改进该系统，并建议进行改进，例如Reed-Solomon纠错。源代码已在GitHub上提供。

最后，文章揭示了这种类型的超声波信号已经用于呼叫软件中，以检测参与同一会议的附近设备。

---

## 6. 我从Flutter和Rust转向Rust和Egui

**原文标题**: I Switched from Flutter and Rust to Rust and Egui

**原文链接**: [https://jdiaz97.github.io/greenblog/posts/flutter_to_egui/](https://jdiaz97.github.io/greenblog/posts/flutter_to_egui/)

作者详述了将BoquilaHUB项目的技术栈从 Flutter + Rust 切换到 Rust + egui 的决定。最初，他们使用 Flutter 构建用户界面，Rust 处理后端逻辑，并通过 flutter_rust_bridge 连接两者。然而，由于与 FFI（外部函数接口）相关的复杂性，以及 flutter_rust_bridge_codegen 生成的大量、难以阅读且难以优化的代码，他们感到沮丧。

作为唯一的开发者，作者发现 Flutter 的 UI 功能未得到充分利用，并且该框架的状态管理（例如“setstate 没有刷新”问题）增加了不必要的复杂性。

切换到 egui 使他们能够用 Rust 编写整个应用程序，从而简化了代码库。Egui 的立即模式范例（UI 每帧刷新）消除了对复杂状态管理解决方案和回调的需求。添加 UI 元素变得直接且可预测。

作者还感觉到全 Rust 技术栈带来了性能提升。虽然没有明确比较 Rust 和 Dart 的速度，但消除 FFI 开销（克隆数据、调用 ONNX Runtime）导致应用程序明显更流畅、响应更快。本质上，这次切换降低了复杂性，发挥了作者的优势，并且似乎提高了性能，从而使项目更易于维护和理解。

---

## 7. Bitmovin (YC S15) 正在丹佛招聘初级解决方案工程师

**原文标题**: Bitmovin (YC S15) Is Hiring a Junior Solutions Engineer in Denver

**原文链接**: [https://bitmovin.com/careers/7943569002/](https://bitmovin.com/careers/7943569002/)

无法访问文章链接。

---

## 8. Whitesmiths C 编译器：最早的商用 C 编译器之一

**原文标题**: Whitesmiths C compiler: One of the earliest commercial C compilers available

**原文链接**: [https://github.com/hansake/Whitesmiths-C-compiler](https://github.com/hansake/Whitesmiths-C-compiler)

本文讨论了Whitesmiths C编译器，这是最早的商业C编译器之一，最初于1978年发布。它是C语言的完全重新实现，不同于Unix。到1985年，3.0版本支持新兴的ANSI C标准，并为各种平台（如DEC PDP-11、Intel 8080和IBM System/370）提供了代码生成器，使其成为流行的交叉编译器。

作者强调了保存该软件的重要性，并分享了Whitesmiths公司1978年至1988年的总裁P.J. Plauger已授权将该编译器用于非商业下载，但前提是收到打包软件的副本。

本文详细介绍了特定编译器版本的当前可用性以及资源：CP/M-80 Edition 2.2版本的Whitesmiths C编译器二进制文件及其手册；Whitesmiths C交叉编译器（用于IBM System/36 Version 3.1的MS-DOS主机）的二进制文件、QEMU磁盘映像及其手册；CP/M-80编译器Edition 2.2的源代码及其Makefile；以及用于Z80的Whitesmiths/COSMIC C交叉编译器Version 3.32的手册。作者希望通过添加更多主机和目标来扩展构建环境。

---

## 9. 月球基地阿尔法：美国国家航空航天局制作表情包游戏的那次

**原文标题**: Moonbase Alpha: That time NASA made a meme video game

**原文链接**: [https://www.spacebar.news/moonbase-alpha-nasa-video-game/](https://www.spacebar.news/moonbase-alpha-nasa-video-game/)

美国宇航局试图通过视频游戏吸引公众，于2010年催生了“月球基地阿尔法”，这是一款由陆军游戏工作室和Virtual Heroes开发的月球基地模拟器。该游戏旨在作为一款大型多人在线游戏的先导，要求玩家在有限的时间内修复一个受损的月球基地。尽管最初的评价褒贬不一，但由于其DECtalk语音合成功能，该游戏意外地获得了欢迎。

玩家利用DECtalk的音高和时长控制功能在游戏中创建歌唱比赛，制作了大量病毒式内容，用合成声音翻唱流行歌曲。这一意想不到的功能将“月球基地阿尔法”变成了一个梗，吸引了一批狂热的追随者，并将其与Vocaloid音乐社区联系起来。

尽管“月球基地阿尔法”取得了成功，但承诺的太空大型多人在线游戏，最初名为“宇航员：月球，火星及更远”（后更名为“星光：宇航员学院”）却从未实现。尽管获得了众筹和来自各组织的资助，但该项目受到内部纠纷和资金限制的困扰，最终导致未完成的演示和失败。虽然“月球基地阿尔法”的辉煌时刻已经过去，但它仍然可以免费获得，其遗产通过其对互联网文化的独特贡献以及偶尔出现的受DECtalk启发的歌曲而得以延续。

---

## 10. 使用新标签兼容性规则的C语言参数化类型

**原文标题**: Parameterized types in C using the new tag compatibility rule

**原文链接**: [https://nullprogram.com/blog/2025/06/26/](https://nullprogram.com/blog/2025/06/26/)

C23标签兼容性规则与宏参数化类型

本文探讨了C23中的一项新特性，即结构体、联合体和枚举的“标签兼容性规则”，以及它如何利用宏实现有限形式的类型参数化。 以前，不同翻译单元 (TU) 中相同的结构体定义被认为是不同的、不兼容的类型。 C23 改变了这一点，如果它们具有相同的标签（名称）和字段，则使它们兼容。

作者演示了如何将此特性与宏结合使用来创建参数化类型，如动态数组（切片）。 无需为每种类型 `T` 编写 `SliceT` 类型定义，宏 `Slice(T)` 可以按需生成兼容的结构体定义。 这允许声明使用针对不同元素类型参数化的切片的函数，例如 `Slice(int)`、`Slice(float)` 或 `Slice(Str)`。

本文还涉及了这种方法的局限性。 虽然它可以参数化类型，但它不能参数化作用于这些类型的函数，这与 C++ 模板不同。 由于宏实现需要一个简单的标识符，因此像 `Slice(Slice(float))` 这样的复杂类型组合也存在问题。 然而，泛型函数可以使用 C23 的 `typeof` 来补充这项新技术，以改进对齐控制。 作者提供了一个演示程序 (`demo.c`) 来测试该特性，并鼓励读者通过电子邮件讨论它。 尽管承认了潜在的缺点，但作者得出结论，探索这项技术是值得的。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 2 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 3 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 4 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 5 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 6 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 7 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 8 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 9 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 10 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 11 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 12 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 13 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 14 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 15 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 16 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 17 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 18 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 19 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 20 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 21 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 22 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 23 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 24 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 25 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 26 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 27 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 28 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 29 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 30 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 31 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 32 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 33 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 34 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 35 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 36 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 37 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 38 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 39 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 40 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 41 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 42 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 43 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 44 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 45 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 46 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 47 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 48 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 49 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 50 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 51 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 52 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 53 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 54 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 55 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 56 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 57 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 58 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 59 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 60 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 61 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 62 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 63 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 64 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 65 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 66 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 67 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 68 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 69 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 70 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 71 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 72 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 73 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 74 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 75 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 76 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 77 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 78 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 79 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 80 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 81 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 82 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 83 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 84 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 85 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 86 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 87 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 88 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 89 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 90 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 91 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 92 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 93 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 94 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 95 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 96 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 97 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 98 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 99 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 100 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
