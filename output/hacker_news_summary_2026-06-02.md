# Hacker News 热门文章摘要 (2026-06-02)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. MAI-代码-1-闪速

**原文标题**: MAI-Code-1-Flash

**原文链接**: [https://microsoft.ai/news/introducingmai-code-1-flash/](https://microsoft.ai/news/introducingmai-code-1-flash/)

2026年6月2日，微软超级智能（Superintelligence）团队发布了 **MAI-Code-1-Flash**。这是一款专为速度、效率以及与现实开发者工作流集成而设计的新型编程模型。该模型完全采用授权数据构建，目前正逐步向 Visual Studio Code 中的 GitHub Copilot 个人用户推出。

**主要特性与性能亮点包括：**

*   **自适应思考：** 该模型可根据任务复杂度调整推理预算。对于简单请求保持简练，而对复杂问题则投入更深层的思考，在解决困难任务时所使用的 Token 比竞品减少多达 60%。
*   **生产优先训练：** 与仅针对基准测试优化的模型不同，MAI-Code-1-Flash 采用生产环境下的 GitHub Copilot 测试框架进行训练。这使其非常适合智能体（agentic）编程任务，例如仓库级问答和代码重构。
*   **卓越的基准表现：** 该模型在多项主要评估中超越了 Claude Haiku 4.5。最显著的是，它在 SWE-Bench Pro 上实现了 51.2% 的成功率（领先 Haiku 16 个百分点），并在精准指令遵循（IF Bench）和对抗性推理方面表现出显著提升。
*   **高效与智能：** 通过结合高准确率和更低的 Token 消耗，该模型在不牺牲质量的前提下降低了延迟和成本。它还在数学、科学和视觉生成编程方面展示了强大的推理能力。

MAI-Code-1-Flash 现可通过 VS Code 模型选择器或“自动（Auto）”选择器使用。此次发布是微软超级智能团队的一个里程碑，该团队利用下一代 GB200 集群来构建其专业化 AI 系列产品。

---

## 2. Gmail 觉得我太蠢，所以我离开了。

**原文标题**: Gmail thinks I'm stupid, so I left

**原文链接**: [https://moddedbear.com/gmail-thinks-im-stupid-so-i-left](https://moddedbear.com/gmail-thinks-im-stupid-so-i-left)

In this article, author JP explains their decision to abandon a 16-year-old Gmail account due to the platform’s intrusive and aggressive integration of generative AI. 

JP’s primary grievance is not the existence of AI, but its unsolicited presence in the user interface. They describe a workflow constantly interrupted by unwanted message summaries, pre-drafted replies, and persistent “Help me write” prompts. To the author, these features feel patronizing and disrespectful, sending the message that users are incapable of reading or writing their own emails and that recipients are not worth the time of a human response.

The author also highlights a "user-hostile" design choice: the inability to disable these AI features without also losing long-standing, useful tools like automatic thread categorization. JP suspects this is an intentional move by Google to artificially inflate usage metrics for their language models.

Disenchanted by the "clean break" required to escape these features, JP has begun migrating to Fastmail using a custom domain. Though early in the transition, they praise the new service's flexibility and are considering starting fresh rather than importing 16 years of Gmail data. Ultimately, the article serves as a warning to tech companies that forced AI integration can alienate even the most loyal, long-term users.

---

## 3. 西雅图监控基础设施步行之旅 (2020)

**原文标题**: A walking tour of surveillance infrastructure in Seattle (2020)

**原文链接**: [https://coveillance.org/a-walking-tour-of-surveillance-infrastructure-in-seattle/](https://coveillance.org/a-walking-tour-of-surveillance-infrastructure-in-seattle/)

本文详细介绍了2020年的一次西雅图徒步导览，旨在揭示“智慧城市”中无处不在、却又“隐于显处”的监控基础设施。该指南由技术公平联盟（Tech Equity Coalition）和华盛顿州美国公民自由联盟（ACLU of Washington）共同制定，重点阐述了几项核心技术及其社会影响：

*   **监控摄像头：** 西雅图市中心随处可见的摄像头不仅能录制视频，还可以被远程控制并联网。该指南质疑这些“编码的注视”如何强化社会规范，并对特定群体进行不成比例的监控。
*   **Amazon Go：** 这些无人商店利用顶置摄像头追踪顾客的移动和浏览习惯。相关数据可与在线个人资料关联，从而预测宗教信仰或健康状况等敏感信息，引发了对透明度和强化刻板印象的担忧。
*   **自动车牌识别器 (ALPR)：** 固定式和移动式 ALPR 每年采集数百万个车牌信息。指南警告称，这存在“功能蔓延”风险，即原用于交通管理或停车执法的数据，在未经监管或公众同意的情况下，被共享给执法机构或私人数据库。
*   **Acyclica：** 这些安装在交通信号灯上的设备通过拦截智能手机发送的 Wi-Fi “探测数据包”来追踪个人位置。这使城市能够通过唯一的 MAC 地址监测移动模式，而公众对此往往毫不知情。
*   **华盛顿州融合中心：** 这是一个 9/11 后建立的情报枢纽，旨在促进当地警方、FBI、国土安全部以及私营企业之间的大规模数据共享。

其核心主题是呼吁加强监督和透明度。文章指出，这些技术通常在未经公众同意的情况下运行，导致了“强制性数据收集”，并可能使监控数据被移民海关执法局 (ICE) 等机构利用，进而针对边缘化群体。

---

## 4. GitHub Copilot App

**原文标题**: GitHub Copilot App

**原文链接**: [https://github.com/features/preview/github-app](https://github.com/features/preview/github-app)

GitHub 发布了 **GitHub Copilot 应用程序** 的技术预览版，这是一款专为智能体驱动（agent-driven）开发设计的原生桌面体验。该应用旨在简化整个开发生命周期——从管理 Issue 和拉取请求到审查代码差异和合并代码。

预览版的主要功能包括：
*   **智能体驱动工作流：** 开发者可以将任务分配给智能体，以实现编码流程自动化并完成闭环。
*   **并行会话：** 该应用支持在不同仓库中同时运行多个智能体会话，每个会话均相互隔离并可实时跟踪。
*   **可扩展性：** 用户可以使用模型上下文协议 (MCP) 服务器和自定义技能来自动化重复工作流并扩展智能体能力。

**访问权限与资格：**
现有的 **Copilot Pro、Pro+、Max、Business 和 Enterprise** 客户可以立即安装该应用。但是，Business 和 Enterprise 用户需要组织层级的许可并启用 Copilot CLI。Copilot 免费版用户和新客户需加入等候名单，以便在权限扩大时获得通知。

---

## 5. MAI-思考-1

**原文标题**: MAI-Thinking-1

**原文链接**: [https://microsoft.ai/news/introducing-mai-thinking-1/](https://microsoft.ai/news/introducing-mai-thinking-1/)

微软 AI 推出了 **MAI-Thinking-1**，这是一款中型推理模型，旨在处理高级数学、科学和软件工程任务。该模型采用稀疏混合专家（MoE）架构，拥有 350 亿激活参数（总参数约 1 万亿），在编程基准测试中达到了与 Claude Opus 4.6 等领先对手相当的水平，且在人类评估中比 Sonnet 4.6 更受青睐。

公告的主要亮点包括：

*   **登山机 (The Hill-Climbing Machine)：** 微软专有的开发流水线，旨在实现持续、可重复的改进。它将内部硬件加速器与强化学习框架相结合，确保能力是原生习得的，而非从第三方模型蒸馏而来。
*   **数据完整性：** 模型完全采用干净、经过商业授权的数据进行训练，预训练过程中特意排除了 AI 生成的内容，以确保更好的来源可靠性和可控性。
*   **性能：** MAI-Thinking-1 展现了卓越的推理能力，在 AIME 2025 数学基准测试中得分 97%。它针对智能体编程进行了优化，提供确定性环境供模型练习多步开发工作流。
*   **人文超级智能：** 开发理念优先考虑人类的自主性。该模型被设计为服务于用户的辅助技术，而非取代用户。值得注意的是，训练平衡了安全性和有用性，以防止对合法请求的“不必要拒绝”。
*   **企业级就绪：** 该模型支持 256k token 上下文窗口、函数调用，并通过 Microsoft Foundry 提供企业级安全性。

MAI-Thinking-1 目前已在 Microsoft Foundry 开启私测（Private Preview），随后将在 MAI Playground 开启公测（Public Preview）。

---

## 6. 开放维修数据标准 – 开放维修联盟

**原文标题**: Open Repair Data Standard – Open Repair Alliance

**原文链接**: [https://openrepair.org/open-data/open-standard/](https://openrepair.org/open-data/open-standard/)

The Open Repair Data Standard (ORDS), developed by the Open Repair Alliance, is a framework designed to unify the collection and sharing of data regarding the repair of small electrical and electronic devices. By standardizing how information is recorded across different community repair groups globally, the Alliance can identify recurring patterns, common product failures, and barriers to repair.

The current version of the standard (v0.3) organizes data into three core modules:
*   **Product Related:** Captures the category, brand, and year of manufacture.
*   **Repair Related:** Documents the specific problem, the outcome (Repair Status), and any obstacles encountered (Repair Barrier).
*   **Session Related:** Includes administrative data such as the event date and the group identifier.

To ensure data quality and ease of aggregation, the standard provides specific guidelines for each field. Notable updates in recent versions include the removal of the "model" field due to inconsistent data quality and the introduction of standardized options for repair statuses and categories.

All aggregated datasets are published every six months under an open Creative Commons license, making them accessible to researchers, policymakers, and the public. Moving forward, the Alliance intends to further refine the standard by investigating UNU-keys for product categorization and developing a formal taxonomy for fault types. The ultimate goal of ORDS is to foster a transparent, global understanding of electronic repairability to inform better product design and policy.

---

## 7. Adafruit 收到 Fenwick 法律顾问代表 Flux.ai 发出的律师函。

**原文标题**: Adafruit receives demand letter from Fenwick legal counsel on behalf of Flux.ai

**原文链接**: [https://blog.adafruit.com/](https://blog.adafruit.com/)

2026年6月1日，Adafruit宣布收到由Fenwick & West律师事务所代表Defy Gravity, Inc. (Flux.ai)发出的律师函。该函件由该律所合伙人、前FBI幕僚长Jonathan F. Lenzner发出，要求Adafruit不得发布一篇包含Flux所称的关于其知识产权、商业势头及用户群体的诽谤性指控的文章。

该律师函还根据《计算机欺诈与滥用法》(CFAA)提出了指控。Adafruit驳斥了这些指控，称相关信息是由于Flux端的服务器配置错误导致数据公开后才被获取的。Adafruit坚称其报道是出于公共安全利益，并遵循了负责任的披露标准。

尽管Adafruit“强烈反对”函件中的主张，但该公司已选择在评估法律应对措施及确定后续步骤期间，暂时停止在博客上发布内容。公司表示，将随着事态发展向社区通报最新进展。

---

## 8. Microsoft announces Scout, an autonomous AI agent built on OpenClaw

**原文标题**: Microsoft announces Scout, an autonomous AI agent built on OpenClaw

**原文链接**: [https://www.computerworld.com/article/4180103/microsoft-unveils-scout-an-autonomous-ai-agent-built-on-openclaw.html](https://www.computerworld.com/article/4180103/microsoft-unveils-scout-an-autonomous-ai-agent-built-on-openclaw.html)

生成摘要时出错

---

## 9. Trump signs downsized AI order after weeks of reversals

**原文标题**: Trump signs downsized AI order after weeks of reversals

**原文链接**: [https://www.politico.com/news/2026/06/02/trump-signs-downsized-ai-order-00946389](https://www.politico.com/news/2026/06/02/trump-signs-downsized-ai-order-00946389)

生成摘要时出错

---

## 10. QBE – Compiler Backend – 1.3

**原文标题**: QBE – Compiler Backend – 1.3

**原文链接**: [https://c9x.me/compile/release/qbe-1.3.html](https://c9x.me/compile/release/qbe-1.3.html)

生成摘要时出错

---

## 11. The advertising cartel coming to your web browser

**原文标题**: The advertising cartel coming to your web browser

**原文链接**: [https://blog.zgp.org/the-advertising-cartel-coming-to-your-web-browser/](https://blog.zgp.org/the-advertising-cartel-coming-to-your-web-browser/)

生成摘要时出错

---

## 12. Expanding Project Glasswing

**原文标题**: Expanding Project Glasswing

**原文链接**: [https://www.anthropic.com/news/expanding-project-glasswing](https://www.anthropic.com/news/expanding-project-glasswing)

生成摘要时出错

---

## 13. Why Janet? (2023)

**原文标题**: Why Janet? (2023)

**原文链接**: [https://ianthehenry.com/posts/why-janet/](https://ianthehenry.com/posts/why-janet/)

生成摘要时出错

---

## 14. Fidonet: Technology, Use, Tools, and History (1993)

**原文标题**: Fidonet: Technology, Use, Tools, and History (1993)

**原文链接**: [https://www.fidonet.org/inet92_Randy_Bush.txt](https://www.fidonet.org/inet92_Randy_Bush.txt)

生成摘要时出错

---

## 15. How we index images for RAG

**原文标题**: How we index images for RAG

**原文链接**: [https://www.kapa.ai/blog/how-we-index-images-for-rag](https://www.kapa.ai/blog/how-we-index-images-for-rag)

生成摘要时出错

---

## 16. Three Ways to Get Paid (2018)

**原文标题**: Three Ways to Get Paid (2018)

**原文链接**: [https://jasonzweig.com/three-ways-to-get-paid/](https://jasonzweig.com/three-ways-to-get-paid/)

生成摘要时出错

---

## 17. Love systemd timers

**原文标题**: Love systemd timers

**原文链接**: [https://blog.tjll.net/you-dont-love-systemd-timers-enough/](https://blog.tjll.net/you-dont-love-systemd-timers-enough/)

生成摘要时出错

---

## 18. Coreutils for Windows

**原文标题**: Coreutils for Windows

**原文链接**: [https://github.com/microsoft/coreutils](https://github.com/microsoft/coreutils)

生成摘要时出错

---

## 19. Multicore suppport for DOS is real – partly

**原文标题**: Multicore suppport for DOS is real – partly

**原文链接**: [https://www.vogons.org/viewtopic.php?t=111336](https://www.vogons.org/viewtopic.php?t=111336)

生成摘要时出错

---

## 20. HP re-releases classic computer science calculator: The HP-16C

**原文标题**: HP re-releases classic computer science calculator: The HP-16C

**原文链接**: [https://hpcalcs.com/product/hp-16c-collectors-edition/](https://hpcalcs.com/product/hp-16c-collectors-edition/)

生成摘要时出错

---

## 21. Great Question (YC W21) Is Hiring Applied AI Interns

**原文标题**: Great Question (YC W21) Is Hiring Applied AI Interns

**原文链接**: [https://www.ycombinator.com/companies/great-question/jobs/J5TNvQH-ai-engineer-intern](https://www.ycombinator.com/companies/great-question/jobs/J5TNvQH-ai-engineer-intern)

生成摘要时出错

---

## 22. Bringing Up DeepSeek-V4-Flash on AMD MI300X

**原文标题**: Bringing Up DeepSeek-V4-Flash on AMD MI300X

**原文链接**: [https://fergusfinn.com/blog/deepseek-v4-flash-mi300x/](https://fergusfinn.com/blog/deepseek-v4-flash-mi300x/)

生成摘要时出错

---

## 23. Rethinking search as code generation

**原文标题**: Rethinking search as code generation

**原文链接**: [https://research.perplexity.ai/articles/rethinking-search-as-code-generation](https://research.perplexity.ai/articles/rethinking-search-as-code-generation)

生成摘要时出错

---

## 24. BQN: What Is a Primitive?

**原文标题**: BQN: What Is a Primitive?

**原文链接**: [https://mlochbaum.github.io/BQN/commentary/primitive.html](https://mlochbaum.github.io/BQN/commentary/primitive.html)

生成摘要时出错

---

## 25. Show HN: RePlaya – self-hosted browser session replay with live tailing

**原文标题**: Show HN: RePlaya – self-hosted browser session replay with live tailing

**原文链接**: [https://github.com/s2-streamstore/replaya](https://github.com/s2-streamstore/replaya)

生成摘要时出错

---

## 26. Key chemistry question answered, no quantum computer required

**原文标题**: Key chemistry question answered, no quantum computer required

**原文链接**: [https://www.quantamagazine.org/key-chemistry-question-answered-no-quantum-computer-required-20260529/](https://www.quantamagazine.org/key-chemistry-question-answered-no-quantum-computer-required-20260529/)

生成摘要时出错

---

## 27. Stop Ruining It

**原文标题**: Stop Ruining It

**原文链接**: [https://seths.blog/2026/06/stop-ruining-it/](https://seths.blog/2026/06/stop-ruining-it/)

生成摘要时出错

---

## 28. Muxcard, a DIY credit card size computer

**原文标题**: Muxcard, a DIY credit card size computer

**原文链接**: [https://github.com/krauseler/muxcard](https://github.com/krauseler/muxcard)

生成摘要时出错

---

## 29. CSS-Native Parallax Effect

**原文标题**: CSS-Native Parallax Effect

**原文链接**: [https://dan-webnotes.com/posts/2026-06-02-css-native-parallax-effect/](https://dan-webnotes.com/posts/2026-06-02-css-native-parallax-effect/)

生成摘要时出错

---

## 30. Show HN: Eyeball

**原文标题**: Show HN: Eyeball

**原文链接**: [https://eyeball.rory.codes/](https://eyeball.rory.codes/)

生成摘要时出错

---

## 31. Amazon faces class action lawsuit over Ring facial-recognition feature

**原文标题**: Amazon faces class action lawsuit over Ring facial-recognition feature

**原文链接**: [https://techcrunch.com/2026/06/02/amazon-faces-class-action-lawsuit-over-ring-facial-recognition-feature/](https://techcrunch.com/2026/06/02/amazon-faces-class-action-lawsuit-over-ring-facial-recognition-feature/)

生成摘要时出错

---

## 32. On the nature of autobiographical memory

**原文标题**: On the nature of autobiographical memory

**原文链接**: [https://theamericanscholar.org/you-must-remember-this/](https://theamericanscholar.org/you-must-remember-this/)

生成摘要时出错

---

## 33. Reviving Teletext for Ham Radio

**原文标题**: Reviving Teletext for Ham Radio

**原文链接**: [https://spectrum.ieee.org/reviving-teletext-for-ham-radio](https://spectrum.ieee.org/reviving-teletext-for-ham-radio)

生成摘要时出错

---

## 34. Pyro Caml Continuous Profiler for OCaml

**原文标题**: Pyro Caml Continuous Profiler for OCaml

**原文链接**: [https://semgrep.dev/blog/2026/announcing-pyro-caml-continuous-profiler-ocaml/](https://semgrep.dev/blog/2026/announcing-pyro-caml-continuous-profiler-ocaml/)

生成摘要时出错

---

## 35. Squillions: How money laundering won

**原文标题**: Squillions: How money laundering won

**原文链接**: [https://www.lrb.co.uk/the-paper/v48/n09/john-lanchester/squillions](https://www.lrb.co.uk/the-paper/v48/n09/john-lanchester/squillions)

生成摘要时出错

---

## 36. Why Custom Attributes in .NET Give Me Nightmares

**原文标题**: Why Custom Attributes in .NET Give Me Nightmares

**原文链接**: [https://blog.washi.dev/posts/custom-attributes-and-why-they-suck/](https://blog.washi.dev/posts/custom-attributes-and-why-they-suck/)

生成摘要时出错

---

## 37. Webcam head tracking, webcam to control in‑game FOV

**原文标题**: Webcam head tracking, webcam to control in‑game FOV

**原文链接**: [https://www.openfov.com/](https://www.openfov.com/)

生成摘要时出错

---

## 38. Apple rejected my dictation app for using the accessibility API

**原文标题**: Apple rejected my dictation app for using the accessibility API

**原文链接**: [https://www.mitmllc.com/blog/apple-rejected-my-dictation-app/](https://www.mitmllc.com/blog/apple-rejected-my-dictation-app/)

生成摘要时出错

---

## 39. The newest Instagram “exploit” is the goofiest I've seen

**原文标题**: The newest Instagram “exploit” is the goofiest I've seen

**原文链接**: [https://www.0xsid.com/blog/meta-account-takeover-fiasco](https://www.0xsid.com/blog/meta-account-takeover-fiasco)

生成摘要时出错

---

## 40. Rk New York police investigate mysterious cases of people coming out of manholes

**原文标题**: Rk New York police investigate mysterious cases of people coming out of manholes

**原文链接**: [https://www.theguardian.com/us-news/2026/jun/02/new-york-police-investigate-people-emerging-manholes](https://www.theguardian.com/us-news/2026/jun/02/new-york-police-investigate-people-emerging-manholes)

生成摘要时出错

---

## 41. CQL: Categorical Databases

**原文标题**: CQL: Categorical Databases

**原文链接**: [https://categoricaldata.net/](https://categoricaldata.net/)

生成摘要时出错

---

## 42. Microsoft Wants to 'Make People Addicted' to Its New AI Assistant

**原文标题**: Microsoft Wants to 'Make People Addicted' to Its New AI Assistant

**原文链接**: [https://www.404media.co/microsoft-wants-to-make-people-addicted-to-scout-its-new-ai-assistant-internal-documents-reveal/](https://www.404media.co/microsoft-wants-to-make-people-addicted-to-scout-its-new-ai-assistant-internal-documents-reveal/)

生成摘要时出错

---

## 43. Do turmeric and curcumin have any actual health benefits?

**原文标题**: Do turmeric and curcumin have any actual health benefits?

**原文链接**: [https://www.newscientist.com/article/2528418-do-turmeric-and-curcumin-have-any-actual-health-benefits/](https://www.newscientist.com/article/2528418-do-turmeric-and-curcumin-have-any-actual-health-benefits/)

生成摘要时出错

---

## 44. CLI tool that packages data science projects for LLM context windows

**原文标题**: CLI tool that packages data science projects for LLM context windows

**原文链接**: [https://github.com/arianmokhtariha/data2prompt](https://github.com/arianmokhtariha/data2prompt)

生成摘要时出错

---

## 45. Can the stockmarket swallow Anthropic, SpaceX and OpenAI?

**原文标题**: Can the stockmarket swallow Anthropic, SpaceX and OpenAI?

**原文链接**: [https://www.economist.com/finance-and-economics/2026/06/01/can-the-stockmarket-swallow-anthropic-spacex-and-openai](https://www.economist.com/finance-and-economics/2026/06/01/can-the-stockmarket-swallow-anthropic-spacex-and-openai)

生成摘要时出错

---

## 46. Android will now warn you if a caller is impersonating someone you know

**原文标题**: Android will now warn you if a caller is impersonating someone you know

**原文链接**: [https://www.engadget.com/2184125/android-will-now-warn-you-if-a-caller-is-impersonating-someone-you-know/](https://www.engadget.com/2184125/android-will-now-warn-you-if-a-caller-is-impersonating-someone-you-know/)

生成摘要时出错

---

## 47. AI Vulnerability Intelligence Agent Converts CVEs to Actionable Security Reports

**原文标题**: AI Vulnerability Intelligence Agent Converts CVEs to Actionable Security Reports

**原文链接**: [https://github.com/gtamir02-png/cve-ai-agent/blob/main/README.md](https://github.com/gtamir02-png/cve-ai-agent/blob/main/README.md)

生成摘要时出错

---

## 48. PCMFlowG722 wideband (HD voice) codec for ESP32

**原文标题**: PCMFlowG722 wideband (HD voice) codec for ESP32

**原文链接**: [https://github.com/tanakamasayuki/PCMFlowG722](https://github.com/tanakamasayuki/PCMFlowG722)

生成摘要时出错

---

## 49. Strace-ui, Bonsai_term, and the TUI renaissance

**原文标题**: Strace-ui, Bonsai_term, and the TUI renaissance

**原文链接**: [https://blog.janestreet.com/strace-ui-bonsai-term-and-the-tui-renaissance/](https://blog.janestreet.com/strace-ui-bonsai-term-and-the-tui-renaissance/)

生成摘要时出错

---

## 50. Should you normalize RGB values by 255 or 256?

**原文标题**: Should you normalize RGB values by 255 or 256?

**原文链接**: [https://30fps.net/pages/255-vs-256-division/](https://30fps.net/pages/255-vs-256-division/)

生成摘要时出错

---

## 51. The S in Interoperability

**原文标题**: The S in Interoperability

**原文链接**: [https://frederikbraun.de/the-s-in-interoperability.html](https://frederikbraun.de/the-s-in-interoperability.html)

生成摘要时出错

---

## 52. Preparing for KDE Plasma's Last X11-Supported Release

**原文标题**: Preparing for KDE Plasma's Last X11-Supported Release

**原文链接**: [https://blog.davidedmundson.co.uk/blog/596/](https://blog.davidedmundson.co.uk/blog/596/)

生成摘要时出错

---

## 53. Larry Ellison: "Citizens will be on their best behavior because we’re recording"

**原文标题**: Larry Ellison: "Citizens will be on their best behavior because we’re recording"

**原文链接**: [https://www.techradar.com/pro/quote-of-the-day-by-oracle-co-founder-larry-ellison-citizens-will-be-on-their-best-behavior-because-were-constantly-recording-and-reporting-everything-that-is-going-on-a-dire-warning-on-the-erosion-of-privacy](https://www.techradar.com/pro/quote-of-the-day-by-oracle-co-founder-larry-ellison-citizens-will-be-on-their-best-behavior-because-were-constantly-recording-and-reporting-everything-that-is-going-on-a-dire-warning-on-the-erosion-of-privacy)

生成摘要时出错

---

## 54. BPF support in GCC 16 and beyond

**原文标题**: BPF support in GCC 16 and beyond

**原文链接**: [https://lwn.net/SubscriberLink/1071973/19e2866f07249dfb/](https://lwn.net/SubscriberLink/1071973/19e2866f07249dfb/)

生成摘要时出错

---

## 55. macOS needs its grid back

**原文标题**: macOS needs its grid back

**原文链接**: [https://blog.hopefullyuseful.com/blog/macos-needs-its-grid-back/](https://blog.hopefullyuseful.com/blog/macos-needs-its-grid-back/)

生成摘要时出错

---

## 56. Gold replaces US Treasuries as top reserve asset, ECB says

**原文标题**: Gold replaces US Treasuries as top reserve asset, ECB says

**原文链接**: [https://www.ft.com/content/87ef8f25-eb81-4eed-919c-fe5b49a1ac2c](https://www.ft.com/content/87ef8f25-eb81-4eed-919c-fe5b49a1ac2c)

生成摘要时出错

---

## 57. Fooling around with encrypted reasoning blobs

**原文标题**: Fooling around with encrypted reasoning blobs

**原文链接**: [https://blog.cryptographyengineering.com/2026/05/29/fooling-around-with-encrypted-reasoning-blobs/](https://blog.cryptographyengineering.com/2026/05/29/fooling-around-with-encrypted-reasoning-blobs/)

生成摘要时出错

---

## 58. What appear to be biochemical processes may be a natural feature of geology

**原文标题**: What appear to be biochemical processes may be a natural feature of geology

**原文链接**: [https://www.quantamagazine.org/the-dirt-that-refused-to-die-20260601/](https://www.quantamagazine.org/the-dirt-that-refused-to-die-20260601/)

生成摘要时出错

---

## 59. Promoting Advanced Artificial Intelligence Innovation and Security

**原文标题**: Promoting Advanced Artificial Intelligence Innovation and Security

**原文链接**: [https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/](https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/)

生成摘要时出错

---

## 60. Promoting Advanced Artificial Intelligence Innovation and Security

**原文标题**: Promoting Advanced Artificial Intelligence Innovation and Security

**原文链接**: [https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/](https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/)

生成摘要时出错

---

## 61. How is Groq raising more money?

**原文标题**: How is Groq raising more money?

**原文链接**: [https://www.zach.be/p/how-the-hell-is-groq-raising-more](https://www.zach.be/p/how-the-hell-is-groq-raising-more)

生成摘要时出错

---

## 62. Amazon paid music subscription will soon include ads and lose downloads

**原文标题**: Amazon paid music subscription will soon include ads and lose downloads

**原文链接**: [https://old.reddit.com/r/mildlyinfuriating/comments/1tur3w5/amazon_just_informed_me_that_my_paid_music/](https://old.reddit.com/r/mildlyinfuriating/comments/1tur3w5/amazon_just_informed_me_that_my_paid_music/)

生成摘要时出错

---

## 63. What Efforts to Cancel Richard Stallman Ought to Teach Us About the Media

**原文标题**: What Efforts to Cancel Richard Stallman Ought to Teach Us About the Media

**原文链接**: [https://techrights.org/n/2026/06/02/What_Efforts_to_Cancel_Richard_Stallman_Ought_to_Teach_Us_About.shtml](https://techrights.org/n/2026/06/02/What_Efforts_to_Cancel_Richard_Stallman_Ought_to_Teach_Us_About.shtml)

生成摘要时出错

---

## 64. Show HN: DropLock – E2EE secret sharing web app with no backend

**原文标题**: Show HN: DropLock – E2EE secret sharing web app with no backend

**原文链接**: [https://droplock.apitman.com/](https://droplock.apitman.com/)

生成摘要时出错

---

## 65. Hermes Desktop

**原文标题**: Hermes Desktop

**原文链接**: [https://hermes-agent.nousresearch.com/desktop](https://hermes-agent.nousresearch.com/desktop)

生成摘要时出错

---

## 66. Sites and role specific plugins in Codex

**原文标题**: Sites and role specific plugins in Codex

**原文链接**: [https://openai.com/index/codex-for-every-role-tool-workflow/](https://openai.com/index/codex-for-every-role-tool-workflow/)

生成摘要时出错

---

## 67. Show HN: Build Your Own AI Agent CLI in 150 Lines

**原文标题**: Show HN: Build Your Own AI Agent CLI in 150 Lines

**原文链接**: [https://go-micro.dev/blog/11](https://go-micro.dev/blog/11)

生成摘要时出错

---

## 68. Intelligent Terminal 0.1

**原文标题**: Intelligent Terminal 0.1

**原文链接**: [https://devblogs.microsoft.com/commandline/announcing-intelligent-terminal-version-0-1/](https://devblogs.microsoft.com/commandline/announcing-intelligent-terminal-version-0-1/)

生成摘要时出错

---

## 69. I made my phone slow on purpose

**原文标题**: I made my phone slow on purpose

**原文链接**: [https://vinewallapp.com/notes/i-made-my-phone-slow-on-purpose/](https://vinewallapp.com/notes/i-made-my-phone-slow-on-purpose/)

生成摘要时出错

---

## 70. Iddqd, or the hardest kind of unsafe Rust

**原文标题**: Iddqd, or the hardest kind of unsafe Rust

**原文链接**: [https://oxide.computer/blog/iddqd-unsafe](https://oxide.computer/blog/iddqd-unsafe)

生成摘要时出错

---

## 71. Chipotlai Max

**原文标题**: Chipotlai Max

**原文链接**: [https://github.com/cyberpapiii/chipotlai-max](https://github.com/cyberpapiii/chipotlai-max)

生成摘要时出错

---

## 72. Surface RTX Spark Dev Box

**原文标题**: Surface RTX Spark Dev Box

**原文链接**: [https://www.microsoft.com/en-us/surface/devices/surface-rtx-spark-dev-box](https://www.microsoft.com/en-us/surface/devices/surface-rtx-spark-dev-box)

生成摘要时出错

---

## 73. OpenAI frontier models and Codex are now available on AWS

**原文标题**: OpenAI frontier models and Codex are now available on AWS

**原文链接**: [https://openai.com/index/openai-frontier-models-and-codex-are-now-available-on-aws/](https://openai.com/index/openai-frontier-models-and-codex-are-now-available-on-aws/)

生成摘要时出错

---

## 74. Alphabet announces $80B equity capital raise to expand AI infra and compute

**原文标题**: Alphabet announces $80B equity capital raise to expand AI infra and compute

**原文链接**: [https://abc.xyz/investor/news/news-details/2026/Alphabet-Announces-Proposed-80-Billion-Equity-Capital-Raise-to-Expand-AI-Infrastructure-and-Compute-2026-b0myAMewCa/default.aspx](https://abc.xyz/investor/news/news-details/2026/Alphabet-Announces-Proposed-80-Billion-Equity-Capital-Raise-to-Expand-AI-Infrastructure-and-Compute-2026-b0myAMewCa/default.aspx)

生成摘要时出错

---

## 75. MAI-Thinking-1 [pdf]

**原文标题**: MAI-Thinking-1 [pdf]

**原文链接**: [https://microsoft.ai/wp-content/uploads/2026/06/main_20260602_2.pdf](https://microsoft.ai/wp-content/uploads/2026/06/main_20260602_2.pdf)

生成摘要时出错

---

## 76. A new way to build chips: Sequentially stacking silicon to extend Moore's Law

**原文标题**: A new way to build chips: Sequentially stacking silicon to extend Moore's Law

**原文链接**: [https://matse.illinois.edu/news/85775](https://matse.illinois.edu/news/85775)

生成摘要时出错

---

## 77. On Reading SRAMs in IR Images, and Establishing Bounds on Trust

**原文标题**: On Reading SRAMs in IR Images, and Establishing Bounds on Trust

**原文链接**: [https://www.bunniestudios.com/blog/2026/on-reading-srams-in-ir-images-and-establishing-bounds-on-trust/](https://www.bunniestudios.com/blog/2026/on-reading-srams-in-ir-images-and-establishing-bounds-on-trust/)

生成摘要时出错

---

## 78. Windows GOG DOS Games on M-Series Macs

**原文标题**: Windows GOG DOS Games on M-Series Macs

**原文链接**: [https://f055.net/technology/windows-gog-dos-games-on-m-series-macs/](https://f055.net/technology/windows-gog-dos-games-on-m-series-macs/)

生成摘要时出错

---

## 79. Amazon joins Microsoft in sending message to employees

**原文标题**: Amazon joins Microsoft in sending message to employees

**原文链接**: [https://finance.yahoo.com/sectors/technology/articles/amazon-joins-microsoft-sending-shocking-171700630.html](https://finance.yahoo.com/sectors/technology/articles/amazon-joins-microsoft-sending-shocking-171700630.html)

生成摘要时出错

---

## 80. Florida sues OpenAI and Sam Altman over AI risks

**原文标题**: Florida sues OpenAI and Sam Altman over AI risks

**原文链接**: [https://www.politico.com/news/2026/06/01/openai-hit-with-florida-lawsuit-00944215](https://www.politico.com/news/2026/06/01/openai-hit-with-florida-lawsuit-00944215)

生成摘要时出错

---

## 81. Privacy isn't dead: it's just that tech companies have made it inconvenient

**原文标题**: Privacy isn't dead: it's just that tech companies have made it inconvenient

**原文链接**: [https://inforrm.org/2026/06/02/privacy-isnt-dead-its-just-that-tech-companies-have-made-it-inconvenient-sandra-matz/](https://inforrm.org/2026/06/02/privacy-isnt-dead-its-just-that-tech-companies-have-made-it-inconvenient-sandra-matz/)

生成摘要时出错

---

## 82. Microsoft to Ship Coreutils with Windows

**原文标题**: Microsoft to Ship Coreutils with Windows

**原文链接**: [https://www.theverge.com/news/941314/microsoft-windows-11-developer-optimized-experience-linux](https://www.theverge.com/news/941314/microsoft-windows-11-developer-optimized-experience-linux)

生成摘要时出错

---

## 83. Toy Story 5 shows 'terror' of children's screen addiction, says Tom Hanks

**原文标题**: Toy Story 5 shows 'terror' of children's screen addiction, says Tom Hanks

**原文链接**: [https://www.bbc.com/news/articles/cy5222wn410o](https://www.bbc.com/news/articles/cy5222wn410o)

生成摘要时出错

---

## 84. Flipper Zero Zig Template

**原文标题**: Flipper Zero Zig Template

**原文链接**: [https://github.com/NishantJoshi00/flipper-template](https://github.com/NishantJoshi00/flipper-template)

生成摘要时出错

---

## 85. U.S. midterms have a cyber problem, but it's not at the ballot box

**原文标题**: U.S. midterms have a cyber problem, but it's not at the ballot box

**原文链接**: [https://blog.checkpoint.com/exposure-management/the-2026-u-s-midterms-have-a-cyber-problem-but-its-not-at-the-ballot-box/](https://blog.checkpoint.com/exposure-management/the-2026-u-s-midterms-have-a-cyber-problem-but-its-not-at-the-ballot-box/)

生成摘要时出错

---

## 86. Nvidia RTX Spark

**原文标题**: Nvidia RTX Spark

**原文链接**: [https://www.nvidia.com/en-us/products/rtx-spark/](https://www.nvidia.com/en-us/products/rtx-spark/)

生成摘要时出错

---

## 87. Crystal Nights (2008)

**原文标题**: Crystal Nights (2008)

**原文链接**: [https://www.gregegan.net/MISC/CRYSTAL/Crystal.html](https://www.gregegan.net/MISC/CRYSTAL/Crystal.html)

生成摘要时出错

---

## 88. Debug Project

**原文标题**: Debug Project

**原文链接**: [https://debug.com/](https://debug.com/)

生成摘要时出错

---

## 89. Linux Basics for Hackers (2019)

**原文标题**: Linux Basics for Hackers (2019)

**原文链接**: [https://github.com/ahegazy0/linux-basics-for-hackers-notes](https://github.com/ahegazy0/linux-basics-for-hackers-notes)

生成摘要时出错

---

## 90. Microsoft builds MacBook Pro rival with NVIDIA-powered Surface Laptop Ultra

**原文标题**: Microsoft builds MacBook Pro rival with NVIDIA-powered Surface Laptop Ultra

**原文链接**: [https://www.windowslatest.com/2026/06/01/microsoft-builds-its-ultimate-macbook-pro-rival-with-the-nvidia-powered-surface-laptop-ultra/](https://www.windowslatest.com/2026/06/01/microsoft-builds-its-ultimate-macbook-pro-rival-with-the-nvidia-powered-surface-laptop-ultra/)

生成摘要时出错

---

## 91. Anthropic confidentially submits draft S-1 to the SEC

**原文标题**: Anthropic confidentially submits draft S-1 to the SEC

**原文链接**: [https://www.anthropic.com/news/confidential-draft-s1-sec](https://www.anthropic.com/news/confidential-draft-s1-sec)

生成摘要时出错

---

## 92. The Pirate Bay Remains Resilient, 20 Years After the Raid

**原文标题**: The Pirate Bay Remains Resilient, 20 Years After the Raid

**原文链接**: [https://torrentfreak.com/the-pirate-bay-remains-resilient-20-years-after-the-raid/](https://torrentfreak.com/the-pirate-bay-remains-resilient-20-years-after-the-raid/)

生成摘要时出错

---

## 93. Decades of Effort Restore Steelhead and Salmon Passage on Alameda Creek

**原文标题**: Decades of Effort Restore Steelhead and Salmon Passage on Alameda Creek

**原文链接**: [https://www.fisheries.noaa.gov/feature-story/decades-effort-restore-steelhead-and-salmon-passage-californias-alameda-creek](https://www.fisheries.noaa.gov/feature-story/decades-effort-restore-steelhead-and-salmon-passage-californias-alameda-creek)

生成摘要时出错

---

## 94. Tracing HTTP Requests with Go's net/HTTP/httptrace

**原文标题**: Tracing HTTP Requests with Go's net/HTTP/httptrace

**原文链接**: [https://blainsmith.com/articles/httptrace-with-go/](https://blainsmith.com/articles/httptrace-with-go/)

生成摘要时出错

---

## 95. AI Agent Guidelines for CS336 at Stanford

**原文标题**: AI Agent Guidelines for CS336 at Stanford

**原文链接**: [https://github.com/stanford-cs336/assignment1-basics/blob/main/CLAUDE.md](https://github.com/stanford-cs336/assignment1-basics/blob/main/CLAUDE.md)

生成摘要时出错

---

## 96. Malicious npm packages detected across Red Hat Cloud Services

**原文标题**: Malicious npm packages detected across Red Hat Cloud Services

**原文链接**: [https://github.com/RedHatInsights/javascript-clients/issues/492](https://github.com/RedHatInsights/javascript-clients/issues/492)

生成摘要时出错

---

## 97. A 10 year old Xeon is all you need

**原文标题**: A 10 year old Xeon is all you need

**原文链接**: [https://point.free/blog/gemma-4-on-a-2016-xeon/](https://point.free/blog/gemma-4-on-a-2016-xeon/)

生成摘要时出错

---

## 98. Stealing from Biologists to Compile Haskell Faster

**原文标题**: Stealing from Biologists to Compile Haskell Faster

**原文链接**: [https://www.iankduncan.com/engineering/2026-05-30-stealing-from-biologists-to-compile-haskell-faster/](https://www.iankduncan.com/engineering/2026-05-30-stealing-from-biologists-to-compile-haskell-faster/)

生成摘要时出错

---

## 99. What happens when companies replace managers with AI?

**原文标题**: What happens when companies replace managers with AI?

**原文链接**: [https://analysis.infocentral.net/replacing-managers-with-ai.html](https://analysis.infocentral.net/replacing-managers-with-ai.html)

生成摘要时出错

---

## 100. We benchmarked Google Cloud's $512 VM – the speed wasn't the interesting part

**原文标题**: We benchmarked Google Cloud's $512 VM – the speed wasn't the interesting part

**原文链接**: [https://webbynode.com/articles/google-cloud-512-vm-not-10x-faster-than-50-vm](https://webbynode.com/articles/google-cloud-512-vm-not-10x-faster-than-50-vm)

生成摘要时出错

---

