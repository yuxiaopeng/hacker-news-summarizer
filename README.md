# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-03-21.md)

*最后自动更新时间: 2026-03-21 17:54:02*
## 1. 有些事，急不来。

**原文标题**: Some Things Just Take Time

**原文链接**: [https://lucumr.pocoo.org/2026/3/20/some-things-just-take-time/](https://lucumr.pocoo.org/2026/3/20/some-things-just-take-time/)

在《有些事情就是需要时间》一文中，Armin Ronacher 指出，生活和商业中最有价值的事物——正如一棵五十年的橡树——无法通过金钱或速度来复制，它们需要时间的沉淀。

Ronacher 批判了现代科技行业对即时满足和“氛围废料”（vibe slop）的痴迷。尽管人工智能可以瞬间生成代码，初创公司可以快速迭代，但这种速度往往以牺牲质量和长久性为代价。他注意到一种令人不安的趋势：初创公司频繁“消失”，开源项目转瞬即逝，它们都缺乏建立持久信任和社区所需的**韧性**。

核心观点包括：
*   **摩擦的必要性：** 尽管行业试图通过自动化消除每一个障碍，但 Ronacher 认为，摩擦（如合规或“冷静期”）对于深思熟虑的决策和走向成熟往往至关重要。
*   **省时工具的悖论：** 尽管人工智能和代理工具承诺可以节省时间，但 Ronacher 观察到，省下的任何时间都会立即被加剧的竞争和产出更多成果的压力所消耗。因此，我们感到比以往任何时候都更加匆忙。
*   **作为价值的承诺：** 结合其二十年的开源经验，Ronacher 断言，真正的成功源于在最初的热情消退后，依然能够长期坚守并解决问题。时间将一个简单的计划转化为一份“深植根基的承诺”，最终能够为他人提供庇护和支持。

Ronacher 最终总结道，信任、质量和社区是数年积累的产物，而非周末冲刺的结果。在这个软件商品化的时代，唯有那些我们愿意为其等待的事物，才能真正经受住时间的考验。

---

## 2. Grafeo – 一款基于 Rust 构建的快速、轻量、可嵌入式图数据库

**原文标题**: Grafeo – A fast, lean, embeddable graph database built in Rust

**原文链接**: [https://grafeo.dev/](https://grafeo.dev/)

**Grafeo** 是一款基于 Rust 构建的高性能、可嵌入图数据库，专为极速、高效和灵活性而设计。根据 LDBC 社交网络基准测试（LDBC Social Network Benchmark），它是目前已测试的最快图数据库，利用了向量化执行、SIMD 优化操作以及低内存占用等技术。

Grafeo 的一大突出特点是其通用性。它支持**双数据模型**——标签属性图（LPG）和 RDF 三元组，并兼容广泛的**查询语言**，包括 GQL、Cypher、Gremlin、SPARQL、GraphQL 以及 SQL/PGQ。这使得开发人员可以根据其特定的领域或专长选择最合适的模型和语言。

关键技术能力包括：
*   **向量搜索：** 基于 HNSW 的带量化相似性搜索，支持将图遍历与语义 AI 搜索相结合。
*   **ACID 合规性：** 通过基于 MVCC 的快照隔离提供可靠的生产性能。
*   **架构：** 采用列式存储、基于代价的查询优化和特定类型压缩的推送式（push-based）执行引擎。
*   **部署：** 既可以零依赖直接嵌入到应用程序中，也可以作为带有 REST API 和 Web UI 的独立服务器运行。

Grafeo 旨在实现广泛的集成，提供针对 **Python、Node.js、Go、Rust、C#、Dart 和 WebAssembly** 的原生绑定。它还拥有一个不断壮大的生态系统，集成了 LangChain 和 LlamaIndex 等 AI 工具。Grafeo 采用 Apache-2.0 协议开源。

---

## 3. OpenCode – Open source AI coding agent

**原文标题**: OpenCode – Open source AI coding agent

**原文链接**: [https://opencode.ai/](https://opencode.ai/)

生成摘要时出错

---

## 4. 404 未找到 Deno CEO

**原文标题**: 404 Deno CEO not found

**原文链接**: [https://dbushell.com/2026/03/20/denos-decline-and-layoffs/](https://dbushell.com/2026/03/20/denos-decline-and-layoffs/)

本文以 2026 年 3 月 20 日的视角，报道了 Deno Land Inc. 在大规模裁员及首席执行官 Ryan Dahl 保持沉默后的严重衰退。尽管该公司筹集了 2600 万美元的资金并发布了 Deno 2.0，但据报道，其在开发者采用率和投资者预期的商业增长方面表现乏力。

作者指出了导致 Deno 危机的几个关键因素：

*   **产品增长失败：** 作为公司主要收入来源的 Deno Deploy 性能不稳定，且在响应开发者反馈方面表现迟缓。 
*   **战略失误：** JSR (JavaScript Registry) 无法与 NPMX 等替代方案竞争。作者认为，Deno 在 HTTP 导入上的“转舵”以及包管理方面令人困惑的文档，为更青睐 Node/NPM 生态的开发者制造了不必要的障碍。
*   **商业可行性：** 随着一半员工被裁的消息传出，作者指出 Deno 为期五年的资金跑道可能已消耗殆尽，且未能建立可持续的商业模式。

文章强调了 Ryan Dahl 针对裁员始终未发表官方声明，这与其此前称“关于 Deno 没落的报道被严重夸大”的言论形成鲜明对比。尽管作者表达了对 Deno 运行时在技术上优于 Node 和 Bun 的个人偏爱，但最终得出的结论是，该公司目前已是一座“鬼城”。文中提到的潜在出路包括向 AI 领域的孤注一掷或传闻中被 OpenAI 收购，但作者对公司能否东山再起仍持怀疑态度。

---

## 5. ZJIT 消除冗余的对象加载与存储

**原文标题**: ZJIT removes redundant object loads and stores

**原文链接**: [https://railsatscale.com/2026-03-18-how-zjit-removes-redundant-object-loads-and-stores/](https://railsatscale.com/2026-03-18-how-zjit-removes-redundant-object-loads-and-stores/)

This article highlights a significant performance milestone for **ZJIT**, a Ruby JIT compiler, which now surpasses **YJIT** on specific microbenchmarks following the implementation of a new **load-store optimization** pass. Specifically, on the `setivar` benchmark, ZJIT is twice as fast as YJIT and 25 times faster than the standard interpreter.

The optimization occurs within ZJIT’s **High-level Intermediate Representation (HIR)**, utilizing its Static Single Assignment (SSA) form. It targets `LoadField` and `StoreField` instructions, which are used in CRuby for both instance variable management and object shape transitions. 

**The Mechanism:**
The algorithm employs a lightweight abstract interpretation within individual basic blocks. It uses a hashmap to cache triples of (object, offset, value):
*   **Redundant Stores:** If a `StoreField` attempts to write a value already present at a specific object offset, the instruction is deleted.
*   **Redundant Loads:** If a `LoadField` targets a previously cached value, the instruction is removed, and subsequent references are updated to use the cached value.

**Soundness and Design:**
To ensure program behavior remains unchanged, the optimizer carefully handles **aliasing** and **side effects**. The cache is cleared or specific entries are removed when encountering instructions that could modify objects, such as `WriteBarrier` operations or arbitrary method calls. 

The authors explain that while a more complex SSA representation could handle these optimizations, ZJIT’s current "lightweight" approach balances performance gains with architectural simplicity. Future work will focus on dead store elimination and type-based alias analysis to further optimize object initialization and interaction.

---

## 6. Show HN：AI SDLC Scaffold，用于 AI 辅助软件开发的仓库模板

**原文标题**: Show HN: AI SDLC Scaffold, repo template for AI-assisted software development

**原文链接**: [https://github.com/pangon/ai-sdlc-scaffold/](https://github.com/pangon/ai-sdlc-scaffold/)

**AI SDLC Scaffold** 是一个专为 AI 优先软件开发设计的仓库模板，特别针对 **Claude Code** 进行了优化。它将软件开发生命周期 (SDLC) 组织为四个结构化阶段——目标 (Objectives)、设计 (Design)、代码 (Code) 和部署 (Deploy)，提供了一个在人类高级监督下由 AI 代理执行工作的框架。

该脚手架基于四大核心原则：
1. **AI 优先开发：** 代理执行具体任务，而人类负责定义方向并审批产出。
2. **全库化管理 (Everything-in-Repo)：** 需求、架构、决策和任务跟踪与源代码共存，确保代理无需外部工具即可获得完整上下文。
3. **上下文效率：** 通过层级化指令结构（利用 `CLAUDE.md` 文件）和“双文件”决策记录，最大程度减少 Token 消耗。
4. **可追溯性：** 从目标到代码的每一个产出物都通过唯一 ID 进行关联，以确保一致性。

**工作流与自动化**
该系统利用内置的“技能”（斜杠命令）自动完成各阶段间的转换：
* **目标阶段：** `/SDLC-init` 和 `/SDLC-elicit` 用于收集需求并定义利益相关者。
* **设计阶段：** `/SDLC-design` 起草架构，`/SDLC-decompose` 识别软件组件。
* **代码阶段：** `/SDLC-implementation-plan` 生成任务清单，而 `/SDLC-execute-next-task` 负责编码和测试。
* **跨阶段：** `/SDLC-status` 提供项目仪表板，用于跟踪进度和“可追溯性健康度”。

系统不鼓励手动编辑，以确保 AI 始终是仓库一致性的主要维护者。通过使用此脚手架，开发人员可以通过标准化的、由代理主导的流程，将模糊的想法转化为已部署的系统，并将每一项设计决策和需求记录在版本控制仓库中。

---

## 7. Meta 1600 种语言全语种机器翻译

**原文标题**: Meta's Omnilingual MT for 1,600 Languages

**原文链接**: [https://ai.meta.com/research/publications/omnilingual-mt-machine-translation-for-1600-languages/?_fb_noscript=1](https://ai.meta.com/research/publications/omnilingual-mt-machine-translation-for-1600-languages/?_fb_noscript=1)

在这项研究成果中，Meta AI 详细介绍了一项机器翻译（MT）领域的重大突破，通过扩展翻译能力，使其覆盖超过 **1,600 种语言**。这项工作建立在 Meta 先前的“不遗漏任何语言”（NLLB）计划基础之上，该计划最初支持 200 种语言。

该论文解决的主要挑战是人工智能领域的“数字鸿沟”。由于缺乏可用的训练数据，在全球 7,000 多种语言中，大多数翻译工具仅支持其中的一小部分。为了克服这一难题，Meta 的研究人员在单一的统一模型中采用了**大规模多语言方法**。

**该研究的核心亮点包括：**

*   **大规模数据挖掘：** 该团队利用先进的数据挖掘技术，在互联网上识别出数百种以前缺乏数字化呈现的低资源语言的平行句子。
*   **自监督学习：** 对于几乎没有平行数据的语言，该模型利用单语数据进行自监督学习以理解语言结构，随后针对翻译任务进行微调。
*   **统一架构：** 研究人员没有为每个语言对构建单独的模型，而是采用了单一的 Transformer 模型。这使得系统能够将知识从高资源语言（如英语或西班牙语）迁移到语言相关的低资源语言中。
*   **评估基准：** 为了确保准确性，团队开发了新的评估数据集，用以衡量这一扩展语言范围内的翻译质量。

**意义：**
通过将语言覆盖范围扩大到 1,600 种，Meta 旨在提升全球的包容性和可访问性。这项研究为“通用翻译”提供了路线图，使原本缺乏支持的语言使用者能够获取以前无法触及的信息、教育资源和数字服务。

---

## 8. Mamba-3

**原文标题**: Mamba-3

**原文链接**: [https://www.together.ai/blog/mamba-3](https://www.together.ai/blog/mamba-3)

Mamba-3 是一种新型状态空间模型 (SSM)，旨在优先考虑**推理效率**，标志着其从 Mamba-2 对训练速度的侧重发生了转变。该模型由卡内基梅隆大学 (CMU)、普林斯顿大学、Cartesia AI 和 Together AI 合作开发，通过增强底层 SSM 机制的表达能力，解决了推理过程中受内存限制的问题。

关键方法论升级包括：
*   **增强型循环 (Enhanced Recurrence)**：一种源自指数-梯形离散化方案的更复杂公式。
*   **复数值状态 (Complex-Valued States)**：扩展了状态跟踪能力，以实现更丰富的动态特性。
*   **MIMO 变体**：一种多输入多输出变体，通过在解码过程中利用空闲 GPU 核心来提高准确性，在不增加延迟的情况下提升性能。

在架构上，Mamba-3 采用了多项现代改进：引入了 **QKNorm** 以增强训练稳定性，利用了交错的 MLP 层，并移除了 Mamba-1/2 中使用的传统“短卷积”，转而通过新的循环方案和特定偏置项来实现其功能。

实证研究表明，在 1.5B 规模下，Mamba-3 SISO（单输入单输出）在预填充和解码延迟方面优于 Mamba-2、Gated DeltaNet，甚至超过了基于 Transformer 的 Llama-3.2-1B。虽然研究人员承认纯线性模型在检索任务中仍落后于 Transformer，但他们证明了 Mamba-3 在结合线性层与自注意力的**混合模型**中非常有效。

为了促进应用并提升性能，团队开源了高速算子内核。这些内核使用 **Triton、TileLang 和 CuTe DSL** 等复杂技术栈构建，在现代 Hopper GPU 上实现了 CUDA 级的控制和优化的内存管理。最终，在推理任务日益繁重的大语言模型 (LLM) 格局中，Mamba-3 代表了高效、高性能部署的新前沿。

---

## 9. Ubuntu 26.04 Ends 46 Years of Silent sudo Passwords

**原文标题**: Ubuntu 26.04 Ends 46 Years of Silent sudo Passwords

**原文链接**: [https://pbxscience.com/ubuntu-26-04-ends-46-years-of-silent-sudo-passwords/](https://pbxscience.com/ubuntu-26-04-ends-46-years-of-silent-sudo-passwords/)

生成摘要时出错

---

## 10. Books of the Century by Le Monde

**原文标题**: Books of the Century by Le Monde

**原文链接**: [https://standardebooks.org/collections/le-mondes-100-books-of-the-century](https://standardebooks.org/collections/le-mondes-100-books-of-the-century)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 2 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 3 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 4 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 5 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 6 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 7 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 8 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 9 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 10 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 11 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 12 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 13 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 14 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 15 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 16 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 17 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 18 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 19 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 20 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 21 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 22 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 23 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 24 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 25 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 26 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 27 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 28 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 29 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 30 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 31 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 32 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 33 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 34 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 35 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 36 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 37 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 38 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 39 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 40 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 41 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 42 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 43 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 44 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 45 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 46 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 47 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 48 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 49 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 50 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 51 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 52 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 53 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 54 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 55 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 56 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 57 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 58 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 59 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 60 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 61 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 62 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 63 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 64 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 65 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 66 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 67 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 68 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 69 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 70 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 71 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 72 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 73 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 74 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 75 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 76 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 77 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 78 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 79 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 80 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 81 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 82 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 83 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 84 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 85 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 86 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 87 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 88 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 89 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 90 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 91 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 92 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 93 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 94 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 95 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 96 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 97 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 98 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 99 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 100 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 101 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 102 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 103 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 104 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 105 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 106 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 107 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 108 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 109 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 110 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 111 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 112 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 113 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 114 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 115 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 116 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 117 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 118 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 119 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 120 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 121 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 122 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 123 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 124 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 125 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 126 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 127 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 128 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 129 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 130 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 131 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 132 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 133 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 134 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 135 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 136 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 137 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 138 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 139 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 140 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 141 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 142 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 143 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 144 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 145 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 146 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 147 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 148 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 149 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 150 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 151 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 152 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 153 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 154 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 155 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 156 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 157 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 158 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 159 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 160 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 161 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 162 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 163 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 164 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 165 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 166 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 167 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 168 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 169 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 170 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 171 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 172 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 173 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 174 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 175 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 176 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 177 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 178 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 179 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 180 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 181 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 182 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 183 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 184 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 185 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 186 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 187 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 188 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 189 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 190 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 191 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 192 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 193 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 194 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 195 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 196 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 197 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 198 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 199 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 200 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 201 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 202 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 203 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 204 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 205 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 206 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 207 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 208 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 209 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 210 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 211 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 212 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 213 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 214 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 215 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 216 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 217 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 218 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 219 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 220 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 221 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 222 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 223 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 224 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 225 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 226 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 227 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 228 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 229 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 230 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 231 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 232 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 233 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 234 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 235 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 236 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 237 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 238 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 239 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 240 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 241 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 242 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 243 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 244 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 245 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 246 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 247 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 248 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 249 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 250 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 251 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 252 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 253 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 254 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 255 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 256 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 257 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 258 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 259 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 260 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 261 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 262 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 263 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 264 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 265 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 266 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 267 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 268 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 269 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 270 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 271 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 272 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 273 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 274 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 275 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 276 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 277 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 278 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 279 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 280 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 281 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 282 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 283 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 284 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 285 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 286 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 287 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 288 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 289 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 290 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 291 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 292 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 293 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 294 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 295 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 296 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 297 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 298 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 299 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 300 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 301 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 302 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 303 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 304 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 305 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 306 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 307 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 308 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 309 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 310 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 311 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 312 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 313 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 314 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 315 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 316 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 317 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 318 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 319 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 320 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 321 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 322 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 323 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 324 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 325 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 326 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 327 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 328 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 329 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 330 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 331 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 332 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 333 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 334 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 335 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 336 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 337 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 338 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 339 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 340 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 341 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 342 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 343 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 344 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 345 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 346 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 347 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 348 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 349 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 350 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 351 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 352 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 353 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 354 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 355 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 356 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 357 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 358 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 359 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 360 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 361 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 362 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 363 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 364 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 365 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 366 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
