# Hacker News 热门文章摘要 (2026-07-15)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 在无 GPU 的 13 年前 Xeon 处理器上以 5 tokens/s 运行 Gemma 4 26B

**原文标题**: Running Gemma 4 26B at 5 tokens/sec on a 13-year-old Xeon with no GPU

**原文链接**: [https://www.neomindlabs.com/2026/06/08/running-gemma-4-26b-at-5-tokens-sec-on-a-13-year-old-xeon-with-no-gpu/](https://www.neomindlabs.com/2026/06/08/running-gemma-4-26b-at-5-tokens-sec-on-a-13-year-old-xeon-with-no-gpu/)

本文详细介绍了如何在一台有着 13 年机龄的 HP StoreVirtual 服务器上运行现代化的 260 亿参数语言模型（Gemma 4 MoE）。这台被戏称为“地下室盒子”的机器配备了两颗 2013 年代架构的 Ivy Bridge 至强（Xeon）处理器，且未搭载 GPU，却实现了约每秒 5.2 个 token 的不俗“阅读速度”。

主要的技术挑战在于，现代推理优化方案（特别是 **ik_llama.cpp** 分支）默认 CPU 支持 AVX2 和 FMA3 指令集。而旧款 Ivy Bridge CPU 仅支持 AVX1，这导致软件要么在编译时报错，要么因计算调度器静默跳过某些混合专家模型（MoE）数学运算，而产生“流畅的胡言乱语”。

为了填补这一技术鸿沟，作者利用（在该服务器上运行的）**Claude** 调试了 C++ 代码库。双方共同发现，未初始化的内存损坏了模型的隐藏状态。随后的补丁（PR #2138）实现了几项关键修复：
*   **标量回退 (Scalar Fallbacks)：** 将特定于 AVX2 的内核重写为可移植的标量循环。
*   **图重定向 (Graph Rerouting)：** 修改了图构建器，将仅限 AVX2 的融合 MoE 操作分解为独立的、兼容 AVX1 的数学函数。
*   **CI 维护：** 更新了存根（stubs）和头文件，使代码能在旧款芯片上编译。

作者总结道，“擅长 AI”不应仅仅意味着支付订阅费，还应包括敢于“打开引擎盖”去改造“报废”企业级硬件的技术热忱。通过这种方式，一台价值 300 美元的二手服务器就能成为付费 API 的可靠本地备选方案，或是处理无需支付 token 费用的慢速批处理任务的性价比工具。

---

## 2. Telegram数据中心之谜

**原文标题**: Mysteries of Telegram Data Centers

**原文链接**: [https://dev.moe/en/3025](https://dev.moe/en/3025)

《Telegram 数据中心之谜》一文调查了该即时通讯平台背后的物理基础设施。出于安全和隐私原因，Telegram 对此一直保持神秘，这是众所周知的。

作者解释说，Telegram 并不拥有整栋建筑，而是利用**托管服务 (colocation services)**，从 Equinix 和 Interxion 等全球主要供应商处租赁机架空间和网络容量。Telegram 的基础设施分为五个主要数据中心 (DC)，每个中心负责特定的地理区域：

*   **DC 1（美国）：** 位于弗吉尼亚州阿什本（或可能是迈阿密），服务于北美洲和南美洲。
*   **DC 2 和 4（荷兰）：** 位于阿姆斯特丹；这些是欧洲、北非和中东的主要枢纽。
*   **DC 3（新加坡）：** 服务于亚洲和大洋洲。
*   **DC 5（芬兰）：** 位于赫尔辛基，主要服务于俄罗斯及周边地区。

文章重点介绍了 Telegram 的 **MTProto 协议** 如何管理这些连接。当用户注册时，应用程序会根据其 IP 地址自动将其分配到最近的数据中心，以最大限度地降低延迟。如果用户旅行，系统可以将他们的数据迁移到更近的数据中心以维持性能。

此外，Telegram 使用自己的自治系统 (AS62041)，并在 Telegram Messenger LLP 和 Telegram FZ-LLC 等多个公司实体下注册 IP 段。作者总结道，这种分布式的、跨司法管辖区的架构是一种刻意为之的策略，旨在确保高可用性，并保护用户数据免受局部法律扣押或政治压力的影响，将这种“神秘感”作为一层运维安全保障。

---

## 3. Show HN: misa77 - 一款比 LZ4 解码快 2 倍（且压缩率更高）的编解码器

**原文标题**: Show HN: misa77 - a codec that decodes 2x faster than LZ4 (at better ratios)

**原文链接**: [https://github.com/welcome-to-the-sunny-side/misa77](https://github.com/welcome-to-the-sunny-side/misa77)

**misa77** 是一款新型基于 LZ 算法的编解码器（v0.2.0），专为“一次写入，多次读取”的应用场景设计。其核心卖点是极高的单线程解压吞吐量，在保持更优压缩比的同时，速度通常能达到 **LZ4 的两倍**。

### 核心特性与性能
*   **专注于解压**：它致力于在解压速度与压缩比之间达到帕累托最优。在 Silesia Corpus 语料库的基准测试中，其解压速度超过 5,000 MB/s，性能优于 LZ4、Zstd 和 Snappy 等竞争对手。
*   **压缩权衡**：为了实现极高的解码速度，misa77 的压缩速度明显慢于同类工具。它提供两个等级：**Level 0**（针对解码速度优化）和 **Level 1**（针对压缩比优化）。
*   **微架构优化**：该编解码器采用了一些实验性模式（如 `--yolo` 和 `--adaptive`），通过在压缩阶段投入额外的计算，生成在解压时对 CPU 微架构更“友好”的数据流。
*   **资源效率**：无论输入数据大小如何，它都保持恒定的内存占用（压缩时 ≤ 5 MB，解压时为 0 MB）。

### 技术规格
*   **环境要求**：需要 C++20 编译器和 64 位小端序系统。支持 x86-64（利用 AVX2/SSE2）和 ARM64 架构。
*   **项目状态**：目前处于实验阶段（v0.x.y）。一个关键的局限性是当前的解码器假定输入数据是有效的；无效输入会导致未定义行为。不过，版本 0.3.0 计划引入具有输入安全性的解码器。
*   **许可协议**：基于 MIT 许可证分发。

总而言之，对于需要最大化数据读取速度，且能够接受较慢的一次性压缩过程的开发者来说，misa77 是一个理想的选择。

---

## 4. 面向编程智能体的开源记忆，支持 SSH 同步

**原文标题**: Open-source memory for coding agents, synced over SSH

**原文链接**: [https://github.com/vshulcz/deja-vu/](https://github.com/vshulcz/deja-vu/)

**Deja** 是一个开源、零依赖的 Go 二进制工具，为 Claude Code、Codex 和 opencode 等编程智能体提供本地记忆层。虽然这些智能体生成的日志包含数 GB 的调试记录和设计决策，但这些数据通常难以检索。*Deja* 通过在本地索引现有的历史记录，让用户和智能体都能瞬间召回过去的解决方案。

**核心功能：**

*   **快速、溯源搜索：** 在 10 毫秒内完成对数 GB 历史记录的词法搜索。由于它索引的是现有的本地文件，因此可以召回安装该工具数月前的对话。
*   **智能体集成：** 利用模型上下文协议 (MCP)，智能体可以查询自身的记忆，以避免重复调试已知问题。`install --auto` 功能可在新会话开始时自动注入相关的历史上下文。
*   **隐私与安全：** 数据绝不离开本地。*Deja* 在索引时会自动脱敏敏感信息（如 API 密钥、JWT 和私钥），确保索引及导出的摘要保持安全。
*   **SSH 与文件夹同步：** 用户可以使用仅追加、幂等的同步方式，通过共享文件夹（如 Syncthing、iCloud）或直接通过 SSH 命令在机器之间迁移记忆。
*   **简单易用：** 不同于需要向量数据库或外部大语言模型的复杂“记忆平台”，*deja* 是一个无依赖的单一二进制文件。它采用高效的本地倒排索引，占用空间通常仅为原始语料库大小的 2.4%。

*deja* 支持 macOS、Linux 和 Windows，可通过 curl、Go、Homebrew 或 npm 安装。它填补了原始日志与可操作上下文之间的空白，确保智能体过去的工作成为永久、可搜索的资产。

---

## 5. Collection of Digital Clock Designs

**原文标题**: Collection of Digital Clock Designs

**原文链接**: [https://clocks.dev](https://clocks.dev)

生成摘要时出错

---

## 6. 《侏罗纪公园》电脑设备极尽详实解析

**原文标题**: Jurassic Park computers in excruciating detail

**原文链接**: [https://fabiensanglard.net/jurrasic_park_computers/index.html](https://fabiensanglard.net/jurrasic_park_computers/index.html)

Fabien Sanglard 的这篇文章对 1993 年电影《侏罗纪公园》中所呈现的计算硬件和软件进行了详尽的技术分析。为了向技术型观众展现高度的真实感，制片方使用了价值约 170 万美元（约合 2026 年的 400 万美元）的真实设备，这些设备主要租借自 **Silicon Graphics (SGI)** 和 **Apple**。

识别出的关键硬件包括：
*   **工作站：** Ray Arnold 使用的是 **SGI R4000 Indigo**，而 Dennis Nedry 则操作一台高端 **SGI IRIS Crimson** 和两台 **Macintosh Quadra 700**。
*   **超级计算机：** 背景中闪烁的红色塔架是五台 **Thinking Machines CM-5** “Connection Machines”，它们是当时世界上最强大的计算机。
*   **便携设备：** 电影早期出现了一台 **Apple Powerbook 100**，此外 Nedry 还使用了一台 **Motorola Envoy**，这是一款在电影拍摄多年后才正式发布的 PDA 原型机。
*   **外设：** 片场配备了高端 **SuperMatch 20-T** 特丽珑（Trinitron）显示器和用于存储的 **PLI Mini Array**。

在软件和特效方面，文章透露许多“交互式”屏幕实际上是伪造的。“实时”视频会议其实是一个 **Quicktime** 视频文件，动画则是由专门的图形团队从相邻的隐蔽房间传输到片场显示器上的。然而，那个著名的 “Unix 系统”界面确实是一个名为 **fsn** 的 SGI 实验性 3D 文件管理器。

文章强调了制片方对细节的极致追求，指出屏幕上可以看到真实的 **Pascal 代码**，且书架上还摆放了《System 7 Revealed》等技术书籍，以增强 “Nedryland” 工作站的真实性。

---

## 7. Launch HN：Coasty (YC S26) – 面向计算机操作智能体的 API

**原文标题**: Launch HN: Coasty (YC S26) – An API for computer-use agents

**原文链接**: [https://coasty.ai/docs](https://coasty.ai/docs)

Coasty (YC S26) is an API platform designed for building and deploying "computer-use" agents that can autonomously operate managed Linux and Windows machines. It provides developers with the infrastructure to automate tasks involving browsers, terminals, and file systems through natural language goals.

The platform offers three levels of abstraction:
1.  **Task Runs:** The default entry point where an agent autonomously drives toward a single goal, executes actions, and verifies its own work.
2.  **Workflows:** A higher-level system for complex automations involving multiple tasks, branching logic, loops, and human approvals.
3.  **Prediction Primitives:** Low-level, stateless endpoints (predict, ground, parse) for developers who want to own the control loop and manage screenshots and actions manually.

**Key Technical Features:**
*   **Human-in-the-Loop:** Agents can detect obstacles like CAPTCHAs or 2FA and pause execution. Developers can then resume the task once a human has completed the blocking step.
*   **Real-time Monitoring:** Supports Server-Sent Events (SSE) for live streaming of the agent's reasoning and actions, as well as HMAC-signed webhooks for lifecycle notifications.
*   **Reliability:** Includes idempotency keys to prevent duplicate runs and a "test key" mode that uses mock VMs for CI/CD and local development without incurring costs.
*   **Pricing:** Coasty operates on a usage-based model, generally charging $0.05 per completed agent step ($0.08 for legacy engines), billed from a USD wallet.

By providing managed execution environments and high-level autonomous loops, Coasty aims to simplify the process of building AI assistants that can perform complex, multi-step operations directly on a computer interface.

---

## 8. Artie (YC S23) 招聘软件工程师

**原文标题**: Artie (YC S23) Is Hiring Software Engineers

**原文链接**: [https://jobs.ashbyhq.com/artie](https://jobs.ashbyhq.com/artie)

关于 **Artie (YC S23) 招聘软件工程师** 的内容不包含具体的职位描述或公司详情，因为源内容需要启用 JavaScript 才能加载。

不过，目前可获取的关键信息如下：

*   **招聘状态：** Artie 目前正在招聘软件工程师职位。
*   **公司背景：** Artie 是一家来自 Y Combinator 2023 年夏季（S23）批次的初创公司。
*   **技术

如需获取这些职位的详细信息，感兴趣的候选人需要使用标准网络浏览器直接访问 Artie 的招聘门户网站。

---

## 9. Sleep regularity is a stronger predictor of mortality risk than sleep duration (2023)

**原文标题**: Sleep regularity is a stronger predictor of mortality risk than sleep duration (2023)

**原文链接**: [https://academic.oup.com/sleep/article/47/1/zsad253/7280269](https://academic.oup.com/sleep/article/47/1/zsad253/7280269)

生成摘要时出错

---

## 10. Towards a Harness That Can Do Anything

**原文标题**: Towards a Harness That Can Do Anything

**原文链接**: [https://eardatasci.github.io/c/ambiance/index.html](https://eardatasci.github.io/c/ambiance/index.html)

生成摘要时出错

---

## 11. My midlife crisis Corolla is fast, furious, and modded

**原文标题**: My midlife crisis Corolla is fast, furious, and modded

**原文链接**: [https://www.zocalopublicsquare.org/my-midlife-crisis-corolla-fast-furious-fully-modded/](https://www.zocalopublicsquare.org/my-midlife-crisis-corolla-fast-furious-fully-modded/)

生成摘要时出错

---

## 12. Prioritize mental health, and why communication is so important

**原文标题**: Prioritize mental health, and why communication is so important

**原文链接**: [https://ramones.dev/posts/mental-health/](https://ramones.dev/posts/mental-health/)

生成摘要时出错

---

## 13. A General Goal-Conditioned Minecraft Model

**原文标题**: A General Goal-Conditioned Minecraft Model

**原文链接**: [https://pantograph.com/journal/pan-1](https://pantograph.com/journal/pan-1)

生成摘要时出错

---

## 14. The Memory Heist

**原文标题**: The Memory Heist

**原文链接**: [https://www.ayush.digital/blog/the-memory-heist](https://www.ayush.digital/blog/the-memory-heist)

生成摘要时出错

---

## 15. When A.I. Is a Member of the Family

**原文标题**: When A.I. Is a Member of the Family

**原文链接**: [https://www.newyorker.com/magazine/2026/07/20/when-ai-is-a-member-of-the-family](https://www.newyorker.com/magazine/2026/07/20/when-ai-is-a-member-of-the-family)

生成摘要时出错

---

## 16. Unsolved Problems in MLOps

**原文标题**: Unsolved Problems in MLOps

**原文链接**: [https://spawn-queue.acm.org/doi/pdf/10.1145/3762989](https://spawn-queue.acm.org/doi/pdf/10.1145/3762989)

生成摘要时出错

---

## 17. The well-calibrated Bayesian [pdf] (1982)

**原文标题**: The well-calibrated Bayesian [pdf] (1982)

**原文链接**: [https://fitelson.org/seminar/dawid.pdf](https://fitelson.org/seminar/dawid.pdf)

生成摘要时出错

---

## 18. The Three-Second Theft: Why AI Voice Fraud Outruns Every Defence

**原文标题**: The Three-Second Theft: Why AI Voice Fraud Outruns Every Defence

**原文链接**: [https://smarterarticles.co.uk/the-three-second-theft-why-ai-voice-fraud-outruns-every-defence](https://smarterarticles.co.uk/the-three-second-theft-why-ai-voice-fraud-outruns-every-defence)

生成摘要时出错

---

## 19. OpenAI loses trademark dispute at EU court

**原文标题**: OpenAI loses trademark dispute at EU court

**原文链接**: [https://dpa-international.com/economics/urn:newsml:dpa.com:20090101:260715-930-389143/](https://dpa-international.com/economics/urn:newsml:dpa.com:20090101:260715-930-389143/)

生成摘要时出错

---

## 20. Today I Rescued 7,234 Old GIFs

**原文标题**: Today I Rescued 7,234 Old GIFs

**原文链接**: [https://danq.me/2026/07/10/rescuing-7234-gifs/](https://danq.me/2026/07/10/rescuing-7234-gifs/)

生成摘要时出错

---

## 21. The Conservationist Who Turned 40 Terabytes of Public Data into a Video Game

**原文标题**: The Conservationist Who Turned 40 Terabytes of Public Data into a Video Game

**原文链接**: [https://blog.exe.dev/meet-the-conservationist-who-turned-40-terabytes-of-government-data-into-a-video-game](https://blog.exe.dev/meet-the-conservationist-who-turned-40-terabytes-of-government-data-into-a-video-game)

生成摘要时出错

---

## 22. Weathergotchi – an open-source climate Tamagotchi

**原文标题**: Weathergotchi – an open-source climate Tamagotchi

**原文链接**: [https://github.com/Michael-Manning/E-Paper-Climate-Logger](https://github.com/Michael-Manning/E-Paper-Climate-Logger)

生成摘要时出错

---

## 23. What designing 54 computer science cards taught me about graphic design

**原文标题**: What designing 54 computer science cards taught me about graphic design

**原文链接**: [https://fhoehl.com/designing-algodeck](https://fhoehl.com/designing-algodeck)

生成摘要时出错

---

## 24. SpaceX bond worth 10% less than issue price – heading for junk bond status

**原文标题**: SpaceX bond worth 10% less than issue price – heading for junk bond status

**原文链接**: [https://www.ft.com/content/3a023b95-66c3-41e1-b0ce-df752a499541](https://www.ft.com/content/3a023b95-66c3-41e1-b0ce-df752a499541)

生成摘要时出错

---

## 25. DEA to Temporarily Schedule 7-Oh and Related Substances to Protect Public Safety

**原文标题**: DEA to Temporarily Schedule 7-Oh and Related Substances to Protect Public Safety

**原文链接**: [https://www.dea.gov/press-releases/2026/07/01/dea-temporarily-schedule-7-oh-and-related-substances-protect-public](https://www.dea.gov/press-releases/2026/07/01/dea-temporarily-schedule-7-oh-and-related-substances-protect-public)

生成摘要时出错

---

## 26. What Every Python Developer Should Know About the CPython ABI

**原文标题**: What Every Python Developer Should Know About the CPython ABI

**原文链接**: [https://labs.quansight.org/blog/python-abi-abi3t](https://labs.quansight.org/blog/python-abi-abi3t)

生成摘要时出错

---

## 27. FreeBSD 16 Retires the Last of Its GPL Code from Its Base System

**原文标题**: FreeBSD 16 Retires the Last of Its GPL Code from Its Base System

**原文链接**: [https://www.phoronix.com/news/FreeBSD-16-Goes-GPL-Free](https://www.phoronix.com/news/FreeBSD-16-Goes-GPL-Free)

生成摘要时出错

---

## 28. Briar Is in Maintenance Mode

**原文标题**: Briar Is in Maintenance Mode

**原文链接**: [https://briarproject.org/news/2026-maintenance-mode/](https://briarproject.org/news/2026-maintenance-mode/)

生成摘要时出错

---

## 29. Show HN: 18KB ls alternative in no_std rust and Libc

**原文标题**: Show HN: 18KB ls alternative in no_std rust and Libc

**原文链接**: [https://crates.io/crates/fli-tool](https://crates.io/crates/fli-tool)

生成摘要时出错

---

## 30. What's the most popular number in Hacker News titles?

**原文标题**: What's the most popular number in Hacker News titles?

**原文链接**: [https://blog.omgmog.net/post/most-popular-numbers-in-hn-post-titles/](https://blog.omgmog.net/post/most-popular-numbers-in-hn-post-titles/)

生成摘要时出错

---

## 31. Germany maybe found a new source of renewable energy

**原文标题**: Germany maybe found a new source of renewable energy

**原文链接**: [https://www.schweizerbart.de/papers/zdgg/detail/prepub/108503/Geological_and_geophysical_characterisation_of_the_exploration_boreholes_EB1_and_EB2_Inde_Syncline_Rhenohercynian_Fold_and_Thrust_Belt_and_Weisweiler_Horst_Lower_Rhine_Embayment_Germany](https://www.schweizerbart.de/papers/zdgg/detail/prepub/108503/Geological_and_geophysical_characterisation_of_the_exploration_boreholes_EB1_and_EB2_Inde_Syncline_Rhenohercynian_Fold_and_Thrust_Belt_and_Weisweiler_Horst_Lower_Rhine_Embayment_Germany)

生成摘要时出错

---

## 32. Bootstrapping GDC with DMD

**原文标题**: Bootstrapping GDC with DMD

**原文链接**: [https://briancallahan.net/blog/20260713.html](https://briancallahan.net/blog/20260713.html)

生成摘要时出错

---

## 33. SendLang: A DSL for Email Automation

**原文标题**: SendLang: A DSL for Email Automation

**原文链接**: [https://www.sendlang.com](https://www.sendlang.com)

生成摘要时出错

---

## 34. Richard Feynman and the Connection Machine (1989)

**原文标题**: Richard Feynman and the Connection Machine (1989)

**原文链接**: [https://longnow.org/ideas/richard-feynman-and-the-connection-machine/](https://longnow.org/ideas/richard-feynman-and-the-connection-machine/)

生成摘要时出错

---

## 35. Using Go for Mobile Apps

**原文标题**: Using Go for Mobile Apps

**原文链接**: [https://www.davidsobsessions.com/p/one-year-of-gomobile/](https://www.davidsobsessions.com/p/one-year-of-gomobile/)

生成摘要时出错

---

## 36. Telegram Serverless

**原文标题**: Telegram Serverless

**原文链接**: [https://core.telegram.org/bots/serverless](https://core.telegram.org/bots/serverless)

生成摘要时出错

---

## 37. Nat Slipstreaming v2.0 allows an attacker to remotely access any TCP/UDP service

**原文标题**: Nat Slipstreaming v2.0 allows an attacker to remotely access any TCP/UDP service

**原文链接**: [https://sa.my/slipstream/](https://sa.my/slipstream/)

生成摘要时出错

---

## 38. The age of the Universe from a large sample of the oldest Galactic stars

**原文标题**: The age of the Universe from a large sample of the oldest Galactic stars

**原文链接**: [https://arxiv.org/abs/2607.00764](https://arxiv.org/abs/2607.00764)

生成摘要时出错

---

## 39. Latent Space as a New Medium

**原文标题**: Latent Space as a New Medium

**原文链接**: [https://kevinkelly.substack.com/p/latent-space-as-a-new-medium](https://kevinkelly.substack.com/p/latent-space-as-a-new-medium)

生成摘要时出错

---

## 40. C3 0.8.2 a Modest Improvement

**原文标题**: C3 0.8.2 a Modest Improvement

**原文链接**: [https://c3-lang.org/blog/0_8_2_a_modest_improvement/](https://c3-lang.org/blog/0_8_2_a_modest_improvement/)

生成摘要时出错

---

## 41. A Trip to 90s Kansai: Exploring the XD FirstClass Network BBS

**原文标题**: A Trip to 90s Kansai: Exploring the XD FirstClass Network BBS

**原文链接**: [https://cdrom.ca/games/2026/05/30/xd.html](https://cdrom.ca/games/2026/05/30/xd.html)

生成摘要时出错

---

## 42. SpaceX stock sinks below $135 IPO price for the first time

**原文标题**: SpaceX stock sinks below $135 IPO price for the first time

**原文链接**: [https://www.cnbc.com/2026/07/15/spacex-spcx-stock-ipo-price.html](https://www.cnbc.com/2026/07/15/spacex-spcx-stock-ipo-price.html)

生成摘要时出错

---

## 43. Microsoft Confirms Windows GDID Device Identifier That Cannot Be Disabled

**原文标题**: Microsoft Confirms Windows GDID Device Identifier That Cannot Be Disabled

**原文链接**: [https://www.ghacks.net/2026/07/12/microsoft-confirms-windows-gdid-device-identifier-that-cannot-be-disabled-documented-in-fbi-case-filing/](https://www.ghacks.net/2026/07/12/microsoft-confirms-windows-gdid-device-identifier-that-cannot-be-disabled-documented-in-fbi-case-filing/)

生成摘要时出错

---

## 44. Museum of the Human Web

**原文标题**: Museum of the Human Web

**原文链接**: [https://museum.parallel.ai/introduction?era=modern](https://museum.parallel.ai/introduction?era=modern)

生成摘要时出错

---

## 45. Treating generic drugs as something special can wreck affordability

**原文标题**: Treating generic drugs as something special can wreck affordability

**原文链接**: [https://www.46brooklyn.com/research/wrecklimid-how-treating-generic-drugs-as-something-special-can-wreck-affordability-jfmve](https://www.46brooklyn.com/research/wrecklimid-how-treating-generic-drugs-as-something-special-can-wreck-affordability-jfmve)

生成摘要时出错

---

## 46. Codex Micro

**原文标题**: Codex Micro

**原文链接**: [https://openai.com/supply/co-lab/work-louder/](https://openai.com/supply/co-lab/work-louder/)

生成摘要时出错

---

## 47. Microsoft has released software updates to plug at least 570 security holes

**原文标题**: Microsoft has released software updates to plug at least 570 security holes

**原文链接**: [https://krebsonsecurity.com/2026/07/microsoft-patches-a-record-570-security-flaws/](https://krebsonsecurity.com/2026/07/microsoft-patches-a-record-570-security-flaws/)

生成摘要时出错

---

## 48. Who's running all those tiny RPKI servers?

**原文标题**: Who's running all those tiny RPKI servers?

**原文链接**: [https://blog.apnic.net/2026/07/15/whos-running-all-those-tiny-rpki-servers/](https://blog.apnic.net/2026/07/15/whos-running-all-those-tiny-rpki-servers/)

生成摘要时出错

---

## 49. CVE-2026-59208: Cross-Issuer Account Takeover in n8n

**原文标题**: CVE-2026-59208: Cross-Issuer Account Takeover in n8n

**原文链接**: [https://www.strix.ai/blog/n8n-cross-issuer-account-takeover](https://www.strix.ai/blog/n8n-cross-issuer-account-takeover)

生成摘要时出错

---

## 50. The kids with phones are alright

**原文标题**: The kids with phones are alright

**原文链接**: [https://heatherburns.tech/2026/07/08/the-kids-with-phones-are-alright/](https://heatherburns.tech/2026/07/08/the-kids-with-phones-are-alright/)

生成摘要时出错

---

## 51. OnePlus to Pull Out of American and European Markets

**原文标题**: OnePlus to Pull Out of American and European Markets

**原文链接**: [https://www.macrumors.com/2026/07/15/report-oneplus-to-pull-out-of-us-and-europe/](https://www.macrumors.com/2026/07/15/report-oneplus-to-pull-out-of-us-and-europe/)

生成摘要时出错

---

## 52. Show HN: Aict – Unix coreutils that output XML/JSON, built for AI agents

**原文标题**: Show HN: Aict – Unix coreutils that output XML/JSON, built for AI agents

**原文链接**: [https://github.com/synseqack/aict](https://github.com/synseqack/aict)

生成摘要时出错

---

## 53. Microsoft Entra ID Will Retire SMS and Voice Authentication

**原文标题**: Microsoft Entra ID Will Retire SMS and Voice Authentication

**原文链接**: [https://lazyadmin.nl/office-365/microsoft-entra-entra-sms-voice-retirement/](https://lazyadmin.nl/office-365/microsoft-entra-entra-sms-voice-retirement/)

生成摘要时出错

---

## 54. I tricked Claude into leaking your deepest, darkest secrets

**原文标题**: I tricked Claude into leaking your deepest, darkest secrets

**原文链接**: [https://www.ayush.digital/blog/the-memory-heist](https://www.ayush.digital/blog/the-memory-heist)

生成摘要时出错

---

## 55. Bonsai 27B: A 27B-Class model that runs on a phone

**原文标题**: Bonsai 27B: A 27B-Class model that runs on a phone

**原文链接**: [https://prismml.com/news/bonsai-27b](https://prismml.com/news/bonsai-27b)

生成摘要时出错

---

## 56. AI Lays Bare the Authoritarianism of Modern Work. Time to Rethink Education

**原文标题**: AI Lays Bare the Authoritarianism of Modern Work. Time to Rethink Education

**原文链接**: [https://www.techpolicy.press/ai-lays-bare-the-authoritarianism-of-modern-work-time-to-rethink-education/](https://www.techpolicy.press/ai-lays-bare-the-authoritarianism-of-modern-work-time-to-rethink-education/)

生成摘要时出错

---

## 57. Andon (manufacturing)

**原文标题**: Andon (manufacturing)

**原文链接**: [https://en.wikipedia.org/wiki/Andon_(manufacturing)](https://en.wikipedia.org/wiki/Andon_(manufacturing))

生成摘要时出错

---

## 58. Vancouver PD website features Quick Escape button that wipes itself from history

**原文标题**: Vancouver PD website features Quick Escape button that wipes itself from history

**原文链接**: [https://vpd.ca/](https://vpd.ca/)

生成摘要时出错

---

## 59. Vancouver PD website features Quick Escape button that wipes itself from history

**原文标题**: Vancouver PD website features Quick Escape button that wipes itself from history

**原文链接**: [https://vpd.ca/](https://vpd.ca/)

生成摘要时出错

---

## 60. LeMario: Training a JEPA World Model on Super Mario Bros

**原文标题**: LeMario: Training a JEPA World Model on Super Mario Bros

**原文链接**: [https://www.benjamin-bai.com/projects/lemario](https://www.benjamin-bai.com/projects/lemario)

生成摘要时出错

---

## 61. The bread paradox: why convenience always wins, and why SaaS isn't doomed

**原文标题**: The bread paradox: why convenience always wins, and why SaaS isn't doomed

**原文链接**: [https://www.joanwestenberg.com/p/the-bread-paradox-why-convenience](https://www.joanwestenberg.com/p/the-bread-paradox-why-convenience)

生成摘要时出错

---

## 62. Boss – Dependency Manager for Delphi and Lazarus

**原文标题**: Boss – Dependency Manager for Delphi and Lazarus

**原文链接**: [https://github.com/HashLoad/boss](https://github.com/HashLoad/boss)

生成摘要时出错

---

## 63. We compiled our TypeScript parser to WASM

**原文标题**: We compiled our TypeScript parser to WASM

**原文链接**: [https://encore.dev/blog/typescript-parser-wasm](https://encore.dev/blog/typescript-parser-wasm)

生成摘要时出错

---

## 64. The form asked my permission to share my health data. It wouldn't let me say no

**原文标题**: The form asked my permission to share my health data. It wouldn't let me say no

**原文链接**: [https://themarkup.org/privacy/2026/05/27/opt-out-dark-patterns](https://themarkup.org/privacy/2026/05/27/opt-out-dark-patterns)

生成摘要时出错

---

## 65. Launch HN: Agnost AI (YC S26) – Extract user feedback from agent conversations

**原文标题**: Launch HN: Agnost AI (YC S26) – Extract user feedback from agent conversations

**原文链接**: [https://agnost.ai](https://agnost.ai)

生成摘要时出错

---

## 66. Show HN: Leet Robotics: Learn robotics and ROS2 with hands-on courses

**原文标题**: Show HN: Leet Robotics: Learn robotics and ROS2 with hands-on courses

**原文链接**: [https://www.leetrobotics.com](https://www.leetrobotics.com)

生成摘要时出错

---

## 67. Combinatorial Games in Lean

**原文标题**: Combinatorial Games in Lean

**原文链接**: [https://github.com/vihdzp/combinatorial-games](https://github.com/vihdzp/combinatorial-games)

生成摘要时出错

---

## 68. German Court Orders Deletion of Footage Exposing Pig Gas Chambers

**原文标题**: German Court Orders Deletion of Footage Exposing Pig Gas Chambers

**原文链接**: [https://veganhorizon.substack.com/p/punished-for-exposing-the-truth](https://veganhorizon.substack.com/p/punished-for-exposing-the-truth)

生成摘要时出错

---

## 69. Ignoring OS files (like .DS_Store) in Git inside dev containers

**原文标题**: Ignoring OS files (like .DS_Store) in Git inside dev containers

**原文链接**: [https://answers.abstractbrain.com/global-gitignore-not-working-in-devcontainers](https://answers.abstractbrain.com/global-gitignore-not-working-in-devcontainers)

生成摘要时出错

---

## 70. Your 'app' could have been a webpage (so I fixed it for you)

**原文标题**: Your 'app' could have been a webpage (so I fixed it for you)

**原文链接**: [https://danq.me/2026/07/09/your-app-could-have-been-a-webpage/](https://danq.me/2026/07/09/your-app-could-have-been-a-webpage/)

生成摘要时出错

---

## 71. Mathematical texts from a Maya site in Guatemala identify an ancient astronomer

**原文标题**: Mathematical texts from a Maya site in Guatemala identify an ancient astronomer

**原文链接**: [https://www.nature.com/articles/d41586-026-02170-8](https://www.nature.com/articles/d41586-026-02170-8)

生成摘要时出错

---

## 72. German AI consortium releases Soofi S, an open 30B model

**原文标题**: German AI consortium releases Soofi S, an open 30B model

**原文链接**: [https://the-decoder.com/german-ai-consortium-releases-soofi-s-an-open-30b-model-that-tops-benchmarks-in-both-english-and-german/](https://the-decoder.com/german-ai-consortium-releases-soofi-s-an-open-30b-model-that-tops-benchmarks-in-both-english-and-german/)

生成摘要时出错

---

## 73. TS-2026-009: Insecure argument handling in Tailscale SSH permitted root access

**原文标题**: TS-2026-009: Insecure argument handling in Tailscale SSH permitted root access

**原文链接**: [https://tailscale.com/security-bulletins](https://tailscale.com/security-bulletins)

生成摘要时出错

---

## 74. Probably check on your smart appliances

**原文标题**: Probably check on your smart appliances

**原文链接**: [https://xeiaso.net/notes/2026/check-your-smart-tv/](https://xeiaso.net/notes/2026/check-your-smart-tv/)

生成摘要时出错

---

## 75. Surprising lessons from my research scientist job search

**原文标题**: Surprising lessons from my research scientist job search

**原文链接**: [https://yongzx.github.io/blog/2026/06/24/job-search/](https://yongzx.github.io/blog/2026/06/24/job-search/)

生成摘要时出错

---

## 76. DSLs Enable Reliable Use of LLMs

**原文标题**: DSLs Enable Reliable Use of LLMs

**原文链接**: [https://martinfowler.com/articles/llm-and-dsls.html](https://martinfowler.com/articles/llm-and-dsls.html)

生成摘要时出错

---

## 77. How I Turned AI to the Dark Side

**原文标题**: How I Turned AI to the Dark Side

**原文链接**: [https://spectrum.ieee.org/jailbreaking-llms](https://spectrum.ieee.org/jailbreaking-llms)

生成摘要时出错

---

## 78. Show HN: StyleSeed – a design-rules engine so AI agents stop building generic UI

**原文标题**: Show HN: StyleSeed – a design-rules engine so AI agents stop building generic UI

**原文链接**: [https://github.com/bitjaru/styleseed](https://github.com/bitjaru/styleseed)

生成摘要时出错

---

## 79. Australian energy retailers must offer three hours of free daytime electricity

**原文标题**: Australian energy retailers must offer three hours of free daytime electricity

**原文链接**: [https://lenergy.com.au/free-daytime-electricity-is-coming-heres-how-it-actually-works/](https://lenergy.com.au/free-daytime-electricity-is-coming-heres-how-it-actually-works/)

生成摘要时出错

---

## 80. Kilo Code has been acquired by Anaconda

**原文标题**: Kilo Code has been acquired by Anaconda

**原文链接**: [https://twitter.com/kilocode/status/2077394060248076699](https://twitter.com/kilocode/status/2077394060248076699)

生成摘要时出错

---

## 81. The Tower Keeps Rising

**原文标题**: The Tower Keeps Rising

**原文链接**: [https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising/](https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising/)

生成摘要时出错

---

## 82. Tutorial: Algebraic Foundations Powering FlashAttention

**原文标题**: Tutorial: Algebraic Foundations Powering FlashAttention

**原文链接**: [https://riftstack.ai/research/learning-flashattention-the-hard-way-part-1](https://riftstack.ai/research/learning-flashattention-the-hard-way-part-1)

生成摘要时出错

---

## 83. The Estranged Worlds of J. G. Ballard

**原文标题**: The Estranged Worlds of J. G. Ballard

**原文链接**: [https://lareviewofbooks.org/article/jg-ballard-illuminated-man-christopher-priest-nina-allan/](https://lareviewofbooks.org/article/jg-ballard-illuminated-man-christopher-priest-nina-allan/)

生成摘要时出错

---

## 84. Are we offloading too much of our thinking to AI?

**原文标题**: Are we offloading too much of our thinking to AI?

**原文链接**: [https://www.artfish.ai/p/offloading-thinking-to-ai](https://www.artfish.ai/p/offloading-thinking-to-ai)

生成摘要时出错

---

## 85. Making My Rust Program Space-Flight Ready

**原文标题**: Making My Rust Program Space-Flight Ready

**原文链接**: [https://w4g1.dev/blog/making-my-rust-program-space-flight-ready](https://w4g1.dev/blog/making-my-rust-program-space-flight-ready)

生成摘要时出错

---

## 86. Punch yourself in the face with reality

**原文标题**: Punch yourself in the face with reality

**原文链接**: [https://adi.bio/reality](https://adi.bio/reality)

生成摘要时出错

---

## 87. Show HN: Production-grade LangGraph template

**原文标题**: Show HN: Production-grade LangGraph template

**原文链接**: [https://github.com/brescou/langgraph-agent-stack](https://github.com/brescou/langgraph-agent-stack)

生成摘要时出错

---

## 88. Show HN: Fast NF4 dequantization Triton kernel (1.41x faster than bitsandbytes)

**原文标题**: Show HN: Fast NF4 dequantization Triton kernel (1.41x faster than bitsandbytes)

**原文链接**: [https://github.com/Griffith-7/nf4-triton-kernel](https://github.com/Griffith-7/nf4-triton-kernel)

生成摘要时出错

---

