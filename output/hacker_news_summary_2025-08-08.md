# Hacker News 热门文章摘要 (2025-08-08)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. GPT-5 vs. Sonnet：复杂自主编码

**原文标题**: GPT-5 vs. Sonnet: Complex Agentic Coding

**原文链接**: [https://elite-ai-assisted-coding.dev/p/copilot-agentic-coding-gpt-5-vs-claude-4-sonnet](https://elite-ai-assisted-coding.dev/p/copilot-agentic-coding-gpt-5-vs-claude-4-sonnet)

本文对比了 GPT-5（新发布并集成至 GitHub Copilot）和 Claude 4 Sonnet 在执行复杂自主编码任务方面的能力。作者要求两模型将一个名为 Ruler 的 TypeScript 工具移植到 Rust，重点考察它们的智能性、自主性、代码质量和对指令的遵循程度。

GPT-5 令人印象深刻，其规划能力、对上下文的理解能力以及以最少的提示执行复杂任务的能力（“自主性”）都很出色。它创建了一个完整且功能正确的移植版本，但生成的代码杂乱无章，结构性差。它遇到了一些需要重启的技术问题。

Claude 4 Sonnet 更快且更具沟通性，产生了优雅且结构良好的代码。 然而，它不太严谨，更倾向于即兴发挥，并非总是精确地遵循指令。它还给出了不可靠的状态更新，并且没有完全完成任务。

强调的关键差异：GPT-5 在前期进行了更多思考，执行准确但结构较差； Claude 尝试不同的方法，犯错但会恢复，并创建优美的代码。 GPT-5 更好地遵循指令，而 Claude 则进行即兴发挥。

作者还讨论了 GitHub Copilot Chat 的改进，但指出对终端命令进行手动批准的需求阻碍了完全自主运行。他们赞赏 Copilot 基于请求而非令牌的定价模型。

最终，两款模型的表现都很好，其中 GPT-5 在智能和任务理解方面表现出色，而 Claude 在代码优雅性和交互性方面表现出色。作者对 GPT-5 在编码方面的潜力持乐观态度。文章的附言指出，Copilot 具有一个实验性的自动批准命令功能，解决了对持续手动批准的需求。

---

## 2. 超薄名片运行流体模拟

**原文标题**: Ultrathin business card runs a fluid simulation

**原文链接**: [https://github.com/Nicholas-L-Johnson/flip-card](https://github.com/Nicholas-L-Johnson/flip-card)

此仓库记录了“翻转卡片”项目，这是一种独特的名片，集成了实时流体模拟。该项目灵感来源于类似作品，特别是流体模拟吊坠。

仓库包含：

*   **PCB设计文件 (kicad-pcb):** 名片硬件的原理图和布局。
*   **流体模拟Crate (fluid\_sim\_crate):** 一个独立的Rust crate，实现了FLIP (Fluid-Implicit-Particle) 流体模拟算法。 这基于Matthias Müller的工作。
*   **USB-C充电:** 利用板边USB-C端口设计进行充电，改编自另一个项目。
*   **WASM模拟器 (sim\_display):** 一个模拟器，允许在Web浏览器环境中调试流体模拟。
*   **RP2350固件 (flip-card\_firmware):** 为RP2350微控制器实现的固件，该固件在名片上运行流体模拟。

该项目成功地集成了硬件和软件，创造出功能强大且视觉上有趣的名片，展示了实时流体模拟。 更多详细信息可在每个文件夹的README文件中找到。

---

## 3. AI必须RTFM：为何技术写作者正成为上下文管理者

**原文标题**: AI must RTFM: Why tech writers are becoming context curators

**原文链接**: [https://passo.uno/from-tech-writers-to-ai-context-curators/](https://passo.uno/from-tech-writers-to-ai-context-curators/)

人工智能崛起正将技术文档撰写者的角色转变为“语境策展人”。作者观察到，开发者越来越重视文档编写，并以一种人工智能工具能够轻松理解和利用的方式对其进行结构化。这种“文档驱动开发”需要技术文档撰写领域发生转变。

文章解释了大型语言模型 (LLM) 如何依赖其输入的质量来生成准确且有用的输出。随着开发者越来越意识到向 LLM 提供正确信息的重要性，对结构化和相关语境的需求也在增加。这就是“语境策展人”发挥作用的地方：一位战略性地组织内容，使其既能供人类又能供人工智能使用的技术文档撰写者。

作者设想技术文档撰写者将在人工智能驱动的文档流程中发挥主导作用，包括语境的策展。这包括制作可插入人工智能驱动的代码编辑器的文档盒，为 LLM 提供必要的知识来帮助开发者。他们提倡创建“LLM 优化”的文档格式，并有可能振兴像 DITA 这样的结构化标记语言。

最终目标是使人类和人工智能都能访问内容，从而使他们能够提取定制的知识。作为语境策展人，技术文档撰写者引导用户理解复杂的信息，帮助他们有效理解和利用这些信息。这种演变代表了技术文档撰写者作为软件开发过程中多才多艺且不可或缺的角色又一次扩展。

---

## 4. 谷歌的Genie比GPT5更令人印象深刻。

**原文标题**: Google's Genie is more impressive than GPT5

**原文链接**: [https://theahura.substack.com/p/tech-things-genies-lamp-openai-cant](https://theahura.substack.com/p/tech-things-genies-lamp-openai-cant)

无法访问文章链接。

---

## 5. Tor：军方项目如何成为隐私保护的生命线

**原文标题**: Tor: How a Military Project Became a Lifeline for Privacy

**原文链接**: [https://thereader.mitpress.mit.edu/the-secret-history-of-tor-how-a-military-project-became-a-lifeline-for-privacy/](https://thereader.mitpress.mit.edu/the-secret-history-of-tor-how-a-military-project-became-a-lifeline-for-privacy/)

本·科利尔的文章《Tor：一项军事项目如何成为隐私的生命线》探讨了Tor的起源和意义。Tor是一种增强隐私的技术，通常与暗网相关联。这篇文章追溯了Tor的发展历程，始于美国海军研究实验室，那里的研究人员试图创建一个安全的通信网络，以隐藏互联网流量的来源和目的地。

这催生了洋葱路由的诞生，数据在多个层中加密并通过中继网络传输，从而难以追踪。为了获得广泛采用，军方研究人员与密码朋克（一群激进的黑客，倡导通过加密保护隐私）合作。

科利尔认为，Tor的存在揭示了对隐私的复杂理解，这种理解是由不同权力结构的互动塑造的。他批评了将隐私技术仅仅定义为促成犯罪活动的说法，并指出它们在保护弱势群体免受国家监视方面的重要性。文章以英国的《在线安全法案》为例，暗示该法案可能会以保护为幌子破坏妇女和儿童的安全。

科利尔总结说，在在线生活日益中心化和不负责任的AI系统崛起的时代，像Tor这样的工具至关重要。他提倡重建对社会机构的信任以解决损害，而不是依赖于侵蚀个人自由的监视技术。

---

## 6. HorizonDB，一个用 Rust 编写的、替代 Elasticsearch 的地理编码引擎

**原文标题**: HorizonDB, a geocoding engine in Rust that replaces Elasticsearch

**原文链接**: [https://radar.com/blog/high-performance-geocoding-in-rust](https://radar.com/blog/high-performance-geocoding-in-rust)

Radar公司开发了HorizonDB，一个用Rust编写的地理空间数据库，以取代之前基于Elasticsearch和MongoDB的地理编码架构。其动机在于提高效率、运营和开发者体验，同时处理大量的地理位置API调用。

HorizonDB通过将多个位置服务整合到一个高性能的二进制文件中来实现这一目标。它每个核心可以处理1,000 QPS，保持低延迟的地理编码，并在通用硬件上实现线性扩展。

该系统利用了以下几项关键技术：

*   **Rust:** 用于性能、内存安全和高效的并发。
*   **RocksDB:** 作为主要的快速记录存储。
*   **S2:** 用于空间索引和快速的点在多边形内查找。
*   **FSTs:** 用于缓存常用查询和压缩字符串。
*   **Tantivy:** 一种用于提高搜索召回率的进程内倒排索引。
*   **FastText:** 用于词语的语义表示和拼写容错。
*   **LightGBM:** 用于查询意图分类和结构化。
*   **Apache Spark:** 用于预处理大型数据集。

通过采用HorizonDB，Radar公司显著改进了其地理位置服务，从而实现了更快的性能、更简单的运营、更快的数据摄取，并通过停用MongoDB和Elasticsearch集群节省了成本。该团队已准备好持续扩展，并计划在未来的文章中详细阐述具体的功能设计。

---

## 7. 2025年度天文摄影师大赛入围名单

**原文标题**: Astronomy Photographer of the Year 2025 shortlist

**原文链接**: [https://www.rmg.co.uk/whats-on/astronomy-photographer-year/galleries/2025-shortlist](https://www.rmg.co.uk/whats-on/astronomy-photographer-year/galleries/2025-shortlist)

2025年度ZWO天文摄影师大赛入围名单揭晓，展示了来自世界各地的天文现象的惊艳影像。今年是第17届比赛，收到了创纪录的参赛作品数量，共有来自68个国家的5880多张照片提交。

入围作品主题多样，包括上海的血月、挪威的北极光、中国的银河、巨大的太阳耀斑爆发、仙女座星系的详细景象以及一颗彗星掠过夏威夷。其他亮点包括展示我们太阳系行星的创意构图以及月亮在各种景观上方的升起。

文章简要描述了几个入围作品，注明了摄影师，并详细介绍了拍摄地点和使用的技术。获奖者和亚军将于9月11日在网上颁奖典礼上公布。

此外，该页面还宣传了比赛的摄影集、历届获奖者以及相关文章，探索了诸如日食、宜居行星、天文摄影社区以及格林威治皇家天文台的历史等主题。文章还提到了在国家海事博物馆举行的比赛展览，展期至8月11日。

---

## 8. 苹果的历史藏在Mac字体中

**原文标题**: Apple's history is hiding in a Mac font

**原文链接**: [https://www.spacebar.news/apple-history-hiding-in-mac-font/](https://www.spacebar.news/apple-history-hiding-in-mac-font/)

文章“苹果的历史隐藏在Mac字体中”探讨了2003年在macOS Panther (10.3) 中引入的 Apple Symbols 字体如何成为苹果过去令人惊讶的时间胶囊。与 Windows 不同，macOS 积极更新和重新设计其核心，使得传统元素非常罕见。

Apple Symbols 字体虽然在很大程度上已被 SF Symbols 取代，用于现代图标，但仍然存在于 macOS Sequoia 15.1 中。它包含 4400 个字形，比原始 Panther 版本的 1224 个字形有了显著增加。虽然许多字形是通用的，但该字体因其 Apple 特有的图像和符号集合而引人注目，充当了过时技术和设计的存储库。

在该字体中发现的遗物包括 Apple Newton PDA（包括其灯泡标志和系统图标）、原始 Macintosh、ADB、AppleTalk、软盘、SCSI 甚至原始 QuickTime 标志（早于更熟悉的蓝色 Q）的图标。它还包含现已弃用的技术（如 PowerPC（Mac 从 1994 年到 2006 年使用的 CPU 架构）和 FireWire）的符号，以及与 CRT 显示器相关的监视器控件（Apple 于 2000 年停产）。甚至可以找到 Boot Camp 标志。

作者认为，令人惊讶的是，苹果公司保留了这个包含历史文物的字体，而 Windows 也包含类似的隐藏复古图标。这款字体可以通过 Mac 上的“字体册”应用程序访问，可以独特地了解苹果的演变及其被遗忘的技术。

---

## 9. HRT的Python分支：利用PEP 690加速导入

**原文标题**: HRT's Python Fork: Leveraging PEP 690 for Faster Imports

**原文链接**: [https://www.hudsonrivertrading.com/hrtbeat/inside-hrts-python-fork/](https://www.hudsonrivertrading.com/hrtbeat/inside-hrts-python-fork/)

本文可能探讨了HRT创建Python分支以充分利用PEP 690（该提案为CPython解释器引入了惰性导入）的举措。总结将重点介绍HRT希望实现的好处以及他们的方法的含义。

以下是一个可能的总结：

HRT创建了一个CPython分支，以充分利用PEP 690的惰性导入，从而显著改善Python应用程序的启动时间。PEP 690允许仅在实际需要模块的符号时才导入模块，而不是在导入时立即导入，从而减少了初始加载和解析开销。

HRT的分支可能采用了激进的惰性导入策略和基于PEP 690基础之上的自定义优化。这可能涉及修改标准库以及潜在的导入机制本身，以最大限度地提高惰性加载的影响。

这种方法的潜在好处包括更快的应用程序启动时间、启动期间减少的内存占用以及命令行工具和无服务器函数的改进的响应能力。本文可能探讨了HRT观察到的具体性能提升以及他们在实施和维护此Python分支版本时遇到的挑战。它还可能讨论所涉及的权衡，例如与兼容性相关的潜在问题以及保持分支与上游CPython同步所需的持续努力。

---

## 10. 从 Claude 代码获得良好结果

**原文标题**: Getting good results from Claude code

**原文链接**: [https://www.dzombak.com/blog/2025/08/getting-good-results-from-claude-code/](https://www.dzombak.com/blog/2025/08/getting-good-results-from-claude-code/)

本文概述了基于作者构建多个项目的经验，有效使用 LLM 编程助手 Claude Code 的策略。作者强调，清晰的规范至关重要，同时还需要一份详细说明项目结构、构建过程和代码检查的文件。一个令人惊讶的好处是，该助手可以自我审查其代码。一个自定义的“全局”助手指南，定义了最佳实践（增量进展、从代码中学习、简洁、TDD）也很关键。该指南强调计划、测试和错误处理。

作者强调验证 LLM 编写代码的重要性。他们认为人工审查和测试对于确保正确性并防止效率低下至关重要。他们添加测试用例，无论是手动添加还是通过提示 LLM 添加，并在合并之前审查所有 AI 生成的代码。

作者包含在本文中的“全局”助手指南涵盖了开发理念、过程（计划、测试驱动开发、重构）、技术标准（架构、代码质量、错误处理）、决策框架、项目集成和质量关口（完成的定义、测试指南）。关键原则包括优先考虑可测试性、可读性、简洁性以及与现有项目模式的一致性。该指南还包括避免走捷径和始终提交可运行代码的具体提醒。

---

## 11. 语音控制集群

**原文标题**: Voice Controlled Swarms

**原文链接**: [https://jasonfantl.com/posts/Voice-Controlled-Swarms/](https://jasonfantl.com/posts/Voice-Controlled-Swarms/)

本文详细介绍了一个受《安德的游戏》启发的项目，该项目旨在创建语音控制的模拟智能体集群。该方法涉及使用语音转文本程序将口头指令翻译成大型语言模型（LLM）的指令，然后由LLM指导集群。

该项目分为两个部分。首先，创建一个通用的语音控制器，该控制器可以与任何支持模型上下文协议（MCP）的应用程序交互。作为演示，该控制器用于通过语音命令在画布上操作形状。这展示了语音控制智能体的可重用性。

第二部分侧重于集群模拟本身。单个智能体（boid）使用改进的boids算法进行控制，强调集群之间的分离和混乱的对齐。主要功能包括将集群分配到特定位置、跟随物体以及导航至航点。还实现了分裂（fork）和合并集群的能力，以及基于分配问题（或最小成本流问题）的“位置感知”无人机分配算法，以提高视觉效果。

禁飞区、环绕行为、地标、语音ID和坐标网格等附加功能增强了模拟的可用性。最后，本文介绍了LLM智能体可用于控制集群的全部工具集，并演示了语音控制的实际应用。该项目的代码可在GitHub上找到。

---

## 12. 我们构建了一个开源的异步编码代理。

**原文标题**: We built an open-source asynchronous coding agent

**原文链接**: [https://blog.langchain.com/introducing-open-swe-an-open-source-asynchronous-coding-agent/](https://blog.langchain.com/introducing-open-swe-an-open-source-asynchronous-coding-agent/)

Open SWE 是一款开源的异步编码代理，旨在作为软件开发中的协作伙伴。它托管在云端，直接与 GitHub 仓库集成，并使用自定义 UI，使用户能够通过 GitHub issue 委托任务。

Open SWE 模仿人类工程师的工作流程，包括研究代码库、创建执行计划、编写代码、运行测试、审查自己的工作，并在完成后打开 pull request。其主要功能包括：能够在运行过程中中断并提供反馈、与 GitHub 的无缝集成（包括 issue 跟踪和 PR 生成），以及用于安全执行的隔离沙箱环境。

该代理采用多代理架构，包含 Manager、Planner、Programmer 和 Reviewer。 Planner 制定详细的执行计划（可选人工审核），Programmer 执行代码，Reviewer 确保代码质量和正确性。它运行在 LangGraph 和 LangGraph Platform 上，并使用 LangSmith 进行可观察性和评估。

虽然 Open SWE 对于复杂任务非常有效，但目前不太适合简单的单行修复。一个基于 CLI 的版本正在开发中，旨在解决这个问题，使 Open SWE 成为适用于所有工程任务的全面解决方案。

---

## 13. 窗口激活

**原文标题**: Window Activation

**原文链接**: [https://blog.broulik.de/2025/08/on-window-activation/](https://blog.broulik.de/2025/08/on-window-activation/)

本文探讨了从X的“强制焦点”窗口激活到Wayland更安全的XDG激活协议的过渡。在Wayland中，应用程序不能简单地窃取焦点；它们必须通过令牌系统*请求*激活才能将它们的窗口置于最前面。

该过程涉及应用程序从合成器请求激活令牌，然后将此令牌传递给目标应用程序（通常通过环境变量或DBus）。目标应用程序使用该令牌请求激活，但如果令牌无效或请求看起来可疑，合成器仍然可以拒绝该请求。

本文强调，有效的令牌并不能保证激活；合成器会使用有关请求表面的信息、输入事件和应用程序ID来确定合法性并防止不必要的焦点窃取。Qt、KDE Frameworks和许多应用程序已经更新以处理这种新的工作流程，自动请求或利用激活令牌。

作者指出，与X不同，X的焦点窃取预防是基于启发式方法且容易被绕过，Wayland强制执行更严格的控制。为了帮助开发人员确保他们的应用程序行为正确，本文建议使用启用“极端”焦点窃取预防的KWin。最近的修复解决了Dolphin、KRunner、LayerShell-Qt和特权客户端中的问题。DBusRunner规范以及Baloo、KClock、最近文档和位置的运行程序也得到了进一步的改进。最终目标是在Wayland上启用KWin的焦点窃取预防，并随着更多应用程序更新以正确使用XDG激活而逐步提高其严格性。

---

## 14. Linear把我带进了本地优先的兔子洞。

**原文标题**: Linear sent me down a local-first rabbit hole

**原文链接**: [https://bytemash.net/posts/i-went-down-the-linear-rabbit-hole/](https://bytemash.net/posts/i-went-down-the-linear-rabbit-hole/)

本文详细介绍了作者对“本地优先”Web应用程序架构的探索，灵感来源于项目管理工具Linear的速度和响应能力。“本地优先”优先将数据存储在客户端设备本地，然后与服务器同步，颠覆了传统的Web应用程序模式，即服务器是真理的来源。这种方法消除了网络延迟，从而实现即时UI更新。

作者强调了构建本地优先应用程序的复杂性，列举了诸如离线支持、冲突解决、部分同步和安全性等挑战。然后，他们调查了当前本地优先工具的现状，包括Electric SQL、PowerSync、Jazz、Replicache、Zero、Triplit、Instant和LiveStore。

本文深入探讨了Jazz，这是一个通过“协作值”（CoValues），即自动同步的数据结构，承诺易于使用的框架。Jazz利用内置唯一性、事件溯源、端到端加密和基于组的权限等技术。然而，Jazz也有其权衡之处，包括由于加密导致的盲后端、由于事件溯源导致的强制时间旅行，以及潜在的高存储成本。

作者还讨论了Electric SQL和Zero，它们通过与现有的Postgres数据库配合使用，采取了一种渐进式的方法。最后，本文概述了本地优先架构的适用和具有挑战性的用例，强调其在创意工具、协作应用程序、支持离线的移动应用程序和开发者工具中的优势，同时警告不要将其用于需要大量服务器端逻辑、严格审计或大规模分析的场景。作者总结说，虽然该生态系统还很年轻，但本地优先的用户体验优势是不可否认的，并鼓励在新项目中进行实验。

---

## 15. 人工智能令人印象深刻，是因为我们在个人计算方面失败了。

**原文标题**: AI is impressive because we've failed at personal computing

**原文链接**: [https://rakhim.exotext.com/ai-is-impressive-because-we-ve-failed-at-semantic-web-and-personal-computing](https://rakhim.exotext.com/ai-is-impressive-because-we-ve-failed-at-semantic-web-and-personal-computing)

本文认为，人工智能（AI），特别是像ChatGPT这样的大型语言模型（LLM）的成功，部分原因是我们在创建有效的个人和网络信息组织系统方面的失败。作者指出，简单的搜索引擎难以处理ChatGPT可以轻松回答的复杂查询。这归因于互联网的非结构化特性以及从结构化HTML到动态JavaScript的转变，阻碍了机器的可读性。

作者批评了优先考虑搜索功能（包括传统搜索和人工智能驱动的搜索）而非结构化组织的趋势。例子包括谷歌云盘(Google Drive)的乏善可陈的文件管理，以及在电子商务和用户文档中分别依赖搜索栏和聊天机器人的做法。他们感叹语义网未能实现，导致依赖蛮力AI从非结构化数据中推断结构。

本文将此与个人计算的潜力进行了对比，后者被设想为具有结构化语义连接的个性化知识库。作者认为，如果信息能够更好地组织和进行语义链接，那么更简单的自然语言处理（NLP）算法可以用更少的计算能力来回答复杂的问题。最终，作者认为人工智能的成功在于它能够从互联网的混乱中导航和提取意义，而这种混乱是由我们集体未能优先考虑结构和组织造成的。因此，人工智能被视为一种变通方法，而不是一种优雅的解决方案。

---

## 16. Show HN: Synchrotron，纯 Python 实现的实时 DSP 引擎

**原文标题**: Show HN: Synchrotron, a real-time DSP engine in pure Python

**原文链接**: [https://synchrotron.thatother.dev/](https://synchrotron.thatother.dev/)

这个“Show HN”帖子介绍了 Synchrotron，一个完全用 Python 构建的实时数字信号处理 (DSP) 引擎。关键在于它是一个基于 Python 的实时音频和其他信号处理解决方案。该帖子强调提供了一个用户界面，表明它具有一个可视化组件，用于与 DSP 引擎进行交互和控制。

本质上，Synchrotron 旨在提供一个灵活且易于访问的平台，以便使用广泛采用的 Python 编程语言进行 DSP 实验和应用。这可能具有易于使用、快速原型设计以及与现有 Python 库集成等优势。通过实现实时性，它表明适用于实时音频处理、交互式装置以及其他需要立即响应的应用。用户界面的提及进一步强调了设计和管理 DSP 工作流程的易用性和用户友好性。

---

## 17. Show HN: Trayce – 开发者专用“Burp Suite”

**原文标题**: Show HN: Trayce – “Burp Suite for developers”

**原文链接**: [https://trayce.dev?resubmit=hn](https://trayce.dev?resubmit=hn)

Trayce被定位为“开发者版的Burp Suite”，它是一款用于监控本地Docker容器内网络流量的工具。它提供轻量且快速的UI（非Electron，非基于浏览器）来跟踪HTTP、HTTPS（适用于Go和基于OpenSSL的语言）、GRPC、MySQL和Postgres协议。它强调离线功能，使用本地`.bru`文件存储HTTP请求，使用户能够将请求组织成集合和文件夹。

主要功能包括变量重用、环境变量切换以及在`.env`文件中安全存储密钥。Trayce通过一个专用的`TrayceAgent`容器实现容器监控，该容器利用eBPF探针来拦截网络请求并在GUI中显示。

Trayce面向后端开发者、QA工程师以及在本地使用Docker容器的测试人员，明确声明不适用于生产环境监控。目前提供Mac和Linux（deb包）的下载，并计划推出RPM和Windows版本。源代码也可供构建。

---

## 18. 电话新闻报：1893年电子收听新闻与音乐

**原文标题**: Telefon Hírmondó: Listen to news and music electronically, in 1893

**原文链接**: [https://en.wikipedia.org/wiki/Telefon_H%C3%ADrmond%C3%B3](https://en.wikipedia.org/wiki/Telefon_H%C3%ADrmond%C3%B3)

电话新闻报：世界首个电话新闻服务

---

## 19. 过度设计我的家庭实验室，这样我就不用花钱给云服务商了。

**原文标题**: Overengineering my homelab so I don't pay cloud providers

**原文链接**: [https://ergaster.org/posts/2025/08/04-overegineering-homelab/](https://ergaster.org/posts/2025/08/04-overegineering-homelab/)

本文详述了作者为避免依赖云服务提供商，通过使用一台迷你PC和Proxmox虚拟环境（PVE）在家自托管服务，从而“过度设计”其家庭实验室的旅程。作者概述了他们的目标，包括安全地进行虚拟机实验，探索Kubernetes，以及通过磁盘加密、备份和自动化设置来缓解诸如盗窃和硬件故障等威胁。

该设置的核心是在Debian之上安装Proxmox，利用其灵活性来创建和管理虚拟机。作者在Proxmox安装过程中遇到了一个障碍，即在安装PVE软件包后系统无法启动。经过调查，他们发现需要静态IP配置。

本文进一步描述了作者计划如何使用Opentofu (Terraform) 将虚拟机配置定义为代码，并使用cloud-init来预配置虚拟机。然后将使用Ansible来管理虚拟机的所需状态，确保配置的一致性。作者提供了Opentofu和Ansible代码片段的示例，演示了虚拟机的创建和配置。

作者还详细介绍了在Proxmox中设置桥接网络的过程，使虚拟机能够利用主机的网卡。为了简化流程并确保可重复性，作者正在使用Ansible自动化整个Proxmox安装过程。本文重点介绍了设置稳定Proxmox hypervisor的初始阶段，并暗示了未来文章将涵盖使用Opentofu、cloud-init和Ansible进行虚拟机部署和配置。

---

## 20. 注意力沉没如何保持语言模型的稳定性

**原文标题**: How Attention Sinks Keep Language Models Stable

**原文链接**: [https://hanlab.mit.edu/blog/streamingllm](https://hanlab.mit.edu/blog/streamingllm)

本文详细介绍了语言模型（LLMs）中“注意力陷阱”的发现及其影响。它解释了作者肖广轩在 Meta 实习期间，如何解决使 LLMs 能够处理长对话而无需二次计算成本的问题。最初尝试使用滑动窗口方法，丢弃旧的 token，导致了灾难性的模型失败。

关键发现是 LLMs 依赖于特定的初始 token，称为“注意力陷阱”，来吸收未使用的注意力，因为 softmax 函数强制注意力权重总和为 1。移除这些陷阱会破坏模型的稳定性，导致输出乱码。

解决方案 StreamingLLM 包括永久保留前几个 token（充当注意力陷阱），同时为剩余的上下文维护一个滑动窗口。这使得模型能够稳定地处理数百万个 token，比其训练上下文大几个数量级。然后，本文探讨了所需的陷阱 token 数量，揭示了使用专用陷阱 token 进行预训练效率更高。

本文讨论了 OpenAI 在其 GPT-OSS 模型中采用类似机制的情况，进一步强调了注意力陷阱的重要性。此后的研究表明，注意力陷阱充当“压力阀”，防止“过度混合”并稳定嵌入。实际应用包括改进模型量化和减少激活异常值。最后，作者详细介绍了英特尔、HuggingFace、英伟达和 OpenAI 迅速采用 StreamingLLM 的情况，展示了这一发现对 LLMs 领域的重大影响。

---

## 21. Flipper Zero 黑网固件绕过滚动码安全机制

**原文标题**: Flipper Zero dark web firmware bypasses rolling code security

**原文链接**: [https://www.rtl-sdr.com/flipperzero-darkweb-firmware-bypasses-rolling-code-security/](https://www.rtl-sdr.com/flipperzero-darkweb-firmware-bypasses-rolling-code-security/)

Flipper Zero 新固件可绕过滚动码安全系统，模拟车辆遥控器。与难以实现的 RollJam 攻击不同，该方法无需干扰原始信号，仅需一次按键捕获即可完整模拟钥匙。攻击通过逆向工程滚动码序列或利用“回滚”攻击方法（以特定顺序重放捕获的代码）实现。结果是仅捕获一个代码后，即可完整模拟遥控钥匙功能（锁定、解锁、后备箱释放）。缺点是原始钥匙会失去同步并停止工作。受影响的车辆品牌包括克莱斯勒、道奇、菲亚特、福特、现代、吉普、起亚、三菱和斯巴鲁。文章建议，鉴于安全漏洞的严重性，大规模召回车辆可能是一种潜在的解决方案。

---

## 22. GPT-5

**原文标题**: GPT-5

**原文链接**: [https://openai.com/gpt-5/](https://openai.com/gpt-5/)

无法访问文章链接。

---

## 23. 历史科技树

**原文标题**: Historical Tech Tree

**原文链接**: [https://www.historicaltechtree.com/](https://www.historicaltechtree.com/)

无法访问文章链接。

---

## 24. 食物、住房和医疗保健费用是许多人压力的主要来源。

**原文标题**: Food, housing, & health care costs are a source of major stress for many people

**原文链接**: [https://apnorc.org/projects/food-housing-and-health-care-costs-are-a-source-of-major-stress-for-many-people/](https://apnorc.org/projects/food-housing-and-health-care-costs-are-a-source-of-major-stress-for-many-people/)

美国民众因食品、住房和医疗等基本生活成本上涨而倍感压力。2025年7月的一项民意调查显示，53%的成年人认为食品开支是主要压力来源，约一半的人同样担心住房成本。医疗保健费用也是40%成年人的主要压力源。总的来说，75%的成年人表示至少因上述一项经济因素而感到巨大压力。

为了应对这些经济压力，29%的公众使用了“先买后付”（BNPL）服务，用于医疗、娱乐、食品杂货和餐饮等开支。BNPL的使用在年轻成年人（45岁以下）和承受更大经济压力的人群中更为普遍。例如，在感到巨大压力的人群中，有21%的人使用BNPL支付医疗或牙科费用，而在感到较小或没有压力的人群中，这一比例仅为8%。

与年长者相比，年轻成年人也报告了更高的收入、住房成本、学生债务和育儿方面的压力水平。虽然与食品杂货和医疗保健费用相关的压力水平在各个年龄段人群中具有可比性，但总体经济压力是普遍存在的。

这项由美联社-NORC公共事务研究中心进行的民意调查，在全国范围内调查了1437名成年人，总体抽样误差为+/- 3.6个百分点，18-29岁人群的抽样误差为+/- 6.6个百分点。调查结果突显了美国家庭日益增长的经济负担，以及对延期付款方式管理基本开支的日益依赖。

---

## 25. 弃税：在你的企业做大之前离开德国

**原文标题**: Exit Tax: Leave Germany before your business gets big

**原文链接**: [https://eidel.io/exit-tax-leave-germany-before-your-business-gets-big/](https://eidel.io/exit-tax-leave-germany-before-your-business-gets-big/)

本文探讨了德国的“离境税”，它可能会在经济上困住该国的企业家。作者认为，一旦企业盈利，离境税就会使所有者离开德国的成本高得令人望而却步。

离境税适用于在任何有限责任公司（包括外国公司）中持有超过 1% 股份的个人。它的计算基于公司过去三年平均收益，乘以 13.75，然后将该数字的 60% 按个人所得税税率（约 42%）征税。这实际上意味着将平均收益乘以约 3.5。

文章根据人们对离境税的脆弱性将其分为四类：员工（豁免）、不盈利公司的所有者（影响最小）、盈利公司的所有者（影响严重）和大型公司的所有者（足够富有可以使用税务漏洞）。

作者关注第三组，即盈利但规模不太大的企业的所有者。他提出了一些情景，表明一个适度盈利的企业如何导致巨大的离境税负担，可能超过企业家的储蓄。这阻碍了搬迁，即使是出于家庭或业务扩张等正当理由。

文章建议，在创业初期阶段的企业家应该考虑在他们的企业变得非常盈利或获得投资 *之前* 离开德国，因为离境税的计算使用高估值倍数或投资估值。作者建议，对公司价值的评估可能会导致较低的税收，但税收仍可能达到六位数。虽然更富有的人有可能通过复杂的金融策略来避免税收，但普通企业家实际上被“锁定”在德国。

在评论中，读者争论了税收的公平性，一些人认为这是收回基础设施投资的必要措施，而另一些人则认为它不公平地惩罚了企业家。

---

## 26. Show HN: Aha域名搜索

**原文标题**: Show HN: Aha Domain Search

**原文链接**: [https://www.ahadomainsearch.com/](https://www.ahadomainsearch.com/)

无法访问文章链接。

---

## 27. FLUX.1-Krea 与观点模型的崛起

**原文标题**: FLUX.1-Krea and the Rise of Opinionated Models

**原文链接**: [https://www.dbreunig.com/2025/08/04/the-rise-of-opinionated-models.html](https://www.dbreunig.com/2025/08/04/the-rise-of-opinionated-models.html)

本文探讨了Midjourney、Gemini和OpenAI等模型生成的AI图像中普遍存在的“AI感”，其特征是光泽感强的纹理、蜡质般的皮肤和过度的虚化效果。模型构建者Krea通过FLUX.1-Krea解决了这个问题，这是一款旨在避免这种通用美学的“主观”模型。

文章强调，目前的模型优先考虑正确性和基准优化，而不是美学。它们依赖于有偏差的美学评估器，如LAION Aesthetics，后者偏爱特定的风格和人群，并将不同的美学品味结合在一起，导致产生不吸引人的“平均”输出。

作者将FLUX.1-Krea与OpenAI的GPT-4.1进行了比较，使用了从真实照片生成的提示。结果表明，GPT-4.1产生的图像更接近提示的语言，但经常表现出不受欢迎的“AI感”，而FLUX.1-Krea则生成了更自然的图像。

文章认为，定性AI任务的未来在于具有特定美学偏好的主观模型，而不是试图普遍吸引人。随着后训练成本的降低，针对特定风格或动画工作室和制作公司内部使用的专业模型将变得越来越普遍。这种趋势也延伸到文本生成和聊天机器人应用程序。

作者欢迎这种专业化，因为它承认了AI模型中固有的偏见和设计选择，而不是将它们呈现为客观的机器。主观模型使这些美学和设计偏好变得明确。

---

## 28. 光标命令行

**原文标题**: Cursor CLI

**原文链接**: [https://cursor.com/cli](https://cursor.com/cli)

Cursor CLI 是一个命令行界面，旨在帮助开发者直接从终端提交代码，并与现有 IDE 和工作流程集成。它提供完全控制，允许用户审查代理编辑、进行代码更改并实时指导代理。自定义选项包括通过 AGENTS.md 和 MCP 设置规则。

该 CLI 提供对最新 AI 模型（如 GPT-5、Claude-4 (Sonnet and Opus) 和 Gemini 2.5 Pro）的访问，提供前沿功能。它支持与各种 IDE 的无缝集成，包括 Cursor、JetBrains、VSCode、Android Studio 和 IntelliJ。

除了简单的代码生成之外，Cursor CLI 还能够创建强大的脚本和自动化，从而促进自动更新文档、触发安全审查和构建自定义编码代理等任务。 要开始使用，用户可以使用提供的 curl 命令安装 CLI。 该界面展示了实时代码建议和编辑功能，展示了其在编码环境中的直接应用。

---

## 29. GPT-5：主要特性、定价和系统卡

**原文标题**: GPT-5: Key characteristics, pricing and system card

**原文链接**: [https://simonwillison.net/2025/Aug/7/gpt-5/](https://simonwillison.net/2025/Aug/7/gpt-5/)

本文第一手展示了预计将于2025年8月左右发布的新GPT-5模型系列。作者获得了提前访问权限，他将GPT-5描述为一个能干且可靠的LLM，它集成了各种专业模型，包括一个快速问答模型、一个用于复杂任务的推理模型以及一个基于提示需求选择适当模型的实时路由器。该API提供GPT-5的常规版、迷你版和纳米版，每个版本都有四个推理级别。

关键特性包括272,000个token的输入限制和128,000个token的输出限制，支持文本和图像输入。作者强调了GPT-5的通用能力和极少发生的错误。

GPT-5旨在取代大部分现有的OpenAI模型，擅长写作、编码和健康相关查询。音频、图像生成和实时音频模型继续由GPT-4o涵盖。

定价被描述为极具竞争力，GPT-5的输入token为每百万1.25美元，输出token为每百万10美元。Token缓存提供高达90%的折扣。

系统卡显示了在减少幻觉和谄媚方面的进展，并引入了“安全补全”功能，该功能会调节答案，而不是直接拒绝潜在有害内容。

虽然提示注入仍然是一个挑战，但与之前的模型相比，GPT-5显示出更高的抵抗力。该API包括访问“思考痕迹”的权限，以获取详细的推理摘要。

---

## 30. OpenAI新开源模型基本就是Phi-5

**原文标题**: OpenAI's new open-source model is basically Phi-5

**原文链接**: [https://www.seangoedecke.com/gpt-oss-is-phi-5/](https://www.seangoedecke.com/gpt-oss-is-phi-5/)

本文认为，OpenAI 新推出的开源模型 gpt-oss-120b 和 gpt-oss-20b，很可能采用了与微软 Phi 模型类似的方法进行训练，重点在于合成数据。作者指出，虽然这些模型在基准测试中可能表现良好，但由于缺乏广泛的真实世界知识，它们的实际性能可能令人失望，这与 Phi 模型的经验类似。

核心论点围绕着塞巴斯蒂安·布贝克（Sebastien Bubeck）的观点展开，他领导了微软 Phi 的开发，后来加入了 OpenAI，很可能影响了 gpt-oss 模型的训练。作者认为，OpenAI 出于安全原因选择了这条合成数据路线。开源模型存在通过微调而被滥用的风险，特别是用于有害或不当内容。通过在合成的、高度控制的数据上进行训练，OpenAI 可以先发制人地注入安全措施，并防止模型学习有害行为。

作者认为，OpenAI 在其开源版本中优先考虑了安全性和基准测试性能，而不是真正的实际效用。其目的是超越竞争对手的基准，同时避免引发丑闻，因为他们的核心业务依赖于闭源模型。文章总结说，gpt-oss 模型本质上是 OpenAI 版本的 Phi 系列，优先考虑安全性和基准测试成功，这可能会以牺牲更广泛的适用性为代价。

---

## 31. 面向开发者的Docker：必备命令速查表

**原文标题**: Docker for Developers: Essential Commands in One Cheatsheet

**原文链接**: [https://jsdev.space/docker-commands-cheatsheet/](https://jsdev.space/docker-commands-cheatsheet/)

本文旨在为开发者提供一份实用的速查表，以便快速掌握并运用必要的 Docker 命令，强调 Docker 作为与 Git 和 VS Code 齐名的基础工具的重要性。它侧重于实用命令而非理论，从而简化初学者和经验丰富的用户的学习过程。

本速查表涵盖：

*   **镜像：** 列出、拉取、删除、清理、查看历史记录和完整镜像信息。
*   **容器：** 列出（运行中和所有）、使用关键标志运行（分离模式、端口映射、卷挂载、名称、退出时删除、交互式终端、环境变量、网络）、启动、停止、重启、删除、查看日志、在内部执行命令、在主机和容器之间复制文件以及查看容器信息。
*   **Dockerfile 构建：** 构建镜像、特定平台构建、以及诸如标记、指定 Dockerfile 路径、禁用缓存和传递构建时变量等标志。
*   **Docker Compose：** 定义多容器设置、运行和构建服务、停止和删除、查看日志、在服务容器内执行以及其他有用的命令。
*   **网络：** 列出、创建、查看、连接和断开网络。
*   **卷：** 列出、创建、查看、删除和清理卷以实现数据持久性。

最后，它强调了开发人员的最佳实践，包括使用 `.dockerignore`、优化图层顺序以进行缓存、使用多阶段构建、避免以 root 身份运行、定期清理以及添加别名。它总结了速查表在赋能开发人员有效使用 Docker 方面的价值。

---

## 32. 咨询是做什么的？

**原文标题**: What Does Consulting Do?

**原文链接**: [https://www.nber.org/papers/w34072](https://www.nber.org/papers/w34072)

本NBER工作论文利用来自比利时（2002-2023年）的独特企业间交易数据集，对管理和战略咨询行业进行了全面的实证分析。该研究考察了咨询业务的性质、咨询客户以及对客户公司的影响。

主要发现包括：

* 咨询主要由大型、高劳动生产率的企业使用，高绩效和低绩效企业都会寻求咨询服务。新客户将其工资总额的约3%用于短期咨询，通常持续不到一年。
* 咨询对劳动生产率有积极影响，五年内提高了3.6%。这主要得益于就业人数的略微减少以及收入的稳定或增加。
* 平均工资提高了2.7%，而劳动在增加值中的份额没有下降，这表明生产率的提高并非通过转移工人的租金来实现的。研究观察到组织结构的调整，解雇率略有上升，服务采购增加，劳务外包减少。
* 最初生产率较低的公司在咨询后经历了更大的生产率提升，表明资源配置效率有所提高。
* 研究结果在很大程度上支持了咨询可以提高生产率的观点，这与接受调查的咨询专业人士和学术经济学家的期望相符。研究结果对咨询行业“租金转移”观点的支持较少。

---

## 33. ARM64上的虚拟Linux设备

**原文标题**: Virtual Linux Devices on ARM64

**原文链接**: [https://underjord.io/500-virtual-linux-devices-on-arm64.html](https://underjord.io/500-virtual-linux-devices-on-arm64.html)

Underjord的Lars Wikman详述了他使用Nerves（一个基于Elixir和Erlang BEAM的物联网框架）在一台192核的Ampere One ARM64服务器上运行大量虚拟Linux设备的实验。其目标是通过模拟大量并发的“真实”设备，来压力测试并展示Nerves和NervesHub的功能。

Wikman最初在为虚拟化环境配置u-boot时遇到了困难，但得到了Frank Hunleth的帮助，他提供了一个绕过引导加载程序问题的解决方案。他从一个基于IOT Gateway iMX8 Plus系统的定制Nerves系统开始，修改了Linux和Buildroot的配置。

Wikman成功地在该服务器上运行了500个虚拟设备，每个设备只占用一小部分核心，并将它们连接到NervesCloud。他计划通过优化启动程序和利用服务器的1TB内存，将这个数字推得更高，可能达到数千个。

他讨论了这项实验的价值，包括为Nerves的特性（如A/B更新）创建测试工具，方便针对虚拟板进行主机开发，以及可能在macOS上使用ARM虚拟化取代Nerves开发中的Docker。最后，他计划提高设备启动效率并探索KVM加速以提高性能，并旨在充分利用资源来确定硬件限制。

---

## 34. 什么是弹出提示？

**原文标题**: What Is Popover=Hint?

**原文链接**: [https://una.im/popover-hint/](https://una.im/popover-hint/)

本文介绍了 HTML 中新增的 `popover="hint"` 属性，该属性在 Chrome 133+ 版本中可用，以及实验性的 `[interestfor]` 属性，旨在简化工具提示和链接预览等分层 UI 元素的创建。

`popover="hint"` 允许打开一个提示性浮窗（如工具提示），而不会像 `popover="auto"` 那样关闭其他已打开的浮窗。虽然 `popover="hint"` 提供了基本功能，但最初仍需要 JavaScript 才能完全控制悬停和焦点行为。

实验性的 `[interestfor]` 属性提供了一种更具声明性的方法。它支持在“兴趣”事件（如悬停或聚焦）时触发提示性浮窗，这些事件发生在链接等元素上，而标准的 `popovertarget` 属性无法做到这一点（该属性仅支持按钮）。这使得双重操作元素成为可能，即点击执行一个操作（例如，导航到链接），而悬停显示提示。`[interestfor]` 需要在 Chrome Canary 中启用 "#experimental-web-platform-features" 标志。它还引入了新的 CSS 属性，如 `interest-show-delay` 和 `interest-hide-delay`，用于控制动画速度。

总而言之，`popover="hint"` 和 `[interestfor]` 旨在简化复杂的分层 UI 元素的创建，使其更易于访问和实现。作者提供了代码示例和演示链接，展示了这两个属性的功能。

---

## 35. LangChain开放软件工程

**原文标题**: Open SWE by LangChain

**原文链接**: [https://swe.langchain.com/](https://swe.langchain.com/)

鉴于提供的内容极其有限（“Open SWE by LangChain Loading (layout)...”），无法提供有意义的总结。 文章显然正在加载中，没有实际内容可用。

任何总结都纯粹是推测，仅基于标题。 例如，仅根据标题可能的（但未经证实的）总结可能是：

“Open SWE by LangChain 可能指的是与软件工程（SWE）相关的开源项目或倡议，该项目或倡议利用了 LangChain 框架。 它可能涉及旨在简化或自动化各种软件工程任务的工具、库或资源。 如果没有更多内容，则不可能知道该项目的具体细节、目标或目标受众。 该文章可能正在加载有关该项目的详细信息。”

然而，这纯粹是推测。 真正的总结需要文章的实际内容。

---

## 36. 为警用和军用无线电设计的加密可能很容易被破解。

**原文标题**: Encryption made for police and military radios may be easily cracked

**原文链接**: [https://www.wired.com/story/encryption-made-for-police-and-military-radios-may-be-easily-cracked-researchers-find/](https://www.wired.com/story/encryption-made-for-police-and-military-radios-may-be-easily-cracked-researchers-find/)

研究人员发现全球警察、军队和关键基础设施所用无线电加密存在漏洞。欧洲电信标准协会(ETSI)开发的原始TETRA加密标准于2023年被发现存在后门。为缓解此问题，ETSI建议使用端到端加密(E2EE)解决方案。现在，同一批研究人员发现，一种被ETSI认可的广泛使用的E2EE实现也存在弱点。

具体而言，所检查的E2EE算法以128位密钥开始，但在加密之前将其压缩到56位，从而使其更容易破解。此漏洞影响依赖额外安全性的执法机构、特种部队和秘密军事团队。

研究人员在Sepura无线电的E2EE中发现了该问题，发现了一个降密钥漏洞和另一个允许注入欺诈性消息或重放合法消息的漏洞，影响了TCCA的E2EE方案的所有用户。

ETSI承认该E2EE解决方案由TCCA开发，但他们密切合作。虽然用户可以部署不同的E2EE解决方案，但TCCA解决方案被广泛使用。 TEA1加密中的密钥缩减最初是为了符合出口管制，但现在安全性较低。

尽管Murgatroyd表示客户知情，但研究人员怀疑政府客户是否会在知晓系统已被削弱的情况下花费数百万美元。目前尚不清楚无线电制造商在密钥缩减方面对客户的透明度如何。

---

## 37. 为我的博客构建Bluesky评论系统

**原文标题**: Building Bluesky comments for my blog

**原文链接**: [https://natalie.sh/posts/bluesky-comments/](https://natalie.sh/posts/bluesky-comments/)

作者计划使用Bluesky为博客文章添加评论区，目前评论加载中，可能需要启用JavaScript。欢迎在Bluesky上参与讨论。

---

## 38. 将任何网站转换为API

**原文标题**: Turn any website into an API

**原文链接**: [https://www.parse.bot](https://www.parse.bot)

将任何网站变成API

本文简要介绍了将任何网站转化为API的概念，可能使用某种服务或工具来解析来自各种在线来源的数据。“将任何网站变成API”的标题直接传达了从网站以编程方式提取数据的核心思想。“解析 - 来自任何地方的数据”的副标题进一步强调了该解决方案的功能：解析数据，使其可访问和可用，并有可能从广泛的网站获取数据。

关键在于自动数据提取的潜力，无需手动复制和粘贴网站信息。此功能对于各种应用非常有用，包括数据分析、竞争研究、信息聚合以及构建依赖于网络实时数据的应用程序。该服务可能提供工具或方法来定义网页上的特定数据元素，然后定期自动检索这些元素，从而提供结构化且易于使用的API。这使得开发人员能够构建与几乎任何网站的内容动态交互和利用的应用，从而显著扩展了可用于其项目的数据源范围。

---

## 39. 致我未来雇主的一封情书 (2020)

**原文标题**: A love letter to my future employer (2020)

**原文链接**: [https://catzkorn.dev/blog/love-letter/](https://catzkorn.dev/blog/love-letter/)

一篇写给未来雇主的爱的情书（2020）：这篇博文记录了作者夏洛特在Makers预科课程第四周期间的情感历程和编码进展，该课程面向有抱负的软件开发人员。起初，夏洛特对自己的非传统背景感到自我怀疑和焦虑，质疑自己在教育领域工作十年并克服一场大病后，是否还有就业能力。她努力将自己的人生经历转化为简历上可销售的技能。

然而，她重新调整精力，渴望成为一名“优秀的软件工程师”。她认识到自己经历的价值，将其转化为解决问题、决心和适应能力等优势。夏洛特向职业教练寻求建议，意识到她可以用积极的态度来构建她的学术背景和生活经历。

这篇文章还详细介绍了夏洛特本周的编码经历。在一次结对任务中，她最初误解了测试驱动开发（TDD）的概念，但从错误中吸取了教训。她在独立编码项目中取得了成功，巩固了对所学概念的理解并建立了信心。她还在空闲时间探索了Go编程语言。

文章结尾，夏洛特带着一丝紧张、兴奋和决心迎接全日制Makers课程的开始。她设定了一个明确的结果目标，以保持脚踏实地，并为即将到来的高强度日程做准备，暗示未来几周可能需要紧急巧克力。

---

## 40. 滞胀将至美国。

**原文标题**: 'Stagflation is coming to the U.S.'

**原文链接**: [https://www.morningstar.com/news/marketwatch/20250808104/stagflation-is-coming-to-the-us-says-this-economist-heres-what-it-means-for-the-dollar-bonds-and-stocks](https://www.morningstar.com/news/marketwatch/20250808104/stagflation-is-coming-to-the-us-says-this-economist-heres-what-it-means-for-the-dollar-bonds-and-stocks)

QuantMetriks的Savvas Savouri预测美国将出现滞胀，其特征为通胀上升、美元走弱和收益率曲线陡峭。他将通胀压力归因于美元贬值、廉价劳动力受限和关税，认为关税的影响是滞后指标。他预计特朗普总统将施压美联储降息，可能导致央行行长更换，类似于日本和土耳其，最终削弱美元。

Savouri预计特朗普和中国之间将达成协议，允许人民币升值。他建议投资者购买通胀保值债券（TIPS）以抵御通胀。虽然他认为某些股票，尤其是具有国际收益的大型科技股，将受益于通胀，但他警告说，规模较小、以国内为重点且负有短期债务的公司将会陷入困境。

他不看好加密货币作为通胀对冲工具，但更喜欢黄金和澳元。文章还指出，美国股指期货走高，国债收益率下跌，美元指数走低，而油价正在上涨。最后，文章还涉及了一些时事，包括特朗普对美联储理事的提名、圣路易斯联储主席谈论银行业和信贷，以及围绕The Trade Desk、Expedia和SoundHound的新闻。

---

## 41. Claude 代码 IDE Emacs 集成

**原文标题**: Claude Code IDE integration for Emacs

**原文链接**: [https://github.com/manzaltu/claude-code-ide.el](https://github.com/manzaltu/claude-code-ide.el)

用于Emacs的Claude Code IDE通过模型上下文协议(MCP)在Emacs和Claude Code CLI之间提供深度集成，将Claude转变为一个Emacs感知的AI助手。它提供诸如自动项目检测、终端集成、MCP协议实现以及文件操作和工作区信息的工具支持等功能。

主要功能包括利用Emacs的LSP、Tree-sitter和Imenu等特性。任何Emacs命令都可以作为MCP工具公开，允许Claude执行项目范围内的搜索、访问专用模式并执行自定义Elisp函数。

安装需要Emacs 28.1+、Claude Code CLI以及vterm或eat。配置选项允许自定义终端后端（vterm或eat）、窗口管理（侧边窗口或常规窗口）以及自定义CLI标志。

该IDE为Claude Code CLI和Emacs日志记录提供了调试选项。它支持使用git worktree为不同的项目使用多个Claude Code实例。

Emacs MCP工具，例如xref-find-references、treesit-info和imenu-list-symbols，包含在内以增强代码导航和分析。可以创建自定义MCP工具以将特定的Emacs函数公开给Claude。

该项目根据GNU GPL v3.0或更高版本获得许可。

---

## 42. Foundry (YC F24) 招聘资深产品工程师

**原文标题**: Foundry (YC F24) is hiring staff-level product engineers

**原文链接**: [https://www.ycombinator.com/companies/foundry/jobs/jwdYx6v-founding-product-engineer](https://www.ycombinator.com/companies/foundry/jobs/jwdYx6v-founding-product-engineer)

Foundry (Y Combinator F24 孵化项目) 正在寻找一位创始产品工程师，以帮助构建基础架构，利用 AI 代理实现数字工作的自动化。他们的目标是创建一个类似 Waymo 的 “模拟器”，但用于基于浏览器的任务。该职位涉及构建逼真的浏览器模拟环境、设计 AI 可靠性评估系统、全栈平台开发（Python、Rust、Go、React/Next.js、TypeScript），以及负责整个产品生命周期。

理想的候选人拥有 6-10 年以上的全栈经验、深厚的系统知识（分布式系统、浏览器内部机制）、强大的编码能力（TypeScript、Python），并熟悉 Kubernetes、Docker 和云平台。拥有开源贡献或竞技编程荣誉的杰出记录者优先考虑。该公司正在寻找一位能够在模糊环境中自如工作并能够塑造基础产品的人。

Foundry 提供具有竞争力的薪酬和大量股权，有机会推动战略决策，并与来自 Scale AI 和 Meta 的团队合作。他们正在构建一个用于 Web 代理的评估和训练平台，专注于确定性 Web 模拟、实时 Web 评估、自动注释和标签，以及 RL 驱动的代理优化。他们的目标是帮助团队构建能够处理真实世界环境的可靠 Web 代理。

---

## 43. 年轻人住房市场是如何变成“一场彻底的灾难”

**原文标题**: How the Housing Market for Young People Became 'A Total Disaster'

**原文链接**: [https://www.derekthompson.org/p/how-the-housing-market-for-young](https://www.derekthompson.org/p/how-the-housing-market-for-young)

德里克·汤普森的文章《年轻人住房市场如何变成“一场彻底的灾难”》指出，年轻的美国人在负担住房方面面临着前所未有的挑战，影响着他们的生活、结婚率和整体经济前景。他赞同塔克·卡尔森的评估，认为这种情况是“一场彻底的灾难”。

汤普森概述了一个“嵌套式的麻烦历史”，由三个因素组成：始于20世纪70年代的限制性分区法规限制了住房供应的50年历史；大萧条对建筑业造成严重破坏的20年经济影响历史；以及新冠疫情在5年内超级刺激住房需求，同时扰乱供应链的历史。这些因素共同造成了一场完美风暴：高价格、因利率上升而昂贵的抵押贷款以及停滞的现有房屋销售。

他指出，住房负担能力现在是年轻选民最关心的问题，与老年选民对社会保障的关注程度相当。他批评唐纳德·特朗普提出的关税和移民限制等政策，认为这些政策加剧了问题。汤普森提倡一项全国性的“充裕议程”，通过“胡萝卜而非大棒”的方式激励各州和城市增加住房许可证。他还强调需要控制通货膨胀并减少国债，以降低长期抵押贷款利率。虽然承认危机的严重性，但汤普森在住房问题日益受到政治关注以及加利福尼亚州和纽约州最近的政策变化中找到了一线希望。他敦促民主党优先考虑住房负担能力，以重新获得年轻选民的支持。

---

## 44. 为Postgres编写存储引擎：一个内存表访问方法 (2023)

**原文标题**: Writing a storage engine for Postgres: An in-memory table access method (2023)

**原文链接**: [https://notes.eatonphil.com/2023-11-01-postgres-table-access-methods.html](https://notes.eatonphil.com/2023-11-01-postgres-table-access-methods.html)

本文是一篇关于为Postgres编写存储引擎的教程，特别是内存表访问方法(TAM)。它重点介绍了Postgres 12中引入的交换存储引擎的能力，类似于MySQL。作者认为，替代存储引擎对于不同的工作负载很有用，例如用于分析的列式存储和用于写入密集型任务的LSM树。使用TAM允许利用Postgres的基础设施（查询语言、线路协议等），同时自定义存储。

本文将TAM与外部数据包装器(FDW)进行对比，认为TAM提供更紧密的集成和潜在的更好性能。作者随后深入介绍了构建最小内存存储引擎的实际步骤。这包括设置Postgres的调试构建、创建必要的扩展基础设施（Makefile、控制文件、SQL文件）以及编写TAM的C代码。文章的核心在于提供必要文件的代码片段。至关重要的是，作者介绍了`TableAmRoutine`结构中缺少函数存根的初始错误，并提供了所有非可选方法的完整代码清单，使基本扩展能够加载而不会导致Postgres崩溃。该代码为构建更复杂的内存存储引擎提供了基础。

---

## 45. 使用高保真标签实现万倍训练数据缩减

**原文标题**: Achieving 10,000x training data reduction with high-fidelity labels

**原文链接**: [https://research.google/blog/achieving-10000x-training-data-reduction-with-high-fidelity-labels/](https://research.google/blog/achieving-10000x-training-data-reduction-with-high-fidelity-labels/)

该 Google Ads 文章介绍了一种新型主动学习方法，该方法能够显著减少为复杂分类任务微调 LLM 所需的训练数据量，特别是在识别不安全广告内容领域。作者 Markus Krause 和 Nancy Chang 证明，通过策略性地管理高质量数据，他们可以将训练数据需求减少高达 10,000 倍，同时提高模型与人类专家的对齐程度。

他们的方法首先使用零样本或少样本 LLM (LLM-0) 在海量数据集上生成初步标签。然后，对具有冲突分类的示例进行聚类，并将最接近的矛盾示例对发送给人类专家进行标记。然后，使用此精选数据集迭代地微调模型。使用 Cohen’s Kappa 评估模型性能，衡量模型与人类专家之间的对齐程度，以及专家之间的内部对齐程度。

实验表明，使用仅包含 250-450 个专家标记示例的精选数据微调的模型，与在 100,000 个众包示例上训练的模型相比，获得了可比或更优越的性能。具体而言，32.5 亿参数的模型与人类专家的对齐程度提高了 55-65%，突出了精选过程的效率和有效性。作者强调，高质量标签（Cohen’s Kappa 值高于 0.8）对于超越众包数据至关重要。该方法能够为广告安全等快速发展的领域更快地进行重新训练，从而利用 LLM 的广泛理解和人类注释者的专注专业知识。

---

## 46. 被诅咒的知识

**原文标题**: Cursed Knowledge

**原文链接**: [https://immich.app/cursed-knowledge/](https://immich.app/cursed-knowledge/)

Immich 项目的“诅咒知识”文章详细介绍了该项目开发过程中遇到的令人沮丧和意外的行为，本质上是一个“避坑指南”。它重点介绍了各种技术和平台存在的特定问题。

以下是摘要：

该文章涵盖了以下领域的问题：

*   **Zitadel:** Zitadel的自定义脚本功能使用的JS引擎对正则表达式的支持有限。
*   **Entra:** Microsoft Entra 在其发现文档中错误地省略了 PKCE 支持。
*   **EXIF 数据:** EXIF 数据中的图像尺寸可能不准确。
*   **YAML:** YAML 空格处理方式可能违反直觉。
*   **Windows SMB:** Windows 中的隐藏文件无法使用 "w" 标志打开。
*   **Bash 脚本:** Git 的 CRLF 转换会破坏 bash 脚本。
*   **Cloudflare Workers:** Cloudflare Workers 中的 Fetch 请求默认使用 HTTP。
*   **移动 GPS 共享:** 移动电话可能会从图像中删除 GPS 数据。
*   **PostgreSQL:** PostgreSQL NOTIFY 每 5 秒写入 WAL。
*   **npm 脚本:** npm 脚本会进行不必要的 HTTP 调用。
*   **JavaScript 包:** 用户以向后兼容为幌子添加大量依赖项。
*   **密码安全:** Bcrypt 实现会忽略密码中前 72 个字节后的字符。
*   **JavaScript Dates:** JavaScript Date 对象使用不一致的索引。
*   **Node.js ESM 导入:** 20.8 之前的 Node.js 版本可能会因为 ESM 和 CJS 互操作而崩溃。
*   **PostgreSQL 参数限制:** PostgreSQL 对批量插入有参数限制。
*   **安全上下文:** 某些 Web API 只能在安全上下文 (HTTPS/localhost) 中工作。
*   **TypeORM:** TypeORM 的 remove 实现会改变输入对象。

该文章旨在警告其他开发人员注意这些潜在的陷阱。

---

## 47. 基准测试框架桌面主板与四节点集群

**原文标题**: Benchmark Framework Desktop Mainboard and 4-node cluster

**原文链接**: [https://github.com/geerlingguy/ollama-benchmark/issues/21](https://github.com/geerlingguy/ollama-benchmark/issues/21)

本文讨论了在Framework Desktop主板上使用单节点和4节点集群配置执行的基准测试。该系统采用AMD Ryzen AI Max+ 395处理器，配备Radeon 8090S显卡。Geerlingguy收到了四台预生产单元，用于本地集群测试。

单节点配置配备128 GB内存，而4节点集群总共配备512 GB内存。初始测试使用了2.5 Gbps以太网互连。后续测试使用NICGIGA交换机将网络升级到5 Gbps，该交换机安装在带有原型Framework Desktop迷你机架托盘的DeskPi T1迷你机架中。还测试了Thunderbolt互连，通过TB4接口实现了10 Gbps的速度。

作者提供了指向进一步基准测试的链接，这些基准测试侧重于CPU、GPU、磁盘和网络性能，特别提到了涉及大型语言模型（LLM）的测试。他还参考了他的Beowulf AI集群存储库，了解这些测试中使用的自动化技术。最后，提供了指向sbc-reviews站点的链接，以获取有关Framework Desktop的更多信息。作者对该项目表示热情，展示了其他人对该问题的反应，并表明该问题尚未分配给任何人。

---

## 48. 劳氏和家得宝与执法部门共享客户数据

**原文标题**: Lowe's and Home Depot are sharing customer data with law enforcement

**原文链接**: [https://flowingdata.com/2025/08/08/lowes-and-home-depot-are-sharing-customer-data-with-law-enforcement/](https://flowingdata.com/2025/08/08/lowes-and-home-depot-are-sharing-customer-data-with-law-enforcement/)

据报道，劳氏公司和家得宝公司正在通过使用Flock摄像头与执法部门共享客户数据。这些摄像头收集进入其停车场的车辆的车牌信息，执法机构可以访问这些信息，将其作为监控来源。

根据404 Media的一份报告，这种做法促成了由Flock Safety协调的“大规模监控网络”。像电子前沿基金会的戴夫·马斯这样的隐私倡导者，对这种数据收集和共享缺乏透明度表示担忧。他质疑客户是否知道他们的信息正在被收集，以及公司是否考虑过潜在的危险，例如执法部门滥用数据或以弱势群体为目标。

该文章暗示，如果目前的趋势继续下去，这种做法可能会产生广泛的未来影响，最终会影响到每个人。

---

## 49. 如何向使用者非购买者销售

**原文标题**: How to sell if your user is not the buyer

**原文链接**: [https://writings.founderlabs.io/p/how-to-sell-if-your-user-is-not-the](https://writings.founderlabs.io/p/how-to-sell-if-your-user-is-not-the)

本文探讨了常见的“使用者非购买者”问题，重点在于当使用者并非购买决策者时，如何有效地销售产品。关键在于了解组织内部**真正拥有决策权的人**，因为拥有预算的人并不总是决策者。

作者提出了两种情景：

*   **较小规模的组织：** 开发者（使用者）通常拥有决策权，因为他们快速实施和迭代的能力对公司的生存至关重要。在这种情况下，应利用开发者的经验和简化工作流程的需求。他们甚至可以实施免费试用并倡导购买。
*   **较大规模的组织：** 领导层（CTO、总监）拥有决策权，因为安全和合规至关重要。销售周期更长，重点在于证明产品的安全性和整体价值。

本文强调了理解使用者和购买者的**动机**的重要性。如果使用者（开发者）重视产品，则需要为他们提供说服领导层的工具。这包括将价值主张从开发者的角度（例如，节省时间，减少痛苦）转化为领导层的角度（例如，更快上市时间，提高生产力，实现公司目标）。

至关重要的是，本文建议让使用者成为有效的内部“销售人员”。提供展示实际效益的报告，如节省的时间，并进行客户访谈，以了解常见的异议以及如何解决这些异议。通过让使用者能够有效地向领导层传达产品的价值，您可以显著提高达成交易的可能性。

---

## 50. 网格化你

**原文标题**: MapYourGrid

**原文链接**: [https://MapYourGrid.org/](https://MapYourGrid.org/)

MapYourGrid：绘制全球电网，助力无化石燃料未来。

---

## 51. 维波图

**原文标题**: Vibechart

**原文链接**: [https://www.vibechart.net/](https://www.vibechart.net/)

Vibechart.net 将“Vibechart”定义为基于期望结果或主观解读而非客观事实或实用性的数据图表。它将其与“谎言、该死的谎言和统计数据”相提并论，表明 Vibechart 可以被用来操纵或歪曲数据。

该网站提到在 GPT5 发布中观察到的“图表犯罪”，并将这一发现归功于 marvinborner.de。它强调了理解图表如何具有欺骗性的重要性，并推荐了“了解图表如何说谎”和“数据可视化耻辱堂”等资源。该网站承认其自身的 CSS 动画可能在视觉上不吸引人，引用用户反馈称其为移动设备的“癌症”。 本质上，Vibechart.net 是对数据可视化可能被用于有偏见或误导性目的的潜在性的一个半开玩笑的评论，旨在促使用户成为图表的批判性消费者。

---

## 52. Show HN: Kitten TTS – 25MB CPU-Only, Open-Source TTS Model
	
展示HN: Kitten TTS – 25MB CPU专用, 开源TTS模型

**原文标题**: Show HN: Kitten TTS – 25MB CPU-Only, Open-Source TTS Model

**原文链接**: [https://github.com/KittenML/KittenTTS](https://github.com/KittenML/KittenTTS)

Kitten TTS：轻量级开源CPU优化文本转语音模型

Kitten TTS是一款全新的开源、轻量级且CPU优化的文本转语音（TTS）模型，旨在实现简易部署和高质量语音合成。它仅有1500万参数，大小小于25MB，几乎可以在任何设备上无需GPU运行。该模型提供多种优质语音选项，并针对快速、实时推理进行了优化。

开发者预览版现已发布，可以通过提供的URL使用pip安装。示例代码展示了如何初始化模型、使用指定语音从文本生成音频，并将输出保存为WAV文件。可用语音选项也已列出，包括男声和女声表现力丰富的声音。

该项目的清单包括未来发布完全训练的模型权重、移动SDK和网页版的计划。Kitten TTS旨在提供可访问且高质量的TTS功能，而无需专门的硬件。

---

## 53. HashiCorp Vault 身份验证、身份、授权中的零日漏洞

**原文标题**: Zero-day flaws in authentication, identity, authorization in HashiCorp Vault

**原文链接**: [https://cyata.ai/blog/cracking-the-vault-how-we-found-zero-day-flaws-in-authentication-identity-and-authorization-in-hashicorp-vault/](https://cyata.ai/blog/cracking-the-vault-how-we-found-zero-day-flaws-in-authentication-identity-and-authorization-in-hashicorp-vault/)

本文（2025年8月6日）讨论了在企业保险库解决方案CyberArk Conjur中发现的一系列漏洞。作者Yarden Porat解释了他们如何通过利用这些缺陷实现未经身份验证的任意远程代码执行（RCE）。虽然标题提到了HashiCorp Vault，但本文重点关注CyberArk Conjur平台内的漏洞。

本文的核心可能详细介绍了具体的漏洞以及它们如何被串联在一起。这可能涉及Conjur中身份验证机制、身份管理或授权控制方面的弱点。该漏洞链允许攻击者完全绕过身份验证，这意味着他们不需要任何有效的凭据即可获得访问权限并在Conjur系统上远程执行代码。

本文可能强调了企业保险库中强大安全措施的重要性，因为它们对于保护敏感信息至关重要。这些漏洞的发现和利用突显了与实施不完善的安全控制相关的潜在风险，以及成功攻击造成的毁灭性后果。它可能还提供了对攻击媒介和缓解策略的见解。

---

## 54. 用于整首歌曲生成的开放音乐基础模型

**原文标题**: Open music foundation models for full-song generation

**原文链接**: [https://map-yue.github.io/](https://map-yue.github.io/)

本文介绍了YuE（乐），一款基于LLaMA2架构的开源音乐基础模型，专为长篇音乐生成而设计，特别是歌词到歌曲的创作。 YuE能够生成长达五分钟的音乐，同时保持歌词对齐、连贯的音乐结构和引人入胜的人声旋律。它通过轨道解耦的下一个令牌预测、结构化的渐进式调节以及多任务、多阶段的预训练方法来实现这一目标。

YuE还采用了一种重新设计的上下文学习技术，用于多功能的风格迁移和双向生成。 评估表明，YuE在音乐性和人声灵活性方面与一些专有系统相媲美或超越。微调增强了控制力并支持尾部语言。 除了生成之外，YuE学习到的表示在音乐理解任务上表现良好，在MARBLE基准测试中与最先进的方法相媲美或超过了它们。

本文提供了YuE模型检查点、各种流派（金属、爵士、说唱、流行、民谣、华语流行、灵魂乐、乡村和另类摇滚）的生成音乐示例及其对应歌词的链接。 这些示例突出了YuE根据给定的歌词和流派标签生成多样化的人声风格和流派的能力。

---

## 55. Show HN: 专为可靠性设计的浏览器AI代理平台

**原文标题**: Show HN: Browser AI agent platform designed for reliability

**原文链接**: [https://github.com/nottelabs/notte](https://github.com/nottelabs/notte)

Notte是一个旨在快速构建可靠的网页自动化代理的平台，它结合了人工智能代理与传统脚本，以实现成本效益和更高的可靠性。它提供开源核心和高级API服务。

开源核心允许用户运行网页代理，获取结构化输出，并使用兼容Playwright的原语与网站交互。API服务增加了诸如隐身浏览器会话（具有CAPTCHA解决和代理）、混合工作流、安全密钥库和数字角色等功能。

Notte提供了一个Python SDK，方便集成。基准测试表明，与其他浏览器使用自动化工具相比，Notte实现了更高的任务可靠性和速度。

主要功能包括：

*   **结构化输出:** 指定Pydantic模型进行结构化数据提取。
*   **代理密钥库:** 安全地存储和管理凭据。
*   **代理角色:** 创建具有唯一电子邮件和电话号码的数字身份。
*   **隐身:** 自动CAPTCHA解决和代理配置。
*   **文件管理:** 在代理执行期间上传和下载文件。
*   **Cookies/身份验证会话:** 通过cookies验证会话。
*   **CDP浏览器兼容性:** 通过CDP与外部无头浏览器提供商集成。
*   **工作流:** 将网页自动化原语与代理结合使用，实现混合工作流。
*   **抓取:** 用于数据提取的专用抓取端点。

Notte在服务器端公共许可证 v1 下获得许可。提供了一个利用抓取端点的搜索演示，展示了LLM聊天机器人中的实时搜索。

---

## 56. 无需GPT-5也能控制Linux电脑，100%保护隐私。

**原文标题**: You don't need GPT-5 to control your computer on Linux. 100% privacy

**原文链接**: [https://grigio.org/you-dont-need-gpt-5-to-control-your-computer-on-linux-100-privacy/](https://grigio.org/you-dont-need-gpt-5-to-control-your-computer-on-linux-100-privacy/)

本文认为，您无需像GPT-5这样尖端的云端AI，即可在Linux上实现高效的计算机自动化。相反，您可以使用免费且离线运行的本地AI解决方案，构建一个私有且安全的系统。

关键组件包括：

*   **原生AI集成：** 诸如Newelle之类的工具集成了本地和云端AI功能。
*   **OpenAI兼容API：** 诸如Ollama、LM Studio或llama.cpp之类的项目提供了必要的API兼容性。
*   **合适的AI模型：** 建议使用紧凑而智能的模型，如Qwen3-4B，该模型适合您的RAM（使用Q5_K_M量化时小于3GB）。

本文强调了通过工具使用（函数调用）进行系统交互以确保安全性的重要性，允许自动化某些任务，同时需要人工批准其他任务。

性能取决于上下文大小、硬件和模型大小等因素，因此建议测试不同的模型。建议以Qwen3-4B-2507作为一个良好的起点。

最终，本文旨在推广使用这些现成的工具和模型，创建一个强大、安全且高效的AI自动化系统，以满足您的特定需求。

---

## 57. 大型语言模型不需要理解MCP。

**原文标题**: An LLM does not need to understand MCP

**原文链接**: [https://hackteam.io/blog/your-llm-does-not-care-about-mcp/](https://hackteam.io/blog/your-llm-does-not-care-about-mcp/)

大型语言模型无需“理解”模型上下文协议（MCP）即可有效进行工具调用。 MCP是一种用于将代理连接到工具、提示和资源的标准。 作者强调，大型语言模型只是根据提供的工具定义（名称、描述、输入参数）生成代表函数调用的文本，但它们本身并不了解如何执行这些调用。

代理循环由开发者构建，负责解析大型语言模型的输出，通过其API调用相应的工具，并将结果反馈给大型语言模型。 MCP通过为工具提供通用适配器，并为交互创建一致的模式，从而简化了开发者的任务。 它涉及一个宿主应用程序、一个MCP客户端和暴露工具的MCP服务器。

虽然MCP通过管理与各种工具交互的复杂性并提高可重用性，使开发者更容易进行工具集成，但它对大型语言模型本身是透明的。 大型语言模型仍然看到相同的工具定义。

本文将MCP定位在更广泛的“上下文工程”背景下，即开发者设计提示和工具定义，以便为大型语言模型提供生成有用输出的必要信息。 MCP通过提供结构化的接口来简化这一过程，使得在不为每个工具编写自定义包装器的情况下，更容易维护和扩展工具集成。 因此，MCP是一种开发者工具，而不是大型语言模型的要求，它可以提高AI系统的可靠性和模块化。

---

## 58. 莱昂纳多·奇亚里廖内 – MPEG联合创始人

**原文标题**: Leonardo Chiariglione – Co-founder of MPEG

**原文链接**: [https://leonardo.chiariglione.org/](https://leonardo.chiariglione.org/)

MPEG联合创始人莱昂纳多·基亚里廖内回顾了他开发数字媒体标准的历程。出于为社会福祉创造互操作技术的愿望，他于1988年创立了MPEG，该组织交付了MPEG-1（视频CD、MP3）和MPEG-2（数字电视基础设施）等基础标准。随后推出的MPEG-4实现了互联网媒体分发。在他的领导下，MPEG制定了200多项标准，并将小组的范围扩展到媒体之外。

基亚里廖内于2020年离开了MPEG，理由是该组织被“不明势力”劫持，这些势力阻碍了技术发展，并维持过时的IP许可模式，最终损害了行业和消费者的利益。

随后，他在2020年9月创立了人工智能移动图像、音频和数据编码（MPAI）。这个新组织旨在开发基于人工智能的标准，克服困扰MPEG的停滞不前和许可问题。MPAI已经开发了五项标准，涵盖人工智能应用程序执行、音频增强、多模式对话、公司绩效预测和生态系统治理。更多标准正在开发中，重点关注基于人工智能的视频编码、元宇宙模型和互联自动驾驶汽车等领域。

他在《即使星星也会陨落》一书中记录了MPEG的兴衰，并在《迈向普及和可信赖的人工智能》一书中记录了MPAI的初步发展。

---

## 59. GPT-5发布令人担忧

**原文标题**: The GPT-5 Launch Was Concerning

**原文链接**: [https://blog.charliemeyer.co/the-gpt-5-launch-was-concerning/](https://blog.charliemeyer.co/the-gpt-5-launch-was-concerning/)

作者对GPT-5的发布表示担忧，主要指出了两个问题：模型性能令人质疑，以及OpenAI的优先事项发生了令人不安的转变。

首先，作者指出，GPT-5虽然被吹捧为“博士级别专家”，但在基本的LLM挑战方面仍然存在问题，一个经典的“技巧”提示的错误答案证明了这一点。虽然承认仅凭这一个例子就断然否定AGI是荒谬的，但作者认为这让人怀疑该模型的真实能力。

其次，作者批评OpenAI在发布会上强调可定制的聊天颜色，包括付费订阅者的专属选项。这被视为一家缺乏创新想法，并诉诸肤浅功能来将其用户群货币化的迹象，尤其是在其目前的财务状况下。

此外，作者指出OpenAI在ChatGPT中展示编码工具所带来的潜在利益冲突。这一举动被形容为“sherlocking”，即模仿Cursor等成功的第三方平台的功能，从而对Cursor构成重大威胁，甚至可能破坏OpenAI自己的API业务，该业务依赖于与此类公司的合作。

最终，作者得出结论，GPT-5的发布令人失望，并加剧了他们对人工智能行业的怀疑。这次演示并未展示AGI方面的重大进展，而是揭示了一家公司可能因模型进展放缓而失去焦点和方向。作者建议需要等待GPT-6的出现。

---

## 60. 我不看你的邮件往来。

**原文标题**: I don't read your email threads

**原文链接**: [https://loganmarek.com/i-dont-read-your-threads/](https://loganmarek.com/i-dont-read-your-threads/)

这篇文章表达了对冗长邮件线程的沮丧，尤其是那些最新的邮件只包含“[您的名字] 请看下文”的线程。作者认为，这些线程迫使收件人筛选数周无关的通信才能理解上下文和分配的任务，并将其描述为一种混乱且低效的体验。

作者承认不再阅读冗长的邮件线程，而是选择使用 Copilot 来解读信息并提取必要的细节。文章提倡一种更结构化的沟通方式，建议：

*   **电子邮件**应保留用于可记录的沟通或复杂的任务。
*   **文档平台**应用于可重复的流程、程序和记录关键决策。
*   **即时通讯**应用于实际的沟通。
*   **会议**应保留用于讨论，特别是那些预期会有分歧的讨论。

核心信息是呼吁避免邮件线程，并使用即时通讯作为更高效的替代方案。作者认为这将节省时间、减少沮丧感，并最终提高工作效率。

---

## 61. 富足的未来与左派

**原文标题**: The Future of Abundance and the Left

**原文链接**: [https://www.derekthompson.org/p/the-future-of-abundance-and-the-left](https://www.derekthompson.org/p/the-future-of-abundance-and-the-left)

In "The Future of Abundance and the Left," Derek Thompson explores the contrasting reactions to his book "Abundance" within left-leaning circles. Online progressive commentators have largely criticized the book, viewing it as a threat to core left-wing ideologies like socialism and anti-monopoly sentiment. These critics fear that focusing on abundance will dilute the Democratic Party's commitment to these principles.

Conversely, many elected Democratic officials, including some from the progressive wing of the party like Rep. Ro Khanna and Gov. Wes Moore, have endorsed the book's ideas. These politicians recognize the need for government to function effectively and see abundance as a framework for improving government efficiency and delivering better outcomes.

Thompson argues that both perspectives hold valid points. Critics correctly identify that "Abundance" promotes a form of liberalism that prioritizes market regulation and diverse solutions over socialist ideals and singular focus on corporate power. However, politicians recognize that improving government functionality and delivery on promises are crucial for the Democratic Party's success.

Thompson highlights a conversation with Democratic Socialist mayoral candidate Zohran Mamdani, who, despite differing policy views, acknowledged the importance of government excellence and outcome-oriented governance. Thompson concludes that the concept of abundance can potentially bridge divides within the left, fostering a broader coalition focused on making government work and addressing real-world problems through improved efficiency and innovation. He envisions a future where abundance helps build a larger, more effective liberal coalition.


---

## 62. The BLS can't be replaced by the private sector

**原文标题**: The BLS can't be replaced by the private sector

**原文链接**: [https://www.bloomberg.com/opinion/articles/2025-08-08/the-bls-can-t-be-replaced-by-the-private-sector](https://www.bloomberg.com/opinion/articles/2025-08-08/the-bls-can-t-be-replaced-by-the-private-sector)

生成摘要时出错

---

## 63. The Paranoid Style in American Politics (1964)

**原文标题**: The Paranoid Style in American Politics (1964)

**原文链接**: [https://harpers.org/archive/1964/11/the-paranoid-style-in-american-politics/](https://harpers.org/archive/1964/11/the-paranoid-style-in-american-politics/)

生成摘要时出错

---

## 64. GPT-5 for Developers

**原文标题**: GPT-5 for Developers

**原文链接**: [https://openai.com/index/introducing-gpt-5-for-developers](https://openai.com/index/introducing-gpt-5-for-developers)

生成摘要时出错

---

## 65. 台积电将采用3D技术生产晶圆级处理器

**原文标题**: TSMC to go 3D with wafer-sized processors

**原文链接**: [https://www.tomshardware.com/tech-industry/tsmc-to-go-3d-with-wafer-sized-processors-cow-sow-system-on-wafer-technology-allows-3d-stacking-for-the-worlds-largest-chips](https://www.tomshardware.com/tech-industry/tsmc-to-go-3d-with-wafer-sized-processors-cow-sow-system-on-wafer-technology-allows-3d-stacking-for-the-worlds-largest-chips)

台积电正在开发一种名为“CoW-SoW”（芯片堆叠于晶圆上之系统级晶圆）的新平台，目标是在2027年实现大规模生产，该平台支持晶圆级处理器与堆叠式存储器以及潜在的逻辑电路进行3D集成。 这是在其现有InFO_SoW技术的基础上发展而来的，特斯拉目前在其Dojo超级计算机中使用该技术，该技术可以制造晶圆级逻辑处理器。

CoW-SoW平台融合了InFO_SoW和系统集成芯片 (SoIC) 技术。 这一增强解决了当前InFO_SoW的局限性，特别是其对片上存储器的依赖以及缺乏3D堆叠能力。 通过使用芯片堆叠于晶圆（CoW）技术，CoW-SoW平台将能够将HBM4存储器直接堆叠到晶圆级处理器上，以满足未来人工智能的计算需求。 堆叠额外的逻辑电路也可能有利于成本优化。

晶圆级处理器具有高性能和高效率优势，例如高带宽、低延迟通信和能源效率。 台积电认为，这项进步将使客户能够集成更多的逻辑电路和存储器，从而实现更强大和更节能的人工智能集群和超级计算机。

---

## 66. Show HN: Octofriend, a cute coding agent that can swap between GPT-5 and Claude

**原文标题**: Show HN: Octofriend, a cute coding agent that can swap between GPT-5 and Claude

**原文链接**: [https://github.com/synthetic-lab/octofriend](https://github.com/synthetic-lab/octofriend)

生成摘要时出错

---

## 67. Monte Carlo Crash Course: Quasi-Monte Carlo

**原文标题**: Monte Carlo Crash Course: Quasi-Monte Carlo

**原文链接**: [https://thenumb.at/QMC/](https://thenumb.at/QMC/)

生成摘要时出错

---

## 68. Europe doesn't have a startup problem, it has a storytelling problem

**原文标题**: Europe doesn't have a startup problem, it has a storytelling problem

**原文链接**: [https://sifted.eu/articles/europe-storytelling-problem](https://sifted.eu/articles/europe-storytelling-problem)

生成摘要时出错

---

## 69. Job Hunting for 21 Months

**原文标题**: Job Hunting for 21 Months

**原文链接**: [https://www.businessinsider.com/laid-off-accenture-manager-struggles-salary-expectations-tough-job-market-2025-7](https://www.businessinsider.com/laid-off-accenture-manager-struggles-salary-expectations-tough-job-market-2025-7)

生成摘要时出错

---

## 70. How to Not Build the Torment Nexus

**原文标题**: How to Not Build the Torment Nexus

**原文链接**: [https://buttondown.com/monteiro/archive/how-to-not-build-the-torment-nexus/](https://buttondown.com/monteiro/archive/how-to-not-build-the-torment-nexus/)

生成摘要时出错

---

## 71. The Inkhaven Blogging Residency

**原文标题**: The Inkhaven Blogging Residency

**原文链接**: [https://www.inkhaven.blog/](https://www.inkhaven.blog/)

生成摘要时出错

---

## 72. The Q Programming Language

**原文标题**: The Q Programming Language

**原文链接**: [https://git.urbach.dev/cli/q](https://git.urbach.dev/cli/q)

生成摘要时出错

---

## 73. Clear Thinking

**原文标题**: Clear Thinking

**原文链接**: [https://read.perspectiveship.com/p/clear-thinking](https://read.perspectiveship.com/p/clear-thinking)

生成摘要时出错

---

## 74. Italy's pizza detectives

**原文标题**: Italy's pizza detectives

**原文链接**: [https://www.bbc.com/travel/article/20250801-italys-undercover-pizza-detectives](https://www.bbc.com/travel/article/20250801-italys-undercover-pizza-detectives)

生成摘要时出错

---

## 75. Wheelchair Users Are Finally Winning the Right to Repair

**原文标题**: Wheelchair Users Are Finally Winning the Right to Repair

**原文链接**: [https://www.motherjones.com/politics/2025/08/power-wheelchair-duopoly-right-repair-law/](https://www.motherjones.com/politics/2025/08/power-wheelchair-duopoly-right-repair-law/)

生成摘要时出错

---

## 76. Emailing a one-time code is worse than passwords

**原文标题**: Emailing a one-time code is worse than passwords

**原文链接**: [https://blog.danielh.cc/blog/passwords](https://blog.danielh.cc/blog/passwords)

生成摘要时出错

---

## 77. DNA tests are uncovering the true prevalence of incest (2024)

**原文标题**: DNA tests are uncovering the true prevalence of incest (2024)

**原文链接**: [https://www.theatlantic.com/health/archive/2024/03/dna-tests-incest/677791/](https://www.theatlantic.com/health/archive/2024/03/dna-tests-incest/677791/)

生成摘要时出错

---

## 78. Rules by which a great empire may be reduced to a small one (1773)

**原文标题**: Rules by which a great empire may be reduced to a small one (1773)

**原文链接**: [https://founders.archives.gov/documents/Franklin/01-20-02-0213](https://founders.archives.gov/documents/Franklin/01-20-02-0213)

生成摘要时出错

---

## 79. Running GPT-OSS-120B at 500 tokens per second on Nvidia GPUs

**原文标题**: Running GPT-OSS-120B at 500 tokens per second on Nvidia GPUs

**原文链接**: [https://www.baseten.co/blog/sota-performance-for-gpt-oss-120b-on-nvidia-gpus/](https://www.baseten.co/blog/sota-performance-for-gpt-oss-120b-on-nvidia-gpus/)

生成摘要时出错

---

## 80. Self-cleaning glass uses electric field to remove dust particles within seconds

**原文标题**: Self-cleaning glass uses electric field to remove dust particles within seconds

**原文链接**: [https://techxplore.com/news/2025-08-glass-electric-field-particles-seconds.html](https://techxplore.com/news/2025-08-glass-electric-field-particles-seconds.html)

生成摘要时出错

---

## 81. PEP 802 – Display Syntax for the Empty Set

**原文标题**: PEP 802 – Display Syntax for the Empty Set

**原文链接**: [https://peps.python.org/pep-0802/](https://peps.python.org/pep-0802/)

生成摘要时出错

---

## 82. Laptop Support and Usability (LSU): July 2025 Report

**原文标题**: Laptop Support and Usability (LSU): July 2025 Report

**原文链接**: [https://github.com/FreeBSDFoundation/proj-laptop/blob/main/monthly-updates/2025-07.md](https://github.com/FreeBSDFoundation/proj-laptop/blob/main/monthly-updates/2025-07.md)

生成摘要时出错

---

## 83. How AI conquered the US economy: A visual FAQ

**原文标题**: How AI conquered the US economy: A visual FAQ

**原文链接**: [https://www.derekthompson.org/p/how-ai-conquered-the-us-economy-a](https://www.derekthompson.org/p/how-ai-conquered-the-us-economy-a)

生成摘要时出错

---

## 84. Show HN: Stasher – Burn-after-read secrets from the CLI, no server, no trust

**原文标题**: Show HN: Stasher – Burn-after-read secrets from the CLI, no server, no trust

**原文链接**: [https://github.com/stasher-dev/stasher-cli](https://github.com/stasher-dev/stasher-cli)

生成摘要时出错

---

## 85. Debounce

**原文标题**: Debounce

**原文链接**: [https://developer.mozilla.org/en-US/docs/Glossary/Debounce](https://developer.mozilla.org/en-US/docs/Glossary/Debounce)

生成摘要时出错

---

## 86. Complex Iterators Are Slow

**原文标题**: Complex Iterators Are Slow

**原文链接**: [https://caolan.uk/notes/2025-07-31_complex_iterators_are_slow.cm](https://caolan.uk/notes/2025-07-31_complex_iterators_are_slow.cm)

生成摘要时出错

---

## 87. How we enforce .NET coding standards to improve productivity

**原文标题**: How we enforce .NET coding standards to improve productivity

**原文链接**: [https://anthonysimmon.com/workleap-dotnet-coding-standards/](https://anthonysimmon.com/workleap-dotnet-coding-standards/)

生成摘要时出错

---

## 88. Sqlite3 will also read and write ZIP archives

**原文标题**: Sqlite3 will also read and write ZIP archives

**原文链接**: [https://mastodon.social/@jpmens/114991866577330548](https://mastodon.social/@jpmens/114991866577330548)

生成摘要时出错

---

## 89. The fundamentals still matter

**原文标题**: The fundamentals still matter

**原文链接**: [https://jordangoodman.bearblog.dev/fundamentals-still-matter/](https://jordangoodman.bearblog.dev/fundamentals-still-matter/)

生成摘要时出错

---

## 90. Windows XP Professional

**原文标题**: Windows XP Professional

**原文链接**: [https://win32.run/](https://win32.run/)

生成摘要时出错

---

## 91. Arm desktop: emulation

**原文标题**: Arm desktop: emulation

**原文链接**: [https://marcin.juszkiewicz.com.pl/2025/07/22/arm-desktop-emulation/](https://marcin.juszkiewicz.com.pl/2025/07/22/arm-desktop-emulation/)

生成摘要时出错

---

## 92. Lightweight LSAT

**原文标题**: Lightweight LSAT

**原文链接**: [https://lightweightlsat.com/](https://lightweightlsat.com/)

生成摘要时出错

---

## 93. Benchmarking GPT-5 on 400 real-world code reviews

**原文标题**: Benchmarking GPT-5 on 400 real-world code reviews

**原文链接**: [https://www.qodo.ai/blog/benchmarking-gpt-5-on-real-world-code-reviews-with-the-pr-benchmark/](https://www.qodo.ai/blog/benchmarking-gpt-5-on-real-world-code-reviews-with-the-pr-benchmark/)

生成摘要时出错

---

## 94. Infinite Pixels

**原文标题**: Infinite Pixels

**原文链接**: [https://meyerweb.com/eric/thoughts/2025/08/07/infinite-pixels/](https://meyerweb.com/eric/thoughts/2025/08/07/infinite-pixels/)

生成摘要时出错

---

## 95. Gemini CLI GitHub Actions

**原文标题**: Gemini CLI GitHub Actions

**原文链接**: [https://blog.google/technology/developers/introducing-gemini-cli-github-actions/](https://blog.google/technology/developers/introducing-gemini-cli-github-actions/)

生成摘要时出错

---

## 96. The Rise of Ritual Features: Why Platforms Are Adding Daily Puzzle Games

**原文标题**: The Rise of Ritual Features: Why Platforms Are Adding Daily Puzzle Games

**原文链接**: [https://productpickle.online/2025/07/20/ritual-features-the-quiet-strategy-behind-daily-puzzle-games-on-linkedin-and-beyond/](https://productpickle.online/2025/07/20/ritual-features-the-quiet-strategy-behind-daily-puzzle-games-on-linkedin-and-beyond/)

生成摘要时出错

---

## 97. Spatio-temporal indexing the Bluesky firehose

**原文标题**: Spatio-temporal indexing the Bluesky firehose

**原文链接**: [https://joelgustafson.com/posts/2025-08-07/spatio-temporal-indexing-the-bluesky-firehose](https://joelgustafson.com/posts/2025-08-07/spatio-temporal-indexing-the-bluesky-firehose)

生成摘要时出错

---

## 98. Open models by OpenAI

**原文标题**: Open models by OpenAI

**原文链接**: [https://openai.com/open-models/](https://openai.com/open-models/)

生成摘要时出错

---

## 99. The Whispering Earring

**原文标题**: The Whispering Earring

**原文链接**: [https://croissanthology.com/earring](https://croissanthology.com/earring)

生成摘要时出错

---

## 100. Jepsen: Capela dda5892

**原文标题**: Jepsen: Capela dda5892

**原文链接**: [https://jepsen.io/analyses/capela-dda5892](https://jepsen.io/analyses/capela-dda5892)

生成摘要时出错

---

