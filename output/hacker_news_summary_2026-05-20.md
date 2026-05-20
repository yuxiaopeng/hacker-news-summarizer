# Hacker News 热门文章摘要 (2026-05-20)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 事件报告：2026年5月19日 – GCP 账户停用

**原文标题**: Incident Report: May 19, 2026 – GCP Account Suspension

**原文链接**: [https://blog.railway.com/p/incident-report-may-19-2026-gcp-account-outage](https://blog.railway.com/p/incident-report-may-19-2026-gcp-account-outage)

2026年5月19日，由于谷歌云平台（GCP）错误地停用了 Railway 的生产账号，Railway 经历了约 8 小时的全平台故障。此次自动停用立即导致 Railway 的控制面板、API 以及托管在 GCP 上的计算基础设施失效。

故障随后波及到托管在 Railway Metal 和 AWS 上的工作负载。虽然这些环境最初保持在线，但它们依赖于托管在 GCP 的控制平面进行网络路由。当本地路由缓存失效后，边缘代理无法解析地址，导致 Railway 在所有区域的所有工作负载均无法访问。

**时间线与恢复：**
*   **22:19 UTC：** 确定根源为 GCP 账号被停用。
*   **22:29 UTC：** 账号访问权限恢复，但所有基础设施仍处于离线状态。
*   **01:38 UTC：** 网络和边缘流量恢复。
*   **04:00 UTC：** 确认 API、控制面板及 OAuth 恢复运行。
*   **07:58 UTC：** 事件完全解决。

在恢复期间，Railway 面临着次生挑战，包括海量部署任务积压以及 GitHub 的速率限制，后者导致登录和构建功能暂时受阻。

**预防措施：**
Railway 对导致单点供应商故障引发全站停机的架构依赖负全部责任。为防止此类事件再次发生，他们正在实施以下变更：
1.  **消除单一依赖：** 将工作负载的可发现性与 GCP 托管的控制平面解耦，构建即使在单一供应商故障时也能运作的“真网格（true mesh）”架构。
2.  **多云数据库仲裁：** 将数据库分片扩展至 AWS 和 Metal，以确保在整个云供应商下线时具备故障转移能力和持久性。
3.  **重新设计数据平面：** 将 GCP 从数据平面的“热路径”中移除，仅将其作为次要或备用容量，以确保独立于供应商的架构弹性。

Railway 强调了其对系统可用性的承诺，并表示未来的架构将确保核心服务不再依赖任何单一平台。

---

## 2. OpenAI 模型证伪了离散几何中的一个核心猜想。

**原文标题**: An OpenAI model has disproved a central conjecture in discrete geometry

**原文链接**: [https://openai.com/index/model-disproves-discrete-geometry-conjecture/](https://openai.com/index/model-disproves-discrete-geometry-conjecture/)

OpenAI 宣布在数学领域取得重大突破，一个通用推理模型自主推翻了离散几何中一个长期存在的猜想。该问题被称为**平面单位距离问题**（planar unit distance problem），最早由保罗·埃尔德什（Paul Erdős）于 1946 年提出，旨在求解 $n$ 个点的集合中，距离恰好为一个单位的点对的最大数量。

80 年来，数学界普遍认为其最优增长率约为 $n^{1+o(1)}$。然而，OpenAI 的模型构造了一个无穷反例族，实现了 $n^{1+\delta}$ 的多项式级别改进。虽然模型最初的证明给出的 $\delta$ 是非显式的，但数学家威尔·萨温（Will Sawin）随后的进一步完善确定了其值为 **$\delta = 0.014$**。

这一发现因以下几点原因而备受瞩目：
*   **自主推理：** 证明是由一个通用模型生成的，而非专门针对数学训练或特定搜索的模型。
*   **跨学科创新：** 模型通过应用代数数论中的高级工具（具体为无穷类域塔和 Golod–Shafarevich 理论）解决了一个初等几何问题——这种关联令专家们感到震惊。
*   **专家验证：** 包括菲尔兹奖得主蒂姆·高尔斯（Tim Gowers）和诺加·阿隆（Noga Alon）在内的知名数学家验证了该证明。阿隆称其为“卓越的成就”，高尔斯则将其描述为“AI 数学领域的里程碑”。

这一里程碑标志着 AI 首次自主解决了数学子领域的一个核心开放问题。OpenAI 表示，这证明了先进模型有能力作为具备“独创见解”的研究伙伴，预示着 AI 未来将在生物学、物理学和工程学等领域的复杂研究中做出贡献。

---

## 3. 每秒 N 个 token 到底有多快？

**原文标题**: How fast is N tokens per second really?

**原文链接**: [https://mikeveerman.github.io/tokenspeed/](https://mikeveerman.github.io/tokenspeed/)

本文探讨了难以直观理解大语言模型（LLM）性能评估中常用的“每秒 Token 数”（tok/s）基准测试的问题。虽然硬件测评中经常出现 47 tok/s 或 500 tok/s 等标准数据，但在缺乏直接参照的情况下，用户很难想象其实际速度。

为了弥补这一差距，作者提供了一个包含四种内容模式的可视化工具：
*   **代码：** 带有语法高亮的伪代码。
*   **文本：** 标准散文（乱数假文）。
*   **思考：** 推理式输出（灰色斜体）与代码交替显示。
*   **代理：** 包含工具调用和代码生成，并伴有间歇性的处理停顿。

文章将常见的硬件和服务划分为不同的速度等级，以帮助用户理解实际的使用体验：
*   **5 tok/s：** 运行在树莓派等低功耗硬件上的本地模型。
*   **60 tok/s：** GPT-4 或 Claude 等托管模型的典型性能。
*   **200 tok/s：** Groq 等高速服务商。
*   **800 tok/s：** Cerebras 等超高速硬件，其速度已超过了人类的阅读极限。

一个核心观点是，模型的**感知速度**会因内容类型而显著不同。代码的 Token 密度比散文更高；因此，即使 tok/s 速率相同，模型在编写脚本和创作故事时的体感速度也大不相同。作者指出，对于英文散文，30 tok/s 约等于每秒 23 个单词（平均每个单词 1.3 个 Token）。该工具最终旨在揭示技术基准测试的客观数据与人类主观感知之间的差距。

---

## 4. Qwen3.7-Max：智能体前沿

**原文标题**: Qwen3.7-Max: The Agent Frontier

**原文链接**: [https://qwen.ai/blog?id=qwen3.7](https://qwen.ai/blog?id=qwen3.7)

所提供的内容仅包含“Qwen”一词，不足以生成文章的完整摘要。

然而，根据标题**“Qwen3.7-Max: The Agent Frontier（Qwen3.7-Max：智能体前沿）”**，本文可能讨论了以下要点：

*   **AI 智能体的进化：** 重点在于从简单的文本生成转向“智能体”能力——即模型可以自主规划、使用工具并执行多步任务，以解决复杂问题。
*   **“Max”级别的性能：** 由于“Max”版本通常代表 Qwen 系列中最强大的迭代，文章可能强调了其在推理、编程和数学能力方面的突破，足以媲美 GPT-4o 或 Claude 3.5 等其他顶级模型。
*   **下一代前沿：** 将 Qwen3.7 定位为下一代 AI 的领导者，特别是探讨模型如何与外部环境和 API 交互，从而成为功能性助手，而非仅仅是聊天机器人。

**如果您打算提供全文，请粘贴文本，我将很乐意为您提供详细摘要。**

---

## 5. 为什么 Inkwell 审核卡住了？

**原文标题**: Why is Inkwell stuck in review

**原文链接**: [https://www.manton.org/2026/05/19/why-is-inkwell-stuck-in.html](https://www.manton.org/2026/05/19/why-is-inkwell-stuck-in.html)

Manton Reece 的 iOS 应用 Inkwell 自 4 月 21 日起就一直陷于苹果的 App Store 审核流程中，期间经历了多次拒绝、技术调整以及一次正式申诉。Reece 概述了他在应对苹果《App Store 审核指南》时面临的几项具体障碍：

*   **安全与隐私 (1.2 & 5.1.1)：** 尽管 Inkwell 只是 Micro.blog 的一款 RSS 辅助应用，但苹果仍要求其添加内容举报、用户屏蔽和账号注销功能。
*   **技术与设计 (2.1 & 4)：** 该应用因“通过 Apple 登录”的漏洞及通用设计问题遭到拒绝，导致 Reece 最终禁用了某些登录功能。
*   **盈利模式 (3.1)：** 为了避开苹果的应用内购买佣金，Reece 删除了应用的发布功能和外部链接。他还将该应用限制在美国区商店上架，以利用 *Epic 诉苹果案* 裁决后的规则，将 Inkwell 定位为“阅读器”或“辅助”类应用。
*   **商标纠纷 (5.2.5)：** 主要症结在于“Inkwell”这个名称。苹果声称它侵犯了其 2002 年一项手写识别功能的商标。Reece 则辩称，根据美国专利及商标局 (USPTO) 的记录，该商标已正式“失效”，且商店中还存在许多其他名为“Inkwell”的应用。

Reece 对苹果在 iOS 分发上的绝对控制权表示沮丧，并指出 Inkwell 的安卓版本在一个月前就已通过谷歌审核。他认为苹果坚持使用一个已失效的商标属于权力扩张，超出了法律的必要范畴。目前，他正在等待应用审核委员会的回应。

---

## 6. GitHub 确认 3800 个仓库因恶意 VSCode 扩展遭到入侵。

**原文标题**: GitHub confirms breach of 3,800 repos via malicious VSCode extension

**原文链接**: [https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/](https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/)

GitHub 确认，因一名员工安装了恶意的 VS Code 扩展程序，导致约 3,800 个内部代码库受到安全漏洞影响。在检测到入侵后，GitHub 已从 VS Code 市场中移除了该木马化插件，隔离了受影响的设备，并启动了事件响应程序。

该公司的调查目前显示，数据泄露仅限于 GitHub 内部代码库，没有证据表明存储在其他位置的客户数据受到影响。

黑客组织 TeamPCP 声称对此次攻击负责，并在一家网络犯罪论坛上发帖称其持有约 4,000 个私有代码库。该组织为这些失窃数据索价至少 5 万美元，并威胁称若无人购买将免费公开。TeamPCP 曾多次针对 NPM、PyPI 和 Docker 等开发者平台发起高调的供应链攻击，近期还开展了针对 OpenAI 员工的攻击活动。

此次事件凸显了 VS Code 市场中“中毒”插件日益增多的趋势。近年来，多款恶意扩展程序（部分安装量达数百万次）被用于窃取凭据、加密货币挖矿及数据窃取。尽管 GitHub 规模庞大，服务于 1.8 亿名开发者和 90% 的财富 100 强企业，但此次泄露事件再次强调了开发者环境在复杂的供应链攻击面前依然存在脆弱性。

---

## 7. SBCL：终极汇编代码面包板 (2014)

**原文标题**: SBCL: the ultimate assembly code breadboard (2014)

**原文链接**: [https://pvk.ca/Blog/2014/03/15/sbcl-the-ultimate-assembly-code-breadboard/](https://pvk.ca/Blog/2014/03/15/sbcl-the-ultimate-assembly-code-breadboard/)

This article explores the implementation of a high-performance, stack-based virtual machine (VM) using SBCL (Steel Bank Common Lisp) as a "breadboard" for assembly code experimentation. Inspired by the x87 floating-point unit and Chuck Moore’s F18 processor, the author proposes an optimization technique for VMs with small, fixed-size stacks (in this case, 8 slots).

**Key Technical Concepts:**
*   **Register-Based Stack Rotation:** Rather than moving data between registers or memory during push and pop operations, the VM maps the stack to eight physical CPU registers (R8–R15). It uses a modular counter to track the Top of Stack (TOS).
*   **Primitive Specialization:** To avoid the overhead of indexing registers at runtime, the author generates eight specialized versions of every VM primitive—one for each possible value of the stack pointer. 
*   **Efficient Dispatch:** The VM uses a direct-threaded model. Specialized primitives are stored at regular intervals (4288 bytes apart). The dispatch sequence (`NEXT`) calculates the jump address by combining a base address, the instruction offset, and the variant offset determined by the current stack pointer.
*   **SBCL as a Toolchain:** The author leverages SBCL’s internal assembler (`sb-assem`) and VM-definition tools (`sb-vm`) to programmatically emit machine code. This allows for rapid iteration and the use of Lisp to handle the repetitive task of generating multiple versions of each opcode.

**Implementation Details:**
The article provides Lisp code for basic primitives like `swap`, `dup`, `add`, and `sub`, as well as control-flow instructions like `jmp`, `call`, and `ret`. Finally, it demonstrates how to interface the VM with Common Lisp using a VOP (Virtual Operation) to handle the transition, including "entering" the VM by copying data from a Lisp buffer into the dedicated registers.

---

## 8. Saying Goodbye to Asm.js

**原文标题**: Saying Goodbye to Asm.js

**原文链接**: [https://spidermonkey.dev/blog/2026/05/20/saying-goodbye-to-asmjs.html](https://spidermonkey.dev/blog/2026/05/20/saying-goodbye-to-asmjs.html)

生成摘要时出错

---

## 9. Sharla Boehm, the programmer whose code underpins the Internet

**原文标题**: Sharla Boehm, the programmer whose code underpins the Internet

**原文链接**: [https://www.scientificamerican.com/article/the-programmer-whose-code-underpins-the-internet/](https://www.scientificamerican.com/article/the-programmer-whose-code-underpins-the-internet/)

生成摘要时出错

---

## 10. Tracking Starbucks' 'widely recyclable' cups: none ended up at recycling

**原文标题**: Tracking Starbucks' 'widely recyclable' cups: none ended up at recycling

**原文链接**: [https://www.beyondplastics.org/press-releases/starbucks-cups-recyclable-report](https://www.beyondplastics.org/press-releases/starbucks-cups-recyclable-report)

生成摘要时出错

---

## 11. Map of Metal

**原文标题**: Map of Metal

**原文链接**: [https://mapofmetal.com/](https://mapofmetal.com/)

生成摘要时出错

---

## 12. Apparently Google hates us now

**原文标题**: Apparently Google hates us now

**原文链接**: [https://twitter.com/pokemoncentral/status/2057123807404638250](https://twitter.com/pokemoncentral/status/2057123807404638250)

生成摘要时出错

---

## 13. Google's AI is being manipulated. The search giant is quietly fighting back

**原文标题**: Google's AI is being manipulated. The search giant is quietly fighting back

**原文链接**: [https://www.bbc.com/future/article/20260519-google-tackles-attempts-to-hack-its-ai-results](https://www.bbc.com/future/article/20260519-google-tackles-attempts-to-hack-its-ai-results)

生成摘要时出错

---

## 14. Meta blocks human rights accounts from reaching audiences in Saudi Arabia, UAE

**原文标题**: Meta blocks human rights accounts from reaching audiences in Saudi Arabia, UAE

**原文链接**: [https://www.alqst.org/ar/posts/1190](https://www.alqst.org/ar/posts/1190)

生成摘要时出错

---

## 15. Flipper One Tech Specs

**原文标题**: Flipper One Tech Specs

**原文链接**: [https://docs.flipper.net/one/general/tech-specs](https://docs.flipper.net/one/general/tech-specs)

生成摘要时出错

---

## 16. Qian Xuesen: The missile genius America lost and China gained (2025)

**原文标题**: Qian Xuesen: The missile genius America lost and China gained (2025)

**原文链接**: [https://www.usni.org/magazines/naval-history/2025/december/missile-genius-america-lost-and-china-gained](https://www.usni.org/magazines/naval-history/2025/december/missile-genius-america-lost-and-china-gained)

生成摘要时出错

---

## 17. Everything in C is undefined behavior

**原文标题**: Everything in C is undefined behavior

**原文链接**: [https://blog.habets.se/2026/05/Everything-in-C-is-undefined-behavior.html](https://blog.habets.se/2026/05/Everything-in-C-is-undefined-behavior.html)

生成摘要时出错

---

## 18. Testing distributed systems with AI agents

**原文标题**: Testing distributed systems with AI agents

**原文链接**: [https://github.com/shenli/distributed-system-testing](https://github.com/shenli/distributed-system-testing)

生成摘要时出错

---

## 19. Formal Verification Gates for AI Coding Loops

**原文标题**: Formal Verification Gates for AI Coding Loops

**原文链接**: [https://reubenbrooks.dev/blog/structural-backpressure-beats-smarter-agents/](https://reubenbrooks.dev/blog/structural-backpressure-beats-smarter-agents/)

生成摘要时出错

---

## 20. Stable Audio 3

**原文标题**: Stable Audio 3

**原文链接**: [https://arxiv.org/abs/2605.17991](https://arxiv.org/abs/2605.17991)

生成摘要时出错

---

## 21. Node.js 26.0.0 (Now with Temporal)

**原文标题**: Node.js 26.0.0 (Now with Temporal)

**原文链接**: [https://nodejs.org/en/blog/release/v26.0.0](https://nodejs.org/en/blog/release/v26.0.0)

生成摘要时出错

---

## 22. Handling the great code forge fragmentation

**原文标题**: Handling the great code forge fragmentation

**原文链接**: [https://www.alexselimov.com/posts/forge_fragmentation/](https://www.alexselimov.com/posts/forge_fragmentation/)

生成摘要时出错

---

## 23. LoRA and Weight Decay (2023)

**原文标题**: LoRA and Weight Decay (2023)

**原文链接**: [https://irhum.github.io/blog/lorawd/](https://irhum.github.io/blog/lorawd/)

生成摘要时出错

---

## 24. Tennessee man jailed 37 days for Trump meme wins settlement after lawsuit

**原文标题**: Tennessee man jailed 37 days for Trump meme wins settlement after lawsuit

**原文链接**: [https://www.fire.org/news/victory-tennessee-man-jailed-37-days-trump-meme-wins-835000-settlement-after-first-amendment](https://www.fire.org/news/victory-tennessee-man-jailed-37-days-trump-meme-wins-835000-settlement-after-first-amendment)

生成摘要时出错

---

## 25. When Fast Fourier Transform Meets Transformer for Image Restoration (2024)

**原文标题**: When Fast Fourier Transform Meets Transformer for Image Restoration (2024)

**原文链接**: [https://github.com/deng-ai-lab/SFHformer](https://github.com/deng-ai-lab/SFHformer)

生成摘要时出错

---

## 26. Show HN: Lance – image/video generation and understanding in one model

**原文标题**: Show HN: Lance – image/video generation and understanding in one model

**原文链接**: [https://github.com/bytedance/Lance](https://github.com/bytedance/Lance)

生成摘要时出错

---

## 27. Show HN: Hocuspocus 4 – self-hosted Yjs collaboration backend

**原文标题**: Show HN: Hocuspocus 4 – self-hosted Yjs collaboration backend

**原文链接**: [https://github.com/ueberdosis/hocuspocus](https://github.com/ueberdosis/hocuspocus)

生成摘要时出错

---

## 28. Japan is gripped by mass allergies. A 1950s project is to blame

**原文标题**: Japan is gripped by mass allergies. A 1950s project is to blame

**原文链接**: [https://www.bbc.com/future/article/20260515-the-1950s-blunder-which-causes-mass-hay-fever-in-japan](https://www.bbc.com/future/article/20260515-the-1950s-blunder-which-causes-mass-hay-fever-in-japan)

生成摘要时出错

---

## 29. Autoregressive next token prediction and KV Cache in transformers

**原文标题**: Autoregressive next token prediction and KV Cache in transformers

**原文链接**: [https://medium.com/advanced-deep-learning/autoregressive-next-token-prediction-kv-cache-in-transformers-afad22285baf](https://medium.com/advanced-deep-learning/autoregressive-next-token-prediction-kv-cache-in-transformers-afad22285baf)

生成摘要时出错

---

## 30. Smartmedia Card Spec Opened, available free (2000)

**原文标题**: Smartmedia Card Spec Opened, available free (2000)

**原文链接**: [https://www.edn.com/smartmedia-card-interface-spec-opened-available-for-free/#google_vignette](https://www.edn.com/smartmedia-card-interface-spec-opened-available-for-free/#google_vignette)

生成摘要时出错

---

## 31. Goodbye Visa and Mastercard: 130M Europeans switching to sovereign payment

**原文标题**: Goodbye Visa and Mastercard: 130M Europeans switching to sovereign payment

**原文链接**: [https://www.lesnumeriques.com/banque-en-ligne/adieu-visa-et-mastercard-130-millions-d-europeens-basculent-vers-un-paiement-100-souverain-des-2026-n250918.html](https://www.lesnumeriques.com/banque-en-ligne/adieu-visa-et-mastercard-130-millions-d-europeens-basculent-vers-un-paiement-100-souverain-des-2026-n250918.html)

生成摘要时出错

---

## 32. Hormuz closure could trigger 'agrifood shock', price crisis within a year

**原文标题**: Hormuz closure could trigger 'agrifood shock', price crisis within a year

**原文链接**: [https://www.reuters.com/world/middle-east/hormuz-closure-could-trigger-agrifood-shock-price-crisis-within-year-fao-warns-2026-05-20/](https://www.reuters.com/world/middle-east/hormuz-closure-could-trigger-agrifood-shock-price-crisis-within-year-fao-warns-2026-05-20/)

生成摘要时出错

---

## 33. Anna's Archive hit with $19.5M default judgment and global domain takedown order

**原文标题**: Anna's Archive hit with $19.5M default judgment and global domain takedown order

**原文链接**: [https://torrentfreak.com/annas-archive-hit-with-19-5m-default-judgment-and-global-domain-takedown-order/](https://torrentfreak.com/annas-archive-hit-with-19-5m-default-judgment-and-global-domain-takedown-order/)

生成摘要时出错

---

## 34. No way to parse integers in C (2022)

**原文标题**: No way to parse integers in C (2022)

**原文链接**: [https://blog.habets.se/2022/10/No-way-to-parse-integers-in-C.html](https://blog.habets.se/2022/10/No-way-to-parse-integers-in-C.html)

生成摘要时出错

---

## 35. Infomaniak transitions to a foundation model to protect user data privacy

**原文标题**: Infomaniak transitions to a foundation model to protect user data privacy

**原文链接**: [https://news.infomaniak.com/en/infomaniak-foundation-sovereign-cloud/](https://news.infomaniak.com/en/infomaniak-foundation-sovereign-cloud/)

生成摘要时出错

---

## 36. Cooling copper plates could slash data center energy use by 90%

**原文标题**: Cooling copper plates could slash data center energy use by 90%

**原文链接**: [https://newatlas.com/energy/cooling-copper-plates-data-center-energy-use/](https://newatlas.com/energy/cooling-copper-plates-data-center-energy-use/)

生成摘要时出错

---

## 37. Gemini 3.5 Flash

**原文标题**: Gemini 3.5 Flash

**原文链接**: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)

生成摘要时出错

---

## 38. FiveThirtyEight articles on the Internet Archive

**原文标题**: FiveThirtyEight articles on the Internet Archive

**原文链接**: [https://fivethirtyeightindex.com/](https://fivethirtyeightindex.com/)

生成摘要时出错

---

## 39. WordPress 7.0

**原文标题**: WordPress 7.0

**原文链接**: [https://wordpress.org/news/2026/05/armstrong/](https://wordpress.org/news/2026/05/armstrong/)

生成摘要时出错

---

## 40. I’ve built a virtual museum with nearly every operating system you can think of

**原文标题**: I’ve built a virtual museum with nearly every operating system you can think of

**原文链接**: [https://virtualosmuseum.org/](https://virtualosmuseum.org/)

生成摘要时出错

---

## 41. GitHub is investigating unauthorized access to their internal repositories

**原文标题**: GitHub is investigating unauthorized access to their internal repositories

**原文链接**: [https://twitter.com/github/status/2056884788179726685](https://twitter.com/github/status/2056884788179726685)

生成摘要时出错

---

## 42. After Town Bans Flock, Councilmember Crashes Out, Proposes Internet, Phone Ban

**原文标题**: After Town Bans Flock, Councilmember Crashes Out, Proposes Internet, Phone Ban

**原文链接**: [https://www.404media.co/after-town-bans-flock-councilmember-crashes-out-proposes-internet-and-phone-ban/](https://www.404media.co/after-town-bans-flock-councilmember-crashes-out-proposes-internet-and-phone-ban/)

生成摘要时出错

---

## 43. CopyFail: From Pod to Host

**原文标题**: CopyFail: From Pod to Host

**原文链接**: [https://xint.io/blog/copy-fail-pod-to-host](https://xint.io/blog/copy-fail-pod-to-host)

生成摘要时出错

---

## 44. RISC-V and Floating-Point

**原文标题**: RISC-V and Floating-Point

**原文链接**: [https://fprox.substack.com/p/risc-v-and-floating-point](https://fprox.substack.com/p/risc-v-and-floating-point)

生成摘要时出错

---

## 45. OpenAI Is Preparing to File for an IPO in the Coming Days or Weeks

**原文标题**: OpenAI Is Preparing to File for an IPO in the Coming Days or Weeks

**原文链接**: [https://www.wsj.com/tech/ai/openai-ipo-filing-date-0ec95af5](https://www.wsj.com/tech/ai/openai-ipo-filing-date-0ec95af5)

生成摘要时出错

---

## 46. Simulated Evolution on the PICO-8

**原文标题**: Simulated Evolution on the PICO-8

**原文链接**: [https://bumbershootsoft.wordpress.com/2026/05/16/simulated-evolution-on-the-pico-8/](https://bumbershootsoft.wordpress.com/2026/05/16/simulated-evolution-on-the-pico-8/)

生成摘要时出错

---

## 47. What Do Unions Do?

**原文标题**: What Do Unions Do?

**原文链接**: [https://nicholasdecker.substack.com/p/what-do-unions-do](https://nicholasdecker.substack.com/p/what-do-unions-do)

生成摘要时出错

---

## 48. Former Cuban president Raúl Castro indicted in US over fatal downing of 2 planes

**原文标题**: Former Cuban president Raúl Castro indicted in US over fatal downing of 2 planes

**原文链接**: [https://www.bbc.com/news/live/czr24nr681gt](https://www.bbc.com/news/live/czr24nr681gt)

生成摘要时出错

---

## 49. In 1979 engineer Hugh Padgham discovered "gated reverb" – by accident

**原文标题**: In 1979 engineer Hugh Padgham discovered "gated reverb" – by accident

**原文链接**: [https://producelikeapro.com/blog/how-one-recording-mistake-created-a-musical-phenomenon-in-the-80s/](https://producelikeapro.com/blog/how-one-recording-mistake-created-a-musical-phenomenon-in-the-80s/)

生成摘要时出错

---

## 50. What You Will Lose When You Retire – By Dan Haylett

**原文标题**: What You Will Lose When You Retire – By Dan Haylett

**原文链接**: [https://danhaylett.substack.com/p/what-you-will-lose-when-you-retire](https://danhaylett.substack.com/p/what-you-will-lose-when-you-retire)

生成摘要时出错

---

## 51. Show HN: Forge – Guardrails take an 8B model from 53% to 99% on agentic tasks

**原文标题**: Show HN: Forge – Guardrails take an 8B model from 53% to 99% on agentic tasks

**原文链接**: [https://github.com/antoinezambelli/forge](https://github.com/antoinezambelli/forge)

生成摘要时出错

---

## 52. The Mercury logic programming system

**原文标题**: The Mercury logic programming system

**原文链接**: [https://github.com/Mercury-Language/mercury](https://github.com/Mercury-Language/mercury)

生成摘要时出错

---

## 53. Lisp in Web-Based Applications (2001)

**原文标题**: Lisp in Web-Based Applications (2001)

**原文链接**: [https://sep.turbifycdn.com/ty/cdn/paulgraham/bbnexcerpts.txt](https://sep.turbifycdn.com/ty/cdn/paulgraham/bbnexcerpts.txt)

生成摘要时出错

---

## 54. Google changes its search box

**原文标题**: Google changes its search box

**原文链接**: [https://blog.google/products-and-platforms/products/search/search-io-2026/](https://blog.google/products-and-platforms/products/search/search-io-2026/)

生成摘要时出错

---

## 55. C++26: More Function Wrappers

**原文标题**: C++26: More Function Wrappers

**原文链接**: [https://www.sandordargo.com/blog/2026/05/20/cpp26-copyable-function](https://www.sandordargo.com/blog/2026/05/20/cpp26-copyable-function)

生成摘要时出错

---

## 56. Learnings from 100K lines of Rust with AI (2025)

**原文标题**: Learnings from 100K lines of Rust with AI (2025)

**原文链接**: [https://zfhuang99.github.io/rust/claude%20code/codex/contracts/spec-driven%20development/2025/12/01/rust-with-ai.html](https://zfhuang99.github.io/rust/claude%20code/codex/contracts/spec-driven%20development/2025/12/01/rust-with-ai.html)

生成摘要时出错

---

## 57. Google I/O 2026 had nothing to say and said it badly ahead of Apple's WWDC

**原文标题**: Google I/O 2026 had nothing to say and said it badly ahead of Apple's WWDC

**原文链接**: [https://appleinsider.com/articles/26/05/20/google-io-2026-had-nothing-to-say-and-said-it-badly-ahead-of-apples-wwdc](https://appleinsider.com/articles/26/05/20/google-io-2026-had-nothing-to-say-and-said-it-badly-ahead-of-apples-wwdc)

生成摘要时出错

---

## 58. Gemini CLI will stop working from June 18, 2026

**原文标题**: Gemini CLI will stop working from June 18, 2026

**原文链接**: [https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)

生成摘要时出错

---

## 59. Remove-AI-Watermarks – CLI and library for removing AI watermarks from images

**原文标题**: Remove-AI-Watermarks – CLI and library for removing AI watermarks from images

**原文链接**: [https://github.com/wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks)

生成摘要时出错

---

## 60. The Invention of Buses

**原文标题**: The Invention of Buses

**原文链接**: [https://worksinprogress.co/issue/the-invention-of-buses/](https://worksinprogress.co/issue/the-invention-of-buses/)

生成摘要时出错

---

## 61. Apple unveils new accessibility features

**原文标题**: Apple unveils new accessibility features

**原文链接**: [https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/](https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/)

生成摘要时出错

---

## 62. Why I don’t vibe code

**原文标题**: Why I don’t vibe code

**原文链接**: [https://jacobharr.is/personal/i-dont-vibe-code](https://jacobharr.is/personal/i-dont-vibe-code)

生成摘要时出错

---

## 63. Copy Fail, Dirty Frag, and Fragnesia kernel vulnerabilities

**原文标题**: Copy Fail, Dirty Frag, and Fragnesia kernel vulnerabilities

**原文链接**: [https://www.gentoo.org/news/2026/05/19/copy-fail-fragnesia-vulnerabilities.html](https://www.gentoo.org/news/2026/05/19/copy-fail-fragnesia-vulnerabilities.html)

生成摘要时出错

---

## 64. Intro to TLA+ for the LLM Era: Prompt Your Way to Victory

**原文标题**: Intro to TLA+ for the LLM Era: Prompt Your Way to Victory

**原文链接**: [https://emptysqua.re/blog/intro-to-tla-plus-for-the-llm-era/](https://emptysqua.re/blog/intro-to-tla-plus-for-the-llm-era/)

生成摘要时出错

---

## 65. HTML-in-Canvas Demos

**原文标题**: HTML-in-Canvas Demos

**原文链接**: [https://github.com/GoogleChromeLabs/css-web-ui-demos/blob/main/html-in-canvas/awesome-html-in-canvas.md](https://github.com/GoogleChromeLabs/css-web-ui-demos/blob/main/html-in-canvas/awesome-html-in-canvas.md)

生成摘要时出错

---

## 66. Mistral AI acquires Emmi AI

**原文标题**: Mistral AI acquires Emmi AI

**原文链接**: [https://www.emmi.ai/news/mistral-ai-acquires-emmi-ai](https://www.emmi.ai/news/mistral-ai-acquires-emmi-ai)

生成摘要时出错

---

## 67. Hanoi’s humble beer glass and the memory of a nation

**原文标题**: Hanoi’s humble beer glass and the memory of a nation

**原文链接**: [https://sundaylongread.com/2026/05/15/hanois-humble-beer-glass-and-the-memory-of-a-nation/](https://sundaylongread.com/2026/05/15/hanois-humble-beer-glass-and-the-memory-of-a-nation/)

生成摘要时出错

---

## 68. Nobody understands the point of hybrid cars [video]

**原文标题**: Nobody understands the point of hybrid cars [video]

**原文链接**: [https://www.youtube.com/watch?v=KnUFH5GX_fI](https://www.youtube.com/watch?v=KnUFH5GX_fI)

生成摘要时出错

---

## 69. OpenAI Adopts Google's SynthID Watermark for AI Images with Verification Tool

**原文标题**: OpenAI Adopts Google's SynthID Watermark for AI Images with Verification Tool

**原文链接**: [https://openai.com/index/advancing-content-provenance/](https://openai.com/index/advancing-content-provenance/)

生成摘要时出错

---

## 70. Russian Troops' Fear Grows as Ukraine AI "Slaughterbot" Drones Headhunt Them

**原文标题**: Russian Troops' Fear Grows as Ukraine AI "Slaughterbot" Drones Headhunt Them

**原文链接**: [http://www.thelowdownblog.com/2026/05/russian-troops-fear-grows-as-ukraine-ai.html](http://www.thelowdownblog.com/2026/05/russian-troops-fear-grows-as-ukraine-ai.html)

生成摘要时出错

---

## 71. The TTY Demystified (2008)

**原文标题**: The TTY Demystified (2008)

**原文链接**: [https://www.linusakesson.net/programming/tty/index.php](https://www.linusakesson.net/programming/tty/index.php)

生成摘要时出错

---

## 72. The two oldest printing presses

**原文标题**: The two oldest printing presses

**原文链接**: [https://museumplantinmoretus.be/en/worlds-two-oldest-printing-presses](https://museumplantinmoretus.be/en/worlds-two-oldest-printing-presses)

生成摘要时出错

---

## 73. Nostalgic Kits Central (2024)

**原文标题**: Nostalgic Kits Central (2024)

**原文链接**: [https://www.nostalgickitscentral.com/](https://www.nostalgickitscentral.com/)

生成摘要时出错

---

## 74. Tool mapping 90 companies in the photonics and CPO supply chain

**原文标题**: Tool mapping 90 companies in the photonics and CPO supply chain

**原文链接**: [https://leonardo-boquillon.com/photonic-cop-supply-chain](https://leonardo-boquillon.com/photonic-cop-supply-chain)

生成摘要时出错

---

## 75. Wi-Wi Is Wireless Time Sync at 1 Nanosecond

**原文标题**: Wi-Wi Is Wireless Time Sync at 1 Nanosecond

**原文链接**: [https://www.jeffgeerling.com/blog/2026/wi-wi-is-wireless-time-sync-less-than-5ns/](https://www.jeffgeerling.com/blog/2026/wi-wi-is-wireless-time-sync-less-than-5ns/)

生成摘要时出错

---

## 76. Show HN: Superlog (YC P26) – Observability that installs itself and fixes bugs

**原文标题**: Show HN: Superlog (YC P26) – Observability that installs itself and fixes bugs

**原文链接**: [https://superlog.sh/](https://superlog.sh/)

生成摘要时出错

---

## 77. Disney erased FiveThirtyEight

**原文标题**: Disney erased FiveThirtyEight

**原文链接**: [https://www.natesilver.net/p/disney-erased-fivethirtyeight](https://www.natesilver.net/p/disney-erased-fivethirtyeight)

生成摘要时出错

---

## 78. Polypad

**原文标题**: Polypad

**原文链接**: [https://polypad.amplify.com/](https://polypad.amplify.com/)

生成摘要时出错

---

## 79. Use a VPN, Says Canadian Government That Wants VPN Logs

**原文标题**: Use a VPN, Says Canadian Government That Wants VPN Logs

**原文链接**: [https://reclaimthenet.org/canada-vpn-companies-threaten-to-leave-over-bill-c-22](https://reclaimthenet.org/canada-vpn-companies-threaten-to-leave-over-bill-c-22)

生成摘要时出错

---

## 80. Museum of Imaginary Musical Instruments

**原文标题**: Museum of Imaginary Musical Instruments

**原文链接**: [https://imaginaryinstruments.org/](https://imaginaryinstruments.org/)

生成摘要时出错

---

## 81. Show HN: Gaussian Splat of a Strawberry

**原文标题**: Show HN: Gaussian Splat of a Strawberry

**原文链接**: [https://superspl.at/scene/84df8849](https://superspl.at/scene/84df8849)

生成摘要时出错

---

## 82. CISA Admin Leaked AWS GovCloud Keys on GitHub

**原文标题**: CISA Admin Leaked AWS GovCloud Keys on GitHub

**原文链接**: [https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/)

生成摘要时出错

---

## 83. Nobody Cares, Write Anyway

**原文标题**: Nobody Cares, Write Anyway

**原文链接**: [https://blog.absurdpirate.com/nobody-cares-write-anyway/](https://blog.absurdpirate.com/nobody-cares-write-anyway/)

生成摘要时出错

---

## 84. Show HN: Open-Source Agentic QA Harness with Memory

**原文标题**: Show HN: Open-Source Agentic QA Harness with Memory

**原文链接**: [https://vostride.com/agent-qa](https://vostride.com/agent-qa)

生成摘要时出错

---

## 85. Kv4p HT – A homebrew 1W radio (VHF or UHF) that plugs into an Android phone

**原文标题**: Kv4p HT – A homebrew 1W radio (VHF or UHF) that plugs into an Android phone

**原文链接**: [https://www.kv4p.com/](https://www.kv4p.com/)

生成摘要时出错

---

## 86. Deutsche Bahn blocks Linux users

**原文标题**: Deutsche Bahn blocks Linux users

**原文链接**: [https://www.heise.de/en/news/Deutsche-Bahn-No-information-under-Linux-11300847.html](https://www.heise.de/en/news/Deutsche-Bahn-No-information-under-Linux-11300847.html)

生成摘要时出错

---

## 87. Dumb ways for an open source project to die

**原文标题**: Dumb ways for an open source project to die

**原文链接**: [https://nesbitt.io/2026/05/19/dumb-ways-for-an-open-source-project-to-die.html](https://nesbitt.io/2026/05/19/dumb-ways-for-an-open-source-project-to-die.html)

生成摘要时出错

---

## 88. The Alaska Permanent Fund as Loose Precedent for AI Data Center 'UBI' Payments

**原文标题**: The Alaska Permanent Fund as Loose Precedent for AI Data Center 'UBI' Payments

**原文链接**: [https://daringfireball.net/linked/2026/05/18/alaska-permanent-fund](https://daringfireball.net/linked/2026/05/18/alaska-permanent-fund)

生成摘要时出错

---

## 89. Public have more fear than hope on AI and future of work, study finds

**原文标题**: Public have more fear than hope on AI and future of work, study finds

**原文链接**: [https://www.kcl.ac.uk/news/one-in-five-britons-think-ai-will-create-civil-unrest-study-finds](https://www.kcl.ac.uk/news/one-in-five-britons-think-ai-will-create-civil-unrest-study-finds)

生成摘要时出错

---

## 90. OpenBSD 7.9

**原文标题**: OpenBSD 7.9

**原文链接**: [https://www.openbsd.org/79.html](https://www.openbsd.org/79.html)

生成摘要时出错

---

## 91. Skills in Web, iOS, and Android

**原文标题**: Skills in Web, iOS, and Android

**原文链接**: [https://x.ai/news/grok-skills](https://x.ai/news/grok-skills)

生成摘要时出错

---

## 92. The foundations of a provably secure operating system (PSOS) (1979) [pdf]

**原文标题**: The foundations of a provably secure operating system (PSOS) (1979) [pdf]

**原文链接**: [http://www.csl.sri.com/users/neumann/psos.pdf](http://www.csl.sri.com/users/neumann/psos.pdf)

生成摘要时出错

---

## 93. The last six months in LLMs in five minutes

**原文标题**: The last six months in LLMs in five minutes

**原文链接**: [https://simonwillison.net/2026/May/19/5-minute-llms/](https://simonwillison.net/2026/May/19/5-minute-llms/)

生成摘要时出错

---

## 94. You can access Gemini chat history without unlocking your phone with Android 16

**原文标题**: You can access Gemini chat history without unlocking your phone with Android 16

**原文链接**: [https://old.reddit.com/r/androiddev/comments/1tihs3s/google_is_not_going_to_fix_this_if_you_see_a/](https://old.reddit.com/r/androiddev/comments/1tihs3s/google_is_not_going_to_fix_this_if_you_see_a/)

生成摘要时出错

---

## 95. Polymarket launches private company trading for speculating on Anthropic, OpenAI

**原文标题**: Polymarket launches private company trading for speculating on Anthropic, OpenAI

**原文链接**: [https://www.cnbc.com/2026/05/19/polymarket-launches-private-company-trading-so-investors-can-speculate-on-anthropic-openai.html](https://www.cnbc.com/2026/05/19/polymarket-launches-private-company-trading-so-investors-can-speculate-on-anthropic-openai.html)

生成摘要时出错

---

## 96. Fixing the Most Dangerous Dam in the World

**原文标题**: Fixing the Most Dangerous Dam in the World

**原文链接**: [https://practical.engineering/blog/2026/5/19/fixing-the-most-dangerous-dam-in-the-world](https://practical.engineering/blog/2026/5/19/fixing-the-most-dangerous-dam-in-the-world)

生成摘要时出错

---

## 97. Incident Report: Railway Blocked by Google Cloud [resolved]

**原文标题**: Incident Report: Railway Blocked by Google Cloud [resolved]

**原文链接**: [https://status.railway.com/incident/I23M92U0](https://status.railway.com/incident/I23M92U0)

生成摘要时出错

---

## 98. Minnesota becomes first state to ban prediction markets

**原文标题**: Minnesota becomes first state to ban prediction markets

**原文链接**: [https://www.npr.org/2026/05/19/nx-s1-5821265/minnesota-ban-prediction-markets](https://www.npr.org/2026/05/19/nx-s1-5821265/minnesota-ban-prediction-markets)

生成摘要时出错

---

## 99. 8k Meta employees are waking up to an email saying they've been laid off

**原文标题**: 8k Meta employees are waking up to an email saying they've been laid off

**原文链接**: [https://qz.com/meta-layoffs-8000-jobs-ai-restructuring-052026](https://qz.com/meta-layoffs-8000-jobs-ai-restructuring-052026)

生成摘要时出错

---

## 100. Gemini Omni

**原文标题**: Gemini Omni

**原文链接**: [https://deepmind.google/models/gemini-omni/](https://deepmind.google/models/gemini-omni/)

生成摘要时出错

---

