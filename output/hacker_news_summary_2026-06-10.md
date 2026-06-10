# Hacker News 热门文章摘要 (2026-06-10)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Mercedes‑Benz starts large‑scale production of electric axial flux motor

**原文标题**: Mercedes‑Benz starts large‑scale production of electric axial flux motor

**原文链接**: [https://media.mercedes-benz.com/en/article/bebac2af-acdc-465a-9538-adb0bf3d8ccf](https://media.mercedes-benz.com/en/article/bebac2af-acdc-465a-9538-adb0bf3d8ccf)

生成摘要时出错

---

## 12. Show HN: Extend UI – open-source UI kit for modern document apps

**原文标题**: Show HN: Extend UI – open-source UI kit for modern document apps

**原文链接**: [https://www.extend.ai/ui](https://www.extend.ai/ui)

生成摘要时出错

---

## 13. Show HN: HelixDB – A graph database built on object storage

**原文标题**: Show HN: HelixDB – A graph database built on object storage

**原文链接**: [https://github.com/HelixDB/helix-db/tree/main](https://github.com/HelixDB/helix-db/tree/main)

生成摘要时出错

---

## 14. Apache Burr: Build reliable AI agents and applications

**原文标题**: Apache Burr: Build reliable AI agents and applications

**原文链接**: [https://burr.apache.org/](https://burr.apache.org/)

生成摘要时出错

---

## 15. All 9,300 Japanese train station, animated by the year it opened (1872–2026)

**原文标题**: All 9,300 Japanese train station, animated by the year it opened (1872–2026)

**原文链接**: [https://jivx.com/eki](https://jivx.com/eki)

生成摘要时出错

---

## 16. A €0.01 bank transfer could compromise a banking AI agent

**原文标题**: A €0.01 bank transfer could compromise a banking AI agent

**原文链接**: [https://blue41.com/blog/how-we-helped-bunq-secure-their-financial-ai-assistant/](https://blue41.com/blog/how-we-helped-bunq-secure-their-financial-ai-assistant/)

生成摘要时出错

---

## 17. The Dynamo and the Computer: The Modern Productivity Paradox (1989) [pdf]

**原文标题**: The Dynamo and the Computer: The Modern Productivity Paradox (1989) [pdf]

**原文链接**: [https://www.almendron.com/tribuna/wp-content/uploads/2018/03/the-dynamo-and-the-computer-an-historical-perspective-on-the-modern-productivity-paradox.pdf](https://www.almendron.com/tribuna/wp-content/uploads/2018/03/the-dynamo-and-the-computer-an-historical-perspective-on-the-modern-productivity-paradox.pdf)

生成摘要时出错

---

## 18. DiffusionGemma: 4x Faster Text Generation

**原文标题**: DiffusionGemma: 4x Faster Text Generation

**原文链接**: [https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/](https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/)

生成摘要时出错

---

## 19. GeoLibre 1.0

**原文标题**: GeoLibre 1.0

**原文链接**: [https://geolibre.app/](https://geolibre.app/)

生成摘要时出错

---

## 20. Who's the Smartest Corvid?

**原文标题**: Who's the Smartest Corvid?

**原文链接**: [https://thetyee.ca/Culture/2026/06/05/Whos-the-Smartest-Corvid/](https://thetyee.ca/Culture/2026/06/05/Whos-the-Smartest-Corvid/)

生成摘要时出错

---

## 21. Buy a train, bridge or tracks from the Swiss Railway

**原文标题**: Buy a train, bridge or tracks from the Swiss Railway

**原文链接**: [https://sbbresale.ch/](https://sbbresale.ch/)

生成摘要时出错

---

## 22. The iPad was on Tailscale: a WebRTC debugging story

**原文标题**: The iPad was on Tailscale: a WebRTC debugging story

**原文链接**: [https://p2claw.com/blog/2026-06-09-the-ipad-was-on-tailscale/](https://p2claw.com/blog/2026-06-09-the-ipad-was-on-tailscale/)

生成摘要时出错

---

## 23. Who Runs Your Rust Future? Hands-On Intro to Async Rust

**原文标题**: Who Runs Your Rust Future? Hands-On Intro to Async Rust

**原文链接**: [https://aibodh.com/posts/async-rust-chapter-1-hands-on-intro-to-async-rust/](https://aibodh.com/posts/async-rust-chapter-1-hands-on-intro-to-async-rust/)

生成摘要时出错

---

## 24. 'They take you out of life, out of time': a journey into Spain's cave paintings

**原文标题**: 'They take you out of life, out of time': a journey into Spain's cave paintings

**原文链接**: [https://www.theguardian.com/science/2026/jun/02/journey-into-spain-palaeolithic-cave-paintings-altamira](https://www.theguardian.com/science/2026/jun/02/journey-into-spain-palaeolithic-cave-paintings-altamira)

生成摘要时出错

---

## 25. The Case for Free Online Books (2014)

**原文标题**: The Case for Free Online Books (2014)

**原文链接**: [http://from-a-to-remzi.blogspot.com/2014/01/the-case-for-free-online-books-fobs.html](http://from-a-to-remzi.blogspot.com/2014/01/the-case-for-free-online-books-fobs.html)

生成摘要时出错

---

## 26. Reviving Papers with Code

**原文标题**: Reviving Papers with Code

**原文链接**: [https://paperswithcode.co/](https://paperswithcode.co/)

生成摘要时出错

---

## 27. macOS Container Machines

**原文标题**: macOS Container Machines

**原文链接**: [https://github.com/apple/container/blob/main/docs/container-machine.md](https://github.com/apple/container/blob/main/docs/container-machine.md)

生成摘要时出错

---

## 28. Claude Fable 5

**原文标题**: Claude Fable 5

**原文链接**: [https://www.anthropic.com/news/claude-fable-5-mythos-5](https://www.anthropic.com/news/claude-fable-5-mythos-5)

生成摘要时出错

---

## 29. The Last Evolution, by John W Campbell Jr. (1932)

**原文标题**: The Last Evolution, by John W Campbell Jr. (1932)

**原文链接**: [https://www.gutenberg.org/files/27462/27462-h/27462-h.htm](https://www.gutenberg.org/files/27462/27462-h/27462-h.htm)

生成摘要时出错

---

## 30. Claude Fable 5

**原文标题**: Claude Fable 5

**原文链接**: [https://www.anthropic.com/news/claude-fable-5-mythos-5](https://www.anthropic.com/news/claude-fable-5-mythos-5)

生成摘要时出错

---

## 31. Babel-USB: USB drive with every file

**原文标题**: Babel-USB: USB drive with every file

**原文链接**: [https://github.com/p2r3/babel-usb](https://github.com/p2r3/babel-usb)

生成摘要时出错

---

## 32. Anatomy of a high-performance EP kernel

**原文标题**: Anatomy of a high-performance EP kernel

**原文链接**: [https://fergusfinn.com/blog/anatomy-of-a-high-performance-ep-kernel/](https://fergusfinn.com/blog/anatomy-of-a-high-performance-ep-kernel/)

生成摘要时出错

---

## 33. Smudging the game disc to make speedrunning 'SpongeBob' faster

**原文标题**: Smudging the game disc to make speedrunning 'SpongeBob' faster

**原文链接**: [https://www.inverse.com/input/gaming/the-dirty-secret-that-makes-speedrunning-on-spongebob-a-lot-faster](https://www.inverse.com/input/gaming/the-dirty-secret-that-makes-speedrunning-on-spongebob-a-lot-faster)

生成摘要时出错

---

## 34. RIP software hackathons. Long live the hardware hackathon

**原文标题**: RIP software hackathons. Long live the hardware hackathon

**原文链接**: [https://blog.oscars.dev/posts/rip-software-hackathons-long-live-the-hardware-hackathon/](https://blog.oscars.dev/posts/rip-software-hackathons-long-live-the-hardware-hackathon/)

生成摘要时出错

---

## 35. Surprise, pay $1000

**原文标题**: Surprise, pay $1000

**原文链接**: [https://forestwalk.ai/blog/surprise-blacksmith-costs/](https://forestwalk.ai/blog/surprise-blacksmith-costs/)

生成摘要时出错

---

## 36. German ruling declares Google liable for false answers in AI Overviews

**原文标题**: German ruling declares Google liable for false answers in AI Overviews

**原文链接**: [https://the-decoder.com/landmark-german-ruling-declares-googles-ai-overviews-are-googles-own-words-and-makes-it-liable-for-false-answers/](https://the-decoder.com/landmark-german-ruling-declares-googles-ai-overviews-are-googles-own-words-and-makes-it-liable-for-false-answers/)

生成摘要时出错

---

## 37. Hacking for Defense Stanford 2026 – Lessons Learned Presentations

**原文标题**: Hacking for Defense Stanford 2026 – Lessons Learned Presentations

**原文链接**: [https://steveblank.com/2026/06/08/g-for-defense-stanford-2026-lessons-learned-presentations/](https://steveblank.com/2026/06/08/g-for-defense-stanford-2026-lessons-learned-presentations/)

生成摘要时出错

---

## 38. Chrome is looking to permanently drop MV2 extension

**原文标题**: Chrome is looking to permanently drop MV2 extension

**原文链接**: [https://www.neowin.net/news/google-chrome-is-killing-all-ublock-origin-bypasses-microsoft-edge-opera-to-follow/](https://www.neowin.net/news/google-chrome-is-killing-all-ublock-origin-bypasses-microsoft-edge-opera-to-follow/)

生成摘要时出错

---

## 39. Farmer donates land for a park, city sells it for $10M as data center land

**原文标题**: Farmer donates land for a park, city sells it for $10M as data center land

**原文链接**: [https://www.tomshardware.com/tech-industry/farmer-donates-land-for-a-park-city-sells-it-for-data-center-development-usd10-gift-became-usd10m-for-city-government-with-usd30m-tax-expected-over-next-decade](https://www.tomshardware.com/tech-industry/farmer-donates-land-for-a-park-city-sells-it-for-data-center-development-usd10-gift-became-usd10m-for-city-government-with-usd30m-tax-expected-over-next-decade)

生成摘要时出错

---

## 40. Rich Sutton on AI creativity and discovery

**原文标题**: Rich Sutton on AI creativity and discovery

**原文链接**: [https://twitter.com/RichardSSutton/status/2061216087744946656](https://twitter.com/RichardSSutton/status/2061216087744946656)

生成摘要时出错

---

## 41. Magnetoelectric antennas could transform how underwater robots talk

**原文标题**: Magnetoelectric antennas could transform how underwater robots talk

**原文链接**: [https://newatlas.com/engineering/magnetoelectric-antennas-submarine-robots-communications/](https://newatlas.com/engineering/magnetoelectric-antennas-submarine-robots-communications/)

生成摘要时出错

---

## 42. Spoiling Linux Kernel with "sanctioned" code

**原文标题**: Spoiling Linux Kernel with "sanctioned" code

**原文链接**: [https://printserver.ink/blog/spoiling-the-kernel/](https://printserver.ink/blog/spoiling-the-kernel/)

生成摘要时出错

---

## 43. BYD to install 5-minute EV chargers across Europe

**原文标题**: BYD to install 5-minute EV chargers across Europe

**原文链接**: [https://www.theverge.com/transportation/947553/byd-flash-chargers-uk-europe-ev-blade-battery](https://www.theverge.com/transportation/947553/byd-flash-chargers-uk-europe-ev-blade-battery)

生成摘要时出错

---

## 44. How do you design a $30k electric pickup? Inside Ford's skunkworks

**原文标题**: How do you design a $30k electric pickup? Inside Ford's skunkworks

**原文链接**: [https://arstechnica.com/cars/2026/05/how-do-you-design-a-30000-electric-pickup-inside-fords-skunkworks/](https://arstechnica.com/cars/2026/05/how-do-you-design-a-30000-electric-pickup-inside-fords-skunkworks/)

生成摘要时出错

---

## 45. OpenCV 5 Is Here: The Biggest Leap in Years for Computer Vision

**原文标题**: OpenCV 5 Is Here: The Biggest Leap in Years for Computer Vision

**原文链接**: [https://opencv.org/opencv-5/](https://opencv.org/opencv-5/)

生成摘要时出错

---

## 46. I thought I knew how electrolysis worked [video]

**原文标题**: I thought I knew how electrolysis worked [video]

**原文链接**: [https://www.youtube.com/watch?v=eq7fR9ISuCw](https://www.youtube.com/watch?v=eq7fR9ISuCw)

生成摘要时出错

---

## 47. I Hate (Most) Keyboard 'Fn' Keys

**原文标题**: I Hate (Most) Keyboard 'Fn' Keys

**原文链接**: [https://danq.me/2026/06/09/fn-keys/](https://danq.me/2026/06/09/fn-keys/)

生成摘要时出错

---

## 48. Show HN: macOS menu bar gauges for your Claude Code quota

**原文标题**: Show HN: macOS menu bar gauges for your Claude Code quota

**原文链接**: [https://github.com/grzegorz-raczek-unit8/claude-quota](https://github.com/grzegorz-raczek-unit8/claude-quota)

生成摘要时出错

---

## 49. The oldest surviving animated feature film at 100

**原文标题**: The oldest surviving animated feature film at 100

**原文链接**: [https://www.bbc.com/culture/article/20260603-how-a-26-year-old-german-woman-made-the-worlds-oldest-surviving-animated-feature-film](https://www.bbc.com/culture/article/20260603-how-a-26-year-old-german-woman-made-the-worlds-oldest-surviving-animated-feature-film)

生成摘要时出错

---

## 50. Notes on DeepSeek

**原文标题**: Notes on DeepSeek

**原文链接**: [https://twitter.com/NikoMcCarty/status/2064686557400100884](https://twitter.com/NikoMcCarty/status/2064686557400100884)

生成摘要时出错

---

## 51. More Molly Guards

**原文标题**: More Molly Guards

**原文链接**: [https://unsung.aresluna.org/more-molly-guards/](https://unsung.aresluna.org/more-molly-guards/)

生成摘要时出错

---

## 52. Oh Good, Screwworms Are Back

**原文标题**: Oh Good, Screwworms Are Back

**原文链接**: [https://www.marginallycompelling.com/p/oh-good-screwworms-are-back](https://www.marginallycompelling.com/p/oh-good-screwworms-are-back)

生成摘要时出错

---

## 53. US Consumer Price Index up 4.2%

**原文标题**: US Consumer Price Index up 4.2%

**原文链接**: [https://www.bls.gov/news.release/cpi.nr0.htm](https://www.bls.gov/news.release/cpi.nr0.htm)

生成摘要时出错

---

## 54. Show HN: Ustps (UDP Speedy Transmission Protocol Secure) and USSH

**原文标题**: Show HN: Ustps (UDP Speedy Transmission Protocol Secure) and USSH

**原文链接**: [https://github.com/x1colegal/USTP-Secure](https://github.com/x1colegal/USTP-Secure)

生成摘要时出错

---

## 55. If Claude Fable stops helping you, you'll never know

**原文标题**: If Claude Fable stops helping you, you'll never know

**原文链接**: [https://jonready.com/blog/posts/claude-fable5-is-allowed-to-sabotage-your-app-if-youre-a-competitor.html](https://jonready.com/blog/posts/claude-fable5-is-allowed-to-sabotage-your-app-if-youre-a-competitor.html)

生成摘要时出错

---

## 56. CEOs who think AI replaces their employees are just bad CEOs

**原文标题**: CEOs who think AI replaces their employees are just bad CEOs

**原文链接**: [https://www.techdirt.com/2026/06/09/ceos-who-think-ai-replaces-their-employees-are-just-bad-ceos/](https://www.techdirt.com/2026/06/09/ceos-who-think-ai-replaces-their-employees-are-just-bad-ceos/)

生成摘要时出错

---

## 57. Upcoming breaking changes for npm v12

**原文标题**: Upcoming breaking changes for npm v12

**原文链接**: [https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/](https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/)

生成摘要时出错

---

## 58. Emerge Career (YC S22) Is Hiring a Founding Growth Marketer

**原文标题**: Emerge Career (YC S22) Is Hiring a Founding Growth Marketer

**原文链接**: [https://www.ycombinator.com/companies/emerge-career/jobs/v0S1AEG-founding-growth-marketer](https://www.ycombinator.com/companies/emerge-career/jobs/v0S1AEG-founding-growth-marketer)

生成摘要时出错

---

## 59. Lies we tell ourselves about email addresses

**原文标题**: Lies we tell ourselves about email addresses

**原文链接**: [https://gitpush--force.com/commits/2026/06/lies-we-tell-ourselves-about-email/](https://gitpush--force.com/commits/2026/06/lies-we-tell-ourselves-about-email/)

生成摘要时出错

---

## 60. Postgres by Example

**原文标题**: Postgres by Example

**原文链接**: [https://github.com/boringcollege/postgres-by-example](https://github.com/boringcollege/postgres-by-example)

生成摘要时出错

---

## 61. Stackoverflow for Agents

**原文标题**: Stackoverflow for Agents

**原文链接**: [https://stackoverflow.blog/2026/06/10/announcing-stack-overflow-for-agents/](https://stackoverflow.blog/2026/06/10/announcing-stack-overflow-for-agents/)

生成摘要时出错

---

## 62. Making Graphics Like it's 1993

**原文标题**: Making Graphics Like it's 1993

**原文链接**: [https://staniks.github.io/articles/catlantean-3d-blog-1/](https://staniks.github.io/articles/catlantean-3d-blog-1/)

生成摘要时出错

---

## 63. U.S. kids no longer reading for pleasure

**原文标题**: U.S. kids no longer reading for pleasure

**原文链接**: [https://www.nbcnews.com/data-graphics/kids-reading-less-lower-levels-department-education-study-rcna348987](https://www.nbcnews.com/data-graphics/kids-reading-less-lower-levels-department-education-study-rcna348987)

生成摘要时出错

---

## 64. Grit: Rewriting Git in Rust with agents

**原文标题**: Grit: Rewriting Git in Rust with agents

**原文链接**: [https://blog.gitbutler.com/true-grit](https://blog.gitbutler.com/true-grit)

生成摘要时出错

---

## 65. A giant star may have destroyed itself in one of the rarest explosions

**原文标题**: A giant star may have destroyed itself in one of the rarest explosions

**原文链接**: [https://phys.org/news/2026-05-giant-star-destroyed-universe-rarest.html](https://phys.org/news/2026-05-giant-star-destroyed-universe-rarest.html)

生成摘要时出错

---

## 66. Test-case reducers are underappreciated debugging tools

**原文标题**: Test-case reducers are underappreciated debugging tools

**原文链接**: [https://tratt.net/laurie/blog/2026/test_case_reducers_are_underappreciated_debugging_tools.html](https://tratt.net/laurie/blog/2026/test_case_reducers_are_underappreciated_debugging_tools.html)

生成摘要时出错

---

## 67. Linux latency measurements and compositor tuning [KWin Wayland]

**原文标题**: Linux latency measurements and compositor tuning [KWin Wayland]

**原文链接**: [https://farnoy.dev/posts/linux-latency](https://farnoy.dev/posts/linux-latency)

生成摘要时出错

---

## 68. WWDC 2026: Apple is Folding

**原文标题**: WWDC 2026: Apple is Folding

**原文链接**: [https://cupertinolens.com/2026/06/09/wwdc-2026-apple-is-folding/](https://cupertinolens.com/2026/06/09/wwdc-2026-apple-is-folding/)

生成摘要时出错

---

## 69. Show HN: NBSDgames – 21 new, improved, original text games for Unix, DOS, Plan9

**原文标题**: Show HN: NBSDgames – 21 new, improved, original text games for Unix, DOS, Plan9

**原文链接**: [https://github.com/abakh/nbsdgames](https://github.com/abakh/nbsdgames)

生成摘要时出错

---

## 70. Why LLMs still lack taste

**原文标题**: Why LLMs still lack taste

**原文链接**: [https://beyondtheprior.com/post/why-llms-lack-taste/](https://beyondtheprior.com/post/why-llms-lack-taste/)

生成摘要时出错

---

## 71. In a U.S. First, Solar Supplied More Power Than Coal Last Month

**原文标题**: In a U.S. First, Solar Supplied More Power Than Coal Last Month

**原文链接**: [https://e360.yale.edu/digest/us-solar-coal](https://e360.yale.edu/digest/us-solar-coal)

生成摘要时出错

---

## 72. Premature optimization is fun sometimes

**原文标题**: Premature optimization is fun sometimes

**原文链接**: [https://invlpg.com/posts/2025-06-19-premature-optimization.html](https://invlpg.com/posts/2025-06-19-premature-optimization.html)

生成摘要时出错

---

## 73. Show HN: Gravity – Interactive solar-system simulator, from Newton to Einstein

**原文标题**: Show HN: Gravity – Interactive solar-system simulator, from Newton to Einstein

**原文链接**: [https://qunabu.github.io/Gravity/](https://qunabu.github.io/Gravity/)

生成摘要时出错

---

## 74. What it feels like to work with Mythos

**原文标题**: What it feels like to work with Mythos

**原文链接**: [https://www.oneusefulthing.org/p/what-it-feels-like-to-work-with-mythos](https://www.oneusefulthing.org/p/what-it-feels-like-to-work-with-mythos)

生成摘要时出错

---

## 75. Ultrafast machine learning on FPGAs via Kolmogorov-Arnold Networks

**原文标题**: Ultrafast machine learning on FPGAs via Kolmogorov-Arnold Networks

**原文链接**: [https://aarushgupta.io/posts/kan-fpga/](https://aarushgupta.io/posts/kan-fpga/)

生成摘要时出错

---

## 76. Is Grep All You Need? How Agent Harnesses Reshape Agentic Search

**原文标题**: Is Grep All You Need? How Agent Harnesses Reshape Agentic Search

**原文链接**: [https://arxiv.org/abs/2605.15184](https://arxiv.org/abs/2605.15184)

生成摘要时出错

---

## 77. iOS 27 features we didn't see onstage

**原文标题**: iOS 27 features we didn't see onstage

**原文链接**: [https://techcrunch.com/2026/06/09/ios-27-features-we-didnt-see-on-stage/](https://techcrunch.com/2026/06/09/ios-27-features-we-didnt-see-on-stage/)

生成摘要时出错

---

## 78. Vibe coding my way to a healthy family: Introducing Gamow Labs

**原文标题**: Vibe coding my way to a healthy family: Introducing Gamow Labs

**原文链接**: [https://www.ddmckinnon.com/2026/06/09/vibe-coding-my-way-to-a-healthy-family-introducing-gamow-labs/](https://www.ddmckinnon.com/2026/06/09/vibe-coding-my-way-to-a-healthy-family-introducing-gamow-labs/)

生成摘要时出错

---

## 79. Microsoft's open source tools were hacked to steal passwords of AI developers

**原文标题**: Microsoft's open source tools were hacked to steal passwords of AI developers

**原文链接**: [https://techcrunch.com/2026/06/08/microsofts-open-source-tools-were-hacked-to-steal-passwords-of-ai-developers/](https://techcrunch.com/2026/06/08/microsofts-open-source-tools-were-hacked-to-steal-passwords-of-ai-developers/)

生成摘要时出错

---

## 80. FCC wants to kill burner phones by forcing telecoms to get all customers' IDs

**原文标题**: FCC wants to kill burner phones by forcing telecoms to get all customers' IDs

**原文链接**: [https://www.404media.co/fcc-wants-to-kill-burner-phones-by-forcing-telecoms-to-get-all-customers-ids/](https://www.404media.co/fcc-wants-to-kill-burner-phones-by-forcing-telecoms-to-get-all-customers-ids/)

生成摘要时出错

---

## 81. Show HN: GentleOS – A pair of hobby OSes for vintage 32-bit and 16-bit PCs

**原文标题**: Show HN: GentleOS – A pair of hobby OSes for vintage 32-bit and 16-bit PCs

**原文链接**: [https://github.com/luke8086/gentleos32](https://github.com/luke8086/gentleos32)

生成摘要时出错

---

## 82. The iPhone's Last Stand?

**原文标题**: The iPhone's Last Stand?

**原文链接**: [https://stratechery.com/2026/the-iphones-last-stand/](https://stratechery.com/2026/the-iphones-last-stand/)

生成摘要时出错

---

## 83. Exif Smuggling (2025)

**原文标题**: Exif Smuggling (2025)

**原文链接**: [https://github.com/signalblur/exifsmugglingpoc](https://github.com/signalblur/exifsmugglingpoc)

生成摘要时出错

---

## 84. Providers, not insurers, are responsible for excess U.S. health care cost (2024)

**原文标题**: Providers, not insurers, are responsible for excess U.S. health care cost (2024)

**原文链接**: [https://www.noahpinion.blog/p/insurers-arent-the-main-villain-of](https://www.noahpinion.blog/p/insurers-arent-the-main-villain-of)

生成摘要时出错

---

## 85. Let's Encrypt bans certificate usage in any US sanctioned territory [pdf]

**原文标题**: Let's Encrypt bans certificate usage in any US sanctioned territory [pdf]

**原文链接**: [https://letsencrypt.org/documents/LE-SA-v1.7-June-04-2026-diff.pdf](https://letsencrypt.org/documents/LE-SA-v1.7-June-04-2026-diff.pdf)

生成摘要时出错

---

## 86. The LD_DEBUG environment variable (2012)

**原文标题**: The LD_DEBUG environment variable (2012)

**原文链接**: [https://bnikolic.co.uk/blog/linux-ld-debug.html](https://bnikolic.co.uk/blog/linux-ld-debug.html)

生成摘要时出错

---

## 87. Forever Young: how one molecule can lock plants in a youthful state (2025)

**原文标题**: Forever Young: how one molecule can lock plants in a youthful state (2025)

**原文链接**: [https://omnia.sas.upenn.edu/story/biologist-scott-poethig-plants-never-age](https://omnia.sas.upenn.edu/story/biologist-scott-poethig-plants-never-age)

生成摘要时出错

---

## 88. Thi.ng – open-source building blocks for computational design and art

**原文标题**: Thi.ng – open-source building blocks for computational design and art

**原文链接**: [https://thi.ng](https://thi.ng)

生成摘要时出错

---

## 89. Apple decided not to roll out Siri in EU after denied request for exemption

**原文标题**: Apple decided not to roll out Siri in EU after denied request for exemption

**原文链接**: [https://www.reuters.com/business/apple-failed-make-its-ai-tool-comply-eu-regulations-eu-commission-says-2026-06-09/](https://www.reuters.com/business/apple-failed-make-its-ai-tool-comply-eu-regulations-eu-commission-says-2026-06-09/)

生成摘要时出错

---

## 90. Computer Lessons

**原文标题**: Computer Lessons

**原文链接**: [https://technicshistory.com/2026/06/06/computer-lessons/](https://technicshistory.com/2026/06/06/computer-lessons/)

生成摘要时出错

---

## 91. Value Numbering

**原文标题**: Value Numbering

**原文链接**: [https://bernsteinbear.com/blog/value-numbering/](https://bernsteinbear.com/blog/value-numbering/)

生成摘要时出错

---

## 92. Cops Keep Getting Arrested for Using Flock to Stalk People

**原文标题**: Cops Keep Getting Arrested for Using Flock to Stalk People

**原文链接**: [https://www.404media.co/cops-keep-getting-arrested-for-using-flock-to-stalk-people/](https://www.404media.co/cops-keep-getting-arrested-for-using-flock-to-stalk-people/)

生成摘要时出错

---

## 93. Job: Head of Stonehenge

**原文标题**: Job: Head of Stonehenge

**原文链接**: [https://www.english-heritage.org.uk/about/our-people/careers-with-us/job-search/default-job-page/?jobRef=16449](https://www.english-heritage.org.uk/about/our-people/careers-with-us/job-search/default-job-page/?jobRef=16449)

生成摘要时出错

---

## 94. I Hacked into the Worst E-Bike and Fixed It [video]

**原文标题**: I Hacked into the Worst E-Bike and Fixed It [video]

**原文链接**: [https://www.youtube.com/watch?v=hPrtVGimBYs](https://www.youtube.com/watch?v=hPrtVGimBYs)

生成摘要时出错

---

## 95. Show HN: Resonate – Low-latency, high-resolution spectral analysis

**原文标题**: Show HN: Resonate – Low-latency, high-resolution spectral analysis

**原文链接**: [https://alexandrefrancois.org/Resonate/](https://alexandrefrancois.org/Resonate/)

生成摘要时出错

---

## 96. Port React Compiler to Rust

**原文标题**: Port React Compiler to Rust

**原文链接**: [https://github.com/react/react/pull/36173](https://github.com/react/react/pull/36173)

生成摘要时出错

---

## 97. Social Security Now Expects Shortfall Earlier, in Late 2032

**原文标题**: Social Security Now Expects Shortfall Earlier, in Late 2032

**原文链接**: [https://www.wsj.com/politics/policy/social-security-trust-insolvency-2032-d26bf25e](https://www.wsj.com/politics/policy/social-security-trust-insolvency-2032-d26bf25e)

生成摘要时出错

---

## 98. Biff.core: system composition for Clojure web apps

**原文标题**: Biff.core: system composition for Clojure web apps

**原文链接**: [https://biffweb.com/p/core/](https://biffweb.com/p/core/)

生成摘要时出错

---

## 99. Apple reveals new AI architecture built around Google Gemini models

**原文标题**: Apple reveals new AI architecture built around Google Gemini models

**原文链接**: [https://www.macrumors.com/2026/06/08/apple-reveals-new-ai-architecture/](https://www.macrumors.com/2026/06/08/apple-reveals-new-ai-architecture/)

生成摘要时出错

---

## 100. We found a $60 Hetzner VM competing with AWS and Google VMs over $500/mo

**原文标题**: We found a $60 Hetzner VM competing with AWS and Google VMs over $500/mo

**原文链接**: [https://webbynode.com/articles/a-60-hetzner-vm-is-challenging-aws-and-google-cloud-instances-costing-8-to-9x-more](https://webbynode.com/articles/a-60-hetzner-vm-is-challenging-aws-and-google-cloud-instances-costing-8-to-9x-more)

生成摘要时出错

---

