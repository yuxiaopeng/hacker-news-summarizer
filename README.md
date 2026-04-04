# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-04.md)

*最后自动更新时间: 2026-04-04 18:05:11*
## 1. Show HN：一款构建 GPU 的游戏

**原文标题**: Show HN: A game where you build a GPU

**原文链接**: [https://jaso1024.com/mvidia/](https://jaso1024.com/mvidia/)

**Mvidia** 是一款近期在“Show HN”上亮相的教育类模拟游戏。该游戏要求玩家从零开始，设计并构建一个功能完整的图形处理器（GPU）。

游戏专注于计算机架构和数字逻辑的核心原理。玩家从基础组件入手，必须应对硬件工程的复杂挑战，从而创造出能够处理图形任务的处理器。其核心体验包括：

*   **底层设计：** 玩家通过逻辑门、寄存器和指令集进行操作，直观了解硬件如何执行软件命令。
*   **并行处理：** 游戏的一个中心主题是掌握并行计算——这是现代 GPU 架构的标志，旨在优化数据吞吐量和渲染速度。
*   **资源管理：** 玩家必须在性能与各种限制之间取得平衡，迫使他们像现实中的硬件工程师一样，为了效率不断优化设计。
*   **教育进阶：** 游戏架起了抽象计算机科学理论与实际应用之间的桥梁，使普通爱好者和学生也能理解 GPU 技术这一“黑盒”。

通过将硬件综合过程游戏化，**Mvidia** 提供了一种独特的、迭代式的解谜体验，揭开了驱动现代计算机图形所需的专业工程技术的神秘面纱。

---

## 2. 简单的自蒸馏提升代码生成能力

**原文标题**: Simple self-distillation improves code generation

**原文链接**: [https://arxiv.org/abs/2604.01193](https://arxiv.org/abs/2604.01193)

论文“**极其简单的自蒸馏提升代码生成能力**”介绍了**简单自蒸馏 (SSD)**，这是一种用于提升大语言模型 (LLM) 代码生成性能的精简方法。与传统方法不同，SSD 不需要外部验证器、教师模型或强化学习。相反，它完全依赖于模型自身的原始输出。

**方法**
SSD 流程包含两个简单的步骤：
1. **采样**：利用特定的温度和截断设置从模型中生成解题方案。
2. **微调**：使用标准的监督微调 (SFT)，在模型自身生成的样本上对其进行重新训练。

**主要结果**
作者展示了显著的性能飞跃，最引人注目的是在 LiveCodeBench v6 基准测试中，将 **Qwen3-30B-Instruct** 的 **pass@1** 准确率从 42.4% 提升至 **55.3%**。研究发现，这些增益在更难的编程问题上最为显著。此外，该方法在不同的模型系列（Qwen 和 Llama）及规模（4B、8B 和 30B）上均表现出良好的泛化性，涵盖了标准指令版和“思考”版变体。

**理论洞察**
为了解释为何如此简单的方法行之有效，研究人员指出了 LLM 解码中的“**精度-探索冲突 (precision-exploration conflict)**”。他们表明，SSD 以一种依赖上下文的方式重塑了 Token 分布：在精度至关重要的场景下，它会抑制“干扰尾部”（错误或无关的 Token）；同时，它保留了模型探索不同逻辑路径所需的多样性。

**结论**
SSD 代表了一个极具易用性且互补的训练后改进方向。它证明了 LLM 能够通过本质上的“自我学习”，在无需复杂的外部监督或奖励建模的情况下，显著提高其推理和编码能力。

---

## 3. 单次提交新增 12,000 篇 AI 生成的博客文章

**原文标题**: 12,000 AI-generated blog posts added in a single commit

**原文链接**: [https://github.com/OneUptime/blog/commit/30cd2384794c897d95aca77d173db44af51ca849](https://github.com/OneUptime/blog/commit/30cd2384794c897d95aca77d173db44af51ca849)

这段内容详细记录了 **OneUptime/blog** 公共 GitHub 仓库的一次大规模更新：在单次提交中，该仓库增加了约 **12,000 篇由 AI 生成的博文**。仓库数据显示，此次更新涉及超过 **5,000 个文件变更**，新增代码行数超过 **716,000 行**。

此次提交的特点是包含了大量详尽的技术“操作指南”和故障排除文章，且几乎完全围绕开源分析型数据库 **ClickHouse** 展开。文件标题遵循高度系统化和程序化的命名规范，涵盖以下内容：

*   **错误修复：** 针对特定代码的指南（例如“如何修复代码 60 表不存在”）。
*   **配置说明：** 有关设置缓存、SSL 证书和分布式 DDL 的指令。
*   **功能教程：** 对特定引擎（如 MergeTree、ReplicatedMergeTree）和函数（如窗口函数、数组处理）的解释。
*   **技术对比：** 将 ClickHouse 与 Apache Pinot、Snowflake 和 BigQuery 等其他技术进行对比的文章。

**关键观察：**
*   **SEO 策略：** 庞大的篇幅和极具针对性的标题表明，这是一种激进的 SEO 手段，旨在捕捉针对 ClickHouse 相关的所有潜在查询或错误消息的搜索流量。
*   **未来日期：** 文件名标注的日期为 **2026 年 3 月 31 日**，这表明内容可能是为了日后逐步发布而准备的，或者是为长期定时发布流程批量生成的。
*   **自动化资产：** 许多文件夹都包含标准化的“social-media.png”素材，这进一步说明了其背后是一个完全自动化的内容生产工作流。

这一事件凸显了技术营销领域的一个重要趋势：利用生成式 AI 实现对某一软件细分领域的“全面覆盖”，从而有效地将博客转变为一个自动化的、经过搜索优化的技术手册。

---

## 4. Show HN: TurboQuant-WASM —— 浏览器中的谷歌向量量化技术

**原文标题**: Show HN: TurboQuant-WASM – Google's vector quantization in the browser

**原文链接**: [https://github.com/teamchong/turboquant-wasm](https://github.com/teamchong/turboquant-wasm)

**TurboQuant-WASM** 是 Google Research 在 ICLR 2026 上发表的 “TurboQuant” 向量量化算法的实验性 WebAssembly (WASM) 实现。该项目专为浏览器和 Node.js 环境中的高性能需求而设计，为向量检索、图像相似度计算和 3D 高斯泼溅 (3D Gaussian Splatting) 等应用提供了一种压缩高维向量的高效方案。

**核心技术特性：**
*   **性能：** 利用支持 **Relaxed SIMD**（单指令多数据流）的 WASM 优化数学运算，特别是通过映射融合乘加 (FMA) 操作来加速处理。
*   **效率：** 在保持内积（点积）精度的同时，实现了约 **6 倍的压缩率**（每维度约 4.5 比特）。
*   **功能：** 核心优势在于能够**直接在压缩数据上进行快速点积计算**，而无需预先解码。
*   **兼容性：** 提供 TypeScript API，并兼容 Chrome 114+、Firefox 128+、Safari 18+ 以及 Node.js 20+ 等现代环境。

该实现以 npm 包的形式分发，并确保“黄金值 (golden-value)”一致性，即其输出与原始 Zig 参考实现逐字节一致。本项目采用 MIT 许可证开源，基于 Google Research 的研究成果及开发者 botirk38 的原始 Zig 移植版本构建。

---

## 5. Show HN: sllm – 与其他开发者共享 GPU 节点，无限 Token

**原文标题**: Show HN: sllm – Split a GPU node with other developers, unlimited tokens

**原文链接**: [https://sllm.cloud](https://sllm.cloud)

**sllm** 是一个在 Hacker News 上推出的面向开发者的平台，它允许用户共享 GPU 节点，以降低运行大语言模型（LLM）的高昂成本。通过在多名开发者之间分配硬件资源，该服务以比租用专用私有实例更实惠的价格，提供了高性能计算访问能力。

该平台的核心价值主张是其**“无限 Token”**模式。与许多按量计费（按 Token 计费）的 AI 供应商不同，sllm 提供了一种可预测的成本结构。这种模式对于在实验或生产中需要持续、高强度使用 GPU 算力的开发者尤为有利，因为它消除了费用波动带来的经济负担，也免去了管理自有基础设施的额外开销。

本质上，sllm 旨在通过构建一个协作环境，让开发者能够利用共享硬件处理大模型任务，从而实现 GPU 资源的普及化。

---

## 6. 奇特的树木

**原文标题**: Some Unusual Trees

**原文链接**: [https://thoughts.wyounas.com/p/some-unusual-trees](https://thoughts.wyounas.com/p/some-unusual-trees)

在《一些奇特的树木》（Some Unusual Trees）中，瓦卡斯·尤纳斯（Waqas Younas）分享了他在第15版《大英百科全书》中发现的引人入胜的植物学发现。文章重点介绍了几种打破常规生长与生存预期的树种。

核心亮点包括：
*   **独特的生长模式：** 红树林通过向海生长来保护海岸线。榕树（如占地5.41英亩的 Thimmamma Marrimanu）从树枝上垂下气根以形成新的树干，使单棵树看起来犹如一片森林。
*   **专门的功能：** 马达加斯加的旅人蕉在叶柄基部储存水分；贝叶棕则需要长达75年的时间为一生仅有一次的开花做准备，随后便会枯死。海椰子则以产出世界上最大、最重的种子而闻名。
*   **记录保持者：** 北美红杉被公认为地球上最高的树种，而澳洲杏仁桉则是最高的开花植物。
*   **寿命与规模：** 刺果松是已知最古老的单体树，寿命超过4800年。此外，文章还探讨了“克隆”生物：**Old Tjikko**，一棵通过古老根系不断再生新树干的9568岁云杉；以及**Pando**，一个占地106英亩、由4.7万个树干组成的群体，它们作为一个庞大的单一生命体运行。

尤纳斯在结尾表示，这些“自然奇观”激发了他进一步探索树木学的兴趣，并邀请读者分享该领域的其他资源。

---

## 7. 苹果批准了使 Nvidia eGPU 兼容 Arm Mac 的驱动程序

**原文标题**: Apple approves driver that lets Nvidia eGPUs work with Arm Macs

**原文链接**: [https://www.theverge.com/tech/907003/apple-approves-driver-that-lets-nvidia-egpus-work-with-arm-macs](https://www.theverge.com/tech/907003/apple-approves-driver-that-lets-nvidia-egpus-work-with-arm-macs)

Apple has officially approved and signed a third-party driver developed by **Tiny Corp** that enables Nvidia and AMD eGPUs to work with Apple Silicon (Arm-based) Macs.

The most significant aspect of this approval is that users no longer need to disable Apple’s **System Integrity Protection (SIP)** to use external GPUs, maintaining the device's security framework. However, there are several key limitations to this release:

*   **Not Plug-and-Play:** The driver is not a standard consumer install; users must currently compile it using Docker.
*   **Target Audience:** It is specifically designed for accelerating Large Language Models (LLMs) rather than gaming or general graphic design.
*   **Third-Party Development:** The driver was created by Tiny Corp, not Nvidia or Apple themselves.

While this does not signal a full return to official Nvidia support for macOS, it marks a major breakthrough for AI developers wanting to leverage powerful external hardware on the Mac platform without compromising system security.

---

## 8. Author of "Careless People" banned from saying anything negative about Meta

**原文标题**: Author of "Careless People" banned from saying anything negative about Meta

**原文链接**: [https://www.thetimes.com/uk/technology-uk/article/sarah-wynn-williams-careless-people-meta-nrffdfpmf](https://www.thetimes.com/uk/technology-uk/article/sarah-wynn-williams-careless-people-meta-nrffdfpmf)

生成摘要时出错

---

## 9. 代码智能体的组成部分

**原文标题**: Components of a Coding Agent

**原文链接**: [https://magazine.sebastianraschka.com/p/components-of-a-coding-agent](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent)

生成摘要时出错

---

## 10. Artemis II crew take “spectacular” image of Earth

**原文标题**: Artemis II crew take “spectacular” image of Earth

**原文链接**: [https://www.bbc.com/news/articles/ce8jzr423p9o](https://www.bbc.com/news/articles/ce8jzr423p9o)

The Artemis II crew has reached the halfway point of their journey to the Moon, marking the first time humans have traveled beyond Earth’s orbit since 1972. NASA recently released a series of "spectacular" high-resolution images taken from the Orion spacecraft, including a standout photo titled "Hello, World." Captured by Commander Reid Wiseman, the images showcase the Atlantic Ocean, polar auroras, the "terminator" (the divide between day and night), and the twinkling lights of Earth against the darkness of space.

The milestone was reached approximately two days and five hours after launching from the Kennedy Space Center. At the halfway mark, the spacecraft was situated roughly 142,000 miles from Earth and 132,000 miles from the Moon. Astronaut Christina Koch described the crew’s "expression of joy" upon hitting the milestone, while mission specialist Jeremy Hansen noted that the crew remained "glued to the windows" to witness the views. Wiseman noted that capturing the photos was initially challenging due to exposure settings and even jokingly asked mission control for advice on cleaning windows smudged by the crew’s excitement.

To commemorate the mission, NASA shared a side-by-side comparison of Earth as seen in 1972 during the Apollo 17 mission and the current 2026 perspective, highlighting how much technology has advanced while our "home" remains gorgeous.

The Artemis II mission is currently on a looping trajectory following a successful trans-lunar injection burn. The four-person crew is expected to pass around the far side of the Moon on April 6, with the mission concluding in a splashdown in the Pacific Ocean on April 10.

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 2 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 3 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 4 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 5 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 6 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 7 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 8 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 9 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 10 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 11 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 12 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 13 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 14 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 15 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 16 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 17 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 18 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 19 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 20 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 21 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 22 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 23 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 24 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 25 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 26 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 27 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 28 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 29 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 30 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 31 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 32 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 33 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 34 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 35 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 36 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 37 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 38 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 39 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 40 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 41 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 42 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 43 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 44 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 45 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 46 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 47 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 48 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 49 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 50 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 51 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 52 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 53 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 54 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 55 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 56 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 57 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 58 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 59 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 60 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 61 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 62 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 63 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 64 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 65 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 66 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 67 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 68 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 69 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 70 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 71 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 72 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 73 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 74 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 75 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 76 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 77 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 78 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 79 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 80 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 81 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 82 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 83 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 84 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 85 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 86 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 87 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 88 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 89 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 90 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 91 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 92 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 93 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 94 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 95 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 96 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 97 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 98 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 99 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 100 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 101 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 102 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 103 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 104 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 105 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 106 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 107 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 108 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 109 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 110 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 111 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 112 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 113 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 114 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 115 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 116 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 117 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 118 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 119 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 120 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 121 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 122 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 123 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 124 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 125 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 126 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 127 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 128 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 129 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 130 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 131 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 132 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 133 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 134 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 135 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 136 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 137 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 138 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 139 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 140 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 141 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 142 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 143 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 144 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 145 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 146 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 147 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 148 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 149 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 150 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 151 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 152 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 153 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 154 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 155 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 156 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 157 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 158 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 159 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 160 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 161 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 162 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 163 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 164 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 165 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 166 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 167 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 168 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 169 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 170 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 171 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 172 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 173 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 174 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 175 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 176 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 177 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 178 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 179 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 180 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 181 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 182 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 183 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 184 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 185 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 186 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 187 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 188 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 189 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 190 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 191 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 192 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 193 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 194 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 195 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 196 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 197 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 198 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 199 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 200 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 201 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 202 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 203 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 204 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 205 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 206 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 207 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 208 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 209 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 210 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 211 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 212 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 213 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 214 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 215 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 216 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 217 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 218 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 219 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 220 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 221 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 222 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 223 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 224 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 225 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 226 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 227 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 228 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 229 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 230 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 231 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 232 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 233 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 234 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 235 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 236 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 237 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 238 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 239 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 240 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 241 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 242 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 243 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 244 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 245 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 246 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 247 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 248 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 249 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 250 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 251 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 252 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 253 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 254 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 255 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 256 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 257 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 258 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 259 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 260 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 261 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 262 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 263 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 264 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 265 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 266 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 267 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 268 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 269 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 270 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 271 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 272 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 273 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 274 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 275 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 276 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 277 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 278 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 279 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 280 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 281 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 282 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 283 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 284 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 285 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 286 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 287 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 288 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 289 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 290 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 291 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 292 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 293 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 294 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 295 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 296 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 297 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 298 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 299 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 300 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 301 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 302 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 303 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 304 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 305 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 306 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 307 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 308 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 309 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 310 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 311 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 312 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 313 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 314 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 315 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 316 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 317 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 318 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 319 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 320 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 321 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 322 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 323 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 324 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 325 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 326 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 327 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 328 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 329 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 330 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 331 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 332 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 333 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 334 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 335 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 336 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 337 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 338 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 339 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 340 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 341 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 342 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 343 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 344 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 345 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 346 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 347 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 348 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 349 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 350 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 351 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 352 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 353 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 354 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 355 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 356 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 357 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 358 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 359 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 360 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 361 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 362 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 363 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 364 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 365 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 366 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 367 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 368 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 369 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 370 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 371 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 372 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 373 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 374 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 375 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 376 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 377 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 378 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 379 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 380 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
