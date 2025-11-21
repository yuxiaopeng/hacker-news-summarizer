# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-11-21.md)

*最后自动更新时间: 2025-11-21 17:47:59*
## 1. Show HN: Wealthfolio 2.0 - 开源投资追踪器。现已支持移动端和 Docker

**原文标题**: Show HN: Wealthfolio 2.0- Open source investment tracker. Now Mobile and Docker

**原文链接**: [https://wealthfolio.app/?v=2.0](https://wealthfolio.app/?v=2.0)

Wealthfolio 2.0 是一款开源的、注重隐私的投资追踪器，现已推出桌面端、移动端和网页端版本。它允许用户在一个地方聚合所有投资和储蓄账户，从而全面了解自己的财富。一个关键特性是其首要关注隐私的方法，确保用户数据保留在他们的设备上。它提供CSV导入功能以及精心设计、用户友好的界面。

Wealthfolio提供诸如持仓概览、投资组合洞察和业绩追踪等功能，允许用户监控股票、ETF和加密货币。业绩仪表板支持账户比较、与标普500等指数进行基准测试以及ETF追踪。收入追踪有助于监控股息和利息收入。

此外，Wealthfolio还提供历史数据、账户分析、目标追踪以及税务优惠账户的供款额度/限额追踪。它可以帮助用户定义财务目标、监控进度并避免过度供款。该平台可以通过插件扩展，例如投资费用追踪器、目标进度追踪器和股票交易追踪器。Wealthfolio可以免费使用，并提供一次性可选付费。

---

## 2. 我们都应该使用依赖冷却机制。

**原文标题**: We should all be using dependency cooldowns

**原文链接**: [https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns](https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns)

本文倡导采用“依赖冷却期”作为一种简单有效的缓解开源供应链攻击的方法。“依赖冷却期”是指在发布新的依赖项版本后，延迟一段时间再集成它们，从而为发现和解决漏洞留出时间。

作者强调，大多数供应链攻击在恶意更新发布与其被检测/移除之间都存在一个很短的窗口期（几小时或几天）。通过实施冷却期（例如，7-14天），开发者可以避免绝大多数此类攻击。

冷却期的优点包括：

*   **经验有效性：** 它们可以缓解最常见的供应链攻击类型。
*   **易于实施：** Dependabot和Renovate等工具提供内置的冷却期功能，一些包管理器也提供原生支持。
*   **激励负责任的供应商行为：** 鼓励安全供应商专注于快速攻击检测，而不是过度炒作营销。

文章强调，冷却期并非完美的解决方案，因为老练的攻击者可能仍然可以逃避检测。然而，作者认为，通过这种免费且简单的技术，可以显著降低风险暴露（80-90%），使其成为一项有价值的安全措施。作者还建议包管理器应原生支持冷却期，以实现全面保护。

---

## 3. FAWK：大型语言模型可以编写语言解释器

**原文标题**: FAWK: LLMs can write a language interpreter

**原文链接**: [https://martin.janiczek.cz/2025/11/21/fawk-llms-can-write-a-language-interpreter.html](https://martin.janiczek.cz/2025/11/21/fawk-llms-can-write-a-language-interpreter.html)

受 AWK 编程语言的启发，但又因其在解决 Advent of Code 问题时的局限性而感到沮丧，作者设想了一种更具函数式和现代化的 "FAWK" 语言。他们渴望拥有诸如一流数组、函数、词法作用域、显式全局变量和管道等功能。

他们没有自己实现 FAWK，而是利用 Cursor Agent 和 LLM（特别是 Sonnet 4.5）生成了一个可工作的 Python 解释器，并配有全面的端到端测试。 LLM 成功处理了复杂的功能，如任意精度浮点运算（借助 `mpmath` 库）、print 语句/表达式的二元性、多维数组和词法作用域。 还在 C、Haskell 和 Rust 中尝试了实现，并取得了初步成功。

作者对 LLM 基于高级指令和迭代指导交付功能性解释器的能力印象深刻。 虽然承认自己对生成的代码不太熟悉，但他们很高兴在未来的 Advent of Code 挑战中使用 "FAWK"。 他们也在考虑将 LLM 用于其他编程项目，例如实现 Hindley-Milner 类型系统，但也认识到需要平衡 LLM 的协助与保持个人编码能力。 FAWK 可在 GitHub (Janiczek/fawk) 上供其他人尝试，但承认其实验性质和潜在的性能问题。

---

## 4. Olmo 3：引领开源AI，探索模型流程之路

**原文标题**: Olmo 3: Charting a path through the model flow to lead open-source AI

**原文链接**: [https://allenai.org/blog/olmo3](https://allenai.org/blog/olmo3)

Olmo 3 于2025年11月20日发布，强调开源人工智能开发，提供对整个模型流程的访问权限，而不仅仅是最终模型。这包括创建和修改语言模型所需的每个阶段、检查点、数据集和依赖项。

该版本的核心是 Olmo 3-Think (32B)，一个推理模型，允许检查中间推理步骤及其在训练数据中的来源。Olmo 3 系列还包括：Olmo 3-Base (7B, 32B)，一个强大的基础模型，优于其他完全开源的基础模型，并与领先的开源权重模型竞争；Olmo 3-Think (7B, 32B)，一个经过后训练的推理模型，缩小了与顶级开源权重模型的差距，同时使用更少的训练tokens；Olmo 3-Instruct (7B)，一个专注于聊天的模型，在对话能力和工具使用方面与开源权重模型相匹配或超过它们；以及 Olmo 3-RL Zero (7B)，一种用于引导复杂推理并支持 RL 算法基准测试的强化学习途径。

Olmo 3 提供来自同一基础模型的多种记录在案的开发路径（Instruct、RL Zero、Think），从而促进定制和实验。所有组件（数据、代码、模型权重、检查点）均在宽松的开源许可下发布。Olmo 3 模型在各种基准测试中表现出强大的性能，其中 Olmo 3-Base 32B 优于完全开源的基础模型，而 Olmo 3-Think 32B 则成为最强大的完全开源的思考模型。严格的数据管理、优化的训练方法以及算法/基础设施的进步促成了这些结果。

---

## 5. 初代Xbox平台的XBMC 4.0

**原文标题**: XBMC 4.0 for the Original Xbox

**原文链接**: [https://www.xbox-scene.info/articles/announcing-xbmc-40-for-the-original-xbox-r64/](https://www.xbox-scene.info/articles/announcing-xbmc-40-for-the-original-xbox-r64/)

XBMC 4.0发布：经典媒体中心平台重大更新，自2016年以来首次重大进展。此更新对软件进行了现代化改造，保留并扩展了这款标志性自制应用程序的功能。

XBMC由XboxMediaPlayer演变而来，后来发展为Kodi和Plex，在家庭媒体软件领域拥有悠久的历史。 4.0版本带来了由Estuary皮肤（最初来自Kodi v17）驱动的现代界面，并更新了GUI框架，以及一个功能完善的游戏库系统，支持Xbox和模拟游戏的元数据。

新版本恢复了电影和电视元数据抓取器的完整功能，支持在线插件存储库，并改进了任务调度，从而在Xbox的有限硬件上实现更流畅的多任务处理。 它保持了对FLAC等无损音频编解码器的支持，并包括与MilkDrop等音频可视化工具的兼容性。

XBMC 4.0继续提供基于Python的插件架构，并具有更新的设置界面，其中包含全面的自定义选项。 开发团队计划过渡到Python 3.4.10，以潜在地反向移植更新的Kodi插件。

此版本致敬了XBMC的传统，同时实现了体验的现代化，展示了Original Xbox上的持续开发，并计划了未来的更新。 下载和源代码可在Github上找到，欢迎大家贡献。 Xbox-Scene Discord服务器提供支持。

---

## 6. 制作小型RPG

**原文标题**: Making a Small RPG

**原文链接**: [https://jslegenddev.substack.com/p/making-a-small-rpg](https://jslegenddev.substack.com/p/making-a-small-rpg)

无法访问文章链接。

---

## 7. 枢轴机器人(YC W24) 招聘工业自动化硬件工程师

**原文标题**: Pivot Robotics (YC W24) Is Hiring for an Industrial Automation Hardware Engineer

**原文链接**: [https://www.ycombinator.com/companies/pivot-robotics/jobs/7xG9Dc6-mechanical-engineer-controls](https://www.ycombinator.com/companies/pivot-robotics/jobs/7xG9Dc6-mechanical-engineer-controls)

Pivot Robotics (YC W24) 招聘机械工程师（控制方向），助力打造并部署用于高混合制造中机械臂的AI大脑。 他们的软件将现成的机器人和视觉传感器与基础视觉模型相结合，使机器人能够适应复杂的任务，其首款产品专注于自动化金属研磨。 该公司目前已在铸铁厂的 10 多个机器人上部署。

该职位涉及构建和连接控制面板、将传感器和执行器与 PLC/Arduino/机器人控制器集成、设计安全系统以及排除机电子系统的故障。 与软件和电气工程师的合作至关重要，支持客户现场的机器人单元设置也同样重要。 该工程师还将设计和组装机械系统，如虎钳和相机支架。

理想的候选人将拥有机械、机电一体化或机器人工程专业的学士或硕士学位，并具有 1-2 年的机械设计和控制系统集成经验。 必需的技能包括构建控制面板的经验、熟悉安全硬件和标准、了解气动系统、精通 CAD（SolidWorks、Fusion 360 或 Onshape），以及能够在实验室和工厂环境中进行实际操作的能力以及出差意愿。 该职位是全职，位于旧金山，薪资为 10 万美元至 13.5 万美元，并提供 0.40% 至 0.75% 的股权。

---

## 8. 从零开始构建一个最小可用的Armv7模拟器

**原文标题**: Building a Minimal Viable Armv7 Emulator from Scratch

**原文链接**: [https://xnacly.me/posts/2025/building-a-minimal-viable-armv7-emulator/](https://xnacly.me/posts/2025/building-a-minimal-viable-armv7-emulator/)

本文详细介绍了如何使用 Rust 从头开始构建一个最小的 Armv7 模拟器，名为 "stinkarm"。该模拟器仅用约 1300 行代码实现，不依赖任何外部依赖项。其重点在于解析和验证 Armv7 ELF 二进制文件，将段映射到内存中，解码 Arm 指令的一个子集，转换内存交互，以及将 Arm Linux 系统调用转发到宿主 x86-64 系统。

作者创建了一个简单的 "hello world" Armv7 二进制文件作为测试用例，并利用构建脚本和 Nix flake 来编译汇编代码。该模拟器解析 ELF 头部和程序头部以了解二进制文件的结构，识别可执行段，并将它们映射到模拟器的内存空间中。

关键方面包括实现 ELF 头部和程序头部的解析逻辑，定义 Rust 结构体和枚举来表示 ELF 格式元素，以及处理字节序。本文重点介绍了使用宏将字节解析为无符号整数。通过细致地重现执行环境，该模拟器展示了在不同架构上运行 Armv7 二进制文件的基本步骤。

---

## 9. 命令行 – AI 编码的控制谱

**原文标题**: Command Lines – AI Coding's Control Spectrum

**原文链接**: [https://www.wreflection.com/p/command-lines-ai-coding](https://www.wreflection.com/p/command-lines-ai-coding)

Nowfal的《命令行——AI编程的控制谱》探讨了AI编程助手快速发展的格局。在Cursor等工具的推动下，市场蓬勃发展，有望释放软件工程领域显著的生产力提升。

文章将用户分为三类：“手工编码”（避免使用AI者）、“凭感觉编码”（非工程师使用AI进行原型设计）和“架构师+AI编码”（工程师策略性地将任务委托给AI）。根据用户类型，AI编码市场分为面向非工程师的“放手型”工具（原型设计）和面向专业工程师的“动手型”工具（生产代码）。

虽然Cursor的收入增长显著，但其对OpenAI和Anthropic等公司基础模型的依赖构成了一个挑战，尤其是在速率限制方面。Cursor开发Composer-2等内部模型旨在解决这个问题。模型质量被认为是AI编码竞赛中的关键因素，Claude Code和OpenAI Codex正在迎头赶上。

微软（GitHub Copilot）、AWS（Kiro）和谷歌（Antigravity）等现有企业利用现有的客户关系和捆绑销售进行竞争。初创公司可以通过赢得组织内单个用户的青睐来获得 traction。这种转变也影响了StackOverflow等传统开发者资源，因为AI越来越多地回答编程问题。

最终目标是完全自主的软件生成，而胜出者将是那些提供卓越模型质量、独特功能和强大用户留存率的公司。

---

## 10. 制造振荡器很难。

**原文标题**: It's hard to build an oscillator

**原文链接**: [https://lcamtuf.substack.com/p/its-hard-to-build-an-oscillator](https://lcamtuf.substack.com/p/its-hard-to-build-an-oscillator)

无法访问文章链接。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 2 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 3 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 4 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 5 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 6 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 7 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 8 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 9 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 10 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 11 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 12 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 13 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 14 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 15 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 16 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 17 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 18 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 19 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 20 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 21 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 22 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 23 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 24 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 25 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 26 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 27 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 28 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 29 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 30 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 31 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 32 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 33 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 34 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 35 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 36 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 37 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 38 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 39 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 40 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 41 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 42 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 43 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 44 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 45 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 46 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 47 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 48 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 49 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 50 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 51 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 52 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 53 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 54 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 55 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 56 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 57 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 58 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 59 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 60 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 61 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 62 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 63 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 64 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 65 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 66 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 67 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 68 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 69 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 70 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 71 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 72 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 73 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 74 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 75 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 76 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 77 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 78 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 79 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 80 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 81 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 82 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 83 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 84 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 85 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 86 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 87 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 88 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 89 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 90 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 91 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 92 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 93 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 94 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 95 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 96 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 97 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 98 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 99 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 100 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 101 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 102 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 103 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 104 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 105 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 106 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 107 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 108 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 109 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 110 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 111 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 112 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 113 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 114 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 115 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 116 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 117 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 118 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 119 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 120 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 121 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 122 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 123 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 124 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 125 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 126 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 127 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 128 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 129 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 130 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 131 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 132 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 133 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 134 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 135 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 136 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 137 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 138 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 139 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 140 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 141 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 142 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 143 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 144 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 145 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 146 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 147 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 148 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 149 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 150 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 151 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 152 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 153 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 154 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 155 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 156 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 157 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 158 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 159 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 160 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 161 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 162 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 163 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 164 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 165 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 166 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 167 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 168 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 169 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 170 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 171 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 172 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 173 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 174 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 175 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 176 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 177 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 178 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 179 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 180 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 181 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 182 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 183 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 184 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 185 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 186 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 187 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 188 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 189 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 190 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 191 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 192 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 193 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 194 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 195 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 196 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 197 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 198 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 199 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 200 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 201 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 202 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 203 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 204 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 205 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 206 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 207 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 208 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 209 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 210 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 211 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 212 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 213 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 214 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 215 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 216 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 217 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 218 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 219 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 220 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 221 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 222 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 223 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 224 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 225 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 226 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 227 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 228 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 229 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 230 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 231 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 232 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 233 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 234 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 235 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 236 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 237 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 238 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 239 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 240 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 241 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 242 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 243 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 244 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 245 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 246 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
