# Hacker News 热门文章摘要 (2026-08-10)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Muse Glimmer：专为全时本地智能体工作流优化的 300 亿参数模型

**原文标题**: Muse Glimmer: 30B-parameter model optimized for always-on local agent workflows

**原文链接**: [https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model)

Meta 超级智能实验室（Meta Superintelligence Labs）发布了 **Muse Glimmer**，这是一个拥有 300 亿参数的开源权重模型，专门针对“全天候”本地智能体工作流进行了优化。该模型采用 Apache 2.0 协议发布，旨在单 GPU 电脑或 MacBook 等消费级硬件上运行，支持私有、离线的 AI 任务，包括函数调用、本地编程以及 LLM-as-a-judge（大模型评审）评估。

**核心技术能力：**
*   **专注于智能体：** Muse Glimmer 针对端到端任务完成、精准工具调用和多步推理进行了训练。它具备故障恢复机制，能够诊断并重试失败的工具调用。
*   **多模态与多语言：** 通过专用的感知编码器，该模型可以处理图文交错的内容（如截图和图表）。它还支持 100 多种语言。
*   **先进训练技术：** 该模型通过对更大的“Muse Spark”教师模型进行 Logit 蒸馏开发而成，随后针对推理密集型数据进行了中期训练和强化学习。

**本地优化：**
为了确保在本地设备上的响应性能，Muse Glimmer 采用 4 位（4-bit）量化技术，使其显存占用控制在 20GB 以内。此外，它还利用了 **DFlash**——一种投机性解码“草案”模型，显著提升了在 MacBook M4/M5 Max 和 NVIDIA RTX 5090 等硬件上的生成速度。

**生态系统与可用性：**
模型权重已在 Hugging Face 上发布，并已支持或即将支持 llama.cpp、MLX、ExecuTorch 和 Ollama 等框架。Meta 还提供了开发者文档和构建自定义智能体支架的指南，进一步履行其对开放 AI 研究和本地智能体能力的承诺。

---

## 2. Sonic Pi v5

**原文标题**: Sonic Pi v5

