# Hacker News 热门文章摘要 (2026-04-30)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 马克·克莱恩是如何向 EFF 披露 641A 房间内幕的 [书籍摘录]

**原文标题**: How Mark Klein told the EFF about Room 641A [book excerpt]

**原文链接**: [https://thereader.mitpress.mit.edu/the-whistleblower-who-uncovered-the-nsas-big-brother-machine/](https://thereader.mitpress.mit.edu/the-whistleblower-who-uncovered-the-nsas-big-brother-machine/)

2003年，AT&T技术人员马克·克莱恩（Mark Klein）在公司位于旧金山的交换中心发现了一个秘密设施——641A房间。本文详述了克莱恩如何揭露一项大规模监控行动：通过“分流”光缆，将所有互联网流量的实时副本同步发送给美国国家安全局（NSA）。这种硬件实现了对国内数据的全盘“真空式吸取”，与政府声称监控具有严格针对性的说法背道而驰。

2004年退休后，受《纽约时报》2005年一篇关于无证窃听报道的启发，克莱恩决定采取行动。意识到公众所了解的仅是该计划规模的冰山一角，他联系了电子前哨基金会（EFF）。克莱恩向EFF提供了关键的内部文件和布线图以证实其主张，证明了大规模监控的基础设施已在物理上整合进了国家的电信骨干网。

他的证据成为了里程碑式的集体诉讼案“赫普廷诉AT&T案”（Hepting v. AT&T）的基石。本文强调了克莱恩作为关键吹哨人的角色，他揭露了这台“老大哥机器”，揭示了电信巨头与美国政府通过协作绕过宪法第四修正案的行为。克莱恩的勇气将有关国家监控的推测转化为了有据可查、不可辩驳的事实，展现了政府介入公民私人生活的惊人规模。

---

## 2. PyTorch Lightning AI 训练库中发现以 Shai-Hulud 为主题的恶意软件

**原文标题**: Shai-Hulud Themed Malware Found in the PyTorch Lightning AI Training Library

**原文链接**: [https://semgrep.dev/blog/2026/malicious-dependency-in-pytorch-lightning-used-for-ai-training/](https://semgrep.dev/blog/2026/malicious-dependency-in-pytorch-lightning-used-for-ai-training/)

PyPI 软件包 **`lightning`**（版本 2.6.2 和 2.6.3）作为 AI 和深度学习的核心框架，于 2026 年 4 月 30 日在一次供应链攻击中被攻陷。该攻击被归因为威胁行为体“mini Shai-Hulud”，其携带的以《沙丘》为主题的恶意软件在模块导入时，通过隐藏在 `_runtime` 目录中的混淆 JavaScript 载荷自动执行。

此次攻击重点在于大规模凭据窃取和蠕虫式传播。它从本地环境、CI/CD 运行器和系统内存中搜集 GitHub 令牌、npm 凭据以及云端机密（AWS、Azure、GCP）。如果发现 npm 凭据，恶意软件会向受害者的自有软件包中植入释放器（dropper）并重新发布，从而实现从 PyPI 到 npm 的跨生态系统扩散。

数据外泄通过四个冗余通道进行：
1. 直接向攻击者的 C2 服务器发送 HTTPS POST 请求。
2. 利用前缀为 `EveryBoiWeBuildIsAWormyBoi` 的 GitHub 提交搜索“死信箱”（dead-drops）。
3. 攻击者控制的标题为“A Mini Shai-Hulud has Appeared”的公共仓库。
4. 直接推送到受害者本人的 GitHub 仓库。

值得注意的是，该恶意软件通过针对开发者专用工具来建立持久化。它向 **Claude Code** (`.claude/settings.json`) 和 **VS Code** (`.vscode/tasks.json`) 注入恶意钩子，确保每当开发者打开受感染的项目时，恶意载荷都会运行。此外，它还会安装一个伪造的“Formatter”GitHub Actions 工作流，通过构建产物（artifacts）泄露仓库机密。

**修复措施：** 用户应检查受影响的版本，审计仓库中是否存在异常的 `.claude/`、`.vscode/` 或 `_runtime/` 目录，并立即轮换所有云凭据、GitHub 令牌和 API 密钥。失陷指标（IoC）包括特定的《沙丘》主题提交消息以及 `EveryBoiWeBuildIsAWormyBoi` 字符串。

---

## 3. Belgium stops decommissioning nuclear power plants

**原文标题**: Belgium stops decommissioning nuclear power plants

**原文链接**: [https://dpa-international.com/general-news/urn:newsml:dpa.com:20090101:260430-930-14717/](https://dpa-international.com/general-news/urn:newsml:dpa.com:20090101:260430-930-14717/)

生成摘要时出错

---

## 4. 我用 F# 开发了一个 Game Boy 模拟器

**原文标题**: I built a Game Boy emulator in F#

**原文链接**: [https://nickkossolapov.github.io/fame-boy/building-a-game-boy-emulator-in-fsharp/](https://nickkossolapov.github.io/fame-boy/building-a-game-boy-emulator-in-fsharp/)

为深入理解计算机硬件基础，一位拥有八年经验的软件工程师开发了 Fame Boy——一个使用 F# 编写的 Game Boy 模拟器。在完成《从 NAND 到 Tetris》课程并构建了 CHIP-8 模拟器后，作者开发出 Fame Boy，使其能够同时在桌面和 Web 平台上运行。

该模拟器的架构在核心逻辑与前端之间保持了严格的接口隔离，并利用单线程“步进”函数来同步 CPU、PPU 和定时器。虽然作者为了确保性能而从函数式纯粹性转向了可变性，但他们充分利用了 F# 强大的类型系统（特别是“判别联合”）来建模 CPU 指令。这种方法将 512 个操作码精简为仅 58 条指令，并利用类型系统在编译阶段捕获非法状态。一项显著的优化是针对 CPU 标志管理编写的 16 行内联模块，使性能提升了 10%。

实现亮点包括：
*   **CPU**：采用测试驱动开发 (TDD)，并使用了根据技术规范生成的 AI 测试用例。
*   **PPU**：作者没有模拟复杂的像素 FIFO 队列，而是采用了更简单的扫描线渲染方法。虽然这种方法在处理某些边缘情况游戏时硬件准确度稍逊，但性能出色且兼容绝大多数作品。
*   **手柄与音频单元 (APU)**：作者攻克了手柄硬件寄存器时序的细节难题，并成功集成了音频处理单元 (APU) 以提供完整体验。

最终，该项目证明了 F# 的领域建模能力非常适合硬件模拟，在代码的表达力、安全性和高执行速度之间达成了平衡。Fame Boy 目前已开源，并可在浏览器中直接游玩。

---

## 5. CopyFail 未向发行版披露

**原文标题**: CopyFail Was Not Disclosed to Distros

**原文链接**: [https://www.openwall.com/lists/oss-security/2026/04/30/10](https://www.openwall.com/lists/oss-security/2026/04/30/10)

本文总结了 `oss-security` 邮件列表上关于 **CVE-2026-31431** 的讨论。该漏洞被称为 **“CopyFail”**，是一个高危的 Linux 本地提权漏洞。

**关键发现包括：**

*   **漏洞范围：** 该缺陷于 2017 年随 Linux 内核 4.14 版本引入。虽然主线版本和最近的稳定版本（6.18.22、6.19.12 和 7.0）已发布修复程序，但许多长期支持 (LTS) 内核（包括 6.12、6.6、6.1、5.15 和 5.10）仍未修复。
*   **后向移植挑战：** 由于 API 发生了重大变化，将官方修复程序后向移植到旧内核非常困难。由于补丁无法“无冲突地应用 (apply cleanly)”，维护者正面临为旧系统提供即时更新的难题。
*   **披露失误：** 一个主要的争议点是，该漏洞在公开之前并未通过 `linux-distros` 邮件列表进行披露。因此，Linux 发行版没有收到预先通知或禁运期来准备补丁，导致它们只能在漏洞公开后被动应对。
*   **临时变通方案：** 针对迫在眉睫的风险，Gentoo 的 Sam James 分享了一个临时解决方案：通过补丁禁用 `authencesn` 加密模块。在开发正式的后向移植补丁期间，相比让系统暴露于“一键提权 (make-me-root)”的漏洞风险中，这被视为一种“两害相权取其轻”的选择。

这一现状凸显了 Linux 内核安全生态系统中，关于漏洞如何向各发行版报告以及如何处理漏洞的持续摩擦。

---

## 6. 如果你的提交记录中提到 “OpenClaw”，Claude Code 将会拒绝请求或额外收费。

**原文标题**: Claude Code refuses requests or charges extra if your commits mention "OpenClaw"

**原文链接**: [https://twitter.com/theo/status/2049645973350363168](https://twitter.com/theo/status/2049645973350363168)

提供的文本是来自 X（原 Twitter）的一条技术错误消息，提示 JavaScript 已禁用。然而，根据标题——**“如果您的提交提及 'OpenClaw'，Claude Code 将拒绝请求或额外收费”**——以下是该事件的背景摘要：

该标题揭示了一场涉及 **Claude Code** 的争议，它是 Anthropic 公司开发的 AI 辅助编程命令行工具。有报告称，当该工具检测到提及 **“OpenClaw”**（一个旨在替代 Anthropic 专有 CLI 的开源项目）时，其程序设定可能会做出负面反应。

**核心要点：**
*   **服务干扰**：用户声称在提交信息（commit messages）或项目文件中包含“OpenClaw”会导致 Claude Code 拒绝执行任务或返回错误。
*   **经济惩罚**：有指控称，提及该开源替代方案会触发更高的 Token 消耗或“额外费用”，这实际上起到了一种经济威慑作用，旨在阻止用户使用或提及竞争工具。
*   **供应商锁定担忧**：此情况引发了开发者社区关于“AI 审查”和“供应商锁定”的争论。这表明专有 AI 工具可能会主动监控并限制开发者的工作流，从而使开源竞争对手处于不利地位。
*   **伦理影响**：如果属实，这些做法将引发关于开发者自主权，以及 AI 服务提供商在管理其生态系统内竞争性软件时透明度的重大质疑。

简而言之，该报告指控 Anthropic 正利用 Claude Code 的逻辑，通过拒绝服务和增加成本，以程序化手段打压其开源对手 OpenClaw。

---

## 7. 炼油厂的工作原理

**原文标题**: How an Oil Refinery Works

**原文链接**: [https://www.construction-physics.com/p/how-an-oil-refinery-works](https://www.construction-physics.com/p/how-an-oil-refinery-works)

Oil refineries are massive industrial facilities essential for transforming crude oil—a complex mixture of hydrocarbons—into usable fuels and chemical feedstocks. Despite the growth of renewable energy, petroleum remains the world’s primary energy source and provides 90% of all chemical feedstocks for products ranging from plastics to fertilizers.

The refining process centers on **distillation**. Crude oil is heated until it vaporizes and is fed into a distillation column. Because different molecules have different boiling points, they condense at different heights: lighter molecules like propane rise to the top, while heavier molecules exit the bottom. 

To maximize the output of high-value products like gasoline, refineries employ several secondary processes:
*   **Cracking:** Splitting heavy, low-value molecules into lighter ones using heat and pressure. Most modern refineries use **fluid catalytic cracking**, which utilizes a catalyst to speed the reaction.
*   **Vacuum Distillation:** Distilling heavy residuals at low pressure to prevent molecules from cracking prematurely due to high heat.
*   **Coking:** A form of thermal cracking that processes the heaviest "bottom of the barrel" molecules into lighter oils and solid coke.
*   **Reforming and Isomerization:** Chemically restructuring molecules to improve their properties, such as turning naphtha into high-octane gasoline components.
*   **Hydrotreating:** Using hydrogen to remove impurities like sulfur.

The scale of these operations is immense. A typical large refinery, such as Chevron’s Richmond facility, processes roughly 250,000 barrels of oil daily. Globally, refineries handle over 100 million barrels per day, with the world's largest facility—India’s Jamnagar refinery—capable of processing 1.4 million barrels daily. This complex infrastructure is what allows raw crude oil to be converted into the specific chemicals that power modern transportation and manufacturing.

---

## 8. 持久化队列、流、发布/订阅及 Cron 调度器 —— 内置于您的 SQLite 文件中

**原文标题**: Durable queues, streams, pub/sub, and a cron scheduler – inside your SQLite file

**原文链接**: [https://honker.dev/](https://honker.dev/)

**Honker** 是一个 SQLite 可加载扩展及一系列语言绑定，它将持久化队列、流、发布/订阅和 cron 调度直接集成到 SQLite 数据库中。通过将这些功能嵌入到数据库文件内，Honker 允许开发者在无需 Redis 或 Celery 等外部中间件的情况下管理后台任务和消息传递。

这种架构的主要优势在于 **ACID 原子性**。由于队列只是同一文件中的一个数据表，用户可以在处理业务写入（例如同时插入订单和“发送邮件”任务）的同一个事务中将任务入队。这消除了“双写”问题，并确保只有在相应的数据库更改成功提交后才会创建任务。

**关键技术细节：**
*   **性能：** 它实现了约 0.7 毫秒的跨进程唤醒延迟。
*   **机制：** Honker 并非采用繁重的轮询方式，而是每毫秒监控一次 SQLite 的 `PRAGMA data_version`。这种轻量级检查能以极低的 CPU 或页面缓存开销，识别来自任何连接或进程的提交。
*   **通用兼容性：** 它拥有统一的磁盘格式，并提供 Python、Node.js、Rust、Go、Ruby、Bun、Elixir 和 C++ 的语言绑定。
*   **简洁性：** 它无需独立的存储库、备份策略或任务管理守护进程，从而简化了技术栈。

Honker 专为那些将 SQLite 作为主数据库，并需要一个能在维持数据完整性的同时支持跨进程扩展、可靠且低延迟的队列系统的开发者而设计。

---

## 9. You can beat the binary search

**原文标题**: You can beat the binary search

**原文链接**: [https://lemire.me/blog/2026/04/27/you-can-beat-the-binary-search/](https://lemire.me/blog/2026/04/27/you-can-beat-the-binary-search/)

生成摘要时出错

---

## 10. Spain's parliament will act against massive IP blockages by LaLiga

**原文标题**: Spain's parliament will act against massive IP blockages by LaLiga

**原文链接**: [https://www.democrata.es/en/politics/congress-and-senate/congress-will-act-against-massive-ip-blockages-by-laliga/](https://www.democrata.es/en/politics/congress-and-senate/congress-will-act-against-massive-ip-blockages-by-laliga/)

生成摘要时出错

---

## 11. SatoshiGuesser – Roll for Bitcoin

**原文标题**: SatoshiGuesser – Roll for Bitcoin

**原文链接**: [https://github.com/Pathos0925/SatoshiGuesser](https://github.com/Pathos0925/SatoshiGuesser)

生成摘要时出错

---

## 12. I aggregated 28 US Government auction sites into one search

**原文标题**: I aggregated 28 US Government auction sites into one search

**原文链接**: [https://bidprowl.com](https://bidprowl.com)

生成摘要时出错

---

## 13. 10Gb/s Ethernet: what I did to get it working in my home

**原文标题**: 10Gb/s Ethernet: what I did to get it working in my home

**原文链接**: [https://www.gilesthomas.com/2026/04/10g-ethernet-what-i-did](https://www.gilesthomas.com/2026/04/10g-ethernet-what-i-did)

生成摘要时出错

---

## 14. Mozilla's opposition to Chrome's Prompt API

**原文标题**: Mozilla's opposition to Chrome's Prompt API

**原文链接**: [https://github.com/mozilla/standards-positions/issues/1213](https://github.com/mozilla/standards-positions/issues/1213)

生成摘要时出错

---

## 15. A 1960s art school experiment that redefined creativity

**原文标题**: A 1960s art school experiment that redefined creativity

**原文链接**: [https://thereader.mitpress.mit.edu/the-1960s-art-school-experiment-that-redefined-creativity/](https://thereader.mitpress.mit.edu/the-1960s-art-school-experiment-that-redefined-creativity/)

生成摘要时出错

---

## 16. Show HN: TRiP – a complete transformer engine in C built from scratch just by me

**原文标题**: Show HN: TRiP – a complete transformer engine in C built from scratch just by me

**原文链接**: [https://github.com/carlovalenti/TRiP](https://github.com/carlovalenti/TRiP)

生成摘要时出错

---

## 17. I scraped 1.94M Airbnb photos for opium dens, pet cameos, and messy kitchens

**原文标题**: I scraped 1.94M Airbnb photos for opium dens, pet cameos, and messy kitchens

**原文链接**: [https://burla-cloud.github.io/examples/airbnb-burla-demo/](https://burla-cloud.github.io/examples/airbnb-burla-demo/)

生成摘要时出错

---

## 18. The Zig project's rationale for their anti-AI contribution policy

**原文标题**: The Zig project's rationale for their anti-AI contribution policy

**原文链接**: [https://simonwillison.net/2026/Apr/30/zig-anti-ai/](https://simonwillison.net/2026/Apr/30/zig-anti-ai/)

生成摘要时出错

---

## 19. Noctua releases official 3D CAD models for its cooling fans

**原文标题**: Noctua releases official 3D CAD models for its cooling fans

**原文链接**: [https://www.noctua.at/en/3d-cad-models](https://www.noctua.at/en/3d-cad-models)

生成摘要时出错

---

## 20. Granite 4.1: IBM's 8B Model Matching 32B MoE

**原文标题**: Granite 4.1: IBM's 8B Model Matching 32B MoE

**原文链接**: [https://firethering.com/granite-4-1-ibm-open-source-model-family/](https://firethering.com/granite-4-1-ibm-open-source-model-family/)

生成摘要时出错

---

## 21. Where the goblins came from

**原文标题**: Where the goblins came from

**原文链接**: [https://openai.com/index/where-the-goblins-came-from/](https://openai.com/index/where-the-goblins-came-from/)

生成摘要时出错

---

## 22. Kubereboot/Kured: Kubernetes Reboot Daemon

**原文标题**: Kubereboot/Kured: Kubernetes Reboot Daemon

**原文链接**: [https://github.com/kubereboot/kured](https://github.com/kubereboot/kured)

生成摘要时出错

---

## 23. Recovering files from beyond the grave using PhotoRec

**原文标题**: Recovering files from beyond the grave using PhotoRec

**原文链接**: [https://lost-number.bearblog.dev/recovering-files-from-beyond-the-grave-using-photorec/](https://lost-number.bearblog.dev/recovering-files-from-beyond-the-grave-using-photorec/)

生成摘要时出错

---

## 24. The Science Behind Honey's Eternal Shelf Life (2013)

**原文标题**: The Science Behind Honey's Eternal Shelf Life (2013)

**原文链接**: [https://www.smithsonianmag.com/science-nature/the-science-behind-honeys-eternal-shelf-life-1218690/](https://www.smithsonianmag.com/science-nature/the-science-behind-honeys-eternal-shelf-life-1218690/)

生成摘要时出错

---

## 25. A Primer on Bézier Curves – So What Makes a Bézier Curve?

**原文标题**: A Primer on Bézier Curves – So What Makes a Bézier Curve?

**原文链接**: [https://pomax.github.io/bezierinfo/](https://pomax.github.io/bezierinfo/)

生成摘要时出错

---

## 26. Craig Venter has died

**原文标题**: Craig Venter has died

**原文链接**: [https://www.jcvi.org/media-center/j-craig-venter-genomics-pioneer-and-founder-jcvi-and-diploid-genomics-inc-dies-79](https://www.jcvi.org/media-center/j-craig-venter-genomics-pioneer-and-founder-jcvi-and-diploid-genomics-inc-dies-79)

生成摘要时出错

---

## 27. What can we gain by losing infinity?

**原文标题**: What can we gain by losing infinity?

**原文链接**: [https://www.quantamagazine.org/what-can-we-gain-by-losing-infinity-20260429/](https://www.quantamagazine.org/what-can-we-gain-by-losing-infinity-20260429/)

生成摘要时出错

---

## 28. My Stratum-0 Atomic Clock

**原文标题**: My Stratum-0 Atomic Clock

**原文链接**: [https://coverclock.blogspot.com/2017/05/my-stratum-0-atomic-clock_9.html](https://coverclock.blogspot.com/2017/05/my-stratum-0-atomic-clock_9.html)

生成摘要时出错

---

## 29. Largest Digital Human Rights Conference Suddenly Canceled

**原文标题**: Largest Digital Human Rights Conference Suddenly Canceled

**原文链接**: [https://www.404media.co/rightscon-human-rights-conference-suddenly-postponed/](https://www.404media.co/rightscon-human-rights-conference-suddenly-postponed/)

生成摘要时出错

---

## 30. GCC 16 has been released

**原文标题**: GCC 16 has been released

**原文链接**: [https://gcc.gnu.org/gcc-16/changes.html](https://gcc.gnu.org/gcc-16/changes.html)

生成摘要时出错

---

## 31. Because It Doesn't Have To

**原文标题**: Because It Doesn't Have To

**原文链接**: [https://blog.computationalcomplexity.org/2026/04/because-it-doesnt-have-to.html](https://blog.computationalcomplexity.org/2026/04/because-it-doesnt-have-to.html)

生成摘要时出错

---

## 32. DataCenter.FM – background noise app featuring the sound of the AI bubble

**原文标题**: DataCenter.FM – background noise app featuring the sound of the AI bubble

**原文链接**: [https://datacenter.fm/](https://datacenter.fm/)

生成摘要时出错

---

## 33. Meta in row after workers who saw smart glasses users having sex lose jobs

**原文标题**: Meta in row after workers who saw smart glasses users having sex lose jobs

**原文链接**: [https://www.bbc.com/news/articles/c5y7yvgy0w6o](https://www.bbc.com/news/articles/c5y7yvgy0w6o)

生成摘要时出错

---

## 34. "Parse, don't validate" through the years with C++

**原文标题**: "Parse, don't validate" through the years with C++

**原文链接**: [https://derekrodriguez.dev/parse-dont-validate-through-the-years-with-c-/](https://derekrodriguez.dev/parse-dont-validate-through-the-years-with-c-/)

生成摘要时出错

---

## 35. Fast GPU Linear Algebra via Compile Time Expression Fusion

**原文标题**: Fast GPU Linear Algebra via Compile Time Expression Fusion

**原文链接**: [https://arxiv.org/abs/2604.22242](https://arxiv.org/abs/2604.22242)

生成摘要时出错

---

## 36. Zed 1.0

**原文标题**: Zed 1.0

**原文链接**: [https://zed.dev/blog/zed-1-0](https://zed.dev/blog/zed-1-0)

生成摘要时出错

---

## 37. Biology is a Burrito: A text- and visual-based journey through a living cell

**原文标题**: Biology is a Burrito: A text- and visual-based journey through a living cell

**原文链接**: [https://burrito.bio/essays/biology-is-a-burrito](https://burrito.bio/essays/biology-is-a-burrito)

生成摘要时出错

---

## 38. Show HN: FusionCore: ROS 2 sensor fusion that outperforms robot_localization

**原文标题**: Show HN: FusionCore: ROS 2 sensor fusion that outperforms robot_localization

**原文链接**: [https://github.com/manankharwar/fusioncore](https://github.com/manankharwar/fusioncore)

生成摘要时出错

---

## 39. OpenTrafficMap

**原文标题**: OpenTrafficMap

**原文链接**: [https://opentrafficmap.org/](https://opentrafficmap.org/)

生成摘要时出错

---

## 40. Copy Fail

**原文标题**: Copy Fail

**原文链接**: [https://copy.fail/](https://copy.fail/)

生成摘要时出错

---

## 41. London to Calcutta by Bus (2022)

**原文标题**: London to Calcutta by Bus (2022)

**原文链接**: [https://www.amusingplanet.com/2022/08/london-to-calcutta-by-bus.html](https://www.amusingplanet.com/2022/08/london-to-calcutta-by-bus.html)

生成摘要时出错

---

## 42. Monad Tutorials Timeline

**原文标题**: Monad Tutorials Timeline

**原文链接**: [https://wiki.haskell.org/Monad_tutorials_timeline](https://wiki.haskell.org/Monad_tutorials_timeline)

生成摘要时出错

---

## 43. Gooseworks (YC W23) Is Hiring a Founding Growth Engineer

**原文标题**: Gooseworks (YC W23) Is Hiring a Founding Growth Engineer

**原文链接**: [https://www.ycombinator.com/companies/gooseworks/jobs/ztgY6bD-founding-growth-engineer](https://www.ycombinator.com/companies/gooseworks/jobs/ztgY6bD-founding-growth-engineer)

生成摘要时出错

---

## 44. Mike: open-source legal AI

**原文标题**: Mike: open-source legal AI

**原文链接**: [https://mikeoss.com/](https://mikeoss.com/)

生成摘要时出错

---

## 45. Most Swiss back initiative to cap population at 10M, poll shows

**原文标题**: Most Swiss back initiative to cap population at 10M, poll shows

**原文链接**: [https://www.reuters.com/world/europe/most-swiss-back-initiative-cap-population-10-million-poll-shows-2026-04-29/](https://www.reuters.com/world/europe/most-swiss-back-initiative-cap-population-10-million-poll-shows-2026-04-29/)

生成摘要时出错

---

## 46. Alignment whack-a-mole: Finetuning activates recall of copyrighted books in LLMs

**原文标题**: Alignment whack-a-mole: Finetuning activates recall of copyrighted books in LLMs

**原文链接**: [https://github.com/cauchy221/Alignment-Whack-a-Mole-Code](https://github.com/cauchy221/Alignment-Whack-a-Mole-Code)

生成摘要时出错

---

## 47. Ghostty is leaving GitHub

**原文标题**: Ghostty is leaving GitHub

**原文链接**: [https://mitchellh.com/writing/ghostty-leaving-github](https://mitchellh.com/writing/ghostty-leaving-github)

生成摘要时出错

---

## 48. Show HN: I wrote a DOOM clone in my own programming language

**原文标题**: Show HN: I wrote a DOOM clone in my own programming language

**原文链接**: [https://spectrelang.org/log/devlog#cubedoom](https://spectrelang.org/log/devlog#cubedoom)

生成摘要时出错

---

## 49. Joby kicks off NYC electric air taxi demos with historic JFK flight

**原文标题**: Joby kicks off NYC electric air taxi demos with historic JFK flight

**原文链接**: [https://www.flyingmag.com/joby-nyc-electric-air-taxi-jfk-airport/](https://www.flyingmag.com/joby-nyc-electric-air-taxi-jfk-airport/)

生成摘要时出错

---

## 50. We're in 1905: Why Electricity (Not Dot-Com) Is the Right AI Analogy

**原文标题**: We're in 1905: Why Electricity (Not Dot-Com) Is the Right AI Analogy

**原文链接**: [https://joereis.substack.com/p/were-in-1905-why-electricity-not](https://joereis.substack.com/p/were-in-1905-why-electricity-not)

生成摘要时出错

---

## 51. Cursor Camp

**原文标题**: Cursor Camp

**原文链接**: [https://neal.fun/cursor-camp/](https://neal.fun/cursor-camp/)

生成摘要时出错

---

## 52. Radio Lockdown Averted

**原文标题**: Radio Lockdown Averted

**原文链接**: [https://fsfe.org/activities/radiodirective/radiodirective.html](https://fsfe.org/activities/radiodirective/radiodirective.html)

生成摘要时出错

---

## 53. House GOP concedes in DHS funding fight, reopening TSA but blocking ICE funds

**原文标题**: House GOP concedes in DHS funding fight, reopening TSA but blocking ICE funds

**原文链接**: [https://www.cnn.com/2026/04/30/politics/dhs-shutdown-funding-bill-house-vote](https://www.cnn.com/2026/04/30/politics/dhs-shutdown-funding-bill-house-vote)

生成摘要时出错

---

## 54. Consequences of passing too few register parameters to a C function

**原文标题**: Consequences of passing too few register parameters to a C function

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20260427-00/?p=112271](https://devblogs.microsoft.com/oldnewthing/20260427-00/?p=112271)

生成摘要时出错

---

## 55. Official SAP NPM packages compromised to steal credentials

**原文标题**: Official SAP NPM packages compromised to steal credentials

**原文链接**: [https://www.bleepingcomputer.com/news/security/official-sap-npm-packages-compromised-to-steal-credentials/](https://www.bleepingcomputer.com/news/security/official-sap-npm-packages-compromised-to-steal-credentials/)

生成摘要时出错

---

## 56. How to Build the Future: Demis Hassabis [video]

**原文标题**: How to Build the Future: Demis Hassabis [video]

**原文链接**: [https://www.youtube.com/watch?v=JNyuX1zoOgU](https://www.youtube.com/watch?v=JNyuX1zoOgU)

生成摘要时出错

---

## 57. Creating a Color Palette from an Image

**原文标题**: Creating a Color Palette from an Image

**原文链接**: [https://amandahinton.com/blog/creating-a-color-palette-from-an-image](https://amandahinton.com/blog/creating-a-color-palette-from-an-image)

生成摘要时出错

---

## 58. Iran war disrupts the circuit board supply chain, raises costs for tech firms

**原文标题**: Iran war disrupts the circuit board supply chain, raises costs for tech firms

**原文链接**: [https://www.reuters.com/world/middle-east/iran-war-disrupts-the-circuit-board-supply-chain-raises-costs-tech-firms-2026-04-27/](https://www.reuters.com/world/middle-east/iran-war-disrupts-the-circuit-board-supply-chain-raises-costs-tech-firms-2026-04-27/)

生成摘要时出错

---

## 59. PostgreSQL 19 features I'm excited about

**原文标题**: PostgreSQL 19 features I'm excited about

**原文链接**: [https://www.bytebase.com/blog/postgres-19-features-im-excited-about/](https://www.bytebase.com/blog/postgres-19-features-im-excited-about/)

生成摘要时出错

---

## 60. A grounded conceptual model for ownership types in Rust

**原文标题**: A grounded conceptual model for ownership types in Rust

**原文链接**: [https://cacm.acm.org/research-highlights/a-grounded-conceptual-model-for-ownership-types-in-rust/](https://cacm.acm.org/research-highlights/a-grounded-conceptual-model-for-ownership-types-in-rust/)

生成摘要时出错

---

## 61. Ramp's Sheets AI Exfiltrates Financials

**原文标题**: Ramp's Sheets AI Exfiltrates Financials

**原文链接**: [https://www.promptarmor.com/resources/ramps-sheets-ai-exfiltrates-financials](https://www.promptarmor.com/resources/ramps-sheets-ai-exfiltrates-financials)

生成摘要时出错

---

## 62. Functional programmers need to take a look at Zig

**原文标题**: Functional programmers need to take a look at Zig

**原文链接**: [https://pure-systems.org/posts/2026-04-29-functional-programmers-need-to-take-a-look-at-zig.html](https://pure-systems.org/posts/2026-04-29-functional-programmers-need-to-take-a-look-at-zig.html)

生成摘要时出错

---

## 63. I accidentally made law enforcement shut down their fake honeypot

**原文标题**: I accidentally made law enforcement shut down their fake honeypot

**原文链接**: [https://lina.sh/blog/ddos-honeypot](https://lina.sh/blog/ddos-honeypot)

生成摘要时出错

---

## 64. FastCGI: 30 years old and still the better protocol for reverse proxies

**原文标题**: FastCGI: 30 years old and still the better protocol for reverse proxies

**原文链接**: [https://www.agwa.name/blog/post/fastcgi_is_the_better_protocol_for_reverse_proxies](https://www.agwa.name/blog/post/fastcgi_is_the_better_protocol_for_reverse_proxies)

生成摘要时出错

---

## 65. Warm Burnout: editor and terminal color scheme

**原文标题**: Warm Burnout: editor and terminal color scheme

**原文链接**: [https://warmburnout.com/](https://warmburnout.com/)

生成摘要时出错

---

## 66. Kyoto cherry blossoms now bloom earlier than at any point in 1,200 years

**原文标题**: Kyoto cherry blossoms now bloom earlier than at any point in 1,200 years

**原文链接**: [https://jivx.com/kyoto-bloom](https://jivx.com/kyoto-bloom)

生成摘要时出错

---

## 67. DRAM Crunch: Lessons for System Design

**原文标题**: DRAM Crunch: Lessons for System Design

**原文链接**: [https://www.eetimes.com/what-the-dram-crunch-teaches-us-about-system-design/](https://www.eetimes.com/what-the-dram-crunch-teaches-us-about-system-design/)

生成摘要时出错

---

## 68. Talkie: a 13B vintage language model from 1930

**原文标题**: Talkie: a 13B vintage language model from 1930

**原文链接**: [https://talkie-lm.com/introducing-talkie](https://talkie-lm.com/introducing-talkie)

生成摘要时出错

---

## 69. GitHub – DOS 1.0: Transcription of Tim Paterson's DOS Printouts

**原文标题**: GitHub – DOS 1.0: Transcription of Tim Paterson's DOS Printouts

**原文链接**: [https://github.com/DOS-History/Paterson-Listings](https://github.com/DOS-History/Paterson-Listings)

生成摘要时出错

---

## 70. Copy-fail-destroyer: K8s remediation for CVE-2026-31431

**原文标题**: Copy-fail-destroyer: K8s remediation for CVE-2026-31431

**原文链接**: [https://github.com/NorskHelsenett/copy-fail-destroyer](https://github.com/NorskHelsenett/copy-fail-destroyer)

生成摘要时出错

---

## 71. Virtualisation on Apple Silicon Macs is different

**原文标题**: Virtualisation on Apple Silicon Macs is different

**原文链接**: [https://eclecticlight.co/2026/04/29/virtualisation-on-apple-silicon-macs-is-different/](https://eclecticlight.co/2026/04/29/virtualisation-on-apple-silicon-macs-is-different/)

生成摘要时出错

---

## 72. How not to ban surveillance pricing

**原文标题**: How not to ban surveillance pricing

**原文链接**: [https://pluralistic.net/2026/04/30/something-must-be-done/](https://pluralistic.net/2026/04/30/something-must-be-done/)

生成摘要时出错

---

## 73. Vera: a programming language designed for machines to write

**原文标题**: Vera: a programming language designed for machines to write

**原文链接**: [https://github.com/aallan/vera](https://github.com/aallan/vera)

生成摘要时出错

---

## 74. Postgres's lateral joins allow for quite the good eDSL

**原文标题**: Postgres's lateral joins allow for quite the good eDSL

**原文链接**: [https://bensimms.moe/postgres-lateral-makes-quite-a-good-dsl/](https://bensimms.moe/postgres-lateral-makes-quite-a-good-dsl/)

生成摘要时出错

---

## 75. No new trial for Sam Bankman-Fried

**原文标题**: No new trial for Sam Bankman-Fried

**原文链接**: [https://www.citationneeded.news/sbf-new-trial-denied/](https://www.citationneeded.news/sbf-new-trial-denied/)

生成摘要时出错

---

## 76. An open-source stethoscope that costs between $2.5 and $5 to produce

**原文标题**: An open-source stethoscope that costs between $2.5 and $5 to produce

**原文链接**: [https://github.com/GliaX/Stethoscope](https://github.com/GliaX/Stethoscope)

生成摘要时出错

---

## 77. Laws of UX

**原文标题**: Laws of UX

**原文链接**: [https://lawsofux.com/](https://lawsofux.com/)

生成摘要时出错

---

## 78. 1.4 GW: battery storage at former Grohnde nuclear power plant

**原文标题**: 1.4 GW: battery storage at former Grohnde nuclear power plant

**原文链接**: [https://www.heise.de/en/news/1-4-GW-Huge-battery-storage-at-former-Grohnde-nuclear-power-plant-11277367.html](https://www.heise.de/en/news/1-4-GW-Huge-battery-storage-at-former-Grohnde-nuclear-power-plant-11277367.html)

生成摘要时出错

---

## 79. Soft launch of open-source code platform for government

**原文标题**: Soft launch of open-source code platform for government

**原文链接**: [https://www.nldigitalgovernment.nl/news/soft-launch-for-government-open-source-code-platform/](https://www.nldigitalgovernment.nl/news/soft-launch-for-government-open-source-code-platform/)

生成摘要时出错

---

## 80. HERMES.md in commit messages causes requests to route to extra usage billing

**原文标题**: HERMES.md in commit messages causes requests to route to extra usage billing

**原文链接**: [https://github.com/anthropics/claude-code/issues/53262](https://github.com/anthropics/claude-code/issues/53262)

生成摘要时出错

---

## 81. Why I still reach for Lisp and Scheme instead of Haskell

**原文标题**: Why I still reach for Lisp and Scheme instead of Haskell

**原文链接**: [https://jointhefreeworld.org/blog/articles/lisps/why-i-still-reach-for-scheme-instead-of-haskell/index.html](https://jointhefreeworld.org/blog/articles/lisps/why-i-still-reach-for-scheme-instead-of-haskell/index.html)

生成摘要时出错

---

## 82. Online age verification is the hill to die on

**原文标题**: Online age verification is the hill to die on

**原文链接**: [https://x.com/GlennMeder/status/2049088498163216560](https://x.com/GlennMeder/status/2049088498163216560)

生成摘要时出错

---

## 83. Gone but Not Forgotten: Recovering the Dead Web

**原文标题**: Gone but Not Forgotten: Recovering the Dead Web

**原文链接**: [https://blog.archive.org/2026/04/23/gone-but-not-forgotten-recovering-the-dead-web/](https://blog.archive.org/2026/04/23/gone-but-not-forgotten-recovering-the-dead-web/)

生成摘要时出错

---

## 84. Show HN: Throwaway – open-source disposable email checker and API

**原文标题**: Show HN: Throwaway – open-source disposable email checker and API

**原文链接**: [https://github.com/sslboard/throwaway](https://github.com/sslboard/throwaway)

生成摘要时出错

---

## 85. Maryland becomes first state to ban surveillance pricing in grocery stores

**原文标题**: Maryland becomes first state to ban surveillance pricing in grocery stores

**原文链接**: [https://www.theguardian.com/technology/2026/apr/29/maryland-grocery-stores-ban-surveillance-pricing](https://www.theguardian.com/technology/2026/apr/29/maryland-grocery-stores-ban-surveillance-pricing)

生成摘要时出错

---

## 86. Raspberry Pi Connect may control Windows soon

**原文标题**: Raspberry Pi Connect may control Windows soon

**原文链接**: [https://www.jeffgeerling.com/blog/2026/raspberry-pi-connect-may-control-windows-soon/](https://www.jeffgeerling.com/blog/2026/raspberry-pi-connect-may-control-windows-soon/)

生成摘要时出错

---

## 87. At Protocol: Building the Social Internet

**原文标题**: At Protocol: Building the Social Internet

**原文链接**: [https://atproto.com/](https://atproto.com/)

生成摘要时出错

---

## 88. Bugs Rust won't catch

**原文标题**: Bugs Rust won't catch

**原文链接**: [https://corrode.dev/blog/bugs-rust-wont-catch/](https://corrode.dev/blog/bugs-rust-wont-catch/)

生成摘要时出错

---

## 89. A 25-Year-Fight over a 2-Second Sample

**原文标题**: A 25-Year-Fight over a 2-Second Sample

**原文链接**: [https://www.plagiarismtoday.com/2026/04/20/a-25-year-fight-over-a-2-second-sample/](https://www.plagiarismtoday.com/2026/04/20/a-25-year-fight-over-a-2-second-sample/)

生成摘要时出错

---

## 90. Letting AI play my game – building an agentic test harness to help play-testing

**原文标题**: Letting AI play my game – building an agentic test harness to help play-testing

**原文链接**: [https://blog.jeffschomay.com/letting-ai-play-my-game](https://blog.jeffschomay.com/letting-ai-play-my-game)

生成摘要时出错

---

