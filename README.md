# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-05-28.md)

*最后自动更新时间: 2026-05-28 20:04:30*
## 1. Claude Opus 4.8

**原文标题**: Claude Opus 4.8

**原文链接**: [https://www.anthropic.com/news/claude-opus-4-8](https://www.anthropic.com/news/claude-opus-4-8)

Anthropic 宣布发布 **Claude Opus 4.8**。这款升级后的模型旨在增强可靠性、提升判断力，并在代理任务（agentic tasks）中表现出卓越性能。Opus 4.8 自 2026 年 5 月 28 日起上线，在编程、法律分析和计算机操作等关键基准测试中，其表现优于其前代产品以及 GPT-5.5 等竞争对手。

**模型关键改进：**
*   **可靠性与诚实度：** 该模型忽略代码缺陷的可能性仅为 Opus 4.7 的四分之一，并且在标记不确定性或输入错误方面表现得更加积极主动。
*   **性能表现：** 它在法律代理基准测试（Legal Agent Benchmark）中刷新了纪录，并在复杂的工具调用中表现出色，完成端到端任务所需的步骤更少。
*   **对齐性：** 安全评估显示，其亲社会特性有所提升，且欺骗等违背对齐原则的行为显著减少。

**新功能：**
*   **精力控制（Effort Control）：** claude.ai 和 Cowork 用户现在可以手动调节 Claude 的“思考”深度，在快速响应或深度推理之间进行选择。
*   **动态工作流：** 这是 Claude Code 中的一项研究预览功能，允许模型编排数百个并行子代理来处理大规模项目（如海量代码库迁移）。
*   **快速模式（Fast Mode）：** 该模式的运行速度提升至 2.5 倍，且成本比之前版本降低了三分之二。

**定价与未来展望：**
标准定价保持不变，仍为每百万输入 Token 5 美元，每百万输出 Token 25 美元。Anthropic 同时预告了 **Project Glasswing**，这是即将推出的“Mythos”级别模型系列，具备更高的智能水平，目前正在进行网络安全测试。

在发布模型的同时，Anthropic 宣布完成了 **650 亿美元的 H 轮融资**（公司估值达 9650 亿美元），并将在米兰和首尔开设新的国际办事处。

---

## 2. 仅需使用 Postgres 实现持久化工作流

**原文标题**: Just Use Postgres for Durable Workflows

**原文链接**: [https://www.dbos.dev/blog/postgres-is-all-you-need-for-durable-execution](https://www.dbos.dev/blog/postgres-is-all-you-need-for-durable-execution)

《直接在 Postgres 上实现持久化工作流》一文指出，传统的持久化工作流系统（依赖于 Temporal 或 AWS Step Functions 等外部编排器）过于复杂。相反，作者建议直接将 **Postgres** 作为编排器，从而构建更简单、更高效且更可靠的系统。

**关键概念：**
*   **持久化工作流 (Durable Workflows)：** 定期将进度“检查点”保存到数据库的程序。如果发生崩溃，程序可以“重新加载”并从上一个完成的步骤恢复运行。
*   **Postgres 方案：** 应用程序的工作节点不再使用中心化编排器服务器，而是通过轮询 Postgres 表来提取任务。它们利用锁定和完整性约束等原生数据库特性来协调执行，并将结果直接作为检查点存入数据库。

**主要优势：**
1.  **可扩展性与可用性：** 系统性能与数据库挂钩，可通过纵向扩展或横向扩展（通过分片或分布式 Postgres）提升。高可用性则通过成熟的 Postgres 复制和故障转移机制来实现。
2.  **可观测性：** 由于工作流状态存储在关系型表中，开发人员可以使用标准 SQL 实时监控、过滤和分析工作流执行情况，无需专用工具。
3.  **安全性与可靠性：** 外部编排器会引入额外的故障点和安全风险。通过使用 Postgres，应用程序可以复用现有的核心基础设施，从而减少攻击面并降低架构复杂度。

文章总结道，对于已经在使用 Postgres 的团队来说，利用其进行持久化执行可以消除对冗余基础设施的需求，同时提供与专用编排平台相同的稳健恢复保障。作者所在的 DBOS 公司旨在提供相关工具，使这种基于 Postgres 的模式更易于实现。

---

## 3. 关于 Zig Days 上的大语言模型

**原文标题**: About LLMs at Zig Days

**原文链接**: [https://kristoff.it/blog/llms-at-zig-days/](https://kristoff.it/blog/llms-at-zig-days/)

在《关于 Zig Days 中的大语言模型》一文中，Loris Cro 探讨了大语言模型（LLM）对 Zig 社区聚会的影响，并主张保留这些活动以人为本的特质。Zig Days 是协作式的编程环节，旨在培养“系统级思维”以及对严谨软件工程的深刻理解。

Cro 表示担心，目前关于 LLM 的讨论正在“耗尽房间里的空气”，挤占了关于数据结构、算法和手动解决问题等有价值的讨论空间。为了应对这一趋势，他提出了三项主要建议：

1. **限制关于 LLM 的讨论：** 参与者应专注于分享在 AI 驱动的对话中无法获取的技术见解和独特方法。
2. **优先考虑人际互动：** 遇到困难时，鼓励与会者咨询同伴而非“询问 AI”，这有助于建立社区感并减少职业孤独感。
3. **亲手编写代码：** Cro 认为，使用 AI 代理来“堆砌”代码会剥夺开发者关键的学习机会。他强调，无论行业自动化趋势如何，Zig Days 都应始终是那些热爱编程手艺的人们的乐土。

对于组织者，Cro 建议在活动开始时说明这些要点。他并不主张全面禁止，而是建议鼓励参与者共同守护活动的独特性：即深度实践学习和真实人际连接的机会。总之，这篇文章呼吁在日益自动化的领域中，将 Zig Days 打造为一处坚守工匠精神和系统级理解的净土。

---

## 4. Show HN: Continue? Y/N: 一款关于 AI 智能体权限疲劳的 60 秒游戏

**原文标题**: Show HN: Continue? Y/N: A 60-second game about AI agent permission fatigue

**原文链接**: [https://llmgame.scalex.dev](https://llmgame.scalex.dev)

**Continue? Y/N** 是一款时长 60 秒的简短互动游戏，旨在展示 AI 智能体背景下的“许可疲劳”（permission fatigue）概念。作为“Show HN”项目发布，该游戏要求玩家在短时间内快速审核并批准或拒绝一系列接踵而至的 AI 生成指令。

该项目探讨了随着 AI 智能体变得更加自主并深度融入日常工作流程，由此产生的安全风险和行为习惯。由于这些系统会频繁提示用户授权执行任务，海量的请求会导致“疲劳”。这往往导致用户在未仔细阅读指令潜在后果的情况下，便反射性地点击“是”或“继续”。

通过将这一过程游戏化，创作者迫使玩家直面一个事实：当监管变成一种无意识的习惯时，危险或非预期的操作（如删除敏感数据或授予未授权访问）极易获得批准。最终，这款游戏凸显了便利与安全之间的张力，并对随着 AI 系统日益复杂和持久，人工介入（human-in-the-loop）安全机制的有效性提出了质疑。

---

## 5. 永久性上牙冠

**原文标题**: The Permanent Upper Crow

**原文链接**: [https://permanent-upper-crow.jasonwu.ink/](https://permanent-upper-crow.jasonwu.ink/)

看来除了标题《永恒的上克罗》（The Permanent Upper Crow）之外，您的请求中并未包含文章的具体内容。为了提供一份准确、简明且涵盖主要观点和关键信息的摘要，我需要文章的全文。请在此粘贴文章内容，我很乐意为您提供 300 字以内的摘要。

---

## 6. 基于 OpenWRT 的室内 Wi-Fi 漫游

**原文标题**: Indoor Wi-Fi Roaming with OpenWRT

**原文链接**: [https://taoofmac.com/space/blog/2026/05/26/1730](https://taoofmac.com/space/blog/2026/05/26/1730)

本文详细介绍了如何针对运行 OpenWRT 的 Cudy AX3000 接入点进行家庭网络 Wi-Fi 漫游优化。尽管已经拥有强大的回程连接并启用了基础的 802.11r/k/v 设置，作者发现移动设备（尤其是苹果产品）仍存在“粘性”问题，即宁愿连接信号极差的远处接入点，也不愿切换到更近的设备。

为了解决这一问题，作者实施了两个主要的扩展技术方案：

1.  **usteer：** 作者安装了 `usteer` 引导守护进程。这使得各个接入点能够相互通信并共享客户端数据，协助网络协调并将客户端引导至最合适的射频频段。
2.  **静态邻居报告：** 作者发现 `hostapd` 未能正确填充 802.11k 邻居报告。通过安装 `static-neighbor-reports` 软件包，作者手动生成了特定频段的邻居列表。这确保了 5GHz 频段仅通告其他 5GHz 邻居，从而维持了作者有意划分的旧版 2.4GHz (WPA2) 与现代 5GHz (WPA3) SSID 布局。

**主要成效：**
*   **消除粘性客户端：** 数据分析显示，信号“极弱”（约 -90dBm）的关联已消失，表明客户端现在能够成功漫游到更近的接入点。
*   **性能提升：** 尽管 2.4GHz 频段仍因环境拥塞而存在噪声，但 5GHz 的比特率和连接稳定性得到了显著改善。
*   **透明度：** 作者强调了基于 OpenWRT 的“哑 AP (dumb AP)”架构的优势，它避开了云端管理和私有软件，实现了本地化控制和可审计的日志记录。

最终，通过引导守护进程与手动邻居报告的结合，在无需统一 SSID 或云控制器的情况下，实现了无缝的漫游体验。

---

## 7. News about Raspberry Pi 6 and Microcontroller Development

**原文标题**: News about Raspberry Pi 6 and Microcontroller Development

**原文链接**: [https://www.jeffgeerling.com/blog/2026/news-about-raspberry-pi-6-and-microcontroller-development/](https://www.jeffgeerling.com/blog/2026/news-about-raspberry-pi-6-and-microcontroller-development/)

生成摘要时出错

---

## 8. Bitburner, programming-based incremental game

**原文标题**: Bitburner, programming-based incremental game

**原文链接**: [https://bitburner-official.github.io/](https://bitburner-official.github.io/)

生成摘要时出错

---

## 9. Show HN: Ktx – Open-source executable context layer for data agents

**原文标题**: Show HN: Ktx – Open-source executable context layer for data agents

**原文链接**: [https://github.com/Kaelio/ktx](https://github.com/Kaelio/ktx)

生成摘要时出错

---

## 10. I hated writing–until I learned there's a science to it(2024)

**原文标题**: I hated writing–until I learned there's a science to it(2024)

**原文链接**: [https://www.science.org/content/article/i-hated-writing-until-i-learned-there-s-science-it](https://www.science.org/content/article/i-hated-writing-until-i-learned-there-s-science-it)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 2 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 3 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 4 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 5 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 6 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 7 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 8 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 9 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 10 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 11 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 12 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 13 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 14 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 15 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 16 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 17 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 18 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 19 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 20 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 21 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 22 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 23 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 24 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 25 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 26 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 27 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 28 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 29 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 30 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 31 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 32 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 33 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 34 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 35 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 36 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 37 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 38 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 39 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 40 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 41 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 42 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 43 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 44 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 45 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 46 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 47 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 48 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 49 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 50 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 51 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 52 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 53 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 54 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 55 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 56 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 57 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 58 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 59 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 60 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 61 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 62 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 63 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 64 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 65 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 66 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 67 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 68 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 69 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 70 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 71 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 72 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 73 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 74 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 75 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 76 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 77 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 78 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 79 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 80 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 81 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 82 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 83 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 84 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 85 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 86 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 87 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 88 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 89 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 90 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 91 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 92 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 93 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 94 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 95 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 96 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 97 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 98 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 99 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 100 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 101 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 102 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 103 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 104 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 105 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 106 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 107 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 108 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 109 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 110 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 111 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 112 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 113 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 114 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 115 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 116 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 117 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 118 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 119 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 120 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 121 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 122 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 123 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 124 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 125 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 126 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 127 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 128 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 129 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 130 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 131 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 132 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 133 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 134 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 135 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 136 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 137 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 138 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 139 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 140 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 141 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 142 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 143 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 144 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 145 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 146 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 147 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 148 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 149 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 150 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 151 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 152 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 153 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 154 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 155 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 156 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 157 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 158 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 159 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 160 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 161 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 162 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 163 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 164 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 165 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 166 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 167 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 168 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 169 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 170 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 171 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 172 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 173 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 174 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 175 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 176 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 177 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 178 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 179 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 180 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 181 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 182 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 183 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 184 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 185 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 186 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 187 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 188 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 189 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 190 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 191 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 192 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 193 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 194 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 195 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 196 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 197 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 198 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 199 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 200 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 201 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 202 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 203 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 204 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 205 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 206 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 207 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 208 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 209 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 210 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 211 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 212 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 213 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 214 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 215 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 216 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 217 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 218 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 219 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 220 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 221 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 222 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 223 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 224 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 225 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 226 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 227 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 228 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 229 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 230 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 231 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 232 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 233 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 234 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 235 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 236 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 237 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 238 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 239 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 240 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 241 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 242 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 243 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 244 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 245 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 246 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 247 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 248 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 249 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 250 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 251 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 252 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 253 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 254 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 255 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 256 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 257 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 258 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 259 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 260 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 261 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 262 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 263 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 264 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 265 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 266 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 267 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 268 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 269 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 270 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 271 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 272 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 273 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 274 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 275 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 276 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 277 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 278 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 279 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 280 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 281 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 282 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 283 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 284 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 285 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 286 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 287 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 288 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 289 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 290 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 291 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 292 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 293 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 294 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 295 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 296 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 297 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 298 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 299 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 300 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 301 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 302 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 303 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 304 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 305 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 306 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 307 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 308 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 309 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 310 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 311 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 312 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 313 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 314 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 315 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 316 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 317 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 318 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 319 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 320 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 321 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 322 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 323 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 324 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 325 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 326 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 327 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 328 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 329 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 330 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 331 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 332 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 333 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 334 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 335 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 336 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 337 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 338 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 339 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 340 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 341 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 342 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 343 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 344 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 345 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 346 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 347 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 348 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 349 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 350 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 351 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 352 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 353 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 354 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 355 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 356 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 357 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 358 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 359 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 360 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 361 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 362 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 363 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 364 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 365 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 366 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 367 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 368 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 369 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 370 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 371 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 372 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 373 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 374 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 375 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 376 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 377 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 378 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 379 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 380 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 381 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 382 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 383 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 384 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 385 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 386 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 387 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 388 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 389 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 390 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 391 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 392 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 393 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 394 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 395 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 396 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 397 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 398 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 399 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 400 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 401 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 402 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 403 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 404 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 405 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 406 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 407 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 408 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 409 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 410 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 411 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 412 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 413 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 414 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 415 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 416 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 417 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 418 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 419 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 420 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 421 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 422 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 423 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 424 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 425 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 426 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 427 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 428 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 429 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 430 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 431 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 432 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 433 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 434 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
