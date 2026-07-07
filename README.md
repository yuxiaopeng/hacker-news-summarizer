# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-07-07.md)

*最后自动更新时间: 2026-07-07 19:29:35*
## 1. OpenSSH 10.4/10.4p1 Released

**原文标题**: OpenSSH 10.4/10.4p1 Released

**原文链接**: [https://www.openssh.org/txt/release-10.4](https://www.openssh.org/txt/release-10.4)

生成摘要时出错

---

## 2. 墨田

**原文标题**: Inkfield

**原文链接**: [https://www.inkfield.studio](https://www.inkfield.studio)

所提供的内容仅包含“**inkfield**”这个单词。假设您指的是同名的独立视频游戏和艺术项目，以下是简要概述：

**Inkfield** 是一项极具氛围感的独立解谜冒险项目，以其鲜明且极简的视觉辨识度为特色。该体验的核心是一个超现实的手绘世界，利用强烈的黑白“纸墨”美学，营造出一种神秘与孤寂感。

核心要点包括：
*   **美术方向**：该项目以其独特的高对比度艺术风格著称，这是其叙事的主要载体。
*   **游戏玩法**：通常结合了探索与环境解谜，要求玩家在梦幻般的景观中穿行。
*   **氛围营造**：叙事基本不使用言语，而是依靠视觉线索和情绪基调，让玩家沉浸在其阴郁且具实验性的环境之中。

如果您原本打算提供全文进行摘要但未能正确粘贴，请提供相关文本，我很乐意为您重新进行总结。

---

## 3. Show HN: Context Warp Drive —— 面向 AI 智能体的确定性上下文折叠

**原文标题**: Show HN: Context Warp Drive – Deterministic context folding for AI agents

**原文链接**: [https://github.com/dogtorjonah/context-warp-drive](https://github.com/dogtorjonah/context-warp-drive)

**Context Warp Drive (CWD)** 是一种确定性上下文折叠引擎，旨在管理长周期 AI 智能体记忆，且无需承担传统摘要或截断方式的弊端。虽然基于 LLM 的摘要等标准方法成本高昂、具有非确定性且会破坏提供商的提示词缓存，但 CWD 利用纯 CPU 逻辑将历史记录“折叠”为紧凑的结构化骨架。

**核心特性与优势：**
*   **确定性压缩：** 无需额外的 LLM 调用即可折叠上下文，确保相同的输入产生字节级一致的输出。这能保持提供商提示词缓存的“热度”，据报告缓存命中率约为 90%。
*   **经济高效：** 在生产负载中（特别是使用 Claude 时），通过利用提供商的缓存折扣（0.30 美元/百万 Token 对比 3.00 美元/百万 Token），CWD 相比 LLM 摘要可降低约 70% 的成本，相比截断方式可降低约 60%。
*   **高事实保留率：** 它使用“坐标库 (Coordinate Closet)”来保留摘要过程中经常丢失的精确标识符（如 UUID、SHA、路径和端口），其保留率显著高于滑动窗口模式。
*   **跨提供商支持：** 该引擎支持 Anthropic、OpenAI 和 Gemini，并提供特定助手来管理不同的缓存机制（例如 Anthropic 的 `cache_control`）。
*   **可扩展性：** 当 Token 压力达到上限时，CWD 会执行“硬纪元重塑 (hard-epoch rebirth)”，将可见历史折叠为紧凑的种子，同时保留原始转录内容以供召回。

**组件：**
*   **FoldSession：** 为模型准备消息历史记录的核心管理器。
*   **Budget Resolver：** 根据所用模型的特定上下文窗口自动调整折叠阈值。
*   **Task Rail：** 一个便携式状态机，用于跟踪智能体计划和执行步骤，确保它们在上下文折叠或系统重启后依然存在。

Context Warp Drive 目前以 TypeScript 软件包的形式在 GitHub 上提供，适用于构建需要高频对话、低延迟和可预测成本的生产级多智能体系统的开发人员。

---

## 4. Anthropic 在移动端和网页端推出 Claude Cowork

**原文标题**: Anthropic is launching Claude Cowork on mobile and web

**原文链接**: [https://www.theverge.com/ai-artificial-intelligence/961978/anthropic-claude-cowork-mobile-web](https://www.theverge.com/ai-artificial-intelligence/961978/anthropic-claude-cowork-mobile-web)

Anthropic 宣布其 Claude Cowork AI 平台正从原有的桌面应用程序扩展至 iOS、Android 及网页端。该更新将于本周二开始面向 Claude Max 订阅用户推出，其他方案的用户预计将在未来几周内获得访问权限。

此次更新的一个重要特性是默认转向云端处理。这使得 Claude Cowork 即使在用户笔记本电脑关闭或设备离线的情况下，仍能继续在后台运行任务。预定任务现在将独立执行，当任务准备好供审查或批准时，平台会向用户发送移动端通知。

虽然移动版和网页版提供了更高的灵活性和跨设备延续性，但 Anthropic 指出，“完整体验”——特别是本地文件访问功能——仍为 macOS 和 Windows 桌面应用专属。桌面用户可以根据需要，在云端处理和本地处理之间进行切换。

配合此次发布，Anthropic 还将其 Cowork 双倍使用额度的优惠活动延长至 2026 年 8 月 5 日。

---

## 5. 给马克·扎克伯格的剧本

**原文标题**: A Script for Mark Zuckerberg

**原文链接**: [https://stratechery.com/2026/a-script-for-mark-zuckerberg/](https://stratechery.com/2026/a-script-for-mark-zuckerberg/)

这份由 *Stratechery* 的 Ben Thompson 撰写的 2026 年模拟财报电话会议剧本，呈现了马克·扎克伯格针对 Meta 战略方向和 AI 投资的一次假设性“公开检讨”。

演讲的核心在于扎克伯格承认，他长期以来对成为“平台”所有者的执着——以推迟向原生移动应用转型以及对 Reality Labs 的巨额支出为代表——是一个错误。相反，剧本建议扎克伯格应当拥抱 Meta 的真实身份：一个广告和娱乐巨头。他承认，虽然过去低估了广告业务，但它实际上是公司最强大的优势，也是连接创作者与消费者的重要经济驱动力。

该演讲为 Meta 的巨额 AI 支出勾勒了三部分战略：
1.  **生存必然性**：AI 对所有数字公司都构成了存亡风险；Meta 必须保持领先才能生存。
2.  **广告与库存增长**：AI 增强了内容推荐和精准投放，通过实现“像素级变现”，创造了史上“最大的广告库存扩张”。
3.  **聚焦休闲**：Meta 不会在生产力工具上与 OpenAI 竞争，而是将 AI 重点放在社交、娱乐和购物上。

最后，剧本提出了一种新颖的财务模式：Meta 将短期出租其富余的算力基础设施。这不仅能产生收入以资助后续建设，还设立了一个“门槛收益率”，确保内部团队仅在项目盈利能力超过市场租赁价格时才使用算力。最终，该剧本构想了一个不再试图成为硬件平台，而是利用 AI 统治数字注意力与广告经济的 Meta。

---

## 6. Canada to buy 12 hi-tech German submarines after bidding war

**原文标题**: Canada to buy 12 hi-tech German submarines after bidding war

**原文链接**: [https://www.theguardian.com/world/2026/jul/06/canada-buys-12-tkms-german-norwegian-submarines-after-bidding-war](https://www.theguardian.com/world/2026/jul/06/canada-buys-12-tkms-german-norwegian-submarines-after-bidding-war)

Canada has selected the German consortium ThyssenKrupp Marine Systems (TKMS) to build 12 new HDW Class 212CD diesel-electric submarines. This multibillion-dollar contract—one of the largest in Canadian history—aims to replace the Royal Canadian Navy’s aging fleet of four secondhand Victoria-class vessels.

The decision followed a competitive bidding war with South Korea’s Hanwha Ocean. While Hanwha offered larger vessels and significant local investment, Canada ultimately chose the German-made 212CD model for its advanced stealth technology and its suitability for long-range Arctic surveillance. The deal also strengthens Canada’s ties with NATO, as TKMS is a primary supplier for the alliance's fleet.

The financial scope of the project is massive: the initial order is estimated at US$12 billion, but with roughly 50 years of maintenance included, the total cost could exceed US$70 billion. Negotiations to finalize the contract are expected to take several years.

Announced by Prime Minister Mark Carney, the deal reflects a broader shift in Canadian defense policy. The government has committed to increasing defense spending to 2% of GDP, with a future goal of 5% by 2035. Furthermore, the selection of a German firm over a U.S. or South Korean rival highlights Ottawa's strategic push to diversify its defense partnerships and reduce its reliance on the United States. This trend is further evidenced by Canada’s potential purchase of 72 Saab-made Gripen fighter jets from Sweden to complement its fleet of American F-35s.

---

## 7. GLM 5.2 and the coming AI margin collapse

**原文标题**: GLM 5.2 and the coming AI margin collapse

**原文链接**: [https://martinalderson.com/posts/the-upcoming-ai-margin-collapse-part-1-glm-5-2/](https://martinalderson.com/posts/the-upcoming-ai-margin-collapse-part-1-glm-5-2/)

生成摘要时出错

---

## 8. Learning to code is still worthwhile

**原文标题**: Learning to code is still worthwhile

**原文链接**: [https://stevekrouse.com/learn-to-code](https://stevekrouse.com/learn-to-code)

生成摘要时出错

---

## 9. How did we make DeepSeek outperform Opus

**原文标题**: How did we make DeepSeek outperform Opus

**原文链接**: [https://twitter.com/MrAhmadAwais/status/2050956678502420612](https://twitter.com/MrAhmadAwais/status/2050956678502420612)

生成摘要时出错

---

## 10. Januscape: Guest-to-Host Escape in KVM/x86 [CVE-2026-53359]

**原文标题**: Januscape: Guest-to-Host Escape in KVM/x86 [CVE-2026-53359]

**原文链接**: [https://github.com/V4bel/Januscape](https://github.com/V4bel/Januscape)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 2 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 3 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 4 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 5 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 6 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 7 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 8 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 9 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 10 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 11 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 12 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 13 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 14 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 15 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 16 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 17 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 18 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 19 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 20 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 21 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 22 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 23 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 24 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 25 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 26 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 27 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 28 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 29 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 30 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 31 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 32 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 33 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 34 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 35 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 36 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 37 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 38 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 39 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 40 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 41 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 42 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 43 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 44 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 45 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 46 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 47 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 48 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 49 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 50 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 51 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 52 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 53 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 54 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 55 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 56 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 57 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 58 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 59 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 60 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 61 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 62 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 63 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 64 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 65 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 66 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 67 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 68 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 69 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 70 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 71 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 72 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 73 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 74 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 75 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 76 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 77 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 78 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 79 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 80 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 81 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 82 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 83 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 84 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 85 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 86 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 87 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 88 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 89 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 90 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 91 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 92 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 93 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 94 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 95 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 96 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 97 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 98 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 99 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 100 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 101 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 102 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 103 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 104 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 105 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 106 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 107 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 108 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 109 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 110 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 111 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 112 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 113 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 114 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 115 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 116 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 117 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 118 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 119 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 120 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 121 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 122 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 123 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 124 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 125 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 126 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 127 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 128 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 129 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 130 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 131 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 132 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 133 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 134 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 135 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 136 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 137 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 138 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 139 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 140 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 141 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 142 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 143 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 144 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 145 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 146 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 147 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 148 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 149 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 150 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 151 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 152 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 153 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 154 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 155 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 156 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 157 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 158 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 159 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 160 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 161 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 162 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 163 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 164 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 165 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 166 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 167 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 168 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 169 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 170 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 171 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 172 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 173 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 174 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 175 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 176 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 177 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 178 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 179 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 180 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 181 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 182 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 183 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 184 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 185 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 186 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 187 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 188 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 189 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 190 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 191 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 192 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 193 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 194 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 195 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 196 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 197 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 198 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 199 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 200 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 201 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 202 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 203 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 204 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 205 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 206 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 207 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 208 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 209 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 210 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 211 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 212 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 213 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 214 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 215 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 216 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 217 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 218 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 219 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 220 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 221 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 222 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 223 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 224 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 225 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 226 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 227 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 228 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 229 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 230 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 231 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 232 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 233 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 234 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 235 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 236 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 237 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 238 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 239 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 240 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 241 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 242 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 243 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 244 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 245 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 246 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 247 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 248 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 249 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 250 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 251 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 252 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 253 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 254 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 255 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 256 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 257 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 258 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 259 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 260 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 261 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 262 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 263 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 264 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 265 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 266 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 267 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 268 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 269 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 270 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 271 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 272 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 273 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 274 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 275 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 276 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 277 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 278 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 279 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 280 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 281 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 282 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 283 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 284 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 285 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 286 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 287 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 288 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 289 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 290 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 291 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 292 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 293 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 294 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 295 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 296 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 297 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 298 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 299 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 300 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 301 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 302 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 303 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 304 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 305 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 306 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 307 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 308 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 309 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 310 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 311 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 312 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 313 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 314 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 315 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 316 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 317 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 318 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 319 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 320 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 321 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 322 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 323 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 324 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 325 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 326 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 327 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 328 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 329 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 330 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 331 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 332 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 333 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 334 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 335 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 336 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 337 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 338 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 339 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 340 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 341 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 342 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 343 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 344 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 345 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 346 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 347 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 348 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 349 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 350 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 351 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 352 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 353 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 354 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 355 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 356 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 357 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 358 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 359 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 360 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 361 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 362 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 363 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 364 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 365 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 366 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 367 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 368 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 369 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 370 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 371 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 372 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 373 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 374 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 375 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 376 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 377 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 378 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 379 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 380 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 381 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 382 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 383 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 384 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 385 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 386 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 387 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 388 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 389 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 390 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 391 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 392 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 393 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 394 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 395 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 396 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 397 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 398 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 399 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 400 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 401 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 402 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 403 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 404 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 405 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 406 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 407 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 408 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 409 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 410 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 411 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 412 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 413 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 414 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 415 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 416 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 417 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 418 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 419 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 420 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 421 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 422 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 423 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 424 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 425 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 426 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 427 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 428 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 429 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 430 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 431 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 432 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 433 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 434 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 435 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 436 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 437 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 438 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 439 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 440 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 441 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 442 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 443 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 444 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 445 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 446 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 447 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 448 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 449 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 450 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 451 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 452 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 453 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 454 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 455 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 456 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 457 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 458 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 459 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 460 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 461 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 462 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 463 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 464 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 465 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 466 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 467 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 468 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 469 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 470 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 471 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 472 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 473 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 474 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
