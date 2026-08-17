# Hacker News 热门文章摘要 (2026-08-17)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Show HN: Sokoban AI Solver

**原文标题**: Show HN: Sokoban AI Solver

**原文链接**: [https://mkornreich.me/projects/sokoban/](https://mkornreich.me/projects/sokoban/)

生成摘要时出错

---

## 12. Apple's App Tracking Transparency treated its own apps better than rivals

**原文标题**: Apple's App Tracking Transparency treated its own apps better than rivals

**原文链接**: [https://www.bundeskartellamt.de/SharedDocs/Meldung/EN/Pressemitteilungen/2026/08_17_2026_Apple_ATTF.html](https://www.bundeskartellamt.de/SharedDocs/Meldung/EN/Pressemitteilungen/2026/08_17_2026_Apple_ATTF.html)

生成摘要时出错

---

## 13. Anthropic's ‘watermark’ text adulteration in Claude is a perversion of writing

**原文标题**: Anthropic's ‘watermark’ text adulteration in Claude is a perversion of writing

**原文链接**: [https://daringfireball.net/2026/08/anthropics_watermark_text_adulteration_in_claude_is_a_perversion_of_writing](https://daringfireball.net/2026/08/anthropics_watermark_text_adulteration_in_claude_is_a_perversion_of_writing)

生成摘要时出错

---

## 14. How to ship a database every day

**原文标题**: How to ship a database every day

**原文链接**: [https://turbopuffer.com/blog/control-plane](https://turbopuffer.com/blog/control-plane)

生成摘要时出错

---

## 15. Show HN: Saggar, a Mac terminal that keeps sessions and your attention organized

**原文标题**: Show HN: Saggar, a Mac terminal that keeps sessions and your attention organized

**原文链接**: [https://saggar.marginalutility.dev/](https://saggar.marginalutility.dev/)

生成摘要时出错

---

## 16. Show HN: Learn Flags Quiz

**原文标题**: Show HN: Learn Flags Quiz

**原文链接**: [https://flagquizzes.com/](https://flagquizzes.com/)

生成摘要时出错

---

## 17. On AI regulation and messaging

**原文标题**: On AI regulation and messaging

**原文链接**: [https://twitter.com/DarioAmodei/status/2088758816376807762](https://twitter.com/DarioAmodei/status/2088758816376807762)

生成摘要时出错

---

## 18. Cross-Validation From Scratch and a Surprise at n=100

**原文标题**: Cross-Validation From Scratch and a Surprise at n=100

**原文链接**: [https://www.kenkoonwong.com/blog/crossvalidation/](https://www.kenkoonwong.com/blog/crossvalidation/)

生成摘要时出错

---

## 19. Show HN: Desktopcolors.com – A museum for solid background colors of classic OS

**原文标题**: Show HN: Desktopcolors.com – A museum for solid background colors of classic OS

**原文链接**: [https://desktopcolors.com](https://desktopcolors.com)

生成摘要时出错

---

## 20. How Go detects struct copies with sync.noCopy

**原文标题**: How Go detects struct copies with sync.noCopy

**原文链接**: [https://func25.dev/posts/go-sync-nocopy/](https://func25.dev/posts/go-sync-nocopy/)

生成摘要时出错

---

## 21. Mexico crackdown on coastal development

**原文标题**: Mexico crackdown on coastal development

**原文链接**: [https://yucatanmagazine.com/mexico-crackdown-on-coastal-development/](https://yucatanmagazine.com/mexico-crackdown-on-coastal-development/)

生成摘要时出错

---

## 22. Universal Health Coverage Could Save $1T and 114k Lives a Year, Yale Study

**原文标题**: Universal Health Coverage Could Save $1T and 114k Lives a Year, Yale Study

**原文链接**: [https://ysph.yale.edu/news-article/universal-health-coverage-could-save-one-trillion-dollars-and-114000-lives-every-year/](https://ysph.yale.edu/news-article/universal-health-coverage-could-save-one-trillion-dollars-and-114000-lives-every-year/)

生成摘要时出错

---

## 23. Ahmad on X: "Anthropic's War on open source AI" / X

**原文标题**: Ahmad on X: "Anthropic's War on open source AI" / X

**原文链接**: [https://twitter.com/TheAhmadOsman/status/2065307070044234186](https://twitter.com/TheAhmadOsman/status/2065307070044234186)

生成摘要时出错

---

## 24. Online clinics and influencers are promoting Cialis as a longevity drug

**原文标题**: Online clinics and influencers are promoting Cialis as a longevity drug

**原文链接**: [https://www.npr.org/2026/08/17/nx-s1-5928263/cialis-viagra-tadalafil-longevity-heart-health](https://www.npr.org/2026/08/17/nx-s1-5928263/cialis-viagra-tadalafil-longevity-heart-health)

生成摘要时出错

---

## 25. Linear algebra done right

**原文标题**: Linear algebra done right

**原文链接**: [https://linear.axler.net/](https://linear.axler.net/)

生成摘要时出错

---

## 26. Reticulum – Decentralized Mesh Network

**原文标题**: Reticulum – Decentralized Mesh Network

**原文链接**: [https://reticulum.network/](https://reticulum.network/)

生成摘要时出错

---

## 27. Qwen 3.8 27B is excellent, but it defaults to overthinking things

**原文标题**: Qwen 3.8 27B is excellent, but it defaults to overthinking things

**原文链接**: [https://simonwillison.net/2026/Aug/16/qwen-38-27b/](https://simonwillison.net/2026/Aug/16/qwen-38-27b/)

生成摘要时出错

---

## 28. The only known trebuchet casualty in history

**原文标题**: The only known trebuchet casualty in history

**原文链接**: [https://arstechnica.com/science/2026/08/meet-the-only-known-trebuchet-casualty-in-history/](https://arstechnica.com/science/2026/08/meet-the-only-known-trebuchet-casualty-in-history/)

生成摘要时出错

---

## 29. AGI-64 Brings Sierra Adventures to the Commodore 64

**原文标题**: AGI-64 Brings Sierra Adventures to the Commodore 64

**原文链接**: [https://meanhamster.com/news/agi-64-brings-sierra-adventures-to-the-commodore-64](https://meanhamster.com/news/agi-64-brings-sierra-adventures-to-the-commodore-64)

生成摘要时出错

---

## 30. Human Interface Guidelines from various platforms

**原文标题**: Human Interface Guidelines from various platforms

**原文链接**: [https://unsung.aresluna.org/i-think-theres-a-lot-of-value-in-these/](https://unsung.aresluna.org/i-think-theres-a-lot-of-value-in-these/)

生成摘要时出错

---

## 31. The Life and Death of Direct File [pdf]

**原文标题**: The Life and Death of Direct File [pdf]

**原文链接**: [https://www.ischool.berkeley.edu/sites/default/files/vinton_report_5.pdf](https://www.ischool.berkeley.edu/sites/default/files/vinton_report_5.pdf)

生成摘要时出错

---

## 32. A True Telnet BBS on a Casio Calculator

**原文标题**: A True Telnet BBS on a Casio Calculator

**原文链接**: [https://ei3lh.eu/2026/08/16/a-true-telnet-bbs-on-a-casio-calculator/](https://ei3lh.eu/2026/08/16/a-true-telnet-bbs-on-a-casio-calculator/)

生成摘要时出错

---

## 33. Nvidia dramatically reduces amount of OpenAI infra financing it may guarantee

**原文标题**: Nvidia dramatically reduces amount of OpenAI infra financing it may guarantee

**原文链接**: [https://www.reuters.com/business/nvidia-scales-back-250-billion-openai-data-center-guarantee-wsj-reports-2026-08-14/](https://www.reuters.com/business/nvidia-scales-back-250-billion-openai-data-center-guarantee-wsj-reports-2026-08-14/)

生成摘要时出错

---

## 34. A quick look at zero-knowledge proofs

**原文标题**: A quick look at zero-knowledge proofs

**原文链接**: [https://bernsteinbear.com/blog/zkp/](https://bernsteinbear.com/blog/zkp/)

生成摘要时出错

---

## 35. Chestnut – eGPU dock with open-source firmware

**原文标题**: Chestnut – eGPU dock with open-source firmware

**原文链接**: [https://hwbusters.com/news/comma-ai-egpu-dock-runs-open-source-firmware-249-bare-799-with-an-rx-9060/](https://hwbusters.com/news/comma-ai-egpu-dock-runs-open-source-firmware-249-bare-799-with-an-rx-9060/)

生成摘要时出错

---

## 36. Strong gravitational lensing and microlensing of supernovae (2024)

**原文标题**: Strong gravitational lensing and microlensing of supernovae (2024)

**原文链接**: [https://infoscience.epfl.ch/entities/publication/644cad8a-6c9b-4b02-bcf3-b8b6e8c614c5](https://infoscience.epfl.ch/entities/publication/644cad8a-6c9b-4b02-bcf3-b8b6e8c614c5)

生成摘要时出错

---

## 37. Show HN: A public AI whose memory is shared across all users

**原文标题**: Show HN: A public AI whose memory is shared across all users

**原文链接**: [https://wildstatic.com/](https://wildstatic.com/)

生成摘要时出错

---

## 38. Does anyone run Postgres without PgBouncer?

**原文标题**: Does anyone run Postgres without PgBouncer?

**原文链接**: [https://brandur.org/fragments/postgres-without-pgbouncer](https://brandur.org/fragments/postgres-without-pgbouncer)

生成摘要时出错

---

## 39. Anton Chekhov played at love most of his life

**原文标题**: Anton Chekhov played at love most of his life

**原文链接**: [https://commonreader.wustl.edu/winning-and-losing-at-the-great-game-of-intimacy/](https://commonreader.wustl.edu/winning-and-losing-at-the-great-game-of-intimacy/)

生成摘要时出错

---

## 40. Anthropic becomes the 'Apple of AI': Most revenue despite being most expensive

**原文标题**: Anthropic becomes the 'Apple of AI': Most revenue despite being most expensive

**原文链接**: [https://www.techradar.com/pro/anthropic-becomes-the-apple-of-ai-as-it-grabs-most-revenue-despite-being-the-most-expensive](https://www.techradar.com/pro/anthropic-becomes-the-apple-of-ai-as-it-grabs-most-revenue-despite-being-the-most-expensive)

生成摘要时出错

---

## 41. GIMP Development Update

**原文标题**: GIMP Development Update

**原文链接**: [https://www.gimp.org/news/2026/08/16/dev-update-august-2026/](https://www.gimp.org/news/2026/08/16/dev-update-august-2026/)

生成摘要时出错

---

## 42. Without a Theory of Intelligence

**原文标题**: Without a Theory of Intelligence

**原文链接**: [https://kk.org/thetechnium/without-a-theory-of-intelligence/](https://kk.org/thetechnium/without-a-theory-of-intelligence/)

生成摘要时出错

---

## 43. The AI Credit Resale Economy

**原文标题**: The AI Credit Resale Economy

**原文链接**: [https://vectoral.com/blog/who-are-the-token-brokers](https://vectoral.com/blog/who-are-the-token-brokers)

生成摘要时出错

---

## 44. Superconducting monolayer cuprate with a single CuO2 plane

**原文标题**: Superconducting monolayer cuprate with a single CuO2 plane

**原文链接**: [https://www.nature.com/articles/s41586-026-10857-1](https://www.nature.com/articles/s41586-026-10857-1)

生成摘要时出错

---

## 45. The beautiful mathematics behind OpenAI's sphere packing result

**原文标题**: The beautiful mathematics behind OpenAI's sphere packing result

**原文链接**: [https://www.empirical.health/blog/ai-math-sphere-packing/](https://www.empirical.health/blog/ai-math-sphere-packing/)

生成摘要时出错

---

## 46. $12B of US ratepayers' money wasted on a modeling mistake in PJM

**原文标题**: $12B of US ratepayers' money wasted on a modeling mistake in PJM

**原文链接**: [https://newsletter.semianalysis.com/p/12b-of-us-ratepayers-money-wasted](https://newsletter.semianalysis.com/p/12b-of-us-ratepayers-money-wasted)

生成摘要时出错

---

## 47. Research papers using "kidney disappointment" instead of "kidney failure"

**原文标题**: Research papers using "kidney disappointment" instead of "kidney failure"

**原文链接**: [https://scholar.google.com/scholar?q=%22kidney+disappointment%22](https://scholar.google.com/scholar?q=%22kidney+disappointment%22)

生成摘要时出错

---

## 48. Qwen 3.8 27B

**原文标题**: Qwen 3.8 27B

**原文链接**: [https://huggingface.co/Qwen/Qwen3.8-27B-FP8](https://huggingface.co/Qwen/Qwen3.8-27B-FP8)

生成摘要时出错

---

## 49. Binance gave Russia crypto donation records for Ukraine fundraisers

**原文标题**: Binance gave Russia crypto donation records for Ukraine fundraisers

**原文链接**: [https://www.reuters.com/legal/government/binance-gave-moscow-client-details-used-charge-russian-over-ukraine-donations-2026-08-17/](https://www.reuters.com/legal/government/binance-gave-moscow-client-details-used-charge-russian-over-ukraine-donations-2026-08-17/)

生成摘要时出错

---

## 50. Falstad Math and Physics Simulations

**原文标题**: Falstad Math and Physics Simulations

**原文链接**: [https://www.falstad.com/mathphysics.html](https://www.falstad.com/mathphysics.html)

生成摘要时出错

---

## 51. The deep history behind the Road to Nowhere inside the Great Smoky Mountains

**原文标题**: The deep history behind the Road to Nowhere inside the Great Smoky Mountains

**原文链接**: [https://www.wunc.org/environment/2026-08-10/road-to-nowhere-great-smoky-mountains](https://www.wunc.org/environment/2026-08-10/road-to-nowhere-great-smoky-mountains)

生成摘要时出错

---

## 52. Expert Witness Used ChatGPT to Write Report Defending Company in Lawsuit

**原文标题**: Expert Witness Used ChatGPT to Write Report Defending Company in Lawsuit

**原文链接**: [https://www.404media.co/show-how-3m-is-0-at-fault-expert-witness-used-chatgpt-to-write-report-defending-company-in-deadly-explosion-lawsuit/](https://www.404media.co/show-how-3m-is-0-at-fault-expert-witness-used-chatgpt-to-write-report-defending-company-in-deadly-explosion-lawsuit/)

生成摘要时出错

---

## 53. EFF Joins Calling on Governor to Reject the Stealth Crawler Prohibition Act

**原文标题**: EFF Joins Calling on Governor to Reject the Stealth Crawler Prohibition Act

**原文链接**: [https://www.eff.org/deeplinks/2026/08/eff-joins-18-civil-rights-organizations-calling-governor-hochul-reject-stealth](https://www.eff.org/deeplinks/2026/08/eff-joins-18-civil-rights-organizations-calling-governor-hochul-reject-stealth)

生成摘要时出错

---

## 54. Clamiga: Common Lisp for the Amiga

**原文标题**: Clamiga: Common Lisp for the Amiga

**原文链接**: [https://nnamgreb.de/blog/Clamiga+-+Common+Lisp+for+the+Amiga](https://nnamgreb.de/blog/Clamiga+-+Common+Lisp+for+the+Amiga)

生成摘要时出错

---

## 55. The weekend is 100 years old

**原文标题**: The weekend is 100 years old

**原文链接**: [https://www.theguardian.com/money/2026/aug/16/the-weekend-is-100-years-old-skiveday-fridays-and-hybrid-working-ruined-it](https://www.theguardian.com/money/2026/aug/16/the-weekend-is-100-years-old-skiveday-fridays-and-hybrid-working-ruined-it)

生成摘要时出错

---

## 56. Patterns and problems in emerging multi-agent systems

**原文标题**: Patterns and problems in emerging multi-agent systems

**原文链接**: [https://www.anthropic.com/research/multiagent-systems](https://www.anthropic.com/research/multiagent-systems)

生成摘要时出错

---

## 57. Plastic mechanical computer from 1963: The Digi-Comp 1 [video]

**原文标题**: Plastic mechanical computer from 1963: The Digi-Comp 1 [video]

**原文链接**: [https://www.youtube.com/watch?v=-y8bGBE71yw](https://www.youtube.com/watch?v=-y8bGBE71yw)

生成摘要时出错

---

## 58. Archie G. Norcross' Maine Forest Fire Maps (1918–22)

**原文标题**: Archie G. Norcross' Maine Forest Fire Maps (1918–22)

**原文链接**: [https://publicdomainreview.org/collection/maine-forest-fire-maps/](https://publicdomainreview.org/collection/maine-forest-fire-maps/)

生成摘要时出错

---

## 59. Software That Implements Itself

**原文标题**: Software That Implements Itself

**原文链接**: [https://achad4.substack.com/p/software-that-implements-itself](https://achad4.substack.com/p/software-that-implements-itself)

生成摘要时出错

---

## 60. What 15M Gemini conversations tell us about AI at work

**原文标题**: What 15M Gemini conversations tell us about AI at work

**原文链接**: [https://leaddev.com/ai/what-15-million-gemini-conversations-tell-us-about-ai-at-work](https://leaddev.com/ai/what-15-million-gemini-conversations-tell-us-about-ai-at-work)

生成摘要时出错

---

## 61. Show HN: Mic Drop, a real-time multiplayer karaoke game

**原文标题**: Show HN: Mic Drop, a real-time multiplayer karaoke game

**原文链接**: [https://www.micdrop.gg/](https://www.micdrop.gg/)

生成摘要时出错

---

## 62. AI Coding Without the Vibes

**原文标题**: AI Coding Without the Vibes

**原文链接**: [https://peterbloem.nl/blog/craft-coding](https://peterbloem.nl/blog/craft-coding)

生成摘要时出错

---

## 63. Firefox for iOS now has a native adblocker

**原文标题**: Firefox for iOS now has a native adblocker

**原文链接**: [https://support.mozilla.org/en-US/kb/block-ads-firefox-ios](https://support.mozilla.org/en-US/kb/block-ads-firefox-ios)

生成摘要时出错

---

## 64. St Lucie Nuclear Reactor Unit 1 manually shutdown, 3 control rods drop into core

**原文标题**: St Lucie Nuclear Reactor Unit 1 manually shutdown, 3 control rods drop into core

**原文链接**: [https://www.wptv.com/news/treasure-coast/region-st-lucie-county/saint-lucie-nuclear-power-plant-unit-1-manually-shut-down-after-3-control-rods-drop-into-reactor-core](https://www.wptv.com/news/treasure-coast/region-st-lucie-county/saint-lucie-nuclear-power-plant-unit-1-manually-shut-down-after-3-control-rods-drop-into-reactor-core)

生成摘要时出错

---

## 65. Models Are Getting Dumber on Purpose

**原文标题**: Models Are Getting Dumber on Purpose

**原文链接**: [https://w4g1.dev/blog/models-are-getting-dumber-on-purpose](https://w4g1.dev/blog/models-are-getting-dumber-on-purpose)

生成摘要时出错

---

## 66. GLM-5.3: Frontier coding with emergent cyber capabilities

**原文标题**: GLM-5.3: Frontier coding with emergent cyber capabilities

**原文链接**: [https://z.ai/blog/glm-5.3](https://z.ai/blog/glm-5.3)

生成摘要时出错

---

## 67. Self hosted email continues to steeply decline

**原文标题**: Self hosted email continues to steeply decline

**原文链接**: [https://labs.ripe.net/author/artem-berezin/two-providers-a-stubborn-plateau-and-a-very-long-tail-email-in-the-tranco-top-1m/](https://labs.ripe.net/author/artem-berezin/two-providers-a-stubborn-plateau-and-a-very-long-tail-email-in-the-tranco-top-1m/)

生成摘要时出错

---

## 68. At-home test for infected ticks could improve Lyme Disease diagnosis

**原文标题**: At-home test for infected ticks could improve Lyme Disease diagnosis

**原文链接**: [https://www.smithsonianmag.com/innovation/the-first-at-home-test-for-infected-ticks-could-improve-lyme-disease-diagnosis-180989235/](https://www.smithsonianmag.com/innovation/the-first-at-home-test-for-infected-ticks-could-improve-lyme-disease-diagnosis-180989235/)

生成摘要时出错

---

## 69. Sectorforth is a 16-bit x86 Forth that fits in a 512-byte boot sector

**原文标题**: Sectorforth is a 16-bit x86 Forth that fits in a 512-byte boot sector

**原文链接**: [https://github.com/cesarblum/sectorforth](https://github.com/cesarblum/sectorforth)

生成摘要时出错

---

## 70. Cultivating a state of mind where new ideas are born (2023)

**原文标题**: Cultivating a state of mind where new ideas are born (2023)

**原文链接**: [https://www.henrikkarlsson.xyz/p/good-ideas](https://www.henrikkarlsson.xyz/p/good-ideas)

生成摘要时出错

---

## 71. Auto-research with codex: How I achieved a 232x Faster Kernel

**原文标题**: Auto-research with codex: How I achieved a 232x Faster Kernel

**原文链接**: [https://sankalp.bearblog.dev/autoresearch/](https://sankalp.bearblog.dev/autoresearch/)

生成摘要时出错

---

## 72. AI-Assisted GPU Porting of a 250k Line Legacy Weather Simulation Code

**原文标题**: AI-Assisted GPU Porting of a 250k Line Legacy Weather Simulation Code

**原文链接**: [https://arxiv.org/abs/2608.13122](https://arxiv.org/abs/2608.13122)

生成摘要时出错

---

## 73. AdNauseam – Clicking ads so you don't have to

**原文标题**: AdNauseam – Clicking ads so you don't have to

**原文链接**: [https://adnauseam.io/](https://adnauseam.io/)

生成摘要时出错

---

## 74. Semaglutide linked to lower predicted dementia risk

**原文标题**: Semaglutide linked to lower predicted dementia risk

**原文链接**: [https://alz-journals.onlinelibrary.wiley.com/doi/10.1002/dad2.70432](https://alz-journals.onlinelibrary.wiley.com/doi/10.1002/dad2.70432)

生成摘要时出错

---

## 75. In the Shadow of the (Berlin) Wall

**原文标题**: In the Shadow of the (Berlin) Wall

**原文链接**: [https://www.slowtravelberlin.com/in-the-shadow-of-the-berlin-wall/](https://www.slowtravelberlin.com/in-the-shadow-of-the-berlin-wall/)

生成摘要时出错

---

## 76. If Meta loses this trial, Instagram and Facebook could change forever

**原文标题**: If Meta loses this trial, Instagram and Facebook could change forever

**原文链接**: [https://www.bbc.com/news/articles/clyqpx6xk69o](https://www.bbc.com/news/articles/clyqpx6xk69o)

生成摘要时出错

---

## 77. Why does Opus 5 feel worse to work with?

**原文标题**: Why does Opus 5 feel worse to work with?

**原文链接**: [https://mun-logadan.github.io/why-does-opus-5-feel-worse/](https://mun-logadan.github.io/why-does-opus-5-feel-worse/)

生成摘要时出错

---

## 78. NIH is ending a key grant for budding clinical researchers

**原文标题**: NIH is ending a key grant for budding clinical researchers

**原文链接**: [https://www.science.org/content/article/nih-ending-key-grant-budding-clinical-researchers](https://www.science.org/content/article/nih-ending-key-grant-budding-clinical-researchers)

生成摘要时出错

---

## 79. The federal keyword lists that canceled billions in research funding

**原文标题**: The federal keyword lists that canceled billions in research funding

**原文链接**: [https://www.highereddive.com/news/inside-the-federal-keyword-lists-that-canceled-billions-in-research-funding/826203/](https://www.highereddive.com/news/inside-the-federal-keyword-lists-that-canceled-billions-in-research-funding/826203/)

生成摘要时出错

---

## 80. Health benefits of Tai Chi

**原文标题**: Health benefits of Tai Chi

**原文链接**: [https://www.health.harvard.edu/exercise-and-fitness/the-health-benefits-of-tai-chi](https://www.health.harvard.edu/exercise-and-fitness/the-health-benefits-of-tai-chi)

生成摘要时出错

---

## 81. Design 3D-printable parts by talking

**原文标题**: Design 3D-printable parts by talking

**原文链接**: [https://nurb.dev/](https://nurb.dev/)

生成摘要时出错

---

## 82. RISC-V: They Should Have Known Better

**原文标题**: RISC-V: They Should Have Known Better

**原文链接**: [https://dmitry.gr/?r=06.%20Thoughts&proj=12.%20RV](https://dmitry.gr/?r=06.%20Thoughts&proj=12.%20RV)

生成摘要时出错

---

## 83. Abdominal fat predicts heart disease risk better than BMI

**原文标题**: Abdominal fat predicts heart disease risk better than BMI

**原文链接**: [https://www.acc.org/about-acc/press-releases/2026/08/11/14/59/abdominal-fat-predicts-heart-disease-risk-better-than-bmi](https://www.acc.org/about-acc/press-releases/2026/08/11/14/59/abdominal-fat-predicts-heart-disease-risk-better-than-bmi)

生成摘要时出错

---

## 84. AI in drug discovery – what it is, where we stand and the path forward

**原文标题**: AI in drug discovery – what it is, where we stand and the path forward

**原文链接**: [https://www.science.org/content/blog-post/so-how-ai-drug-discovery-doing-really](https://www.science.org/content/blog-post/so-how-ai-drug-discovery-doing-really)

生成摘要时出错

---

## 85. Using GCC's Nested Functions with Wide Pointers and No Trampolines II

**原文标题**: Using GCC's Nested Functions with Wide Pointers and No Trampolines II

**原文链接**: [https://uecker.codeberg.page/2026-07-14.html](https://uecker.codeberg.page/2026-07-14.html)

生成摘要时出错

---

## 86. Tess's Android Wayland Compositor

**原文标题**: Tess's Android Wayland Compositor

**原文链接**: [https://github.com/wmww/tawc](https://github.com/wmww/tawc)

生成摘要时出错

---

## 87. XCancel – An Unofficial Twitter/X Mirror

**原文标题**: XCancel – An Unofficial Twitter/X Mirror

**原文链接**: [https://xcancel.com/about](https://xcancel.com/about)

生成摘要时出错

---

## 88. Show HN: PageSieve, a web scraping browser extension

**原文标题**: Show HN: PageSieve, a web scraping browser extension

**原文链接**: [https://julius383.github.io/PageSieve/](https://julius383.github.io/PageSieve/)

生成摘要时出错

---

