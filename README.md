# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-08-22.md)

*最后自动更新时间: 2025-08-22 17:48:29*
## 1. FFmpeg 8.0

**原文标题**: FFmpeg 8.0

**原文链接**: [https://ffmpeg.org/index.html#pr8.0](https://ffmpeg.org/index.html#pr8.0)

本文记录了FFmpeg这一跨平台音视频录制、转换和流媒体解决方案从6.0版本到即将发布的8.0版本的演变历程。

**FFmpeg 8.0 "Huffman" (2025年8月):** 这一主要版本强调现代化，引入了新的原生解码器（APV、ProRes RAW、RealVideo 6.0、三洋 LD-ADPCM、G.728），改进了VVC解码器，并引入了基于Vulkan计算的编解码器（FFv1、ProRes RAW）。硬件加速扩展到Vulkan VP9、VAAPI VVC和OpenHarmony H264/5。基础设施已通过升级邮件列表和新的贡献平台实现了现代化。

**以往版本:**

*   **FFmpeg 7.1 "Péter" (2024年9月):** 包含稳定的VVC解码器、原生AAC USAC解码器、MV-HEVC解码支持，以及用于H264/HEVC的Vulkan编码。还包括改进的色彩范围处理以及对Matroska和MP4格式的裁剪元数据支持。
*   **其他更新 (2024):** 值得注意的事件包括Coverity对代码质量的认可、原生xHE-AAC解码器以及德国Sovereign Tech Fund的赞助。
*   **FFmpeg 7.0 "Dijkstra" (2024年4月):** 引入了原生VVC解码器（实验性）、IAMF支持以及多线程ffmpeg CLI工具。此版本不向后兼容，删除了已弃用的API。
*   **FFmpeg 6.1 "Heaviside" (2023年11月):** 包含各种新的解码器、解复用器、过滤器，并支持Vulkan解码加速。致力于改进时间戳和帧时长。
*   **FFmpeg 6.0 "Von Neumann" (2023年2月):** 这标志着发布策略的改变，具有更频繁的主要版本发布和ABI版本升级。它引入了新的编码器、解码器、过滤器，并提高了ffmpeg CLI工具的性能。值得注意的是，增加了QSV和NVenc对AV1编码的支持。

本文重点介绍了该项目为提高性能、添加新的编解码器支持以及改善整体稳定性和功能所做的持续努力，以及向Vulkan等标准化API的转变。

---

## 2. 我的开发团队每月花费 41.73 美元。

**原文标题**: My development team costs $41.73 a month

**原文链接**: [https://philipotoole.com/my-development-team-costs-41-73-a-month/](https://philipotoole.com/my-development-team-costs-41-73-a-month/)

作者反思了之前关于大型语言模型(LLMs)对软件开发产生变革性影响的预测，现在认为这已成为现实。基于提交次数和代码更改行数，AI赋能的编程助手GitHub Copilot已成为作者开源数据库项目rqlite的第二大贡献者。作者描述了一种协作流程，Copilot根据提供的目标生成代码，然后由作者审查和改进，类似于与初级开发人员合作。

然而，这种协作缺乏人际互动的开发和情境要素。Copilot不会保留信息或从之前的互动中学习，从而阻碍了共享项目理解和指导机会。

尽管存在这些局限性，作者认为Copilot每月仅需41.73美元（含税）的低廉价格，使得这种权衡是值得的，从而导致软件开发经济学发生了深刻的转变。作者认为，这种廉价且容易获得的AI辅助将重塑软件的创建方式，即使它牺牲了人际协作和程序员发展的某些方面。

---

## 3. Io_uring、kTLS与Rust打造零系统调用HTTPS服务器

**原文标题**: Io_uring, kTLS and Rust for zero syscall HTTPS server

**原文链接**: [https://blog.habets.se/2025/04/io-uring-ktls-and-rust-for-zero-syscall-https-server.html](https://blog.habets.se/2025/04/io-uring-ktls-and-rust-for-zero-syscall-https-server.html)

本文深入探讨了使用现代 Linux 内核特性优化 Web 服务器性能的方法，重点在于消除系统调用开销。作者首先概述了 Web 服务器架构的历史演变，从预先派生到 `select`/`poll`，最终到 `epoll`。虽然 `epoll` 显著提高了性能，但系统调用仍然构成相当大的成本。

文章随后介绍了 `io_uring`，这是一种 Linux 内核特性，允许应用程序异步地将操作排队，从而减少了频繁系统调用的需求。Web 服务器将命令写入队列，内核处理这些命令并将完成通知添加到另一个队列。这种方法允许繁忙的 Web 服务器在初始设置后，有可能在没有任何系统调用的情况下为请求提供服务。

作者强调了利用多个 CPU 核心和 NUMA 感知内存访问对于优化性能的重要性。其他优化包括预先分配内存以避免动态分配系统调用。

此外，文章还讨论了 `kTLS`，即内核级 TLS 加密，它将加密/解密卸载到内核，从而可以使用 `sendfile()` 并可能使用硬件加速。通过 `register_files` 实现的无描述符文件也有助于性能，因为它避免了文件描述符的传递。

作者的项目 `tarweb`，一个从 tar 文件提供内容的 Web 服务器，是使用 Rust 实现这些技术的实际示例。文章还探讨了在 Rust 中使用 `io_uring` 的挑战，特别是缓冲区管理缺乏编译时安全性，并建议需要一个更安全的包装箱。未来计划进行基准测试。

---

## 4. 面向专家程序员的通用人工智能/大型语言模型“氛围编码”指南

**原文标题**: A Guide to Gen AI / LLM Vibecoding for Expert Programmers

**原文链接**: [https://www.stochasticlifestyle.com/a-guide-to-gen-ai-llm-vibecoding-for-expert-programmers/](https://www.stochasticlifestyle.com/a-guide-to-gen-ai-llm-vibecoding-for-expert-programmers/)

Christopher Rackauckas认为，与GenAI/LLMs进行的“凭感觉编程”不仅适用于初学者；对于能够将这些工具用作初级团队成员的专家程序员来说，这种方式最为有效。他挑战了经验丰富的开发者“不屑于”凭感觉编程的观点，并断言他们才是唯一能够真正高效地做到这一点的人。

他将LLM代理比作二年级实习生：有能力进行基本编程、复制架构、运行测试和使用搜索引擎，但缺乏深刻的理解。他建议像对待一组实习生一样对待LLM，分配你熟悉的任务，审查他们的代码，并提供反馈。

成功进行凭感觉编程的关键在于同时管理多个代理，为他们分配直接的任务，例如重构、修复错误或编写文档。他强调快速丢弃不良或偏离方向的结果，并专注于最大化总体成功，而不是纠结于成功率的重要性。

Rackauckas强调，凭感觉编程最适合应用于专家非常熟悉的代码库，从而能够快速进行代码审查并识别问题。文章总结说，凭感觉编程将经验丰富的程序员转变为能够领导大型“实习生”团队的CTO，从而加速开发并使专家能够专注于最具挑战性的问题。作者警告说，需要一位经验丰富且训练有素的程序员才能正确处理并有效地使用生成式AI的凭感觉编程。

---

## 5. LabPlot: 免费、开源、跨平台的数据可视化与分析

**原文标题**: LabPlot: Free, open source and cross-platform Data Visualization and Analysis

**原文链接**: [https://labplot.org/](https://labplot.org/)

LabPlot 2.12.1小补丁版本现已发布，由Alexander Semke于2025年8月18日宣布。此版本专注于修复错误和对应用程序各个领域的细微改进。建议用户更新至此版本。该公告未详细说明具体的错误修复或改进，仅说明它们“分布在应用程序的许多不同领域”。摘要中未提供关于可用性的更多信息。

---

## 6. 通过性能效率优化路由降低大型语言模型的成本并提高其性能

**原文标题**: Making LLMs Cheaper and Better via Performance-Efficiency Optimized Routing

**原文链接**: [https://arxiv.org/abs/2508.12631](https://arxiv.org/abs/2508.12631)

该arXiv文章于2025年8月18日提交，介绍了Avengers-Pro，一种新颖的测试时路由框架，旨在优化大型语言模型（LLM）中的性能-效率权衡。其核心思想是集成不同容量和效率的LLM，并根据性能-效率得分将传入查询动态路由到最合适的模型。

Avengers-Pro框架首先嵌入并聚类传入查询。然后，它使用这些集群将查询智能地路由到集成中最合适的模型。这提供了一个统一的解决方案，解决了LLM中性能和计算成本之间固有的张力。

作者张亦群等人展示了Avengers-Pro在六个具有挑战性的基准测试和八个领先模型（包括未来的GPT-5-medium、Gemini-2.5-pro和Claude-opus-4.1）上的有效性。他们报告了最先进的结果，表明Avengers-Pro可以超过最强单一模型（GPT-5-medium）的准确率7%。此外，它可以以低27%的成本达到最强模型的准确率，并以低63%的成本实现~90%的性能。值得注意的是，Avengers-Pro实现了帕累托前沿，与单一模型相比，它在给定成本下提供最高的准确率，在给定准确率下提供最低的成本。

该工作正在进行中，代码可在提供的URL处获得。作者将Avengers-Pro定位为使LLM更便宜和更好的关键进展。

---

## 7. 兆赫兹还重要吗？

**原文标题**: Does MHz Still Matter?

**原文链接**: [https://www.ubicloud.com/blog/does-mhz-still-matter](https://www.ubicloud.com/blog/does-mhz-still-matter)

MHz还重要吗？

这篇 Ubicloud 博客文章“MHz 还重要吗？”探讨了单核 CPU 性能对实际云工作负载的影响。 他们在其基础设施上比较了 AMD Ryzen 9 7950X3D（游戏专用，单核性能强劲）和 AMD EPYC 9454P（数据中心 CPU）。

他们发现，在各种基准测试和实际场景中，Ryzen CPU 的性能始终优于 EPYC CPU。 最初的单核基准测试显示 Ryzen 的性能大约提高了 32%。 GitHub Actions Runner 测试（模拟典型的云工作负载）也显示 Ryzen 带来了显著的性能提升，尤其是在较短的任务中。

有趣的是，当工作负载涉及 CPU 和磁盘 I/O 时，PostgreSQL 基准测试显示出更大的性能差异（约 60%）。 这归因于 Ubicloud 使用 SPDK 实现的加密块存储的 CPU 密集型特性，其中更快的 CPU 核心加速了加密/解密过程，从而提高了 I/O 吞吐量。

结论是，单核性能在云环境中仍然非常重要，尤其是在短时任务和涉及加密的 I/O 密集型工作负载中。 更快的核心可以减少等待时间并提高整体性能。 Ubicloud 计划继续优先考虑具有强大单核性能的硬件，以提高其平台上运行的工作负载的速度，而无需任何代码更改。

---

## 8. DeepSeek-v3.1

**原文标题**: DeepSeek-v3.1

**原文链接**: [https://api-docs.deepseek.com/news/news250821](https://api-docs.deepseek.com/news/news250821)

DeepSeek-V3.1发布，通过增强的Agent能力和提供“思考”与“非思考”两种模式的混合推理系统，标志着向“Agent时代”迈进了一步。“思考”模式比以前的版本(DeepSeek-R1-0528)更快，更适合Agent任务，而“非思考”是标准聊天模式。

主要更新包括：

*   **混合推理：** 通过DeepSeek聊天平台上的切换按钮访问思考/非思考模式。
*   **API更新：** `deepseek-chat` 用于非思考模式，`deepseek-reasoner` 用于思考模式。两者均支持128K上下文、Anthropic API格式和严格的函数调用（Beta API）。
*   **Agent/工具升级：** 在SWE和Terminal-Bench等基准测试中性能提升，更强的复杂搜索多步骤推理能力，以及更高的思考效率。
*   **模型更新：** V3.1基础模型拥有8400亿 tokens，持续预训练，更新的分词器/聊天模板。V3.1基础模型和V3.1的开源权重可用。
*   **定价变更：** 新定价和非高峰时段折扣的结束将于UTC时间2025年9月5日16:00开始。在此之前，当前定价保持不变。

---

## 9. 氛围调试：企业冉冉升起的新噩梦

**原文标题**: Vibe Debugging: Enterprises' Up and Coming Nightmare

**原文链接**: [https://marketsaintefficient.substack.com/p/vibe-debugging-enterprises-up-and](https://marketsaintefficient.substack.com/p/vibe-debugging-enterprises-up-and)

无法访问文章链接。

---

## 10. 使用rel="share-url"来暴露分享意图怎么样？

**原文标题**: What about using rel="share-url" to expose sharing intents?

**原文链接**: [https://shkspr.mobi/blog/2025/08/what-about-using-relshare-url-to-expose-sharing-intents/](https://shkspr.mobi/blog/2025/08/what-about-using-relshare-url-to-expose-sharing-intents/)

本文提出了一种新的 HTML `<link rel="share-url">` 属性，旨在标准化网站公开其分享机制的方式。目前，每个社交媒体平台都使用不同的 URL 格式，并带有不同的参数（URL、文本、标题）来预填充分享意图，这导致了开发人员的不一致性和复杂性。

该提案利用了 `<link>` 标签中现有的 `rel` 属性。网站将在其 HTML 头部包含 `<link rel="share-url" href="...">`，从而提供特定于其平台的 URL 模板。该模板将使用诸如 `{url}` 和 `{text}` 之类的占位符，这些占位符将被替换为要分享的内容。

本文展示了 Facebook、LinkedIn、Lemmy、BlueSky 和 Mastodon 等各种平台的示例，演示了如何为不同的输入要求实现 `share-url`。虽然对于接受 URL 和标题的平台来说很简单，但本文承认了 Mastodon 和 BlueSky 等平台面临的挑战，这些平台主要依赖于基于文本的分享。针对这些平台的解决方案涉及将文本和 URL 都插入到文本字段中。

作者强调，形式化该提案涉及创建规范并倡导社交网络的采用。文章最后呼吁反馈，询问读者是否认为 `<link rel="share-url">` 是一个好主意，他们会提出什么修改意见，以及他们是否会将其用作分享者或分享目的地。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 2 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 3 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 4 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 5 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 6 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 7 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 8 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 9 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 10 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 11 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 12 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 13 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 14 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 15 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 16 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 17 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 18 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 19 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 20 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 21 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 22 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 23 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 24 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 25 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 26 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 27 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 28 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 29 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 30 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 31 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 32 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 33 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 34 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 35 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 36 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 37 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 38 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 39 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 40 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 41 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 42 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 43 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 44 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 45 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 46 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 47 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 48 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 49 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 50 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 51 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 52 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 53 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 54 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 55 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 56 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 57 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 58 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 59 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 60 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 61 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 62 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 63 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 64 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 65 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 66 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 67 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 68 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 69 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 70 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 71 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 72 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 73 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 74 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 75 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 76 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 77 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 78 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 79 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 80 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 81 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 82 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 83 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 84 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 85 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 86 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 87 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 88 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 89 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 90 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 91 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 92 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 93 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 94 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 95 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 96 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 97 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 98 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 99 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 100 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 101 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 102 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 103 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 104 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 105 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 106 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 107 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 108 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 109 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 110 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 111 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 112 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 113 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 114 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 115 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 116 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 117 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 118 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 119 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 120 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 121 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 122 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 123 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 124 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 125 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 126 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 127 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 128 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 129 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 130 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 131 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 132 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 133 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 134 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 135 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 136 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 137 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 138 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 139 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 140 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 141 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 142 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 143 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 144 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 145 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 146 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 147 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 148 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 149 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 150 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 151 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 152 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 153 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 154 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 155 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 156 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
