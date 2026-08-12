# Hacker News 热门文章摘要 (2026-08-12)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. HTML over WebSockets: real-time SPAs with barely any JavaScript

**原文标题**: HTML over WebSockets: real-time SPAs with barely any JavaScript

**原文链接**: [https://en.andros.dev/blog/ef4968f5/html-over-websockets-real-time-spas-with-barely-any-javascript/](https://en.andros.dev/blog/ef4968f5/html-over-websockets-real-time-spas-with-barely-any-javascript/)

生成摘要时出错

---

## 12. 车牌识别器搜查应需搜查令

**原文标题**: License plate reader searches should require a warrant

**原文链接**: [https://andrewpwheeler.com/2026/08/12/license-plate-reader-searches-should-require-a-warrant/](https://andrewpwheeler.com/2026/08/12/license-plate-reader-searches-should-require-a-warrant/)

生成摘要时出错

---

## 13. AI is removing the middle class of software engineering

**原文标题**: AI is removing the middle class of software engineering

**原文链接**: [https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html](https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html)

生成摘要时出错

---

## 14. Pixel Watch 5

**原文标题**: Pixel Watch 5

**原文链接**: [https://blog.google/products-and-platforms/devices/pixel/pixel-watch-5/](https://blog.google/products-and-platforms/devices/pixel/pixel-watch-5/)

生成摘要时出错

---

## 15. Qwen3.8-2.4T

**原文标题**: Qwen3.8-2.4T

**原文链接**: [https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B-FP8](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B-FP8)

生成摘要时出错

---

## 16. Bike Bureau: Report Bike Lane Obstructions

**原文标题**: Bike Bureau: Report Bike Lane Obstructions

**原文链接**: [https://loudbicycle.com/bb](https://loudbicycle.com/bb)

生成摘要时出错

---

## 17. Qwen/Qwen3.8-2.4T-A95B

**原文标题**: Qwen/Qwen3.8-2.4T-A95B

**原文链接**: [https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)

生成摘要时出错

---

## 18. What sort of maths are LLMs good at?

**原文标题**: What sort of maths are LLMs good at?

**原文链接**: [https://gowers.wordpress.com/2026/08/12/what-sort-of-maths-are-llms-good-at/](https://gowers.wordpress.com/2026/08/12/what-sort-of-maths-are-llms-good-at/)

生成摘要时出错

---

## 19. We just raised $400M in Series C

**原文标题**: We just raised $400M in Series C

**原文链接**: [https://lovable.dev/blog/series-c](https://lovable.dev/blog/series-c)

生成摘要时出错

---

## 20. Shade Map

**原文标题**: Shade Map

**原文链接**: [https://shademap.app](https://shademap.app)

生成摘要时出错

---

## 21. The Bit Player: My Father with Steve Zissou

**原文标题**: The Bit Player: My Father with Steve Zissou

**原文链接**: [https://www.theparisreview.org/blog/2026/07/27/the-bit-player-my-father-with-steve-zissou/](https://www.theparisreview.org/blog/2026/07/27/the-bit-player-my-father-with-steve-zissou/)

生成摘要时出错

---

## 22. Show HN: Woxi - Open-source Mathematica / Wolfram Language reimplementation

**原文标题**: Show HN: Woxi - Open-source Mathematica / Wolfram Language reimplementation

**原文链接**: [https://woxi.ad-si.com](https://woxi.ad-si.com)

生成摘要时出错

---

## 23. Hax – a minimalist, terminal-native coding agent written in C

**原文标题**: Hax – a minimalist, terminal-native coding agent written in C

**原文链接**: [https://usehax.dev/](https://usehax.dev/)

生成摘要时出错

---

## 24. Felix and I

**原文标题**: Felix and I

**原文链接**: [https://jacobfilipp.com/felix/](https://jacobfilipp.com/felix/)

生成摘要时出错

---

## 25. Delphi 13 Community Edition Is Now Available

**原文标题**: Delphi 13 Community Edition Is Now Available

**原文链接**: [https://blogs.embarcadero.com/delphi-13-community-edition-is-now-available/](https://blogs.embarcadero.com/delphi-13-community-edition-is-now-available/)

生成摘要时出错

---

## 26. Automatic1111 for Apple metal, 40% speed up sd1.5

**原文标题**: Automatic1111 for Apple metal, 40% speed up sd1.5

**原文链接**: [https://therad.ninja/from-8-10-seconds-to-3-7-teaching-automatic1111-to-speak-metal-on-an-m3-pro/](https://therad.ninja/from-8-10-seconds-to-3-7-teaching-automatic1111-to-speak-metal-on-an-m3-pro/)

生成摘要时出错

---

## 27. My Agent Setup

**原文标题**: My Agent Setup

**原文链接**: [https://chad.cm/posts/2026-8-11-my-agent-setup](https://chad.cm/posts/2026-8-11-my-agent-setup)

生成摘要时出错

---

## 28. High-Res Photo Shows Sand-Capped Butte Rising from Mars Plain of Polygons

**原文标题**: High-Res Photo Shows Sand-Capped Butte Rising from Mars Plain of Polygons

**原文链接**: [https://petapixel.com/2026/08/04/amazing-high-res-photo-shows-a-butte-rising-from-mars/](https://petapixel.com/2026/08/04/amazing-high-res-photo-shows-a-butte-rising-from-mars/)

生成摘要时出错

---

## 29. Solving the Shortest Vector Problem in $2^{0.6039n}$ Time via Mid-Point Hessian

**原文标题**: Solving the Shortest Vector Problem in $2^{0.6039n}$ Time via Mid-Point Hessian

**原文链接**: [https://arxiv.org/abs/2608.02478](https://arxiv.org/abs/2608.02478)

生成摘要时出错

---

## 30. Bigos (Polish Hunter's Stew) Recipe Builder

**原文标题**: Bigos (Polish Hunter's Stew) Recipe Builder

**原文链接**: [https://chefsbinge.com/bigos-recipe-builder/](https://chefsbinge.com/bigos-recipe-builder/)

生成摘要时出错

---

## 31. The Ultimate Horse

**原文标题**: The Ultimate Horse

**原文链接**: [https://worksinprogress.co/issue/the-ultimate-horse/](https://worksinprogress.co/issue/the-ultimate-horse/)

生成摘要时出错

---

## 32. Launch HN: Discovered Materials (YC P26) – AI agents to discover new materials

**原文标题**: Launch HN: Discovered Materials (YC P26) – AI agents to discover new materials

**原文链接**: [https://discoveredmaterials.com/research/](https://discoveredmaterials.com/research/)

生成摘要时出错

---

## 33. ArenaAllocators don't play nicely with ArrayLists

**原文标题**: ArenaAllocators don't play nicely with ArrayLists

**原文链接**: [https://www.openmymind.net/Arena-Allocators-and-ArrayLists/](https://www.openmymind.net/Arena-Allocators-and-ArrayLists/)

生成摘要时出错

---

## 34. The hardest working font in Manhattan (2025)

**原文标题**: The hardest working font in Manhattan (2025)

**原文链接**: [https://aresluna.org/the-hardest-working-font-in-manhattan/](https://aresluna.org/the-hardest-working-font-in-manhattan/)

生成摘要时出错

---

## 35. Commodore 8-Bit 5¼" Disk Images

**原文标题**: Commodore 8-Bit 5¼" Disk Images

**原文链接**: [https://www.masswerk.at/nowgobang/2026/commodore-disk-images](https://www.masswerk.at/nowgobang/2026/commodore-disk-images)

生成摘要时出错

---

## 36. uBlock Origin Is Giving Up the Fight to Keep Ads Off Facebook

**原文标题**: uBlock Origin Is Giving Up the Fight to Keep Ads Off Facebook

**原文链接**: [https://digitalescapetools.com/2026/08/ublock-origin-stops-chasing-facebook-ads.html](https://digitalescapetools.com/2026/08/ublock-origin-stops-chasing-facebook-ads.html)

生成摘要时出错

---

## 37. Worms: The Future of Yesterday's Worms Today

**原文标题**: Worms: The Future of Yesterday's Worms Today

**原文链接**: [https://worm.net/](https://worm.net/)

生成摘要时出错

---

## 38. DeepSeek-V4-Pro-0813 Publish

**原文标题**: DeepSeek-V4-Pro-0813 Publish

**原文链接**: [https://api-docs.deepseek.com/](https://api-docs.deepseek.com/)

生成摘要时出错

---

## 39. Controversial creators are benefiting from monetization programs run by Meta

**原文标题**: Controversial creators are benefiting from monetization programs run by Meta

**原文链接**: [https://www.abc.net.au/news/2026-08-06/ragebait-how-facebook-is-paying-controversial-creators/106940696](https://www.abc.net.au/news/2026-08-06/ragebait-how-facebook-is-paying-controversial-creators/106940696)

生成摘要时出错

---

## 40. German advocacy group lodges criminal complaint over Meta AI glasses

**原文标题**: German advocacy group lodges criminal complaint over Meta AI glasses

**原文链接**: [https://www.reuters.com/legal/government/german-advocacy-group-lodges-criminal-complaint-over-meta-ai-glasses-2026-08-12/](https://www.reuters.com/legal/government/german-advocacy-group-lodges-criminal-complaint-over-meta-ai-glasses-2026-08-12/)

生成摘要时出错

---

## 41. U of Michigan drops first-semester grades to ‘curb mental health crisis’

**原文标题**: U of Michigan drops first-semester grades to ‘curb mental health crisis’

**原文链接**: [https://www.wsj.com/us-news/education/university-of-michigan-grades-mental-health-1a5701d4](https://www.wsj.com/us-news/education/university-of-michigan-grades-mental-health-1a5701d4)

生成摘要时出错

---

## 42. Show HN: KidScreen, a finite YouTube shelf chosen by parents

**原文标题**: Show HN: KidScreen, a finite YouTube shelf chosen by parents

**原文链接**: [https://kidscreen.app](https://kidscreen.app)

生成摘要时出错

---

## 43. Fail Faster

**原文标题**: Fail Faster

**原文链接**: [https://derickrethans.nl/fail-faster.html](https://derickrethans.nl/fail-faster.html)

生成摘要时出错

---

## 44. Decrypting my Flume water monitor's MQTT traffic with a passive relay

**原文标题**: Decrypting my Flume water monitor's MQTT traffic with a passive relay

**原文链接**: [https://lithostech.com/2026/08/decrypting-flume-water-monitor-traffic/](https://lithostech.com/2026/08/decrypting-flume-water-monitor-traffic/)

生成摘要时出错

---

## 45. DosTips, Windows scripting knowledge trove, scraped to death

**原文标题**: DosTips, Windows scripting knowledge trove, scraped to death

**原文链接**: [https://www.dostips.com/](https://www.dostips.com/)

生成摘要时出错

---

## 46. US hires over 2k video gamers as air traffic controllers

**原文标题**: US hires over 2k video gamers as air traffic controllers

**原文链接**: [https://www.cbsnews.com/news/video-gamer-air-traffic-controllers-faa-recruitment-sean-duffy/](https://www.cbsnews.com/news/video-gamer-air-traffic-controllers-faa-recruitment-sean-duffy/)

生成摘要时出错

---

## 47. Grok 4.6 (High) Intelligence, Performance and Price Analysis

**原文标题**: Grok 4.6 (High) Intelligence, Performance and Price Analysis

**原文链接**: [https://artificialanalysis.ai/models/grok-4-6](https://artificialanalysis.ai/models/grok-4-6)

生成摘要时出错

---

## 48. FDA Admitted in Print That Nothing It Knows of Will Wash Cyclospora Off Lettuce

**原文标题**: FDA Admitted in Print That Nothing It Knows of Will Wash Cyclospora Off Lettuce

**原文链接**: [https://www.marlerblog.com/case-news/fda-just-admitted-in-print-that-nothing-it-knows-of-will-wash-cyclospora-off-your-lettuce-then-it-never-told-anyone-to-test-the-water-for-it/](https://www.marlerblog.com/case-news/fda-just-admitted-in-print-that-nothing-it-knows-of-will-wash-cyclospora-off-your-lettuce-then-it-never-told-anyone-to-test-the-water-for-it/)

生成摘要时出错

---

## 49. Show HN: /show-me：用于紧凑视觉呈现的智能体技能

**原文标题**: Show HN: /show-me: agent skill for compact visual representations

**原文链接**: [https://www.humanlayer.com/blog/show-me-skill](https://www.humanlayer.com/blog/show-me-skill)

生成摘要时出错

---

## 50. SpaceXAI: Grok 4.6

**原文标题**: SpaceXAI: Grok 4.6

**原文链接**: [https://openrouter.ai/x-ai/grok-4.6](https://openrouter.ai/x-ai/grok-4.6)

生成摘要时出错

---

## 51. Introducing Grok 4.6

**原文标题**: Introducing Grok 4.6

**原文链接**: [https://cursor.com/blog/grok-4-6](https://cursor.com/blog/grok-4-6)

生成摘要时出错

---

## 52. USS Abraham Lincoln sailors tried to jump overboard amid extended deployment

**原文标题**: USS Abraham Lincoln sailors tried to jump overboard amid extended deployment

**原文链接**: [https://www.theguardian.com/us-news/2026/aug/12/uss-abraham-lincoln-overboard-extended-deployment](https://www.theguardian.com/us-news/2026/aug/12/uss-abraham-lincoln-overboard-extended-deployment)

生成摘要时出错

---

## 53. CFTC declares market emergency, orders Kalshi to continue to operate in New York

**原文标题**: CFTC declares market emergency, orders Kalshi to continue to operate in New York

**原文链接**: [https://www.cftc.gov/PressRoom/PressReleases/9281-26](https://www.cftc.gov/PressRoom/PressReleases/9281-26)

生成摘要时出错

---

## 54. Bluesky's active user base is shrinking as its focus expands beyond the app

**原文标题**: Bluesky's active user base is shrinking as its focus expands beyond the app

**原文链接**: [https://techcrunch.com/2026/08/11/blueskys-active-user-base-is-shrinking-as-its-focus-expands-beyond-the-app/](https://techcrunch.com/2026/08/11/blueskys-active-user-base-is-shrinking-as-its-focus-expands-beyond-the-app/)

生成摘要时出错

---

## 55. The Human Is the Loop

**原文标题**: The Human Is the Loop

**原文链接**: [https://brentfitzgerald.com/posts/the-human-is-the-loop/](https://brentfitzgerald.com/posts/the-human-is-the-loop/)

生成摘要时出错

---

## 56. Netflix Has Peaked

**原文标题**: Netflix Has Peaked

**原文链接**: [https://daringfireball.net/linked/2026/08/11/netflix-has-peaked](https://daringfireball.net/linked/2026/08/11/netflix-has-peaked)

生成摘要时出错

---

## 57. I built a jellyfish laboratory in my backyard [video]

**原文标题**: I built a jellyfish laboratory in my backyard [video]

**原文链接**: [https://www.youtube.com/watch?v=MILwxfQBm6Q](https://www.youtube.com/watch?v=MILwxfQBm6Q)

生成摘要时出错

---

## 58. Show HN: Seisin – a desktop app that turns your job search into analytics

**原文标题**: Show HN: Seisin – a desktop app that turns your job search into analytics

**原文链接**: [https://getseisin.com](https://getseisin.com)

生成摘要时出错

---

## 59. Bb: The IDE that builds itself

**原文标题**: Bb: The IDE that builds itself

**原文链接**: [https://getbb.app/](https://getbb.app/)

生成摘要时出错

---

## 60. Google launches Pixel 11 Pro Fold

**原文标题**: Google launches Pixel 11 Pro Fold

**原文链接**: [https://blog.google/products-and-platforms/devices/pixel/pixel-11-pro-fold/](https://blog.google/products-and-platforms/devices/pixel/pixel-11-pro-fold/)

生成摘要时出错

---

## 61. Aaron Rodgers secretly funded his town's Flock-style cameras

**原文标题**: Aaron Rodgers secretly funded his town's Flock-style cameras

**原文链接**: [https://www.foiaball.com/p/aaron-rodgers-secretly-bought-police-alpr-cameras](https://www.foiaball.com/p/aaron-rodgers-secretly-bought-police-alpr-cameras)

生成摘要时出错

---

## 62. llama.cpp

**原文标题**: llama.cpp

**原文链接**: [https://llama.app](https://llama.app)

生成摘要时出错

---

## 63. A shell exclamation mark is not for yelling. Be lazy

**原文标题**: A shell exclamation mark is not for yelling. Be lazy

**原文链接**: [https://refp.se/articles/your-shell-and-the-lazy-exclamation-mark](https://refp.se/articles/your-shell-and-the-lazy-exclamation-mark)

生成摘要时出错

---

## 64. European scientists developed a tactile sensor capable of 100 μm resolution

**原文标题**: European scientists developed a tactile sensor capable of 100 μm resolution

**原文链接**: [https://spectrum.ieee.org/robot-finger](https://spectrum.ieee.org/robot-finger)

生成摘要时出错

---

## 65. Electricity Pricing in the Age of AI

**原文标题**: Electricity Pricing in the Age of AI

**原文链接**: [https://power2026.ai/](https://power2026.ai/)

生成摘要时出错

---

## 66. A BSON symbol namespace bypasses MongoDB's authorization check (CVE-2026-18690)

**原文标题**: A BSON symbol namespace bypasses MongoDB's authorization check (CVE-2026-18690)

**原文链接**: [https://hellorecon.com/blog/cve-2026-18690-mongodb-symbol-type-authz-bypass](https://hellorecon.com/blog/cve-2026-18690-mongodb-symbol-type-authz-bypass)

生成摘要时出错

---

## 67. See what solar eclipses would look like from other planets

**原文标题**: See what solar eclipses would look like from other planets

**原文链接**: [https://benmccarthy.com.au/p/eclipses](https://benmccarthy.com.au/p/eclipses)

生成摘要时出错

---

## 68. Show HN: Smarter Shell History for Zsh

**原文标题**: Show HN: Smarter Shell History for Zsh

**原文链接**: [https://github.com/overflowy/zhist](https://github.com/overflowy/zhist)

生成摘要时出错

---

## 69. Show HN: Meteor shower, planet alignment, eclipse kit

**原文标题**: Show HN: Meteor shower, planet alignment, eclipse kit

**原文链接**: [https://lifesprites.com/share/0ACA25](https://lifesprites.com/share/0ACA25)

生成摘要时出错

---

## 70. The little-known winstart.bat batch file

**原文标题**: The little-known winstart.bat batch file

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20260811-00/?p=112605](https://devblogs.microsoft.com/oldnewthing/20260811-00/?p=112605)

生成摘要时出错

---

## 71. Compression is prediction

**原文标题**: Compression is prediction

**原文链接**: [https://ngrok.com/blog/compression-is-prediction](https://ngrok.com/blog/compression-is-prediction)

生成摘要时出错

---

## 72. Signal adds new security feature to thwart man-in-the-middle attacks

**原文标题**: Signal adds new security feature to thwart man-in-the-middle attacks

**原文链接**: [https://www.bleepingcomputer.com/news/security/signal-adds-new-security-feature-to-thwart-man-in-the-middle-attacks/](https://www.bleepingcomputer.com/news/security/signal-adds-new-security-feature-to-thwart-man-in-the-middle-attacks/)

生成摘要时出错

---

## 73. Lazarus hackers exploited Windows zero-day to target defense firms

**原文标题**: Lazarus hackers exploited Windows zero-day to target defense firms

**原文链接**: [https://www.bleepingcomputer.com/news/security/lazarus-hackers-exploited-windows-zero-day-to-target-defense-firms/](https://www.bleepingcomputer.com/news/security/lazarus-hackers-exploited-windows-zero-day-to-target-defense-firms/)

生成摘要时出错

---

## 74. The lifesaving secret hidden inside a horseshoe crab's blue blood

**原文标题**: The lifesaving secret hidden inside a horseshoe crab's blue blood

**原文链接**: [https://whdh.com/news/the-lifesaving-secret-hidden-inside-a-horseshoe-crabs-blue-blood-and-the-race-to-protect-the-species/](https://whdh.com/news/the-lifesaving-secret-hidden-inside-a-horseshoe-crabs-blue-blood-and-the-race-to-protect-the-species/)

生成摘要时出错

---

## 75. The Neurosurgery Resident Who Proved Crouzeix's Conjecture [pdf]

**原文标题**: The Neurosurgery Resident Who Proved Crouzeix's Conjecture [pdf]

**原文链接**: [https://alextownsend.net/essays/SIAMNews_CrouzeixConjecture.pdf](https://alextownsend.net/essays/SIAMNews_CrouzeixConjecture.pdf)

生成摘要时出错

---

## 76. 92 percent of US adults are not going to the doctor – too expensive

**原文标题**: 92 percent of US adults are not going to the doctor – too expensive

**原文链接**: [https://www.independent.co.uk/us/money/us-medical-costs-doctors-health-insurance-b3026479.html](https://www.independent.co.uk/us/money/us-medical-costs-doctors-health-insurance-b3026479.html)

生成摘要时出错

---

## 77. Turbo Pascal on CP/M, MSX-DOS and MS-DOS – Pascal for Small Machines

**原文标题**: Turbo Pascal on CP/M, MSX-DOS and MS-DOS – Pascal for Small Machines

**原文链接**: [http://pascal.hansotten.com/delphi/turbo-pascal-on-cpm-msx-dos-and-ms-dos/](http://pascal.hansotten.com/delphi/turbo-pascal-on-cpm-msx-dos-and-ms-dos/)

生成摘要时出错

---

## 78. WorldClaw Agentic 3D open-world generation at scale

**原文标题**: WorldClaw Agentic 3D open-world generation at scale

**原文链接**: [https://tencent-hunyuan.github.io/Hunyuan3D-WorldClaw/](https://tencent-hunyuan.github.io/Hunyuan3D-WorldClaw/)

生成摘要时出错

---

## 79. Retire the Abstractions

**原文标题**: Retire the Abstractions

**原文链接**: [https://hazyresearch.stanford.edu/blog/2026-08-05-retire-the-abstractions](https://hazyresearch.stanford.edu/blog/2026-08-05-retire-the-abstractions)

生成摘要时出错

---

## 80. OpenAI’s head of ethics leaves less than a year after joining

**原文标题**: OpenAI’s head of ethics leaves less than a year after joining

**原文链接**: [https://www.ft.com/content/e49dfb75-f841-4466-a577-f7aaff8779a0](https://www.ft.com/content/e49dfb75-f841-4466-a577-f7aaff8779a0)

生成摘要时出错

---

## 81. Computer scientists today are in the position of economists in the early 2000s

**原文标题**: Computer scientists today are in the position of economists in the early 2000s

**原文链接**: [https://statmodeling.stat.columbia.edu/2026/08/11/computer-scientists-today-are-like-economists-in-the-early-2000s-and-freudian-psychiatrists-in-the-1950s/](https://statmodeling.stat.columbia.edu/2026/08/11/computer-scientists-today-are-like-economists-in-the-early-2000s-and-freudian-psychiatrists-in-the-1950s/)

生成摘要时出错

---

## 82. The Government Is Monitoring Anti-Flock TikTok and Instagram Accounts

**原文标题**: The Government Is Monitoring Anti-Flock TikTok and Instagram Accounts

**原文链接**: [https://www.404media.co/the-government-is-monitoring-anti-flock-tiktok-and-instagram-accounts/](https://www.404media.co/the-government-is-monitoring-anti-flock-tiktok-and-instagram-accounts/)

生成摘要时出错

---

## 83. How hot has the European summer been? 22 cities of 42 beat records

**原文标题**: How hot has the European summer been? 22 cities of 42 beat records

**原文链接**: [https://thelongswell.com/heat/](https://thelongswell.com/heat/)

生成摘要时出错

---

## 84. Stealing Reasoning Traces from Proprietary LLM APIs

**原文标题**: Stealing Reasoning Traces from Proprietary LLM APIs

**原文链接**: [https://stolen-thoughts.com/](https://stolen-thoughts.com/)

生成摘要时出错

---

## 85. Putting away the tools of his trade for good

**原文标题**: Putting away the tools of his trade for good

**原文链接**: [https://www.ahwatukee.com/business/putting-away-the-tools-of-his-trade-for-good/article_14b2a9b1-cb5b-45db-be57-d11b29606f70.html](https://www.ahwatukee.com/business/putting-away-the-tools-of-his-trade-for-good/article_14b2a9b1-cb5b-45db-be57-d11b29606f70.html)

生成摘要时出错

---

## 86. Go is an ideal language for AI-assisted software engineering

**原文标题**: Go is an ideal language for AI-assisted software engineering

**原文链接**: [https://developers.googleblog.com/why-go-is-an-ideal-language-for-ai-assisted-software-engineering/](https://developers.googleblog.com/why-go-is-an-ideal-language-for-ai-assisted-software-engineering/)

生成摘要时出错

---

## 87. Unearthing a 31 year old Easter egg in Ecco the Dolphin

**原文标题**: Unearthing a 31 year old Easter egg in Ecco the Dolphin

**原文链接**: [https://32bits.substack.com/p/under-the-microscope-ecco-the-dolphin-98c](https://32bits.substack.com/p/under-the-microscope-ecco-the-dolphin-98c)

生成摘要时出错

---

## 88. Show HN: Tamron Lens Utility Alternative on Linux

**原文标题**: Show HN: Tamron Lens Utility Alternative on Linux

**原文链接**: [https://github.com/yikerman/tamron-lens-control](https://github.com/yikerman/tamron-lens-control)

生成摘要时出错

---

## 89. Grok 4.6

**原文标题**: Grok 4.6

**原文链接**: [https://x.ai/news/grok-4-6](https://x.ai/news/grok-4-6)

生成摘要时出错

---

## 90. Jellyfish-hit French nuclear plant shuts down three reactors

**原文标题**: Jellyfish-hit French nuclear plant shuts down three reactors

**原文链接**: [https://www.reuters.com/business/energy/jellyfish-hit-french-nuclear-plant-shuts-down-three-reactors-2026-08-11/](https://www.reuters.com/business/energy/jellyfish-hit-french-nuclear-plant-shuts-down-three-reactors-2026-08-11/)

生成摘要时出错

---

## 91. Mojo 1.0

**原文标题**: Mojo 1.0

**原文链接**: [https://www.modular.com/blog/modular-26-5-mojo-1-0-is-here](https://www.modular.com/blog/modular-26-5-mojo-1-0-is-here)

生成摘要时出错

---

## 92. Show HN: Line9 – A Mermaid rendering engine with its own layout

**原文标题**: Show HN: Line9 – A Mermaid rendering engine with its own layout

**原文链接**: [https://line9.ai/diagram](https://line9.ai/diagram)

生成摘要时出错

---

## 93. Nvidia Nemotron 3.5 Lightning and NeMo Switchyard

**原文标题**: Nvidia Nemotron 3.5 Lightning and NeMo Switchyard

**原文链接**: [https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/](https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/)

生成摘要时出错

---

## 94. Show HN: Git-knife – Edit commit messages, authors, and dates like a spreadsheet

**原文标题**: Show HN: Git-knife – Edit commit messages, authors, and dates like a spreadsheet

**原文链接**: [https://github.com/TheRealYT/git-knife](https://github.com/TheRealYT/git-knife)

生成摘要时出错

---

## 95. CSS properties you should know for better text designs

**原文标题**: CSS properties you should know for better text designs

**原文链接**: [https://master.dev/blog/typographic-css-tricks/](https://master.dev/blog/typographic-css-tricks/)

生成摘要时出错

---

## 96. Manus will return to operating as an independent company

**原文标题**: Manus will return to operating as an independent company

**原文链接**: [https://manus.im/blog/a-note-to-our-users](https://manus.im/blog/a-note-to-our-users)

生成摘要时出错

---

## 97. What good requirements look like (and how to write them)

**原文标题**: What good requirements look like (and how to write them)

**原文链接**: [https://projan.ai/blog/what-good-requirements-look-like-and-how-to-write-them](https://projan.ai/blog/what-good-requirements-look-like-and-how-to-write-them)

生成摘要时出错

---

## 98. In case you think there is consciousness, intelligence or personality in an LLM [video]

**原文标题**: In case you think there is consciousness, intelligence or personality in an LLM [video]

**原文链接**: [https://www.youtube.com/watch?v=vXV2ltVdLMQ](https://www.youtube.com/watch?v=vXV2ltVdLMQ)

生成摘要时出错

---

## 99. As AI eats the web, the internet’s collective memory is disappearing

**原文标题**: As AI eats the web, the internet’s collective memory is disappearing

**原文链接**: [https://thewalrus.ca/google-search-is-dying/](https://thewalrus.ca/google-search-is-dying/)

生成摘要时出错

---

## 100. Neutrinos from Deep Inside Earth Provide a New Picture of the Mantle

**原文标题**: Neutrinos from Deep Inside Earth Provide a New Picture of the Mantle

**原文链接**: [https://www.quantamagazine.org/neutrinos-from-deep-inside-earth-provide-a-new-picture-of-the-mantle-20260807/](https://www.quantamagazine.org/neutrinos-from-deep-inside-earth-provide-a-new-picture-of-the-mantle-20260807/)

生成摘要时出错

---

