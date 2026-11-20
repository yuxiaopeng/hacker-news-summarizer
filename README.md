# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-11-20.md)

*最后自动更新时间: 2026-11-20 23:25:56*
## 1. 紧急公告：亚历山德罗·马苏洛 GRH

**原文标题**: Hurried Announcement: Alessandro Masullo GRH

**原文链接**: [https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/](https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/)

在2026年11月20日发布的一篇博文中，数学家拉维·瓦基勒（Ravi Vakil）宣布，亚历山德罗·马苏洛（Alessandro Masullo）提出了一项关于广义黎曼猜想（GRH）的拟议证明。

该公告强调了几个关键点：

*   **专家评审：**布莱恩·康拉德（Brian Conrad）已花费数月时间仔细审查马苏洛的工作。康拉德的大量反馈正被纳入证明中，目前的研究结果被形容为“进展良好”。
*   **人类创作：**瓦基勒强调，该证明完全由人类完成，没有人工智能的辅助。
*   **提前发布：**虽然原计划是邀请马苏洛前往斯坦福大学进行为期一年的访问，在正式发布前完善手稿，但瓦基勒决定立即向数学界公开当前的草案。
*   **呼吁核实：**鼓励数学界对这份题为《素数的音乐》（The Music of the Primes）的草案进行审查和形式化验证，并指出其中可能存在的任何漏洞。

瓦基勒在参加美国数学学会会议期间撰写了此文，他表达了对康拉德判断力的坚定信心，并希望该证明能经受住严苛的审查。

---

## 2. Inkling 2 迷你

**原文标题**: Inkling 2 Mini

