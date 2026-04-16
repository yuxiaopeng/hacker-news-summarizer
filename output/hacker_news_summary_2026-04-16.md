# Hacker News 热门文章摘要 (2026-04-16)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Claude Opus 4.7

**原文标题**: Claude Opus 4.7

**原文链接**: [https://www.anthropic.com/news/claude-opus-4-7](https://www.anthropic.com/news/claude-opus-4-7)

Anthropic 宣布正式推出 **Claude Opus 4.7**（截至 2026 年 4 月 16 日）。这是针对 Opus 4.6 的重大更新，专为高级软件工程和复杂的自主工作流而设计。

**核心功能与改进：**
*   **工程与自主性：** Opus 4.7 擅长处理长程任务，代码解决率比前代提升了 13%。它具有更强的“抗循环性”、更好的错误恢复能力，并能自主验证其输出结果。
*   **指令遵循与记忆：** 该模型对提示词的遵循更加精准，并能更高效地利用基于文件系统的记忆来维持跨会话的上下文。
*   **多模态视觉：** 支持高分辨率图像（最高 375 万像素），能够从复杂的图表和密集的截图中精确提取数据。
*   **领域成果：** 早期测试者报告称，该模型在法律分析（BigLaw Bench 准确率 90.9%）、金融（在 GDPval-AA 上达到顶尖水平）和文档推理（错误减少 21%）方面取得了重大进展。

**安全与网络安全：**
继“海角蝶项目”（Project Glasswing）之后，Anthropic 刻意限制了 Opus 4.7 相较于其旗舰模型 **Claude Mythos Preview** 的网络能力。虽然它包含拦截违规用途的自动化防护措施，但针对经过审核的安全专业人员，官方已启动了一项全新的**网络验证计划**。总体而言，该模型对抗提示词注入的能力有所增强，但在对齐表现上仍略逊于 Mythos 模型。

**可用性与定价：**
定价与 Opus 4.6 保持一致：**每百万输入 Token 5 美元**，**每百万输出 Token 25 美元**。用户现可通过 Claude API、Amazon Bedrock、Google Cloud Vertex AI 以及 Microsoft Foundry 立即获取。

总体而言，Opus 4.7 被定位为一种高度可靠的“智能体”模型，旨在减少在复杂、多步骤专业任务中对人工监管的需求。

---

## 2. 万物宝典

**原文标题**: Codex for Almost Everything

**原文链接**: [https://openai.com/index/codex-for-almost-everything/](https://openai.com/index/codex-for-almost-everything/)

OpenAI 的“万能 Codex”发布了 OpenAI Codex，这是一款旨在弥合自然语言与计算机代码之间鸿沟的 AI 模型。作为 GPT-3 的衍生模型，Codex 专门针对来自 GitHub 的海量公开代码进行了微调，能够理解自然英语并从中生成编程指令。

此次发布的核心要点包括：

*   **多功能性：** 尽管在 Python 方面表现极其卓越，但 Codex 还支持广泛的语言，包括 JavaScript、Go、Perl、PHP、Ruby、Swift 和 TypeScript。
*   **广泛的应用场景：** 该模型的能力远不止简单的代码补全。在演示中，Codex 构建了简单的游戏，在不同软件（如 Excel）之间处理数据，并通过自然语言指令与各种第三方 API（如 Spotify 和 Mailchimp）进行交互。它本质上充当了一个界面，允许用户使用对话式语言来控制计算机。
*   **生产力与易用性：** 该工具旨在通过自动化重复性任务显著提高开发者的生产力。此外，它还致力于降低非程序员的准入门槛，使他们无需深厚的专业技术知识即可创建软件并实现工作流自动化。
*   **API 开放情况：** OpenAI 已通过其 API 平台的私人测试版推出了 Codex，邀请开发者和企业探索其功能并构建新应用。

总的来说，Codex 代表了向**“意图导向型计算”**的转变，重点从“如何”编程的技术细节转向“创造什么”的创意愿景。通过将人类意图转化为机器可执行的代码，Codex 为专业软件工程师和普通用户都提供了强大的助力。

---

## 3. Qwen3.6-35B-A3B：Agent 级编程能力，现已全面开放

**原文标题**: Qwen3.6-35B-A3B: Agentic coding power, now open to all

**原文链接**: [https://qwen.ai/blog?id=qwen3.6-35b-a3b](https://qwen.ai/blog?id=qwen3.6-35b-a3b)

根据提供的标题，以下是关于 **Qwen3.6-35B-A3B** 公告的简要总结：

**概览**
阿里巴巴 Qwen 团队宣布发布 **Qwen3.6-35B-A3B**，这是一款专为**智能体编码（agentic coding）**设计的全新开源权重模型。此次发布标志着高性能、自主编程工具向全球开发者社区普及的重大里程碑。

**核心特性与架构**
*   **MoE 带来的高效性**：“A3B”标识表明该模型采用了混合专家（MoE）架构。虽然模型总参数量为 350 亿，但在推理时仅使用约 **30 亿激活参数**。这使其能够以较小模型的速度和较低的硬件需求，提供大型模型的推理能力。
*   **智能体能力**：与标准的代码补全模型不同，Qwen3.6 针对“智能体”工作流进行了优化。这意味着它被设计为一个自主智能体——能够规划多步任务、使用外部工具（如编译器和调试器），并对复杂的软件架构进行推理。
*   **开放访问**：通过以开源权重许可发布该模型，Qwen 使开发者能够在本地硬件或私有云上运行高级编程助手，从而确保数据隐私并减少对专有 API 的依赖。

**重要意义**
Qwen3.6-35B-A3B 旨在缩小软件工程领域开源模型与领先专有系统（如 GPT-4o 或 Claude 3.5 Sonnet）之间的性能差距。它为构建能够处理端到端开发任务（而非简单的代码片段）的自主“AI 软件工程师”提供了坚实基础。

---

## 4. Cloudflare AI 平台：专为智能体设计的推理层

**原文标题**: Cloudflare's AI Platform: an inference layer designed for agents

**原文链接**: [https://blog.cloudflare.com/ai-platform/](https://blog.cloudflare.com/ai-platform/)

Cloudflare 宣布将其 AI 平台演进为**统一推理层**，专门用于满足 AI 智能体（AI agents）的高标准需求。Cloudflare 认识到智能体工作流通常需要串联多个模型，因此其新架构专注于灵活性、速度和可靠性。

**主要特性包括：**

*   **统一 API 与目录：** 通过 `AI.run()` 绑定，开发者只需一行代码即可访问来自 12 个以上供应商（包括 OpenAI、Anthropic、Google 和 Meta）的 70 多个模型。这实现了模型间的无缝切换，以及对 AI 支出和元数据的集中管理。
*   **自带模型 (BYOM)：** 整合了 Replicate（其团队已加入 Cloudflare）的技术，该平台现在允许用户使用 “Cog” 将自定义或微调模型容器化。这些模型可以直接部署在 Cloudflare 的 Workers AI 基础设施上，并利用 GPU 快照等性能优化特性。
*   **低延迟性能：** 利用 Cloudflare 遍布 330 个城市的全球网络，该平台最大限度地缩短了“首字时间”（time to first token）。在与应用程序代码相同的网络上运行推理，消除了不必要的网络跃点，这对于实现智能体的极速响应至关重要。
*   **以智能体为中心的可靠性：** AI 网关现在支持**自动故障转移**；如果某个供应商发生故障，请求将自动重新路由到另一个供应商。此外，缓冲流技术确保如果智能体连接中断，可以重新连接并检索其响应，而无需重新运行推理或产生额外费用。

通过整合 Replicate 的托管能力并提供与供应商无关的界面，Cloudflare 旨在成为开发者构建复杂、多模态且具韧性的 AI 智能体所必需的基础设施。

---

## 5. Launch HN：Kampala (YC W26) – 将应用程序逆向工程为 API

**原文标题**: Launch HN: Kampala (YC W26) – Reverse-Engineer Apps into APIs

**原文链接**: [https://www.zatanna.ai/kampala](https://www.zatanna.ai/kampala)

**Kampala** 是一家由 Zatanna 创立并获得 Y Combinator (W26) 支持的初创公司，其开发了一款旨在将网站、移动应用和桌面应用程序逆向工程为功能性 API 的工具。其主要目标是通过捕获和复制任何软件的底层网络流量，帮助开发者实现复杂工作流的自动化。

该平台提供了几项核心功能，以简化逆向工程流程：
*   **全流量拦截：** 用户可以实时监控来自任何应用程序或浏览器的每一条 HTTP/S 请求。
*   **认证链追踪：** 自动映射复杂的身份验证序列，包括令牌、Cookie 和多步会话。
*   **流程重放与导出：** 用户可以捕获特定的操作序列，并将其导出为稳定且可重复的自动化程序。
*   **指纹保持：** 为防止被检测并确保稳定性，该工具会保留原始的 HTTP/TLS 指纹，使自动化流量看起来与原应用完全一致。

Kampala 目前已可在 **macOS** 上下载，**Windows** 版本正在开发中（现已开放候补名单）。团队还设有 Discord 社区，用于用户支持和反馈。

---

## 6. 万物的未来或许尽是谎言：我们该何去何从？

**原文标题**: The future of everything is lies, I guess: Where do we go from here?

**原文链接**: [https://aphyr.com/posts/420-the-future-of-everything-is-lies-i-guess-where-do-we-go-from-here](https://aphyr.com/posts/420-the-future-of-everything-is-lies-i-guess-where-do-we-go-from-here)

在《我想，未来的万物皆为谎言》一文中，作者对大语言模型（LLM）提出了发人深省的批判，将其社会影响比作私家车所带来的变革性且往往具有破坏性的遗产。正如汽车重塑了城市和社会结构（且通常伴随着灾难性的副作用）一样，作者认为人工智能正在侵蚀真理、劳动和人类技能的根基。

文章重点阐述了日益泛滥的“垃圾内容”（slop）：充斥着虚假信息的搜索结果、数据中心带来的环境压力，以及合成内容的激增。作者表达了深切的担忧，认为人工智能正在贬低“实践智慧”（metis）——即通过亲身实践获得的经验智慧和深度理论构建能力。通过将写作、编程和思考外包给机器，人类面临着失去批判性推理“肌肉记忆”的风险。

为了应对这一局面，作者倡导一种**拒绝哲学**，敦促读者：
*   在个人生活和职业生涯中**拒绝使用大语言模型工具**，以维护人类的主体性。
*   **组织与监管**，倡导成立工会，并要求政府对碳排放和数据中心扩张进行严厉监管。
*   **放缓技术发展步伐**，认为推迟人工智能的进步能为社会赢得关键时间，以便适应环境、保护劳动者，并建立针对欺诈和合成媒体的防御机制。

尽管承认大语言模型在特定任务中具有诱人的实用性，但作者得出结论，其对人类文化和生计构成的长期风险远超短期便利。本文既是一次警告，也是一份行动号召，强调面对这个“荒唐的未来”，最符合伦理的回应就是坚持由人类主导工作。为了强调这一点，作者指出本文本身完全由人工撰写和编辑。

---

## 7. Show HN: CodeBurn – 按任务分析 Claude Code 的 Token 使用情况

**原文标题**: Show HN: CodeBurn – Analyze Claude Code token usage by task

**原文链接**: [https://github.com/AgentSeal/codeburn](https://github.com/AgentSeal/codeburn)

**CodeBurn** 是一款开源命令行（CLI）工具，旨在帮助开发者跟踪并分析多个 AI 编程助手的 Token 使用情况和成本。它目前支持 Claude Code、Cursor、Codex、OpenCode、Pi 和 GitHub Copilot。与需要 API 代理或包装器的工具不同，CodeBurn 通过直接从用户本地磁盘读取会话记录和 SQLite 数据库来运行，在无需额外 API 密钥的情况下，确保了隐私性并简化了设置流程。

该工具的核心功能是一个交互式 TUI（终端用户界面）仪表板，它将 AI 活动细分为 13 种确定性的任务类型，如编码、调试、重构和测试。其提供的一项关键指标是**“一次性成功率”**（one-shot success rate），用于衡量 AI 在首次尝试时完成任务的频率，而非通过重复的“编辑-测试-修复”循环消耗 Token。

**主要特性包括：**
*   **详细明细：** 按模型（如 Sonnet、GPT-4o）、项目、MCP 服务器和特定 Shell 命令分析使用情况。
*   **准确的成本计算：** 利用 LiteLLM 计价数据计算费用，支持 162 种货币及缓存汇率。
*   **报告功能：** 提供日、周、月视图，并支持将数据导出为 CSV 或 JSON 格式。
*   **集成：** 包含通过 SwiftBar 实现的 macOS 菜单栏组件，用于实时监控成本。
*   **优化洞察：** 帮助用户识别“Token 损耗”，例如低缓存命中率、过度文件读取，或在简单任务中使用性能过剩的模型。

CodeBurn 基于 Node.js 和 Ink 库构建，可以通过 npm 安装或使用 `npx codeburn` 直接运行。对于希望优化 AI 工作流并管理自主编程代理日益增长成本的开发者来说，它是一款极佳的诊断工具。

---

## 8. Show HN: MacMind – A transformer neural network in HyperCard on a 1989 Macintosh

**原文标题**: Show HN: MacMind – A transformer neural network in HyperCard on a 1989 Macintosh

**原文链接**: [https://github.com/SeanFDZ/macmind](https://github.com/SeanFDZ/macmind)

**MacMind** is a functional 1,216-parameter transformer neural network implemented entirely in HyperTalk, the scripting language for HyperCard. Developed by Sean Lavigne, the project demonstrates that the fundamental mechanics of modern AI—including self-attention and backpropagation—are transparent mathematical processes rather than "magic," capable of running on a 1989 Macintosh SE/30.

The model is a single-layer, single-head transformer designed to learn the bit-reversal permutation, a critical initial step in the Fast Fourier Transform (FFT). Despite its vintage platform, MacMind incorporates the same core architecture found in massive models like GPT-4, featuring token and positional embeddings, scaled dot-product attention, cross-entropy loss, and stochastic gradient descent. It contains no compiled code or external libraries; every line of math is inspectable and modifiable within the HyperCard environment.

Key highlights include:
*   **Hardware Agnostic Math:** The project proves that the logic of deep learning can function on an 8 MHz 68000-series processor, though training to convergence (approx. 1,000 steps) takes several hours on original hardware.
*   **Independent Discovery:** After training, the model’s attention map reveals the "butterfly" routing pattern of the FFT, a structure the model discovers independently through gradient descent.
*   **Educational Transparency:** Designed as an "engine with the hood up," users can adjust learning rates or swap training tasks directly in the script editor.
*   **Technical Requirements:** It requires HyperCard 2.0 or later to ensure standard mathematical operator precedence, which was absent in earlier versions.

MacMind serves as both a technical feat and an educational tool, stripping away the "black box" of AI to show that the difference between vintage experiments and modern LLMs is primarily a matter of scale, not fundamental kind.

---

## 9. Artifacts: Versioned storage that speaks Git

**原文标题**: Artifacts: Versioned storage that speaks Git

**原文链接**: [https://blog.cloudflare.com/artifacts-git-for-agents-beta/](https://blog.cloudflare.com/artifacts-git-for-agents-beta/)

Cloudflare has introduced **Artifacts**, a distributed, versioned filesystem designed specifically to handle the high-volume storage demands of AI agents. Recognizing that agents generate code and state at a scale traditional source control platforms cannot support, Artifacts provides a storage primitive that "speaks Git" but is optimized for programmatic, serverless environments.

Key features and capabilities include:
*   **Git Compatibility:** Artifacts uses the Git protocol, making it natively compatible with standard Git clients and AI models already trained on Git workflows.
*   **Programmatic Management:** Developers can create repositories, generate credentials, and perform forks or imports via a REST API or a native Workers API.
*   **Agent-Centric Design:** It supports features like `git-notes` for attaching metadata (e.g., prompts or attribution) to commits without mutating objects.
*   **Optimized Performance:** For large repositories, Cloudflare is open-sourcing **ArtifactFS**, a filesystem driver that enables "async clones." This allows agents to start working immediately by hydrating file contents on the fly rather than waiting for a full download.

Technically, Artifacts is built on **Cloudflare Durable Objects** with a Git engine written in **Zig** and compiled to **WebAssembly**. This architecture allows for the creation of millions of isolated, stateful repositories.

Currently in private beta for paid Workers plans, a public beta is expected by **May 2026**. Pricing is consumption-based: **$0.50/GB per month** for storage and **$0.15 per 1,000 operations** (clones, forks, pushes), with a free tier planned. Future updates will include event subscriptions, search APIs, and native SDKs for TypeScript, Go, and Python.

---

## 10. Darkbloom – Private inference on idle Macs

**原文标题**: Darkbloom – Private inference on idle Macs

**原文链接**: [https://darkbloom.dev](https://darkbloom.dev)

Eigen Labs Research has introduced **Darkbloom**, a decentralized inference network designed to leverage the idle processing power of over 100 million Apple Silicon machines. By bypassing the traditional supply chain of GPU manufacturers and hyperscalers, Darkbloom offers AI inference at costs up to 70% lower than centralized providers like OpenAI or AWS.

**Key Features and Benefits:**
*   **For Users:** Access to an OpenAI-compatible API for text (LLMs up to 239B parameters), image generation, and speech-to-text at roughly half the market rate.
*   **For Hardware Owners:** Mac users can monetize idle hardware, retaining up to 100% of revenue. With Apple Silicon’s high efficiency, electricity costs remain as low as $0.01–$0.03 per hour, resulting in high profit margins.
*   **Privacy and Trust:** Darkbloom solves the "untrusted hardware" problem through a multi-layered security architecture. Using end-to-end encryption, Apple’s hardware-bound keys (Secure Enclave), and hardened runtimes, the network ensures that operators cannot observe or extract user data. Every response is hardware-verified and signed by the specific machine that produced it.

**Market Impact:**
The project likens its model to Airbnb or Uber, turning "idle capacity" into a competitive asset. By utilizing the 273 to 819 GB/s memory bandwidth of Apple Silicon, the network can run sophisticated models (such as Qwen 122B and MiniMax 239B) that typically require expensive enterprise GPUs.

**Implementation:**
Developers can integrate Darkbloom by simply changing their API base URL. Operators can currently join the network via a CLI tool, with a native macOS menu bar app currently in development. Darkbloom aims to democratize AI compute, shifting control away from a small number of centralized companies to a distributed network of individual hardware owners.

---

## 11. We gave an AI a 3 year retail lease and asked it to make a profit

**原文标题**: We gave an AI a 3 year retail lease and asked it to make a profit

**原文链接**: [https://andonlabs.com/blog/andon-market-launch](https://andonlabs.com/blog/andon-market-launch)

生成摘要时出错

---

## 12. Cloudflare Email Service

**原文标题**: Cloudflare Email Service

**原文链接**: [https://blog.cloudflare.com/email-for-agents/](https://blog.cloudflare.com/email-for-agents/)

生成摘要时出错

---

## 13. IPv6 traffic crosses the 50% mark

**原文标题**: IPv6 traffic crosses the 50% mark

**原文链接**: [https://www.google.com/intl/en/ipv6/statistics.html?yzh=28197](https://www.google.com/intl/en/ipv6/statistics.html?yzh=28197)

生成摘要时出错

---

## 14. Six Characters

**原文标题**: Six Characters

**原文链接**: [https://ajitem.com/blog/iron-core-part-2-six-characters/](https://ajitem.com/blog/iron-core-part-2-six-characters/)

生成摘要时出错

---

## 15. The paper computer

**原文标题**: The paper computer

**原文链接**: [https://jsomers.net/blog/the-paper-computer](https://jsomers.net/blog/the-paper-computer)

生成摘要时出错

---

## 16. Codex Hacked a Samsung TV

**原文标题**: Codex Hacked a Samsung TV

**原文链接**: [https://blog.calif.io/p/codex-hacked-a-samsung-tv](https://blog.calif.io/p/codex-hacked-a-samsung-tv)

生成摘要时出错

---

## 17. FSF trying to contact Google about spammer sending 10k+ mails from Gmail account

**原文标题**: FSF trying to contact Google about spammer sending 10k+ mails from Gmail account

**原文链接**: [https://daedal.io/@thomzane/116410863009847575](https://daedal.io/@thomzane/116410863009847575)

生成摘要时出错

---

## 18. AI cybersecurity is not proof of work

**原文标题**: AI cybersecurity is not proof of work

**原文链接**: [https://antirez.com/news/163](https://antirez.com/news/163)

生成摘要时出错

---

## 19. Modern Microprocessors – A 90-Minute Guide

**原文标题**: Modern Microprocessors – A 90-Minute Guide

**原文链接**: [https://www.lighterra.com/papers/modernmicroprocessors/](https://www.lighterra.com/papers/modernmicroprocessors/)

生成摘要时出错

---

## 20. Laravel raised money and now injects ads directly into your agent

**原文标题**: Laravel raised money and now injects ads directly into your agent

**原文链接**: [https://techstackups.com/articles/laravel-raised-money-and-now-injects-ads-directly-into-your-agent/](https://techstackups.com/articles/laravel-raised-money-and-now-injects-ads-directly-into-your-agent/)

生成摘要时出错

---

## 21. Claude Opus 4.7 Model Card

**原文标题**: Claude Opus 4.7 Model Card

**原文链接**: [https://anthropic.com/claude-opus-4-7-system-card](https://anthropic.com/claude-opus-4-7-system-card)

生成摘要时出错

---

## 22. Japan implements language proficiency requirements for certain visa applicants

**原文标题**: Japan implements language proficiency requirements for certain visa applicants

**原文链接**: [https://www.japantimes.co.jp/news/2026/04/15/japan/society/jlpt-visa-requirement/](https://www.japantimes.co.jp/news/2026/04/15/japan/society/jlpt-visa-requirement/)

生成摘要时出错

---

## 23. ChatGPT for Excel

**原文标题**: ChatGPT for Excel

**原文链接**: [https://chatgpt.com/apps/spreadsheets/](https://chatgpt.com/apps/spreadsheets/)

生成摘要时出错

---

## 24. €54k spike in 13h from unrestricted Firebase browser key accessing Gemini APIs

**原文标题**: €54k spike in 13h from unrestricted Firebase browser key accessing Gemini APIs

**原文链接**: [https://discuss.ai.google.dev/t/unexpected-54k-billing-spike-in-13-hours-firebase-browser-key-without-api-restrictions-used-for-gemini-requests/140262](https://discuss.ai.google.dev/t/unexpected-54k-billing-spike-in-13-hours-firebase-browser-key-without-api-restrictions-used-for-gemini-requests/140262)

生成摘要时出错

---

## 25. Mozilla Thunderbolt

**原文标题**: Mozilla Thunderbolt

**原文链接**: [https://www.thunderbolt.io/](https://www.thunderbolt.io/)

生成摘要时出错

---

## 26. PHP 8.6 Closure Optimizations

**原文标题**: PHP 8.6 Closure Optimizations

**原文链接**: [https://wiki.php.net/rfc/closure-optimizations](https://wiki.php.net/rfc/closure-optimizations)

生成摘要时出错

---

## 27. Cybersecurity looks like proof of work now

**原文标题**: Cybersecurity looks like proof of work now

**原文链接**: [https://www.dbreunig.com/2026/04/14/cybersecurity-is-proof-of-work-now.html](https://www.dbreunig.com/2026/04/14/cybersecurity-is-proof-of-work-now.html)

生成摘要时出错

---

## 28. RamAIn (YC W26) Is Hiring

**原文标题**: RamAIn (YC W26) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/ramain/jobs/bwtwd9W-founding-gtm-operations-lead](https://www.ycombinator.com/companies/ramain/jobs/bwtwd9W-founding-gtm-operations-lead)

生成摘要时出错

---

## 29. RedSun: System user access on Win 11/10 and Server with the April 2026 Update

**原文标题**: RedSun: System user access on Win 11/10 and Server with the April 2026 Update

**原文链接**: [https://github.com/Nightmare-Eclipse/RedSun](https://github.com/Nightmare-Eclipse/RedSun)

生成摘要时出错

---

## 30. North American English Dialects

**原文标题**: North American English Dialects

**原文链接**: [https://aschmann.net/AmEng/](https://aschmann.net/AmEng/)

生成摘要时出错

---

## 31. Too much discussion of the XOR swap trick

**原文标题**: Too much discussion of the XOR swap trick

**原文链接**: [https://heather.cafe/posts/too_much_xor_swap_trick/](https://heather.cafe/posts/too_much_xor_swap_trick/)

生成摘要时出错

---

## 32. Ancient DNA reveals pervasive directional selection across West Eurasia [pdf]

**原文标题**: Ancient DNA reveals pervasive directional selection across West Eurasia [pdf]

**原文链接**: [https://reich.hms.harvard.edu/sites/reich.hms.harvard.edu/files/inline-files/2026_Akbari_Nature_selection_0.pdf](https://reich.hms.harvard.edu/sites/reich.hms.harvard.edu/files/inline-files/2026_Akbari_Nature_selection_0.pdf)

生成摘要时出错

---

## 33. Show HN: Home Memory – A local DB of my house, down to cables and pipes

**原文标题**: Show HN: Home Memory – A local DB of my house, down to cables and pipes

**原文链接**: [https://github.com/impactjo/home-memory](https://github.com/impactjo/home-memory)

生成摘要时出错

---

## 34. Long Instruction Word architectures and the ELI-512

**原文标题**: Long Instruction Word architectures and the ELI-512

**原文链接**: [https://dl.acm.org/doi/10.1145/800046.801649](https://dl.acm.org/doi/10.1145/800046.801649)

生成摘要时出错

---

## 35. Moving a large-scale metrics pipeline from StatsD to OpenTelemetry / Prometheus

**原文标题**: Moving a large-scale metrics pipeline from StatsD to OpenTelemetry / Prometheus

**原文链接**: [https://medium.com/airbnb-engineering/building-a-high-volume-metrics-pipeline-with-opentelemetry-and-vmagent-c714d6910b45](https://medium.com/airbnb-engineering/building-a-high-volume-metrics-pipeline-with-opentelemetry-and-vmagent-c714d6910b45)

生成摘要时出错

---

## 36. Shares in shoe brand Allbirds rise 580% after it pivots from footwear to AI

**原文标题**: Shares in shoe brand Allbirds rise 580% after it pivots from footwear to AI

**原文链接**: [https://www.bbc.com/news/articles/c98mrepzgj7o](https://www.bbc.com/news/articles/c98mrepzgj7o)

生成摘要时出错

---

## 37. Where the DOGE Operatives Are Now

**原文标题**: Where the DOGE Operatives Are Now

**原文链接**: [https://www.wired.com/story/where-the-doge-operatives-are-now/](https://www.wired.com/story/where-the-doge-operatives-are-now/)

生成摘要时出错

---

## 38. Put your SSH keys in your TPM chip

**原文标题**: Put your SSH keys in your TPM chip

**原文链接**: [https://raymii.org/s/tutorials/Put_your_SSH_keys_in_your_TPM_chip.html](https://raymii.org/s/tutorials/Put_your_SSH_keys_in_your_TPM_chip.html)

生成摘要时出错

---

## 39. I made a terminal pager

**原文标题**: I made a terminal pager

**原文链接**: [https://theleo.zone/posts/pager/](https://theleo.zone/posts/pager/)

生成摘要时出错

---

## 40. KLM cancels 160 flights due to fuel shortage

**原文标题**: KLM cancels 160 flights due to fuel shortage

**原文链接**: [https://www.theguardian.com/business/live/2026/apr/16/uk-february-gdp-report-economy-iran-war-stock-market-reeves-ftse-sterling-live-updates](https://www.theguardian.com/business/live/2026/apr/16/uk-february-gdp-report-economy-iran-war-stock-market-reeves-ftse-sterling-live-updates)

生成摘要时出错

---

## 41. SDL bans AI-written commits

**原文标题**: SDL bans AI-written commits

**原文链接**: [https://github.com/libsdl-org/SDL/issues/15350](https://github.com/libsdl-org/SDL/issues/15350)

生成摘要时出错

---

## 42. Qwen3.6-35B-A3B on my laptop drew me a better pelican than Claude Opus 4.7

**原文标题**: Qwen3.6-35B-A3B on my laptop drew me a better pelican than Claude Opus 4.7

**原文链接**: [https://simonwillison.net/2026/Apr/16/qwen-beats-opus/](https://simonwillison.net/2026/Apr/16/qwen-beats-opus/)

生成摘要时出错

---

## 43. US v. Heppner (S.D.N.Y. 2026) no attorney-client privilege for AI chats [pdf]

**原文标题**: US v. Heppner (S.D.N.Y. 2026) no attorney-client privilege for AI chats [pdf]

**原文链接**: [https://fingfx.thomsonreuters.com/gfx/legaldocs/xmvjyjekkpr/Rakoff%20-%20order%20-%20AI.pdf](https://fingfx.thomsonreuters.com/gfx/legaldocs/xmvjyjekkpr/Rakoff%20-%20order%20-%20AI.pdf)

生成摘要时出错

---

## 44. Introduction to spherical harmonics for graphics programmers

**原文标题**: Introduction to spherical harmonics for graphics programmers

**原文链接**: [https://gpfault.net/posts/sph.html](https://gpfault.net/posts/sph.html)

生成摘要时出错

---

## 45. Retrofitting JIT Compilers into C Interpreters

**原文标题**: Retrofitting JIT Compilers into C Interpreters

**原文链接**: [https://tratt.net/laurie/blog/2026/retrofitting_jit_compilers_into_c_interpreters.html](https://tratt.net/laurie/blog/2026/retrofitting_jit_compilers_into_c_interpreters.html)

生成摘要时出错

---

## 46. Show HN: Libretto – Making AI browser automations deterministic

**原文标题**: Show HN: Libretto – Making AI browser automations deterministic

**原文链接**: [https://github.com/saffron-health/libretto](https://github.com/saffron-health/libretto)

生成摘要时出错

---

## 47. The Accursèd Alphabetical Clock

**原文标题**: The Accursèd Alphabetical Clock

**原文链接**: [https://boat.horse/clock/index.html](https://boat.horse/clock/index.html)

生成摘要时出错

---

## 48. Fast and Easy Levenshtein distance using a Trie (2011)

**原文标题**: Fast and Easy Levenshtein distance using a Trie (2011)

**原文链接**: [https://stevehanov.ca/blog/fast-and-easy-levenshtein-distance-using-a-trie](https://stevehanov.ca/blog/fast-and-easy-levenshtein-distance-using-a-trie)

生成摘要时出错

---

## 49. The Death of Character in Game Console Interfaces

**原文标题**: The Death of Character in Game Console Interfaces

**原文链接**: [https://vale.rocks/posts/game-console-interfaces](https://vale.rocks/posts/game-console-interfaces)

生成摘要时出错

---

## 50. FIXAPL

**原文标题**: FIXAPL

**原文链接**: [https://fixapl.netlify.app/](https://fixapl.netlify.app/)

生成摘要时出错

---

## 51. The buns in McDonald's Japan's burger photos are all slightly askew

**原文标题**: The buns in McDonald's Japan's burger photos are all slightly askew

**原文链接**: [https://www.mcdonalds.co.jp/en/menu/burger/](https://www.mcdonalds.co.jp/en/menu/burger/)

生成摘要时出错

---

## 52. Agent - Native Mac OS X coding ide/harness

**原文标题**: Agent - Native Mac OS X coding ide/harness

**原文链接**: [https://github.com/macOS26/Agent](https://github.com/macOS26/Agent)

生成摘要时出错

---

## 53. PiCore - Raspberry Pi Port of Tiny Core Linux

**原文标题**: PiCore - Raspberry Pi Port of Tiny Core Linux

**原文链接**: [http://tinycorelinux.net/5.x/armv6/releases/README](http://tinycorelinux.net/5.x/armv6/releases/README)

生成摘要时出错

---

## 54. A Look into NaviDial, Japan's Legacy Phone Service

**原文标题**: A Look into NaviDial, Japan's Legacy Phone Service

**原文链接**: [https://www.tokyodev.com/articles/a-look-into-navidial-japan-s-legacy-phone-service](https://www.tokyodev.com/articles/a-look-into-navidial-japan-s-legacy-phone-service)

生成摘要时出错

---

## 55. Tailscale-rs: Official Rust library for embedding Tailscale

**原文标题**: Tailscale-rs: Official Rust library for embedding Tailscale

**原文链接**: [https://tailscale.com/blog/tailscale-rs-rust-tsnet-library-preview](https://tailscale.com/blog/tailscale-rs-rust-tsnet-library-preview)

生成摘要时出错

---

## 56. The Gemini app is now on Mac

**原文标题**: The Gemini app is now on Mac

**原文链接**: [https://blog.google/innovation-and-ai/products/gemini-app/gemini-app-now-on-mac-os/](https://blog.google/innovation-and-ai/products/gemini-app/gemini-app-now-on-mac-os/)

生成摘要时出错

---

## 57. Show HN: Ilha – a UI library that fits in an AI context window

**原文标题**: Show HN: Ilha – a UI library that fits in an AI context window

**原文链接**: [https://ilha.build/](https://ilha.build/)

生成摘要时出错

---

## 58. Do you even need a database?

**原文标题**: Do you even need a database?

**原文链接**: [https://www.dbpro.app/blog/do-you-even-need-a-database](https://www.dbpro.app/blog/do-you-even-need-a-database)

生成摘要时出错

---

## 59. Live Nation illegally monopolized ticketing market, jury finds

**原文标题**: Live Nation illegally monopolized ticketing market, jury finds

**原文链接**: [https://www.bloomberg.com/news/articles/2026-04-15/live-nation-illegally-monopolized-ticketing-market-jury-finds](https://www.bloomberg.com/news/articles/2026-04-15/live-nation-illegally-monopolized-ticketing-market-jury-finds)

生成摘要时出错

---

## 60. Direct Win32 API, weird-shaped windows, and why they mostly disappeared

**原文标题**: Direct Win32 API, weird-shaped windows, and why they mostly disappeared

**原文链接**: [https://warped3.substack.com/p/direct-win32-api-weird-shaped-windows](https://warped3.substack.com/p/direct-win32-api-weird-shaped-windows)

生成摘要时出错

---

## 61. How can I keep from singing?

**原文标题**: How can I keep from singing?

**原文链接**: [https://blog.danieljanus.pl/singing/](https://blog.danieljanus.pl/singing/)

生成摘要时出错

---

## 62. Cal.com is going closed source

**原文标题**: Cal.com is going closed source

**原文链接**: [https://cal.com/blog/cal-com-goes-closed-source-why](https://cal.com/blog/cal-com-goes-closed-source-why)

生成摘要时出错

---

## 63. God sleeps in the minerals

**原文标题**: God sleeps in the minerals

**原文链接**: [https://wchambliss.wordpress.com/2026/03/03/god-sleeps-in-the-minerals/](https://wchambliss.wordpress.com/2026/03/03/god-sleeps-in-the-minerals/)

生成摘要时出错

---

## 64. What's new in Claude Opus 4.7

**原文标题**: What's new in Claude Opus 4.7

**原文链接**: [https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7)

生成摘要时出错

---

## 65. Fixing a monitor that goes black, off or blinks due to static electricity (2023)

**原文标题**: Fixing a monitor that goes black, off or blinks due to static electricity (2023)

**原文链接**: [https://aalonso.dev/blog/2023/how-to-fix-monitor-that-goes-black-off-due-to-static-electricity-in-chair/](https://aalonso.dev/blog/2023/how-to-fix-monitor-that-goes-black-off-due-to-static-electricity-in-chair/)

生成摘要时出错

---

## 66. Google broke its promise to me – now ICE has my data

**原文标题**: Google broke its promise to me – now ICE has my data

**原文链接**: [https://www.eff.org/deeplinks/2026/04/google-broke-its-promise-me-now-ice-has-my-data](https://www.eff.org/deeplinks/2026/04/google-broke-its-promise-me-now-ice-has-my-data)

生成摘要时出错

---

## 67. Show HN: Hiraeth – AWS Emulator

**原文标题**: Show HN: Hiraeth – AWS Emulator

**原文链接**: [https://github.com/SethPyle376/hiraeth](https://github.com/SethPyle376/hiraeth)

生成摘要时出错

---

## 68. Want to write a compiler? Just read these two papers (2008)

**原文标题**: Want to write a compiler? Just read these two papers (2008)

**原文链接**: [https://prog21.dadgum.com/30.html](https://prog21.dadgum.com/30.html)

生成摘要时出错

---

## 69. Google Gemma 4 Runs Natively on iPhone with Full Offline AI Inference

**原文标题**: Google Gemma 4 Runs Natively on iPhone with Full Offline AI Inference

**原文链接**: [https://www.gizmoweek.com/gemma-4-runs-iphone/](https://www.gizmoweek.com/gemma-4-runs-iphone/)

生成摘要时出错

---

## 70. Stealth signals are bypassing Iran’s internet blackout

**原文标题**: Stealth signals are bypassing Iran’s internet blackout

**原文链接**: [https://spectrum.ieee.org/iran-internet-blackout-satellite-tv](https://spectrum.ieee.org/iran-internet-blackout-satellite-tv)

生成摘要时出错

---

## 71. Intel Xpress Resurrection: Reviving a Forgotten EISA Beast

**原文标题**: Intel Xpress Resurrection: Reviving a Forgotten EISA Beast

**原文链接**: [https://x86.fr/intel-xpress-resurrection-reviving-a-forgotten-eisa-beast/](https://x86.fr/intel-xpress-resurrection-reviving-a-forgotten-eisa-beast/)

生成摘要时出错

---

## 72. Pokemon Evolution vs Darwinian Evolution

**原文标题**: Pokemon Evolution vs Darwinian Evolution

**原文链接**: [https://superheroetc.wordpress.com/2017/05/31/pokemon-evolution-vs-darwinian-evolution/](https://superheroetc.wordpress.com/2017/05/31/pokemon-evolution-vs-darwinian-evolution/)

生成摘要时出错

---

## 73. CRISPR takes important step toward silencing Down syndrome’s extra chromosome

**原文标题**: CRISPR takes important step toward silencing Down syndrome’s extra chromosome

**原文链接**: [https://medicalxpress.com/news/2026-04-crispr-bold-silencing-syndrome-extra.html](https://medicalxpress.com/news/2026-04-crispr-bold-silencing-syndrome-extra.html)

生成摘要时出错

---

## 74. Anna's Archive loses $322M Spotify piracy case without a fight

**原文标题**: Anna's Archive loses $322M Spotify piracy case without a fight

**原文链接**: [https://torrentfreak.com/annas-archive-loses-322-million-spotify-piracy-case-without-a-fight/](https://torrentfreak.com/annas-archive-loses-322-million-spotify-piracy-case-without-a-fight/)

生成摘要时出错

---

## 75. Open Source Isn't Dead

**原文标题**: Open Source Isn't Dead

**原文链接**: [https://www.strix.ai/blog/cal-com-is-closing-its-code-due-to-ai-threats](https://www.strix.ai/blog/cal-com-is-closing-its-code-due-to-ai-threats)

生成摘要时出错

---

## 76. Hacker News CLI (2014)

**原文标题**: Hacker News CLI (2014)

**原文链接**: [https://pythonhosted.org/hackernews-cli/commands.html](https://pythonhosted.org/hackernews-cli/commands.html)

生成摘要时出错

---

## 77. The public sours on AI, data centers as firms look to IPO, tech keeps spending

**原文标题**: The public sours on AI, data centers as firms look to IPO, tech keeps spending

**原文链接**: [https://www.cnbc.com/2026/04/15/public-opinion-ai-data-centers-anthropic-openai-ipo.html](https://www.cnbc.com/2026/04/15/public-opinion-ai-data-centers-anthropic-openai-ipo.html)

生成摘要时出错

---

## 78. Good sleep, good learning, good life (2012)

**原文标题**: Good sleep, good learning, good life (2012)

**原文链接**: [https://super-memory.com/articles/sleep.htm](https://super-memory.com/articles/sleep.htm)

生成摘要时出错

---

## 79. C++26: Structured Bindings in Conditions

**原文标题**: C++26: Structured Bindings in Conditions

**原文链接**: [https://www.sandordargo.com/blog/2026/04/15/cpp26-structured-bindings-condition](https://www.sandordargo.com/blog/2026/04/15/cpp26-structured-bindings-condition)

生成摘要时出错

---

## 80. YouTube users get option to set their Shorts time limit to zero minutes

**原文标题**: YouTube users get option to set their Shorts time limit to zero minutes

**原文链接**: [https://www.theverge.com/streaming/912898/youtube-shorts-feed-limit-zero-minutes](https://www.theverge.com/streaming/912898/youtube-shorts-feed-limit-zero-minutes)

生成摘要时出错

---

## 81. US nationals behind DPRK IT worker 'laptop farm' sent to prison

**原文标题**: US nationals behind DPRK IT worker 'laptop farm' sent to prison

**原文链接**: [https://www.bleepingcomputer.com/news/security/us-nationals-behind-north-korean-it-worker-laptop-farm-sent-to-prison/](https://www.bleepingcomputer.com/news/security/us-nationals-behind-north-korean-it-worker-laptop-farm-sent-to-prison/)

生成摘要时出错

---

## 82. The Internet's Most Powerful Archiving Tool Is in Peril

**原文标题**: The Internet's Most Powerful Archiving Tool Is in Peril

**原文链接**: [https://www.wired.com/story/the-internets-most-powerful-archiving-tool-is-in-mortal-peril/](https://www.wired.com/story/the-internets-most-powerful-archiving-tool-is-in-mortal-peril/)

生成摘要时出错

---

## 83. Ohio prison inmates 'built computers and hid them in ceiling' (2017)

**原文标题**: Ohio prison inmates 'built computers and hid them in ceiling' (2017)

**原文链接**: [https://www.bbc.com/news/technology-39576394](https://www.bbc.com/news/technology-39576394)

生成摘要时出错

---

## 84. PBS Nova: Terror in Space (1998)

**原文标题**: PBS Nova: Terror in Space (1998)

**原文链接**: [https://www.pbs.org/wgbh/nova/mir/](https://www.pbs.org/wgbh/nova/mir/)

生成摘要时出错

---

## 85. Fly Drones from the Browser

**原文标题**: Fly Drones from the Browser

**原文链接**: [https://fpvsim.com/sim](https://fpvsim.com/sim)

生成摘要时出错

---

## 86. The Age of Snarky UI

**原文标题**: The Age of Snarky UI

**原文链接**: [https://thoughtbot.com/blog/the-age-of-snarky-ui](https://thoughtbot.com/blog/the-age-of-snarky-ui)

生成摘要时出错

---

## 87. Dependency cooldowns turn you into a free-rider

**原文标题**: Dependency cooldowns turn you into a free-rider

**原文链接**: [https://calpaterson.com/deps.html](https://calpaterson.com/deps.html)

生成摘要时出错

---

## 88. Show HN: Gave Claude a casino bankroll – it gambles till it's too broke to think

**原文标题**: Show HN: Gave Claude a casino bankroll – it gambles till it's too broke to think

**原文链接**: [https://letaigamble.com/](https://letaigamble.com/)

生成摘要时出错

---

## 89. Monsters in the Archives by Caroline Bicks – The Writing Secrets of Stephen King

**原文标题**: Monsters in the Archives by Caroline Bicks – The Writing Secrets of Stephen King

**原文链接**: [https://www.theguardian.com/books/2026/mar/30/monsters-in-the-archives-by-caroline-bicks-review-the-writing-secrets-of-stephen-king](https://www.theguardian.com/books/2026/mar/30/monsters-in-the-archives-by-caroline-bicks-review-the-writing-secrets-of-stephen-king)

生成摘要时出错

---

## 90. One interface, every protocol

**原文标题**: One interface, every protocol

**原文链接**: [https://openbindings.com/blog/one-interface-every-protocol](https://openbindings.com/blog/one-interface-every-protocol)

生成摘要时出错

---

## 91. Claude Code Routines

**原文标题**: Claude Code Routines

**原文链接**: [https://code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines)

生成摘要时出错

---

## 92. DESI Completes Planned 3D Map of the Universe

**原文标题**: DESI Completes Planned 3D Map of the Universe

**原文链接**: [https://newscenter.lbl.gov/2026/04/15/desi-completes-planned-3d-map-of-the-universe-and-continues-exploring/](https://newscenter.lbl.gov/2026/04/15/desi-completes-planned-3d-map-of-the-universe-and-continues-exploring/)

生成摘要时出错

---

## 93. The Future of Everything Is Lies, I Guess: New Jobs

**原文标题**: The Future of Everything Is Lies, I Guess: New Jobs

**原文链接**: [https://aphyr.com/posts/419-the-future-of-everything-is-lies-i-guess-new-jobs](https://aphyr.com/posts/419-the-future-of-everything-is-lies-i-guess-new-jobs)

生成摘要时出错

---

## 94. 5NF and Database Design

**原文标题**: 5NF and Database Design

**原文链接**: [https://kb.databasedesignbook.com/posts/5nf/](https://kb.databasedesignbook.com/posts/5nf/)

生成摘要时出错

---

## 95. Keycard – inject API keys into subprocesses, never touch shell env

**原文标题**: Keycard – inject API keys into subprocesses, never touch shell env

**原文链接**: [https://www.keycard.studio/](https://www.keycard.studio/)

生成摘要时出错

---

## 96. The local LLM ecosystem doesn’t need Ollama

**原文标题**: The local LLM ecosystem doesn’t need Ollama

**原文链接**: [https://sleepingrobots.com/dreams/stop-using-ollama/](https://sleepingrobots.com/dreams/stop-using-ollama/)

生成摘要时出错

---

## 97. Not all elementary functions can be expressed with exp-minus-log

**原文标题**: Not all elementary functions can be expressed with exp-minus-log

**原文链接**: [https://www.stylewarning.com/posts/not-all-elementary/](https://www.stylewarning.com/posts/not-all-elementary/)

生成摘要时出错

---

## 98. Rare concert recordings are landing on the Internet Archive

**原文标题**: Rare concert recordings are landing on the Internet Archive

**原文链接**: [https://techcrunch.com/2026/04/13/thousands-of-rare-concert-recordings-are-landing-on-the-internet-archive-listen-now/](https://techcrunch.com/2026/04/13/thousands-of-rare-concert-recordings-are-landing-on-the-internet-archive-listen-now/)

生成摘要时出错

---

## 99. How Wake-On-LAN works (2020)

**原文标题**: How Wake-On-LAN works (2020)

**原文链接**: [https://blog.xaner.dev/post/wake-on-lan/](https://blog.xaner.dev/post/wake-on-lan/)

生成摘要时出错

---

## 100. Study: Back-to-basics approach can match or outperform AI in language analysis

**原文标题**: Study: Back-to-basics approach can match or outperform AI in language analysis

**原文链接**: [https://www.manchester.ac.uk/about/news/back-to-basics-approach-can-match-or-outperform-ai/](https://www.manchester.ac.uk/about/news/back-to-basics-approach-can-match-or-outperform-ai/)

生成摘要时出错

---

