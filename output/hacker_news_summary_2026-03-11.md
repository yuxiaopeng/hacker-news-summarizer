# Hacker News 热门文章摘要 (2026-03-11)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Faster asin() was hiding in plain sight

**原文标题**: Faster asin() was hiding in plain sight

**原文链接**: [https://16bpp.net/blog/post/faster-asin-was-hiding-in-plain-sight/](https://16bpp.net/blog/post/faster-asin-was-hiding-in-plain-sight/)

生成摘要时出错

---

## 12. Launch HN: Sentrial (YC W26) – Catch AI Agent Failures Before Your Users Do

**原文标题**: Launch HN: Sentrial (YC W26) – Catch AI Agent Failures Before Your Users Do

**原文链接**: [https://www.sentrial.com/](https://www.sentrial.com/)

生成摘要时出错

---

## 13. AI Agent Hacks McKinsey

**原文标题**: AI Agent Hacks McKinsey

**原文链接**: [https://codewall.ai/blog/how-we-hacked-mckinseys-ai-platform](https://codewall.ai/blog/how-we-hacked-mckinseys-ai-platform)

生成摘要时出错

---

## 14. Show HN: Vanilla JavaScript refinery simulator built to explain job to my kids

**原文标题**: Show HN: Vanilla JavaScript refinery simulator built to explain job to my kids

**原文链接**: [https://fuelingcuriosity.com/game.html](https://fuelingcuriosity.com/game.html)

生成摘要时出错

---

## 15. Fungal Electronics

**原文标题**: Fungal Electronics

**原文链接**: [https://arxiv.org/abs/2111.11231](https://arxiv.org/abs/2111.11231)

生成摘要时出错

---

## 16. Show HN: Open-source browser for AI agents

**原文标题**: Show HN: Open-source browser for AI agents

**原文链接**: [https://github.com/theredsix/agent-browser-protocol](https://github.com/theredsix/agent-browser-protocol)

生成摘要时出错

---

## 17. The MacBook Neo

**原文标题**: The MacBook Neo

**原文链接**: [https://daringfireball.net/2026/03/the_macbook_neo](https://daringfireball.net/2026/03/the_macbook_neo)

生成摘要时出错

---

## 18. Searching for the Agentic IDE

**原文标题**: Searching for the Agentic IDE

**原文链接**: [https://twitter.com/karpathy/status/2031616709560610993](https://twitter.com/karpathy/status/2031616709560610993)

生成摘要时出错

---

## 19. Show HN: I built an ISP infrastructure emulator from scratch with a custom vBNG

**原文标题**: Show HN: I built an ISP infrastructure emulator from scratch with a custom vBNG

**原文链接**: [https://aether.saphal.me/dashboard/default](https://aether.saphal.me/dashboard/default)

生成摘要时出错

---

## 20. Swiss e-voting pilot can't count 2,048 ballots after decryption failure

**原文标题**: Swiss e-voting pilot can't count 2,048 ballots after decryption failure

**原文链接**: [https://www.theregister.com/2026/03/11/swiss_evote_usb_snafu/](https://www.theregister.com/2026/03/11/swiss_evote_usb_snafu/)

生成摘要时出错

---

## 21. Building a TB-303 from Scratch

**原文标题**: Building a TB-303 from Scratch

**原文链接**: [https://loopmaster.xyz/tutorials/tb303-from-scratch](https://loopmaster.xyz/tutorials/tb303-from-scratch)

生成摘要时出错

---

## 22. PeppyOS: A simpler alternative to ROS 2 (now with containers support)

**原文标题**: PeppyOS: A simpler alternative to ROS 2 (now with containers support)

**原文链接**: [https://peppy.bot/](https://peppy.bot/)

生成摘要时出错

---

## 23. Zig – Type Resolution Redesign and Language Changes

**原文标题**: Zig – Type Resolution Redesign and Language Changes

**原文链接**: [https://ziglang.org/devlog/2026/#2026-03-10](https://ziglang.org/devlog/2026/#2026-03-10)

生成摘要时出错

---

## 24. Why the global elite gave up on spelling and grammar

**原文标题**: Why the global elite gave up on spelling and grammar

**原文链接**: [https://www.wsj.com/lifestyle/jeffrey-epstein-files-bad-grammar-spelling-trump-ellison-dorsey-gates-thiel-cbfe9fb1](https://www.wsj.com/lifestyle/jeffrey-epstein-files-bad-grammar-spelling-trump-ellison-dorsey-gates-thiel-cbfe9fb1)

生成摘要时出错

---

## 25. Visualizing Ukkonen's Suffix Tree Algorithm

**原文标题**: Visualizing Ukkonen's Suffix Tree Algorithm

**原文链接**: [https://www.abahgat.com/blog/visualizing-ukkonens-algorithm/](https://www.abahgat.com/blog/visualizing-ukkonens-algorithm/)

生成摘要时出错

---

## 26. Writing my own text editor, and daily-driving it

**原文标题**: Writing my own text editor, and daily-driving it

**原文链接**: [https://blog.jsbarretto.com/post/text-editor](https://blog.jsbarretto.com/post/text-editor)

生成摘要时出错

---

## 27. Cloudflare crawl endpoint

**原文标题**: Cloudflare crawl endpoint

**原文链接**: [https://developers.cloudflare.com/changelog/post/2026-03-10-br-crawl-endpoint/](https://developers.cloudflare.com/changelog/post/2026-03-10-br-crawl-endpoint/)

生成摘要时出错

---

## 28. Yann LeCun raises $1B to build AI that understands the physical world

**原文标题**: Yann LeCun raises $1B to build AI that understands the physical world

**原文链接**: [https://www.wired.com/story/yann-lecun-raises-dollar1-billion-to-build-ai-that-understands-the-physical-world/](https://www.wired.com/story/yann-lecun-raises-dollar1-billion-to-build-ai-that-understands-the-physical-world/)

生成摘要时出错

---

## 29. Tony Hoare has died

**原文标题**: Tony Hoare has died

**原文链接**: [https://blog.computationalcomplexity.org/2026/03/tony-hoare-1934-2026.html](https://blog.computationalcomplexity.org/2026/03/tony-hoare-1934-2026.html)

生成摘要时出错

---

## 30. Bypassing PatchGuard on Windows x64 (2005)

**原文标题**: Bypassing PatchGuard on Windows x64 (2005)

**原文链接**: [http://uninformed.org/index.cgi?v=3&a=3&t=txt](http://uninformed.org/index.cgi?v=3&a=3&t=txt)

生成摘要时出错

---

## 31. Whistleblower claims ex-DOGE member says he took Social Security data to new job

**原文标题**: Whistleblower claims ex-DOGE member says he took Social Security data to new job

**原文链接**: [https://www.washingtonpost.com/politics/2026/03/10/social-security-data-breach-doge-2/](https://www.washingtonpost.com/politics/2026/03/10/social-security-data-breach-doge-2/)

生成摘要时出错

---

## 32. SSH Secret Menu

**原文标题**: SSH Secret Menu

**原文链接**: [https://twitter.com/rebane2001/status/2031037389347406054](https://twitter.com/rebane2001/status/2031037389347406054)

生成摘要时出错

---

## 33. Create value for others and don’t worry about the returns

**原文标题**: Create value for others and don’t worry about the returns

**原文链接**: [https://geohot.github.io//blog/jekyll/update/2026/03/11/running-69-agents.html](https://geohot.github.io//blog/jekyll/update/2026/03/11/running-69-agents.html)

生成摘要时出错

---

## 34. U+237C ⍼ Is Azimuth

**原文标题**: U+237C ⍼ Is Azimuth

**原文链接**: [https://ionathan.ch/2026/02/16/angzarr.html](https://ionathan.ch/2026/02/16/angzarr.html)

生成摘要时出错

---

## 35. TADA: Speech generation through text-acoustic synchronization

**原文标题**: TADA: Speech generation through text-acoustic synchronization

**原文链接**: [https://www.hume.ai/blog/opensource-tada](https://www.hume.ai/blog/opensource-tada)

生成摘要时出错

---

## 36. Agents that run while I sleep

**原文标题**: Agents that run while I sleep

**原文链接**: [https://www.claudecodecamp.com/p/i-m-building-agents-that-run-while-i-sleep](https://www.claudecodecamp.com/p/i-m-building-agents-that-run-while-i-sleep)

生成摘要时出错

---

## 37. Hurricane Electric (HE.NET) IPv6 tunnelbroker page offline due to expired domain

**原文标题**: Hurricane Electric (HE.NET) IPv6 tunnelbroker page offline due to expired domain

**原文链接**: [https://tunnelbroker.net](https://tunnelbroker.net)

生成摘要时出错

---

## 38. Julia Snail – An Emacs Development Environment for Julia Like Clojure's Cider

**原文标题**: Julia Snail – An Emacs Development Environment for Julia Like Clojure's Cider

**原文链接**: [https://github.com/gcv/julia-snail](https://github.com/gcv/julia-snail)

生成摘要时出错

---

## 39. RISC-V Is Sloooow

**原文标题**: RISC-V Is Sloooow

**原文链接**: [https://marcin.juszkiewicz.com.pl/2026/03/10/risc-v-is-sloooow/](https://marcin.juszkiewicz.com.pl/2026/03/10/risc-v-is-sloooow/)

生成摘要时出错

---

## 40. Show HN: Ink – Deploy full-stack apps from AI agents via MCP or Skills

**原文标题**: Show HN: Ink – Deploy full-stack apps from AI agents via MCP or Skills

**原文链接**: [https://ml.ink/](https://ml.ink/)

生成摘要时出错

---

## 41. Let yourself fall down more

**原文标题**: Let yourself fall down more

**原文链接**: [https://ntietz.com/blog/let-yourself-fall-down-more/](https://ntietz.com/blog/let-yourself-fall-down-more/)

生成摘要时出错

---

## 42. Debian decides not to decide on AI-generated contributions

**原文标题**: Debian decides not to decide on AI-generated contributions

**原文链接**: [https://lwn.net/SubscriberLink/1061544/125f911834966dd0/](https://lwn.net/SubscriberLink/1061544/125f911834966dd0/)

生成摘要时出错

---

## 43. When the chain becomes the product: Seven years inside a token-funded venture

**原文标题**: When the chain becomes the product: Seven years inside a token-funded venture

**原文链接**: [https://markmhendrickson.com/posts/when-the-chain-becomes-the-product/](https://markmhendrickson.com/posts/when-the-chain-becomes-the-product/)

生成摘要时出错

---

## 44. Levels of Agentic Engineering

**原文标题**: Levels of Agentic Engineering

**原文链接**: [https://www.bassimeledath.com/blog/levels-of-agentic-engineering](https://www.bassimeledath.com/blog/levels-of-agentic-engineering)

生成摘要时出错

---

## 45. Roblox is minting teen millionaires

**原文标题**: Roblox is minting teen millionaires

**原文链接**: [https://www.bloomberg.com/news/articles/2026-03-06/roblox-s-teen-millionaires-are-disrupting-the-gaming-industry](https://www.bloomberg.com/news/articles/2026-03-06/roblox-s-teen-millionaires-are-disrupting-the-gaming-industry)

生成摘要时出错

---

## 46. Launch HN: RunAnywhere (YC W26) – Faster AI Inference on Apple Silicon

**原文标题**: Launch HN: RunAnywhere (YC W26) – Faster AI Inference on Apple Silicon

**原文链接**: [https://github.com/RunanywhereAI/rcli](https://github.com/RunanywhereAI/rcli)

生成摘要时出错

---

## 47. AMD Ryzen AI NPUs Are Finally Useful Under Linux for Running LLMs

**原文标题**: AMD Ryzen AI NPUs Are Finally Useful Under Linux for Running LLMs

**原文链接**: [https://www.phoronix.com/news/AMD-Ryzen-AI-NPUs-Linux-LLMs](https://www.phoronix.com/news/AMD-Ryzen-AI-NPUs-Linux-LLMs)

生成摘要时出错

---

## 48. Standardizing source maps

**原文标题**: Standardizing source maps

**原文链接**: [https://bloomberg.github.io/js-blog/post/standardizing-source-maps/](https://bloomberg.github.io/js-blog/post/standardizing-source-maps/)

生成摘要时出错

---

## 49. Universal vaccine against respiratory infections and allergens

**原文标题**: Universal vaccine against respiratory infections and allergens

**原文链接**: [https://med.stanford.edu/news/all-news/2026/02/universal-vaccine.html](https://med.stanford.edu/news/all-news/2026/02/universal-vaccine.html)

生成摘要时出错

---

## 50. GitHub Accounts Compromised

**原文标题**: GitHub Accounts Compromised

**原文链接**: [https://opensourcemalware.com/blog/polinrider-attack](https://opensourcemalware.com/blog/polinrider-attack)

生成摘要时出错

---

## 51. Mesh over Bluetooth LE, TCP, or Reticulum

**原文标题**: Mesh over Bluetooth LE, TCP, or Reticulum

**原文链接**: [https://github.com/torlando-tech/columba](https://github.com/torlando-tech/columba)

生成摘要时出错

---

## 52. FFmpeg-over-IP – Connect to remote FFmpeg servers

**原文标题**: FFmpeg-over-IP – Connect to remote FFmpeg servers

**原文链接**: [https://github.com/steelbrain/ffmpeg-over-ip](https://github.com/steelbrain/ffmpeg-over-ip)

生成摘要时出错

---

## 53. Surpassing vLLM with a Generated Inference Stack

**原文标题**: Surpassing vLLM with a Generated Inference Stack

**原文链接**: [https://infinity.inc/case-studies/qwen3-optimization](https://infinity.inc/case-studies/qwen3-optimization)

生成摘要时出错

---

## 54. Slow is smooth and smooth is fast: What software teams can learn from Navy SEALs

**原文标题**: Slow is smooth and smooth is fast: What software teams can learn from Navy SEALs

**原文链接**: [https://www.heise.de/en/blog/Slow-is-smooth-and-smooth-is-fast-What-software-teams-can-learn-from-Navy-SEALs-11200229.html](https://www.heise.de/en/blog/Slow-is-smooth-and-smooth-is-fast-What-software-teams-can-learn-from-Navy-SEALs-11200229.html)

生成摘要时出错

---

## 55. Meta acquires Moltbook

**原文标题**: Meta acquires Moltbook

**原文链接**: [https://www.axios.com/2026/03/10/meta-facebook-moltbook-agent-social-network](https://www.axios.com/2026/03/10/meta-facebook-moltbook-agent-social-network)

生成摘要时出错

---

## 56. Where did you think the training data was coming from?

**原文标题**: Where did you think the training data was coming from?

**原文链接**: [https://idiallo.com/blog/where-did-the-training-data-come-from-meta-ai-rayban-glasses](https://idiallo.com/blog/where-did-the-training-data-come-from-meta-ai-rayban-glasses)

生成摘要时出错

---

## 57. M5 MacBook Air Review: Not just more of the same–the same, but more

**原文标题**: M5 MacBook Air Review: Not just more of the same–the same, but more

**原文链接**: [https://sixcolors.com/post/2026/03/m5-macbook-air-review-not-just-more-of-the-same-the-same-but-more/](https://sixcolors.com/post/2026/03/m5-macbook-air-review-not-just-more-of-the-same-the-same-but-more/)

生成摘要时出错

---

## 58. Pike: To Exit or Not to Exit

**原文标题**: Pike: To Exit or Not to Exit

**原文链接**: [https://tomjohnell.com/pike-solving-the-should-we-stop-here-or-gamble-on-the-next-exit-problem/](https://tomjohnell.com/pike-solving-the-should-we-stop-here-or-gamble-on-the-next-exit-problem/)

生成摘要时出错

---

## 59. Exploring the ocean with Raspberry Pi–powered marine robots

**原文标题**: Exploring the ocean with Raspberry Pi–powered marine robots

**原文链接**: [https://www.raspberrypi.com/news/exploring-the-ocean-with-raspberry-pi-powered-marine-robots/](https://www.raspberrypi.com/news/exploring-the-ocean-with-raspberry-pi-powered-marine-robots/)

生成摘要时出错

---

## 60. We are building data breach machines and nobody cares

**原文标题**: We are building data breach machines and nobody cares

**原文链接**: [https://idealloc.me/posts/we-are-building-data-breach-machines-and-nobody-cares/](https://idealloc.me/posts/we-are-building-data-breach-machines-and-nobody-cares/)

生成摘要时出错

---

## 61. AutoKernel: Autoresearch for GPU Kernels

**原文标题**: AutoKernel: Autoresearch for GPU Kernels

**原文链接**: [https://github.com/RightNow-AI/autokernel](https://github.com/RightNow-AI/autokernel)

生成摘要时出错

---

## 62. Invoker Commands API

**原文标题**: Invoker Commands API

**原文链接**: [https://developer.mozilla.org/en-US/docs/Web/API/Invoker_Commands_API](https://developer.mozilla.org/en-US/docs/Web/API/Invoker_Commands_API)

生成摘要时出错

---

## 63. Mother of All Grease Fires (1994)

**原文标题**: Mother of All Grease Fires (1994)

**原文链接**: [https://milk.com/wall-o-shame/bucket.html](https://milk.com/wall-o-shame/bucket.html)

生成摘要时出错

---

## 64. Open Weights isn't Open Training

**原文标题**: Open Weights isn't Open Training

**原文链接**: [https://www.workshoplabs.ai/blog/open-weights-open-training](https://www.workshoplabs.ai/blog/open-weights-open-training)

生成摘要时出错

---

## 65. Support for Aquantia AQC113 and AQC113C Ethernet Controllers on FreeBSD

**原文标题**: Support for Aquantia AQC113 and AQC113C Ethernet Controllers on FreeBSD

**原文链接**: [https://github.com/Aquantia/aqtion-freebsd/issues/32](https://github.com/Aquantia/aqtion-freebsd/issues/32)

生成摘要时出错

---

## 66. After outages, Amazon to make senior engineers sign off on AI-assisted changes

**原文标题**: After outages, Amazon to make senior engineers sign off on AI-assisted changes

**原文链接**: [https://arstechnica.com/ai/2026/03/after-outages-amazon-to-make-senior-engineers-sign-off-on-ai-assisted-changes/](https://arstechnica.com/ai/2026/03/after-outages-amazon-to-make-senior-engineers-sign-off-on-ai-assisted-changes/)

生成摘要时出错

---

## 67. EQT eyes potential $6B sale of Linux pioneer SUSE, sources say

**原文标题**: EQT eyes potential $6B sale of Linux pioneer SUSE, sources say

**原文链接**: [https://www.reuters.com/business/eqt-eyes-potential-6-billion-sale-linux-pioneer-suse-sources-say-2026-03-09](https://www.reuters.com/business/eqt-eyes-potential-6-billion-sale-linux-pioneer-suse-sources-say-2026-03-09)

生成摘要时出错

---

## 68. Bippy: React Internals Toolkit

**原文标题**: Bippy: React Internals Toolkit

**原文链接**: [https://www.bippy.dev/](https://www.bippy.dev/)

生成摘要时出错

---

## 69. I built a programming language using Claude Code

**原文标题**: I built a programming language using Claude Code

**原文链接**: [https://ankursethi.com/blog/programming-language-claude-code/](https://ankursethi.com/blog/programming-language-claude-code/)

生成摘要时出错

---

## 70. Throwing away 18 months of code and starting over

**原文标题**: Throwing away 18 months of code and starting over

**原文链接**: [https://tompiagg.io/posts/we-threw-away-1-5-years-of-code](https://tompiagg.io/posts/we-threw-away-1-5-years-of-code)

生成摘要时出错

---

## 71. Redox OS has adopted a Certificate of Origin policy and a strict no-LLM policy

**原文标题**: Redox OS has adopted a Certificate of Origin policy and a strict no-LLM policy

**原文链接**: [https://gitlab.redox-os.org/redox-os/redox/-/blob/master/CONTRIBUTING.md](https://gitlab.redox-os.org/redox-os/redox/-/blob/master/CONTRIBUTING.md)

生成摘要时出错

---

## 72. I used pulsar detection techniques to turn a phone into a watch timegrapher

**原文标题**: I used pulsar detection techniques to turn a phone into a watch timegrapher

**原文链接**: [https://www.chronolog.watch/timegrapher](https://www.chronolog.watch/timegrapher)

生成摘要时出错

---

## 73. Scientists revive activity in frozen mouse brains for the first time

**原文标题**: Scientists revive activity in frozen mouse brains for the first time

**原文链接**: [https://www.nature.com/articles/d41586-026-00756-w](https://www.nature.com/articles/d41586-026-00756-w)

生成摘要时出错

---

## 74. No, it doesn't cost Anthropic $5k per Claude Code user

**原文标题**: No, it doesn't cost Anthropic $5k per Claude Code user

**原文链接**: [https://martinalderson.com/posts/no-it-doesnt-cost-anthropic-5k-per-claude-code-user/](https://martinalderson.com/posts/no-it-doesnt-cost-anthropic-5k-per-claude-code-user/)

生成摘要时出错

---

## 75. JPMorgan marking down loan portfolios of private credit groups

**原文标题**: JPMorgan marking down loan portfolios of private credit groups

**原文链接**: [https://www.ft.com/content/389a0003-d8de-4afd-9de9-be6e9fc6888c](https://www.ft.com/content/389a0003-d8de-4afd-9de9-be6e9fc6888c)

生成摘要时出错

---

## 76. PgAdmin 4 9.13 with AI Assistant Panel

**原文标题**: PgAdmin 4 9.13 with AI Assistant Panel

**原文链接**: [https://www.pgadmin.org/docs/pgadmin4/9.13/query_tool.html#ai-assistant-panel](https://www.pgadmin.org/docs/pgadmin4/9.13/query_tool.html#ai-assistant-panel)

生成摘要时出错

---

## 77. The Browser Becomes Your WordPress

**原文标题**: The Browser Becomes Your WordPress

**原文链接**: [https://wordpress.org/news/2026/03/announcing-my-wordpress/](https://wordpress.org/news/2026/03/announcing-my-wordpress/)

生成摘要时出错

---

## 78. LoGeR – 3D reconstruction from extremely long videos (DeepMind, UC Berkeley)

**原文标题**: LoGeR – 3D reconstruction from extremely long videos (DeepMind, UC Berkeley)

**原文链接**: [https://loger-project.github.io](https://loger-project.github.io)

生成摘要时出错

---

## 79. Billion-Parameter Theories

**原文标题**: Billion-Parameter Theories

**原文链接**: [https://www.worldgov.org/complexity.html](https://www.worldgov.org/complexity.html)

生成摘要时出错

---

## 80. Lotus 1-2-3 on the PC with DOS

**原文标题**: Lotus 1-2-3 on the PC with DOS

**原文链接**: [https://stonetools.ghost.io/lotus123-dos/](https://stonetools.ghost.io/lotus123-dos/)

生成摘要时出错

---

## 81. I put my whole life into a single database

**原文标题**: I put my whole life into a single database

**原文链接**: [https://howisfelix.today/](https://howisfelix.today/)

生成摘要时出错

---

## 82. HyperCard discovery: Neuromancer, Count Zero, Mona Lisa Overdrive (2022)

**原文标题**: HyperCard discovery: Neuromancer, Count Zero, Mona Lisa Overdrive (2022)

**原文链接**: [https://macintoshgarden.org/apps/neuromancer-count-zero-mona-lisa-overdrive](https://macintoshgarden.org/apps/neuromancer-count-zero-mona-lisa-overdrive)

生成摘要时出错

---

## 83. Defeat as Method

**原文标题**: Defeat as Method

**原文链接**: [https://www.cabinetmagazine.org/issues/71/khosravi.php](https://www.cabinetmagazine.org/issues/71/khosravi.php)

生成摘要时出错

---

## 84. I'm going to build my own OpenClaw, with blackjack and bun

**原文标题**: I'm going to build my own OpenClaw, with blackjack and bun

**原文链接**: [https://github.com/rcarmo/piclaw](https://github.com/rcarmo/piclaw)

生成摘要时出错

---

## 85. UK MPs give ministers powers to restrict Internet for under 18s

**原文标题**: UK MPs give ministers powers to restrict Internet for under 18s

**原文链接**: [https://www.openrightsgroup.org/press-releases/mps-give-ministers-powers-to-restrict-entire-internet/](https://www.openrightsgroup.org/press-releases/mps-give-ministers-powers-to-restrict-entire-internet/)

生成摘要时出错

---

## 86. Online age-verification tools for child safety are surveilling adults

**原文标题**: Online age-verification tools for child safety are surveilling adults

**原文链接**: [https://www.cnbc.com/2026/03/08/social-media-child-safety-internet-ai-surveillance.html](https://www.cnbc.com/2026/03/08/social-media-child-safety-internet-ai-surveillance.html)

生成摘要时出错

---

## 87. Intel Demos Chip to Compute with Encrypted Data

**原文标题**: Intel Demos Chip to Compute with Encrypted Data

**原文链接**: [https://spectrum.ieee.org/fhe-intel](https://spectrum.ieee.org/fhe-intel)

生成摘要时出错

---

## 88. Practical Guide to Bare Metal C++

**原文标题**: Practical Guide to Bare Metal C++

**原文链接**: [https://arobenko.github.io/bare_metal_cpp/#_abstract_classes](https://arobenko.github.io/bare_metal_cpp/#_abstract_classes)

生成摘要时出错

---

## 89. The Gervais Principle, or the Office According to “The Office” (2009)

**原文标题**: The Gervais Principle, or the Office According to “The Office” (2009)

**原文链接**: [https://www.ribbonfarm.com/2009/10/07/the-gervais-principle-or-the-office-according-to-the-office/](https://www.ribbonfarm.com/2009/10/07/the-gervais-principle-or-the-office-according-to-the-office/)

生成摘要时出错

---

## 90. Ig Nobel award ceremony moving to Zurich due to concern over U.S. travel visas

**原文标题**: Ig Nobel award ceremony moving to Zurich due to concern over U.S. travel visas

**原文链接**: [https://www.swissinfo.ch/eng/research-frontiers/ig-nobels-to-move-awards-to-switzerland-due-to-concern-over-us-travel-visas/91073250](https://www.swissinfo.ch/eng/research-frontiers/ig-nobels-to-move-awards-to-switzerland-due-to-concern-over-us-travel-visas/91073250)

生成摘要时出错

---

## 91. RFC 454545 – Human Em Dash Standard

**原文标题**: RFC 454545 – Human Em Dash Standard

**原文链接**: [https://gist.github.com/bignimbus/a75cc9d703abf0b21a57c0d21a79e2be](https://gist.github.com/bignimbus/a75cc9d703abf0b21a57c0d21a79e2be)

生成摘要时出错

---

## 92. Ichi-go ichi-e

**原文标题**: Ichi-go ichi-e

**原文链接**: [https://en.wikipedia.org/wiki/Ichi-go_ichi-e](https://en.wikipedia.org/wiki/Ichi-go_ichi-e)

生成摘要时出错

---

## 93. Show HN: How I topped the HuggingFace open LLM leaderboard on two gaming GPUs

**原文标题**: Show HN: How I topped the HuggingFace open LLM leaderboard on two gaming GPUs

**原文链接**: [https://dnhkng.github.io/posts/rys/](https://dnhkng.github.io/posts/rys/)

生成摘要时出错

---

## 94. Revolut wins UK banking licence after five-year tussle

**原文标题**: Revolut wins UK banking licence after five-year tussle

**原文链接**: [https://sifted.eu/articles/revolut-uk-banking-licence-granted](https://sifted.eu/articles/revolut-uk-banking-licence-granted)

生成摘要时出错

---

## 95. Revise age verification terms for MidnightBSD

**原文标题**: Revise age verification terms for MidnightBSD

**原文链接**: [https://github.com/MidnightBSD/src/commit/529b708846e30e8eb4fcec8dfc23176ec6a74bcf](https://github.com/MidnightBSD/src/commit/529b708846e30e8eb4fcec8dfc23176ec6a74bcf)

生成摘要时出错

---

## 96. Optimizing Top K in Postgres

**原文标题**: Optimizing Top K in Postgres

**原文链接**: [https://www.paradedb.com/blog/optimizing-top-k](https://www.paradedb.com/blog/optimizing-top-k)

生成摘要时出错

---

## 97. Upcoming Vote on Chat Control: Renew Deal Is Worse Than Rejected Draft Report

**原文标题**: Upcoming Vote on Chat Control: Renew Deal Is Worse Than Rejected Draft Report

**原文链接**: [https://www.patrick-breyer.de/en/upcoming-vote-on-chat-control-new-sd-epp-and-renew-deal-is-worse-than-rejected-draft-report-ai-text-scanning-and-mass-surveillance-set-to-continue/](https://www.patrick-breyer.de/en/upcoming-vote-on-chat-control-new-sd-epp-and-renew-deal-is-worse-than-rejected-draft-report-ai-text-scanning-and-mass-surveillance-set-to-continue/)

生成摘要时出错

---

## 98. 1kB Club

**原文标题**: 1kB Club

**原文链接**: [https://1kb.club/](https://1kb.club/)

生成摘要时出错

---

## 99. Caxlsx: Ruby gem for xlsx generation with charts, images, schema validation

**原文标题**: Caxlsx: Ruby gem for xlsx generation with charts, images, schema validation

**原文链接**: [https://github.com/caxlsx/caxlsx](https://github.com/caxlsx/caxlsx)

生成摘要时出错

---

## 100. Rebasing in Magit

**原文标题**: Rebasing in Magit

**原文链接**: [https://entropicthoughts.com/rebasing-in-magit](https://entropicthoughts.com/rebasing-in-magit)

生成摘要时出错

---

