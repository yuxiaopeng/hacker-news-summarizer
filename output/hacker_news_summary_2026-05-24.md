# Hacker News 热门文章摘要 (2026-05-24)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. I keep bouncing off the Scheme language

**原文标题**: I keep bouncing off the Scheme language

**原文链接**: [https://www.sicpers.info/2026/05/i-keep-bouncing-off-the-scheme-language/](https://www.sicpers.info/2026/05/i-keep-bouncing-off-the-scheme-language/)

生成摘要时出错

---

## 12. Microsoft open-sources "the earliest DOS source code discovered to date"

**原文标题**: Microsoft open-sources "the earliest DOS source code discovered to date"

**原文链接**: [https://arstechnica.com/gadgets/2026/04/microsoft-open-sources-the-earliest-dos-source-code-discovered-to-date/](https://arstechnica.com/gadgets/2026/04/microsoft-open-sources-the-earliest-dos-source-code-discovered-to-date/)

生成摘要时出错

---

## 13. FreeBSD Foundation Executive Director Tries Daily Driving FreeBSD on Laptop

**原文标题**: FreeBSD Foundation Executive Director Tries Daily Driving FreeBSD on Laptop

**原文链接**: [https://www.phoronix.com/news/FreeBSD-On-Laptop-Driver](https://www.phoronix.com/news/FreeBSD-On-Laptop-Driver)

生成摘要时出错

---

## 14. Perceptual Image Codec: What Matters in Practical Learned Image Compression

**原文标题**: Perceptual Image Codec: What Matters in Practical Learned Image Compression

**原文链接**: [https://apple.github.io/ml-pico/](https://apple.github.io/ml-pico/)

生成摘要时出错

---

## 15. Build Adafruit projects right from Firefox

**原文标题**: Build Adafruit projects right from Firefox

**原文链接**: [https://www.firefox.com/en-US/landing/adafruit/](https://www.firefox.com/en-US/landing/adafruit/)

生成摘要时出错

---

## 16. Curly braces: An evolution of Unix and C

**原文标题**: Curly braces: An evolution of Unix and C

**原文链接**: [https://thalia.dev/blog/unix-braces/](https://thalia.dev/blog/unix-braces/)

生成摘要时出错

---

## 17. Wake up! 16b

**原文标题**: Wake up! 16b

**原文链接**: [https://hellmood.111mb.de/wake_up_16b_writeup.html](https://hellmood.111mb.de/wake_up_16b_writeup.html)

生成摘要时出错

---

## 18. Scammers are abusing an internal Microsoft account to send spam links

**原文标题**: Scammers are abusing an internal Microsoft account to send spam links

**原文链接**: [https://techcrunch.com/2026/05/21/scammers-are-abusing-an-internal-microsoft-account-to-send-spam/](https://techcrunch.com/2026/05/21/scammers-are-abusing-an-internal-microsoft-account-to-send-spam/)

生成摘要时出错

---

## 19. Noroboto: Lying Fonts and Mitigation in Rust

**原文标题**: Noroboto: Lying Fonts and Mitigation in Rust

**原文链接**: [https://tritium.legal/blog/noroboto](https://tritium.legal/blog/noroboto)

生成摘要时出错

---

## 20. The C64 Dead Test Font

**原文标题**: The C64 Dead Test Font

**原文链接**: [https://www.masswerk.at/nowgobang/2026/c64-dead-test-font](https://www.masswerk.at/nowgobang/2026/c64-dead-test-font)

生成摘要时出错

---

## 21. Silk: Open-source cooperative fiber scheduler

**原文标题**: Silk: Open-source cooperative fiber scheduler

**原文链接**: [https://github.com/ClickHouse/silk](https://github.com/ClickHouse/silk)

生成摘要时出错

---

## 22. Swap tables, flash-friendly swap, swap_ops, and more

**原文标题**: Swap tables, flash-friendly swap, swap_ops, and more

**原文链接**: [https://lwn.net/SubscriberLink/1072657/394b87abd7cc215e/](https://lwn.net/SubscriberLink/1072657/394b87abd7cc215e/)

生成摘要时出错

---

## 23. Predicting the 2026 Bristol Bay and Kodiak Salmon Runs

**原文标题**: Predicting the 2026 Bristol Bay and Kodiak Salmon Runs

**原文链接**: [https://www.salmonfinder.com/2026/05/13/bristol-bay-kodiak-predictions-2026](https://www.salmonfinder.com/2026/05/13/bristol-bay-kodiak-predictions-2026)

生成摘要时出错

---

## 24. Alexander Grothendieck Revolutionized 20th-Century Mathematics

**原文标题**: Alexander Grothendieck Revolutionized 20th-Century Mathematics

**原文链接**: [https://www.quantamagazine.org/how-alexander-grothendieck-revolutionized-20th-century-mathematics-20260520/](https://www.quantamagazine.org/how-alexander-grothendieck-revolutionized-20th-century-mathematics-20260520/)

生成摘要时出错

---

## 25. Time to talk about my writerdeck

**原文标题**: Time to talk about my writerdeck

**原文链接**: [https://veronicaexplains.net/my-first-writerdeck/](https://veronicaexplains.net/my-first-writerdeck/)

生成摘要时出错

---

## 26. Converting an Integer to a Decimal String in Under Two Nanoseconds

**原文标题**: Converting an Integer to a Decimal String in Under Two Nanoseconds

**原文链接**: [https://onlinelibrary.wiley.com/doi/10.1002/spe.70079](https://onlinelibrary.wiley.com/doi/10.1002/spe.70079)

生成摘要时出错

---

## 27. On The <dl> (2021)

**原文标题**: On The <dl> (2021)

**原文链接**: [https://benmyers.dev/blog/on-the-dl/](https://benmyers.dev/blog/on-the-dl/)

生成摘要时出错

---

## 28. DeepSeek to Make Permanent 75% Discount on Flagship AI Model

**原文标题**: DeepSeek to Make Permanent 75% Discount on Flagship AI Model

**原文链接**: [https://www.bloomberg.com/news/articles/2026-05-23/deepseek-to-make-permanent-75-discount-on-flagship-ai-model](https://www.bloomberg.com/news/articles/2026-05-23/deepseek-to-make-permanent-75-discount-on-flagship-ai-model)

生成摘要时出错

---

## 29. Artificial egg hatched 26 healthy chickens

**原文标题**: Artificial egg hatched 26 healthy chickens

**原文链接**: [https://www.nationalgeographic.com/science/article/artificial-egg-colossal-chickens-moa-dodo](https://www.nationalgeographic.com/science/article/artificial-egg-colossal-chickens-moa-dodo)

生成摘要时出错

---

## 30. Greg Brockman interview [video]

**原文标题**: Greg Brockman interview [video]

**原文链接**: [https://fs.blog/knowledge-project-podcast/greg-brockman/](https://fs.blog/knowledge-project-podcast/greg-brockman/)

生成摘要时出错

---

## 31. My two-part desk setup (2025)

**原文标题**: My two-part desk setup (2025)

**原文链接**: [https://arslan.io/2025/11/18/my-two-part-desk-setup/](https://arslan.io/2025/11/18/my-two-part-desk-setup/)

生成摘要时出错

---

## 32. Why is Vivado 2026.1 dropping Linux support for free tier?

**原文标题**: Why is Vivado 2026.1 dropping Linux support for free tier?

**原文链接**: [https://adaptivesupport.amd.com/s/question/0D5Pd00001YQLdMKAX/why-is-vivado-20261-dropping-linux-support-for-free-tier-?language=en_US](https://adaptivesupport.amd.com/s/question/0D5Pd00001YQLdMKAX/why-is-vivado-20261-dropping-linux-support-for-free-tier-?language=en_US)

生成摘要时出错

---

## 33. Omarchy Is Not A Distro

**原文标题**: Omarchy Is Not A Distro

**原文链接**: [https://abyss.fish/your_dotfiles_are_not_a_distro](https://abyss.fish/your_dotfiles_are_not_a_distro)

生成摘要时出错

---

## 34. When (if ever) it's appropriate to make jokes before the US Supreme Court

**原文标题**: When (if ever) it's appropriate to make jokes before the US Supreme Court

**原文链接**: [https://www.scotusblog.com/2026/05/when-if-ever-its-appropriate-to-make-jokes-take-selfies-or-curse-before-the-court/](https://www.scotusblog.com/2026/05/when-if-ever-its-appropriate-to-make-jokes-take-selfies-or-curse-before-the-court/)

生成摘要时出错

---

## 35. My I3-Emacs Integration

**原文标题**: My I3-Emacs Integration

**原文链接**: [https://khz.ac/software/i3-integration.html](https://khz.ac/software/i3-integration.html)

生成摘要时出错

---

## 36. Green card seekers must leave U.S. to apply, Trump administration says

**原文标题**: Green card seekers must leave U.S. to apply, Trump administration says

**原文链接**: [https://www.nytimes.com/2026/05/22/us/politics/green-card-changes-trump.html](https://www.nytimes.com/2026/05/22/us/politics/green-card-changes-trump.html)

生成摘要时出错

---

## 37. Sales and Dungeons: Thermal printer TTRPG utility

**原文标题**: Sales and Dungeons: Thermal printer TTRPG utility

**原文链接**: [https://sales-and-dungeons.app/](https://sales-and-dungeons.app/)

生成摘要时出错

---

## 38. Key, in sight – A guide, of sorts, to keyboard customization

**原文标题**: Key, in sight – A guide, of sorts, to keyboard customization

**原文链接**: [https://aresluna.org/key-in-sight/](https://aresluna.org/key-in-sight/)

生成摘要时出错

---

## 39. Show HN: Git-based front-end interface for Hugo

**原文标题**: Show HN: Git-based front-end interface for Hugo

**原文链接**: [https://github.com/arashthr/hugo-flow](https://github.com/arashthr/hugo-flow)

生成摘要时出错

---

## 40. Hengefinder: Finding when the sun aligns with your street

**原文标题**: Hengefinder: Finding when the sun aligns with your street

**原文链接**: [https://victoriaritvo.com/blog/hengefinder/](https://victoriaritvo.com/blog/hengefinder/)

生成摘要时出错

---

## 41. Judson's Last Ride

**原文标题**: Judson's Last Ride

**原文链接**: [https://www.realclearpolitics.com/articles/2026/05/22/judsons_last_ride_154150.html](https://www.realclearpolitics.com/articles/2026/05/22/judsons_last_ride_154150.html)

生成摘要时出错

---

## 42. 80386 microcode disassembled

**原文标题**: 80386 microcode disassembled

**原文链接**: [https://www.reenigne.org/blog/80386-microcode-disassembled/](https://www.reenigne.org/blog/80386-microcode-disassembled/)

生成摘要时出错

---

## 43. -​-dangerously-skip-reading-code

**原文标题**: -​-dangerously-skip-reading-code

**原文链接**: [https://olano.dev/blog/dangerously-skip/](https://olano.dev/blog/dangerously-skip/)

生成摘要时出错

---

## 44. Schlitz Is Gone, but First It's Getting One Last Hurrah

**原文标题**: Schlitz Is Gone, but First It's Getting One Last Hurrah

**原文链接**: [https://www.milwaukeemag.com/schlitz-is-gone/](https://www.milwaukeemag.com/schlitz-is-gone/)

生成摘要时出错

---

## 45. Spanish court declines to fine NordVPN over LaLiga piracy blocking order

**原文标题**: Spanish court declines to fine NordVPN over LaLiga piracy blocking order

**原文链接**: [https://torrentfreak.com/spanish-court-declines-to-fine-nordvpn-over-laliga-piracy-blocking-order/](https://torrentfreak.com/spanish-court-declines-to-fine-nordvpn-over-laliga-piracy-blocking-order/)

生成摘要时出错

---

## 46. Don't Roll Your Own

**原文标题**: Don't Roll Your Own

**原文链接**: [https://susam.net/do-not-roll-your-own.html](https://susam.net/do-not-roll-your-own.html)

生成摘要时出错

---

## 47. Microsoft's 6502 BASIC is now Open Source (2025)

**原文标题**: Microsoft's 6502 BASIC is now Open Source (2025)

**原文链接**: [https://opensource.microsoft.com/blog/2025/09/03/microsoft-open-source-historic-6502-basic/](https://opensource.microsoft.com/blog/2025/09/03/microsoft-open-source-historic-6502-basic/)

生成摘要时出错

---

## 48. Reverse engineering circuitry in a Spacelab computer from 1980

**原文标题**: Reverse engineering circuitry in a Spacelab computer from 1980

**原文链接**: [https://www.righto.com/2026/05/reverse-engineering-spacelab-computer.html](https://www.righto.com/2026/05/reverse-engineering-spacelab-computer.html)

生成摘要时出错

---

## 49. Amazon Web Services – Four Years and Out

**原文标题**: Amazon Web Services – Four Years and Out

**原文链接**: [https://www.adventuresinoss.com/aws-four-years/](https://www.adventuresinoss.com/aws-four-years/)

生成摘要时出错

---

## 50. PHP's Oddities

**原文标题**: PHP's Oddities

**原文链接**: [https://flowtwo.io/post/php%27s-oddities](https://flowtwo.io/post/php%27s-oddities)

生成摘要时出错

---

## 51. Making deep learning go brrrr from first principles (2022)

**原文标题**: Making deep learning go brrrr from first principles (2022)

**原文链接**: [https://horace.io/brrr_intro.html](https://horace.io/brrr_intro.html)

生成摘要时出错

---

## 52. What it takes to transpose a matrix

**原文标题**: What it takes to transpose a matrix

**原文链接**: [https://gudok.xyz/transpose/](https://gudok.xyz/transpose/)

生成摘要时出错

---

## 53. DeepSeek makes the V4 Pro price discount permanent

**原文标题**: DeepSeek makes the V4 Pro price discount permanent

**原文链接**: [https://api-docs.deepseek.com/quick_start/pricing](https://api-docs.deepseek.com/quick_start/pricing)

生成摘要时出错

---

## 54. .NET (OK, C#) finally gets union types

**原文标题**: .NET (OK, C#) finally gets union types

**原文链接**: [https://andrewlock.net/exploring-the-dotnet-11-preview-2-dotnet-gets-union-types/](https://andrewlock.net/exploring-the-dotnet-11-preview-2-dotnet-gets-union-types/)

生成摘要时出错

---

## 55. Of Course They Booed

**原文标题**: Of Course They Booed

**原文链接**: [https://2ndbreakfast.audreywatters.com/of-c/](https://2ndbreakfast.audreywatters.com/of-c/)

生成摘要时出错

---

## 56. New map reveals lost roads of the Roman Empire

**原文标题**: New map reveals lost roads of the Roman Empire

**原文链接**: [https://www.scientificamerican.com/article/new-high-resolution-map-transforms-what-we-know-about-roman-roads-and-the-roman-empire/](https://www.scientificamerican.com/article/new-high-resolution-map-transforms-what-we-know-about-roman-roads-and-the-roman-empire/)

生成摘要时出错

---

## 57. SpaceX launches Starship v3 rocket

**原文标题**: SpaceX launches Starship v3 rocket

**原文链接**: [https://www.space.com/space-exploration/launches-spacecraft/spacex-starship-v3-megarocket-first-test-flight](https://www.space.com/space-exploration/launches-spacecraft/spacex-starship-v3-megarocket-first-test-flight)

生成摘要时出错

---

## 58. Neoclassical C++: segmented iterators revisited

**原文标题**: Neoclassical C++: segmented iterators revisited

**原文链接**: [https://boostedcpp.net/2026/05/18/neoclassical-c-segmented-iterators-revisited-1/](https://boostedcpp.net/2026/05/18/neoclassical-c-segmented-iterators-revisited-1/)

生成摘要时出错

---

## 59. Show HN: Kanban CLI (A local-first, agent-first task manager for the terminal)

**原文标题**: Show HN: Kanban CLI (A local-first, agent-first task manager for the terminal)

**原文链接**: [https://codeberg.org/hydrafog/kanban](https://codeberg.org/hydrafog/kanban)

生成摘要时出错

---

## 60. Improving C# Memory Safety

**原文标题**: Improving C# Memory Safety

**原文链接**: [https://devblogs.microsoft.com/dotnet/improving-csharp-memory-safety/](https://devblogs.microsoft.com/dotnet/improving-csharp-memory-safety/)

生成摘要时出错

---

## 61. Air France and Airbus found guilty of manslaughter over 2009 plane crash

**原文标题**: Air France and Airbus found guilty of manslaughter over 2009 plane crash

**原文链接**: [https://www.bbc.com/news/articles/czd2qmdvmq6o](https://www.bbc.com/news/articles/czd2qmdvmq6o)

生成摘要时出错

---

## 62. Buildcraft Is a Compiler Problem

**原文标题**: Buildcraft Is a Compiler Problem

**原文链接**: [https://mitander.xyz/posts/buildcraft-is-a-compiler-problem/](https://mitander.xyz/posts/buildcraft-is-a-compiler-problem/)

生成摘要时出错

---

## 63. Project Glasswing: An Initial Update

**原文标题**: Project Glasswing: An Initial Update

**原文链接**: [https://www.anthropic.com/research/glasswing-initial-update](https://www.anthropic.com/research/glasswing-initial-update)

生成摘要时出错

---

## 64. A scoping review of bicycling interventions’ impacts on well-being

**原文标题**: A scoping review of bicycling interventions’ impacts on well-being

**原文链接**: [https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2026.1807791/full](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2026.1807791/full)

生成摘要时出错

---

## 65. Show HN: Anyone interested in a tool helps to explore C++ ASTs

**原文标题**: Show HN: Anyone interested in a tool helps to explore C++ ASTs

**原文链接**: [https://uvic-aurora.github.io/acav-manual/index.html](https://uvic-aurora.github.io/acav-manual/index.html)

生成摘要时出错

---

## 66. API proposed by Chrome: Declarative partial updates

**原文标题**: API proposed by Chrome: Declarative partial updates

**原文链接**: [https://developer.chrome.com/blog/declarative-partial-updates](https://developer.chrome.com/blog/declarative-partial-updates)

生成摘要时出错

---

## 67. The quadratic sandwich

**原文标题**: The quadratic sandwich

**原文链接**: [https://fedemagnani.github.io/math/2026/04/08/the-quadratic-sandwich.html](https://fedemagnani.github.io/math/2026/04/08/the-quadratic-sandwich.html)

生成摘要时出错

---

## 68. Miranda's Rescue was paid to save dogs, but is accused of killing them instead

**原文标题**: Miranda's Rescue was paid to save dogs, but is accused of killing them instead

**原文链接**: [https://kymkemp.com/2026/05/22/paid-to-save-them-accused-of-killing-them-the-investigation-of-mirandas-rescue/](https://kymkemp.com/2026/05/22/paid-to-save-them-accused-of-killing-them-the-investigation-of-mirandas-rescue/)

生成摘要时出错

---

## 69. Highest Random Weight in Elixir

**原文标题**: Highest Random Weight in Elixir

**原文链接**: [https://jola.dev/posts/highest-random-weight-in-elixir](https://jola.dev/posts/highest-random-weight-in-elixir)

生成摘要时出错

---

## 70. Official Kotlin Support for Visual Studio Code Is Now Available in Alpha

**原文标题**: Official Kotlin Support for Visual Studio Code Is Now Available in Alpha

**原文链接**: [https://blog.jetbrains.com/kotlin/2026/05/official-kotlin-support-for-visual-studio-code-is-now-available-in-alpha/](https://blog.jetbrains.com/kotlin/2026/05/official-kotlin-support-for-visual-studio-code-is-now-available-in-alpha/)

生成摘要时出错

---

## 71. Why Japanese companies do so many different things

**原文标题**: Why Japanese companies do so many different things

**原文链接**: [https://davidoks.blog/p/why-japanese-companies-do-so-many](https://davidoks.blog/p/why-japanese-companies-do-so-many)

生成摘要时出错

---

## 72. Kindle loyalists scramble as Amazon turns page on old e-readers

**原文标题**: Kindle loyalists scramble as Amazon turns page on old e-readers

**原文链接**: [https://www.reuters.com/business/retail-consumer/kindle-loyalists-scramble-amazon-turns-page-old-e-readers-2026-05-19/](https://www.reuters.com/business/retail-consumer/kindle-loyalists-scramble-amazon-turns-page-old-e-readers-2026-05-19/)

生成摘要时出错

---

## 73. ICE Awards $25M Iris-Scanning Contract to Bi2 Technologies

**原文标题**: ICE Awards $25M Iris-Scanning Contract to Bi2 Technologies

**原文链接**: [https://www.projectsaltbox.com/p/ice-awards-25-million-iris-scanning](https://www.projectsaltbox.com/p/ice-awards-25-million-iris-scanning)

生成摘要时出错

---

## 74. Italy moves to Airbus A330 tankers

**原文标题**: Italy moves to Airbus A330 tankers

**原文链接**: [https://www.euronews.com/my-europe/2026/05/21/italy-moves-to-airbus-a330-tankers-in-major-nato-aligned-shift](https://www.euronews.com/my-europe/2026/05/21/italy-moves-to-airbus-a330-tankers-in-major-nato-aligned-shift)

生成摘要时出错

---

## 75. NeuralNote

**原文标题**: NeuralNote

**原文链接**: [https://github.com/DamRsn/NeuralNote](https://github.com/DamRsn/NeuralNote)

生成摘要时出错

---

## 76. Electrobun 2.0 will be decoupled from Bun due to the Rust rewrite

**原文标题**: Electrobun 2.0 will be decoupled from Bun due to the Rust rewrite

**原文链接**: [https://twitter.com/YoavCodes/status/2058064720553222567](https://twitter.com/YoavCodes/status/2058064720553222567)

生成摘要时出错

---

## 77. The seed oil panic is hurting my cardiac patients

**原文标题**: The seed oil panic is hurting my cardiac patients

**原文链接**: [https://www.statnews.com/2026/05/22/seed-oils-healthy-fats-tallow-fact-check-cardiac-health/](https://www.statnews.com/2026/05/22/seed-oils-healthy-fats-tallow-fact-check-cardiac-health/)

生成摘要时出错

---

## 78. Egypt deploys jets to UAE as Iran war strains Arab alliances

**原文标题**: Egypt deploys jets to UAE as Iran war strains Arab alliances

**原文链接**: [https://www.ft.com/content/8e81a505-7aa4-4c42-a103-f89b5e095901](https://www.ft.com/content/8e81a505-7aa4-4c42-a103-f89b5e095901)

生成摘要时出错

---

## 79. A 1955 Los Alamos computer experiment changed our understanding of chaos

**原文标题**: A 1955 Los Alamos computer experiment changed our understanding of chaos

**原文链接**: [https://www.lanl.gov/media/publications/1663/science-of-unpredictability](https://www.lanl.gov/media/publications/1663/science-of-unpredictability)

生成摘要时出错

---

## 80. Oura says it gets government demands for user data

**原文标题**: Oura says it gets government demands for user data

**原文链接**: [https://this.weekinsecurity.com/oura-says-it-gets-government-demands-for-user-data-will-it-share-how-many/](https://this.weekinsecurity.com/oura-says-it-gets-government-demands-for-user-data-will-it-share-how-many/)

生成摘要时出错

---

## 81. Solving the “Zork” Mystery

**原文标题**: Solving the “Zork” Mystery

**原文链接**: [https://www.dpolakovic.space/blogs/zork-part2](https://www.dpolakovic.space/blogs/zork-part2)

生成摘要时出错

---

## 82. Shipping a laptop to a refugee camp in Uganda

**原文标题**: Shipping a laptop to a refugee camp in Uganda

**原文链接**: [https://notesbylex.com/shipping-a-laptop-to-a-refugee-camp-in-uganda](https://notesbylex.com/shipping-a-laptop-to-a-refugee-camp-in-uganda)

生成摘要时出错

---

## 83. You can no longer Google the word 'disregard'

**原文标题**: You can no longer Google the word 'disregard'

**原文链接**: [https://techcrunch.com/2026/05/22/you-can-no-longer-google-the-word-disregard/](https://techcrunch.com/2026/05/22/you-can-no-longer-google-the-word-disregard/)

生成摘要时出错

---

## 84. ArcBrush – Node-based 2D image editor

**原文标题**: ArcBrush – Node-based 2D image editor

**原文链接**: [https://arcbrush.com/](https://arcbrush.com/)

生成摘要时出错

---

## 85. Limerick

**原文标题**: Limerick

**原文链接**: [https://www.worldwidewords.org/surprise.html](https://www.worldwidewords.org/surprise.html)

生成摘要时出错

---

## 86. Lisp in Vim (2019)

**原文标题**: Lisp in Vim (2019)

**原文链接**: [https://susam.net/lisp-in-vim.html](https://susam.net/lisp-in-vim.html)

生成摘要时出错

---

## 87. Texas woman arrested for Facebook post about town water quality

**原文标题**: Texas woman arrested for Facebook post about town water quality

**原文链接**: [https://reclaimthenet.org/texas-woman-arrested-for-facebook-post-about-town-water-quality](https://reclaimthenet.org/texas-woman-arrested-for-facebook-post-about-town-water-quality)

生成摘要时出错

---

## 88. The Worlds Left to Conquer

**原文标题**: The Worlds Left to Conquer

**原文链接**: [https://ludic.mataroa.blog/blog/the-worlds-left-to-conquer/](https://ludic.mataroa.blog/blog/the-worlds-left-to-conquer/)

生成摘要时出错

---

## 89. sp.h: Fixing C by giving it a high quality, ultra portable standard library

**原文标题**: sp.h: Fixing C by giving it a high quality, ultra portable standard library

**原文链接**: [https://spader.zone/sp/](https://spader.zone/sp/)

生成摘要时出错

---

## 90. Microsoft starts canceling Claude Code licenses

**原文标题**: Microsoft starts canceling Claude Code licenses

**原文链接**: [https://www.theverge.com/tech/930447/microsoft-claude-code-discontinued-notepad](https://www.theverge.com/tech/930447/microsoft-claude-code-discontinued-notepad)

生成摘要时出错

---

## 91. Microsoft starts canceling Claude Code licenses

**原文标题**: Microsoft starts canceling Claude Code licenses

**原文链接**: [https://www.theverge.com/tech/930447/microsoft-claude-code-discontinued-notepad](https://www.theverge.com/tech/930447/microsoft-claude-code-discontinued-notepad)

生成摘要时出错

---

## 92. Byrne's Euclid

**原文标题**: Byrne's Euclid

**原文链接**: [https://www.c82.net/euclid/](https://www.c82.net/euclid/)

生成摘要时出错

---

## 93. Revised^7 Report on Scheme, Large: Procedural Fascicle Draft is now public

**原文标题**: Revised^7 Report on Scheme, Large: Procedural Fascicle Draft is now public

**原文链接**: [https://r7rs.org/large/fascicles/proc/](https://r7rs.org/large/fascicles/proc/)

生成摘要时出错

---

## 94. Earliest Uses of Various Mathematical Symbols

**原文标题**: Earliest Uses of Various Mathematical Symbols

**原文链接**: [https://mathshistory.st-andrews.ac.uk/Miller/mathsym/](https://mathshistory.st-andrews.ac.uk/Miller/mathsym/)

生成摘要时出错

---

## 95. Local LLMs perform better when you teach them to ask before they answer

**原文标题**: Local LLMs perform better when you teach them to ask before they answer

**原文链接**: [https://www.xda-developers.com/local-llm-clarifying-questions-system-prompt/](https://www.xda-developers.com/local-llm-clarifying-questions-system-prompt/)

生成摘要时出错

---

## 96. Fast Factorial Algorithms

**原文标题**: Fast Factorial Algorithms

**原文链接**: [http://www.luschny.de/math/factorial/FastFactorialFunctions.htm](http://www.luschny.de/math/factorial/FastFactorialFunctions.htm)

生成摘要时出错

---

## 97. The FBI Wants 'Near Real-Time' Access to US License Plate Readers

**原文标题**: The FBI Wants 'Near Real-Time' Access to US License Plate Readers

**原文链接**: [https://www.wired.com/story/security-news-this-week-fbi-license-plate-reader-real-time-access/](https://www.wired.com/story/security-news-this-week-fbi-license-plate-reader-real-time-access/)

生成摘要时出错

---

## 98. Launch HN: Superset (YC P26) – IDE for the agents era

**原文标题**: Launch HN: Superset (YC P26) – IDE for the agents era

**原文链接**: [https://github.com/superset-sh/superset](https://github.com/superset-sh/superset)

生成摘要时出错

---

## 99. Rubish: A Unix shell written in pure Ruby

**原文标题**: Rubish: A Unix shell written in pure Ruby

**原文链接**: [https://github.com/amatsuda/rubish](https://github.com/amatsuda/rubish)

生成摘要时出错

---

## 100. Google Discover's headline rewrites strike again

**原文标题**: Google Discover's headline rewrites strike again

**原文链接**: [https://www.theverge.com/tech/936822/google-discovers-headline-rewrites-strike-again](https://www.theverge.com/tech/936822/google-discovers-headline-rewrites-strike-again)

生成摘要时出错

---

