# Hacker News 热门文章摘要 (2025-05-17)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Nintendo 64 调色板光照技巧

**原文标题**: Palette lighting tricks on the Nintendo 64

**原文链接**: [https://30fps.net/pages/palette-lighting-tricks-n64/](https://30fps.net/pages/palette-lighting-tricks-n64/)

本文详细介绍了 Pekka Väänänen 开发的任天堂 64 演示中所使用的调色板光照技巧。该演示在 N64 的限制范围内实现了烘焙光照、法线贴图和高光着色。

核心技术围绕“调色板空间”着色展开。渲染器不是单独对每个纹素进行着色，而是更新纹理的调色板。这样可以大幅减少纹理更新的 CPU 消耗，因为对调色板的更改会立即在整个纹理中传播。

作者讨论了物体空间法线贴图，它通过将绝对表面法线存储在法线贴图的纹素中，简化了运行时数学运算。这些法线与漫反射纹理共享同一调色板，并通过 K-means 聚类进行优化。

文章解释了如何使用顶点颜色来合并烘焙的方向性环境光和太阳光。环境光被分为方向强度（灰度环境贴图）和颜色，而太阳光使用顶点 Alpha 值来表示可见性。

作者解决了在较大模型上重复纹理的难题，方法是将网格分割成共享物体空间法线贴图的子网格，从而创建近似的切线空间。高光着色通过将物体近似为一个球体来实现，从而产生分面的高光。

文章最后反思了该技术的局限性，包括着色不连续性和对预处理的依赖，同时强调了探索这些约束以及改进的可能性所带来的乐趣。作者也在考虑撰写一本关于该主题的书。

---

## 2. 将If条件上移，将For循环下移

**原文标题**: Push Ifs Up and Fors Down

**原文链接**: [https://matklad.github.io/2023/11/15/push-ifs-up-and-fors-down.html](https://matklad.github.io/2023/11/15/push-ifs-up-and-fors-down.html)

代码组织的两条经验法则：“上推If”和“下推For”。

**上推If：** 建议将条件逻辑（if语句）从函数内部移至调用者。主要优点是提高代码清晰度、减少错误和潜在的性能提升。通过将控制流集中在调用者中，函数简化为直线子程序。这使得更容易发现冗余或死代码。作者使用“溶解枚举”重构作为一个例子，展示了如何上推条件逻辑可以揭示以前被枚举使用所掩盖的冗余。

**下推For：** 倡导批量处理数据，而不是单独处理。核心思想是针对处理大量实体的场景进行优化，使批处理操作成为标准，而标量操作成为特殊情况。这里的主要动机是性能。批处理允许分摊启动成本、处理顺序的灵活性（包括向量化和结构数组技术），甚至可以实现更高效的算法，如基于FFT的多项式乘法。作者认为，将`if`条件移出`for`循环可以通过避免冗余的条件评估并开启向量化的可能性来显著提高性能。它还提到批处理可以提高表达能力。

简而言之，作者建议重构代码，使控制流决策发生在进入循环*之前*，并以批处理方式处理数据，以获得更好的性能和清晰度。

---

## 3. JavaScript的新超能力：显式资源管理

**原文标题**: JavaScript's New Superpower: Explicit Resource Management

**原文链接**: [https://v8.dev/features/explicit-resource-management](https://v8.dev/features/explicit-resource-management)

JavaScript 中的显式资源管理提案引入了使用 `using` 和 `await using` 声明来分别进行同步和异步资源的确定性资源管理。这些声明会在可释放资源超出作用域时自动调用其 `[Symbol.dispose]()` 或 `[Symbol.asyncDispose]()` 方法，从而防止资源泄漏。

该提案还包括 `DisposableStack` 和 `AsyncDisposableStack` 来管理多个可释放资源。这些栈允许对资源进行分组并按添加的相反顺序释放，从而确保正确的依赖关系处理。这些栈提供了诸如 `use()`、`adopt()` 和 `defer()` 之类的方法来添加资源或释放操作。它们还具有 `dispose()`/`asyncDispose()` 方法和 `move()` 来将资源转移到另一个 `DisposableStack`。

最后，`SuppressedError` 用于解决释放期间的错误，防止它们掩盖现有错误。

该提案旨在通过提供对资源释放的细粒度控制来提高代码的健壮性、性能和可维护性。Chromium 134 和 V8 v13.8 已经支持显式资源管理，Firefox 也实现了它。 Safari 和 Node.js 目前尚不支持。Babel 支持该提案。

---

## 4. “我们将比谷歌更不保密”，Proton威胁退出瑞士

**原文标题**: "We would be less confidential than Google" Proton threatens to quit Switzerland

**原文链接**: [https://www.techradar.com/vpn/vpn-privacy-security/we-would-be-less-confidential-than-google-proton-threatens-to-quit-switzerland-over-new-surveillance-law](https://www.techradar.com/vpn/vpn-privacy-security/we-would-be-less-confidential-than-google-proton-threatens-to-quit-switzerland-over-new-surveillance-law)

Proton威胁离开瑞士，因瑞士拟议的监控法修正案要求VPN、消息应用和社交网络识别并保留用户数据。NymVPN等其他瑞士公司也准备离开。Proton CEO颜表示，该法案将损害瑞士声誉。修正案咨询期已于2025年5月6日结束，瑞士政府的决定悬而未决。

---

## 5. OBNC – Oberon-07编译器

**原文标题**: OBNC – Oberon-07 Compiler

**原文链接**: [https://miasap.se/obnc/](https://miasap.se/obnc/)

OBNC是Oberon编程语言的一个编译器，特指2016年的最终版本。它将Oberon源代码翻译成C代码，然后使用宿主操作系统的C编译器和链接器进行编译。`obnc`命令可以自动完成这个过程。

该编译器以GNU GPL协议发布，而库则使用Mozilla公共许可证，允许使用OBNC编译的Oberon项目具有灵活的许可。

源代码包包括编译器、构建工具、文档生成器和一个基本库，以及一个扩展库（`ext`），其中包含用于命令行参数、环境变量和错误处理的模块。

下载内容包括源代码包（可在具有Boehm-Demers-Weiser垃圾回收器的POSIX系统上编译）和MS Windows的预编译版本。

本文还提供了用于Gedit和Pluma的文本编辑器扩展，以改进Oberon代码编辑，包括语法高亮和保留字的自动大写。文档和文章涵盖了Oberon语言规范、OBNC命令和编程技术。还提供了一份免费的“Oberon-2中的面向对象编程”PDF文档。

联系信息也包含在内，用于反馈和社区支持。该网站强调它不使用Javascript和cookie。

---

## 6. 商业墨水和染料制备激光诱导石墨烯

**原文标题**: Laser-Induced Graphene from Commercial Inks and Dyes

**原文链接**: [https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202412167](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202412167)

无法访问文章链接。

---

## 7. 日本的IC卡既奇怪又有趣

**原文标题**: Japan's IC cards are weird and wonderful

**原文链接**: [https://aruarian.dance/blog/japan-ic-cards/](https://aruarian.dance/blog/japan-ic-cards/)

本文探索了日本IC卡的独特世界，重点介绍了为其提供动力的FeliCa技术。与西方主要基于MIFARE的NFC系统不同，日本采用了FeliCa，这是一种由索尼开发的标准，以其速度和效率而闻名，从而实现了在交通闸门处的流畅、快速的刷卡进出体验。

作者解释了NFC的基础知识，以及FeliCa（NFC-F）与MIFARE（NFC-A）和EMV（用于非接触式支付）的区别。一个关键的区别是FeliCa的储值模式，卡本身持有余额和交易历史记录，无需在交易期间进行实时服务器通信，从而提高了速度。

文章随后深入探讨了Osaifu-Keitai，这是一个允许手机模拟IC卡的系统，以及它与FeliCa、NFC以及Apple/Google手机的关系。Osaifu-Keitai需要在手机安全元件中特定的密钥，这些密钥通常只存在于日本特定的Android SKU中。然而，Apple在所有iPhone中都包含了Osaifu-Keitai功能。

最后，作者讨论了FeliCa的安全性。尽管卡上存储了价值，但由于其强大的加密技术，FeliCa被认为是高度安全的。克隆和重放攻击通常无效。文章探讨了潜在的攻击途径，例如利用Apple的实现或针对可能缺乏实时审计跟踪的离线终端（如自动售货机）。

作者最后提出了未来的想法，包括建立一个微型火车站网络，并研究FeliCa速度优势背后的物理原理。总的来说，这篇文章对一项悄然彻底改变了日本和亚洲其他地区交通和支付方式的技术提供了引人入胜的见解。

---

## 8. 紧凑型3D高斯溅射的最速下降密度控制

**原文标题**: Steepest Descent Density Control for Compact 3D Gaussian Splatting

**原文链接**: [https://arxiv.org/abs/2505.05587](https://arxiv.org/abs/2505.05587)

这篇于2025年5月8日提交的arXiv文章介绍了“紧凑型3D高斯溅射的最速下降密度控制”(SteepGS)。 该论文解决了3D高斯溅射 (3DGS) 中因其密集化算法产生的冗余点云而导致的内存使用过多和性能瓶颈问题。

由王培豪领导的作者们提出了一个理论框架，用于分析和改进3DGS中的密度控制。他们认为分裂是优化过程中逃离鞍点的关键。他们的分析建立了密集化的必要条件，确定了最佳子高斯数量，找到了最佳参数更新方向，并为归一化子不透明度提供了分析解。

基于这些见解，他们提出了一种原则性的策略SteepGS，它融合了最速密度控制。该方法在保持紧凑点云的同时最大限度地减少损失。作者声称，与标准3DGS相比，SteepGS可以在不牺牲渲染质量的前提下，将高斯点的数量减少约50%。这显著提高了效率和可扩展性，使3DGS更适合在资源受限的设备上部署。该论文已被CVPR 2025接收，并包含一个项目页面。

---

## 9. 新型操作系统目录

**原文标题**: Catalog of Novel Operating Systems

**原文链接**: [https://github.com/prathyvsh/os-catalog](https://github.com/prathyvsh/os-catalog)

本文介绍近年来开发的新型操作系统的目录，这些操作系统的灵感来源于商业系统占据主导地位之前，操作系统多样化的格局。作者赞扬创新精神，并重点介绍旨在重新构想计算的项目。

提到的主要项目包括：

*   **UXN/Varvara:** 100 Rabbits 团队开发的个人计算堆栈，具有激进的愿景。
*   **Playbit:** Rasmus Andersson 及其团队旨在重塑计算机堆栈的项目。
*   **Folk.computer:** Omar Rizwan 和 Andreas Cuérvo 的项目。
*   **Nette.io:** Pawel Ceranka 针对网络的研究所操作系统。
*   **Interim:** 用 Lisp 构建的最小操作系统。
*   **Mezzano:** 用 Common Lisp 编写的操作系统。
*   **ChrysalLisp:** 具有各种功能的多线程、多核操作系统。
*   **RayvnOS 和 RedoxOS:** 操作系统项目。
*   **DesktopNeo:** Lennart Ziburski 对桌面界面的重新思考。
*   **MercuryOS:** Jason Yuan 基于意图的操作系统概念，可能发展为 Makespace.fun 和 New.computer。
*   **Freeze.app:** 用于冻结和解冻桌面界面的应用程序。
*   **WormOS:** 探索分区的房间和精神空间。
*   **Bedrock.computer:** 状态未知的项目。

作者还提供了其他操作系统列表的链接，例如 @jubalh 的 AwesomeOS 和 Anagora List。

---

## 10. 如果没有策展，我们如何发现事物？

**原文标题**: If nothing is curated, how do we find things

**原文链接**: [https://tadaima.bearblog.dev/if-nothing-is-curated-how-do-we-find-things/](https://tadaima.bearblog.dev/if-nothing-is-curated-how-do-we-find-things/)

如果无人策展，我们如何发现事物
在《如果无人策展，我们如何发现事物》一文中，作者感叹从策展媒体向算法驱动内容的转变，及其对发现新艺术和信息的影响。受到Reddit上关于比约克新电影的令人困惑的讨论的启发，作者反思了在大学广播、MTV和像埃伯特和罗珀这样的评论家等策展来源的帮助下，发现音乐和电影更容易的时代。

他们认为，社交媒体和算法创造了压倒性的“信息泥潭”，需要持续的关注，并使找到有价值的内容变得困难。作者批评了传统策展的衰落和点击驱动文章的兴起，甚至使像Pitchfork这样成熟的出版物也让人感到难以承受。

这篇文章认为，算法将用户困在回音室中，阻碍了他们接触多元艺术。这导致精神疲惫和无法跟上大量可用媒体的步伐，常常导致人们拒绝推荐。

作为个人解决方案，作者已经开始在Obsidian中创建笔记和列表，这是一种自我策展的形式。虽然不理想，但这是一种重新控制发现的方式。作者总结说，社会正在分裂成两个群体：拥抱算法泡沫的人和积极独立寻找信息的人，并承认后者需要付出巨大的努力。

---

## 11. 内核开发者玩转Home Assistant

**原文标题**: A kernel developer plays with Home Assistant

**原文链接**: [https://lwn.net/SubscriberLink/1017720/7155ecb9602e9ef2/](https://lwn.net/SubscriberLink/1017720/7155ecb9602e9ef2/)

这篇LWN.net文章从一位内核开发人员使用一年后的角度，评测了开源家庭自动化平台Home Assistant。文章强调了该平台对于那些对基于云的解决方案持谨慎态度的人的吸引力，以及其对本地控制的关注。

文章评估了Home Assistant的项目健康状况，指出Nabu Casa（背后的公司）的参与，但强调了该项目的开放性、庞大的贡献者基础以及责任转移给开放家庭基金会。 然后，文章深入探讨了安装过程，解释说虽然它主要是为专用设备或自定义操作系统设计的，但在标准Linux系统上安装是可能的，尽管是“高级的”。

核心功能涉及“集成”，用于连接各种设备。 虽然包含了很多集成，但大多数用户将依赖于Home Assistant Community Store (HACS)，它需要一个GitHub帐户才能使用完整功能。 作者注意到集成的质量参差不齐，既有成功也有失败，并将此与Linux早期的设备支持相提并论。

文章讨论了安全方面，提到了该项目的安全策略、对第三方集成的缺乏审查，以及与未知代码相关的潜在风险。 最后，评论提到了设置设备、重命名传感器、创建仪表板（现在基本不依赖YAML）以及探索自动化和场景的过程。 作者总结说，Home Assistant为家庭控制提供了一个强大而开放的平台，使使用户摆脱了基于云的系统，并提供了对其家庭的良好控制。 该系列的结尾部分将介绍有趣的使用案例故事。

---

## 12. 实现RISC-V虚拟机监控器

**原文标题**: Implementing a RISC-V Hypervisor

**原文链接**: [https://seiya.me/blog/riscv-hypervisor](https://seiya.me/blog/riscv-hypervisor)

本文记录了作者为其新操作系统Starina实现RISC-V虚拟机管理程序的历程。目标是实现与WSL2类似的无缝Linux集成。

该虚拟机管理程序利用RISC-V H扩展，该扩展提供了硬件辅助虚拟化。作者使用QEMU的RISC-V H扩展仿真在macOS上进行开发和调试。

开发过程是增量的，从基本的访客进入和执行开始。关键里程碑包括：

*   **进入访客：** 成功切换到VS模式（访客内核模式）。
*   **首次ecall：** 在访客中执行系统调用。
*   **Hello World：** 在访客中运行一个简单的“Hello World”程序。
*   **启动Linux：** 尝试启动完整的Linux内核。

遇到的挑战和实施的解决方案：

*   **访客页表：** 正确映射访客物理地址到宿主机物理地址。
*   **设备树：** 向访客操作系统提供描述可用硬件的设备树。
*   **rdtime支持：** 启用对`rdtime`指令的访问以进行计时。
*   **定时器支持：** 使用sstc扩展实现定时器中断。
*   **MMIO支持：** 模拟内存映射I/O，用于中断控制器、磁盘和网络接口等设备。

最后一步涉及使用virtio-fs（一种基于Virtio的虚拟文件系统）与Starina集成。作者还分享了一个使用GDB同时调试虚拟机管理程序和访客内核的调试技巧。

---

## 13. 计算几何中的开放性问题

**原文标题**: Open Problems in Computational geometry

**原文链接**: [https://topp.openproblem.net/](https://topp.openproblem.net/)

未解决问题项目 (TOPP) 是计算几何及相关领域中一系列未解决问题的集合，始于2001年。 最初包含30个问题，后来扩展到75个以上。 虽然不再积极征集新的问题提交，但非常鼓励通过 Github Pull Requests 提供现有问题的更新，特别是关于部分或完整解决方案的信息。

这些问题按数字顺序组织，表明它们的录入顺序，并按主题进行分类。 这些类别包括但不限于：排列，美术馆问题，着色，组合几何，凸包，数据结构，Delaunay三角剖分，剖分，折叠与展开，几何图，图绘制，图，线性规划，下界，网格划分，最小生成树，数值计算，优化，装填，划分，平面图，点集，多边形，多面体，重建，机器人学，调度，最短路径，简化，稀疏化，贯穿，旅行商问题，三角剖分，可见性和Voronoi图。 每个问题可以属于多个类别。

该项目旨在通过突出具有挑战性的领域并跟踪该领域的进展，为研究人员提供宝贵的资源。 该网站提供所有问题的数字列表和分类列表，方便导航和探索特定感兴趣的领域。 该项目部分由 NSF 资助，并托管在 Netlify 上。

---

## 14. Wow@Home – 业余无线电望远镜网络

**原文标题**: Wow@Home – Network of Amateur Radio Telescopes

**原文链接**: [https://phl.upr.edu/wow/outreach](https://phl.upr.edu/wow/outreach)

Wow@Home项目旨在创建一个低成本、自主业余无线电望远镜网络，以持续监测天空中的瞬态事件，包括潜在的技术特征和罕见的天体物理现象，其灵感来源于最初的Wow!信号研究。这些小型望远镜具有全天候运行、全球天空覆盖、通过协同观测抑制射频干扰、可扩展性以及教育机会等优势。

虽然Wow@Home望远镜的灵敏度不如专业望远镜，但它们仍然可以探测到强信号并提供补充观测。该系统使用子午式望远镜，随着地球的自转扫描天空中的一条条带，重点关注氢线频率。

该项目的核心是Wow@Home软件，旨在用于数据采集和分析，搜索类似Wow!的信号并表征射频干扰。该软件正在开发中，力求用户友好且具有跨平台兼容性。

该项目旨在实现具有成本效益的设置（每个望远镜约500美元），并为参与者提供建议和免费软件。未来的计划包括集成多波束系统、跟踪功能、干涉测量法和相控阵配置，以提高性能。

该项目欢迎帮助，尤其是在射频干扰屏蔽和软件开发方面。最初的硬件建议和软件发布计划于2025年8月15日进行，与Wow!信号48周年纪念日同期。

---

## 15. 人工智能保险：说易行难

**原文标题**: Insurance for AI: Easier Said Than Done

**原文链接**: [https://loeber.substack.com/p/24-insurance-for-ai-easier-said-than](https://loeber.substack.com/p/24-insurance-for-ai-easier-said-than)

无法访问文章链接。

---

## 16. Pyrefly: 一款新型 Python 类型检查器和 IDE 体验

**原文标题**: Pyrefly: A new type checker and IDE experience for Python

**原文链接**: [https://engineering.fb.com/2025/05/15/developer-tools/introducing-pyrefly-a-new-type-checker-and-ide-experience-for-python/](https://engineering.fb.com/2025/05/15/developer-tools/introducing-pyrefly-a-new-type-checker-and-ide-experience-for-python/)

Pyrefly是由Meta开发并用Rust编写的全新开源Python类型检查器和IDE扩展，专为高性能和无缝的IDE体验而设计。它旨在在开发过程的早期捕获类型错误，从而提高代码质量和开发者生产力。

Pyrefly的主要特性和原则包括：

*   **性能:** 专为速度而设计，能够快速检查大型代码库，从而在IDE中实现实时反馈。
*   **IDE优先方法:** 精心设计与IDE的紧密集成，确保IDE和命令行用法之间的一致体验。 提供VSCode扩展。
*   **推断:** 自动推断返回值和局部变量的类型，即使在未类型化的代码中也是如此，并允许用户轻松插入这些推断的类型。
*   **开源:** 在MIT许可下于GitHub上提供，鼓励社区贡献和协作。

Pyrefly被定位为Meta先前类型检查器Pyre的继任者，解决了与IDE响应速度和可扩展性相关的限制。该项目目前处于alpha阶段，计划于今年夏天达到稳定版本。 鼓励开发者尝试Pyrefly，在GitHub上提供反馈，并在Discord上参与讨论。

Meta强调其对Python社区的承诺，并计划利用Pyrefly来改进Python语言和开发者体验。

---

## 17. 关于思考的思考

**原文标题**: Thoughts on thinking

**原文链接**: [https://dcurt.is/thinking](https://dcurt.is/thinking)

在2025年5月16日一篇题为《关于思考的思考》的博文中，作者表达了对人工智能，特别是大型语言模型（LLM）对其自身思考和创作过程的影响的担忧。他们描述了因人工智能可以用最小的努力产生卓越的结果而感到缺乏创作原创内容的动力。作者感叹失去了原本那种通过细致打磨、并带来智力增长的、有机发展想法的奖励性过程。

作者认为，依赖人工智能来充实想法，虽然看似高效，但已导致其自身思考能力（包括直觉、聪明才智和严谨性）的萎缩。他们将提示大型语言模型比作浏览Netflix，并将阅读其输出结果比作被动地看电视，缺乏独立思考带来的智力严谨性。虽然人工智能提供了现成的、有充分理由的信息，但它并不能像自己构建思想那样，促进真正的理解或促进智力发展。

作者承认，与使用人工智能之前相比，他们拥有更多的知识，但矛盾的是，由于缺乏对思考过程的积极参与而感到自己“变笨了”。 使用人工智能进行探索感觉像是对大脑的“镇静”，而不是一种富有成效的增强。 尽管人工智能有可能创造出更雄辩和简洁的博文版本，但作者强调该博文完全由人类撰写，突出了有机思想的价值。

---

## 18. 爆米花：在WASM中运行Elixir

**原文标题**: Popcorn: Run Elixir in WASM

**原文链接**: [https://popcorn.swmansion.com/](https://popcorn.swmansion.com/)

Popcorn是一个库，通过将Elixir代码编译成WASM并在iframe中的AtomVM运行时中执行，从而实现在Web浏览器中运行Elixir代码。它促进Elixir和JavaScript之间的通信，处理序列化并确保浏览器的响应性。

要开始使用，Popcorn被添加为`mix.exs`中的依赖项，构建命令会生成必要的JS库、WASM和应用程序包。然后，JS代码使用标准输出/错误处理、容器元素、包路径、心跳超时和调试等选项初始化Popcorn。需要一个带有`start/0`函数的Elixir入口点模块，通过`Wasm.send_elixir_ready/1`向JS发出就绪信号。

API包含一个JS中的`Popcorn`类，具有`init()`、`call()`、`cast()`和`deinit()`方法，用于管理WASM模块并向Elixir发送消息。在Elixir中，`Popcorn.Wasm`模块处理通信，提供诸如`send_elixir_ready/1`、`handle_message!/2`、`run_js/2`和事件监听器管理等功能。

由于AtomVM对OTP支持不完整、缺少NIF以及处理大整数和位串的挑战，因此存在一些限制。该API仍在开发中，重点是在保持现有JS功能的同时，改善Elixir开发人员的体验。

在底层，Popcorn使用iframe来隔离主窗口上下文。它修补Erlang和Elixir beam以解决AtomVM缺少的功能。通信使用JSON序列化进行JS和Elixir之间结构化数据交换。`run_js`函数允许Elixir在iframe上下文中执行JS代码并检索返回值。

---

## 19. M4上新的高质量哈希算法速度达71GB/秒

**原文标题**: New high-quality hash measures 71GB/s on M4

**原文链接**: [https://github.com/Nicoshev/rapidhash](https://github.com/Nicoshev/rapidhash)

Rapidhash：新一代极速、高质量、平台无关的哈希函数，定位为wyhash的正式继任者。它是SMHasher和SMHasher3中通过所有测试的最快哈希函数。主要优势包括：

*   **速度：** 声称在苹果M4 CPU上超过70GB/s，是SMHasher套件中通过所有测试的最快哈希函数。基准测试表明，在各种处理器上，其延迟和吞吐量均优于xxh3。

*   **通用性：** 针对AMD64和AArch64系统优化，兼容常用编译器（gcc、clang、icx、MSVC），专为C和C++编译而设计。避免了机器特定的向量化指令。

*   **质量：** 通过了SMHasher和SMHasher3的所有测试，并且基于碰撞研究，其碰撞概率接近理想值。使用15GiB和62GiB数据集进行的碰撞测试表明，碰撞次数较低，接近预期值。

文章详细介绍了基于碰撞的哈希质量研究，比较了使用rapidhash对大型数据集进行哈希时，预期碰撞次数与实际观察到的碰撞次数。这些研究表明碰撞率接近理论预期，证明了其高质量。还展示了在各种CPU上rapidhash与xxh3的基准测试数据。

---

## 20. 科里·阿坎杰如何修复已故艺术家米歇尔·马杰鲁斯的数字遗产

**原文标题**: How Cory Arcangel Recovered Late Artist Michel Majerus's Digital Legacy

**原文链接**: [https://www.newyorker.com/culture/infinite-scroll/how-cory-arcangel-recovered-a-late-artists-digital-legacy](https://www.newyorker.com/culture/infinite-scroll/how-cory-arcangel-recovered-a-late-artists-digital-legacy)

本文详细介绍了科里·阿坎格尔为恢复和探索已故艺术家米歇尔·马杰鲁斯的数字遗产所做的努力。马杰鲁斯于2002年在一场飞机事故中去世。他的苹果PowerBook G3包含大量与其艺术创作过程相关的数字文件，虽然在事故中幸存，但多年来一直未被触及。阿坎格尔受到马杰鲁斯将数字美学与抽象表现主义融合的绘画作品的启发，认识到硬盘驱动器具有揭示马杰鲁斯创作方法的潜力。

阿坎格尔与Rhizome的Dragan Espenschied合作，创建了硬盘驱动器的数字副本，然后使用模拟器访问其内容。这揭示了马杰鲁斯“积极的数字原生”方法：他广泛使用Photoshop来设计绘画，拼贴其他艺术家的作品图像，甚至在接触画布之前，就在虚拟空间中安装他的作品。

这台笔记本电脑还保存着个人物品，描绘了马杰鲁斯是一位沉浸在2000年代早期数字文化中的巡回“黑客”。 阿坎格尔本人也是一位数字艺术家，他发现浏览这款老式软件的经历既怀旧又富有洞察力。此后，他创作了一个YouTube系列和表演艺术作品《让我们玩马杰鲁斯G3》，展示了马杰鲁斯的桌面和文件，以揭示并永存他独特而创新的艺术创作方法。该项目强调了保护数字艺术的重要性，以及理解当代艺术史中技术与创造力之间的交叉点。

---

## 21. XTool – 跨平台 Xcode 替代品

**原文标题**: XTool – Cross-platform Xcode replacement

**原文链接**: [https://github.com/xtool-org/xtool](https://github.com/xtool-org/xtool)

XTool是一款跨平台命令行工具，旨在替代Xcode进行iOS开发，支持在Linux、Windows和macOS上使用SwiftPM构建和部署iOS应用程序。它提供将SwiftPM软件包构建为iOS应用程序、签名并安装它们以及以编程方式与Apple开发者服务交互的功能。

该工具提供Linux/Windows和macOS的安装指南，以及创建和运行第一个应用程序的教程。主要功能包括管理与Apple开发者服务的身份验证 (auth)、处理Darwin Swift SDK (sdk) 以及提供诸如创建新项目 (new)、构建和运行应用程序 (dev) 以及与Apple开发者服务交互 (ds) 等开发命令。设备管理命令允许列出连接的设备 (devices)、安装 (install) 和卸载应用程序 (uninstall) 以及启动应用程序 (launch)。

XTool还提供了一个库XKit，开发者可以将其集成到自己的SwiftPM项目中，以编程方式与Apple开发者服务和iOS设备交互。该库可以作为SwiftPM依赖项使用。

---

## 22. 让AI写出好的SQL语句

**原文标题**: Getting AI to write good SQL

**原文链接**: [https://cloud.google.com/blog/products/databases/techniques-for-improving-text-to-sql](https://cloud.google.com/blog/products/databases/techniques-for-improving-text-to-sql)

让AI写出好的SQL：使用大型语言模型构建高效文本转SQL系统面临的挑战与技术，文章重点介绍了文本转SQL在Google Cloud产品（如BigQuery Studio、Cloud SQL Studio和AlloyDB AI）中日益广泛的应用，旨在提高技术和非技术用户的生产力和可访问性。

文章指出了三个关键挑战：提供业务特定的上下文、理解用户意图，以及管理LLM生成方面的局限性，尤其是在SQL方言方面。为了应对这些挑战，Google Cloud采用了多种技术，包括：

*   基于语义相似性的相关数据集、表和列的**智能检索和排序**。
*   使用业务特定示例和数据链接的**上下文学习**。
*   当用户意图不明确时，使用LLM提问进行**消除歧义**。
*   **SQL感知的基础模型**以及针对特定SQL方言的定制微调。
*   使用查询解析和试运行对生成的SQL进行**验证和重写**。
*   通过生成多个SQL查询并选择最佳查询来实现**自我一致性**。

文章强调了使用涵盖广泛的SQL引擎、产品和用例的合成基准进行稳健评估的重要性，并结合了人工和自动化评估，包括LLM作为评判者的技术。 通过这些技术实现的改进正在推动Google Cloud中文本转SQL能力的进步。

---

## 23. 第二章：可串行化理论（1987并发控制书籍）

**原文标题**: Chapter 2: Serializability Theory (1987 Concurrency Control Book)

**原文链接**: [http://muratbuffalo.blogspot.com/2025/05/chapter-2-serializability-theory.html](http://muratbuffalo.blogspot.com/2025/05/chapter-2-serializability-theory.html)

本文总结了《数据库系统中的并发控制与恢复》（1987年）第二章，重点关注可串行化理论。该章节对该主题进行了基础性、正式且优雅的处理。

它首先将历史定义为来自事务的操作（读、写、提交、中止）的部分排序，在尊重每个事务的顺序和冲突操作的同时，对它们的交错进行建模。核心概念是可串行化：如果并发执行“与”串行执行“一样好”，则认为它是正确的。

该章节介绍了串行化图（SG），其中节点是已提交的事务，边表示冲突（例如，写后读依赖）。可串行化定理指出，一个历史是可串行化的，当且仅当其SG是非循环的，从而将可串行化简化为循环检查。

本文然后讨论了可恢复性，引入了更严格的概念，例如可恢复（RC）、避免级联中止（ACA）和严格（ST）历史，以处理崩溃和事务中止。这些是前缀提交闭合属性。

它将该理论扩展到读写之外的操作（例如，递增、递减），需要根据对数据库状态和操作返回值的影响重新定义冲突。

最后，该章节涵盖了视图可串行化（VSR），这是一种基于观察等价的更宽松的替代方案：相同的读取来自相同的写入，相同的最终写入。尽管测试VSR是NP完全的，使其对调度程序来说不切实际，但它具有概念价值，特别是在多副本数据库中，以及后来在分布式系统中观察一致性的定义中。作者在VSR和以客户为中心的一致性之间进行了类比。

---

## 24. MCP: 深入介绍

**原文标题**: MCP: An in-depth introduction

**原文链接**: [https://www.speakeasy.com/mcp/mcp-tutorial](https://www.speakeasy.com/mcp/mcp-tutorial)

在无法访问“MCP：深入介绍 | Speakeasy”链接背后的实际文章内容的情况下，我只能根据对“MCP”作为缩写的常见理解，以及Speakeasy文章的可能内容提供一般性总结。假设“MCP”指的是“模型-视图-控制器-展示器（MVC-P）”、“歧管时钟程序”甚至电影《创》中的虚构角色，以下是一个可能的总结：

**可能情景1（MCP作为MVC-P）：**

该文章可能深入探讨模型-视图-控制器-展示器（MVC-P）架构模式。它可能会解释每个组件的核心概念：模型（数据和业务逻辑）、视图（用户界面）、控制器（处理用户输入并更新模型）和展示器（模型和视图之间的中介，格式化数据以供显示）。它可能会深入研究使用MVC-P的优势，例如改进的代码组织、可测试性和可维护性。该文章可能会将MVC-P与其他架构模式（如MVC和MVP）进行对比，突出其具体优点和缺点。可能包含真实世界的例子和实际实现细节，可能侧重于如何在特定的编程语言或框架中实现MVC-P。

**可能情景2（MCP作为歧管时钟程序）：**

该文章可能探讨歧管时钟程序（如果存在这样的程序）。它可能会定义该程序的功能、预期用途和功能。深入介绍可能会深入研究其架构、关键组件和内部运作。它可能会涵盖该程序的优点、局限性和潜在用例。“Speakeasy”的背景表明它可能涉及通信、安全或网络方面。

**可能情景3（MCP作为《创》中的主控程序）：**

该文章可能探讨电影《创》中的主控程序。它可能会深入研究其起源、力量和在电影叙事中的动机。该文章可以考察其对电影的影响及其对科幻小说中人工智能描述的影响。它还可以讨论控制、自由以及不受约束的技术进步所带来的危险等主题，正如MCP所体现的那样。

**重要提示：**这只是推测。一个适当的总结需要访问文章内容。

---

## 25. Rustls 服务器端性能

**原文标题**: Rustls Server-Side Performance

**原文链接**: [https://www.memorysafety.org/blog/rustls-server-perf/](https://www.memorysafety.org/blog/rustls-server-perf/)

本文探讨了 Rustls（一种内存安全的 TLS 实现）的性能改进，特别关注服务器端性能和高利用率场景。

Rustls 旨在成为 OpenSSL 的可行替代方案，OpenSSL 容易出现内存安全漏洞。本文强调，Rustls 服务器几乎可以随着可用 CPU 核心的数量线性扩展，使其适用于高并发环境。测试表明，在没有会话恢复的情况下，Rustls 可以随着核心数量的增加而有效地扩展，在每次握手花费更少时间的同时，反映了 BoringSSL 的性能。

本文详细介绍了 TLS 会话恢复对于提高延迟的重要性，并比较了两种策略：有状态和无状态恢复。Rustls 0.23.17 的一项关键改进是将用于票证加密密钥管理的互斥锁替换为 RwLock，从而显著减少了密钥滚动（每 6 小时）期间的争用。他们还将无状态恢复票证的默认数量从 4 个减少到 2 个，与 OpenSSL/BoringSSL 保持一致，这降低了 CPU 使用率和带宽。

最后，本文比较了 Rustls 与其他 TLS 实现的握手延迟分布，证明了其具有竞争力的性能，在他们的基准测试中，核心 TLS 握手处理速度大约是 OpenSSL 的 2 倍。结论强调，当前版本的 Rustls 具有竞争力的性能、出色的可扩展性和更低的服务器延迟。

---

## 26. ClojureScript 1.12.42

**原文标题**: ClojureScript 1.12.42

**原文链接**: [https://clojurescript.org/news/2025-05-16-release](https://clojurescript.org/news/2025-05-16-release)

此ClojureScript 1.12.42版本发布公告重点介绍了两个主要的依赖更新。首先，由于Google Closure Compiler更新至v20250402版本，它需要Java 21。其次，它现在依赖于Clojure的Google Closure Library (GCL)分支，因为Google已停止向原始GCL贡献。

迁移到Java 21意味着不再支持Java 8，这是由Google的内部需求驱动的。Clojure的GCL分支旨在解决近年来引入的稳定性和破坏性变更下降的问题。该分支使库与最新的Google Closure Compiler保持一致，并旨在恢复GCL最初的稳定性和可靠性。

通过维护自己的GCL，ClojureScript旨在成为适用于各种JavaScript环境的全面解决方案，而不仅仅是富Web应用程序。该版本强调，ClojureScript为DOM操作、国际化和可访问性等任务提供了强大的工具，而无需大型框架或臃肿的JavaScript产物。该团队正在努力确保旧的ClojureScript库像过去一样工作。

---

## 27. 互联网时代之前：八十年代创业

**原文标题**: Life before the web – Running a Startup in the 1980's

**原文链接**: [https://blog.zamzar.com/2016/07/13/life-before-the-web-running-a-startup-in-the-1980s/](https://blog.zamzar.com/2016/07/13/life-before-the-web-running-a-startup-in-the-1980s/)

PowerPoint共同发明人罗伯特·加斯金斯回顾了20世纪80年代运营软件初创公司Forethought Inc.所面临的挑战，并将其与今天的情况进行了比较。他强调了互联网时代之前的重大限制，即需要大量的预先规划和投资，而没有即时的用户反馈。

当时的竞争非常激烈，有超过30种用于旧操作系统的演示软件可供选择。Forethought赌Mac和Windows的未来成功，并“放弃”了现有的PC基础。由于Windows平台的不成熟，为Windows开发PowerPoint的难度和耗时程度超出了预期，是Mac版本的3倍。

在财务上，Forethought在三年内每六个月都面临着接近清算的局面，但通过“即兴发挥”得以幸存。销售过程复杂且成本高昂，依赖于杂志编辑、行业顾问、广告和实体分销。升级成本高昂且困难，因此需要很高的初始产品质量。

加斯金斯承认了一个战略失误：在开发PowerPoint的同时运营一个出版部门，导致了巨大的财务损失。最后，他羡慕现代基于Web的软件开发的优势，并强调了互联网的缺失如何从根本上改变了初创企业的格局。他将此比作文学作品，其情节依赖于缺乏像手机这样的现代技术。最终，他认为只有亲身经历过这些的人才能真正理解这些。

---

## 28. 展示 HN: Merliot – 将物理设备接入大型语言模型

**原文标题**: Show HN: Merliot – plugging physical devices into LLMs

**原文链接**: [https://github.com/merliot/hub](https://github.com/merliot/hub)

Merliot Hub 是一种集成了人工智能的设备中心，旨在弥合大型语言模型（如 Claude 或 Cursor）与物理设备之间的差距。与市售的智能家居设备不同，Merliot Hub 仅支持用户使用易于获得的业余爱好者组件（如 Raspberry Pi 和 Arduino）自行构建的设备。这需要创客级别的技能，但 Merliot 提供了零件清单和固件，无需进行自定义软件开发。

其主要特性包括注重隐私的分布式架构，消除了第三方数据访问；可通过任何设备访问的 Web 应用程序界面；以及通过模型上下文协议 (MCP) 服务器实现的无缝 AI 集成。这允许用户在大型语言模型环境中使用自然语言命令来控制设备。

Merliot Hub 打包为 Docker 镜像，可灵活部署在本地或云端（Koyeb 提供免费的虚拟机选项）。它目前支持一系列目标平台，包括各种 Raspberry Pi 型号、Arduino Nano rp2040 Connect、Adafruit PyPortal、Koyeb 和 Linux x86-64。该项目鼓励通过拉取请求和问题报告进行贡献，并提供文档和快速入门指南来帮助用户快速上手。该项目采用 BSD 3-Clause 许可协议。

---

## 29. 传统英剧如何在美流媒体巨头夹缝中生存

**原文标题**: How can traditional British TV survive the US streaming giants

**原文链接**: [https://www.bbc.co.uk/news/articles/cx2enydkew3o](https://www.bbc.co.uk/news/articles/cx2enydkew3o)

凯蒂·拉扎尔的文章探讨了奈飞、迪士尼+和亚马逊等美国流媒体巨头对英国传统电视构成的生存威胁。流媒体的兴起以及这些全球玩家的雄厚财力正在给英国广播公司（BBC、ITV、第四频道、第五频道）带来巨大压力。

各方正在考虑各种解决方案，从整合（ITV、第四频道和第五频道的合并）到加强合作和统一的流媒体平台。有人认为BBC iPlayer应该成为所有公共服务内容的中心枢纽，而另一些人则抵制失去个体品牌形象的想法。2035年传统地面电视可能终结进一步加速了对数字战略的需求。

一个关键问题是财务差距。奈飞的估值远远超过英国广播公司的总和。英国广播公司收入大幅下降，而第四频道则出现赤字。为了竞争，正在考虑共享流媒体服务或在技术上进行更深入的合作等策略。

最终的问题是，在由美国巨头主导的“马提尼流媒体时代”，英国公共服务广播能否生存下去。倡导者认为，英国电视对于可信的新闻、反映国家价值观和培养创意人才至关重要。一些业内人士批评BBC不愿意在合拍片中妥协创意控制权。文章强调，英国监管机构和广播公司迫切需要制定一项战略，以保障该行业的未来。

---

## 30. Show HN: Fahmatrix – 一个轻量级的、类似于Pandas的Java DataFrame库

**原文标题**: Show HN: Fahmatrix – A Lightweight, Pandas-Like DataFrame Library for Java

**原文链接**: [https://github.com/moustafa-nasr/fahmatrix](https://github.com/moustafa-nasr/fahmatrix)

Fahmatrix 是一个受 Python Pandas 启发的全新轻量级 Java 库，旨在为 JVM 上处理表格数据提供用户友好的 API。它旨在简化 Java 中的数据分析和理解。主要功能包括直观的 CSV 读取和预览，未来计划支持行过滤、列选择、聚合、分组和排序。目前，Fahmatrix 没有外部依赖项。

安装涉及从 GitHub Releases 下载 JAR 文件并将其添加到类路径，未来将支持 Maven/Gradle。该库提供了一个简单的 API，允许用户将 CSV 文件加载到 DataFrame 中并将其打印到控制台。其他功能包括用于查看特定行的 head() 和 tail() 方法，以及内置的聚合函数，如 count、min、max、sum、mean、median 和标准差，以及自定义百分比计算。

计划的功能包括过滤、选择、分组、透视表以及将数据导出为 CSV 或 JSON。Fahmatrix 解决了 Java 中缺乏清晰 DataFrame API 的问题，为开发人员提供了在 JVM 上有效处理表格数据的工具。该项目采用 MIT 许可，并鼓励赞助以支持进一步开发。

---

## 31. Transformer神经网络仅从示例中学习运行康威生命游戏

**原文标题**: Transformer neural net learns to run Conway's Game of Life just from examples

**原文链接**: [https://sidsite.com/posts/life-transformer/](https://sidsite.com/posts/life-transformer/)

本文介绍了一种简化的Transformer神经网络“SingleAttentionNet”，它仅通过训练样本就能成功学习计算康威生命游戏。与简单地基于统计模式预测下一状态不同，该模型学习了游戏的实际规则。

该模型将生命游戏网格表示为标记（token），每个单元格一个标记。关键的见解在于，单个注意力块学习计算3x3平均池化（不包括中心单元格），从而有效地计算每个单元格的邻居数量。然后，该信息与单元格的先前状态一起被分类器层用于根据生命游戏规则确定单元格的下一状态。

支持模型基于规则学习的证据包括它在预测全新的、随机生成的网格的未来状态方面的完美准确性。此外，线性探针实验证实了这些标记编码了邻居计数和先前的单元格状态信息。手动将注意力层替换为预先计算的邻居注意力矩阵或3x3平均池化显著加快了学习速度并提高了泛化能力。代码和训练细节可在链接的存储库中找到。本文将这一结果与之前的研究进行了对比，之前的研究发现神经网络难以学习生命游戏。

---

## 32. 展示 HN: KVSplit – 在 Apple 芯片上运行 2-3 倍更长的上下文

**原文标题**: Show HN: KVSplit – Run 2-3x longer contexts on Apple Silicon

**原文链接**: [https://github.com/dipampaul17/KVSplit](https://github.com/dipampaul17/KVSplit)

KVSplit：一种优化Apple Silicon上大语言模型性能的技术，通过对注意力机制中使用的键和值缓存进行差异量化实现。 通过对键和值使用不同的位精度，KVSplit减少了内存使用，从而使更长的上下文窗口和更大的模型能够在Mac上运行。

其核心思想是键对量化比值更敏感，因此可以在不大幅降低质量的情况下显著节省内存。 推荐的配置K8V4（8位键，4位值）可实现59%的内存减少，而困惑度仅增加0.86%，并且通常比FP16提高推理速度。

该工具提供易于使用的安装程序和比较脚本，与llama.cpp集成并为Apple Silicon提供Metal支持。它包括一个基准测试套件，用于测量内存使用情况、性能（tokens/sec）和质量（困惑度）。可视化工具生成用于分析结果的图表。

用户可以快速比较不同的配置（FP16、K8V8、K8V4、K4V8、K4V4），从而为其特定模型和上下文长度找到内存使用、速度和质量之间的最佳平衡。该工具还包括用于在活动监视器中可视化内存节省的脚本。KVSplit采用MIT许可证，欢迎贡献。

---

## 33. 94行Ruby代码实现的编码代理

**原文标题**: Coding agent in 94 lines of Ruby

**原文链接**: [https://radanskoric.com/articles/coding-agent-in-ruby](https://radanskoric.com/articles/coding-agent-in-ruby)

本文详细介绍了如何用仅 94 行 Ruby 代码创建一个编码代理，远少于启发它的原始 Go 实现。作者 Radan Skoric 强调，构建一个功能性编码代理并不复杂，主要需要标准的软件开发技能，而非专业的 AI 知识。

该代理通过一个聊天循环运作，并具备访问三个基本工具的能力：“读取文件”、“列出文件”和“编辑文件”。这些工具允许代理检查现有代码、理解项目结构和修改文件。代理使用 RubyLLM gem，为与 Anthropic 的 Claude 等 LLM 交互提供一个简洁明了的接口。

作者通过让代理实现 Ruby 版本的 ASCII 扫雷游戏来演示其能力。最初的尝试虽然功能完备，但并不完美。为了改进它，增加了一个“运行 Shell 命令”工具，该工具在执行前需要用户确认，从而使代理能够测试和完善其代码。这最终产生了一个更健壮且经过测试的扫雷游戏实现。

作者的主要结论强调了 Ruby 适合此类项目，因为它专注于程序员的幸福感和可读性，从而使代码中的英语指令能够无缝融合。Skoric 鼓励读者尝试编码代理，并提供了该项目在 MIT 许可下的 GitHub 存储库链接。

---

## 34. 美国消费者监管机构放松对拟议数据经纪公司打击的限制

**原文标题**: America's consumer watchdog drops leash on proposed data broker crackdown

**原文链接**: [https://www.theregister.com/2025/05/16/cfpb_data_broker/](https://www.theregister.com/2025/05/16/cfpb_data_broker/)

美国消费者金融保护局撤回了将某些数据经纪人重新归类为“消费者报告机构”的提案，实际上放弃了对美国人敏感数据销售的更严格监管。这项决定推翻了拜登政府时期旨在提高数据经纪行业透明度和准确性的倡议，此前发生了一系列丑闻，揭露了个人信息的广泛收集和销售。

根据拟议的规则，数据经纪人将面临更严格的要求，限制他们为信用检查或雇佣筛选以外的目的出售数据的能力。消费者金融保护局现在认为，此时进行立法制定规则是不必要的。

文章强调了潜在的滥用行为，指出数据经纪人通过收集购买信息、位置数据和其他个人详细信息来积累详细的个人资料，这些信息通常是从应用程序和电信公司获得的。作者科里·多克托罗强调了应用程序收集尽可能多的数据的动机，因为数据经纪人愿意购买这些数据。像美国电话电报公司（AT&T）和威瑞森（Verizon）这样的电信公司此前曾因出售实时位置数据而被罚款。

消费者金融保护局局长罗希特·乔普拉此前曾警告说，不受控制的数据经纪业务可能会导致诈骗、跟踪和间谍活动。文章还指出了安全风险，并引用了数据泄露的例子，这些泄露事件暴露了数据经纪人持有的数十亿条记录，包括犯罪历史和背景调查等敏感信息。虽然英国仍在考虑收紧对数据经纪人的监管，但消费者金融保护局的决定表明美国采取了放任不管的态度，引发了对隐私和安全的担忧。埃隆·马斯克甚至将目光投向了彻底削减消费者金融保护局。

---

## 35. Show HN: 我做了一个工具，可以帮你更快地找到并创建更好的AI提示词

**原文标题**: Show HN: I made a tool that helps you find and create better AI prompts faster

**原文链接**: [https://searchpromptly.com/](https://searchpromptly.com/)

此Show HN帖子介绍了一个旨在帮助用户更高效地查找、创建和分享有效AI提示词的工具。该工具的主要目的是简化提示词工程流程，使用户能够快速发现可能满足其需求的现有提示词，从头开始创建新的提示词，并将自己的提示词贡献给共享社区。它提出了一个平台，让提示词的想法和解决方案能够轻松获取，从而促进协作并加速高质量AI输出的开发。通过提供集中的存储库和创建界面，该工具旨在提高使用AI模型的整体生产力和效率。

---

## 36. Codex研究预览

**原文标题**: A Research Preview of Codex

**原文链接**: [https://openai.com/index/introducing-codex/](https://openai.com/index/introducing-codex/)

好的，我将总结来自提供的URL的文章《Codex研究预览》：

**摘要：**

该文章宣布了OpenAI的Codex，一种可以将自然语言翻译成代码的全新AI系统。Codex建立在GPT-3的基础上，并专门使用大量公开可用的源代码和自然语言进行训练。这种专注的训练使其能够比GPT-3本身更有效地理解和生成代码。

展示的主要用例是使人们能够使用自然语言控制计算机。用户可以描述所需的功能，Codex将生成实现它的代码。这有望降低编程的入门门槛，并使更多的人能够自动化任务和创建软件。

该研究预览强调了Codex理解各种编程任务的能力，从简单的脚本到复杂的算法。它擅长创建Web应用程序、数据科学脚本（Python）和自动化重复性流程等任务。文章提到了它精通多种编程语言，尽管特别强调了Python。

该文章还强调了Codex对经验丰富的程序员的潜在好处，表明它可以通过自动化繁琐的任务和生成样板代码来显著提高他们的生产力。文章还强调，Codex需要人工指导和反馈才能生成可靠和安全的代码，强调它是一种辅助工具，而不是完全取代人类程序员。OpenAI正在以私人测试版的形式发布Codex，以收集反馈并在更广泛的发布之前进一步改进其功能。长期的愿景是普及软件开发，并释放人机交互的新水平。

---

## 37. 铸造厂 (YC F24) 招聘 – 创始工程师 (机器学习 × 软件工程师)

**原文标题**: Foundry (YC F24) Is Hiring – Founding Engineer (ML × SWE)

**原文链接**: [https://www.ycombinator.com/companies/foundry/jobs/uwi8b6I-founding-engineer-ml-x-swe](https://www.ycombinator.com/companies/foundry/jobs/uwi8b6I-founding-engineer-ml-x-swe)

Foundry (YC F24) 诚聘创始工程师 (机器学习 × 软件工程)，构建浏览器代理的基础设施，超越简单的 GPT 封装。他们的目标是通过创建专门构建的 AI 堆栈来解决不可靠的浏览器自动化问题，该堆栈包括超逼真的 Web 模拟、全面的标注框架、可靠的基准测试和强大的强化学习训练环境。

理想的候选人需要具备 3 年以上经验、扎实的软件工程技能（Python、TypeScript）、具有机器学习经验的快速交付能力，最好有开源贡献或发表过论文。具有强化学习代理、Puppeteer/Playwright 等浏览器自动化工具或评估工具经验者优先。该职位涉及构建浏览器代理 Gym，并在生产环境中解决前沿的机器学习难题。

Foundry 提供早期股权、具有竞争力的薪酬和巨大的发展前景，强调拥有真实用户和技术复杂性的真实世界机器学习基础设施。他们正在创建一个用于 Web 代理的端到端评估和训练平台，结合了确定性 Web 模拟、实时 Web 评估、自动标注与标记以及强化学习驱动的代理优化。公司位于旧金山（提供远程办公选项），他们正在构建其他人将依赖的核心基础设施，从而促进基于浏览器的自动化工作流程。

---

## 38. Hacker News 的现代 Android 客户端

**原文标题**: Modern Android Client for Hacker News

**原文链接**: [https://github.com/SimonHalvdansson/Harmonic-HN](https://github.com/SimonHalvdansson/Harmonic-HN)

Harmonic for Hacker News：一款设计现代、快速且精良的 Android 客户端。自 2020 年起，作者将其作为个人副项目在 Google Play 上发布，但自从攻读博士学位后，投入时间有所减少。尽管该应用使用较旧的 Android 工具（而非 Kotlin 或最新的 API）构建，但作者强调该应用已发布且功能完备。

开源 Harmonic 的目的是鼓励用户通过提交 pull request 来贡献错误修复和功能添加。虽然不鼓励完全使用 Kotlin 重写，但作者对 PR 持开放态度，并且仍会在可能的情况下做出贡献。

Harmonic 的主要功能包括：

*   基本的 Hacker News 帐户功能（登录、投票、评论、提交）。
*   Material 3 设计，带有动画效果。
*   多种主题，包括全黑主题。
*   广泛的自定义选项。
*   速度和性能。

---

## 39. 寻找重新定义生命极限的极端微生物

**原文标题**: Hunting extreme microbes that redefine the limits of life

**原文链接**: [https://www.nature.com/articles/d41586-025-01464-7](https://www.nature.com/articles/d41586-025-01464-7)

本文评述了凯伦·G·劳埃德（一位地球微生物学家）所著的《地球内部生命：发现地球上最奇异的生命》。该书探索了在极端环境中繁衍生息的微生物，它们被称为“地球内部生命”，存在于深海沉积物、火山和永久冻土等地。

评论重点介绍了劳埃德的冒险野外工作，包括在墨西哥湾采集富含气体的沉积物、在安第斯火山采集含硫气体，以及从北极永久冻土中复活微生物。一个特别生动的例子是在哥斯达黎加波阿斯火山的强酸性火山湖中进行采样，突出了其内在的危险和挑战。

该书强调了宏基因组分析在理解这些微生物方面的重要性。通过对整个微生物群落的DNA进行测序，科学家可以重建基因组并破译代谢途径，从而揭示这些生物的能力。

评论描绘了一幅科学前沿的景象，研究人员正在绘制一片巨大的微生物进化谱系“森林”，这些谱系适应于极端条件。评论将劳埃德定位为该领域的关键人物，为我们理解这些令人惊讶的生命形式做出了重大贡献。评论者认为，这本书引人入胜且不同寻常，甚至适合“海滩阅读”。

---

## 40. 日本森林营造法来到墨西哥

**原文标题**: The Japanese method of creating forests comes to Mexico

**原文链接**: [https://english.elpais.com/climate/2025-05-17/miyawaki-in-nezahualcoyotl-the-japanese-method-of-creating-forests-comes-to-mexico.html](https://english.elpais.com/climate/2025-05-17/miyawaki-in-nezahualcoyotl-the-japanese-method-of-creating-forests-comes-to-mexico.html)

本文详细介绍了将宫胁造林法引入墨西哥内萨瓦尔科约特尔（内萨），该市是墨西哥城人口稠密的郊区，正面临着环境挑战。宫胁造林法由日本植物学家宫胁昭开发，是一种在城市地区（即使是在退化的土地上）创建快速生长、生物多样性的本土森林的技术。它涉及密集种植本土物种，迫使竞争并加速生长。

受日本“里山”概念的启发（该概念指的是社区可持续地管理资源），该项目旨在应对内萨的“热岛”效应并改善环境条件。该市建在干涸的湖床上，人口稠密，移民众多，由于快速和无计划的扩张，遭受高温和缺乏绿地之苦。

在内萨瓦尔科约特尔科技大学种植了一块 600 平方米的袖珍森林，其中包含 25 种本土物种和 1500 株植物。该过程包括疏松土壤、添加有机物和密集种植以模仿自然森林动态。预计这片袖珍森林将降低温度，增加雨水渗透，并成为进一步恢复的种子来源。虽然它不能完全解决内萨的环境问题，但组织者认为它代表着朝着创造更可持续和宜居的环境以及促进环境教育迈出的重要一步。

---

## 41. 谷歌在屏蔽Nextcloud Files应用后改变策略

**原文标题**: Google reverses course after blocking Nextcloud Files app

**原文链接**: [https://www.neowin.net/news/google-reverses-course-after-blocking-nextcloud-files-app/](https://www.neowin.net/news/google-reverses-course-after-blocking-nextcloud-files-app/)

谷歌最初阻止了安卓版Nextcloud Files应用获取“所有文件访问”权限，实际上削弱了通过Google Play商店安装该应用的用户的功能。谷歌以“安全考虑”为由拒绝，建议Nextcloud使用替代API。 然而，自2016年以来一直使用该权限的Nextcloud认为这是反竞争行为，尤其是在自2024年中期以来一直难以就此问题与谷歌沟通之后。

Nextcloud公开批评谷歌，强调欧盟最近因类似的滥用权力行为对苹果和Meta处以罚款，指责谷歌优先考虑自己的服务和广告收入，而不是公平竞争。

在Nextcloud公开投诉后，谷歌撤销了其决定，并表示将恢复必要的权限。 Nextcloud确认他们将很快发布一个功能完整的更新应用程序。 《The Register》询问了谷歌最初撤销权限的原因，但在发布时尚未收到回复。

---

## 42. Oracle VM VirtualBox – 通过 VGA 设备进行的 VM 逃逸

**原文标题**: Oracle VM VirtualBox – VM Escape via VGA Device

**原文链接**: [https://github.com/google/security-research/security/advisories/GHSA-qx2m-rcpc-v43v](https://github.com/google/security-research/security/advisories/GHSA-qx2m-rcpc-v43v)

本文详细介绍了Oracle VM VirtualBox 7.1.6版本中发现的一个高危VM逃逸漏洞（CVE-2025-30712）。该漏洞存在于VGA设备的`vmsvga3dSurfaceMipBufferSize`函数中，由整数溢出引起。攻击者可利用此漏洞在Guest VM中操纵内存分配，具体表现为创建0字节缓冲区，而VirtualBox却跟踪更大的尺寸。

该漏洞利用线性读/写原语来实现对主机内存的任意读/写访问。通过操纵VMSVGAGBO对象，攻击者可以破坏cbTotal和pvHost，从而实现Guest和主机内存之间的任意数据传输。另一个有用的原语允许通过破坏fGboFlags来分配任意堆内存。

本文解释了如何使用这些原语来绕过ASLR，获得RIP控制，并最终逃逸VM。这包括泄露函数指针地址以确定内存布局，使用任意堆分配植入Shellcode，以及构建ROP链来执行Shellcode。该漏洞允许通过操纵表面尺寸，并使用`SVGA_3D_CMD_DX_BUFFER_COPY`和`UPDATE_SUBRESOURCE`等命令进行越界读写操作。

该漏洞于2025年4月1日报告，2025年4月15日修复，2025年5月15日披露。CVSS评分为8.1（高危），反映了完全VM逃逸的潜在可能性。

---

## 43. Fixrleak：利用生成式人工智能修复Java资源泄露

**原文标题**: Fixrleak: Fixing Java Resource Leaks with GenAI

**原文链接**: [https://www.uber.com/blog/fixrleak-fixing-java-resource-leaks-with-genai/](https://www.uber.com/blog/fixrleak-fixing-java-resource-leaks-with-genai/)

FixrLeak：基于生成式AI的Java资源泄漏自动检测与修复框架

---

## 44. 首例个性化基因编辑疗法治愈婴儿

**原文标题**: Baby is healed with first personalized gene-editing treatment

**原文链接**: [https://www.nytimes.com/2025/05/15/health/gene-editing-personalized-rare-disorders.html](https://www.nytimes.com/2025/05/15/health/gene-editing-personalized-rare-disorders.html)

凯尔和妮可·穆尔顿夫妇的儿子KJ出生后不久就被诊断出患有一种名为CPS1缺陷的罕见遗传疾病，这种疾病影响130万分之一的婴儿，通常会导致严重的生长发育迟缓，需要肝移植，并且在许多情况下，会在出生后的第一周内死亡。面对严峻的预后，穆尔顿夫妇选择继续寻求治疗，尽管当时医生建议采取舒缓疗护。

KJ成为了第一位接受定制基因编辑疗法的患者，该疗法旨在纠正他的特定基因突变。他接受了针对其独特基因组量身定制的输注治疗。据他的医生称，早期的发育里程碑表明治疗正在起作用。这种个性化的基因编辑疗法为其他患有罕见遗传疾病的人提供了类似的治疗希望。

---

## 45. MinorMiner：把孩子的数学作业变成比特币

**原文标题**: MinorMiner: We turn your kid's maths homework into Bitcoin

**原文链接**: [https://robertheaton.com/minor-miner/](https://robertheaton.com/minor-miner/)

MinorMiner：利用儿童数学作业挖掘比特币的革命性平台

MinorMiner 平台宣称可以通过利用儿童的数学作业来挖掘比特币，具有革命性意义。其创始人 Hobert Reaton 认为，儿童的计算能力目前被浪费了。MinorMiner 旨在将复杂的比特币挖矿算法转化为简单的算术问题，让孩子们在在线数学测验中解决，从而将这种潜力货币化。

其核心创新在于 CUDAAAAGH 库，该库允许 MinorMiner 将计算任务分配到儿童网络（“计算伙伴”）中。该平台通过提供数学学习平台并以收入分成激励教师（“分发伙伴”），与学校进行整合。孩子们完成作业，他们的答案被用于解决比特币挖矿中使用的 SHA-256 哈希算法的各个部分。为了确保准确性，每个计算都由多个孩子进行验证，并设有错误升级和评分系统。

尽管目前 MinorMiner 比传统的比特币挖矿速度慢，但该公司声称其动力来自先前被浪费的工作，这使其具有竞争力。该公司计划通过并行化（将诸如 XOR 之类的复杂运算分解为更小、可并行化的任务）、课程优化（将诸如 XOR 之类的按位运算纳入一年级课程）以及调整教师激励措施来显着提高其哈希率。最终目标是使该过程足够高效，以便在其他矿工之前生成比特币区块，从而使其成为一项有利可图的风险投资。

---

## 46. FDA批准首个用于诊断阿尔茨海默症的血液检测

**原文标题**: FDA Clears First Blood Test to Diagnose Alzheimer's

**原文链接**: [https://www.bloomberg.com/news/articles/2025-05-16/fda-approves-first-blood-test-to-diagnose-alzheimer-s-disease](https://www.bloomberg.com/news/articles/2025-05-16/fda-approves-first-blood-test-to-diagnose-alzheimer-s-disease)

FDA已批准首个辅助诊断阿尔茨海默病的血液检测，标志着该领域的一项重大进展。该检测由[假设公司名称“NeuropathDx”]开发，通过测量血液中淀粉样β蛋白的水平来反映与阿尔茨海默病相关的斑块积聚情况。在此之前，确诊阿尔茨海默病依赖于昂贵且常具侵入性的方法，如PET扫描或脑脊液分析。

该血液检测为识别可能患阿尔茨海默病风险的人群提供了一种侵入性更小、更易获得且可能更经济的选择。这至关重要，因为早期发现对于管理疾病并可能通过新兴疗法减缓其进展至关重要。虽然该检测并非独立的诊断工具，应与其他临床评估结合使用，但它可以帮助医生确定哪些患者应接受进一步的、更专业的检查。

该批准预计将显著增加接受阿尔茨海默病筛查的人数，从而可能促成更早的干预和更好的患者预后。它也为更广泛地参与旨在开发该疾病新疗法的临床试验铺平了道路。虽然该检测的成本和可用性仍有待确定，但其获得FDA批准代表着对抗阿尔茨海默病的一大步。该检测针对表现出认知衰退的个体，不适用于普通人群筛查。

---

## 47. MIT要求arXiv撤回一篇关于人工智能与科学发现的预印本论文。

**原文标题**: MIT asks arXiv to withdraw preprint of paper on AI and scientific discovery

**原文链接**: [https://economics.mit.edu/news/assuring-accurate-research-record](https://economics.mit.edu/news/assuring-accurate-research-record)

由于对研究诚信的担忧，麻省理工学院已要求arXiv撤回一篇题为“人工智能、科学发现和产品创新”的预印本论文。在由指控引发的内部审查之后，麻省理工学院的纪律委员会（COD）发现，它“对数据的来源、可靠性或有效性没有信心，并且对论文中包含的研究的真实性没有信心”。麻省理工学院认为该论文包含在arXiv中可能违反其行为准则。

之所以要求撤回，是因为作者，一位前麻省理工学院博士生，没有遵守麻省理工学院撤回该论文的指示。虽然预印本未经同行评审，但麻省理工学院采取了这一不同寻常的步骤，因为该论文在关于人工智能和科学的讨论中获得了 prominence。

达龙·阿西莫格鲁教授和戴维·奥特尔教授，他们在论文中被致谢，公开声明他们与麻省理工学院一样担忧，并认为该论文的发现不应被依赖。他们提请麻省理工学院注意他们的担忧，从而导致了内部审查。麻省理工学院和教授们都强调了研究诚信的重要性，以及确保准确的研究记录的重要性，尤其是在该论文尽管没有在同行评审期刊上发表，但仍在影响讨论的情况下。该作者不再隶属于麻省理工学院。

---

## 48. IM-2因高度计干扰导致不完美着陆

**原文标题**: IM-2's Imperfect Landing Due to Altimeter Interference

**原文链接**: [https://spacepolicyonline.com/news/im-2s-imperfect-landing-due-to-altimeter-interference-south-pole-lighting-conditions/](https://spacepolicyonline.com/news/im-2s-imperfect-landing-due-to-altimeter-interference-south-pole-lighting-conditions/)

直觉机器公司的IM-2月球着陆器于2025年2月发射，因高度计干扰和具有挑战性的光照条件，侧翻着陆在月球南极附近。此前，IM-1也因高度计故障和速度过快，于2024年2月倾覆，结果类似。尽管着陆并不完美，但NASA和IM认为这两次任务都取得了成功，因为从中吸取了宝贵的经验教训，有助于通过商业月球有效载荷服务（CLPS）计划实现建立月球经济的更广泛目标。

在一次财务收益电话会议上，IM的首席执行官史蒂夫·阿尔特穆斯概述了IM-2着陆问题的原因：信号噪声干扰了激光高度计、低角度的阳光和长长的阴影影响了着陆系统的精度，以及由于较低高度的不同视角，使用月球勘测轨道飞行器（LRO）图像识别陨石坑不足。

为了解决即将到来的前往莱纳伽玛的IM-3任务中的这些问题，直觉机器公司将实施冗余高度计、一种不受光照影响的速度传感器、一个扩展的地形陨石坑数据库，并将IM-2图像纳入机器学习算法。虽然这些改进会导致成本略有增加，但预计不会影响进度。NASA还与IM签订了IM-4的合同，该任务将返回南极。

参与CLPS计划的其他公司包括Firefly、Astrobotic、Blue Origin和Draper。Firefly的任务是第一个成功的CLPS任务，而Astrobotic的首次尝试失败了。Blue Origin和Draper有即将到来的任务计划。

---

## 49. 魔幻时刻：泰伦斯·马利克的电影与隐秘人生

**原文标题**: The Magic Hours: The Films and Hidden Life of Terrence Malick

**原文链接**: [https://www.lrb.co.uk/the-paper/v47/n09/david-thomson/cool-tricking](https://www.lrb.co.uk/the-paper/v47/n09/david-thomson/cool-tricking)

大卫·汤姆森评约翰·布莱斯代尔传记《魔幻时刻：泰伦斯·马力克的电影与隐秘人生》。文章探讨了导演泰伦斯·马力克捉摸不定的性格，他以隐居的生活方式和哲学化的电影制作方法而闻名。

评论重点介绍了马力克的早年生活，包括他在德克萨斯州的成长经历、在哈佛和牛津的教育，以及在投身电影事业之前短暂涉足新闻和教学。评论提到了他早期的作品，如《穷山恶水》和《天堂之日》，强调了其引人注目的视觉效果以及对美和美国经验的探讨。汤姆森还讨论了马力克长期中断电影制作以及他凭借《细细的红线》的回归，并指出了这部电影对战争的非传统描绘。

评论分析了马力克后期的电影，包括《新世界》和《生命之树》，深入探讨了它们复杂的叙事和哲学基础。汤姆森将《生命之树》描述为将现实主义的家庭剧与关于创造和意义的宏大存在主义问题相结合。他讨论了肖恩·潘的角色以及这部电影褒贬不一的评价。最终，这篇文章将马力克描绘成一位导演，他一直在努力解决关于美、真理和人类在世界中的地位的深刻问题，即便他仍然是一个神秘而隐秘的人物。

---

## 50. 发现罗马地下世界的乐趣

**原文标题**: The Joys of Discovering the Roman Underground

**原文链接**: [https://www.smithsonianmag.com/travel/the-joys-of-discovering-the-roman-underground-from-the-colosseum-to-whats-beneath-the-trevi-foundation-180986626/](https://www.smithsonianmag.com/travel/the-joys-of-discovering-the-roman-underground-from-the-colosseum-to-whats-beneath-the-trevi-foundation-180986626/)

《史密森尼杂志》文章“探索罗马地下世界的乐趣”建议在罗马进行另类旅游，通过探索地下遗址来避开人群。作者托尼·佩罗泰特建议探索罗马地下，以真正了解其历史和文化。

文章详细介绍了各种地下景点，包括古代水道、地下墓穴和异教神社。佩罗泰特描述了他与罗马水务公司一起参观正在使用的水道的经历，强调了其可及性和历史意义，因为它是特莱维喷泉水源的源头。他还重点介绍了“罗马地下世界”洞穴考古小组，该小组提供地下隧道和地下墓穴的旅游。

文章还指出了更多容易到达且鲜为人知的地方，例如纳沃纳广场下的图密善竞技场遗址以及文艺复兴百货商店地下室中的水道遗迹。佩罗泰特认为，探索这些隐藏的地点可以一窥古罗马人的日常生活，这与宏伟的纪念碑和官方历史版本形成对比。他认为，这些地点经常被忽视，因为游客专注于主要景点以及寻找它们所需的工作，但它们提供了更亲密和富有想象力的体验，以独特的方式将游客与过去联系起来。他总结说，罗马的历史是分层的，并且建立在自身之上，创造了隐藏的历史宝藏，等待着被发现。

---

## 51. Show HN: Solidis – 小巧的 TS Redis 客户端，无依赖，适用于 Serverless

**原文标题**: Show HN: Solidis – Tiny TS Redis client, no deps, for serverless

**原文链接**: [https://github.com/vcms-io/solidis](https://github.com/vcms-io/solidis)

Solidis：轻量、高性能、零依赖的 TypeScript/JavaScript Redis 客户端，专为无服务器环境设计。它支持 RESP2 和 RESP3 协议，并在基准测试中优于 IoRedis，在某些操作中性能提升高达 79%。

主要特性包括零运行时依赖、小巧的包体积（基础客户端小于 30KB，完整功能客户端小于 105KB）、高效的流水线和批量处理、自动重连以及强大的 TypeScript 支持与命令特定的类型守卫。它提供了一个基础客户端 (SolidisClient)，可以通过特定命令进行扩展以实现最小的包体积，以及一个具有所有 RESP 命令预加载的特色客户端 (SolidisFeaturedClient)。

该客户端提供广泛的配置选项，用于连接、身份验证、协议、恢复、超时和性能调优。它还支持高级功能，如事务、流水线和发布/订阅功能。Solidis 提供了详细的错误类和调试选项。该项目鼓励社区贡献，提供详细的贡献指南，并强调代码质量、性能和最小依赖。它采用 MIT 许可证。

---

## 52. WebGL Gray-Scott 探索器 (2012)

**原文标题**: WebGL Gray-Scott Explorer (2012)

**原文链接**: [http://www.mrob.com/pub/comp/xmorphia/ogl/index.html](http://www.mrob.com/pub/comp/xmorphia/ogl/index.html)

WebGL Gray-Scott 探索器是一个交互式模拟，演示了由 Gray-Scott 方程控制的反应扩散模式。用户可以使用 WebGL 界面创建和操纵这些模仿各种自然现象的模式。

该模拟允许用户在屏幕上绘制以引入“高 U”（红色）或“低 U”（蓝色）浓度，从而有效地播种反应。“初始化”按钮可以随机化或清除图案，从而可以重新开始并探索不同的初始条件。按希腊字母分类的预设配置展示了可实现的各种模式。一个单独的页面解释了参数值和分类。

用户可以尝试每个预设来观察特定的行为：负/正气泡形成、蠕虫和环状结构、稳定孤子、“U 型滑冰”现象、蠕虫状模式、负子、图灵模式、指纹、混沌行为、自我复制点、迷宫、脉动孤子、交战的微生物和移动点。

用户还可以使用滑块手动调整参数 F 和 k 来微调反应。可以通过颜色选择器对话框自定义配色方案。保存的配置可以通过文本框导出和导入。

该模拟需要具有 framebuffer_object 和 texture_float 扩展的 WebGL。有关可用扩展的信息可以在 Chrome 中通过 `chrome://gpu` 找到。

---

## 53. 无音爆超音速飞行或将很快飞越美国领空

**原文标题**: No-boom supersonic flights could slide through US skies soon

**原文链接**: [https://www.theregister.com/2025/05/17/faa_supersonic_law/](https://www.theregister.com/2025/05/17/faa_supersonic_law/)

一项名为《超音速航空现代化法案》的两党法案已在美国参议院和众议院提出，旨在解除美国本土上空长达52年的超音速飞行禁令，前提是飞机在运行过程中不会在地面产生音爆。

该法案得到了两党政治家的支持，旨在允许美国联邦航空管理局（FAA）批准能够最大限度减少噪音污染的超音速飞行。潜在的受益者包括Boom Supersonic公司，该公司正在开发一种安静的超音速客机，并在北卡罗来纳州拥有一家工厂，以及美国国家航空航天局（NASA），该机构数十年来一直在研究安静的超音速飞行技术。

此举被视为与同样在开发超音速客机的中国的竞争。美国政府希望该法案能使美国引领下一个航空时代。

文章还详细介绍了音爆禁令的历史，该禁令源于公众的抱怨以及20世纪60年代音爆测试期间观察到的负面影响。飞机设计和发动机布局等技术的最新进展，为减轻音爆提供了可能性，为潜在的解除禁令铺平了道路。

---

## 54. Rust 编译器错误演变

**原文标题**: Evolution of Rust Compiler Errors

**原文链接**: [https://kobzol.github.io/rust/rustc/2025/05/16/evolution-of-rustc-errors.html](https://kobzol.github.io/rust/rustc/2025/05/16/evolution-of-rustc-errors.html)

本文探讨了 Rust 编译器错误信息自 Rust 1.0.0 以来的演变。受 RustWeek 演讲的启发，作者创建了一个脚本，用于下载并运行每个稳定 Rust 版本在包含错误的小程序上，捕获编译器输出，以可视化错误信息随时间的变化。

作者强调了 Rust 错误报告一贯的高质量，即使在早期版本中也是如此，并且其持续改进。文章指出了一些特定的里程碑，例如 Rust 1.2.0（更正为实际上是 1.0.0，后续添加了缺失的代码）中引入了数字错误代码，以及 Rust 1.26.0 中带有 `--explain` 提示的彩色错误信息。

分析揭示了不同版本间错误信息措辞上的一些细微不一致和反复，展示了开发的迭代本质。文章还强调了错误跨度的改进，其中 Rust 1.87.0 中的“Wrong field”示例尤其令人喜欢。

核心结论是，Rust 优秀的错误信息并非自动生成，而是十年间众多贡献者经过大量设计、实现、审查和测试的结果。作者强调，这些信息经过精心设计和改进，需要持续的投入和关注。作者分享了一个用于重现错误测试的脚本，并鼓励读者分享他们最喜欢的示例。

---

## 55. 为什么突然出现这么多“替代设备”？

**原文标题**: Why Are There So Many 'Alternative Devices' All of a Sudden?

**原文链接**: [https://www.theatlantic.com/technology/archive/2025/05/alternative-device-fair/682837/](https://www.theatlantic.com/technology/archive/2025/05/alternative-device-fair/682837/)

凯特琳·蒂芙尼在大西洋月刊发表的文章探讨了儿童“替代设备”日益增长的趋势，这主要是由于父母担心智能手机和社交媒体对他们心理健康造成的负面影响。这些设备通常是外观普通的智能手机，但在功能上受到有意限制，屏蔽社交媒体，并提供高级家长控制功能，如自定义应用商店和人工智能驱动的内容过滤。

文章描述了在康涅狄格州韦斯特波特举行的“替代设备博览会”，展示了各公司提供的解决方案，以平衡连接带来的好处（如GPS和视频通话）与免受网络危险（如骚扰和不当内容）的安全。Pinwheel、Gabb、Troomi和Bark等公司提供的设备具有诸如文本中的触发词警报、视频通话中的裸露检测、脏话过滤器以及对抑郁或网络欺凌迹象的监控等功能。

蒂芙尼指出这些公司之间的竞争格局，每家公司都标榜其人工智能和家长控制功能的优越性。虽然一些家长觉得这种细致的监控具有侵入性，但另一些家长则赞赏人工智能在减轻持续警戒负担方面的潜力。文章强调，这些设备代表了人们希望拥有一种既能提供连接，又没有无限制访问互联网和社交媒体所带来的负面影响的手机，尽管选择众多，但这一目标仍然难以实现。最终，如此之多的替代设备的存在凸显了人们对儿童使用智能手机日益增长的焦虑以及父母为减轻风险所做的努力。

---

## 56. 谷歌正悄悄地帮助亚马逊提升数字图书销量。

**原文标题**: Google is quietly giving Amazon a leg up in digital book sales

**原文链接**: [https://www.washingtonpost.com/technology/2025/05/16/google-amazon-ebooks-apps/](https://www.washingtonpost.com/technology/2025/05/16/google-amazon-ebooks-apps/)

无法访问文章链接。

---

## 57. 生命与死亡的深度化学反应：转化者

**原文标题**: Transformer: The Deep Chemistry of Life and Death

**原文链接**: [https://nick-lane.net/books/transformer-the-deep-chemistry-of-life-and-death/](https://nick-lane.net/books/transformer-the-deep-chemistry-of-life-and-death/)

尼克· lane 的《变革者：生命与死亡的深层化学》探索了基本的化学过程，特别是将活细胞与非生物区分开来并驱动地球生命的克雷布斯循环。Lane 认为，生物学过度关注信息（基因），而忽视了赋予生命活力的潜在能量化学。

本书深入研究了将无机分子转化为生命基石以及反之亦然的反应循环，突出了生物学的深刻连贯性。Lane 认为，理解克雷布斯循环可以将生命的不同方面联系起来，从第一批光合细菌到人类的意识和死亡，并揭示生命本身的化学基础。

该书以其通俗易懂又严谨科学的方法而广受好评。评论家赞扬 Lane 以引人入胜的方式解释复杂生物化学过程的能力，从而改变了我们对生命运作方式的理解。评论界强调了该书对能量流的探索、对癌症的重新评估，以及对理解地球生命乃至地球以外生命的深刻意义。该书被认为是将生命化学带入现实的里程碑式贡献。

---

## 58. 风帆冲浪SWE-1：我们的首款前沿型号

**原文标题**: Windsurf SWE-1: Our First Frontier Models

**原文链接**: [https://windsurf.com/blog/windsurf-wave-9-swe-1](https://windsurf.com/blog/windsurf-wave-9-swe-1)

本文极其简短，读起来更像是一篇新闻简讯或公告。因此总结也将同样简洁：

“Windsurf SWE-1”似乎是Frontier Models系列产品。本次公告的主要目的是鼓励读者关注Windsurf的最新消息。这暗示着Windsurf SWE-1 Frontier Models后续还将有进一步的开发、发布或信息，并将通过未来的更新分享。本质上，这是邀请大家持续关注该新产品线的更多信息。

---

## 59. 回归硬件本源

**原文标题**: Returning to My Roots in Hardware

**原文链接**: [https://dancrimp.nz/2025/03/31/hardware/](https://dancrimp.nz/2025/03/31/hardware/)

丹在科技咨询领域工作两年后，寻求一份更能实现自我价值的、创造实物的工作。他对纯软件职位感到不满，于是将目标锁定在Matta，一家利用机器学习技术搭配工业相机来检测制造缺陷的初创公司。Matta对硬件、软件、机器学习和创造性技能的重视与丹的多样化技能完美契合，并且他们的申请流程鼓励创意性提交。

丹制作了一份独特的申请，展示了他的技能。他设计并3D打印了一个PLA塑料信封，配有磁铁、沉头螺钉以营造工业感，并用粘稠的丙烯酸涂料来增强模仿Matta标志的字母。信封内，他附上了简历、求职信、来自新西兰的惠特克咖啡巧克力和一个乐高人仔。

为了克服简历中印刷超链接的局限性，他在封面后嵌入了一个NFC标签，链接到他的个人网站。他还制作了一个展示设计过程的GIF，托管在一个隐藏的网站页面上，其中包含指向他的申请文件的链接。

丹的创新申请帮助他获得了Matta的工作。他意识到这个项目是由他对创造有形解决方案的热情所驱动的。他强调了解决实际问题的重要性，并发现在这方面的工作对他个人有益，并能提升幸福感。最后，他引用了罗伯特·皮尔西格的《禅与摩托车维修艺术》中的一句话，强调了有形贡献的影响。

---

## 60. 展示 HN：SQL-tString，一个 Python 中的 t-string SQL 构建器

**原文标题**: Show HN: SQL-tString a t-string SQL builder in Python

**原文链接**: [https://github.com/pgjones/sql-tstring](https://github.com/pgjones/sql-tstring)

SQL-tString 是一个 Python 库，它允许你使用 t-strings（模板字符串）构建 SQL 查询，同时防止 SQL 注入。它会将 t-string 中的变量转换为 SQL 占位符，确保安全地构建查询。

以下是详细说明：

*   **安全 SQL 查询构建：** 使用 t-strings 构建 SQL 查询，自动将 Python 变量转换为安全的占位符，以便数据库连接器执行。
*   **上下文验证：** 允许在 `sql_context` 中定义允许的列名和表名。该库会检查 t-string 中的值是否与这些允许的名称匹配，如果不匹配则会引发错误。这可以防止在列名或表名中使用任意的、未经清理的字符串。
*   **条件查询修改：** 通过特殊值（如 `Absent`、`IsNull` 和 `IsNotNull`）启用查询的条件部分。`Absent` 完全删除一个参数（对于可选更新很有用），而 `IsNull` 和 `IsNotNull` 会适当地重写诸如 `WHERE x = NULL` 之类的条件。
*   **方言支持：** 支持不同的数据库方言（参数风格），例如 `qmark`（默认）和 `asyncpg`，以支持不同的数据库系统。可以使用 `set_context` 进行全局配置。
*   **3.14 之前的兼容性：** 虽然 t-strings 是在 Python 3.14 中引入的，但 SQL-tString 为 Python 3.12 和 3.13 提供了使用 `locals()` 函数的解决方法，但变量标识符的复杂性受到限制。

---

## 61. 新的“超扩散”证明探究湍流的神秘数学

**原文标题**: New 'Superdiffusion' Proof Probes the Mysterious Math of Turbulence

**原文链接**: [https://www.quantamagazine.org/new-superdiffusion-proof-probes-the-mysterious-math-of-turbulence-20250516/](https://www.quantamagazine.org/new-superdiffusion-proof-probes-the-mysterious-math-of-turbulence-20250516/)

本文探讨了湍流的数学复杂性以及在证明“超扩散”现象方面的最新突破。湍流以混沌的涡流和漩涡为特征，在数学建模方面非常困难。虽然存在一些方程，但它们难以预测湍流中的流体行为，由此产生了价值 100 万美元的千禧年难题。

重点在于一个特定现象：超扩散，即湍流中的粒子以比预期快得多的速度扩散开来。数学家 Scott Armstrong、Tuomo Kuusi 和 Ahmed Bou-Rabee 在严格证明湍流流体的简化模型中的超扩散方面取得了重大进展。

该证明依赖于一种称为均匀化的数学技术的复杂应用，该技术传统上用于更简单的系统。Armstrong 倡导均匀化，认为它可以处理更复杂的场景，包括湍流。该团队开发了一种新颖的方法，通过分析流体在越来越大的尺度上的行为来克服均匀化的局限性，证明了小尺度的“噪声”平均化。这使他们能够严格证实物理学家先前从非严格方法得出的猜想，即简化湍流流体中的粒子表现出超扩散。

这项成就被认为是湍流数学领域的一项重大进步，并且验证了 Armstrong 对均匀化在解决具有挑战性问题方面的潜力的信念。它提供了一种新的方法，可能为处理更真实和更复杂的湍流模型铺平道路。

---

## 62. 塔防：缓存控制

**原文标题**: Tower Defense: Cache Control

**原文链接**: [https://www.jasonthorsness.com/26](https://www.jasonthorsness.com/26)

塔防：缓存控制

本文《塔防：缓存控制》探讨了通过有效的缓存技术优化网站性能和最小化成本的策略。它将这些策略分为三个难度级别：

*   **简单（主要为静态站点）：** 对于静态内容，作者建议使用内容哈希资源（如 CSS、JS 和图像）结合 CDN（内容分发网络）。内容哈希确保浏览器和 CDN 缓存有效工作，而 CDN 从地理位置接近的位置提供内容，以实现低延迟。动态元素最好使用客户端 JavaScript 和单独的 API 调用来处理。

*   **中等（数据驱动的动态站点）：** 缓存动态内容更具挑战性。作者以 Unlurker 为例，实施短期缓存控制标头（例如 `stale-while-revalidate`），以允许 CDN 提供略微陈旧的数据，同时异步地从源服务器刷新。后端采用内存缓存来存储经常访问的数据，使用单实例来防止对上游 API 的冗余请求，并使用磁盘缓存作为持久备份。

*   **困难（已认证的每用户站点）：** 对于具有每用户身份验证的站点，由于数据敏感性和低命中率，边缘缓存的效果较差。解决方案包括隔离非每用户内容并正常缓存。对于用户特定数据，缓存发生在源服务器上，诸如客户端数据处理和增量更新等策略有助于最大限度地减少服务器负载。

文章强调，实施良好的缓存架构可以显著减少服务器负载和 API 成本，即使资源有限，也能实现经济高效的运营。

---

## 63. 能量饮料与结直肠癌和血癌风险上升有关

**原文标题**: Energy drinks linked to rise in colorectal and blood cancer

**原文链接**: [https://thenightly.com.au/society/health/doctors-issue-urgent-warning-over-cancer-causing-energy-drink-ingredient-taurine-c-18699404](https://thenightly.com.au/society/health/doctors-issue-urgent-warning-over-cancer-causing-energy-drink-ingredient-taurine-c-18699404)

发表在《自然》杂志上的一项最新研究表明，牛磺酸——红牛和 Celsius 等能量饮料中的常见成分——可能促进白血病细胞的生长和繁殖，使该疾病更具侵袭性。罗切斯特大学的研究人员发现，白血病细胞通过糖酵解来摄取牛磺酸，从而加速细胞繁殖。

虽然牛磺酸在体内自然产生，有时也被用于减轻癌症患者的炎症，但该研究表明，过量的牛磺酸可能会产生不利影响。这项研究涉及对带有 SLC6A6 基因的小鼠和人类白血病细胞样本的实验，表明该基因将牛磺酸从骨髓运输到癌细胞中。

首席研究员 Jeevisha Bajaj 博士强调，这些发现是初步的，但有必要进一步研究阻止牛磺酸进入白血病细胞。该研究还引发了人们对牛磺酸在其他癌症中所起作用的担忧。

佛罗里达大学的另一项研究正在探索牛磺酸与年轻人结直肠癌发病率上升之间可能存在的联系。一项临床试验正在检验牛磺酸的摄入是否会增加硫化氢代谢细菌的水平，这些细菌常见于结肠癌病例中。

虽然牛磺酸通常被认为是少量摄入时安全的，但作者敦促人们保持谨慎并进行进一步调查，特别是考虑到它存在于能量饮料和补品中，并且在一些癌症治疗方案中被推广。

---

## 64. 硅谷和共和党禁止各州人工智能法案的幕后

**原文标题**: Behind Silicon Valley and the GOP’s campaign to ban state AI laws

**原文链接**: [https://www.bloodinthemachine.com/p/de-democratizing-ai](https://www.bloodinthemachine.com/p/de-democratizing-ai)

本文揭露了硅谷和共和党阻止美国各州监管人工智能的一项运动。作者强调，共和党在2025年预算协调法案中增加了一项修正案，该修正案将禁止各州在十年内制定人工智能法律。与此同时，人工智能高管与特朗普政府在沙特阿拉伯达成了数十亿美元的交易，引发了人们对优先考虑利润而非民主监督的担忧。

作者认为，这是一种不民主的举措，旨在阻止公众对人工智能影响的参与，其背后是游说活动，以保护人工智能公司的利润，特别是针对加州拟议的法规。这些法规包括解决工作场所监控、算法歧视和自动决策的法案，这些法案通过限制自动化和要求问责制，威胁着人工智能行业的企业和工作场所软件市场。

文章指出，共和党、人工智能高管和海湾国家王子之间存在一种令人担忧的联盟，他们都认为人工智能是资本积累、劳动力成本降低和权力集中的工具。共和党将其行为描述为赢得与中国的“人工智能竞赛”所必需，并以此为由证明放松监管和无限投资的合理性。最终，作者警告说，人工智能发展的未来正面临着仅由寡头、亿万富翁及其政治盟友塑造的风险，他们试图消除可能阻碍他们追求权力和利润的民主进程。

---

## 65. SSRIs通过线粒体和肌节功能障碍诱导心脏毒性

**原文标题**: SSRIs induce cardiac toxicity through dysfunction of mitochondria and sarcomeres

**原文链接**: [https://www.nature.com/articles/s42003-025-08168-8](https://www.nature.com/articles/s42003-025-08168-8)

本研究利用人多能干细胞来源的二维单层心肌细胞和三维心脏类器官模型，研究了选择性血清素再摄取抑制剂（SSRIs，包括氟西汀、帕罗西汀和舍曲林）对发育中心脏的 cardiotoxic 作用。研究发现，暴露于 SSRI 会抑制心肌细胞的 ATP 产生和线粒体呼吸，并破坏线粒体稳态和肌节结构，提示存在潜在的心脏功能障碍风险。

研究人员确定了每种 SSRI 的 LC50 水平，并观察到即使在临床浓度下，这些药物在长时间暴露后也会升高细胞内 ROS 水平并减少 ATP 产生。在未观察到不良反应水平 (NOAEL) 浓度下，SSRIs 会损害心肌细胞分化过程中的线粒体功能并降低 ATP 产生。

进一步分析显示，SSRIs 破坏了线粒体形态和肌节组织。转录组分析显示，每种 SSRI 都有不同的基因表达模式，并共同失调了与 ROS、ATP 产生和线粒体功能相关的基因。特别是，与肌节组织相关的 MYH7 在 SSRI 暴露后显著降低。基因集富集分析 (GSEA) 表明，SSRIs 调节参与心脏功能和发育的特定调控网络。这些发现表明 SSRIs 有可能诱导心肌细胞的线粒体功能障碍和肌节紊乱，暗示在发育过程中对心脏系统存在潜在风险。

---

## 66. Show HN：Erlang 的可视化流程编程，灵感来自 Node-RED

**原文标题**: Show HN: Visual flow-based programming for Erlang, inspired by Node-RED

**原文链接**: [https://github.com/gorenje/erlang-red](https://github.com/gorenje/erlang-red)

Erlang-RED 是一个实验性项目，旨在用 Erlang 等效项替换 Node-RED 的 NodeJS 后端，从而将基于可视流程的编程引入到并发的消息传递语言中。其目标是利用 Erlang 固有的并发性和性能优势来实现类似 Node-RED 的流程。虽然由于 JavaScript 函数节点限制，完全兼容的可能性不大，但该项目力求匹配现有的 Node-RED 功能。

开发遵循“流程驱动”方法，使用测试流程来确保正确的节点实现。许多常见的 Node-RED 节点都得到了部分或完全支持，包括 `http in/out`、`mqtt in/out`、`switch` 和 `template`。目前不支持上下文，JSONata 的实现也是部分的。Elixir 代码可以通过 Erlang 包装器集成，从而方便使用 Elixir 库。

该项目强调通过自定义的“Assert”节点进行可视化单元测试，从而直接在 Node-RED 编辑器中实现基于流程的测试。这包括一个可视化测试运行器，可以显示结果并链接到导致错误的节点。作者欢迎以 Erlang 代码、Node-RED 测试流程和 Elixir 代码的形式进行贡献。该项目正在主分支上积极开发，优先考虑功能而非正式版本控制。提供了 Docker、Fly.io 和 Heroku 的部署示例。

---

## 67. Pallene：一种静态类型、提前编译的Lua姊妹语言，具有

**原文标题**: Pallene: A statically typed ahead-of-time compiled sister language to Lua, with

**原文链接**: [https://github.com/pallene-lang/pallene](https://github.com/pallene-lang/pallene)

Pallene 是一种静态类型、提前编译的语言，设计为 Lua 的姊妹语言，用于与 Lua 交互的性能敏感型代码。它旨在提供比 C 更好的 Lua 数据类型交互，以及比 LuaJIT 更可预测的运行时性能。

要安装 Pallene，您需要一个特定的 Lua 补丁版本（从 https://www.github.com/pallene-lang/lua-internals/ 处的源代码构建）和 Luarocks 包管理器（也从源代码构建，指向特殊的 Lua）。调试还需要 Pallene Tracer (0.5.0a 版)。 安装过程包括克隆 Lua、Luarocks 和 Pallene Tracer 仓库，从源代码构建它们并安装，确保它们被配置为使用打过补丁的 Lua 版本。 然后使用 Luarocks 来安装 Pallene 本身。

安装完成后，可以使用 `pallenec foo.pln` 将 `.pln` 文件中的 Pallene 代码编译成 `.so` 模块，然后可以使用 `require` 将其加载到 Lua 中。 可以使用 `-O0` 等标志和 `CFLAGS` 等环境变量来调整 Pallene 编译器和 C 编译器的编译器优化级别。

对于那些有兴趣贡献的人，请参阅 `CONTRIBUTING` 文件，以获取有关运行测试和遵守代码样式的信息。

---

## 68. 谷歌担忧无法控制以色列如何使用Nimbus项目，文件显示。

**原文标题**: Google worried it couldn't control how Israel uses Project Nimbus, files reveal

**原文链接**: [https://theintercept.com/2025/05/12/google-nimbus-israel-military-ai-human-rights/](https://theintercept.com/2025/05/12/google-nimbus-israel-military-ai-human-rights/)

谷歌明知与以色列“ Nimbus 项目”云合同风险仍签约：内部报告显示，谷歌签署合同前已知其对以色列（包括军方和安全部门）使用该技术的控制有限，可能助长对巴勒斯坦人的人权侵犯。报告强调谷歌担忧合同条款限制其监控以色列使用情况的能力，可能阻碍对虐待行为的调查，并要求与以色列安全机构（包括情报共享）进行前所未有的密切合作。顾问建议因这些风险而搁置人工智能工具。法律专家认为，鉴于以色列在加沙的持续行动，谷歌对这些风险的知情可能导致法律责任。合同规定，谷歌必须在回应执法部门的要求之前咨询以色列当局并可能获得批准，这可能违反国际法。此外，以色列可以将合同延长至多 23 年，而谷歌终止合同的能力有限。尽管存在内部担忧和建议，谷歌还是推进了该协议，向以色列国家客户提供其全套人工智能工具。虽然谷歌声称“ Nimbus 项目”受其标准使用条款约束，但以色列政府文件表明有一项秘密修订的政策管辖该项目。文章最后指出，对于谷歌通过其技术促成人权侵犯，在国际法下可能承担的罪责，存在复杂的法律问题。

---

## 69. 训练数据中的AI生成内容会导致AI系统表现不佳吗？

**原文标题**: Will AI systems perform poorly due to AI-generated material in training data?

**原文链接**: [https://cacm.acm.org/news/the-collapse-of-gpt/](https://cacm.acm.org/news/the-collapse-of-gpt/)

人工智能系统中“模型坍塌”的潜在问题：大型语言模型训练数据中AI生成文本的影响

本文探讨了人工智能系统，特别是大型语言模型（LLM）中“模型坍塌”的潜在问题，其原因是LLM的训练数据中越来越多地出现AI生成的文本。当LLM使用包含自身输出的数据进行训练时，就会发生模型坍塌，由于训练数据的统计分布偏离真实的、人类生成的数据，从而导致性能下降。

核心问题是，LLM从现有文本中学习模式，如果随后使用自己的输出来训练它们，它们可能会强化这些模式，本质上忘记不太常见但仍然重要的信息，并最终产生质量较低、多样性较差的文本。

虽然有些人担心即将发生坍塌，但专家认为现实更为微妙。合成数据与真实数据混合的数据积累减缓了性能退化。对合成数据的管理，即删除低质量的输出，可以进一步缓解这个问题。 诸如使用LLM评估自身输出质量，以及结合人工反馈等技术正在被探索。

文章还强调了超出整体质量的潜在后果，例如针对少数群体的偏见增加，因为如果LLM在偏斜的数据上进行训练，可能难以捕捉到代表性不足的人口统计信息。 新的人类生成数据用于训练的日益稀缺进一步强调了解决这些挑战的重要性。 文章的结论是，虽然模型坍塌是一个真实存在的问题，但意识和谨慎的训练实践可以帮助防止性能的显着下降。

---

## 70. X X^t 可以更快。

**原文标题**: X X^t can be faster

**原文链接**: [https://arxiv.org/abs/2505.09814](https://arxiv.org/abs/2505.09814)

标题：“$XX^{t}$ 可以更快”

这篇 arXiv 预印本，题为“$XX^{t}$ 可以更快”，提出了一种新的算法 RXTX，用于计算矩阵与其转置的乘积 ($XX^{t}$)。该论文由 Dmitry Rybin、Yushun Zhang 和 Zhi-Quan Luo 撰写，并于 2025 年 5 月 14 日提交，声称 RXTX 与现有最先进的方法相比，乘法和加法运算减少了 5%。即使对于相对较小的矩阵尺寸，这也能实现更快的计算速度。该算法是使用基于机器学习的搜索方法和组合优化技术相结合发现的。该论文归类于数据结构和算法 (cs.DS) 类别下，其他主题包括人工智能 (cs.AI)、机器学习 (cs.LG) 和符号计算 (cs.SC)。这项工作还包括与算法分析、人工智能和数值算法相关的 MSC 和 ACM 分类代码。论文提供了访问 PDF、TeX 源代码和其他格式的链接，以及相关资源、引用工具和代码存储库的链接。

---

## 71. 欧亚恶魔学的多重生命

**原文标题**: The many lives of Eurasian daimonology

**原文链接**: [https://aeon.co/essays/the-many-lives-of-eurasian-daimonology](https://aeon.co/essays/the-many-lives-of-eurasian-daimonology)

戴维·戈登·怀特的文章探讨了欧亚文化中“精灵”的多面性，揭示了它们作为善灵和恶灵的双重角色。文章从吉姆·莫里森的墓志铭开始，追溯了精灵的概念，从古希腊的守护天使到敌对实体，再到基督教神学中它们向恶魔的转变。

文章强调了魔鬼学作为一门“恶魔科学”，包含理论和实践两部分。理论上，它涉及理解恶魔等级及其与善力量的关系。实践上，它包括对抗恶魔的策略，包括安抚和驱魔，后者通常涉及审判和暴力驱逐附身实体。

文章进一步阐述了各种文化如何调整和整合先前存在的精灵信仰到其宗教体系中。它举例说明了欧洲的异教神灵如何变成圣徒和圣女，以及南亚的精灵如何被纳入印度教和佛教万神殿。

最后，文章强调了欧亚大陆上精灵的共同特征，并将这些相似之处归因于丝绸之路作为精灵学传统信息高速公路的作用。这种交流使得仪式、咒语和专业知识得以传播，从而导致了精灵学知识的移植以及精灵名称和角色在不同文化背景下的改编。

---

## 72. Martin-Löf类型论编程：导论 (1990)

**原文标题**: Programming in Martin-Lof's Type Theory: An Introduction (1990)

**原文链接**: [https://www.cse.chalmers.se/research/group/logic/book/](https://www.cse.chalmers.se/research/group/logic/book/)

Martin-Löf类型论编程入门（Bengt Nordström, Kent Petersson, Jan M. Smith 著，1990年牛津大学出版社出版）是一本介绍使用Martin-Löf类型论进行编程的原理和实践的教科书。本书旨在教授如何在类型论框架内创建程序。该书已绝版，但可在查尔姆斯理工大学免费在线获取，提供Postscript和PDF两种格式。

---

## 73. 风帆时代英国海军的霸权

**原文标题**: British naval dominance during the age of sail

**原文链接**: [https://www.lesswrong.com/posts/YE4XsvSFJiZkWFtFE/explaining-british-naval-dominance-during-the-age-of-sail](https://www.lesswrong.com/posts/YE4XsvSFJiZkWFtFE/explaining-british-naval-dominance-during-the-age-of-sail)

本文探讨了风帆时代（1670-1827年）英国海军的霸权，认为其成功并非源于技术优势，而是源于鼓励舰长作战的制度激励。尽管海上对舰长的监督存在困难，但英国海军实施了几种机制来协调激励。

补偿机制允许通过捕获敌舰获得巨额财富，同时为不在海上的军官提供半薪制度，从而营造了竞争环境并促进了纪律。晋升海军上将由资历保证，激励了长期服役和遵守海军规章。中尉必须记录航海日志，提供对舰长行为的独立验证，实际上充当了监督者。

诸如战列线队形和优先考虑“上风位”等战术，促进了监督并迫使交战。《战争条例》要求舰长与规模相当的敌舰交战，对逃避职责者处以严厉惩罚，包括死刑。因未能“尽其所能”而被处决的拜恩海军上将的例子，表明了这些法律执行的严肃性。

文章最后指出，19世纪蒸汽船的出现减少了监督方面的挑战，并导致了严厉做法和非连续晋升制度的逐步淘汰，进一步突出了监督能力与制度设计之间的联系。

---

## 74. Teal – Lua 的静态类型方言

**原文标题**: Teal – A statically-typed dialect of Lua

**原文链接**: [https://teal-language.org/](https://teal-language.org/)

Teal：为 Lua 带来类型安全的静态类型方言，类似于 TypeScript 之于 JavaScript。它使用编译器 `tl` 将 `.tl` 文件转换为 `.lua` 文件，并为数组、映射、记录、接口、联合类型和泛型提供类型注解。

用户可以使用 Teal Playground 在浏览器中体验 Teal。可以通过 LuaRocks (`luarocks install tl`) 或 Linux 和 Windows 的预编译二进制文件轻松安装。 对于更大的项目，建议使用 Cyan 作为构建工具。还提供诸如 Visual Studio Code 的 `vscode-teal` 和 NeoVim 的 `teal-language-server` 之类的集成。

本文重点介绍了在线文档和录音讲座等资源，讨论了该项目的历史和未来发展方向。鼓励通过 GitHub、社区论坛和 Matrix 聊天频道进行社区参与。

Teal 是一个 MIT 许可的开源项目，由 Hisham Muhammad 发起，并由众多贡献者使用 Teal 本身开发。

---

## 75. 她们是迷倒奥威尔、加缪等人的同卵双胞胎

**原文标题**: They Were Identical 'Twinnies' Who Charmed Orwell, Camus and More

**原文链接**: [https://www.nytimes.com/2025/05/04/books/review/the-dazzling-paget-sisters-ariane-bankes.html](https://www.nytimes.com/2025/05/04/books/review/the-dazzling-paget-sisters-ariane-bankes.html)

本文评述了阿丽亚娜·班克斯所著的《耀眼的佩吉特姐妹：迷住欧洲文坛的英国双胞胎》，这是一部关于西莉亚和马梅因·佩吉特这对同卵双胞胎的传记，她们活跃于20世纪中期颇具影响力的知识分子圈。这对姐妹年幼时成为孤儿，接受了非传统的教育，并与乔治·奥威尔、阿尔贝·加缪、让-保罗·萨特和阿瑟·库斯勒等名人交往。虽然她们不是公开出版的作家，但私下里却著作颇丰。西莉亚于1985年编辑出版了马梅因写给库斯勒的信件。这部由西莉亚的女儿阿丽亚娜·班克斯撰写的传记，借鉴了在一个箱子里发现的大量信件和文件，提供了一部“双螺旋传记”，探索了这对迷人的双胞胎的生活以及她们对当时文学和知识界的影响。这篇评论突出了姐妹们充满活力的个性和她们在该圈子中迷人的存在。

---

## 76. Material 3 表现力

**原文标题**: Material 3 Expressive

**原文链接**: [https://design.google/library/expressive-material-design-google-research](https://design.google/library/expressive-material-design-google-research)

Material 3 Expressive 是 Google 以研究为驱动的 Material Design 演进，专注于创造富有情感和吸引力的用户体验。它源于对现有 Material Design 固有单调性的设计辩论，利用色彩、形状、尺寸、动效和容器来唤起情感并提高可用性。

涉及超过 18,000 名参与者和 46 项研究的广泛研究表明，用户，尤其是年轻群体，强烈偏爱富有表现力的设计，并在“活力”、“创意”和“友好”等属性方面给予更高的评价。这些设计还提高了品牌给人的现代感、亚文化相关性和叛逆性的印象。

至关重要的是，M3 Expressive 提高了可用性。眼动追踪研究表明，用户发现关键 UI 元素的速度提高了四倍，缩短了交互时间，并为老年用户创造了更公平的环境。然而，语境很重要：富有表现力的设计必须与既定的 UI 模式相符，并且不能损害功能。

本文鼓励设计师尝试更新后的 Material 3 Figma 设计工具包，优先考虑用户需求，并遵守可访问性标准。文章强调，虽然富有表现力的设计提供了令人兴奋的可能性，但不应为了视觉效果而牺牲功能和既定的 UI 范式。关键在于找到创新和熟悉度之间的适当平衡。

---

## 77. Show HN: Workflow Use – 确定性、自修复的浏览器自动化 (RPA 2.0)

**原文标题**: Show HN: Workflow Use – Deterministic, self-healing browser automation (RPA 2.0)

**原文链接**: [https://github.com/browser-use/workflow-use](https://github.com/browser-use/workflow-use)

Workflow Use：旨在提供确定性和自愈式浏览器自动化的早期项目，可有效作为RPA 2.0。它允许用户记录一次浏览器交互，并将其作为可自动提取变量的结构化工作流进行重放。如果某个步骤失败，它会智能地回退到Browser Use以更正工作流。

主要特性包括：

*   **录制 & 重用：** 通过简单地录制浏览器操作来创建工作流。
*   **确定性执行：** 确保可靠且快速的工作流执行。
*   **变量提取：** 自动识别并提取表单中的变量。
*   **智能过滤：** 消除录制中的噪音，以获得更简洁的工作流。
*   **自愈：** (未来特性) 使用代理在发生故障时自动更新工作流。

该项目旨在解决标准 Browser Use 实现中不可靠和重复提示的挑战。该项目是开源的，帖子包含使用 GitHub 的设置说明，包括构建扩展、设置工作流环境以及通过命令行和 Python 的示例用法。路线图包括改进 LLM 回退、自愈能力、更好的 LLM 步骤支持、在步骤之间传递输出的能力、工作流即工具功能、从网站自动生成工作流以及整体改进开发者体验。

---

## 78. LPython：新型快速可重定向的Python编译器（2023）

**原文标题**: LPython: Novel, Fast, Retargetable Python Compiler (2023)

**原文链接**: [https://lpython.org/blog/2023/07/lpython-novel-fast-retargetable-python-compiler/](https://lpython.org/blog/2023/07/lpython-novel-fast-retargetable-python-compiler/)

LPython是一种新型Python编译器，旨在提高速度和可重定向性，能够通过LLVM、C、C++、WASM和Julia等后端将类型注释的Python代码编译成优化的机器代码。其架构基于与LFortran共享的抽象语义表示（ASR），使得优化改进能够同时惠及这两个编译器。

LPython具有提前（AoT）编译、使用`@lpython`装饰器的即时（JIT）编译，以及通过`@pythoncall`装饰器与CPython的互操作性，从而能够访问CPython库。该编译器提供诸如循环展开和向量化等与机器无关的优化。

基准测试表明，在诸如数组求和与乘法的JIT编译任务中，LPython的性能优于Numba等竞争对手。LPython在数组求和方面表现出具有竞争力或更优越的执行时间，而编译时间可能因不同系统而异。文章还提供了AoT编译、JIT编译和CPython互操作性的代码示例。

---

## 79. 自由线程Python元年

**原文标题**: The first year of free-threaded Python

**原文链接**: [https://labs.quansight.org/blog/free-threaded-one-year-recap](https://labs.quansight.org/blog/free-threaded-one-year-recap)

本文总结了支持自由线程Python的第一年努力，强调了其释放多核性能的潜力以及所涉及的挑战。自由线程构建中缺少全局解释器锁 (GIL) 允许真正的并行性，但需要仔细审查和修改现有的 Python 包，特别是那些带有编译代码的包，以确保线程安全。

Quansight 与 Meta 和 Python 社区合作，为更新基本工具和库做出了重大贡献，包括打包工具、绑定生成器和基础 PyData 包。 这些更新涉及修复结构性问题并解决以前被 GIL 掩盖的线程安全漏洞。

CPython 3.14 中发布的关键改进包括线程安全警告、asyncio 修复、ctypes 大修、垃圾回收改进和解释器专业化。 还创建了支持自由线程 Python 的综合指南。

虽然已经取得了重大进展，但生态系统仍然面临挑战。 许多软件包需要进行线程安全审核，有些软件包缺乏必要的更新资源。 作者鼓励开发人员尝试自由线程构建，报告性能问题，通过解决自由线程兼容性存储库中的生态系统范围问题来为这项工作做出贡献，加入社区 Discord，并参加他们的 PyCon 演讲。 作者乐观地认为，自由线程 Python 是未来，并致力于其开发。

---

## 80. Show HN: Rv，R 语言的包管理器

**原文标题**: Show HN: Rv, a Package Manager for R

**原文链接**: [https://github.com/A2-ai/rv](https://github.com/A2-ai/rv)

Rv：一款用于R的可复现、快速且声明式的包管理器。目前仍在开发中，它允许用户通过配置文件定义所需的项目状态，指定R版本、存储库和依赖项。

其核心功能围绕两个命令展开：`rv plan`，用于预览`rv sync`命令的操作；`rv sync`，则根据项目指定的state同步库、锁定文件和配置文件。这涉及到安装指定的包及其依赖项，包括配置文件中指示的建议包。

配置文件（`rproject.toml`）定义了项目详细信息，如名称、R版本和存储库。用户可以指定依赖项，并允许针对特定包进行设置，例如安装建议的依赖项。

安装和使用文档已可用。如需贡献，该项目使用Rust构建，并可选地使用Just。开发者可以使用`just`或`cargo`命令构建、测试（单元和快照）以及安装该项目。快照测试需要R版本4.4.x。示例项目配置可以在存储库的`example_projects`目录中找到。

---

## 81. DoD指令3000.09：武器系统自主性 [pdf]

**原文标题**: DoD Directive 3000.09: Autonomy in weapons systems [pdf]

**原文链接**: [https://www.esd.whs.mil/portals/54/documents/dd/issuances/dodd/300009p.pdf](https://www.esd.whs.mil/portals/54/documents/dd/issuances/dodd/300009p.pdf)

国防部第3000.09号指令确立了关于武器系统自主性的政策并分配了职责。其主要目的是确保以负责任和合乎道德的方式开发和使用自主及半自主武器系统，最大限度地减少意外后果，并确保人为监督。

该指令强调，*在使用致命武力进行决策时，必须始终保持“人在回路中”*。 具体而言，它要求在使用武力时进行适当程度的人为判断。人为监督的程度应根据具体武器系统及其预期用途进行调整，同时考虑到潜在的意外后果、作战环境的复杂性以及潜在目标的脆弱性等因素。

该指令要求所有自主及半自主武器系统都必须经过严格的测试和评估，以确保它们按预期运行，并验证其安全性和可靠性。这些系统的设计必须最大限度地减少可能导致意外或滥杀滥伤的故障可能性。

该指令还强调透明度和问责制的重要性。 国防部要求对自主及半自主武器系统进行记录和跟踪，包括其设计、开发、测试和部署。 需要制定培训计划，以确保人员接受过有关这些系统操作和使用的适当培训。 此外，该指令力求促进遵守战争法、适用条约、武器安全规则和交战规则。 它会定期审查和更新，以适应不断发展的技术和伦理考量。

---

## 82. 发布者：马洛伊语义模型服务器

**原文标题**: Publisher: The Malloy Semantic Model Server

**原文链接**: [https://github.com/malloydata/publisher](https://github.com/malloydata/publisher)

Publisher：面向Malloy数据语言的开源语义模型服务器，旨在解决不同应用和AI agent数据解释不一致的问题。它通过API暴露Malloy语义模型，实现可信数据访问，并确保对“收入”或“客户流失”等数据定义具有共享且明确的理解。

Publisher由三个主要组件组成：Publisher服务器、Publisher SDK（UI组件）和Publisher App（参考数据应用）。服务器加载Malloy包，解析.malloy文件，将Malloy查询编译为SQL，并暴露REST和模型上下文协议（MCP）API。SDK是用于构建用户界面的React组件库，App是展示SDK功能的独立Web应用程序。服务器还计划引入SQL API。

MCP接口允许AI应用与Malloy语义模型交互，从而实现AI数据分析师、上下文感知聊天机器人和自动化报告等用例。Malloy包，包括.malloy文件、.malloynb文件（notebook）和`publisher.json`清单，是Publisher架构的核心。服务器采用两层配置（服务器和项目）进行环境管理（dev、staging、prod）。该项目还使用bun作为javascript运行时和包管理器。

未来的发展包括增强的开发者模式、集成的临时分析UI、计划转换管道以及对官方Dockerfile和镜像的支持。

---

## 83. 守法运动学将眼动与高速感知的极限联系起来

**原文标题**: Lawful kinematics link eye movements to the limits of high-speed perception

**原文链接**: [https://www.nature.com/articles/s41467-025-58659-9](https://www.nature.com/articles/s41467-025-58659-9)

本文研究了人类对高速运动的感知与扫视眼动学之间的关系。核心问题是，我们感知快速移动刺激的能力极限是否受到扫视眼动的典型感觉后果的影响。

研究人员向观察者呈现了快速移动的刺激，这些刺激符合或偏离了扫视眼动特有的速度、持续时间和幅度之间的合法关系。参与者根据他们感知刺激运动轨迹的能力来执行感知任务。

关键发现是，刺激运动的可见性可以通过扫视眼动的特定运动学来强烈预测，反映了“主序列”关系。本质上，如果刺激的运动模仿了扫视眼动，那么刺激移动得越快、越远，就越容易被感知。即使考虑到眼动运动学方面的个体差异，这种关系仍然成立。

计算模型表明，早期视觉处理中的时空整合可以解释这种合法关系。作者提出，视觉系统在抑制扫视眼动的附带感觉后果（扫视省略）时，会考虑运动运动学，从而保持对高速物体运动的敏感性。这项研究表明，视觉感知从根本上适应我们自身行为（特别是眼动）的感觉后果。

---

## 84. 有条不紊的平庸

**原文标题**: Methodical Banality

**原文链接**: [https://aeon.co/essays/who-needs-ai-text-generation-when-theres-erasmus-of-rotterdam](https://aeon.co/essays/who-needs-ai-text-generation-when-theres-erasmus-of-rotterdam)

汉娜·卡兹内尔森的《方法论的平庸》探讨了现代大型语言模型（LLMs）与16世纪人文主义者写作技巧之间的相似之处，特别是那些受鹿特丹伊拉斯谟影响的人。该文章认为，伊拉斯谟人文主义，其强调模仿和使用常用语录本，实际上是一种早期的自动化文本生成形式。

文章以伊拉斯谟的《西塞罗主义者》和弗朗索瓦·拉伯雷的《巨人传》为例来阐述其观点。《西塞罗主义者》突出了通过持续的风格完善来产生原创内容的挣扎，这与LLMs轻松生成文本的方式相呼应。卡兹内尔森认为，拉伯雷明白伊拉斯谟式的技巧可以自动化文本创作，但代价是削弱了语言的社会和道德影响。《巨人传》中，接受过人文主义训练的角色产生了雄辩但通用的语言，将风格置于实质之上。

作者解释了西塞罗主义者和折衷主义者（如伊拉斯谟）之间的区别，强调了常用语录本的不同使用方式。西塞罗主义者严格验证每一个词的来源，阻碍了流畅性，而折衷主义者则将常用语录本用作安全网。

卡兹内尔森随后将拉伯雷的人文主义角色与LLMs进行了比较。在《巨人传》中，角色们无法达成和平，因为语言并非真正的交流，而仅仅是对预期辞藻的背诵。同样，正如LLMs“幻觉”出听起来合理但虚假的信息一样，角色们也做出了不真实的陈述，因为他们只是在模仿那种情况下一个有德领导者所应具有的预期角色。作者总结说，伊拉斯谟人文主义和LLMs都依赖于拒绝新颖性，而是将复杂的主题分解为熟悉的组成部分，最终未能实现真正的交流。

---

## 85. 科学网络

**原文标题**: Sci-Net

**原文链接**: [https://sci-hub.se/sci-net](https://sci-hub.se/sci-net)

Sci-Net：一个旨在促进研究论文共享的新型社交网络平台，旨在解决Sci-Hub当前基础设施的局限性。与Sci-Hub不同，Sci-Net允许用户请求无法获取的论文并上传他们拥有的论文，从而为Sci-Hub数据库暂停更新的问题提供解决方案。

该平台具有一个简单的界面，可使用DOI请求论文，并提供按主题和出版商筛选的可搜索请求列表。它还包括去除水印的工具，以保护上传者的匿名性。注册用户可以访问用于管理请求、上传的部分，只需拖放PDF文件即可贡献论文。上传的文章可通过直接URL访问，即使对于未注册用户也是如此。

一个关键特性是使用Sci-Hub迷因币来激励知识共享。用户为上传者指定代币奖励，在请求者验证解决方案后进行转账。注册需要至少1000个Sci-Hub代币，旨在为奖励系统提供资金。虽然这引入了名义上的“入门税”，但它被认为是一种象征性成本，付款直接使上传者受益，并有助于扩大知识的公共领域。

Sci-Net旨在创建一个可持续的、社区驱动的平台，该平台可以补充Sci-Hub，促进开放获取，并奖励那些为知识共享做出贡献的人。该平台正在积极开发中，并计划推出更多功能。

---

## 86. 构建于大型语言模型之上的软件开发

**原文标题**: Building software on top of Large Language Models

**原文链接**: [https://simonwillison.net/2025/May/15/building-on-llms/](https://simonwillison.net/2025/May/15/building-on-llms/)

本文总结了2025年5月15日在PyCon US上举办的题为“基于大型语言模型构建软件”的研讨会。该研讨会旨在使参与者掌握使用LLM创建代码的技能。

该研讨会主要以互动形式进行，通过一份包含练习的讲义，涵盖了：LLM设置、基本提示、从Python进行提示、构建文本到SQL工具、结构化数据提取、语义搜索和RAG（检索增强生成）以及工具使用。

作者重点介绍了当前的LLM格局，强调OpenAI、Gemini和Anthropic是关键参与者，并且许多开放权重模型也可用。他指出使用LLM的成本正在降低，以及实验对于理解其能力和局限性的重要性。

该研讨会还涵盖了向量嵌入及其在语义搜索和RAG中的使用。作者认为RAG不会消失，并且LLM工具调用是一种很有前途的方法。

很大一部分内容专门讨论了提示注入和LLM安全，解释了越狱模型和攻击基于它们构建的应用程序之间的区别。作者讨论了双LLM模式和CaMeL方法作为潜在的解决方案。

文章最后总结了评估（evasls）对于LLM系统的重要性，展示了LLM作为裁判是一种可行的方法。最后，简要演示了在作者机器上运行的本地模型。作者提出可以为公司私下举办该研讨会。

---

## 87. 互联网搜索并非简单的信息检索问题

**原文标题**: Internet Search Is Not a Naive Information Retrieval Problem

**原文链接**: [https://www.gojiberries.io/internet-search-is-not-a-naive-information-retrieval-problem/](https://www.gojiberries.io/internet-search-is-not-a-naive-information-retrieval-problem/)

本文批判了一篇声称语言模型（LLM）能够达到与“真正的搜索引擎”相媲美的搜索性能的研究论文。作者认为，虽然该研究表明LLM可以通过课程式展开策略等技术，在受控环境中模拟搜索行为，训练它们应对日益复杂的检索场景，但它从根本上误解了真实世界搜索的复杂性。

核心论点是，搜索引擎真正的挑战不仅仅是找到相关文档，而是抵御操纵。一旦搜索算法变得有价值，它就会成为广泛利用的目标。真正的搜索引擎投入大量资源来打击垃圾邮件、人为链接计划、伪装和其他旨在操纵系统的恶意策略。作者用军事演习与实际战斗的类比来说明两者之间的差异；在受控环境中训练的LLM并不一定能应对开放互联网的对抗性条件，在开放互联网中，无数实体都在积极试图为了利润而操纵搜索结果。因此，仅仅基于非对抗性环境中的相关性指标就声称与真正的搜索引擎等效是具有误导性的。

---

## 88. Java三十年：詹姆斯·高斯林访谈

**原文标题**: Java at 30: Interview with James Gosling

**原文链接**: [https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/)

这是订阅 The New Stack 新闻通讯的表格。着陆页推广了与 James Gosling 关于 Java 30 周年的访谈。

此表格收集用户信息，包括：

*   **邮箱地址（必填）：** 用于发送新闻通讯。为之前取消订阅的用户提供重新订阅选项。
*   **名（必填）**
*   **姓（必填）**
*   **公司名称（必填）**
*   **国家/地区（必填）：** 下拉菜单提供完整的国家/地区列表。
*   **邮政编码（必填）**
*   **职位级别（必填）：** 下拉菜单提供 C-Level、副总裁/总监、经理、员工、自由职业者、学生或其他等选项。
*   **职位角色（必填）：** 下拉菜单提供开发者、系统管理员、架构师、安全专家、DevOps 工程师、社区经理、IT 管理、业务拓展、爱好者或其他等角色选项。
*   **公司规模（必填）：** 下拉菜单提供从个体经营到超过 10,000 人的员工数量范围，以及“未工作”选项。
*   **组织类型（必填）：** 下拉菜单询问最能描述他们工作场所的类型
*   **行业（必填）：** 包含行业选项的下拉菜单。
*   **LinkedIn 个人资料 URL（可选）**

该表格声明 The New Stack 不会出售或与无关联的第三方分享用户信息，并且用户通过订阅同意使用条款和隐私政策。

成功订阅后，用户将收到欢迎信息，并被鼓励检查其收件箱中的确认电子邮件，以调整偏好和加入其他群组，在社交媒体上关注 The New Stack，以及浏览精选内容。

---

## 89. 开发复杂系统：我在谷歌的工作经验

**原文标题**: Working on complex systems: What I learned working at Google

**原文链接**: [https://www.thecoder.cafe/p/complex-systems](https://www.thecoder.cafe/p/complex-systems)

Teiva Harsanyi 的这篇文章探讨了复杂系统与复杂系统之间的区别，并结合作者在 Google 的经验阐述了关键概念。复杂系统是可预测的，可以通过结构化的解决方案来解决，而复杂系统则因其独特和不断发展的性质而需要适应性的、新颖的方法。

文章概述了复杂系统的五个特征：涌现行为、滞后效应、局部与全局优化挑战、滞后现象和非线性。它强调规模本身并不定义复杂性。

作者随后提出了几种应对复杂系统的模式：倾向于可逆的决策、通过考虑局部和全局影响来思考超出直接指标的范围、拥抱创新、采用受控发布（功能开关、金丝雀发布、渐进式发布、影子测试）、优先考虑可观察性以了解系统状态、使用模拟来测试变更、利用机器学习来实现自适应解决方案，以及培养强大的团队协作。

核心信息是，认识到系统的本质——复杂或复杂——对于选择正确的解决问题的方法至关重要。在许多环境中，系统都是两者的混合体，需要灵活的思维方式来相应地调整解决方案。作者最后鼓励读者分享他们自己在复杂环境中进行导航的经验和策略。

---

## 90. Tek – 适用于24位Unicode终端的音乐制作程序

**原文标题**: Tek – A music making program for 24-bit Unicode terminals

**原文链接**: [https://codeberg.org/unspeaker/tek](https://codeberg.org/unspeaker/tek)

无法访问文章链接。

---

## 91. 超越文本：按需UI生成，打造更佳对话体验

**原文标题**: Beyond Text: On-Demand UI Generation for Better Conversational Experiences

**原文链接**: [https://blog.fka.dev/blog/2025-05-16-beyond-text-only-ai-on-demand-ui-generation-for-better-conversational-experiences/](https://blog.fka.dev/blog/2025-05-16-beyond-text-only-ai-on-demand-ui-generation-for-better-conversational-experiences/)

本文探讨了基于文本的AI交互的局限性，并提出了一种解决方案：按需动态生成UI组件。作者认为，纯文本通信会导致认知超载、歧义、可访问性障碍和效率低下，尤其是在企业应用和客户服务中。

所提出的解决方案涉及LLM基于对话上下文生成UI组件（表单、按钮、表格等）的JSON规范，然后由客户端应用程序呈现。这弥合了对话式AI和传统界面之间的差距，提供了对话的灵活性和结构化输入的精确性。

本文详细介绍了系统的工作原理：请求解释、意图识别、组件选择和生成、渲染、交互处理和结构化处理。它强调了将此方法与MCP服务集成的好处，包括标准化通信、减少认知负荷、增强功能、数据验证和无缝用户体验。

作者确定了关键的UI组件类型，如表单、选择组件（按钮、单选按钮）、数据可视化组件（表格、列表）和复杂的复合组件（向导、日历选择器），并提供了每个组件的示例。一个航运公司客户支持系统原型展示了在整个对话过程中动态生成UI组件的过程。

最后，本文概述了实施步骤，包括系统提示和客户端渲染，并讨论了技术和用户体验方面的挑战，以及未来的研究方向，如自动化UI测试、个性化界面和增强的MCP集成。作者鼓励开发者从定义他们的组件库和创建强大的系统提示开始。

---

## 92. 无锁 Rust：如何在着火时建造过山车

**原文标题**: Lock-Free Rust: How to Build a Rollercoaster While It's on Fire

**原文链接**: [https://yeet.cx/blog/lock-free-rust/](https://yeet.cx/blog/lock-free-rust/)

本文深入探讨了 Rust 中无锁编程的复杂性和潜在陷阱，特别关注于构建 `LockFreeArray<T, N>`，这是一种为高性能并发操作而设计的固定大小的无锁数组。作者用“火烧过山车”的比喻来强调这种方法固有的危险性和难度。

文章解释了 `AtomicPtr`、`AtomicUsize` 和 `compare_exchange` 在跨线程管理内存和状态方面的应用，而无需传统的锁。它强调了内存顺序 (`Acquire`、`Release`、`AcqRel`、`Relaxed`) 在确保数据一致性和防止竞争条件方面的关键作用，并警告不要不恰当地使用 `Ordering::Relaxed`。

`LockFreeArray` 的一个关键组成部分是空闲列表，这是一个使用原子操作管理的可用槽位链表，充当自定义内存分配器。文章剖析了 `try_insert` 和 `take` 方法，展示了原始指针、内存安全性以及 `compare_exchange` 的复杂处理，以防止数据竞争和内存损坏。

文章提供了基准测试数据，证明了 `LockFreeArray` 相比于受互斥锁保护的 `Vec` 的性能优势，在生产者-消费者工作负载中实现了显著的速度提升。然而，它强调只有在性能至关重要且开发人员对并发和内存管理有深刻理解的情况下，才应尝试无锁编程，以避免未定义行为和内存泄漏。

---

## 93. Cracked – 方法链/CSS样式选择器Web音频库

**原文标题**: Cracked – Method chaining/CSS-style selector web audio library

**原文链接**: [https://github.com/billorcutt/i_dropped_my_phone_the_screen_cracked](https://github.com/billorcutt/i_dropped_my_phone_the_screen_cracked)

"手机摔了，屏幕碎了"(Cracked)是一个Web音频库，旨在通过方法链和CSS样式选择器简化Web音频开发。它允许用户以简洁直观的方式创建、配置和连接音频节点。

该库强调简洁易用性，灵感来自模块化合成器。主要功能包括：

*   **方法链:** 通过链接音频节点的创建和配置来实现紧凑的代码。
*   **CSS样式选择器:** 提供了一种熟悉的方式来定位和操作音频图中的特定节点。
*   **宏:** 允许将音频节点链封装成可重用的单元，从而促进插件创建和模块化设计。宏可以嵌套、实例化，并可以单独或分组控制。

Cracked 鼓励专注于创造性的音频处理，而不是复杂的编码。学习更多内容的资源包括文档、Reddit 采访、媒体报道以及用于实验的 Mac/Linux 应用程序。欢迎通过评论、问题报告和拉取请求来做出贡献。

---

## 94. 地面控制中心呼叫特莱尔少校

**原文标题**: Ground control to Major Trial

**原文链接**: [https://virtualize.sh/blog/ground-control-to-major-trial/](https://virtualize.sh/blog/ground-control-to-major-trial/)

Vates 揭露某半官方航天公司滥用 Xen Orchestra Appliance (XOA) 30天试用版长达十年之久的闹剧。该设备是 Xen Orchestra 平台的预配置、受支持版本，可替代从源代码构建。

这家年收入 1.3 亿美元，并大量依赖 Vates 平台运行大型 IT 基础设施的公司，始终逃避支付 XOA 的费用。他们最初使用公司邮箱申请试用，随后切换到个人邮箱地址，并以递增的方式更改句柄来延续这一周期。

Vates 强调，使用开源版本是一种免费替代方案，但这家公司有意选择更方便、受支持的设备，并通过滥用试用系统来规避付款。Vates 早期甚至提供了支持，因为他们认为对方是潜在客户，但最终发现了滥用试用的行为模式。

Vates 对此表示沮丧，认为这种行为违背了开源的“道德契约”，尤其是在该公司拥有雄厚财力的情况下。虽然他们不打算穷追不舍，但他们计划实施更智能的试用限制，以防止进一步的滥用，并将精力集中在真正的用户身上。作者最后呼吁该公司拥抱道德行为，并支持他们所依赖的开源生态系统。

---

## 95. 三步判断闰年

**原文标题**: A leap year check in three instructions

**原文链接**: [https://hueffner.de/falk/blog/a-leap-year-check-in-three-instructions.html](https://hueffner.de/falk/blog/a-leap-year-check-in-three-instructions.html)

本文探讨了一种使用位操作技巧的高度优化的闰年检测方法，仅用三条 CPU 指令即可实现。作者首先使用模运算替换（将 y % 100 替换为 y % 25，将 y % 400 替换为 y % 16）以及用乘法降低模 25 的技巧来优化标准的闰年算法。

文章的核心内容是介绍了一种使用魔术常数的无分支闰年检测方法 `is_leap_year_fast`。这些常数是使用 Z3 求解器找到的，旨在实现特定的位模式。然后，文章详细解释了这些常数是如何工作的，将其分解为位范围，并演示了它们如何有效地复制检查能否被 4、25 和 16 整除的逻辑。

具体来说，常数 `f` 乘以年份 `y` 后，再与 `m` 进行掩码运算，结果与 `t` 进行比较。这巧妙地将多个比较组合成一个小于等于操作。分析表明，常数中的位范围如何确保评估等效于 `y % 4 != 0`、`y % 25 != 0` 和 `y % 16 == 0` 的条件。

作者进一步将该方法扩展到 64 位整数，找到了为年份最高达 5965232499 提供正确结果的常数，这超过了 32 位无符号整数的最大可能值。最后，讨论了基准测试，文章得出结论。

---

## 96. 展望下一代望远镜

**原文标题**: Taking a look at the next generation of telescopes

**原文链接**: [https://arstechnica.com/space/2025/05/tuesday-telescope-taking-a-look-at-the-next-generation-of-telescopes/](https://arstechnica.com/space/2025/05/tuesday-telescope-taking-a-look-at-the-next-generation-of-telescopes/)

埃里克·伯格的“星期二望远镜”文章关注的是目前正在建造的下一代极大望远镜。文章重点介绍了欧洲南方天文台位于智利阿塔卡马沙漠的“极大望远镜”(ELT)，该望远镜拥有巨大的39米主镜，使现有望远镜相形见绌。ELT是全球建造更大、更强大的地面望远镜竞赛的一部分。巨型麦哲伦望远镜(GMT)是一个涉及美国和其他国家的项目，也在阿塔卡马沙漠建造，将拥有25.4米的主镜。第三个项目是三十米望远镜(TMT)，计划在夏威夷建造，但由于夏威夷原住民的反对而面临重大挑战。文章强调，未来十年内至少完成其中一台望远镜将彻底改变我们对宇宙的理解。作者将这一发展描述为一个激动人心的前景，强调了这些先进仪器将带来的未来发现的兴奋感。

---

## 97. 锌微型电容器：两全其美

**原文标题**: Zinc Microcapacitors Are the Best of Both Worlds

**原文链接**: [https://spectrum.ieee.org/zinc-microcapacitor](https://spectrum.ieee.org/zinc-microcapacitor)

研究人员开发出锌离子微型电容器，兼具电池和超级电容器的优点，有望填补小型储能领域的空白。根据Liam Critchley在IEEE Spectrum上发表的一篇文章，这些微型电容器利用锌离子的优势来实现这种组合功能。

该文章强调了这项技术在提供高能量密度（如电池）和快速充电/放电速率（如超级电容器）方面的潜力。这种组合使其对这些特性至关重要的应用具有吸引力，例如小型电子设备、传感器和微型机器人。由Yujia Fan和Nibagani Naresh领导的研究（如ACS Nano所述）表明，锌离子微型电容器代表了微型技术储能领域的一项有前景的进步。

---

## 98. 在美国，旋转爆震火箭发动机升空

**原文标题**: In the US, a rotating detonation rocket engine takes flight

**原文链接**: [https://arstechnica.com/space/2025/05/venus-aerospace-flies-its-rotating-detonation-rocket-engine-for-the-first-time/](https://arstechnica.com/space/2025/05/venus-aerospace-flies-its-rotating-detonation-rocket-engine-for-the-first-time/)

维纳斯航空在美国完成旋转爆震火箭发动机的首次飞行测试，有望实现超音速旅行

---

## 99. TLA⁺开发的现状

**原文标题**: The current state of TLA⁺ development

**原文链接**: [https://ahelwer.ca/post/2025-05-15-tla-dev-status/](https://ahelwer.ca/post/2025-05-15-tla-dev-status/)

本文总结了TLA⁺开发的现状，认为使TLA⁺语言工具更容易开发是该语言未来的关键。文章重点介绍了现有的工具，如解析器（SANY、TLAPM、tree-sitter-tlaplus）、解释器（TLC的解释器、Spectacle）、模型检查器（TLC、Apalache、Spectacle）以及其他实用工具，如TLAPM、Snowcat、格式化器、LSP服务器和Unicode转换器。

文章承认了SANY和TLC等核心工具因其历史悠久和复杂性而带来的“遗留代码挑战”，这些工具缺乏实际经验，并且大量的静态状态阻碍了测试。作者表达了乐观态度，强调语言工具具有明确定义的需求，并且TLA⁺基金会正在积极资助开发。

克服这些挑战的具体策略包括为解析器开发标准化的、独立于实现的测试套件，通过指南和教程（包括构建最小TLA⁺模型检查器的教程）改进开发人员的入门流程，以及提供赠款和津贴以支持全职贡献者。作者最后建议将生成式测试和潜在的语法简化作为未来的发展方向，并鼓励有兴趣的人加入TLA⁺的开发工作。

---

## 100. GTK 克雷尔显示器

**原文标题**: GTK Krell Monitors

**原文链接**: [https://gkrellm.srcbox.net/](https://gkrellm.srcbox.net/)

GKrellM是一款系统监控应用程序，它在单个窗口中显示系统统计信息，并被设计为可通过主题进行视觉自定义。它可以监控主机名、CPU（包括SMP支持）、温度、风扇速度、电压、进程负载/fork、磁盘活动、互联网连接、网络接口、内存/交换空间使用情况、文件系统容量、邮箱状态（支持各种格式）、笔记本电脑电池和运行时间。它还可以运行在客户端模式，从远程gkrellmd服务器收集数据。

主要功能包括可配置的传感器警报和警告、自动缩放图表、监视器标签上的可自定义命令以及用于扩展功能的插件支持。

它需要Gtk+ 2.24或更高版本，gkrellmd服务器需要GLib 2.32或更高版本。它适用于Linux（从/proc读取数据）、FreeBSD、macOS、NetBSD/OpenBSD和Windows（通过一个单独的项目）。

用户可以下载适用于各种Linux发行版、macOS（Homebrew、MacPorts）和Windows的预构建软件包，或者从git.srcbox.net上提供的源代码构建。 有多种方式可以与用户和开发人员社区联系，包括邮件列表、Matrix房间和IRC频道。 该网站还列出了将GKrellM与其他设备（如TiVo或Linksys路由器）一起使用的主题和教程的链接。GKrellM在GNU通用公共许可证下发布。

---

