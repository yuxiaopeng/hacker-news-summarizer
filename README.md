# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-23.md)

*最后自动更新时间: 2026-04-23 18:31:19*
## 1. Bitwarden CLI 在持续进行的 Checkmarx 供应链攻击中遭到入侵

**原文标题**: Bitwarden CLI Compromised in Ongoing Checkmarx Supply Chain Campaign

**原文链接**: [https://socket.dev/blog/bitwarden-cli-compromised](https://socket.dev/blog/bitwarden-cli-compromised)

**摘要**

来自 Socket 和 Docker 的安全研究人员发现了一起涉及 Bitwarden CLI 和官方 Checkmarx KICS（Keeping Infrastructure as Code Secure）制品的重大供应链入侵事件。

据报告，在官方 Docker 仓库中发现了 Checkmarx KICS 镜像的恶意版本。此外，研究人员还在相关的代码扩展中检测到了可疑的发布版本。此次入侵被描述为一场更广泛、持续进行的供应链攻击活动的一部分，旨在向受信任的开发工具和官方分发渠道植入恶意代码。

这一发现凸显了攻击者正通过复杂的手段，瞄准开发人员和 IT 专业人员所使用的基础设施即代码 (IaC) 安全工具及命令行界面。建议使用 Bitwarden CLI 或 KICS Docker 镜像的机构对其环境进行审计，检查是否存在未经授权的修改，并验证当前安装程序的完整性。

---

## 2. 关于近期 Claude Code 质量报告的更新

**原文标题**: An update on recent Claude Code quality reports

**原文链接**: [https://www.anthropic.com/engineering/april-23-postmortem](https://www.anthropic.com/engineering/april-23-postmortem)

Anthropic 近期针对 Claude Code、Claude Agent SDK 和 Claude Cowork 性能下降的相关报告做出了回应。调查发现，用户感知的性能问题并非由模型范围内的整体退步引起，而是由三项特定的变更导致的。标准 API 未受影响。

这三项已确认的问题如下：
1.  **推理力度变更（3 月 4 日）：** Anthropic 为了降低延迟，将默认推理力度从“高”下调至“中”。在用户反馈智能水平下降后，该变更于 4 月 7 日被撤销，默认恢复为高/超高推理力度。
2.  **缓存 Bug（3 月 26 日）：** 一项旨在清除空闲会话中“思考”令牌（thinking tokens）的优化措施存在 Bug，导致每一轮对话都会清除历史记录。这导致模型变得健忘且重复，并加速了使用额度的消耗。该问题已于 4 月 10 日修复。
3.  **字数限制（4 月 16 日）：** 一项旨在限制回复字数的系统提示词变更无意中损害了编码质量。该变更于 4 月 20 日被撤销。

由于这些变更发生的时间不同且影响的用户群体各异，其累积效应呈现为不连续的性能退化。

**解决方案与未来防范措施：**
所有问题均已在 4 月 20 日（v2.1.116 版本）前得到解决。为了补偿用户的不佳体验，Anthropic 已于 4 月 23 日重置了所有订阅者的使用限额。

为防止未来再次出现性能倒退，公司正在实施更严格的协议，包括：
*   针对每次系统提示词变更运行更广泛的评估套件和“消融实验”。
*   确保内部员工“试用（dogfood）”与公开发布版完全一致的 Claude Code。
*   使用由 Opus 4.7 驱动的改进版内部代码审查工具。
*   针对任何权衡速度与智能的更新，实施“观察期”和逐步推广机制。

---

## 3. 'Hairdryer used to trick weather sensor' to win $34,000 Polymarket bet

**原文标题**: 'Hairdryer used to trick weather sensor' to win $34,000 Polymarket bet

**原文链接**: [https://www.telegraph.co.uk/business/2026/04/23/hairdryer-used-trick-weather-sensor-34000-polymarket-bet/](https://www.telegraph.co.uk/business/2026/04/23/hairdryer-used-trick-weather-sensor-34000-polymarket-bet/)

生成摘要时出错

---

## 4. 隆重推出 GPT-5.5

**原文标题**: Introducing GPT-5.5

**原文链接**: [https://openai.com/index/introducing-gpt-5-5/](https://openai.com/index/introducing-gpt-5-5/)

无法访问文章链接。

---

## 5. 法国政府机构确认发生数据泄露，黑客正兜售相关数据。

**原文标题**: French government agency confirms breach as hacker offers to sell data

**原文链接**: [https://www.bleepingcomputer.com/news/security/french-govt-agency-confirms-breach-as-hacker-offers-to-sell-data/](https://www.bleepingcomputer.com/news/security/french-govt-agency-confirms-breach-as-hacker-offers-to-sell-data/)

On April 15, 2026, the French government agency **France Titres** (also known as **ANTS**) confirmed a security breach affecting its user portal, *ants.gouv.fr*. ANTS is the administrative body responsible for issuing official identity documents, including passports, driver’s licenses, and national ID cards.

**Key details of the breach include:**
*   **Data Exposed:** The compromised information includes login IDs, full names, email addresses, dates and places of birth, unique account identifiers, and, for some individuals, postal addresses and phone numbers. 
*   **Scope of the Attack:** While the agency did not specify the number of victims, a threat actor using the alias **“breach3d”** claimed on hacker forums to have stolen **19 million records**. This data is currently being offered for sale.
*   **Security Risks:** ANTS stated that the stolen data does not grant unauthorized access to its electronic portals. However, officials warned that the information is highly valuable for phishing and social engineering attacks.
*   **Official Response:** The agency has notified the French data protection authority (CNIL), the national cybersecurity agency (ANSSI), and the Paris Public Prosecutor. They are currently in the process of notifying impacted individuals.

**Guidance for Users:**
ANTS advises users that no immediate technical action is required. However, they are urged to exercise **extreme caution** and remain vigilant against suspicious emails, SMS messages, or phone calls that appear to originate from the agency, as these may be fraudulent attempts to exploit the leaked data.

---

## 6. MeshCore development team splits over trademark dispute and AI-generated code

**原文标题**: MeshCore development team splits over trademark dispute and AI-generated code

**原文链接**: [https://blog.meshcore.io/2026/04/23/the-split](https://blog.meshcore.io/2026/04/23/the-split)

生成摘要时出错

---

## 7. 多个 GitHub 服务故障

**原文标题**: Incident with Multple GitHub Services

**原文链接**: [https://www.githubstatus.com/incidents/myrbk7jvvs6p](https://www.githubstatus.com/incidents/myrbk7jvvs6p)

2026年4月23日，GitHub 遭遇了一次服务中断，影响了三个主要组件：**Actions、Copilot 和 Webhooks**。

该事件始于 UTC 时间 16:12，最初有报告称 Copilot 和 Webhooks 的可用性下降。在 20 分钟内，影响范围进一步扩大，其他几项服务也相继不可用，同时 GitHub Actions 开始出现性能问题。

GitHub 工程师在 UTC 16:52 确定了问题的根本原因，并立即开始采取缓解措施。恢复工作进展迅速：
*   **UTC 17:03：** Actions 和 Copilot 服务故障得到缓解。
*   **UTC 17:10：** Webhooks 恢复正常运行状态。
*   **UTC 17:30：** 该事件被正式宣布已解决。

整个中断过程持续了约 78 分钟。GitHub 已恢复所有受影响服务的全部功能，并承诺在报告最终完成后，提供一份详细的根本原因分析 (RCA) 以解释此次故障。

---

## 8. 一款真正可以佩戴的DIY手表

**原文标题**: A DIY Watch You Can Actually Wear

**原文链接**: [https://www.hackster.io/news/a-diy-watch-you-can-actually-wear-8f91c2dac682](https://www.hackster.io/news/a-diy-watch-you-can-actually-wear-8f91c2dac682)

LILYGO 推出了 **T-Watch Ultra**，这是一款坚固耐用的 DIY 智能手表，旨在填补爱好者硬件与商用级耐用性之间的空白。大多数自制手表在恶劣环境下都比较脆弱，而 T-Watch Ultra 采用了 **IP65 级外壳**，具备防雨、防尘和防溅性能，非常适合日常佩戴。

在核心配置上，该设备搭载了 **ESP32-S3 双核处理器**，拥有 16MB Flash 和 8MB PSRAM，为复杂应用和边缘 AI 任务提供了充足的内存。它配备了一块清晰的 2.01 英寸 AMOLED 触摸屏，并升级了 1,100mAh 电池以提升续航时间。

该手表的亮点在于其多样化的连接方式和传感器套件，包括：
*   **LoRa 收发器：** 采用 Semtech SX1262，支持远距离、离网通信（是 Meshtastic 节点的理想选择）。
*   **GNSS 与 NFC：** 搭载 u-blox 模块用于精确位置追踪，以及 ST25R3916 芯片支持 NFC 功能。
*   **高级传感器：** 配备博世 BHI260AP 智能传感器以支持基于运动的 AI 功能，并内置麦克风。
*   **可扩展性：** 包含一个 microSD 卡槽和一个用于充电及编程的 USB Type-C 接口。

T-Watch Ultra 专为硬件极客设计，支持 **Arduino IDE、MicroPython 和 ESP-IDF** 等开放开发平台，避开了“围墙花园”的限制。这允许用户构建完全自定义的固件和应用程序。该设备目前已开启预售，价格为 **78.32 美元**。

---

## 9. 我正在构建云。

**原文标题**: I am building a cloud

**原文链接**: [https://crawshaw.io/blog/building-a-cloud](https://crawshaw.io/blog/building-a-cloud)

生成摘要时出错

---

## 10. Show HN: Honker – Postgres NOTIFY/LISTEN Semantics for SQLite

**原文标题**: Show HN: Honker – Postgres NOTIFY/LISTEN Semantics for SQLite

**原文链接**: [https://github.com/russellromney/honker](https://github.com/russellromney/honker)

**Honker** is a SQLite extension and set of language bindings (including Python, Node.js, Rust, Go, and Ruby) that brings Postgres-style `NOTIFY/LISTEN` semantics to SQLite. It enables durable pub/sub, task queues, and event streams without the need for an external broker like Redis or a background daemon.

The project’s core philosophy is that if SQLite is the primary datastore, the queue should live in the same file. This ensures **transactional atomicity**: business writes and task enqueuing occur within the same transaction. If a transaction rolls back, both the data change and the queued task are dropped, effectively solving the "dual-write" problem.

**Technical Implementation:**
Honker achieves high-performance push semantics by monitoring SQLite's **Write-Ahead Log (WAL)** file. Instead of expensive polling queries, it uses a background thread to watch for file-system changes (`stat(2)`). When a commit occurs, Honker wakes listeners across processes with single-digit millisecond latency. Because it relies on WAL mode, it supports concurrent readers and writers without blocking.

**Key Features:**
*   **Work Queues:** At-least-once delivery with retries, priorities, delayed jobs, and dead-letter tables.
*   **Durable Streams:** Event logging with per-consumer offsets for reliable replay.
*   **Ephemeral Pub/Sub:** Lightweight notifications for immediate cross-process signaling.
*   **Built-in Tools:** Support for cron-style periodic tasks, rate-limiting, and named locks.
*   **Language Interoperability:** Since it is a loadable SQLite extension, any language can interact with the same underlying tables and logic.

Honker is currently experimental. It is designed for applications where SQLite is the primary database and developers want to simplify their stack by eliminating the operational overhead of a separate message broker.

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 2 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 3 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 4 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 5 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 6 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 7 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 8 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 9 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 10 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 11 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 12 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 13 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 14 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 15 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 16 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 17 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 18 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 19 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 20 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 21 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 22 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 23 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 24 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 25 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 26 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 27 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 28 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 29 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 30 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 31 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 32 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 33 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 34 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 35 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 36 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 37 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 38 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 39 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 40 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 41 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 42 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 43 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 44 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 45 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 46 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 47 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 48 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 49 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 50 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 51 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 52 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 53 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 54 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 55 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 56 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 57 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 58 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 59 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 60 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 61 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 62 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 63 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 64 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 65 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 66 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 67 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 68 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 69 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 70 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 71 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 72 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 73 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 74 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 75 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 76 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 77 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 78 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 79 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 80 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 81 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 82 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 83 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 84 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 85 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 86 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 87 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 88 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 89 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 90 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 91 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 92 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 93 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 94 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 95 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 96 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 97 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 98 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 99 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 100 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 101 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 102 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 103 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 104 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 105 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 106 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 107 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 108 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 109 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 110 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 111 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 112 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 113 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 114 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 115 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 116 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 117 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 118 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 119 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 120 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 121 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 122 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 123 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 124 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 125 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 126 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 127 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 128 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 129 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 130 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 131 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 132 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 133 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 134 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 135 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 136 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 137 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 138 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 139 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 140 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 141 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 142 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 143 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 144 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 145 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 146 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 147 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 148 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 149 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 150 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 151 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 152 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 153 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 154 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 155 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 156 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 157 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 158 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 159 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 160 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 161 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 162 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 163 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 164 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 165 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 166 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 167 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 168 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 169 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 170 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 171 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 172 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 173 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 174 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 175 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 176 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 177 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 178 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 179 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 180 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 181 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 182 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 183 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 184 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 185 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 186 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 187 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 188 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 189 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 190 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 191 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 192 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 193 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 194 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 195 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 196 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 197 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 198 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 199 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 200 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 201 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 202 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 203 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 204 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 205 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 206 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 207 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 208 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 209 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 210 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 211 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 212 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 213 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 214 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 215 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 216 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 217 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 218 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 219 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 220 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 221 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 222 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 223 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 224 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 225 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 226 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 227 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 228 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 229 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 230 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 231 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 232 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 233 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 234 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 235 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 236 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 237 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 238 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 239 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 240 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 241 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 242 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 243 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 244 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 245 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 246 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 247 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 248 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 249 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 250 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 251 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 252 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 253 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 254 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 255 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 256 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 257 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 258 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 259 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 260 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 261 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 262 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 263 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 264 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 265 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 266 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 267 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 268 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 269 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 270 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 271 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 272 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 273 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 274 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 275 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 276 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 277 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 278 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 279 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 280 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 281 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 282 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 283 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 284 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 285 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 286 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 287 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 288 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 289 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 290 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 291 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 292 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 293 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 294 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 295 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 296 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 297 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 298 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 299 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 300 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 301 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 302 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 303 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 304 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 305 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 306 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 307 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 308 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 309 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 310 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 311 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 312 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 313 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 314 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 315 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 316 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 317 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 318 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 319 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 320 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 321 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 322 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 323 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 324 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 325 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 326 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 327 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 328 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 329 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 330 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 331 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 332 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 333 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 334 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 335 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 336 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 337 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 338 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 339 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 340 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 341 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 342 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 343 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 344 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 345 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 346 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 347 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 348 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 349 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 350 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 351 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 352 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 353 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 354 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 355 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 356 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 357 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 358 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 359 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 360 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 361 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 362 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 363 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 364 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 365 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 366 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 367 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 368 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 369 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 370 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 371 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 372 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 373 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 374 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 375 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 376 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 377 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 378 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 379 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 380 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 381 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 382 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 383 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 384 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 385 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 386 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 387 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 388 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 389 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 390 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 391 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 392 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 393 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 394 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 395 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 396 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 397 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 398 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 399 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
