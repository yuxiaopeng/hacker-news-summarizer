# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-08-12.md)

*最后自动更新时间: 2026-08-12 18:27:14*
## 1. DeepSeek V4 专业版 0813

**原文标题**: DeepSeek V4 Pro 0813

**原文链接**: [https://openrouter.ai/deepseek/deepseek-v4-pro-0813](https://openrouter.ai/deepseek/deepseek-v4-pro-0813)

无法访问文章链接。

---

## 2. Tailscale 将数据库损坏追溯到存在 16 年之久的 SQLite WAL 重置漏洞

**原文标题**: Tailscale Traces Database Corruption to 16y/o SQLite WAL-Reset Bug

**原文链接**: [https://tailscale.com/blog/sqlite-wal-reset-bug](https://tailscale.com/blog/sqlite-wal-reset-bug)

Tailscale 最近通过协助发现 SQLite 中一个潜伏了 16 年的漏洞，解决了一系列频发的数据库损坏事件。在过去的六个月里，Tailscale 的控制面（采用手动检查点的分片式 SQLite 架构）遭遇了 19 次损坏，导致了服务不稳定和轻微的元数据丢失。

由于该漏洞无法在测试环境中复现且呈现偶发性，诊断过程异常困难。Tailscale 与 SQLite 核心开发者合作，实施了事务日志流水线和自定义虚拟文件系统追踪层（`tmstmpvfs`），以便在生产环境中捕获该错误。他们发现，已提交的数据在“检查点（checkpointing）”过程中“消失”了，即数据从预写日志（WAL）移动到主数据库文件的过程中发生了丢失。

根本原因被确定为“WAL-Reset 漏洞”，这是一种在写事务与检查点之间发生的罕见竞态条件。在特定的时机下，检查点进程会错误地认为某些数据页已复制到主数据库并将其遗漏；当 WAL 随后被重置时，便会导致永久性的数据损坏。由于 Tailscale 频繁使用手动检查点进行备份，因此特别容易受到该漏洞的影响。

修复过程曾遭遇短暂阻碍：最初的修复版本（SQLite 3.52.0）由于表达式索引中浮点数舍入规则的变化，触发了虚假的损坏警告。Tailscale 通过调整其时间戳精度缓解了这一问题，而 SQLite 开发者则在 3.51.3 和 3.53.0 版本中发布了专门的修复补丁。随着这些更新的部署，Tailscale 报告服务已恢复稳定，成功结束了这场针对 SQLite 潜伏时间最长的隐蔽缺陷之一、为期数月的深入调查。

---

## 3. 2026年日食网络摄像头

**原文标题**: 2026 Eclipse Webcams

**原文链接**: [https://jonty.github.io/2026_eclipse_webcams/](https://jonty.github.io/2026_eclipse_webcams/)

生成摘要时出错

---

## 4. 气候仪表盘上的冰川

**原文标题**: Glaciers on the Climate Dashboard

**原文链接**: [https://climate.metoffice.cloud/glaciers.html](https://climate.metoffice.cloud/glaciers.html)

本文探讨了全球冰川的现状、其在环境中的作用以及追踪其消退的方法。冰川由积雪压缩而成，充当着重要的水库，在旱季提供淡水。然而，冰川融化是全球海平面上升的主要原因，威胁着沿海社区。

**当前趋势与观测**
世界冰川监测服务处 (WGMS) 的数据表明，自 19 世纪以来，冰川一直处于长期退缩状态，且自 20 世纪 80 年代末以来，其缩减速度明显加快。自 1976 年以来，参考冰川的累计质量损失约为 20 米“水当量”。包括美国国家航空航天局 (NASA) 和澳大利亚联邦科学与工业研究组织 (CSIRO) 在内的多家机构的卫星数据证实，由于这种消融，全球海平面呈持续长期上升趋势。

**变化的驱动因素**
冰川的健康状况取决于其“质量平衡”——即积雪量与冰流失量之间的差值。虽然冰川对气温、降水、湿度和云量等自然因素非常敏感，但政府间气候变化专门委员会第五次评估报告 (IPCC AR5) 以高度可信度得出结论，自 20 世纪 60 年代以来观测到的质量损失中，人为影响是一个主要驱动因素。

**监测技术**
科学家使用以下几种方法测量冰川变化：
*   **物理测量：** 利用测量杆量化冰流失，并通过挖掘雪坑或分析冰裂隙来测量积雪量。
*   **遥感技术：** 利用卫星雷达和可见光传感器测绘高度和形状。
*   **重力任务：** 使用 GRACE 等技术，通过测量地球引力场的变化来监测大规模冰体。

通过“水当量”将这些测量结果标准化，使研究人员能够在不同的冰雪密度之间保持一致性，从而更清晰地描绘全球环境变化的图景。

---

## 5. AmigaDOS 开发者 Tim King 逝世

**原文标题**: Tim King, AmigaDOS developer, has died

**原文链接**: [https://amiga-news.de/en/news/AN-2026-08-00070-EN.html](https://amiga-news.de/en/news/AN-2026-08-00070-EN.html)

计算机科学及 Amiga 电脑历史上的关键人物蒂姆·金博士（Dr. Tim King）于 2026 年 7 月下旬逝世。

金于 1979 年在剑桥大学获得博士学位，并在那里开发了 Tripos，这是一个使用 BCPL 编写的抢占式多任务操作系统。1984 年，他加入 MetaComCo 公司，期间 Tripos 被改编为 Amiga 电脑的基础操作系统 AmigaDOS。

在结束 Amiga 的工作后，金于 1986 年创立了 Perihelion 公司，专注于并行处理和跨处理机（transputer）技术。此后，他还创办了互联网服务提供商 UK Online。金因其对操作系统演进做出的重大技术贡献，以及他在 Amiga 社区留下的深远遗产而为人所铭记。

---

## 6. 有人正伪装成 ClaudeBot 等 AI 机器人进行大规模漏洞扫描

**原文标题**: Someone is running mass vulnerability scans, spoofing AI bots like ClaudeBot

**原文链接**: [https://knownagents.com/insights](https://knownagents.com/insights)

**智能体网络指数 (Agentic Web Index)** 揭示了互联网流量的重大转变：包括 AI 智能体、爬虫和抓取工具在内的机器流量现在已占到**所有网页访问量的 35%**。尽管整体机器人流量略有下降，但“智能体化”（与 AI 相关的机器人活动）激增了 11%，表明互联网正日益针对人工智能进行优化，并越来越多地被其消耗。

报告的核心发现包括：

*   **机器人合规性：** 尽管自动化流量有所上升，但机器人表现得高度自律，在 **98.5%** 的情况下都遵循 `robots.txt` 协议。
*   **主导厂商：** 少数几家主要运营商控制了绝大部分 AI 流量。**OpenAI** 在“AI 获取”（用于 RAG 的实时数据检索）领域占据主导地位，市场份额达 86.4%。**Anthropic 的 ClaudeBot** 则在“AI 抓取”（用于模型训练的数据收集）方面以 27% 的份额领跑，Meta 和亚马逊紧随其后。
*   **搜索与 SEO：** 传统搜索引擎爬虫（Googlebot、bingbot）和 SEO 工具（Ahrefs）仍占据机器人总流量的最大份额。然而，华为的 **PetalBot**、Amzn-SearchBot 和 Applebot 等 AI 专用搜索索引器正在开辟重要的细分市场。
*   **用户行为：** 目前，自主浏览网页以替人类完成任务的 AI 智能体平均会话时长为 1 分钟，每次会话访问约 7.6 个页面。
*   **引流趋势：** 尽管 AI 机器人消耗了海量数据，但目前它们为网站引回的人类流量极少；AI 聊天带来的引流仅占人类访问量的 **0.1%**。

总之，数据描绘了一个不断演变的数字图景：AI 公司正积极地抓取并索引内容，以为下一代助手和搜索引擎提供动力，即便这些工具带来的直接人类点击量目前仍微乎其微。

---

## 7. SpaceXAI 的 Grok 4.6 在人工分析智能指数中获 61 分

**原文标题**: SpaceXAI's Grok 4.6 Scores 61 on the Artificial Analysis Intelligence Index

**原文链接**: [https://artificialanalysis.ai/articles/grok-4-6-benchmarks-and-analysis](https://artificialanalysis.ai/articles/grok-4-6-benchmarks-and-analysis)

SpaceXAI 发布了 Grok 4.6，在人工智能分析智能指数（Artificial Analysis Intelligence Index）中取得了 61 分。这一得分较其前代产品提升了 5 分，使该模型与 GPT-5.6 Sol 共同跻身行业前沿，仅次于 Anthropic 的 Claude Opus 5 和 Fable 5。

本次发布的主要亮点包括：

*   **卓越的智能体能力：** Grok 4.6 在现实世界的智能体任务中表现优异，在 GDPval-AA v2 上获得了 1753 Elo 评分。它在多项专业基准测试中名列前茅，包括 $\tau^3$-Banking (50.7%) 和 Terminal-Bench v2.1 (88.4%)，证明了其在多轮工具调用和软件任务处理方面的高效性。
*   **成本效益：** 颠覆了前沿模型市场，SpaceXAI 维持了 Grok 4.5 的定价：每 100 万输入 token 为 2 美元，每 100 万输出 token 为 6 美元。这比 OpenAI 和 Anthropic 的同类模型便宜 60% 以上。凭借每项任务 0.84 美元的平均成本，Grok 4.6 处于“智能 vs. 成本”的帕累托前沿（Pareto frontier）。
*   **运营效率：** 在长周期任务（AA-Briefcase）中，该模型展现了显著的 token 效率。它仅需约 53 轮对话及 5 亿（0.5B）输入 token 即可完成任务——在达成相似效果的情况下，其所需的轮数仅为 Claude Opus 5 的一半，输入 token 消耗仅为后者的 25%。
*   **技术规格：** 该模型保留了 500k 的上下文窗口。虽然基础定价保持不变，但缓存命中（cache hits）的成本略微上涨至每 100 万 token 0.5 美元。

总体而言，Grok 4.6 将 SpaceXAI 定位为“轮次效率型”智能的领导者，以主要竞争对手极小比例的成本提供了行业顶尖的性能。

---

## 8. Reflex (YC W23) 正在招聘增长与 GTM 岗位

**原文标题**: Reflex (YC W23) Is hiring Growth and GTM Roles

**原文链接**: [https://www.ycombinator.com/companies/reflex/jobs/71x5GFb-growth-engineer](https://www.ycombinator.com/companies/reflex/jobs/71x5GFb-growth-engineer)

生成摘要时出错

---

## 9. Why Tiny JPEGs Look Different in Chrome

**原文标题**: Why Tiny JPEGs Look Different in Chrome

**原文链接**: [https://guillaumetech.github.io/posts/jpg-scaling-chrome/](https://guillaumetech.github.io/posts/jpg-scaling-chrome/)

This article explores why small JPEG images, such as icons, often appear "thicker" or distorted in Chrome compared to other browsers like Firefox. The author discovered that this visual discrepancy is not a bug, but rather a performance optimization within Chrome’s rendering engine, Skia, and its JPEG library, libjpeg-turbo.

The core of the issue lies in how JPEGs are decoded. Traditionally, a browser would fully decompress a large image into memory before scaling it down—a process that is memory-intensive and wasteful for tiny display sizes. To save resources, Chrome utilizes **partial IDCT (Inverse Discrete Cosine Transform) scaling**.

JPEGs store data in 8x8 pixel blocks converted into the frequency domain. In this format, low-frequency coefficients represent flat colors and basic shapes, while high-frequency coefficients capture fine details and sharp edges. When an image is scaled down significantly, most high-frequency information is naturally lost. Chrome takes advantage of this by skipping the high-frequency coefficients during the decoding process. It decodes the image at a fraction of its size (typically a denominator of eight) using only the low-frequency data, then performs a final downsampling to the desired dimensions.

While this optimization makes rendering faster and significantly reduces memory consumption, it results in the loss of edge softening and subtle gradients. This causes small graphics to look blockier or "thicker." The author concludes that because JPEGs are designed specifically for photographs—as the name **Joint Photographic Experts Group** suggests—they are ill-suited for icons. For small UI elements and logos, SVGs are recommended to ensure consistent rendering across all platforms.

---

## 10. Wednesday, August 12: GitHub, Incident with Pull Requests and Issues

**原文标题**: Wednesday, August 12: GitHub, Incident with Pull Requests and Issues

**原文链接**: [https://www.githubstatus.com/incidents/76t89hbfb09h](https://www.githubstatus.com/incidents/76t89hbfb09h)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 2 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 3 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 4 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 5 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 6 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 7 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 8 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 9 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 10 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 11 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 12 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 13 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 14 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 15 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 16 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 17 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 18 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 19 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 20 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 21 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 22 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 23 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 24 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 25 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 26 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 27 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 28 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 29 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 30 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 31 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 32 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 33 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 34 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 35 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 36 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 37 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 38 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 39 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 40 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 41 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 42 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 43 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 44 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 45 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 46 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 47 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 48 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 49 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 50 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 51 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 52 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 53 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 54 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 55 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 56 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 57 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 58 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 59 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 60 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 61 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 62 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 63 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 64 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 65 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 66 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 67 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 68 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 69 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 70 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 71 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 72 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 73 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 74 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 75 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 76 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 77 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 78 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 79 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 80 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 81 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 82 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 83 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 84 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 85 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 86 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 87 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 88 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 89 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 90 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 91 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 92 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 93 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 94 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 95 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 96 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 97 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 98 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 99 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 100 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 101 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 102 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 103 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 104 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 105 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 106 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 107 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 108 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 109 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 110 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 111 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 112 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 113 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 114 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 115 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 116 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 117 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 118 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 119 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 120 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 121 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 122 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 123 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 124 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 125 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 126 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 127 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 128 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 129 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 130 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 131 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 132 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 133 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 134 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 135 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 136 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 137 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 138 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 139 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 140 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 141 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 142 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 143 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 144 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 145 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 146 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 147 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 148 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 149 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 150 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 151 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 152 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 153 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 154 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 155 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 156 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 157 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 158 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 159 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 160 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 161 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 162 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 163 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 164 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 165 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 166 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 167 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 168 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 169 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 170 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 171 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 172 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 173 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 174 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 175 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 176 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 177 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 178 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 179 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 180 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 181 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 182 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 183 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 184 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 185 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 186 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 187 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 188 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 189 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 190 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 191 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 192 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 193 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 194 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 195 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 196 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 197 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 198 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 199 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 200 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 201 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 202 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 203 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 204 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 205 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 206 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 207 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 208 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 209 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 210 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 211 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 212 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 213 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 214 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 215 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 216 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 217 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 218 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 219 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 220 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 221 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 222 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 223 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 224 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 225 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 226 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 227 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 228 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 229 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 230 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 231 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 232 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 233 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 234 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 235 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 236 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 237 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 238 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 239 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 240 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 241 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 242 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 243 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 244 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 245 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 246 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 247 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 248 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 249 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 250 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 251 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 252 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 253 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 254 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 255 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 256 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 257 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 258 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 259 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 260 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 261 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 262 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 263 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 264 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 265 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 266 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 267 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 268 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 269 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 270 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 271 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 272 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 273 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 274 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 275 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 276 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 277 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 278 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 279 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 280 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 281 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 282 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 283 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 284 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 285 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 286 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 287 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 288 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 289 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 290 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 291 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 292 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 293 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 294 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 295 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 296 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 297 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 298 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 299 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 300 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 301 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 302 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 303 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 304 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 305 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 306 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 307 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 308 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 309 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 310 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 311 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 312 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 313 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 314 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 315 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 316 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 317 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 318 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 319 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 320 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 321 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 322 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 323 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 324 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 325 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 326 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 327 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 328 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 329 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 330 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 331 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 332 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 333 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 334 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 335 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 336 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 337 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 338 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 339 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 340 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 341 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 342 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 343 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 344 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 345 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 346 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 347 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 348 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 349 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 350 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 351 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 352 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 353 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 354 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 355 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 356 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 357 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 358 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 359 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 360 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 361 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 362 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 363 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 364 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 365 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 366 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 367 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 368 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 369 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 370 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 371 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 372 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 373 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 374 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 375 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 376 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 377 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 378 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 379 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 380 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 381 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 382 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 383 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 384 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 385 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 386 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 387 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 388 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 389 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 390 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 391 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 392 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 393 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 394 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 395 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 396 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 397 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 398 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 399 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 400 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 401 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 402 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 403 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 404 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 405 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 406 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 407 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 408 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 409 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 410 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 411 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 412 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 413 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 414 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 415 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 416 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 417 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 418 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 419 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 420 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 421 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 422 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 423 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 424 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 425 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 426 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 427 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 428 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 429 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 430 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 431 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 432 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 433 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 434 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 435 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 436 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 437 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 438 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 439 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 440 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 441 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 442 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 443 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 444 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 445 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 446 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 447 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 448 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 449 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 450 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 451 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 452 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 453 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 454 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 455 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 456 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 457 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 458 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 459 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 460 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 461 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 462 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 463 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 464 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 465 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 466 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 467 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 468 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 469 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 470 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 471 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 472 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 473 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 474 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 475 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 476 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 477 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 478 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 479 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 480 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 481 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 482 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 483 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 484 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 485 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 486 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 487 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 488 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 489 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 490 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 491 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 492 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 493 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 494 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 495 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 496 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 497 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 498 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 499 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 500 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 501 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 502 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 503 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 504 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 505 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 506 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 507 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 508 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 509 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
