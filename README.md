# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-06-08.md)

*最后自动更新时间: 2026-06-08 19:48:47*
## 1. 阻止 Apple Music 应用启动

**原文标题**: Stop the Apple Music app from launching

**原文链接**: [https://lowtechguys.com/musicdecoy/](https://lowtechguys.com/musicdecoy/)

**Music Decoy** 是一款轻量级的 macOS 工具，旨在防止 Apple Music 应用自动启动。这种非预期的启动行为通常发生在没有其他媒体应用处于活动状态时按下“播放”键、连接蓝牙耳机或通话结束时。

**工作原理**
该应用通过采用与官方 Music 应用相同的 Bundle Identifier (`com.apple.Music`) 来运行。这会误导 macOS 的 **Remote Control Daemon (rcd)**（负责处理媒体键的进程），使其认为 Music 应用已经在运行，从而阻止其触发新实例。与其他方案不同，Music Decoy 在保留媒体键功能的同时，几乎不消耗后台 CPU。

**主要功能与配置**
*   **自定义重定向：** 自 1.1 版本起，用户可以使用特定的终端命令 (`defaults write com.lowtechguys.MusicDecoy mediaAppPath`) 配置 Music Decoy，使其在按下“播放”按钮时启动其他应用程序（如 Spotify）。
*   **安装：** 可通过 Homebrew 安装：`brew install music-decoy`。
*   **管理：** 为保持极简占用，该应用没有 Dock 或菜单栏图标。用户可以通过“活动监视器”或在终端使用 `killall 'Music Decoy'` 命令来退出程序。

**方案对比**
相比常见的替代方案，Music Decoy 提供了一种更优雅的处理方式。卸载 `rcd` 守护进程会导致媒体键完全失效，而像 `noTunes` 类的应用则是在 Music 启动后将其强行关闭；Music Decoy 则能在启动发生之前将其阻止，且无需牺牲键盘控制功能。

---

## 2. MiMo-v2.5-Pro-UltraSpeed：每秒 1000 token 的 1T 模型

**原文标题**: MiMo-v2.5-Pro-UltraSpeed: 1T model with 1000 tokens per second

**原文链接**: [https://mimo.xiaomi.com/blog/mimo-tilert-1000tps](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps)

小米与 TileRT 合作发布了 MiMo-v2.5-Pro-UltraSpeed，这是一款拥有 1 万亿参数 (1T) 的模型，在通用 GPU 硬件上实现了超过 1,000 tokens/秒 (TPS) 的突破性生成速度。这一性能代表了范式的转变，支持实时推理（并行“N 选最优”路径）、瞬时编程代理，以及高频交易和手术辅助等关键领域的毫秒级决策。

这种速度是通过涉及三项核心技术创新的极致“模型-系统协同设计”实现的：
1. **FP4 量化：** 通过对混合专家模型 (MoE) 选择性地应用 FP4 (MXFP4) 量化，同时保留其他模块的精度，团队在不牺牲推理质量的情况下显著降低了显存带宽压力。
2. **DFlash 投机解码：** 利用块级掩码并行预测方法，该模型每轮可以验证 6-7 个 token（在编程场景中），从根本上打破了传统自回归草稿生成的串行约束。
3. **TileRT 推理系统：** 一种定制引擎，通过持久化算子 (Persistent Kernels) 和 Warp 特化 (Warp Specialization) 消除了算子之间的“执行间隙”。这使计算流水线常驻 GPU，最大限度地提高了硬件利用率。

**获取方式：**
MiMo-v2.5-Pro-UltraSpeed API 将在 **2026 年 6 月 9 日至 6 月 23 日**期间通过限时申请窗口提供。虽然该 API 的价格是标准 Pro 模型的 3 倍，但其输出速度提升了 10 倍。为了支持开发者社区，小米已在 HuggingFace 上开源了 FP4 量化权重和 DFlash 参数。

---

## 3. Show HN: Performative-UI – 一个设计套路 React 组件库

**原文标题**: Show HN: Performative-UI – a react component library of design tropes

**原文链接**: [https://vorpus.github.io/performativeUI/](https://vorpus.github.io/performativeUI/)

**Performative-UI** 是一个专门为构建“AI 原生”用户界面而设计的 React 组件库。该项目最近在 Hacker News 上发布，旨在为开发者提供一套“设计范式”工具包，涵盖了现代、高质感 AI 应用中常用的视觉模式和审美风格。

该库专注于以下几个核心领域：

*   **AI 原生设计：** 组件针对生成式 AI 独特的交互模型进行了优化，例如流式文本输出、复杂处理过程的加载状态以及动态内容布局。
*   **现代美学：** 它将流行的 UI 趋势（常被称为“设计惯例”）转化为可复用的 React 组件，让开发者能够轻松实现复杂的视觉效果，从而营造出高端且前沿的使用体验。
*   **易于集成：** 作为基于 React 的库，它能够无缝接入现有的前端开发流程，使开发者无需从零开始设计每一个自定义动画或过渡效果，即可构建出视觉效果出众的 AI 工具。

简而言之，Performative-UI 在原始的 AI 功能与用户所期待的现代生成式平台那种高度风格化、具有“表演性”的界面之间搭建了一座桥梁。

---

## 4. TI-84 Plus 操作系统完整逆向工程

**原文标题**: Full Reverse Engineering of the TI-84 Plus Operating System

**原文链接**: [https://siraben.github.io/ti84p-re/](https://siraben.github.io/ti84p-re/)

本文提供了 TI-84 Plus 操作系统 (v2.55MP) 逆向工程的技术概览。该系统专为 Zilog Z80 CPU 设计，通过 4 插槽分页方案和“bcall”（系统调用）机制管理 1 MiB 闪存和 128 KiB RAM 环境，从而突破了 Z80 原生的 64 KiB 地址总线限制。

该架构建立在四个核心支柱之上：
1. **分页与 bcall：** 通过 `rst 28h` 指令实现跨不同内存页面的代码执行和数据检索。
2. **浮点引擎：** 使用专用“OP”寄存器处理 9 字节 BCD 实数和复数。
3. **变量分配表 (VAT)：** 编目并管理命名对象，如列表、程序、矩阵和字符串。
4. **令牌生成器/解析器：** 解释并执行以令牌形式存储的 TI-BASIC 程序。

该操作系统作为单任务监控程序运行，其永久内核核心位于闪存第 0 页。它利用 IM1 中断服务例程来处理计时、ON 键以及键盘扫描。专用子系统负责管理 I/O，包括 LCD 驱动程序、链接端口和 USB 传输协议。

该文档为各种模块提供了详尽的索引，涵盖内存管理（堆和闪存存档）、计算引擎（统计、矩阵和求解器）以及绘图原语。该项目采用分层置信度系统——[已确认]、[标准] 或 [假设]——来验证反汇编结果，并使用 Ghidra 进行 ROM 分析。这项逆向工程工作提供了 TI-84 Plus 内部逻辑的详细路线图，从底层硬件端口到高层用户界面行为均有涵盖。

---

## 5. 反社交：如今主导社交媒体动态的是流行趋势，而非朋友。

**原文标题**: Anti-social: It's fads, not friends, which now dominate social media feeds

**原文链接**: [https://www.bbc.com/worklife/article/20260520-how-social-media-ceased-to-be-social](https://www.bbc.com/worklife/article/20260520-how-social-media-ceased-to-be-social)

社交媒体经历了根本性的转型，从朋友间的“数字城镇广场”演变为由人工智能驱动、以专业内容为主导的娱乐中心。TikTok、Instagram和Facebook等主流平台现在优先推送“非关注内容”——即来自陌生人的视频和梗图——并利用旨在最大化参与度而非促进个人联系的算法。

文章指出，英国、美国和法国的活跃发帖量显著下降。用户（尤其是Z世代）正逐渐成为被动消费者；虽然74%的Z世代每天通过社交媒体寻求娱乐，但只有18%的人会发布内容。专家将此归因于人们对数字足迹意识的增强，以及高质量专业内容带来的“威慑效应”。个人社交互动并未消失，而是转移到了WhatsApp等私密通讯应用和封闭群组中。

这种转变为平台的盈利带来了巨大红利。全球社交媒体广告收入预计到2026年将达到3170亿美元，Meta有望在广告销售额上超越谷歌。AI驱动的定向投送已变得如此精准，以至于信息流就像是个性化的电视，算法根据深度用户数据掌控着“遥控器”。这一演化迫使小企业必须扮演专业内容创作者和“趋势洞察者”的角色，以维持品牌曝光。

最终，社交媒体分化成了两部分：大型平台充当被动娱乐和发现引擎，而私密通讯则成为了新的“社交”空间。尽管存在优先显示好友动态的工具，但绝大多数用户仍选择浏览算法筛选的信息流，这标志着数字行为发生了永久性的转变。

---

## 6. 瑞士将举行全民公投，限制人口上限为1000万。

**原文标题**: Switzerland wil have a referendum to cap population at 10M

**原文链接**: [https://www.admin.ch/en/sustainability-initiative](https://www.admin.ch/en/sustainability-initiative)

“可持续发展倡议”（正式名称为“反对1000万人口的瑞士”）是由右翼的瑞士人民党（SVP）发起的一项全民倡议，目前已正式获得触发全国公投所需的法定签名数。该倡议旨在修改瑞士联邦宪法，以确保常住人口在2050年之前不超过1000万人。

该提案概述了应对人口增长的分级措施：
*   **950万人口门槛：** 若人口达到950万，联邦委员会和议会将必须采取限制性措施，特别是针对庇护程序和家庭团聚。
*   **1000万人口上限：** 若人口触及1000万上限，该倡议要求瑞士终止会导致人口增长的国际协议，其中明确包括与欧盟签署的《人员自由流动协议》。

支持者认为，主要由移民驱动的人口快速增长正给瑞士的基础设施、住房市场、医疗体系和自然环境带来不可持续的压力。他们主张，必须设立硬性上限以维护国家的高生活质量及其“人文规模”的景观。

然而，该倡议遭到政府、多个政党以及商业部门的强烈反对。批评者认为，限制人口并可能退出人员自由流动协议将导致严重的劳动力短缺，并危及瑞士与欧盟的经济及外交关系。

该倡议已于2024年4月提交了超过11.4万份有效签名，目前将进入议会审查程序，随后预计将在未来几年内交付全民表决。

---

## 7. xAI 看起来更像是一家数据中心 REIT，而非前沿实验室。

**原文标题**: xAI is looking more like a datacentre REIT than a frontier lab

**原文链接**: [https://martinalderson.com/posts/xais-new-rental-business/](https://martinalderson.com/posts/xais-new-rental-business/)

在与 SpaceX 合并后，xAI 正从纯粹的前沿人工智能实验室转型为庞大的基础设施提供商，其模式日益趋向于“数据中心房地产投资信托（REIT）”。该公司近期达成了多项高价值协议，将其 GPU 算力租赁给竞争对手 Anthropic 和 Google，标志着其战略的重大转向。

据报道，此前深受产能限制困扰的 Anthropic 每月支付 12.5 亿美元以获取 xAI 孟菲斯“Colossus 1”设施的使用权。Google 紧随其后，签署了每月 9.2 亿美元的协议。这些交易的利润空间极大；作者估计，由于电力等运营成本与巨额租金相比几乎可以忽略不计，xAI 有望在 18 个月内回收全部资本支出。

推动这一转变的关键因素是 xAI 的速度。当传统的超大规模云服务商需要数年时间兴建设施，且 OpenAI 因阿联酋项目面临地缘政治风险时，xAI 仅用 122 天就完成了孟菲斯数据中心的建设。在全球算力短缺的情况下，这种快速部署基础设施的能力构成了独特的竞争优势。

然而，这一转型也让 xAI 自身模型 Grok 的未来变得模糊不清。通过向竞争对手出租大量算力，xAI 似乎正在退出主导性前沿模型的角逐——这或许是因为 Grok 的需求低于预期，或者是为了优先确保即时收入的战略考量。

作者最后指出，尽管这些举动可能包含为提升 SpaceX 即将进行的 IPO 估值而进行的财技运作，但它们反映出一个现实：xAI 的核心价值在于成为基础设施强权，而非仅仅是一个模型开发商。如今的 xAI 本质上已成为 AI 行业的高毛利“房东”，并附设了一个研究实验室。

---

## 8. Why are cells small?

**原文标题**: Why are cells small?

**原文链接**: [https://burrito.bio/essays/what-limits-a-cells-size](https://burrito.bio/essays/what-limits-a-cells-size)

The article explores the biological and physical factors that determine cell size, noting that while human cells range from tiny sperm (30 µm³) to large oocytes (4,000,000 µm³), their dimensions are primarily dictated by the laws of physics.

The first major constraint is the **surface area-to-volume ratio**. As a cell grows, its volume increases much faster than its surface area. Because the cell membrane is responsible for nutrient intake, waste removal, and energy production, a cell that is too large cannot sustain its internal "stuff" efficiently.

The second constraint is **diffusion**. Cellular processes rely on random molecular collisions to function. In a small volume, molecules like enzymes and substrates meet quickly. However, as volume increases, the time required for molecules to traverse the cell grows exponentially; a protein that crosses a bacterium in 0.01 seconds would take hours to travel just one centimeter.

Cells employ various strategies to work within or bypass these limits:
*   **Red blood cells** adopt a biconcave shape to increase surface area for oxygen exchange while remaining small enough to fit through capillaries.
*   **Eukaryotic cells** use compartmentalization (organelles) to concentrate molecules and facilitate faster interactions.
*   **Oocytes** can be large because they are less metabolically active and stockpile nutrients.
*   **Giant cells**, such as the bacterium *Thiomargarita magnifica* and bubble algae, reach visible sizes by filling their centers with large, inert vacuoles. This pushes the cytoplasm to the edge of the cell, keeping diffusion distances short.

Ultimately, the author concludes that cell architecture is a "diagram of forces," shaped by a delicate trade-off between functional needs and the immutable physical limits of geometry and diffusion.

---

## 9. Thunderbird Littering My Home

**原文标题**: Thunderbird Littering My Home

**原文链接**: [https://thefoggiest.dev/2026/06/04/thunderbird-littering-my-home](https://thefoggiest.dev/2026/06/04/thunderbird-littering-my-home)

生成摘要时出错

---

## 10. OCaml Onboarding: Introduction to the Dune build system

**原文标题**: OCaml Onboarding: Introduction to the Dune build system

**原文链接**: [https://ocamlpro.com/blog/2025_07_29_ocaml_onboarding_introduction_to_dune/](https://ocamlpro.com/blog/2025_07_29_ocaml_onboarding_introduction_to_dune/)

This article provides a practical introduction to **Dune**, the standard build system for the OCaml ecosystem. Aimed at newcomers, it explains how to structure, build, and test projects from the ground up to foster a deep understanding of the toolchain.

The guide identifies two essential configuration files:
*   **`dune-project`**: Located at the project root, it contains metadata such as the Dune version, package names, and configuration for automatic opam file generation.
*   **`dune`**: These files reside in subdirectories and use **stanzas** (declarative configuration blocks) to define how code is compiled. Key stanzas include `library` for reusable packages, `executable` for runnable binaries, and `test` for defining test suites.

The article outlines several fundamental commands for the development workflow:
*   **`dune build @all`**: Compiles all targets defined in the project.
*   **`dune build @doc`**: Uses `odoc` to generate HTML documentation from OCaml comments.
*   **`dune exec -- [path]`**: Builds and runs a specific executable, passing any subsequent arguments to the binary.
*   **`dune runtest`**: Executes the project's test suite.

A significant portion of the guide focuses on testing. Beyond standard library testing with tools like `Alcotest`, it highlights **Cram tests**. These are functional tests stored in `.t` files that simulate shell sessions, comparing the actual output of a command-line tool against the expected output.

While Dune offers scaffolding tools like `dune init`, the authors advocate for manual configuration initially. This approach ensures developers understand how Dune works "under the hood," enabling them to modify projects confidently and integrate effectively with other tools like **opam**.

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 2 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 3 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 4 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 5 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 6 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 7 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 8 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 9 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 10 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 11 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 12 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 13 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 14 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 15 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 16 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 17 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 18 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 19 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 20 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 21 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 22 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 23 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 24 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 25 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 26 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 27 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 28 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 29 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 30 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 31 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 32 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 33 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 34 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 35 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 36 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 37 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 38 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 39 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 40 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 41 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 42 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 43 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 44 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 45 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 46 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 47 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 48 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 49 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 50 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 51 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 52 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 53 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 54 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 55 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 56 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 57 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 58 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 59 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 60 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 61 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 62 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 63 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 64 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 65 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 66 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 67 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 68 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 69 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 70 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 71 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 72 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 73 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 74 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 75 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 76 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 77 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 78 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 79 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 80 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 81 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 82 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 83 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 84 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 85 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 86 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 87 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 88 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 89 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 90 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 91 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 92 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 93 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 94 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 95 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 96 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 97 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 98 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 99 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 100 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 101 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 102 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 103 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 104 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 105 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 106 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 107 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 108 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 109 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 110 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 111 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 112 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 113 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 114 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 115 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 116 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 117 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 118 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 119 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 120 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 121 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 122 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 123 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 124 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 125 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 126 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 127 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 128 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 129 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 130 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 131 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 132 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 133 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 134 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 135 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 136 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 137 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 138 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 139 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 140 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 141 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 142 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 143 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 144 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 145 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 146 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 147 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 148 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 149 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 150 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 151 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 152 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 153 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 154 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 155 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 156 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 157 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 158 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 159 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 160 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 161 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 162 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 163 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 164 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 165 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 166 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 167 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 168 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 169 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 170 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 171 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 172 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 173 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 174 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 175 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 176 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 177 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 178 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 179 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 180 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 181 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 182 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 183 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 184 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 185 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 186 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 187 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 188 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 189 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 190 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 191 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 192 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 193 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 194 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 195 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 196 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 197 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 198 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 199 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 200 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 201 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 202 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 203 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 204 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 205 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 206 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 207 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 208 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 209 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 210 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 211 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 212 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 213 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 214 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 215 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 216 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 217 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 218 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 219 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 220 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 221 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 222 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 223 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 224 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 225 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 226 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 227 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 228 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 229 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 230 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 231 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 232 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 233 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 234 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 235 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 236 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 237 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 238 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 239 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 240 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 241 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 242 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 243 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 244 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 245 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 246 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 247 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 248 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 249 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 250 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 251 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 252 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 253 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 254 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 255 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 256 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 257 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 258 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 259 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 260 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 261 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 262 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 263 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 264 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 265 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 266 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 267 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 268 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 269 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 270 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 271 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 272 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 273 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 274 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 275 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 276 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 277 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 278 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 279 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 280 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 281 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 282 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 283 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 284 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 285 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 286 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 287 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 288 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 289 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 290 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 291 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 292 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 293 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 294 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 295 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 296 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 297 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 298 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 299 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 300 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 301 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 302 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 303 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 304 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 305 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 306 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 307 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 308 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 309 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 310 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 311 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 312 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 313 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 314 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 315 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 316 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 317 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 318 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 319 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 320 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 321 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 322 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 323 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 324 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 325 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 326 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 327 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 328 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 329 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 330 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 331 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 332 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 333 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 334 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 335 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 336 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 337 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 338 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 339 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 340 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 341 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 342 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 343 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 344 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 345 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 346 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 347 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 348 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 349 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 350 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 351 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 352 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 353 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 354 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 355 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 356 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 357 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 358 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 359 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 360 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 361 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 362 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 363 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 364 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 365 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 366 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 367 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 368 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 369 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 370 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 371 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 372 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 373 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 374 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 375 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 376 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 377 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 378 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 379 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 380 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 381 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 382 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 383 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 384 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 385 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 386 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 387 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 388 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 389 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 390 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 391 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 392 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 393 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 394 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 395 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 396 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 397 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 398 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 399 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 400 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 401 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 402 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 403 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 404 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 405 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 406 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 407 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 408 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 409 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 410 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 411 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 412 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 413 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 414 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 415 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 416 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 417 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 418 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 419 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 420 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 421 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 422 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 423 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 424 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 425 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 426 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 427 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 428 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 429 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 430 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 431 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 432 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 433 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 434 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 435 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 436 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 437 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 438 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 439 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 440 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 441 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 442 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 443 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 444 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 445 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
