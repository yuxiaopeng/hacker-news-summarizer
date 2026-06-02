# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-06-02.md)

*最后自动更新时间: 2026-06-02 20:31:47*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 2 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 3 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 4 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 5 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 6 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 7 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 8 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 9 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 10 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 11 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 12 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 13 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 14 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 15 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 16 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 17 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 18 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 19 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 20 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 21 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 22 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 23 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 24 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 25 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 26 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 27 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 28 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 29 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 30 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 31 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 32 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 33 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 34 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 35 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 36 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 37 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 38 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 39 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 40 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 41 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 42 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 43 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 44 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 45 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 46 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 47 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 48 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 49 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 50 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 51 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 52 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 53 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 54 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 55 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 56 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 57 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 58 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 59 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 60 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 61 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 62 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 63 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 64 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 65 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 66 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 67 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 68 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 69 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 70 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 71 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 72 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 73 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 74 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 75 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 76 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 77 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 78 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 79 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 80 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 81 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 82 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 83 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 84 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 85 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 86 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 87 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 88 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 89 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 90 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 91 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 92 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 93 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 94 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 95 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 96 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 97 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 98 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 99 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 100 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 101 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 102 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 103 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 104 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 105 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 106 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 107 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 108 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 109 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 110 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 111 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 112 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 113 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 114 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 115 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 116 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 117 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 118 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 119 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 120 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 121 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 122 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 123 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 124 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 125 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 126 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 127 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 128 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 129 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 130 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 131 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 132 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 133 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 134 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 135 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 136 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 137 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 138 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 139 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 140 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 141 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 142 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 143 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 144 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 145 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 146 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 147 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 148 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 149 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 150 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 151 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 152 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 153 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 154 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 155 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 156 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 157 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 158 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 159 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 160 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 161 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 162 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 163 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 164 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 165 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 166 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 167 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 168 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 169 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 170 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 171 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 172 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 173 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 174 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 175 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 176 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 177 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 178 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 179 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 180 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 181 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 182 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 183 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 184 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 185 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 186 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 187 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 188 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 189 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 190 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 191 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 192 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 193 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 194 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 195 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 196 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 197 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 198 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 199 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 200 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 201 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 202 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 203 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 204 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 205 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 206 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 207 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 208 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 209 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 210 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 211 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 212 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 213 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 214 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 215 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 216 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 217 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 218 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 219 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 220 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 221 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 222 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 223 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 224 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 225 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 226 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 227 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 228 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 229 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 230 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 231 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 232 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 233 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 234 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 235 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 236 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 237 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 238 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 239 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 240 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 241 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 242 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 243 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 244 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 245 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 246 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 247 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 248 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 249 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 250 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 251 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 252 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 253 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 254 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 255 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 256 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 257 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 258 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 259 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 260 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 261 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 262 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 263 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 264 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 265 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 266 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 267 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 268 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 269 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 270 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 271 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 272 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 273 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 274 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 275 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 276 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 277 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 278 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 279 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 280 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 281 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 282 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 283 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 284 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 285 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 286 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 287 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 288 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 289 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 290 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 291 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 292 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 293 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 294 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 295 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 296 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 297 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 298 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 299 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 300 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 301 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 302 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 303 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 304 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 305 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 306 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 307 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 308 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 309 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 310 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 311 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 312 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 313 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 314 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 315 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 316 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 317 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 318 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 319 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 320 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 321 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 322 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 323 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 324 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 325 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 326 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 327 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 328 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 329 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 330 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 331 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 332 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 333 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 334 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 335 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 336 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 337 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 338 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 339 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 340 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 341 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 342 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 343 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 344 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 345 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 346 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 347 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 348 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 349 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 350 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 351 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 352 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 353 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 354 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 355 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 356 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 357 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 358 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 359 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 360 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 361 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 362 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 363 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 364 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 365 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 366 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 367 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 368 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 369 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 370 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 371 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 372 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 373 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 374 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 375 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 376 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 377 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 378 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 379 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 380 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 381 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 382 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 383 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 384 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 385 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 386 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 387 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 388 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 389 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 390 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 391 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 392 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 393 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 394 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 395 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 396 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 397 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 398 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 399 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 400 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 401 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 402 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 403 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 404 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 405 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 406 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 407 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 408 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 409 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 410 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 411 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 412 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 413 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 414 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 415 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 416 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 417 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 418 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 419 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 420 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 421 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 422 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 423 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 424 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 425 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 426 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 427 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 428 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 429 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 430 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 431 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 432 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 433 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 434 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 435 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 436 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 437 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 438 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 439 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
