# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-06-18.md)

*最后自动更新时间: 2025-06-18 17:52:15*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 2 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 3 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 4 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 5 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 6 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 7 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 8 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 9 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 10 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 11 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 12 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 13 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 14 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 15 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 16 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 17 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 18 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 19 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 20 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 21 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 22 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 23 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 24 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 25 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 26 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 27 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 28 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 29 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 30 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 31 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 32 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 33 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 34 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 35 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 36 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 37 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 38 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 39 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 40 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 41 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 42 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 43 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 44 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 45 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 46 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 47 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 48 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 49 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 50 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 51 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 52 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 53 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 54 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 55 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 56 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 57 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 58 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 59 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 60 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 61 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 62 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 63 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 64 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 65 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 66 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 67 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 68 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 69 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 70 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 71 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 72 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 73 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 74 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 75 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 76 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 77 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 78 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 79 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 80 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 81 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 82 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 83 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 84 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 85 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 86 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 87 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 88 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 89 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 90 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 91 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
