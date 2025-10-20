# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-10-20.md)

*最后自动更新时间: 2025-10-20 17:48:36*
## 1. BERT 只是一个单步文本扩散

**原文标题**: BERT Is Just a Single Text Diffusion Step

**原文链接**: [https://nathan.rs/posts/roberta-diffusion/](https://nathan.rs/posts/roberta-diffusion/)

本文探讨了BERT风格的掩码语言模型与文本扩散模型之间的联系。作者证明了BERT，通常用于分类等任务，可以通过将其掩码语言建模（MLM）目标定义为离散扩散过程中的一步，从而适应于文本生成。

核心思想是文本扩散模型逐步向文本添加噪声（掩码tokens），然后训练模型来逆转这个过程，迭代地去噪并恢复原始文本。BERT凭借其MLM目标，已经在特定掩码率下执行去噪。通过以可变的掩码率和去噪步骤计划训练BERT，作者将其转化为生成模型。

作者在WikiText数据集上微调了一个RoBERTa模型，修改了训练过程以纳入变化的掩码概率。在推理过程中，模型从一个部分掩码的序列开始，并迭代地预测tokens，根据预定义的计划在每个步骤重新掩码。

结果表明，这种简单的实现可以生成出人意料的连贯文本，尽管它比GPT-2略慢且连贯性稍差。作者承认，更复杂的扩散技术，如AR-Diffusion和Skip-Step Diffusion，以及优化的实现，可以极大地提高性能。

主要结论是，BERT风格的模型，通过对其训练目标进行略微修改，可以通过将可变速率掩码解释为离散扩散过程，从而重新用作生成引擎。这验证了BERT模型从根本上与文本扩散模型相关联的想法，只是在固定的掩码率下训练。

---

## 2. 生产环境RAG：我处理500万+文档的经验总结

**原文标题**: Production RAG: what I learned from processing 5M+ documents

**原文链接**: [https://blog.abdellatif.io/production-rag-processing-5m-documents](https://blog.abdellatif.io/production-rag-processing-5m-documents)

本文详细介绍了作者为两家人工智能企业构建可用于生产环境的 RAG 系统的经验，处理了超过 500 万份文档。他们最初使用 Langchain 和 Llamaindex 进行快速原型设计，但发现性能不佳，并花费数月时间改进了方法。

主要改进包括：

*   **查询生成：** 通过从对话线程生成多个语义和关键词查询来扩大搜索范围。
*   **重排序：** 通过智能选择最相关的块来显著改善结果，甚至弥补了不太理想的初始设置。50 个块输入到 15 个块输出的配置被证明是最佳的。
*   **分块策略：** 认识到定制分块的重要性，他们强调创建逻辑上的、独立的块，而不切割单词或句子。他们最初使用 Unstructured.io，然后使用自定义解决方案。
*   **元数据注入：** 通过包含相关元数据（标题、作者）以及块文本来丰富提供给 LLM 的上下文。
*   **查询路由：** 实施一个路由器来处理非 RAG 相关的问题（总结、作者识别），直接使用 API 调用 + LLM。

作者的技术栈演变如下：

*   **向量数据库：** Azure -> Pinecone -> Turbopuffer
*   **文档提取：** 自定义
*   **嵌入：** text-embedding-large-3
*   **重排序器：** 无 -> Cohere 3.5 -> Zerank
*   **LLM：** GPT 4.1 -> GPT 5 -> GPT 4.1

他们的经验教训已被编译成一个开源项目，agentset-ai/agentset (MIT 许可证)。

---

## 3. AWS us-east-1区域多项服务中断

**原文标题**: AWS Multiple Services Down in us-east-1

**原文链接**: [https://health.aws.amazon.com/health/status?ts=20251020](https://health.aws.amazon.com/health/status?ts=20251020)

无法访问文章链接。

---

## 4. 阿里云称其新型池化系统将英伟达AI GPU使用率降低了82%

**原文标题**: Alibaba Cloud says it cut Nvidia AI GPU use by 82% with new pooling system

**原文链接**: [https://www.tomshardware.com/tech-industry/semiconductors/alibaba-says-new-pooling-system-cut-nvidia-gpu-use-by-82-percent](https://www.tomshardware.com/tech-industry/semiconductors/alibaba-says-new-pooling-system-cut-nvidia-gpu-use-by-82-percent)

阿里云宣称其新型Aegaeon池化系统可大幅减少大型语言模型(LLM)推理所需的英伟达GPU数量。一篇即将于会议上发表的同行评审论文详细介绍了Aegaeon如何在阿里巴巴Model Studio的beta测试中实现GPU使用率降低82%。这意味着只需使用213个GPU即可支持高达720亿参数的各种LLM，而此前需要1,192个。

Aegaeon通过在token级别虚拟化访问来优化GPU利用率，允许一个GPU同时服务于多个模型。与旧的无服务器系统相比，这使得“有效吞吐量”（衡量有效输出的指标）提高了九倍。该系统在生成输出时动态分配计算能力，进一步优化了资源分配。

测试使用了英伟达H20 GPU，该GPU目前在中国有售，但受美国出口管制。 阿里巴巴将收益归功于每个GPU封装多个模型以及使用token级别的自动缩放器。 虽然具体的网络基础设施尚未详细说明，但阿里巴巴在集成GPU服务堆栈方面的专业知识表明，结果可能受到高度优化环境的影响。 尽管如此，这些发现可能会引起其他寻求最大限度提高现有加速器集群效率的云提供商的兴趣。

---

## 5. 太空电梯

**原文标题**: Space Elevator

**原文链接**: [https://neal.fun/space-elevator/](https://neal.fun/space-elevator/)

无法访问文章链接。

---

## 6. 深寻 OCR

**原文标题**: DeepSeek OCR

**原文链接**: [https://github.com/deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR)

DeepSeek OCR：一款基于大语言模型的视觉-文本压缩OCR模型 (目标发布时间: 2025/x/x)。本文档提供DeepSeek-OCR的安装和使用说明，用于光学字符识别（OCR）任务。

安装需要特定环境（cuda11.8+torch2.6.0），包括克隆仓库、创建conda环境以及安装必要的软件包，如`torch`、`torchvision`、`torchaudio`、`vllm`、`flash-attn`以及 `requirements.txt` 中的依赖项。文档提供了 vLLM 和 Transformers 两种推理方式的说明。

对于 vLLM 推理，用户需要在 `config.py` 中配置输入/输出路径，并可以运行脚本进行图像、PDF 和批量评估。对于 Transformers 推理，文档提供了代码示例，展示了如何加载模型和分词器，以及如何使用特定的提示词和图像文件执行 OCR。此外，还提供了一个 `run_dpsk_ocr.py` 脚本。

该模型支持不同的原生分辨率（Tiny、Small、Base、Large）和一个动态分辨率模式（"Gundam"）。文档给出了各种提示词示例，用于不同的 OCR 任务，包括文档转换、通用 OCR、图像描述和文本定位。

开发者感谢并致敬了启发 DeepSeek OCR 的多个模型和基准，包括 Vary、GOT-OCR2.0、MinerU、PaddleOCR、OneChart、Slow Perception、Fox 和 OminiDocBench。引用信息即将发布。

---

## 7. 如何干净地停止 Linux 线程

**原文标题**: How to stop Linux threads cleanly

**原文链接**: [https://mazzo.li/posts/stopping-linux-threads.html](https://mazzo.li/posts/stopping-linux-threads.html)

本文探讨了干净地停止 Linux 线程所面临的挑战，重点在于确保正确清理诸如内存、锁和日志等资源。文章强调了实现这一目标的困难，尤其是在处理阻塞系统调用或无法直接控制的代码时。

作者首先提出了一种简单的“准忙循环”方法，线程定期检查一个布尔标志以确定是否终止。然而，当线程无限期地阻塞在系统调用上时，这种方法是不合适的。

文章随后深入探讨了使用信号中断线程的复杂性。信号虽然是一种中断执行的机制，但如果处理不当，可能会导致资源泄漏和不一致状态等问题。作者批评通过 `pthread_cancel` 取消线程是不安全的，因为它可能会在关键部分内中断，尤其是在使用 RAII 的 C++ 程序中，强制解栈可能会导致 `std::terminate`。

文章提倡受控线程取消或自制的基于信号的方法。这涉及到有选择地启用取消或在进行阻塞系统调用之前检查一个标志（由信号处理程序触发）。然而，这可能会引入竞争条件。

最后，文章强调了使用具有原子信号掩码操作能力的系统调用的重要性，例如 `pselect`、`ppoll` 和 `epoll_pwait`，以及如何使用这些系统调用来干净地中断许多系统调用。文章承认这些方法的局限性，并提出了一种通用策略，用于解决在无法原子地更改信号掩码的情况下的问题。

---

## 8. 使用MOPA激光雕刻机制作的光学衍射图案 [视频]

**原文标题**: Optical diffraction patterns made with a MOPA laser engraving machine [video]

**原文链接**: [https://www.youtube.com/watch?v=RsGHr7dXLuI](https://www.youtube.com/watch?v=RsGHr7dXLuI)

YouTube视频，标题为“使用MOPA激光雕刻机制作的光学衍射图案”，可能展示了使用MOPA（主振荡功率放大器）激光雕刻机创建或演示光学衍射图案的过程。视频标题强烈暗示了当光波通过障碍物或孔径时产生的干涉图案的视觉展示。

然而，所提供的内容仅仅是一个通用的YouTube页脚，包含版权信息、联系方式、广告链接以及其他标准的法律和平台信息。这并没有描述视频本身的内容。

因此，仅根据标题判断，该视频可能演示了如何使用MOPA激光雕刻机来创建结构或图案，这些结构或图案在被照亮时会产生可见的光学衍射图案。该视频很可能展示了创建这些结构的过程以及由此产生的衍射效应。由于所提供的内容是样板式的YouTube法律文本，因此在不观看视频本身的情况下，不可能提供更详细的摘要。

---

## 9. 伺服 v0.0.1

**原文标题**: Servo v0.0.1

**原文链接**: [https://github.com/servo/servo](https://github.com/servo/servo)

Servo v0.0.1 是一个用 Rust 开发的原型网页浏览器引擎，专为并行处理而设计。它支持 macOS、Linux、Windows、OpenHarmony 和 Android，并欢迎贡献。开发工作通过 GitHub Issues、Zulip 和视频会议进行协调。

本文档为每个支持的操作系统提供了快速启动构建说明。对于 macOS，它涉及安装 Xcode、brew、uv 和 rustup，然后运行 `./mach bootstrap` 和 `./mach build`。在 Linux 上，它概述了 curl、uv 和 rustup 的安装，然后是相同的 `mach` 命令。Windows 需要下载 uv、choco 和 rustup，确保安装特定的 Visual Studio 组件，然后使用 `.\mach bootstrap` 和 `.\mach build`。

Android 开发需要设置 `ANDROID_SDK_ROOT` 和 `ANDROID_NDK_ROOT` 环境变量。该文档列出了使用 Android 命令行工具安装的组件，然后是主机平台的标准构建说明。

OpenHarmony 开发建立在您的主机操作系统设置之上，需要 `DEVECO_SDK_HOME` 和 `OHOS_BASE_SDK_HOME` 环境变量，以及通过 `SERVO_OHOS_SIGNING_CONFIG` 指定的 demo 应用签名配置文件路径。目标发行版可以使用 `mach` 命令中的 `--flavor` 标志指定。

---

## 10. Docker 系统状态：服务完全中断

**原文标题**: Docker Systems Status: Full Service Disruption

**原文链接**: [https://www.dockerstatus.com/pages/incident/533c6539221ae15e3f000031/68f5e1c741c825463df7486c](https://www.dockerstatus.com/pages/incident/533c6539221ae15e3f000031/68f5e1c741c825463df7486c)

2025年10月20日，Docker遭遇全面服务中断，影响包括Registry、Hub、Scout、DBC和DHI在内的多个组件。此次中断影响了Docker Hub Registry、身份验证、Web服务、账单、自动构建、安全扫描、Docker Scout、Docker Build Cloud、Testcontainers Cloud、Docker Cloud以及Docker Hardened Images。

该事件始于太平洋夏令时00:16（世界协调时07:16）左右，Docker检测到访问和使用其服务的广泛问题。他们立即展开调查并尽快汇报情况。

太平洋夏令时01:22（世界协调时08:22），Docker确定根本问题源于其云服务提供商之一出现故障。他们监控情况并准备系统进行解决。

太平洋夏令时02:43（世界协调时09:43），Docker报告称其SaaS服务错误率正在恢复，并在处理积压工作的同时继续监控。

该事件于太平洋夏令时03:05（世界协调时10:05）解决。状态页面提供了通过电子邮件、Webhook、RSS订阅源和Slack接收更新的选项。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 2 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 3 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 4 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 5 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 6 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 7 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 8 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 9 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 10 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 11 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 12 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 13 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 14 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 15 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 16 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 17 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 18 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 19 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 20 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 21 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 22 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 23 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 24 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 25 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 26 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 27 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 28 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 29 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 30 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 31 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 32 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 33 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 34 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 35 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 36 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 37 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 38 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 39 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 40 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 41 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 42 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 43 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 44 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 45 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 46 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 47 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 48 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 49 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 50 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 51 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 52 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 53 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 54 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 55 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 56 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 57 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 58 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 59 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 60 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 61 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 62 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 63 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 64 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 65 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 66 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 67 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 68 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 69 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 70 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 71 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 72 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 73 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 74 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 75 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 76 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 77 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 78 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 79 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 80 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 81 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 82 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 83 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 84 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 85 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 86 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 87 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 88 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 89 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 90 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 91 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 92 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 93 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 94 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 95 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 96 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 97 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 98 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 99 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 100 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 101 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 102 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 103 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 104 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 105 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 106 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 107 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 108 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 109 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 110 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 111 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 112 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 113 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 114 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 115 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 116 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 117 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 118 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 119 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 120 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 121 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 122 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 123 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 124 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 125 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 126 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 127 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 128 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 129 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 130 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 131 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 132 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 133 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 134 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 135 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 136 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 137 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 138 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 139 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 140 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 141 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 142 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 143 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 144 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 145 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 146 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 147 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 148 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 149 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 150 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 151 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 152 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 153 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 154 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 155 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 156 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 157 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 158 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 159 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 160 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 161 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 162 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 163 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 164 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 165 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 166 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 167 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 168 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 169 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 170 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 171 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 172 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 173 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 174 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 175 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 176 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 177 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 178 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 179 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 180 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 181 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 182 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 183 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 184 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 185 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 186 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 187 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 188 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 189 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 190 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 191 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 192 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 193 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 194 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 195 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 196 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 197 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 198 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 199 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 200 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 201 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 202 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 203 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 204 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 205 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 206 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 207 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 208 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 209 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 210 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 211 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 212 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 213 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 214 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 215 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
