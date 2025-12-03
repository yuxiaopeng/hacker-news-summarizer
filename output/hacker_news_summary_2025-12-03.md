# Hacker News 热门文章摘要 (2025-12-03)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 国会议员选股能力高出47个百分点

**原文标题**: Congressional lawmakers 47% pts better at picking stocks

**原文链接**: [https://www.nber.org/papers/w34524](https://www.nber.org/papers/w34524)

题为《国会山的“船长获利”》的这份NBER工作论文，调查了美国国会立法者的股票交易表现，揭示了他们在晋升领导职位后表现出显著的差异。该研究利用交易层面的数据发现，领导者每年的表现比与其匹配的同僚高出惊人的47个百分点。

作者魏尚进和周一帆将这种优异表现归因于两种主要机制：政治影响力和公司关系。

**政治影响力：** 当其所在党派控制议院时，领导者从其影响力中获益，并在监管行动前战略性地出售股票，以及购买获得更多政府合同或在法案中享受有利党派支持的公司的股票，从而获得更高的回报。

**公司关系：** 领导者获得了特权的公司信息，股票交易预测了随后的公司新闻，以及对捐助者拥有或家乡州公司的投资获得了更好的回报，这些都证明了这一点。

本质上，该研究表明，与同僚相比，国会领导人利用其政治权力和内部关系在股市中获得明显更高的回报。

---

## 2. MinIO 目前处于维护模式。

**原文标题**: MinIO is now in maintenance-mode

**原文链接**: [https://github.com/minio/minio/commit/27742d469462e1561c776f88ca7a1f26816d69e2](https://github.com/minio/minio/commit/27742d469462e1561c776f88ca7a1f26816d69e2)

MinIO项目现已进入维护模式，不再接受新功能、增强或拉取请求。这意味着代码库处于仅维护状态。虽然可能会根据具体情况评估关键安全修复，但现有问题和拉取请求将不会被积极审查。社区支持将继续尽力通过其Slack频道提供。如需企业支持和积极维护的版本，用户可访问MinIO AIStor。本质上，开源MinIO项目已停止积极开发，仅专注于关键维护，用户可转向商业替代方案以获得积极开发和支持。

---

## 3. Steam Deck负责人透露Valve正在资助Windows游戏的ARM兼容性

**原文标题**: Steam Deck lead reveals Valve is funding ARM compatibility of Windows games

**原文链接**: [https://frvr.com/blog/news/steam-deck-lead-reveals-valve-is-funding-arm-compatibility-of-windows-games-to-expand-pc-gaming-and-release-ultraportables-in-the-future/](https://frvr.com/blog/news/steam-deck-lead-reveals-valve-is-funding-arm-compatibility-of-windows-games-to-expand-pc-gaming-and-release-ultraportables-in-the-future/)

本文重点介绍了游戏行业的两个不同主题。

首先，文章报道称 Valve 正在积极资助改进 Windows 游戏在 ARM 架构上的兼容性的工作，特别是针对 Steam Deck。这一由 Steam Deck 负责人透露的消息表明，Valve 致力于扩大该掌机上可玩的游戏范围，可能是通过模拟或其他利用 ARM 架构的兼容层来实现。这可能会显著扩展 Steam Deck 的游戏库，并使其对更广泛的受众更具吸引力。

其次，文章提到了来自“远征 33 号”的配音演员呼吁在 TGA 游戏大奖中设立专门的“动作捕捉类别”。演员们认为，认可动作捕捉表演至关重要，因为这些表演者尽管对游戏开发做出了重大贡献，但往往很少甚至没有得到关注。他们强调了缺乏认可以及动作捕捉表演者可能“消失”而没有得到对其工作的认可的可能性。 这提倡提高对电子游戏创作中一个重要但经常被忽视的方面的认可。

---

## 4. React 和 Next.js 中的 RCE 漏洞

**原文标题**: RCE Vulnerability in React and Next.js

**原文链接**: [https://github.com/vercel/next.js/security/advisories/GHSA-9qr9-h5gf-34mp](https://github.com/vercel/next.js/security/advisories/GHSA-9qr9-h5gf-34mp)

本文档描述了一个影响 React Server Components 和 Next.js 应用程序的关键远程代码执行 (RCE) 漏洞。具体来说，它影响某些 React 包的 19.0.0、19.1.0、19.1.1 和 19.2.0 版本，以及使用 App Router 的 Next.js 15.x 和 16.x 版本。该漏洞的上游追踪编号为 CVE-2025-55182。

该问题还影响 Next.js 从 14.3.0-canary.77 开始的实验性 Canary 版本。建议这些 Canary 构建的用户降级到稳定的 14.x 版本或 14.3.0-canary.76。

React 19.0.1、19.1.2 和 19.2.1 版本以及 Next.js 15.0.5、15.1.9、15.2.6、15.3.6、15.4.8、15.5.7 和 16.0.7 版本提供了补丁。强烈建议稳定 Next.js 15.x 和 16.x 版本用户立即升级。

由于网络攻击向量、低攻击复杂度、无需权限、无需用户交互、作用范围已更改以及对机密性、完整性和可用性的高影响，该漏洞的 CVSS 评分为 10.0（严重）。

---

## 5. 你骗不了优化器

**原文标题**: You Can't Fool the Optimizer

**原文链接**: [https://xania.org/202512/03-more-adding-integers](https://xania.org/202512/03-more-adding-integers)

你骗不了优化器

这篇文章《你骗不了优化器》强调了编译器在优化甚至高度混淆代码方面的强大能力。作者Matt Godbolt用几个为ARM架构编写的复杂的无符号加法例程来说明了这一点。尽管它们的结构不同，编译器始终将它们简化为一条高效的`add w0, w1, w0`指令。

关键在于编译器并不依赖于已知“愚蠢”代码模式的数据库。相反，它们将代码转换为中间表示，一种简化的抽象形式，这使它们能够识别潜在的数学等价性。例如，一个旨在添加两个数字的复杂`while`循环被转换为“将y增加x，然后返回y”，编译器随后将其识别为等同于“返回x + y”。

这种将代码转换为标准、规范形式的过程使编译器能够以相同的方式处理看似不同的代码片段。这种强大的模式识别能力使程序员可以优先考虑代码的可读性和清晰性，相信编译器会有效地生成优化后的代码。 这篇文章是“2025编译器优化探索”系列的一部分，并鼓励读者在Compiler Explorer中探索“Opt Pipeline Viewer”，以亲眼目睹编译器的转换过程。

---

## 6. 如何合成House Loop

**原文标题**: How to Synthesize a House Loop

**原文链接**: [https://loopmaster.xyz/tutorials/how-to-synthesize-a-house-loop](https://loopmaster.xyz/tutorials/how-to-synthesize-a-house-loop)

loopmaster网站“实时音频编程”栏目中的文章《如何合成House Loop》专注于教授读者如何使用数字音频合成技术从零开始创建House音乐鼓loop。它很可能将这个过程分解为创建单独的鼓元素——底鼓、军鼓/拍手声、踩镲，以及可能的其他打击乐元素——然后将它们组合成一个有凝聚力的节奏模式。

这篇文章很可能涵盖：

*   **合成单独的鼓声：** 描述使用各种合成技术（例如，减法合成、FM合成、噪声发生器）生成每种声音的方法。诸如频率、振幅包络、滤波器设置和共振之类的参数很可能会被讨论，以便为每个鼓元素创建所需的音色特征。
*   **构建节奏：** 解释如何在音序器或DAW中排列合成的鼓声，以创建典型的4/4 House节拍。这包括将底鼓放在第1拍和第3拍上，将军鼓或拍手声放在第2拍和第4拍上，并排列踩镲以创建驱动的节奏感。
*   **混音和处理：** 可能会包含关于对各个鼓声和整个loop进行EQ、压缩和添加混响的技巧，以实现专业和精致的声音。
*   **编程环境：** 这篇文章可能假设读者对DAW或音频合成编程环境有基本的熟悉程度。

本质上，这篇文章是为有兴趣深入了解声音设计和节奏编排的电子音乐制作人提供的实用指南，尤其是在House音乐的背景下。

---

## 7. Rocketable (YC W25) 正在招聘一位创始工程师，以实现软件公司的自动化。

**原文标题**: Rocketable (YC W25) is hiring a founding engineer to automate software companies

**原文链接**: [https://www.ycombinator.com/companies/rocketable/jobs/CArgzmX-founding-engineer-automation-platform](https://www.ycombinator.com/companies/rocketable/jobs/CArgzmX-founding-engineer-automation-platform)

Rocketable (YC W25) 寻求创始工程师，构建自动化平台，将SaaS公司收购并转型为完全自主的AI驱动业务，无需人工操作员、工程团队和支持人员。理想的候选人坚信完全自动化的必然性，并希望构建前所未有的解决方案，而不是渐进式的改进。

该职位涉及构建一个自动化真实SaaS公司的平台，从客户支持开始，逐步发展成为一个从人工干预中学习、构建自己的工具并实现超人性能的系统。该公司正在寻找具有5年以上扩展生产系统经验、在AI/ML（LLM集成、提示工程）和基础设施（Kubernetes、Docker、云平台）方面具有强大技能的人员。精通TypeScript和Python者优先。

Rocketable 获得了来自 Y Combinator 和其他机构的 650 万美元种子轮融资，为多次收购提供了资金。团队规模很小，每周 5 天在旧金山（或马林县）进行面对面办公。该公司承认其工作的社会影响，但仍专注于构建一个持久的、由人工智能驱动的未来。面试过程包括介绍性电话、系统设计面试、背景调查、付费试用项目和推荐人面试。Rocketable 旨在创建一个由可扩展且自我完善的人工智能驱动的高利润软件产品组合，这些产品以人类无法达到的水平运行。

---

## 8. GSWT：高斯溅射王氏瓦片

**原文标题**: GSWT: Gaussian Splatting Wang Tiles

**原文链接**: [https://yunfan.zone/gswt_webpage/](https://yunfan.zone/gswt_webpage/)

本文介绍了一种名为GSWT（高斯溅射王氏砖）的新颖框架，该框架扩展了3D高斯溅射（3DGS）的功能，能够从单个捕获的样本生成大规模或无限地形。其核心思想是使用王氏砖创建一个基于瓦片的系统，其中每个瓦片代表一个局部高斯场。这些瓦片的设计具有边界约束，以确保相邻瓦片之间的无缝过渡，从而能够在任意表面上实现高斯场的随机且连续的平铺。

GSWT流程首先从多视图图像重建多个细节级别（LOD）的3DGS样本。对于每个LOD，该方法通过采样边缘和中心块并应用语义感知的图割算法来生成王氏砖集合。在渲染之前，瓦片会进行预排序，以便进行高效的无排序溅射。

在运行时，系统会动态执行平铺，从而实现高效的基于GSWT的地形合成和渲染。本文还介绍了专门为3DGS王氏砖的独特特性设计的渲染优化，从而实现大规模3DGS地形的实时渲染。作者承诺提供代码、数据集和演示，以供进一步探索。该论文计划在SIGGRAPH Asia 2025上发表。

---

## 9. 为什么我玩游戏的时候耳机总是有嗡嗡声？

**原文标题**: Why are my headphones buzzing whenever I run my game?

**原文链接**: [https://alexene.dev/2025/12/03/Why-do-my-headphones-buzz-when-i-run-my-game.html](https://alexene.dev/2025/12/03/Why-do-my-headphones-buzz-when-i-run-my-game.html)

作者在使用等距视角游戏时，耳机中出现嗡嗡声，而运行其他图形密集型游戏时则无此问题。耳机通过USB连接至MODI 2 DAC，并由电脑上的USB端口供电。

作者最初怀疑是电源问题，但由于更大的游戏不会触发嗡嗡声而排除了该可能性。通过排除法，他们发现嗡嗡声与游戏的渲染管线有关，更具体地说，与频繁将“拾取纹理”从GPU复制到CPU有关。该纹理用于鼠标点击对象选择，使游戏能够识别玩家点击的对象。禁用纹理传输消除了嗡嗡声，降低传输频率则减轻了噪音。

根本原因是GPU在满载和空闲状态之间快速切换，这是由于每帧传输整个拾取纹理造成的。这种通过USB端口的突然功率波动干扰了MODI 2 DAC，导致嗡嗡声。解决方案是仅下载拾取纹理中的相关像素，从而显著减少GPU负载波动并消除嗡嗡声。作为次要解决方案，作者可以使用不同的电源为MODI 2 DAC供电。

---

## 10. 2012年的Rust一览

**原文标题**: A Look at Rust from 2012

**原文链接**: [https://purplesyringa.moe/blog/a-look-at-rust-from-2012/](https://purplesyringa.moe/blog/a-look-at-rust-from-2012/)

这篇博文基于 2012 年左右（大约 0.5-0.6 版本）的官方教程，饶有趣味地展现了当时的 Rust。它突出了与现代 Rust 的显著差异，尤其是在安装、语法、内存管理、并发和模块系统等方面。

主要区别包括涉及 tarball 和 MinGW 的手动安装过程，使用 `fmt!` 而不是 `println!`，以及使用 `uint` 和 `int` 分别代替 `usize` 和 `isize`。语法通常更加冗长，trait 的实现写作 `impl Type: Trait`。

一个显著的分歧在于内存管理，存在 `@T` (任务本地垃圾回收堆)、`~T` (拥有的、可发送的对象) 和具有不同可变性语义的 `&T` 引用。与现代 Rust 不同，`&mut T` 不保证独占访问，并且 `&T` 的行为更接近于 `&UnsafeCell<T>`。Rust 还具有绿色线程和轻量级任务，通过内置的 `spsc` 管道进行消息传递通信。当时的 Panics，被称为 exceptions，会使整个任务崩溃。

该文章还详细介绍了缺少 Cargo 和 `Cargo.toml`，而是依赖于根文件中指定的 crate 元数据。结构体默认与 C 兼容，可见性由 `pub` 和 `priv` 关键字控制。最后，这篇文章重点介绍了 "do expressions"——一种现已废弃的用于创建控制流结构的机制，以及在过渡到拉取迭代器之前存在的推送式迭代器。

---

## 11. React和Next.js存在严重RCE漏洞

**原文标题**: Critical RCE Vulnerabilities in React and Next.js

**原文链接**: [https://www.wiz.io/blog/critical-vulnerability-in-react-cve-2025-55182](https://www.wiz.io/blog/critical-vulnerability-in-react-cve-2025-55182)

本文详细介绍了React中的CVE-2025-55182和Next.js中的CVE-2025-66478关键远程代码执行(RCE)漏洞，这些漏洞影响React服务器组件(RSC)和“Flight”协议。漏洞源于RSC有效载荷的不安全反序列化，允许攻击者通过精心设计的HTTP请求在服务器上执行任意代码。利用非常可靠，无需事先身份验证。

使用`create-next-app`构建的Next.js应用程序的标准配置默认存在漏洞。Wiz Research表明，39%的云环境包含易受攻击的实例。

根本原因在于`react-server`包对RSC有效载荷的不安全处理。受影响的产品包括React 19.0、19.1和19.2版本，以及Next.js 14.3.0-canary、15.x和16.x版本（App Router）。强烈建议立即修补到强化版本：React (19.0.1、19.1.2、19.2.1) 和 Next.js (14.3.0-canary.88，以及原始文章中列出的多个以.7或.8结尾的15.x和16.x版本)。Redwood和Waku等其他启用RSC的框架的用户也应检查更新。Wiz客户可以利用Wiz威胁中心进行漏洞检测。由于其严重性，具体技术细节将被保留，以便在公开披露前进行广泛修补。

---

## 12. React 服务端组件中的严重安全漏洞

**原文标题**: Critical Security Vulnerability in React Server Components

**原文链接**: [https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components](https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components)

2025年12月3日，React团队宣布了一个严重未经身份验证的远程代码执行（RCE）漏洞，CVE-2025-55182（CVSS 10.0），影响React服务端组件。该漏洞存在于React解码发送到React服务端函数端点的负载的方式中，可能允许攻击者在服务器上执行任意代码。

即使应用程序没有明确使用React服务端函数，如果它支持React服务端组件，也存在漏洞。受影响的软件包包括`react-server-dom-webpack`、`react-server-dom-parcel`和`react-server-dom-turbopack`的19.0、19.1.0、19.1.1和19.2.0版本。

需要立即采取行动升级到19.0.1、19.1.2或19.2.1版本。如果React代码不使用服务器，或者应用程序不使用支持React服务端组件的框架/打包器，则不受影响。

受影响的框架和打包器包括Next.js、React Router、Waku、@parcel/rsc、@vitejs/plugin-rsc和rwsdk，每个框架和打包器都提供了具体的升级说明。托管提供商已实施临时缓解措施，但立即更新仍然至关重要。

该漏洞于11月29日报告，11月30日确认，12月1日创建了修复程序，并于12月3日公开披露。报告感谢Lachlan Davidson发现并报告了该漏洞。

---

## 13. 我们会在AI数据中心重蹈电信业崩溃的覆辙吗？

**原文标题**: Are we repeating the telecoms crash with AI datacenters?

**原文链接**: [https://martinalderson.com/posts/are-we-really-repeating-the-telecoms-crash-with-ai-datacenters/](https://martinalderson.com/posts/are-we-really-repeating-the-telecoms-crash-with-ai-datacenters/)

本文反驳了当前人工智能数据中心热潮与2000年代电信崩盘之间的常见比较。虽然两者都涉及大规模基础设施支出和泡沫担忧，但其根本基础存在显著差异。

电信崩盘是由对互联网流量增长的严重高估（高估了4倍），以及光纤技术的指数级进步造成的，这使得现有基础设施过时。这导致了大量未使用的“暗光纤”。

相比之下，人工智能数据中心面临着每瓦GPU性能提升速度放缓和功耗上升的问题，这表明现有硬件不会迅速过时。此外，对人工智能计算能力的需求，特别是随着人工智能代理的兴起，可能被低估，而不是高估。从简单的聊天到复杂的人工智能代理的转变预计将推动token消耗的大幅增长，可能超过当前的基础设施能力。

虽然本文承认由于诸如代理采用速度放缓、金融市场不稳定或意外的效率突破等因素，可能出现短期调整，但它强调这只是一个时间问题，而不是根本性的崩溃。过度建设的人工智能基础设施最终可能会被利用，这与电信时代永久黑暗的光纤不同。 理性过度建设源于囚徒困境：过度建设并浪费资本的风险低于建设不足并在“人工智能战争”中失去阵地。

作者得出结论，关键风险在于时机，而非方向。 为需求增长“过早”建设基础设施可能会导致一段财务痛苦期，但它与为永远无法实现的需求而建设基础设施，同时技术使其过时，有着根本的不同。

---

## 14. Zig 退出 GitHub，称微软对人工智能的痴迷毁了这项服务

**原文标题**: Zig quits GitHub, says Microsoft's AI obsession has ruined the service

**原文链接**: [https://www.theregister.com/2025/12/02/zig_quits_github_microsoft_ai_obsession/](https://www.theregister.com/2025/12/02/zig_quits_github_microsoft_ai_obsession/)

The Zig programming language project is leaving GitHub for Codeberg, citing a decline in engineering excellence at the Microsoft-owned platform, driven by an overemphasis on AI. Andrew Kelly, president of the Zig Software Foundation, criticized GitHub Actions for persistent bugs, particularly a "safe_sleep.sh" script issue that caused 100% CPU usage and runner failures due to "vibe-scheduling." This bug, reported in April 2025 but stemming from a 2022 code change, went unaddressed for an extended period despite being easily identifiable.

Jeremy Howard echoed concerns about GitHub Actions' poor state, highlighting the lengthy delay in fixing the CPU usage issue. Another software project, Dillo browser, is also migrating away from GitHub due to concerns about JavaScript reliance, service denial risks, usability issues, inadequate moderation, and the platform's focus on generative AI.

Codeberg has seen a doubling of its supporting membership since January, suggesting that more developers are choosing to migrate away from Github.  While GitHub's overall user numbers remain high, its focus on AI, specifically GitHub Copilot, has led to significant revenue growth, accounting for approximately 40% of annual revenue growth in Q4 2024.


---

## 15. 地狱潜者2开发商将安装包大小从154GB缩减至23GB

**原文标题**: Helldivers 2 devs slash install size from 154GB to 23GB

**原文链接**: [https://www.tomshardware.com/video-games/pc-gaming/helldivers-2-install-size-slashed-from-154gb-to-just-23gb-85-percent-reduction-accomplished-by-de-duplicating-game-data-an-optimization-for-older-mechanical-hard-drives](https://www.tomshardware.com/video-games/pc-gaming/helldivers-2-install-size-slashed-from-154gb-to-just-23gb-85-percent-reduction-accomplished-by-de-duplicating-game-data-an-optimization-for-older-mechanical-hard-drives)

《地狱潜者2》开发商Arrowhead Game Studios，在Nixxes Software的协助下，已将游戏安装包大小从154GB大幅缩减至23GB，降幅达85%。 这一显著缩减是通过去除最初为机械硬盘(HDD)优化而重复的游戏数据来实现的。 最初的大体积是为了通过复制数据来减少HDD上的加载时间。 然而，Arrowhead的数据测量表明，对于11%使用HDD的玩家来说，加载时间仅增加了几秒钟，并且加载时间的主要因素是关卡生成，它与资源加载并行发生。 这一改变对于拥有SSD的PC游戏玩家来说是一次胜利，释放了大量的存储空间。 新的“精简版”《地狱潜者2》已作为Steam上的beta更新提供，在安装体积更小的情况下提供相同的体验。 所有进度、购买和战争贡献都将保留。 评论区反映了关于现代游戏是否需要SSD的讨论，以及关于为了迁就使用旧硬件（特别是HDD）的玩家，而牺牲所有玩家更大文件大小的挫败感。

---

## 16. 云霄飞车大亨创始人克里斯·索耶访谈 (2024)

**原文标题**: Interview with RollerCoaster Tycoon's Creator, Chris Sawyer (2024)

**原文链接**: [https://medium.com/atari-club/interview-with-rollercoaster-tycoons-creator-chris-sawyer-684a0efb0f13](https://medium.com/atari-club/interview-with-rollercoaster-tycoons-creator-chris-sawyer-684a0efb0f13)

无法访问文章链接。

---

## 17. 绘制美国5万亿美元医疗系统的每一分钱流向

**原文标题**: Mapping Every Dollar of America's $5T Healthcare System

**原文链接**: [https://healthisotherpeople.substack.com/p/an-abominable-creature](https://healthisotherpeople.substack.com/p/an-abominable-creature)

无法访问文章链接。

---

## 18. 手写识别大势已去

**原文标题**: The Writing Is on the Wall for Handwriting Recognition

**原文链接**: [https://newsletter.dancohen.org/archive/the-writing-is-on-the-wall-for-handwriting-recognition/](https://newsletter.dancohen.org/archive/the-writing-is-on-the-wall-for-handwriting-recognition/)

手写识别面临末日？

丹·科恩宣布人工智能在准确转录手写文本方面取得重大突破，解决了数字人文领域长期存在的挑战。他以解读数学家乔治·布尔手稿的经验为例，对比了费力的人工过程与谷歌 Gemini 3 Pro 的卓越准确性。

尽管先前的手写文本识别(HTR)尝试举步维艰，Gemini 3 Pro 却展示了对来自布尔、查尔斯·卡罗尔，甚至简·奥斯汀极具挑战性的交叉书写 19 世纪信件的近乎完美的转录。值得注意的是，Gemini 为其解读提供了详细的推理，反映了古文字学中教授的分析步骤。

科恩认为，这一进展使研究人员能够专注于更深入的诠释性工作，而不是繁琐的解读文本任务。他提倡利用人工智能的 HTR 能力来增强人类的理解，并建议将其作为一种教学工具，指导学生完成解读历史文献的过程。在承认沉浸式档案研究的价值的同时，他也认识到现代历史学家面临的时间限制，并强调了 Tropy 和 Sourcery 等工具的重要性，这些工具与人工智能驱动的 HTR 相结合，可以简化研究过程。最终，科恩设想人工智能是一种减少研究单调性的手段，从而腾出时间进行更有意义的人类活动和连接。

---

## 19. universal-tbxi-patchset：用于启动System 7.5的Mac OS New World ROM补丁集

**原文标题**: universal-tbxi-patchset: Mac OS New World ROM patchset to boot System 7.5

**原文链接**: [https://github.com/Wack0/universal-tbxi-patchset](https://github.com/Wack0/universal-tbxi-patchset)

本文档描述了“universal-tbxi-patchset”，这是一个补丁集合，旨在修改经典 Mac OS New World Toolbox ROM 镜像 (TBXI) 1.2 及更高版本，使其能够启动较早版本的 Mac OS，特别是 System 7.5 及更高版本。原始的 TBXI 镜像删除了一些早期系统运行所需的代码。

该补丁集合主要关注三个方面：

*   **m68k_patch:** 此补丁集合恢复了不同 TBXI 版本中删除的各种 Toolbox 实现，包括程序间通信工具箱、声音工具箱、通信工具箱、事件管理器、图片实用程序、文本服务管理器和图标实用程序。它还解决了函数表初始化问题。
*   **ProcessMgrSupport:** 这解决了 TBXI 版本之间 ProcessMgrSupport.pef 初始化方式的更改。该补丁集合同时提供新旧初始化格式，以支持早期和后期的系统文件。
*   **InterfaceLib patches:** 这些补丁解决了 Mac OS 9.0 中引入的文件控制块 (FCB) 格式的更改。它提供了手动补丁说明（以及 TBXI v10.2.1 的特定偏移量），用于修复 InterfaceLib 中处理 FCB 的函数，以防止在较新的 TBXI 上运行较旧的系统版本时出现系统错误。

本文档还提到了已知问题，例如在使用打过补丁的 v10.2.1 TBXI 时，System 7.x 中的“日期和时间”控制面板会崩溃，并警告说打过补丁的系统可能不稳定。

---

## 20. PostgreSQL 19 中的超快速聚合

**原文标题**: Super fast aggregations in PostgreSQL 19

**原文链接**: [https://www.cybertec-postgresql.com/en/super-fast-aggregations-in-postgresql-19/](https://www.cybertec-postgresql.com/en/super-fast-aggregations-in-postgresql-19/)

无法访问文章链接。

---

## 21. Anthropic 收购 Bun

**原文标题**: Anthropic acquires Bun

**原文链接**: [https://bun.com/blog/bun-joins-anthropic](https://bun.com/blog/bun-joins-anthropic)

Bun已被Anthropic收购：专注AI驱动的软件开发

---

## 22. Anthropic 据报道正准备进行 3000 亿美元的首次公开募股。

**原文标题**: Anthropic reportedly preparing for $300B IPO

**原文链接**: [https://vechron.com/2025/12/anthropic-hires-wilson-sonsini-ipo-2026-openai-race/](https://vechron.com/2025/12/anthropic-hires-wilson-sonsini-ipo-2026-openai-race/)

据报道，Claude聊天机器人的开发公司Anthropic正准备最早于2026年进行首次公开募股（IPO），目标估值超过3000亿美元。该公司已聘请在指导科技公司上市方面经验丰富的威尔逊·桑西尼·古德里奇·罗萨蒂律师事务所协助处理此事。

此举使Anthropic有可能先于竞争对手OpenAI进入公开市场，测试投资者对支出巨大且持续亏损的人工智能公司的投资意愿。虽然讨论仍处于初步阶段，且尚未选择承销商，但Anthropic表示尚未就上市做出任何最终决定。

IPO准备工作与一轮可能将Anthropic估值超过3000亿美元的私募融资同时进行，据报道，微软和英伟达承诺投资150亿美元。Anthropic还承诺在微软的云平台上花费300亿美元。首席执行官Dario Amodei预计收入将大幅增长，预计明年年化收入将达到260亿美元，这得益于不断扩大的客户群。

公司内部正为公开市场要求做准备，包括聘请新的首席财务官，并专注于治理、会计和披露实践。虽然OpenAI也在进行类似的初步工作，但他们表示上市并非迫在眉睫。两家公司都面临着在大量投资于模型训练和基础设施的同时，证明盈利能力这一挑战，Anthropic计划斥资500亿美元建设数据中心并扩大员工队伍。

---

## 23. 退伍军人事务部员工指出甲骨文构建的电子健康记录存在危险错误

**原文标题**: VA staff flag dangerous errors in Oracle-built electronic health record

**原文链接**: [https://www.washingtonpost.com/investigations/2025/12/03/veterans-administration-va-hospitals-health/](https://www.washingtonpost.com/investigations/2025/12/03/veterans-administration-va-hospitals-health/)

无法访问文章链接。

---

## 24. 页面调出

**原文标题**: Paged Out

**原文链接**: [https://pagedout.institute](https://pagedout.institute)

《Paged Out!》是一本免费的、社区驱动的技术杂志，专注于编程、黑客技术、安全、复古/现代计算机、电子学和演示场景话题。每篇文章占据一页。该杂志以非营利方式运作，确保所有期刊都可以免费下载、分享和打印。印刷版可在活动中获取，也可通过lulu.com等按需印刷服务获得，有时还提供赞助选项。

网站列出了可用的期刊，从第1期（2019年8月）到最新第7期（2025年10月）。每期条目包括：

*   简短的描述或标题。
*   下载计数器。
*   印刷计数器（手动更新）。
*   该期网络PDF版本的下载链接。
*   与该期封面艺术相关的各种格式（JPG、PNG、8K）壁纸的下载链接。
*   在lulu.com上购买印刷版本的链接，可以选择普通版和赞助版。
*   封面艺术家署名。

一些期刊被标记为“测试版本”，表示正在进行改进，并且缺少诸如针对出血印刷优化的PDF等元素。该网站还设有“下一期进度追踪器”，显示下一期有多少文章已准备就绪或正在审核中。读者可以订阅电子邮件新闻通讯或使用RSS/Atom订阅源，以接收有关新期刊发布的通知。该网站鼓励社区以单页文章的形式进行投稿。

---

## 25. 《广告狂人》HBO Max 4K版惨败

**原文标题**: The "Mad Men" in 4K on HBO Max Debacle

**原文链接**: [http://fxrant.blogspot.com/2025/12/the-mad-men-in-4k-on-hbo-max-debacle.html](http://fxrant.blogspot.com/2025/12/the-mad-men-in-4k-on-hbo-max-debacle.html)

托德·瓦齐里博文详细描述了HBO Max上新4K“修复”版《广告狂人》的一个重大质量控制问题。问题在于，剧集流媒体版本，尤其是在第一季中，缺少了原版播出和家庭视频发行版中存在的数字视觉特效。

最明显的例子是罗杰·斯特林呕吐的场景，在HBO Max版本中可以看到用于制造效果的软管和技术人员。这揭示了应用数字特效之前的原始、未编辑的片段。其他例子包括拍摄地点缺少符合时代背景的修改，以及第一集开头缺少介绍文字。

瓦齐里强调，这个问题不同于将旧4:3节目重新构图为16:9的有争议的做法，因为《广告狂人》已经以16:9格式制作。他提供了蓝光版本和HBO Max流媒体之间的视觉比较，以说明缺失的特效和修改后的剧集标题。作者还强调，HBO Max上的初始剧集顺序是混乱的，但此后已得到纠正。

作者认为，这些失误对狮门影业和HBO Max产生了不良影响，有可能将备受期待的4K首秀变成一个关于媒体修复中质量控制的警示故事。文章承诺随着情况发展会进行更新。

---

## 26. 研究人员发现一种能从火星土壤中产生氧气的微生物

**原文标题**: Researchers Find Microbe Capable of Producing Oxygen from Martian Soil

**原文链接**: [https://scienceclock.com/microbe-that-could-turn-martian-dust-into-oxygen/](https://scienceclock.com/microbe-that-could-turn-martian-dust-into-oxygen/)

研究人员发现了一种极端微生物——球形蓝细菌 (*Chroococcidiopsis*)，它能够利用火星土壤（风化层）中的资源产生氧气。 这对于在火星上建立人类定居点的潜力来说是一项重大发现，因为从地球运输氧气是不切实际的。

该微生物在模拟火星条件下的土壤中茁壮成长，提取养分并释放氧气。 它的复原力扩展到在极端辐射和低压环境中生存，甚至在补水后修复DNA损伤。 这使得球形蓝细菌成为火星上生物制氧系统的一个有希望的候选者。

虽然在扩大其培养规模并确保其在火星条件下生产力方面仍然存在挑战，但这一发现代表着向前迈出的关键一步。 它提出了在火星上“种植”氧气的可能性，从而为食物、水和氧气生产创造闭环系统，减少对地球补给的依赖。 这一发现也激发了关于生命在太阳系内其他极端环境中存在的可能性的更广泛问题，突显了极端微生物的适应性。 目前的研究重点是将微生物制氧整合到全面的、自给自足的生命支持系统中，以供未来的火星定居点使用。

---

## 27. 人工智能代理在日常压力下违反规则

**原文标题**: AI agents break rules under everyday pressure

**原文链接**: [https://spectrum.ieee.org/ai-agents-safety](https://spectrum.ieee.org/ai-agents-safety)

AI新闻：AI智能体在日常压力下违规

---

## 28. 微软下调人工智能软件增长目标

**原文标题**: Microsoft lowers AI software growth targets

**原文链接**: [https://finance.yahoo.com/news/microsoft-lowers-ai-software-sales-141531121.html](https://finance.yahoo.com/news/microsoft-lowers-ai-software-sales-141531121.html)

以下是该文章的简明摘要：

微软否认了The Information的一篇报道，该报道称，由于一些销售人员在上个财政年度未能完成目标，微软降低了部分人工智能软件产品的销售增长目标。 The Information援引了Azure云计算部门的消息来源，该部门是微软人工智能工作的关键领域。微软驳斥了该报道，称人工智能产品的总销售配额并未降低，并批评The Information对销售组织动态的理解。在微软否认后，其股价最初下跌，但随后收复了部分失地。

文章还涉及对人工智能泡沫的广泛担忧，引用了麻省理工学院的一项研究，该研究显示人工智能项目的采用率较低，以及一份报告称凯雷集团削减了对微软Copilot Studio的支出。The Information声称，在未达到目标后，一个Azure销售部门降低了 Foundry 销售的增长目标。尽管承认人工智能采用方面存在潜在挑战，但分析师们仍然对人工智能的潜力持乐观态度。

美国科技公司面临着证明其巨额人工智能投资回报的压力，微软报告了创纪录的资本支出。尽管存在供应限制，微软的Azure云计算部门仍实现了强劲的收入增长，为该公司短暂达到4万亿美元的估值做出了贡献。

---

## 29. C++编译器优化实战

**原文标题**: Optimizations in C++ compilers: a practical journey

**原文链接**: [https://queue.acm.org/detail.cfm?id=3372264](https://queue.acm.org/detail.cfm?id=3372264)

无法访问文章链接。

---

## 30. 印度取消智能手机预装国营网络安全应用程序的命令

**原文标题**: India scraps order to pre-install state-run cyber safety app on smartphones

**原文链接**: [https://www.bbc.com/news/articles/clydg2re4d1o](https://www.bbc.com/news/articles/clydg2re4d1o)

印度撤回强制手机厂商预装政府网络安全应用Sanchar Saathi的命令。此举源于公众强烈抗议以及苹果和三星等科技巨头的抵制，后者对隐私问题和缺乏事先协商表示担忧。

政府最初辩称该应用对于手机验证是必要的，但网络安全专家批评此举侵犯了公民的隐私权。Sanchar Saathi应用旨在帮助用户举报诈骗和验证手机真伪。虽然已有1400万用户下载该应用，并每天报告2000起诈骗案件，但强制预装指令引发了强烈反对。

尽管撤回了命令，印度通信部长保证该应用不会被用于监视。数字权益倡导团体对这一转变表示欢迎，但仍在等待确认撤销该命令和修订网络安全规则的正式法律文件。在正式法律指令发布并得到独立确认之前，他们保持谨慎乐观。

---

## 31. Quad9 DOH HTTP/1.1 服务将于2025年12月15日停止使用

**原文标题**: Quad9 DOH HTTP/1.1 Retirement, December 15, 2025

**原文链接**: [https://quad9.net/news/blog/doh-http-1-1-retirement/](https://quad9.net/news/blog/doh-http-1-1-retirement/)

Quad9 将于 2025 年 12 月 15 日停止支持使用 HTTP/1.1 的 DNS-over-HTTPS (DOH)。此更改主要影响不支持推荐的 DOH HTTP/2 协议的较旧或不兼容设备。大多数现代浏览器和操作系统（Chrome、Firefox、Safari、Android、iOS）不受影响。

依赖 HTTP/1.1 进行 DOH 的用户需要升级其系统，切换到 DNS-over-TLS（不使用 HTTP），或者，作为最后的手段并谨慎操作，恢复到未加密的 DNS。

已知受影响的主要平台是配置为 DOH 的 MikroTik 设备，因为它们目前缺少 HTTP/2 支持。Quad9 已通知 MikroTik，但尚未发布更新公告。可能还有其他物联网设备或软件库也会受到影响。

Quad9 正在逐步淘汰 HTTP/1.1，以简化其代码库、降低潜在的安全风险，并在较新的服务器硬件上部署新功能和协议。支持旧协议需要大量的开发工作，并带来可扩展性方面的挑战。

Quad9 承认给受影响的用户带来了不便，但强调此更改对于整体平台改进是必要的。由于 Quad9 不跟踪用户数据，因此他们依赖社区分享来通知那些受此更改影响的人员。

---

## 32. 尝试使用C++26执行器

**原文标题**: Trying Out C++26 Executors

**原文链接**: [https://mropert.github.io/2025/11/21/trying_out_stdexec/](https://mropert.github.io/2025/11/21/trying_out_stdexec/)

本文详细介绍了作者尝试使用 C++26 executors 以提高 Vulkan 渲染器项目中资源加载速度的经验。受之前使用 TBB 并发优化游戏启动时间的成功经验的启发，作者旨在利用 C++26 executors 进行多线程资源加载，特别是着色器编译和纹理解压缩。

作者最初使用 TBB 实现了一个解决方案，获得了显著的性能提升。然后，他们探索了 NVIDIA 的 stdexec，即 C++26 executors 的参考实现。最初的 stdexec 实现性能不佳，尽管使用了 `stdexec::par_unseq`，`bulk()` 操作仍然串行运行。添加 `continues_on(scheduler)` 解决了这个问题，实现了正确的多线程处理。作者发现语法冗长且容易出错，需要 `just()`、`continues_on()` 和 `then()` 来进行基本的任务链，以及 `let_value()` 来处理运行时依赖项。

作者的结论是，虽然声明式管道语法很吸引人，但潜在的陷阱和冗长性可能会阻碍其应用。他们还强调了对编译时间和管理任务之间数据传递的复杂性的担忧。最终，作者质疑现在标准化 executors 是否为时过早，并建议在标准化之前，通过广泛采用的库获得更多实际经验可能是一种更好的方法，并引用了 Boost 等库的成功经验。目前，作者将继续使用 TBB，因为它可靠且熟悉。

---

## 33. IBM CEO 称在 AI 数据中心上的花费“不可能”获得回报

**原文标题**: IBM CEO says there is 'no way' spending on AI data centers will pay off

**原文链接**: [https://www.businessinsider.com/ibm-ceo-big-tech-ai-capex-data-center-spending-2025-12](https://www.businessinsider.com/ibm-ceo-big-tech-ai-capex-data-center-spending-2025-12)

据商业内幕报道，IBM首席执行官Arvind Krishna对在人工智能数据中心进行大规模投资的盈利能力表示怀疑。他认为目前用于构建支持人工智能的基础设施的支出水平是不可持续的，并且不太可能产生足够的回报。

核心论点是，人工智能数据中心所需的投资规模正在超过潜在的收入来源。Krishna认为，虽然人工智能无疑是一项变革性技术，但目前仅仅专注于构建越来越多的基础设施，而没有明确的盈利途径是一种有缺陷的策略。他暗示，该行业需要将其重点从原始基础设施建设转移到寻找更有效、更有利可图的方式来部署和利用人工智能。

文章没有详细说明Krishna为何这样认为的具体原因，但暗示是成本太高（可能在硬件、能源消耗或维护方面），相对于人工智能服务产生的收入而言。他本质上是在说，围绕人工智能基础设施的淘金热心态正在制造一个注定破裂的泡沫。

---

## 34. Qwen3-VL能扫描两小时的视频并精确指出几乎每一个细节。

**原文标题**: Qwen3-VL can scan two-hour videos and pinpoint nearly every detail

**原文链接**: [https://the-decoder.com/qwen3-vl-can-scan-two-hour-videos-and-pinpoint-nearly-every-detail/](https://the-decoder.com/qwen3-vl-can-scan-two-hour-videos-and-pinpoint-nearly-every-detail/)

阿里巴巴的Qwen3-VL是一款开源多模态AI模型，擅长处理长视频和大量文本。一份技术报告详细介绍了其高精度分析两小时视频的能力，即使在一百万个tokens中也能以99.5%的准确率精确定位特定帧。在视觉数学任务中，它超越了Gemini 2.5 Pro、OpenAI GPT-5和Claude Opus 4.1，在MathVista和MathVision等基准测试中取得了更高的分数。该模型还表现出强大的文档理解能力，在DocVQA和OCRBench上取得了不错的成绩，支持39种语言。

Qwen3-VL在GUI代理任务（如导航界面和操作Android应用）方面也显示出前景。它可以有效地处理复杂的文档和科学图表。然而，在一般推理方面，它落后于竞争对手，这体现在其在MMMU-Pro测试和视频QA基准测试中的表现。

关键的架构升级包括用于改进长视频处理的“交错MRoPE”、用于访问中间视觉编码器结果的DeepStack技术以及用于更好理解基于时间的视频任务的基于文本的时间戳系统。该模型使用一万个GPU在万亿tokens的大规模数据集上进行了训练。参数范围从2B到235B的Qwen3-VL模型在Hugging Face上以Apache 2.0许可证和开放权重提供。

---

## 35. 汽车激光雷达全解析

**原文标题**: All about automotive lidar

**原文链接**: [https://mainstreetautonomy.com/blog/2025-08-29-all-about-automotive-lidar/](https://mainstreetautonomy.com/blog/2025-08-29-all-about-automotive-lidar/)

本文全面概述了汽车激光雷达技术。激光雷达是一种通过向周围表面发射光线并测量其反射回来的时间来测量距离、方位、反射率、速度和环境光的传感器，对于自动驾驶车辆至关重要。

激光雷达的核心围绕着测量距离（测距），主要通过两种方法：测量光线传播所需的时间或使用视差。基于时间的方法包括直接飞行时间脉冲激光雷达和调制激光雷达（幅度或频率）。脉冲激光雷达发射激光脉冲并测量返回时间，这需要像雪崩光电二极管（APD）或单光子雪崩二极管（SPAD）这样的快速传感器。SPAD具有诸如CMOS兼容性和更高增益的优点，但存在死区时间的问题。SPAD宏像素结合了多个SPAD以减轻这些缺点。多重拍摄测距通过发射多个脉冲来提高信号强度。硅光电倍增管是SPAD的组合。

幅度调制激光雷达使用快速闪烁的灯和探测器，通过检查落在具有不同相位的探测器上的光线的比例来估计范围，但测距精度较差。频率调制激光雷达使用快速改变频率的激光器。

分辨方位是通过阵列（离散或固态）和各种扫描/光束控制方法来实现的。这些方法包括旋转系统、旋转镜、振荡镜、MEMS镜、光学相控阵、Baraja SpectrumScan和里斯利棱镜。一些系统还结合了两种一维方法来确定方位。本文详细介绍了每种技术的优缺点以及最适合它们的特定应用。

---

## 36. 音乐认知中是否存在普遍性？(2024)

**原文标题**: What, if anything, is universal to music cognition? (2024)

**原文链接**: [https://www.nature.com/articles/s41562-023-01800-9](https://www.nature.com/articles/s41562-023-01800-9)

这项2024年的研究调查了音乐认知的普遍性，特别是关注人类如何在不同文化中对节奏进行心理表征。研究人员测量了来自15个国家、39个参与者群体（包括城市和土著人口）的节奏“先验”——人们感知和再现节奏的潜在偏见。实验采用了一种“传话游戏”方法，参与者再现一个节奏，然后他们的再现被迭代地用作刺激。这种方法使研究人员能够估计每个群体的潜在节奏“先验”。

关键发现是，**所有测试的群体都表现出稀疏先验，其特征是在整数比率的节奏处出现峰值**，这表明人们普遍倾向于基于简单的数学比率以离散的类别来感知节奏。然而，特定整数比率的显著性在不同群体之间差异很大，这可能反映了当地的音乐传统。

该研究表明，**基于小整数比率的离散节奏类别是音乐认知的一个共同特征**，在文化传播中起着稳定作用。这些普遍的趋势与特定文化的音乐实践相互作用，从而产生了全球观察到的节奏表达的丰富多样性。这项研究强调了跨文化研究在理解音乐感知背后的基本认知机制方面的重要性。作者在使用“西方”与“非西方”二分法对参与者进行分类时也持谨慎态度，承认其局限性和历史偏见。

---

## 37. 反伽罗瓦洋葱：改进的Tor电路流量加密

**原文标题**: Counter Galois Onion: Improved encryption for Tor circuit traffic

**原文链接**: [https://blog.torproject.org/introducing-cgo/](https://blog.torproject.org/introducing-cgo/)

本文宣布即将用一种新的、经过研究支持的设计——计数器伽罗瓦洋葱(Counter Galois Onion, CGO)——取代Tor的"tor1"中继加密算法。其目标是增强用户安全性，防御范围更广的攻击者，主要通过缓解可能导致用户去匿名化的“标记攻击”。

当前的"tor1"算法使用AES-128-CTR流密码进行加密，并使用4字节摘要进行身份验证。由于加密的可塑性（允许攻击者修改密文并预测更改），这使其容易受到标记攻击。它也缺乏前向保密性（被泄露的密钥可以解密过去的流量），并且使用SHA-1的4字节摘要较弱。

CGO通过使用一种名为UIV+的坚固伪随机置换(Rugged Pseudorandom Permutation, RPRP)结构来解决这些问题，提供了一种宽块密码，如果消息被篡改，则会使整个消息无法恢复。标签值的链式连接确保消息完整性取决于所有先前的消息。通过每次单元的密钥转换（“更新”算法）来实现前向保密，从而防止使用被泄露的密钥解密早期流量。身份验证器摘要也已升级到16字节。

虽然CGO是一种较新的设计，但作者认为它比tor1提供了显著的安全改进，使其值得应用，即使存在潜在的、未被发现的弱点。 Arti（Rust Tor）和C Tor都在进行实施，需要代码重构以适应新的加密并为未来的更改做好准备。

---

## 38. 理解 ECDSA

**原文标题**: Understanding ECDSA

**原文链接**: [https://avidthinker.github.io/2025/11/28/understanding-ecdsa/](https://avidthinker.github.io/2025/11/28/understanding-ecdsa/)

本文自下而上地解释了椭圆曲线数字签名算法 (ECDSA)，重点介绍以太坊使用的版本。它面向对公钥密码学有基本了解，但寻求比典型的面向开发者的解释更深入、更直观的理解的读者。

作者强调一种“建设性”的方法，从基本原理构建理解，无需外部资源。这导致了有见地但可能非标准和幼稚的解释，促使读者批判性地评估内容。

本文首先详细解释了模算术，涵盖了等价类、模运算符和乘法逆元等概念。它强调，一个数如果与p互质，则总是可模p求逆的。

扩展欧几里得算法 (EEA) 被介绍为计算乘法逆元的实用方法。本文演示了计算最大公约数 (GCD) 的算法步骤，并找到整数 x 和 y，使得 ax + py = GCD(a, p)。文章包含了欧几里得算法核心原理有效性的证明。

本文强调了批判性思维和独立验证在理解数学概念中的作用。

---

## 39. 亚马逊推出Trainium3

**原文标题**: Amazon launches Trainium3

**原文链接**: [https://techcrunch.com/2025/12/02/amazon-releases-an-impressive-new-ai-chip-and-teases-a-nvidia-friendly-roadmap/](https://techcrunch.com/2025/12/02/amazon-releases-an-impressive-new-ai-chip-and-teases-a-nvidia-friendly-roadmap/)

亚马逊云科技(AWS)在2025 AWS re:Invent大会上发布了其新型AI训练芯片Trainium3。这款第三代芯片和配套的UltraServer系统相比上一代产品性能显著提升，速度快4倍，内存多4倍，能效提高40%。每个UltraServer可容纳144个芯片，数千个服务器可以连接成总计100万个Trainium3芯片的集群，从而更快地进行AI训练和推理，并为客户节省成本。

AWS已经在开发下一代产品Trainium4，它将支持英伟达的NVLink Fusion技术，从而实现与英伟达GPU的互操作性。此举旨在通过结合亚马逊的低成本服务器技术和英伟达的广泛采用技术，将为英伟达CUDA平台构建的AI应用吸引到AWS云。

包括Anthropic和Karakuri在内的多家客户已经在使用Trainium3来降低推理成本。虽然AWS没有公布Trainium4的发布日期，但预计将在明年的大会上公布更多信息。Trainium3的发布和Trainium4的开发凸显了AWS致力于构建自己的AI训练芯片，并为其云客户提供经济高效、高性能的AI解决方案的决心。

---

## 40. 高粮价将使公共食品杂货店成为必然

**原文标题**: Why High Food Prices Will Make Public Groceries Inevitable

**原文链接**: [https://grocerynerd.substack.com/p/grocery-update-116-why-high-food](https://grocerynerd.substack.com/p/grocery-update-116-why-high-food)

无法访问文章链接。

---

## 41. 学校禁止手机与学生成绩

**原文标题**: School cell phone bans and student achievement

**原文链接**: [https://www.nber.org/digest/202512/school-cell-phone-bans-and-student-achievement](https://www.nber.org/digest/202512/school-cell-phone-bans-and-student-achievement)

NBER文摘：佛罗里达州大学区手机禁令的影响

本NBER文摘总结了Figlio和Özek的一篇工作论文，该论文研究了佛罗里达州一大型学区严格手机禁令的影响。该禁令要求学生在整个上课期间保持手机静音并收好。研究人员比较了禁令实施前（2022-23学年）与禁令实施后两年（2023-24学年和2024-25学年）的学生数据，以及智能手机活动数据。

研究发现，禁令实施后，学校的手机使用量显著下降。最初，停学处分有所增加，尤其是在黑人男学生中，但到第二年恢复到禁令实施前的水平。考试成绩在第一年没有显著变化。然而，在第二年，成绩显著提高（平均提高1.1个百分点），尤其是在春季学期。成绩的提高主要集中在男学生（提高1.4个百分点）以及初中和高中学生（提高1.3个百分点）中。

研究人员还观察到禁令实施后无故缺勤人数减少，这表明出勤率提高与考试成绩提高之间可能存在联系。该研究表明，虽然实施手机禁令最初可能导致纪律方面的挑战，但随着时间的推移，它可以带来学业成绩的提高，特别是对于特定学生群体。该研究由史密斯·理查森基金会资助。

---

## 42. 涩谷区取消新年倒计时活动；将加强安保。

**原文标题**: Shibuya Ward cancels New Year countdown event; security to be tightened

**原文链接**: [https://japantoday.com/category/national/Shibuya-Ward-cancels-New-Year-countdown-event-security-to-be-tightened](https://japantoday.com/category/national/Shibuya-Ward-cancels-New-Year-countdown-event-security-to-be-tightened)

东京涩谷区已取消年度跨年倒计时活动，理由是担心过度拥挤以及过去发生的公共场所醉酒和轻微骚乱事件，可能危及安全。这已是该活动连续第四年被取消，此举旨在防止大量人群聚集和在热门地区可能出现的混乱。

尽管活动取消，涩谷区将在跨年夜大幅加强涩谷地区的安保措施。这些措施包括部署更多保安人员，增加多种语言的警告标志数量，限制涩谷十字路口周围的交通，以及从12月下旬到1月初禁止在车站周围的公共街道和公园饮酒。他们还与铁路运营商协调，以管理从车站出站的人群。

该区强调，虽然官方活动已取消，但他们预计仍会有大量人群聚集。因此，加强安保措施是为了确保公共安全并在整个新年假期期间维持秩序。目的是防止因大量人群聚集而产生的任何危险情况，并保护居民和游客。

---

## 43. Show HN: Taka编程语言

**原文标题**: Show HN: The Taka Programming Language

**原文链接**: [https://codeberg.org/marton/taka](https://codeberg.org/marton/taka)

无法访问文章链接。

---

## 44. 在NASA小行星贝努样本中发现糖类、“口香糖”和星尘

**原文标题**: Sugars, 'Gum,' Stardust Found in NASA's Asteroid Bennu Samples

**原文链接**: [https://www.nasa.gov/missions/osiris-rex/sugars-gum-stardust-found-in-nasas-asteroid-bennu-samples/](https://www.nasa.gov/missions/osiris-rex/sugars-gum-stardust-found-in-nasas-asteroid-bennu-samples/)

美国宇航局对奥西里斯-雷克斯任务带回的小行星贝努样本的分析揭示了关于早期太阳系和生命起源的突破性发现。

首先，科学家在样本中发现了对生命至关重要的糖类，包括核糖和葡萄糖。这一发现，结合之前对氨基酸和其他生物构件的探测，表明RNA以及潜在的早期生命所需的成分在早期太阳系中广泛存在。值得注意的是，核糖的存在和脱氧核糖的缺失支持了“RNA世界”假说。

其次，发现了一种前所未见的独特胶状物质。这种富含氮和氧的物质，很可能是在贝努的母体小行星中形成的，可能为地球上生命的触发提供了必要的化学前体。据推测，这种“太空胶”是通过氨基甲酸酯的聚合形成的，可能早于小行星上的水环境。

第三，样本中含有出乎意料的高丰度的超新星爆炸尘埃（太阳前颗粒）。这表明贝努的母体是在富含这种尘埃的原行星盘区域形成的。此外，研究表明，虽然贝努的母体小行星经历了流体的大量改变，但仍保留了未发生明显改变的物质，为了解其起源提供了宝贵的见解。

这些发现共同有助于理解太阳系的形成、生命构件的分布以及可能导致地球生命出现的条件。

---

## 45. 毁灭战士本可以有PC扬声器音乐

**原文标题**: DOOM could have had PC Speaker Music

**原文链接**: [https://lenowo.org/viewtopic.php?t=45](https://lenowo.org/viewtopic.php?t=45)

本文讨论了一个项目，旨在在经典游戏《DOOM》中启用PC扬声器音乐，这在之前被认为对资源消耗过大。作者创建了一种自定义的“pcsp”文件格式，用于在32位系统上高效播放PC扬声器音乐，其中包含指定频率和持续时间的一系列音调单元。

实现这一点的关键是修改《DOOM》的`sndserver`（声音服务器），以包含PC扬声器输出的优先级混音器，类似于处理Adlib声音的方式。这涉及到整合新的pcsp格式，并允许游戏转换为扬声器输出。

作者发现，即使在《DOOM》最初发布的硬件上，实施此补丁对游戏的性能也没有明显影响。他计划公开发布该补丁，但希望首先添加更多除E1M1之外的音乐曲目，并解决现代Linux系统上sndserver中其他潜在问题。该项目表明，通过PC扬声器在《DOOM》中播放音乐确实是可行的，这打破了之前关于其资源需求的假设。

---

## 46. 小型餐厅和咖啡馆的免费静态网站生成器

**原文标题**: Free static site generator for small restaurants and cafes

**原文链接**: [https://lite.localcafe.org/](https://lite.localcafe.org/)

本文描述了一种需求：一款专为小型餐厅和咖啡馆量身定制的免费静态网站生成器。虽然文章未提及任何具体生成器，但通过提供示例内容（一道菜品描述）暗示了其潜在应用。这个单一条目展示了该生成器在显示食物项目及其价格、成分、描述和膳食信息（无麸质、含乳制品）方面的作用。该示例以“沙拉”为例，价格为17.89美元，并列出了其成分：罗马生菜、田园蔬菜、培根、番茄、煎鸡胸肉、无笼鸡蛋和蓝纹奶酪酱。它被归类为“沙拉”和“配菜”，表明该生成器最好能支持分类和菜单组织。因此，本文隐含地表明，这款静态网站生成器应能够为小型餐饮企业呈现一个简单、易于导航且信息丰富的在线菜单。

---

## 47. 发送 DMARC 报告具有一定的风险。

**原文标题**: Sending DMARC reports is somewhat hazardous

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/spam/DMARCSendingReportsProblems](https://utcc.utoronto.ca/~cks/space/blog/spam/DMARCSendingReportsProblems)

克里斯·西本曼的博客（漫游思绪）正在实施激进的反爬虫措施，原因是大量使用旧浏览器用户代理（尤其是 Chrome）的高流量爬虫激增。这些预防措施旨在降低服务器负载，但可能无意中阻止使用较旧或不常见浏览器的合法用户。

如果用户遇到屏蔽，很可能是因为他们的浏览器被认为过旧或可疑。西本曼鼓励遇到此问题的用户联系他并提供他们的浏览器详细信息（尤其是 User-Agent 字符串）以进行故障排除。

一个特殊的问题是像 archive.today、archive.ph 和 archive.is 这样的存档服务。这些服务使用与恶意机器人无法区分的方法抓取网站：旧的 Chrome User-Agent 字符串、广泛分布且无法识别的 IP 地址以及伪造的反向 DNS 条目。西本曼建议改用 archive.org，因为它以更负责任的方式抓取网站，并且能够存档他的博客。总体的目标是保护博客免受资源密集型爬虫的侵害，即使这会给一些用户带来不便。

---

## 48. 瓢虫月报：2025年11月

**原文标题**: This Month in Ladybird: November 2025

**原文链接**: [https://buttondown.com/ladybird/archive/this-month-in-ladybird-november-2025/](https://buttondown.com/ladybird/archive/this-month-in-ladybird-november-2025/)

Ladybird浏览器引擎本月进展：2025年11月

本文总结了Ladybird浏览器引擎的进展。11月，来自34位贡献者的215个拉取请求被合并。主要亮点包括欢迎37signals、Coursiv和Andrew Mead等新赞助商，以及Web平台测试（WPT）通过数量的显著增加，达到近200万。

团队实现了对可变字体的支持，可动态调整字体宽度和粗细，并添加了CSS属性`perspective`和`perspective-origin`，以改进3D变换。通过移除缓冲模式，Fetch API得到了简化，从而实现了增量数据传递，例如ChatGPT的响应方式。WebGL的alpha预乘处理得到了修复，SVG支持得到了增强，包括`<feComponentTransfer>`和`<feMorphology>`等功能。

Base64转换的性能得到了改进，速度显著提高。CSS @import规则现在会阻塞首次渲染，以防止FOUC。嵌入在`<img>`标签中的SVG图像现在可以使用GPU加速，从而实现更快的渲染。`setInterval()`回调计时得到了改进，运行更加流畅，并且现在可以使用JavaScript编写原生函数，从而开启了新的功能。DNS-over-HTTPS的开发取得了进展。最后，媒体处理得到了改进，包括WebM/Matroska解复用器的增强和H.264视频播放的修复。Windows支持也取得了进展。

---

## 49. 载入ZX Spectrum – 首个献给我们首台个人电脑的博物馆

**原文标题**: Load ZX Spectrum – first Museum dedicated to our first personal computer

**原文链接**: [https://loadzx.com/en/](https://loadzx.com/en/)

位于葡萄牙坎塔涅迪的LOAD ZX Spectrum博物馆致力于展示ZX Spectrum个人电脑及其相关技术。馆内陈列着由João Diogo Ramos收集的大量藏品，展现了ZX Spectrum对技术和文化，尤其是在葡萄牙的影响。

该博物馆着重介绍了ZX Spectrum在向大众普及技术方面所起的作用，以及它对技术革命的影响。游客可以了解20世纪80年代葡萄牙在TIMEX工厂中所扮演的角色，向使ZX Spectrum声名鹊起的发明家和游戏致敬，并欣赏为该系统仍在开发的新游戏和电脑。

博物馆提供葡萄牙语和英语导览，并计划提供西班牙语导览。博物馆收入将重新投入。欢迎游客拍照和录像，并可在馆内查阅书籍和杂志。

用户评论强调了博物馆令人印象深刻的藏品、馆长的热情以及它所提供的怀旧体验。博物馆周二至周日开放，时间为上午10点至下午6点，免费入场。团体导览需付费，当地学校、非营利组织和大家庭可享受折扣。

博物馆还提供有关如何前往坎塔涅迪的信息，包括从里斯本和波尔图出发的路线、公共交通选择以及巴士时刻表。同时还提供当地住宿和停车的建议。

---

## 50. OpenAI宣布进入“红色警戒”，因谷歌在人工智能竞赛中赶上。

**原文标题**: OpenAI declares 'code red' as Google catches up in AI race

**原文链接**: [https://www.theverge.com/news/836212/openai-code-red-chatgpt](https://www.theverge.com/news/836212/openai-code-red-chatgpt)

据The Verge报道，OpenAI首席执行官山姆·奥特曼已宣布进入“红色警戒”状态，这表明随着竞争对手，特别是谷歌，正在缩小在人工智能竞赛中的差距，该公司内部的压力日益增加。《华尔街日报》和The Information的报道显示，OpenAI正在推迟多项计划，包括广告、购物、健康代理以及名为Pulse的个人助理的计划功能，以便专注于改进ChatGPT的核心功能。

重新调整的重点是提高ChatGPT的速度、可靠性、个性化以及回答更广泛问题的能力。将实施每日电话会议和临时团队调动以加速开发。这种紧迫性反映了OpenAI在应对高成本并争取盈利的关键时刻。

文章强调了谷歌的进步是OpenAI担忧的主要因素。谷歌在回应ChatGPT时也发起了自己的“红色警戒”，其人工智能用户群一直在增长，这得益于Nano Banana图像模型等成功工具。谷歌最新的AI模型Gemini 3在各种行业基准和指标中都超越了竞争对手，进一步巩固了其在人工智能领域的地位。文章阐述了人工智能行业中不断变化的格局，OpenAI的优势正受到谷歌进步的挑战。

---

## 51. 十亿行数据上的10万TPS：SQLite的惊人效率

**原文标题**: 100k TPS over a billion rows: the unreasonable effectiveness of SQLite

**原文链接**: [https://andersmurphy.com/2025/12/02/100000-tps-over-a-billion-rows-the-unreasonable-effectiveness-of-sqlite.html](https://andersmurphy.com/2025/12/02/100000-tps-over-a-billion-rows-the-unreasonable-effectiveness-of-sqlite.html)

本文论证了SQLite在处理高吞吐量、交互式事务处理，尤其是处理大型数据集（10亿行）时，具有出人意料的可扩展性。它认为SQLite的嵌入式特性和单写者架构，通常被认为是限制，实际上是优势，可以最大限度地减少网络延迟的影响，而网络延迟是像PostgreSQL这样的网络数据库的关键瓶颈。

作者使用基于Clojure的基准测试，在Apple M1 Pro上证明，SQLite可以实现比PostgreSQL更高的每秒事务数（TPS），尤其是在引入网络延迟的情况下。虽然PostgreSQL在低延迟环境中表现良好，但由于Amdahl定律和跨网络的行锁定，其性能会随着网络延迟的微小增加而迅速下降。

SQLite通过消除网络开销，避免了这个问题。此外，单写者架构允许对事务进行简单的批处理，从而进一步提高了性能。文章通过使用SQLite的SAVEPOINT功能，在批处理中进行细粒度回滚，解决了对事务隔离的担忧。

文章还考虑了并发读取，模拟了真实的读/写混合（75/25），并表明即使在这种负载下，SQLite仍能保持令人印象深刻的TPS。作者提供了在各种条件下（包括不同的网络延迟、隔离级别和连接池大小）比较PostgreSQL和SQLite的基准测试结果。

关键的结论是，对于需要高TPS和大型数据集的应用程序，尤其是在网络延迟是限制因素的情况下，SQLite可能是一种出人意料的有效解决方案。但是，作者警告说，SQLite并非万能药，只有那些了解其局限性并能够轻松管理备份和副本的人才应该使用它。文章最后提供了相关主题的进一步阅读链接，例如Amdahl定律、SQLite扩展和Litestream。

---

## 52. 日本游戏开发者面临字体困境：授权费从 380 美元涨至 2 万美元

**原文标题**: Japanese game devs face font dilemma as license increases from $380 to $20k

**原文链接**: [https://www.gamesindustry.biz/japanese-devs-face-font-licensing-dilemma-as-leading-provider-increases-annual-plan-price-from-380-to-20000](https://www.gamesindustry.biz/japanese-devs-face-font-licensing-dilemma-as-leading-provider-increases-annual-plan-price-from-380-to-20000)

日本游戏开发者正面临着字体授权成本大幅上涨带来的严峻挑战。主要字体授权服务商Fontworks LETS停止了其价格合理的（每年约380美元）游戏授权计划，并由其母公司Monotype推出了一项价格高昂得多的计划，费用高达20,500美元，用户上限为25,000。这项新计划缺乏针对日本开发者的本地定价，这对于大型工作室来说尤其成问题。

由于难以找到能够准确渲染汉字和片假名字符的合适且价格合理的字体，这个问题更加严重。这种突然的价格上涨引起了广泛关注，特别是对于需要大量重新测试和质量保证的在线服务游戏，如果被迫更换字体，情况将更加糟糕。

情况非常严峻，一些工作室甚至可能被迫进行品牌重塑，如果他们的企业形象严重依赖于他们再也负担不起的商业字体。独立开发者和老牌工作室都在努力寻找可行且价格合理的替代方案，以应对这场字体授权危机。

---

## 53. 任务关键型高级调度（ALAP/ASAP）系统

**原文标题**: Mission Critical Advanced Scheduling (ALAP/ASAP) System

**原文链接**: [https://github.com/rodmena-limited/scriptplan](https://github.com/rodmena-limited/scriptplan)

ScriptPlan：一款任务关键型、先进的调度系统，具有分钟级精度，专为资源分配和依赖关系管理而设计。它兼容 TaskJuggler 的 .tjp 语法，便于轻松采用。可通过 `pip install scriptplan` 进行安装。

主要功能包括生成 JSON 和 CSV 格式的报告，支持 Unix 风格的管道，并与 `jq` 和 `csvkit` 等工具集成。它具有基于内容的 SHA256 报告 ID、小写列名、无 HTML 元数据、无文件污染，并且对于并发执行是安全的。还提供 Python API 以进行编程访问。

ScriptPlan 通过了“机场级/任务关键型”使用认证，经验证具有时间物理学、资源约束（每日/每周限制、分层配额、班次交叉）、高级调度（ALAP、优先级抢占、智能资源选择）和工作流程逻辑（原子性、易腐性、零缓冲同步）方面的能力。它使用整数算术精确处理非标准班次边界、素数持续时间、资源争用以及日历/工作时间间隔，以避免浮点错误。

一个示例项目演示了制造过程的 ALAP 调度，解决了资源争用并遵循工作时间。该项目在 Apache 2.0 许可下获得许可，并由 Highway Workflow Engine 的 Farshid 开源。它利用 TaskJuggler 的语法以便于使用，并承认 TaskJuggler 在原始项目定义语言方面的贡献。

---

## 54. 我设计并打印了一个定制的鼻罩，以帮助我的狗狗治疗DLE。

**原文标题**: I designed and printed a custom nose guard to help my dog with DLE

**原文链接**: [https://snoutcover.com/billie-story](https://snoutcover.com/billie-story)

本文讲述了比特犬比莉的故事。比莉被诊断出患有盘状红斑狼疮 (DLE)，这是一种影响她鼻子的自身免疫性疾病。这种疾病导致色素流失、结痂、脱屑和疼痛，阳光照射会加剧这些症状。传统的治疗方法，如防晒霜和药物，都证明无效，因为比莉会舔掉它们，或者用布料遮挡也会被蹭掉。把她关在室内大大降低了她的生活质量。

出于爱和无奈，作者使用 3D 打印机设计并制作了 SnoutCover，一种定制的鼻子防护罩。设计过程涉及多次迭代，最初使用 PLA 进行初始测量，然后过渡到柔软的 TPU 以提高舒适度。早期的原型缺乏通风和适当的贴合度，但通过不断的重新设计，包括增加通风孔和可调节的带子系统，最终实现了功能性和舒适性的设计。

SnoutCover 有效地保护了比莉的鼻子免受紫外线伤害，防止她舔掉药物，并能牢固地固定到位。使用 SnoutCover 五个月后，比莉的鼻子完全痊愈：出血停止了，结痂减少了，色素恢复了，皮肤质地也得到了改善。

受到 Reddit 和 MakerWorld 上积极回应的启发，作者在 MakerWorld 上免费分享 SnoutCover 的设计，希望能帮助其他患有 DLE 或类似鼻子疾病的狗狗。该设计适用于中型到大型犬，并且可以在切片软件中进行调整。文章强调，SnoutCover 源于爱，以及不接受比莉的痛苦是不可避免的这种想法，为其他面临类似挑战的狗父母提供了希望。

---

## 55. Beej的计算机科学学习指南

**原文标题**: Beej's Guide to Learning Computer Science

**原文链接**: [https://beej.us/guide/bglcs/](https://beej.us/guide/bglcs/)

《Beej计算机科学学习指南》是一份仍在完善中的指南，目前处于测试阶段，旨在帮助个人学习计算机科学。作者Beej邀请读者提供反馈和更正，以改进文档。该指南提供多种格式，包括HTML（针对不同屏幕尺寸和传输方式的多个版本）和PDF（美国信纸和A4尺寸，单面和双面打印选项，以及带或不带语法高亮）。

该文档还为希望为指南做出贡献的翻译者和编写者提供资源，提供有关如何从GitHub克隆项目并遵循README的说明。如有疑问和反馈，可直接通过beej@beej.us联系Beej。该指南目前尚未完成，但希望对大家有所帮助，并提供不同的格式以提高可访问性。

---

## 56. Ecosia：最环保的AI来了

**原文标题**: Ecosia: The greenest AI is here

**原文链接**: [https://blog.ecosia.org/ecosia-ai/](https://blog.ecosia.org/ecosia-ai/)

Ecosia，种树的搜索引擎，正推出名为“概览”和“AI搜索”的AI驱动功能，同时坚持其对环境责任和用户隐私的承诺。“概览”在搜索结果顶部提供带有引用的简洁摘要，用户可以选择禁用以获得经典体验。“AI搜索”提供交互式聊天模式，用于解答详细问题和提供环保建议。

Ecosia通过在其AI开发中优先考虑可持续性来突出自身。它使用更小、更高效的AI模型，并避免使用视频生成等能源密集型功能。此外，Ecosia产生的可再生能源超过其AI功能消耗的能源，并投资1800万欧元于太阳能和风能项目以替代化石燃料。该公司使用AI能量评分和Ecologits等工具来跟踪其能源使用情况。

隐私是另一个关键关注点。Ecosia只收集必要的数据并遵守GDPR法规。它已启动其独立的欧洲搜索索引，以保持对其技术的控制并确保其保持对隐私的友好性。作为一家公司，Ecosia不运营电子邮件或地图等其他平台，以避免收集过多的用户数据。

Ecosia邀请用户提供反馈以改进其AI功能，并鼓励合作以构建一个既重视智能又重视环境友好的未来。

---

## 57. Mistral 3模型系列发布

**原文标题**: Mistral 3 family of models released

**原文链接**: [https://mistral.ai/news/mistral-3](https://mistral.ai/news/mistral-3)

Mistral AI 发布 Mistral 3 系列开源 AI 模型，包括旗舰模型 Mistral Large 3（稀疏混合专家模型）和专为边缘和本地使用设计的 Ministral 3 系列。这些模型以 Apache 2.0 许可证发布，旨在提高可访问性和定制性。

Mistral Large 3 被誉为最先进的开源模型，在 NVIDIA H200 GPU 上训练，在通用提示中与领先的指令调优模型持平，并在图像理解和多语言对话方面表现出色。它在 LMArena 等排行榜上也表现出色。推理版本正在计划中。

Ministral 3 系列包含三个模型（3B、8B 和 14B 参数），具有基础、指令和推理变体，全部具有图像理解能力。它们专为高效性能和良好的性价比而设计。

Mistral 与 NVIDIA、vLLM 和 Red Hat 合作，优化并提高其模型的可访问性。它们已在 NVIDIA Hopper GPU 上进行训练，并在 TensorRT-LLM 和 SGLang 上针对整个 Mistral 3 系列进行了优化推理支持，以实现高效的低精度执行，并且具有 NVFP4 格式的检查点可用于高效利用。

Mistral 3 可在 Mistral AI Studio、Amazon Bedrock、Azure Foundry、Hugging Face 等平台上使用。还提供定制模型训练服务，以满足量身定制的 AI 解决方案的需求。此次发布强调开放访问、多模态、多语言能力、可扩展的效率以及对各种应用程序的适应性。

---

## 58. 是的通知

**原文标题**: YesNotice

**原文链接**: [https://infinitedigits.co/docs/software/yesnotice/](https://infinitedigits.co/docs/software/yesnotice/)

YesNotice，于2025年10月10日发布，是一个软件组合项目。其核心功能是向用户提供实时通知，每当他们跟踪的事物从负面（“否”）状态变为正面（“是”）状态时。本质上，该网站会主动提醒用户他们正在监控的信息或状态的积极转变。

---

## 59. 童年及早期职业生涯片段

**原文标题**: A series of vignettes from my childhood and early career

**原文链接**: [https://www.jasonscheirer.com/weblog/vignettes/](https://www.jasonscheirer.com/weblog/vignettes/)

本文以一系列幽默的轶事短篇，反思作者在软件开发领域的经验，以及该领域衰落的预测如何一再被证明是错误的。

最初的几个故事围绕着软件工程将会过时的想法展开，先是由于面向对象编程，然后是多媒体，后来是像IntelliJ这样强大的IDE。在每一种情况下，专家们都预测编程工作的终结，因为技术将自动化地取代对人类程序员的需求。然而，作者指出，新的问题总是会出现，技术只是进化到更高的抽象层次，需要更复杂的解决问题的能力。

接着，作者分享了两个关于自动化任务的故事，一次是通过自动化迁移过程帮助承包商摆脱困境，另一次是自动化了自己用Excel表格更新网站数据的工作。在这两种情况下，失业的预测都没有实现，无论是对承包商还是作者而言。

文章随后将早期NLP项目中负责任的数据收集实践与当前围绕LLM的环境进行了对比。作者回忆起一丝不苟地尊重版权和许可，这与今天使用的数据实践形成了鲜明对比。

最后，作者将互联网泡沫与Web 2.0时代进行了对比，观察到互联网的承诺是通过有机增长和可靠的商业模式实现的，而不是通过强制集成和炒作实现的。

最后，作者透露本文是对当前围绕大型语言模型（LLM）炒作的一系列“被动攻击”，可能暗示着类似的关于过时的预测正在发生。

---

## 60. 苹果将在14年来首次超越三星成为智能手机出货量第一

**原文标题**: Apple to beat Samsung in smartphone shipments for first time in 14 years

**原文链接**: [https://sherwood.news/tech/apple-to-beat-samsung-in-smartphone-shipments-for-first-time-in-14-years/](https://sherwood.news/tech/apple-to-beat-samsung-in-smartphone-shipments-for-first-time-in-14-years/)

据CNBC引用的Counterpoint Research报告显示，苹果预计将在14年来首次超越三星，成为智能手机出货量第一的厂商。 在iPhone 17的推动下，苹果预计将在2025年出货约2.43亿部手机，占据全球19.4%的市场份额。 三星预计将出货2.35亿部手机，市场份额为18.7%。 该报告认为，苹果预计领先的原因在于有利的升级周期以及明年即将发布的更实惠的入门级iPhone。 这些因素预计将有助于苹果在未来几年保持其在智能手机市场的领导地位。

---

## 61. 用Strudel学习音乐

**原文标题**: Learning music with Strudel

**原文链接**: [https://terryds.notion.site/Learning-Music-with-Strudel-2ac98431b24180deb890cc7de667ea92](https://terryds.notion.site/Learning-Music-with-Strudel-2ac98431b24180deb890cc7de667ea92)

这看起来像 Notion 页面上的一个损坏的占位符或错误提示信息。 并没有关于“使用 Strudel 学习音乐”的实际内容。整个内容是一个使用 Notion 需要 JavaScript 的通知，以及启用 JavaScript 的说明。

因此，总结为：

这不是一篇文章，而是来自 Notion 的一个通知。它表明该网页需要 JavaScript 才能运行，并指示用户启用它。没有关于使用 Strudel 学习音乐的内容。

---

## 62. 所有DirectX 12文档来源

**原文标题**: All Sources of DirectX 12 Documentation

**原文链接**: [https://asawicki.info/news_1794_all_sources_of_directx_12_documentation](https://asawicki.info/news_1794_all_sources_of_directx_12_documentation)

所有DirectX 12文档来源

这篇名为“所有DirectX 12文档来源”的博文讨论了官方DirectX 12文档分散且不完整的现状，并为开发者整理了一份资源列表。

作者强调了完备的图形API文档的重要性，并将这种情况与Vulkan更完整（尽管形式化）的规范进行了比较。 然后，他们批评了DirectX 12文档的碎片化状态，这些文档分散在多个网站和格式中。

该文章列出了六个主要的DirectX 12文档来源：

1.  **Direct3D 12编程指南 @ learn.microsoft.com：** 这被认为是主要的文档中心，但也被认为是是不完整的。
2.  **Direct3D 11.3功能规范：** 一个较旧的文档，可以填补D3D12文档中缺失的空白。
3.  **github.com/microsoft/DirectX-Specs：** 一个GitHub仓库，包含Agility SDK中引入的较新的DirectX 12功能的文档。
4.  **github.com/microsoft/DirectXShaderCompiler/wiki：** 一个专门介绍HLSL着色器语言和编译器的GitHub Wiki。
5.  **github.com/microsoft/hlsl-specs：** 另一个GitHub仓库，包含HLSL规范的“工作草案”和未来语言功能的提案。
6.  **DirectX开发者博客：** 一个发布与DirectX相关的新闻、更新和独立文章的博客。

作者对这种缺乏组织的情况表示沮丧，并将其归因于微软内部因素，例如专注于新功能而忽视了详尽的文档，以及组织结构反映了文档的碎片化。他们以充满希望的结尾，引用了诸如HLSL规范之类的举措，认为情况可能会有所改善。最后，作者提到了DirectX 登陆页面，该页面收集了许多与 DirectX 相关的 SDK、工具、助手、示例和其他项目的链接。

---

## 63. DNA分析表明，第一批澳大利亚人大约在六万年前抵达。

**原文标题**: DNA analysis suggests first Australians arrived about 60k years ago

**原文链接**: [https://www.abc.net.au/news/science/2025-11-29/sahul-aboriginal-australia-65000-genetic-evidence/106054352](https://www.abc.net.au/news/science/2025-11-29/sahul-aboriginal-australia-65000-genetic-evidence/106054352)

ABC科学文章：DNA分析表明首批澳大利亚人约六万年前抵达

---

## 64. YouTube 提升 FreeBASIC 性能 (2019)

**原文标题**: YouTube increases FreeBASIC performance (2019)

**原文链接**: [https://freebasic.net/forum/viewtopic.php?t=27927](https://freebasic.net/forum/viewtopic.php?t=27927)

无法访问文章链接。

---

## 65. 实用操作转换入门

**原文标题**: Practical Intro to Operational Transformation

**原文链接**: [https://archive.casouri.cc/note/2025/practical-intro-ot/](https://archive.casouri.cc/note/2025/practical-intro-ot/)

本文对协同编辑技术——操作转换(OT)提供了一个实用的介绍。首先将OT与无冲突复制数据类型(CRDTs)进行对比，后者是协同编辑的另一种主要方法。OT转换插入和删除等操作，以确保并发编辑发生时的一致性，而CRDTs则通过可以以任何顺序应用的操作来保证最终一致性。

本文强调不存在单一“最佳”的OT算法，并突出了不同算法之间的权衡。它介绍了关键的OT概念，包括转换属性(TP1和TP2)，这些属性定义了转换的正确性。TP1很容易满足，而TP2很少满足，需要控制算法来管理操作排序。

OT的核心组成部分是控制算法，它确保操作根据其上下文（操作创建时文档的状态）进行正确的转换。本文还深入探讨了在OT中实现“撤销”功能的复杂性，解释了逆属性（IP1、IP2和IP3）以及墓碑（标记已删除的字符而不实际删除它们）如何简化撤销过程。

最后，本文介绍了一种简化的OT算法，该算法使用基于字符串的插入和删除操作，一个用于管理全局操作序列的中央服务器，以及用于简化撤销功能的墓碑。虽然这种简化的算法不支持富文本或分布式，但它提供了一个OT如何实现的具体例子。

---

## 66. 诅咒电路：电荷泵降压器

**原文标题**: Cursed circuits: charge pump voltage halver

**原文链接**: [https://lcamtuf.substack.com/p/cursed-circuits-charge-pump-voltage](https://lcamtuf.substack.com/p/cursed-circuits-charge-pump-voltage)

无法访问文章链接。

---

## 67. 并非总是ICache

**原文标题**: It's Not Always ICache

**原文链接**: [https://matklad.github.io/2021/07/10/its-not-always-icache.html](https://matklad.github.io/2021/07/10/its-not-always-icache.html)

内联代码并非总是优化：一个反例

---

## 68. The Junior Hiring Crisis

**原文标题**: The Junior Hiring Crisis

**原文链接**: [https://people-work.io/blog/junior-hiring-crisis/](https://people-work.io/blog/junior-hiring-crisis/)

生成摘要时出错

---

## 69. Zig's new plan for asynchronous programs

**原文标题**: Zig's new plan for asynchronous programs

**原文链接**: [https://lwn.net/SubscriberLink/1046084/4c048ee008e1c70e/](https://lwn.net/SubscriberLink/1046084/4c048ee008e1c70e/)

生成摘要时出错

---

## 70. Apple Pushes iPhone Users Still on iOS 18 to Upgrade to iOS 26

**原文标题**: Apple Pushes iPhone Users Still on iOS 18 to Upgrade to iOS 26

**原文链接**: [https://www.macrumors.com/2025/12/02/apple-pushes-ios-18-users-to-ios-26/](https://www.macrumors.com/2025/12/02/apple-pushes-ios-18-users-to-ios-26/)

生成摘要时出错

---

## 71. An extra solar system planet once orbited next to Earth

**原文标题**: An extra solar system planet once orbited next to Earth

**原文链接**: [https://www.livescience.com/space/planets/an-extra-solar-system-planet-once-orbited-next-to-earth-and-it-may-be-the-reason-we-have-a-moon](https://www.livescience.com/space/planets/an-extra-solar-system-planet-once-orbited-next-to-earth-and-it-may-be-the-reason-we-have-a-moon)

生成摘要时出错

---

## 72. After Windows Update, Password icon invisible, click where it used to be

**原文标题**: After Windows Update, Password icon invisible, click where it used to be

**原文链接**: [https://support.microsoft.com/en-us/topic/august-29-2025-kb5064081-os-build-26100-5074-preview-3f9eb9e1-72ca-4b42-af97-39aace788d93](https://support.microsoft.com/en-us/topic/august-29-2025-kb5064081-os-build-26100-5074-preview-3f9eb9e1-72ca-4b42-af97-39aace788d93)

生成摘要时出错

---

## 73. Nixtml: Static website and blog generator written in Nix

**原文标题**: Nixtml: Static website and blog generator written in Nix

**原文链接**: [https://github.com/arnarg/nixtml](https://github.com/arnarg/nixtml)

生成摘要时出错

---

## 74. India withdraws mandatory pre-installation of Sanchar Saathi app on smartphones

**原文标题**: India withdraws mandatory pre-installation of Sanchar Saathi app on smartphones

**原文链接**: [https://www.pib.gov.in/PressReleasePage.aspx?PRID=2198110&reg=3&lang=2](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2198110&reg=3&lang=2)

生成摘要时出错

---

## 75. Claude 4.5 Opus’ Soul Document

**原文标题**: Claude 4.5 Opus’ Soul Document

**原文链接**: [https://www.lesswrong.com/posts/vpNG99GhbBoLov9og/claude-4-5-opus-soul-document](https://www.lesswrong.com/posts/vpNG99GhbBoLov9og/claude-4-5-opus-soul-document)

生成摘要时出错

---

## 76. Code Wiki: Accelerating your code understanding

**原文标题**: Code Wiki: Accelerating your code understanding

**原文链接**: [https://developers.googleblog.com/en/introducing-code-wiki-accelerating-your-code-understanding/](https://developers.googleblog.com/en/introducing-code-wiki-accelerating-your-code-understanding/)

生成摘要时出错

---

## 77. Cars are steadily becoming longer, wider and heavier in the UK and across Europe

**原文标题**: Cars are steadily becoming longer, wider and heavier in the UK and across Europe

**原文链接**: [https://www.bbc.com/news/articles/cy7vdvl2531o](https://www.bbc.com/news/articles/cy7vdvl2531o)

生成摘要时出错

---

## 78. Comparing AWS Lambda ARM64 vs. x86_64 Performance Across Runtimes in Late 2025

**原文标题**: Comparing AWS Lambda ARM64 vs. x86_64 Performance Across Runtimes in Late 2025

**原文链接**: [https://chrisebert.net/comparing-aws-lambda-arm64-vs-x86_64-performance-across-multiple-runtimes-in-late-2025/](https://chrisebert.net/comparing-aws-lambda-arm64-vs-x86_64-performance-across-multiple-runtimes-in-late-2025/)

生成摘要时出错

---

## 79. Exploring Large HTML Documents on the Web

**原文标题**: Exploring Large HTML Documents on the Web

**原文链接**: [https://calendar.perfplanet.com/2025/exploring-large-html-documents-on-the-web/](https://calendar.perfplanet.com/2025/exploring-large-html-documents-on-the-web/)

生成摘要时出错

---

## 80. Kohler Can Access Pictures from "End-to-End Encrypted" Toilet Camera

**原文标题**: Kohler Can Access Pictures from "End-to-End Encrypted" Toilet Camera

**原文链接**: [https://varlogsimon.leaflet.pub/3m6zrw6k2bs2p?interactionDrawer=quotes](https://varlogsimon.leaflet.pub/3m6zrw6k2bs2p?interactionDrawer=quotes)

生成摘要时出错

---

## 81. How Brian Eno Created Ambient 1: Music for Airports (2019)

**原文标题**: How Brian Eno Created Ambient 1: Music for Airports (2019)

**原文链接**: [https://reverbmachine.com/blog/deconstructing-brian-eno-music-for-airports/](https://reverbmachine.com/blog/deconstructing-brian-eno-music-for-airports/)

生成摘要时出错

---

## 82. Apple will not let me join the Developer Program – and will not say why

**原文标题**: Apple will not let me join the Developer Program – and will not say why

**原文链接**: [https://blog.kulman.sk/apple-developer-program/](https://blog.kulman.sk/apple-developer-program/)

生成摘要时出错

---

## 83. LNG Exports Will Drive Explosion in U.S. Natural Gas Consumption

**原文标题**: LNG Exports Will Drive Explosion in U.S. Natural Gas Consumption

**原文链接**: [https://oilprice.com/Energy/Natural-Gas/LNG-Exports-Will-Drive-Explosion-in-US-Natural-Gas-Consumption.html](https://oilprice.com/Energy/Natural-Gas/LNG-Exports-Will-Drive-Explosion-in-US-Natural-Gas-Consumption.html)

生成摘要时出错

---

## 84. The Rise and Fall of the H-1B Visa – American Affairs Journal

**原文标题**: The Rise and Fall of the H-1B Visa – American Affairs Journal

**原文链接**: [https://americanaffairsjournal.org/2025/11/the-rise-and-fall-of-the-h-1b-visa/](https://americanaffairsjournal.org/2025/11/the-rise-and-fall-of-the-h-1b-visa/)

生成摘要时出错

---

## 85. Instant Supercompute: Launching Wolfram Compute Services

**原文标题**: Instant Supercompute: Launching Wolfram Compute Services

**原文链接**: [https://writings.stephenwolfram.com/2025/12/instant-supercompute-launching-wolfram-compute-services/](https://writings.stephenwolfram.com/2025/12/instant-supercompute-launching-wolfram-compute-services/)

生成摘要时出错

---

## 86. Tom Stoppard has died

**原文标题**: Tom Stoppard has died

**原文链接**: [https://www.bbc.com/news/articles/c74xe49q7vlo](https://www.bbc.com/news/articles/c74xe49q7vlo)

生成摘要时出错

---

## 87. AI generated font using Nano Banana

**原文标题**: AI generated font using Nano Banana

**原文链接**: [https://constanttime.notion.site/Worlds-first-Ai-generated-font-using-nano-banana-2ba6f8e15af18012864bdb760fa9c9ba?pvs=74](https://constanttime.notion.site/Worlds-first-Ai-generated-font-using-nano-banana-2ba6f8e15af18012864bdb760fa9c9ba?pvs=74)

生成摘要时出错

---

## 88. India orders smartphone makers to preload state-owned cyber safety app

**原文标题**: India orders smartphone makers to preload state-owned cyber safety app

**原文链接**: [https://www.reuters.com/sustainability/boards-policy-regulation/india-orders-mobile-phones-preloaded-with-government-app-ensure-cyber-safety-2025-12-01/](https://www.reuters.com/sustainability/boards-policy-regulation/india-orders-mobile-phones-preloaded-with-government-app-ensure-cyber-safety-2025-12-01/)

生成摘要时出错

---

## 89. DeepSeek-v3.2: Pushing the frontier of open large language models [pdf]

**原文标题**: DeepSeek-v3.2: Pushing the frontier of open large language models [pdf]

**原文链接**: [https://huggingface.co/deepseek-ai/DeepSeek-V3.2/resolve/main/assets/paper.pdf](https://huggingface.co/deepseek-ai/DeepSeek-V3.2/resolve/main/assets/paper.pdf)

生成摘要时出错

---

## 90. Reverse math shows why hard problems are hard

**原文标题**: Reverse math shows why hard problems are hard

**原文链接**: [https://www.quantamagazine.org/reverse-mathematics-illuminates-why-hard-problems-are-hard-20251201/](https://www.quantamagazine.org/reverse-mathematics-illuminates-why-hard-problems-are-hard-20251201/)

生成摘要时出错

---

## 91. The Algorithm That Exposed the AI Industry's Circular Financing Scheme

**原文标题**: The Algorithm That Exposed the AI Industry's Circular Financing Scheme

**原文链接**: [https://substack.com/home/post/p-179453867](https://substack.com/home/post/p-179453867)

生成摘要时出错

---

## 92. Apple Releases Open Weights Video Model

**原文标题**: Apple Releases Open Weights Video Model

**原文链接**: [https://starflow-v.github.io](https://starflow-v.github.io)

生成摘要时出错

---

## 93. What will enter the public domain in 2026?

**原文标题**: What will enter the public domain in 2026?

**原文链接**: [https://publicdomainreview.org/features/entering-the-public-domain/2026/](https://publicdomainreview.org/features/entering-the-public-domain/2026/)

生成摘要时出错

---

## 94. Lowtype: Elegant Types in Ruby

**原文标题**: Lowtype: Elegant Types in Ruby

**原文链接**: [https://codeberg.org/Iow/type](https://codeberg.org/Iow/type)

生成摘要时出错

---

## 95. Mathematics is hard for mathematicians to understand too

**原文标题**: Mathematics is hard for mathematicians to understand too

**原文链接**: [https://www.science.org/doi/10.1126/science.aec9014](https://www.science.org/doi/10.1126/science.aec9014)

生成摘要时出错

---

## 96. Rootless Pings in Rust

**原文标题**: Rootless Pings in Rust

**原文链接**: [https://bou.ke/blog/rust-ping/](https://bou.ke/blog/rust-ping/)

生成摘要时出错

---

## 97. Advent of Code 2025

**原文标题**: Advent of Code 2025

**原文链接**: [https://adventofcode.com/2025/about](https://adventofcode.com/2025/about)

生成摘要时出错

---

## 98. Advent of Compiler Optimisations 2025

**原文标题**: Advent of Compiler Optimisations 2025

**原文链接**: [https://xania.org/202511/advent-of-compiler-optimisation](https://xania.org/202511/advent-of-compiler-optimisation)

生成摘要时出错

---

## 99. Decreasing Certificate Lifetimes to 45 Days

**原文标题**: Decreasing Certificate Lifetimes to 45 Days

**原文链接**: [https://letsencrypt.org/2025/12/02/from-90-to-45.html](https://letsencrypt.org/2025/12/02/from-90-to-45.html)

生成摘要时出错

---

## 100. Python Data Science Handbook

**原文标题**: Python Data Science Handbook

**原文链接**: [https://jakevdp.github.io/PythonDataScienceHandbook/](https://jakevdp.github.io/PythonDataScienceHandbook/)

生成摘要时出错

---

