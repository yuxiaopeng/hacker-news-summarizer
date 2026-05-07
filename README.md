# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-05-07.md)

*最后自动更新时间: 2026-05-07 19:11:05*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 2 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 3 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 4 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 5 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 6 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 7 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 8 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 9 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 10 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 11 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 12 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 13 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 14 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 15 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 16 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 17 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 18 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 19 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 20 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 21 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 22 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 23 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 24 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 25 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 26 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 27 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 28 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 29 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 30 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 31 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 32 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 33 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 34 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 35 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 36 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 37 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 38 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 39 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 40 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 41 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 42 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 43 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 44 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 45 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 46 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 47 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 48 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 49 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 50 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 51 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 52 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 53 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 54 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 55 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 56 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 57 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 58 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 59 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 60 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 61 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 62 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 63 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 64 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 65 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 66 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 67 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 68 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 69 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 70 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 71 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 72 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 73 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 74 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 75 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 76 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 77 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 78 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 79 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 80 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 81 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 82 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 83 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 84 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 85 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 86 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 87 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 88 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 89 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 90 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 91 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 92 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 93 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 94 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 95 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 96 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 97 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 98 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 99 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 100 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 101 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 102 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 103 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 104 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 105 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 106 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 107 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 108 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 109 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 110 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 111 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 112 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 113 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 114 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 115 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 116 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 117 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 118 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 119 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 120 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 121 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 122 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 123 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 124 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 125 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 126 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 127 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 128 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 129 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 130 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 131 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 132 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 133 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 134 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 135 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 136 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 137 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 138 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 139 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 140 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 141 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 142 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 143 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 144 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 145 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 146 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 147 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 148 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 149 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 150 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 151 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 152 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 153 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 154 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 155 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 156 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 157 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 158 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 159 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 160 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 161 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 162 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 163 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 164 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 165 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 166 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 167 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 168 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 169 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 170 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 171 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 172 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 173 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 174 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 175 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 176 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 177 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 178 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 179 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 180 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 181 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 182 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 183 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 184 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 185 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 186 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 187 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 188 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 189 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 190 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 191 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 192 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 193 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 194 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 195 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 196 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 197 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 198 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 199 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 200 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 201 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 202 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 203 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 204 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 205 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 206 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 207 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 208 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 209 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 210 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 211 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 212 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 213 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 214 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 215 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 216 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 217 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 218 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 219 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 220 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 221 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 222 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 223 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 224 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 225 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 226 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 227 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 228 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 229 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 230 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 231 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 232 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 233 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 234 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 235 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 236 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 237 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 238 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 239 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 240 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 241 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 242 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 243 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 244 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 245 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 246 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 247 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 248 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 249 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 250 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 251 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 252 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 253 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 254 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 255 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 256 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 257 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 258 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 259 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 260 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 261 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 262 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 263 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 264 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 265 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 266 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 267 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 268 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 269 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 270 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 271 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 272 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 273 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 274 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 275 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 276 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 277 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 278 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 279 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 280 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 281 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 282 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 283 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 284 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 285 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 286 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 287 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 288 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 289 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 290 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 291 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 292 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 293 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 294 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 295 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 296 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 297 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 298 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 299 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 300 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 301 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 302 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 303 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 304 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 305 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 306 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 307 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 308 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 309 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 310 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 311 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 312 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 313 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 314 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 315 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 316 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 317 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 318 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 319 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 320 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 321 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 322 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 323 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 324 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 325 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 326 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 327 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 328 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 329 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 330 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 331 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 332 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 333 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 334 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 335 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 336 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 337 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 338 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 339 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 340 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 341 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 342 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 343 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 344 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 345 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 346 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 347 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 348 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 349 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 350 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 351 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 352 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 353 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 354 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 355 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 356 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 357 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 358 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 359 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 360 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 361 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 362 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 363 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 364 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 365 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 366 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 367 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 368 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 369 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 370 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 371 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 372 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 373 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 374 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 375 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 376 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 377 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 378 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 379 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 380 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 381 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 382 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 383 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 384 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 385 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 386 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 387 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 388 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 389 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 390 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 391 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 392 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 393 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 394 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 395 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 396 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 397 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 398 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 399 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 400 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 401 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 402 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 403 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 404 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 405 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 406 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 407 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 408 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 409 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 410 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 411 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 412 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 413 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
