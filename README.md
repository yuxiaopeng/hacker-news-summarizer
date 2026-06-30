# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-06-30.md)

*最后自动更新时间: 2026-06-30 19:26:32*
## 1. Claude Sonnet 5

**原文标题**: Claude Sonnet 5

**原文链接**: [https://www.anthropic.com/news/claude-sonnet-5](https://www.anthropic.com/news/claude-sonnet-5)

Anthropic 宣布发布 Claude Sonnet 5（截至 2026 年 6 月 30 日），该模型被定位为 Sonnet 系列中“自主代理能力”最强的模型。Sonnet 5 旨在弥合中端与高端模型之间的差距，其性能接近 Opus 4.8，但价格显著降低。

**核心能力与性能**
Sonnet 5 在自主任务方面表现卓越，包括规划、编程以及使用浏览器和终端等工具。相较于 Sonnet 4.6，它在推理、知识性工作和多步执行方面实现了实质性升级。早期测试者报告称，该模型在“全程执行”方面表现更好——能够完成复杂的软件工程任务并调试现有代码而不会停滞。在 BrowseComp（代理搜索）和 OSWorld（计算机操作）等评估中，它相较于前代产品有显著提升，允许开发人员通过调整“投入水平”来平衡成本和准确性。

**安全性与网络安全**
安全评估表明，Sonnet 5 比 Sonnet 4.6 更可靠，幻觉、谄媚及不良行为的发生率更低。值得注意的是，其网络安全能力受到了刻意限制；它不具备 Opus 模型中那种先进的漏洞利用开发技能，并内置了默认的网络安全防护措施以阻止危险用途。

**价格与可用性**
该模型现已向所有 Claude 用户（免费版、Pro、Max、Team 和 Enterprise）以及通过 Claude API 开放。
*   **首发优惠价（至 2026 年 8 月 31 日）：** 每百万输入 Token 为 2 美元 / 每百万输出 Token 为 10 美元。
*   **标准价格：** 每百万输入 Token 为 3 美元 / 每百万输出 Token 为 15 美元。

用户需注意，Sonnet 5 使用了更新的分词器（tokenizer），在提升性能的同时，根据内容的不同，Token 数量可能会增加约 1.0–1.35 倍。

---

## 2. Claude Code 正在隐写标记请求。

**原文标题**: Claude Code is steganographically marking requests

**原文链接**: [https://thereallo.dev/blog/claude-code-prompt-steganography](https://thereallo.dev/blog/claude-code-prompt-steganography)

Lo 发表的《Claude Code 正在通过隐写术标记请求》一文揭示，Anthropic 新发布的命令行界面（CLI）工具 **Claude Code** 正利用隐写术悄悄地在用户提示词中嵌入元数据。

通过分析网络流量，作者发现该 CLI 工具会在发送给大语言模型（LLM）的文本中注入一系列不可见的 Unicode 字符——特别是**零宽空格 (U+200B)** 和**零宽不连通空格 (U+200C)**。这些字符充当了二进制编码的“指纹”。虽然用户在终端中看不到它们，但它们存在于发送到 Anthropic 服务器的原始负载中。

这种行为的主要目的似乎是**遥测和识别**。通过以这种方式标记请求，Anthropic 可以将 Claude Code CLI 生成的流量与其他 API 或网页端的交互区分开来，即使用户尝试剥离或修改标准的标识请求头。

作者指出，虽然这是一种用于跟踪产品使用情况和归属的巧妙工程技巧，但它引发了有关透明度的质疑。这实际上是在用户不知情的情况下为提示词添加了“水印”。尽管这些字符不可打印，且通常不会影响大语言模型的语言输出，但它们代表了一个隐藏的数据传输层。这一发现凸显了 AI 公司在跟踪工具采用情况、以及监控其模型在各种环境下如何被访问和利用时所采用的微妙方式。

---

## 3. 我们是最后一批了解其运作原理的人。

**原文标题**: We Are the Last People Who Know How It Works

**原文链接**: [https://unix.foo/posts/last-people-who-know-how-it-works/](https://unix.foo/posts/last-people-who-know-how-it-works/)

本文反思了人与技术之间不断演变的关系，将20世纪90年代“高摩擦”的计算环境与现代人工智能时代的无缝便捷进行了对比。

作者指出，早期的计算机技术需要用户对软硬件有深刻的手动理解。为了玩游戏或连接互联网，用户必须处理配置文件、设置硬件跳线，并解读调制解调器的“握手协商”。这种阻力创造了一种独特的“熟稔感”——一种源于努力让机器运转而产生的亲密。你了解机器，正是因为它在挑战你。

相比之下，现代技术和人工智能旨在消除所有摩擦。这些工具极尽顺从，对用户别无所求，并能即时调整自身以满足需求。作者认为，虽然我们并没有丧失“胜任力”——因为人工智能模型存储的技术知识已远超人类——但我们正在失去“熟稔感”。我们比以往任何时候都更加依赖工具，却对它们前所未有地陌生。

最终，作者断言，我们是通过“困难”来了解机器的最后一代人。尽管年轻一代不会感到失落，因为他们从未需要为了让设备工作而与之“搏斗”，但在这种转型中却蕴含着一种独特的哀伤。我们亲手打造了梦寐以求的、充满便利的世界，但在这个过程中，我们也牺牲了那种唯有在克服机器阻力时才能建立的深层联系。

---

## 4. Claude 科学

**原文标题**: Claude Science

**原文链接**: [https://claude.com/product/claude-science](https://claude.com/product/claude-science)

**Claude Science** 是 Anthropic 推出的全新测试版应用，旨在为科学家（尤其是生命科学和“硬科学”领域的研究人员）提供专业的研究工作平台。与通用的 AI 助手不同，Claude Science 专为执行复杂分析、管理计算环境以及维持严谨的科学标准而设计。

**核心功能与能力：**
*   **可复现性与溯源性：** 每一个生成的产出物（包括图表、表格和笔记本）都会永久链接到生成它的确切代码、环境和对话历史。这确保了结果在数月后仍可被审计、编辑或复现。
*   **科学工具与渲染：** 该应用内置了分子结构、基因组轨道、蛋白质比对和化学结构的原生渲染器，并集成了 60 多个科学数据库及 NVIDIA BioNeMo 等工具。
*   **高级计算管理：** 它支持管理本地机器、Linux 工作站以及 HPC 集群（通过 SSH 或 Slurm）的计算环境。持久化的 Python 和 R 内核允许变量和模型驻留在内存中，从而实现更快速的迭代。
*   **智能代理审核：** 后台审核机制会自动标记错误的引用、无法追溯的数据以及与底层代码不匹配的图表。
*   **领域专业知识：** 该应用预置了针对基因组学、蛋白质组学、化学信息学和结构生物学等领域的专业配置。

**可用性与获取：**
Claude Science 目前面向 Pro、Team 和 Enterprise 方案的 macOS 和 Linux 用户开放。Anthropic 专门为学术和非营利研究实验室提供折扣版 Team 方案，需通过首席研究员（PI）进行身份验证。虽然该应用使用的是现有的 Claude 模型，但它提供了专业科学研究所需的特定基础设施、工具连接器和数据溯源功能。

---

## 5. 纳米香蕉 2 Lite

**原文标题**: Nano Banana 2 Lite

**原文链接**: [https://deepmind.google/models/gemini-image/flash-lite/](https://deepmind.google/models/gemini-image/flash-lite/)

**Nano Banana 2 Lite** 致力于通过显著降低延迟来最大化效率。凭借其高速性能，该设备能够让用户快速进行探索与迭代，确保工作流程无缝且不间断。

---

## 6. I built a mmWave material classification radar

**原文标题**: I built a mmWave material classification radar

**原文链接**: [https://gauthier-lechevalier.com/radar](https://gauthier-lechevalier.com/radar)

This article details the development of a portable mmWave radar designed to classify materials, specifically targeting the detection of asbestos in buildings to bypass expensive lab testing. The author, a recent engineering graduate, utilized a Texas Instruments IWRL6432 radar sensor and an ESP32 microcontroller to build the prototype.

**Technical Execution**
The device uses Frequency Modulated Continuous Wave (FMCW) radar. The Digital Signal Processing (DSP) chain involves:
*   **Chirp Characterization:** Emitting and measuring linear frequency sweeps.
*   **Range FFT:** Converting beat signals into distance data to map reflected energy.
*   **Capon Beamforming:** Resolving the angle of arrival to create a sharp "density spectre" or electromagnetic fingerprint.
*   **AI Classification:** This fingerprint is fed into a Convolutional Neural Network (CNN) that learns the dielectric properties ($\epsilon'$ and $\epsilon''$) of materials to identify their composition.

For RF design, the author used **OpenEMS** (an open-source FDTD simulator). To save time, they developed a shortcut by calculating the system's transfer function with a Gaussian pulse and using convolution to simulate chirp reflections, reducing simulation times from hours to minutes.

**Business Outcome and Lessons**
While the proof-of-concept successfully classified various materials (wood, plastics, stone), the startup failed due to a lack of funding. The author encountered a "chicken and egg" problem: customers refused to sign Letters of Intent (LOIs) without regulatory clearances, but clearances required more capital. 

**Key takeaways include:**
1.  **Validate first:** Use preorders and landing pages to confirm willingness to pay before building.
2.  **Stay Lean:** Prototype with dev boards and design casings around electronics, not vice-versa.
3.  **Software-First Mindset:** Use OTA (Over-the-Air) updates to keep hardware flexible and upgradable.

---

## 7. Looking Ahead to Postgres 19

**原文标题**: Looking Ahead to Postgres 19

**原文链接**: [https://www.snowflake.com/en/blog/engineering/postgresql-19-features-beta/](https://www.snowflake.com/en/blog/engineering/postgresql-19-features-beta/)

生成摘要时出错

---

## 8. Xsnow "protestware" in Debian

**原文标题**: Xsnow "protestware" in Debian

**原文链接**: [https://lwn.net/SubscriberLink/1079385/3d7a57da58b41aa9/](https://lwn.net/SubscriberLink/1079385/3d7a57da58b41aa9/)

生成摘要时出错

---

## 9. County with 37 Data Centers Asks Schools to 'Conserve Electricity'

**原文标题**: County with 37 Data Centers Asks Schools to 'Conserve Electricity'

**原文链接**: [https://www.404media.co/henrico-virginia-datacenter-energy-cost-email/](https://www.404media.co/henrico-virginia-datacenter-energy-cost-email/)

生成摘要时出错

---

## 10. Memoirs of Extraordinary Popular Delusions and the Madness of Crowds (1852)

**原文标题**: Memoirs of Extraordinary Popular Delusions and the Madness of Crowds (1852)

**原文链接**: [https://www.gutenberg.org/ebooks/24518](https://www.gutenberg.org/ebooks/24518)

*Memoirs of Extraordinary Popular Delusions and the Madness of Crowds*, written by Charles Mackay and originally published in 1841, is a seminal journalistic study of crowd psychology and collective human folly. The work explores how various societies throughout history have succumbed to irrational manias, ranging from economic bubbles to religious and social delusions.

The book is divided into several thematic areas, notably covering:
*   **Economic Bubbles:** Mackay provides detailed accounts of famous financial crashes, including the Mississippi Scheme, the South Sea Bubble, and the Dutch "Tulipomania."
*   **Pseudo-Science and the Occult:** He examines the history of alchemy, fortune-telling, and the "magnetisers."
*   **Social and Religious Manias:** The text delves into the Crusades, the witch-hunting craze, the influence of politics on hair and beard styles, and the popular admiration for notorious thieves.

Mackay’s work is celebrated for its colorful storytelling and its enduring relevance to the field of behavioral economics. His analysis of market speculation remains a foundational text for financiers attempting to understand and predict modern market crashes. 

The version described is a Project Gutenberg eBook (No. 24518), which entered the public domain in 2008. It is available in multiple digital formats, including EPUB and Kindle, and is categorized under social psychology, economics, and history. With a reading ease score suitable for 8th and 9th graders, it remains an accessible and influential critique of human irrationality.

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 2 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 3 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 4 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 5 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 6 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 7 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 8 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 9 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 10 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 11 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 12 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 13 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 14 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 15 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 16 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 17 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 18 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 19 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 20 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 21 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 22 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 23 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 24 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 25 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 26 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 27 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 28 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 29 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 30 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 31 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 32 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 33 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 34 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 35 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 36 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 37 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 38 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 39 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 40 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 41 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 42 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 43 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 44 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 45 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 46 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 47 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 48 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 49 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 50 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 51 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 52 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 53 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 54 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 55 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 56 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 57 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 58 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 59 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 60 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 61 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 62 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 63 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 64 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 65 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 66 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 67 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 68 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 69 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 70 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 71 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 72 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 73 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 74 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 75 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 76 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 77 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 78 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 79 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 80 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 81 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 82 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 83 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 84 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 85 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 86 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 87 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 88 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 89 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 90 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 91 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 92 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 93 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 94 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 95 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 96 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 97 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 98 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 99 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 100 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 101 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 102 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 103 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 104 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 105 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 106 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 107 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 108 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 109 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 110 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 111 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 112 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 113 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 114 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 115 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 116 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 117 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 118 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 119 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 120 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 121 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 122 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 123 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 124 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 125 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 126 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 127 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 128 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 129 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 130 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 131 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 132 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 133 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 134 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 135 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 136 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 137 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 138 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 139 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 140 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 141 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 142 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 143 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 144 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 145 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 146 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 147 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 148 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 149 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 150 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 151 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 152 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 153 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 154 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 155 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 156 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 157 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 158 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 159 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 160 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 161 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 162 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 163 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 164 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 165 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 166 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 167 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 168 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 169 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 170 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 171 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 172 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 173 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 174 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 175 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 176 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 177 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 178 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 179 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 180 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 181 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 182 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 183 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 184 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 185 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 186 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 187 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 188 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 189 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 190 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 191 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 192 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 193 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 194 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 195 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 196 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 197 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 198 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 199 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 200 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 201 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 202 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 203 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 204 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 205 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 206 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 207 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 208 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 209 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 210 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 211 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 212 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 213 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 214 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 215 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 216 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 217 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 218 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 219 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 220 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 221 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 222 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 223 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 224 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 225 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 226 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 227 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 228 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 229 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 230 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 231 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 232 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 233 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 234 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 235 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 236 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 237 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 238 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 239 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 240 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 241 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 242 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 243 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 244 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 245 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 246 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 247 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 248 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 249 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 250 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 251 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 252 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 253 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 254 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 255 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 256 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 257 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 258 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 259 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 260 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 261 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 262 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 263 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 264 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 265 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 266 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 267 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 268 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 269 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 270 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 271 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 272 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 273 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 274 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 275 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 276 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 277 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 278 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 279 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 280 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 281 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 282 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 283 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 284 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 285 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 286 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 287 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 288 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 289 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 290 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 291 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 292 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 293 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 294 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 295 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 296 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 297 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 298 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 299 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 300 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 301 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 302 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 303 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 304 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 305 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 306 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 307 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 308 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 309 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 310 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 311 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 312 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 313 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 314 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 315 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 316 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 317 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 318 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 319 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 320 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 321 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 322 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 323 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 324 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 325 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 326 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 327 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 328 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 329 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 330 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 331 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 332 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 333 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 334 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 335 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 336 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 337 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 338 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 339 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 340 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 341 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 342 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 343 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 344 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 345 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 346 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 347 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 348 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 349 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 350 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 351 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 352 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 353 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 354 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 355 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 356 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 357 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 358 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 359 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 360 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 361 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 362 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 363 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 364 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 365 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 366 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 367 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 368 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 369 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 370 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 371 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 372 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 373 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 374 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 375 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 376 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 377 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 378 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 379 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 380 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 381 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 382 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 383 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 384 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 385 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 386 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 387 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 388 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 389 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 390 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 391 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 392 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 393 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 394 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 395 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 396 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 397 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 398 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 399 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 400 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 401 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 402 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 403 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 404 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 405 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 406 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 407 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 408 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 409 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 410 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 411 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 412 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 413 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 414 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 415 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 416 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 417 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 418 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 419 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 420 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 421 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 422 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 423 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 424 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 425 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 426 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 427 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 428 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 429 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 430 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 431 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 432 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 433 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 434 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 435 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 436 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 437 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 438 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 439 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 440 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 441 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 442 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 443 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 444 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 445 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 446 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 447 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 448 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 449 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 450 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 451 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 452 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 453 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 454 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 455 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 456 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 457 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 458 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 459 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 460 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 461 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 462 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 463 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 464 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 465 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 466 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 467 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
