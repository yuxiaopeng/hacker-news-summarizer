# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-10-19.md)

*最后自动更新时间: 2026-10-19 21:45:40*
## 1. MiniMax M3.1 极速版

**原文标题**: MiniMax M3.1 Flash

**原文链接**: [https://www.minimax.io/blog/minimax-m31f](https://www.minimax.io/blog/minimax-m31f)

MiniMax 正式发布了新一代模型 MiniMax M3.1 Flash，该模型此前的匿名代号为“Space Bunny”。此次发布标志着在平衡效率与高水平智能方面取得了重大进展，特别针对智能体任务、编程、计算机操作及网络安全等领域。

**核心性能提升：**
M3.1 Flash 在能力上实现了代际跨越，同时推理速度提升了近三倍，输出速度突破每秒 200 token (TPS)。此外，其使用成本较前代降低了 70%，定价为每 100 万输入 token 0.15 美元，每 100 万输出 token 0.60 美元。

**核心能力与基准测试：**
*   **智能体任务与自动化：** 在复杂 SaaS 工作流 (AutomationBench-AA) 和金融多步规划 (BankerToolBench) 测试中，该模型表现均位列前茅。
*   **编程：** 在 DeepSWE v1.1 中得分 73.7%，展现了独立理解代码、开发功能和验证软件任务的能力。
*   **计算机操作：** 目前在 OSWorld V2 和 Agents’ Last Exam (ALE) 榜单中位列中国模型第一，彰显了其在真实桌面环境导航方面的卓越能力。
*   **网络安全：** 在 CyberGym 测试中获得 82 分，擅长漏洞发现、渗透测试和恶意软件分析。

**获取方式：**
M3.1 Flash 现已通过 MiniMax API、M Plan 和 MiniMax Code 上线。虽然模型权重将于稍后发布，但公司同时宣布，性能更强大的“Pro”版本正在开发中，将进一步挑战 AI 智能的极限。

---

## 2. 我只用一个电机造了一台无人机 [视频]

**原文标题**: I built a drone with only one motor [video]

**原文链接**: [https://www.youtube.com/watch?v=Ndftcft6XhU](https://www.youtube.com/watch?v=Ndftcft6XhU)

根据提供的标题，以下是内容的简要总结：

**总结：构建单电机无人机**

本视频展示的项目是一项重大的工程挑战：仅使用一个电机构建一台功能性无人机，这与标准的四电机（四旋翼）设计形成了鲜明对比。

**关键信息：**
*   **工程突破：** 传统无人机依靠改变多个旋翼的速度来实现稳定和方向控制。单电机设计必须寻找替代方案来抵消扭矩并管理飞行矢量。
*   **设计力学：** 为了实现单电机飞行，该无人机可能采用了“翅果”设计（模仿飘落的枫树种子）或一套气动叶片与舵机系统。这些组件通过重新引导单个螺旋桨产生的气流，来控制俯仰、横滚和偏航。
*   **技术成就：** 该项目突显了增稳的复杂性。在没有差速推力优势的情况下，无人机需要精确的重量分配和对控制面的高速调整，才能维持悬停或进行定向移动。
*   **性能权衡：** 虽然单电机无人机在动力效率和机械独特性上可能更具优势，但与传统的多旋翼飞行器相比，它的操控和增稳通常要困难得多。

*注：提供的文本内容主要由 YouTube 的法律页脚和 2026 年版权信息组成；因此，本总结重点关注标题中所描述的技术成就。*

---

## 3. Wine 移植到 OpenBSD

**原文标题**: Wine ported to OpenBSD

**原文链接**: [https://marc.info/?l=openbsd-ports&m=179236125692175](https://marc.info/?l=openbsd-ports&m=179236125692175)

Thomas Frohwein 宣布了 OpenBSD 版 Wine 的全新移植，这是与开发者 Andrii 和 Fabien 协作取得的重大里程碑。这一突破通过软件方案模拟 `%gs` 前缀，绕过了该平台无法设置 `gsbase` 的限制。

该移植版主要面向 **64 位 Windows 软件**，反映了现代 Windows 应用开发的趋势。已有数十款应用测试成功，包括《巫师 3》重制版（使用 `vkd3d-proton`）等对图形性能要求较高的作品。然而，目前仍存在一个主要限制：**暂不支持 32 位 Windows 软件 (WoW64)**，且无法运行。

尽管实际测试反馈积极，但由于内置的 Wine 测试需要 X 服务器访问权限且容易导致挂起，目前已被禁用。对于初步测试，开发者建议使用 64 位便携版的 Notepad++。

在安全性方面，Frohwein 建议用户以**非特权用户**身份运行 Wine，并自行承担风险。开发团队正在探索未来的安全增强措施，例如利用 OpenBSD 的 `unveil(2)` 系统调用来实现环境沙盒化。尽管目前缺乏 32 位兼容性，但该移植版代表了在 OpenBSD 上原生运行 Windows 二进制文件的重大进展。

---

## 4. 因为没有微软账号，我给我的 RTX Spark 笔记本装了 Linux。

**原文标题**: Putting Linux on my RTX spark laptop because I don't have a Microsoft account

**原文链接**: [https://josie.lol/blog/linux-rtx-spark](https://josie.lol/blog/linux-rtx-spark)

This article details the successful installation and optimization of **Arch Linux ARM** on the **ASUS ProArt P16** (H7607BA), a high-spec laptop featuring 128 GB of RAM and an NVIDIA GPU with 6,144 CUDA cores. The author, an Arch Linux package maintainer, migrated to Linux to avoid Microsoft’s privacy concessions and to leverage a more efficient memory architecture.

**Key Technical Achievements:**
*   **Unified Memory:** Unlike Windows, which partitions RAM into dedicated GPU and CPU regions, the Linux setup provides a unified **116.0 GiB pool** accessible to both the OS and CUDA. This allows for massive model allocations without the need for manual reboots or "reservation sliders."
*   **Custom Patches:** To achieve a functional system, the author implemented ACPI overrides for console mapping, patched the `hid-asus` driver for keyboard support, and extracted proprietary speaker firmware to enable audio.
*   **Performance Benchmarks:** In 7-Zip CPU testing, the Linux configuration outperformed Windows ARM64 results by approximately **5% in multi-threaded compression** and **2.7% in decompression**, while matching single-thread performance.

**AI and LLM Testing:**
The author utilized the hardware to run **Qwen3.8-Flash-Next** via vLLM, allocating nearly **90 GiB** of the laptop’s RAM for the model and KV cache. 
*   **Inference Speed:** The setup achieved roughly **30 tokens per second** for code review tasks, which is comparable to Windows performance.
*   **Efficiency:** The system processed nearly 10,000 tokens of incident logs in under six seconds.
*   **Reliability:** In a stress test of 171 requests, the system maintained consistent response times (less than 1.6% variance) and achieved a 100% success rate on deterministic checks.

Ultimately, the article demonstrates that with proper kernel and driver patches, high-end ARM laptops can serve as powerful, private, and flexible local workstations for fine-tuning and running large-scale open-weight AI models.

---

## 5. 回滚将持续到士气好转为止。

**原文标题**: The reverts will continue until morale improves

**原文链接**: [http://peter.eisentraut.org/blog/2026/10/09/the-reverts-will-continue-until-morale-improves](http://peter.eisentraut.org/blog/2026/10/09/the-reverts-will-continue-until-morale-improves)

在本文中，作者反思了 PostgreSQL 19 测试阶段中前所未有的大量功能回滚——涉及约 8 到 10 个重要项目。虽然部分回滚属正常现象，但此次规模之大实属罕见，主要源于技术变革、资源限制和系统复杂性的共同影响。

一个核心因素是 **LLM 辅助代码审查与模糊测试** 的兴起。这些工具能够比开发人员修复缺陷更快地识别出“长尾”边缘案例，显著提升了质量门槛。由于许多代码是在这些工具普及之前编写的，开发人员在开发周期后期突然面临海量的缺陷报告，感到措手不及。

此外，一系列被称为**“漏洞大爆发”（Vulnpocalypse）**的安全漏洞在 4 月至 8 月期间分散了高级开发人员的注意力。这导致深度架构审查和测试被推迟到测试期末尾，使得在不延误发布的前提下，没有足够的时间来解决发现的问题。

作者还指出，PostgreSQL“万物皆可协同”的哲学造就了极端的**架构复杂性**。在缺乏更好的内部脚手架或正式“实验性”状态（以便在主干树中磨合功能）的情况下，确保新功能与域、分区及触发器的各种组合正确交互正变得日益困难。

尽管遭遇挫折，作者仍持乐观态度。PostgreSQL 19 仍将包含 `REPACK CONCURRENTLY` 和序列逻辑复制等重大特性。作者总结道，更严格的审查将成就一个更稳健的版本，且许多被回滚的功能已为纳入 PostgreSQL 20 做好了充分准备。

---

## 6. Android 应用在 macOS 上原生运行

**原文标题**: Android apps running native on macOS

**原文链接**: [https://github.com/kksimp/Mac.apk](https://github.com/kksimp/Mac.apk)

**Mac.apk** 是一款开源工具，旨在 Apple Silicon Mac 上原生运行 Android 应用程序。与传统的模拟器或虚拟机不同，Mac.apk 直接在 macOS 之上实现 Android 环境。这使得应用程序可以作为普通的 macOS 进程启动，充分利用 Mac 的 GPU 并以原生速度在 CPU 上执行。

**核心功能与性能：**
应用程序可无缝集成到 macOS 生态系统中，不仅会出现在 Dock 栏中，还支持调整窗口大小、旋转以及浅色/深色模式切换等标准窗口行为。虽然应用的首次启动需要长达一分钟的准备时间，但随后的启动速度非常快。

**系统

**当前状态与安全性：**
该项目目前处于 **Alpha** 开发阶段。虽然稳定性足以支持使用，但兼容性表现不一——部分应用运行完美，而另一部分暂无法运行。

一个关键的安全区别在于，Mac.apk **不**为 Android 应用提供沙盒。它们运行时的权限与任何其他原生 Mac 应用程序相同，这意味着它们可以读写用户文件。建议用户仅从受信任的来源安装 APK。

**许可协议：**
Mac.apk 采用 GNU AGPL v3.0 许可协议，同时为希望规避 AGPL 条款的企业提供商业授权。该工具由 Voltare 开发，对个人用户保持免费。

---

## 7. 依然可以享受编程

**原文标题**: It's still ok to enjoy programming

**原文链接**: [https://chriskiehl.com/article/it-is-still-ok-to-enjoy-programming](https://chriskiehl.com/article/it-is-still-ok-to-enjoy-programming)

生成摘要时出错

---

## 8. RuneScape Bench: MMOs for Agents [video]

**原文标题**: RuneScape Bench: MMOs for Agents [video]

**原文链接**: [https://www.youtube.com/watch?v=cNm4zyUtWj0](https://www.youtube.com/watch?v=cNm4zyUtWj0)

Based on the title "RuneScape Bench: MMOs for Agents," this video explores the use of the classic MMORPG **RuneScape** as a benchmarking environment for autonomous AI agents.

While the provided text consists only of YouTube’s standard legal and footer information, the title points to a growing trend in AI research where complex video games are used to test the reasoning, planning, and execution capabilities of Large Action Models (LAMs) and autonomous agents.

**Key Themes and Information:**

*   **MMOs as Benchmarks:** Massively Multiplayer Online games offer a "sandbox" with complex economies, social interactions, and multi-step tasks. This makes them more challenging and realistic testing grounds for AI than traditional static benchmarks.
*   **Why RuneScape?** The game is an ideal "bench" because it requires long-term strategic planning (e.g., leveling up skills over hundreds of hours), resource management, and navigating a vast, persistent world. Its point-and-click interface is also more accessible for current AI vision and action systems compared to fast-paced 3D shooters.
*   **Evaluating Agent Performance:** The "Bench" likely refers to a framework for measuring how well an AI can perform human-like tasks—such as completing quests, trading on the Grand Exchange, or optimizing experience gain—without manual intervention.

In summary, the video likely discusses how RuneScape serves as a bridge between simple digital tasks and real-world problem solving for the next generation of AI agents.

---

## 9. The fire retardant in the seafood chain

**原文标题**: The fire retardant in the seafood chain

**原文链接**: [https://insideclimatenews.org/news/14102026/ethoxyquin-fire-retardant-in-seafood-chain/](https://insideclimatenews.org/news/14102026/ethoxyquin-fire-retardant-in-seafood-chain/)

生成摘要时出错

---

## 10. Timestral：Mistral 时间序列基础模型

**原文标题**: Timestral: Mistral's time-series foundation models

**原文链接**: [https://mistral.ai/news/timestral/](https://mistral.ai/news/timestral/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 2 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 3 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 4 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 5 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 6 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 7 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 8 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 9 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 10 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 11 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 12 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 13 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 14 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 15 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 16 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 17 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 18 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 19 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 20 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 21 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 22 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 23 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 24 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 25 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 26 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 27 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 28 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 29 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 30 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 31 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 32 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 33 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 34 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 35 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 36 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 37 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 38 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 39 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 40 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 41 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 42 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 43 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 44 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 45 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 46 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 47 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 48 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 49 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 50 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 51 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 52 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 53 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 54 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 55 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 56 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 57 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 58 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 59 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 60 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 61 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 62 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 63 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 64 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 65 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 66 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 67 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 68 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 69 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 70 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 71 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 72 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 73 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 74 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 75 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 76 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 77 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 78 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 79 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 80 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 81 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 82 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 83 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 84 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 85 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 86 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 87 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 88 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 89 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 90 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 91 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 92 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 93 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 94 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 95 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 96 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 97 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 98 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 99 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 100 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 101 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 102 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 103 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 104 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 105 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 106 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 107 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 108 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 109 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 110 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 111 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 112 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 113 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 114 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 115 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 116 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 117 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 118 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 119 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 120 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 121 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 122 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 123 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 124 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 125 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 126 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 127 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 128 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 129 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 130 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 131 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 132 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 133 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 134 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 135 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 136 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 137 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 138 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 139 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 140 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 141 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 142 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 143 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 144 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 145 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 146 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 147 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 148 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 149 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 150 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 151 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 152 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 153 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 154 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 155 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 156 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 157 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 158 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 159 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 160 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 161 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 162 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 163 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 164 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 165 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 166 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 167 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 168 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 169 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 170 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 171 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 172 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 173 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 174 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 175 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 176 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 177 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 178 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 179 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 180 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 181 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 182 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 183 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 184 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 185 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 186 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 187 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 188 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 189 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 190 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 191 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 192 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 193 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 194 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 195 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 196 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 197 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 198 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 199 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 200 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 201 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 202 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 203 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 204 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 205 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 206 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 207 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 208 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 209 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 210 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 211 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 212 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 213 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 214 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 215 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 216 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 217 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 218 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 219 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 220 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 221 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 222 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 223 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 224 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 225 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 226 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 227 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 228 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 229 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 230 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 231 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 232 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 233 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 234 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 235 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 236 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 237 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 238 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 239 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 240 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 241 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 242 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 243 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 244 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 245 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 246 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 247 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 248 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 249 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 250 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 251 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 252 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 253 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 254 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 255 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 256 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 257 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 258 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 259 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 260 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 261 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 262 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 263 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 264 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 265 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 266 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 267 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 268 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 269 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 270 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 271 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 272 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 273 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 274 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 275 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 276 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 277 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 278 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 279 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 280 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 281 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 282 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 283 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 284 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 285 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 286 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 287 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 288 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 289 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 290 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 291 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 292 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 293 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 294 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 295 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 296 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 297 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 298 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 299 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 300 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 301 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 302 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 303 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 304 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 305 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 306 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 307 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 308 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 309 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 310 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 311 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 312 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 313 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 314 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 315 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 316 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 317 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 318 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 319 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 320 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 321 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 322 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 323 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 324 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 325 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 326 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 327 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 328 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 329 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 330 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 331 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 332 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 333 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 334 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 335 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 336 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 337 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 338 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 339 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 340 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 341 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 342 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 343 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 344 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 345 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 346 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 347 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 348 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 349 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 350 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 351 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 352 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 353 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 354 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 355 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 356 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 357 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 358 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 359 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 360 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 361 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 362 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 363 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 364 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 365 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 366 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 367 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 368 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 369 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 370 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 371 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 372 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 373 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 374 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 375 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 376 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 377 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 378 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 379 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 380 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 381 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 382 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 383 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 384 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 385 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 386 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 387 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 388 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 389 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 390 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 391 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 392 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 393 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 394 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 395 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 396 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 397 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 398 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 399 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 400 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 401 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 402 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 403 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 404 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 405 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 406 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 407 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 408 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 409 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 410 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 411 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 412 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 413 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 414 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 415 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 416 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 417 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 418 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 419 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 420 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 421 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 422 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 423 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 424 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 425 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 426 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 427 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 428 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 429 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 430 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 431 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 432 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 433 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 434 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 435 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 436 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 437 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 438 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 439 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 440 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 441 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 442 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 443 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 444 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 445 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 446 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 447 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 448 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 449 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 450 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 451 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 452 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 453 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 454 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 455 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 456 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 457 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 458 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 459 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 460 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 461 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 462 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 463 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 464 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 465 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 466 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 467 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 468 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 469 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 470 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 471 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 472 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 473 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 474 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 475 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 476 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 477 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 478 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 479 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 480 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 481 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 482 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 483 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 484 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 485 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 486 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 487 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 488 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 489 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 490 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 491 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 492 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 493 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 494 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 495 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 496 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 497 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 498 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 499 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 500 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 501 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 502 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 503 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 504 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 505 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 506 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 507 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 508 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 509 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 510 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 511 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 512 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 513 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 514 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 515 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 516 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 517 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 518 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 519 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 520 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 521 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 522 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 523 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 524 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 525 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 526 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 527 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 528 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 529 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 530 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 531 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 532 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 533 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 534 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 535 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 536 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 537 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 538 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 539 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 540 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 541 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 542 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 543 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 544 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 545 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 546 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 547 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 548 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 549 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 550 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 551 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 552 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 553 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 554 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 555 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 556 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 557 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 558 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 559 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 560 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 561 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 562 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 563 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 564 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 565 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 566 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 567 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 568 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 569 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 570 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 571 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 572 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 573 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 574 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 575 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 576 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
