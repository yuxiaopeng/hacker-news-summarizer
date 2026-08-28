# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-08-28.md)

*最后自动更新时间: 2026-08-28 01:46:00*
## 1. 通过优化 1.1.1.1 的 DNS 缓存节省 100 TB 内存

**原文标题**: Saving 100 terabytes of memory by optimizing 1.1.1.1's DNS cache

**原文链接**: [https://blog.cloudflare.com/dns-cache-memory-optimization-1111/](https://blog.cloudflare.com/dns-cache-memory-optimization-1111/)

Cloudflare 优化了其名为“Big Pineapple”的 DNS 平台，该平台为 1.1.1.1 等服务管理着超过 2500 亿条缓存条目。通过实施五项连续的内存优化，工程团队将单个条目的占用空间缩减了 56%，并在其服务器集群中释放了约 100 TB 的内存。

五项核心优化包括：

1.  **使用 `Box` 替换 `Vec` 和 `String`**：由于 DNS 缓存条目在存储后是不可变的，向量和字符串中的“容量”（capacity）字段是冗余的。切换到 `Box<[T]>` 和 `Box<str>` 消除了这一开销并防止了过度分配。
2.  **合并列表**：不再将 DNS 区域（应答、权威和附加）存储在三个独立的列表中，而是改用 `u16` 偏移量将它们整合进单个列表。这减少了存储指针和长度所需的空间。
3.  **条件化所有者存储**：大多数 DNS 记录的所有者名称与查询名称一致。通过仅在两者不同（例如在 CNAME 链中）时存储所有者名称，否则进行推断，他们避免了数百万次冗余的堆分配。
4.  **对大型枚举变体进行装箱（Boxing）**：Rust 枚举的大小由其最大的变体决定。通过对罕见的大型记录类型（如 NAPTR）进行装箱，他们防止了常见的微型记录（如 A 和 AAAA）因未使用的内存填充而浪费空间。
5.  **线格式（Wire Format）存储**：他们从结构化枚举转向以单个 `Box<[u8]>` 的形式将记录数据存储为原始字节。这提高了内存局部性，并允许在构建响应时直接进行字节拷贝。

这些改进带来了巨大的效率提升：单个条目的内存占用从 953 字节降至 420 字节。与通常的性能权衡相反，这些优化还提升了性能：由于分配减少且 CPU 缓存局部性更好，插入吞吐量提升了 43%，查询延迟降低了 19%。

---

## 2. 小模型时代已经到来

**原文标题**: Small Models Have Arrived

**原文链接**: [https://calv.info/small-models-have-arrived](https://calv.info/small-models-have-arrived)

在《小模型已至》一文中，作者强调了人工智能领域的一个关键转变：高能力、低成本模型（如“gpt-5.6-luna”）的兴起。这些模型运行速度极快（约 100 tps），且成本显著降低——将复杂个性化任务的价格从约 1.00 美元降至 0.10 美元。

作者指出，高昂的 Token 成本是目前缺乏消费级 AI 公司的主要原因。传统的科技行业策略依赖低廉的运营成本来扩大用户规模，随后通过广告变现。此前，高昂的推理成本使这一模式无法实现，但新一代小模型首次让面向消费者的 AI 应用在经济上变得可行。

文章借鉴了 Segment 联合创始人 Peter Reinhardt 的见解，将工作分为两类：
1. **“IQ 180”型工作：** 深层的、创新的问题解决和科学突破。
2. **“Token 喷涌”型工作：** 构成约 95% 职业活动的协调、响应和行政性“基础事务”。

作者总结道，虽然前沿模型（如 Fable 5 或 5.6 Sol）在探索和硬核工程方面依然必不可少，但真正的市场爆发将源于“快速、廉价且够用”的模型。这些模型正准备接管驱动日常业务运作的大量“人类 Token”任务。这一转型的下一个障碍是开发必要的基础设施，包括安全防护、角色和权限管理，以将这些模型整合到专业工作流中。

---

## 3. 507种机械运动

**原文标题**: 507 Mechanical Movements

**原文链接**: [https://507movements.com/](https://507movements.com/)

生成摘要时出错

---

## 4. Show HN：OpenTIE 与 OpenXWA，《钛战机》和《X翼战机联盟》的现代移植版

**原文标题**: Show HN: OpenTIE and OpenXWA, Modern Ports of Tie Fighter and X-Wing Alliance

**原文链接**: [https://github.com/elyosh/OpenTIE/](https://github.com/elyosh/OpenTIE/)

本文介绍了 **OpenTIE** 和 **OpenXWA**，这是针对经典游戏《星球大战：钛战机》（Star Wars: TIE Fighter）和《星球大战：X翼战机联盟》（X-Wing Alliance）的开源重制项目，支持 Windows、macOS 和 Linux 系统。这些项目使原版游戏能够利用 Vulkan、Metal 和 Direct3D 12 等现代图形后端在当代硬件上原生运行。

**OpenTIE** 致力于提供“两全其美”的体验，允许玩家结合 1995 年收藏版 CD-ROM 和 1998 年 Windows 版的元素。推荐配置采用了 1995 年版的菜单和自适应 **iMUSE 配乐**（可根据任务事件动态响应），并结合了 1998 年版改进的飞行模拟系统和 3D 资源。

主要特性包括：
*   **增强图形：** “现代”模式增加了阴影、环境光遮蔽（AO）、光晕（Bloom）、HDR 和超分辨率技术（AMD FidelityFX FSR 3.1）。玩家可以通过 TAB 键在经典和现代视觉效果之间即时切换。
*   **性能提升：** 飞行引擎支持高达 240Hz 的刷新率，与原版相比，画面更平滑，操控响应更灵敏。
*   **高保真音频：** 内置 OPL3 模拟，并支持 Roland SC-55 硬件模拟或通过 FluidSynth 使用 SoundFonts 音色库。
*   **现代兼容性：** 原生支持现代飞行摇杆和手柄。

该软件不包含原版游戏资源；用户必须拥有 1995 或 1998 原版游戏（可在 GOG 或 Steam 购买）方可游玩。文章还重点介绍了姊妹项目 **OpenXWA**，该项目对《X翼战机联盟》进行了类似的现代化改造。这两个项目目前均处于积极开发阶段，并已在 GitHub 上发布。

---

## 5. Terminal-Bench-Science: Evaluating AI agents on scientific research workflows

**原文标题**: Terminal-Bench-Science: Evaluating AI agents on scientific research workflows

**原文链接**: [https://www.terminal-bench-science.ai/announcement](https://www.terminal-bench-science.ai/announcement)

**Terminal-Bench-Science** is a new, continuous benchmark led by Stanford University designed to evaluate AI agents on authentic scientific research workflows. Unlike traditional benchmarks that rely on textbook questions, Terminal-Bench-Science features 70 expert-curated tasks drawn from real-world practices in the life, physical, Earth, mathematical, and engineering sciences.

The benchmark’s primary goal is to drive the development of AI agents that can serve as effective research assistants, handling technically demanding tasks—such as data analysis, simulation, and theorem proving—to free scientists for higher-level judgment and discovery. 

Key findings from the version 0.1 release include:
*   **Performance Gap:** Current frontier models find these tasks highly challenging. **Claude Opus 5** achieved the highest resolution rate at only **30.0%**, followed by GPT-5.6 Sol (22.4%) and Claude Fable 5 (21.4%).
*   **Rigorous Selection:** The tasks are subject to a strict peer-review process. Out of 920 initial proposals from the global scientific community, only 70 (7.6%) were accepted for the initial release, ensuring tasks are objectively verifiable and genuinely difficult.
*   **Efficiency Metrics:** Beyond resolution rates, the benchmark tracks total evaluation costs and token usage. Claude Opus 5 and GPT-5.6 Sol currently define the Pareto frontier for performance, though costs remain high (e.g., $7.0k for an Opus 5 evaluation run).

Terminal-Bench-Science is designed to evolve alongside AI advancements. The team has already begun work on version 0.2 (due late 2026), maintaining an open invitation for researchers to contribute workflows that challenge current frontier models. By creating a feedback loop between scientific needs and AI development, the project aims to accelerate the pace of global scientific discovery.

---

## 6. Gemini-3.5-转录

**原文标题**: Gemini-3.5-Transcribe

**原文链接**: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/)

谷歌推出了 Gemini 3.5 Transcribe，这是一款旨在实现高精度、智能化音频处理的新一代语音转文字模型。该模型超越了传统的识别工具，具备“智能转录”功能，能够自动过滤语气词（如“嗯”、“啊”）、处理自我纠正并实时进行文本格式化。

**核心技术亮点：**
*   **性能：** 该模型在预录制音频中的词错率 (WER) 为 2.6%，流式传输为 4.0%。与之前的 Chirp 3 模型相比，转录延迟降低了 70%。
*   **功能：** 支持超过 85 种语言、多发言人识别（最多三人）以及针对专业术语的自定义词库。
*   **高级功能：** 一项突出的功能是支持“函数调用”，允许用户直接通过语音命令执行复杂任务，例如生成图像或分析文件。

**集成与可用性：**
该模型通过两个 API 提供：用于亚秒级双向流式传输的 **Live API**，以及用于处理带有时间戳的录制内容的 **Interactions API**。

面向消费者的应用包括：
*   **Gboard 上的 Rambler (Android)：** 将口述想法转化为精炼、格式规范的文本。
*   **Gemini macOS 应用：** 实现语音驱动的工作流和屏幕语境感知。
*   **Google Antigravity：** 利用聊天记录和屏幕语境确保精准度。
*   **即将推出：** Chrome 浏览器的“语音输入”功能。

Gemini 3.5 Transcribe 目前处于公开预览阶段，开发者可通过 Google AI Studio 和 Gemini Enterprise Agent Platform 获取，并得到了 Vercel、LangChain 和 LiveKit 等合作伙伴的支持。

---

## 7. Show HN：我们构建了 OpenRouter，将使用数据转化为更优的模型

**原文标题**: Show HN: We built open OpenRouter that turns usage into a better model

**原文链接**: [https://github.com/experientiallabs/experiential](https://github.com/experientiallabs/experiential)

**Experiential** 是一款开源网关和路由器，旨在简化并优化 AI 代理（Agent）工作流。它提供了一个统一且兼容 OpenAI 的 API，使开发人员能够访问来自 OpenAI、Anthropic、Gemini 和 Azure 等供应商的托管、本地及自带密钥 (BYOK) 模型。

该平台提供三大核心价值主张：

1.  **集中管控：** 它作为一个管理层，允许开发人员管控特定用户或代理访问哪些模型。它包含针对具体用例的细粒度控制，并提供预算管理工具以限制支出。
2.  **流量驱动的优化：** Experiential 的独特之处在于能将生产数据转化为更佳的性能。通过收集代理交互中的 OpenTelemetry (OTLP) 追踪数据，用户可以运行模拟并构建针对其特定需求优化的自定义路由器。
3.  **模型微调：** 除了路由功能，该工具还允许用户利用收集的遥测数据微调开源模型（通过 `exp optimize` 命令），从而提高特定任务的质量、速度和成本效益。

**快速入门：**
用户可以使用 `pip install experiential` 部署本地网关，或访问 `experientiallabs.ai` 使用托管平台。该系统旨在轻松集成 Claude Code、Cursor 和 Aider 等流行的编程代理。虽然系统默认包含匿名聚合产品遥测数据以改进工具，但它不会截获提示词、凭据或原始客户内容，用户可以通过 CLI 选择退出。

总之，Experiential 充当了一个“智能”中间层，帮助开发人员根据实际使用数据，从通用的 LLM 使用方案过渡到高度优化、针对特定任务的模型部署。

---

## 8. AI Engineer Notebooks – free, framework-free RAG/agents/evals on Colab

**原文标题**: AI Engineer Notebooks – free, framework-free RAG/agents/evals on Colab

**原文链接**: [https://github.com/calmrocks/ai-engineer-notebooks](https://github.com/calmrocks/ai-engineer-notebooks)

生成摘要时出错

---

## 9. 微鸭

**原文标题**: Microduck

**原文链接**: [https://pollen-robotics.com/microduck/](https://pollen-robotics.com/microduck/)

**Microduck** 是一款身高 25 厘米的开源双足机器人，专为开发者和爱好者探索强化学习（RL）而设计。由 Pollen Robotics 打造的“AV-1 Microduck”专注于“从仿真到现实”（sim-to-real）的工作流，允许用户在物理模拟器（MuJoCo）中训练运动策略，并将其直接部署到硬件上。

**关键技术规格：**
*   **硬件：** 15 个电机、集成激光雷达（LiDAR）、摄像头和双惯性测量单元（IMU）。
*   **性能：** 重量 800 克，板载策略循环运行频率为 50 Hz。
*   **软件：** 完全开源（Apache-2.0 协议），SDK 和强化学习训练栈已在 GitHub 上线。

该机器人具备“开箱即用”的功能，内置七种预训练行为，包括行走、坐下、踢球、抓取以及跌倒后自恢复。在配备特定配件时，它甚至支持轮滑运动。官方鼓励用户重新训练这些行为，或创造全新的“技能”通过 Discord 与社区分享。

**价格与发售信息：**
*   **价格：** 首发价 399 美元（不含税及运费）。
*   **预订：** 2026 年 8 月 27 日开启。
*   **发货：** 预计 2026 年圣诞节前。
*   **定制化：** 提供四种配色，可选购包含备件和积分的 **开发者包（Dev pack）**（119 美元）以及用于互动游戏的 **配件包（Accessory pack）**（39 美元）。

通过将易于获取的硬件与专业级训练栈相结合，Microduck 旨在降低学习和实验高级机器人运动控制的门槛。

---

## 10. We found a division by zero bug in FFmpeg with a vibecoded fuzzer

**原文标题**: We found a division by zero bug in FFmpeg with a vibecoded fuzzer

**原文链接**: [https://code.ffmpeg.org/FFmpeg/FFmpeg/issues/24290](https://code.ffmpeg.org/FFmpeg/FFmpeg/issues/24290)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 2 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 3 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 4 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 5 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 6 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 7 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 8 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 9 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 10 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 11 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 12 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 13 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 14 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 15 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 16 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 17 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 18 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 19 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 20 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 21 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 22 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 23 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 24 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 25 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 26 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 27 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 28 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 29 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 30 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 31 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 32 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 33 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 34 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 35 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 36 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 37 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 38 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 39 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 40 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 41 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 42 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 43 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 44 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 45 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 46 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 47 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 48 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 49 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 50 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 51 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 52 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 53 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 54 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 55 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 56 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 57 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 58 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 59 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 60 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 61 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 62 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 63 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 64 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 65 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 66 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 67 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 68 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 69 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 70 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 71 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 72 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 73 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 74 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 75 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 76 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 77 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 78 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 79 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 80 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 81 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 82 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 83 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 84 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 85 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 86 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 87 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 88 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 89 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 90 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 91 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 92 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 93 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 94 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 95 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 96 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 97 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 98 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 99 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 100 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 101 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 102 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 103 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 104 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 105 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 106 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 107 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 108 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 109 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 110 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 111 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 112 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 113 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 114 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 115 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 116 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 117 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 118 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 119 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 120 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 121 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 122 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 123 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 124 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 125 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 126 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 127 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 128 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 129 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 130 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 131 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 132 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 133 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 134 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 135 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 136 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 137 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 138 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 139 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 140 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 141 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 142 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 143 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 144 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 145 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 146 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 147 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 148 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 149 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 150 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 151 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 152 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 153 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 154 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 155 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 156 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 157 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 158 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 159 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 160 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 161 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 162 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 163 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 164 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 165 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 166 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 167 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 168 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 169 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 170 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 171 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 172 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 173 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 174 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 175 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 176 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 177 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 178 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 179 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 180 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 181 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 182 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 183 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 184 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 185 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 186 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 187 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 188 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 189 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 190 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 191 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 192 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 193 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 194 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 195 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 196 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 197 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 198 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 199 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 200 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 201 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 202 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 203 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 204 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 205 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 206 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 207 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 208 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 209 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 210 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 211 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 212 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 213 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 214 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 215 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 216 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 217 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 218 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 219 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 220 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 221 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 222 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 223 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 224 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 225 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 226 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 227 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 228 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 229 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 230 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 231 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 232 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 233 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 234 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 235 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 236 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 237 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 238 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 239 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 240 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 241 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 242 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 243 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 244 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 245 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 246 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 247 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 248 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 249 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 250 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 251 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 252 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 253 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 254 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 255 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 256 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 257 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 258 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 259 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 260 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 261 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 262 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 263 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 264 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 265 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 266 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 267 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 268 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 269 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 270 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 271 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 272 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 273 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 274 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 275 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 276 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 277 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 278 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 279 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 280 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 281 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 282 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 283 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 284 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 285 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 286 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 287 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 288 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 289 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 290 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 291 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 292 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 293 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 294 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 295 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 296 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 297 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 298 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 299 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 300 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 301 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 302 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 303 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 304 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 305 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 306 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 307 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 308 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 309 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 310 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 311 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 312 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 313 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 314 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 315 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 316 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 317 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 318 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 319 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 320 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 321 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 322 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 323 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 324 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 325 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 326 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 327 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 328 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 329 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 330 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 331 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 332 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 333 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 334 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 335 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 336 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 337 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 338 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 339 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 340 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 341 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 342 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 343 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 344 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 345 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 346 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 347 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 348 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 349 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 350 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 351 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 352 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 353 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 354 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 355 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 356 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 357 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 358 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 359 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 360 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 361 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 362 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 363 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 364 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 365 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 366 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 367 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 368 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 369 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 370 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 371 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 372 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 373 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 374 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 375 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 376 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 377 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 378 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 379 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 380 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 381 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 382 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 383 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 384 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 385 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 386 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 387 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 388 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 389 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 390 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 391 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 392 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 393 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 394 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 395 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 396 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 397 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 398 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 399 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 400 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 401 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 402 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 403 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 404 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 405 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 406 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 407 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 408 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 409 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 410 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 411 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 412 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 413 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 414 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 415 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 416 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 417 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 418 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 419 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 420 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 421 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 422 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 423 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 424 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 425 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 426 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 427 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 428 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 429 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 430 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 431 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 432 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 433 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 434 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 435 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 436 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 437 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 438 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 439 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 440 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 441 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 442 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 443 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 444 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 445 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 446 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 447 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 448 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 449 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 450 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 451 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 452 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 453 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 454 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 455 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 456 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 457 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 458 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 459 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 460 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 461 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 462 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 463 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 464 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 465 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 466 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 467 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 468 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 469 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 470 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 471 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 472 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 473 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 474 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 475 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 476 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 477 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 478 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 479 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 480 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 481 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 482 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 483 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 484 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 485 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 486 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 487 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 488 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 489 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 490 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 491 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 492 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 493 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 494 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 495 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 496 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 497 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 498 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 499 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 500 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 501 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 502 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 503 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 504 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 505 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 506 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 507 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 508 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 509 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 510 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 511 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 512 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 513 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 514 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 515 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 516 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 517 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 518 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 519 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 520 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 521 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 522 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 523 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 524 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
