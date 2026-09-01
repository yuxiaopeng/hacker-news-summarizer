# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-09-01.md)

*最后自动更新时间: 2026-09-01 20:15:55*
## 1. Claude Fable 5.1 和 Claude Mythos 5.1

**原文标题**: Claude Fable 5.1 and Claude Mythos 5.1

**原文链接**: [https://www.anthropic.com/claude-fable-and-mythos-5-1](https://www.anthropic.com/claude-fable-and-mythos-5-1)

Anthropic 宣布推出 Claude Fable 5.1 和 Claude Mythos 5.1，这是其迄今为止在编程、知识工作和科学研究领域最先进的模型。虽然两个版本使用相同的底层模型，但 Fable 5.1 已全面开放，而 Mythos 5.1 则通过“受信访问计划”为网络安全和生命科学领域提供专门的安全保障。

**主要改进包括：**

*   **成本效益：** Fable 5.1 在典型工作负载下的成本降低了约 25%，在代理任务中降低了高达 45%，这主要归功于缓存读取定价的下调。
*   **隐私与数据保留：** 全新的“企业前沿保障”（EFS）系统实现了零数据保留，允许企业客户将数据存储在自己的云基础设施中，而非 Anthropic 的服务器上。
*   **优化的安全机制：** 该模型的网络安全误报率降低了 60%，使其能够在识别软件漏洞的同时，防止开发漏洞利用程序。
*   **卓越性能：** Fable 5.1 在代理编程 (Terminal-Bench)、多学科推理 (Humanity's Last Exam) 和计算机操作 (OSWorld 2.0) 方面树立了新基准。它旨在处理长周期的无人值守任务，且能保持逻辑连贯。

**行业影响：**
早期合作伙伴报告了显著的质性提升。Jane Street 和 Millennium 指出，该模型能够解决困扰人类工程师多年的复杂陈年漏洞；而 Cognition 和 Every 等公司则强调，与 Opus 5 相比，其速度和 Token 效率显著提升。该模型擅长“高难度”推理、创造性问题解决以及专业级内容生成，例如法律合同修订和金融演示文稿制作。

总体而言，5.1 版本的发布代表了自主问题解决能力的重大飞跃，以更经济的价格提供了前沿级别的智能。

---

## 2. Play 商店封杀 AuroraStore，损害 GrapheneOS 用户利益

**原文标题**: Play Store blocks AuroraStore, hurting GrapheneOS users

**原文链接**: [https://gitlab.com/AuroraOSS/AuroraStore/-/work_items/1566](https://gitlab.com/AuroraOSS/AuroraStore/-/work_items/1566)

这份 GitLab 问题报告指出 Aurora Store（一款 Google Play 商店的开源客户端）出现严重故障，导致用户无法安装应用程序。

**关键信息：**
*   **问题：** 用户在安装阶段遇到“服务器繁忙，请稍后再试”的错误消息。
*   **影响范围：** 该问题专门影响匿名账号。此类账号通常由不想在设备上绑定个人 Google 账号的用户使用。目前已确认稳定版和开发版（包括 2026 年 8 月的版本）均存在此问题。
*   **无效的对策：** 标准的故障排除步骤已证明无效。用户报告称，即便使用 VPN、清除应用缓存、刷新匿名凭据或重启设备，错误依然存在。
*   **影响：** 此次中断主要影响了 GrapheneOS 和 CalyxOS 等注重隐私的操作系统用户，他们依赖 Aurora Store 在没有 Google Play 服务的情况下管理应用。
*   **环境详情：** 该报告由一名使用 Fairphone 5（运行 CalyxOS，Android 16）的用户提交，这表明该问题在现代“去 Google 化”的硬件配置中广泛存在。

总之，报告指出 Google 可能正在屏蔽 Aurora Store 的匿名访问方式，从而有效阻止了没有 Google 账号的用户通过该客户端下载或更新应用程序。

---

## 3. Launch HN：Nori Robotics (YC S26) —— 一款用于开发的低成本人形机器人

**原文标题**: Launch HN: Nori Robotics (YC S26) – A low-cost humanoid robot for development

**原文链接**: [https://www.norirobotics.com/](https://www.norirobotics.com/)

Nori Robotics (YC S26) 宣布推出 **Nori A3**，这是一款旨在用于开发和日常家务辅助的平价人形机器人。该机器人售价为 **1,688 美元**，无需预付定金，被定位为同价位中功能最强的人形机器人。

**核心功能与特性：**
*   **家务任务：** Nori A3 旨在协助整理、折叠衣服、摆放碗筷，以及倒食材或从冰箱取物等厨房任务。
*   **硬件规格：** 该机器人配备双臂，具有 7+1 自由度 (DOF)，单臂负载能力为 1.5kg。它配有四个 720p RGB 摄像头（安装在头部、颈部和机械手掌上）、一个量程为 12 米的激光雷达系统，以及用于语音指令的集成音频。
*   **电池续航：** 提供 6 至 8 小时的运行时间。
*   **软件生态系统：** 用户可以通过 **Nori Lab** 笔记本电脑应用管理和训练机器人。专门的**技能市场**允许用户在家训练机器人，并向全球分享或下载新技能。

**发售信息：**
Nori Robotics 总部位于旧金山并在此组装，目前已开始接受 A3 的订单，计划于 **2026 年秋季**发货。该项目旨在降低人形机器人的准入门槛，为开发者和早期采用者提供一个低成本平台，以实现日常任务的自动化。

---

## 4. AnkiDroid：Google Play 不再允许 Open Collective 捐赠链接

**原文标题**: AnkiDroid: Google Play no longer allowing Open Collective donation link

**原文链接**: [https://github.com/ankidroid/Anki-Android/issues/21656](https://github.com/ankidroid/Anki-Android/issues/21656)

AnkiDroid 是一款拥有超过 1000 万次安装的热门开源记忆卡应用，因捐赠链接争议，正面临被 Google Play 商店下架的风险。

**冲突点**
Google Play 的支付政策要求大多数交易必须使用 Google 的结算系统，但对“免税捐赠”设有例外。AnkiDroid 的捐赠由 Open Source Collective 处理，这是一个具有 **IRS 501(c)(6) 免税身份** 的美国非营利组织。尽管 AnkiDroid 提供了官方的美国国税局（IRS）认定函，但 Google 仍拒绝了其应用更新，声称该组织“并非免税”。

**政策模糊性**
争议的核心在于“免税”的定义。虽然 501(c)(6) 组织属于免税实体，但与 501(c)(3) 慈善机构不同，向其捐赠的款项通常无法为捐赠者提供税收抵扣。Google 的沟通暗示他们可能仅认可 501(c)(3) 身份，尽管其书面政策仅简单表述为“免税”。

**后果与应对**
Google 已设定 **2026 年 9 月 11 日** 为该应用全球下架的截止日期（印度和俄罗斯除外）。为避免数百万用户受到断供影响，AnkiDroid 志愿者团队正“在抗议中”移除相关捐赠链接。

**行动倡议**
开发者正在寻求：
1. **Google 的澄清**：明确 501(c)(6) 身份是否符合其政策要求。
2. **社区支持**：协助转发此问题，以引起 Google 代表的关注，促成对该案例的人工审核。

AnkiDroid 是一个由志愿者主导的项目，这些捐赠是其持续开发和维护的唯一资金来源。

---

## 5. Show HN：在 48GB Mac 上以约 12 tok/s 的速度运行 104GB 的 Qwen3.8-Flash-Next

**原文标题**: Show HN: Running 104GB Qwen3.8-Flash-Next on 48GB Mac with at ~12 tok/s

**原文链接**: [https://github.com/carloslfu/slotstream](https://github.com/carloslfu/slotstream)

**slotstream** 是一款新型基于 Swift 的工具，旨在 Apple Silicon Mac 上运行 **Qwen3.8-Flash-Next** 模型（一个 125B 参数的混合专家 MoE 模型），即使在仅有 8GB 内存的设备上也能运行。虽然该模型在 4 位量化下需要 104GB 的磁盘空间，但 slotstream 通过利用 SSD 串流和自定义缓存系统，消除了对海量统一内存的需求。

**核心特性与性能：**
*   **性能：** 在配备 48GB 内存的 M5 Pro 上，该工具可实现约 **12 tokens/s** 的生成速度，冷启动仅需 3 秒。性能随内存增加而提升，在 8GB 内存机型上约为 3 tok/s，在 48GB 及以上机型上可达约 12 tok/s。
*   **内存管理：** 引擎会根据主机配置自动调整规模，通常设定 33GB 的上限以实现最佳性能。在系统压力下，它会动态缩小缓存，以确保 Mac 保持响应。
*   **兼容性：** 这是一个独立的 Swift 二进制文件（无 Python 依赖），实现了 OpenAI 和 Ollama 聊天 API。它可以直接适配 Open WebUI 和 Ollama CLI 等工具。
*   **高级功能：** 支持前缀缓存（prefix caching）以加速后续对话轮次，并提供可选的投机采样（MTP）功能以提升高端硬件上的运行速度。

**技术创新：**
传统的框架在尝试交换超过 100GB 的模型时往往会崩溃，而 slotstream 则不同，它将模型的“密集主干”（3.8GB）保留在内存中，同时将特定的“专家”层从 SSD 串流到共享缓存池。这使其能够运行远超可用内存容量的模型，且不会出现传统内存映射（mmap）带来的性能崩盘。

**运行

---

## 6. How accurate have Ed Zitron's AI skeptic predictions been?

**原文标题**: How accurate have Ed Zitron's AI skeptic predictions been?

**原文链接**: [https://danluu.com/zitron/](https://danluu.com/zitron/)

This article provides a detailed critique of Ed Zitron, a prominent AI skeptic, concluding that his predictions have been consistently inaccurate and his reasoning fundamentally flawed. The author, a neutral observer with a history of analyzing both futurist and skeptic claims, argues that Zitron relies on "sleight of hand" and "anti-tech grift" rather than sound analysis.

**Key points include:**

*   **Financial Misinterpretations:** Zitron claimed that Meta, Google, and Microsoft are "dying" companies using AI as a desperate move to hide a lack of growth. However, the author provides financial data from 2023 through 2026 showing these companies experiencing massive, record-breaking increases in both revenue and profit.
*   **Methodological Flaws:** The author highlights Zitron’s tendency to use "minor issues" or unreliable third-party data to support grand narratives of collapse. Other critics, such as Juho Snellman and Timothy B. Lee, are cited for finding egregious errors in Zitron’s financial models, including basic spreadsheet mistakes like counting dates twice or including "February 30."
*   **Failed Predictions:** The article lists a series of Zitron’s predictions from 2024 and 2025 that were proven wrong by subsequent events:
    *   **AI "Peaking":** Zitron repeatedly claimed AI had reached its limit in early 2024, yet models (like GPT-5 and o1) continued to show significant progress.
    *   **OpenAI's Collapse:** Despite Zitron’s claims of stalling growth, OpenAI significantly exceeded its revenue targets.
    *   **Gemini User Growth:** Zitron called Sundar Pichai’s goal of 500 million Gemini users "unrealistic"; the product eventually hit 750 million.
    *   **Data Scarcity:** His warnings that AI would stop improving due to a lack of data have not manifested.

The author concludes that Zitron’s primary appeal is his aggressive, angry tone which drives engagement among those already skeptical of tech, despite the fact that his "numbers-based" arguments fall apart under professional scrutiny.

---

## 7. Ambient CSS v3 – Blender meets CSS

**原文标题**: Ambient CSS v3 – Blender meets CSS

**原文链接**: [https://ambientcss.vercel.app/](https://ambientcss.vercel.app/)

生成摘要时出错

---

## 8. Movie Scene Map – 13,312 films, series, games, anime and manga

**原文标题**: Movie Scene Map – 13,312 films, series, games, anime and manga

**原文链接**: [https://moviescenemap.com/](https://moviescenemap.com/)

生成摘要时出错

---

## 9. I trained a small transformer in 1.5hrs and it beats many LLMs

**原文标题**: I trained a small transformer in 1.5hrs and it beats many LLMs

**原文链接**: [https://mvakde.github.io/blog/44-on-arc-1/](https://mvakde.github.io/blog/44-on-arc-1/)

生成摘要时出错

---

## 10. The creator of Jujutsu has joined ERSC

**原文标题**: The creator of Jujutsu has joined ERSC

**原文链接**: [https://ersc.io/blog/martin-joins-ersc](https://ersc.io/blog/martin-joins-ersc)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 2 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 3 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 4 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 5 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 6 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 7 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 8 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 9 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 10 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 11 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 12 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 13 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 14 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 15 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 16 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 17 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 18 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 19 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 20 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 21 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 22 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 23 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 24 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 25 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 26 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 27 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 28 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 29 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 30 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 31 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 32 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 33 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 34 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 35 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 36 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 37 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 38 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 39 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 40 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 41 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 42 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 43 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 44 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 45 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 46 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 47 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 48 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 49 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 50 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 51 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 52 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 53 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 54 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 55 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 56 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 57 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 58 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 59 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 60 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 61 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 62 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 63 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 64 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 65 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 66 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 67 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 68 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 69 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 70 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 71 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 72 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 73 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 74 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 75 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 76 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 77 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 78 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 79 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 80 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 81 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 82 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 83 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 84 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 85 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 86 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 87 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 88 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 89 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 90 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 91 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 92 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 93 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 94 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 95 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 96 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 97 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 98 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 99 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 100 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 101 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 102 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 103 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 104 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 105 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 106 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 107 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 108 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 109 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 110 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 111 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 112 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 113 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 114 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 115 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 116 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 117 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 118 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 119 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 120 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 121 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 122 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 123 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 124 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 125 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 126 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 127 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 128 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 129 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 130 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 131 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 132 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 133 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 134 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 135 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 136 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 137 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 138 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 139 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 140 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 141 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 142 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 143 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 144 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 145 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 146 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 147 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 148 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 149 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 150 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 151 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 152 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 153 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 154 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 155 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 156 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 157 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 158 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 159 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 160 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 161 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 162 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 163 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 164 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 165 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 166 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 167 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 168 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 169 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 170 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 171 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 172 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 173 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 174 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 175 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 176 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 177 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 178 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 179 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 180 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 181 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 182 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 183 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 184 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 185 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 186 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 187 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 188 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 189 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 190 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 191 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 192 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 193 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 194 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 195 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 196 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 197 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 198 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 199 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 200 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 201 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 202 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 203 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 204 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 205 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 206 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 207 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 208 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 209 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 210 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 211 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 212 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 213 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 214 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 215 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 216 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 217 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 218 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 219 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 220 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 221 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 222 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 223 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 224 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 225 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 226 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 227 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 228 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 229 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 230 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 231 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 232 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 233 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 234 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 235 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 236 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 237 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 238 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 239 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 240 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 241 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 242 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 243 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 244 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 245 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 246 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 247 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 248 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 249 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 250 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 251 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 252 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 253 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 254 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 255 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 256 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 257 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 258 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 259 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 260 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 261 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 262 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 263 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 264 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 265 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 266 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 267 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 268 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 269 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 270 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 271 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 272 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 273 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 274 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 275 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 276 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 277 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 278 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 279 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 280 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 281 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 282 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 283 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 284 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 285 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 286 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 287 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 288 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 289 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 290 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 291 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 292 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 293 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 294 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 295 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 296 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 297 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 298 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 299 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 300 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 301 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 302 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 303 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 304 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 305 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 306 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 307 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 308 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 309 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 310 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 311 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 312 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 313 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 314 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 315 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 316 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 317 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 318 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 319 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 320 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 321 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 322 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 323 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 324 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 325 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 326 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 327 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 328 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 329 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 330 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 331 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 332 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 333 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 334 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 335 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 336 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 337 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 338 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 339 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 340 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 341 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 342 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 343 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 344 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 345 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 346 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 347 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 348 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 349 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 350 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 351 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 352 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 353 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 354 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 355 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 356 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 357 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 358 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 359 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 360 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 361 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 362 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 363 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 364 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 365 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 366 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 367 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 368 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 369 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 370 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 371 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 372 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 373 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 374 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 375 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 376 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 377 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 378 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 379 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 380 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 381 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 382 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 383 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 384 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 385 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 386 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 387 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 388 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 389 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 390 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 391 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 392 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 393 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 394 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 395 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 396 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 397 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 398 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 399 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 400 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 401 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 402 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 403 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 404 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 405 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 406 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 407 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 408 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 409 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 410 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 411 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 412 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 413 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 414 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 415 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 416 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 417 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 418 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 419 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 420 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 421 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 422 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 423 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 424 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 425 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 426 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 427 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 428 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 429 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 430 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 431 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 432 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 433 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 434 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 435 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 436 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 437 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 438 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 439 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 440 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 441 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 442 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 443 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 444 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 445 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 446 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 447 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 448 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 449 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 450 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 451 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 452 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 453 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 454 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 455 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 456 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 457 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 458 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 459 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 460 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 461 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 462 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 463 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 464 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 465 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 466 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 467 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 468 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 469 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 470 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 471 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 472 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 473 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 474 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 475 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 476 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 477 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 478 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 479 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 480 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 481 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 482 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 483 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 484 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 485 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 486 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 487 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 488 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 489 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 490 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 491 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 492 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 493 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 494 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 495 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 496 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 497 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 498 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 499 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 500 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 501 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 502 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 503 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 504 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 505 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 506 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 507 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 508 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 509 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 510 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 511 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 512 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 513 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 514 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 515 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 516 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 517 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 518 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 519 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 520 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 521 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 522 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 523 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 524 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 525 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 526 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 527 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 528 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
