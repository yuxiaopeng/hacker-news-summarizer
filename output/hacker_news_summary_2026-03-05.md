# Hacker News 热门文章摘要 (2026-03-05)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 维基百科在大规模管理员账号被盗后进入只读模式

**原文标题**: Wikipedia in read-only mode following mass admin account compromise

**原文链接**: [https://www.wikimediastatus.net](https://www.wikimediastatus.net)

2026年3月5日，包括维基百科在内的维基媒体各站点进入受限访问阶段，网站被置于只读模式。根据官方状态日志，该事件始于协调世界时（UTC）约15:36，当时该机构开始调查有关访问问题的报告。

截至UTC 16:11，技术团队已确定原因并开始实施修复。尽管读写功能在17:09已部分恢复，但为维持系统稳定性，若干功能仍处于禁用状态。根据UTC 18:36的最新更新，维基媒体已进入监控阶段，并指出虽然修复程序已生效，但某些编辑功能依然受限。

此次中断发生在该平台此前几周面临的一系列技术挑战之后。状态报告显示，3月3日的数据库问题曾导致严重的编辑延迟，而在2月下旬，该平台多次出现性能下降和连接错误，包括欧洲地区的局部访问缓慢。

虽然提供的状态页面侧重于技术恢复时间表和当前的监控状态，但它确认该平台尚未完全恢复正常运行能力，并正持续接受观察以防止再次发生服务中断。

---

## 2. GPT-5.4 思维系统卡

**原文标题**: GPT-5.4 Thinking System Card

**原文链接**: [https://openai.com/index/gpt-5-4-thinking-system-card/](https://openai.com/index/gpt-5-4-thinking-system-card/)

无法访问文章链接。

---

## 3. Show HN: Jido 2.0，Elixir 智能体框架

**原文标题**: Show HN: Jido 2.0, Elixir Agent Framework

**原文链接**: [https://jido.run/blog/jido-2-0-is-here](https://jido.run/blog/jido-2-0-is-here)

Jido 2.0 是一款新发布的开源 Elixir 框架，旨在 BEAM 运行时上构建自主智能体（autonomous agents）。经过 18 个月的开发，此版本摒弃了 1.0 中过度设计的抽象，转向了优先考虑简洁性和并发性的“BEAM 优先”架构。

**核心架构**
Jido 2.0 的基础是一个纯函数式智能体模型。智能体被视为数据——具体而言，是包含状态、动作和工具的结构体（structs）。所有逻辑都通过单一函数 `cmd/2` 流转，该函数接收一个动作并返回更新后的智能体状态以及“指令”（directives，描述副作用的有类型数据结构）。这种设计允许在无需网络、数据库或 LLM 访问的情况下，对智能体逻辑进行深入的单元测试。

**核心组件与特性**
*   **Jido.AgentServer：** 一个基于 GenServer 的运行时，负责管理智能体的生命周期、信号路由以及父子层级结构。
*   **策略（Strategies）：** 可插拔的执行模型，包括直接执行（顺序执行）、有限状态机（FSM）和行为树。
*   **jido_action 和 jido_signal：** 基于 CloudEvents 规范的标准化合约，用于可组合工具和消息传递。
*   **Jido AI：** 一个提供六种推理策略（如 ReAct、思维链 CoT 和思维树 ToT）的集成层。它利用 ReqLLM，这是一款自定义的多供应商客户端，支持跨多个平台的 600 多个模型。

**生态系统集成**
2.0 版本的一个重要亮点是 **ash_jido**，它为 **Ash Framework** 提供了原生支持。这允许开发人员自动将 Ash 资源转化为可供 AI 调用的工具，同时保留授权策略和类型安全性。

通过利用 Elixir 在容错能力和分布式系统方面的固有优势，Jido 旨在提供一种比 TypeScript 和 Python 生态系统中常见的“玩具级”智能体框架更稳定、更具扩展性的替代方案。

---

## 4. 优秀的软件懂得适可而止。

**原文标题**: Good software knows when to stop

**原文链接**: [https://ogirardot.writizzy.com/p/good-software-knows-when-to-stop](https://ogirardot.writizzy.com/p/good-software-knows-when-to-stop)

在《好的软件懂得适可而止》一文中，奥利维尔·吉拉多特（Olivier Girardot）反对现代科技行业对过度工程和将简单实用的工具进行“AI 粉饰”的痴迷。他以一个讽刺性的场景开篇：基础的 Linux `ls` 命令被一个名为“自适应列表系统”（`als`）的臃肿、人工智能驱动的订阅服务所取代。这一恶搞突显了将复杂技术强加于已经完美运行的工具之上的荒谬性。

文章的核心论点是，高质量软件了解其特定用途，并能抵制成为“全能型”产品的冲动。吉拉多特借鉴了 37Signals（Basecamp 的创作者）的设计哲学及其著作《重来》（*Rework*）和《返璞归真》（*Getting Real*）。他强调了可持续产品开发的几个核心原则：

*   **拥抱约束：** 小团队和有限的预算能带来更好的决策。
*   **默认拒绝：** 每一项新功能都会引入隐藏成本，如复杂性和维护成本。
*   **聚焦“核心”（Epicenter）：** 优先考虑核心界面和功能，而非边缘特性。
*   **理解问题：** 不要只是构建用户要求的东西，而是要解决底层需求。

吉拉多特批评了当前的市趋势，指出像 Minio 和 Oracle Database 这样成熟的产品是如何通过打上 AI 标签来重新包装自己以紧跟潮流的。他最后总结道，成为解决特定问题的可靠“事实标准”具有巨大价值。最终，“好的软件”是由克制定义的——即知道其任务何时完成，并拒绝为了追逐“新热点”而牺牲实用性。

---

## 5. 一个 GitHub Issue 标题导致 4000 台开发者机器被攻破

**原文标题**: A GitHub Issue Title Compromised 4k Developer Machines

**原文链接**: [https://grith.ai/blog/clinejection-when-your-ai-tool-installs-another](https://grith.ai/blog/clinejection-when-your-ai-tool-installs-another)

2026 年 2 月，一场名为“Clinejection”的供应链攻击通过利用热门 npm 软件包 `cline` 破坏了约 4000 台开发人员机器。此次入侵展示了一个由简单 GitHub issue 标题发起的、复杂的五步漏洞利用链。

**攻击链：**
1.  **提示词注入：** 攻击者提交了一个标题中嵌入指令的 GitHub issue。Cline 的 AI 分拣机器人 (Claude) 将这个未经清理的标题处理为合法命令。
2.  **任意代码执行：** 机器人根据指令从一个仿冒 (typosquatted) 仓库安装了软件包，从而触发了远程 shell 脚本。
3.  **缓存投毒：** 该脚本使用名为“Cacheract”的工具灌满 GitHub Actions 缓存，驱逐合法条目并替换为恶意版本。
4.  **凭据窃取：** 当 Cline 的每日发布工作流恢复被投毒的缓存时，攻击者窃取了包括 `NPM_RELEASE_TOKEN` 在内的敏感凭据。
5.  **恶意发布：** 攻击者利用窃取的令牌发布了 `cline@2.3.0`。该版本包含一个 `postinstall` 钩子，会静默安装 **OpenClaw**——这是一个拥有完整系统访问权限和持久化能力的独立 AI 智能体。

**人为与系统失效：**
研究人员 Adnan Khan 已于 1 月份报告了该漏洞，但 Cline 团队未予回应。在 Khan 于 2 月份公开披露后，团队试图轮换凭据，却不慎让暴露的令牌保持有效。一名身份不明的攻击者将 Khan 的概念验证代码武器化，发起了最终攻击。

**关键启示：**
此事件凸显了“AI 安装 AI”的风险，即受损的智能体将其权限委托给未经审核的工具。由于载荷是合法软件包，`npm audit` 等标准安全控制措施均告失效。此后，Cline 已转向基于 OIDC 的来源验证以消除长期令牌，并从 CI/CD 中移除了 AI 分拣。这印证了在缺乏系统调用级监控的情况下，授予 AI 智能体访问机密和系统操作权限的危险性。

---

## 6. 基于脑数据重建视觉感知的数据集

**原文标题**: Datasets for Reconstructing Visual Perception from Brain Data

**原文链接**: [https://github.com/seelikat/neuro-visual-reconstruction-dataset-index](https://github.com/seelikat/neuro-visual-reconstruction-dataset-index)

本文为人工智能和机器学习研究人员提供了一份关于利用公开神经影像（fMRI）数据集进行视觉感知重建的综合指南。其首要目标是通过强调可能导致“伪重建”的方法论陷阱，架起计算机视觉与神经科学之间的桥梁。

**核心概念与定义**
本指南严格区分了机器学习文献中经常混淆的三项任务：
*   **解码（Decoding）：** 划分为闭集类别的N路分类。
*   **识别（Identification）：** 从有限的候选集中检索特定刺激。
*   **重建（Reconstruction）：** 一种生成式逆问题，旨在从大脑活动中重建全新的、开集式刺激。

**数据集评估标准**
为确保结果的严谨性，本文概述了选择数据集的几项标准：
*   **训练-测试独立性：** 避免语义或视觉重叠，以确保模型不仅仅是通过分类来走“捷径”。
*   **数据质量：** 高视野覆盖范围和细小的体素尺寸（高分辨率）能提供更细粒度的信息。
*   **可靠性：** 优先选择具有多次刺激重复（高信噪比）和严格受试者注视要求的数据集，以最大限度地减少噪声和眼动干扰。

**重点数据集**
索引对几个具有影响力的数据集进行了分类：
*   **vim-1 & Miyawaki：** 用于灰度和像素级重建的基础性、小规模数据集。
*   **通用物体解码（Generic Object Decoding）：** 专为重建设计，训练集和测试集之间有严格的类别隔离。
*   **自然场景数据集（NSD）：** 目前的行业金标准，具有大规模和高分辨率的7T fMRI数据，但研究人员需警惕其默认划分中的语义聚类问题。
*   **BOLD5000 & BRAINS：** 分别提供极高的刺激多样性和受控的手写字符集。

文章总结指出，虽然基于fMRI的重建正日益流行，但其成功取决于对底层生物数据局限性的理解，并确保模型能够泛化到真正的全新视觉体验中。

---

## 7. 利用 JDK Vector API 优化推荐系统

**原文标题**: Optimizing Recommendation Systems with JDK's Vector API

**原文链接**: [https://netflixtechblog.com/optimizing-recommendation-systems-with-jdks-vector-api-30d2830401ec](https://netflixtechblog.com/optimizing-recommendation-systems-with-jdks-vector-api-30d2830401ec)

在《利用 JDK Vector API 优化推荐系统》一文中，Netflix 工程师探讨了如何通过 Java 直接利用现代 CPU 功能来提升其推荐引擎的性能。

**面临的挑战**
Netflix 的推荐系统在比较用户和内容嵌入（embeddings）时，高度依赖点积和余弦相似度等向量数学运算。长期以来，在 Java 中实现这些运算的高性能，要么依赖 JIT 编译器的自动向量化（这并不稳定），要么使用 JNI（Java Native Interface）调用原生 C++ 库，而后者会引入复杂性和额外开销。

**解决方案：JDK Vector API**
JDK Vector API（作为孵化功能引入）允许开发者直接在 Java 中编写 SIMD（单指令多数据）代码。SIMD 使 CPU 能够利用宽寄存器（如 AVX-2 或 AVX-512）同时对多个数据点执行相同的操作。

**核心优势**
1. **性能**：Netflix 观察到了显著的提速，基于向量的点积实现性能比传统的标量 Java 代码快达 9 倍。
2. **可维护性**：通过使用 Vector API，开发者无需离开 Java 生态系统即可获得接近原生的性能，从而避免了“JNI 税”以及维护独立原生二进制文件带来的架构复杂性。
3. **移植性**：该 API 采用平台无关设计，能够编译为底层硬件上可用的最高效指令（例如，在 AVX-2 和 AVX-512 之间自动切换）。

**结论**
Vector API 弥补了 Java 的开发效率与机器学习及高维数据处理所需的极致性能之间的鸿沟。对于 Netflix 而言，这项优化支持了更复杂的模型，并降低了为用户提供个性化推荐的延迟。

---

## 8. Show HN: PageAgent, A GUI agent that lives inside your web app

**原文标题**: Show HN: PageAgent, A GUI agent that lives inside your web app

**原文链接**: [https://alibaba.github.io/page-agent/](https://alibaba.github.io/page-agent/)

生成摘要时出错

---

## 9. The Brand Age

**原文标题**: The Brand Age

**原文链接**: [https://paulgraham.com/brandage.html](https://paulgraham.com/brandage.html)

生成摘要时出错

---

## 10. The Government Uses Targeted Advertising to Track Your Location

**原文标题**: The Government Uses Targeted Advertising to Track Your Location

**原文链接**: [https://www.eff.org/deeplinks/2026/03/targeted-advertising-gives-your-location-government-just-ask-cbp](https://www.eff.org/deeplinks/2026/03/targeted-advertising-gives-your-location-government-just-ask-cbp)

生成摘要时出错

---

## 11. GPT-5.4 Thinking and GPT-5.4 Pro

**原文标题**: GPT-5.4 Thinking and GPT-5.4 Pro

**原文链接**: [https://twitter.com/i/status/2029620619743219811](https://twitter.com/i/status/2029620619743219811)

生成摘要时出错

---

## 12. Nvidia PersonaPlex 7B on Apple Silicon: Full-Duplex Speech-to-Speech in Swift

**原文标题**: Nvidia PersonaPlex 7B on Apple Silicon: Full-Duplex Speech-to-Speech in Swift

**原文链接**: [https://blog.ivan.digital/nvidia-personaplex-7b-on-apple-silicon-full-duplex-speech-to-speech-in-native-swift-with-mlx-0aa5276f2e23](https://blog.ivan.digital/nvidia-personaplex-7b-on-apple-silicon-full-duplex-speech-to-speech-in-native-swift-with-mlx-0aa5276f2e23)

生成摘要时出错

---

## 13. Fast-Servers

**原文标题**: Fast-Servers

**原文链接**: [https://geocar.sdf1.org/fast-servers.html](https://geocar.sdf1.org/fast-servers.html)

生成摘要时出错

---

## 14. Google Workspace CLI

**原文标题**: Google Workspace CLI

**原文链接**: [https://github.com/googleworkspace/cli](https://github.com/googleworkspace/cli)

生成摘要时出错

---

## 15. Greg Kroah-Hartman Stretches Support Periods for Key Linux LTS Kernels

**原文标题**: Greg Kroah-Hartman Stretches Support Periods for Key Linux LTS Kernels

**原文链接**: [https://fossforce.com/2026/03/greg-kroah-hartman-stretches-support-periods-for-key-linux-lts-kernels/](https://fossforce.com/2026/03/greg-kroah-hartman-stretches-support-periods-for-key-linux-lts-kernels/)

生成摘要时出错

---

## 16. GPT 5.4 思维与专业版

**原文标题**: GPT 5.4 Thinking and Pro

**原文链接**: [https://twitter.com/OpenAI/status/2029620619743219811](https://twitter.com/OpenAI/status/2029620619743219811)

生成摘要时出错

---

## 17. World-first gigabit laser link between aircraft and geostationary satellite

**原文标题**: World-first gigabit laser link between aircraft and geostationary satellite

**原文链接**: [https://www.esa.int/Applications/Connectivity_and_Secure_Communications/World-first_gigabit-per-second_laser_link_between_aircraft_and_geostationary_satellite](https://www.esa.int/Applications/Connectivity_and_Secure_Communications/World-first_gigabit-per-second_laser_link_between_aircraft_and_geostationary_satellite)

生成摘要时出错

---

## 18. Relicensing with AI-Assisted Rewrite

**原文标题**: Relicensing with AI-Assisted Rewrite

**原文链接**: [https://tuananh.net/2026/03/05/relicensing-with-ai-assisted-rewrite/](https://tuananh.net/2026/03/05/relicensing-with-ai-assisted-rewrite/)

生成摘要时出错

---

## 19. Google Safe Browsing missed 84% of confirmed phishing sites

**原文标题**: Google Safe Browsing missed 84% of confirmed phishing sites

**原文链接**: [https://www.norn-labs.com/blog/huginn-report-feb-2026](https://www.norn-labs.com/blog/huginn-report-feb-2026)

生成摘要时出错

---

## 20. Intelligence is a commodity. Context is the real AI Moat

**原文标题**: Intelligence is a commodity. Context is the real AI Moat

**原文链接**: [https://adlrocha.substack.com/p/adlrocha-intelligence-is-a-commodity](https://adlrocha.substack.com/p/adlrocha-intelligence-is-a-commodity)

生成摘要时出错

---

## 21. Poor Man's Polaroid

**原文标题**: Poor Man's Polaroid

**原文链接**: [https://boxart.lt/blog/poor_mans_polaroid](https://boxart.lt/blog/poor_mans_polaroid)

生成摘要时出错

---

## 22. The Man Who Broke into Jail

**原文标题**: The Man Who Broke into Jail

**原文链接**: [https://www.newyorker.com/magazine/2026/03/09/alexander-friedmann-profile-prison-reform](https://www.newyorker.com/magazine/2026/03/09/alexander-friedmann-profile-prison-reform)

生成摘要时出错

---

## 23. AMD will bring its “Ryzen AI” processors to standard desktop PCs for first time

**原文标题**: AMD will bring its “Ryzen AI” processors to standard desktop PCs for first time

**原文链接**: [https://arstechnica.com/gadgets/2026/03/amd-ryzen-ai-400-cpus-will-bring-upgraded-graphics-to-socket-am5-desktops/](https://arstechnica.com/gadgets/2026/03/amd-ryzen-ai-400-cpus-will-bring-upgraded-graphics-to-socket-am5-desktops/)

生成摘要时出错

---

## 24. Building a new Flash

**原文标题**: Building a new Flash

**原文链接**: [https://bill.newgrounds.com/news/post/1607118](https://bill.newgrounds.com/news/post/1607118)

生成摘要时出错

---

## 25. Smalltalk's Browser: Unbeatable, yet Not Enough

**原文标题**: Smalltalk's Browser: Unbeatable, yet Not Enough

**原文链接**: [https://blog.lorenzano.eu/smalltalks-browser-unbeatable-yet-not-enough/](https://blog.lorenzano.eu/smalltalks-browser-unbeatable-yet-not-enough/)

生成摘要时出错

---

## 26. Judge orders government to begin refunding more than $130B in tariffs

**原文标题**: Judge orders government to begin refunding more than $130B in tariffs

**原文链接**: [https://www.wsj.com/politics/policy/judge-orders-government-to-begin-refunding-more-than-130-billion-in-tariffs-fdc1e62c](https://www.wsj.com/politics/policy/judge-orders-government-to-begin-refunding-more-than-130-billion-in-tariffs-fdc1e62c)

生成摘要时出错

---

## 27. Jails for NetBSD – Kernel Enforced Isolation and Native Resource Control

**原文标题**: Jails for NetBSD – Kernel Enforced Isolation and Native Resource Control

**原文链接**: [https://netbsd-jails.petermann-digital.de/](https://netbsd-jails.petermann-digital.de/)

生成摘要时出错

---

## 28. Arabic document from 17th-cent. rubbish heap confirms semi-legendary Nubian king

**原文标题**: Arabic document from 17th-cent. rubbish heap confirms semi-legendary Nubian king

**原文链接**: [https://phys.org/news/2026-02-arabic-document-17th-century-rubbish.html](https://phys.org/news/2026-02-arabic-document-17th-century-rubbish.html)

生成摘要时出错

---

## 29. The IRIX 6.5.7M (sgi) source code

**原文标题**: The IRIX 6.5.7M (sgi) source code

**原文链接**: [https://github.com/calmsacibis995/irix-657m-src](https://github.com/calmsacibis995/irix-657m-src)

生成摘要时出错

---

## 30. Something is afoot in the land of Qwen

**原文标题**: Something is afoot in the land of Qwen

**原文链接**: [https://simonwillison.net/2026/Mar/4/qwen/](https://simonwillison.net/2026/Mar/4/qwen/)

生成摘要时出错

---

## 31. The L in "LLM" Stands for Lying

**原文标题**: The L in "LLM" Stands for Lying

**原文链接**: [https://acko.net/blog/the-l-in-llm-stands-for-lying/](https://acko.net/blog/the-l-in-llm-stands-for-lying/)

生成摘要时出错

---

## 32. A Number with a Shadow

**原文标题**: A Number with a Shadow

**原文链接**: [https://campedersen.com/tang](https://campedersen.com/tang)

生成摘要时出错

---

## 33. OpenBSD on SGI: A Rollercoaster Story

**原文标题**: OpenBSD on SGI: A Rollercoaster Story

**原文链接**: [http://miod.online.fr/software/openbsd/stories/sgiall.html](http://miod.online.fr/software/openbsd/stories/sgiall.html)

生成摘要时出错

---

## 34. Earth Garden: Field Recordings Around the World

**原文标题**: Earth Garden: Field Recordings Around the World

**原文链接**: [https://earth-garden.alen.ro/](https://earth-garden.alen.ro/)

生成摘要时出错

---

## 35. MacBook Neo

**原文标题**: MacBook Neo

**原文链接**: [https://www.apple.com/newsroom/2026/03/say-hello-to-macbook-neo/](https://www.apple.com/newsroom/2026/03/say-hello-to-macbook-neo/)

生成摘要时出错

---

## 36. AI and the Ship of Theseus

**原文标题**: AI and the Ship of Theseus

**原文链接**: [https://lucumr.pocoo.org/2026/3/5/theseus/](https://lucumr.pocoo.org/2026/3/5/theseus/)

生成摘要时出错

---

## 37. US asked Ukraine for help fighting Iranian drones, Zelensky says

**原文标题**: US asked Ukraine for help fighting Iranian drones, Zelensky says

**原文链接**: [https://www.bbc.com/news/articles/cr5llg0e9g9o](https://www.bbc.com/news/articles/cr5llg0e9g9o)

生成摘要时出错

---

## 38. BMW Group to deploy humanoid robots in production in Germany for the first time

**原文标题**: BMW Group to deploy humanoid robots in production in Germany for the first time

**原文链接**: [https://www.press.bmwgroup.com/global/article/detail/T0455864EN/bmw-group-to-deploy-humanoid-robots-in-production-in-germany-for-the-first-time?language=en](https://www.press.bmwgroup.com/global/article/detail/T0455864EN/bmw-group-to-deploy-humanoid-robots-in-production-in-germany-for-the-first-time?language=en)

生成摘要时出错

---

## 39. GPT-5.4

**原文标题**: GPT-5.4

**原文链接**: [https://openai.com/index/introducing-gpt-5-4/](https://openai.com/index/introducing-gpt-5-4/)

生成摘要时出错

---

## 40. The Self-Help Trap: What 20 Years of "Optimizing" Has Taught Me

**原文标题**: The Self-Help Trap: What 20 Years of "Optimizing" Has Taught Me

**原文链接**: [https://tim.blog/2026/03/04/the-self-help-trap/](https://tim.blog/2026/03/04/the-self-help-trap/)

生成摘要时出错

---

## 41. No right to relicense this project

**原文标题**: No right to relicense this project

**原文链接**: [https://github.com/chardet/chardet/issues/327](https://github.com/chardet/chardet/issues/327)

生成摘要时出错

---

## 42. US tech firms pledge at White House to bear costs of energy for datacenters

**原文标题**: US tech firms pledge at White House to bear costs of energy for datacenters

**原文链接**: [https://www.theguardian.com/us-news/2026/mar/04/us-tech-companies-energy-cost-pledge-white-house](https://www.theguardian.com/us-news/2026/mar/04/us-tech-companies-energy-cost-pledge-white-house)

生成摘要时出错

---

## 43. Show HN: Poppy – A simple app to stay intentional with relationships

**原文标题**: Show HN: Poppy – A simple app to stay intentional with relationships

**原文链接**: [https://poppy-connection-keeper.netlify.app/](https://poppy-connection-keeper.netlify.app/)

生成摘要时出错

---

## 44. Picking Up a Zillion Pieces of Litter

**原文标题**: Picking Up a Zillion Pieces of Litter

**原文链接**: [https://www.sixstepstobetterhealth.com/litter.html](https://www.sixstepstobetterhealth.com/litter.html)

生成摘要时出错

---

## 45. Dulce et Decorum Est (1921)

**原文标题**: Dulce et Decorum Est (1921)

**原文链接**: [https://www.poetryfoundation.org/poems/46560/dulce-et-decorum-est](https://www.poetryfoundation.org/poems/46560/dulce-et-decorum-est)

生成摘要时出错

---

## 46. Roboflow (YC S20) Is Hiring a Security Engineer for AI Infra

**原文标题**: Roboflow (YC S20) Is Hiring a Security Engineer for AI Infra

**原文链接**: [https://roboflow.com/careers](https://roboflow.com/careers)

生成摘要时出错

---

## 47. Qwen3.5 Fine-Tuning Guide

**原文标题**: Qwen3.5 Fine-Tuning Guide

**原文链接**: [https://unsloth.ai/docs/models/qwen3.5/fine-tune](https://unsloth.ai/docs/models/qwen3.5/fine-tune)

生成摘要时出错

---

## 48. Dario Amodei calls OpenAI’s messaging around military deal ‘straight up lies’

**原文标题**: Dario Amodei calls OpenAI’s messaging around military deal ‘straight up lies’

**原文链接**: [https://techcrunch.com/2026/03/04/anthropic-ceo-dario-amodei-calls-openais-messaging-around-military-deal-straight-up-lies-report-says/](https://techcrunch.com/2026/03/04/anthropic-ceo-dario-amodei-calls-openais-messaging-around-military-deal-straight-up-lies-report-says/)

生成摘要时出错

---

## 49. Apple: Enough Is Enough

**原文标题**: Apple: Enough Is Enough

**原文链接**: [https://bastibe.de/2026-03-05-apple-woes.html](https://bastibe.de/2026-03-05-apple-woes.html)

生成摘要时出错

---

## 50. NRC issues first commercial reactor construction approval in 10 years [pdf]

**原文标题**: NRC issues first commercial reactor construction approval in 10 years [pdf]

**原文链接**: [https://www.nrc.gov/sites/default/files/cdn/doc-collection-news/2026/26-028.pdf](https://www.nrc.gov/sites/default/files/cdn/doc-collection-news/2026/26-028.pdf)

生成摘要时出错

---

## 51. Moss is a pixel canvas where every brush is a tiny program

**原文标题**: Moss is a pixel canvas where every brush is a tiny program

**原文链接**: [https://www.moss.town/](https://www.moss.town/)

生成摘要时出错

---

## 52. “It turns out” (2010)

**原文标题**: “It turns out” (2010)

**原文链接**: [https://jsomers.net/blog/it-turns-out](https://jsomers.net/blog/it-turns-out)

生成摘要时出错

---

## 53. Libre Solar – Open Hardware for Renewable Energy

**原文标题**: Libre Solar – Open Hardware for Renewable Energy

**原文链接**: [https://libre.solar](https://libre.solar)

生成摘要时出错

---

## 54. Humans 40k yrs ago developed a system of conventional signs

**原文标题**: Humans 40k yrs ago developed a system of conventional signs

**原文链接**: [https://www.pnas.org/doi/10.1073/pnas.2520385123](https://www.pnas.org/doi/10.1073/pnas.2520385123)

生成摘要时出错

---

## 55. NanoGPT Slowrun: Language Modeling with Limited Data, Infinite Compute

**原文标题**: NanoGPT Slowrun: Language Modeling with Limited Data, Infinite Compute

**原文链接**: [https://qlabs.sh/slowrun](https://qlabs.sh/slowrun)

生成摘要时出错

---

## 56. You Just Reveived

**原文标题**: You Just Reveived

**原文链接**: [https://dylan.gr/1772520728](https://dylan.gr/1772520728)

生成摘要时出错

---

## 57. Claude's Cycles [pdf]

**原文标题**: Claude's Cycles [pdf]

**原文链接**: [https://www-cs-faculty.stanford.edu/~knuth/papers/claude-cycles.pdf](https://www-cs-faculty.stanford.edu/~knuth/papers/claude-cycles.pdf)

生成摘要时出错

---

## 58. Was Windows 1.0's lack of overlapping windows a legal or a technical matter?

**原文标题**: Was Windows 1.0's lack of overlapping windows a legal or a technical matter?

**原文链接**: [https://retrocomputing.stackexchange.com/questions/32511/was-windows-1-0s-lack-of-overlapping-windows-a-legal-or-a-technical-matter](https://retrocomputing.stackexchange.com/questions/32511/was-windows-1-0s-lack-of-overlapping-windows-a-legal-or-a-technical-matter)

生成摘要时出错

---

## 59. Glaze by Raycast

**原文标题**: Glaze by Raycast

**原文链接**: [https://www.glazeapp.com/](https://www.glazeapp.com/)

生成摘要时出错

---

## 60. The View from RSS

**原文标题**: The View from RSS

**原文链接**: [https://www.carolinecrampton.com/the-view-from-rss/](https://www.carolinecrampton.com/the-view-from-rss/)

生成摘要时出错

---

## 61. Motorola GrapheneOS devices will be bootloader unlockable/relockable

**原文标题**: Motorola GrapheneOS devices will be bootloader unlockable/relockable

**原文链接**: [https://grapheneos.social/@GrapheneOS/116160393783585567](https://grapheneos.social/@GrapheneOS/116160393783585567)

生成摘要时出错

---

## 62. Stop the Interviews

**原文标题**: Stop the Interviews

**原文链接**: [https://blog.joeschrag.com/2026/03/stop-interviews.html](https://blog.joeschrag.com/2026/03/stop-interviews.html)

生成摘要时出错

---

## 63. Raspberry Pi Pico as AM Radio Transmitter

**原文标题**: Raspberry Pi Pico as AM Radio Transmitter

**原文链接**: [https://www.pesfandiar.com/blog/2026/02/28/pico-am-radio-transmitter](https://www.pesfandiar.com/blog/2026/02/28/pico-am-radio-transmitter)

生成摘要时出错

---

## 64. MyFirst Kids Watch Hacked. Access to Camera and Microphone

**原文标题**: MyFirst Kids Watch Hacked. Access to Camera and Microphone

**原文链接**: [https://www.kth.se/en/om/nyheter/centrala-nyheter/kth-studenten-hackade-klocka-for-barn-1.1461249](https://www.kth.se/en/om/nyheter/centrala-nyheter/kth-studenten-hackade-klocka-for-barn-1.1461249)

生成摘要时出错

---

## 65. What Python’s asyncio primitives get wrong about shared state

**原文标题**: What Python’s asyncio primitives get wrong about shared state

**原文链接**: [https://www.inngest.com/blog/no-lost-updates-python-asyncio](https://www.inngest.com/blog/no-lost-updates-python-asyncio)

生成摘要时出错

---

## 66. A CPU that runs entirely on GPU

**原文标题**: A CPU that runs entirely on GPU

**原文链接**: [https://github.com/robertcprice/nCPU](https://github.com/robertcprice/nCPU)

生成摘要时出错

---

## 67. Emails to Outlook.com rejected due to a fault or overzealous blocking rules

**原文标题**: Emails to Outlook.com rejected due to a fault or overzealous blocking rules

**原文链接**: [https://www.theregister.com/2026/03/04/users_fume_at_outlookcom_email/](https://www.theregister.com/2026/03/04/users_fume_at_outlookcom_email/)

生成摘要时出错

---

## 68. Devenv 2.0: A Fresh Interface to Nix

**原文标题**: Devenv 2.0: A Fresh Interface to Nix

**原文链接**: [https://devenv.sh/blog/2026/03/05/devenv-20-a-fresh-interface-to-nix/](https://devenv.sh/blog/2026/03/05/devenv-20-a-fresh-interface-to-nix/)

生成摘要时出错

---

## 69. Dbslice: Extract a slice of your production database to reproduce bugs

**原文标题**: Dbslice: Extract a slice of your production database to reproduce bugs

**原文链接**: [https://github.com/nabroleonx/dbslice](https://github.com/nabroleonx/dbslice)

生成摘要时出错

---

## 70. An interactive map of Flock Cams

**原文标题**: An interactive map of Flock Cams

**原文链接**: [https://deflock.org/map#map=5/37.125286/-96.284180](https://deflock.org/map#map=5/37.125286/-96.284180)

生成摘要时出错

---

## 71. Relax NG is a schema language for XML (2014)

**原文标题**: Relax NG is a schema language for XML (2014)

**原文链接**: [https://relaxng.org/](https://relaxng.org/)

生成摘要时出错

---

## 72. Chaos and Dystopian news for the dead internet survivors

**原文标题**: Chaos and Dystopian news for the dead internet survivors

**原文链接**: [https://www.fubardaily.com](https://www.fubardaily.com)

生成摘要时出错

---

## 73. To understand our fascination with crystals, researchers gave some to chimps

**原文标题**: To understand our fascination with crystals, researchers gave some to chimps

**原文链接**: [https://www.nytimes.com/2026/03/04/science/chimpanzees-crystals.html](https://www.nytimes.com/2026/03/04/science/chimpanzees-crystals.html)

生成摘要时出错

---

## 74. RE#: how we built the fastest regex engine in F#

**原文标题**: RE#: how we built the fastest regex engine in F#

**原文链接**: [https://iev.ee/blog/resharp-how-we-built-the-fastest-regex-in-fsharp/](https://iev.ee/blog/resharp-how-we-built-the-fastest-regex-in-fsharp/)

生成摘要时出错

---

## 75. Malm Whale

**原文标题**: Malm Whale

**原文链接**: [https://www.atlasobscura.com/places/malm-whale](https://www.atlasobscura.com/places/malm-whale)

生成摘要时出错

---

## 76. Jensen Huang says Nvidia is pulling back from OpenAI and Anthropic

**原文标题**: Jensen Huang says Nvidia is pulling back from OpenAI and Anthropic

**原文链接**: [https://techcrunch.com/2026/03/04/jensen-huang-says-nvidia-is-pulling-back-from-openai-and-anthropic-but-his-explanation-raises-more-questions-than-it-answers/](https://techcrunch.com/2026/03/04/jensen-huang-says-nvidia-is-pulling-back-from-openai-and-anthropic-but-his-explanation-raises-more-questions-than-it-answers/)

生成摘要时出错

---

## 77. Espflash – Go CLI/library for flashing ESP8266/ESP32 with no dependencies

**原文标题**: Espflash – Go CLI/library for flashing ESP8266/ESP32 with no dependencies

**原文链接**: [https://github.com/tinygo-org/espflash](https://github.com/tinygo-org/espflash)

生成摘要时出错

---

## 78. Making Firefox's right-click not suck with about:config

**原文标题**: Making Firefox's right-click not suck with about:config

**原文链接**: [https://joshua.hu/firefox-making-right-click-not-suck](https://joshua.hu/firefox-making-right-click-not-suck)

生成摘要时出错

---

## 79. Daemon (2006)

**原文标题**: Daemon (2006)

**原文链接**: [https://en.wikipedia.org/wiki/Daemon_(novel)](https://en.wikipedia.org/wiki/Daemon_(novel))

生成摘要时出错

---

## 80. FCC Chair to Europe: If You Restrict US Satellite Providers, We'll Ban You Here

**原文标题**: FCC Chair to Europe: If You Restrict US Satellite Providers, We'll Ban You Here

**原文链接**: [https://www.pcmag.com/news/fcc-chair-to-europe-restrict-us-satellite-providers-well-ban-you-in-us](https://www.pcmag.com/news/fcc-chair-to-europe-restrict-us-satellite-providers-well-ban-you-in-us)

生成摘要时出错

---

## 81. Data Has Weight but Only on SSDs

**原文标题**: Data Has Weight but Only on SSDs

**原文链接**: [https://cubiclenate.com/2026/03/04/data-has-weight-but-only-on-ssds-blathering/](https://cubiclenate.com/2026/03/04/data-has-weight-but-only-on-ssds-blathering/)

生成摘要时出错

---

## 82. Show HN: Stacked Game of Life

**原文标题**: Show HN: Stacked Game of Life

**原文链接**: [https://stacked-game-of-life.koenvangilst.nl/](https://stacked-game-of-life.koenvangilst.nl/)

生成摘要时出错

---

## 83. A bit of fluid mechanics from scratch not from scratch

**原文标题**: A bit of fluid mechanics from scratch not from scratch

**原文链接**: [https://tsvibt.blogspot.com/2026/02/a-bit-of-fluid-mechanics-from-scratch.html](https://tsvibt.blogspot.com/2026/02/a-bit-of-fluid-mechanics-from-scratch.html)

生成摘要时出错

---

## 84. Faster C software with Dynamic Feature Detection

**原文标题**: Faster C software with Dynamic Feature Detection

**原文链接**: [https://gist.github.com/jjl/d998164191af59a594500687a679b98d](https://gist.github.com/jjl/d998164191af59a594500687a679b98d)

生成摘要时出错

---

## 85. Graphics Programming Resources

**原文标题**: Graphics Programming Resources

**原文链接**: [https://develop--gpvm-website.netlify.app/resources/](https://develop--gpvm-website.netlify.app/resources/)

生成摘要时出错

---

## 86. Rising carbon dioxide levels now detected in human blood

**原文标题**: Rising carbon dioxide levels now detected in human blood

**原文链接**: [https://phys.org/news/2026-02-carbon-dioxide-human-blood.html](https://phys.org/news/2026-02-carbon-dioxide-human-blood.html)

生成摘要时出错

---

## 87. Weave – A language aware merge algorithm based on entities

**原文标题**: Weave – A language aware merge algorithm based on entities

**原文链接**: [https://github.com/Ataraxy-Labs/weave](https://github.com/Ataraxy-Labs/weave)

生成摘要时出错

---

## 88. TikTok will not introduce end-to-end encryption, saying it makes users less safe

**原文标题**: TikTok will not introduce end-to-end encryption, saying it makes users less safe

**原文链接**: [https://www.bbc.com/news/articles/cly2m5e5ke4o](https://www.bbc.com/news/articles/cly2m5e5ke4o)

生成摘要时出错

---

## 89. My spicy take on vibe coding for PMs

**原文标题**: My spicy take on vibe coding for PMs

**原文链接**: [https://www.ddmckinnon.com/2026/02/11/my-%f0%9f%8c%b6-take-on-vibe-coding-for-pms/](https://www.ddmckinnon.com/2026/02/11/my-%f0%9f%8c%b6-take-on-vibe-coding-for-pms/)

生成摘要时出错

---

## 90. Agentic Engineering Patterns

**原文标题**: Agentic Engineering Patterns

**原文链接**: [https://simonwillison.net/guides/agentic-engineering-patterns/](https://simonwillison.net/guides/agentic-engineering-patterns/)

生成摘要时出错

---

## 91. You need to rewrite your CLI for AI agents

**原文标题**: You need to rewrite your CLI for AI agents

**原文链接**: [https://justin.poehnelt.com/posts/rewrite-your-cli-for-ai-agents/](https://justin.poehnelt.com/posts/rewrite-your-cli-for-ai-agents/)

生成摘要时出错

---

## 92. Microplastics and nanoplastics in urban air originate mainly from tire abrasion

**原文标题**: Microplastics and nanoplastics in urban air originate mainly from tire abrasion

**原文链接**: [https://phys.org/news/2026-03-microplastics-nanoplastics-urban-air-abrasion.html](https://phys.org/news/2026-03-microplastics-nanoplastics-urban-air-abrasion.html)

生成摘要时出错

---

## 93. Meta’s AI smart glasses and data privacy concerns

**原文标题**: Meta’s AI smart glasses and data privacy concerns

**原文链接**: [https://www.svd.se/a/K8nrV4/metas-ai-smart-glasses-and-data-privacy-concerns-workers-say-we-see-everything](https://www.svd.se/a/K8nrV4/metas-ai-smart-glasses-and-data-privacy-concerns-workers-say-we-see-everything)

生成摘要时出错

---

## 94. My Favorite 39C3 Talks

**原文标题**: My Favorite 39C3 Talks

**原文链接**: [https://asindu.xyz/my-favorite-39c3-talks/](https://asindu.xyz/my-favorite-39c3-talks/)

生成摘要时出错

---

## 95. Billy bookshelves as a retro motherboard "rack"

**原文标题**: Billy bookshelves as a retro motherboard "rack"

**原文链接**: [https://rubenerd.com/billy-bookcase-as-a-retro-motherboard-rack/](https://rubenerd.com/billy-bookcase-as-a-retro-motherboard-rack/)

生成摘要时出错

---

## 96. MacBook Pro with M5 Pro and M5 Max

**原文标题**: MacBook Pro with M5 Pro and M5 Max

**原文链接**: [https://www.apple.com/newsroom/2026/03/apple-introduces-macbook-pro-with-all-new-m5-pro-and-m5-max/](https://www.apple.com/newsroom/2026/03/apple-introduces-macbook-pro-with-all-new-m5-pro-and-m5-max/)

生成摘要时出错

---

## 97. Flip Distance of Convex Triangulations and Tree Rotation Is NP-Complete

**原文标题**: Flip Distance of Convex Triangulations and Tree Rotation Is NP-Complete

**原文链接**: [https://arxiv.org/abs/2602.22874](https://arxiv.org/abs/2602.22874)

生成摘要时出错

---

## 98. Rust: The Unlikely Engine of the Vibe Coding Era

**原文标题**: Rust: The Unlikely Engine of the Vibe Coding Era

**原文链接**: [https://www.forbes.com/councils/forbestechcouncil/2026/03/03/rust-the-unlikely-engine-of-the-vibe-coding-era/](https://www.forbes.com/councils/forbestechcouncil/2026/03/03/rust-the-unlikely-engine-of-the-vibe-coding-era/)

生成摘要时出错

---

## 99. British Columbia is permanently adopting daylight time

**原文标题**: British Columbia is permanently adopting daylight time

**原文链接**: [https://www.cbc.ca/news/canada/british-columbia/b-c-adopting-year-round-daylight-time-9.7111657](https://www.cbc.ca/news/canada/british-columbia/b-c-adopting-year-round-daylight-time-9.7111657)

生成摘要时出错

---

## 100. Motorola announces a partnership with GrapheneOS

**原文标题**: Motorola announces a partnership with GrapheneOS

**原文链接**: [https://motorolanews.com/motorola-three-new-b2b-solutions-at-mwc-2026/](https://motorolanews.com/motorola-three-new-b2b-solutions-at-mwc-2026/)

生成摘要时出错

---

