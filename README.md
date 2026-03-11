# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-03-11.md)

*最后自动更新时间: 2026-03-11 18:15:39*
## 1. Temporal：历时九年的 JavaScript 时间修复之旅

**原文标题**: Temporal: A nine-year journey to fix time in JavaScript

**原文链接**: [https://bloomberg.github.io/js-blog/post/temporal/](https://bloomberg.github.io/js-blog/post/temporal/)

在本文中，Jason Williams 详细阐述了 Temporal 这一新 JavaScript API 为期九年的标准化历程。该 API 旨在修复原始 `Date` 对象长期存在的缺陷。

传统的 `Date` API 是 1995 年对 Java 实现的仓促移植，由于其可变性（mutability）、不一致的月份运算以及模糊的解析方式，数十年来一直困扰着开发者。虽然 Moment.js 等库最初解决了这些问题，但由于必须自带时区和本地化数据，它们带来了显著的包体积和性能开销。

Temporal 由 TC39 推进开发，彭博社（Bloomberg）、Igalia、微软和谷歌深度参与，提供了一种现代化的、**不可变（immutable）**的解决方案。与单一类型的 `Date` 不同，Temporal 提供了一系列专门的类型来处理不同的使用场景：

*   **Temporal.ZonedDateTime**：一种综合类型，用于处理具有完整时区、历法和夏令时（DST）准确性的精确时刻。
*   **Temporal.Instant**：表示一个与时区无关的精确时刻，具有纳秒级精度（相较于 `Date` 的毫秒级精度有所提升）。
*   **无时区类型（PlainDate、PlainTime 等）**：表示“挂钟时间”，即不含时区的值，适用于不希望受夏令时转换干扰的日历或时钟计算。

该提案标志着 JavaScript 开始转向对国际历法的一流支持和强大的时区处理。Temporal 从 2017 年的阶段 1（Stage 1）发展到如今即将完成标准化，代表了多方大规模协作的成果，旨在为 JavaScript 提供现代全球化应用所需的高精度、可靠的时间处理能力。

---

## 2. 促成大规模科研造假的实体：规模庞大、适应力强且在不断增长 (2025)

**原文标题**: Entities enabling scientific fraud at scale are large, resilient, growing (2025)

**原文链接**: [https://doi.org/10.1073/pnas.2420092122](https://doi.org/10.1073/pnas.2420092122)

本文发表于《美国国家科学院院刊》（PNAS），探讨了“论文工厂”令人警觉的演变过程——这些商业实体专门制造并销售虚假的科研手稿以供发表。作者指出，科研不端行为已从孤立的个人失信行为，演变为一种以史无前例的规模运作的、复杂且工业化的造假体系。

该研究强调了几个关键进展：

*   **规模与增长：** 论文工厂已演变成大规模的营利性业务，每年产出数千篇伪造论文。虽然最初集中在生命科学和医学领域，但目前正迅速向其他学科扩张。
*   **技术韧性：** 这些实体具有极强的适应性。随着出版商加强对抄袭或图片篡改的审查，论文工厂转而利用生成式人工智能和先进的数据造假技术来规避检测。这种韧性使得传统的“打地鼠”式监管手段日益失效。
*   **系统性驱动因素：** 该行业的主要诱因是全球性的“不出版便出局”文化。在许多地区，职称晋升、医学学位和政府资助与论文发表数量直接挂钩，催生了一个由急于购买作者署名的“客户”组成的庞大市场。
*   **后果：** 这种“规模化造假”污染了全球科学记录，误导科研人员，浪费公共资金。当虚假的临床数据被纳入荟萃分析或医学指南时，还会对公众健康构成重大风险。

作者得出结论，单靠技术方案和软件检测不足以解决问题。他们主张从根本上转变学术评价方式——弱化对论文数量的重视——并呼吁出版商、大学和监管机构开展国际协作，共同瓦解使这些顽固实体得以生存的经济诱因。

---

## 3. 使 WebAssembly 成为 Web 上的一等语言

**原文标题**: Making WebAssembly a first-class language on the Web

**原文链接**: [https://hacks.mozilla.org/2026/02/making-webassembly-a-first-class-language-on-the-web/](https://hacks.mozilla.org/2026/02/making-webassembly-a-first-class-language-on-the-web/)

自 2017 年问世以来，WebAssembly (Wasm) 经历了显著的发展，引入了 SIMD、垃圾回收 (GC) 和尾调用等特性。然而，本文认为 Wasm 在 Web 领域仍处于“二等公民”地位，因为它缺乏 JavaScript 所享有的那种无缝平台集成。

核心问题在于 Wasm 在两个关键功能上对 JavaScript 的依赖：
1.  **代码加载：** 与 JavaScript 简单的 script 标签不同，Wasm 需要复杂的 JS API 调用来获取并实例化模块。
2.  **访问 Web API：** Wasm 无法直接调用 Web API（如 DOM 或 `console.log`）。它必须依赖“胶水代码”——即在两种环境之间转换和重新编码数据的 JavaScript 封装层。

这种依赖带来了重重障碍。由于 JS 与 Wasm 转换产生的额外开销，这造成了“性能税”；基准测试表明，移除这些胶水代码可将 DOM 操作速度提升 45%。此外，它还导致了陡峭的学习曲线，开发者即使使用 Rust 或 C++ 语言，也必须处理“抽象泄漏”并掌握 JavaScript。因此，标准编译器通常缺乏内置的 Web 支持，迫使开发者依赖非官方的、特定语言的工具链。

为了解决这些问题，作者倡导采用 **WebAssembly 组件模型 (Component Model)**。这一标准提案引入了自包含的高级构件，用于处理加载、链接，以及最关键的——无需 JavaScript 中介即可直接访问 Web API。通过转向直接内置于浏览器的标准化接口，组件模型旨在消除对 JS 胶水代码的需求，简化开发体验，并最终确立 WebAssembly 作为 Web 平台一等公民语言的地位。

---

## 4. 众人见“弦”，她却见分形构成的时空。

**原文标题**: Where Some See Strings, She Sees a Space-Time Made of Fractals

**原文链接**: [https://www.quantamagazine.org/where-some-see-strings-she-sees-a-space-time-made-of-fractals-20260311/](https://www.quantamagazine.org/where-some-see-strings-she-sees-a-space-time-made-of-fractals-20260311/)

在本文中，海德堡大学的物理学家 Astrid Eichhorn 讨论了“渐近安全性”（asymptotic safety），这是一种量子引力理论，认为物理定律在极微观尺度下并不会失效。

弦理论或圈量子引力论等理论认为宇宙是由基本的弦或离散的时空“原子”组成的，相比之下，渐近安全性是一种更为保守的方法。该理论假设在普朗克尺度下，宇宙会达到一个“不动点”，届时基本相互作用的强度趋于稳定。在此阶段，宇宙变得具有“尺度对称性”，即呈现出一种类似分形的结构，无论如何进一步放大，物理规则都保持不变。

Eichhorn 的研究重点是“引力-物质系统”，旨在计算时空的量子涨落如何与已知粒子相互作用。通过使用一种被称为“重整化”的数学“显微镜”，她的团队成功地得出了“追溯预测”——即通过假设微观层面存在不动点，计算出宏观世界的已知数值。最值得注意的是，这种方法解释了希格斯玻色子的质量以及顶夸克与底夸克之间的特定质量差异。

该理论还为通过暗物质研究验证其有效性提供了途径。Eichhorn 指出，几种主流的暗物质候选者，如某些弱相互作用大质量粒子（WIMPs）和轴子，似乎与渐近安全性的“分形世界”不兼容。如果这些粒子被发现，将挑战该理论；如果没有被发现，则会为其提供进一步的间接证据。最终，渐近安全性表明，标准的量子场论或许足以解释引力和时空，而无需转向更奇异的“弦”结构。

---

## 5. BitNet：适用于本地 CPU 的 1000 亿参数 1 比特模型

**原文标题**: BitNet: 100B Param 1-Bit model for local CPUs

**原文链接**: [https://github.com/microsoft/BitNet](https://github.com/microsoft/BitNet)

**bitnet.cpp** 是专为 1-bit 大语言模型（LLM）（如 BitNet b1.58）设计的官方推理框架。它提供优化的内核，可在 CPU 和 GPU 上实现快速、无损的推理，并计划在未来支持 NPU。

该框架相比传统模型实现了显著的性能和效率提升。在 ARM CPU 上，其加速比高达 5.07 倍，能耗降低多达 70%。在 x86 架构上，性能提升高达 6.17 倍，节能效果达 82.2%。该框架的一个里程碑式成就是能够**在单台本地 CPU 上以人类阅读速度（每秒 5–7 个 token）运行 100B 参数的 BitNet b1.58 模型**。

技术上，`bitnet.cpp` 基于 `llama.cpp` 框架构建，并融合了来自 T-MAC 的查找表（lookup table）方法。最近的优化包括并行内核实现、可配置分块（tiling）以及嵌入量化，从而带来了额外的 1.15 倍至 2.1 倍加速。

该框架支持 Hugging Face 上的多款 1-bit 模型，包括：
*   **BitNet b1.58 变体**（0.7B、2B 和 3B）
*   **Llama3-8B-1.58**
*   **Falcon3 和 Falcon-E 系列**（1B–10B）

安装环境要求 Python 3.9+、CMake 和 Clang 18。该仓库为用户提供了简化的工作流，包括克隆代码、通过 Conda 配置环境、下载 GGUF 模型，以及使用提供的 Python 脚本运行推理或基准测试。通过支持在标准本地硬件上运行超大规模参数模型，`bitnet.cpp` 极大地拓展了边缘 AI 的应用潜力。

---

## 6. Wiz加入谷歌

**原文标题**: Wiz joins Google

**原文链接**: [https://www.wiz.io/blog/google-closes-deal-to-acquire-wiz](https://www.wiz.io/blog/google-closes-deal-to-acquire-wiz)

Wiz 已正式加入谷歌，完成了旨在将 Wiz 的云安全创新与谷歌的规模优势相结合的收购。公告强调，尽管公司的使命依然是保护组织构建和运行的一切，但发展重点已演变为应对快速的“AI 速度”。

转型及过去一年的主要亮点包括：

*   **AI 驱动的安全：** Wiz 优先考虑能够促进而非阻碍创新的安全。近期扩展的产品包括 Wiz AI 安全平台、用于自动化风险修复的 AI 安全代理，以及提供经过加固且几乎零 CVE 的容器基础镜像的 WizOS。
*   **研究里程碑：** 在过去的一年中，Wiz Research 发现了多个严重漏洞，例如 RediShell（Redis 中存在 13 年之久的缺陷）、NVIDIAScape（针对 AI 基础设施）以及 CodeBreach（AWS 中的供应链风险）。
*   **持续的多云支持：** 尽管已成为谷歌旗下的公司，Wiz 仍致力于其多云基因。它将继续支持并保护 AWS、Azure、GCP 和 OCI 上的工作负载，服务于包括财富 100 强和主要 AI 研究实验室在内的客户群。
*   **与谷歌生态系统的整合：** 展望未来，Wiz 将利用 Google Cloud 的基础设施、Mandiant 的威胁情报以及 Gemini AI 来增强其产品路线图，并为安全团队提供先进的能力。

公告最后强调，与谷歌的合作加强了而非收窄了 Wiz 的关注重点。通过双方联手，公司旨在以现代 AI 发展的速度，提供从代码到云的主动、统一的风险视角。

---

## 7. Show HN: Klaus – OpenClaw on a VM, batteries included

**原文标题**: Show HN: Klaus – OpenClaw on a VM, batteries included

**原文链接**: [https://klausai.com/](https://klausai.com/)

**Klaus** is a deployment platform designed to simplify the hosting of AI assistants, specifically those utilizing the **OpenClaw** framework. Featured as a "Show HN" project, it provides a "batteries-included" solution for developers looking to run AI agents that can interact with computer interfaces.

The core value of Klaus lies in its use of **Virtual Machines (VMs)**. By hosting the AI assistant within a dedicated VM, the platform offers several key benefits:

*   **Ease of Deployment:** It removes the technical friction of manual configuration, providing a ready-to-use environment for OpenClaw.
*   **Security and Isolation:** Running the agent in a VM ensures that the AI operates in a sandboxed environment. This protects the user's primary system from any unintended actions taken by the autonomous agent during "computer use" tasks.
*   **Stability:** The pre-configured stack ensures that all dependencies are managed, offering a consistent environment for the AI to function.

In summary, Klaus serves as a turnkey infrastructure for those experimenting with autonomous AI agents. It bridges the gap between complex AI frameworks and practical, secure execution, allowing users to get their assistants up and running quickly without worrying about underlying infrastructure or system safety.

---

## 8. Elevated errors on login with Claude Code

**原文标题**: Elevated errors on login with Claude Code

**原文链接**: [https://status.claude.com/incidents/jm3b4jjy2jrt](https://status.claude.com/incidents/jm3b4jjy2jrt)

生成摘要时出错

---

## 9. Lego's 0.002mm specification and its implications for manufacturing (2025)

**原文标题**: Lego's 0.002mm specification and its implications for manufacturing (2025)

**原文链接**: [https://www.thewave.engineer/articles.html/productivity/legos-0002mm-specification-and-its-implications-for-manufacturing-r120/](https://www.thewave.engineer/articles.html/productivity/legos-0002mm-specification-and-its-implications-for-manufacturing-r120/)

生成摘要时出错

---

## 10. Launch HN: Prism (YC X25) – Workspace and API to generate and edit videos

**原文标题**: Launch HN: Prism (YC X25) – Workspace and API to generate and edit videos

**原文链接**: [https://www.prismvideos.com](https://www.prismvideos.com)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 2 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 3 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 4 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 5 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 6 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 7 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 8 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 9 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 10 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 11 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 12 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 13 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 14 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 15 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 16 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 17 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 18 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 19 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 20 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 21 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 22 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 23 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 24 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 25 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 26 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 27 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 28 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 29 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 30 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 31 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 32 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 33 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 34 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 35 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 36 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 37 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 38 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 39 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 40 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 41 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 42 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 43 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 44 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 45 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 46 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 47 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 48 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 49 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 50 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 51 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 52 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 53 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 54 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 55 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 56 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 57 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 58 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 59 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 60 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 61 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 62 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 63 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 64 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 65 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 66 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 67 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 68 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 69 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 70 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 71 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 72 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 73 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 74 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 75 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 76 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 77 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 78 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 79 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 80 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 81 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 82 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 83 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 84 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 85 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 86 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 87 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 88 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 89 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 90 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 91 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 92 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 93 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 94 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 95 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 96 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 97 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 98 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 99 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 100 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 101 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 102 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 103 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 104 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 105 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 106 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 107 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 108 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 109 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 110 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 111 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 112 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 113 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 114 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 115 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 116 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 117 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 118 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 119 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 120 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 121 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 122 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 123 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 124 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 125 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 126 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 127 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 128 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 129 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 130 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 131 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 132 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 133 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 134 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 135 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 136 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 137 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 138 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 139 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 140 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 141 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 142 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 143 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 144 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 145 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 146 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 147 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 148 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 149 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 150 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 151 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 152 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 153 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 154 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 155 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 156 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 157 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 158 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 159 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 160 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 161 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 162 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 163 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 164 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 165 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 166 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 167 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 168 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 169 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 170 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 171 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 172 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 173 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 174 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 175 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 176 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 177 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 178 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 179 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 180 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 181 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 182 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 183 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 184 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 185 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 186 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 187 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 188 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 189 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 190 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 191 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 192 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 193 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 194 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 195 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 196 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 197 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 198 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 199 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 200 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 201 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 202 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 203 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 204 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 205 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 206 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 207 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 208 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 209 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 210 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 211 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 212 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 213 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 214 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 215 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 216 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 217 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 218 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 219 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 220 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 221 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 222 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 223 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 224 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 225 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 226 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 227 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 228 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 229 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 230 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 231 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 232 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 233 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 234 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 235 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 236 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 237 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 238 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 239 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 240 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 241 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 242 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 243 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 244 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 245 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 246 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 247 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 248 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 249 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 250 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 251 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 252 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 253 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 254 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 255 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 256 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 257 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 258 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 259 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 260 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 261 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 262 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 263 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 264 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 265 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 266 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 267 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 268 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 269 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 270 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 271 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 272 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 273 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 274 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 275 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 276 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 277 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 278 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 279 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 280 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 281 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 282 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 283 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 284 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 285 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 286 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 287 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 288 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 289 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 290 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 291 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 292 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 293 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 294 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 295 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 296 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 297 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 298 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 299 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 300 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 301 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 302 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 303 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 304 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 305 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 306 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 307 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 308 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 309 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 310 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 311 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 312 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 313 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 314 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 315 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 316 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 317 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 318 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 319 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 320 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 321 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 322 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 323 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 324 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 325 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 326 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 327 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 328 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 329 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 330 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 331 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 332 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 333 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 334 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 335 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 336 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 337 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 338 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 339 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 340 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 341 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 342 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 343 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 344 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 345 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 346 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 347 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 348 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 349 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 350 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 351 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 352 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 353 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 354 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 355 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 356 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
