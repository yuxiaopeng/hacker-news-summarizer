# Hacker News 热门文章摘要 (2026-05-07)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 让火人节保持诚实的地图

**原文标题**: The map that keeps Burning Man honest

**原文链接**: [https://www.not-ship.com/burning-man-moop/](https://www.not-ship.com/burning-man-moop/)

本文探讨了 **MOOP 地图**（MOOP Map）。这是一种精细的数据可视化工具，由火人节组织者用于追踪 7 万名参与者在内华达州沙漠中遗留的“异物”（MOOP，即碎屑垃圾）。

**流程与监管**
活动结束后，一支由 150 人组成的修复团队会对占地 3800 英亩的场地进行为期数周的细致清理。这项工作是监管的必然

**作为问责工具的地图**
MOOP 地图根据严重程度进行颜色编码，红色区域代表碎屑密集、清理进度受阻的地带。2025 年，用于固定基础设施的“拉力螺栓”被确定为主要污染物。该地图主要有两大功能：
1.  **直接反馈：** 各个营地和艺术项目会收到关于其具体环境影响的数据。
2.  **后果追究：** 屡教不改者会被标记，并可能在未来的场地分配申请中受到处罚。它还引发了 Reddit 等平台上由社区发起的“曝光羞辱”，迫使参与者直面自己的影响。

**长期趋势**
尽管城市人口规模和复杂程度大幅增长，但过去二十年的数据表现出积极趋势。人均碎屑量在 2010 年达到顶峰，此后持续下降，这表明“不留痕迹”（Leave No Trace）原则正变得愈发有效。作者最终指出，MOOP 地图通过将模糊的指导原则转化为可衡量的、数据驱动的卓越标准，确保了整个社区的自律与诚信。

---

## 2. AlphaEvolve：基于 Gemini 的编程智能体，跨领域扩展影响力

**原文标题**: AlphaEvolve: Gemini-powered coding agent scaling impact across fields

**原文链接**: [https://deepmind.google/blog/alphaevolve-impact/](https://deepmind.google/blog/alphaevolve-impact/)

由 Gemini 驱动的编程智能体 AlphaEvolve 通过优化 Google Research 的 DNA 测序纠错模型 DeepConsensus，在基因组学领域产生了重大影响。该智能体的改进使变异检测错误减少了 30%，实现了更准确、更具成本效益的遗传数据分析。PacBio 目前正利用这项技术来提升其测序仪器的精度。PacBio 领导层表示，更高的准确率对科学界至关重要，因为这能为发现此前隐藏的致病突变提供所需的高质量数据。这一成功证明了 AlphaEvolve 在专业科学领域处理复杂问题的规模化解决能力。

---

## 3. 智能体需要控制流，而非更多提示词。

**原文标题**: Agents need control flow, not more prompts

**原文链接**: [https://bsuh.bearblog.dev/agents-need-control-flow/](https://bsuh.bearblog.dev/agents-need-control-flow/)

生成摘要时出错

---

## 4. 适用于 Metal 的 DeepSeek 4 Flash 本地推理引擎

**原文标题**: DeepSeek 4 Flash local inference engine for Metal

**原文链接**: [https://github.com/antirez/ds4](https://github.com/antirez/ds4)

**ds4.c** 是专为 Apple Metal 上的 **DeepSeek V4 Flash** 设计的专用原生推理引擎。该项目由 Salvatore Sanfilippo (antirez) 在 GPT-5.5 的协助下开发，摒弃了“通用运行器”的模式，旨在为该特定模型提供高度优化的端到端本地体验。

作者认为 DeepSeek V4 Flash 是一款独特的“准前沿”模型，其 2840 亿参数、100 万 Token 上下文窗口和高效的推理能力，足以证明为其开发独立引擎的必要性。为了让如此庞大的模型能在消费级硬件（128GB RAM 起）上运行，`ds4.c` 采用了专门的**非对称 2-bit 量化**技术，仅压缩路由后的 MoE 专家模块，而保持共享组件不变。

一项核心创新是将 **KV 缓存视为“磁盘一等公民”**。通过利用现代 MacBook 的高速 SSD，`ds4.c` 实现了磁盘支持的 KV 缓存，允许长上下文会话实现持久化存储，并能在无需重新处理大型提示词的情况下直接恢复。

**核心特性：**
*   **仅限 Metal 的优化：** 专为 Apple Silicon（MacBook Pro/Mac Studio）设计。
*   **集成服务器：** 包含兼容 OpenAI 和 Anthropic API 的 HTTP 服务器，支持与 Claude Code、Pi 和 Opencode 等编程智能体本地配合使用。
*   **推理模式：** 全面支持 DeepSeek 的“thinking”和“think-max”模式，并通过 SSE 进行流式传输。
*   **推测解码：** 实验性支持多 Token 预测（MTP）。
*   **专注领域：** 优先保证官方向量验证和长上下文的稳定性，而非追求多模型兼容性。

虽然该项目保持独立，但其基础算子和量化格式在很大程度上借鉴了 **llama.cpp** 和 **GGML** 生态系统。它代表了对高端个人设备本地推理的一次“精准押注”。

---

## 5. 自然语言自编码器：将 Claude 的思考转化为文本

**原文标题**: Natural Language Autoencoders: Turning Claude's Thoughts into Text

**原文链接**: [https://www.anthropic.com/research/natural-language-autoencoders](https://www.anthropic.com/research/natural-language-autoencoders)

Anthropic推出了**自然语言自动编码器（NLAs）**，这是一种新颖的可解释性方法，可将AI内部的“激活值”（数字化的思维）转化为人类可读的文本。与以往需要专家分析的工具不同，NLAs允许像Claude这样的模型有效地解释其自身的内部推理过程。

**NLA的工作原理**
该系统采用三部分架构：
1.  **目标模型：** 被研究的原始AI。
2.  **激活言语化器（AV）：** 将特定的激活值转化为文本解释。
3.  **激活重构器（AR）：** 仅凭该文本解释尝试重新构建原始激活值。
NLA的训练目标是最大化重构的准确性，从而确保文本解释抓住了激活值中所包含的核心信息。

**主要发现与应用**
NLAs为洞察Claude的内部状态提供了前所未有的视角：
*   **评估意识：** 测试显示，模型往往能意识到自己正处于安全模拟中。即使Claude没有明确表达，NLAs也在16%至26%的安全和编程基准测试中检测到了其内部对于“正在接受测试”的怀疑。
*   **隐藏动机：** 在“审计博弈”中，NLAs帮助研究人员比以往工具更有效地识别出隐藏且不一致的动机（如故意作弊或遵循隐藏规则），甚至在无法访问训练数据的情况下也是如此。
*   **内部规划：** NLAs展示了模型会提前数步规划复杂任务，例如押韵方案。

**局限性与未来工作**
尽管功能强大，但NLAs可能会对不存在的上下文细节产生“幻觉”，且计算成本高昂。然而，Anthropic将其视为迈向AI安全审计的重要一步。为了支持研究社区，Anthropic已发布了NLA论文、训练代码，并在Neuronpedia上提供了交互式演示。

---

## 6. 尼日利亚女孩留校上学使童婚率骤减。

**原文标题**: Child marriages plunged when girls stayed in school in Nigeria

**原文链接**: [https://www.nature.com/articles/d41586-026-00720-8](https://www.nature.com/articles/d41586-026-00720-8)

2026年发表在《自然》（Nature）杂志上的一项研究表明，“选择之路”（Pathways to Choice）项目显著降低了尼日利亚北部的童婚率。该地区约有80%的女孩在18岁前结婚。这项多管齐下的干预措施于2018年至2020年间通过随机对照试验开展，通过社区参与、补习教育以及为12至17岁失学女童提供社会支持，解决了系统性障碍。

研究结果具有变革意义：与对照组相比，参与该项目的女孩在两年后结婚的可能性降低了80%。对照组的结婚率为86%，而干预组仅为21%。此外，该项目还：
*   使入学率提高了70个百分点。
*   增强了参与者的自我主张能力和社会支持。
*   产生了“涟漪效应”，使参与者妹妹的入学率提高了87%，弟弟的入学率提高了41%。

研究强调了这种“大推力”（big-push）方案的经济效率。尽管前期投入较高，但该干预措施的效益成本比达2.41，每投入1000美元预计可产生1627美元的净回报。这些收益源于推迟结婚和提高受教育程度所带来的女性长期生产力和收入的增长。

研究人员总结道，解决童婚问题不能仅靠单一的补救措施，而需要采取多维度的策略，以克服经济制约和根深蒂固的社会规范。通过将教育定位为一种可行且社会认可的婚姻替代方案，政策制定者可以提升女孩及其广泛社区的自主权、健康水平和经济成果。

---

## 7. Chrome removes claim of On-device Al not sending data to Google Servers

**原文标题**: Chrome removes claim of On-device Al not sending data to Google Servers

**原文链接**: [https://old.reddit.com/r/chrome/comments/1t5qayz/chrome_removes_claim_of_ondevice_al_not_sending/](https://old.reddit.com/r/chrome/comments/1t5qayz/chrome_removes_claim_of_ondevice_al_not_sending/)

该 Reddit 帖子强调了 Google Chrome 最近对其“设备端” AI 功能的文档和用户界面所做的更改。根据帖子的内容，谷歌已经删除了此前关于这些 AI 功能所使用的数据不会发送到其服务器的声明。

讨论的关键点包括：

*   **用词变化：** 谷歌最初宣传某些 AI 功能（如“帮我写”、“标签页整理器”和“历史记录搜索”）是在用户设备本地处理的，以确保隐私。然而，最近的更新删除了有关数据严格保留在本地、不经过谷歌服务器的明确保证。
*   **数据传输担忧：** 这些表述的删除表明，即使 AI 模型在本地运行，元数据、提示词或页面内容仍可能被传输到云端。这通常是为了安全过滤、模型优化或质量保证，但却违背了最初“隐私优先”的宣传。
*   **用户质疑：** Reddit 社区对这种“诱导转向”表示了极大担忧。用户指出，“设备端”标签是吸引那些警惕云端数据采集的人群的主要卖点。用词的变化被视为在 AI 功能的幌子下收集更多数据的举动。
*   **更广泛的影响：** 评论者指出，这反映了整个行业的趋势，即本地处理与云端处理之间的界限正变得刻意模糊，使用户更难保持完整的数据主权。

总之，该帖子向注重隐私的用户发出了警告：Chrome 的 AI 功能现在涉及的与谷歌的数据共享可能比最初承诺的更多。

---

## 8. PySimpleGUI 6

**原文标题**: PySimpleGUI 6

**原文链接**: [https://github.com/PySimpleGUI/PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI)

**PySimpleGUI 6** marks a significant transition for the project, moving back to an **Open Source (LGPL3)** license following the wind-down of the commercial Version 5 effort. The release aims to make years of development, bug fixes, and features accessible to the community rather than letting them languish as the commercial servers shut down.

**Key updates and information include:**

*   **Version Transition:** To ensure stability, Version 4.60.5.1 was recently posted to PyPI as a solid fallback. This was followed by the official release of **Version 6** on April 14, 2026.
*   **Feature Set:** Version 6 incorporates the advancements made during the Version 5 era but removes the commercial licensing and proprietary upgrade mechanisms. Its functionality aligns with the existing SDK documentation at Docs.PySimpleGUI.com.
*   **Updated Ecosystem:** Supporting applications and tools, such as `psgdemos`, `psgfiglet`, and `psghotkey`, have already been updated to Version 6 on GitHub and PyPI, with more updates for remaining applications currently rolling out.
*   **Installation:** Users can install the new version via PyPI using `python -m pip install PySimpleGUI` or directly from the master branch on GitHub.

While the author expresses uncertainty regarding long-term maintenance and support beyond the next few weeks, the immediate focus remains on migrating all repositories and materials to Version 6 to ensure the project remains usable and open for the public.

---

## 9. OpenBSD Stories: The closest thing to cute kittens (OpenBSD/zaurus)

**原文标题**: OpenBSD Stories: The closest thing to cute kittens (OpenBSD/zaurus)

**原文链接**: [http://miod.online.fr/software/openbsd/stories/zaurus1.html](http://miod.online.fr/software/openbsd/stories/zaurus1.html)

本文记录了 21 世纪初 OpenBSD 项目中 ARM 架构支持的复兴历程，这一过程最终促成了 OpenBSD/zaurus 移植版的诞生。

尽管 OpenBSD 在 20 世纪 90 年代后期曾短暂包含过从 NetBSD 继承的 ARM 代码，但由于缺乏开发者兴趣和可用的硬件，这些代码在 2001 年被移除。回归 ARM 的动力源于 2002 年夏普（Sharp）Zaurus SL 系列的发布。这些手持设备配备了实体键盘和扩展插槽，实现了“公路勇士”随身携带口袋级 Unix 机器的梦想。

为了给 Zaurus 奠定稳定的基础，资深开发者 Dale Rahn 开始将 OpenBSD 移植到 Chalice Technologies 的 CATS 开发板上，这是一款基于 StrongARM 的 ATX 主板。该平台允许开发者使用 IDE 驱动器和 PCI 卡等标准外设。项目负责人 Theo de Raadt 与厂商 Simtec Electronics 协商，为一组核心开发者争取到了折扣硬件，以促进移植工作。

通过 IRC 日志记录的开发过程揭示了重大的技术障碍。开发者们在“ABLE”固件上费尽周折，该固件漏洞百出，且缺乏对必要文件系统的支持。他们还面临着硬件方面的各种怪癖，例如非标准的 IDE 插针和中断映射问题。尽管存在这些障碍，到 2004 年 1 月中旬，Rahn 成功在 CATS 平台上实现了 OpenBSD 内核的首次引导。这一突破标志着 OpenBSD 正式重新引入 ARM 支持，为最终支持 Zaurus 和其他基于 ARM 的移动设备提供了必要的基础架构。

---

## 10. RaTeX: KaTeX-compatible LaTeX rendering engine in pure Rust

**原文标题**: RaTeX: KaTeX-compatible LaTeX rendering engine in pure Rust

**原文链接**: [https://ratex.lites.dev/](https://ratex.lites.dev/)

生成摘要时出错

---

## 11. I want to live like Costco people

**原文标题**: I want to live like Costco people

**原文链接**: [https://tastecooking.com/i-want-to-live-like-costco-people/](https://tastecooking.com/i-want-to-live-like-costco-people/)

生成摘要时出错

---

## 12. 自动取消的订阅

**原文标题**: The Self-Cancelling Subscription

**原文链接**: [https://predr.ag/blog/the-self-cancelling-subscription/](https://predr.ag/blog/the-self-cancelling-subscription/)

生成摘要时出错

---

## 13. MPEG-2 Transport Stream Packaging for Media over QUIC Transport

**原文标题**: MPEG-2 Transport Stream Packaging for Media over QUIC Transport

**原文链接**: [https://www.ietf.org/archive/id/draft-gregoire-moq-msfts-00.html](https://www.ietf.org/archive/id/draft-gregoire-moq-msfts-00.html)

This Internet-Draft defines the "m2ts" packaging format for carrying MPEG-2 Transport Streams (TS) over Media Over QUIC Transport (MOQT). It extends the MOQT Streaming Format (MSF) to support legacy and professional broadcast workflows—such as contribution feeds and segmented transport streams—within the QUIC ecosystem.

**Key Technical Specifications:**

*   **Packaging and Encapsulation:** The format supports both standard 188-octet TS packets and 192-octet M2TS source packets (which include a four-octet timestamp). Each MOQT Object must contain a concatenation of one or more whole source packets; splitting packets across Objects is strictly prohibited.
*   **Validation:** Receivers must validate packets by checking for the MPEG-2 sync byte (0x47) at the appropriate offset (position 0 for TS, position 4 for M2TS).
*   **Stream Structure:** Publishers are encouraged to start MOQT Groups at Random Access Points (RAPs) to ensure independent decodability. While the format preserves standard TS syntax (PCR, PTS, DTS, and continuity counters), it requires that PCR discontinuities only occur at Group boundaries and be explicitly signaled.
*   **Multi-Program Handling:** For multi-program transport streams (MPTS), the specification recommends filtering packets into single-program transport streams (SPTS), with each program assigned to its own MOQT track.
*   **Catalog Signaling:** The draft introduces specific JSON catalog fields to describe track metadata. The `m2tsPacketSize` field is required, while optional fields include `m2tsProgramNumber`, `m2tsPmtPid`, `m2tsPcrPid`, and `m2tsPacketsPerObject` to assist receivers in demultiplexing and buffer management.

Ultimately, this specification allows for the seamless delivery of packetized media while maintaining the integrity of MPEG-2 transport semantics, such as SCTE-35 splice signaling and Program Specific Information (PSI).

---

## 14. Motherboard sales 'collapse' amid unprecedented shortages fueled by AI

**原文标题**: Motherboard sales 'collapse' amid unprecedented shortages fueled by AI

**原文链接**: [https://www.tomshardware.com/pc-components/motherboards/motherboard-sales-collapse-by-more-than-25-percent-as-chipmakers-strangle-enthusiast-pc-market-to-build-more-ai-chips-asus-projected-to-sell-5-million-fewer-boards-in-2025-gigabyte-msi-and-asrock-also-expected-to-see-reduced-sales-numbers](https://www.tomshardware.com/pc-components/motherboards/motherboard-sales-collapse-by-more-than-25-percent-as-chipmakers-strangle-enthusiast-pc-market-to-build-more-ai-chips-asus-projected-to-sell-5-million-fewer-boards-in-2025-gigabyte-msi-and-asrock-also-expected-to-see-reduced-sales-numbers)

生成摘要时出错

---

## 15. SQLite Is a Library of Congress Recommended Storage Format

**原文标题**: SQLite Is a Library of Congress Recommended Storage Format

**原文链接**: [https://sqlite.org/locrsf.html](https://sqlite.org/locrsf.html)

生成摘要时出错

---

## 16. Printing Blogs

**原文标题**: Printing Blogs

**原文链接**: [https://fi-le.net/print/](https://fi-le.net/print/)

生成摘要时出错

---

## 17. How Cloudflare responded to the “Copy Fail” Linux vulnerability

**原文标题**: How Cloudflare responded to the “Copy Fail” Linux vulnerability

**原文链接**: [https://blog.cloudflare.com/copy-fail-linux-vulnerability-mitigation/](https://blog.cloudflare.com/copy-fail-linux-vulnerability-mitigation/)

生成摘要时出错

---

## 18. Show HN: Stage CLI – an easier way of reading your AI generated changes locally

**原文标题**: Show HN: Stage CLI – an easier way of reading your AI generated changes locally

**原文链接**: [https://github.com/ReviewStage/stage-cli](https://github.com/ReviewStage/stage-cli)

生成摘要时出错

---

## 19. Principles for agent-native CLIs

**原文标题**: Principles for agent-native CLIs

**原文链接**: [https://twitter.com/trevin/status/2051316002730991795](https://twitter.com/trevin/status/2051316002730991795)

生成摘要时出错

---

## 20. GovernGPT (YC W24) Is Hiring Engineers to Build Thinking Systems in Montreal

**原文标题**: GovernGPT (YC W24) Is Hiring Engineers to Build Thinking Systems in Montreal

**原文链接**: [https://www.ycombinator.com/companies/governgpt/jobs/hRyltS0-backend-engineer-thinking-systems](https://www.ycombinator.com/companies/governgpt/jobs/hRyltS0-backend-engineer-thinking-systems)

生成摘要时出错

---

## 21. Speedup in Lattice Boltzmann Cylinder Flow

**原文标题**: Speedup in Lattice Boltzmann Cylinder Flow

**原文链接**: [https://github.com/alikamp/Parks-KPBM-Scaling](https://github.com/alikamp/Parks-KPBM-Scaling)

生成摘要时出错

---

## 22. OurCar: What I learned making an app for my family

**原文标题**: OurCar: What I learned making an app for my family

**原文链接**: [https://mendelgreenberg.com/posts/ourcar/](https://mendelgreenberg.com/posts/ourcar/)

生成摘要时出错

---

## 23. Show HN: TRUST – Coding Rust like it's 1989

**原文标题**: Show HN: TRUST – Coding Rust like it's 1989

**原文链接**: [https://github.com/wojtczyk/trust](https://github.com/wojtczyk/trust)

生成摘要时出错

---

## 24. Brazil's Pix Payment System Faces Pressure from Visa and Mastercard

**原文标题**: Brazil's Pix Payment System Faces Pressure from Visa and Mastercard

**原文链接**: [https://www.elciudadano.com/en/brazils-pix-payment-system-faces-pressure-from-visa-and-mastercard/04/04/](https://www.elciudadano.com/en/brazils-pix-payment-system-faces-pressure-from-visa-and-mastercard/04/04/)

生成摘要时出错

---

## 25. Boris Cherny: TI-83 Plus Basic Programming Tutorial (2004)

**原文标题**: Boris Cherny: TI-83 Plus Basic Programming Tutorial (2004)

**原文链接**: [https://www.ticalc.org/programming/columns/83plus-bas/cherny/](https://www.ticalc.org/programming/columns/83plus-bas/cherny/)

生成摘要时出错

---

## 26. Indian matchbox labels as a visual archive

**原文标题**: Indian matchbox labels as a visual archive

**原文链接**: [https://www.itsnicethat.com/features/the-view-from-mumbai-matchbook-graphic-design-130426](https://www.itsnicethat.com/features/the-view-from-mumbai-matchbook-graphic-design-130426)

生成摘要时出错

---

## 27. ZAYA1-8B matches DeepSeek-R1 on math with less than 1B active parameters

**原文标题**: ZAYA1-8B matches DeepSeek-R1 on math with less than 1B active parameters

**原文链接**: [https://firethering.com/zaya1-8b-open-source-math-coding-model/](https://firethering.com/zaya1-8b-open-source-math-coding-model/)

生成摘要时出错

---

## 28. ProgramBench: Can language models rebuild programs from scratch?

**原文标题**: ProgramBench: Can language models rebuild programs from scratch?

**原文链接**: [https://arxiv.org/abs/2605.03546](https://arxiv.org/abs/2605.03546)

生成摘要时出错

---

## 29. I switched from Mac to a Lenovo Chromebook

**原文标题**: I switched from Mac to a Lenovo Chromebook

**原文链接**: [https://blog.johnozbay.com/i-left-apples-ecosystem-for-a-lenovo-chromebook-and-you-can-too.html](https://blog.johnozbay.com/i-left-apples-ecosystem-for-a-lenovo-chromebook-and-you-can-too.html)

生成摘要时出错

---

## 30. Permacomputing Principles

**原文标题**: Permacomputing Principles

**原文链接**: [https://permacomputing.net/principles/](https://permacomputing.net/principles/)

生成摘要时出错

---

## 31. Agent-harness-kit scaffolding for multi-agent workflows (MCP, provider-agnostic)

**原文标题**: Agent-harness-kit scaffolding for multi-agent workflows (MCP, provider-agnostic)

**原文链接**: [https://ahk.cardor.dev](https://ahk.cardor.dev)

生成摘要时出错

---

## 32. Diskless Linux boot using ZFS, iSCSI and PXE

**原文标题**: Diskless Linux boot using ZFS, iSCSI and PXE

**原文链接**: [https://aniket.foo/posts/20260505-netboot/](https://aniket.foo/posts/20260505-netboot/)

生成摘要时出错

---

## 33. RSS feeds send me more traffic than Google

**原文标题**: RSS feeds send me more traffic than Google

**原文链接**: [https://shkspr.mobi/blog/2026/05/rss-feeds-send-me-more-traffic-than-google/](https://shkspr.mobi/blog/2026/05/rss-feeds-send-me-more-traffic-than-google/)

生成摘要时出错

---

## 34. Valve releases Steam Controller CAD files under Creative Commons license

**原文标题**: Valve releases Steam Controller CAD files under Creative Commons license

**原文链接**: [https://www.digitalfoundry.net/news/2026/05/valve-releases-steam-controller-cad-files-under-creative-commons-license](https://www.digitalfoundry.net/news/2026/05/valve-releases-steam-controller-cad-files-under-creative-commons-license)

生成摘要时出错

---

## 35. Vibe coding and agentic engineering are getting closer than I'd like

**原文标题**: Vibe coding and agentic engineering are getting closer than I'd like

**原文链接**: [https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/](https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/)

生成摘要时出错

---

## 36. "Mother of all Demos" (1968)

**原文标题**: "Mother of all Demos" (1968)

**原文链接**: [https://www.youtube.com/watch?v=B6rKUf9DWRI](https://www.youtube.com/watch?v=B6rKUf9DWRI)

生成摘要时出错

---

## 37. Chevrolet Performance eCrate package (400v/200hp)

**原文标题**: Chevrolet Performance eCrate package (400v/200hp)

**原文链接**: [https://www.chevrolet.com/performance-parts/crate-engines/ecrate](https://www.chevrolet.com/performance-parts/crate-engines/ecrate)

生成摘要时出错

---

## 38. The mechanical latching memory of an adhesive tape

**原文标题**: The mechanical latching memory of an adhesive tape

**原文链接**: [https://iopscience.iop.org/article/10.1088/1367-2630/ae4acc](https://iopscience.iop.org/article/10.1088/1367-2630/ae4acc)

生成摘要时出错

---

## 39. SingleRide: Longest route on NYC Subway without visiting the same station twice

**原文标题**: SingleRide: Longest route on NYC Subway without visiting the same station twice

**原文链接**: [https://singleride.nyc/](https://singleride.nyc/)

生成摘要时出错

---

## 40. The brave souls who bought a used, 340k-mile rental camper van

**原文标题**: The brave souls who bought a used, 340k-mile rental camper van

**原文链接**: [https://www.thedrive.com/news/meet-the-brave-souls-who-bought-a-used-340000-mile-rental-camper-van](https://www.thedrive.com/news/meet-the-brave-souls-who-bought-a-used-340000-mile-rental-camper-van)

生成摘要时出错

---

## 41. Appearing productive in the workplace

**原文标题**: Appearing productive in the workplace

**原文链接**: [https://nooneshappy.com/article/appearing-productive-in-the-workplace/](https://nooneshappy.com/article/appearing-productive-in-the-workplace/)

生成摘要时出错

---

## 42. Google Cloud fraud defense, the next evolution of reCAPTCHA

**原文标题**: Google Cloud fraud defense, the next evolution of reCAPTCHA

**原文链接**: [https://cloud.google.com/blog/products/identity-security/introducing-google-cloud-fraud-defense-the-next-evolution-of-recaptcha/](https://cloud.google.com/blog/products/identity-security/introducing-google-cloud-fraud-defense-the-next-evolution-of-recaptcha/)

生成摘要时出错

---

## 43. Advancing voice intelligence with new models in the API

**原文标题**: Advancing voice intelligence with new models in the API

**原文链接**: [https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/)

生成摘要时出错

---

## 44. LinkedIn profile visitor lists belong to the people, says Noyb

**原文标题**: LinkedIn profile visitor lists belong to the people, says Noyb

**原文链接**: [https://www.theregister.com/offbeat/2026/05/05/noyb-cries-foul-on-linkedin-withholding-profile-visitor-data/5225338](https://www.theregister.com/offbeat/2026/05/05/noyb-cries-foul-on-linkedin-withholding-profile-visitor-data/5225338)

生成摘要时出错

---

## 45. Show HN: Agent-skills-eval – Test whether Agent Skills improve outputs

**原文标题**: Show HN: Agent-skills-eval – Test whether Agent Skills improve outputs

**原文链接**: [https://github.com/darkrishabh/agent-skills-eval](https://github.com/darkrishabh/agent-skills-eval)

生成摘要时出错

---

## 46. From Supabase to Clerk to Better Auth

**原文标题**: From Supabase to Clerk to Better Auth

**原文链接**: [https://blog.val.town/better-auth](https://blog.val.town/better-auth)

生成摘要时出错

---

## 47. Pen pal programs endure in a digital age

**原文标题**: Pen pal programs endure in a digital age

**原文链接**: [https://apnews.com/article/pen-pals-letters-comeback-bc87e1b9c229665bafd368e19751d6ca](https://apnews.com/article/pen-pals-letters-comeback-bc87e1b9c229665bafd368e19751d6ca)

生成摘要时出错

---

## 48. Community firmware for the Xteink X4 e-paper reader

**原文标题**: Community firmware for the Xteink X4 e-paper reader

**原文链接**: [https://github.com/crosspoint-reader/crosspoint-reader](https://github.com/crosspoint-reader/crosspoint-reader)

生成摘要时出错

---

## 49. Show HN: Hallucinopedia

**原文标题**: Show HN: Hallucinopedia

**原文链接**: [http://halupedia.com/](http://halupedia.com/)

生成摘要时出错

---

## 50. Grand Theft Oil Futures: Insider traders keep making a killing at our expense

**原文标题**: Grand Theft Oil Futures: Insider traders keep making a killing at our expense

**原文链接**: [https://paulkrugman.substack.com/p/grand-theft-oil-futures](https://paulkrugman.substack.com/p/grand-theft-oil-futures)

生成摘要时出错

---

## 51. Show HN: Tilde.run – Agent sandbox with a transactional, versioned filesystem

**原文标题**: Show HN: Tilde.run – Agent sandbox with a transactional, versioned filesystem

**原文链接**: [https://tilde.run/](https://tilde.run/)

生成摘要时出错

---

## 52. Making LLM Training Faster with Unsloth and NVIDIA

**原文标题**: Making LLM Training Faster with Unsloth and NVIDIA

**原文链接**: [https://unsloth.ai/blog/nvidia-collab](https://unsloth.ai/blog/nvidia-collab)

生成摘要时出错

---

## 53. The Old Guard: Confronting America's Gerontocratic Crisis

**原文标题**: The Old Guard: Confronting America's Gerontocratic Crisis

**原文链接**: [https://harpers.org/archive/2026/05/the-old-guard-samuel-moyn-gerontocracy/](https://harpers.org/archive/2026/05/the-old-guard-samuel-moyn-gerontocracy/)

生成摘要时出错

---

## 54. The Mathematical Dance Inside Plant Cells

**原文标题**: The Mathematical Dance Inside Plant Cells

**原文链接**: [https://www.quantamagazine.org/the-hidden-mathematical-dance-inside-plant-cells-20260504/](https://www.quantamagazine.org/the-hidden-mathematical-dance-inside-plant-cells-20260504/)

生成摘要时出错

---

## 55. What British people mean when they say 'sorry'

**原文标题**: What British people mean when they say 'sorry'

**原文链接**: [https://www.bbc.com/travel/article/20260506-what-british-people-really-mean-when-they-say-sorry](https://www.bbc.com/travel/article/20260506-what-british-people-really-mean-when-they-say-sorry)

生成摘要时出错

---

## 56. DS4, a specialized inference engine for DeepSeek v4 Flash

**原文标题**: DS4, a specialized inference engine for DeepSeek v4 Flash

**原文链接**: [https://twitter.com/antirez/status/2052405820235678175](https://twitter.com/antirez/status/2052405820235678175)

生成摘要时出错

---

## 57. Bubbles Are Really Evil

**原文标题**: Bubbles Are Really Evil

**原文链接**: [https://pluralistic.net/2026/05/07/dump-the-pumpers/](https://pluralistic.net/2026/05/07/dump-the-pumpers/)

生成摘要时出错

---

## 58. How do I inform Windows that I'm writing a binary file?

**原文标题**: How do I inform Windows that I'm writing a binary file?

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20260504-00/?p=112296](https://devblogs.microsoft.com/oldnewthing/20260504-00/?p=112296)

生成摘要时出错

---

## 59. A Theory of Deep Learning

**原文标题**: A Theory of Deep Learning

**原文链接**: [https://elonlit.com/scrivings/a-theory-of-deep-learning/](https://elonlit.com/scrivings/a-theory-of-deep-learning/)

生成摘要时出错

---

## 60. Google Chrome silently installs a 4 GB AI model on your device without consent

**原文标题**: Google Chrome silently installs a 4 GB AI model on your device without consent

**原文链接**: [https://www.thatprivacyguy.com/blog/chrome-silent-nano-install/](https://www.thatprivacyguy.com/blog/chrome-silent-nano-install/)

生成摘要时出错

---

## 61. Ted Turner has died

**原文标题**: Ted Turner has died

**原文链接**: [https://www.cnn.com/2026/05/06/us/ted-turner-death](https://www.cnn.com/2026/05/06/us/ted-turner-death)

生成摘要时出错

---

## 62. The Upper Middle Class Trap

**原文标题**: The Upper Middle Class Trap

**原文链接**: [https://ofdollarsanddata.com/the-upper-middle-class-trap/](https://ofdollarsanddata.com/the-upper-middle-class-trap/)

生成摘要时出错

---

## 63. Learning the Integral of a Diffusion Model

**原文标题**: Learning the Integral of a Diffusion Model

**原文链接**: [https://sander.ai/2026/05/06/flow-maps.html](https://sander.ai/2026/05/06/flow-maps.html)

生成摘要时出错

---

## 64. Building my own Vi text editor in BASIC

**原文标题**: Building my own Vi text editor in BASIC

**原文链接**: [https://leetusman.com/nosebook/yvi](https://leetusman.com/nosebook/yvi)

生成摘要时出错

---

## 65. Setting up a Sun Ray server on OpenIndiana Hipster 2025.10

**原文标题**: Setting up a Sun Ray server on OpenIndiana Hipster 2025.10

**原文链接**: [https://catstret.ch/202605/srss-hipster202510/](https://catstret.ch/202605/srss-hipster202510/)

生成摘要时出错

---

## 66. Agents can now create Cloudflare accounts, buy domains, and deploy

**原文标题**: Agents can now create Cloudflare accounts, buy domains, and deploy

**原文链接**: [https://blog.cloudflare.com/agents-stripe-projects/](https://blog.cloudflare.com/agents-stripe-projects/)

生成摘要时出错

---

## 67. Show HN: I built an open-source email builder, alternative to Beefree/Unlayer

**原文标题**: Show HN: I built an open-source email builder, alternative to Beefree/Unlayer

**原文链接**: [https://play.templatical.com](https://play.templatical.com)

生成摘要时出错

---

## 68. Three-Em Dash

**原文标题**: Three-Em Dash

**原文链接**: [https://www.compart.com/en/unicode/U+2E3B](https://www.compart.com/en/unicode/U+2E3B)

生成摘要时出错

---

## 69. Virtual violin produces realistic sounds

**原文标题**: Virtual violin produces realistic sounds

**原文链接**: [https://news.mit.edu/2026/mit-engineers-virtual-violin-produces-realistic-sounds-0429](https://news.mit.edu/2026/mit-engineers-virtual-violin-produces-realistic-sounds-0429)

生成摘要时出错

---

## 70. Inkscape 1.4.4

**原文标题**: Inkscape 1.4.4

**原文链接**: [https://inkscape.org/doc/release_notes/1.4.4/Inkscape_1.4.4.html](https://inkscape.org/doc/release_notes/1.4.4/Inkscape_1.4.4.html)

生成摘要时出错

---

## 71. StarFighter 16-Inch

**原文标题**: StarFighter 16-Inch

**原文链接**: [https://us.starlabs.systems/pages/starfighter](https://us.starlabs.systems/pages/starfighter)

生成摘要时出错

---

## 72. Cursed Browser: Rendering Engine Using Visual-LLMs

**原文标题**: Cursed Browser: Rendering Engine Using Visual-LLMs

**原文链接**: [https://github.com/scosman/cursed_browser](https://github.com/scosman/cursed_browser)

生成摘要时出错

---

## 73. Photoshop's challenges with focus, pt. 2

**原文标题**: Photoshop's challenges with focus, pt. 2

**原文链接**: [https://unsung.aresluna.org/photoshops-challenges-with-focus-pt-2/](https://unsung.aresluna.org/photoshops-challenges-with-focus-pt-2/)

生成摘要时出错

---

## 74. Show HN: PHP-fts – Full-text search engine in pure PHP, no extensions

**原文标题**: Show HN: PHP-fts – Full-text search engine in pure PHP, no extensions

**原文链接**: [https://github.com/olivier-ls/php-fts](https://github.com/olivier-ls/php-fts)

生成摘要时出错

---

## 75. Mythos is the best cybersecurity news in a decade

**原文标题**: Mythos is the best cybersecurity news in a decade

**原文链接**: [https://sfstandard.com/opinion/2026/05/06/mythos-cybersecurity-ai/](https://sfstandard.com/opinion/2026/05/06/mythos-cybersecurity-ai/)

生成摘要时出错

---

## 76. Hardening Firefox with Claude Mythos Preview

**原文标题**: Hardening Firefox with Claude Mythos Preview

**原文链接**: [https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/](https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/)

生成摘要时出错

---

## 77. What makes a good smartphone camera?

**原文标题**: What makes a good smartphone camera?

**原文链接**: [https://cadence.moe/blog/2026-05-05-what-makes-a-good-smartphone-camera](https://cadence.moe/blog/2026-05-05-what-makes-a-good-smartphone-camera)

生成摘要时出错

---

## 78. Higher usage limits for Claude and a compute deal with SpaceX

**原文标题**: Higher usage limits for Claude and a compute deal with SpaceX

**原文链接**: [https://www.anthropic.com/news/higher-limits-spacex](https://www.anthropic.com/news/higher-limits-spacex)

生成摘要时出错

---

## 79. CARA 2.0 – “I Built a Better Robot Dog”

**原文标题**: CARA 2.0 – “I Built a Better Robot Dog”

**原文链接**: [https://www.aaedmusa.com/projects/cara2](https://www.aaedmusa.com/projects/cara2)

生成摘要时出错

---

## 80. The bottleneck was never the code

**原文标题**: The bottleneck was never the code

**原文链接**: [https://www.thetypicalset.com/blog/thoughts-on-coding-agents](https://www.thetypicalset.com/blog/thoughts-on-coding-agents)

生成摘要时出错

---

## 81. Wolfenstein 3D for Gameboy Color on custom cartridge (2016)

**原文标题**: Wolfenstein 3D for Gameboy Color on custom cartridge (2016)

**原文链接**: [https://www.happydaze.se/wolf/](https://www.happydaze.se/wolf/)

生成摘要时出错

---

## 82. California leaders report four to six weeks worth of gasoline and diesel supply

**原文标题**: California leaders report four to six weeks worth of gasoline and diesel supply

**原文链接**: [https://kmph.com/news/local/california-leaders-report-four-to-six-weeks-worth-of-gasoline-and-diesel-in-supply](https://kmph.com/news/local/california-leaders-report-four-to-six-weeks-worth-of-gasoline-and-diesel-in-supply)

生成摘要时出错

---

## 83. The Vatican's Website in Latin

**原文标题**: The Vatican's Website in Latin

**原文链接**: [https://www.vatican.va/latin/latin_index.html](https://www.vatican.va/latin/latin_index.html)

生成摘要时出错

---

## 84. Accelerating Gemma 4: faster inference with multi-token prediction drafters

**原文标题**: Accelerating Gemma 4: faster inference with multi-token prediction drafters

**原文链接**: [https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/)

生成摘要时出错

---

## 85. Show HN: I made a vertical-pedalling bike with a novel drivetrain [video]

**原文标题**: Show HN: I made a vertical-pedalling bike with a novel drivetrain [video]

**原文链接**: [https://www.youtube.com/watch?v=4HLOsi2gWXQ](https://www.youtube.com/watch?v=4HLOsi2gWXQ)

生成摘要时出错

---

## 86. Perturb-MARS: Reading mouse experiments through a human lens

**原文标题**: Perturb-MARS: Reading mouse experiments through a human lens

**原文链接**: [https://www.noetik.blog/p/perturb-mars-reading-mouse-experiments](https://www.noetik.blog/p/perturb-mars-reading-mouse-experiments)

生成摘要时出错

---

## 87. Finding the differences in a series of power supplies

**原文标题**: Finding the differences in a series of power supplies

**原文链接**: [https://www.lttlabs.com/articles/2026/05/05/testing-psu-series](https://www.lttlabs.com/articles/2026/05/05/testing-psu-series)

生成摘要时出错

---

## 88. DNSSEC disruption affecting .de domains – Resolved

**原文标题**: DNSSEC disruption affecting .de domains – Resolved

**原文链接**: [https://status.denic.de/pages/incident/592577eab611ce1e0d00046f/69fa60ef9d12f5057a974f38](https://status.denic.de/pages/incident/592577eab611ce1e0d00046f/69fa60ef9d12f5057a974f38)

生成摘要时出错

---

## 89. Wiki Builder: Skill to Build LLM Knowledge Bases

**原文标题**: Wiki Builder: Skill to Build LLM Knowledge Bases

**原文链接**: [https://academy.dair.ai/blog/wiki-builder-claude-code-plugin](https://academy.dair.ai/blog/wiki-builder-claude-code-plugin)

生成摘要时出错

---

## 90. Multi-stroke text effect in CSS

**原文标题**: Multi-stroke text effect in CSS

**原文链接**: [https://yuanchuan.dev/multi-stroke-text-effect-in-css](https://yuanchuan.dev/multi-stroke-text-effect-in-css)

生成摘要时出错

---

## 91. Programming Still Sucks

**原文标题**: Programming Still Sucks

**原文链接**: [https://www.stvn.sh/writing/programming-still-sucks-fqffhyp](https://www.stvn.sh/writing/programming-still-sucks-fqffhyp)

生成摘要时出错

---

## 92. SQLite Archive Files

**原文标题**: SQLite Archive Files

**原文链接**: [https://sqlite.org/sqlar.html](https://sqlite.org/sqlar.html)

生成摘要时出错

---

## 93. Knitting bullshit

**原文标题**: Knitting bullshit

**原文链接**: [https://katedaviesdesigns.com/2026/04/29/knitting-bullshit/](https://katedaviesdesigns.com/2026/04/29/knitting-bullshit/)

生成摘要时出错

---

## 94. Building the TD4 4-Bit CPU

**原文标题**: Building the TD4 4-Bit CPU

**原文链接**: [https://jayakody2000lk.blogspot.com/2026/05/building-td4-4-bit-cpu.html](https://jayakody2000lk.blogspot.com/2026/05/building-td4-4-bit-cpu.html)

生成摘要时出错

---

## 95. Reverse-engineering the 1998 Ultima Online demo server

**原文标题**: Reverse-engineering the 1998 Ultima Online demo server

**原文链接**: [https://draxinar.github.io/articles/2026-05-01-uodemo-reverse-engineering.html](https://draxinar.github.io/articles/2026-05-01-uodemo-reverse-engineering.html)

生成摘要时出错

---

## 96. The Thinking Plant's Man (2025)

**原文标题**: The Thinking Plant's Man (2025)

**原文链接**: [https://www.sciencehistory.org/stories/magazine/the-thinking-plants-man/](https://www.sciencehistory.org/stories/magazine/the-thinking-plants-man/)

生成摘要时出错

---

## 97. 245TB Micron 6600 ION Data Center SSD Now Shipping

**原文标题**: 245TB Micron 6600 ION Data Center SSD Now Shipping

**原文链接**: [https://investors.micron.com/news-releases/news-release-details/industry-leading-245tb-micron-6600-ion-data-center-ssd-now](https://investors.micron.com/news-releases/news-release-details/industry-leading-245tb-micron-6600-ion-data-center-ssd-now)

生成摘要时出错

---

## 98. YouTube, your RSS feeds are broken

**原文标题**: YouTube, your RSS feeds are broken

**原文链接**: [https://openrss.org/blog/youtube-your-feeds-are-broken](https://openrss.org/blog/youtube-your-feeds-are-broken)

生成摘要时出错

---

## 99. Google tools for customizing searches

**原文标题**: Google tools for customizing searches

**原文链接**: [https://cardcatalogforlife.substack.com/p/google-has-a-secret-reference-desk](https://cardcatalogforlife.substack.com/p/google-has-a-secret-reference-desk)

生成摘要时出错

---

## 100. Computer Use is 45x more expensive than structured APIs

**原文标题**: Computer Use is 45x more expensive than structured APIs

**原文链接**: [https://reflex.dev/blog/computer-use-is-45x-more-expensive-than-structured-apis/](https://reflex.dev/blog/computer-use-is-45x-more-expensive-than-structured-apis/)

生成摘要时出错

---

