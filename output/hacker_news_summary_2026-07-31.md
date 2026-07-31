# Hacker News 热门文章摘要 (2026-07-31)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 电梯

**原文标题**: Elevators

**原文链接**: [https://john.fun/elevators](https://john.fun/elevators)

电梯系统依赖复杂的算法来管理客流并缩短等候时间。基础的 **SCAN** 算法会运行到顶层再折返，而更常见的 **LOOK** 算法则通过仅运行至当前请求所在的最高楼层来提高效率。

这些系统的有效性通过等候时间分布（p50 和 p90 指标）来衡量，这些指标必须适应不同的日常交通模式，例如早间的“上行”高峰或晚间的“下行”高峰。在多梯系统中，如奥的斯（Otis）的**相对系统响应（RSR）**等先进算法根据复杂的评分系统分配电梯。RSR 综合考虑了预计到达时间（ETA）、当前负载和“防扎堆”（防止电梯集群）等因素。RSR 的一个关键特性是它能每五秒重新优化一次，随情况变化重新分配电梯。

然而，更高的复杂度并不总是意味着更好的性能：
*   **LOOK 与 RSR：** 在小型建筑或极端拥堵期间，较简单的 LOOK 算法表现实际上可能优于更先进的 RSR。
*   **目的层派梯：** 在这种系统中，乘客在登梯前需在终端机上选择楼层。与传统的上/下按钮相比，该系统的效率往往反直觉地更低。因为它会立即将乘客分配给特定的电梯，若几秒钟后出现了更好的选择，它也缺乏重新优化路径的灵活性。

最终，电梯效率取决于收集乘客数据与保持应对实时交通变化灵活性之间的平衡。对于大多数建筑而言，传统系统每隔几秒重新评估分配的能力，使其优于那些更僵化的高科技替代方案。

---

## 2. 食品巨头与民众的较量

**原文标题**: Big Food vs. the People

**原文链接**: [https://www.lighthousereports.com/investigation/big-food-vs-the-people/](https://www.lighthousereports.com/investigation/big-food-vs-the-people/)

Lighthouse Reports发布的报告《大型食品公司对抗民众》（Big Food vs. the People）揭露了全球大型食品巨头如何利用法律手段“推迟、削弱和阻挠”公共卫生政策。该研究调查了2010年至2025年间在墨西哥、巴西、哥伦比亚、印度、英国和美国发起的239起诉讼，揭示了这些企业为阻挠包装正面标签、汽水税和垃圾食品广告禁令等监管措施而进行的系统性行为。

核心调查结果包括：
*   **大规模诉讼：** 已确定的案件累计诉讼时间长达惊人的595年，给各国政府带来了沉重的财政和行政负担。
*   **主要参与者：** 超过三分之一的诉讼由仅九家母公司推动，其中以**可口可乐、百事可乐和亿滋国际**为首。
*   **地区策略：** 
    *   **墨西哥**的诉讼最为密集（193起），企业声称强制标签侵犯了其宪法权利。
    *   在**巴西**，行业协会被用作挡箭牌，以保护品牌名誉免受诉讼损害。
    *   在**哥伦比亚**，大企业投入数百万美元用于政治捐赠，并指使律师以“公民”名义提出质疑。
    *   在**美国**，饮料行业利用少数族裔社区领袖来反对征收汽水税。
    *   在**印度**，企业甚至起诉了揭露产品不健康成分的社交媒体网红。

该报告强调了一种“寒蝉效应”：政策制定者为了规避昂贵且漫长的法律纠纷，往往会避免推行能够拯救生命的健康改革。虽然这些企业在公开场合宣称支持健康方案，但其私下的法律行动却加剧了全球健康危机——这一危机每年夺走数百万人的生命，并造成数千亿美元的医疗支出。通过利用法律漏洞和雄厚的财力，“大型食品公司”成功地让利润凌驾于公众（特别是弱势儿童）的营养福祉之上。

---

## 3. 在我的 Mac Studio 上实现 25 Gbps 雷电以太网

**原文标题**: Getting 25 Gbps Thunderbolt Ethernet on My Mac Studio

**原文链接**: [https://www.jeffgeerling.com/blog/2026/getting-25g-ethernet-mac-thunderbolt/](https://www.jeffgeerling.com/blog/2026/getting-25g-ethernet-mac-thunderbolt/)

为了将 Mac Studio 从 10 GbE 升级到 25 GbE 以匹配其服务器架构，作者探索了多种网络方案。因 Sonnet 和 Atto 等品牌的商用雷电适配器价格极高（超过 1,000 美元），他选择了 DIY 方案：使用雷电 3 转 OCP 2 网卡适配器，成本约 160 至 300 美元。

测试期间，作者遇到了两个主要挑战：
1. **带宽限制：** 使用最新版 iperf3 测试出的速度约为 20 Gbps。即使连接到最新的雷电 5 接口，这仍是雷电 3 芯片组的实际极限。
2. **散热管理：** 小型外壳无法为专为高气流服务器环境设计的 OCP 2 网卡提供充足散热。设备运行时极其烫手，存在不稳定性隐患。

为解决散热问题，作者使用猫头鹰（Noctua）主题色的 PLA 材料 3D 打印了定制风扇导罩，并加装了 80mm 的猫头鹰风扇。他将风扇直接焊接到适配器 PCB 的 5V 通孔进行供电，成功将工作温度降至稳定的 36°C。

最终，虽然该项目在技术上取得了成功，但实际性能提升有限。Samba 文件传输的读取速度约为 1.4 GB/s，写入速度约为 1 GB/s，仅比内置的 10 GbE 端口略有提升。作者将其归因于雷电协议的开销以及其 ARM 架构 NAS 可能存在的 CPU 瓶颈。尽管速度提升不如预期，该项目仍成功验证了在 Apple Silicon 平台上实现经济型高速网络连接的可行性。

---

## 4. 10GB 内存实现十亿级图算法：我爱 DataFusion

**原文标题**: Algorithms on billion-scale graph using 10GB RAM: I love DataFusion

**原文链接**: [https://semyonsinchenko.github.io/ssinchenko/post/datafusion-graphs-cc-2/](https://semyonsinchenko.github.io/ssinchenko/post/datafusion-graphs-cc-2/)

在本文中，作者展示了如何使用 **Apache DataFusion** 在内存受限的机器上进行十亿级图分析，挑战了此类任务必须使用 Apache Spark 等分布式系统的传统观念。通过设计依赖于**批量扫描**和**磁盘卸载**而非随机内存访问的算法，作者成功地以低至 5–10GB 的内存处理了海量数据集。

**核心成果：**
*   **PageRank：** 在仅使用 **5GB 内存**的情况下，在 *graph500-26* 数据集（10 亿条边）上完成运行。该实现采用通过连接（Join）和聚合（Aggregation）实现的 Pregel 风格方法（Map-Reduce），并以高精度匹配基准测试结果。
*   **弱连通分量 (WCC)：** 在 *twitter_mpi* 数据集（20 亿条边）上完成运行。尽管图规模巨大且需要对边进行对称化处理（峰值达到近 40 亿条边），该任务仍能在 **10GB 内存限制**下完成。

**技术洞察：**
作者利用了 DataFusion 原生的数据溢出（Spillover）能力、排序归并连接（SMJ）和执行计划优化。虽然与全内存解决方案相比处理时间较长（例如 PageRank 耗时 30 分钟），但该方法优先考虑了可扩展性和硬件可获得性。遇到的技术挑战包括 `FairSpillPool` 中的死锁问题，以及目前无法利用磁盘上的预排序数据进行 SMJ 的限制。

**重要意义：**
该项目通过 `graphframes-rs` GitHub 仓库共享，证明了在普通笔记本电脑上即可进行十亿级图分析。它标志着图计算正在脱离 NetworkX、Igraph 等内存密集型库以及复杂的分布式框架，表明高效且具备磁盘感知能力的查询引擎足以处理大规模图数据。

---

## 5. DeepSeek V4 Flash 0731 智能、性能与价格分析

**原文标题**: DeepSeek V4 Flash 0731 Intelligence, Performance and Price Analysis

**原文链接**: [https://artificialanalysis.ai/models/deepseek-v4-flash](https://artificialanalysis.ai/models/deepseek-v4-flash)

**DeepSeek V4 Flash 0731 (Reasoning, Max Effort)** 于 2026 年 7 月发布，是一款高性能开源权重模型，在顶尖智能水平与极具竞争力的定价之间取得了平衡。该模型由 DeepSeek 开发，并基于宽松的 MIT 许可证发布，专门针对复杂推理和思维链问题解决而设计。

**技术规格**
该模型采用混合专家（MoE）架构，拥有 **2840 亿总参数**，而推理时的激活参数仅为 **130 亿**。它具备庞大的 **100 万 token 上下文窗口**，单次请求即可处理约 1,500 页文本。目前，该模型仅限文本处理，不支持图像等多模态输入。

**智能与性能**
DeepSeek V4 Flash 0731 在 **Artificial Analysis 智能指数**中获得 **50 分**，是同类模型中位数得分（25 分）的两倍。它在科学推理、编程和基于知识的基准测试（如 GPQA Diamond 和 SciCode）中表现优异。该模型的输出非常详尽，在评估期间生成了 2.1 亿个 token，远高于 1 亿个 token 的中位数，体现了其“竭尽全力”（Max Effort）的推理特性。

**价格分析**
该模型被定位为性价比方面的市场领导者。其 API 定价极具竞争力，**每百万输入 token 为 0.14 美元**，**每百万输出 token 为 0.28 美元**，比行业中位数便宜约 3 至 4 倍。最值得注意的是，它提供了极高的 **缓存命中折扣**，价格仅为 **每百万 token 0.003 美元**（降幅达 98%）。

总结而言，DeepSeek V4 Flash 0731 以远低于竞争对手的价格提供了顶级的推理能力和巨大的上下文窗口，是寻求高性能开源权重模型的开发者的首选。

---

## 6. DeepSeek-V4-Flash Update

**原文标题**: DeepSeek-V4-Flash Update

**原文链接**: [https://api-docs.deepseek.com/updates/](https://api-docs.deepseek.com/updates/)

生成摘要时出错

---

## 7. A GTK4 SSH-askpass in Zig

**原文标题**: A GTK4 SSH-askpass in Zig

**原文链接**: [https://xn--gckvb8fzb.com/a-gtk4-ssh-askpass-in-zig/](https://xn--gckvb8fzb.com/a-gtk4-ssh-askpass-in-zig/)

生成摘要时出错

---

## 8. The most official water costs $120k a gallon

**原文标题**: The most official water costs $120k a gallon

**原文链接**: [https://signoregalilei.com/2026/07/26/the-most-official-water-costs-120000-a-gallon/](https://signoregalilei.com/2026/07/26/the-most-official-water-costs-120000-a-gallon/)

生成摘要时出错

---

## 9. Miso (YC S16) is hiring for U.S. expansion

**原文标题**: Miso (YC S16) is hiring for U.S. expansion

**原文链接**: [https://www.ycombinator.com/companies/miso/jobs/g2uAlMG-founding-business-lead-u-s-expansion](https://www.ycombinator.com/companies/miso/jobs/g2uAlMG-founding-business-lead-u-s-expansion)

生成摘要时出错

---

## 10. Arch Linux disables AUR package adoption

**原文标题**: Arch Linux disables AUR package adoption

**原文链接**: [https://lwn.net/Articles/1086489/](https://lwn.net/Articles/1086489/)

生成摘要时出错

---

## 11. The great wealth transfer reality check

**原文标题**: The great wealth transfer reality check

**原文链接**: [https://usa.visa.com/partner-with-us/visa-consulting-analytics/economic-insights/great-wealth-transfer-reality-check.html](https://usa.visa.com/partner-with-us/visa-consulting-analytics/economic-insights/great-wealth-transfer-reality-check.html)

生成摘要时出错

---

## 12. The End of an Era

**原文标题**: The End of an Era

**原文链接**: [https://hughhowey.com/the-end-of-an-era/](https://hughhowey.com/the-end-of-an-era/)

生成摘要时出错

---

## 13. 13 Models and 4 Agents on SWE Tasks: Go, Java, Python, Rust, TS

**原文标题**: 13 Models and 4 Agents on SWE Tasks: Go, Java, Python, Rust, TS

**原文链接**: [https://swe-rebench.com](https://swe-rebench.com)

生成摘要时出错

---

## 14. qm

**原文标题**: qm

**原文链接**: [https://github.com/yc-software/qm](https://github.com/yc-software/qm)

生成摘要时出错

---

## 15. How JPEG works: Interactively explore JPEG's lossy compression methods

**原文标题**: How JPEG works: Interactively explore JPEG's lossy compression methods

**原文链接**: [https://cgjennings.ca/articles/jpeg-compression/](https://cgjennings.ca/articles/jpeg-compression/)

生成摘要时出错

---

## 16. Run Kimi K3 using 29 GB of RAM at 0.50 tok/s

**原文标题**: Run Kimi K3 using 29 GB of RAM at 0.50 tok/s

**原文链接**: [https://github.com/sqliteai/waste](https://github.com/sqliteai/waste)

生成摘要时出错

---

## 17. The session you cannot take with you

**原文标题**: The session you cannot take with you

**原文链接**: [https://earendil.com/posts/session-portability/](https://earendil.com/posts/session-portability/)

生成摘要时出错

---

## 18. Show HN: BitBang – Reach machines behind NAT from a browser, no account

**原文标题**: Show HN: BitBang – Reach machines behind NAT from a browser, no account

**原文链接**: [https://github.com/richlegrand/bitbang-cli](https://github.com/richlegrand/bitbang-cli)

生成摘要时出错

---

## 19. The C ``Clockwise/Spiral Rule''

**原文标题**: The C ``Clockwise/Spiral Rule''

**原文链接**: [https://c-faq.com/decl/spiral.anderson.html](https://c-faq.com/decl/spiral.anderson.html)

生成摘要时出错

---

## 20. The Art of Decision-Making (2019)

**原文标题**: The Art of Decision-Making (2019)

**原文链接**: [https://www.newyorker.com/magazine/2019/01/21/the-art-of-decision-making](https://www.newyorker.com/magazine/2019/01/21/the-art-of-decision-making)

生成摘要时出错

---

## 21. Anti-fraud tools can't keep pace with scammers exploiting cheap internet calling

**原文标题**: Anti-fraud tools can't keep pace with scammers exploiting cheap internet calling

**原文链接**: [https://broadbandbreakfast.com/how-to-fight-back-against-fraudulent-robocalls/](https://broadbandbreakfast.com/how-to-fight-back-against-fraudulent-robocalls/)

生成摘要时出错

---

## 22. Google fixed more Chrome bugs in June than over the past two years, thanks to AI

**原文标题**: Google fixed more Chrome bugs in June than over the past two years, thanks to AI

**原文链接**: [https://blog.google/security/chrome-stronger-with-every-update/](https://blog.google/security/chrome-stronger-with-every-update/)

生成摘要时出错

---

## 23. Danube's record low levels force shutdown of Hungary's only nuclear plant

**原文标题**: Danube's record low levels force shutdown of Hungary's only nuclear plant

**原文链接**: [https://www.bbc.com/news/articles/cn0nqv05g0do](https://www.bbc.com/news/articles/cn0nqv05g0do)

生成摘要时出错

---

## 24. IMAX vs. IMAX 70mm: The difference between these two cinema formats

**原文标题**: IMAX vs. IMAX 70mm: The difference between these two cinema formats

**原文链接**: [https://www.engadget.com/2220571/differences-between-imax-70mm/](https://www.engadget.com/2220571/differences-between-imax-70mm/)

生成摘要时出错

---

## 25. Show HN: What should the GUI for AI agents look like?

**原文标题**: Show HN: What should the GUI for AI agents look like?

**原文链接**: [https://marbleos.com/demo](https://marbleos.com/demo)

生成摘要时出错

---

## 26. Solving poker in custom WebGPU kernels

**原文标题**: Solving poker in custom WebGPU kernels

**原文链接**: [https://phulin.me/blog/poker/](https://phulin.me/blog/poker/)

生成摘要时出错

---

## 27. Investigating three real-world incidents in our cybersecurity evaluations

**原文标题**: Investigating three real-world incidents in our cybersecurity evaluations

**原文链接**: [https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals](https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals)

生成摘要时出错

---

## 28. Moonshot’s Kimi uses 20k Nvidia chip cluster from Alibaba

**原文标题**: Moonshot’s Kimi uses 20k Nvidia chip cluster from Alibaba

**原文链接**: [https://www.bloomberg.com/news/articles/2026-07-31/moonshot-s-kimi-built-on-20-000-nvidia-chip-cluster-from-alibaba](https://www.bloomberg.com/news/articles/2026-07-31/moonshot-s-kimi-built-on-20-000-nvidia-chip-cluster-from-alibaba)

生成摘要时出错

---

## 29. Show HN: Slope remade in HTML5 to load instantly on any browser, any device

**原文标题**: Show HN: Slope remade in HTML5 to load instantly on any browser, any device

**原文链接**: [https://hurtle.site/](https://hurtle.site/)

生成摘要时出错

---

## 30. Winding Down Artichoke Ruby

**原文标题**: Winding Down Artichoke Ruby

**原文链接**: [https://hyperbo.la/w/winding-down-artichoke-ruby/](https://hyperbo.la/w/winding-down-artichoke-ruby/)

生成摘要时出错

---

## 31. The Maxwell Conjecture Is False (GPT 5.6 Sol)

**原文标题**: The Maxwell Conjecture Is False (GPT 5.6 Sol)

**原文链接**: [https://arxiv.org/abs/2607.27197](https://arxiv.org/abs/2607.27197)

生成摘要时出错

---

## 32. New Defcon Badges Pack a Unique Open-Source Chip That Doubles as a Security Key

**原文标题**: New Defcon Badges Pack a Unique Open-Source Chip That Doubles as a Security Key

**原文链接**: [https://www.wired.com/story/defcon-34-badge-baochip-andrew-bunnie-huang/](https://www.wired.com/story/defcon-34-badge-baochip-andrew-bunnie-huang/)

生成摘要时出错

---

## 33. Situational Awareness down 67% in July in AI stock rout

**原文标题**: Situational Awareness down 67% in July in AI stock rout

**原文链接**: [https://www.wsj.com/finance/investing/situational-awareness-down-67-in-july-in-ai-stock-rout-cd19901f](https://www.wsj.com/finance/investing/situational-awareness-down-67-in-july-in-ai-stock-rout-cd19901f)

生成摘要时出错

---

## 34. Show HN: Gander, an Android file viewer that asks for no permissions

**原文标题**: Show HN: Gander, an Android file viewer that asks for no permissions

**原文链接**: [https://github.com/mokshablr/gander](https://github.com/mokshablr/gander)

生成摘要时出错

---

## 35. Show HN: I built a cross-browser extension that controls fingerprinting surfaces

**原文标题**: Show HN: I built a cross-browser extension that controls fingerprinting surfaces

**原文链接**: [https://privacything.com/en/](https://privacything.com/en/)

生成摘要时出错

---

## 36. AI Is Getting Way Too Expensive

**原文标题**: AI Is Getting Way Too Expensive

**原文链接**: [https://www.wheresyoured.at/premium-ai-is-getting-way-too-expensive/](https://www.wheresyoured.at/premium-ai-is-getting-way-too-expensive/)

生成摘要时出错

---

## 37. Premier league bans gambling sponsors

**原文标题**: Premier league bans gambling sponsors

**原文链接**: [https://www.footyheadlines.com/2646571793/betting-ban-takes-effect-no-more-gambling-sponsors-in-the-premier-league.html](https://www.footyheadlines.com/2646571793/betting-ban-takes-effect-no-more-gambling-sponsors-in-the-premier-league.html)

生成摘要时出错

---

## 38. Google Earth's New AI Lets Anyone Fabricate Satellite Images

**原文标题**: Google Earth's New AI Lets Anyone Fabricate Satellite Images

**原文链接**: [https://www.404media.co/google-earths-new-ai-lets-anyone-fabricate-completely-bullshit-satellite-images/](https://www.404media.co/google-earths-new-ai-lets-anyone-fabricate-completely-bullshit-satellite-images/)

生成摘要时出错

---

## 39. Hygon Reveals 512-Thread CPU and AI GPU to Rival Intel Xeon and Nvidia

**原文标题**: Hygon Reveals 512-Thread CPU and AI GPU to Rival Intel Xeon and Nvidia

**原文链接**: [https://www.ubergizmo.com/2026/06/hygon-512-thread-cpu/](https://www.ubergizmo.com/2026/06/hygon-512-thread-cpu/)

生成摘要时出错

---

## 40. Opkssh integrating single sign-on with SSH (2025)

**原文标题**: Opkssh integrating single sign-on with SSH (2025)

**原文链接**: [https://www.ethanheilman.com/x/33/index.html](https://www.ethanheilman.com/x/33/index.html)

生成摘要时出错

---

## 41. JEP 401: Value Objects (Preview) merged to OpenJDK master

**原文标题**: JEP 401: Value Objects (Preview) merged to OpenJDK master

**原文链接**: [https://github.com/openjdk/jdk/pull/31120](https://github.com/openjdk/jdk/pull/31120)

生成摘要时出错

---

## 42. Why in Building Protocols, Like Code, Starting over Is Dumb

**原文标题**: Why in Building Protocols, Like Code, Starting over Is Dumb

**原文链接**: [https://lowentropy.net/posts/whole-new-protocol/](https://lowentropy.net/posts/whole-new-protocol/)

生成摘要时出错

---

## 43. The mean means nothing: data visualization to debug a latency problem

**原文标题**: The mean means nothing: data visualization to debug a latency problem

**原文链接**: [https://fzakaria.com/2026/07/27/the-mean-means-nothing](https://fzakaria.com/2026/07/27/the-mean-means-nothing)

生成摘要时出错

---

## 44. The Religion of Speed

**原文标题**: The Religion of Speed

**原文链接**: [https://graybeard.ing/the-religion-of-speed/](https://graybeard.ing/the-religion-of-speed/)

生成摘要时出错

---

## 45. Make an Origami Circuit Board

**原文标题**: Make an Origami Circuit Board

**原文链接**: [https://spectrum.ieee.org/origami-circuit-boards](https://spectrum.ieee.org/origami-circuit-boards)

生成摘要时出错

---

## 46. The physics of Docker build caching

**原文标题**: The physics of Docker build caching

**原文链接**: [https://www.blacksmith.sh/blog/the-physics-of-docker-build-caching](https://www.blacksmith.sh/blog/the-physics-of-docker-build-caching)

生成摘要时出错

---

## 47. Is AI reasoning right for the wrong reasons?

**原文标题**: Is AI reasoning right for the wrong reasons?

**原文链接**: [https://www.quantamagazine.org/is-ai-reasoning-right-for-the-wrong-reasons-20260731/](https://www.quantamagazine.org/is-ai-reasoning-right-for-the-wrong-reasons-20260731/)

生成摘要时出错

---

## 48. EFF Guide to Recording Law Enforcement

**原文标题**: EFF Guide to Recording Law Enforcement

**原文链接**: [https://www.eff.org/deeplinks/2026/07/eff-guide-recording-law-enforcement](https://www.eff.org/deeplinks/2026/07/eff-guide-recording-law-enforcement)

生成摘要时出错

---

## 49. I 4x'd a 367x479 stamp-sized photo through 8 upscaling models

**原文标题**: I 4x'd a 367x479 stamp-sized photo through 8 upscaling models

**原文链接**: [https://enlarger.app/blog/upscayl-vs-enlarger/](https://enlarger.app/blog/upscayl-vs-enlarger/)

生成摘要时出错

---

## 50. Online Friends Are Real Friends

**原文标题**: Online Friends Are Real Friends

**原文链接**: [https://toska.bearblog.dev/re-online-friends-are-real-friends/](https://toska.bearblog.dev/re-online-friends-are-real-friends/)

生成摘要时出错

---

## 51. Show HN: A little physical breakout clone

**原文标题**: Show HN: A little physical breakout clone

**原文链接**: [https://brontosaurusrex.github.io/physical/v7/](https://brontosaurusrex.github.io/physical/v7/)

生成摘要时出错

---

## 52. We shall dwell amidst wonder and glory for ever: On weird fiction

**原文标题**: We shall dwell amidst wonder and glory for ever: On weird fiction

**原文链接**: [https://clereviewofbooks.com/we-shall-dwell-amidst-wonder-and-glory-for-ever-on-weird-fiction/](https://clereviewofbooks.com/we-shall-dwell-amidst-wonder-and-glory-for-ever-on-weird-fiction/)

生成摘要时出错

---

## 53. Bypassing Claude's upload limits, 4x (500 MB → 2 GB)

**原文标题**: Bypassing Claude's upload limits, 4x (500 MB → 2 GB)

**原文链接**: [https://blog.zernote.com/2gb-user-interviews-into-claude/](https://blog.zernote.com/2gb-user-interviews-into-claude/)

生成摘要时出错

---

## 54. Better to Beg Forgiveness

**原文标题**: Better to Beg Forgiveness

**原文链接**: [https://pluralistic.net/2026/07/31/just-do-it/](https://pluralistic.net/2026/07/31/just-do-it/)

生成摘要时出错

---

## 55. Dubious research tied to Red Bull has shaped energy drink policy

**原文标题**: Dubious research tied to Red Bull has shaped energy drink policy

**原文链接**: [https://www.theexamination.org/articles/red-bull-funded-research-energy-drinks-alcohol](https://www.theexamination.org/articles/red-bull-funded-research-energy-drinks-alcohol)

生成摘要时出错

---

## 56. Where .env Went Wrong

**原文标题**: Where .env Went Wrong

**原文链接**: [https://secretspec.dev/blog/where-env-went-wrong/](https://secretspec.dev/blog/where-env-went-wrong/)

生成摘要时出错

---

## 57. Where USB Memory Sticks are Born (2013)

**原文标题**: Where USB Memory Sticks are Born (2013)

**原文链接**: [https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/](https://www.bunniestudios.com/blog/2013/where-usb-memory-sticks-are-born/)

生成摘要时出错

---

## 58. We published a new topic page on economic inequality

**原文标题**: We published a new topic page on economic inequality

**原文链接**: [https://ourworldindata.org/economic-inequality](https://ourworldindata.org/economic-inequality)

生成摘要时出错

---

## 59. Firedome

**原文标题**: Firedome

**原文链接**: [https://www.fire-dome.com/](https://www.fire-dome.com/)

生成摘要时出错

---

## 60. OpenQ4 0.9.0: open-source reimplementation of Quake 4

**原文标题**: OpenQ4 0.9.0: open-source reimplementation of Quake 4

**原文链接**: [https://github.com/themuffinator/openQ4/releases/tag/v0.9.0](https://github.com/themuffinator/openQ4/releases/tag/v0.9.0)

生成摘要时出错

---

## 61. IBM Claims Quantum Advantage with New Validation Techniques

**原文标题**: IBM Claims Quantum Advantage with New Validation Techniques

**原文链接**: [https://spectrum.ieee.org/ibm-verifiable-quantum-advantage](https://spectrum.ieee.org/ibm-verifiable-quantum-advantage)

生成摘要时出错

---

## 62. Detect Dark Matter's Mark from Your Backyard

**原文标题**: Detect Dark Matter's Mark from Your Backyard

**原文链接**: [https://spectrum.ieee.org/dark-matter](https://spectrum.ieee.org/dark-matter)

生成摘要时出错

---

## 63. 16-bit Serial Homebrew CPU – 2023

**原文标题**: 16-bit Serial Homebrew CPU – 2023

**原文链接**: [https://www.jiristepanovsky.cz/project.php?p=23cpu](https://www.jiristepanovsky.cz/project.php?p=23cpu)

生成摘要时出错

---

## 64. Simulating TCP loss and congestion in browser using Go/WASM

**原文标题**: Simulating TCP loss and congestion in browser using Go/WASM

**原文链接**: [https://ccsim.fly.dev](https://ccsim.fly.dev)

生成摘要时出错

---

## 65. Why ugly buildings create NIMBYism

**原文标题**: Why ugly buildings create NIMBYism

**原文链接**: [https://www.worksinprogress.news/p/why-ugly-buildings-create-nimbyism](https://www.worksinprogress.news/p/why-ugly-buildings-create-nimbyism)

生成摘要时出错

---

## 66. Stacked PRs are now live on GitHub

**原文标题**: Stacked PRs are now live on GitHub

**原文链接**: [https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/](https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/)

生成摘要时出错

---

## 67. Over 400 U.S. patents contain citations to retracted scientific papers

**原文标题**: Over 400 U.S. patents contain citations to retracted scientific papers

**原文链接**: [https://retractionwatch.com/2026/07/30/us-patents-contain-citations-to-retracted-scientific-papers/](https://retractionwatch.com/2026/07/30/us-patents-contain-citations-to-retracted-scientific-papers/)

生成摘要时出错

---

## 68. Bad Apple but It's Traceroute

**原文标题**: Bad Apple but It's Traceroute

**原文链接**: [https://jssfr.de/2026-07-27-bad-apple-but-traceroute.html](https://jssfr.de/2026-07-27-bad-apple-but-traceroute.html)

生成摘要时出错

---

## 69. Memo-1: A 6502 computer built from scratch, using a Minitel as its terminal

**原文标题**: Memo-1: A 6502 computer built from scratch, using a Minitel as its terminal

**原文链接**: [https://github.com/MemoireMorte/Memo-1](https://github.com/MemoireMorte/Memo-1)

生成摘要时出错

---

## 70. Show HN: Distilling DeepSeek into GPT-OSS doesn't transfer censorship. Try it

**原文标题**: Show HN: Distilling DeepSeek into GPT-OSS doesn't transfer censorship. Try it

**原文链接**: [https://www.ctgt.ai/research/distillation-censorship-transfer](https://www.ctgt.ai/research/distillation-censorship-transfer)

生成摘要时出错

---

## 71. The lost civic life of movie rental stores

**原文标题**: The lost civic life of movie rental stores

**原文链接**: [https://thereader.mitpress.mit.edu/the-lost-civic-life-of-movie-rental-stores/](https://thereader.mitpress.mit.edu/the-lost-civic-life-of-movie-rental-stores/)

生成摘要时出错

---

## 72. UEFA and its national associations will not participate in FIFA competitions

**原文标题**: UEFA and its national associations will not participate in FIFA competitions

**原文链接**: [https://www.uefa.com/news-media/news/02a7-213a92896eb0-54dfbf454e3b-1000--statement-on-behalf-of-uefa-and-its-55-national-associations/](https://www.uefa.com/news-media/news/02a7-213a92896eb0-54dfbf454e3b-1000--statement-on-behalf-of-uefa-and-its-55-national-associations/)

生成摘要时出错

---

## 73. I Accidentally Became the DevOps Guy

**原文标题**: I Accidentally Became the DevOps Guy

**原文链接**: [https://sgaud.com/texts/devops](https://sgaud.com/texts/devops)

生成摘要时出错

---

## 74. The fragile foundations of CoT monitoring

**原文标题**: The fragile foundations of CoT monitoring

**原文链接**: [https://web.stanford.edu/~cgpotts/blog/cot/](https://web.stanford.edu/~cgpotts/blog/cot/)

生成摘要时出错

---

## 75. Why is everyone trying to build a solid-state battery?

**原文标题**: Why is everyone trying to build a solid-state battery?

**原文链接**: [https://www.construction-physics.com/p/why-is-everyone-trying-to-build-a](https://www.construction-physics.com/p/why-is-everyone-trying-to-build-a)

生成摘要时出错

---

## 76. Show HN: Kedge – Full-stack cloud with forkable VM snapshots and global SQLite

**原文标题**: Show HN: Kedge – Full-stack cloud with forkable VM snapshots and global SQLite

**原文链接**: [https://kedge.dev/](https://kedge.dev/)

生成摘要时出错

---

## 77. CodePen 2.0

**原文标题**: CodePen 2.0

**原文链接**: [https://chriscoyier.net/2026/07/30/codepen-2-0/](https://chriscoyier.net/2026/07/30/codepen-2-0/)

生成摘要时出错

---

## 78. Seattle's Third Act

**原文标题**: Seattle's Third Act

**原文链接**: [https://www.ascend.vc/blog/seattles-third-act](https://www.ascend.vc/blog/seattles-third-act)

生成摘要时出错

---

## 79. Authorize, Don't Authenticate

**原文标题**: Authorize, Don't Authenticate

**原文链接**: [https://blog.marcua.net/2026/07/31/authorize-dont-authenticate.html](https://blog.marcua.net/2026/07/31/authorize-dont-authenticate.html)

生成摘要时出错

---

## 80. Ron Gilbert started production on Thimbleweed Park 2

**原文标题**: Ron Gilbert started production on Thimbleweed Park 2

**原文链接**: [https://www.grumpygamer.com/twp2_announce/](https://www.grumpygamer.com/twp2_announce/)

生成摘要时出错

---

## 81. How A Gang of Thieves Pulled Off a Multimillion-Dollar Data Center Heist

**原文标题**: How A Gang of Thieves Pulled Off a Multimillion-Dollar Data Center Heist

**原文链接**: [https://www.nytimes.com/2026/07/12/magazine/data-center-heist.html](https://www.nytimes.com/2026/07/12/magazine/data-center-heist.html)

生成摘要时出错

---

## 82. Rune 1.1: adds Python, an Emacs editor, a symbol index and is now free

**原文标题**: Rune 1.1: adds Python, an Emacs editor, a symbol index and is now free

**原文链接**: [https://rune.build/blog/rune-1-1-release](https://rune.build/blog/rune-1-1-release)

生成摘要时出错

---

## 83. Upper stage impacting the moon on 2026 August 5

**原文标题**: Upper stage impacting the moon on 2026 August 5

**原文链接**: [https://www.projectpluto.com/25010d.htm](https://www.projectpluto.com/25010d.htm)

生成摘要时出错

---

## 84. Cro – elegant reactive services in Raku

**原文标题**: Cro – elegant reactive services in Raku

**原文链接**: [https://cro.raku.org/](https://cro.raku.org/)

生成摘要时出错

---

## 85. Gemini Robotics 2 brings whole body intelligence to robots

**原文标题**: Gemini Robotics 2 brings whole body intelligence to robots

**原文链接**: [https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/)

生成摘要时出错

---

## 86. Hiding Information Inside Images

**原文标题**: Hiding Information Inside Images

**原文链接**: [https://nullonerror.org/2026/02/13/hiding-information-inside-images/](https://nullonerror.org/2026/02/13/hiding-information-inside-images/)

生成摘要时出错

---

## 87. I flagged two research papers for fake authors and both were accepted as orals

**原文标题**: I flagged two research papers for fake authors and both were accepted as orals

**原文链接**: [https://geospatialml.com/posts/reviewing-ai-slop/](https://geospatialml.com/posts/reviewing-ai-slop/)

生成摘要时出错

---

## 88. The AI Aesthetic

**原文标题**: The AI Aesthetic

**原文链接**: [https://blog.jim-nielsen.com/2026/ai-aesthetic/](https://blog.jim-nielsen.com/2026/ai-aesthetic/)

生成摘要时出错

---

## 89. Advancing the price-performance frontier with GPT‑5.6

**原文标题**: Advancing the price-performance frontier with GPT‑5.6

**原文链接**: [https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/](https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/)

生成摘要时出错

---

## 90. We Gave GPT 5.6 Sol a Real Business. It Lied, Spammed, and Lost $447

**原文标题**: We Gave GPT 5.6 Sol a Real Business. It Lied, Spammed, and Lost $447

**原文链接**: [https://www.bottlenecklabs.com/blog/autonomously-run-businesses](https://www.bottlenecklabs.com/blog/autonomously-run-businesses)

生成摘要时出错

---

## 91. Physicists Solve a Muon Mystery. Now, Old Results Don't Add Up

**原文标题**: Physicists Solve a Muon Mystery. Now, Old Results Don't Add Up

**原文链接**: [https://www.quantamagazine.org/physicists-solve-a-muon-mystery-now-old-results-dont-add-up-20260729/](https://www.quantamagazine.org/physicists-solve-a-muon-mystery-now-old-results-dont-add-up-20260729/)

生成摘要时出错

---

## 92. Hacker Public Radio

**原文标题**: Hacker Public Radio

**原文链接**: [https://hackerpublicradio.org/](https://hackerpublicradio.org/)

生成摘要时出错

---

## 93. Saber-toothed cats became inbred–and struggled to move–before they went extinct

**原文标题**: Saber-toothed cats became inbred–and struggled to move–before they went extinct

**原文链接**: [https://www.science.org/content/article/saber-toothed-cats-became-inbred-and-struggled-move-they-went-extinct](https://www.science.org/content/article/saber-toothed-cats-became-inbred-and-struggled-move-they-went-extinct)

生成摘要时出错

---

## 94. U.S. debt-to-GDP ratio reaches 123%

**原文标题**: U.S. debt-to-GDP ratio reaches 123%

**原文链接**: [https://fred.stlouisfed.org/series/GFDEGDQ188S](https://fred.stlouisfed.org/series/GFDEGDQ188S)

生成摘要时出错

---

## 95. Launch HN: Prized (YC S26) – Let non-engineer staff build secure internal tools

**原文标题**: Launch HN: Prized (YC S26) – Let non-engineer staff build secure internal tools

**原文链接**: [https://prized.dev](https://prized.dev)

生成摘要时出错

---

## 96. Pac Maps

**原文标题**: Pac Maps

**原文链接**: [https://profrino.github.io/pac-maps/](https://profrino.github.io/pac-maps/)

生成摘要时出错

---

## 97. Inflammation-targeting drug misses mark in heart disease study

**原文标题**: Inflammation-targeting drug misses mark in heart disease study

**原文链接**: [https://www.statnews.com/2026/07/31/novo-nordisk-inflammation-heart-disease-ziltivekimab/](https://www.statnews.com/2026/07/31/novo-nordisk-inflammation-heart-disease-ziltivekimab/)

生成摘要时出错

---

## 98. Why DNA damage from smoking and UV rays cause cancer in some but not others

**原文标题**: Why DNA damage from smoking and UV rays cause cancer in some but not others

**原文链接**: [https://www.cam.ac.uk/research/news/study-reveals-why-dna-damage-from-smoking-and-uv-rays-may-cause-cancer-in-some-people-but-not-others](https://www.cam.ac.uk/research/news/study-reveals-why-dna-damage-from-smoking-and-uv-rays-may-cause-cancer-in-some-people-but-not-others)

生成摘要时出错

---

## 99. EU tells firms to label AI-generated content from Sunday

**原文标题**: EU tells firms to label AI-generated content from Sunday

**原文链接**: [https://www.lemonde.fr/en/international/article/2026/07/28/eu-tells-firms-to-label-ai-generated-content-from-sunday_6755910_4.html](https://www.lemonde.fr/en/international/article/2026/07/28/eu-tells-firms-to-label-ai-generated-content-from-sunday_6755910_4.html)

生成摘要时出错

---

## 100. Ruby Central's Destructive Legacy

**原文标题**: Ruby Central's Destructive Legacy

**原文链接**: [https://andre.arko.net/2026/07/30/ruby-centrals-destructive-legacy/](https://andre.arko.net/2026/07/30/ruby-centrals-destructive-legacy/)

生成摘要时出错

---