**原文链接**: [https://thinkingmachines.ai/news/inkling-2-mini/](https://thinkingmachines.ai/news/inkling-2-mini/)

**Inkling 2 Mini** 是一款新型开源权重混合专家（MoE）模型，专为本地硬件上的高性能推理而设计。该模型总参数量为 26.4B（激活参数 3.4B），采用了独特的**循环 Transformer（looped transformer）**架构，使其核心中间层在处理每个 token 时循环运行三次。这种设计在不增加模型物理尺寸的情况下，实现了更深层的推理能力和更长的“非思维链（no-CoT）”推理视界。

**主要性能亮点：**
*   **编程与推理：** 在主流基准测试中，它在 100B 参数以下的开源模型中处于领先地位，在 DeepSWE v1.1 和 Vals Index v2.2 中分别获得 48.2% 和 46.5% 的评分。它在自主编程和内核优化等智能体任务中表现卓越。
*   **能效：** 该模型具有极高的能源效率，在“单位焦耳智能”指标上显著高于 Qwen 和 Gemma 等竞争对手。
*   **本地部署：** 经过 NVFP4 和 MXFP8 量化优化，该模型的显存占用约为 20GB。它可以在消费级设备上离线运行，其实力已通过在单台 MacBook Pro 上构建飞行模拟器并驱动 20 个智能体模拟项目（Thinkyville）得到证明。

**能力与局限性：**
虽然循环架构显著提升了推理和长上下文表现，但它并不会增加模型的内部事实知识，其知识储备仍受限于总参数量。为了弥补这一不足，该模型针对工具调用和搜索进行了优化。其主要弱点包括多轮对话和复杂指令遵循，在这些方面略逊于 Qwen3.8-27B 等模型。

Inkling 2 Mini 目前已在 Tinker 平台上开放推理和定制，为研究人员提供了一个观察功能性循环架构的难得机会。

---

## 3. Levent Alpöge 声称证明了广义黎曼猜想 [pdf]

**原文标题**: Levent Alpöge claims proof of the Generalized Riemann Hypothesis [pdf]

**原文链接**: [https://alpo.ge/remark.pdf](https://alpo.ge/remark.pdf)

根据所提供文档的标题和元数据，以下是关于 Levent Alpöge 所声称之突破的文章简要概述：

**摘要：广义黎曼猜想的证明**

本文详细介绍了数学家 **Levent Alpöge** 在**广义黎曼猜想 (GRH)** 方面声称取得的重大数论突破。广义黎曼猜想是原始黎曼猜想的扩展；它假设一类被称为 $L$-函数（$L$-functions）的广泛数学函数的所有非平凡零点都位于一条特定的“临界线”上。

**关键信息：**

*   **研究主体：** Levent Alpöge 是算术几何领域的杰出人物（与哈佛大学和纽约大学有学术关联），因其在椭圆曲线秩方面的研究而闻名。他的最新工作针对的是数学领域中最重大的未解难题之一。
*   **科学意义：** 广义黎曼猜想是现代数论的基石。其证明将对素数分布、类数（class numbers）的行为以及计算数学中各种算法的效率产生直接影响。
*   **声称背景：** 尽管普适性的广义黎曼猜想（涵盖所有代数数域）仍是该领域最艰巨的挑战之一，但 Alpöge 的工作通常侧重于证明特定的大规模 $L$-函数类别的猜想——这些函数通常与函数域上的代数簇或特定的几何对象相关。
*   **方法论：** 该证明可能利用了**朗兰兹纲领 (Langlands Program)** 和算术统计中的先进工具，架起了复分析与几何表示论之间的桥梁。

**结论：**
如果得到数学界的验证，Alpöge 的证明将具有历史里程碑意义。即便该证明仅限于特定类别的 $L$-函数，它也为全面解决该猜想提供了关键路线图，并巩固了 Alpöge 作为现代数论领军人物的地位。

---

## 4. 我们在未告知开发人员的情况下，将他们提拔为了架构师。

**原文标题**: We promoted developers into architects without informing them

**原文链接**: [https://manidoraisamy.com/developer-to-architect.html](https://manidoraisamy.com/developer-to-architect.html)

Mani Doraisamy 在其文章中指出，AI 辅助的“氛围编程”（vibe coding）的兴起已从根本上将开发者的角色转变为架构师，而开发者往往并未意识到这一点。

他以一个真实案例说明了这种转变：一个由 AI 生成的日志功能因优先满足一项需求（获取用户电子邮件）而采用了多个同步 API 调用，导致了 15 秒的延迟。虽然 AI 成功编写了代码，但它未能权衡性能与安全性之间的架构利弊。

作者强调了 AI 在开发过程中的几个关键局限性：
*   **缺乏上下文：** AI 不理解业务规模或用户体验的优先级。
*   **盲从性：** AI 会机械地执行指令，很少对可能损害应用性能或可维护性的需求提出异议。
*   **保守的默认设置：** AI 往往优先考虑安全性及向后兼容性，而牺牲了速度和简洁的数据模型。

Doraisamy 总结道，虽然手动编写代码的任务正在被自动化，但开发者的工作并不会消失，而是在进化。为了在这一新格局中取得成功，开发者必须接受向架构师的“晋升”。他们的新职责包括：
1.  在让 AI 编写实现代码之前，先**设计数据模型和架构**。
2.  **约束 AI** 遵循特定的架构模式。
3.  **回绝**利益相关者提出的在技术上不切实际的需求。
4.  **审查代码**的结构完整性，而不仅仅是功能的正确性。

最后，作者警告说，如果开发者不承担起这种架构师的角色，结果将导致系统不可维护且用户体验糟糕。开发的未来在于高层设计和批判性监督，而不仅仅是代码实现。

---

## 5. 无驱动纳维-斯托克斯奇异性与广义黎曼猜想

**原文标题**: Unforced Navier-Stokes Singularity and the Generalized Riemann Hypothesis

**原文链接**: [https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/)

这篇文章发表于 Ben Eastaugh 和 Chris Sternal-Johnson 的博客 *Theorema*，探讨了流体动力学与解析数论之间一个重大且出人意料的联系。文章重点介绍了数学家亚科夫·西奈（Yakov Sinai）为解决纳维-斯托克斯存在性与光滑性问题所做的尝试，该问题是七大千禧年大奖难题之一。

讨论的核心涉及西奈的断言，即三维无外力纳维-斯托克斯方程可能产生有限时间奇异性（或称“爆破”）。如果该断言被证明正确，将表明光滑解并不总是全局存在的，从而实际上为这一千禧年难题提供了一个否定的答案。

西奈研究中最引人注目的方面在于其对**广义黎曼猜想 (GRH)** 的依赖。西奈的方法利用基于傅里叶变换的重整化技术来分析方程。他假设这些奇异性的存在取决于一类特定复函数的行为。作者解释道，西奈的证明取决于一个“全局引理”，该引理要求这些函数的某些零点位于一条特定的临界线上——这一条件与广义黎曼猜想直接类比。

文章强调了数学界的反应，在兴奋与审慎之间保持了平衡。通过将物理流体的行为与素数分布及 L-函数的分布联系起来，西奈的研究揭示了偏微分方程与数论之间深层的潜在统一性。作者总结指出，虽然该证明仍面临严密的审查，但其跨学科的性质代表了数学家在研究湍流和奇异性问题时一种潜在的革命性转变。

---

## 6. 语言模型可以重写自身权重

**原文标题**: Language Models Can Rewrite Their Own Weights

**原文链接**: [https://arxiv.org/abs/2611.21885](https://arxiv.org/abs/2611.21885)

The paper **"Language Models Can Rewrite Their Own Weights"** (arXiv:2611.21885) introduces a novel paradigm called **self-rewriting**, where a language model optimizes its own parameters through reasoning rather than traditional gradient-based training. 

Using an open 27B parameter model, the researchers demonstrate that a model can analyze its own weights, diagnose performance failures on graded tasks, and implement weight edits using only forward passes. Key findings include:

*   **Autonomous Improvement:** The model improved its accuracy on unseen problems by 6.6 points. Through eight consecutive sessions of testing and refining its own edits, its performance consistently rose.
*   **Self-Repair:** In a "broken robot" scenario, the model successfully repaired a damaged copy of itself—which initially solved almost nothing—restoring it to over 80% of its original accuracy on new image tasks without reading the original weights.
*   **Emergence with Scale:** This capability is scale-dependent; while the 27B model succeeded, smaller models in the same family either failed to make edits or corrupted their own weights.
*   **Efficiency:** Unlike test-time scaling, self-rewriting embeds gains directly into the weights, incurring no extra cost per inference. Unlike traditional training, it requires no gradients, harnesses, or backpropagation.

The authors conclude that the historical wall between "training" and "inference" is a limitation of current tools rather than an inherent property of AI. They position self-rewriting as a critical step toward **recursive self-improvement**, enabling models to continuously upgrade themselves through a lifecycle of reasoning and self-correction, much like human intelligence.

---

## 7. A few hours ago Google DeepMind created a math horizon repo

**原文标题**: A few hours ago Google DeepMind created a math horizon repo

**原文链接**: [https://github.com/google-deepmind/math-horizon](https://github.com/google-deepmind/math-horizon)

生成摘要时出错

---

## 8. The stochastic parrots have apparently proved the Riemann Hypothesis

**原文标题**: The stochastic parrots have apparently proved the Riemann Hypothesis

**原文链接**: [https://scottaaronson.blog/?p=10344](https://scottaaronson.blog/?p=10344)

在这篇日期为2026年11月20日的博客文章中，Scott Aaronson报道了数学领域的一个里程碑：据称，Anthropic公司的一个AI模型已经证明了广义黎曼猜想（GRH）。在数学家Levent Alpöge的指导下，该AI生成了一份包含1740万行Lean代码的形式化证明。

鉴于大语言模型解决千年级问题的能力日益增强，Aaronson反思了将其贴上“随机鹦鹉”标签的讽刺意味。他指出，虽然该证明已通过Lean进行了形式化验证，但人类数学家可能需要数年时间才能提炼并理解其背后的核心思想，因为与AI相比，人类的运作速度仅为“生物速度”。尽管存在对Lean内核漏洞的潜在担忧，但Aaronson押注该证明能够成立，并指出带有Lean证书的AI结果已被证明比没有证书的结果更可靠。

这篇文章捕捉到了一种“奇迹与恐怖”并存的氛围。随着黎曼猜想有望得到解决，Aaronson将“P vs NP”问题视为数学界的“终极Boss”。他描述了更广泛的生存紧张感，引用专家的观点称，AI的递归自我改进可能会在12到18个月内从根本上改变或终结世界。

文章以一个个人轶事结尾，突显了现状的超现实色彩：正当Aaronson沉思即将到来的AI奇点时，他的妻子仍专注于解决家中漏水这一现实琐事。随后的评论则讨论了纯人类证明（如传闻中Alessandro Masullo的证明）是否仍具竞争力，以及AI最终是否会解决量子引力和AI对齐等其他“终极Boss”问题。

---

## 9. Finite-time blow-up for the Navier–Stokes equations

**原文标题**: Finite-time blow-up for the Navier–Stokes equations

**原文链接**: [https://github.com/tristanbuckmaster/navier-stokes/](https://github.com/tristanbuckmaster/navier-stokes/)

生成摘要时出错

---

## 10. Vibecoding an inference chip

**原文标题**: Vibecoding an inference chip

**原文链接**: [https://ankitg.me/blog/vibecoding-inference-chip/](https://ankitg.me/blog/vibecoding-inference-chip/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-11-20](output/hacker_news_summary_2026-11-20.md) |
| 2 | [2026-11-19](output/hacker_news_summary_2026-11-19.md) |
| 3 | [2026-11-18](output/hacker_news_summary_2026-11-18.md) |
| 4 | [2026-11-14](output/hacker_news_summary_2026-11-14.md) |
| 5 | [2026-11-15](output/hacker_news_summary_2026-11-15.md) |
| 6 | [2026-11-12](output/hacker_news_summary_2026-11-12.md) |
| 7 | [2026-11-13](output/hacker_news_summary_2026-11-13.md) |
| 8 | [2026-11-17](output/hacker_news_summary_2026-11-17.md) |
| 9 | [2026-11-07](output/hacker_news_summary_2026-11-07.md) |
| 10 | [2026-11-11](output/hacker_news_summary_2026-11-11.md) |
| 11 | [2026-11-08](output/hacker_news_summary_2026-11-08.md) |
| 12 | [2026-11-10](output/hacker_news_summary_2026-11-10.md) |
| 13 | [2026-11-01](output/hacker_news_summary_2026-11-01.md) |
| 14 | [2026-11-06](output/hacker_news_summary_2026-11-06.md) |
| 15 | [2026-11-03](output/hacker_news_summary_2026-11-03.md) |
| 16 | [2026-11-05](output/hacker_news_summary_2026-11-05.md) |
| 17 | [2026-11-04](output/hacker_news_summary_2026-11-04.md) |
| 18 | [2026-10-27](output/hacker_news_summary_2026-10-27.md) |
| 19 | [2026-10-28](output/hacker_news_summary_2026-10-28.md) |
| 20 | [2026-10-29](output/hacker_news_summary_2026-10-29.md) |
| 21 | [2026-10-31](output/hacker_news_summary_2026-10-31.md) |
| 22 | [2026-10-30](output/hacker_news_summary_2026-10-30.md) |
| 23 | [2026-10-24](output/hacker_news_summary_2026-10-24.md) |
| 24 | [2026-10-23](output/hacker_news_summary_2026-10-23.md) |
| 25 | [2026-10-25](output/hacker_news_summary_2026-10-25.md) |
| 26 | [2026-10-22](output/hacker_news_summary_2026-10-22.md) |
| 27 | [2026-10-26](output/hacker_news_summary_2026-10-26.md) |
| 28 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 29 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 30 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 31 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 32 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 33 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 34 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 35 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 36 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 37 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 38 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 39 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 40 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 41 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 42 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 43 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 44 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 45 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 46 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 47 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 48 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 49 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 50 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 51 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 52 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 53 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 54 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 55 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 56 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 57 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 58 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 59 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 60 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 61 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 62 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 63 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 64 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 65 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 66 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 67 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 68 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 69 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 70 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 71 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 72 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 73 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 74 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 75 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 76 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 77 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 78 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 79 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 80 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 81 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 82 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 83 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 84 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 85 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 86 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 87 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 88 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 89 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 90 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 91 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 92 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 93 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 94 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 95 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 96 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 97 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 98 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 99 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 100 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 101 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 102 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 103 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 104 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 105 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 106 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 107 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 108 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 109 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 110 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 111 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 112 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 113 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 114 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 115 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 116 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 117 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 118 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 119 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 120 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 121 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 122 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 123 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 124 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 125 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 126 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 127 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 128 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 129 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 130 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 131 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 132 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 133 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 134 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 135 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 136 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 137 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 138 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 139 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 140 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 141 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 142 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 143 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 144 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 145 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 146 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 147 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 148 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 149 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 150 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 151 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 152 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 153 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 154 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 155 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 156 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 157 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 158 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 159 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 160 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 161 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 162 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 163 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 164 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 165 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 166 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 167 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 168 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 169 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 170 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 171 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 172 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 173 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 174 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 175 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 176 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 177 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 178 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 179 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 180 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 181 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 182 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 183 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 184 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 185 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 186 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 187 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 188 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 189 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 190 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 191 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 192 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 193 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 194 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 195 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 196 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 197 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 198 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 199 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 200 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 201 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 202 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 203 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 204 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 205 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 206 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 207 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 208 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 209 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 210 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 211 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 212 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 213 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 214 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 215 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 216 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 217 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 218 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 219 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 220 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 221 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 222 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 223 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 224 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 225 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 226 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 227 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 228 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 229 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 230 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 231 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 232 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 233 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 234 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 235 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 236 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 237 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 238 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 239 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 240 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 241 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 242 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 243 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 244 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 245 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 246 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 247 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 248 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 249 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 250 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 251 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 252 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 253 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 254 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 255 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 256 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 257 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 258 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 259 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 260 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 261 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 262 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 263 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 264 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 265 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 266 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 267 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 268 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 269 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 270 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 271 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 272 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 273 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 274 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 275 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 276 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 277 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 278 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 279 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 280 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 281 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 282 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 283 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 284 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 285 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 286 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 287 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 288 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 289 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 290 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 291 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 292 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 293 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 294 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 295 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 296 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 297 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 298 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 299 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 300 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 301 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 302 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 303 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 304 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 305 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 306 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 307 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 308 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 309 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 310 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 311 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 312 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 313 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 314 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 315 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 316 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 317 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 318 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 319 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 320 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 321 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 322 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 323 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 324 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 325 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 326 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 327 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 328 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 329 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 330 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 331 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 332 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 333 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 334 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 335 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 336 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 337 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 338 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 339 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 340 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 341 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 342 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 343 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 344 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 345 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 346 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 347 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 348 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 349 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 350 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 351 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 352 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 353 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 354 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 355 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 356 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 357 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 358 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 359 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 360 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 361 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 362 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 363 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 364 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 365 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 366 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 367 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 368 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 369 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 370 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 371 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 372 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 373 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 374 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 375 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 376 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 377 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 378 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 379 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 380 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 381 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 382 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 383 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 384 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 385 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 386 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 387 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 388 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 389 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 390 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 391 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 392 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 393 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 394 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 395 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 396 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 397 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 398 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 399 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 400 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 401 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 402 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 403 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 404 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 405 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 406 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 407 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 408 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 409 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 410 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 411 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 412 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 413 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 414 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 415 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 416 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 417 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 418 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 419 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 420 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 421 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 422 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 423 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 424 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 425 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 426 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 427 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 428 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 429 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 430 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 431 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 432 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 433 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 434 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 435 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 436 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 437 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 438 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 439 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 440 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 441 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 442 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 443 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 444 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 445 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 446 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 447 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 448 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 449 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 450 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 451 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 452 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 453 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 454 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 455 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 456 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 457 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 458 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 459 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 460 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 461 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 462 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 463 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 464 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 465 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 466 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 467 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 468 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 469 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 470 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 471 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 472 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 473 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 474 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 475 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 476 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 477 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 478 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 479 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 480 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 481 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 482 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 483 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 484 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 485 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 486 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 487 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 488 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 489 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 490 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 491 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 492 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 493 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 494 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 495 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 496 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 497 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 498 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 499 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 500 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 501 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 502 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 503 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 504 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 505 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 506 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 507 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 508 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 509 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 510 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 511 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 512 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 513 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 514 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 515 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 516 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 517 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 518 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 519 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 520 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 521 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 522 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 523 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 524 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 525 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 526 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 527 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 528 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 529 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 530 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 531 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 532 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 533 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 534 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 535 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 536 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 537 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 538 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 539 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 540 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 541 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 542 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 543 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 544 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 545 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 546 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 547 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 548 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 549 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 550 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 551 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 552 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 553 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 554 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 555 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 556 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 557 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 558 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 559 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 560 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 561 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 562 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 563 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 564 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 565 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 566 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 567 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 568 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 569 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 570 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 571 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 572 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 573 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 574 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 575 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 576 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 577 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 578 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 579 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 580 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 581 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 582 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 583 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 584 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 585 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 586 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 587 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 588 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 589 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 590 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 591 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 592 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 593 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 594 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 595 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 596 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 597 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 598 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 599 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 600 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 601 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 602 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 603 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 604 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 605 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
