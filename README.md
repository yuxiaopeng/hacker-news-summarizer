# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-06-13.md)

*最后自动更新时间: 2025-06-13 17:53:51*
## 1. Meta投资143亿美元于Scale AI，启动超智能实验室

**原文标题**: Meta Invests $14.3B in Scale AI to Kick-Start Superintelligence Lab

**原文链接**: [https://www.nytimes.com/2025/06/12/technology/meta-scale-ai.html](https://www.nytimes.com/2025/06/12/technology/meta-scale-ai.html)

无法访问文章链接。

---

## 2. OxCaml - OCaml编程语言的一组扩展。

**原文标题**: OxCaml - a set of extensions to the OCaml programming language.

**原文链接**: [https://oxcaml.org/](https://oxcaml.org/)

OxCaml是由Jane Street开发的OCaml编程语言的一组扩展，旨在提高面向性能的编程能力，同时保留OCaml的核心原则。其主要目标是在OCaml生态系统中，仅在需要时，提供对程序行为中性能关键方面的安全、便捷和可预测的控制。

这些扩展侧重于：

*   **无畏并发：** 类型系统新增功能，以防止数据竞争。
*   **布局：** 指定内存中的数据布局，并启用对SIMD指令的本地访问。
*   **分配控制：** 管理分配的工具，减少GC压力并提高缓存效率。
*   **生活质量：** 增强功能，如多态参数、include functor、带标签的元组和不可变数组。

OxCaml优先考虑安全性、便捷性和可预测性，旨在保持OCaml的类型推断和清晰的性能特征。它采用“按需付费”模式，意味着只有在使用其优化能力时才会遇到增加的复杂性。至关重要的是，有效的OCaml程序也是有效的OxCaml程序。

OxCaml是开源的，欢迎实验用户提供反馈，但对其扩展不提供稳定性或向后兼容性保证。它带有修改后的标准OCaml工具版本，包括包管理、编辑器集成、源代码格式化和文档生成。Jane Street开发的库和工具提供OCaml兼容版本（剥离扩展）和OxCaml版本。由于所用扩展的性质，某些库是OxCaml独有的。

---

## 3. 如果月亮只有1像素：一个极其精确的太阳系模型 (2014)

**原文标题**: If the moon were only 1 pixel: A tediously accurate solar system model (2014)

**原文链接**: [https://joshworth.com/dev/pixelspace/pixelspace_solarsystem.html](https://joshworth.com/dev/pixelspace/pixelspace_solarsystem.html)

如果月亮只有一个像素：乔什·沃思的互动在线项目，以比例可视化太阳系内的巨大距离。该项目用一个像素代表月亮，突出了太空的广袤空虚。旅程从太阳开始，逐个经过每个行星，以公里和其他易于理解的单位强调它们之间相当大的距离。

该作品探讨了人类难以理解如此巨大尺度的困难，转而使用隐喻和比较来使距离更易于理解（例如，乘坐太空飞船的旅行时间、屏幕堆叠）。它认为，传统的地图往往未能传达太空的真实比例，而这才是太阳系最重要的部分。

文章深入探讨了这种空虚的哲学意义，表明我们的大脑并非天生就适合理解如此广阔的空间。它讨论了这种感知的“虚无”如何令人不安，导致感觉剥夺效应，并突出了人类感知的局限性。

最终，该项目以思考物质（行星、恒星，甚至人类）存在于这片巨大空虚中的意义作为结尾。它表明，这些“小点”的存在或许可以使空虚本身变得可测量且有意义，而我们在如此多的虚无中存在，本身就是一个令人惊叹的现象，尽管在宇宙尺度上可能微不足道。它鼓励人们反思我们与宇宙相关的渺小感和重要感之间的对比。

---

## 4. 帽子、幽灵与SAT求解器 (2024)

**原文标题**: The Hat, the Spectre and SAT Solvers (2024)

**原文链接**: [https://www.nhatcher.com/post/on-hats-and-sats/](https://www.nhatcher.com/post/on-hats-and-sats/)

这篇博文探讨了一项近期数学发现：用名为“帽子”的单一形状对平面进行非周期性平铺，并介绍了SAT求解器作为解决平铺问题的工具。作者解释了“帽子”的形状、其非周期性平铺性质，以及它与早期发现（如彭罗斯瓷砖）的联系。

博文随后介绍了SAT求解器，解释了它们通过将布尔代数问题转换为合取范式（CNF）来解决这些问题的原理。作者描述了如何在WASM环境中使用SAT求解器来解决数独难题，展示了求解器的实用性并提供了一个实际例子。

接下来，作者解释了如何将SAT求解器应用于平铺问题，灵感来源于Craig Kaplan的研究。他们描述了如何将六边形网格系统与“帽子”结合使用，以及如何制定子句来找到平铺给定区域的解决方案。博文随后介绍了与“帽子”类似的“海龟”瓷砖，它也能非周期性地平铺平面。

最后，博文讨论了“幽灵”，它是“帽子”家族的一个变体，可以在没有其镜像（反幽灵）的情况下非周期性地平铺平面。它解释了定理3.1，描述了“幽灵”的平铺与{帽子，海龟}集合的平铺之间的双射关系。作者描述了如何使用该应用程序，通过更改“帽子”和“海龟”的边长来创建“幽灵”，从而找到一种非周期性单片瓷砖。

---

## 5. Show HN: Tattoy – 基于文本的终端合成器

**原文标题**: Show HN: Tattoy – a text-based terminal compositor

**原文链接**: [https://tattoy.sh](https://tattoy.sh)

Tattoy: 一款基于文本的终端合成器，通过视觉效果和实用功能增强终端体验。它与现有终端设置配合使用，在不影响复制粘贴等常规终端操作的前提下，增添视觉效果。

主要功能包括：

*   **GPU着色器：** 在终端中渲染 Shader Toy 和 Ghostty 着色器。
*   **后台终端：** 在后台显示另一命令的输出，适用于可视化或系统监控。
*   **回滚小地图：** 提供终端回滚历史记录的实时更新像素化视图，包括滚动条支持。
*   **自动文本对比度：** 通过分析终端颜色的真实 RGB 值，智能调整文本颜色，确保可读性，克服终端调色板的局限性。
*   **插件：** 支持通过 STDIN/STDOUT 上的 JSON 以任何语言编写的插件，从而实现自定义效果以及与终端内容的交互。一个演示示例是烟雾粒子与光标附近的文本交互。

Tattoy 旨在提升现代终端的美观性和可用性。

---

## 6. 策梅洛选择公理百年：问题何在？(2006)

**原文标题**: 100 years of Zermelo's axiom of choice: What was the problem with it? (2006)

**原文链接**: [https://research.mietek.io/mi.MartinLof2006.html](https://research.mietek.io/mi.MartinLof2006.html)

本文回顾了策梅洛选择公理（AC）诞生一个世纪后引发的争议，考察了其最初的拒绝和最终在主流数学中的接受，以及直觉主义者对其持续的拒绝。虽然毕肖普主张对选择公理进行构造性解释，但迪亚科内斯库定理突出了构造性观点与拓扑斯理论对选择公理的理解之间潜在的不相容性。

作者在构造类型论的框架内分析了策梅洛1908年对选择公理的表述，将集合表示为外延集合（具有等价关系的集合），将子集表示为外延命题函数。该分析试图基于集合S、索引集合I和一系列子集（A_i）来证明选择公理，这些子集是外延的、互斥的、穷举的和非空的。

作者证明，虽然构造性选择公理可以提供一个函数*f*，满足A_i(f(i))，但它无法保证*f*的外延性（即，i ≍ j → f(i) ≍ f(j)）。这种外延性对于证明策梅洛选择公理所需的唯一性条件是必要的。

论文的结论是，策梅洛选择公理由一个*外延的*选择公理（ExtAC）所暗示，该公理明确包括了选择函数必须是外延的的要求。然而，ExtAC缺乏内涵性选择公理所享有的直接论证，后者源于其与布劳威尔-海廷-柯尔莫哥洛夫对逻辑常数的解释的联系。因此，策梅洛选择公理的核心问题在于它依赖于一个外延的选择函数，但没有为其外延性提供构造性的证据。

---

## 7. 当陌生人给陌生人钱 (2017)

**原文标题**: When random people give money to random other people (2017)

**原文链接**: [https://quomodocumque.wordpress.com/2017/06/27/when-random-people-give-money-to-random-other-people/](https://quomodocumque.wordpress.com/2017/06/27/when-random-people-give-money-to-random-other-people/)

随机财富再分配导致财富不均：一个悖论的解释

---

## 8. Jemalloc事后分析

**原文标题**: Jemalloc Postmortem

**原文链接**: [https://jasone.github.io/2025/06/12/jemalloc-postmortem/](https://jasone.github.io/2025/06/12/jemalloc-postmortem/)

jemalloc事后分析：jemalloc内存分配器的开发历程，从最初作为Lyken编程语言的一部分（阶段0）开始，在FreeBSD（阶段1）中获得初步成功，取代了现有的分配器，但也面临碎片化问题，促使其进行重大重新设计。

阶段1.5涉及与Mozilla Firefox的集成，由于性能差异，导致了一个分支版本，这令作者非常失望。在Facebook（阶段2），jemalloc的集成是由对pprof兼容的堆分析的需求所推动的，并且该项目极大地受益于Facebook的内部遥测和性能数据。引入了诸如广泛的测试、Valgrind支持（后来颇具争议地被移除）、JSON遥测以及向范围的过渡等功能。在作者离开之前，成立了一个jemalloc团队来解决性能和基础设施的改进问题。

Meta阶段（阶段3）看到对投资回报的关注转移，导致长期开发的停滞，并最终导致通用性的下降。作者将此归因于公司优先事项的转变。

阶段4标志着上游开发的结束，作者认为这是由于累积的技术债务以及缺乏继续下去的热情。他对缺乏对Valgrind和Android等外部使用的意识表示遗憾，并强调尽管是开放开发，但jemalloc未能保留来自其他组织的主要贡献者。尽管是垃圾收集的倡导者，但他承认jemalloc是一个令人满意的项目。

---

## 9. 量子时间关联中的几何学

**原文标题**: Geometry from Quantum Temporal Correlations

**原文链接**: [https://arxiv.org/abs/2502.13293](https://arxiv.org/abs/2502.13293)

James Fullwood 和 Vlatko Vedral 的 arXiv 预印本，题为《量子时间关联中的几何》，探索了量子力学和几何之间令人惊讶的联系。作者证明，欧几里得3维空间可以从对单个量子比特进行 Pauli 观测量的序列测量所产生的量子时间关联结构中唯一地涌现出来。

一个关键发现是，从这些时间关联推导出的几何与量子比特的初始状态无关。 这意味着观察者可以从序列测量中提取几何信息，而无需知道量子比特的初始条件，这是一个非凡的性质，暗示了量子力学和几何之间存在着根本的联系。

基于这些结果，作者提出了一个“玩具模型”，表明空间本身可能从量子时间关联中涌现出来。这是一个高度推测性的想法，将这篇论文定位为对空间基础性质的探索性研究。

这篇论文简洁明了，共 4 页，没有图。它被归类在量子物理（quant-ph）学科下，并提出了一个理论框架，用于理解空间如何可能从系统的底层量子特性中涌现出来。它是一项重要的概念贡献，而不是详细的计算或实验报告。

---

## 10. 频繁重新验证并不能让你更安全

**原文标题**: Frequent reauth doesn't make you more secure

**原文链接**: [https://tailscale.com/blog/frequent-reath-security](https://tailscale.com/blog/frequent-reath-security)

Avery Pennarun的博文认为，频繁的重新身份验证并不能增强安全性，甚至可能削弱安全性。文章批判了强制用户重复登录的过时做法，强调了由此带来的挫败感和安全风险，例如MFA疲劳。

作者认为，安全应该侧重于强大的访问管理、快速的策略变更以及检测被盗用的凭据。频繁登录的实施通常是因为管理员对立即执行策略缺乏信心，尤其是在SAML方面。

文章驳斥了频繁登录对常见攻击媒介（如远程网络钓鱼）的有效性，因为被盗用的凭据会使它们的目的失效。相反，作者提倡利用操作系统级别的安全措施，例如自动屏幕锁定，这提供了类似的保护，而无需持续中断。

作者批评了Web会话过期策略，认为它们基本上是无效的。Pennarun建议，与其进行任意登录提示，不如仅在必要时验证设备所有权，例如在执行敏感操作之前，Tailscale的SSH检查模式和Slack Accessbot就是例证。

该帖子强调通过设备姿势检查和基于SCIM的访问控制进行持续验证，以实现实时安全更新，而无需用户干预。当设备离线或角色发生变化时，访问权限会立即被撤销或更新。

作者的结论是，最好的安全是无缝且自适应的，它在后台发生，而不会让用户感到沮丧并养成不良的安全习惯。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 2 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 3 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 4 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 5 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 6 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 7 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 8 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 9 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 10 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 11 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 12 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 13 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 14 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 15 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 16 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 17 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 18 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 19 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 20 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 21 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 22 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 23 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 24 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 25 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 26 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 27 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 28 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 29 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 30 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 31 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 32 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 33 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 34 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 35 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 36 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 37 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 38 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 39 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 40 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 41 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 42 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 43 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 44 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 45 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 46 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 47 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 48 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 49 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 50 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 51 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 52 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 53 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 54 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 55 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 56 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 57 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 58 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 59 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 60 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 61 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 62 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 63 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 64 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 65 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 66 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 67 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 68 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 69 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 70 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 71 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 72 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 73 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 74 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 75 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 76 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 77 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 78 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 79 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 80 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 81 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 82 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 83 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 84 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 85 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 86 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
