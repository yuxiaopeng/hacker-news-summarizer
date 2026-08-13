# Hacker News 热门文章摘要 (2026-08-13)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Gemini 3.7 Flash

**原文标题**: Gemini 3.7 Flash

**原文链接**: [https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash)

Gemini 3.7 Flash 是 Gemini 系列中最新的高性能原生多模态推理模型。现已通过 Interactions API 和 Google AI Studio 全面开放，专为提升速度和解决复杂问题而设计。

**关键技术规格：**
*   **输入支持：** 支持处理文本、图像、视频、音频和 PDF。
*   **Token 限制：** 拥有高达 1,048,576 个输入 Token 和 65,536 个输出 Token 的庞大限制。
*   **版本：** 稳定版模型代码为 `gemini-3.7-flash`。

**核心能力：**
该模型引入了专门的**“思考 (Thinking)”**功能，允许用户选择低、中、高三种推理强度。它支持高级开发者功能，如**计算机使用（预览版）**、代码执行、函数调用、文件搜索和结构化输出。此外，它还支持通过 Google 搜索和 Google 地图进行 Grounding（数据核实），以确保信息的准确性。

**可用性与限制：**
尽管该模型在推理和处理方面表现出色，但目前暂不支持原生音频生成、图像生成或 Live API。用户可以通过多种调用模式访问，包括 Batch API、Flex 推理和 Priority 推理。根据文档显示，最近一次更新记录于 2026 年 8 月。

---

## 2. DRAM 面条化

**原文标题**: Spaghettifying DRAM

