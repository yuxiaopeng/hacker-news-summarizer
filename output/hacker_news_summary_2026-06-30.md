# Hacker News 热门文章摘要 (2026-06-30)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Knoppix

**原文标题**: Knoppix

**原文链接**: [https://www.knopper.net/knoppix/index-en.html](https://www.knopper.net/knoppix/index-en.html)

生成摘要时出错

---

## 12. Crypto firms have spent $189M so far on 2026 US election, report says

**原文标题**: Crypto firms have spent $189M so far on 2026 US election, report says

**原文链接**: [https://www.reuters.com/world/crypto-firms-have-spent-189-million-so-far-2026-us-election-report-says-2026-06-30/](https://www.reuters.com/world/crypto-firms-have-spent-189-million-so-far-2026-us-election-report-says-2026-06-30/)

生成摘要时出错

---

## 13. Open Source Low Tech

**原文标题**: Open Source Low Tech

**原文链接**: [https://opensourcelowtech.org/](https://opensourcelowtech.org/)

生成摘要时出错

---

## 14. Building a custom octocopter from scratch with no prior hardware experience

**原文标题**: Building a custom octocopter from scratch with no prior hardware experience

**原文链接**: [https://karolina.mgdubiel.com/drone/](https://karolina.mgdubiel.com/drone/)

生成摘要时出错

---

## 15. Don't Make Gates Optional, Make Them Flexible

**原文标题**: Don't Make Gates Optional, Make Them Flexible

**原文链接**: [https://wakamoleguy.com/p/flexible-gates](https://wakamoleguy.com/p/flexible-gates)

生成摘要时出错

---

## 16. Factorio 2.1 Experimental Release

**原文标题**: Factorio 2.1 Experimental Release

**原文链接**: [https://factorio.com/blog/post/fff-444](https://factorio.com/blog/post/fff-444)

生成摘要时出错

---

## 17. European digital ID wallets rely on safety services of Google and Apple

**原文标题**: European digital ID wallets rely on safety services of Google and Apple

**原文链接**: [https://waag.org/en/article/european-digital-id-wallets-are-gift-google-and-apple/](https://waag.org/en/article/european-digital-id-wallets-are-gift-google-and-apple/)

生成摘要时出错

---

## 18. Zluda 6 release (run unmodified CUDA applications on non-Nvidia GPUs)

**原文标题**: Zluda 6 release (run unmodified CUDA applications on non-Nvidia GPUs)

**原文链接**: [https://vosen.github.io/ZLUDA/blog/zluda-update-q1q2-2026/](https://vosen.github.io/ZLUDA/blog/zluda-update-q1q2-2026/)

生成摘要时出错

---

## 19. Qwen 3.6 27B is the sweet spot for local development

**原文标题**: Qwen 3.6 27B is the sweet spot for local development

**原文链接**: [https://quesma.com/blog/qwen-36-is-awesome/](https://quesma.com/blog/qwen-36-is-awesome/)

生成摘要时出错

---

## 20. LongCat-2.0, a large-scale MoE model with 1.6T total and 48B Active

**原文标题**: LongCat-2.0, a large-scale MoE model with 1.6T total and 48B Active

**原文链接**: [https://longcat.chat/blog/longcat-2.0/](https://longcat.chat/blog/longcat-2.0/)

生成摘要时出错

---

## 21. We moved our Bluesky data to Eurosky

**原文标题**: We moved our Bluesky data to Eurosky

**原文链接**: [https://waag.org/en/article/why-we-moved-our-bluesky-data-eurosky/](https://waag.org/en/article/why-we-moved-our-bluesky-data-eurosky/)

生成摘要时出错

---

## 22. Mathematics: Its Content, Methods and Meaning

**原文标题**: Mathematics: Its Content, Methods and Meaning

**原文链接**: [https://old.maa.org/press/maa-reviews/mathematics-its-content-methods-and-meaning](https://old.maa.org/press/maa-reviews/mathematics-its-content-methods-and-meaning)

生成摘要时出错

---

## 23. Amazon Seller Reveals Rare Glimpse of Shadow Bribery Market

**原文标题**: Amazon Seller Reveals Rare Glimpse of Shadow Bribery Market

**原文链接**: [https://www.bloomberg.com/news/articles/2026-06-24/inside-the-shadow-market-selling-access-to-amazon-employees](https://www.bloomberg.com/news/articles/2026-06-24/inside-the-shadow-market-selling-access-to-amazon-employees)

生成摘要时出错

---

## 24. .self: A new top-level domain designed to support self-hosting

**原文标题**: .self: A new top-level domain designed to support self-hosting

**原文链接**: [https://hccf.onmy.cloud/2026/06/21/reclaiming-our-digital-selves-hccfs-vision-for-a-human-centered-top-level-domain/](https://hccf.onmy.cloud/2026/06/21/reclaiming-our-digital-selves-hccfs-vision-for-a-human-centered-top-level-domain/)

生成摘要时出错

---

## 25. Free the Icons

**原文标题**: Free the Icons

**原文链接**: [https://weblog.rogueamoeba.com/2026/06/26/free-the-icons/](https://weblog.rogueamoeba.com/2026/06/26/free-the-icons/)

生成摘要时出错

---

## 26. Exercise intensity influences body composition in healthy older adults (2025)

**原文标题**: Exercise intensity influences body composition in healthy older adults (2025)

**原文链接**: [https://www.maturitas.org/article/S0378-5122(25)00571-7/fulltext](https://www.maturitas.org/article/S0378-5122(25)00571-7/fulltext)

生成摘要时出错

---

## 27. The labor share of income in the US is at its lowest post-war level

**原文标题**: The labor share of income in the US is at its lowest post-war level

**原文链接**: [https://libertystreeteconomics.newyorkfed.org/2026/06/the-post-covid-decline-in-the-labor-share/](https://libertystreeteconomics.newyorkfed.org/2026/06/the-post-covid-decline-in-the-labor-share/)

生成摘要时出错

---

## 28. I'm building a Space Cadet Pinball Machine! [video]

**原文标题**: I'm building a Space Cadet Pinball Machine! [video]

**原文链接**: [https://www.youtube.com/watch?v=lHQ8c8i42VE](https://www.youtube.com/watch?v=lHQ8c8i42VE)

生成摘要时出错

---

## 29. Memory Safe Context Switching

**原文标题**: Memory Safe Context Switching

**原文链接**: [https://fil-c.org/context_switches](https://fil-c.org/context_switches)

生成摘要时出错

---

## 30. Rocketlab acquires Iridium

**原文标题**: Rocketlab acquires Iridium

**原文链接**: [https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-acquire-iridium-historic-deal-creating-fully](https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-acquire-iridium-historic-deal-creating-fully)

生成摘要时出错

---

## 31. Have You Restarted Your Computer This Week?

**原文标题**: Have You Restarted Your Computer This Week?

**原文链接**: [https://taonaw.com/2026/06/27/have-you-restarted-your-computer.html](https://taonaw.com/2026/06/27/have-you-restarted-your-computer.html)

生成摘要时出错

---

## 32. Linux for the Sega MegaDrive

**原文标题**: Linux for the Sega MegaDrive

**原文链接**: [https://github.com/LinuxMD/linuxmd](https://github.com/LinuxMD/linuxmd)

生成摘要时出错

---

## 33. 计算机辅助非言语儿童的语言发展 (1968) [pdf]

**原文标题**: Computer-Aided Language Development in Nonspeaking Children (1968) [pdf]

**原文链接**: [https://archive.org/details/colby1968-computer-aided-language-development-in-non-speaking-children](https://archive.org/details/colby1968-computer-aided-language-development-in-non-speaking-children)

生成摘要时出错

---

## 34. Parse, Don't Validate – In a Language That Doesn't Want You To

**原文标题**: Parse, Don't Validate – In a Language That Doesn't Want You To

**原文链接**: [https://cekrem.github.io/posts/parse-dont-validate-typescript/](https://cekrem.github.io/posts/parse-dont-validate-typescript/)

生成摘要时出错

---

## 35. All Logic, No Bite

**原文标题**: All Logic, No Bite

**原文链接**: [https://lcamtuf.substack.com/p/all-logic-no-bite](https://lcamtuf.substack.com/p/all-logic-no-bite)

生成摘要时出错

---

## 36. Ornith-1.0: self-improving open-source models for agentic coding

**原文标题**: Ornith-1.0: self-improving open-source models for agentic coding

**原文链接**: [https://github.com/deepreinforce-ai/Ornith-1](https://github.com/deepreinforce-ai/Ornith-1)

生成摘要时出错

---

## 37. Who are the fire-tamers?

**原文标题**: Who are the fire-tamers?

**原文链接**: [https://aeon.co/essays/who-are-the-fire-taming-healers-of-modern-france](https://aeon.co/essays/who-are-the-fire-taming-healers-of-modern-france)

生成摘要时出错

---

## 38. Exploring PDP-1 Lisp (1960)

**原文标题**: Exploring PDP-1 Lisp (1960)

**原文链接**: [https://obsolescence.dev/pdp1-lisp-introduction.html](https://obsolescence.dev/pdp1-lisp-introduction.html)

生成摘要时出错

---

## 39. Claude Desktop is now available on Linux (in beta)

**原文标题**: Claude Desktop is now available on Linux (in beta)

**原文链接**: [https://code.claude.com/docs/en/desktop-linux](https://code.claude.com/docs/en/desktop-linux)

生成摘要时出错

---

## 40. I Ported Kubernetes to the Browser

**原文标题**: I Ported Kubernetes to the Browser

**原文链接**: [https://ngrok.com/blog/i-ported-kubernetes-to-the-browser](https://ngrok.com/blog/i-ported-kubernetes-to-the-browser)

生成摘要时出错

---

## 41. Why problem statements aren't enough

**原文标题**: Why problem statements aren't enough

**原文链接**: [https://letters.unchartedpathbreakthroughs.com/posts/why-problem-statements-arent-enough](https://letters.unchartedpathbreakthroughs.com/posts/why-problem-statements-arent-enough)

生成摘要时出错

---

## 42. How to corrupt an SQLite database file

**原文标题**: How to corrupt an SQLite database file

**原文链接**: [https://www.sqlite.org/howtocorrupt.html](https://www.sqlite.org/howtocorrupt.html)

生成摘要时出错

---

## 43. US Supreme Court rules geofence warrants require constitutional protections

**原文标题**: US Supreme Court rules geofence warrants require constitutional protections

**原文链接**: [https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision)

生成摘要时出错

---

## 44. Apple Neural Engine: Architecture, Programming, and Performance

**原文标题**: Apple Neural Engine: Architecture, Programming, and Performance

**原文链接**: [https://arxiv.org/abs/2606.22283](https://arxiv.org/abs/2606.22283)

生成摘要时出错

---

## 45. New Claude app strings, Fable 5 coming back only with verification

**原文标题**: New Claude app strings, Fable 5 coming back only with verification

**原文链接**: [https://twitter.com/kimmonismus/status/2071868011804266828](https://twitter.com/kimmonismus/status/2071868011804266828)

生成摘要时出错

---

## 46. Supreme Court strikes down limits on party spending in federal elections

**原文标题**: Supreme Court strikes down limits on party spending in federal elections

**原文链接**: [https://apnews.com/article/supreme-court-campaign-finance-party-spending-ohio-91e49ee112197ae1210a9abfa46986ed](https://apnews.com/article/supreme-court-campaign-finance-party-spending-ohio-91e49ee112197ae1210a9abfa46986ed)

生成摘要时出错

---

## 47. Dark Sky Lighting

**原文标题**: Dark Sky Lighting

**原文链接**: [https://www.savingourstars.org/darkskylighting#whatisdarkskylighting](https://www.savingourstars.org/darkskylighting#whatisdarkskylighting)

生成摘要时出错

---

## 48. The US ambassador had Belgian police stop our reporting

**原文标题**: The US ambassador had Belgian police stop our reporting

**原文链接**: [https://europeancorrespondent.com/en/r/the-us-ambassador-had-belgian-police-stop-our-reporting](https://europeancorrespondent.com/en/r/the-us-ambassador-had-belgian-police-stop-our-reporting)

生成摘要时出错

---

## 49. The Freedom of Not Trying to Look Good

**原文标题**: The Freedom of Not Trying to Look Good

**原文链接**: [https://www.theatlantic.com/books/2026/06/fairyington-ugly-beauty-values-book-review/687662/](https://www.theatlantic.com/books/2026/06/fairyington-ugly-beauty-values-book-review/687662/)

生成摘要时出错

---

## 50. Zig – SPIR-V Backend Progress

**原文标题**: Zig – SPIR-V Backend Progress

**原文链接**: [https://ziglang.org/devlog/2026/#2026-06-26](https://ziglang.org/devlog/2026/#2026-06-26)

生成摘要时出错

---

## 51. Old Computer Challenge

**原文标题**: Old Computer Challenge

**原文链接**: [http://occ.sdf.org/](http://occ.sdf.org/)

生成摘要时出错

---

## 52. Anthropic has embedded hidden spyware-like code in Claude Code

**原文标题**: Anthropic has embedded hidden spyware-like code in Claude Code

**原文链接**: [https://twitter.com/IntCyberDigest/status/2071971609183678544](https://twitter.com/IntCyberDigest/status/2071971609183678544)

生成摘要时出错

---

## 53. A native graphical shell for SSH

**原文标题**: A native graphical shell for SSH

**原文链接**: [https://probablymarcus.com/blocks/2026/06/28/native-graphical-shell-for-SSH.html](https://probablymarcus.com/blocks/2026/06/28/native-graphical-shell-for-SSH.html)

生成摘要时出错

---

## 54. What happens when you run a CUDA kernel?

**原文标题**: What happens when you run a CUDA kernel?

**原文链接**: [https://fergusfinn.com/blog/what-happens-when-you-run-a-gpu-kernel/](https://fergusfinn.com/blog/what-happens-when-you-run-a-gpu-kernel/)

生成摘要时出错

---

## 55. WATaBoy: JIT-Ing Game Boy Instructions to WASM Beats a Native Interpreter

**原文标题**: WATaBoy: JIT-Ing Game Boy Instructions to WASM Beats a Native Interpreter

**原文链接**: [https://humphri.es/blog/WATaBoy/](https://humphri.es/blog/WATaBoy/)

生成摘要时出错

---

## 56. No Systemd

**原文标题**: No Systemd

**原文链接**: [https://nosystemd.org/](https://nosystemd.org/)

生成摘要时出错

---

## 57. Kb – Prolog Knowledge Base

**原文标题**: Kb – Prolog Knowledge Base

**原文链接**: [https://github.com/mat-mgm/kb-prolog](https://github.com/mat-mgm/kb-prolog)

生成摘要时出错

---

## 58. Sandia National Labs SA3000 8085 CPU

**原文标题**: Sandia National Labs SA3000 8085 CPU

**原文链接**: [https://www.cpushack.com/2026/06/03/sandia-national-labs-sa3000-8085-cpu/](https://www.cpushack.com/2026/06/03/sandia-national-labs-sa3000-8085-cpu/)

生成摘要时出错

---

## 59. Wallace the 6 inch f/2.8 telescope, building it, and hiking with it

**原文标题**: Wallace the 6 inch f/2.8 telescope, building it, and hiking with it

**原文链接**: [https://lucassifoni.info/blog/hiking-with-wallace/](https://lucassifoni.info/blog/hiking-with-wallace/)

生成摘要时出错

---

## 60. Working With AI: A concrete example

**原文标题**: Working With AI: A concrete example

**原文链接**: [https://htmx.org/essays/working-with-ai/](https://htmx.org/essays/working-with-ai/)

生成摘要时出错

---

## 61. Microsoft Needs Windows Lite

**原文标题**: Microsoft Needs Windows Lite

**原文链接**: [https://philipbohun.com/blog/0011.html](https://philipbohun.com/blog/0011.html)

生成摘要时出错

---

## 62. Supreme Court takes sledgehammer to federal regulatory structure

**原文标题**: Supreme Court takes sledgehammer to federal regulatory structure

**原文链接**: [https://www.npr.org/2026/06/29/nx-s1-5875161/supreme-court-takes-sledgehammer-to-much-of-federal-governments-regulatory-structure](https://www.npr.org/2026/06/29/nx-s1-5875161/supreme-court-takes-sledgehammer-to-much-of-federal-governments-regulatory-structure)

生成摘要时出错

---

## 63. What can you confidently guarantee about your software?

**原文标题**: What can you confidently guarantee about your software?

**原文链接**: [https://queue.acm.org/detail.cfm?id=3819084](https://queue.acm.org/detail.cfm?id=3819084)

生成摘要时出错

---

## 64. Ornith-1.0: Self-scaffolding LLMs for agentic coding

**原文标题**: Ornith-1.0: Self-scaffolding LLMs for agentic coding

**原文链接**: [https://deep-reinforce.com/ornith_1_0.html](https://deep-reinforce.com/ornith_1_0.html)

生成摘要时出错

---

## 65. One million passports leaked online

**原文标题**: One million passports leaked online

**原文链接**: [https://www.theverge.com/tech/947157/passports-data-breach-cannabis-club-systems-nefos-puffpal](https://www.theverge.com/tech/947157/passports-data-breach-cannabis-club-systems-nefos-puffpal)

生成摘要时出错

---

## 66. British Origami: the 1955 exhibition by Akira Yoshizawa (2005)

**原文标题**: British Origami: the 1955 exhibition by Akira Yoshizawa (2005)

**原文链接**: [https://www.britishorigami.org/cp-lister-list/the-1955-exhibition-by-akira-yoshizawa/](https://www.britishorigami.org/cp-lister-list/the-1955-exhibition-by-akira-yoshizawa/)

生成摘要时出错

---

## 67. Halvar's Guide to Entrepreneurship

**原文标题**: Halvar's Guide to Entrepreneurship

**原文链接**: [https://thomasdullien.github.io/guides/entrepreneurship/](https://thomasdullien.github.io/guides/entrepreneurship/)

生成摘要时出错

---

## 68. Rendering ray tracing in a database (ClickHouse)

**原文标题**: Rendering ray tracing in a database (ClickHouse)

**原文链接**: [https://github.com/ClickHouse/RayTracer](https://github.com/ClickHouse/RayTracer)

生成摘要时出错

---

## 69. HackerRank open sourced its ATS. My resume scored 90/100. Oh wait 74. No – 88

**原文标题**: HackerRank open sourced its ATS. My resume scored 90/100. Oh wait 74. No – 88

**原文链接**: [https://danunparsed.com/p/hackerrank-open-source-ats](https://danunparsed.com/p/hackerrank-open-source-ats)

生成摘要时出错

---

## 70. AWS puts $1B into new AI unit to embed engineers with customers

**原文标题**: AWS puts $1B into new AI unit to embed engineers with customers

**原文链接**: [https://www.cnbc.com/2026/06/30/aws-amazon-ai-forward-deployed-engineers.html](https://www.cnbc.com/2026/06/30/aws-amazon-ai-forward-deployed-engineers.html)

生成摘要时出错

---

## 71. Micro-Agent: Beat Frontier Models with Collaboration Inside Model API

**原文标题**: Micro-Agent: Beat Frontier Models with Collaboration Inside Model API

**原文链接**: [https://vllm.ai/blog/2026-06-29-micro-agent-frontier-models](https://vllm.ai/blog/2026-06-29-micro-agent-frontier-models)

生成摘要时出错

---

## 72. Rebuilding the Computer Room

**原文标题**: Rebuilding the Computer Room

**原文链接**: [https://alexwlchan.net/2026/computer-room/](https://alexwlchan.net/2026/computer-room/)

生成摘要时出错

---

## 73. Claude Sonnet 5

**原文标题**: Claude Sonnet 5

**原文链接**: [https://www.anthropic.com/news/claude-sonnet-5](https://www.anthropic.com/news/claude-sonnet-5)

生成摘要时出错

---

## 74. GLM 5.2 beats Claude in our benchmarks

**原文标题**: GLM 5.2 beats Claude in our benchmarks

**原文链接**: [https://semgrep.dev/blog/2026/we-have-mythos-at-home-glm-52-beats-claude-in-our-cyber-benchmarks/](https://semgrep.dev/blog/2026/we-have-mythos-at-home-glm-52-beats-claude-in-our-cyber-benchmarks/)

生成摘要时出错

---

## 75. The Return of Aspect Oriented Programming

**原文标题**: The Return of Aspect Oriented Programming

**原文链接**: [https://thomaswc.com/blog/the_return_of_aop.html](https://thomaswc.com/blog/the_return_of_aop.html)

生成摘要时出错

---

## 76. Samsung, SK Hynix, Micron Sued in US over Memory Price Fixing

**原文标题**: Samsung, SK Hynix, Micron Sued in US over Memory Price Fixing

**原文链接**: [https://en.sedaily.com/international/2026/06/29/samsung-sk-hynix-micron-sued-in-us-over-memory-price-fixing](https://en.sedaily.com/international/2026/06/29/samsung-sk-hynix-micron-sued-in-us-over-memory-price-fixing)

生成摘要时出错

---

## 77. Philae's extraordinary comet landing relived (2024)

**原文标题**: Philae's extraordinary comet landing relived (2024)

**原文链接**: [https://www.esa.int/Science_Exploration/Space_Science/Rosetta/Philae_s_extraordinary_comet_landing_relived](https://www.esa.int/Science_Exploration/Space_Science/Rosetta/Philae_s_extraordinary_comet_landing_relived)

生成摘要时出错

---

## 78. DGX Spark vs. Mac Studio and Halo

**原文标题**: DGX Spark vs. Mac Studio and Halo

**原文链接**: [https://aimultiple.com/dgx-spark-alternatives](https://aimultiple.com/dgx-spark-alternatives)

生成摘要时出错

---

## 79. South Korea to spend $1T on more memory chip production and humanoid robots

**原文标题**: South Korea to spend $1T on more memory chip production and humanoid robots

**原文链接**: [https://arstechnica.com/ai/2026/06/south-korea-to-spend-1t-on-more-memory-chip-production-and-humanoid-robots/](https://arstechnica.com/ai/2026/06/south-korea-to-spend-1t-on-more-memory-chip-production-and-humanoid-robots/)

生成摘要时出错

---

## 80. The CEO of Mullvad is the main financer of the Swedish Örebro party

**原文标题**: The CEO of Mullvad is the main financer of the Swedish Örebro party

**原文链接**: [https://det.social/@lostgen/116820546568940358](https://det.social/@lostgen/116820546568940358)

生成摘要时出错

---

## 81. Scientists reverse autism-like symptoms in mice

**原文标题**: Scientists reverse autism-like symptoms in mice

**原文链接**: [https://www.psypost.org/scientists-reverse-autism-like-symptoms-in-mice-by-repairing-shortened-nerve-cell-structures/](https://www.psypost.org/scientists-reverse-autism-like-symptoms-in-mice-by-repairing-shortened-nerve-cell-structures/)

生成摘要时出错

---

## 82. European ISPs Want Rightsholders Held Accountable for Overblocking Damage

**原文标题**: European ISPs Want Rightsholders Held Accountable for Overblocking Damage

**原文链接**: [https://torrentfreak.com/european-isps-want-rightsholders-held-accountable-for-overblocking-damage/](https://torrentfreak.com/european-isps-want-rightsholders-held-accountable-for-overblocking-damage/)

生成摘要时出错

---

## 83. JumpServer: Open-Source Privileged Access Management

**原文标题**: JumpServer: Open-Source Privileged Access Management

**原文链接**: [https://github.com/jumpserver/jumpserver](https://github.com/jumpserver/jumpserver)

生成摘要时出错

---

## 84. Popping the GPU Bubble

**原文标题**: Popping the GPU Bubble

**原文链接**: [https://moondream.ai/blog/popping-the-gpu-bubble](https://moondream.ai/blog/popping-the-gpu-bubble)

生成摘要时出错

---

## 85. Iran's new plan for the most important oil route: Make every ship pay to pass

**原文标题**: Iran's new plan for the most important oil route: Make every ship pay to pass

**原文链接**: [https://www.msn.com/en-us/news/world/iran-has-a-new-plan-for-the-world-s-most-important-oil-route-make-every-ship-pay-to-pass-and-washington-says-that-s-a-red-line/ar-AA26TOic](https://www.msn.com/en-us/news/world/iran-has-a-new-plan-for-the-world-s-most-important-oil-route-make-every-ship-pay-to-pass-and-washington-says-that-s-a-red-line/ar-AA26TOic)

生成摘要时出错

---

## 86. NUMA: Cores, memory, and the distance between them

**原文标题**: NUMA: Cores, memory, and the distance between them

**原文链接**: [https://edera.dev/stories/numa-part-1-cores-memory-and-the-distance-between-them](https://edera.dev/stories/numa-part-1-cores-memory-and-the-distance-between-them)

生成摘要时出错

---

## 87. Migrating to client-side load balancing at a million requests per second

**原文标题**: Migrating to client-side load balancing at a million requests per second

**原文链接**: [https://engineering.zalando.com/posts/2026/06/client-side-load-balancing.html](https://engineering.zalando.com/posts/2026/06/client-side-load-balancing.html)

生成摘要时出错

---

## 88. 30-year sentence for transporting zines is a five-alarm fire for free speech

**原文标题**: 30-year sentence for transporting zines is a five-alarm fire for free speech

**原文链接**: [https://theintercept.com/2026/06/26/daniel-sanchez-estrada-zines-prairieland-free-speech/](https://theintercept.com/2026/06/26/daniel-sanchez-estrada-zines-prairieland-free-speech/)

生成摘要时出错

---

## 89. The Radiation Exposure Lie

**原文标题**: The Radiation Exposure Lie

**原文链接**: [https://worksinprogress.co/issue/how-to-lie-about-radiation/](https://worksinprogress.co/issue/how-to-lie-about-radiation/)

生成摘要时出错

---

## 90. Dissecting Apple's Sparse Image Format (ASIF)

**原文标题**: Dissecting Apple's Sparse Image Format (ASIF)

**原文链接**: [https://schamper.dev/dissecting-apples-sparse-image-format-asif/](https://schamper.dev/dissecting-apples-sparse-image-format-asif/)

生成摘要时出错

---

## 91. Age verification is just a precursor to automated attribution of speech

**原文标题**: Age verification is just a precursor to automated attribution of speech

**原文链接**: [https://nonogra.ph/age-verification-is-just-a-precursor-to-attribution-of-speech-06-29-2026](https://nonogra.ph/age-verification-is-just-a-precursor-to-attribution-of-speech-06-29-2026)

生成摘要时出错

---

## 92. Gemma 4 on Cerebras - The Fastest Inference Is Now Multimodal

**原文标题**: Gemma 4 on Cerebras - The Fastest Inference Is Now Multimodal

**原文链接**: [https://www.cerebras.ai/blog/gemma-4-on-cerebras-the-fastest-inference-is-now-multimodal](https://www.cerebras.ai/blog/gemma-4-on-cerebras-the-fastest-inference-is-now-multimodal)

生成摘要时出错

---

## 93. NixOS 26.05

**原文标题**: NixOS 26.05

**原文链接**: [https://nixos.org/blog/announcements/2026/nixos-2605/](https://nixos.org/blog/announcements/2026/nixos-2605/)

生成摘要时出错

---

## 94. Pollen tried to remove my article and Google is assisting with it

**原文标题**: Pollen tried to remove my article and Google is assisting with it

**原文链接**: [https://blog.pragmaticengineer.com/pollen-tried-to-remove-my-article-about-callum-negus-fancey-and-google-is-assisting-to-it/](https://blog.pragmaticengineer.com/pollen-tried-to-remove-my-article-about-callum-negus-fancey-and-google-is-assisting-to-it/)

生成摘要时出错

---

## 95. Changes to Our Contribution Policies

**原文标题**: Changes to Our Contribution Policies

**原文链接**: [https://godotengine.org/article/contribution-policy-2026/](https://godotengine.org/article/contribution-policy-2026/)

生成摘要时出错

---

## 96. Venetian Bridge Brawls in 17th and 18th Century Art

**原文标题**: Venetian Bridge Brawls in 17th and 18th Century Art

**原文链接**: [https://publicdomainreview.org/collection/venice-bridge-fights/](https://publicdomainreview.org/collection/venice-bridge-fights/)

生成摘要时出错

---

## 97. Is sunscreen the new margarine? (2019)

**原文标题**: Is sunscreen the new margarine? (2019)

**原文链接**: [https://www.outsideonline.com/health/wellness/sunscreen-sun-exposure-skin-cancer-science/](https://www.outsideonline.com/health/wellness/sunscreen-sun-exposure-skin-cancer-science/)

生成摘要时出错

---

## 98. Font-Family Recommendations

**原文标题**: Font-Family Recommendations

**原文链接**: [https://chrismorgan.info/font-family](https://chrismorgan.info/font-family)

生成摘要时出错

---

## 99. Cursor now has a mobile app for guiding your coding agent on the go

**原文标题**: Cursor now has a mobile app for guiding your coding agent on the go

**原文链接**: [https://techcrunch.com/2026/06/29/cursor-now-has-a-mobile-app-for-guiding-your-coding-agent-on-the-go/](https://techcrunch.com/2026/06/29/cursor-now-has-a-mobile-app-for-guiding-your-coding-agent-on-the-go/)

生成摘要时出错

---

## 100. Supabase (YC S20) Is Hiring for Multigres

**原文标题**: Supabase (YC S20) Is Hiring for Multigres

**原文链接**: [https://jobs.ashbyhq.com/supabase/2e718684-4f75-4a99-8d6b-3b6bd44e4228](https://jobs.ashbyhq.com/supabase/2e718684-4f75-4a99-8d6b-3b6bd44e4228)

生成摘要时出错

---

