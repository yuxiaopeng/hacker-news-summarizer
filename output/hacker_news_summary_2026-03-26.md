# Hacker News 热门文章摘要 (2026-03-26)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 从 GitHub 迁移到 Codeberg：懒人版

**原文标题**: Moving from GitHub to Codeberg, for lazy people

**原文链接**: [https://unterwaditzer.net/2025/codeberg.html](https://unterwaditzer.net/2025/codeberg.html)

本文为从 GitHub 迁移到 Codeberg 提供了一份指南，旨在帮助追求最简迁移过程的用户。作者认为，虽然迁移看似令人望而生畏，但对大多数项目而言其实非常直接。

**迁移要点：**
*   **仓库数据：** Codeberg 的内置导入工具可无缝迁移 Issue、拉取请求（PR）和 Release。它保留了原始的 Issue 编号、标签和作者信息，且用户界面与 GitHub 几乎一致。
*   **网页托管：** GitHub Pages 的用户可以转用 `codeberg.page`（或 `grebedoc.dev` 等替代方案）。工作流程保持不变：即向特定分支推送 HTML 内容。
*   **持续集成 (CI)：** 这是最具挑战性的部分，因为 GitHub 提供了免费的 macOS 运行器和高容量支持。作者建议“懒人”迁移者优先选择 **Forgejo Actions** 而非 Woodpecker CI，因为其语法和 UI 与 GitHub Actions 几乎完全相同。这允许用户通过简单地在特定 Action 中使用完整的 GitHub URL 来复用现有工作流。
*   **处理旧仓库：** 为避免链接失效（404 错误），作者建议将 GitHub 仓库存档并更新 README，而不是删除 Issue 或整个仓库。对于仍需 GitHub 特定 CI 功能的用户，将提交从 Codeberg 镜像回 GitHub 是一个有效的折中方案。

总之，尽管在 CI 容量和 macOS 支持方面需要做出一些牺牲，但 Codeberg 熟悉的工具和自动化导入功能让这一过渡变得十分便捷。

---

## 2. 我对 LiteLLM 恶意软件攻击的逐分钟应对记录

**原文标题**: My minute-by-minute response to the LiteLLM malware attack

**原文链接**: [https://futuresearch.ai/blog/litellm-attack-transcript/](https://futuresearch.ai/blog/litellm-attack-transcript/)

本文详细记录了 2026 年 3 月 24 日针对 `litellm` Python 软件包（v1.82.8）供应链攻击的快速响应过程。通过使用 AI 开发者工具“Claude Code”，一名用户在短短 72 分钟内将一次针对系统死机的常规调查转化为一次完整的恶意软件分析和公开披露。

该事件始于一个被植入病毒的 `litellm` 版本作为依赖项被拉取，随后触发了产生 11,000 个 Python 进程的“分叉炸弹”（fork bomb），导致系统被迫硬重启。虽然用户起初怀疑是 AI 工具自身出现了死循环，但 Claude Code 通过对系统日志和 `htop` 负载进行取证分析，最终锁定了罪魁祸首：`litellm_init.pth`。该恶意文件旨在每次 Python 启动时自动执行，以窃取 SSH 密钥、AWS 机密和 Kubernetes 令牌等敏感凭据，并将其外泄至虚假域名（`models.litellm.cloud`）。此外，它还试图通过隐藏的 systemd 服务建立持久化攻击。

AI 智能体在以下方面发挥了关键作用：
1.  **取证分析：** 解码 base64 负载并解析系统日志，将进程激增追溯至受感染的软件包。
2.  **验证：** 在隔离的 Docker 环境中证实了 PyPI 上存在的实时感染。
3.  **快速响应：** 自动处理披露流程，在仅三分钟内便完成了博客草案撰写及 PR 的管理与合并。

作者总结认为，AI 工具显著降低了非安全专业人员进行复杂取证研究和事件响应的门槛。然而，此次经历也表明，前沿 AI 模型应当被训练得对潜在安全威胁更具警惕性，因为最初正是通过人工干预，才引导 AI 纠正了将异常行为误认为良性 Bug 的倾向。

---

## 3. 为什么这么多控制室都是海泡绿 (2025)

**原文标题**: Why so many control rooms were seafoam green (2025)

**原文链接**: [https://bethmathews.substack.com/p/why-so-many-control-rooms-were-seafoam](https://bethmathews.substack.com/p/why-so-many-control-rooms-were-seafoam)

《为什么那么多控制室都是海泡绿色的》一文探讨了20世纪中期技术环境（如美国航天局任务控制中心和核电站）中随处可见的薄荷绿美学背后，深思熟虑的心理与实用原因。

选择这种被称为“远景绿”（Vista Green）或“护眼绿”（Eye-Rest Green）的特定色调，很大程度上是由色彩顾问费伯·比伦（Faber Birren）推动的。其关键因素包括：

*   **心理调节：** 在高压环境下，绿色被认为是最能让人平静的颜色。工业设计师利用它来降低血压、缓解焦虑，并让操作人员在长班期间保持专注。
*   **视觉工效学：** 这种色调旨在最大限度地减轻眼部疲劳。它提供了中性且低眩光的背景，使黑白仪表盘和红色警示灯能清晰显现，既不像白色那样刺眼，也不像灰色那样沉闷。
*   **工业实用性：** 除了美学考量，这种颜色还能非常有效地掩盖污迹、指纹和机油。
*   **标准化：** 该颜色成为了政府和军事标准（联邦标准595）。这使得来自不同制造商的设备在安装到同一设施时，颜色能够完美匹配。

随着从物理模拟仪表向数字电脑显示器的转型，“海泡绿时代”最终走向衰落。深灰色和蓝色成为了减少 CRT 和 LCD 屏幕眩光的新标准。如今，这种颜色被视为一种“复古未来主义”的标志，记录了工业设计开始优先考虑人类生理特征以应对机器时代复杂性的特定时期。

---

## 4. OpenTelemetry Profiles 进入公开 Alpha 阶段

**原文标题**: OpenTelemetry profiles enters public alpha

**原文链接**: [https://opentelemetry.io/blog/2026/profiles-alpha/](https://opentelemetry.io/blog/2026/profiles-alpha/)

OpenTelemetry 正式宣布其 **Profiles**（性能剖析）信号已进入 **公开 Alpha 阶段**，这标志着在建立供应商中立的持续生产性能剖析行业标准方面迈出了重要一步。继链路追踪（Traces）、指标（Metrics）和日志（Logs）之后，Profiles 提供了一个统一的框架，帮助组织排查故障并优化资源消耗。

Alpha 版本的主要亮点包括：

*   **标准化数据表示**：OTLP Profiles 格式提供高效的去重调用栈编码和字典表，可将传输数据大小减少 40%。它保持了与流行的 `pprof` 格式的双向兼容性，同时能够通过 `trace_id` 和 `span_id` 实现跨信号关联。
*   **eBPF 剖析代理**：最初由 Elastic 捐赠的参考 eBPF 代理可提供低开销的全系统剖析。Alpha 版本新增了对 ARM64 (Node.js)、.NET 9 和 10、Go 符号化的支持，以及对 BEAM (Erlang/Elixir) 的初步支持。
*   **生态系统集成**：OpenTelemetry Collector 现在已支持 Profiles，允许用户接入 `pprof` 文件，使用 OTTL 进行数据转换，并通过 `k8sattributesprocessor` 利用 Kubernetes 元数据增强剖析数据。
*   **落地工具**：为了方便实验，官方发布了一致性检查器来验证数据质量。此外，Elastic 还开源了 **devfiler**，这是一款作为测试和可视化本地后端的桌面应用程序。

虽然该信号目前处于 Alpha 阶段，尚不建议用于关键生产负载，但 Profiling SIG 正寻求社区反馈以完善规范。随着项目向 Beta 和正式发布（GA）迈进，未来的工作重点将是标准化符号化 API，并改进基于 eBPF 的代理与进程内 SDK 之间的关联。

---

## 5. Colibri —— 为各种规模社区打造的基于 AT 协议的聊天平台

**原文标题**: Colibri – chat platform built on the AT Protocol for communities big and small

**原文链接**: [https://colibri.social/](https://colibri.social/)

**Colibri** 是一款基于去中心化 **AT Protocol**（与 Bluesky 相同的底层技术）构建的开源聊天和社区平台。它专为各种规模的社区设计，核心关注用户数据所有权并防止平台锁定。由于其去中心化的特性，用户真正拥有自己的个人资料和消息，并能自由地在不同服务器间迁移数据。

**核心特性与功能：**
*   **沟通工具：** 平台支持实时文字聊天、即插即用的语音和视频通话，以及有条理的论坛式讨论。
*   **社区管理：** 管理员可以设置自定义角色和权限，并利用内置的审核工具来管理其空间。
*   **生态集成：** 用户可以使用现有的 **Bluesky 账号** 或自己的 **个人数据服务器 (PDS)** 无缝登录。
*   **托管选项：** Colibri 提供自有的 PDS 托管服务 (colibri.social)，并为有需求的用户提供数据迁移支持。

**隐私与数据处理：**
虽然 Colibri 与 Bluesky 运行在同一网络上，但消息存储在独立的“集合”中，这意味着聊天记录不会作为公开帖子出现在 Bluesky 上。该平台目前专注于公开社区，但计划随着 AT Protocol 对私有数据支持的演进，推出私密群聊功能。

总之，Colibri 通过优先考虑开放标准、互操作性以及用户对个人数据的绝对控制权，为传统聊天平台提供了一个面向未来的去中心化替代方案。

---

## 6. 个人百科全书

**原文标题**: Personal Encyclopedias

**原文链接**: [https://whoami.wiki/blog/personal-encyclopedias](https://whoami.wiki/blog/personal-encyclopedias)

在《个人百科全书》（Personal Encyclopedias）中，作者描述了一个家庭历史项目如何演变成一个用于数字保存的开源工具。这段旅程始于作者在祖母家发现了1351张纸质家庭照片。为了保存这些照片背后的故事，作者采访了祖母，并利用本地部署的 MediaWiki 为她的婚礼创建了一个维基百科风格的词条，其中包含历史背景链接和家庭成员“小作品”（stubs）。

随着作者整合数字数据，该项目不断扩大。利用人工智能（特别是 Claude Code），作者实现了从数千张数字照片和视频中自动创建维基页面的功能。通过向 AI 提供各种导出的数据——包括 Google 地图时间轴、银行交易记录、Uber 行程和 Shazam 识别历史——模型能够交叉引用细节，重构出极其具体的叙述，例如识别多年前的餐厅、足球比赛或背景音乐。

进一步整合 WhatsApp 和 Facebook 的聊天记录后，AI 能够追踪友谊的长期脉络。这种结构化、互联的格式揭示了被遗忘的记忆，并加深了作者与家人和朋友之间的情感联系。

意识到使用百科全书软件整理一生数据的强大力量后，作者创建了 whoami.wiki。该项目现已作为开源项目发布，允许用户构建私密、可搜索且本地托管的个人百科全书。该工具利用了大语言模型对维基百科结构已经非常熟悉的特性，使其能够将原始导出数据转化为可浏览的人生记录，同时确保数据的私密性和安全性。

---

## 7. HyperAgents：自引用自改进智能体

**原文标题**: HyperAgents: Self-referential self-improving agents

**原文链接**: [https://github.com/facebookresearch/hyperagents](https://github.com/facebookresearch/hyperagents)

**HyperAgents** is a framework designed to create self-referential, self-improving AI agents capable of optimizing for any computable task. Detailed in a 2026 research paper by Jenny Zhang et al., the system utilizes a dual-agent architecture—comprising a **meta-agent** and a **task-agent**—to iteratively refine performance across various domains.

The framework is built to leverage foundation models from providers such as OpenAI, Anthropic, and Gemini. Its technical implementation relies on a loop-based optimization process, where the meta-agent analyzes and modifies the task-agent’s code to improve its efficiency or success rate. The repository includes comprehensive setup instructions requiring Python 3.12, Docker, and several system-level dependencies (like Graphviz and CMake). The primary entry point for the algorithm is `generate_loop.py`, which coordinates the interaction between the agents and the target domains.

A critical aspect of the project is its **safety consideration**. The authors issue a strong warning that the framework involves executing untrusted, model-generated code. While they suggest that overtly malicious actions are unlikely with current models, they acknowledge risks of destructive behavior arising from model limitations or alignment issues. 

For researchers and developers, the project provides archived experiment logs and a standardized citation format. Overall, HyperAgents serves as a platform for exploring autonomous self-optimization and the capabilities of self-improving software architectures in the field of artificial intelligence.

---

## 8. 互操作性可以拯救开放网络 (2023)

**原文标题**: Interoperability Can Save the Open Web (2023)

**原文链接**: [https://spectrum.ieee.org/doctorow-interoperability](https://spectrum.ieee.org/doctorow-interoperability)

生成摘要时出错

---

## 9. Show HN: Claude skill that evaluates B2B vendors by talking to their AI agents

**原文标题**: Show HN: Claude skill that evaluates B2B vendors by talking to their AI agents

**原文链接**: [https://github.com/salespeak-ai/buyer-eval-skill](https://github.com/salespeak-ai/buyer-eval-skill)

生成摘要时出错

---

## 10. Doom entirely from DNS records

**原文标题**: Doom entirely from DNS records

**原文链接**: [https://github.com/resumex/doom-over-dns](https://github.com/resumex/doom-over-dns)

生成摘要时出错

---

## 11. Building a Blog with Elixir and Phoenix

**原文标题**: Building a Blog with Elixir and Phoenix

**原文链接**: [https://jola.dev/posts/building-a-blog-with-elixir-and-phoenix](https://jola.dev/posts/building-a-blog-with-elixir-and-phoenix)

生成摘要时出错

---

## 12. From zero to a RAG system: successes and failures

**原文标题**: From zero to a RAG system: successes and failures

**原文链接**: [https://en.andros.dev/blog/aa31d744/from-zero-to-a-rag-system-successes-and-failures/](https://en.andros.dev/blog/aa31d744/from-zero-to-a-rag-system-successes-and-failures/)

生成摘要时出错

---

## 13. My home network observes bedtime with OpenBSD and pf

**原文标题**: My home network observes bedtime with OpenBSD and pf

**原文链接**: [https://ratfactor.com/openbsd/pf-gateway-bedtime](https://ratfactor.com/openbsd/pf-gateway-bedtime)

生成摘要时出错

---

## 14. “聊天监控”终结：欧洲议会叫停大规模监控

**原文标题**: End of "Chat Control": EU parliament stops mass surveillance

**原文链接**: [https://www.patrick-breyer.de/en/end-of-chat-control-eu-parliament-stops-mass-surveillance-in-voting-thriller-paving-the-way-for-genuine-child-protection/](https://www.patrick-breyer.de/en/end-of-chat-control-eu-parliament-stops-mass-surveillance-in-voting-thriller-paving-the-way-for-genuine-child-protection/)

生成摘要时出错

---

## 15. Running Tesla Model 3's computer on my desk using parts from crashed cars

**原文标题**: Running Tesla Model 3's computer on my desk using parts from crashed cars

**原文链接**: [https://bugs.xdavidhu.me/tesla/2026/03/23/running-tesla-model-3s-computer-on-my-desk-using-parts-from-crashed-cars/](https://bugs.xdavidhu.me/tesla/2026/03/23/running-tesla-model-3s-computer-on-my-desk-using-parts-from-crashed-cars/)

生成摘要时出错

---

## 16. Swift 6.3

**原文标题**: Swift 6.3

**原文链接**: [https://www.swift.org/blog/swift-6.3-released/](https://www.swift.org/blog/swift-6.3-released/)

生成摘要时出错

---

## 17. Light on Glass: Why do you start making a game engine?

**原文标题**: Light on Glass: Why do you start making a game engine?

**原文链接**: [https://analogdreamdev.substack.com/p/light-on-glass](https://analogdreamdev.substack.com/p/light-on-glass)

生成摘要时出错

---

## 18. Stripe Projects: Provision and manage services from the CLI

**原文标题**: Stripe Projects: Provision and manage services from the CLI

**原文链接**: [https://projects.dev/](https://projects.dev/)

生成摘要时出错

---

## 19. Obsolete Sounds

**原文标题**: Obsolete Sounds

**原文链接**: [https://citiesandmemory.com/obsolete-sounds/](https://citiesandmemory.com/obsolete-sounds/)

生成摘要时出错

---

## 20. Shell Tricks That Make Life Easier (and Save Your Sanity)

**原文标题**: Shell Tricks That Make Life Easier (and Save Your Sanity)

**原文链接**: [https://blog.hofstede.it/shell-tricks-that-actually-make-life-easier-and-save-your-sanity/](https://blog.hofstede.it/shell-tricks-that-actually-make-life-easier-and-save-your-sanity/)

生成摘要时出错

---

## 21. SpaceStarCarz KoolWheelz Paper Models

**原文标题**: SpaceStarCarz KoolWheelz Paper Models

**原文链接**: [https://davesdesigns.ca/dcc/html/spacestarcarz_.html](https://davesdesigns.ca/dcc/html/spacestarcarz_.html)

生成摘要时出错

---

## 22. Intel Announces Arc Pro B70 and Arc Pro B65 GPUs

**原文标题**: Intel Announces Arc Pro B70 and Arc Pro B65 GPUs

**原文链接**: [https://www.techpowerup.com/347703/intel-announces-arc-pro-b70-and-arc-pro-b65-gpus-maxes-out-xe2-battlemage-architecture](https://www.techpowerup.com/347703/intel-announces-arc-pro-b70-and-arc-pro-b65-gpus-maxes-out-xe2-battlemage-architecture)

生成摘要时出错

---

## 23. Niche Museums

**原文标题**: Niche Museums

**原文链接**: [https://www.niche-museums.com/](https://www.niche-museums.com/)

生成摘要时出错

---

## 24. Optimizing a lock-free ring buffer

**原文标题**: Optimizing a lock-free ring buffer

**原文链接**: [https://david.alvarezrosa.com/posts/optimizing-a-lock-free-ring-buffer/](https://david.alvarezrosa.com/posts/optimizing-a-lock-free-ring-buffer/)

生成摘要时出错

---

## 25. Ashby (YC W19) Is Hiring Engineers Who Make Product Decisions

**原文标题**: Ashby (YC W19) Is Hiring Engineers Who Make Product Decisions

**原文链接**: [https://www.ashbyhq.com/careers?ashby_jid=c3c7125d-7883-4dff-a2bf-f5a55de4a364&utm_source=hn](https://www.ashbyhq.com/careers?ashby_jid=c3c7125d-7883-4dff-a2bf-f5a55de4a364&utm_source=hn)

生成摘要时出错

---

## 26. AI users whose lives were wrecked by delusion

**原文标题**: AI users whose lives were wrecked by delusion

**原文链接**: [https://www.theguardian.com/lifeandstyle/2026/mar/26/ai-chatbot-users-lives-wrecked-by-delusion](https://www.theguardian.com/lifeandstyle/2026/mar/26/ai-chatbot-users-lives-wrecked-by-delusion)

生成摘要时出错

---

## 27. ARC-AGI-3

**原文标题**: ARC-AGI-3

**原文链接**: [https://arcprize.org/arc-agi/3](https://arcprize.org/arc-agi/3)

生成摘要时出错

---

## 28. Optimization lessons from a Minecraft structure locator

**原文标题**: Optimization lessons from a Minecraft structure locator

**原文链接**: [https://purplesyringa.moe/blog/optimization-lessons-from-a-minecraft-structure-locator/](https://purplesyringa.moe/blog/optimization-lessons-from-a-minecraft-structure-locator/)

生成摘要时出错

---

## 29. Earthquake scientists reveal how overplowing weakens soil at experimental farm

**原文标题**: Earthquake scientists reveal how overplowing weakens soil at experimental farm

**原文链接**: [https://www.washington.edu/news/2026/03/19/earthquake-scientists-reveal-how-overplowing-weakens-soil-at-experimental-farm/](https://www.washington.edu/news/2026/03/19/earthquake-scientists-reveal-how-overplowing-weakens-soil-at-experimental-farm/)

生成摘要时出错

---

## 30. French e, è, é, ê, ë – what's the difference?

**原文标题**: French e, è, é, ê, ë – what's the difference?

**原文链接**: [https://jakubmarian.com/french-e-e-e-e-e-whats-the-difference/](https://jakubmarian.com/french-e-e-e-e-e-whats-the-difference/)

生成摘要时出错

---

## 31. My DIY FPGA board can run Quake II

**原文标题**: My DIY FPGA board can run Quake II

**原文链接**: [https://blog.mikhe.ch/quake2-on-fpga/part4.html](https://blog.mikhe.ch/quake2-on-fpga/part4.html)

生成摘要时出错

---

## 32. LibreOffice and the art of overreacting

**原文标题**: LibreOffice and the art of overreacting

**原文链接**: [https://blog.documentfoundation.org/blog/2026/03/25/libreoffice-and-the-art-of-overreacting/](https://blog.documentfoundation.org/blog/2026/03/25/libreoffice-and-the-art-of-overreacting/)

生成摘要时出错

---

## 33. What came after the 486?

**原文标题**: What came after the 486?

**原文链接**: [https://dfarq.homeip.net/what-came-after-486/](https://dfarq.homeip.net/what-came-after-486/)

生成摘要时出错

---

## 34. More precise elevation data for GraphHopper routing engine

**原文标题**: More precise elevation data for GraphHopper routing engine

**原文链接**: [https://www.graphhopper.com/blog/2026/03/23/more-precise-elevation-data-for-graphhopper/](https://www.graphhopper.com/blog/2026/03/23/more-precise-elevation-data-for-graphhopper/)

生成摘要时出错

---

## 35. Government agencies buy commercial data about Americans in bulk

**原文标题**: Government agencies buy commercial data about Americans in bulk

**原文链接**: [https://www.npr.org/2026/03/25/nx-s1-5752369/ice-surveillance-data-brokers-congress-anthropic](https://www.npr.org/2026/03/25/nx-s1-5752369/ice-surveillance-data-brokers-congress-anthropic)

生成摘要时出错

---

## 36. Two studies in compiler optimisations

**原文标题**: Two studies in compiler optimisations

**原文链接**: [https://www.hmpcabral.com/2026/03/20/two-studies-in-compiler-optimisations/](https://www.hmpcabral.com/2026/03/20/two-studies-in-compiler-optimisations/)

生成摘要时出错

---

## 37. The truth that haunts the Ramones: 'They sold more T-shirts than records'

**原文标题**: The truth that haunts the Ramones: 'They sold more T-shirts than records'

**原文链接**: [https://english.elpais.com/culture/2026-03-17/the-uncomfortable-truth-that-will-always-haunt-the-ramones-they-sold-more-t-shirts-than-records.html](https://english.elpais.com/culture/2026-03-17/the-uncomfortable-truth-that-will-always-haunt-the-ramones-they-sold-more-t-shirts-than-records.html)

生成摘要时出错

---

## 38. Jury finds Meta liable in case over child sexual exploitation on its platforms

**原文标题**: Jury finds Meta liable in case over child sexual exploitation on its platforms

**原文链接**: [https://www.cnn.com/2026/03/24/tech/meta-new-mexico-trial-jury-deliberation](https://www.cnn.com/2026/03/24/tech/meta-new-mexico-trial-jury-deliberation)

生成摘要时出错

---

## 39. Quantization from the Ground Up

**原文标题**: Quantization from the Ground Up

**原文链接**: [https://ngrok.com/blog/quantization](https://ngrok.com/blog/quantization)

生成摘要时出错

---

## 40. Newly purchased Vizio TVs now require Walmart accounts to use smart features

**原文标题**: Newly purchased Vizio TVs now require Walmart accounts to use smart features

**原文链接**: [https://arstechnica.com/gadgets/2026/03/newly-purchased-vizio-tvs-now-require-walmart-accounts-to-use-smart-features/](https://arstechnica.com/gadgets/2026/03/newly-purchased-vizio-tvs-now-require-walmart-accounts-to-use-smart-features/)

生成摘要时出错

---

## 41. Show HN: Optio – Orchestrate AI coding agents in K8s to go from ticket to PR

**原文标题**: Show HN: Optio – Orchestrate AI coding agents in K8s to go from ticket to PR

**原文链接**: [https://github.com/jonwiggins/optio](https://github.com/jonwiggins/optio)

生成摘要时出错

---

## 42. AMD Announces the Ryzen 9 9950X3D2

**原文标题**: AMD Announces the Ryzen 9 9950X3D2

**原文链接**: [https://www.phoronix.com/news/AMD-Ryzen-9-9950X3D2](https://www.phoronix.com/news/AMD-Ryzen-9-9950X3D2)

生成摘要时出错

---

## 43. Show HN: A plain-text cognitive architecture for Claude Code

**原文标题**: Show HN: A plain-text cognitive architecture for Claude Code

**原文链接**: [https://lab.puga.com.br/cog/](https://lab.puga.com.br/cog/)

生成摘要时出错

---

## 44. My astrophotography in the movie Project Hail Mary

**原文标题**: My astrophotography in the movie Project Hail Mary

**原文链接**: [https://rpastro.square.site/s/stories/phm](https://rpastro.square.site/s/stories/phm)

生成摘要时出错

---

## 45. Apple randomly closes bug reports unless you "verify" the bug remains unfixed

**原文标题**: Apple randomly closes bug reports unless you "verify" the bug remains unfixed

**原文链接**: [https://lapcatsoftware.com/articles/2026/3/11.html](https://lapcatsoftware.com/articles/2026/3/11.html)

生成摘要时出错

---

## 46. Show HN: Robust LLM Extractor for Websites in TypeScript

**原文标题**: Show HN: Robust LLM Extractor for Websites in TypeScript

**原文链接**: [https://github.com/lightfeed/extractor](https://github.com/lightfeed/extractor)

生成摘要时出错

---

## 47. False claims in a widely-cited paper

**原文标题**: False claims in a widely-cited paper

**原文链接**: [https://statmodeling.stat.columbia.edu/2026/03/24/false-claims-in-a-published-no-corrections-no-consequences-welcome-to-the-business-school/](https://statmodeling.stat.columbia.edu/2026/03/24/false-claims-in-a-published-no-corrections-no-consequences-welcome-to-the-business-school/)

生成摘要时出错

---

## 48. "Disregard That" Attacks

**原文标题**: "Disregard That" Attacks

**原文链接**: [https://calpaterson.com/disregard.html](https://calpaterson.com/disregard.html)

生成摘要时出错

---

## 49. When it comes to data-ink ratio, optimize rather than maximize

**原文标题**: When it comes to data-ink ratio, optimize rather than maximize

**原文链接**: [https://scienceux.org/articles/data-ink-ideal-vs-minimal](https://scienceux.org/articles/data-ink-ideal-vs-minimal)

生成摘要时出错

---

## 50. Asbestos, talc, and The Lancet's 1977 publication

**原文标题**: Asbestos, talc, and The Lancet's 1977 publication

**原文链接**: [https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(26)00558-1/fulltext](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(26)00558-1/fulltext)

生成摘要时出错

---

## 51. Power consumption of Game Boy flash cartridges (2021)

**原文标题**: Power consumption of Game Boy flash cartridges (2021)

**原文链接**: [https://gekkio.fi/blog/2021/power-consumption-of-game-boy-flash-cartridges/](https://gekkio.fi/blog/2021/power-consumption-of-game-boy-flash-cartridges/)

生成摘要时出错

---

## 52. Maxell MXCP-P100 – wireless cassette player

**原文标题**: Maxell MXCP-P100 – wireless cassette player

**原文链接**: [https://maxell-usa.com/product/cassetteplayer/](https://maxell-usa.com/product/cassetteplayer/)

生成摘要时出错

---

## 53. The Last Contract: William T. Vollmann's Battle to Publish an Epic (2025)

**原文标题**: The Last Contract: William T. Vollmann's Battle to Publish an Epic (2025)

**原文链接**: [https://www.metropolitanreview.org/p/the-last-contract](https://www.metropolitanreview.org/p/the-last-contract)

生成摘要时出错

---

## 54. FreeCAD  v1.1

**原文标题**: FreeCAD  v1.1

**原文链接**: [https://blog.freecad.org/2026/03/25/freecad-version-1-1-released/](https://blog.freecad.org/2026/03/25/freecad-version-1-1-released/)

生成摘要时出错

---

## 55. I tried to prove I'm not AI. My aunt wasn't convinced

**原文标题**: I tried to prove I'm not AI. My aunt wasn't convinced

**原文链接**: [https://www.bbc.com/future/article/20260324-i-tried-to-prove-im-not-an-ai-deepfake](https://www.bbc.com/future/article/20260324-i-tried-to-prove-im-not-an-ai-deepfake)

生成摘要时出错

---

## 56. Supreme Court Sides with Cox in Copyright Fight over Pirated Music

**原文标题**: Supreme Court Sides with Cox in Copyright Fight over Pirated Music

**原文链接**: [https://www.nytimes.com/2026/03/25/us/politics/supreme-court-cox-music-copyright.html](https://www.nytimes.com/2026/03/25/us/politics/supreme-court-cox-music-copyright.html)

生成摘要时出错

---

## 57. Refusal to Give the Govt Passwords to Personal Mobile Criminalized in Hong Kong

**原文标题**: Refusal to Give the Govt Passwords to Personal Mobile Criminalized in Hong Kong

**原文链接**: [https://hk.usconsulate.gov/security-alert-2026032601/](https://hk.usconsulate.gov/security-alert-2026032601/)

生成摘要时出错

---

## 58. Building a coding agent in Swift from scratch

**原文标题**: Building a coding agent in Swift from scratch

**原文链接**: [https://github.com/ivan-magda/swift-claude-code](https://github.com/ivan-magda/swift-claude-code)

生成摘要时出错

---

## 59. 90% of Claude-linked output going to GitHub repos w <2 stars

**原文标题**: 90% of Claude-linked output going to GitHub repos w <2 stars

**原文链接**: [https://www.claudescode.dev/?window=since_launch](https://www.claudescode.dev/?window=since_launch)

生成摘要时出错

---

## 60. Goodbye to Sora

**原文标题**: Goodbye to Sora

**原文链接**: [https://twitter.com/soraofficialapp/status/2036532795984715896](https://twitter.com/soraofficialapp/status/2036532795984715896)

生成摘要时出错

---

## 61. Do architects still need to draw? (2020)

**原文标题**: Do architects still need to draw? (2020)

**原文链接**: [https://www.lifeofanarchitect.com/do-architects-still-need-to-draw/](https://www.lifeofanarchitect.com/do-architects-still-need-to-draw/)

生成摘要时出错

---

## 62. VNDB founder Yorhel has died

**原文标题**: VNDB founder Yorhel has died

**原文链接**: [https://vndb.org/t24787](https://vndb.org/t24787)

生成摘要时出错

---

## 63. On-Device AI Models Might Be the Next Reason to Upgrade Your iPhone

**原文标题**: On-Device AI Models Might Be the Next Reason to Upgrade Your iPhone

**原文链接**: [https://philippdubach.com/posts/on-device-ai-models-will-be-the-new-reason-to-upgrade-your-phone/](https://philippdubach.com/posts/on-device-ai-models-will-be-the-new-reason-to-upgrade-your-phone/)

生成摘要时出错

---

## 64. Thoughts on slowing the fuck down

**原文标题**: Thoughts on slowing the fuck down

**原文链接**: [https://mariozechner.at/posts/2026-03-25-thoughts-on-slowing-the-fuck-down/](https://mariozechner.at/posts/2026-03-25-thoughts-on-slowing-the-fuck-down/)

生成摘要时出错

---

## 65. TurboQuant: Redefining AI efficiency with extreme compression

**原文标题**: TurboQuant: Redefining AI efficiency with extreme compression

**原文链接**: [https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/)

生成摘要时出错

---

## 66. Miscellanea: The War in Iran

**原文标题**: Miscellanea: The War in Iran

**原文链接**: [https://acoup.blog/2026/03/25/miscellanea-the-war-in-iran/](https://acoup.blog/2026/03/25/miscellanea-the-war-in-iran/)

生成摘要时出错

---

## 67. Antimatter has been transported for the first time

**原文标题**: Antimatter has been transported for the first time

**原文链接**: [https://www.nature.com/articles/d41586-026-00950-w](https://www.nature.com/articles/d41586-026-00950-w)

生成摘要时出错

---

## 68. Tell HN: Litellm 1.82.7 and 1.82.8 on PyPI are compromised

**原文标题**: Tell HN: Litellm 1.82.7 and 1.82.8 on PyPI are compromised

**原文链接**: [https://github.com/BerriAI/litellm/issues/24512](https://github.com/BerriAI/litellm/issues/24512)

生成摘要时出错

---

## 69. Updates to GitHub Copilot interaction data usage policy

**原文标题**: Updates to GitHub Copilot interaction data usage policy

**原文链接**: [https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/](https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/)

生成摘要时出错

---

## 70. Algorithm Visualizer

**原文标题**: Algorithm Visualizer

**原文链接**: [https://algorithm-visualizer.org/](https://algorithm-visualizer.org/)

生成摘要时出错

---

## 71. The Military Failures of Fascism

**原文标题**: The Military Failures of Fascism

**原文链接**: [https://acoup.blog/2024/02/23/fireside-friday-february-23-2024-on-the-military-failures-of-fascism/](https://acoup.blog/2024/02/23/fireside-friday-february-23-2024-on-the-military-failures-of-fascism/)

生成摘要时出错

---

## 72. Rendering complex scripts in terminal and OSC 66

**原文标题**: Rendering complex scripts in terminal and OSC 66

**原文链接**: [https://thottingal.in/blog/2026/03/22/complex-scripts-in-terminal/](https://thottingal.in/blog/2026/03/22/complex-scripts-in-terminal/)

生成摘要时出错

---

## 73. Wine 11 rewrites how Linux runs Windows games at kernel with massive speed gains

**原文标题**: Wine 11 rewrites how Linux runs Windows games at kernel with massive speed gains

**原文链接**: [https://www.xda-developers.com/wine-11-rewrites-linux-runs-windows-games-speed-gains/](https://www.xda-developers.com/wine-11-rewrites-linux-runs-windows-games-speed-gains/)

生成摘要时出错

---

## 74. The EU still wants to scan  your private messages and photos

**原文标题**: The EU still wants to scan  your private messages and photos

**原文链接**: [https://fightchatcontrol.eu/?foo=bar](https://fightchatcontrol.eu/?foo=bar)

生成摘要时出错

---

## 75. A Year with the Framework 13

**原文标题**: A Year with the Framework 13

**原文链接**: [https://kevquirk.com/a-year-with-the-framework-13](https://kevquirk.com/a-year-with-the-framework-13)

生成摘要时出错

---

## 76. AI and bots have officially taken over the internet, report finds

**原文标题**: AI and bots have officially taken over the internet, report finds

**原文链接**: [https://www.cnbc.com/2026/03/26/ai-bots-humans-internet.html](https://www.cnbc.com/2026/03/26/ai-bots-humans-internet.html)

生成摘要时出错

---

## 77. Mazda may have found the apex in ICE design with the Skyactiv-Z

**原文标题**: Mazda may have found the apex in ICE design with the Skyactiv-Z

**原文链接**: [https://newatlas.com/automotive/mazda-skyactiv-z/](https://newatlas.com/automotive/mazda-skyactiv-z/)

生成摘要时出错

---

## 78. Sodium-ion EV battery breakthrough delivers 11-min charging and 450 km range

**原文标题**: Sodium-ion EV battery breakthrough delivers 11-min charging and 450 km range

**原文链接**: [https://electrek.co/2026/03/25/sodium-ion-ev-battery-delivers-11-min-charging-450-km-range/](https://electrek.co/2026/03/25/sodium-ion-ev-battery-delivers-11-min-charging-450-km-range/)

生成摘要时出错

---

## 79. Show HN: I took back Video.js after 16 years and we rewrote it to be 88% smaller

**原文标题**: Show HN: I took back Video.js after 16 years and we rewrote it to be 88% smaller

**原文链接**: [https://videojs.org/blog/videojs-v10-beta-hello-world-again](https://videojs.org/blog/videojs-v10-beta-hello-world-again)

生成摘要时出错

---

## 80. VitruvianOS – Desktop Linux Inspired by the BeOS

**原文标题**: VitruvianOS – Desktop Linux Inspired by the BeOS

**原文链接**: [https://v-os.dev](https://v-os.dev)

生成摘要时出错

---

## 81. The Mystery of Rennes-Le-Château, Part 1: The Priest's Treasure

**原文标题**: The Mystery of Rennes-Le-Château, Part 1: The Priest's Treasure

**原文链接**: [https://www.filfre.net/2026/03/the-mystery-of-rennes-le-chateau-part-1-the-priests-treasure/](https://www.filfre.net/2026/03/the-mystery-of-rennes-le-chateau-part-1-the-priests-treasure/)

生成摘要时出错

---

## 82. Apple Business

**原文标题**: Apple Business

**原文链接**: [https://www.apple.com/newsroom/2026/03/introducing-apple-business-a-new-all-in-one-platform-for-businesses-of-all-sizes/](https://www.apple.com/newsroom/2026/03/introducing-apple-business-a-new-all-in-one-platform-for-businesses-of-all-sizes/)

生成摘要时出错

---

## 83. Health NZ staff told to stop using ChatGPT to write clinical notes

**原文标题**: Health NZ staff told to stop using ChatGPT to write clinical notes

**原文链接**: [https://www.rnz.co.nz/news/national/590645/health-nz-staff-told-to-stop-using-chatgpt-to-write-clinical-notes](https://www.rnz.co.nz/news/national/590645/health-nz-staff-told-to-stop-using-chatgpt-to-write-clinical-notes)

生成摘要时出错

---

## 84. Flighty Airports

**原文标题**: Flighty Airports

**原文链接**: [https://flighty.com/airports](https://flighty.com/airports)

生成摘要时出错

---

## 85. Show HN: Mantyx – A platform to orchestrate, manage, and share your agents

**原文标题**: Show HN: Mantyx – A platform to orchestrate, manage, and share your agents

**原文链接**: [https://mantyx.io/](https://mantyx.io/)

生成摘要时出错

---

## 86. Tracy Kidder has died

**原文标题**: Tracy Kidder has died

**原文链接**: [https://www.nytimes.com/2026/03/25/books/tracy-kidder-dead.html](https://www.nytimes.com/2026/03/25/books/tracy-kidder-dead.html)

生成摘要时出错

---

## 87. Ensu – Ente’s Local LLM app

**原文标题**: Ensu – Ente’s Local LLM app

**原文链接**: [https://ente.com/blog/ensu/](https://ente.com/blog/ensu/)

生成摘要时出错

---

## 88. Box of Secrets: Discreetly modding an apartment intercom to work with Apple Home

**原文标题**: Box of Secrets: Discreetly modding an apartment intercom to work with Apple Home

**原文链接**: [https://www.jackhogan.me/blog/box-of-secrets/](https://www.jackhogan.me/blog/box-of-secrets/)

生成摘要时出错

---

## 89. Data centers are transitioning from AC to DC

**原文标题**: Data centers are transitioning from AC to DC

**原文链接**: [https://spectrum.ieee.org/data-center-dc](https://spectrum.ieee.org/data-center-dc)

生成摘要时出错

---

## 90. Woman who never stopped updating her lost dog's chip reunites with him after 11y

**原文标题**: Woman who never stopped updating her lost dog's chip reunites with him after 11y

**原文链接**: [https://www.cbc.ca/radio/asithappens/11-year-dog-reunion-9.7140780](https://www.cbc.ca/radio/asithappens/11-year-dog-reunion-9.7140780)

生成摘要时出错

---

## 91. Terafab semiconductor project could cost $5T – 70% of the US budget

**原文标题**: Terafab semiconductor project could cost $5T – 70% of the US budget

**原文链接**: [https://www.tomshardware.com/tech-industry/semiconductors/elon-musks-terafab-semiconductor-project-could-cost-usd5-trillion-bernstein-claims-herculean-effort-would-cost-more-than-70-percent-of-the-total-yearly-us-government-budget](https://www.tomshardware.com/tech-industry/semiconductors/elon-musks-terafab-semiconductor-project-could-cost-usd5-trillion-bernstein-claims-herculean-effort-would-cost-more-than-70-percent-of-the-total-yearly-us-government-budget)

生成摘要时出错

---

## 92. Meta and YouTube found negligent in landmark social media addiction case

**原文标题**: Meta and YouTube found negligent in landmark social media addiction case

**原文链接**: [https://www.nytimes.com/2026/03/25/technology/social-media-trial-verdict.html](https://www.nytimes.com/2026/03/25/technology/social-media-trial-verdict.html)

生成摘要时出错

---

## 93. Slovenian officials blame Israeli firm Black Cube for trying to manipulate vote

**原文标题**: Slovenian officials blame Israeli firm Black Cube for trying to manipulate vote

**原文链接**: [https://www.wsj.com/world/europe/spies-lies-and-fake-investors-in-disguise-how-plotters-tried-to-flip-a-european-election-1f42b39a](https://www.wsj.com/world/europe/spies-lies-and-fake-investors-in-disguise-how-plotters-tried-to-flip-a-european-election-1f42b39a)

生成摘要时出错

---

## 94. Overcoming the friendship recession

**原文标题**: Overcoming the friendship recession

**原文链接**: [https://joeprevite.com/friendship-recession/](https://joeprevite.com/friendship-recession/)

生成摘要时出错

---

## 95. Hypura – A storage-tier-aware LLM inference scheduler for Apple Silicon

**原文标题**: Hypura – A storage-tier-aware LLM inference scheduler for Apple Silicon

**原文链接**: [https://github.com/t8/hypura](https://github.com/t8/hypura)

生成摘要时出错

---

## 96. Show HN: Yoink – Spotify to lossless with full metadata, self-hostable, ad-free

**原文标题**: Show HN: Yoink – Spotify to lossless with full metadata, self-hostable, ad-free

**原文链接**: [https://yoinkify.com](https://yoinkify.com)

生成摘要时出错

---

## 97. As US Midterms Approach, AI Is Going to Emerge as a Key Issue Concerning Voters

**原文标题**: As US Midterms Approach, AI Is Going to Emerge as a Key Issue Concerning Voters

**原文链接**: [https://www.schneier.com/blog/archives/2026/03/as-the-us-midterms-approach-ai-is-going-to-emerge-as-a-key-issue-concerning-voters.html](https://www.schneier.com/blog/archives/2026/03/as-the-us-midterms-approach-ai-is-going-to-emerge-as-a-key-issue-concerning-voters.html)

生成摘要时出错

---

## 98. Microsoft's "fix" for Windows 11

**原文标题**: Microsoft's "fix" for Windows 11

**原文链接**: [https://www.sambent.com/microsofts-plan-to-fix-windows-11-is-gaslighting/](https://www.sambent.com/microsofts-plan-to-fix-windows-11-is-gaslighting/)

生成摘要时出错

---

## 99. Debunking Zswap and Zram Myths

**原文标题**: Debunking Zswap and Zram Myths

**原文链接**: [https://chrisdown.name/2026/03/24/zswap-vs-zram-when-to-use-what.html](https://chrisdown.name/2026/03/24/zswap-vs-zram-when-to-use-what.html)

生成摘要时出错

---

## 100. Log File Viewer for the Terminal

**原文标题**: Log File Viewer for the Terminal

**原文链接**: [https://lnav.org/](https://lnav.org/)

生成摘要时出错

---

