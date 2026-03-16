# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-03-16.md)

*最后自动更新时间: 2026-03-16 18:25:17*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 2 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 3 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 4 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 5 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 6 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 7 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 8 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 9 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 10 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 11 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 12 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 13 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 14 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 15 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 16 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 17 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 18 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 19 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 20 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 21 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 22 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 23 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 24 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 25 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 26 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 27 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 28 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 29 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 30 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 31 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 32 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 33 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 34 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 35 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 36 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 37 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 38 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 39 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 40 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 41 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 42 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 43 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 44 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 45 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 46 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 47 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 48 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 49 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 50 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 51 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 52 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 53 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 54 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 55 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 56 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 57 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 58 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 59 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 60 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 61 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 62 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 63 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 64 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 65 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 66 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 67 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 68 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 69 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 70 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 71 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 72 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 73 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 74 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 75 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 76 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 77 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 78 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 79 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 80 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 81 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 82 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 83 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 84 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 85 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 86 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 87 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 88 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 89 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 90 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 91 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 92 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 93 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 94 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 95 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 96 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 97 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 98 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 99 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 100 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 101 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 102 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 103 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 104 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 105 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 106 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 107 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 108 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 109 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 110 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 111 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 112 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 113 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 114 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 115 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 116 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 117 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 118 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 119 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 120 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 121 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 122 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 123 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 124 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 125 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 126 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 127 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 128 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 129 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 130 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 131 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 132 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 133 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 134 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 135 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 136 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 137 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 138 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 139 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 140 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 141 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 142 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 143 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 144 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 145 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 146 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 147 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 148 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 149 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 150 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 151 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 152 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 153 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 154 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 155 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 156 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 157 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 158 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 159 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 160 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 161 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 162 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 163 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 164 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 165 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 166 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 167 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 168 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 169 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 170 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 171 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 172 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 173 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 174 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 175 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 176 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 177 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 178 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 179 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 180 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 181 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 182 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 183 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 184 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 185 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 186 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 187 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 188 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 189 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 190 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 191 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 192 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 193 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 194 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 195 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 196 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 197 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 198 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 199 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 200 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 201 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 202 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 203 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 204 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 205 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 206 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 207 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 208 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 209 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 210 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 211 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 212 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 213 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 214 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 215 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 216 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 217 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 218 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 219 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 220 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 221 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 222 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 223 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 224 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 225 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 226 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 227 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 228 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 229 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 230 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 231 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 232 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 233 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 234 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 235 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 236 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 237 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 238 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 239 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 240 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 241 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 242 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 243 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 244 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 245 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 246 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 247 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 248 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 249 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 250 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 251 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 252 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 253 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 254 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 255 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 256 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 257 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 258 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 259 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 260 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 261 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 262 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 263 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 264 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 265 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 266 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 267 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 268 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 269 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 270 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 271 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 272 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 273 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 274 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 275 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 276 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 277 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 278 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 279 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 280 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 281 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 282 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 283 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 284 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 285 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 286 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 287 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 288 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 289 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 290 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 291 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 292 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 293 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 294 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 295 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 296 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 297 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 298 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 299 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 300 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 301 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 302 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 303 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 304 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 305 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 306 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 307 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 308 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 309 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 310 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 311 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 312 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 313 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 314 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 315 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 316 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 317 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 318 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 319 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 320 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 321 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 322 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 323 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 324 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 325 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 326 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 327 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 328 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 329 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 330 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 331 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 332 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 333 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 334 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 335 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 336 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 337 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 338 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 339 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 340 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 341 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 342 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 343 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 344 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 345 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 346 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 347 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 348 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 349 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 350 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 351 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 352 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 353 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 354 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 355 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 356 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 357 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 358 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 359 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 360 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 361 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
