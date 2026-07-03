# Hacker News 热门文章摘要 (2026-07-03)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Claude，请别再试图记那些乱七八糟的东西了。

**原文标题**: Claude, please stop trying to memorize random crap

**原文链接**: [https://12gramsofcarbon.com/p/agentics-memorizing-session-transcripts](https://12gramsofcarbon.com/p/agentics-memorizing-session-transcripts)

在《Claude，请停止记忆那些没用的废话》一文中，作者挑战了“存储并检索历史会话记录（基于会话的记忆）能提升 AI 编程智能体性能”的流行观点。尽管作者团队曾围绕“会话记录是新石油”这一理念构建产品，但他们发现这不仅没有带来性能提升，甚至还导致了模型退化。

文章强调了自动化会话记忆失败的几个原因：

1. **冗余与噪声**：有关意图和决策的有价值背景已提炼到 PR 消息、提交记录和文档等“编程产物”中。搜索原始记录会迫使智能体将 Token 浪费在“草稿纸”噪声和已被弃用的方案上，而这些方案的有效信息早已以更精炼的形式存在。
2. **缺乏“记忆修剪”**：智能体难以修剪或删除无关背景。由于模型被训练为将所有输入视为“事实”，它们无法区分经过人工审核的决策与历史会话中随机、未经审核的选择。这导致了“意图漂移”，使错误随时间累积。
3. **对齐约束**：当前模型如果假设输入数据是“错误”的，往往会受到惩罚。这使得智能体很难忽略“损坏”的记忆，或识别某次历史会话何时偏离了正确方向。

作者得出结论，智能体尚无法自主管理记忆。内部数据显示，当机器人根据公司活动建议更新记忆时，**80% 的建议在人工审核中被拒绝**。为了提高智能体的表现，作者建议应专注于高质量文档和“人工在环”验证，而非原始会话记录的索引。

---

## 2. Maxis 的前世今生 第一部：模拟万物

**原文标题**: The Life and Times of Maxis, Part 1: SimEverything

**原文链接**: [https://www.filfre.net/2026/07/the-life-and-times-of-maxis-part-1-simeverything/](https://www.filfre.net/2026/07/the-life-and-times-of-maxis-part-1-simeverything/)

本文探讨了 Maxis 软件公司的早期历史，以及其联合创始人威尔·赖特（Will Wright）对游戏行业的革命性影响。文章首先指出，“硬核”游戏历史与实际商业现实之间存在脱节，并注意到最成功的游戏——如《神秘岛》或《模拟城市》——通常吸引的是那些并不自诩为游戏玩家的主流受众。

1989 年推出的《模拟城市》摒弃了传统的“胜负”状态，转而采用“软件玩具”理念，从而成为一种文化现象。尽管赖特承认该游戏只是城市规划的“漫画式呈现”而非写实模拟，但其成就斐然。它确立了城市建设类游戏的地位，并引入了实时机制和“沙盒”模式，影响了包括席德·梅尔的《文明》在内的后世经典。

随后，文章详细阐述了赖特更宏大的“模拟一切”愿景——即各种模拟系统最终能互联成一个统一的游戏宇宙。在这一雄心的驱使下，1990 年《模拟地球》问世，将视角从城市规划转向了行星生态学。受当时关于全球变暖的公众讨论及詹姆斯·洛夫洛克“盖亚假说”的启发，《模拟地球》试图将地球建模为一个单一、互锁的有机体。赖特的作品受到了洛夫洛克本人“黛西世界”计算机模型的启发，该模型展示了生命与环境是如何相互作用的。

最终，本文将 Maxis 描绘为不仅是一家游戏开发商，更是一个先驱，它推动游戏媒介从小众幻想转向主流的、基于现实的模拟，永久地改变了现代游戏设计的基因。

---

## 3. 半成品

**原文标题**: Half-Baked Product

**原文链接**: [https://weli.dev/blog/half-baked-product/](https://weli.dev/blog/half-baked-product/)

在《半成品》（Half-Baked Product）一文中，作者探讨了产品开发中常见的陷阱，特别是区分了真正的“最小可行性产品”（MVP）与所谓的“半成品”之间的本质区别。

核心观点是：“最小”应当指代产品的范围，而非其质量。作者强调了以下几个关键点：

*   **对 MVP 的误解：** 许多团队将 MVP 标签当作发布漏洞百出、缺乏打磨或不完整软件的借口。这种“半成品”缺乏提供价值所需的核心功能或用户体验，会导致用户倍感挫败。
*   **纸杯蛋糕类比：** 作者倡导“纸杯蛋糕”式开发。与其做一个大而无味、并承诺以后再补上糖衣的大蛋糕，团队应该创造一个“纸杯蛋糕”——一个小而完整、高品质且“美味”的产品。把一件事做到完美，胜过把十件事做得平庸。
*   **声誉风险：** 发布平庸的产品会损害品牌信任。第一印象很难改变，挽回一个已有负面体验的用户，要比用一款精致的工具吸引新用户困难得多。
*   **最小受人喜爱的产品（MLP）：** 作者建议将关注点转向构建“最小受人喜爱的产品”。这意味着要确保核心功能不仅可用，而且能让用户感到愉悦。

归根结底，本文是对那种因追求“快速行动、打破陈规”而导致技术债和工艺粗糙的心态的批判。它鼓励开发人员和产品经理在扩展功能之前，优先在基础核心上追求卓越。

---

## 4. Jamesob 的本地运行 SOTA 大语言模型指南

**原文标题**: Jamesob's guide to running SOTA LLMs locally

**原文链接**: [https://github.com/jamesob/local-llm](https://github.com/jamesob/local-llm)

Jamesob’s guide provides a blueprint for running State-of-the-Art (SOTA) LLMs locally, offering solutions for two budget levels: a **$2,000 entry-level setup** and a **$46,000 high-end workstation**.

**The High-End Build ($46k)**
The flagship system centers on **4x NVIDIA RTX PRO 6000 Blackwell GPUs**, providing 384GB of VRAM. To keep costs manageable, the author uses a last-gen **AMD EPYC Milan** base system with DDR4 RAM. A standout feature is the use of **c-payne PCIe Gen4 switches**, which allow GPUs to communicate peer-to-peer (P2P) at wire speeds during tensor parallelism, bypassing the CPU root complex to reduce latency.

**Technical Optimization**
The guide emphasizes several critical hardware and software tweaks:
*   **BIOS/Kernel:** Disable ASPM to prevent link downgrades and IOMMU to prevent NCCL hangs. Enable Re-Size BAR for VRAM exposure.
*   **P2P Traffic:** Use `setpci` to disable ACS (Access Control Services), ensuring data stays within the switch fabric rather than bouncing through the CPU.
*   **Power Management:** To run the system on a standard 110V circuit, GPUs are power-limited to 350W each via systemd scripts.

**Software and Workflow**
Models (such as the 594B GLM-5.2) are served via **vLLM in Docker containers**, with weights stored on a ZFS filesystem. The author uses a sandboxed VM "clanker" for interaction, utilizing local tools like Gitea for code collaboration and SearXNG for web search to maintain privacy.

**The Budget Option ($2k)**
For those with less to spend, the author recommends **2x RTX 3090s** (48GB VRAM). This setup is capable of running **Qwen-27B** and high-quality local speech-to-text via **Whisper-large-v3**, providing a powerful entry point into local machine intelligence.

---

## 5. International chess federation sanctions Kramnik

**原文标题**: International chess federation sanctions Kramnik

**原文链接**: [https://www.fide.com/fide-ethics-disciplinary-commission-issues-a-decision-in-case-involving-gm-vladimir-kramnik/](https://www.fide.com/fide-ethics-disciplinary-commission-issues-a-decision-in-case-involving-gm-vladimir-kramnik/)

生成摘要时出错

---

## 6. Factories Are Just Rooms

**原文标题**: Factories Are Just Rooms

**原文链接**: [https://interconnected.org/home/2026/07/03/factories](https://interconnected.org/home/2026/07/03/factories)

生成摘要时出错

---

## 7. Hunting a 16-year-old SQLite WAL bug with TLA+

**原文标题**: Hunting a 16-year-old SQLite WAL bug with TLA+

**原文链接**: [https://ubuntu.com/blog/hunting-a-16-year-old-sqlite-bug-with-tla-is-dqlite-affected](https://ubuntu.com/blog/hunting-a-16-year-old-sqlite-bug-with-tla-is-dqlite-affected)

生成摘要时出错

---

## 8. AI saves about 3% of your hours, and almost none of it reaches the money

**原文标题**: AI saves about 3% of your hours, and almost none of it reaches the money

**原文链接**: [https://okaneland.com/study/ai-productivity-roi-at-work/](https://okaneland.com/study/ai-productivity-roi-at-work/)

生成摘要时出错

---

## 9. PostgreSQL and the OOM Killer: Why We Use Strict Memory Overcommit

**原文标题**: PostgreSQL and the OOM Killer: Why We Use Strict Memory Overcommit

**原文链接**: [https://www.ubicloud.com/blog/postgresql-and-the-oom-killer-why-we-use-strict-memory-overcommit](https://www.ubicloud.com/blog/postgresql-and-the-oom-killer-why-we-use-strict-memory-overcommit)

生成摘要时出错

---

## 10. My Dad Helped Build North America's Oat Supply Chain: Can It Be Remade?

**原文标题**: My Dad Helped Build North America's Oat Supply Chain: Can It Be Remade?

**原文链接**: [https://ambrook.com/offrange/perspective/how-we-lost-our-oats](https://ambrook.com/offrange/perspective/how-we-lost-our-oats)

生成摘要时出错

---

## 11. Valve open source the Steam Machine e-ink screen so you can make your own

**原文标题**: Valve open source the Steam Machine e-ink screen so you can make your own

**原文链接**: [https://www.gamingonlinux.com/2026/07/valve-open-source-the-steam-machine-e-ink-screen-so-you-can-make-your-own/](https://www.gamingonlinux.com/2026/07/valve-open-source-the-steam-machine-e-ink-screen-so-you-can-make-your-own/)

生成摘要时出错

---

## 12. The Fall and Rise of Screwworm

**原文标题**: The Fall and Rise of Screwworm

**原文链接**: [https://www.construction-physics.com/p/the-fall-and-rise-of-screwworm](https://www.construction-physics.com/p/the-fall-and-rise-of-screwworm)

生成摘要时出错

---

## 13. Wordgard: The new in-browser rich-text editor from the creator of ProseMirror

**原文标题**: Wordgard: The new in-browser rich-text editor from the creator of ProseMirror

**原文链接**: [https://wordgard.net/](https://wordgard.net/)

生成摘要时出错

---

## 14. America, 1926: What a Forgotten 100-Year-Old Report Says About Who We Are

**原文标题**: America, 1926: What a Forgotten 100-Year-Old Report Says About Who We Are

**原文链接**: [https://www.derekthompson.org/p/america-1926-an-absurdly-deep-dive](https://www.derekthompson.org/p/america-1926-an-absurdly-deep-dive)

生成摘要时出错

---

## 15. Best Simple System for Now

**原文标题**: Best Simple System for Now

**原文链接**: [https://dannorth.net/blog/best-simple-system-for-now/](https://dannorth.net/blog/best-simple-system-for-now/)

生成摘要时出错

---

## 16. Right to Local Intelligence

**原文标题**: Right to Local Intelligence

**原文链接**: [https://righttointelligence.org/](https://righttointelligence.org/)

生成摘要时出错

---

## 17. Supersonic flight returning to US after half-century ban

**原文标题**: Supersonic flight returning to US after half-century ban

**原文链接**: [https://www.forbes.com/sites/suzannerowankelleher/2026/06/30/faa-supersonic-flight-no-boom/](https://www.forbes.com/sites/suzannerowankelleher/2026/06/30/faa-supersonic-flight-no-boom/)

生成摘要时出错

---

## 18. Show HN: ctx – Search the coding agent history already on your machine

**原文标题**: Show HN: ctx – Search the coding agent history already on your machine

**原文链接**: [https://github.com/ctxrs/ctx](https://github.com/ctxrs/ctx)

生成摘要时出错

---

## 19. CarPlay Is Additive

**原文标题**: CarPlay Is Additive

**原文链接**: [https://www.caseyliss.com/2026/7/2/carplay-is-additive-you-dolts](https://www.caseyliss.com/2026/7/2/carplay-is-additive-you-dolts)

生成摘要时出错

---

## 20. US residents angry datacenters 'shoved down our throats' are recalling officials

**原文标题**: US residents angry datacenters 'shoved down our throats' are recalling officials

**原文链接**: [https://www.theguardian.com/us-news/2026/jul/03/datacenter-recall-elections](https://www.theguardian.com/us-news/2026/jul/03/datacenter-recall-elections)

生成摘要时出错

---

## 21. 60% Fable cost cut by converting code to images and having the model OCR it

**原文标题**: 60% Fable cost cut by converting code to images and having the model OCR it

**原文链接**: [https://github.com/teamchong/pxpipe](https://github.com/teamchong/pxpipe)

生成摘要时出错

---

## 22. Anatomy of Persistent Memory's 3 Layers: Comparing ContextNest, Mem0 and Zep

**原文标题**: Anatomy of Persistent Memory's 3 Layers: Comparing ContextNest, Mem0 and Zep

**原文链接**: [https://promptowl.ai/resources/persistent-memory-ai-agents/](https://promptowl.ai/resources/persistent-memory-ai-agents/)

生成摘要时出错

---

## 23. Give Smart People the Tools to Do Smart Things

**原文标题**: Give Smart People the Tools to Do Smart Things

**原文链接**: [https://superuserdone.com/posts/2026-07-03-give-smart-people-the-tools/](https://superuserdone.com/posts/2026-07-03-give-smart-people-the-tools/)

生成摘要时出错

---

## 24. The Safari MCP server for web developers

**原文标题**: The Safari MCP server for web developers

**原文链接**: [https://webkit.org/blog/18136/introducing-the-safari-mcp-server-for-web-developers/](https://webkit.org/blog/18136/introducing-the-safari-mcp-server-for-web-developers/)

生成摘要时出错

---

## 25. Show HN: Mcpsnoop – Wireshark for MCP (transparent proxy and live TUI)

**原文标题**: Show HN: Mcpsnoop – Wireshark for MCP (transparent proxy and live TUI)

**原文链接**: [https://github.com/kerlenton/mcpsnoop](https://github.com/kerlenton/mcpsnoop)

生成摘要时出错

---

## 26. How working with a blind client revealed invisible accessibility gaps

**原文标题**: How working with a blind client revealed invisible accessibility gaps

**原文链接**: [https://iinteractive.com/resources/blog/read-only](https://iinteractive.com/resources/blog/read-only)

生成摘要时出错

---

## 27. crustc: entirety of `rustc`, translated to C

**原文标题**: crustc: entirety of `rustc`, translated to C

**原文链接**: [https://github.com/FractalFir/crustc](https://github.com/FractalFir/crustc)

生成摘要时出错

---

## 28. Commodore 64 Basic for PostgreSQL

**原文标题**: Commodore 64 Basic for PostgreSQL

**原文链接**: [https://thombrown.blogspot.com/2026/07/load-plcbmbasic81-commodore-64-basic.html](https://thombrown.blogspot.com/2026/07/load-plcbmbasic81-commodore-64-basic.html)

生成摘要时出错

---

## 29. Program-as-Weights: A Programming Paradigm for Fuzzy Functions

**原文标题**: Program-as-Weights: A Programming Paradigm for Fuzzy Functions

**原文链接**: [https://arxiv.org/abs/2607.02512](https://arxiv.org/abs/2607.02512)

生成摘要时出错

---

## 30. Markets are competitive if and only if P != NP

**原文标题**: Markets are competitive if and only if P != NP

**原文链接**: [https://arxiv.org/abs/2602.20415](https://arxiv.org/abs/2602.20415)

生成摘要时出错

---

## 31. Reality has a surprising amount of detail (2017)

**原文标题**: Reality has a surprising amount of detail (2017)

**原文链接**: [https://johnsalvatier.org/blog/2017/reality-has-a-surprising-amount-of-detail](https://johnsalvatier.org/blog/2017/reality-has-a-surprising-amount-of-detail)

生成摘要时出错

---

## 32. Quake in 13 Kilobytes (2021)

**原文标题**: Quake in 13 Kilobytes (2021)

**原文链接**: [https://js13kgames.com/games/q1k3](https://js13kgames.com/games/q1k3)

生成摘要时出错

---

## 33. Local Reasoning for Global Properties

**原文标题**: Local Reasoning for Global Properties

**原文链接**: [https://tratt.net/laurie/blog/2026/local_reasoning_for_global_properties.html](https://tratt.net/laurie/blog/2026/local_reasoning_for_global_properties.html)

生成摘要时出错

---

## 34. Exapunks (2018)

**原文标题**: Exapunks (2018)

**原文链接**: [https://www.zachtronics.com/exapunks/](https://www.zachtronics.com/exapunks/)

生成摘要时出错

---

## 35. Costco Is the Anti-Amazon

**原文标题**: Costco Is the Anti-Amazon

**原文链接**: [https://phenomenalworld.org/analysis/the-anti-amazon/](https://phenomenalworld.org/analysis/the-anti-amazon/)

生成摘要时出错

---

## 36. Holes

**原文标题**: Holes

**原文链接**: [https://xkcd.com/3266/large/](https://xkcd.com/3266/large/)

生成摘要时出错

---

## 37. Alibaba to ban Claude Code in workplace over alleged backdoor risks, source says

**原文标题**: Alibaba to ban Claude Code in workplace over alleged backdoor risks, source says

**原文链接**: [https://www.reuters.com/world/china/alibaba-ban-claude-code-workplace-over-alleged-backdoor-risks-source-says-2026-07-03/](https://www.reuters.com/world/china/alibaba-ban-claude-code-workplace-over-alleged-backdoor-risks-source-says-2026-07-03/)

生成摘要时出错

---

## 38. Underwater suit-wearing cyborg insect capable of diving and terra-aqua travel

**原文标题**: Underwater suit-wearing cyborg insect capable of diving and terra-aqua travel

**原文链接**: [https://www.nature.com/articles/s41467-026-74235-1](https://www.nature.com/articles/s41467-026-74235-1)

生成摘要时出错

---

## 39. Virginia bans sale of precise geolocation data

**原文标题**: Virginia bans sale of precise geolocation data

**原文链接**: [https://www.hunton.com/privacy-and-cybersecurity-law-blog/virginia-bans-sale-of-geolocation-data](https://www.hunton.com/privacy-and-cybersecurity-law-blog/virginia-bans-sale-of-geolocation-data)

生成摘要时出错

---

## 40. I Wasn't Allowed Prompting ChatGPT During My Chalk Talk: This Is Discrimination

**原文标题**: I Wasn't Allowed Prompting ChatGPT During My Chalk Talk: This Is Discrimination

**原文链接**: [https://inpreparation.substack.com/p/opinion-i-was-not-allowed-to-type](https://inpreparation.substack.com/p/opinion-i-was-not-allowed-to-type)

生成摘要时出错

---

## 41. Hackers shoveled snow for company, were rewarded with network admin access

**原文标题**: Hackers shoveled snow for company, were rewarded with network admin access

**原文链接**: [https://www.theregister.com/security/2026/07/02/hackers-shoveled-snow-for-company-were-rewarded-with-network-admin-access/5265240](https://www.theregister.com/security/2026/07/02/hackers-shoveled-snow-for-company-were-rewarded-with-network-admin-access/5265240)

生成摘要时出错

---

## 42. Using OpenTofu's Exclude Flag to Isolate Performance Bottlenecks

**原文标题**: Using OpenTofu's Exclude Flag to Isolate Performance Bottlenecks

**原文链接**: [https://masterpoint.io/blog/using-opentofu-exclude-flag-isolate-performance-bottlenecks/](https://masterpoint.io/blog/using-opentofu-exclude-flag-isolate-performance-bottlenecks/)

生成摘要时出错

---

## 43. AI coding is addictive. Engineers are paying the price

**原文标题**: AI coding is addictive. Engineers are paying the price

**原文链接**: [https://leaddev.com/ai/ai-coding-is-addictive-engineers-are-paying-the-price](https://leaddev.com/ai/ai-coding-is-addictive-engineers-are-paying-the-price)

生成摘要时出错

---

## 44. Show HN: Pieces – Social network for people

**原文标题**: Show HN: Pieces – Social network for people

**原文链接**: [https://try.piecesof.me/](https://try.piecesof.me/)

生成摘要时出错

---

## 45. The short leash AI coding method for beating Fable

**原文标题**: The short leash AI coding method for beating Fable

**原文链接**: [https://blog.okturtles.org/2026/07/short-leash-ai-method/](https://blog.okturtles.org/2026/07/short-leash-ai-method/)

生成摘要时出错

---

## 46. Postgres transactions are a distributed systems superpower

**原文标题**: Postgres transactions are a distributed systems superpower

**原文链接**: [https://www.dbos.dev/blog/co-locating-workflow-state-with-your-data](https://www.dbos.dev/blog/co-locating-workflow-state-with-your-data)

生成摘要时出错

---

## 47. Q&A with Micron's VP and GM of Memory

**原文标题**: Q&A with Micron's VP and GM of Memory

**原文链接**: [https://morethanmoore.substack.com/p/q-and-a-with-microns-vp-and-gm-of](https://morethanmoore.substack.com/p/q-and-a-with-microns-vp-and-gm-of)

生成摘要时出错

---

## 48. Zuckerberg 'Admits' Meta's Layoffs Were Ineffective

**原文标题**: Zuckerberg 'Admits' Meta's Layoffs Were Ineffective

**原文链接**: [https://eshumarneedi.com/2026/07/03/zuckerberg-admits-metas-layoffs-were.html](https://eshumarneedi.com/2026/07/03/zuckerberg-admits-metas-layoffs-were.html)

生成摘要时出错

---

## 49. Faster embeddings: how we rebuilt the ONNX path in Manticore

**原文标题**: Faster embeddings: how we rebuilt the ONNX path in Manticore

**原文链接**: [https://manticoresearch.com/blog/onnx-embeddings-speedup/](https://manticoresearch.com/blog/onnx-embeddings-speedup/)

生成摘要时出错

---

## 50. An American Privacy Emergency

**原文标题**: An American Privacy Emergency

**原文链接**: [https://scottaaronson.blog/?p=9902](https://scottaaronson.blog/?p=9902)

生成摘要时出错

---

## 51. Great Salt Lake Tracker

**原文标题**: Great Salt Lake Tracker

**原文链接**: [https://growtheflowutah.org/laketracker/](https://growtheflowutah.org/laketracker/)

生成摘要时出错

---

## 52. FoundationDB's Flow – Bringing Actor-Based Concurrency to C++11

**原文标题**: FoundationDB's Flow – Bringing Actor-Based Concurrency to C++11

**原文链接**: [https://apple.github.io/foundationdb/flow.html](https://apple.github.io/foundationdb/flow.html)

生成摘要时出错

---

## 53. Android Developer Verification: Threat masquerading as protection

**原文标题**: Android Developer Verification: Threat masquerading as protection

**原文链接**: [https://f-droid.org/2026/07/01/adv-malware.html](https://f-droid.org/2026/07/01/adv-malware.html)

生成摘要时出错

---

## 54. Superpowers 6

**原文标题**: Superpowers 6

**原文链接**: [https://blog.fsck.com/2026/06/15/Superpowers-6/](https://blog.fsck.com/2026/06/15/Superpowers-6/)

生成摘要时出错

---

## 55. Gemini Code Assist will be shut down on July 17

**原文标题**: Gemini Code Assist will be shut down on July 17

**原文链接**: [https://docs.cloud.google.com/gemini/docs/code-review/review-repo-code](https://docs.cloud.google.com/gemini/docs/code-review/review-repo-code)

生成摘要时出错

---

## 56. Claude-real-video － any LLM can watch a video

**原文标题**: Claude-real-video － any LLM can watch a video

**原文链接**: [https://github.com/HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video)

生成摘要时出错

---

## 57. Hazel (YC W24) Is Hiring for Our Largest Government Contract

**原文标题**: Hazel (YC W24) Is Hiring for Our Largest Government Contract

**原文链接**: [https://www.ycombinator.com/companies/hazel-2/jobs/3epPWgu-full-stack-engineer-ts-sci](https://www.ycombinator.com/companies/hazel-2/jobs/3epPWgu-full-stack-engineer-ts-sci)

生成摘要时出错

---

## 58. This is my attempt to get Vulkan going on NetBSD

**原文标题**: This is my attempt to get Vulkan going on NetBSD

**原文链接**: [https://github.com/segaboy/vulkan-netbsd](https://github.com/segaboy/vulkan-netbsd)

生成摘要时出错

---

## 59. Instead of banning AI, I made a classroom contract with my students

**原文标题**: Instead of banning AI, I made a classroom contract with my students

**原文链接**: [https://www.science.org/content/article/instead-banning-ai-i-made-classroom-contract-my-students](https://www.science.org/content/article/instead-banning-ai-i-made-classroom-contract-my-students)

生成摘要时出错

---

## 60. Show HN: TaskPeace – a task queue my AI coding agents pull work from over MCP

**原文标题**: Show HN: TaskPeace – a task queue my AI coding agents pull work from over MCP

**原文链接**: [https://taskpeace.com/](https://taskpeace.com/)

生成摘要时出错

---

## 61. Since Linux 6.9, LUKS suspend stopped wiping disk-encryption keys from memory

**原文标题**: Since Linux 6.9, LUKS suspend stopped wiping disk-encryption keys from memory

**原文链接**: [https://mathstodon.xyz/@iblech/116769502749142438](https://mathstodon.xyz/@iblech/116769502749142438)

生成摘要时出错

---

## 62. The Beauty of Tautologies

**原文标题**: The Beauty of Tautologies

**原文链接**: [https://scottsumner.substack.com/p/the-beauty-of-tautologies](https://scottsumner.substack.com/p/the-beauty-of-tautologies)

生成摘要时出错

---

## 63. Heuristics for lab robotics, and where its future may go

**原文标题**: Heuristics for lab robotics, and where its future may go

**原文链接**: [https://www.owlposting.com/p/heuristics-for-lab-robotics-and-where](https://www.owlposting.com/p/heuristics-for-lab-robotics-and-where)

生成摘要时出错

---

## 64. Cache Merging as a Convergent Replicated State for Multi-Agent Latent Reasoning

**原文标题**: Cache Merging as a Convergent Replicated State for Multi-Agent Latent Reasoning

**原文链接**: [https://arxiv.org/abs/2607.01308](https://arxiv.org/abs/2607.01308)

生成摘要时出错

---

## 65. PeerTube is a free, decentralized and federated video platform

**原文标题**: PeerTube is a free, decentralized and federated video platform

**原文链接**: [https://github.com/Chocobozzz/PeerTube](https://github.com/Chocobozzz/PeerTube)

生成摘要时出错

---

## 66. EFF letter to FTC on X consent order [pdf]

**原文标题**: EFF letter to FTC on X consent order [pdf]

**原文链接**: [https://www.eff.org/deeplinks/2026/06/eff-and-allies-xs-ftc-petition-waive-privacy-violation-order-should-be-rejected](https://www.eff.org/deeplinks/2026/06/eff-and-allies-xs-ftc-petition-waive-privacy-violation-order-should-be-rejected)

生成摘要时出错

---

## 67. Podman v6.0.0

**原文标题**: Podman v6.0.0

**原文链接**: [https://blog.podman.io/2026/07/introducing-podman-v6-0-0/](https://blog.podman.io/2026/07/introducing-podman-v6-0-0/)

生成摘要时出错

---

## 68. Immich 3.0

**原文标题**: Immich 3.0

**原文链接**: [https://github.com/immich-app/immich/discussions/29439](https://github.com/immich-app/immich/discussions/29439)

生成摘要时出错

---

## 69. AI's $2.2T deficit fix is already half fake, economists say

**原文标题**: AI's $2.2T deficit fix is already half fake, economists say

**原文链接**: [https://fortune.com/2026/07/02/ai-productivity-deficit-national-debt-brookings-fed-study/](https://fortune.com/2026/07/02/ai-productivity-deficit-national-debt-brookings-fed-study/)

生成摘要时出错

---

## 70. Show HN: OM Core – multidimensional models without spreadsheet cell formulas

**原文标题**: Show HN: OM Core – multidimensional models without spreadsheet cell formulas

**原文链接**: [https://github.com/cloudcell/om-core](https://github.com/cloudcell/om-core)

生成摘要时出错

---

## 71. LibreCAD in the Browser

**原文标题**: LibreCAD in the Browser

**原文链接**: [https://magik.net/librecad/](https://magik.net/librecad/)

生成摘要时出错

---

## 72. A Special Wireless-Free Nikon Camera Is Publicly Available for the First Time

**原文标题**: A Special Wireless-Free Nikon Camera Is Publicly Available for the First Time

**原文链接**: [https://petapixel.com/2026/06/24/a-special-wireless-free-nikon-camera-is-publicly-available-for-the-first-time/](https://petapixel.com/2026/06/24/a-special-wireless-free-nikon-camera-is-publicly-available-for-the-first-time/)

生成摘要时出错

---

## 73. The fall of the theorem economy

**原文标题**: The fall of the theorem economy

**原文链接**: [https://davidbessis.substack.com/p/the-fall-of-the-theorem-economy](https://davidbessis.substack.com/p/the-fall-of-the-theorem-economy)

生成摘要时出错

---

## 74. German button maker searched rivers of American Midwest for valuable shells

**原文标题**: German button maker searched rivers of American Midwest for valuable shells

**原文链接**: [https://www.smithsonianmag.com/smithsonian-institution/how-one-german-button-maker-searched-the-rivers-of-the-american-midwest-for-the-shells-that-could-make-him-a-fortune-180989012/](https://www.smithsonianmag.com/smithsonian-institution/how-one-german-button-maker-searched-the-rivers-of-the-american-midwest-for-the-shells-that-could-make-him-a-fortune-180989012/)

生成摘要时出错

---

## 75. 24-bit/192kHz music downloads and why they make no sense (2012)

**原文标题**: 24-bit/192kHz music downloads and why they make no sense (2012)

**原文链接**: [https://people.xiph.org/~xiphmont/demo/neil-young.html#toc_wd2bm](https://people.xiph.org/~xiphmont/demo/neil-young.html#toc_wd2bm)

生成摘要时出错

---

## 76. Launch HN: Manufact (YC S25) – MCP Cloud

**原文标题**: Launch HN: Manufact (YC S25) – MCP Cloud

**原文链接**: [https://manufact.com](https://manufact.com)

生成摘要时出错

---

## 77. Spain Orders Blacklist of Palantir from Public and Private Companies

**原文标题**: Spain Orders Blacklist of Palantir from Public and Private Companies

**原文链接**: [https://clashreport.com/world/articles/spain-orders-blacklist-of-us-tech-giant-palantir-from-public-and-private-companies-fsnc2z17gjv](https://clashreport.com/world/articles/spain-orders-blacklist-of-us-tech-giant-palantir-from-public-and-private-companies-fsnc2z17gjv)

生成摘要时出错

---

## 78. NSA tries to weaken mlkem standardisation?

**原文标题**: NSA tries to weaken mlkem standardisation?

**原文链接**: [https://nsa.2026.action.cr.yp.to](https://nsa.2026.action.cr.yp.to)

生成摘要时出错

---

## 79. Show HN: zkGolf – Competitive optimization of formally verified circuits

**原文标题**: Show HN: zkGolf – Competitive optimization of formally verified circuits

**原文链接**: [https://zk.golf/](https://zk.golf/)

生成摘要时出错

---

## 80. How Fighter Jets Lock on (and How the Targets Know) (2014)

**原文标题**: How Fighter Jets Lock on (and How the Targets Know) (2014)

**原文链接**: [https://gizmodo.com/how-fighter-jets-lock-on-and-how-the-targets-know-1644871272](https://gizmodo.com/how-fighter-jets-lock-on-and-how-the-targets-know-1644871272)

生成摘要时出错

---

## 81. Senior SWE-Bench: open-source benchmark that assesses agents as senior engineers

**原文标题**: Senior SWE-Bench: open-source benchmark that assesses agents as senior engineers

**原文链接**: [https://senior-swe-bench.snorkel.ai/](https://senior-swe-bench.snorkel.ai/)

生成摘要时出错

---

## 82. Is One Layer Enough? A Single Transformer Layer Matches Full-Parameter RL Train

**原文标题**: Is One Layer Enough? A Single Transformer Layer Matches Full-Parameter RL Train

**原文链接**: [https://arxiv.org/abs/2607.01232](https://arxiv.org/abs/2607.01232)

生成摘要时出错

---

## 83. Show HN: Inkwell – An RSS reader for e-ink devices

**原文标题**: Show HN: Inkwell – An RSS reader for e-ink devices

**原文链接**: [https://kendal.codeberg.page/inkwell/](https://kendal.codeberg.page/inkwell/)

生成摘要时出错

---

## 84. AI can't be listed as inventor on patent applications, Japan's top court rules

**原文标题**: AI can't be listed as inventor on patent applications, Japan's top court rules

**原文链接**: [https://japannews.yomiuri.co.jp/science-nature/technology/20260306-314930/](https://japannews.yomiuri.co.jp/science-nature/technology/20260306-314930/)

生成摘要时出错

---

## 85. How to ask for help from people who don't know you

**原文标题**: How to ask for help from people who don't know you

**原文链接**: [https://pradyuprasad.com/writings/how-to-ask-for-help/](https://pradyuprasad.com/writings/how-to-ask-for-help/)

生成摘要时出错

---

## 86. Gun Mistakes in Fiction Writing: Handgun Edition

**原文标题**: Gun Mistakes in Fiction Writing: Handgun Edition

**原文链接**: [https://www.swiftsilentdeadly.com/blog/gun-mistakes-in-fiction-writing-handgun-edition](https://www.swiftsilentdeadly.com/blog/gun-mistakes-in-fiction-writing-handgun-edition)

生成摘要时出错

---

## 87. Client-side load balancing at a million requests per second

**原文标题**: Client-side load balancing at a million requests per second

**原文链接**: [https://engineering.zalando.com/posts/2026/06/client-side-load-balancing.html?v=2](https://engineering.zalando.com/posts/2026/06/client-side-load-balancing.html](https://engineering.zalando.com/posts/2026/06/client-side-load-balancing.html?v=2](https://engineering.zalando.com/posts/2026/06/client-side-load-balancing.html)

生成摘要时出错

---

## 88. Why jet engines aren't made in China

**原文标题**: Why jet engines aren't made in China

**原文链接**: [https://aakash.substack.com/p/why-jet-engines-arent-made-in-china](https://aakash.substack.com/p/why-jet-engines-arent-made-in-china)

生成摘要时出错

---

## 89. Bring back crappy forums

**原文标题**: Bring back crappy forums

**原文链接**: [https://tedium.co/2026/07/01/online-web-forums-retrospective/](https://tedium.co/2026/07/01/online-web-forums-retrospective/)

生成摘要时出错

---

## 90. JEP 539: Strict Field Initialization in the JVM moved to preview

**原文标题**: JEP 539: Strict Field Initialization in the JVM moved to preview

**原文链接**: [https://openjdk.org/jeps/539](https://openjdk.org/jeps/539)

生成摘要时出错

---

## 91. CursorBench 3.1

**原文标题**: CursorBench 3.1

**原文链接**: [https://cursor.com/evals](https://cursor.com/evals)

生成摘要时出错

---

## 92. Cowboys, Frontiersmen, Settlers, Townspeople, Cityfolk

**原文标题**: Cowboys, Frontiersmen, Settlers, Townspeople, Cityfolk

**原文链接**: [https://huntersoftwareconsulting.com/posts/2026-06-28-company-phase-changes/](https://huntersoftwareconsulting.com/posts/2026-06-28-company-phase-changes/)

生成摘要时出错

---

## 93. Perform DFU Restores on Apple Silicon Macs with Macvdmtool (2021)

**原文标题**: Perform DFU Restores on Apple Silicon Macs with Macvdmtool (2021)

**原文链接**: [https://www.bkurtz.io/posts/macvdmtool/](https://www.bkurtz.io/posts/macvdmtool/)

生成摘要时出错

---

## 94. FBI Seizes NetNut Proxy Platform, Popa Botnet

**原文标题**: FBI Seizes NetNut Proxy Platform, Popa Botnet

**原文链接**: [https://krebsonsecurity.com/2026/07/fbi-seizes-netnut-proxy-platform-popa-botnet/](https://krebsonsecurity.com/2026/07/fbi-seizes-netnut-proxy-platform-popa-botnet/)

生成摘要时出错

---

## 95. The primary purpose of code review is to find code that will be hard to maintain

**原文标题**: The primary purpose of code review is to find code that will be hard to maintain

**原文链接**: [https://mathstodon.xyz/@mjd/115096720350507897](https://mathstodon.xyz/@mjd/115096720350507897)

生成摘要时出错

---

## 96. Amazon has enough satellites to launch its Starlink competitor

**原文标题**: Amazon has enough satellites to launch its Starlink competitor

**原文链接**: [https://www.theverge.com/science/960563/amazon-leo-service-tipping-point](https://www.theverge.com/science/960563/amazon-leo-service-tipping-point)

生成摘要时出错

---

## 97. Apricot Computers: An underrated British brand

**原文标题**: Apricot Computers: An underrated British brand

**原文链接**: [https://dfarq.homeip.net/apricot-computers-an-underrated-british-brand/](https://dfarq.homeip.net/apricot-computers-an-underrated-british-brand/)

生成摘要时出错

---

## 98. The Egg Bandits Made a Thousand Times the Fine They Just Paid for Price Fixing

**原文标题**: The Egg Bandits Made a Thousand Times the Fine They Just Paid for Price Fixing

**原文链接**: [https://www.thebignewsletter.com/p/crime-pays-the-egg-bandits-made-a](https://www.thebignewsletter.com/p/crime-pays-the-egg-bandits-made-a)

生成摘要时出错

---

## 99. For first time, a cell built from scratch grows and divides

**原文标题**: For first time, a cell built from scratch grows and divides

**原文链接**: [https://www.quantamagazine.org/for-the-first-time-a-cell-built-from-scratch-grows-and-divides-20260701/](https://www.quantamagazine.org/for-the-first-time-a-cell-built-from-scratch-grows-and-divides-20260701/)

生成摘要时出错

---

## 100. Show HN: I made a tool that prevents websites from tracking you

**原文标题**: Show HN: I made a tool that prevents websites from tracking you

**原文链接**: [https://github.com/alex-w-developer/GetBlocked](https://github.com/alex-w-developer/GetBlocked)

生成摘要时出错

---

