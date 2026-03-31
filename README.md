# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-03-31.md)

*最后自动更新时间: 2026-03-31 18:22:24*
## 1. Claude Code 源代码通过其 NPM 仓库中的 map 文件泄露。

**原文标题**: Claude Code's source code has been leaked via a map file in their NPM registry

**原文链接**: [https://twitter.com/Fried_rice/status/2038894956459290963](https://twitter.com/Fried_rice/status/2038894956459290963)

根据提供的标题，以下是该报道事件的简要总结：

**总结：Claude Code 源代码泄露**

据报告显示，Anthropic 为开发者提供的命令行界面（CLI）工具 **Claude Code** 的源代码，因疏忽通过 **NPM（Node 包管理器）注册表** 意外暴露。

此次泄露是由于在公共包中包含了 **源码映射文件（.map）** 导致的。在 Web 开发中，源码映射文件用于将压缩或混淆后的生产代码映射回原始的可读源码，以便进行调试。通过将这些文件发布到公共注册表，Claude Code 工具的原始逻辑、注释和结构便可被公众访问。

这一事件是软件分发中常见安全疏忽的一个典型案例：由于在上传至包管理器之前未能妥善过滤构建产物，导致敏感的内部代码意外曝光。

**注：** 您在请求中提供的内容是 X（原 Twitter）关于禁用 JavaScript 的占位错误信息；上述总结是基于您提供的特定标题生成的。

---

## 2. Cohere Transcribe：语音识别

**原文标题**: Cohere Transcribe: Speech Recognition

**原文链接**: [https://cohere.com/blog/transcribe](https://cohere.com/blog/transcribe)

Cohere 宣布推出 **Transcribe**，这是一款尖端的开源自动语音识别 (ASR) 模型，专为高性能企业级工作流而设计。该模型拥有 20 亿（2B）参数，采用基于 Conformer 的编码器-解码器架构，并遵循 **Apache 2.0 开源协议**。

**核心亮点：**
*   **业界领先的准确率：** Transcribe 目前在 **Hugging Face 的开源 ASR 排行榜上名列第一**，平均词错率 (WER) 为 5.42%。其性能超越了 OpenAI 的 Whisper Large v3、ElevenLabs Scribe v2 以及 Qwen3-ASR 等知名模型。
*   **生产级效率：** 该模型专为实际应用而非单纯的研究而设计，实现了准确率与高吞吐量 (RTFx) 的平衡。它具有适中的推理占用空间，适用于本地 GPU 使用或大规模部署。
*   **多语言能力：** 该模型从零开始在包括英语、法语、普通话、日语、韩语和阿拉伯语在内的 **14 种语言**上进行了训练。
*   **真实场景的鲁棒性：** 测试表明，该模型在多发言人环境、不同口音和会议室音效等挑战性条件下表现优异。人工评估证实了这些提升，特别是在实体识别和格式化方面。

**获取方式与未来整合：**
用户可以通过 Hugging Face 下载该模型，通过 Cohere 的 API 进行访问，或通过 Cohere 的托管安全推理平台 **Model Vault** 进行部署。展望未来，Cohere 计划将 Transcribe 与其 AI 智能体编排平台 **North** 集成，推动该模型从单一的转录工具转型为企业语音智能的综合基础。

---

## 3. Axios 在 NPM 上遭到入侵 – 恶意版本植入远程访问木马

**原文标题**: Axios compromised on NPM – Malicious versions drop remote access trojan

**原文链接**: [https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan)

2026年3月30日，广受欢迎的JavaScript库 **axios** 在npm注册表中遭到入侵。在一名主要维护者的账户被劫持后，恶意版本 **1.14.1** 和 **0.30.4** 被发布。此次攻击具有极高的操作复杂性和外科手术般的精准度。

受侵害的发行版注入了一个隐藏依赖项 **plain-crypto-js@4.2.1**，该依赖项从未被导入到 axios 的源代码中。相反，该依赖项触发了一个 `postinstall` 脚本，充当针对 Windows、macOS 和 Linux 的跨平台远程访问木马（RAT）投放器。安装后，该投放器会联系命令控制（C2）服务器，以交付针对特定平台的第二阶段负载。

为了逃避检测，攻击者采用了先进的反取证技术：
*   **预置：** 在18小时前提前发布了一个干净的恶意依赖项“诱饵”版本（4.2.0），以建立合法的发布历史。
*   **自毁：** 执行后，恶意软件会删除自身，并将其 `package.json` 替换为诱饵版本（4.2.0）。这会导致 `npm list` 报告干净的版本，从而可能误导事件响应人员。
*   **绕过 CI/CD：** 恶意版本是通过窃取的访问令牌手动发布的，绕过了项目标准的 OIDC 验证 GitHub Actions 流水线。

StepSecurity 通过标记指向 C2 域名 `sfrclak.com` 的异常出站连接识别了此次入侵。npm 随后撤销了恶意版本的发布，并用安全存根替换了攻击者的软件包。尽管恶意版本的存续时间仅约为两到三小时，但在此窗口期内执行过安装的任何环境都面临风险。建议开发者确保使用 axios 1.14.0 或更高版本（不包括 1.14.1），并检查其 `node_modules` 中是否存在 `plain-crypto-js` 目录。

---

## 4. 浏览器中的开源CAD (Solvespace)

**原文标题**: Open source CAD in the browser (Solvespace)

**原文链接**: [https://solvespace.com/webver.pl](https://solvespace.com/webver.pl)

开源参数化 2D/3D CAD 工具 SolveSpace 现已推出实验性网页版。虽然该软件主要针对桌面端开发，但目前已通过 Emscripten 编译，可以直接在浏览器中运行。

本次实验性版本的主要亮点包括：

*   **功能与性能：** 尽管目前处于实验阶段，存在一定的性能损耗和漏洞，但网页版仍具有很高的可用性，尤其适用于小型模型。
*   **开发状态：** 此版本基于最新的开发分支构建。用户可能会遇到桌面版中不存在的问题，诚邀用户报告漏洞以协助改进。
*   **隐私与便携性：** 加载完成后，该应用不再依赖网络，确保可以离线运行。
*   **自托管：** 开发者可以自行构建该软件，并将其作为标准的静态网页内容进行托管。

这一举措将 SolveSpace CAD 精简而强大的功能带到了浏览器中，无需本地安装即可在不同平台上进行参数化建模，提升了易用性。

---

## 5. Show HN: Forkrun – NUMA 感知的 Shell 并行工具（比 parallel 快 50–400 倍）

**原文标题**: Show HN: Forkrun – NUMA-aware shell parallelizer (50×–400× faster than parallel)

**原文链接**: [https://github.com/jkool702/forkrun](https://github.com/jkool702/forkrun)

**forkrun** 是一款高性能、支持 NUMA 的 shell 并行器，旨在作为 GNU Parallel 和 `xargs -P` 的无缝替代方案。它解决了传统工具的性能瓶颈——特别是高 IPC 开销和现代多插槽系统上的低 CPU 利用率——其速度比 GNU Parallel 快 50 到 400 倍。

**关键性能特性：**
*   **高效率：** 在所有核心上实现 95–99% 的 CPU 利用率，而 GNU Parallel 仅为 6% 左右。
*   **海量吞吐量：** 每秒支持超过 200,000 次批量调度，在特定流模式下每秒可处理多达 15 亿行数据。
*   **NUMA 感知设计：** 采用“原生本地（born-local）”内存策略，最大限度地减少跨插槽数据迁移，确保在深层 NUMA 硬件上实现线性扩展。

**技术架构：**
forkrun 利用四阶段流水线来保持物理局部性并减少竞争：
1.  **摄取 (Ingest)：** 通过 `splice()` 将数据移动到共享 `memfd` 中，并通过内存策略将内存页绑定到特定的 NUMA 节点。
2.  **索引 (Index)：** 每个节点的索引器使用 AVX2/NEON SIMD 扫描，以内存带宽级的速度识别记录边界。
3.  **认领 (Claim)：** 工作线程使用原子操作进行无竞争的任务认领，避免了传统的锁机制。
4.  **自调节 (Self-Tuning)：** 内部基于 PID 的控制器根据系统压力和输入速率实时自动优化批处理大小。

**易用性与

项目规划包括增强故障隔离、为集群作业（如 Slurm）添加中断后恢复功能，以及与工作负载管理器的深度集成。

---

## 6. GitHub Monaspace 案例研究

**原文标题**: GitHub Monaspace Case Study

**原文链接**: [https://lettermatic.com/custom/monaspace-case-study](https://lettermatic.com/custom/monaspace-case-study)

与 GitHub Next 合作，字体设计公司 Lettermatic 开发了 **Monaspace**。这是一个开源的超级字体家族，包含五款旨在现代化编程体验的等宽字体。该项目于 2023 年 11 月发布，旨在解决开发者排版领域长期停滞的问题——在此之前，代码的清晰度和多样性往往局限于单一字体和基础的颜色编码语法高亮。

Monaspace 超级家族由五种独特的风格组成：**Neon**（无衬线体）、**Argon**（人文主义体）、**Radon**（手写体）、**Krypton**（机械感体）和 **Xenon**（粗衬线体），共计 210 种样式。这些字体基于共享网格构建，可以相互替换，允许开发者在不破坏代码对齐的情况下混合使用不同风格。每款字体支持 200 多种语言，并包含粗细、宽度和倾斜等可变轴，提供了前所未有的个性化空间。

该项目最重要的创新是**纹理修复 (Texture Healing)**。这种上下文感知技术解决了等宽字体设计的根本缺陷：宽字符（如 m、w）的尴尬“挤压感”以及窄字符（如 i、l）周围过多的空白。纹理修复允许相邻字符“协商”空间；例如，窄字符 'i' 可以为宽字符 'm' 让出空间。这产生了一种更平衡、更具“比例感”的纹理，在严格保持等宽网格的同时，提高了易读性并减轻了视觉疲劳。

通过引入排版风格作为语法高亮的新维度，Monaspace 为开发者提供了一套精致且实用的工具包。该项目体现了 GitHub 对开源软件的承诺，将高端、高性能的排版设计免费提供给全球编程社区。

---

## 7. Accidentally created my first fork bomb with Claude Code

**原文标题**: Accidentally created my first fork bomb with Claude Code

**原文链接**: [https://www.droppedasbaby.com/posts/2602-01/](https://www.droppedasbaby.com/posts/2602-01/)

生成摘要时出错

---

## 8. Ollama is now powered by MLX on Apple Silicon in preview

**原文标题**: Ollama is now powered by MLX on Apple Silicon in preview

**原文链接**: [https://ollama.com/blog/mlx](https://ollama.com/blog/mlx)

生成摘要时出错

---

## 9. Good code will still win

**原文标题**: Good code will still win

**原文链接**: [https://www.greptile.com/blog/ai-slopware-future](https://www.greptile.com/blog/ai-slopware-future)

生成摘要时出错

---

## 10. Artemis II is not safe to fly

**原文标题**: Artemis II is not safe to fly

**原文链接**: [https://idlewords.com/2026/03/artemis_ii_is_not_safe_to_fly.htm](https://idlewords.com/2026/03/artemis_ii_is_not_safe_to_fly.htm)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 2 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 3 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 4 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 5 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 6 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 7 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 8 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 9 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 10 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 11 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 12 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 13 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 14 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 15 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 16 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 17 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 18 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 19 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 20 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 21 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 22 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 23 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 24 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 25 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 26 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 27 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 28 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 29 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 30 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 31 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 32 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 33 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 34 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 35 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 36 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 37 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 38 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 39 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 40 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 41 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 42 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 43 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 44 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 45 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 46 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 47 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 48 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 49 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 50 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 51 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 52 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 53 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 54 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 55 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 56 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 57 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 58 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 59 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 60 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 61 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 62 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 63 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 64 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 65 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 66 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 67 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 68 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 69 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 70 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 71 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 72 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 73 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 74 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 75 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 76 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 77 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 78 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 79 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 80 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 81 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 82 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 83 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 84 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 85 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 86 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 87 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 88 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 89 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 90 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 91 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 92 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 93 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 94 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 95 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 96 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 97 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 98 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 99 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 100 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 101 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 102 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 103 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 104 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 105 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 106 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 107 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 108 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 109 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 110 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 111 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 112 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 113 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 114 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 115 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 116 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 117 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 118 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 119 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 120 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 121 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 122 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 123 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 124 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 125 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 126 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 127 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 128 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 129 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 130 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 131 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 132 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 133 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 134 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 135 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 136 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 137 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 138 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 139 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 140 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 141 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 142 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 143 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 144 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 145 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 146 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 147 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 148 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 149 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 150 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 151 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 152 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 153 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 154 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 155 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 156 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 157 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 158 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 159 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 160 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 161 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 162 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 163 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 164 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 165 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 166 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 167 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 168 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 169 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 170 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 171 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 172 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 173 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 174 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 175 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 176 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 177 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 178 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 179 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 180 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 181 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 182 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 183 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 184 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 185 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 186 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 187 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 188 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 189 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 190 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 191 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 192 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 193 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 194 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 195 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 196 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 197 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 198 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 199 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 200 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 201 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 202 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 203 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 204 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 205 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 206 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 207 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 208 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 209 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 210 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 211 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 212 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 213 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 214 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 215 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 216 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 217 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 218 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 219 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 220 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 221 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 222 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 223 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 224 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 225 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 226 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 227 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 228 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 229 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 230 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 231 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 232 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 233 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 234 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 235 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 236 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 237 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 238 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 239 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 240 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 241 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 242 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 243 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 244 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 245 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 246 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 247 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 248 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 249 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 250 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 251 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 252 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 253 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 254 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 255 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 256 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 257 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 258 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 259 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 260 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 261 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 262 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 263 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 264 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 265 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 266 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 267 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 268 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 269 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 270 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 271 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 272 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 273 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 274 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 275 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 276 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 277 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 278 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 279 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 280 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 281 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 282 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 283 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 284 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 285 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 286 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 287 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 288 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 289 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 290 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 291 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 292 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 293 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 294 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 295 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 296 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 297 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 298 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 299 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 300 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 301 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 302 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 303 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 304 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 305 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 306 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 307 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 308 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 309 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 310 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 311 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 312 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 313 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 314 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 315 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 316 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 317 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 318 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 319 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 320 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 321 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 322 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 323 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 324 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 325 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 326 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 327 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 328 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 329 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 330 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 331 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 332 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 333 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 334 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 335 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 336 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 337 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 338 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 339 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 340 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 341 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 342 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 343 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 344 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 345 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 346 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 347 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 348 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 349 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 350 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 351 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 352 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 353 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 354 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 355 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 356 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 357 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 358 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 359 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 360 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 361 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 362 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 363 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 364 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 365 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 366 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 367 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 368 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 369 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 370 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 371 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 372 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 373 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 374 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 375 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 376 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
