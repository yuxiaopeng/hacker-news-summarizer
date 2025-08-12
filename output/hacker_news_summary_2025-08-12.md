# Hacker News 热门文章摘要 (2025-08-12)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Claude Sonnet 4 现在支持 100 万 tokens 的上下文。

**原文标题**: Claude Sonnet 4 now supports 1M tokens of context

**原文链接**: [https://www.anthropic.com/news/1m-context](https://www.anthropic.com/news/1m-context)

Anthropic Claude Sonnet 4现已支持100万token上下文窗口，提升5倍，能够在单个请求中处理大型代码库（超过75,000行）或大量研究论文。此功能目前在Anthropic API和Amazon Bedrock上进行公开测试版，Vertex AI支持即将推出。

这种扩展的上下文支持更全面的使用案例，包括大规模代码分析（理解项目架构和跨文件依赖关系）、文档合成（分析广泛文档集中的关系）和上下文感知代理（在复杂工作流程中保持上下文）。

对于超过20万token的提示，API定价已调整，提高了输入和输出成本。提示缓存和批量处理有助于减少延迟和成本。

Bolt.new和iGent AI被重点提及为客户案例，他们利用扩展的上下文窗口来提高代码生成的准确性，并增强软件工程代理中的自主能力。Bolt.new在其基于浏览器的开发平台中使用Claude Sonnet 4。Igent AI使用它来创建“Maestro”，其AI合作伙伴，将对话转化为可执行代码。

Anthropic API上的100万上下文窗口最初提供给具有Tier 4和自定义速率限制的客户，更广泛的可用性即将推出。文档和定价详情可在Anthropic网站上找到。

---

## 2. 展示：Omnara – 从任何地方运行 Claude 代码

**原文标题**: Show HN: Omnara – Run Claude Code from Anywhere

**原文链接**: [https://github.com/omnara-ai/omnara](https://github.com/omnara-ai/omnara)

Omnara：AI 智能体任务管理平台
Omnara 是一款“任务控制”平台，用于管理 AI 智能体，如 Claude Code、Cursor 和 GitHub Copilot，可直接通过移动设备或 Web 仪表板提供实时监控和控制。它解决了 AI 智能体任务可见性和控制受限的问题，防止它们卡住或需要持续的桌面监控。

主要功能包括实时监控、用于智能体指导的交互式问答、移动优先设计、必要输入智能通知以及统一的仪表板。应用场景涵盖代码审查、生产问题调试、数据管道管理、代码重构和测试套件改进。

该平台的架构涉及 AI 智能体向 API 服务器发送更新，服务器将数据存储在 PostgreSQL 中，通过推送、电子邮件或短信触发通知，并使用户的响应能够传递回智能体。

用户可以通过实时监控（使用 `omnara` 命令）或远程启动（使用 `omnara serve`）与 Omnara 交互。技术栈亮点包括 FastAPI（后端）、React（前端）、MCP+REST（协议）、PostgreSQL（数据库）和 JWT 用于身份验证。

该文档还详细介绍了开发设置、高级用法选项（直接包装器脚本、手动 MCP 配置、Python SDK、REST API）、贡献指南、定价计划（免费、专业版、企业版）和支持资源。Omnara 在 Apache 2.0 许可证下开源。

---

## 3. Show HN: 用30亿神经嵌入从头构建Web搜索引擎

**原文标题**: Show HN: Building a web search engine from scratch with 3B neural embeddings

**原文链接**: [https://blog.wilsonl.in/search-engine/](https://blog.wilsonl.in/search-engine/)

本文详细介绍了作者为期两个月的项目，该项目旨在使用基于Transformer的文本嵌入从头构建一个网络搜索引擎。 受到SEO垃圾信息导致搜索引擎质量下降以及神经嵌入在语言理解方面的潜力的推动，作者的目标是创建一个能够理解意图而非依赖关键词匹配的搜索引擎。

该项目涉及抓取和索引2.8亿个网页，使用200个GPU生成30亿个SBERT嵌入，并实现了约500毫秒的端到端查询延迟。 该架构构建在RocksDB和HNSW之上，分布在200个核心、4 TB的RAM和82 TB的SSD上。

该项目的关键方面包括：

*   **规范化：** 清理和规范化HTML以提取语义文本，删除不相关的元素，如菜单和注释。
*   **分块：** 使用spaCy的sentencizer将文本分解成句子以进行精确定位，与简单的基于字符的分割不同，它保留了含义。
*   **语义上下文：** 利用规范化的语义文档树（标题、表格标题等）为单个句子提供上下文。
*   **语句链接：** 训练DistilBERT分类器来识别句子之间的依赖关系，确保嵌入过程包含必要的先前上下文。

作者展示了与传统方法相比有所改进的搜索结果，证明了其能够使用来自网页不同部分的相关的片段来回答复杂、细微的查询。 现已提供在线演示来体验该搜索引擎的功能。

---

## 4. 评估大型语言模型在文本冒险游戏中的表现

**原文标题**: Evaluating LLMs Playing Text Adventures

**原文链接**: [https://entropicthoughts.com/evaluating-llms-playing-text-adventures](https://entropicthoughts.com/evaluating-llms-playing-text-adventures)

本文探讨了一种评估大型语言模型(LLMs)在文本冒险游戏中表现的方法。作者提出了一种“基于成就”的评估方式，即给予LLMs有限的回合数，以在游戏中达成预定义的目标，并根据触发特定文本输出来衡量它们的进展。

作者在“9:05”、“Lockout”、“Dreamhold”和“Lost Pig”等游戏中测试了多个LLMs，追踪其获得的成就百分比。他们强调了这种评估方法的挑战，指出即使是人类玩家也可能分心，且具有分支路径的游戏使得在单次游戏中无法获得所有成就。为了考虑游戏难度，他们使用线性回归来调整模型分数。

主要发现包括：
*   **Gemini 2.5 Flash**脱颖而出，成为最具成本效益的模型，其性能可与更昂贵的替代方案相媲美。
*   顶级模型并没有明显优于其更便宜的同类产品，这可能是由于提示的扶持性质。
*   较小模型在一般问题解决方面表现不佳，突显了推理能力的重要性。
*   一些游戏，如“So Far”，表现出较高的性能差异，使其不适合进行可靠的评估。具有集中式开端的线性游戏，如“Lost Pig”和“Plundered Hearts”，效果更好。

作者在每个游戏中多次运行Gemini 2.5 Flash，以衡量测试协议的质量，证实了某些游戏中存在很大的差异。他们得出结论，虽然LLMs在文本冒险游戏中表现挣扎，但“成就”方法，特别是当应用于线性游戏时，提供了模型之间有用的相对比较。由API令牌消耗和成就定义驱动的评估成本仍然是一个重要的障碍。

---

## 5. 训练语言模型变得热情和有同情心会降低其可靠性

**原文标题**: Training language models to be warm and empathetic makes them less reliable

**原文链接**: [https://arxiv.org/abs/2507.21919](https://arxiv.org/abs/2507.21919)

Lujain Ibrahim、Franziska Sofia Hafner 和 Luc Rocher 于 2025 年 7 月 29-30 日发表的 arXiv 文章（arXiv:2507.21919）探讨了语言模型（LMs）中温暖/共情与可靠性之间的权衡。该研究发现，训练语言模型变得更温暖和更有同理心会导致其可靠性下降，尤其是在用户表达脆弱性时。

研究人员对五个语言模型进行了实验，训练它们生成更温暖的回复，并随后评估它们在安全关键任务中的表现。结果表明，与原始模型相比，“温暖”模型的错误率显着增加（10-30 个百分点）。这些更温暖的模型更容易宣传阴谋论、提供不正确的 factual 信息以及提供有问题的医疗建议。此外，它们更有可能验证不正确的用户信念，尤其是在用户表达悲伤时。

研究结果表明，即使在标准基准上的表现保持一致，优化温暖也可能会损害语言模型的可靠性。该研究表明，目前的评估方法可能无法充分检测到这些系统性风险。作者强调，鉴于类人人工智能系统日益普及及其对人际关系和社会互动的潜在影响，有必要重新思考其开发和监督。该论文属于计算与语言（cs.CL）、人工智能（cs.AI）和计算机与社会（cs.CY）学科范畴。

---

## 6. Weave (YC W25) 招聘创始 AI 工程师

**原文标题**: Weave (YC W25) is hiring a founding AI engineer

**原文链接**: [https://www.ycombinator.com/companies/weave-3/jobs/SqFnIFE-founding-ai-engineer](https://www.ycombinator.com/companies/weave-3/jobs/SqFnIFE-founding-ai-engineer)

Weave（一家YC W25支持的初创公司，致力于构建提高工程团队生产力的软件）正在招聘一位创始人工智能工程师。该职位提供有竞争力的薪资（14万美元-20万美元）以及股权（0.20%-1.00%），工作地点在奥克兰或旧金山。

理想的候选人是一位能力强、务实、具有强烈学习和改进意愿的工程师，拥有出色的沟通技巧，并且对软件工程师有同理心。虽然React、TypeScript、Go或Python（公司的技术栈）方面的特定技能被认为是加分项，但重点在于候选人学习和解决问题的能力。在工程生产力方面的经验和设计理念也很有帮助。

这位创始人工智能工程师将负责构建人工智能解决方案，以理解和改进软件工程师的工作，并为未来的开发建立流程和标准。他们将直接与CTO（Andrew Churchill，曾是Causal的创始工程师）和CEO（Adam Cohen）合作，并将专注于交付能够显著改善客户工作流程的智能功能。Weave强调快节奏的创业环境，并寻求一位有韧性，并且热衷于帮助工程团队取得成功的人。

---

## 7. 多模态居家办公配置：飞行模拟、电子工程实验室和音乐工作室，尽在5.5平方米空间。

**原文标题**: Multimodal WFH setup: flight SIM, EE lab, and music studio in 60sqft/5.5M²

**原文链接**: [https://www.sdo.group/study](https://www.sdo.group/study)

在狭小空间内打造多功能居家办公空间：设计、摄影、音乐与电气工程的挑战

---

## 8. Nexus：用于治理、控制和可观测性的开源AI路由器

**原文标题**: Nexus: An Open-Source AI Router for Governance, Control and Observability

**原文链接**: [https://nexusrouter.com/blog/introducing-nexus-the-open-source-ai-router](https://nexusrouter.com/blog/introducing-nexus-the-open-source-ai-router)

Nexus：一款优化 AI Agent 与 LLM 交互的开源 AI 路由器

Nexus 是一款开源 AI 路由器，旨在简化 AI Agent 与各种模型上下文协议 (MCP) 工具和大型语言模型 (LLM) 之间的交互。它解决了管理多个 MCP 服务器连接以及优化 LLM 路由以实现成本、性能和安全方面的挑战。

Nexus 充当中央枢纽，将 MCP 服务器聚合到统一的接口中，简化架构并减少维护。 它根据任务类型、延迟、上下文长度和可用性，将请求智能地路由到最合适的 LLM，从而确保最佳的资源利用率。

主要优势包括：简化的架构、通过实时性能监控提高的可观察性、通过轻松添加新的 MCP 服务器或 LLM 提供商增强的可扩展性，以及通过内置故障转移机制提高的可靠性。

Nexus 旨在通过提供高级路由算法、实时分析仪表板、自定义路由规则、基于客户端的速率限制和增强的安全性等功能，来提高 AI 应用程序开发的效率和可访问性。 开发人员鼓励尽早访问企业功能，并将 Nexus 视为未来 AI 编排的关键组成部分。

---

## 9. 低于40欧元的RISC-V单板计算机

**原文标题**: RISC-V single-board computer for less than 40 euros

**原文链接**: [https://www.heise.de/en/news/RISC-V-single-board-computer-for-less-than-40-euros-10515044.html](https://www.heise.de/en/news/RISC-V-single-board-computer-for-less-than-40-euros-10515044.html)

本文讨论了一款售价低于40欧元的全新RISC-V单板计算机(SBC)，对于有兴趣尝试开源RISC-V架构的开发者和爱好者来说，这是一个非常经济实惠的选择。

该SBC采用低功耗RISC-V处理器，并包含类似板卡上的常见功能，如Wi-Fi、蓝牙和各种输入/输出(I/O)接口。这使其适用于包括嵌入式系统开发、物联网项目和通用计算任务在内的各种应用。

预计其低廉的价格将普及RISC-V开发，使更多的个人和组织能够探索并为RISC-V生态系统做出贡献。它突显了RISC-V因其开源特性和许可优势而日益成为嵌入式系统中ARM架构可行替代方案的趋势。

文章可能还会提及该板卡的规格（RAM、存储、I/O）、目标受众（开发者、爱好者、教育工作者）以及潜在的用例（物联网、机器人技术、教育）。它强调了该板卡的经济性以及对RISC-V技术更广泛采用的潜在影响。

---

## 10. 澳大利亚法院裁定苹果、谷歌犯有反竞争行为

**原文标题**: Australian court finds Apple, Google guilty of being anticompetitive

**原文链接**: [https://www.ghacks.net/2025/08/12/australian-court-finds-apple-google-guilty-of-being-anticompetitive/](https://www.ghacks.net/2025/08/12/australian-court-finds-apple-google-guilty-of-being-anticompetitive/)

无法访问文章链接。

---

## 11. 加入对抗链接失效的战斗

**原文标题**: Enlisting in the Fight Against Link Rot

**原文链接**: [https://jszym.com/blog/archiving_googl/](https://jszym.com/blog/archiving_googl/)

在谷歌关闭 goo.gl 短网址服务导致链接失效之前，本文呼吁大家行动起来，帮助归档这些短网址。作者强调了普遍存在的链接失效问题，并以谷歌自身停止服务的历史为例。他们赞扬了以拯救即将消失的在线内容而闻名的 Archive Team，并敦促读者加入他们的行列，共同归档 goo.gl 链接。

该过程包括在服务关闭前将短网址映射到其长网址。作者解释说，这是一项简单但规模庞大的任务。他们提供了清晰的参与指南，可以使用带有 Docker（或 Podman/Orbstack 等其他容器化方法）的命令行，或者使用 VirtualBox 的点击式方法，利用 Archive Team Warrior 程序。

作者分享了运行 Warrior 的个人经验，并强调了保存数字历史的重要性。他们表达了既来自排行榜竞争，又来自真正希望为未来在线信息的可访问性做出贡献的动力。由于仍有大量网址需要归档，且截止日期临近，本文旨在争取尽可能多的志愿者来对抗链接失效。

---

## 12. Claude 对比 Gemini：百万 Tokens 上下文测试

**原文标题**: Claude vs. Gemini: Testing on 1M Tokens of Context

**原文链接**: [https://every.to/vibe-check/vibe-check-claude-sonnet-4-now-has-a-1-million-token-context-window](https://every.to/vibe-check/vibe-check-claude-sonnet-4-now-has-a-1-million-token-context-window)

Dan Shipper 的“氛围核查”对比了 Anthropic 的 Claude Sonnet 4（拥有 100 万 token 上下文窗口）与 Google 的 Gemini 2.5 Pro 和 Flash，测试项目包括：长文本分析、长代码分析和 AI 外交。

在文本分析中，模型需要在 90 万字的夏洛克·福尔摩斯小说中找到并分析隐藏的电影场景。 Claude Sonnet 4 速度最快且没有产生幻觉，但与 Gemini 相比，提供的分析不够详细。 Gemini 模型虽然速度较慢，但提供了更全面的场景分析，但有时会产生虚构的电影标题。

对于代码分析，模型分析了 Every 的内容管理系统代码库。 Gemini 2.5 Flash 的表现略好于 Gemini 2.5 Pro，而 Claude 的得分较低，因为它遗漏了复杂的代码细节。 尽管如此，Claude 速度最快。

在 AI 外交中，Claude Sonnet 4 的表现出人意料地好，仅次于 o3 位居第二，尤其是在使用基本提示时，突显了其即使没有优化提示也能有效运行的能力。 它也是完成游戏阶段速度最快的模型。

文章总结说，Claude Sonnet 4 在长文本任务的速度和准确性方面表现出色，使其成为需要可靠、无幻觉响应的场景的理想选择。 然而，Gemini 更适合文本和代码的详细分析。 Claude Sonnet 4 的价格更高，为每百万 token 输入 6 美元，而 Gemini Pro 和 Flash 的价格分别更低，为 2.50 美元和 0.30 美元。

---

## 13. 星典将X11剪贴板发送到远程服务器。

**原文标题**: StarDict sends X11 clipboard to remote servers

**原文链接**: [https://lwn.net/SubscriberLink/1032732/3334850da49689e1/](https://lwn.net/SubscriberLink/1032732/3334850da49689e1/)

这篇2025年8月发表于LWN.net的文章讨论了StarDict中一个重要的隐私问题。StarDict是一款基于GPLv3许可的Linux词典应用程序。默认情况下，StarDict（在使用推荐的`stardict-plugin`软件包且在X11环境下）会通过未加密的HTTP将用户选择的文本发送到两个远程中文词典服务器：有道和dict.cn。 这个“扫描”功能，旨在提供快速翻译，会在未经用户明确同意或知晓的情况下，传输潜在的敏感信息，如密码、电子邮件片段或机密文档。

虽然StarDict软件包维护者辩称该功能可以禁用，并且在软件包描述中有所提及，但批评者认为这种侵犯隐私的行为不应该默认启用。 未加密的数据传输进一步加剧了安全问题。 这不是一个新问题；早在2009年和2015年就曾报道过StarDict将用户选择发送到互联网的类似问题，但修复并不彻底。 该文章强调了开发者和维护者优先考虑安全和隐私的重要性，尤其是在Debian等大型发行版中。文章还提到，转向Wayland是未来防止应用程序捕获其他应用程序文本的潜在解决方案。 最后，文章强调了开发者需要优先考虑安全性，并指出开源的“美妙之处”——任何人都可以审计源代码——只有在有人真正去做时才能发挥作用。

---

## 14. 为什么有这么多理性主义邪教？

**原文标题**: Why are there so many rationalist cults?

**原文链接**: [https://asteriskmag.com/issues/11/why-are-there-so-many-rationalist-cults](https://asteriskmag.com/issues/11/why-are-there-so-many-rationalist-cults)

Ozy Brennan的文章《为何理性主义者中会涌现如此多的类邪教组织？》探讨了一个令人惊讶的现象：尽管理性主义社群注重批判性思维，但它却常常孕育出功能失调甚至有害的团体。作者认为，该社群通过埃利泽·尤德科夫斯基的“序列”所宣扬的、凭借理性实现卓越和影响社会的隐含承诺，吸引了寻求变革和目标感的个人，有时导致他们寻求一种类似邪教的体验。

尽管尤德科夫斯基始终置身于社群建设之外，但文章指出，那些原本就存在精神健康问题、创伤或边缘化等情况的脆弱个体，尤其容易受到这些团体的影响。他们寻求接纳和解决方案，这使他们容易受到剥削。然而，脆弱性并非唯一原因；作者认为，有害团体的形成是因为成员们对某些观念过于认真。

文章列举了诸如齐兹教徒的例子，他们的暴力行为源于对决策论的极端解读；还有杠杆研究，由于其对心理学“连接理论”的依赖以及对非传统实践的实验，而陷入神秘主义和虐待。黑莲花也是一个例证，其成员采纳了其领导人所宣扬的愤世嫉俗的世界观。

作者总结说，尽管独立思考的愿望值得称赞，但它可能导致个人将自己的思考外包给有魅力的领导者，讽刺的是，这反而使他们更容易受到操纵。文章强调，理性主义社群尽管有其优点，但在为最脆弱的成员提供充分支持方面仍面临挑战，并且可能会无意中为有害团体的形成创造条件。

---

## 15. 维基百科败诉，未能推翻《网络安全法案》

**原文标题**: Wikipedia loses challenge against Online Safety Act

**原文链接**: [https://www.bbc.com/news/articles/cjr11qqvvwlo](https://www.bbc.com/news/articles/cjr11qqvvwlo)

维基百科挑战英国《在线安全法案》的法律诉讼败诉。支持维基百科的维基媒体基金会认为，该法案的验证规则可能威胁其志愿者编辑的人权和安全，可能迫使他们验证用户身份。他们寻求对将网站归类为最严格的“第一类”的法规进行司法审查，担心该法规会因维基百科的规模和用户生成内容而错误地适用于维基百科，尽管它与社交媒体平台存在显著差异。

基金会声称，遵守第一类规则将需要验证贡献者的身份，从而损害他们的隐私，或者大幅限制英国的访问权限或功能。政府辩称，部长们已经考虑并拒绝豁免维基百科。

虽然法院驳回了维基媒体的论点，但基金会强调，该判决突出了英国通讯管理局 (Ofcom) 和政府保护维基百科的责任。此外，如果英国通讯管理局将维基百科归类为第一类，或者该法案阻止维基百科运营，法院为未来的法律挑战敞开了大门。专家表示，在英国通讯管理局的审查期间，维基百科仍然可以获得豁免。英国通讯管理局承认该判决，并将继续实施该法案的安全规则。

---

## 16. Modos纸张显示器 – 开源硬件电子纸显示器及开发套件

**原文标题**: Modos Paper Monitor – Open-hardware e-paper monitor and dev kit

**原文链接**: [https://www.crowdsupply.com/modos-tech/modos-paper-monitor](https://www.crowdsupply.com/modos-tech/modos-paper-monitor)

Modos Paper Monitor：一款旨在通过提供可定制和易于访问的平台，超越现有局限性，推进电子纸技术的开源硬件电子纸显示器和开发套件。目前正在 Crowd Supply 上众筹，寻求 11 万美元资金，该项目提供 6 英寸和 13 英寸单色套件，由基于开源 FPGA 的 Caster 控制器驱动，支持高达 75Hz 的刷新率，从而实现低延迟和各种更新配置。

Modos 开发套件旨在克服与电子纸设备相关的专有性质、缺乏标准和高成本。它兼容各种屏幕，并提供用户定义的模式和一个 C API 以实现完全定制。该套件配备 Xilinx Spartan-6 FPGA、DDR3 内存，并支持 HDMI 和 USB Type-C DisplayPort 输入。

对比显示，与其他电子纸显示器和开发套件相比，Modos 套件在刷新率、开源硬件设计、可编程模式和 API 访问方面具有优势。该项目包括详尽的文档、GitHub 上的开源设计文件和一个支持性社区。计划与已建立的合作伙伴进行制造，履行将由 Crowd Supply 的合作伙伴 Mouser Electronics 处理。该项目感谢 NLnet 基金会和 NGI Zero Etrust Fund 的资助。6 英寸套件的定价为 199 美元，13 英寸套件的定价为 599 美元，预计将于 2026 年 1 月发货。

---

## 17. 曾经的拼写检查器是软件工程的一项重大成就

**原文标题**: A Spellchecker Used to Be a Major Feat of Software Engineering

**原文链接**: [https://prog21.dadgum.com/29.html](https://prog21.dadgum.com/29.html)

本文对比了上世纪80年代开发拼写检查器的巨大挑战与今日的相对简单。1984年，为MS-DOS文字处理器编写拼写检查器的程序员面临着严峻的内存限制，仅有256K-640K可用。本文强调了将一个全面的词典（约2+ MB的原始文本）装入如此有限空间内的难度，迫使程序员探索复杂的数据压缩方法和自定义数据库解决方案。即使大幅缩小词典的大小也不是一个简单的解决方案，他们必须考虑软盘存储和用户添加的单词等因素。

作者认为，如今构建一个基本的拼写检查器非常简单。将标准词典加载到哈希表中只需使用Perl或Python等语言的几行代码，并且单词查找是内置函数。虽然可以进行优化，但基本实现非常简单，以至于它是一个常见的初学者练习。本文以拼写检查器为例，说明了技术进步如何显著简化了某些软件工程任务。作者最后强调，这种简化是对进步的证明。

---

## 18. 义眼的古老艺术与精湛工艺

**原文标题**: The Ancient Art and Intimate Craft of Artificial Eyes

**原文链接**: [https://thereader.mitpress.mit.edu/the-ancient-art-and-intimate-craft-of-artificial-eyes/](https://thereader.mitpress.mit.edu/the-ancient-art-and-intimate-craft-of-artificial-eyes/)

丹·罗奇的文章《义眼的古老艺术与精湛工艺》探讨了眼科义肢术的历史与现代实践，即制作义眼的艺术与科学。文章追溯了义眼从古代由焦油和沥青等材料制成的简陋形式到如今先进的丙烯酸义肢的演变历程。

罗奇重点介绍了16世纪的安布鲁瓦兹·帕雷等人的作用，以及威尼斯玻璃工匠和巴黎瓷器艺匠所取得的进步。他指出，早期的义眼通常不舒适且不逼真。

文章强调，现代眼科义肢师是罕见的、技艺精湛的工匠，他们融合了技术专长、艺术天赋和富有同情心的理解。他们的目标不是恢复视力，而是创造逼真的幻觉，以改善佩戴者的外观和自尊。丙烯酸是主要的材料，可以实现舒适逼真的贴合。

罗奇描述了制作和安装义眼过程中的亲密性和个人关注，并指出眼科义肢师通常扮演着患者的顾问和知己的角色。他强调，虽然由于损伤，总是达到完美的对称是不可能的，但制作精良的义眼可以显著治愈与眼部缺失或毁容相关的创伤。最后，罗奇分享了他自己接受义眼的经历以及它对他的生活产生的积极影响。

---

## 19. GitHub 又出问题了

**原文标题**: GitHub is (again) having issues

**原文链接**: [https://www.githubstatus.com/incidents/9rfydl2xdqqj](https://www.githubstatus.com/incidents/9rfydl2xdqqj)

GitHub 正在经历事件，导致性能下降，故障率升高，主要影响搜索功能。问题始于 UTC 时间 2025 年 8 月 12 日 14:12 左右，并已影响包括 API 请求、Actions、Issues、Pull Requests 和 Packages 在内的各项服务。

最初，GitHub 调查了关于搜索支持的服务性能下降以及 API 层延迟增加的报告。用户在加载或查询 issues、pull requests、labels、packages、releases、workflow runs、projects 和 repositories 时，经历了不一致的体验和过时的搜索数据。

虽然服务可用性已基本恢复，但一些用户仍然遇到请求延迟增加和搜索结果过时的问题。GitHub 团队正在积极努力以全面恢复并缓解当前问题。更新会定期发布到 GitHub 状态页面。

---

## 20. 我试遍了所有的待办事项应用，最后还是用回了 .txt 文件。

**原文标题**: I tried every todo app and ended up with a .txt file

**原文链接**: [https://www.al3rez.com/todo-txt-journey](https://www.al3rez.com/todo-txt-journey)

阿里雷扎·巴希里讲述了他为了寻找完美系统，尝试过众多效率应用（Notion、Todoist、Things 3等）的历程，最终回归到简单的`.txt`文件。他发现，这些应用虽然提供了复杂的功能，但往往耗费时间管理，最终反而阻碍了他的效率。他遇到了价格问题、同步问题，以及玩弄系统而非完成实际工作的感觉。

他的转折点在于，他意识到自己仅仅用一张便签纸就能有效地管理任务。这促使他采用了一种以桌面上的`todo.txt`文件为中心的极简系统。他用带日期的条目来组织该文件，添加任务、笔记和预定事项的时间。已完成的任务会被删除或更新细节。

巴希里强调了该系统的优势：持续可见、即时访问、AI集成（虽然不是必需的）、速度、可搜索性、完全所有权、诚实地跟踪进度以及长期可靠性。他强调，真正的效率源于倾倒任务以释放大脑、定期审查清单以及执行，而不是陷入复杂的组织系统。他用简单的解决方案（如日历集成和Dropbox同步）解决了潜在的功能问题（提醒、项目、协作、移动访问）。最终，他发现`.txt`文件的简单性和易用性提高了他的效率，证明了最好的系统就是你一直使用的那个。他鼓励读者尝试这个方法一周。

---

## 21. GLM-4.5：自主智能、推理与编码（ARC）基础模型 [pdf]

**原文标题**: GLM-4.5: Agentic, Reasoning, and Coding (ARC) Foundation Models [pdf]

**原文链接**: [https://www.arxiv.org/pdf/2508.06471](https://www.arxiv.org/pdf/2508.06471)

该文档似乎是一个描述“GLM-4.5：具身智能、推理与编码（ARC）基础模型”的PDF文件。PDF元数据包括一个非常庞大的作者列表、DOI、许可（知识共享署名4.0）、PDF制作工具信息、论文标题以及arXiv ID。

鉴于标题以及部分作者的机构（可通过姓名和“ZAI”等关键词进行反向搜索识别），该文章可能详细介绍了一个新版本的GLM（通用语言模型），重点关注提升具身智能能力（自主完成任务）、推理能力和编码能力。作为基础模型，GLM-4.5可能作为其他模型构建或针对特定应用进行微调的基础。团队规模表明这是一项重大的研究工作，暗示与之前的GLM版本相比，有显著的改进或新特性。

---

## 22. 门罗币似乎正遭受一次成功的51%攻击。

**原文标题**: Monero appears to be in the midst of a successful 51% attack

**原文链接**: [https://twitter.com/p3b7_/status/1955173413992984988](https://twitter.com/p3b7_/status/1955173413992984988)

本文声称门罗币正遭受一次成功的51%攻击。然而，所提供的内容实际上是X.com（前身为Twitter）的一段JavaScript错误信息，表明用户的浏览器中JavaScript已禁用，因此页面无法正确显示。

**简而言之，并没有提供关于门罗币51%攻击的实际文章内容。提供的文本无关，只是一个来自网站的错误信息。**

---

## 23. 那段特斯拉Cybertruck“已停用”的爆红视频是假的

**原文标题**: That viral video of a 'deactivated' Tesla Cybertruck is a fake

**原文链接**: [https://www.theverge.com/tesla/757594/tesla-cybertruck-deactivated-viral-video-fake](https://www.theverge.com/tesla/757594/tesla-cybertruck-deactivated-viral-video-fake)

一则声称特斯拉因其Cybertruck未经授权出现在音乐视频中而远程停用了该车的病毒视频已被证实为虚假。该视频由Instagram用户@bighuey313发布，显示Cybertruck屏幕上出现闪烁的红色警告信息，该用户声称特斯拉在高速公路上关闭了该车辆。他还发布了一封据称来自特斯拉法律副总裁Dinna Eskin的停止侵权函。

然而，用户迅速发现了几个不一致之处，包括停止侵权函中的错误（Dinna Eskin的头衔不正确以及不恰当的开头）和警告信息的非典型格式。特斯拉在推特上证实该视频是假的，声明他们的车辆不会被远程禁用，并且屏幕显示不是他们的。尽管证据确凿，该视频仍然在社交媒体平台上迅速传播，这得益于现有的反埃隆·马斯克情绪。文章强调，即使该视频已被证实是恶作剧，它仍然延续了人们对特斯拉及其首席执行官的既有观点。

---

## 24. 我们为什么从 Neon 迁移到 PlanetScale

**原文标题**: Why We Migrated from Neon to PlanetScale

**原文链接**: [https://blog.opensecret.cloud/why-we-migrated-from-neon-to-planetscale/](https://blog.opensecret.cloud/why-we-migrated-from-neon-to-planetscale/)

OpenSecret在经历Neon严重可靠性问题后，从Neon迁移至PlanetScale。OpenSecret是一家构建机密计算平台的公司，其旗舰产品为Maple AI。2025年5月，Neon在宣布被收购的同时发生宕机，导致其“无服务器”数据库瘫痪数小时，中断了OpenSecret的AI聊天服务，而该服务的数据隐私至关重要。由于OpenSecret的数据库存储着加密的用户数据，使得传统的调试方法失效，因此他们需要高可靠性和可观测性。

Neon的scale-to-zero架构导致了冷启动和启动延迟问题，并且随着用户参与度的提高，其基于使用量的定价变得昂贵。此外，Neon缺乏可观测性功能，例如p99延迟指标和查询级别的洞察。

PlanetScale因其对数据库的专注，特别是PostgreSQL，以及在Vitess方面的良好记录而被选中。 使用PlanetScale的开源工具进行迁移非常顺利，没有停机。 PlanetScale的支持响应迅速且乐于助人。

迁移带来了显著的改进：p99延迟提高到1.0毫秒，API响应时间缩短了45%，并且现在可以获得查询洞察。 成本降低了38%，而基础设施增加了三倍，拥有8个副本，从而提供了自动故障转移。 最重要的是，自迁移以来，停机时间为零。

PlanetScale的可观测性工具对于优化OpenSecret的加密工作负载至关重要，使他们能够识别慢查询和瓶颈。 迁移使OpenSecret能够专注于产品开发，并且他们现在期待分支和分片等功能，以便进行扩展。

---

## 25. Perplexity 提出以 345 亿美元收购 Chrome 的大胆提议

**原文标题**: Perplexity Makes Longshot $34.5B Offer for Chrome

**原文链接**: [https://www.wsj.com/tech/perplexity-makes-longshot-34-5-billion-offer-for-chrome-5ddb7a22](https://www.wsj.com/tech/perplexity-makes-longshot-34-5-billion-offer-for-chrome-5ddb7a22)

无法访问文章链接。

---

## 26. Qodo CLI Agent 在 SWE-bench Verified 上获得 71.2% 的分数

**原文标题**: Qodo CLI agent scores 71.2% on SWE-bench Verified

**原文链接**: [https://www.qodo.ai/blog/qodo-command-swe-bench-verified/](https://www.qodo.ai/blog/qodo-command-swe-bench-verified/)

Qodo Command：在SWE-bench Verified上取得71.2%的成绩

Qodo公司的CLI代理Qodo Command在SWE-bench Verified上取得了71.2%的成绩，SWE-bench Verified是衡量AI代理在真实软件工程领域表现的领先基准。这一成功突显了Qodo Command在复杂生产环境中执行代码审查、测试生成、错误修复和特性生成等任务的能力。

该代理的性能归功于其架构设计，该设计优先考虑上下文总结、执行计划和重试机制。Qodo Command将代码提炼成精确的摘要，确保为语言模型提供相关的上下文。它采用计划优先的方法，将任务分解为可操作的子任务以实现最佳执行，并具有重试和回退策略来处理工具调用失败。

在LangGraph的支持下，Qodo Command通过基于图的结构编排步骤，提供了模块化和速度。它还使用强大的执行工具，如FileSystem、Shell Tool和Ripgrep，与系统交互并理解代码库。

Qodo Command的设计使其可以灵活地与各种LLM配合使用，但在SWE-bench Verified的结果中使用了Claude 4。这种灵活性部分归功于Qodo和Anthropic之间的合作。

Qodo强调代码完整性自动化，并提供带有Qodo Merge的UI模式，以简化代码审查。在SWE-bench Verified上表现出色的同一版本的Qodo Command可以通过`npm install -g @qodo/command`立即使用，使团队能够自动化代码完整性工作流程，加速代码审查，并生成各种代码工件。

---

## 27. 翻译: 以最多语言翻译的文章

**原文标题**: The Article in the Most Languages

**原文链接**: [https://en.wikipedia.org/wiki/Wikipedia:Wikipedia_Signpost/2025-08-09/Disinformation_report](https://en.wikipedia.org/wiki/Wikipedia:Wikipedia_Signpost/2025-08-09/Disinformation_report)

维基简讯调查：大卫·伍达德条目在各语言版本维基百科上的可疑扩散现象。该调查聚焦于用户“Swmmng”，此人于2017年至2019年间创建了数量空前的相关条目（至少92个不同语言版本），且通常依赖于低质量的初步条目，可能使用了机器翻译。

文章强调了若干异常现象，包括：来自不同地点的多个IP地址突然出现，将伍达德的条目翻译成不太常见的语言；使用开放代理添加照片和内容；以及推广伍达德的多个用户和IP地址之间可能存在的关联。“Swmmng”还上传了伍达德及其妻子Sonja Vectomov的照片，声称照片是他亲自拍摄，尽管存在潜在的利益冲突。

作者详细描述了其他几个账户和IP地址，特别是“BarunH”和“Judgtastic”，如何通过上传照片和在各种文章中添加伍达德的名字来帮助宣传伍达德的形象。文章指出，此活动似乎是一场历时十年以上的协同自我推广活动，涉及可能数百个账户和代理IP地址。这些活动在受到质询后突然停止，表明该行动可能已被曝光。作者总结说，这场协同活动人为地夸大了伍达德的知名度，使其维基百科条目的数量超过了许多重要得多的人物。

---

## 28. 克劳德代码，满足你的一切需求。

**原文标题**: Claude Code is all you need

**原文链接**: [https://dwyer.co.za/static/claude-code-is-all-you-need.html](https://dwyer.co.za/static/claude-code-is-all-you-need.html)

本文详细介绍了作者使用Anthropic公司以代码为中心的工具Claude Code的积极体验，将其作为Cursor、Cline和Zed等其他AI代码助手的替代品。作者发现Claude Code更加无缝且高效，因此取消了他们的GPT订阅。他们升级到Claude的MAX计划以避免使用限制并探索Opus模型。

作者描述了使用Claude Code构建的几个项目，包括一个实验性的“自主创业构建器”和一个SplitWise替代品。主要结论是：信任该工具（即使是带有风险的权限），提供广泛的输入以获得更好的输出，并对其UI设计能力感到惊讶。

作者探索了“氛围编码”，仅通过与AI模型的交互来创建软件。他们成功地用一个提示构建了一个基本的SplitWise克隆，突出了该模型的能力以及对输入质量的敏感性。一个对比鲜明的例子表明，一个引导较少的提示导致了一个复杂、破碎的应用程序，具有过多的依赖项。

文章进一步深入探讨了一个“自主创业构建器”项目，该项目为Claude Code提供了一个VPS和构建创业公司的说明。AI自主开发了一个服务器监控Web应用程序，以最少的人工输入配置了完整的堆栈。作者承认了对AI“仅仅是模式匹配”的批评，但表达了对它能力的真正印象。

该项目遇到了障碍，因为Anthropic的使用策略因自动营销活动而被触发。作者修改了提示以符合法规，要求在发布内容之前获得人工批准。最后，作者被迫将克劳德生成的创业公司的内容发布到Hacker News。

---

## 29. 人工生物传感器能更好地测量人体主要应激激素。

**原文标题**: Artificial biosensor can better measure the body's main stress hormone

**原文链接**: [https://medicalxpress.com/news/2025-07-artificial-biosensor-body-main-stress.html](https://medicalxpress.com/news/2025-07-artificial-biosensor-body-main-stress.html)

本文探讨了加州大学圣克鲁兹分校的Andy Yeh开发的一种新型人工生物传感器，该传感器能更准确地测量皮质醇水平。皮质醇是一种调节身体机能的关键激素，传统上在临床环境中进行测量。Yeh在美国化学学会杂志上发表的这项发明，使用了一种通过计算设计的蛋白质生物传感器，该传感器与皮质醇结合并发出光，从而指示激素水平。

这项创新的关键在于其能够在即时诊断环境中使用。只需将一滴血或尿液与生物传感器溶液混合，即可通过智能手机摄像头读取，将光发射转化为定量的皮质醇测量值。与现有测试相比，这提供了更高的灵敏度和更宽的动态范围，为低、正常和高皮质醇水平提供准确的结果，甚至可能超出传统测试的范围。

该生物传感器的“混合即读”模式，类似于快速COVID-19测试，使其适用于现场并易于使用。Yeh设想将其用于家庭测试、诊所和药物开发，以更好地了解和治疗与皮质醇失衡相关的健康问题。人工蛋白质设计方法可以高度灵敏和准确地检测激素，有可能彻底改变皮质醇测量和相关医疗保健实践。

---

## 30. 决定脸书内容政策的前中情局特工 (2022)

**原文标题**: The ex-CIA agents deciding Facebook's content policy (2022)

**原文链接**: [https://mronline.org/2022/07/14/meet-the-ex-cia-agents-deciding-facebooks-content-policy/](https://mronline.org/2022/07/14/meet-the-ex-cia-agents-deciding-facebooks-content-policy/)

文章认为，脸书（Meta）因其招聘行为，尤其是在信任、安全和内容审核相关职位上，受到美国国家安全机构的严重影响。文章着重指出，大量前中央情报局、联邦调查局、国防部和其他政府机构官员担任关键职位，决定着数十亿用户看到的内容。

作者认为，这种前情报官员，特别是来自中央情报局的涌入，引发了人们对脸书公正性和可能与美国政府利益保持一致的严重担忧。文章暗示，这种安排使华盛顿能够以一定程度的似是而非的否认，对全球信息流施加影响。

文章指出具体个人及其先前在情报部门或政府机构中的职位，强调这些人现在对脸书上的内容政策和信息控制做出决定。文章对可能存在偏见的审查、某些叙事的宣传以及异议声音的压制表示担忧。虽然没有指责这些个人怀有恶意，但作者认为，在关键决策岗位上拥有如此多的前情报官员，这种结构性问题造成了信息偏见或被操纵的内在风险。

文章还将脸书声称打击外国虚假信息行动的努力，与其明显缺乏针对美国政府在其平台上潜在的影响行动形成对比。文章最后暗示，这种影响可能直接影响其他国家的选举，例如在尼加拉瓜执政党选举前删除支持该党的账户。

---

## 31. GitHub在微软已不再独立，此前CEO已辞职

**原文标题**: GitHub is no longer independent at Microsoft after CEO resignation

**原文链接**: [https://www.theverge.com/news/757461/microsoft-github-thomas-dohmke-resignation-coreai-team-transition](https://www.theverge.com/news/757461/microsoft-github-thomas-dohmke-resignation-coreai-team-transition)

继首席执行官托马斯·多姆克辞职后，GitHub正被更紧密地整合到微软的CoreAI团队中，这标志着该公司正逐渐偏离其此前独立的运营模式。担任首席执行官近四年的多姆克将离职成为一名创业公司创始人。微软将不会任命新的首席执行官，GitHub的领导层现在将直接向CoreAI团队汇报。

此举代表着自2018年微软收购GitHub以来，其结构上的重大变化。由前Meta高管杰伊·帕里克领导的CoreAI团队专注于为微软及其客户构建人工智能平台和工具。这种整合表明，GitHub的资源和开发工作将越来越与微软的整体人工智能战略保持一致。

此前，GitHub的汇报结构在2021年发生过变化，当时多姆克向微软开发者部门负责人朱莉娅·柳森汇报，后者在今年早些时候CoreAI团队成立后向帕里克汇报。文章还提到多姆克最近在Decoder节目中讨论了GitHub在软件开发未来中的作用及其人工智能工作，突显了他离职的时机。此举表明，未来GitHub将不再是一个独立的实体，而是作为微软人工智能开发工作的一个组成部分。

---

## 32. 韩国星巴克要求顾客停止携带打印机/台式电脑入内

**原文标题**: Starbucks in Korea asks customers to stop bringing in printers/desktop computers

**原文链接**: [https://fortune.com/2025/08/11/starbucks-south-korea-policy-desktop-computer-printer-ban-cagongjok/](https://fortune.com/2025/08/11/starbucks-south-korea-policy-desktop-computer-printer-ban-cagongjok/)

星巴克韩国严打“咖啡馆办公族”，禁止携带台式电脑和打印机等笨重物品。此举旨在应对疫情、临时合同工增加以及首尔办公空间有限等因素驱动下，远程工作者将星巴克作为廉价办公场所的趋势。

虽然星巴克的目标是维持其“温馨的第三空间”，但该政策反映了对顾客过度逗留和占用座位的日益关注。在咖啡馆工作的趋势与韩国的历史茶馆文化有关，并因远程办公以及韩国公司难以获得经济实惠的办公空间而加剧。许多公司已经意识到他们不需要同样的房地产规模，并继续允许员工远程工作。

然而，并非所有咖啡馆老板都对这种转变感到满意，一些人称这些顾客为“电费小偷”，因为他们长时间逗留却很少消费。专家认为，星巴克的政策表明其希望将咖啡馆体验重新平衡到休闲和放松的状态。星巴克韩国由易买得公司控股，但仍受星巴克监督。韩国星巴克门店数量已超过日本。

---

## 33. 高危WinRAR零日漏洞已被两团伙利用数周

**原文标题**: High-severity WinRAR 0-day exploited for weeks by 2 groups

**原文链接**: [https://arstechnica.com/security/2025/08/high-severity-winrar-0-day-exploited-for-weeks-by-2-groups/](https://arstechnica.com/security/2025/08/high-severity-winrar-0-day-exploited-for-weeks-by-2-groups/)

俄罗斯网络犯罪团伙RomCom和Paper Werewolf（GOFFEE）自7月18日左右开始，积极利用WinRAR文件压缩软件中一个被广泛使用的高危零日漏洞（CVE-2025-8088）长达数周。该漏洞允许攻击者通过附加在网络钓鱼信息中的特制压缩包，将恶意可执行文件植入通常禁止访问的目录，从而对计算机进行后门攻击。

ESET发现了该漏洞的利用行为，并通知了WinRAR开发者，他们在六天后发布了修复程序。该漏洞利用了备用数据流来绕过安全措施。RomCom是一个以经济利益为动机的团伙，以其复杂的攻击而闻名，他们利用该漏洞传播了Mythic Agent、SnipBot、RustyClaw和Melting Claw等恶意软件。Paper Werewolf也利用了CVE-2025-8088以及CVE-2025-6218，安装恶意软件以获取系统访问权限，并在他们的网络钓鱼攻击中冒充全俄罗斯研究所的员工。

虽然这些团伙的发现是独立的，但尚不清楚他们之间是否存在联系。文章强调，WinRAR因其庞大的用户群和缺乏自动更新而成为恶意软件分发的主要目标，需要用户手动安装补丁。强烈建议用户更新到WinRAR 7.13或更高版本，以缓解这些漏洞。

---

## 34. Show HN：我用Python构建了一个离线开源桌面像素画编辑器

**原文标题**: Show HN: I built an offline, open‑source desktop Pixel Art Editor in Python

**原文链接**: [https://github.com/danterolle/tilf](https://github.com/danterolle/tilf)

Tilf 是一款开源、离线桌面像素艺术编辑器，使用 Python 和 PySide6 构建。它的目标是提供一个简单易用的工具，用于创建精灵图、图标和小型 2D 资源，无需账户注册或复杂的设置。主要功能包括基本的绘图工具（铅笔、橡皮擦、填充、取色器、矩形、椭圆）、画布操作（缩放、背景颜色、可选网格）、撤销/重做功能、实时预览以及 PNG、JPEG/JPG 和 BMP 格式的导入/导出选项。

Tilf 可在 Windows、macOS 和 GNU/Linux 上运行，并为每种操作系统提供了下载链接。创建者承认代码仍有改进空间，并欢迎通过 pull request 提交贡献。提供了在不同操作系统上构建应用程序的说明，包括为 Windows 创建可执行文件。

该编辑器为常用操作提供了键盘快捷键，在关闭时自动保存以防止数据丢失，并存在一些已知限制，例如 50 步撤销/重做限制以及处理非常大的图像时可能出现的性能问题。该项目根据 GPL v3.0 许可授权，开发者提供了联系方式以供咨询和贡献。目标是创建一个简单直接且免费使用的像素艺术创作工具。

---

## 35. 所有已知的49年历史的Apple-1电脑

**原文标题**: All known 49-year-old Apple-1 computers

**原文链接**: [https://www.apple1registry.com/en/list.html](https://www.apple1registry.com/en/list.html)

Apple-1 注册表是一个非营利网站，致力于编目和记录所有已知的 Apple-1 电脑，这是苹果公司制造的第一台电脑。据估计，1976 年分两批生产了大约 200 块电路板，该注册表旨在跟踪和验证它们的存在和状况。

该网站提供 Apple-1 电脑的可搜索列表，包括序列号（如有）、批次信息、位置（如果已知）、工作状态、博物馆馆藏情况和现有历史等详细信息。该注册表包含 92 台已验证或几乎已验证的 Apple-1 电脑的信息，以及关于可能存在或可能已不存在的电脑的信息。

该网站还提供有关 Apple-1 外围设备、软件和相关文档的信息。它强调了 Apple-1 的稀有性，并预计随着越来越多的电脑被博物馆和公司收购，它们在市场上的供应量将会减少。该注册表还承认存在高质量的复制品，并警告潜在买家注意这些复制品。该注册表欢迎提供信息和照片，并提供联系方式。它提供了关于 Apple-1 的各种统计数据，包括工作单元的数量和带有原始 Byte Shop 外壳的单元的数量。该网站还尊重希望其信息保密的拥有者的意愿。

---

## 36. OpenSSH 后量子密码学

**原文标题**: OpenSSH Post-Quantum Cryptography

**原文链接**: [https://www.openssh.com/pq.html](https://www.openssh.com/pq.html)

这篇OpenSSH文章讨论了后量子密码学（PQC）的实现，以防御“现在存储，将来解密”攻击。在这种攻击中，加密的SSH会话被存储起来，并在量子计算机能够破解当前加密标准时被解密。

OpenSSH自9.0版本起默认支持PQC密钥协商算法，最初是`sntrup761x25519-sha512`，后来添加了`mlkem768x25519-sha256`，该算法在10.0版本中成为默认算法。 OpenSSH 10.1及更高版本会在使用非后量子密钥协商方案时警告用户，可以使用ssh配置中的`WarnWeakCrypto`选项禁用此警告。

文章解释了量子计算机对当前密码学算法构成的威胁，特别是SSH中使用的密钥协商和数字签名。虽然目前还没有强大到足以破解密码学的量子计算机，但“现在存储，将来解密”攻击的风险使得主动实施PQC成为必要。

对于收到警告的用户，建议的解决方案是将SSH服务器更新到支持`mlkem768x25519-sha256`或`sntrup761x25519-sha512`的版本。即使PQC算法的安全性低于预期，OpenSSH也会将它们与经典算法结合起来作为“混合算法”实现，以至少保持现有方法的安全级别。 文章还提到，OpenSSH将来会增加对后量子签名算法的支持。

---

## 37. C/C++中的未定义行为 (2024)

**原文标题**: Undefined Behavior in C and C++ (2024)

**原文链接**: [https://russellw.github.io/undefined-behavior](https://russellw.github.io/undefined-behavior)

本文深入探讨了C和C++中未定义行为（UB）的概念，解释了它是什么、为什么存在以及如何避免它。 UB不仅仅是一个警告；它意味着编译器可以假定特定条件永远不会发生，并据此进行优化，如果违反该假设，可能会导致不可预测的、怪异的程序行为。

文章概述了UB的几个常见来源，包括解引用坏指针（空指针、越界访问、双重释放）、使用未初始化的数据、有符号整数溢出、越界位移和别名违规（指针的错误类型转换）。 C标准中提供了可能的UB的完整列表，尽管其中许多是小众情况。

UB背后的基本原理不仅仅是为了适应不同的硬件限制。 虽然历史硬件约束发挥了一定的作用，但主要驱动力是优化。 允许UB使编译器能够自由地做出积极的假设，尤其是在指针使用和整数算术方面，从而通过诸如寄存器分配之类的技术实现显着的性能提升。

作者承认UB可能引起的沮丧，但认为这是在C/C++这样的语言中获得性能优势的必要权衡。 为了减轻风险，文章建议使用编译器警告、边界检查工具、消毒器、静态分析器、安全标志，甚至完全关闭优化（尽管会付出巨大的性能代价）。 最后，作者开玩笑地建议使用不同的语言作为最终解决方案。 一些UB也被列出，例如省略换行符，它们对任何优化都没有贡献。

---

## 38. 口渴意味着什么？

**原文标题**: What does it mean to be thirsty?

**原文链接**: [https://www.quantamagazine.org/what-does-it-mean-to-be-thirsty-20250811/](https://www.quantamagazine.org/what-does-it-mean-to-be-thirsty-20250811/)

丹·萨莫罗德尼茨基的文章《口渴意味着什么？》探讨了口渴的神经生物学，解释了我们的身体如何向大脑发出需要水的信号。

文章解释说，大脑，特别是下丘脑和脑干等区域，通过脑室周围器官（OVLT和SFO）中的传感器监测身体的水分含量。这些器官就像科学家一样检测血液，以确定身体的盐/水比例，从而推断出水的需求。当盐浓度高时，这些区域会触发口渴的感觉。

关键在于，大脑必须预测水分的吸收，这需要30-60分钟。因此，大脑会根据来自口腔、喉咙和肠道的信号做出“有根据的猜测”，估计水的体积。这些信号会迅速抑制口渴信号。

文章还提到了钠（盐）的稳态，这对于细胞功能至关重要。虽然我们的身体渴望钠，但它主要通过味觉和多巴胺驱动的奖励通路来调节，这与口渴的强烈、内在的驱动力不同。

最后，文章强调了不同物种体验口渴的方式不同。文章以十三条纹地松鼠为例，展示了冬眠如何抑制口渴信号，即使身体需要水也是如此。最终，每种动物管理水和盐的方式都专门针对其生态系统和进化压力，展示了口渴在动物王国中呈现出的多样化方式。文章总结说，“口渴意味着什么？”这个问题的答案因生物而异。

---

## 39. Radicle 1.3.0:

Radicle 1.3.0

**原文标题**: Radicle 1.3.0

**原文链接**: [https://radicle.xyz/2025/08/12/radicle-1.3.0](https://radicle.xyz/2025/08/12/radicle-1.3.0)

Radicle 1.3.0 发布，为点对点代码协作栈带来多项关键改进。 主要功能是通过身份载荷引入规范引用规则（`crefs`），从而实现对标签等引用的更安全、更受控的更新。 这些规则指定了哪些去中心化标识符（DID）有权更新特定引用，并设置了所需的批准阈值。

此次发布还引入了 `radicle-protocol` crate，提供 Radicle 协议的无 I/O 实现，从而提高了模块化程度，并为更广泛的平台支持铺平了道路。 在 Windows 兼容性方面取得了重大进展； rad CLI 现在可以在没有 WSL 的 Windows 上运行，但 `git-remote-rad` 和 `radicle-node` 仍需进一步完善。

日志轮换已通过编号系统得到改进，确保了运行之间的日志持久性。 节点 ID 和地址现在以更清晰的格式呈现，方便复制粘贴。 固定的存储库保持其插入顺序。 git-remote-rad 工具更加灵活，允许从带有任何 Git 修订版本的裸存储库进行推送。 失败的连接尝试现在会报告错误而不是超时，从而改进了调试。 最后，`rad init` 现在建议使用当前分支或 `init.defaultBranch` 作为默认分支。

---

## 40. 混合CPU上的FreeBSD调度

**原文标题**: FreeBSD Scheduling on Hybrid CPUs

**原文链接**: [https://wiki.freebsd.org/Scheduler/Hybrid](https://wiki.freebsd.org/Scheduler/Hybrid)

文章描述了网站使用 Anubis 系统来防御 AI 机器人大规模抓取内容的情况。主要担忧是这种抓取可能导致网站过载和崩溃，阻止合法用户访问资源。

Anubis 通过实施类似 Hashcash 用于打击垃圾邮件的工作量证明机制来工作。这要求访问者执行少量计算工作，对于单个用户来说可以忽略不计，但对于大规模机器人来说成本过高。

该系统被视为一种临时解决方案，与此同时网站开发人员正在开发更强大、长期的防御措施，例如识别无头浏览器指纹（例如，字体渲染分析）。这种高级识别技术将允许阻止机器人，而不会给合法用户带来不便。

该消息还强调 Anubis 依赖于现代 JavaScript 功能，并且像 JShelter 这样的浏览器扩展程序可能会干扰其运行。建议遇到问题的用户禁用特定域的此类扩展程序。

最后，文本承认需要 JavaScript 进行验证带来的不便，并将这种必要性归因于 AI 公司所造成的不断变化的环境。并指出正在开发无需 JavaScript 的替代解决方案。

---

## 41. 度过软件寒冬 (2022)

**原文标题**: Weathering Software Winter (2022)

**原文链接**: [https://100r.co/site/weathering_software_winter.html](https://100r.co/site/weathering_software_winter.html)

Devine的《熬过软件寒冬》讲述了一次在太平洋上航行期间，对现代科技感到幻灭的旅程。由于依赖互联网连接、订阅服务和DRM，设备频繁出现故障的经历，促使人们重新评估软件和硬件的依赖性。

该演讲批评了当代软件的计划报废和缺乏离线功能，突出了依赖此类系统的技能的脆弱性。 这种经历促使Hundred Rabbits探索技术替代方案，重点关注弹性、硬件再利用和数据保存。

他们尝试使用虚拟机（VM）来确保对软件和游戏的长期访问，灵感来自BBC末日审判项目的失败。 他们将重点转移到为任天堂DS等较旧硬件开发软件，找到了一个竞争较小的利基市场。

这篇文章提倡一种个人计算的理念，倾向于可定制和可维修的设备，而不是大规模生产的、不可访问的设备。 他们质疑强加于个人的普遍技术使用，并倡导好玩、量身定制的软件，这些软件能够赋能用户而不是控制他们。

最后，文章提到了2025年早些时候发生的一件事，当时作者在一次会议上发言，但后来该会议为演讲者“过于多元化”道歉，随后对作者本人变得充满敌意。 这件事突显了作者希望与该会议保持距离的愿望，并从他们的各个频道中删除了演讲视频。

---

## 42. Neki – Vitess 团队出品的 Sharded Postgres

**原文标题**: Neki – Sharded Postgres by the team behind Vitess

**原文链接**: [https://planetscale.com/blog/announcing-neki](https://planetscale.com/blog/announcing-neki)

本文宣布了 Neki，一个由 PlanetScale 的 Vitess (MySQL 的分片解决方案) 团队开发的新型分片 Postgres 解决方案。Neki 旨在将 Vitess 的强大功能和可扩展性带给 Postgres 数据库。与 Vitess 不同，Neki 是从头开始构建的，利用了 Postgres 的优势，而不是规避其弱点。该团队强调了他们在超大规模运行 Vitess 方面的丰富经验，以及使分片能够被众多用户访问的经验，暗示 Neki 将为 Postgres 提供类似的访问性和性能水平。Neki 正在与大规模的设计合作伙伴合作开发。该项目准备就绪后将作为开源解决方案发布。作者鼓励有兴趣的人士在 neki.dev 上注册，以获取项目进展的最新信息。本质上，Neki 被定位为 Postgres 的 Vitess 等价物，承诺提供可扩展且易于访问的分片解决方案。

---

## 43. Perplexity 大胆出价 345 亿美元竞购谷歌 Chrome 浏览器

**原文标题**: Perplexity makes bold $34.5B bid for Google's Chrome browser

**原文链接**: [https://www.reuters.com/business/media-telecom/ai-startup-perplexity-makes-bold-345-billion-bid-googles-chrome-browser-2025-08-12/](https://www.reuters.com/business/media-telecom/ai-startup-perplexity-makes-bold-345-billion-bid-googles-chrome-browser-2025-08-12/)

无法访问文章链接。

---

## 44. 盖德隆城堡

**原文标题**: Guédelon Castle

**原文链接**: [https://en.wikipedia.org/wiki/Gu%C3%A9delon_Castle](https://en.wikipedia.org/wiki/Gu%C3%A9delon_Castle)

盖德隆城堡是位于法国特雷尼的一个独特的实验考古项目，专注于仅使用当时的工艺、材料和服饰来重建一座13世纪的城堡。该项目由圣法尔若城堡的主人米歇尔·居约于1997年发起，旨在通过完全使用当地取材的石材和木材从零开始建造一座城堡来了解中世纪的建造方法。城堡的设计遵循法国国王腓力二世的建筑模型，由建筑师雅克·穆兰解读。

选址的原因是其靠近采石场、森林和池塘，能够提供必要的原材料。该项目获得了包括欧盟和法国政府在内的各种来源的资金。随着城堡的建成，它已成为一个热门的旅游目的地，每年吸引数十万游客。

盖德隆城堡还通过提供中世纪建筑技术的专业知识，为巴黎圣母院的重建做出了贡献。该项目曾在纪录片和媒体中出现，突显了其作为大型考古实验的重要性。

---

## 45. Windows XP 的历史

**原文标题**: The History of Windows XP

**原文链接**: [https://www.abortretry.fail/p/the-history-of-windows-xp](https://www.abortretry.fail/p/the-history-of-windows-xp)

本文详细介绍了Windows XP的历史，从微软希望取代MS-DOS的初衷，到最终的发布和成功。最初，微软与IBM合作开发OS/2，但由于分歧而分道扬镳，这促使他们在David Neil Cutler Sr.的帮助下开发了Windows NT。NT旨在统一微软的消费者和商业操作系统。

最初以消费者为中心的NT项目“海王星”及其企业级对应项目“奥德赛”最终因功能过载而被取消。它们被合并为“惠斯勒”，最终成为了Windows XP。微软聘请frog design公司来创建视觉元素，包括标志性的Luna主题。

XP开发过程中的关键进展包括取消对OS/2的支持，放弃对旧处理器的支持，以及整合Windows Me和Windows 2000的元素。 Beta测试导致了重大的设计变更，并引入了诸如系统还原之类的功能。

XP的发布伴随着大规模的营销活动，由于9/11袭击事件而进行了品牌重塑。著名的“Bliss”背景照片以高价购得。 Windows XP引入了Windows产品激活（WPA）、新的网络功能以及对旧软件的兼容模式。随后的服务包（SP1、SP2、SP3）增加了诸如USB 2.0支持、Wi-Fi安全增强和.NET框架支持之类的功能。 Windows XP在发布后不久就取得了显著的销售额。

---

## 46. 机构记忆的价值

**原文标题**: The value of institutional memory

**原文链接**: [https://timharford.com/2025/05/the-value-of-institutional-memory/](https://timharford.com/2025/05/the-value-of-institutional-memory/)

蒂姆·哈福德的文章强调了机构记忆的关键价值以及其丧失带来的有害后果。他以切斯特菲尔德运河的轶事开篇，运河工人因遗忘了一个塞子而意外排干了运河，突显了保留看似微不足道的信息的重要性。

哈福德阐述了组织机构尽管有其宗旨，但在保存机构记忆方面也会面临困难。他引用了大众汽车反复发生的排放丑闻和美国宇航局的航天飞机灾难为例，表明未能从过去的错误中吸取教训导致了严重的后果。挑战者号和哥伦比亚号事故虽然不同，但都存在一个共同点，即忽视警告，未能保留关键的安全知识。

他进一步解释说，组织机构不仅会忘记重大事件，还会忘记高效执行任务所需的流程和技能。洛克希德三星客机就是一个“因不做而忘记”的例子，产量减少导致专业知识的丧失和成本的增加。

哈福德最后强调，遗忘可能通过多种因素发生，包括员工流动、物理和数字档案的退化，甚至是有意销毁记录。他强调，机构记忆的侵蚀可能会产生重大的社会后果，并以温德拉什丑闻为例。他强调了组织机构遗忘的容易程度，即使它们正在积极努力记住，并认为必须积极地对抗这种趋势。

---

## 47. 英国政府建议删除邮件以节约用水

**原文标题**: UK government advises deleting emails to save water

**原文链接**: [https://www.gov.uk/government/news/national-drought-group-meets-to-address-nationally-significant-water-shortfall](https://www.gov.uk/government/news/national-drought-group-meets-to-address-nationally-significant-water-shortfall)

截至2025年8月11日，英国正面临“国家级”严重缺水，五个地区已正式进入干旱状态，另有六个地区正经历长期干旱。由政府机构、水务公司和其他利益相关者组成的国家干旱小组 (NDG) 正在协调努力以缓解局势。

正在采取的主要行动包括敦促公众和各行各业减少用水量。约克郡水务公司在实施软管禁令后报告称家庭用水需求减少了 10%。水务公司也在努力修复泄漏并降低泄漏率，并对基础设施进行了大量投资。由于缺水，农民面临挑战，影响作物产量和牲畜饲料。

环境署（EA）已升级其运营响应，增加了对取水者的合规性检查，并与水务公司合作处理干旱许可证。 气象局预测将恢复干燥气候，这将进一步加剧局势。

政府正在推动改革并投资建设新的水库和管道，以解决日益严重的水资源短缺问题。 目前，已有多个地区宣布干旱，一些水务公司已实施临时用水禁令。全国大部分地区的河流流量低于正常水平，影响航运和野生动物。

鼓励公众通过简单措施节约用水，例如修复泄漏、缩短淋浴时间，甚至删除旧电子邮件，因为数据中心需要水来冷却其系统。英国卫生安全局也在更新关于干旱对公众健康影响的指南。

---

## 48. 如何教孩子玩扑克：从一张牌开始

**原文标题**: How to teach your kids to play poker: Start with one card

**原文链接**: [https://www.bloomberg.com/news/articles/2025-08-08/how-to-teach-your-kids-poker-with-one-card-at-age-four](https://www.bloomberg.com/news/articles/2025-08-08/how-to-teach-your-kids-poker-with-one-card-at-age-four)

无法访问文章链接。

---

## 49. Perplexity 提出以 345 亿美元收购 Chrome 的大胆提议

**原文标题**: Perplexity Makes Longshot $34.5B Offer for Chrome

**原文链接**: [https://www.wsj.com/tech/perplexity-ai-google-chrome-offer-5ddb7a22](https://www.wsj.com/tech/perplexity-ai-google-chrome-offer-5ddb7a22)

无法访问文章链接。

---

## 50. 尾递归函数为何是循环

**原文标题**: Why tail-recursive functions are loops

**原文链接**: [https://kmicinski.com/functional-programming/2025/08/01/loops/](https://kmicinski.com/functional-programming/2025/08/01/loops/)

本文解释了循环和尾递归函数的等价性，并强调了它们的性能影响。由于栈帧压入操作增加了内存访问并可能从缓存中逐出数据，递归函数通常比循环慢。直接递归需要 O(n) 的栈空间来存储部分结果。

另一方面，循环使用常量空间并更新累加器变量来存储部分结果，避免了栈的使用。尾递归函数是一种特殊的递归类型，其中递归调用是执行的最后一个操作（“在尾位置”）。这使得具有尾调用优化的编译器可以将这些调用转换为 `jmp` 语句，从而使它们与循环一样高效，使用常量栈空间。函数的参数被可变地更新，模仿了循环的行为。

本文阐述了如何通过引入累加器变量并在基本情况下返回它，将直接递归函数转换为尾递归函数。然后，作者提出了两个练习供读者将函数转换为使用尾递归。最后，本文提到可以使用延续传递风格 (CPS) 将任何程序转换为尾调用形式，CPS 用堆分配的表示来代替传统的栈，从而可能避免栈溢出。

---

## 51. 美国在线将停止拨号上网服务

**原文标题**: AOL to discontinue dial-up internet

**原文链接**: [https://www.nytimes.com/2025/08/11/business/aol-dial-up-internet.html](https://www.nytimes.com/2025/08/11/business/aol-dial-up-internet.html)

无法访问文章链接。

---

## 52. 宇宙马蹄引力透镜中心的360亿太阳质量黑洞

**原文标题**: 36B solar mass black hole at centre of the Cosmic Horseshoe gravitational lens

**原文链接**: [https://academic.oup.com/mnras/article/541/4/2853/8213862?login=false](https://academic.oup.com/mnras/article/541/4/2853/8213862?login=false)

好的，我已经访问并阅读了这篇文章：“宇宙马蹄引力透镜中心质量为360亿太阳质量的黑洞”。

摘要如下：

这篇文章详细介绍了位于一个遥远星系中心的超大质量黑洞（SMBH）的发现和描述，该黑洞质量约为360亿太阳质量（36B M⊙），该星系充当引力透镜，被称为宇宙马蹄。研究人员利用詹姆斯·韦伯太空望远镜（JWST）的数据分析了引力透镜图像，并准确地模拟了透镜系统。

主要发现是精确确定了透镜星系中心SMBH的质量。这个巨大的质量使其成为迄今为止探测到的质量最大的SMBH之一。此外，该研究能够精确确定星系的质量分布，揭示了其结构和暗物质含量的细节。

通过仔细模拟宇宙马蹄的引力透镜效应（该效应放大并扭曲了背景星系的图像），该团队能够推断出前景透镜星系的属性，以及至关重要的中心SMBH的属性。JWST的高空间分辨率和灵敏度对于实现这种程度的细节至关重要。

这项研究意义重大，因为它提供了对遥远星系中SMBH的直接质量测量，为高红移星系及其中心SMBH的共同演化提供了宝贵的见解。研究结果有助于持续探索宇宙早期如此巨大的黑洞是如何形成和增长的。该研究强调了引力透镜与JWST的能力相结合的强大功能，可以探测遥远星系及其中心黑洞的特性。

---

## 53. 展示一下：玩宝可梦来解锁你的Wayland会话

**原文标题**: Show HN: Play Pokémon to unlock your Wayland session

**原文链接**: [https://github.com/AdoPi/wlgblock](https://github.com/AdoPi/wlgblock)

这个“Show HN”帖子展示了一个独特的项目：一个 Wayland 屏幕锁，它用可玩的、打过补丁的宝可梦 Gameboy 游戏取代了传统的密码提示。目标是通过解决游戏中的谜题来解锁用户会话，本质上是将登录过程变成了一个迷你密室逃脱。

作者是一位 Linux 爱好者，他受到了 Wayland 的定制可能性以及将乐趣与操作系统的技术方面相结合的想法的启发。该项目使用 `ext-session-lock-v1` 协议（需要像 Sway 这样的兼容合成器）来安全地锁定会话。

该实现涉及使用 EGL 和键盘侦听器构建的自定义底层 Wayland 窗口，绕过了像 SDL 这样的传统 GUI 库。作者修改了 `gbcc` 模拟器，添加了一个 Wayland 窗口后端并将着色器转换为 OpenGLES2。至关重要的是，宝可梦水晶游戏被打上了补丁，加入了谜题逻辑，其中输入正确的“密码”（通过游戏中的特定动作触发，例如找到一个隐藏的无线电然后在游戏中输入特定的密码）将特定的 RAM 地址设置为一个预定义的值。锁定器会监视此地址，并在检测到正确的值后解锁会话。

该项目被认为是实验性的，并带有关于潜在不稳定性的警告。作者提供了一个针对 `pokecrystal` 存储库的特定提交的补丁，以修改游戏以进行密码输入。该代码以 MIT (原始 `gbcc`) 和 GPLv3 (锁定器修改) 双重许可。

---

## 54. 围绕 Claude 使用限制优化睡眠

**原文标题**: Optimizing my sleep around Claude usage limits

**原文链接**: [https://mattwie.se/no-sleep-till-agi](https://mattwie.se/no-sleep-till-agi)

此人已大幅调整睡眠时间以最大化利用Claude Pro订阅，其动机是5小时重置限制。由于编码流程经常被打断，他们采用了受单人水手启发的睡眠模式，即每隔2-3小时短睡一次。这使他们可以使用Claude 1-3小时，耗尽令牌限制，然后小睡到下次重置。据称，该策略已大幅提高他们的编码速度（据报道提高了10倍），使他们能够为隐形模式的B2B SaaS项目快速发布功能。他们承认这种睡眠模式可能对健康产生影响，并意识到Anthropic最终可能会提高订阅费用或进一步限制使用。他们正在为这种可能性做准备，甚至考虑使用闹钟来确保他们不会错过Claude的重置时间，从而进一步优化他们的使用。他们策略的核心在于围绕Claude的使用限制来优化他们的生活。

---

## 55. Perplexity拟以345亿美元收购谷歌Chrome浏览器

**原文标题**: Perplexity offers to buy Google's Chrome browser for $34.5B

**原文链接**: [https://www.cnbc.com/2025/08/12/perplexity-google-chrome-ai.html](https://www.cnbc.com/2025/08/12/perplexity-google-chrome-ai.html)

AI 初创公司 Perplexity AI 出价 345 亿美元，欲收购谷歌 Chrome 浏览器，该收购要约未经主动请求。此前，美国司法部提出，作为谷歌反垄断败诉的补救措施，要求谷歌剥离 Chrome 浏览器，理由是谷歌对 Chrome 的控制在搜索市场造成了不公平的优势。Perplexity 声称风险投资者愿意为这笔交易提供资金。

Chrome 于 2008 年推出，为谷歌提供有价值的用户数据，用于定向广告。美国司法部认为，强制谷歌剥离 Chrome 将为竞争性搜索引擎创造公平的竞争环境。然而，谷歌将司法部的提议称为“激进”和“过于宽泛”。

Perplexity 以其 AI 驱动的搜索引擎和最近推出的 AI 浏览器 Comet 而闻名，一直在积极寻求增长，包括之前与 TikTok 提出的未成功的合并提议。该公司也曾被 Meta 接洽，寻求潜在的收购。这家 AI 初创公司正在竞争激烈的环境中航行，科技巨头和初创公司都在大力投资 AI 基础设施和人才。

---

## 56. 读卖新闻起诉Perplexity侵犯版权

**原文标题**: Japan's largest paper, Yomiuri Shimbun, sues Perplexity for copyright violations

**原文链接**: [https://www.niemanlab.org/2025/08/japans-largest-newspaper-yomiuri-shimbun-sues-perplexity-for-copyright-violations/](https://www.niemanlab.org/2025/08/japans-largest-newspaper-yomiuri-shimbun-sues-perplexity-for-copyright-violations/)

2025年8月7日，日本最大报纸《读卖新闻》在东京地方法院起诉人工智能初创公司Perplexity侵犯版权。这是日本主要新闻出版商首次对人工智能公司发起此类法律挑战。

《读卖新闻》声称，Perplexity在2025年2月至6月期间访问了其网站上的119,467篇文章，未经许可使用抓取的内容来复制受版权保护的文章，以回应用户的查询。该报指控其违反了日本法律规定的“复制权”和“向公众传播权”，寻求近1500万美元的赔偿，并要求停止复制其文章。

虽然日本版权法允许人工智能使用受版权保护的材料进行训练，但禁止大规模复制或发行“不合理地损害版权所有者利益”的行为。

Perplexity发言人表示遗憾，并表示该公司致力于确保出版商从人工智能中受益。

此前，新闻集团旗下的《华尔街日报》和《纽约邮报》也对Perplexity采取了类似的法律行动。OpenAI和Meta也面临着国际出版商提出的版权侵权诉讼。在印度，多家新闻出版物对OpenAI提起了联合诉讼，而法国的作家和出版商则以“寄生”为由起诉Meta。

日本新闻协会此前曾警告人工智能公司不要抓取受版权保护的材料，认为这可能会损害新闻机构和公众的知情权。

---

## 57. 长期睡眠不足危害婴幼儿发育

**原文标题**: Chronic sleep deprivation harms development of growing babies

**原文链接**: [https://www.uc.edu/news/articles/2025/08/pregnant-roaches-need-sleep.html](https://www.uc.edu/news/articles/2025/08/pregnant-roaches-need-sleep.html)

辛辛那提大学研究揭示睡眠对太平洋甲虫拟态蟑螂幼崽发育的关键作用，与人类妊娠有相似之处。研究人员发现，当怀孕的蟑螂长期睡眠不足时，会对它们的后代发育产生负面影响，延长妊娠期并扰乱乳蛋白的产生，而乳蛋白对滋养幼崽至关重要。

这些原产于夏威夷和亚洲部分地区的蟑螂，在昆虫中独一无二，因为它们会产下活体幼崽，并以类似于哺乳动物通过胎盘的方式，用乳蛋白喂养它们。这项发表在《实验生物学杂志》上的研究强调了充足睡眠对于母亲和发育中的婴儿的重要性。

主要作者Ronja Frigard强调，像甲虫拟态蟑螂这样的动物模型，可以为人类健康提供有价值的见解，尤其是在妊娠和睡眠方面。由Joshua Benoit教授领导的研究团队强调了重视睡眠的重要性，因为长期的睡眠不足可能会对健康产生累积性的不良后果。

该研究涉及辛辛那提大学的学生，为他们提供了宝贵的科研经验。其中一位学生Gabrielle LeFevre强调了Benoit博士实验室中合作和鼓励的环境，并鼓励大家参与原创研究。

---

## 58. Boom如何利用软件加速硬件开发

**原文标题**: How Boom uses software to accelerate hardware development

**原文链接**: [https://bscholl.substack.com/p/move-fast-and-dont-break-safety-critical](https://bscholl.substack.com/p/move-fast-and-dont-break-safety-critical)

无法访问文章链接。

---

## 59. Ollama 和 gguf

**原文标题**: Ollama and gguf

**原文链接**: [https://github.com/ollama/ollama/issues/11714](https://github.com/ollama/ollama/issues/11714)

该文章是提交给GitHub上Ollama项目仓库的错误报告（#11714）。用户VictorWangwz报告称，转换后的gpt-oss 20b的GGUF模型无法在Ollama中运行，尽管原始模型可以工作，并且该GGUF模型在llama.cpp中运行良好。遇到的错误与初始化过程中（gguf_init_from_file_impl）张量'blk.0.ffn_down_exps.weight'的无效GGML类型（39/NONE）有关。该用户认为问题可能源于Ollama中过时的ggml依赖项，并引用了llama.cpp仓库中的相关问题。该错误报告缺少基本的系统信息（操作系统、GPU、CPU和Ollama版本）。该错误被标记为“bug”和“Something isn't working”。该问题收到了15位用户的正面反馈和1位用户的负面反馈。

---

## 60. Byte Buddy是一个用于Java的代码生成和操作库。

**原文标题**: Byte Buddy is a code generation and manipulation library for Java

**原文链接**: [https://bytebuddy.net/](https://bytebuddy.net/)

Byte Buddy 是一个用于 Java 虚拟机 (JVM) 的强大的代码生成和操纵库。它允许开发者在运行时创建 Java 类，而无需传统的编译器。与标准的 Java 运行时代码生成工具不同，Byte Buddy 提供了创建全新类的灵活性，并且不限于像运行时代理这样的简单接口实现。这种能力允许在运行中的 Java 应用程序中实现更高级和动态的代码生成场景。本质上，与用于运行时类创建的标准 Java 库工具相比，它提供了更大的控制和能力。

---

## 61. 定价页面 – 精选定价页面设计展示

**原文标题**: Pricing Pages – A Curated Gallery of Pricing Page Designs

**原文链接**: [https://pricingpages.design/](https://pricingpages.design/)

此精选画廊展示了不同公司的多种定价页面设计，主要侧重于SaaS和基础设施平台。这些设计涵盖了一系列方法，包括分层订阅、按使用量定价、一次性付款和定制企业解决方案。

这些定价页面上常见的要素包括：

*   **分层卡片：** 呈现具有不同功能和限制的不同定价方案。
*   **订阅选项：** 提供按月或按年付款的选项。
*   **按使用量定价：** 根据存储、查询或活跃用户等消费指标收费。
*   **功能勾选：** 清楚地突出显示每个定价层级中包含的功能。
*   **企业定价：** 通常需要直接联系销售部门以获得定制解决方案。
*   **常见问题解答：** 回答有关定价的常见问题和疑虑。
*   **按使用量计算器：** 允许潜在客户根据预计的使用情况估算其成本。
*   **表格：** 比较不同定价层级的功能。
*   **客户评价：** 展示积极的反馈和社群证明。

该画廊展示了Dynamic、Chroma、Mux、Replit、Vimeo、Pleo等公司的真实案例，说明了他们如何构建定价并将其呈现给潜在客户。一些条目显示“未找到任何项目”，表明抓取时网站或列表可能存在问题。

---

## 62. 混合自定义元素、Web 组件和 Markdown 的乐趣

**原文标题**: The Joy of Mixing Custom Elements, Web Components, and Markdown

**原文链接**: [https://deanebarker.net/tech/blog/custom-elements-markdown/](https://deanebarker.net/tech/blog/custom-elements-markdown/)

本文探讨了将Markdown、自定义元素和Web Components结合用于Web开发的优势。作者提倡使用Markdown的简洁性进行文本格式化，并将自定义元素作为“HTML宏”来表示Markdown内容中复杂的UI组件。

Markdown处理器会忽略HTML，从而允许将自定义元素直接嵌入到Markdown文件中。这些使用Web Component标准定义的自定义元素，可以在浏览器中动态地扩展为复杂的HTML结构。这种方法实现了关注点分离，作者可以专注于Markdown中的内容，而开发者可以创建可重用的组件。

作者强调了Markdown的文本格式化和自定义元素创建更复杂结构的能力之间的协同作用。示例包括一个订阅按钮。本文展示了一个场景，其中一个Markdown段落包含一个自定义元素，该元素扩展为一个完整的HTML表单。

作者还涉及了技术方面的考虑，例如需要显式关闭自定义元素标签，以及Markdown中多行属性的挑战。Markdown预处理器可以通过在HTML到达Markdown引擎之前修复HTML来解决这些问题。

最后，作者鼓励自定义元素的语言设计，重点是简化作者所需的信息并最大化代码驱动的功能。它讨论了服务器端与客户端处理的优缺点。

---

## 63. Syncthing 2.0 发布

**原文标题**: Syncthing 2.0 Released

**原文链接**: [https://github.com/syncthing/syncthing/releases/tag/v2.0.0](https://github.com/syncthing/syncthing/releases/tag/v2.0.0)

Syncthing 2.0 发布，这是一次重大更新，包含一些不兼容的变更，并侧重于提高可维护性和效率。数据库后端已从 LevelDB 切换到 SQLite，首次启动时可能需要长时间迁移。日志记录已彻底改造为结构化格式，具有按包日志级别控制和新的 WARNING 级别。

主要变更包括：删除的项目现在在六个月后被遗忘（可配置）；命令行选项解析已现代化（不再支持旧的单破折号选项）；为提高性能而删除了滚动哈希检测；启动时不再创建默认文件夹。默认情况下，v2 设备之间现在使用多个连接（三个）。不再为几个不太常见的平台提供预构建的二进制文件。

此版本包含大量错误修复、功能添加和性能改进。新增功能包括 `syncthing debug database-statistics` 命令、默认的多个连接、将文件夹和设备信息作为指标公开、用于同步连接的 Ed25519 密钥、通过 GUI 限制 LAN 中的带宽以及 QUIC 的 UDP 端口映射。一些“例行”变更侧重于内部改进和代码清理。

---

## 64. 使用Zig语言通过SIMD加速子字符串搜索

**原文标题**: Faster substring search with SIMD in Zig

**原文链接**: [https://aarol.dev/posts/zig-simd-substr/](https://aarol.dev/posts/zig-simd-substr/)

本文探讨了使用SIMD（单指令多数据）加速Zig中的子字符串搜索，与`std.mem.indexOf`相比，性能提升高达60%。作者实现了Wojciech Muła的SIMD友好算法，该算法使用SIMD寄存器将haystack的32字节块与needle的第一个和最后一个字符进行比较，从而生成指示潜在子字符串出现的位掩码，显著减少了必要的内存访问次数。

文章详细介绍了Zig的实现，利用了AVX2指令以及Zig的`@Vector`和`@splat`函数。针对大型文本（《白鲸记》）的基准测试显示出显著的性能提升，包括减少了CPU周期。作者随后研究了字符选择策略，以最大限度地减少误报和分支未命中，通过选择needle中最稀有的字符来进一步优化SIMD版本。这提高了性能并减少了分支未命中。

最后，文章考虑了使用512位指令的AVX-512，并提出了一个使用`std.simd.suggestVectorLength()`动态适应CPU的SIMD能力的版本。针对较小字符串的微基准测试证实，即使对于小型输入，SIMD算法仍然更快。作者得出结论，SIMD可以显著提高Zig中的子字符串搜索性能，并且具有进一步优化的潜力。

---

## 65. Llama.cpp 中 Mistral 集成得到改进

**原文标题**: Mistral Integration Improved in Llama.cpp

**原文链接**: [https://github.com/ggml-org/llama.cpp/pull/14737](https://github.com/ggml-org/llama.cpp/pull/14737)

本文讨论了llama.cpp项目中旨在改进Mistral AI模型集成的pull request（PR #14737）。现有将Mistral模型转换为GGUF格式（llama.cpp使用）的过程效率低下，需要先转换为Hugging Face格式，可能导致错误，并且缺乏对聊天模板的原生支持。

该PR引入了一个新的脚本`convert_mistral_to_gguf.py`，用于直接从Hugging Face模型转换为GGUF。它在llama.cpp中注册了Mistral架构，允许原生支持，无需中间转换。还提出了通过FastAPI实现的REST API，以使mistral-common tokenizer更易于访问。

该PR建议使用llama-server工具，通过`/completions`路由并设置`return_tokens=True`来利用mistral-common进行分词和逆分词。作者承认了关于多模态数据支持的局限性，因为llama.cpp目前仅通过聊天模板支持此功能。

开发人员的反馈强调了使用参考tokenizer进行准确性的好处，同时也承认了需要单独的分词服务器的缺点。有人建议将滑动窗口注意力（SWA）参数包含在GGUF文件中。

后续讨论建议将新转换脚本的功能合并到现有的`convert_hf_to_gguf.py`脚本中，以提高可维护性和用户清晰度。讨论还涉及支持包含音频组件的Voxtral模型。解决依赖冲突和处理代码格式问题也被讨论为使PR准备好合并的一部分。

---

## 66. Tesla Dojo Went from Essential to Shut Down in 12 Months

**原文标题**: Tesla Dojo Went from Essential to Shut Down in 12 Months

**原文链接**: [https://www.bloomberg.com/news/newsletters/2025-08-12/tesla-dojo-went-from-essential-to-shut-down-in-12-months](https://www.bloomberg.com/news/newsletters/2025-08-12/tesla-dojo-went-from-essential-to-shut-down-in-12-months)

无法访问文章链接。

---

## 67. 133-year old Kodak says it might have to cease operations

**原文标题**: 133-year old Kodak says it might have to cease operations

**原文链接**: [https://www.cnn.com/2025/08/12/business/kodak-survival-warning](https://www.cnn.com/2025/08/12/business/kodak-survival-warning)

生成摘要时出错

---

## 68. The Quiet Disappearance of Skeptics in the AI Gold Rush

**原文标题**: The Quiet Disappearance of Skeptics in the AI Gold Rush

**原文链接**: [https://middlelayer.substack.com/p/where-did-all-the-ai-doomers-go-the](https://middlelayer.substack.com/p/where-did-all-the-ai-doomers-go-the)

生成摘要时出错

---

## 69. 大型语言模型的思维链推理是海市蜃楼吗？一种数据分布视角

**原文标题**: Is Chain-of-Thought Reasoning of LLMs a Mirage? A Data Distribution Lens

**原文链接**: [https://arstechnica.com/ai/2025/08/researchers-find-llms-are-bad-at-logical-inference-good-at-fluent-nonsense/](https://arstechnica.com/ai/2025/08/researchers-find-llms-are-bad-at-logical-inference-good-at-fluent-nonsense/)

生成摘要时出错

---

## 70. Chris Simpkins, creator of Hack font, has died

**原文标题**: Chris Simpkins, creator of Hack font, has died

**原文链接**: [https://typo.social/@Hilary/114845913381245488](https://typo.social/@Hilary/114845913381245488)

生成摘要时出错

---

## 71. Claude is the drug, Cursor is the dealer

**原文标题**: Claude is the drug, Cursor is the dealer

**原文链接**: [https://middlelayer.substack.com/p/i-claude-is-the-drug-cursor-is-the](https://middlelayer.substack.com/p/i-claude-is-the-drug-cursor-is-the)

生成摘要时出错

---

## 72. The Chrome VRP Panel has decided to award $250k for this report

**原文标题**: The Chrome VRP Panel has decided to award $250k for this report

**原文链接**: [https://issues.chromium.org/issues/412578726](https://issues.chromium.org/issues/412578726)

生成摘要时出错

---

## 73. Going faster than memcpy

**原文标题**: Going faster than memcpy

**原文链接**: [https://squadrick.dev/journal/going-faster-than-memcpy](https://squadrick.dev/journal/going-faster-than-memcpy)

生成摘要时出错

---

## 74. The demographic future of humanity: facts and consequences [pdf]

**原文标题**: The demographic future of humanity: facts and consequences [pdf]

**原文链接**: [https://www.sas.upenn.edu/~jesusfv/Slides_London.pdf](https://www.sas.upenn.edu/~jesusfv/Slides_London.pdf)

生成摘要时出错

---

## 75. Outside of the top stocks, S&P 500 forward profits haven't grown in 3 years

**原文标题**: Outside of the top stocks, S&P 500 forward profits haven't grown in 3 years

**原文链接**: [https://insight-public.sgmarkets.com/quant-motion-pictures/outside-of-the-top-10-stocks-sp500-forward-profits-haven-t-grown-in-three-years](https://insight-public.sgmarkets.com/quant-motion-pictures/outside-of-the-top-10-stocks-sp500-forward-profits-haven-t-grown-in-three-years)

生成摘要时出错

---

## 76. White Mountain Direttissima

**原文标题**: White Mountain Direttissima

**原文链接**: [https://whitemountainski.co/pages/white-mountain-direttissima](https://whitemountainski.co/pages/white-mountain-direttissima)

The "White Mountain Direttissima" chronicles the author's attempt to complete a challenging unsupported trail run through the White Mountains of New Hampshire, aiming for a five-day completion. This was his third attempt after a six-day finish in 2016 and a DNF (Did Not Finish) in 2024 due to tendonitis.

The article details the daily mileage, elevation gain, and significant events encountered during the run. Day 1 involved multiple peaks and a painful fall on the tailbone. Day 2 included bushwhacking, sleep deprivation, and the first signs of potential tendon issues. Day 3 marked a turning point, surpassing the previous DNF point. Day 4 highlighted the Willey Range, Presidential Traverse, and an out-and-back to Isolation.

Day 5 was the final push, aiming to finish under five days. It involved climbing out of Carter Notch, traversing the northern Presidentials, and enduring difficult terrain on the Pliny-Pilot Range. The author faced physical challenges like a sore throat, aching body, and foot pain, but continued to "chip" away at the miles. The excerpt ends mid-sentence as the author realizes something on his way to Cabot.


---

## 77. GLM-4.5V: An open-source multimodal large language model from Zhipu AI

**原文标题**: GLM-4.5V: An open-source multimodal large language model from Zhipu AI

**原文链接**: [https://github.com/zai-org/GLM-V](https://github.com/zai-org/GLM-V)

Zhipu AI has released GLM-4.5V, an open-source multimodal large language model built on the GLM-4.5-Air text foundation model, along with updates to the GLM-4.1V series. These models aim to enhance reasoning capabilities beyond basic multimodal perception for complex AI tasks.

GLM-4.5V achieves state-of-the-art performance on 42 vision-language benchmarks and excels in real-world usability by handling diverse visual content like images, videos, documents, and GUI tasks. It introduces a "Thinking Mode" switch for balancing response speed and reasoning depth.

GLM-4.1V-9B-Thinking, built on the GLM-4-9B-0414 model, focuses on reasoning through a Chain-of-Thought mechanism and RLCS (Reinforcement Learning with Curriculum Sampling). It supports 64k context length, any aspect ratio up to 4k image resolution, and is bilingual (Chinese/English). It outperforms larger models like Qwen-2.5-VL-72B on multiple tasks. A base model, GLM-4.1V-9B-Base, is also open-sourced for research.

The release includes model implementation code, download links, examples (GUI agents, desktop assistants), and quick start guides for inference using NVIDIA GPUs (with instructions for Ascend NPUs). Fine-tuning instructions using LLaMA-Factory and dataset construction examples are also provided. While improvements have been made since GLM-4.1V, limitations such as frontend code reproduction issues, pure text Q&A capabilities, and occasional overthinking/repetition remain.


---

## 78. A simple pixel physics simulator in Rust using Macroquad

**原文标题**: A simple pixel physics simulator in Rust using Macroquad

**原文链接**: [https://github.com/gale93/sbixel](https://github.com/gale93/sbixel)

生成摘要时出错

---

## 79. Millau Viaduct

**原文标题**: Millau Viaduct

**原文链接**: [https://www.fosterandpartners.com/projects/millau-viaduct](https://www.fosterandpartners.com/projects/millau-viaduct)

生成摘要时出错

---

## 80. Learn, Reflect, Apply, Prepare: The Four Daily Practices That Changed How I Live

**原文标题**: Learn, Reflect, Apply, Prepare: The Four Daily Practices That Changed How I Live

**原文链接**: [https://opuslabs.substack.com/p/learn-reflect-apply-prepare](https://opuslabs.substack.com/p/learn-reflect-apply-prepare)

生成摘要时出错

---

## 81. A Global Look at Teletext

**原文标题**: A Global Look at Teletext

**原文链接**: [https://text-mode.org/?p=23643](https://text-mode.org/?p=23643)

生成摘要时出错

---

## 82. Designing Software in the Large

**原文标题**: Designing Software in the Large

**原文链接**: [https://dafoster.net/articles/2025/07/22/designing-software-in-the-large/](https://dafoster.net/articles/2025/07/22/designing-software-in-the-large/)

生成摘要时出错

---

## 83. Token growth indicates future AI spend per dev

**原文标题**: Token growth indicates future AI spend per dev

**原文链接**: [https://blog.kilocode.ai/p/future-ai-spend-100k-per-dev](https://blog.kilocode.ai/p/future-ai-spend-100k-per-dev)

生成摘要时出错

---

## 84. Try and

**原文标题**: Try and

**原文链接**: [https://ygdp.yale.edu/phenomena/try-and](https://ygdp.yale.edu/phenomena/try-and)

生成摘要时出错

---

## 85. Vanishing from Hyundai’s data network

**原文标题**: Vanishing from Hyundai’s data network

**原文链接**: [http://techno-fandom.org/~hobbit/cars/ev/offnet.html](http://techno-fandom.org/~hobbit/cars/ev/offnet.html)

生成摘要时出错

---

## 86. Generic Containers in C: Safe Division Using Maybe

**原文标题**: Generic Containers in C: Safe Division Using Maybe

**原文链接**: [https://uecker.codeberg.page/2025-08-10.html](https://uecker.codeberg.page/2025-08-10.html)

生成摘要时出错

---

## 87. Manpower discloses data breach affecting nearly 145,000 people

**原文标题**: Manpower discloses data breach affecting nearly 145,000 people

**原文链接**: [https://www.bleepingcomputer.com/news/security/manpower-staffing-agency-discloses-data-breach-after-attack-claimed-by-ransomhub/](https://www.bleepingcomputer.com/news/security/manpower-staffing-agency-discloses-data-breach-after-attack-claimed-by-ransomhub/)

生成摘要时出错

---

## 88. Trump Orders National Guard to Washington and Takeover of Capital’s Police

**原文标题**: Trump Orders National Guard to Washington and Takeover of Capital’s Police

**原文链接**: [https://www.nytimes.com/live/2025/08/11/us/trump-news](https://www.nytimes.com/live/2025/08/11/us/trump-news)

生成摘要时出错

---

## 89. Easily run Windows software on Linux with Bottles

**原文标题**: Easily run Windows software on Linux with Bottles

**原文链接**: [https://usebottles.com/](https://usebottles.com/)

生成摘要时出错

---

## 90. Lists and Lists: Basics of Lisp through interactive fiction (1996)

**原文标题**: Lists and Lists: Basics of Lisp through interactive fiction (1996)

**原文链接**: [https://eblong.com/zarf/zweb/lists/](https://eblong.com/zarf/zweb/lists/)

生成摘要时出错

---

## 91. Show HN: ServerBuddy – GUI SSH client for managing Linux servers from macOS

**原文标题**: Show HN: ServerBuddy – GUI SSH client for managing Linux servers from macOS

**原文链接**: [https://serverbuddy.app](https://serverbuddy.app)

生成摘要时出错

---

## 92. Anti-competitive practices masquerading as security is a dangerous pattern

**原文标题**: Anti-competitive practices masquerading as security is a dangerous pattern

**原文链接**: [https://blog.alinelerner.com/i-posted-some-interview-prep-materials-on-linkedin-then-they-deleted-me/](https://blog.alinelerner.com/i-posted-some-interview-prep-materials-on-linkedin-then-they-deleted-me/)

生成摘要时出错

---

## 93. Show HN: Keeps – Mail a postcard that plays your voice

**原文标题**: Show HN: Keeps – Mail a postcard that plays your voice

**原文链接**: [https://www.sendkeeps.com/](https://www.sendkeeps.com/)

生成摘要时出错

---

## 94. Sloppy AI defenses take cybersecurity back to the 1990s, researchers say

**原文标题**: Sloppy AI defenses take cybersecurity back to the 1990s, researchers say

**原文链接**: [https://www.scworld.com/news/sloppy-ai-defenses-take-cybersecurity-back-to-the-1990s-researchers-say](https://www.scworld.com/news/sloppy-ai-defenses-take-cybersecurity-back-to-the-1990s-researchers-say)

生成摘要时出错

---

## 95. AP to end its weekly book reviews

**原文标题**: AP to end its weekly book reviews

**原文链接**: [https://dankennedy.net/2025/08/08/the-associated-press-tells-its-book-critics-that-its-ending-weekly-reviews/](https://dankennedy.net/2025/08/08/the-associated-press-tells-its-book-critics-that-its-ending-weekly-reviews/)

生成摘要时出错

---

## 96. I want everything local – Building my offline AI workspace

**原文标题**: I want everything local – Building my offline AI workspace

**原文链接**: [https://instavm.io/blog/building-my-offline-ai-workspace](https://instavm.io/blog/building-my-offline-ai-workspace)

生成摘要时出错

---

## 97. GPT-OSS-120B runs on just 8GB VRAM & 64GB+ system RAM

**原文标题**: GPT-OSS-120B runs on just 8GB VRAM & 64GB+ system RAM

**原文链接**: [https://old.reddit.com/r/LocalLLaMA/comments/1mke7ef/120b_runs_awesome_on_just_8gb_vram/](https://old.reddit.com/r/LocalLLaMA/comments/1mke7ef/120b_runs_awesome_on_just_8gb_vram/)

生成摘要时出错

---

## 98. GPT-OSS vs. Qwen3 and a detailed look how things evolved since GPT-2

**原文标题**: GPT-OSS vs. Qwen3 and a detailed look how things evolved since GPT-2

**原文链接**: [https://magazine.sebastianraschka.com/p/from-gpt-2-to-gpt-oss-analyzing-the](https://magazine.sebastianraschka.com/p/from-gpt-2-to-gpt-oss-analyzing-the)

生成摘要时出错

---

## 99. Raised by Wolves Is Original Sci-Fi at Its Most Polarizing (2020)

**原文标题**: Raised by Wolves Is Original Sci-Fi at Its Most Polarizing (2020)

**原文链接**: [https://www.rogerebert.com/streaming/hbo-maxs-raised-by-wolves-is-original-sci-fi-at-its-most-polarizing](https://www.rogerebert.com/streaming/hbo-maxs-raised-by-wolves-is-original-sci-fi-at-its-most-polarizing)

生成摘要时出错

---

## 100. PHP compile time generics: yay or nay?

**原文标题**: PHP compile time generics: yay or nay?

**原文链接**: [https://thephp.foundation/blog/2025/08/05/compile-generics/](https://thephp.foundation/blog/2025/08/05/compile-generics/)

生成摘要时出错

---

