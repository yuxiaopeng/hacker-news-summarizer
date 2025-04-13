# Hacker News 热门文章摘要 (2025-04-13)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 姆明一族的阴暗面

**原文标题**: The Dark Side of the Moomins

**原文链接**: [https://www.newstatesman.com/culture/books/2025/04/dark-side-of-the-moomins-tove-jansson](https://www.newstatesman.com/culture/books/2025/04/dark-side-of-the-moomins-tove-jansson)

本文深入探讨了托芙·杨松备受欢迎的姆明角色背后复杂而往往阴暗的现实，揭示了异想天开、商业上成功的姆明形象与杨松最初更深刻的意图之间鲜明的对比。《姆明与大洪水》是第一部姆明书籍，创作于冬季战争期间，反映了流离失所和生存的主题。

本文强调了杨松作为一名半瑞典、半芬兰艺术家和拥有多元关系的“边界居民”身份，这影响了她的角色的焦虑和对家的追寻。虽然早期的姆明故事提供了安慰和快乐的结局，但后来的书籍，如《姆明谷的仲冬》和《姆明爸爸出海记》，则探讨了抑郁、家庭破裂和存在主义焦虑的主题。

本文揭露了杨松在姆明现象商业化方面所面临的挑战，她对此感到不堪重负。杨松与她的角色，特别是姆明，进行着抗争，甚至讽刺了她苛刻的粉丝。最终，她试图通过结束漫画连载并在一个偏远的岛屿上与她的伴侣避难来与姆明保持距离。本质上，本文揭示了编织到姆明宇宙中的隐藏深度和个人斗争，展示了杨松如何将她的角色作为她自己复杂个性的画布。

---

## 2. Skywork-OR1：全新SOTA 320亿参数开源思维模型

**原文标题**: Skywork-OR1: new SOTA 32B thinking model with open weight

**原文链接**: [https://github.com/SkyworkAI/Skywork-OR1](https://github.com/SkyworkAI/Skywork-OR1)

Skywork AI 发布了 Skywork-OR1（Open Reasoner 1）系列，这是一系列专注于数学和代码推理的最新开源权重模型。该系列包括 Skywork-OR1-Math-7B、Skywork-OR1-32B-Preview 和 Skywork-OR1-7B-Preview，均提供开源权重。这些模型使用强化学习和精心设计的数据集进行训练。

Skywork-OR1-Math-7B 专为数学推理而设计，在 AIME24 和 AIME25 上取得了令人印象深刻的分数。Skywork-OR1-32B-Preview 在数学和编码任务上的表现与更大的 Deepseek-R1 相媲美，而 Skywork-OR1-7B-Preview 的表现优于其他同等规模的模型。

文章引入了 Avg@K 作为一种新的评估指标，用于衡量 K 次独立尝试的平均性能，以提供更可靠的评估。文章包含了在 AIME24、AIME25 和 LiveCodeBench 上的评估结果，展示了这些模型相对于竞争对手的强大性能。

文章提供了使用 Docker 和 Conda 环境安装和评估模型的说明。训练脚本即将发布。技术报告也在计划中。这些模型基于 DeepSeek-R1-Distill-Qwen-7B 和 DeepSeek-R1-Distill-Qwen-32B，并使用 verl 项目的自定义分支。文章提供了 Skywork-OR1 系列的引用。

---

## 3. 使用Aider浪费推理

**原文标题**: Wasting Inferences with Aider

**原文链接**: [https://worksonmymachine.substack.com/p/wasting-inferences-with-aider](https://worksonmymachine.substack.com/p/wasting-inferences-with-aider)

无法访问文章链接。

---

## 4. Whenever - Python 的类型化和时区安全日期时间

**原文标题**: Whenever – typed and DST-safe datetimes for Python

**原文链接**: [https://github.com/ariebovenberg/whenever](https://github.com/ariebovenberg/whenever)

Whenever：一款旨在解决Python `datetime` 模块及Arrow和Pendulum等现有第三方库不足的全新 Python 库。它致力于为处理日期时间提供更健壮、类型安全和高性能的解决方案，尤其是在夏令时 (DST) 以及 naive 和 aware 日期时间区分方面。

Whenever 的主要优势包括：

*   **DST 安全的算术运算：** 在日期时间计算过程中正确处理 DST 转换，避免常见错误。
*   **类型安全的 API：** 强制正确使用 naive 和 aware 日期时间，防止类型相关的错误。
*   **性能：** 与 Arrow 和 Pendulum 相比，提供卓越的性能。
*   **熟悉的概念：** 基于 Temporal、Noda Time 和 Joda Time 等其他日期时间库中已建立的成熟概念。

Whenever 引入了 `Instant`、`ZonedDateTime` 和 `LocalDateTime` 等特定类型，用于不同的日期时间用例，从而提高显式性并防止 naive 和 aware 日期时间的意外混合。

该库仍处于 1.0 之前的版本，API 可能会发生变化，但开发人员正在积极寻求反馈。除了更快的 Rust 实现之外，还提供纯 Python 版本。项目路线图包括可自定义的解析、间隔、范围、重复时间和闰秒解析等功能。它支持纳秒精度并遵循语义版本控制。

---

## 5. 茴香的魅力？

**原文标题**: Why Fennel?

**原文链接**: [https://fennel-lang.org/rationale](https://fennel-lang.org/rationale)

茴香（Fennel）是一种运行在 Lua 运行时上的编程语言，提供了一种替代语法并解决了人们认为 Lua 存在的不足。Lua 以其简洁性、速度和可嵌入性而著称，使得程序可以重新编程。茴香在利用 Lua 优势的同时，改进了语法和错误预防等方面的特性。

茴香的主要区别在于其 Lisp 风格的、以括号优先的语法，消除了歧义、语句、运算符优先级和提前返回，从而简化了语法。它通过使意外的全局变量使用变得困难来解决 Lua 的全局变量问题。与 Lua 的可选 `const` 变量不同，茴香强制使用 `var` 来声明重新赋值的变量，从而促进更简洁的代码。

茴香改进了 Lua 的表表示法，使用方括号表示顺序表，使用大括号表示键/值表。它将数值 for 循环与基于迭代器的循环分开，并引入 `each` 用于后者。

在函数方面，茴香允许未经检查的 (`fn`) 和经过参数个数检查的 (`lambda`) 函数定义。此外，茴香还融入了解构和模式匹配，这些都是 Lua 所缺乏的特性。最后，它还具有用于扩展语言的宏系统，尽管其使用被有意地淡化。本质上，茴香旨在增强 Lua 的可用性并防止常见错误，同时保留其核心优势。

---

## 6. Cargo-mutants:僵尸: 注入缺陷，看你的测试能否发现它们

**原文标题**: Cargo-mutants:zombie: Inject bugs and see if your tests catch them

**原文链接**: [https://github.com/sourcefrog/cargo-mutants](https://github.com/sourcefrog/cargo-mutants)

`cargo-mutants` 是一款 Rust 工具，旨在通过识别在不导致测试失败的情况下可以插入 bug 的区域来提高程序质量，从而指出测试套件的潜在弱点。它通过验证测试是否彻底检查了代码行为来补充覆盖率测量。该工具旨在轻松用于任何使用 `cargo test` 或 `cargo nextest run` 的 Rust 项目，目的是突出显示容易出现 bug 或缺乏足够测试的区域。

可以通过 `cargo install --locked cargo-mutants` 轻松安装。 用户可以使用 `cargo mutants` 在整个项目上启动突变测试，或使用 `cargo mutants -f src/something.rs` 专注于特定文件。 文档 (https://mutants.rs/) 提供了详细指导，包括用于 pull requests 的增量测试的 CI 集成。

该项目欢迎用户反馈、赞助和贡献，以增强其功能。 截至 2025 年 1 月，它正在积极维护中，并计划定期发布版本。 该文档包括与其他技术的比较、设计说明、贡献指南和发行说明。

---

## 7. 菲利普·K·迪克：斯坦尼斯拉夫·莱姆是个共产主义委员会

**原文标题**: Philip K. Dick: Stanisław Lem Is a Communist Committee

**原文链接**: [https://culture.pl/en/article/philip-k-dick-stanislaw-lem-is-a-communist-committee](https://culture.pl/en/article/philip-k-dick-stanislaw-lem-is-a-communist-committee)

菲利普·K·迪克：斯坦尼斯拉夫·莱姆是个共产主义委员会
文章“菲利普·K·迪克：斯坦尼斯拉夫·莱姆是个共产主义委员会”详细描述了菲利普·K·迪克对备受赞誉的波兰科幻作家斯坦尼斯拉夫·莱姆的离奇而偏执的痴迷。 在 20 世纪 70 年代，迪克确信莱姆不是一个单独的个体，而是一个由共产主义作家和宣传员组成的集体，他们伪装成一个单一的作者，目的是渗透和控制科幻小说领域。

在偏执和安非他命的驱动下，迪克为联邦调查局编写了一份 180 页的报告，指责莱姆和所谓的共产主义委员会在科幻小说领域进行意识形态操纵和颠覆。 他认为他们利用自己的影响力来传播宣传，并通过巧妙编码的叙事来推行亲共议程。

这篇文章突出了迪克指控的非理性。 莱姆的作品虽然具有哲学性和对社会结构的批判性，但并不包含明确的甚至是可辨别的共产主义宣传。 文章指出，迪克的偏执源于他个人的挣扎，包括吸毒、精神不稳定以及对权威的根深蒂固的不信任，这导致他通过扭曲的视角来解读现实。

讽刺的是：迪克是一位以探索现实扭曲和意识本质为主题的作家，却成为了自己扭曲的现实感知的受害者，将自己的恐惧和焦虑投射到科幻小说界一位受人尊敬的人物身上。 这篇文章最终描绘了迪克陷入偏执的过程，以及他不受控制的焦虑所造成的悲剧性后果，这导致他不公正地指责莱姆是共产主义阴谋的一部分。

---

## 8. Show HN: Gatehouse-TS – Rust 授权策略框架的 TypeScript 移植版

**原文标题**: Show HN: Gatehouse-TS – TypeScript port of Rust's authorization policy framework

**原文链接**: [https://github.com/9Morello/gatehouse-ts](https://github.com/9Morello/gatehouse-ts)

Gatehouse-TS 是一个 TypeScript 授权库，移植了 Rust 的 Gatehouse 的功能。它提供了灵活的访问控制策略，结合了基于角色的访问控制 (RBAC)、基于属性的访问控制 (ABAC) 和基于关系的访问控制 (ReBAC)。它拥有零运行时依赖，使其易于直接嵌入到项目中。

主要功能包括支持多范式授权、使用逻辑运算符（AND、OR、NOT）的策略组合、用于调试和审计的详细评估跟踪、用于构建自定义策略的流畅构建器 API，以及资源、操作和上下文的类型安全。

该库的源代码位于单个 TypeScript 文件 (src/index.ts) 中，鼓励直接集成和修改。文档提供了深入的使用说明，并且提供的快速入门示例演示了如何创建和使用基于角色的策略来评估用户访问权限。该示例展示了如何为资源上的操作定义角色，并检查具有特定角色的用户是否被允许执行给定的操作。可以将多个策略添加到 `PermissionChecker` 实例以实现复杂的授权逻辑。

---

## 9. 一个棘手的Commodore PET维修：追踪6个半坏的芯片

**原文标题**: A tricky Commodore PET repair: tracking down 6 1/2 bad chips

**原文链接**: [http://www.righto.com/2025/04/commodore-pet-repair.html](http://www.righto.com/2025/04/commodore-pet-repair.html)

本文详细介绍了修复一台1977年Commodore PET电脑的挑战性过程。作者出于怀旧情怀购入了这台PET电脑，但由于其组件的年代和设计而面临诸多困难。最初的症状是屏幕上充斥着乱码，表明系统存在故障。

修复过程包括使用Retro Chip Tester，结果显示有两个ROM芯片失效。使用适配器板替换了标准EPROM，但问题仍然存在。随后，利用逻辑分析仪跟踪6502处理器的内存访问，并结合Ghidra对ROM内容进行反向工程。

逻辑分析仪显示内存测试失败以及启动过程中的问题。识别并更换了三个损坏的RAM芯片（暂时减少了内存）。对启动信息错误的进一步分析，查明了一个有故障的ROM，导致了错误的内存地址和乱码的屏幕输出。这被追溯到一个功率不足的EPROM编程器，导致ROM数据不稳定。重新编程EPROM并更换另一个RAM芯片后，问题最终得到解决。

总共有六个芯片损坏：两个ROM和四个RAM。作者反思了逻辑分析仪在理解系统行为方面的价值，即使直接芯片测试可能更快。文章最后，PET电脑终于可以正常工作并显示图形模式，突出了老式电脑维修的挑战和回报。

---

## 10. 《Compute》杂志时隔35年回归，将专注于复古计算

**原文标题**: Compute's Gazette Magazine Returns After 35 Yrs, Will Focus on Retro Computing

**原文链接**: [https://www.computesgazette.com/](https://www.computesgazette.com/)

《Compute!'s Gazette》杂志将于35年后回归，扩大关注范围，涵盖整个复古计算社群。该杂志将提供印刷版和数字版，并提供月度订阅计划。回归刊计划于2025年7月发布，并承诺为复古计算爱好者带来“重大新闻”。

该杂志将刊登深入的文章、技巧和故事，庆祝计算的黄金时代。最近的新闻稿重点介绍了诸如“任天堂的游戏密钥改变了开发者和玩家的游戏规则”等功能，讨论了不断发展的DRM，以及一篇鼓励支持当地复古街机厅的文章。即将发行的一期还将探讨生成式人工智能对游戏开发的影响，解决其挑战和潜力。

---

## 11. AMD NPU和赛灵思Versal AI引擎在射电天文学中的信号处理（2024）[pdf]

**原文标题**: AMD NPU and Xilinx Versal AI Engines Signal Processing in Radio Astronomy (2024) [pdf]

**原文链接**: [https://git.astron.nl/RD/acap/-/raw/main/Presentation_FPL24_Vincent_Sprave.pdf](https://git.astron.nl/RD/acap/-/raw/main/Presentation_FPL24_Vincent_Sprave.pdf)

由于该PDF文档主要由二进制数据（很可能是压缩图像和字体）组成，我无法提取有意义的文本来提供关于“AMD NPU 和 Xilinx Versal AI 引擎在射电天文学中的信号处理 (2024)”一文的摘要。提供的文本包含 PDF 命令和编码数据，而不是研究论文的实际内容。因此，我无法根据提供的信息给出有用的摘要。

要获得摘要，您需要：

1. 使用 OCR（光学字符识别）软件从 PDF 中提取文本。
2. 向我提供提取的文本。

然后，我可以处理它并为您提供摘要。

---

## 12. BPS：鲜为人知的GPS替代方案

**原文标题**: BPS is a GPS alternative that nobody's heard of

**原文链接**: [https://www.jeffgeerling.com/blog/2025/bps-gps-alternative-nobodys-heard](https://www.jeffgeerling.com/blog/2025/bps-gps-alternative-nobodys-heard)

文章讨论了BPS（广播定位系统），这是一种实验性的授时标准，可以作为GPS的地面备份。作者在NAB展会上偶然发现了它，并对其印象深刻，因为它使用ATSC 3.0电视广播信号实现了与GPS +/- 10纳秒的同步精度。

ATSC 3.0是一种正在推广的新型IP广播标准，BPS可以被纳入其中，利用美国潜在的1700个电视台的现有基础设施。精确授时对于包括媒体、电网和5G通信在内的各个领域至关重要，因此可靠的GPS替代方案至关重要，尤其是一个能够抵抗干扰的方案。

作者强调了NAB展会上出现的与BPS相关的技术，包括消费者英特尔主板上的内置PPS连接器。他们计划在未来的YouTube频道内容中更深入地研究BPS。评论部分讨论了BPS的潜在应用，包括作为航空GPS的备份以及与GPS等系统相比，其在全球普及方面的局限性。一位评论者提到了一种使用FM广播同步时钟的历史方法，展示了一个类似的概念。

---

## 13. Show HN: Chonky – 一种用于文本语义分块的神经方法

**原文标题**: Show HN: Chonky – a neural approach for text semantic chunking

**原文链接**: [https://github.com/mirth/chonky](https://github.com/mirth/chonky)

Chonky：一款利用微调Transformer模型，将文本智能分割成语义连贯片段的全新Python库。它尤其适用于检索增强生成（RAG）系统等应用。

该库可以使用 `pip install chonky` 轻松安装。 使用Chonky涉及实例化 `TextSplitter` 类（首次运行时会下载transformer模型），并将要分块的文本传递给 `splitter()` 函数。然后，该库会返回一个文本块的迭代器。

提供的示例展示了Chonky如何将一段关于作者早期写作和编程经历的段落分割成三个不同的语义块：一个关于写短篇故事，一个关于使用IBM 1401，以及最后一个关于机器的描述性块。 使用的transformer模型是 `mirth/chonky_distilbert_base_uncased_1`。

---

## 14. 超过1500种新字体，包括经典字体，加入Adobe Fonts。

**原文标题**: More than 1,500 new fonts – including all-time favorites – come to Adobe Fonts

**原文链接**: [https://blog.adobe.com/en/publish/2025/04/08/more-than-1500-new-fonts-including-all-time-favorites-come-to-adobe-fonts](https://blog.adobe.com/en/publish/2025/04/08/more-than-1500-new-fonts-including-all-time-favorites-come-to-adobe-fonts)

Adobe Fonts新增1500多种字体，为五年来最大规模的字体扩展，Creative Cloud订阅者无需额外付费。本次更新包含Monotype公司广受欢迎且通用性强的字体，例如Helvetica、Gotham、Avenir、Times New Roman、Arial和Proxima Nova（扩展至四种更多语言）。

本次更新强调了跨平台和应用程序的品牌一致性和易用性。这些新字体旨在满足广泛的设计需求，从徽标创建到商业提案，并且可以在Adobe Creative Cloud应用程序（如Photoshop、Illustrator、InDesign和Express）的桌面版、移动版和网页版上使用。此举旨在减少共享设计时字体缺失的弹出窗口问题。

除了经典字体的增加，Adobe Fonts还扩展了其全球字体库，增加了对阿拉伯语、中文、日语、韩语、泰语和印地语的支持，以满足更广泛的国际项目需求。Adobe Fonts目前共有超过30,000种字体，旨在为创作者提供一个适用于印刷、数字和多语言设计项目的通用字体库。付费Creative Cloud订阅者无需额外下载即可立即使用这些字体。

---

## 15. SVG的妙用

**原文标题**: Nice things with SVG

**原文链接**: [https://fuma-nama.vercel.app/blog/svg-art](https://fuma-nama.vercel.app/blog/svg-art)

本文探讨了 SVG 的创意用法，特别关注动画和遮罩技术。文章首先演示了如何使用 SVG 线条、遮罩和 CSS 动画创建动画“导线”。 通过动画矩形块并使用 SVG 中绘制的线条对其进行遮罩，作者实现了流畅的导线效果。 该示例逐步添加样式、渐变和基于变量的动画，以增强自定义。

然后，文章转向一个更复杂的应用：在 Fumadocs 中复制 Clerk 的目录 (TOC) 样式。 挑战在于创建一个动态的、高亮的“缩略图”，用于指示目录的活动部分，同时保持服务器端渲染 (SSR) 兼容性。 解决方案包括使用绝对定位在服务器上渲染基本的 TOC 轮廓。

然而，动态缩略图是在客户端使用 SVG 渲染的。 关键是构造一个 SVG `<path>` 元素，其 "d" 属性定义了一系列精确模仿服务器渲染的 TOC 轮廓的线条命令。 然后，此 SVG 用作 `mask-image` 来遮罩一个动画 `div`，从而创建高亮的缩略图效果。 通过使用 JavaScript 根据活动的 TOC 项目控制 `div` 的高度和垂直位置，作者实现了平滑的交互式动画。文章最后感谢 Clerk 为这种创新的 TOC 设计方法提供的灵感。

---

## 16. 命名性失语症：命名检索障碍

**原文标题**: Nominal Aphasia: Problems in Name Retrieval

**原文链接**: [https://serendipstudio.org/exchange/darlene-forde/nominal-aphasia-problems-name-retrieval](https://serendipstudio.org/exchange/darlene-forde/nominal-aphasia-problems-name-retrieval)

虽然标题为“命名性失语症：名称检索问题”，但内容似乎是网站或文档“Serendip Studio”的菜单或章节列表。内容概述了与特定平台Serendip Studio相关的各种资源和信息，尽管标题暗示着对命名性失语症的关注。

虽然标题表明内容将涉及名称检索方面的困难（命名性失语症），但所提供的主题列表并未直接反映这一点。相反，它侧重于：

*   **Serendip Studio简介：** 几个章节专门介绍和浏览该平台，包括“关于Serendip Studio”、“如何找到方向”和“导览”。
*   **更新和社区：** “最新消息”、“论坛”和“Serendip读者反馈”等部分表明该平台具有持续更新和活跃的社区。
*   **导航和资源：** “站点地图”、“Serendip A到Z”和“书架”等选项指向可供用户使用的资源。
*   **一般信息：** “关于Serendip的事实”和“成立于1994年”提供了关于平台本身的基本细节。
*   **用户互动：** “加入我们”鼓励参与和社区参与。

因此，此内容的主要功能是引导访问者了解 Serendip Studio 平台，而不是像标题可能暗示的那样深入研究命名性失语症的具体内容。真正的摘要需要关于名称检索困难的实际内容。

---

## 17. WebTUI – 将终端UI之美带到浏览器的CSS库

**原文标题**: WebTUI – A CSS Library That Brings the Beauty of Terminal UIs to the Browser

**原文链接**: [https://webtui.ironclad.sh](https://webtui.ironclad.sh)

WebTUI是一个CSS库，旨在将终端用户界面（TUI）的美学带到Web浏览器。文档涵盖WebTUI的多个方面，包括样式指南、插件开发、入门功能以及输入字段、徽章、按钮和排版等组件的详细信息。

该库支持通过CSS变量进行主题化，并提供官方和社区创建的插件，包括Catppuccin和Nord等主题，以及用于Nerd Font集成的插件。

文档提供了ESM、CDN和完整库导入的安装说明。此外，文档还包括ASCII框创建的信息，涵盖用法、边框类型、包含和自定义属性，以及创建插件的指南。

主要主题包括如何使用`box-`、`size-`和`variant-`等前缀来设置元素样式，以及如何扩展和限定样式范围。文档还阐述了等宽字体和字符单元格在Web上创建真正的TUI体验中的重要性。最后，文档解释了TUI和GUI之间的区别。

---

## 18. 使用C#制作SNES ROM

**原文标题**: Making SNES ROMs using C#

**原文链接**: [https://www.reddit.com/r/dotnet/s/fhm4TUNhlX](https://www.reddit.com/r/dotnet/s/fhm4TUNhlX)

无法访问文章链接。

---

## 19. 为什么 Pascal 不是我最喜欢的编程语言 (1981) [pdf]

**原文标题**: Why Pascal Is Not My Favorite Programming Language (1981) [pdf]

**原文链接**: [https://doc.cat-v.org/bell_labs/why_pascal/why_pascal_is_not_my_favorite_language.pdf](https://doc.cat-v.org/bell_labs/why_pascal/why_pascal_is_not_my_favorite_language.pdf)

鉴于所提供的PDF内容，无法对“为什么 Pascal 不是我最喜欢的编程语言 (1981)”一文进行有意义的总结。文本内容似乎已被破坏，包含大量无法辨认的字符和符号。看来该PDF未正确转换为可读的文本格式，或者包含损坏。因此，所提供的内容无法体现作者在对Pascal编程语言的批判中所要表达的实际论点或观点。

---

## 20. 如何避免制作二级火箭

**原文标题**: How to not build a two stage model rocket

**原文链接**: [https://knowone08.gitbook.io/vgecrocketry](https://knowone08.gitbook.io/vgecrocketry)

一个团队建造名为维内莎的两级火箭的首次尝试，这篇博文幽默地讲述了整个过程。目标并非挑战纪录高度，而是成功设计并执行级间分离，为更大的项目铺平道路。

该团队优先考虑学习和简洁性，专注于掌握级间分离，而不是追求完美的性能指标。他们接受妥协方案，使用现成的材料，如纸张和3D打印部件，而不是昂贵的航空航天级材料。

火箭采用了定制设计的固体火箭发动机，带有金属外壳和KNDX燃料，并使用OpenMotor进行模拟。主体结构主要使用手工制作的纸质箭体，并用螺旋缠绕的工程图纸加固，搭配3D打印的鼻锥、尾翼支架和尾翼。

航空电子系统至关重要，旨在基于实时传感器数据进行主动级间分离，而不是依赖于预先编程的定时。燃尽检测逻辑依赖于检测加速度下降。该系统采用冗余飞行计算机（Grace和RocketNerve），配备加速度计、气压传感器和热爆/弹射通道。

回收仅针对第二级，使用由任一飞行计算机在远地点检测时触发的弹簧加载降落伞弹射系统。第一级则允许自由坠落。该博客承诺未来的文章将详细介绍航空电子逻辑的固件和流程图。最终，该博客强调了从错误中学习的价值以及在构建复杂项目时专注于核心挑战的重要性。

---

## 21. 告知蜜蜂

**原文标题**: Telling the Bees

**原文链接**: [https://emergencemagazine.org/essay/telling-the-bees/](https://emergencemagazine.org/essay/telling-the-bees/)

《告知蜜蜂》一文，于2023年2月15日发表在《涌现》杂志上，聚焦斯洛文尼亚的授粉昆虫，很可能探讨了斯洛文尼亚人与其蜜蜂之间的关系。鉴于标题，该文章可能深入探讨“告知蜜蜂”这一历史和文化习俗，即养蜂人将人类家庭中的重要事件，如出生、死亡、婚姻和离世，告知他们的蜜蜂。

该文章很可能强调了蜜蜂对斯洛文尼亚生态系统和文化的重要性。斯洛文尼亚以其丰富的养蜂传统而闻名，该文章很可能讨论了维持健康的蜜蜂种群的重要性以及它们面临的威胁，例如农药使用、栖息地丧失和气候变化。

此外，该文章可能探讨了斯洛文尼亚独特的养蜂实践，或许会提及彩绘蜂箱面板、原产于该地区的卡尼鄂拉蜜蜂（Apis mellifera carnica），或养蜂教育和保护工作的重要性。

总之，《告知蜜蜂》很可能调查了蜜蜂的文化意义，以及在斯洛文尼亚养蜂背景下告知蜜蜂人类事件的历史习俗，同时也突出了授粉昆虫健康和保护在斯洛文尼亚生态系统和文化中的重要性。

---

## 22. RNA干扰与纳米药物联手对抗危险的真菌感染

**原文标题**: RNA interference and nanomedicine team up to fight dangerous fungal infections

**原文链接**: [https://phys.org/news/2025-03-rna-nanomedicine-dangerous-fungal-infections.html](https://phys.org/news/2025-03-rna-nanomedicine-dangerous-fungal-infections.html)

本文报道了一种对抗危险真菌感染的新方法，该方法前景广阔。目前，真菌感染呈上升趋势，且对现有治疗方法的耐药性日益增强。维尔茨堡大学医院的研究人员已成功将RNA干扰(RNAi)与纳米医学相结合，以靶向致命的烟曲霉菌。

这项创新策略包括将小干扰RNA(siRNA)与两性霉素B(AmB)封装在阴离子脂质体中。脂质体将siRNA直接递送到真菌细胞内。然后，siRNA会沉默重要的真菌基因，从而有效抑制病原体的生长。两性霉素B有助于渗透真菌细胞壁，增强siRNA的进入。

这是一项重大突破，因为它标志着RNAi技术首次成功应用于人体致病真菌的感染模型。研究团队利用昆虫幼虫作为感染模型，以减少动物实验。该研究强调了siRNA作为对抗真菌感染的有效工具，尤其是在耐药菌株日益普遍的情况下。该方法也具有应用于其他危险真菌病原体的潜力。

---

## 23. 如何在Unix系统上安装个人版本的程序

**原文标题**: How I install personal versions of programs on Unix

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/sysadmin/MyPersonalProgramsSetup](https://utcc.utoronto.ca/~cks/space/blog/sysadmin/MyPersonalProgramsSetup)

由于大量通常用于LLM训练，并使用旧浏览器用户代理（尤其是Chrome）的高流量爬虫激增，Chris Siebenmann的博客Wandering Thoughts正在阻止使用较旧或可疑浏览器版本的用户访问。此举旨在减轻这些爬虫对博客服务器造成的负载。

如果合法用户遇到此阻止，建议他们通过其大学电子邮件（可从其隶属关系推断）联系Siebenmann，提供他们的浏览器详细信息和User-Agent字符串以进行故障排除。

针对archive.today、archive.ph和archive.is等存档服务解决了一个特定问题。这些存档服务使用与恶意爬虫无法区分的方法来抓取网站，采用旧的Chrome User-Agent值，使用广泛分布的IP地址，有时还会伪造反向DNS条目。Siebenmann建议使用archive.org，因为它是一个行为更好的存档爬虫，可以访问他的博客。

本质上，这篇文章解释了为打击Wandering Thoughts上的恶意爬虫而采取的措施，并为被系统错误阻止的合法用户（尤其是那些使用某些存档服务的用户）提供了指导。

---

## 24. 我抛弃了笔记本电脑，转而使用了一台袖珍迷你电脑和一副AR眼镜。

**原文标题**: I ditched my laptop for a pocketable mini PC and a pair of AR glasses

**原文链接**: [https://www.tomsguide.com/computing/i-ditched-my-laptop-for-a-pocketable-mini-pc-and-a-pair-of-ar-glasses-heres-what-happened](https://www.tomsguide.com/computing/i-ditched-my-laptop-for-a-pocketable-mini-pc-and-a-pair-of-ar-glasses-heres-what-happened)

Tom's Guide 的 Anthony Spadafora 详细介绍了自己放弃笔记本电脑，转而使用迷你 PC (Khadas Mind 2S)、AR 眼镜 (Xreal One) 和大容量充电宝 (Ugreen Nexode 25,000 mAh) 组成的便携式设备的体验。他发现虽然他喜欢自己的桌面设置，但他怀念在家外办公的自由。

他选择 Khadas Mind 2S 是因为其便携性、USB-C 供电和视频输出功能。选择 Xreal One AR 眼镜是因为其即插即用的简易性以及缺乏内置电池，使其更轻便且无需单独充电。Ugreen 充电宝为这两个设备在旅途中提供了充足的电力。

Spadafora 发现这种设置出奇地容易适应，即使在咖啡店和飞机等公共场所也是如此。AR 眼镜让他能够创建一个个性化的工作空间，拥有一个大型虚拟超宽显示器，同时仍能保持对周围环境的感知。他能够无缝地执行所有常规工作任务，例如编辑评论和撰写文章。他更喜欢这种设置而不是笔记本电脑，因为它允许他使用自己喜欢的机械键盘和轨迹球鼠标，并提供相当于超宽显示器的效果，这是笔记本电脑通常所缺乏的。他在前往纽约旅行时成功使用了它，并撰写了 Nintendo Switch 2 的评测。他鼓励读者考虑尝试类似的设置。

---

## 25. Emacs Lisp 元素

**原文标题**: Emacs Lisp Elements

**原文链接**: [https://protesilaos.com/emacs/emacs-lisp-elements](https://protesilaos.com/emacs/emacs-lisp-elements)

《Protesilaos Stavrou Emacs Lisp 元素》是一本指南，全面概述了用于扩展 Emacs 文本编辑器的 Emacs Lisp (Elisp) 编程语言。本书侧重于理解核心概念以及它们如何应用于自定义 Emacs。

涵盖的主要主题包括：

*   **入门：** Emacs Lisp 介绍，强调其在自定义 Emacs 中的作用以及为个人使用编程的乐趣。
*   **求值：** 理解 Emacs 如何求值 Elisp 代码，包括交互式函数、键绑定以及不同的求值方法，例如 `eval-last-sexp` 和 `eval-expression`。
*   **副作用和返回值：** 平衡函数输出与 Emacs 环境的更改，以实现有效的自定义。
*   **缓冲区作为数据结构：** 使用缓冲区来存储、操作和显示数据，提取文件内容，呈现操作结果，以及将变量与缓冲区关联。
*   **文本属性：** 管理缓冲区中的文本属性，包括显示属性，获取没有属性的文本，以及在文本段之间复制属性。
*   **符号和引用：** 解释符号、平衡表达式以及引用技术以防止过早求值。
*   **部分求值：** 讨论如何在列表、宏和特殊形式内部求值表达式。
*   **列表映射：** 侧重于迭代和转换元素列表。
*   **匹配数据：** 解释如何访问上次搜索的结果。
*   **切换上下文：** 讨论如何更改当前缓冲区、窗口或缩小状态。
*   **控制流：** 使用诸如 `if`、`cond`、`if-let*` 和 `pcase` 等构造的基本和高级控制流机制。
*   **错误处理：** 使用回退机制运行代码的策略。
*   **函数：** 关于使用命名函数与 lambda 函数的建议。
*   **交互式函数：** 创建以交互方式和编程方式工作的函数的技巧。

本书旨在提供 Elisp 的“大局观”，作为 Emacs Lisp 参考手册的指南，鼓励动手实验和更深入地理解 Emacs 自定义。

---

## 26. 鱼鹰 – 保护您免受恶意网站侵害的浏览器扩展

**原文标题**: Osprey – Browser extension that protects you from malicious websites

**原文链接**: [https://github.com/Foulest/Osprey](https://github.com/Foulest/Osprey)

鱼鹰浏览器扩展程序旨在保护用户免受恶意网站的侵害。它集成了多个知名安全服务，包括 Microsoft SmartScreen、Symantec Browser Protection、Emsisoft Web Protection、Bitdefender TrafficLight、Norton SafeWeb、TOTAL WebShield 和 G DATA WebProtection，以实时分析 URL。

该扩展程序会阻止被归类为恶意、钓鱼、欺诈、PUA（潜在有害应用程序）、加密劫持、恶意广告、垃圾邮件、广告软件、已入侵、吸费软件和不受信任的网站。当检测到恶意网站时，鱼鹰会阻止该页面并向用户显示警告。

鱼鹰通过其设置提供可自定义的保护选项，允许用户微调他们希望受到保护的威胁类型。

可以通过 Chrome Web Store 和 Microsoft Edge Addons 安装。 对于手动安装，用户可以为 Chrome 或 Edge 编译扩展程序，下载工件，解压 ZIP 文件，在其浏览器中启用开发者模式，然后加载解压缩的扩展程序文件夹。

如需支持和帮助，建议用户在项目的 Issues 部分中提出问题。

---

## 27. Pixel 9a 的 GrapheneOS 实验性版本发布

**原文标题**: Experimental release of GrapheneOS for Pixel 9a

**原文链接**: [https://grapheneos.social/@GrapheneOS/114327666433966529](https://grapheneos.social/@GrapheneOS/114327666433966529)

GrapheneOS发布Pixel 9a高实验性操作系统版本。该消息在Mastodon上发布。这表明GrapheneOS可能正在扩大对谷歌Pixel设备的支持，但“高实验性”性质意味着用户应预期潜在的不稳定性和错误。Mastodon公告还指出，使用Mastodon网页版需要Javascript，并建议用户探索适用于其特定平台的原生应用程序。因此，要访问完整公告和有关实验性版本的任何随附信息，建议用户使用Mastodon客户端或在其Web浏览器中启用Javascript。

---

## 28. 亚马逊在欧洲实验中将司机转变为急救员

**原文标题**: Amazon Turned Drivers into First Responders in Europe Experiment

**原文链接**: [https://www.bloomberg.com/news/articles/2025-04-10/amazon-turned-drivers-into-first-responders-in-europe-experiment](https://www.bloomberg.com/news/articles/2025-04-10/amazon-turned-drivers-into-first-responders-in-europe-experiment)

无法访问文章链接。

---

## 29. IBM代码页437中为什么有个“小屋”字符？

**原文标题**: Why is there a “small house” in IBM's Code page 437?

**原文链接**: [https://blog.glyphdrawing.club/why-is-there-a-small-house-in-ibm-s-code-page-437/](https://blog.glyphdrawing.club/why-is-there-a-small-house-in-ibm-s-code-page-437/)

本文探讨了 IBM 代码页 437 (CP437) 中代码位置 0x7F 处的小房子字形 (⌂) 背后的谜团，该位置按理应代表“删除”(DEL) 控制字符。 作者深入研究了 CP437 随 IBM PC 兴起的历史背景，强调其通过包含诸如笑脸和扑克牌花色等“不严肃”字符而偏离既定标准，这些字符旨在用于基于文本的游戏中显示。

然后，本文提出了几种试图解释房子符号起源的理论，并承认缺乏明确的文档。 这些理论包括：

*   **家用电脑符号：** 房子代表 IBM 进入家用电脑市场。
*   **退格关系：** 旋转退格符号类似于房子。
*   **Datamaster 来源：** 复制自 IBM 的 System/23 Datamaster。
*   **王安影响：** 借用自王安文字处理机。
*   **布利斯符号学联系：** 受布利斯符号学房子字形的启发。
*   **误解的王安 Delta：** 匆忙复制王安的 delta 符号，由于像素拉伸而被误解为房子。
*   **Delta 符号象征意义：** 代表数学符号 Delta (Δ)，在某些旧系统中也称为 DEL。

本文强调了房子符号的模糊性和多功能性，展示了它在 DOS 游戏和 ASCII 艺术中的各种用途。 虽然没有提供明确的答案，但作者倾向于认为“误解的王安 Delta”理论是最引人注目的。

---

## 30. 交叉熵与KL散度

**原文标题**: Cross-Entropy and KL Divergence

**原文链接**: [https://eli.thegreenplace.net/2025/cross-entropy-and-kl-divergence/](https://eli.thegreenplace.net/2025/cross-entropy-and-kl-divergence/)

本文解释了交叉熵和KL散度，这两个概念在机器学习中至关重要，尤其是在分类损失函数方面。文章首先将单个事件的信息内容定义为惊讶程度，并使用事件逆概率的对数以比特为单位进行衡量。然后将熵定义为随机变量信息的期望值，用于量化不确定性；熵越高，不确定性越高。

交叉熵将熵扩展到具有两个概率分布的场景：实际数据分布（P）和预测分布（Q）。它表示在假设数据遵循Q的情况下，编码P所需的平均比特数。在模型训练期间，最小化交叉熵旨在使预测分布与实际分布对齐。

KL散度，或相对熵，衡量两个概率分布之间的差异。它计算为交叉熵与真实分布的熵之间的差值。与交叉熵不同，当分布相同时，KL散度为零，使其成为更合适的差异度量。然而，它不是对称的，因此不是真正的距离度量。

文章还强调了交叉熵最小化与最大似然估计（MLE）之间的联系。最大化参数化模型分布与真实数据分布匹配的似然性，在数学上等同于最小化这两个分布之间的交叉熵。这为在机器学习中使用交叉熵作为损失函数提供了理论依据。

---

## 31. Show HN: memEx，一款受 Zettlekasten 和 Org-mode 启发的个人知识库

**原文标题**: Show HN: memEx, a personal knowledge base inspired by zettlekasten and org-mode

**原文链接**: [https://gitea.bubbletea.dev/shibao/memex](https://gitea.bubbletea.dev/shibao/memex)

无法访问文章链接。

---

## 32. 苦涩的预言

**原文标题**: The Bitter Prediction

**原文链接**: [https://4zm.org/2025/04/05/bitter-prediction.html](https://4zm.org/2025/04/05/bitter-prediction.html)

作者是一位软件开发者，分享了他们在采用 Claude、Copilot 和 Gemini 等 AI 编码工具时的情感历程，强调了最初的兴奋，随后是对编程未来日益增长的担忧。

作者最初对 Claude Code 理解和重构代码的能力印象深刻，这提高了生产力，但也体验到了一种不满。这种感觉类似于童年时在游戏中作弊（《幽浮：未知敌人》），最终毁掉了游戏的乐趣。作者担心 AI 可能会以类似的方式削弱编码带来的满足感，即使只是作为一种爱好，因为它能做得“更好”。

作者的担忧不仅仅在于个人乐趣。他们强调了使用 AI 编码工具的成本，提到个人每天花费 5 美元。这引发了对有抱负的开发者，尤其是在大部分人口每天生活费低于这个数额的地区，进入门槛日益增长的担忧。作者预测，先进的 AI 编码工具将变得不可或缺，但对许多人来说却遥不可及，从而加剧现有的不平等。他们还提到了为驱动这些 AI 工具所需的数据中心可能造成的环境影响。

最终，作者认为由于其经济效率，采用智能体 AI 开发是不可避免的，无论其潜在的缺点如何。虽然希望被证明是错误的，但作者以一个“痛苦的预测”结束：未来的软件开发将变得更少乐趣和更难获得。

---

## 33. 欧洲核子研究中心发布未来环形对撞机可行性报告

**原文标题**: CERN releases report on the feasibility of a possible Future Circular Collider

**原文链接**: [https://home.cern/news/news/accelerators/cern-releases-report-feasibility-possible-future-circular-collider](https://home.cern/news/news/accelerators/cern-releases-report-feasibility-possible-future-circular-collider)

欧洲核子研究中心发布了未来环形对撞机 (FCC) 的可行性研究报告，该对撞机有望成为大型强子对撞机 (LHC) 的继任者。 FCC 将是一个周长 91 公里的粒子对撞机，旨在进一步研究希格斯玻色子和其他基本物理问题。

拟议的项目包括两个阶段：首先，一个用于希格斯玻色子、弱电和顶夸克研究的正负电子对撞机，随后是一个以 100 TeV 运行的质子-质子对撞机。 该研究涵盖了物理目标、地质、土木工程、基础设施、环境影响、研发、社会经济效益和成本等方面。

包括隧道和基础设施在内的正负电子阶段的预计成本为 150 亿瑞士法郎，将在 2030 年代初开始的 12 年内分摊。 欧洲核子研究中心强调可持续性，旨在通过生态设计原则和能源再利用等地域协同效应来实现低环境足迹。

对撞机环的布局经过精心规划，周长 90.7 公里，平均深度 200 米，考虑了地域兼容性、环境问题、施工限制和成本。 在整个研究过程中，欧洲核子研究中心与法国和瑞士进行了合作。

该报告将由专家审查，然后于 2025 年 11 月由欧洲核子研究中心理事会审查，并可能在 2028 年左右做出是否继续进行的决定。 像 FCC 这样的粒子对撞机推动了医学、能源和先进探测器等领域的技术进步。 该研究有助于不断更新的欧洲粒子物理战略。

---

## 34. 欺骗世界的假照片

**原文标题**: Fake images that fooled the world

**原文链接**: [https://www.theguardian.com/artanddesign/2025/apr/12/28-fake-images-that-fooled-the-world](https://www.theguardian.com/artanddesign/2025/apr/12/28-fake-images-that-fooled-the-world)

本文探讨了照片篡改的历史，认为这种做法并非现代现象，而是在摄影术发明之初就已存在。作者认为，虽然人工智能深度伪造被视为一种新的威胁，但照片修改自一开始就被用于各种目的。

照片篡改的动机包括政治公关和宣传，例如将亚伯拉罕·林肯的头叠加到另一个人的身体上，朝鲜在军事展示中添加气垫船，以及共和党人伪造约翰·克里与简·方达的合影。文章还强调了照片篡改如何被用来负面描绘他人，例如《时代》杂志上辛普森被调暗的照片。

除了政治之外，文章还探讨了其他动机，例如虚荣、经济利益甚至复仇。作者提到了围绕罗伯特·卡帕的“倒下的士兵”照片的争论、大脚怪录像的商业潜力以及尼斯湖水怪的恶作剧。

文章还讨论了缺乏明确解释的篡改图像，例如9/11事件前在双子塔上的恶作剧照片。作者认为，观众受幻想或恐惧驱动的相信欲望，对于假图像的传播至关重要。文章最后指出，假图像之所以能够存在，是因为它们向我们展示了我们想看到的东西，满足了我们的梦想或噩梦。

---

## 35. ArkType：人体工学 TS 验证器，速度比 Zod 快 100 倍

**原文标题**: ArkType: Ergonomic TS validator 100x faster than Zod

**原文链接**: [https://arktype.io/](https://arktype.io/)

ArkType 是一款高性能 TypeScript 验证器，旨在改进现有的 Zod 和 Yup 等解决方案。它拥有显著的速度优势，声称运行时速度比 Zod 快 100 倍，比 Yup 快 2000 倍。主要特性和优势包括：

*   **符合人体工程学的 TypeScript 验证：** ArkType 利用熟悉的 TypeScript 语法来定义验证模式，提供类型安全和自动补全。
*   **改进的开发者体验：** 该平台在编辑器中提供类型级别的反馈，无需插件或构建步骤。 它还生成深度可定制且可读的错误消息。 定义设计得简洁明了，并且悬停提示信息丰富。
*   **性能：** 强调在运行时验证和编辑器性能方面的卓越速度。
*   **深度内省能力：** 使用集合论来暴露运行时类型之间的关系，镜像 TypeScript 的编译时理解。 启用运行时类型分析。
*   **内在优化：** 模式在内部进行规范化，以实现联合的最佳区分和快速处理。
*   **全面的文档：** 提供涵盖安装和集成的详尽文档。

---

## 36. 狩猎采集者航海远至最偏远的地中海岛屿

**原文标题**: Hunter-gatherer sea voyages extended to remotest Mediterranean islands

**原文链接**: [https://www.nature.com/articles/s41586-025-08780-y](https://www.nature.com/articles/s41586-025-08780-y)

本文提供了证据，证明马耳他群岛存在一个此前未知的旧石器时代中期居住点，从而将人类出现在这些偏远地中海岛屿上的时间线向前推进了约1000年。在马耳他Latnija进行的考古调查显示，一系列沉积物中包含石器工具、炉灶以及距今约8500年（ka）的野生动植物遗骸。

当时居住在马耳他的狩猎采集者既利用陆地动物（主要是红鹿），也利用海洋资源（鱼类、海洋哺乳动物和腹足动物），表明他们有能力在一个小岛上维持生存。木炭和贝壳的放射性碳年代测定支持了年代学模型，证实了在新石器时代农民于约7500年前到达之前，人类就已存在。

这一发现挑战了狩猎采集者无法或不愿意进行长途海上航行到偏远岛屿的传统观点。马耳他群岛需要从西西里岛进行约100公里的海上航行，是迄今为止有记录的最长地中海狩猎采集者海上航行。

在Latnija发现的石器工具主要由当地石灰石制成，与后来的新石器时代组合不同，类似于在撒丁岛发现的权宜性的旧石器时代中期技术。动物遗骸证实了对野生资源的利用，表明在农业引入之前存在狩猎采集的生活方式。这些发现为欧洲晚期狩猎采集者的航海能力提供了新的见解，并突出了此前未被认识到的地中海区域之间的联系。

---

## 37. Tunarr：从服务器媒体创建并配置直播电视频道

**原文标题**: Tunarr: Create and configure live TV channels from media on your servers

**原文链接**: [https://tunarr.com/](https://tunarr.com/)

Tunarr是一款软件应用程序，允许用户从存储在Plex、Jellyfin或Emby服务器上的媒体创建和配置直播电视频道。它构建于dizqueTV的基础之上，并进行了大量的重写以实现现代化和增强性能。

用户可以通过基于Web的UI自定义频道、节目、广告和设置。然后，通过将模拟的Tunarr HDHomerun调谐器添加到Plex、Jellyfin和Emby等媒体服务器，或通过与任何IPTV播放器应用程序兼容的生成的M3U文件，可以观看这些频道。

该项目旨在使其技术堆栈现代化，为现有的dizqueTV用户提供迁移路径，使用最新的Node.js版本稳定性能，改进Web UI的美观性，并引入新功能。最终，Tunarr致力于提供一种用户友好的方式，使用现有媒体库创建个性化的电视体验。

---

## 38. 告别ArcoLinux大学

**原文标题**: A Farewell to the ArcoLinux University

**原文链接**: [https://www.arcolinux.info/a-farewell-to-the-arcolinux-university/](https://www.arcolinux.info/a-farewell-to-the-arcolinux-university/)

ArcoLinux项目宣告终结

本文宣布ArcoLinux项目将在其创建者奉献八年后结束。由于接近60岁，精力与专注力下降，创建者决定卸任。ArcoLinux被设计为一个教育平台，提供超过5000个视频，ArcoInstall安装器，用于构建自定义ISO的Carli，ALCI（Arch Linux Calamares安装器）以及定制发行版（如ArcoPlasma）。该项目专注于教授Linux原理，鼓励窗口管理器实验，并使用户能够创建软件包并深入研究系统管理。

作者对ArcoLinux的成就和社区感到自豪，但为了保持其质量，决定停止该项目。代码、视频和文档将继续供他人使用。

为了促进平稳过渡，ArcoLinux正在提供过渡软件包，以将现有的ArcoLinux系统转换为Arch Linux安装。这些软件包将删除ArcoLinux品牌，更新pacman配置，并依靠Chaotic-AUR来获得AUR软件包支持。对此过渡的支持将持续到2025年7月1日，之后所有社交媒体渠道将被停用。作者还发布了最终ISO，反映了从ArcoLinux到Arch的转变，以用户而非开发者的身份测试ISO的寿命。作者将亲自离线运行带有Chadwm的ArcoNet，表明用户无需重新安装或切换发行版；他们只需“更新”即可成为Arch Linux。

---

## 39. 使用劣质硬件：我为何在终端工作 (2024)

**原文标题**: Using bad hardware: why I work in the terminal (2024)

**原文链接**: [https://colean.cc/journal/2024/08sep.html](https://colean.cc/journal/2024/08sep.html)

Abbieoverflight 的文章《使用劣质硬件：我为何在终端工作》阐述了如何在低配置电脑上优化编程工作流程。作者详述了使用搭载 Intel Celeron 和 Atom 处理器的机器的个人经验，并认为精心选择的配置可以消除此类硬件的局限性。

该工作流程的核心组成部分包括：

1.  **Linux：** 一个最小化的 Linux 发行版，最好提供“服务器”安装选项。Arch Linux 是作者的选择，因为它拥有软件包管理器 (pacman)、AUR 和全面的文档。
2.  **窗口管理器：** 像 i3wm（作者首选）这样的轻量级窗口管理器，而不是完整的桌面环境。其他选择包括 Fluxbox、fvwm 和 qtile。
3.  **终端和文本编辑器：** 使用基于终端的文本编辑器（例如 Neovim，替代 Nano）以及 Alacritty 终端。这提供了跨不同机器（包括通过 SSH 访问的服务器）一致的编辑体验，并且资源效率高。

作者强调了此设置的可移植性和资源效率。该工作流程使他们能够在各种机器上舒适地工作，包括低配置设备和远程服务器。作者还提倡轻量级依赖编程，进一步缩短编译时间和减少二进制文件大小。最终，这篇文章展示了一种旨在即使在有限的硬件上也能舒适高效地编程的工作流程。

---

## 40. YAML：挪威问题 (2022)

**原文标题**: YAML: The Norway Problem (2022)

**原文链接**: [https://www.bram.us/2022/01/11/yaml-the-norway-problem/](https://www.bram.us/2022/01/11/yaml-the-norway-problem/)

本文重点指出YAML解析中一个重要的陷阱，被称为“挪威问题”。YAML灵活的布尔值解析规则可能导致意想不到的数据类型转换。具体来说，由于YAML布尔值规范中包含了"NO"（挪威的ISO 3166-1 ALPHA-2代码），YAML将其解释为布尔值"false"。

作者通过一个使用`pyyaml`的Python示例演示了这一点，表明包含"NO"的国家列表会导致"NO"被解析为`False`。这说明了YAML自动类型强制转换的更广泛问题，该问题还会影响以“.0”结尾的版本号以及像“Null”这样的姓氏，它们分别被错误地解释为数字和`NULL`。

本文提出了两种解决方案：用双引号转义有问题的数值，或者使用更严格的YAML库，例如Python的StrictYAML，它可以避免这些激进的类型转换，从而确保数据的完整性。作者Bramus强调了YAML默认行为可能带来的意外后果，并提倡在YAML解析过程中更加谨慎地处理数据类型。

---

## 41. 风中之尘：城市如何改变天然空气悬浮颗粒

**原文标题**: Dust in the wind: How cities alter natural airborne particles

**原文链接**: [https://phys.org/news/2025-04-cities-natural-airborne-particles.html](https://phys.org/news/2025-04-cities-natural-airborne-particles.html)

犹他大学发表在《科学报告》上的一篇文章，调查了城市环境如何影响天然空气传播粉尘，尤其是在犹他州瓦萨奇山前地区。研究人员发现，城市粉尘与天然粉尘混合，污染了流域，并可能构成潜在的健康危害。瓦萨奇山前地区是犹他州四分之三人口的所在地，容易受到来自大盐湖等自然源和采石场、采矿作业等人为源的粉尘污染。

由Kevin Perry和Jeff Munroe领导的研究团队分析了从不同地点（包括城市地区和山顶）收集的粉尘样本。与天然粉尘相比，城市粉尘样本显示出更高的锌、钙、钼、镉、铜、铅、钴和砷等金属浓度。一些浓度，特别是砷和钴，超过了美国环保署的标准。这些金属来源于采矿、车辆排放和工业。

受污染的粉尘沉降在积雪上，当积雪融化时，这些金属被带入溪流，最终进入大盐湖，影响水质。该研究强调了了解城市粉尘的来源和成分，以减轻其对环境和健康的负面影响的重要性。

---

## 42. 如何维修联想 Yoga 笔记本电脑 (2019) 中爆炸的部件

**原文标题**: How to repair the parts that explode in Lenovo Yoga laptops (2019)

**原文链接**: [http://adammunich.com/how-to-repair-the-parts-that-explode-in-lenovo-yoga-laptops/](http://adammunich.com/how-to-repair-the-parts-that-explode-in-lenovo-yoga-laptops/)

联想 Yoga 笔记本电脑电源电路设计缺陷：晶体管烧毁导致自毁

---

## 43. 特朗普豁免手机、电脑、芯片的“对等”关税

**原文标题**: Trump exempts phones, computers, chips from ‘reciprocal’ tariffs

**原文链接**: [https://www.bloomberg.com/news/articles/2025-04-12/trump-exempts-phones-computers-chips-from-reciprocal-tariffs](https://www.bloomberg.com/news/articles/2025-04-12/trump-exempts-phones-computers-chips-from-reciprocal-tariffs)

无法访问文章链接。

---

## 44. Artie（YC S23）招聘第三位工程师

**原文标题**: Artie (YC S23) Is Hiring Engineer #3

**原文链接**: [https://www.ycombinator.com/companies/artie/jobs/7kGvDVC-founding-product-engineer](https://www.ycombinator.com/companies/artie/jobs/7kGvDVC-founding-product-engineer)

Artie (YC S23支持的初创公司，使用Kafka和变更数据捕获(CDC)提供实时数据库复制解决方案)正在寻找一位创始产品工程师（3号工程师）加入其位于旧金山的团队。他们的目标是以亚分钟级的延迟解决数据同步难题。该公司拥有8名团队成员和超过100万美元的年度经常性收入(ARR)，并得到Pathlight Ventures、General Catalyst以及Benn Stancil和Lenny Rachitsky等知名投资者的支持。

该职位涉及直接的客户互动、功能开发（例如，列排除、加密、警报）以及改进内部工具。理想的候选人应具有4年以上在初创公司进行Web开发的经验，扎实的计算机科学基础，务实的构建方法，能够胜任全栈职责，并且对用户友好型产品充满热情。首选具备Go语言能力，但不是必需的。

Artie的技术栈包括前端的TypeScript（React和Material UI）和后端的Go、PostgreSQL、Redis、Kafka和Elasticsearch。基础设施通过Terraform、Kubernetes和Helm在GCP和AWS上进行管理。面试流程包括与CTO的电话沟通、技术电话筛选和现场面试。

---

## 45. 微重力101

**原文标题**: Microgravity 101

**原文链接**: [https://sparkgravity.com/journal/microgravity-101/](https://sparkgravity.com/journal/microgravity-101/)

塞巴斯蒂安·古铁雷斯撰写的《微重力101》一文解释了什么是微重力、其重要性以及它如何影响科学研究。微重力被定义为一种重力存在但极其微弱的状态，通常在地球重力的1/1000到1/1,000,000之间。它与理想化的“零重力”不同，国际空间站上的宇航员由于持续自由落体而体验到的是微重力。

这篇文章强调了微重力对流体、细胞、燃烧和晶体形成的独特影响，使其成为进行实验的宝贵环境，这些实验揭示了地球重力掩盖的行为，并创造了新的研究机会。它列出了可以体验微重力的各种平台，包括国际空间站、抛物线飞行、探空火箭、立方体卫星和落塔。

该文澄清了常见的误解，强调重力始终存在，并且微重力显著影响实验结果。最后，它介绍了Spark Gravity对可编程重力的关注，包括0G、部分重力和全重力环境，以使科学家更好地控制研究中的重力变量，并弥合全有或全无重力环境之间的差距。Spark Gravity旨在促进长期研究并模拟像月球或火星这样的环境。文章最后提供了更多资源的链接，并邀请读者订阅以获取最新信息。

---

## 46. 谷歌在人工智能的各个领域都取得了胜利。

**原文标题**: Google is winning on every AI front

**原文链接**: [https://www.thealgorithmicbridge.com/p/google-is-winning-on-every-ai-front](https://www.thealgorithmicbridge.com/p/google-is-winning-on-every-ai-front)

谷歌正主导人工智能领域，竞争对手望尘莫及

---

## 47. 如何构建B2B市场平台

**原文标题**: How to Structure a B2B Marketplace Venture

**原文链接**: [https://sloanreview.mit.edu/article/how-to-structure-a-b2b-marketplace-venture/](https://sloanreview.mit.edu/article/how-to-structure-a-b2b-marketplace-venture/)

本文探讨了B2B交易平台的不同所有权结构及其各自的优缺点。核心问题是公司应将B2B交易平台保留在内部、分拆出去，还是作为纯粹的初创公司推出。

文章重点介绍了三种常见模式：内部部门（占调查交易平台的30%）、公司分拆（19%）和纯粹的初创公司（51%）。内部交易平台受益于母公司的资源、安全性和现有客户群，例如Sysco的在线交易平台。然而，它们存在渠道冲突和蚕食现有销售额的风险。分拆公司可以获得母公司的技术、专业知识和资金，而初创公司则依赖独立投资者，并且通常瞄准高度分散的市场。

最终，最佳结构取决于市场分散程度、独立性的优势以及外部投资者或合作伙伴可以带来的价值等因素。文章强调，这些结构并非静态；交易平台可以从内部部门演变为分拆公司，或被公司收购。Wayne Thompson的评论进一步表明，开放式交易平台可以服务于不同的细分市场，甚至可以创建一个低端交易平台作为防御策略。

---

## 48. 特斯拉发布简配后驱版Cybertruck：性能大减，价格降幅不大

**原文标题**: Tesla Releases Stripped RWD Cybertruck: So Much Worse for Not Much Less Money

**原文链接**: [https://www.jalopnik.com/1832213/tesla-releases-cheaper-rwd-cybertruck/](https://www.jalopnik.com/1832213/tesla-releases-cheaper-rwd-cybertruck/)

特斯拉于2025年4月发布后轮驱动版Cybertruck，旨在提振因召回和未兑现的功能承诺而滞后的销量。这款基本款车型售价71985美元（含目的地费用），仅比双电机四驱版便宜10000美元，但配置大幅缩减。

性能下降，0-60英里加速时间降至6.2秒。续航里程增加至350英里，但配备的是较小且吸引力不足的18英寸轮毂（20英寸轮毂需额外支付3500美元）。牵引力降至7500磅，有效载荷也随之减少。充电速度略有提升，但最大充电功率保持不变。

后驱版Cybertruck取消了许多高端配置。自适应空气悬架被螺旋弹簧系统取代，电动卷帘盖也取消了。货箱缺少地板下储物空间、高级照明、L型轨道和240v/120v电源插座。外观上的降级包括取消标志性前大灯、后灯条、有色玻璃、织物内饰、标准中控台以及通风前排座椅/加热后排座椅。其他省略的功能包括后排乘客显示屏、降级的音响系统、主动降噪、车内120v电源插座和HEPA空气滤清器。

作者认为，这种配置缩减使得后驱版Cybertruck性价比极低，尤其是与价格相似或略高的福特F-150 Lightning、Rivian R1T和雪佛兰Silverado EV等提供双电机驱动的其他电动卡车相比。作者总结道，这款配置缩减的Cybertruck缺乏吸引力，并预测它将因需求低迷而被悄然取消。

---

## 49. 巴黎限制车辆通行后，空气污染显著下降。

**原文标题**: Air pollution fell substantially as Paris restricted car traffic

**原文链接**: [https://www.washingtonpost.com/climate-solutions/2025/04/12/air-pollution-paris-health-cars/](https://www.washingtonpost.com/climate-solutions/2025/04/12/air-pollution-paris-health-cars/)

无法访问文章链接。

---

## 50. 用 Rust 和 WebAssembly 重建 Prime Video UI

**原文标题**: Rebuilding Prime Video UI with Rust and WebAssembly

**原文链接**: [https://www.infoq.com/presentations/prime-video-rust/](https://www.infoq.com/presentations/prime-video-rust/)

Alexandru Ene 探讨了 Prime Video 使用 Rust 和 WebAssembly 重建客厅设备（机顶盒、游戏机、流媒体棒、电视）UI 的历程。挑战在于如何在维护单一应用的同时，兼顾这些设备性能上的巨大差异。 目标是在性能、硬件兼容性和可更新性之间取得平衡。

之前，Prime Video 采用双技术栈：React/JavaScript (TypeScript) 用于业务逻辑，Rust/WebAssembly（以及一些 C++）用于底层 UI 引擎。这种架构虽然实现了频道和直播活动等功能，但由于 JavaScript 的性能限制（尤其是在低端设备上），存在输入延迟的问题。该架构的工作方式是将消息从 React 应用发送到 WebAssembly 引擎来操作场景树。

为了改善输入延迟，他们过渡到完全基于 Rust 的 UI SDK。 这消除了对消息总线的需求，并绕过了 JavaScript 的性能瓶颈。 新的架构包含一个构建在引擎之上的 Rust UI SDK，该引擎处理焦点管理和布局。 他们正在逐页部署这个新系统。

Rust UI SDK 虽然由于生态系统的限制而需要自定义开发，但利用了诸如 signals（灵感来自 Leptos）等概念。 演讲者展示了可运行的 Rust UI 代码，突出了使用 composables 创建可重用 UI 元素。 结果是性能得到了提高，从而实现了以前使用旧技术栈无法实现的功能，例如布局动画和近乎即时的页面过渡。

---

## 51. 阿努比斯工作室

**原文标题**: Anubis Works

**原文链接**: [https://xeiaso.net/notes/2025/anubis-works/](https://xeiaso.net/notes/2025/anubis-works/)

阿努比斯方案：一种保护网站免受AI恶意爬取的技术

“阿努比斯方案”描述了一项网站安全措施，旨在阻止人工智能公司过度抓取网站内容。这种抓取行为会导致服务器停机，并使合法用户无法访问网站。

阿努比斯采用类似于Hashcash的工作量证明（PoW）机制来阻止抓取。对于单个用户来说，PoW的成本可以忽略不计，但对于大规模抓取者来说，成本会变得很高，从而降低这种行为的可行性。

文章强调，阿努比斯方案是一种临时解决方案。长期目标是实施更好的指纹识别技术，以识别和阻止用于抓取的无头浏览器，从而消除合法用户的工作量证明挑战。

该系统需要JavaScript才能运行，因为人工智能公司已经改变了网站托管方式。遇到阿努比斯挑战的用户可能需要禁用JShelter等浏览器扩展，这些扩展可能会干扰所需的JavaScript功能。目前正在开发一种无需JavaScript的解决方案。本质上，阿努比斯是一种权宜之计，用于在开发更复杂的检测方法的同时，保护网站免受恶意抓取。

---

## 52. Show HN: 警方/消防/急救无线电实时突发事件地图

**原文标题**: Show HN: Real-time emergency incident maps from police/fire/EMS radio

**原文链接**: [https://alertpage.ai](https://alertpage.ai)

AlertPage.ai：基于警消急救无线电通讯数据的实时突发事件地图平台

---

## 53. 开源且可自托管/私有的文件转换器

**原文标题**: Open source and self hostable/private file converter

**原文链接**: [https://vert.sh](https://vert.sh)

VERT.sh 是一款开源且可能支持自托管的文件转换器。它强调用户隐私，图像和音频转换直接在用户设备上执行。然而，视频转换默认在VERT.sh服务器上处理，但该页面表明可以设置本地视频转换。

该平台承诺无文件大小限制且无广告。它支持多种媒体类型的各种文件格式：

*   **图像:** .png, .jpeg, .jpg, .webp, .gif, .hdr, .jpe, .mat, .pbm, .pfm, .pgm, .pnm, .ppm, .raw, .tif, .tiff, .jfif
*   **音频:** .mp3, .wav, .flac, .ogg, .aac, .m4a, .wma, .amr, .ac3, .alac, .aiff
*   **文档:** .docx, .doc, .md, .html, .rtf, .csv, .tsv, .json, .rst, .epub, .odt, .docbook
*   **视频:** .mkv, .mp4, .webm, .avi, .wmv, .mov, .gif, .mts

视频转换方面被标记为“就绪”，而图像、音频和文档转换的状态则被标记为“未就绪”，这表明这些功能可能正在开发中或在访问时未完全正常运行。

---

## 54. 谷歌将允许企业在自家数据中心运行 Gemini 模型。

**原文标题**: Google will let companies run Gemini models in their own data centers

**原文链接**: [https://www.cnbc.com/2025/04/09/google-will-let-companies-run-gemini-models-in-their-own-data-centers.html](https://www.cnbc.com/2025/04/09/google-will-let-companies-run-gemini-models-in-their-own-data-centers.html)

谷歌云将允许企业自第三季度起通过Google Distributed Cloud在其自身数据中心运行Gemini AI模型。这使客户在利用谷歌AI技术的同时，能够掌控自己的数据。英伟达也将把Gemini模型引入其Blackwell GPU，这些GPU可通过谷歌或其他渠道购买。

此举使谷歌区别于OpenAI和Anthropic等竞争对手，后者因担心质量和控制问题，尚未将其模型开放给物理数据中心。谷歌旨在吸引那些倾向于维护自身硬件的组织，包括那些具有严格安全要求的组织。一个气隙隔离版的Google Distributed Cloud甚至将允许美国政府机密用户使用Gemini。

谷歌云首席执行官Thomas Kurian强调，公司对多云的承诺和对AI的投资是客户增长的驱动因素，尤其是在以320亿美元收购云安全初创公司Wiz之后。Gemini模型支持100多种语言的文本、音频和视频处理。据Gartner称，云基础设施市场规模庞大，2023年谷歌占8%，而亚马逊占39%，微软占23%。

---

## 55. 欧洲正试图摆脱星链。

**原文标题**: Europe is trying to leave Starlink behind

**原文链接**: [https://www.wsj.com/world/europe/europe-eutelsat-elon-musk-starlink-c283c4c8](https://www.wsj.com/world/europe/europe-eutelsat-elon-musk-starlink-c283c4c8)

无法访问文章链接。

---

## 56. 中国批准无人驾驶飞行出租车

**原文标题**: China just approved flying taxis – no pilot needed

**原文链接**: [https://engineerine.com/chinas-flying-taxis/](https://engineerine.com/chinas-flying-taxis/)

中国批准首款载人商业运营飞行出租车，欲引领自动空中交通。中国民用航空局已向亿航智能颁发航空运营许可证，允许其开始运营。这款双座电动飞机配备 16 个螺旋桨，时速可达 81 英里，单次充电可飞行 22 英里，载重可达 485 磅。初期将用于短途旅游航线，最终扩展到城市和城际旅行。

虽然是无人驾驶，但这些飞行出租车受到地面控制中心的监控，并遵守严格的安全规定。车辆充电需要两个小时，未来计划包括电池更换站和太阳能充电。采用电力推进为传统交通提供了可持续的替代方案，城市规划者正在开发垂直起降机场和数字空中交通管制系统。

公众反应积极，预计此举将影响全球监管机构，并可能引发对城市空中交通（UAM）的投资。分析师预测，到 2040 年，UAM 市场将超过 1 万亿美元，而中国将处于领先地位。先进的人工智能、通信系统和传感器确保飞行安全。亿航的目标是在全球范围内出口该型号，目前正在与迪拜、新加坡和洛杉矶进行讨论。这一发展代表着在减少交通拥堵和改变城市通勤方面迈出了重要一步。

---

## 57. 在波特兰，教师缺勤情况比以往任何时候都更严重

**原文标题**: In Portland, teachers are missing more school than ever

**原文链接**: [https://www.oregonlive.com/education/2025/04/in-and-around-portland-teachers-are-missing-more-school-than-ever-their-bosses-dont-want-to-talk-about-it.html](https://www.oregonlive.com/education/2025/04/in-and-around-portland-teachers-are-missing-more-school-than-ever-their-bosses-dont-want-to-talk-about-it.html)

俄勒冈州波特兰地区教师缺勤率上升：一个值得关注的趋势

---

## 58. Go 语言的通道很糟糕 (2016)

**原文标题**: Go channels are bad (2016)

**原文链接**: [https://www.jtolio.com/2016/03/go-channels-are-bad-and-you-should-feel-bad/](https://www.jtolio.com/2016/03/go-channels-are-bad-and-you-should-feel-bad/)

Jtolio的文章《Go Channels很糟糕》认为，Go的channel实现虽然根植于理论上可靠的通信顺序进程（CSP）模型，但在实践中存在缺陷，并且常常是一种反模式。

作者认为channels被过度使用，并且不是解决许多并发问题的最佳方案。他的观点如下：

*   **Channels并非总是足够：** 现实世界的Go程序经常需要互斥锁、信号量和条件变量与channels一起使用，从而破坏了纯粹CSP“通过通信共享内存”的理想。这使得推理并发性变得更加困难。
*   **Channels可能更慢：** 基准测试表明，由于底层的锁机制，channels可能比直接使用互斥锁和条件变量慢得多。
*   **Channels组合性不好：** channel发送的阻塞性使得它们与其他并发原语（如互斥锁）一起使用时变得复杂，可能导致死锁。非阻塞发送需要冗长的`select`语句。
*   **回调函数更强大：** 使用channels的API通常会强制创建不必要的goroutine。基于回调的API通常更灵活、资源效率更高，允许在需要时使用channels，而不会强制使用它。作者提供了一个重构`context.Done()`以使用回调来避免goroutine泄漏的示例。
*   **Channel API的不一致性：** 关闭或向关闭的channel发送数据会导致panic，需要外部同步并增加复杂性。

总之，作者认为Go程序员过度依赖channels，往往以牺牲性能、简单性和可组合性为代价。他建议考虑使用传统的同步原语和基于回调的API，以获得更高效、更灵活的并发解决方案。

---

## 59. TTRPG 必读书单

**原文标题**: The Essential Reading List for TTRPGs

**原文链接**: [https://thealexandrian.net/wordpress/52329/roleplaying-games/rpgs-the-essential-reading-list](https://thealexandrian.net/wordpress/52329/roleplaying-games/rpgs-the-essential-reading-list)

本文概述了一门入门级角色扮演游戏设计课程的假想大学阅读书目。作者设想这门课程是对RPG历史和设计原则的概览。课程的核心围绕分析关键RPG及其对行业的影响展开。

阅读书目包括：

*   **1974版《龙与地下城》:** 奠基之作，展示了RPG的起源。
*   **《旅行者》:** 早期科幻RPG和人生轨迹角色创建的范例。
*   **《通用无限制角色扮演系统/冠军》:** 体现了“精确模拟”的设计趋势和点数购买角色创建。
*   **《偏执狂》（第一版）:** 突出了创造性议程的多样化以及模拟的荒谬应用。
*   **《吸血鬼：避世》:** 一次至关重要的尝试，将创造性议程置于模拟之上。
*   **《琥珀无骰角色扮演》:** 对复杂性的一种反击，专注于为设定量身定制的机制。
*   **《燃烧之轮》:** 对Forge时代独立游戏界创新的综合，与GNS理论相关。
*   **《末日世界》:** 代表了有影响力的“末日引擎驱动”系统以及D. Vincent Baker的设计理念。
*   **《龙与地下城》3E、4E、5E:** 用于分析《龙与地下城》如何对行业趋势做出反应和反映行业趋势。

作者还承认了诸如FATE、故事叙述游戏、盒装RPG、新手套装、基于组织的游戏和《克苏鲁的呼唤》等值得注意的遗漏，并解释了为什么这些内容尽管重要，却没有被包括在内。该列表试图在历史意义与用于教授设计原则的说明性价值之间取得平衡。

---

## 60. 适用于Commodore电脑的33岁AmigaOS系统迎来意外更新 新闻

**原文标题**: 33-year-old AmigaOS for Commodore computers gets an unexpected update News

**原文链接**: [https://www.tomshardware.com/software/operating-systems/33-year-old-amigaos-for-commodore-computers-gets-an-unexpected-update](https://www.tomshardware.com/software/operating-systems/33-year-old-amigaos-for-commodore-computers-gets-an-unexpected-update)

本文报道了经典Commodore电脑操作系统AmigaOS出人意料的持续发展。当前的管理方Hyperion Entertainment最近发布了AmigaOS 3.2.3，该更新包含50多项修复和增强，基于始于2021年的AmigaOS 3.2系列。AmigaOS 3.0最初由Commodore于1992年发布。

3.2.3版本的主要更新包括改进了ReAction（该操作系统的面向对象GUI工具包），允许在TextEditor中使用带有宏的自定义菜单，释放了12KB的芯片RAM，以及新的Kickstart 3.2.3 ROM。该更新还包含许多其他修复，包括DiskDoctor和HDToolbox的更新。

本文简要介绍了Commodore于1994年倒闭后AmigaOS开发的支离破碎的历史，导致了基于PowerPC的AmigaOS 4.X版本的发布，以及其他受Amiga启发的操作系统，如MorphOS和AROS。

AmigaOS 3.2.3是现有3.2用户的免费更新，可通过官方经销商获得。本文还指出，基于Arm的加速器越来越受到现代Amiga爱好者的欢迎，AmigaOS 3.2.3支持带有此类加速器的经典Amiga。最后，本文提到了一款延迟发布的“新型全尺寸Amiga游戏机”以及Hyperion愿意讨论其软件/操作系统。

---

## 61. Apache ECharts + Leaflet + shadcn 数据可视化

**原文标题**: Apache ECharts + Leaflet + shadcn for data viz

**原文链接**: [https://docs.evidence.dev/components/all-components/](https://docs.evidence.dev/components/all-components/)

本文重点介绍 Evidence，一个使用 Markdown 和 SQL 生成报告的库，并强调其数据可视化功能。它利用 Apache ECharts 创建各种交互式图表，并利用 Leaflet 实现地图功能。用户界面采用 Shadcn 组件构建。

本文展示了通过 ECharts 集成提供的各种图表类型，包括折线图（单系列和多系列，多 Y 轴列）、面积图（标准、堆叠、100% 堆叠）、柱状图（各种配置，如堆叠、分组、水平变化）、散点图（单系列和多系列）、气泡图、漏斗图、桑基图、热图（包括日历热图）、直方图和箱线图。还演示了混合型图表（柱状图和折线图组合）和注释功能（参考线和参考区域）。进一步强调了自定义 ECharts 实现的能力，包括树状图、饼图和甜甜圈图以及高级示例。

除了图表，本文还介绍了 Evidence 由 Shadcn 提供的 UI 元素。这些包括输入组件（按钮组、下拉菜单、文本输入、日期范围）、布局工具（维度网格、网格、模态框、选项卡）和通用 UI（手风琴、警报、详细信息）。

由 Leaflet 提供支持的地图功能包括区域地图、点地图、气泡地图和底图，并特别提到了对美国地图的支持。最后，它邀请用户试用 Evidence Cloud (Beta)。

---

## 62. 我们一直都误解了多动症吗？

**原文标题**: Have We Been Thinking About A.D.H.D. All Wrong?

**原文链接**: [https://www.nytimes.com/2025/04/13/magazine/adhd-medication-treatment-research.html](https://www.nytimes.com/2025/04/13/magazine/adhd-medication-treatment-research.html)

本文预览探讨了围绕多动症出现的新问题，尤其是在诊断和治疗方面。文章重点介绍20世纪90年代初，多动症诊断和利他林处方迅速增加的时期，这引发了辩论和质疑，甚至引来了像科学教这样的团体的抗议。

文章聚焦于研究心理学家詹姆斯·斯旺森，他最初认为诊断率是准确的，但后来意识到人们对多动症缺乏全面的科学理解，以及像利他林这样的兴奋剂药物的长期影响。这促使了一项名为“多动症多模式治疗研究”（M.T.A.）的大规模研究。

M.T.A.是一项多中心随机对照试验，比较了兴奋剂药物、行为训练、两者结合以及对7-9岁被诊断患有多动症症状的儿童不进行任何特定治疗的效果。目的是了解不同方法的有效性以及利他林的长期影响。文章的预览在揭示研究结果之前戛然而止，但提出了这样一种观点：即已确立的多动症临床定义可能与科学发现脱节。

---

## 63. 配置语言的层级

**原文标题**: Levels of configuration languages

**原文链接**: [https://beza1e1.tuxen.de/config_levels.html](https://beza1e1.tuxen.de/config_levels.html)

本文概述了五种配置语言级别，从简单到复杂，并主张选择满足项目需求的最简单级别。

**第一级：文件中的字符串：** 最简单的方法，将文件视为键值存储。例如 Linux 的 procfs 和 sysfs。

**第二级：列表：** 文件包含列表，可能包含键值对和节（如 INI 文件）。 这提供稍微更多的表达能力，但受到无法嵌套列表的限制。

**第三级：嵌套数据结构：** 流行的格式，如 JSON、YAML、XML 和 TOML。 这些允许嵌套数据结构，但缺乏计算能力，通常导致在数据文件中添加有问题的代码片段。

**第四级：完整的编程语言：** 不太常见但可能强大的语言，允许计算但保证终止。例如 XSLT、Jsonnet 和 Dhall。 一个缺点是工具有限。

**第五级：完整的编程语言：** 利用通用脚本语言，如 Python 或 Lua。 提供最大的灵活性，但可能导致循环依赖和复杂的配置逻辑。

作者提倡使用尽可能低的级别以保持简单性，并警告不要在单个级别内进行广泛的辩论（例如，JSON 与 YAML），因为它们的差异通常可以忽略不计。 他总结说，这是一种在简单性和未来需求之间的平衡。

---

## 64. Shadertoys移植到Rust GPU

**原文标题**: Shadertoys Ported to Rust GPU

**原文链接**: [https://rust-gpu.github.io/blog/2025/04/10/shadertoys/](https://rust-gpu.github.io/blog/2025/04/10/shadertoys/)

本文讨论了如何使用 Rust GPU 将 Shadertoy shaders 移植到 Rust，Rust GPU 是一个允许用 Rust 编写 GPU 代码的项目。 Rust GPU 使用 Rust 来编写 shaders，而不是使用像 WGSL、GLSL、MSL 或 HLSL 这样的专用语言，然后将 shaders 编译成与 Vulkan 兼容的 SPIR-V 格式。

作者重点介绍了使用 Rust GPU 的优点，包括使用 `bytemuck` crate 在 CPU 和 GPU 之间无缝共享数据，这使得可以共享用 `#[repr(C)]` 定义的数据结构而无需修改。他们还展示了 Rust 的 traits、泛型和宏等特性在代码重用和减少重复代码方面的有效使用。

提到的一个关键优势是能够使用标准的 Rust 工具（如 `cargo check`、`cargo build` 和 `cargo run --release`）进行 shader 开发。 这简化了开发过程并利用了现有的 Rust 专业知识。

此外，作者强调了他们通过识别和修复 `wgpu` 和 `naga` 中的问题，从而为 Rust 生态系统做出的贡献，这使这些库的所有用户受益。

总而言之，本文将 Rust GPU 介绍为 shader 开发的可行选择，强调了它的易用性、与现有 Rust 工具的集成以及使用 Rust 高级特性所带来的好处。 它鼓励用户尝试 Rust GPU，并邀请大家为该项目做出贡献，同时提到了即将到来的入门和文档改进。

---

## 65. 学习汇编：为了乐趣、性能和收益

**原文标题**: Learning Assembly for Fun, Performance and Profit

**原文链接**: [https://thechipletter.substack.com/p/learning-assembly-for-fun-and-profit](https://thechipletter.substack.com/p/learning-assembly-for-fun-and-profit)

无法访问文章链接。

---

## 66. 西雅图半数男性为未婚单身，人口普查数据显示

**原文标题**: Half the men in Seattle are never-married singles, census data shows

**原文链接**: [https://www.seattletimes.com/seattle-news/data/half-the-men-in-seattle-are-never-married-singles-for-the-first-time/](https://www.seattletimes.com/seattle-news/data/half-the-men-in-seattle-are-never-married-singles-for-the-first-time/)

以下是基于《西雅图时报》文章标题的摘要：

文章报道，根据最近的人口普查数据，西雅图首次出现一半男性为从未结婚的单身人士。这表明该城市的人口结构发生了重大转变。文章可能探讨了这一趋势的原因，我们可以根据常见的社会趋势推断出一些潜在因素，包括：

*   **婚姻延迟：** 男性（和女性）的结婚年龄推迟，在安定下来之前专注于职业发展、教育和个人目标。
*   **经济因素：** 西雅图高昂的生活成本，尤其是住房，可能使一些男性更难实现结婚和组建家庭。
*   **职业重心：** 西雅图蓬勃发展的科技产业可能会吸引那些高度专注于自己事业的人，从而推迟或放弃婚姻。
*   **生活方式选择：** 有些男性可能仅仅是更喜欢单身生活方式，选择不结婚。
*   **性别比例失衡：** 西雅图男性与女性比例可能存在的失衡可能导致单身男性比例偏高。 但是，在没有阅读全文的情况下，这只是一种推测。

文章可能还会进一步分析这些单身男性的年龄分布、就业状况，或许还会将这一趋势与其他主要城市进行比较。它可能还会探讨西雅图这一人口结构转变的潜在社会和经济影响。

---

## 67. Show HN: 我做了个YC拒绝模拟器

**原文标题**: Show HN: I Made YC Rejection Simulator

**原文链接**: [https://yc-sim.vercel.app/](https://yc-sim.vercel.app/)

YC拒绝模拟器

---

## 68. 为何教育不平等在家庭中代代相传：基因的影响大于环境

**原文标题**: Why educational inequality runs in families: Genetics more than environment

**原文链接**: [https://osf.io/preprints/psyarxiv/rehdj_v1](https://osf.io/preprints/psyarxiv/rehdj_v1)

对不起，我没有足够的信息来提供文章的简明摘要。 提供的内容仅是带有JavaScript指令的网站标题，没有实际的文章文本。 我需要文章的内容才能准确总结其要点以及有关教育不平等以及遗传和环境作用的关键信息。

---

## 69. Zod v4 Beta

**原文标题**: Zod v4 Beta

**原文链接**: [https://v4.zod.dev/v4](https://v4.zod.dev/v4)

Zod v4 beta 发布，带来性能提升、更小体积和更好的 TypeScript 集成。安装方式：`pnpm upgrade zod@next`。

**主要改进：**

*   **性能：** 显著提升字符串、数组和对象解析速度，并减少 TypeScript 实例化。
*   **体积：** 核心体积减少 57%。`@zod/mini` 提供函数式 API，可实现更小体积（相比 Zod 3 减少 6.6 倍）。
*   **TypeScript：** 简化泛型，避免“实例化爆炸”，提升编辑器处理复杂 schema 的性能。
*   **元数据：** 引入新的元数据系统，使用 `z.registry()` 和 `z.globalRegistry` 进行强类型 schema 注解，兼容 JSON Schema。优先使用 `.meta()` 代替 `.describe()`。
*   **JSON Schema 转换：** 通过 `z.toJSONSchema()` 提供官方 JSON Schema 转换。
*   **`z.interface()`：** 用于定义对象类型的新 API，可精确控制可选属性（键与值可选性），并使用 getter 实现真正的递归类型，用于循环属性。仍然支持 `z.object()`。
*   **文件 Schema：** 验证 File 实例的大小和 MIME 类型约束。

---

## 70. 一个代号“小丑”的神秘赌徒赢走了德州彩票。

**原文标题**: A Secretive Gambler Called 'The Joker' Took Down the Texas Lottery

**原文链接**: [https://www.wsj.com/us-news/texas-lottery-gamblers-jackpot-win-40e3d6fb](https://www.wsj.com/us-news/texas-lottery-gamblers-jackpot-win-40e3d6fb)

无法访问文章链接。

---

## 71. 一个代号“小丑”的神秘赌徒赢走了德州彩票。

**原文标题**: A Secretive Gambler Called 'The Joker' Took Down the Texas Lottery

**原文链接**: [https://www.wsj.com/us-news/texas-lottery-gamblers-jackpot-win-40e3d6fb](https://www.wsj.com/us-news/texas-lottery-gamblers-jackpot-win-40e3d6fb)

无法访问文章链接。

---

## 72. 过去百万年来猛犸象的基因多样性

**原文标题**: Mammoth genetic diversity throughout the last million years

**原文链接**: [https://www.sciencedaily.com/releases/2025/04/250409114704.htm](https://www.sciencedaily.com/releases/2025/04/250409114704.htm)

无法访问文章链接。

---

## 73. 拱心石输油管道泄漏，估计约3500桶原油

**原文标题**: Keystone Pipeline spills estimated 3,500 barrels of crude oil

**原文链接**: [https://www.cbsnews.com/news/keystone-oil-pipeline-shut-down-spill-cleanup-crude-oil/](https://www.cbsnews.com/news/keystone-oil-pipeline-shut-down-spill-cleanup-crude-oil/)

2025年4月8日星期二，据估计，基石输油管道向北达科他州兰森堡附近的一片农田泄漏了约3500桶原油，此前一名员工听到“机械撞击声”。自2024年起成为该管道运营商的South Bow公司检测到压力下降并关闭了系统。截至周四，约700桶（20%）泄漏的原油已被回收。

此次泄漏发生在171英里标记处的一个泵站以南。虽然官员最初报告说附近的一条小溪未受影响，但此后已被隔离。超过200名人员正在现场进行清理和修复。空气质量监测未显示任何不利的健康问题。

基石输油管道于2011年开始运营，将原油从加拿大输送到伊利诺伊州和俄克拉荷马州的炼油厂。 这并非首次事故；自2017年以来，该管道至少发生了三起重大泄漏事故，其中包括2022年发生在堪萨斯州的14000桶泄漏事故。

South Bow公司正在与管道和危险材料安全管理局以及北达科他州环境质量部合作进行清理和调查。 该管道仍然关闭，未经监管部门批准，服务不会恢复。 泄漏原因仍在调查中。

---

## 74. iOS 18.4 上的环境音乐及回归 Apple Music 应用

**原文标题**: Ambient music on iOS 18.4 and the return to the Apple's Music app

**原文链接**: [https://manualdousuario.net/en/ambient-music-ios-18-4/](https://manualdousuario.net/en/ambient-music-ios-18-4/)

无法访问文章链接。

---

## 75. 一个漏洞不够：通过SAP的Setuid环境双重提权

**原文标题**: One Bug Wasn't Enough: Escalating Twice Through SAP's Setuid Landscape

**原文链接**: [https://www.anvilsecure.com/blog/one-bug-wasnt-enough-escalating-twice-through-saps-setuid-landscape.html](https://www.anvilsecure.com/blog/one-bug-wasnt-enough-escalating-twice-through-saps-setuid-landscape.html)

Tao Sauvage 详述了他们在 SAP setuid 二进制文件中发现两个本地提权漏洞 (CVE-2024-47595) 的过程，超越了其 CTO 之前的发现。目标环境是客户使用的 SAP 软件，目标是将权限从 'sapsys' 用户提升到 'root'。

侦察阶段确定了潜在目标：`hostexecstart`、`sapuxuserchk` 和 `icmbnd`。作者排除了之前被利用或被 CVE 覆盖的二进制文件，专注于 `icmbnd` 和 `hostexecstart`。

`icmbnd` 允许任意文件覆盖，原因是跟踪文件选项的参数验证不足。通过向 `/etc/passwd` 中注入新行，将 hxeadm 用户的组 ID 修改为 root，从而实现提权。

`hostexecstart` 用于使用 SAR 存档升级 SAPHostAgent，证明更具挑战性。作者探索了操纵存档路径以将参数注入 SAPCAR 命令。虽然研究了自定义安全库和签署 SAR 存档等选项，但最终都未成功。作者无法签署 SAR 存档，因为它需要 SAP 信任的 CA。

最后，文章提到作者创建了一个 Python 工具 SAPCARve，用于解析和操作 SAR 存档，因为现有工具不足以满足需求。

---

## 76. P2Panda: 点对点应用构建基石

**原文标题**: P2Panda: Building blocks for peer-to-peer applications

**原文链接**: [https://p2panda.org/](https://p2panda.org/)

P2Panda 是一组模块化的 Rust crate，旨在促进现代、尊重隐私且安全的本地优先点对点应用的开发。它强调互操作性，并通过提供可与现有数据类型和 CRDT 集成的灵活组件来避免框架锁定。该项目利用 BLAKE3、Ed25519 和 UCAN 等既定标准，并专注于具有弹性的协作、加密和访问控制解决方案，即使在连接不稳定的情况下也是如此。

p2panda 的一个关键特性是其“仅广播”核心，使其与各种通信基础设施兼容，包括低带宽选项。它积极参与研究、协议设计、赠款申请、社区活动和应用程序开发。

主要库包括：`p2panda-net` (对等发现和连接)、`p2panda-discovery` (对等查找)、`p2panda-sync` (状态同步)、`p2panda-blobs` (大文件传输)、`p2panda-core` (数据类型)、`p2panda-store` (数据存储) 和 `p2panda-stream` (数据处理)。正在进行中的工作包括 `p2panda-node`、`p2panda-caps` 和 `p2panda-group`。

最近的新闻重点介绍了事件流、本地优先加密和离线优先网络支持方面的进展。

一些项目使用 p2panda 构建，包括 Aardvark (协作文本编辑器)、Toolkitty (协调工具包)、Meli Bees App (蜜蜂观测应用程序)、rhio (消息路由器和文件同步) 和 aquadoggo (节点实现)。

---

## 77. 数字与独角兽

**原文标题**: Numbers and Unicorns

**原文链接**: [https://freedommathdance.blogspot.com/2025/01/on-numbers-and-unicorns.html](https://freedommathdance.blogspot.com/2025/01/on-numbers-and-unicorns.html)

安托万·尚贝尔-洛伊尔的博文“数字与独角兽”受一本数学哲学书籍的启发，探讨了关于存在，特别是关于数字和独角兽的哲学问题。他展示了一个 Mastodon 投票，揭示了人们对这些概念的存在与否的不同看法。

文章随后深入探讨了数字的历史存在，引用了巴比伦的泥板、毕达哥拉斯三元组和欧几里得的著作。它说明了数字在贸易、计算（computus）以及最终的数字时代所发挥的根本作用。与此同时，它承认独角兽在神话、艺术（挂毯）和文学中的存在，并提到了翁贝托·埃科。

尚贝尔-洛伊尔探讨了一种观点，即数字对现代世界的影响可能比独角兽更大，它渗透到从基本贸易到复杂的科学、政治和排名系统的一切事物中，游泳记录的比喻就证明了这一点。

作者最喜欢的论点是，数字和独角兽都没有实际意义上的“存在”。他引用了克罗内克的关于整数的引言，并质疑这些东西是否存在于与物理物质相同的方式中。他讨论了 ZFC 公理以及可能存在的矛盾，而这些矛盾并没有对我们的日常使用造成干扰。最后，作者得出结论，数字或独角兽是否存在并不重要，重要的是我们有一种语言来谈论它们，而这才是最重要的。

---

## 78. Sphere即将推出的《绿野仙踪》体验背后的AI魔法

**原文标题**: The AI magic behind Sphere's upcoming 'The Wizard of Oz' experience

**原文链接**: [https://blog.google/products/google-cloud/sphere-wizard-of-oz/](https://blog.google/products/google-cloud/sphere-wizard-of-oz/)

本文详细介绍了在拉斯维加斯Sphere场馆重塑《绿野仙踪》的宏伟项目，该项目采用了谷歌DeepMind和谷歌云的前沿人工智能技术。目标是在忠于1939年经典作品的同时，创造一种沉浸式感官体验，环绕这个拥有17600个座位的场馆。

团队面临着将原始粗糙的35毫米胶片升级到Sphere巨大的16K LED屏幕上的挑战。他们正在利用人工智能媒体模型，特别是Imagen和Veo的微调版本，以及Gemini来实现这一目标。这些工具用于“超分辨率”以增强图像质量，“外绘”以扩展场景并填补由相机切换造成的空白，以及“性能生成”以将原始表演无缝集成到扩展的环境中。

研究人员收集了大量补充材料，包括拍摄剧本、制作插图和场景设计图，以使用原始角色和环境的特定细节来微调人工智能模型。这使得人工智能能够生成超逼真的细节，而这些细节用传统的CGI很难实现。该项目涉及谷歌、Sphere Studios、Magnopus、华纳兄弟探索和视觉特效艺术家的合作。《绿野仙踪Sphere奇观》计划于8月28日首映。

---

## 79. 泄露数据揭示以色列政府发起行动，要求Meta移除支持巴勒斯坦的帖子

**原文标题**: Leaked data reveals Israeli govt campaign to remove pro-Palestine posts on Meta

**原文链接**: [https://www.dropsitenews.com/p/leaked-data-israeli-censorship-meta](https://www.dropsitenews.com/p/leaked-data-israeli-censorship-meta)

基于泄露的Meta数据的“投放点新闻”调查显示，以色列政府发起大规模行动，审查脸书和Instagram上支持巴勒斯坦的内容。据报道，自2023年10月7日以来，Meta已遵从了以色列94%的删除请求，使以色列成为全球此类请求的最大来源国。平均每30秒内有超过9万个帖子被删除，另有3880万个帖子因扩大自动删除范围而被“采取行动”（删除、禁止或压制）。

10月7日之后，所有以色列的删除请求都使用相同的样板语言，无论内容的具体性质如何，都声称违反了以色列的反恐和隐私法。Meta优先处理政府请求，经常绕过人工审核，并将结果反馈到其人工智能审核系统中。

该报告指出，Meta的领导层，包括前以色列军方官员盖伊·罗森和前本雅明·内塔尼亚胡顾问约达娜·卡特勒，担任的职位有利于这种审查。卡特勒甚至积极标记支持巴勒斯坦的内容，即使是与加桑·卡纳法尼等历史人物相关的内容。

该行动不成比例地针对阿拉伯和穆斯林占多数的国家的用户，只有一小部分删除请求针对以色列用户。人权观察组织和Meta内部审查证实了对支持巴勒斯坦内容的过度执行。尽管意识到了这个问题，Meta仍被指控纵容了以色列政府的大规模审查行动。

---

## 80. AI编码与花生酱果酱问题

**原文标题**: AI coding and the peanut butter and jelly problem

**原文链接**: [https://iamcharliegraham.substack.com/p/ai-coding-and-the-peanut-butter-and](https://iamcharliegraham.substack.com/p/ai-coding-and-the-peanut-butter-and)

无法访问文章链接。

---

## 81. PDP-8 相关

**原文标题**: PDP-8 Stuff

**原文链接**: [https://so-much-stuff.com/pdp8/index.php](https://so-much-stuff.com/pdp8/index.php)

PDP-8资料：本网站是Vince Slyngstad的个人网站，致力于记录作者对20世纪60年代和70年代数字设备公司（DEC）PDP-8小型计算机的业余研究。Slyngstad旨在记录其PDP-8相关项目和资源，希望能帮助其他收藏家和修复者。

网站提供了一系列链接，涵盖PDP-8系统及相关设备的各个方面，包括具体的PDP-8型号（8L、8a、8e、8i、8s）、外围设备（RK05、RL02、RX02、TU10、TU55、TU56、LA36、PC04）、相关计算机（Decmate I、II、III、SBC6120）、组件和接口（Omnibus、Flipchip、TTY卡）、开发工具（CAD）和软件资源。此外，还有“FPGA8i”和“df32emul”（DF32模拟器）等项目页面以及文档。总而言之，该网站为Slyngstad的PDP-8项目以及PDP-8社区的资源提供了一个中心枢纽。

---

## 82. C++：更精简的Lambda == SHORTY (滥用？)

**原文标题**: C++: terser (shorter) lambda == SHORTY (ab-use?)

**原文链接**: [https://github.com/hanickadot/shorty](https://github.com/hanickadot/shorty)

"SHORTY" C++库为lambda表达式提供了一种更简洁的语法，旨在提高简洁性，而非用DSL替代C++。它为常用的lambda操作和参数访问引入了简短的别名。

主要特性包括：

*   **简化排序：** 使用 `$lhs` 和 `$rhs` 作为比较参数，无需记忆 `std::less` 与 `std::greater` 的区别。
*   **简洁的过滤和转换：** 与 `std::views` 无缝集成，允许使用诸如 `($i % 2) == 0` 这样的简短表达式来过滤偶数。
*   **外部函数调用：** 使用 `$<>` 或 `$call<>` 调用外部函数，例如 `$<sqrt>($a * $a + $b * $b)`。
*   **类型转换：** 使用 `$<>` 或 `$cast<>` 进行静态转换，例如 `$<int>($0)`。
*   **参数访问：** 提供多种参数访问方法：`$0`-$9`，`$arg<N>`，`$lhs`，`$rhs`，`$it`，`$a`-$f`，`$x`，`$y`，`$z`，`$i`，`$n`，`$k`，`$in`。它会自动解包单参数lambda的元组式参数。
*   **参数信息：** `$argc` 提供参数数量，`$args` 提供所有参数作为元组。
*   **捕获：** 提供按引用捕获（`$(v)` 或 `$ref(v)`）、按值捕获（`$value(v)`、`$val(v)`、`$copy(v)`）以及按CNTPT捕获（`$fixed<v>`、`$const<v>`）。
*   **元组创建：** 使用 `($a, $b, $c)` 或 `($0, $1)` 简化元组创建。
*   **赋值运算符：** 支持赋值运算符，例如 `$a += 2`。

该库旨在减少与标准C++ lambda相关的样板代码，使代码更具可读性和简洁性。

---

## 83. 使用重心坐标在四边形上进行双线性插值

**原文标题**: Bilinear interpolation on a quadrilateral using Barycentric coordinates

**原文链接**: [https://gpuopen.com/learn/bilinear-interpolation-quadrilateral-barycentric-coordinates/](https://gpuopen.com/learn/bilinear-interpolation-quadrilateral-barycentric-coordinates/)

此公告重点介绍了AgilitySDK预览版1.716.0的发布，该版本支持新的Microsoft DirectX和视频编码功能。 简而言之，使用AgilitySDK的开发者现在可以访问和利用与DirectX和视频编码相关的最新功能。 此版本侧重于扩展开发者在其应用程序中进行图形和视频处理的可用功能。 在没有关于特定新功能的更多细节的情况下，该公告主要用于通知用户AgilitySDK已更新，以包含这两个关键领域（DirectX和视频编码）中的较新技术。 用户需要下载AgilitySDK预览版1.716.0才能利用这些新功能。

---

## 84. Amiga双启动ROM替换

**原文标题**: Dual Kickstart ROM Replacement for Amiga

**原文链接**: [https://github.com/cdhooper/kicksmash32](https://github.com/cdhooper/kicksmash32)

KickSmash32是一个开源的Kickstart ROM替换模块，主要为Amiga 3000和Amiga 4000设计，也提供适用于Amiga 1200、3000T、4000T和4000CR型号的版本。它允许用户存储和切换多个Kickstart ROM镜像，通过Amiga命令行实用程序`smash`提供系统内编程，并通过Linux实用程序`hostsmash`提供系统外编程(USB-C)。

主要功能包括支持多达8个独立的闪存库，可配置的ROM库在重启或开机时切换，以及可选的主机文件服务（`smashfs`和`smashftp`），允许从主机PC传输文件和挂载卷。包含一个ROM切换器模块（适用于Kickstart 3.1.4+），使用户能够在启动时选择要使用的ROM镜像。

`doc`目录下提供了全面的文档，涵盖硬件构建、编程、安装、软件构建和安装，以及`hostsmash`、`smash`、`smashfs`和`smashftp`实用程序的用法指南。该文档还有助于用户确定适合其特定Amiga型号的正确KickSmash版本。

---

## 85. 金星地表照片全集（2021年）

**原文标题**: Every picture from Venus' surface, ever (2021)

**原文链接**: [https://www.planetary.org/articles/every-picture-from-venus-surface-ever](https://www.planetary.org/articles/every-picture-from-venus-surface-ever)

金星地表的所有照片

本文题为“金星地表的所有照片”，展示了有史以来从金星表面捕捉到的唯一图像。这些图像由苏联的四个金星探测器于1975年和1982年拍摄。由于金星上的极端高温和高压，这些着陆器寿命极短。金星探测器扫描了金星表面，创建了全景图像，揭示了黄色的天空和荒凉、龟裂的景观。

本文重点介绍了泰德·斯特里克的工作，他是一位哲学教授，专门从事早期太空任务图像的重建。他与俄罗斯科学院的数据合作，创造了原始金星全景图像的最佳版本。

本文展示了金星探测器拍摄的六张全景图像：金星9号（1975年）、金星10号（1975年）、金星13号（前后摄像头，1982年）和金星14号（前后摄像头，1982年）。它将金星描绘成一个潜在的、曾经类似地球的世界，经历了灾难性的气候变化。文章还包括行动号召，敦促人们通过捐款和加入行星协会来支持美国宇航局的科学基金和太空探索。

---

## 86. 如何开始对话

**原文标题**: How to Start a Conversation

**原文链接**: [https://talk.bradwoods.io/blog/how-to-start-a-conversation](https://talk.bradwoods.io/blog/how-to-start-a-conversation)

查理感到孤独，不擅长交谈，尤其是在每天与艾玛同乘电梯时。他们礼貌地寒暄，但总是陷入尴尬的沉默。查理渴望更深层次的联系。

他发现了“面包屑”的概念——将谈话话题融入到日常的回应中，比如“你好吗？”。他不再只是简单地回答“很好”，而是可以提供一个暗示他兴趣的回答。文章建议关注你真正感兴趣的话题，而不是试图猜测别人想听什么。目的是找到共同点，并从表面话题转向价值观、愿望或经历。

查理对电影和绘画感兴趣，他计划了带有这些兴趣“面包屑”的回答。第二天，当艾玛问他怎么样时，他用一个有趣的评论回应，其中包含了绘画、职业抱负和股票市场。艾玛透露了她对绘画的热爱，这源于她的母亲，一位风景画家。

他们的谈话变得轻松流畅，一直延续到大厅。查理感到了一种真诚的联系。文章总结说，专注于分享你的热情可以创造更深入的谈话机会，并减少孤独感。第二天，查理期待着见到艾玛并继续他们的谈话。

---

## 87. 饥饿使注意力转向不健康食品，研究发现

**原文标题**: Hunger shifts attention towards less healthy food options, study finds

**原文链接**: [https://medicalxpress.com/news/2025-03-hunger-shifts-attention-healthy-food.html](https://medicalxpress.com/news/2025-03-hunger-shifts-attention-healthy-food.html)

饥饿如何影响食物选择：一项eLife研究

本文讨论了一项发表在eLife上的研究，该研究探讨了饥饿如何影响食物选择。研究人员发现，饥饿会将注意力转移到食物的美味程度上，同时削弱对营养信息的关注，从而导致可能不健康的饮食决定。

该研究招募了70名成年人，他们在饥饿和饱腹状态下完成了食物选择实验。参与者面前呈现标有Nutri-Score（一种标准化的营养评级）的食物选项，并追踪他们的眼球运动。结果表明，虽然参与者通常更喜欢美味的选项，但饥饿会放大这种偏好。

与饱腹状态相比，饥饿的参与者更关注食物的视觉吸引力，而较少关注Nutri-Score。计算模型显示，饥饿增加了味道的重要性，同时降低了对健康信息的考虑。本质上，饥饿的人往往会忽略Nutri-Score，除非他们主动关注它。

研究人员认为，仅仅提供营养信息可能不足以抵消饥饿驱动的食物选择。他们建议，干预措施应侧重于使健康信息在视觉上更加突出或引导注意力。他们还指出，该研究是在受控的实验室环境中进行的，未来需要进一步研究，以探讨研究结果如何转化为现实情景。关键的结论是，饥饿会改变决策过程，优先考虑味道而非健康。

---

## 88. 内存分配器之战

**原文标题**: Battle of the Mallocators

**原文链接**: [http://smalldatum.blogspot.com/2025/04/battle-of-mallocators.html](http://smalldatum.blogspot.com/2025/04/battle-of-mallocators.html)

该博客发布于2025年4月11日，深入探讨了不同内存分配器（glibc malloc、jemalloc和tcmalloc）与MySQL (InnoDB) 和 MyRocks 一起使用时的性能和内存使用情况。作者强调，对于RocksDB（MyRocks使用），jemalloc或tcmalloc优于glibc malloc，以避免内存不足(OOM)错误。RocksDB的分配模式，涉及频繁的块缓存分配和释放，会给glibc malloc带来压力，导致过多的RSS（常驻内存集大小）。

作者在拥有128GB内存的AMD EPYC服务器上进行的测试表明，glibc malloc与MyRocks和50GB缓冲池一起使用会导致OOM。 使用10GB缓冲池时，与jemalloc和tcmalloc相比，glibc malloc导致MyRocks的RSS明显更高。 对于InnoDB，所有分配器的峰值RSS相似，仅略大于缓冲池大小。

在性能方面（使用sysbench测量的QPS），jemalloc和tcmalloc通常在InnoDB和MyRocks上都优于glibc malloc。 但是，在某些特定的微基准测试中，一种分配器显示出明显的优势。 作者强调了这些异常情况并分享了vmstat指标。

该文章还解决了使用jemalloc时对VSZ（虚拟内存集大小）的担忧，声明尽管它可能看起来比预期的要大，但这可能是jemalloc内存管理的一种假象，不一定是问题。 作者最后再次强调，建议将jemalloc或tcmalloc与MyRocks结合使用，以避免内存问题并可能提高性能。

---

## 89. Datastar：面向未来的Web框架？

**原文标题**: Datastar: Web Framework for the Future?

**原文链接**: [https://chrismalek.me/posts/data-star-first-impressions/](https://chrismalek.me/posts/data-star-first-impressions/)

Chris Malek 探索 Datastar：一种超媒体 Web 框架，作为 HTMX 的潜在替代方案，用于构建现代、实时 Web 应用程序。由于在开发更复杂的应用程序时，HTMX 的复杂性（尤其是需要集成 AlpineJS 以实现前端交互）令 Malek 不满，他在观看了一段对其创建者的采访后，重新审视了 Datastar。

Datastar 强调服务器端逻辑，使用 "信号" 通过反应式编程自动更新 UI，并利用服务器发送事件 (SSE) 实现快速性能。拥有 PeopleSoft ERP 开发背景的 Malek 正在寻找一种框架，该框架优先考虑后端控制、简单性和 Go 中的快速开发，同时最大限度地减少 JavaScript 的使用。

他强调了 Datastar 的关键概念：信号（用于自动 UI 更新的反应式编程原语）、SSE（高效的数据流）、动作（触发服务器端逻辑的 HTTP 动词）和片段（用于 UI 更新的 HTML 片段）。

与 HTMX 相比，Datastar 旨在提供一种更简化的方法，将前端状态管理和动作整合到一个 JavaScript 库中，从而可能消除对 React 或 Vue.js 等单独前端框架的需求。文章强调了理解“信号”的重要性，信号能够实现反应式编程，并通过基于数据更改自动更新元素来简化 UI 开发。虽然仍处于学习 Datastar 的早期阶段，但 Malek 对其潜力表示兴奋，并旨在引起更多人对其的关注。

---

## 90. Fedora 计划将软件包可复现性提升至 99%

**原文标题**: Fedora change aims for 99% package reproducibility

**原文链接**: [https://lwn.net/Articles/1014979/](https://lwn.net/Articles/1014979/)

LWN.net文章探讨Fedora 43发布版实现99%软件包可复现性的计划。可复现构建确保相同的源代码、构建环境和指令产生逐位相同的制品。尽管Fedora已经拥有受控的构建基础设施，但可复现性旨在通过检测供应链攻击和实现二进制文件的独立验证来增强安全性。

Fedora对可复现性的定义与Debian略有不同，由于RPM软件包格式的固有特性（嵌入式签名和构建时间/主机信息），它排除了签名和一些元数据。Fedora的工作始于钳制文件修改时间并实施`add-determinism`工具以标准化元数据。

实现99%的目标需要软件包维护者将可复现性问题作为错误来解决。`fedora-repro-build`实用程序将支持本地重建测试，公共的`rebuilderd`实例将提供独立的验证。该提案还建议更新打包指南以鼓励可复现构建。

Fedora Discourse论坛上的讨论重点围绕`rebuilderd`的基础设施、与Koji或Copr的潜在集成以及文档。虽然可复现性提供了安全优势，但它也通过暴露代码中的错误和粗心大意来提高软件包的质量。Haskell和Go软件包以及Linux内核的模块签名存在已知的可复现性问题。

---

## 91. 英国皇家邮政试用太阳能供电、带条形码扫描器的邮筒

**原文标题**: Royal Mail trials solar-powered postboxes with barcode scanners

**原文链接**: [https://eandt.theiet.org/2025/04/10/royal-mail-trials-solar-powered-postboxes-barcode-scanners](https://eandt.theiet.org/2025/04/10/royal-mail-trials-solar-powered-postboxes-barcode-scanners)

英国皇家邮政试点太阳能邮筒，配备条形码扫描仪，方便包裹投递。这项新设计是175年来首个重大变革，设有更大的包裹投递口、供客户扫描包裹的条形码扫描仪以及投递抽屉。客户还可以通过皇家邮政应用程序获取投递证明。

在英国全国推广之前，沃、赫特福德和福尔米尔正在试用五个邮筒。标准信件投递仍然可以通过单独的投递口进行。

该举措旨在服务在线市场卖家和寄送退货的在线购物者。皇家邮政更新了其应用程序，支持条形码包裹投递和投递证明请求，利用4G和定位服务。该公司计划改造其现有的115,000个邮筒中的数千个，以适应更大的包裹，这些邮筒位于英国98%的地址半英里范围内。

首席执行官艾玛·吉尔索普强调，在信件数量下降和包裹流量激增的情况下，此举是实现邮筒现代化的一种方式，为客户提供更多选择和便利。文章还简要介绍了英国邮筒标准化的历史。

---

## 92. 魯珀特王子之淚玻璃為何堅硬到能擊碎子彈 (2023)

**原文标题**: Why 'Prince Rupert's Drop' Glass Is Strong Enough to Shatter a Bullet (2023)

**原文链接**: [https://www.popularmechanics.com/science/a40008994/why-the-prince-ruperts-drop-is-so-strong/](https://www.popularmechanics.com/science/a40008994/why-the-prince-ruperts-drop-is-so-strong/)

《大众机械》的这篇文章探讨了“鲁珀特王子之泪”的惊人强度，这是一种玻璃泪珠，尽管外观脆弱，却能击碎子弹。秘密在于快速冷却过程。熔融玻璃滴入冷水后会形成硬化的外壳，而内部冷却并收缩，从而在核心产生巨大的抗压强度，并在表面产生张力。这种力的平衡使水滴具有极强的抗冲击能力。

当子弹击中水滴时，冲击会引发源自尾部的冲击波，导致整个结构在瞬间汽化。子弹本身通常会因玻璃内部压缩力的释放而破碎。

文章随后将这种原理与实际应用联系起来，以大猩猩玻璃为例。大猩猩玻璃利用类似的抗压强度原理，通过离子交换，表面较小的钠离子被较大的钾离子取代。这会在内部产生压力，从而强化玻璃。虽然并非坚不可摧，但大猩猩玻璃为手机等设备提供了保护。文章最后介绍了作者的个人简介。

---

## 93. 巨蟒与圣杯成为喜剧传奇。

**原文标题**: Monty Python and the Holy Grail became a comedy legend

**原文链接**: [https://www.bbc.com/culture/article/20250407-how-monty-python-and-the-holy-grail-became-a-comedy-legend](https://www.bbc.com/culture/article/20250407-how-monty-python-and-the-holy-grail-became-a-comedy-legend)

本文庆祝《巨蟒与圣杯》上映五十周年，探讨其作为喜剧传奇的持久影响力。文章收录了迈克尔·佩林和特瑞·吉列姆对电影创作和影响的见解。

巨蟒剧团最初是一个电视小品团体，他们试图用《圣杯》创造一种“电影体验”，尽管一些成员专注于其他项目。这部电影改编自亚瑟王传奇，是荒诞和历史元素的独特结合。

由于BBC的拒绝和对摇滚乐队资助的依赖，资金限制迫使他们采取创造性的解决方案，比如用椰子来模拟马，并从多个角度拍摄杜恩城堡。吉列姆强调了将幽默建立在真实的中古世纪背景中的重要性，尽管这与一些成员追求纯粹喜剧的愿望相冲突。

这部电影的成功巩固了吉列姆作为导演的地位，提升了剧团的国际声誉，并催生了更多的巨蟒剧团电影，如《万世魔星》。它还孕育了托尼奖获奖音乐剧《Spamalot》。这部电影中的角色和短语已经渗透到英国文化中，反映了在荒诞中所能找到的现实生活态度。吉列姆将巨蟒剧团的魔力归功于其六位成员独特的“化学平衡”，并强调他们的个人贡献对他们的成功至关重要。

---

## 94. Adobe因强烈反对而删除Bluesky帖子

**原文标题**: Adobe deletes Bluesky posts after backlash

**原文链接**: [https://petapixel.com/2025/04/10/adobe-deletes-bluesky-posts-after-furious-backlash/](https://petapixel.com/2025/04/10/adobe-deletes-bluesky-posts-after-furious-backlash/)

Adobe在Bluesky上与用户互动的尝试惨遭滑铁卢。该公司在其主账号和Photoshop账号上的最初帖子都受到了大量负面评论，用户批评Adobe的订阅定价模式、对人工智能的拥抱，以及其与创意社区沟通不足。

用户对价格上涨、产品质量下降以及该公司对人工智能生成艺术的所谓支持表示不满，这对许多艺术家来说是一个敏感问题。有些人甚至讽刺地表示，Adobe会按月向用户收费以查看其帖子。

由于不堪重负的负面反馈，Adobe删除了其在两个账号上的开篇帖子。这一举动遭到了Bluesky用户的嘲笑和进一步批评，他们认为这是该公司承认其在艺术家社区中不受欢迎。

文章将Adobe目前不受欢迎的原因归咎于十多年前转向订阅定价、随后的价格上涨以及对人工智能的拥抱。文章还强调了PetaPixel主编Jaron Schnieder过去的一段话，指出由于沟通不畅和最近的负面新闻，Adobe与摄影师的关系受到了损害。

---

## 95. 江诗丹顿打破世界纪录，推出最复杂腕表。

**原文标题**: Vacheron Constantin breaks the world record for most complicated wristwatch

**原文链接**: [https://www.hodinkee.com/articles/introducing-vacheron-constantin-les-cabinotiers-solaria](https://www.hodinkee.com/articles/introducing-vacheron-constantin-les-cabinotiers-solaria)

由于提供的内容讨论的是帝舵碧湾58勃艮第红，而标题讨论的是江诗丹顿打破世界纪录，这两个主题毫不相关，因此无法提供摘要。

根据侧重于帝舵碧湾58勃艮第红的内容，可以推断该文章是一篇“上手体验”评测。这意味着对这款腕表的实际考察，可能涵盖以下方面：

*   **美学设计:** 勃艮第红表圈是关键特征，突显了复古风格的设计。文章可能讨论了这种颜色及其吸引力。
*   **尺寸和佩戴感受:** 碧湾58以其更小、更符合复古风格的表壳尺寸而闻名。文章很可能探讨了它在手腕上的佩戴感受。
*   **机芯:** 文章很可能讨论了帝舵自产机芯的性能和规格。
*   **历史/背景:** “新复古原型回归”暗示了这款腕表的历史灵感，可能还有之前的原型或迭代版本。文章很可能探讨了这款腕表与帝舵历史的联系。
*   **总体印象:** “上手体验”的性质意味着评测者会对这款腕表的价值、质量和目标受众提供意见。

这篇文章很可能旨在让读者详细而实际地了解帝舵碧湾58勃艮第红。 在没有实际文章的情况下，这是我能提供的最准确的摘要。

---

## 96. 如何制作长弓

**原文标题**: How to Make a Longbow

**原文链接**: [https://www.howtomakealongbow.co.uk](https://www.howtomakealongbow.co.uk)

如何制作长弓

**概要:**

该页面标题为“如何制作长弓”，大概旨在提供制作长弓的说明或信息。作者声明该网站正在不断更新，并鼓励读者提供反馈和建议，以供未来内容参考。 目前，页面上没有提供任何关于如何制作长弓的实际内容，只是承诺未来会进行扩展。

---

## 97. 你可能并不需要 WebSockets

**原文标题**: You might not need WebSockets

**原文链接**: [https://hntrl.io/posts/you-dont-need-websockets/](https://hntrl.io/posts/you-dont-need-websockets/)

本文认为，尽管WebSockets看似是实时应用的理想选择，但可能并非总是必要或最佳方案。作者指出了使用WebSockets的三个主要缺点：

1.  **非事务性消息：** WebSocket消息缺乏固有的事务性，导致难以可靠地将命令与响应或错误消息关联起来，尤其是在跨多个客户端维护状态一致性时。这需要复杂的手动跟踪和错误处理。作者建议对事务性操作（如更新）使用HTTP，而将socket降级为表示单向数据流。
2.  **复杂的Socket生命周期：** 管理WebSocket连接涉及处理诸如打开、关闭和错误之类的事件，以及重新连接尝试和资源清理。与HTTP更简单的请求/响应生命周期相比，这增加了复杂性。
3.  **增加的服务器代码复杂性：** WebSockets需要服务器处理HTTP升级握手、解析WebSocket头部以及管理潜在的故障。与标准的HTTP请求相比，这引入了额外的代码和故障排除开销。

作为替代方案，本文提倡使用 **HTTP流** 将实时更新从服务器发送到客户端。HTTP流允许使用标准的HTTP协议创建单向数据流，从而消除了对全双工连接及其相关复杂性的需求。作者提供了一个JavaScript示例，演示了如何使用HTTP流实现服务器发送事件（SSE），以跨多个客户端维护实时计数器。

作者还推荐了他的库EventKit，作为简化异步数据流管理的工具。

---

## 98. 为什么训练人工智能不算作知识产权盗窃

**原文标题**: Why training AI can't be IP theft

**原文链接**: [https://blog.giovanh.com/blog/2025/04/03/why-training-ai-cant-be-ip-theft/](https://blog.giovanh.com/blog/2025/04/03/why-training-ai-cant-be-ip-theft/)

本文探讨了一个复杂的问题：人工智能训练使用受版权保护的材料是否构成知识产权盗窃，以及是否应该存在一种“学习权”，允许艺术家控制其作品用于人工智能训练。作者承认艺术家们对人工智能驱动的竞争以及未经同意或补偿而利用其作品的合理担忧。然而，作者认为将这个问题定性为侵犯版权并创造一种新的“学习权”是一种危险且最终有害的做法。

反对学习权的核心论点在于自由学习和灵感对人类创造力的重要性。作者断言，基于版权限制人工智能训练将不可避免地通过为艺术影响创造一种令人窒息的监管链体系，来扼杀人类艺术家。

文章进一步强调，无论是物理形式、表演还是在线形式，观看公开作品固有地赋予了从中学习的权利。虽然艺术家保留对其作品的复制和商业化的版权和控制权，但公开展示意味着接受观察和讨论。

作者批评了通过实施学习权来扩大版权的提议，认为这些提议往往缺乏合理的限制，并可能无意中损害人类艺术家。目前的版权框架不包括“可保留的学习权”，作者认为增加这种权利将对艺术自由和创新产生毁灭性的后果。虽然承认艺术家们真实的经济焦虑，但文章最终拒绝使用版权法来监管人工智能训练的想法，认为这是一种比疾病更糟糕的治疗方法。

---

## 99. GCC 15 的可用性改进

**原文标题**: Usability Improvements in GCC 15

**原文链接**: [https://developers.redhat.com/articles/2025/04/10/6-usability-improvements-gcc-15](https://developers.redhat.com/articles/2025/04/10/6-usability-improvements-gcc-15)

我能够访问网页，因此我将从提供的URL总结题为“GCC 15中的可用性改进”的文章。

该文章重点介绍了 GCC 15 中引入的六项关键可用性改进。这些改进旨在使 GCC 更易于使用和调试。

1. **改进了缺少包含文件的错误消息：** 当缺少所需的头文件时，GCC 15 提供更具信息性的错误消息，并建议可能的解决方案。这减少了识别和修复包含错误时的猜测。

2. **增强了类型不匹配的诊断：** 类型不匹配的诊断（尤其是涉及隐式转换的类型不匹配）得到了改进，可针对具体问题提供更清晰的指导。这包括指出涉及的类型以及可能的精度损失。

3. **对未初始化变量的更好警告：** GCC 15 具有针对使用未初始化变量的更精确的警告。分析已经过改进，以减少误报并提供更具可操作性的警报。

4. **更清晰的错误函数调用消息：** 与不正确的函数调用相关的错误消息更加明确。这有助于开发人员快速识别诸如参数类型或参数数量不正确之类的问题，从而减少调试时间。

5. **带有范围的更具信息性的诊断：** GCC 15 引入了一种新的诊断格式来显示发生错误的范围。这在源代码中提供了更多上下文，并且对于复杂的模板构造特别有用。

6. **-Wformat标志的诊断增强：** GCC 15 中对“-Wformat”标志的工作方式进行了改进，以提供更好，更全面的警告。

GCC 15 中的这些可用性增强功能有助于简化开发体验，从而帮助开发人员更快，更有效地识别和解决问题。总体目标是使 GCC 成为更实用且直观的 C 和 C++ 编程工具。

---

## 100. 刻意结交挚友 (2021)

**原文标题**: Intentionally Making Close Friends (2021)

**原文链接**: [https://www.neelnanda.io/blog/43-making-friends](https://www.neelnanda.io/blog/43-making-friends)

尼尔·南达博客文章《刻意结交挚友》详述了他学习如何建立更深层次情感连接的个人历程。起初，他缺少亲密朋友，并且从未将其视为一种可能。一段浪漫关系凸显了情感亲密的重要性，从而改变了他的心态。

为了弥补这一点，他进行了一项实验：他确定了亲密友谊的特征，并通过询问熟人一系列个人、能引发脆弱感的问题，来设计类似的互动。令人惊讶的是，这产生了积极的结果，并帮助他建立了更牢固的联系。

南达强调了积极主动培养友谊的重要性，而不是被动地等待友谊“自然发生”。他建议打破“正常”的谈话模式，并挑战既定的社会界限。他的回顾突出了有意的、真实的1对1时间和敢于“另类”以解锁更深层次连接的价值。

文章最后给出了建议，重点在于利用“递归式好奇心”在对话中寻求兴奋感，提出开放式问题，并表现出真诚的兴趣。他还讨论了脆弱性的重要性，创造一个安全的分享空间，并在尊重界限的基础上加以平衡。最终，他提倡有意识和真实性是建立有意义和充实友谊的关键要素。

---

