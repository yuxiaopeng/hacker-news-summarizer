# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-09-16.md)

*最后自动更新时间: 2026-09-16 20:21:02*
## 1. 向量化且性能可移植的快速排序

**原文标题**: Vectorized and performance-portable Quicksort

**原文链接**: [https://opensource.googleblog.com/2022/06/Vectorized%20and%20performance%20portable%20Quicksort.html](https://opensource.googleblog.com/2022/06/Vectorized%20and%20performance%20portable%20Quicksort.html)

研究人员开发了一种矢量化、性能可移植的快速排序（Quicksort）实现，其性能比 C++ 标准库（`std::sort`）快 10 到 19 倍。尽管排序在传统上一直是计算瓶颈，但这种新方法利用 SIMD（单指令多数据）指令，大幅加速了算法的划分阶段。

**关键技术创新：**
该实现利用现代指令集（如 AVX-512 和 Arm SVE）中的“压缩存储”（compress-store）指令，根据基准值快速将元素过滤到子数组中。为了确保可移植性，研究人员使用了 **Highway** SIMD 库，使代码能够在六种不同的指令集（包括 AVX2、AVX-512 和 Arm NEON）上高效运行，而无需针对每种架构进行手动重新优化。在缺乏“压缩存储”指令的旧硬件上，该库通过排列（permute）指令模拟该功能。

**性能与通用性：**
*   **高吞吐量：** 该算法在 Intel Skylake (AVX-512) 上的处理速度达到约 1.1 GB/s，在 Apple M1 (NEON) 上接近 500 MB/s。
*   **广泛支持：** 与以往仅限于 32 位整数的专用排序算法不同，该版本支持 16 位到 128 位的全范围输入。
*   **高效性：** 它甚至优于现有的针对特定架构的最先进算法，例如仅针对 AVX2 优化的算法。

**重要意义：**
这一突破对于列式数据库尤为重要，因为快速排序和过滤是高性能 SQL 查询的核心需求。通过在单个 CPU 核心上实现 1 GB/s 的处理能力，该实现为数据处理开辟了新的可能性。该项目基于 Apache2 协议开源，并已在 GitHub 上发布。

---

## 2. Training a 4B model to produce 81% faster query plans than Postgres

**原文标题**: Training a 4B model to produce 81% faster query plans than Postgres

**原文链接**: [https://rohanbansal.com/qorl](https://rohanbansal.com/qorl)

This article documents a successful experiment in which a 4B-parameter language model was trained to outperform the Postgres query optimizer, achieving a **44.7% reduction in latency** across 113 join-heavy queries.

The author identifies that while query optimization—specifically **join ordering**—is an NP-hard problem, it is an ideal candidate for Reinforcement Learning (RL) because the output is easily verifiable: a "good" plan is simply one that runs faster. Traditional optimizers like Postgres struggle with the **combinatorial explosion** of possible plans. For a query with nine tables, factors such as join trees, inner/outer orientations, algorithms (hash vs. merge), and scan types (sequential vs. index) result in quadrillions of potential execution paths.

**Key methodology and technical highlights include:**
*   **Post-Training:** The model underwent Supervised Fine-Tuning (SFT) followed by agentic RL.
*   **GRPO Variant:** The author designed a custom variant of Group Relative Policy Optimization to score RL rollouts in a noisy environment.
*   **Noise Reduction:** To ensure accurate benchmarking, a custom Postgres rig was built to minimize Linux page cache contention across concurrent containers.
*   **Distributed Training:** The setup utilized vLLM and a trainer on a remote 2x H100 node, while the Postgres execution environment ran on local hardware.
*   **Distillation:** The process incorporated off-policy distillation from high-quality agent trajectories.

The experiment demonstrates that a small, open-weights model can learn to navigate massive search spaces more effectively than traditional heuristic-based or dynamic programming optimizers. By focusing on the single axis of execution time, the model evolved from being unable to produce valid plans to consistently beating Postgres’s default selections.

---

## 3. Small programming tricks

**原文标题**: Small programming tricks

**原文链接**: [https://will-keleher.com/posts/small-programming-tricks-matter/](https://will-keleher.com/posts/small-programming-tricks-matter/)

生成摘要时出错

---

## 4. AMD 矩阵核心的精确模型

**原文标题**: Accurate Models of AMD Matrix Cores

**原文链接**: [https://arxiv.org/abs/2609.14845](https://arxiv.org/abs/2609.14845)

《AMD 矩阵核心的精确模型》针对 GPU 矩阵乘法器缺乏标准化和文档记录的问题进行了研究，这些硬件通常偏离 IEEE 754 浮点标准。由于累加器宽度、舍入行为和次正规数处理等特性在不同厂商及代际之间存在差异，仅通过软件往往无法在不同设备间实现位级可复现性。

研究人员表征了三种 AMD 架构的数值行为：CDNA 1 (MI100)、CDNA 2 (MI210/250) 和 CDNA 3 (MI300A/X)。为了逆向推导这些未公开的实现细节，作者设计了特定的测试向量，以探测所有支持的输入格式下的数值特性。随后，他们为每种架构开发了基于 MATLAB 的软件模型。

为确保位级准确性，作者采用了迭代精化技术。他们利用包含 1000 万个输入向量的随机化测试集，针对硬件对模型进行了验证，不断完善逻辑，直到软件模型在所有情况下都与硬件输出完全匹配。

最后，作者通过对比分析 AMD 矩阵核心与 NVIDIA Tensor Core 的应用级精度，展示了这些模型的实用价值。这项工作为理解特定硬件的数值差异提供了一个框架，并为高性能计算和数学软件领域更精确的实验研究奠定了基础。

---

## 5. 通胀担忧推高债券收益率，美联储加息。

**原文标题**: Fed hikes rates as inflation worries push up bond yields

**原文链接**: [https://www.reuters.com/live/live-fed-rate-hike-expected-inflation-worries-push-up-bond-yields-2026-09-16/](https://www.reuters.com/live/live-fed-rate-hike-expected-inflation-worries-push-up-bond-yields-2026-09-16/)

无法访问文章链接。

---

## 6. Dream-RSI：通过演化世界实现递归自我提升

**原文标题**: Dream-RSI: Recursive Self-Improvement through Evolving Worlds

**原文链接**: [https://arxiv.org/abs/2609.14858](https://arxiv.org/abs/2609.14858)

摘要生成失败

---

## 7. Mistral X Mozilla：私密、多语言 AI 浏览

**原文标题**: Mistral X Mozilla: Private, Multilingual AI Browsing

**原文链接**: [https://mistral.ai/news/mistral-x-mozilla/](https://mistral.ai/news/mistral-x-mozilla/)

Mistral 和 Mozilla 宣布建立战略合作伙伴关系，将 Mistral 的 AI 模型集成到一款全新的 AI 驱动浏览助手——**Firefox Smart Window** 中。Smart Window 目前处于测试阶段，旨在帮助用户进行复杂搜索、调取已访问页面的信息，并根据当前活动的浏览器标签页获取数据。

此次合作聚焦于四大核心支柱：

*   **开放分发：** 推动开源 AI 成为封闭、专有系统的可行且透明的替代方案。
*   **文化本土化：** 针对地区语言、方言和文化背景对模型进行微调，确保 AI 能够理解当地的细微差别，而非提供“千篇一律”的体验。
*   **隐私与控制：** 秉持 Mozilla 隐私至上的标准。默认情况下，对话不会保存在 Mozilla 的服务器上，且 Mistral 已承诺执行零数据保留政策。
*   **主权 AI：** 将企业级、高掌控的技术延伸至普通消费者，确保用户对自己的浏览体验拥有自主权。

该集成功能将率先面向**法国和北美**用户推出，并预计于 2026 年晚些时候在**英国和德国**上线。

Mozilla 首席执行官 Anthony Enzor-DeMeo 和 Mistral 首席执行官 Arthur Mensch 强调，此次合作旨在防止互联网变成由少数几家主导科技公司控制的“单向漏斗”。通过优先考虑选择权和开放技术，他们力求在提供原生于浏览器的私密、多语言 AI 体验的同时，维护互联网探索与发现的核心价值。

---

## 8. Tell the speakers that you liked their talks

**原文标题**: Tell the speakers that you liked their talks

**原文链接**: [https://ohhelloana.blog/tell-the-speakers/](https://ohhelloana.blog/tell-the-speakers/)

在这篇文章中，Ana Rodrigues 反思了她在 SmashingConf 和 CSS Day 等会议上的近期经历，强调了参会者向演讲者提供反馈的需求正日益增长。

Rodrigues 观察到“演讲圈”已经发生了变化，并指出 Twitter 等平台的衰落造成了反馈真空。由于失去了演讲者曾经依赖的即时在线评论浪潮，许多人陷入了自我怀疑，纳闷自己的演讲是引起了共鸣，还是反应平平。她坦诚地分享道，尽管她有担任主持人和演讲者的丰富经验，但她仍会受到冒名顶替综合征、害羞以及演讲后对表现产生的焦虑所困扰。

为了弥补这一鸿沟，Rodrigues 描述了她如何积极促成“吃豆人式”的小组对话，帮助害羞的参会者克服在接触演讲者时的畏缩心理。她强调，演讲者也“只是普通人”，他们感受到的紧张情绪往往不亚于那些想与他们交谈的观众。

文章最后向参会者发出了直接呼吁：**如果你喜欢他们的演讲，请告诉演讲者。** 无论是当面的一句简单赞美，还是网络上的一条发布，这种反馈都至关重要。它肯定了准备演讲所付出的巨大努力，并为那些往往对自己最为苛刻的演讲者提供了急需的宽慰。

---

## 9. Show HN: An e-ink frame that hears birds and draws them as 1800s illustrations

**原文标题**: Show HN: An e-ink frame that hears birds and draws them as 1800s illustrations

**原文链接**: [https://github.com/arnegiacomo/fugleramme](https://github.com/arnegiacomo/fugleramme)

生成摘要时出错

---

## 10. The Siberian Ice Maiden and the Scythian World

**原文标题**: The Siberian Ice Maiden and the Scythian World

**原文链接**: [https://patrickwyman.substack.com/p/the-siberian-ice-maiden-and-the-scythian](https://patrickwyman.substack.com/p/the-siberian-ice-maiden-and-the-scythian)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 2 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 3 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 4 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 5 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 6 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 7 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 8 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 9 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 10 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 11 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 12 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 13 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 14 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 15 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 16 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 17 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 18 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 19 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 20 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 21 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 22 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 23 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 24 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 25 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 26 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 27 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 28 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 29 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 30 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 31 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 32 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 33 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 34 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 35 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 36 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 37 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 38 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 39 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 40 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 41 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 42 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 43 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 44 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 45 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 46 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 47 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 48 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 49 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 50 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 51 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 52 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 53 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 54 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 55 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 56 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 57 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 58 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 59 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 60 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 61 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 62 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 63 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 64 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 65 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 66 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 67 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 68 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 69 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 70 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 71 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 72 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 73 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 74 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 75 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 76 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 77 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 78 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 79 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 80 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 81 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 82 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 83 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 84 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 85 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 86 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 87 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 88 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 89 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 90 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 91 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 92 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 93 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 94 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 95 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 96 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 97 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 98 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 99 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 100 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 101 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 102 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 103 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 104 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 105 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 106 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 107 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 108 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 109 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 110 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 111 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 112 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 113 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 114 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 115 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 116 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 117 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 118 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 119 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 120 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 121 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 122 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 123 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 124 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 125 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 126 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 127 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 128 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 129 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 130 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 131 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 132 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 133 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 134 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 135 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 136 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 137 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 138 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 139 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 140 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 141 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 142 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 143 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 144 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 145 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 146 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 147 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 148 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 149 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 150 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 151 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 152 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 153 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 154 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 155 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 156 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 157 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 158 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 159 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 160 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 161 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 162 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 163 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 164 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 165 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 166 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 167 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 168 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 169 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 170 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 171 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 172 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 173 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 174 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 175 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 176 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 177 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 178 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 179 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 180 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 181 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 182 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 183 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 184 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 185 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 186 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 187 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 188 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 189 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 190 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 191 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 192 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 193 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 194 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 195 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 196 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 197 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 198 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 199 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 200 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 201 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 202 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 203 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 204 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 205 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 206 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 207 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 208 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 209 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 210 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 211 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 212 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 213 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 214 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 215 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 216 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 217 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 218 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 219 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 220 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 221 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 222 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 223 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 224 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 225 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 226 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 227 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 228 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 229 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 230 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 231 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 232 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 233 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 234 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 235 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 236 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 237 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 238 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 239 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 240 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 241 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 242 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 243 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 244 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 245 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 246 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 247 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 248 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 249 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 250 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 251 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 252 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 253 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 254 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 255 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 256 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 257 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 258 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 259 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 260 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 261 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 262 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 263 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 264 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 265 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 266 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 267 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 268 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 269 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 270 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 271 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 272 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 273 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 274 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 275 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 276 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 277 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 278 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 279 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 280 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 281 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 282 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 283 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 284 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 285 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 286 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 287 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 288 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 289 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 290 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 291 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 292 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 293 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 294 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 295 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 296 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 297 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 298 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 299 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 300 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 301 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 302 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 303 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 304 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 305 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 306 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 307 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 308 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 309 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 310 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 311 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 312 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 313 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 314 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 315 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 316 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 317 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 318 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 319 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 320 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 321 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 322 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 323 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 324 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 325 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 326 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 327 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 328 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 329 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 330 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 331 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 332 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 333 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 334 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 335 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 336 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 337 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 338 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 339 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 340 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 341 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 342 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 343 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 344 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 345 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 346 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 347 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 348 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 349 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 350 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 351 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 352 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 353 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 354 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 355 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 356 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 357 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 358 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 359 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 360 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 361 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 362 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 363 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 364 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 365 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 366 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 367 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 368 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 369 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 370 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 371 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 372 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 373 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 374 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 375 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 376 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 377 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 378 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 379 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 380 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 381 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 382 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 383 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 384 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 385 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 386 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 387 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 388 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 389 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 390 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 391 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 392 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 393 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 394 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 395 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 396 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 397 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 398 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 399 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 400 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 401 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 402 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 403 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 404 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 405 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 406 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 407 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 408 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 409 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 410 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 411 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 412 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 413 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 414 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 415 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 416 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 417 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 418 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 419 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 420 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 421 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 422 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 423 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 424 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 425 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 426 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 427 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 428 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 429 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 430 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 431 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 432 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 433 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 434 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 435 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 436 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 437 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 438 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 439 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 440 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 441 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 442 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 443 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 444 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 445 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 446 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 447 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 448 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 449 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 450 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 451 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 452 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 453 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 454 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 455 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 456 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 457 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 458 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 459 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 460 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 461 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 462 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 463 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 464 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 465 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 466 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 467 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 468 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 469 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 470 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 471 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 472 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 473 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 474 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 475 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 476 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 477 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 478 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 479 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 480 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 481 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 482 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 483 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 484 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 485 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 486 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 487 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 488 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 489 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 490 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 491 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 492 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 493 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 494 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 495 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 496 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 497 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 498 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 499 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 500 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 501 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 502 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 503 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 504 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 505 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 506 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 507 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 508 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 509 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 510 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 511 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 512 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 513 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 514 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 515 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 516 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 517 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 518 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 519 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 520 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 521 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 522 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 523 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 524 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 525 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 526 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 527 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 528 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 529 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 530 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 531 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 532 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 533 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 534 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 535 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 536 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 537 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 538 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 539 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 540 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 541 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 542 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 543 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
