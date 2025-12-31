# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-12-31.md)

*最后自动更新时间: 2025-12-31 17:46:44*
## 1. 《星露谷物语》开发者向开源 C# 框架 MonoGame 捐赠了 12.5 万美元。

**原文标题**: Stardew Valley developer made a $125k donation to the FOSS C# framework MonoGame

**原文链接**: [https://monogame.net/blog/2025-12-30-385-new-sponsor-announcement/](https://monogame.net/blog/2025-12-30-385-new-sponsor-announcement/)

MonoGame 基金会于 2025 年 12 月 30 日宣布，《星露谷物语》的开发者 Eric Barone 已向该项目捐赠了 **12.5 万美元**。

MonoGame 是一个基于 C# 的自由开源软件 (FOSS) 框架，也是《星露谷物语》的底层引擎。这笔捐款体现了开发者对助力游戏取得成功的工具所做出的重大回馈。

在宣布此次赞助的同时，MonoGame 基金会还列出了社区可以持续支持和改进该框架的几种方式：

*   **资金支持：** 接受通过 GitHub、PayPal 和 Patreon 进行的捐款。
*   **周边商品：** 专门的商店提供 MonoGame 品牌装备。
*   **技术参与：** 基金会鼓励开发者提交 Pull Request、在社区 Discord 中帮助他人，并参与通过修复漏洞和增加新功能获取报酬的悬赏计划。

此次合作是该基金会的一个重要里程碑，进一步强化了其为独立游戏行业提供易用、高质量开发工具的使命。

---

## 2. 从脚手架到超人：课程学习如何攻克 2048 和俄罗斯方块

**原文标题**: Scaffolding to Superhuman: How Curriculum Learning Solved 2048 and Tetris

**原文链接**: [https://kywch.github.io/blog/2025/12/curriculum-learning-2048-tetris/](https://kywch.github.io/blog/2025/12/curriculum-learning-2048-tetris/)

本文详细介绍了作者如何利用 PufferLib 和消费级硬件（RTX 4090）训练强化学习 (RL) 智能体，使其在《2048》和《俄罗斯方块》中达到超越人类的水平。核心哲学强调快速迭代、系统的超参数扫描，以及最重要的——**课程学习**。

**主要成就：**
*   **2048：** 一个训练时长仅 75 分钟、大小为 15MB 的策略模型，其表现超越了 TB 级别的巨型搜索方案。它在 65,536 方块上的成功率为 14.75%，在 32,768 方块上的成功率为 71.22%。成功的关键在于“脚手架式课程”——通过让智能体在高级残局状态（如 32k+ 方块）中生成，使其能够练习在常规情况下极难遇到的高难度操作。
*   **俄罗斯方块：** 作者发现“Bug 也能成为特性”。一段损坏观察结果的代码错误反而让智能体更具鲁棒性。这演变为一种课程策略：在训练早期注入“垃圾行”和噪声，使智能体为后期的超高速混乱局面做好准备。

**成功“秘诀”：**
1.  **速度与迭代：** PufferLib 基于 C 语言的环境支持每秒数百万步的模拟，将强化学习从“猜测”转变为通过数百次超参数扫描进行的系统性搜索。
2.  **观察与奖励设计：** 作者优先为策略模型提供高质量信息（如 2048 中的“蛇形模式”标记），并在扩大规模前精调奖励信号。
3.  **课程优于规模：** 作者认为智能体无法学习其从未经历过的事情。只有在穷尽了课程学习和观察改进的手段后，才应该考虑扩大网络规模。

**结论：**
该项目证明，通过注重模拟速度和精选经验的、严谨且“重磨练”的 RL 方法，个人开发者即便使用游戏台式机，也能超越传统的顶尖（SOTA）系统。

---

## 3. 编译器是你最好的朋友，别再骗它了。

**原文标题**: The Compiler Is Your Best Friend, Stop Lying to It

**原文链接**: [https://blog.daniel-beskin.com/2025-12-22-the-compiler-is-your-best-friend-stop-lying-to-it](https://blog.daniel-beskin.com/2025-12-22-the-compiler-is-your-best-friend-stop-lying-to-it)

《编译器是你最好的朋友，别再欺骗它了》一文指出，拥抱编译器的类型系统对于预防生产环境故障和确保代码长期稳定至关重要。通过将编译器视为合作伙伴而非障碍，开发者可以在开发阶段捕捉错误，从而避免灾难性的运行时崩溃。

作者揭示了编译过程（解析、类型检查、优化和代码生成）的奥秘，并对比了不同语言如何利用这些步骤：

*   **Rust (提前编译/AOT)：** 专注于性能和内存安全。其“借用检查器”在编译时强制执行严格的所有权规则，无需垃圾回收器即可消除数据竞态和悬空指针等问题。
*   **Java (即时编译/JIT)：** 通过编译成 Java 虚拟机 (JVM) 字节码来优先保证可移植性。其 JIT 编译器通过识别“热点”在运行时优化代码，从而根据实际执行模式进行激进的性能提升。
*   **TypeScript (转译器)：** 旨在扩展 JavaScript 代码库。它采用“渐进类型”以实现增量采用，并使用“结构类型”来模拟动态语言的“鸭子类型”特性。

文章还解释了“自举”（Bootstrapping），即一种语言通过编译自身源代码来实现“自托管”的元过程。这通常会产生一些既能惠及编译器开发者，也能惠及普通开发者的语言特性（如模式匹配）。

核心观点是，尽管开发者常受诱惑通过“撒谎”（如强制类型转换）来绕过类型系统，但这样做忽视了保障软件可靠性最有效的工具。配合编译器的约束能带来更健壮、更易维护的代码，并最终减少深夜处理生产事故的频率。

---

## 4. 阿金航天器设计法则 [pdf]

**原文标题**: Akin's Laws of Spacecraft Design [pdf]

**原文链接**: [https://www.ece.uvic.ca/~elec399/201409/Akin%27s%20Laws%20of%20Spacecraft%20Design.pdf](https://www.ece.uvic.ca/~elec399/201409/Akin%27s%20Laws%20of%20Spacecraft%20Design.pdf)

**《阿金的航天器设计法则》**是由马里兰大学空间系统实验室主任戴维·阿金（Dr. David Akin）博士汇编的一套著名工程准则。这些法则为航空航天工程师提供了实用且不失幽默的指导，将复杂的航天器开发过程浓缩为精练且具操作性的智慧。

这些法则聚焦于高风险工程中不可或缺的几个核心主题：

*   **严谨与数据：** 第一条法则——“工程是靠数字完成的。没有数字的分析仅仅是观点”——奠定了基调。阿金强调，设计必须植根于可量化的事实，而非直觉。
*   **设计的矛盾：** 阿金指出了该领域所需的双重心理：设计师必须是乐观主义者，以构思任务的可能性；同时必须是坚定的悲观主义者，以识别并化解每一个潜在的故障点。
*   **简洁与可靠：** 许多法则警告不要进行“镀金”（增加不必要的复杂性）。阿金有一句名言：任何依赖于人类完美表现的设计在根本上都是有缺陷的，且“使系统可靠的最佳方法就是使其简单”。
*   **测试与验证：** 一个反复出现的主题是验证的必要性。阿金断言，如果你还没有在实际运行环境中测试过某个组件，就应该假定它会失败。
*   **进度与成本：** 他对项目管理进行了冷峻的现实审视，指出进度总是会推迟，并且“最后 10% 的性能提升会消耗三分之一的成本，并引发三分之二的问题”。

总之，这份文件是系统工程的基石，它提醒从业者，航天器设计是一个迭代且不容差错的过程，必须预见人为错误，而简洁才是终极的美德。

---

## 5. 2025年是Windows 11的灾难之年：Bug与侵入性功能正不断侵蚀用户信任。

**原文标题**: 2025 was a disaster for Windows 11 as bugs and intrusive features erode trust

**原文链接**: [https://www.windowscentral.com/microsoft/windows-11/2025-has-been-an-awful-year-for-windows-11-with-infuriating-bugs-and-constant-unwanted-features](https://www.windowscentral.com/microsoft/windows-11/2025-has-been-an-awful-year-for-windows-11-with-infuriating-bugs-and-constant-unwanted-features)

根据文章所述，2025年对 Windows 11 而言是“灾难性”的一年，其标志是发展重心的迷失和用户信任的流失。作者认为，微软激进且往往是强制性的 AI 集成（例如在记事本等应用中植入 Copilot）将追逐潮流置于平台稳定性和安全性之上。

挫败感的一个主要来源是“持续创新”战略和“受控功能推送”（CFR）系统。由于每月发布新功能而非进行重大的年度更新，微软造成了碎片化的体验，导致两台完全相同的电脑可能拥有不同的功能。这种持续的更迭，加上感知上的质量控制下降，导致了频繁的漏洞和往往需要数周才能修复的“半成品”功能。此外，作者还批评了向 Web 应用（如新版 Outlook）转型的趋势，称其与原生 UI 相比运行缓慢且缺乏优化。

这些内部困局正值外部威胁加剧之际。竞争对手正伺机利用 Windows 的弱点：
* **谷歌**正在为低端市场开发 Android 电脑。
* **Valve**正将 SteamOS 定位为游戏玩家的有力替代方案。
* **苹果**据传正计划推出更实惠的 MacBook。

尽管存在这些失败，文章也指出了一些改进。微软在 UI 一致性方面取得了长足进步，特别是在深色模式和任务栏动画方面。新的“开始”菜单提供了更好的自定义功能，系统恢复选项也经过了精简，能更有效地处理更新失败。此外，凭借 Xbox 应用的增强，Windows 11 仍然是一个强大的游戏平台。

最后，作者警告称，除非微软重新聚焦于质量和以用户为中心的设计，否则它将面临把大量市场份额拱手让给那些更优化、更专注的竞争对手的风险。

---

## 6. 从大气中捕集二氧化碳的高效方法 / 赫尔辛基大学

**原文标题**: Efficient method to capture CO2 from the atmosphere / Univ of Helsinki

**原文链接**: [https://www.helsinki.fi/en/news/innovations/efficient-method-capture-carbon-dioxide-atmosphere-developed-university-helsinki](https://www.helsinki.fi/en/news/innovations/efficient-method-capture-carbon-dioxide-atmosphere-developed-university-helsinki)

赫尔辛基大学化学系的研究人员开发出一种极具前景的二氧化碳直接空气捕捉（DAC）新方法，该方法利用了一种可循环使用的超强碱-醇液体。

**核心特性与性能**
这种由苯甲醇与超强碱 TBN（1,5,7-三氮杂双环[4.3.0]壬-6-烯）结合而成的新型化合物，每克材料可吸收 156 毫克二氧化碳。值得注意的是，该化合物具有高度选择性，仅与二氧化碳反应，而不会与其他大气气体（如氧气和氮气）发生反应。

**显著优势**
主要的突破在于回收过程的能源效率。目前的工业二氧化碳捕捉方法通常需要超过 900°C 的高温才能释放捕捉到的气体，而这种新化合物仅需 70°C 并在约 30 分钟内即可释放纯净的二氧化碳。这种较低的温度阈值显著降低了循环使用所需的能量。此外，该组分无毒且生产成本较低。

**耐用性与未来展望**
该材料设计用于多次循环使用，在 50 次循环后仍能保持 75% 的原始容量，100 次循环后仍能保持 50%。在博士后研究员 Zahra Eshaghi Gorji 的带领下，团队目前正准备进行接近工业规模的试点测试。为了促进这一转型，研究人员正致力于通过将该液体化合物与二氧化硅和氧化石墨烯等材料结合，开发其固态版本，以优化其与大气的相互作用。

---

## 7. SigNoz (YC W21，开源可观测性平台) 正在招聘多个岗位

**原文标题**: SigNoz (YC W21, open source observability platform) Is Hiring across roles

**原文链接**: [https://signoz.io/careers](https://signoz.io/careers)

开源可观测性平台 SigNoz（Y Combinator 2021年冬季，即 YC W21 孵化企业）近日宣布，正面向多个部门积极招聘多个职位。

作为 Datadog 和 New Relic 等专有工具的开源替代方案，SigNoz 为开发人员提供了一个统一的界面，用于监控指标、分布式追踪和日志。此次招聘计划标志着公司进入了增长期，旨在进一步扩大平台规模，并增强其工程与运营能力。

有意向的候选人请访问 SigNoz 官方招聘门户，查看具体职位空缺及申请要求。

---

## 8. Fifteen Most Famous Transcendental Numbers

**原文标题**: Fifteen Most Famous Transcendental Numbers

**原文链接**: [https://sprott.physics.wisc.edu/pickover/trans.html](https://sprott.physics.wisc.edu/pickover/trans.html)

生成摘要时出错

---

## 9. When square pixels aren't square

**原文标题**: When square pixels aren't square

**原文链接**: [https://alexwlchan.net/2025/square-pixels/](https://alexwlchan.net/2025/square-pixels/)

生成摘要时出错

---

## 10. Show HN: Use Claude Code to Query 600 GB Indexes over Hacker News, ArXiv, etc.

**原文标题**: Show HN: Use Claude Code to Query 600 GB Indexes over Hacker News, ArXiv, etc.

**原文链接**: [https://exopriors.com/scry](https://exopriors.com/scry)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 2 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 3 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 4 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 5 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 6 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 7 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 8 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 9 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 10 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 11 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 12 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 13 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 14 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 15 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 16 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 17 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 18 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 19 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 20 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 21 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 22 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 23 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 24 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 25 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 26 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 27 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 28 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 29 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 30 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 31 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 32 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 33 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 34 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 35 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 36 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 37 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 38 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 39 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 40 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 41 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 42 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 43 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 44 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 45 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 46 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 47 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 48 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 49 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 50 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 51 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 52 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 53 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 54 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 55 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 56 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 57 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 58 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 59 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 60 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 61 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 62 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 63 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 64 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 65 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 66 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 67 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 68 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 69 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 70 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 71 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 72 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 73 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 74 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 75 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 76 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 77 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 78 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 79 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 80 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 81 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 82 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 83 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 84 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 85 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 86 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 87 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 88 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 89 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 90 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 91 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 92 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 93 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 94 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 95 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 96 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 97 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 98 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 99 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 100 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 101 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 102 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 103 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 104 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 105 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 106 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 107 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 108 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 109 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 110 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 111 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 112 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 113 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 114 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 115 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 116 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 117 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 118 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 119 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 120 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 121 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 122 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 123 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 124 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 125 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 126 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 127 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 128 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 129 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 130 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 131 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 132 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 133 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 134 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 135 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 136 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 137 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 138 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 139 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 140 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 141 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 142 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 143 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 144 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 145 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 146 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 147 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 148 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 149 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 150 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 151 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 152 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 153 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 154 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 155 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 156 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 157 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 158 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 159 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 160 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 161 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 162 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 163 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 164 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 165 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 166 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 167 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 168 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 169 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 170 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 171 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 172 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 173 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 174 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 175 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 176 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 177 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 178 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 179 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 180 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 181 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 182 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 183 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 184 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 185 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 186 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 187 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 188 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 189 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 190 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 191 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 192 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 193 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 194 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 195 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 196 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 197 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 198 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 199 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 200 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 201 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 202 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 203 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 204 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 205 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 206 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 207 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 208 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 209 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 210 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 211 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 212 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 213 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 214 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 215 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 216 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 217 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 218 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 219 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 220 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 221 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 222 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 223 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 224 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 225 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 226 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 227 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 228 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 229 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 230 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 231 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 232 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 233 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 234 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 235 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 236 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 237 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 238 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 239 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 240 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 241 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 242 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 243 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 244 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 245 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 246 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 247 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 248 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 249 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 250 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 251 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 252 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 253 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 254 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 255 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 256 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 257 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 258 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 259 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 260 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 261 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 262 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 263 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 264 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 265 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 266 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 267 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 268 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 269 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 270 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 271 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 272 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 273 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 274 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 275 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 276 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 277 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 278 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 279 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 280 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 281 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 282 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 283 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 284 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 285 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 286 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
