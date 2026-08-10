# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-08-10.md)

*最后自动更新时间: 2026-08-10 18:16:22*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 2 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 3 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 4 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 5 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 6 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 7 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 8 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 9 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 10 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 11 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 12 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 13 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 14 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 15 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 16 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 17 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 18 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 19 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 20 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 21 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 22 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 23 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 24 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 25 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 26 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 27 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 28 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 29 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 30 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 31 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 32 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 33 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 34 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 35 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 36 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 37 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 38 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 39 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 40 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 41 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 42 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 43 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 44 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 45 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 46 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 47 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 48 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 49 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 50 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 51 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 52 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 53 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 54 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 55 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 56 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 57 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 58 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 59 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 60 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 61 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 62 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 63 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 64 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 65 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 66 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 67 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 68 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 69 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 70 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 71 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 72 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 73 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 74 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 75 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 76 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 77 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 78 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 79 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 80 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 81 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 82 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 83 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 84 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 85 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 86 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 87 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 88 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 89 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 90 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 91 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 92 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 93 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 94 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 95 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 96 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 97 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 98 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 99 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 100 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 101 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 102 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 103 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 104 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 105 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 106 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 107 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 108 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 109 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 110 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 111 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 112 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 113 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 114 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 115 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 116 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 117 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 118 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 119 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 120 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 121 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 122 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 123 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 124 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 125 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 126 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 127 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 128 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 129 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 130 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 131 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 132 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 133 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 134 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 135 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 136 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 137 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 138 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 139 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 140 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 141 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 142 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 143 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 144 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 145 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 146 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 147 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 148 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 149 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 150 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 151 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 152 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 153 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 154 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 155 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 156 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 157 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 158 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 159 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 160 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 161 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 162 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 163 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 164 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 165 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 166 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 167 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 168 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 169 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 170 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 171 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 172 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 173 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 174 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 175 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 176 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 177 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 178 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 179 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 180 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 181 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 182 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 183 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 184 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 185 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 186 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 187 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 188 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 189 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 190 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 191 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 192 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 193 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 194 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 195 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 196 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 197 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 198 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 199 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 200 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 201 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 202 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 203 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 204 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 205 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 206 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 207 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 208 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 209 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 210 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 211 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 212 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 213 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 214 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 215 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 216 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 217 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 218 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 219 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 220 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 221 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 222 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 223 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 224 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 225 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 226 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 227 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 228 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 229 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 230 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 231 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 232 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 233 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 234 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 235 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 236 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 237 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 238 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 239 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 240 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 241 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 242 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 243 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 244 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 245 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 246 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 247 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 248 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 249 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 250 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 251 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 252 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 253 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 254 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 255 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 256 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 257 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 258 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 259 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 260 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 261 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 262 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 263 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 264 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 265 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 266 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 267 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 268 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 269 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 270 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 271 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 272 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 273 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 274 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 275 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 276 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 277 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 278 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 279 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 280 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 281 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 282 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 283 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 284 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 285 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 286 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 287 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 288 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 289 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 290 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 291 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 292 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 293 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 294 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 295 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 296 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 297 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 298 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 299 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 300 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 301 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 302 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 303 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 304 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 305 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 306 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 307 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 308 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 309 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 310 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 311 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 312 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 313 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 314 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 315 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 316 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 317 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 318 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 319 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 320 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 321 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 322 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 323 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 324 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 325 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 326 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 327 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 328 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 329 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 330 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 331 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 332 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 333 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 334 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 335 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 336 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 337 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 338 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 339 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 340 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 341 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 342 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 343 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 344 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 345 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 346 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 347 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 348 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 349 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 350 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 351 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 352 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 353 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 354 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 355 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 356 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 357 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 358 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 359 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 360 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 361 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 362 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 363 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 364 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 365 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 366 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 367 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 368 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 369 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 370 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 371 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 372 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 373 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 374 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 375 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 376 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 377 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 378 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 379 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 380 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 381 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 382 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 383 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 384 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 385 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 386 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 387 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 388 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 389 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 390 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 391 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 392 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 393 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 394 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 395 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 396 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 397 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 398 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 399 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 400 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 401 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 402 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 403 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 404 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 405 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 406 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 407 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 408 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 409 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 410 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 411 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 412 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 413 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 414 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 415 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 416 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 417 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 418 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 419 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 420 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 421 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 422 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 423 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 424 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 425 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 426 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 427 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 428 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 429 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 430 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 431 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 432 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 433 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 434 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 435 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 436 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 437 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 438 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 439 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 440 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 441 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 442 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 443 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 444 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 445 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 446 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 447 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 448 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 449 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 450 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 451 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 452 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 453 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 454 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 455 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 456 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 457 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 458 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 459 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 460 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 461 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 462 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 463 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 464 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 465 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 466 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 467 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 468 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 469 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 470 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 471 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 472 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 473 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 474 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 475 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 476 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 477 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 478 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 479 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 480 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 481 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 482 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 483 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 484 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 485 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 486 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 487 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 488 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 489 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 490 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 491 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 492 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 493 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 494 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 495 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 496 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 497 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 498 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 499 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 500 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 501 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 502 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 503 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 504 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 505 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 506 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 507 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
