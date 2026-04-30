# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-30.md)

*最后自动更新时间: 2026-04-30 18:35:48*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 2 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 3 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 4 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 5 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 6 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 7 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 8 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 9 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 10 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 11 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 12 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 13 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 14 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 15 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 16 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 17 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 18 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 19 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 20 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 21 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 22 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 23 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 24 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 25 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 26 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 27 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 28 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 29 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 30 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 31 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 32 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 33 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 34 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 35 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 36 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 37 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 38 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 39 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 40 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 41 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 42 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 43 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 44 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 45 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 46 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 47 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 48 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 49 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 50 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 51 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 52 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 53 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 54 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 55 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 56 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 57 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 58 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 59 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 60 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 61 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 62 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 63 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 64 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 65 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 66 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 67 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 68 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 69 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 70 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 71 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 72 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 73 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 74 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 75 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 76 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 77 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 78 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 79 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 80 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 81 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 82 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 83 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 84 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 85 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 86 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 87 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 88 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 89 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 90 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 91 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 92 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 93 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 94 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 95 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 96 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 97 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 98 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 99 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 100 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 101 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 102 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 103 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 104 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 105 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 106 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 107 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 108 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 109 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 110 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 111 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 112 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 113 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 114 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 115 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 116 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 117 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 118 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 119 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 120 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 121 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 122 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 123 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 124 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 125 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 126 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 127 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 128 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 129 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 130 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 131 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 132 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 133 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 134 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 135 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 136 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 137 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 138 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 139 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 140 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 141 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 142 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 143 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 144 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 145 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 146 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 147 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 148 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 149 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 150 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 151 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 152 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 153 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 154 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 155 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 156 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 157 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 158 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 159 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 160 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 161 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 162 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 163 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 164 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 165 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 166 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 167 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 168 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 169 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 170 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 171 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 172 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 173 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 174 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 175 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 176 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 177 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 178 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 179 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 180 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 181 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 182 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 183 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 184 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 185 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 186 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 187 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 188 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 189 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 190 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 191 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 192 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 193 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 194 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 195 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 196 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 197 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 198 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 199 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 200 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 201 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 202 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 203 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 204 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 205 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 206 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 207 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 208 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 209 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 210 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 211 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 212 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 213 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 214 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 215 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 216 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 217 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 218 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 219 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 220 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 221 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 222 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 223 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 224 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 225 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 226 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 227 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 228 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 229 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 230 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 231 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 232 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 233 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 234 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 235 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 236 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 237 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 238 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 239 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 240 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 241 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 242 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 243 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 244 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 245 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 246 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 247 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 248 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 249 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 250 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 251 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 252 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 253 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 254 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 255 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 256 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 257 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 258 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 259 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 260 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 261 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 262 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 263 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 264 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 265 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 266 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 267 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 268 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 269 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 270 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 271 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 272 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 273 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 274 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 275 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 276 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 277 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 278 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 279 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 280 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 281 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 282 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 283 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 284 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 285 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 286 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 287 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 288 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 289 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 290 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 291 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 292 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 293 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 294 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 295 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 296 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 297 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 298 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 299 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 300 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 301 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 302 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 303 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 304 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 305 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 306 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 307 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 308 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 309 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 310 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 311 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 312 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 313 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 314 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 315 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 316 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 317 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 318 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 319 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 320 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 321 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 322 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 323 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 324 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 325 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 326 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 327 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 328 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 329 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 330 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 331 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 332 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 333 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 334 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 335 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 336 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 337 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 338 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 339 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 340 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 341 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 342 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 343 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 344 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 345 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 346 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 347 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 348 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 349 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 350 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 351 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 352 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 353 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 354 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 355 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 356 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 357 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 358 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 359 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 360 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 361 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 362 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 363 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 364 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 365 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 366 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 367 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 368 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 369 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 370 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 371 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 372 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 373 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 374 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 375 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 376 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 377 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 378 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 379 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 380 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 381 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 382 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 383 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 384 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 385 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 386 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 387 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 388 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 389 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 390 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 391 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 392 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 393 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 394 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 395 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 396 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 397 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 398 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 399 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 400 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 401 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 402 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 403 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 404 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 405 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 406 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
