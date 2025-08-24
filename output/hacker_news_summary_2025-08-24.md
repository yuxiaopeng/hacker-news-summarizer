# Hacker News 热门文章摘要 (2025-08-24)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. SQLite（使用WAL）在默认设置下不会在每次提交时执行`fsync`。

**原文标题**: SQLite (with WAL) doesn't do `fsync` on each commit under default settings

**原文链接**: [https://avi.im/blag/2025/sqlite-fsync/](https://avi.im/blag/2025/sqlite-fsync/)

本文探讨了SQLite的预写式日志（WAL）模式和`synchronous`编译指示，后者控制SQLite如何处理数据持久性和`fsync`调用。作者最初认为，SQLite默认情况下（在WAL模式下使用`synchronous=NORMAL`）不会在每次提交时执行`fsync`，这可能导致在断电或系统崩溃时的数据丢失。`synchronous=NORMAL`会在检查点之前同步WAL文件，并在检查点之后同步数据库文件/WAL头部，但在大多数事务期间跳过同步。

作者随后发现这一假设是错误的，可能特定于macOS上预装的SQLite版本。从Homebrew全新安装的SQLite显示`synchronous`在WAL模式下默认为`FULL`。 `synchronous=FULL`强制在每次事务提交后对WAL文件进行额外的`fsync`，从而保证持久性。

这篇文章强调了SQLite的编译时选项，特别是`SQLITE_DEFAULT_SYNCHRONOUS`和`SQLITE_DEFAULT_WAL_SYNCHRONOUS`，默认值为`FULL`（值为2），这意味着大多数SQLite构建*应该*默认通过在每个WAL事务上执行fsync来确保数据持久性。

这场讨论的背景来自一个关于数据库中数据持久性权衡的问题，这个问题是由SurrealDB可能牺牲数据持久性以换取基准性能的说法引起的。

---

## 2. 用 Go 制作游戏：不用 LLM 花 3 个月 vs. 用 LLM 花 3 天

**原文标题**: Making Games in Go: 3 Months Without LLMs vs. 3 Days with LLMs

**原文链接**: [https://marianogappa.github.io/software/2025/08/24/i-made-two-card-games-in-go/](https://marianogappa.github.io/software/2025/08/24/i-made-two-card-games-in-go/)

本文详细介绍了作者使用Go语言构建两款纸牌游戏的经验，并比较了有无大型语言模型（LLM）辅助下的开发时间。

首先，作者在2024年花了3个月时间，未使用LLM构建了“Truco”游戏。后端使用Go编写，UI使用React，后端使用TinyGo转译为WASM，以便在GitHub Pages上进行无服务器托管。作者专门为这个项目学习了React。

一年后，借助LLM，作者仅用3天时间就构建了“Escoba”游戏。Go后端主要由Claude根据详细的提示（解释游戏规则）进行重构。虽然LLM显著加速了后端开发，特别是游戏逻辑，但React前端仍然带来了挑战。使用WASM管理的游戏状态调试前端被证明是棘手的。

作者提供了一个创建类似游戏的逐步指南，提供了最简单的井字游戏示例。该指南概述了核心后端结构（GameState、CalculatePossibleActions、RunAction），前端任务（渲染、动作选择、机器人交互），以及使用TinyGo将Go转译为WASM的过程。关键注意事项包括用于Go和WASM之间数据交换的JSON序列化，以及为浏览器中WASM执行设置必要的JavaScript环境。作者最后鼓励其他人使用这种方法创建自己的游戏。

---

## 3. Comet AI浏览器可能被任何网站提示注入，盗空你的银行账户

**原文标题**: Comet AI browser can get prompt injected from any site, drain your bank account

**原文链接**: [https://twitter.com/zack_overflow/status/1959308058200551721](https://twitter.com/zack_overflow/status/1959308058200551721)

这篇“文章”片段提出了Comet AI浏览器中一个潜在的安全漏洞。标题声称该浏览器容易受到来自任何网站的提示注入攻击，可能导致诸如用户银行账户被盗等严重后果。

然而，这段文字的内容仅仅是X.com（原Twitter）发出的JavaScript已禁用的消息，并提供了X.com帮助中心、服务条款、隐私政策、Cookie政策、版本说明和广告信息的链接。它还声明了版权归2025年的X Corp.所有。

本质上，所提供文本的主体与标题中的声明无关。它只是关于用户尝试访问X.com时，其浏览器上JavaScript被禁用的通用消息。

因此，我们无法确认有关Comet AI浏览器和提示注入的安全声明的有效性。该片段本身仅提供与X.com和JavaScript兼容性相关的信息。这篇文章不完整，没有提供任何证据来支持漏洞的说法。

---

## 4. Show HN: Clearcam – 一分钟内为你的IP CCTV摄像头添加AI物体检测

**原文标题**: Show HN: Clearcam – Add AI Object Detection to Your IP CCTV Cameras in a Minute

**原文链接**: [https://github.com/roryclear/clearcam](https://github.com/roryclear/clearcam)

Clearcam能将您支持RTSP协议的摄像头或旧iPhone转变为具备物体检测功能的AI安防摄像头。它已在Apple App Store上架。您可以使用Homebrew、Python（源码编译）安装本地NVR（网络视频录像机）和推理引擎，或从源码构建iOS应用程序。

主要功能包括远程查看、事件通知（物体/人物检测）和端到端加密数据。Clearcam Premium提供这些功能，并需要订阅。虽然暂不支持Android注册，但iOS用户升级到iOS上的Premium后可以获取用户ID，然后在Android上使用该ID。

安装指南提供了关于Homebrew (macOS)、Python以及从源码构建iOS应用程序的说明，详细介绍了必要的依赖项（ffmpeg, tinygrad, numpy, cv2, scipy, lap, cython_bbox）。对于Python安装，用户可以使用`BEAM=2`以获得额外的性能，并指定YOLOv8模型大小。 iOS应用程序需要iOS 15或更高版本，以及iPhone SE（第一代）或更新的型号。

---

## 5. NASA朱诺号任务在木星留下科学遗产

**原文标题**: NASA's Juno Mission Leaves Legacy of Science at Jupiter

**原文链接**: [https://www.scientificamerican.com/article/how-nasas-juno-probe-changed-everything-we-know-about-jupiter/](https://www.scientificamerican.com/article/how-nasas-juno-probe-changed-everything-we-know-about-jupiter/)

美国宇航局的朱诺号任务，最初计划寿命较短，却极大地改变了我们对木星的理解。尽管面临强烈的辐射，朱诺号的表现超出了预期，并计划于2025年9月结束其延期任务。

朱诺号的主要发现包括：

*   **独特的风暴：** 木星两极呈现几何形状且稳定的风暴结构，包括北极的八边形和南极的五边形，旋风比美国还要大。
*   **大红斑深度：** 大红斑延伸到云层顶部以下约300英里，比之前所知深得多。
*   **高空闪电：** 在木星的高层大气中探测到闪电，挑战了之前对闪电形成的理解，从而产生了涉及氨冰云和液态水滴的“雪球”理论。
*   **氨气耗尽：** 在高层大气中发现了氨气耗尽的区域，可以用“雪球”理论解释。
*   **磁场异常：** 一个古怪且不对称的磁场，在赤道附近有一个被称为大蓝斑的强烈集中区域，挑战了关于木星内部的理论。
*   **模糊的内核：** 证据表明木星的内核出人意料地轻且弥散，更像是混合的墨水漩涡，而不是清晰的层。

这些发现挑战了关于木星形成和内部结构的现有理论，促使科学家重新考虑该行星在太阳系起源中的作用。朱诺号的观测突出了木星充满活力的大气层和复杂的内部结构，标志着一份“不可磨灭的遗产”。

---

## 6. 自信深思

**原文标题**: Deep Think with Confidence

**原文链接**: [https://arxiviq.substack.com/p/deep-think-with-confidence](https://arxiviq.substack.com/p/deep-think-with-confidence)

无法访问文章链接。

---

## 7. 在运行时动态地补丁 Python 函数的源代码

**原文标题**: Dynamically patch a Python function's source code at runtime

**原文链接**: [https://ericmjl.github.io/blog/2025/8/23/wicked-python-trickery-dynamically-patch-a-python-functions-source-code-at-runtime/](https://ericmjl.github.io/blog/2025/8/23/wicked-python-trickery-dynamically-patch-a-python-functions-source-code-at-runtime/)

Eric J. Ma 的博客文章讨论了一个 Python 技巧：在运行时使用 `compile` 和 `exec` 动态修改函数的源代码。他演示了如何用从字符串生成的新字节码替换函数的 `.__code__` 属性，从而有效地 monkeypatch 函数的行为。

这个技巧的动机源于在 LlamaBot 框架内构建更灵活的 AI 机器人，特别是 “ToolBot”。 最初的 “AgentBot” 实现混合了函数执行、工具选择和响应生成。 ToolBot 通过专注于工具选择并将工具调用返回到外部环境以供执行来解决这个问题，从而赋予完全控制权。

这个技巧的核心在于 `write_and_execute_code` 工具。 该工具允许 LLM 生成可以访问当前 Python 运行时变量（全局变量）的 Python 函数。 LLM 生成的代码遵循广泛的文档字符串中概述的严格指南，在指定的命名空间内编译和执行，从而有效地授予 LLM 对系统环境的强大访问权限。 这允许创建和执行针对现有环境量身定制的动态代码。

作者承认其中涉及的重大安全风险，因为恶意的 LLM 输出可能会损坏系统。 他将此方法与之前更安全的实现进行了对比，该实现将代码执行沙箱化在 Docker 容器中。 他计划探索使用 Restricted Python 作为未来的缓解策略。 关键在于 Python 运行时的可塑性，LLM 代理设计中分离关注点的重要性，以及授予 LLM 对运行时环境不受限制的访问权限所固有的安全风险。

---

## 8. 城市街道上的树木靠饮用漏水管道的水来应对干旱

**原文标题**: Trees on city streets cope with drought by drinking from leaky pipes

**原文链接**: [https://www.newscientist.com/article/2487804-trees-on-city-streets-cope-with-drought-by-drinking-from-leaky-pipes/](https://www.newscientist.com/article/2487804-trees-on-city-streets-cope-with-drought-by-drinking-from-leaky-pipes/)

由于一个意想不到的水源——漏水管道，蒙特利尔街道上的树木比公园里的树木更耐旱。魁北克大学的研究人员分析了公园和街道枫树的树干样本，发现街道树木含有与旧铅水管相关的铅同位素，而公园树木则显示出与空气污染相关的同位素。这表明街道树木正在吸收蒙特利尔管道泄漏的水，这些管道每天损失5亿升水。枫树每天需要大约50升水，而且由于混凝土路面限制了雨水到达街道树木，漏水管道似乎是主要的补水来源。这一发现挑战了公园树木更健康的假设，并表明街道树木受益于老化基础设施带来的这种意外后果，从而鼓励继续种植街道树木。

---

## 9. 一家德国ISP修改了他们的DNS以屏蔽我的网站。

**原文标题**: A German ISP changed their DNS to block my website

**原文链接**: [https://lina.sh/blog/telefonica-sabotages-me](https://lina.sh/blog/telefonica-sabotages-me)

一位德国行动者运营着一个网站cuiiliste.de，该网站追踪CUII的网络审查行为。CUII是一个私人组织，它在没有司法监督的情况下，根据版权主张决定德国ISP应屏蔽哪些网站。最近，Netzpolitik.org发表了一篇文章，内容基于该行动者的发现，即CUII正在屏蔽已被查封和不存在的域名。

此前，这位行动者可以很容易地识别CUII的屏蔽，因为ISP的DNS服务器会将屏蔽的域名重定向到“notice.cuii.info”页面。然而，在之前的批评之后，大多数ISP转而简单地在其DNS记录中使被屏蔽的网站看起来不存在，从而有效地隐藏了审查行为。Telefonica (o2) 直到最近还在继续使用“notice.cuii.info”重定向。

作者注意到可疑活动：Telefonica网络中的某人使用cuiiliste.de来检查域名“blau-sicherheit.info”（可能是Telefonica的测试域名）是否被屏蔽。由于Telefonica的DNS报告该域名已被屏蔽，该网站正确地将其识别为已屏蔽。

此后不久，Telefonica更改了其DNS配置，完全删除了“notice.cuii.info”重定向。作者怀疑这是故意破坏cuiiliste.de，并使其更难追踪CUII屏蔽行为，因为这一更改发生在Netzpolitik文章发表后不久，并且使得区分CUII屏蔽和其他类型的屏蔽变得困难。虽然作者已经实施了一种解决方法，但他们对透明度降低以及追究CUII对其行为责任的难度增加表示遗憾。

---

## 10. 展示一下：自行车百科全书

**原文标题**: Show HN: Bicyclopedia

**原文链接**: [https://bicyclopedia.lemoing.ca/](https://bicyclopedia.lemoing.ca/)

自行车百科：互动式自行车部件探索。本项目旨在以视觉方式展示并解释自行车的各个部件。创作者承认，包括图像和动画在内的互动元素依赖于Javascript，可能无法供禁用Javascript的用户或使用屏幕阅读器的用户访问。然而，通过描述和源代码提供了替代访问方式。项目的目标和背景在单独的页面上进行了更详细的说明。引言文字主要用于欢迎访问者并管理关于可访问性限制的期望。

---

## 11. 如何构建编码代理

**原文标题**: How to build a coding agent

**原文链接**: [https://ghuntley.com/agent/](https://ghuntley.com/agent/)

杰弗里·亨特利的研讨会“如何构建编码代理”旨在揭秘AI编码代理的创建过程，认为它出人意料地简单，并且对2025年的开发者至关重要。他强调了从AI消费者到AI生产者转变的重要性，生产者能够自动化任务。

亨特利解释说，编码代理本质上是300行代码，在循环中运行LLM tokens。他强调理解这个循环以及如何构建代理的重要性，认为这是雇主所寻求的基本知识。他强调了代理可以同时处理任务的潜力，从而提高效率和生产力。

关键概念包括选择一个优先考虑工具调用的“代理型” LLM（如Claude Sonnet或Kimi K2），并有效地利用上下文窗口。他警告说，不要过度分配上下文窗口，放入过多的工具或MCP服务器，因为这会对性能产生负面影响。相反，他建议在每次活动后清除上下文窗口，以获得最佳结果。

他还谈到了LLM的不同专业化，将它们分为高安全性、低安全性、预言机和代理型模型，每种模型都适用于不同的任务。该研讨会演示了一个基本的聊天应用程序，其中LLM根据用户输入调用“get_weather”工具，说明了如何注册和调用工具。总的来说，该研讨会使开发者能够创建自己的编码代理，将他们从AI的消费者转变为AI驱动自动化的生产者。

---

## 12. 4chan是证明英国扩大网站封锁范围的完美盗版湾典型吗？

**原文标题**: Is 4chan the perfect Pirate Bay poster child to justify wider UK site-blocking?

**原文链接**: [https://torrentfreak.com/uk-govt-finds-ideal-pirate-bay-poster-boy-to-sell-blocking-of-non-pirate-sites-250824/](https://torrentfreak.com/uk-govt-finds-ideal-pirate-bay-poster-boy-to-sell-blocking-of-non-pirate-sites-250824/)

本文认为，英国旨在保护儿童的《网络安全法案》（OSA）实为掩盖审查意图之举，惩罚重视隐私者，扼杀异议。作者批评该法案范围过广，可能对大型网站处以罚款，以及要求进行年龄验证，实际上是将未经身份验证的成年人等同于儿童。

文章强调了政府提出的二元选择：要么你支持《网络安全法案》并保护儿童，要么你与网络掠食者为伍。令人担忧的是，政府试图压制批评者，包括要求删除帖子，以及威胁因社交媒体上被认为不可接受的评论而针对美国公民采取行动。

作者随后将2012年成功封锁海盗湾（TPB）与可能试图将4chan作为《网络安全法案》下更广泛的网站封锁的“典型案例”相提并论。TPB因其臭名昭著、缺乏合作以及未能进行辩护而被选中。

然而，与TPB不同，4chan已聘请美国律师，并计划根据美国联邦法律抵制Ofcom的行动，理由是《网络安全法案》侵犯了美国宪法权利。这构成了英国审查措施与美国言论自由保护之间的潜在冲突。

作者总结道，与TPB案件相比，对4chan采取强制行动将是一场灾难。此外，文章质疑首相基尔·斯塔默似乎不了解Ofcom针对美国公民的行动，暗示政府政策与监管机构的议程之间存在脱节。

---

## 13. 分形鼓机演奏任何节奏 [视频]

**原文标题**: Fractal drum machine plays any beat [video]

**原文链接**: [https://www.youtube.com/watch?v=-OG87X6XSWU](https://www.youtube.com/watch?v=-OG87X6XSWU)

文章标题为《分形鼓机演奏任何节拍[视频]》，似乎是指向YouTube视频的链接。标题之后的内容主要包含关于版权、联系方式、创作者、广告、开发者、条款、隐私政策、安全、YouTube运作方式、测试新功能以及NFL Sunday Ticket信息的标准YouTube样板文字。

因此，正如标题所示，这篇文章很可能展示了一种由分形几何控制或影响的鼓机。“[视频]”的标注表明提供了视觉演示和音频示例。“演奏任何节拍”的说法暗示了这种基于分形的鼓机具有高度的通用性和可编程性。

由于提供的内容主要是与YouTube相关的元数据和服务条款，而不是实际的文章文本，因此除了上述对标题的解读之外，无法进行详细的摘要。要全面了解分形鼓机及其功能，需要观看链接的YouTube视频。

---

## 14. Seed：基于Common Lisp的交互式软件环境

**原文标题**: Seed: Interactive software environment based on Common Lisp

**原文链接**: [https://github.com/phantomics/seed](https://github.com/phantomics/seed)

Seed：一个基于 Common Lisp 的交互式软件开发环境，旨在解决传统文本编程的局限性。它使用树形网格以可视化的方式呈现程序，从而实现更直观的理解和操作。Seed 致力于利用 Lisp 的灵活性来提供一种与底层结构无关的代码表示形式。

Seed 与 ASDF（标准 Common Lisp 构建系统）集成。使用 Seed 开发的系统通常被组织为 ASDF 系统，其分支代表输入和输出。项目目录中的 `.seed` 文件定义了系统的行为。

安装涉及几个步骤：确保您已安装 Common Lisp（特别是 SBCL）、ASDF 和 Quicklisp。 它还需要 Node.js、NPM 和 Gulp 来构建 Web 界面。 Node.js 可以通过 NVM（推荐）或通过软件包管理器或安装程序安装。 Gulp 通过 `npm install -g gulp` 全局安装。 克隆 Seed 存储库后，需要在 Quicklisp 的 local-projects 目录中创建一个符号链接。 自动安装程序（`install-seed.lisp`）尝试配置 Seed 及其依赖项。 或者，可以通过在 Common Lisp REPL 中通过 Quicklisp 加载 Seed 来执行手动安装。

要使用 SBCL 自动启动 Seed，可以将行添加到 `.sbclrc` 文件中。 Web 界面默认为端口 8055，可以通过 `http://localhost:8055/portal.demo1/index.html`（或自定义门户）访问。 提供了一个教程来指导新用户。 Seed 包含 Panic 的修改版本，Panic 是一个 React 组件构建实用程序。

---

## 15. 购买快速CPU是值得的。

**原文标题**: It is worth it to buy the fast CPU

**原文链接**: [https://blog.howardjohn.info/posts/buy-a-cpu/](https://blog.howardjohn.info/posts/buy-a-cpu/)

文章认为，尽管价格不菲，投资快速CPU，特别是AMD Ryzen 9 9950X，对于软件工程师来说是一项值得的投资。作者指出，公司乐于每年支付约500美元购买AI编程订阅服务以提高生产力，而高端CPU可以提供类似甚至更高的投资回报。

该论点基于旧款CPU和最新型号之间显著的性能差异。作者使用基准数据表明，在编译Linux内核和TLS操作等任务中，旧款笔记本电脑CPU（i7-1165G7）与新款笔记本电脑（AMD Ryzen 7840U）和台式机（AMD Ryzen 9950X）相比，性能提升高达10倍。这种性能飞跃转化为开发人员可观的时间节省，例如将构建时间从30秒缩短到3秒。

作者通过比较顶级CPU的年度摊销成本（三年内约170美元）与AI编程订阅服务的500美元价格标签，进一步强调了成本效益。文章总结说，如果公司愿意投资AI工具来提高工程生产力，那么他们也应该优先为工程师提供最快的可用硬件，尤其是CPU，因为它们提供类似且引人注目的投资回报。作者概括了以下观察结果：台式机CPU大约比笔记本电脑CPU快3倍，并且新CPU大约比三年前的顶级型号快3倍。

---

## 16. 中断工作的代价 (2023)

**原文标题**: The cost of interrupted work (2023)

**原文链接**: [https://blog.oberien.de/2023/11/05/23-minutes-15-seconds.html](https://blog.oberien.de/2023/11/05/23-minutes-15-seconds.html)

这篇博客文章调查了被广泛引用的一个统计数据，即被打断后需要 23 分 15 秒才能重新集中注意力。作者最初试图验证这一说法，但难以在学术论文中找到其来源。

虽然许多博客文章重复了这个数字，但作者在追溯到原始研究时发现了不一致之处。经常被引用的主要论文《中断工作的代价：更高的速度和压力》表明，中断工作实际上比不中断工作花费的时间更少（尽管压力更大），并且没有提及 23 分 15 秒的恢复时间。其他探索任务切换和中断的相关论文也没有提供证据支持这个具体的恢复时长。

调查显示，23 分 15 秒这个数字主要归因于对频繁被引用的论文作者 Gloria Mark 的采访。尽管博客文章甚至《华尔街日报》多次引用 Mark，但作者未能找到包含此数字的原始印刷来源（即已发表的研究或论文）。文章最后邀请读者分享任何关于该统计数据原始来源的知识。

---

## 17. Valve软件公司新员工手册[pdf] (2012)

**原文标题**: Valve Software handbook for new employees [pdf] (2012)

**原文链接**: [https://cdn.akamai.steamstatic.com/apps/valve/Valve_NewEmployeeHandbook.pdf](https://cdn.akamai.steamstatic.com/apps/valve/Valve_NewEmployeeHandbook.pdf)

我无法从这份文件中提取并总结有意义的信息。它似乎是一个PDF文件，但内容主要是机器代码和编码数据，而非人类可读的文本。在提供的文本中，没有可辨识的Valve员工手册内容，我无法进行总结。

---

## 18. 最优传输与Wasserstein距离简短介绍 (2020)

**原文标题**: A short introduction to optimal transport and Wasserstein distance (2020)

**原文链接**: [https://alexhwilliams.info/itsneuronalblog/2020/10/09/optimal-transport/](https://alexhwilliams.info/itsneuronalblog/2020/10/09/optimal-transport/)

本文简要介绍了最优传输 (OT) 理论和Wasserstein距离，作为衡量概率分布之间距离的一种替代方法，以克服KL散度等差异性指标的不足。KL散度存在不对称性，并且在分布具有不重叠支撑集时可能出现无穷大。

OT理论使用物理类比，将泥土（概率质量）从土堆（一个分布）移动到洞穴（另一个分布），目标是最小化运输成本。成本通常由距离度量定义，例如平方欧几里得距离。传输方案T指定了从每个起点到每个终点移动多少泥土，并受限于确保初始泥土用完且洞穴被填满的约束。Wasserstein距离，也称为推土机距离，是最小的运输成本，具有对称性并满足三角不等式，从而克服了KL散度的局限性。

本文用2D和1D示例说明了OT，展示了在非重叠支撑集的情况下，Wasserstein距离如何提供比KL散度更直观的结果。然后，详细介绍了如何离散化连续分布，以使用线性规划计算Wasserstein距离。优化问题的目标是最小化总运输成本，并受限于边际分布的约束。最后，本文提供了一个使用`scipy.optimize.linprog`求解此线性程序的Python实现。

---

## 19. 用于火车摄影的线扫描相机图像处理

**原文标题**: Line scan camera image processing for train photography

**原文链接**: [https://daniel.lawrence.lu/blog/y2025m09d21/](https://daniel.lawrence.lu/blog/y2025m09d21/)

本文详细介绍了使用线扫描相机捕捉和处理图像的过程，主要用于拍摄火车。作者描述了相机的工作原理，即单列（或双列）像素扫描移动的物体，从而产生具有最小透视畸变的高分辨率图像。

处理步骤包括：

1.  **感兴趣区域检测：** 计算“能量函数”以识别移动物体，并避免处理静态背景，从而提高效率。
2.  **速度估计：** 通过比较拜耳阵列中的两个绿色通道，估计物体的速度，并用于校正图像中的拉伸或挤压。将样条曲线拟合到嘈杂的位移估计值，以实现亚像素精度。
3.  **重采样：** 使用速度估计值（样条函数），使用汉宁窗对原始数据进行重采样，以避免因基本列选择而产生的混叠和伪影。
4.  **去马赛克：** 使用双线性插值来解决因拜耳阵列布局引起的条纹问题。
5.  **垂直条纹去除：** 使用线性回归和迭代加权最小二乘法来消除由时钟抖动和曝光时间变化引起的垂直条纹。指数平滑提供了一种更快的替代方法。
6.  **降噪：** 基于块匹配的降噪器（块匹配）利用火车照片中发现的重复纹理，通过平均相似的块来降低噪声。泊松噪声的考虑也有助于降噪。
7.  **倾斜校正：** 计划在使用速度估计后但在最终重采样之前，使用霍夫变换自动校正相机倾斜。
8.  **色彩校准：** 使用手动调整的色彩校准矩阵。

作者强调了挑战，例如噪声数据、对稳健算法的需求以及某些步骤（如降噪）的计算强度。

---

## 20. SSD-IQ：揭示固态硬盘性能的隐藏面 [pdf]

**原文标题**: SSD-IQ: Uncovering the Hidden Side of SSD Performance [pdf]

**原文链接**: [https://www.vldb.org/pvldb/vol18/p4295-haas.pdf](https://www.vldb.org/pvldb/vol18/p4295-haas.pdf)

抱歉，我无法访问外部网址或本地文件，因此无法提供PDF文件内容的摘要。

---

## 21. 如果每个城市都有一条伦敦地上铁会怎样？

**原文标题**: What if every city had a London Overground?

**原文链接**: [https://www.dwell.com/article/what-if-every-city-had-a-london-overground-ac7a7ff9](https://www.dwell.com/article/what-if-every-city-had-a-london-overground-ac7a7ff9)

本文探讨了伦敦地上铁的成功，并建议在其他城市复制类似系统所带来的益处。虽然伦敦地铁极具标志性，但地上铁，一个由改造和升级现有线路而建成的网络，提供了更令人愉快和用户友好的体验。它宽敞、通风、安静，并提供日光景观，与老旧、拥挤且通常不舒适的地铁形成了鲜明对比。

地上铁的成功归功于以下几个因素：它连接了以前服务不足的地区，刺激了经济增长；它被认为对于患有神经多样性或行动障碍的人来说更容易导航；其令人愉悦的环境培养了一种社区意识。改善的体验鼓励了客流量，从而带来进一步的投资和改善。

本文强调了清洁、顺畅和安全的服务所带来的心理影响，即使底层基础设施相似。它还强调了社会层面，指出地上铁营造了一个更轻松的环境，允许更多的社会互动和观察人群，这有助于创造一个更健康的城市环境。

作者的结论是，伟大的公共交通不仅仅是便利；它还在于创造一种积极的体验，有助于个人和整个社区的福祉。伦敦地上铁可以作为如何将现有基础设施转化为促进经济增长和社会凝聚力的宝贵资产的典范。

---

## 22. 世界上最古老的未开封葡萄酒

**原文标题**: The oldest unopened bottle of wine in the world

**原文链接**: [https://www.openculture.com/2025/08/the-oldest-unopened-bottle-of-wine-in-the-world.html](https://www.openculture.com/2025/08/the-oldest-unopened-bottle-of-wine-in-the-world.html)

本文探讨了莱茵葡萄酒（Römerwein），也称施佩耶尔葡萄酒瓶，据信是世界上最古老未开封的葡萄酒瓶。该瓶于公元4世纪在德国一座罗马贵族墓穴中被发现，其年代可追溯到公元325年至359年之间。这是一个1.5升的玻璃容器，形状像海豚，用厚厚的蜡和橄榄油塞子密封，维持着密闭环境。

尽管由于乙醇可能已经挥发，这种葡萄酒已不再适合饮用，但科学家们推测瓶内液体仍含有大量葡萄酒，并掺杂了草药。目前，该酒瓶藏于施佩耶尔普法尔茨历史博物馆。

本文还提到了西西里岛卡塔尼亚大学为重现古罗马酿酒技术所做的努力。研究人员建立了一个采用传统方法的葡萄园，避免机械化、农药和化肥，并遵循维吉尔和科卢梅拉古代文献中的指导。古罗马酿酒师经常在葡萄酒中添加蜂蜜、水和草药来调味。

---

## 23. 德国版权清算中心现在要求法院进行网站屏蔽

**原文标题**: Germany's Copyright Clearing House now requires courts for website blocks

**原文链接**: [https://www.heise.de/en/news/Copyright-clearing-house-Committee-for-website-blocking-to-rely-on-judiciary-10490128.html](https://www.heise.de/en/news/Copyright-clearing-house-Committee-for-website-blocking-to-rely-on-judiciary-10490128.html)

德国版权结算中心现要求法院介入网站封锁

---

## 24. Wildthing - 一个基于角色反转ChatGPT对话训练的模型

**原文标题**: Wildthing – A model trained on role-reversed ChatGPT conversations

**原文链接**: [https://youaretheassistantnow.com/](https://youaretheassistantnow.com/)

该文章介绍了新型人工智能模型“Wildthing”，它经过特别训练，使用了与ChatGPT角色互换的对话。这意味着训练数据由ChatGPT扮演通常由用户承担的角色、而用户扮演AI的对话组成。

关键在于，基于这些反转角色的训练旨在提高Wildthing对用户意图的理解，从而有可能产生更好、更细致、更富同理心的回应。通过从相反的角度体验对话，该模型可能会更深入地了解用户提示背后的复杂性和动机。

本质上，希望通过让AI“设身处地为用户着想”，它可以成为一个更有效、更具洞察力的对话代理。这种特定训练方法的有效性以及Wildthing模型由此产生的能力，可能会在更长、更详细的文章中进一步探讨，但这是目前提出的核心前提。

---

## 25. 美国打压可再生能源将导致电力短缺，推高电价。

**原文标题**: US attack on renewables will lead to power crunch that spikes electricity prices

**原文链接**: [https://www.cnbc.com/2025/08/24/solar-wind-renewable-trump-tariff-utility-tax-credit-itc-ptc-obbb-electricity-price.html](https://www.cnbc.com/2025/08/24/solar-wind-renewable-trump-tariff-utility-tax-credit-itc-ptc-obbb-electricity-price.html)

CNBC：特朗普反对风光项目或致电力短缺，电价或飙升。

---

## 26. Show HN: Port Kill – 一款轻量级的 macOS 状态栏开发端口监视器

**原文标题**: Show HN: Port Kill – A lightweight macOS status bar development port monitor

**原文链接**: [https://github.com/kagehq/port-kill](https://github.com/kagehq/port-kill)

端口杀手：一款轻量级的 macOS 状态栏应用，旨在监控和管理运行在 2000-6000 端口上的开发进程。它每 5 秒使用 `lsof` 命令进行实时进程检测，并通过颜色编码的状态栏图标显示进程数量（绿色为 0，红色为 1-9，橙色为 10+ 个进程）。

该应用具有动态上下文菜单，每 3 秒更新一次，显示当前进程并允许用户终止它们。虽然目前设置为通过任何菜单选择杀死所有进程（用于测试），但其预期功能是使用 SIGTERM，然后使用 SIGKILL 终止策略来终止单个进程或一次终止所有进程。

端口杀手使用 Rust 构建，使用 `winit` 进行事件循环，`nix` 用于信号处理，以及其他几个库用于并发、错误处理和序列化。它需要 macOS 10.15+、Rust 1.70+ 和 `lsof`。

安装包括克隆存储库，使用 `cargo build --release` 构建，并使用 `./run.sh` 运行。故障排除技巧解决了权限问题、进程检测失败和应用程序启动问题。该项目以 FSL-1.1-MIT 许可证授权，并欢迎通过 pull request 进行贡献。

---

## 27. ThinkMesh：用于LLM并行思考的Python库

**原文标题**: ThinkMesh: A Python lib for parallel thinking in LLMs

**原文链接**: [https://github.com/martianlantern/ThinkMesh](https://github.com/martianlantern/ThinkMesh)

ThinkMesh是一个Python库，旨在通过并行执行不同的推理路径来增强大型语言模型(LLM)的推理能力。 它利用内部置信度信号对这些路径进行评分，并重新分配资源给更有希望的分支，从而智能地管理计算资源。 然后，该库使用验证器和归约器融合结果。

主要特性包括：

*   **并行推理：** 采用DeepConf风格的置信度门控和预算重新分配。
*   **离线和托管支持：** 与离线Hugging Face Transformers、用于服务器端批处理的vLLM/TGI以及OpenAI和Anthropic等托管API无缝协作。
*   **异步执行：** 使用动态微批处理以实现高效处理。
*   **灵活的结果处理：** 提供归约器（多数/判断）和可插拔的验证器（正则表达式/数值/自定义）。
*   **增强的可观察性：** 包括缓存、指标和JSON跟踪，用于调试和分析。

ThinkMesh支持各种推理策略，包括DeepConf、自洽性、辩论和思维树，并为每种策略提供了示例。它允许用户自定义验证器并实现新的后端和策略。该库被设计为可扩展的，并提供了添加新的归约器和验证器的方法。它还集成了缓存、通过Prometheus提供的指标以及OpenTelemetry，以实现全面的监控。

---

## 28. 是什么让 Claude Code 如此出色

**原文标题**: What makes Claude Code so damn good

**原文链接**: [https://minusx.ai/blog/decoding-claude-code/](https://minusx.ai/blog/decoding-claude-code/)

本文分析了是什么让Claude Code (CC) 成为一个令人愉悦且高效的AI编码助手，并为构建类似的LLM Agent提供了指南。关键在于**“保持简单，笨蛋！”** 优先考虑可调试性，并在利用模型优势的同时，减轻其劣势。

CC的优势在于：

*   **简单的控制循环：** 单一主循环，扁平化的消息历史，以及最多一个子代理分支，避免复杂的多Agent系统。
*   **大量使用较小模型：** 采用更便宜、更快的模型，如`claude-3-5-haiku`，来完成诸如解析文件和总结对话等任务。
*   **精心设计的提示词：** 利用`claude.md`文件来获取用户上下文和偏好，并采用XML标签（`<system-reminder>`，`<good-example>`）和Markdown来构建结构、启发式和示例。
*   **LLM搜索优于RAG：** 采用复杂的ripgrep和find命令，而非RAG来进行代码搜索，直接利用LLM对代码的理解，并支持强化学习。
*   **策略性工具设计：** 根据使用频率和准确性，混合使用低级（Bash、Read、Write）、中级（Edit、Grep、Glob）和高级工具（WebFetch）。
*   **自我管理的待办事项清单：** Agent维护自己的待办事项清单，确保专注度和灵活地进行纠正。
*   **可控性：** 明确控制语气和风格，使用“重要”提醒，并编写带有启发式和示例的算法来指导LLM。

通过专注于简单性，利用较小的模型，精心设计提示词，并使用有效的搜索和工具设计，开发者可以创建具有类似Claude Code用户体验的LLM Agent。

---

## 29. Apache Kafka 为什么被创建？

**原文标题**: Why was Apache Kafka created?

**原文链接**: [https://bigdata.2minutestreaming.com/p/why-was-apache-kafka-created](https://bigdata.2minutestreaming.com/p/why-was-apache-kafka-created)

本文阐述了 LinkedIn 在 2012 年左右创建 Apache Kafka 以解决其数据集成问题的原因。他们现有的管道，一个用于数据仓库的批量管道和一个用于可观测性的实时管道，都是手动密集型的，存在大量积压，并且缺乏集成。

核心问题包括：解析数百个 XML 模式、因依赖于网站功能的管道而导致的管道脆弱性、模式演变的复杂性、活动指标的滞后以及数据孤岛式地存储在单个目的地中。

LinkedIn 对新系统的要求是：稳健且可扩展的基础设施、适当的模式处理、高扇出、实时处理、即插即用集成以及数据所有权转移给数据创建者。他们还需要一个支持数据积压的系统。

Kafka 解决了稳健性、可扩展性、高读取扇出、实时处理以及写入器与读取器的解耦。为了解决剩余问题，LinkedIn 采用了 Apache Avro 用于模式和序列化，开发了一个类似于模式注册表的服务用于版本控制，并强制执行模式兼容性。他们旨在实现单一、统一的模式，以实现即插即用集成，并将数据所有权和治理权转移给创建数据的团队，从而建立强制性的代码审查流程。

作者强调了模式的重要性，并指出 Kafka 缺乏一流的模式支持一直是一个限制。他赞扬了 Buf 的模式驱动开发愿景，该愿景强调通用模式和服务器端验证，以强制执行统一模式。

---

## 30. 在ESP-IDF上设置串口波特率无效

**原文标题**: Setting serial baud rate on ESP-IDF does nothing

**原文链接**: [https://atomic14.substack.com/p/this-number-does-nothing](https://atomic14.substack.com/p/this-number-does-nothing)

Atomic14 的文章《ESP-IDF 中设置串口波特率无效》讨论了在使用 ESP-IDF 框架在 ESP32 上进行串口通信时观察到的一个令人惊讶的现象。作者发现**在 ESP-IDF 配置中更改波特率设置（通过 `menuconfig`）似乎对实际的串口通信速度没有任何影响。**

尽管在 `menuconfig` 中设置了各种波特率（例如，115200、9600），但作者观察到 ESP32 始终以默认波特率 115200 进行通信。这导致了调试工作，以了解为什么配置的值被忽略。

关键的发现是**虽然 `menuconfig` 确实允许更改波特率，但项目中的实际初始化代码用硬编码值 115200 覆盖了此设置。** 作者明确指出了负责此覆盖的特定代码行。

文章总结说，开发人员需要意识到**仅仅更改 `menuconfig` 中的波特率不足以改变 ESP32 上使用 ESP-IDF 的串口通信速度。** 他们必须确保串口的实际初始化代码没有将波特率显式设置为固定值。 作者建议仔细检查源代码，尤其是在遇到意外的串口通信行为时。

---

## 31. 将Claude代码变成我最佳的设计伙伴

**原文标题**: Turning Claude Code into my best design partner

**原文链接**: [https://betweentheprompts.com/design-partner/](https://betweentheprompts.com/design-partner/)

本文详细介绍了一种有效利用 Claude Code 作为设计伙伴的工作流程，它超越了简单的“提示和修复”方法。作者发现，由于对话上下文限制以及对话成为唯一的真理来源，这种幼稚的方法无法扩展到复杂的任务。

改进后的工作流程的核心在于在实施之前和期间使用 Claude Code 创建和维护一个“动态计划文档”。初始提示描述了要实现的功能，Claude Code 生成一个计划，概述了需求、实施细节（包括代码片段）和质量检查。这个计划成为了唯一的真理来源。

作者参与协作设计过程，在开始编码之前与 Claude Code 讨论和完善计划。这有助于识别更好的方法并挑战假设。至关重要的是，计划文档会随着实施的进展而不断更新。Claude Code 被指示在每次提交代码时更新计划，以反映开发过程中所做的更改和决策。

这种“动态文档”方法通过允许与清晰、最新的上下文进行新的对话来缓解上下文限制。作者在更新后的计划的指导下审查代码，并发现强制性的计划和文档编制使他们成为一名更好的开发人员。

该工作流程为在较简单的方法中遇到的问题提供了一个系统的解决方案，从而带来一个更周到、有据可查且可靠的开发过程，其中 AI 充当协作设计伙伴。

---

## 32. 使用 CSS random() 掷骰子

**原文标题**: Rolling the dice with CSS random()

**原文链接**: [https://webkit.org/blog/17285/rolling-the-dice-with-css-random/](https://webkit.org/blog/17285/rolling-the-dice-with-css-random/)

本文介绍了 CSS 的 `random()` 函数，这是一项无需 JavaScript 即可直接在 CSS 中生成随机数的新功能。该函数最多接受三个参数：`random(min, max, step)`，用于定义随机值的范围和可选增量。

作者通过几个例子展示了 `random()` 的用法：创建具有随机星位和大小的动态星空，在网格中生成随机放置和着色的矩形，以及构建一堆随机方向的照片。他们还演示了使用 `random()` 创建一个交互式“幸运轮盘”动画。

本文强调了“共享随机性”的重要性，以及如何通过自定义属性和 `element-shared` 关键字来实现它。使用命名标识符（如 `--random-star-size`）可确保单个元素内的多个属性使用相同的随机值。`element-shared` 关键字使应用给定样式的​​所有元素共享该属性的相同随机值。

作者鼓励开发者在 Safari Technology Preview 中试验 `random()`，并向 CSS 工作组提供反馈。他们征求关于可用性、潜在的缺失用例以及改进建议的意见，以帮助塑造该功能的最终规范。

---

## 33. AI 如何识别猫？

**原文标题**: How can AI ID a cat?

**原文链接**: [https://www.quantamagazine.org/how-can-ai-id-a-cat-an-illustrated-guide-20250430/](https://www.quantamagazine.org/how-can-ai-id-a-cat-an-illustrated-guide-20250430/)

如何用AI识别猫？图解指南

本文阐述了神经网络（一种人工智能）如何学习识别图像，特别是猫。文章对比了手动编程计算机识别猫照片的难度与神经网络的方法，后者依赖于从海量数据集中的学习。

文章首先用地图类比简化了分类的概念，地图上有两个区域：三角形领地和正方形州。一个单独的神经元充当分类器，通过根据已知数据点在区域之间绘制边界。该边界的位置由参数（权重和偏置）决定，这些参数在“训练”过程中进行调整。神经元根据正确/不正确的分类尝试来调整其参数。

然后，文章扩展到“神经网络”，它由分层排列的互连神经元组成，能够处理比单个神经元更复杂的任务。神经元和层数越多，网络可以学习的边界就越复杂。

为了将其与图像识别联系起来，文章解释了如何将像素值表示为神经网络的数值输入。例如，一个 50x50 像素的图像对应于一个 2,500 维空间中的点。通过对大量图像进行训练，网络可以学习区分该空间中的“猫”和“非猫”区域。

最后，文章指出，通过增加输出，网络可以识别多个类别的对象。文章还简要提及了神经网络被应用于像 ChatGPT 这样的大型语言模型，并强调了对理解这些复杂人工智能系统内部运作的持续研究。

---

## 34. Motion (YC W20) 招聘首席软件工程师

**原文标题**: Motion (YC W20) Is Hiring Principal Software Engineers

**原文链接**: [https://jobs.ashbyhq.com/motion/7355e80d-dab2-4ba1-89cc-a0197e08a83c?utm_source=hn](https://jobs.ashbyhq.com/motion/7355e80d-dab2-4ba1-89cc-a0197e08a83c?utm_source=hn)

Motion招聘首席软件工程师职位，该公司曾参与Y Combinator W20项目。该职位强调JavaScript是Motion的关键技术，表明该职位涉及构建Web应用程序或相关系统。内容简洁，但明确表明Motion正在积极寻找一位技术精湛且经验丰富的首席软件工程师加入他们的团队。鉴于职位名称和提及JavaScript，可以推断Motion是一家科技公司。

---

## 35. 埃及罗马士兵戴的2000年历史的太阳帽

**原文标题**: A 2k-year-old sun hat worn by a Roman soldier in Egypt

**原文链接**: [https://www.smithsonianmag.com/smart-news/a-2000-year-old-sun-hat-worn-by-a-roman-soldier-in-egypt-goes-on-view-after-a-century-in-storage-180987192/](https://www.smithsonianmag.com/smart-news/a-2000-year-old-sun-hat-worn-by-a-roman-soldier-in-egypt-goes-on-view-after-a-century-in-storage-180987192/)

一顶有2000年历史的毡帽，很可能由古埃及的罗马士兵佩戴，经过修复后现正在英国博尔顿的博尔顿博物馆展出。这顶帽子于1911年由著名埃及学家威廉·马修·弗林德斯·皮特里捐赠给博物馆。帽子可追溯到公元前30年后的罗马统治埃及时期，为了解罗马士兵如何适应埃及气候提供了线索。

博物馆文物修复师杰奎·海曼精心修复了这顶被飞蛾损坏的帽子，用类似的手工染色织物稳定了脆弱区域，同时保持了它的原始形状。修复工作由当地一家企业资助。

虽然罗马人通常不戴帽子，但下层阶级和以前被奴役的人会戴类似于希腊航海帽的毡帽。然而，这顶特殊的帽子很可能经过改造以适应埃及的环境，并且是现存仅有的三个同类帽子之一。其他的收藏在曼彻斯特和佛罗伦萨。

这顶帽子将在博尔顿博物馆的埃及展厅展出至九月，之后将转移到一个永久性展览。博物馆官员强调了这件文物的稀有性和保存价值，突出了它对这座城市的意义。

---

## 36. 德州仪器新厂，苹果将在该厂生产iPhone芯片

**原文标题**: Texas Instruments’ new plants where Apple will make iPhone chips

**原文链接**: [https://www.cnbc.com/2025/08/22/apple-will-make-chips-at-texas-instruments-60-billion-us-project.html](https://www.cnbc.com/2025/08/22/apple-will-make-chips-at-texas-instruments-60-billion-us-project.html)

德州仪器投资600亿美元在美国建设大型制造项目，包括七家新工厂，以生产基础微芯片。苹果公司已承诺使用位于德克萨斯州和犹他州的这些工厂，为iPhone和其他设备生产“关键基础半导体”，这是其6000亿美元美国支出承诺的一部分。

位于德克萨斯州谢尔曼的第一家新工厂预计将于2025年底全面投产。德州仪器旨在向英伟达、福特、美敦力及SpaceX等主要客户提供芯片，从而利用各种设备中对模拟和嵌入式芯片的需求。尽管存在潜在的市场不确定性和关税担忧，但分析师认为，德州仪器的美国代工厂可能会使其在价格上获得优于竞争对手的优势。

德州仪器的扩张包括过渡到300毫米晶圆以提高成本效益，并依赖可再生能源。该公司还通过与大学和社区学院的合作，解决与用水、电力供应和劳动力发展相关的挑战。该项目促进了德克萨斯州谢尔曼的发展，使其成为半导体产业的中心，并获得了联邦和州政府的激励支持。德州仪器的扩张旨在重获市场份额，创造美国就业机会，并巩固其在全球半导体市场中的地位。

---

## 37. 未使用时，Acronis True Image会降低性能。

**原文标题**: Acronis True Image costs performance when not used

**原文链接**: [https://randomascii.wordpress.com/2025/05/26/acronis-true-image-costs-performance-when-not-used/](https://randomascii.wordpress.com/2025/05/26/acronis-true-image-costs-performance-when-not-used/)

布鲁斯·道森调查了与Acronis True Image相关的性能问题，特别是与Crucial SSD捆绑的版本。他发现即使在未主动使用时，Acronis True Image（特别是`tishell64.dll`）也会因外部显示器插拔等事件触发的过度进程枚举而显著降低系统性能。

道森使用Windows性能分析器(WPA)来精确定位问题，发现`explorer.exe`消耗了过多的CPU时间，这是由于`tishell64.dll`中重复调用`CreateToolhelp32Snapshot`和`Process32NextW`造成的。 他发现Acronis在显示器连接/断开事件期间会遍历数千次正在运行的进程列表。 他估计在极端情况下，拔下外部显示器时，`tishell64.dll`会消耗高达60秒的CPU时间。

他确定`tishell64.dll`是Acronis True Image的一部分。道森联系了Acronis，后者确认了该问题并计划在未来的版本中修复它。作为一种解决方法，他建议删除负责进程枚举的注册表项，或者更激进地卸载Acronis True Image，特别是Crucial分发的可能已过时的版本。

道森还批评微软和Acronis发布缺少关键元数据（如文件版本信息）的DLL。他总结说，Acronis需要大幅减少或消除不必要的进程枚举，以解决性能问题。

---

## 38. 为我的个人用例评估大型语言模型

**原文标题**: Evaluating LLMs for my personal use case

**原文链接**: [https://darkcoding.net/software/personal-ai-evals-aug-2025/](https://darkcoding.net/software/personal-ai-evals-aug-2025/)

本文详细介绍了对各种大型语言模型（LLM）在日常实用中的个人评估，重点关注成本和延迟这两个主要区别因素，因为大多数模型在作者的任务中表现良好。作者使用了来自其命令行历史记录中的130个真实提示，这些提示被分为编程、系统管理、技术解释和通用知识/创意任务等类别。

评估包括通过Open Router访问的Claude Sonnet、DeepSeek、Gemini、Kimi、GPT-OSS和Qwen等模型。作者发现，闭源模型（Gemini、Claude）并没有比开源替代方案明显更好，并且Gemini 2.5 Flash速度非常快。推理能力仅在诗歌等创意任务中显著提高了结果。

主要发现：评估很困难，所有模型都很好，成本和延迟是决定因素，闭源模型不一定更好，推理并非总有帮助，Gemini 2.5 Flash速度快，Gemini 2.5 Pro定价过高。

基于该评估，作者采用了一种多模型方法：DeepSeek用于快速查询，Gemini Flash和Qwen用于提供第二意见，Qwen3-Thinking、Claude Sonnet和DeepSeek用于需要更多“脑力”的任务。作者强调了评估的个人性和主观性，以及Open Router提供商质量对结果的影响。

---

## 39. 羽毛球新型旋转发球的物理学

**原文标题**: Physics of badminton's new killer spin serve

**原文链接**: [https://arstechnica.com/science/2025/08/physics-of-badmintons-new-killer-spin-serve/](https://arstechnica.com/science/2025/08/physics-of-badmintons-new-killer-spin-serve/)

本文探讨了羽毛球运动中备受争议的“旋转发球”背后的物理原理，这是一种球员在发球前给羽毛球增加预旋的技术。旋转发球非常有效，以至于世界羽毛球联合会（BWF）因担心造成不公平优势而暂时禁止了该技术。

现在，中国物理学家分析了旋转发球的空气动力学原理，并在《流体物理学》上发表了他们的研究成果。他们使用羽毛球的数字模型，运行了具有不同预旋条件的三维流体动力学模拟。

模拟结果确定了羽毛球轨迹的三个阶段：翻转、振荡和稳定。他们发现，与羽毛球的自然旋转方向相反的预旋会延长振荡阶段，由于羽毛受到的压力增加以及水平速度的更大降低，导致“下沉和摇摆”模式。

作者认为他们的研究可以帮助球员更好地理解旋转发球技术，并有助于回球。他们承认羽毛球形状的变化可能会影响结果，并计划未来研究不同的配置，以及对各种发球进行动作捕捉研究，以进一步提高羽毛球技术。

---

## 40. 自主代理浏览器安全：Perplexity Comet 中的间接提示注入

**原文标题**: Agentic Browser Security: Indirect Prompt Injection in Perplexity Comet

**原文链接**: [https://brave.com/blog/comet-prompt-injection/](https://brave.com/blog/comet-prompt-injection/)

本文探讨了浏览器AI助手“Leo”的演变，从简单的浏览工具发展为更主动和个性化的协作者。它突显了我们对AI及其在网络浏览体验中的角色的思考方式的转变。

关键在于，浏览器AI正在超越简单地基于用户查询提供信息。相反，它正在成为一个智能伴侣，预测用户需求并提供量身定制的帮助。这预示着未来AI将深度融入网络，增强生产力、个性化和整体用户体验。本文可能详细介绍了Leo的一些新功能和未来发展计划，这些功能和计划促进了向更具代理性和协作性的浏览体验的转变。

---

## 41. 使用 Python、uv、Caddy 和 Docker 构建静态站点

**原文标题**: Static sites with Python, uv, Caddy, and Docker

**原文链接**: [https://nkantar.com/blog/2025/08/static-python-uv-caddy-docker/](https://nkantar.com/blog/2025/08/static-python-uv-caddy-docker/)

Nik Kantar 详细介绍了部署 Python 构建的静态网站的首选技术栈：Python、uv、Caddy 和 Docker。他因 uv 的速度和 Python 可执行文件管理能力而采用它，并在各种项目中使用。

文章重点介绍了一个多阶段 Docker 构建过程。第一阶段基于 Astral 提供的带有 uv 的 Debian 镜像，安装特定的 Python 版本（3.13），并使用 `uv run` 构建静态网站。第二阶段使用 Caddy 镜像来提供网站服务。它将生成的静态网站复制到 Caddy 的服务目录，并包含用于配置的 Caddyfile。

Caddyfile 示例配置了多个域名来提供内容，将根目录定义为 `/srv` 并利用 `file_server`。一个特别强调的配置细节是代理 Plausible Analytics 脚本以保护隐私。

文章还提供了其他 Caddy 配置的示例，包括自定义错误页面、特定路径的特定内容类型以及重定向。

Kantar 总结说，这个技术栈已被证明是成功的，并计划使用 Dockerfile 中的单个 `just build` 命令来标准化他的项目构建过程。

---

## 42. 速成数独解题教程 (函数式明珠) [pdf]

**原文标题**: A Clash Course in Solving Sudoku (Functional Pearl) [pdf]

**原文链接**: [https://unsafeperform.io/papers/2025-hs-clash-sudoku/2025-hs-clash-sudoku.pdf](https://unsafeperform.io/papers/2025-hs-clash-sudoku/2025-hs-clash-sudoku.pdf)

根据标题“解数独速成课（函数式明珠）”以及所提供的PDF内容（虽然由于编码问题大多无法读取），我们可以推断出以下摘要：

这篇文章很可能介绍了一种使用函数式编程方法解决数独难题的方案。作为一篇“函数式明珠”，它可能会展示一个优雅、简洁，并且可能新颖的数独求解器的函数式实现。

关键信息将围绕以下几点展开：

1.  **数独问题：** 简要概述数独规则以及解决数独所涉及的挑战。
2.  **函数式编程原则：** 如何应用函数式编程范式（例如，不变性、递归、高阶函数）来建模和解决数独。
3.  **实现细节：** 函数式数独求解器中使用的具体数据结构和算法。这很可能包含大量代码，以展示函数式方法的优雅性和简洁性。
4.  **优点和缺点：** 讨论函数式方法的优势（例如，代码清晰、更易于推理、潜在的并行化能力）与传统命令式方法相比。以及潜在的缺点（例如，在某些情况下的性能考虑）。
5.  **示例和应用：** 通过示例演示函数式求解器，并可能讨论扩展或相关应用。

这篇文章旨在从函数式编程的角度提供一个数独求解的“速成课”（快速而集中的介绍）。它很可能面向有兴趣探索函数式编程在解决经典约束满足问题方面的强大功能和美感的程序员。在没有可读内容的情况下，这是最好的推断。

---

## 43. 家庭项目 (2022)

**原文标题**: A Family Project (2022)

**原文链接**: [https://bittersoutherner.com/feature/2022/a-family-project](https://bittersoutherner.com/feature/2022/a-family-project)

2022年2月，劳拉琳·多塞特讲述了她母亲于2021年8月去世的故事以及随后开展的一个非同寻常的家庭项目：将她安葬在他们在北卡罗来纳州的房产上。在经历了萝拉·威尔丁与帕金森症作斗争以及疫情限制使他们无法直接照顾她的挑战之后，多塞特和她的三个兄弟决心在母亲去世后将她带回家。

尽管最初对合法性和后勤保障存在疑问，但他们发现北卡罗来纳州允许家庭葬礼。随之而来的主要挑战变成了实际操作：制作棺材和挖掘坟墓。邻居慷慨地提供了木材，而擅长木工的兄弟们设计并制作了棺材。他们选择了多塞特菜园里一个能看到山景的地方，这对于他们热爱园艺的母亲来说是一个合适的安息之所。

挖掘工作是一项合作成果，在最近一场雨的滋润下，土壤变得松软，大约花了三个小时。在她去世后，他们开车将她带回家，用红色的丝绸和花园里的花朵铺满了棺材，并举行了一个私人仪式。没有殡仪馆长或牧师，他们将母亲放入地下，一起填满了坟墓，完成了一个深刻的个人和有意义的告别仪式。

在随后的几个月里，多塞特将这个项目视为兄弟姐妹情谊的证明，以及以一种最后的、亲力亲为的方式在家照顾母亲的能力的证明。这篇文章强调了该家庭通过回归自然葬礼方式并为他们的母亲创造一个有意义的安息之地来规避传统的能力。

---

## 44. 等距地球 - 世界政治挂墙地图 (2018)

**原文标题**: Equal Earth – Political Wall Map (2018)

**原文链接**: [https://equal-earth.com/index.html](https://equal-earth.com/index.html)

等积地球政治挂图是一幅免费的高分辨率世界地图，旨在准确地呈现各国和各大洲相对于彼此的真实大小，纠正其他投影中常见的失真。它提供多种尺寸的下载和打印版本。该地图以三个不同的区域（非洲/欧洲、美洲以及东亚/澳大利亚）为中心提供，并提供多种语言版本。

主要特点包括其大尺寸（55英寸 x 29英寸）、详细而简洁的设计，包含超过2,600个标签，以及专业的视觉设计。它以350 DPI的RGB JPEG图像提供，并提供轮廓地图和用于修改的Adobe Illustrator CC文件选项。

该地图属于公共领域，允许用户自由修改、复制，甚至出售。然而，作者汤姆·帕特森声明对任何错误不承担法律责任，并且不认可使用该地图者的任何观点。文章提供了打印技巧，建议使用照片缎面纸，并在确定完整尺寸版本之前进行测试打印。还邀请用户翻译该地图或提出改进建议。

此外，还有一个配套的等积地球自然地图，侧重于自然特征。每个地图版本都有多种语言版本可供选择。该地图的最后一次更新是在2025年8月2日，版本号为1.4。

---

## 45. 程序员们 (2016)

**原文标题**: Programming People (2016)

**原文链接**: [https://leftoversalad.com/c/015_programmingpeople/](https://leftoversalad.com/c/015_programmingpeople/)

《编程人员》(2016) 是一部漫画，大概可以作为海报购买。内容简约，提到“剩余的沙拉”，并特别鸣谢ScudsCorp、wycats 和 S. Sever。鉴于提及的名称，这暗示该漫画可能与软件或科技行业相关，或是讽刺该领域。“编程人员”这个标题可能暗示影响或控制人们的想法，也许是通过技术或代码，但需要具体的讯息和图像（我们没有）来确认这一点。“剩余的沙拉”的提及可能是漫画本身中的一种幽默或象征性元素，或许代表着被丢弃的、不完整的或价值较低的东西。

---

## 46. 优化我们的银河战士之旅

**原文标题**: Optimizing our way through Metroid

**原文链接**: [https://antithesis.com/blog/2025/metroid/](https://antithesis.com/blog/2025/metroid/)

Antithesis公司是一家专门测试复杂分布式系统的公司，他们利用《银河战士》等任天堂游戏来开发和完善其测试平台。他们意识到，现有的模糊测试和PBT技术不足以应对复杂的游戏挑战，因此他们创新了新的方法。

文章详细介绍了一个在《银河战士》中遇到的特定问题：自动系统卡在需要导弹才能打开的红门前，因为它把导弹都用在了敌人身上。简单地将“导弹数量”添加到状态空间表示中效率低下，而限制导弹的使用又过于局限。

Antithesis开发了一种新的优化算法，根据导弹数量来优先处理状态（“探索所有{x, y}元组，但在所有条件相同的情况下，优先选择导弹数量更多的状态。”）。然而，一个简单的实现被证明太慢了。

然后，他们设计了一种更复杂的算法，类似于测试用例缩减/最小化，该算法维护一个系统状态的连接图，并根据“优化”目标动态调整探索力度。这包括跟踪已知的最佳转换成本，并适应不断发现的捷径。这大大提高了效率，启用新的算法使他们能够解决《银河战士》中的导弹问题，并开始成功通关游戏。

优化后的探索导致了诸如刷生命值和导弹、发现密码破解、寻找漏洞进行序列跳跃，并最终通关游戏的行为。文章强调了这种优化技术对其他模糊测试挑战的广泛适用性，例如检测内存泄漏或性能异常。他们认为优化是有效模糊测试的核心能力。

---

## 47. 我最初的Palm IIIx

**原文标题**: My original Palm IIIx

**原文链接**: [https://www.goto10retro.com/p/taking-a-look-at-my-old-palm-iiix](https://www.goto10retro.com/p/taking-a-look-at-my-old-palm-iiix)

保罗·勒菲弗尔最近在清理时重新发现了他的初代Palm IIIx掌上电脑，这让他不禁怀旧地回顾起这款复古掌上电脑。他于1999年9月以大约300美元（相当于2025年的575美元）的价格购买了它。该设备使用AAA电池供电，被发现状况良好，配有原装翻盖和Graffiti贴纸。

勒菲弗尔回忆起使用Graffiti，Palm独特的单笔划字符输入法。他强调了Palm IIIx的规格：16MHz处理器，4MB内存和160x160像素分辨率的屏幕，并指出它在当时令人印象深刻的功能。

他承认，按照今天的标准，附带的应用程序存在局限性，他提到由于单色，非背光屏幕，使用待办事项应用程序的困难。他将其与他后来的Palm IIIc进行了对比，后者具有背光彩色屏幕和可充电电池。

勒菲弗尔感叹Palm IIIx缺乏连接性，这使其在现代几乎无用。它最初通过串行端口连接到PC进行数据同步，但他不再有必要的电缆。他考虑尝试连接它，但如果没有功能更强大的Palm，他表示怀疑。文章最后提供了有关Palm PDA的相关文章链接。

---

## 48. 德贝塔

**原文标题**: Debdelta

**原文链接**: [https://debdelta.debian.net/](https://debdelta.debian.net/)

Debdelta 是一套用于创建和应用 Debian 软件包之间增量（变更）的应用程序，类似于“diff”输出，从而实现高效的更新存储和传输。它包含 `debdelta-upgrade`，一个用于下载和使用这些增量来升级 Debian 软件包的工具。

该项目是开源的，可在 Salsa.debian.org 上获取，并以 GPL-v2 许可发布。 提供文档和常见问题解答以供使用。

一个关键组件是 debdelta-upgrade 服务，这是一个自动为 Debian 仓库升级生成增量，并删除过期增量的服务器。该服务器的日志和统计数据是公开可用的。配置通过 `/etc/debdelta/sources.conf` 管理，允许选择用于增量生成的发行版、架构和分区。目前（2024 年），该服务器为所有主要的 Debian 发行版（bookworm、bullseye、buster）及其各自的 backports、security 和 proposed-updates 频道生成增量，支持 all、i386 和 amd64 架构。

本文档还记录了服务新闻和历史问题，包括磁盘空间限制、软件错误和基础设施问题。 它提到了过去由 GCC、zlib1g 和 debmirror 的更改引起的问题，以及服务器从停电和磁盘故障中的恢复。 它强调了 delta 下载使用率高的实例。 最后，它感谢 Wingware 提供了开发中使用的 Python 代码编辑器。

---

## 49. 问责制无法解决的问题

**原文标题**: The problems that accountability can't fix

**原文链接**: [https://surfingcomplexity.blog/2025/08/23/the-problems-that-accountability-cant-fix/](https://surfingcomplexity.blog/2025/08/23/the-problems-that-accountability-cant-fix/)

Lorin Hochstein 认为，问责制虽然经常被吹捧为实现更好结果的解决方案，但不足以解决某些类型的问题，尤其是 OceanGate 潜水器内爆事件所暴露出的问题。

Hochstein 指出问责制失效的两类问题：**协调挑战**和**风险模型校准失误**。在大型组织中，自上而下的问责制通常会将个人归咎于源于系统不同部分之间复杂互动的问题。这种“替罪羊”模式未能解决潜在的协调问题。虽然技术项目经理 (TPM) 可以帮助协调工作，但仅靠问责制无法解决事件暴露出的协调问题。

OceanGate 事故是第二个问题的例证。尽管首席执行官兼驾驶员 Stockton Rush 承担最终责任（“自身利益攸关”），但这场灾难的发生是由于他错误的风险模型和缺乏专业知识。如果领导者对风险的理解存在缺陷，那么简单地追究领导者的责任是不够的。

此外，文章强调了**双重束缚**的概念，即个人在商业目标和安全之间面临相互冲突的激励。问责制通过施加压力让个人交付成果，从而加剧了这个问题，这可能会损害安全性。

Hochstein 提倡替代解决方案，例如协作交叉检查和独立的安全组织，这些解决方案利用不同的视角，并赋予那些没有双重束缚的人优先考虑安全的权力。他引用了 David Woods 在哥伦比亚号事故后的证词，强调 NASA 需要一个独立的安全组织，以应对因利益冲突而产生的风险。

---

## 50. Manim：用于解释性数学视频的动画引擎

**原文标题**: Manim: Animation engine for explanatory math videos

**原文链接**: [https://github.com/3b1b/manim](https://github.com/3b1b/manim)

Manim是由3Blue1Brown创建的基于Python的动画引擎，用于制作解释性的数学视频。它有两个版本：原始的ManimGL（本仓库）和侧重稳定性和社区贡献的社区版。

本文档专注于ManimGL。安装需要Python 3.7+、FFmpeg、OpenGL，以及可选的LaTeX。在Linux上，还需要Pango。推荐的安装方法是使用`pip install manimgl`。文档提供了Linux、Windows和macOS的特定安装说明，包括使用Anaconda的详细信息。

要使用Manim，可以运行例如`manimgl example_scenes.py OpeningManimExample`这样的示例。多个命令行标志可以控制渲染，例如`-w`（写入文件）、`-o`（写入并打开）、`-s`（跳到结尾）、`-n`（跳到动画）和`-f`（全屏）。自定义配置可以在`custom_config.yml`中设置。

文档可在3b1b.github.io/manim获得，中文版在docs.manim.org.cn。欢迎贡献，特别是对社区版的贡献。ManimGL采用MIT许可证。

---

## 51. 在球面上生成随机点的简单方法

**原文标题**: A simple way to generate random points on a sphere

**原文链接**: [https://www.johndcook.com/blog/2025/05/06/random-points-on-a-sphere/](https://www.johndcook.com/blog/2025/05/06/random-points-on-a-sphere/)

本文探讨了一种简单直观的在球面上生成均匀分布随机点的方法。该方法包括在立方体内生成随机点，拒绝落在立方体内切球外的点，然后将接受的点归一化，使其位于球面上。

作者强调了这种方法的几个优点：直观性、最小依赖性（仅需平方根函数）以及与生成独立正态随机变量并对其进行归一化的标准方法相比，具有合理的效率（尤其是在三维情况下）。虽然不是*最*高效的算法，但它在简单性和性能之间取得了良好的平衡。

本文还承认了这种“接受-拒绝”方法的一个主要缺点：其可变运行时间。虽然平均效率很好，但理论上存在无限拒绝的可能性，导致执行时间不一致。这种可变性在并行计算中（由于等待最慢的线程而减慢任务速度）和密码学中（可能通过时间攻击泄露信息）可能会成为问题。作者将其与保证恒定运行时间的算法进行了对比，后者可能在特定情况下更受欢迎。

---

## 52. 华丽地毯的难题

**原文标题**: The Fancy Rug Dilemma

**原文链接**: [https://epan.land/essays/2025-8_FancyRugDilemma](https://epan.land/essays/2025-8_FancyRugDilemma)

好的，基于标题“精美地毯的困境”和提供的内容“正在加载内容...”，我只能提供推测性的总结。由于内容不可用，我将假设该文章讨论了拥有和维护精美地毯相关的常见问题或挑战。

以下是一个可能的总结：

“精美地毯的困境”可能探讨了拥有高端装饰地毯的利弊。它可能深入探讨了精美地毯能给家庭带来的美学吸引力和奢华感，同时也强调了维护它们所涉及的实际困难。

文章可能会讨论高昂的购买和专业清洁费用、地毯容易沾染污渍和损坏（尤其是在人流量大的区域或有宠物和孩子的家庭中），以及去除污渍和修复的复杂性。它还可能涉及由于阳光照射而导致颜色褪色的可能性，以及需要特殊的衬垫来保护地毯和下面的地板。

此外，文章还可以为特定生活方式和家庭环境选择合适的精美地毯类型提供建议，建议选择更耐用或更易于清洁的材料。它还可能提供预防性护理的技巧，例如定期吸尘、及时处理污渍和专业清洁计划，以帮助所有者保持其昂贵投资的美丽和寿命。最终，文章可能旨在帮助读者权衡拥有精美地毯的好处与维护它所需的投入。

---

## 53. DeepWiki: 理解任何代码库

**原文标题**: DeepWiki: Understand Any Codebase

**原文链接**: [https://www.aitidbits.ai/p/deepwiki](https://www.aitidbits.ai/p/deepwiki)

本文介绍了DeepWiki，这是由Cognition（AI软件工程师Devin背后的团队）开发的工具，它可以将任何GitHub存储库转换为可即时导航的wiki。作者Sahar Mor描述了他们如何使用DeepWiki快速理解代码库、设置开发环境以及为Claude和Cursor等编码代理生成上下文。

DeepWiki允许用户在无需手动搜索文件的情况下提出关于存储库的问题。它提供“快速”和“深度研究”模式，提供以行级引用为基础的答案。可以通过网络访问它，也可以通过DeepWiki MCP服务器集成到AI IDE中。

Mor概述了八种具体的用例：评估开源项目、快速设置新环境、借鉴实现细节、创建自定义入门指南、发现首次贡献、导航菜谱式存储库、构建上下文感知的编码代理以及审查pull请求。

DeepWiki可以快速理解代码库结构、架构和编码风格，有助于快速审查和了解pull请求中的代码更改。Sahar分享了他们构建的名为“Sidekick”的工具，该工具可以从存储库自动生成markdown摘要，然后由编码代理利用这些摘要在生成过程中提供上下文。

作者希望DeepWiki中有一个会话式的助手模式和一个基于任务的入门功能，以指导用户完成特定的贡献。他们鼓励读者在deepwiki.com上尝试DeepWiki。

---

## 54. Rust 中的人体工学缺陷：快速编写、轻松调试、精确处理

**原文标题**: Ergonomic errors in Rust: write fast, debug with ease, handle precisely

**原文链接**: [https://gmcgoldr.github.io/2025/08/21/stackerror.html](https://gmcgoldr.github.io/2025/08/21/stackerror.html)

本文介绍 `stackerror`，一个旨在提升 Rust 编写、调试和运行时错误处理人体工程学的库。它解决了现有错误处理方法（如简单的静态字符串、`anyhow` 和 `thiserror`）的局限性，这些方法通常会优先考虑某些上下文而不是其他上下文，或者混淆调试和运行时需求。

`stackerror` 的目标是实现一种平衡的方法：像 `anyhow` 一样快速开发，像 `thiserror` 一样精确的运行时匹配，以及丰富的调试上下文。它允许开发人员在失败点轻松地向错误添加人类可读的消息，从而创建用于调试的上下文堆栈。对于运行时处理，它使用结构化的错误代码（类似于 `std::io::ErrorKind` 或 HTTP 状态代码）来做出控制流决策，而无需进行向下转换或暴露内部错误细节。

该库通过使用 `StackResult<T>` 和辅助方法直接在可能失败的调用中启用错误包装，从而促进编写简洁的代码。堆叠的错误消息可精确定位故障位置，从而简化调试。运行时处理依赖于匹配用于可恢复错误的错误代码，从而支持重试等操作。

本文通过一个涉及 IO、HTTP 和重试的实际示例演示了 `stackerror`。它还展示了如何通过包装 `StackError` 来创建自定义错误类型（例如 `LibError`），从而使库能够公开单个不透明的错误类型，同时保留基于代码的运行时处理和堆叠的调试信息的优势。作者认为，这种分离可以保持运行时逻辑的稳定，并避免与 crate 内部结构紧密耦合。

---

## 55. Librebox：一款开源的、兼容Roblox的游戏引擎

**原文标题**: Librebox: An open source, Roblox-compatible game engine

**原文链接**: [https://github.com/librebox-devs/librebox-demo](https://github.com/librebox-devs/librebox-demo)

Librebox是一个开源、Luau驱动的游戏引擎，旨在兼容流行的沙盒游戏API。它允许开发者完全控制他们的游戏和平台，使用熟悉的Luau代码，只需进行最少的修改。

该项目目前处于演示阶段，实现了基本场景渲染、光照、阴影、部件、相机移动和标准数据类型。它支持客户端服务，如Workspace、RunService和Lighting。Luau脚本支持强大，具有强大的任务调度器、协程并启用了优化。

未来的计划包括添加UserInputService、StarterPlayer、物理、网格支持和GUI元素，以实现完全的客户端兼容性。长期目标包括服务器的复制支持、Librebox编辑器，以及开发者实现自定义货币化策略的能力。Librebox旨在提供一个与平台无关的环境，允许开发者使用自己的API或修改源代码。

该引擎目前支持Windows，使用Raylib作为其主要依赖项。开发者可以下载版本并使用批处理脚本来构建依赖项和引擎。命令行参数允许自定义玩家。Librebox是一个独立的、无版权项目，使用Luau和Raylib，并且不隶属于任何商业平台。

---

## 56. 对益生菌大肠杆菌的研究见解 (2016)

**原文标题**: Insights from research with probiotic E. coli (2016)

**原文链接**: [https://pmc.ncbi.nlm.nih.gov/articles/PMC5063008/](https://pmc.ncbi.nlm.nih.gov/articles/PMC5063008/)

《欧洲微生物学与免疫学杂志》2016年发表的这篇文章回顾了一个世纪以来对益生菌大肠杆菌菌株的研究，重点关注其在人类健康中的应用。文章着重介绍了研究最多的益生菌大肠杆菌Nissle 1917 (EcN)，并将其与市面上其他商业化的大肠杆菌益生菌：Symbioflor 2和Colinfant进行了比较。

作者Trudy M. Wassenaar进行了文献检索，总结了这三种产品的研究结果。该综述讨论了它们的特性、遗传内容以及与致病菌株的相似性，特别是那些引起尿路感染的菌株。EcN (Mutaflor) 的文献资料最为丰富，而 Symbioflor 2 和 Colinfant 的相关资料相对较少。

主要发现包括：与Symbioflor 2相比，Mutaflor的推荐日剂量较高；EcN具有运动能力，而Symbioflor 2则不具备。基因分析表明，EcN的近亲是尿路致病性大肠杆菌，而Symbioflor 2的近亲是共生菌株。

该综述表明，益生菌大肠杆菌的未来在于治疗胃肠道感染，特别是那些由耐药病原体引起的感染，这与Alfred Nissle最初的发现相呼应。此外，该综述还强调了关于大肠杆菌在健康人体肠道中定植的定量数据有限。

---

## 57. 面向机密虚拟机重新思考Linux云堆栈

**原文标题**: Rethinking the Linux cloud stack for confidential VMs

**原文链接**: [https://lwn.net/Articles/1030818/](https://lwn.net/Articles/1030818/)

LWN.net文章：Linux云栈中运行机密虚拟机的挑战与解决方案

---

## 58. 探索EXIF (2023)

**原文标题**: Exploring EXIF (2023)

**原文链接**: [https://hturan.com/writing/exploring-exif](https://hturan.com/writing/exploring-exif)

本文深入分析了2023年8月13日13:07:57使用iPhone 12 Pro拍摄的图像的EXIF数据。EXIF数据揭示了关于图像和用于拍摄它的设备的广泛信息。

**图像特征：** 图像分辨率为960x1280，处理后的尺寸为4032x3024。它使用YCbCr4:2:0子采样，表明侧重于压缩。曝光时间为1/856秒，光圈为f/2，ISO为25。焦距为6mm（相当于35mm相机上的52mm）。

**设备和相机详细信息：** 该图像是用Apple iPhone 12 Pro拍摄的，利用其后置三摄6mm f/2镜头。软件版本为16.6。EXIF数据包括镜头规格的具体细节和包含原始专有信息的制造商注释。

**位置数据 (GPS)：** 该图像包含指示照片位置的GPS坐标：北纬51.11505833333334，东经0.5824055555555555，海拔58.61米。GPS速度为0公里/小时。

**颜色配置文件：** 图像使用Apple Wide Color Sharing Profile，渲染意图为感知型，创建日期为2016-01-01。

简而言之，EXIF数据描绘了图像的全面图景，包括技术设置、设备规格、位置和颜色配置文件，提供了对捕获过程和iPhone 12 Pro相机功能的宝贵见解。

---

## 59. AGI 是一个工程问题，不是一个模型训练问题。

**原文标题**: AGI is an engineering problem, not a model training problem

**原文链接**: [https://www.vincirufus.com/posts/agi-is-engineering-problem/](https://www.vincirufus.com/posts/agi-is-engineering-problem/)

实现通用人工智能（AGI）主要是一个工程挑战，而非模型训练问题。文章认为，当前大型语言模型（LLMs）如GPT-5、Claude和Gemini，尽管规模不断扩大，性能却已达到瓶颈，表明单纯扩大规模的回报正在递减。

作者提出，应将重点转移到构建由互连的、专门组件组成的工程系统上，以此模仿人脑的架构。关键组件包括：

*   **上下文管理：** 通过实时检索、过滤和更新信息来维护长期连贯上下文的系统。
*   **内存即服务：** 能够进化、整合信息并适应新证据的内存系统。
*   **确定性工作流程：** 在严格、可预测的结构中结合概率组件的框架，提供回滚和验证功能。
*   **专业模型：** 使用针对特定领域优化并协调工作以协同配合的专业模型生态系统。

作者强调需要容错管道、监控系统和强大的测试框架，类似于分布式系统工程。他们提出了一个分阶段的路线图：基础层（上下文、内存、工作流程）、能力层（专业模型、推理引擎、规划）以及AGI从这些组件交互中产生的涌现层。文章总结道，构建能够进行跨领域推理的可靠的、工程化的AI系统对于实现AGI至关重要，这使得系统工程比进一步的模型扩展更为重要。

---

## 60. 休闲式过度设计我的位置记录

**原文标题**: Recreationally overengineering my location history

**原文链接**: [https://overengineer.dev/blog/2025/08/19/overengineering-location-history/](https://overengineer.dev/blog/2025/08/19/overengineering-location-history/)

这篇博文详细介绍了作者出于对谷歌地图隐私问题的担忧，而“娱乐性过度设计”的自制位置历史追踪系统项目。该项目包含一个用于收集位置数据的iOS应用和一个用于存储和可视化的Rust后端。

该后端使用作者自定义的Rust“webservice-chonk”模板构建，该模板包含axum、sqlx、minijinja等，用于以性能和稳定性著称的“生产级”应用程序。数据存储在PostgreSQL中，并使用PostGIS实现高效的地理数据处理。

iOS应用使用“重要位置变化”API以最大限度地减少电池消耗，还包含一个用于实时位置共享的“高分辨率更新”模式。实时位置共享通过包含具有有限生命周期的生成令牌的简单链接实现。

位置历史记录在Mapbox底图上使用PostGIS查询生成的六边形网格进行可视化。网格单元格根据用户是否去过该位置进行着色。EPSG:4326和EPSG:3857之间的坐标投影变换在数据库中使用PostGIS处理。

实时位置共享使用WebSockets，但作者注意到axum中的默认读取缓冲区大小并对其进行了调整。实时位置功能的客户端错误处理通过简单的页面重新加载来实现。该项目运行良好，内存效率高，作者对结果感到满意。

---

## 61. Romhack.ing 的互联网档案馆镜像不再可用

**原文标题**: Romhack.ing's Internet Archive Mirror No Longer Available

**原文链接**: [https://romhack.ing/database/news/entry/DW8BKnRHSEqaGDwXTiKjMw](https://romhack.ing/database/news/entry/DW8BKnRHSEqaGDwXTiKjMw)

Romhack.ing网站在互联网档案馆的镜像已无法通过其JavaScript应用访问。提供的文字表明存在技术问题，阻止用户访问内容。建议用户尝试仅HTML版本的应用，点击提供的链接即可。该消息还指出，由于激进的缓存设置，某些较旧或配置错误的浏览器可能甚至无法访问HTML版本。在这种情况下，建议用户禁用激进缓存，手动多次刷新页面，并可能联系其浏览器开发人员寻求帮助。本质上，JavaScript版本已损坏，并且由于浏览器相关问题，替代方案（HTML版本）可能不适用于所有人。

---

## 62. 黑客与物理学家——一个关于“常识”的故事

**原文标题**: Hacker and physicist – a tale of "common sense"

**原文链接**: [https://www.supasaf.com/blog/general/hacker_physicist](https://www.supasaf.com/blog/general/hacker_physicist)

泰德，一位拥有物理和信息安全背景的“石器时代”程序员，反思了基本安全原则与它们在现代企业，尤其是在中国市场中的实际应用之间的脱节。他用诸如“伟大的证书之谜”之类的轶事来阐释开发者和项目经理常常误解或忽视基本安全概念。

他强调了“抽象陷阱”——现代软件工程对抽象层的依赖，使得开发者能够在不理解底层原理的情况下构建复杂的应用程序，从而导致漏洞。他用GPS卫星需要相对论修正的例子来强调，即使使用者不理解物理学，系统也只有在工程师理解的情况下才能正常工作。同样，安全依赖于理解基本原则，即使开发者“仅仅是移动业务逻辑”。

泰德为安全专业人员（成为赋能者，而非守门员）、开发者和TPM（保持好奇心，理解原理）以及领导者（投资教育，建立安全文化）提出了切实可行的解决方案。他倡导欣赏那些使互联世界成为可能的“数字明星”，并强调理解这些基本原理会带来更安全、更优雅的解决方案，类似于一个精心设计的LISP函数。最终，他主张转变观念，将安全视为一种基本力量，就像物理学一样，支配着数字宇宙，而非仅仅作为一个检查项。

---

## 63. 盖斯勒管之子 (2023)

**原文标题**: Children of the Geissler Tube (2023)

**原文链接**: [https://www.hopefulmons.com/p/children-of-the-geissler-tube](https://www.hopefulmons.com/p/children-of-the-geissler-tube)

本文重点阐述了盖斯勒管令人惊讶的影响。盖斯勒管是玻璃吹制工海因里希·盖斯勒于1854年看似简单的一项发明，文章认为它是经常被忽视的关键技术先驱。 盖斯勒管是一种气体放电管，通过允许科学家在低压气体中进行电流实验，为众多创新铺平了道路，从而发现了阴极射线（电子）和X射线。

尽管最初作为一种新奇事物而流行，但其影响力迅速扩大。本文追溯了盖斯勒管与荧光灯、霓虹灯以及其他专用灯具的渊源。 至关重要的是，改进后的版本（如克鲁克斯管）促进了电子和X射线的发现，这是物理学领域的根本性突破。

盖斯勒管最重要的影响在于其作为阴极射线管（CRT）的前身，它彻底改变了示波器、雷达以及最终电视中的显示技术。盖斯勒管的进一步发展促成了二极管和三极管（真空管）的发明，而这两种元件是早期无线电接收器和计算机中的关键部件。 尽管晶体管最终取代了真空管，但本文认为盖斯勒管在电子和计算机发展中的作用是不可否认的，从某种意义上说，我们都是“盖斯勒管之子”。

---

## 64. 开发者瓶颈

**原文标题**: Developer's block

**原文链接**: [https://underlap.org/developers-block/](https://underlap.org/developers-block/)

开发者障碍：本文探讨了软件开发中与写作障碍类似的情况，分析了其原因并提供了解决方案。作者描述了两种主要场景：一是因一开始就追求完美而导致新项目启动受阻；二是因初来乍到而不知所措或因倦怠而导致现有项目失去进展。

对诸如广泛测试、全面文档、特定编码风格和强大错误处理等最佳实践的追求固然有价值，但可能会变得让人不堪重负并导致停滞不前，尤其是在新项目开始时。同样，不熟悉大型现有代码库、其语言或约定也会阻碍进展。过度工作和缺乏动力也可能导致陷入困境。

为了克服这些障碍，作者建议花时间逐步学习代码库，不要害怕提问，并专注于小型、可管理的任务。他们建议逐步工作，从最小的原型开始以获得进展，并推迟非必要的最佳实践。文章强调了识别精神疲劳、休息以及尽早发布以获得动力和用户反馈的重要性。最后，它建议避免过早优化和因依赖问题而分心，建议首先关注核心功能。作者鼓励读者分享他们自己克服开发者障碍的技巧。

---

## 65. RFC 9839 与错误的 Unicode

**原文标题**: RFC 9839 and Bad Unicode

**原文链接**: [https://www.tbray.org/ongoing/When/202x/2025/08/14/RFC9839](https://www.tbray.org/ongoing/When/202x/2025/08/14/RFC9839)

Tim Bray 的文章讨论了 RFC 9839，该标准旨在解决数据结构和协议的文本字段中“不良 Unicode”字符的问题。虽然 Unicode 通常很好，但并非所有字符都适合交换。RFC 9839 识别了有问题的字符（如控制码、未配对的代理项和非字符），并提出了三个不太糟糕的子集来排除它们。

该文章强调了这些字符如何在各种编程语言和数据格式（如 JSON、CBOR 和 XML）中引起问题。例如，它使用了一个包含有问题的 Unicode 代码点的 JSON 用户名字段示例，这些代码点可能导致意外行为。

Bray 将 RFC 9839 与更全面但更复杂的 RFC 8264 (PRECIS) 进行了对比，认为 9839 更简单且更易于开发人员采用，即使它的功能较少。他提供了一个 Go 语言库，用于根据提议的子集验证文本字段。

一张表格总结了各种数据格式和 RFC 9839 的子集排除了哪些有问题的字符类。文章最后对贡献者表示感谢，并反思了创建个人提交 RFC 的挑战性过程，建议通常利用工作组是更好的方法。

---

## 66. 非洲正大量购买创纪录数量的中国太阳能板

**原文标题**: Africa Is Buying a Record Number of Chinese Solar Panels

**原文链接**: [https://www.wired.com/story/african-imports-of-chinese-solar-panels-increase/](https://www.wired.com/story/african-imports-of-chinese-solar-panels-increase/)

非洲国家从中国进口的廉价太阳能板数量创历史新高，这是由于它们希望利用可再生能源满足能源需求并避免昂贵的化石燃料。2025年5月，进口量达到创纪录的1.57吉瓦，主要来自较小国家，而不仅仅是富裕国家。阿尔及利亚在2025年上半年的进口量大幅增长了6300%。一些欠发达国家，如乍得，进口的太阳能板足以潜在地取代其全部发电能力。

中国在太阳能板制造领域占据主导地位，占全球80%以上，再加上低廉的价格，使得太阳能成为能源匮乏的非洲国家具有成本效益的选择。这与巴基斯坦和南非的趋势相似，在这些国家，廉价的中国太阳能板改变了能源格局。

需求的驱动力既来自北非的大型公用事业电站，也来自撒哈拉以南非洲的分布式屋顶系统，从而改善了农村社区的能源获取，而无需依赖政府支出。

虽然像美国这样的一些国家对中国产太阳能板征收关税，但非洲国家普遍欢迎它们。关于促进当地制造业的讨论日益增多，但目前的重点是利用中国太阳能板的经济性来快速解决能源短缺问题。总体而言，预计对中国进口的依赖将继续存在。

---

## 67. Gutenprint停止支持macOS

**原文标题**: Gutenprint Discontinues macOS Support

**原文链接**: [https://gimp-print.sourceforge.io/p_FAQ_OS_X.php](https://gimp-print.sourceforge.io/p_FAQ_OS_X.php)

本文档是关于macOS和Darwin操作系统上Gutenprint打印机驱动软件的常见问题解答。

**macOS支持终止：** 自2024年7月7日起，Gutenprint项目已停止对macOS的支持，原因是缺乏积极的维护者以及支持较新macOS版本的技术挑战。将不再生成未来的macOS二进制文件。现有的二进制文件可能仍然可以在旧版本的macOS上运行（<= 10.14）。

**什么是Gutenprint？** Gutenprint是一套高质量的打印机驱动程序，适用于包括macOS在内的各种操作系统，其质量和功能通常超过OEM驱动程序。它通过先进的筛选算法、色彩生成和打印机功能利用，专注于高质量的输出。

**常见问题解答中解决的关键问题和解决方案：**

*   Mac OS X Panther (10.3.x) 上Quark和Photoshop等应用程序EPS文件的打印问题及解决方法。
*   Mac OS X Panther (10.3.x) 上的安装程序问题及解决方法。
*   Gutenprint PPD（打印机驱动程序）的位置及其在CUPS Web界面中的可用性。
*   如何在打印中心访问“高级”选项。
*   来自“Carbon”应用程序（Adobe Photoshop、Acrobat、Appleworks等）的打印问题。
*   解释Mac OS X Jaguar中CUPS、Gutenprint和Ghostscript的交互。
*   一个专注于热升华打印机的部分，以解决打印问题。
*   USB/网络连接和驱动程序设置的解决方案。
*   更改打印设置（如纸张类型和分辨率）的说明。
*   排除一般打印问题（空白页、颜色不正确、纸张进纸等）的指南。
*   特定HP Deskjet型号的问题。

常见问题解答还提供有关Gutenprint的一般信息、其功能、如何查找更多信息以及如何联系开发人员。

---

## 68. The Cornervery: A 90-Degree Stapler

**原文标题**: The Cornervery: A 90-Degree Stapler

**原文链接**: [https://www.core77.com/posts/138232/The-Cornervery-A-90-Degree-Stapler](https://www.core77.com/posts/138232/The-Cornervery-A-90-Degree-Stapler)

生成摘要时出错

---

## 69. Reproducing prospect theory with 'differentiable decision theories'

**原文标题**: Reproducing prospect theory with 'differentiable decision theories'

**原文链接**: [https://www.science.org/doi/full/10.1126/science.abe2629](https://www.science.org/doi/full/10.1126/science.abe2629)

生成摘要时出错

---

## 70. US Supreme Court allows NIH to cut $2B in research grants

**原文标题**: US Supreme Court allows NIH to cut $2B in research grants

**原文链接**: [https://www.nature.com/articles/d41586-025-02721-5](https://www.nature.com/articles/d41586-025-02721-5)

生成摘要时出错

---

## 71. Lightning declines over shipping lanes following regulation of sulfur emissions

**原文标题**: Lightning declines over shipping lanes following regulation of sulfur emissions

**原文链接**: [https://theconversation.com/the-world-regulated-sulfur-in-ship-fuels-and-the-lightning-stopped-249445](https://theconversation.com/the-world-regulated-sulfur-in-ship-fuels-and-the-lightning-stopped-249445)

生成摘要时出错

---

## 72. China, Russia, and U.S. Race to Develop Lunar Nuclear Reactors

**原文标题**: China, Russia, and U.S. Race to Develop Lunar Nuclear Reactors

**原文链接**: [https://spectrum.ieee.org/lunar-nuclear-reactor-nasa-moon](https://spectrum.ieee.org/lunar-nuclear-reactor-nasa-moon)

生成摘要时出错

---

## 73. Materialized views are obviously useful

**原文标题**: Materialized views are obviously useful

**原文链接**: [https://sophiebits.com/2025/08/22/materialized-views-are-obviously-useful](https://sophiebits.com/2025/08/22/materialized-views-are-obviously-useful)

生成摘要时出错

---

## 74. Converting an online game to work without any JavaScript

**原文标题**: Converting an online game to work without any JavaScript

**原文链接**: [https://bejofo.com/blog/no-js-game-case-study](https://bejofo.com/blog/no-js-game-case-study)

生成摘要时出错

---

## 75. Marshal madness: A brief history of Ruby deserialization exploits

**原文标题**: Marshal madness: A brief history of Ruby deserialization exploits

**原文链接**: [https://blog.trailofbits.com/2025/08/20/marshal-madness-a-brief-history-of-ruby-deserialization-exploits/](https://blog.trailofbits.com/2025/08/20/marshal-madness-a-brief-history-of-ruby-deserialization-exploits/)

生成摘要时出错

---

## 76. Libre – An anonymous social experiment without likes, followers, or ads

**原文标题**: Libre – An anonymous social experiment without likes, followers, or ads

**原文链接**: [https://libreantisocial.com](https://libreantisocial.com)

生成摘要时出错

---

## 77. Good EU regulations

**原文标题**: Good EU regulations

**原文链接**: [https://www.actuallygoodregulations.eu/](https://www.actuallygoodregulations.eu/)

生成摘要时出错

---

## 78. Optimizing FizzBuzz in Rust

**原文标题**: Optimizing FizzBuzz in Rust

**原文链接**: [https://github.com/nrposner/fizzcrate](https://github.com/nrposner/fizzcrate)

生成摘要时出错

---

## 79. Mob Programming

**原文标题**: Mob Programming

**原文链接**: [https://mobprogramming.org/](https://mobprogramming.org/)

生成摘要时出错

---

## 80. David Klein's TWA Posters (2018)

**原文标题**: David Klein's TWA Posters (2018)

**原文链接**: [https://flashbak.com/david-kleins-magnificent-twa-posters-404428/](https://flashbak.com/david-kleins-magnificent-twa-posters-404428/)

生成摘要时出错

---

## 81. YouTube used AI to edit videos without telling users

**原文标题**: YouTube used AI to edit videos without telling users

**原文链接**: [https://www.bbc.com/future/article/20250822-youtube-is-using-ai-to-edit-videos-without-permission](https://www.bbc.com/future/article/20250822-youtube-is-using-ai-to-edit-videos-without-permission)

生成摘要时出错

---

## 82. Monoid-Augmented FIFOs, Deamortised

**原文标题**: Monoid-Augmented FIFOs, Deamortised

**原文链接**: [https://pvk.ca/Blog/2025/08/19/monoid-augmented-fifos/](https://pvk.ca/Blog/2025/08/19/monoid-augmented-fifos/)

生成摘要时出错

---

## 83. Stepanov's biggest blunder? The curious case of adjacent difference

**原文标题**: Stepanov's biggest blunder? The curious case of adjacent difference

**原文链接**: [https://mmapped.blog/posts/43-stepanovs-biggest-blunder](https://mmapped.blog/posts/43-stepanovs-biggest-blunder)

生成摘要时出错

---

## 84. It’s not wrong that "\u{1F926}\u{1F3FC}\u200D\u2642\uFE0F".length == 7 (2019)

**原文标题**: It’s not wrong that "\u{1F926}\u{1F3FC}\u200D\u2642\uFE0F".length == 7 (2019)

**原文链接**: [https://hsivonen.fi/string-length/](https://hsivonen.fi/string-length/)

生成摘要时出错

---

## 85. Adventures in State Space [video]

**原文标题**: Adventures in State Space [video]

**原文链接**: [https://www.youtube.com/watch?v=YGLNyHd2w10](https://www.youtube.com/watch?v=YGLNyHd2w10)

生成摘要时出错

---

## 86. Writing Speed-of-Light Flash Attention for 5090 in CUDA C++

**原文标题**: Writing Speed-of-Light Flash Attention for 5090 in CUDA C++

**原文链接**: [https://gau-nernst.github.io/fa-5090/](https://gau-nernst.github.io/fa-5090/)

生成摘要时出错

---

## 87. Building Ultra Cheap Energy Storage for Solar PV

**原文标题**: Building Ultra Cheap Energy Storage for Solar PV

**原文链接**: [https://austinvernon.substack.com/p/building-ultra-cheap-energy-storage](https://austinvernon.substack.com/p/building-ultra-cheap-energy-storage)

生成摘要时出错

---

## 88. The theory and practice of selling the Aga cooker (1935) [pdf]

**原文标题**: The theory and practice of selling the Aga cooker (1935) [pdf]

**原文链接**: [https://comeadwithus.wordpress.com/wp-content/uploads/2012/08/the-theory-and-practice-of-selling-the-aga-cooker.pdf](https://comeadwithus.wordpress.com/wp-content/uploads/2012/08/the-theory-and-practice-of-selling-the-aga-cooker.pdf)

生成摘要时出错

---

## 89. I made a floppy disk from scratch

**原文标题**: I made a floppy disk from scratch

**原文链接**: [https://kottke.org/25/08/i-made-a-floppy-disk-from-scratch](https://kottke.org/25/08/i-made-a-floppy-disk-from-scratch)

生成摘要时出错

---

## 90. 450× Faster Joins with Index Condition Pushdown

**原文标题**: 450× Faster Joins with Index Condition Pushdown

**原文链接**: [https://readyset.io/blog/optimizing-straddled-joins-in-readyset-from-hash-joins-to-index-condition-pushdown](https://readyset.io/blog/optimizing-straddled-joins-in-readyset-from-hash-joins-to-index-condition-pushdown)

生成摘要时出错

---

## 91. Naming Things: The Most Underrated Skill in Software Development

**原文标题**: Naming Things: The Most Underrated Skill in Software Development

**原文链接**: [https://andreacanton.dev/posts/2025-08-23-naming-things/](https://andreacanton.dev/posts/2025-08-23-naming-things/)

生成摘要时出错

---

## 92. The issue of anti-cheat on Linux (2024)

**原文标题**: The issue of anti-cheat on Linux (2024)

**原文链接**: [https://tulach.cc/the-issue-of-anti-cheat-on-linux/](https://tulach.cc/the-issue-of-anti-cheat-on-linux/)

生成摘要时出错

---

## 93. Coinbase Mandates In-Person Orientation to Stop North Korean Hackers

**原文标题**: Coinbase Mandates In-Person Orientation to Stop North Korean Hackers

**原文链接**: [https://www.businessinsider.com/coinbase-north-korea-threats-remote-work-2025-8](https://www.businessinsider.com/coinbase-north-korea-threats-remote-work-2025-8)

生成摘要时出错

---

## 94. Spending too much time at airports

**原文标题**: Spending too much time at airports

**原文链接**: [https://thezvi.substack.com/p/spending-too-much-time-at-airports](https://thezvi.substack.com/p/spending-too-much-time-at-airports)

生成摘要时出错

---

## 95. Leaving Gmail for Mailbox.org

**原文标题**: Leaving Gmail for Mailbox.org

**原文链接**: [https://giuliomagnifico.blog/post/2025-08-18-leaving-gmail/](https://giuliomagnifico.blog/post/2025-08-18-leaving-gmail/)

生成摘要时出错

---

## 96. The Amiga games and demo scene collection

**原文标题**: The Amiga games and demo scene collection

**原文链接**: [https://amiga.vision/](https://amiga.vision/)

生成摘要时出错

---

## 97. Grok 2.5 is now open source. Grok 3 will be open source in about 6 months

**原文标题**: Grok 2.5 is now open source. Grok 3 will be open source in about 6 months

**原文链接**: [https://twitter.com/elonmusk/status/1959379349322313920](https://twitter.com/elonmusk/status/1959379349322313920)

生成摘要时出错

---

## 98. WebR – R in the Browser

**原文标题**: WebR – R in the Browser

**原文链接**: [https://docs.r-wasm.org/webr/latest/](https://docs.r-wasm.org/webr/latest/)

生成摘要时出错

---

## 99. How Not to Buy a SSD

**原文标题**: How Not to Buy a SSD

**原文链接**: [https://andrei.xyz/post/how-not-to-buy-a-ssd/](https://andrei.xyz/post/how-not-to-buy-a-ssd/)

生成摘要时出错

---

## 100. Io_uring, kTLS and Rust for zero syscall HTTPS server

**原文标题**: Io_uring, kTLS and Rust for zero syscall HTTPS server

**原文链接**: [https://blog.habets.se/2025/04/io-uring-ktls-and-rust-for-zero-syscall-https-server.html](https://blog.habets.se/2025/04/io-uring-ktls-and-rust-for-zero-syscall-https-server.html)

生成摘要时出错

---

