# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-10-24.md)

*最后自动更新时间: 2025-10-24 17:50:12*
## 1. 禁用火狐浏览器中的人工智能

**原文标题**: Disable AI in Firefox

**原文链接**: [https://flamedfury.com/posts/disable-ai-in-firefox/](https://flamedfury.com/posts/disable-ai-in-firefox/)

本文详细介绍了如何禁用集成到 Firefox 浏览器中的新 AI 功能。作者表达了对这些功能（如弹出式聊天建议和侧边栏 AI）默认启用，且弊大于利的失望之情。

提供的首要解决方案是通过在 Firefox 地址栏中导航至 `about:config`，搜索 `browser.ml.enable`，并将其设置为 `false` 来禁用 Firefox 机器学习平台的总开关。这将禁用所有 AI 功能。

或者，作者提供了一个可以单独禁用各个 AI 功能的列表，同时保持总开关启用。这允许用户选择性地禁用他们认为具有破坏性的特定功能。然后，本文列出了每个设置并解释了它控制的内容，包括 AI 聊天机器人集成、页面上的聊天菜单、基于 AI 的链接预览和智能标签页分组等功能。

作者还分享了他们测试“智能标签页分组”功能的意图，以了解 AI 组织打开的标签页的有效性。他们将报告其有用性。最终，本文旨在为希望自定义或完全禁用新引入的 AI 功能的 Firefox 用户提供指导。

---

## 2. “Attention is all you need”合著者称他“厌倦”了Transformer

**原文标题**: 'Attention is all you need' coauthor says he's 'sick' of transformers

**原文链接**: [https://venturebeat.com/ai/sakana-ais-cto-says-hes-absolutely-sick-of-transformers-the-tech-that-powers](https://venturebeat.com/ai/sakana-ais-cto-says-hes-absolutely-sick-of-transformers-the-tech-that-powers)

以下是基于标题提供的VentureBeat文章的摘要：

文章讨论了“Attention is All You Need”这篇开创性论文（介绍了Transformer架构）的合著者David Ha对Transformer在人工智能领域被过度使用及其局限性的担忧。作为Sakana AI的首席技术官，Ha表达了对Transformer感到“厌倦”的情绪，这表明一种日益增长的观点，即人工智能界需要探索替代方案，并超越当前的主导范式。

文章可能强调以下几点：

*   **Transformer的主导地位：** 强调了Transformer在现代人工智能中的普遍性，为大型语言模型（LLMs）和各种其他应用程序提供支持。
*   **Ha的不满：** 展示了David Ha的挫败感以及他希望看到Transformer架构之外的创新的愿望。这可能源于对可扩展性、效率或能力方面停滞不前或局限性的感知。
*   **寻找替代方案：** 暗示Sakana AI正在积极研究和开发替代人工智能架构，以解决Transformer的感知缺陷。这可能涉及仿生学、新的注意力机制或完全不同的计算方法。
*   **Transformer的潜在局限性：** 文章可能涉及具体的局限性，例如计算成本、数据效率低下、推理或可解释性困难，或潜在的偏见放大。
*   **呼吁创新：** 将Ha的评论定位为呼吁人工智能界探索新的途径，并将人工智能研究的边界推向超越Transformer这条老路的界限。

本质上，这篇文章表明，Transformer革命的关键架构师现在认为，是时候迎接人工智能创新的新时代了，而这需要通过克服当前主导架构的局限性来实现。

---

## 3. Twake Drive – Google Drive 的开源替代方案

**原文标题**: Twake Drive – An open-source alternative to Google Drive

**原文链接**: [https://github.com/linagora/twake-drive](https://github.com/linagora/twake-drive)

Twake Drive：一款开源的Google Drive替代方案。该项目提供文件存储和共享功能。

本文提供了一份快速入门指南，介绍如何从GitHub克隆仓库并使用Docker以最小配置运行它，这使得用户能够快速测试和部署本地实例。

为了进行开发，本文概述了先决条件（Node.js、MongoDB和Yarn），并详细介绍了设置过程，包括使用Docker启动MongoDB、启动前端和启动后端。这些说明还包括为后端设置必要的环境变量，例如数据库连接和存储路径。它指向一个配置文件，以便进一步调整参数。

该软件根据Affero GPL v3许可协议授权，强调其开源性质。该文档还包含Telegram、项目网站、问题跟踪器和路线图的链接，以便进一步探索和互动。

---

## 4. Linux 磁盘 I/O 图 (2024)

**原文标题**: Linux disk I/O diagram (2024)

**原文链接**: [https://zenodo.org/records/15234151](https://zenodo.org/records/15234151)

本文发布于2024年4月17日，介绍了一个展示Linux磁盘I/O子系统的图表。该图表由爱立信尼古拉·特斯拉的Hrvoje Horvat创建，详细说明了I/O过程中各种组件及其相应的命令。

该图表概述了I/O过程在不同层之间的流动：应用层、使用直接I/O或缓冲区+页面缓存的虚拟文件系统（VFS）层、文件系统层、可选的块层、通用块层、磁盘调度器层（BLK-Mq或经典的I/O调度器，如noop、anticipatory、deadline或cfq）、块设备驱动程序层、设备驱动程序，最后是硬件（RAID控制器或连接到硬盘驱动器（如HDD、SSD和NVMe驱动器）的磁盘控制器）。

该图表包含在文件"Disk IO-ALL-expanded-poster--EN.pdf"中，是书籍《Operativni sustavi i računalne mreže - Linux u primjeni》（DOI: 10.5281/zenodo.8119310）的一部分。 该图旨在为改进理解和应用提供Linux磁盘I/O子系统的全面可视化表示。

---

## 5. Typst 0.14

**原文标题**: Typst 0.14

**原文链接**: [https://typst.app/blog/2025/typst-0.14/](https://typst.app/blog/2025/typst-0.14/)

Typst 0.14 于 2025 年 10 月 24 日发布，强调可访问性并扩展了生产能力。核心功能是在生成的 PDF 中默认启用可访问性，包括屏幕阅读器的标签和语义含义。图形上的新 `alt` 参数允许为辅助技术提供替代文本描述。该版本还支持 PDF/UA-1 通用可访问性标准，有助于遵守 EAA 和 ADA 等法规。

Typst 0.14 扩展了 PDF 标准支持，允许用户选择 PDF 版本 1.4-2.0 和各种 PDF/A 子标准。它还引入了原生 PDF 支持，作为所有导出目标（PDF、HTML、SVG、PNG）的图像格式，由内部 "hayro" PDF 处理库处理。

字符级对齐通过调整字符之间的间距来增强排版效果，使段落在视觉上更加平衡，补充了单词间距的调整。这解决了微排版问题，并提供了 LaTeX 的替代方案。

HTML 导出功能得到了显著增强，语义元素现在能够正确映射到 HTML，并且新的类型化 HTML 接口简化了元素构造。HTML 导出功能很快将在 Web 应用程序中提供。

迁移到 Typst 0.14 通常很顺利，只有一些小的破坏性更改，主要集中在更严格的验证上。弃用的功能包括 `pdf.embed`（替换为 `pdf.attach`）和一个重命名的参考文献样式。Web 应用程序具有改进的升级体验，带有自动兼容性检查。

Typst 团队将于 11 月 7 日在 Discord 上举行社区电话会议，讨论新版本。

---

## 6. Mesh2Motion – 用于动画 3D 模型的开源 Web 应用

**原文标题**: Mesh2Motion – Open-source web application to animate 3D models

**原文链接**: [https://mesh2motion.org/](https://mesh2motion.org/)

Mesh2Motion 是一款免费开源的Web应用程序，旨在为3D模型（特别是人形、四足动物和鸟类生物）制作动画。其目标是为网页和游戏引擎提供一个易于访问的3D模型动画制作工具，可用于个人和商业用途。

该应用程序支持导入GLB、GLTF和FBX格式的模型，并为人类和动物提供各种骨骼选项。它具有直观的骨骼定位功能、用于纠正错误的撤销/重做系统，以及同时导出多种动画为广泛支持的GLB格式的能力。用户还可以访问来自Quaternius的人类动画库。

该项目强调其开源性质，鼓励社区参与和发展。GitHub存储库（[github.com/scottpetrovic/mesh2motion-app](github.com/scottpetrovic/mesh2motion-app)）是提交错误报告、反馈意见和访问代码的主要平台。或者，可以通过Scott Petrovic的社交媒体账号@scottpetrovic和@scottpetrovic.bsky.social联系他本人。

---

## 7. 为什么要形式化数学——不仅仅是为了发现错误

**原文标题**: Why formalize mathematics – more than catching errors

**原文链接**: [https://rkirov.github.io/posts/why_lean/](https://rkirov.github.io/posts/why_lean/)

本文认为数学形式化，特别是使用像Lean这样的工具，带来的好处远不止捕捉证明中的错误。作者将其与软件工程中TypeScript的采用相提并论，在后者中，最初对错误检测的关注远不如意想不到的优势更有价值。

作者强调了数学形式化的几个关键好处：

*   **增强的工具支持：**形式化支持强大的IDE功能，例如点击查看定义、悬停显示声明、自动生成文档和非字符串搜索。这与LaTeX等传统方法形成对比，在传统方法中，定义在很大程度上仍然存在于脑海中。

*   **元数学分析：**通过固定的定理名称和导入，可以分析数学证明的结构、绘制定理依赖关系图，并自动发现替代证明路径。

*   **改进的版本控制：**形式化的结果可以被视为具有版本控制和依赖管理的库，从而可以更可靠地跟踪和撤回结果。这在撤回结果必须影响大量相关声明的领域中尤其重要。

*   **仅声明本身就有价值：**即使没有完整的证明，形式化数学陈述也是一项有价值的工作，有助于提高严谨性和清晰度。

作者承认数学家采用新工具和工作流程面临挑战，但表示希望长期效益将使这种转变值得。虽然证明“微不足道”的陈述可能看起来很繁琐，但像Lean这样的工具中自动化策略的强大功能正在使这项任务变得不那么令人望而却步。

---

## 8. 朝日 Linux 仍在努力支持 Apple M3，M1n1 引导加载程序转向 Rust

**原文标题**: Asahi Linux Still Working on Apple M3 Support, M1n1 Bootloader Going Rust

**原文链接**: [https://www.phoronix.com/news/Asahi-Linux-M3-m1n1-Update](https://www.phoronix.com/news/Asahi-Linux-M3-m1n1-Update)

朝日Linux项目致力于将Linux移植到苹果芯片Mac电脑上，并在开发工作中不断取得进展。根据最近的进度报告，内核补丁正在向上游推送至Linux 6.17和6.18版本，Apple M2 Pro/Max/Ultra设备的设备树已进入Linux 6.18版本。

一项重大进展是将m1n1引导加载程序（在苹果芯片上启动Linux的关键组件）计划迁移到Rust编程语言。此举的动机是为了提高这种关键软件的可维护性、安全性和逻辑正确性。

该团队还专注于改善用户体验，在运行更多游戏和改善muvm之外的Wine兼容性方面取得了进展。图形驱动程序支持也在不断成熟。

虽然在M1和M2设备上的进展强劲，但Asahi Linux团队仍在努力获得对Apple M3芯片的基本支持。目前，M3可以启动到闪烁的光标，但要使其具有实际可用性，仍有许多工作要做。他们计划在未来改进M3支持。完整的进度报告可以在AsahiLinux.org上找到。

---

## 9. 大鹏相机

**原文标题**: Roc Camera

**原文链接**: [https://roc.camera/](https://roc.camera/)

在AI生成和图像篡改泛滥的时代，Roc Camera旨在恢复摄影的真实性。文章指出，图像易于分享和生成式AI的兴起模糊了现实与虚构之间的界限，导致人们对视觉媒体的信任丧失。

Roc Camera提出了一种解决方案，通过结合认证的传感器数据、零知识证明（ZK证明）和防篡改环境来捕捉“可验证的真实照片”。这项技术为每张照片创建唯一的指纹，确保它只能由Roc Camera本身拍摄。

该过程涉及三个关键步骤：拍摄照片、创建相机传感器数据和元数据的ZK证明，以及使用Roc Photo SDK验证照片的真实性。

相机本身具有4英寸IPS LCD屏幕、带有广角镜头的16MP Sony IMX519 CMOS传感器、带有4GB RAM的Raspberry Pi 4、4000mAh电池和不间断电源。

Roc Camera目前可以订购（第二批），价格为399美元，发货时间为2-3周。其核心价值在于提供一种工具，用于在数字篡改时代捕捉和验证摄影瞬间的真实性。

---

## 10. 早期宇宙或曾存在“结主导时代”：研究

**原文标题**: A “knot dominated era” may have existed in the early universe: study

**原文链接**: [https://phys.org/news/2025-10-key-universe-1800s-idea-science.html](https://phys.org/news/2025-10-key-universe-1800s-idea-science.html)

本文探讨了一种新的理论，该理论认为早期宇宙中形成的“宇宙结”在物质与反物质的不对称性中发挥了关键作用，最终导致了我们今天所看到的一切的存在。

广岛大学和德国电子同步加速器的研究人员认为，通过将规范化的重子数减轻子数（B-L）对称性与Peccei-Quinn（PQ）对称性相结合，可能会出现稳定的结状结构。这些由磁通量管和超流体涡旋产生的结，在大爆炸后短暂地主导了宇宙的能量密度。

随着这些结通过量子隧穿坍缩，它们产生了重型右手性中微子，这些中微子随后衰变，略微偏向物质多于反物质，从而解决了“重子产生”之谜——为什么宇宙中物质多于反物质。 该模型表明，这个过程将宇宙重新加热到100 GeV的关键温度，这是电弱反应将中微子不平衡转化为物质的最后一个窗口。

该理论预测了来自这个“结主导时代”的独特引力波信号，未来可能会被LISA、Cosmic Explorer和DECIGO等天文台探测到。 研究人员认为，该模型首次将结的概念与粒子物理学联系起来，并可能提供对宇宙起源的更全面的理解。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 2 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 3 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 4 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 5 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 6 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 7 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 8 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 9 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 10 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 11 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 12 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 13 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 14 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 15 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 16 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 17 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 18 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 19 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 20 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 21 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 22 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 23 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 24 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 25 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 26 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 27 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 28 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 29 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 30 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 31 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 32 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 33 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 34 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 35 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 36 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 37 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 38 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 39 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 40 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 41 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 42 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 43 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 44 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 45 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 46 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 47 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 48 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 49 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 50 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 51 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 52 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 53 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 54 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 55 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 56 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 57 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 58 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 59 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 60 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 61 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 62 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 63 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 64 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 65 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 66 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 67 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 68 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 69 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 70 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 71 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 72 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 73 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 74 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 75 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 76 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 77 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 78 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 79 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 80 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 81 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 82 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 83 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 84 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 85 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 86 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 87 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 88 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 89 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 90 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 91 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 92 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 93 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 94 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 95 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 96 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 97 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 98 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 99 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 100 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 101 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 102 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 103 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 104 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 105 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 106 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 107 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 108 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 109 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 110 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 111 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 112 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 113 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 114 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 115 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 116 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 117 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 118 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 119 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 120 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 121 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 122 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 123 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 124 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 125 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 126 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 127 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 128 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 129 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 130 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 131 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 132 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 133 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 134 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 135 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 136 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 137 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 138 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 139 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 140 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 141 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 142 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 143 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 144 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 145 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 146 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 147 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 148 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 149 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 150 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 151 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 152 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 153 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 154 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 155 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 156 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 157 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 158 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 159 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 160 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 161 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 162 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 163 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 164 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 165 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 166 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 167 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 168 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 169 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 170 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 171 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 172 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 173 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 174 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 175 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 176 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 177 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 178 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 179 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 180 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 181 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 182 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 183 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 184 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 185 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 186 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 187 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 188 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 189 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 190 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 191 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 192 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 193 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 194 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 195 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 196 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 197 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 198 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 199 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 200 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 201 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 202 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 203 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 204 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 205 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 206 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 207 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 208 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 209 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 210 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 211 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 212 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 213 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 214 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 215 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 216 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 217 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 218 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 219 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
