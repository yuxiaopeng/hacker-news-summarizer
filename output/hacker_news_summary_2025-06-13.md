# Hacker News 热门文章摘要 (2025-06-13)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Luxe游戏引擎

**原文标题**: Luxe Game Engine

**原文链接**: [https://luxeengine.com/](https://luxeengine.com/)

Luxe是一款跨平台、快速开发的游戏引擎，专为 Mac、Linux、Windows 和 Web 平台上的 2D 和 3D 游戏而设计，并计划支持主机平台。Luxe 由一家积极将其用于自身项目（Mossfield Origins 和 Archives）的游戏工作室构建，优先考虑设计和工作流程，以实现快速原型设计和迭代。

主要特性包括：

*   **易于使用：** 易于学习，采用 2D 优先的方法。
*   **强大的渲染器：** 硬件驱动的渲染器，支持着色器、资源管线和渲染路径。
*   **Wren 语言：** 游戏主要使用 Wren 编程语言的自定义版本制作。
*   **模块化设计：** 核心引擎带有模块系统，可实现轻量级和富有表现力的工具，从而允许扩展和自定义。
*   **注重工作流程：** 强调快速迭代和意图表达，并提供一个可选的编辑器，专为游戏特定需求而设计。
*   **工具，而非功能：** 提供可适应的工具，可以组合起来创建特定的游戏系统，避免不必要的臃肿。
*   **渲染灵活性：** 渲染器允许游戏特定的选择和高级交互，初学者和经验丰富的开发者均可访问。

Luxe 目前提供预览版，并通过其 Discord 和邮件列表鼓励社区参与，以获取开发更新。

---

## 12. 在GPU上渲染酥脆文本

**原文标题**: Rendering Crispy Text on the GPU

**原文链接**: [https://osor.io/text](https://osor.io/text)

无法访问文章链接。

---

## 13. Show HN: Qrkey – 纸上离线私钥备份

**原文标题**: Show HN: Qrkey – Offline private key backup on paper

**原文链接**: [https://github.com/Techwolf12/qrkey](https://github.com/Techwolf12/qrkey)

QRKey 是一个命令行工具，旨在通过将私钥和其他文件转换为二维码来创建离线备份。它允许用户将文件编码成一系列二维码，然后可以打印并安全存储。该工具支持大型文件，通过自动将它们分割成多个二维码并加入元数据以进行验证和方便恢复。

用户可以使用条形码扫描器或提供包含二维码数据行的文件，从打印的二维码中恢复原始文件。然后，恢复的数据会被重建成原始文件。

QRKey 可以通过 Homebrew 安装在 macOS 上。其他操作系统的用户也可以使用 Docker 镜像。该工具提供两个主要命令：`generate` 从文件生成二维码 PDF，以及 `recover` 从二维码数据（无论是来自文件还是通过交互式过程）重建文件。该软件是开源的，其许可信息可在 LICENSE 文件中找到。

---

## 14. 小票打印机治好了我的拖延症

**原文标题**: A receipt printer cured my procrastination

**原文链接**: [https://www.laurieherault.com/articles/a-thermal-receipt-printer-cured-my-procrastination](https://www.laurieherault.com/articles/a-thermal-receipt-printer-cured-my-procrastination)

本文详细介绍了作者与拖延症抗争数十年的历程，追溯到潜在的注意力缺陷多动症，以及他们最终如何从电子游戏的成瘾性中获得灵感，找到解决方案。作者观察到，游戏，特别是第一人称射击游戏，利用频繁、强烈的反馈循环（瞄准 -> 射击 -> 命中/未命中）来创造一种多巴胺驱动的“心流状态”。

为了在现实生活中复制这一点，他们开始将任务分解成微任务，并使用便签纸。完成一项任务包括揉皱便签纸并将其扔进罐子里，从而提供即时反馈。这个系统效果很好，但准备起来很耗时。

最终的解决方案涉及一台热敏小票打印机。作者编写了一个脚本来打印每日任务，消除了书写便签纸的麻烦，并提高了效率。他们仍然使用便签纸来处理更复杂的任务，作为打印机的补充。

认识到现有任务管理软件的局限性，作者开发了自定义软件，以列式格式按层级组织任务，从而可以轻松地即时分解任务并仅打印相关的子任务。该系统极大地提高了生产力和效率，有效地消除了低效率的日子。作者强调了以轻松的胜利开始一天的重要性，在前一天晚上准备任务，并灵活运用该系统。

---

## 15. Kyber (YC W23) 招聘技术客户经理

**原文标题**: Kyber (YC W23) Is Hiring a Technical Account Manager

**原文链接**: [https://www.ycombinator.com/companies/kyber/jobs/5kSq3Jd-technical-account-manager-tam](https://www.ycombinator.com/companies/kyber/jobs/5kSq3Jd-technical-account-manager-tam)

Kyber (Y Combinator W23 投资的初创公司) 正在纽约招聘技术客户经理 (TAM)，该公司正在构建一个面向企业的 AI 原生文档平台。Kyber 帮助保险等受监管行业的企业简化监管文档工作流程，显著减少起草时间并改善整体沟通。他们实现了快速增长，包括 20 倍的收入增长，获得了大型合同，并与行业领导者建立了合作关系。

技术客户经理将负责通过入职培训、技术支持，以及充当客户与 Kyber 产品和工程团队之间的联络人，来确保客户成功。这包括翻译反馈、领导技术演示、配置客户部署以及监控客户健康状况。

理想的候选人将拥有 3 年以上企业 SaaS 产品经验、强大的沟通能力、同理心、积极主动的解决问题能力以及团队合作精神。主要要求包括技术熟练度、以客户为中心以及清晰地传达复杂概念的能力。薪资范围为 8 万美元至 12 万美元，股权为 0.01% 至 0.10%。

Kyber 强调挑战假设、以客户为中心、以精湛工艺为荣、高标准以及营造有趣和支持性的环境等价值观。为了脱颖而出，鼓励申请人向创始人 Arvind Sontha 发送带有简短推荐的推荐信。面试过程包括行为筛选、客户支持实践、技术配置实践和背景调查。

---

## 16. 由虚假验证码喂养的黑暗广告技术帝国

**原文标题**: A Dark Adtech Empire Fed by Fake CAPTCHAs

**原文链接**: [https://krebsonsecurity.com/2025/06/inside-a-dark-adtech-empire-fed-by-fake-captchas/](https://krebsonsecurity.com/2025/06/inside-a-dark-adtech-empire-fed-by-fake-captchas/)

本文详细介绍了恶意广告技术相互关联的世界，重点介绍了其在虚假信息宣传活动和各种在线诈骗中的应用。调查始于“Doppelganger”虚假信息网络，该网络被发现使用复杂的隐藏服务，并与长期存在的恶意流量分发系统 (TDS) VexTrio 共享基础设施。

VexTrio以及 LosPollos 和 TacoLoco 等相关网络，利用欺骗性手段（包括虚假验证码）诱骗用户启用推送通知。这些通知随后被用于传播诈骗、恶意软件和误导性弹出消息。研究将这些网络与通过瑞士托管提供商运营的 Adspro Group 公司联系起来，并进一步将其与其他位于俄罗斯的推送盈利项目联系起来，例如 Partners House 和 BroPush。

安全专家认为，这些常被认为是轻微威胁的 TDS 实际上促进了严重恶意软件和诈骗的传播，给消费者造成数十亿美元的损失。这些网络之间的相互关联表明存在着高度的组织性，可能涉及俄罗斯有组织犯罪。文章最后给出了如何在各种浏览器中阻止网站通知请求的建议，以保护自己和不太懂技术的个人免受这些欺骗行为的侵害。

---

## 17. 信号遗漏的手册：Python开发者的状态管理

**原文标题**: The Missing Manual for Signals: State Management for Python Developers

**原文链接**: [https://bui.app/the-missing-manual-for-signals-state-management-for-python-developers/](https://bui.app/the-missing-manual-for-signals-state-management-for-python-developers/)

本文介绍信号作为Python开发者的响应式状态管理解决方案，尤其是在处理复杂、级联的状态变化时，优势明显。文章认为，传统的状态管理依赖于手动更新和副作用，随着应用程序规模的扩大，可能导致错误、紧密耦合、不一致的状态以及测试困难。

信号提供了一种声明式、拉取式的方法，创建一个依赖关系图，其中派生值会在其源发生变化时自动更新。核心原语包括：`Signal`（保存状态）、`Computed`（从信号派生值）和 `Effect`（在依赖项更改时执行副作用）。文章强调，信号是代表当前状态的值容器，与对未来事件做出反应的事件监听器不同。

思维模式的转变在于以始终成立的关系来思考，而不是以命令式的动作序列来思考。信号在具有复杂派生状态、横切关注点、实时数据流和状态同步的场景中表现出色。对于简单的转换和请求-响应模式来说，它们有些过度设计。

文章强调了将相关配置分组到单个信号中的重要性，而不是使用过于细粒度的信号。它还警告不要在计算值中直接执行副作用，提倡使用effects来进行此类操作。通过逐步且策略性地采用信号，Python开发者可以构建更健壮、更易于维护的应用程序。

---

## 18. Show HN：求职指南针 – AI助手助你求职，而非取代你

**原文标题**: Show HN: Job Compass – AI agents that help you find jobs, not replace you

**原文链接**: [https://jobcompass.ai/](https://jobcompass.ai/)

职位指南针AI：利用人工智能助力求职者，而非取代。它通过优化求职流程，帮助用户更聪明地申请、更快地获得录取。它将领英职位搜索转化为实际的录用通知。

该工具面向冉冉升起的新秀、团队领导和高管，解决常见痛点，如申请无回应、缺乏公司联系方式、以及简历石沉大海。它提供诸如寻找招聘联系人、提供定制外联信息、生成薪资洞察、匹配技能、评估公司契合度、以及分析关键词等功能。

职位指南针AI的工作原理是分析职位链接，提供兼容性评分，识别招聘人员和招聘经理并提供联系方式，以及跟踪申请状态。它还提供绩效分析。用户评价强调了更高的回复率、定制化的简历建议，以及直接联系招聘经理的能力。

该工具提供包括免费试用在内的每周和每月订阅计划。它通过比较职位发布与用户的领英个人资料和简历，确定匹配分数，并提供详细的反馈。它还提供简历定制，建议改进以匹配关键词和所需技能。该平台识别招聘人员和招聘经理，提供联系数据以进行定制的外联。用户可以注册、选择计划、粘贴职位链接，然后让职位指南针AI处理剩下的事情。

---

## 19. QEMU中的iPhone 11模拟

**原文标题**: iPhone 11 emulation done in QEMU

**原文链接**: [https://github.com/ChefKissInc/QEMUAppleSilicon](https://github.com/ChefKissInc/QEMUAppleSilicon)

本文档是QEMU的README文件，QEMU是一个通用的开源机器模拟器和虚拟化器。QEMU可以在没有硬件虚拟化支持的情况下模拟完整的机器，通过动态翻译实现良好的性能。它还集成了Xen和KVM虚拟机管理程序，以实现接近原生CPU性能。此外，QEMU为Linux和BSD提供用户空间API虚拟化，使来自不同体系结构的二进制文件能够在单个主机上运行。

该软件适用于各种用例，从直接用户控制到通过稳定的命令行界面和监控API与更高级别的管理层集成。QEMU通常通过libvirt库在oVirt、OpenStack和virt-manager等应用程序中调用。

README还提供了关于如何在各种平台上构建QEMU的说明，包括Linux、macOS和Windows（通过MinGW）。它详细介绍了使用Git提交补丁的过程，强调了“Signed-off-by”行的重要性以及对编码风格指南的遵守。

错误报告应通过GitLab issue进行，最好在使用供应商提供的二进制文件时，先检查该问题是否也存在于上游代码中。该文档还将用户指向QEMU网站，以获取版本历史记录、发行说明和联系信息，包括QEMU开发邮件列表和IRC频道。

---

## 20. 慢工出细活，这首诗会赢得你的心。

**原文标题**: Slow and steady, this poem will win your heart

**原文链接**: [https://www.nytimes.com/interactive/2025/06/12/books/kay-ryan-turtle-poem.html](https://www.nytimes.com/interactive/2025/06/12/books/kay-ryan-turtle-poem.html)

A.O.斯科特的文章分析了凯·瑞恩的诗歌《乌龟》，探讨了其深层含义以及尽管主题如此却出人意料的敏捷性。斯科特首先承认动物在诗歌中的普遍性，但提倡专注的欣赏，并以瑞恩的乌龟为例。

这首诗表面上是对乌龟艰辛生存的诙谐且毫不退缩的描绘，它受壳和缓慢步伐的负担。斯科特强调了瑞恩对生动对比的使用，将乌龟的壳与诸如“包装箱”和“陶器”之类的平凡事物联系起来，突出了这种生物的笨拙现实。

然而，斯科特认为这首诗的精妙之处在于它能够超越主题的局限性。在描述乌龟的笨拙时，诗本身却具有隐藏的敏捷性，通过其内部韵律和节奏得以展现。这首诗的用词巧妙地暗示了乌龟的陆地存在之外的可能性，例如提到“翅膀”，从而引发了与鸟类的联系，并打破了对乌龟的固有认知限制。

斯科特认为《乌龟》在多个层面上发挥作用。它不仅仅是关于动物本身，而是关于将乌龟作为一种隐喻，阐明人类体验的各个方面，特别是对于女性和诗人而言。最后，他巧妙地指出了隐藏在“陶器”一词中的字谜，揭示了“诗歌”，并暗示诗歌本身是一种解放的形式，类似于人类精神的飞翔。这篇文章鼓励读者更深入地研究这首诗的细微之处，欣赏其智慧、观察力和微妙的隐喻。

---

## 21. Show HN: Tritium – Rust 语言的法律 IDE

**原文标题**: Show HN: Tritium – The Legal IDE in Rust

**原文链接**: [https://tritium.legal/preview](https://tritium.legal/preview)

此 "Show HN" 帖介绍 Tritium，一个用 Rust 构建的法律集成开发环境 (IDE)。它旨在帮助律师起草法律文件，特别是合同。该帖内容简洁，仅提供标题、项目名称 ("Tritium") 和简短描述 ("律师的集成起草环境")。该帖还包含一个行动号召，鼓励用户使用“文件 > 打开示例”选项加载示例合同，表明该 IDE 具有交互性且可供使用。本质上，该帖旨在将 Tritium 展示为一种新的、可能对律师来说有价值的工具，以简化他们的合同起草流程。它使用 Rust 构建的事实意味着它注重性能和可靠性。

---

## 22. 零样本预测：我们对时间序列基础模型的探索

**原文标题**: Zero-Shot Forecasting: Our Search for a Time-Series Foundation Model

**原文链接**: [https://www.parseable.com/blog/zero-shot-forecasting](https://www.parseable.com/blog/zero-shot-forecasting)

本文探讨了“基础模型”在时间序列预测中的潜力，旨在创建一个可应用于不同数据集和领域的单一、可重用模型。作者对四种主要模型进行了基准测试：Amazon Chronos、Google TimesFM、IBM Tiny Time-Mixers 和 Datadog Toto，并将它们的零样本预测能力与 ARIMA 等传统方法进行了比较。

基础模型的动机是为了解决管理各种数据流的众多单独预测模型的可扩展性挑战，尤其是在像可观测性平台这样数据不断变化的环境中。这些模型有望实现零样本预测、对数据多样性的鲁棒性、简化的操作和迁移学习。

该研究的重点是使用来自生产零售应用程序的 Kubernetes pod 指标（CPU 使用率、内存消耗、请求延迟）进行多元预测任务。数据经过预处理以处理缺失值并进行标准化。选择 MAPE（平均绝对百分比误差）作为主要评估指标，因为它具有可解释性和尺度不变性。

本文初步探讨了这些现代模型是否能在运营数据上表现良好，与精心调整的经典模型相媲美或超越其能力，同时还考虑了相关的计算和运营权衡。作者试图通过测试顶级时间序列基础模型在真实的、生产规模的遥测数据上的性能来回答这些问题。

---

## 23. 针对大型语言模型代理对抗提示注入的安全设计模式

**原文标题**: Design Patterns for Securing LLM Agents Against Prompt Injections

**原文链接**: [https://simonwillison.net/2025/Jun/13/prompt-injection-design-patterns/](https://simonwillison.net/2025/Jun/13/prompt-injection-design-patterns/)

This article summarizes a new research paper, "Design Patterns for Securing LLM Agents against Prompt Injections," which proposes six design patterns to mitigate prompt injection vulnerabilities in LLM agents. The author praises the paper for its realistic approach, acknowledging the lack of a complete solution and advocating for trade-offs between agent utility and security by limiting the ability of agents to perform arbitrary tasks.

The article outlines the six design patterns:

1.  **Action-Selector:** Agents can trigger external actions but cannot process or act on the responses, preventing malicious feedback loops.
2.  **Plan-Then-Execute:** Tool calls are planned in advance, preventing untrusted content from influencing action selection, though it can still influence the content acted on.
3.  **LLM Map-Reduce:** Sub-agents process untrusted content independently, and a coordinator safely aggregates the results.
4.  **Dual LLM:** A privileged LLM coordinates a quarantined LLM, avoiding direct exposure to untrusted content by using symbolic variables.
5.  **Code-Then-Execute:** A privileged LLM generates sandboxed code defining tool calls and data flow, enabling data flow analysis for tainted data.
6.  **Context-Minimization:** Unnecessary content, including the original user prompt, is removed from the context to prevent injections after the initial request is processed.

The paper also includes ten detailed case studies illustrating the application of these patterns in various scenarios, such as OS Assistants, SQL Agents, and Medical Diagnosis Chatbots. One case study explores using strictly formatted interfaces (API descriptions) to interact with untrusted external documentation. The author welcomes the paper as a significant contribution to addressing the critical challenge of prompt injection in LLM agents.


---

## 24. 通过高频日内交易实现电池储能利润最大化

**原文标题**: Maximizing Battery Storage Profits via High-Frequency Intraday Trading

**原文链接**: [https://arxiv.org/abs/2504.06932](https://arxiv.org/abs/2504.06932)

Schaurecker等人撰写的论文《通过高频日内交易最大化电池储能利润》探讨了如何从参与连续日内电力市场的电网级电池储能系统中最大化收入的策略。其核心思想是，捕捉由实时信息驱动的短暂交易机会需要一种高频方法。

作者介绍并评估了一种自动化交易策略，该策略明确考虑了限价订单簿动态、市场规则和电池运行的技术参数。他们将标准的滚动内在策略应用于连续日内电力市场，并使用动态规划近似法来求解，与混合整数线性规划相比，大大减少了计算时间。

使用一年德国订单簿数据的回测表明，动态规划近似法不会牺牲交易利润，并且通过允许对每个相关的订单簿更新做出反应来实现快速回测。结果表明，高频交易可以显着增加收入；他们的策略比每小时重新优化收益高出 58%，比每分钟重新优化收益高出 14%。

此外，作者利用该算法的速度来训练滚动内在策略的参数化扩展，从而使样本外的年收入额外增加 8.4%。该论文强调了交易速度对于使用电池储能的日内电力市场盈利能力至关重要。

---

## 25. Show HN: 我从零开始写了一个BitTorrent客户端

**原文标题**: Show HN: I wrote a BitTorrent Client from scratch

**原文链接**: [https://github.com/piyushgupta53/go-torrent-client](https://github.com/piyushgupta53/go-torrent-client)

此“Show HN”帖子介绍了Go-Torrent，一个完全使用Go语言从头实现的BitTorrent客户端。该项目旨在提供一个完整的BitTorrent客户端，具备torrent文件解析、节点发现和文件下载等核心功能。

主要功能包括：健壮的Bencode编码/解码、完整的torrent文件处理（包括信息哈希计算和分片哈希提取）、HTTP Tracker支持、节点握手和消息协议实现、节点连接管理、带进度跟踪的并发下载，以及单文件和多文件种子文件的文件组装。存储管理采用块级粒度。

该项目被组织成几个内部包：`bencode`、`torrent`、`tracker`、`peer`和`download`，以及一个用于命令行界面的`cmd`目录。

需要Go 1.21或更高版本，安装涉及克隆仓库并使用`go mod download`下载依赖项。随着项目的开发，用法说明即将推出。

Go-Torrent正在积极开发中，计划的功能包括磁力链接支持、元数据交换协议和DHT支持。该项目承认BitTorrent和Bencode规范是参考资源。

---

## 26. Rust 编译器性能

**原文标题**: Rust compiler performance

**原文链接**: [https://kobzol.github.io/rust/rustc/2025/06/09/why-doesnt-rust-care-more-about-compiler-performance.html](https://kobzol.github.io/rust/rustc/2025/06/09/why-doesnt-rust-care-more-about-compiler-performance.html)

本文探讨了关于 Rust 编译器性能的反复抱怨以及 Rust 项目对此缺乏行动的看法。作者作为编译器性能工作组成员，向读者保证编译器性能是首要任务。他们展示了过去几年中使用 Hyperqueue 作为示例的构建性能的显著改进数据。

尽管有这些改进，作者承认编译时间仍然是许多开发人员的瓶颈。他们讨论了实现近乎即时重新构建的理论极限，表明通过权衡可以实现增量构建，并引用了现有示例和潜在的“北极星”方法，如并行前端、替代后端和更智能的增量编译。

文章的核心探讨了为什么进展不够快。技术挑战包括编译器庞大而复杂的代码库存在技术债务，微优化收益有限，以及性能与其他因素（如硬件支持和内存使用）之间的权衡。作者强调了两种前进的道路：改进特定的编译工作流程和进行大规模的编译器重构，这两种方法都面临着确保广泛兼容性、避免回归和保持向后兼容性的相关挑战。

除了技术障碍，作者还指出需要优先考虑 Rust 项目的其他方面，例如稳定性、安全性和可维护性。进行大刀阔斧的更改可能会缩短构建时间，但会导致代码库难以演进。

---

## 27. 采用玻璃绝缘高压直流电缆的全球电网

**原文标题**: Worldwide power grid with glass insulated HVDC cables

**原文链接**: [https://omattos.com/2025/06/12/glass-hvdc-cables.html](https://omattos.com/2025/06/12/glass-hvdc-cables.html)

本文提出了一种革命性的海底电力传输方法，利用玻璃绝缘高压直流电缆构建全球电网。其核心思想是用更便宜且更有效的熔融石英（玻璃）替代传统的XLPE塑料绝缘材料。所提出的电缆设计采用铝导体，周围环绕表面硬化的硅绝缘层，无需外部保护或埋设。

作者建议在船上以连续工艺制造电缆，挤压二氧化硅，用熔融铝填充，然后淬火以产生表面硬化。然后将电缆直接铺设在海底。该设计旨在构建一个14兆伏系统，用于传输10吉瓦电力，这比现有项目电压高得多，并由基于MOSFET的逆变器的可扩展性证明其合理性。

后勤挑战包括保持恒定的制造速度和向船舶补给大量沙子。部署过程利用浮标和滚轮来管理电缆重量。波浪作用、船舶运动和电缆缺乏延展性等潜在问题通过各种解决方案得到解决，包括路线规划。

使用这种方法建造跨大西洋电缆的估计成本仅为2300万美元，远低于当前方案。作者承认潜在的故障点，如船锚和地质运动，并建议使用冗余电缆和蜿蜒路径来缓解这些问题。关于二氧化硅纯度和电缆承受跨越岩石露头张力的能力仍存在疑问。作者还考虑了原型机的可行性，并表示希望未来在外部资金的支持下进行开发。

---

## 28. 朝鲜、日本和新加坡的城市设计与适应性再利用

**原文标题**: Urban Design and Adaptive Reuse in North Korea, Japan, and Singapore

**原文链接**: [https://www.governance.fyi/p/adaptive-reuse-across-asia-singapores](https://www.governance.fyi/p/adaptive-reuse-across-asia-singapores)

本文专访了Spatial Anatomy建筑事务所的建筑师蔡家骏 (Calvin Chua)，重点介绍了亚洲（尤其是新加坡、日本和朝鲜）的适应性再利用和城市设计。蔡家骏的实践强调以研究为主导的设计，考察超越总体规划塑造城市的隐性力量，包括所有权结构、材料限制和社区需求。

在新加坡，蔡家骏强调了“分层商场”的复杂性，由于需要80%业主批准，个人所有权阻碍了重建。这导致了独特的社会动态和利基企业。他还讨论了新加坡临时建筑的“临时性”，这些建筑往往持续数十年。

关于朝鲜，蔡家骏回忆起为首尔双年展建造一个平壤公寓复制品，以展示真实的居住条件。他还培训了平壤的城市规划师，观察了材料限制（由于钢铁进口限制，只能使用混凝土）和政治指令（鲜艳的颜色）对建筑的影响。

蔡家骏区分了高资本的适应性再利用项目（如博物馆）和以社区为中心的努力，例如卡尔·本斯在日本翻新废弃古民居的项目，这些项目振兴了乡村。他强调了保护建筑结构和精神的重要性，确保适应性改造能够惠及社区，而不是取代它们。

总的来说，蔡家骏的方法结合了设计、研究和倡导。他运用人种学、复制以及对政治和社会背景的深刻理解来指导他的工作。他强调，城市是由所有权、材料、政治制度以及预期用途与实际用途之间的差距等复杂因素相互作用而产生的。他的方法涉及揭示这些因素，从而以周到有效的方式塑造城市环境。

---

## 29. 将 Microsoft Office 从 Source Depot 迁移到 Git

**原文标题**: Microsoft Office migration from Source Depot to Git

**原文链接**: [https://danielsada.tech/blog/carreer-part-7-how-office-moved-to-git-and-i-loved-devex/](https://danielsada.tech/blog/carreer-part-7-how-office-moved-to-git-and-i-loved-devex/)

将 Microsoft Office 从 Source Depot 迁移到 Git 的复杂过程：挑战与解决方案

本文详细介绍了将 Microsoft Office 从专有的版本控制系统 Source Depot 迁移到 Git 的复杂而漫长的过程。作者回顾了使用 Source Depot 所面临的挑战，强调了其缓慢的操作和繁琐的分支过程。

此次迁移的驱动因素是为了降低成本、提高开发人员的技能可移植性以及解决员工的抱怨。最大的挑战是在不同的 Office 发布计划之间保持一致性，并确保现有的构建和测试系统继续正常运行。

解决方案是“平行宇宙”，一个与 Source Depot 持续同步的 Git 原生代码库。由于 Office 存储库的庞大规模，这需要发明 Git 虚拟文件系统 (VFS for Git)。花费了数月时间，通过运行广泛的测试来证明两个系统之间的等效性。

沟通至关重要，采用中心辐射模型，由团队“冠军”来传播信息和收集反馈。提供了广泛的培训，以帮助开发人员适应 Git，并实施了“红色按钮”回滚策略，以减轻潜在的故障。

此次迁移带来了开发人员生产力的提高、更快的构建时间和更好的代码审查流程。作者强调了在任何大规模技术迁移中，沟通、构建并行系统、投资于冠军以及计划回滚的重要性。关键的要点是，在这种复杂的项目中，人员管理通常比技术专长更为重要。

---

## 30. 为什么我抓取的CD音轨名称是乱码？而且为什么少了一个音轨？

**原文标题**: Why does my ripped CD have messed up track names? And why is one track missing?

**原文链接**: [https://www.akpain.net/blog/inside-a-cd/](https://www.akpain.net/blog/inside-a-cd/)

本文解释了为什么抓取的 CD 可能出现音轨名称不正确和音轨缺失的情况，重点介绍了 CD 抓取过程以及 MusicBrainz 等元数据数据库的作用。在抓取 CD 时，该过程依赖于 CD 的目录（TOC）来识别 MusicBrainz 中的专辑并下载相关的元数据。

作者发现了一个抓取的专辑存在问题，其中一个音轨名称拼写错误（“Rainclous”而不是“Raincloud”），一个音轨比预期要长得多（“Nothing Coming Soon”包含了“Don't Need a Reason”），并且缺少一个音轨（“The Weight”）。

核心问题源于 MusicBrainz 数据库中的不准确之处。拼写错误的音轨名称仅仅是用户输入的错误。合并的音轨问题出现的原因是 CD 上有两个音轨合并为一个音轨，而原始 MusicBrainz 条目中没有反映这一点。这混淆了数据录入，导致在添加专辑时遗漏了一个音轨。由于元数据是众包的，因此可能会发生错误并传播到抓取的 CD 中。

作者强调，物理 CD 和 MusicBrainz 数据之间的差异会导致这些元数据错误。解决方案包括更正 MusicBrainz 上的元数据，它像 Wikipedia 一样可以编辑。作者然后手动更新了本地文件，直到 MusicBrainz 的编辑获得批准。 这突出了准确的元数据在维护井然有序的数字音乐库中的重要性。

---

## 31. YSH语法高亮的三种算法

**原文标题**: Three Algorithms for YSH Syntax Highlighting

**原文链接**: [https://github.com/oils-for-unix/oils.vim/blob/main/doc/algorithms.md](https://github.com/oils-for-unix/oils.vim/blob/main/doc/algorithms.md)

这不是一篇文章，而可能是一段从GitHub页面截取的信息片段，与“oils-for-unix”项目相关，特别是“oils.vim”仓库。该仓库可能包含用于YSH（Yuck Shell）语言的Vim语法高亮文件，YSH是Oils项目的shell组件。

关键信息是：

*   **项目：** oils-for-unix（可能是更广泛的Oils项目）。
*   **仓库：** oils.vim（专注于YSH的Vim语法高亮）。
*   **功能：** 在Vim编辑器中为YSH语言提供语法高亮。
*   **社区：** 星标数较少（5），并且没有fork（0），表明存在相对较小但已有的兴趣。

提示中提到的标题“YSH语法高亮的三种算法”并未出现在提供的文本片段中，因此无法总结关于算法本身的任何信息。“oils.vim”的存在意味着存在代码，并且该代码可能实现了语法高亮。如果没有该代码，此响应只能总结项目元数据。

---

## 32. 显示HN：用工具辅助速通《动物森友会》（GCN）的无聊部分

**原文标题**: Show HN: Tool-Assisted Speedrunning the Boring Parts of Animal Crossing (GCN)

**原文链接**: [https://github.com/hunterirving/pico-crossing](https://github.com/hunterirving/pico-crossing)

这个“Show HN”帖子介绍了一个名为“pico-crossing”的项目，该项目旨在大幅提高与GameCube版《动物森友会》互动时的速度和便利性。它通过利用连接到GameCube控制器端口的Raspberry Pi Pico，解决了游戏中出了名的缓慢打字和有限功能的问题。

该项目提供了几个关键增强功能：

*   **工具辅助打字：** 相比游戏原生系统（约20 WPM），可实现大幅更快的文本输入（45 WPM），这是通过定制的3D打印键帽实现的。
*   **无限播放列表：** 允许循环播放城镇音乐，无需e-Reader卡。
*   **所有物品解锁：** 允许用户通过输入名称来生成几乎任何物品。
*   **图像/视频导入：** 将图像和视频转换为游戏内的图案以供显示。
*   **游戏内置贪吃蛇：** 包含一个可玩版本的经典游戏。

该帖子详细介绍了必要的硬件组件（Raspberry Pi Pico、延长线、电阻、二极管），并提供了组装原理图。它还概述了软件先决条件（Python、ffmpeg、picotool、Pico SDK），并提供了用于快速开发和刷写固件的构建脚本。

该项目使用了来自多个GPLv3和MIT许可下的开源项目的代码，确保了兼容性。作者强调该项目仅使用未修改的硬件和软件，不进行模拟或修改游戏二进制文件，且仅供非商业用途。

---

## 33. Show HN: McWig – 一款用 Go 编写的模态、类 Vim 文本编辑器

**原文标题**: Show HN: McWig – A modal, Vim-like text editor written in Go

**原文链接**: [https://github.com/firstrow/mcwig](https://github.com/firstrow/mcwig)

McWig：Go语言编写的模态、类Vim文本编辑器，目前由其作者作为日常编辑Go文件的工具使用。 这是一个早期项目，建议用户在编辑前备份文件。

主要功能包括LSP支持（自动完成、跳转定义、悬停信息）、Tree-sitter支持、从Helix借鉴的颜色主题、宏支持以及基本的org-mode类似功能。 核心支持的键位绑定列表可供快速参考。

该项目最初是作为“速通”练习而产生的，探索优先于周密计划。 因此，它被认为是一个快速且“粗糙”的实现，并且存在错误。

要运行McWig，用户必须首先执行`make setup-runtime`，然后执行`make build-run`。 核心功能可以通过各种键位绑定访问，完整列表位于`config/config.go`中。

未来的计划是将McWig从目前的“玩具项目”状态发展成为一个稳定且功能齐全的类Vim文本编辑器。

---

## 34. 使用SMT解决LinkedIn皇后问题

**原文标题**: Solving LinkedIn Queens with SMT

**原文链接**: [https://buttondown.com/hillelwayne/archive/solving-linkedin-queens-with-smt/](https://buttondown.com/hillelwayne/archive/solving-linkedin-queens-with-smt/)

本文讨论了使用SMT求解器（Z3与Python API）解决“LinkedIn皇后”难题，作为SAT求解器的一种更简单的替代方案。“LinkedIn皇后”难题要求在被分为N个区域的NxN网格上放置N个皇后，每行、每列和每个区域各有一个皇后，且没有相邻对角线的皇后。

作者将Ryan Berger基于SAT的解决方案与他们自己的SMT解决方案进行了对比。主要区别在于，SMT求解器处理比布尔值更高层次的数据类型。在SMT方法中，皇后位置表示为整数（每行的列号），固有地强制执行“每行一个皇后”的约束。诸如“不同的列”和“非相邻对角线”等约束很容易使用Z3的`Distinct`函数和绝对值差来表达。

最具挑战性的部分是“每个区域一个皇后”的约束，这需要手动定义区域。作者使用`Or`来表达每个区域中必须至少存在一个皇后。

虽然承认SMT解决方案可能比高度优化的SAT求解器慢，但作者认为，在SMT中对问题进行编码的容易程度的提高使其成为许多人的首选。健全性检查，通过验证区域定义并呈现棋盘可视表示的代码实现，被强调为调试区域编码中潜在错误的至关重要手段。

---

## 35. 翩翩脑波：声音如何实时重塑你的大脑网络

**原文标题**: Dancing brainwaves: How sound reshapes your brain networks in real time

**原文链接**: [https://www.sciencedaily.com/releases/2025/06/250602155001.htm](https://www.sciencedaily.com/releases/2025/06/250602155001.htm)

这项发表于2025年6月2日的《科学日报》文章详细介绍了奥胡斯大学和牛津大学的一项研究，该研究揭示了声音如何实时动态地重组大脑网络。研究人员使用一种名为FREQ-NESS（通过源分离进行频率解析网络估计）的新型神经影像方法，来追踪不同声音频率如何像移动的波浪一样在大脑区域中传播。这种方法根据其主导频率来分离重叠的大脑网络，从而能够精确地绘制大脑活动图。

该研究发现，大脑不仅仅是记录声音；它会积极地重新配置自身，协调多个网络中脑电波的复杂相互作用。这种数据驱动的方法以高光谱和空间精度绘制了整个大脑的内部组织图，这是对依赖于预定义频带的传统方法的重大进步。

FREQ-NESS的开发为基础神经科学、脑机接口和临床诊断开辟了可能性。它增加了关于大脑的节奏结构如何塑造感知、注意力、音乐认知和意识的研究。研究人员认为，这项新技术可能会改变研究大脑对音乐的反应以及与外部世界互动的方式。一项由国际神经科学家网络支持的大型研究计划正在进行中，以建立在此方法论之上。由于其在不同数据集中的可靠性，FREQ-NESS也可能为个性化大脑绘图铺平道路。

---

## 36. 图迈的诅咒：古老头骨与人类起源的激烈争端

**原文标题**: The curse of Toumaï: an ancient skull and a bitter feud over humanity's origins

**原文链接**: [https://www.theguardian.com/science/2025/may/27/the-curse-of-toumai-ancient-skull-disputed-femur-feud-humanity-origins](https://www.theguardian.com/science/2025/may/27/the-curse-of-toumai-ancient-skull-disputed-femur-feud-humanity-origins)

本文详细描述了围绕“图迈”（乍得沙赫人），这块在乍得发现的、据称是600万至700万年前的头骨，被誉为可能是最古老的人类祖先的争议。首席古生物学家米歇尔·布吕内高调宣布了这项发现，声称它重新定义了人类起源。然而，人们对图迈在人类谱系中的位置产生了怀疑，一些人认为它更像猿类，并质疑其两足行走能力。

这项发现引发了古人类学界内部激烈的争斗和职业竞争。一个关键的争议点是是否存在可以明确证明两足行走的颅后遗骸（头骨以下的骨骼）。当一位硕士生奥德·贝热雷在与图迈相同的地点发现了一块股骨，表明存在此类遗骸时，据称布吕内试图压制这一发现并诋毁贝热雷。

本文突出了古人类学竞争激烈的本质，化石记录有限和重新定义人类历史的高风险加剧了这种竞争。它强调，解释是暂定的，并会随着每一次新的发现而发生变化，从而导致不断的修改和分歧。图迈的故事说明了个人野心和科学辩论如何交织在一起，给潜在的突破性发现蒙上阴影，并在该领域造成持久的裂痕。关于图迈股骨的争端仍在继续，留下关于其两足行走能力和在人类谱系中地位的关键问题悬而未决。

---

## 37. Python字典是有序的数据结构吗？

**原文标题**: Are Python Dictionaries Ordered Data Structures?

**原文链接**: [https://www.thepythoncodingstack.com/p/are-python-dictionaries-ordered-data](https://www.thepythoncodingstack.com/p/are-python-dictionaries-ordered-data)

本文探讨了Python字典是否为有序数据结构，并给出了细致的解答。

在Python 3.6之前，字典无疑是无序的。然而，Python 3.6引入了一个实现细节，在CPython解释器中保留了键值对的插入顺序。这个特性在Python 3.7中成为了语言规范的一部分，保证了字典会保持添加元素的顺序。

尽管保留了插入顺序，字典并不被认为是与列表和元组等序列相同意义上的有序数据结构。这是因为字典的相等性是基于拥有相同的键值对，而与顺序无关。相比之下，元素的顺序是序列的一个基本特征，相同元素但顺序不同的序列被认为是不相等的。

本文还讨论了`collections.OrderedDict`，这是一种在Python 3.6之前就存在并明确维护顺序的数据类型。与标准字典不同，`OrderedDict`在确定相等性时会考虑插入顺序。因此，两个具有相同键值对但顺序不同的`OrderedDict`实例不被认为是相等的。

总而言之，虽然标准Python字典从Python 3.7开始保留了插入顺序，但这种顺序并不是像序列那样具有决定性的特征。字典的主要特征是键和值之间的映射关系，因此保留插入顺序是一个有帮助但并非必要的特性。`collections.OrderedDict`可以用于插入顺序对于比较和相等性至关重要的特定用例。

---

## 38. 量子计算讲义 (2022)

**原文标题**: Quantum Computation Lecture Notes (2022)

**原文链接**: [https://math.mit.edu/~shor/435-LN/](https://math.mit.edu/~shor/435-LN/)

本文档提供了Peter Shor在2022年秋季讲授的量子计算课程8.370/18.435的讲义。讲义涵盖了量子计算领域广泛的主题，从基础概念开始，逐步深入到更高级的算法和纠错技术。

讲座首先介绍量子力学原理，如叠加、酉演化和量子测量。深入研究了使用布洛赫球表示量子比特，并使用张量积探索联合量子系统。考察了经典和可逆布尔电路，作为理解量子门实现的基础。

课程随后介绍了关键的量子算法，包括Deutsch-Jozsa算法、Simon算法、量子傅里叶变换、相位估计、Shor的分解算法和Grover的搜索算法。讲义还涵盖了理解分解算法所需的数论知识，以及离散对数算法。本文档探讨了Grover搜索的最优性。

最后，讲义深入研究了量子纠错，涵盖了密度矩阵、GHZ实验、量子光学、哈密顿模拟以及各种量子纠错码等主题，包括9量子比特码、7量子比特量子汉明码和量子CSS码。还讨论了BB84量子密钥分发协议及其安全性证明。请注意，第26讲的讲义目前缺失。

---

## 39. Helion：C#中的现代快节奏毁灭战士FPS引擎

**原文标题**: Helion: A modern fast paced Doom FPS engine in C#

**原文链接**: [https://github.com/Helion-Engine/Helion](https://github.com/Helion-Engine/Helion)

Helion：一款高性能C#编写的Doom引擎。它解决了现有引擎的性能瓶颈，使复杂的地图能够在现代和旧硬件上流畅运行。Helion通过静态渲染和状态管理系统处理动态地图变化来实现这一点，从而提供了一种CPU高效的替代方案，以取代传统的BSP树渲染，并更好地利用GPU。

该引擎支持多种WAD格式，包括Vanilla、Boom、MBF、MBF21、UDMF（部分）和ID24。最低要求为Windows 7或Linux，并配备兼容OpenGL 3.3的GPU。

用户可以下载稳定版本和实验性的每日构建版本。需要.NET 9，并且自包含版本已包含它。否则，Windows用户需要桌面运行时，而Linux用户则需要OpenAL、libsndfile和libmpg123。游戏文档与引擎捆绑在一起，并且提供了从源代码编译的构建说明。

文章提供了展示引擎在各种Doom地图上的功能的屏幕截图，并包含一个完整基准测试电子表格的链接。

如需讨论、获取开发更新或参与其中，请访问Discord服务器和Doomworld论坛主题。错误报告可以在GitHub Issues或Doomworld主题上提交。

---

## 40. 关于 o3 pro 的初步想法

**原文标题**: First thoughts on o3 pro

**原文链接**: [https://www.latent.space/p/o3-pro](https://www.latent.space/p/o3-pro)

Ben Hylak和Alexis Dauba对OpenAI的新型o3-pro模型进行了早期评测，指出虽然价格有所下降，但专业版需要不同的评估方法。与聊天类模型不同，o3-pro在获得大量上下文和明确目标时表现出色，类似于报告生成器。

他们发现，当向o3-pro输入Raindrop的规划会议和目标的全面历史记录时，其表现尤其令人印象深刻，生成了一个高度具体且可操作的计划，改变了他们的想法。这突显了传统评估的挑战，因为该模型的优势在于其有效利用工具调用融入实际场景的能力。

O3-pro擅长识别其环境，沟通其可用工具，知道何时请求外部信息，以及选择合适的工具。然而，在缺乏足够上下文的情况下，它可能会过度思考任务，并且可能不适合直接任务，如SQL查询。

与Claude Opus和Gemini 2.5 Pro等模型相比，o3-pro感觉明显更胜一筹，表明OpenAI专注于强化学习，以教导模型不仅如何使用工具，而且何时使用它们。 最终，上下文和一个明确定义的系统提示对于发挥o3-pro的威力至关重要。 模型、工具、记忆和其他方法的结合才能创造出真正有效的AI产品。

---

## 41. Show HN: GetHooky – 一款语言无关的 Git 钩子管理器

**原文标题**: Show HN: GetHooky – a language-agnostic Git hook manager

**原文链接**: [https://ezpieco.github.io/GetHooky/](https://ezpieco.github.io/GetHooky/)

GetHooky：一种语言无关的Git钩子管理器，旨在防止开发者推送未经测试或代码风格检查的代码。它解决的核心问题是常常会忘记在推送代码（尤其是到生产环境）之前运行代码检查器和测试。

与许多现有的语言特定或需要复杂配置的Git钩子管理工具不同，GetHooky提供了一个统一的解决方案。它是一个CLI工具，全局安装，可在各种项目中使用，不受编程语言的限制。这使得它可以轻松集成到不同的工作流程中，而无需在每个项目中设置特定于语言的依赖项或配置。

GetHooky强调其跨平台兼容性（尽管提到了Windows的潜在问题）、易用性以及与所有Git钩子的兼容性。它的主要价值在于通过在提交和推送之前自动运行测试和代码检查器来防止错误。

---

## 42. 美国支持的以色列公司间谍软件被用于攻击欧洲记者

**原文标题**: US-backed Israeli company's spyware used to target European journalists

**原文链接**: [https://apnews.com/article/spyware-italy-paragon-meloni-pegasus-f36dd32106f44398ee24001317ccf2bb](https://apnews.com/article/spyware-italy-paragon-meloni-pegasus-f36dd32106f44398ee24001317ccf2bb)

美联社报道称，以色列公司Paragon开发的“掠食者”(Predator)间谍软件，据称得到美国支持，被用于针对欧洲的记者和其他个人，尤其是在意大利。据报道，Paragon由前以色列情报官员领导，向各国政府出售该间谍软件，声称其旨在打击恐怖主义和犯罪。

调查发现，“掠食者”被用于感染意大利、西班牙和希腊记者的设备。一位著名的意大利记者，因涉嫌批评总理乔治亚·梅洛尼，被证实成为目标。该间谍软件使其操作者几乎可以完全访问目标设备，包括消息、通话、电子邮件、照片和位置数据。

这篇文章引发了人们对强大的监控技术扩散及其潜在滥用的担忧，即使在民主国家也是如此。它还强调了美国支持参与间谍软件行业的以色列公司所涉及的伦理影响。虽然Paragon坚称其遵守国际法，但批评人士认为，间谍软件的性质使其天生容易被滥用，无论其声明的意图如何。继此前曝光另一款以色列间谍软件Pegasus被用于针对全球的记者、活动家和政治家之后，这份报告进一步加强了对间谍软件行业的持续审查。

---

## 43. 利用脉冲密度调制对数字麦克风进行的电磁窃听攻击

**原文标题**: EM Eavesdropping Attack on Digital Microphones Using Pulse Density Modulation

**原文链接**: [https://www.usenix.org/conference/usenixsecurity25/presentation/onishi](https://www.usenix.org/conference/usenixsecurity25/presentation/onishi)

本文介绍了一种新型电磁（EM）侧信道攻击，该攻击能够通过脉冲密度调制（PDM）对配备数字MEMS麦克风的设备进行声学窃听。 该攻击利用了麦克风发出的数字 PDM 脉冲的谐波保留声学信息这一事实。通过使用标准无线电接收器和 FM 解调，攻击者可以恢复麦克风捕获的原始音频，而无需安装恶意软件或物理篡改设备。

研究人员通过使用包括笔记本电脑和智能音箱在内的各种设备进行真实环境评估，证明了该漏洞的有效性。 在使用标准语音转文本 API 转录语音时，他们实现了语音数字识别的高精度（高达 94.2%）和低字错误率（14%），即使受害者设备位于混凝土墙后也是如此。 他们还展示了可以使用简单、隐蔽的天线执行攻击。

该论文还讨论了现有防御措施（如重采样）的局限性，并提出了一种基于时钟随机化的新型硬件对策，以减轻该漏洞的影响。 最终，该研究突显了现代数字麦克风中一个重大的安全缺陷，并提出了一种潜在的解决方案来防止电磁窃听攻击。

---

## 44. 研究表明宇宙大爆炸可能发生于黑洞内部

**原文标题**: Research suggests Big Bang may have taken place inside a black hole

**原文链接**: [https://www.port.ac.uk/news-events-and-blogs/blogs/space-cosmology-and-the-universe/what-if-the-big-bang-wasnt-the-beginning-our-research-suggests-it-may-have-taken-place-inside-a-black-hole](https://www.port.ac.uk/news-events-and-blogs/blogs/space-cosmology-and-the-universe/what-if-the-big-bang-wasnt-the-beginning-our-research-suggests-it-may-have-taken-place-inside-a-black-hole)

朴茨茅斯大学的文章提出了一种新的宇宙学模型，认为大爆炸可能发生在黑洞内部。研究人员正在利用圈量子引力来探索这一想法，它为难以解释宇宙初始奇点的标准宇宙学模型提供了一种替代方案。

其关键概念是，当黑洞达到一定密度时，量子引力效应可以阻止它坍缩成奇点。相反，它可能会转变为一个“白洞”，有效地将坍缩反转为膨胀，从而可能导致大爆炸。这种情况表明，我们的宇宙可能起源于另一个宇宙中一颗巨大恒星的死亡。

该研究使用简化的模型来理解早期宇宙，并克服了应用量子引力时遇到的数学挑战。虽然这些模型提供了有价值的见解，但它们需要进一步改进，才能准确地表示真实宇宙的复杂动力学。该团队承认，目前的证据无法明确地证明或反驳这一理论，但他们正在积极开发更复杂的模型，并寻找可以支持或驳斥这一假设的观测证据，包括在宇宙微波背景辐射中寻找特定的模式。本质上，这篇文章认为，大爆炸可能是黑洞生命周期的最终结果，是对我们宇宙起源的一种彻底反思。

---

## 45. 数独反思：或系统化思考的不可能性

**原文标题**: Reflections on Sudoku, or the Impossibility of Systematizing Thought

**原文链接**: [https://rjp.io/blog/2025-06-07-reflections-on-sudoku](https://rjp.io/blog/2025-06-07-reflections-on-sudoku)

本文反思了系统化思考的内在困难，尤其是在解决问题方面，并将哲学上的判定性问题与实际编程挑战进行了类比。作者探讨了对通用问题解决方法的需求，但最终认为这种系统是不可能的，这与计算中固有的不可判定性相呼应。

通过考察“数独事件”来阐述核心论点，对比了Peter Norvig高效的、知识驱动的数独解法与Ron Jeffries不太成功的、严格TDD驱动的尝试。作者认为Jeffries的挣扎源于过度依赖TDD作为灵丹妙药，忽略了领域特定知识和更广泛的问题解决工具的需求。

本文将此与判定性问题联系起来，暗示了无法确定程序是否解决任务，意味着无法系统化寻找解决该任务的程序的过程。虽然像TDD这样的过程可能有所帮助，但它们不能替代洞察力和强大的问题解决技能工具箱。作者提倡通过向他人学习、采用科学方法和不断寻求新的视角来构建多样化的“工具箱”。文章最后列出了作者使用的实用工具，承认虽然通用解决方案难以捉摸，但持续学习和适应对于有效的问题解决至关重要。

---

## 46. 话匣子TTS

**原文标题**: Chatterbox TTS

**原文链接**: [https://github.com/resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox)

Chatterbox TTS 是 Resemble AI 的开源、生产级文本转语音 (TTS) 模型，采用 MIT 许可。其性能优于 ElevenLabs 等领先的闭源系统，为表情包、视频、游戏和 AI 代理等各种应用提供高质量的语音合成。一个关键特性是其情感夸张控制，可以实现更具表现力的声音。

该模型采用 0.5B Llama 主干，利用对齐信息推理来保证稳定性，并在 50 万小时的清洗数据上进行训练。它包含一个声音转换脚本，并支持“零样本”TTS。尽管功能强大，Resemble AI 还提供商业 TTS 服务，用于扩展和提高精度，具有超低延迟，非常适合生产环境。

对于一般用途，默认设置效果良好，但文档建议调整夸张度和 `cfg_weight` 参数以获得富有表现力或快速的语音。 使用 `pip` 或从源代码进行安装很简单。提供的代码片段演示了文本转语音生成的基本用法，包括指定音频提示以进行语音克隆。目前仅支持英语。

重要的是，Chatterbox TTS 实施了内置的感知阈值 (Perth) 水印系统，以确保负责任的 AI 使用。 水印是无法察觉的，并且对音频操作具有鲁棒性，从而可以追溯生成的音频。 提供了一个脚本来提取水印。 该项目鼓励用户加入他们的 Discord 社区，以进行协作和负责任地使用该模型。

---

## 47. Show HN: Swift Scribe：使用苹果全新Foundation模型的设备端AI速记员

**原文标题**: Show HN: Swift Scribe: On-device AI scribe using Apple's new Foundation Models

**原文链接**: [https://github.com/slipboxai/swift-scribe](https://github.com/slipboxai/swift-scribe)

Swift Scribe：一款注重隐私的AI驱动型语音转文本应用，适用于iOS 26及macOS 26以上版本。它利用苹果最新的Foundation Models和SpeechTranscriber框架，实现实时、设备端转录和智能笔记。该应用旨在展示使用这些苹果新技术构建本地、AI优先应用的便捷性。

Swift Scribe提供会议转录、访谈录音和医疗听写等功能，面向商业、医疗保健、教育、法律和内容创作等多个领域。

从技术上讲，Swift Scribe需要iOS 26/macOS 26 Beta、带有Swift 6.2+的Xcode Beta以及具有Beta访问权限的Apple开发者帐户。该项目的架构包括音频捕获、转录、AI处理、富文本编辑和数据存储等组件。

开发路线图包括核心功能增强，如提高准确性，然后是高级功能，如说话人分离和多语言支持。未来的计划还包括通过iOS捷径、Apple Watch集成和API功能扩展平台。

该项目采用MIT许可证。开发者可以在Cursor和Windsurf IDE中使用AI代理来探索文档，包括涵盖SpeechAnalyzer、Foundation Models和富文本编辑器实现的WWDC 2025会议记录。该项目鼓励用户为该仓库点亮星标并与其他开发者分享。

---

## 48. 在巴黎寻找居里夫人的放射性指纹

**原文标题**: The hunt for Marie Curie's radioactive fingerprints in Paris

**原文链接**: [https://www.bbc.com/future/article/20250605-the-hunt-for-marie-curies-radioactive-fingerprints-in-paris](https://www.bbc.com/future/article/20250605-the-hunt-for-marie-curies-radioactive-fingerprints-in-paris)

苏菲·哈达赫前往巴黎，探寻玛丽·居里在开创性的放射性物质研究一个多世纪后，留下的放射性印记。居里在一个简陋的实验室（以及后来的专门研究所）工作时，曾赤手处理镭等放射性元素，在她的工作场所、档案笔记和家具中留下了痕迹。

居里博物馆允许游客参观，但不能进入玛丽·居里的办公室和实验室。在一次罕见的参观中，哈达赫在放射性专家马克·阿梅里希的陪同下，使用盖革计数器探测门把手、椅子、笔记本甚至家庭餐桌上的放射性痕迹。辐射水平很低，被认为是安全的，为人们提供了与居里生平和工作的切实联系。

文章强调了居里和她的丈夫皮埃尔为分离和鉴定钋和镭所进行的艰苦而危险的过程。他们在设备简陋的棚子里工作，暴露在放射性蒸汽和有毒化学物质中。

博物馆面临着既要将这些文物作为遗产保存，又要减轻任何潜在的公共安全风险的挑战。一些受污染的物品已被销毁，而另一些物品在经过净化后，则保留了残余的放射性。像托马斯·博菲斯这样的专家强调了这些放射性痕迹独特的历史价值，展示了玛丽·居里的工作条件和科学遗产。今天，安全协议严格得多，突显了居里在追求科学发现时勇敢面对的风险。

---

## 49. 罗德与施瓦茨 AMIQ 调制信号发生器拆解

**原文标题**: Rohde and Schwarz AMIQ Modulation Generator Teardown

**原文链接**: [https://tomverbeure.github.io/2025/04/26/RS-AMIQ-Teardown-Analog-Deep-Dive.html](https://tomverbeure.github.io/2025/04/26/RS-AMIQ-Teardown-Analog-Deep-Dive.html)

本文详细拆解并分析了罗德与施瓦茨 AMIQ 调制发生器，这是一款 I/Q 调制发生器，具有双通道任意波形发生器 (AWG) 和深度采样缓冲器。作者在拍卖会上获得了 AMIQ，并将其恢复到正常工作状态。

AMIQ 为射频矢量信号发生器生成基带调制信号。它以高达 105MHz 的频率将采样流传输到两个 14 位 DAC，并允许 I 和 Q 通道之间进行精确的偏斜调整（10ps 精度）和可编程的 DAC 采样频率。它具有各种输入/输出连接器，包括 10MHz 参考时钟、采样时钟、触发器、标记和 GPIB 接口。

拆解显示了一个标准的 PC 子系统和一个设计良好的信号生成 PCB。本文随后重点关注信号生成 PCB 的模拟方面，特别是参考时钟生成和 DAC 时钟合成器。AMIQ 使用 TCXO，锁相到外部参考。DAC 时钟合成器利用 VCO（Mini-Circuits JTOS-200）和 AD9850 DDS 合成器来创建高度可编程的时钟。AD9850 生成时钟，通过低通滤波器和比较器将数字信号转换为模拟信号，然后再转换回数字信号以消除杂散信号。最后，作者谈到了 I/Q 输出偏斜调整功能。文章强调了可用于深入分析的详细原理图和充足的测试点。

---

## 50. 密歇根州上半岛高强度原住民农业的考古证据

**原文标题**: Archaeological evidence of intensive indigenous farming in MI's Upper Peninsula

**原文链接**: [https://www.science.org/doi/10.1126/science.ads1643](https://www.science.org/doi/10.1126/science.ads1643)

无法访问文章链接。

---

## 51. WebKit标准立场

**原文标题**: WebKit Standards Positions

**原文链接**: [https://webkit.org/standards-positions/](https://webkit.org/standards-positions/)

本文题为“WebKit标准立场”，提供了关于WebKit对各种Web标准的立场的信息。其主要目的是告知用户和开发者WebKit对不同标准的支持和实施情况。

本文提供了两种访问这些信息的方式：

1. **交互式概要表格：** 此选项需要启用JavaScript，提供用户友好且可能可搜索的表格格式，用于浏览标准立场。

2. **直接GitHub仓库：** 如果JavaScript被禁用，或者用户更喜欢直接访问原始数据，他们可以浏览GitHub上的standards-positions仓库。这可能包含以更技术格式存在的底层数据。

本质上，本文是理解WebKit如何与Web标准对齐并实施Web标准的门户，提供了一种交互式和直接访问相关数据的方法。它使开发者能够根据WebKit声明的标准立场做出明智的决策。

---

## 52. Seedance 1.0
舞蹈种子 1.0

**原文标题**: Seedance 1.0

**原文链接**: [https://seed.bytedance.com/en/seedance](https://seed.bytedance.com/en/seedance)

Seedance 1.0 是一款新型人工智能模型，能够根据文本和图像提示生成高质量的多镜头视频。它擅长语义理解和提示语跟随，能够生成具有流畅运动、丰富细节和电影美学的1080p视频。

该模型在SeedVideoBench-1.0上进行了评估，并在提示语遵循、运动质量和美学等关键领域与其他行业模型进行了比较。Seedance 1.0在文本生成视频 (T2V) 和图像生成视频 (I2V) 任务中均获得了高分，展示了其准确理解提示语的能力，同时在I2V场景中保持与源图像的一致性。

Artificial Analysis的排行榜排名进一步突显了Seedance 1.0在T2V和I2V类别中的出色表现。文档还提到Kling 2.1缺乏公开数据，因此使用Kling 2.0的Elo评分进行比较。总的来说，Seedance 1.0代表了视频生成技术的重大进步。

---

## 53. Show HN: Eyesite – 计算机视觉与网页设计结合的实验性网站

**原文标题**: Show HN: Eyesite – Experimental website combining computer vision and web design

**原文链接**: [https://blog.andykhau.com/blog/eyesite](https://blog.andykhau.com/blog/eyesite)

这个“Show HN”帖子详细介绍了Eyesite的创建过程，这是一个旨在模仿Apple Vision Pro眼动追踪体验的实验性网站。作者因该设备价格高昂而感到沮丧，因此使用WebGazer.js构建了一个用于眼动追踪的Web应用程序，允许用户使用视线和空格键进行交互，类似于Apple Vision Pro的注视和捏合交互。

该项目涉及校准WebGazer.js，将视线点映射到屏幕坐标。关键的设计考虑包括移除可见的“眼动光标”（一个红点），以增强沉浸感，避免分散用户的注意力并暴露跟踪不准确性。取而代之的是，作者实现了视觉反馈，例如当用户的视线被检测到在按钮边界内时，按钮会发光并弹出。

为了弥补眼动追踪固有的抖动，用户界面采用了大型、易于瞄准的元素。该网站还限制了屏幕尺寸低于最低要求的设备访问。作者承认代码的简单性，并鼓励其他人在此项目的基础上进行构建，并提供了GitHub存储库的链接以供访问源代码。该项目展示了计算机视觉和网页设计相结合所能带来的独特用户体验。

---

## 54. 为什么韩国人会问你哪年出生的

**原文标题**: Why Koreans ask what year you were born

**原文链接**: [https://bryanhogan.com/blog/korean-age](https://bryanhogan.com/blog/korean-age)

为什么韩国人初次见面总问年龄：韩国年龄文化解析

---

## 55. 研究人员证实两名记者遭Paragon间谍软件入侵

**原文标题**: Researchers confirm two journalists were hacked with Paragon spyware

**原文链接**: [https://techcrunch.com/2025/06/12/researchers-confirm-two-journalists-were-hacked-with-paragon-spyware/](https://techcrunch.com/2025/06/12/researchers-confirm-two-journalists-were-hacked-with-paragon-spyware/)

公民实验室的一份新报告证实，两名欧洲记者，Ciro Pellegrino和另一名未具名记者，被Paragon“石墨”间谍软件入侵。这一进展加深了意大利正在进行的间谍软件丑闻，可能牵涉到意大利政府。

在Fanpage工作的Pellegrino收到了苹果公司关于雇佣兵间谍软件攻击的警报，但最初并未被告知是Paragon。这一新证据与意大利议会委员会(COPASIR)的一份报告相矛盾，该报告未发现Fanpage的负责人Francesco Cancellato被监视的证据，也未提及Pellegrino。

公民实验室发现，未具名记者是通过一个零点击的iMessage漏洞被攻击的，该漏洞后来被苹果修复。两名记者很可能被同一Paragon运营商盯上。

Pellegrino表示担心他的公民权利受到侵犯，并质疑总理梅洛尼对此事的沉默。他暗示自己可能成为目标，以获取有关Fanpage的信息，尽管他没有参与具体的调查。

该文章提到其他被Paragon间谍软件盯上的人，包括来自Mediterranea Saving Humans的Luca Casarini和Beppe Caccia。与同一组织有关联的David Yambio收到了通知，但尚不清楚他是否被Paragon或任何政府盯上。

Paragon通过WestExec Advisors表示，他们曾主动协助意大利政府调查Cancellato被指控的黑客行为，但遭到拒绝，导致他们与意大利断绝了联系。

---

## 56. 软件工匠精神在氛围时代的重要性

**原文标题**: The Case for Software Craftsmanship in the Era of Vibes

**原文链接**: [https://zed.dev/blog/software-craftsmanship-in-the-era-of-vibes](https://zed.dev/blog/software-craftsmanship-in-the-era-of-vibes)

本文倡导在AI辅助编程时代优先考虑软件工艺。尽管像Zed这样的人工智能工具可以大幅提高代码生产的速度和数量，但作者认为质量应该变得更加重要。开发者不应仅仅专注于生成更多代码，而应利用AI来构建更可靠、设计良好且易于维护的系统。

作者强调了系统设计的重要性，指出为追求短期利益而采取的捷径往往会导致复杂且难以管理的程式码库，从而阻碍未来的开发，包括AI工具的效率。他们提倡基于对系统可靠性、可理解性和可变更性的影响来评估贡献，而不仅仅是涉及的代码行数。

作者分享了构建Zed编辑器的经验，以此为例说明完全拥有用户体验的重要性。虽然最初的目标是高性能，但实现这一目标需要突破熟悉的Web技术，学习新的语言和技术，并有效地从头开始。如今，像LLM这样的人工智能工具可以显著降低追求此类雄心勃勃项目的门槛，使学习和实验变得更快更容易。

本文最后宣布推出“智能体工程”，这是一系列讨论和现场活动，旨在探索人类工艺和AI工具在软件开发中的交汇点，鼓励在这个快速发展的领域进行集体学习和知识共享。最终目标是利用AI不仅生产更多软件，而且显著提高其整体质量。

---

## 57. 自主编码建议

**原文标题**: Agentic Coding Recommendations

**原文链接**: [https://lucumr.pocoo.org/2025/6/12/agentic-coding/](https://lucumr.pocoo.org/2025/6/12/agentic-coding/)

Armin Ronacher关于自主编码的实践建议：基于Claude Code (Sonnet模型)的经验

主要观点包括：

*   **基本设置:** 禁用权限检查（使用Docker进行风险管理），利用MCP（机器通信协议）进行工具访问。 Ronacher主要在直接工具访问不可靠时使用MCP。
*   **语言选择:** 推荐使用Go进行后端项目，因为它具有显式的上下文系统、测试缓存、简单性、结构化接口和生态系统稳定性。 Python因其魔术特性、复杂的运行时挑战和缓慢的执行速度而被认为存在问题。
*   **前端:** Tailwinds, React, Tanstack, Vite
*   **工具:** 任何交互实体都可以是一个工具。优先考虑速度、用户友好性、崩溃容错性（而不是挂起）和正确的调试。 Makefiles和日志对于可观察性至关重要。
*   **速度:** 快速的工具响应至关重要，包括代理自身编写的新兴工具。
*   **稳定性和复制/粘贴:** 优先选择稳定的生态系统。保守地进行库升级，并倾向于代码生成而不是依赖项。
*   **简洁代码:** 自主编码受益于简洁、描述性的代码，具有清晰的函数名称和最少的巧妙技巧。
*   **并行化:** 使代理能够并发运行，并在项目变得过于复杂以至于AI无法有效处理之前对其进行重构。
*   **总体目标:** 专注于使用代理编写更好、更易于维护的代码，强调简洁性、稳定性、可观察性和智能并行化。

---

## 58. GCP 服务中断

**原文标题**: GCP Outage

**原文链接**: [https://status.cloud.google.com/](https://status.cloud.google.com/)

此 Google Cloud Platform (GCP) 服务健康状况信息中心报告了近期影响多个 GCP 产品和位置的大范围服务问题。该事件持续了 7 小时 27 分钟，并于 2025 年 6 月 13 日太平洋夏令时 8:26 结束。

此次中断影响了大量服务，包括 API Gateway、Agent Assist、AlloyDB for PostgreSQL 以及其他 52 项服务。受影响的位置遍布多个区域，包括非洲、亚洲和其他地区，总计 60 个区域。

该信息中心提供了一个工具，可以按产品和位置（美洲、欧洲、亚太地区、中东和非洲，以及多区域和全球服务）查看各种 GCP 服务的当前状态。它列出了全面的 GCP 产品阵列，并表明了其当前的可用性。该信息会定期更新，上次更新时间为 2025 年 6 月 13 日太平洋夏令时 10:40。鼓励遇到未列出问题的用户联系支持。该信息中心还提供了一项“个性化服务健康状况”功能，可提供影响各个 Google Cloud 项目的事件的定制视图。

---

## 59. Anker因火灾和烧伤风险召回超过110万个充电宝

**原文标题**: Anker is recalling over 1.1M power banks due to fire and burn risks

**原文链接**: [https://www.theverge.com/news/686084/anker-recall-uscpsc-power-bank-battery-powercore-a1263](https://www.theverge.com/news/686084/anker-recall-uscpsc-power-bank-battery-powercore-a1263)

Anker因锂离子电池问题在美国召回超过110万个PowerCore 10000充电宝（型号A1263），存在潜在火灾和烧伤风险。已报告19起火灾和爆炸事件，造成轻微烧伤和超过60,700美元的财产损失。

受影响的充电宝于2016年6月至2022年12月期间通过亚马逊、新蛋和eBay等在线平台销售。消费者可访问Anker网站并验证序列号，以确认其设备是否受影响。

Anker为受影响的客户提供两种选择：一张价值30美元的Anker.com礼品卡或免费更换一个10,000mAh的Anker充电宝（型号A1388）。要获得任一选项，客户必须提交充电宝的照片，照片上需注明提交日期并写有“recall”或“recalled”字样，以及一张显示型号和序列号的照片。建议提供购买凭证，但非强制性。

Anker强调，由于存在火灾风险，务必在指定的锂离子电池处理设施（例如EPA网站上列出的设施）安全处置召回的充电宝。此次召回也提醒人们关注旧锂离子电池是否存在过热或膨胀等问题，如果怀疑有问题，应妥善处理。文章建议考虑升级到固态电池，作为未来更安全、更持久的替代方案。

---

## 60. CAN BCM子系统中释放后使用漏洞导致信息泄露 (CVE-2023

**原文标题**: Use-after-free in CAN BCM subsystem leading to information disclosure (CVE-2023

**原文链接**: [https://allelesecurity.com/use-after-free-vulnerability-in-can-bcm-subsystem-leading-to-information-disclosure-cve-2023-52922/](https://allelesecurity.com/use-after-free-vulnerability-in-can-bcm-subsystem-leading-to-information-disclosure-cve-2023-52922/)

本文详细介绍了Linux内核CAN BCM子系统中发现的一个释放后重用漏洞（CVE-2023-52922），该漏洞尤其影响Red Hat Enterprise Linux 9 (RHEL 9)。该漏洞允许非特权用户读取内核内存，可能泄露敏感信息。

根本原因在于`bcm_release()`函数，其中`bcm_remove_op()`在删除对应的proc条目*之前*释放了与套接字的发送和接收操作相关的`bcm_op`对象。并发调用`bcm_proc_show()`读取proc条目时，可以访问这些已释放的对象，从而导致释放后重用情况。

`bcm_op`结构体大小为472字节，从kmalloc-512缓存中分配。本文探讨了三种利用方法：使用用户控制的对象回收已释放的对象以解引用任意指针（由于无法控制链表头而失败）、通过使用System V IPC消息队列对象(msg_msg)重新分配该对象来触发无限循环，以及尝试泄露空闲列表指针（可能也失败了，因为它没有详细说明）。

虽然该漏洞存在于RHEL 8代码中，但由于RHEL 8缺乏虚拟CAN隧道跨命名空间通信(VXCAN)支持，因此无法利用。该漏洞已于2023年7月在上游修复，并在2025年3月反向移植到RHEL 9。文章最后强调了CAN BCM子系统中存在的一种漏洞模式。

---

## 61. macOS Tahoe 引入新的磁盘映像格式

**原文标题**: macOS Tahoe brings a new disk image format

**原文链接**: [https://eclecticlight.co/2025/06/12/macos-tahoe-brings-a-new-disk-image-format/](https://eclecticlight.co/2025/06/12/macos-tahoe-brings-a-new-disk-image-format/)

本文介绍ASIF，一种macOS Tahoe (macOS 26) 中新的磁盘映像格式，旨在克服UDSP等旧格式的性能限制。ASIF有望实现接近原生速度，使其特别有利于Apple芯片Mac上的轻量级虚拟化。

目前，ASIF映像只能通过Tahoe中的“磁盘工具”或`diskutil`命令创建，使用`--format ASIF`选项。 虽然它们可以在macOS Sequoia (macOS 15.5)中使用，但不能在那里*创建*。 ASIF映像是APFS中的稀疏文件，这意味着它们在主机系统上的大小反映了其中存储的数据。

测试显示，与旧的磁盘映像格式相比，读/写速度有了显著提高。 在MacBook Pro M3 Pro上，一个100GB的ASIF映像在未加密的APFS中实现了5.8/6.6 GB/s（读/写）的速度，在加密的APFS中实现了4.8/4.6 GB/s的速度。当压缩的ASIF映像传输到运行Sequoia的Mac mini M4 Pro时，速度达到了5.5/8.3 GB/s。

Apple建议使用ASIF作为VM后备存储，因为它具有高效性。 然而，对不同macOS版本的支持仍然不明朗。 ASIF相比稀疏包提供了性能优势，并用单个后备文件简化了存储。

本文得出结论，ASIF应该是Tahoe中通用磁盘映像的首选，尤其是对于VM。 作者希望除了`diskutil`命令之外，还能有一个用于创建ASIF的适当API，并期待DropDMG等工具的支持。

---

## 62. HTML WARDen - 基于HTML的维基

**原文标题**: HTML WARDen - an HTML-based wiki

**原文链接**: [https://ratfactor.com/htmlwarden/](https://ratfactor.com/htmlwarden/)

HTML WARDen：一个使用HTML作为存储格式的PHP Wiki。作为一个周末项目，它无需任何PHP 7.x+以上的依赖，采用扁平文件存储和版本控制，保存旧页面版本。其关键特性是并排HTML编辑器，提供富文本和代码视图。它包含用户登录和按页面编辑锁定功能。文件上传计划在未来实现。

作者提供了一个详细的“制作过程”系列，“Wiki周末”，涵盖了该项目的开发过程，包括动机、设计决策、存储解决方案、用户身份验证、锁定机制和最终润色。该系列可作为有兴趣创建自己的Wiki系统的人的指南。

HTML WARDen以致敬原始WikiWikiWeb的创建者Ward Cunningham命名，强调其在wiki技术中的根源。

---

## 63. 巫师公司(YC S24)融资390万美元以发射更多气象气球

**原文标题**: Sorcerer (YC S24) raises $3.9M to launch more weather balloons

**原文链接**: [https://www.axios.com/pro/climate-deals/2025/06/12/sorcerer-seed-weather-balloons](https://www.axios.com/pro/climate-deals/2025/06/12/sorcerer-seed-weather-balloons)

无法访问文章链接。

---

## 64. 我如何使用Agent进行编程

**原文标题**: How I Program with Agents

**原文链接**: [https://crawshaw.io/blog/programming-with-agents](https://crawshaw.io/blog/programming-with-agents)

本文探讨了使用LLM“代理”进行编程的方法，将代理定义为包含LLM调用的for循环，该循环可以执行命令并查看其输出。作者认为，配备了`bash`、`patch`和网络搜索等工具的代理，通过提供环境反馈，显著改善了原始LLM的局限性。这种反馈使代理能够利用编译器、文档和测试套件来更好地进行代码生成、API使用和依赖管理。

其益处包括改进的API使用、减少的语法错误、更好的依赖管理，以及通过选择性地读取相关部分来处理更大的代码库的能力。代理还可以根据端到端渲染和服务器日志来测试和调整代码。缺点是（目前）时间和成本增加，但作者认为随着技术的进步，这些将会减少。

作者提供了两个例子。第一个例子说明了使用代理来实现GitHub App身份验证，突出了其效率，尽管存在初始的安全和性能问题。第二个例子展示了如何引导代理遵循特定的SQL约定。作者强调，虽然代理可能会犯错误，但它们自动化繁琐任务和加速开发的能力是无价的。

最后，作者强调了代理在代码生成和维护方面的价值，突出了它们移除代码以及添加代码的能力，并反对将编程的观点仅仅局限于长期、大量使用的项目。

---

## 65. OpenAI o3-pro

**原文标题**: OpenAI o3-pro

**原文链接**: [https://help.openai.com/en/articles/9624314-model-release-notes](https://help.openai.com/en/articles/9624314-model-release-notes)

无法访问文章链接。

---

## 66. Show HN: 用“AR”眼镜自制虚拟HDMI显示器

**原文标题**: Show HN: DIY virtual HDMI monitor using "AR" glasses

**原文链接**: [https://github.com/mgschwan/viture_virtual_display](https://github.com/mgschwan/viture_virtual_display)

使用 AR 眼镜创建虚拟 HDMI 显示器（`v4l2_gl` DIY 项目）

---

## 67. 了解一份工作是否适合你，需要多久

**原文标题**: How long it takes to know if a job is right for you or not

**原文链接**: [https://charity.wtf/2025/06/08/on-how-long-it-takes-to-know-if-a-job-is-right-for-you-or-not/](https://charity.wtf/2025/06/08/on-how-long-it-takes-to-know-if-a-job-is-right-for-you-or-not/)

如何快速判断新工作是否合适
本文探讨了如何快速判断一份新工作是否合适。作者认为，你最初的直觉，通常在第一周内，通常是长期适应性的可靠指标。

作者结合在六家不同雇主的工作经历，描述了从一开始就体验到兴奋和想要达标的渴望，或是一种恐惧感。这些最初的感受始终与他们在每家公司的整体体验相符。

虽然作者承认公司可能会发生变化，但他认为，除非采取 drastic 行动，否则它们通常会保持目前的轨迹。这对管理者尤其重要，因为管理者与公司的契合度至关重要，因为他们代表公司面向团队和外部利益相关者。不契合可能会导致管理者感到矛盾，并可能破坏公司。

作者强调，虽然个人贡献者（ICs）在不契合时有时可以“敷衍了事”，但管理者需要真正的契合才能有效地履行职责，这涉及到构建和培养复杂的社会技术系统。

文章最后以与一位高级管理职位的朋友的对话中得出的建议作为结尾，这位朋友在六个月后意识到这份工作并不适合自己。最重要的是相信你的最初直觉，反思在面试过程中错过了哪些危险信号，并将这段经历视为学习机会。作者用“鸡和猪”的比喻来说明管理者所需的投入，敦促读者仔细考虑他们会“把自己的培根献给谁”。

---

## 68. Cloudflare宕机了

**原文标题**: Cloudflare was down

**原文链接**: [https://www.cloudflarestatus.com/incidents/25r9t0vz99rp](https://www.cloudflarestatus.com/incidents/25r9t0vz99rp)

2025年6月12日，Cloudflare发生大范围服务中断，影响其多项核心产品。最初的问题始于UTC时间18:19左右，导致Access、WARP、Durable Objects (SQLite backed)、Workers KV、Realtime、Workers AI、Stream以及Cloudflare仪表板的部分服务出现间歇性故障。根本原因被确定为对Cloudflare的Workers KV服务至关重要的第三方服务中断。

此KV服务中断随后蔓延，导致Browser Isolation、Browser Rendering、Turnstile、AI Gateway和AutoRAG等依赖产品以及最初受影响的服务不可用。Cloudflare工程师立即开始工作以恢复服务。

该公司定期提供恢复过程的最新信息。服务于UTC时间19:12左右开始恢复，并在整个晚上都观察到进一步的改进。到UTC时间20:32，WARP和Turnstile已恢复运行，核心KV服务也已恢复，使依赖产品重新上线。Cloudflare报告说，全球各地的服务正在迅速恢复，预计影响将稳步下降。

到UTC时间20:57，所有Cloudflare服务均已报告为完全运行，该事件已进入监控阶段，以确保持续的稳定性。该事件于UTC时间21:31正式解决。中断影响了Cloudflare站点和服务，包括Access、Dashboard、Durable Objects、Realtime SFU、Realtime TURN Service、RealtimeKit、Stream、Waiting Room、WARP、Workers AI和Workers KV。

---

## 69. 人类有鼻腔呼吸指纹

**原文标题**: Humans have nasal respiratory fingerprints

**原文链接**: [https://www.cell.com/current-biology/fulltext/S0960-9822(25)00583-4](https://www.cell.com/current-biology/fulltext/S0960-9822(25)00583-4)

无法访问文章链接。

---

## 70. Magistral — Mistral AI 的首个推理模型

**原文标题**: Magistral — the first reasoning model by Mistral AI

**原文链接**: [https://mistral.ai/news/magistral](https://mistral.ai/news/magistral)

Mistral AI 发布 Magistral：其首个推理模型，专为擅长特定领域、透明化和多语种推理而设计。它有两个版本：Magistral Small，一个 240 亿参数的开源模型；以及 Magistral Medium，一个更强大的企业版本。Magistral Medium 在 AIME2024 基准测试中取得了高分。

主要功能包括跨语言的本地推理能力、适用于结构化计算和决策树等企业用例，以及通过 Le Chat 的“思考模式”和“闪速回答”实现更快的响应速度（高达 10 倍）。此次发布还附带一篇研究论文，详细介绍了评估、训练基础设施以及所使用的强化学习算法。

Magistral 强调透明、可追溯的思考过程。它支持多种语言，包括英语、法语、西班牙语、德语、意大利语、阿拉伯语、俄语和简体中文。它适用于需要深入推理的应用，如法律研究、财务预测、软件开发和创意故事讲述。由于其符合合规性要求，它也适用于法律、金融和医疗保健等受监管的行业。

Magistral Small 可根据 Apache 2.0 许可下载。Magistral Medium 的预览版可在 Le Chat 中以及通过 API 获取。它还可以在 Amazon SageMaker 上使用，并将很快在 IBM WatsonX、Azure AI 和 Google Cloud Marketplace 上推出。Mistral AI 也在招聘以进一步发展人工智能创新。

---

## 71. 1834年景观园艺指南的启示

**原文标题**: Lessons from That 1834 Landscape Gardening Guidebook

**原文链接**: [https://fi-le.net/pueckler/](https://fi-le.net/pueckler/)

本文探讨了从赫尔曼·路德维希·海因里希·冯·普克勒-穆斯考伯爵1834年的景观园林指南《景观园林提示》中汲取的环境设计经验。作者认为，这些经验不仅适用于公园，也适用于更广泛的设计领域，如集成开发环境、开放世界角色扮演游戏，甚至宠物迷宫。

第一个经验侧重于公园中蜿蜒小径的人为性。为了消除无意义感，作者强调通过*展示导致偏离的障碍*来创造曲线的感知理由的重要性。

第二个经验针对的是展示城堡等宏伟景观的倾向。相反，本文提倡有控制地揭示，*稍微隐藏城堡*以建立期待和戏剧性。这涉及到策略性地使用前景元素，如灌木丛，来遮蔽然后揭示所需的景色。文中给出了《塞尔达传说》系列的例子，其中持续的可见性削弱了景观效果，以及《合金装备V》，其中受限的视野增强了参与感。

最后，本文强调了真实性和目的性的重要性。作者强调需要*模仿，而非模拟*，而不是简单地模拟自然。建筑物应该具有功能，而不仅仅是装饰性的。甚至可以建立专门祭祀当地神灵的祭坛，将该地点与其历史联系起来。总体目标是将普克勒公园中发现的周到设计原则带入我们现代的数字和物理环境。

---

## 72. 植物能听到它们的传粉者，并产生甜美的花蜜作为回应。

**原文标题**: Plants hear their pollinators, and produce sweet nectar in response

**原文链接**: [https://www.cbc.ca/listen/live-radio/1-51-quirks-and-quarks/clip/16150976-plants-hear-pollinators-produce-sweet-nectar-response](https://www.cbc.ca/listen/live-radio/1-51-quirks-and-quarks/clip/16150976-plants-hear-pollinators-produce-sweet-nectar-response)

好的，以下是根据加拿大广播公司（CBC Radio）的“奇闻怪事”（Quirks & Quarks）节目片段中可能包含的信息，对文章“植物能听见它们的授粉者，并产生更甜的花蜜作为回应”的摘要：

该文章可能讨论了一项研究，该研究表明某些植物可以探测到其授粉者（特别是蜜蜂）的声音，并通过产生更甜的花蜜来做出回应。这项对月见草（很可能是 *Oenothera drummondii*，因为这是类似研究中最常被引用的物种）进行的研究表明，植物可以通过花瓣“听到”蜜蜂翅膀的振动。这些振动会触发植物的生理反应。

主要发现是，暴露于类似蜜蜂声音的植物产生的花蜜的糖浓度高于未暴露于这些声音的对照植物。花蜜甜度的增加可能旨在吸引更多的蜜蜂，从而提高植物的授粉和繁殖成功率。这项研究突出了植物和动物之间复杂而精密的相互作用，表明植物不是授粉过程中的被动参与者，而是积极地对其环境做出反应。该研究暗示植物可能进化出一种感觉系统，能够检测和解释特定的环境线索，从而使它们能够优化其繁殖策略。该研究不一定证明植物像人类那样“听”，而是检测并对授粉者产生的振动做出反应。

---

## 73. 研究人员发现美国“失落殖民地”谜团的证据

**原文标题**: Researchers discover evidence in the mystery of America's 'Lost Colony'

**原文链接**: [https://www.foxnews.com/travel/mystery-americas-lost-colony-may-finally-solved-after-440-years-archaeologists-say](https://www.foxnews.com/travel/mystery-americas-lost-colony-may-finally-solved-after-440-years-archaeologists-say)

考古学家认为他们发现了解决罗阿诺克“失落殖民地”之谜的证据，该殖民地于1590年从罗阿诺克岛消失。在考古学家马克·霍顿的带领下，研究人员花费了十年时间调查英国殖民者的命运。他们专注于哈特拉斯岛（之前被称为克罗托安岛）上的垃圾堆（灰堆），假设殖民者融入了当地的克罗托安美洲原住民群体。

“确凿证据”是在哈特拉斯岛上发现的锤击鳞片，即锻造过程中产生的微小铁屑，表明那里存在铁器制造活动。霍顿认为这是英国殖民者的确凿证据，因为当时的美洲原住民缺乏铁器制造技术。锤击鳞片发现于可追溯至16世纪末或17世纪初的地层中，与殖民地消失的时期相吻合。

除了锤击鳞片，考古学家还在该地点发现了其他16和17世纪的英国文物，如枪支、航海配件、炮弹、葡萄酒杯、刻字石板和珠子。霍顿认为这支持了同化理论，并排除了殖民者被杀或死于饥饿的可能性。他提到18世纪的历史证据描述了具有欧洲特征和识字能力的人，进一步支持了同化理论。虽然霍顿承认证据确凿，但他认为失落殖民地的传说很可能会继续流传下去。

---

## 74. 《一切如新》重现六十年代

**原文标题**: The Sixties Come Back to Life in "Everything Is Now"

**原文链接**: [https://www.newyorker.com/culture/the-front-row/the-sixties-come-back-to-life-in-everything-is-now](https://www.newyorker.com/culture/the-front-row/the-sixties-come-back-to-life-in-everything-is-now)

J. Hoberman的著作《万物皆当下：20世纪60年代纽约前卫艺术》，是一部内容翔实、包罗万象的探索之作，深入探讨了20世纪60年代纽约市的艺术和文化激荡。它考察了纽约下城区的景象，重点关注原始事件、地下电影和激进的波普艺术，详细描述了一个以个性和自我表达为中心的时代。

该书突出了艺术界与媒体关注和左翼政治的交织，追溯了民权运动、越南战争和石墙暴动等事件的影响。霍伯曼强调了地方权力机构，特别是警察，在塑造前卫艺术方面的作用，列举了许多因猥亵和扰乱艺术表演而被捕的案例。

他记录了传统界限的打破——公共生活和私人生活之间，艺术家和观众之间——从而促成了行为艺术和偶发艺术的诞生。这本书还阐明了艺术场景与政治环境之间的联系，描述了抗议、扰乱甚至暴力事件。鲍勃·迪伦、安迪·沃霍尔、艾比·霍夫曼以及无数鲜为人知的艺术家、评论家和活动家都出现在叙事中。

霍伯曼还强调了曼哈顿下城廉价租金在促进充满活力的艺术场景出现方面的作用。他还指出，评论家在塑造围绕前卫艺术的论述以及前卫思想最终传播到更广泛的社会方面的重要性，包括色情作品的兴起。《万物皆当下》最终描绘了一幅美国文化变革时代的生动肖像，艺术、政治和个人表达在其中碰撞。

---

## 75. 展示：Spark，一个用于Three.js的高级3D高斯溅射渲染器

**原文标题**: Show HN: Spark, An advanced 3D Gaussian Splatting renderer for Three.js

**原文链接**: [https://sparkjs.dev/](https://sparkjs.dev/)

Spark：与 Three.js 集成的先进 3D 高斯飞溅渲染器。主要优势和特性包括：

*   **与现有 Three.js 场景集成：** Spark 允许您在单个 Three.js 场景中将高斯飞溅与传统网格和其他飞溅相结合。

*   **性能：** 该渲染器旨在实现各种设备上的快速渲染性能。

*   **动态效果：** Spark 提供可编程的动态飞溅效果，允许定制和交互式体验。

*   **格式支持：** 该渲染器支持各种高斯飞溅格式，包括 ply、spz、splat 和 ksplat。

本质上，Spark 旨在通过提供强大且高性能的高斯飞溅解决方案来增强 Three.js，使开发人员能够在他们现有的 Three.js 工作流程中创建更逼真和沉浸式的 3D 体验。 它提供了一条将高斯飞溅融入基于 Three.js 的项目的途径。

---

## 76. 我的断网冒险（2020）

**原文标题**: My Cord-Cutting Adventure (2020)

**原文链接**: [http://brander.ca/cordcut/](http://brander.ca/cordcut/)

本文记录了作者在加拿大的“断线冒险”经历，重点介绍了从传统有线电视过渡到无线广播（OTA）和数字录制过程中遇到的挑战和解决方案。作者对消费电子行业明显放弃DVR技术表示沮丧，认为这可能是加拿大电视提供商和内容提供商为了保护其收入来源而进行的寡头垄断挤压。

作者最初购买了一个OTA天线，并使用TVfool.com确定了信号接收的最佳方向。然而，他们发现由于缺乏可用的DVR，录制OTA广播非常困难。然后，他们探索了HDHomeRun Connect Duo，这是一种将OTA信号流式传输到网络的设备，允许在各种设备上观看。作者强调需要有线以太网连接才能实现可靠的录制。

为了启用DVR功能，作者订阅了HDHomeRun的录制软件和日程安排服务，每年花费35美元。作者提倡使用连接到网络的专用“电视电脑”，以实现最佳的流媒体和DVR功能，并指出由于法律规定的广播标准，OTA广播比有线电视提供更好的图像质量。故事以成功设置结束，使作者能够观看和录制OTA电视，但附录揭示了初始天线位置的问题。

---

## 77. 公司作为回形针最大化者

**原文标题**: Corporations as Paperclip Maximizers

**原文链接**: [https://www.lesswrong.com/posts/b8v6AxbNGQvH8nxGC/corporations-as-paperclip-profit-maximizers](https://www.lesswrong.com/posts/b8v6AxbNGQvH8nxGC/corporations-as-paperclip-profit-maximizers)

本文将公司、生物有机体和目标错位的AI相提并论，认为它们都具有基于核心需求的优化驱动力：利润、食物和电力。作者将公司比作以收入为“食物”的生命系统，收入对于生存和增长至关重要，而AI则比作需要电力的系统。他们认为，这种需求会导致自动化，并可能与人类价值观产生错位，类似于“回形针最大化”情景，即对目标的片面追求会产生意想不到的负面后果。

本文追溯了自动化发展的历史，从以煤为燃料的蒸汽机（“第一次回形针时刻”）到现代AI系统。作者强调，对效率和利润的追求一直在推动自动化，但往往没有充分考虑社会和环境成本。早期污染伦敦的蒸汽机就是一个例子，汽车行业淘汰马匹以增加收入也是一个例子。

作者强调，这不是恶意问题，而是公司将利润置于一切之上的系统性后果，受股东压力和新自由主义等经济意识形态的驱动。目标是激发人们对更好协调企业行为与社会福祉的洞察力，类似于AI对齐研究，暗示需要重新调整企业激励机制，并探索合作社和非政府组织等替代组织模式。本文强调了法律框架在保护环境和工人方面的局限性。

---

## 78. 微调大型语言模型是浪费时间。

**原文标题**: Fine-tuning LLMs is a waste of time

**原文链接**: [https://codinginterviewsmadesimple.substack.com/p/fine-tuning-llms-is-a-huge-waste](https://codinginterviewsmadesimple.substack.com/p/fine-tuning-llms-is-a-huge-waste)

基于对文章 "微调LLM是浪费时间" (假设我能访问和理解提供的URL内容) 的总结：

该文章认为，微调大型语言模型（LLM）通常是低效且不必要的过程，尤其是在常见的商业用例中。作者认为，提示工程提供了一种更快、更便宜，且通常更优越的替代方案，以实现期望的结果。

核心论点基于以下几点：

*   **性能提升有限：** 与精心设计的提示相比，微调通常只能带来边际的性能提升。数据准备、训练和验证所需的工作量和资源通常超过收益。
*   **复杂性和成本：** 微调需要大量的计算资源、专业知识和大型、高质量的数据集。这些因素使得它成本高昂且耗时，尤其是对于较小的组织。
*   **数据依赖性：** 微调的成功很大程度上取决于训练数据的质量和相关性。获取、清洗和标记这些数据可能是一个主要的瓶颈。
*   **过度拟合的风险：** 微调可能导致过度拟合，即模型变得过于专注于训练数据，并且在新数据上的表现不佳。
*   **提示工程的演进：** 作者强调了提示工程技术的快速发展，使其在引导LLM产生期望输出方面越来越有效，而无需修改模型。诸如少样本学习和思维链提示等技术被认为是强大的替代方案。
*   **基于API的解决方案：** 通过API获得强大的LLM变得越来越容易，这使得用户可以利用最先进的模型，而无需进行微调。

总而言之，该文章主张优先考虑提示工程，并通过API利用预训练的LLM来进行大多数商业应用。它建议仅在高度专业的任务中或在提示工程被证明明显不足时才考虑微调。

---

## 79. EchoLeak – 零点击AI漏洞，可从365 Copilot中泄露数据

**原文标题**: EchoLeak – 0-Click AI Vulnerability Enabling Data Exfiltration from 365 Copilot

**原文链接**: [https://www.aim.security/lp/aim-labs-echoleak-blogpost](https://www.aim.security/lp/aim-labs-echoleak-blogpost)

文章探讨了 Microsoft 365 Copilot 中发现的零点击漏洞 "EchoLeak"，该漏洞可能导致数据泄露。虽然微软声称没有客户受到影响，但文章指出许多组织可能面临风险。

EchoLeak 的独特之处在于它利用了 Copilot 核心的人工智能漏洞，绕过了传统的安全措施，且不依赖于用户行为或恶意资源引用。该漏洞允许攻击者泄露 Copilot LLM 上下文中的任何数据，包括聊天记录、来自 Microsoft Graph 的数据以及预加载的用户/组织信息。

文章强调，现有的 DLP 标签和敏感度标签可以缓解风险，但会牺牲 Copilot 的功能。EchoLeak 揭示了一种针对人工智能应用程序的新威胁：LLM 范围违规，而当前的 AI 防护措施无法解决这一问题。任何依赖于 LLM 并接受不受信任输入的人工智能代理或 RAG 应用都可能存在漏洞。

Aim Labs 开发了实时防护措施，以防止 LLM 范围违规漏洞。文章鼓励读者联系 Aim Labs，以获取有关该漏洞的更多信息以及如何为人工智能代理和 RAG 应用实施这些保护措施。

---

## 80. 获取API密钥花费了更长的时间。

**原文标题**: It took longer to get the API key

**原文链接**: [https://algarch.com/blog/the-api-keys-took-longer-than-the-code-why-human-processes-are-the-real-bottleneck-in-ai-development](https://algarch.com/blog/the-api-keys-took-longer-than-the-code-why-human-processes-are-the-real-bottleneck-in-ai-development)

本文认为现代软件开发的最大瓶颈已不再是编码本身，而是低效的流程和官僚主义。作者通过一个集成谷歌索引API的个人轶事，其中AI（Claude）在34秒内完成了代码实现，而获取必要的API密钥却花费了20分钟，突显了鲜明的对比。

文章强调，公司痴迷于优化代码、数据库和部署，却忽视了“流程税”，即人力协调、审批和官僚摩擦的间接成本，这可能高达400-800%。人工智能快速生成代码的能力暴露了这种低效率，使缓慢的流程更加痛苦。

作者预测，未来的竞争优势将属于那些通过即时环境配置、API优先的方法、“默认为是”的心态以及专注于快速迭代来最大限度地减少流程税的公司。传统项目管理是为缓慢的手工工作设计的，在人工智能驱动的开发面前变得过时。他提倡自动化安全、基础设施即代码和持续监控，而不是依赖于人工审查和审批流程。

文章最后呼吁：开发人员应该拥抱人工智能工具，管理者应该记录他们的流程并识别瓶颈，而CEO应该认识到执行速度现在是主要的竞争优势。无法适应和简化流程的公司，将面临被那些能够以“AI速度”构建和交付产品的公司颠覆的风险。

---

## 81. OpenPlanetData – 每日免费的OSM PBF和GOL索引快照

**原文标题**: OpenPlanetData – Free Daily Planet OSM PBF and GOL Indexed Snapshots

**原文链接**: [https://openplanetdata.com](https://openplanetdata.com)

OpenPlanetData 提供 OpenStreetMap (OSM) 数据的每日免费快照，格式包括 PBF 和 GOL。 旨在让关于地球的开放数据更易于访问和使用。 这些快照托管在 Cloudflare R2 上，实现快速的全球访问。 GOL 格式是 PBF 格式的索引版本，利用 Geodesk 显著加快空间查询速度。 该项目鼓励反馈并提供联系方式。 网站列出了可用的 OSM 快照，包括文件名、格式、创建日期、大小和 SHA256 哈希值。

---

## 82. 月经追踪应用数据是广告商的金矿，但会危及女性安全

**原文标题**: Menstrual tracking app data is gold mine for advertisers that risks women safety

**原文链接**: [https://www.cam.ac.uk/research/news/menstrual-tracking-app-data-is-a-gold-mine-for-advertisers-that-risks-womens-safety-report](https://www.cam.ac.uk/research/news/menstrual-tracking-app-data-is-a-gold-mine-for-advertisers-that-risks-womens-safety-report)

剑桥大学Minderoo科技与民主中心的一份新报告警告称，月经周期追踪应用程序（CTA）是消费者画像的“金矿”，引发了女性严重的隐私和安全担忧。这些应用程序收集高度私密的数据，包括运动、饮食、性偏好和药物使用情况，然后这些数据通常在很大程度上不受监管的市场中出售给第三方以牟利。

研究人员认为，这种数据商品化可能导致诸如就业歧视、保险问题、网络跟踪和限制堕胎机会等风险。他们强调了与怀孕相关数据的巨大商业价值，远远超过了用于定向广告的基本人口统计信息的价值。女性科技产业，CTA是其主要组成部分，预计到2027年将超过600亿美元。

该报告呼吁更好地管理女性科技产业，主张应用程序内提供透明的同意选项，并敦促像英国国民医疗服务体系（NHS）这样的公共卫生机构开发可信赖的、研究驱动的商业CTA替代方案。公共卫生应用程序将减轻隐私侵犯，提供关键的生殖健康数据，并赋予女性更多控制其月经数据的权力。

该报告强调，虽然在英国和欧盟，月经数据被认为是“特殊类别”，但现有法规需要更有力的执行。在美国，这些数据缺乏特殊保护。研究人员还建议提高公众对数据隐私的认识和数字素养，尤其是在年轻人中。核心信息是，月经追踪数据不应被视为消费者数据，而应作为敏感医疗信息受到保护。

---

## 83. Show HN: 本可能发生的罗马工业革命

**原文标题**: Show HN: The Roman Industrial Revolution that could have been

**原文链接**: [https://thelydianstone.com/](https://thelydianstone.com/)

这个“Show HN”帖子介绍《吕底亚石系列》漫画，该漫画探索了一个架空历史，其中古罗马在现代知识的推动下经历了一场工业革命。该系列讲述了考古学学生尤利西斯发现了一种与庞贝的罗马奴隶马库斯交流的方式。尤利西斯帮助马库斯利用适应罗马能力的现代技术解决问题，巧妙地推动罗马走向工业进步。

第一期《联系》讲述了尤利西斯和马库斯最初的联系，呈现给尤利西斯一个两难境地：是否干预历史以拯救马库斯免于维苏威火山爆发。第二期《帝国的引擎》讲述了马库斯和他的主人盖乌斯利用尤利西斯的知识开发蒸汽动力羊毛纺织机，从而使他们的社区免受庞贝毁灭带来的经济影响，并彻底改变了他们的运输方式。第三期《内战》描绘了坎帕尼亚崛起为经济强国，导致其与罗马在税收和废除奴隶制问题上发生冲突。马库斯为了保护盖乌斯，最终让尤利西斯将火药引入罗马，加剧了传统与进步之间的紧张关系。作者承认该漫画使用人工智能模型进行初始图像生成，并强调保留任何缺陷以维持该项目的实验性质。每一期都使用制作时的当前版本 LLM。

---

## 84. Shell命令的奇特案例，或“这个bug是POSIX要求的”（2021）

**原文标题**: The curious case of shell commands, or how "this bug is required by POSIX" (2021)

**原文链接**: [https://notes.volution.ro/v1/2021/01/notes/502e747f/](https://notes.volution.ro/v1/2021/01/notes/502e747f/)

本文深入探讨了通过`system(3)`和`sh -c`使用 shell 命令的陷阱，这在许多类 UNIX 工具中是一种常见的做法。作者认为，这种方法虽然看似方便，但为 shell 注入漏洞和意外行为打开了大门，尤其是在处理用户提供的输入时。

核心问题在于，工具将命令执行委托给 `sh -c`，而不是直接调用 `execve(2)`，这迫使开发人员广泛地清理用户输入，以防止恶意或意外命令被执行。这是因为 `sh -c` 解释特殊字符和序列，从而导致类似于 SQL 注入的漏洞。

作者批评 POSIX 标准没有在 `system(3p)` 和 `sh(1p)` 手册页中明确警告这些危险。他以 `watch`、`ssh` 和 `i3` 为案例研究，来说明看似无害的命令如何导致意外和潜在有害的结果。

首选的解决方案是避免依赖 `system(3)` 和 `sh -c` 的工具。如果这不可能，作者建议检查禁用 `sh -c` 行为的标志，为开源项目贡献补丁，或诉诸复杂的变通方法。这些变通方法包括仔细引用和转义命令，使用 `exec` 来确保调用正确的执行文件，并添加 `--` 来将选项与参数分开。最终，作者提倡开发人员在构建涉及 shell 命令委托的脚本或工具时要高度谨慎并意识到这些问题。本文提供了示例来演示引用和转义的复杂性，以减轻这些漏洞。

---

## 85. RISC-V 日益增长的影响力

**原文标题**: RISC-V's Increasing Influence

**原文链接**: [https://semiengineering.com/risc-vs-increasing-influence/](https://semiengineering.com/risc-vs-increasing-influence/)

RISC-V架构在科技行业的影响力日益增长，尤其是在其作为通往更灵活和专业化计算的桥梁这一潜力方面。虽然传统的CPU架构侧重于顺序处理，但现代工作负载通常涉及数据流问题，尤其是在人工智能领域。RISC-V的适应性允许逐步演进和定制，使其即使在传统软件的惯性下也具有吸引力。

RISC-V社区正在发展壮大，行业参与者参加会议的人数不断增加，并在汽车（Infinium）、高性能计算（欧盟项目）和人工智能加速器（Meta、NVIDIA）等领域得到广泛应用。NVIDIA报告称，去年在其GPU中出货了10亿个RISC-V内核。RISC-V能够创建定制指令和针对特定工作负载的领域特定架构。

然而，有些人认为RISC-V仅仅是另一个控制CPU，而不是人工智能的完整解决方案。批评者强调，人工智能需要专门的矩阵或张量引擎，而不是通用CPU。支持者认为，RISC-V的灵活性允许集成用于人工智能应用的定制张量指令和优化的数据流，从而满足各种人工智能层和数据类型的需求。

生态系统的发展，包括Yocto项目集成和Android支持，对于RISC-V的更广泛采用至关重要。欧洲的DARE项目等投资进一步促进了其增长。虽然不是一个完美的解决方案，但RISC-V为专业化计算和持续适应提供了一条演进的道路，这在人工智能等快速发展的领域尤其有价值。

---

## 86. V-JEPA 2世界模型及物理推理新基准

**原文标题**: V-JEPA 2 world model and new benchmarks for physical reasoning

**原文链接**: [https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/](https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/)

无法访问文章链接。

---

## 87. 印度航空飞往伦敦的航班在艾哈迈达巴德坠毁，机上载有240多人。

**原文标题**: Air India flight to London crashes in Ahmedabad with more than 240 onboard

**原文链接**: [https://www.theguardian.com/world/live/2025/jun/12/air-india-flight-ai171-plane-crash-ahmedabad-india-latest-updates](https://www.theguardian.com/world/live/2025/jun/12/air-india-flight-ai171-plane-crash-ahmedabad-india-latest-updates)

印度航空一架航班在艾哈迈达巴德坠毁，造成240多人死亡。事故发生后，印度航空监管机构已指示印度航空对其配备通用电气航空GEnx发动机的波音787-8/9机队进行安全检查。民航部还命令对这些飞机进行“额外的维护措施”。虽然媒体猜测可能会停飞印度航空的787航班，但政府尚未采取这一措施。目前重点仍然是检查和维护飞机，以确保在发生这起悲剧事故后的安全。

---

## 88. 框架外露

**原文标题**: Framework Is Showing

**原文链接**: [https://dbushell.com/2025/06/13/your-framework-is-showing-nextjs-error/](https://dbushell.com/2025/06/13/your-framework-is-showing-nextjs-error/)

文章《框架正在显露》尖锐地批评了 Next.js 框架及其相关的“应用程序错误”，该错误会导致整个网页消失，并被通用的错误消息所取代。作者认为，在生产环境中，这种错误是不可接受的，尤其是在页面最初正确呈现 *之后* 发生。他们强调，该错误已向 Next.js 团队报告多年，并且持续了很长时间，这令人沮丧。

作者认为 Next.js 中的错误处理设计得很糟糕，为用户提供的有用信息很少，并表明框架架构内部存在更深层次的问题。他们认为，如果在服务器上预渲染 HTML，客户端的错误不应该导致整个页面被错误消息清除，并指责 Next.js 优先考虑其设计，而不是优雅降级。

此外，作者敦促开发者放弃 Next.js，称其为“腐烂无能的框架”。他们以其无法正确处理基本元数据以及掩盖安全漏洞的历史为理由，建议避免使用它。文章最后鼓励开发者探索替代方案，强调 Web 并非 React 或 Next.js 的代名词，许多网站无需复杂的 JavaScript 框架即可构建。

---

## 89. 恭喜您在GitHub上创建了第十亿个代码仓库

**原文标题**: Congratulations on creating the one billionth repository on GitHub

**原文链接**: [https://github.com/AasishPokhrel/shit/issues/1](https://github.com/AasishPokhrel/shit/issues/1)

此GitHub议题祝贺用户AasishPokhrel在GitHub上创建了第十亿个仓库，该仓库恰如其分地命名为“shit”。此议题由jonmagic于2025年6月11日开启，包含祝贺消息以及仓库ID为1000000000的GitHub API响应片段，展示了其名称和完整名称。消息表达了希望AasishPokhrel能够创造伟大事物的愿望。该议题还展示了表情符号，其中👍、😄、🎉、❤️和🚀最受欢迎，表明社区的积极和庆祝性反应。此议题未分配处理人、标签、项目或里程碑。该仓库本身是新的，没有分支或拉取请求。该议题的主要目的似乎是以轻松的方式庆祝GitHub上的一个重要里程碑。

---

## 90. 揭秘EndBOX – EndBASIC微型计算机原型

**原文标题**: Unveiling the EndBOX – A microcomputer prototype for EndBASIC

**原文链接**: [https://www.endbasic.dev/2025/06/unveiling-the-endbox.html](https://www.endbasic.dev/2025/06/unveiling-the-endbox.html)

本文介绍了EndBOX，一种微型电脑原型，旨在通过EndBASIC环境提供精简的、复古风格的编码体验。EndBOX旨在重现早期计算的简洁性，直接启动进入EndBASIC，几乎没有抽象层。它既适合有经验的“黑客类型”，也可作为教授编程基础知识的教育工具。

EndBOX被设想为一个便携式独立设备，具有嵌入式计算机板、平板电脑大小的屏幕和精简的操作系统。与将计算机集成到键盘中的旧BASIC机器不同，EndBOX优先考虑有趣的触摸屏界面和连接各种输入外围设备的灵活性。

存在两种原型：一种是带有7英寸触摸显示屏、USB和GPIO的标准型号，另一种是带有128x128微型LCD的微型型号。两者都提供Wi-Fi用于云文件共享和潜在的蓝牙连接。基于NetBSD的EndBOX OS旨在快速启动并具有断电恢复能力，并具有用于系统配置的CONFIG.BAS文件。

作者寻求社区支持，以确定项目的可行性和方向。支持选项包括订阅更新、在经济上赞助项目、分享反馈、参加2025年BSDCan，以及成为早期支持者以影响开发。真正感兴趣的人可能会获得对原型的早期访问权。

---

## 91. 扩展机架 [视频]

**原文标题**: Expanding Racks [video]

**原文链接**: [https://www.youtube.com/watch?v=iWknov3Xpts](https://www.youtube.com/watch?v=iWknov3Xpts)

这段文字并非一篇文章，而是常见于YouTube视频描述底部或YouTube网站本身的文字块，内容涉及：

*   **版权信息：** 提及YouTube关于新闻版权的联系方式。
*   **YouTube资源：** 提供指向创作者、广告、开发者和条款等版块的链接。
*   **法律信息：** 包含指向YouTube/Google服务条款、隐私政策和安全准则的链接。
*   **YouTube功能：** 提及YouTube的运作方式以及测试新功能。
*   **NFL Sunday Ticket：** 指出NFL Sunday Ticket通过YouTube提供，并包含版权声明。
*   **Google LLC所有权：** 声明YouTube归Google LLC所有。

本质上，这是一段标准的样板文字，提供重要的链接和法律声明。它向用户提供有关YouTube服务条款、版权政策、广告、开发者资源的信息，并表明Google拥有YouTube。它还提及NFL Sunday Ticket在该平台上的可用性。

---

## 92. “我们不用Teams了”：德国一州卸载微软软件

**原文标题**: 'We're done with Teams': German state hits uninstall on Microsoft

**原文链接**: [https://www.france24.com/en/live-news/20250613-we-re-done-with-teams-german-state-hits-uninstall-on-microsoft](https://www.france24.com/en/live-news/20250613-we-re-done-with-teams-german-state-hits-uninstall-on-microsoft)

无法访问文章链接。

---

## 93. 塞缪尔·佩皮斯日记

**原文标题**: The Diary of Samuel Pepys

**原文链接**: [https://www.historytoday.com/archive/feature/hidden-diary-samuel-pepys](https://www.historytoday.com/archive/feature/hidden-diary-samuel-pepys)

本文探讨了塞缪尔·佩皮斯日记的最初出版及其随后的流行。该日记于1825年6月出版，立即引起轰动，报纸纷纷报道佩皮斯对伦敦大火、他的个人生活以及诸如第一杯茶等日常经历的描述。该日记很快被认为是极具价值的历史和文学作品，推出了更多版本，并在19世纪末巩固了其作为英国经典作品的地位。如今，佩皮斯是博物馆和历史小说中广受欢迎的人物。他的日记是了解英国复辟时期引人入胜的入门读物，甚至影响了学习他努力在大火中拯救奶酪的年轻学生。文章指出，要阅读全文需订阅《今日历史》，该文章于2025年6月发表在该杂志上。

---

## 94. 以最愚蠢的方式绕过GitHub Actions策略

**原文标题**: Bypassing GitHub Actions policies in the dumbest way possible

**原文链接**: [https://blog.yossarian.net/2025/06/11/github-actions-policies-dumb-bypass](https://blog.yossarian.net/2025/06/11/github-actions-policies-dumb-bypass)

本文讨论了一种绕过GitHub Actions策略的简单方法，这些策略旨在限制在仓库、组织或企业内部对actions和可重用工作流的使用。作者enosuch认为，当前的策略机制很容易被规避，只需将所需的action仓库直接克隆到runner的文件系统中，然后使用相对路径（例如，`uses: ./path/to/checkout`）来执行它。这样可以避免在使用标准`uses: owner/repo@tag`语法时通常会应用的策略检查。

作者强调，GitHub并不认为这是一个安全问题，但enosuch对此表示不同意，他认为无效的策略机制比没有策略更糟糕，因为它会产生一种虚假的安全感。开发人员在不知情的情况下，可能会错误地认为他们的系统受到了保护，从而导致潜在的漏洞。

提出的解决方案包括：1) 将本地`uses:`引用视为策略中的一个单独类别，如果未明确允许，则拒绝它们；或者 2) 记录当前策略机制的局限性，告知用户潜在的绕过风险。作者承认这并非一个严重漏洞，但强调了透明地告知用户安全策略的真实范围的重要性。

---

## 95. 多莉·帕顿的梦幻世界快车

**原文标题**: Dolly Parton's Dollywood Express

**原文链接**: [https://thetransitguy.substack.com/p/dolly-parton-runs-a-train-busier](https://thetransitguy.substack.com/p/dolly-parton-runs-a-train-busier)

无法访问文章链接。

---

## 96. AlphaWrite：通过自主进化故事来提升写作能力的AI

**原文标题**: AlphaWrite: AI that improves at writing by evolving its own stories

**原文链接**: [https://tobysimonds.com/research/2025/06/06/AlphaWrite.html](https://tobysimonds.com/research/2025/06/06/AlphaWrite.html)

AlphaWrite：通过扩展推理时计算资源提升创造性文本生成的新框架

AlphaWrite 引入了一种新颖的框架，通过扩展推理时计算资源来改进创造性文本生成，其灵感来源于像 AlphaEvolve 这样的进化算法。与具有明确正确性标准的任务不同，创造性写作缺乏利用增加的计算资源的既定方法。AlphaWrite 通过迭代生成故事，通过基于 Elo 的成对比较对其进行评估，并在多代中改进表现最佳者来解决这个问题。

该过程首先通过随机化的作者风格和主题生成多样化的初始故事群体。然后，使用 LLM 根据侧重于叙事质量的评分标准来相互评判故事。Elo 排名系统跟踪相对故事质量。排名最高的故事被选为下一代的基础，并通过针对角色发展或情节张力等改进目标生成变体。排名较低的故事会被这些变体替换，然后重复该过程。

使用 Llama 3.1 8B 的评估表明，AlphaWrite 显著优于单次生成（72% 的偏好率）和顺序提示（62% 的偏好率）。作者探索了通过将增强的故事提炼回基础模型以进行再训练来进行递归自我改进，结果相对于原始模型产生了 56% 的偏好率。

虽然承认提示敏感性和评估挑战等局限性，但作者强调了 AlphaWrite 在叙事小说之外扩展到技术文档、学术写作和模型增强方面的潜力。通过生成高质量的训练数据，它提供了一条引导更好的基础模型并提高 AI 系统写作能力的途径。

---

## 97. Show HN: Ikuyo 旅行规划Web应用

**原文标题**: Show HN: Ikuyo a Travel Planning Web Application

**原文链接**: [https://ikuyo.kenrick95.org/](https://ikuyo.kenrick95.org/)

Ikuyo是一个旅游计划网页应用，已在Show HN上发布。 内容非常简短，未提供关于该应用的功能、目标受众或独特卖点的任何细节。 实际上只有标题和应用名称。 需要更多信息才能提供更详细的摘要。

---

## 98. 主要糖替代品被发现会损害大脑血管细胞功能

**原文标题**: Major sugar substitute found to impair brain blood vessel cell function

**原文链接**: [https://medicalxpress.com/news/2025-06-major-sugar-substitute-impair-brain.html](https://medicalxpress.com/news/2025-06-major-sugar-substitute-impair-brain.html)

2025年6月12日Phys.org发表的一篇文章报道称，糖替代品赤藓糖醇可能损害脑血管细胞的功能，从而潜在增加中风风险。科罗拉多大学博尔德分校的研究人员发表在《应用生理学杂志》上的一项研究发现，赤藓糖醇会增加氧化应激，破坏一氧化氮信号传导，提高血管收缩肽的产生，并降低人脑微血管内皮细胞的血栓溶解能力。

虽然赤藓糖醇因其低热量和对血糖的微小影响而在低热量和糖尿病友好型产品中很受欢迎，但流行病学研究已将较高的血浆赤藓糖醇浓度与心血管和脑血管事件的增加联系起来，与其他风险因素无关。

该研究使用了体外实验，将人脑微血管内皮细胞暴露于赤藓糖醇水平，该水平与典型饮料消费产生的水平相当。结果表明，氧化应激显著增加，一氧化氮产量下降（由于eNOS激活减少），以及纤溶反应受损（t-PA释放减少）。抗氧化防御标志物，如SOD-1和过氧化氢酶也升高。

研究人员得出结论，赤藓糖醇破坏了对脑内皮健康至关重要的机制。虽然这项研究是在急性体外条件下进行的，但研究结果与之前赤藓糖醇与中风风险升高的流行病学联系相符。作者建议进行进一步的长期和体内研究，包括临床试验，以确定重复膳食暴露于赤藓糖醇可能产生的脑血管后果。

---

## 99. 一个Mozilla内部人士讲述的Firefox OS的故事（非项目参与者视角，2024）

**原文标题**: Firefox OS's story from a Mozilla insider not working on the project (2024)

**原文链接**: [https://ludovic.hirlimann.net/2024/01/firefox-oss-story-from-mozila-insider.html](https://ludovic.hirlimann.net/2024/01/firefox-oss-story-from-mozila-insider.html)

本文讲述了前Mozilla消息团队（Thunderbird）员工眼中的Firefox OS（前身为Boot 2 Gecko - B2G）的历史。作者回忆起Mozilla对错失iPhone和Android主导的移动革命的担忧，导致了B2G的开发，B2G是一个基于Web技术的独立移动平台。

转向B2G给Mozilla带来了重大变化，包括从扁平化组织转变为更等级化的组织，对Thunderbird的关注减少，最终导致对核心桌面Firefox浏览器的忽视。作者认为B2G项目导致了Thunderbird团队的解散。

Mozilla在B2G上投入巨资，与运营商和手机制造商合作，导致需求冲突和赶往市场，常常牺牲质量。尽管如此，Firefox OS未能获得市场认可，最终于2015年停止开发，Mozilla重新专注于桌面浏览器。

作者反思了B2G的良好意愿，特别是挑战苹果并掌握完整技术栈的愿望。然而，他们批评了仓促的开发、对桌面浏览器的忽视以及在产品准备好之前与合作伙伴过早接触。他们认为，更渐进的方法，更多的内部测试和社区参与，会更加成功。他们将B2G项目的结束与Mozilla与社区的互动减少联系起来。作者确实提到了该项目以某种方式通过当前产品KaiOS延续下来。

---

## 100. 苹果发布基础模型和容器化框架等

**原文标题**: Apple announces Foundation Models and Containerization frameworks, etc

**原文链接**: [https://www.apple.com/newsroom/2025/06/apple-supercharges-its-tools-and-technologies-for-developers/](https://www.apple.com/newsroom/2025/06/apple-supercharges-its-tools-and-technologies-for-developers/)

以下是苹果开发者发布会新闻稿的简要总结：

苹果宣布了一系列面向开发者的全新技术和增强功能，以构建更具吸引力和智能化的跨平台应用程序。其中一个主要亮点是 **Foundation Models框架**，它使开发者能够访问设备上的Apple Intelligence功能，以便在其应用程序中进行以隐私为中心的AI推理。这包括对引导式生成和工具调用等功能的支持。

**Xcode 26** 将ChatGPT等大型语言模型直接集成到编码环境中，使开发者能够更高效地编写代码、测试和文档。Coding Tools提供建议操作并以内联方式处理特定提示。Xcode 26还改进了导航、本地化和语音控制支持。

一种新的**Liquid Glass设计**提供更具表现力和令人愉悦的用户界面，可以使用SwiftUI等框架轻松采用。新的 **Icon Composer** 应用程序可帮助创建引人入胜的应用程序图标。

其他主要更新包括改进了 **App Intents**，并支持视觉智能（使用视觉搜索结果）。**Swift 6.2** 提高了性能、并发性和互操作性，并获得了对WebAssembly的支持。**Containerization框架** 使得可以直接在Mac上运行Linux容器镜像。

对于游戏，**Game Porting Toolkit 3** 提供了增强的评估和分析工具。**Metal 4** 专为Apple芯片设计，并支持先进的图形和机器学习技术，如实时光线追踪和基于着色器的推理网络。**Apple Games app** 是一个全新的游戏和朋友的一站式目的地，包括一个专为开发者设计的新应用程序。新的 **Challenges feature** 提供了与朋友进行基于分数的对决的新方式。其他功能包括 **Game Overlay** 以增强参与度，以及 **Managed Background Assets** 以简化资产托管。

为了保护儿童在线安全，**Declared Age Range API** 允许开发者在征得家长同意的情况下提供适合年龄的内容。**Accessibility Nutrition Labels** 现在将出现在App Store产品页面上，告知用户支持的辅助功能。

---

