# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-10-20.md)

*最后自动更新时间: 2026-10-20 20:46:06*
## 1. 《模拟城市》，但要办证

**原文标题**: SimCity, but with Permits

**原文链接**: [https://permit.petercai.com/](https://permit.petercai.com/)

文章《模拟城市，但有许可证》描述了对传统城市建设类游戏的一种冷峻而现实的改编。其核心前提是：每一次城市改进都会引发特定利益团体的相应抵制。

作者强调了该模型中的几个关键权衡：
* **住房：** 增加住房供应降低了租金，但激怒了担心房产贬值的业主。
* **工业：** 建造工厂创造了就业机会，但会产生雾霾和环境投诉。
* **基础设施：** 改善交通促进了开发，但这反过来又招致了有组织的增长反对者。

最终，文章指出，在现实的模拟中，解决一个问题并不代表胜利，而是创造了一个新的愤怒选民群体。这捕捉到了现实世界城市规划中固有的政治摩擦和“邻避效应”（NIMBY）。

---

## 2. 沃克斯特拉 3

**原文标题**: Voxtral 3

**原文链接**: [https://mistral.ai/news/voxtral-3/](https://mistral.ai/news/voxtral-3/)

Mistral 推出了 **Voxtral 3**，这是一套全面的语音套件，包含全新的语音智能体 SDK 以及先进的语音转文本 (STT) 和文本转语音 (TTS) 模型。该系统专为实时、多步骤交互而设计，助力开发者构建能够跨 50 多种语言进行推理并执行任务的高级虚拟助手和呼叫中心代理。

此次发布的核心组件包括：

*   **Voxtral Transcribe 3 (STT)：** 该模型在转写和说话人识别（Diarization）方面具有行业领先的准确率。它具备“上下文偏置”功能，可帮助模型识别技术或特定领域的专业术语，并利用声学和语义线索进行精确的“话轮结束检测”，在低于 500 毫秒的延迟下确保自然的对话流。
*   **Voxtral Mini TTS 3 (TTS)：** 该模型能以 35 多种语言提供富有表现力、类人的语音，并根据对话上下文自动调整情感、语速和重音。它还引入了 “Pro Voice” 适配功能，仅需 30 分钟音频即可实现高保真语音克隆。
*   **Voice Agent SDK：** 这是一个集听觉、推理、工具调用和表达于一体的统一流水线。它允许智能体在实时通话中执行复杂的工作流，例如从业务系统中检索数据或预订行程。

Voxtral 3 的一大核心亮点是**主权部署**。企业既可以通过 Mistral 位于欧盟托管的 API 访问模型，也可以将其部署在自有基础设施上，从而确保对数据隐私和音频保留的完全控制。作为 OpenAI、ElevenLabs 和 Google 等竞争对手的高性价比替代方案，Voxtral 3 为企业级语音 AI 提供了高性能、低延迟的解决方案。

---

## 3. DeepInfer：DeepSeek 模型高性能推理框架

**原文标题**: DeepInfer: High-performance inference framework for DeepSeek models

**原文链接**: [https://github.com/deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer)

生成摘要时出错

---

## 4. 谷歌开源 TorchTPU，一个针对 TPU 的原生 PyTorch 后端。

**原文标题**: Google open-sources TorchTPU, a native PyTorch back end for TPUs

**原文链接**: [https://github.com/google-pytorch/torch_tpu](https://github.com/google-pytorch/torch_tpu)

Google 已开源 **TorchTPU**，这是一个原生的 PyTorch 后端，旨在让用户能够直接在 Google 的张量处理单元 (TPU) 上运行 PyTorch 模型和操作。该项目通过以下几个关键特性，弥合了 PyTorch 灵活的框架与 TPU 硬件效率之间的差距：

*   **核心功能：** 包括针对 TPU 的自定义 ATen 算子实现，以及用于优化 XLA 计算执行的编译缓存。它还与 `torch.compile()` 无缝集成，支持图模式执行。
*   **扩展性与模型：** TorchTPU 支持分布式训练技术，包括数据并行和张量并行。为了帮助用户快速上手，该仓库提供了 Llama、Qwen、ResNet、DLRM、minGPT 和 UNet 等热门模型的示例。
*   **安装与

TorchTPU 采用 Apache 2.0 许可证开源，欢迎社区贡献，旨在简化 Google 专用硬件上的高性能机器学习工作流。

---

## 5. SlopCodeBench 10/2026 – Opus 5.5, Astra wins overall, xhigh considered harmful

**原文标题**: SlopCodeBench 10/2026 – Opus 5.5, Astra wins overall, xhigh considered harmful

**原文链接**: [https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-new-models-on-slop-code-bench.md](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-new-models-on-slop-code-bench.md)

The SlopCodeBench (SCB) October 2026 update, authored by Dex Horthy, provides a comprehensive look at how frontier AI models handle evolving software requirements. Testing models like GPT-6 Astra, SOL 6.1, and Opus 5.5, the benchmark evaluates their ability to maintain code across multiple checkpoints where requirements change over time.

**Key Findings:**
*   **Top Performer:** GPT-6 Astra achieved the highest "strict pass rate" at 16.33%, a modest increase from GPT-5.5’s 14.8% in May. This "strict" metric requires models to pass all new tests while maintaining all previous functionality (regression testing).
*   **The "XHigh" Paradox:** Increased effort settings (XHigh) often resulted in diminishing returns. Despite costing 2.11x to 4.22x more than "Medium" settings, XHigh only improved strict success for Astra. Notably, Opus 5.5 performed better on Medium effort than on XHigh.
*   **Core vs. Strict Success:** While models showed high "core pass rates" (65.8%–74.0%), their ability to avoid regressions was much lower, with strict rates hovering between 12.2% and 16.3%.
*   **Code Quality and "Slop":** The report tracks "slop"—junk code, scratch files, and redundant patterns. Opus 5.5 Medium produced the most slop (94.25% coverage), whereas the XHigh version produced code that was roughly five times cleaner, even though it failed more strict tests.

**Conclusion:**
The benchmark highlights a significant "maintenance gap." While AI agents are improving at initial coding tasks, they still struggle to keep a codebase stable as requirements evolve. The author concludes that while progress is steady, the slow rate of improvement suggests that AI is not yet ready to handle complex software maintenance without significant human oversight.

---

## 6. 我该教我儿子什么？

**原文标题**: What shall I teach my son?

**原文链接**: [https://stevekrouse.com/ends](https://stevekrouse.com/ends)

在《我该教我儿子什么？》一文中，作者以一位 2026 年的程序员及准父亲的视角，探讨了通用人工智能（AGI）时代教育所面临的存在危机。随着 AGI 威胁到编程等传统技能的经济价值，作者对学习的“初衷”提出了质疑。

文章指出，从托马斯·爱迪生到作者本人，技术专家们一直存在一种历史惯性，即错误地预言技术（如广播、电影、慕课）将使学校走向消亡。作者援引“林迪效应”指出，学校通过不断调整自身定位已存续数个世纪，其存在往往源于托儿需求和声望等现实因素，而非其宣称的使命。

然而，AGI 的兴起动摇了教育的传统支柱，尤其是“谋生”这一目标。如果 AI 智能体现在能够掌握“应变能力”并在市场和科学领域超越人类，那么传统学位的客观价值便会动摇。

借鉴尼尔·波兹曼在《教育的终结》中的观点，作者考虑了学校教育的其他更具人文色彩的目的，例如：
*   **地球飞船：** 培养全球管家意识。
*   **美利坚实验：** 激发公民的好奇心与责任感。
*   **世界创造者：** 鼓励学生去塑造定义社会的工具和叙事。

最终，作者总结道，“媒介即讯息”。他不再将教育视为一种“施加于”孩子身上的行为，而是将其转变为与孩子“共同完成”的协作过程。他建议，应对不确定未来最有效的方式，是邀请孩子在共同探索新世界的过程中，共同创造属于他们自己的教育目标。

---

## 7. 苹果破坏了 iPad 的一项核心演示功能。

**原文标题**: Apple broke an essential presentation feature of iPads

**原文链接**: [https://teddysvoronos.com/2026-10-19-apple-broke-an-essential-presentation-feature-of-ipads/](https://teddysvoronos.com/2026-10-19-apple-broke-an-essential-presentation-feature-of-ipads/)

In the article "Apple broke an essential presentation feature of iPads," the author details a significant regression in **iPadOS 27** (and its predecessor, iPadOS 26) that disrupts professional and pedagogical workflows.

**The Problem**
The author highlights a change in how the iPad handles external displays via AirPlay. Previously, presenters could display a specific app (like a handout or slides) to an audience while using the iPad’s screen for private tasks, such as viewing notes, controlling polls, or managing a Mac. Now, tapping any app other than the one being presented causes the external display to immediately mirror the entire iPad screen. This exposes private information to students or audiences and creates a jarring visual experience.

**Impact on Apps**
The behavior varies by application, but all are negatively affected:
*   **GoodNotes:** The presenter view returns only when the user taps back into the app.
*   **Keynote:** The presentation exits entirely when another app is touched.
*   **PowerPoint:** The app enters a "limbo" state that requires a full restart of the presentation.

**The Cause and Solution**
The author suggests Apple implemented this change to simplify which app "controls" the external display. However, they argue the fix is worse than the original problem. The author proposes a logical alternative: any app currently in "presenter mode" should maintain exclusive precedence on the external display until the user manually stops the presentation or closes the app.

**Conclusion**
Due to these "devastating" changes, the author currently advises against using the iPad for teaching or presenting. They encourage affected users to submit feedback to Apple (referencing feedback code **FB23615646**) to lobby for a restoration of proper presenter functionality.

---

## 8. Ofcom concedes defeat in 4chan case

**原文标题**: Ofcom concedes defeat in 4chan case

**原文链接**: [https://prestonbyrne.com/2026/10/20/ofcom-concedes-defeat/](https://prestonbyrne.com/2026/10/20/ofcom-concedes-defeat/)

生成摘要时出错

---

## 9. Jepsen：Orkes Conductor 5.3.2

**原文标题**: Jepsen: Orkes Conductor 5.3.2

**原文链接**: [https://jepsen.io/analyses/orkes-conductor-5.3.2](https://jepsen.io/analyses/orkes-conductor-5.3.2)

The Jepsen report on Orkes Conductor (v5.3.2–5.5.0-rc2) evaluates the orchestrator's behavior under fault conditions like network partitions and node crashes. Using a Postgres database and Redis queue, Jepsen identified several consistency and reliability issues during the testing process.

Key findings include:

*   **Concurrent Task Execution:** Despite locking mechanisms, tasks were occasionally executed by multiple workers simultaneously. This was exacerbated by a "sweeper" process bug that re-enqueued active tasks; Orkes reported this fixed in version 5.5.6.
*   **Stalled Workflows:** Faults isolating Conductor servers from Redis or Postgres caused workflows to stall until the response timeout (defaulting to one hour) triggered a reschedule. While disruptive, this did not violate Conductor’s core guarantees.
*   **API and Database Errors:** Researchers observed `startWorkflow()` returning `null` IDs, SQL syntax errors caused by race conditions during table partition rotations, and duplicate key errors in Postgres due to faulty retry logic in early 5.5.0 builds.
*   **Indeterminate Failures:** Network errors during API calls sometimes masked successful workflow starts, leading to "aborted reads" where a workflow existed despite the client receiving a connection failure.

Orkes addressed the most critical bugs—including the sweeper bug, partition management race conditions, and duplicate key errors—in version 5.5.6. The analysis concludes that while Conductor maintains its "at-least-once" delivery guarantee, users should design tasks to be idempotent and adjust response timeouts to mitigate stalling during infrastructure failures.

---

## 10. EMudhra Intermediate CA Compromise

**原文标题**: EMudhra Intermediate CA Compromise

**原文链接**: [https://emudhra.we-have-a-problem.com/](https://emudhra.we-have-a-problem.com/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 2 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 3 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 4 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 5 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 6 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 7 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 8 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 9 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 10 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 11 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 12 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 13 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 14 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 15 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 16 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 17 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 18 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 19 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 20 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 21 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 22 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 23 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 24 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 25 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 26 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 27 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 28 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 29 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 30 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 31 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 32 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 33 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 34 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 35 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 36 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 37 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 38 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 39 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 40 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 41 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 42 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 43 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 44 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 45 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 46 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 47 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 48 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 49 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 50 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 51 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 52 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 53 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 54 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 55 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 56 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 57 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 58 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 59 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 60 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 61 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 62 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 63 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 64 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 65 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 66 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 67 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 68 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 69 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 70 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 71 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 72 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 73 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 74 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 75 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 76 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 77 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 78 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 79 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 80 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 81 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 82 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 83 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 84 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 85 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 86 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 87 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 88 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 89 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 90 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 91 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 92 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 93 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 94 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 95 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 96 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 97 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 98 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 99 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 100 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 101 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 102 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 103 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 104 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 105 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 106 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 107 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 108 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 109 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 110 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 111 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 112 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 113 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 114 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 115 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 116 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 117 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 118 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 119 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 120 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 121 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 122 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 123 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 124 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 125 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 126 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 127 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 128 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 129 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 130 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 131 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 132 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 133 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 134 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 135 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 136 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 137 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 138 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 139 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 140 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 141 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 142 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 143 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 144 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 145 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 146 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 147 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 148 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 149 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 150 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 151 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 152 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 153 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 154 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 155 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 156 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 157 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 158 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 159 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 160 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 161 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 162 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 163 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 164 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 165 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 166 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 167 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 168 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 169 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 170 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 171 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 172 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 173 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 174 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 175 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 176 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 177 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 178 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 179 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 180 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 181 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 182 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 183 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 184 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 185 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 186 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 187 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 188 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 189 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 190 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 191 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 192 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 193 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 194 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 195 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 196 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 197 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 198 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 199 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 200 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 201 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 202 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 203 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 204 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 205 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 206 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 207 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 208 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 209 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 210 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 211 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 212 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 213 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 214 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 215 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 216 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 217 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 218 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 219 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 220 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 221 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 222 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 223 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 224 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 225 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 226 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 227 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 228 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 229 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 230 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 231 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 232 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 233 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 234 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 235 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 236 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 237 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 238 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 239 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 240 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 241 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 242 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 243 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 244 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 245 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 246 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 247 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 248 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 249 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 250 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 251 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 252 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 253 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 254 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 255 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 256 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 257 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 258 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 259 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 260 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 261 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 262 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 263 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 264 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 265 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 266 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 267 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 268 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 269 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 270 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 271 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 272 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 273 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 274 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 275 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 276 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 277 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 278 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 279 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 280 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 281 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 282 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 283 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 284 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 285 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 286 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 287 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 288 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 289 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 290 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 291 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 292 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 293 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 294 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 295 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 296 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 297 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 298 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 299 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 300 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 301 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 302 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 303 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 304 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 305 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 306 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 307 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 308 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 309 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 310 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 311 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 312 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 313 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 314 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 315 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 316 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 317 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 318 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 319 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 320 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 321 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 322 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 323 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 324 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 325 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 326 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 327 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 328 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 329 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 330 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 331 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 332 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 333 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 334 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 335 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 336 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 337 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 338 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 339 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 340 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 341 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 342 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 343 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 344 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 345 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 346 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 347 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 348 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 349 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 350 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 351 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 352 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 353 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 354 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 355 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 356 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 357 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 358 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 359 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 360 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 361 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 362 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 363 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 364 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 365 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 366 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 367 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 368 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 369 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 370 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 371 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 372 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 373 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 374 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 375 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 376 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 377 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 378 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 379 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 380 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 381 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 382 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 383 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 384 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 385 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 386 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 387 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 388 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 389 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 390 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 391 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 392 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 393 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 394 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 395 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 396 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 397 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 398 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 399 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 400 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 401 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 402 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 403 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 404 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 405 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 406 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 407 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 408 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 409 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 410 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 411 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 412 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 413 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 414 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 415 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 416 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 417 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 418 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 419 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 420 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 421 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 422 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 423 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 424 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 425 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 426 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 427 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 428 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 429 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 430 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 431 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 432 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 433 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 434 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 435 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 436 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 437 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 438 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 439 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 440 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 441 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 442 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 443 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 444 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 445 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 446 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 447 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 448 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 449 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 450 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 451 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 452 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 453 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 454 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 455 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 456 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 457 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 458 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 459 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 460 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 461 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 462 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 463 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 464 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 465 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 466 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 467 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 468 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 469 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 470 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 471 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 472 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 473 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 474 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 475 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 476 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 477 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 478 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 479 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 480 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 481 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 482 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 483 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 484 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 485 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 486 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 487 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 488 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 489 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 490 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 491 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 492 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 493 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 494 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 495 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 496 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 497 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 498 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 499 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 500 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 501 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 502 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 503 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 504 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 505 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 506 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 507 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 508 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 509 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 510 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 511 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 512 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 513 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 514 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 515 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 516 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 517 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 518 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 519 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 520 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 521 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 522 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 523 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 524 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 525 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 526 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 527 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 528 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 529 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 530 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 531 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 532 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 533 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 534 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 535 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 536 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 537 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 538 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 539 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 540 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 541 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 542 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 543 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 544 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 545 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 546 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 547 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 548 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 549 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 550 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 551 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 552 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 553 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 554 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 555 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 556 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 557 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 558 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 559 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 560 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 561 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 562 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 563 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 564 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 565 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 566 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 567 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 568 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 569 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 570 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 571 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 572 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 573 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 574 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 575 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 576 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 577 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
