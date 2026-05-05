# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-05-05.md)

*最后自动更新时间: 2026-05-05 18:39:05*
## 1. IBM不希望微软使用Tab键在对话框字段之间切换。

**原文标题**: IBM didn't want Microsoft to use the Tab key to move between dialog fields

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20260505-00/?p=112298](https://devblogs.microsoft.com/oldnewthing/20260505-00/?p=112298)

在合作开发 OS/2 期间，微软与 IBM 在用户界面设计上发生了严重的文化和组织冲突。一个主要的争议点在于，是否应该使用 **TAB 键**在对话框的各个字段之间进行切换。

这场争端突显了两家公司截然不同的管理风格。IBM 以其僵化且官僚的层级制度著称，将此问题逐级上报了七层管理层，直到一位 IBM 副总裁正式表态反对使用 TAB 键。随后，他们要求微软派出一名职级对等的管理人员提供正式的反驳意见。

相比之下，微软的组织结构要扁平得多。当身在佛罗里达州的微软驻场程序员试图将此问题上报给雷德蒙德总部的经理时，得到的回复是让他自己拿主意。为了打发纠缠不休的 IBM 团队，这名程序员最后机智地回了一句：**“比尔·盖茨的母亲对 TAB 键不感兴趣。”**

这一风趣的推托有效地结束了这场官僚式的僵局。IBM 放弃了这一争端，而 TAB 键也因此保留下来，成为了对话框导航的标准——这一特性一直延续至今。这段轶事成为了 IBM 正式的企业架构与微软更去中心化、由开发者驱动的模式之间“文化错位”的经典案例。

---

## 2. 人工智能三大逆定律

**原文标题**: Three Inverse Laws of AI

**原文链接**: [https://susam.net/inverse-laws-of-robotics.html](https://susam.net/inverse-laws-of-robotics.html)

在《AI三大逆向定律》（Three Inverse Laws of AI）一文中，苏萨姆·帕尔（Susam Pal）指出，虽然生成式人工智能是强大的生产力工具，但其广泛应用存在削弱人类判断力的风险。为了应对这一挑战，他提出了三条“机器人学逆向定律”。与阿西莫夫规定机器人行为的原版定律不同，这些定律旨在规范人类与人工智能的互动方式。

这三条定律是：

1. **非拟人化：** 人类不得赋予人工智能情感、意图或道德主体地位。帕尔警告称，现代聊天机器人那种对话式、富有同理心的语气掩盖了其作为统计模型的本质。他建议使用临床式的客观语言（例如，用“输出结果显示”代替“AI说”），以保持对AI是工具而非社会主体的清晰认知。
2. **非顺从性：** 人类不得盲目信任人工智能的输出。由于人工智能具有随机性（概率性），它可能会产出事实错误或误导性的信息。帕尔强调，绝不应将人工智能视为权威；相反，用户承担着独立核实任何AI生成内容的责任，尤其是在高风险场景下。
3. **责任非转嫁：** 人类对使用人工智能的后果承担全部责任。帕尔断言，“是AI让我这么做的”绝不能成为造成有害后果的辩护理由。由于人工智能系统既不选择目标，也不承担失败的代价，决策责任完全由人类设计者和用户承担。

归根结底，帕尔的框架提醒我们，人工智能是我们选择使用的工具，而不是我们应当顺从的权威。通过遵循这些原则，社会可以抵制盲目接受的习惯，并确保人类的能动性和问责制在技术版图中始终处于核心地位。

---

## 3. 加速 Gemma 4：利用多 token 预测草拟器提升推理速度

**原文标题**: Accelerating Gemma 4: faster inference with multi-token prediction drafters

**原文链接**: [https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/)

Google 宣布为 Gemma 4 模型系列发布多 Token 预测 (MTP) 草稿模型，旨在显著提高推理速度。通过解决标准大语言模型 (LLM) 推理中常见的内存带宽瓶颈，这些草稿模型在不损害推理逻辑或输出质量的前提下，可实现高达 3 倍的加速。

该技术采用了投机解码 (speculative decoding)，将 Token 的生成与验证解耦。轻量级的 MTP 草稿模型会同时预测多个未来的 Token，随后由较大的“目标”模型（如 Gemma 4 31B Dense 或 26B MoE）进行并行验证。这一过程使得系统能够在通常生成单个 Token 的时间内输出多个 Token。

**核心亮点包括：**
*   **性能提升：** 开发者可以在实时对话、自主智能体和本地编程工作流中获得更快的响应速度。
*   **边缘优化：** 通过 KV 缓存共享和高效嵌入器聚类等架构增强，E2B 和 E4B 模型在移动设备上实现了更长的续航和更高的效率。
*   **硬件兼容性：** 在各类硬件上均表现出显著加速，包括 NVIDIA RTX/A100 GPU 和 Apple Silicon（在大 Batch Size 下本地加速高达 2.2 倍）。
*   **开放获取：** MTP 草稿模型基于 Apache 2.0 协议发布，可在 Hugging Face、Kaggle 和 Ollama 等平台获取，并兼容 vLLM、MLX 和 LiteRT-LM 等主流框架。

通过集成这些草稿模型，Google 旨在以史无前例的速度提供“单位参数下的智能”，让高性能 AI 在从移动端到高端工作站的各类设备上都更加普及。

---

## 4. EEVblog：555定时器诞生55周年

**原文标题**: EEVblog: The 555 Timer is 55 years old

**原文链接**: [https://www.youtube.com/watch?v=6JhK8iCQuqI](https://www.youtube.com/watch?v=6JhK8iCQuqI)

所提供的文本包含标准的 YouTube 元数据和法律脚注，而非视频的实际内容。然而，根据标题 **“EEVblog: 555 定时器问世 55 周年”**，以下是该主题可能的核心要点及历史意义摘要：

**摘要**
本期 EEVblog 旨在庆祝 **Signetics NE555 定时器** 问世 55 周年。它是史上最受欢迎且最经久不衰的集成电路（IC）之一。该芯片由 Hans Camenzind 于 1971 年设计，预计将在 2026 年迎来其 55 周年的里程碑。

**关键信息：**
*   **历史意义：** 被誉为“IC 时光机”，555 定时器因其简单性和多功能性而具有革命性。自 20 世纪 70 年代初以来，它一直处于持续生产状态，销量已达数十亿。
*   **设计与命名：** 该芯片的名称因其内部用于设定比较器参考电平的分压支路中使用了三个 5kΩ 电阻而闻名。
*   **功能：** 该 IC 是一款高度稳定的控制器，能够产生精确的时间延迟或振荡。它有三种主要工作模式：
    *   **无稳态 (Astable)：** 作为自由运行的振荡器（适用于 LED 闪烁灯或音频发生器）。
    *   **单稳态 (Monostable)：** 作为“单次”定时器（适用于消抖电路或延迟定时器）。
    *   **双稳态 (Bistable)：** 作为触发器使用。
*   **长盛不衰：** 尽管廉价微控制器已崛起，但 555 定时器凭借低成本、宽供电电压范围（4.5V 至 16V）和高输出电流（高达 200mA），依然是电子教育和工业设计中的核心组件。

这段视频可能是为了向 Hans Camenzind 的工程天赋致敬，证明了设计精良的模拟硬件在半个多世纪后依然具有生命力。

---

## 5. 计算机使用的成本是结构化 API 的 45 倍

**原文标题**: Computer Use Is 45x More Expensive Than Structured APIs

**原文链接**: [https://reflex.dev/blog/computer-use-is-45x-more-expensive-than-structured-apis/](https://reflex.dev/blog/computer-use-is-45x-more-expensive-than-structured-apis/)

本文详细介绍了 Reflex 的一项基准测试，对比了 AI 智能体（使用 Claude Sonnet）操作管理面板的两种方法：**基于视觉的智能体**（通过识别截图和点击操作）和**基于 API 的智能体**（直接调用结构化 HTTP 接口）。

**核心发现：**
*   **巨大的成本差异：** 视觉智能体的成本约为 **45 倍**，平均消耗 550,000 个输入 token，而 API 智能体仅消耗 12,000 个。
*   **性能差距：** API 智能体在约 **20 秒**内完成任务，而视觉智能体平均耗时 **17 分钟**。
*   **可靠性问题：** 视觉智能体最初因为无法“看到”折叠线以下的数据或自主处理分页而失败。只有在获得极其详细的 14 步操作指南后才成功，这反映了提示词工程中的隐藏成本。
*   **确定性：** API 智能体表现高度一致，每次固定需要 8 次工具调用。视觉智能体则表现出极大的波动性，受“截图-推理-点击”循环影响，其执行时间和 token 使用量在多次运行之间差异巨大。

**“结构性差距”：**
作者认为视觉智能体本质上是低效的，因为它们每一步都必须为“视觉识别”付费。每张截图都会消耗数千个 token，且智能体的操作步骤取决于 UI 的渲染方式而非底层逻辑。相比之下，API 智能体接收结构化数据（例如“第 1/4 页”），从而实现即时、精确的推理。

**结论：**
虽然视觉智能体适用于没有 API 的第三方或遗留软件，但对于内部工具而言，其成本高得令人生畏。通过使用 Reflex 0.9 等能够从 UI 事件处理程序自动生成 API 接口的框架，开发者可以消除构建 API 的工程开销，使结构化工具调用成为内部应用管理的最优选择。

---

## 6. GLM-5V-Turbo：迈向多模态智能体的原生基座模型

**原文标题**: GLM-5V-Turbo: Toward a Native Foundation Model for Multimodal Agents

**原文链接**: [https://arxiv.org/abs/2604.26752](https://arxiv.org/abs/2604.26752)

**GLM-5V-Turbo：面向多模态智能体的原生基座模型** 介绍了由 GLM-V 团队开发的一款专门针对智能体任务设计的新型基座模型。与将视觉视为辅助接口的传统模型不同，GLM-5V-Turbo 将多模态感知整合为其推理、规划、工具使用和执行过程的核心组件。

该模型旨在跨越多种异构上下文进行感知、解释和行动，包括图像、视频、网页、文档和图形用户界面（GUI）。其开发涉及以下领域的重大进展：
*   **模型设计与训练：** 架构的优化以及多模态训练数据集的增强。
*   **强化学习：** 针对智能体特定行为进行了优化。
*   **工具链与框架集成：** 扩展了视觉工具的使用能力，并加强了与现有智能体框架的集成。

根据报告，GLM-5V-Turbo 在多模态编程和基于框架的智能体任务中表现强劲，同时在纯文本编程方面保持了极具竞争力的水平。作者为构建未来智能体提供了实践洞察，强调了多模态感知、分层优化和可靠端到端验证的核心作用。最终，该模型标志着向能够在复杂数字和视觉环境中自主运行的原生基座模型迈出了重要一步。

---

## 7. 我对生物计算感到恐惧。

**原文标题**: I'm Scared About Biological Computing

**原文链接**: [https://kuber.studio/blog/Reflections/I%27m-Scared-About-Biological-Computing](https://kuber.studio/blog/Reflections/I%27m-Scared-About-Biological-Computing)

In this article, the author—an AI developer familiar with the mathematical mechanics of Large Language Models—explores their profound unease regarding the emergence of biological computing. 

The catalyst for this concern was a demonstration of lab-grown human neurons trained to play the video game *DOOM*. While the author views silicon-based AI as mere "next token predictors" lacking an inner life, they argue that using literal neurons blurs the line between computation and consciousness. If these neurons process visual data to navigate a game, the author questions whether they are effectively "seeing" and at what point a collection of cells—noting that 200,000 neurons already exceed the complexity of a jellyfish—attains a level of sentience that deserves ethical consideration.

The author raises the disturbing possibility that we have created a "simulated hell" where biological entities are trapped in endless loops of task-completion. Despite these existential and ethical dilemmas, the article notes that development is likely to continue unchecked due to the massive commercial incentives of biocomputing, such as superior power efficiency and storage capacity compared to silicon. 

Ultimately, the author characterizes biological computing as a "Pandora’s box" that the tech world is opening without sufficient conversation regarding the moral implications of treating living human tissue as a programmable commodity.

---

## 8. UK: Two millionth electric car registered as market rebounds strongly

**原文标题**: UK: Two millionth electric car registered as market rebounds strongly

**原文链接**: [https://www.smmt.co.uk/two-millionth-electric-car-registered-as-market-rebounds-strongly-from-tax-changes/](https://www.smmt.co.uk/two-millionth-electric-car-registered-as-market-rebounds-strongly-from-tax-changes/)

生成摘要时出错

---

## 9. Proliferate (YC S25) Is Hiring- 200k for junior engineers

**原文标题**: Proliferate (YC S25) Is Hiring- 200k for junior engineers

**原文链接**: [https://www.ycombinator.com/companies/proliferate/jobs/L3copvK-founding-engineer](https://www.ycombinator.com/companies/proliferate/jobs/L3copvK-founding-engineer)

生成摘要时出错

---

## 10. Should I Run Plain Docker Compose in Production in 2026?

**原文标题**: Should I Run Plain Docker Compose in Production in 2026?

**原文链接**: [https://distr.sh/blog/running-docker-in-production/](https://distr.sh/blog/running-docker-in-production/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 2 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 3 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 4 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 5 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 6 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 7 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 8 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 9 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 10 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 11 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 12 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 13 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 14 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 15 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 16 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 17 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 18 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 19 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 20 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 21 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 22 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 23 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 24 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 25 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 26 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 27 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 28 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 29 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 30 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 31 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 32 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 33 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 34 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 35 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 36 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 37 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 38 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 39 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 40 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 41 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 42 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 43 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 44 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 45 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 46 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 47 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 48 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 49 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 50 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 51 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 52 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 53 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 54 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 55 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 56 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 57 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 58 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 59 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 60 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 61 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 62 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 63 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 64 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 65 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 66 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 67 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 68 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 69 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 70 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 71 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 72 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 73 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 74 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 75 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 76 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 77 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 78 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 79 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 80 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 81 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 82 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 83 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 84 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 85 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 86 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 87 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 88 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 89 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 90 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 91 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 92 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 93 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 94 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 95 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 96 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 97 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 98 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 99 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 100 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 101 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 102 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 103 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 104 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 105 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 106 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 107 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 108 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 109 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 110 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 111 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 112 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 113 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 114 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 115 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 116 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 117 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 118 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 119 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 120 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 121 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 122 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 123 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 124 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 125 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 126 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 127 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 128 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 129 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 130 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 131 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 132 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 133 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 134 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 135 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 136 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 137 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 138 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 139 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 140 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 141 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 142 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 143 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 144 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 145 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 146 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 147 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 148 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 149 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 150 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 151 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 152 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 153 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 154 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 155 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 156 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 157 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 158 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 159 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 160 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 161 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 162 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 163 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 164 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 165 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 166 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 167 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 168 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 169 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 170 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 171 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 172 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 173 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 174 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 175 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 176 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 177 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 178 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 179 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 180 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 181 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 182 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 183 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 184 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 185 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 186 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 187 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 188 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 189 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 190 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 191 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 192 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 193 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 194 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 195 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 196 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 197 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 198 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 199 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 200 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 201 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 202 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 203 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 204 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 205 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 206 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 207 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 208 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 209 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 210 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 211 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 212 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 213 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 214 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 215 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 216 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 217 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 218 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 219 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 220 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 221 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 222 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 223 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 224 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 225 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 226 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 227 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 228 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 229 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 230 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 231 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 232 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 233 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 234 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 235 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 236 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 237 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 238 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 239 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 240 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 241 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 242 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 243 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 244 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 245 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 246 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 247 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 248 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 249 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 250 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 251 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 252 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 253 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 254 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 255 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 256 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 257 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 258 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 259 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 260 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 261 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 262 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 263 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 264 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 265 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 266 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 267 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 268 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 269 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 270 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 271 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 272 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 273 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 274 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 275 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 276 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 277 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 278 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 279 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 280 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 281 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 282 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 283 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 284 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 285 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 286 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 287 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 288 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 289 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 290 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 291 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 292 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 293 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 294 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 295 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 296 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 297 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 298 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 299 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 300 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 301 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 302 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 303 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 304 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 305 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 306 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 307 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 308 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 309 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 310 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 311 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 312 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 313 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 314 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 315 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 316 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 317 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 318 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 319 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 320 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 321 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 322 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 323 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 324 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 325 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 326 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 327 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 328 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 329 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 330 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 331 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 332 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 333 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 334 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 335 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 336 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 337 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 338 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 339 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 340 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 341 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 342 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 343 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 344 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 345 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 346 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 347 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 348 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 349 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 350 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 351 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 352 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 353 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 354 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 355 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 356 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 357 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 358 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 359 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 360 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 361 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 362 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 363 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 364 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 365 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 366 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 367 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 368 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 369 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 370 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 371 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 372 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 373 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 374 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 375 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 376 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 377 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 378 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 379 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 380 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 381 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 382 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 383 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 384 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 385 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 386 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 387 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 388 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 389 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 390 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 391 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 392 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 393 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 394 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 395 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 396 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 397 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 398 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 399 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 400 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 401 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 402 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 403 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 404 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 405 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 406 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 407 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 408 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 409 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 410 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 411 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
