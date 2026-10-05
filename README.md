# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-10-05.md)

*最后自动更新时间: 2026-10-05 23:31:59*
## 1. Beam：Reflection 的 501B 开放权重模型

**原文标题**: Beam: Reflection's 501B open-weight model

**原文链接**: [https://reflection.ai/blog/introducing-beam](https://reflection.ai/blog/introducing-beam)

Reflection 推出了其首款开源权重的稀疏混合专家（MoE）模型 **Beam**，专为编程、推理和智能体工作负载而设计。Beam 拥有 **5010 亿总参数**（230 亿激活参数），在提供前沿性能的同时保持了极高的推理效率，其计算消耗仅为 GLM 5.2 和 Qwen 3.8-Max 等同类性能模型的 1/3 至 1/4。

该模型的能力源于预训练和强化学习（RL）的大规模扩展。Beam 在 **23.8 万亿 token** 上进行了预训练，并经历了迄今为止规模最大的强化学习训练之一：使用 1.05 万颗 NVIDIA GB300 GPU，历时四周，在 100 万个环境中生成了 1 亿次轨迹（rollouts）。

**核心技术亮点：**
*   **性能表现：** Beam 在专项基准测试中表现卓越，在 AIME 2026 上得分为 97.8%，在 GPQA Diamond 上为 90.5%，在 SWEBench Verified 上为 80.9%。
*   **推理控制：** 独特的“推理力度”（reasoning effort）参数允许用户在快速、节省 token 的响应与针对复杂任务的深度扩展推理之间进行切换。
*   **基础设施创新：** Reflection 开发了一个完全异步的强化学习平台，即使在存在“策略陈旧”（即利用旧版本模型生成的数据进行学习）的情况下也能保持稳定性。
*   **泛化能力：** 尽管是纯文本模型，Beam 仍展现出强大的智能体迁移能力，能够成功执行网页调研、调用 OCR API，并自主微调其他模型（如 Gemma-4）。

目前 Beam 正在进行最后的红队测试，其权重、技术报告和开发者工具包计划于本月晚些时候发布。早期访问现已开放申请。

---

## 2. 查找旧金山任意两点间最平坦的路线。

**原文标题**: Find the flattest route between any two points in SF

**原文链接**: [https://flattensf.com/](https://flattensf.com/)

**Flatten SF** 由 Drew Edwards 开发，是一款专门的网页端路径规划工具，旨在通过寻找最平坦的路径，帮助行人和骑行者在旧金山著名的多山地形中穿行。

该应用程序直接在用户的浏览器中处理超过 160,000 条街道段，利用高分辨率的 USGS 1米激光雷达高程数据，并结合了 Overture 和 OpenStreetMap 的街道图。其核心功能是一个交互式滑块，允许用户在最短距离与最低海拔增益之间进行权衡。在极端的“平坦”设置下，算法会将 1 英尺的垂直爬升视作等同于 200 英尺的水平步行距离，以此来判断绕路是否值得。

该工具的主要特点包括：
*   **特定模式逻辑：** 该工具在步行路线中自动包含楼梯，但在骑行路线中将其排除。
*   **累积海拔：** 该工具计算总的累积爬升增益，而非仅仅测量起点和终点之间的高度差，从而更准确地反映体力消耗。
*   **基于浏览器的性能：** 该工具在本地执行计算，并内置了旧金山地址、地点和交叉路口的离线搜索功能。

通过提供从最直接到最平坦的一系列可视化路径选择，Flatten SF 让用户能够根据自己的体力偏好或骑行设备自定义通勤路线。

---

## 3. Dust: 无需反向传播的 Transformer 预训练

**原文标题**: Dust: Pretraining Transformers Without Backpropagation

**原文链接**: [https://qlabs.sh/research/dust](https://qlabs.sh/research/dust)

**Dust** 是一种用于预训练 Transformer 的新型零阶优化方法，它为反向传播提供了一个极具竞争力的替代方案。与扰动模型权重的传统演化策略 (ES) 不同，Dust 采用**节点扰动**，在每个 token 上独立地为激活值添加高斯噪声。这创建了一个“虚拟种群”，只需一次前向传播即可并行评估数千个成员，使其效率比 EGGROLL 等先进的权重空间 ES 方法高出 $10^3$ 到 $10^4$ 倍。

主要发现和贡献包括：
*   **性能：** Dust 是首个在预训练中能与反向传播相媲美的零阶方法，在算力充足的情况下甚至能超越后者。这表明随着可用算力的规模化，基于搜索的方法最终可能会取代反向传播。
*   **可扩展性：** 作者挑战了传统观点，发现大型模型实际上比小型模型具有更高的种群效率。即使在高达 10 亿 token 的规模下，梯度估计仍与反向传播保持高度一致。
*   **机制：** 该算法根据局部和未来 token 损失的降低程度来奖励激活扰动。它通过计算奖励加权噪声与层输入的外积来估计权重梯度。
*   **实现：** 为了管理同时扰动之间的干扰，Dust 在不同的前向传播中对不同类型的层进行扰动，并利用缓存的“干净”激活值来减少冗余计算。

这项研究暗示了学习算法将向更通用、更“暴力”的方向转变。通过摆脱对可微性的严格要求，Dust 为训练复杂架构（例如涉及外部程序或长循环 Transformer 的架构）敞开了大门，而这些架构目前难以使用反向传播进行优化。

---

## 4. Opus 5.5 智能体发现两种室温磁性半导体候选材料

**原文标题**: Opus 5.5 agents discover two room-temperature magnetic semiconductor candidates

**原文链接**: [https://www.vals.ai/blogs/room-temperature-magnetic-semiconductors](https://www.vals.ai/blogs/room-temperature-magnetic-semiconductors)

AI智能体 (Opus 5.5) 发现了两种属于“Luttinger补偿 (LC) 磁体”类别的室温磁性半导体候选材料。这些材料在自旋电子学和计算机存储领域备受青睐，因为它们兼具了铁磁体和反铁磁体的最佳特性：它们具有零净磁场（可实现更密集、更快速的存储），同时保持了按自旋对电子进行排序的能力（这是读写数据所必需的）。

确定的两种候选材料为：

1.  **YBaMnFeO₅：** 这是一种由AI设计的化合物，预测具有2.35 eV的带隙，且磁稳定性高达490 K。虽然它为数据存储提供了巨大的“自旋窗口”，但其合成可能较为困难，因为它需要精确的“棋盘式”原子排列，而这种排列在高温下往往会变得紊乱。
2.  **KV[Cr(CN)₆]：** 该材料于1999年首次合成，但此前未被识别为LC半导体。AI分析显示，它具有2.1 eV的带隙，并在高达376 K (103 °C) 的温度下保持磁有序。与第一种候选材料不同，其晶体结构能自然地将金属原子锁定在正确的位置，使其成为更具稳健性的实际应用候选材料。

研究得出结论，下一代非易失性存储器（特别是室温LC半导体）的关键可能已经存在于化学文献中，“就隐藏在显而易见之处”。研究人员已在GitHub上发布了数据和代码，邀请科学界重新合成KV[Cr(CN)₆]并直接测量其自旋排序性能。这一发现标志着向实用、高性能自旋技术迈出了重要一步。

---

## 5. 使用蓝光 M-Disk 作为终极备份

**原文标题**: Using Blu-ray M-Disk as Backup of Last Resort

**原文链接**: [https://smyck.net/2026/10/03/holocron-the-backup-of-last-resort/](https://smyck.net/2026/10/03/holocron-the-backup-of-last-resort/)

This article details a "last-resort" decentralized backup strategy using Blu-ray M-Discs for long-term data archival. Inspired by the practice of leaving spare house keys with trusted friends, the author proposes creating physical backup kits to survive catastrophic events, such as a fire, that might destroy both a primary computer and local backups.

**The Strategy**
The author stores "core essential data"—including digitized documents, music, photos, and "digital life" reboot files—on three M-Discs. Most critical data is password-protected. These discs are placed in a rugged B&W Outdoor Case (Type 500) and padded with non-degrading PE foam to prevent physical damage.

**Security and Maintenance**
To ensure the integrity of the backup while it is stored with a "custodian" (a trusted friend), the author employs several security measures:
*   **Tamper-Evident Seals:** Plastic seals with unique serial numbers and barcodes are used to lock the case. 
*   **Custom Labeling:** Personalized stickers help identify the unit.
*   **Handover Ceremony:** Every 1–3 years, the author replaces the case, inspecting the old seal for tampering before handing over a refreshed version.
*   **Environmental Protection:** Silica gel packs are included to monitor and prevent moisture buildup.

**The "Holocron"**
The author nicknames these units "Holocrons," referencing the information-storage devices from *Star Wars*. This method provides a secure, offline, and decentralized alternative to cloud storage, relying on durable physical media and a "web of trust" to ensure that essential data can be recovered even in a worst-case scenario.

---

## 6. Web Search API

**原文标题**: Web Search API

**原文链接**: [https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/](https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/)

生成摘要时出错

---

## 7. Worth Building

**原文标题**: Worth Building

**原文链接**: [https://armstr.ng/writing/worth-building](https://armstr.ng/writing/worth-building)

生成摘要时出错

---

## 8. Competitive Programmer's Handbook (2018) [pdf]

**原文标题**: Competitive Programmer's Handbook (2018) [pdf]

**原文链接**: [https://cses.fi/book/book.pdf](https://cses.fi/book/book.pdf)

生成摘要时出错

---

## 9. Example.com 刚刚推出了数十年来规模最大的改版

**原文标题**: Example.com Just Launched the Biggest Redesign in Decades

**原文链接**: [https://www.debugbear.com/blog/example-dot-com-redesign-history](https://www.debugbear.com/blog/example-dot-com-redesign-history)

生成摘要时出错

---

## 10. DEDA – Tracking Dots Extraction, Decoding and Anonymisation Toolkit

**原文标题**: DEDA – Tracking Dots Extraction, Decoding and Anonymisation Toolkit

**原文链接**: [https://github.com/dfd-tud/deda](https://github.com/dfd-tud/deda)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 2 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 3 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 4 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 5 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 6 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 7 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 8 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 9 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 10 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 11 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 12 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 13 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 14 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 15 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 16 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 17 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 18 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 19 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 20 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 21 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 22 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 23 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 24 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 25 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 26 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 27 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 28 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 29 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 30 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 31 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 32 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 33 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 34 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 35 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 36 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 37 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 38 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 39 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 40 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 41 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 42 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 43 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 44 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 45 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 46 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 47 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 48 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 49 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 50 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 51 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 52 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 53 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 54 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 55 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 56 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 57 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 58 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 59 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 60 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 61 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 62 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 63 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 64 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 65 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 66 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 67 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 68 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 69 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 70 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 71 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 72 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 73 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 74 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 75 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 76 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 77 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 78 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 79 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 80 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 81 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 82 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 83 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 84 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 85 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 86 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 87 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 88 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 89 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 90 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 91 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 92 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 93 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 94 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 95 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 96 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 97 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 98 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 99 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 100 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 101 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 102 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 103 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 104 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 105 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 106 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 107 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 108 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 109 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 110 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 111 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 112 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 113 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 114 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 115 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 116 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 117 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 118 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 119 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 120 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 121 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 122 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 123 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 124 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 125 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 126 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 127 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 128 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 129 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 130 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 131 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 132 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 133 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 134 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 135 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 136 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 137 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 138 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 139 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 140 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 141 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 142 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 143 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 144 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 145 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 146 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 147 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 148 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 149 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 150 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 151 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 152 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 153 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 154 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 155 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 156 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 157 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 158 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 159 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 160 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 161 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 162 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 163 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 164 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 165 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 166 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 167 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 168 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 169 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 170 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 171 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 172 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 173 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 174 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 175 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 176 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 177 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 178 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 179 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 180 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 181 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 182 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 183 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 184 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 185 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 186 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 187 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 188 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 189 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 190 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 191 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 192 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 193 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 194 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 195 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 196 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 197 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 198 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 199 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 200 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 201 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 202 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 203 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 204 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 205 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 206 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 207 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 208 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 209 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 210 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 211 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 212 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 213 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 214 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 215 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 216 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 217 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 218 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 219 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 220 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 221 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 222 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 223 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 224 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 225 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 226 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 227 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 228 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 229 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 230 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 231 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 232 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 233 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 234 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 235 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 236 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 237 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 238 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 239 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 240 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 241 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 242 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 243 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 244 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 245 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 246 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 247 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 248 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 249 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 250 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 251 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 252 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 253 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 254 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 255 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 256 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 257 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 258 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 259 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 260 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 261 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 262 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 263 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 264 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 265 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 266 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 267 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 268 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 269 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 270 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 271 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 272 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 273 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 274 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 275 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 276 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 277 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 278 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 279 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 280 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 281 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 282 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 283 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 284 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 285 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 286 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 287 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 288 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 289 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 290 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 291 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 292 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 293 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 294 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 295 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 296 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 297 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 298 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 299 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 300 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 301 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 302 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 303 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 304 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 305 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 306 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 307 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 308 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 309 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 310 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 311 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 312 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 313 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 314 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 315 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 316 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 317 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 318 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 319 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 320 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 321 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 322 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 323 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 324 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 325 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 326 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 327 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 328 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 329 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 330 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 331 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 332 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 333 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 334 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 335 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 336 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 337 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 338 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 339 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 340 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 341 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 342 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 343 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 344 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 345 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 346 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 347 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 348 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 349 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 350 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 351 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 352 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 353 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 354 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 355 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 356 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 357 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 358 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 359 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 360 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 361 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 362 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 363 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 364 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 365 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 366 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 367 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 368 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 369 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 370 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 371 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 372 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 373 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 374 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 375 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 376 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 377 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 378 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 379 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 380 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 381 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 382 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 383 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 384 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 385 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 386 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 387 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 388 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 389 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 390 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 391 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 392 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 393 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 394 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 395 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 396 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 397 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 398 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 399 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 400 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 401 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 402 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 403 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 404 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 405 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 406 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 407 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 408 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 409 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 410 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 411 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 412 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 413 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 414 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 415 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 416 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 417 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 418 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 419 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 420 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 421 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 422 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 423 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 424 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 425 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 426 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 427 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 428 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 429 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 430 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 431 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 432 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 433 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 434 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 435 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 436 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 437 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 438 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 439 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 440 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 441 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 442 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 443 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 444 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 445 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 446 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 447 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 448 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 449 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 450 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 451 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 452 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 453 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 454 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 455 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 456 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 457 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 458 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 459 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 460 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 461 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 462 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 463 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 464 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 465 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 466 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 467 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 468 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 469 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 470 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 471 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 472 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 473 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 474 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 475 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 476 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 477 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 478 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 479 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 480 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 481 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 482 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 483 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 484 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 485 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 486 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 487 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 488 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 489 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 490 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 491 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 492 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 493 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 494 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 495 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 496 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 497 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 498 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 499 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 500 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 501 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 502 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 503 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 504 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 505 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 506 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 507 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 508 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 509 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 510 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 511 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 512 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 513 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 514 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 515 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 516 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 517 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 518 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 519 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 520 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 521 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 522 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 523 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 524 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 525 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 526 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 527 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 528 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 529 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 530 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 531 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 532 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 533 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 534 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 535 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 536 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 537 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 538 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 539 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 540 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 541 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 542 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 543 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 544 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 545 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 546 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 547 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 548 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 549 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 550 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 551 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 552 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 553 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 554 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 555 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 556 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 557 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 558 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 559 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 560 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 561 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 562 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
