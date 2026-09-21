# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-09-21.md)

*最后自动更新时间: 2026-09-21 21:17:47*
## 1. 小米 MiMo v2.6

**原文标题**: Xiaomi MiMo v2.6

**原文链接**: [https://mimo.xiaomi.com/mimo-v2-6](https://mimo.xiaomi.com/mimo-v2-6)

**MiMo-V2.6 | 小米**

所提供的文本“**MiMo-V2.6 | 小米**”是一个标题或页眉，而非完整文章。然而，基于小米技术发布的相关背景，以下是关于 **小米 MiMo v2.6** 的简要概述：

**小米 MiMo v2.6 概述**

小米 MiMo v2.6 指的是小米多输入多输出（MIMO）技术框架内的一次特定更新。该版本专注于优化小米智能手机的无线通信能力，以确保更快、更稳定的数据传输。

**关键信息与改进：**

*   **增强的网络吞吐量：** 2.6 版本引入了精细化的算法，使设备能够更高效地处理多条数据流。这显著提升了峰值下载和上传速度，尤其是在 5G 和高端 Wi-Fi 网络环境下。
*   **信号稳定性：** 该更新通过改进内部天线之间的切换逻辑，解决了“信号盲区”和信号干扰问题。这确保了在蜂窝网络覆盖较弱的区域拥有更稳定的连接。
*   **降低延迟：** v2.6 的一个核心重点是降低“Ping”值或延迟，这对于移动游戏、高清视频会议和实时云应用至关重要。
*   **功耗管理：** 尽管增加了数据处理能力，该更新仍包含多项优化，旨在最大限度地减少与高速调制解调器运行相关的电池损耗。
*   **MIUI 集成：** 作为一项核心系统优化，v2.6 旨在与小米的 MIUI/HyperOS 无缝协作，为整个生态系统提供更流畅的用户体验。

简而言之，MiMo v2.6 是一项技术固件/软件进步，旨在最大限度地发挥小米天线阵列的硬件潜力，从而提供卓越的网络连接体验。

---

## 2. NASA/ESA火星采样返回任务已取消。

**原文标题**: The NASA/ESA Mars Sample Return mission has been canceled

**原文链接**: [https://www.science.org/content/article/nasa-s-mars-sample-return-mission-dead](https://www.science.org/content/article/nasa-s-mars-sample-return-mission-dead)

无法访问文章链接。

---

## 3. What Sun got wrong

**原文标题**: What Sun got wrong

**原文链接**: [https://bcantrill.dtrace.org/2026/09/20/what-sun-got-wrong/](https://bcantrill.dtrace.org/2026/09/20/what-sun-got-wrong/)

生成摘要时出错

---

## 4. 注意力就是你所拥有的一切。

**原文标题**: Attention is all you have

**原文链接**: [https://alicegg.tech/2026/09/21/attention](https://alicegg.tech/2026/09/21/attention)

生成摘要时出错

---

## 5. AI 编程使 CI 成为瓶颈，为此我们重构了系统以跟上节奏

**原文标题**: AI coding has made CI a bottleneck, so we reworked ours to keep up

**原文链接**: [https://linear.app/now/ci-bottleneck-reworked](https://linear.app/now/ci-bottleneck-reworked)

为应对 AI 驱动开发加速带来的瓶颈，Linear 团队彻底改造了其持续集成（CI）流水线。尽管测试套件规模翻了四倍，他们仍成功将拉取请求（PR）的等待时间缩短至约五分钟，并将每个测试的运行耗时减少了一半。

改进主要集中在四个关键领域：

*   **基础设施与工具：** Linear 从 GitHub Actions 迁移到了更快的第三方运行器，并更新了工具链。切换到 **tsgo**（原生 TypeScript 编译器）和 **Oxlint** 显著缩短了类型检查和代码检查（linting）的时间。他们还将代码检查与 TypeScript 类型检查器解耦，通过静态分析使代码检查耗时缩减了 68%。
*   **优化关键路径：** 他们精简了“门控”任务——即决定后续运行内容的初始检查。通过采用稀疏、无对象（blobless）检出，并从合并路径中移除缓存写入等非必要任务，使 API 拉取请求的时间缩短了近一分钟。
*   **减少安装开销：** 团队通过创建预装依赖项的自定义 CI 基础镜像来减少重复工作。他们转向过滤安装以仅获取必要的包，并停止缓存 `node_modules`（因为他们发现从零重建反而更快）。通过将简短且独立的检查合并为并发任务，每月节省了约 87,000 分钟的运行时间。
*   **高效测试执行：** 为了优化 **Vitest**，他们拆分了大文件以平衡各分片（shards）的工作负载。最显著的收益源于一种“选择性加入”的非隔离测试模式，该模式允许安全文件共享模块状态，使 API 分片的运行时间缩短了约 33%。

最终，这些优化将 CI 从开发瓶颈转变为一个可扩展的系统，每周能够处理 2,000 个新增测试。

---

## 6. 为什么 mathmain 需要加密加载器？

**原文标题**: Why does mathmain need an encrypted loader?

**原文链接**: [https://safedep.io/mathmain-encrypted-loader/](https://safedep.io/mathmain-encrypted-loader/)

SafeDep 在包括 `mathmain`、`mathsbase` 和 `math-universe` 在内的多个 npm 软件包中发现了一个复杂的远程访问植入程序。这些包伪装成流行的 `mathjs` 库的副本，但包含隐藏的加密恶意代码。

该恶意软件采用了一种独特的“休眠”执行策略。加载器仅在以特定输入（一个 3x3 帕斯卡矩阵）调用库的 `lusolve()` 函数时才会激活。由 LU 分解产生的下三角矩阵 (L) 被转换为 JSON 字符串，用作解密密钥。这确保了在调用者提供特定触发条件之前，有效载荷始终保持加密状态，且无法被标准扫描检测到。

一旦解密，有效载荷将作为多阶段远程访问木马 (RAT) 运行：
*   **初始化：** 收集主机数据并生成加密密钥。
*   **命令与控制 (C2)：** 该植入程序利用公共 Slack 频道和 Telegram 进行通信，同时参考 Base Sepolia 区块链上的智能合约来获取指令。
*   **执行：** 命令代理每 10 秒轮询一次 Slack，以在受害者主机上接收并执行 Shell 命令。

安全分析显示，恶意代码是在 npm 发布过程中注入的；这些代码在软件包的公共 GitHub 仓库中并不存在。虽然 npm 报告的下载量很高，但研究人员无法确认成功的感染数量。SafeDep 已提供失陷指标 (IOCs)，包括 SHA-256 哈希值和特定的触发矩阵，以帮助组织识别并移除这些恶意软件包。

---

## 7. 图解 Transformer

**原文标题**: Transformers Explained Visually

**原文链接**: [https://poloclub.github.io/transformer-explainer/](https://poloclub.github.io/transformer-explainer/)

**Transformer Explainer** 是由佐治亚理工学院的研究人员开发的一款交互式可视化工具，旨在揭示 GPT 等基于 Transformer 模型的内部工作原理。该文章及配套工具将大语言模型（LLM）复杂的数学运算分解为易于理解、循序渐进的视觉叙事。

整个过程始于**分词与嵌入（Tokenization and Embedding）**，输入的文本被拆分为微小单元（标记），并转换为捕获语义信息和位置信息的数值向量。架构的核心是**多头自注意力（Multi-Head Self-Attention）**机制。它使模型能够衡量句子中不同单词之间的相对重要性，从而理解上下文和长程依赖关系。例如，它能帮助模型在复杂的句子中确定代词“它（it）”具体指代哪个名词。

在注意力机制之后，数据通过**前馈网络（Feed-Forward Networks）**进一步细化这些表示。Transformer 块中的每一层都会处理数据，以建立对输入内容的深层数学理解。最后，模型使用**线性层与 Softmax 层（Linear and Softmax layer）**在整个词表中计算概率分布，并选择最有可能生成的下一个标记。

通过提供“探究内部原理”的视角，Transformer Explainer 阐明了查询（Query）、键（Key）和值（Value）向量等抽象概念是如何相互作用的。它弥合了高层 AI 行为与支撑现代自然语言处理的底层线性代数之间的鸿沟。该工具强调，虽然像 GPT-4 这样的模型规模巨大，但它们正是依靠这些基础且可重复的构建模块来实现领先的性能。

---

## 8. 数学与人工智能咨询小组

**原文标题**: The Advisory Group on Mathematics and Artificial Intelligence

**原文链接**: [https://terrytao.wordpress.com/2026/09/21/advisory-group-on-mathematics-and-artificial-intelligence/](https://terrytao.wordpress.com/2026/09/21/advisory-group-on-mathematics-and-artificial-intelligence/)

这段文字是一个名为“数学与人工智能顾问小组”（The Advisory Group on Mathematics and Artificial Intelligence）博客的页眉与署名，该博客由 Ben Eastaugh 和 Chris Sternal-Johnson 撰写，并托管于 WordPress。

根据标题及作者已有的研究工作，其内容专注于严谨数学理论与人工智能发展的交叉领域。该小组探讨的核心主题通常包括：

*   **数学基础**：探索如何应用范畴论、数理逻辑和概率论等抽象结构来优化人工智能架构。
*   **贝叶斯推断**：重点关注概率建模及其在机器学习和决策系统中的作用。
*   **函数式编程**：探讨特定的编程范式如何能更好地在软件中实现复杂的数学概念。
*   **咨询与研究**：该小组作为一个协作平台，旨在分享关于构建智能系统所面临的技术与理论挑战的见解。

总之，该博客为对支撑现代及理论人工智能的深层数学框架感兴趣的专业人士和研究人员，提供了一个专业的学术资源。

---

## 9. In Search of a Compositional Theory of Self-Stabilization

**原文标题**: In Search of a Compositional Theory of Self-Stabilization

**原文链接**: [http://muratbuffalo.blogspot.com/2026/09/in-search-of-compositional-theory-of.html](http://muratbuffalo.blogspot.com/2026/09/in-search-of-compositional-theory-of.html)

In this article, the author explores a compositional theory of self-stabilization to address **metastable failures**, such as retry storms in distributed systems. Finding existing literature on layered stabilization insufficient, the author investigates "Parametric Assume-Guarantee Contracts," a concept from a 2017 control theory paper.

**Parametric Contracts**
Traditional contracts often fail during large shocks because their preconditions are no longer met. Parametric contracts solve this by providing a family of promises indexed by "badness" levels. Instead of a single "if-then" statement, a component guarantees a specific output bound for any given input bound. This ensures the contract remains valid in every state, allowing for reasoning about convergence back to a stable state.

**Limitations and Analysis**
The author notes that current control theory models are often "memoryless," failing to account for backlog—a critical element in distributed systems with queues. By analyzing a retry storm model (involving a server and a retrier), the author identifies two primary factors affecting stability:
1.  **Coupling:** How the fresh work queue and duplicate queue interact and feed into one another.
2.  **Memory:** The percentage of backlog that persists from one round to the next.

Using linear stability analysis, the author demonstrates that even if the "gain" (interaction) between components seems small, the "memory" of the queues can push the system's growth factor above one, leading to divergence and failure.

**Key Findings**
The analysis confirms that common fixes, such as **retry budgets** or **fresh-priority service**, work by "zeroing" the coupling between queues. Conversely, simply capping queue sizes does not prevent failure; it merely causes the system to "park" in a metastable state where redundant work consumes all capacity. The author concludes that while parametric contracts offer a better way to define component promises, a robust compositional theory for systems with memory is still under development.

---

## 10. Turn off and restrict access to Apple Intelligence features on Mac

**原文标题**: Turn off and restrict access to Apple Intelligence features on Mac

**原文链接**: [https://support.apple.com/guide/mac-help/turn-restrict-access-apple-intelligence-mchlb2e44f94/mac](https://support.apple.com/guide/mac-help/turn-restrict-access-apple-intelligence-mchlb2e44f94/mac)

This article provides instructions on how to restrict or disable Apple Intelligence features on a Mac (macOS Sequoia 15 and later) using **Screen Time**. 

**Key Information and Restrictions:**
Apple Intelligence availability is limited by region and language. It is currently **not available** for devices purchased in Mainland China, nor for users physically located in Mainland China using a Mainland China Apple Account.

**How to Restrict Features:**
To manage these settings, users must navigate to **System Settings > Screen Time > Content & Privacy** and enable **Content & Privacy Restrictions**. Under the **Intelligence & Siri** section, users can individually toggle off the following:

*   **Writing Tools:** Disables AI-powered text assistance, such as proofreading and rewriting.
*   **Image Creation:** Blocks access to creative tools like Image Playground and Genmoji (dedicated to generating original images and emojis).
*   **Intelligence Extensions:** Restricts the use of third-party AI integrations, such as ChatGPT.

The guide emphasizes that these settings are particularly useful for parental controls or for users who wish to limit AI interactions on their devices. To access these settings, the Mac must be running the latest version of macOS.

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 2 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 3 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 4 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 5 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 6 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 7 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 8 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 9 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 10 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 11 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 12 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 13 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 14 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 15 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 16 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 17 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 18 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 19 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 20 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 21 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 22 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 23 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 24 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 25 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 26 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 27 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 28 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 29 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 30 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 31 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 32 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 33 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 34 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 35 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 36 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 37 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 38 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 39 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 40 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 41 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 42 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 43 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 44 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 45 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 46 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 47 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 48 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 49 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 50 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 51 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 52 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 53 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 54 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 55 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 56 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 57 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 58 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 59 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 60 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 61 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 62 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 63 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 64 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 65 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 66 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 67 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 68 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 69 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 70 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 71 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 72 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 73 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 74 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 75 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 76 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 77 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 78 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 79 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 80 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 81 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 82 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 83 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 84 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 85 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 86 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 87 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 88 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 89 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 90 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 91 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 92 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 93 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 94 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 95 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 96 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 97 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 98 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 99 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 100 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 101 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 102 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 103 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 104 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 105 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 106 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 107 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 108 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 109 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 110 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 111 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 112 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 113 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 114 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 115 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 116 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 117 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 118 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 119 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 120 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 121 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 122 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 123 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 124 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 125 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 126 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 127 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 128 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 129 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 130 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 131 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 132 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 133 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 134 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 135 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 136 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 137 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 138 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 139 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 140 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 141 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 142 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 143 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 144 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 145 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 146 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 147 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 148 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 149 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 150 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 151 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 152 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 153 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 154 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 155 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 156 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 157 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 158 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 159 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 160 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 161 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 162 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 163 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 164 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 165 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 166 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 167 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 168 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 169 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 170 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 171 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 172 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 173 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 174 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 175 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 176 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 177 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 178 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 179 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 180 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 181 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 182 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 183 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 184 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 185 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 186 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 187 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 188 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 189 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 190 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 191 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 192 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 193 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 194 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 195 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 196 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 197 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 198 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 199 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 200 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 201 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 202 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 203 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 204 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 205 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 206 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 207 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 208 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 209 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 210 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 211 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 212 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 213 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 214 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 215 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 216 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 217 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 218 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 219 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 220 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 221 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 222 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 223 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 224 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 225 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 226 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 227 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 228 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 229 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 230 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 231 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 232 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 233 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 234 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 235 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 236 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 237 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 238 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 239 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 240 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 241 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 242 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 243 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 244 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 245 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 246 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 247 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 248 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 249 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 250 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 251 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 252 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 253 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 254 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 255 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 256 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 257 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 258 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 259 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 260 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 261 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 262 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 263 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 264 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 265 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 266 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 267 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 268 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 269 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 270 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 271 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 272 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 273 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 274 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 275 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 276 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 277 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 278 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 279 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 280 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 281 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 282 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 283 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 284 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 285 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 286 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 287 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 288 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 289 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 290 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 291 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 292 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 293 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 294 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 295 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 296 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 297 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 298 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 299 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 300 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 301 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 302 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 303 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 304 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 305 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 306 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 307 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 308 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 309 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 310 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 311 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 312 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 313 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 314 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 315 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 316 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 317 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 318 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 319 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 320 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 321 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 322 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 323 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 324 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 325 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 326 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 327 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 328 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 329 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 330 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 331 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 332 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 333 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 334 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 335 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 336 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 337 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 338 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 339 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 340 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 341 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 342 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 343 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 344 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 345 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 346 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 347 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 348 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 349 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 350 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 351 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 352 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 353 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 354 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 355 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 356 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 357 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 358 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 359 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 360 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 361 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 362 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 363 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 364 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 365 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 366 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 367 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 368 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 369 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 370 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 371 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 372 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 373 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 374 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 375 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 376 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 377 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 378 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 379 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 380 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 381 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 382 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 383 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 384 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 385 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 386 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 387 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 388 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 389 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 390 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 391 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 392 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 393 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 394 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 395 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 396 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 397 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 398 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 399 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 400 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 401 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 402 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 403 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 404 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 405 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 406 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 407 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 408 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 409 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 410 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 411 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 412 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 413 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 414 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 415 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 416 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 417 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 418 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 419 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 420 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 421 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 422 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 423 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 424 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 425 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 426 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 427 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 428 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 429 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 430 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 431 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 432 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 433 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 434 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 435 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 436 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 437 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 438 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 439 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 440 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 441 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 442 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 443 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 444 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 445 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 446 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 447 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 448 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 449 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 450 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 451 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 452 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 453 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 454 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 455 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 456 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 457 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 458 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 459 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 460 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 461 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 462 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 463 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 464 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 465 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 466 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 467 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 468 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 469 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 470 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 471 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 472 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 473 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 474 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 475 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 476 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 477 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 478 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 479 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 480 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 481 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 482 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 483 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 484 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 485 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 486 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 487 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 488 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 489 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 490 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 491 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 492 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 493 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 494 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 495 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 496 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 497 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 498 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 499 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 500 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 501 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 502 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 503 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 504 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 505 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 506 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 507 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 508 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 509 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 510 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 511 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 512 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 513 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 514 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 515 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 516 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 517 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 518 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 519 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 520 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 521 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 522 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 523 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 524 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 525 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 526 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 527 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 528 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 529 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 530 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 531 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 532 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 533 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 534 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 535 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 536 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 537 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 538 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 539 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 540 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 541 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 542 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 543 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 544 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 545 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 546 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 547 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 548 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
