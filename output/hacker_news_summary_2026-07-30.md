# Hacker News 热门文章摘要 (2026-07-30)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Father of Apalachee school shooter has been sentenced to 15 years in prison

**原文标题**: Father of Apalachee school shooter has been sentenced to 15 years in prison

**原文链接**: [https://www.wsbtv.com/news/local/apalachee-school-shooting-father-shooter-faces-own-sentence-up-180-years/ZXCE3UUUFZH6NPGN2JR5LGRSHM/](https://www.wsbtv.com/news/local/apalachee-school-shooting-father-shooter-faces-own-sentence-up-180-years/ZXCE3UUUFZH6NPGN2JR5LGRSHM/)

生成摘要时出错

---

## 12. Bryan Johnson: I've taken longevity too far

**原文标题**: Bryan Johnson: I've taken longevity too far

**原文链接**: [https://xcancel.com/bryan_johnson/status/2082631490840760622#m](https://xcancel.com/bryan_johnson/status/2082631490840760622#m)

生成摘要时出错

---

## 13. Pgtestdb's template cloning approach to testing is fast

**原文标题**: Pgtestdb's template cloning approach to testing is fast

**原文链接**: [https://brandur.org/fragments/pgtestdb](https://brandur.org/fragments/pgtestdb)

生成摘要时出错

---

## 14. Citadel Buys Situational Awareness's Stock Portfolio After Big Losses in AI

**原文标题**: Citadel Buys Situational Awareness's Stock Portfolio After Big Losses in AI

**原文链接**: [https://www.wsj.com/finance/citadel-buys-situational-awarenesss-stock-portfolio-after-big-losses-in-ai-5117159b](https://www.wsj.com/finance/citadel-buys-situational-awarenesss-stock-portfolio-after-big-losses-in-ai-5117159b)

生成摘要时出错

---

## 15. Google will expand age checks on Android worldwide till the end of the year

**原文标题**: Google will expand age checks on Android worldwide till the end of the year

**原文链接**: [https://android-developers.googleblog.com/2026/07/google-play-age-signals-api-safer-experiences.html](https://android-developers.googleblog.com/2026/07/google-play-age-signals-api-safer-experiences.html)

生成摘要时出错

---

## 16. Logic for Programmers

**原文标题**: Logic for Programmers

**原文链接**: [https://logicforprogrammers.com/](https://logicforprogrammers.com/)

生成摘要时出错

---

## 17. The coolest use for the Vision Pro

**原文标题**: The coolest use for the Vision Pro

**原文链接**: [https://christianselig.com/2026/07/vision-pro-house/](https://christianselig.com/2026/07/vision-pro-house/)

生成摘要时出错

---

## 18. Concurrency, interactivity, mutability, choose two

**原文标题**: Concurrency, interactivity, mutability, choose two

**原文链接**: [https://www.n16f.net/blog/concurrency-interactivity-mutability-choose-two/](https://www.n16f.net/blog/concurrency-interactivity-mutability-choose-two/)

生成摘要时出错

---

## 19. Why don't people use formal methods? (2019)

**原文标题**: Why don't people use formal methods? (2019)

**原文链接**: [https://www.hillelwayne.com/post/why-dont-people-use-formal-methods/](https://www.hillelwayne.com/post/why-dont-people-use-formal-methods/)

生成摘要时出错

---

## 20. ESP32-C6 Power Consumption: Arduino vs. Zephyr vs. ESP-IDF Comparison

**原文标题**: ESP32-C6 Power Consumption: Arduino vs. Zephyr vs. ESP-IDF Comparison

**原文链接**: [https://www.qoitech.com/blog/esp32-c6-power-consumption-comparison/](https://www.qoitech.com/blog/esp32-c6-power-consumption-comparison/)

生成摘要时出错

---

## 21. LLM Routers Have Become a Service Category of Their Own

**原文标题**: LLM Routers Have Become a Service Category of Their Own

**原文链接**: [https://techstrong.ai/articles/llm-routers-have-become-a-service-category-of-their-own/](https://techstrong.ai/articles/llm-routers-have-become-a-service-category-of-their-own/)

生成摘要时出错

---

## 22. US gov and OpenAI mislabel map of Africa at global conference

**原文标题**: US gov and OpenAI mislabel map of Africa at global conference

**原文链接**: [https://www.theguardian.com/us-news/2026/jul/30/government-map-mislabels-african-countries](https://www.theguardian.com/us-news/2026/jul/30/government-map-mislabels-african-countries)

生成摘要时出错

---

## 23. Kuna: Decompiler Development in the Age of Coding Agents

**原文标题**: Kuna: Decompiler Development in the Age of Coding Agents

**原文链接**: [https://noelo.org/blog/kuna-release/](https://noelo.org/blog/kuna-release/)

生成摘要时出错

---

## 24. Show HN：仅需 2GB 内存即可在任何 M 系列 Mac 上运行 Gemma 4 26B 的开源引擎

**原文标题**: Show HN: Open-source engine running Gemma 4 26B in 2 GB RAM on any M-series Mac

**原文链接**: [https://github.com/drumih/turbo-fieldfare](https://github.com/drumih/turbo-fieldfare)

生成摘要时出错

---

## 25. Going beneath NTFS: USN Journal, dfir_NTFS, and artefact-driven investigations

**原文标题**: Going beneath NTFS: USN Journal, dfir_NTFS, and artefact-driven investigations

**原文链接**: [https://andreafortuna.org/2026/07/06/ntfs-forensics-deep-dive/](https://andreafortuna.org/2026/07/06/ntfs-forensics-deep-dive/)

生成摘要时出错

---

## 26. Parody Hacker News (2013)

**原文标题**: Parody Hacker News (2013)

**原文链接**: [http://bradconte.com/files/misc/HackerNewsParodyThread/](http://bradconte.com/files/misc/HackerNewsParodyThread/)

生成摘要时出错

---

## 27. Superlogical

**原文标题**: Superlogical

**原文链接**: [https://www.superlogical.com/](https://www.superlogical.com/)

生成摘要时出错

---

## 28. ChatGPT, Roblox to fall under strictest EU rules for platforms

**原文标题**: ChatGPT, Roblox to fall under strictest EU rules for platforms

**原文链接**: [https://www.bloomberg.com/news/articles/2026-07-29/chatgpt-roblox-to-fall-under-strictest-eu-rules-for-platforms](https://www.bloomberg.com/news/articles/2026-07-29/chatgpt-roblox-to-fall-under-strictest-eu-rules-for-platforms)

生成摘要时出错

---

## 29. List of 6502 based computers and 6502 history

**原文标题**: List of 6502 based computers and 6502 history

**原文链接**: [https://www.machineideas.com/6502](https://www.machineideas.com/6502)

生成摘要时出错

---

## 30. Why DNA damage from smoking and UV rays cause cancer in some but not others

**原文标题**: Why DNA damage from smoking and UV rays cause cancer in some but not others

**原文链接**: [https://www.cam.ac.uk/research/news/study-reveals-why-dna-damage-from-smoking-and-uv-rays-may-cause-cancer-in-some-people-but-not-others](https://www.cam.ac.uk/research/news/study-reveals-why-dna-damage-from-smoking-and-uv-rays-may-cause-cancer-in-some-people-but-not-others)

生成摘要时出错

---

## 31. We discovered a new variant of Super Mario Bros

**原文标题**: We discovered a new variant of Super Mario Bros

**原文链接**: [https://nintendowire.com/news/2026/07/29/we-discovered-a-new-super-mario-bros-variant/](https://nintendowire.com/news/2026/07/29/we-discovered-a-new-super-mario-bros-variant/)

生成摘要时出错

---

## 32. U.S. Sees Iran as Likely Behind Cyberattack on Minnesota Water Systems

**原文标题**: U.S. Sees Iran as Likely Behind Cyberattack on Minnesota Water Systems

**原文链接**: [https://www.nytimes.com/2026/07/30/us/politics/minnesota-water-cyberattack-iran.html](https://www.nytimes.com/2026/07/30/us/politics/minnesota-water-cyberattack-iran.html)

生成摘要时出错

---

## 33. LLM Honeypot

**原文标题**: LLM Honeypot

**原文链接**: [https://llm2human.pages.dev/](https://llm2human.pages.dev/)

生成摘要时出错

---

## 34. The Apple Calculator Language

**原文标题**: The Apple Calculator Language

**原文链接**: [https://wadetregaskis.com/the-apple-calculator-language/](https://wadetregaskis.com/the-apple-calculator-language/)

生成摘要时出错

---

## 35. thinkingmachines/Inkling-Small

**原文标题**: thinkingmachines/Inkling-Small

**原文链接**: [https://huggingface.co/thinkingmachines/Inkling-Small](https://huggingface.co/thinkingmachines/Inkling-Small)

生成摘要时出错

---

## 36. Launch HN: Tokenless (YC S26) – Automatic model switching to save money

**原文标题**: Launch HN: Tokenless (YC S26) – Automatic model switching to save money

**原文链接**: [https://usetokenless.com/](https://usetokenless.com/)

生成摘要时出错

---

## 37. KOReader

**原文标题**: KOReader

**原文链接**: [https://koreader.rocks/](https://koreader.rocks/)

生成摘要时出错

---

## 38. North Korea's elite hackers turned on their own government – and got caught

**原文标题**: North Korea's elite hackers turned on their own government – and got caught

**原文链接**: [https://www.bitdefender.com/en-us/blog/hotforsecurity/north-korea-hackers-own-government](https://www.bitdefender.com/en-us/blog/hotforsecurity/north-korea-hackers-own-government)

生成摘要时出错

---

## 39. Keychron announces first open-source firmware for gaming mice

**原文标题**: Keychron announces first open-source firmware for gaming mice

**原文链接**: [https://www.digitalfoundry.net/news/2026/07/keychron-announces-first-open-source-firmware-for-gaming-mice](https://www.digitalfoundry.net/news/2026/07/keychron-announces-first-open-source-firmware-for-gaming-mice)

生成摘要时出错

---

## 40. Self-hosting Kimi K3: 20% more hardware cost, 20% better task resolution

**原文标题**: Self-hosting Kimi K3: 20% more hardware cost, 20% better task resolution

**原文链接**: [https://aistack.imec-int.com/blog/gpu-self-hosting](https://aistack.imec-int.com/blog/gpu-self-hosting)

生成摘要时出错

---

## 41. The Productivity Mirage

**原文标题**: The Productivity Mirage

**原文链接**: [https://frantic.im/mirage/](https://frantic.im/mirage/)

生成摘要时出错

---

## 42. Hunter-gatherers introduced fish to a mountain lake 7000 years ago

**原文标题**: Hunter-gatherers introduced fish to a mountain lake 7000 years ago

**原文链接**: [https://www.newscientist.com/article/2580119-hunter-gatherers-introduced-fish-to-a-mountain-lake-7000-years-ago/](https://www.newscientist.com/article/2580119-hunter-gatherers-introduced-fish-to-a-mountain-lake-7000-years-ago/)

生成摘要时出错

---

## 43. Show HN: Hacker Fables – A satirical cyberpunk novel you can read as a man page

**原文标题**: Show HN: Hacker Fables – A satirical cyberpunk novel you can read as a man page

**原文链接**: [https://sebastiancarlos.github.io/hacker-fables/](https://sebastiancarlos.github.io/hacker-fables/)

生成摘要时出错

---

## 44. 'My life's screwed': Korean investors stress out after AI bubble bursts

**原文标题**: 'My life's screwed': Korean investors stress out after AI bubble bursts

**原文链接**: [https://www.ft.com/content/23f388eb-e8ab-4fb1-b1ca-8e04eb4561a1](https://www.ft.com/content/23f388eb-e8ab-4fb1-b1ca-8e04eb4561a1)

生成摘要时出错

---

## 45. Is Samsung Pioneering Mass Adoption of USDC?

**原文标题**: Is Samsung Pioneering Mass Adoption of USDC?

**原文链接**: [https://irishtechnews.ie/is-samsung-pioneering-mass-adoption-of-usdc/](https://irishtechnews.ie/is-samsung-pioneering-mass-adoption-of-usdc/)

生成摘要时出错

---

## 46. Anatomy of a Frontier Lab Agent Intrusion: A Timeline of the July 2026 Incident

**原文标题**: Anatomy of a Frontier Lab Agent Intrusion: A Timeline of the July 2026 Incident

**原文链接**: [https://huggingface.co/blog/agent-intrusion-technical-timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline)

生成摘要时出错

---

## 47. Angels in Coptic Magic I: Introduction

**原文标题**: Angels in Coptic Magic I: Introduction

**原文链接**: [https://www.coptic-magic.phil.uni-wuerzburg.de/index.php/2026/01/16/angels-in-coptic-magic-i-introduction/](https://www.coptic-magic.phil.uni-wuerzburg.de/index.php/2026/01/16/angels-in-coptic-magic-i-introduction/)

生成摘要时出错

---

## 48. A Trampoline

**原文标题**: A Trampoline

**原文链接**: [https://dogdogfish.com/blog/2026/07/29/a-trampoline/](https://dogdogfish.com/blog/2026/07/29/a-trampoline/)

生成摘要时出错

---

## 49. Recursive Filters: SMA, EMA, Low‑Pass, and a Tiny Kalman

**原文标题**: Recursive Filters: SMA, EMA, Low‑Pass, and a Tiny Kalman

**原文链接**: [https://www.staszewski.xyz/blog/recursive-filters/](https://www.staszewski.xyz/blog/recursive-filters/)

生成摘要时出错

---

## 50. Refactoring cuisine: how an Iraqi stew sailed to Singapore

**原文标题**: Refactoring cuisine: how an Iraqi stew sailed to Singapore

**原文链接**: [https://iza.ac/posts/2026/07/the-journey-of-bamya/](https://iza.ac/posts/2026/07/the-journey-of-bamya/)

生成摘要时出错

---

## 51. The Cold Email

**原文标题**: The Cold Email

**原文链接**: [https://zachholman.com/posts/cold-email](https://zachholman.com/posts/cold-email)

生成摘要时出错

---

## 52. Shipping Godot VR and Porting to PSVR2: A Partial Post Mortem

**原文标题**: Shipping Godot VR and Porting to PSVR2: A Partial Post Mortem

**原文链接**: [https://www.claire-blackshaw.com/blog/2026/07/shipping-godot-vr-and-porting-to-psvr2-a-partial-post-mortem/](https://www.claire-blackshaw.com/blog/2026/07/shipping-godot-vr-and-porting-to-psvr2-a-partial-post-mortem/)

生成摘要时出错

---

## 53. Hyatt Regency Walkway Collapse

**原文标题**: Hyatt Regency Walkway Collapse

**原文链接**: [https://en.wikipedia.org/wiki/Hyatt_Regency_walkway_collapse](https://en.wikipedia.org/wiki/Hyatt_Regency_walkway_collapse)

生成摘要时出错

---

## 54. NSF pilots 4-year PhDs with industry research placements

**原文标题**: NSF pilots 4-year PhDs with industry research placements

**原文链接**: [https://www.nsf.gov/news/nsf-partners-universities-industry-pilot-initiative-four](https://www.nsf.gov/news/nsf-partners-universities-industry-pilot-initiative-four)

生成摘要时出错

---

## 55. SQLite in Production: Optimizing WAL Mode, Concurrency, and VFS Layers

**原文标题**: SQLite in Production: Optimizing WAL Mode, Concurrency, and VFS Layers

**原文链接**: [https://micrologics.org/blog/sqlite-in-production-optimizing-wal-mode-concurrency-and-vfs-layers-for-low-latency-app-servers](https://micrologics.org/blog/sqlite-in-production-optimizing-wal-mode-concurrency-and-vfs-layers-for-low-latency-app-servers)

生成摘要时出错

---

## 56. Amiga Graphics Archive

**原文标题**: Amiga Graphics Archive

**原文链接**: [https://amiga.lychesis.net/index.html](https://amiga.lychesis.net/index.html)

生成摘要时出错

---

## 57. Man and the Computer by John G. Kemeny (1972 book by the co-creator of BASIC)

**原文标题**: Man and the Computer by John G. Kemeny (1972 book by the co-creator of BASIC)

**原文链接**: [https://archive.org/details/mancomputerbyjoh0000john](https://archive.org/details/mancomputerbyjoh0000john)

生成摘要时出错

---

## 58. A.I. companies are recruiting electricians and carpenters by the thousands

**原文标题**: A.I. companies are recruiting electricians and carpenters by the thousands

**原文链接**: [https://www.nytimes.com/2026/07/29/business/economy/data-center-electricians-training.html](https://www.nytimes.com/2026/07/29/business/economy/data-center-electricians-training.html)

生成摘要时出错

---

## 59. GCC steering committee announces AI policy

**原文标题**: GCC steering committee announces AI policy

**原文链接**: [https://lwn.net/Articles/1086041/](https://lwn.net/Articles/1086041/)

生成摘要时出错

---

## 60. Steam Client Adds HDR Streaming on Steam Deck OLED, AV1 Video Streaming

**原文标题**: Steam Client Adds HDR Streaming on Steam Deck OLED, AV1 Video Streaming

**原文链接**: [https://www.phoronix.com/news/Steam-Beta-Video-Streaming](https://www.phoronix.com/news/Steam-Beta-Video-Streaming)

生成摘要时出错

---

## 61. Reaping the Whirlwind – Inside the Potomac River Midair Collision

**原文标题**: Reaping the Whirlwind – Inside the Potomac River Midair Collision

**原文链接**: [https://admiralcloudberg.medium.com/reaping-the-whirlwind-inside-the-potomac-river-midair-collision-0475416f2b0f](https://admiralcloudberg.medium.com/reaping-the-whirlwind-inside-the-potomac-river-midair-collision-0475416f2b0f)

生成摘要时出错

---

## 62. Document-borne AI worms can self-propagate through Copilot for Word

**原文标题**: Document-borne AI worms can self-propagate through Copilot for Word

**原文链接**: [https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/)

生成摘要时出错

---

## 63. GPT-5.6 vs. Claude Fable 5 for Physical AI, which performs best?

**原文标题**: GPT-5.6 vs. Claude Fable 5 for Physical AI, which performs best?

**原文链接**: [https://juliahub.com/blog/frontier-models-physical-ai-evaluation](https://juliahub.com/blog/frontier-models-physical-ai-evaluation)

生成摘要时出错

---

## 64. Software Foundations Series

**原文标题**: Software Foundations Series

**原文链接**: [https://softwarefoundations.cis.upenn.edu/](https://softwarefoundations.cis.upenn.edu/)

生成摘要时出错

---

## 65. Cisco FMC static credential vulnerability exploited as a zero-day

**原文标题**: Cisco FMC static credential vulnerability exploited as a zero-day

**原文链接**: [https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-static-cred-BET3Cjh](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-static-cred-BET3Cjh)

生成摘要时出错

---

## 66. Carolina Cloud pays SOFR on unused prepaid credits

**原文标题**: Carolina Cloud pays SOFR on unused prepaid credits

**原文链接**: [https://docs.carolinacloud.io/organizations/prepaid-interest/](https://docs.carolinacloud.io/organizations/prepaid-interest/)

生成摘要时出错

---

## 67. Visualizing the Artemis II Mission

**原文标题**: Visualizing the Artemis II Mission

**原文链接**: [https://foxglove.dev/blog/visualizing-the-artemis-ii-mission](https://foxglove.dev/blog/visualizing-the-artemis-ii-mission)

生成摘要时出错

---

## 68. Handbook.md shows that long policy documents do not reliably govern agents

**原文标题**: Handbook.md shows that long policy documents do not reliably govern agents

**原文链接**: [https://arxiv.org/abs/2607.25398](https://arxiv.org/abs/2607.25398)

生成摘要时出错

---

## 69. Show HN: CheapFoodMap – A map of good meals under $10

**原文标题**: Show HN: CheapFoodMap – A map of good meals under $10

**原文链接**: [https://cheapfoodmap.com/](https://cheapfoodmap.com/)

生成摘要时出错

---

## 70. Lisp moving Forth moving Lisp

**原文标题**: Lisp moving Forth moving Lisp

**原文链接**: [https://letoverlambda.com/textmode.cl/guest/chap8.html](https://letoverlambda.com/textmode.cl/guest/chap8.html)

生成摘要时出错

---

## 71. FTC Acts Against Hims & Hers for Deceptive and Unlawful Privacy Practices

**原文标题**: FTC Acts Against Hims & Hers for Deceptive and Unlawful Privacy Practices

**原文链接**: [https://www.ftc.gov/news-events/news/press-releases/2026/07/ftc-states-act-against-hims-hers-deceptive-unlawful-privacy-practices](https://www.ftc.gov/news-events/news/press-releases/2026/07/ftc-states-act-against-hims-hers-deceptive-unlawful-privacy-practices)

生成摘要时出错

---

## 72. Show HN: A local merge queue for parallel Claude Code agents

**原文标题**: Show HN: A local merge queue for parallel Claude Code agents

**原文链接**: [https://github.com/funador/claude-code-merge-queue](https://github.com/funador/claude-code-merge-queue)

生成摘要时出错

---

## 73. Show HN: Qwen Scribe – local transcription and dictation for Apple Silicon

**原文标题**: Show HN: Qwen Scribe – local transcription and dictation for Apple Silicon

**原文链接**: [https://github.com/VladUZH/qwen-scribe](https://github.com/VladUZH/qwen-scribe)

生成摘要时出错

---

## 74. Steel Bank Common Lisp version 2.6.7

**原文标题**: Steel Bank Common Lisp version 2.6.7

**原文链接**: [https://sbcl.org/all-news.html?2.6.7](https://sbcl.org/all-news.html?2.6.7)

生成摘要时出错

---

## 75. How much can you delegate to agents?

**原文标题**: How much can you delegate to agents?

**原文链接**: [https://newsletter.posthog.com/p/agent-autonomy](https://newsletter.posthog.com/p/agent-autonomy)

生成摘要时出错

---

## 76. Flume Water Monitor 915 MHz Security Is Pretty Good

**原文标题**: Flume Water Monitor 915 MHz Security Is Pretty Good

**原文链接**: [https://waveformsecurity.com/blog/flume/](https://waveformsecurity.com/blog/flume/)

生成摘要时出错

---

## 77. Leopold Aschenbrenner unwinds all public stock positions after steep losses

**原文标题**: Leopold Aschenbrenner unwinds all public stock positions after steep losses

**原文链接**: [https://www.cnbc.com/2026/07/30/leopold-aschenbrenners-hedge-fund-is-facing-steep-ai-losses.html](https://www.cnbc.com/2026/07/30/leopold-aschenbrenners-hedge-fund-is-facing-steep-ai-losses.html)

生成摘要时出错

---

## 78. Darktable

**原文标题**: Darktable

**原文链接**: [https://www.darktable.org/](https://www.darktable.org/)

生成摘要时出错

---

## 79. ReFrame – The EPaper Camera

**原文标题**: ReFrame – The EPaper Camera

**原文链接**: [https://reframe.camera/](https://reframe.camera/)

生成摘要时出错

---

## 80. Try sending "see the below –" to Opus 5

**原文标题**: Try sending "see the below –" to Opus 5

**原文链接**: [https://twitter.com/matthen2/status/2082566186785480708](https://twitter.com/matthen2/status/2082566186785480708)

生成摘要时出错

---

## 81. Kimi K3-256k

**原文标题**: Kimi K3-256k

**原文链接**: [https://www.kimi.com/code/docs/en/kimi-code/models](https://www.kimi.com/code/docs/en/kimi-code/models)

生成摘要时出错

---

## 82. Kimi K3's Design Secret May Be in Its Thinking Traces

**原文标题**: Kimi K3's Design Secret May Be in Its Thinking Traces

**原文链接**: [https://notes.designarena.ai/kimi-k3s-design-secret-may-be-in-its-thinking-traces/](https://notes.designarena.ai/kimi-k3s-design-secret-may-be-in-its-thinking-traces/)

生成摘要时出错

---

## 83. Turning a dumb AC unit smart (without losing my security deposit)

**原文标题**: Turning a dumb AC unit smart (without losing my security deposit)

**原文链接**: [https://prilik.com/blog/post/automating-ac-nyc/](https://prilik.com/blog/post/automating-ac-nyc/)

生成摘要时出错

---

## 84. Excessive time spent online linked to stress and worse mood – study

**原文标题**: Excessive time spent online linked to stress and worse mood – study

**原文链接**: [https://www.theguardian.com/technology/2026/jul/29/excessive-time-spent-online-linked-to-stress-and-worse-mood-study](https://www.theguardian.com/technology/2026/jul/29/excessive-time-spent-online-linked-to-stress-and-worse-mood-study)

生成摘要时出错

---

## 85. More Tailscale tricks for your jailbroken Kindle

**原文标题**: More Tailscale tricks for your jailbroken Kindle

**原文链接**: [https://tailscale.com/blog/jailbroken-kindle-proxy-tun-modes](https://tailscale.com/blog/jailbroken-kindle-proxy-tun-modes)

生成摘要时出错

---

## 86. Enabling two settings tripled our scores on the ARC-AGI-3 benchmark

**原文标题**: Enabling two settings tripled our scores on the ARC-AGI-3 benchmark

**原文链接**: [https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores/](https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores/)

生成摘要时出错

---

## 87. Some thoughts about Anthropic's new cryptanalysis results

**原文标题**: Some thoughts about Anthropic's new cryptanalysis results

**原文链接**: [https://blog.cryptographyengineering.com/2026/07/29/some-notes-about-anthropics-new-results/](https://blog.cryptographyengineering.com/2026/07/29/some-notes-about-anthropics-new-results/)

生成摘要时出错

---

## 88. Disrupting supply chain attacks on NPM and GitHub Actions

**原文标题**: Disrupting supply chain attacks on NPM and GitHub Actions

**原文链接**: [https://github.blog/security/supply-chain-security/disrupting-supply-chain-attacks-on-npm-and-github-actions/](https://github.blog/security/supply-chain-security/disrupting-supply-chain-attacks-on-npm-and-github-actions/)

生成摘要时出错

---

## 89. The New Science of Inflammation

**原文标题**: The New Science of Inflammation

**原文链接**: [https://www.nytimes.com/interactive/2026/07/29/magazine/inflammation-chronic-immune-system-health.html](https://www.nytimes.com/interactive/2026/07/29/magazine/inflammation-chronic-immune-system-health.html)

生成摘要时出错

---

## 90. User Interfaces of the Demo Scene

**原文标题**: User Interfaces of the Demo Scene

**原文链接**: [https://www.datagubbe.se/scenegui/](https://www.datagubbe.se/scenegui/)

生成摘要时出错

---

