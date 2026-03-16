# Hacker News 热门文章摘要 (2026-03-16)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 凯文·布恩：“小众网络”比你想象的要大

**原文标题**: Kevin Boone: The "small web" is bigger than you might think

**原文链接**: [https://kevinboone.me/small_web_is_big.html](https://kevinboone.me/small_web_is_big.html)

在《凯文·布恩：“小众网络”比你想象的更庞大》一文中，作者探讨了“小众网络”（small web）的生命力——这是一个由不受企业跟踪和广告干扰的非商业性个人网站所组成的集合。

布恩首先将小众网络与 Gemini 协议进行了比较，后者是一个拥有约 6,000 个“胶囊”（capsules）且功能有限的小众社区。布恩指出，由于 Gemini 规模较小，通过单一的信息聚合器就能轻松追踪社区的所有更新。他想知道是否能为更广泛的小众网络构建类似的工具，以便集中查看个人博客的更新动态。

为了验证这一想法，布恩使用了 Kagi 搜索引擎“小众网络计划”提供的 32,000 个站点列表。他开发了一个程序，根据技术有效性和活跃度对这些站点进行筛选，剔除了已失效、缺失时间戳或每月更新不足一次的站点。这使名单缩小到了约 9,000 个活跃站点。

研究结果显示，这些站点在一天内产生了超过 1,200 条新内容更新。布恩总结道，虽然这种更新量让单页面聚合器变得不再可行，但它却是这一运动健康发展的积极信号。“小众网络”比他最初预想的要庞大且活跃得多，这证明了尽管商业平台占据主导地位，一个充满活力且不断壮大的私人、非商业表达生态系统仍在互联网上蓬勃发展。

---

## 2. 我的可靠且愉悦的本地语音助手探索之路

**原文标题**: My Journey to a reliable and enjoyable locally hosted voice assistant

**原文链接**: [https://community.home-assistant.io/t/my-journey-to-a-reliable-and-enjoyable-locally-hosted-voice-assistant/944860](https://community.home-assistant.io/t/my-journey-to-a-reliable-and-enjoyable-locally-hosted-voice-assistant/944860)

本文详细介绍了用户如何成功从 Google Home 迁移到基于 **llama.cpp** 的全本地 Home Assistant 语音助手。由于对商业助手日益下降的可靠性和隐私问题的担忧，作者构建了一个能够处理复杂工具、天气预报和媒体控制的高性能系统。

**关键技术组件：**
*   **硬件：** 该方案采用 MiniPC 搭配 **外置显卡（eGPU，如 RTX 3090 或 RX 7900XTX）** 来运行 20B–30B 参数的大语言模型，响应时间缩短至两秒以内。
*   **软件栈：** 为了获得更佳性能，作者从 Ollama 转向了 **llama.cpp**，并使用 **Wyoming OpenVINO** 实现语音转文本，以及使用 **Kokoro** 实现高质量文本转语音。
*   **模型选择：** 作者强调应使用来自 HuggingFace 的高量化 GGUF 模型，而非 Ollama 的默认模型，以确保工具调用和指令执行的可靠性。

**主要改进与经验：**
*   **提示词工程：** 作者发现详尽且结构化的提示词至关重要。通过与 ChatGPT 的迭代测试，他们不断优化指令，确保大模型在调用天气或网页搜索工具时，不会产生多余的“废话”或表情符号。
*   **混合方案：** 针对大模型表现欠佳的任务（如特定音乐播放），作者利用 Home Assistant 的**语句触发自动化**来弥补不足，将语音指令直接关联至 Music Assistant。
*   **个性化定制：** 为了提升“家庭接受度（WAF）”，作者使用 microWakeWord 训练了自定义唤醒词“Hey Robot”。

**结论：**
尽管作者承认该方案需要深厚的技术研究和专用硬件支持，但其最终打造出的私密、可靠且高度可定制的助手，在速度和功能上均超越了商业替代品。

---

## 3. Apideck CLI – 一款上下文消耗远低于 MCP 的 AI 代理接口

**原文标题**: Apideck CLI – An AI-agent interface with much lower context consumption than MCP

**原文链接**: [https://www.apideck.com/blog/mcp-server-eating-context-window-cli-alternative](https://www.apideck.com/blog/mcp-server-eating-context-window-cli-alternative)

本文探讨了模型上下文协议（MCP）固有的“上下文膨胀”问题。虽然 MCP 是目前连接 AI 智能体与工具的主流标准，但其对详尽 JSON 架构的依赖，可能在对话开始前就消耗掉模型 70% 以上的上下文窗口（例如超过 55,000 个 token）。

Apideck 提出了一种基于 CLI 的接口作为更高效的替代方案，其核心优势体现在以下三个方面：

1. **渐进式披露：** 智能体无需预先加载所有工具定义，而是接收一个极简（约 80 token）的系统提示。随后，它仅在需要时通过 `--help` 命令发现特定的 API 功能。与 MCP 相比，这种方法将 token 消耗降低了 4 到 32 倍，为推理和历史记录保留了更多上下文空间。
2. **结构化可靠性与安全性：** 基准测试显示，远程 MCP 服务器的连接失败率最高可达 28%，而 CLI 作为静态二进制文件在本地运行。此外，安全性在结构层面得到了加强：二进制文件本身会拦截危险操作（如 `DELETE`）或要求显式标识，这比单纯依赖提示词指令更加安全。
3. **通用兼容性：** 由于大多数智能体框架（如 Claude Code、Cursor 等）都支持 Shell 执行，CLI 集成无需任何协议开销或复杂的中间件。

**何时选择替代方案：**
作者承认，对于高频、低多样性的工具集或复杂的多租户 OAuth 场景，MCP 仍是更优选择。同样，直接执行代码更适合有状态的复杂工作流。然而，在处理广泛的 API 接口时，Apideck CLI 提供了一个务实的“平衡点”，通过最大限度减少管理性 token 的浪费，从而充分发挥模型的智能。

---

## 4. 我爱 FreeBSD

**原文标题**: I Love FreeBSD

**原文链接**: [https://it-notes.dragas.net/2026/03/16/why-i-love-freebsd/](https://it-notes.dragas.net/2026/03/16/why-i-love-freebsd/)

在本文中，作者回顾了与 FreeBSD 结缘二十年的历程，这段旅程始于 2002 年对《FreeBSD 手册》的发现。最初，作者被该手册卓越的质量和准确性所吸引，并发现 FreeBSD 所提供的成熟度、稳定性和性能均超越了当时的 Linux 发行版。

文章的核心主题是**“演进而非变革”**的哲学。作者赞扬 FreeBSD 优先考虑可预测性和一致性，而非盲目追逐行业热点。虽然作者最终在桌面端改用了 Mac，但 FreeBSD 仍然是其服务器和关键业务负载的首选。重点提到的技术特性包括：

*   **Jails：** 一种自 2000 年起便开始使用的原生、简单且安全的虚拟化机制。
*   **ZFS 集成：** 提供原生引导环境，实现安全、可逆的系统升级。
*   **性能：** 与 Linux 相比，在重负载下具有更优异的热管理和系统响应能力。
*   **可预测性：** 稳定的网络接口命名，以及“先理解，后行动”的系统设计理念。

除了技术优势，作者还强调了**社区的力量**。与许多由商业利益驱动的现代技术圈不同，FreeBSD 社区被描述为一个由“为人类而写作的人类”组成的充满激情且能力出众的群体。作者将这种协作、积极的环境归功于 FreeBSD 基金会以及来自 Netflix 等公司的工程师，这种环境促进了匠心精神，而非单纯的商业依赖。

最后，作者总结道，FreeBSD 的座右铭**“为服务而生”（The Power to Serve）**完美概括了它的价值：它是一个经久耐用、可靠且高性能的工具，并得到了一个对其使命深信不疑的社区的支持。

---

## 5. 证书颁发机构即日起开始检查 DNSSEC

**原文标题**: Cert Authorities Check for DNSSEC from Today

**原文链接**: [https://www.grepular.com/Cert_Authorities_Check_for_DNSSEC_From_Today](https://www.grepular.com/Cert_Authorities_Check_for_DNSSEC_From_Today)

从今天起，所有证书颁发机构（CA）必须正式对已启用 DNSSEC 的域名进行验证。这一要求既适用于 CAA（证书颁发机构授权）记录的查询，也适用于 ACME 协议执行过程中的 DNS 记录验证。

虽然许多 CA 可能在截止日期前已经实施了这些验证检查，但今后任何违规行为预计都将面临严厉的纪律处分。这一转变确保了 CA 在颁发证书前必须核实 DNS 响应的真实性，从而防止潜在的拦截或欺骗。

作者已使用 DNSSEC 超过 14 年，他强调了其可靠性，并鼓励域名所有者检查其注册商是否支持 DNSSEC。启用该功能通常过程简单，且能显著提升证书颁发过程中的域名安全与完整性。

---

## 6. 腐败在民主国家对社会信任的侵蚀程度高于专制国家。

**原文标题**: Corruption erodes social trust more in democracies than in autocracies

**原文链接**: [https://www.frontiersin.org/journals/political-science/articles/10.3389/fpos.2026.1779810/full](https://www.frontiersin.org/journals/political-science/articles/10.3389/fpos.2026.1779810/full)

这项由 Kimmo Eriksson 和 Irina Vartanova 发表在《政治科学前沿》（*Frontiers in Political Science*，2026）上的研究，探讨了腐败在民主政体和专制政体中对社会信任产生的不同影响。尽管在全球范围内，腐败通常与较低的社会信任度相关，但作者认为，由于两种心理机制的作用，民主国家更容易受到腐败的影响：

1.  **规范放大效应 (Normative Amplification)：** 由于民主制度建立在平等和公正的原则之上，腐败被视为对社会契约的根本性违背。相比之下，在专制国家，腐败往往在预料之中，并被视为一种常规的生存策略。
2.  **代表性传染 (Representative Contagion)：** 在民主国家，当选官员被视为“人民”的代表。当这些官员腐败时，选举他们的公民也会受到牵连，从而削弱了个体之间的横向信任。而在专制国家，精英阶层被视为一个独立的、掠夺性的阶级，这使得他们的不法行为与普通公民之间的社会信任“隔离开来”。

为了验证这些理论，研究人员对来自 62 个国家的数据进行了多层分析，将《世界价值观调查》（World Values Survey）中的个人层面调查结果与“民主多样性”（V-Dem）项目的国家层面指标相结合。

研究结果证实，虽然感知到的腐败几乎普遍预示着更低的普遍信任，但这种负相关性**在民主国家明显更强**。即使在控制了收入不平等和客观的国家腐败程度等因素后，这一结论依然成立。作者总结道，这就是“问责的代价”：正是使民主制度得以运行的透明和代表性规范，也使其社会资本更加脆弱。因此，民主国家的制度失效会在公民的社会世界观中产生更深层的共鸣，进而威胁到维持民主韧性所必需的合作。

---

## 7. Kaizen (YC P25) 招聘工程师、GTM 和幕僚长，致力于 BPO 自动化

**原文标题**: Kaizen (YC P25) Hiring Eng, GTM, Cos to Automate BPOs

**原文链接**: [https://www.kaizenautomation.com/careers](https://www.kaizenautomation.com/careers)

生成摘要时出错

---

## 8. 美国就业市场可视化工具

**原文标题**: US Job Market Visualizer

**原文链接**: [https://karpathy.ai/jobs/](https://karpathy.ai/jobs/)

The **US Job Market Visualizer** is an interactive research tool that maps 342 occupations—representing 143 million jobs—using data from the Bureau of Labor Statistics (BLS). It utilizes a treemap format where the area of each rectangle is proportional to total employment, allowing users to color-code the data by median pay, education requirements, projected growth, and "Digital AI Exposure."

A key feature of the tool is its **LLM-powered pipeline**, which allows users to generate custom scoring metrics. By writing specific prompts, users can task an AI to evaluate occupations based on criteria such as offshoring risk, climate impact, or robotics exposure. 

The **Digital AI Exposure** metric serves as a primary example, scoring jobs on a scale of 0 to 10. 
*   **Low Exposure (0–3):** Occupations requiring physical presence, manual skill, or unpredictable environments (e.g., roofers, electricians).
*   **High Exposure (8–10):** Roles that are primarily digital or involve routine information processing (e.g., software developers, data analysts).

The tool emphasizes that a high exposure score does not necessarily predict job loss. Instead, it indicates the degree to which AI will **reshape** the occupation. For example, while software developers are highly exposed, increased productivity could lead to higher demand rather than replacement. Ultimately, the visualizer is intended as a development tool for exploring economic data and the transformative potential of technology on the workforce.

---

## 9. Launch HN: Chamber (YC W26) – An AI Teammate for GPU Infrastructure

**原文标题**: Launch HN: Chamber (YC W26) – An AI Teammate for GPU Infrastructure

**原文链接**: [https://www.usechamber.io/](https://www.usechamber.io/)

生成摘要时出错

---

## 10. Canada's bill C-22 mandates mass metadata surveillance

**原文标题**: Canada's bill C-22 mandates mass metadata surveillance

**原文链接**: [https://www.michaelgeist.ca/2026/03/a-tale-of-two-bills-lawful-access-returns-with-changes-to-warrantless-access-but-dangerous-backdoor-surveillance-risks-remains/](https://www.michaelgeist.ca/2026/03/a-tale-of-two-bills-lawful-access-returns-with-changes-to-warrantless-access-but-dangerous-backdoor-surveillance-risks-remains/)

生成摘要时出错

---

## 11. Speed at the cost of quality: Study of use of Cursor AI in open source projects

**原文标题**: Speed at the cost of quality: Study of use of Cursor AI in open source projects

**原文链接**: [https://arxiv.org/abs/2511.04427](https://arxiv.org/abs/2511.04427)

生成摘要时出错

---

## 12. MoD sources warn Palantir role at heart of government is threat to UK security

**原文标题**: MoD sources warn Palantir role at heart of government is threat to UK security

**原文链接**: [https://www.thenerve.news/p/palantir-technologies-uk-mod-sources-government-data-insights-security-state-secrets](https://www.thenerve.news/p/palantir-technologies-uk-mod-sources-government-data-insights-security-state-secrets)

生成摘要时出错

---

## 13. 更快的 Asin() 就在我眼前

**原文标题**: Even Faster Asin() Was Staring Right at Me

**原文链接**: [https://16bpp.net/blog/post/even-faster-asin-was-staring-right-at-me/](https://16bpp.net/blog/post/even-faster-asin-was-staring-right-at-me/)

生成摘要时出错

---

## 14. Lazycut: A simple terminal video trimmer using FFmpeg

**原文标题**: Lazycut: A simple terminal video trimmer using FFmpeg

**原文链接**: [https://github.com/emin-ozata/lazycut](https://github.com/emin-ozata/lazycut)

生成摘要时出错

---

## 15. Comparing Python Type Checkers: Typing Spec Conformance

**原文标题**: Comparing Python Type Checkers: Typing Spec Conformance

**原文链接**: [https://pyrefly.org/blog/typing-conformance-comparison/](https://pyrefly.org/blog/typing-conformance-comparison/)

生成摘要时出错

---

## 16. Home Assistant waters my plants

**原文标题**: Home Assistant waters my plants

**原文链接**: [https://finnian.io/blog/home-assistant-waters-my-plants/](https://finnian.io/blog/home-assistant-waters-my-plants/)

生成摘要时出错

---

## 17. How I write software with LLMs

**原文标题**: How I write software with LLMs

**原文链接**: [https://www.stavros.io/posts/how-i-write-software-with-llms/](https://www.stavros.io/posts/how-i-write-software-with-llms/)

生成摘要时出错

---

## 18. Human Organ Atlas

**原文标题**: Human Organ Atlas

**原文链接**: [https://human-organ-atlas.esrf.fr/](https://human-organ-atlas.esrf.fr/)

生成摘要时出错

---

## 19. The 49MB web page

**原文标题**: The 49MB web page

**原文链接**: [https://thatshubham.com/blog/news-audit](https://thatshubham.com/blog/news-audit)

生成摘要时出错

---

## 20. On The Need For Understanding

**原文标题**: On The Need For Understanding

**原文链接**: [https://blog.information-superhighway.net/on-the-need-for-understanding](https://blog.information-superhighway.net/on-the-need-for-understanding)

生成摘要时出错

---

## 21. Event Publisher enables event integration between Keycloak and OpenFGA

**原文标题**: Event Publisher enables event integration between Keycloak and OpenFGA

**原文链接**: [https://github.com/embesozzi/keycloak-openfga-event-publisher](https://github.com/embesozzi/keycloak-openfga-event-publisher)

生成摘要时出错

---

## 22. Polymarket gamblers threaten to kill me over Iran missile story

**原文标题**: Polymarket gamblers threaten to kill me over Iran missile story

**原文链接**: [https://www.timesofisrael.com/gamblers-trying-to-win-a-bet-on-polymarket-are-vowing-to-kill-me-if-i-dont-rewrite-an-iran-missile-story/](https://www.timesofisrael.com/gamblers-trying-to-win-a-bet-on-polymarket-are-vowing-to-kill-me-if-i-dont-rewrite-an-iran-missile-story/)

生成摘要时出错

---

## 23. AirPods Max 2

**原文标题**: AirPods Max 2

**原文链接**: [https://www.apple.com/airpods-max/](https://www.apple.com/airpods-max/)

生成摘要时出错

---

## 24. 'Pokémon Go' players unknowingly trained delivery robots with 30B images

**原文标题**: 'Pokémon Go' players unknowingly trained delivery robots with 30B images

**原文链接**: [https://www.popsci.com/technology/pokemon-go-delivery-robots-crowdsourcing/](https://www.popsci.com/technology/pokemon-go-delivery-robots-crowdsourcing/)

生成摘要时出错

---

## 25. Chrome DevTools MCP (2025)

**原文标题**: Chrome DevTools MCP (2025)

**原文链接**: [https://developer.chrome.com/blog/chrome-devtools-mcp-debug-your-browser-session](https://developer.chrome.com/blog/chrome-devtools-mcp-debug-your-browser-session)

生成摘要时出错

---

## 26. Bringing Semiconductors to Kazakhstan

**原文标题**: Bringing Semiconductors to Kazakhstan

**原文链接**: [https://www.siliconimist.com/p/bringing-semiconductors-to-kazakhstan](https://www.siliconimist.com/p/bringing-semiconductors-to-kazakhstan)

生成摘要时出错

---

## 27. MM120, a pharmaceutical form of LSD, shown to reduce anxiety symptoms (2025)

**原文标题**: MM120, a pharmaceutical form of LSD, shown to reduce anxiety symptoms (2025)

**原文链接**: [https://www.sciencedaily.com/releases/2025/10/251027023816.htm](https://www.sciencedaily.com/releases/2025/10/251027023816.htm)

生成摘要时出错

---

## 28. Stop Sloppypasta

**原文标题**: Stop Sloppypasta

**原文链接**: [https://stopsloppypasta.ai/](https://stopsloppypasta.ai/)

生成摘要时出错

---

## 29. Six ingenious ways how Canon DSLRs used to illuminate their autofocus points

**原文标题**: Six ingenious ways how Canon DSLRs used to illuminate their autofocus points

**原文链接**: [https://exclusivearchitecture.com/03-technical-articles-CSDS-00-table-of-contents.html](https://exclusivearchitecture.com/03-technical-articles-CSDS-00-table-of-contents.html)

生成摘要时出错

---

## 30. Reviewing Large Changes with Jujutsu

**原文标题**: Reviewing Large Changes with Jujutsu

**原文链接**: [https://ben.gesoff.uk/posts/reviewing-large-changes-with-jj/](https://ben.gesoff.uk/posts/reviewing-large-changes-with-jj/)

生成摘要时出错

---

## 31. Why Are Viral Capsids Icosahedral?

**原文标题**: Why Are Viral Capsids Icosahedral?

**原文链接**: [https://www.asimov.press/p/viral-capsids](https://www.asimov.press/p/viral-capsids)

生成摘要时出错

---

## 32. Electric motor scaling laws and inertia in robot actuators

**原文标题**: Electric motor scaling laws and inertia in robot actuators

**原文链接**: [https://robot-daycare.com/posts/actuation_series_1/](https://robot-daycare.com/posts/actuation_series_1/)

生成摘要时出错

---

## 33. LLM Architecture Gallery

**原文标题**: LLM Architecture Gallery

**原文链接**: [https://sebastianraschka.com/llm-architecture-gallery/](https://sebastianraschka.com/llm-architecture-gallery/)

生成摘要时出错

---

## 34. What every computer scientist should know about floating-point arithmetic (1991) [pdf]

**原文标题**: What every computer scientist should know about floating-point arithmetic (1991) [pdf]

**原文链接**: [https://www.itu.dk/~sestoft/bachelor/IEEE754_article.pdf](https://www.itu.dk/~sestoft/bachelor/IEEE754_article.pdf)

生成摘要时出错

---

## 35. Autoresearch Hub

**原文标题**: Autoresearch Hub

**原文链接**: [http://autoresearchhub.com/](http://autoresearchhub.com/)

生成摘要时出错

---

## 36. LLMs can be exhausting

**原文标题**: LLMs can be exhausting

**原文链接**: [https://tomjohnell.com/llms-can-be-absolutely-exhausting/](https://tomjohnell.com/llms-can-be-absolutely-exhausting/)

生成摘要时出错

---

## 37. The Linux Programming Interface as a university course text

**原文标题**: The Linux Programming Interface as a university course text

**原文链接**: [https://man7.org/tlpi/academic/index.html](https://man7.org/tlpi/academic/index.html)

生成摘要时出错

---

## 38. Show HN: Sprinklz.io – An RSS reader with powerful algorithmic controls

**原文标题**: Show HN: Sprinklz.io – An RSS reader with powerful algorithmic controls

**原文链接**: [https://sprinklz.io](https://sprinklz.io)

生成摘要时出错

---

## 39. The emergence of print-on-demand Amazon paperback books

**原文标题**: The emergence of print-on-demand Amazon paperback books

**原文链接**: [https://www.alexerhardt.com/en/enshittification-amazon-paperback-books/](https://www.alexerhardt.com/en/enshittification-amazon-paperback-books/)

生成摘要时出错

---

## 40. Show HN: Hackerbrief – Top posts on Hacker News summarized daily

**原文标题**: Show HN: Hackerbrief – Top posts on Hacker News summarized daily

**原文链接**: [https://hackerbrief.vercel.app/](https://hackerbrief.vercel.app/)

生成摘要时出错

---

## 41. The Accidental Room (2018)

**原文标题**: The Accidental Room (2018)

**原文链接**: [https://99percentinvisible.org/episode/the-accidental-room/](https://99percentinvisible.org/episode/the-accidental-room/)

生成摘要时出错

---

## 42. How far can you go with IX Route Servers only?

**原文标题**: How far can you go with IX Route Servers only?

**原文链接**: [https://blog.benjojo.co.uk/post/how-far-can-you-get-with-ix-route-servers](https://blog.benjojo.co.uk/post/how-far-can-you-get-with-ix-route-servers)

生成摘要时出错

---

## 43. Which jobs are most vulnerable to AI?

**原文标题**: Which jobs are most vulnerable to AI?

**原文链接**: [https://www.washingtonpost.com/technology/interactive/2026/jobs-most-affected-ai-automation/](https://www.washingtonpost.com/technology/interactive/2026/jobs-most-affected-ai-automation/)

生成摘要时出错

---

## 44. A new Bigfoot documentary helps explain our conspiracy-minded era

**原文标题**: A new Bigfoot documentary helps explain our conspiracy-minded era

**原文链接**: [https://www.msn.com/en-us/news/us/a-new-bigfoot-documentary-helps-explain-our-conspiracy-minded-era/ar-AA1Yv6px](https://www.msn.com/en-us/news/us/a-new-bigfoot-documentary-helps-explain-our-conspiracy-minded-era/ar-AA1Yv6px)

生成摘要时出错

---

## 45. Obsession with growth is destroying nature, 150 countries warn

**原文标题**: Obsession with growth is destroying nature, 150 countries warn

**原文链接**: [https://www.politico.eu/article/obsession-with-growth-destroying-nature-150-countries-warn/](https://www.politico.eu/article/obsession-with-growth-destroying-nature-150-countries-warn/)

生成摘要时出错

---

## 46. SpiceCrypt: A Python library for decrypting LTspice encrypted model files

**原文标题**: SpiceCrypt: A Python library for decrypting LTspice encrypted model files

**原文链接**: [https://github.com/jtsylve/spice-crypt](https://github.com/jtsylve/spice-crypt)

生成摘要时出错

---

## 47. Schemesh – Unix shell and Lisp REPL, now with structured pipelines

**原文标题**: Schemesh – Unix shell and Lisp REPL, now with structured pipelines

**原文链接**: [https://github.com/cosmos72/schemesh/blob/main/README.md](https://github.com/cosmos72/schemesh/blob/main/README.md)

生成摘要时出错

---

## 48. Bandit: A 32bit baremetal computer that runs Color Forth [video]

**原文标题**: Bandit: A 32bit baremetal computer that runs Color Forth [video]

**原文链接**: [https://www.youtube.com/watch?v=HK0uAKkt0AE](https://www.youtube.com/watch?v=HK0uAKkt0AE)

生成摘要时出错

---

## 49. Things Linux Can Do That Windows Still Can't

**原文标题**: Things Linux Can Do That Windows Still Can't

**原文链接**: [https://itsfoss.com/things-linux-can-window-not/](https://itsfoss.com/things-linux-can-window-not/)

生成摘要时出错

---

## 50. Cannabinoids remove plaque-forming Alzheimer's proteins from brain cells (2016)

**原文标题**: Cannabinoids remove plaque-forming Alzheimer's proteins from brain cells (2016)

**原文链接**: [https://www.salk.edu/news-release/cannabinoids-remove-plaque-forming-alzheimers-proteins-from-brain-cells/](https://www.salk.edu/news-release/cannabinoids-remove-plaque-forming-alzheimers-proteins-from-brain-cells/)

生成摘要时出错

---

## 51. Apache Iggy: thread-per-core with io_uring in Rust

**原文标题**: Apache Iggy: thread-per-core with io_uring in Rust

**原文链接**: [https://iggy.apache.org/blogs/2026/02/27/thread-per-core-io_uring/](https://iggy.apache.org/blogs/2026/02/27/thread-per-core-io_uring/)

生成摘要时出错

---

## 52. Lies I was told about collaborative editing, Part 2: Why we don't use Yjs

**原文标题**: Lies I was told about collaborative editing, Part 2: Why we don't use Yjs

**原文链接**: [https://www.moment.dev/blog/lies-i-was-told-pt-2](https://www.moment.dev/blog/lies-i-was-told-pt-2)

生成摘要时出错

---

## 53. ASCII and Unicode quotation marks (2007)

**原文标题**: ASCII and Unicode quotation marks (2007)

**原文链接**: [https://www.cl.cam.ac.uk/~mgk25/ucs/quotes.html](https://www.cl.cam.ac.uk/~mgk25/ucs/quotes.html)

生成摘要时出错

---

## 54. 385TB video game archive saved by fans; torrents being generated

**原文标题**: 385TB video game archive saved by fans; torrents being generated

**原文链接**: [https://www.tomshardware.com/video-games/retro-gaming/385tb-video-game-archive-saved-by-fans-myrient-has-been-100-percent-backed-up-and-validated-torrents-being-generated](https://www.tomshardware.com/video-games/retro-gaming/385tb-video-game-archive-saved-by-fans-myrient-has-been-100-percent-backed-up-and-validated-torrents-being-generated)

生成摘要时出错

---

## 55. In Memoriam: John W. Addison, my PhD advisor

**原文标题**: In Memoriam: John W. Addison, my PhD advisor

**原文链接**: [https://billwadge.com/2026/03/15/in-memoriam-john-w-addison-jr-my-phd-advisor/](https://billwadge.com/2026/03/15/in-memoriam-john-w-addison-jr-my-phd-advisor/)

生成摘要时出错

---

## 56. Is this product 'human-made'? The race to establish an AI-free logo

**原文标题**: Is this product 'human-made'? The race to establish an AI-free logo

**原文链接**: [https://www.bbc.co.uk/news/articles/cj0d6el50ppo](https://www.bbc.co.uk/news/articles/cj0d6el50ppo)

生成摘要时出错

---

## 57. Nasdaq's Shame

**原文标题**: Nasdaq's Shame

**原文链接**: [https://keubiko.substack.com/p/nasdaqs-shame](https://keubiko.substack.com/p/nasdaqs-shame)

生成摘要时出错

---

## 58. Federal Right to Privacy Act – Draft legislation

**原文标题**: Federal Right to Privacy Act – Draft legislation

**原文链接**: [https://righttoprivacyact.github.io](https://righttoprivacyact.github.io)

生成摘要时出错

---

## 59. Malawi's solar boom is leaving a toxic legacy of lead waste

**原文标题**: Malawi's solar boom is leaving a toxic legacy of lead waste

**原文链接**: [https://news.mongabay.com/2026/02/malawis-solar-boom-is-leaving-a-toxic-legacy-of-lead-waste/](https://news.mongabay.com/2026/02/malawis-solar-boom-is-leaving-a-toxic-legacy-of-lead-waste/)

生成摘要时出错

---

## 60. Hollywood Enters Oscars Weekend in Existential Crisis

**原文标题**: Hollywood Enters Oscars Weekend in Existential Crisis

**原文链接**: [https://www.theculturenewspaper.com/hollywood-enters-oscars-weekend-in-existential-crisis/](https://www.theculturenewspaper.com/hollywood-enters-oscars-weekend-in-existential-crisis/)

生成摘要时出错

---

## 61. Show HN: GDSL – 800 line kernel: Lisp subset in 500, C subset in 1300

**原文标题**: Show HN: GDSL – 800 line kernel: Lisp subset in 500, C subset in 1300

**原文链接**: [https://firthemouse.github.io/](https://firthemouse.github.io/)

生成摘要时出错

---

## 62. Show HN: Signet – Autonomous wildfire tracking from satellite and weather data

**原文标题**: Show HN: Signet – Autonomous wildfire tracking from satellite and weather data

**原文链接**: [https://signet.watch](https://signet.watch)

生成摘要时出错

---

## 63. IBM, sonic delay lines, and the history of the 80×24 display (2019)

**原文标题**: IBM, sonic delay lines, and the history of the 80×24 display (2019)

**原文链接**: [https://www.righto.com/2019/11/ibm-sonic-delay-lines-and-history-of.html](https://www.righto.com/2019/11/ibm-sonic-delay-lines-and-history-of.html)

生成摘要时出错

---

## 64. In Search of Banksy

**原文标题**: In Search of Banksy

**原文链接**: [https://www.reuters.com/investigates/special-report/global-art-banksy/](https://www.reuters.com/investigates/special-report/global-art-banksy/)

生成摘要时出错

---

## 65. A Plain Anabaptist Story: The Hutterites

**原文标题**: A Plain Anabaptist Story: The Hutterites

**原文链接**: [https://ulmer457718.substack.com/p/a-plain-anabaptist-story-the-hutterites](https://ulmer457718.substack.com/p/a-plain-anabaptist-story-the-hutterites)

生成摘要时出错

---

## 66. Glassworm is back: A new wave of invisible Unicode attacks hits repositories

**原文标题**: Glassworm is back: A new wave of invisible Unicode attacks hits repositories

**原文链接**: [https://www.aikido.dev/blog/glassworm-returns-unicode-attack-github-npm-vscode](https://www.aikido.dev/blog/glassworm-returns-unicode-attack-github-npm-vscode)

生成摘要时出错

---

## 67. Kona EV Hacking

**原文标题**: Kona EV Hacking

**原文链接**: [http://techno-fandom.org/~hobbit/cars/ev/](http://techno-fandom.org/~hobbit/cars/ev/)

生成摘要时出错

---

## 68. Show HN: What if your synthesizer was powered by APL (or a dumb K clone)?

**原文标题**: Show HN: What if your synthesizer was powered by APL (or a dumb K clone)?

**原文链接**: [https://octetta.github.io/k-synth/](https://octetta.github.io/k-synth/)

生成摘要时出错

---

## 69. Linux 7.1 to Retire UDP-Lite – Allows for Better Performance with Cleansed Code

**原文标题**: Linux 7.1 to Retire UDP-Lite – Allows for Better Performance with Cleansed Code

**原文链接**: [https://www.phoronix.com/news/Linux-7.1-Retiring-UDP-Lite](https://www.phoronix.com/news/Linux-7.1-Retiring-UDP-Lite)

生成摘要时出错

---

## 70. Badreads

**原文标题**: Badreads

**原文链接**: [https://www.funnest.world/badreads](https://www.funnest.world/badreads)

生成摘要时出错

---

## 71. MCP is dead; long live MCP

**原文标题**: MCP is dead; long live MCP

**原文链接**: [https://chrlschn.dev/blog/2026/03/mcp-is-dead-long-live-mcp/](https://chrlschn.dev/blog/2026/03/mcp-is-dead-long-live-mcp/)

生成摘要时出错

---

## 72. Why the World Still Runs on SAP

**原文标题**: Why the World Still Runs on SAP

**原文链接**: [https://www.a16z.news/p/why-the-world-still-runs-on-sap](https://www.a16z.news/p/why-the-world-still-runs-on-sap)

生成摘要时出错

---

## 73. $96 3D-printed rocket that recalculates its mid-air trajectory using a $5 sensor

**原文标题**: $96 3D-printed rocket that recalculates its mid-air trajectory using a $5 sensor

**原文链接**: [https://github.com/novatic14/MANPADS-System-Launcher-and-Rocket](https://github.com/novatic14/MANPADS-System-Launcher-and-Rocket)

生成摘要时出错

---

## 74. Building a blog with Git-crypt for private posts in a public repo

**原文标题**: Building a blog with Git-crypt for private posts in a public repo

**原文链接**: [https://thobiasn.dev/posts/a-pragmatic-blog](https://thobiasn.dev/posts/a-pragmatic-blog)

生成摘要时出错

---

## 75. What makes Intel Optane stand out (2023)

**原文标题**: What makes Intel Optane stand out (2023)

**原文链接**: [https://blog.zuthof.nl/2023/06/02/what-makes-intel-optane-stand-out/](https://blog.zuthof.nl/2023/06/02/what-makes-intel-optane-stand-out/)

生成摘要时出错

---

## 76. Type systems are leaky abstractions: the case of Map.take!/2

**原文标题**: Type systems are leaky abstractions: the case of Map.take!/2

**原文链接**: [https://dashbit.co/blog/type-systems-are-leaky-abstractions-map-take](https://dashbit.co/blog/type-systems-are-leaky-abstractions-map-take)

生成摘要时出错

---

## 77. A Visual Introduction to Machine Learning (2015)

**原文标题**: A Visual Introduction to Machine Learning (2015)

**原文链接**: [https://r2d3.us/visual-intro-to-machine-learning-part-1/](https://r2d3.us/visual-intro-to-machine-learning-part-1/)

生成摘要时出错

---

## 78. Generating All 32-Bit Primes (Part I)

**原文标题**: Generating All 32-Bit Primes (Part I)

**原文链接**: [https://hnlyman.github.io/pages/prime32_I.html](https://hnlyman.github.io/pages/prime32_I.html)

生成摘要时出错

---

## 79. What is agentic engineering?

**原文标题**: What is agentic engineering?

**原文链接**: [https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/](https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/)

生成摘要时出错

---

## 80. Separating the Wayland compositor and window manager

**原文标题**: Separating the Wayland compositor and window manager

**原文链接**: [https://isaacfreund.com/blog/river-window-management/](https://isaacfreund.com/blog/river-window-management/)

生成摘要时出错

---

## 81. Rack-mount hydroponics

**原文标题**: Rack-mount hydroponics

**原文链接**: [https://sa.lj.am/rack-mount-hydroponics/](https://sa.lj.am/rack-mount-hydroponics/)

生成摘要时出错

---

## 82. Learning athletic humanoid tennis skills from imperfect human motion data

**原文标题**: Learning athletic humanoid tennis skills from imperfect human motion data

**原文链接**: [https://zzk273.github.io/LATENT/](https://zzk273.github.io/LATENT/)

生成摘要时出错

---

## 83. Human Organ Atlas

**原文标题**: Human Organ Atlas

**原文链接**: [https://www.science.org/doi/10.1126/sciadv.adz2240](https://www.science.org/doi/10.1126/sciadv.adz2240)

生成摘要时出错

---

## 84. 1M context is now generally available for Opus 4.6 and Sonnet 4.6

**原文标题**: 1M context is now generally available for Opus 4.6 and Sonnet 4.6

**原文链接**: [https://claude.com/blog/1m-context-ga](https://claude.com/blog/1m-context-ga)

生成摘要时出错

---

## 85. The 100 hour gap between a vibecoded prototype and a working product

**原文标题**: The 100 hour gap between a vibecoded prototype and a working product

**原文链接**: [https://kanfa.macbudkowski.com/vibecoding-cryptosaurus](https://kanfa.macbudkowski.com/vibecoding-cryptosaurus)

生成摘要时出错

---

## 86. Clock-accurate FPGA replacement for NES PPU

**原文标题**: Clock-accurate FPGA replacement for NES PPU

**原文链接**: [https://github.com/andkorzh/PPU-LITE](https://github.com/andkorzh/PPU-LITE)

生成摘要时出错

---

## 87. Animated 'Firefly' Reboot in Development from Nathan Fillion, 20th TV

**原文标题**: Animated 'Firefly' Reboot in Development from Nathan Fillion, 20th TV

**原文链接**: [https://www.hollywoodreporter.com/tv/tv-news/animated-firefly-reboot-in-development-nathan-fillion-1236533089/](https://www.hollywoodreporter.com/tv/tv-news/animated-firefly-reboot-in-development-nathan-fillion-1236533089/)

生成摘要时出错

---

## 88. NASA officials sidestepped questions on Artemis II risks–there's a reason why

**原文标题**: NASA officials sidestepped questions on Artemis II risks–there's a reason why

**原文链接**: [https://arstechnica.com/space/2026/03/flying-to-the-moon-for-the-first-time-in-54-years-is-risky-but-how-risky/](https://arstechnica.com/space/2026/03/flying-to-the-moon-for-the-first-time-in-54-years-is-risky-but-how-risky/)

生成摘要时出错

---

## 89. An experiment to use GitHub Actions as a control plane for a PaaS

**原文标题**: An experiment to use GitHub Actions as a control plane for a PaaS

**原文链接**: [https://towlion.github.io](https://towlion.github.io)

生成摘要时出错

---

## 90. Mathematics Distillation Challenge – Equational Theories

**原文标题**: Mathematics Distillation Challenge – Equational Theories

**原文链接**: [https://terrytao.wordpress.com/2026/03/13/mathematics-distillation-challenge-equational-theories/](https://terrytao.wordpress.com/2026/03/13/mathematics-distillation-challenge-equational-theories/)

生成摘要时出错

---

## 91. OpenJarvis: Personal AI, on Personal Devices

**原文标题**: OpenJarvis: Personal AI, on Personal Devices

**原文链接**: [https://scalingintelligence.stanford.edu/blogs/openjarvis/](https://scalingintelligence.stanford.edu/blogs/openjarvis/)

生成摘要时出错

---

## 92. How kernel anti-cheats work

**原文标题**: How kernel anti-cheats work

**原文链接**: [https://s4dbrd.github.io/posts/how-kernel-anti-cheats-work/](https://s4dbrd.github.io/posts/how-kernel-anti-cheats-work/)

生成摘要时出错

---

## 93. The Blade Runner File: A Usenet Debate (1989)

**原文标题**: The Blade Runner File: A Usenet Debate (1989)

**原文链接**: [https://scribble.com/uwi/br/br-file.html](https://scribble.com/uwi/br/br-file.html)

生成摘要时出错

---

## 94. Can I run AI locally?

**原文标题**: Can I run AI locally?

**原文链接**: [https://www.canirun.ai/](https://www.canirun.ai/)

生成摘要时出错

---

## 95. Demos of 2025 from the Demoscene

**原文标题**: Demos of 2025 from the Demoscene

**原文链接**: [https://laurent.le-brun.eu/blog/the-best-demos-of-2025-from-the-demoscene](https://laurent.le-brun.eu/blog/the-best-demos-of-2025-from-the-demoscene)

生成摘要时出错

---

## 96. Civic opinion sharing to promote democracy

**原文标题**: Civic opinion sharing to promote democracy

**原文链接**: [https://www.ourpublicvoice.org/](https://www.ourpublicvoice.org/)

生成摘要时出错

---

## 97. The Iran war may be about to escalate

**原文标题**: The Iran war may be about to escalate

**原文链接**: [https://www.economist.com/middle-east-and-africa/2026/03/15/the-iran-war-may-be-about-to-escalate](https://www.economist.com/middle-east-and-africa/2026/03/15/the-iran-war-may-be-about-to-escalate)

生成摘要时出错

---

## 98. SH4ZAM – Fast Math Library for the Sega Dreamcast's SH4 CPU

**原文标题**: SH4ZAM – Fast Math Library for the Sega Dreamcast's SH4 CPU

**原文链接**: [https://github.com/gyrovorbis/sh4zam](https://github.com/gyrovorbis/sh4zam)

生成摘要时出错

---

## 99. Grandparents are glued to their phones [video]

**原文标题**: Grandparents are glued to their phones [video]

**原文链接**: [https://www.bbc.com/reel/video/p0n61dg3/grandparents-are-glued-to-their-phones-families-are-worried](https://www.bbc.com/reel/video/p0n61dg3/grandparents-are-glued-to-their-phones-families-are-worried)

生成摘要时出错

---

## 100. Allow me to get to know you, mistakes and all

**原文标题**: Allow me to get to know you, mistakes and all

**原文链接**: [https://sebi.io/posts/2026-03-14-allow-me-to-get-to-know-you-mistakes-and-all/](https://sebi.io/posts/2026-03-14-allow-me-to-get-to-know-you-mistakes-and-all/)

生成摘要时出错

---

