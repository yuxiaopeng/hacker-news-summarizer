# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-05-17.md)

*最后自动更新时间: 2025-05-17 17:47:16*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 2 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 3 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 4 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 5 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 6 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 7 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 8 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 9 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 10 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 11 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 12 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 13 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 14 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 15 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 16 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 17 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 18 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 19 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 20 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 21 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 22 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 23 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 24 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 25 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 26 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 27 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 28 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 29 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 30 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 31 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 32 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 33 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 34 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 35 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 36 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 37 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 38 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 39 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 40 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 41 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 42 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 43 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 44 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 45 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 46 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 47 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 48 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 49 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 50 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 51 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 52 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 53 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 54 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 55 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 56 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 57 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 58 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 59 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
