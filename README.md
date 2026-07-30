# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-07-30.md)

*最后自动更新时间: 2026-07-30 18:53:38*
## 1. 玻璃荒

**原文标题**: The Glass Famine

**原文链接**: [https://edconway.substack.com/p/the-glass-famine](https://edconway.substack.com/p/the-glass-famine)

在《玻璃饥荒》中，埃德·康威（Ed Conway）探讨了全球技术供应链中一个关键但被忽视的脆弱环节：世界对高纯度石英（HPQ）的依赖。虽然沙子随处可见，但制造半导体、太阳能电池板和光纤所需的特定超纯石英却极其稀有。

文章的焦点是北卡罗来纳州的小镇斯普鲁斯派恩（Spruce Pine），那里拥有世界上最重要的矿床。由于独特的地质条件，斯普鲁斯派恩提供了全球唯一纯度足以制造硅精炼坩埚的石英。这些坩埚对于生长单晶硅锭至关重要，而单晶硅锭正是切割成计算机芯片的原材料。如果没有这种特定的石英，现代电子产品的生产将实际上陷入停滞。

康威强调了全球经济中一个可怕的“单点故障”。目前，斯普鲁斯派恩的两家公司——西贝尔科（Sibelco）和奎茨沃克集团（The Quarzwerke Group）控制着绝大部分供应。尽管人们曾尝试寻找替代矿床或研发合成版本，但尚未有任何方案能与北卡罗来纳州矿山的规模、质量和成本效益相媲美。

文章将这场现代危机置于玻璃制造的宏大历史背景中，指出尽管玻璃曾彻底改变了科学和光学领域，但其最高纯度的形式现在却成了数字时代的瓶颈。康威得出结论，我们最先进的技术正摇摇欲坠地维系在一个单一的地质奇迹之上，这反映了现代文明物质基础的脆弱性。阿巴拉契亚这个小小角落的任何动荡，都将引发一场比近期半导体短缺严重得多的全球技术“饥荒”。

---

## 2. CosmosEscape：接管 Azure Cosmos DB 中的所有数据库

**原文标题**: CosmosEscape: Taking over Every Database in Azure Cosmos DB

**原文链接**: [https://www.wiz.io/blog/cosmosescape-taking-over-every-database-in-azure-cosmos-db](https://www.wiz.io/blog/cosmosescape-taking-over-every-database-in-azure-cosmos-db)

Wiz Research 最近披露了 **CosmosEscape**，这是 Azure Cosmos DB Gremlin API 中的一个关键（现已修复）漏洞。该漏洞可能允许攻击者入侵该平台上的任何数据库。

该漏洞源于将查询转换为 .NET 代码的 Gremlin 查询引擎。研究人员发现，该引擎的沙盒未能充分限制 **.NET 反射**，使他们能够在 **DB Gateway**（一种处理客户查询的多租户服务）上实现任意代码执行。

通过在网关上获得代码执行权限，研究人员识别出了 **“Cosmos 主密钥” (Cosmos Master Key)**，这是一种平台范围的签名密钥。该密钥赋予了两种高影响力的能力：
1.  **接管：** 能够检索任何 Cosmos DB 账户的主密钥，从而获得对其数据的完整读写访问权限。
2.  **枚举：** 访问“配置库” (Config Store)，这是一个包含每个账户元数据的区域注册库，使攻击者能够通过订阅或租户 ID 针对特定组织。

该漏洞的影响延伸到了微软的内部基础设施，因为 Microsoft Teams、Entra ID 和 Copilot 等服务均使用 Cosmos DB。此外，由于 DB Gateway 负责管理网络隔离，该漏洞还可以绕过私有网络保护。

**解决方案：**
微软已通过移除 Cosmos 主密钥并迁移到具有改进的服务间身份验证的加固架构，全面修复了该问题。微软的调查未发现恶意利用的证据，客户无需采取任何行动。

---

## 3. 支持流式传输与工具调用的 Go 语言 LLM SDK（及前端 React 库）

**原文标题**: Go LLM SDK for streaming, tool-calling AI backends (plus frontend React lib)

**原文链接**: [https://github.com/grafana/ai-sdk](https://github.com/grafana/ai-sdk)

Grafana 的 **Go LLM SDK** 是一个旨在利用 Go 语言构建 AI 驱动后端的库。它为模型交互、响应流式传输和多步工具执行提供了一套统一的 API。该 SDK 的一大亮点是它在传输协议上与 Vercel 的 AI SDK 兼容；这使得 Go 后端能够直接将服务器发送事件 (SSE) 流式传输到常用的 React 前端 Hook（如 `useChat` 和 `useCompletion`），而无需任何协议适配器。

**核心特性与功能：**
*   **统一的供应商支持：** 通过单一接口调用多个 LLM 供应商，包括 Anthropic、OpenAI、Amazon Bedrock 以及兼容 OpenAI 的 API。
*   **流式传输与生成：** 支持 `StreamText` 和 `GenerateText` 函数，具备内置重试机制和多步智能体 (Agent) 逻辑。
*   **可组合工具：** 允许模型调用纯 Go 函数，并可针对高风险操作设置可选的人工审批步骤。
*   **结构化输出：** 直接从模型生成经过 Schema 验证的对象、数组和选项。
*   **生产就绪：** 包含必要的企业级控制功能，如超时设置、降级逻辑、日志中间件、Prometheus 指标以及智能体可观测性。

**集成与理念：**
该 SDK 专为希望使用 Go 替换或补充 TypeScript 后端，同时保持无缝 React 前端体验的开发者而设计。它遵循 Vercel AI SDK 的设计模式，并采用 Apache 2.0 协议授权。

开发者可以通过安装核心模块 (`github.com/grafana/ai-sdk`) 及其首选的供应商模块来开始使用。该 SDK 强调“规范驱动开发”，确保与已确立的 AI 通信协议行业标准保持一致。

---

## 4. 纽约市执行新法后，外卖员小费收入增加1.04亿美元。

**原文标题**: Delivery workers made $104M more in tips after NYC began enforcing new law

**原文链接**: [https://www.nydailynews.com/2026/07/29/delivery-workers-made-104-million-more-in-tips-after-city-began-enforcing-new-law-mamdani/](https://www.nydailynews.com/2026/07/29/delivery-workers-made-104-million-more-in-tips-after-city-began-enforcing-new-law-mamdani/)

市长马姆达尼（Mamdani）宣布，在针对外送平台“误导性”小费做法的法律强制执行后，纽约市外送员额外赚取了1.04亿美元的小费。这一增长意味着全市7万名外送员每人每年的收入约增加2,287美元。

该立法要求Uber Eats和DoorDash等应用程序在结账时提供小费选项。此前，为应对纽约市22.13美元的时薪最低工资规定，这些公司将小费提示移至交易末尾（即送货完成后）。市府官员认为，这种转变刻意抑制了外送员的收入，声称这导致工人损失了约5.5亿美元的小费。尽管相关平台试图在联邦法院阻止这一结账要求，但其挑战被驳回，法律已于1月开始强制执行。

根据消费者和劳工保护局（DCWP）的一份报告，自该法律生效以来，每单外卖的平均小费翻了一番。DCWP局长萨姆·莱文（Sam Levine）指出，数据证明，尽管平台此前有所说辞，但纽约人仍愿意支持外送员。此外，报告显示外送行业依然发展强劲，与实施最低工资标准之前相比，餐厅每周订单量激增了70多万份。

尽管新法成功提高了收入，但市府官员指出，平均小费水平仍低于2023年11月的水平，即平台最初更改界面并移动小费选项之前的时期。

---

## 5. You can't solve computer use by ignoring the interface

**原文标题**: You can't solve computer use by ignoring the interface

**原文链接**: [https://steelmanlabs.com/blog/computer-use-is-far-from-solved](https://steelmanlabs.com/blog/computer-use-is-far-from-solved)

Despite the success of LLMs in coding and chat, agentic computer use remains a major hurdle. On realistic benchmarks like OSWorld-V2, completion rates for top models peak at only 20.6%. Steelman Labs argues that current approaches have hit a wall because they rely on "cushioned" environments and fail to address the core mechanics of interface interaction.

The article identifies a "core flaw": modern agents avoid using interfaces altogether. Instead of clicking buttons or filling forms, frontier models often bypass the UI by injecting JavaScript, reverse-engineering internal APIs, or writing custom scripts. This happens because these trillion-parameter models lack the basic motor control and real-time perception that humans use instinctively. 

This leads to a massive misallocation of compute. Agents spend the majority of their action budget on low-level visual grounding and tool-use overhead rather than high-level planning, reasoning, or error recovery. Furthermore, the standard "screenshot–toolcall" loop is too slow and misses the temporal information necessary to navigate dynamic real-world software.

Steelman Labs asserts that simply increasing model size or token limits will not solve the problem. Instead, they propose a paradigm shift: separating high-level planning from low-level execution. By introducing a "System 1" for agents—a dedicated manipulator for motor control and real-time vision-first perception—AI can interact with any interface a human can. This allows the primary reasoning model to focus on the task at hand, leading to faster, cheaper, and more reliable computer use.

---

## 6. The first watch featuring computer functions

**原文标题**: The first watch featuring computer functions

**原文链接**: [https://by.seiko-design.com/140th/en/topic/58.html](https://by.seiko-design.com/140th/en/topic/58.html)

生成摘要时出错

---

## 7. Agent-Manager: A Tmux TUI for Running Claude Code, Codex and OpenCode

**原文标题**: Agent-Manager: A Tmux TUI for Running Claude Code, Codex and OpenCode

**原文链接**: [https://github.com/YoanWai/agent-manager](https://github.com/YoanWai/agent-manager)

生成摘要时出错

---

## 8. Atomarine: Nuclear Data Centers at Sea

**原文标题**: Atomarine: Nuclear Data Centers at Sea

**原文链接**: [https://atomarine.co/](https://atomarine.co/)

生成摘要时出错

---

## 9. Reversing Abstractions: An Existential Crisis

**原文标题**: Reversing Abstractions: An Existential Crisis

**原文链接**: [https://www.humprog.org/~stephen/blog/research/recovering-abstraction.html](https://www.humprog.org/~stephen/blog/research/recovering-abstraction.html)

生成摘要时出错

---

## 10. AI's top startups are barely publishing their research

**原文标题**: AI's top startups are barely publishing their research

**原文链接**: [https://www.science.org/content/article/ai-s-top-startups-are-barely-publishing-their-research](https://www.science.org/content/article/ai-s-top-startups-are-barely-publishing-their-research)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 2 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 3 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 4 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 5 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 6 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 7 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 8 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 9 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 10 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 11 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 12 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 13 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 14 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 15 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 16 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 17 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 18 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 19 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 20 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 21 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 22 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 23 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 24 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 25 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 26 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 27 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 28 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 29 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 30 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 31 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 32 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 33 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 34 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 35 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 36 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 37 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 38 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 39 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 40 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 41 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 42 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 43 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 44 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 45 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 46 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 47 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 48 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 49 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 50 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 51 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 52 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 53 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 54 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 55 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 56 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 57 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 58 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 59 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 60 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 61 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 62 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 63 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 64 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 65 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 66 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 67 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 68 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 69 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 70 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 71 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 72 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 73 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 74 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 75 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 76 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 77 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 78 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 79 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 80 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 81 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 82 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 83 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 84 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 85 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 86 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 87 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 88 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 89 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 90 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 91 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 92 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 93 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 94 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 95 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 96 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 97 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 98 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 99 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 100 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 101 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 102 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 103 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 104 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 105 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 106 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 107 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 108 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 109 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 110 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 111 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 112 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 113 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 114 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 115 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 116 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 117 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 118 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 119 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 120 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 121 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 122 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 123 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 124 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 125 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 126 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 127 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 128 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 129 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 130 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 131 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 132 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 133 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 134 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 135 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 136 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 137 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 138 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 139 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 140 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 141 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 142 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 143 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 144 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 145 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 146 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 147 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 148 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 149 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 150 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 151 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 152 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 153 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 154 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 155 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 156 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 157 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 158 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 159 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 160 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 161 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 162 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 163 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 164 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 165 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 166 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 167 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 168 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 169 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 170 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 171 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 172 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 173 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 174 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 175 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 176 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 177 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 178 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 179 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 180 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 181 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 182 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 183 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 184 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 185 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 186 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 187 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 188 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 189 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 190 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 191 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 192 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 193 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 194 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 195 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 196 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 197 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 198 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 199 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 200 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 201 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 202 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 203 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 204 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 205 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 206 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 207 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 208 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 209 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 210 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 211 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 212 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 213 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 214 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 215 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 216 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 217 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 218 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 219 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 220 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 221 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 222 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 223 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 224 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 225 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 226 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 227 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 228 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 229 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 230 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 231 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 232 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 233 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 234 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 235 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 236 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 237 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 238 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 239 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 240 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 241 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 242 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 243 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 244 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 245 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 246 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 247 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 248 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 249 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 250 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 251 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 252 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 253 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 254 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 255 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 256 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 257 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 258 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 259 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 260 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 261 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 262 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 263 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 264 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 265 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 266 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 267 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 268 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 269 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 270 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 271 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 272 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 273 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 274 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 275 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 276 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 277 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 278 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 279 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 280 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 281 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 282 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 283 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 284 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 285 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 286 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 287 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 288 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 289 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 290 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 291 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 292 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 293 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 294 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 295 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 296 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 297 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 298 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 299 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 300 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 301 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 302 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 303 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 304 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 305 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 306 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 307 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 308 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 309 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 310 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 311 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 312 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 313 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 314 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 315 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 316 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 317 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 318 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 319 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 320 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 321 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 322 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 323 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 324 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 325 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 326 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 327 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 328 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 329 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 330 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 331 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 332 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 333 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 334 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 335 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 336 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 337 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 338 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 339 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 340 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 341 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 342 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 343 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 344 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 345 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 346 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 347 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 348 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 349 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 350 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 351 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 352 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 353 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 354 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 355 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 356 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 357 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 358 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 359 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 360 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 361 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 362 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 363 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 364 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 365 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 366 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 367 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 368 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 369 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 370 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 371 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 372 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 373 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 374 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 375 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 376 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 377 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 378 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 379 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 380 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 381 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 382 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 383 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 384 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 385 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 386 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 387 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 388 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 389 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 390 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 391 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 392 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 393 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 394 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 395 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 396 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 397 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 398 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 399 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 400 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 401 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 402 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 403 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 404 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 405 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 406 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 407 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 408 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 409 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 410 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 411 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 412 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 413 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 414 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 415 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 416 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 417 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 418 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 419 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 420 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 421 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 422 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 423 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 424 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 425 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 426 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 427 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 428 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 429 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 430 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 431 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 432 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 433 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 434 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 435 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 436 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 437 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 438 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 439 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 440 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 441 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 442 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 443 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 444 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 445 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 446 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 447 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 448 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 449 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 450 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 451 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 452 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 453 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 454 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 455 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 456 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 457 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 458 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 459 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 460 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 461 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 462 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 463 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 464 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 465 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 466 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 467 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 468 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 469 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 470 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 471 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 472 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 473 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 474 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 475 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 476 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 477 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 478 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 479 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 480 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 481 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 482 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 483 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 484 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 485 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 486 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 487 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 488 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 489 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 490 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 491 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 492 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 493 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 494 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 495 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 496 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 497 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