**原文链接**: [https://github.com/xoreaxeaxeax/skitter-creek-bath-salts](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts)

《DRAM 乱序化》（Spaghettifying DRAM）一文详述了一个名为 **skitter-creek-bath-salts** 的项目，该项目展示了如何通过操纵 DRAM 控制器的内部地址转换逻辑来绕过硬件安全边界。

**核心机制**
作者指出，尽管 CPU 使用多层保护（如 MMU、IOMMU 和内存区域排除）来隔离系统管理模式（SMM）和平台安全处理器（PSP）等敏感区域，但这些防护机制是基于**物理地址**运行的。然而，内存控制器（MCT）和 DRAM 控制器（DCT）会对这些物理地址进行最后的、通常未公开的转换，将其变为原始的 DRAM 坐标（Bank、Rank、行和列）。

**攻击手段：“乱序化”（Spaghettification）**
通过修改 DRAM 控制器中的特定寄存器（例如 Bank-Swizzle 模式），攻击者可以“重连”内存层级的底层逻辑。这会导致物理地址最终指向的 DRAM 位置与预期不符。由于安全“围栏”位于该层级之上，它们会继续监控原始物理地址，却察觉不到其下方的数据已被重定向。这使得攻击者能够创建“别名”来访问受保护的内存区域，而这些区域对内核而言原本是不可见的。

**技术实现**
该利用技术涉及对 DRAM 控制器寄存器进行高速“注入”（poke），同时通过禁用中断和预填充缓存来尽量减少 DRAM 交互，以防止系统崩溃。由于特定的硬件转换通常未公开，作者利用线性代数来解析新的映射关系。通过将 DRAM 控制器的转换视为 **GF(2) 线性映射**，他们使用 **Z3 SMT 求解器**从观察到的内存模式中重构出转换矩阵。

**目标系统**
该研究在 **AMD Family 16h CPU** 上开发并测试，这些处理器的 DRAM 控制器寄存器已有文档说明且未锁定。作者认为，其底层原理——“*p 的奥德赛”——适用于包括 ARM 和 RISC-V 在内的大多数现代架构。

---

## 3. Mistral OCR 4.1

**原文标题**: Mistral OCR 4.1

**原文链接**: [https://docs.mistral.ai/models/ocr-4-1](https://docs.mistral.ai/models/ocr-4-1)

Mistral OCR 4.1 于 2026 年 7 月 16 日开启公开预览（Public Preview），是专为赋能 Mistral 文档 AI 技术栈而设计的顶级服务。此次更新引入了重大的技术增强，旨在提升文档数字化的精确度与实用性。

**核心特性：**
*   **细粒度提取：** 原生支持段落级边界框（Bounding Box）提取及结构化区块标注。
*   **质量控制：** 提供区块级置信度评分，以确保数据准确性。
*   **API 集成：** 通过 `/v1/ocr` 和 `/v1/batch` 端点支持结构化注释和批量处理。

**定价方案：**
该模型（`mistral-ocr-4-1`）的定价极具竞争力：
*   **标准 OCR：** 每 1,000 页 3.5 欧元（约合 3.81 美元）。
*   **标注页：** 每 1,000 页 4.38 欧元（约合 4.77 美元）。

通过优先提升速度与性能，Mistral OCR 4.1 将自身定位为生态系统中的强大解决方案，该生态系统还包括 Z.ai GLM 5.2 和 Shieldstral 1.0 等其他专业模型。此次发布标志着在为开发者提供复杂结构化文档分析所需工具方面迈出了重要一步。

---

## 4. 为ENIAC而来，为UNIVAC和Skeduflo而留

**原文标题**: Come for ENIAC, Stay for UNIVAC and Skeduflo

**原文链接**: [https://uniqueatpenn.wordpress.com/2026/08/05/come-for-eniac-stay-for-univac-and-skeduflo/](https://uniqueatpenn.wordpress.com/2026/08/05/come-for-eniac-stay-for-univac-and-skeduflo/)

本文重点介绍了计算机先驱约翰·莫奇利（John Mauchly）的生平与遗产，其大量的个人档案现收藏于基斯拉特特藏中心。尽管莫奇利因 1946 年与 J. 普雷斯珀·埃克特共同发明了世界上第一台通用电子计算机 ENIAC 而闻名于世，但作者强调，他的贡献远不止于这一单一成就。

在 ENIAC 之后，莫奇利与埃克特又开发了多个具有里程碑意义的系统，包括 BINAC、EDVAC 以及世界上第一台商用电子计算机 UNIVAC。作者特别突出了莫奇利在 20 世纪 50 年代领导 UNIVAC 应用与研究中心（UARC）时期的成就。在 UARC，莫奇利将重点从仅用计算机解决现有问题，转向主动为商业机构和政府探索利用技术的新途径。这一创新时代也为包括葛丽丝·穆雷·霍珀准将在内的其他先驱提供了支持。

莫奇利的前瞻性通过“Skeduflo”得到了进一步印证，这是一款装在手提箱中、专为建筑进度调度设计的便携式计算机。令人惊叹的是，莫奇利在 1967 年就预言商人终将随身携带口袋式计算机，这一愿景在现代智能手机上得到了实现。

文章最后对莫奇利的品格进行了回顾。作者引用了 J. 普雷斯珀·埃克特在悼词中的话，将莫奇利描述为一位“卓越”的创新者，同时也是一位“正直的人”。基斯拉特中心邀请公众探索莫奇利的丰富藏品，以进一步了解这位助力开启现代计算机工业的伟人。

---

## 5. 选择乏味的技术 (2015)

**原文标题**: Choose Boring Technology (2015)

**原文链接**: [https://mcfunley.com/choose-boring-technology](https://mcfunley.com/choose-boring-technology)

在《选择乏味的技术》中，丹·麦金利（Dan McKinley）认为，公司的成功取决于其专注于核心业务使命而非技术新颖性的能力。他提出了“**创新令牌**”（innovation tokens）的概念：这是一种有限的资源（通常约为三个），公司可以将其用于采用新技术或未经证实的技术。在“光鲜亮丽”的工具（如新数据库或新语言）上过度消耗这些令牌，会分散公司对实际目标的关键注意力。

**乏味 vs. 光鲜**
麦金利将“乏味”技术（如 Postgres、Python、Memcached）定义为能力已被充分理解，且更重要的是其故障模式也已被充分理解的工具。新技术充满风险，因为它们充斥着“未知的未知数”。虽然它们看起来令人兴奋，但危机期间不可预测的表现会产生沉重的运维负担，甚至可能“压垮”团队。

**全局优化**
作者对“最适合该工作的工具”这一观念提出了挑战，称其为忽略了“全局”成本的局部优化。每一项新技术都会以运维开销、监控和认知负荷的形式增加永久性的“税收”。因此，“最佳”工具往往是现有技术栈中“最不差”的选择。开发人员应致力于用最少的一套工具解决尽可能多的问题。

**采用新技术**
麦金利建议采用严谨的流程来引入新技术：
1. **穷尽现有工具**：首先尝试用当前技术栈解决问题。
2. **定义差距**：明确说明为什么当前技术栈在处理此特定任务时成本极高或极其困难。
3. **承诺迁移**：如果新工具是为了替代旧工具，必须有迁移旧功能的计划，以防止留下“残骸”。

最终的目标是“**交付即可**”（Just Ship）。通过选择乏味的技术，工程师可以获得认知上的自由，去解决有意义的业务问题，而不是把时间浪费在基础设施管理上。

---

## 6. DeepSeek Harness 开发者预览版

**原文标题**: DeepSeek Harness developer preview

**原文链接**: [https://deepseek.com/harness/en/](https://deepseek.com/harness/en/)

DeepSeek 宣布推出 DeepSeek Harness (DSH) 开发者预览版，这是一个旨在构建、管理和部署 AI 智能体（AI Agents）的开源框架。该平台秉持“一切皆插件”的核心理念，允许开发者在不修改源代码的情况下，自由更换或重组包括模型、工具、沙箱、存储和 UI 在内的每一项能力。

DSH 基于 Cordis 内核构建，通过管理插件依赖和事件来确保高度模块化的环境。它将智能体定义为“模型”（灵魂）与“Harness”（环境和工具）的结合。

核心特性包括：
*   **全流程可追溯性：** 每一次交互（包括推理、工具调用和上下文注入）都会记录在仅追加的会话日志中。这实现了“轨迹视图”，用户可以恢复、派生、搜索或重放事件流中的任何部分。
*   **多种运行模式：** 
    *   **Standard（标准模式）：** 具备完整网页和文件搜索能力的综合性编码智能体。
    *   **Code（代码模式）：** 利用 TypeScript SDK 允许模型在单个程序中编排复杂的多步操作。
    *   **Minimal（极简模式）：** 仅包含 Shell 和文件编辑器的轻量化环境，针对模型基准测试进行了优化。
    *   **Creator（创作者模式）：** 用于检查运行时并编写自定义智能体预设的专用模式。

DeepSeek Harness 目前已面向全球开放测试。开发者可以通过运行 `npx @deepseek-ai/dsh web` 或从 GitHub 克隆仓库开始体验。该项目旨在培育一个可复用、可组合的智能体基础设施开源生态系统。

---

## 7. 吐火罗语在线

**原文标题**: Tocharian Online

**原文链接**: [https://lrc.la.utexas.edu/eieol/tokol/0](https://lrc.la.utexas.edu/eieol/tokol/0)

"Tocharian Online" provides a comprehensive introduction to Tocharian A and B, two distinct but closely related Indo-European languages discovered in the Tarim Basin of East Turkestan (modern-day Xinjiang). Recovered from Silk Road sites like Turfan and Kučā, the surviving documents date primarily between the 6th and 8th centuries AD.

While most Tocharian texts are Buddhist translations written in a variant of the Brāhmī script, secular documents—such as caravan passes and business letters—exist exclusively in Tocharian B. This leads scholars to suggest that Tocharian A may have already been an extinct liturgical language, similar to Latin, by the time these records were created.

The name "Tocharian" is a historical misnomer. Early 20th-century scholars mistakenly identified the language with the "Toxrï" people of Bactria; however, research now shows these groups were distinct. Native terms for the languages likely included *ārśi* (Tocharian A) and *kuśiññe* (Tocharian B).

Tocharian holds a unique place in historical linguistics as the easternmost Indo-European language. Surprisingly, it is a "centum" language—a characteristic usually reserved for western branches like Celtic and Germanic. This discovery overturned previous theories that divided Indo-European dialects strictly by geography. Furthermore, the language features a reduced phonetic inventory (lacking voiced stops like *b, d, g*) and an agglutinative case system. These features suggest a long period of contact with non-Indo-European families, such as Turkic, Uralic, and Mongolian. 

The article serves as a preface to a series of lessons from the University of Texas at Austin aimed at documenting and preserving these ancient languages.

---

## 8. How art invented humanity

**原文标题**: How art invented humanity

**原文链接**: [https://aeon.co/essays/humans-did-not-invent-art-it-was-the-other-way-around](https://aeon.co/essays/humans-did-not-invent-art-it-was-the-other-way-around)

生成摘要时出错

---

## 9. Gloomberb

**原文标题**: Gloomberb

**原文链接**: [https://gloom.sh/](https://gloom.sh/)

生成摘要时出错

---

## 10. Kubernetes on Oxide: How customer needs shaped our integrations

**原文标题**: Kubernetes on Oxide: How customer needs shaped our integrations

**原文链接**: [https://oxide.computer/blog/kubernetes-on-oxide](https://oxide.computer/blog/kubernetes-on-oxide)

生成摘要时出错

---

## 11. Donkey.bas is 45 Years Old – 131 line of Glory

**原文标题**: Donkey.bas is 45 Years Old – 131 line of Glory

**原文链接**: [https://donkeybas.com/](https://donkeybas.com/)

生成摘要时出错

---

## 12. We Have AI at Home Chapter 1: A Box of Scraps

**原文标题**: We Have AI at Home Chapter 1: A Box of Scraps

**原文链接**: [https://jdagostino.github.io/ai-pt1-box-o-scraps/index.html](https://jdagostino.github.io/ai-pt1-box-o-scraps/index.html)

生成摘要时出错

---

## 13. Ordinary Abundance

**原文标题**: Ordinary Abundance

**原文链接**: [https://ordinaryabundance.com/](https://ordinaryabundance.com/)

生成摘要时出错

---

## 14. Codex in ChatGPT desktop app for Linux is now in preview

**原文标题**: Codex in ChatGPT desktop app for Linux is now in preview

**原文链接**: [https://community.openai.com/t/codex-in-chatgpt-desktop-app-for-linux-is-now-in-preview/1390027](https://community.openai.com/t/codex-in-chatgpt-desktop-app-for-linux-is-now-in-preview/1390027)

生成摘要时出错

---

## 15. I built a 500k-domain search engine for makers in a weekend for $10

**原文标题**: I built a 500k-domain search engine for makers in a weekend for $10

**原文链接**: [https://alexmorleyfinch.github.io/marlin/history/v1/article/the_birth.html](https://alexmorleyfinch.github.io/marlin/history/v1/article/the_birth.html)

生成摘要时出错

---

## 16. Show HN: MCP Memory – Fast Agent Memory Using Google's OKF and SQLite FTS5

**原文标题**: Show HN: MCP Memory – Fast Agent Memory Using Google's OKF and SQLite FTS5

**原文链接**: [https://github.com/fellowgeek/mcp-memory](https://github.com/fellowgeek/mcp-memory)

生成摘要时出错

---

## 17. Graduate student proves a quantum uncertainty principle for fractals

**原文标题**: Graduate student proves a quantum uncertainty principle for fractals

**原文链接**: [https://www.quantamagazine.org/graduate-student-proves-the-fractal-uncertainty-principle-20260812/](https://www.quantamagazine.org/graduate-student-proves-the-fractal-uncertainty-principle-20260812/)

生成摘要时出错

---

## 18. ATG (YC F25) Is Hiring Member of Technical Staff (Data Platform)

**原文标题**: ATG (YC F25) Is Hiring Member of Technical Staff (Data Platform)

**原文链接**: [https://atg.science/careers](https://atg.science/careers)

生成摘要时出错

---

## 19. Choosing an AI model: one prompt, 11 models, different results

**原文标题**: Choosing an AI model: one prompt, 11 models, different results

**原文链接**: [https://www.netlify.com/blog/one-prompt-11-models-very-different-results/](https://www.netlify.com/blog/one-prompt-11-models-very-different-results/)

生成摘要时出错

---

## 20. We eliminated 1,400 CVEs in NanoClaw's container images

**原文标题**: We eliminated 1,400 CVEs in NanoClaw's container images

**原文链接**: [https://www.echo.ai/blog/echo-xnanoclaw-under-the-hood](https://www.echo.ai/blog/echo-xnanoclaw-under-the-hood)

生成摘要时出错

---

## 21. Show HN: OJCP – an open protocol for agent-consumable job data

**原文标题**: Show HN: OJCP – an open protocol for agent-consumable job data

**原文链接**: [https://ojcp.dev/](https://ojcp.dev/)

生成摘要时出错

---

## 22. 我向麦当劳会员计划索取了一份我的个人数据副本。

**原文标题**: I requested a copy of my data from McDonald’s loyalty program

**原文链接**: [https://www.wired.com/story/mcdonalds-built-a-515-page-dossier-on-me-it-says-ill-never-leave/](https://www.wired.com/story/mcdonalds-built-a-515-page-dossier-on-me-it-says-ill-never-leave/)

A WIRED reporter exercised their legal rights under California privacy law to request their personal data from McDonald’s loyalty program, receiving a staggering 515-page report. The document revealed that the company’s "secret sauce" is extensive commercial surveillance, tracking every transaction, app interaction, and location visit.

The report’s most striking feature was its use of predictive algorithms. McDonald’s estimated the reporter’s future behavior over a six-week period, predicting exactly how many times they would visit (2.16), their average spend per order ($13.49), and their total predicted value ($29.15). The system even assigned an "attrition" score of zero, suggesting the reporter was a guaranteed lifelong customer. Furthermore, the data categorized the author into behavioral archetypes, such as "Food-Led Afternoon Snack," and ranked their most relevant products based on frequency and recency.

Privacy experts noted that while individual data points might seem innocuous, the aggregation of years of information creates an invasive profile of a consumer’s life. They highlighted a stark power imbalance where technology is designed to maximize profit through long-term surveillance rather than just providing deals.

Ultimately, the author found the level of detail and predictive "dossier" concerning. They requested that McDonald’s delete their stored information and decided to stop eating at the chain—not just for health reasons, but to defy the algorithm’s prediction of their "zero" attrition. The article serves as a wake-up call regarding the hidden costs of digital loyalty programs and the extensive data mining practiced by major corporations.

---

## 23. Better Gaussian Splatting in Julia

**原文标题**: Better Gaussian Splatting in Julia

**原文链接**: [https://pxl-th.github.io/blog/better-gs-julia/](https://pxl-th.github.io/blog/better-gs-julia/)

生成摘要时出错

---

## 24. Deutsche Bank becomes first foreign yuan clearing bank in Europe

**原文标题**: Deutsche Bank becomes first foreign yuan clearing bank in Europe

**原文链接**: [https://tradersunion.com/news/central-banks/show/2973571-deutsche-bank-becomes/](https://tradersunion.com/news/central-banks/show/2973571-deutsche-bank-becomes/)

生成摘要时出错

---

## 25. The Indo-European Family Tree

**原文标题**: The Indo-European Family Tree

**原文链接**: [https://djbinder.com/language-tree/](https://djbinder.com/language-tree/)

生成摘要时出错

---

## 26. GoAccess – Open-source real-time log analyzer and interactive viewer

**原文标题**: GoAccess – Open-source real-time log analyzer and interactive viewer

**原文链接**: [https://goaccess.io/](https://goaccess.io/)

生成摘要时出错

---

## 27. The mathematical physics of rainbows and glories (2001) [pdf]

**原文标题**: The mathematical physics of rainbows and glories (2001) [pdf]

**原文链接**: [https://tlakoba.w3.uvm.edu/AppliedUGMath/auxpaper_rainbow_glory_review.pdf](https://tlakoba.w3.uvm.edu/AppliedUGMath/auxpaper_rainbow_glory_review.pdf)

生成摘要时出错

---

## 28. Time to Move On: Querying Without Nulls and Bags

**原文标题**: Time to Move On: Querying Without Nulls and Bags

**原文链接**: [https://arxiv.org/abs/2608.10863](https://arxiv.org/abs/2608.10863)

生成摘要时出错

---

## 29. Launch HN: Bullet (YC S26) – A Faster Coding Agent

**原文标题**: Launch HN: Bullet (YC S26) – A Faster Coding Agent

**原文链接**: [https://www.codewithbullet.com](https://www.codewithbullet.com)

生成摘要时出错

---

## 30. The lattice of sets of natural numbers is rich (2021)

**原文标题**: The lattice of sets of natural numbers is rich (2021)

**原文链接**: [https://jdh.hamkins.org/the-lattice-of-sets-of-natural-numbers-is-rich/](https://jdh.hamkins.org/the-lattice-of-sets-of-natural-numbers-is-rich/)

生成摘要时出错

---

## 31. Translating the Renaissance: 17,000+ historical source texts

**原文标题**: Translating the Renaissance: 17,000+ historical source texts

**原文链接**: [https://sourcelibrary.org](https://sourcelibrary.org)

生成摘要时出错

---

## 32. Nine PBS could lose 70 years of archives after cloud vendor goes defunct

**原文标题**: Nine PBS could lose 70 years of archives after cloud vendor goes defunct

**原文链接**: [https://www.tomshardware.com/software/cloud-storage/nine-pbs-loses-access-to-70-years-of-data-after-contracted-cloud-storage-vendor-goes-defunct-public-tv-channel-sues-iron-mountain-data-center-which-hosts-archival-materials-to-ensure-preservation](https://www.tomshardware.com/software/cloud-storage/nine-pbs-loses-access-to-70-years-of-data-after-contracted-cloud-storage-vendor-goes-defunct-public-tv-channel-sues-iron-mountain-data-center-which-hosts-archival-materials-to-ensure-preservation)

生成摘要时出错

---

## 33. Picking berries is my meditation

**原文标题**: Picking berries is my meditation

**原文链接**: [https://www.tsoon.com/posts/picking-berries-meditation/](https://www.tsoon.com/posts/picking-berries-meditation/)

生成摘要时出错

---

## 34. Show HN: At 16K features, flat autoencoders break. Curved space doesn't

**原文标题**: Show HN: At 16K features, flat autoencoders break. Curved space doesn't

**原文链接**: [https://github.com/vishal-dehurdle/hypersae](https://github.com/vishal-dehurdle/hypersae)

生成摘要时出错

---

## 35. OpenCV AI Competition 2026

**原文标题**: OpenCV AI Competition 2026

**原文链接**: [https://opencv.org/opencv-ai-competition-2026/](https://opencv.org/opencv-ai-competition-2026/)

生成摘要时出错

---

## 36. DeepSeek API Pricing Update

**原文标题**: DeepSeek API Pricing Update

**原文链接**: [https://twitter.com/deepseek_ai/status/2087864589895798968](https://twitter.com/deepseek_ai/status/2087864589895798968)

生成摘要时出错

---

## 37. Antiqua–Fraktur dispute

**原文标题**: Antiqua–Fraktur dispute

**原文链接**: [https://en.wikipedia.org/wiki/Antiqua%E2%80%93Fraktur_dispute](https://en.wikipedia.org/wiki/Antiqua%E2%80%93Fraktur_dispute)

生成摘要时出错

---

## 38. Flutter 3.47

**原文标题**: Flutter 3.47

**原文链接**: [https://flutter.dev/blog/whats-new-in-flutter-3-47](https://flutter.dev/blog/whats-new-in-flutter-3-47)

生成摘要时出错

---

## 39. Build a Stratum 1 PTP Grandmaster on a Budget

**原文标题**: Build a Stratum 1 PTP Grandmaster on a Budget

**原文链接**: [https://opscode.io/posts/ptp-grandmaster-cm4-sr1723u10/](https://opscode.io/posts/ptp-grandmaster-cm4-sr1723u10/)

生成摘要时出错

---

## 40. Amazon will train on Twitch streamers' content by default, unless they opt out

**原文标题**: Amazon will train on Twitch streamers' content by default, unless they opt out

**原文链接**: [https://techcrunch.com/2026/08/12/amazon-will-train-on-twitch-streamers-content-by-default-unless-they-opt-out/](https://techcrunch.com/2026/08/12/amazon-will-train-on-twitch-streamers-content-by-default-unless-they-opt-out/)

生成摘要时出错

---

## 41. Heart aerospace completes first flight of largest electric aircraft

**原文标题**: Heart aerospace completes first flight of largest electric aircraft

**原文链接**: [https://www.heartaerospace.com/newsroom/heart-aerospace-completes-first-flight-of-world-s-largest-electric-aircraft](https://www.heartaerospace.com/newsroom/heart-aerospace-completes-first-flight-of-world-s-largest-electric-aircraft)

生成摘要时出错

---

## 42. DeepSeek V4 Pro 0813

**原文标题**: DeepSeek V4 Pro 0813

**原文链接**: [https://openrouter.ai/deepseek/deepseek-v4-pro-0813](https://openrouter.ai/deepseek/deepseek-v4-pro-0813)

生成摘要时出错

---

## 43. Launch HN: Discovered Materials (YC P26) – AI agents to discover new materials

**原文标题**: Launch HN: Discovered Materials (YC P26) – AI agents to discover new materials

**原文链接**: [https://discoveredmaterials.com/research/](https://discoveredmaterials.com/research/)

生成摘要时出错

---

## 44. Rails Is Built for AI

**原文标题**: Rails Is Built for AI

**原文链接**: [https://rubyonrails.org/ai](https://rubyonrails.org/ai)

生成摘要时出错

---

## 45. Samsung is using Claude to verify chip designs. It's not going smoothly

**原文标题**: Samsung is using Claude to verify chip designs. It's not going smoothly

**原文链接**: [https://www.neowin.net/news/samsung-is-using-claude-to-verify-chip-designs-and-its-not-going-smoothly/](https://www.neowin.net/news/samsung-is-using-claude-to-verify-chip-designs-and-its-not-going-smoothly/)

生成摘要时出错

---

## 46. US Navy sailors try to throw themselves overboard after 250 days at sea

**原文标题**: US Navy sailors try to throw themselves overboard after 250 days at sea

**原文链接**: [https://www.telegraph.co.uk/world-news/2026/08/13/us-navy-sailors-jump-overboard-after-nine-months-at-sea/](https://www.telegraph.co.uk/world-news/2026/08/13/us-navy-sailors-jump-overboard-after-nine-months-at-sea/)

生成摘要时出错

---

## 47. Tracking down the 16-year-old WAL-reset SQLite bug

**原文标题**: Tracking down the 16-year-old WAL-reset SQLite bug

**原文链接**: [https://tailscale.com/blog/sqlite-wal-reset-bug](https://tailscale.com/blog/sqlite-wal-reset-bug)

生成摘要时出错

---

## 48. DeepSeek up to 1000% price hike is live

**原文标题**: DeepSeek up to 1000% price hike is live

**原文链接**: [https://xcancel.com/deepseek_ai/status/2087864589895798968](https://xcancel.com/deepseek_ai/status/2087864589895798968)

生成摘要时出错

---

## 49. Show HN: Track habits, metrics, time and whateven you think worth tracking

**原文标题**: Show HN: Track habits, metrics, time and whateven you think worth tracking

**原文链接**: [https://habitpocket.io/](https://habitpocket.io/)

生成摘要时出错

---

## 50. Why Target Common Lisp for Code Generation?

**原文标题**: Why Target Common Lisp for Code Generation?

**原文链接**: [http://funcall.blogspot.com/2026/08/why-vibe-code-in-lisp.html](http://funcall.blogspot.com/2026/08/why-vibe-code-in-lisp.html)

生成摘要时出错

---

## 51. Thanks to social media, canned sardines are a scarcity on the supermarket shelf

**原文标题**: Thanks to social media, canned sardines are a scarcity on the supermarket shelf

**原文链接**: [https://corneroffifth.studio/why-cant-you-find-canned-sardines-right-now/](https://corneroffifth.studio/why-cant-you-find-canned-sardines-right-now/)

生成摘要时出错

---

## 52. You Can't Copy Palantir

**原文标题**: You Can't Copy Palantir

**原文链接**: [https://ethanding.substack.com/p/why-you-cant-copy-palantir](https://ethanding.substack.com/p/why-you-cant-copy-palantir)

生成摘要时出错

---

## 53. Happy 45th Birthday to the IBM PC and Model F/XT

**原文标题**: Happy 45th Birthday to the IBM PC and Model F/XT

**原文链接**: [https://sharktastica.co.uk/articles/pc-fxt-45](https://sharktastica.co.uk/articles/pc-fxt-45)

生成摘要时出错

---

## 54. Qwen3.8-2.4T

**原文标题**: Qwen3.8-2.4T

**原文链接**: [https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)

生成摘要时出错

---

## 55. Three years after police raid on Kansas newspaper, reporter settles for $850K

**原文标题**: Three years after police raid on Kansas newspaper, reporter settles for $850K

**原文链接**: [https://kansasreflector.com/2026/08/11/three-years-after-police-raid-on-kansas-newspaper-reporter-settles-lawsuit-for-850k/](https://kansasreflector.com/2026/08/11/three-years-after-police-raid-on-kansas-newspaper-reporter-settles-lawsuit-for-850k/)

生成摘要时出错

---

## 56. AI Generated 3D Models Flood Market, but Almost No One Is Buying Them

**原文标题**: AI Generated 3D Models Flood Market, but Almost No One Is Buying Them

**原文链接**: [https://www.404media.co/ai-generated-3d-models-flood-market-but-almost-no-one-is-buying-them/](https://www.404media.co/ai-generated-3d-models-flood-market-but-almost-no-one-is-buying-them/)

生成摘要时出错

---

## 57. Previewing Ultrafast mode: GPT‑5.6 Sol at up to 14X the speed

**原文标题**: Previewing Ultrafast mode: GPT‑5.6 Sol at up to 14X the speed

**原文链接**: [https://openai.com/index/previewing-ultrafast/](https://openai.com/index/previewing-ultrafast/)

生成摘要时出错

---

## 58. Delta

**原文标题**: Delta

**原文链接**: [https://zed.dev/blog/introducing-delta](https://zed.dev/blog/introducing-delta)

生成摘要时出错

---

## 59. Principia Mathematica is modern and insightful

**原文标题**: Principia Mathematica is modern and insightful

**原文链接**: [https://okmij.org/ftp/Computation/Impressions/PrincipiaMathematica.html](https://okmij.org/ftp/Computation/Impressions/PrincipiaMathematica.html)

生成摘要时出错

---

## 60. Breaking the WAL

**原文标题**: Breaking the WAL

**原文链接**: [https://antithesis.com/blog/2026/wal-reset-bug/](https://antithesis.com/blog/2026/wal-reset-bug/)

生成摘要时出错

---

## 61. Anthropic: Introducing The Conceptual Reasoning Index

**原文标题**: Anthropic: Introducing The Conceptual Reasoning Index

**原文链接**: [https://alignment.anthropic.com/2026/conceptual-reasoning-index/](https://alignment.anthropic.com/2026/conceptual-reasoning-index/)

生成摘要时出错

---

## 62. In a first, US will allow some private firms to carry out cyberattacks

**原文标题**: In a first, US will allow some private firms to carry out cyberattacks

**原文链接**: [https://techcrunch.com/2026/08/13/in-a-first-us-will-allow-some-private-firms-to-carry-out-cyberattacks/](https://techcrunch.com/2026/08/13/in-a-first-us-will-allow-some-private-firms-to-carry-out-cyberattacks/)

生成摘要时出错

---

## 63. White House taps security firms for offensive hack-back operations

**原文标题**: White House taps security firms for offensive hack-back operations

**原文链接**: [https://www.bleepingcomputer.com/news/security/white-house-taps-security-firms-for-offensive-hack-back-operations/](https://www.bleepingcomputer.com/news/security/white-house-taps-security-firms-for-offensive-hack-back-operations/)

生成摘要时出错

---

## 64. The Three-Stroke Problem

**原文标题**: The Three-Stroke Problem

**原文链接**: [https://penpot.app/blog/the-three-stroke-problem/](https://penpot.app/blog/the-three-stroke-problem/)

生成摘要时出错

---

## 65. Pixel Watch 5

**原文标题**: Pixel Watch 5

**原文链接**: [https://blog.google/products-and-platforms/devices/pixel/pixel-watch-5/](https://blog.google/products-and-platforms/devices/pixel/pixel-watch-5/)

生成摘要时出错

---

## 66. Anthropic in talks to buy Decart AI for $6B

**原文标题**: Anthropic in talks to buy Decart AI for $6B

**原文链接**: [https://www.reuters.com/technology/anthropic-talks-buy-decart-ai-source-says-2026-08-13/](https://www.reuters.com/technology/anthropic-talks-buy-decart-ai-source-says-2026-08-13/)

生成摘要时出错

---

## 67. Lovable raises $400M Series C

**原文标题**: Lovable raises $400M Series C

**原文链接**: [https://lovable.dev/blog/series-c](https://lovable.dev/blog/series-c)

生成摘要时出错

---

## 68. uBlock Origin is giving up the fight to keep ads off Facebook

**原文标题**: uBlock Origin is giving up the fight to keep ads off Facebook

**原文链接**: [https://digitalescapetools.com/2026/08/ublock-origin-stops-chasing-facebook-ads.html](https://digitalescapetools.com/2026/08/ublock-origin-stops-chasing-facebook-ads.html)

生成摘要时出错

---

## 69. Mushroom behind 'tiny people' hallucinations identified

**原文标题**: Mushroom behind 'tiny people' hallucinations identified

**原文链接**: [https://phys.org/news/2026-08-qa-mushroom-tiny-people-hallucinations.html](https://phys.org/news/2026-08-qa-mushroom-tiny-people-hallucinations.html)

生成摘要时出错

---

## 70. Mozilla says stricter antitrust measures against Google 'threaten Firefox'

**原文标题**: Mozilla says stricter antitrust measures against Google 'threaten Firefox'

**原文链接**: [https://www.techcentral.ie/mozilla-says-stricter-antitrust-measures-against-google-threaten-firefox/](https://www.techcentral.ie/mozilla-says-stricter-antitrust-measures-against-google-threaten-firefox/)

生成摘要时出错

---

## 71. The hardest working font in Manhattan (2025)

**原文标题**: The hardest working font in Manhattan (2025)

**原文链接**: [https://aresluna.org/the-hardest-working-font-in-manhattan/](https://aresluna.org/the-hardest-working-font-in-manhattan/)

生成摘要时出错

---

## 72. Build Wide, Ship Narrow

**原文标题**: Build Wide, Ship Narrow

**原文链接**: [https://adapt.com/blog/build-wide-ship-narrow](https://adapt.com/blog/build-wide-ship-narrow)

生成摘要时出错

---

## 73. From rubber boots to Copa: When MicroProse Soccer revolutionized football

**原文标题**: From rubber boots to Copa: When MicroProse Soccer revolutionized football

**原文链接**: [https://spillhistorie.no/2026/08/08/fra-gummistovler-til-copa-da-microprose-soccer-revolusjonerte-fotballen/](https://spillhistorie.no/2026/08/08/fra-gummistovler-til-copa-da-microprose-soccer-revolusjonerte-fotballen/)

生成摘要时出错

---

## 74. Text AI watermarks will always be trivial to remove

**原文标题**: Text AI watermarks will always be trivial to remove

**原文链接**: [https://www.seangoedecke.com/text-ai-watermarks/](https://www.seangoedecke.com/text-ai-watermarks/)

生成摘要时出错

---

## 75. 2026 Eclipse Webcams

**原文标题**: 2026 Eclipse Webcams

**原文链接**: [https://jonty.github.io/2026_eclipse_webcams/](https://jonty.github.io/2026_eclipse_webcams/)

生成摘要时出错

---

## 76. High-Res Photo Shows Sand-Capped Butte Rising from Mars Plain of Polygons

**原文标题**: High-Res Photo Shows Sand-Capped Butte Rising from Mars Plain of Polygons

**原文链接**: [https://petapixel.com/2026/08/04/amazing-high-res-photo-shows-a-butte-rising-from-mars/](https://petapixel.com/2026/08/04/amazing-high-res-photo-shows-a-butte-rising-from-mars/)

生成摘要时出错

---

## 77. The Strongest El Niño Ever Forecast and the Hunger It Will Leave Behind

**原文标题**: The Strongest El Niño Ever Forecast and the Hunger It Will Leave Behind

**原文链接**: [https://www.4hunger.org/p/scorched-harvest-the-strongest-el](https://www.4hunger.org/p/scorched-harvest-the-strongest-el)

生成摘要时出错

---

## 78. License plate reader searches should require a warrant

**原文标题**: License plate reader searches should require a warrant

**原文链接**: [https://andrewpwheeler.com/2026/08/12/license-plate-reader-searches-should-require-a-warrant/](https://andrewpwheeler.com/2026/08/12/license-plate-reader-searches-should-require-a-warrant/)

生成摘要时出错

---

## 79. Pixel 11 Pro Fold

**原文标题**: Pixel 11 Pro Fold

**原文链接**: [https://blog.google/products-and-platforms/devices/pixel/pixel-11-pro-fold/](https://blog.google/products-and-platforms/devices/pixel/pixel-11-pro-fold/)

生成摘要时出错

---

## 80. U of Michigan drops first-semester grades to ‘curb mental health crisis’

**原文标题**: U of Michigan drops first-semester grades to ‘curb mental health crisis’

**原文链接**: [https://www.wsj.com/us-news/education/university-of-michigan-grades-mental-health-1a5701d4](https://www.wsj.com/us-news/education/university-of-michigan-grades-mental-health-1a5701d4)

生成摘要时出错

---

## 81. LoongLeak: A Vulnerability Affecting Chinese Loongson 3A5000 and 3A6000 CPUs

**原文标题**: LoongLeak: A Vulnerability Affecting Chinese Loongson 3A5000 and 3A6000 CPUs

**原文链接**: [https://loongleakattack.com/](https://loongleakattack.com/)

生成摘要时出错

---

## 82. Record heat is drying up Europe's major rivers, as these striking images show

**原文标题**: Record heat is drying up Europe's major rivers, as these striking images show

**原文链接**: [https://www.washingtonpost.com/climate-environment/interactive/2026/08/12/see-receding-water-levels-europes-major-rivers/](https://www.washingtonpost.com/climate-environment/interactive/2026/08/12/see-receding-water-levels-europes-major-rivers/)

生成摘要时出错

---

## 83. Amazon loses US court ban on Perplexity's AI shopping tools

**原文标题**: Amazon loses US court ban on Perplexity's AI shopping tools

**原文链接**: [https://www.reuters.com/business/retail-consumer/amazon-loses-us-court-ban-perplexitys-ai-shopping-tools-2026-08-04/](https://www.reuters.com/business/retail-consumer/amazon-loses-us-court-ban-perplexitys-ai-shopping-tools-2026-08-04/)

生成摘要时出错

---

## 84. Tim King, AmigaDOS developer, has died

**原文标题**: Tim King, AmigaDOS developer, has died

**原文链接**: [https://amiga-news.de/en/news/AN-2026-08-00070-EN.html](https://amiga-news.de/en/news/AN-2026-08-00070-EN.html)

生成摘要时出错

---

## 85. Grok 4.6

**原文标题**: Grok 4.6

**原文链接**: [https://x.ai/news/grok-4-6](https://x.ai/news/grok-4-6)

生成摘要时出错

---

## 86. 2026 Clacton By-Election

**原文标题**: 2026 Clacton By-Election

**原文链接**: [https://en.wikipedia.org/wiki/2026_Clacton_by-election](https://en.wikipedia.org/wiki/2026_Clacton_by-election)

生成摘要时出错

---

## 87. HTML over WebSockets: real-time SPAs with barely any JavaScript

**原文标题**: HTML over WebSockets: real-time SPAs with barely any JavaScript

**原文链接**: [https://en.andros.dev/blog/ef4968f5/html-over-websockets-real-time-spas-with-barely-any-javascript/](https://en.andros.dev/blog/ef4968f5/html-over-websockets-real-time-spas-with-barely-any-javascript/)

生成摘要时出错

---

## 88. Why is C the symbol for the speed of light? (2004)

**原文标题**: Why is C the symbol for the speed of light? (2004)

**原文链接**: [https://math.ucr.edu/home/baez/physics/Relativity/SpeedOfLight/c.html](https://math.ucr.edu/home/baez/physics/Relativity/SpeedOfLight/c.html)

生成摘要时出错

---

## 89. Perplexity blocks Time's ads served to AI agents, calling them 'deceptive'

**原文标题**: Perplexity blocks Time's ads served to AI agents, calling them 'deceptive'

**原文链接**: [https://digiday.com/media/perplexity-blocks-times-ads-served-to-ai-agents-calling-them-deceptive/](https://digiday.com/media/perplexity-blocks-times-ads-served-to-ai-agents-calling-them-deceptive/)

生成摘要时出错

---

## 90. Hiroshi Okuda, Toyota chair who pushed for the Prius, dies at 93

**原文标题**: Hiroshi Okuda, Toyota chair who pushed for the Prius, dies at 93

**原文链接**: [https://www.japantimes.co.jp/business/2026/08/12/companies/toyota-hiroshi-okada-death/](https://www.japantimes.co.jp/business/2026/08/12/companies/toyota-hiroshi-okada-death/)

生成摘要时出错

---

## 91. OpenAI Hires New Chief Revenue Officer After Less Than a Year

**原文标题**: OpenAI Hires New Chief Revenue Officer After Less Than a Year

**原文链接**: [https://www.bloomberg.com/news/articles/2026-08-13/openai-hires-new-chief-revenue-officer-after-less-than-a-year](https://www.bloomberg.com/news/articles/2026-08-13/openai-hires-new-chief-revenue-officer-after-less-than-a-year)

生成摘要时出错

---

## 92. Show HN: Ballet – Workflow automation that writes integrations against any API

**原文标题**: Show HN: Ballet – Workflow automation that writes integrations against any API

**原文链接**: [https://www.ballet.dev/](https://www.ballet.dev/)

生成摘要时出错

---

## 93. The 37signals Manager Playbook

**原文标题**: The 37signals Manager Playbook

**原文链接**: [https://basecamp.com/managers](https://basecamp.com/managers)

生成摘要时出错

---

## 94. Anthropic investors bet on $2T valuation in record IPO

**原文标题**: Anthropic investors bet on $2T valuation in record IPO

**原文链接**: [https://www.ft.com/content/840ac156-af1c-4a82-b260-ae791072fcfa](https://www.ft.com/content/840ac156-af1c-4a82-b260-ae791072fcfa)

生成摘要时出错

---

## 95. The punched card tabulator

**原文标题**: The punched card tabulator

**原文链接**: [https://www.ibm.com/history/punched-card-tabulator](https://www.ibm.com/history/punched-card-tabulator)

生成摘要时出错

---

## 96. Felix and I

**原文标题**: Felix and I

**原文链接**: [https://jacobfilipp.com/felix/](https://jacobfilipp.com/felix/)

生成摘要时出错

---

## 97. Temperature Zero for Culture: Why Everything Is Starting to Look the Same

**原文标题**: Temperature Zero for Culture: Why Everything Is Starting to Look the Same

**原文链接**: [https://laurenleek.substack.com/p/temperature-zero-for-culture-why](https://laurenleek.substack.com/p/temperature-zero-for-culture-why)

生成摘要时出错

---

## 98. Why tiny JPEGs look different in Chrome

**原文标题**: Why tiny JPEGs look different in Chrome

**原文链接**: [https://guillaumetech.github.io/posts/jpg-scaling-chrome/](https://guillaumetech.github.io/posts/jpg-scaling-chrome/)

生成摘要时出错

---

## 99. Process as a Proxy for Motivation

**原文标题**: Process as a Proxy for Motivation

**原文链接**: [https://bengodfrey.dev/blog/process/](https://bengodfrey.dev/blog/process/)

生成摘要时出错

---

## 100. Worms: The Future of Yesterday's Worms Today

**原文标题**: Worms: The Future of Yesterday's Worms Today

**原文链接**: [https://worm.net/](https://worm.net/)

生成摘要时出错

---

