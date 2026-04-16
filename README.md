# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-16.md)

*最后自动更新时间: 2026-04-16 18:34:39*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 2 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 3 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 4 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 5 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 6 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 7 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 8 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 9 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 10 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 11 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 12 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 13 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 14 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 15 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 16 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 17 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 18 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 19 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 20 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 21 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 22 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 23 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 24 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 25 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 26 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 27 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 28 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 29 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 30 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 31 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 32 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 33 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 34 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 35 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 36 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 37 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 38 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 39 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 40 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 41 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 42 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 43 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 44 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 45 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 46 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 47 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 48 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 49 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 50 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 51 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 52 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 53 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 54 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 55 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 56 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 57 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 58 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 59 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 60 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 61 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 62 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 63 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 64 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 65 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 66 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 67 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 68 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 69 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 70 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 71 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 72 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 73 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 74 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 75 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 76 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 77 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 78 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 79 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 80 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 81 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 82 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 83 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 84 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 85 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 86 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 87 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 88 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 89 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 90 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 91 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 92 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 93 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 94 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 95 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 96 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 97 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 98 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 99 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 100 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 101 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 102 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 103 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 104 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 105 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 106 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 107 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 108 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 109 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 110 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 111 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 112 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 113 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 114 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 115 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 116 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 117 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 118 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 119 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 120 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 121 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 122 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 123 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 124 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 125 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 126 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 127 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 128 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 129 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 130 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 131 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 132 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 133 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 134 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 135 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 136 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 137 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 138 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 139 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 140 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 141 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 142 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 143 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 144 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 145 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 146 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 147 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 148 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 149 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 150 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 151 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 152 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 153 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 154 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 155 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 156 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 157 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 158 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 159 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 160 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 161 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 162 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 163 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 164 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 165 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 166 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 167 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 168 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 169 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 170 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 171 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 172 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 173 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 174 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 175 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 176 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 177 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 178 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 179 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 180 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 181 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 182 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 183 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 184 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 185 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 186 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 187 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 188 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 189 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 190 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 191 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 192 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 193 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 194 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 195 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 196 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 197 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 198 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 199 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 200 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 201 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 202 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 203 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 204 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 205 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 206 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 207 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 208 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 209 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 210 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 211 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 212 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 213 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 214 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 215 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 216 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 217 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 218 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 219 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 220 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 221 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 222 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 223 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 224 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 225 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 226 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 227 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 228 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 229 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 230 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 231 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 232 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 233 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 234 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 235 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 236 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 237 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 238 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 239 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 240 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 241 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 242 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 243 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 244 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 245 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 246 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 247 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 248 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 249 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 250 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 251 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 252 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 253 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 254 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 255 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 256 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 257 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 258 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 259 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 260 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 261 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 262 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 263 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 264 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 265 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 266 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 267 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 268 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 269 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 270 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 271 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 272 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 273 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 274 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 275 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 276 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 277 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 278 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 279 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 280 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 281 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 282 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 283 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 284 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 285 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 286 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 287 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 288 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 289 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 290 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 291 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 292 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 293 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 294 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 295 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 296 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 297 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 298 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 299 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 300 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 301 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 302 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 303 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 304 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 305 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 306 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 307 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 308 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 309 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 310 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 311 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 312 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 313 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 314 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 315 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 316 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 317 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 318 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 319 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 320 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 321 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 322 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 323 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 324 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 325 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 326 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 327 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 328 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 329 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 330 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 331 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 332 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 333 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 334 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 335 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 336 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 337 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 338 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 339 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 340 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 341 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 342 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 343 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 344 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 345 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 346 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 347 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 348 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 349 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 350 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 351 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 352 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 353 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 354 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 355 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 356 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 357 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 358 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 359 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 360 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 361 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 362 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 363 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 364 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 365 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 366 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 367 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 368 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 369 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 370 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 371 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 372 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 373 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 374 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 375 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 376 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 377 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 378 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 379 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 380 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 381 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 382 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 383 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 384 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 385 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 386 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 387 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 388 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 389 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 390 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 391 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 392 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
