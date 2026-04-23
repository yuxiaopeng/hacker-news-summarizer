# Hacker News 热门文章摘要 (2026-04-23)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Alberta startup sells no-tech tractors for half price

**原文标题**: Alberta startup sells no-tech tractors for half price

**原文链接**: [https://wheelfront.com/this-alberta-startup-sells-no-tech-tractors-for-half-price/](https://wheelfront.com/this-alberta-startup-sells-no-tech-tractors-for-half-price/)

生成摘要时出错

---

## 12. Your hex editor should color-code bytes

**原文标题**: Your hex editor should color-code bytes

**原文链接**: [https://simonomi.dev/blog/color-code-your-bytes/](https://simonomi.dev/blog/color-code-your-bytes/)

生成摘要时出错

---

## 13. The Ferrari of Espresso Machines Is Fueling a Hot Resale Market

**原文标题**: The Ferrari of Espresso Machines Is Fueling a Hot Resale Market

**原文链接**: [https://www.nytimes.com/2026/04/20/dining/la-marzocco-espresso-machine.html](https://www.nytimes.com/2026/04/20/dining/la-marzocco-espresso-machine.html)

生成摘要时出错

---

## 14. To Protect and Swerve: NYPD Cop Has 547 Speeding Tickets

**原文标题**: To Protect and Swerve: NYPD Cop Has 547 Speeding Tickets

**原文链接**: [https://nyc.streetsblog.org/2026/04/23/to-protect-and-swerve-nypd-cop-has-527-speeding-tickets-yet-remains-on-the-force](https://nyc.streetsblog.org/2026/04/23/to-protect-and-swerve-nypd-cop-has-527-speeding-tickets-yet-remains-on-the-force)

生成摘要时出错

---

## 15. Apple fixes bug that cops used to extract deleted chat messages from iPhones

**原文标题**: Apple fixes bug that cops used to extract deleted chat messages from iPhones

**原文链接**: [https://techcrunch.com/2026/04/22/apple-fixes-bug-that-cops-used-to-extract-deleted-chat-messages-from-iphones/](https://techcrunch.com/2026/04/22/apple-fixes-bug-that-cops-used-to-extract-deleted-chat-messages-from-iphones/)

生成摘要时出错

---

## 16. If America's so rich, how'd it get so sad?

**原文标题**: If America's so rich, how'd it get so sad?

**原文链接**: [https://www.derekthompson.org/p/if-americas-so-rich-howd-it-get-so](https://www.derekthompson.org/p/if-americas-so-rich-howd-it-get-so)

生成摘要时出错

---

## 17. Palantir Employees Are Starting to Wonder If They're the Bad Guys

**原文标题**: Palantir Employees Are Starting to Wonder If They're the Bad Guys

**原文链接**: [https://www.wired.com/story/palantir-employees-are-starting-to-wonder-if-theyre-the-bad-guys/](https://www.wired.com/story/palantir-employees-are-starting-to-wonder-if-theyre-the-bad-guys/)

生成摘要时出错

---

## 18. Jiga (YC W21) Is Hiring

**原文标题**: Jiga (YC W21) Is Hiring

**原文链接**: [https://jiga.io/about-us/](https://jiga.io/about-us/)

生成摘要时出错

---

## 19. Writing a C Compiler, in Zig (2025)

**原文标题**: Writing a C Compiler, in Zig (2025)

**原文链接**: [https://ar-ms.me/thoughts/c-compiler-1-zig/](https://ar-ms.me/thoughts/c-compiler-1-zig/)

生成摘要时出错

---

## 20. Investigation uncovers two sophisticated telecom surveillance campaigns

**原文标题**: Investigation uncovers two sophisticated telecom surveillance campaigns

**原文链接**: [https://techcrunch.com/2026/04/23/surveillance-vendors-caught-abusing-access-to-telcos-to-track-peoples-phone-locations-researchers-say/](https://techcrunch.com/2026/04/23/surveillance-vendors-caught-abusing-access-to-telcos-to-track-peoples-phone-locations-researchers-say/)

生成摘要时出错

---

## 21. We found a stable Firefox identifier linking all your private Tor identities

**原文标题**: We found a stable Firefox identifier linking all your private Tor identities

**原文链接**: [https://fingerprint.com/blog/firefox-tor-indexeddb-privacy-vulnerability/](https://fingerprint.com/blog/firefox-tor-indexeddb-privacy-vulnerability/)

生成摘要时出错

---

## 22. A Renaissance gambling dispute spawned probability theory

**原文标题**: A Renaissance gambling dispute spawned probability theory

**原文链接**: [https://www.scientificamerican.com/article/how-a-renaissance-gambling-dispute-spawned-probability-theory/](https://www.scientificamerican.com/article/how-a-renaissance-gambling-dispute-spawned-probability-theory/)

生成摘要时出错

---

## 23. Arch Linux Now Has a Bit-for-Bit Reproducible Docker Image

**原文标题**: Arch Linux Now Has a Bit-for-Bit Reproducible Docker Image

**原文链接**: [https://antiz.fr/blog/archlinux-now-has-a-reproducible-docker-image/](https://antiz.fr/blog/archlinux-now-has-a-reproducible-docker-image/)

生成摘要时出错

---

## 24. 5x5 Pixel font for tiny screens

**原文标题**: 5x5 Pixel font for tiny screens

**原文链接**: [https://maurycyz.com/projects/mcufont/](https://maurycyz.com/projects/mcufont/)

生成摘要时出错

---

## 25. Isopods of the world

**原文标题**: Isopods of the world

**原文链接**: [https://isopod.site/](https://isopod.site/)

生成摘要时出错

---

## 26. People Do Not Yearn for Automation

**原文标题**: People Do Not Yearn for Automation

**原文链接**: [https://www.theverge.com/podcast/917029/software-brain-ai-backlash-databases-automation](https://www.theverge.com/podcast/917029/software-brain-ai-backlash-databases-automation)

生成摘要时出错

---

## 27. A History of Erasures Learning to Write Like Leylâ Erbil

**原文标题**: A History of Erasures Learning to Write Like Leylâ Erbil

**原文链接**: [https://thepointmag.com/criticism/a-history-of-erasures/](https://thepointmag.com/criticism/a-history-of-erasures/)

生成摘要时出错

---

## 28. Our newsroom AI policy

**原文标题**: Our newsroom AI policy

**原文链接**: [https://arstechnica.com/staff/2026/04/our-newsroom-ai-policy/](https://arstechnica.com/staff/2026/04/our-newsroom-ai-policy/)

生成摘要时出错

---

## 29. X is shutting down Communities because of low usage and lots of spam

**原文标题**: X is shutting down Communities because of low usage and lots of spam

**原文链接**: [https://techcrunch.com/2026/04/23/x-is-shutting-down-communities-because-of-low-usage-and-lots-of-spam/](https://techcrunch.com/2026/04/23/x-is-shutting-down-communities-because-of-low-usage-and-lots-of-spam/)

生成摘要时出错

---

## 30. Raylib v6.0

**原文标题**: Raylib v6.0

**原文链接**: [https://github.com/raysan5/raylib/releases/tag/6.0](https://github.com/raysan5/raylib/releases/tag/6.0)

生成摘要时出错

---

## 31. A True Life Hack: What Physical 'Life Force' Turns Biology's Wheels?

**原文标题**: A True Life Hack: What Physical 'Life Force' Turns Biology's Wheels?

**原文链接**: [https://www.quantamagazine.org/what-physical-life-force-turns-biologys-wheels-20260420/](https://www.quantamagazine.org/what-physical-life-force-turns-biologys-wheels-20260420/)

生成摘要时出错

---

## 32. An amateur historian's favorite books about the Silk Road

**原文标题**: An amateur historian's favorite books about the Silk Road

**原文链接**: [https://bookdna.com/best-books/silk-road](https://bookdna.com/best-books/silk-road)

生成摘要时出错

---

## 33. The end of responsive images

**原文标题**: The end of responsive images

**原文链接**: [https://piccalil.li/blog/the-end-of-responsive-images/](https://piccalil.li/blog/the-end-of-responsive-images/)

生成摘要时出错

---

## 34. Website streamed live directly from a model

**原文标题**: Website streamed live directly from a model

**原文链接**: [https://flipbook.page/](https://flipbook.page/)

生成摘要时出错

---

## 35. Over-editing refers to a model modifying code beyond what is necessary

**原文标题**: Over-editing refers to a model modifying code beyond what is necessary

**原文链接**: [https://nrehiew.github.io/blog/minimal_editing/](https://nrehiew.github.io/blog/minimal_editing/)

生成摘要时出错

---

## 36. Highlights from Git 2.54

**原文标题**: Highlights from Git 2.54

**原文链接**: [https://github.blog/open-source/git/highlights-from-git-2-54/](https://github.blog/open-source/git/highlights-from-git-2-54/)

生成摘要时出错

---

## 37. Technical, cognitive, and intent debt

**原文标题**: Technical, cognitive, and intent debt

**原文链接**: [https://martinfowler.com/fragments/2026-04-02.html](https://martinfowler.com/fragments/2026-04-02.html)

生成摘要时出错

---

## 38. Ping-pong robot beats top-level human players

**原文标题**: Ping-pong robot beats top-level human players

**原文链接**: [https://www.reuters.com/sports/ping-pong-robot-ace-makes-history-by-beating-top-level-human-players-2026-04-22/](https://www.reuters.com/sports/ping-pong-robot-ace-makes-history-by-beating-top-level-human-players-2026-04-22/)

生成摘要时出错

---

## 39. Books are not too expensive

**原文标题**: Books are not too expensive

**原文链接**: [https://www.millersbookreview.com/p/no-books-are-not-remotely-too-expensive](https://www.millersbookreview.com/p/no-books-are-not-remotely-too-expensive)

生成摘要时出错

---

## 40. Qwen3.6-27B: Flagship-Level Coding in a 27B Dense Model

**原文标题**: Qwen3.6-27B: Flagship-Level Coding in a 27B Dense Model

**原文链接**: [https://qwen.ai/blog?id=qwen3.6-27b](https://qwen.ai/blog?id=qwen3.6-27b)

生成摘要时出错

---

## 41. Parallel agents in Zed

**原文标题**: Parallel agents in Zed

**原文链接**: [https://zed.dev/blog/parallel-agents](https://zed.dev/blog/parallel-agents)

生成摘要时出错

---

## 42. A Full Apple Ecosystem Now Costs Less Than a MacBook Pro

**原文标题**: A Full Apple Ecosystem Now Costs Less Than a MacBook Pro

**原文链接**: [https://www.macrumors.com/2026/04/23/apple-ecosystem-now-costs-less-than-macbook-pro/](https://www.macrumors.com/2026/04/23/apple-ecosystem-now-costs-less-than-macbook-pro/)

生成摘要时出错

---

## 43. Show HN: LocalLLM – Recipes for Running the Local LLM (Need Contributors)

**原文标题**: Show HN: LocalLLM – Recipes for Running the Local LLM (Need Contributors)

**原文链接**: [https://locallllm.fly.dev](https://locallllm.fly.dev)

生成摘要时出错

---

## 44. Scoring Show HN submissions for AI design patterns

**原文标题**: Scoring Show HN submissions for AI design patterns

**原文链接**: [https://www.adriankrebs.ch/blog/design-slop/](https://www.adriankrebs.ch/blog/design-slop/)

生成摘要时出错

---

## 45. The active ingredients: physical activity features linked to healthy brain aging

**原文标题**: The active ingredients: physical activity features linked to healthy brain aging

**原文链接**: [https://link.springer.com/article/10.1186/s13195-026-01998-6](https://link.springer.com/article/10.1186/s13195-026-01998-6)

生成摘要时出错

---

## 46. Tempest vs. Tempest: The Making and Remaking of Atari's Iconic Video Game

**原文标题**: Tempest vs. Tempest: The Making and Remaking of Atari's Iconic Video Game

**原文链接**: [https://tempest.homemade.systems](https://tempest.homemade.systems)

生成摘要时出错

---

## 47. Windows 9x Subsystem for Linux

**原文标题**: Windows 9x Subsystem for Linux

**原文链接**: [https://social.hails.org/@hailey/116446826733136456](https://social.hails.org/@hailey/116446826733136456)

生成摘要时出错

---

## 48. Bodega cats of New York

**原文标题**: Bodega cats of New York

**原文链接**: [https://bodegacatsofnewyork.com](https://bodegacatsofnewyork.com)

生成摘要时出错

---

## 49. OpenAI's response to the Axios developer tool compromise

**原文标题**: OpenAI's response to the Axios developer tool compromise

**原文链接**: [https://openai.com/index/axios-developer-tool-compromise/](https://openai.com/index/axios-developer-tool-compromise/)

生成摘要时出错

---

## 50. Canonical Releases Ubuntu 26.04 LTS Resolute Raccoon

**原文标题**: Canonical Releases Ubuntu 26.04 LTS Resolute Raccoon

**原文链接**: [https://ubuntu.com/blog/canonical-releases-ubuntu-26-04-lts-resolute-raccoon](https://ubuntu.com/blog/canonical-releases-ubuntu-26-04-lts-resolute-raccoon)

生成摘要时出错

---

## 51. Workspace Agents in ChatGPT

**原文标题**: Workspace Agents in ChatGPT

**原文链接**: [https://openai.com/index/introducing-workspace-agents-in-chatgpt/](https://openai.com/index/introducing-workspace-agents-in-chatgpt/)

生成摘要时出错

---

## 52. Borrow-checking without type-checking

**原文标题**: Borrow-checking without type-checking

**原文链接**: [https://www.scattered-thoughts.net/writing/borrow-checking-without-type-checking/](https://www.scattered-thoughts.net/writing/borrow-checking-without-type-checking/)

生成摘要时出错

---

## 53. The Forgotten History of Hershey's Electric Railway (1916) in Cuba

**原文标题**: The Forgotten History of Hershey's Electric Railway (1916) in Cuba

**原文链接**: [https://spectrum.ieee.org/hershey-electric-railway-cuba](https://spectrum.ieee.org/hershey-electric-railway-cuba)

生成摘要时出错

---

## 54. Verus is a tool for verifying the correctness of code written in Rust

**原文标题**: Verus is a tool for verifying the correctness of code written in Rust

**原文链接**: [https://verus-lang.github.io/verus/guide/](https://verus-lang.github.io/verus/guide/)

生成摘要时出错

---

## 55. What killed the Florida orange?

**原文标题**: What killed the Florida orange?

**原文链接**: [https://slate.com/business/2026/04/florida-state-orange-food-houses-real-estate.html](https://slate.com/business/2026/04/florida-state-orange-food-houses-real-estate.html)

生成摘要时出错

---

## 56. Bring Your Agent to Teams

**原文标题**: Bring Your Agent to Teams

**原文链接**: [https://microsoft.github.io/teams-sdk/blog/bring-your-agent-to-teams/](https://microsoft.github.io/teams-sdk/blog/bring-your-agent-to-teams/)

生成摘要时出错

---

## 57. Plexus P/20 Emulator

**原文标题**: Plexus P/20 Emulator

**原文链接**: [https://spritetm.github.io/plexus_20_emu/](https://spritetm.github.io/plexus_20_emu/)

生成摘要时出错

---

## 58. XOR'ing a register with itself is the idiom for zeroing it out. Why not sub?

**原文标题**: XOR'ing a register with itself is the idiom for zeroing it out. Why not sub?

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20260421-00/?p=112247](https://devblogs.microsoft.com/oldnewthing/20260421-00/?p=112247)

生成摘要时出错

---

## 59. LLM pricing has never made sense

**原文标题**: LLM pricing has never made sense

**原文链接**: [https://anderegg.ca/2026/04/22/llm-pricing-has-never-made-sense](https://anderegg.ca/2026/04/22/llm-pricing-has-never-made-sense)

生成摘要时出错

---

## 60. SteamOS now runs on every AMD handheld

**原文标题**: SteamOS now runs on every AMD handheld

**原文链接**: [https://www.xda-developers.com/steamos-now-runs-on-every-amd-handheld-and-valve-didnt-even-make-a-big-deal-about-it/](https://www.xda-developers.com/steamos-now-runs-on-every-amd-handheld-and-valve-didnt-even-make-a-big-deal-about-it/)

生成摘要时出错

---

## 61. New study compares growing corn for energy to solar production

**原文标题**: New study compares growing corn for energy to solar production

**原文链接**: [https://www.anthropocenemagazine.org/2025/04/new-study-compares-growing-corn-for-energy-to-solar-production-its-no-contest/](https://www.anthropocenemagazine.org/2025/04/new-study-compares-growing-corn-for-energy-to-solar-production-its-no-contest/)

生成摘要时出错

---

## 62. Columnar Storage Is Normalization

**原文标题**: Columnar Storage Is Normalization

**原文链接**: [https://buttondown.com/jaffray/archive/columnar-storage-is-normalization/](https://buttondown.com/jaffray/archive/columnar-storage-is-normalization/)

生成摘要时出错

---

## 63. 98% of all recent environmental claims can be categorized as "greenwashing"

**原文标题**: 98% of all recent environmental claims can be categorized as "greenwashing"

**原文链接**: [https://www.eurekalert.org/news-releases/1124525](https://www.eurekalert.org/news-releases/1124525)

生成摘要时出错

---

## 64. The Illuminated Man: an unconventional portrait of JG Ballard

**原文标题**: The Illuminated Man: an unconventional portrait of JG Ballard

**原文链接**: [https://www.theguardian.com/books/2026/apr/20/the-illuminated-man-by-christopher-priest-and-nina-allan-review-an-unconventional-portrait-of-jg-ballard](https://www.theguardian.com/books/2026/apr/20/the-illuminated-man-by-christopher-priest-and-nina-allan-review-an-unconventional-portrait-of-jg-ballard)

生成摘要时出错

---

## 65. The Neon King of New Orleans

**原文标题**: The Neon King of New Orleans

**原文链接**: [https://gardenandgun.com/new-orleans-neon-king](https://gardenandgun.com/new-orleans-neon-king)

生成摘要时出错

---

## 66. ChatGPT Images 2.0

**原文标题**: ChatGPT Images 2.0

**原文链接**: [https://openai.com/index/introducing-chatgpt-images-2-0/](https://openai.com/index/introducing-chatgpt-images-2-0/)

生成摘要时出错

---

## 67. Our eighth generation TPUs: two chips for the agentic era

**原文标题**: Our eighth generation TPUs: two chips for the agentic era

**原文链接**: [https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)

生成摘要时出错

---

## 68. You don't need advice from editors on rejected manuscripts

**原文标题**: You don't need advice from editors on rejected manuscripts

**原文链接**: [https://twitter.com/orsonscottcard/status/2046702294406680751](https://twitter.com/orsonscottcard/status/2046702294406680751)

生成摘要时出错

---

## 69. The handmade beauty of Machine Age data visualizations

**原文标题**: The handmade beauty of Machine Age data visualizations

**原文链接**: [https://resobscura.substack.com/p/the-handmade-beauty-of-machine-age](https://resobscura.substack.com/p/the-handmade-beauty-of-machine-age)

生成摘要时出错

---

## 70. Kernel code removals driven by LLM-created security reports

**原文标题**: Kernel code removals driven by LLM-created security reports

**原文链接**: [https://lwn.net/Articles/1068928/](https://lwn.net/Articles/1068928/)

生成摘要时出错

---

## 71. Effectful Recursion Schemes

**原文标题**: Effectful Recursion Schemes

**原文链接**: [https://effekt-lang.org/blog/recursion-schemes/](https://effekt-lang.org/blog/recursion-schemes/)

生成摘要时出错

---

## 72. Ubuntu 26.04 LTS Released

**原文标题**: Ubuntu 26.04 LTS Released

**原文链接**: [https://ubuntu.com/download/desktop](https://ubuntu.com/download/desktop)

生成摘要时出错

---

## 73. Surveillance Pricing: Exploiting Information Asymmetries

**原文标题**: Surveillance Pricing: Exploiting Information Asymmetries

**原文链接**: [https://lpeproject.org/blog/surveillance-pricing-exploiting-information-asymmetries/](https://lpeproject.org/blog/surveillance-pricing-exploiting-information-asymmetries/)

生成摘要时出错

---

## 74. OpenAI model for masking personally identifiable information (PII) in text

**原文标题**: OpenAI model for masking personally identifiable information (PII) in text

**原文链接**: [https://openai.com/index/introducing-openai-privacy-filter/](https://openai.com/index/introducing-openai-privacy-filter/)

生成摘要时出错

---

## 75. The great Scouse pasty war

**原文标题**: The great Scouse pasty war

**原文链接**: [https://www.livpost.co.uk/the-great-scouse-pasty-war/](https://www.livpost.co.uk/the-great-scouse-pasty-war/)

生成摘要时出错

---

## 76. 3.4M Solar Panels

**原文标题**: 3.4M Solar Panels

**原文链接**: [https://tech.marksblogg.com/american-solar-farms-v2.html](https://tech.marksblogg.com/american-solar-farms-v2.html)

生成摘要时出错

---

## 77. Spam in conversational replies to blog posts

**原文标题**: Spam in conversational replies to blog posts

**原文链接**: [https://shkspr.mobi/blog/2026/04/sneaky-spam-in-conversational-replies-to-blog-posts/](https://shkspr.mobi/blog/2026/04/sneaky-spam-in-conversational-replies-to-blog-posts/)

生成摘要时出错

---

## 78. Approximating Hyperbolic Tangent

**原文标题**: Approximating Hyperbolic Tangent

**原文链接**: [https://jtomschroeder.com/blog/approximating-tanh/](https://jtomschroeder.com/blog/approximating-tanh/)

生成摘要时出错

---

## 79. Show HN: Broccoli, one shot coding agent on the cloud

**原文标题**: Show HN: Broccoli, one shot coding agent on the cloud

**原文链接**: [https://github.com/besimple-oss/broccoli](https://github.com/besimple-oss/broccoli)

生成摘要时出错

---

## 80. US Department of Justice has officially reclassified cannabis as less dangerous

**原文标题**: US Department of Justice has officially reclassified cannabis as less dangerous

**原文链接**: [https://www.bbc.com/news/articles/cdxd0xxp0jko](https://www.bbc.com/news/articles/cdxd0xxp0jko)

生成摘要时出错

---

## 81. Iran claims US exploited networking equipment backdoors during strikes

**原文标题**: Iran claims US exploited networking equipment backdoors during strikes

**原文链接**: [https://www.tomshardware.com/tech-industry/cyber-security/iran-claims-us-exploited-networking-equipment-backdoors-during-strikes](https://www.tomshardware.com/tech-industry/cyber-security/iran-claims-us-exploited-networking-equipment-backdoors-during-strikes)

生成摘要时出错

---

## 82. Another Day Has Come

**原文标题**: Another Day Has Come

**原文链接**: [https://daringfireball.net/2026/04/another_day_has_come](https://daringfireball.net/2026/04/another_day_has_come)

生成摘要时出错

---

## 83. Ultraviolet corona discharges on treetops during storms

**原文标题**: Ultraviolet corona discharges on treetops during storms

**原文链接**: [https://www.psu.edu/news/earth-and-mineral-sciences/story/treetops-glowing-during-storms-captured-film-first-time](https://www.psu.edu/news/earth-and-mineral-sciences/story/treetops-glowing-during-storms-captured-film-first-time)

生成摘要时出错

---

## 84. Making RAM at Home [video]

**原文标题**: Making RAM at Home [video]

**原文链接**: [https://www.youtube.com/watch?v=h6GWikWlAQA](https://www.youtube.com/watch?v=h6GWikWlAQA)

生成摘要时出错

---

## 85. Congressman Introduces Bill to Ban AI Chatbots in Children's Toys

**原文标题**: Congressman Introduces Bill to Ban AI Chatbots in Children's Toys

**原文链接**: [https://blakemoore.house.gov/media/press-releases/congressman-blake-moore-introduces-bill-to-ban-artificial-intelligence-chatbots-in-childrens-toys](https://blakemoore.house.gov/media/press-releases/congressman-blake-moore-introduces-bill-to-ban-artificial-intelligence-chatbots-in-childrens-toys)

生成摘要时出错

---

## 86. All your agents are going async

**原文标题**: All your agents are going async

**原文链接**: [https://zknill.io/posts/all-your-agents-are-going-async/](https://zknill.io/posts/all-your-agents-are-going-async/)

生成摘要时出错

---

## 87. The Onion to Take over InfoWars

**原文标题**: The Onion to Take over InfoWars

**原文链接**: [https://www.nytimes.com/2026/04/20/business/infowars-alex-jones-the-onion.html](https://www.nytimes.com/2026/04/20/business/infowars-alex-jones-the-onion.html)

生成摘要时出错

---

## 88. Musicians are manufacturing sold-out shows

**原文标题**: Musicians are manufacturing sold-out shows

**原文链接**: [https://www.bloomberg.com/news/articles/2026-04-17/how-bands-like-cameron-winter-s-geese-are-manufacturing-sold-out-shows](https://www.bloomberg.com/news/articles/2026-04-17/how-bands-like-cameron-winter-s-geese-are-manufacturing-sold-out-shows)

生成摘要时出错

---

## 89. Rip language. Compiles to ES2022. Built-in reactivity

**原文标题**: Rip language. Compiles to ES2022. Built-in reactivity

**原文链接**: [https://github.com/shreeve/rip-lang](https://github.com/shreeve/rip-lang)

生成摘要时出错

---

## 90. Laws of Software Engineering

**原文标题**: Laws of Software Engineering

**原文链接**: [https://lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com)

生成摘要时出错

---

## 91. Laws of Software Engineering

**原文标题**: Laws of Software Engineering

**原文链接**: [https://lawsofsoftwareengineering.com](https://lawsofsoftwareengineering.com)

生成摘要时出错

---

## 92. Garbage collection without unsafe code

**原文标题**: Garbage collection without unsafe code

**原文链接**: [https://fitzgen.com/2024/02/06/safe-gc.html](https://fitzgen.com/2024/02/06/safe-gc.html)

生成摘要时出错

---

## 93. MuJoCo – Advanced Physics Simulation

**原文标题**: MuJoCo – Advanced Physics Simulation

**原文链接**: [https://github.com/google-deepmind/mujoco](https://github.com/google-deepmind/mujoco)

生成摘要时出错

---

## 94. Mythos is shaping up to be a nothingburger

**原文标题**: Mythos is shaping up to be a nothingburger

**原文链接**: [https://www.theregister.com/2026/04/22/anthropic_mythos_hype_nothingburger/](https://www.theregister.com/2026/04/22/anthropic_mythos_hype_nothingburger/)

生成摘要时出错

---

## 95. Anonymous credentials: an illustrated primer (Part 2)

**原文标题**: Anonymous credentials: an illustrated primer (Part 2)

**原文链接**: [https://blog.cryptographyengineering.com/2026/04/17/anonymous-credentials-an-illustrated-primer-part-2/](https://blog.cryptographyengineering.com/2026/04/17/anonymous-credentials-an-illustrated-primer-part-2/)

生成摘要时出错

---

## 96. GitHub CLI now collects pseudoanonymous telemetry

**原文标题**: GitHub CLI now collects pseudoanonymous telemetry

**原文链接**: [https://cli.github.com/telemetry](https://cli.github.com/telemetry)

生成摘要时出错

---

## 97. Contact Lens Uses Microfluidics to Monitor and Treat Glaucoma

**原文标题**: Contact Lens Uses Microfluidics to Monitor and Treat Glaucoma

**原文链接**: [https://spectrum.ieee.org/smart-contact-lens-glaucoma-microfluidics](https://spectrum.ieee.org/smart-contact-lens-glaucoma-microfluidics)

生成摘要时出错

---

## 98. Youth Suicides Declined After Creation of National Hotline

**原文标题**: Youth Suicides Declined After Creation of National Hotline

**原文链接**: [https://www.nytimes.com/2026/04/22/science/988-youth-suicides-decline.html](https://www.nytimes.com/2026/04/22/science/988-youth-suicides-decline.html)

生成摘要时出错

---

## 99. How Much Caffeine in Coffee Cup?

**原文标题**: How Much Caffeine in Coffee Cup?

**原文链接**: [https://www.researchgate.net/publication/317824932_How_Much_Caffeine_in_Coffee_Cup_Effects_of_Processing_Operations_Extraction_Methods_and_Variables](https://www.researchgate.net/publication/317824932_How_Much_Caffeine_in_Coffee_Cup_Effects_of_Processing_Operations_Extraction_Methods_and_Variables)

生成摘要时出错

---

## 100. Changes to GitHub Copilot individual plans

**原文标题**: Changes to GitHub Copilot individual plans

**原文链接**: [https://github.blog/news-insights/company-news/changes-to-github-copilot-individual-plans/](https://github.blog/news-insights/company-news/changes-to-github-copilot-individual-plans/)

生成摘要时出错

---

