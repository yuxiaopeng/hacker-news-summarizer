# Hacker News 热门文章摘要 (2026-04-15)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Forcing an inversion of control on the SaaS stack

**原文标题**: Forcing an inversion of control on the SaaS stack

**原文链接**: [https://www.100x.bot/a/client-side-injection-inversion-of-control-saas](https://www.100x.bot/a/client-side-injection-inversion-of-control-saas)

生成摘要时出错

---

## 12. Do you even need a database?

**原文标题**: Do you even need a database?

**原文链接**: [https://www.dbpro.app/blog/do-you-even-need-a-database](https://www.dbpro.app/blog/do-you-even-need-a-database)

生成摘要时出错

---

## 13. The Future of Everything Is Lies, I Guess: New Jobs

**原文标题**: The Future of Everything Is Lies, I Guess: New Jobs

**原文链接**: [https://aphyr.com/posts/419-the-future-of-everything-is-lies-i-guess-new-jobs](https://aphyr.com/posts/419-the-future-of-everything-is-lies-i-guess-new-jobs)

生成摘要时出错

---

## 14. Gemini Robotics-ER 1.6

**原文标题**: Gemini Robotics-ER 1.6

**原文链接**: [https://deepmind.google/blog/gemini-robotics-er-1-6/](https://deepmind.google/blog/gemini-robotics-er-1-6/)

生成摘要时出错

---

## 15. Anna's Archive loses $322M Spotify piracy case without a fight

**原文标题**: Anna's Archive loses $322M Spotify piracy case without a fight

**原文链接**: [https://torrentfreak.com/annas-archive-loses-322-million-spotify-piracy-case-without-a-fight/](https://torrentfreak.com/annas-archive-loses-322-million-spotify-piracy-case-without-a-fight/)

生成摘要时出错

---

## 16. Costasiella kuroshimae – Solar Powered animals, that do indirect photosynthesis

**原文标题**: Costasiella kuroshimae – Solar Powered animals, that do indirect photosynthesis

**原文链接**: [https://en.wikipedia.org/wiki/Costasiella_kuroshimae](https://en.wikipedia.org/wiki/Costasiella_kuroshimae)

生成摘要时出错

---

## 17. Wacli – WhatsApp CLI

**原文标题**: Wacli – WhatsApp CLI

**原文链接**: [https://github.com/steipete/wacli](https://github.com/steipete/wacli)

生成摘要时出错

---

## 18. Fixing a 20-year-old bug in Enlightenment E16

**原文标题**: Fixing a 20-year-old bug in Enlightenment E16

**原文链接**: [https://iczelia.net/posts/e16-20-year-old-bug/](https://iczelia.net/posts/e16-20-year-old-bug/)

生成摘要时出错

---

## 19. We ran Doom on a 40 year old printer controller (Agfa Compugraphic 9000PS) [video]

**原文标题**: We ran Doom on a 40 year old printer controller (Agfa Compugraphic 9000PS) [video]

**原文链接**: [https://www.youtube.com/watch?v=cltnlks2-uU](https://www.youtube.com/watch?v=cltnlks2-uU)

生成摘要时出错

---

## 20. Where did my taxes go?

**原文标题**: Where did my taxes go?

**原文链接**: [https://wherethefuckdidmytaxesgo.com/](https://wherethefuckdidmytaxesgo.com/)

生成摘要时出错

---

## 21. Metro stop is Ancient Rome's new attraction

**原文标题**: Metro stop is Ancient Rome's new attraction

**原文链接**: [https://www.bbc.com/travel/article/20260408-a-150-metro-ticket-to-ancient-rome](https://www.bbc.com/travel/article/20260408-a-150-metro-ticket-to-ancient-rome)

生成摘要时出错

---

## 22. Pretty Fish: A better mermaid diagram editor

**原文标题**: Pretty Fish: A better mermaid diagram editor

**原文链接**: [https://pretty.fish/](https://pretty.fish/)

生成摘要时出错

---

## 23. Google Gemma 4 Runs Natively on iPhone with Full Offline AI Inference

**原文标题**: Google Gemma 4 Runs Natively on iPhone with Full Offline AI Inference

**原文链接**: [https://www.gizmoweek.com/gemma-4-runs-iphone/](https://www.gizmoweek.com/gemma-4-runs-iphone/)

生成摘要时出错

---

## 24. Show HN: Every CEO and CFO change at US public companies, live from SEC

**原文标题**: Show HN: Every CEO and CFO change at US public companies, live from SEC

**原文链接**: [https://tracksuccession.com/explore](https://tracksuccession.com/explore)

生成摘要时出错

---

## 25. Study: Back-to-basics approach can match or outperform AI in language analysis

**原文标题**: Study: Back-to-basics approach can match or outperform AI in language analysis

**原文链接**: [https://www.manchester.ac.uk/about/news/back-to-basics-approach-can-match-or-outperform-ai/](https://www.manchester.ac.uk/about/news/back-to-basics-approach-can-match-or-outperform-ai/)

生成摘要时出错

---

## 26. The tiniest e-reader in the world, and you can build one yourself

**原文标题**: The tiniest e-reader in the world, and you can build one yourself

**原文链接**: [https://www.androidauthority.com/tiny-e-reader-diy-3657661/](https://www.androidauthority.com/tiny-e-reader-diy-3657661/)

生成摘要时出错

---

## 27. AI ruling prompts warnings from US lawyers: Your chats could be used against you

**原文标题**: AI ruling prompts warnings from US lawyers: Your chats could be used against you

**原文链接**: [https://www.reuters.com/legal/government/ai-ruling-prompts-warnings-us-lawyers-your-chats-could-be-used-against-you-2026-04-15/](https://www.reuters.com/legal/government/ai-ruling-prompts-warnings-us-lawyers-your-chats-could-be-used-against-you-2026-04-15/)

生成摘要时出错

---

## 28. Dependency cooldowns turn you into a free-rider

**原文标题**: Dependency cooldowns turn you into a free-rider

**原文链接**: [https://calpaterson.com/deps.html](https://calpaterson.com/deps.html)

生成摘要时出错

---

## 29. CRISPR takes a bold leap toward silencing Down syndrome's extra chromosome

**原文标题**: CRISPR takes a bold leap toward silencing Down syndrome's extra chromosome

**原文链接**: [https://medicalxpress.com/news/2026-04-crispr-bold-silencing-syndrome-extra.html](https://medicalxpress.com/news/2026-04-crispr-bold-silencing-syndrome-extra.html)

生成摘要时出错

---

## 30. Elevated errors on Claude.ai, API, Claude Code

**原文标题**: Elevated errors on Claude.ai, API, Claude Code

**原文链接**: [https://claudestatus.com/](https://claudestatus.com/)

生成摘要时出错

---

## 31. MIT Radiation Laboratory

**原文标题**: MIT Radiation Laboratory

**原文链接**: [https://www.ll.mit.edu/about/history/mit-radiation-laboratory](https://www.ll.mit.edu/about/history/mit-radiation-laboratory)

生成摘要时出错

---

## 32. Not all elementary functions can be expressed with exp-minus-log

**原文标题**: Not all elementary functions can be expressed with exp-minus-log

**原文链接**: [https://www.stylewarning.com/posts/not-all-elementary/](https://www.stylewarning.com/posts/not-all-elementary/)

生成摘要时出错

---

## 33. A communist Apple II and fourteen years of not knowing what you're testing

**原文标题**: A communist Apple II and fourteen years of not knowing what you're testing

**原文链接**: [https://llama.gs/blog/index.php/2026/04/10/friday-archaeology-a-communist-apple-ii-and-fourteen-years-of-not-knowing-what-youre-testing/](https://llama.gs/blog/index.php/2026/04/10/friday-archaeology-a-communist-apple-ii-and-fourteen-years-of-not-knowing-what-youre-testing/)

生成摘要时出错

---

## 34. New Modern Greek

**原文标题**: New Modern Greek

**原文链接**: [https://redas.dev/NewModernGreek/](https://redas.dev/NewModernGreek/)

生成摘要时出错

---

## 35. My adventure in designing API keys

**原文标题**: My adventure in designing API keys

**原文链接**: [https://vjay15.github.io/blog/apikeys/](https://vjay15.github.io/blog/apikeys/)

生成摘要时出错

---

## 36. Picasso’s Guernica (Gigapixel)

**原文标题**: Picasso’s Guernica (Gigapixel)

**原文链接**: [https://guernica.museoreinasofia.es/gigapixel/#3/63.11/-120.59](https://guernica.museoreinasofia.es/gigapixel/#3/63.11/-120.59)

生成摘要时出错

---

## 37. Stop Flock

**原文标题**: Stop Flock

**原文链接**: [https://stopflock.com](https://stopflock.com)

生成摘要时出错

---

## 38. Installing OpenBSD on the Pomera DM250 Writerdeck

**原文标题**: Installing OpenBSD on the Pomera DM250 Writerdeck

**原文链接**: [https://jcs.org/2026/04/09/openbsd-dm250](https://jcs.org/2026/04/09/openbsd-dm250)

生成摘要时出错

---

## 39. US v. Heppner (S.D.N.Y. 2026) no attorney-client privilege for AI chats [pdf]

**原文标题**: US v. Heppner (S.D.N.Y. 2026) no attorney-client privilege for AI chats [pdf]

**原文链接**: [https://fingfx.thomsonreuters.com/gfx/legaldocs/xmvjyjekkpr/Rakoff%20-%20order%20-%20AI.pdf](https://fingfx.thomsonreuters.com/gfx/legaldocs/xmvjyjekkpr/Rakoff%20-%20order%20-%20AI.pdf)

生成摘要时出错

---

## 40. Direct Win32 API, Weird-Shaped Windows, and Why They Mostly Disappeared

**原文标题**: Direct Win32 API, Weird-Shaped Windows, and Why They Mostly Disappeared

**原文链接**: [https://warped3.substack.com/p/direct-win32-api-weird-shaped-windows](https://warped3.substack.com/p/direct-win32-api-weird-shaped-windows)

生成摘要时出错

---

## 41. Claude Code Routines

**原文标题**: Claude Code Routines

**原文链接**: [https://code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines)

生成摘要时出错

---

## 42. The next evolution of the Agents SDK

**原文标题**: The next evolution of the Agents SDK

**原文链接**: [https://openai.com/index/the-next-evolution-of-the-agents-sdk/](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)

生成摘要时出错

---

## 43. 5NF and Database Design

**原文标题**: 5NF and Database Design

**原文链接**: [https://kb.databasedesignbook.com/posts/5nf/](https://kb.databasedesignbook.com/posts/5nf/)

生成摘要时出错

---

## 44. Turn your best AI prompts into one-click tools in Chrome

**原文标题**: Turn your best AI prompts into one-click tools in Chrome

**原文链接**: [https://blog.google/products-and-platforms/products/chrome/skills-in-chrome/](https://blog.google/products-and-platforms/products/chrome/skills-in-chrome/)

生成摘要时出错

---

## 45. My AI-Assisted Workflow

**原文标题**: My AI-Assisted Workflow

**原文链接**: [https://www.maiobarbero.dev/articles/ai-assisted-workflow/](https://www.maiobarbero.dev/articles/ai-assisted-workflow/)

生成摘要时出错

---

## 46. Rare concert recordings are landing on the Internet Archive

**原文标题**: Rare concert recordings are landing on the Internet Archive

**原文链接**: [https://techcrunch.com/2026/04/13/thousands-of-rare-concert-recordings-are-landing-on-the-internet-archive-listen-now/](https://techcrunch.com/2026/04/13/thousands-of-rare-concert-recordings-are-landing-on-the-internet-archive-listen-now/)

生成摘要时出错

---

## 47. What Is in Road Flares?

**原文标题**: What Is in Road Flares?

**原文链接**: [https://www.spiegl.org/rocket/flare/flare.html](https://www.spiegl.org/rocket/flare/flare.html)

生成摘要时出错

---

## 48. Let's talk space toilets

**原文标题**: Let's talk space toilets

**原文链接**: [https://mceglowski.substack.com/p/lets-talk-space-toilets](https://mceglowski.substack.com/p/lets-talk-space-toilets)

生成摘要时出错

---

## 49. Guide.world: A compendium of travel guides

**原文标题**: Guide.world: A compendium of travel guides

**原文链接**: [https://guide.world/](https://guide.world/)

生成摘要时出错

---

## 50. Allbirds announces pivot from shoes to AI, stock explodes 175%

**原文标题**: Allbirds announces pivot from shoes to AI, stock explodes 175%

**原文链接**: [https://www.cnbc.com/2026/04/15/allbirds-bird-stock-shoes-ai.html](https://www.cnbc.com/2026/04/15/allbirds-bird-stock-shoes-ai.html)

生成摘要时出错

---

## 51. The dangers of California's legislation to censor 3D printing

**原文标题**: The dangers of California's legislation to censor 3D printing

**原文链接**: [https://www.eff.org/deeplinks/2026/04/dangers-californias-legislation-censor-3d-printing](https://www.eff.org/deeplinks/2026/04/dangers-californias-legislation-censor-3d-printing)

生成摘要时出错

---

## 52. Allbirds shares soar 600% as it pivots from footwear to AI

**原文标题**: Allbirds shares soar 600% as it pivots from footwear to AI

**原文链接**: [https://www.cnn.com/2026/04/15/investing/allbirds-pivot-to-ai](https://www.cnn.com/2026/04/15/investing/allbirds-pivot-to-ai)

生成摘要时出错

---

## 53. Sam Vimes 'Boots' Theory of Socio-Economic Unfairness

**原文标题**: Sam Vimes 'Boots' Theory of Socio-Economic Unfairness

**原文链接**: [https://terrypratchett.com/explore-discworld/sam-vimes-boots-theory-of-socio-economic-unfairness/](https://terrypratchett.com/explore-discworld/sam-vimes-boots-theory-of-socio-economic-unfairness/)

生成摘要时出错

---

## 54. Amazon to acquire Globalstar and expand Amazon Leo satellite network

**原文标题**: Amazon to acquire Globalstar and expand Amazon Leo satellite network

**原文链接**: [https://www.businesswire.com/news/home/20260414237496/en/Amazon-to-Acquire-Globalstar-and-Expand-Amazon-Leo-Satellite-Network](https://www.businesswire.com/news/home/20260414237496/en/Amazon-to-Acquire-Globalstar-and-Expand-Amazon-Leo-Satellite-Network)

生成摘要时出错

---

## 55. The Orange Pi 6 Plus

**原文标题**: The Orange Pi 6 Plus

**原文链接**: [https://taoofmac.com/space/reviews/2026/04/11/1900](https://taoofmac.com/space/reviews/2026/04/11/1900)

生成摘要时出错

---

## 56. DaVinci Resolve – Photo

**原文标题**: DaVinci Resolve – Photo

**原文链接**: [https://www.blackmagicdesign.com/products/davinciresolve/photo](https://www.blackmagicdesign.com/products/davinciresolve/photo)

生成摘要时出错

---

## 57. A new spam policy for “back button hijacking”

**原文标题**: A new spam policy for “back button hijacking”

**原文链接**: [https://developers.google.com/search/blog/2026/04/back-button-hijacking](https://developers.google.com/search/blog/2026/04/back-button-hijacking)

生成摘要时出错

---

## 58. What Claude Code's Source Revealed About AI Engineering Culture

**原文标题**: What Claude Code's Source Revealed About AI Engineering Culture

**原文链接**: [https://techtrenches.dev/p/the-snake-that-ate-itself-what-claude](https://techtrenches.dev/p/the-snake-that-ate-itself-what-claude)

生成摘要时出错

---

## 59. Understanding Clojure's Persistent Vectors, pt. 1 (2013)

**原文标题**: Understanding Clojure's Persistent Vectors, pt. 1 (2013)

**原文链接**: [https://hypirion.com/musings/understanding-persistent-vector-pt-1](https://hypirion.com/musings/understanding-persistent-vector-pt-1)

生成摘要时出错

---

## 60. Someone bought 30 WordPress plugins and planted a backdoor in all of them

**原文标题**: Someone bought 30 WordPress plugins and planted a backdoor in all of them

**原文链接**: [https://anchor.host/someone-bought-30-wordpress-plugins-and-planted-a-backdoor-in-all-of-them/](https://anchor.host/someone-bought-30-wordpress-plugins-and-planted-a-backdoor-in-all-of-them/)

生成摘要时出错

---

## 61. 'Seeking connection': video game where players stopped shooting, started talking

**原文标题**: 'Seeking connection': video game where players stopped shooting, started talking

**原文链接**: [https://www.theguardian.com/games/2026/apr/15/arc-raiders-players-stopped-shooting-started-talking](https://www.theguardian.com/games/2026/apr/15/arc-raiders-players-stopped-shooting-started-talking)

生成摘要时出错

---

## 62. I wrote to Flock's privacy contact to opt out of their domestic spying program

**原文标题**: I wrote to Flock's privacy contact to opt out of their domestic spying program

**原文链接**: [https://honeypot.net/2026/04/14/i-wrote-to-flocks-privacy.html](https://honeypot.net/2026/04/14/i-wrote-to-flocks-privacy.html)

生成摘要时出错

---

## 63. PCBWay sponsorship: full-size SD module for Arduino projects

**原文标题**: PCBWay sponsorship: full-size SD module for Arduino projects

**原文链接**: [https://www.colino.net/wordpress/archives/2026/04/10/pcbway-sponsorship-full-size-sd-module-for-arduino-projects/](https://www.colino.net/wordpress/archives/2026/04/10/pcbway-sponsorship-full-size-sd-module-for-arduino-projects/)

生成摘要时出错

---

## 64. Show HN: Pseudonymizing sensitive data for LLMs without losing context

**原文标题**: Show HN: Pseudonymizing sensitive data for LLMs without losing context

**原文链接**: [https://atticsecurity.com/en/blog/why-llms-hate-fake-data-token-proxy/](https://atticsecurity.com/en/blog/why-llms-hate-fake-data-token-proxy/)

生成摘要时出错

---

## 65. Troubleshooting Email Delivery to Microsoft Users

**原文标题**: Troubleshooting Email Delivery to Microsoft Users

**原文链接**: [https://rozumem.xyz/posts/14](https://rozumem.xyz/posts/14)

生成摘要时出错

---

## 66. Distributed DuckDB Instance

**原文标题**: Distributed DuckDB Instance

**原文链接**: [https://github.com/citguru/openduck](https://github.com/citguru/openduck)

生成摘要时出错

---

## 67. AI disease-prediction models were trained on dubious data

**原文标题**: AI disease-prediction models were trained on dubious data

**原文链接**: [https://www.nature.com/articles/d41586-026-00697-4](https://www.nature.com/articles/d41586-026-00697-4)

生成摘要时出错

---

## 68. The M×N problem of tool calling and open-source models

**原文标题**: The M×N problem of tool calling and open-source models

**原文链接**: [https://www.thetypicalset.com/blog/grammar-parser-maintenance-contract](https://www.thetypicalset.com/blog/grammar-parser-maintenance-contract)

生成摘要时出错

---

## 69. OpenSSL 4.0.0

**原文标题**: OpenSSL 4.0.0

**原文链接**: [https://github.com/openssl/openssl/releases/tag/openssl-4.0.0](https://github.com/openssl/openssl/releases/tag/openssl-4.0.0)

生成摘要时出错

---

## 70. US national level OS-level age verification bill proposed

**原文标题**: US national level OS-level age verification bill proposed

**原文链接**: [https://www.congress.gov/bill/119th-congress/house-bill/8250/all-info](https://www.congress.gov/bill/119th-congress/house-bill/8250/all-info)

生成摘要时出错

---

## 71. Seed: Adding `vau` with an immutable dynamic environment to Chez Scheme

**原文标题**: Seed: Adding `vau` with an immutable dynamic environment to Chez Scheme

**原文链接**: [https://github.com/amirouche/seed](https://github.com/amirouche/seed)

生成摘要时出错

---

## 72. GitHub Stacked PRs

**原文标题**: GitHub Stacked PRs

**原文链接**: [https://github.github.com/gh-stack/](https://github.github.com/gh-stack/)

生成摘要时出错

---

## 73. Show HN: LangAlpha – what if Claude Code was built for Wall Street?

**原文标题**: Show HN: LangAlpha – what if Claude Code was built for Wall Street?

**原文链接**: [https://github.com/ginlix-ai/langalpha](https://github.com/ginlix-ai/langalpha)

生成摘要时出错

---

## 74. Show HN: Plain – The full-stack Python framework designed for humans and agents

**原文标题**: Show HN: Plain – The full-stack Python framework designed for humans and agents

**原文链接**: [https://github.com/dropseed/plain](https://github.com/dropseed/plain)

生成摘要时出错

---

## 75. Why Is France Moving from Microsoft Windows to Linux

**原文标题**: Why Is France Moving from Microsoft Windows to Linux

**原文链接**: [https://qazinform.com/news/why-is-france-moving-from-microsoft-windows-to-linux-8887c4](https://qazinform.com/news/why-is-france-moving-from-microsoft-windows-to-linux-8887c4)

生成摘要时出错

---

## 76. Your codebase doesn't care how it got written

**原文标题**: Your codebase doesn't care how it got written

**原文链接**: [https://robbyonrails.com/articles/2026/04/14/your-codebase-doesnt-care-how-it-got-written/](https://robbyonrails.com/articles/2026/04/14/your-codebase-doesnt-care-how-it-got-written/)

生成摘要时出错

---

## 77. MCP as Observability Interface: Connecting AI Agents to Kernel Tracepoints

**原文标题**: MCP as Observability Interface: Connecting AI Agents to Kernel Tracepoints

**原文链接**: [https://ingero.io/mcp-observability-interface-ai-agents-kernel-tracepoints/](https://ingero.io/mcp-observability-interface-ai-agents-kernel-tracepoints/)

生成摘要时出错

---

## 78. Multi-Agentic Software Development Is a Distributed Systems Problem

**原文标题**: Multi-Agentic Software Development Is a Distributed Systems Problem

**原文链接**: [https://kirancodes.me/posts/log-distributed-llms.html](https://kirancodes.me/posts/log-distributed-llms.html)

生成摘要时出错

---

## 79. I just want simple S3

**原文标题**: I just want simple S3

**原文链接**: [https://blog.feld.me/posts/2026/04/i-just-want-simple-s3/](https://blog.feld.me/posts/2026/04/i-just-want-simple-s3/)

生成摘要时出错

---

## 80. Allbirds abandons clothes, pivots to "AI compute infrastructure"

**原文标题**: Allbirds abandons clothes, pivots to "AI compute infrastructure"

**原文链接**: [https://arstechnica.com/ai/2026/04/bubble-watch-fashion-brand-allbirds-pivots-hard-to-become-ai-services-company/](https://arstechnica.com/ai/2026/04/bubble-watch-fashion-brand-allbirds-pivots-hard-to-become-ai-services-company/)

生成摘要时出错

---

## 81. Don't feel like exercising? Maybe it's the wrong time of day for you

**原文标题**: Don't feel like exercising? Maybe it's the wrong time of day for you

**原文链接**: [https://www.bbc.com/news/articles/cd6lzpxwx50o](https://www.bbc.com/news/articles/cd6lzpxwx50o)

生成摘要时出错

---

## 82. Game: Print Gallery Of An Artist, A brief exploration of recursive spaces

**原文标题**: Game: Print Gallery Of An Artist, A brief exploration of recursive spaces

**原文链接**: [https://managore.itch.io/print-gallery-of-an-artist](https://managore.itch.io/print-gallery-of-an-artist)

生成摘要时出错

---

## 83. Fuck the cloud (2009)

**原文标题**: Fuck the cloud (2009)

**原文链接**: [https://ascii.textfiles.com/archives/1717](https://ascii.textfiles.com/archives/1717)

生成摘要时出错

---

## 84. Claude may require identity verification in some cases

**原文标题**: Claude may require identity verification in some cases

**原文链接**: [https://support.claude.com/en/articles/14328960-identity-verification-on-claude](https://support.claude.com/en/articles/14328960-identity-verification-on-claude)

生成摘要时出错

---

## 85. Nucleus Nouns

**原文标题**: Nucleus Nouns

**原文链接**: [https://ben-mini.com/2026/nucleus-nouns](https://ben-mini.com/2026/nucleus-nouns)

生成摘要时出错

---

## 86. Carol's Causal Conundrum: a zine intro to causally ordered message delivery

**原文标题**: Carol's Causal Conundrum: a zine intro to causally ordered message delivery

**原文链接**: [https://decomposition.al/zines/](https://decomposition.al/zines/)

生成摘要时出错

---

## 87. Hazardous States and Accidents

**原文标题**: Hazardous States and Accidents

**原文链接**: [https://entropicthoughts.com/hazardous-states-and-accidents](https://entropicthoughts.com/hazardous-states-and-accidents)

生成摘要时出错

---

## 88. Backblaze has stopped backing up OneDrive and Dropbox folders and maybe others

**原文标题**: Backblaze has stopped backing up OneDrive and Dropbox folders and maybe others

**原文链接**: [https://rareese.com/posts/backblaze/](https://rareese.com/posts/backblaze/)

生成摘要时出错

---

## 89. Trusted access for the next era of cyber defense

**原文标题**: Trusted access for the next era of cyber defense

**原文链接**: [https://openai.com/index/scaling-trusted-access-for-cyber-defense/](https://openai.com/index/scaling-trusted-access-for-cyber-defense/)

生成摘要时出错

---

## 90. Academic fraud may be the symptom of a more systemic problem

**原文标题**: Academic fraud may be the symptom of a more systemic problem

**原文链接**: [https://www.voxweb.nl/en/academic-fraud-may-be-the-symptom-of-a-much-more-systemic-problem](https://www.voxweb.nl/en/academic-fraud-may-be-the-symptom-of-a-much-more-systemic-problem)

生成摘要时出错

---

## 91. Design and implementation of DuckDB internals

**原文标题**: Design and implementation of DuckDB internals

**原文链接**: [https://duckdb.org/library/design-and-implementation-of-duckdb-internals/](https://duckdb.org/library/design-and-implementation-of-duckdb-internals/)

生成摘要时出错

---

## 92. A soft robot has no problem moving with no motor and no gears

**原文标题**: A soft robot has no problem moving with no motor and no gears

**原文链接**: [https://engineering.princeton.edu/news/2026/04/08/soft-robot-has-no-problem-moving-no-motor-and-no-gears](https://engineering.princeton.edu/news/2026/04/08/soft-robot-has-no-problem-moving-no-motor-and-no-gears)

生成摘要时出错

---

## 93. Founders Need to Be Ruthless When Chasing Deals

**原文标题**: Founders Need to Be Ruthless When Chasing Deals

**原文链接**: [https://steveblank.com/2024/04/16/founders-need-to-be-ruthless-when-chasing-deals/](https://steveblank.com/2024/04/16/founders-need-to-be-ruthless-when-chasing-deals/)

生成摘要时出错

---

## 94. Keep Android Open

**原文标题**: Keep Android Open

**原文链接**: [https://keepandroidopen.org/cta/](https://keepandroidopen.org/cta/)

生成摘要时出错

---

## 95. Cal.com is closing its core codebase, citing AI security risks

**原文标题**: Cal.com is closing its core codebase, citing AI security risks

**原文链接**: [https://twitter.com/pumfleet/status/2044406553508274554](https://twitter.com/pumfleet/status/2044406553508274554)

生成摘要时出错

---

## 96. US states can't account for datacenter tax breaks

**原文标题**: US states can't account for datacenter tax breaks

**原文链接**: [https://www.theregister.com/2026/04/15/us_states_gaap_datacenters/](https://www.theregister.com/2026/04/15/us_states_gaap_datacenters/)

生成摘要时出错

---

## 97. Write less code, be more responsible

**原文标题**: Write less code, be more responsible

**原文链接**: [https://blog.orhun.dev/code-responsibly/](https://blog.orhun.dev/code-responsibly/)

生成摘要时出错

---

## 98. Lean proved this program correct; then I found a bug

**原文标题**: Lean proved this program correct; then I found a bug

**原文链接**: [https://kirancodes.me/posts/log-who-watches-the-watchers.html](https://kirancodes.me/posts/log-who-watches-the-watchers.html)

生成摘要时出错

---

## 99. On hacker mindset

**原文标题**: On hacker mindset

**原文链接**: [https://www.henrikkarlsson.xyz/p/hacker-mindset](https://www.henrikkarlsson.xyz/p/hacker-mindset)

生成摘要时出错

---

## 100. New bill would let New Yorkers hang solar panels from windows

**原文标题**: New bill would let New Yorkers hang solar panels from windows

**原文链接**: [https://gothamist.com/news/here-comes-the-sun-new-bill-would-let-new-yorkers-hang-solar-panels-from-windows](https://gothamist.com/news/here-comes-the-sun-new-bill-would-let-new-yorkers-hang-solar-panels-from-windows)

生成摘要时出错

---

