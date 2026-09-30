# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-09-30.md)

*最后自动更新时间: 2026-09-30 21:43:07*
## 1. 双子座 4 氩

**原文标题**: Gemini 4 Argon

**原文链接**: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)

Google DeepMind has announced **Gemini 4 Argon**, a new frontier AI model engineered for deep reasoning and complex, long-horizon professional workflows. Released on September 30, 2026, the model excels in software engineering, enterprise knowledge work (legal and finance), and cybersecurity defense.

**Key Technical Advancements**
The model features an industry-leading **1-million-token output limit** (up from 64K), allowing it to generate massive, multi-step solutions in a single trajectory. Internally, Google has already utilized Argon to optimize quantum algorithms, save over 300 TiB of data center memory, and migrate hundreds of thousands of lines of C++ code to memory-safe Rust. 

**Performance and Benchmarks**
Argon sets new standards across several industry benchmarks:
*   **Coding:** 77.9% on DeepSWE v1.1.
*   **Economic Impact:** Leads the Vals Index for finance, legal, and tax work.
*   **Visual/Video:** 91.7% on LVBench for long video understanding.
*   **Cybersecurity:** Ties for first on CWE-bench v1 for remediating security vulnerabilities.

**Cybersecurity and Safety**
Through the **Fairwind Program**, Argon is being rolled out to trusted defenders without certain cyber guardrails to enable autonomous vulnerability patching. To ensure safety for the general public, Google is employing a phased release, working with the U.S. government on pre-release access, and implementing advanced monitoring for model misalignment and prompt injections.

**Pricing and Availability**
Argon will launch at an introductory price of **$2 per million input tokens** and **$10 per million output tokens**. While currently limited to trusted testers and cyber defenders, it will soon expand to developers, enterprise customers, and Google AI Ultra subscribers.

---

## 2. Surprisingly Complex Waves Reveal the Brain's Inner Workings

**原文标题**: Surprisingly Complex Waves Reveal the Brain's Inner Workings

