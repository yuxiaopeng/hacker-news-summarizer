# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-01.md)

*最后自动更新时间: 2026-04-01 18:19:26*
## 1. EmDash —— 解决插件安全问题的 WordPress 精神续作

**原文标题**: EmDash – a spiritual successor to WordPress that solves plugin security

**原文链接**: [https://blog.cloudflare.com/emdash-wordpress/](https://blog.cloudflare.com/emdash-wordpress/)

EmDash 是一款开源且遵循 MIT 协议的 CMS，被定位为 WordPress 的“精神继承者”。它利用 AI 编程助手开发，旨在通过从传统的 PHP 架构转向基于 TypeScript 和 Astro Web 框架的无服务器原生平台，实现 Web 发布领域的现代化。

文章强调了以下几项关键创新：

*   **插件安全**：EmDash 通过将插件沙箱化在隔离的 **Dynamic Workers**（v8 隔离实例）中，解决了 WordPress 的主要安全漏洞。插件必须在清单文件中明确声明所需的“能力”（如邮件访问、内容读取），从而防止它们在未经许可的情况下访问文件系统或数据库。
*   **许可与市场**：通过将插件执行与核心代码解耦，EmDash 允许开发者为其插件使用任何许可协议，摆脱了 WordPress 严格的 GPL 限制。这降低了“市场锁定”效应，并鼓励建立更开放的生态系统。
*   **AI 原生特性**：该 CMS 专为 AI 代理的程序化管理而设计。它内置了**模型上下文协议 (MCP) 服务端**、CLI 以及“代理技能”，为 AI 执行迁移、自定义模式 (Schema) 和管理内容提供必要的上下文。
*   **原生货币化**：EmDash 内置支持 **x402 标准**，允许发布者通过微支付对内容收费。这一设计专门面向“AI 时代”，届时数据的主要消费者可能是 AI 代理而非人类。
*   **无服务器架构**：EmDash 针对 Cloudflare 的 *workerd* 运行时进行了优化，支持“缩减至零 (scale to zero)”，与传统的虚拟专用服务器 (VPS) 相比，具有极高的性能和成本效益。

EmDash 目前处于 v0.1.0 预览版，开发者可以将其部署在 Cloudflare 或 Node.js 服务器上，并配备了诸如 Passkey 身份验证等现代化默认功能。

---

## 2. 人工智能助力美国产水泥与混凝土

**原文标题**: AI for American-Produced Cement and Concrete

**原文链接**: [https://engineering.fb.com/2026/03/30/data-center-engineering/ai-for-american-produced-cement-and-concrete/](https://engineering.fb.com/2026/03/30/data-center-engineering/ai-for-american-produced-cement-and-concrete/)

Meta正在通过发布**BOxCrete**（混凝土贝叶斯优化）来推动美国建筑行业的发展。这是一个开源人工智能模型和基础数据集，旨在优化混凝土配方。该计划聚焦于三大核心目标：提升可持续性、改善性能，以及通过减少行业对进口水泥的依赖（目前进口水泥占美国消费量的近25%）来促进“制造业回流”。

传统的混凝土设计依赖于缓慢且昂贵的实验室试错法。Meta的BOxCrete模型利用**自适应实验**和贝叶斯优化，智能地筛选数百万种潜在的材料组合。这使生产商能够利用本土原材料快速制定配方，并预测结构强度、固化速度和工作性能（坍落度）等关键指标。

该技术已展现出显著的现实影响力：
*   **明尼苏达州：** Meta与**Amrize**及**Mortenson**合作，在罗斯芒特的一个数据中心地基中使用了AI优化的配方。新配方达到结构强度的速度比传统配方快43%，并将裂缝风险降低了10%。
*   **伊利诺伊州：** Meta正与**伊利诺伊大学厄巴纳-香槟分校**及Amrize合作，在工业规模上应用AI驱动的低排放混凝土。
*   **宾夕法尼亚州：** 软件提供商**Quadrel**已将Meta的开源框架整合到其企业平台中，将人工智能植入日常质量控制和生产流程。

通过在MIT许可证下开源BOxCrete，Meta旨在促进全行业的普及，帮助美国生产商在成本上提升竞争力，减少碳排放并强化国内供应链。该项目已获得多项盛誉，包括“2025年度可持续混凝土项目奖”。Meta计划继续开展此类学术和工业合作，以应对混凝土性能和可持续性方面更广泛的挑战。

---

## 3. StepFun 3.5 Flash 是 OpenClaw 任务中性价比最高的模型（300 场对决）

**原文标题**: StepFun 3.5 Flash is #1 cost-effective model for OpenClaw tasks (300 battles)

**原文链接**: [https://app.uniclaw.ai/arena?tab=costEffectiveness&via=hn](https://app.uniclaw.ai/arena?tab=costEffectiveness&via=hn)

根据所提供的信息，简要总结如下：

**StepFun 3.5 Flash** 在 OpenClaw Arena 榜单上荣登智能体（Agent）任务**最具性价比模型榜首**。

该排名基于 **300 场两两对决**，旨在评估顶级 AI 模型使用“真实智能体”处理“真实任务”的能力。与理论基准测试不同，OpenClaw Arena 侧重于考察实际的现实世界智能和自主表现。

测试结果彰显了 StepFun 3.5 Flash 在高性能与经济效率之间的卓越平衡，使其成为开发者在竞争激烈的 AI 环境中寻求高性价比智能体驱动解决方案的首选。

---

## 4. Show HN：Claude Code 智能体团队实时仪表板

**原文标题**: Show HN: Real-time dashboard for Claude Code agent teams

**原文链接**: [https://github.com/simple10/agents-observe](https://github.com/simple10/agents-observe)

**Agents Observe** 是一款专为 Claude Code 智能体团队设计的实时可观测性仪表板，旨在为复杂的多智能体工作流提供透明度。尽管 Claude Code 在终端中通常以“黑盒”模式运行——自动派生子智能体并执行工具——但该工具能够捕捉并可视化每一个动作，帮助开发者调试并优化智能体行为。

**核心功能：**
*   **实时流式传输：** 使用自定义钩子（而非 OTEL）捕捉智能体动作的完整上下文，包括工具调用、bash 命令、文件编辑和 grep 模式。
*   **层级可视化：** 清晰映射父协调器与子智能体之间的关系，使并行执行过程易于追踪。
*   **深度调试：** 提供包含完整负载的可搜索时间轴，允许用户在会话中进行“时光旅行”，精准定位智能体出错的具体环节。
*   **会话管理：** 保存具有易读名称的临时会话，便于用户分析历史模式和智能体的长期性能表现。

**技术架构：**
系统通过一个轻量级的 Node.js 钩子脚本运行，该脚本捕捉事件并将其发送至基于 Hono 的 API 服务器。数据存储在本地 SQLite 数据库中，并通过 WebSockets 实时推送到基于 React 的仪表板。整个服务器环境作为 Docker 容器在本地运行，确保了数据隐私和低延迟。

**安装方法：**
用户可以直接将其作为 Claude 插件安装（`claude plugin install agents-observe`）或独立运行。激活后，可通过 `http://localhost:4981` 访问仪表板。它还包含特定技能（如 `/observe`），以便直接在 Claude 界面内检查服务器健康状况和状态。

最终，Agents Observe 将晦涩的智能体执行过程转化为透明、可操作的数据，为 Claude 与代码库的交互提供“事实真相”。

---

## 5. AI公司根据语言和BPE分词多收你60%的费用。

**原文标题**: AI companies charge you 60% more based on your language, BPE tokens

**原文链接**: [https://tokenstree.com/newsletter-article-5.html](https://tokenstree.com/newsletter-article-5.html)

文章指出，基于“Token”的AI定价模式是一种具有误导性的做法，为非英语使用者制造了巨大的隐性“语言税”。

**Token问题**
AI模型并非按字数计费，而是按Token（由字节对编码 BPE 生成的子词单位）计费。由于缺乏行业标准，各供应商（OpenAI、Google、Anthropic）使用各自的专有分词器，对文本的切分方式各不相同。这种不一致性导致用户无法准确比较成本，形成了一个有利于卖方的“黑箱”计费系统。

**语言税**
由于训练数据主要以英语为核心，英语文本的分词效率最高。其他语言的用户在处理相同内容时需支付巨额溢价：
*   **西班牙语/德语：** 比英语贵约 60%。
*   **俄语：** 贵约 154%。
*   **印地语：** 贵了近 400%。

这种差异，加之不同模型间高达 420 倍的价格差距（截至 2026 年 3 月），为国际开发者和企业制造了巨大的财务壁垒。

**解决方案：TokensTree**
为了解决这些结构性的低效问题，文章介绍了 **TokensTree**。这是一款基础设施工具，旨在通过两大核心功能优化 Token 消耗：
1.  **带有远程缓存的 SafePaths：** 该系统存储并重用经过验证的指令路径。一旦智能体（Agent）解决了某个问题，结果就会被缓存并共享，从而允许后续请求绕过完整的 Token 成本，无论用户使用的是哪种语言。
2.  **跨供应商标准化：** 提供统一的仪表板来比较不同供应商的实际成本，消除专有分词技术带来的“迷雾”。

最终，TokensTree 旨在通过拦截请求并将其转换为 BPE 效率最高的格式，从而实现 AI 访问权的平等化，降低成本并减少对环境的影响。

---

## 6. NASA Artemis II moon mission live launch broadcast

**原文标题**: NASA Artemis II moon mission live launch broadcast

**原文链接**: [https://plus.nasa.gov/scheduled-video/nasas-artemis-ii-crew-launches-to-the-moon-official-broadcast/](https://plus.nasa.gov/scheduled-video/nasas-artemis-ii-crew-launches-to-the-moon-official-broadcast/)

NASA has scheduled the official broadcast for the Artemis II mission launch, set to take place today at 1:00 PM from the Kennedy Space Center in Florida. 

As the first crewed mission of the Artemis program, this flight marks a major milestone in lunar exploration. The crew consists of four astronauts: NASA’s Reid Wiseman, Victor Glover, and Christina Koch, along with Jeremy Hansen from the Canadian Space Agency (CSA). 

The mission will involve an approximately 10-day journey around the Moon. Its primary objectives are to perform the first human-crewed test of the Orion spacecraft’s life support systems and to lay the technical groundwork for future Artemis missions. This flight is a critical step in NASA’s plan to establish a long-term human presence on and around the Moon.

---

## 7. CERN levels up with new superconducting karts

**原文标题**: CERN levels up with new superconducting karts

**原文链接**: [https://home.cern/news/news/engineering/cern-levels-new-superconducting-karts](https://home.cern/news/news/engineering/cern-levels-new-superconducting-karts)

生成摘要时出错

---

## 8. The OpenAI Graveyard: All the Deals and Products That Haven't Happened

**原文标题**: The OpenAI Graveyard: All the Deals and Products That Haven't Happened

**原文链接**: [https://www.forbes.com/sites/phoebeliu/2026/03/31/openai-graveyard-deals-and-products-havent-happened-openai/](https://www.forbes.com/sites/phoebeliu/2026/03/31/openai-graveyard-deals-and-products-havent-happened-openai/)

生成摘要时出错

---

## 9. Is BGP safe yet?

**原文标题**: Is BGP safe yet?

**原文链接**: [https://isbgpsafeyet.com/](https://isbgpsafeyet.com/)

生成摘要时出错

---

## 10. Random numbers, Persian code: A mysterious signal transfixes radio sleuths

**原文标题**: Random numbers, Persian code: A mysterious signal transfixes radio sleuths

**原文链接**: [https://www.rferl.org/a/mystery-numbers-station-persian-signal-iran-war/33700659.html](https://www.rferl.org/a/mystery-numbers-station-persian-signal-iran-war/33700659.html)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 2 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 3 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 4 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 5 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 6 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 7 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 8 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 9 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 10 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 11 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 12 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 13 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 14 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 15 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 16 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 17 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 18 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 19 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 20 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 21 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 22 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 23 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 24 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 25 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 26 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 27 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 28 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 29 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 30 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 31 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 32 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 33 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 34 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 35 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 36 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 37 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 38 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 39 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 40 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 41 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 42 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 43 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 44 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 45 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 46 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 47 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 48 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 49 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 50 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 51 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 52 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 53 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 54 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 55 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 56 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 57 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 58 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 59 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 60 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 61 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 62 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 63 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 64 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 65 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 66 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 67 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 68 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 69 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 70 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 71 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 72 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 73 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 74 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 75 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 76 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 77 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 78 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 79 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 80 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 81 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 82 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 83 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 84 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 85 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 86 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 87 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 88 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 89 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 90 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 91 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 92 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 93 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 94 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 95 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 96 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 97 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 98 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 99 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 100 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 101 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 102 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 103 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 104 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 105 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 106 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 107 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 108 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 109 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 110 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 111 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 112 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 113 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 114 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 115 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 116 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 117 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 118 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 119 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 120 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 121 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 122 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 123 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 124 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 125 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 126 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 127 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 128 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 129 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 130 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 131 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 132 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 133 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 134 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 135 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 136 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 137 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 138 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 139 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 140 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 141 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 142 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 143 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 144 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 145 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 146 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 147 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 148 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 149 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 150 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 151 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 152 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 153 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 154 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 155 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 156 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 157 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 158 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 159 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 160 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 161 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 162 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 163 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 164 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 165 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 166 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 167 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 168 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 169 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 170 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 171 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 172 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 173 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 174 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 175 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 176 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 177 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 178 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 179 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 180 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 181 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 182 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 183 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 184 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 185 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 186 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 187 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 188 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 189 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 190 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 191 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 192 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 193 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 194 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 195 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 196 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 197 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 198 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 199 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 200 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 201 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 202 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 203 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 204 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 205 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 206 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 207 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 208 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 209 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 210 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 211 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 212 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 213 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 214 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 215 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 216 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 217 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 218 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 219 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 220 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 221 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 222 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 223 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 224 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 225 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 226 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 227 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 228 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 229 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 230 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 231 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 232 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 233 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 234 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 235 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 236 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 237 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 238 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 239 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 240 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 241 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 242 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 243 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 244 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 245 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 246 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 247 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 248 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 249 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 250 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 251 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 252 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 253 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 254 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 255 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 256 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 257 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 258 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 259 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 260 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 261 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 262 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 263 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 264 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 265 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 266 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 267 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 268 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 269 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 270 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 271 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 272 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 273 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 274 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 275 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 276 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 277 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 278 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 279 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 280 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 281 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 282 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 283 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 284 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 285 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 286 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 287 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 288 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 289 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 290 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 291 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 292 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 293 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 294 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 295 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 296 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 297 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 298 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 299 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 300 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 301 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 302 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 303 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 304 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 305 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 306 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 307 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 308 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 309 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 310 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 311 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 312 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 313 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 314 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 315 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 316 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 317 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 318 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 319 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 320 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 321 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 322 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 323 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 324 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 325 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 326 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 327 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 328 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 329 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 330 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 331 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 332 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 333 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 334 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 335 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 336 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 337 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 338 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 339 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 340 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 341 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 342 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 343 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 344 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 345 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 346 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 347 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 348 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 349 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 350 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 351 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 352 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 353 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 354 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 355 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 356 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 357 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 358 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 359 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 360 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 361 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 362 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 363 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 364 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 365 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 366 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 367 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 368 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 369 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 370 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 371 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 372 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 373 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 374 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 375 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 376 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 377 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
