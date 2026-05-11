# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-05-11.md)

*最后自动更新时间: 2026-05-11 19:23:41*
## 1. CUDA-oxide：英伟达官方 Rust 转 CUDA 编译器

**原文标题**: CUDA-oxide: Nvidia's official Rust to CUDA compiler

**原文链接**: [https://nvlabs.github.io/cuda-oxide/index.html](https://nvlabs.github.io/cuda-oxide/index.html)

**CUDA-oxide** 是英伟达（Nvidia）推出的一个实验性官方项目，旨在支持使用地道的、具有一定安全性的 Rust 语言开发 CUDA 核函数。它不依赖领域特定语言（DSL）或外部语言绑定，而是利用自定义的 `rustc` 代码生成后端，将标准 Rust 代码直接编译为 PTX（并行线程执行）代码。

该项目的主要特性包括：
*   **GPU 上的地道 Rust：** 开发者可以利用 Rust 强大的类型系统、所有权模型、Trait 和泛型来编写 SIMT（单指令多线程）核函数。
*   **异步集成：** 编译器支持 `async/.await` 等现代 Rust 特性，允许用户将 GPU 工作组合成惰性的 `DeviceOperation` 图，并在流池（stream pools）中调度任务。
*   **精简的工作流：** 通过 `#[cuda_module]` 和 `#[kernel]` 等宏，该工具可自动将设备侧构件嵌入主机二进制文件，并生成类型化的启动方法。它还引入了 `cargo oxide` 命令用于构建和运行项目。
*   **内存管理：** 其 API 包含 `DeviceBuffer` 和 `DisjointSlice` 等专门类型，用以安全地处理数据传输和 GPU 内存访问。

目前该项目处于 **v0.1.0 alpha** 版本，尚在早期阶段。英伟达提醒用户可能会遇到 Bug、功能不完整以及频繁的 API 变更。尽管仍处于实验状态，但 CUDA-oxide 代表了将内存安全和现代编程抽象引入高性能 GPU 计算的重要一步。

---

## 2. 有人能解释一下 Cloudflare 是否勒索了 Canonical 吗？

**原文标题**: Can Someone Please Explain Whether Cloudflare Blackmailed Canonical?

**原文链接**: [https://www.flyingpenguin.com/can-someone-please-explain-whether-cloudflare-blackmailed-canonical/](https://www.flyingpenguin.com/can-someone-please-explain-whether-cloudflare-blackmailed-canonical/)

本文调查了 2026 年 4 月针对 Canonical (Ubuntu) 发起的大规模 DDoS 攻击，并质疑 Cloudflare 的商业模式是否构成了现代版的“保护费勒索”。

该攻击由“313 团队”声称负责，利用了一个名为“Beamed”的商业 DDoS 攻击服务。作者指出了其中严重的利益冲突：Cloudflare 在托管并保护“Beamed”基础设施的同时，却向受害者 Canonical 收取 DDoS 缓解费用以结束干扰。在这种“选择性接入”的情况下，Canonical 在攻击中途将其最关键的软件仓库端点迁移至 Cloudflare 的付费服务，以恢复全球范围内的安全更新访问。

作者强调了 2026 年 2 月 27 日（即攻击前两个月）发生的系列可疑且同步的事件。当天，攻击者注册商（与海盗湾创始人及活动家 Naomi Colvin 有关）的路由基础设施变更了司法管辖区。与此同时，Canonical 为随后遭受攻击的特定主机名签发了新的“顶级”证书，而这是将服务迁移至 Cloudflare 等 CDN 后台的技术前提。

文章指出，Cloudflare 通过免费托管攻击工具并向受害者收取救济费用，形成了一种自我维持的收入流。作者将其比作 20 世纪 30 年代 Moses Annenberg 的电讯社垄断——当时同一实体控制了威胁产生与企业生存所需的信息流。通过保持“内容中立”，Cloudflare 从冲突双方中获利，实际上将攻击服务的持续存在变成了缴纳保护费的“无声要求”。作者认为，即使这并非一场协同阴谋，其架构结果在功能上也与敲诈勒索无异。

---

## 3. Nullsoft, 1997-2004 (2004)

**原文标题**: Nullsoft, 1997-2004 (2004)

**原文链接**: [https://slate.com/technology/2004/11/the-death-of-the-last-maverick-tech-company.html](https://slate.com/technology/2004/11/the-death-of-the-last-maverick-tech-company.html)

生成摘要时出错

---

## 4. Ratty – 支持内联 3D 图形的终端模拟器

**原文标题**: Ratty – A terminal emulator with inline 3D graphics

**原文链接**: [https://ratty-term.org/](https://ratty-term.org/)

**Ratty** 是一款创新的终端模拟器，其独特之处在于能够在命令行界面内直接渲染**行内 3D 图形**。传统的终端通常局限于显示文本和基础 2D 图像，而 Ratty 扩展了终端的视觉功能，允许 3D 模型和环境与标准输出原生地并排显示。

该项目为用户和开发者提供了三类主要资源：
*   **文档：** 详述软件技术实现和使用场景的专题博客文章。
*   **获取方式：** 为希望测试该模拟器的用户提供直接下载链接。
*   **开源：** 开放源代码，允许社区贡献，并确保 3D 渲染集成至终端环境的透明度。

总之，Ratty 旨在通过弥合文本工作流与高保真图形可视化之间的差距，实现终端体验的现代化。

---

## 5. 用 Swift 训练 LLM（第一部分）：将矩阵乘法性能从 Gflop/s 提升至 Tflop/s

**原文标题**: Training an LLM in Swift, Part 1: Taking matrix mult from Gflop/s to Tflop/s

**原文链接**: [https://www.cocoawithlove.com/blog/matrix-multiplications-swift.html](https://www.cocoawithlove.com/blog/matrix-multiplications-swift.html)

In this article, the author explores optimizing handwritten Swift code for training a Large Language Model (LLM) on Apple Silicon, aiming to match or exceed the performance of Andrej Karpathy’s `llm.c` (a plain C GPT-2 implementation). 

The author identifies that a standard "naive" Swift port is significantly slower than C—performing at only 2.8 Gflop/s, or about 7% of the C implementation's speed. To close this gap, the author details several key optimizations leveraging features in **Swift 6.2** and the **Swift-Numerics** library:

1.  **Eliminating Array Overhead:** The author notes that Swift’s standard `Array` type incurs significant overhead due to uniqueness checks and Copy-on-Write (COW) mutations. By utilizing the new **`MutableSpan`** type, the code achieves direct, low-overhead memory access, which triples the speed of training iterations.
2.  **Enabling Fused Multiply-Add (FMA):** Unlike C, which uses the `-ffast-math` flag to combine multiplication and addition into a single CPU instruction, Swift defaults to more precise, separate operations. By using **`Relaxed.multiplyAdd`** from the Swift-Numerics package, the author forces the compiler to use SIMD-vectorized FMA instructions, resulting in a 10x performance boost.
3.  **Loop Unrolling with `InlineArray`:** To match C’s efficiency in loop unrolling, the author utilizes **`InlineArray`**, a Swift 6.2 feature that allows for stack-allocated arrays. This avoids the heap allocation costs of standard arrays when storing temporary results during matrix multiplication.

Through these steps, the author demonstrates that by bypassing high-level safety abstractions in favor of modern, low-level Swift features, it is possible to transform Swift from a "slow" language for mathematics into a high-performance engine capable of Tflop/s-scale throughput on Apple Silicon.

---

## 6. Gmail 注册现在需要扫描二维码并发送短信

**原文标题**: Gmail registration now requires scanning a QR code and sending a text message

**原文链接**: [https://discuss.privacyguides.net/t/google-account-registration-now-requires-sending-an-sms-via-phone-instead-of-receiving-an-sms/36082](https://discuss.privacyguides.net/t/google-account-registration-now-requires-sending-an-sms-via-phone-instead-of-receiving-an-sms/36082)

**摘要：**

据报道，谷歌更新了 Gmail 注册流程，要求用户使用智能手机扫描二维码。此操作会触发用户设备向谷歌发送一条外发短信，以验证手机号码。

此次更改的主要目的是增强安全性并防止机器人自动注册。然而，由于验证过程依赖于直接从硬件设备发送的短信，这有效地屏蔽了 SMSPool 等虚拟号码服务的使用。虽然这增加了批量注册账号的难度，但也给那些希望在不使用传统个人手机套餐的情况下注册账号的用户带来了挑战。

---

## 7. AMÁLIA与欧洲葡萄牙语大语言模型的未来

**原文标题**: AMÁLIA and the future of European Portuguese LLMs

**原文链接**: [https://duarteocarmo.com/blog/amalia-and-the-future-of-european-portuguese-llms](https://duarteocarmo.com/blog/amalia-and-the-future-of-european-portuguese-llms)

本文对 AMÁLIA 进行了批判性分析。这是一项耗资 550 万欧元的政府资助计划，旨在开发一个专门针对欧洲葡萄牙语的“完全开源”大语言模型（LLM）。该模型由葡萄牙研究机构联盟（NOVA、IST、IT 和 FCT）开发，是现有 EuroLLM 架构的延伸，而非从零开始构建的项目。

作者强调了几个关键点：

*   **训练与性能：** AMÁLIA 侧重于以数据为中心的改进，利用了 Arquivo.pt 数据和合成的葡萄牙语数据集。在包括新创建的 **ALBA** 基准测试在内的多项葡萄牙语指标中，其表现优于 Qwen 3-8B 等前沿模型。
*   **“开源”疑问：** 一个主要的批评点是目前缺乏透明度。尽管宣传为开源，但作者指出，在撰写本文时，模型权重、训练日志和数据集尚未向公众开放。
*   **数据代表性：** 作者对所使用的特定欧洲葡萄牙语数据量表示担忧。在扩展预训练阶段的 1070 亿个 Token 中，只有约 5.5% 被确认为欧洲葡萄牙语，这引发了关于该模型专业化程度是否足够的质疑。
*   **文化基准测试：** 虽然该项目创建了四个新的基准测试，但作者认为它们过于侧重于语法和句法。他们建议，一个真正的“葡萄牙语”模型应该针对该国特定的文化、历史和地理等内在知识进行测试。

**结论：** 作者认为 AMÁLIA 是葡萄牙人工智能领域迈出的重要且令人印象深刻的第一步。然而，作者强调，为了让该项目真正造福国家，团队必须优先发布模型权重和数据，同时寻找更具创造性的方式将当地特有的文化信息融入训练过程中。

---

## 8. Interfaze: A new model architecture built for high accuracy at scale

**原文标题**: Interfaze: A new model architecture built for high accuracy at scale

**原文链接**: [https://interfaze.ai/blog/interfaze-a-new-model-architecture-built-for-high-accuracy-at-scale](https://interfaze.ai/blog/interfaze-a-new-model-architecture-built-for-high-accuracy-at-scale)

生成摘要时出错

---

## 9. Bild AI (YC W25) 招聘创始产品工程师

**原文标题**: Bild AI (YC W25) Is Hiring Founding Product Engineers

**原文链接**: [https://bild.ai/jobs](https://bild.ai/jobs)

**Bild AI** 是一家入选 **Y Combinator 2025年冬季（W25）** 批次的初创公司，目前正在招聘 **创始产品工程师**。

作为创始团队的一员，这些工程师将在从零开始塑造公司的核心技术和产品路线图中发挥关键作用。在此阶段加入通常意味着拥有高度的自主权、巨大的股权潜力，并有机会在一家获风投支持的初创公司最早期阶段影响其文化和技术方向。

尽管具体的技术要求和职位描述发布在需启用 JavaScript 才能完整访问的平台上，但“创始”一词表明公司正在寻找能够构建并扩展新型 AI 驱动产品的全能型、高影响力开发人员。

---

## 10. Show HN: TikTok but for Scientific Papers

**原文标题**: Show HN: TikTok but for Scientific Papers

**原文链接**: [https://andreaturchet.github.io/website/index.html](https://andreaturchet.github.io/website/index.html)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 2 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 3 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 4 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 5 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 6 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 7 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 8 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 9 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 10 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 11 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 12 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 13 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 14 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 15 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 16 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 17 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 18 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 19 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 20 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 21 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 22 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 23 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 24 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 25 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 26 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 27 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 28 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 29 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 30 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 31 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 32 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 33 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 34 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 35 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 36 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 37 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 38 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 39 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 40 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 41 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 42 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 43 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 44 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 45 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 46 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 47 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 48 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 49 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 50 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 51 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 52 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 53 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 54 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 55 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 56 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 57 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 58 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 59 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 60 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 61 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 62 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 63 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 64 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 65 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 66 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 67 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 68 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 69 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 70 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 71 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 72 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 73 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 74 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 75 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 76 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 77 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 78 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 79 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 80 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 81 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 82 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 83 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 84 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 85 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 86 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 87 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 88 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 89 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 90 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 91 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 92 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 93 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 94 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 95 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 96 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 97 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 98 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 99 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 100 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 101 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 102 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 103 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 104 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 105 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 106 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 107 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 108 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 109 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 110 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 111 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 112 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 113 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 114 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 115 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 116 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 117 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 118 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 119 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 120 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 121 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 122 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 123 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 124 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 125 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 126 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 127 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 128 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 129 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 130 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 131 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 132 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 133 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 134 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 135 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 136 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 137 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 138 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 139 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 140 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 141 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 142 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 143 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 144 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 145 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 146 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 147 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 148 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 149 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 150 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 151 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 152 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 153 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 154 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 155 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 156 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 157 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 158 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 159 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 160 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 161 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 162 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 163 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 164 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 165 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 166 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 167 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 168 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 169 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 170 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 171 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 172 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 173 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 174 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 175 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 176 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 177 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 178 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 179 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 180 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 181 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 182 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 183 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 184 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 185 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 186 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 187 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 188 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 189 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 190 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 191 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 192 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 193 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 194 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 195 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 196 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 197 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 198 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 199 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 200 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 201 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 202 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 203 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 204 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 205 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 206 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 207 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 208 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 209 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 210 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 211 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 212 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 213 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 214 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 215 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 216 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 217 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 218 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 219 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 220 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 221 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 222 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 223 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 224 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 225 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 226 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 227 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 228 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 229 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 230 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 231 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 232 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 233 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 234 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 235 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 236 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 237 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 238 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 239 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 240 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 241 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 242 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 243 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 244 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 245 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 246 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 247 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 248 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 249 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 250 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 251 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 252 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 253 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 254 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 255 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 256 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 257 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 258 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 259 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 260 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 261 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 262 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 263 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 264 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 265 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 266 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 267 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 268 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 269 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 270 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 271 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 272 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 273 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 274 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 275 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 276 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 277 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 278 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 279 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 280 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 281 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 282 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 283 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 284 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 285 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 286 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 287 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 288 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 289 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 290 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 291 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 292 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 293 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 294 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 295 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 296 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 297 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 298 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 299 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 300 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 301 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 302 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 303 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 304 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 305 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 306 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 307 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 308 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 309 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 310 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 311 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 312 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 313 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 314 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 315 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 316 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 317 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 318 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 319 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 320 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 321 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 322 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 323 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 324 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 325 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 326 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 327 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 328 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 329 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 330 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 331 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 332 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 333 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 334 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 335 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 336 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 337 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 338 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 339 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 340 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 341 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 342 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 343 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 344 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 345 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 346 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 347 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 348 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 349 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 350 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 351 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 352 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 353 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 354 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 355 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 356 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 357 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 358 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 359 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 360 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 361 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 362 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 363 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 364 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 365 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 366 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 367 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 368 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 369 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 370 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 371 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 372 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 373 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 374 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 375 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 376 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 377 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 378 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 379 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 380 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 381 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 382 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 383 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 384 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 385 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 386 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 387 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 388 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 389 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 390 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 391 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 392 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 393 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 394 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 395 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 396 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 397 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 398 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 399 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 400 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 401 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 402 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 403 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 404 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 405 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 406 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 407 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 408 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 409 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 410 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 411 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 412 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 413 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 414 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 415 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 416 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 417 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
