# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-03-26.md)

*最后自动更新时间: 2026-03-26 18:25:26*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 2 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 3 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 4 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 5 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 6 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 7 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 8 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 9 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 10 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 11 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 12 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 13 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 14 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 15 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 16 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 17 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 18 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 19 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 20 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 21 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 22 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 23 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 24 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 25 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 26 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 27 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 28 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 29 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 30 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 31 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 32 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 33 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 34 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 35 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 36 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 37 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 38 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 39 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 40 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 41 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 42 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 43 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 44 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 45 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 46 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 47 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 48 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 49 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 50 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 51 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 52 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 53 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 54 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 55 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 56 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 57 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 58 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 59 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 60 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 61 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 62 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 63 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 64 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 65 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 66 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 67 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 68 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 69 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 70 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 71 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 72 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 73 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 74 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 75 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 76 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 77 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 78 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 79 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 80 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 81 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 82 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 83 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 84 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 85 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 86 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 87 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 88 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 89 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 90 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 91 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 92 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 93 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 94 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 95 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 96 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 97 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 98 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 99 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 100 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 101 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 102 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 103 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 104 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 105 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 106 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 107 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 108 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 109 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 110 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 111 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 112 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 113 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 114 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 115 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 116 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 117 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 118 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 119 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 120 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 121 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 122 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 123 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 124 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 125 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 126 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 127 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 128 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 129 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 130 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 131 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 132 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 133 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 134 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 135 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 136 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 137 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 138 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 139 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 140 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 141 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 142 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 143 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 144 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 145 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 146 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 147 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 148 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 149 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 150 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 151 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 152 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 153 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 154 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 155 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 156 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 157 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 158 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 159 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 160 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 161 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 162 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 163 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 164 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 165 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 166 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 167 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 168 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 169 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 170 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 171 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 172 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 173 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 174 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 175 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 176 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 177 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 178 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 179 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 180 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 181 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 182 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 183 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 184 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 185 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 186 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 187 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 188 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 189 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 190 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 191 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 192 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 193 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 194 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 195 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 196 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 197 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 198 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 199 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 200 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 201 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 202 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 203 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 204 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 205 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 206 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 207 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 208 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 209 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 210 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 211 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 212 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 213 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 214 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 215 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 216 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 217 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 218 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 219 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 220 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 221 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 222 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 223 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 224 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 225 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 226 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 227 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 228 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 229 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 230 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 231 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 232 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 233 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 234 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 235 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 236 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 237 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 238 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 239 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 240 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 241 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 242 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 243 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 244 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 245 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 246 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 247 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 248 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 249 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 250 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 251 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 252 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 253 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 254 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 255 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 256 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 257 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 258 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 259 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 260 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 261 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 262 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 263 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 264 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 265 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 266 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 267 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 268 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 269 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 270 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 271 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 272 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 273 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 274 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 275 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 276 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 277 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 278 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 279 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 280 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 281 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 282 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 283 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 284 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 285 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 286 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 287 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 288 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 289 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 290 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 291 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 292 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 293 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 294 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 295 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 296 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 297 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 298 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 299 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 300 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 301 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 302 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 303 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 304 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 305 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 306 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 307 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 308 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 309 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 310 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 311 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 312 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 313 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 314 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 315 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 316 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 317 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 318 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 319 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 320 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 321 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 322 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 323 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 324 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 325 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 326 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 327 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 328 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 329 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 330 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 331 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 332 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 333 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 334 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 335 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 336 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 337 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 338 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 339 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 340 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 341 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 342 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 343 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 344 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 345 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 346 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 347 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 348 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 349 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 350 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 351 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 352 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 353 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 354 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 355 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 356 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 357 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 358 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 359 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 360 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 361 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 362 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 363 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 364 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 365 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 366 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 367 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 368 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 369 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 370 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 371 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
