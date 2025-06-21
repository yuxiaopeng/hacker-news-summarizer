# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-06-21.md)

*最后自动更新时间: 2025-06-21 17:47:57*
## 1. Airpass – 轻松突破WiFi时长限制

**原文标题**: Airpass – easily overcome WiFi time limits

**原文链接**: [https://airpass.tiagoalves.me/](https://airpass.tiagoalves.me/)

Airpass：一款绕过WiFi时间限制的Mac应用。公共WiFi网络通常通过MAC地址追踪用户以实施这些限制。Airpass通过允许用户更新设备的MAC地址来规避这一点。这有效地使WiFi网络将设备视为新的，允许用户再次登录并绕过设定的时间限制。该应用程序由Tiago Alves在航空旅行期间创建。本质上，Airpass通过掩盖设备的身份来欺骗WiFi网络，从而获得延长的访问权限。

---

## 2. 幕后故事：Redpanda Cloud应对GCP中断

**原文标题**: Behind the scenes: Redpanda Cloud's response to the GCP outage

**原文链接**: [https://www.redpanda.com/blog/gcp-outage-june-redpanda-cloud](https://www.redpanda.com/blog/gcp-outage-june-redpanda-cloud)

此博文详述了 Redpanda Cloud 如何应对 2025 年 6 月 12 日全球 Google Cloud Platform (GCP) 中断事件。 尽管此次大规模中断影响了许多服务，但由于 Redpanda Cloud 集群基于单元架构，并着重于高 SLA（99.99% 可用性）的设计，因此保持了稳定。

文章提供了事件时间线，从中断的初始通知开始，随后是 Redpanda 对影响的评估、主动创建的低严重性事件以及对其 GCP 集群的监控。 虽然他们用于云市场管理的供应商以及他们的第三方仪表板和警报系统受到部分影响，但 Redpanda 能够依靠其自我管理的指标和日志记录堆栈来评估影响。

作者强调了理解复杂系统以及实施安全和可靠性措施的重要性。 促成 Redpanda 弹性的因素包括其基于单元的架构、针对高 SLA 的有目的设计（包括数据复制和冗余）、持续测试以及严格的发布工程流程。

文章承认了一些运气成分，例如 Redpanda 在客户堆栈中的位置以及事件期间丢失的节点数量有限。 该帖子还强调了其自我管理的可观测性堆栈的优势。 最终，此次中断对大多数 Redpanda Cloud GCP 客户没有产生负面影响。 文章最后反思了系统思维的重要性以及人工智能在管理复杂系统中可能发挥的作用。 它还提到，由于与内部基础设施组件的异常交互，一个暂存集群受到了影响。

---

## 3. 通过拥抱宽事件并替代OTel来扩展我们的可观测性平台

**原文标题**: Scaling our observability platform by embracing wide events and replacing OTel

**原文链接**: [https://clickhouse.com/blog/scaling-observability-beyond-100pb-wide-events-replacing-otel](https://clickhouse.com/blog/scaling-observability-beyond-100pb-wide-events-replacing-otel)

本文详细介绍了 ClickHouse 如何扩展其内部可观测性平台 LogHouse，从 19 PiB 扩展到超过 100 PB 的未压缩数据，管理近 500 万亿行数据。 最初依赖 OpenTelemetry (OTel) 进行所有日志收集，但随着规模的扩大，他们遇到了效率和数据丢失问题。 OTel 的解析和编组开销，以及收集器代理的资源限制，成为了瓶颈。

为了解决这个问题，他们开发了 SysEx，一种专门用于直接 ClickHouse 到 ClickHouse 数据传输的工具。 SysEx 执行从客户实例中的系统表到 LogHouse 的数据字节对字节复制，消除了中间转换并保留了原生 ClickHouse 类型。 这显着降低了 CPU 使用率（关键数据降低了 90% 以上）并防止了数据丢失。

SysEx 的关键功能包括使用滑动时间窗口从系统表中抓取数据、为 Go ClickHouse 客户端贡献代码以绕过编组，以及使用 ClickHouse 的 Merge 表引擎进行动态模式生成，以处理不断演变的系统表模式。 他们还实现了状态快照，以捕获内存中的系统表。

文章强调，虽然 OTel 很有价值，但在大规模情况下，有时需要专门构建的工具才能获得最佳性能。 ClickHouse 收购 HyperDX 提供了 ClickHouse 原生的 UI，用于探索、关联和根本原因分析，从而摆脱了 Grafana。 最后，他们解锁了全集群范围的查询能力。

---

## 4. 在Ubuntu上使用微软的新CLI文本编辑器

**原文标题**: Using Microsoft's New CLI Text Editor on Ubuntu

**原文链接**: [https://www.omgubuntu.co.uk/2025/06/microsoft-edit-text-editor-ubuntu](https://www.omgubuntu.co.uk/2025/06/microsoft-edit-text-editor-ubuntu)

本文介绍了微软全新的开源命令行文本编辑器“Edit”，它是对旧版 MS-DOS Editor 的现代重构。Edit 使用 Rust 构建，旨在提供类似于 VS Code 的用户友好体验，即使对于不熟悉终端编辑器的用户也易于上手。

虽然 Edit 主要面向缺少原生 CLI 文本编辑器的 Windows 用户，但它也适用于 Linux 和 macOS。熟悉 VS Code 的 Linux 用户可能会喜欢 Edit 共享的快捷键，它提供了 Vim 或 Nano 之外的替代方案。其简单性和速度是主要卖点，即使在处理大型文件时也是如此。

Edit 具有文本驱动的 UI（TUI），是无模式的，并支持鼠标和键盘交互以实现直观使用。它包括查找和替换（使用正则表达式）、自动换行、缩进控制、文件编码设置以及对多个文件的支持等功能。虽然缺乏语法高亮等高级功能，但微软计划在未来添加配色方案和设置 TUI。

本文提供了如何在 Ubuntu 上运行 Edit 的说明。用户可以从 GitHub 下载二进制文件，解压缩并直接从终端运行它。或者，他们可以安装一个非官方的 snap 包。官方二进制文件提供比 snap 包更快的性能。作者鼓励读者尝试 Edit 并分享他们的反馈。

---

## 5. 双射组合艺术

**原文标题**: The Art of Bijective Combinatorics

**原文链接**: [https://www.viennot.org/abjc.html](https://www.viennot.org/abjc.html)

双射组合数学艺术 (ABjC) 是一部“视频书”，包含2016-2019年间在金奈数学科学研究所 (IMSc) 举办的77讲系列视频讲座。这些讲座由 Xavier Viennot 主讲，涵盖双射组合数学及相关主题。ABjC 项目包括视频录像、每讲对应的幻灯片以及一个网站，该网站允许在视频中轻松导航，类似于翻书。

内容分为四个部分，每个部分对应一门课程：1) 枚举、代数和双射组合数学导论；2) 可换性和碎片堆；3) 细胞 ansatz 和二次代数；4) 正交多项式和连分数的组合理论。这些课程分为两个级别，既面向本科/研究生，也面向具有高级主题和“补充”内容的研究人员。

该项目旨在通过提供每个视频的详细描述以及指向特定点的链接来克服视频讲座的局限性。它强调双射视角，结合了可视化数学和动画。作者鼓励在学术文献中引用 ABjC，类似于引用书籍，并提供了引用部分、章节或整个集合的特定格式指南。IMSc 托管着该网站的镜像。

---

## 6. 三星在WANA地区手机上预装IronSource间谍软件应用

**原文标题**: Samsung embeds IronSource spyware app on phones across WANA

**原文链接**: [https://smex.org/open-letter-to-samsung-end-forced-israeli-app-installations-in-the-wana-region/](https://smex.org/open-letter-to-samsung-end-forced-israeli-app-installations-in-the-wana-region/)

该文章关注三星在西亚北非(WANA)地区A和M系列智能手机上预装的AppCloud应用。AppCloud由以色列公司ironSource（现Unity）开发，据称是一款侵入性臃肿软件，未经用户同意收集敏感用户数据，且难以在不损害设备安全的情况下卸载。

该文章指责三星在AppCloud的隐私政策、数据收集方法（包括生物识别信息、IP地址和设备指纹）以及强制安装的原因方面缺乏透明度。据报道，用户对其数据的使用方式一无所知，并且缺乏直接的选择退出方式。这被视为可能违反GDPR和WANA地区相关数据保护法律。

鉴于ironSource的历史以及以色列公司在该地区（如黎巴嫩）周围的法律敏感性，该文章强调了三星合作的伦理和法律影响。文章批评三星在其服务条款中没有明确提及AppCloud，尽管该应用被授予了重要的数据访问权限。

该文章敦促三星披露AppCloud的隐私政策，为用户提供选择退出和删除该应用的方式，解释预安装的决定，并重新考虑未来设备上的预安装。文章最后呼吁召开会议，讨论WANA地区的用户隐私和数据保护问题。简而言之，该文章声称三星正在通过一家有争议的公司提供的一款难以删除的应用程序，强迫WANA地区的客户使用间谍软件，并要求采取行动保护用户。

---

## 7. Weave (YC W25) 招聘创始 AI 工程师

**原文标题**: Weave (YC W25) is hiring a founding AI engineer

**原文链接**: [https://www.ycombinator.com/companies/weave-3/jobs/SqFnIFE-founding-ai-engineer](https://www.ycombinator.com/companies/weave-3/jobs/SqFnIFE-founding-ai-engineer)

Weave (YC W25) 是一家资金充足且盈利的初创公司，致力于开发提高工程团队效率的软件，现诚聘创始 AI 工程师。该职位涉及构建 AI 以理解和改善软件工程师的工作，直接影响产品开发，并通过智能功能取悦客户。

理想的候选人是一位积极进取的工程师，具有务实、同理心和出色的沟通技巧。 具备特定的技术栈经验（React/TypeScript、Go、用于 ML 的 Python）是加分项，但重点在于候选人的学习能力和对成长的承诺。 对提高工程生产力的热情至关重要。

创始 AI 工程师将直接与 CTO (Andrew Churchill，Causal 前创始工程师) 和 CEO (Adam Cohen，高增长初创公司的前销售主管) 合作。薪资为 14 万美元至 20 万美元，股权为 0.20% 至 1.00%。 该职位位于奥克兰/旧金山，需要美国公民身份/签证。

---

## 8. Delta Chat 是一个去中心化的安全通讯应用。

**原文标题**: Delta Chat is a decentralized and secure messenger app

**原文链接**: [https://delta.chat/en/](https://delta.chat/en/)

Delta Chat：基于互联网标准的去中心化安全通讯应用

---

## 9. 微软暂停了海牙国际刑事法院检察官的电子邮件账户。

**原文标题**: Microsoft suspended the email account of an ICC prosecutor at The Hague

**原文链接**: [https://www.nytimes.com/2025/06/20/technology/us-tech-europe-microsoft-trump-icc.html](https://www.nytimes.com/2025/06/20/technology/us-tech-europe-microsoft-trump-icc.html)

无法访问文章链接。

---

## 10. 展示HN：MMOndrian

**原文标题**: Show HN: MMOndrian

**原文链接**: [https://mmondrian.com/](https://mmondrian.com/)

MMOndrian是由谢尔盖·阿列克谢申科创建的多人蒙德里安编辑器。用户可以实时协作，创作出皮特·蒙德里安风格的艺术作品，他以抽象的几何矩形和线条构图而闻名。

界面交互性强且直观。用户可以左键单击（或在移动设备上点击）来重新着色矩形。右键单击（或双击）会添加或删除线条。可以通过拖动来移动线条，并且可以通过相同的操作来平移视图。通过滚动或捏合实现缩放。

界面还显示实时统计信息：当前艺术作品中矩形的数量以及当前在线协作的人数。这促进了一种社区和协作的感觉，因为用户共同为共享画布做出贡献。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 2 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 3 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 4 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 5 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 6 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 7 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 8 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 9 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 10 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 11 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 12 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 13 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 14 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 15 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 16 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 17 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 18 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 19 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 20 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 21 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 22 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 23 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 24 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 25 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 26 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 27 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 28 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 29 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 30 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 31 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 32 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 33 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 34 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 35 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 36 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 37 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 38 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 39 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 40 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 41 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 42 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 43 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 44 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 45 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 46 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 47 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 48 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 49 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 50 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 51 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 52 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 53 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 54 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 55 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 56 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 57 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 58 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 59 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 60 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 61 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 62 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 63 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 64 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 65 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 66 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 67 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 68 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 69 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 70 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 71 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 72 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 73 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 74 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 75 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 76 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 77 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 78 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 79 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 80 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 81 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 82 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 83 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 84 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 85 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 86 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 87 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 88 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 89 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 90 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 91 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 92 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 93 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 94 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
