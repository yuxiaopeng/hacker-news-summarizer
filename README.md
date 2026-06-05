# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-06-05.md)

*最后自动更新时间: 2026-06-05 19:27:09*
## 1. 因漏气修复避险后，宇航员受命返回国际空间站。

**原文标题**: Astronauts told to return to ISS after sheltering over air leak repairs

**原文链接**: [https://www.bbc.com/news/live/c4g44ew3g1kt](https://www.bbc.com/news/live/c4g44ew3g1kt)

国际空间站（ISS）上的五名宇航员在俄罗斯舱段维修期间，于对接的飞船内采取避险措施后，现已返回空间站主舱。在两名俄罗斯航天员修复“星辰”号服务舱转移通道的漏气点时，机组人员接到指令，采取了“提升安全防范级别”的姿态。

据美国国家航空航天局（NASA）称，该特定舱段一段时间以来一直饱受裂缝和漏气问题的困扰。俄罗斯国际文传电讯社报道，俄罗斯国家航天集团（Roscosmos）在最近的任务中发现了两处漏气点，其中一处已成功修复。

NASA发言人贝瑟尼·史蒂文斯表示，由于工程师正在评估测量结果和数据，结构修复工作已暂时暂停。尽管漏气问题反复出现，但NASA和俄罗斯国家航天集团均确认，机组人员及空间站机载系统在整个过程中始终保持安全。

---

## 2. pg_durable：微软开源数据库内持久执行

**原文标题**: pg_durable: Microsoft open sources in-database durable execution

**原文链接**: [https://github.com/microsoft/pg_durable](https://github.com/microsoft/pg_durable)

微软开源了 **pg_durable**，这是一个专为**持久化执行（durable execution）**设计的 PostgreSQL 扩展。它允许工程师直接在数据库内使用 SQL 构建长耗时、容错的工作流。通过为工作流图的每个步骤设置检查点，pg_durable 确保进程在崩溃、重启或失败后能从上一个成功状态自动恢复，从而消除了手动重建状态的必要。

**核心特性与优势：**
*   **降低复杂性：** 它取代了外部编排器（如 Temporal 或 Airflow）以及碎片化的“cron + 队列 + 工作节点”配置，使计算更贴近数据。
*   **原生 SQL DSL：** 工作流使用可组合的 SQL 语法定义（例如，使用 `~>` 表示顺序执行，使用 `|=>` 表示管道传输），并通过标准 SQL 命令进行管理。
*   **运维可见性：** 进度和状态存储在标准 Postgres 表中，可以使用熟悉的工具对工作流进行审计。
*   **应用场景：** 非常适合向量嵌入流水线、批量数据摄取、定期维护以及并行的“扇出”聚合。

**技术架构：**
pg_durable 基于 Rust 和 `pgrx` 框架构建，作为 PostgreSQL 进程内的后台工作线程运行。它利用 `duroxide` 编排库进行确定性回放和状态管理。该扩展支持 PostgreSQL 17 和 18，并包含行级安全性（RLS），以确保用户只能管理自己的工作流实例。

**局限性：**
该工具专门围绕 SQL 设计。它不适用于亚毫秒级的同步请求，或需要复杂非 HTTP SDK 的逻辑，除非该逻辑被封装在 SQL 函数或外部 HTTP 端点中。

pg_durable 目前处于**预览阶段**，旨在为已将 PostgreSQL 作为主要状态存储的团队简化后端架构。

---

## 3. Gemma 4 QAT 模型：针对移动端与笔记本电脑优化压缩效率

**原文标题**: Gemma 4 QAT models: Optimizing compression for mobile and laptop efficiency

**原文链接**: [https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/](https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/)

Google DeepMind 宣布发布 **Gemma 4 QAT 模型**，这是利用量化感知训练 (QAT) 优化的全新系列检查点。这些模型旨在通过在不牺牲质量的前提下显著降低显存需求，从而最大限度地提高手机、笔记本电脑和消费级 GPU 等边缘设备的性能和效率。

与通常会导致性能下降的标准训练后量化 (PTQ) 不同，QAT 将压缩过程集成到训练阶段，使模型在缩小体积的同时能够保持更高的准确度。此次发布的主要亮点包括：

*   **移动端优化：** 一种新型的专业移动量化方案将 **Gemma 4 E2B** 模型的内存占用降低至仅 **1GB**。这是通过静态激活、通道级量化以及针对 Token 生成层的定向 2-bit 量化实现的。
*   **性能格式：** 此次发布包含了主流的 **Q4_0** 格式检查点，确保在各种硬件上实现高速推理。
*   **模块化：** 为了进一步节省显存 (VRAM)，开发者可以部署特定模态的版本（例如纯文本版），从而移除不必要的音频或视觉编码器。
*   **生态集成：** 模型权重已在 Hugging Face 上以 **GGUF** 和压缩张量格式提供。它们兼容多种开发者工具，包括 llama.cpp、Ollama、LM Studio、vLLM 以及 Google 的 LiteRT-LM。

通过弥合高端 AI 能力与本地消费级硬件之间的差距，这些 QAT 模型让开发者能够以极低的内存开销，在日常设备上本地运行复杂的 Gemma 4 架构。

---

## 4. Cloudflare CEO 正就机器人流量激增一事对你撒谎

**原文标题**: Cloudflare CEO Is Lying to You About the Bot Traffic Jump

**原文链接**: [https://www.flyingpenguin.com/cloudflare-ceo-is-lying-to-you-about-the-bot-traffic-jump/](https://www.flyingpenguin.com/cloudflare-ceo-is-lying-to-you-about-the-bot-traffic-jump/)

这篇文章指出，Cloudflare 首席执行官 Matthew Prince 歪曲了数据，虚假声称机器人流量已首次超过人类流量。作者断言，Prince 的说法基于一种“伎俩”，即他采用了“仅限 HTML”的统计指标，却忽略了 Cloudflare 自身的“全流量”数据面板，而后者显示人类仍占据互联网活动约三分之二的份额。

作者强调了 Prince 叙述中的几处具体矛盾：

*   **AI 增长的错误分类：** 尽管 Prince 将流量激增归咎于“代理型”AI（代表用户操作的 AI），但作者指出，在 Cloudflare 的数据集中，这一类别实际上是占比最小的。
*   **爬虫的作用：** AI 流量的真实增长源于大规模训练爬虫（如 GPTBot 和 ClaudeBot），它们被用于构建模型，而非响应个人用户请求。
*   **数据虚增：** 作者声称，通过重复计算 Googlebot 以及错误呈现搜索引擎爬虫（这仍是最大的机器人类别），AI 流量数据被人为夸大了。

最终，文章将这些言论定性为一场欺骗性的营销辞令。作者认为，Prince 有意将“代理型”AI 与大规模抓取混为一谈，以此构建一套叙事来为其 Cloudflare 的“付费爬取”产品辩护，实际上是歪曲了自家公司的数据以驱动收入增长。

---

## 5. 约定式提交引导人们关注错误的事情

**原文标题**: Conventional Commits encourages focus on the wrong things

**原文链接**: [https://sumnerevans.com/posts/software-engineering/stop-using-conventional-commits/](https://sumnerevans.com/posts/software-engineering/stop-using-conventional-commits/)

在《常规提交（Conventional Commits）助长了错误的关注点》一文中，作者指出“常规提交”标准是一种有缺陷的实践，它将元数据置于有意义的上下文之上。

作者的核心批评在于，该标准优先考虑“类型”（如 `feat`、`fix`）而非“作用域”（代码更改的具体区域）。对于贡献者、调试者和事故响应者来说，作用域是查阅历史或定位 Bug 来源时最关键的信息。通过将作用域设为可选并将类型置于首位，“常规提交”完全搞错了优先级。

此外，作者认为提交类型通常是多余的——因为清晰的描述往往已隐含了类型——且具有局限性，因为许多提交无法简单地归入单一类别。文章还拆解了该标准所谓的几大优势：

*   **自动化变更日志：** 作者认为面向用户的变更日志与面向开发者的提交日志受众不同，不应从同一来源生成。
*   **自动化语义化版本（SemVer）：** 这被认为是不可靠的，因为它无法兼顾回滚、意外破坏或追溯修复等复杂情况。
*   **工具化/安全性：** 相比于对更改文件使用 `git diff`，依赖提交类型来触发 CI/CD 流程被视为一种安全风险。

作为替代方案，作者提倡“作用域提交”（Scoped Commits），这是 Linux、Git 和 Go 等成功项目采用的格式。该方法使用简单的 `作用域: 描述` 格式（如 `kernel: fix memory leak`）来提供即时且相关的上下文。为了推动这种“回归理性”，作者推出了 `scopedcommits.com`，敦促开发者优先考虑与项目相关的作用域，而非僵化的、便于自动化的类型。

---

## 6. Mouseless – 键盘驱动的 macOS/Linux/Windows 操控

**原文标题**: Mouseless – keyboard-driven control of macOS/Linux/Windows

**原文链接**: [https://mouseless.click](https://mouseless.click)

**Mouseless** 是一款跨平台软件工具，旨在仅通过键盘实现对计算机鼠标功能的高速控制。该应用兼容 **macOS、Linux 和 Windows**，旨在让用户在无需将手移开键盘的情况下导航操作系统，从而提升生产力和效率。

其核心宗旨是提供“闪电般快速”的光标控制，这主要通过键盘快捷键和特定的导航模式来实现。根据文中所述，该工具面向偏好在多种桌面环境中使用键盘驱动型工作流的高级用户。

---

## 7. I tested every IP KVM in my Homelab

**原文标题**: I tested every IP KVM in my Homelab

**原文链接**: [https://www.jeffgeerling.com/blog/2026/i-tested-every-ip-kvm/](https://www.jeffgeerling.com/blog/2026/i-tested-every-ip-kvm/)

The article explores the evolution of IP KVM (Keyboard, Video, Mouse) devices since the PiKVM’s 2017 debut, highlighting their utility for remote hardware management without requiring local software. Unlike VNC or SSH, IP KVMs provide BIOS-level access and function even when the target computer is frozen or powered off.

The author categorizes the current market into three main groups:

1.  **Premium/Open-Source Pioneers:** **PiKVM** and **TinyPilot** remain the gold standards. PiKVM offers a fully open-source stack and high-end features like 5G backup but carries a high price tag ($275–$400). TinyPilot targets business users with simplified setup, centralized management, and professional support.
2.  **Budget-Friendly Innovations:** Newer entries like **GL-iNet’s Comet** ($99) and **JetKVM** ($103) offer features like 4K support and polished UIs at a much lower price point. **Sipeed’s NanoKVM** ($70) represents the extreme budget end using RISC-V hardware, though its low cost and inconspicuous nature have reportedly made it a tool for corporate espionage, leading to an FBI visit for the author.
3.  **Specialized Form Factors:** Many brands now offer PCIe card versions for internal installation. Additionally, "direct-connect" options like **Openterface KVM-GO** and **Pi-Cast** allow users to control machines via a direct USB/VGA connection rather than over a standard LAN.

The author concludes with a strong security warning: because these devices provide deep access to hardware, they must be treated as potential security holes. Users should prioritize firewalls, frequent updates, and vendor trust when integrating an IP KVM into their network. For hobbyists, the market now offers a wide range of choices between premium open-source hardware and affordable, specialized clones.

---

## 8. New method turns ocean water into drinking water, without waste

**原文标题**: New method turns ocean water into drinking water, without waste

**原文链接**: [https://www.rochester.edu/newscenter/what-is-desalination-definition-ocean-water-704732/](https://www.rochester.edu/newscenter/what-is-desalination-definition-ocean-water-704732/)

生成摘要时出错

---

## 9. My Agent Skill for Test-Driven Development

**原文标题**: My Agent Skill for Test-Driven Development

**原文链接**: [https://www.saturnci.com/my-agent-skill-for-test-driven-development.html](https://www.saturnci.com/my-agent-skill-for-test-driven-development.html)

生成摘要时出错

---

## 10. Gov.uk has replaced Stripe with Dutch provider Adyen

**原文标题**: Gov.uk has replaced Stripe with Dutch provider Adyen

**原文链接**: [https://www.theregister.com/public-sector/2026/06/04/govuk-goes-dutch-on-payments-as-it-dumps-stripe/5250763](https://www.theregister.com/public-sector/2026/06/04/govuk-goes-dutch-on-payments-as-it-dumps-stripe/5250763)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 2 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 3 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 4 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 5 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 6 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 7 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 8 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 9 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 10 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 11 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 12 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 13 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 14 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 15 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 16 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 17 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 18 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 19 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 20 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 21 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 22 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 23 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 24 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 25 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 26 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 27 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 28 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 29 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 30 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 31 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 32 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 33 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 34 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 35 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 36 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 37 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 38 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 39 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 40 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 41 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 42 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 43 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 44 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 45 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 46 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 47 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 48 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 49 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 50 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 51 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 52 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 53 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 54 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 55 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 56 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 57 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 58 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 59 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 60 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 61 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 62 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 63 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 64 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 65 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 66 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 67 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 68 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 69 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 70 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 71 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 72 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 73 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 74 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 75 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 76 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 77 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 78 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 79 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 80 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 81 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 82 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 83 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 84 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 85 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 86 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 87 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 88 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 89 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 90 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 91 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 92 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 93 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 94 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 95 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 96 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 97 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 98 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 99 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 100 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 101 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 102 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 103 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 104 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 105 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 106 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 107 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 108 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 109 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 110 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 111 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 112 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 113 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 114 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 115 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 116 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 117 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 118 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 119 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 120 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 121 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 122 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 123 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 124 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 125 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 126 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 127 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 128 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 129 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 130 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 131 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 132 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 133 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 134 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 135 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 136 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 137 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 138 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 139 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 140 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 141 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 142 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 143 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 144 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 145 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 146 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 147 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 148 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 149 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 150 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 151 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 152 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 153 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 154 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 155 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 156 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 157 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 158 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 159 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 160 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 161 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 162 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 163 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 164 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 165 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 166 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 167 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 168 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 169 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 170 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 171 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 172 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 173 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 174 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 175 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 176 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 177 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 178 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 179 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 180 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 181 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 182 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 183 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 184 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 185 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 186 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 187 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 188 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 189 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 190 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 191 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 192 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 193 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 194 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 195 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 196 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 197 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 198 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 199 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 200 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 201 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 202 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 203 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 204 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 205 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 206 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 207 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 208 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 209 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 210 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 211 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 212 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 213 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 214 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 215 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 216 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 217 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 218 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 219 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 220 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 221 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 222 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 223 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 224 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 225 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 226 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 227 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 228 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 229 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 230 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 231 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 232 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 233 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 234 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 235 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 236 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 237 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 238 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 239 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 240 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 241 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 242 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 243 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 244 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 245 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 246 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 247 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 248 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 249 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 250 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 251 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 252 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 253 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 254 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 255 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 256 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 257 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 258 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 259 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 260 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 261 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 262 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 263 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 264 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 265 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 266 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 267 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 268 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 269 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 270 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 271 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 272 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 273 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 274 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 275 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 276 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 277 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 278 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 279 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 280 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 281 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 282 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 283 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 284 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 285 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 286 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 287 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 288 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 289 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 290 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 291 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 292 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 293 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 294 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 295 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 296 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 297 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 298 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 299 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 300 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 301 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 302 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 303 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 304 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 305 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 306 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 307 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 308 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 309 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 310 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 311 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 312 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 313 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 314 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 315 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 316 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 317 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 318 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 319 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 320 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 321 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 322 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 323 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 324 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 325 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 326 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 327 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 328 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 329 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 330 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 331 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 332 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 333 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 334 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 335 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 336 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 337 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 338 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 339 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 340 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 341 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 342 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 343 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 344 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 345 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 346 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 347 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 348 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 349 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 350 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 351 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 352 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 353 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 354 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 355 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 356 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 357 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 358 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 359 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 360 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 361 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 362 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 363 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 364 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 365 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 366 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 367 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 368 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 369 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 370 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 371 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 372 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 373 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 374 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 375 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 376 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 377 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 378 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 379 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 380 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 381 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 382 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 383 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 384 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 385 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 386 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 387 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 388 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 389 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 390 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 391 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 392 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 393 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 394 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 395 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 396 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 397 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 398 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 399 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 400 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 401 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 402 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 403 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 404 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 405 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 406 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 407 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 408 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 409 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 410 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 411 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 412 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 413 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 414 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 415 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 416 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 417 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 418 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 419 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 420 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 421 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 422 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 423 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 424 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 425 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 426 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 427 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 428 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 429 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 430 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 431 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 432 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 433 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 434 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 435 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 436 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 437 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 438 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 439 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 440 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 441 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 442 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
