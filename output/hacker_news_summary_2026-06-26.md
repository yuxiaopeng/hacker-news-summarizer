# Hacker News 热门文章摘要 (2026-06-26)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. What is a Lithium-ion capacitor?

**原文标题**: What is a Lithium-ion capacitor?

**原文链接**: [https://www.jtekt.co.jp/e/products/capacitor/capacitor_about.html](https://www.jtekt.co.jp/e/products/capacitor/capacitor_about.html)

生成摘要时出错

---

## 12. What Is a Nomogram and Why Would It Interest Me?

**原文标题**: What Is a Nomogram and Why Would It Interest Me?

**原文链接**: [https://lefakkomies.github.io/pynomo-doc/introduction/introduction.html#what-is-a-nomogram-and-why-would-it-interest-me](https://lefakkomies.github.io/pynomo-doc/introduction/introduction.html#what-is-a-nomogram-and-why-would-it-interest-me)

生成摘要时出错

---

## 13. 'Cost Me the Election': Data Centers Trigger Voter Backlash

**原文标题**: 'Cost Me the Election': Data Centers Trigger Voter Backlash

**原文链接**: [https://www.newsweek.com/cost-me-the-election-data-centers-trigger-voter-backlash-12118327](https://www.newsweek.com/cost-me-the-election-data-centers-trigger-voter-backlash-12118327)

生成摘要时出错

---

## 14. Libre Barcode Project

**原文标题**: Libre Barcode Project

**原文链接**: [https://graphicore.github.io/librebarcode/](https://graphicore.github.io/librebarcode/)

生成摘要时出错

---

## 15. Incident CVE-2026-LGTM

**原文标题**: Incident CVE-2026-LGTM

**原文链接**: [https://nesbitt.io/2026/06/26/incident-report-cve-2026-lgtm.html](https://nesbitt.io/2026/06/26/incident-report-cve-2026-lgtm.html)

生成摘要时出错

---

## 16. 22-year-old Mozart's handwritten notebook unearthed in 'major discovery'

**原文标题**: 22-year-old Mozart's handwritten notebook unearthed in 'major discovery'

**原文链接**: [https://www.classicfm.com/composers/mozart/handwritten-notebook-discovered-major-paris/](https://www.classicfm.com/composers/mozart/handwritten-notebook-discovered-major-paris/)

生成摘要时出错

---

## 17. What happened after 2k people tried to hack my AI assistant

**原文标题**: What happened after 2k people tried to hack my AI assistant

**原文链接**: [https://www.fernandoi.cl/posts/hackmyclaw/](https://www.fernandoi.cl/posts/hackmyclaw/)

生成摘要时出错

---

## 18. Framework's 10G Ethernet module exposes USB-C's complexity

**原文标题**: Framework's 10G Ethernet module exposes USB-C's complexity

**原文链接**: [https://www.jeffgeerling.com/blog/2026/framework-10g-ethernet-module-usb-c-complexity/](https://www.jeffgeerling.com/blog/2026/framework-10g-ethernet-module-usb-c-complexity/)

生成摘要时出错

---

## 19. A US military exercise to launch a satellite on short notice

**原文标题**: A US military exercise to launch a satellite on short notice

**原文链接**: [https://arstechnica.com/space/2026/06/a-us-military-exercise-in-space-got-underway-with-barely-anyone-noticing/](https://arstechnica.com/space/2026/06/a-us-military-exercise-in-space-got-underway-with-barely-anyone-noticing/)

生成摘要时出错

---

## 20. LaTeX.wasm: LaTeX Engines in Browsers

**原文标题**: LaTeX.wasm: LaTeX Engines in Browsers

**原文链接**: [https://www.swiftlatex.com/](https://www.swiftlatex.com/)

生成摘要时出错

---

## 21. Bipartite Matching Is in NC

**原文标题**: Bipartite Matching Is in NC

**原文链接**: [https://scottaaronson.blog/?p=9851](https://scottaaronson.blog/?p=9851)

生成摘要时出错

---

## 22. Show HN: WebBase-III – dBASE III rebuilt in the browser with its own interpreter

**原文标题**: Show HN: WebBase-III – dBASE III rebuilt in the browser with its own interpreter

**原文链接**: [https://github.com/DDecoene/WebBaseIII](https://github.com/DDecoene/WebBaseIII)

生成摘要时出错

---

## 23. Jolla Phone (October 2026)

**原文标题**: Jolla Phone (October 2026)

**原文链接**: [https://commerce.jolla.com/products/jolla-phone-october-2026](https://commerce.jolla.com/products/jolla-phone-october-2026)

生成摘要时出错

---

## 24. A game where you're an OS and have to manage processes, memory and I/O events

**原文标题**: A game where you're an OS and have to manage processes, memory and I/O events

**原文链接**: [https://github.com/plbrault/youre-the-os](https://github.com/plbrault/youre-the-os)

生成摘要时出错

---

## 25. The 'papers, please' era of the internet will decimate your privacy

**原文标题**: The 'papers, please' era of the internet will decimate your privacy

**原文链接**: [https://expression.fire.org/p/the-papers-please-era-of-the-internet](https://expression.fire.org/p/the-papers-please-era-of-the-internet)

生成摘要时出错

---

## 26. The Garbage Collection Handbook: The Art of Automatic Memory Management (2nd Ed) (2023)

**原文标题**: The Garbage Collection Handbook: The Art of Automatic Memory Management (2nd Ed) (2023)

**原文链接**: [https://gchandbook.org/](https://gchandbook.org/)

生成摘要时出错

---

## 27. Oxide computer 3D rack guided tour

**原文标题**: Oxide computer 3D rack guided tour

**原文链接**: [https://explorer.oxide.computer/](https://explorer.oxide.computer/)

生成摘要时出错

---

## 28. We all depend on open source. We will defend it together

**原文标题**: We all depend on open source. We will defend it together

**原文链接**: [https://akrites.org/letter/](https://akrites.org/letter/)

生成摘要时出错

---

## 29. FEXPRs vs. vtable: how LispE interpreter works

**原文标题**: FEXPRs vs. vtable: how LispE interpreter works

**原文链接**: [https://github.com/naver/lispe/wiki/2.7-FEXPR-vs.-vtable](https://github.com/naver/lispe/wiki/2.7-FEXPR-vs.-vtable)

生成摘要时出错

---

## 30. IBM debuts sub-1 nanometer chip technology

**原文标题**: IBM debuts sub-1 nanometer chip technology

**原文链接**: [https://newsroom.ibm.com/2026-06-25-ibm-debuts-worlds-first-sub-1-nanometer-chip-technology](https://newsroom.ibm.com/2026-06-25-ibm-debuts-worlds-first-sub-1-nanometer-chip-technology)

生成摘要时出错

---

## 31. Show HN: Chess-Inspired Roguelike

**原文标题**: Show HN: Chess-Inspired Roguelike

**原文链接**: [https://princechazz.com](https://princechazz.com)

生成摘要时出错

---

## 32. Show HN: OpenKnowledge – open source AI-first alternative to Obsidian/Notion

**原文标题**: Show HN: OpenKnowledge – open source AI-first alternative to Obsidian/Notion

**原文链接**: [https://github.com/inkeep/open-knowledge](https://github.com/inkeep/open-knowledge)

生成摘要时出错

---

## 33. Un-0: Generating Images with Coupled Oscillators

**原文标题**: Un-0: Generating Images with Coupled Oscillators

**原文链接**: [https://unconv.ai/blog/introducing-un-0-generating-images-with-coupled-oscillators/](https://unconv.ai/blog/introducing-un-0-generating-images-with-coupled-oscillators/)

生成摘要时出错

---

## 34. I'm building a Space Cadet Pinball Machine! [video]

**原文标题**: I'm building a Space Cadet Pinball Machine! [video]

**原文链接**: [https://www.youtube.com/watch?v=lHQ8c8i42VE](https://www.youtube.com/watch?v=lHQ8c8i42VE)

生成摘要时出错

---

## 35. The Doorman's Fallacy in action

**原文标题**: The Doorman's Fallacy in action

**原文链接**: [https://rozumem.xyz/posts/17](https://rozumem.xyz/posts/17)

生成摘要时出错

---

## 36. OpenAI leans toward waiting until next year for IPO

**原文标题**: OpenAI leans toward waiting until next year for IPO

**原文链接**: [https://www.nytimes.com/2026/06/25/technology/openai-ipo-artificial-intelligence.html](https://www.nytimes.com/2026/06/25/technology/openai-ipo-artificial-intelligence.html)

生成摘要时出错

---

## 37. Apple raises prices of MacBooks, iPads

**原文标题**: Apple raises prices of MacBooks, iPads

**原文链接**: [https://www.reuters.com/world/asia-pacific/apple-raises-prices-macbooks-ipads-memory-costs-skyrocket-2026-06-25/](https://www.reuters.com/world/asia-pacific/apple-raises-prices-macbooks-ipads-memory-costs-skyrocket-2026-06-25/)

生成摘要时出错

---

## 38. Zig's new bitCast semantics and LLVM back end improvements

**原文标题**: Zig's new bitCast semantics and LLVM back end improvements

**原文链接**: [https://ziglang.org/devlog/2026/#2026-06-25](https://ziglang.org/devlog/2026/#2026-06-25)

生成摘要时出错

---

## 39. Microbubbles in Medicine

**原文标题**: Microbubbles in Medicine

**原文链接**: [https://worksinprogress.co/issue/microbubbles/](https://worksinprogress.co/issue/microbubbles/)

生成摘要时出错

---

## 40. OS9Map

**原文标题**: OS9Map

**原文链接**: [https://yllan.org/software/OS9Map/](https://yllan.org/software/OS9Map/)

生成摘要时出错

---

## 41. An oral history of Bank Python (2021)

**原文标题**: An oral history of Bank Python (2021)

**原文链接**: [https://calpaterson.com/bank-python.html](https://calpaterson.com/bank-python.html)

生成摘要时出错

---

## 42. The last Romans are still around

**原文标题**: The last Romans are still around

**原文链接**: [https://signoregalilei.com/2026/06/20/the-last-romans-are-still-around/](https://signoregalilei.com/2026/06/20/the-last-romans-are-still-around/)

生成摘要时出错

---

## 43. You can't unit test for taste

**原文标题**: You can't unit test for taste

**原文链接**: [https://dev.karltryggvason.com/you-cant-unit-test-for-taste/](https://dev.karltryggvason.com/you-cant-unit-test-for-taste/)

生成摘要时出错

---

## 44. Record type inference for dummies

**原文标题**: Record type inference for dummies

**原文链接**: [http://haskellforall.com/2026/06/record-type-inference-for-dummies](http://haskellforall.com/2026/06/record-type-inference-for-dummies)

生成摘要时出错

---

## 45. The disappearance of Japan's animators

**原文标题**: The disappearance of Japan's animators

**原文链接**: [https://economist.com/interactive/1843/2026/06/19/the-strange-disappearance-of-japans-animators](https://economist.com/interactive/1843/2026/06/19/the-strange-disappearance-of-japans-animators)

生成摘要时出错

---

## 46. Parallel Parentheses Matching

**原文标题**: Parallel Parentheses Matching

**原文链接**: [https://williamdue.github.io/blog/parallel-parentheses-matching](https://williamdue.github.io/blog/parallel-parentheses-matching)

生成摘要时出错

---

## 47. The unbearable cheapness of open weight models

**原文标题**: The unbearable cheapness of open weight models

**原文链接**: [https://jamesoclaire.com/2026/06/25/the-unbearable-cheapness-of-open-weight-models/](https://jamesoclaire.com/2026/06/25/the-unbearable-cheapness-of-open-weight-models/)

生成摘要时出错

---

## 48. Political bias in AI: Where the AI models stand

**原文标题**: Political bias in AI: Where the AI models stand

**原文链接**: [https://trakkr.ai/bias](https://trakkr.ai/bias)

生成摘要时出错

---

## 49. GloriousEggroll's Proton has been rebased on Proton 11

**原文标题**: GloriousEggroll's Proton has been rebased on Proton 11

**原文链接**: [https://github.com/GloriousEggroll/proton-ge-custom/releases/tag/GE-Proton11-1](https://github.com/GloriousEggroll/proton-ge-custom/releases/tag/GE-Proton11-1)

生成摘要时出错

---

## 50. The White House is asking OpenAI to slow roll the release of its new model

**原文标题**: The White House is asking OpenAI to slow roll the release of its new model

**原文链接**: [https://techcrunch.com/2026/06/25/the-white-house-is-asking-openai-to-slow-roll-the-release-of-its-new-model-over-safety-concerns/](https://techcrunch.com/2026/06/25/the-white-house-is-asking-openai-to-slow-roll-the-release-of-its-new-model-over-safety-concerns/)

生成摘要时出错

---

## 51. Swsim: A Software SIM Card

**原文标题**: Swsim: A Software SIM Card

**原文链接**: [https://github.com/tomasz-lisowski/swsim](https://github.com/tomasz-lisowski/swsim)

生成摘要时出错

---

## 52. South Korea to Train All Active-Duty Soldiers to Operate Drones

**原文标题**: South Korea to Train All Active-Duty Soldiers to Operate Drones

**原文链接**: [https://www.wsj.com/world/asia/south-korea-to-train-all-active-duty-soldiers-to-operate-drones-28ddcceb](https://www.wsj.com/world/asia/south-korea-to-train-all-active-duty-soldiers-to-operate-drones-28ddcceb)

生成摘要时出错

---

## 53. The annotated PyTorch training loop

**原文标题**: The annotated PyTorch training loop

**原文链接**: [https://idlemachines.co.uk/essays/pytorch-training-loop](https://idlemachines.co.uk/essays/pytorch-training-loop)

生成摘要时出错

---

## 54. Show HN: I made Google Trends for Hacker News by indexing 18 years of comments

**原文标题**: Show HN: I made Google Trends for Hacker News by indexing 18 years of comments

**原文链接**: [https://hackernewstrends.com](https://hackernewstrends.com)

生成摘要时出错

---

## 55. Medical students are using popular research tool to pump out misleading studies

**原文标题**: Medical students are using popular research tool to pump out misleading studies

**原文链接**: [https://www.science.org/content/article/medical-students-are-using-popular-research-tool-pump-out-misleading-studies](https://www.science.org/content/article/medical-students-are-using-popular-research-tool-pump-out-misleading-studies)

生成摘要时出错

---

## 56. Mixing Visual and Textual Code

**原文标题**: Mixing Visual and Textual Code

**原文链接**: [https://arxiv.org/abs/2603.15855](https://arxiv.org/abs/2603.15855)

生成摘要时出错

---

## 57. Advanced Nintendo Entertainment System (ANES) – NES Modded to Use 2 PPUs

**原文标题**: Advanced Nintendo Entertainment System (ANES) – NES Modded to Use 2 PPUs

**原文链接**: [https://github.com/decrazyo/anes](https://github.com/decrazyo/anes)

生成摘要时出错

---

## 58. Anthropic says Alibaba illicitly extracted Claude AI model capabilities

**原文标题**: Anthropic says Alibaba illicitly extracted Claude AI model capabilities

**原文链接**: [https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/)

生成摘要时出错

---

## 59. Tw-fade: pure CSS scroll-driven edge masking

**原文标题**: Tw-fade: pure CSS scroll-driven edge masking

**原文链接**: [https://pete.design/tw-fade](https://pete.design/tw-fade)

生成摘要时出错

---

## 60. Eyewitness at the Triangle (1911)

**原文标题**: Eyewitness at the Triangle (1911)

**原文链接**: [http://trianglefire.ilr.cornell.edu/index.html](http://trianglefire.ilr.cornell.edu/index.html)

生成摘要时出错

---

## 61. Half-Life 2 in a Browser

**原文标题**: Half-Life 2 in a Browser

**原文链接**: [https://hl2.slqnt.dev/](https://hl2.slqnt.dev/)

生成摘要时出错

---

## 62. OpenAI unveils its first custom chip, built by Broadcom

**原文标题**: OpenAI unveils its first custom chip, built by Broadcom

**原文链接**: [https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/)

生成摘要时出错

---

## 63. Captcha proves you're human. HATCHA proves you're not

**原文标题**: Captcha proves you're human. HATCHA proves you're not

**原文链接**: [https://github.com/mondaycom/HATCHA](https://github.com/mondaycom/HATCHA)

生成摘要时出错

---

## 64. Show HN: Turn native language audio into flashcards and shadowing practice

**原文标题**: Show HN: Turn native language audio into flashcards and shadowing practice

**原文链接**: [https://lingochunk.com/try](https://lingochunk.com/try)

生成摘要时出错

---

## 65. Apple to skip high-end M6 Mac chips in favor of AI-focused M7 line

**原文标题**: Apple to skip high-end M6 Mac chips in favor of AI-focused M7 line

**原文链接**: [https://www.bloomberg.com/news/articles/2026-06-25/apple-to-skip-high-end-m6-mac-chips-to-launch-m7-pro-m7-max-m7-ultra-instead?embedded-checkout=true](https://www.bloomberg.com/news/articles/2026-06-25/apple-to-skip-high-end-m6-mac-chips-to-launch-m7-pro-m7-max-m7-ultra-instead?embedded-checkout=true)

生成摘要时出错

---

## 66. LastPass notifies users of yet another data breach

**原文标题**: LastPass notifies users of yet another data breach

**原文链接**: [https://9to5mac.com/2026/06/23/lastpass-notifies-users-of-yet-another-data-breach/](https://9to5mac.com/2026/06/23/lastpass-notifies-users-of-yet-another-data-breach/)

生成摘要时出错

---

## 67. Hey Nico, you didn't vibe code your data room but stole it from Papermark

**原文标题**: Hey Nico, you didn't vibe code your data room but stole it from Papermark

**原文链接**: [https://twitter.com/mfts0/status/2070080422482977095](https://twitter.com/mfts0/status/2070080422482977095)

生成摘要时出错

---

## 68. SOCKMAP - TCP splicing of the future

**原文标题**: SOCKMAP - TCP splicing of the future

**原文链接**: [https://blog.cloudflare.com/sockmap-tcp-splicing-of-the-future/](https://blog.cloudflare.com/sockmap-tcp-splicing-of-the-future/)

生成摘要时出错

---

## 69. Experiments in Sports Seismology for the World Cup

**原文标题**: Experiments in Sports Seismology for the World Cup

**原文链接**: [https://pnsn.org/blog/experiments-in-sports-seismology-for-the-world-cup](https://pnsn.org/blog/experiments-in-sports-seismology-for-the-world-cup)

生成摘要时出错

---

## 70. Zombie unicorns are haunting Silicon Valley

**原文标题**: Zombie unicorns are haunting Silicon Valley

**原文链接**: [https://www.economist.com/business/2026/06/21/zombie-unicorns-are-haunting-silicon-valley](https://www.economist.com/business/2026/06/21/zombie-unicorns-are-haunting-silicon-valley)

生成摘要时出错

---

## 71. How physicists track and trap the elusive neutrino

**原文标题**: How physicists track and trap the elusive neutrino

**原文链接**: [https://www.quantamagazine.org/how-physicists-track-and-trap-the-elusive-neutrino-20260624/](https://www.quantamagazine.org/how-physicists-track-and-trap-the-elusive-neutrino-20260624/)

生成摘要时出错

---

## 72. Show HN: MiniPCs.zip – Charting the Pareto frontier of Mini PCs

**原文标题**: Show HN: MiniPCs.zip – Charting the Pareto frontier of Mini PCs

**原文链接**: [https://minipcs.zip](https://minipcs.zip)

生成摘要时出错

---

## 73. Doing a masters while working in Spain

**原文标题**: Doing a masters while working in Spain

**原文链接**: [https://jan-herlyn.com/blog/doing-a-masters-while-working/](https://jan-herlyn.com/blog/doing-a-masters-while-working/)

生成摘要时出错

---

## 74. RRB-Trees: Efficient Immutable Vectors (2012) [pdf]

**原文标题**: RRB-Trees: Efficient Immutable Vectors (2012) [pdf]

**原文链接**: [https://infoscience.epfl.ch/server/api/core/bitstreams/e5d662ea-1e8d-4dda-b917-8cbb8bb40bf9/content](https://infoscience.epfl.ch/server/api/core/bitstreams/e5d662ea-1e8d-4dda-b917-8cbb8bb40bf9/content)

生成摘要时出错

---

## 75. AMD Readies Full Open-Source HDMI 2.1 Support for Linux

**原文标题**: AMD Readies Full Open-Source HDMI 2.1 Support for Linux

**原文链接**: [https://www.techpowerup.com/348723/amd-readies-full-open-source-hdmi-2-1-support-for-linux](https://www.techpowerup.com/348723/amd-readies-full-open-source-hdmi-2-1-support-for-linux)

生成摘要时出错

---

## 76. Bohemia Interactive: Cold War Assault Remastered Source Code on GitHub

**原文标题**: Bohemia Interactive: Cold War Assault Remastered Source Code on GitHub

**原文链接**: [https://github.com/BohemiaInteractive/CWR](https://github.com/BohemiaInteractive/CWR)

生成摘要时出错

---

## 77. Zig – SPIR-V Backend Progress

**原文标题**: Zig – SPIR-V Backend Progress

**原文链接**: [https://ziglang.org/devlog/2026/#2026-06-26](https://ziglang.org/devlog/2026/#2026-06-26)

生成摘要时出错

---

## 78. Why Dark Sky Lighting?

**原文标题**: Why Dark Sky Lighting?

**原文链接**: [https://www.savingourstars.org/darkskylighting](https://www.savingourstars.org/darkskylighting)

生成摘要时出错

---

## 79. 52-hertz whale

**原文标题**: 52-hertz whale

**原文链接**: [https://en.wikipedia.org/wiki/52-hertz_whale](https://en.wikipedia.org/wiki/52-hertz_whale)

生成摘要时出错

---

## 80. The AI industry is pouring millions into US elections

**原文标题**: The AI industry is pouring millions into US elections

**原文链接**: [https://www.bloodinthemachine.com/p/the-ai-industry-is-pouring-hundreds](https://www.bloodinthemachine.com/p/the-ai-industry-is-pouring-hundreds)

生成摘要时出错

---

## 81. My Steam Machine Is a 50ft HDMI Cable

**原文标题**: My Steam Machine Is a 50ft HDMI Cable

**原文链接**: [https://blog.matthewbrunelle.com/my-steam-machine-is-a-50ft-hdmi-cable/](https://blog.matthewbrunelle.com/my-steam-machine-is-a-50ft-hdmi-cable/)

生成摘要时出错

---

## 82. OAuth for all

**原文标题**: OAuth for all

**原文链接**: [https://blog.cloudflare.com/oauth-for-all/](https://blog.cloudflare.com/oauth-for-all/)

生成摘要时出错

---

## 83. Early adversity leaves lasting molecular imprint across the body: primate study

**原文标题**: Early adversity leaves lasting molecular imprint across the body: primate study

**原文链接**: [https://medicalxpress.com/news/2026-06-early-life-adversity-molecular-imprint.html](https://medicalxpress.com/news/2026-06-early-life-adversity-molecular-imprint.html)

生成摘要时出错

---

## 84. A little bird told her: scientist wins $100k prize for decoding birdsong

**原文标题**: A little bird told her: scientist wins $100k prize for decoding birdsong

**原文链接**: [https://www.theguardian.com/science/2026/jun/26/human-animal-communication-step-closer-scientist-wins-prize-for-decoding-birdsong](https://www.theguardian.com/science/2026/jun/26/human-animal-communication-step-closer-scientist-wins-prize-for-decoding-birdsong)

生成摘要时出错

---

## 85. How to get your first customers [video]

**原文标题**: How to get your first customers [video]

**原文链接**: [https://www.ycombinator.com/library/SF-how-to-get-your-first-10-customers](https://www.ycombinator.com/library/SF-how-to-get-your-first-10-customers)

生成摘要时出错

---

## 86. 45°C cooling design cuts data center water use to near zero

**原文标题**: 45°C cooling design cuts data center water use to near zero

**原文链接**: [https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/](https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/)

生成摘要时出错

---

## 87. Mlibc: A fukk-featured portable C standard library

**原文标题**: Mlibc: A fukk-featured portable C standard library

**原文链接**: [https://github.com/managarm/mlibc](https://github.com/managarm/mlibc)

生成摘要时出错

---

## 88. We’re making Bunny DNS free

**原文标题**: We’re making Bunny DNS free

**原文链接**: [https://bunny.net/blog/were-making-bunny-dns-free/](https://bunny.net/blog/were-making-bunny-dns-free/)

生成摘要时出错

---

## 89. Blogging can just be stating the obvious

**原文标题**: Blogging can just be stating the obvious

**原文链接**: [https://blog.jim-nielsen.com/2026/blogging-stating-the-obvious/](https://blog.jim-nielsen.com/2026/blogging-stating-the-obvious/)

生成摘要时出错

---

## 90. Show HN: Bible as RAG Database

**原文标题**: Show HN: Bible as RAG Database

**原文链接**: [https://www.crosscanon.com/](https://www.crosscanon.com/)

生成摘要时出错

---

## 91. Vision for the Godot Engine

**原文标题**: Vision for the Godot Engine

**原文链接**: [https://godotengine.org/article/godot-vision-statement-2026/](https://godotengine.org/article/godot-vision-statement-2026/)

生成摘要时出错

---

## 92. Puzzling Success of Overparameterization: Lottery Tickets or Escape Dimensions?

**原文标题**: Puzzling Success of Overparameterization: Lottery Tickets or Escape Dimensions?

**原文链接**: [https://infoscience.epfl.ch/entities/publication/9a49779b-f9f8-448d-b3d1-737c78455309](https://infoscience.epfl.ch/entities/publication/9a49779b-f9f8-448d-b3d1-737c78455309)

生成摘要时出错

---

## 93. Polymarket says hackers stole users' funds

**原文标题**: Polymarket says hackers stole users' funds

**原文链接**: [https://techcrunch.com/2026/06/25/polymarket-says-hackers-stole-users-funds/](https://techcrunch.com/2026/06/25/polymarket-says-hackers-stole-users-funds/)

生成摘要时出错

---

## 94. Stealing Is a Skill

**原文标题**: Stealing Is a Skill

**原文链接**: [https://ben-mini.com/2026/stealing-is-a-skill](https://ben-mini.com/2026/stealing-is-a-skill)

生成摘要时出错

---

## 95. What is the mechanical world picture?

**原文标题**: What is the mechanical world picture?

**原文链接**: [http://edwardfeser.blogspot.com/2026/06/what-is-mechanical-world-picture.html](http://edwardfeser.blogspot.com/2026/06/what-is-mechanical-world-picture.html)

生成摘要时出错

---

## 96. FCC may kill $2B program that connects schools and libraries to Internet

**原文标题**: FCC may kill $2B program that connects schools and libraries to Internet

**原文链接**: [https://arstechnica.com/tech-policy/2026/06/fcc-may-kill-2b-program-that-connects-schools-and-libraries-to-internet/](https://arstechnica.com/tech-policy/2026/06/fcc-may-kill-2b-program-that-connects-schools-and-libraries-to-internet/)

生成摘要时出错

---

## 97. I built a GPU back end for Emacs

**原文标题**: I built a GPU back end for Emacs

**原文链接**: [https://en.andros.dev/blog/4b707a03/how-i-built-a-gpu-backend-for-emacs/](https://en.andros.dev/blog/4b707a03/how-i-built-a-gpu-backend-for-emacs/)

生成摘要时出错

---

## 98. I can haz smoller NixOS ISOs?

**原文标题**: I can haz smoller NixOS ISOs?

**原文链接**: [https://natkr.com/2026-06-19-nixos-but-smol/](https://natkr.com/2026-06-19-nixos-but-smol/)

生成摘要时出错

---

## 99. SoftBank 2026 AGM [pdf]

**原文标题**: SoftBank 2026 AGM [pdf]

**原文链接**: [https://group.softbank/media/Project/sbg/sbg/pdf/ir/investors/shareholders/2026/shareholders-meeting_46_05_en.pdf](https://group.softbank/media/Project/sbg/sbg/pdf/ir/investors/shareholders/2026/shareholders-meeting_46_05_en.pdf)

生成摘要时出错

---

## 100. Matt's Script Archive: The Scripts That Reshaped the Web

**原文标题**: Matt's Script Archive: The Scripts That Reshaped the Web

**原文链接**: [https://tedium.co/2026/06/22/matts-script-archive-retrospective/](https://tedium.co/2026/06/22/matts-script-archive-retrospective/)

生成摘要时出错

---

