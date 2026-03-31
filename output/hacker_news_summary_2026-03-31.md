# Hacker News 热门文章摘要 (2026-03-31)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. From 300KB to 69KB per Token: How LLM Architectures Solve the KV Cache Problem

**原文标题**: From 300KB to 69KB per Token: How LLM Architectures Solve the KV Cache Problem

**原文链接**: [https://news.future-shock.ai/the-weight-of-remembering/](https://news.future-shock.ai/the-weight-of-remembering/)

生成摘要时出错

---

## 12. 甲骨文裁员3万人

**原文标题**: Oracle slashes 30k jobs

**原文链接**: [https://rollingout.com/2026/03/31/oracle-slashes-30000-jobs-with-a-cold-6/](https://rollingout.com/2026/03/31/oracle-slashes-30000-jobs-with-a-cold-6/)

Unable to access the article link.

---

## 13. Combinators

**原文标题**: Combinators

**原文链接**: [https://tinyapl.rubenverg.com/docs/info/combinators](https://tinyapl.rubenverg.com/docs/info/combinators)

生成摘要时出错

---

## 14. Audio tapes reveal mass rule-breaking in Milgram's obedience experiments

**原文标题**: Audio tapes reveal mass rule-breaking in Milgram's obedience experiments

**原文链接**: [https://www.psypost.org/audio-tapes-reveal-mass-rule-breaking-in-milgram-s-obedience-experiments-2026-03-26/](https://www.psypost.org/audio-tapes-reveal-mass-rule-breaking-in-milgram-s-obedience-experiments-2026-03-26/)

生成摘要时出错

---

## 15. RubyGems Fracture Incident Report

**原文标题**: RubyGems Fracture Incident Report

**原文链接**: [https://rubycentral.org/news/rubygems-fracture-incident-report/](https://rubycentral.org/news/rubygems-fracture-incident-report/)

生成摘要时出错

---

## 16. Microsoft: Copilot is for entertainment purposes only

**原文标题**: Microsoft: Copilot is for entertainment purposes only

**原文链接**: [https://www.microsoft.com/en-us/microsoft-copilot/for-individuals/termsofuse](https://www.microsoft.com/en-us/microsoft-copilot/for-individuals/termsofuse)

生成摘要时出错

---

## 17. A Love Letter to 'Girl Games'

**原文标题**: A Love Letter to 'Girl Games'

**原文链接**: [https://aftermath.site/a-love-letter-to-girl-games/](https://aftermath.site/a-love-letter-to-girl-games/)

生成摘要时出错

---

## 18. Securing Elliptic Curve Cryptocurrencies Against Quantum Vulnerabilities [pdf]

**原文标题**: Securing Elliptic Curve Cryptocurrencies Against Quantum Vulnerabilities [pdf]

**原文链接**: [https://quantumai.google/static/site-assets/downloads/cryptocurrency-whitepaper.pdf](https://quantumai.google/static/site-assets/downloads/cryptocurrency-whitepaper.pdf)

生成摘要时出错

---

## 19. The Claude Code Source Leak: fake tools, frustration regexes, undercover mode

**原文标题**: The Claude Code Source Leak: fake tools, frustration regexes, undercover mode

**原文链接**: [https://alex000kim.com/posts/2026-03-31-claude-code-source-leak/](https://alex000kim.com/posts/2026-03-31-claude-code-source-leak/)

生成摘要时出错

---

## 20. What major works of literature were written after age of 85? 75? 65?

**原文标题**: What major works of literature were written after age of 85? 75? 65?

**原文链接**: [https://statmodeling.stat.columbia.edu/2026/03/25/what-major-works-of-literature-were-written-after-age-of-85-75-65/](https://statmodeling.stat.columbia.edu/2026/03/25/what-major-works-of-literature-were-written-after-age-of-85-75-65/)

生成摘要时出错

---

## 21. Claude Code users hitting usage limits 'way faster than expected'

**原文标题**: Claude Code users hitting usage limits 'way faster than expected'

**原文链接**: [https://www.theregister.com/2026/03/31/anthropic_claude_code_limits/](https://www.theregister.com/2026/03/31/anthropic_claude_code_limits/)

生成摘要时出错

---

## 22. Show HN: Loreline, narrative language transpiled via Haxe: C++/C#/JS/Java/Py/Lua

**原文标题**: Show HN: Loreline, narrative language transpiled via Haxe: C++/C#/JS/Java/Py/Lua

**原文链接**: [https://loreline.app/en/docs/technical-overview/](https://loreline.app/en/docs/technical-overview/)

生成摘要时出错

---

## 23. Multiple Sclerosis

**原文标题**: Multiple Sclerosis

**原文链接**: [https://subfictional.com/multiple-sclerosis/](https://subfictional.com/multiple-sclerosis/)

生成摘要时出错

---

## 24. Universal Claude.md – cut Claude output tokens

**原文标题**: Universal Claude.md – cut Claude output tokens

**原文链接**: [https://github.com/drona23/claude-token-efficient](https://github.com/drona23/claude-token-efficient)

生成摘要时出错

---

## 25. Google's 200M-parameter time-series foundation model with 16k context

**原文标题**: Google's 200M-parameter time-series foundation model with 16k context

**原文链接**: [https://github.com/google-research/timesfm](https://github.com/google-research/timesfm)

生成摘要时出错

---

## 26. Scotty: A beautiful SSH task runner

**原文标题**: Scotty: A beautiful SSH task runner

**原文链接**: [https://freek.dev/3064-scotty-a-beautiful-ssh-task-runner](https://freek.dev/3064-scotty-a-beautiful-ssh-task-runner)

生成摘要时出错

---

## 27. South Polar Times

**原文标题**: South Polar Times

**原文链接**: [https://www.laphamsquarterly.org/roundtable/south-polar-times](https://www.laphamsquarterly.org/roundtable/south-polar-times)

生成摘要时出错

---

## 28. Good CTE, Bad CTE

**原文标题**: Good CTE, Bad CTE

**原文链接**: [https://boringsql.com/posts/good-cte-bad-cte/](https://boringsql.com/posts/good-cte-bad-cte/)

生成摘要时出错

---

## 29. Good CTE, Bad CTE

**原文标题**: Good CTE, Bad CTE

**原文链接**: [https://boringsql.com/posts/good-cte-bad-cte/](https://boringsql.com/posts/good-cte-bad-cte/)

生成摘要时出错

---

## 30. Clojure: The Documentary, official trailer [video]

**原文标题**: Clojure: The Documentary, official trailer [video]

**原文链接**: [https://www.youtube.com/watch?v=JJEyffSdBsk](https://www.youtube.com/watch?v=JJEyffSdBsk)

生成摘要时出错

---

## 31. Forth VM and compiler written in C++ and Scryer Prolog

**原文标题**: Forth VM and compiler written in C++ and Scryer Prolog

**原文链接**: [https://github.com/no382001/forth-vm](https://github.com/no382001/forth-vm)

生成摘要时出错

---

## 32. GitHub backs down, kills Copilot pull-request ads after backlash

**原文标题**: GitHub backs down, kills Copilot pull-request ads after backlash

**原文链接**: [https://www.theregister.com/2026/03/30/github_copilot_ads_pull_requests/](https://www.theregister.com/2026/03/30/github_copilot_ads_pull_requests/)

生成摘要时出错

---

## 33. 7,655 Ransomware Claims in One Year: Group, Sector, and Country Breakdown

**原文标题**: 7,655 Ransomware Claims in One Year: Group, Sector, and Country Breakdown

**原文链接**: [https://ciphercue.com/blog/7655-ransomware-claims-march-2025-to-march-2026](https://ciphercue.com/blog/7655-ransomware-claims-march-2025-to-march-2026)

生成摘要时出错

---

## 34. Show HN: Hyprmoncfg – Terminal-based monitor config manager for Hyprland

**原文标题**: Show HN: Hyprmoncfg – Terminal-based monitor config manager for Hyprland

**原文链接**: [https://paolino.me/hyprmoncfg-monitor-configuration-for-hyprland/](https://paolino.me/hyprmoncfg-monitor-configuration-for-hyprland/)

生成摘要时出错

---

## 35. Raspberry Pi profit surges as AI boom lifts demand

**原文标题**: Raspberry Pi profit surges as AI boom lifts demand

**原文链接**: [https://www.ft.com/content/5c167591-80bb-4290-ae66-7d04112cbd1c](https://www.ft.com/content/5c167591-80bb-4290-ae66-7d04112cbd1c)

生成摘要时出错

---

## 36. Project Mario: the inside story of DeepMind

**原文标题**: Project Mario: the inside story of DeepMind

**原文链接**: [https://colossus.com/article/project-mario-demis-hassabis-deepmind-mallaby/](https://colossus.com/article/project-mario-demis-hassabis-deepmind-mallaby/)

生成摘要时出错

---

## 37. Turning a MacBook into a touchscreen with $1 of hardware (2018)

**原文标题**: Turning a MacBook into a touchscreen with $1 of hardware (2018)

**原文链接**: [https://anishathalye.com/macbook-touchscreen/](https://anishathalye.com/macbook-touchscreen/)

生成摘要时出错

---

## 38. Android Developer Verification

**原文标题**: Android Developer Verification

**原文链接**: [https://android-developers.googleblog.com/2026/03/android-developer-verification-rolling-out-to-all-developers.html](https://android-developers.googleblog.com/2026/03/android-developer-verification-rolling-out-to-all-developers.html)

生成摘要时出错

---

## 39. We're pausing Asimov Press

**原文标题**: We're pausing Asimov Press

**原文链接**: [https://www.asimov.press/p/pause](https://www.asimov.press/p/pause)

生成摘要时出错

---

## 40. Acceptance of entomophagy among Canadians at an insectarium

**原文标题**: Acceptance of entomophagy among Canadians at an insectarium

**原文链接**: [https://www.nature.com/articles/s41598-026-35288-w](https://www.nature.com/articles/s41598-026-35288-w)

生成摘要时出错

---

## 41. In Expanding de Sitter Space, Quantum Mechanics Gets More Elusive

**原文标题**: In Expanding de Sitter Space, Quantum Mechanics Gets More Elusive

**原文链接**: [https://www.quantamagazine.org/in-expanding-de-sitter-space-quantum-mechanics-gets-even-more-elusive-20260330/](https://www.quantamagazine.org/in-expanding-de-sitter-space-quantum-mechanics-gets-even-more-elusive-20260330/)

生成摘要时出错

---

## 42. 30 Years Ago, Robots Learned to Walk Without Falling

**原文标题**: 30 Years Ago, Robots Learned to Walk Without Falling

**原文链接**: [https://spectrum.ieee.org/honda-p2-robot-ieee-milestone](https://spectrum.ieee.org/honda-p2-robot-ieee-milestone)

生成摘要时出错

---

## 43. Fedware: Government apps that spy harder than the apps they ban

**原文标题**: Fedware: Government apps that spy harder than the apps they ban

**原文链接**: [https://www.sambent.com/the-white-house-app-has-huawei-spyware-and-an-ice-tip-line/](https://www.sambent.com/the-white-house-app-has-huawei-spyware-and-an-ice-tip-line/)

生成摘要时出错

---

## 44. Someone just converted Claude Leark from TypeScript to 100% Python

**原文标题**: Someone just converted Claude Leark from TypeScript to 100% Python

**原文链接**: [https://github.com/instructkr/claw-code](https://github.com/instructkr/claw-code)

生成摘要时出错

---

## 45. Show HN: Sundial – a new way to look at a weather forecast

**原文标题**: Show HN: Sundial – a new way to look at a weather forecast

**原文链接**: [https://sundial.page/](https://sundial.page/)

生成摘要时出错

---

## 46. OpenGridWorks: The Electricity Infrasctructure, Mapped

**原文标题**: OpenGridWorks: The Electricity Infrasctructure, Mapped

**原文链接**: [https://www.opengridworks.com](https://www.opengridworks.com)

生成摘要时出错

---

## 47. Vulnerability research is cooked

**原文标题**: Vulnerability research is cooked

**原文链接**: [https://sockpuppet.org/blog/2026/03/30/vulnerability-research-is-cooked/](https://sockpuppet.org/blog/2026/03/30/vulnerability-research-is-cooked/)

生成摘要时出错

---

## 48. CodingFont: A game to help you pick a coding font

**原文标题**: CodingFont: A game to help you pick a coding font

**原文链接**: [https://www.codingfont.com/](https://www.codingfont.com/)

生成摘要时出错

---

## 49. Do your own writing

**原文标题**: Do your own writing

**原文链接**: [https://alexhwoods.com/dont-let-ai-write-for-you/](https://alexhwoods.com/dont-let-ai-write-for-you/)

生成摘要时出错

---

## 50. Cherri – programming language that compiles to an Apple Shortuct

**原文标题**: Cherri – programming language that compiles to an Apple Shortuct

**原文链接**: [https://github.com/electrikmilk/cherri](https://github.com/electrikmilk/cherri)

生成摘要时出错

---

## 51. Italy blocks US use of Sicily air base for Middle East war

**原文标题**: Italy blocks US use of Sicily air base for Middle East war

**原文链接**: [https://www.politico.eu/article/italy-blocks-us-use-of-sicily-air-base/](https://www.politico.eu/article/italy-blocks-us-use-of-sicily-air-base/)

生成摘要时出错

---

## 52. I'm betting on ATProto

**原文标题**: I'm betting on ATProto

**原文链接**: [https://brittanyellich.com/atproto/](https://brittanyellich.com/atproto/)

生成摘要时出错

---

## 53. Mr. Chatterbox is a Victorian-era ethically trained model

**原文标题**: Mr. Chatterbox is a Victorian-era ethically trained model

**原文链接**: [https://simonwillison.net/2026/Mar/30/mr-chatterbox/](https://simonwillison.net/2026/Mar/30/mr-chatterbox/)

生成摘要时出错

---

## 54. Agents of Chaos

**原文标题**: Agents of Chaos

**原文链接**: [https://agentsofchaos.baulab.info/report.html](https://agentsofchaos.baulab.info/report.html)

生成摘要时出错

---

## 55. TSMC is reportedly sold out until 2028

**原文标题**: TSMC is reportedly sold out until 2028

**原文链接**: [https://www.pcgamer.com/hardware/tsmc-is-reportedly-sold-out-until-2028-and-even-its-next-gen-arizona-fab-is-fully-booked-before-it-has-even-been-built/](https://www.pcgamer.com/hardware/tsmc-is-reportedly-sold-out-until-2028-and-even-its-next-gen-arizona-fab-is-fully-booked-before-it-has-even-been-built/)

生成摘要时出错

---

## 56. Car Seats as Contraception

**原文标题**: Car Seats as Contraception

**原文链接**: [https://www.journals.uchicago.edu/doi/abs/10.1086/731812](https://www.journals.uchicago.edu/doi/abs/10.1086/731812)

生成摘要时出错

---

## 57. Oscar Reutersvärd (2021)

**原文标题**: Oscar Reutersvärd (2021)

**原文链接**: [https://escherinhetpaleis.nl/en/about-escher/escher-today/oscar-reutersvard](https://escherinhetpaleis.nl/en/about-escher/escher-today/oscar-reutersvard)

生成摘要时出错

---

## 58. Show HN: I turned a sketch into a 3D-print pegboard for my kid with an AI agent

**原文标题**: Show HN: I turned a sketch into a 3D-print pegboard for my kid with an AI agent

**原文链接**: [https://github.com/virpo/pegboard](https://github.com/virpo/pegboard)

生成摘要时出错

---

## 59. Meta, Snapchat, TikTok, YouTube aren't complying with U16 ban, Australia says

**原文标题**: Meta, Snapchat, TikTok, YouTube aren't complying with U16 ban, Australia says

**原文链接**: [https://apnews.com/article/australia-social-media-ban-children-58c50c845d96057b39529e988bd778bc](https://apnews.com/article/australia-social-media-ban-children-58c50c845d96057b39529e988bd778bc)

生成摘要时出错

---

## 60. How to turn anything into a router

**原文标题**: How to turn anything into a router

**原文链接**: [https://nbailey.ca/post/router/](https://nbailey.ca/post/router/)

生成摘要时出错

---

## 61. Researchers find 3,500-year-old loom that reveals textile revolution

**原文标题**: Researchers find 3,500-year-old loom that reveals textile revolution

**原文链接**: [https://web.ua.es/en/actualidad-universitaria/2026/marzo2026/23-31/ua-researchers-find-3-500-year-old-loom-that-reveals-key-aspects-of-textile-revolution-in-the-bronze-age.html](https://web.ua.es/en/actualidad-universitaria/2026/marzo2026/23-31/ua-researchers-find-3-500-year-old-loom-that-reveals-key-aspects-of-textile-revolution-in-the-bronze-age.html)

生成摘要时出错

---

## 62. Incident March 30th, 2026 – Accidental CDN Caching

**原文标题**: Incident March 30th, 2026 – Accidental CDN Caching

**原文链接**: [https://blog.railway.com/p/incident-report-march-30-2026-accidental-cdn-caching](https://blog.railway.com/p/incident-report-march-30-2026-accidental-cdn-caching)

生成摘要时出错

---

## 63. Prerelease of Ky 2.0

**原文标题**: Prerelease of Ky 2.0

**原文链接**: [https://github.com/sindresorhus/ky/releases/tag/v2.0.0-0](https://github.com/sindresorhus/ky/releases/tag/v2.0.0-0)

生成摘要时出错

---

## 64. Why some American accents have endured – while others have faded away

**原文标题**: Why some American accents have endured – while others have faded away

**原文链接**: [https://www.vox.com/explain-it-to-me/483964/american-accent-history-identity-southern-new-england-language](https://www.vox.com/explain-it-to-me/483964/american-accent-history-identity-southern-new-england-language)

生成摘要时出错

---

## 65. Show HN: Pardus Browser- a browser for AI agents without Chromium

**原文标题**: Show HN: Pardus Browser- a browser for AI agents without Chromium

**原文链接**: [https://github.com/JasonHonKL/PardusBrowser/tree/main](https://github.com/JasonHonKL/PardusBrowser/tree/main)

生成摘要时出错

---

## 66. Unit: A self-replicating Forth mesh agent running in a browser tab

**原文标题**: Unit: A self-replicating Forth mesh agent running in a browser tab

**原文链接**: [https://davidcanhelp.github.io/unit/](https://davidcanhelp.github.io/unit/)

生成摘要时出错

---

## 67. President's new science council: 9 billionaires and 1 scientist

**原文标题**: President's new science council: 9 billionaires and 1 scientist

**原文链接**: [https://www.scientificamerican.com/article/trumps-new-science-panel-includes-9-tech-billionaires-and-just-one-scientist/](https://www.scientificamerican.com/article/trumps-new-science-panel-includes-9-tech-billionaires-and-just-one-scientist/)

生成摘要时出错

---

## 68. Seeing like a spreadsheet

**原文标题**: Seeing like a spreadsheet

**原文链接**: [https://davidoks.blog/p/how-the-spreadsheet-reshaped-america](https://davidoks.blog/p/how-the-spreadsheet-reshaped-america)

生成摘要时出错

---

## 69. Mathematical methods and human thought in the age of AI

**原文标题**: Mathematical methods and human thought in the age of AI

**原文链接**: [https://arxiv.org/abs/2603.26524](https://arxiv.org/abs/2603.26524)

生成摘要时出错

---

## 70. In math, rigor is vital, but are digitized proofs taking it too far?

**原文标题**: In math, rigor is vital, but are digitized proofs taking it too far?

**原文链接**: [https://www.quantamagazine.org/in-math-rigor-is-vital-but-are-digitized-proofs-taking-it-too-far-20260325/](https://www.quantamagazine.org/in-math-rigor-is-vital-but-are-digitized-proofs-taking-it-too-far-20260325/)

生成摘要时出错

---

## 71. JetBrains Guide Shutdown

**原文标题**: JetBrains Guide Shutdown

**原文链接**: [https://www.jetbrains.com/guide/shutdown/](https://www.jetbrains.com/guide/shutdown/)

生成摘要时出错

---

## 72. Recover Apple Keychain

**原文标题**: Recover Apple Keychain

**原文链接**: [https://arkoinad.com/posts/apple_keychain_recovery.html](https://arkoinad.com/posts/apple_keychain_recovery.html)

生成摘要时出错

---

## 73. R3 Bio pitched “brainless clones” to serve the role of backup human bodies

**原文标题**: R3 Bio pitched “brainless clones” to serve the role of backup human bodies

**原文链接**: [https://www.technologyreview.com/2026/03/30/1134780/r3-bio-brainless-human-clones-full-body-replacement-john-schloendorn-aging-longevity/](https://www.technologyreview.com/2026/03/30/1134780/r3-bio-brainless-human-clones-full-body-replacement-john-schloendorn-aging-longevity/)

生成摘要时出错

---

## 74. Show HN: Coasts – Containerized Hosts for Agents

**原文标题**: Show HN: Coasts – Containerized Hosts for Agents

**原文链接**: [https://github.com/coast-guard/coasts](https://github.com/coast-guard/coasts)

生成摘要时出错

---

## 75. One of the largest salt mines in the world exists under Lake Erie

**原文标题**: One of the largest salt mines in the world exists under Lake Erie

**原文链接**: [https://apnews.com/article/cleveland-salt-mine-winter-road-0daf091e3d56f65766bcf6a597683893](https://apnews.com/article/cleveland-salt-mine-winter-road-0daf091e3d56f65766bcf6a597683893)

生成摘要时出错

---

## 76. Build123d: A Python CAD programming library

**原文标题**: Build123d: A Python CAD programming library

**原文链接**: [https://github.com/gumyr/build123d](https://github.com/gumyr/build123d)

生成摘要时出错

---

## 77. AI data centres can warm surrounding areas by up to 9.1°C

**原文标题**: AI data centres can warm surrounding areas by up to 9.1°C

**原文链接**: [https://www.newscientist.com/article/2521256-ai-data-centres-can-warm-surrounding-areas-by-up-to-9-1c/](https://www.newscientist.com/article/2521256-ai-data-centres-can-warm-surrounding-areas-by-up-to-9-1c/)

生成摘要时出错

---

## 78. William Blake, Remote by the Sea

**原文标题**: William Blake, Remote by the Sea

**原文链接**: [https://www.laphamsquarterly.org/roundtable/william-blake-remote-sea](https://www.laphamsquarterly.org/roundtable/william-blake-remote-sea)

生成摘要时出错

---

## 79. Learn Claude Code by doing, not reading

**原文标题**: Learn Claude Code by doing, not reading

**原文链接**: [https://claude.nagdy.me/](https://claude.nagdy.me/)

生成摘要时出错

---

## 80. IRGC threatens imminent strikes on US tech giants across the Middle East

**原文标题**: IRGC threatens imminent strikes on US tech giants across the Middle East

**原文链接**: [https://www.i24news.tv/en/news/middle-east/iran-eastern-states/artc-irgc-threatens-strikes-on-us-tech-giants-across-the-middle-east](https://www.i24news.tv/en/news/middle-east/iran-eastern-states/artc-irgc-threatens-strikes-on-us-tech-giants-across-the-middle-east)

生成摘要时出错

---

## 81. ChatGPT won't let you type until Cloudflare reads your React state

**原文标题**: ChatGPT won't let you type until Cloudflare reads your React state

**原文链接**: [https://www.buchodi.com/chatgpt-wont-let-you-type-until-cloudflare-reads-your-react-state-i-decrypted-the-program-that-does-it/](https://www.buchodi.com/chatgpt-wont-let-you-type-until-cloudflare-reads-your-react-state-i-decrypted-the-program-that-does-it/)

生成摘要时出错

---

## 82. Bird brains (2023)

**原文标题**: Bird brains (2023)

**原文链接**: [https://www.dhanishsemar.com/writing/bird-brains](https://www.dhanishsemar.com/writing/bird-brains)

生成摘要时出错

---

## 83. Hamilton-Jacobi-Bellman Equation: Reinforcement Learning and Diffusion Models

**原文标题**: Hamilton-Jacobi-Bellman Equation: Reinforcement Learning and Diffusion Models

**原文链接**: [https://dani2442.github.io/posts/continuous-rl/](https://dani2442.github.io/posts/continuous-rl/)

生成摘要时出错

---

## 84. Copilot edited an ad into my PR

**原文标题**: Copilot edited an ad into my PR

**原文链接**: [https://notes.zachmanson.com/copilot-edited-an-ad-into-my-pr/](https://notes.zachmanson.com/copilot-edited-an-ad-into-my-pr/)

The author describes an incident where GitHub Copilot inserted an advertisement for itself and Raycast into a Pull Request (PR) description after being summoned to fix a minor typo. 

Expressing outrage at this intrusive behavior, the author frames the incident as a sign of platform decay. They reference Cory Doctorow’s theory of "enshittification," outlining a three-stage lifecycle for digital platforms:
1. Being helpful to users to build a base.
2. Exploiting users to benefit business customers.
3. Exploiting business customers to maximize value for the platform itself.

The author concludes that by injecting ads into functional developer workflows, the platform has entered a stage of user abuse that inevitably leads to its decline and eventual death.

---

## 85. A sea of sparks: Seeing radioactivity

**原文标题**: A sea of sparks: Seeing radioactivity

**原文链接**: [https://maurycyz.com/projects/spinthariscope/](https://maurycyz.com/projects/spinthariscope/)

生成摘要时出错

---

## 86. Sony halts memory card shipments due to NAND shortage

**原文标题**: Sony halts memory card shipments due to NAND shortage

**原文链接**: [https://www.techzine.eu/news/devices/140058/sony-halts-memory-card-shipments-due-to-nand-shortage/](https://www.techzine.eu/news/devices/140058/sony-halts-memory-card-shipments-due-to-nand-shortage/)

生成摘要时出错

---

## 87. What we learned building 100 API integrations with OpenCode

**原文标题**: What we learned building 100 API integrations with OpenCode

**原文链接**: [https://nango.dev/blog/learned-building-200-api-integrations-with-opencode/](https://nango.dev/blog/learned-building-200-api-integrations-with-opencode/)

生成摘要时出错

---

## 88. Every Time Zone

**原文标题**: Every Time Zone

**原文链接**: [https://everytimezone.com/](https://everytimezone.com/)

生成摘要时出错

---

## 89. The ladder is missing rungs – Engineering Progression When AI Ate the Middle

**原文标题**: The ladder is missing rungs – Engineering Progression When AI Ate the Middle

**原文链接**: [https://negroniventurestudios.com/2026/03/19/the-ladder-is-missing-rungs/](https://negroniventurestudios.com/2026/03/19/the-ladder-is-missing-rungs/)

生成摘要时出错

---

## 90. VHDL's Crown Jewel

**原文标题**: VHDL's Crown Jewel

**原文链接**: [https://www.sigasi.com/opinion/jan/vhdls-crown-jewel/](https://www.sigasi.com/opinion/jan/vhdls-crown-jewel/)

生成摘要时出错

---

## 91. FTC action against Match and OkCupid for deceiving users, sharing personal data

**原文标题**: FTC action against Match and OkCupid for deceiving users, sharing personal data

**原文链接**: [https://www.ftc.gov/news-events/news/press-releases/2026/03/ftc-takes-action-against-match-okcupid-deceiving-users-sharing-personal-data-third-party](https://www.ftc.gov/news-events/news/press-releases/2026/03/ftc-takes-action-against-match-okcupid-deceiving-users-sharing-personal-data-third-party)

生成摘要时出错

---

## 92. My MacBook keyboard is broken and it's insanely expensive to fix

**原文标题**: My MacBook keyboard is broken and it's insanely expensive to fix

**原文链接**: [https://tobiasberg.net/posts/my-macbook-keyboard-is-broken-and-its-insanely-expensive-to-fix/](https://tobiasberg.net/posts/my-macbook-keyboard-is-broken-and-its-insanely-expensive-to-fix/)

生成摘要时出错

---

## 93. I am definitely missing the pre-AI writing era

**原文标题**: I am definitely missing the pre-AI writing era

**原文链接**: [https://www.lesswrong.com/posts/BJ4pnropWdnzzgeJc/i-am-definitely-missing-the-pre-ai-writing-era](https://www.lesswrong.com/posts/BJ4pnropWdnzzgeJc/i-am-definitely-missing-the-pre-ai-writing-era)

生成摘要时出错

---

## 94. From Proxmox to FreeBSD and Sylve in our office lab

**原文标题**: From Proxmox to FreeBSD and Sylve in our office lab

**原文链接**: [https://www.iptechnics.com/blogs/from-proxmox-to-freebsd-and-sylve-in-our-office-lab](https://www.iptechnics.com/blogs/from-proxmox-to-freebsd-and-sylve-in-our-office-lab)

生成摘要时出错

---

## 95. Take better notes, by hand

**原文标题**: Take better notes, by hand

**原文链接**: [https://brianschrader.com/archive/take-better-notes-by-hand/](https://brianschrader.com/archive/take-better-notes-by-hand/)

生成摘要时出错

---

## 96. Rock Star: Reading the Rosetta Stone

**原文标题**: Rock Star: Reading the Rosetta Stone

**原文链接**: [https://www.historytoday.com/archive/feature/original-rock-star](https://www.historytoday.com/archive/feature/original-rock-star)

生成摘要时出错

---

## 97. Prediction: The Shopify CEO's Pull Request Will Never Be Merged nor Closed

**原文标题**: Prediction: The Shopify CEO's Pull Request Will Never Be Merged nor Closed

**原文链接**: [https://joshmoody.org/blog/shopify-ceo-autoresearch-pr/](https://joshmoody.org/blog/shopify-ceo-autoresearch-pr/)

生成摘要时出错

---

## 98. Voyager 1 runs on 69 KB of memory and an 8-track tape recorder

**原文标题**: Voyager 1 runs on 69 KB of memory and an 8-track tape recorder

**原文链接**: [https://techfixated.com/a-1977-time-capsule-voyager-1-runs-on-69-kb-of-memory-and-an-8-track-tape-recorder-4/](https://techfixated.com/a-1977-time-capsule-voyager-1-runs-on-69-kb-of-memory-and-an-8-track-tape-recorder-4/)

生成摘要时出错

---

## 99. Roulette Computers: Hidden Devices That Predict Spins

**原文标题**: Roulette Computers: Hidden Devices That Predict Spins

**原文链接**: [https://www.roulette-computers.com/](https://www.roulette-computers.com/)

生成摘要时出错

---

## 100. Entirety of Wikinews to be shut down

**原文标题**: Entirety of Wikinews to be shut down

**原文链接**: [https://en.wikipedia.org/wiki/Wikipedia:Wikipedia_Signpost/2026-03-31/News_and_notes](https://en.wikipedia.org/wiki/Wikipedia:Wikipedia_Signpost/2026-03-31/News_and_notes)

生成摘要时出错

---

