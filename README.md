# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-08-08.md)

*最后自动更新时间: 2025-08-08 17:48:45*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 2 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 3 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 4 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 5 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 6 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 7 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 8 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 9 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 10 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 11 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 12 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 13 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 14 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 15 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 16 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 17 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 18 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 19 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 20 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 21 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 22 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 23 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 24 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 25 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 26 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 27 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 28 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 29 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 30 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 31 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 32 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 33 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 34 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 35 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 36 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 37 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 38 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 39 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 40 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 41 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 42 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 43 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 44 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 45 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 46 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 47 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 48 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 49 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 50 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 51 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 52 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 53 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 54 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 55 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 56 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 57 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 58 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 59 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 60 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 61 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 62 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 63 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 64 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 65 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 66 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 67 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 68 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 69 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 70 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 71 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 72 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 73 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 74 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 75 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 76 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 77 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 78 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 79 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 80 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 81 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 82 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 83 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 84 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 85 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 86 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 87 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 88 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 89 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 90 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 91 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 92 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 93 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 94 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 95 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 96 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 97 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 98 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 99 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 100 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 101 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 102 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 103 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 104 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 105 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 106 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 107 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 108 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 109 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 110 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 111 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 112 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 113 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 114 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 115 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 116 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 117 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 118 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 119 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 120 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 121 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 122 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 123 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 124 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 125 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 126 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 127 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 128 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 129 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 130 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 131 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 132 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 133 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 134 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 135 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 136 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 137 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 138 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 139 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 140 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 141 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 142 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
