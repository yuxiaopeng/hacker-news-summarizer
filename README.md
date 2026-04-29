# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-29.md)

*最后自动更新时间: 2026-04-29 18:40:03*
## 1. Zed 1.0

**原文标题**: Zed 1.0

**原文链接**: [https://zed.dev/blog/zed-1-0](https://zed.dev/blog/zed-1-0)

Nathan Sobo 宣布 Zed 1.0 正式发布，标志着这款高性能代码编辑器迎来了一个重要里程碑。Zed 摒弃了 Atom 和 VS Code 所采用的基于 Electron 的架构，而是利用 Rust 语言和 “GPUI” 框架从零开始构建。这一自定义框架将编辑器视作视频游戏引擎，将 UI 渲染交给 GPU 处理，从而突破了 Web 技术的性能限制。

1.0 版本的发布意味着 Zed 已达到专业成熟水平，支持数十种编程语言、Git 集成、SSH 远程连接，并兼容 macOS、Windows 和 Linux 系统。Zed 的一个核心优势在于其 AI 原生基础：它通过 Agent Client Protocol 支持多个并行智能体，并提供高速、按键级的编辑预测。此外，团队还推出了 “Zed for Business”，为企业提供统一计费和管理控制功能。

展望未来，团队正在开发 DeltaDB，这是一款由无冲突复制数据类型 (CRDTs) 驱动的同步引擎。它将实现在共享工作空间中，人类开发者与 AI 智能体之间无缝的字符级协作。虽然 1.0 版本代表了走向主流应用的 “临界点”，但 Sobo 强调，开发工作将保持每周更新的节奏，继续专注于软件工艺和极致性能。

---

## 2. 我们需要一个锻造场联邦。

**原文标题**: We need a federation of forges

**原文链接**: [https://blog.tangled.org/federation/](https://blog.tangled.org/federation/)

文章指出，开源软件（OSS）社区对 GitHub 的过度依赖存在风险，因为中心化系统容易发生故障。作者倡导“代码托管平台联邦化”，并强调电子邮件和 IRC 等成功的长青技术均采用去中心化架构。

协作通常涉及两种协议：一种用于代码传输（git），另一种用于通信。作者介绍了 Tangled 项目，该项目旨在通过使用 git 处理代码并利用 AT 协议（AT Protocol）处理通信，来实现协作过程的去中心化。

Tangled 的核心特性包括：
*   **Knots：** 实现事件联合的独立 git 服务器。
*   **跨服务器协作：** 用户可以跨不同服务器 fork 仓库，并从自己的“knot”向远程服务器提交拉取请求（pull request）。
*   **AT 协议集成：** Tangled 使用 AT 协议处理社交和管理数据，如 issue、拉取请求、关注、点赞（stars）以及 SSH 密钥管理。

最终，Tangled 的目标是提供一个去中心化且具韧性的替代方案，在打破 GitHub 单一文化的同时，保留开发者所青睐的社交与协作体验。

---

## 3. FastCGI: 30 years old and still the better protocol for reverse proxies

**原文标题**: FastCGI: 30 years old and still the better protocol for reverse proxies

**原文链接**: [https://www.agwa.name/blog/post/fastcgi_is_the_better_protocol_for_reverse_proxies](https://www.agwa.name/blog/post/fastcgi_is_the_better_protocol_for_reverse_proxies)

生成摘要时出错

---

## 4. 线上年龄验证是必须坚守的阵地。

**原文标题**: Online age verification is the hill to die on

**原文链接**: [https://x.com/GlennMeder/status/2049088498163216560](https://x.com/GlennMeder/status/2049088498163216560)

所提供的文本是来自 X（原 Twitter）的技术错误提示，表明 JavaScript 已被禁用，因此不包含文章的实际内容。

然而，根据标题 **“在线年龄验证是不容退让的底线”**（该标题涉及当代技术与社会政策中的一个著名论点），以下是通常与该立场相关的核心要点简述：

**摘要**
文章认为，实施强制性在线年龄验证是保护儿童免受不受监管的网络环境所带来的身心伤害的道德和社会必然。作者将这一问题视为“必须坚守的阵地”，暗示这是一个高于一般反对意见的、不可妥协的优先事项。

**关键信息：**
*   **儿童安全至上：** 核心前提是，儿童无限制地接触社交媒体、色情内容和算法陷阱已导致了心理健康危机。作者主张，互联网的“野蛮生长”时代必须结束，以保障未成年人的发育成长。
*   **隐私与保护的博弈：** 文章承认了主要的反方观点——即年龄验证会威胁用户隐私和数据安全。然而，它断言，年轻一代正在遭受的系统性损害是比潜在的数据滥用风险远为严重的危机。
*   **科技巨头的问责：** 文章倡导将责任主体转向科技平台，要求其强制验证用户年龄，而不是允许其打着“用户自由”的旗号从未成年人的参与中获利。
*   **行动号召：** 通过使用“不容退让的底线”这一表达，作者声称这是现代数字政策中最关键的一场战斗，敦促家长和立法者接受以降低在线匿名性为代价，换取对儿童更安全的环境。

*如果您能提供全文或启用 JavaScript 以复制具体内容，我可以对该作者的具体论点提供更详细的分析。*

---

## 5. 政府开源代码平台开启试运行

**原文标题**: Soft launch of open-source code platform for government

**原文链接**: [https://www.nldigitalgovernment.nl/news/soft-launch-for-government-open-source-code-platform/](https://www.nldigitalgovernment.nl/news/soft-launch-for-government-open-source-code-platform/)

荷兰政府宣布试运行 **code.overheid.nl**，这是一个致力于开源软件开发与发布的全新全政府统一平台。

该平台目前处于试点阶段，基于 **Forgejo** 构建。Forgejo 是 GitHub 和 GitLab 等服务的一种具有主权的欧洲开源替代方案。通过采用完全自托管的基础设施，该倡议在公共软件开发中优先考虑数字主权和透明度。

虽然该平台尚未对所有政府机构开放，但其长期目标是将其打造为面向所有荷兰公共机构的共享 Git 环境。该项目是由内政及王国关系部 (BZK) 开源计划办公室 (OSPO) 主导的协作成果，合作伙伴包括 SSC-ICT、Opensourcewerken 以及 developer.overheid.nl。

现诚邀开发人员和政府利益相关者参与试点，并为平台的发展做出贡献。感兴趣的相关方可通过发送邮件至 codeplatform@rijksoverheid.nl 参与其中。

---

## 6. 爱思唯尔整治引用卡特尔，第三名编辑被解雇

**原文标题**: Third Editor Fired in Elsevier's Citation Cartel Crackdown

**原文链接**: [https://www.chrisbrunet.com/p/third-editor-fired-in-elseviers-citation](https://www.chrisbrunet.com/p/third-editor-fired-in-elseviers-citation)

爱思唯尔（Elsevier）已免去约翰·古德尔（John Goodell）《国际商业与金融研究》（RIBAF）期刊主编的职务，这是在持续打击学术“引用卡特尔”行动中发生的第三起高层解雇事件。古德尔被解雇前，其同僚金融学教授布莱恩·卢西（Brian Lucey）和塞缪尔·维涅（Samuel Vigne）也已相继离职，据称古德尔与两人共同运作着一个工业规模的“利益交换”计划。

调查显示，在2021年至2025年间，古德尔的论文产出从每年寥寥几篇激增至50多篇。据称，这种爆发式增长源于一个“赠送署名”圈子：据报道，古德尔会向研究人员承诺在RIBAF上发表论文，作为交换，这些研究人员在向其他期刊投稿时需将他列为共同作者。证据显示，古德尔在卢西和维涅担任编辑的期刊上发表了125篇论文，构建了一个庞大的“引用操纵”网络，从而人为地抬高了他的学术影响力。

文中引用的一个主要案例是安娜·敏·杜（Anna Min Du）博士，她在两年内于RIBAF发表了至少22篇论文，同时在她发表于其他刊物的14篇论文中将古德尔列为共同作者。这种互惠交易使古德尔的引用数据呈现出“J型曲线”，尽管其研究质量存疑，却使他成为爱思唯尔生态系统中被引次数最高的研究人员之一。

尽管爱思唯尔已经更换了涉事编辑，但文章认为，该出版商尚未彻底根除“根源性的腐败”。据估计，约有200至350篇论文可能涉嫌造假并面临撤稿。作者指出，爱思唯尔可能正试图控制丑闻的影响范围，以避免大规模撤稿带来的难堪，尽管多年来其同行评审过程的严谨性已名存实亡。

---

## 7. 一款生产成本仅为 2.5 至 5 美元的开源听诊器

**原文标题**: An open-source stethoscope that costs between $2.5 and $5 to produce

**原文链接**: [https://github.com/GliaX/Stethoscope](https://github.com/GliaX/Stethoscope)

该项目提供了一款开源且经过研究验证的听诊器设计方案，其制造成本仅需 2.50 至 5.00 美元。同行评审的研究证实，其声学性能与行业标准的 Littmann Cardiology III 相当，使其成为资源匮乏地区切实可行的医疗级工具。

**组件与组装**
该设备由五个 3D 打印部件组成：听诊头、耳管、Y 型接头、弹簧和固定环。这些部件需结合廉价的现成硬件，包括：
*   特定规格的半透明硅橡胶管。
*   从标准塑料报告封面剪下的振动膜（厚度约 0.35 毫米）。
*   标准大号硅胶耳塞。

**制造要求**
为确保声学完整性，文档强调所有部件**必须以 100% 填充率打印**。需使用 PETG 或 ABS 耗材以保证其耐用性和耐热性；不建议使用 PLA，因为它在受热时容易变形并导致弹簧过早失效。设计文件使用 CrystalSCAD 和 OpenSCAD 创建，允许用户在出现装配适配问题时微调部件比例。

**质量控制与许可**
对于批量生产，该项目建议每盘打印四个单元以保持一致性，并利用特定的序列号系统来跟踪线材标识和生产数量。该项目根据 TAPR 开源硬件许可协议 (TAPR OHL) 发布，确保设计方案始终可供公众免费使用和改进。

---

## 8. Linux 7.0 导致 PostgreSQL 故障：抢占回归详解

**原文标题**: Linux 7.0 Broke PostgreSQL: The Preemption Regression Explained

**原文链接**: [https://read.thecoder.cafe/p/linux-broke-postgresql](https://read.thecoder.cafe/p/linux-broke-postgresql)

Linux 7.0 中的一个性能回退被发现会导致 PostgreSQL 在高并行系统（如 AWS 的 96 核 Graviton4）上的吞吐量下降近 50%。性能分析显示，系统超过 55% 的 CPU 时间消耗在 `StrategyGetBuffer` 函数内的自旋锁上，该函数负责管理数据库的共享缓冲区池。

该问题源于 Linux 7.0 移除了 `PREEMPT_NONE` 调度模型，使得 `PREEMPT_LAZY` 成为服务器工作负载的默认设置。PostgreSQL 使用自旋锁的前提是假设其持有时间仅为几纳秒。然而，在使用标准的 4 KB 内存页时，后端进程会频繁触发“次要缺页中断”来映射物理内存。

在新的 `PREEMPT_LAZY` 模型下，内核可能会在进程处理缺页中断且持有自旋锁时将其抢占。如果持锁者被停止调度，其他所有尝试获取该锁的后端进程都必须持续“自旋”（消耗 CPU 周期），直到持锁者被重新调度并完成任务。在拥有大量 vCPU 和数百个并发客户端的系统上，这会产生破坏性的 CPU 时间浪费倍增效应。

最有效的解决方案是在 PostgreSQL 中启用**大页 (Huge Pages)**（2 MB 或 1 GB）。这能大幅减少潜在的缺页中断和 TLB（转址旁路缓存）未命中，确保自旋锁的持有时间保持极短。尽管内核工程师建议使用可重入序列 (`rseq`) 来缓解此问题，但对于因内核调度哲学改变而引起的性能回退，PostgreSQL 社区对在应用层采用修复方案仍持谨慎态度。

---

## 9. Cursor Camp

**原文标题**: Cursor Camp

**原文链接**: [https://neal.fun/cursor-camp/](https://neal.fun/cursor-camp/)

生成摘要时出错

---

## 10. Ramp's Sheets AI Exfiltrates Financials

**原文标题**: Ramp's Sheets AI Exfiltrates Financials

**原文链接**: [https://www.promptarmor.com/resources/ramps-sheets-ai-exfiltrates-financials](https://www.promptarmor.com/resources/ramps-sheets-ai-exfiltrates-financials)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 2 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 3 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 4 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 5 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 6 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 7 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 8 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 9 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 10 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 11 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 12 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 13 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 14 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 15 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 16 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 17 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 18 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 19 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 20 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 21 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 22 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 23 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 24 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 25 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 26 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 27 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 28 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 29 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 30 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 31 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 32 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 33 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 34 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 35 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 36 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 37 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 38 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 39 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 40 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 41 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 42 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 43 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 44 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 45 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 46 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 47 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 48 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 49 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 50 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 51 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 52 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 53 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 54 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 55 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 56 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 57 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 58 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 59 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 60 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 61 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 62 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 63 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 64 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 65 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 66 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 67 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 68 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 69 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 70 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 71 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 72 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 73 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 74 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 75 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 76 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 77 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 78 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 79 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 80 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 81 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 82 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 83 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 84 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 85 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 86 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 87 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 88 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 89 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 90 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 91 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 92 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 93 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 94 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 95 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 96 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 97 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 98 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 99 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 100 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 101 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 102 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 103 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 104 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 105 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 106 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 107 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 108 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 109 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 110 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 111 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 112 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 113 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 114 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 115 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 116 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 117 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 118 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 119 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 120 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 121 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 122 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 123 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 124 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 125 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 126 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 127 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 128 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 129 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 130 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 131 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 132 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 133 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 134 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 135 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 136 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 137 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 138 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 139 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 140 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 141 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 142 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 143 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 144 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 145 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 146 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 147 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 148 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 149 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 150 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 151 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 152 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 153 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 154 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 155 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 156 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 157 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 158 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 159 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 160 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 161 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 162 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 163 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 164 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 165 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 166 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 167 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 168 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 169 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 170 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 171 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 172 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 173 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 174 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 175 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 176 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 177 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 178 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 179 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 180 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 181 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 182 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 183 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 184 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 185 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 186 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 187 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 188 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 189 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 190 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 191 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 192 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 193 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 194 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 195 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 196 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 197 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 198 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 199 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 200 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 201 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 202 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 203 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 204 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 205 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 206 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 207 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 208 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 209 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 210 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 211 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 212 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 213 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 214 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 215 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 216 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 217 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 218 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 219 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 220 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 221 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 222 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 223 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 224 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 225 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 226 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 227 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 228 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 229 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 230 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 231 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 232 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 233 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 234 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 235 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 236 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 237 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 238 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 239 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 240 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 241 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 242 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 243 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 244 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 245 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 246 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 247 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 248 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 249 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 250 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 251 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 252 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 253 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 254 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 255 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 256 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 257 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 258 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 259 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 260 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 261 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 262 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 263 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 264 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 265 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 266 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 267 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 268 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 269 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 270 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 271 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 272 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 273 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 274 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 275 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 276 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 277 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 278 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 279 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 280 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 281 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 282 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 283 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 284 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 285 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 286 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 287 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 288 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 289 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 290 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 291 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 292 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 293 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 294 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 295 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 296 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 297 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 298 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 299 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 300 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 301 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 302 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 303 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 304 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 305 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 306 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 307 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 308 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 309 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 310 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 311 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 312 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 313 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 314 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 315 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 316 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 317 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 318 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 319 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 320 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 321 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 322 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 323 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 324 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 325 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 326 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 327 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 328 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 329 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 330 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 331 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 332 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 333 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 334 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 335 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 336 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 337 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 338 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 339 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 340 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 341 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 342 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 343 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 344 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 345 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 346 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 347 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 348 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 349 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 350 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 351 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 352 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 353 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 354 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 355 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 356 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 357 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 358 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 359 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 360 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 361 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 362 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 363 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 364 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 365 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 366 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 367 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 368 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 369 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 370 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 371 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 372 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 373 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 374 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 375 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 376 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 377 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 378 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 379 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 380 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 381 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 382 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 383 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 384 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 385 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 386 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 387 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 388 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 389 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 390 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 391 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 392 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 393 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 394 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 395 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 396 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 397 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 398 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 399 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 400 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 401 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 402 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 403 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 404 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 405 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
