# Hacker News 热门文章摘要 (2025-06-18)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Show HN: Workout.cool – 开源健身指导平台

**原文标题**: Show HN: Workout.cool – Open-source fitness coaching platform

**原文链接**: [https://github.com/Snouzy/workout-cool](https://github.com/Snouzy/workout-cool)

Workout.cool 是一个全新的开源健身教练平台，脱胎于被废弃的 workout.lol 项目。由于目睹该项目因视频版权问题失败，并被新所有者放弃，原开发者决定重建并改进这一理念。

Workout.cool 提供全面的锻炼计划创建、进度跟踪以及包含详细说明和视频演示的庞大练习数据库。它强调社区参与，旨在为健身爱好者提供可靠且现代的替代方案。

该平台使用 Next.js 构建，并遵循 Feature-Sliced Design 原则，从而提高模块化和可维护性。该架构围绕特性、实体和共享组件构建。

主要功能包括练习数据库导入（来自 CSV）、使用 Docker 或手动 PostgreSQL 设置的快速入门说明，以及包含添加新练习、开发移动应用程序、实施游戏化、高级统计、可穿戴设备集成、多语言支持、OAuth 身份验证和社区论坛的路线图。

该项目欢迎贡献，并提供详细的开发说明。它采用 MIT 许可证。作者正在积极寻求社区支持，包括错误报告、功能请求、代码贡献和赞助，以帮助支付托管费用和进一步开发。最终目标是创建一个由社区为社区服务的繁荣的开源健身平台。

---

## 2. 同态加密的CRDT

**原文标题**: Homomorphically Encrypting CRDTs

**原文链接**: [https://jakelazaroff.com/words/homomorphically-encrypted-crdts/](https://jakelazaroff.com/words/homomorphically-encrypted-crdts/)

本文探讨了同态加密（HE）在解决本地优先软件中的隐私问题方面的应用，特别是当使用CRDT进行协同文档编辑时。传统的端到端加密阻止同步服务器合并更新，要求用户同时在线。HE提供了一种解决方案，它允许服务器在不解密的情况下对加密数据执行计算（如合并CRDT更新）。

本文介绍了HE的概念，解释了它允许对加密数据进行数学运算，从而产生与对明文执行相同运算等效的加密结果。它根据支持的运算（加法和乘法）以及由于“噪声”对其使用的限制，区分了部分同态加密、某种程度上同态加密、分级同态加密和全同态加密。本文使用TFHE-rs（一个Rust HE库）来演示如何添加加密数字。它还解释了布尔电路（使用AND和XOR逻辑门）如何实现对加密数据的复杂计算。

最后，本文开始构建一个同态加密的后写胜出注册CRDT，展示了未加密版本的结构和加密版本的框架，突出了使用来自TFHE-rs库的加密数据类型（FheUint64、FheUint8）。它强调，数据的大小需要静态地知道，这是由于HE的工作方式所造成的限制。

---

## 3. 模糊测试在程序移植中的惊人有效性

**原文标题**: The Unreasonable Effectiveness of Fuzzing for Porting Programs

**原文链接**: [https://rjp.io/blog/2025-06-17-unreasonable-effectiveness-of-fuzzing](https://rjp.io/blog/2025-06-17-unreasonable-effectiveness-of-fuzzing)

本文探讨了使用大型语言模型（LLM）自动将 C 代码移植到 Rust 的方法，以解决维护背负技术债务的大型复杂库的难题。作者认为，LLM 可以执行彻底的更新，例如移植语言，而这些更新以前由于成本和破坏现有功能的风险而不可行。

作者详细介绍了使用 Claude 等编码代理的经验，强调了它们在被赋予具体目标和强大的测试用例时解决微妙问题的能力。核心思想是通过比较 C 和 Rust 实现的输出来约束 LLM，并使用模糊测试来识别差异。

本文概述了移植 Zopfli 压缩库的三次尝试。前两次是半手动的，揭示了与 C 版本直接比较的重要性以及自动化的必要性。成功的“真正”尝试包括：1) 以拓扑顺序对符号进行排序。2) 生成 FFI 条目和 Rust 实现。3) 创建比较 C 和 Rust 输出的模糊测试。4) 迭代修复差异，直到模糊测试通过。

作者强调了这种方法的简单性和直接性，并将其与 Syzygy 等更复杂的方法进行了对比。通过利用模糊测试，LLM 被迫找到真正的解决方案，从而产生更健壮和准确的移植。文章总结说，这种自动化方法大大降低了移植的成本，使以前不可行的重构成为可能。

---

## 4. "poline"：一个使用极坐标的神秘调色板生成器

**原文标题**: "poline" is an enigmatic color palette generator using polar coordinates

