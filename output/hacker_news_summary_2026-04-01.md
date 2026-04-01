# Hacker News 热门文章摘要 (2026-04-01)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Playing Wolfenstein 3D with one hand in 2026

**原文标题**: Playing Wolfenstein 3D with one hand in 2026

**原文链接**: [https://arstechnica.com/gaming/2026/03/playing-wolfenstein-3d-with-one-hand-in-2026/](https://arstechnica.com/gaming/2026/03/playing-wolfenstein-3d-with-one-hand-in-2026/)

生成摘要时出错

---

## 12. A new way to measure poverty shows the US falling behind Europe

**原文标题**: A new way to measure poverty shows the US falling behind Europe

**原文链接**: [https://www.euronews.com/business/2026/03/29/a-new-way-to-measure-poverty-shows-the-us-falling-behind-europe](https://www.euronews.com/business/2026/03/29/a-new-way-to-measure-poverty-shows-the-us-falling-behind-europe)

生成摘要时出错

---

## 13. Randomness on Apple Platforms (2024)

**原文标题**: Randomness on Apple Platforms (2024)

**原文链接**: [https://blog.xoria.org/randomness-on-apple-platforms/](https://blog.xoria.org/randomness-on-apple-platforms/)

生成摘要时出错

---

## 14. Consider the Greenland Shark (2020)

**原文标题**: Consider the Greenland Shark (2020)

**原文链接**: [https://www.lrb.co.uk/the-paper/v42/n09/katherine-rundell/consider-the-greenland-shark](https://www.lrb.co.uk/the-paper/v42/n09/katherine-rundell/consider-the-greenland-shark)

生成摘要时出错

---

## 15. What Is Copilot Exactly?

**原文标题**: What Is Copilot Exactly?

**原文链接**: [https://idiallo.com/blog/what-is-copilot-exactly](https://idiallo.com/blog/what-is-copilot-exactly)

生成摘要时出错

---

## 16. Intuiting Pratt Parsing

**原文标题**: Intuiting Pratt Parsing

**原文链接**: [https://louis.co.nz/2026/03/26/pratt-parsing.html](https://louis.co.nz/2026/03/26/pratt-parsing.html)

生成摘要时出错

---

## 17. Wasmer (YC S19) Is Hiring – Rust and DevRel Positions

**原文标题**: Wasmer (YC S19) Is Hiring – Rust and DevRel Positions

**原文链接**: [https://www.workatastartup.com/companies/wasmer](https://www.workatastartup.com/companies/wasmer)

生成摘要时出错

---

## 18. Show HN: Zerobox – Sandbox any command with file and network restrictions

**原文标题**: Show HN: Zerobox – Sandbox any command with file and network restrictions

**原文链接**: [https://github.com/afshinm/zerobox](https://github.com/afshinm/zerobox)

生成摘要时出错

---

## 19. Ada and Spark on ARM Cortex-M – A Tutorial with Arduino and Nucleo Examples

**原文标题**: Ada and Spark on ARM Cortex-M – A Tutorial with Arduino and Nucleo Examples

**原文链接**: [http://inspirel.com/articles/Ada_On_Cortex.html](http://inspirel.com/articles/Ada_On_Cortex.html)

生成摘要时出错

---

## 20. Claude Wrote a Full FreeBSD Remote Kernel RCE with Root Shell (CVE-2026-4747)

**原文标题**: Claude Wrote a Full FreeBSD Remote Kernel RCE with Root Shell (CVE-2026-4747)

**原文链接**: [https://github.com/califio/publications/blob/main/MADBugs/CVE-2026-4747/write-up.md](https://github.com/califio/publications/blob/main/MADBugs/CVE-2026-4747/write-up.md)

生成摘要时出错

---

## 21. Show HN: Sycamore – next gen Rust web UI library using fine-grained reactivity

**原文标题**: Show HN: Sycamore – next gen Rust web UI library using fine-grained reactivity

**原文链接**: [https://sycamore.dev](https://sycamore.dev)

生成摘要时出错

---

## 22. Show HN: CLI to order groceries via reverse-engineered REWE API (Haskell)

**原文标题**: Show HN: CLI to order groceries via reverse-engineered REWE API (Haskell)

**原文链接**: [https://github.com/yannick-cw/korb](https://github.com/yannick-cw/korb)

生成摘要时出错

---

## 23. Claude Code Unpacked : A visual guide

**原文标题**: Claude Code Unpacked : A visual guide

**原文链接**: [https://ccunpacked.dev/](https://ccunpacked.dev/)

生成摘要时出错

---

## 24. The Document Foundation ejects its core developers

**原文标题**: The Document Foundation ejects its core developers

**原文链接**: [https://www.collaboraonline.com/blog/tdf-ejects-its-core-developers/](https://www.collaboraonline.com/blog/tdf-ejects-its-core-developers/)

生成摘要时出错

---

## 25. A dot a day keeps the clutter away

**原文标题**: A dot a day keeps the clutter away

**原文链接**: [https://scottlawsonbc.com/post/dot-system](https://scottlawsonbc.com/post/dot-system)

生成摘要时出错

---

## 26. Chess in SQL

**原文标题**: Chess in SQL

**原文链接**: [https://www.dbpro.app/blog/chess-in-pure-sql](https://www.dbpro.app/blog/chess-in-pure-sql)

生成摘要时出错

---

## 27. New patches allow building Linux IPv6-only

**原文标题**: New patches allow building Linux IPv6-only

**原文链接**: [https://www.phoronix.com/news/Linux-IPv6-IPv4-Legacy-Knobs](https://www.phoronix.com/news/Linux-IPv6-IPv4-Legacy-Knobs)

生成摘要时出错

---

## 28. Show HN: 1-Bit Bonsai, the First Commercially Viable 1-Bit LLMs

**原文标题**: Show HN: 1-Bit Bonsai, the First Commercially Viable 1-Bit LLMs

**原文链接**: [https://prismml.com/](https://prismml.com/)

生成摘要时出错

---

## 29. TruffleRuby

**原文标题**: TruffleRuby

**原文链接**: [https://chrisseaton.com/truffleruby/](https://chrisseaton.com/truffleruby/)

生成摘要时出错

---

## 30. TinyLoRA – Learning to Reason in 13 Parameters

**原文标题**: TinyLoRA – Learning to Reason in 13 Parameters

**原文链接**: [https://arxiv.org/abs/2602.04118](https://arxiv.org/abs/2602.04118)

生成摘要时出错

---

## 31. MiniStack (replacement for LocalStack)

**原文标题**: MiniStack (replacement for LocalStack)

**原文链接**: [https://ministack.org/](https://ministack.org/)

生成摘要时出错

---

## 32. Bring Back MiniDV with This Raspberry Pi FireWire Hat

**原文标题**: Bring Back MiniDV with This Raspberry Pi FireWire Hat

**原文链接**: [https://www.jeffgeerling.com/blog/2026/minidv-with-raspberry-pi-firewire-hat/](https://www.jeffgeerling.com/blog/2026/minidv-with-raspberry-pi-firewire-hat/)

生成摘要时出错

---

## 33. The Finest Swiss Quality Quaternions

**原文标题**: The Finest Swiss Quality Quaternions

**原文链接**: [https://se3.ch/](https://se3.ch/)

生成摘要时出错

---

## 34. 4D Doom

**原文标题**: 4D Doom

**原文链接**: [https://github.com/danieldugas/HYPERHELL](https://github.com/danieldugas/HYPERHELL)

生成摘要时出错

---

## 35. Magic mushroom-infused products appear in Colorado gas stations

**原文标题**: Magic mushroom-infused products appear in Colorado gas stations

**原文链接**: [https://theconversation.com/magic-mushroom-infused-products-appear-in-colorado-gas-stations-what-public-health-officials-want-consumers-to-know-274935](https://theconversation.com/magic-mushroom-infused-products-appear-in-colorado-gas-stations-what-public-health-officials-want-consumers-to-know-274935)

生成摘要时出错

---

## 36. Axios compromised on NPM – Malicious versions drop remote access trojan

**原文标题**: Axios compromised on NPM – Malicious versions drop remote access trojan

**原文链接**: [https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan)

生成摘要时出错

---

## 37. OpenAI closes funding round at an $852B valuation

**原文标题**: OpenAI closes funding round at an $852B valuation

**原文链接**: [https://www.cnbc.com/2026/03/31/openai-funding-round-ipo.html](https://www.cnbc.com/2026/03/31/openai-funding-round-ipo.html)

生成摘要时出错

---

## 38. The Autocrat's Dilemma

**原文标题**: The Autocrat's Dilemma

**原文链接**: [https://www.theatlantic.com/international/2026/04/donald-trump-xi-jinping-china-authoritarianism/686631/](https://www.theatlantic.com/international/2026/04/donald-trump-xi-jinping-china-authoritarianism/686631/)

生成摘要时出错

---

## 39. Neanderthals survived on a knife's edge for 350k years

**原文标题**: Neanderthals survived on a knife's edge for 350k years

**原文链接**: [https://www.science.org/content/article/neanderthals-survived-knife-s-edge-350-000-years](https://www.science.org/content/article/neanderthals-survived-knife-s-edge-350-000-years)

生成摘要时出错

---

## 40. Estonia to relaunch Skype as Europe's sovereign platform

**原文标题**: Estonia to relaunch Skype as Europe's sovereign platform

**原文链接**: [https://estonianworld.com/technology/estonia-to-relaunch-skype-as-europes-sovereign-platform/](https://estonianworld.com/technology/estonia-to-relaunch-skype-as-europes-sovereign-platform/)

生成摘要时出错

---

## 41. Teenage Engineering's PO-32 acoustic modem and synth implementation

**原文标题**: Teenage Engineering's PO-32 acoustic modem and synth implementation

**原文链接**: [https://github.com/ericlewis/libpo32](https://github.com/ericlewis/libpo32)

生成摘要时出错

---

## 42. CUDA Released in Basic

**原文标题**: CUDA Released in Basic

**原文链接**: [https://developer.nvidia.com/blog/cuda-tile-programming-now-available-for-basic/](https://developer.nvidia.com/blog/cuda-tile-programming-now-available-for-basic/)

生成摘要时出错

---

## 43. Ordinary Lab Gloves May Have Skewed Microplastic Data

**原文标题**: Ordinary Lab Gloves May Have Skewed Microplastic Data

**原文链接**: [https://nautil.us/ordinary-lab-gloves-may-have-skewed-microplastic-data-1279386](https://nautil.us/ordinary-lab-gloves-may-have-skewed-microplastic-data-1279386)

生成摘要时出错

---

## 44. From 300KB to 69KB per Token: How LLM Architectures Solve the KV Cache Problem

**原文标题**: From 300KB to 69KB per Token: How LLM Architectures Solve the KV Cache Problem

**原文链接**: [https://news.future-shock.ai/the-weight-of-remembering/](https://news.future-shock.ai/the-weight-of-remembering/)

生成摘要时出错

---

## 45. Cohere Transcribe: Speech Recognition

**原文标题**: Cohere Transcribe: Speech Recognition

**原文链接**: [https://cohere.com/blog/transcribe](https://cohere.com/blog/transcribe)

生成摘要时出错

---

## 46. Show HN: Postgres extension for BM25 relevance-ranked full-text search

**原文标题**: Show HN: Postgres extension for BM25 relevance-ranked full-text search

**原文链接**: [https://github.com/timescale/pg_textsearch](https://github.com/timescale/pg_textsearch)

生成摘要时出错

---

## 47. In Case of Emergency, Make Burrito Bison 3 (2017)

**原文标题**: In Case of Emergency, Make Burrito Bison 3 (2017)

**原文链接**: [https://juicybeast.com/2017/08/03/in-case-of-emergency-make-burrito-bison-3/](https://juicybeast.com/2017/08/03/in-case-of-emergency-make-burrito-bison-3/)

生成摘要时出错

---

## 48. Back to FreeBSD – Part 2 – Jails

**原文标题**: Back to FreeBSD – Part 2 – Jails

**原文链接**: [https://hypha.pub/back-to-freebsd-part-2](https://hypha.pub/back-to-freebsd-part-2)

生成摘要时出错

---

## 49. Digitizing photos from the 1998 Game Boy Camera

**原文标题**: Digitizing photos from the 1998 Game Boy Camera

**原文链接**: [https://swiftrocks.com/digitizing-photos-from-the-1998-game-boy-camera](https://swiftrocks.com/digitizing-photos-from-the-1998-game-boy-camera)

生成摘要时出错

---

## 50. I traced my traffic through a home Tailscale exit node

**原文标题**: I traced my traffic through a home Tailscale exit node

**原文链接**: [https://tech.stonecharioteer.com/posts/2026/tailscale-exit-nodes/](https://tech.stonecharioteer.com/posts/2026/tailscale-exit-nodes/)

生成摘要时出错

---

## 51. OpenAI demand sinks on secondary market as Anthropic runs hot

**原文标题**: OpenAI demand sinks on secondary market as Anthropic runs hot

**原文链接**: [https://www.bloomberg.com/news/articles/2026-04-01/openai-demand-sinks-on-secondary-market-as-anthropic-runs-hot](https://www.bloomberg.com/news/articles/2026-04-01/openai-demand-sinks-on-secondary-market-as-anthropic-runs-hot)

生成摘要时出错

---

## 52. 6o6 v1.1: Faster 6502-on-6502 virtualization for a C64/Apple II Apple-1 emulator

**原文标题**: 6o6 v1.1: Faster 6502-on-6502 virtualization for a C64/Apple II Apple-1 emulator

**原文链接**: [http://oldvcr.blogspot.com/2026/03/6o6-v11-faster-6502-on-6502.html](http://oldvcr.blogspot.com/2026/03/6o6-v11-faster-6502-on-6502.html)

生成摘要时出错

---

## 53. Replace axios with a simple custom fetch wrapper

**原文标题**: Replace axios with a simple custom fetch wrapper

**原文链接**: [https://kentcdodds.com/blog/replace-axios-with-a-simple-custom-fetch-wrapper](https://kentcdodds.com/blog/replace-axios-with-a-simple-custom-fetch-wrapper)

生成摘要时出错

---

## 54. We Built It with Slide Rules. Then We Forgot How

**原文标题**: We Built It with Slide Rules. Then We Forgot How

**原文链接**: [https://unmitigatedrisk.com/?p=1227](https://unmitigatedrisk.com/?p=1227)

生成摘要时出错

---

## 55. Learn Something Old Every Day, Part XVIII: How Does FPU Detection Work?

**原文标题**: Learn Something Old Every Day, Part XVIII: How Does FPU Detection Work?

**原文链接**: [https://www.os2museum.com/wp/learn-something-old-every-day-part-xviii-how-does-fpu-detection-work/](https://www.os2museum.com/wp/learn-something-old-every-day-part-xviii-how-does-fpu-detection-work/)

生成摘要时出错

---

## 56. Show HN: Forkrun – NUMA-aware shell parallelizer (50×–400× faster than parallel)

**原文标题**: Show HN: Forkrun – NUMA-aware shell parallelizer (50×–400× faster than parallel)

**原文链接**: [https://github.com/jkool702/forkrun](https://github.com/jkool702/forkrun)

生成摘要时出错

---

## 57. Iran threatens Nvidia, Apple and other 18 tech companies

**原文标题**: Iran threatens Nvidia, Apple and other 18 tech companies

**原文链接**: [https://www.cnbc.com/2026/04/01/iran-irgc-nvidia-appple-attack-threat.html](https://www.cnbc.com/2026/04/01/iran-irgc-nvidia-appple-attack-threat.html)

生成摘要时出错

---

## 58. Analyzing Geekbench 6 under Intel's BOT

**原文标题**: Analyzing Geekbench 6 under Intel's BOT

**原文链接**: [https://www.geekbench.com/blog/2026/03/analyzing-geekbench-6-under-intels-bot/](https://www.geekbench.com/blog/2026/03/analyzing-geekbench-6-under-intels-bot/)

生成摘要时出错

---

## 59. Why the US Navy won't blast the Iranians and 'open' Strait of Hormuz

**原文标题**: Why the US Navy won't blast the Iranians and 'open' Strait of Hormuz

**原文链接**: [https://responsiblestatecraft.org/iran-strait-of-hormuz/](https://responsiblestatecraft.org/iran-strait-of-hormuz/)

生成摘要时出错

---

## 60. Show HN: Baton – A desktop app for developing with AI agents

**原文标题**: Show HN: Baton – A desktop app for developing with AI agents

**原文链接**: [https://getbaton.dev/](https://getbaton.dev/)

生成摘要时出错

---

## 61. AI has suddenly become more useful to open-source developers

**原文标题**: AI has suddenly become more useful to open-source developers

**原文链接**: [https://www.zdnet.com/article/maybe-open-source-needs-ai/](https://www.zdnet.com/article/maybe-open-source-needs-ai/)

生成摘要时出错

---

## 62. The Claude Code Source Leak: fake tools, frustration regexes, undercover mode

**原文标题**: The Claude Code Source Leak: fake tools, frustration regexes, undercover mode

**原文链接**: [https://alex000kim.com/posts/2026-03-31-claude-code-source-leak/](https://alex000kim.com/posts/2026-03-31-claude-code-source-leak/)

生成摘要时出错

---

## 63. What major works of literature were written after age of 85? 75? 65?

**原文标题**: What major works of literature were written after age of 85? 75? 65?

**原文链接**: [https://statmodeling.stat.columbia.edu/2026/03/25/what-major-works-of-literature-were-written-after-age-of-85-75-65/](https://statmodeling.stat.columbia.edu/2026/03/25/what-major-works-of-literature-were-written-after-age-of-85-75-65/)

生成摘要时出错

---

## 64. GitHub Monaspace Case Study

**原文标题**: GitHub Monaspace Case Study

**原文链接**: [https://lettermatic.com/custom/monaspace-case-study](https://lettermatic.com/custom/monaspace-case-study)

生成摘要时出错

---

## 65. Combinators

**原文标题**: Combinators

**原文链接**: [https://tinyapl.rubenverg.com/docs/info/combinators](https://tinyapl.rubenverg.com/docs/info/combinators)

生成摘要时出错

---

## 66. Apple Removes iPhone Vibe Coding App from App Store

**原文标题**: Apple Removes iPhone Vibe Coding App from App Store

**原文链接**: [https://gizmodo.com/apple-removes-iphone-vibe-coding-app-from-app-store-2000740084](https://gizmodo.com/apple-removes-iphone-vibe-coding-app-from-app-store-2000740084)

生成摘要时出错

---

## 67. Movie Review: The AI Doc (2026)

**原文标题**: Movie Review: The AI Doc (2026)

**原文链接**: [https://thezvi.substack.com/p/movie-review-the-ai-doc](https://thezvi.substack.com/p/movie-review-the-ai-doc)

生成摘要时出错

---

## 68. Artemis II is not safe to fly

**原文标题**: Artemis II is not safe to fly

**原文链接**: [https://idlewords.com/2026/03/artemis_ii_is_not_safe_to_fly.htm](https://idlewords.com/2026/03/artemis_ii_is_not_safe_to_fly.htm)

生成摘要时出错

---

## 69. Google's 200M-parameter time-series foundation model with 16k context

**原文标题**: Google's 200M-parameter time-series foundation model with 16k context

**原文链接**: [https://github.com/google-research/timesfm](https://github.com/google-research/timesfm)

生成摘要时出错

---

## 70. Remembering Magnetic Memories and the Apollo AGC

**原文标题**: Remembering Magnetic Memories and the Apollo AGC

**原文链接**: [https://2earth.github.io/website/20260304.html](https://2earth.github.io/website/20260304.html)

生成摘要时出错

---

## 71. Slop is not necessarily the future

**原文标题**: Slop is not necessarily the future

**原文链接**: [https://www.greptile.com/blog/ai-slopware-future](https://www.greptile.com/blog/ai-slopware-future)

生成摘要时出错

---

## 72. Pandoc: A Workhorse for Document Conversion

**原文标题**: Pandoc: A Workhorse for Document Conversion

**原文链接**: [https://lwn.net/Articles/1064692/](https://lwn.net/Articles/1064692/)

生成摘要时出错

---

## 73. Ollama is now powered by MLX on Apple Silicon in preview

**原文标题**: Ollama is now powered by MLX on Apple Silicon in preview

**原文链接**: [https://ollama.com/blog/mlx](https://ollama.com/blog/mlx)

生成摘要时出错

---

## 74. Show HN: Claude Code rewritten as a bash script

**原文标题**: Show HN: Claude Code rewritten as a bash script

**原文链接**: [https://github.com/jdcodes1/claude-sh](https://github.com/jdcodes1/claude-sh)

生成摘要时出错

---

## 75. Good CTE, Bad CTE

**原文标题**: Good CTE, Bad CTE

**原文链接**: [https://boringsql.com/posts/good-cte-bad-cte/](https://boringsql.com/posts/good-cte-bad-cte/)

生成摘要时出错

---

## 76. GitHub's Historic Uptime

**原文标题**: GitHub's Historic Uptime

**原文链接**: [https://damrnelson.github.io/github-historical-uptime/](https://damrnelson.github.io/github-historical-uptime/)

生成摘要时出错

---

## 77. Anthropic Races to Contain Leak of Code Behind Claude AI Agent

**原文标题**: Anthropic Races to Contain Leak of Code Behind Claude AI Agent

**原文链接**: [https://www.wsj.com/tech/ai/anthropic-races-to-contain-leak-of-code-behind-claude-ai-agent-4bc5acc7](https://www.wsj.com/tech/ai/anthropic-races-to-contain-leak-of-code-behind-claude-ai-agent-4bc5acc7)

生成摘要时出错

---

## 78. Open source CAD in the browser (Solvespace)

**原文标题**: Open source CAD in the browser (Solvespace)

**原文链接**: [https://solvespace.com/webver.pl](https://solvespace.com/webver.pl)

生成摘要时出错

---

## 79. Microsoft: Copilot is for entertainment purposes only

**原文标题**: Microsoft: Copilot is for entertainment purposes only

**原文链接**: [https://www.microsoft.com/en-us/microsoft-copilot/for-individuals/termsofuse](https://www.microsoft.com/en-us/microsoft-copilot/for-individuals/termsofuse)

生成摘要时出错

---

## 80. Inside the 'self-driving' lab revolution

**原文标题**: Inside the 'self-driving' lab revolution

**原文链接**: [https://www.nature.com/articles/d41586-026-00974-2](https://www.nature.com/articles/d41586-026-00974-2)

生成摘要时出错

---

## 81. Accidentally created my first fork bomb with Claude Code

**原文标题**: Accidentally created my first fork bomb with Claude Code

**原文链接**: [https://www.droppedasbaby.com/posts/2602-01/](https://www.droppedasbaby.com/posts/2602-01/)

生成摘要时出错

---

## 82. Claude Code's source code has been leaked via a map file in their NPM registry

**原文标题**: Claude Code's source code has been leaked via a map file in their NPM registry

**原文链接**: [https://twitter.com/Fried_rice/status/2038894956459290963](https://twitter.com/Fried_rice/status/2038894956459290963)

生成摘要时出错

---

## 83. 食线虫真菌

**原文标题**: Nematophagous Fungus

**原文链接**: [https://en.wikipedia.org/wiki/Nematophagous_fungus](https://en.wikipedia.org/wiki/Nematophagous_fungus)

生成摘要时出错

---

## 84. Claude Code users hitting usage limits 'way faster than expected'

**原文标题**: Claude Code users hitting usage limits 'way faster than expected'

**原文链接**: [https://www.theregister.com/2026/03/31/anthropic_claude_code_limits/](https://www.theregister.com/2026/03/31/anthropic_claude_code_limits/)

生成摘要时出错

---

## 85. Super Micro Computer Investors Look for Exits

**原文标题**: Super Micro Computer Investors Look for Exits

**原文链接**: [https://catenaa.com/markets/equities/super-micro-computer-investors-look-for-exits/](https://catenaa.com/markets/equities/super-micro-computer-investors-look-for-exits/)

生成摘要时出错

---

## 86. Fedware: Government apps that spy harder than the apps they ban

**原文标题**: Fedware: Government apps that spy harder than the apps they ban

**原文链接**: [https://www.sambent.com/the-white-house-app-has-huawei-spyware-and-an-ice-tip-line/](https://www.sambent.com/the-white-house-app-has-huawei-spyware-and-an-ice-tip-line/)

生成摘要时出错

---

## 87. We intercepted the White House app's network traffic

**原文标题**: We intercepted the White House app's network traffic

**原文链接**: [https://www.atomic.computer/blog/white-house-app-network-traffic-analysis/](https://www.atomic.computer/blog/white-house-app-network-traffic-analysis/)

生成摘要时出错

---

## 88. Butterfly-collecting: The history of an insult (2017)

**原文标题**: Butterfly-collecting: The history of an insult (2017)

**原文链接**: [http://lughat.blogspot.com/2017/10/butterfly-collecting-history-of-insult.html](http://lughat.blogspot.com/2017/10/butterfly-collecting-history-of-insult.html)

生成摘要时出错

---

## 89. Prompt Engineering for Humans

**原文标题**: Prompt Engineering for Humans

**原文链接**: [https://michaelheap.com/prompt-engineering-for-humans/](https://michaelheap.com/prompt-engineering-for-humans/)

生成摘要时出错

---

## 90. GitHub backs down, kills Copilot pull-request ads after backlash

**原文标题**: GitHub backs down, kills Copilot pull-request ads after backlash

**原文链接**: [https://www.theregister.com/2026/03/30/github_copilot_ads_pull_requests/](https://www.theregister.com/2026/03/30/github_copilot_ads_pull_requests/)

生成摘要时出错

---

## 91. Cherri – programming language that compiles to an Apple Shortuct

**原文标题**: Cherri – programming language that compiles to an Apple Shortuct

**原文链接**: [https://github.com/electrikmilk/cherri](https://github.com/electrikmilk/cherri)

生成摘要时出错

---

## 92. Scotty: A beautiful SSH task runner

**原文标题**: Scotty: A beautiful SSH task runner

**原文链接**: [https://freek.dev/3064-scotty-a-beautiful-ssh-task-runner](https://freek.dev/3064-scotty-a-beautiful-ssh-task-runner)

生成摘要时出错

---

## 93. If You Need a Laptop, Buy It Now

**原文标题**: If You Need a Laptop, Buy It Now

**原文链接**: [https://www.theatlantic.com/technology/2026/03/laptop-electronics-ram-ai-tax/686628/](https://www.theatlantic.com/technology/2026/03/laptop-electronics-ram-ai-tax/686628/)

生成摘要时出错

---

## 94. Vulnerability research is cooked

**原文标题**: Vulnerability research is cooked

**原文链接**: [https://sockpuppet.org/blog/2026/03/30/vulnerability-research-is-cooked/](https://sockpuppet.org/blog/2026/03/30/vulnerability-research-is-cooked/)

生成摘要时出错

---

## 95. Safe ways to do things in bash (2023)

**原文标题**: Safe ways to do things in bash (2023)

**原文链接**: [https://github.com/anordal/shellharden/blob/master/how_to_do_things_safely_in_bash.md](https://github.com/anordal/shellharden/blob/master/how_to_do_things_safely_in_bash.md)

生成摘要时出错

---

## 96. Securing Elliptic Curve Cryptocurrencies Against Quantum Vulnerabilities [pdf]

**原文标题**: Securing Elliptic Curve Cryptocurrencies Against Quantum Vulnerabilities [pdf]

**原文链接**: [https://quantumai.google/static/site-assets/downloads/cryptocurrency-whitepaper.pdf](https://quantumai.google/static/site-assets/downloads/cryptocurrency-whitepaper.pdf)

生成摘要时出错

---

## 97. OpenGridWorks: Electricity infrastructure, mapped

**原文标题**: OpenGridWorks: Electricity infrastructure, mapped

**原文链接**: [https://www.opengridworks.com](https://www.opengridworks.com)

生成摘要时出错

---

## 98. Do your own writing

**原文标题**: Do your own writing

**原文链接**: [https://alexhwoods.com/dont-let-ai-write-for-you/](https://alexhwoods.com/dont-let-ai-write-for-you/)

生成摘要时出错

---

## 99. Audio tapes reveal mass rule-breaking in Milgram's obedience experiments

**原文标题**: Audio tapes reveal mass rule-breaking in Milgram's obedience experiments

**原文链接**: [https://www.psypost.org/audio-tapes-reveal-mass-rule-breaking-in-milgram-s-obedience-experiments-2026-03-26/](https://www.psypost.org/audio-tapes-reveal-mass-rule-breaking-in-milgram-s-obedience-experiments-2026-03-26/)

生成摘要时出错

---

## 100. A million new SpaceX satellites will destroy the night sky

**原文标题**: A million new SpaceX satellites will destroy the night sky

**原文链接**: [https://theconversation.com/a-million-new-spacex-satellites-will-destroy-the-night-sky-for-everyone-on-earth-277938](https://theconversation.com/a-million-new-spacex-satellites-will-destroy-the-night-sky-for-everyone-on-earth-277938)

生成摘要时出错

---

