# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-03-05.md)

*最后自动更新时间: 2026-03-05 19:12:02*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 2 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 3 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 4 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 5 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 6 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 7 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 8 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 9 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 10 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 11 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 12 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 13 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 14 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 15 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 16 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 17 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 18 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 19 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 20 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 21 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 22 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 23 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 24 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 25 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 26 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 27 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 28 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 29 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 30 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 31 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 32 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 33 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 34 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 35 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 36 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 37 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 38 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 39 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 40 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 41 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 42 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 43 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 44 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 45 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 46 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 47 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 48 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 49 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 50 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 51 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 52 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 53 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 54 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 55 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 56 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 57 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 58 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 59 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 60 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 61 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 62 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 63 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 64 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 65 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 66 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 67 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 68 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 69 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 70 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 71 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 72 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 73 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 74 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 75 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 76 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 77 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 78 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 79 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 80 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 81 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 82 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 83 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 84 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 85 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 86 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 87 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 88 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 89 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 90 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 91 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 92 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 93 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 94 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 95 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 96 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 97 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 98 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 99 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 100 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 101 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 102 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 103 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 104 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 105 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 106 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 107 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 108 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 109 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 110 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 111 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 112 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 113 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 114 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 115 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 116 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 117 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 118 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 119 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 120 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 121 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 122 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 123 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 124 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 125 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 126 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 127 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 128 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 129 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 130 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 131 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 132 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 133 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 134 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 135 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 136 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 137 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 138 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 139 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 140 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 141 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 142 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 143 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 144 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 145 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 146 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 147 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 148 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 149 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 150 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 151 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 152 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 153 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 154 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 155 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 156 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 157 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 158 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 159 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 160 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 161 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 162 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 163 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 164 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 165 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 166 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 167 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 168 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 169 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 170 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 171 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 172 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 173 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 174 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 175 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 176 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 177 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 178 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 179 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 180 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 181 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 182 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 183 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 184 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 185 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 186 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 187 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 188 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 189 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 190 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 191 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 192 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 193 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 194 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 195 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 196 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 197 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 198 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 199 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 200 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 201 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 202 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 203 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 204 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 205 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 206 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 207 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 208 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 209 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 210 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 211 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 212 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 213 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 214 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 215 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 216 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 217 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 218 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 219 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 220 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 221 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 222 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 223 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 224 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 225 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 226 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 227 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 228 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 229 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 230 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 231 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 232 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 233 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 234 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 235 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 236 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 237 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 238 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 239 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 240 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 241 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 242 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 243 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 244 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 245 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 246 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 247 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 248 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 249 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 250 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 251 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 252 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 253 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 254 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 255 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 256 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 257 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 258 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 259 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 260 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 261 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 262 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 263 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 264 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 265 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 266 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 267 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 268 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 269 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 270 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 271 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 272 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 273 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 274 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 275 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 276 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 277 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 278 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 279 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 280 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 281 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 282 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 283 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 284 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 285 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 286 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 287 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 288 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 289 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 290 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 291 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 292 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 293 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 294 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 295 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 296 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 297 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 298 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 299 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 300 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 301 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 302 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 303 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 304 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 305 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 306 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 307 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 308 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 309 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 310 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 311 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 312 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 313 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 314 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 315 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 316 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 317 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 318 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 319 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 320 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 321 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 322 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 323 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 324 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 325 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 326 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 327 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 328 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 329 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 330 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 331 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 332 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 333 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 334 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 335 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 336 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 337 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 338 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 339 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 340 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 341 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 342 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 343 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 344 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 345 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 346 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 347 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 348 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 349 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 350 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
