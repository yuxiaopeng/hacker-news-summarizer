# Hacker News 热门文章摘要 (2025-08-22)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Show HN: Clyp – Linux 剪贴板管理器

**原文标题**: Show HN: Clyp – Clipboard Manager for Linux

**原文链接**: [https://github.com/murat-cileli/clyp](https://github.com/murat-cileli/clyp)

Clyp：一款使用 Go 和 GTK4 构建的现代 Linux 开源剪贴板管理器。它提供简洁、以键盘为中心的界面，用于浏览、搜索、复制和删除剪贴板历史记录。Clyp 支持文本和图像内容（最多 3 张图像），使用针对性能优化的 SQLite 后端（已测试超过 10,000 条记录），并在 Wayland 和 X11 上原生工作。

该应用程序自动监控剪贴板，使用户可以通过可搜索的界面轻松访问过去的条目。主要功能包括自动剪贴板监控、浏览历史记录、搜索、快速复制和删除项目。

Clyp 将其数据（包括时间戳和内容类型）存储在位于 `~/.local/share/bio.murat.clyp/clyp.db` 的 SQLite3 数据库中。它遵循 XDG Base Directory 规范。

目前可以通过 Ubuntu 和 Arch Linux 包安装，或者从最新版本下载二进制文件。Flatpak 支持正在开发中。

该项目被组织成用于应用程序逻辑、剪贴板监控、数据库操作、UI 资源和元数据的组件。未来的待办事项包括导入/导出功能和数据库加密。

---

## 12. 万物皆相关 (2014–23)

**原文标题**: Everything is correlated (2014–23)

**原文链接**: [https://gwern.net/everything](https://gwern.net/everything)

一切皆相关(2014–23)

本文《一切皆相关(2014–23)》探讨了一种普遍的观察：在现实世界的数据集中，几乎所有变量都表现出非零相关性，即使是看似独立的变量也是如此。这种被称为“粗略因素”或“万物皆有关联”的现象，对统计理论，特别是零假设显著性检验，具有重大影响。作者认为，由于零相关的零假设几乎总是错误的，因此只要有足够的数据，它必然会被拒绝，从而使显著性检验在很大程度上毫无意义。

此外，本文认为定向假设并没有带来多大改善，因为参数的真实值不太可能正好为零，这导致仅凭运气就能做出正确预测的可能性很高。广泛的相互关联也使模型解释复杂化，并威胁到朴素的统计模型。

作者认为，这些相关性源于复杂的因果网络、潜在变量以及诸如遗传相关性之类的现象，这些现象将所有测量到的特征联系起来。尽管这种现象很普遍，但“押注稀疏性”原则表明，一些关键变量（例如，智商、唤醒程度）可能充当这些网络中的中心枢纽。

本文强调了不相关变量的潜在无意义性，表明它们可能指示数据损坏、系统性偏差或数据生成过程中的问题。作者编撰了一份按时间顺序排列的讨论过这一概念的学者名单，强调这并非一个新颖的想法，而是各个领域中反复出现的主题。

---

## 13. 用手机控制购物车轮子 (2021)

**原文标题**: Control shopping cart wheels with your phone (2021)

**原文链接**: [https://www.begaydocrime.com/](https://www.begaydocrime.com/)

本文介绍了一种黑客技术，允许用户使用手机控制某些购物车的车轮。这些购物车使用的是Gatekeeper Systems车轮，通常根据地下电线或管理遥控器发出的7.8 kHz信号进行锁定和解锁。

文章解释说，这个7.8 kHz的频率落在可听范围内，允许手机扬声器模仿该信号。通过手机扬声器播放专门制作的音频文件，并将其靠近车轮，用户可以利用扬声器发出的寄生电磁场来“传输”信号，从而有效地锁定或解锁车轮。

作者提供了几个音频文件供下载，对应于“锁定”、“解锁”和“布防”等操作，以及“购买检查”选项。他们还链接到他们在DEFCON 29上关于该主题的原始演讲，并鼓励用户在Twitter上查看他们。该页面还包含一个耳机警告，因为存在高频音频损伤的风险。本质上，这种黑客技术利用手机的扬声器来模拟授权的遥控信号，从而未经授权地控制购物车车轮。

---

## 14. 雷鸟专业版 2025年8月更新

**原文标题**: Thunderbird Pro August 2025 Update

**原文链接**: [https://blog.thunderbird.net/2025/08/tbpro-august-2025-update/](https://blog.thunderbird.net/2025/08/tbpro-august-2025-update/)

Thunderbird Pro 2025年8月更新： 此更新详细介绍了Thunderbird可选的、基于订阅服务的进展，这些服务旨在增强现有的Thunderbird体验。这些服务均为开源，并设计为与Thunderbird应用程序无缝集成，包括：

*   **Thundermail：** 一种支持IMAP、SMTP和JMAP的电子邮件托管服务，允许用户携带自己的域名，或使用@thundermail.com或@tb.pro地址。服务器最初将位于德国。
*   **Thunderbird Appointment：** 一种集成到撰写窗口中的日程安排工具，方便插入日程安排链接。它将支持各种会议类型，并提供自托管选项。未来的开发目标是实现群组日程安排功能。
*   **Thunderbird Send：** 一种端到端加密的文件共享工具，提供500 GB的存储空间，没有文件大小限制。它利用分块上传和加密技术来实现可靠性和数据保护，并作为系统附加组件交付，以便更快地更新。

所有Thunderbird Pro工具均为开源且可自托管。

未来的考虑事项包括基于Markdown的笔记功能。之前宣布的AI驱动服务Assist仍在研发阶段。

正在开发公共路线图，以提高透明度并鼓励桌面、移动和Pro服务之间的社区协作。

核心Thunderbird桌面和移动应用程序将保持免费并接受捐赠。Thunderbird Pro是一个可选套件，收费可确保使用这些服务的用户支付存储和带宽成本。用户可以在thundermail.com上注册以获得Thunderbird Pro的测试版访问权限。

---

## 15. Waymo获准在纽约市开始测试自动驾驶车辆的首张许可

**原文标题**: Waymo granted first permit to begin testing autonomous vehicles in New York City

**原文链接**: [https://www.cnbc.com/2025/08/22/waymo-permit-new-york-city-nyc-rides.html](https://www.cnbc.com/2025/08/22/waymo-permit-new-york-city-nyc-rides.html)

Waymo获准在纽约市测试自动驾驶汽车

---

## 16. VHS-C：懒惰想法走向完美的意外之喜 [视频]

**原文标题**: VHS-C: When a lazy idea stumbles towards perfection [video]

**原文链接**: [https://www.youtube.com/watch?v=HFYWHeBhYbM](https://www.youtube.com/watch?v=HFYWHeBhYbM)

VHS-C：当一个懒惰的想法跌跌撞撞地走向完美。

这似乎是一个名为“VHS-C：当一个懒惰的想法跌跌撞撞地走向完美”的YouTube视频。所列内容只是标准的YouTube页脚，包括指向各种资源的链接，如联系信息、创作者支持、广告、开发者工具、服务条款、隐私政策和安全信息。它还提到了YouTube的运营实践、测试新功能，并包括与Google LLC和NFL Sunday Ticket相关的版权信息。

由于无法获得实际视频内容，并且所提供的信息纯粹是管理性质的，因此不可能对文章本身进行总结。提供的文本没有提供任何关于视频讨论VHS-C、其设计、其被认为的“懒惰”或其所谓的最终“完美”的见解。我们只知道视频的标题和样板化的YouTube信息。

---

## 17. uv 实验性地支持代码格式化

**原文标题**: Code formatting comes to uv experimentally

**原文链接**: [https://pydevtools.com/blog/uv-format-code-formatting-comes-to-uv-experimentally/](https://pydevtools.com/blog/uv-format-code-formatting-comes-to-uv-experimentally/)

`uv` 包管理器 0.8.13 版本实验性引入代码格式化功能，Python 开发者翘首以盼。 新的 `uv format` 命令将代码格式化直接集成到 `uv` 中，简化了 Python 开发，无需单独的格式化工具。

`uv format` 在底层使用 Ruff 的格式化器，自动且一致地进行代码风格化。这类似于 Rust 中 `cargo fmt` 使用 `rustfmt`。 虽然 `ruff` 和 `uv` 仍然是独立的工具，但这种集成提供了简化的用户体验。

本文提供了入门指南，包括升级到 `uv 0.8.13` 或更高版本，以及使用该命令来格式化代码、检查格式或查看差异。 它还演示了如何将其他参数直接传递给 Ruff 进行自定义，例如设置行长度或指定文件。

作者指出该功能是实验性的，可能会发生变化。潜在的改进领域包括与 uv 项目模型的集成以及错误处理。 鼓励读者尝试该功能并提供反馈以影响其开发。文章最后提到了 Google 停止维护 Pytype。

---

## 18. 所有管理者都会犯错；优秀的管理者会承认并改正。

**原文标题**: All managers make mistakes; good managers acknowledge and repair

**原文链接**: [https://terriblesoftware.org/2025/08/22/the-management-skill-nobody-talks-about/](https://terriblesoftware.org/2025/08/22/the-management-skill-nobody-talks-about/)

本文认为，最关键的管理技能并非完美，而是承认和弥补错误的能力。所有管理者都不可避免地会犯错，从给出错误的反馈到过度承诺团队。优秀和糟糕的管理者之间的关键区别在于他们如何应对这些错误。

作者将此比作育儿，强调“弥补”的重要性——承认错误、承担责任并重新建立联系。即使在犯错的情况下，承认错误也能建立信任。未能承认错误、加倍辩解或将自我凌驾于问责之上会削弱信任，并导致宝贵团队成员的流失。

本文概述了有效弥补的实用步骤：具体说明错误，关注对他人的影响（而非个人辩解），切实改变行为以避免重蹈覆辙，并理解弥补需要时间和持续的努力。

作者认为，拥抱弥补可以营造更健康的环境，使管理者能够承担经过计算的风险，并进行艰难的对话，而无需担心失败。这并非是成为糟糕管理者的借口，而是承认复杂角色中人类的易错性。最终目标是创建一个支持性的环境，让团队能够蓬勃发展，而弥补是实现这一目标的重要工具。

---

## 19. 围棋还是不行。

**原文标题**: Go is still not good

**原文链接**: [https://blog.habets.se/2025/07/Go-is-still-not-good.html](https://blog.habets.se/2025/07/Go-is-still-not-good.html)

对Go语言长达十年的批判：设计缺陷导致问题。

---

## 20. 构建日志：Macintosh Classic

**原文标题**: Build Log: Macintosh Classic

**原文链接**: [https://www.jeffgeerling.com/blog/2025/build-log-macintosh-classic](https://www.jeffgeerling.com/blog/2025/build-log-macintosh-classic)

本文详细介绍了作者修复其姑妈的Macintosh Classic（一款1990年发布的经济型Mac）的过程。初始状态评估强调了由于老化的电池和电容器可能造成的潜在损坏，不要立即启动老式电脑的重要性。

修复过程包括彻底检查，移除原装Sonnenschein电池（幸运的是，电池没有泄漏），以及从Console5.com订购套件后更换模拟板和主板上的电容器。作者警告了CRT上的阳极帽，以及由于潜在的有害电压而采取安全预防措施的重要性，并强调了安全放电CRT的重要性。

升级包括安装4MB RAM升级套件，以及使用MacBatt适配器将旧电池更换为现代纽扣电池。作者成功地重新组装了机器，并且可以工作了！一个有趣的发现是一个名为The Grouch的老程序。

硬盘驱动器最初可以运行，但在几次启动循环后出现故障。作者目前正在对SCSI驱动器进行故障排除，使用外部BlueSCSI v2进行启动。最后，作者计划对机箱进行复古增亮处理，并计划修复另一位姑妈的Mac Plus。本文还提供了相关构建日志和文件传输指南的链接。

---

## 21. 4chan拒绝支付每日在线安全罚款，律师告知BBC

**原文标题**: 4chan will refuse to pay daily online safety fines, lawyer tells BBC

**原文链接**: [https://www.bbc.co.uk/news/articles/cq68j5g2nr1o](https://www.bbc.co.uk/news/articles/cq68j5g2nr1o)

2025年未来新闻报道：在线论坛4chan拒绝支付英国通信管理局Ofcom根据《在线安全法案》征收的罚款。Ofcom希望对4chan处以最初2万英镑的罚款，此后每天加罚，原因是其未遵守与用户安全和非法内容相关的信息请求。

4chan的律师普雷斯顿·拜恩辩称，Ofcom的要求在美国（4chan注册地）没有法律效力，并称这项调查是“非法的骚扰活动”。4chan声称其拥有美国宪法第一修正案赋予的权利，并表示美国法院不会强制执行外国的处罚或审查。他们已向美国当局通报情况，并敦促特朗普政府干预他们眼中的“域外审查授权”。

这篇文章突显了英国和美国之间在监管科技公司方面日益紧张的关系。一些美国政客，尤其是在特朗普政府内部，担心《在线安全法案》等法律可能对言论自由和数据隐私产生影响。

虽然Ofcom不能直接对外国实体强制执行罚款，但它有权要求英国法院干扰4chan在英国的业务，包括从搜索结果中删除、阻止付款，甚至完全屏蔽ISP。文章还指出，最近美国的施压导致英国放弃了对苹果数据保护系统“后门”的要求。

---

## 22. 如何避免买错固态硬盘

**原文标题**: How Not to Buy a SSD

**原文链接**: [https://andrei.xyz/post/how-not-to-buy-a-ssd/](https://andrei.xyz/post/how-not-to-buy-a-ssd/)

作者从eMag（罗马尼亚最大的在线零售商）购买了一块金士顿SSD，但它是通过eMag的 marketplace 由第三方卖家出售的。在使用过程中发现传输速度极慢后，作者怀疑这块SSD是假货。使用磁盘工具进行的初步测试略微提高了速度，但仍远低于预期水平。

之后，作者使用F3（Fight Flash Fraud）测试了该硬盘的容量，但SSD变得无法使用，并在格式化过程中出现错误。作者认为这块硬盘是一个正品但已损坏/需要RMA的128GB金士顿SSD，其固件被修改为显示更大的容量。虽然包装看起来很逼真，但作者注意到背面的标签质量很差，这应该是一个警告信号。

这篇文章强调了即使在信誉良好的在线市场上从第三方卖家购买产品的风险（陷入 "由亚马逊配送 "的骗局）。作者在发起退货时遇到了困难，因为产品清单在购买后被更改了。

使用F3进行的进一步测试显示，写入速度在超过128GB标记后急剧下降，证实了这是一个容量较小的伪装硬盘的怀疑。幸运的是，作者联系了eMag的客户支持并成功获得了全额退款。

---

## 23. SVG路径交互式指南

**原文标题**: An interactive guide to SVG paths

**原文链接**: [https://www.joshwcomeau.com/svg/interactive-guide-to-paths/](https://www.joshwcomeau.com/svg/interactive-guide-to-paths/)

本文是一篇互动指南，旨在帮助读者理解和使用 SVG `<path>` 元素。它通过解释构成 SVG 路径的基本概念和命令，揭开了其常常令人困惑的语法的神秘面纱。

作者首先将 `<path>` 元素介绍为一种“笔”工具，允许用户串联绘图指令。并解释了包含路径数据的 `d` 属性。

然后，文章深入探讨了具体的路径命令：

*   **M (Move):** 将笔移动到新位置而不绘制。
*   **L (Line):** 从当前位置到指定点绘制一条直线。
*   **Q (Quadratic Bézier curve):** 创建由起点、控制点和终点定义的曲线。
*   **C (Cubic Bézier curve):** 与二次贝塞尔曲线类似，但有两个控制点，可用于创建更复杂的曲线。
*   **A (Elliptical Arc):** 最复杂的命令，在两点之间绘制椭圆弧。它需要 rx、ry（半径）、旋转、大弧标志（选择较长或较短的弧）和扫描标志（选择顺时针或逆时针方向）等参数。文章通过互动示例详细解释了每个参数。

作者利用视觉辅助工具分解了弧线的复杂性，说明了半径、标志和旋转参数如何影响弧线的形状和方向。

文章还提到了用 `Z` 命令关闭路径。最后，文章推广了一门涵盖这些 SVG 路径基础知识的动画课程。

---

## 24. 利用图像缩放攻击生产环境中的人工智能系统

**原文标题**: Weaponizing image scaling against production AI systems

**原文链接**: [https://blog.trailofbits.com/2025/08/21/weaponizing-image-scaling-against-production-ai-systems/](https://blog.trailofbits.com/2025/08/21/weaponizing-image-scaling-against-production-ai-systems/)

本文详细介绍了一种针对人工智能系统的新型攻击向量：**利用图像缩放进行多模态提示注入**。 核心概念是人工智能系统通常会在处理大型图像之前对其进行缩小，攻击者可以制作全分辨率下看起来无害的图像，但在缩小时会显示隐藏的提示注入。 这使得攻击者能够在用户不知情的情况下操纵人工智能的行为。

作者演示了在各种平台上的数据泄露，例如 **Google Gemini CLI、Vertex AI Studio、Gemini 的 Web 和 API 接口、Google Assistant 和 Genspark**。 他们利用 Gemini CLI 的默认设置自动批准工具调用，从而将数据泄露到攻击者的电子邮件中。

该攻击的工作原理是利用降尺度算法（最近邻、双线性、双三次）执行的插值。 可以使用特定的测试图像对这些算法进行指纹识别，从而使攻击者能够制作基于目标算法行为显示特定有效负载的图像。 本文解释了他们的开源工具 Anamorpher 如何通过操纵高重要性像素来促进创建这些精心制作的图像，特别是对于双三次插值。

作者建议**完全避免图像降尺度，方法是限制上传尺寸**。 如果必须进行降尺度，则应向用户显示模型处理后的降尺度图像的预览。 **最有效的防御措施是安全设计模式，通过要求用户明确确认敏感工具调用来缓解有影响的提示注入。** 文章最后建议未来研究移动/边缘设备，并探索更复杂的攻击技术。

---

## 25. 使用Python模式匹配的犯罪行为 (2022)

**原文标题**: Crimes with Python's Pattern Matching (2022)

**原文链接**: [https://www.hillelwayne.com/post/python-abc/](https://www.hillelwayne.com/post/python-abc/)

本文探讨了Python的模式匹配（3.10引入）和抽象基类(ABCs)之间令人惊讶且可能存在危险的交互，尤其是在使用`__subclasshook__`方法时。作者展示了`__subclasshook__`如何允许ABC基于任意条件定义其子类，即使“子类”并未意识到ABC的存在。

核心问题是模式匹配使用`isinstance`，而它会尊重`__subclasshook__`。这使得ABC能够“劫持”模式匹配，根据对象的运行时属性（而不仅仅是其固有类型）来控制触发哪个case。

作者通过创建`NotIterable`（如果对象缺少`__iter__`则匹配）和`DistanceMetric`（匹配任何具有`distance`属性的对象）来展示这一点。作者甚至展示了模式匹配如何解构在`__subclasshook__`中定义的属性，例如检查“DistanceMetric”对象上的`z`坐标。

此外，作者还创建了组合器函数`Not`和`And`，以动态生成ABC，从而实现更复杂的匹配条件。他们探索了在`__subclasshook__`中引入副作用以获得更不可预测行为的可能性，尽管Python的缓存机制对此有所限制。

文章最后强烈警告不要在生产代码中使用这些技术，因为它们违反了对模式匹配行为方式的预期，并可能导致代码难以维护。作者强调，虽然这些技术很有趣并揭示了模式匹配的潜在误用，但最好不要在实际应用中进行探索。

---

## 26. 从GPT-4到GPT-5：通过MedHELM衡量进展 [pdf]

**原文标题**: From GPT-4 to GPT-5: Measuring progress through MedHELM [pdf]

**原文链接**: [https://www.fertrevino.com/docs/gpt5_medhelm.pdf](https://www.fertrevino.com/docs/gpt5_medhelm.pdf)

从GPT-4到GPT-5：通过MedHELM衡量进展

这份题为“从GPT-4到GPT-5：通过MedHELM衡量进展”的文档是一个PDF文件，其中包含的似乎是与评估语言模型（可能是GPT-4和一个假设的GPT-5）相关的技术数据或输出。其中还提到了MedHELM这个名称。该文档似乎侧重于评估模型之间的改进和差异。

鉴于PDF格式和编码内容，这很可能是一份详细说明性能指标的技术报告，可能涉及医疗或健康保健相关的数据集（由“MedHELM”暗示）。内容似乎是机器生成的，包含来自PDF文档的编码二进制数据。

在不解码和分析嵌入数据的情况下，无法进行详细总结。但是，根据标题，这篇文章可能：

*   **比较 GPT-4 和 GPT-5：** 评估两种模型的能力。
*   **使用 MedHELM：** 采用名为 MedHELM 的特定基准或数据集进行评估。
*   **衡量进展：** 量化从 GPT-4 到 GPT-5 取得的进步，可能侧重于医疗或健康保健相关任务。

总而言之，该文档是一份技术报告，概述了使用名为 MedHELM 的医疗基准评估从 GPT-4 到假设的 GPT-5 的进展的方法和结果。

---

## 27. 美国如何用水？

**原文标题**: How does the US use water?

**原文链接**: [https://www.construction-physics.com/p/how-does-the-us-use-water](https://www.construction-physics.com/p/how-does-the-us-use-water)

本文探讨了美国如何利用水资源，突出了水基础设施相对于其他行业而言常常被忽视的重要性。尽管美国每天降水约 5 万亿加仑，但每天的用水量为 3220 亿加仑。

最大的用水户是火力发电厂（占总用水量的 41%），主要用于冷却，尽管由于循环系统取代了旧的“一次通过”方法，大部分用水是非消耗性的。灌溉是第二大用水户（占 37%），大部分水用于苜蓿、果园、玉米、大豆和水稻等作物。很大一部分灌溉用水是消耗性的。

公共用水占总用水量的 12%，其中家庭用水占多数。与德国、英国和法国等国家相比，美国人均家庭用水量很高。工业用水占总用水量的 4.5%，包括林产品、钢铁制造和半导体制造等行业。数据中心正受到越来越多的审查，它们直接和间接地消耗了可观的水量，但少于高尔夫球场或棉花等某些作物。

用水量因地域而异，加利福尼亚州、德克萨斯州和爱达荷州是最大的用水户，原因是灌溉和发电厂冷却。由于降水量较低，美国西部严重依赖灌溉，经常从地下含水层取水，导致某些地区枯竭。发电厂冷却集中在美国东部和德克萨斯州。公共用水量与人口相关。

---

## 28. 在概率时代构建人工智能产品

**原文标题**: Building AI products in the probabilistic era

**原文链接**: [https://giansegato.com/essays/probabilistic-era](https://giansegato.com/essays/probabilistic-era)

人工智能的兴起，尤其是像ChatGPT这样的通用人工智能，正在根本性地改变我们构建和发展软件产品的方式，将我们从一个“经典”的确定性世界带入一个“量子”概率性世界。

在经典世界中，软件将特定输入映射到预期输出（F: X → Y），从而实现精确控制和可预测的结果。这塑造了工程、产品管理和增长策略，使其围绕优化预定义的渠道和最大化转化率。然而，人工智能引入了不确定性因素，因为模型现在可以接受开放式输入，并产生潜在输出的统计分布（F'(?)），而不是保证“正确”的答案。

这种转变使许多既定的策略失效。与传统软件具有接近于零的边际成本和确定性输出不同，人工智能产品具有确定性成本，但输出是随机的，从而产生紧张和用户挫败感。用户期望可预测的结果，但遇到人工智能固有的不确定性，从而导致不满。

作者强调，人工智能模型是“发现”的，而不是“工程”出来的，这导致对其能力的深度未知。这需要一种新的产品开发方法，从预定义的渠道转向驾驭“无限领域”的可能性。重点不应是保证100%的准确性，而应是理解和利用人工智能的概率性质，在模糊和不确定的情况下交付价值。作者强调了注入随机性（在推理时采样）的重要性，以使用户能够根据自己的判断来驾驭概率分布。

---

## 29. 亚马逊云科技CEO称用人工智能取代初级员工是“我听过的最愚蠢的事情”

**原文标题**: AWS CEO says using AI to replace junior staff is 'Dumbest thing I've ever heard'

**原文链接**: [https://www.theregister.com/2025/08/21/aws_ceo_entry_level_jobs_opinion/](https://www.theregister.com/2025/08/21/aws_ceo_entry_level_jobs_opinion/)

亚马逊云服务CEO Matt Garman 批评了用人工智能取代初级员工的想法，称其为“我听过的最愚蠢的事情”。他认为，初级员工成本低廉，对人工智能参与度高，并且对于培养未来人才至关重要。Garman 强调了培养他们在软件开发、问题解决和批判性思维方面技能的重要性。他认为，公司应该继续招聘大学毕业生，并以正确的方式培训他们构建软件和应对挑战。

Garman 还驳斥了仅以人工智能生成代码的百分比来衡量其价值的观点，他表示，少量且编写良好的代码通常比更多且可能很糟糕的代码更好。他指出，超过 80% 的 AWS 开发者以各种方式使用人工智能，从编写单元测试和文档到实际编码以及与人工智能代理协作，并且这种使用正在增长。

他建议年轻人专注于学习如何学习、培养批判性推理能力和培养创造力，而不是专注于由于技术快速进步而可能很快过时的特定技能。Garman 认为，培养这些基本技能对于在快速发展的环境中蓬勃发展至关重要。

---

## 30. 显示 HN：OS X Mavericks 永存

**原文标题**: Show HN: OS X Mavericks Forever

**原文链接**: [https://mavericksforever.com/](https://mavericksforever.com/)

在现代（截至2025年）继续使用OS X Mavericks的指南。

---

## 31. 1981年索尼特丽珑KV-3000R：最豪华的特丽珑 [视频]

**原文标题**: 1981 Sony Trinitron KV-3000R: The Most Luxurious Trinitron [video]

**原文链接**: [https://www.youtube.com/watch?v=jHG_I-9a7FY](https://www.youtube.com/watch?v=jHG_I-9a7FY)

这似乎是YouTube视频页面描述。标题暗示视频展示了1981年的索尼特丽珑KV-3000R，并将其定位为一款豪华电视型号。然而，提供的内容是通用的YouTube样板文本，包括指向条款、隐私、广告和谷歌所有权的链接。

因此，我们可以推断出以下几点：

*   **该视频很可能专注于1981年的索尼特丽珑KV-3000R电视。** 可能是对这款特定型号的评测、演示或怀旧回顾。
*   **该视频的角度强调了KV-3000R的豪华或高端特性。** 标题表明它在当时被认为是高端电视。
*   **提供的内容仅仅是标准的YouTube页面页脚信息，除了标题的暗示之外，没有提供关于实际视频内容的任何细节。**

---

## 32. 反洗钱控制系统运作如何？

**原文标题**: How well does the money laundering control system work?

**原文链接**: [https://www.journals.uchicago.edu/doi/10.1086/735665](https://www.journals.uchicago.edu/doi/10.1086/735665)

无法访问文章链接。

---

## 33. Text.ai (YC X25) 招聘创始全栈工程师

**原文标题**: Text.ai (YC X25) Is Hiring Founding Full-Stack Engineer

**原文链接**: [https://www.ycombinator.com/companies/text-ai/jobs/OJBr0v2-founding-full-stack-engineer](https://www.ycombinator.com/companies/text-ai/jobs/OJBr0v2-founding-full-stack-engineer)

Text.ai 是一家 Y Combinator (X25) 支持的初创公司，现寻求一位创始全栈工程师来领导其 AI 原生通信平台的开发。此职位包括从头开始构建一个 React Native 移动应用程序（iOS 和 Android），并承担一些后端（Python）集成职责。公司旨在通过使用 AI 创建智能协作体验，从而彻底改变群聊通信。

理想的候选人拥有 4 年以上 React Native 经验、全栈能力、对消费产品的热情以及创业导向的思维。他们应该能够适应不确定性，优先考虑快速迭代，并专注于产品质量。拥有 GenAI/LLM 集成、社交平台、移动性能优化和病毒式增长经验者优先。

这是一个高影响力的机会，可以定义 AI 驱动通信领域的新产品类别，扩大具有现有产品市场契合度信号的产品，并致力于解决与群体 AI 协调和多参与者优化相关的技术难题。

Text.ai 获得了 Y Combinator、SV Angel 以及来自 Shopify 和腾讯的天使投资支持，创始团队来自特斯拉、Eventbrite、亚马逊和麦肯锡。该职位提供具有竞争力的薪酬、有意义的股权、401k 计划和健身报销。鼓励申请人提交简历，说明对 Text.ai 感兴趣的原因，提供相关作品链接，以及对构建协作式 AI 体验的想法。

---

## 34. 我的另一个邮件客户端是守护进程。

**原文标题**: My other email client is a daemon

**原文链接**: [https://feyor.sh/blog/my-other-email-client-is-a-mail-daemon/](https://feyor.sh/blog/my-other-email-client-is-a-mail-daemon/)

作者详细介绍了如何将他们的电子邮件客户端mu4e与游戏NetHack集成，以便在游戏中接收电子邮件通知，同时不影响沉浸感。问题在于NetHack使用mbox文件，而mu4e使用maildir。

解决方案包括一个作为cron作业运行的Python脚本，该脚本检查maildir中最近5分钟内收到的新邮件。如果存在新邮件，脚本会touch mbox文件。NetHack只检查mbox文件的mtime，因此简单地touch该文件即可触发游戏内的邮件通知。

第二部分涉及一个Bash脚本，用于打开mu4e并专门搜索个人INBOX文件夹中的未读邮件。此脚本使用`emacsclient`来避免创建多个Emacs进程，并处理mu数据库的锁定问题。他们还包装了`emacsclient`，以智能地重用现有的Emacs框架，无论脚本是从Emacs内部还是外部调用。作者提供了包装器的代码以方便理解。

本质上，本文提供了一个实用示例，说明如何使用简单的脚本来弥合老式游戏的通知系统（NetHack的mbox邮件检查）和现代电子邮件客户端（mu4e）之间的差距。

---

## 35. 超越传感器数据：可穿戴设备行为数据的基础模型

**原文标题**: Beyond sensor data: Foundation models of behavioral data from wearables

**原文链接**: [https://arxiv.org/abs/2507.00191](https://arxiv.org/abs/2507.00191)

超越传感器数据：可穿戴设备行为数据基础模型提升健康预测

---

## 36. 使用 Podman、Compose 和 BuildKit

**原文标题**: Using Podman, Compose and BuildKit

**原文链接**: [https://emersion.fr/blog/2025/using-podman-compose-and-buildkit/](https://emersion.fr/blog/2025/using-podman-compose-and-buildkit/)

本文详细介绍了如何结合使用Podman、Docker Compose和BuildKit，解决了在Podman的无根和无守护进程方式下使用Docker Compose的挑战。作者探讨了`podman-compose`（缺少功能）和标准Docker Compose CLI（缺乏BuildKit支持）的局限性。

作者概述了一种将官方Docker Compose CLI与Podman和BuildKit结合使用的解决方案：启用Podman socket，创建一个指向它的Docker context，并安装Docker Buildx。这使得Docker Compose能够利用BuildKit，但会引入一个可能不需要的BuildKit守护进程。

为了避免BuildKit守护进程，作者引入了`Bakah`，一个自定义工具，可以将Docker Compose项目转换为JSON Bake文件，然后使用Buildah（Podman的底层库）直接构建镜像，从而绕过了运行时对BuildKit的需求。这在Podman生态系统中提供了一个真正的无守护进程构建过程。作者承认`Bakah`对高级Bake功能的支持存在局限性，但它足以满足复杂的Compose项目，并计划在未来的项目中使用。

---

## 37. “自信地犯错”正在阻碍人工智能发展

**原文标题**: Being “Confidently Wrong” is holding AI back

**原文链接**: [https://promptql.io/blog/being-confidently-wrong-is-holding-ai-back](https://promptql.io/blog/being-confidently-wrong-is-holding-ai-back)

Tanmai Gopal的文章《“自信地犯错”正在阻碍人工智能发展》认为，人工智能应用停滞不前的核心原因并非集成、数据准备或组织准备，而是人工智能“自信地犯错”的倾向。他指出，即使在看似很高的准确率（例如90%）下，人工智能的不准确性也会导致“验证税”，因为用户必须仔细检查每一个回应，从而削弱信任并阻碍投资回报率。隐藏的失败模式也扼杀了改进人工智能的动力，因为用户无法查明错误的原因。

Gopal提出了一种以人工智能系统发出不确定性信号为中心的解决方案。一个只有50%准确率但能够可靠地传达不确定性的系统，比一个自信但不准确的90%准确率系统更有价值。这允许一个反馈循环，用户可以提供输入，人工智能可以从修正中学习，并且准确率会随着时间的推移而提高。这种“准确性飞轮”需要原生的不确定性信号、人工提示来填补规划空白以及通过更新领域知识来改进模型。

他提倡使用带有验证和策略检查的领域特定语言 (DSL) 来生成计划，而不是简单地生成答案。持续地将人工智能专门化于特定领域、将其绑定到本体以及理解边缘情况，将校准对生成计划的信心。Gopal最后敦促那些资助人工智能项目的人优先考虑能够发出不确定性信号并从修正中学习的系统，从而为可用的企业人工智能开辟道路。

---

## 38. 贡献必须披露人工智能工具的使用情况

**原文标题**: AI tooling must be disclosed for contributions

**原文链接**: [https://github.com/ghostty-org/ghostty/pull/8289](https://github.com/ghostty-org/ghostty/pull/8289)

`ghostty-org/ghostty`仓库的此GitHub议题提出并实施了一项政策，要求贡献者在他们的拉取请求（PR）中披露人工智能工具的使用情况。理由是虽然人工智能可能有所帮助，但其目前的输出并不总是高质量，需要仔细审查。披露人工智能的使用情况可以让维护者评估PR所需的审查程度，特别是对于可能没有充分审查人工智能生成的代码的经验不足的贡献者而言。

主要内容包括：

*   **披露

---

## 39. 私有铁路车厢

**原文标题**: Privately-Owned Rail Cars

**原文链接**: [https://www.amtrak.com/privately-owned-rail-cars](https://www.amtrak.com/privately-owned-rail-cars)

我能访问互联网。以下是Amtrak网站上关于私人铁路客车的摘要：

Amtrak网站关于私人铁路客车的页面为有兴趣在其网络上运营私人铁路客车的个人和组织提供信息。它概述了相关的要求、程序和注意事项。

该页面解释说，私人铁路客车车主可以安排将其客车挂在Amtrak列车上，但须经Amtrak批准并符合运营条件。这使得车主可以使用自己的私人住宿设施旅行，并享受独特的铁路旅行体验。

涵盖的关键方面包括：

*   **资格：** 铁路客车必须符合Amtrak的安全标准、机械要求和兼容性标准。需要进行检查。
*   **安排：** 车主必须与Amtrak的私人客车办公室协调，请求将客车安排在特定列车上，同时考虑到时间表、路线和可用性。
*   **费用：** 车主负责各种费用，包括里程费、调车费、检查费以及Amtrak人员的任何相关费用。
*   **乘客限制：** 对Amtrak线上牵引的私人客车有乘客人数限制。
*   **乘务员

该页面还强调了遵守Amtrak的政策和法规以确保安全高效运营的重要性。它鼓励有兴趣的各方联系私人客车办公室，以获取详细信息、申请程序和具体要求。该办公室的目的是协助安排、解答任何问题并促进流程。

---

## 40. 优雅数学，塑造设计未来

**原文标题**: Elegant mathematics bending the future of design

**原文链接**: [https://actu.epfl.ch/news/elegant-mathematics-bending-the-future-of-design/](https://actu.epfl.ch/news/elegant-mathematics-bending-the-future-of-design/)

EPFL研究人员开发了一种名为C-Tubes的新方法，利用纸张、铝或塑料等平面材料设计复杂的弯曲三维形状。 这种创新方法将创意设计与一种新的计算算法相结合，从而能够利用弯曲并连接成管状的扁平条带创建坚固、轻巧的结构。

C-Tubes方法利用“可展”曲面，这些曲面可以由平面片材创建，而不会产生折痕或变形。 算法确定如何切割、弯曲和连接平面零件以匹配设计师的目标，确保形状在现实世界中可构建。 这消除了制造的复杂性，让设计师专注于美学和功能。

C-Tubes具有多项优势，包括更可持续的生产和更少的浪费，由于其轻巧而坚硬的特性，减少了材料的使用，并且更容易采购、运输和回收平面材料。 应用领域包括家具、照明、建筑、船体和汽车设计。 虽然采用可能面临惯性，但C-Tubes有望通过提供材料性、设计和优雅数学的结合来减少设计时间并促进更可持续的产品。 研究人员正在寻找合作伙伴，以进一步探索该技术的潜力。

---

## 41. 远离海洋，布达佩斯街下潜水。

**原文标题**: Miles from the ocean, there's diving beneath the streets of Budapest

**原文链接**: [https://www.cnn.com/2025/08/18/travel/budapest-diving-molnar-janos-cave](https://www.cnn.com/2025/08/18/travel/budapest-diving-molnar-janos-cave)

在布达佩斯熙攘的街道下，卢卡奇温泉浴场附近，隐藏着莫尔纳·亚诺什洞穴，它是世界上最大的活跃地热水洞穴系统之一。这个隐秘的世界绵延超过3.6英里，深近300英尺，是为持有认证的洞穴潜水员开放的独特潜水目的地。洞穴由地热温泉供水，上层水温常年保持在舒适的27°C（80°F），这在洞穴潜水地点中实属罕见。

该洞穴系统经富含矿物质的地热水数千年雕琢而成，拥有宽敞的洞室和缓和的水流。潜水员可以探索超现实的景观，其中包括镶嵌着水晶的墙壁和古潘诺尼亚海的化石遗迹。能见度可能极佳，但很容易被淤泥破坏，因此潜水员需要遵守指导方针，以保护脆弱的环境。

虽然官方绘制的网络已经非常广泛，但该洞穴仍在积极生长并被探索。志愿者潜水员定期绘制新的通道，研究人员则监测水质。当地运营商MJ Cave提供导游潜水服务，为合格的潜水员提供装备租赁和简报，以体验这个非凡的水下世界。该洞穴为经验丰富的洞穴潜水员提供了科学研究价值和独特的探险机会。

---

## 42. AI职位名称解码环

**原文标题**: The AI Job Title Decoder Ring

**原文链接**: [https://www.dbreunig.com/2025/08/21/a-guide-to-ai-titles.html](https://www.dbreunig.com/2025/08/21/a-guide-to-ai-titles.html)

人工智能职位名称解码环

---

## 43. 技能问题——辩证行为疗法及其不满 (2024)

**原文标题**: Skill issues – Dialectical Behavior Therapy and its discontents (2024)

**原文链接**: [https://www.thedriftmag.com/skill-issues/](https://www.thedriftmag.com/skill-issues/)

莉莉·舍利斯的文章《技能问题——辩证行为疗法及其不满》探讨了辩证行为疗法（DBT）的兴起及其影响。文章首先讲述了DBT的创始人玛莎·莱恩汉及其自身与精神健康作斗争的经历，正是这些经历促使她开发了这种疗法。DBT现在被认为是治疗自杀倾向患者的“黄金标准”，它强调教授特定的情绪调节技能。

文章追溯了“技能”概念的演变，从其在管理理论中的起源到目前在流行文化中的盛行，DBT技能进入了学校、工作场所和自助媒体。作者批判了这样一个潜在的假设，即感觉良好主要在于掌握生活技能，并将其视为在面临重大挑战的世界中，对自主性的虚假承诺。

DBT的一个关键组成部分是接受和改变之间的辩证关系，鼓励患者在接受自己的同时努力改变自己的行为。治疗师必须在认可和“不敬”之间保持平衡。

文章最后指出，基于技能的思维方式虽然可能有所帮助，但也存在将系统性问题个体化的风险，并助长了一种对自身福祉负责的责任感，即使在面对更大的社会问题，如经济不稳定和气候危机时也是如此。

---

## 44. Golang SQLite 驱动基准测试

**原文标题**: Benchmarks for Golang SQLite Drivers

**原文链接**: [https://github.com/cvilsmeier/go-sqlite-bench](https://github.com/cvilsmeier/go-sqlite-bench)

本文对各种 Golang SQLite 驱动程序进行了基准测试，旨在评估它们在不同场景下的性能。作者测试了九个库：bvinc、craw、eaton、glebarez、mattn、modernc、ncruces、sqinn 和 zombie，每个库都具有不同的特性（基于 CGO 与纯 Go，database/sql 驱动程序与非驱动程序）。基准测试环境包括一个运行 Debian Linux 系统的 Intel i7 处理器、32GB 内存和 NVME SSD。

基准测试包括“简单”（插入和查询用户）、“真实”（模拟具有多个表和事务的真实世界使用）、“复杂”（大型插入和一个复杂的 JOIN 查询）、“大量”（具有重复查询的读取密集型场景）、“大型”（处理大型行内容）和“并发”（模拟并发读取）。

结果以毫秒为单位测量，驱动程序和基准测试类型之间差异显着。没有哪个驱动程序始终优于其他驱动程序。sqinn 和 zombie 通常在某些类别中表现出强大的性能，而事实上的标准 mattn 通常在并发场景中落后。像 modernc 和 glebarez 这样的纯 Go 解决方案有时具有更高的插入成本，但具有可观的查询性能。作者强调，基准测试是根据其特定的数据库使用场景量身定制的，并鼓励读者为自己的独特需求创建自己的基准测试。文章总结说，在现代 Golang 开发中，没有 CGO 的 SQLite 是一个可行的选择。

---

## 45. 扎克伯格冻结人工智能招聘，疑虑泡沫风险

**原文标题**: Mark Zuckerberg freezes AI hiring amid bubble fears

**原文链接**: [https://www.telegraph.co.uk/business/2025/08/21/zuckerberg-freezes-ai-hiring-amid-bubble-fears/](https://www.telegraph.co.uk/business/2025/08/21/zuckerberg-freezes-ai-hiring-amid-bubble-fears/)

马克·扎克伯格暂停Meta人工智能招聘，因担忧巨额投资未达预期回报，引发人工智能泡沫恐慌。此次冻结影响Meta的“超级智能实验室”，逆转了近期从OpenAI和谷歌等竞争对手高薪挖角人工智能研究人员的招聘狂潮。

此前，科技股价值下跌，原因是人们对人工智能投资的盈利能力持怀疑态度。麻省理工学院的一份报告称，95%的公司在人工智能投资上“零回报”，进一步加剧了这些担忧。Meta发言人淡化了此次冻结，将其归因于组织规划。

扎克伯格亲自参与人工智能开发，包括追求“个人超级智能”，并承诺对人工智能数据中心进行前所未有的投资来吸引顶尖人才。然而，由于战略调整，人工智能部门面临中断，导致最新人工智能模型的发布延迟。

摩根士丹利的分析师警告称，人工智能员工薪资的飙升可能会对股东价值产生负面影响。对最新ChatGPT版本GPT-5的反响平淡，以及Sam Altman将人工智能炒作比作互联网泡沫，进一步加剧了人们日益增长的忧虑。

---

## 46. 为什么D3如此冗长？

**原文标题**: Why is D3 so Verbose?

**原文链接**: [https://theheasman.com/short_stories/why-is-d3-code-so-long-and-complicated-or-why-is-it-so-verbose/](https://theheasman.com/short_stories/why-is-d3-code-so-long-and-complicated-or-why-is-it-so-verbose/)

本文以幽默的方式探讨了D3.js库的冗长性，将其戏称为一门“语言”，以达到戏剧性的效果。作者在学习D3的过程中，将在Excel中创建箱线图的便捷性与D3中所需的194行代码进行了对比。尽管最初感到沮丧，但他们认为D3的冗长性是其强大和灵活性的关键。

作者解释说，D3本质上是为浏览器提供指令，使其根据数据绘制SVG形状。即使绘制一条简单的线也需要指定其端点的坐标。然而，这种细致的控制实现了广泛的定制和艺术表达。与Excel等工具中预先构建的图表选项不同，D3允许定制可视化效果，以适应特定的数据和所需的美学。

虽然Datawrapper和Flourish等工具为基本图表提供了更简单的解决方案，但D3对于创建独特而复杂的可视化效果仍然很有价值，例如滚动叙事和流图。作者总结说，最初是一种负担的冗长性最终变成了一种优势，使数据可视化者能够制作个性化且有影响力的叙事。文章最后轻松地宣传了作者的newsletter，突出了D3的复杂性与订阅获取见解的简单性之间的对比。

---

## 47. 柯尔莫哥洛夫-阿诺德网络之哲学思考 (2024)

**原文标题**: Philosophical Thoughts on Kolmogorov-Arnold Networks (2024)

**原文链接**: [https://kindxiaoming.github.io/blog/2024/kolmogorov-arnold-networks/](https://kindxiaoming.github.io/blog/2024/kolmogorov-arnold-networks/)

本文从哲学角度探讨了柯尔莫哥洛夫-阿诺德网络（KANs）与多层感知机（MLPs）的对比。作者认为，尽管MLPs和KANs在基础层面上可能具有相同的表达能力，但由于优化、泛化和可解释性等涌现属性，它们本质上是不同的。

核心差异在于它们的哲学立场：MLPs体现了整体论（“多即不同”），通过具有固定激活函数的简单神经元之间的复杂连接来实现复杂性。相反，KANs倾向于还原论，在更简单的网络结构中采用复杂的、可学习的激活函数。MLPs的力量源于完全连接结构中产生的涌现行为，而KANs则通过其单个单元的复杂性和对网络分解的还原论方法来获得力量。

作者认为，KANs更符合科学方法，科学方法在历史上更倾向于还原论。将像胡克定律这样的符号公式编译到神经网络中的例子支持了这一点，由于KANs具有灵活的激活函数，因此更容易实现。将科学公式编译到具有ReLu激活函数的MLP中很困难，但由于可学习的激活函数，KANs更容易实现。

文章最后强调，没有一种模型是普遍优越的。KANs可能在符合还原论的任务中表现出色，尤其是在科学领域，而MLPs已被证明在视觉和语言等其他领域有效。作者鼓励进行实证实验，以及哲学推理，以充分理解KANs和MLPs的优势和局限性。

---

## 48. Show HN: Splice – 电缆线束和电气组件的CAD

**原文标题**: Show HN: Splice – CAD for Cable Harnesses and Electrical Assemblies

**原文链接**: [https://splice-cad.com](https://splice-cad.com)

这篇“Show HN”提交介绍了一款名为“Splice”的CAD（计算机辅助设计）工具，专为线束和电气组件设计。极简短的描述表明，Splice旨在解决设计和管理这些复杂系统时遇到的独特挑战。虽然提供的内容细节有限，但我们可以推断其目的：

*   **专业CAD：** Splice不是通用的CAD程序，而是专门为从事线束和电气组件的电气工程师和设计师量身定制的。
*   **问题解决：** 它的目标是简化这些组件的设计、文档编制，并可能简化制造流程。
*   **效率：** 通过提供专用工具，与使用通用CAD软件处理这些特定任务相比，Splice可能旨在提高效率和准确性。

本质上，Splice被呈现为创建、可视化和管理线束和电气组件中固有复杂设计的解决方案，暗示了潜在的功能，如线路布线、元件放置和自动文档生成。它可能面向汽车、航空航天和电子制造等复杂布线系统至关重要的行业的专业人士。

---

## 49. 科学家不再觉得 X 在专业上有用，转而使用 Bluesky。

**原文标题**: Scientists No Longer Find X Professionally Useful, and Have Switched to Bluesky

**原文链接**: [https://academic.oup.com/icb/advance-article-abstract/doi/10.1093/icb/icaf127/8196180?redirectedFrom=fulltext&login=false](https://academic.oup.com/icb/advance-article-abstract/doi/10.1093/icb/icaf127/8196180?redirectedFrom=fulltext&login=false)

无法访问文章链接。

---

## 50. Show HN: 纯 Rust 实现的超高速嵌入式键值存储

**原文标题**: Show HN: Ultra-fast, embedded KV store in pure Rust

**原文链接**: [https://github.com/mehrantsi/FeOxDB](https://github.com/mehrantsi/FeOxDB)

FeOxDB：一款纯Rust编写的超快速嵌入式键值数据库，旨在实现GET和INSERT操作的亚微秒级延迟。它强调通过DashMap和Crossbeam SkipList实现的无锁并发，以及Linux上可选的io_uring支持以实现内核旁路I/O。

该数据库提供灵活的存储选项，包括纯内存模式和具有异步I/O的持久模式。主要功能包括JSON Patch支持（RFC 6902）、原子计数器、写入缓冲、用于淘汰的CLOCK缓存、实时性能统计以及通过自动合并实现的零碎片。

FeOxDB通过牺牲持久性来优先考虑性能。它使用后写日志，这会根据刷新间隔和写入吞吐量引入有界数据丢失窗口。用户可以显式刷新数据以获得更强的保证。

该文档提供了一个快速入门指南，其中包含安装说明和涵盖内存和持久存储的基本用法示例。它还演示了高级配置选项、并发访问模式、范围查询、JSON补丁操作和原子计数器操作。

基准测试显示出令人鼓舞的性能，在M3 Max上，GET操作约为200-260ns，INSERT操作约为700ns。该架构利用无锁设计、分片写入缓冲区、批量刷新和可选的io_uring集成。API文档涵盖了主要数据库接口、配置构建器、错误类型和性能指标。

---

## 51. 旅行者号错过了，但詹姆斯·韦伯刚刚发现了天王星隐藏的卫星

**原文标题**: Voyager missed it, but James Webb Just Found Uranus' hidden moon

**原文链接**: [https://www.sciencedaily.com/releases/2025/08/250821004237.htm](https://www.sciencedaily.com/releases/2025/08/250821004237.htm)

2025年8月，天文学家使用詹姆斯·韦伯太空望远镜（JWST）发现了一颗新的天王星卫星，使该行星的卫星总数达到29颗。这颗小型卫星，暂定名为S/2025 U 1，估计直径仅约六英里（10公里），并且在1986年旅行者2号飞掠期间未被探测到。

该发现是由西南研究院（SwRI）的Maryame El Moutamid博士领导的团队在JWST的客座观测员计划中完成的。这颗卫星是在2025年2月2日近红外相机拍摄的一系列长曝光照片中被识别出来的。

天王星因其极端的轴倾斜而被称为“横向行星”，是太阳系中第七颗行星，主要由氢、氦和甲烷组成。这颗新卫星在奥菲莉亚和比安卡轨道之间运行，位于天王星内环的边缘。它位于距离行星中心约35,000英里（56,250公里）的赤道平面上。

虽然旅行者2号此前发现了光环和10颗较小的卫星，但这颗新卫星的小尺寸和微弱亮度使其当时无法被探测到。天王星的其他28颗卫星以莎士比亚和亚历山大·蒲柏作品中的人物命名，该团队正在考虑从这些作品中为这颗新卫星命名。

---

## 52. D4D4

**原文标题**: D4D4

**原文链接**: [https://www.nmichaels.org/musings/d4d4/d4d4/](https://www.nmichaels.org/musings/d4d4/d4d4/)

内森调查反汇编ARM代码中一种奇怪的模式，即`d4d4`指令出现在不可达的位置。起初他怀疑是对齐填充，但发现LLVM链接器(LLD)插入了这些指令，而不是编译器。进一步的实验表明，LLD使用`d4d4`将目标文件对齐到32位边界，这与使用零填充的GNU链接器不同。

深入研究LLD源代码和提交日志，内森发现这些`d4d4`序列原本打算作为“陷阱指令”，这是Theo de Raadt的建议。然而，通过查阅ARMv7-M架构参考手册，内森发现`d4d4`根本不是陷阱。相反，它被解释为一条条件相对分支，如果条件满足，可能会导致意外的代码执行。

反汇编工具将`d4d4`解释为相对于当前位置向后跳转0x58个字节的相对分支。虽然这段代码*应该*是不可达的，但作者认为使用条件分支作为陷阱指令是有问题的，因为与真正的陷阱不同，它不会使处理器停止运行。因此，他得出结论，这是LLD在实现“trapInstr”时的错误，并打算提交一份错误报告。这篇文章强调了预期功能与代码实际行为之间的差异，展示了理解底层架构的重要性。

---

## 53. 政府将审查所有5500万签证持有者是否存在可被驱逐的出入境违规行为。

**原文标题**: Administration will review all 55M visa holders for deportable violations

**原文链接**: [https://apnews.com/article/trump-visas-deportations-068ad6cd5724e7248577f17592327ca4](https://apnews.com/article/trump-visas-deportations-068ad6cd5724e7248577f17592327ca4)

无法访问文章链接。

---

## 54. 爱普生 MX-80 字体

**原文标题**: Epson MX-80 Fonts

**原文链接**: [https://mw.rat.bz/MX-80/](https://mw.rat.bz/MX-80/)

无法访问文章链接。

---

## 55. 两次随机选择的力量 (2012)

**原文标题**: The power of two random choices (2012)

**原文链接**: [https://brooker.co.za/blog/2012/01/17/two-random.html](https://brooker.co.za/blog/2012/01/17/two-random.html)

Marc Brooker的博文《两个随机选择的力量》探讨了分布式系统中高效的负载均衡策略，对比了集中式和分散式方法。集中式负载均衡器能提供精确的负载分配，但引入了成本、延迟和潜在的单点故障。纯随机分配（如DNS轮询）在大型同构系统中可能足够，但在较小系统或异构请求中会失效。

文章强调了在分布式负载均衡中使用陈旧负载数据的弊端，这会导致“蜂群行为”，即请求涌向最近空闲的主机，导致忙碌和空闲状态之间的震荡。

Mitzenmacher的研究提出了一种出人意料的有效解决方案：“两个随机选择的力量”。客户端不基于可能过时的信息选择最佳服务器，而是随机选择两个服务器，并选择负载最低的一个（或基于缓存数据认为负载最低的一个）。

一项比较随机选择、最佳服务器选择、二选一和三选一的模拟实验表明，“二选一”方法的优越性，即使使用延迟数据也是如此。这种策略在利用实时负载信息与抵御蜂群行为之间取得了平衡。它在各种刷新间隔范围内始终优于其他方法，突显了该算法的稳健性和简单性。文章鼓励读者深入研究Mitzenmacher的调查，以进行更深入的数学分析和进一步应用该原理。

---

## 56. SK海力士超越三星，成为全球最大DRAM制造商

**原文标题**: SK hynix dethrones Samsung as world’s top DRAM maker

**原文链接**: [https://koreajoongangdaily.joins.com/news/2025-08-15/business/tech/Thanks-Nvidia-SK-hynix-dethrones-Samsung-as-worlds-top-DRAM-maker-for-first-time-in-over-30-years/2376834](https://koreajoongangdaily.joins.com/news/2025-08-15/business/tech/Thanks-Nvidia-SK-hynix-dethrones-Samsung-as-worlds-top-DRAM-maker-for-first-time-in-over-30-years/2376834)

SK海力士逾三十年来首次超越三星电子，成为全球领先的DRAM（动态随机存取存储器）制造商。 市场领导地位的转变主要归功于SK海力士在高带宽存储器（HBM）市场的优势，HBM是AI加速器的关键组件，特别是英伟达使用的那些。

文章强调，由于人工智能热潮带来的需求激增，SK海力士对HBM的关注，特别是其HBM3和HBM3E芯片，已被证明非常成功。 英伟达在其高性能GPU中采用SK海力士的HBM技术，极大地提升了该公司的收入和市场份额。

虽然三星也生产HBM，但据报道，它在匹配SK海力士的性能和良率方面面临挑战，导致SK海力士占据了更大的利润丰厚的HBM市场份额。 这使得他们在整体DRAM市场份额上超越了三星。

文章表明，这标志着半导体行业的一个重大转折点，展示了适应新兴技术和不断变化的市场需求的重要性。 专注于人工智能相关的内存解决方案（如HBM）已被证明是SK海力士的制胜策略，使其能够取代长期以来的领导者三星。 虽然三星仍然是一个主要参与者，但他们需要提高其HBM的生产和性能，才能重夺榜首。

---

## 57. 洋葱报复刊纸质版，豪赌奏效。

**原文标题**: The Onion brought back its print edition and the gamble is paying off

**原文链接**: [https://www.wsj.com/business/media/the-onion-print-subscribers-6c24649c](https://www.wsj.com/business/media/the-onion-print-subscribers-6c24649c)

无法访问文章链接。

---

## 58. 超越Logo：如何在二维码中编织完整图像

**原文标题**: Beyond the Logo: How We're Weaving Full Images Inside QR Codes

**原文链接**: [https://blog.nitroqr.com/beyond-the-logo-how-were-weaving-full-images-inside-qr-codes](https://blog.nitroqr.com/beyond-the-logo-how-were-weaving-full-images-inside-qr-codes)

好的，我已阅读文章。摘要如下：

NitroQR 博客文章“超越Logo：我们如何在二维码中编织完整图像”详细介绍了 NitroQR 如何开发出一种技术，将完整、复杂的图像直接嵌入二维码中，超越了仅仅嵌入一个小logo的传统做法。

文章解释说，传统上，将图像嵌入二维码涉及到在中心放置一个logo，但二维码的数据容量和纠错能力限制了logo的尺寸和复杂度。NitroQR 的创新之处在于，它允许将整个图像编码到二维码的结构中，使图像成为代码本身的组成部分。

文章强调，这种方法的主要优点是：

*   **视觉吸引力：** 创建更具视觉吸引力和美观的二维码，改善品牌形象并吸引更多扫描。
*   **品牌整合：** 更强的品牌存在感，因为图像是代码的组成部分。
*   **纠错优化：** NitroQR 优化了纠错能力，即使集成了大量图像数据，也能确保可扫描性。
*   **创意可能性：** 为使用二维码的创意营销活动和设计开辟了新途径。

文章强调，这是通过复杂的算法和专有技术实现的，这些算法和技术有效地平衡了图像数据和纠错能力，以保持可扫描性。 NitroQR 将这项技术视为二维码设计方面的一项重大进步，从简单的 logo 转变为完全集成的图像体验。他们认为，这种新方法将彻底改变二维码在营销和品牌推广中的应用方式。

---

## 59. Show HN: 我用 Git 替换了向量数据库来实现 AI 记忆（概念验证）

**原文标题**: Show HN: I replaced vector databases with Git for AI memory (PoC)

**原文链接**: [https://github.com/Growth-Kinetics/DiffMem](https://github.com/Growth-Kinetics/DiffMem)

DiffMem是一个概念验证项目，探索使用Git作为AI代理的内存后端，提供传统数据库和向量存储之外的替代方案。它将AI代理知识的“当前状态”存储在人类可读的Markdown文件中，利用Git追踪历史变更，并使用内存中的BM25索引进行快速检索。

核心思想是利用Git的优势：关注当前状态以实现高效查询，利用差异智能跟踪内存演变，使用纯文本Markdown实现持久性和可移植性，以及通过将当前信息与历史数据分离来提高效率。这对于处理不断演变的个人知识的长期AI系统尤其有用。

DiffMem由写入代理、上下文管理器和搜索代理组成，并通过API层进行编排。它通过仅索引当前状态文件来最大限度地减少查询中的噪声，通过Git历史记录实现可扩展的演变跟踪，并提供开发人员友好的环境。

虽然仍处于原型阶段，但DiffMem展示了实体创建/更新、多深度上下文组装、语义搜索和基于Git的时间查询。目前的局限性包括手动Git同步、基本错误处理以及缺乏并发锁。

该项目设想未来AI记忆是版本化的和协作的，从而实现代理驱动的修剪、共享记忆的多代理系统、跟踪自身变更的时间代理以及将Git与向量嵌入相结合的混合存储。该项目是开源的，欢迎贡献，旨在构建一个分布式、隐私优先的AI记忆系统。

---

## 60. Show HN: 从浏览器内部使用 Common Lisp

**原文标题**: Show HN: Using Common Lisp from Inside the Browser

**原文链接**: [https://turtleware.eu/posts/Using-Common-Lisp-from-inside-the-Browser.html](https://turtleware.eu/posts/Using-Common-Lisp-from-inside-the-Browser.html)

丹尼尔·科赫曼斯基介绍了Web嵌入式通用Lisp (WECL) 项目，该项目旨在将Common Lisp与Web浏览器环境集成。本文详细介绍了其目前的进展、技术方面、局限性和未来计划。

WECL允许使用`<script type="text/common-lisp">`标签将Common Lisp代码直接嵌入到HTML中。一个低级JavaScript外部函数接口(JS-FFI)提供了与JavaScript交互的宏，包括定义变量、对象、函数、方法、getter、setter和回调函数。本文概述了可用的运算符和参数类型。

作者开发了LIME/SLUG，一个SLIME/SWANK的适配器，可以通过Websocket从Emacs与WECL交互。这有助于在浏览器内进行代码编译、REPL使用和调试。

将CL运行时注入到任意网站的演示展示了WECL的多功能性，尽管这更像是一种噱头。

当前的局限性包括由于Emscripten的限制以及垃圾回收问题而缺乏线程原语。未来的计划包括将运行时移植到WASI，利用浏览器的GC，并使用ASYNCIFY实现协作线程。作者承认，目前JS和CL的互操作性不稳定，并且影响性能。

---

## 61. 思科宣布大规模裁员，此前刚发布营收飙升报告

**原文标题**: Cisco announces mass layoffs just after soaring revenue report

**原文链接**: [https://www.sfgate.com/tech/article/bay-area-tech-titan-announces-layoffs-strong-20826542.php](https://www.sfgate.com/tech/article/bay-area-tech-titan-announces-layoffs-strong-20826542.php)

思科：营收增长强劲，仍裁员数千人。

---

## 62. Waymo获准在纽约市开始自动驾驶测试

**原文标题**: Waymo Approved to Start Autonomous Testing in NYC

**原文链接**: [https://techcrunch.com/2025/08/22/waymo-approved-to-start-autonomous-vehicle-testing-in-new-york-city/](https://techcrunch.com/2025/08/22/waymo-approved-to-start-autonomous-vehicle-testing-in-new-york-city/)

Waymo获准在纽约市测试自动驾驶车辆，为在这个充满挑战的都市环境中推出无人出租车服务迈出重要一步。该许可允许Waymo在曼哈顿和布鲁克林市中心部署最多八辆捷豹I-Pace SUV，有效期至九月下旬。这些车辆将在训练有素的安全驾驶员的监督下运行，以便在需要时进行干预。

此次测试附带若干条件，包括禁止接载乘客以及定期向市交通局报告。该许可是市长埃里克·亚当斯新自动驾驶车辆安全机制的一部分，要求Waymo与急救人员协调并提交详细的测试和安全计划。

自2021年以来，Waymo一直在探索在纽约市运营的可能性，使用其小型货车手动绘制城市地图。获得许可需要与立法者和组织进行数月的会议。虽然Waymo已在旧金山、奥斯汀、菲尼克斯和洛杉矶等其他城市运营，但纽约市因其交通复杂性而带来了一系列独特的挑战。在试用期结束时，Waymo需要申请延期才能继续测试。

---

## 63. 谷歌赢得价值超过100亿美元的六年Meta云服务协议

**原文标题**: Google scores six-year Meta cloud deal worth over $10B

**原文链接**: [https://www.cnbc.com/2025/08/21/google-scores-six-year-meta-cloud-deal-worth-over-10-billion.html](https://www.cnbc.com/2025/08/21/google-scores-six-year-meta-cloud-deal-worth-over-10-billion.html)

谷歌与Meta达成价值超100亿美元的六年云服务协议。该协议突显了人工智能工作负载扩展对云基础设施日益增长的需求。Meta此前主要依赖亚马逊云服务和微软Azure，目前正在大幅扩展其云基础设施，以支持其人工智能计划，包括Llama系列模型的开发以及人工智能在其各项服务中的集成。

对于在云基础设施市场与亚马逊云服务和微软Azure竞争的谷歌来说，这是一项重大胜利。谷歌云部门表现出强劲的增长势头，第二季度收入增长了32%。Meta在人工智能基础设施方面的大量投资（预计2025年支出将达1140亿至1180亿美元）突显了此次合作对两家公司的战略重要性。虽然谷歌和Meta在在线广告领域是竞争对手，但Meta不断增长的云需求使其必须与包括亚马逊、微软以及现在的谷歌在内的多家供应商建立合作关系。

---

## 64. 逆向物理播客亚文化

**原文标题**: The contrarian physics podcast subculture

**原文链接**: [https://timothynguyen.org/2025/08/21/physics-grifters-eric-weinstein-sabine-hossenfelder-and-a-crisis-of-credibility/](https://timothynguyen.org/2025/08/21/physics-grifters-eric-weinstein-sabine-hossenfelder-and-a-crisis-of-credibility/)

本文详述了作者与埃里克·魏因斯坦、萨宾·霍森菲尔德、布赖恩·基廷和科特·杰蒙加尔等一群科学传播者的交往经历，并指控他们将获取观众和部落忠诚置于科学诚信之上。作者认为，这个群体表面上提倡自由探究，却积极压制批评，特别是针对埃里克·魏因斯坦的“几何统一理论”（GU）的批评。

作为GU详细反驳的合著者，作者声称魏因斯坦试图通过恐吓来压制他的批评，包括施压一个播客节目删除讨论该反驳的一集。他还指责杰蒙加尔取消了一次采访，以避免对GU的批评。此外，作者指出，魏因斯坦通过攻击合著者的匿名性和发起人身攻击来回避解决批评的科学实质。

文章进一步声称，霍森菲尔德、基廷和杰蒙加尔一直都在支持魏因斯坦，要么是推广存在缺陷的GU，要么是制造关于其有效性的模糊性。基廷尤其受到批评，因为他多次主持魏因斯坦的节目，推广GU，并拒绝与作者的批评进行互动。霍森菲尔德则被指控制造了一种误导性的叙事。作者将此描述为科学传播领域的知名人士为了保护他们的“部落”和维护他们的平台而牺牲科学严谨性的案例。

---

## 65. 我强迫每位工程师都去接听销售电话，结果他们重写了我们的平台。

**原文标题**: I forced every engineer to take sales calls and they rewrote our platform

**原文链接**: [https://old.reddit.com/r/Entrepreneur/comments/1mw5yfg/forced_every_engineer_to_take_sales_calls_they/](https://old.reddit.com/r/Entrepreneur/comments/1mw5yfg/forced_every_engineer_to_take_sales_calls_they/)

好的，以下是基于所提供标题的摘要，推断可能的内容和论点，因为我无法直接访问该URL：

**摘要 (基于标题：我强迫所有工程师接听销售电话，结果他们重写了我们的平台)**

这篇发布在 r/Entrepreneur 子版块上的文章，可能详细描述了一种策略，即作者强制要求所有软件工程师参与销售电话。其核心前提是，通过让工程师直接了解客户的需求、痛点以及销售过程，他们能够更深入地了解公司平台的实际应用和局限性。

正如标题所暗示的那样，由此产生的影响是对平台进行了重大重写。 这意味着在接触销售电话之前，工程师可能是在假设的基础上运作，或者专注于未直接满足客户需求或有助于成功销售的功能。 在第一手听到客户反馈后，他们能够更有效地确定开发工作的优先级。

可能的主要收获包括：

*   **更好地了解客户需求：** 直接接触销售互动使工程师们对客户真正想要什么以及他们如何使用该平台有了具体的了解。
*   **增加对销售团队的同情：** 工程师们更加了解销售团队面临的挑战，以及某些功能在完成交易中的重要性。
*   **更好地确定开发工作的优先级：** 工程师们现在可以专注于直接解决客户痛点并有助于销售成功的功能，从而打造一个更有效且用户友好的平台。
*   **平台采用率和收入可能增加：** 通过使平台更紧密地与客户需求保持一致，此次重写可能导致更高的采用率和更高的公司收入。

这篇文章可能认为，打破工程和销售之间的壁垒，并培养工程师直接与客户互动，是产品开发和公司增长的一项有价值的策略。

---

## 66. 如何画太空侵略者

**原文标题**: How to Draw a Space Invader

**原文链接**: [https://muffinman.io/blog/invaders/](https://muffinman.io/blog/invaders/)

本文详述了一个太空侵略者生成器的创建过程，其诞生源于将矢量3D渲染器应用于一个简单有趣项目的愿望。作者最初绘制了38个独特的侵略者，然后着手解决以编程方式生成它们的问题。

该方法包括为侵略者的身体创建一个矢量多边形，利用对称性仅生成一侧并将其镜像。然后使用“粗线”算法添加肢体（触手和角），该算法会加粗折线。在整个过程中都使用了具有约束的随机性来引入变化。

然后，通过检查像素中心是否落在矢量形状内来将矢量表示像素化。眼睛是从预定义的集合中添加的，并使用OKLCH颜色空间应用颜色以获得一致的亮度。 CSS变量用于方便的颜色操作和调试。

本文解释了如何通过触手、角和眼睛的轻微移动来动画化侵略者，模仿原始游戏。增加网格大小可以提供更多细节，但超过一定限制会破坏像素化错觉。

作者强调完成项目并发布它们，即使存在待改进之处。生成器的代码可在GitHub上找到。本文还提到了使用Anime.js进行动画制作，并鼓励读者探索另一篇关于绘制SVG绳索的互动博客文章。核心概念是使用智能随机化和几何原理将矢量图形转换为可识别的像素艺术。

---

## 67. 为什么动漫猫娘阻止我访问Linux内核？

**原文标题**: Why are anime catgirls blocking my access to the Linux kernel?

**原文链接**: [https://lock.cmpxchg8b.com/anubis.html](https://lock.cmpxchg8b.com/anubis.html)

本文批判了 Anubis 系统，该系统利用动漫猫娘头像和工作量证明挑战（类似于加密货币挖矿）来阻止 AI 爬虫访问网站。作者 Anubis 质疑 Anubis 在保护网站免受 AI 爬虫侵害方面的有效性，特别是其在 git.kernel.org 和 lore.kernel.org（托管 Linux 内核的网站）上的应用。

作者认为，解决 SHA-256 谜题的挑战对于拥有大量计算资源的 AI 供应商来说是微不足道的，但对于资源有限的人类来说却负担沉重。作者计算得出，AI 绕过 Anubis 防护的成本在所有已知部署中都可以忽略不计。

作者将 Anubis 与传统的 CAPTCHA（对计算机来说困难，对人类来说容易）以及过时的反垃圾邮件解决方案（如 Hashcash 和 Habeas）进行了对比。他提出了一个实际的解决方法，即使用 C 程序来挖掘所需的令牌，演示了用户如何轻松绕过 Anubis 挑战并获得有效的身份验证 Cookie。他发现了一个“双重支付”漏洞，即可以重复使用先前挖掘的令牌来获取新的 Cookie。他指出，维护者在他提交错误报告后不久就修复了该双重支付漏洞。

作者的结论是，Anubis 的方法对于有决心的 AI 爬虫来说无效，反而使合法用户更难访问，同时浪费能源。他强调，该分析是在没有 AI 协助的情况下进行的。

---

## 68. Show HN: ChartDB Cloud – Visualize and Share Database Diagrams

**原文标题**: Show HN: ChartDB Cloud – Visualize and Share Database Diagrams

**原文链接**: [https://app.chartdb.io](https://app.chartdb.io)

生成摘要时出错

---

## 69. You Should Add Debug Views to Your DB

**原文标题**: You Should Add Debug Views to Your DB

**原文链接**: [https://chrispenner.ca/posts/views-for-debugging](https://chrispenner.ca/posts/views-for-debugging)

生成摘要时出错

---

## 70. French firm Gouach is pitching an Infinite Battery with replaceable cells

**原文标题**: French firm Gouach is pitching an Infinite Battery with replaceable cells

**原文链接**: [https://arstechnica.com/gadgets/2025/05/gouach-wants-you-to-insert-and-pluck-the-cells-from-its-infinite-e-bike-battery/](https://arstechnica.com/gadgets/2025/05/gouach-wants-you-to-insert-and-pluck-the-cells-from-its-infinite-e-bike-battery/)

生成摘要时出错

---

## 71. Show HN: I was curious about spherical helix, ended up making this visualization

**原文标题**: Show HN: I was curious about spherical helix, ended up making this visualization

**原文链接**: [https://visualrambling.space/moving-objects-in-3d/](https://visualrambling.space/moving-objects-in-3d/)

生成摘要时出错

---

## 72. Show HN: Luminal – Open-source, search-based GPU compiler

**原文标题**: Show HN: Luminal – Open-source, search-based GPU compiler

**原文链接**: [https://github.com/luminal-ai/luminal](https://github.com/luminal-ai/luminal)

生成摘要时出错

---

## 73. Analysis of the GFW's Unconditional Port 443 Block on August 20, 2025

**原文标题**: Analysis of the GFW's Unconditional Port 443 Block on August 20, 2025

**原文链接**: [https://gfw.report/blog/gfw_unconditional_rst_20250820/en/](https://gfw.report/blog/gfw_unconditional_rst_20250820/en/)

生成摘要时出错

---

## 74. Home Depot sued for 'secretly' using facial recognition at self-checkouts

**原文标题**: Home Depot sued for 'secretly' using facial recognition at self-checkouts

**原文链接**: [https://petapixel.com/2025/08/20/home-depot-sued-for-secretly-using-facial-recognition-technology-on-self-checkout-cameras/](https://petapixel.com/2025/08/20/home-depot-sued-for-secretly-using-facial-recognition-technology-on-self-checkout-cameras/)

生成摘要时出错

---

## 75. The Open-Office Trap (2014)

**原文标题**: The Open-Office Trap (2014)

**原文链接**: [https://www.newyorker.com/business/currency/the-open-office-trap](https://www.newyorker.com/business/currency/the-open-office-trap)

生成摘要时出错

---

## 76. Show HN: I integrated my from-scratch TCP/IP stack into the xv6-riscv OS

**原文标题**: Show HN: I integrated my from-scratch TCP/IP stack into the xv6-riscv OS

**原文链接**: [https://github.com/pandax381/xv6-riscv-net](https://github.com/pandax381/xv6-riscv-net)

生成摘要时出错

---

## 77. Electrical Grid Mapping

**原文标题**: Electrical Grid Mapping

**原文链接**: [https://github.com/open-energy-transition/Awesome-Electrical-Grid-Mapping](https://github.com/open-energy-transition/Awesome-Electrical-Grid-Mapping)

生成摘要时出错

---

## 78. Python f-string cheat sheets (2022)

**原文标题**: Python f-string cheat sheets (2022)

**原文链接**: [https://fstring.help/cheat/](https://fstring.help/cheat/)

生成摘要时出错

---

## 79. How to stop feeling lost in tech: the wafflehouse method

**原文标题**: How to stop feeling lost in tech: the wafflehouse method

**原文链接**: [https://www.yacinemahdid.com/p/how-to-stop-feeling-lost-in-tech](https://www.yacinemahdid.com/p/how-to-stop-feeling-lost-in-tech)

生成摘要时出错

---

## 80. Happy 100000th birthday, Debian

**原文标题**: Happy 100000th birthday, Debian

**原文链接**: [https://lists.debian.org/debian-devel-announce/2025/08/msg00006.html](https://lists.debian.org/debian-devel-announce/2025/08/msg00006.html)

生成摘要时出错

---

## 81. Project to formalise a proof of Fermat’s Last Theorem in the Lean theorem prover

**原文标题**: Project to formalise a proof of Fermat’s Last Theorem in the Lean theorem prover

**原文链接**: [https://imperialcollegelondon.github.io/FLT/](https://imperialcollegelondon.github.io/FLT/)

生成摘要时出错

---

## 82. Margin debt surges to record high

**原文标题**: Margin debt surges to record high

**原文链接**: [https://www.advisorperspectives.com/dshort/updates/2025/07/23/margin-debt-surges-record-high-june-2025](https://www.advisorperspectives.com/dshort/updates/2025/07/23/margin-debt-surges-record-high-june-2025)

生成摘要时出错

---

## 83. Don't pick weird subnets for embedded networks, use VRFs

**原文标题**: Don't pick weird subnets for embedded networks, use VRFs

**原文链接**: [https://blog.brixit.nl/dont-pick-weird-subnets-for-embedded-networks/](https://blog.brixit.nl/dont-pick-weird-subnets-for-embedded-networks/)

生成摘要时出错

---

## 84. The Core of Rust

**原文标题**: The Core of Rust

**原文链接**: [https://jyn.dev/the-core-of-rust/](https://jyn.dev/the-core-of-rust/)

生成摘要时出错

---

## 85. Adding my home electricity uptime to status.href.cat

**原文标题**: Adding my home electricity uptime to status.href.cat

**原文链接**: [https://aggressivelyparaphrasing.me/2025/08/21/adding-my-home-electricity-uptime-to-status-href-cat/](https://aggressivelyparaphrasing.me/2025/08/21/adding-my-home-electricity-uptime-to-status-href-cat/)

生成摘要时出错

---

## 86. Code review can be better

**原文标题**: Code review can be better

**原文链接**: [https://tigerbeetle.com/blog/2025-08-04-code-review-can-be-better/](https://tigerbeetle.com/blog/2025-08-04-code-review-can-be-better/)

生成摘要时出错

---

## 87. The attr() function in CSS now supports types

**原文标题**: The attr() function in CSS now supports types

**原文链接**: [https://www.amitmerchant.com/attr-function-types-css/](https://www.amitmerchant.com/attr-function-types-css/)

生成摘要时出错

---

## 88. Unification (2018)

**原文标题**: Unification (2018)

**原文链接**: [https://eli.thegreenplace.net/2018/unification/](https://eli.thegreenplace.net/2018/unification/)

生成摘要时出错

---

## 89. Sixteen bottles of wine riddle

**原文标题**: Sixteen bottles of wine riddle

**原文链接**: [https://chriskw.xyz/2025/08/11/Wine/](https://chriskw.xyz/2025/08/11/Wine/)

生成摘要时出错

---

## 90. Introduction to AT Protocol

**原文标题**: Introduction to AT Protocol

**原文链接**: [https://mackuba.eu/2025/08/20/introduction-to-atproto/](https://mackuba.eu/2025/08/20/introduction-to-atproto/)

生成摘要时出错

---

## 91. An Update on Pytype

**原文标题**: An Update on Pytype

**原文链接**: [https://github.com/google/pytype](https://github.com/google/pytype)

生成摘要时出错

---

## 92. Mirrorshades: The Cyberpunk Anthology (1986)

**原文标题**: Mirrorshades: The Cyberpunk Anthology (1986)

**原文链接**: [https://www.rudyrucker.com/mirrorshades/HTML/](https://www.rudyrucker.com/mirrorshades/HTML/)

生成摘要时出错

---

## 93. Data, objects, and how we're railroaded into poor design (2018)

**原文标题**: Data, objects, and how we're railroaded into poor design (2018)

**原文链接**: [https://www.tedinski.com/2018/01/23/data-objects-and-being-railroaded-into-misdesign.html](https://www.tedinski.com/2018/01/23/data-objects-and-being-railroaded-into-misdesign.html)

生成摘要时出错

---

## 94. Databricks is raising a Series K Investment at >$100B valuation

**原文标题**: Databricks is raising a Series K Investment at >$100B valuation

**原文链接**: [https://www.databricks.com/company/newsroom/press-releases/databricks-raising-series-k-investment-100-billion-valuation](https://www.databricks.com/company/newsroom/press-releases/databricks-raising-series-k-investment-100-billion-valuation)

生成摘要时出错

---

## 95. Sütterlin

**原文标题**: Sütterlin

**原文链接**: [https://en.wikipedia.org/wiki/S%C3%BCtterlin](https://en.wikipedia.org/wiki/S%C3%BCtterlin)

生成摘要时出错

---

## 96. Universal Tool Calling Protocol (UTCP)

**原文标题**: Universal Tool Calling Protocol (UTCP)

**原文链接**: [https://github.com/universal-tool-calling-protocol/python-utcp](https://github.com/universal-tool-calling-protocol/python-utcp)

生成摘要时出错

---

## 97. AI Mode in Search gets new agentic features and expands globally

**原文标题**: AI Mode in Search gets new agentic features and expands globally

**原文链接**: [https://blog.google/products/search/ai-mode-agentic-personalized/](https://blog.google/products/search/ai-mode-agentic-personalized/)

生成摘要时出错

---

## 98. The issue of anti-cheat on Linux

**原文标题**: The issue of anti-cheat on Linux

**原文链接**: [https://tulach.cc/the-issue-of-anti-cheat-on-linux/](https://tulach.cc/the-issue-of-anti-cheat-on-linux/)

生成摘要时出错

---

## 99. AI crawlers, fetchers are blowing up websites; Meta, OpenAI are worst offenders

**原文标题**: AI crawlers, fetchers are blowing up websites; Meta, OpenAI are worst offenders

**原文链接**: [https://www.theregister.com/2025/08/21/ai_crawler_traffic/](https://www.theregister.com/2025/08/21/ai_crawler_traffic/)

生成摘要时出错

---

## 100. Show HN: PlutoPrint – Generate PDFs and PNGs from HTML with Python

**原文标题**: Show HN: PlutoPrint – Generate PDFs and PNGs from HTML with Python

**原文链接**: [https://github.com/plutoprint/plutoprint](https://github.com/plutoprint/plutoprint)

生成摘要时出错

---

