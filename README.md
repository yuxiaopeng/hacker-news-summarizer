# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-24.md)

*最后自动更新时间: 2026-04-24 18:21:10*
## 1. 过度思考、范围蔓延和结构化对比对项目的破坏

**原文标题**: Sabotaging projects by overthinking, scope creep, and structural diffing

**原文链接**: [https://kevinlynagh.com/newsletter/2026_04_overthinking/](https://kevinlynagh.com/newsletter/2026_04_overthinking/)

在这期通讯中，Kevin探讨了个人项目为何常因过度思考和范围蔓延而停滞。他对比了两种项目路径：一种是受清晰且内在的成功标准驱动的“直接去做”；另一种则是沉溺于“现有技术”调研和复杂需求。他以一个成功的极简木工项目与几个长期未完成的软件构想为例，阐述了这一观点。

文章的核心主题是“范围蔓延守恒定律”。Kevin观察到，虽然大模型（LLM）代理提升了编程速度，但往往也会诱使开发者添加不必要的功能。他讲述了自己构建文件系统搜索工具的经历：他差点过度设计了复杂的“锚定”功能，直到意识到自己根本不会用到它，最终将代码精简至核心要素（遵循 YAGNI 原则）。

技术核心部分聚焦于“结构化/语义化差异比对”。Kevin认为，标准的逐行比对——甚至是像 *difftastic* 这样的工具——在代码实体（如函数或结构体）发生移动或变更时，往往无法进行准确匹配。在研究了 *Gumtree*、*SemanticDiff* 和 *Weave* 等现有工具后，他发现它们要么过于学术化、臃肿，要么无法很好地适配他基于 Emacs 的工作流。

他的目标是为逐轮审查大模型生成的代码创建一个高层概览，以便在实体层面而非行层面查看变更。为了避免陷入过度思考的陷阱，他计划构建一个基于 Rust 的最小化实体提取原型供自己使用，而非尝试开发商业级产品。

最后，Kevin倡导“在做中学”并秉持“最小范围”的心态。他总结道，与其因过度权衡各种可能性而一事无成，不如做出一个事后看来“明显很差”的成品。

---

## 2. SDL 现已支持 DOS

**原文标题**: SDL Now Supports DOS

**原文链接**: [https://github.com/libsdl-org/SDL/pull/15377](https://github.com/libsdl-org/SDL/pull/15377)

2026年4月，SDL (Simple DirectMedia Layer) 库正式增加了对 DOS 的支持。该移植版本由 AJenbo、icculus 及其他几位贡献者组成的团队开发，为在老旧硬件及 DOSBox 等模拟器上运行现代 SDL 应用程序提供了一个健壮的框架。

**技术规范：**
*   **视频：** 该移植版支持 VGA 和 VESA 1.2+ 帧缓冲，提供 8 位索引色和 RGB 模式，并包含硬件页翻转 (page-flipping) 和垂直同步 (vsync) 支持。
*   **音频：** 具备全面的 Sound Blaster 支持，涵盖从 SB16（16 位立体声）到 SB 1.x（8 位单声道），并利用中断驱动的 DMA 技术。
*   **输入：** 支持 PS/2 键盘、INT 33h 鼠标，以及通过 BIOS INT 15h 实现的游戏端口摇杆。
*   **线程与系统：** 由于 DOS 缺乏原生多任务处理能力，SDL 通过使用 `setjmp/longjmp` 配合堆栈修补 (stack patching) 实现了一个协作式调度器。它采用 DJGPP 工具链进行交叉编译，并提供基于原生 PIT 的计时功能。

**当前状态与局限性：**
虽然该移植版已基本完成，并能运行《雷神之锤》(Quake) 和 DevilutionX 等对性能有要求的作品，但仍缺失部分功能，包括音频录制和共享库加载 (`SDL_LoadObject`)。

在拉取请求的最后阶段，开发者解决了有关 8 位调色板处理以及 DOS 兼容性所需的“8.3”文件名限制等特定问题。尽管某些自动化测试在特定环境下显示出轻微的稳定性问题，但贡献者们一致认为该移植版已具备合并入主分支的条件，这标志着复古计算和爱好者开发社区的一个重要里程碑。

---

## 3. 我退订了 Claude：Token 问题、质量下降及支持不力

**原文标题**: I Cancelled Claude: Token Issues, Declining Quality, and Poor Support

**原文链接**: [https://nickyreinert.de/en/2026/2026-04-24-claude-critics/](https://nickyreinert.de/en/2026/2026-04-24-claude-critics/)

本文详细介绍了一位订阅者决定取消 Claude Pro 账户的原因。其心态经历了从最初的热情到因以下三个主要问题而产生的沮丧：

**1. 糟糕的客户支持**
在简单的提问导致不明原因的 100% 代币（Token）使用率激增后，作者联系了客服。然而，他们仅收到了自动化的模板化回复，随后人工代表发来了一封敷衍的邮件，仅提供了一些公式化的信息，并在未解决具体问题的情况下关闭了工单。

**2. 质量下降与“懒惰”的 AI**
作者观察到模型性能显著下降。在一个案例中，Claude Opus 建议采用“偷懒”的代码变通方案，而非进行正规的重构。纠正这些劣质建议浪费了用户 5 小时代币额度的约 50%。作者指出，过去他们能同时处理三个项目，而现在的代币限制在仅处理一个项目两小时后就会耗尽。

**3. 代币与缓存机制的不一致**
作者批评了当前的缓存系统，该系统要求用户在休息后重新“支付”代币以加载其代码库。他们还遇到了未说明的“月度使用限制”警告，以及每周重置计划的意外变更，这造成了技术上的不可预测性。

**结论**
尽管作者依然认可 Claude 的潜力，并称赞该工具显著提高了其生产力，但他们得出结论：Anthropic 目前无法应对规模扩张带来的挑战。技术摩擦、AI 输出的“懒惰”感，以及在客户服务中表现出的傲慢态度，最终促使他们取消了订阅。

---

## 4. DeepSeek v4

**原文标题**: DeepSeek v4

**原文链接**: [https://api-docs.deepseek.com/](https://api-docs.deepseek.com/)

本文详细介绍了向 **DeepSeek v4** 的过渡，并推出了两个主要模型：`deepseek-v4-flash` 和 `deepseek-v4-pro`。

关键信息包括：

*   **API 兼容性：** DeepSeek API 完全兼容 OpenAI 和 Anthropic 的 SDK。用户只需将基础 URL 设置为 `https://api.deepseek.com` 即可访问这些模型。
*   **新功能：** v4 模型支持用于复杂推理的“思考”模式。该模式通过 `thinking: {"type": "enabled"}` 参数激活，并可配合 `reasoning_effort` 设置（如 "high"）。
*   **模型废弃：** 现有的 `deepseek-chat` 和 `deepseek-reasoner` 模型计划于 **2026 年 7 月 24 日** 停止服务。为确保在此之前的向后兼容性，这些旧模型名称将自动分别路由至 `deepseek-v4-flash` 的非思考模式和思考模式。
*   **开发实现：** 文档提供了 cURL、Python 和 Node.js 的代码示例。开发者可以使用标准的 OpenAI 客户端，只需提供 DeepSeek API 密钥，并更新 `model` 和 `extra_body` 参数即可调用 v4 的新能力。

总之，DeepSeek v4 在精简模型产品线的同时，通过标准化的 API 格式实现了对推理过程的精细化控制。

---

## 5. 我不再开发桌面应用了 (2009)

**原文标题**: I'm done making desktop applications (2009)

**原文链接**: [https://www.kalzumeus.com/2009/09/05/desktop-aps-versus-web-apps/](https://www.kalzumeus.com/2009/09/05/desktop-aps-versus-web-apps/)

In this 2009 article, Patrick McKenzie outlines his transition from developing downloadable desktop software to web-based applications (SaaS), primarily based on his experiences with his business, Bingo Card Creator. He identifies several fundamental disadvantages of the desktop model that hinder growth for independent developers.

Key points include:

*   **Reduced Friction and Higher Conversion:** Desktop software requires a "Download-Install-Run" cycle that often triggers security warnings and requires technical competence. Web apps offer "instant gratification," allowing users to trial and purchase immediately within the browser, significantly increasing conversion rates.
*   **Support and Maintenance Simplification:** Supporting desktop software involves troubleshooting endless combinations of operating systems (Windows XP, Vista, etc.) and hardware. With web apps, the developer controls the environment, and the only requirement for the user is a modern browser.
*   **Seamless Updates:** Updating desktop software is a logistical challenge involving version fragmentation. In contrast, web app updates are instantaneous for all users, ensuring everyone is always on the most stable and feature-rich version.
*   **Elimination of Piracy:** While desktop applications are easily cracked and distributed, SaaS models are virtually immune to traditional piracy because the core logic and data reside on the developer’s server.
*   **Marketing Integration:** McKenzie notes that web apps allow for a tighter loop between SEO, marketing, and the product itself. The "sales page" and the "product" live in the same ecosystem, streamlining the customer journey.

Ultimately, McKenzie concludes that the web-app model provides a superior ROI and a more scalable business framework by removing the technical and psychological barriers inherent in installing local software.

---

## 6. Different Language Models Learn Similar Number Representations

**原文标题**: Different Language Models Learn Similar Number Representations

**原文链接**: [https://arxiv.org/abs/2604.20817](https://arxiv.org/abs/2604.20817)

生成摘要时出错

---

## 7. Norway Set to Become Latest Country to Ban Social Media for Under 16s

**原文标题**: Norway Set to Become Latest Country to Ban Social Media for Under 16s

**原文链接**: [https://www.bloomberg.com/news/articles/2026-04-24/norway-wants-kids-to-be-kids-with-social-media-ban-for-under-16s](https://www.bloomberg.com/news/articles/2026-04-24/norway-wants-kids-to-be-kids-with-social-media-ban-for-under-16s)

生成摘要时出错

---

## 8. How to be anti-social – a guide to incoherent and isolating social experiences

**原文标题**: How to be anti-social – a guide to incoherent and isolating social experiences

**原文链接**: [https://nate.leaflet.pub/3mk4xkaxobc2p](https://nate.leaflet.pub/3mk4xkaxobc2p)

生成摘要时出错

---

## 9. Spinel: Ruby AOT Native Compiler

**原文标题**: Spinel: Ruby AOT Native Compiler

**原文链接**: [https://github.com/matz/spinel](https://github.com/matz/spinel)

生成摘要时出错

---

## 10. Show HN: Browser Harness – Gives LLM freedom to complete any browser task

**原文标题**: Show HN: Browser Harness – Gives LLM freedom to complete any browser task

**原文链接**: [https://github.com/browser-use/browser-harness](https://github.com/browser-use/browser-harness)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 2 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 3 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 4 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 5 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 6 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 7 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 8 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 9 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 10 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 11 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 12 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 13 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 14 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 15 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 16 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 17 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 18 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 19 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 20 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 21 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 22 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 23 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 24 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 25 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 26 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 27 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 28 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 29 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 30 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 31 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 32 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 33 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 34 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 35 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 36 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 37 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 38 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 39 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 40 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 41 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 42 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 43 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 44 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 45 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 46 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 47 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 48 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 49 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 50 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 51 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 52 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 53 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 54 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 55 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 56 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 57 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 58 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 59 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 60 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 61 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 62 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 63 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 64 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 65 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 66 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 67 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 68 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 69 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 70 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 71 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 72 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 73 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 74 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 75 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 76 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 77 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 78 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 79 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 80 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 81 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 82 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 83 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 84 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 85 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 86 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 87 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 88 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 89 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 90 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 91 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 92 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 93 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 94 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 95 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 96 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 97 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 98 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 99 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 100 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 101 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 102 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 103 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 104 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 105 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 106 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 107 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 108 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 109 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 110 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 111 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 112 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 113 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 114 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 115 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 116 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 117 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 118 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 119 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 120 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 121 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 122 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 123 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 124 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 125 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 126 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 127 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 128 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 129 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 130 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 131 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 132 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 133 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 134 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 135 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 136 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 137 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 138 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 139 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 140 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 141 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 142 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 143 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 144 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 145 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 146 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 147 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 148 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 149 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 150 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 151 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 152 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 153 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 154 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 155 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 156 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 157 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 158 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 159 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 160 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 161 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 162 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 163 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 164 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 165 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 166 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 167 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 168 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 169 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 170 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 171 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 172 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 173 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 174 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 175 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 176 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 177 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 178 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 179 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 180 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 181 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 182 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 183 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 184 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 185 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 186 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 187 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 188 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 189 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 190 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 191 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 192 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 193 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 194 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 195 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 196 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 197 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 198 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 199 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 200 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 201 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 202 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 203 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 204 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 205 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 206 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 207 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 208 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 209 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 210 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 211 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 212 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 213 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 214 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 215 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 216 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 217 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 218 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 219 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 220 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 221 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 222 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 223 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 224 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 225 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 226 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 227 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 228 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 229 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 230 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 231 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 232 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 233 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 234 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 235 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 236 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 237 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 238 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 239 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 240 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 241 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 242 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 243 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 244 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 245 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 246 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 247 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 248 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 249 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 250 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 251 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 252 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 253 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 254 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 255 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 256 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 257 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 258 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 259 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 260 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 261 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 262 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 263 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 264 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 265 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 266 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 267 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 268 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 269 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 270 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 271 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 272 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 273 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 274 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 275 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 276 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 277 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 278 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 279 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 280 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 281 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 282 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 283 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 284 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 285 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 286 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 287 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 288 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 289 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 290 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 291 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 292 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 293 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 294 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 295 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 296 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 297 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 298 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 299 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 300 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 301 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 302 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 303 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 304 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 305 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 306 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 307 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 308 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 309 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 310 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 311 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 312 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 313 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 314 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 315 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 316 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 317 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 318 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 319 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 320 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 321 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 322 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 323 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 324 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 325 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 326 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 327 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 328 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 329 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 330 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 331 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 332 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 333 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 334 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 335 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 336 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 337 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 338 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 339 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 340 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 341 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 342 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 343 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 344 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 345 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 346 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 347 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 348 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 349 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 350 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 351 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 352 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 353 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 354 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 355 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 356 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 357 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 358 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 359 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 360 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 361 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 362 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 363 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 364 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 365 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 366 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 367 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 368 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 369 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 370 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 371 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 372 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 373 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 374 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 375 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 376 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 377 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 378 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 379 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 380 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 381 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 382 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 383 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 384 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 385 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 386 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 387 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 388 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 389 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 390 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 391 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 392 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 393 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 394 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 395 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 396 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 397 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 398 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 399 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 400 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
