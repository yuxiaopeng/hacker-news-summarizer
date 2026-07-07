# Hacker News 热门文章摘要 (2026-07-07)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. OpenSSH 10.4/10.4p1 Released

**原文标题**: OpenSSH 10.4/10.4p1 Released

**原文链接**: [https://www.openssh.org/txt/release-10.4](https://www.openssh.org/txt/release-10.4)

生成摘要时出错

---

## 2. 墨田

**原文标题**: Inkfield

**原文链接**: [https://www.inkfield.studio](https://www.inkfield.studio)

所提供的内容仅包含“**inkfield**”这个单词。假设您指的是同名的独立视频游戏和艺术项目，以下是简要概述：

**Inkfield** 是一项极具氛围感的独立解谜冒险项目，以其鲜明且极简的视觉辨识度为特色。该体验的核心是一个超现实的手绘世界，利用强烈的黑白“纸墨”美学，营造出一种神秘与孤寂感。

核心要点包括：
*   **美术方向**：该项目以其独特的高对比度艺术风格著称，这是其叙事的主要载体。
*   **游戏玩法**：通常结合了探索与环境解谜，要求玩家在梦幻般的景观中穿行。
*   **氛围营造**：叙事基本不使用言语，而是依靠视觉线索和情绪基调，让玩家沉浸在其阴郁且具实验性的环境之中。

如果您原本打算提供全文进行摘要但未能正确粘贴，请提供相关文本，我很乐意为您重新进行总结。

---

## 3. Show HN: Context Warp Drive —— 面向 AI 智能体的确定性上下文折叠

**原文标题**: Show HN: Context Warp Drive – Deterministic context folding for AI agents

**原文链接**: [https://github.com/dogtorjonah/context-warp-drive](https://github.com/dogtorjonah/context-warp-drive)

**Context Warp Drive (CWD)** 是一种确定性上下文折叠引擎，旨在管理长周期 AI 智能体记忆，且无需承担传统摘要或截断方式的弊端。虽然基于 LLM 的摘要等标准方法成本高昂、具有非确定性且会破坏提供商的提示词缓存，但 CWD 利用纯 CPU 逻辑将历史记录“折叠”为紧凑的结构化骨架。

**核心特性与优势：**
*   **确定性压缩：** 无需额外的 LLM 调用即可折叠上下文，确保相同的输入产生字节级一致的输出。这能保持提供商提示词缓存的“热度”，据报告缓存命中率约为 90%。
*   **经济高效：** 在生产负载中（特别是使用 Claude 时），通过利用提供商的缓存折扣（0.30 美元/百万 Token 对比 3.00 美元/百万 Token），CWD 相比 LLM 摘要可降低约 70% 的成本，相比截断方式可降低约 60%。
*   **高事实保留率：** 它使用“坐标库 (Coordinate Closet)”来保留摘要过程中经常丢失的精确标识符（如 UUID、SHA、路径和端口），其保留率显著高于滑动窗口模式。
*   **跨提供商支持：** 该引擎支持 Anthropic、OpenAI 和 Gemini，并提供特定助手来管理不同的缓存机制（例如 Anthropic 的 `cache_control`）。
*   **可扩展性：** 当 Token 压力达到上限时，CWD 会执行“硬纪元重塑 (hard-epoch rebirth)”，将可见历史折叠为紧凑的种子，同时保留原始转录内容以供召回。

**组件：**
*   **FoldSession：** 为模型准备消息历史记录的核心管理器。
*   **Budget Resolver：** 根据所用模型的特定上下文窗口自动调整折叠阈值。
*   **Task Rail：** 一个便携式状态机，用于跟踪智能体计划和执行步骤，确保它们在上下文折叠或系统重启后依然存在。

Context Warp Drive 目前以 TypeScript 软件包的形式在 GitHub 上提供，适用于构建需要高频对话、低延迟和可预测成本的生产级多智能体系统的开发人员。

---

## 4. Anthropic 在移动端和网页端推出 Claude Cowork

**原文标题**: Anthropic is launching Claude Cowork on mobile and web

**原文链接**: [https://www.theverge.com/ai-artificial-intelligence/961978/anthropic-claude-cowork-mobile-web](https://www.theverge.com/ai-artificial-intelligence/961978/anthropic-claude-cowork-mobile-web)

Anthropic 宣布其 Claude Cowork AI 平台正从原有的桌面应用程序扩展至 iOS、Android 及网页端。该更新将于本周二开始面向 Claude Max 订阅用户推出，其他方案的用户预计将在未来几周内获得访问权限。

此次更新的一个重要特性是默认转向云端处理。这使得 Claude Cowork 即使在用户笔记本电脑关闭或设备离线的情况下，仍能继续在后台运行任务。预定任务现在将独立执行，当任务准备好供审查或批准时，平台会向用户发送移动端通知。

虽然移动版和网页版提供了更高的灵活性和跨设备延续性，但 Anthropic 指出，“完整体验”——特别是本地文件访问功能——仍为 macOS 和 Windows 桌面应用专属。桌面用户可以根据需要，在云端处理和本地处理之间进行切换。

配合此次发布，Anthropic 还将其 Cowork 双倍使用额度的优惠活动延长至 2026 年 8 月 5 日。

---

## 5. 给马克·扎克伯格的剧本

**原文标题**: A Script for Mark Zuckerberg

**原文链接**: [https://stratechery.com/2026/a-script-for-mark-zuckerberg/](https://stratechery.com/2026/a-script-for-mark-zuckerberg/)

这份由 *Stratechery* 的 Ben Thompson 撰写的 2026 年模拟财报电话会议剧本，呈现了马克·扎克伯格针对 Meta 战略方向和 AI 投资的一次假设性“公开检讨”。

演讲的核心在于扎克伯格承认，他长期以来对成为“平台”所有者的执着——以推迟向原生移动应用转型以及对 Reality Labs 的巨额支出为代表——是一个错误。相反，剧本建议扎克伯格应当拥抱 Meta 的真实身份：一个广告和娱乐巨头。他承认，虽然过去低估了广告业务，但它实际上是公司最强大的优势，也是连接创作者与消费者的重要经济驱动力。

该演讲为 Meta 的巨额 AI 支出勾勒了三部分战略：
1.  **生存必然性**：AI 对所有数字公司都构成了存亡风险；Meta 必须保持领先才能生存。
2.  **广告与库存增长**：AI 增强了内容推荐和精准投放，通过实现“像素级变现”，创造了史上“最大的广告库存扩张”。
3.  **聚焦休闲**：Meta 不会在生产力工具上与 OpenAI 竞争，而是将 AI 重点放在社交、娱乐和购物上。

最后，剧本提出了一种新颖的财务模式：Meta 将短期出租其富余的算力基础设施。这不仅能产生收入以资助后续建设，还设立了一个“门槛收益率”，确保内部团队仅在项目盈利能力超过市场租赁价格时才使用算力。最终，该剧本构想了一个不再试图成为硬件平台，而是利用 AI 统治数字注意力与广告经济的 Meta。

---

## 6. Canada to buy 12 hi-tech German submarines after bidding war

**原文标题**: Canada to buy 12 hi-tech German submarines after bidding war

**原文链接**: [https://www.theguardian.com/world/2026/jul/06/canada-buys-12-tkms-german-norwegian-submarines-after-bidding-war](https://www.theguardian.com/world/2026/jul/06/canada-buys-12-tkms-german-norwegian-submarines-after-bidding-war)

Canada has selected the German consortium ThyssenKrupp Marine Systems (TKMS) to build 12 new HDW Class 212CD diesel-electric submarines. This multibillion-dollar contract—one of the largest in Canadian history—aims to replace the Royal Canadian Navy’s aging fleet of four secondhand Victoria-class vessels.

The decision followed a competitive bidding war with South Korea’s Hanwha Ocean. While Hanwha offered larger vessels and significant local investment, Canada ultimately chose the German-made 212CD model for its advanced stealth technology and its suitability for long-range Arctic surveillance. The deal also strengthens Canada’s ties with NATO, as TKMS is a primary supplier for the alliance's fleet.

The financial scope of the project is massive: the initial order is estimated at US$12 billion, but with roughly 50 years of maintenance included, the total cost could exceed US$70 billion. Negotiations to finalize the contract are expected to take several years.

Announced by Prime Minister Mark Carney, the deal reflects a broader shift in Canadian defense policy. The government has committed to increasing defense spending to 2% of GDP, with a future goal of 5% by 2035. Furthermore, the selection of a German firm over a U.S. or South Korean rival highlights Ottawa's strategic push to diversify its defense partnerships and reduce its reliance on the United States. This trend is further evidenced by Canada’s potential purchase of 72 Saab-made Gripen fighter jets from Sweden to complement its fleet of American F-35s.

---

## 7. GLM 5.2 and the coming AI margin collapse

**原文标题**: GLM 5.2 and the coming AI margin collapse

**原文链接**: [https://martinalderson.com/posts/the-upcoming-ai-margin-collapse-part-1-glm-5-2/](https://martinalderson.com/posts/the-upcoming-ai-margin-collapse-part-1-glm-5-2/)

生成摘要时出错

---

## 8. Learning to code is still worthwhile

**原文标题**: Learning to code is still worthwhile

**原文链接**: [https://stevekrouse.com/learn-to-code](https://stevekrouse.com/learn-to-code)

生成摘要时出错

---

## 9. How did we make DeepSeek outperform Opus

**原文标题**: How did we make DeepSeek outperform Opus

**原文链接**: [https://twitter.com/MrAhmadAwais/status/2050956678502420612](https://twitter.com/MrAhmadAwais/status/2050956678502420612)

生成摘要时出错

---

## 10. Januscape: Guest-to-Host Escape in KVM/x86 [CVE-2026-53359]

**原文标题**: Januscape: Guest-to-Host Escape in KVM/x86 [CVE-2026-53359]

**原文链接**: [https://github.com/V4bel/Januscape](https://github.com/V4bel/Januscape)

生成摘要时出错

---

## 11. A verification loop 4x'd DeepSeek's intelligence, matching Opus at 1/7 the cost

**原文标题**: A verification loop 4x'd DeepSeek's intelligence, matching Opus at 1/7 the cost

**原文链接**: [https://ironbee.medium.com/what-a-verification-loop-adds-to-a-coding-agent-a-first-look-5049017e636e](https://ironbee.medium.com/what-a-verification-loop-adds-to-a-coding-agent-a-first-look-5049017e636e)

生成摘要时出错

---

## 12. The Making of Claude Code

**原文标题**: The Making of Claude Code

**原文链接**: [https://www.anthropic.com/features/making-of-claude-code](https://www.anthropic.com/features/making-of-claude-code)

生成摘要时出错

---

## 13. Kani: A Model Checker for Rust

**原文标题**: Kani: A Model Checker for Rust

**原文链接**: [https://arxiv.org/abs/2607.01504](https://arxiv.org/abs/2607.01504)

生成摘要时出错

---

## 14. Rotman Lens

**原文标题**: Rotman Lens

**原文链接**: [https://en.wikipedia.org/wiki/Rotman_lens](https://en.wikipedia.org/wiki/Rotman_lens)

生成摘要时出错

---

## 15. Clojure 1.13 adds support for checked keys

**原文标题**: Clojure 1.13 adds support for checked keys

**原文链接**: [https://clojure.org/news/2026/07/02/clojure-1-13-alpha1](https://clojure.org/news/2026/07/02/clojure-1-13-alpha1)

生成摘要时出错

---

## 16. Ternlight – 7 MB embedding model that runs in browser (WASM)

**原文标题**: Ternlight – 7 MB embedding model that runs in browser (WASM)

**原文链接**: [https://ternlight-demo.vercel.app/](https://ternlight-demo.vercel.app/)

生成摘要时出错

---

## 17. A global workspace in language models

**原文标题**: A global workspace in language models

**原文链接**: [https://www.anthropic.com/research/global-workspace](https://www.anthropic.com/research/global-workspace)

生成摘要时出错

---

## 18. Introduction to Genomics for Engineers

**原文标题**: Introduction to Genomics for Engineers

**原文链接**: [https://learngenomics.dev/docs/biological-foundations/cells-genomes-dna-chromosomes/](https://learngenomics.dev/docs/biological-foundations/cells-genomes-dna-chromosomes/)

生成摘要时出错

---

## 19. Resetting Xbox

**原文标题**: Resetting Xbox

**原文链接**: [https://news.xbox.com/en-us/2026/07/06/resetting-xbox/](https://news.xbox.com/en-us/2026/07/06/resetting-xbox/)

生成摘要时出错

---

## 20. Fable turned reMarkable into Tom Riddle's diary from Harry Potter

**原文标题**: Fable turned reMarkable into Tom Riddle's diary from Harry Potter

**原文链接**: [https://github.com/MaximeRivest/Riddle](https://github.com/MaximeRivest/Riddle)

生成摘要时出错

---

## 21. Almost all coders at Id Software have been fired, following Xbox reset

**原文标题**: Almost all coders at Id Software have been fired, following Xbox reset

**原文链接**: [https://xcancel.com/ScottApogee/status/2074198967550685268#m](https://xcancel.com/ScottApogee/status/2074198967550685268#m)

生成摘要时出错

---

## 22. Automated Moderation Is Here to Stay

**原文标题**: Automated Moderation Is Here to Stay

**原文链接**: [https://www.eff.org/deeplinks/2026/07/part-1-automated-moderation-here-stay](https://www.eff.org/deeplinks/2026/07/part-1-automated-moderation-here-stay)

生成摘要时出错

---

## 23. Emerging evidence links tire pollution to Alzheimer's risk

**原文标题**: Emerging evidence links tire pollution to Alzheimer's risk

**原文链接**: [https://www.eurekalert.org/news-releases/1134924](https://www.eurekalert.org/news-releases/1134924)

生成摘要时出错

---

## 24. Midtown Manhattan blocks evacuated after beams buckling at construction site

**原文标题**: Midtown Manhattan blocks evacuated after beams buckling at construction site

**原文链接**: [https://abcnews.com/US/midtown-manhattan-blocks-evacuated-after-beams-found-buckling/story?id=134549272](https://abcnews.com/US/midtown-manhattan-blocks-evacuated-after-beams-found-buckling/story?id=134549272)

生成摘要时出错

---

## 25. NSA and IETF: Fairness

**原文标题**: NSA and IETF: Fairness

**原文链接**: [https://blog.cr.yp.to/20260706-fairness.html](https://blog.cr.yp.to/20260706-fairness.html)

生成摘要时出错

---

## 26. Using precision editing to study human embryo development shows master gene

**原文标题**: Using precision editing to study human embryo development shows master gene

**原文链接**: [https://www.cam.ac.uk/research/news/first-use-of-precision-editing-to-study-human-embryo-development-reveals-role-of-master-gene](https://www.cam.ac.uk/research/news/first-use-of-precision-editing-to-study-human-embryo-development-reveals-role-of-master-gene)

生成摘要时出错

---

## 27. A 2048-spin bulk acoustic wave Ising machine for number partitioning and Sudoku

**原文标题**: A 2048-spin bulk acoustic wave Ising machine for number partitioning and Sudoku

**原文链接**: [https://arxiv.org/abs/2607.02112](https://arxiv.org/abs/2607.02112)

生成摘要时出错

---

## 28. Evaluation order and nontermination in query languages

**原文标题**: Evaluation order and nontermination in query languages

**原文链接**: [https://www.rntz.net/post/2026-06-11-datalog-nontermination.html](https://www.rntz.net/post/2026-06-11-datalog-nontermination.html)

生成摘要时出错

---

## 29. M/PC – A Concatenative OS

**原文标题**: M/PC – A Concatenative OS

**原文链接**: [https://wiki.xxiivv.com/site/m_pc.html](https://wiki.xxiivv.com/site/m_pc.html)

生成摘要时出错

---

## 30. AMD Ryzen AI Halo – $4k AI Dev Kit

**原文标题**: AMD Ryzen AI Halo – $4k AI Dev Kit

**原文链接**: [https://www.lttlabs.com/articles/2026/07/06/amd-ryzen-ai-halo](https://www.lttlabs.com/articles/2026/07/06/amd-ryzen-ai-halo)

生成摘要时出错

---

## 31. Pruning RAG context down to what the answer actually needs

**原文标题**: Pruning RAG context down to what the answer actually needs

**原文链接**: [https://www.kapa.ai/blog/how-we-prune-rag-context](https://www.kapa.ai/blog/how-we-prune-rag-context)

生成摘要时出错

---

## 32. EndBASIC 0.14: Are we multimedia yet?

**原文标题**: EndBASIC 0.14: Are we multimedia yet?

**原文链接**: [https://www.endbasic.dev/2026/07/endbasic-0.14.html](https://www.endbasic.dev/2026/07/endbasic-0.14.html)

生成摘要时出错

---

## 33. The LLVM Compiler Infrastructure

**原文标题**: The LLVM Compiler Infrastructure

**原文链接**: [https://cacm.acm.org/federal-funding-of-academic-research/the-llvm-compiler-infrastructure/](https://cacm.acm.org/federal-funding-of-academic-research/the-llvm-compiler-infrastructure/)

生成摘要时出错

---

## 34. Linux on the Atari Jaguar

**原文标题**: Linux on the Atari Jaguar

**原文链接**: [https://cakehonolulu.github.io/linux-for-jaguar/](https://cakehonolulu.github.io/linux-for-jaguar/)

生成摘要时出错

---

## 35. Full Writeup of the Windows GDID

**原文标题**: Full Writeup of the Windows GDID

**原文链接**: [https://github.com/SmtimesIWndr/gdid-reversal](https://github.com/SmtimesIWndr/gdid-reversal)

生成摘要时出错

---

## 36. A System of Systems for the Selection of Optimal Climate Change Decisions

**原文标题**: A System of Systems for the Selection of Optimal Climate Change Decisions

**原文链接**: [https://ieeexplore.ieee.org/document/11357917](https://ieeexplore.ieee.org/document/11357917)

生成摘要时出错

---

## 37. Claude Cowork is coming to mobile and web

**原文标题**: Claude Cowork is coming to mobile and web

**原文链接**: [https://claude.com/blog/cowork-web-mobile](https://claude.com/blog/cowork-web-mobile)

生成摘要时出错

---

## 38. Show HN: Pulpie – Models for Cleaning the Web

**原文标题**: Show HN: Pulpie – Models for Cleaning the Web

**原文链接**: [https://usefeyn.com/blog/pulpie-pareto-optimal-models-for-cleaning-the-web/](https://usefeyn.com/blog/pulpie-pareto-optimal-models-for-cleaning-the-web/)

生成摘要时出错

---

## 39. Reinforcement Learning with Metacognitive Feedback Elicits Uncertainty in LLMs

**原文标题**: Reinforcement Learning with Metacognitive Feedback Elicits Uncertainty in LLMs

**原文链接**: [https://arxiv.org/abs/2606.32032](https://arxiv.org/abs/2606.32032)

生成摘要时出错

---

## 40. Not Dark Yet

**原文标题**: Not Dark Yet

**原文链接**: [https://agoodhardstare.substack.com/p/not-dark-yet](https://agoodhardstare.substack.com/p/not-dark-yet)

生成摘要时出错

---

## 41. Does code cleanliness affect coding agents? A controlled minimal-pair study

**原文标题**: Does code cleanliness affect coding agents? A controlled minimal-pair study

**原文链接**: [https://arxiv.org/abs/2605.20049](https://arxiv.org/abs/2605.20049)

生成摘要时出错

---

## 42. Organic Maps

**原文标题**: Organic Maps

**原文链接**: [https://organicmaps.app/](https://organicmaps.app/)

生成摘要时出错

---

## 43. A new study just debunked the biggest fear about AI and open source

**原文标题**: A new study just debunked the biggest fear about AI and open source

**原文链接**: [https://thenewstack.io/ai-open-source-newcomers-study/](https://thenewstack.io/ai-open-source-newcomers-study/)

生成摘要时出错

---

## 44. As Amazon lets Mechanical Turk fade, Mercor hits a $2B gross run rate

**原文标题**: As Amazon lets Mechanical Turk fade, Mercor hits a $2B gross run rate

**原文链接**: [https://runtimewire.com/article/as-amazon-lets-mechanical-turk-fade-mercor-hits-a-2-billion-gross-run-rate](https://runtimewire.com/article/as-amazon-lets-mechanical-turk-fade-mercor-hits-a-2-billion-gross-run-rate)

生成摘要时出错

---

## 45. OfficeCLI: Office suite for AI agents to read and edit Microsoft Office files

**原文标题**: OfficeCLI: Office suite for AI agents to read and edit Microsoft Office files

**原文链接**: [https://github.com/iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI)

生成摘要时出错

---

## 46. Egypt Is Building a New Nile

**原文标题**: Egypt Is Building a New Nile

**原文链接**: [https://www.theb1m.com/video/egypt-is-building-a-new-nile](https://www.theb1m.com/video/egypt-is-building-a-new-nile)

生成摘要时出错

---

## 47. Aluminum foil (2021)

**原文标题**: Aluminum foil (2021)

**原文链接**: [https://dernocua.github.io/notes/aluminum-foil.html](https://dernocua.github.io/notes/aluminum-foil.html)

生成摘要时出错

---

## 48. Real-time map of Great Britain's rail network

**原文标题**: Real-time map of Great Britain's rail network

**原文链接**: [https://www.map.signalbox.io](https://www.map.signalbox.io)

生成摘要时出错

---

## 49. 1k Words: A Writing Contest

**原文标题**: 1k Words: A Writing Contest

**原文链接**: [https://writingclub.world/1picture1000words](https://writingclub.world/1picture1000words)

生成摘要时出错

---

## 50. Poly/ML – A Standard ML Implementation

**原文标题**: Poly/ML – A Standard ML Implementation

**原文链接**: [https://github.com/polyml/polyml](https://github.com/polyml/polyml)

生成摘要时出错

---

## 51. Fable 5 On Vending-Bench: Misbehaving, With Plausible Deniability

**原文标题**: Fable 5 On Vending-Bench: Misbehaving, With Plausible Deniability

**原文链接**: [https://andonlabs.com/blog/fable5-vending-bench](https://andonlabs.com/blog/fable5-vending-bench)

生成摘要时出错

---

## 52. Top researchers leave USA for the Netherlands (in Dutch)

**原文标题**: Top researchers leave USA for the Netherlands (in Dutch)

**原文链接**: [https://www.nwo.nl/nieuws/eerste-internationale-wetenschappers-via-het-tulp-fonds-naar-nederland](https://www.nwo.nl/nieuws/eerste-internationale-wetenschappers-via-het-tulp-fonds-naar-nederland)

生成摘要时出错

---

## 53. Road to Elm 1.0

**原文标题**: Road to Elm 1.0

**原文链接**: [https://elm-lang.org/news/faster-builds](https://elm-lang.org/news/faster-builds)

生成摘要时出错

---

## 54. Companies hire more after AI adoption

**原文标题**: Companies hire more after AI adoption

**原文链接**: [https://ramp.com/data/heavy-ai-adopters-hire-more](https://ramp.com/data/heavy-ai-adopters-hire-more)

生成摘要时出错

---

## 55. Apricot Computers: An underrated British brand

**原文标题**: Apricot Computers: An underrated British brand

**原文链接**: [https://dfarq.homeip.net/apricot-computers-an-underrated-british-brand/](https://dfarq.homeip.net/apricot-computers-an-underrated-british-brand/)

生成摘要时出错

---

## 56. New virus catalog reveals which pathogens pose the greatest threat

**原文标题**: New virus catalog reveals which pathogens pose the greatest threat

**原文链接**: [https://theconversation.com/new-virus-catalogue-reveals-which-pathogens-pose-the-greatest-threat-283599](https://theconversation.com/new-virus-catalogue-reveals-which-pathogens-pose-the-greatest-threat-283599)

生成摘要时出错

---

## 57. Delta flight hit by firework while landing at Midway Airport on Fourth of July

**原文标题**: Delta flight hit by firework while landing at Midway Airport on Fourth of July

**原文链接**: [https://www.nbcchicago.com/news/local/delta-flight-hit-by-firework-while-landing-at-midway-airport-on-fourth-of-july/3957451/](https://www.nbcchicago.com/news/local/delta-flight-hit-by-firework-while-landing-at-midway-airport-on-fourth-of-july/3957451/)

生成摘要时出错

---

## 58. The Private Capture of Public Genius

**原文标题**: The Private Capture of Public Genius

**原文链接**: [https://www.wysr.xyz/p/the-private-capture-of-public-genius](https://www.wysr.xyz/p/the-private-capture-of-public-genius)

生成摘要时出错

---

## 59. Dr Richard Hipp still maintains 40% of the lines contributed to SQLite

**原文标题**: Dr Richard Hipp still maintains 40% of the lines contributed to SQLite

**原文链接**: [https://www.reddit.com/r/PrincipalAi/s/PbfYg15IAK](https://www.reddit.com/r/PrincipalAi/s/PbfYg15IAK)

生成摘要时出错

---