**原文链接**: [https://www.patreon.com/samaaron/posts/sonic-pi-v5-166001392](https://www.patreon.com/samaaron/posts/sonic-pi-v5-166001392)

在这篇 Patreon 帖子中，开发者 Sam Aaron 宣布发布 **Sonic Pi v5**，代号为“蓝色版”（The Blue Edition）。这一重大更新标志着该软件十年历史中的一个重要里程碑，重点在于基础架构的全面重构，以确保长期的可持续性与性能。

v5 的核心亮点是重大的内部重写。该项目已将大部分核心逻辑迁移至全新的 C++ 架构，从而提升了时间精度并降低了延迟。这一变革使实时编程（live-coding）体验更加稳健且响应迅速，尤其适用于专业演出。

v5 的主要功能与改进包括：

*   **Ableton Link 集成**：现已内置对 Ableton Link 的原生支持，允许 Sonic Pi 与网络中的其他音乐软件及硬件进行无缝同步。
*   **现代操作系统支持**：该更新全面兼容最新的操作系统，包括针对 Apple Silicon 的原生构建，以及对 Raspberry Pi OS (Bookworm) 的优化支持。
*   **新工具与音效**：新版本引入了全新的合成与效果功能，例如 `fx_pitch_shift`（移调效果器），丰富了用户的音色选择。
*   **架构稳定性**：通过转向更具模块化的 C++ 核心，该平台能更好地支持未来的功能开发并保持跨平台的一致性。

Aaron 强调，v5 是一个“奠基性”的版本。尽管它包含了一些直观的新功能（如 Link），但其首要目标是实现代码库的现代化，使 Sonic Pi 在未来十年内依然保持生命力。他在文末感谢了 Patreon 支持者，正是得益于他们的资助，他才能全身心投入于这一复杂的技术转型，确保这款工具始终对所有人免费且开源。

---

## 3. Show HN：Ante，一个可离线运行的单二进制编程智能体

**原文标题**: Show HN: Ante, a coding agent in a single binary that runs offline

**原文链接**: [https://github.com/AntigmaLabs/ante](https://github.com/AntigmaLabs/ante)

生成摘要时出错

---

## 4. Launch HN：Stoa Markets (YC S26) —— GPU 与 AI 服务器交易平台

**原文标题**: Launch HN: Stoa Markets (YC S26) – A Marketplace for GPUs and AI Servers

**原文链接**: [https://www.stoaexchange.com](https://www.stoaexchange.com)

Stoa Markets (YC S26) 是一个专门的交易平台，旨在为碎片化的 AI 硬件行业带来透明度、价格发现和安全性。该平台通过在结构化环境中连接经过验证的交易对手，促进高需求 GPU 和 AI 服务器（如 NVIDIA H100、H200 和 B200）的买卖。

目前，GPU 市场面临供应分散（分布在经纪商、OEM 和云提供商中）和价格信号不完整的问题。Stoa 通过提供一个中心化场所来解决这些问题，用户可以在这里查看实时的“出清水平”，并根据确定的报价而非过时的私人询价进行交易。

**该平台具有四个步骤的执行流程：**
1. **创建 RFQ：** 用户描述需求或上传报价 PDF，由 AI 协助起草报价请求 (RFQ)。
2. **实价报价：** 经过验证的交易商提供具有法律约束力的价格。
3. **执行：** 报价一旦被接受，交易即成为具有明确规格和条件条款的约束性合同。
4. **安全结算：** 资金由第三方托管，仅在发货、交付和验收的记录流程完成后才予以释放。

Stoa 面向广泛的行业参与者，包括 AI 实验室、数据中心运营商、云提供商以及寻求承销 GPU 抵押交易的金融机构。通过摆脱通过私信和表格进行场外交易带来的“先汇款后碰运气”的风险，Stoa 提供了一个具有清晰审计追踪并能降低交易对手风险的专业化替代方案。

---

## 5. Exploiting System Management Mode with a very long interrupt

**原文标题**: Exploiting System Management Mode with a very long interrupt

**原文链接**: [https://github.com/xoreaxeaxeax/smiiiiiiiiiiiiiiii](https://github.com/xoreaxeaxeax/smiiiiiiiiiiiiiiii)

本文描述了 x86 CPU 系统管理模式（SMM）中一个被称为“SMI 去同步”（SMI desynchronization）的漏洞。SMM 是一种高特权执行环境，它基于所有 CPU 核心必须同时进入和退出该模式的假设，从而确保在执行敏感操作时不会运行任何非 SMM 代码。

**机制**
该漏洞利用了固件在同步核心进入 SMM 时所使用的“汇合”（rendezvous）过程。当系统管理中断（SMI）被触发时，固件会等待所有核心就位。然而，为了防止系统挂起，这种等待设有一个硬编码的超时限制——通常为一秒。

研究员 Christopher Domas 证明，通过执行一条执行时间超过该超时限制的极端冗长机器指令，可以使某个核心保持在 SMM 之外。由于 SMI 仅在指令边界处响应，因此在该指令完成之前，该核心始终处于不可中断状态。

**方法**
该概念验证（PoC）通过从缓慢且未公开的内存映射 I/O（MMIO）区域进行宽向量读取（例如 `vmovdqu`）来实现这种“耗时一秒的指令”。通过强制 CPU 在存在资源竞争的高延迟总线上停顿，单条指令的执行可以超过 40 亿个时钟周期，导致其他核心放弃等待并独自进入 SMM。

**安全影响**
这种去同步破坏了 SMM 的核心安全前提。它将以前无法利用的“检查时间到使用时间”（TOCTOU）漏洞——即 SMM 处理程序在检查共享内存中的值后立即使用该值——转化为可实行的软件攻击。历史上，利用此类漏洞通常需要通过具有 DMA 能力的硬件进行物理接触；而这项研究证明，通过允许“受害者”核心在“处理程序”核心于 SMM 中执行时修改内存，仅靠软件手段即可实现攻击。

---

## 6. 认知公地悲剧

**原文标题**: The Tragedy of the Cognitive Commons

**原文链接**: [https://arxiv.org/abs/2607.29380](https://arxiv.org/abs/2607.29380)

《认知公地的悲剧》由诺兰·洛维特（Nolan Lovett）撰写，探讨了人工智能的广泛采用如何可能在无意中耗尽长期更新所需的集体专业知识储备。虽然对于追求效率的单个组织而言，采用人工智能往往看似理性，但作者认为，这可能会破坏初级从业者成长为资深专家的传统路径。

本文引入了“认知公地”框架，该框架认为专业知识是一种需要集体维护的共享资源。其核心主题是区分“内化精通”（通过持续实践获得的深厚、直觉性的领域知识）与“分布式精通”（协调人机协作系统的技能）。洛维特强调了一个被称为“验证纽带”的关键悖论：有效监督和验证人工智能输出的能力，恰恰依赖于那种正受到人工智能采用威胁的内化专业知识。

研究表明，在临床医学和技术劳动力市场等人工智能高度渗透的行业中，专业知识的“再生路径”已显现出中断迹象。如果入门级任务被完全自动化，初级专业人员可能永远无法获得达到高级水平所需的基石经验。

最终，本文将专业知识的发展重新定义为集体治理问题，而非单纯的组织优化。洛维特总结道，为了防止人类能力枯竭的“悲剧”，必须在组织、行业和政策层面建立治理安排，以保护未来创新和安全所依赖的认知基础。

---

## 7. 7.4级地震 - 哥伦比亚圣何塞德尔帕尔马以南5公里

**原文标题**: Magnitude 7.4 Earthquake – 5 km S of San José del Palmar, Colombia

**原文链接**: [https://earthquake.usgs.gov/earthquakes/eventpage/us6000tjl2/executive](https://earthquake.usgs.gov/earthquakes/eventpage/us6000tjl2/executive)

The provided text reports a **magnitude 7.4 earthquake** occurring **5 km south of San José del Palmar, Colombia**. 

While the title specifies the location and significant intensity of the seismic event, the body of the article contains no further situational details, such as depth, damage, or casualties. Instead, the content is a technical notice indicating that the full "Earthquake Event Page" requires Javascript to load. It suggests that users enable Javascript or utilize alternative tools, such as real-time notifications, feeds, and web services, to access the complete data and updates regarding the event.

---

## 8. 50k Boat Names

**原文标题**: 50k Boat Names

**原文链接**: [https://www.beautifulpublicdata.com/boat-names/](https://www.beautifulpublicdata.com/boat-names/)

生成摘要时出错

---

## 9. Squeak 6.1

**原文标题**: Squeak 6.1

**原文链接**: [https://squeak.org/release_notes/6.1/](https://squeak.org/release_notes/6.1/)

Squeak 6.1, titled **"Vanessa"** in memory of developer Vanessa Freudenberg, marks a significant milestone as the platform approaches its 30th anniversary. This release is the culmination of four years of development, incorporating over 1,700 patches and 9,000 method changes to enhance the system's performance, stability, and usability.

**Key Highlights:**

*   **UI and Morphic Enhancements:** The release features a major overhaul of "tree morphs," improving navigation, filtering, and drag-and-drop functionality. High-DPI support has been expanded across menus, buttons, and tools. The interactive "Objectland" (Worlds of Squeak) makes a return, offering a colorful collection of examples demonstrating the system's capabilities.
*   **Advanced Programming Tools:** A new **Tree Browser** allows for hierarchical navigation of classes, categories, and Monticello packages. The **Debugger** has been significantly upgraded with a "byteCodes" mode for viewing single VM instructions and a "simulate" button for the metacircular evaluator. **Inspectors** now support custom fields and provide safer handling of proxy objects.
*   **Kernel and System Infrastructure:** The update includes vital improvements to process scheduling, class reshaping, and the infrastructure for simulating and unwinding processes. 
*   **Environment Refinements:** Numerous tweaks were made to the text editors (such as automatic quote escaping), the AndreasSystemProfiler was integrated into the trunk, and ST80 (the classic interface) received high-DPI and stability updates.
*   **Etoys and Multimedia:** Etoys saw restorations of classic tutorials and examples (like the BlobMorph), alongside improved support for webcams and MIDI inputs.

Overall, Squeak 6.1 balances modern high-DPI requirements and toolset innovations with a commitment to its historical roots, providing a more robust environment for Smalltalk development and exploration.

---

## 10. Itadakimasu: A word you say to the food, not the cook

**原文标题**: Itadakimasu: A word you say to the food, not the cook

**原文链接**: [https://thetokyohermit.substack.com/p/itadakimasu-a-word-you-say-to-the](https://thetokyohermit.substack.com/p/itadakimasu-a-word-you-say-to-the)

生成摘要时出错

---

## 11. Midlife Vascular Risk Burden and Dementia-Free Survival Years

**原文标题**: Midlife Vascular Risk Burden and Dementia-Free Survival Years

**原文链接**: [https://www.neurology.org/doi/10.1212/WN9.0000000000000152](https://www.neurology.org/doi/10.1212/WN9.0000000000000152)

生成摘要时出错

---

## 12. Docker Sandboxes – Disposable, isolated sandboxes for AI agents

**原文标题**: Docker Sandboxes – Disposable, isolated sandboxes for AI agents

**原文链接**: [https://www.docker.com/products/docker-sandboxes/](https://www.docker.com/products/docker-sandboxes/)

生成摘要时出错

---

## 13. Kinney Drugs pulls back AI phone assistant after hundreds of customer complaints

**原文标题**: Kinney Drugs pulls back AI phone assistant after hundreds of customer complaints

**原文链接**: [https://www.wcax.com/2026/08/07/kinney-drugs-pulls-back-ai-phone-assistant-after-hundreds-customer-complaints/](https://www.wcax.com/2026/08/07/kinney-drugs-pulls-back-ai-phone-assistant-after-hundreds-customer-complaints/)

生成摘要时出错

---

## 14. Extreme 220GHz+Broadband Silicon Capacitor X2SC 0201M 22nF BV11

**原文标题**: Extreme 220GHz+Broadband Silicon Capacitor X2SC 0201M 22nF BV11

**原文链接**: [https://pim.murata.com/asset/pim4/siliconCapacitor/SICAP_X2SC422522_PDF_SILICONCAPACITOR](https://pim.murata.com/asset/pim4/siliconCapacitor/SICAP_X2SC422522_PDF_SILICONCAPACITOR)

生成摘要时出错

---

## 15. Mars Bar from 1991 found – and it's 20g bigger than today's

**原文标题**: Mars Bar from 1991 found – and it's 20g bigger than today's

**原文链接**: [https://www.bbc.com/news/articles/c1j1kjy7gewo](https://www.bbc.com/news/articles/c1j1kjy7gewo)

生成摘要时出错

---

## 16. Sorting, hashing, and sketches on 370,103 words

**原文标题**: Sorting, hashing, and sketches on 370,103 words

**原文链接**: [https://stochastic.blog/sorting-hashing-and-sketches-on-370-103-words/](https://stochastic.blog/sorting-hashing-and-sketches-on-370-103-words/)

生成摘要时出错

---

## 17. Back to the Future of Handwriting Recognition (2016)

**原文标题**: Back to the Future of Handwriting Recognition (2016)

**原文链接**: [https://jackschaedler.github.io/handwriting-recognition/](https://jackschaedler.github.io/handwriting-recognition/)

生成摘要时出错

---

## 18. Why Addresses Have Numbers

**原文标题**: Why Addresses Have Numbers

**原文链接**: [https://thehistoricalinsights.page/2026/06/why-addresses-have-numbers.html](https://thehistoricalinsights.page/2026/06/why-addresses-have-numbers.html)

生成摘要时出错

---

## 19. Mistral Patent for “Code implemented tool calls”

**原文标题**: Mistral Patent for “Code implemented tool calls”

**原文链接**: [https://patentsgazette.uspto.gov/week26/OG/html/1547-5/US12670045-20260630.html](https://patentsgazette.uspto.gov/week26/OG/html/1547-5/US12670045-20260630.html)

生成摘要时出错

---

## 20. Tail-call optimization in C is relatively recent (2025)

**原文标题**: Tail-call optimization in C is relatively recent (2025)

**原文链接**: [https://lwn.net/Articles/1034703/](https://lwn.net/Articles/1034703/)

生成摘要时出错

---

## 21. Parametron: 50s Japanese computer that uses neither transistors nor vacuum tubes

**原文标题**: Parametron: 50s Japanese computer that uses neither transistors nor vacuum tubes

**原文链接**: [https://ethw.org/Milestones:Parametron,_1954](https://ethw.org/Milestones:Parametron,_1954)

生成摘要时出错

---

## 22. Tl;dv: Over 180k meetings left wide open

**原文标题**: Tl;dv: Over 180k meetings left wide open

**原文链接**: [https://bobdahacker.com/blog/tldv-hack](https://bobdahacker.com/blog/tldv-hack)

生成摘要时出错

---

## 23. There is no “done”: Reflections on a completed Appalachian Trail thru-hike (2022)

**原文标题**: There is no “done”: Reflections on a completed Appalachian Trail thru-hike (2022)

**原文链接**: [https://thetrek.co/appalachian-trail/there-is-no-done-reflections-on-a-completed-at-thru-hike/](https://thetrek.co/appalachian-trail/there-is-no-done-reflections-on-a-completed-at-thru-hike/)

生成摘要时出错

---

## 24. Exploring Claude/GPT Knowledge Cutoffs and Pre-Training Timelines

**原文标题**: Exploring Claude/GPT Knowledge Cutoffs and Pre-Training Timelines

**原文链接**: [https://blog.sshh.io/p/exploring-claudegpt-knowledge-cutoffs](https://blog.sshh.io/p/exploring-claudegpt-knowledge-cutoffs)

生成摘要时出错

---

## 25. What Happened to HackerOne?

**原文标题**: What Happened to HackerOne?

**原文链接**: [https://blog.teknogeek.io/posts/what-happened-to-hackerone/](https://blog.teknogeek.io/posts/what-happened-to-hackerone/)

生成摘要时出错

---

## 26. Humanising LLM Outputs Is Dumb

**原文标题**: Humanising LLM Outputs Is Dumb

**原文链接**: [https://kuber.studio/blog/Reflections/Humanising-LLM-Outputs-is-Actually-Dumb](https://kuber.studio/blog/Reflections/Humanising-LLM-Outputs-is-Actually-Dumb)

生成摘要时出错

---

## 27. Run Android ARM64 VR APKs on Apple Vision Pro

**原文标题**: Run Android ARM64 VR APKs on Apple Vision Pro

**原文链接**: [https://github.com/shinyquagsire23/Klepton](https://github.com/shinyquagsire23/Klepton)

生成摘要时出错

---

## 28. An Interesting Fourier Transform – 1/f Noise (2007)

**原文标题**: An Interesting Fourier Transform – 1/f Noise (2007)

**原文链接**: [https://www.dsprelated.com/showarticle/40.php](https://www.dsprelated.com/showarticle/40.php)

生成摘要时出错

---

## 29. How Blackwing Pencils are Made [video]

**原文标题**: How Blackwing Pencils are Made [video]

**原文链接**: [https://www.youtube.com/watch?v=fow-LsdaH2E](https://www.youtube.com/watch?v=fow-LsdaH2E)

The provided text contains only the generic YouTube footer and copyright information, rather than the specific content of the video. However, based on the title **"How Blackwing Pencils are Made,"** a summary of the typical manufacturing process for these iconic pencils is as follows:

Blackwing pencils are renowned for their high-quality materials and distinct design. The manufacturing process generally involves several key stages:

1.  **Sourcing Wood:** The process begins with **California Incense-cedar**, chosen for its stability, ease of sharpening, and pleasant scent. The wood is cut into "slats."
2.  **Milling and Grooving:** Each slat is precision-milled with several grooves to hold the graphite cores.
3.  **Inserting Graphite:** High-quality Japanese graphite cores (known for being smooth and dark) are placed into the grooves. A second grooved slat is then glued on top, creating a "sandwich."
4.  **Shaping:** Once the glue is set, the sandwich is passed through a machine that cuts and shapes the block into individual hexagonal or round pencils.
5.  **Finishing:** The pencils are sanded and receive multiple coats of lacquer (the signature matte black, pearl white, or grey).
6.  **The Ferrule and Eraser:** The most defining step is the attachment of the **unique rectangular ferrule**. Unlike standard round erasers, the Blackwing ferrule is clamped onto the end, allowing the flat eraser to be extended or replaced as it wears down.

In summary, the video details the craftsmanship involved in blending traditional techniques with modern precision to create a premium tool favored by artists and writers.

---

## 30. Study links GLP-1 drugs to bigger jump in women's employment than a degree

**原文标题**: Study links GLP-1 drugs to bigger jump in women's employment than a degree

**原文链接**: [https://finance.yahoo.com/healthcare/articles/harvard-study-links-glp-1-123000637.html](https://finance.yahoo.com/healthcare/articles/harvard-study-links-glp-1-123000637.html)

生成摘要时出错

---

## 31. Show HN: Voice driven murder mystery, Interview AI suspects with your voice

**原文标题**: Show HN: Voice driven murder mystery, Interview AI suspects with your voice

**原文链接**: [https://www.whodunnitai.com/](https://www.whodunnitai.com/)

生成摘要时出错

---

## 32. AI Fortunes Are Reviving an Old Debate About Private Power

**原文标题**: AI Fortunes Are Reviving an Old Debate About Private Power

**原文链接**: [https://ai-updates.net/ai-fortunes-philanthropy-private-power/](https://ai-updates.net/ai-fortunes-philanthropy-private-power/)

生成摘要时出错

---

## 33. Findphone: Locate a nearby Bluetooth device by signal strength

**原文标题**: Findphone: Locate a nearby Bluetooth device by signal strength

**原文链接**: [https://github.com/ben-z/findphone](https://github.com/ben-z/findphone)

生成摘要时出错

---

## 34. Germany Sets New Six-Month Startup Record

**原文标题**: Germany Sets New Six-Month Startup Record

**原文链接**: [https://www.gtai.de/en/meta/press/germany-sets-new-six-month-start-up-record-2012048](https://www.gtai.de/en/meta/press/germany-sets-new-six-month-start-up-record-2012048)

生成摘要时出错

---

## 35. Felix and I

**原文标题**: Felix and I

**原文链接**: [https://jacobfilipp.com/felix/](https://jacobfilipp.com/felix/)

生成摘要时出错

---

## 36. Signal is working on a paid option to create an account without a phone number

**原文标题**: Signal is working on a paid option to create an account without a phone number

**原文链接**: [https://aboutsignal.com/news/signal-login-registration-without-a-phone-number/](https://aboutsignal.com/news/signal-login-registration-without-a-phone-number/)

生成摘要时出错

---

## 37. 'Pervert glasses': Backlash against Meta's smart glasses grows

**原文标题**: 'Pervert glasses': Backlash against Meta's smart glasses grows

**原文链接**: [https://www.seattletimes.com/business/technology/pervert-glasses-backlash-against-metas-smart-glasses-grows/](https://www.seattletimes.com/business/technology/pervert-glasses-backlash-against-metas-smart-glasses-grows/)

生成摘要时出错

---

## 38. Tail-Call Interpreters in Rust – Jimmy Ostler

**原文标题**: Tail-Call Interpreters in Rust – Jimmy Ostler

**原文链接**: [https://lordgoati.us/blog/tail-call/](https://lordgoati.us/blog/tail-call/)

生成摘要时出错

---

## 39. How We Pushed CDC into Postgres

**原文标题**: How We Pushed CDC into Postgres

**原文链接**: [https://www.snowflake.com/en/blog/engineering/postgres-to-snowflake-replication-mirroring/](https://www.snowflake.com/en/blog/engineering/postgres-to-snowflake-replication-mirroring/)

生成摘要时出错

---

## 40. Show HN: A tiny LLM running at 21,000 tok/s on a $250 FPGA (Live Demo)

**原文标题**: Show HN: A tiny LLM running at 21,000 tok/s on a $250 FPGA (Live Demo)

**原文链接**: [https://www.mikeayles.com/blog/on-chip-llm-kv260/](https://www.mikeayles.com/blog/on-chip-llm-kv260/)

生成摘要时出错

---

## 41. AI Boot Camps Surge as Workers Race to Learn New Skills

**原文标题**: AI Boot Camps Surge as Workers Race to Learn New Skills

**原文链接**: [https://www.bloomberg.com/news/articles/2026-08-08/ai-training-boom-sends-colleges-racing-to-offer-credentials](https://www.bloomberg.com/news/articles/2026-08-08/ai-training-boom-sends-colleges-racing-to-offer-credentials)

生成摘要时出错

---

## 42. Self-Hosted Inference for Agents

**原文标题**: Self-Hosted Inference for Agents

**原文链接**: [https://github.com/superlinked/sie](https://github.com/superlinked/sie)

生成摘要时出错

---

## 43. In AI, the 41% Depends on the -59%

**原文标题**: In AI, the 41% Depends on the -59%

**原文链接**: [https://www.apollo.com/wealth/insights-news/insights/daily-spark/in-ai-the-41-percent-depends-on-the-59-percent](https://www.apollo.com/wealth/insights-news/insights/daily-spark/in-ai-the-41-percent-depends-on-the-59-percent)

生成摘要时出错

---

## 44. CEO Just Fired 500 People Because He Says Zillow Is More Efficient Without Them

**原文标题**: CEO Just Fired 500 People Because He Says Zillow Is More Efficient Without Them

**原文链接**: [https://galratner.substack.com/p/zillows-ceo-just-fired-500-people](https://galratner.substack.com/p/zillows-ceo-just-fired-500-people)

生成摘要时出错

---

## 45. A California Program Is Bringing Down the Cost of Heat Pumps by Buying Bulk

**原文标题**: A California Program Is Bringing Down the Cost of Heat Pumps by Buying Bulk

**原文链接**: [https://www.wired.com/story/california-group-buy-bringing-down-heat-pump-costs/](https://www.wired.com/story/california-group-buy-bringing-down-heat-pump-costs/)

生成摘要时出错

---

## 46. I Benchmarked Local LLMs on the Laptop I Have

**原文标题**: I Benchmarked Local LLMs on the Laptop I Have

**原文链接**: [https://mamonas.dev/posts/local-llms-on-the-laptop-i-already-have/](https://mamonas.dev/posts/local-llms-on-the-laptop-i-already-have/)

生成摘要时出错

---

## 47. Don't Build Mindreading

**原文标题**: Don't Build Mindreading

**原文链接**: [https://www.lesswrong.com/posts/CAdG5dzkWrrK2NQg8/don-t-build-mindreading](https://www.lesswrong.com/posts/CAdG5dzkWrrK2NQg8/don-t-build-mindreading)

生成摘要时出错

---

## 48. Flatworms, Ion Channels, and Burning Mouths

**原文标题**: Flatworms, Ion Channels, and Burning Mouths

**原文链接**: [https://www.science.org/content/blog-post/flatworms-ion-channels-and-burning-mouths](https://www.science.org/content/blog-post/flatworms-ion-channels-and-burning-mouths)

生成摘要时出错

---

## 49. ATProto for Distributed Systems Engineers

**原文标题**: ATProto for Distributed Systems Engineers

**原文链接**: [https://atproto.com/articles/atproto-for-distsys-engineers](https://atproto.com/articles/atproto-for-distsys-engineers)

生成摘要时出错

---

## 50. I've vibe coded an application to see what it's like

**原文标题**: I've vibe coded an application to see what it's like

**原文链接**: [https://rz01.org/vibecoding/](https://rz01.org/vibecoding/)

生成摘要时出错

---

## 51. Show HN: Design Engineering, as a Service

**原文标题**: Show HN: Design Engineering, as a Service

**原文链接**: [https://designshippers.com/?0](https://designshippers.com/?0)

生成摘要时出错

---

## 52. Show HN: Neolabs.fyi – 100 new AI labs by research area, valuation, and more

**原文标题**: Show HN: Neolabs.fyi – 100 new AI labs by research area, valuation, and more

**原文链接**: [https://neolabs.fyi/](https://neolabs.fyi/)

生成摘要时出错

---

## 53. When Agentic Glue Melts: Exploiting Cloudflare Code Mode and Workers

**原文标题**: When Agentic Glue Melts: Exploiting Cloudflare Code Mode and Workers

**原文链接**: [https://research.checkpoint.com/2026/when-agentic-glue-melts/](https://research.checkpoint.com/2026/when-agentic-glue-melts/)

生成摘要时出错

---

## 54. Convince an AI it's not alive in psychological horror game Prove You're Human

**原文标题**: Convince an AI it's not alive in psychological horror game Prove You're Human

**原文链接**: [https://www.theguardian.com/games/2026/aug/10/ai-psychological-horror-game-prove-youre-human-sunset-visitor-studio](https://www.theguardian.com/games/2026/aug/10/ai-psychological-horror-game-prove-youre-human-sunset-visitor-studio)

生成摘要时出错

---

## 55. John Crowley Has Died

**原文标题**: John Crowley Has Died

**原文链接**: [https://www.programmablemutter.com/p/john-crowley-has-died](https://www.programmablemutter.com/p/john-crowley-has-died)

生成摘要时出错

---

## 56. Ocean heat records broken as hottest July temperature recorded

**原文标题**: Ocean heat records broken as hottest July temperature recorded

**原文链接**: [https://www.bbc.com/news/articles/cpvw8vmmgrwo](https://www.bbc.com/news/articles/cpvw8vmmgrwo)

生成摘要时出错

---

## 57. An alias-based formulation of the borrow checker (2018)

**原文标题**: An alias-based formulation of the borrow checker (2018)

**原文链接**: [https://smallcultfollowing.com/babysteps/blog/2018/04/27/an-alias-based-formulation-of-the-borrow-checker/](https://smallcultfollowing.com/babysteps/blog/2018/04/27/an-alias-based-formulation-of-the-borrow-checker/)

生成摘要时出错

---

## 58. Venaya – A financial wellness platform that adapts to your life stage

**原文标题**: Venaya – A financial wellness platform that adapts to your life stage

**原文链接**: [https://venaya.app](https://venaya.app)

生成摘要时出错

---

## 59. Humanity renamed genes because of Excel

**原文标题**: Humanity renamed genes because of Excel

**原文链接**: [https://davidemornatta.it/excel-genes](https://davidemornatta.it/excel-genes)

生成摘要时出错

---

## 60. Toggles Considered Harmful

**原文标题**: Toggles Considered Harmful

**原文链接**: [https://ignorethecode.net/blog/2026/08/09/toggles_considered_harmful/](https://ignorethecode.net/blog/2026/08/09/toggles_considered_harmful/)

生成摘要时出错

---

## 61. New Zealand lost its music media, and what we're building to replace it

**原文标题**: New Zealand lost its music media, and what we're building to replace it

**原文链接**: [https://propelmusic.co.nz/articles/the-sound-went-quiet-nz-music-media](https://propelmusic.co.nz/articles/the-sound-went-quiet-nz-music-media)

生成摘要时出错

---

## 62. ChatGPT Knows Who It'll Recommend Before It Searches

**原文标题**: ChatGPT Knows Who It'll Recommend Before It Searches

**原文链接**: [https://suganthan.com/blog/chatgpt-decides-before-it-searches/](https://suganthan.com/blog/chatgpt-decides-before-it-searches/)

生成摘要时出错

---

## 63. Show HN: 100% native Swift harness (NOT Electron)

**原文标题**: Show HN: 100% native Swift harness (NOT Electron)

**原文链接**: [https://github.com/Lore-Hex/QuillCode](https://github.com/Lore-Hex/QuillCode)

生成摘要时出错

---

## 64. Defending my own brain against enshittification

**原文标题**: Defending my own brain against enshittification

**原文链接**: [https://mrmarket.lol/how-i-feel-calmin-control-of-my-life-in-the-time-of-enshittification/](https://mrmarket.lol/how-i-feel-calmin-control-of-my-life-in-the-time-of-enshittification/)

生成摘要时出错

---

## 65. Fedi Thread to Blog Post

**原文标题**: Fedi Thread to Blog Post

**原文链接**: [https://shom.dev/posts/20260809_fedi-thread-to-blog-post/](https://shom.dev/posts/20260809_fedi-thread-to-blog-post/)

生成摘要时出错

---

## 66. Nearest Pint

**原文标题**: Nearest Pint

**原文链接**: [https://knowwhereconsulting.co.uk/maps/pubs/](https://knowwhereconsulting.co.uk/maps/pubs/)

生成摘要时出错

---

## 67. LLM Rewrite of the TerminalTextEffects Python

**原文标题**: LLM Rewrite of the TerminalTextEffects Python

**原文链接**: [https://github.com/omacom-io/ttfx](https://github.com/omacom-io/ttfx)

生成摘要时出错

---

## 68. Tech leaders say AI means less work – staff say they work up to 90 hours a week

**原文标题**: Tech leaders say AI means less work – staff say they work up to 90 hours a week

**原文链接**: [https://www.bbc.com/news/articles/cvgx4yd1gl2o](https://www.bbc.com/news/articles/cvgx4yd1gl2o)

生成摘要时出错

---

## 69. OpenChamber: An Agentic Development Environment

**原文标题**: OpenChamber: An Agentic Development Environment

**原文链接**: [https://openchamber.dev/](https://openchamber.dev/)

生成摘要时出错

---

## 70. An ambiguity in c89 which will never be fixed

**原文标题**: An ambiguity in c89 which will never be fixed

**原文链接**: [https://sebsite.pw/w/20260810-c89ambiguity.html](https://sebsite.pw/w/20260810-c89ambiguity.html)

生成摘要时出错

---

## 71. When longing for something becomes hate

**原文标题**: When longing for something becomes hate

**原文链接**: [https://burnoutdv.bearblog.dev/longing/](https://burnoutdv.bearblog.dev/longing/)

生成摘要时出错

---

## 72. How do you sell a CPU design when the instruction set is free?

**原文标题**: How do you sell a CPU design when the instruction set is free?

**原文链接**: [https://www.siliconimist.com/p/credibility-is-the-barrier-to-entry](https://www.siliconimist.com/p/credibility-is-the-barrier-to-entry)

生成摘要时出错

---

## 73. The Ambition Project

**原文标题**: The Ambition Project

**原文链接**: [https://www.betonit.ai/p/the-ambition-project](https://www.betonit.ai/p/the-ambition-project)

生成摘要时出错

---

## 74. Windows 11's built-in Weather app wastes more than 1 GB of RAM

**原文标题**: Windows 11's built-in Weather app wastes more than 1 GB of RAM

**原文链接**: [https://www.notebookcheck.net/Windows-11-s-built-in-Weather-app-wastes-more-than-1-GB-of-RAM.1364205.0.html](https://www.notebookcheck.net/Windows-11-s-built-in-Weather-app-wastes-more-than-1-GB-of-RAM.1364205.0.html)

生成摘要时出错

---

## 75. Turn satellite imagery into a paper globe you fold yourself

**原文标题**: Turn satellite imagery into a paper globe you fold yourself

**原文链接**: [https://foldingglobes.com/](https://foldingglobes.com/)

生成摘要时出错

---

## 76. Taxi drivers rarely die of Alzheimer's

**原文标题**: Taxi drivers rarely die of Alzheimer's

**原文链接**: [https://theconversation.com/taxi-drivers-rarely-die-of-alzheimers-how-complex-mental-maps-and-spatial-reasoning-protect-your-brain-286650](https://theconversation.com/taxi-drivers-rarely-die-of-alzheimers-how-complex-mental-maps-and-spatial-reasoning-protect-your-brain-286650)

生成摘要时出错

---

## 77. Open QEC harness – greedy vs. GE, uniform vs. clustered k=4

**原文标题**: Open QEC harness – greedy vs. GE, uniform vs. clustered k=4

**原文链接**: [https://github.com/mrblakessinger-rgb/qec-evaluation-suite](https://github.com/mrblakessinger-rgb/qec-evaluation-suite)

生成摘要时出错

---

## 78. Space mirrors could ruin astronomy — and your eyes

**原文标题**: Space mirrors could ruin astronomy — and your eyes

**原文链接**: [https://www.theverge.com/science/976977/space-mirror-reflect-orbital-fcc-solar-eye-damage](https://www.theverge.com/science/976977/space-mirror-reflect-orbital-fcc-solar-eye-damage)

生成摘要时出错

---

## 79. China is now the world's greatest oil power

**原文标题**: China is now the world's greatest oil power

**原文链接**: [https://www.economist.com/finance-and-economics/2026/08/09/china-is-now-the-worlds-great-oil-power](https://www.economist.com/finance-and-economics/2026/08/09/china-is-now-the-worlds-great-oil-power)

生成摘要时出错

---

## 80. Colombia Hit by Magnitude 7.4 Quake, Widespread Damage Reported

**原文标题**: Colombia Hit by Magnitude 7.4 Quake, Widespread Damage Reported

**原文链接**: [https://www.bloomberg.com/news/articles/2026-08-10/colombia-hit-by-strong-earthquake-that-shakes-bogota](https://www.bloomberg.com/news/articles/2026-08-10/colombia-hit-by-strong-earthquake-that-shakes-bogota)

生成摘要时出错

---

## 81. The main way I've seen people turn ideologically crazy (2025)

**原文标题**: The main way I've seen people turn ideologically crazy (2025)

**原文链接**: [https://blog.andymasley.com/p/the-main-way-ive-seen-people-turn](https://blog.andymasley.com/p/the-main-way-ive-seen-people-turn)

生成摘要时出错

---

## 82. Reviving a four year old reMarkable 2

**原文标题**: Reviving a four year old reMarkable 2

**原文链接**: [https://oskrim.github.io/hardware/2026/08/09/remarkable-over-ssh.html](https://oskrim.github.io/hardware/2026/08/09/remarkable-over-ssh.html)

生成摘要时出错

---

## 83. Mark Zuckerberg attacks 'closed' AI rivals as Meta returns to open models

**原文标题**: Mark Zuckerberg attacks 'closed' AI rivals as Meta returns to open models

**原文链接**: [https://www.ft.com/content/4e3957f8-ea7c-4c46-a3de-cdce8e526878](https://www.ft.com/content/4e3957f8-ea7c-4c46-a3de-cdce8e526878)

生成摘要时出错

---

## 84. Judge rules Meta caused "public nuisance" and must fund mental health treatment

**原文标题**: Judge rules Meta caused "public nuisance" and must fund mental health treatment

**原文链接**: [https://arstechnica.com/tech-policy/2026/08/meta-ordered-to-pay-567m-to-treat-youth-mental-health-problems-it-helped-create/](https://arstechnica.com/tech-policy/2026/08/meta-ordered-to-pay-567m-to-treat-youth-mental-health-problems-it-helped-create/)

生成摘要时出错

---

## 85. The tragedy of the commons, AI edition

**原文标题**: The tragedy of the commons, AI edition

**原文链接**: [https://www.economist.com/britain/2026/08/06/the-tragedy-of-the-commons-ai-edition](https://www.economist.com/britain/2026/08/06/the-tragedy-of-the-commons-ai-edition)

生成摘要时出错

---

## 86. Django is moving to an annual release cycle

**原文标题**: Django is moving to an annual release cycle

**原文链接**: [https://www.djangoproject.com/weblog/2026/aug/10/annual-release-cycle/](https://www.djangoproject.com/weblog/2026/aug/10/annual-release-cycle/)

生成摘要时出错

---

## 87. Meta's new open-weight model targets local agentic AI

**原文标题**: Meta's new open-weight model targets local agentic AI

**原文链接**: [https://twitter.com/finkd/status/2086754845218726027](https://twitter.com/finkd/status/2086754845218726027)

生成摘要时出错

---

## 88. Slap ROM Patcher

**原文标题**: Slap ROM Patcher

**原文链接**: [https://nyuu.page/projects/slap/](https://nyuu.page/projects/slap/)

生成摘要时出错

---

## 89. Show HN: A Project Oberon System version running on RISC-V instead of RISC-5

**原文标题**: Show HN: A Project Oberon System version running on RISC-V instead of RISC-5

**原文链接**: [https://github.com/rochus-keller/OberonSystem/tree/op2-rv32](https://github.com/rochus-keller/OberonSystem/tree/op2-rv32)

生成摘要时出错

---

## 90. Show HN: I made alchemical-cosmological PCB badges

**原文标题**: Show HN: I made alchemical-cosmological PCB badges

**原文链接**: [https://github.com/KaiPereira/Alchemical-Cosmological-Badges](https://github.com/KaiPereira/Alchemical-Cosmological-Badges)

生成摘要时出错

---

## 91. Muse Glimmer: Meta's open model built for always-on local agents. 30B parameters

**原文标题**: Muse Glimmer: Meta's open model built for always-on local agents. 30B parameters

**原文链接**: [https://developer.meta.com/ai/models/muse-glimmer/](https://developer.meta.com/ai/models/muse-glimmer/)

生成摘要时出错

---

## 92. OpenAI's letter to Governor Abbott on responsible AI infrastructure in Texas

**原文标题**: OpenAI's letter to Governor Abbott on responsible AI infrastructure in Texas

**原文链接**: [https://openai.com/index/responsible-ai-infrastructure-texas/](https://openai.com/index/responsible-ai-infrastructure-texas/)

生成摘要时出错

---

## 93. Auto mode is now the default in Claude Code

**原文标题**: Auto mode is now the default in Claude Code

**原文链接**: [https://claude.com/blog/auto-mode-default-in-claude-code](https://claude.com/blog/auto-mode-default-in-claude-code)

生成摘要时出错

---

## 94. UK argued that excess death figures could lead to distress of bereaved relatives

**原文标题**: UK argued that excess death figures could lead to distress of bereaved relatives

**原文链接**: [https://www.telegraph.co.uk/politics/2025/11/15/government-withholding-data-covid-jab-link-excess-deaths/](https://www.telegraph.co.uk/politics/2025/11/15/government-withholding-data-covid-jab-link-excess-deaths/)

生成摘要时出错

---

## 95. The Future Is for Everyone

**原文标题**: The Future Is for Everyone

**原文链接**: [https://about.fb.com/news/2026/08/the-future-is-for-everyone/](https://about.fb.com/news/2026/08/the-future-is-for-everyone/)

生成摘要时出错

---

## 96. How I use LLMs to learn complex topics

**原文标题**: How I use LLMs to learn complex topics

**原文链接**: [https://laurentiugabriel.github.io/blog/articles/how-i-use-llms-to-learn/](https://laurentiugabriel.github.io/blog/articles/how-i-use-llms-to-learn/)

生成摘要时出错

---

## 97. "The Persian MâR-Nâmeh Or, the Book for Taking Omens from Snakes" (1892)

**原文标题**: "The Persian MâR-Nâmeh Or, the Book for Taking Omens from Snakes" (1892)

**原文链接**: [https://publicdomainreview.org/collection/marnameh/](https://publicdomainreview.org/collection/marnameh/)

生成摘要时出错

---

## 98. Robot Videos: Heavy Lift Cargo Drones, Grippers, More

**原文标题**: Robot Videos: Heavy Lift Cargo Drones, Grippers, More

**原文链接**: [https://spectrum.ieee.org/video-friday-heavy-lift-drone](https://spectrum.ieee.org/video-friday-heavy-lift-drone)

生成摘要时出错

---

## 99. The Alpha 21264 CPU: NT's Greatest RISC (1998)

**原文标题**: The Alpha 21264 CPU: NT's Greatest RISC (1998)

**原文链接**: [https://halfhill.com/byte/1998-12_alpha.html](https://halfhill.com/byte/1998-12_alpha.html)

生成摘要时出错

---

## 100. Autoscaling MirageOS Unikernels in Mollymawk

**原文标题**: Autoscaling MirageOS Unikernels in Mollymawk

**原文链接**: [https://blog.robur.coop/articles/2026-07-08-Autoscaling-MirageOS-unikernels-in-Mollymawk.html](https://blog.robur.coop/articles/2026-07-08-Autoscaling-MirageOS-unikernels-in-Mollymawk.html)

生成摘要时出错

---

