# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-15.md)

*最后自动更新时间: 2026-04-15 18:30:41*
## 1. 神眠于矿物

**原文标题**: God Sleeps in the Minerals

**原文链接**: [https://wchambliss.wordpress.com/2026/03/03/god-sleeps-in-the-minerals/](https://wchambliss.wordpress.com/2026/03/03/god-sleeps-in-the-minerals/)

这篇题为《神眠于矿物之中》（日期为2026年3月3日）的博文收录了一系列拍摄于洛杉矶县自然历史博物馆的照片。这些快照展示了“出土：原始之美”（Unearthed: Raw Beauty）展览，重点呈现了各类矿物标本。

该博文在发布后不久便引起了广泛的网络关注，其被收录进2026年4月的Hacker News每日摘要及各类数字“快讯”便是佐证。文中收录的15条回复反映出受众两极分化且略显困惑的反应。尽管一些评论者赞美照片的精美，但接连有用户询问“这是什么？”，暗示人们对该博文的背景或意图感到不解。

此外，标题还在评论区引发了一场短暂的神学冲突：一名用户认为“神眠”一词冒犯了其宗教信仰，而其他用户则以哲学调侃、不敬的言辞或简单的信仰表白予以回应。归根结底，这篇博文既是博物馆之行的简要视觉记录，也触发了一场广泛的社交媒体对话。

---

## 2. 开源未死，Cal.com 只是吸取了错误的教训。

**原文标题**: Open Source Isn't Dead. Cal.com Just Learned the Wrong Lesson

**原文链接**: [https://www.strix.ai/blog/cal-com-is-closing-its-code-due-to-ai-threats](https://www.strix.ai/blog/cal-com-is-closing-its-code-due-to-ai-threats)

在《开源并未消亡，Cal.com 只是吸取了错误的教训》一文中，Strix 批评了 Cal.com 放弃传统开源许可、转向更具限制性的商业条款的决定。作者认为，Cal.com 的转型旨在保护公司免受“克隆”和竞争对手的侵害，但这实际上是对开源企业所面临挑战的误诊。

文章概述了几个关键点：

*   **“抽地毯”（Rug-Pull）现象：** Strix 指出了一种令人不安的趋势，即公司利用“开源”品牌来建立社区并获取开发者信任，而一旦面临变现压力或需要满足风险投资的预期，便转向专有许可或“源码可用”许可。
*   **开源不是一种商业模式：** 作者断言，开源是一种开发和分发方法论，而非财务战略。Cal.com 的困境并非开源哲学的失败，而是未能建立起一个不依赖代码稀缺性的、具有防御力的商业模式。
*   **错位的指责：** Cal.com 将许可变更归咎于竞争和克隆，却忽略了真正的开源成功需要提供原始代码之外的价值——如卓越的托管服务、企业级支持和生态系统集成。
*   **社区信任：** 文章警告称，这些许可转向会引发贡献者的怀疑，从而损害更广泛的生态系统。当公司优先考虑保护厂商利益而非用户自由时，就会失去最初为其提供竞争优势的社区。

Strix 最终总结道，开源正在蓬勃发展，但它要求公司在软件之上进行创新，而不是在市场竞争加剧时试图设限。Cal.com 的“错误教训”在于误以为许可协议是问题的根源，而实际上问题在于其差异化策略。

---

## 3. CPU 尚未过时：Gemma 2B 在让 GPT-3.5 Turbo 声名鹊起的测试中得分更高

**原文标题**: CPUs Aren't Dead. Gemma2B Out Scored GPT-3.5 Turbo on Test That Made It Famous

**原文链接**: [https://seqpu.com/CPUsArentDead/](https://seqpu.com/CPUsArentDead/)

SeqPU 团队的调研报告指出，高性能 AI 必须依赖 GPU 集群的时代正在终结。他们的测试显示，谷歌的 **Gemma 2B**（一款拥有 20 亿参数的开源权重模型）在 **MT-Bench** 测试中获得了 **~8.0** 的评分，超越了参数量大其 87 倍的 **GPT-3.5 Turbo**（得分为 7.94）。

这一突破证明，生产级推理现在可以在标准的笔记本电脑 CPU（4 核，16GB 内存）上本地运行，而不再需要依赖昂贵的闭源 API。该模型仅为 4GB，可以免费下载并离线运行，确保了完整的数据隐私并消除了供应商锁定。对于云端部署，团队建议使用 Cloudflare 容器，每月成本仅需 5 美元。

一个核心发现是，AI 能力正在从“算力问题”转向**“软件工程问题”**。团队在原始模型中识别出了七个特定的“失效类别”，例如算术漂移和逻辑承诺错误。通过应用“外科手术式修复”——每项修复仅需约 60 行 Python 代码，例如针对数学计算使用 PAL（程序辅助语言）封装——模型的评分攀升至 **~8.2**，开始逼近 GPT-4 的水准。

**关键对比：**
*   **性能：** 达到或超越 GPT-3.5 Turbo。
*   **硬件：** 在消费级 CPU 上运行；无需 GPU。
*   **成本：** 0 元（本地）或 5 美元/月（云端），对比按 Token 计费的 API。
*   **延迟：** CPU 响应时间为 30–60 秒（比 GPU 慢，但质量相当）。

团队已发布了基准测试结果的“完整记录”以及一个用于公开验证的实时 Telegram 机器人。他们得出结论：任何有动力的开发者，现在都能通过精巧的软件支架工程，在短短一个周末内缩小本地开源模型与前沿云端 AI 之间的差距。

---

## 4. 想写编译器？只需阅读这两篇论文 (2008)

**原文标题**: Want to Write a Compiler? Just Read These Two Papers (2008)

**原文链接**: [https://prog21.dadgum.com/30.html](https://prog21.dadgum.com/30.html)

在这篇文章中，James Hague 指出编写编译器的难度其实是一种误解，这主要是由那些过度偏重宽泛理论而非实际操作的学术教科书造成的。Hague 建议不要从像《龙书》（Dragon Book）这样晦涩的资源入手，而是通过两份关键资源，采取一种更易上手、更注重实践的方法。

首先，他重点推介了 **Jack Crenshaw 的《让我们来写个编译器！》（Let’s Build a Compiler!）**系列。Hague 称赞这套教程简单易懂，它教导初学者如何构建单通（single-pass）编译器。虽然原系列为了保持 Pascal 代码简洁而避开了内部表示（如抽象语法树），但 Hague 指出，使用 Python、Haskell 或 Lisp 等现代高级语言，处理这些结构会变得非常简单。

其次，他推荐了由 Sarkar、Waddell 和 Dybvig 撰写的论文 **《编译器教育中的 Nanopass 框架》（A Nanopass Framework for Compiler Education）**。该资源引入了一种理念：编译器应该被构造成一系列极小、简单的转换（passes），而不是少数几个复杂的转换。这种“nanopass”方法使开发过程更易于管理，也更方便调试。

Hague 的核心观点是，有志于此的开发者应当首先关注构建实用工具的“方法论”。通过掌握微小、离散的转换并利用高级语言，编写编译器将成为任何程序员都能完成的任务。他建议，只有在构建出一个可运行的编译器之后，再深入研究更高级的理论著作。

---

## 5. 睡眠好，学习好 (2012)

**原文标题**: Good Sleep, Good Learning (2012)

**原文链接**: [https://super-memory.com/articles/sleep.htm](https://super-memory.com/articles/sleep.htm)

皮奥特·沃兹尼亚克（Piotr Wozniak）博士的《好睡眠，好学习》（"Good Sleep, Good Learning"）是对睡眠科学的全面综合论述，旨在优化智力表现和创造力。沃兹尼亚克认为，睡眠不仅仅是休息，而是一个关键的神经生理过程，对于记忆巩固和“神经优化”至关重要。

本文的核心是“睡眠双过程模型”，该模型由昼夜节律（生物钟）和稳态过程（睡眠压力的积累）组成。沃兹尼亚克的主要建议是“自由睡眠”（free running sleep）——即只在疲倦时入睡，并在没有闹钟的情况下自然醒来。他指出闹钟是脑功能的主要抑制因素，会导致“睡眠惯性”并损害大脑巩固信息的能力。

核心要点包括：
*   **记忆巩固：** 沃兹尼亚克用“硬盘与内存”的比喻解释道，睡眠将记忆从短期储存转移到长期储存，同时进行“垃圾回收”以清除神经干扰。
*   **小睡：** 作者提倡双相睡眠，认为午睡（siesta）是自然的生理需求，能提升创造力和警觉性。
*   **多相睡眠：** 沃兹尼亚克强烈反对“Uberman式”多相睡眠计划，称其不可持续，且有害于高水平的智力成就。
*   **睡眠障碍：** 诸如睡眠相位后移综合征（DSPS）和失眠等病症，通常最好通过采用自由睡眠计划而非依赖药物来治疗。
*   **学习影响：** 研究表明，睡眠不足会显著降低回忆能力和获取新知识的能力，这使得“牺牲睡眠来学习”变得适得其反。

最终，沃兹尼亚克断言，尊重生物睡眠信号是提高人类智力和保持长期健康最有效的方法。

---

## 6. Show HN：Libretto – 让 AI 浏览器自动化具备确定性

**原文标题**: Show HN: Libretto – Making AI browser automations deterministic

**原文链接**: [https://github.com/saffron-health/libretto](https://github.com/saffron-health/libretto)

Libretto 是由 Saffron Health 开发的一款开源工具包，旨在帮助 AI 编程智能体构建和维护稳健的 Web 集成。它提供了一个实时浏览器环境和高效利用 Token 的命令行界面（CLI），使智能体能够确定性地执行复杂的自动化任务。

该工具包的主要功能包括：

*   **实时页面审查：** 智能体可以以极低的上下文开销分析实时网页，通过专门的快照分析，将繁重的视觉数据排除在 LLM 主上下文窗口之外。
*   **网络流量捕获：** 用户可以通过捕获网络流量对网站 API 进行逆向工程。这使得智能体能够将缓慢、脆弱的 UI 自动化转变为运行速度更快、更可靠的直接网络请求脚本。
*   **动作录制与回放：** Libretto 可以录制浏览器中的手动用户操作，并将其自动转换为 Playwright 自动化脚本。
*   **交互式调试：** 当集成失败时，智能体可以自主重现错误，检查实时页面，并实时修复失效的选择器或逻辑。

Libretto 支持 OpenAI、Anthropic 和 Gemini 等主流 LLM 供应商，以支持其快照分析功能。它还具备强大的会话管理功能，允许开发人员在不同运行任务之间保存和复用身份验证状态（如 Cookie 和 localStorage）。

通过提供这些工具，Libretto 旨在弥合脆弱的浏览器脚本与可靠集成之间的差距，从而显著降低开发人员针对 Web 软件实现复杂工作流自动化的难度。

---

## 7. 解决由于椅子静电导致的显示器黑屏、断电或闪烁问题。

**原文标题**: Fix monitor that goes black, off or blinks due to static electricity in chair

**原文链接**: [https://aalonso.dev/blog/2023/how-to-fix-monitor-that-goes-black-off-due-to-static-electricity-in-chair/](https://aalonso.dev/blog/2023/how-to-fix-monitor-that-goes-black-off-due-to-static-electricity-in-chair/)

本文解释了一种离奇但有据可查的现象：办公椅（特别是像宜家 Markus 这样带有气压升降机构的椅子）会导致外接显示器闪烁、黑屏或断连。

作者确定了造成这一现象的两个主要原因：
1. **静电：** 动作产生的摩擦会积聚电荷，从而导致电击感和信号干扰。
2. **EMI 脉冲：** 当人坐下或站起时，气压升降机构会产生电磁干扰 (EMI) 脉冲。这种干扰通常会被敏感的视频线缆（尤其是 DisplayPort 线缆和各种 USB-C 适配器）捕捉到。

为了解决这些问题，作者实施了两种实用的硬件方案：
* **椅子接地：** 为了泄放静电，作者在椅子上连接了一条保持触地的细金属链，从而显著降低了电击发生的频率。
* **铁氧体磁环：** 为了对抗 EMI，作者在视频线缆上安装了铁氧体磁芯（抑制滤波器）。这些磁环有助于在干扰到达显示器之前将其滤除。

虽然在剧烈移动时这些措施未能完全消除问题，但它们显著提高了显示器的稳定性，并减少了黑屏和静电电击的频率。作者总结道，虽然这些“极客式”的修复方法看起来有些不同寻常，但对于稳定受环境干扰困扰的家庭办公环境而言，它们是行之有效的工具。

---

## 8. Adaptional (YC S25) Is Hiring Founding AI Engineers

**原文标题**: Adaptional (YC S25) Is Hiring Founding AI Engineers

**原文链接**: [https://www.ycombinator.com/companies/adaptional/jobs/k7W6ge9-founding-engineer](https://www.ycombinator.com/companies/adaptional/jobs/k7W6ge9-founding-engineer)

生成摘要时出错

---

## 9. How do Wake-On-LAN works

**原文标题**: How do Wake-On-LAN works

**原文链接**: [https://blog.xaner.dev/post/wake-on-lan/](https://blog.xaner.dev/post/wake-on-lan/)

生成摘要时出错

---

## 10. Google Broke Its Promise to Me. Now ICE Has My Data

**原文标题**: Google Broke Its Promise to Me. Now ICE Has My Data

**原文链接**: [https://www.eff.org/deeplinks/2026/04/google-broke-its-promise-me-now-ice-has-my-data](https://www.eff.org/deeplinks/2026/04/google-broke-its-promise-me-now-ice-has-my-data)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 2 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 3 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 4 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 5 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 6 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 7 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 8 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 9 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 10 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 11 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 12 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 13 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 14 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 15 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 16 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 17 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 18 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 19 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 20 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 21 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 22 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 23 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 24 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 25 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 26 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 27 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 28 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 29 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 30 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 31 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 32 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 33 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 34 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 35 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 36 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 37 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 38 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 39 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 40 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 41 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 42 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 43 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 44 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 45 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 46 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 47 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 48 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 49 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 50 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 51 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 52 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 53 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 54 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 55 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 56 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 57 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 58 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 59 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 60 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 61 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 62 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 63 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 64 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 65 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 66 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 67 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 68 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 69 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 70 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 71 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 72 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 73 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 74 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 75 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 76 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 77 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 78 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 79 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 80 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 81 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 82 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 83 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 84 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 85 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 86 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 87 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 88 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 89 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 90 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 91 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 92 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 93 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 94 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 95 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 96 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 97 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 98 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 99 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 100 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 101 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 102 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 103 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 104 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 105 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 106 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 107 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 108 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 109 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 110 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 111 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 112 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 113 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 114 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 115 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 116 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 117 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 118 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 119 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 120 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 121 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 122 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 123 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 124 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 125 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 126 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 127 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 128 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 129 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 130 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 131 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 132 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 133 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 134 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 135 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 136 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 137 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 138 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 139 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 140 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 141 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 142 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 143 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 144 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 145 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 146 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 147 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 148 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 149 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 150 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 151 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 152 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 153 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 154 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 155 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 156 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 157 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 158 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 159 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 160 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 161 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 162 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 163 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 164 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 165 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 166 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 167 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 168 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 169 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 170 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 171 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 172 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 173 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 174 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 175 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 176 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 177 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 178 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 179 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 180 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 181 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 182 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 183 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 184 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 185 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 186 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 187 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 188 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 189 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 190 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 191 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 192 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 193 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 194 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 195 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 196 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 197 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 198 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 199 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 200 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 201 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 202 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 203 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 204 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 205 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 206 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 207 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 208 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 209 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 210 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 211 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 212 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 213 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 214 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 215 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 216 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 217 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 218 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 219 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 220 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 221 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 222 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 223 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 224 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 225 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 226 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 227 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 228 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 229 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 230 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 231 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 232 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 233 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 234 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 235 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 236 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 237 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 238 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 239 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 240 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 241 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 242 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 243 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 244 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 245 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 246 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 247 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 248 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 249 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 250 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 251 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 252 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 253 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 254 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 255 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 256 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 257 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 258 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 259 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 260 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 261 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 262 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 263 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 264 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 265 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 266 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 267 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 268 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 269 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 270 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 271 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 272 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 273 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 274 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 275 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 276 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 277 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 278 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 279 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 280 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 281 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 282 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 283 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 284 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 285 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 286 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 287 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 288 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 289 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 290 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 291 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 292 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 293 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 294 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 295 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 296 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 297 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 298 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 299 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 300 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 301 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 302 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 303 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 304 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 305 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 306 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 307 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 308 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 309 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 310 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 311 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 312 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 313 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 314 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 315 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 316 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 317 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 318 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 319 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 320 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 321 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 322 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 323 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 324 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 325 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 326 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 327 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 328 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 329 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 330 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 331 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 332 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 333 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 334 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 335 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 336 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 337 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 338 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 339 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 340 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 341 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 342 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 343 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 344 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 345 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 346 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 347 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 348 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 349 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 350 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 351 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 352 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 353 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 354 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 355 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 356 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 357 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 358 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 359 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 360 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 361 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 362 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 363 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 364 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 365 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 366 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 367 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 368 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 369 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 370 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 371 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 372 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 373 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 374 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 375 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 376 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 377 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 378 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 379 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 380 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 381 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 382 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 383 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 384 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 385 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 386 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 387 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 388 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 389 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 390 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 391 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
