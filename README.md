# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-28.md)

*最后自动更新时间: 2026-04-28 18:44:43*
## 1. Localsend：AirDrop 的开源跨平台替代方案

**原文标题**: Localsend: An open-source cross-platform alternative to AirDrop

**原文链接**: [https://github.com/localsend/localsend](https://github.com/localsend/localsend)

**LocalSend** 是一款免费、开源、跨平台的 AirDrop 替代方案，支持在本地网络中安全地共享文件和消息。与许多竞争对手不同，它不需要互联网连接或第三方服务器，而是利用 REST API 和带有即时生成 SSL 证书的 HTTPS 加密，以确保隐私和传输速度。

**核心功能与兼容性：**
*   **广泛的平台支持：** 兼容 Android (5.0+)、iOS (12.0+)、macOS (11+)、Windows (10+)、Linux 和 Fire OS。
*   **灵活的分发方式：** 可通过主流应用商店（App Store、Play Store）、包管理器（Homebrew、Winget、Nixpkgs、F-Droid）以及便携式二进制文件获取。
*   **技术规格：** 基于 **Flutter** 和 **Rust** 构建，通过 53317 端口进行通信。包含“便携模式”和用于系统托盘集成的“隐藏启动”标志等高级选项。

**设置与故障排除：**
虽然该应用设计为开箱即用，但用户可能需要配置防火墙以允许通信，或禁用路由器上的“AP 隔离”。对于 Windows 用户，建议将网络类型设置为“专用”以确保设备可见。

**社区与开发：**
作为一个社区驱动的项目，LocalSend 鼓励通过以下方式做出贡献：
*   **** 通过 Weblate 或手动编辑 i18n 文件进行管理。
*   **开发：** 提供了使用 Flutter 和 Rust 从源代码构建应用的详细说明。
*   **Bug 修复：** 用户可以通过 GitHub 或 Codeberg 报告问题或提交拉取请求。

总之，LocalSend 为需要在不同操作系统之间快速迁移数据，且不愿依赖云服务的用户提供了一个强大、注重隐私的解决方案。

---

## 2. Claude.ai 无法使用

**原文标题**: Claude.ai is unavailable

**原文链接**: [https://status.claude.com/incidents/9l93x2ht4s5w](https://status.claude.com/incidents/9l93x2ht4s5w)

2026年4月28日，Anthropic 报告其全线产品出现重大服务中断。该事件始于 UTC 时间 17:41 的连接问题报告，并在 17:51 升级为“已确认”故障。

**本次停机事件的关键详情包括：**

*   **受影响的服务：** 此次中断影响了 Claude.ai、Claude API (api.anthropic.com)、Claude 控制台 (Claude Console)、Claude Code（包括登录路径）、Claude Cowork 以及 Claude for Government。
*   **当前状态：** 用户面临 API 错误率升高以及完全无法访问 Claude.ai 界面的问题。
*   **已采取的措施：** Anthropic 已查明故障原因，目前正在努力修复。

该公司承诺在致力于恢复平台全部功能的过程中，将持续发布更新动态。

---

## 3. 微软 VibeVoice：开源前沿语音 AI

**原文标题**: Microsoft VibeVoice: Open-Source Frontier Voice AI

**原文链接**: [https://github.com/microsoft/VibeVoice](https://github.com/microsoft/VibeVoice)

微软推出了 **VibeVoice**，这是一个开源研究框架，包含了用于自动语音识别 (ASR) 和文本转语音 (TTS) 的前沿语音 AI 模型。该框架的核心创新在于采用了工作在超低帧率（7.5 Hz）下的连续语音分词器以及下一标记扩散（next-token diffusion）框架，从而实现了极高的效率并支持超长音频序列的处理。

该套件包含三个主要模型：

1.  **VibeVoice-ASR (7B)：** 一个统一模型，可一次性处理长达 60 分钟的音频。与需要对音频进行分段处理的传统模型不同，它能保持全局上下文，提供包含说话人识别（“谁”）、时间戳（“何时”）和内容（“什么”）的结构化转录。它支持 50 多种语言和自定义热词。
2.  **VibeVoice-TTS (1.5B)：** 专为长文本、多说话人合成（长达 90 分钟）而设计，支持最多四个不同说话人的自然交替对话。尽管该模型已被 ICLR 2026 接收为口头报告 (Oral)，但微软已从公共代码库中移除了 TTS 代码，以恪守其负责任的 AI 原则并防止滥用。
3.  **VibeVoice-Realtime (0.5B)：** 用于流式 TTS 的轻量级、易部署模型。它具有低延迟（约 300 毫秒）的特点，并支持实时应用的流式文本输入。

最近的更新包括：将 VibeVoice-ASR 集成到 Hugging Face Transformers 库中，支持 vLLM 以实现更快的推理，以及发布了微调代码。

**安全与伦理：** 微软强调 VibeVoice 仅用于研究目的。提醒用户注意深度伪造 (deepfakes) 和虚假信息的潜在风险。这些模型还可能继承其基座模型 (Qwen2.5) 的偏见。微软鼓励负责任的使用，并提倡披露 AI 生成的内容。

---

## 4. AISLE 在 OpenEMR 医疗软件中发现 38 个 CVE 漏洞

**原文标题**: AISLE Discovers 38 CVEs in OpenEMR Healthcare Software

**原文链接**: [https://aisle.com/blog/aisle-discovers-38-critical-security-vulnerabilities-in-healthcare-software-used-by-100000-providers](https://aisle.com/blog/aisle-discovers-38-critical-security-vulnerabilities-in-healthcare-software-used-by-100000-providers)

AISLE 研究人员最近在 OpenEMR 中发现了 38 个 CVE 漏洞。OpenEMR 是一个领先的开源电子健康记录 (EHR) 平台，为超过 10 万名医疗服务提供商和 2 亿名患者提供服务。在 2026 年第一季度，AISLE 团队利用自主式人工智能驱动分析器，在单季度内发现的漏洞数量超过了以往高规格人工审计在更长时间跨度内发现的总和。

调查结果包括多个严重级别的缺陷，可能导致数据库全面沦陷以及受保护健康信息 (PHI) 的外泄。值得注意的是，**CVE-2026-24908**（患者 REST API 中的 CVSS 10.0 SQL 注入）和 **CVE-2026-23627**（免疫模块中的 SQL 注入）可能允许攻击者执行远程代码或读取服务器敏感文件。其他重大漏洞还包括 FHIR 分隔绕过、跨站脚本攻击 (XSS) 以及广泛存在的不安全直接对象引用 (IDOR) 问题，即端点未能验证用户权限。

AISLE 与 OpenEMR 基金会的合作促进了漏洞的快速修复。AISLE 提供了针对代码库原生的修复建议，大部分补丁已于 2026 年 2 月（即初始披露后仅数周）随 OpenEMR 8.0.0 版本发布。

为了从“发现”转型为“预防”，双方已正式建立合作伙伴关系，将 AISLE 的人工智能驱动提交分析器直接集成到 OpenEMR 的代码审查工作流中。这使得维护者能够在漏洞进入生产环境之前进行检测和修复。此次合作凸显了医疗数字化与安全之间“不断扩大的差距”，并展示了人工智能驱动的防御手段如何应对针对关键医疗基础设施的、日益复杂的 AI 驱动威胁。

---

## 5. Laguna XS.2 和 M.1

**原文标题**: Laguna XS.2 and M.1

**原文链接**: [https://poolside.ai/blog/laguna-a-deeper-dive](https://poolside.ai/blog/laguna-a-deeper-dive)

Laguna 宣布发布其首批两款“智能体”编程模型：**Laguna M.1** 和 **Laguna XS.2**，专为长周期任务和自主代码执行而设计。此次发布标志着该公司从服务高安全性政府客户向贡献权重开放生态系统的转型。

**模型规格与性能**
*   **Laguna M.1：** 拥有 225B 参数的混合专家（MoE）模型，激活参数为 23B。该模型在超过 6,000 颗 NVIDIA Hopper GPU 上使用 30T token 进行训练，在 SWE-bench Pro 基准测试中取得了 46.9% 的成绩。
*   **Laguna XS.2：** 侧重于效率的 33B MoE 模型（激活参数为 3B）。尽管体积较小，但其表现惊人，在 SWE-bench Pro 上得分达 44.5%。该模型采用 Apache 2.0 协议开放。

**技术创新**
这些模型优先考虑编写和执行代码，而非简单的工具调用，将软件视为智能体更具表现力的接口。训练过程由三大核心支柱驱动：
1.  **数据与 AutoMixing：** 模型使用了 30T token 的数据集，其中包括 4.4T 合成 token。专有的“AutoMixer”框架通过训练 60 个代理模型来衡量不同数据比例对代码、数学和 STEM 性能的影响，从而优化数据配比。
2.  **Muon 优化器：** 团队采用了 Muon 优化器的分布式实现。在达到与 AdamW 相同训练损失的情况下，其步数减少了 15%，且内存开销更低。
3.  **硬件优化：** 基于 NVIDIA 硬件开发，Laguna XS.2 在发布首日即支持 TensorRT-LLM 和 NVIDIA Blackwell 架构（NVFP4）。

Laguna XS.2 可通过 API、OpenRouter 获取或直接下载。此次发布还包含一个智能体客户端协议（ACP）服务器，旨在帮助开发者构建和运行智能体。

---

## 6. Show HN：带 NASA 影像素材的日月实时仪表板

**原文标题**: Show HN: Live Sun and Moon Dashboard with NASA Footage

**原文链接**: [https://www.lumara-space.app/](https://www.lumara-space.app/)

This "Live Sun and Moon Dashboard" is a real-time visualization tool featuring high-frequency footage from NASA. The solar portion of the dashboard utilizes data from the Solar Dynamics Observatory (SDO), updating every 12 seconds to provide a near-continuous view of the Sun.

By capturing the Sun in 12 distinct wavelengths, the project allows viewers to observe various layers of solar activity that are otherwise invisible. The imagery spans a massive thermal range, from the 5,000 K visible surface to the intense 10 million K plasma found in solar flares, offering a comprehensive look at the star's dynamic behavior.

---

## 7. Claude Code 编写的代码归谁所有？

**原文标题**: Who owns the code Claude Code wrote?

**原文链接**: [https://legallayer.substack.com/p/who-owns-the-claude-code-wrote](https://legallayer.substack.com/p/who-owns-the-claude-code-wrote)

本文探讨了 Anthropic 新推出的开发者工具 **Claude Code** 所生成代码的所有权法律影响。

核心观点总结如下：

**合同所有权**
根据 Anthropic 的服务条款，公司将输出内容的所有“权利、权属和权益”均转让给用户。这意味着从合同角度来看，用户拥有 Claude 生成代码的所有权。

**版权挑战**
尽管有服务条款的规定，美国版权局 (USCO) 目前仍坚持认为，缺乏“人类作者身份”的 AI 生成内容不具备版权保护资格。要主张版权，人类必须提供重大的创意投入或对 AI 输出进行实质性修改。仅提供提示词通常被认为不足以确立法律上的作者身份。这导致了“版权真空”的出现，即纯 AI 生成的代码可能处于公共领域，使开发者难以针对第三方进行维权。

**赔偿与知识产权保护**
Anthropic 为 Pro、Team 或 Enterprise 计划的付费用户提供“商业知识产权保护”。该政策充当了法律盾牌：只要用户并非故意诱导工具生成侵权内容，若工具输出被判定侵犯第三方知识产权，公司承诺为用户辩护并承担赔偿责任。

**数据隐私**
虽然 Claude Code 通过命令行界面 (CLI) 运行，但它会将数据传回 Anthropic 的服务器。不过，对于商业用户，Anthropic 通常不会利用“客户内容”来训练其核心模型，这为私有代码库提供了一定程度的安全保障。

**结论**
虽然 Anthropic 通过条款授予了用户所有权，但这些权利的法律效力受到现行版权法的限制。开发者拥有代码的商业使用权，但除非投入了显著的人类创意贡献，否则可能难以在法律层面保护这些代码。

---

## 8. Things C++26 define_static_array can't do

**原文标题**: Things C++26 define_static_array can't do

**原文链接**: [https://quuxplusone.github.io/blog/2026/04/24/define-static-array/](https://quuxplusone.github.io/blog/2026/04/24/define-static-array/)

生成摘要时出错

---

## 9. Infisical (YC W23) Is Hiring Full Stack Software Engineers (Remote)

**原文标题**: Infisical (YC W23) Is Hiring Full Stack Software Engineers (Remote)

**原文链接**: [https://jobs.ashbyhq.com/infisical/782b9da8-20e1-48b2-919e-6c5430c58628](https://jobs.ashbyhq.com/infisical/782b9da8-20e1-48b2-919e-6c5430c58628)

生成摘要时出错

---

## 10. I have officially retired from Emacs

**原文标题**: I have officially retired from Emacs

**原文链接**: [https://nullprogram.com/blog/2026/04/26/](https://nullprogram.com/blog/2026/04/26/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 2 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 3 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 4 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 5 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 6 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 7 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 8 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 9 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 10 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 11 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 12 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 13 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 14 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 15 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 16 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 17 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 18 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 19 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 20 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 21 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 22 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 23 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 24 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 25 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 26 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 27 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 28 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 29 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 30 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 31 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 32 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 33 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 34 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 35 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 36 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 37 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 38 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 39 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 40 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 41 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 42 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 43 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 44 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 45 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 46 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 47 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 48 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 49 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 50 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 51 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 52 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 53 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 54 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 55 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 56 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 57 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 58 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 59 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 60 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 61 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 62 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 63 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 64 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 65 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 66 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 67 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 68 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 69 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 70 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 71 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 72 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 73 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 74 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 75 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 76 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 77 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 78 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 79 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 80 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 81 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 82 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 83 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 84 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 85 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 86 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 87 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 88 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 89 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 90 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 91 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 92 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 93 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 94 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 95 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 96 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 97 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 98 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 99 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 100 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 101 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 102 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 103 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 104 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 105 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 106 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 107 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 108 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 109 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 110 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 111 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 112 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 113 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 114 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 115 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 116 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 117 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 118 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 119 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 120 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 121 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 122 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 123 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 124 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 125 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 126 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 127 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 128 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 129 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 130 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 131 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 132 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 133 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 134 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 135 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 136 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 137 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 138 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 139 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 140 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 141 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 142 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 143 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 144 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 145 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 146 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 147 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 148 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 149 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 150 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 151 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 152 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 153 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 154 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 155 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 156 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 157 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 158 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 159 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 160 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 161 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 162 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 163 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 164 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 165 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 166 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 167 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 168 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 169 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 170 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 171 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 172 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 173 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 174 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 175 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 176 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 177 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 178 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 179 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 180 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 181 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 182 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 183 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 184 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 185 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 186 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 187 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 188 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 189 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 190 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 191 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 192 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 193 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 194 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 195 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 196 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 197 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 198 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 199 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 200 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 201 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 202 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 203 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 204 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 205 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 206 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 207 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 208 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 209 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 210 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 211 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 212 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 213 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 214 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 215 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 216 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 217 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 218 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 219 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 220 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 221 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 222 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 223 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 224 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 225 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 226 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 227 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 228 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 229 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 230 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 231 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 232 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 233 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 234 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 235 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 236 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 237 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 238 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 239 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 240 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 241 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 242 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 243 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 244 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 245 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 246 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 247 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 248 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 249 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 250 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 251 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 252 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 253 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 254 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 255 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 256 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 257 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 258 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 259 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 260 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 261 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 262 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 263 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 264 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 265 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 266 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 267 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 268 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 269 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 270 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 271 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 272 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 273 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 274 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 275 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 276 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 277 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 278 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 279 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 280 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 281 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 282 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 283 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 284 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 285 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 286 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 287 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 288 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 289 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 290 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 291 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 292 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 293 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 294 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 295 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 296 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 297 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 298 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 299 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 300 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 301 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 302 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 303 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 304 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 305 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 306 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 307 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 308 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 309 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 310 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 311 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 312 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 313 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 314 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 315 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 316 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 317 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 318 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 319 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 320 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 321 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 322 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 323 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 324 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 325 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 326 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 327 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 328 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 329 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 330 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 331 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 332 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 333 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 334 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 335 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 336 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 337 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 338 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 339 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 340 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 341 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 342 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 343 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 344 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 345 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 346 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 347 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 348 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 349 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 350 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 351 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 352 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 353 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 354 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 355 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 356 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 357 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 358 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 359 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 360 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 361 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 362 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 363 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 364 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 365 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 366 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 367 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 368 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 369 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 370 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 371 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 372 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 373 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 374 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 375 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 376 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 377 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 378 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 379 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 380 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 381 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 382 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 383 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 384 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 385 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 386 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 387 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 388 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 389 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 390 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 391 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 392 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 393 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 394 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 395 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 396 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 397 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 398 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 399 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 400 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 401 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 402 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 403 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 404 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
