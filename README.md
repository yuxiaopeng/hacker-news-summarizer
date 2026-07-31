# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-07-31.md)

*最后自动更新时间: 2026-07-31 18:52:19*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 2 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 3 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 4 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 5 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 6 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 7 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 8 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 9 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 10 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 11 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 12 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 13 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 14 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 15 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 16 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 17 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 18 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 19 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 20 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 21 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 22 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 23 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 24 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 25 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 26 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 27 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 28 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 29 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 30 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 31 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 32 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 33 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 34 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 35 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 36 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 37 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 38 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 39 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 40 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 41 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 42 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 43 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 44 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 45 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 46 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 47 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 48 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 49 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 50 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 51 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 52 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 53 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 54 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 55 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 56 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 57 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 58 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 59 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 60 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 61 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 62 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 63 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 64 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 65 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 66 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 67 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 68 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 69 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 70 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 71 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 72 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 73 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 74 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 75 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 76 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 77 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 78 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 79 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 80 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 81 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 82 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 83 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 84 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 85 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 86 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 87 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 88 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 89 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 90 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 91 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 92 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 93 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 94 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 95 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 96 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 97 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 98 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 99 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 100 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 101 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 102 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 103 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 104 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 105 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 106 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 107 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 108 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 109 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 110 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 111 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 112 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 113 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 114 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 115 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 116 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 117 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 118 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 119 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 120 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 121 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 122 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 123 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 124 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 125 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 126 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 127 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 128 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 129 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 130 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 131 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 132 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 133 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 134 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 135 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 136 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 137 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 138 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 139 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 140 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 141 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 142 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 143 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 144 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 145 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 146 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 147 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 148 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 149 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 150 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 151 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 152 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 153 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 154 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 155 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 156 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 157 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 158 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 159 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 160 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 161 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 162 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 163 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 164 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 165 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 166 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 167 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 168 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 169 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 170 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 171 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 172 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 173 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 174 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 175 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 176 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 177 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 178 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 179 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 180 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 181 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 182 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 183 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 184 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 185 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 186 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 187 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 188 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 189 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 190 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 191 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 192 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 193 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 194 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 195 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 196 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 197 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 198 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 199 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 200 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 201 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 202 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 203 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 204 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 205 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 206 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 207 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 208 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 209 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 210 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 211 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 212 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 213 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 214 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 215 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 216 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 217 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 218 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 219 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 220 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 221 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 222 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 223 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 224 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 225 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 226 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 227 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 228 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 229 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 230 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 231 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 232 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 233 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 234 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 235 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 236 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 237 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 238 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 239 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 240 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 241 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 242 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 243 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 244 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 245 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 246 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 247 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 248 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 249 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 250 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 251 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 252 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 253 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 254 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 255 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 256 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 257 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 258 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 259 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 260 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 261 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 262 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 263 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 264 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 265 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 266 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 267 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 268 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 269 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 270 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 271 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 272 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 273 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 274 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 275 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 276 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 277 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 278 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 279 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 280 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 281 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 282 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 283 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 284 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 285 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 286 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 287 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 288 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 289 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 290 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 291 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 292 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 293 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 294 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 295 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 296 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 297 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 298 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 299 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 300 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 301 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 302 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 303 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 304 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 305 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 306 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 307 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 308 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 309 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 310 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 311 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 312 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 313 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 314 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 315 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 316 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 317 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 318 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 319 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 320 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 321 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 322 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 323 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 324 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 325 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 326 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 327 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 328 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 329 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 330 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 331 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 332 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 333 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 334 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 335 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 336 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 337 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 338 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 339 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 340 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 341 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 342 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 343 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 344 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 345 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 346 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 347 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 348 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 349 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 350 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 351 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 352 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 353 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 354 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 355 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 356 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 357 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 358 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 359 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 360 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 361 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 362 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 363 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 364 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 365 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 366 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 367 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 368 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 369 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 370 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 371 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 372 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 373 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 374 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 375 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 376 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 377 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 378 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 379 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 380 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 381 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 382 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 383 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 384 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 385 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 386 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 387 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 388 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 389 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 390 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 391 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 392 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 393 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 394 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 395 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 396 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 397 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 398 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 399 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 400 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 401 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 402 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 403 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 404 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 405 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 406 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 407 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 408 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 409 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 410 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 411 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 412 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 413 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 414 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 415 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 416 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 417 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 418 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 419 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 420 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 421 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 422 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 423 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 424 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 425 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 426 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 427 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 428 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 429 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 430 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 431 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 432 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 433 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 434 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 435 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 436 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 437 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 438 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 439 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 440 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 441 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 442 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 443 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 444 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 445 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 446 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 447 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 448 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 449 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 450 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 451 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 452 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 453 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 454 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 455 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 456 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 457 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 458 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 459 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 460 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 461 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 462 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 463 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 464 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 465 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 466 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 467 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 468 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 469 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 470 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 471 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 472 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 473 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 474 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 475 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 476 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 477 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 478 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 479 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 480 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 481 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 482 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 483 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 484 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 485 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 486 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 487 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 488 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 489 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 490 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 491 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 492 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 493 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 494 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 495 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 496 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 497 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 498 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
