# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-08-17.md)

*最后自动更新时间: 2026-08-17 17:52:18*
## 1. DuckDB v2.0 预览

**原文标题**: A Preview of DuckDB v2.0

**原文链接**: [https://duckdb.org/2026/08/17/duckdb-20-highlights](https://duckdb.org/2026/08/17/duckdb-20-highlights)

DuckDB v2.0，代号为“Cyanoptera”，计划于 2026 年秋季发布。这一重大版本标志着 DuckDB 从纯嵌入式数据库向支持客户端/服务器架构的系统转变，同时引入了重大的架构变革和性能提升。

**核心亮点包括：**
*   **DuckDB 作为服务器：** 通过全新的 `quack` 扩展和 `CONNECT` 语句，DuckDB 现在可以通过网络提供数据库服务。这包括对 PostgreSQL 和 MySQL 等外部数据库的远程查询下推。
*   **VARIANT 类型：** 被设计为“加强版 JSON”，该类型能自动将半结构化数据“粉碎”为列式格式，从而实现快速、无模式的查询以及高压缩率。
*   **全触发器支持：** 此版本引入了标准 SQL 触发器（`BEFORE`/`AFTER`，行级/语句级），支持复杂的审计和自动化工作流。
*   **性能与 I/O：** 全新的异步 I/O 层显著加速了在 S3 等网络存储上的查询。性能优化包括重写的递归 CTE 引擎（速度提升达 40 倍）以及支持聚合操作溢出至磁盘。
*   **新 SQL 解析器：** 一个基于 PEG 的自定义解析器取代了源自 PostgreSQL 的旧版本。这改善了错误提示，并允许扩展程序添加新的 SQL 语法。
*   **存储与内核：** 存储格式 v2.0 引入了缓冲区管理索引和元数据延迟加载，使大型数据库能以更少的内存消耗更快地打开。移除 ICU 库简化了时区和排序规则的处理，使二进制文件体积更小、运行更高效。
*   **扩展稳定性：** 具有版本控制且稳定的 C API 允许开发者只需构建一次扩展，即可在未来的版本中保持兼容，从而促进更强大的社区生态系统。

总之，v2.0 在增加重大功能与深度引擎改进之间取得了平衡，使 DuckDB 能够胜任长期运行的多租户部署和高性能云原生分析。

---

## 2. 给朋友买电池

**原文标题**: Buy Your Friends Batteries

**原文链接**: [https://domenkozar.com/2026/08/17/buy-your-friends-batteries/](https://domenkozar.com/2026/08/17/buy-your-friends-batteries/)

在《给朋友买电池》一文中，作者提出了一种比那些容易被遗忘的生日礼物更实用的替代方案：“生日电池俱乐部”。通过每人出资50至200欧元，朋友圈可以随着时间的推移，为每位成员购买一台5千瓦时的家用电池（成本约为1600欧元）。

其核心经济收益在于**电网套利**。通过自动价格优化，电池在电价低廉时充电，在用电高峰电价昂贵时放电。根据德国和西班牙2025年的数据，这一策略每年可节省约126至144欧元。虽然仅靠套利的投资回报周期为11至13年，但若结合太阳能电池板或参与电网服务补偿，其经济效益将显著提升。

除了节省开支，作者还强调了两大主要优势：
1. **可靠性：** 电池提供高达3千瓦的离网输出，确保冰箱、照明和路由器等关键设备在停电期间仍能正常运行。
2. **可持续性：** 分布式储能有助于实现能源生产与消费的解耦。这使电网能够利用更多原本可能被浪费的可再生能源，例如西班牙正午的阳光或德国深夜的风力。

为了实现这一方案，作者建议先确认朋友家的安装兼容性，随后筹集资金，并购买带有自动费率整合功能的设备。最终，作者展望了一个由数百万台分布式电池构成庞大储能网络（容量可达50吉瓦时）的未来，从而构建一个更具韧性、更低碳的欧洲能源电网。

---

## 3. AI-Generated GitHub Copilot “Autofix” Allowed Compromise of Snowflake's Jira

**原文标题**: AI-Generated GitHub Copilot “Autofix” Allowed Compromise of Snowflake's Jira

**原文链接**: [https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug)

生成摘要时出错

---

## 4. Launch HN: Speko (YC S26) —— 语音 AI 版 OpenRouter

**原文标题**: Launch HN: Speko (YC S26) – OpenRouter for Voice AI

**原文链接**: [https://speko.ai/](https://speko.ai/)

**Speko (YC S26)** 是一个统一的 API 网关，旨在简化语音 AI 的集成与优化，被誉为“语音版的 OpenRouter”。它将数十家语音转文本 (STT)、大语言模型 (LLM) 和文本转语音 (TTS) 服务商（如 OpenAI、Deepgram、AssemblyAI 和 ElevenLabs）聚合到一个兼容 OpenAI 的单一接口中。

该平台的核心价值在于其**针对特定语言的基准测试**。Speko 不依赖通用的厂商排行榜，而是根据多种语言（包括英语、阿拉伯语、法语、德语和印地语）的字错率 (WER) 和每分钟成本来衡量模型。这使开发者能够针对特定的全球市场或性能目标，做出数据驱动的模型选择。

关键特性包括：
*   **统一网关：** 仅需一个 API 密钥和单一基础 URL 即可访问多家服务商。
*   **自动路由：** 通过将模型设置为“auto”，Speko 会根据发布的基准测试，将请求动态路由至性能最佳或成本最低的模型。
*   **无缝集成：** 由于 Speko 兼容 OpenAI API，只需极少的代码改动即可将其接入 **LiveKit、Pipecat 以及 Claude/Cursor（通过 MCP）** 等现有框架。
*   **可观测性：** 开发者可以集中运行并监控其语音工作流，实时对比性能与成本。

通过对语音 AI 基础设施层的抽象，Speko 让开发者能够灵活地在不同服务商之间进行测试和切换，而无需重写代码。

---

## 5. 如何禁用或避开侵入式 AI

**原文标题**: How to disable or avoid intrusive AI

**原文链接**: [https://www.librarian.net/notoai/](https://www.librarian.net/notoai/)

本指南为希望在各类数字平台上减少或消除侵入性 AI 功能的用户提供了全面说明。指南指出，许多 AI 集成功能均为默认开启，用户需要手动关闭（opt-out）才能维持传统的科技环境。

**主要操作说明包括：**

*   **操作系统：** 在较新款的 iOS 和 Mac 设备上禁用 **Apple Intelligence**；通过任务栏设置和应用列表卸载或关闭 **Windows Copilot**；在 Android 上移除或限制 **Google Gemini**，包括从助手手中夺回电源键的控制权。
*   **浏览器与搜索：** 访问 **Chrome** 和 **Edge** 的内部“flags”设置以禁用 AI 驱动的侧边栏和按钮；利用 **Firefox** 的“AI 控制”屏蔽增强功能；以及使用 **DuckDuckGo** 专门的“无 AI”版本。
*   **生产力工具：** 禁用 **Adobe Acrobat** 中的生成式 AI 偏好设置；关闭 **Gmail** 和 **Google Workspace** 中的“智能功能”；以及退出 **Office 365** 和**记事本**的 AI 功能。
*   **通讯应用：** 关闭 **WhatsApp** 中的消息摘要和贴纸建议；管理 **Slack** 中的管理级 AI 设置；以及禁用 **Zoom** 中的 AI 标签和转录功能。
*   **电子邮件：** 关闭 **Yahoo Mail** 中的 AI 消息摘要。

指南还推荐了适用于 Windows 的第三方“去臃肿”工具（如 O&O ShutUp 10），以及来自 **Library Freedom Project** 的外部资源，以进行进一步的 AI 检测和移除。由于各平台经常增加默认开启的新 AI 功能，作者建议定期检查设置，以确保持续获得无 AI 的体验。

---

## 6. GPT 5.6 Sol 是 OpenAI 有史以来发布的最好的“视觉”模型。

**原文标题**: GPT 5.6 Sol is the best "vision" model OpenAI ever released

**原文链接**: [https://blog.roboflow.com/openai-gpt-5-6/](https://blog.roboflow.com/openai-gpt-5-6/)

生成摘要时出错

---

## 7. Github.com 故障

**原文标题**: Incident with Github.com

**原文链接**: [https://www.githubstatus.com/incidents/zkxwbgr0cnmx](https://www.githubstatus.com/incidents/zkxwbgr0cnmx)

2026年8月17日，GitHub 遭遇了严重的服务中断，波及了几乎所有主要组件，包括 Git 操作、Actions、API 请求、Issues、Pull Requests、Pages 以及 Copilot。

故障始于 UTC 时间约 13:40。在中断高峰期，GitHub 报告网页和 API 流量的错误率约为 20%，而归档和原始代码库下载的错误率则接近 50%。此次停机还影响了关键的管理与安全功能，例如 SAML 和 OIDC 认证、SCIM 以及团队同步（Team Sync）。

整个下午，GitHub 的工程团队持续进行调查并采取缓解措施。截至 UTC 时间 16:36，团队确定了一个故障组件并实施了纠正操作，随后服务进入了短暂的受监控稳定期。然而，UTC 时间 17:34 的最新更新显示，虽然主要诱因已得到解决，但余留影响仍持续波及多项服务。

根据日志中的最终报告，Git 操作的性能目前仍处于下降状态，团队正在采取额外的缓解措施以解决剩余问题。服务全面恢复工作仍在进行中。

---

## 8. How to put 170 atoms in an atom

**原文标题**: How to put 170 atoms in an atom

**原文链接**: [https://signoregalilei.com/2026/08/02/how-to-put-170-atoms-in-an-atom/](https://signoregalilei.com/2026/08/02/how-to-put-170-atoms-in-an-atom/)

This article explains how scientists have successfully nested multiple atoms within the space of a single atom, a feat made possible by the fact that atoms are mostly empty space. 

The process relies on two key components: **Rydberg atoms** and **Bose-Einstein Condensates (BECs)**. A Rydberg atom is created through "electron excitation," where a laser is used to nudge an electron into an orbital significantly farther from the nucleus. These atoms can become over 1,000 times wider than a standard atom. To prevent these delicate structures from collapsing, scientists use a BEC—a state of matter where atoms are cooled to near absolute zero, causing them to move slowly and share the same quantum state.

In 2018, researchers used strontium atoms in a BEC to create these conditions. By exciting one strontium atom within the cold cluster, its massive electron orbital encompassed several neighboring atoms. This unique bond created a "Rydberg polaron." While the initial experiment captured only a few atoms, computer simulations indicate that up to 170 atoms could theoretically fit inside a single Rydberg atom's orbital. 

Although these Rydberg polarons do not yet have practical applications for the general public, they provide scientists with a valuable tool for observing and understanding quantum mechanics on a larger, more accessible scale.

---

## 9. Olo (颜色)

**原文标题**: Olo (Color)

**原文链接**: [https://en.wikipedia.org/wiki/Olo_(color)](https://en.wikipedia.org/wiki/Olo_(color))

**Olo**，也被称为“迷幻水绿色”，是加州大学伯克利分校的科学家于2025年4月18日发现的一种“虚色”。它存在于标准人类可见色域之外，因为它需要对M型视锥细胞进行独立刺激；而在正常光照条件下，由于人眼S型和L型视锥细胞的感光灵敏度存在重叠，这种效果是无法实现的。

为了生成这种颜色，研究人员利用激光精确瞄准并激活了五名受试者视网膜中的单个M型视锥细胞。这些参与者将Olo描述为一种具有“前所未有饱和度”的蓝绿色，比自然界中任何可感知的颜色都更加强烈。它的名字源于其在LMS色彩空间中的理论坐标(0, 1, 0)，这与Leet语（骇客语）中的单词“olo”形状相似。虽然与其最接近的sRGB等效色是十六进制代码#00FFCC，但真正的颜色依然无法通过传统的显示器或颜料呈现。

由任吴（Ren Ng）教授共同参与的研究团队指出，用于产生Olo的技术最终可能被应用于治疗色盲，甚至实现“四色视觉”——这是一种能扩大可感知颜色范围的增强型视觉。

尽管科学界承认该实验是一项重大的技术成就，但Olo作为一种“新”颜色的地位尚存争议。包括约翰·巴伯（John Barbur）教授在内的一些专家质疑，人工刺激产生的反应是否真的构成一种全新的颜色。无论争议如何，这一发现已在科学、艺术和媒体领域引起了广泛关注。

---

## 10. How I developed an Am29000 C compiler and web browser

**原文标题**: How I developed an Am29000 C compiler and web browser

**原文链接**: [https://nanochess.org/am29000_c_compiler_web_browser.html](https://nanochess.org/am29000_c_compiler_web_browser.html)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 2 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 3 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 4 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 5 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 6 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 7 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 8 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 9 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 10 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 11 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 12 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 13 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 14 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 15 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 16 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 17 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 18 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 19 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 20 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 21 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 22 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 23 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 24 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 25 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 26 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 27 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 28 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 29 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 30 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 31 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 32 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 33 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 34 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 35 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 36 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 37 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 38 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 39 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 40 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 41 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 42 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 43 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 44 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 45 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 46 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 47 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 48 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 49 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 50 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 51 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 52 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 53 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 54 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 55 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 56 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 57 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 58 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 59 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 60 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 61 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 62 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 63 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 64 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 65 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 66 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 67 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 68 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 69 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 70 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 71 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 72 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 73 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 74 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 75 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 76 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 77 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 78 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 79 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 80 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 81 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 82 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 83 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 84 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 85 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 86 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 87 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 88 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 89 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 90 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 91 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 92 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 93 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 94 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 95 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 96 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 97 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 98 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 99 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 100 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 101 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 102 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 103 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 104 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 105 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 106 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 107 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 108 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 109 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 110 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 111 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 112 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 113 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 114 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 115 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 116 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 117 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 118 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 119 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 120 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 121 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 122 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 123 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 124 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 125 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 126 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 127 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 128 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 129 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 130 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 131 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 132 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 133 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 134 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 135 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 136 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 137 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 138 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 139 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 140 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 141 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 142 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 143 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 144 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 145 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 146 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 147 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 148 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 149 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 150 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 151 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 152 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 153 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 154 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 155 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 156 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 157 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 158 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 159 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 160 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 161 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 162 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 163 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 164 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 165 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 166 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 167 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 168 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 169 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 170 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 171 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 172 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 173 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 174 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 175 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 176 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 177 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 178 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 179 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 180 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 181 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 182 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 183 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 184 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 185 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 186 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 187 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 188 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 189 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 190 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 191 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 192 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 193 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 194 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 195 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 196 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 197 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 198 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 199 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 200 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 201 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 202 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 203 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 204 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 205 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 206 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 207 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 208 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 209 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 210 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 211 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 212 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 213 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 214 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 215 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 216 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 217 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 218 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 219 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 220 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 221 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 222 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 223 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 224 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 225 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 226 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 227 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 228 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 229 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 230 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 231 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 232 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 233 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 234 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 235 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 236 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 237 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 238 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 239 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 240 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 241 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 242 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 243 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 244 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 245 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 246 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 247 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 248 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 249 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 250 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 251 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 252 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 253 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 254 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 255 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 256 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 257 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 258 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 259 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 260 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 261 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 262 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 263 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 264 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 265 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 266 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 267 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 268 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 269 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 270 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 271 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 272 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 273 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 274 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 275 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 276 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 277 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 278 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 279 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 280 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 281 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 282 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 283 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 284 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 285 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 286 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 287 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 288 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 289 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 290 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 291 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 292 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 293 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 294 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 295 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 296 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 297 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 298 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 299 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 300 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 301 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 302 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 303 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 304 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 305 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 306 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 307 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 308 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 309 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 310 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 311 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 312 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 313 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 314 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 315 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 316 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 317 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 318 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 319 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 320 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 321 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 322 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 323 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 324 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 325 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 326 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 327 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 328 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 329 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 330 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 331 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 332 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 333 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 334 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 335 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 336 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 337 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 338 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 339 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 340 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 341 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 342 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 343 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 344 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 345 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 346 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 347 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 348 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 349 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 350 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 351 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 352 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 353 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 354 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 355 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 356 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 357 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 358 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 359 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 360 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 361 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 362 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 363 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 364 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 365 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 366 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 367 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 368 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 369 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 370 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 371 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 372 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 373 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 374 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 375 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 376 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 377 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 378 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 379 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 380 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 381 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 382 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 383 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 384 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 385 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 386 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 387 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 388 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 389 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 390 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 391 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 392 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 393 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 394 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 395 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 396 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 397 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 398 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 399 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 400 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 401 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 402 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 403 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 404 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 405 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 406 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 407 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 408 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 409 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 410 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 411 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 412 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 413 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 414 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 415 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 416 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 417 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 418 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 419 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 420 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 421 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 422 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 423 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 424 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 425 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 426 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 427 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 428 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 429 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 430 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 431 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 432 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 433 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 434 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 435 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 436 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 437 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 438 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 439 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 440 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 441 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 442 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 443 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 444 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 445 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 446 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 447 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 448 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 449 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 450 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 451 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 452 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 453 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 454 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 455 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 456 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 457 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 458 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 459 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 460 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 461 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 462 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 463 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 464 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 465 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 466 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 467 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 468 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 469 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 470 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 471 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 472 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 473 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 474 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 475 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 476 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 477 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 478 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 479 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 480 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 481 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 482 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 483 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 484 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 485 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 486 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 487 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 488 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 489 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 490 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 491 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 492 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 493 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 494 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 495 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 496 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 497 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 498 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 499 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 500 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 501 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 502 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 503 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 504 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 505 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 506 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 507 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 508 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 509 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 510 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 511 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 512 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 513 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 514 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
