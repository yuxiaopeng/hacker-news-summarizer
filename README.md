# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-07-15.md)

*最后自动更新时间: 2026-07-15 18:32:40*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 2 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 3 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 4 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 5 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 6 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 7 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 8 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 9 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 10 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 11 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 12 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 13 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 14 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 15 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 16 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 17 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 18 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 19 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 20 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 21 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 22 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 23 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 24 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 25 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 26 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 27 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 28 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 29 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 30 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 31 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 32 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 33 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 34 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 35 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 36 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 37 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 38 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 39 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 40 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 41 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 42 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 43 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 44 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 45 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 46 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 47 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 48 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 49 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 50 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 51 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 52 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 53 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 54 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 55 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 56 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 57 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 58 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 59 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 60 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 61 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 62 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 63 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 64 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 65 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 66 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 67 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 68 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 69 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 70 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 71 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 72 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 73 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 74 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 75 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 76 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 77 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 78 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 79 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 80 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 81 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 82 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 83 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 84 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 85 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 86 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 87 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 88 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 89 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 90 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 91 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 92 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 93 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 94 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 95 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 96 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 97 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 98 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 99 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 100 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 101 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 102 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 103 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 104 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 105 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 106 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 107 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 108 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 109 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 110 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 111 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 112 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 113 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 114 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 115 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 116 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 117 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 118 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 119 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 120 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 121 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 122 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 123 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 124 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 125 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 126 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 127 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 128 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 129 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 130 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 131 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 132 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 133 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 134 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 135 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 136 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 137 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 138 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 139 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 140 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 141 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 142 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 143 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 144 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 145 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 146 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 147 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 148 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 149 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 150 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 151 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 152 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 153 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 154 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 155 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 156 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 157 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 158 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 159 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 160 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 161 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 162 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 163 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 164 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 165 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 166 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 167 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 168 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 169 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 170 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 171 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 172 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 173 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 174 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 175 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 176 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 177 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 178 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 179 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 180 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 181 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 182 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 183 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 184 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 185 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 186 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 187 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 188 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 189 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 190 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 191 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 192 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 193 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 194 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 195 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 196 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 197 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 198 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 199 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 200 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 201 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 202 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 203 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 204 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 205 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 206 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 207 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 208 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 209 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 210 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 211 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 212 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 213 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 214 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 215 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 216 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 217 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 218 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 219 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 220 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 221 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 222 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 223 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 224 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 225 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 226 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 227 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 228 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 229 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 230 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 231 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 232 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 233 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 234 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 235 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 236 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 237 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 238 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 239 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 240 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 241 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 242 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 243 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 244 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 245 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 246 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 247 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 248 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 249 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 250 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 251 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 252 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 253 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 254 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 255 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 256 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 257 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 258 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 259 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 260 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 261 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 262 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 263 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 264 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 265 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 266 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 267 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 268 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 269 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 270 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 271 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 272 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 273 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 274 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 275 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 276 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 277 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 278 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 279 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 280 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 281 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 282 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 283 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 284 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 285 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 286 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 287 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 288 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 289 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 290 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 291 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 292 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 293 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 294 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 295 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 296 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 297 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 298 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 299 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 300 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 301 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 302 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 303 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 304 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 305 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 306 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 307 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 308 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 309 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 310 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 311 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 312 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 313 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 314 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 315 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 316 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 317 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 318 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 319 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 320 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 321 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 322 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 323 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 324 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 325 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 326 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 327 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 328 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 329 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 330 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 331 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 332 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 333 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 334 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 335 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 336 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 337 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 338 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 339 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 340 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 341 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 342 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 343 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 344 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 345 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 346 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 347 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 348 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 349 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 350 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 351 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 352 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 353 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 354 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 355 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 356 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 357 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 358 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 359 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 360 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 361 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 362 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 363 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 364 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 365 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 366 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 367 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 368 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 369 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 370 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 371 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 372 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 373 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 374 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 375 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 376 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 377 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 378 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 379 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 380 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 381 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 382 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 383 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 384 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 385 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 386 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 387 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 388 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 389 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 390 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 391 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 392 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 393 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 394 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 395 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 396 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 397 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 398 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 399 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 400 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 401 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 402 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 403 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 404 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 405 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 406 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 407 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 408 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 409 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 410 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 411 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 412 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 413 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 414 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 415 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 416 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 417 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 418 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 419 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 420 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 421 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 422 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 423 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 424 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 425 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 426 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 427 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 428 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 429 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 430 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 431 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 432 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 433 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 434 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 435 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 436 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 437 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 438 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 439 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 440 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 441 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 442 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 443 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 444 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 445 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 446 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 447 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 448 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 449 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 450 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 451 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 452 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 453 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 454 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 455 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 456 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 457 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 458 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 459 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 460 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 461 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 462 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 463 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 464 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 465 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 466 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 467 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 468 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 469 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 470 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 471 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 472 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 473 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 474 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 475 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 476 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 477 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 478 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 479 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 480 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 481 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 482 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
