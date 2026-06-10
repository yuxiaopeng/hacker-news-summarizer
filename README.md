# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-06-10.md)

*最后自动更新时间: 2026-06-10 20:09:16*
## 1. Claude Desktop 启动了一个无法停止的虚拟机

**原文标题**: Claude Desktop spins up a VM without no way of stopping it

**原文链接**: [https://github.com/anthropics/claude-code/issues/29045](https://github.com/anthropics/claude-code/issues/29045)

一份 GitHub 错误报告（Issue #29045）指出 Claude Windows 桌面版应用存在严重的性能问题。据报告，该应用在每次启动时都会生成一个 Hyper-V 虚拟机（在任务管理器中显示为 `Vmmem`），并占用约 1.8 GB 的内存，即便用户仅需要基础聊天功能也是如此。

**核心技术细节：**
*   **影响：** 在 16 GB 内存的系统上，这占用了超过 11% 的总内存，导致系统运行缓慢。
*   **根本原因：** 该应用在启动时会触发 Hyper-V 主机计算服务。调查显示，应用未能清理“Cowork”或代理模式的会话文件，一名用户在其 AppData 文件夹中发现了超过 2600 个残留文件。即使清理了这些文件，虚拟机仍会自动启动。
*   **日志：** 系统日志显示，在初始化过程中反复出现与无效 JSON 文档相关的 Hyper-V 错误。
*   **环境：** 该问题主要影响启用了“虚拟机平台”功能的 Windows 11 用户，即使他们并未安装 WSL、Docker 或 Hyper-V 管理工具。

**当前临时解决方案：**
目前，用户必须完全禁用“虚拟机平台”功能（这将导致 Claude 的代理化“Cowork”功能失效），或者在应用打开后通过 PowerShell 手动终止 `vmwp.exe` 和 `vmcompute` 进程。即使杀掉虚拟机进程，聊天功能仍可正常运行。

**请求的修复方案：**
该报告敦促 Anthropic 修改桌面客户端以实现：
1.  仅在激活代理/Cowork 功能时，**按需**初始化虚拟机基础架构。
2.  实现残留会话数据的自动清理。
3.  确保应用默认进入轻量级的纯聊天模式。

---

## 2. 喷气推进实验室如何让服役13年的“好奇号”火星车持续开展科学探测

**原文标题**: How JPL keeps the 13-year-old Curiosity rover doing science

**原文链接**: [https://spectrum.ieee.org/curiosity-rover-jpl-mars-science](https://spectrum.ieee.org/curiosity-rover-jpl-mars-science)

这篇文章探讨了美国国家航空航天局（NASA）喷气推进实验室（JPL）如何成功延长“好奇号”火星车的任务寿命。该探测器已在火星上运行超过13年，远超其最初设定的两年期主要任务。由于其距离地球约2亿公里，无法进行实地维修，工程师们被迫开发创意性的远程方案以维持其正常运行。

总结中强调了JPL为应对探测器硬件老化和恶劣火星环境而采用的几项“巧妙策略”：

*   **软件创新：** 工程师频繁上传软件补丁，以优化性能、完善功耗并绕过硬件故障。
*   **车轮维护：** 针对火星尖锐岩石造成的严重磨损和车轮破洞，JPL开发了牵引力控制软件，通过调节轮速来减轻压力并防止进一步损坏。
*   **能源管理：** 随着好奇号的放射性同位素热电发生器（MMRTG）动力源自然衰减，团队实施了能源管理策略，确保火星车仍能执行高耗能的钻探和科学分析任务。
*   **远程故障排除：** 工程师利用JPL内部的好奇号“地面孪生机”来测试每一次操作指令和软件更新，确认无误后再发送至火星，从而最大限度地降低导致任务失败的风险。

最终，好奇号的长寿证明了JPL前瞻性工程设计的成功。通过将火星车视为一个不断进化的平台而非静态机器，NASA已将这个拥有十年历史的机器人转变为一个长期的火星实验室，持续为研究这颗红色星球的历史及其潜在宜居性提供宝贵数据。

---

## 3. 为什么SpaceX 2040年4.3万亿美元的营收预测极不可能

**原文标题**: Why SpaceX 2040 Revenue FCST $4.3T in highly unlikely

**原文链接**: [https://www.matteast.io/spacex-escape-velocity.html](https://www.matteast.io/spacex-escape-velocity.html)

本文对 SpaceX 1.77 万亿美元的 IPO 估值及其 2040 年 3.4 万亿美元的营收预测提出了质疑，认为该预测在统计和经济层面均不具备可行性。

作者的核心论点围绕“增长前沿”（Growth Frontier）展开。尽管特斯拉等公司曾实现过更高的年增长率，但那是基于极小的初始基数。SpaceX 必须在 187 亿美元的基数上保持 41.5% 的年复合增长率（CAGR）——这一壮举将使其超出任何历史先例 44%，成为极其罕见的特例。要达到 3.4 万亿美元的目标，SpaceX 的规模需达到沃尔玛的五倍，并贡献美国 GDP 总额的 6%，同时还需维持 79% 这一史无前例的息税折旧摊销前利润率（EBITDA margin），甚至超过沙特阿美。

文章指出，此次 IPO 的架构并非为了长期价值，而是为了促成一次“强制竞价”（forced bid）的流动性事件：
*   **极低流通盘：** 仅公司 4% 的股份向公众出售。
*   **指数纳入：** 纳斯达克针对超大市值公司的“快速通道”规则，将迫使被动型基金（如追踪 QQQ 的基金）不计价格买入预计 600 亿美元的股票。
*   **退出路径：** 这种人为创造的需求形成了价格支撑，使得内部人士在 90-180 天的锁定期满后即可向市场套现。

作者最终得出结论，2040 年的预测只是一个为了合理化天价估值而编造的“自圆其说的故事”。此次 IPO 的真正目的并非实现 20 年后的营收目标，而是利用指数再平衡机制，促成财富从被动型公共基金向私人内部人士的大规模转移。

---

## 4. 关于人工智能指数级发展的政策

**原文标题**: Policy on the AI Exponential

**原文链接**: [https://darioamodei.com/post/policy-on-the-ai-exponential](https://darioamodei.com/post/policy-on-the-ai-exponential)

在《人工智能指数级增长政策》（Policy on the AI Exponential）中，Anthropic 认为，在缩放法则（scaling laws）的推动下，人工智能的飞速发展正在超越传统政策制定的缓慢步伐。鉴于“强 AI”（定义为“数据中心里的天才之国”）可能在短短几年内实现，文章断言，仅靠透明度已不足以应对当前的局势。

作者强调了风险格局的转变，并以“Claude Mythos Preview”等前沿模型为例，证明 AI 现已对网络安全、国家安全和关键基础设施构成了实质性威胁。为应对这些新兴风险，文章提出了一个效仿美国联邦航空管理局（FAA）的监管框架。主要建议包括：

*   **强制性测试：** 超过特定算力阈值的模型必须接受第三方审计，以评估网络安全、生物武器、失控风险以及自主研发等相关的风险。
*   **执法权：** 政府应有权阻止未能达到安全标准的模型进行部署。
*   **安全标准：** AI 公司必须对模型权重实施严密的保护，并及时报告安全事件。

在宏观经济方面，文章警告称可能会出现“高速增长与高度不平等”并存的局面。虽然 AI 将极大提升生产力，但由于它在大多数领域取代了人类认知，可能会导致持久的劳动力流失。为此，Anthropic 提倡采取积极的经济政策，包括：
*   加强政府对 AI 就业影响的追踪。
*   实施促进就业的激励措施，如工资保险和保留员工税收抵免。
*   如果人类劳动在经济中的核心地位下降，需对税收政策进行长期重新评估。

最终，该文章旨在呼吁政策制定者推动机构现代化并制定具有约束力的安全标准，以确保向 AI 驱动世界的转型能够得到负责任的管理。

---

## 5. PgDog 获融资，即将来到你身边的数据库

**原文标题**: PgDog is funded and coming to a database near you

**原文链接**: [https://pgdog.dev/blog/our-funding-announcement](https://pgdog.dev/blog/our-funding-announcement)

**PgDog** 是一家致力于解决 PostgreSQL 核心局限性——水平扩展能力的初创公司。该公司由三位资深基础设施工程师组成的团队创立，其成员包括曾在 2020 年 Instacart 业务增长 5 倍期间负责扩展其数据库系统的资深专家。公司的目标是让 Postgres 成为开发者唯一需要的数据库。

PgDog 作为一个开源代理运行在标准 Postgres 实例前端，使其能够处理海量工作负载，例如 100 TB 以上的大表和每秒数百万次（QPS）的查询。该工具设计灵活，可通过 Docker 部署在本地私有设施、云端或个人机器上。与许多现代替代方案不同，它避免了隐藏的无服务器（serverless）成本，并通过多线程代码充分利用 CPU 资源。

该项目已经取得了显著的市场牵引力：
*   **性能：** 目前在各类生产环境部署中提供超过 200 万 QPS 的服务。
*   **采用率：** 在 GitHub 上的 Docker 拉取量已超过 140 万次。
*   **数据管理：** 使用该平台进行分片管理的数据量已至少达到 20 TB。

该公司近期从 Y Combinator、Basis Set、Pioneer Fund 等机构获得了 **550 万美元** 的融资，确保了为期数年的稳健运营空间。虽然核心产品保持开源并每周发布更新，但公司也同步推出了专门针对 AWS 环境的**企业版**，提供带有 SLA 保障的技术支持。

PgDog 的最终使命是应用第一性原理工程，确保 Postgres 在任何规模下都能“开箱即用”，从而消除开发者因扩展瓶颈而不得不迁移到 MongoDB 或 DynamoDB 等专用数据库的需求。

---

## 6. Anthropic's Model Naming, Extrapolated

**原文标题**: Anthropic's Model Naming, Extrapolated

**原文链接**: [https://samwilkinson.io/posts/2026-06-09-anthropics-model-naming-extrapolated](https://samwilkinson.io/posts/2026-06-09-anthropics-model-naming-extrapolated)

In the article "Anthropic's Model Naming, Extrapolated," Sam Wilkinson explores the creative logic behind Anthropic’s naming convention for the Claude 3 family—Haiku, Sonnet, and Opus—and humorously projects where this pattern might lead as AI models continue to scale.

The author notes that Anthropic has bypassed traditional numerical versioning in favor of evocative, literary terms that signify increasing complexity: **Haiku** (small/fast), **Sonnet** (medium/balanced), and **Opus** (large/powerful). Wilkinson argues that this creates a "prestige" branding ladder that will eventually require more extreme titles as the delta between model sizes grows.

The post extrapolates this taxonomy in both directions:
*   **Smaller Models:** For ultra-efficient or "tiny" models, Wilkinson suggests names like **Limerick**, **Couplet**, **Aphorism**, and eventually just **Grunt** for models with minimal functionality.
*   **Larger Models:** As capabilities expand, the names become increasingly grand and academic. Potential future names include **Epic**, **Tragedy**, **Canon**, **Scripture**, and **Encyclopedia**. 

The satire reaches its peak with the suggestion that eventually, Anthropic will run out of earthly literary forms and move toward the metaphysical, proposing names like **The Akashic Records** or **Omniscience**. 

Ultimately, the article serves as a lighthearted critique of the branding arms race in the AI industry. It highlights how companies use high-brow terminology to signal "intelligence" and "depth," suggesting that the trajectory of these names will inevitably lead to the absurd as models become either hyper-specialized or god-like in scale.

---

## 7. L'Affaire Siloxane

**原文标题**: L'Affaire Siloxane

**原文链接**: [https://mceglowski.substack.com/p/laffaire-siloxane](https://mceglowski.substack.com/p/laffaire-siloxane)

生成摘要时出错

---

## 8. Meta steals a tactic from Tesla and builds data centers in tents

**原文标题**: Meta steals a tactic from Tesla and builds data centers in tents

**原文链接**: [https://techcrunch.com/2026/06/04/meta-steals-a-tactic-from-tesla-and-builds-data-centers-in-tents/](https://techcrunch.com/2026/06/04/meta-steals-a-tactic-from-tesla-and-builds-data-centers-in-tents/)

生成摘要时出错

---

## 9. GitHub Authentication issues related to API requests

**原文标题**: GitHub Authentication issues related to API requests

**原文链接**: [https://www.githubstatus.com/incidents/fcj3088jg1wx](https://www.githubstatus.com/incidents/fcj3088jg1wx)

生成摘要时出错

---

## 10. Building an HTML-first site doubled our users overnight

**原文标题**: Building an HTML-first site doubled our users overnight

**原文链接**: [https://mohkohn.co.uk/writing/html-first/](https://mohkohn.co.uk/writing/html-first/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 2 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 3 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 4 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 5 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 6 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 7 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 8 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 9 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 10 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 11 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 12 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 13 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 14 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 15 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 16 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 17 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 18 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 19 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 20 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 21 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 22 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 23 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 24 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 25 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 26 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 27 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 28 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 29 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 30 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 31 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 32 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 33 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 34 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 35 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 36 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 37 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 38 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 39 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 40 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 41 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 42 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 43 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 44 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 45 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 46 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 47 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 48 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 49 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 50 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 51 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 52 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 53 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 54 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 55 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 56 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 57 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 58 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 59 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 60 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 61 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 62 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 63 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 64 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 65 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 66 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 67 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 68 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 69 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 70 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 71 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 72 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 73 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 74 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 75 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 76 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 77 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 78 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 79 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 80 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 81 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 82 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 83 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 84 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 85 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 86 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 87 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 88 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 89 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 90 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 91 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 92 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 93 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 94 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 95 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 96 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 97 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 98 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 99 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 100 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 101 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 102 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 103 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 104 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 105 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 106 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 107 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 108 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 109 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 110 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 111 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 112 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 113 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 114 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 115 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 116 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 117 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 118 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 119 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 120 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 121 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 122 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 123 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 124 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 125 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 126 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 127 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 128 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 129 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 130 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 131 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 132 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 133 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 134 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 135 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 136 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 137 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 138 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 139 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 140 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 141 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 142 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 143 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 144 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 145 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 146 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 147 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 148 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 149 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 150 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 151 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 152 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 153 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 154 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 155 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 156 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 157 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 158 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 159 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 160 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 161 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 162 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 163 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 164 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 165 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 166 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 167 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 168 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 169 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 170 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 171 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 172 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 173 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 174 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 175 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 176 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 177 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 178 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 179 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 180 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 181 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 182 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 183 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 184 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 185 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 186 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 187 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 188 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 189 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 190 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 191 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 192 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 193 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 194 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 195 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 196 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 197 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 198 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 199 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 200 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 201 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 202 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 203 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 204 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 205 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 206 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 207 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 208 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 209 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 210 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 211 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 212 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 213 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 214 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 215 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 216 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 217 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 218 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 219 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 220 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 221 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 222 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 223 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 224 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 225 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 226 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 227 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 228 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 229 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 230 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 231 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 232 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 233 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 234 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 235 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 236 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 237 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 238 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 239 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 240 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 241 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 242 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 243 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 244 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 245 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 246 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 247 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 248 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 249 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 250 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 251 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 252 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 253 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 254 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 255 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 256 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 257 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 258 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 259 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 260 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 261 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 262 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 263 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 264 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 265 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 266 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 267 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 268 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 269 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 270 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 271 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 272 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 273 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 274 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 275 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 276 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 277 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 278 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 279 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 280 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 281 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 282 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 283 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 284 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 285 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 286 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 287 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 288 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 289 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 290 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 291 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 292 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 293 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 294 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 295 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 296 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 297 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 298 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 299 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 300 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 301 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 302 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 303 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 304 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 305 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 306 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 307 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 308 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 309 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 310 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 311 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 312 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 313 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 314 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 315 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 316 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 317 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 318 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 319 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 320 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 321 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 322 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 323 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 324 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 325 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 326 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 327 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 328 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 329 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 330 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 331 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 332 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 333 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 334 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 335 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 336 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 337 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 338 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 339 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 340 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 341 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 342 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 343 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 344 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 345 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 346 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 347 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 348 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 349 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 350 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 351 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 352 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 353 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 354 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 355 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 356 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 357 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 358 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 359 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 360 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 361 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 362 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 363 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 364 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 365 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 366 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 367 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 368 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 369 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 370 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 371 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 372 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 373 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 374 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 375 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 376 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 377 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 378 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 379 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 380 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 381 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 382 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 383 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 384 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 385 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 386 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 387 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 388 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 389 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 390 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 391 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 392 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 393 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 394 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 395 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 396 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 397 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 398 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 399 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 400 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 401 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 402 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 403 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 404 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 405 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 406 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 407 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 408 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 409 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 410 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 411 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 412 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 413 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 414 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 415 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 416 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 417 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 418 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 419 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 420 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 421 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 422 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 423 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 424 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 425 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 426 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 427 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 428 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 429 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 430 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 431 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 432 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 433 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 434 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 435 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 436 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 437 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 438 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 439 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 440 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 441 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 442 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 443 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 444 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 445 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 446 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 447 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
