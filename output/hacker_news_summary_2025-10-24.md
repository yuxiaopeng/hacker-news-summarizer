# Hacker News 热门文章摘要 (2025-10-24)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 63节点分片DuckDB在5秒内完成1T行聚合挑战

**原文标题**: A sharded DuckDB on 63 nodes runs 1T row aggregation challenge in 5 sec

**原文链接**: [https://gizmodata.com/blog/gizmoedge-one-trillion-row-challenge](https://gizmodata.com/blog/gizmoedge-one-trillion-row-challenge)

GizmoData 使用分片 DuckDB 在 63 个节点上成功完成了万亿行聚合挑战，仅用时 5 秒。这篇来自 GizmoData 的文章突显了他们在企业级分析中有效利用大规模 DuckDB 的能力。关键在于他们在此设置中实现的速度和效率，展示了 DuckDB 在分布式环境中处理大型数据集的潜力。虽然文章简短，但暗示了 GizmoData 在数据分析解决方案方面的专业知识以及其优化 DuckDB 以执行性能关键任务的能力。他们将自己定位为能够以惊人的速度处理大量数据的提供商，这对企业级分析需求有利。重点是展示他们的技术能力以及他们的解决方案对于处理大型数据集的企业的潜在优势。

---

## 12. 冰岛首次发现蚊子

**原文标题**: Mosquitoes discovered in Iceland for the first time

**原文链接**: [https://www.cnn.com/2025/10/21/climate/iceland-mosquito-discovery](https://www.cnn.com/2025/10/21/climate/iceland-mosquito-discovery)

冰岛首次发现蚊子：或因气候变化入侵

在冰岛，这个此前因严酷冬季而免受蚊虫侵扰的国家，首次发现了蚊子。比约恩·夏尔塔松在冰岛西部发现了三只环纹库蚊，昆虫学家马蒂亚斯·阿尔弗雷德松随后确认了它们的身份。

这标志着在冰岛自然环境中首次确认存在蚊子，尽管此前曾在飞机上发现过一只蚊子。环纹库蚊原产于东半球的广大地区，通过在隐蔽地点以成虫越冬的方式适应寒冷气候。

文章讨论了蚊子可能通过船只或集装箱抵达的可能性，并强调需要进一步监测，以确定它们能否过冬并建立种群。

这一发现正值人们对气候变化及其对全球蚊子种群影响的担忧之际。气温上升和天气模式变化正在扩大这些携带疾病的昆虫的活动范围和寿命。虽然冰岛经历了创纪录的高温，但专家们对将蚊子的发现直接与气候变化联系起来持谨慎态度，并指出环纹库蚊已经适应了寒冷气候。需要进一步的研究来了解气候变化在蚊子分布和潜在范围转移中的作用。

---

## 13. 大型机六巨头 (2022)

**原文标题**: The Mainframe Six (2022)

**原文链接**: [https://arcanesciences.com/os2200/app1.html](https://arcanesciences.com/os2200/app1.html)

《大型机六巨头》详细介绍了截至2022年大型机行业中剩余的六家公司：IBM、Unisys、富士通、日立、源讯和NEC。它概述了它们的地域重点、客户群规模估计、操作系统和CPU开发状态。

IBM凭借其全球影响力和庞大的客户群（使用其强大的Z系统）占据主导地位。Unisys也具有全球影响力，服务于银行/电信（MCP）和航空/政府（OS 2200）领域，在退出定制CPU后依赖模拟器。富士通专注于北美以外的地区，提供多个大型机系列（BS2000、GS21、ICL 29系列），用户群集中在德国和日本，尽管ICL系统主要在英国进行模拟。

日立仅在日本销售，在使用其VOS3操作系统（在放弃定制CPU后）重新命名的IBM Z系统。源讯收购了布尔，维护着GCOS 7（在x86上模拟）和GCOS 8（在Itanium上模拟）操作系统，在西欧、北美和非洲拥有少量客户群。最后，NEC主要拥有日本客户群，继续为其ACOS-4操作系统设计自己的处理器。文章估计了每家公司的客户群规模，突出了每个操作系统及其相应架构的独特特征。

---

## 14. ChunkLLM: 加速LLM推理的轻量级可插拔框架

**原文标题**: ChunkLLM: A Lightweight Pluggable Framework for Accelerating LLMs Inference

**原文链接**: [https://arxiv.org/abs/2510.02361](https://arxiv.org/abs/2510.02361)

本文介绍了ChunkLLM，一种轻量级且可插拔的训练框架，旨在通过解决自注意力机制的计算效率低下问题来加速大型语言模型（LLM）的推理。ChunkLLM解决了现有块选择和压缩方法中普遍存在的语义不完整和训练-推理效率低下的问题。

该框架包含两个主要组件：QK适配器（Q-Adapter和K-Adapter）和Chunk适配器。QK适配器连接到每个Transformer层，用于压缩特征并获取块注意力。Chunk适配器在底层运行，利用上下文语义信息来检测块边界。

在训练期间，仅训练QK适配器和Chunk适配器，而骨干模型保持冻结。采用注意力蒸馏方法来训练QK适配器，提高关键块的召回率。在推理期间，仅当检测到块边界时才激活块选择，从而加速该过程。

在各种长文本和短文本基准测试上的实验表明，ChunkLLM在短文本上实现了可比的性能。重要的是，它在保持48.58%的键值缓存保留率的同时，在长文本上保持了98.64%的性能。此外，在处理120K长文本时，ChunkLLM实现了高达4.48倍的速度提升，与原始Transformer相比，证明了其效率。

---

## 15. 廉价DIY太阳能围栏设计

**原文标题**: Cheap DIY solar fence design

**原文链接**: [https://joeyh.name/blog/entry/cheap_DIY_solar_fence_design/](https://joeyh.name/blog/entry/cheap_DIY_solar_fence_design/)

本文详细介绍了一个DIY太阳能围栏项目，它为传统的地面安装太阳能阵列提供了一种经济高效的替代方案。作者采用了Ironridge屋顶安装硬件来设计垂直围栏，与传统的地面安装系统相比，显著降低了成本。他们使用了易于获得的材料，如经过处理的4x4立柱和Ironridge XR-10导轨来建造结构。

主要建造要点包括：

* 使用7英尺长的Ironridge XR-10导轨，每根导轨可固定两块面板。
* 将12英尺长的4x4立柱安装在3英尺深的混凝土填充孔中，每段围栏成对设置。
* 使用Ironridge L型支架和木螺钉将导轨连接到立柱，并使用保护胶带以防止腐蚀。
* 在面板下方增加额外的支撑支架，以防止滑动（尽管后来证明没有必要）。
* 设置围栏间距，以便在下方进行割草。

该设计结合了成对立柱以提高稳定性和灵活性，以适应不平坦的地形和弯曲的布局，从而优化太阳照射。添加了背部支撑以抵抗风力。作者报告说，第一年后没有出现问题，经过处理的木材寿命是预期的限制因素。

该太阳能围栏使用Aptos 370W双面面板，已被证明是宝贵的电力来源，并作为更大太阳能发电场的电力主干网。围栏安装硬件的总成本约为每块太阳能板110美元。

---

## 16. Apple II 上的 VisiCalc

**原文标题**: VisiCalc on the Apple II

**原文链接**: [https://stonetools.ghost.io/visicalc-apple2/](https://stonetools.ghost.io/visicalc-apple2/)

本文回顾了VisiCalc，这款开创性的电子表格软件对Apple II的早期成功做出了重大贡献。作者着重讲述了史蒂夫·乔布斯介绍它的那个未经证实的传闻，并强调了该产品的真正影响，估计Apple II销量的25%是由VisiCalc单独驱动的。文章赞扬了Dan Bricklin和Bob Frankston的远见卓识，并指出尽管以现代标准来看VisiCalc显得“笨拙”，但它从一开始就做得非常出色。

作者探讨了用户体验，详细描述了其易于识别的界面、创新的“斜杠菜单”以及当时的独特限制，例如有限的RAM和需要手动管理重新计算。文章强调了通过其原始教程来理解VisiCalc的重要性，该教程有效地解释了计算机化电子表格的概念，并展示了其优于传统方法的好处。作者指出，菜单命令的直观性和“基本的自动完成”功能促进了其易用性。

文章还触及了VisiCalc的文化影响，强调了其熟悉的设计已变得如此普遍，以至于很难体会其最初的意义。它讨论了在其成功之后涌现出的“VisiCalc克隆产品”的泛滥，并使用书籍《动物营养和饲养的电子表格应用》来展示VisiCalc的各种应用。最终，作者赞扬了VisiCalc的天才之处在于使数据处理变得易于访问和直观，从而改变了人们与计算机交互的方式。

---

## 17. Padlet (YC W13) 正在旧金山和新加坡招聘

**原文标题**: Padlet (YC W13) Is Hiring in San Francisco and Singapore

**原文链接**: [https://padlet.jobs](https://padlet.jobs)

这并非一份寻常的招聘启事，而是Padlet创始人兼CEO Nitesh所创作的一首鼓舞人心的颂歌。信息并非关于具体的职位或资质要求，而是一篇激励潜在员工的动员令。

其核心信息颂扬了工作、奉献和贡献的价值。它强调了我们享受到的舒适、快乐和回忆，都源于前人的努力和当今人们的持续工作。这首“颂歌”描绘了一幅与工作生活相关的日常奋斗和胜利的画面，强调了无论面临何种挑战，都要坚持付出努力的重要性。它鼓励读者积极参与创造和建设。虽然标题表明在旧金山和新加坡招聘，但提供的内容主要侧重于通过更广阔的视野，激励潜在候选人通过他们的工作为世界做出贡献。

---

## 18. 前往黑洞的星际任务

**原文标题**: Interstellar Mission to a Black Hole

**原文链接**: [https://www.centauri-dreams.org/2025/10/23/interstellar-mission-to-a-black-hole/](https://www.centauri-dreams.org/2025/10/23/interstellar-mission-to-a-black-hole/)

保罗·吉尔斯特的文章探讨了星际任务前往黑洞的可能性，将焦点从仅仅瞄准像比邻星这样的系外行星转移。 他强调了科西莫·班比关于黑洞普遍性的研究，估计我们的银河系中可能存在数十亿个黑洞。 虽然已知最近的黑洞 GAIA-BH1 距离我们 1560 光年，但班比认为可能有一个黑洞位于 20-25 光年范围内。

寻找这些恒星质量黑洞，特别是孤立的黑洞，具有挑战性，但有可能使用诸如平方公里阵列、ALMA 和 JWST 等仪器，通过探测吸积产生的电磁辐射来实现。 吉尔斯特提出，如果发现附近的黑洞，它可能成为束流帆飞船任务的主要目标。 这样的任务可能包括发送纳米飞船去观察黑洞对时空的影响，测试基本常数，甚至研究事件视界的存在与否，以及“无视界致密天体”的存在。

这篇文章还引用了一项研究，该研究探讨了暗物质在系外行星内部坍塌成黑洞的可能性，这可能使它们可以被探测到。 评论区讨论了这种推论的影响，质疑为什么这样的黑洞不会立即吞噬这些行星。 文章最后强调了研究黑洞可以获得的丰富知识，并提出如果我们能够实现前往像比邻星这样的恒星的星际旅行，那么前往黑洞的任务就在我们的技术能力范围之内。

---

## 19. 反恐精英玩家经济面临数十亿美元的自由落体式崩盘

**原文标题**: Counter-Strike's player economy is in a multi-billion dollar freefall

**原文链接**: [https://www.polygon.com/counter-strike-cs-player-economy-multi-billion-dollar-freefall/](https://www.polygon.com/counter-strike-cs-player-economy-multi-billion-dollar-freefall/)

Valve 近期对《反恐精英》的更新引发了游戏玩家经济的巨大下滑，据报道一夜之间损失了 17.5 亿美元的价值。 此更新允许玩家交易升级“隐秘（红色）”级别的物品以获得刀具和手套，这些物品以前只能通过随机战利品箱获得，从而大大增加了这些备受追捧的皮肤的潜在供应量。

在此更新之前，多普勒红宝石蝴蝶刀等稀有物品的价格高达 20,000 美元。 现在，由于供应增加，这些物品的价值已经暴跌。 例如，蝴蝶刀现在的售价约为 12,000 美元，因为玩家争相抛售库存。

据报道，《反恐精英》皮肤物品的市场整体下降了 25%，CSFloat 等网站正在经历大甩卖，而 Skin Port 则难以应对激增的流量。 这种情况与 NFT 和加密货币市场的波动性相似，让交易员们争先恐后地收回投资。 虽然较低稀有度的物品和“红色”物品可能会从更新中获得一些好处，但对于高端皮肤的价值来说，整体市场转变无疑是负面的。 《反恐精英》物品经济的未来仍然不明朗。

---

## 20. 黄蜂鼓风机

**原文标题**: Wasp Blower

**原文链接**: [https://softsolder.com/2025/08/12/wasp-blower/](https://softsolder.com/2025/08/12/wasp-blower/)

这篇题为“黄蜂鼓风机”的博文，详细介绍了作者Ed自行解决前门门框内黄夹克黄蜂巢穴的方案。由于杀虫剂喷雾和粘蝇纸效果不佳，Ed制作了一个“黄蜂鼓风机”——一个安装在隧道中的风扇，将飞出巢穴的黄蜂吹入风扇叶片中，从而杀死它们。

鼓风机由一个12V电子设备外壳风扇、纸板和一个延长线组成，目标是飞出巢穴的黄蜂。虽然能有效地杀死黄蜂，但作者指出由此造成的“杀戮”令人不快。

评论区进一步探讨了黄蜂控制方法。Steve建议自制黄蜂陷阱，而Dave警告不要喷洒杀虫剂，因为它可能会将黄蜂赶入房屋深处。Dwight面临着一个位于更高处的类似黄蜂问题，他考虑过一个复杂的伺服控制喷雾罐系统，但最终决定采用一种更容易获得的解决方案。

Ed建议Dwight不要对高处的蜂巢采用过于复杂的 DIY 解决方案，并建议如果蜂巢无法触及，应寻求专业帮助，同时也强调了一些专业服务的潜在无效性。讨论最后提到了杀虫粉尘，专业人士可能会使用它进行长期虫害控制，但其对公众的可用性尚不明确。

---

## 21. 为什么Transformer不能学习乘法？

**原文标题**: Why can't transformers learn multiplication?

**原文链接**: [https://arxiv.org/abs/2510.00184](https://arxiv.org/abs/2510.00184)

这篇 arXiv 论文《为什么 Transformer 学不会乘法？逆向工程揭示了长程依赖陷阱》研究了训练 Transformer 执行多位数乘法的难度。鉴于 Transformer 在其他领域的强大能力，这看似是一个简单的任务。作者对一个 *能够* 通过隐式链式思考推理成功学习乘法的 Transformer 模型进行逆向工程，以了解标准模型失败的原因。

他们的主要发现是：

1.  **长程结构已被编码：** 成功的模型编码了多位数乘法所需的必要长程依赖关系，这已通过 logits 归因和线性探针得到证实。

2.  **机制：基于注意力的有向无环图 (DAG)：** 该模型使用注意力构建有向无环图 (DAG)，该图缓存并检索成对的中间结果。这种机制对于管理中间计算至关重要。

3.  **几何：闵可夫斯基和与傅里叶基：** 中间结果通过使用傅里叶基表示的数字的闵可夫斯基和在注意力头中实现。 这种表示形式有助于高效计算。

该论文随后探讨了为什么标准微调模型难以进行乘法运算。他们发现这些模型通常会收敛到缺乏必要长程依赖关系的局部最优解。为了验证这一点，作者引入了一个辅助损失，该损失使用线性回归探针预测运行总和。这种归纳偏置有助于模型成功学习多位数乘法。

本质上，该论文指出，Transformer 无法学习乘法源于学习和利用必要的长程依赖关系的困难，而这可以通过提供适当的归纳偏置来克服，例如鼓励模型预测运行总和。成功的模型使用基于注意力的机制来缓存和检索中间结果，以及有助于乘法的几何表示（闵可夫斯基和与傅里叶基）。

---

## 22. Debian技术委员会否决systemd变更

**原文标题**: Debian Technical Committee overrides systemd change

**原文链接**: [https://lwn.net/Articles/1041316/](https://lwn.net/Articles/1041316/)

LWN.net文章讨论了Debian技术委员会(TC)决定推翻systemd v258中的一项更改，该更改影响了依赖于世界可写`/run/lock`目录的软件。Systemd根据其自身的文件层级文档，已将该目录设置为仅root可写，从而破坏了诸如UUCP和`cu`之类的程序，这些程序依赖于世界可写权限来锁定串行设备。

虽然systemd开发者认为世界可写目录存在安全风险，并且文件系统层级标准(FHS)已经过时，但Debian策略仍然遵循FHS。此策略要求存在`/var/lock`目录（指向`/run/lock`的符号链接），从而导致了冲突。

在收到错误报告并经过讨论后，Debian TC决定systemd必须遵守Debian策略，并通过放宽权限来维护`/var/lock`的功能。TC投票要求systemd提供`/var/lock`，直到受影响的软件迁移到更好的锁定机制（如`flock()`）并且Debian策略得到更新为止。

该文章强调了上游软件更改、发行版策略和遗留软件需求之间的紧张关系。它还提到了Fedora使用`lockdev`用于UUCP的替代方法，并讨论了可能的迁移策略，强调了桥接新旧锁定机制的复杂性。文章最后指出，一位systemd维护者打算准备一个合并请求以遵守TC的决定。

---

## 23. 公立蒙台梭利项目以更低的成本加强学习成果：研究

**原文标题**: Public Montessori programs strengthen learning outcomes at lower costs: study

**原文链接**: [https://phys.org/news/2025-10-national-montessori-early-outcomes-sharply.html](https://phys.org/news/2025-10-national-montessori-early-outcomes-sharply.html)

弗吉尼亚大学、宾夕法尼亚大学和美国研究所的研究人员领导的一项全国性研究发现，公立蒙特梭利幼儿园（3-6岁）比传统幼儿园项目以更低的成本为儿童带来更强的早期学习成果。

这项随机对照试验追踪了全国24个公立蒙特梭利幼儿园近600名儿童，结果表明，到幼儿园结束时，蒙特梭利学生的阅读、执行功能、短期记忆和社交理解能力都优于同龄人。值得注意的是，这些益处持续存在，不像许多传统幼儿园项目那样，收益往往会消退。

该研究还揭示了显著的成本节约。与传统的公立幼儿园相比，公立蒙特梭利幼儿园在三年内（3-6岁）每个孩子的花费大约减少了13,000美元，这主要是由于更高效的班级结构和同伴教学。研究人员认为，考虑到蒙特梭利项目中观察到的教师士气和留任率的提高，成本节约可能更高。

这些益处对于来自低收入家庭的儿童尤其明显，这与玛丽亚·蒙特梭利最初为服务不足的社区提供有效教育的愿景相一致。来自美国研究所和弗吉尼亚大学的研究人员共同撰写了这篇论文，该论文已发表在《美国国家科学院院刊》上。该研究结果对寻求以有限资源改善早期学习成果的政策制定者和教育工作者具有可操作的意义。

---

## 24. 何时更适合不用言语思考？

**原文标题**: When is it better to think without words?

**原文链接**: [https://www.henrikkarlsson.xyz/p/wordless-thought](https://www.henrikkarlsson.xyz/p/wordless-thought)

亨里克·卡尔森的文章探讨了何时进行无词语思考更有优势，并将其与以结构化、口头方式思考和写作的更常见的益处进行对比。 卡尔森借鉴了雅克·阿达玛调查的数学家的经验，指出这些专家通常通过非语言手段（如振动、声音或模糊形状）而不是文字或方程式来解决复杂问题。

这篇文章深入探讨了解决问题过程中发生的潜意识处理，即大脑并行地探索大量替代方案。 卡尔森推测，专家级思考者可能会同时激活默认模式网络（走神）和执行控制网络（集中注意力），以促进这一过程。

虽然无词语思考可能更快、更广泛，但由于缺乏精确性，它也容易出错。 另一方面，写作可以迫使精确，并有助于提炼想法，使它们更完整。 然而，过早的精确也可能导致虚假的确定性。

卡尔森强调，通过阅读和写作培养的对某一主题的深刻理解，最终可以使无词语思考更有效。 最终，语言思考和非语言思考之间的关系是复杂且循环的。 写作有助于构建大脑并为潜意识提供必要的构建块，但无词语思考可以成为探索复杂问题的强大工具，尤其是对于那些具有深厚专业知识的人。 关键是要注意在思考过程中何时文字会阻碍，何时文字会有帮助。

---

## 25. 阿拉斯加航空关于IT系统中断的声明

**原文标题**: Alaska Airlines' statement on IT outage

**原文链接**: [https://news.alaskaair.com/on-the-record/alaska-statement-on-it-outage/](https://news.alaskaair.com/on-the-record/alaska-statement-on-it-outage/)

阿拉斯加航空10月23日因主数据中心故障，于太平洋时间下午3:30左右发生重大IT系统故障，导致阿拉斯加航空和地平线航空航班全系统停飞。停飞于太平洋时间晚上11:30解除。

周四全天及周五上午，此次故障导致阿拉斯加航空和地平线航空取消了超过360个航班。航空公司警告称，由于需要重新部署飞机和机组人员，可能会出现进一步中断。夏威夷航空航班未受影响。

阿拉斯加航空强调，此次IT系统故障并非网络安全事件，也与任何其他事件无关。

航空公司向旅行计划受影响的乘客致歉，并敦促他们在前往机场前查询航班状态。为了支持旅客，随着运营恢复正常，航空公司实施了灵活的旅行政策。阿拉斯加航空向客户保证，他们正在尽快、安全地恢复运营，并将乘客送达目的地。

---

## 26. LightlyStudio – 一款开源多模态数据整理和标注工具

**原文标题**: LightlyStudio – an open-source multimodal data curation and labeling tool

**原文链接**: [https://github.com/lightly-ai/lightly-studio](https://github.com/lightly-ai/lightly-studio)

LightlyStudio：多模态数据管理开源工具，用于统一数据工作流程，包括整理、标注和管理。它采用 Rust 构建，速度快，即使在资源受限的机器上也能支持 COCO 和 ImageNet 等格式。

通过 `pip install lightly-studio` 即可轻松安装，需要 Python 3.8 或更高版本。该工具提供图像文件夹、YOLO 目标检测、COCO 实例分割和 COCO 标题的快速入门示例，所有示例均可通过提供的 Python 脚本和示例数据集访问。

Python 接口功能强大，允许用户索引、查询和操作数据集。`Dataset` 对象是核心，提供各种加载选项，包括本地路径、云存储（S3、GCS）和现有 `.db` 文件。用户可以迭代 `Sample` 对象来访问和修改文件名称、路径、标签和元数据等属性。

数据集查询允许使用表达式进行过滤、排序和切片，以实现复杂的条件筛选。结果可以被标记、迭代、收集为列表或以 COCO 格式导出。

LightlyStudio 提供高级数据选择功能，可自动选择具有代表性和多样性的样本，从而节省标注成本和训练时间。它使用元数据加权和嵌入多样性等策略来实现最佳子集选择。

本文还提到了发布公告，鼓励通过问题页面进行贡献，并提供联系方式。

---

## 27. Clojure拉链 (2021)

**原文标题**: Clojure Zippers (2021)

**原文链接**: [https://grishaev.me/en/clojure-zippers/](https://grishaev.me/en/clojure-zippers/)

本文介绍了Clojure zippers，一种用于遍历和操作复杂数据结构的强大工具。Zippers提供了一种在集合中上下左右导航以及添加、编辑和删除节点的方法。它们内置于Clojure中，并利用不可变集合；每次移动都会创建一个新的“位置”，而不会修改原始数据。

本文强调，当处理未知或可变形状的数据结构时，zippers最为有用，此时诸如`get-in`之类的传统方法是不够的。一个关键函数是`zip/next`，它系统地遍历整个结构。`iterate`可用于生成一系列位置，但务必检查`zip/end?`条件以避免无限循环，因为`zip/next`在完成后会循环回到初始位置。

本文演示了使用`zip/vector-zip`进行嵌套向量的导航，说明了如何使用`zip/down`、`zip/right`和`zip/up`在结构中移动指针。它强调了理解`branch?`和`children`函数的重要性，这些函数分别定义了zipper如何识别分支节点并提取其子节点。虽然可以手动导航，但本文建议利用`zip/next`自动遍历未知数据结构。`xml-zip`（虽有提及但未详细介绍）暗示了更多的应用。

---

## 28. SierraDB: 用 Rust 构建的分布式事件存储

**原文标题**: SierraDB: A distributed event store built in Rust

**原文链接**: [https://tqwewe.com/blog/building-sierradb/](https://tqwewe.com/blog/building-sierradb/)

SierraDB：用 Rust 构建的分布式事件存储，旨在解决通用数据库在事件溯源方面的不足。其创建者 Ari Seyhun 强调了对特定保证的需求，例如仅追加存储、无间隙序列号、高效的流读取和内置订阅，这些通用数据库通常缺乏或难以高效提供。

SierraDB 的架构围绕分区、存储桶和段展开，确保水平可扩展性和可预测的性能，而无需垃圾回收暂停。它使用固定数量的逻辑分区进行顺序写入处理和单调序列号。数据以仅追加文件的形式存储在存储桶中，并划分为可管理的段。

主要功能包括：使用单调递增数字实现流版本控制、通过共享分区键实现跨流事务，以及用于复制的分布式共识机制。读取通过水印系统进行优化，确保分区视图的一致性和无间隙性。

SierraDB 利用现有技术，例如用于客户端通信的 RESP3、用于节点间通信的 libp2p 以及用于构建容错分布式系统的 Actor 框架 Kameo。它为订阅提供一流的支持，帮助创建投影和事件处理程序，并提供一个 Web 界面 SierraDB Inspector，用于浏览事件和运行投影。

该项目旨在成为一个可用于生产环境的开源事件存储，并欢迎贡献。Docker 镜像可用于轻松设置和测试。

---

## 29. /dev/null 是一个符合 ACID 标准的数据库

**原文标题**: /dev/null is an ACID compliant database

**原文链接**: [https://jyu.dev/blog/why-dev-null-is-an-acid-compliant-database/](https://jyu.dev/blog/why-dev-null-is-an-acid-compliant-database/)

这篇讽刺文章幽默地论证了`/dev/null`是一个符合ACID标准的数据库。它通过将原子性、一致性、隔离性和持久性（ACID）的定义应用于类Unix系统中`/dev/null`的行为来实现这一点。

文章声称：

*   **原子性：** 写入`/dev/null`是一个“要么全部要么全无”的操作，因为数据要么被写入并丢弃，要么根本不被写入。
*   **一致性：** 无论写入什么，`/dev/null`始终保持一个总是为空的一致状态。
*   **隔离性：** 来自多个进程的并发写入操作不会冲突，因为没有任何内容被存储。
*   **持久性：** 写入`/dev/null`的数据被“持久”地提交到虚无，即使在系统崩溃或重启后仍然保持一致。

作者承认`/dev/null`仅有0字节存储空间的限制。文章以一个半开玩笑的行动号召结束，建议联系“企业销售”（暗示是作者本人）以获取额外的存储空间。总体基调是轻松的，旨在通过将数据库的严格要求与丢弃所有输入的行为并列来达到幽默的效果。

---

## 30. 人工智能设计的文艺复兴在哪里？

**原文标题**: Where's the AI design Renaissance?

**原文链接**: [https://www.learnui.design/blog/wheres-the-ai-design-renaissance.html](https://www.learnui.design/blog/wheres-the-ai-design-renaissance.html)

在其题为《人工智能设计复兴在哪里？》的文章中，埃里克·D·肯尼迪探讨了截至2025年末人工智能对设计行业的影响。他质疑了人工智能已彻底革新设计的普遍观点，并指出缺乏证据表明设计师的生产力显著提高或失业率上升。肯尼迪认为，人工智能目前的能力被过度炒作，尚未带来真正的“软件复兴”。

一个中心论点是，有效的设计依赖于更广泛的过程，使得与人工智能设计工具的一次性互动不足以创造真正伟大的设计，尤其对于非设计师而言。他将此比作客户经常要求对设计进行表面更改，却不了解其基本原理。

肯尼迪进一步解释说，大型语言模型（LLM）基于预测运行，使其难以处理新颖、大胆或严重偏离其训练数据的设计。他建议设计师专注于人工智能固有局限的领域：复杂性、跨学科工作和独特概念。

他确定了人工智能确实显示出前景的具体用例，例如用于图像处理、内容创建（图像、视频、音频）以及启动小型应用程序或工具的特定任务工具，尤其对于那些具备一定编码知识的人。他认为人工智能对于个人项目、内部原型设计和小型公共项目最为有效，并概述了每种情况的潜在缺点和注意事项。最终，肯尼迪强调，设计师应利用人工智能执行特定任务，同时专注于人工智能难以复制的更高层次的战略和创造性设计方面。

---

## 31. 扑克诈骗案用X光赌桌、高科技眼镜和NBA球员

**原文标题**: Poker fraud used X-ray tables, high-tech glasses and NBA players

**原文链接**: [https://www.bbc.com/news/articles/cz6nd9wnzn6o](https://www.bbc.com/news/articles/cz6nd9wnzn6o)

一起由黑手党成员策划的广泛扑克诈骗案被曝光，导致超过30人被捕，其中包括前NBA球员达蒙·琼斯和波特兰开拓者队教练昌西·比卢普斯。检察官称，该团伙在美国多个城市的非法地下德州扑克游戏中诈骗受害者至少700万美元。

该骗局涉及精密的科技手段，包括X光牌桌、作弊的洗牌机、藏在桌子和灯具中的摄像头，以及用特制眼镜或隐形眼镜可识别的预先标记的牌。这些工具使得同谋者能够看到对手的牌并操纵游戏，以确保受害者输钱。信息被传递给场外的“操作员”，然后操作员再传递给牌桌上的“四分卫”，后者向其他参与骗局的玩家发出信号。

前职业运动员，被描述为“人头牌”，被用来引诱富有的个人（“肥鱼”）参与游戏，承诺与名人一起玩的机会。起诉书显示，甚至连筹码托盘和洗牌机都被动了手脚。据称，同谋者通过加密货币、现金交易和空壳公司来洗白非法所得，部分利润用于资助黑手党的犯罪活动。一些同谋者甚至会故意输掉牌局，以让受害者在牌桌上停留更长时间。

---

## 32. Show HN: 一款快速、注重隐私且在浏览器中运行的图像转换器

**原文标题**: Show HN: A fast, privacy-first image converter that runs in browser

**原文链接**: [https://imageconverter.dev/](https://imageconverter.dev/)

这个"Show HN"帖子介绍`imageconverter.dev`，一个免费、注重隐私且快速的图像转换器，完全在浏览器内运行。它支持JPEG、JPG、PNG和WebP格式之间的转换，最大文件大小为50MB。

其主要卖点是速度（闪电般的转换速度）、隐私（无需服务器上传，一切都在本地进行）和易用性（免费、无限制且无水印）。用户只需拖放或选择图片即可立即转换。该转换器保持图像质量和尺寸，仅在必要时进行压缩。对于JPG转换，透明背景将被压平为白色。

该帖子包含一个关于如何将PNG转换为JPG的分步指南。它还提供了一个简短的FAQ，解答关于成本、数据隐私、图像质量和批量转换功能的疑问，并引导用户使用他们的批量调整工具进行具有格式切换支持的批量转换。总的来说，它被展示为服务器端图像转换服务的一个便捷且安全的替代方案。

---

## 33. 克劳德记忆

**原文标题**: Claude Memory

**原文链接**: [https://www.anthropic.com/news/memory](https://www.anthropic.com/news/memory)

本文介绍了Claude的“记忆”功能，该功能使AI助手能够记住用户偏好、项目详情和团队流程，从而提高生产力。该功能最初面向团队版和企业版用户推出，现已扩展到Pro和Max用户（2025年10月23日）。“记忆”旨在最大程度地减少重复性上下文解释的需求，从而在专业环境中实现更高效的工作流程。

主要功能包括：

*   **项目范围记忆：**为每个项目单独设置记忆，保持细节井井有条，并包含机密讨论。
*   **用户控制：**用户可以随时查看、编辑和更新Claude的记忆摘要，决定它关注或忽略的内容。
*   **隐身聊天：**为敏感的头脑风暴或用户不希望保存到记忆中的机密讨论提供了一个干净的环境。
*   **安全措施：**进行了广泛的安全测试，以防止有害模式并确保负责任的使用。

“记忆”是可选的，可以在“设置”中启用。要开始使用，用户可以允许Claude从过去的聊天记录中生成记忆。该功能专为工作环境而设计，避免涉及敏感话题。公司正在采取分阶段的方法，以确保负责任的部署，并将继续评估和测试“记忆”在人们使用Claude的不同方式中的工作方式，然后再扩大可用性。

---

## 34. 展示HN：MacOS动态屏保 – 播放实时视频流的屏保

**原文标题**: Show HN: MacOS Live Screensaver – A screensaver that plays live video streams

**原文链接**: [https://github.com/hauxir/macos-live-screensaver](https://github.com/hauxir/macos-live-screensaver)

此“Show HN”帖子介绍MacOS Live Screensaver，一款播放实时视频流的屏幕保护程序应用。它支持YouTube直播流和直接HLS流，允许用户将实时内容转换为屏幕保护程序。

主要功能包括：

*   **直播流支持：** 播放YouTube（仅限直播）和HLS流。
*   **安装：** 使用`make`命令或手动步骤进行简单安装。需要Xcode Command Line Tools，可选`yt-dlp`以支持YouTube。
*   **使用：** 通过系统偏好设置 -> 屏幕保护程序进行配置，用户可以在其中输入视频URL。
*   **局限性：** 专门为在M2 MacBook上的macOS Tahoe（可能是Ventura）设计和测试，因此与其他版本和硬件的兼容性可能有所不同。仅支持YouTube直播视频，不支持普通视频。
*   **故障排除：** 提供常见问题的指导，例如YouTube视频无法播放（需要`yt-dlp`和直播流URL）以及黑屏（建议等待或尝试其他URL）。
*   **Vibe-Coded：** 作者公开声明缺乏Swift经验，并欢迎贡献，特别是解决UI错误。

---

## 35. 常春藤心理学家： “将完整的自我带到工作中” 是个糟糕的建议

**原文标题**: Ivy League psychologist: 'Bring your whole self to work' is bad advice

**原文链接**: [https://www.cnbc.com/2025/10/24/bring-your-whole-self-to-work-is-bad-advice-ivy-league-psychologist-saysheres-why.html](https://www.cnbc.com/2025/10/24/bring-your-whole-self-to-work-is-bad-advice-ivy-league-psychologist-saysheres-why.html)

常春藤心理学家托马斯·查莫罗-普雷穆齐克认为，广受欢迎的“将完整的自我带到工作中”的建议往往是误导性的。 虽然其意图是积极的，旨在鼓励包容和自我表达，但在实践中是不切实际且可能有害的。

查莫罗-普雷穆齐克认为，工作场所主要重视专业的举止，而不是个人的怪癖。 认真对待这个建议可能会导致尴尬的社交场合，甚至损害一个人的职业生涯。 真实性在理论上经常受到赞扬，但顺从通常会得到奖励。 表达与公司文化冲突的观点会损害声誉。

他强调，缺乏工作场所礼仪知识的年轻专业人士尤其容易受到伤害。 在求职面试等情况下，展现自己未经修饰的真实一面是一种劣势。

此外，查莫罗-普雷穆齐克认为，每个人的“完整自我”都包括不太受欢迎的行为。 鼓励毫无约束的真实性会助长不良行为，尤其是来自当权者的不良行为，因为问责制会减弱。 他建议将重点从真实性转移到促进尊重行为，以营造更积极的工作环境。

---

## 36. 交通灯协议

**原文标题**: Traffic Light Protocol

**原文链接**: [https://www.first.org/tlp/](https://www.first.org/tlp/)

交通灯协议（TLP）是由FIRST创建的一个标准化系统，旨在通过指定明确的共享边界来促进信息共享。截至2022年8月，当前标准版本2.0使用四个标签：TLP:RED、TLP:AMBER、TLP:GREEN和TLP:CLEAR，每个标签都指示信息传播的允许范围。

TLP不是正式的分类方案，也不是许可协议的替代品，而是一个简单直观的模式。信息的来源负责确保接收者理解并遵守TLP指南。接收者在超出指定TLP标签范围共享信息之前，必须获得来源的明确许可。

该文档详细说明了如何在各种媒介中使用TLP，包括消息传递（电子邮件主题行）、文档（带有特定字号的页眉/页脚）和自动化信息交换（由设计者决定）。它还为每个TLP级别指定了颜色编码指南（RGB、CMYK和Hex），以提高可访问性，特别是对于低视力人士。

该文档在TLP上下文中定义了“社区”、“组织”和“客户”，以进一步明确如何应用标签。具体而言，每个标签都定义了一个披露级别，从仅限个人接收者（RED）到无限制披露（CLEAR），中间有各种规定。FIRST通过TLP特别兴趣小组（TLP-SIG）管理该标准，并提供多种语言版本。

---

## 37. Rust 传染性借用问题

**原文标题**: Rust Contagious Borrow Issue

**原文链接**: [https://qouteall.fun/qouteall-blog/2025/How%20to%20Avoid%20Fighting%20Rust%20Borrow%20Checker#contagious-borrow-issue](https://qouteall.fun/qouteall-blog/2025/How%20to%20Avoid%20Fighting%20Rust%20Borrow%20Checker#contagious-borrow-issue)

本文深入探讨Rust中的“传染性借用”问题，这是一个源于Rust所有权和借用规则的常见难题。 核心问题在于，当你借用一个子对象时，你会间接地借用它的父对象（以此类推），这可能会阻止其他的借用，即使它们实际上不会导致内存安全问题。 这是因为借用检查器在函数签名上进行局部工作，从而丢失了函数体内的细粒度借用信息。

本文探讨了针对此问题的各种解决方法，包括：

*   **面向数据设计：** 避免不必要的getter和setter，以实现分割借用。
*   **分割借用：** 在同一作用域内分别借用各个字段。
*   **ID/句柄和Arena：** 使用ID替换借用，以访问arena中的数据。
*   **延迟突变：** 将突变转化为稍后执行的命令，以避免同时发生可变和不可变借用。
*   **避免就地突变：** 使用不可变数据和重新创建突变的策略，通常使用持久性数据结构。
*   **手动索引管理：** 使用索引而不是迭代器来遍历容器。
*   **克隆数据：** 克隆数据以释放借用。

对于循环引用，本文建议使用带有arena的ID/句柄，或采用诸如事件总线或 `Arc<QCell<T>>` 之类的技术。 本文强调存在许多解决方案，最佳方法取决于具体情况。 它还涉及延迟突变的好处，突出了其在序列化、调试、并行化以及在事务数据库和事件溯源等领域的应用潜力。

---

## 38. 贝蒂·怀特的肩包是二战时期的时光胶囊 (2023)

**原文标题**: Betty White's shoulder bag is a time capsule of World War II (2023)

**原文链接**: [https://americanhistory.si.edu/explore/stories/betty-white-world-war-ii](https://americanhistory.si.edu/explore/stories/betty-white-world-war-ii)

无法访问文章链接。

---

## 39. JupyterGIS 突破至新境界

**原文标题**: JupyterGIS breaks through to the next level

**原文链接**: [https://eo4society.esa.int/2025/10/16/jupytergis-breaks-through-to-the-next-level/](https://eo4society.esa.int/2025/10/16/jupytergis-breaks-through-to-the-next-level/)

JupyterGIS：协作式Web GIS环境的最新进展

JupyterGIS是一个基于JupyterLab构建的协作式Web GIS环境，自2024年6月首次发布以来取得了显著进展。该平台在社区贡献和合作伙伴支持的推动下，现已拥有增强的分析、可视化和协作功能。

主要改进包括：通过pmtiles支持增强了矢量瓦片功能；新增了识别工具和符号系统面板。一个基于浏览器的全新处理工具箱，由GDAL的WebAssembly (WASM)构建提供支持，提供缓冲、凸包、溶解、边界框、质心和凹包工具。符号系统增强功能提供了更灵活的可视化选项，包括Viridis作为默认颜色映射、GeoTIFF的多波段符号系统，以及点图层颜色和标记大小的独立样式设置。

与时空资产目录 (STAC) 的集成简化了数据访问，允许用户直接在Jupyter Notebook中搜索和集成卫星图像。对GeoParquet和PMTiles的支持扩展了支持的数据格式范围。

用户体验改进包括集成的控制面板、改进的工具栏、位置居中、地图标注链接和全屏模式。矢量图层的自动图例生成确保了一致的解释。JupyterGIS-tiler扩展允许从xarray变量创建图层。

未来的开发计划包括扩展基于GDAL的工具箱、更深入的QGIS集成、更丰富的Python API，以及故事地图编辑器/查看器。鼓励用户通过文档、GeoJupyter Zulip频道、黑客松和开发存储库的贡献参与其中。

---

## 40. Postgres 17 与 18 基准测试

**原文标题**: Benchmarking Postgres 17 vs. 18

**原文链接**: [https://planetscale.com/blog/benchmarking-postgres-17-vs-18](https://planetscale.com/blog/benchmarking-postgres-17-vs-18)

本文对比了 Postgres 17 和新发布的 Postgres 18 的性能，重点关注 Postgres 18 中新增的 `io_method` 配置选项对磁盘 I/O 处理的影响。该选项包括 `sync`（与 Postgres 17 相同）、`worker`（新的默认选项，使用后台工作进程）和 `io_uring`（使用 Linux `io_uring` 接口的异步 I/O）。

该基准测试使用 `sysbench`，采用 `oltp_read_only` 工作负载，改变连接数（1、10、50）和 `range_size`（100、10000）来影响点查询与范围扫描的比例。数据库大小约为 300GB。基准测试在四种 EC2 实例配置上进行：三种使用 EBS 存储（gp3 3k IOPS、gp3 10k IOPS、io2 16k IOPS），一种使用本地 NVMe 存储。

主要发现：

*   由于更低的延迟和更高的 IOPS，本地 NVMe 存储始终优于 EBS 存储。
*   对于单连接工作负载，Postgres 18 的 `sync` 和 `worker` 选项通常优于 Postgres 17 和 Postgres 18 的 `io_uring` 选项（在使用网络连接存储时）。
*   在高并发（50 个连接）的情况下，IOPS 和吞吐量成为 EBS 支持实例的主要瓶颈。Postgres 18 的 `sync` 和 `worker` 选项表现出略微更好的性能。`io_uring` 在 CPU 密集型场景下表现最佳。
*   `io_uring` 在高 I/O 并发下表现最佳，但在低并发场景下收益较小。
*   具有本地 NVMe 存储的服务器提供了最佳的性价比。
*   `worker` I/O 方法是默认设置的良好选择。

---

## 41. 基于Rust的coreutils中的日期错误影响Ubuntu 25.10自动更新

**原文标题**: Date bug in Rust-based coreutils affects Ubuntu 25.10 automatic updates

**原文链接**: [https://lwn.net/Articles/1043103/](https://lwn.net/Articles/1043103/)

LWN.net文章报道了Ubuntu 25.10的`uutils` coreutils包中基于Rust的`date`命令存在一个漏洞，该漏洞导致自动更新失效。该漏洞存在于0.2.2-0ubuntu2及更早版本中，阻止了系统检查可用的软件更新，影响了云部署、容器镜像以及桌面和服务器安装。通过`apt`手动更新不受影响。0.2.2-0ubuntu2.1及更高版本已修复该问题。

该事件引发了关于Ubuntu“氧化”项目的讨论，该项目旨在用基于Rust的替代品（如`uutils`和`sudo-rs`）取代传统的C语言实用程序。评论员讨论了C语言实用程序的已被验证的稳定性与使用Rust的潜在长期优势（包括更合理的构建系统和可能更少的安全漏洞）之间的权衡。人们对`uutils`的MIT许可证（与GPL相比）、Rust实现的性能开销以及过早采用这些未经测试的实用程序表示担忧。一些人认为，用Rust重写经过实战检验的C语言实用程序会引入新的错误，而改进现有的C语言版本会是更好的方法。讨论还涉及管理大型多调用二进制文件和确保正确的程序调用的挑战。

---

## 42. 文明的冲突

**原文标题**: The Coming Clash of Civilizations

**原文链接**: [https://www.notesfromthecircus.com/p/the-coming-clash-of-civilizations](https://www.notesfromthecircus.com/p/the-coming-clash-of-civilizations)

前科技中心主义者迈克·布洛克认为，社会正走向文明的冲突，但并非文化之间的冲突，而是社会组织不兼容的愿景之间的冲突：民主与新封建等级制度。在观察到新反动思想的兴起后，他描述了自己对当前体系的幻灭，这些思想主张回归明确的等级制度并拒绝民主治理。

布洛克指出，年轻人尽管满足了社会期望，但所经历的不稳定和缺乏机会是制度崩溃的症状。他认为，民粹主义左派和新反动右派都认识到这种崩溃，但提出了相反的解决方案。左派呼吁重振民主承诺，即为所有人提供机会和繁荣，而右派则主张由“少数智者”统治的等级制度，认为民主是一项失败的实验。

布洛克强调，危险在于导致封建结果的框架的常态化，即使在其中运作的个人认为他们的行为是理性的。他批评依赖国内生产总值和失业率等指标，这些指标在掩盖普遍的不稳定和人类繁荣的下降时可能显得积极。他认为，通过允许专家在技术优化的伪装下做出价值判断，民主内容已从治理中撤出，从而为威权民粹主义者创造了填补真空的机会。他总结说，专业知识应该为民主选择提供信息，而不是取代它。

---

## 43. “第二生命”电动汽车电池能用作电网级储能吗？

**原文标题**: Can “second life” EV batteries work as grid-scale energy storage?

**原文链接**: [https://www.volts.wtf/p/can-second-life-ev-batteries-work](https://www.volts.wtf/p/can-second-life-ev-batteries-work)

Volts播客：David Roberts采访红木材料首席技术官Colin Campbell，探讨Redwood Energy，该新部门专注于将废旧电动汽车电池改造为电网级储能。红木公司已是电动汽车电池回收领域的领头羊，如今致力于在回收前最大限度地挖掘电池价值。

其关键创新在于红木公司的“通用转换器”，这是一种电力电子系统和软件，可以管理各种化学成分、电压和健康状态不同的电动汽车电池的混合。该系统允许红木公司在不拆卸的情况下连接来自不同制造商和型号的电池，从而使该过程在经济上可行。

Campbell强调，电动汽车电池坚固耐用，非常适合要求较低的电网存储环境。 经过快速评估后，大多数（超过90%）的来料电池都被认为“足够好”可用于二次利用。 从这种二次利用应用中获得的价值可能等于或大于通过回收获得的原材料的价值，从而有可能使整体价值翻倍。

红木公司已经部署了一个63兆瓦时的二次利用电池储能系统来为数据中心供电，证明了该概念在大规模应用中的可行性。 该系统被设计为模块化和可扩展的，尽管红木公司目前专注于大规模部署。 该公司已经控制了美国锂离子电池回收市场的大部分份额（70-80%），为其二次利用储能业务提供了强大的供应链。

---

## 44. "Return YouTube Dislike" Chrome 扩展注入广告

**原文标题**: Return YouTube Dislike" Chrome Extension Injecting Ads

**原文链接**: [https://chromewebstore.google.com/detail/return-youtube-dislike/gebbhagfogifgggkldgodflihgfeippi/reviews](https://chromewebstore.google.com/detail/return-youtube-dislike/gebbhagfogifgggkldgodflihgfeippi/reviews)

本文介绍了针对Chrome浏览器扩展程序“Return YouTube Dislike”的负面用户评价，主要集中于近期新增的侵入式广告和存在问题的行为。用户主要关注的问题包括：

*   **广告注入：** 许多用户报告称该扩展程序现在会注入广告，其中一些广告占据了大量的屏幕空间，本质上是强迫用户付费购买高级版本才能移除它们。
*   **不需要的功能：** 一些用户觉得“估计的踩数”功能不必要且难以禁用，更希望显示实际的踩数。
*   **功能问题：** 一位用户报告称该扩展程序导致YouTube无法加载，需要禁用该插件。其他用户报告称该扩展程序在正确返回踩数方面可能存在问题。
*   **负面情绪：** 总体基调是压倒性的负面，用户对这些变化表达了沮丧、愤怒和失望，导致卸载和严厉的评论。

较早的评价（在广告实施之前）更为积极，称赞了该扩展程序显示踩数的核心功能。然而，最近的变化似乎严重影响了用户体验，导致了负面反馈。

---

## 45. OpenAI 收购 Sky.app

**原文标题**: OpenAI acquires Sky.app

**原文链接**: [https://openai.com/index/openai-acquires-software-applications-incorporated](https://openai.com/index/openai-acquires-software-applications-incorporated)

OpenAI收购Sky.app开发商Software Applications Incorporated。公告简短且缺乏细节，但强调了OpenAI持续致力于推进其技术和扩展其能力。

此次收购似乎具有战略意义，旨在增强OpenAI现有产品并可能将Sky.app的技术整合到其未来产品中。然而，公告中并未明确说明Sky.app技术的具体性质以及OpenAI将如何利用它。

此次收购被视为两家公司向前迈出的一步，表明Sky.app团队有望获得OpenAI的资源和专业知识，而Sky.app的人才和技术将被整合以进一步推进OpenAI的使命。

本质上，OpenAI收购了Sky.app，可能为了加强自身在人工智能领域的进展，但关于收购技术的具体用途细节目前尚未披露。

---

## 46. Go语言中内存映射 (mmap) 如何实现更快的文件访问

**原文标题**: How memory maps (mmap) deliver faster file access in Go

**原文链接**: [https://info.varnish-software.com/blog/how-memory-maps-mmap-deliver-25x-faster-file-access-in-go](https://info.varnish-software.com/blog/how-memory-maps-mmap-deliver-25x-faster-file-access-in-go)

本文探讨了在Go语言中使用内存映射（mmap）进行文件I/O，特别是读取操作时的性能优势。 Mmap允许将文件直接映射到虚拟内存中，与传统的`ReaderAt`（seek/read）方法相比，可以更快地访问数据。 基准测试表明，速度有显著提高，mmap在随机查找和迭代方面实现了显著更低的延迟。

然而，本文强调了写入内存映射的缺点。 当由于写入未映射的页面而发生页面错误时，操作系统必须分配内存、读取文件内容，然后允许应用程序写入，这使得该过程非常低效。 基准测试表明，`WriterAt`通常更可预测，并且在写入方面表现更好，尤其是在内存页尚未缓存的情况下。

作者使用构建HTTP支持的文件系统的真实示例来说明性能提升。 通过用mmap替换`ReaderAt`进行数据库查找，作者实现了25倍的性能提升。 作者指出，虽然Varnish Cache最初使用mmap进行写入，但由于通过内存映射写入的效率低下，后来过渡到`malloc`和`io_uring`。 总之，mmap是提高Go语言读取性能的强大工具，但应谨慎对待写入操作，并应考虑诸如`WriterAt`之类的替代方法。

---

## 47. Fast-DLLM：扩散LLM的免训练加速

**原文标题**: Fast-DLLM: Training-Free Acceleration of Diffusion LLM

**原文链接**: [https://arxiv.org/abs/2505.22618](https://arxiv.org/abs/2505.22618)

这篇arXiv文章《Fast-dLLM：通过启用KV缓存和并行解码实现Diffusion LLM的免训练加速》，旨在解决扩散大型语言模型(Diffusion LLM)相比于自回归模型推理速度缓慢的问题。作者吴承岳等人提出了两项关键创新，在*无需重新训练*的情况下显著提高Diffusion LLM的性能。

首先，他们提出了一种专门为双向扩散模型设计的**块状近似Key-Value (KV)缓存**机制。这使得可以重用先前计算的键和值向量，从而在推理过程中大幅减少冗余计算，并且性能损失极小。

其次，他们解决了Diffusion LLM并行解码过程中常见的生成质量下降问题。作者认为条件独立性假设下token依赖关系的破坏是罪魁祸首。为了缓解这个问题，他们引入了一种**置信度感知并行解码策略**。该策略有选择性地解码那些超过特定置信度阈值的token，从而防止高度依赖的token同时解码，并保持生成质量。

在LLaDA和Dream模型上的实验结果证明了该方法的有效性。Fast-dLLM在多个LLM基准测试中实现了高达**27.6倍的吞吐量提升**，而精度损失可忽略不计，有效地弥合了Diffusion LLM和自回归模型之间的性能差距。这为Diffusion LLM的实际部署铺平了道路，使其速度更快、效率更高。

---

## 48. 自动化算法发现：MoE负载均衡案例研究

**原文标题**: Automating Algorithm Discovery: A Case Study in MoE Load Balancing

**原文链接**: [https://adrs-ucb.notion.site/moe-load-balancing](https://adrs-ucb.notion.site/moe-load-balancing)

本文介绍了一个关于自动发现算法的案例研究，特别关注于混合专家（MoE）模型中的负载均衡。其核心思想是利用自动化机器学习技术，可能是强化学习或其他优化方法，来发现相比传统手工设计的负载均衡策略而言，更新颖、更高效的策略。

作者很可能会强调现有MoE负载均衡算法的局限性，例如专家利用率不均、路由不稳定以及计算开销过高等问题。通过自动化算法发现过程，他们旨在克服这些局限性，并找到为特定MoE架构和数据集量身定制的算法。

文章可能详细介绍用于自动化算法发现的方法论。这可能包括定义可能的算法搜索空间，指定量化负载均衡性能的奖励函数（例如，专家利用率、延迟、准确性），以及选择合适的优化算法来导航搜索空间。

结果很可能会展示自动发现的负载均衡算法与基线方法相比的性能。关键指标可能包括改善的专家利用率、降低的路由延迟和整体模型准确性。作者可能还会讨论发现的算法在不同MoE设置中的泛化能力。

最后，文章可能会涉及自动化算法发现的更广泛意义，表明其在加速机器学习其他领域（超出MoE负载均衡）的研发方面的潜力。

---

## 49. Clang字节码解释器更新

**原文标题**: Clang Bytecode Interpreter Update

**原文链接**: [https://developers.redhat.com/articles/2025/10/15/clang-bytecode-interpreter-update](https://developers.redhat.com/articles/2025/10/15/clang-bytecode-interpreter-update)

无法访问文章链接。

---

## 50. 与克劳德共历险境

**原文标题**: Living Dangerously with Claude

**原文链接**: [https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/](https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/)

在对Claude Code爱好者的演讲中，作者探讨了以“YOLO模式”（使用`--dangerously-skip-permissions`标志）运行代码代理的益处和风险之间的张力。YOLO模式允许无监督的问题解决，提高了生产力，正如作者在48小时内完成三个副项目所展示的那样，包括使DeepSeek-OCR在NVIDIA Spark上运行，创建一个服务器端Python WebAssembly演示，以及构建一个基于浏览器的SLOCCount工具。

然而，作者强调了YOLO模式的危险性，因为它容易受到提示注入攻击，恶意行为者可以通过不受信任的内容操纵代理并控制代理的行为，从而可能导致私人数据的泄露（“致命的三重奏”：私人数据访问+不受信任的内容+外部通信）。他们认为，基于人工智能的解决方案来检测这些攻击是不可靠的。

作者提倡沙盒化，认为它是对抗提示注入最可靠的防御手段。他们建议使用在他人计算机上运行的沙盒（例如，OpenAI Codex Cloud，Claude Code for the web），或者控制文件系统访问，最重要的是控制网络连接。文章指出Anthropic在Claude Code CLI中使用Apple的sandbox-exec命令来实现新的沙盒功能，通过具有允许域名的HTTP代理来限制网络访问，但也指出Apple已经弃用了该命令。 结论是要拥抱代码代理的力量，但始终要在安全沙盒中进行，以减轻风险。

---

## 51. 美国调查Waymo自动驾驶出租车，因其对校车安全构成威胁

**原文标题**: US probes Waymo robotaxis over school bus safety

**原文链接**: [https://www.yahoo.com/news/articles/us-investigates-waymo-robotaxis-over-102015308.html](https://www.yahoo.com/news/articles/us-investigates-waymo-robotaxis-over-102015308.html)

美国国家公路交通安全管理局（NHTSA）已对约2000辆Waymo自动驾驶汽车展开初步调查。此次调查源于有报告称Waymo无人驾驶出租车可能未遵守有关停靠校车的交通安全法规。具体而言，令人担忧的是，Waymo车辆在接近闪烁红灯并伸出停车臂的校车时，未能保持静止。

一份媒体报道重点介绍了佐治亚州发生的一起事件，其中一辆Waymo车辆最初停了下来，但随后绕过一辆校车，在学生下车时驶过停车臂。NHTSA认为，鉴于Waymo庞大的运营里程，可能发生了类似事件。

Waymo承认了这个问题，并表示他们已经对校车停车问题进行了改进，并将发布进一步的软件更新。该公司强调了在儿童周围安全驾驶的重要性，并表示佐治亚州报告的事件中，车辆从一个灯光和停车标志不可见的角度接近了校车。

此前，NHTSA曾对Waymo车辆进行过为期14个月的调查，并在两次召回后于7月结束。该调查主要集中在与可见物体的轻微碰撞以及可能违反交通安全法规的意外驾驶行为。Waymo的无人驾驶出租车队包括在美国主要城市运营的1500多辆汽车。

---

## 52. 应该开设但尚未开设的计算机科学课程 (2015)

**原文标题**: Computer science courses that don't exist, but should (2015)

**原文链接**: [https://prog21.dadgum.com/210.html](https://prog21.dadgum.com/210.html)

詹姆斯·海格，一位正在恢复的程序员，提出了几门他认为目前缺乏但对现代程序员极具价值的计算机科学课程。他强调了有效实现想法的重要性，而非仅仅为了技术本身而追求技术。

他提出的课程包括：

*   **反思面向对象编程：** 一门专注于理解和运用面向对象范式之外的编程概念的课程，强调独立于对象层次结构之外的函数和变量。
*   **经典软件研究：** 探索具有历史意义的软件，如VisiCalc和Zork，分析硬件约束下的用户界面设计和创造力。
*   **在慢速语言中编写快速代码：** 一门旨在优化Python等解释型语言的性能的课程，以实现与C++相当的速度，同时可能降低脆弱性。
*   **命令行工具的用户体验：** 一门专门应用于命令行程序的用户体验原则的课程，侧重于输出相关性、可读性以及最大程度地减少不必要的复杂性。
*   **程序员思维的痴迷：** 一门分析常见的程序员固执点（如代码格式、分类法和类型系统）以及对不熟悉系统的下意识反应的课程。

海格的建议强调了需要更广泛、更实用、更具历史意义的计算机科学教育，以超越传统的算法和理论重点。他还讨论了编程中创造力和组织能力的重要性。

---

## 53. React Flow，基于 React 或 Svelte 的节点式 UI 开源库

**原文标题**: React Flow, open source libraries for node-based UIs with React or Svelte

**原文链接**: [https://github.com/xyflow/xyflow](https://github.com/xyflow/xyflow)

React Flow 和 Svelte Flow 是强大的开源库，旨在用 React 或 Svelte 构建基于节点的用户界面。`xyflow` 仓库包含核心包：React Flow（版本 11 和 12）、Svelte Flow 和一个共享的辅助库。

这些库在 MIT 许可下可免费用于个人项目，作者鼓励提交错误报告、项目截图和 GitHub Star 作为支持。鼓励商业用户通过 React Flow Pro 或 GitHub Sponsors 进行经济贡献，以确保持续的开发和维护。

入门需要安装相关的包（`@xyflow/react` 或 `@xyflow/svelte`）并将其集成到您的 React 或 Svelte 项目中。文档提供了基本的使用示例，展示了节点和边的创建和管理，以及 MiniMap、Controls 和 Background 等基本 UI 组件。

版本发布使用 Changesets 和专门的 GitHub action 进行管理。这些库由 xyflow 团队维护，他们通过联系表单和 Discord 服务器提供支持和协作机会。

---

## 54. 似然概念及其应用简介 (2018)

**原文标题**: Introduction to the concept of likelihood and its applications (2018)

**原文链接**: [https://journals.sagepub.com/doi/10.1177/2515245917744314](https://journals.sagepub.com/doi/10.1177/2515245917744314)

无法访问文章链接。

---

## 55. 特朗普赦免了被判刑的币安创始人

**原文标题**: Trump pardons convicted Binance founder

**原文链接**: [https://www.wsj.com/finance/currencies/trump-pardons-convicted-binance-founder-7509bd63](https://www.wsj.com/finance/currencies/trump-pardons-convicted-binance-founder-7509bd63)

无法访问文章链接。

---

## 56. 算法如何推高价格的博弈论

**原文标题**: The game theory of how algorithms can drive up prices

**原文链接**: [https://www.quantamagazine.org/the-game-theory-of-how-algorithms-can-drive-up-prices-20251022/](https://www.quantamagazine.org/the-game-theory-of-how-algorithms-can-drive-up-prices-20251022/)

本文探讨了定价算法，即使是简单的算法，如何在没有明确共谋的情况下导致消费者面临更高的价格。它挑战了禁止“幕后交易”的传统法律方法，因为算法可以通过学习报复降价来默契共谋，从而有效地建立价格战的威慑。

一个关键发现是，即使是旨在避免后悔的算法（事后来看本可以产生更好结果的策略），特别是“无交换后悔”算法，仍然可能导致高价格。这种情况发生在与采用固定、高概率定价策略的“无反应”算法对抗时，有效地诱导避免后悔的算法采取更高的价格。即使从表面上看价格是合理的，也会发生这种情况。文章强调，精确的概率并不重要，只要最终结果是待售商品的价格更高即可。

本文讨论了这些发现对监管机构的影响，监管机构可能会发现，在没有明确共谋证据的情况下，很难识别和解决算法定价问题。一些研究人员建议禁止除无交换后悔算法之外的所有算法，而另一些研究人员则认为，非共谋情景仍然可能导致不公平的定价。这项工作最终强调了算法定价的复杂性，以及需要进一步研究以了解和规范其对消费者的影响。

---

## 57. Antislop：一种消除语言模型中重复模式的框架

**原文标题**: Antislop: A framework for eliminating repetitive patterns in language models

**原文链接**: [https://arxiv.org/abs/2510.15061](https://arxiv.org/abs/2510.15061)

这篇题为“Antislop：用于识别和消除语言模型中重复模式的综合框架”的arXiv文章，介绍了一种旨在解决大型语言模型（LLM）输出中重复用语（“slop”）问题的新型框架。该论文由Samuel Paech等人撰写，提出了一种三管齐下的方法：

1. **Antislop采样器：**一种基于回溯的采样方法，可在不影响词汇量的情况下，在推理过程中抑制不需要的字符串。该采样器在保持输出质量的同时，成功抑制了8000多种模式。

2. **自动化管道：**一种自动化系统，用于针对人类生成的文本对模型特定的slop进行分析，从而创建用于减少slop的训练数据。

3. **最终Token偏好优化（FTPO）：**一种微调技术，当在推理轨迹中检测到被禁止的模式时，选择性地调整单个token的logits。FTPO实现了显著的90% slop减少，甚至提高了跨领域评估中的性能，如GSM8K和创意写作任务。

作者发现，与人类写作相比，某些slop模式在LLM输出中出现的频率高出1000倍以上。在减少slop方面，FTPO优于直接偏好优化（DPO），并保持了更好的写作质量和词汇多样性。代码和结果已在MIT许可下发布。该论文强调了解决“slop”问题以提高人工智能生成文本的质量和可识别性的重要性。

---

## 58. Lodash 的未来

**原文标题**: The Future of Lodash

**原文链接**: [https://blog.ulisesgascon.com/the-future-of-lodash](https://blog.ulisesgascon.com/the-future-of-lodash)

本文宣告 Lodash 的全新、协作、可持续的未来。尽管 JavaScript 不断发展，但 Lodash 仍然是数百万网站和项目的重要依赖，每周下载量达数十亿次。 鉴于维护如此流行的库对个人（John-David Dalton）而言充满挑战，该计划的重点是：

*   **简化维护：** 过渡到技术指导委员会（TSC）进行共享治理，并弃用较少使用的变体以整合工作。
*   **提高安全性：** 实施安全报告的共享分类流程，采用威胁模型，正式使用 OpenJS 基金会的 CNA 进行事件处理，改进报告渠道，并制定事件响应计划（IRP）。
*   **提供清晰的未来：** 计划在现有接口下使用原生 JavaScript 函数对库进行渐进式重写，仅限于现代环境，确保性能优势且不破坏兼容性。

本文强调了从 Express 框架复兴中汲取的经验教训，强调了活跃的社区、明确的治理和财政支持的必要性。 它承认，即使有 Alpha Omega 和 Sovereign Tech Agency 等举措，开源的可持续性仍然是一个挑战，并倡导为开源项目提供更多资金作为公共产品。 作者寻求赞助商以帮助维护 Lodash，并鼓励开发者、公司和任何关心自由软件未来的人参与其中。

---

## 59. Kaitai Struct：声明式二进制格式解析语言

**原文标题**: Kaitai Struct: declarative binary format parsing language

**原文链接**: [https://kaitai.io/](https://kaitai.io/)

Kaitai Struct 是一种声明式语言和工具集，用于解析二进制数据格式，如文件格式和网络数据包。它允许用户在 `.ksy` 文件中描述二进制数据的结构，然后可以将其编译成各种编程语言（包括 C++、C#、Go、Java、JavaScript、Lua、Nim、Perl、PHP、Python、Ruby 和 Rust）的解析器代码。这消除了为每种语言手动编写重复且容易出错的解析代码的需求。

该工具集包括一个编译器 (`ksc`)、一个 IDE 和一个用于调试格式的可视化工具。该过程包括在 `.ksy` 文件中描述格式，使用可视化工具验证正确的解析，将 `.ksy` 文件编译成目标语言，并将生成的代码和运行时库包含到项目中。

本文档提供了一个使用 GIF 图像文件格式的快速入门示例，并演示了如何在不同的编程语言中访问特定数据，如宽度和高度。它还详细介绍了如何下载和安装 Kaitai Struct，提供了适用于 Linux (.deb)、macOS (Homebrew)、Windows 和通用 .zip 归档的说明。

Kaitai Struct 是开源的，编译器和可视化工具采用 GPLv3+ 许可，运行时库采用 MIT/Apache v2 许可。文档最后重点介绍了 Format Gallery，这是一个不断增长的格式规范存储库，并列出了使用 Kaitai Struct 的开源项目。

---

## 60. FocusTube: A Chrome extension that hides YouTube Shorts

**原文标题**: FocusTube: A Chrome extension that hides YouTube Shorts

**原文链接**: [https://github.com/CaptainYouz/FocusTube](https://github.com/CaptainYouz/FocusTube)

FocusTube is a Chrome extension designed to help users avoid wasting time on YouTube Shorts. It removes the Shorts block from the YouTube homepage and reduces the size of thumbnails to make them less appealing. The extension aims to encourage users to focus on more valuable content and reclaim time spent mindlessly scrolling through short-form videos. The provided link directs users to a Chrome developer tutorial explaining how to install unpacked extensions, enabling them to install FocusTube manually. In essence, FocusTube is a tool to improve focus and reduce distractions on YouTube by minimizing the visibility and appeal of YouTube Shorts.


---

## 61. Apple loses UK App Store monopoly case, penalty might near $2B

**原文标题**: Apple loses UK App Store monopoly case, penalty might near $2B

**原文链接**: [https://9to5mac.com/2025/10/23/apple-loses-uk-app-store-monopoly-case-penalty-might-near-2-billion/](https://9to5mac.com/2025/10/23/apple-loses-uk-app-store-monopoly-case-penalty-might-near-2-billion/)

生成摘要时出错

---

## 62. Police Break Up Lego Theft Ring

**原文标题**: Police Break Up Lego Theft Ring

**原文链接**: [https://www.nytimes.com/2025/10/18/us/lego-theft-california-arrest.html](https://www.nytimes.com/2025/10/18/us/lego-theft-california-arrest.html)

生成摘要时出错

---

## 63. Zram Performance Analysis

**原文标题**: Zram Performance Analysis

**原文链接**: [https://notes.xeome.dev/notes/Zram](https://notes.xeome.dev/notes/Zram)

生成摘要时出错

---

## 64. RFC 863 – Discard Protocol (1983)

**原文标题**: RFC 863 – Discard Protocol (1983)

**原文链接**: [https://datatracker.ietf.org/doc/html/rfc863](https://datatracker.ietf.org/doc/html/rfc863)

生成摘要时出错

---

## 65. Armed police swarm student after AI mistakes bag of Doritos for a weapon

**原文标题**: Armed police swarm student after AI mistakes bag of Doritos for a weapon

**原文链接**: [https://www.dexerto.com/entertainment/armed-police-swarm-student-after-ai-mistakes-bag-of-doritos-for-a-weapon-3273512/](https://www.dexerto.com/entertainment/armed-police-swarm-student-after-ai-mistakes-bag-of-doritos-for-a-weapon-3273512/)

生成摘要时出错

---

## 66. New updates and more access to Google Earth AI

**原文标题**: New updates and more access to Google Earth AI

**原文链接**: [https://blog.google/technology/research/new-updates-and-more-access-to-google-earth-ai/](https://blog.google/technology/research/new-updates-and-more-access-to-google-earth-ai/)

生成摘要时出错

---

## 67. Pyscripter – Open-source Python IDE written in Delphi

**原文标题**: Pyscripter – Open-source Python IDE written in Delphi

**原文链接**: [https://github.com/pyscripter/pyscripter](https://github.com/pyscripter/pyscripter)

生成摘要时出错

---

## 68. Make any TypeScript function durable

**原文标题**: Make any TypeScript function durable

**原文链接**: [https://useworkflow.dev/](https://useworkflow.dev/)

生成摘要时出错

---

## 69. Google flags Immich sites as dangerous

**原文标题**: Google flags Immich sites as dangerous

**原文链接**: [https://immich.app/blog/google-flags-immich-as-dangerous](https://immich.app/blog/google-flags-immich-as-dangerous)

生成摘要时出错

---

## 70. Identifying Life-Changing Books with LLMs (2024)

**原文标题**: Identifying Life-Changing Books with LLMs (2024)

**原文链接**: [https://blog.joellehman.com/identifying-life-changing-books-with-llms.html](https://blog.joellehman.com/identifying-life-changing-books-with-llms.html)

生成摘要时出错

---

## 71. What happened to Apple's legendary attention to detail?

**原文标题**: What happened to Apple's legendary attention to detail?

**原文链接**: [https://blog.johnozbay.com/what-happened-to-apples-attention-to-detail.html](https://blog.johnozbay.com/what-happened-to-apples-attention-to-detail.html)

生成摘要时出错

---

## 72. Show HN: Sqlite3-dump - a fast SQLite to CSV and parquet

**原文标题**: Show HN: Sqlite3-dump - a fast SQLite to CSV and parquet

**原文链接**: [https://github.com/i64/sqlite3-dump](https://github.com/i64/sqlite3-dump)

生成摘要时出错

---

## 73. Show HN: Git for LLMs – A context management interface

**原文标题**: Show HN: Git for LLMs – A context management interface

**原文链接**: [https://twigg.ai](https://twigg.ai)

生成摘要时出错

---

## 74. VST3 audio plugin format is now MIT

**原文标题**: VST3 audio plugin format is now MIT

**原文链接**: [https://forums.steinberg.net/t/vst-3-8-0-sdk-released/1011988](https://forums.steinberg.net/t/vst-3-8-0-sdk-released/1011988)

生成摘要时出错

---

## 75. Radios, how do they work? (2024)

**原文标题**: Radios, how do they work? (2024)

**原文链接**: [https://lcamtuf.substack.com/p/radios-how-do-they-work](https://lcamtuf.substack.com/p/radios-how-do-they-work)

生成摘要时出错

---

## 76. Summary of the Amazon DynamoDB Service Disruption in US-East-1 Region

**原文标题**: Summary of the Amazon DynamoDB Service Disruption in US-East-1 Region

**原文链接**: [https://aws.amazon.com/message/101925/](https://aws.amazon.com/message/101925/)

生成摘要时出错

---

## 77. CRDTs: Convergence without coordination

**原文标题**: CRDTs: Convergence without coordination

**原文链接**: [https://read.thecoder.cafe/p/crdt](https://read.thecoder.cafe/p/crdt)

生成摘要时出错

---

## 78. PyTorch Monarch

**原文标题**: PyTorch Monarch

**原文链接**: [https://pytorch.org/blog/introducing-pytorch-monarch/](https://pytorch.org/blog/introducing-pytorch-monarch/)

生成摘要时出错

---

## 79. Lea Albaugh, "Underdetermined Weaving with Machines" (2021) [video]

**原文标题**: Lea Albaugh, "Underdetermined Weaving with Machines" (2021) [video]

**原文链接**: [https://www.youtube.com/watch?v=on_sK8KoObo](https://www.youtube.com/watch?v=on_sK8KoObo)

生成摘要时出错

---

## 80. Show HN: Tommy – Turn ESP32 devices into through-wall motion sensors

**原文标题**: Show HN: Tommy – Turn ESP32 devices into through-wall motion sensors

**原文链接**: [https://www.tommysense.com](https://www.tommysense.com)

生成摘要时出错

---

## 81. Show HN: OpenSnowcat – A fork of Snowplow to keep open analytics alive

**原文标题**: Show HN: OpenSnowcat – A fork of Snowplow to keep open analytics alive

**原文链接**: [https://opensnowcat.io/](https://opensnowcat.io/)

生成摘要时出错

---

## 82. Apple Starts Shipping Made-in-America AI Servers Early

**原文标题**: Apple Starts Shipping Made-in-America AI Servers Early

**原文链接**: [https://www.macrumors.com/2025/10/24/apple-starts-shipping-made-in-america-ai-servers/](https://www.macrumors.com/2025/10/24/apple-starts-shipping-made-in-america-ai-servers/)

生成摘要时出错

---

## 83. I spent a year making an ASN.1 compiler in D

**原文标题**: I spent a year making an ASN.1 compiler in D

**原文链接**: [https://bradley.chatha.dev/blog/dlang-propaganda/asn1-compiler-in-d/](https://bradley.chatha.dev/blog/dlang-propaganda/asn1-compiler-in-d/)

生成摘要时出错

---

## 84. Killing Charles Dickens (2023)

**原文标题**: Killing Charles Dickens (2023)

**原文链接**: [https://www.newyorker.com/magazine/2023/07/10/on-killing-charles-dickens](https://www.newyorker.com/magazine/2023/07/10/on-killing-charles-dickens)

生成摘要时出错

---

## 85. Show HN: Deta Surf – An open source and local-first AI notebook

**原文标题**: Show HN: Deta Surf – An open source and local-first AI notebook

**原文链接**: [https://github.com/deta/surf](https://github.com/deta/surf)

生成摘要时出错

---

## 86. I managed to grow countable yeast colonies

**原文标题**: I managed to grow countable yeast colonies

**原文链接**: [https://chillphysicsenjoyer.substack.com/p/i-managed-to-grow-countable-yeast](https://chillphysicsenjoyer.substack.com/p/i-managed-to-grow-countable-yeast)

生成摘要时出错

---

## 87. Scripts I wrote that I use all the time

**原文标题**: Scripts I wrote that I use all the time

**原文链接**: [https://evanhahn.com/scripts-i-wrote-that-i-use-all-the-time/](https://evanhahn.com/scripts-i-wrote-that-i-use-all-the-time/)

生成摘要时出错

---

## 88. Show HN: Inspec – Specification scheduling software for interior designers

**原文标题**: Show HN: Inspec – Specification scheduling software for interior designers

**原文链接**: [https://inspec.design](https://inspec.design)

生成摘要时出错

---

## 89. Unconventional Ways to Cast in TypeScript

**原文标题**: Unconventional Ways to Cast in TypeScript

**原文链接**: [https://wolfgirl.dev/blog/2025-10-22-4-unconventional-ways-to-cast-in-typescript/](https://wolfgirl.dev/blog/2025-10-22-4-unconventional-ways-to-cast-in-typescript/)

生成摘要时出错

---

## 90. Teen Swarmed by Cops After AI Metal Detector Flags His Doritos Bag as a Gun

**原文标题**: Teen Swarmed by Cops After AI Metal Detector Flags His Doritos Bag as a Gun

**原文链接**: [https://gizmodo.com/teen-swarmed-by-cops-after-ai-metal-detector-flags-his-doritos-bag-as-a-gun-2000676491](https://gizmodo.com/teen-swarmed-by-cops-after-ai-metal-detector-flags-his-doritos-bag-as-a-gun-2000676491)

生成摘要时出错

---

## 91. Intel hamstrung by supply shortages across its business

**原文标题**: Intel hamstrung by supply shortages across its business

**原文链接**: [https://www.tomshardware.com/pc-components/cpus/intel-hamstrung-by-supply-shortages-across-its-business-including-production-capacity-says-it-will-prioritize-data-center-cpus-over-consumer-chips-warns-of-price-hikes](https://www.tomshardware.com/pc-components/cpus/intel-hamstrung-by-supply-shortages-across-its-business-including-production-capacity-says-it-will-prioritize-data-center-cpus-over-consumer-chips-warns-of-price-hikes)

生成摘要时出错

---

## 92. A dual-screen, ESP32 powered ereader: Own your device, own your books

**原文标题**: A dual-screen, ESP32 powered ereader: Own your device, own your books

**原文链接**: [https://hackaday.io/project/204323-diptyx-e-reader](https://hackaday.io/project/204323-diptyx-e-reader)

生成摘要时出错

---

## 93. Programming with Less Than Nothing

**原文标题**: Programming with Less Than Nothing

**原文链接**: [https://joshmoody.org/blog/programming-with-less-than-nothing/](https://joshmoody.org/blog/programming-with-less-than-nothing/)

生成摘要时出错

---

## 94. What does the Turing Test test?

**原文标题**: What does the Turing Test test?

**原文链接**: [https://philipball86.substack.com/p/what-does-the-turing-test-test](https://philipball86.substack.com/p/what-does-the-turing-test-test)

生成摘要时出错

---

## 95. Show HN: Nostr Web – decentralized website hosting on Nostr

**原文标题**: Show HN: Nostr Web – decentralized website hosting on Nostr

**原文链接**: [https://nweb.shugur.com](https://nweb.shugur.com)

生成摘要时出错

---

## 96. Upgrading Our Way Through OpenGL 1.x

**原文标题**: Upgrading Our Way Through OpenGL 1.x

**原文链接**: [https://bumbershootsoft.wordpress.com/2025/09/27/upgrading-our-way-through-opengl-1-x/](https://bumbershootsoft.wordpress.com/2025/09/27/upgrading-our-way-through-opengl-1-x/)

生成摘要时出错

---

## 97. Front-Panel Booting an ATmega88 Microcontroller

**原文标题**: Front-Panel Booting an ATmega88 Microcontroller

**原文链接**: [https://www.linusakesson.net/hardware/frontpanel/index.php](https://www.linusakesson.net/hardware/frontpanel/index.php)

生成摘要时出错

---

## 98. Deepstaria Enigmatica

**原文标题**: Deepstaria Enigmatica

**原文链接**: [https://en.wikipedia.org/wiki/Deepstaria_enigmatica](https://en.wikipedia.org/wiki/Deepstaria_enigmatica)

生成摘要时出错

---

## 99. More than 1,200 games journalists have left the media in the last two years

**原文标题**: More than 1,200 games journalists have left the media in the last two years

**原文链接**: [https://www.videogameschronicle.com/news/more-than-1200-games-journalists-have-left-the-media-in-the-last-two-years/](https://www.videogameschronicle.com/news/more-than-1200-games-journalists-have-left-the-media-in-the-last-two-years/)

生成摘要时出错

---

## 100. How count-min sketches work – frequencies, but without the actual data

**原文标题**: How count-min sketches work – frequencies, but without the actual data

**原文链接**: [https://www.instantdb.com/essays/count_min_sketch](https://www.instantdb.com/essays/count_min_sketch)

生成摘要时出错

---