**原文链接**: [https://meodai.github.io/poline/](https://meodai.github.io/poline/)

Poline：一个使用极坐标生成调色板的 TypeScript 微型库。它名称源于 "polar"（极坐标）和 "line"（线）的组合，代表其核心功能：在极坐标空间中的锚点之间绘制线条以创建颜色变化。用户定义锚点，这些锚点作为调色板每个段的起始和结束颜色。每个锚点对之间生成的颜色数量由指定的点数决定。本质上，“Poline”通过在极坐标系中沿锚颜色之间的线进行插值来创建平滑的颜色渐变，颜色的密度由生成的点数控制。位置函数确定生成点的确切位置。总之，Poline 是一种利用极坐标和线性插值来生成多样化调色板的工具，它可以控制锚点颜色、渐变平滑度（通过点数）和点定位。

---

## 5. Show HN: 我用 C++/CUDA 从零开始构建了一个张量库

**原文标题**: Show HN: I built a tensor library from scratch in C++/CUDA

**原文链接**: [https://github.com/nirw4nna/dsc](https://github.com/nirw4nna/dsc)

DSC：一个全新的机器学习张量库和推理框架

---

## 6. 使用流式SQL查询构建代理

**原文标题**: Building agents using streaming SQL queries

**原文链接**: [https://www.morling.dev/blog/this-ai-agent-should-have-been-sql-query/](https://www.morling.dev/blog/this-ai-agent-should-have-been-sql-query/)

本文对比了传统的拉取式SQL查询与流式SQL查询。传统的SQL查询按需执行，扫描整个数据集并返回完整的结果集。相反，流式SQL查询持续且增量式地运行。它们在数据发生变化时处理数据，仅用受影响的记录更新查询结果，并将这些增量推送给客户端。这种“推送式”方法意味着流式SQL查询避免了为每个更改重新处理整个数据集，使其对于数据不断演变的实时或近实时应用程序而言更加高效。关键的区别在于数据处理方式：按需检索与持续、增量更新。流式SQL更适合需要对数据变化做出立即反应的应用程序。

---

## 7. Attimet (YC F24) – 量化交易研究实验室 – 招聘创始工程师

**原文标题**: Attimet (YC F24) – Quant Trading Research Lab – Is Hiring Founding Engineer

**原文链接**: [https://www.ycombinator.com/companies/attimet/jobs/b1w9pjE-founding-engineer](https://www.ycombinator.com/companies/attimet/jobs/b1w9pjE-founding-engineer)

Attimet (YC F24)是一家位于旧金山的量化交易研究实验室，正在寻找一名创始工程师加入其团队。他们正在建立一个研究实验室，利用数据驱动系统和机器学习来改进传统的、基于直觉的交易方法，以测试金融市场（特别是期权）中的想法。

该职位涉及从头开始构建数据摄取、模型训练、策略模拟和实时执行的核心系统。工程师还将设计基础设施以加速研究，包括特征存储、实验跟踪和反馈循环。他们将与创始人紧密合作，在实际市场中测试预测。

Attimet 正在寻找具有构建分布式计算或 ML 管道等实际系统经验，并且精通 Python、C++、Rust 和云技术的人才。他们重视迭代速度、清晰的抽象和强大的系统设计。不需要事先的金融经验，但好奇心和解决复杂问题的意愿至关重要。

该公司强调快节奏、所有权驱动的环境，尽量减少繁文缛节。该职位提供 10 万美元至 15 万美元的薪水，以及 0.25% 至 1.00% 的股权。这是一个全职职位，面向美国公民或签证持有者开放，包括应届毕业生。Attimet 的目标是构建一个在流动性市场中进行实验的平台，弥合理论研究和实际应用之间的差距。

---

## 8. Terpstra 键盘

**原文标题**: Terpstra Keyboard

**原文链接**: [http://terpstrakeyboard.com/web-app/keys.htm](http://terpstrakeyboard.com/web-app/keys.htm)

本文介绍了Terpstra键盘WebApp，它是对20世纪80年代末设计的实体Terpstra键盘的数字化再现。该Web应用程序最初由James Fenn开发，随后由Brandon Lewis、Bo Constantinsen和陈谷望改进和修改。Scott Thompson和Ozan Yarman博士提供了样本。当前版本1.5.2的时间跨度为2015年1月至2019年5月。该WebApp以GPL-3.0许可发布，属于自由/开放源码软件，欢迎用户通过GitHub下载、派生、贡献和改进该项目。

---

## 9. Framework Laptop 12 评测

**原文标题**: Framework Laptop 12 review

**原文链接**: [https://arstechnica.com/gadgets/2025/06/framework-laptop-12-review-im-excited-to-see-what-the-2nd-generation-looks-like/](https://arstechnica.com/gadgets/2025/06/framework-laptop-12-review-im-excited-to-see-what-the-2nd-generation-looks-like/)

评测：Framework Laptop 12

本次评测考察了 Framework Laptop 12，这是 Framework 最新推出的模块化、可维修笔记本电脑。Laptop 12 以其色彩鲜艳的塑料外壳脱颖而出，提供了比其金属前代产品更平易近人的设计。它保留了 Framework 的标志性功能，例如通过扩展卡自定义端口、易于拆卸和 Linux 支持。

该评测称赞了 Laptop 12 的设计和坚固的结构，但也指出了一些缺点。12.2 英寸触摸屏虽然亮度很高，但边框很厚，色域平庸。键盘缺少背光灯和指纹传感器，这对于它的价格来说是一个重大的疏忽。虽然维修和升级相对容易，但该笔记本电脑使用单个 RAM 插槽，限制了内存带宽和容量。

得益于其第 13 代英特尔酷睿处理器，性能足以满足基本计算需求，但在要求苛刻的任务和游戏中落后于较新的芯片。单个 RAM 插槽会影响 GPU 性能。电池续航能力尚可，在测试中持续约 10 小时。

主要的批评集中在价格上。尽管 Laptop 12 的定位是更实惠的选择，但其价格与 MacBook Air、Surface Laptop 甚至 Framework Laptop 13 大致相同，同时提供了不太完善的用户体验。评测人员得出结论，虽然 Laptop 12 很有吸引力，但其成本削减妥协和相当的价格使其不如竞争对手那样具有吸引力。

---

## 10. 为人工智能编写文档：最佳实践

**原文标题**: Writing documentation for AI: best practices

**原文链接**: [https://docs.kapa.ai/improving/writing-best-practices](https://docs.kapa.ai/improving/writing-best-practices)

本文概述了编写对人类读者和AI/LLM都有效的文档的最佳实践，尤其是在Kapa等检索增强生成 (RAG) 系统中。高质量的文档至关重要，因为它直接影响 AI 回复的质量；糟糕的文档会导致糟糕的 AI 答案。

本文详细介绍了 AI 系统如何处理文档：摄取、查询处理、检索和答案生成。它强调 AI 系统处理的是文本块，依赖于内容匹配，可能会遗漏隐含的联系，并且无法推断未说明的信息。因此，文档应明确、自包含且上下文完整。

主要建议包括：

*   **使用标准化的语义 HTML**: 确保正确使用 HTML 元素以获得清晰的结构。
*   **首选 HTML 或 Markdown 而不是 PDF**: 简化机器解析。
*   **创建对爬虫友好的内容**: 尽量减少复杂的 UI 元素和 JavaScript。
*   **确保语义清晰**: 使用描述性标题和有意义的 URL。
*   **为视觉内容提供文本等效内容**: 包括图表和屏幕截图的文本描述。
*   **保持布局简单**: 避免依赖视觉定位的布局。

本文还讨论了内容设计挑战，强调了将相关信息放在一起以避免上下文依赖的重要性、使用一致的术语以提高语义可发现性、明确说明假设以避免隐含的知识差距以及提供基于文本的视觉信息替代方案。最后，它建议避免依赖布局或表格结构的信息。通过实施这些实践，文档可以显著提高 AI 的准确性和可用性。

---

## 11. 人工智能代理的成功率是否存在半衰期？

**原文标题**: Is There a Half-Life for the Success Rates of AI Agents?

**原文链接**: [https://www.tobyord.com/writing/half-life](https://www.tobyord.com/writing/half-life)

Toby Ord的文章探讨了人工智能代理的成功率是否表现出“半衰期”特征，借鉴了Kwa等人（2025年）的实证研究。Kwa等人发现了一个指数趋势，人工智能能够解决的任务长度每7个月翻一番，他们使用了一套通过人类任务完成时间衡量的研究工程任务。

Ord提出了一个简单的数学模型来解释这些结果：在人类任务时间的每一分钟内，存在一个恒定的失败率。这意味着成功率呈指数下降，并引出了人工智能代理“半衰期”的概念，代表成功率为50%的任务长度。该模型表明，较长的任务失败是由于一系列子任务，任何一个子任务的失败都会导致整体任务失败。

Ord强调，恒定风险率模型准确地预测了不同成功率（例如，80% vs. 50%）下时间范围之间的关系。他指出，虽然Kwa等人观察到S形衰减曲线，但指数函数以更少的参数同样可以很好地拟合数据。有趣的是，人类的表现似乎比人工智能的表现更能随着任务长度而扩展，这可能表明当前人工智能范式存在效率低下。

文章总结道，如果恒定风险率模型成立，它就能预测成功率，表明人工智能的表现可以用半衰期来描述，并间接支持了任务由一系列没有错误恢复的顺序子任务组成的想法。偏离指数衰减的情况可以为了解人工智能代理的缺点和优势提供见解。

---

## 12. MiniMax-M1 开源大模型，混合注意力推理模型

**原文标题**: MiniMax-M1 open-weight, large-scale hybrid-attention reasoning model

**原文链接**: [https://github.com/MiniMax-AI/MiniMax-M1](https://github.com/MiniMax-AI/MiniMax-M1)

MiniMax-M1：新一代开放权重、大规模混合注意力推理模型，由MiniMax在MiniMax-Text-01模型基础上开发。它拥有4560亿参数（每个token激活459亿），并支持100万token的上下文长度，显著超过DeepSeek R1的能力。其闪电注意力机制实现了高效的测试时计算扩展，在10万token生成长度下，仅消耗DeepSeek R1的25%的FLOPs。

MiniMax-M1通过大规模强化学习(RL)在数学推理和软件工程等多样化任务上进行训练，采用了CISPO，一种剪裁重要性采样权重的创新RL算法，并利用其混合注意力架构来提高RL效率。训练了两个版本，分别具有4万和8万的思考预算。

评估表明，MiniMax-M1优于同类开放权重模型，尤其是在软件工程、工具使用和长上下文任务方面。该论文提供了详细的基准性能数据，并解释了SWE-bench和TAU-bench的评估方法。

该文档包含优化模型使用的建议，建议了针对通用、Web开发和数学场景的特定推理参数（Temperature：1.0，Top_p：0.95）和系统提示。

提供了使用vLLM和Transformers的部署说明，以及使用模型函数调用功能的指南。最后，文档提及了一个具有在线搜索和在线API的聊天机器人、联系方式以及论文引用信息。

---

## 13. A*算法简介

**原文标题**: Introduction to the A* Algorithm

**原文链接**: [https://www.redblobgames.com/pathfinding/a-star/introduction.html](https://www.redblobgames.com/pathfinding/a-star/introduction.html)

本文介绍了A*寻路算法及其与广度优先搜索和Dijkstra算法等其他图搜索算法的关系。它解释了A*用于在由节点（位置）和边（连接）表示的图上找到最短路径。

广度优先搜索向所有方向均匀探索，而Dijkstra算法考虑了移动成本。A*结合了两者的优点，使用启发式方法来估计到目标的距离，同时考虑了到目前为止实际行进的距离。这使得A*能够比向所有方向扩展的Dijkstra算法更有效地向目的地探索。

本文分解了每种算法的核心概念，提供了代码示例和可视化演示。它解释了如何实现广度优先搜索、Dijkstra算法、贪婪最佳优先搜索和A*，突出了它们在扩展搜索边界和优先考虑节点方面的主要区别。它还涵盖了诸如提前退出条件、处理移动成本和重建路径等主题。

最终，本文建议在搜索到单个目的地的路径时，A*是满足大多数寻路需求的一个不错的选择，它可以平衡速度和最优性。如果需要到达所有位置的路径，则建议考虑广度优先搜索或Dijkstra算法。

---

## 14. 简易应用 - 为你和你的朋友制作小型应用

**原文标题**: Scrappy - make little apps for you and your friends

**原文链接**: [https://pontus.granstrom.me/scrappy/](https://pontus.granstrom.me/scrappy/)

"Scrappy" 是一个研究原型，旨在为小型亲友群体创建简单、个性化的应用("Scrapps")。由 John 和 Pontus 开发，其目标是提供一种易于访问的替代方案，以取代大众市场软件和昂贵的企业解决方案。Scrappy 设想了一个任何人都可以创建和修改软件以满足其特定需求的世界，从而培养一种自主感并实现软件生产的民主化。

Scrappy 具有类似于 Figma 或 Google Slides 的直观的基于画布的界面，用户可以在其中拖放交互式对象（按钮、文本字段、标签）并附加 JavaScript 代码以实现自定义行为。应用是多人游戏，具有共享状态和实时更新。 Scrapps 的示例包括儿童算术练习、活动参与者计数器、会议成本时钟和家务跟踪器。

该项目的灵感来自 Notion 和 tldraw 等工具的简洁性，以及“具有脚本的媒体”环境的交互性。Scrappy 的设计宗旨是用户友好，侧重于直接操作和用户控制，有意避免以人工智能为中心的代码生成方法。

目标用户是“DIY 爱好者”，他们喜欢定制自己的环境并创建自己的工具。Scrappy 旨在降低应用程序开发的门槛，使用户无需广泛的编程知识即可创建解决方案。本文还将 Scrappy 与大众市场应用程序和 AI 编写的应用程序进行了对比，突出了 Scrappy 在定制、协作以及易于理解和修改方面的优势。最终，Scrappy 鼓励向“自制”思维转变，用户可以为特定需求创建个性化的共享应用程序。

---

## 15. 基于大型模型的实时行为分块

**原文标题**: Real-time action chunking with large models

**原文链接**: [https://www.pi.website/research/real_time_chunking](https://www.pi.website/research/real_time_chunking)

本文介绍了一种名为“实时分块”(RTC)的新算法，该算法由Physical Intelligence的研究人员开发，旨在解决使用视觉-语言-动作(VLA)模型的机器人实时控制难题。VLA模型虽然在开放世界泛化方面前景广阔，但计算成本高且速度慢，阻碍了对机器人技术至关重要的实时性能。

核心问题在于VLA生成的动作块在切换时如何保持一致性。推理延迟意味着新的动作块可能与机器人当前状态不兼容，从而可能导致错误或不安全动作。

RTC通过将问题定义为图像修复任务来解决这个问题。它冻结新动作块的初始动作，使其与先前动作块中已执行的动作相匹配，然后使用VLA模型（特别是扩散或流模型）来“填充”剩余的动作，在鼓励一致性的同时允许模型对新信息做出反应。

研究人员在各种任务中测试了RTC，包括诸如点燃火柴和插入以太网电缆之类的精密任务，并证明它可以在不牺牲精度的情况下显着加快执行速度。重要的是，即使人为地注入延迟，RTC仍然保持稳健性，证明了其对各种推理延迟的适应能力，这对于扩大模型规模或使用基于云的推理至关重要。他们表明，如果没有RTC，即使在高延迟条件下，诸如时间集成之类的简单平滑技术也会失效。RTC提供了一种更简单、有效的实时VLA推理策略，并强调了随着模型持续增长，需要更复杂的实时推理机制。

---

## 16. 本地托管联网服务器

**原文标题**: Locally hosting an internet-connected server

**原文链接**: [https://mjg59.dreamwidth.org/72095.html](https://mjg59.dreamwidth.org/72095.html)

这是一个网页片段，具体来说是验证码挑战，并非文章。关键在于用户触发了验证码检测，可能是由于类似自动化的行为或被安全系统标记。用户必须完成验证码以证明其是人类，并验证其继续操作的请求。页面提示验证码选择是“半随机”的，表明采用了概率安全方法。本质上，这段代码片段的目的是阻止机器人并确保与网站或服务的合法人类互动。

---

## 17. 本田成功进行实验性可重复使用火箭的发射和着陆

**原文标题**: Honda conducts successful launch and landing of experimental reusable rocket

**原文链接**: [https://global.honda/en/topics/2025/c_2025-06-17ceng.html](https://global.honda/en/topics/2025/c_2025-06-17ceng.html)

本田技术研究所有限公司于2025年6月17日在日本北海道大树町成功进行了其自主研发的实验性可重复使用火箭的发射和着陆试验。 这标志着本田首次在达到约300米高度后成功实现火箭着陆。 该试验旨在展示火箭可重复使用性的关键技术，包括飞行稳定性和着陆能力。

该火箭达到271.4米的高度，着陆点距离目标37厘米以内，飞行时长为56.6秒。 本田实现了其预期的火箭行为，并在上升和下降过程中获得了宝贵的数据。

本田将太空技术视为利用其核心技术并实现全球人民的“梦想”和“潜力”的一种方式。 他们的研究包括循环可再生能源系统、用于太空的机器人技术和可重复使用的火箭。 火箭研究的灵感来自本田工程师，他们旨在利用核心技术发射卫星，从而有可能提供与其他本田业务兼容的服务。

本田认为对卫星发射火箭的需求日益增长，并相信可重复使用的火箭将有助于可持续运输。 虽然仍处于基础研究阶段，尚未做出商业化决定，但本田的目标是在2029年之前实现亚轨道发射能力。

本田全球CEO三部敏宏对试验的成功表示高兴，并强调了公司对新挑战、价值创造以及解决环境和安全问题的承诺。 公司在试验期间采取了广泛的安全措施，包括建立禁区和为火箭配备安全系统。

---

## 18. 我用机器学习数了蒙古所有的蒙古包。

**原文标题**: I counted all of the yurts in Mongolia using machine learning

**原文链接**: [https://monroeclinton.com/counting-all-yurts-in-mongolia/](https://monroeclinton.com/counting-all-yurts-in-mongolia/)

受蒙古帝国相关播客的启发，作者决定利用机器学习技术统计蒙古国境内的所有蒙古包（毡房）。由于缺乏现成的蒙古包数量数据，作者凭借对机器学习的有限理解，开启了一项个人项目。

该项目涉及训练一个模型，以识别谷歌地图卫星图像中的蒙古包。最初，作者使用开源标注工具Label Studio手动标记了数百个地图瓦片中的蒙古包，从而为YOLOv11目标检测模型创建训练数据。最初的模型并不准确，因此作者专注于缩小搜索范围以降低计算负载。他们利用Overpass Turbo和geopandas的数据，专注于人口稠密地区。

为了改进标注过程，作者为Label Studio创建了一个模型后端，本质上是一个API，它使用训练好的模型预先标注新瓦片中的蒙古包，从而显著加快了数据标注速度。这种反馈循环使得能够创建包含超过10,000个标注蒙古包的更大的数据集。

随着数据集的增长，作者将模型训练转移到vast.ai，租用GPU并利用Docker进行简化的训练。模型在临时容器中进行训练。完成的模型及其元数据被上传到S3以供后续分析。

最后，作者在多个服务器上通过Docker Swarm部署了经过优化的模型，利用它们组合的CPU能力来处理覆盖蒙古国的海量卫星瓦片并统计蒙古包的数量。

---

## 19. 叠加推理：对持续性思维链的视角

**原文标题**: Reasoning by Superposition: A Perspective on Chain of Continuous Thought

**原文链接**: [https://arxiv.org/abs/2505.12514](https://arxiv.org/abs/2505.12514)

本文《叠加推理：连续思维链的理论视角》探讨了大型语言模型（LLM）中，连续思维链（CoT）在推理任务中相对于离散CoT的理论优势。 尽管现有理论解释了离散CoT的优势，但这项工作侧重于为什么*连续* CoT可能优于它们。

作者证明，使用连续CoT的两层Transformer可以在D步内（其中D是图的直径）解决有向图可达性问题。 相比之下，离散CoT需要O(n^2)步（n是顶点数），且使用恒定深度Transformer。 核心论点是，连续CoT利用“叠加”，其中每个“思维向量”同时编码多个搜索前沿，从而有效地执行并行广度优先搜索（BFS）。 另一方面，离散CoT被迫采样单个路径，导致顺序搜索，这可能会更慢并且陷入局部最优。

实证实验证实了该理论结构，表明即使没有明确的监督，在连续CoT的训练过程中，多个搜索前沿的编码作为叠加状态自然出现。 这突出了连续CoT在同时有效探索多个潜在解决方案方面的内在优势，从而在复杂的推理任务中获得更好的性能。

---

## 20. Show HN: Trieve CLI – 用于 PDF 搜索的基于终端的 LLM 代理循环

**原文标题**: Show HN: Trieve CLI – Terminal-based LLM agent loop with search tool for PDFs

**原文链接**: [https://github.com/devflowinc/trieve/tree/main/clients/cli](https://github.com/devflowinc/trieve/tree/main/clients/cli)

此“Show HN”提交介绍 Trieve CLI，一个基于终端的命令行界面，旨在创建 LLM（大型语言模型）代理循环。其主要亮点是集成了专门为 PDF 定制的搜索工具。这意味着用户可以直接从终端利用 LLM 分析和交互 PDF 文档中包含的数据。

Trieve CLI 位于 GitHub 的 "devflowinc/trieve" 下，旨在通过命令行界面使 LLM 驱动的 PDF 分析更易于访问和高效。该提交显示出对该项目的浓厚兴趣，GitHub 上有 2.3k 星星和 199 个分支。

本质上，Trieve CLI 允许开发人员和用户构建自定义代理，这些代理可以搜索、处理和响应 PDF 文档中的信息，所有这些都可以在他们方便的终端上完成。“代理循环”功能表明一个迭代过程，其中 LLM 代理基于 PDF 内容不断搜索、分析和完善其理解。

---

## 21. 2025年重温明斯基的《心智社会》

**原文标题**: Revisiting Minsky's Society of Mind in 2025

**原文链接**: [https://suthakamal.substack.com/p/revisiting-minskys-society-of-mind](https://suthakamal.substack.com/p/revisiting-minskys-society-of-mind)

无法访问文章链接。

---

## 22. 经过数百万年，为什么食肉植物仍然这么小？

**原文标题**: After millions of years, why are carnivorous plants still so small?

**原文链接**: [https://www.smithsonianmag.com/articles/carnivorous-plants-have-been-trapping-animals-for-millions-of-years-so-why-have-they-never-grown-larger-180986708/](https://www.smithsonianmag.com/articles/carnivorous-plants-have-been-trapping-animals-for-millions-of-years-so-why-have-they-never-grown-larger-180986708/)

本文探讨了食肉植物的进化历史和体型限制，解释了为什么它们没有进化成小说中描绘的食人巨型植物。食肉植物至少存在了3400万年，拥有多种捕食机制，如粘性叶子（茅膏菜）、捕蝇夹（维纳斯捕蝇草）和瓶状结构。化石证据，包括琥珀中保存的叶片和花粉，揭示了它们古老的起源以及在不同植物谱系中的重复进化。

尽管历史悠久且适应性强，食肉植物的体型仍然相对较小。本文解释说，食肉性是对贫瘠营养环境的一种特殊适应，植物通过动物来源的营养物质来补充光合作用。它们体型较小的关键原因是，较大的植物需要更肥沃的土壤，从而抵消了食肉的必要性。换句话说，它们之所以是食肉植物，是因为它们需要在贫瘠的土壤中获取额外的营养，如果土壤足够肥沃，它们就不需要是食肉植物。

文章还强调了实际的限制。例如，干旱环境中的植物可能缺乏产生捕获所需的粘性粘液的水分。此外，肥沃土壤中的植物已经从腐烂的有机物中获得了足够的营养，这使得食肉变得不必要，甚至可能因为获得过多营养而有害。因此，食肉植物代表着对特定生态位的成功适应，它们优化了在资源有限的环境中的生存，而不是追求巨大的体型。

---

## 23. 格鲁格脑开发者 (2022)

**原文标题**: The Grug Brained Developer (2022)

**原文链接**: [https://grugbrain.dev/](https://grugbrain.dev/)

头脑简单的开发者：从外行视角看软件开发，强调简单和实用，而非抽象的复杂性。自知的“小脑瓜”Grug优先对抗“复杂性恶魔”，他认为复杂性恶魔源于过度聪明的开发者和项目经理引入的不必要的抽象。

对抗复杂性的主要武器是“不”，拒绝那些没有显著价值的功能或抽象。“好的”是妥协，选择以最少的代码交付最大价值的80/20解决方案。Grug警告不要过早地重构代码，主张耐心等待，让切割点自然出现。

测试至关重要，但Grug不喜欢测试驱动开发（TDD）的教条。他更喜欢集成测试而非单元测试（他认为单元测试很脆弱），也不喜欢难以调试的端到端测试。他提倡在系统稳定后专注于集成测试，并为核心功能构建一个精选的端到端测试套件。敏捷是可以接受的，但不是万能药，大型重构则受到怀疑。

Grug引用了切斯特顿的栅栏，敦促开发者在盲目重构之前理解现有代码的目的。他质疑微服务的效用，并赞扬调试器和代码补全等强大工具的价值。类型系统主要因其代码补全功能而被重视，而非抽象的正确性。最终，Grug提倡一种平衡、务实的方法，重视可用的代码而非理论上的纯粹性。

---

## 24. S表达式的另类解读

**原文标题**: A different take on S-expressions

**原文链接**: [https://gist.github.com/tearflake/569db7fdc8b363b7d320ebfeef8ab503](https://gist.github.com/tearflake/569db7fdc8b363b7d320ebfeef8ab503)

本文介绍S-expr，一种S-表达式的变体，其扩展旨在提高代码可读性，尤其对于初学者。S-表达式是诸如Lisp等语言的基础，它使用带括号的符号来表示嵌套的列表数据结构。

S-expr保留了原子和列表的核心概念，但在字符串、注释以及一种名为“转置块”的新概念的处理方式上引入了增强。字符串可以是单行的（使用`"`）或多行的（使用`"""..."""`），其中多行字符串由包含字符串内容的矩形定义。类似地，注释使用`/`代替`"`，用于单行和多行注释，并提供相同的矩形边界。

最显著的特性是“转置块”，由垂直堆叠的`*`序列表示。这些块有效地交换行和列，允许水平方向表达式的垂直缩进。这旨在解决S-表达式中常见的长序列结束括号引起的视觉混乱。本文还介绍了“转置线”，包含在单个`*`字符内，被视为转置块内的单行表达式。目标是创建更具可读性、视觉结构化的S-表达式，尽管与标准Lisp方言相比复杂性有所增加。本文总结认为，简单性和可用性之间的权衡是合理的。

---

## 25. 展示HN: Lstr – 一个用 Rust 编写的现代、交互式 tree 命令

**原文标题**: Show HN: Lstr – A modern, interactive tree command written in Rust

**原文链接**: [https://github.com/bgreenwell/lstr](https://github.com/bgreenwell/lstr)

Lstr：一款快速、极简且交互式的目录树查看器，用 Rust 编写，灵感来自经典的 `tree` 命令。它提供传统的树状视图和交互式的 TUI 模式，方便通过键盘进行浏览。Lstr 默认采用并行目录扫描，优先考虑速度。

主要特性包括可选的丰富信息显示，例如文件图标（需要 Nerd Font）、权限和大小。Git 集成可在树中直接显示文件状态。智能过滤遵循 `.gitignore` 文件，并允许控制递归深度和仅显示目录。

安装方法是克隆存储库并使用 `cargo install`。 使用方法简单，使用 `lstr [OPTIONS] [PATH]` 可查看经典视图，使用 `lstr interactive [OPTIONS] [PATH]` 可查看 TUI。 TUI 提供直观的键盘控件，用于导航和目录展开。

该工具与 `fzf`（用于模糊查找）和 `less` 或 `bat`（用于分页大型树）等其他命令行工具集成良好。 提供了一个 shell 函数 `lcd`，用于将 lstr 用作可视化的 `cd` 命令，从而实现交互式目录更改。

性能通过使用 `rayon` 线程池的并行目录遍历进行优化，并可通过 `RAYON_NUM_THREADS` 环境变量控制线程数。

---

## 26. 一个汉堡人的慕尼黑视角

**原文标题**: Munich from a Hamburger's Perspective

**原文链接**: [https://mertbulan.com/2025/06/14/munich-from-a-hamburgers-perspective/](https://mertbulan.com/2025/06/14/munich-from-a-hamburgers-perspective/)

汉堡人视角的慕尼黑之旅：历史、自然、博物馆与城市生活的对比（兼带主观偏好）

---

## 27. 构建高效的AI智能体

**原文标题**: Building Effective AI Agents

**原文链接**: [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)

Anthropic文章：利用大型语言模型构建高效AI Agent。它区分了工作流（预定义的代码路径）和Agent（动态的、模型驱动的过程）。文章建议从简单的解决方案入手，仅在必要时增加复杂性，并警告不要过度依赖框架，这可能会掩盖底层代码。

文章介绍了一系列构建模块和工作流，从增强型LLM（通过检索、工具和记忆进行增强）开始。工作流包括提示链、路由、并行化（分段和投票）、协调器-工作者以及评估器-优化器。Agent被认为最适合步骤不可预测的开放式任务，强调清晰的工具文档和测试的重要性。

文章重点介绍了两个有前景的应用：客户支持（将聊天机器人与外部数据和操作集成）和编码Agent（解决GitHub问题并提高代码质量）。两者都利用了工具集成、清晰的成功标准和人工监督。

主要要点是：优先考虑简洁性，确保规划步骤的透明性，并仔细设计Agent-计算机接口（ACI）。构建适合您需求的系统至关重要，框架应被战略性地使用，而不是取代对底层代码的理解。

---

## 28. 想一个数字

**原文标题**: Think of a Number

**原文链接**: [https://xenaproject.wordpress.com/2025/01/20/think-of-a-number/](https://xenaproject.wordpress.com/2025/01/20/think-of-a-number/)

在此博文中，数学家“xenaproject”对人工智能通用智能（AGI）即将到来的说法表示怀疑，特别是关于人工智能执行高等数学的能力。作者批评了将人工智能在本科水平数学问题上的表现等同于真正的数学理解和研究能力的倾向。他们认为，目前的人工智能，主要是大型语言模型（LLM），擅长基于现有数据进行释义和模式匹配，这种技能足以应付本科考试，但不足以进行需要原创性思维的博士级研究。

为了评估人工智能真正的数学能力，作者建议创建一个“秘密数据库”，其中包含超出本科水平的具有挑战性的数论问题，这些问题需要本科课程通常不教授的技能。这些问题应具有非负整数答案，以方便评估人工智能的回答。作者向博士或博士以上级别的数论专家征集贡献。

目标是让人工智能系统尝试解决这些问题并公开报告他们的分数，之后将发布这些问题。这种方法旨在区分真正的数学理解和作者认为LLM的特征的“随机鹦鹉”行为。作者强调了对FrontierMath等数据集的担忧，质疑它们的质量以及由于行业参与而产生的潜在偏见。提交问题的截止日期为2025年2月20日。

---

## 29. 谷歌翻译能告诉我们关于氛围编码的什么

**原文标题**: What Google Translate can tell us about vibecoding

**原文链接**: [https://ingrids.space/posts/what-google-translate-can-tell-us-about-vibecoding/](https://ingrids.space/posts/what-google-translate-can-tell-us-about-vibecoding/)

英格丽德的文章《谷歌翻译能告诉我们关于氛围编码的什么》将机器翻译对翻译行业的影响，与大型语言模型 (LLM) 对编程的潜在影响进行了类比。文章认为，尽管大型语言模型似乎威胁要取代程序员，但仔细观察翻译领域会发现一个更为微妙的现实。

作者以谷歌翻译为例，指出尽管它取得了进步，但并没有消除对人工翻译和口译的需求。相反，它改变了他们的角色。虽然谷歌翻译擅长基本的词语替换，但它在语境、歧义和文化敏感性方面表现欠佳。人工翻译对于驾驭这些复杂性、确保准确且符合文化规范的沟通至关重要。

同样，作者认为编程不仅仅是生成代码。与翻译人员一样，程序员也需要将“柔软的人类”需求翻译成计算机的绝对语言。他们还管理新的抽象概念，并处理人类沟通中固有的模糊性。

文章认为，大型语言模型就像谷歌翻译一样，可以成为程序员的有用工具，尤其是在建议替代措辞或生成代码片段等任务中。然而，它们无法完全取代人类程序员，因为人类程序员对于理解语境、消除歧义和处理复杂的解决问题至关重要。作者还警告说，不要不加批判地接受这些工具，并指出伦理问题以及人工智能在细微差别有限的情况下可能产生不负责任的输出。

---

## 30. OpenSERDES – 基于Verilog的开源硬件串行器/解串器 (2020)

**原文标题**: OpenSERDES – Open Hardware Serializer/Deserializer (SerDes) in Verilog (2020)

**原文链接**: [https://github.com/SparcLab/OpenSERDES](https://github.com/SparcLab/OpenSERDES)

OpenSERDES是一个开源的串行器/解串器(SerDes)硬件实现，用于高速通信，使用Verilog HDL编写，目标是Skywater OpenPDK 130nm工艺。它将并行数据转换为串行流进行传输，并在接收端将其转换回并行数据。该设计使用OpenLane进行综合，使用Virtuoso Cadence进行布局。

该项目包括几个关键组件：一个串行器和一个解串器，一个基于反相器的发送器(TX)驱动器，一个接收器(RX)，该接收器具有用于感应微弱信号的电阻反馈反相器，随后是一个用于增益的CMOS反相器，一个用于数据采样的主从D触发器(DFF)，以及一个过采样时钟数据恢复(CDR)电路，用于从接收到的数据中提取时钟信号。CDR利用数据跳变来调整时钟频率。

该存储库包含TX驱动器的GDS、SPICE、网表和OA文件，串行器、解串器和CDR的综合Verilog文件（使用OpenLane生成），以及电阻反馈反相器、DFF和NAND门实现的详细信息。该项目旨在为高速数据传输提供一个完整且开源的SerDes解决方案。

---

## 31. 现在可能是学习软件开发的最佳时机。

**原文标题**: Now might be the best time to learn software development

**原文链接**: [https://substack.com/home/post/p-165655726](https://substack.com/home/post/p-165655726)

无法访问文章链接。

---

## 32. 3D打印设备无需电源即可将白噪声分解成声学彩虹

**原文标题**: 3D-printed device splits white noise into an acoustic rainbow without power

**原文链接**: [https://phys.org/news/2025-06-3d-device-white-noise-acoustic.html](https://phys.org/news/2025-06-3d-device-white-noise-acoustic.html)

研究人员开发了一种名为声学彩虹发射器(ARE)的3D打印设备，该设备能够被动地将宽带白噪声分解为不同的声音频率，从而创造出一种“声学彩虹”。ARE发表在《科学进展》上，它利用通过计算形态发生学设计的复杂散射体——一种利用算法进行结构优化和有限元分析的过程。这种方法可以在没有电力或有源元件的情况下精确控制声音的发射。

当暴露于发射白噪声的点声源时，ARE的功能类似于棱镜，将不同的声音频率导向不同的方向。与许多需要有源设备或仅限于封闭环境的现有声学系统不同，ARE可以在自由空间中控制声音，模仿天然耳朵复杂的塑形声音能力。

研究人员采用拓扑优化、基于波的建模和3D打印技术，创造出以新颖方式控制声音的复杂结构。他们还设计了一种lambda分离器，可以将低频和高频声波导向不同的方向。这两种设备都是被动运行的，仅依赖于结构的硬塑料表面和声波之间的相互作用。

这项研究展示了计算形态发生学在精确塑造声场方面的潜力，为各种波传感和控制应用提供了宝贵的见解。研究人员强调，这些设备展示了被动结构的巧妙排列如何在无需耗能方法的情况下有效控制声音。

---

## 33. 对好调节器定理的简明解释

**原文标题**: A Straightforward Explanation of the Good Regulator Theorem

**原文链接**: [https://www.lesswrong.com/posts/JQefBJDHG6Wgffw6T/a-straightforward-explanation-of-the-good-regulator-theorem](https://www.lesswrong.com/posts/JQefBJDHG6Wgffw6T/a-straightforward-explanation-of-the-good-regulator-theorem)

本文旨在以简明易懂的方式解释康南特和艾希比1970年论文中的“良 регулятор定理”，该定理指出：“系统中的每一个良 регулятор都必须是该系统的一个模型。” 作者旨在阐明该定理，因为原始论文晦涩难懂，且缺乏易于理解的解释。

该定理关注一个系统，其中结果 Z 受系统变量 S 和 регулятор变量 R 的影响（用贝叶斯网络表示，箭头表示影响）。目标是通过选择条件概率分布 P(R|S) 来设计一个 регулятор R，以便在 S 引入的随机性下，引导 Z 朝着期望的结果发展。

根据康南特和艾希比的观点，“良” регулятор可以最大限度地减少结果变量 Z 的香农熵（使结果可预测），并且不会不必要地复杂（例如，如果确定性策略能够达到相同的结果，则优先选择确定性策略而不是随机策略）。

定理本身断言，如果一个 регулятор 是“良” регулятора，那么 R 可以被描述为 S 的确定性函数，这意味着对于 S 的每一个状态，R 输出特定动作的概率要么是 0 要么是 1。

该证明的关键在于熵的凹性：增加两个结果之间概率的不平衡（使一个结果比另一个结果更可能发生）必然会降低总体熵。引理指出，一个“良” регулятор，即能够导致 Z 的熵达到最低值的 регулятор，必须确保 Z 是 S 的一个确定性函数（H(Z|S)=0）。

---

## 34. 大脱钩（或你的点击量下降但曝光量上升的原因）

**原文标题**: The Great Decoupling (Or Why Your Clicks Are Down and Impressions Up)

**原文链接**: [https://ahrefs.com/blog/the-great-decoupling/](https://ahrefs.com/blog/the-great-decoupling/)

瑞安·劳的文章《大脱钩》解释了SEO中最近出现的一种现象：展示次数增加，而点击次数减少，在Google Search Console报告中形成了“鳄鱼嘴”形状。这种脱钩主要归因于谷歌AI概览的广泛推出。

AI概览使网站有两次记录展示次数的机会：一次在传统的搜索结果中，另一次作为AI概览中的引用。然而，AI概览也在搜索结果中直接回答用户的问题，从而导致点击率大幅下降（在Ahrefs的研究中约为34.5%），因为用户不再需要访问网站来查找他们所需的信息。

文章强调，这一趋势与3月份核心更新后AI概览在搜索结果中日益增加的出现相吻合。劳建议使用Ahrefs的工具，特别是Site Explorer和Brand Radar，来识别AI概览正在影响排名和可见性的关键词。这使得营销人员能够看到哪些关键词通过自然结果和AI概览产生展示次数，从而可能突出显示点击次数正在丢失的领域。

尽管点击次数有所下降，劳还是提供了一个充满希望的视角。Ahrefs的数据表明，来自AI搜索的流量转化率远高于（高出23倍）传统搜索流量。他总结说，虽然内容营销策略需要调整，但业务增长的根本驱动因素仍然是对产品和服务的需求，而不仅仅是对博客的点击。

---

## 35. 发布 2.5 Flash 和 2.5 Pro 正式版，并推出 Gemini 2.5 Flash-Lite

**原文标题**: Making 2.5 Flash and 2.5 Pro GA, and introducing Gemini 2.5 Flash-Lite

**原文链接**: [https://blog.google/products/gemini/gemini-2-5-model-family-expands/](https://blog.google/products/gemini/gemini-2-5-model-family-expands/)

2025年6月17日，谷歌宣布 Gemini 2.5 Flash 和 Pro 模型正式上线，并推出 Gemini 2.5 Flash-Lite 的预览版。

Gemini 2.5 Flash 和 Pro 现已稳定可靠，可投入生产使用，并经过 Spline、Rooms、Snap 和 SmartBear 等开发者的测试。

Gemini 2.5 Flash-Lite 作为最具成本效益且速度最快的 2.5 模型推出，擅长对延迟敏感的任务，如翻译和分类。它在编码、数学、科学、推理和多模态基准测试中超越了 2.0 Flash-Lite，同时还提供比 2.0 Flash-Lite 和 2.0 Flash 更低的延迟。它保留了 Gemini 2.5 的关键特性，包括动态思维预算、工具连接（Google 搜索、代码执行）、多模态输入和 100 万 token 的上下文长度。

Gemini 2.5 Flash-Lite 的预览版可在 Google AI Studio 和 Vertex AI 中获取，同时也可获取正式上线的 2.5 Flash 和 Pro。 2.5 Flash 和 Pro 也可以在 Gemini 应用程序中使用。Google 搜索中已实施定制版本的 2.5 Flash-Lite 和 Flash。

---

## 36. 复活死亡的种子追踪器并找到300万用户

**原文标题**: Resurrecting a dead torrent tracker and finding 3M peers

**原文链接**: [https://kianbradley.com/2025/06/15/resurrecting-a-dead-tracker.html](https://kianbradley.com/2025/06/15/resurrecting-a-dead-tracker.html)

作者在下载Linux ISO时发现了许多失效的Tracker。出于好奇，他们决定复活一个，购买了被列为“找不到主机”的域名`open.demonii.si`，并在VPS上设置了开源软件`opentracker`。令作者惊讶的是，即使在启动Tracker之前，UDP端口1337就立即涌入了大量流量。启动Tracker后，其迅速达到170万个种子和310万个对等点的高峰，突显了大量Torrent客户端仍然配置为使用这个已失效的Tracker。

随后，作者分析了托管Tracker的合法性，承认存在版权侵权相关的潜在法律风险，特别是关于诱导侵权。与宣传受版权保护内容的公开Torrent网站不同，托管未公开的Tracker基础设施提出了一个更模糊的法律案例。

由于担心使用信用卡购买域名而被识别身份，作者决定关闭VPS并放弃该域名。作者最后建议其他人可以注册`open.demonii.si`和类似的未声明域名，作为一项潜在的“公共服务”，含蓄地提到了支持Torrent活动的可能性。

---

## 37. 中性氮同素异形体六氮C2h-N6的制备

**原文标题**: Preparation of a neutral nitrogen allotrope hexanitrogen C2h-N6

**原文链接**: [https://www.nature.com/articles/s41586-025-09032-9](https://www.nature.com/articles/s41586-025-09032-9)

本文报道了一种中性氮同素异形体，六氮(N6)的成功制备，这是追求高能量密度材料的一个重要成就。N6在室温下通过氯或溴与叠氮化银(AgN3)的气相反应合成，然后在10 K的氩基质中或77 K的纯薄膜中捕获。

合成的N6通过红外(IR)和紫外-可见(UV-Vis)光谱进行表征，并辅以15N同位素标记实验和先进的计算方法。红外光谱显示了归属于N6的独特谱带，这些谱带在用436 nm光照射后消失。同位素标记证实了N6分子中存在两个叠氮基团(N3)。紫外-可见光谱显示了与N6的计算预测电子激发一致的跃迁。

使用CCSD(T)/cc-pVTZ的计算分析确定C2h-N6反式构象体是最稳定的形式。势能面和电子密度计算提供了对N6的键合和稳定性的深入了解。分解成三个N2分子的相对较高的计算势垒（ΔG‡298K = 14.8 kcal mol−1）表明具有相当大的动力学稳定性，这与实验观察到的N6在液氮温度下作为纯薄膜的持久性相印证。

N6的成功合成和表征有助于基础科学知识，并可能为开发高能量存储材料开辟新的途径。

---

## 38. 为什么JPEG仍然统治网络 (2024)

**原文标题**: Why JPEGs still rule the web (2024)

**原文链接**: [https://spectrum.ieee.org/jpeg-image-format-history](https://spectrum.ieee.org/jpeg-image-format-history)

题为《为何JPEG仍统治网络》的文章，发表于2025年6月17日，探讨了JPEG图像格式在互联网上持久的统治地位，即使在其最初出现三十年后。该文章由“Tedium”新闻通讯的编辑厄尼·史密斯撰写，可能深入探讨了JPEG持续流行的原因，尽管出现了更新、可能更优越的图像格式。

虽然在没有阅读的情况下，文章中的具体论点尚不清楚，但我们可以根据标题和上下文推断，它可能涉及以下方面：

*   **早期采用和生态系统：**JPEG的早期出现和广泛采用创造了一个重要的支持软件、硬件和工作流程的生态系统，使得更新的格式难以取代它。
*   **无处不在的支持：**几乎每个浏览器、操作系统和设备都原生支持JPEG，消除了可能阻碍其他格式采用的兼容性问题。
*   **熟悉度和用户习惯：**用户熟悉JPEG及其相关特性（例如，文件大小与图像质量的权衡），这使得他们不愿意切换。
*   **渐进式改进：**虽然更新的格式可能提供卓越的压缩或功能，但JPEG随着时间的推移已经看到了渐进式改进，使其保持相关性。
*   **性能考量：**对于许多用例，更新格式的性能优势微乎其微，而JPEG的简单性仍然具有吸引力。
*   **替代方案的实际限制：**尽管像WebP或AVIF这样的格式具有理论上的优势，但现实世界的实施复杂性、兼容性怪癖或许可问题可能会限制其更广泛的采用。

文章可能得出结论，尽管更新的图像格式提供了进步，但历史优势、广泛支持、用户熟悉度和持续改进的结合，确保了在可预见的未来，JPEG仍可能在网络上占据重要地位。

---

## 39. 无字证明

**原文标题**: Proofs Without Words

**原文链接**: [https://artofproblemsolving.com/wiki/index.php/Proofs_without_words](https://artofproblemsolving.com/wiki/index.php/Proofs_without_words)

这篇解题技巧维基页面展示了“无字证明”，即通过视觉表示来演示数学定理和恒等式，而无需正式的代数运算。它本质上是一个用图表说明各种数学概念的画廊。

这些证明被分为几个部分：

*   **求和：** 包括前几个奇自然数之和、前 *n* 个正整数之和、尼科马霍斯定理（关于立方和）、五边形数的性质以及斐波那契数恒等式的视觉证明。

*   **几何级数：** 提供各种无限几何级数的视觉证明。

*   **几何：** 展示了毕达哥拉斯定理的多种视觉证明、使用内切圆半径和半周长计算三角形面积的方法、使用边向量计算平行四边形面积的方法、十二边形的面积、一个最短距离问题、梯形的性质、瓦里尼翁定理，以及圆锥体体积的提示。

*   **杂项：** 包括与算术平均数、几何平均数、均方根平均数和调和平均数之间不等式、费马小定理、球极投影和反正切和公式相关的视觉表示。

该页面提供指向 MathOverflow 和 Wolfram MathWorld 等外部资源的链接，以获取一些概念的更详细解释。它还包括一些证明的参考文献和归属。总体目标是通过视觉演示提供直观的理解，从而使复杂的数学思想更容易理解。

---

## 40. 贝塞斯达宣言

**原文标题**: The Bethesda Declaration

**原文链接**: [https://www.science.org/content/blog-post/bethesda-declaration](https://www.science.org/content/blog-post/bethesda-declaration)

无法访问文章链接。

---

## 41. 大型语言模型为领域特定语言 (DSL) 设计者提出了一个有趣的问题。

**原文标题**: LLMs pose an interesting problem for DSL designers

**原文链接**: [https://kirancodes.me/posts/log-lang-design-llms.html](https://kirancodes.me/posts/log-lang-design-llms.html)

大型语言模型对领域特定语言设计的影响
本文探讨了大型语言模型 (LLM) 对领域特定语言 (DSL) 设计的影响。作者认为，LLM 尤其是其在 Python 等语言上的熟练程度，提高了对 DSL 的要求。由于 LLM 在小众语言上的表现不佳，用户可能会放弃 DSL，转而利用 LLM 在更通用语言中生成代码。

随后，作者转向更为乐观的视角，提出了 LLM 时代语言设计的三个方向：

1.  **教导 LLM 关于 DSL**: 使用 Python 作为中介，设计者可以将 DSL 语义翻译成 Python，使 LLM 能够生成可被“提升”到 DSL 中的代码。
2.  **桥接形式与非形式**: DSL 可以通过结合形式化代码（手动编写）与非正式文本提示来与基于 LLM 的工作流程集成。其理念是人类可以编写复杂的部分，而 LLM 处理样板代码。
3.  **为已验证的 LLM 合成进行语言设计**: 为 DSL 设计规范语言，允许 LLM 生成已验证语言的代码。用户可以专注于规范，而不是复杂的 LLM 生成的代码。

作者总结道，DSL 设计必须适应 LLM 的格局，以避免停滞不前。虽然 LLM 通过增加使用小众语言的机会成本带来了挑战，但它们也为语言设计领域的探索和协作开辟了新的途径。

---

## 42. Linux 中理解 NAT 和数据包修改

**原文标题**: Grokking NAT and packet mangling in Linux

**原文链接**: [https://vivekn.dev/blog/grokking-nat-and-packet-mangling-in-linux](https://vivekn.dev/blog/grokking-nat-and-packet-mangling-in-linux)

理解Linux中的NAT和数据包处理

本文“理解Linux中的NAT和数据包处理”阐述了网络地址转换（NAT）的必要性和功能。由于IPv4地址数量有限，NAT允许多个私有网络设备共享一个公共IP地址，从而解决了地址短缺问题。

本文详细介绍了不同类型的NAT：基本/静态NAT（一对一IP转换）、端口地址转换（PAT），它使用端口来区分连接，以及各种锥型NAT类型（完全、受限、端口受限和对称），它们在对传入连接的限制方面有所不同。对称NAT使得WebRTC在没有TURN服务器的情况下难以实现。

作者深入研究了路由器如何实现NAT，重点介绍了Linux中的nftables模块，特别是函数`nf_nat_mangle_udp_packet`和`nf_nat_mangle_tcp_packet`。这些函数确保数据包可写性，必要时扩展缓冲区，替换数据包内容，更新报头长度，并重新计算校验和以保持数据包有效性。Docker使用NAT，通过iptables将主机端口映射到容器端口。

尽管NAT有其优点，但它也有局限性，包括破坏端到端连接、使加密和点对点应用程序复杂化，以及需要内存用于连接映射。IPv6凭借其庞大的地址空间提供了一种解决方案，消除了对NAT的需求，但全球范围内的采用仍在进行中。

---

## 43. 我写了一个编译器

**原文标题**: I Wrote a Compiler

**原文链接**: [https://blog.singleton.io/posts/2021-01-31-i-wrote-a-compiler/](https://blog.singleton.io/posts/2021-01-31-i-wrote-a-compiler/)

本文介绍了作者使用 Go 语言编写一个名为 toybasic 的简化版 BASIC 编译器 的经验。作者具有计算机科学背景和编译器理论知识，旨在在几个小时内创建一个功能完备的编译器。

toybasic 编译器将 BASIC 代码翻译成 Go 代码，并使用三个阶段：词法分析器 (Lexer)、语法分析器 (Parser) 和编译器 (Compiler)。词法分析器使用 `nex` (一个 Go 语言的词法分析器生成器) 将源代码转换为 tokens。语法分析器使用 `goyacc` (yacc 的 Go 版本) 从这些 tokens 构建语法树，确保代码的语法正确性并提供错误消息。然后，编译器遍历语法树并生成等效的 Go 代码。

作者强调了使用 `nex` 和 `goyacc` 等工具来简化词法分析和语法分析过程。文章包括 toybasic 语法的代码片段、词法分析器配置和 `PrintOp` 节点的生成逻辑。它提供了一个 toybasic 程序的示例及其相应的 Go 输出。最终，作者发现该项目具有教育意义且有趣，成功地从头到尾重新创建了一个编译器。整个项目都可以在 GitHub 上找到。

---

## 44. 梵高，AMD Steam Deck APU (2023)

**原文标题**: Van Gogh, AMD's Steam Deck APU (2023)

**原文链接**: [https://chipsandcheese.com/p/van-gogh-amds-steam-deck-apu](https://chipsandcheese.com/p/van-gogh-amds-steam-deck-apu)

本文深入分析了AMD为Steam Deck定制的“梵高”(Van Gogh) APU。它在台积电7纳米工艺上集成了四个Zen 2 CPU核心和一个RDNA 2 GPU。

**CPU:** 虽然基于Zen 2架构，但CPU性能受到LPDDR5内存延迟的影响。CPU采用单CCX设计，具有4MB的三级缓存，但在Linux系统中，三级缓存的性能不稳定。LPDDR5的带宽尽管额定速度为5500 MT/s，但实际表现令人惊讶地低，阻碍了CPU性能。此外，CPU的时钟频率提升速度较慢，影响响应速度。

**GPU:** 基于RDNA 2架构的GPU，被称为“AMD Custom GPU 0405”，具有512个FP32通道，运行频率高达1.6 GHz。它缺少OpenCL支持，导致测试难度增加。GPU采用RDNA风格的缓存设置，具有16KB的L1向量/标量缓存和128KB的L1缓存，并由1MB的L2缓存支持。尽管GPU的内存延迟仍然受到LPDDR5问题的影响，但带宽明显更好，为Steam Deck带来了强大的图形性能。与Renoir的iGPU相比，“梵高”展现出改进的内存访问延迟。“梵高”使用了巨大的内存带宽，而不是更大的缓存，并且具有与游戏机相当的计算与带宽比率。

**总体而言:** “梵高”优先考虑GPU的性能以用于游戏，更高的带宽分配证明了这一点。CPU在一定程度上受到内存限制，导致响应速度降低。尽管存在限制，该APU的设计有效地平衡了CPU和GPU在有限功率预算内的性能。

---

## 45. 图Transformer的时间序列预测

**原文标题**: Time Series Forecasting with Graph Transformers

**原文链接**: [https://kumo.ai/research/time-series-forecasting/](https://kumo.ai/research/time-series-forecasting/)

基于图结构数据的时序预测：利用图变换器进行端到端预测

---

## 46. Bzip2 包已从 C 语言切换为 100% Rust

**原文标题**: Bzip2 crate switches from C to 100% Rust

**原文链接**: [https://trifectatech.org/blog/bzip2-crate-switches-from-c-to-rust/](https://trifectatech.org/blog/bzip2-crate-switches-from-c-to-rust/)

bzip2 crate 已更新至 0.6.0 版本，默认情况下从 C 实现切换为 100% Rust 实现 libbz2-rs-sys。此更改提高了性能、简化了交叉编译并改善了可维护性。

Rust 实现通常在压缩和解压缩基准测试中都优于 C 版本，并观察到显著的加速。一个例外是在 macOS 上进行解压缩时，偶尔会观察到性能差异。

切换到 Rust 简化了交叉编译，特别是对于像 webassembly、Windows 和 Android 这样的平台，这些平台以前由于 C 依赖项而面临挑战。Rust 实现还通过默认不导出符号来避免符号冲突。

Rust 实现已经过安全审计，其中发现了一个逻辑错误并改进了模糊测试器。代码也可以通过 MIRI 验证。

此次更新的动机是各种协议和库对 bzip2 支持的持续需求。作者借鉴了 zlib-rs 的经验来现代化 bzip2 crate。

---

## 47. Timescale 更名 TigerData

**原文标题**: Timescale Is Now TigerData

**原文链接**: [https://www.tigerdata.com/blog/timescale-becomes-tigerdata](https://www.tigerdata.com/blog/timescale-becomes-tigerdata)

文章：《速度与质量并存：为分析和代理时代构建现代 PostgreSQL》，宣布 Timescale 更名为 TigerData。该文章分类于“所有文章”、“公告与发布”以及其他类别，包括人工智能、分析、PostgreSQL 和时序数据。

重点是 Timescale 更名为 TigerData。文章暗示将继续专注于增强 PostgreSQL 在分析和“代理”用例中的应用，表明在不影响功能的前提下，提高了速度和性能。标题暗示构建现代 PostgreSQL 解决方案，针对人工智能、分析以及其他新兴技术的需求进行了优化。

该文章由 Ajay Kulkarni 和 Mike Freedman 于 2025 年 6 月 17 日发表。 “基准测试与比较”、“PostgreSQL 性能”和“PostgreSQL 技巧”等类别的存在表明，TigerData 可能会继续提供与优化 PostgreSQL 性能和为用户提供实用建议相关的内容。

---

## 48. 迪内什的仲夏死亡谷徒步 (1998)

**原文标题**: Dinesh’s Mid-Summer Death Valley Walk (1998)

**原文链接**: [https://dineshdesai.info/dv/photos.html](https://dineshdesai.info/dv/photos.html)

1998年7月，迪内什开始了穿越死亡谷国家公园的挑战性旅程，以体验极端高温对人体的影响。他的目标是从北到南徒步走完整个公园，大约180英里。这项雄心勃勃的计划包括在12天内每天行走15英里。这段文字作为相册的介绍，表明这次冒险用照片记录了下来。其中一张照片的说明描述了迪内什的准备工作，突出了他的着装，包括输水管、羊毛裤、羊毛衬衫和保暖内衣。广播节目《汽车闲话》对这张照片进行了幽默评论，为这项潜在的危险行动增添了轻松的元素。本文由《汽车闲话》友情提供，并受版权保护。文章的主要重点是迪内什的极限行走以及试图了解在沙漠高温中的耐力。

---

## 49. 我为什么不用人工智能

**原文标题**: Why I Won't Use AI

**原文链接**: [https://agentultra.com/blog/why-i-wont-use-ai/index.html](https://agentultra.com/blog/why-i-wont-use-ai/index.html)

在2025年的一篇文章中，作者解释了其拒绝在编程中使用人工智能的原因，认为它会损害劳动者利益、缺乏已被证实的生产力提升、削减编程乐趣、依赖于伦理上可疑的数据，并且对环境产生不利影响。

作者认为自己是一名劳动者，其价值正被人工智能抽取，这呼应了卢德运动对技术取代工人且缺乏充分社会保障的担忧。尽管承认人工智能工具的便利性，但作者强调，产量增加并不等同于更好的代码。对开发者生产力的实证研究尚无定论，表明人工智能工具可能会增加错误率，使得现行的代码审查实践变得不足。

作者认为，编程的乐趣来自于应对挑战并通过实践改进代码。相反，人工智能使这个过程变得不那么吸引人。

在伦理方面，作者批评人工智能依赖于从互联网上抓取的数据，而不考虑知识产权或给个人服务器带来的压力。此外，人工智能模型能源密集型的训练和推理正在加剧环境压力，特别是通过增加对化石燃料和淡水的需求，而这些需求已经在压力重重的地区。

在财务方面，作者指出，许多人工智能工具并不盈利，需要政府补贴。他们对未来改进的承诺表示怀疑，认为人工智能的进步正在放缓，并且可能由于物理限制和理解这些模型如何工作的内在挑战而达到了极限。

最终，作者提倡使用能够帮助程序员思考和验证代码的工具，而不是简单地生成更多代码。他们呼吁保护人类劳动，并更好地监管人工智能技术，以确保它服务于社会，而不仅仅是资本。

---

## 50. 从SDR到“伪HDR”：Switch 2上的马力欧卡丁车世界

**原文标题**: From SDR to 'Fake HDR': Mario Kart World on Switch 2

**原文链接**: [https://www.alexandermejia.com/from-sdr-to-fake-hdr-mario-kart-world-on-switch-2-undermines-modern-display-potential/](https://www.alexandermejia.com/from-sdr-to-fake-hdr-mario-kart-world-on-switch-2-undermines-modern-display-potential/)

本文批评任天堂Switch 2上的《马力欧卡丁车世界》，认为其HDR实现是“假HDR”，因为它采用的是SDR优先的制作流程和后期色调映射的权宜之计。作者作为杜比视界专家，认为该游戏的色域被限制在SDR，其动态范围也未超过SDR。通过使用专业级采集和分析工具进行的调查显示，无论主机亮度设置如何，该游戏都采用静态色调映射，并将亮度限制在1,000尼特。

作者认为这款游戏最初是为SDR设计的，HDR效果只是通过将SDR图像拉伸到HDR来实现的，这种技术无法充分利用HDR显示器的潜力。他发现天空中有条带现象，并且色彩空间利用率有限。他将该游戏的视觉效果与其他以HDR为主导制作的游戏进行了对比，发现前者逊色不少。

文章将此问题归因于行业持续依赖SDR优先的流程，即艺术审查和光照最初是在SDR中开发的，导致HDR的实现仓促且妥协。作者建议开发者致力于升级其用于广色域(WCG)的流程，允许动态范围，调整VFX，并构建动态色调映射服务以获得最佳的HDR结果。在一个HDR为主流，消费者重视图像质量的世界里，作者强调从开发一开始就认真对待HDR的重要性。

---

## 51. 展示一下：我做了一个在线Unicode楔形文字数字时钟

**原文标题**: Show HN: I made an online Unicode Cuneiform digital clock

**原文链接**: [https://oisinmoran.com/sumertime](https://oisinmoran.com/sumertime)

奥伊辛·莫兰用Unicode楔形文字创建了一个在线数字时钟。这个名为“苏美尔时钟”的项目在Show HN上展示，并且可能可以通过提供的链接访问（虽然内容中没有明确给出，但有暗示）。其核心概念是通过古代文字系统可视化时间，融合了历史和技术美学。该摘要强调了该项目的新颖性，即使用楔形文字以现代数字格式表示时间。

---

## 52. AMD Zen架构前互连：Trinity北桥测试

**原文标题**: AMD's Pre-Zen Interconnect: Testing Trinity's Northbridge

**原文链接**: [https://chipsandcheese.com/p/amds-pre-zen-interconnect-testing](https://chipsandcheese.com/p/amds-pre-zen-interconnect-testing)

本文深入探讨了AMD 2012年“Trinity”APU（加速处理器）的互连架构，这是一款前Zen时代的芯片，它结合了CPU核心和集成GPU（iGPU）。与AMD现代的Infinity Fabric不同，Trinity依赖于基于北桥的互连，让人想起Athlon 64时代，但进行了调整以适应iGPU。

北桥以1.8 GHz的频率运行，采用两级交叉开关（XBAR）系统，用于在CPU核心、IO和内存之间路由请求。一个关键方面是CPU和GPU内存访问的分离。iGPU使用“Garlic”链路（Radeon Memory Bus）直接访问DRAM，绕过CPU的内存控制器（MCT）和缓存一致性机制，从而为图形密集型任务提供高带宽。这避免了不必要的缓存窥探，因为CPU和GPU通常不共享数据。

对于需要CPU和GPU数据共享的场景，Trinity采用“Onion”链路，该链路通过XBAR和MCT路由GPU请求，允许通过CPU缓存探测实现缓存一致性。然而，这条路径明显慢于“Garlic”链路。将GPU内存映射到CPU地址空间可以通过“Garlic”实现高带宽，但迫使CPU将内存视为不可缓存，导致性能下降。

文章总结说，虽然Trinity的互连是一种折衷方案，但它使iGPU能够在图形工作负载中获得不错的性能，尤其得益于高带宽的“Garlic”链路。然而，缺乏统一的、一致的内存访问路径（如在后来的AMD架构（如Infinity Fabric）中看到的那样）限制了其在CPU和GPU之间进行零拷贝数据共享的潜力。虽然当时英特尔的iGPU实现具有更好的内存一致性，但Trinity的设置并没有在GPU消耗大量带宽时严重影响CPU延迟。

---

## 53. 我们是否应该为不稳定的网络环境进行设计？

**原文标题**: Should we design for iffy internet?

**原文链接**: [https://bytes.zone/posts/should-we-design-for-iffy-internet/](https://bytes.zone/posts/should-we-design-for-iffy-internet/)

布莱恩·希克斯的文章《我们是否应该为不稳定的网络进行设计？》探讨了2025年美国互联网接入的现实情况，认为Web开发者不应假定普遍存在快速互联网连接。他使用来自FCC和NCES的数据来说明问题的范围。

希克斯将“稳定、可靠的互联网”定义为至少具有25Mbps下载速度和3Mbps上传速度的地面链路。他分析了FCC宽带地图，显示虽然互联网覆盖在城市地区普遍良好，但在农村地区显著下降，尤其是在考虑更快连接速度（250/25 Mbps）时。

他还研究了教育部关于学生互联网接入的数据，揭示了虽然接入情况有所改善，但仍有大量学生（2021年为297万）仅依赖智能手机或根本无法访问互联网，而低收入家庭受到的影响尤为严重。

希克斯的核心观点是，虽然大约97%的美国家庭可以使用某种互联网接入，但开发者不应假定速度超过25Mbps下载和3Mbps上传，并且应该预见到更高的延迟。他敦促开发者考虑具有慢速连接（如飞机WiFi或卫星）以及使用移动/按流量计费网络用户的体验。虽然没有做出道德判断，但他认为忽视这些限制可能会对用户和企业产生负面影响。他总结说，虽然以美国为中心且未考虑数据中心延迟，但不稳定网络的问题是真实存在的，应该在软件设计中加以考虑。

---

## 54. Claude Code的魔力在于其迭代性。

**原文标题**: Claude Code feels like magic because it is iterative

**原文链接**: [https://omarabid.com/claude-magic](https://omarabid.com/claude-magic)

文章认为，Claude Code以及通用AI工具所带来的所谓“魔法”，源于其迭代的本质，而非LLM智能的必然提升。文章引用了史蒂夫·乔布斯关于快速指令执行使流程感觉神奇的说法作为类比。作者解释说，在这种情况下，智能可以被视为启发式方法和尝试次数的产物。LLM提供启发式方法，而像Claude Code这样的工具通过自动化和加速这些尝试来提升智能。

作者最初不以为然，认为与LLM的手动来回聊天界面就足够了。然而，他们现在看到了它所提供的速度和自主性的价值。一个关键的例子是更新带有编译和测试的项目依赖项，Claude Code自主迭代了数十次，几乎不需要人工干预。

作者强调了通过大规模并行计算进一步加速的潜力，暗示目前需要40分钟的任务有可能缩短到几分钟。这引发了一个问题，即开发人员是否会再回到对可以自动化的任务进行手动处理。文章最后强调了即使在当前LLM性能下，AI工具也有潜力自动化其他任务，并提示读者订阅新闻通讯以获取更多更新。

---

## 55. 穿梭跑的魔力

**原文标题**: The magic of through running

**原文链接**: [https://www.worksinprogress.news/p/the-magic-of-through-running](https://www.worksinprogress.news/p/the-magic-of-through-running)

本文探讨了“贯通运营”的概念，作为改善城市交通系统的解决方案，尤其是在拥有广泛维多利亚时代铁路网络的城市中。文章强调，许多老城市都拥有郊区铁路线，这些线路在市中心边缘终止，造成效率低下并限制了运力。

文章认为，“贯通运营”，即将这些郊区线路通过隧道连接起来，让火车穿过市中心，可以将这些遗留系统转变为现代地铁式网络。这种方法具有多项优势：它允许乘客无需换乘即可直接到达市中心，通过消除中央终点站的瓶颈来提高整体网络容量，并且由于大部分基础设施已经存在，因此比建造全新的地铁系统便宜得多。

文章以慕尼黑和伦敦作为案例研究。慕尼黑被视为一个成功的例子，因为它使用贯通运营来创建一个高效的交通网络。伦敦凭借其庞大的维多利亚时代铁路网络，例证了贯通运营解决复杂交通挑战的潜力。慕尼黑城市快铁通过隧道连接了现有支线，使通勤者可以直接进入市中心。伦敦的老旧网络比现代地铁大得多。

核心论点是，对于拥有遗留铁路网络的城市来说，贯通运营提供了一种经济高效的方式来现代化其交通系统，释放现有基础设施的潜力，从而打造世界领先的公共交通。

---

## 56. KiCad与Wayland支持

**原文标题**: KiCad and Wayland Support

**原文链接**: [https://www.kicad.org/blog/2025/06/KiCad-and-Wayland-Support/](https://www.kicad.org/blog/2025/06/KiCad-and-Wayland-Support/)

KiCad 在 Wayland 系统上的运行存在显著局限性，影响用户体验。KiCad 开发团队强调，Wayland 的设计以及不同合成器之间实现的不一致性导致了许多他们无法控制的问题。

主要问题包括窗口管理（窗口位置、停靠面板定位、多窗口协调、拖动限制）、输入/交互（光标扭曲、焦点管理、输入设备处理）以及性能/稳定性（OpenGL 节流、高 CPU/GPU 使用率、图形故障、崩溃、剪贴板问题）。这些问题的出现是因为 Wayland 缺少 X11、Windows 和 macOS 所依赖的基本功能。

KiCad 团队优先考虑惠及所有用户的功能，并避免针对特定窗口管理器进行修复。因此，他们不会调查或支持与 Wayland 相关问题的错误报告。

对于专业用途，KiCad 强烈建议使用基于 X11 的桌面环境，如 XFCE、KDE Plasma 或 MATE，以及与 X11 兼容的显示管理器。虽然 KiCad 可以在 Wayland 上运行以供休闲使用，但用户应该预料到局限性和潜在的挫败感。

KiCad 持续关注 Wayland 的发展，并欢迎对上游项目（包括 wxWidgets）做出贡献，以提高 Wayland 的兼容性。团队专注于核心功能，并鼓励用户在 Wayland 成熟之前使用 X11 以获得可靠的体验。

---

## 57. 今天的汉堡菜单图标：它还容易识别吗？

**原文标题**: The hamburger-menu icon today: Is it recognizable?

**原文链接**: [https://www.nngroup.com/articles/hamburger-menu-icon-recognizability/](https://www.nngroup.com/articles/hamburger-menu-icon-recognizability/)

本文重新审视了关于汉堡菜单图标的争议，探讨了其在2025年的可识别性与早期相比的差异。 汉堡菜单最初因隐藏导航而阻碍可用性，导致参与度、任务成功率和满意度下降而备受批评，但由于移动优先设计的普及以及大型科技公司的采用，它已成为一种常见的模式。

研究表明，用户通常将该图标识别为隐藏菜单，尤其是在顶部左侧以标准样式放置时。 然而，熟悉并不保证万无一失的可用性，特别是对于不太懂技术的用户或在不熟悉的布局中。 本文警告了视觉干扰，即类似的基于线条的图标由于其结构和位置而被误解为汉堡菜单。

本文重申了汉堡菜单设计的最佳实践：在左上角使用标准的3线图标，避免额外的样式，标记为“菜单”，使用微妙的动画，并提供足够的视觉填充和对比度。 至关重要的是，它强调隐藏导航仍然会增加交互成本，并鼓励使用其他导航方法和清晰的搜索功能。

结论是，汉堡菜单是可行的，但并非普遍理想。 应该深思熟虑地使用它们，尤其是在空间受限的屏幕上，并仔细考虑其权衡取舍并与用户进行彻底的测试。 除非绝对必要，否则应避免隐藏导航。

---

## 58. 城市中心的陌生人：洛杉矶医疗中心的无名氏们

**原文标题**: Strangers in the Middle of a City: The John and Jane Does of L.A. Medical Center

**原文链接**: [https://www.latimes.com/science/story/2025-06-15/l-a-seeks-help-for-a-patient-with-no-name](https://www.latimes.com/science/story/2025-06-15/l-a-seeks-help-for-a-patient-with-no-name)

柯琳·珀蒂尔的文章《城市中的陌生人》着重介绍了洛杉矶总医院身份不明患者（无名氏）的困境。每年，有数千人因昏迷、丧失能力或疾病而无法识别身份进入急诊室。虽然大多数人在48小时内被确认身份，但仍有几十人保持匿名，成为长期住院者。

医院工作人员，包括社工，竭尽全力识别这些患者，通过体貌特征、发现地点以及通过新闻稿发布照片进行公开呼吁。识别这些患者不仅对于行政和安全原因（过敏、药物）至关重要，而且对于将他们转移到合适的护理机构也至关重要。由于没有身份证明或保险，技术熟练的护理机构拒绝接收，导致患者滞留在洛杉矶总医院，这是一个忙碌的创伤中心，不适合长期护理。

文章强调了有关患者隐私的法律限制，这限制了可以公开分享的信息。虽然大约一半的公众呼吁能够帮助确认身份，但剩下的患者面临着不确定的未来，可能会在医院度过几个月甚至几年。这个故事强调了医疗保健、身份以及弱势群体在大型城市环境中面临的挑战的复杂性。文章最后呼吁公众协助识别这些迷失的人。

---

## 59. Incant – 为你的代码添加魔法咒语

**原文标题**: Incant – add magic spells to your code

**原文链接**: [https://github.com/montyanderson/incant](https://github.com/montyanderson/incant)

Incant是一款旨在将语言模型调用安全地集成到代码中的工具，它使用基本组件与上游推理提供商交互。它允许开发者利用语言模型的强大功能，而不会暴露敏感数据，因为所有输入数据都会发送给这些提供商。

Incant通过访问诸如`OPENAI_API_KEY`之类的环境变量工作，使其易于配置。它提供两个核心功能：`createSelector`和`createFilter`。

`createSelector`能够创建根据定义的标准从给定输入数组中选择特定元素的函数。主要优点是保证输出是输入值之一，从而防止幻觉并确保类型安全。一个例子展示了如何使用`createSelector`从数组中选择最大的数字。

`createFilter`允许开发者构建根据特定标准过滤元素列表的函数。与`createSelector`类似，输出保证是输入数组的子集，保持原始顺序并防止幻觉。该示例演示了过滤名称列表以仅返回男性名称。

本质上，Incant提供了一种安全可靠的方式来利用语言模型执行诸如选择特定元素或过滤列表之类的任务，同时确保输出保持在输入数据的范围内并避免潜在的幻觉。

---

## 60. 美国路灯变紫

**原文标题**: US Streetlights Are Turning Purple

**原文链接**: [https://www.scientificamerican.com/article/streetlights-are-mysteriously-turning-purple-heres-why/](https://www.scientificamerican.com/article/streetlights-are-mysteriously-turning-purple-heres-why/)

以下是关于文章《美国路灯变紫》的简要总结：

自2021年初以来，美国（及全球）各地的路灯神秘地变成了紫色，这是一种现象。发生这种情况的原因是，大约15年前，城市用LED灯取代了旧的钠灯，而现在LED灯正在失效。

白色LED路灯通常使用涂有荧光物质的蓝色LED，该荧光物质会发出红色和黄色光，从而产生白光外观。紫色色调表明荧光粉涂层正在剥落，暴露了底层的蓝色LED光。这种剥离可能是由热量积聚、振动甚至重力引起的。

紫色光可能是一种安全隐患，因为它会影响司机和行人感知周围环境的方式。虽然蓝色光可能在昏暗光线条件下改善周边视觉，但由于眼睛中对蓝色敏感的锥状感光细胞数量有限，它也可能降低看清中心视觉细节的能力。无法看到所有颜色范围也可能是一个问题。

专家建议晚上避免佩戴太阳镜或滤蓝光眼镜，以最大限度地利用可用光线。虽然紫色路灯令人担忧，但这并不意味着所有LED灯都不好。这可能是制造问题或某些特定LED的问题。

---

## 61. 伊朗呼吁民众从设备上删除WhatsApp。

**原文标题**: Iran asks its people to delete WhatsApp from their devices

**原文链接**: [https://apnews.com/article/iran-whatsapp-meta-israel-d9e6fe43280123c9963802e6f10ac8d1](https://apnews.com/article/iran-whatsapp-meta-israel-d9e6fe43280123c9963802e6f10ac8d1)

无法访问文章链接。

---

## 62. 皮肤细胞直接转化为神经元用于细胞治疗

**原文标题**: Skin cells turned directly into neurons for cell therapy

**原文链接**: [https://news.mit.edu/2025/mit-engineers-turn-skin-cells-into-neurons-for-cell-therapy-0313](https://news.mit.edu/2025/mit-engineers-turn-skin-cells-into-neurons-for-cell-therapy-0313)

麻省理工研究人员开发出一种简便高效的方法，可将皮肤细胞直接转化为运动神经元，绕过了传统的干细胞中间阶段。这种新方法目前对小鼠细胞效果更好，它只需使用三种转录因子（NGN2、ISL1和LHX3），通过单个改造病毒传递，以及两种促进细胞快速分裂的基因。与之前的直接转化方法相比，这导致神经元的产量显著提高（超过1000%）。

研究人员已成功将这些实验室培养的运动神经元移植到小鼠大脑中，它们与现有的大脑组织融合，表现出可测量的电活动和通讯潜力。他们还实现了人类皮肤细胞向神经元的直接转化，尽管效率较低（10-30%）。

这种改进的效率和简化的方法可以通过实现大量运动神经元的生产，显著推进脊髓损伤和肌萎缩侧索硬化症等疾病的细胞替代疗法。该团队目前正致力于提高人类细胞转化的效率，并探索将这些神经元植入脊髓的可能性。

---

## 63. 五分钟内讲述“不要嘲笑你所不拥有的”（2022）

**原文标题**: “Don’t mock what you don't own” in 5 minutes (2022)

**原文链接**: [https://hynek.me/articles/what-to-mock-in-5-mins/](https://hynek.me/articles/what-to-mock-in-5-mins/)

本文提倡“不要 Mock 你不拥有的东西”的测试原则，即只 Mock 你控制的对象，而不是第三方依赖。作者认为直接 Mock 第三方 API（例如 HTTP 客户端）会导致测试脆弱、复杂，并与 API 的实现细节绑定，从而使业务逻辑更难辨认，且容易因 API 更改而中断。

文章使用 Docker 仓库客户端示例来说明该问题。直接 Mock `httpx` 库的 `get()` 方法需要多层 Mock 才能模拟 HTTP 响应，模糊了测试意图并产生了样板代码。

解决方案是在第三方依赖项周围引入一个薄的抽象层（一个外观模式）。在示例中，创建了一个 `DockerRegistryClient` 类，封装了 `httpx` 调用。这允许 Mock `DockerRegistryClient` 的方法（`get_repos`，`get_repo_tags`），而不是底层的 HTTP 客户端，从而产生更简单、更集中的测试，并且对 HTTP 库的更改不太敏感。这通常也会带来更符合语言习惯和更简洁的业务逻辑。

虽然该原则很有价值，但它不是一个硬性规则。作者建议在第三方 API 已经定义良好、模拟特定错误（网络问题、超时）或对于简单的程序，测试助手就足够的情况下打破它。要点是将该原则用作启发式方法，以指导测试策略朝着更可维护和可理解的测试方向发展。

---

## 64. JPEG XL与谷歌的战争 (2024)

**原文标题**: JPEG XL and Google's War Against It (2024)

**原文链接**: [https://vale.rocks/posts/jpeg-xl-and-googles-war-against-it](https://vale.rocks/posts/jpeg-xl-and-googles-war-against-it)

本文认为，谷歌为了推广其WebP格式并保持对网络标准的控制，正在扼杀更优秀的图像格式JPEG XL的普及。文章首先简要回顾了GIF、JPEG和PNG等图像格式的历史，强调了它们在现代网络中的局限性。然后介绍了WebP和AVIF，指出谷歌迅速推动了WebP的普及并增加了对AVIF的支持。

作者强调了JPEG XL的优势，声称其在无损/有损压缩、更小的文件大小、更好的色域和速度等方面超越了所有其他栅格图像格式。尽管JPEG XL具有明显的优势，但由于谷歌的阻挠，它缺乏广泛的浏览器支持。

文章指责谷歌利用其在搜索和浏览器技术（Chromium）中的主导地位来阻碍JPEG XL的普及。文章指出，尽管最初实施并引起了用户兴趣，谷歌还是从Chromium中移除了对JPEG XL的支持，这是反竞争行为的证据。谷歌的理由是缺乏生态系统兴趣和增量收益不足，但作者对此进行了反驳。他们认为，谷歌担心JPEG XL的优越性会使WebP过时，从而削弱谷歌的控制力。

作者敦促读者提高意识，使用支持的浏览器/标志，推广该格式，并与垄断行为作斗争，以确保创新不会因公司控制而被扼杀。文章总结说，JPEG XL应该有机会参与竞争，而谷歌的行为不利于进步。

---

## 65. AMD CDNA 4 架构发布

**原文标题**: AMD's CDNA 4 Architecture Announcement

**原文链接**: [https://chipsandcheese.com/p/amds-cdna-4-architecture-announcement](https://chipsandcheese.com/p/amds-cdna-4-architecture-announcement)

AMD CDNA 4架构发布：专注于矩阵运算性能提升

关键特性包括：

*   **系统架构：** 沿用CDNA 3的chiplet设计，采用与AMD CPU相似的方式，通过Infinity Fabric将四个基础die上的八个XCD（加速计算die）连接起来。
*   **MI355X：** 每个XCD的CU数量略少于MI300X，但通过更高的时钟速度进行弥补。它仍然比英伟达的B200更大，拥有更多的基本构建块。
*   **计算单元变更：** 重新平衡执行单元，以提高矩阵乘法吞吐量，特别是在较低精度的数据类型上，在FP6吞吐量方面与英伟达的B200 SM相匹配。由于更高的核心数量和时钟速度，AMD在向量运算和更高精度的数据类型方面保持领先优势。
*   **更大的LDS：** 将LDS（本地数据共享）容量增加到160 KB，读取带宽翻倍，允许软件将更多数据保持在靠近执行单元的位置。新的指令改进了数据移动到LDS的过程，包括转置操作。
*   **系统架构增强：** L2缓存现在可以写回脏数据并保留该行的副本，DRAM子系统升级到HBM3E，提供更高的带宽（8 TB/s）和容量（288 GB），超过了英伟达的B200。
*   **总体策略：** AMD正在调整CDNA 3的架构，而不是进行大刀阔斧的改变，类似于英伟达对Blackwell的处理方式，利用其在超级计算领域的现有成功。

---

## 66. 富士X半格：是完美的家庭相机吗？

**原文标题**: Fujifilm X half: Is it the perfect family camera?

**原文链接**: [https://arslan.io/2025/06/14/fujifilm-x-half-is-it-the-perfect-family-camera/](https://arslan.io/2025/06/14/fujifilm-x-half-is-it-the-perfect-family-camera/)

本文探讨了作者使用富士X半格相机的体验，尤其是在家庭使用场景下，并将其与作者使用徕卡M11和各种富士X型号相机的专业经验进行了对比。

起初，作者对X半格相机的功能与其价格相比持怀疑态度，但在发布后还是购买了一台，认为它能够满足特定的需求。由于M11的复杂性不适合作者的家人，特别是孩子们，因此作者开始寻找一款对儿童友好的数码相机，要求易于使用、维护，并且最好带有取景器。最初尝试在亚马逊上购买廉价的无牌相机，但由于功能差、电池问题和糟糕的图像质量而宣告失败。

X半格相机成为了一个解决方案，不仅对作者而言，而且对整个家庭而言。其轻巧的重量、简单的自动模式、垂直纵横比和USB-C充电都是巨大的优势。胶片模式也让他的孩子们了解了每张照片的局限性和价值。缺点包括Wi-Fi连接不稳定、图像质量一般（尽管孩子们并不在意）、运行缓慢以及花哨的胶片拨杆。快门按钮的反馈也不令人满意。

尽管存在缺陷且价格相对较高（在作者居住的土耳其约为700美元，但在其他地方可能高达850美元），作者仍然认为X半格相机作为一款适合家庭和儿童使用的用户友好型相机表现出色。它突出了富士相机直接输出的JPEG质量，这一点非常重要，因为他的家人不会使用RAW格式。作者总结说，X半格相机不应被视为专业摄影师的高性能相机，而应被视为一种有趣、简单且怀旧的设备，非常适合捕捉家庭瞬间，前提是你能接受它的价格。

---

## 67. 航海家：在您的手机上实时绘制城市规模的3D高斯点云

**原文标题**: Voyager: Real-Time Splatting City-Scale 3D Gaussians on Your Phone

**原文链接**: [https://arxiv.org/abs/2506.02774](https://arxiv.org/abs/2506.02774)

本文题为“Voyager: 在手机上实时渲染城市级规模的3D高斯”，旨在解决在资源有限的移动设备上渲染大规模3D高斯溅射(3DGS)场景的挑战。作者指出，虽然基于云的渲染是一种潜在的解决方案，但由于需要流式传输渲染帧，它会引入显著的延迟和带宽问题。

该论文提出了一种新颖的方法，即仅将必要的Gaussians流式传输到客户端，这是基于在正常用户运动期间每秒新出现的Gaussians数量保持相对恒定的观察。该系统利用云端的异步细节层次搜索来识别和传输这些必要的Gaussians。在客户端，渲染使用基于查找表的栅格化技术进行加速。

最终的系统能够在移动设备上实现低延迟、城市级规模的3DGS渲染。作者报告说，与现有解决方案相比，该系统取得了显著的改进，在保持可比的渲染质量的同时，数据传输减少了100倍以上，渲染速度提高了8.9倍。该论文于2025年6月3日提交，并于2025年6月4日进行了修订。

---

## 68. 尝试制作最小的*电动机 [视频]

**原文标题**: Attempting to Make the Smallest* Electric Motor [video]

**原文链接**: [https://www.youtube.com/watch?v=6x_NMytSA90](https://www.youtube.com/watch?v=6x_NMytSA90)

这个名为“尝试制作最小*电动机”的YouTube视频，很可能记录了一项关于制造微型电动机的实验或项目。然而，所提供的内容片段实际上并未描述电动机本身、其构造或尝试的结果。相反，它完全由标准的YouTube页脚信息组成，包括版权声明、联系方式、广告和开发者资源、服务条款、隐私和安全政策、关于YouTube如何运作的信息、测试中的功能以及与NFL Sunday Ticket相关的信息。

因此，仅根据提供的文本，我们只能说该视频托管在YouTube上，并受其政策约束。我们没有任何关于实际尝试制造小型电动机的细节。要了解视频的内容，需要实际观看它。

---

## 69. Show HN: WFGY – 无需重新训练即可修复LLM逻辑的推理引擎

**原文标题**: Show HN: WFGY – A reasoning engine that repairs LLM logic without retraining

**原文链接**: [https://github.com/onestardao/WFGY](https://github.com/onestardao/WFGY)

“Show HN”：WFGY（万法归一）——一种无需重新训练即可提升LLM逻辑并减少幻觉的推理引擎。它提供了一个关于如何使用WFGY的教程，包括下载PDF，将其输入LLM，并提示LLM“使用WFGY回答 + 你的问题”。文章还提及了功能更强大的SDK版本。

WFGY的核心是一个旨在与LLM配合使用的提示，它解锁了诸如语义残差分析、渐进公式应用、逆向重构和注意力调节等功能。该框架分为六个阶段：信任、扩展、荒诞、应用、前沿和行动，每个阶段都包含各类问题，旨在测试和利用WFGY在各种场景下的能力，从基本理解到哲学探究，甚至迷因生成。

“大爆炸提示”贯穿各个阶段，它模拟一个专家小组通过WFGY框架分析情况。这种方法强调分析潜在的上下文、潜台词和非常规应用的潜力。该文档旨在展示WFGY增强LLM推理能力、提供更深刻见解，并通过鼓励AI考虑多个角度并以更全面的方式分析信息，从而潜在地解锁新的创造性可能性的能力。作者希望在2025年8月1日前获得1万个stars，以解锁WFGY 2.0。

---

## 70. 苹果全新语音API在快速转录方面超越 Whisper

**原文标题**: Apple's New Speech APIs Outpace Whisper for Fast Transcription

**原文链接**: [https://www.macstories.net/stories/hands-on-how-apples-new-speech-apis-outpace-whisper-for-lightning-fast-transcription/](https://www.macstories.net/stories/hands-on-how-apples-new-speech-apis-outpace-whisper-for-lightning-fast-transcription/)

本文重点介绍与苹果技术相关的两个独立主题：

1. **苹果全新语音API：** 标题表明苹果发布了全新的语音API，与已有的Whisper模型相比，该API提供更快的转录速度。 这意味着苹果的语音识别技术取得了进步，可能会影响依赖转录服务的开发者和用户。 本文可能详细介绍了这些新API的性能改进、准确性和功能。

2. **克雷格·费德里吉访谈：** 文章的第二部分重点介绍了对苹果软件工程高级副总裁克雷格·费德里吉的采访。 采访深入探讨了iPadOS，探索了其发展历程，特别是关于多任务处理能力。讨论可能还涵盖了iPad作为产品的基本本质及其在苹果整体生态系统中的作用。 预计会深入了解苹果对iPad未来的愿景以及其设计和功能选择背后的基本原理。

---

## 71. 天文学家捕捉到星系最详细的千色图像

**原文标题**: Astronomers capture most detailed thousand-colour image of a galaxy

**原文链接**: [https://www.eso.org/public/news/eso2510/](https://www.eso.org/public/news/eso2510/)

天文学家利用欧洲南方天文台的甚大望远镜（VLT）制作了一张极为详细、千色呈现的玉夫座星系（NGC 253）图像。这张前所未有的图像揭示了以前未见的特征，并为全面研究星系的组成部分：恒星、气体和尘埃提供了可能。

通过利用VLT上的多单元光谱探测器（MUSE）观测该星系超过50小时，研究人员捕获了大量数据，使他们能够绘制这些组成部分的年龄、成分和运动图。这张详细的图谱使科学家能够放大到单个恒星尺度的恒星形成区域，并缩小以研究整个星系。

对数据的初步分析揭示了玉夫座星系中约500个行星状星云，远多于通常在银河系近邻之外的星系中探测到的数量。这些星云可作为距离标记，从而更准确地确定星系的距离（1100万光年）。

未来的研究将利用该图谱来研究整个星系中的气体流动、成分变化和恒星形成过程。该研究旨在了解小尺度过程如何影响跨越数十万光年的星系的整体演化。该研究发表在《天文与天体物理学》杂志上，已被接受发表。

---

## 72. Show HN: MediaCMS v6 – 开源视频平台，带裁剪器和RBAC

**原文标题**: Show HN: MediaCMS v6 – open-source video platform with trimmer and RBAC

**原文链接**: [https://github.com/mediacms-io/mediacms](https://github.com/mediacms-io/mediacms)

MediaCMS v6 是一款开源、功能丰富的视频和媒体内容管理系统，采用 Django 和 React 构建。 它允许用户创建和管理自己的视频平台，并完全掌控他们的数据。 主要功能包括：支持多种媒体类型和分类、社交分享、视频剪辑器、基于角色的访问控制 (RBAC)、SAML 支持、实时搜索、播放列表、具有浅色和深色主题的响应式设计、高级用户管理、可配置的操作、定制视频播放器、多种转码配置文件、自适应视频流、字幕支持、可扩展的转码、分块文件上传、REST API 和多语言翻译。

示例用例包括学校和组织处理敏感内容。 MediaCMS 旨在提供全面的功能、简易的安装和维护以及简单的定制。 它采用 GNU AGPL v3.0 许可。

该平台通过 Elestio 提供商业支持和托管。 硬件建议表明，中小规模安装至少需要 4GB 内存/2-4 个 CPU。 可以通过 Docker Compose 或单服务器自动化脚本进行部署。

该软件利用 Python、Django、React、PostgreSQL 和 FFMPEG 等技术。 值得注意的用户包括 Cinemata、Critical Commons 和美国妇科腹腔镜医师协会。 欢迎通过各种方式做出贡献，包括聘请开发人员、撰写关于该项目的文章、在社交媒体上分享、报告错误、提出建议和贡献代码。

---

## 73. 谦卑的程序员 (1972)

**原文标题**: The Humble Programmer (1972)

**原文链接**: [https://www.cs.utexas.edu/~EWD/transcriptions/EWD03xx/EWD340.html](https://www.cs.utexas.edu/~EWD/transcriptions/EWD03xx/EWD340.html)

在《谦卑的程序员》一文中，艾兹格·W·戴克斯特拉反思了编程行业从初期阶段到20世纪60年代中期“软件危机”的演变。他回顾了自己的亲身经历，强调了早期编程作为一门学科缺乏尊重和定义。

戴克斯特拉认为，早期编程深受硬件限制的影响。程序员专注于最大限度地利用缓慢、不可靠的机器，经常诉诸巧妙的技巧并优先考虑效率。这导致了一种误解，认为编程仅仅是优化计算过程。

更强大的机器的出现并没有解决编程问题，反而加剧了它们。社会利用这些机器的雄心壮志日益增长，给程序员带来了巨大的压力。戴克斯特拉批评了第三代计算机的设计，认为它们对性价比的关注导致了复杂且对程序员不友好的系统，阻碍了计算科学的进步。

他强调了硬件对思维习惯的影响的重要性，并提倡对新计算机进行客观评估。然后，他强调了EDSAC首创的子程序库作为一种促进抽象的基本软件发明的重要性。戴克斯特拉在赞扬FORTRAN最初的成功的同时，认为由于缺乏概念性辅助工具，面对日益复杂的编程挑战，它已经过时。他建议现在是时候将FORTRAN留在过去了。

---

## 74. Fossify - 一套开源、无广告的应用程序

**原文标题**: Fossify – A suite of open-source, ad-free apps

**原文链接**: [https://github.com/FossifyOrg](https://github.com/FossifyOrg)

Fossify是一套开源、注重隐私、且无广告的移动应用，源于SimpleMobileTools的停用。其使命是为所有人提供简单且隐私的技术。该平台鼓励社区参与，途径包括：用于解决影响多个应用的问题的通用问题区、用于分享想法的通用讨论区，以及贡献代码和翻译的机会。如有问题或反馈，用户可前往讨论论坛或通过电子邮件hello@fossify.org直接联系Fossify。Fossify强调并感谢用户的贡献。

---

## 75. Google 试图用 Wave (2009) 重新定义电子邮件

**原文标题**: Google aims to reinvent email with Wave (2009)

**原文链接**: [https://www.cbc.ca/news/canada/how-google-aims-to-reinvent-email-with-wave-1.826825](https://www.cbc.ca/news/canada/how-google-aims-to-reinvent-email-with-wave-1.826825)

2009年，谷歌推出了雄心勃勃的Wave项目，旨在通过将电子邮件、即时通讯、维基和博客的元素合并到一个单一平台，来重塑在线交流方式。Wave由谷歌地图的创始人Lars和Jens Rasmussen开发，旨在通过实时按键可见性和文档的协作、多用户编辑来提高沟通速度。

Wave提供了回放等功能，允许用户查看对话中的更改历史，以及拖放文件共享。用户可以将wave嵌入网页，有效地创建实时评论区或聊天室。该平台支持扩展和应用程序，从而实现诸如wave内游戏和协作地图编辑等功能。

谷歌强调了自然语言处理能力，包括高级拼写检查和实时翻译。Wave采用了开源协议，鼓励开发者创建应用程序并改进服务。

尽管有些人称赞Wave是一个革命性的概念，但另一些人，如微软的Ray Ozzie，则批评其复杂性。人们对Wave如何与现有电子邮件系统交互、解决与嵌入私人对话相关的隐私问题以及减轻类似于维基百科上出现的潜在“编辑战”表示担忧。尽管议论纷纷，但随着公众等待更广泛地访问该平台，许多问题仍未得到解答。

---

## 76. 萨姆·奥特曼称Meta曾向OpenAI员工提供1亿美元奖金

**原文标题**: Sam Altman says Meta offered OpenAI staffers $100M bonuses

**原文链接**: [https://www.bloomberg.com/news/articles/2025-06-17/altman-says-meta-offered-openai-staffers-100-million-bonuses](https://www.bloomberg.com/news/articles/2025-06-17/altman-says-meta-offered-openai-staffers-100-million-bonuses)

无法访问文章链接。

---

## 77. 考古学家发现埋藏地下五千年的古代面包

**原文标题**: Archaeologists unearth ancient bread that survived underground for 5k years

**原文链接**: [https://www.foxnews.com/food-drink/archaeologists-unearth-ancient-bread-survived-underground-5000-years](https://www.foxnews.com/food-drink/archaeologists-unearth-ancient-bread-survived-underground-5000-years)

土耳其考古学家在埃斯基谢希尔省的库鲁欧巴遗址出土一块有5000年历史的面包。这块面包可追溯到土耳其青铜时代（公元前3300年），被发现烧焦并埋在一处住宅入口下方，据信是这种埋藏方式保存了它。这块罕见的发现直径约5英寸，为了解古代烹饪方法提供了线索。

考古学家穆拉特·图尔克泰基强调，在挖掘过程中发现完整面包非常罕见。受这一发现的启发，土耳其面包师现在正在使用适合干旱条件的古老小麦，以及小扁豆和碾碎干小麦来重制这种古老面包。据面包店经理塞拉普·居勒称，最终产品是一种低麸质、不含防腐剂的面包。

重制的面包已经受到当地人的欢迎，一位顾客表示对它的味道感到好奇。文章还指出，发现保存完好的古代食物非常罕见，并引用了之前的发现，比如在中国发现的3500年历史的开菲尔奶酪和在西班牙发现的世界上最古老的一瓶葡萄酒。

---

## 78. 用自制球磨机制作的氮化铁永磁体[视频]

**原文标题**: Iron nitride permanent magnets made with DIY ball mill [video]

**原文链接**: [https://www.youtube.com/watch?v=M6XIgdS1rzs](https://www.youtube.com/watch?v=M6XIgdS1rzs)

这个名为“自制球磨机制作氮化铁永磁体”的YouTube视频，很可能展示了一种使用自制球磨机制造氮化铁永磁体的方法。虽然提供的文字主要是YouTube样板内容，但标题给出了主要思路：该视频展示了一种使用氮化铁制造永磁体的DIY方法，该方法通过球磨过程实现，很可能使用自制或经过大量改造的机器进行。

在没有观看实际视频的情况下，我们可以推断它可能涵盖：

*   **材料：** 讨论所需的材料，包括铁粉、氮源（可能是氨气或氮气）以及用于构建或改造球磨机的材料。
*   **过程：** 解释球磨过程，包括研磨时长、气氛控制以及任何必要的热处理。它可能会详细说明铁和氮如何在球磨机内反应形成氮化铁。
*   **测试：** 展示如何测试生成的氮化铁材料，以确认其磁性能。这可能包括展示吸引铁磁性物体的简单测试，或更复杂的磁矫顽力和剩余磁通密度测量。
*   **DIY方面：** 强调DIY球磨机的构造和功能，解释为实现预期结果所做的任何修改或调整。

该视频很可能面向爱好者、创客以及对材料科学和DIY项目感兴趣的人。它展示了一种可能具有成本效益的方法，可以使用相对容易获得的技术来生产永磁体。

---

## 79. 基准测试：snapDOM 对比 html2canvas

**原文标题**: Benchmark: snapDOM vs html2canvas

**原文链接**: [https://zumerlab.github.io/snapdom/](https://zumerlab.github.io/snapdom/)

本文呈现了一个基准测试，比较了两个 JavaScript 库 snapDOM 和 html2canvas 在将 DOM 元素捕获为 canvas 图像方面的性能。该基准测试的重点是通过让每个库捕获相同的 DOM 元素五次，然后计算平均执行时间来衡量它们的速度。

本文提供了一个实时交互测试，用户可以启动该基准测试。它展示了各种测试用例，旨在评估每个库在处理不同场景时的表现，包括：

*   **基本元素：** 简单的 "Hello SnapDOM!" 文本。
*   **动画：** 带有 CSS 过渡和动画的元素。
*   **CSS 框架：** 捕获使用 Orbit CSS 框架设置样式的元素。
*   **Google 字体：** 使用 Google 字体，测试嵌入字体数据的能力。
*   **Shadow DOM：** 捕获 Shadow DOM 结构中的元素。
*   **Canvas 元素：** 捕获现有的 canvas 元素。
*   **导出格式：** 测试导出为 PNG、JPG 和 WebP 的能力。
*   **伪元素：** 捕获使用 CSS 伪元素设置样式的元素。
*   **Clip-path：** 测试带有剪切路径的元素。
*   **混合模式：** 捕获混合内容
*   **整页捕获：** 捕获整个页面

本文包含使用两个库“捕获”每个测试元素和“下载”生成的 canvas 图像的按钮。基准测试的结果，显示哪个库更快，预计在运行测试后显示，但当前摘录未提供最终结果。

---

## 80. 神职人员服用裸盖菇素会发生什么

**原文标题**: What happens when clergy take psilocybin

**原文链接**: [https://nautil.us/clergy-blown-away-by-psilocybin-1217112/](https://nautil.us/clergy-blown-away-by-psilocybin-1217112/)

神职人员被赛洛西宾震撼一文探讨了一项研究，该研究中来自不同信仰（浸信会、天主教、犹太教、伊斯兰教、佛教）的33位宗教领袖服用了高剂量的赛洛西宾，即迷幻蘑菇中的活性成分。该研究发表在《迷幻药医学》杂志上，结果显示，超过90%的参与者认为这次体验是他们一生中最具精神意义和最神圣的体验之一，近一半的人称之为他们经历过的最深刻的体验。许多人觉得这使他们成为更好的宗教领袖，导致一些人将迷幻药纳入他们的教义中，并培养对各种宗教体验的开放性。

这项由约翰·霍普金斯大学和纽约大学进行的研究，由于在资金和研究人员参与方面的伦理问题，以及方法论上的缺陷，出版延迟。这些缺陷包括招募中存在的潜在偏见，以及一个小型、严重偏向白人、男性和基督教的样本，缺乏对许多主要世界宗教的代表性。

尽管存在这些局限性，该研究引发了关于致幻剂与宗教体验之间联系的问题。虽然主要世界宗教通常不提倡改变精神状态的物质，但数千年来，土著文化在神圣仪式中使用过它们。该文章还提到了威廉·詹姆斯关于神秘体验的重要性和宇宙多元论的观点，这些观点部分受到了幻觉体验的影响。文章最终给读者留下的印象是，赛洛西宾与宗教体验之间的关系是复杂而微妙的。

---

## 81. 基于CPU的拣货到零件托盘仓库布局设计

**原文标题**: CPU-Based Layout Design for Picker-to-Parts Pallet Warehouses

**原文链接**: [https://arxiv.org/abs/2506.04266](https://arxiv.org/abs/2506.04266)

Timo Looms和Lin Xie的这篇arXiv文章 (arXiv:2506.04266) 提出了一种受CPU架构启发的拣货员到货位托盘仓库的新型仓库布局设计。该论文旨在解决传统仓库布局效率低下的问题，这些问题通常导致过长的行进距离和高昂的人工成本。

所提出的基于CPU的布局将仓库划分为三个专门的区域：性能区（P）、效率区（E）和共享区（S）。研究人员使用离散事件仿真将这种布局的性能与传统的矩形布局（包括随机存储和ABC存储）以及飞翼V型布局进行了比较。

仿真结果表明，与其他布局相比，基于CPU的布局显著提高了吞吐量并减少了人工需求。这表明受CPU启发的设计具有优化仓库运营的潜力。

该文章共8页，包含6个图，并已提交会议。它在计算机科学领域被归类为多智能体系统 (cs.MA) 和硬件架构 (cs.AR)。

---

## 82. 旅行作家的两难：分享还是保守？

**原文标题**: The Travel Writer's Dilemma: Share, or Gatekeep?

**原文链接**: [https://www.nytimes.com/2025/06/10/travel/travel-writing-secret-discoveries.html](https://www.nytimes.com/2025/06/10/travel/travel-writing-secret-discoveries.html)

无法访问文章链接。

---

## 83. 使用 AI 助手撰写论文任务时认知负债的累积

**原文标题**: Accumulation of cognitive debt when using an AI assistant for essay writing task

**原文链接**: [https://arxiv.org/abs/2506.08872](https://arxiv.org/abs/2506.08872)

你的大脑与ChatGPT：使用AI助手进行论文写作任务时认知负债的累积

---

## 84. O3 专业版

**原文标题**: O3 Turns Pro

**原文链接**: [https://thezvi.substack.com/p/o3-turns-pro](https://thezvi.substack.com/p/o3-turns-pro)

无法访问文章链接。

---

## 85. OpenAI赢得2亿美元美国国防合同

**原文标题**: OpenAI wins $200M U.S. defense contract

**原文链接**: [https://www.cnbc.com/2025/06/16/openai-wins-200-million-us-defense-contract.html](https://www.cnbc.com/2025/06/16/openai-wins-200-million-us-defense-contract.html)

OpenAI与美国国防部达成2亿美元合同，为其提供人工智能工具，以应对国家安全挑战和行政管理。这项为期一年的合同是OpenAI与国防部之间的首个直接协议，隶属于OpenAI的“OpenAI for Government”新计划。

人工智能将被用于构建战争和企业领域的解决方案原型，重点是改善诸如军人医疗保健、简化项目和采购数据分析以及加强网络防御等领域。OpenAI强调，所有用例都必须遵守其使用政策。大部分工作将在华盛顿特区地区进行。

此前，OpenAI曾与国防科技初创公司Anduril合作。不久前，竞争对手Anthropic也宣布与Palantir和亚马逊合作，向美国国防和情报机构提供人工智能模型。OpenAI首席执行官Sam Altman表示，他很自豪能参与到国家安全领域。

虽然这笔交易意义重大，但2亿美元的合同仅占OpenAI总收入的一小部分，该公司年化销售额已超过100亿美元，最近估值达3000亿美元。此外，OpenAI正在通过5000亿美元的“星门”项目，致力于提高其在美国的计算能力。微软是OpenAI的关键合作伙伴，提供云基础设施，其Azure OpenAI服务也已获得授权，可以为国防信息系统局处理机密信息。

---

## 86. 你的呼吸方式就像能识别你的指纹。

**原文标题**: How you breathe is like a fingerprint that can identify you

**原文链接**: [https://www.nature.com/articles/d41586-025-01835-0](https://www.nature.com/articles/d41586-025-01835-0)

本文探讨了一项研究，该研究表明，人的呼吸模式具有唯一性，如同指纹，可用于识别身份，并可能揭示其身心健康信息。研究人员开发了一种可穿戴设备，用于追踪参与者24小时内的鼻孔气流。通过分析呼吸模式的各种参数，一种机器学习算法能够以高精度识别个体，即使在数周或数月后也是如此。呼吸特征数据集越大，准确性越高。

该研究还发现，呼吸模式与BMI以及抑郁和焦虑指标之间存在相关性，这是基于问卷调查结果得出的。例如，BMI较高和较低的个体之间的睡眠呼吸模式不同，而焦虑或抑郁评分较高的人表现出不同的吸气和呼气模式。研究人员认为，这种“通过鼻子读取思维”的方法有可能成为一种强大的诊断工具。

---

## 87. 四色视觉

**原文标题**: Tetrachromatic Vision

**原文链接**: [https://www.bookofjoe.com/2025/05/my-entry-32.html](https://www.bookofjoe.com/2025/05/my-entry-32.html)

无法访问文章链接。

---

## 88. 构建可访问UI的自私理由

**原文标题**: Selfish reasons for building accessible UIs

**原文链接**: [https://nolanlawson.com/2025/06/16/selfish-reasons-for-building-accessible-uis/](https://nolanlawson.com/2025/06/16/selfish-reasons-for-building-accessible-uis/)

Nolan Lawson认为，构建无障碍用户界面不仅是道义上的必要，也能为开发者自身带来切实的益处。他批评了常见的“吃蔬菜”式无障碍倡导方式，转而强调实际优势。

首先，无障碍HTML（使用语义化元素如`<table>`、`<th>`、`<td>`以及ARIA角色）能显著提高调试效率。它在DevTools中提供清晰的结构，相比于在充斥着通用CSS类的“div汤”中摸索，能更容易地识别和修复问题。

其次，无障碍指南，特别是WAI ARIA，为UI组件提供了明确的命名规范（例如，使用“combobox”而不是争论“autocomplete”和“dropdown”）。使用ARIA属性还可以简化CSS样式，并通过减少冗余来提高代码可读性。从角色和ARIA属性的角度思考也能加深开发者对界面的理解。

第三，无障碍用户界面更易于测试。开发者可以使用基于标签和角色的语义化选择器（例如，`getByLabel('Name')`，`getByRole('button')`），而不是依赖脆弱的CSS类或文本搜索，从而获得更具弹性的测试。

最后，无障碍用户界面能够满足依赖键盘导航的高级用户。确保基本的键盘可访问性（例如，Esc键关闭对话框，Enter键提交表单）可以提高开发者和其他键盘用户的易用性。

Lawson最后承认了Web无障碍的糟糕现状，并引用了WebAIM的数据。他认为人工智能最终可能会实现无障碍自动化，但在那之前，开发者有责任构建无障碍界面，即使他们的动机是出于自身利益。

---

## 89. 利用卫星图像计算储油罐的占用率

**原文标题**: Calculating Oil Storage Tank Occupancy with Help of Satellite Imagery

**原文链接**: [https://medium.com/planet-stories/a-beginners-guide-to-calculating-oil-storage-tank-occupancy-with-help-of-satellite-imagery-e8f387200178](https://medium.com/planet-stories/a-beginners-guide-to-calculating-oil-storage-tank-occupancy-with-help-of-satellite-imagery-e8f387200178)

TankerTrackers.com 利用卫星图像直观确认石油储存变化，并提供全球石油市场洞察。他们专注于官方产量和储存数据不透明的地区。他们的方法依赖于分析储油罐内的阴影来估算储量水平。

该过程包括：

1.  **寻找参考点：** 使用 Google Earth 等工具的标尺确定油罐的直径。油罐的高度至关重要，可以从公司网站、照片或通过测量侧视图图像（如果可用）获得。

2.  **计算储量：** 利用投射在油罐上的阴影来确定油位。浮动顶盖直接位于油面上，随油位升降。油罐内的阴影越大，含油量越少。通过比较不同时间拍摄的图像，可以估算储量水平的变化。

文章以中国宁波为例，通过分析 Planet 提供的卫星图像，跟踪特定油罐的储存变化，来说明这种方法。最终，这种分析通过对可能无法获得的储存数据进行直观确认，帮助专业人士和业余交易者了解石油市场的变化和趋势。

---

## 90. Show HN: Nexus.js - 用于3D的Fabric.js

**原文标题**: Show HN: Nexus.js - Fabric.js for 3D

**原文链接**: [https://punk.cam/lab/nexus](https://punk.cam/lab/nexus)

无法访问文章链接。

---

## 91. 使用过保的Windows 10（通过LTSC支持至2032年）

**原文标题**: Using Windows 10 past EOL (via LTSC supported to 2032)

**原文链接**: [https://massgrave.dev/windows10_eol](https://massgrave.dev/windows10_eol)

本文概述了用户在 Windows 10 于 2025 年 10 月 14 日停止支持后，继续接收 Windows 官方更新的方案，特别是对于那些无法或不愿升级到 Windows 11 的用户。

讨论的主要解决方案包括：

1.  **扩展安全更新 (ESU):** 从微软购买 ESU 订阅，以获得长达三年的安全更新（2025 年 10 月至 2028 年 10 月）。建议使用 MAS 工具激活 ESU。
2.  **Windows 10 IoT 企业版 LTSC 2021:** 迁移到 Windows 10 IoT 企业版 LTSC 2021，该版本支持至 2032 年 1 月 13 日。指南提供了全新安装和从现有 Windows 10 版本升级，同时保留文件和应用程序的方法。
3.  **Windows 11 IoT 企业版 (GAC/LTSC) 2024:** 升级到 Windows 11 IoT 企业版 24H2 (GAC) 或 IoT 企业版 LTSC 2024 (LTSC)，它们放宽了硬件要求，允许在不满足标准 Windows 11 要求（如 TPM、安全启动和 UEFI）的系统上获得官方支持。文档详细介绍了全新安装和升级方法，强调保留文件和应用程序。

文档指出，LTSC 版本不包含预装的应用商店应用程序（除非从 GAC 版本升级），并强调 IoT 版本在功能上与企业版相同，主要区别在于许可。它还解决了在缺乏 TPM 的系统上，Windows 11 潜在的游戏兼容性问题。

---

## 92. 疑似以色列团体入侵伊朗加密货币交易所Nobitex，盗取超过8200万美元

**原文标题**: Iranian Crypto Exchange Nobitex Hacked for over $82M by Suspected Israeli Group

**原文链接**: [https://www.coindesk.com/markets/2025/06/18/iranian-crypto-exchange-nobitex-hacked-for-47m-by-suspected-israeli-group](https://www.coindesk.com/markets/2025/06/18/iranian-crypto-exchange-nobitex-hacked-for-47m-by-suspected-israeli-group)

据报道，与以色列有关联的黑客行动组织Gonjeshke Darande攻击了伊朗加密货币交易所Nobitex，窃取了超过8200万美元。该组织声称对此负责，并表示前一天也袭击了Sepah银行。他们威胁要泄露Nobitex的内部数据和源代码，称该交易所是规避制裁的“恐怖融资工具”。

区块链安全公司Elliptic估计被盗资金为8200万美元，包括比特币、狗狗币和波场币等加密货币。这些资金被转移到包含反伊朗政府情绪的个性化地址。Gonjeshke Darande似乎通过将资金发送到他们没有私钥的地址来“销毁”了这些资金，表明这次攻击主要是出于政治动机。

Nobitex证实了此次袭击，但未确认被盗资金的数额。此次袭击发生在伊朗和以色列之间网络和实体紧张局势升级之际。此前与以色列情报部门有关联的Gonjeshke Darande曾声称对伊朗基础设施的袭击负责。由于即将泄露的源代码，Nobitex目前面临信誉危机以及财务损失。

---

## 93. Show HN: Rulebook AI – AI编码 IDE 的规则和记忆管理器

**原文标题**: Show HN: Rulebook AI – rules and memory manager for AI coding IDEs

**原文链接**: [https://github.com/botingw/rulebook-ai](https://github.com/botingw/rulebook-ai)

规则手册AI提供了一个结构化的框架，旨在提升AI编码助手在Cursor、CLINE、RooCode、Windsurf和Github Copilot等平台上的性能。它通过提供通用的规则模板和记忆管理系统，解决了AI行为不一致的问题。

该模板通过定义清晰的工作流程、通过结构化文档系统实现的持久项目记忆、跨平台兼容性以及强制执行的最佳实践，来促进一致的AI行为。它专为从事复杂项目的开发人员、使用多种AI工具的团队以及寻求结构化AI工作流程的人员而设计。

主要功能包括无缝跨平台操作、通过“记忆库”实现的一致AI上下文、强制执行的软件工程最佳实践、优化的Token使用以及与最新AI助手版本的兼容性。示例演示了该框架如何通过增强的上下文促进项目规划、信息检索和功能实现。

快速入门指南详细介绍了如何使用`manage_rules.py`在目标项目存储库中安装、自定义和同步规则。它涵盖了列出可用规则集、安装模板（包括规则、记忆启动器和工具启动器）、同步自定义项、清理规则以及完全卸载框架。该指南还包括有关使用必要依赖项设置Conda环境的说明。

---

## 94. 光子在成人头部的整体传输

**原文标题**: Photon transport through the entire adult human head

**原文链接**: [https://www.spiedigitallibrary.org/journals/neurophotonics/volume-12/issue-02/025014/Photon-transport-through-the-entire-adult-human-head/10.1117/1.NPh.12.2.025014.full](https://www.spiedigitallibrary.org/journals/neurophotonics/volume-12/issue-02/025014/Photon-transport-through-the-entire-adult-human-head/10.1117/1.NPh.12.2.025014.full)

本文研究了探测直接穿透整个成年人头部的光子的可行性，从而推进了非侵入性光学脑成像的极限。研究人员使用蒙特卡洛模拟和实验时间分辨光子计数来探索光子传输路径。模拟结果表明，光可以探索大脑的所有区域，并受脑脊液等低散射和低吸收区域的引导。通过使用强大的脉冲激光器和大面积单光子敏感探测器（针对光通量进行了优化），克服了高衰减（约10^18）。

对一位皮肤白皙且无头发的受试者进行的实验成功地检测到穿透头部的光子。实验飞行时间 (ToF) 分布与模拟结果显示出良好的一致性。对光子迁移路径的分析表明，其对超出公认极限的大脑区域具有敏感性，并且源位置的重新调整可以实现对深层大脑结构的靶向探测。研究结果表明，光学技术可能能够监测先前无法到达的区域（如脑沟、中脑和小脑）的活动。该研究为推进用于中风和肿瘤检测等医疗保健应用的非侵入性脑成像技术打开了大门。

---

## 95. 西班牙电网运营商REE的误算导致停电

**原文标题**: Miscalculation by Spanish power grid operator REE contributed to blackout

**原文链接**: [https://www.reuters.com/business/energy/investigation-into-spains-april-28-blackout-shows-no-evidence-cyberattack-2025-06-17/](https://www.reuters.com/business/energy/investigation-into-spains-april-28-blackout-shows-no-evidence-cyberattack-2025-06-17/)

以下是根据标题对路透社文章的总结：

文章报道称，西班牙电网运营商西班牙电网公司（REE）的一次误算导致了4月28日发生的停电事故。对该事件的调查未发现网络攻击的证据。文章可能详细介绍了这项调查的结果，重点是REE误算的性质以及它如何导致停电。文章暗示，人为错误而非外部干扰是停电的主要原因。

---

## 96. 使用大语言模型辅助编程时过早结束的陷阱

**原文标题**: Pitfalls of premature closure with LLM assisted coding

**原文链接**: [https://www.shayon.dev/post/2025/164/pitfalls-of-premature-closure-with-llm-assisted-coding/](https://www.shayon.dev/post/2025/164/pitfalls-of-premature-closure-with-llm-assisted-coding/)

过度依赖AI代码助手可能导致“过早闭合”陷阱

---

## 97. Telnet 乐趣 (2024)

**原文标题**: Fun with Telnet (2024)

**原文链接**: [https://brandonrozek.com/blog/fun-with-telnet/](https://brandonrozek.com/blog/fun-with-telnet/)

布兰登·罗杰克的“Telnet乐趣 (2024)”向读者介绍了Telnet的怀旧魅力，重点介绍了它用于访问古怪和有趣内容的用途。文章首先引用了流行的星球大战ASCII动画，可通过 `telnet towel.blinkenlights.nl 23` 访问。

罗杰克随后提供了一系列其他有趣的Telnet地址，包括：

*   `freechess.org 5000` 用于下棋
*   `mtrek.com 1701` 用于星际迷航风格的太空战斗游戏
*   `fibs.com 4321` 用于玩西洋双陆棋
*   `mapscii.me` 用于可缩放的世界地图
*   `telehack.com` 用于包含大量文本游戏Arpanet/Usenet模拟。

作者强调Telnet通信未加密，并建议不要传输敏感信息。这篇文章鼓励读者探索和享受Telnet独特的、老派的世界。

---

## 98. Show HN: 茶碗 TUI 网页浏览器

**原文标题**: Show HN: Chawan TUI web browser

**原文链接**: [https://chawan.net/news/chawan-0-2-0.html](https://chawan.net/news/chawan-0-2-0.html)

Chawan，一款TUI网页浏览器，发布了0.2.0版本。 源代码以tarball形式提供，同时提供amd64 Linux平台的静态二进制分发包（以及.deb包），以便更轻松地安装。 该版本具备了最低可行产品（MVP）的所有预期功能，并且据信没有致命错误。 v0.2分支将来只会接收错误修复。

该软件需要libssh2、libbrotli（特别是libbrotlicommon和libbrotlidec）以及OpenSSL（3.0+）或LibreSSL（已在OpenBSD 7.7上测试）。 值得注意的是，zlib、libseccomp、termcap/ncurses和libcurl不再是依赖项。

开发者鼓励软件包维护者直接与他们联系，解决任何打包问题，以确保上游解决方案。 未来的开发将专注于改进布局性能和正确性，以及更友好的用户界面，将在主分支上继续进行，用于下一个版本。

---

## 99. 我几乎完全从“Python”切换到“uv run”了。

**原文标题**: I've almost completely switched from "Python" to "uv run"

**原文链接**: [https://actinium226.substack.com/p/ive-almost-completely-switched-from](https://actinium226.substack.com/p/ive-almost-completely-switched-from)

我无法访问文章链接。

---

## 100. “人工智能并非万灵药”：诺贝尔奖得主提出质疑

**原文标题**: 'AI is not a miracle cure': Nobel laureate raises questions

**原文链接**: [https://www.livescience.com/space/black-holes/artificial-intelligence-is-not-a-miracle-cure-nobel-laureate-raises-questions-about-ai-generated-image-of-black-hole-spinning-at-the-heart-of-our-galaxy](https://www.livescience.com/space/black-holes/artificial-intelligence-is-not-a-miracle-cure-nobel-laureate-raises-questions-about-ai-generated-image-of-black-hole-spinning-at-the-heart-of-our-galaxy)

这篇《Live Science》的文章报道了一种新型人工智能模型，该模型用于分析来自事件视界望远镜（EHT）的数据，以创建更详细的关于人马座A*（我们银河系中心的超大质量黑洞）的图像。该人工智能模型经过对先前被丢弃的“嘈杂”EHT数据的训练，表明人马座A*正以接近“最高速度”旋转，且其旋转轴指向地球。这可能为了解黑洞周围的辐射行为以及周围物质的稳定性提供见解。

然而，诺贝尔奖得主莱因哈德·根泽尔警告不要完全信任人工智能的结果，他认为输入数据的低质量可能会使模型产生偏差，从而导致图像中的潜在扭曲。根泽尔强调，“人工智能不是万能药”。

EHT是世界各地望远镜的网络，在使用甚长基线干涉测量时面临大气干扰的挑战。正如该研究的合著者、天体物理学家迈克尔·詹森所解释的那样，该人工智能模型试图克服这些挑战。詹森的团队计划通过将模型的输出与未来的EHT数据和真实世界的观测结果进行比较来完善该模型。该团队的研究结果发表在《天文学与天体物理学》杂志上。

---

