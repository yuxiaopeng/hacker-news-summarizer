# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-06-26.md)

*最后自动更新时间: 2026-06-26 19:34:33*
## 1. MicroVMs：运行全生命周期可控的隔离沙箱

**原文标题**: MicroVMs: Run isolated sandboxes with full lifecycle control

**原文链接**: [https://aws.amazon.com/blogs/aws/run-isolated-sandboxes-with-full-lifecycle-control-aws-lambda-introduces-microvms/](https://aws.amazon.com/blogs/aws/run-isolated-sandboxes-with-full-lifecycle-control-aws-lambda-introduces-microvms/)

AWS 最近发布了 **AWS Lambda MicroVMs**，这是一种全新的无服务器计算原语，旨在隔离的有状态环境中运行用户或 AI 生成的代码。MicroVMs 由 Firecracker 技术驱动（该技术也是标准 Lambda 函数的底层支撑），既具备虚拟机的安全隔离性，又拥有无服务器计算近乎即时的启动速度。

该服务填补了开发者在构建 AI 编程助手、数据分析平台和交互式环境等多租户应用时的关键空白。与共享内核的传统容器或无状态且事件驱动的标准 Lambda 函数不同，MicroVMs 可以在整个会话期间保留内存、磁盘状态和运行中的进程。

**核心功能包括：**
*   **基于快照的性能：** 采用“先镜像后启动”模式，Lambda 会预先初始化基于 Docker 的环境，并拍摄其内存和磁盘状态的快照。后续启动将从该快照恢复，从而消除了冷启动延迟。
*   **有状态执行：** MicroVMs 支持长达 8 小时的长时间运行交互式会话，并在用户交互过程中保留环境状态。
*   **生命周期控制：** 开发者可以设置空闲策略，在未使用时自动挂起 MicroVMs 以降低成本，同时确保环境能在下次请求时立即恢复。
*   **简化管理：** 用户可以通过标准的 Dockerfile 和 AWS CLI/控制台管理环境，无需维护复杂的虚拟化基础设施。

Lambda MicroVMs 目前已在特定区域（美国、欧洲和东京）支持 **ARM64 架构**，最高提供 16 个 vCPU 和 32 GB 内存。它们旨在与标准 Lambda 函数互补：标准函数处理事件驱动型任务，而 MicroVMs 则专为安全、有状态且交互式的多租户工作负载而设计。

---

## 2. Show HN：在 Claude、Codex 和 Cursor 中直接实现智能模型路由

**原文标题**: Show HN: Smart model routing directly in Claude, Codex and Cursor

**原文链接**: [https://github.com/workweave/router](https://github.com/workweave/router)

Weave 推出了一个智能模型路由，旨在为 Claude Code、Codex 和 Cursor 等工具优化大语言模型（LLM）的使用。作为 Anthropic、OpenAI 和 Gemini 的即插即用代理，该路由会自动为每个请求选择最高效的模型。

与基于提示词（prompt）的路由不同，该系统利用本地嵌入器和源自 Avengers-Pro 架构的集群评分器。凭借在准确性和成本效益之间的出色平衡，这种方法目前在 RouterArena 排行榜上名列第一。

**核心特性：**
*   **广泛的兼容性：** 支持 Anthropic Messages、OpenAI Chat Completions 和 Gemini 的原生 API，并可通过 OpenRouter 支持开源模型。
*   **无缝集成：** 通过快捷的 `npx` 命令，用户可将路由立即接入 Claude Code 和 Cursor 等开发工具。它同时支持项目级和全局配置。
*   **隐私与安全：** 该工具遵循“自带密钥”（BYOK）模式。API 密钥保存在本地并进行静态加密，确保绝不泄露给第三方。
*   **可观测性：** 开箱即用的 OTLP 追踪和内置仪表板提供了对路由决策和性能的深度可见性。它还可以将数据导出到 Honeycomb 或 Datadog 等平台。

用户可以选择托管版本，也可以使用 Docker 和 Postgres 进行私有化部署。通过将流量导向本地端点（`localhost:8080`），开发者可以确保在对话的每一轮中都使用“最合适”的模型，从而显著降低成本并提高响应质量。未来的更新计划引入令牌感知限流和推测性调度。

---

## 3. 美国政府将决定谁可以使用 ChatGPT 的最新升级。

**原文标题**: U.S. government will decide who gets to use latest upgrade to ChatGPT

**原文链接**: [https://www.washingtonpost.com/technology/2026/06/26/openai-says-us-government-will-vet-users-its-latest-ai-model/](https://www.washingtonpost.com/technology/2026/06/26/openai-says-us-government-will-vet-users-its-latest-ai-model/)

无法访问文章链接。

---

## 4. 脑部超声成像

**原文标题**: Ultrasound imaging of the brain

**原文链接**: [https://alephneuro.com/blog/ultrasound-brain](https://alephneuro.com/blog/ultrasound-brain)

本文详细介绍了利用超声波实现的非侵入式脑机接口（BCI）技术的重大突破。目前，脑成像技术面临着低分辨率EEG的便携性与非便携式MRI的高分辨率之间的权衡。为了解决这一问题，研究人员正在开发利用超声波绘制大脑血管系统的硬件，旨在利用血流与神经活动之间的相关性。

目前已实现一个重要的里程碑：首次通过完整的颅骨捕捉到了活人大脑最精细的3D血管图像。这是利用超声定位显微成像（ULM）技术完成的，其体积分辨率比同类CT扫描高出100倍。该过程使用经FDA批准的微泡作为造影剂。通过稀疏地注入这些微泡并逐帧精确定位其中心，该系统绕过了传统的超声衍射极限，从而能够重建微细血管并测量血流速度。

研究团队已经开源了其处理流程和数据集，并强调了该技术在识别阿尔茨海默病、中风和创伤性脑损伤等疾病血管特征方面的潜力，而这些特征在目前的MRI和CT扫描中是无法察觉的。

最终目标是从增强造影成像过渡到无造影神经血管成像。研究人员相信，通过将超声硬件的持续小型化与端到端机器学习相结合，这一目标将成为可能。通过在大规模数据集上训练AI，他们的目标是恢复由红细胞散射的微弱信号，而这些信号在传统的数据处理中往往会丢失。这种方法预示着未来无需手术即可实现便携式、高分辨率脑机交互的前景。

---

## 5. Previewing GPT‑5.6 Sol: a next-generation model

**原文标题**: Previewing GPT‑5.6 Sol: a next-generation model

**原文链接**: [https://openai.com/index/previewing-gpt-5-6-sol/](https://openai.com/index/previewing-gpt-5-6-sol/)

生成摘要时出错

---

## 6. Om Malik has died

**原文标题**: Om Malik has died

**原文链接**: [https://om.co/2026/06/24/1966-2026/](https://om.co/2026/06/24/1966-2026/)

生成摘要时出错

---

## 7. An entire Herculaneum scroll has been read for the first time

**原文标题**: An entire Herculaneum scroll has been read for the first time

**原文链接**: [https://scrollprize.org/firstscroll](https://scrollprize.org/firstscroll)

生成摘要时出错

---

## 8. Modern GPU Programming for MLSys

**原文标题**: Modern GPU Programming for MLSys

**原文链接**: [https://mlc.ai/modern-gpu-programming-for-mlsys/](https://mlc.ai/modern-gpu-programming-for-mlsys/)

生成摘要时出错

---

## 9. Springer Nature has removed two studies by Max Planck

**原文标题**: Springer Nature has removed two studies by Max Planck

**原文链接**: [https://www.science.org/content/article/why-have-papers-one-history-s-most-famous-physicists-been-retracted](https://www.science.org/content/article/why-have-papers-one-history-s-most-famous-physicists-been-retracted)

生成摘要时出错

---

## 10. Liva AI (YC S25) Is Hiring

**原文标题**: Liva AI (YC S25) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/liva-ai/jobs/gvtc3Ep-founding-operations-lead](https://www.ycombinator.com/companies/liva-ai/jobs/gvtc3Ep-founding-operations-lead)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 2 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 3 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 4 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 5 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 6 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 7 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 8 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 9 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 10 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 11 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 12 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 13 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 14 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 15 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 16 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 17 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 18 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 19 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 20 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 21 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 22 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 23 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 24 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 25 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 26 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 27 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 28 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 29 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 30 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 31 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 32 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 33 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 34 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 35 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 36 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 37 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 38 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 39 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 40 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 41 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 42 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 43 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 44 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 45 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 46 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 47 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 48 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 49 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 50 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 51 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 52 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 53 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 54 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 55 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 56 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 57 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 58 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 59 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 60 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 61 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 62 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 63 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 64 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 65 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 66 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 67 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 68 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 69 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 70 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 71 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 72 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 73 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 74 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 75 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 76 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 77 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 78 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 79 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 80 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 81 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 82 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 83 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 84 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 85 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 86 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 87 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 88 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 89 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 90 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 91 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 92 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 93 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 94 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 95 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 96 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 97 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 98 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 99 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 100 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 101 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 102 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 103 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 104 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 105 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 106 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 107 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 108 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 109 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 110 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 111 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 112 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 113 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 114 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 115 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 116 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 117 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 118 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 119 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 120 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 121 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 122 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 123 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 124 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 125 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 126 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 127 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 128 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 129 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 130 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 131 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 132 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 133 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 134 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 135 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 136 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 137 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 138 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 139 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 140 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 141 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 142 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 143 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 144 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 145 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 146 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 147 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 148 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 149 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 150 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 151 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 152 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 153 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 154 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 155 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 156 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 157 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 158 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 159 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 160 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 161 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 162 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 163 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 164 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 165 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 166 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 167 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 168 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 169 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 170 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 171 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 172 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 173 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 174 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 175 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 176 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 177 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 178 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 179 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 180 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 181 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 182 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 183 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 184 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 185 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 186 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 187 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 188 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 189 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 190 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 191 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 192 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 193 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 194 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 195 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 196 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 197 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 198 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 199 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 200 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 201 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 202 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 203 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 204 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 205 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 206 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 207 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 208 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 209 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 210 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 211 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 212 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 213 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 214 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 215 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 216 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 217 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 218 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 219 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 220 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 221 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 222 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 223 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 224 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 225 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 226 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 227 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 228 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 229 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 230 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 231 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 232 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 233 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 234 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 235 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 236 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 237 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 238 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 239 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 240 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 241 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 242 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 243 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 244 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 245 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 246 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 247 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 248 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 249 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 250 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 251 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 252 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 253 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 254 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 255 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 256 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 257 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 258 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 259 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 260 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 261 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 262 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 263 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 264 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 265 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 266 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 267 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 268 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 269 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 270 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 271 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 272 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 273 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 274 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 275 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 276 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 277 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 278 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 279 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 280 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 281 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 282 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 283 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 284 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 285 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 286 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 287 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 288 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 289 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 290 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 291 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 292 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 293 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 294 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 295 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 296 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 297 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 298 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 299 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 300 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 301 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 302 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 303 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 304 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 305 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 306 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 307 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 308 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 309 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 310 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 311 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 312 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 313 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 314 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 315 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 316 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 317 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 318 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 319 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 320 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 321 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 322 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 323 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 324 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 325 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 326 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 327 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 328 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 329 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 330 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 331 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 332 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 333 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 334 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 335 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 336 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 337 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 338 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 339 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 340 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 341 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 342 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 343 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 344 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 345 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 346 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 347 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 348 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 349 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 350 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 351 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 352 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 353 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 354 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 355 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 356 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 357 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 358 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 359 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 360 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 361 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 362 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 363 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 364 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 365 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 366 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 367 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 368 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 369 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 370 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 371 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 372 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 373 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 374 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 375 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 376 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 377 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 378 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 379 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 380 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 381 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 382 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 383 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 384 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 385 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 386 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 387 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 388 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 389 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 390 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 391 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 392 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 393 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 394 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 395 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 396 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 397 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 398 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 399 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 400 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 401 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 402 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 403 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 404 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 405 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 406 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 407 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 408 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 409 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 410 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 411 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 412 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 413 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 414 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 415 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 416 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 417 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 418 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 419 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 420 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 421 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 422 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 423 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 424 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 425 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 426 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 427 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 428 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 429 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 430 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 431 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 432 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 433 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 434 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 435 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 436 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 437 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 438 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 439 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 440 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 441 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 442 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 443 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 444 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 445 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 446 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 447 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 448 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 449 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 450 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 451 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 452 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 453 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 454 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 455 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 456 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 457 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 458 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 459 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 460 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 461 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 462 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 463 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
