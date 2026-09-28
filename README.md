# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-09-28.md)

*最后自动更新时间: 2026-09-28 22:56:05*
## 1. Jeff – 兼容 Jev 的 0.8B 决策模型，在家训练，约 30 毫秒

**原文标题**: Jeff – Jev-compatible 0.8B decision models, trained at home, ~30 ms

**原文链接**: [https://github.com/firelex/jeff](https://github.com/firelex/jeff)

**Jeff** 是一套小型、高速决策模型系列（参数量为 0.8B 至 2B），专为零样本分类任务设计。Jeff 模型基于 Qwen3.5 和 Gemma 4 构建，兼容 Jev 请求格式，能够通过单次前向传播为用户定义的选项提供校准概率。通过消除文本生成和解析环节，它们实现了极高的效率，在 NVIDIA RTX PRO 6000 或 Apple M4 Max 等本地硬件上的决策处理时间仅需约 22–30 毫秒。

该项目突出了以下几个核心特性：
*   **零样本能力：** 模型可以对多种输入进行分类（如服务工单、用户意图或游戏动作），且无需训练数据中包含这些特定类别。
*   **本地与开放训练：** Jeff 完全在本地硬件上使用开源模型（Qwen-Flash）生成的合成数据构建而成。这是一个利用 MIT 许可的 AutoJev 配方的独立项目，模型权重按 Apache 2.0 协议发布。
*   **性能表现：** 在基准测试中，Jeff 在分类和接地（grounding）任务中的准确率接近甚至超过了体量更大的模型（如 27B 的 AutoJev）。然而，受限于较小的规模，它们在复杂的多步推理方面仍逊于大模型。
*   **专业化能力：** 虽然零样本性能强劲，但在经过简短的特定领域微调后，模型表现尤为出色；一项测试显示，仅需 30 分钟的训练，其准确率就从 31.7% 跃升至 95.8%。

开发者将 Jeff 定位为“系统 1”模型——即非常适合快速、直觉式的判断，而非复杂的规划。建议用户在使用时注意措辞（wording）的影响，并指出 0.8B 模型通常是速度与可靠性的“黄金平衡点”，在游戏等动态环境中，其表现有时甚至优于 2B 版本。

---

## 2. World Labs 加入 AMD

**原文标题**: World Labs Is Joining AMD

**原文链接**: [https://www.worldlabs.ai/blog/amd-announcement](https://www.worldlabs.ai/blog/amd-announcement)

World Labs 宣布已达成加入 AMD 的最终协议，此举旨在加速针对空间与物理世界的 AI 技术开发。此次收购是基于双方去年建立的深度技术合作伙伴关系，该合作专注于优化 AMD GPU 上的模型训练与推理。

关键领导层变动包括 AI 先驱李飞飞博士（Dr. Fei-Fei Li）加入 AMD 担任执行副总裁兼首席科学家，直接向首席执行官苏姿丰博士（Dr. Lisa Su）汇报。联合创始人 Justin Johnson 和 Ben Mildenhall 将继续领导 World Labs 团队，该团队在并入 AMD 后将组建一个新的前沿研究机构。

合并后的实体旨在构建一个涵盖硬件、软件、平台和易于获取的开放模型的全面、开放式 AI 生态系统。通过将 World Labs 的基础模型和应用与 AMD 的硬件能力相结合，两家公司意在更有效地扩展 AI 解决方案。

该交易预计将于 2026 年底完成，但需满足惯例成交条件并获得监管批准。

---

## 3. 紧跟前沿并非AI实验室的真正目标

**原文标题**: Pacing the Frontier is not the actual goal for AI labs

**原文链接**: [https://www.lesswrong.com/posts/Nm4ewbYovtjq69dvH/pacing-the-frontier-is-not-the-actual-goal-for-ai-labs](https://www.lesswrong.com/posts/Nm4ewbYovtjq69dvH/pacing-the-frontier-is-not-the-actual-goal-for-ai-labs)

In the article "Pacing the Frontier is not the actual goal for AI labs," the author argues that the common perception of the "AI race"—where labs compete to marginally outdo each other with incremental releases—is a misunderstanding of their true strategy.

According to the author, "pacing the frontier" (releasing models like GPT-4 or Claude 3) is merely a survival requirement to maintain relevance, secure talent, and attract capital. The actual goal is **discontinuous scaling**: positioning themselves to be the first to leapfrog the current frontier by orders of magnitude.

Key points include:

*   **Infrastructure as the Real Battlefield:** The true competition is not over software tweaks but over the massive physical infrastructure required for the next generation of AI. This includes securing unprecedented amounts of compute (chips), energy, and capital.
*   **The Compute Moat:** Labs are racing to build a "compute moat" so large that once they achieve a breakthrough, competitors will find it physically and financially impossible to catch up. The goal is a decisive, winner-take-all advantage.
*   **Maintenance vs. Breakthrough:** Current releases serve as "proofs of concept" to keep investors interested and to test safety protocols. However, these are just the "phoney war" stage of the race.
*   **Resource Accumulation:** The author suggests that labs are currently in a transition period, accumulating the necessary resources for a massive, non-linear shift in capabilities that will occur once their large-scale data centers are fully operational.

Ultimately, the article suggests that the current steady stream of AI updates masks a much more aggressive underlying race to build the industrial-scale foundation for super-intelligence.

---

## 4. Pirating the Pirates

**原文标题**: Pirating the Pirates

**原文链接**: [https://mubi.com/en/notebook/posts/pirating-the-pirates](https://mubi.com/en/notebook/posts/pirating-the-pirates)

生成摘要时出错

---

## 5. MicroLLM Lab – Try 7 tiny LLM's in the browser

**原文标题**: MicroLLM Lab – Try 7 tiny LLM's in the browser

**原文链接**: [https://stateofutopia.com/experiments/microllmlab/](https://stateofutopia.com/experiments/microllmlab/)

**MicroLLM Lab** 是一个交互式的网页端实验平台，旨在展示完全在用户浏览器中运行的“微型”大语言模型（LLM）的能力。该工具由 State of Utopia 开发，利用 **WebGPU** 技术进行本地推理，这意味着 AI 处理过程是在用户自身的硬件上完成的，而非远程服务器。

该实验室允许用户测试和对比七种不同的微型模型，参数规模通常在 1.35 亿到 5 亿之间。其中的特色模型包括 **SmolLM**、**Qwen2-0.5B** 和 **H2O-Danube** 的各种版本。通过专注于这些小规模模型，该平台证明了 AI 可以兼具实用、高效和私密，因为数据从未离开本地环境。

**核心功能与要点包括：**

*   **本地隐私与速度：** 由于模型通过浏览器的 WebGPU 接口运行，它们能提供低延迟响应，且无需将数据发送到外部 API。
*   **并排对比：** 用户只需输入一个提示词，即可同时查看不同微型模型的响应，从而直观展示模型规模与智能水平之间的权衡。
*   **高效性：** 该实验证明了轻量化模型（SLM）在处理摘要、简单逻辑和创意写作等基础任务方面能力日益增强，且能在笔记本电脑甚至智能手机等标准消费级设备上运行。

总而言之，MicroLLM Lab 为“本地 AI”运动提供了一个极具说服力的概念验证，将关注点从庞大且耗费资源的模型转向了优先考虑用户隐私和易用性的高效、去中心化替代方案。

---

## 6. 1.2万年前的哥贝克力石阵墓葬解释了散落骨骼的成因。

**原文标题**: 12,000-year-old Göbeklitepe burials explain scattered bones

**原文链接**: [https://archaeologymag.com/2026/09/gobeklitepe-burials-hundreds-of-scattered-bones/](https://archaeologymag.com/2026/09/gobeklitepe-burials-hundreds-of-scattered-bones/)

生成摘要时出错

---

## 7. Palantir founder purchases large swath of forest in Sweden

**原文标题**: Palantir founder purchases large swath of forest in Sweden

**原文链接**: [https://www.arctictoday.com/palantir-founder-purchases-large-swath-of-forest-in-sweden/](https://www.arctictoday.com/palantir-founder-purchases-large-swath-of-forest-in-sweden/)

生成摘要时出错

---

## 8. Scientists solve 1840s space weather mystery

**原文标题**: Scientists solve 1840s space weather mystery

**原文链接**: [https://arstechnica.com/science/2026/09/scientists-solve-1840s-space-weather-mystery/](https://arstechnica.com/science/2026/09/scientists-solve-1840s-space-weather-mystery/)

生成摘要时出错

---

## 9. Hijacking the PS5's RTMP stream

**原文标题**: Hijacking the PS5's RTMP stream

**原文链接**: [https://yashgarg.dev/posts/hijacking-ps5-rtmp-stream/](https://yashgarg.dev/posts/hijacking-ps5-rtmp-stream/)

生成摘要时出错

---

## 10. What reversing, modernising old games tells us about the economic impact of AI

**原文标题**: What reversing, modernising old games tells us about the economic impact of AI

**原文链接**: [https://this.os.isfine.org/blog/posts/what-reverse-engineering-and-modernising-an-old-war-game-tells-us-about-the-econ/](https://this.os.isfine.org/blog/posts/what-reverse-engineering-and-modernising-an-old-war-game-tells-us-about-the-econ/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 2 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 3 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 4 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 5 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 6 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 7 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 8 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 9 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 10 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 11 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 12 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 13 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 14 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 15 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 16 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 17 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 18 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 19 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 20 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 21 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 22 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 23 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 24 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 25 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 26 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 27 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 28 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 29 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 30 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 31 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 32 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 33 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 34 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 35 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 36 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 37 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 38 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 39 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 40 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 41 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 42 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 43 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 44 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 45 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 46 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 47 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 48 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 49 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 50 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 51 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 52 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 53 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 54 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 55 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 56 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 57 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 58 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 59 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 60 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 61 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 62 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 63 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 64 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 65 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 66 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 67 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 68 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 69 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 70 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 71 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 72 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 73 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 74 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 75 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 76 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 77 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 78 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 79 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 80 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 81 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 82 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 83 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 84 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 85 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 86 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 87 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 88 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 89 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 90 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 91 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 92 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 93 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 94 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 95 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 96 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 97 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 98 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 99 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 100 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 101 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 102 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 103 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 104 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 105 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 106 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 107 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 108 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 109 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 110 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 111 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 112 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 113 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 114 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 115 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 116 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 117 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 118 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 119 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 120 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 121 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 122 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 123 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 124 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 125 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 126 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 127 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 128 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 129 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 130 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 131 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 132 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 133 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 134 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 135 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 136 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 137 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 138 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 139 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 140 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 141 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 142 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 143 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 144 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 145 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 146 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 147 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 148 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 149 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 150 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 151 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 152 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 153 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 154 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 155 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 156 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 157 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 158 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 159 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 160 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 161 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 162 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 163 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 164 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 165 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 166 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 167 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 168 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 169 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 170 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 171 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 172 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 173 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 174 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 175 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 176 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 177 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 178 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 179 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 180 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 181 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 182 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 183 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 184 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 185 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 186 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 187 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 188 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 189 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 190 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 191 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 192 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 193 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 194 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 195 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 196 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 197 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 198 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 199 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 200 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 201 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 202 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 203 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 204 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 205 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 206 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 207 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 208 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 209 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 210 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 211 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 212 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 213 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 214 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 215 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 216 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 217 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 218 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 219 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 220 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 221 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 222 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 223 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 224 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 225 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 226 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 227 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 228 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 229 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 230 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 231 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 232 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 233 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 234 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 235 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 236 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 237 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 238 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 239 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 240 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 241 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 242 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 243 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 244 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 245 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 246 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 247 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 248 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 249 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 250 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 251 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 252 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 253 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 254 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 255 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 256 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 257 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 258 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 259 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 260 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 261 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 262 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 263 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 264 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 265 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 266 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 267 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 268 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 269 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 270 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 271 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 272 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 273 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 274 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 275 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 276 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 277 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 278 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 279 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 280 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 281 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 282 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 283 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 284 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 285 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 286 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 287 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 288 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 289 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 290 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 291 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 292 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 293 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 294 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 295 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 296 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 297 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 298 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 299 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 300 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 301 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 302 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 303 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 304 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 305 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 306 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 307 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 308 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 309 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 310 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 311 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 312 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 313 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 314 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 315 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 316 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 317 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 318 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 319 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 320 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 321 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 322 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 323 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 324 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 325 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 326 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 327 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 328 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 329 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 330 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 331 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 332 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 333 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 334 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 335 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 336 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 337 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 338 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 339 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 340 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 341 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 342 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 343 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 344 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 345 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 346 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 347 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 348 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 349 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 350 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 351 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 352 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 353 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 354 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 355 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 356 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 357 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 358 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 359 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 360 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 361 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 362 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 363 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 364 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 365 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 366 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 367 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 368 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 369 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 370 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 371 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 372 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 373 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 374 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 375 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 376 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 377 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 378 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 379 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 380 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 381 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 382 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 383 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 384 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 385 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 386 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 387 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 388 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 389 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 390 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 391 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 392 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 393 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 394 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 395 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 396 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 397 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 398 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 399 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 400 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 401 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 402 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 403 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 404 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 405 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 406 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 407 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 408 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 409 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 410 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 411 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 412 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 413 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 414 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 415 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 416 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 417 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 418 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 419 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 420 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 421 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 422 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 423 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 424 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 425 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 426 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 427 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 428 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 429 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 430 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 431 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 432 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 433 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 434 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 435 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 436 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 437 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 438 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 439 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 440 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 441 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 442 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 443 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 444 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 445 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 446 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 447 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 448 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 449 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 450 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 451 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 452 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 453 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 454 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 455 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 456 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 457 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 458 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 459 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 460 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 461 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 462 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 463 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 464 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 465 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 466 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 467 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 468 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 469 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 470 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 471 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 472 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 473 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 474 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 475 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 476 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 477 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 478 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 479 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 480 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 481 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 482 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 483 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 484 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 485 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 486 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 487 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 488 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 489 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 490 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 491 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 492 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 493 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 494 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 495 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 496 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 497 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 498 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 499 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 500 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 501 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 502 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 503 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 504 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 505 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 506 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 507 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 508 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 509 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 510 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 511 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 512 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 513 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 514 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 515 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 516 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 517 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 518 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 519 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 520 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 521 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 522 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 523 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 524 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 525 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 526 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 527 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 528 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 529 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 530 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 531 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 532 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 533 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 534 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 535 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 536 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 537 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 538 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 539 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 540 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 541 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 542 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 543 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 544 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 545 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 546 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 547 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 548 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 549 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 550 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 551 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 552 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 553 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 554 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 555 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
