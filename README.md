# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-06-29.md)

*最后自动更新时间: 2026-06-29 19:34:27*
## 1. Qwen 3.6 27B 是本地开发的最佳平衡点

**原文标题**: Qwen 3.6 27B is the sweet spot for local development

**原文链接**: [https://quesma.com/blog/qwen-36-is-awesome/](https://quesma.com/blog/qwen-36-is-awesome/)

在这篇博文中，Piotr Migdał 指出，截至 2026 年 6 月，**Qwen 3.6 27B** 已成为本地 AI 开发的“黄金平衡点”。尽管该模型提供了速度更快的 35B 混合专家（MoE）版本，但 Migdał 更推荐 **27B 稠密版**，因其具备更卓越的“通用智能”和指令遵循能力。

**核心亮点：**
*   **性能与推理：** 27B 模型在处理复杂且受限的任务时表现优异——例如创作关于量子物理的诗歌或生成功能完备的多文件代码包——此类任务此前需要 GPT-4.5 等昂贵的前沿模型才能完成。
*   **技术配置：** 作者建议通过 **llama.cpp** 配合 8 位量化（Q8_0）来运行该模型。他特别强调了 **多标记预测（MTP）** 的应用，这显著提升了运行速度。在 MacBook Max M5 上，该配置的生成速度可达每秒约 32 个标记（tokens），足以媲美许多云端 API。
*   **基准测试：** 在 2026 年的基准测试中，Qwen 3.6 27B 与 2025 年中的前沿模型（如 GPT-5 和 Claude 4.5 Sonnet）旗鼓相当，并轻松超越了 Gemma 4 31B 等竞争对手。
*   **伦理与实用优势：** Migdał 主张使用本地模型以确保数据隐私，规避私有 API 价格波动的风险，并保持对“前沿级”智能的离线访问。此外，出于伦理考量，他表示相比 Ollama 更倾向于使用 `llama.cpp`。

**展望未来：**
文章最后预测，模型开发将趋向于将纯粹的推理能力与事实性知识分离。通过将数据检索任务交给工具调用（tool-calling），未来的本地模型可能会变得更加智能和高效，甚至能够在保持高水平推理能力的同时，在消费级智能手机上流畅运行。

---

## 2. Rocket Lab 收购铱星公司

**原文标题**: Rocketlab acquires Iridium

**原文链接**: [https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-acquire-iridium-historic-deal-creating-fully](https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-acquire-iridium-historic-deal-creating-fully)

无法访问文章链接。

---

## 3. 一款原生的 SSH 图形化 Shell

**原文标题**: A native graphical shell for SSH

**原文链接**: [https://probablymarcus.com/blocks/2026/06/28/native-graphical-shell-for-SSH.html](https://probablymarcus.com/blocks/2026/06/28/native-graphical-shell-for-SSH.html)

本文介绍了 **Outer Shell**，这是一个开源的原生图形化外壳程序，旨在现代化用户通过 SSH 与远程服务器及边缘设备交互的方式。作者认为，尽管浏览器已经精通客户端-服务器流程，但 Linux 服务器仍缺乏统一且安全的图形界面，目前仍依赖于基于终端的应用或碎片化的 Web 工具（如 Jupyter）。

**关键技术创新：**
*   **基于 SSH 的交付：** 系统使用 **Outer Loop**（一种具备 SSH 感知能力的浏览器）连接到服务器。安全和加密完全由 SSH 层处理，从而使内部应用能够保持简洁且无依赖。
*   **Unix 域套接字：** 应用作为小型 HTTP 服务器运行，使用 Unix 域套接字而非传统的 localhost 端口。这利用了文件系统权限来增强安全性，并避免了端口冲突。
*   **集成 API：** 该外壳程序为应用提供了一个主屏幕，并提供 API 允许应用相互发现和交互（例如，文件管理器可以在已注册的编辑器应用中打开文本文件）。
*   **原生体验：** 通过 **Outerframe** 框架，系统同时支持标准 HTML 应用和原生的、针对平台定制的应用。作者指出，AI 辅助编程使得跨平台维护原生代码库变得切实可行，从而提供比纯 Web 工具更稳健的体验。

**意义：**
该项目旨在填补服务器管理“技术树”中的空白。通过将服务器视为“外部”图形化外壳的提供者，而不仅仅是命令行界面，Outer Shell 为远程工作创建了一个内聚的生态系统。作者已发布了关于该浏览器、Shell API 以及原生应用框架的文档，以鼓励采纳与开发。

---

## 4. 80%问题：最后的20%才是工程师曾经的战场

**原文标题**: The 80% Problem: The Last 20% Is Where the Engineer Used to Live

**原文链接**: [https://www.jonathanbeard.io/blog/2026/06/27/the-80-percent-problem.html](https://www.jonathanbeard.io/blog/2026/06/27/the-80-percent-problem.html)

This article explores the "80% problem" in the age of generative AI: while AI can rapidly produce the first 80% of a project—the scaffolding and "happy-path" logic—it consistently fails at the final 20%. This critical remainder consists of the edge cases, concurrency issues, and operational realities (like rate limiting and state corruption) that determine if a system survives in production.

The author argues that this last 20% is precisely where engineers traditionally "lived" and developed their professional judgment. By automating the "easy" 80%, we risk creating **"synthetic competence"**: output that appears polished and professional but lacks underlying understanding. This creates a dangerous gap where users become better at producing confident work but worse at identifying when that work is fundamentally flawed.

Drawing on Lisanne Bainbridge’s "Ironies of Automation," the article highlights a growing paradox: the more reliable automation becomes, the more crucial human oversight is during failures—yet the act of automating routine tasks strips humans of the very practice needed to handle those failures. Senior engineers today rely on "muscle memory" built from years of manual struggle, but the next generation may lack the opportunity to develop these "hard reps" as boilerplate tasks are automated away.

The conclusion is that the value of human experience is increasing, not decreasing. To combat skill atrophy, the industry must move beyond treating "productive struggle" as an efficiency leak. Instead, it must deliberately preserve apprenticeships, on-call rotations, and manual problem-solving as the essential curriculum for building engineers capable of managing the last 20%. The "new agile bargain" is using AI for speed while systematically staffing for the human adaptation required when that code meets reality.

---

## 5. Ornith-1.0: self-improving open-source models for agentic coding

**原文标题**: Ornith-1.0: self-improving open-source models for agentic coding

**原文链接**: [https://github.com/deepreinforce-ai/Ornith-1](https://github.com/deepreinforce-ai/Ornith-1)

生成摘要时出错

---

## 6. WATaBoy: JIT-Ing Game Boy Instructions to WASM Beats a Native Interpreter

**原文标题**: WATaBoy: JIT-Ing Game Boy Instructions to WASM Beats a Native Interpreter

**原文链接**: [https://humphri.es/blog/WATaBoy/](https://humphri.es/blog/WATaBoy/)

生成摘要时出错

---

## 7. Wallace the 6 inch f/2.8 telescope, building it, and hiking with it

**原文标题**: Wallace the 6 inch f/2.8 telescope, building it, and hiking with it

**原文链接**: [https://lucassifoni.info/blog/hiking-with-wallace/](https://lucassifoni.info/blog/hiking-with-wallace/)

生成摘要时出错

---

## 8. The Radiation Exposure Lie

**原文标题**: The Radiation Exposure Lie

**原文链接**: [https://worksinprogress.co/issue/how-to-lie-about-radiation/](https://worksinprogress.co/issue/how-to-lie-about-radiation/)

生成摘要时出错

---

## 9. US Supreme Court rules geofence warrants require constitutional protections

**原文标题**: US Supreme Court rules geofence warrants require constitutional protections

**原文链接**: [https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision)

生成摘要时出错

---

## 10. What happens when you run a CUDA kernel?

**原文标题**: What happens when you run a CUDA kernel?

**原文链接**: [https://fergusfinn.com/blog/what-happens-when-you-run-a-gpu-kernel/](https://fergusfinn.com/blog/what-happens-when-you-run-a-gpu-kernel/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 2 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 3 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 4 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 5 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 6 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 7 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 8 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 9 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 10 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 11 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 12 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 13 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 14 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 15 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 16 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 17 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 18 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 19 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 20 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 21 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 22 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 23 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 24 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 25 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 26 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 27 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 28 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 29 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 30 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 31 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 32 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 33 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 34 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 35 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 36 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 37 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 38 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 39 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 40 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 41 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 42 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 43 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 44 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 45 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 46 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 47 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 48 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 49 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 50 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 51 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 52 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 53 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 54 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 55 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 56 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 57 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 58 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 59 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 60 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 61 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 62 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 63 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 64 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 65 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 66 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 67 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 68 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 69 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 70 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 71 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 72 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 73 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 74 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 75 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 76 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 77 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 78 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 79 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 80 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 81 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 82 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 83 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 84 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 85 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 86 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 87 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 88 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 89 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 90 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 91 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 92 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 93 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 94 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 95 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 96 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 97 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 98 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 99 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 100 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 101 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 102 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 103 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 104 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 105 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 106 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 107 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 108 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 109 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 110 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 111 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 112 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 113 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 114 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 115 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 116 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 117 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 118 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 119 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 120 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 121 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 122 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 123 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 124 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 125 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 126 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 127 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 128 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 129 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 130 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 131 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 132 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 133 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 134 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 135 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 136 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 137 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 138 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 139 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 140 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 141 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 142 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 143 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 144 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 145 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 146 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 147 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 148 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 149 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 150 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 151 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 152 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 153 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 154 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 155 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 156 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 157 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 158 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 159 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 160 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 161 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 162 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 163 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 164 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 165 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 166 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 167 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 168 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 169 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 170 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 171 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 172 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 173 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 174 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 175 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 176 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 177 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 178 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 179 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 180 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 181 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 182 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 183 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 184 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 185 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 186 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 187 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 188 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 189 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 190 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 191 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 192 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 193 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 194 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 195 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 196 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 197 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 198 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 199 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 200 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 201 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 202 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 203 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 204 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 205 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 206 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 207 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 208 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 209 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 210 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 211 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 212 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 213 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 214 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 215 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 216 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 217 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 218 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 219 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 220 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 221 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 222 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 223 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 224 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 225 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 226 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 227 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 228 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 229 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 230 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 231 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 232 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 233 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 234 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 235 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 236 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 237 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 238 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 239 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 240 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 241 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 242 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 243 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 244 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 245 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 246 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 247 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 248 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 249 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 250 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 251 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 252 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 253 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 254 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 255 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 256 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 257 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 258 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 259 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 260 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 261 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 262 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 263 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 264 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 265 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 266 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 267 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 268 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 269 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 270 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 271 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 272 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 273 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 274 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 275 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 276 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 277 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 278 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 279 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 280 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 281 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 282 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 283 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 284 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 285 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 286 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 287 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 288 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 289 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 290 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 291 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 292 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 293 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 294 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 295 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 296 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 297 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 298 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 299 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 300 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 301 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 302 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 303 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 304 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 305 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 306 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 307 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 308 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 309 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 310 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 311 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 312 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 313 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 314 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 315 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 316 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 317 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 318 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 319 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 320 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 321 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 322 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 323 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 324 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 325 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 326 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 327 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 328 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 329 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 330 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 331 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 332 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 333 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 334 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 335 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 336 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 337 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 338 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 339 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 340 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 341 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 342 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 343 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 344 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 345 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 346 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 347 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 348 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 349 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 350 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 351 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 352 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 353 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 354 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 355 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 356 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 357 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 358 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 359 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 360 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 361 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 362 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 363 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 364 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 365 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 366 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 367 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 368 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 369 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 370 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 371 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 372 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 373 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 374 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 375 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 376 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 377 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 378 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 379 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 380 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 381 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 382 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 383 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 384 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 385 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 386 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 387 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 388 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 389 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 390 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 391 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 392 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 393 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 394 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 395 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 396 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 397 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 398 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 399 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 400 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 401 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 402 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 403 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 404 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 405 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 406 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 407 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 408 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 409 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 410 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 411 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 412 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 413 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 414 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 415 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 416 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 417 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 418 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 419 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 420 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 421 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 422 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 423 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 424 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 425 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 426 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 427 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 428 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 429 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 430 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 431 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 432 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 433 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 434 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 435 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 436 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 437 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 438 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 439 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 440 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 441 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 442 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 443 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 444 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 445 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 446 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 447 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 448 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 449 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 450 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 451 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 452 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 453 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 454 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 455 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 456 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 457 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 458 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 459 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 460 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 461 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 462 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 463 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 464 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 465 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 466 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
