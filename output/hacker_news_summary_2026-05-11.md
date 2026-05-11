# Hacker News 热门文章摘要 (2026-05-11)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Venom and Hot Peppers Offer a Key to Killing Resistant Bacteria

**原文标题**: Venom and Hot Peppers Offer a Key to Killing Resistant Bacteria

**原文链接**: [https://www.wired.com/story/mexican-science-transforms-scorpion-venom-and-habanero-chile-into-antibiotics-against-resistant-bacteria/](https://www.wired.com/story/mexican-science-transforms-scorpion-venom-and-habanero-chile-into-antibiotics-against-resistant-bacteria/)

生成摘要时出错

---

## 12. I'm going back to writing code by hand

**原文标题**: I'm going back to writing code by hand

**原文链接**: [https://blog.k10s.dev/im-going-back-to-writing-code-by-hand/](https://blog.k10s.dev/im-going-back-to-writing-code-by-hand/)

生成摘要时出错

---

## 13. Building a web server in aarch64 assembly to give my life (a lack of) meaning

**原文标题**: Building a web server in aarch64 assembly to give my life (a lack of) meaning

**原文链接**: [https://imtomt.github.io/ymawky/](https://imtomt.github.io/ymawky/)

生成摘要时出错

---

## 14. Holding Community Space

**原文标题**: Holding Community Space

**原文链接**: [https://supernuclear.substack.com/p/building-a-space-people-never-want](https://supernuclear.substack.com/p/building-a-space-people-never-want)

生成摘要时出错

---

## 15. Software engineering may no longer be a lifetime career

**原文标题**: Software engineering may no longer be a lifetime career

**原文链接**: [https://www.seangoedecke.com/software-engineering-may-no-longer-be-a-lifetime-career/](https://www.seangoedecke.com/software-engineering-may-no-longer-be-a-lifetime-career/)

生成摘要时出错

---

## 16. The Boston Library Where You Still Can Borrow a Giant Puppet

**原文标题**: The Boston Library Where You Still Can Borrow a Giant Puppet

**原文链接**: [https://binj.news/2026/05/06/the-boston-library-where-you-still-can-borrow-a-giant-puppet/](https://binj.news/2026/05/06/the-boston-library-where-you-still-can-borrow-a-giant-puppet/)

生成摘要时出错

---

## 17. Running local models on an M4 with 24GB memory

**原文标题**: Running local models on an M4 with 24GB memory

**原文链接**: [https://jola.dev/posts/running-local-models-on-m4](https://jola.dev/posts/running-local-models-on-m4)

生成摘要时出错

---

## 18. The greatest shot in television: James Burke had one chance to nail this scene (2024)

**原文标题**: The greatest shot in television: James Burke had one chance to nail this scene (2024)

**原文链接**: [https://www.openculture.com/2024/10/the-greatest-shot-in-television.html](https://www.openculture.com/2024/10/the-greatest-shot-in-television.html)

生成摘要时出错

---

## 19. Hardware Attestation as Monopoly Enabler

**原文标题**: Hardware Attestation as Monopoly Enabler

**原文链接**: [https://grapheneos.social/@GrapheneOS/116550899908879585](https://grapheneos.social/@GrapheneOS/116550899908879585)

生成摘要时出错

---

## 20. Guitar tuner that uses phone accelerometer

**原文标题**: Guitar tuner that uses phone accelerometer

**原文链接**: [https://tautme.github.io/phone-sensors/accel-tuner.html](https://tautme.github.io/phone-sensors/accel-tuner.html)

生成摘要时出错

---

## 21. An AI coding agent, used to write code, needs to reduce your maintenance costs

**原文标题**: An AI coding agent, used to write code, needs to reduce your maintenance costs

**原文链接**: [https://www.jamesshore.com/v2/blog/2026/you-need-ai-that-reduces-your-maintenance-costs](https://www.jamesshore.com/v2/blog/2026/you-need-ai-that-reduces-your-maintenance-costs)

生成摘要时出错

---

## 22. Obsidian plugin was abused to deploy a remote access trojan

**原文标题**: Obsidian plugin was abused to deploy a remote access trojan

**原文链接**: [https://cyber.netsecops.io/articles/obsidian-plugin-abused-in-campaign-to-deploy-phantom-pulse-rat/](https://cyber.netsecops.io/articles/obsidian-plugin-abused-in-campaign-to-deploy-phantom-pulse-rat/)

生成摘要时出错

---

## 23. Local AI needs to be the norm

**原文标题**: Local AI needs to be the norm

**原文链接**: [https://unix.foo/posts/local-ai-needs-to-be-norm/](https://unix.foo/posts/local-ai-needs-to-be-norm/)

生成摘要时出错

---

## 24. Students Boo Commencement Speaker After She Calls AI Next Industrial Revolution

**原文标题**: Students Boo Commencement Speaker After She Calls AI Next Industrial Revolution

**原文链接**: [https://www.404media.co/ucf-ai-commencement-speaker-booed/](https://www.404media.co/ucf-ai-commencement-speaker-booed/)

生成摘要时出错

---

## 25. Bliss (Photograph)

**原文标题**: Bliss (Photograph)

**原文链接**: [https://en.wikipedia.org/wiki/Bliss_(photograph)](https://en.wikipedia.org/wiki/Bliss_(photograph))

生成摘要时出错

---

## 26. Mythos Finds a Curl Vulnerability

**原文标题**: Mythos Finds a Curl Vulnerability

**原文链接**: [https://daniel.haxx.se/blog/2026/05/11/mythos-finds-a-curl-vulnerability/](https://daniel.haxx.se/blog/2026/05/11/mythos-finds-a-curl-vulnerability/)

生成摘要时出错

---

## 27. Should you leave red herrings about yourself online?

**原文标题**: Should you leave red herrings about yourself online?

**原文链接**: [https://blog.alcazarsec.com/posts/should-you-leave-red-herrings-about-yourself-online](https://blog.alcazarsec.com/posts/should-you-leave-red-herrings-about-yourself-online)

生成摘要时出错

---

## 28. A.I. note takers are making lawyers nervous

**原文标题**: A.I. note takers are making lawyers nervous

**原文链接**: [https://www.nytimes.com/2026/05/09/business/dealbook/ai-notetakers-legal-risk.html](https://www.nytimes.com/2026/05/09/business/dealbook/ai-notetakers-legal-risk.html)

生成摘要时出错

---

## 29. Guy Goma's Accidental BBC Interview Lives on After 20 Years

**原文标题**: Guy Goma's Accidental BBC Interview Lives on After 20 Years

**原文链接**: [https://www.nytimes.com/2026/05/06/business/media/bbc-guy-goma-interview.html](https://www.nytimes.com/2026/05/06/business/media/bbc-guy-goma-interview.html)

生成摘要时出错

---

## 30. First tunnel element of the Fehmarnbelt Tunnel immersed

**原文标题**: First tunnel element of the Fehmarnbelt Tunnel immersed

**原文链接**: [https://www.arup.com/en-us/news/first-fehmarnbelt-tunnel-element-lowered/](https://www.arup.com/en-us/news/first-fehmarnbelt-tunnel-element-lowered/)

生成摘要时出错

---

## 31. The Adventure Family Tree (2024)

**原文标题**: The Adventure Family Tree (2024)

**原文链接**: [https://mipmip.org/advfamily/advfamily.html](https://mipmip.org/advfamily/advfamily.html)

生成摘要时出错

---

## 32. Microsoft Israel chief leaves amid ethical controversy

**原文标题**: Microsoft Israel chief leaves amid ethical controversy

**原文链接**: [https://en.globes.co.il/en/article-microsoft-israel-chief-leaves-amid-ethical-controversy-1001542602](https://en.globes.co.il/en/article-microsoft-israel-chief-leaves-amid-ethical-controversy-1001542602)

生成摘要时出错

---

## 33. How Fast Does Claude, Acting as a User Space IP Stack, Respond to Pings?

**原文标题**: How Fast Does Claude, Acting as a User Space IP Stack, Respond to Pings?

**原文链接**: [https://dunkels.com/adam/claude-user-space-ip-stack-ping/](https://dunkels.com/adam/claude-user-space-ip-stack-ping/)

生成摘要时出错

---

## 34. Show HN: adamsreview – better multi-agent PR reviews for Claude Code

**原文标题**: Show HN: adamsreview – better multi-agent PR reviews for Claude Code

**原文链接**: [https://github.com/adamjgmiller/adamsreview](https://github.com/adamjgmiller/adamsreview)

生成摘要时出错

---

## 35. 7 lines of code, 3 minutes: Implement a programming language (2010)

**原文标题**: 7 lines of code, 3 minutes: Implement a programming language (2010)

**原文链接**: [https://matt.might.net/articles/implementing-a-programming-language/](https://matt.might.net/articles/implementing-a-programming-language/)

生成摘要时出错

---

## 36. What a Japanese cooking principle taught me about overcoming AI fatigue

**原文标题**: What a Japanese cooking principle taught me about overcoming AI fatigue

**原文链接**: [https://www.devas.life/what-a-japanese-cooking-principle-taught-me-about-overcoming-ai-fatigue/](https://www.devas.life/what-a-japanese-cooking-principle-taught-me-about-overcoming-ai-fatigue/)

生成摘要时出错

---

## 37. Scaffold a 1990s Geocities-themed static website

**原文标题**: Scaffold a 1990s Geocities-themed static website

**原文链接**: [https://pypi.org/project/create-geocities-app/](https://pypi.org/project/create-geocities-app/)

生成摘要时出错

---

## 38. dBase: 1979-2026

**原文标题**: dBase: 1979-2026

**原文链接**: [https://delphinightmares.substack.com/p/dbase-1979-2026](https://delphinightmares.substack.com/p/dbase-1979-2026)

生成摘要时出错

---

## 39. Incident Report: CVE-2024-YIKES

**原文标题**: Incident Report: CVE-2024-YIKES

**原文链接**: [https://nesbitt.io/2026/02/03/incident-report-cve-2024-yikes.html](https://nesbitt.io/2026/02/03/incident-report-cve-2024-yikes.html)

生成摘要时出错

---

## 40. ICE to Develop Own Smart Glasses to 'Supplement' Its Facial Recognition App

**原文标题**: ICE to Develop Own Smart Glasses to 'Supplement' Its Facial Recognition App

**原文链接**: [https://www.404media.co/ice-plans-to-develop-own-smart-glasses-to-supplement-its-facial-recognition-app/](https://www.404media.co/ice-plans-to-develop-own-smart-glasses-to-supplement-its-facial-recognition-app/)

生成摘要时出错

---

## 41. Phel v0.36.0 – Lisp on PHP, now with numeric tower and first-class Vars

**原文标题**: Phel v0.36.0 – Lisp on PHP, now with numeric tower and first-class Vars

**原文链接**: [https://github.com/phel-lang/phel-lang/releases/tag/v0.36.0](https://github.com/phel-lang/phel-lang/releases/tag/v0.36.0)

生成摘要时出错

---

## 42. Traces Of Humanity

**原文标题**: Traces Of Humanity

**原文链接**: [https://tracesofhumanity.org/hello-world/](https://tracesofhumanity.org/hello-world/)

生成摘要时出错

---

## 43. Stop MitM on the first SSH connection, on any VPS or cloud provider

**原文标题**: Stop MitM on the first SSH connection, on any VPS or cloud provider

**原文链接**: [https://www.joachimschipper.nl/Stop%20MITM%20on%20the%20first%20SSH%20connection,%20on%20any%20VPS%20or%20cloud%20provider.html](https://www.joachimschipper.nl/Stop%20MITM%20on%20the%20first%20SSH%20connection,%20on%20any%20VPS%20or%20cloud%20provider.html)

生成摘要时出错

---

## 44. Driver accused of DUI tracks missing laptop to Illinois State trooper's house

**原文标题**: Driver accused of DUI tracks missing laptop to Illinois State trooper's house

**原文链接**: [https://abc7chicago.com/post/top-cop-driver-accused-dui-tracks-missing-laptop-illinois-state-police-trooper-kevin-bradleys-house/19060850/](https://abc7chicago.com/post/top-cop-driver-accused-dui-tracks-missing-laptop-illinois-state-police-trooper-kevin-bradleys-house/19060850/)

生成摘要时出错

---

## 45. Eight More '8-Bit Era' Microprocessors

**原文标题**: Eight More '8-Bit Era' Microprocessors

**原文链接**: [https://thechipletter.substack.com/p/eight-more-8-bit-era-microprocessors](https://thechipletter.substack.com/p/eight-more-8-bit-era-microprocessors)

生成摘要时出错

---

## 46. The people preserving the scientific practice of bird banding

**原文标题**: The people preserving the scientific practice of bird banding

**原文链接**: [https://thenarwhal.ca/bird-banding-ontario/](https://thenarwhal.ca/bird-banding-ontario/)

生成摘要时出错

---

## 47. AI-powered hacking has exploded into industrial-scale threat, Google says

**原文标题**: AI-powered hacking has exploded into industrial-scale threat, Google says

**原文链接**: [https://www.theguardian.com/technology/2026/may/11/ai-powered-hacking-industrial-scale-threat-three-months-google](https://www.theguardian.com/technology/2026/may/11/ai-powered-hacking-industrial-scale-threat-three-months-google)

生成摘要时出错

---

## 48. The locals don't know

**原文标题**: The locals don't know

**原文链接**: [https://www.quarter--mile.com/The-Locals-Dont-Know](https://www.quarter--mile.com/The-Locals-Dont-Know)

生成摘要时出错

---

## 49. A recent experience with ChatGPT 5.5 Pro

**原文标题**: A recent experience with ChatGPT 5.5 Pro

**原文链接**: [https://gowers.wordpress.com/2026/05/08/a-recent-experience-with-chatgpt-5-5-pro/](https://gowers.wordpress.com/2026/05/08/a-recent-experience-with-chatgpt-5-5-pro/)

生成摘要时出错

---

## 50. Building a Memory Allocator from Scratch in C

**原文标题**: Building a Memory Allocator from Scratch in C

**原文链接**: [https://0xkiire.com/memory-allocators/](https://0xkiire.com/memory-allocators/)

生成摘要时出错

---

## 51. European Money Pours into Palantir

**原文标题**: European Money Pours into Palantir

**原文链接**: [https://english.elpais.com/economy-and-business/branded/2026-04-11/european-money-pours-into-palantir-over-100-asset-managers-and-banks-boost-their-investments-in-the-controversial-tech-company.html](https://english.elpais.com/economy-and-business/branded/2026-04-11/european-money-pours-into-palantir-over-100-asset-managers-and-banks-boost-their-investments-in-the-controversial-tech-company.html)

生成摘要时出错

---

## 52. The Inference Shift

**原文标题**: The Inference Shift

**原文链接**: [https://stratechery.com/2026/the-inference-shift/](https://stratechery.com/2026/the-inference-shift/)

生成摘要时出错

---

## 53. Maryland citizens hit with $2B power grid upgrade for out-of-state AI

**原文标题**: Maryland citizens hit with $2B power grid upgrade for out-of-state AI

**原文链接**: [https://www.tomshardware.com/tech-industry/artificial-intelligence/maryland-citizens-slapped-with-usd2-billion-grid-upgrade-bill-for-out-of-state-ai-data-centers-state-complains-to-federal-energy-regulators-says-additional-cost-breaks-ratepayer-protection-pledge-promises](https://www.tomshardware.com/tech-industry/artificial-intelligence/maryland-citizens-slapped-with-usd2-billion-grid-upgrade-bill-for-out-of-state-ai-data-centers-state-complains-to-federal-energy-regulators-says-additional-cost-breaks-ratepayer-protection-pledge-promises)

生成摘要时出错

---

## 54. Out with the JavaScript, in with the HTML

**原文标题**: Out with the JavaScript, in with the HTML

**原文链接**: [https://blog.jim-nielsen.com/2026/out-with-js-in-with-html/](https://blog.jim-nielsen.com/2026/out-with-js-in-with-html/)

生成摘要时出错

---

## 55. What's a mathematician to do? (2010)

**原文标题**: What's a mathematician to do? (2010)

**原文链接**: [https://mathoverflow.net/questions/43690/whats-a-mathematician-to-do](https://mathoverflow.net/questions/43690/whats-a-mathematician-to-do)

生成摘要时出错

---

## 56. Show HN: An index of indie web/blog indexes

**原文标题**: Show HN: An index of indie web/blog indexes

**原文链接**: [https://theindex.fyi](https://theindex.fyi)

生成摘要时出错

---

## 57. Seeing Birdsong

**原文标题**: Seeing Birdsong

**原文链接**: [https://www.lucioarese.net/seeing-birdsong/](https://www.lucioarese.net/seeing-birdsong/)

生成摘要时出错

---

## 58. Ice Cream Blending (1965) [pdf]

**原文标题**: Ice Cream Blending (1965) [pdf]

**原文链接**: [https://bitsavers.org/pdf/ibm/generalInfo/E20-0156-0_Linear_Programming_-_Ice_Cream_Blending.pdf](https://bitsavers.org/pdf/ibm/generalInfo/E20-0156-0_Linear_Programming_-_Ice_Cream_Blending.pdf)

生成摘要时出错

---

## 59. Lakebase architecture delivers faster Postgres writes

**原文标题**: Lakebase architecture delivers faster Postgres writes

**原文链接**: [https://www.databricks.com/blog/how-lakebase-architecture-delivers-5x-faster-postgres-writes](https://www.databricks.com/blog/how-lakebase-architecture-delivers-5x-faster-postgres-writes)

生成摘要时出错

---

## 60. Hosting an Open Alternative to Google Docs for Digital Sovereignty

**原文标题**: Hosting an Open Alternative to Google Docs for Digital Sovereignty

**原文链接**: [https://www.heltweg.org/posts/hosting-an-open-alternative-to-google-docs-for-digital-sovereignty/](https://www.heltweg.org/posts/hosting-an-open-alternative-to-google-docs-for-digital-sovereignty/)

生成摘要时出错

---

## 61. Forget the AI job apocalypse. AIs real threat is worker control and surveillance

**原文标题**: Forget the AI job apocalypse. AIs real threat is worker control and surveillance

**原文链接**: [https://www.theguardian.com/technology/2026/may/11/ai-worker-control-surveillance](https://www.theguardian.com/technology/2026/may/11/ai-worker-control-surveillance)

生成摘要时出错

---

## 62. Louis Rossmann offers to pay legal fees for a threatened OrcaSlicer developer

**原文标题**: Louis Rossmann offers to pay legal fees for a threatened OrcaSlicer developer

**原文链接**: [https://www.tomshardware.com/3d-printing/louis-rossmann-tells-3d-printer-maker-bambu-lab-to-go-bleep-yourself-over-its-lawsuit-against-enthusiast-right-to-repair-advocate-offers-to-pay-the-legal-fees-for-a-threatened-orcaslicer-developer](https://www.tomshardware.com/3d-printing/louis-rossmann-tells-3d-printer-maker-bambu-lab-to-go-bleep-yourself-over-its-lawsuit-against-enthusiast-right-to-repair-advocate-offers-to-pay-the-legal-fees-for-a-threatened-orcaslicer-developer)

生成摘要时出错

---

## 63. What's Wrong with AI?

**原文标题**: What's Wrong with AI?

**原文链接**: [https://kurtis.weblog.lol/2026/05/whats-wrong-with-ai](https://kurtis.weblog.lol/2026/05/whats-wrong-with-ai)

生成摘要时出错

---

## 64. Space Cadet Pinball on Linux

**原文标题**: Space Cadet Pinball on Linux

**原文链接**: [https://brennan.io/2026/05/09/pinball-and-escrow/](https://brennan.io/2026/05/09/pinball-and-escrow/)

生成摘要时出错

---

## 65. PS3 Emulator Devs Politely Ask That People Stop Flooding It with AI PRs

**原文标题**: PS3 Emulator Devs Politely Ask That People Stop Flooding It with AI PRs

**原文链接**: [https://kotaku.com/playstation-3-emulator-devs-politely-ask-that-people-stop-flooding-it-with-ai-code-pull-requests-2000694656](https://kotaku.com/playstation-3-emulator-devs-politely-ask-that-people-stop-flooding-it-with-ai-code-pull-requests-2000694656)

生成摘要时出错

---

## 66. Bun's experimental Rust rewrite hits 99.8% test compatibility on Linux x64 glibc

**原文标题**: Bun's experimental Rust rewrite hits 99.8% test compatibility on Linux x64 glibc

**原文链接**: [https://twitter.com/jarredsumner/status/2053047748191232310](https://twitter.com/jarredsumner/status/2053047748191232310)

生成摘要时出错

---

## 67. Gode Cookery – Authentic Medieval Recipes

**原文标题**: Gode Cookery – Authentic Medieval Recipes

**原文链接**: [http://www.godecookery.com/godeboke/godeboke.htm](http://www.godecookery.com/godeboke/godeboke.htm)

生成摘要时出错

---

## 68. Scientists Prolong Life of Mice with Invisible Energy Fields, New Study Shows

**原文标题**: Scientists Prolong Life of Mice with Invisible Energy Fields, New Study Shows

**原文链接**: [https://www.nmn.com/news/scientists-prolong-the-life-of-mice-with-invisible-energy-fields-new-study-shows](https://www.nmn.com/news/scientists-prolong-the-life-of-mice-with-invisible-energy-fields-new-study-shows)

生成摘要时出错

---

## 69. I keep tripping over "true, false, true"

**原文标题**: I keep tripping over "true, false, true"

**原文链接**: [https://allthingssmitty.com/2026/05/11/i-keep-tripping-over-true-false-true/](https://allthingssmitty.com/2026/05/11/i-keep-tripping-over-true-false-true/)

生成摘要时出错

---

## 70. Gemini API File Search is now multimodal

**原文标题**: Gemini API File Search is now multimodal

**原文链接**: [https://blog.google/innovation-and-ai/technology/developers-tools/expanded-gemini-api-file-search-multimodal-rag/](https://blog.google/innovation-and-ai/technology/developers-tools/expanded-gemini-api-file-search-multimodal-rag/)

生成摘要时出错

---

## 71. Google broke reCAPTCHA for de-googled Android users

**原文标题**: Google broke reCAPTCHA for de-googled Android users

**原文链接**: [https://reclaimthenet.org/google-broke-recaptcha-for-de-googled-android-users](https://reclaimthenet.org/google-broke-recaptcha-for-de-googled-android-users)

生成摘要时出错

---

## 72. Half-assing it with everything you've got

**原文标题**: Half-assing it with everything you've got

**原文链接**: [https://mindingourway.com/half-assing-it-with-everything-youve-got/](https://mindingourway.com/half-assing-it-with-everything-youve-got/)

生成摘要时出错

---

## 73. I returned to AWS and was reminded why I left

**原文标题**: I returned to AWS and was reminded why I left

**原文链接**: [http://fourlightyears.blogspot.com/2026/05/i-returned-to-aws-and-was-reminded-hard.html](http://fourlightyears.blogspot.com/2026/05/i-returned-to-aws-and-was-reminded-hard.html)

生成摘要时出错

---

## 74. The Struggle Is Gone

**原文标题**: The Struggle Is Gone

**原文链接**: [https://dogdogfish.com/blog/2026/05/10/the-struggle-is-gone/](https://dogdogfish.com/blog/2026/05/10/the-struggle-is-gone/)

生成摘要时出错

---

## 75. The Interstitium, the Human Body's Hidden Pathways

**原文标题**: The Interstitium, the Human Body's Hidden Pathways

**原文链接**: [https://www.nytimes.com/interactive/2026/05/11/magazine/interstitium-anatomy-acupuncture-medicine.html](https://www.nytimes.com/interactive/2026/05/11/magazine/interstitium-anatomy-acupuncture-medicine.html)

生成摘要时出错

---

## 76. Show HN: I made a Clojure-like language in Go, boots in 7ms

**原文标题**: Show HN: I made a Clojure-like language in Go, boots in 7ms

**原文链接**: [https://github.com/nooga/let-go](https://github.com/nooga/let-go)

生成摘要时出错

---

## 77. Rotten Dot Com

**原文标题**: Rotten Dot Com

**原文链接**: [https://www.theparisreview.org/blog/2026/05/06/rotten-dot-com/](https://www.theparisreview.org/blog/2026/05/06/rotten-dot-com/)

生成摘要时出错

---

## 78. Why we lose our friends as we age (2023)

**原文标题**: Why we lose our friends as we age (2023)

**原文链接**: [https://www.theatlantic.com/newsletters/archive/2023/02/friendship-aging/673026/](https://www.theatlantic.com/newsletters/archive/2023/02/friendship-aging/673026/)

生成摘要时出错

---

## 79. Why modern parents feel more sleep deprived than our ancestors did

**原文标题**: Why modern parents feel more sleep deprived than our ancestors did

**原文链接**: [https://www.bbc.com/future/article/20260508-parents-in-ancient-times-felt-less-sleep-deprived-what-our-ancestors-did-differently-on-baby-sleep](https://www.bbc.com/future/article/20260508-parents-in-ancient-times-felt-less-sleep-deprived-what-our-ancestors-did-differently-on-baby-sleep)

生成摘要时出错

---

## 80. Internet Archive Switzerland

**原文标题**: Internet Archive Switzerland

**原文链接**: [https://blog.archive.org/2026/05/06/internet-archive-switzerland-expanding-a-global-mission-to-preserve-knowledge/](https://blog.archive.org/2026/05/06/internet-archive-switzerland-expanding-a-global-mission-to-preserve-knowledge/)

生成摘要时出错

---

## 81. Shunting-Yard Animation

**原文标题**: Shunting-Yard Animation

**原文链接**: [https://somethingorotherwhatever.com/shunting-yard-animation/](https://somethingorotherwhatever.com/shunting-yard-animation/)

生成摘要时出错

---

## 82. I'm writing a history of Visual Basic, Chapter 1 is up

**原文标题**: I'm writing a history of Visual Basic, Chapter 1 is up

**原文链接**: [https://evilgeniuslabs.ca/blog/visual-basic-history-chapter-1-launch](https://evilgeniuslabs.ca/blog/visual-basic-history-chapter-1-launch)

生成摘要时出错

---

## 83. Idempotency is easy until the second request is different

**原文标题**: Idempotency is easy until the second request is different

**原文链接**: [https://blog.dochia.dev/blog/idempotency/](https://blog.dochia.dev/blog/idempotency/)

生成摘要时出错

---

## 84. Singapore introduces caning for boys who bully others at school

**原文标题**: Singapore introduces caning for boys who bully others at school

**原文链接**: [https://www.theguardian.com/world/2026/may/06/singapore-caning-school-bullies](https://www.theguardian.com/world/2026/may/06/singapore-caning-school-bullies)

生成摘要时出错

---

## 85. American Agriculture Is Broken

**原文标题**: American Agriculture Is Broken

**原文链接**: [https://www.ft.com/content/a4e41434-b047-485f-a5e1-0e88277f8aae](https://www.ft.com/content/a4e41434-b047-485f-a5e1-0e88277f8aae)

生成摘要时出错

---

## 86. Shelf Source: Tom MacWright

**原文标题**: Shelf Source: Tom MacWright

**原文链接**: [https://roadlessread.com/views/ss-macwright](https://roadlessread.com/views/ss-macwright)

生成摘要时出错

---

## 87. The One Dollar Counterfeiter

**原文标题**: The One Dollar Counterfeiter

**原文链接**: [https://www.amusingplanet.com/2026/05/emerich-juettner-one-dollar.html](https://www.amusingplanet.com/2026/05/emerich-juettner-one-dollar.html)

生成摘要时出错

---

## 88. Show HN: Rust but Lisp

**原文标题**: Show HN: Rust but Lisp

**原文链接**: [https://github.com/ThatXliner/rust-but-lisp](https://github.com/ThatXliner/rust-but-lisp)

生成摘要时出错

---

## 89. Nuke All Routers

**原文标题**: Nuke All Routers

**原文链接**: [https://github.com/maxbrito500/esp32-c5-deauth](https://github.com/maxbrito500/esp32-c5-deauth)

生成摘要时出错

---

## 90. Show HN: Countries where you can leave your MacBook at a random coffee shop

**原文标题**: Show HN: Countries where you can leave your MacBook at a random coffee shop

**原文链接**: [https://vouchatlas.com](https://vouchatlas.com)

生成摘要时出错

---

## 91. CPanel's Black Week: 3 New Vulnerabilities Patched After Attack on 44k Servers

**原文标题**: CPanel's Black Week: 3 New Vulnerabilities Patched After Attack on 44k Servers

**原文链接**: [https://www.copahost.com/blog/cpanels-black-week-three-new-vulnerabilities-patched-after-ransomware-attack-on-44000-servers/](https://www.copahost.com/blog/cpanels-black-week-three-new-vulnerabilities-patched-after-ransomware-attack-on-44000-servers/)

生成摘要时出错

---

## 92. I’ve banned query strings

**原文标题**: I’ve banned query strings

**原文链接**: [https://chrismorgan.info/no-query-strings](https://chrismorgan.info/no-query-strings)

生成摘要时出错

---

## 93. Spain has become one of Europe’s cheapest power markets

**原文标题**: Spain has become one of Europe’s cheapest power markets

**原文链接**: [https://janrosenow.substack.com/p/spain-just-became-one-of-europes](https://janrosenow.substack.com/p/spain-just-became-one-of-europes)

生成摘要时出错

---

## 94. Prosecutors Investigating Drugs-for-Votes Scheme Were Told Not to Pursue Charges

**原文标题**: Prosecutors Investigating Drugs-for-Votes Scheme Were Told Not to Pursue Charges

**原文链接**: [https://www.propublica.org/article/trump-doj-puerto-rico-election-fraud-prison-drugs-votes](https://www.propublica.org/article/trump-doj-puerto-rico-election-fraud-prison-drugs-votes)

生成摘要时出错

---

## 95. BLAS, Lapack and OpenMP

**原文标题**: BLAS, Lapack and OpenMP

**原文链接**: [https://pypackaging-native.github.io/key-issues/native-dependencies/blas_openmp/](https://pypackaging-native.github.io/key-issues/native-dependencies/blas_openmp/)

生成摘要时出错

---

## 96. Show HN: Building a web server in assembly to give my life (a lack of) meaning

**原文标题**: Show HN: Building a web server in assembly to give my life (a lack of) meaning

**原文链接**: [https://github.com/imtomt/ymawky](https://github.com/imtomt/ymawky)

生成摘要时出错

---

## 97. Officially canceling our Anthropic plan, it's [too expensive]

**原文标题**: Officially canceling our Anthropic plan, it's [too expensive]

**原文链接**: [https://twitter.com/morganlinton/status/2053165575824887938](https://twitter.com/morganlinton/status/2053165575824887938)

生成摘要时出错

---

## 98. Task Paralysis and AI

**原文标题**: Task Paralysis and AI

**原文链接**: [https://g5t.de/articles/20260510-task-paralysis-and-ai/index.html](https://g5t.de/articles/20260510-task-paralysis-and-ai/index.html)

生成摘要时出错

---

## 99. Making your own programming language is easier than you think (but also harder)

**原文标题**: Making your own programming language is easier than you think (but also harder)

**原文链接**: [https://lisyarus.github.io/blog/posts/making-your-own-programming-language.html](https://lisyarus.github.io/blog/posts/making-your-own-programming-language.html)

生成摘要时出错

---

## 100. Walking slower? Your ears, not your knees, might be the problem

**原文标题**: Walking slower? Your ears, not your knees, might be the problem

**原文链接**: [https://www.wsj.com/health/wellness/hearing-loss-walking-speed-iphone-study-c53c482a](https://www.wsj.com/health/wellness/hearing-loss-walking-speed-iphone-study-c53c482a)

生成摘要时出错

---

