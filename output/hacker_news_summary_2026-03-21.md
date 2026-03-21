# Hacker News 热门文章摘要 (2026-03-21)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. A Japanese glossary of chopsticks faux pas (2022)

**原文标题**: A Japanese glossary of chopsticks faux pas (2022)

**原文链接**: [https://www.nippon.com/en/japan-data/h01362/](https://www.nippon.com/en/japan-data/h01362/)

生成摘要时出错

---

## 12. Blocking Internet Archive Won't Stop AI, but Will Erase Web's Historical Record

**原文标题**: Blocking Internet Archive Won't Stop AI, but Will Erase Web's Historical Record

**原文链接**: [https://www.eff.org/deeplinks/2026/03/blocking-internet-archive-wont-stop-ai-it-will-erase-webs-historical-record](https://www.eff.org/deeplinks/2026/03/blocking-internet-archive-wont-stop-ai-it-will-erase-webs-historical-record)

生成摘要时出错

---

## 13. FFmpeg 101 (2024)

**原文标题**: FFmpeg 101 (2024)

**原文链接**: [https://blogs.igalia.com/llepage/ffmpeg-101/](https://blogs.igalia.com/llepage/ffmpeg-101/)

生成摘要时出错

---

## 14. Senior European journalist suspended over AI-generated quotes

**原文标题**: Senior European journalist suspended over AI-generated quotes

**原文链接**: [https://www.theguardian.com/technology/2026/mar/20/mediahuis-suspends-senior-journalist-over-ai-generated-quotes](https://www.theguardian.com/technology/2026/mar/20/mediahuis-suspends-senior-journalist-over-ai-generated-quotes)

生成摘要时出错

---

## 15. Molly guard in reverse

**原文标题**: Molly guard in reverse

**原文链接**: [https://unsung.aresluna.org/molly-guard-in-reverse/](https://unsung.aresluna.org/molly-guard-in-reverse/)

生成摘要时出错

---

## 16. Invisalign Became the Biggest User of 3D Printers

**原文标题**: Invisalign Became the Biggest User of 3D Printers

**原文链接**: [https://www.wired.com/story/how-invisalign-became-the-worlds-biggest-3d-printing-company/](https://www.wired.com/story/how-invisalign-became-the-worlds-biggest-3d-printing-company/)

生成摘要时出错

---

## 17. Fujifilm X RAW STUDIO webapp clone

**原文标题**: Fujifilm X RAW STUDIO webapp clone

**原文链接**: [https://github.com/eggricesoy/filmkit](https://github.com/eggricesoy/filmkit)

生成摘要时出错

---

## 18. How we give every user SQL access to a shared ClickHouse cluster

**原文标题**: How we give every user SQL access to a shared ClickHouse cluster

**原文链接**: [https://trigger.dev/blog/how-trql-works](https://trigger.dev/blog/how-trql-works)

生成摘要时出错

---

## 19. Iran launched unsuccessful attack on UK's Diego Garcia

**原文标题**: Iran launched unsuccessful attack on UK's Diego Garcia

**原文链接**: [https://www.bbc.com/news/articles/c5yljdgwppzo](https://www.bbc.com/news/articles/c5yljdgwppzo)

生成摘要时出错

---

## 20. Ghostling

**原文标题**: Ghostling

**原文链接**: [https://github.com/ghostty-org/ghostling](https://github.com/ghostty-org/ghostling)

生成摘要时出错

---

## 21. An industrial piping contractor on Claude Code [video]

**原文标题**: An industrial piping contractor on Claude Code [video]

**原文链接**: [https://twitter.com/toddsaunders/status/2034243420147859716](https://twitter.com/toddsaunders/status/2034243420147859716)

生成摘要时出错

---

## 22. Linux Applications Programming by Example: The Fundamental APIs (2nd Edition)

**原文标题**: Linux Applications Programming by Example: The Fundamental APIs (2nd Edition)

**原文链接**: [https://github.com/arnoldrobbins/LinuxByExample-2e](https://github.com/arnoldrobbins/LinuxByExample-2e)

生成摘要时出错

---

## 23. The Story of Marina Abramovic and Ulay (2020)

**原文标题**: The Story of Marina Abramovic and Ulay (2020)

**原文链接**: [https://www.sydney-yaeko.com/artsandculture/marina-and-ulay](https://www.sydney-yaeko.com/artsandculture/marina-and-ulay)

生成摘要时出错

---

## 24. The worst volume control UI in the world (2017)

**原文标题**: The worst volume control UI in the world (2017)

**原文链接**: [https://uxdesign.cc/the-worst-volume-control-ui-in-the-world-60713dc86950](https://uxdesign.cc/the-worst-volume-control-ui-in-the-world-60713dc86950)

生成摘要时出错

---

## 25. We rewrote our Rust WASM parser in TypeScript and it got faster

**原文标题**: We rewrote our Rust WASM parser in TypeScript and it got faster

**原文链接**: [https://www.openui.com/blog/rust-wasm-parser](https://www.openui.com/blog/rust-wasm-parser)

生成摘要时出错

---

## 26. Attention Residuals

**原文标题**: Attention Residuals

**原文链接**: [https://github.com/MoonshotAI/Attention-Residuals](https://github.com/MoonshotAI/Attention-Residuals)

生成摘要时出错

---

## 27. Padel Chess – tactical simulator for padel

**原文标题**: Padel Chess – tactical simulator for padel

**原文链接**: [https://www.padelchess.me/](https://www.padelchess.me/)

生成摘要时出错

---

## 28. Cryptography in Home Entertainment (2004)

**原文标题**: Cryptography in Home Entertainment (2004)

**原文链接**: [https://mathweb.ucsd.edu/~crypto/Projects/MarkBarry/](https://mathweb.ucsd.edu/~crypto/Projects/MarkBarry/)

生成摘要时出错

---

## 29. France's aircraft carrier located in real time by Le Monde through fitness app

**原文标题**: France's aircraft carrier located in real time by Le Monde through fitness app

**原文链接**: [https://www.lemonde.fr/en/international/article/2026/03/20/stravaleaks-france-s-aircraft-carrier-located-in-real-time-by-le-monde-through-fitness-app_6751640_4.html](https://www.lemonde.fr/en/international/article/2026/03/20/stravaleaks-france-s-aircraft-carrier-located-in-real-time-by-le-monde-through-fitness-app_6751640_4.html)

生成摘要时出错

---

## 30. Show HN: We built a terminal-only Bluesky / AT Proto client written in Fortran

**原文标题**: Show HN: We built a terminal-only Bluesky / AT Proto client written in Fortran

**原文链接**: [https://github.com/FormerLab/fortransky](https://github.com/FormerLab/fortransky)

生成摘要时出错

---

## 31. Turing Award Honors Bennett and Brassard for Quantum Information Science

**原文标题**: Turing Award Honors Bennett and Brassard for Quantum Information Science

**原文链接**: [https://amturing.acm.org](https://amturing.acm.org)

生成摘要时出错

---

## 32. Discontinuation and reinitiation of dual-labeled GLP-1 receptor agonists

**原文标题**: Discontinuation and reinitiation of dual-labeled GLP-1 receptor agonists

**原文链接**: [https://nautil.us/whiplash-heart-attack-and-stroke-risk-jumps-when-people-stop-taking-glp-1s-1279029](https://nautil.us/whiplash-heart-attack-and-stroke-risk-jumps-when-people-stop-taking-glp-1s-1279029)

生成摘要时出错

---

## 33. How HN: Ironkernel – Python expressions, Rust parallel

**原文标题**: How HN: Ironkernel – Python expressions, Rust parallel

**原文链接**: [https://github.com/YuminosukeSato/ironkernel](https://github.com/YuminosukeSato/ironkernel)

生成摘要时出错

---

## 34. VisiCalc Reconstructed

**原文标题**: VisiCalc Reconstructed

**原文链接**: [https://zserge.com/posts/visicalc/](https://zserge.com/posts/visicalc/)

生成摘要时出错

---

## 35. Just make it hard to fail

**原文标题**: Just make it hard to fail

**原文链接**: [https://nekolucifer.substack.com/p/just-make-it-really-hard-to-fail](https://nekolucifer.substack.com/p/just-make-it-really-hard-to-fail)

生成摘要时出错

---

## 36. The Ugliest Airplane: An Appreciation

**原文标题**: The Ugliest Airplane: An Appreciation

**原文链接**: [https://www.smithsonianmag.com/air-space-magazine/ugliest-airplane-appreciation-180978708/](https://www.smithsonianmag.com/air-space-magazine/ugliest-airplane-appreciation-180978708/)

生成摘要时出错

---

## 37. Jury signals tech titans on hook for social media addiction

**原文标题**: Jury signals tech titans on hook for social media addiction

**原文链接**: [https://techxplore.com/news/2026-03-jury-tech-titans-social-media.html](https://techxplore.com/news/2026-03-jury-tech-titans-social-media.html)

生成摘要时出错

---

## 38. Claude Code and the Great Productivity Panic of 2026

**原文标题**: Claude Code and the Great Productivity Panic of 2026

**原文链接**: [https://www.bloomberg.com/news/articles/2026-02-26/ai-coding-agents-like-claude-code-are-fueling-a-productivity-panic-in-tech](https://www.bloomberg.com/news/articles/2026-02-26/ai-coding-agents-like-claude-code-are-fueling-a-productivity-panic-in-tech)

生成摘要时出错

---

## 39. Lent and Lisp

**原文标题**: Lent and Lisp

**原文链接**: [https://leancrew.com/all-this/2026/02/lent-and-lisp/](https://leancrew.com/all-this/2026/02/lent-and-lisp/)

生成摘要时出错

---

## 40. ArXiv declares independence from Cornell

**原文标题**: ArXiv declares independence from Cornell

**原文链接**: [https://www.science.org/content/article/arxiv-pioneering-preprint-server-declares-independence-cornell](https://www.science.org/content/article/arxiv-pioneering-preprint-server-declares-independence-cornell)

生成摘要时出错

---

## 41. Albert's Swarm

**原文标题**: Albert's Swarm

**原文链接**: [https://en.wikipedia.org/wiki/Albert%27s_swarm](https://en.wikipedia.org/wiki/Albert%27s_swarm)

生成摘要时出错

---

## 42. Entso-E final report on Iberian 2025 blackout

**原文标题**: Entso-E final report on Iberian 2025 blackout

**原文链接**: [https://www.entsoe.eu/publications/blackout/28-april-2025-iberian-blackout/](https://www.entsoe.eu/publications/blackout/28-april-2025-iberian-blackout/)

生成摘要时出错

---

## 43. Canada moves towards homegrown rocket launches

**原文标题**: Canada moves towards homegrown rocket launches

**原文链接**: [https://www.ctvnews.ca/sci-tech/article/incredibly-important-canada-moves-towards-homegrown-rocket-launches/](https://www.ctvnews.ca/sci-tech/article/incredibly-important-canada-moves-towards-homegrown-rocket-launches/)

生成摘要时出错

---

## 44. Too Much Color

**原文标题**: Too Much Color

**原文链接**: [https://www.keithcirkel.co.uk/too-much-color/](https://www.keithcirkel.co.uk/too-much-color/)

生成摘要时出错

---

## 45. Delve – Fake Compliance as a Service

**原文标题**: Delve – Fake Compliance as a Service

**原文链接**: [https://deepdelver.substack.com/p/delve-fake-compliance-as-a-service](https://deepdelver.substack.com/p/delve-fake-compliance-as-a-service)

生成摘要时出错

---

## 46. First science from private Moon lander challenges lunar divide

**原文标题**: First science from private Moon lander challenges lunar divide

**原文链接**: [https://www.science.org/content/article/first-science-private-moon-lander-challenges-lunar-divide](https://www.science.org/content/article/first-science-private-moon-lander-challenges-lunar-divide)

生成摘要时出错

---

## 47. A Markdown textfile based Kanban board in a single HTML file

**原文标题**: A Markdown textfile based Kanban board in a single HTML file

**原文链接**: [https://github.com/chr15m/kanban-todo](https://github.com/chr15m/kanban-todo)

生成摘要时出错

---

## 48. The Social Smolnet

**原文标题**: The Social Smolnet

**原文链接**: [https://ploum.net/2026-03-20-social-smolnet.html](https://ploum.net/2026-03-20-social-smolnet.html)

生成摘要时出错

---

## 49. Our commitment to Windows quality

**原文标题**: Our commitment to Windows quality

**原文链接**: [https://blogs.windows.com/windows-insider/2026/03/20/our-commitment-to-windows-quality/](https://blogs.windows.com/windows-insider/2026/03/20/our-commitment-to-windows-quality/)

生成摘要时出错

---

## 50. Show HN: Sonar – A tiny CLI to see and kill whatever's running on localhost

**原文标题**: Show HN: Sonar – A tiny CLI to see and kill whatever's running on localhost

**原文链接**: [https://github.com/RasKrebs/sonar](https://github.com/RasKrebs/sonar)

生成摘要时出错

---

## 51. Parallel Perl – Autoparallelizing interpreter with JIT

**原文标题**: Parallel Perl – Autoparallelizing interpreter with JIT

**原文链接**: [https://perl.petamem.com/gpw2026/perl-mit-ai-gpw2026.html#/4/1/1](https://perl.petamem.com/gpw2026/perl-mit-ai-gpw2026.html#/4/1/1)

生成摘要时出错

---

## 52. Gangs of Karachi

**原文标题**: Gangs of Karachi

**原文链接**: [https://harpers.org/archive/2015/09/gangs-of-karachi/](https://harpers.org/archive/2015/09/gangs-of-karachi/)

生成摘要时出错

---

## 53. The Los Angeles Aqueduct Is Wild

**原文标题**: The Los Angeles Aqueduct Is Wild

**原文链接**: [https://practical.engineering/blog/2026/3/17/the-los-angeles-aqueduct-is-wild](https://practical.engineering/blog/2026/3/17/the-los-angeles-aqueduct-is-wild)

生成摘要时出错

---

## 54. Google details new 24-hour process to sideload unverified Android apps

**原文标题**: Google details new 24-hour process to sideload unverified Android apps

**原文链接**: [https://arstechnica.com/gadgets/2026/03/google-details-new-24-hour-process-to-sideload-unverified-android-apps/](https://arstechnica.com/gadgets/2026/03/google-details-new-24-hour-process-to-sideload-unverified-android-apps/)

生成摘要时出错

---

## 55. Astral to Join OpenAI

**原文标题**: Astral to Join OpenAI

**原文链接**: [https://astral.sh/blog/openai](https://astral.sh/blog/openai)

生成摘要时出错

---

## 56. Show HN: Red Grid Link – peer-to-peer team tracking over Bluetooth, no servers

**原文标题**: Show HN: Red Grid Link – peer-to-peer team tracking over Bluetooth, no servers

**原文链接**: [https://github.com/RedGridTactical/RedGridLink](https://github.com/RedGridTactical/RedGridLink)

生成摘要时出错

---

## 57. The Soul of a Pedicab Driver

**原文标题**: The Soul of a Pedicab Driver

**原文链接**: [https://www.sheldonbrown.com/pedicab.html](https://www.sheldonbrown.com/pedicab.html)

生成摘要时出错

---

## 58. AI Team OS – Turn Claude Code into a Self-Managing AI Team

**原文标题**: AI Team OS – Turn Claude Code into a Self-Managing AI Team

**原文链接**: [https://github.com/CronusL-1141/AI-company](https://github.com/CronusL-1141/AI-company)

生成摘要时出错

---

## 59. Drawvg Filter for FFmpeg

**原文标题**: Drawvg Filter for FFmpeg

**原文链接**: [https://ayosec.github.io/ffmpeg-drawvg/](https://ayosec.github.io/ffmpeg-drawvg/)

生成摘要时出错

---

## 60. Reboot: Rebuild civilization by reinventing lost technologies

**原文标题**: Reboot: Rebuild civilization by reinventing lost technologies

**原文链接**: [https://ksindi.com/reboot/](https://ksindi.com/reboot/)

生成摘要时出错

---

## 61. Super Micro Shares Plunge 25% After Co-Founder Charged in $2.5B Smuggling Plot

**原文标题**: Super Micro Shares Plunge 25% After Co-Founder Charged in $2.5B Smuggling Plot

**原文链接**: [https://www.forbes.com/sites/tylerroush/2026/03/20/super-micro-shares-plunge-25-after-co-founder-charged-in-25-billion-ai-chip-smuggling-plot/](https://www.forbes.com/sites/tylerroush/2026/03/20/super-micro-shares-plunge-25-after-co-founder-charged-in-25-billion-ai-chip-smuggling-plot/)

生成摘要时出错

---

## 62. Meme Buildings

**原文标题**: Meme Buildings

**原文链接**: [https://misfitsarchitecture.com/2026/03/15/meme-buildings/](https://misfitsarchitecture.com/2026/03/15/meme-buildings/)

生成摘要时出错

---

## 63. NumKong: 2'000 Mixed Precision Kernels for All

**原文标题**: NumKong: 2'000 Mixed Precision Kernels for All

**原文链接**: [https://ashvardanian.com/posts/numkong/](https://ashvardanian.com/posts/numkong/)

生成摘要时出错

---

## 64. A Portrait of the Artist as an LLM

**原文标题**: A Portrait of the Artist as an LLM

**原文链接**: [https://evernotquite.substack.com/p/a-portrait-of-the-artist-as-an-llm](https://evernotquite.substack.com/p/a-portrait-of-the-artist-as-an-llm)

生成摘要时出错

---

## 65. Heisuke Hironaka Has Died

**原文标题**: Heisuke Hironaka Has Died

**原文链接**: [https://japannews.yomiuri.co.jp/society/general-news/20260319-317449/](https://japannews.yomiuri.co.jp/society/general-news/20260319-317449/)

生成摘要时出错

---

## 66. Atuin v18.13 – better search, a PTY proxy, and AI for your shell

**原文标题**: Atuin v18.13 – better search, a PTY proxy, and AI for your shell

**原文链接**: [https://blog.atuin.sh/atuin-v18-13/](https://blog.atuin.sh/atuin-v18-13/)

生成摘要时出错

---

## 67. Java is fast, code might not be

**原文标题**: Java is fast, code might not be

**原文链接**: [https://jvogel.me/posts/2026/java-is-fast-your-code-might-not-be/](https://jvogel.me/posts/2026/java-is-fast-your-code-might-not-be/)

生成摘要时出错

---

## 68. Mayor of Paris removed parking spaces, "drastically" reduced the number of cars

**原文标题**: Mayor of Paris removed parking spaces, "drastically" reduced the number of cars

**原文链接**: [https://www.cnn.com/2026/03/21/travel/paris-transformation-anne-hidalgo-mayor](https://www.cnn.com/2026/03/21/travel/paris-transformation-anne-hidalgo-mayor)

生成摘要时出错

---

## 69. Regex Blaster

**原文标题**: Regex Blaster

**原文链接**: [https://mdp.github.io/regex-blaster/](https://mdp.github.io/regex-blaster/)

生成摘要时出错

---

## 70. Departure Mono Font

**原文标题**: Departure Mono Font

**原文链接**: [https://departuremono.com/](https://departuremono.com/)

生成摘要时出错

---

## 71. Claude dispatch: assign tasks to Claude from anywhere

**原文标题**: Claude dispatch: assign tasks to Claude from anywhere

**原文链接**: [https://support.claude.com/en/articles/13947068-assign-tasks-to-claude-from-anywhere-in-cowork](https://support.claude.com/en/articles/13947068-assign-tasks-to-claude-from-anywhere-in-cowork)

生成摘要时出错

---

## 72. Apple Announces New Mac Sales Record Following MacBook Neo Launch

**原文标题**: Apple Announces New Mac Sales Record Following MacBook Neo Launch

**原文链接**: [https://www.macrumors.com/2026/03/20/apple-shares-mac-sales-achievement/](https://www.macrumors.com/2026/03/20/apple-shares-mac-sales-achievement/)

生成摘要时出错

---

## 73. Major leap towards reanimation after death as mammal's brain preserved

**原文标题**: Major leap towards reanimation after death as mammal's brain preserved

**原文链接**: [https://www.newscientist.com/article/2520204-major-leap-towards-reanimation-after-death-as-mammals-brain-preserved/](https://www.newscientist.com/article/2520204-major-leap-towards-reanimation-after-death-as-mammals-brain-preserved/)

生成摘要时出错

---

## 74. HP trialed mandatory 15-minute support call wait times (2025)

**原文标题**: HP trialed mandatory 15-minute support call wait times (2025)

**原文链接**: [https://arstechnica.com/gadgets/2025/02/misguided-hp-customer-support-approach-included-forced-15-minute-call-wait-times/](https://arstechnica.com/gadgets/2025/02/misguided-hp-customer-support-approach-included-forced-15-minute-call-wait-times/)

生成摘要时出错

---

## 75. Work_mem: It's a Trap

**原文标题**: Work_mem: It's a Trap

**原文链接**: [https://mydbanotebook.org/posts/work_mem-its-a-trap/](https://mydbanotebook.org/posts/work_mem-its-a-trap/)

生成摘要时出错

---

## 76. Mole – Deep clean and optimize your Mac

**原文标题**: Mole – Deep clean and optimize your Mac

**原文链接**: [https://github.com/tw93/Mole](https://github.com/tw93/Mole)

生成摘要时出错

---

## 77. No Pills or Needles, Just Paper: How Deadly Drugs Are Changing

**原文标题**: No Pills or Needles, Just Paper: How Deadly Drugs Are Changing

**原文链接**: [https://www.nytimes.com/2026/03/21/world/deadly-drugs-paper.html](https://www.nytimes.com/2026/03/21/world/deadly-drugs-paper.html)

生成摘要时出错

---

## 78. I'm OK being left behind, thanks

**原文标题**: I'm OK being left behind, thanks

**原文链接**: [https://shkspr.mobi/blog/2026/03/im-ok-being-left-behind-thanks/](https://shkspr.mobi/blog/2026/03/im-ok-being-left-behind-thanks/)

生成摘要时出错

---

## 79. Show HN: Baltic shadow fleet tracker – live AIS, cable proximity alerts

**原文标题**: Show HN: Baltic shadow fleet tracker – live AIS, cable proximity alerts

**原文链接**: [https://github.com/FormerLab/shadow-fleet-tracker-light](https://github.com/FormerLab/shadow-fleet-tracker-light)

生成摘要时出错

---

## 80. purl: a curl-esque CLI for making HTTP requests that require payment

**原文标题**: purl: a curl-esque CLI for making HTTP requests that require payment

**原文链接**: [https://www.purl.dev/](https://www.purl.dev/)

生成摘要时出错

---

## 81. Why western carmakers' retreat from electric risks dooming them to irrelevance

**原文标题**: Why western carmakers' retreat from electric risks dooming them to irrelevance

**原文链接**: [https://www.theguardian.com/business/2026/mar/21/west-carmakers-retreat-electric-vehicle-risks-irrelevance-iran-war-evs-china](https://www.theguardian.com/business/2026/mar/21/west-carmakers-retreat-electric-vehicle-risks-irrelevance-iran-war-evs-china)

生成摘要时出错

---

## 82. Exploring 8 Shaft Weaving

**原文标题**: Exploring 8 Shaft Weaving

**原文链接**: [https://slab.org/2026/03/11/exploring-8-shaft-weaving/](https://slab.org/2026/03/11/exploring-8-shaft-weaving/)

生成摘要时出错

---

## 83. Afroman found not liable in defamation case

**原文标题**: Afroman found not liable in defamation case

**原文链接**: [https://nypost.com/2026/03/18/us-news/afroman-found-not-liable-in-bizarre-ohio-defamation-case/](https://nypost.com/2026/03/18/us-news/afroman-found-not-liable-in-bizarre-ohio-defamation-case/)

生成摘要时出错

---

## 84. Chuck Norris has died

**原文标题**: Chuck Norris has died

**原文链接**: [https://variety.com/2026/film/news/chuck-norris-dead-walker-texas-ranger-dies-1236694953/](https://variety.com/2026/film/news/chuck-norris-dead-walker-texas-ranger-dies-1236694953/)

生成摘要时出错

---

## 85. Show HN: I fixed FFmpeg's subtitle conversion (the bug from 2014)

**原文标题**: Show HN: I fixed FFmpeg's subtitle conversion (the bug from 2014)

**原文链接**: [https://connollydavid.github.io/pgs-release/](https://connollydavid.github.io/pgs-release/)

生成摘要时出错

---

## 86. Show HN: Three new Kitten TTS models – smallest less than 25MB

**原文标题**: Show HN: Three new Kitten TTS models – smallest less than 25MB

**原文链接**: [https://github.com/KittenML/KittenTTS](https://github.com/KittenML/KittenTTS)

生成摘要时出错

---

## 87. Windows 11's Start menu was built using React – now switching to native WinUI

**原文标题**: Windows 11's Start menu was built using React – now switching to native WinUI

**原文链接**: [https://www.windowscentral.com/microsoft/windows-11/windows-11-major-improvements-announced-movable-taskbar-less-ads-reduced-copilot-better-performance-2026](https://www.windowscentral.com/microsoft/windows-11/windows-11-major-improvements-announced-movable-taskbar-less-ads-reduced-copilot-better-performance-2026)

生成摘要时出错

---

## 88. Randomization in Controlled Experiments

**原文标题**: Randomization in Controlled Experiments

**原文链接**: [https://queue.acm.org/detail.cfm?id=3778029](https://queue.acm.org/detail.cfm?id=3778029)

生成摘要时出错

---

## 89. Drugwars for the TI-82/83/83 Calculators (2011)

**原文标题**: Drugwars for the TI-82/83/83 Calculators (2011)

**原文链接**: [https://gist.github.com/mattmanning/1002653/b7a1e88479a10eaae3bd5298b8b2c86e16fb4404](https://gist.github.com/mattmanning/1002653/b7a1e88479a10eaae3bd5298b8b2c86e16fb4404)

生成摘要时出错

---

## 90. Full Disclosure: A Third (and Fourth) Azure Sign-In Log Bypass Found

**原文标题**: Full Disclosure: A Third (and Fourth) Azure Sign-In Log Bypass Found

**原文链接**: [https://trustedsec.com/blog/full-disclosure-a-third-and-fourth-azure-sign-in-log-bypass-found](https://trustedsec.com/blog/full-disclosure-a-third-and-fourth-azure-sign-in-log-bypass-found)

生成摘要时出错

---

## 91. Flash-KMeans: Fast and Memory-Efficient Exact K-Means

**原文标题**: Flash-KMeans: Fast and Memory-Efficient Exact K-Means

**原文链接**: [https://arxiv.org/abs/2603.09229](https://arxiv.org/abs/2603.09229)

生成摘要时出错

---

## 92. AI (2014)

**原文标题**: AI (2014)

**原文链接**: [https://blog.samaltman.com/ai](https://blog.samaltman.com/ai)

生成摘要时出错

---

## 93. Zvec – A lightweight in-process vector database

**原文标题**: Zvec – A lightweight in-process vector database

**原文链接**: [https://zvec.org/en/](https://zvec.org/en/)

生成摘要时出错

---

## 94. “Your frustration is the product”

**原文标题**: “Your frustration is the product”

**原文链接**: [https://daringfireball.net/2026/03/your_frustration_is_the_product](https://daringfireball.net/2026/03/your_frustration_is_the_product)

生成摘要时出错

---

## 95. How many branches can your CPU predict?

**原文标题**: How many branches can your CPU predict?

**原文链接**: [https://lemire.me/blog/2026/03/18/how-many-branches-can-your-cpu-predict/](https://lemire.me/blog/2026/03/18/how-many-branches-can-your-cpu-predict/)

生成摘要时出错

---

## 96. Linux Page Faults, MMAP, and userfaultfd for faster VM boots

**原文标题**: Linux Page Faults, MMAP, and userfaultfd for faster VM boots

**原文链接**: [https://www.shayon.dev/post/2026/65/linux-page-faults-mmap-and-userfaultfd/](https://www.shayon.dev/post/2026/65/linux-page-faults-mmap-and-userfaultfd/)

生成摘要时出错

---

## 97. Ozempic Is About to Go Generic for Billions of People

**原文标题**: Ozempic Is About to Go Generic for Billions of People

**原文链接**: [https://www.nytimes.com/2026/03/19/health/ozempic-wegovy-generic-india-china-canada.html](https://www.nytimes.com/2026/03/19/health/ozempic-wegovy-generic-india-china-canada.html)

生成摘要时出错

---

## 98. 4Chan mocks £520k fine for UK online safety breaches

**原文标题**: 4Chan mocks £520k fine for UK online safety breaches

**原文链接**: [https://www.bbc.com/news/articles/c624330lg1ko](https://www.bbc.com/news/articles/c624330lg1ko)

生成摘要时出错

---

## 99. Waymo Safety Impact

**原文标题**: Waymo Safety Impact

**原文链接**: [https://waymo.com/safety/impact/](https://waymo.com/safety/impact/)

生成摘要时出错

---

## 100. OpenAI Plans Desktop Superapp Merging ChatGPT, Codex, and Atlas Browser

**原文标题**: OpenAI Plans Desktop Superapp Merging ChatGPT, Codex, and Atlas Browser

**原文链接**: [https://www.cnbc.com/2026/03/19/openai-desktop-super-app-chatgpt-browser-codex.html](https://www.cnbc.com/2026/03/19/openai-desktop-super-app-chatgpt-browser-codex.html)

生成摘要时出错

---

