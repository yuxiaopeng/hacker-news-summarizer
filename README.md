# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-05-24.md)

*最后自动更新时间: 2026-05-24 18:25:06*
## 1. 尤斯伯恩20世纪80年代计算机图书

**原文标题**: Usborne 1980s Computer Books

**原文链接**: [https://usborne.com/us/books/computer-and-coding-books](https://usborne.com/us/books/computer-and-coding-books)

Usborne 提供旨在向儿童教授技术与编程基础的教育资源。在传承其 20 世纪 80 年代计算机图书传统的同时，目前的系列丛书专注于 **Scratch** 和 **Python** 等现代工具。这些书籍旨在帮助当今青少年清晰地理解计算机的工作原理及编程基础。

---

## 2. 存储器已占 AI 芯片组件成本的近三分之二

**原文标题**: Memory has grown to nearly two-thirds of AI chip component costs

**原文链接**: [https://epoch.ai/data-insights/ai-chip-component-cost-shares](https://epoch.ai/data-insights/ai-chip-component-cost-shares)

Epoch AI 的一项分析显示，高带宽内存（HBM）已成为 AI 芯片生产中的首要支出，其在组件成本中的占比预计将从 2024 年第一季度的 52% 上升至 2025 年第四季度的 63%。这一增长反映了英伟达、AMD、谷歌和亚马逊等行业领先者所设计的芯片面临供应紧张和价格上涨。

从绝对数值来看，这四家设计公司的 HBM 支出预计将从 2024 年的约 120 亿美元飙升至 2025 年的 320 亿美元，是所有组件中同比增幅最大的。在同一时期，AI 芯片的总组件支出预计将从 220 亿美元增长到 520 亿美元。

在 HBM 份额增长的同时，其他类别的相对份额则出现下降或停滞：
*   **逻辑裸片：** 基本持平，维持在 13–14%。
*   **先进封装 (CoWoS)：** 从 19% 降至 15%。
*   **辅助组件：** 从 15% 降至 9%。

报告指出，HBM 在 2026 年的占比可能会进一步扩大。主要的超大规模云服务商已在调整财务预期以应对这些成本。例如，微软 2026 财年的资本支出指引中，有 250 亿美元归因于组件价格上涨；Meta 也出于类似原因将其 2026 年资本支出预期上调了 100 亿美元。

最终，Epoch AI 的研究结果凸显了 AI 硬件供应链的重大转变：内存（而非逻辑芯片或封装）现已成为硬件成本不断攀升的主要驱动因素。

---

## 3. Ruby for Good

**原文标题**: Ruby for Good

**原文链接**: [https://ti.to/codeforgood/rubyforgood](https://ti.to/codeforgood/rubyforgood)

生成摘要时出错

---

## 4. DeepSeek reasonix：高缓存、低成本的 DeepSeek 原生编程智能体

**原文标题**: DeepSeek reasonix, DeepSeek native coding agent with high caching and low cost

**原文链接**: [https://esengine.github.io/DeepSeek-Reasonix/](https://esengine.github.io/DeepSeek-Reasonix/)

生成摘要时出错

---

## 5. 约束衰减：LLM 智能体在后端代码生成中的脆弱性

**原文标题**: Constraint Decay: The Fragility of LLM Agents in Back End Code Generation

**原文链接**: [https://arxiv.org/abs/2605.06445](https://arxiv.org/abs/2605.06445)

**《约束衰减：大语言模型智能体在后端代码生成中的脆弱性》摘要**

本研究调查了大语言模型（LLM）智能体在生成生产级后端软件时的性能，重点关注其遵循严格结构约束（如架构模式、数据库和对象关系映射 ORM）的能力。虽然智能体在宽松规范下的功能性代码生成方面表现出色，但本研究揭示了它们在处理实际应用中必不可少的非功能性需求时存在关键差距。

**研究方法**
研究人员针对八种不同的 Web 框架，开展了包含 80 个新项目生成任务和 20 个功能实现任务的系统性研究。通过维持统一的 API 契约，他们隔离了结构复杂性的影响。评估采用了双重方法：端到端行为测试以及用于确保架构合规性的静态验证器。

**主要发现**
*   **约束衰减：** 作者发现了一种现象，即随着结构化要求的累积，智能体的性能急剧下降。平均而言，断言通过率从基准任务到完全指定任务下降了 30 个百分点，部分较弱的配置甚至完全失败。
*   **框架敏感性：** 智能体在极简且显式的框架（如 Flask）中的表现显著优于在重约定、复杂的环境（如 Django、FastAPI）中的表现。
*   **数据层故障：** 错误分析表明，数据层是主要的故障点，具体表现为错误的查询构建和 ORM 运行时违规。

**结论**
研究结论指出，“约束衰减”是自主编程智能体面临的主要障碍。虽然这些模型在功能上具备能力，但如何同时满足功能目标和严苛的结构要求，仍是软件工程人工智能领域的一项公开挑战。

---

## 6. Mastering Dyalog APL

**原文标题**: Mastering Dyalog APL

**原文链接**: [https://mastering.dyalog.com/README.html](https://mastering.dyalog.com/README.html)

"Mastering Dyalog APL" is widely considered the definitive resource for learning the Dyalog APL programming language. Originally published in 2009 by Bernard Legrand, the book is currently being updated to reflect modern advancements in the language and to prevent the content from becoming obsolete.

The rework, led by Rodrigo Girão Serrão with assistance from various contributors, aims to modernize the original text while preserving its core prose and examples where appropriate. Significant updates include the addition of new chapters covering features introduced after Dyalog APL version 12.0. 

To provide a more engaging learning experience, the new version is being developed using Jupyter Notebooks, allowing for interactivity. It is also available as a static online resource, with a printed version planned for future release. 

As the project is currently a work in progress, the authors encourage community feedback and error reporting via GitHub or email (mdapl@dyalog.com). Readers can also consult a changelog to track the specific revisions and additions made to this modernized edition.

---

## 7. 我花了50个小时画一张折线图

**原文标题**: I spent 50 hours drawing a line graph

**原文链接**: [https://www.dougmacdowell.com/50-hours-to-draw-some-lines.html](https://www.dougmacdowell.com/50-hours-to-draw-some-lines.html)

生成摘要时出错

---

## 8. Flick (YC F25) 诚聘前端工程师，打造 AI 影视制作领域的 Figma

**原文标题**: Flick (YC F25) Is Hiring Front End Engineer to Build Figma for AI Filmmaking

**原文链接**: [https://www.ycombinator.com/companies/flick/jobs/Tdu6FH6-senior-frontend-engineer](https://www.ycombinator.com/companies/flick/jobs/Tdu6FH6-senior-frontend-engineer)

**Flick (YC F25)** 是一家总部位于旧金山的初创公司，致力于开发被誉为电影界“Figma 和 Cursor”的 AI 原生电影制作平台。该公司由一名前 Instagram Stories 工程师和一位获奖电影制作人共同创立，将技术专长与艺术愿景相结合，旨在打造高性能的创意工具。

**职位描述**
Flick 正在寻找一名**高级前端工程师**作为创始团队成员加入。该人选将主导核心编辑器 UI 的架构与开发，包括画布、时间轴和节点图界面。此角色涉及高层级技术决策、创意工作流的快速原型设计，以及针对复杂客户端状态的性能优化。

**核心要求**
*   **经验：** 3 年以上领导高性能 Web 应用技术项目的经验。
*   **技术栈：** 精通 **React 和 TypeScript**。
*   **专业领域：** 在构建复杂 UX 交互（如编辑器、可视化生成器或多媒体工具）方面拥有深厚经验。
*   **心态：** 具备初创公司导向的工作方式，能够解决模糊性问题，并对精美、直观的界面充满热情。有视频编辑器开发经验或开源项目贡献者优先。

**薪酬福利**
*   **薪资：** 10 万美元 – 20 万美元。
*   **股权：** 0.10% – 1.00%。
*   **地点：** 加州桑尼维尔或远程办公。
*   **签证：** 可提供签证担保。

Flick 获得了顶级风投机构的充足资金支持，为您提供在 AI 与艺术交汇点塑造视觉叙事未来的机会。理想的候选人将与创始人直接合作，从零开始打造下一代创意套件。

---

## 9. Childhood Computing

**原文标题**: Childhood Computing

**原文链接**: [https://susam.net/childhood-computing.html](https://susam.net/childhood-computing.html)

In "Childhood Computing," Susam Pal reflects on his introduction to technology in 1992 as an eight-year-old in a small industrial town. His school’s computer lab featured hand-me-down IBM PC compatibles with monochrome monitors, no hard drives, and 5¼-inch floppy disks. Because of the equipment's scarcity and fragility, students followed strict rituals, such as removing shoes before entering the lab.

With only two hours of computer time per month, Pal spent most of his time writing Logo programs in physical notebooks and "testing" them on graph paper at home. This led to his first experience with "open-source" software: a Logo program for an animated house that his classmates manually copied into their own notebooks to modify. 

Pal also highlights the influence of early games like *Moon Bugs*, *Digger*, and *Grand Prix Circuit*. The latter's pseudo-3D graphics sparked a sense of wonder about the possibilities of programming. These early experiences left a lasting impact; in 2022, Pal fulfilled a childhood dream by coding *Andromeda Invaders*, a game inspired by the *Space Invaders* title he played decades earlier.

Ultimately, the article is a sensory-rich retrospective. Pal describes how the specific sounds of power-on tests and the unique smell of the air-conditioned lab remain his strongest memories, marking a period of "magical" exploration that defined his lifelong passion for computers.

---

## 10. “AI 包装”：企业正争先恐后地将自己重塑为科技驱动型公司。

**原文标题**: 'AI washing': firms are scrambling to rebrand themselves as tech-focused

**原文链接**: [https://www.theguardian.com/technology/2026/may/24/ai-washing-pr-firms-scrambling-rebrand](https://www.theguardian.com/technology/2026/may/24/ai-washing-pr-firms-scrambling-rebrand)

本文探讨了日益普遍的“AI洗白”（AI washing）现象，即企业为了利用当前的市场热潮，牵强地将现有技术或基础自动化重新包装为人工智能。

公关高管报告称，客户施加了巨大压力，要求将各种平凡的产品——从物业扫描仪、篮球架到安全激光器——宣传为“AI驱动”或“由AI赋能”。公关人员将这些行为形容为“瑜伽级别的生拉硬拽”，并指出许多公司仅仅是利用了改进后的自动化技术，而非真正的生成式人工智能。

这种误导性品牌包装的激增导致了“媒体麻木”，记者们对与AI相关的推介正变得愈发怀疑。公关专业人士对被迫发送明知站不住脚的推介稿感到沮丧，他们往往还必须劝阻品牌不要为了显得紧跟技术潮流而对AI政策发表无关痛痒的评论。

除了营销层面，这一趋势还反映了企业为了在投资者面前保持存在感而展开的更广泛的角逐。然而，这一转变也充满了社会争议。例如，渣打银行首席执行官最近不得不为将那些被AI取代的员工称为“低价值人力资本”而道歉。尽管媒体持怀疑态度且这种炒作本质上“不负责任”，但文章指出，股市投资者在很大程度上仍在继续支持AI热潮，这激励着企业不顾技术准确性，持续追逐这一标签。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 2 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 3 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 4 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 5 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 6 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 7 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 8 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 9 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 10 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 11 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 12 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 13 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 14 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 15 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 16 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 17 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 18 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 19 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 20 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 21 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 22 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 23 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 24 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 25 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 26 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 27 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 28 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 29 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 30 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 31 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 32 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 33 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 34 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 35 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 36 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 37 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 38 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 39 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 40 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 41 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 42 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 43 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 44 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 45 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 46 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 47 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 48 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 49 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 50 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 51 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 52 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 53 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 54 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 55 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 56 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 57 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 58 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 59 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 60 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 61 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 62 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 63 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 64 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 65 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 66 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 67 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 68 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 69 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 70 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 71 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 72 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 73 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 74 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 75 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 76 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 77 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 78 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 79 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 80 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 81 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 82 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 83 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 84 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 85 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 86 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 87 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 88 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 89 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 90 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 91 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 92 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 93 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 94 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 95 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 96 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 97 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 98 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 99 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 100 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 101 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 102 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 103 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 104 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 105 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 106 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 107 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 108 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 109 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 110 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 111 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 112 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 113 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 114 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 115 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 116 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 117 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 118 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 119 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 120 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 121 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 122 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 123 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 124 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 125 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 126 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 127 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 128 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 129 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 130 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 131 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 132 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 133 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 134 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 135 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 136 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 137 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 138 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 139 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 140 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 141 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 142 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 143 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 144 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 145 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 146 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 147 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 148 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 149 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 150 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 151 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 152 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 153 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 154 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 155 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 156 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 157 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 158 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 159 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 160 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 161 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 162 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 163 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 164 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 165 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 166 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 167 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 168 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 169 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 170 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 171 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 172 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 173 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 174 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 175 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 176 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 177 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 178 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 179 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 180 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 181 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 182 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 183 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 184 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 185 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 186 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 187 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 188 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 189 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 190 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 191 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 192 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 193 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 194 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 195 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 196 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 197 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 198 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 199 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 200 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 201 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 202 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 203 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 204 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 205 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 206 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 207 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 208 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 209 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 210 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 211 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 212 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 213 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 214 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 215 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 216 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 217 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 218 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 219 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 220 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 221 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 222 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 223 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 224 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 225 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 226 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 227 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 228 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 229 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 230 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 231 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 232 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 233 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 234 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 235 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 236 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 237 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 238 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 239 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 240 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 241 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 242 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 243 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 244 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 245 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 246 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 247 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 248 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 249 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 250 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 251 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 252 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 253 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 254 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 255 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 256 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 257 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 258 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 259 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 260 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 261 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 262 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 263 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 264 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 265 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 266 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 267 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 268 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 269 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 270 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 271 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 272 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 273 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 274 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 275 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 276 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 277 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 278 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 279 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 280 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 281 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 282 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 283 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 284 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 285 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 286 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 287 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 288 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 289 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 290 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 291 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 292 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 293 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 294 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 295 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 296 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 297 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 298 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 299 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 300 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 301 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 302 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 303 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 304 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 305 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 306 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 307 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 308 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 309 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 310 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 311 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 312 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 313 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 314 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 315 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 316 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 317 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 318 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 319 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 320 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 321 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 322 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 323 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 324 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 325 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 326 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 327 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 328 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 329 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 330 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 331 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 332 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 333 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 334 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 335 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 336 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 337 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 338 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 339 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 340 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 341 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 342 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 343 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 344 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 345 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 346 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 347 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 348 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 349 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 350 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 351 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 352 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 353 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 354 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 355 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 356 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 357 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 358 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 359 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 360 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 361 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 362 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 363 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 364 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 365 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 366 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 367 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 368 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 369 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 370 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 371 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 372 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 373 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 374 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 375 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 376 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 377 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 378 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 379 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 380 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 381 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 382 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 383 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 384 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 385 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 386 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 387 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 388 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 389 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 390 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 391 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 392 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 393 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 394 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 395 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 396 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 397 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 398 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 399 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 400 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 401 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 402 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 403 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 404 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 405 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 406 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 407 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 408 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 409 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 410 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 411 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 412 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 413 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 414 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 415 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 416 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 417 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 418 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 419 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 420 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 421 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 422 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 423 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 424 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 425 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 426 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 427 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 428 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 429 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 430 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
