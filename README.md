# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-05-23.md)

*最后自动更新时间: 2025-05-23 17:50:11*
## 1. VS Code 中的 PostgreSQL IDE

**原文标题**: PostgreSQL IDE in VS Code

**原文链接**: [https://techcommunity.microsoft.com/blog/adforpostgresql/announcing-a-new-ide-for-postgresql-in-vs-code-from-microsoft/4414648](https://techcommunity.microsoft.com/blog/adforpostgresql/announcing-a-new-ide-for-postgresql-in-vs-code-from-microsoft/4414648)

此文宣布 Visual Studio Code (VS Code) 适用的全新 PostgreSQL 扩展的公开预览版，该扩展旨在简化 PostgreSQL 数据库管理和开发工作流程。它通过在 VS Code 中集成数据库工具和 @pgsql GitHub Copilot 代理，解决了开发人员面临的挑战，例如任务切换和调试时间。

主要功能包括：

*   **模式可视化：** 通过右键单击上下文菜单轻松可视化。
*   **数据库感知型 GitHub Copilot：** 利用 AI 辅助进行查询、模式优化和 SQL 操作，提供实时指导并提高代码质量。提供一个包含“重写查询”和“解释查询”等选项的上下文菜单。
*   **GitHub Copilot 聊天代理模式：** 一种智能助手，可以执行多阶段任务、编写和调试代码、简化应用程序原型设计以及优化模式。
*   **简化连接管理：** 轻松连接到本地和云托管的 PostgreSQL 实例，包括 Azure Database for PostgreSQL，并集成 Entra ID。
*   **使用 Entra ID 的无密码身份验证：** 通过自动令牌刷新实现简化的安全身份验证。
*   **数据库资源管理器：** 数据库对象的结构化视图，用于创建、修改和删除。
*   **查询历史记录：** 快速访问以前运行的查询。
*   **上下文感知型 IntelliSense：** 自动完成和语法突出显示，以提高查询可读性。

该扩展旨在提高生产力、简化入门流程、通过 Entra ID 提高安全性、提供全面的工具集以及提供与 Azure Database for PostgreSQL 的无缝云集成。文中包含安装扩展程序和启用 PostgreSQL GitHub Copilot 聊天的说明。作者鼓励用户提供反馈以改进扩展程序。

---

## 2. 找到你的同伴

**原文标题**: Find Your People

**原文链接**: [https://foundersatwork.posthaven.com/find-your-people](https://foundersatwork.posthaven.com/find-your-people)

在巴克内尔大学的毕业典礼上，演讲者面向毕业生，特别是那些对未来感到迷茫的人们发表讲话。他认为毕业后，生活将从预设的“轨道”转变为更加开放的景象，既充满兴奋，又充满恐惧。他鼓励毕业生们积极地掌控自己的生活，而不是被动地漂流。

他建议那些不确定的人“重塑”自我，摆脱过去基于学业成绩对自身能力的认知。他强调，他们有能力采纳新的品质，比如好奇心和责任感，而不会因为过去的表现而受到评判。

为了应对大量职业选择带来的迷茫，演讲者建议使用一个“技巧”：与有趣的人建立联系。他强调与各个领域的人交谈，发现什么能激发他们的兴趣的重要性。他还建议离开那些与自己不合拍的工作场所。

最后，他强调需要培养对拒绝的免疫力。雄心勃勃的想法往往会受到怀疑，坚持至关重要。他分享了他与Y Combinator的经历，最初被认为是笑话，以说明看似“平庸”的想法也可能具有突破性。他最后重申了积极选择道路和向有趣的人学习的重要性，最终鼓励毕业生们拥抱雄心，忽略反对者。

---

## 3. 超越语义：无理性中间令牌的不可思议的有效性

**原文标题**: Beyond Semantics: Unreasonable Effectiveness of Reasonless Intermediate Tokens

**原文链接**: [https://arxiv.org/abs/2505.13775](https://arxiv.org/abs/2505.13775)

这篇arXiv论文《超越语义：无理性中间令牌的出乎意料的有效性》挑战了一个被广泛接受的观点，即大型语言模型（LLMs）中思维链（CoT）提示的成功源于中间“思考”令牌的有意义的语义。作者认为，这些通常被解释为推理证据的令牌，可能不像之前认为的那么关键。

为了调查这一点，他们训练了转换器模型，使用了来自A*搜索的形式上可验证的推理轨迹和解决方案，确保中间步骤和最终输出与形式求解器对齐。然后，他们系统地评估了不仅解决方案的准确性，还评估了这些中间轨迹的正确性。

关键发现是，用准确的轨迹训练的模型仍然可以产生不正确的推理步骤，同时得出正确的解决方案。更令人惊讶的是，作者发现，用与特定问题无关的嘈杂、损坏的轨迹训练的模型，表现与用正确的轨迹训练的模型相当，有时甚至更好。这表明轨迹准确性和解决方案准确性之间的联系并不紧密，甚至使用“无理性”的中间令牌可能会提高泛化能力。

论文的结论是，告诫人们不要将中间令牌拟人化，或者过度解读它们为人类般的或算法推理的证据，尽管它们通常看起来格式正确。结果表明，CoT的有效性可能更多地在于中间令牌提供的结构或支架，而不是它们特定的语义内容。

---

## 4. 凯撒之息

**原文标题**: Caesar's Last Breath

**原文链接**: [https://charliesabino.com/caesars-last-breath/](https://charliesabino.com/caesars-last-breath/)

本文探讨了费米估算的概念，并以“凯撒的最后一口气”这个思想实验为例，展示了如何通过简单的计算来估算看似不可能的数量。核心问题是：我们每次呼吸会吸入多少凯撒最后一口气中的分子？

文章认为，由于分子的扩散和保存，我们每次呼吸都包含着曾经生活过的所有人的呼吸的一部分。为了估算这一点，文章将问题分解为计算地球大气层的体积和单次呼吸的体积。

文章使用锚定值（地球半径、大气层厚度、大气密度和空气分子量）估计大气层的体积约为 5 x 10^18 立方米，单次呼吸的体积为 5 x 10^-4 立方米。这得出一个结论：凯撒的最后一口气占据了大气层的 1/10^22。

接下来，文章估计单次呼吸中的分子数量约为 10^22。将此数字乘以先前计算的比例，得出的结论是，我们每次呼吸大约会吸入凯撒最后一口气中的一个分子。

文章最后强调了费米估算的强大之处及其在现实世界中的适用性。它建议了一些资源，用于进一步练习和探索该技术，尤其是在软件工程的背景下。

---

## 5. 米制起源于法国大革命

**原文标题**: The metre originated in the French Revolution

**原文链接**: [https://www.abc.net.au/news/science/2025-05-20/metre-treaty-anniversary-metric-system-measurement-metrology/105302024](https://www.abc.net.au/news/science/2025-05-20/metre-treaty-anniversary-metric-system-measurement-metrology/105302024)

本文探讨了米的单位历史和演变，从其在法国的革命性起源到目前基于光速的定义。米最初在法国大革命期间被构想为一种与自然相关的通用测量单位，定义为从北极经巴黎到赤道距离的千万分之一。

1875年的《米制公约》（米制条约）在国际上标准化了米和千克，并建立了国际计量局。早期的米物理表示，如铂金棒，后来被基于氪-86发出的光波长的定义所取代。

原子钟和光速测量技术的进步导致了米目前的定义，自1983年以来，米被定义为光在真空中1/299,792,458秒内传播的距离。这种精确的定义可以进行精确的测量，例如确定地球和月球之间的距离。

虽然以米为基础的公制已被全球广泛采用，但本文强调了不同国家采用速度的差异。即使是《米制条约》的原始签署国美国，尽管在法律上承认公制，但在日常生活中仍然主要使用英制单位。文章还指出了即使在使用公制单位的国家内部，测量也存在不一致性，例如澳大利亚的汤匙测量与其他国家/地区的不同。

---

## 6. 进入隧道：风洞的秘密生活

**原文标题**: Into The Tunnel: The secret life of wind tunnels

**原文链接**: [https://jordanwtaylor2.substack.com/p/into-the-tunnel](https://jordanwtaylor2.substack.com/p/into-the-tunnel)

无法访问文章链接。

---

## 7. Show HN: Samchika – 用于快速多线程文件处理的 Java 库

**原文标题**: Show HN: Samchika – A Java Library for Fast, Multithreaded File Processing

**原文链接**: [https://github.com/MayankPratap/Samchika](https://github.com/MayankPratap/Samchika)

Samchika是一个Java库，专为快速、多线程的文件处理而设计，通过并行处理实现对大型文件的高效处理。其特性包括简单的API、可选的运行时统计以及适用于CPU密集型任务，如日志分析、ETL操作和数据转换。

该库的核心功能围绕`SmartFileProcessor`展开，它允许用户定义输入和输出路径、批处理大小以及用于自定义逻辑的行处理器。通过Maven或Gradle可以轻松集成。

针对标准`BufferedReader`实现的性能基准测试表明，尤其是在多核系统上，性能有显著提升，处理速度最多可提高70%。在提供更高速度的同时，即使对于大型文件，内存使用量也保持在可控范围内。

Samchika采用MIT许可证，鼓励免费使用和修改。该项目的灵感来自一个JavaScript库和一个LinkedIn讨论，其中强调了大型文件处理中的挑战。开发者感谢Shubham Maurya提供的灵感。

---

## 8. 史莱姆 (2021)

**原文标题**: Slime (2021)

**原文链接**: [https://granta.com/slime/](https://granta.com/slime/)

苏珊娜·韦德利希的《粘液》深入探讨了粘液在我们世界中出人意料的深刻作用，挑战了我们对这种常常被忽视的物质的普遍厌恶。这本书以作者在亨特博物馆寻找一瓶特定的“原始粘液”开始，这个样本最终驳斥了粘液是生命起源的理论。

韦德利希认为，粘液，一种存在于固态和液态之间的物质，不仅仅是一种令人作呕的副产品，而是生命的关键组成部分。它在自然界中无处不在，为生物体提供从结构支撑到防御的各种功能。许多熟悉的物质，如粘液和海洋雪，实际上都是粘液的形式。粘液充当生态系统的水泥，并在我们自己的身体中发挥着至关重要的作用，保护我们免受病原体的侵害并维持基本功能。

这本书探讨了粘液的历史观念，从其在古埃及受人尊敬的地位到其在现代社会中与怪物和厌恶的联系。它还考察了对粘液的科学研究，包括原始粘液作为生命起源的被驳斥的理论。尽管存在负面含义，科学家们现在正在研究粘液的独特特性，用于机器人技术和医学等各个领域。韦德利希警告说，气候变化等环境危机威胁着基于粘液的生态系统，但也可能迎来粘液重新占据主导地位的新时代。最终，这本书旨在颠覆我们对粘液的负面认知，揭示它是生命、健康和环境的重要元素。

---

## 9. 为高质量类型错误设计类型推断

**原文标题**: Designing type inference for high quality type errors

**原文链接**: [https://blog.polybdenum.com/2025/02/14/designing-type-inference-for-high-quality-type-errors.html](https://blog.polybdenum.com/2025/02/14/designing-type-inference-for-high-quality-type-errors.html)

本文探讨了如何设计能够提供高质量错误信息的类型推断系统，并指出类型推断在这方面声名狼藉的原因是特定的设计选择，而非其固有的局限性。

作者指出了导致不良错误信息的两个主要缺陷：

1.  **猜测和回溯：** 使用临时重载或类似功能的语言会迫使类型检查器在多种可能性之间进行猜测。这可能导致编译时间呈指数级增长，并产生与用户预期代码无关的冗长错误信息。作者认为，类型系统的设计应确保类型检查器永远不必猜测。

2.  **仓促下结论：** 像 OCaml 这样的语言通常会根据它们遇到的第一个类型来报告错误，而不跟踪冲突中涉及的其他类型。这可能导致误导性的错误信息，无法识别类型不匹配的根本原因。作者提供了一个例子，其中 OCaml 错误地将浮点数识别为期望的整数，但没有说明原因或期望的来源。

作者介绍了 PolySubML，一种在设计时充分考虑了良好错误信息的语言。其方法与 OCaml 形成对比，展示了 PolySubML 如何跟踪类型冲突的双方，并提供添加手动类型注释的提示，以缩小错误原因的范围。 最关键的结论是，将错误信息质量作为核心关注点来设计类型系统对于积极的开发者体验至关重要。

---

## 10. 纪念阿拉斯代尔·麦金太尔

**原文标题**: Remembering Alasdair MacIntyre

**原文链接**: [https://www.wordonfire.org/articles/remembering-alasdair-macintyre-1929-2025/](https://www.wordonfire.org/articles/remembering-alasdair-macintyre-1929-2025/)

无法访问文章链接。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 2 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 3 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 4 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 5 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 6 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 7 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 8 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 9 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 10 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 11 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 12 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 13 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 14 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 15 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 16 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 17 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 18 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 19 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 20 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 21 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 22 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 23 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 24 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 25 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 26 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 27 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 28 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 29 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 30 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 31 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 32 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 33 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 34 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 35 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 36 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 37 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 38 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 39 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 40 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 41 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 42 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 43 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 44 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 45 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 46 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 47 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 48 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 49 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 50 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 51 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 52 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 53 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 54 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 55 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 56 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 57 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 58 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 59 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 60 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 61 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 62 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 63 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 64 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 65 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
