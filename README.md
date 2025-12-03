# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-12-03.md)

*最后自动更新时间: 2025-12-03 17:54:57*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 2 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 3 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 4 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 5 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 6 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 7 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 8 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 9 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 10 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 11 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 12 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 13 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 14 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 15 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 16 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 17 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 18 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 19 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 20 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 21 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 22 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 23 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 24 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 25 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 26 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 27 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 28 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 29 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 30 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 31 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 32 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 33 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 34 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 35 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 36 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 37 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 38 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 39 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 40 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 41 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 42 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 43 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 44 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 45 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 46 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 47 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 48 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 49 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 50 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 51 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 52 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 53 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 54 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 55 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 56 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 57 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 58 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 59 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 60 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 61 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 62 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 63 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 64 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 65 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 66 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 67 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 68 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 69 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 70 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 71 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 72 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 73 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 74 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 75 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 76 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 77 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 78 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 79 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 80 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 81 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 82 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 83 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 84 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 85 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 86 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 87 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 88 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 89 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 90 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 91 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 92 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 93 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 94 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 95 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 96 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 97 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 98 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 99 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 100 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 101 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 102 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 103 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 104 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 105 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 106 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 107 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 108 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 109 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 110 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 111 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 112 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 113 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 114 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 115 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 116 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 117 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 118 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 119 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 120 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 121 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 122 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 123 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 124 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 125 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 126 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 127 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 128 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 129 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 130 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 131 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 132 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 133 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 134 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 135 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 136 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 137 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 138 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 139 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 140 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 141 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 142 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 143 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 144 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 145 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 146 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 147 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 148 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 149 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 150 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 151 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 152 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 153 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 154 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 155 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 156 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 157 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 158 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 159 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 160 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 161 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 162 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 163 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 164 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 165 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 166 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 167 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 168 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 169 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 170 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 171 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 172 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 173 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 174 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 175 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 176 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 177 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 178 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 179 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 180 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 181 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 182 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 183 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 184 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 185 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 186 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 187 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 188 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 189 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 190 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 191 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 192 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 193 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 194 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 195 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 196 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 197 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 198 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 199 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 200 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 201 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 202 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 203 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 204 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 205 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 206 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 207 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 208 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 209 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 210 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 211 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 212 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 213 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 214 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 215 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 216 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 217 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 218 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 219 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 220 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 221 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 222 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 223 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 224 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 225 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 226 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 227 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 228 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 229 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 230 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 231 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 232 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 233 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 234 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 235 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 236 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 237 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 238 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 239 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 240 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 241 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 242 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 243 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 244 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 245 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 246 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 247 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 248 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 249 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 250 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 251 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 252 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 253 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 254 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 255 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 256 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 257 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 258 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
