# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-08-24.md)

*最后自动更新时间: 2025-08-24 17:45:18*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 2 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 3 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 4 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 5 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 6 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 7 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 8 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 9 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 10 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 11 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 12 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 13 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 14 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 15 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 16 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 17 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 18 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 19 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 20 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 21 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 22 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 23 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 24 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 25 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 26 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 27 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 28 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 29 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 30 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 31 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 32 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 33 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 34 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 35 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 36 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 37 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 38 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 39 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 40 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 41 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 42 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 43 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 44 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 45 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 46 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 47 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 48 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 49 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 50 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 51 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 52 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 53 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 54 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 55 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 56 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 57 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 58 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 59 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 60 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 61 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 62 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 63 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 64 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 65 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 66 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 67 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 68 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 69 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 70 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 71 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 72 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 73 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 74 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 75 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 76 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 77 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 78 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 79 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 80 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 81 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 82 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 83 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 84 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 85 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 86 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 87 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 88 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 89 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 90 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 91 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 92 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 93 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 94 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 95 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 96 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 97 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 98 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 99 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 100 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 101 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 102 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 103 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 104 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 105 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 106 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 107 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 108 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 109 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 110 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 111 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 112 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 113 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 114 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 115 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 116 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 117 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 118 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 119 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 120 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 121 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 122 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 123 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 124 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 125 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 126 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 127 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 128 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 129 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 130 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 131 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 132 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 133 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 134 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 135 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 136 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 137 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 138 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 139 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 140 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 141 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 142 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 143 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 144 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 145 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 146 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 147 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 148 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 149 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 150 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 151 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 152 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 153 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 154 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 155 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 156 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 157 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 158 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
