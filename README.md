# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-06-17.md)

*最后自动更新时间: 2026-06-17 19:50:32*
## 1. Epic Games 发布 Lore 版本控制系统

**原文标题**: Epic Games announces Lore version control system

**原文链接**: [https://lore.org/](https://lore.org/)

Epic Games 宣布推出 **Lore**，这是一个下一代开源版本控制系统 (VCS)，专为处理现代游戏开发和媒体项目的海量规模而设计。与传统系统不同，Lore 针对源代码与大型二进制资产共存的环境进行了优化，能够同时满足开发者和艺术家的工作流程需求。

**技术架构**
Lore 采用基于 Merkle 树和不可变版本链的中心化、内容寻址架构。这确保了加密数据的完整性和“防篡改”的历史记录。主要技术特性包括：
*   **大文件分块：** 将沉重的资产分解为可复用的数据块，以最大限度地减少冗余并优化传输。
*   **按需填充 (On-Demand Hydration)：** 支持稀疏工作区，仅在需要时下载数据，从而保持本地环境的轻量化。
*   **高扩展性：** 采用内置缓存的面向服务设计，使系统能够处理大型团队的高吞吐量需求。
*   **高效分支：** 分支以轻量级引用的形式实现，支持近乎瞬时的创建和切换，且无需复制底层数据。

**集成与开源理念**
Lore 完全开源，并在 **MIT 许可证**下发布。Epic Games 强调协作模式，鼓励社区贡献代码，旨在打造版本控制的开放标准。

该系统提供功能完备的命令行界面 (CLI)，并为多种编程语言提供 SDK，包括 **C/C++、C#、Rust、Go、Python 和 JavaScript**，确保其能够无缝集成到各种生产管线中。

**入门指南**
该项目目前托管在 Epic Games 的 GitHub 仓库中，用户可以在此处获取核心库、服务器代码和文档。此外，官方还建立了专门的 Discord 社区，为早期采用者和贡献者提供支持。

---

## 2. Only 16 Percent of Americans Think AI Will Have a Positive Impact on Society

**原文标题**: Only 16 Percent of Americans Think AI Will Have a Positive Impact on Society

**原文链接**: [https://techcrunch.com/2026/06/17/only-16-percent-of-americans-think-ai-will-have-a-positive-impact-on-society-a-new-study-shows/](https://techcrunch.com/2026/06/17/only-16-percent-of-americans-think-ai-will-have-a-positive-impact-on-society-a-new-study-shows/)

A recent Pew Research study reveals a profound disconnect between Americans’ increasing use of AI and their deep-seated skepticism regarding its future. While AI adoption is surging—with ChatGPT usage doubling since 2023 to 44% of adults—only 16% of Americans believe the technology will have a positive impact on society over the next 20 years. Conversely, 40% anticipate a negative impact, and two-thirds feel development is moving too quickly.

Public trust in the oversight of AI is notably low: 67% of respondents doubt the government’s ability to regulate the industry effectively, and 59% do not trust corporations to develop the technology safely. Surprisingly, young people (under 30) are the most pessimistic, with only 14% expecting a positive societal outcome.

Usage patterns also highlight demographic divides:
*   **Gender:** Men use AI more frequently and express more enthusiasm, while women remain more skeptical.
*   **Age:** While those under 50 are the primary users, nearly 75% of Americans aged 65 and older have never used a chatbot and express little interest in doing so.
*   **Market Dominance:** ChatGPT remains the leader, followed by Google’s Gemini (24%) and Microsoft’s Copilot (17%).

Despite their reservations, many Americans now find AI unavoidable. Approximately 25% use chatbots daily for work or research, and 60% regularly consume AI-generated internet summaries. Ultimately, the report portrays a nation that is integrating AI into daily life out of utility or necessity, even as it remains profoundly uneasy about the long-term consequences.

---

## 3. Launch HN: Adam (YC W25) – Open-Source AI CAD

**原文标题**: Launch HN: Adam (YC W25) – Open-Source AI CAD

**原文链接**: [https://github.com/Adam-CAD/CADAM](https://github.com/Adam-CAD/CADAM)

生成摘要时出错

---

## 4. GLM-5.2 是 Artificial Analysis 上新晋领先的开源权重模型。

**原文标题**: GLM-5.2 is the new leading open weights model on Artificial Analysis

**原文链接**: [https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index](https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index)

2026年6月17日，Z ai 发布了 **GLM-5.2**，该模型已正式成为 Artificial Analysis 智能指数 v4.1 上领先的开源权重模型。它凭借 51 分的得分，超越了 MiniMax-M3、DeepSeek V4 Pro 和 Kimi K2.6 等竞争对手。

**关键性能与技术规格：**
*   **架构：** 保持与 GLM-5.1 相同的规模（总参数 744B / 激活参数 40B），但实现了 11 分的智力提升。
*   **基准测试：** 该模型在科学推理（CritPt、HLE 和 GPQA Diamond）和智能体性能方面表现出显著进步。值得注意的是，它在 GDPval-AA v2 上获得了 1524 分，足以媲美 GPT-5.5 等私有模型。
*   **上下文窗口：** 从上一版本的 20 万 token 大幅扩展至 100 万 token。
*   **许可协议：** 基于 MIT 协议发布。

**成本与效率：**
GLM-5.2 处于**“智力 vs. 单任务成本”帕累托前沿**，这意味着在同等智力水平下，它提供了最低的成本（每任务 0.46 美元）。然而，它的 token 效率低于同类模型，每任务消耗 4.3 万个输出 token（其中 3.7 万个为推理 token）。其 API 定价与 GLM-5.1 保持一致：每百万输入 token 1.40 美元，每百万输出 token 4.40 美元。

**可用性：**
除了 Z ai 的官方 API 外，该模型还通过 DeepInfra、Novita、Nebius、硅基流动 (Siliconflow) 和 Fireworks 等第三方供应商广泛提供。尽管 GLM-5.2 在开源权重类别中处于领先地位，但在综合性能上目前仍落后于 Anthropic 的 Claude Fable 5 等“神话级” (Mythos-class) 私有模型。

---

## 5. How we run Firecracker VMs inside EC2 and start browsers in less than 1s

**原文标题**: How we run Firecracker VMs inside EC2 and start browsers in less than 1s

**原文链接**: [https://browser-use.com/posts/firecracker-browser-infra](https://browser-use.com/posts/firecracker-browser-infra)

Browser Use Cloud recently overhauled its infrastructure to achieve three primary goals for its cloud browsers: speed, security, and affordability. By transitioning from Unikraft unikernels to **Firecracker VMs** running on standard **AWS EC2** instances, the company reduced costs from $0.06 to $0.02 per hour and achieved start times of under one second.

To overcome the latency of "nested virtualization" (running a VM inside an EC2 VM), the team implemented several low-level optimizations:

*   **Memory Management:** By switching from 4KB to **2MB memory pages**, they reduced expensive page faults by 91%, cutting VM resume time from 9.8s to 3.1s. They also utilized a custom `userfaultfd` handler to proactively load memory pages.
*   **CPU Optimization:** To handle Chromium’s resource-heavy startup, vCPUs are left unpinned during the launch burst to spread the load across the host. Once the browser is ready, vCPUs are pinned to specific cores with real-time priority to ensure stability and high density.
*   **Communication:** The host monitors the VM via **vsock** instead of HTTP polling, reducing "VM exits" and latency.
*   **Stealth and Efficiency:** Instead of using resource-heavy display servers, they developed a custom **headless Chromium fork**. By patching the browser at a low level and using real-world fingerprints, they achieved a top-tier 81% anti-bot bypass rate without the overhead of a graphical interface.

The result is a system with a **p50 creation latency of 825ms** and 100% reliability during stress tests. Moving forward, the team plans to snapshot VMs *after* Chromium has already launched, which could shave another 500ms off the startup time by eliminating the browser’s internal boot process.

---

## 6. US holds off blacklisting DeepSeek, more than 100 firms deemed security risks

**原文标题**: US holds off blacklisting DeepSeek, more than 100 firms deemed security risks

**原文链接**: [https://www.reuters.com/world/china/us-holds-off-blacklisting-chinas-deepseek-more-than-100-firms-deemed-security-2026-06-17/](https://www.reuters.com/world/china/us-holds-off-blacklisting-chinas-deepseek-more-than-100-firms-deemed-security-2026-06-17/)

生成摘要时出错

---

## 7. The Competitive Moat That AI Can't Replicate

**原文标题**: The Competitive Moat That AI Can't Replicate

**原文链接**: [https://ghostinthedata.info/posts/2026/2026-06-13-human-connection-moat/](https://ghostinthedata.info/posts/2026/2026-06-13-human-connection-moat/)

生成摘要时出错

---

## 8. Sixty percent of US consumers say 'AI' in brand messaging is a turnoff

**原文标题**: Sixty percent of US consumers say 'AI' in brand messaging is a turnoff

**原文链接**: [https://wpvip.com/future-of-the-web-2026/](https://wpvip.com/future-of-the-web-2026/)

生成摘要时出错

---

## 9. RFC 10008: The new HTTP Query Method

**原文标题**: RFC 10008: The new HTTP Query Method

**原文链接**: [https://www.rfc-editor.org/info/rfc10008/](https://www.rfc-editor.org/info/rfc10008/)

生成摘要时出错

---

## 10. U.S. science is in chaos

**原文标题**: U.S. science is in chaos

**原文链接**: [https://www.scientificamerican.com/article/americas-compact-between-science-and-politics-is-broken/](https://www.scientificamerican.com/article/americas-compact-between-science-and-politics-is-broken/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 2 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 3 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 4 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 5 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 6 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 7 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 8 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 9 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 10 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 11 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 12 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 13 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 14 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 15 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 16 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 17 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 18 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 19 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 20 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 21 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 22 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 23 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 24 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 25 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 26 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 27 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 28 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 29 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 30 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 31 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 32 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 33 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 34 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 35 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 36 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 37 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 38 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 39 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 40 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 41 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 42 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 43 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 44 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 45 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 46 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 47 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 48 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 49 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 50 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 51 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 52 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 53 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 54 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 55 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 56 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 57 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 58 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 59 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 60 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 61 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 62 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 63 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 64 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 65 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 66 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 67 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 68 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 69 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 70 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 71 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 72 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 73 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 74 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 75 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 76 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 77 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 78 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 79 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 80 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 81 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 82 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 83 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 84 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 85 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 86 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 87 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 88 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 89 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 90 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 91 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 92 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 93 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 94 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 95 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 96 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 97 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 98 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 99 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 100 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 101 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 102 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 103 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 104 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 105 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 106 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 107 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 108 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 109 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 110 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 111 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 112 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 113 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 114 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 115 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 116 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 117 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 118 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 119 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 120 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 121 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 122 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 123 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 124 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 125 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 126 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 127 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 128 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 129 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 130 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 131 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 132 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 133 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 134 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 135 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 136 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 137 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 138 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 139 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 140 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 141 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 142 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 143 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 144 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 145 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 146 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 147 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 148 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 149 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 150 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 151 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 152 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 153 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 154 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 155 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 156 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 157 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 158 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 159 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 160 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 161 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 162 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 163 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 164 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 165 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 166 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 167 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 168 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 169 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 170 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 171 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 172 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 173 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 174 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 175 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 176 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 177 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 178 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 179 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 180 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 181 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 182 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 183 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 184 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 185 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 186 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 187 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 188 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 189 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 190 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 191 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 192 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 193 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 194 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 195 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 196 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 197 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 198 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 199 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 200 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 201 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 202 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 203 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 204 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 205 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 206 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 207 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 208 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 209 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 210 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 211 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 212 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 213 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 214 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 215 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 216 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 217 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 218 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 219 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 220 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 221 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 222 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 223 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 224 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 225 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 226 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 227 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 228 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 229 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 230 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 231 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 232 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 233 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 234 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 235 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 236 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 237 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 238 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 239 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 240 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 241 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 242 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 243 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 244 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 245 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 246 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 247 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 248 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 249 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 250 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 251 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 252 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 253 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 254 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 255 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 256 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 257 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 258 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 259 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 260 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 261 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 262 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 263 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 264 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 265 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 266 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 267 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 268 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 269 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 270 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 271 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 272 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 273 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 274 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 275 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 276 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 277 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 278 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 279 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 280 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 281 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 282 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 283 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 284 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 285 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 286 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 287 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 288 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 289 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 290 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 291 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 292 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 293 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 294 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 295 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 296 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 297 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 298 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 299 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 300 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 301 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 302 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 303 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 304 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 305 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 306 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 307 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 308 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 309 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 310 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 311 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 312 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 313 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 314 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 315 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 316 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 317 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 318 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 319 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 320 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 321 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 322 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 323 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 324 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 325 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 326 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 327 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 328 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 329 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 330 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 331 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 332 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 333 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 334 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 335 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 336 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 337 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 338 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 339 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 340 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 341 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 342 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 343 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 344 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 345 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 346 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 347 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 348 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 349 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 350 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 351 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 352 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 353 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 354 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 355 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 356 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 357 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 358 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 359 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 360 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 361 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 362 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 363 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 364 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 365 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 366 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 367 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 368 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 369 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 370 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 371 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 372 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 373 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 374 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 375 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 376 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 377 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 378 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 379 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 380 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 381 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 382 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 383 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 384 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 385 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 386 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 387 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 388 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 389 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 390 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 391 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 392 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 393 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 394 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 395 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 396 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 397 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 398 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 399 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 400 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 401 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 402 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 403 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 404 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 405 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 406 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 407 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 408 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 409 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 410 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 411 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 412 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 413 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 414 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 415 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 416 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 417 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 418 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 419 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 420 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 421 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 422 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 423 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 424 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 425 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 426 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 427 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 428 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 429 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 430 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 431 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 432 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 433 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 434 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 435 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 436 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 437 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 438 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 439 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 440 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 441 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 442 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 443 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 444 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 445 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 446 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 447 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 448 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 449 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 450 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 451 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 452 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 453 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 454 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