**原文链接**: [https://www.quantamagazine.org/surprisingly-complex-waves-reveal-the-brains-inner-workings-20260930/](https://www.quantamagazine.org/surprisingly-complex-waves-reveal-the-brains-inner-workings-20260930/)

生成摘要时出错

---

## 3. EDG C++ front-end goes public

**原文标题**: EDG C++ front-end goes public

**原文链接**: [https://edgcpp.org/#transition](https://edgcpp.org/#transition)

生成摘要时出错

---

## 4. Launch HN: Magnitude (YC S25) – Self-optimizing inference engine for agents

**原文标题**: Launch HN: Magnitude (YC S25) – Self-optimizing inference engine for agents

**原文链接**: [https://github.com/magnitudedev/magnitude](https://github.com/magnitudedev/magnitude)

生成摘要时出错

---

## 5. 边缘函数提速 5 倍：从 V8 Isolate 迁移至 Firecracker MicroVMs

**原文标题**: 5x faster Edge Functions: V8 isolates to Firecracker MicroVMs

**原文链接**: [https://www.netlify.com/blog/edge-functions-firecracker-microvms/](https://www.netlify.com/blog/edge-functions-firecracker-microvms/)

Netlify 重构了其边缘函数（Edge Functions）基础设施，从托管的 V8 isolate 转向运行在自有边缘网络上的 Firecracker MicroVM。这一转变带来了 5 倍的性能提升，中值延迟从 25–40ms 降至仅 5–6ms，同时保持了 99.998% 的可用性。

**关键技术改进：**
*   **MicroVM 架构：** 通过与 Unikraft 合作，Netlify 现在采用可在 1 毫秒内启动的 Firecracker MicroVM。利用快照和内存映射技术，函数在空闲时可“缩减至零”，并在收到请求时即时恢复，仅通过 EROFS 镜像读取函数包的必要部分。
*   **增强的隔离性：** 与 V8 isolate 不同，MicroVM 为每次部署提供专用的 Linux 环境。这能防止受损的函数影响其他客户或底层平台，显著提升了安全性。
*   **优化路由：** 边缘节点使用“汇合哈希（rendezvous hashing）”将请求路由到特定的计算节点。这使函数能保持“热启动”并缓存在磁盘上，同时允许系统在流量激增时灵活调整粘性，以防止出现热点。
*   **开发者体验：** 此次过渡对用户是无缝的；现有的代码、npm 包和 Node 内置模块无需修改即可直接运行。

**未来展望：**
通过将计算能力整合进自有网络，Netlify 正在消除以往的限制。未来的优势包括支持完整的 npm 包（包括原生二进制文件）、更高的 CPU 和内存限制，以及对网络路径更精准的控制。这一新架构为 Netlify 持续提升复杂边缘计算任务的性能上限奠定了基础。

---

## 6. Halfspace：基于距离场的实验性实体建模 IDE

**原文标题**: Halfspace experimental IDE for solid modeling with distance fields

**原文链接**: [https://www.mattkeeter.com/projects/halfspace/](https://www.mattkeeter.com/projects/halfspace/)

**Halfspace** 是一款基于 **Fidget** 几何内核构建的实验性集成开发环境 (IDE)，专用于利用距离场进行实体建模。该工具由一位具有 CAD/CAM 背景的开发者设计，专注于创建具有明确内外边界的“实体”模型，适用于物理制造和 3D 打印。

该项目旨在弥合底层隐式表面与高层抽象之间的鸿沟。与传统的构造实体几何 (CSG) 工具不同，Halfspace 将底层的距离场置于核心位置。这种透明度允许用户诊断并修复诸如“跳跃”不连续性和非均匀梯度等问题，这些问题通常会导致着色效果差和网格质量低。

**主要特性与技术规格包括：**
*   **跨平台性能：** Halfspace 使用 **Rust** 构建，兼顾原生和 Web 平台。它利用 **WebGPU (wgpu)** 进行 GPU 加速的光栅化和着色，确保即使在浏览器中通过 WebAssembly 运行也能获得实时性能。
*   **混合工作流：** 用户可以结合使用标准基元库和手写脚本 (**Rhai**) 来逐步构建模型。
*   **Fidget 内核集成：** 该 IDE 作为 Fidget 内核的试验场，推动了其 GPU 渲染和 API 设计的改进。
*   **输出：** 模型可导出为高分辨率图像或三角网格。

Halfspace 基于 **MPLv2 许可证**开源，目前定位为“展示型应用”和实验性工具。虽然作者提醒不要将其用于关键任务，但它代表了一种将隐式表面建模变得对个人化制造更加直观且高效的深入探索。

---

## 7. A brief history of the Bloomberg terminal

**原文标题**: A brief history of the Bloomberg terminal

**原文链接**: [https://spectrum.ieee.org/bloomberg-terminal](https://spectrum.ieee.org/bloomberg-terminal)

生成摘要时出错

---

## 8. 你说过不使用 MCP。

**原文标题**: You said no MCP

**原文链接**: [https://earendil.com/posts/you-said-no-mcp/](https://earendil.com/posts/you-said-no-mcp/)

Earendil Engineering 宣布“Pi”现已原生支持**模型上下文协议 (MCP)**，这标志着该公司此前立场的重大转变。这一转变是由 MCP 的演进驱动的，同时也源于公司意识到 MCP 的要求与 Pi 对健壮解释器沙箱的需求高度契合。

此次更新的核心要点包括：

*   **集成优于扩展**：MCP 未被作为可选扩展，而是直接集成到核心中以支持“代码模式 (Codemode)”。这使得 Earendil 能够推动 MCP 标准向结构化数据和智能工具发现方向发展，而非仅停留在简单的文本响应。
*   **代码模式 (Codemode)**：这是一个由 WASM 驱动的新型 JavaScript 沙箱，运行在智能体循环中受信任的“驾驭端 (harness)”。它允许 AI 高效地编排、协调和组合多个工具调用。由于它在驾驭端运行，其状态保存在会话记录中，而非文件系统中。
*   **增强的组合能力**：Codemode 解决了 MCP 长期以来在“组合性”方面的难题。智能体现可以使用 JavaScript 将不同工具连接在一起——例如将 Linear MCP 服务器与“Jev”（一种类型安全分类器）相结合——以执行复杂任务（如对数百个 Issue 进行情感分析），且不会耗尽上下文窗口。
*   **现代大语言模型支持**：通过为工具可用性提供更完善的元数据，此次更新让 Pi 为更先进的模型能力（如延迟工具加载和推理层级的变化）做好了准备。

最终，Earendil Engineering 旨在将 MCP 从一个简单的工具堆砌机制转型为类似于 OpenAPI 的功能性系统，使智能体能够在安全的环境中以“类 bash”的高效方式操作结构化数据。

---

## 9. Gitea 28.0

**原文标题**: Gitea 28.0

**原文链接**: [https://blog.gitea.com/release-of-28.0.0/](https://blog.gitea.com/release-of-28.0.0/)

2026年8月29日，用户 **bircni** 宣布发布 **Gitea 1.27.3**。尽管公告标题提到了“Gitea 28.0”，但核心内容明确指出该更新版本为 1.27.3。所提供的文本仅作为发布的简要通知，未详细列出具体的功能更新或错误修复。

---

## 10. I could've accessed 17T Microsoft records

**原文标题**: I could've accessed 17T Microsoft records

**原文链接**: [https://blog.faav.net/how-i-couldve-accessed-17-trillion-microsoft-records](https://blog.faav.net/how-i-couldve-accessed-17-trillion-microsoft-records)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 2 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 3 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 4 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 5 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 6 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 7 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 8 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 9 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 10 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 11 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 12 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 13 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 14 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 15 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 16 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 17 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 18 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 19 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 20 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 21 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 22 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 23 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 24 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 25 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 26 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 27 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 28 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 29 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 30 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 31 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 32 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 33 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 34 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 35 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 36 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 37 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 38 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 39 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 40 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 41 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 42 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 43 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 44 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 45 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 46 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 47 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 48 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 49 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 50 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 51 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 52 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 53 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 54 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 55 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 56 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 57 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 58 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 59 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 60 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 61 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 62 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 63 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 64 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 65 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 66 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 67 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 68 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 69 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 70 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 71 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 72 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 73 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 74 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 75 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 76 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 77 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 78 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 79 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 80 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 81 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 82 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 83 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 84 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 85 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 86 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 87 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 88 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 89 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 90 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 91 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 92 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 93 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 94 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 95 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 96 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 97 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 98 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 99 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 100 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 101 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 102 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 103 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 104 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 105 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 106 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 107 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 108 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 109 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 110 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 111 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 112 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 113 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 114 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 115 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 116 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 117 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 118 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 119 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 120 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 121 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 122 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 123 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 124 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 125 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 126 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 127 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 128 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 129 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 130 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 131 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 132 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 133 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 134 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 135 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 136 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 137 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 138 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 139 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 140 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 141 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 142 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 143 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 144 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 145 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 146 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 147 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 148 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 149 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 150 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 151 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 152 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 153 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 154 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 155 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 156 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 157 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 158 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 159 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 160 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 161 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 162 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 163 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 164 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 165 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 166 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 167 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 168 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 169 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 170 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 171 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 172 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 173 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 174 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 175 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 176 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 177 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 178 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 179 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 180 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 181 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 182 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 183 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 184 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 185 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 186 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 187 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 188 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 189 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 190 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 191 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 192 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 193 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 194 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 195 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 196 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 197 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 198 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 199 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 200 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 201 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 202 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 203 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 204 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 205 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 206 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 207 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 208 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 209 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 210 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 211 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 212 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 213 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 214 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 215 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 216 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 217 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 218 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 219 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 220 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 221 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 222 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 223 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 224 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 225 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 226 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 227 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 228 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 229 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 230 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 231 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 232 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 233 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 234 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 235 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 236 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 237 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 238 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 239 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 240 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 241 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 242 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 243 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 244 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 245 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 246 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 247 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 248 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 249 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 250 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 251 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 252 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 253 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 254 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 255 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 256 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 257 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 258 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 259 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 260 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 261 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 262 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 263 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 264 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 265 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 266 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 267 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 268 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 269 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 270 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 271 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 272 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 273 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 274 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 275 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 276 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 277 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 278 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 279 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 280 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 281 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 282 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 283 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 284 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 285 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 286 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 287 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 288 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 289 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 290 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 291 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 292 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 293 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 294 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 295 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 296 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 297 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 298 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 299 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 300 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 301 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 302 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 303 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 304 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 305 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 306 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 307 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 308 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 309 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 310 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 311 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 312 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 313 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 314 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 315 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 316 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 317 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 318 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 319 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 320 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 321 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 322 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 323 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 324 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 325 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 326 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 327 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 328 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 329 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 330 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 331 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 332 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 333 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 334 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 335 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 336 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 337 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 338 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 339 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 340 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 341 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 342 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 343 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 344 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 345 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 346 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 347 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 348 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 349 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 350 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 351 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 352 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 353 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 354 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 355 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 356 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 357 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 358 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 359 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 360 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 361 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 362 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 363 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 364 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 365 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 366 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 367 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 368 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 369 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 370 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 371 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 372 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 373 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 374 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 375 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 376 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 377 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 378 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 379 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 380 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 381 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 382 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 383 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 384 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 385 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 386 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 387 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 388 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 389 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 390 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 391 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 392 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 393 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 394 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 395 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 396 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 397 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 398 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 399 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 400 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 401 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 402 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 403 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 404 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 405 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 406 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 407 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 408 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 409 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 410 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 411 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 412 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 413 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 414 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 415 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 416 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 417 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 418 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 419 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 420 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 421 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 422 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 423 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 424 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 425 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 426 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 427 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 428 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 429 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 430 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 431 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 432 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 433 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 434 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 435 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 436 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 437 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 438 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 439 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 440 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 441 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 442 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 443 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 444 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 445 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 446 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 447 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 448 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 449 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 450 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 451 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 452 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 453 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 454 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 455 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 456 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 457 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 458 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 459 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 460 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 461 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 462 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 463 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 464 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 465 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 466 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 467 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 468 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 469 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 470 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 471 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 472 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 473 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 474 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 475 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 476 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 477 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 478 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 479 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 480 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 481 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 482 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 483 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 484 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 485 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 486 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 487 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 488 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 489 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 490 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 491 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 492 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 493 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 494 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 495 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 496 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 497 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 498 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 499 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 500 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 501 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 502 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 503 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 504 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 505 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 506 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 507 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 508 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 509 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 510 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 511 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 512 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 513 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 514 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 515 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 516 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 517 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 518 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 519 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 520 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 521 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 522 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 523 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 524 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 525 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 526 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 527 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 528 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 529 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 530 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 531 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 532 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 533 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 534 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 535 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 536 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 537 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 538 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 539 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 540 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 541 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 542 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 543 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 544 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 545 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 546 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 547 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 548 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 549 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 550 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 551 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 552 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 553 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 554 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 555 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 556 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 557 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
