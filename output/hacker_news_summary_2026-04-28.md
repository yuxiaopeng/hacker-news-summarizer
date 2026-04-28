# Hacker News 热门文章摘要 (2026-04-28)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Google and Pentagon reportedly agree on deal for 'any lawful' use of AI

**原文标题**: Google and Pentagon reportedly agree on deal for 'any lawful' use of AI

**原文链接**: [https://www.theverge.com/ai-artificial-intelligence/919494/google-pentagon-classified-ai-deal](https://www.theverge.com/ai-artificial-intelligence/919494/google-pentagon-classified-ai-deal)

生成摘要时出错

---

## 12. FCC Funding Application Notes Paramount Will Be 49.5% Foreign-Owned Post-Merger

**原文标题**: FCC Funding Application Notes Paramount Will Be 49.5% Foreign-Owned Post-Merger

**原文链接**: [https://deadline.com/2026/04/paramount-fcc-request-wbd-merger-middle-east-1236873732/](https://deadline.com/2026/04/paramount-fcc-request-wbd-merger-middle-east-1236873732/)

生成摘要时出错

---

## 13. GitHub RCE Vulnerability: CVE-2026-3854 Breakdown

**原文标题**: GitHub RCE Vulnerability: CVE-2026-3854 Breakdown

**原文链接**: [https://www.wiz.io/blog/github-rce-vulnerability-cve-2026-3854](https://www.wiz.io/blog/github-rce-vulnerability-cve-2026-3854)

生成摘要时出错

---

## 14. GitHub Copilot code review will start consuming GitHub Actions minutes

**原文标题**: GitHub Copilot code review will start consuming GitHub Actions minutes

**原文链接**: [https://github.blog/changelog/2026-04-27-github-copilot-code-review-will-start-consuming-github-actions-minutes-on-june-1-2026/](https://github.blog/changelog/2026-04-27-github-copilot-code-review-will-start-consuming-github-actions-minutes-on-june-1-2026/)

生成摘要时出错

---

## 15. Deep under Antarctic ice, a long-predicted cosmic whisper breaks through

**原文标题**: Deep under Antarctic ice, a long-predicted cosmic whisper breaks through

**原文链接**: [https://phys.org/news/2026-04-deep-antarctic-ice-cosmic-strange.html](https://phys.org/news/2026-04-deep-antarctic-ice-cosmic-strange.html)

生成摘要时出错

---

## 16. GitHub Actions is the weakest link

**原文标题**: GitHub Actions is the weakest link

**原文链接**: [https://nesbitt.io/2026/04/28/github-actions-is-the-weakest-link.html](https://nesbitt.io/2026/04/28/github-actions-is-the-weakest-link.html)

生成摘要时出错

---

## 17. Talkie: a 13B vintage language model from 1930

**原文标题**: Talkie: a 13B vintage language model from 1930

**原文链接**: [https://talkie-lm.com/introducing-talkie](https://talkie-lm.com/introducing-talkie)

生成摘要时出错

---

## 18. ASML became the chokepoint for cutting-edge chips

**原文标题**: ASML became the chokepoint for cutting-edge chips

**原文链接**: [https://worksinprogress.co/issue/the-worlds-most-complex-machine/](https://worksinprogress.co/issue/the-worlds-most-complex-machine/)

生成摘要时出错

---

## 19. Anthropic Joins the Blender Development Fund as Corporate Patron

**原文标题**: Anthropic Joins the Blender Development Fund as Corporate Patron

**原文链接**: [https://www.blender.org/press/anthropic-joins-the-blender-development-fund-as-corporate-patron/](https://www.blender.org/press/anthropic-joins-the-blender-development-fund-as-corporate-patron/)

生成摘要时出错

---

## 20. PyWry: Cross-Platform Rendering Engine in Python

**原文标题**: PyWry: Cross-Platform Rendering Engine in Python

**原文链接**: [https://deeleeramone.github.io/PyWry/](https://deeleeramone.github.io/PyWry/)

生成摘要时出错

---

## 21. AI's Economics Don't Make Sense

**原文标题**: AI's Economics Don't Make Sense

**原文链接**: [https://www.wheresyoured.at/ais-economics-dont-make-sense/](https://www.wheresyoured.at/ais-economics-dont-make-sense/)

生成摘要时出错

---

## 22. UAE Leaves OPEC and OPEC+

**原文标题**: UAE Leaves OPEC and OPEC+

**原文链接**: [https://www.reuters.com/markets/commodities/uae-says-it-quits-opec-opec-statement-2026-04-28/](https://www.reuters.com/markets/commodities/uae-says-it-quits-opec-opec-statement-2026-04-28/)

生成摘要时出错

---

## 23. Can You Find the Comet?

**原文标题**: Can You Find the Comet?

**原文链接**: [https://apod.nasa.gov/apod/ap260427.html](https://apod.nasa.gov/apod/ap260427.html)

生成摘要时出错

---

## 24. Cybersec is a thankless job: expanding workload and shrinking pay packet

**原文标题**: Cybersec is a thankless job: expanding workload and shrinking pay packet

**原文链接**: [https://www.theregister.com/2026/04/27/from_a_massive_skills_gap/](https://www.theregister.com/2026/04/27/from_a_massive_skills_gap/)

生成摘要时出错

---

## 25. I Spent My Sabbatical Building a Power Meter for Sledgehammers

**原文标题**: I Spent My Sabbatical Building a Power Meter for Sledgehammers

**原文链接**: [https://leblancfg.com/intensity-pad-founder-story.html](https://leblancfg.com/intensity-pad-founder-story.html)

生成摘要时出错

---

## 26. After Spain's blackout, its shift to renewables and grid evolution power on

**原文标题**: After Spain's blackout, its shift to renewables and grid evolution power on

**原文链接**: [https://www.theguardian.com/world/2026/apr/28/blackout-spain-renewable-energy-grid-solar-wind](https://www.theguardian.com/world/2026/apr/28/blackout-spain-renewable-energy-grid-solar-wind)

生成摘要时出错

---

## 27. BookStack Moves from GitHub to Codeberg

**原文标题**: BookStack Moves from GitHub to Codeberg

**原文链接**: [https://github.com/BookStackApp/BookStack/issues/4551](https://github.com/BookStackApp/BookStack/issues/4551)

生成摘要时出错

---

## 28. Voice Modems

**原文标题**: Voice Modems

**原文链接**: [https://computer.rip/2026-04-26-voice-modems.html](https://computer.rip/2026-04-26-voice-modems.html)

生成摘要时出错

---

## 29. Physicists Discover the Most Complex Forms of Ice Yet

**原文标题**: Physicists Discover the Most Complex Forms of Ice Yet

**原文链接**: [https://www.quantamagazine.org/physicists-discover-the-most-complex-forms-of-ice-yet-20260427/](https://www.quantamagazine.org/physicists-discover-the-most-complex-forms-of-ice-yet-20260427/)

生成摘要时出错

---

## 30. WASM is not quite a stack machine

**原文标题**: WASM is not quite a stack machine

**原文链接**: [https://purplesyringa.moe/blog/wasm-is-not-quite-a-stack-machine/](https://purplesyringa.moe/blog/wasm-is-not-quite-a-stack-machine/)

生成摘要时出错

---

## 31. Is my blue your blue? (2024)

**原文标题**: Is my blue your blue? (2024)

**原文链接**: [https://ismy.blue/](https://ismy.blue/)

生成摘要时出错

---

## 32. The predictable failure of the QDay Prize

**原文标题**: The predictable failure of the QDay Prize

**原文链接**: [https://algassert.com/post/2601](https://algassert.com/post/2601)

生成摘要时出错

---

## 33. An Update on GitHub Availability

**原文标题**: An Update on GitHub Availability

**原文链接**: [https://github.blog/news-insights/company-news/an-update-on-github-availability/](https://github.blog/news-insights/company-news/an-update-on-github-availability/)

生成摘要时出错

---

## 34. Your phone is about to stop being yours

**原文标题**: Your phone is about to stop being yours

**原文链接**: [https://keepandroidopen.org/en/](https://keepandroidopen.org/en/)

生成摘要时出错

---

## 35. Period tracking app, Flo, found to be selling user data to Meta

**原文标题**: Period tracking app, Flo, found to be selling user data to Meta

**原文链接**: [https://femtechdesigndesk.substack.com/p/your-period-tracking-app-has-been](https://femtechdesigndesk.substack.com/p/your-period-tracking-app-has-been)

生成摘要时出错

---

## 36. Pgrx: Build Postgres Extensions with Rust

**原文标题**: Pgrx: Build Postgres Extensions with Rust

**原文链接**: [https://github.com/pgcentralfoundation/pgrx](https://github.com/pgcentralfoundation/pgrx)

生成摘要时出错

---

## 37. Mo RAM, Mo Problems (2025)

**原文标题**: Mo RAM, Mo Problems (2025)

**原文链接**: [https://fabiensanglard.net/curse/](https://fabiensanglard.net/curse/)

生成摘要时出错

---

## 38. GTFOBins

**原文标题**: GTFOBins

**原文链接**: [https://gtfobins.org/](https://gtfobins.org/)

生成摘要时出错

---

## 39. UAE to leave OPEC

**原文标题**: UAE to leave OPEC

**原文链接**: [https://www.ft.com/content/8c354f2d-3e66-47f1-aad4-9b4aa30e386d](https://www.ft.com/content/8c354f2d-3e66-47f1-aad4-9b4aa30e386d)

生成摘要时出错

---

## 40. Tiled Words 6 Month Update

**原文标题**: Tiled Words 6 Month Update

**原文链接**: [https://paulmakeswebsites.com/writing/six-months-of-tiled-words/](https://paulmakeswebsites.com/writing/six-months-of-tiled-words/)

生成摘要时出错

---

## 41. Warp is now open-source

**原文标题**: Warp is now open-source

**原文链接**: [https://www.warp.dev/blog/warp-is-now-open-source](https://www.warp.dev/blog/warp-is-now-open-source)

生成摘要时出错

---

## 42. Meetings are forcing functions

**原文标题**: Meetings are forcing functions

**原文链接**: [https://www.mooreds.com/wordpress/archives/3734](https://www.mooreds.com/wordpress/archives/3734)

生成摘要时出错

---

## 43. Greece to ban anonymity on social media

**原文标题**: Greece to ban anonymity on social media

**原文链接**: [https://www.euractiv.com/news/greece-to-ban-anonymity-on-social-media/](https://www.euractiv.com/news/greece-to-ban-anonymity-on-social-media/)

生成摘要时出错

---

## 44. In Kannauj, perfumers have been making monsoon-infused mitti attar for centuries

**原文标题**: In Kannauj, perfumers have been making monsoon-infused mitti attar for centuries

**原文链接**: [https://www.atlasobscura.com/articles/smell-of-rain-kannauj-perfume-mitti-attar-india](https://www.atlasobscura.com/articles/smell-of-rain-kannauj-perfume-mitti-attar-india)

生成摘要时出错

---

## 45. Microsoft and OpenAI end their exclusive and revenue-sharing deal

**原文标题**: Microsoft and OpenAI end their exclusive and revenue-sharing deal

**原文链接**: [https://www.bloomberg.com/news/articles/2026-04-27/microsoft-to-stop-sharing-revenue-with-main-ai-partner-openai](https://www.bloomberg.com/news/articles/2026-04-27/microsoft-to-stop-sharing-revenue-with-main-ai-partner-openai)

生成摘要时出错

---

## 46. Easyduino: Open Source PCB Devboards for KiCad

**原文标题**: Easyduino: Open Source PCB Devboards for KiCad

**原文链接**: [https://github.com/Hanqaqa/Easyduino](https://github.com/Hanqaqa/Easyduino)

生成摘要时出错

---

## 47. The Americans queueing up to renounce their citizenship

**原文标题**: The Americans queueing up to renounce their citizenship

**原文链接**: [https://www.theguardian.com/us-news/2026/apr/28/americans-queueing-up-renounce-citizenship-dictatorship](https://www.theguardian.com/us-news/2026/apr/28/americans-queueing-up-renounce-citizenship-dictatorship)

生成摘要时出错

---

## 48. The quiet resurgence of RF engineering

**原文标题**: The quiet resurgence of RF engineering

**原文链接**: [https://atempleton.bearblog.dev/quiet-resurgence-of-rf-engineering/](https://atempleton.bearblog.dev/quiet-resurgence-of-rf-engineering/)

生成摘要时出错

---

## 49. Networking changes coming in macOS 27

**原文标题**: Networking changes coming in macOS 27

**原文链接**: [https://eclecticlight.co/2026/04/23/networking-changes-coming-in-macos-27/](https://eclecticlight.co/2026/04/23/networking-changes-coming-in-macos-27/)

生成摘要时出错

---

## 50. High Performance Git

**原文标题**: High Performance Git

**原文链接**: [https://gitperf.com/](https://gitperf.com/)

生成摘要时出错

---

## 51. How I leared what a decoupling capacitor is for, the hard way

**原文标题**: How I leared what a decoupling capacitor is for, the hard way

**原文链接**: [https://nbelakovski.substack.com/p/how-i-learned-what-a-decoupling-capacitor](https://nbelakovski.substack.com/p/how-i-learned-what-a-decoupling-capacitor)

生成摘要时出错

---

## 52. The woes of sanitizing SVGs

**原文标题**: The woes of sanitizing SVGs

**原文链接**: [https://muffin.ink/blog/scratch-svg-sanitization/](https://muffin.ink/blog/scratch-svg-sanitization/)

生成摘要时出错

---

## 53. Why does walking through doorways make us forget? (2016)

**原文标题**: Why does walking through doorways make us forget? (2016)

**原文链接**: [https://www.bbc.com/future/article/20160307-why-does-walking-through-doorways-make-us-forget](https://www.bbc.com/future/article/20160307-why-does-walking-through-doorways-make-us-forget)

生成摘要时出错

---

## 54. Fedora Linux 44

**原文标题**: Fedora Linux 44

**原文链接**: [https://fedoramagazine.org/announcing-fedora-linux-44/](https://fedoramagazine.org/announcing-fedora-linux-44/)

生成摘要时出错

---

## 55. OpenAI CEO's Identity Verification Company Announced Fake Bruno Mars Partnership

**原文标题**: OpenAI CEO's Identity Verification Company Announced Fake Bruno Mars Partnership

**原文链接**: [https://www.vice.com/en/article/openai-ceo-identity-verification-company-fake-bruno-mars-partnership-mistaken-identity/](https://www.vice.com/en/article/openai-ceo-identity-verification-company-fake-bruno-mars-partnership-mistaken-identity/)

生成摘要时出错

---

## 56. Spanish archaeologists discover trove of ancient shipwrecks in Bay of Gibraltar

**原文标题**: Spanish archaeologists discover trove of ancient shipwrecks in Bay of Gibraltar

**原文链接**: [https://www.theguardian.com/science/2026/apr/15/hidden-treasures-spanish-archaeologists-discover-trove-of-ancient-shipwrecks-in-bay-of-gibraltar](https://www.theguardian.com/science/2026/apr/15/hidden-treasures-spanish-archaeologists-discover-trove-of-ancient-shipwrecks-in-bay-of-gibraltar)

生成摘要时出错

---

## 57. GitHub Copilot is moving to usage-based billing

**原文标题**: GitHub Copilot is moving to usage-based billing

**原文链接**: [https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/)

生成摘要时出错

---

## 58. Three men are facing charges in Toronto SMS Blaster arrests

**原文标题**: Three men are facing charges in Toronto SMS Blaster arrests

**原文链接**: [https://www.tps.ca/media-centre/stories/unprecedented-sms-blaster-arrests/](https://www.tps.ca/media-centre/stories/unprecedented-sms-blaster-arrests/)

生成摘要时出错

---

## 59. Radar Laboratory – Interactive Radar Phenomenology

**原文标题**: Radar Laboratory – Interactive Radar Phenomenology

**原文链接**: [https://radarlaboratory.com/](https://radarlaboratory.com/)

生成摘要时出错

---

## 60. LingBot-Map: Streaming 3D reconstruction with geometric context transformer

**原文标题**: LingBot-Map: Streaming 3D reconstruction with geometric context transformer

**原文链接**: [https://technology.robbyant.com/lingbot-map](https://technology.robbyant.com/lingbot-map)

生成摘要时出错

---

## 61. OpenAI 营收不及预期，AI 泡沫要破裂了吗？

**原文标题**: OpenAI misses revenue, is the AI bubble bursting?

**原文链接**: [https://www.cnbc.com/2026/04/28/openai-reportedly-missed-revenue-targets-shares-of-oracle-and-these-chip-stocks-are-falling.html](https://www.cnbc.com/2026/04/28/openai-reportedly-missed-revenue-targets-shares-of-oracle-and-these-chip-stocks-are-falling.html)

生成摘要时出错

---

## 62. 美国各大航空公司第一季度燃油支出增加12亿美元

**原文标题**: Biggest US airlines spent $1.2B more on fuel in Q1

**原文链接**: [https://sherwood.news/business/the-6-biggest-us-airlines-spent-1-2-billion-more-on-fuel-in-q1-and-things-are-about-to-get-worse/](https://sherwood.news/business/the-6-biggest-us-airlines-spent-1-2-billion-more-on-fuel-in-q1-and-things-are-about-to-get-worse/)

生成摘要时出错

---

## 63. “Why not just use Lean?”

**原文标题**: “Why not just use Lean?”

**原文链接**: [https://lawrencecpaulson.github.io//2026/04/23/Why_not_Lean.html](https://lawrencecpaulson.github.io//2026/04/23/Why_not_Lean.html)

生成摘要时出错

---

## 64. Notice of Obsolescence

**原文标题**: Notice of Obsolescence

**原文链接**: [https://thebuild.com/blog/2026/04/27/notice-of-obsolescence/](https://thebuild.com/blog/2026/04/27/notice-of-obsolescence/)

生成摘要时出错

---

## 65. 4TB of voice samples just stolen from 40k AI contractors at Mercor

**原文标题**: 4TB of voice samples just stolen from 40k AI contractors at Mercor

**原文链接**: [https://app.oravys.com/blog/mercor-breach-2026](https://app.oravys.com/blog/mercor-breach-2026)

生成摘要时出错

---

## 66. Super ZSNES – GPU Powered SNES Emulator

**原文标题**: Super ZSNES – GPU Powered SNES Emulator

**原文链接**: [https://zsnes.com/](https://zsnes.com/)

生成摘要时出错

---

## 67. Utah greenlights 9GW AI campus using over twice state electricity

**原文标题**: Utah greenlights 9GW AI campus using over twice state electricity

**原文链接**: [https://www.tomshardware.com/tech-industry/kevin-o-learys-9-gw-utah-data-center-campus-approved](https://www.tomshardware.com/tech-industry/kevin-o-learys-9-gw-utah-data-center-campus-approved)

生成摘要时出错

---

## 68. DeepSeek-V4: a million-token context that agents can use

**原文标题**: DeepSeek-V4: a million-token context that agents can use

**原文链接**: [https://huggingface.co/blog/deepseekv4](https://huggingface.co/blog/deepseekv4)

生成摘要时出错

---

## 69. Show HN: OSS Agent I built topped the TerminalBench on Gemini-3-flash-preview

**原文标题**: Show HN: OSS Agent I built topped the TerminalBench on Gemini-3-flash-preview

**原文链接**: [https://github.com/dirac-run/dirac](https://github.com/dirac-run/dirac)

生成摘要时出错

---

## 70. AI's Economics Don't Make Sense

**原文标题**: AI's Economics Don't Make Sense

**原文链接**: [https://www.wheresyoured.at/ais-economics-dont-make-sense-ad-free/](https://www.wheresyoured.at/ais-economics-dont-make-sense-ad-free/)

生成摘要时出错

---

## 71. The Prompt API

**原文标题**: The Prompt API

**原文链接**: [https://developer.chrome.com/docs/ai/prompt-api](https://developer.chrome.com/docs/ai/prompt-api)

生成摘要时出错

---

## 72. Lessons from building multiplayer browsers

**原文标题**: Lessons from building multiplayer browsers

**原文链接**: [https://www.alejandro.pe/writing/sail-muddy-lessons](https://www.alejandro.pe/writing/sail-muddy-lessons)

生成摘要时出错

---

## 73. Should we just skip code review now?

**原文标题**: Should we just skip code review now?

**原文链接**: [https://xata.io/blog/ai-codes-humans-engineer](https://xata.io/blog/ai-codes-humans-engineer)

生成摘要时出错

---

## 74. Interview with Bob Odenkirk

**原文标题**: Interview with Bob Odenkirk

**原文链接**: [https://www.nytimes.com/2026/04/25/magazine/bob-odenkirk-interview.html](https://www.nytimes.com/2026/04/25/magazine/bob-odenkirk-interview.html)

生成摘要时出错

---

## 75. $1,605: average annual ad value of a U.S. Google user

**原文标题**: $1,605: average annual ad value of a U.S. Google user

**原文链接**: [https://proton.me/blog/what-is-your-data-worth-to-google](https://proton.me/blog/what-is-your-data-worth-to-google)

生成摘要时出错

---

## 76. Integrated by Design

**原文标题**: Integrated by Design

**原文链接**: [https://vivianvoss.net/blog/integrated-by-design-launch](https://vivianvoss.net/blog/integrated-by-design-launch)

生成摘要时出错

---

## 77. I bought Friendster for $30k – Here's what I'm doing with it

**原文标题**: I bought Friendster for $30k – Here's what I'm doing with it

**原文链接**: [https://ca98am79.medium.com/i-bought-friendster-for-30k-heres-what-i-m-doing-with-it-d5e8ddb3991d](https://ca98am79.medium.com/i-bought-friendster-for-30k-heres-what-i-m-doing-with-it-d5e8ddb3991d)

生成摘要时出错

---

## 78. Men who stare at walls

**原文标题**: Men who stare at walls

**原文链接**: [https://www.alexselimov.com/posts/men_who_stare_at_walls/](https://www.alexselimov.com/posts/men_who_stare_at_walls/)

生成摘要时出错

---

## 79. David Silver of DeepMind raises $1B to build AI that learns without human data

**原文标题**: David Silver of DeepMind raises $1B to build AI that learns without human data

**原文链接**: [https://techcrunch.com/2026/04/27/deepminds-david-silver-just-raised-1-1b-to-build-an-ai-that-learns-without-human-data/](https://techcrunch.com/2026/04/27/deepminds-david-silver-just-raised-1-1b-to-build-an-ai-that-learns-without-human-data/)

生成摘要时出错

---

## 80. The Secret Life of NaN (2018)

**原文标题**: The Secret Life of NaN (2018)

**原文链接**: [https://anniecherkaev.com/the-secret-life-of-nan](https://anniecherkaev.com/the-secret-life-of-nan)

生成摘要时出错

---

## 81. Lenovo buys Phoenix Technologies' firmware business

**原文标题**: Lenovo buys Phoenix Technologies' firmware business

**原文链接**: [https://news.lenovo.com/pressroom/press-releases/lenovo-completes-acquisition-of-phoenix-technologies-firmware-business/](https://news.lenovo.com/pressroom/press-releases/lenovo-completes-acquisition-of-phoenix-technologies-firmware-business/)

生成摘要时出错

---

## 82. US Supreme Court reviews police use of cell location data

**原文标题**: US Supreme Court reviews police use of cell location data

**原文链接**: [https://www.nytimes.com/2026/04/27/us/politics/supreme-court-cell-data-geofence.html](https://www.nytimes.com/2026/04/27/us/politics/supreme-court-cell-data-geofence.html)

生成摘要时出错

---

## 83. After 16 years and $8B the military's new GPS software still doesn't work

**原文标题**: After 16 years and $8B the military's new GPS software still doesn't work

**原文链接**: [https://arstechnica.com/space/2026/03/after-16-years-and-8-billion-the-militarys-new-gps-software-still-doesnt-work/](https://arstechnica.com/space/2026/03/after-16-years-and-8-billion-the-militarys-new-gps-software-still-doesnt-work/)

生成摘要时出错

---

## 84. The Social Edge of Intelligence: Individual Gain, Collective Loss

**原文标题**: The Social Edge of Intelligence: Individual Gain, Collective Loss

**原文链接**: [https://www.theideasletter.org/essay/the-social-edge-of-intelligence/](https://www.theideasletter.org/essay/the-social-edge-of-intelligence/)

生成摘要时出错

---

## 85. China blocks Meta's acquisition of AI startup Manus

**原文标题**: China blocks Meta's acquisition of AI startup Manus

**原文链接**: [https://www.cnbc.com/2026/04/27/meta-manus-china-blocks-acquisition-ai-startup.html](https://www.cnbc.com/2026/04/27/meta-manus-china-blocks-acquisition-ai-startup.html)

生成摘要时出错

---

## 86. Magic by return of post: How mail order delivered the occult

**原文标题**: Magic by return of post: How mail order delivered the occult

**原文链接**: [https://publicdomainreview.org/essay/magic-by-return-of-post/](https://publicdomainreview.org/essay/magic-by-return-of-post/)

生成摘要时出错

---

## 87. Show HN: Utilyze – an open source GPU monitoring tool more accurate than nvtop

**原文标题**: Show HN: Utilyze – an open source GPU monitoring tool more accurate than nvtop

**原文链接**: [https://www.systalyze.com/utilyze](https://www.systalyze.com/utilyze)

生成摘要时出错

---

## 88. Adding a team was the wrong strategic decision

**原文标题**: Adding a team was the wrong strategic decision

**原文链接**: [https://learnings.aleixmorgadas.dev/p/adding-a-team-was-the-wrong-strategic](https://learnings.aleixmorgadas.dev/p/adding-a-team-was-the-wrong-strategic)

生成摘要时出错

---

## 89. Fully Featured Audio DSP Firmware for the Raspberry Pi Pico

**原文标题**: Fully Featured Audio DSP Firmware for the Raspberry Pi Pico

**原文链接**: [https://github.com/WeebLabs/DSPi](https://github.com/WeebLabs/DSPi)

生成摘要时出错

---

## 90. Getting my daily news from a dot matrix printer 2024

**原文标题**: Getting my daily news from a dot matrix printer 2024

**原文链接**: [https://aschmelyun.com/blog/getting-my-daily-news-from-a-dot-matrix-printer/](https://aschmelyun.com/blog/getting-my-daily-news-from-a-dot-matrix-printer/)

生成摘要时出错

---

## 91. Flipdiscs

**原文标题**: Flipdiscs

**原文链接**: [https://flipdisc.io](https://flipdisc.io)

生成摘要时出错

---

## 92. Supreme Court to hear arguments in landmark Roundup weedkiller case

**原文标题**: Supreme Court to hear arguments in landmark Roundup weedkiller case

**原文链接**: [https://www.nytimes.com/2026/04/26/climate/supreme-court-bayer-monsanto-roundup-glyphosate.html](https://www.nytimes.com/2026/04/26/climate/supreme-court-bayer-monsanto-roundup-glyphosate.html)

生成摘要时出错

---

## 93. 7-Zip 26.01 Now Allows Making Use Of Huge Pages On Linux For Faster Compression

**原文标题**: 7-Zip 26.01 Now Allows Making Use Of Huge Pages On Linux For Faster Compression

**原文链接**: [https://www.phoronix.com/news/7-Zip-26.01](https://www.phoronix.com/news/7-Zip-26.01)

生成摘要时出错

---

## 94. Show HN: A terminal spreadsheet editor with Vim keybindings

**原文标题**: Show HN: A terminal spreadsheet editor with Vim keybindings

**原文链接**: [https://github.com/garritfra/cell](https://github.com/garritfra/cell)

生成摘要时出错

---

## 95. Den stora Älgvandringen – The great moose migration (live)

**原文标题**: Den stora Älgvandringen – The great moose migration (live)

**原文链接**: [https://www.svtplay.se/video/jXv3A5G/den-stora-algvandringen/idag-00-00](https://www.svtplay.se/video/jXv3A5G/den-stora-algvandringen/idag-00-00)

生成摘要时出错

---

## 96. AI should elevate your thinking, not replace it

**原文标题**: AI should elevate your thinking, not replace it

**原文链接**: [https://www.koshyjohn.com/blog/ai-should-elevate-your-thinking-not-replace-it/](https://www.koshyjohn.com/blog/ai-should-elevate-your-thinking-not-replace-it/)

生成摘要时出错

---

## 97. Pgbackrest is no longer being maintained

**原文标题**: Pgbackrest is no longer being maintained

**原文链接**: [https://github.com/pgbackrest/pgbackrest](https://github.com/pgbackrest/pgbackrest)

生成摘要时出错

---

## 98. Managing the Unmanaged Switch

**原文标题**: Managing the Unmanaged Switch

**原文链接**: [https://watchmysys.com/blog/2026/03/managing-the-unmanaged-switch/](https://watchmysys.com/blog/2026/03/managing-the-unmanaged-switch/)

生成摘要时出错

---

## 99. FDA approves first gene therapy for treatment of genetic hearing loss

**原文标题**: FDA approves first gene therapy for treatment of genetic hearing loss

**原文链接**: [https://www.fda.gov/news-events/press-announcements/fda-approves-first-ever-gene-therapy-treatment-genetic-hearing-loss-under-national-priority-voucher](https://www.fda.gov/news-events/press-announcements/fda-approves-first-ever-gene-therapy-treatment-genetic-hearing-loss-under-national-priority-voucher)

生成摘要时出错

---

## 100. AI vendor lock-in bites back

**原文标题**: AI vendor lock-in bites back

**原文链接**: [https://www.theregister.com/2026/04/28/locked_stocked_and_losing_budget/](https://www.theregister.com/2026/04/28/locked_stocked_and_losing_budget/)

生成摘要时出错

---

