# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-06-02.md)

*最后自动更新时间: 2025-06-02 17:53:42*
## 1. Show HN: Wireshark 的玩具版

**原文标题**: Show HN: A toy version of Wireshark

**原文链接**: [https://github.com/lixiasky/vanta](https://github.com/lixiasky/vanta)

Vanta：一款轻量级命令行网络行为分析器，由一位本科生作为个人项目创建，以感谢支持国际学生的大学。其旨在提供清晰、结构化和简易的数据包分析，专注于协议层流量和结构化活动提取。

主要特性包括：

*   **协议层解析：** 支持HTTP、DNS和TLS（带有部分指纹识别）。
*   **连接追踪：** 重建双向流量。
*   **行为导出：** 输出JSON格式的摘要。
*   **可移植性：** 单个二进制文件，无外部依赖。

Vanta使用Go语言在MacBook Air M1上开发，旨在用于自定义脚本和最简设置。项目结构包括数据包捕获、流量重组、协议解码、模糊测试（实验性）、行为导出和使用文档（中文）等模块。

作者承认Vanta是Wireshark的“玩具版本”，强调其用心创作。该项目以Apache 2.0许可协议提供，作者欢迎反馈、评论和分享。

---

## 2. 有用不代表有价值。

**原文标题**: If you are useful, it doesn't mean you are valued

**原文链接**: [https://betterthanrandom.substack.com/p/if-you-are-useful-it-doesnt-mean](https://betterthanrandom.substack.com/p/if-you-are-useful-it-doesnt-mean)

无法访问文章链接。

---

## 3. 展示HN：Penny-1.7B 爱尔兰便士期刊风格迁移

**原文标题**: Show HN: Penny-1.7B Irish Penny Journal style transfer

**原文链接**: [https://huggingface.co/dleemiller/Penny-1.7B](https://huggingface.co/dleemiller/Penny-1.7B)

Penny-1.7B是一个拥有17亿参数的语言模型，经过微调以模仿19世纪爱尔兰《便士杂志》（1840年）的写作风格。它利用群体相对策略优化（GRPO）这一强化学习技术，从基础模型SmolLM2-1.7B-Instruct实现这种风格迁移。该模型使用奖励模型进行训练，该奖励模型区分原始IPJ文本和现代翻译，训练了6800个策略步骤。

主要特点包括：

*   **基础模型：** SmolLM2-1.7B-Instruct
*   **微调：** GRPO (RL)
*   **训练数据：** 爱尔兰《便士杂志》（1840年）及其现代翻译。
*   **硬件：** 1x RTX A6000 (48GB)

Penny-1.7B适用于需要维多利亚时代爱尔兰英语的创意写作、教育内容或风格模仿。由于语言陈旧，不建议用于当代事实问答。

该模型存在局限性，包括19世纪文本中可能存在的偏见，并可能产生过时的社会观点。建议用户在使用前审查生成的内容。该模型可以通过Hugging Face Transformers使用提供的代码片段轻松访问。该模型采用Apache 2.0许可。

---

## 4. Show HN: Kan.bn – Trello 的开源替代方案

**原文标题**: Show HN: Kan.bn – An open-source alterative to Trello

**原文链接**: [https://github.com/kanbn/kan](https://github.com/kanbn/kan)

Kan.bn：一款开源项目管理工具，是 Trello 的替代方案。该平台提供看板可见性控制、工作区成员、Trello 导入功能、标签和筛选器、评论协作以及详细的活动日志等功能。即将推出的功能包括模板和集成。

该项目基于 Next.js、tRPC、Better Auth、Tailwind CSS、Drizzle ORM 和 React Email 构建。文章提供了本地开发指导，包括克隆仓库、安装依赖、配置环境变量以及启动开发服务器。

欢迎贡献，项目采用 AGPLv3 许可。用户可以通过电子邮件 (henry@kan.bn) 或加入其 Discord 服务器联系开发者寻求支持。此外，文章还链接到项目的路线图、网站和文档。

---

## 5. Piramidal (YC W24) 招聘资深全栈工程师

**原文标题**: Piramidal (YC W24) Is Hiring a Senior Full Stack Engineer

**原文链接**: [https://www.ycombinator.com/companies/piramidal/jobs/1a1PgE9-senior-full-stack-engineer](https://www.ycombinator.com/companies/piramidal/jobs/1a1PgE9-senior-full-stack-engineer)

Piramidal公司（Y Combinator W24 孵化项目），正在纽约招聘高级全栈工程师，该公司致力于构建用于脑电生理数据的基础模型。 该职位薪资范围为 12 万美元至 25 万美元，要求拥有 3 年以上经验且具备美国公民/签证身份。

该工程师将负责为其旗舰神经数据平台构建和维护基础设施和后端系统，与机器学习工程师和产品团队合作，实施有效的解决方案并迭代模型。

主要要求包括在产品驱动型公司拥有 5 年以上的工程经验，精通 Python 和其他后端语言，熟悉容器化/编排技术（例如 Kubernetes）、关系数据库（例如 Postgres/MySQL）和 Web 技术（例如 JavaScript、React）。 他们强调在动态环境中快速行动的能力。 无需神经科学或数据科学经验。

Piramidal 致力于构建神经解码器，以实现对神经句法的理解和控制，从而促进认知自由并反对心灵的商品化。

面试流程包括初步筛选、技术筛选（居家或现场）以及最终轮，最终轮包括为实时推理架构一个可扩展的系统以及问答环节。该公司由 Dimitris Fotis Sakellariou 和 Kris Pahuja 于 2024 年创立。

---

## 6. 网格边构建

**原文标题**: Mesh Edge Construction

**原文链接**: [https://maxliani.wordpress.com/2025/03/01/mesh-edge-construction/](https://maxliani.wordpress.com/2025/03/01/mesh-edge-construction/)

本文讨论了用于构建多边形网格唯一边的三种算法，重点在于优化效率。文章首先定义了面-顶点网格表示，并区分了“半边”（表示多边形边的有序索引对）和“边”（不考虑多边形方向的唯一线段）。

核心问题是高效地确定网格中唯一边的数量及其索引。作者提出了三种逐步优化的算法：

1.  **映射方法：** 使用 `std::map` 存储边，通过仅插入第一次出现的边来确保唯一性。这种方法的时间复杂度为 O(n log n)，并且存在细粒度内存分配效率低下的问题。

2.  **扁平向量 + 排序：** 创建一个 `EdgeEntry` 结构体（边和原始索引）的向量。然后，对向量进行排序以对重复的边进行分组，使用 `std::unique` 删除重复项（保留第一次遇到的边），并再次按原始索引排序以恢复边的顺序。这种方法的时间复杂度也为 O(n log n)，但由于扁平内存布局和更少的分配而更快。它确实需要更多内存。

文章强调将边定义为排序的索引对对于一致的识别至关重要，并使用联合体来有效地存储和比较边，将其作为 64 位整数。这些算法旨在按照边在网格拓扑结构中遇到的顺序枚举边，以实现一致性和简单的边索引。文章还涉及了边价和邻接的概念，以用于潜在的未来优化。

---

## 7. Arcol以浏览器建模简化建筑设计

**原文标题**: Arcol simplifies building design with browser-based modeling

**原文链接**: [https://www.arcol.io/](https://www.arcol.io/)

Arcol是一个基于浏览器的建筑设计平台，它简化了建筑师、设计师、开发商、总承包商和业主之间的协作，并优化了设计流程。该平台促进了利益相关者之间的实时协作，减少了电子邮件的混乱，并促进了更快、更明智的决策。

Arcol集成了数据和文档以消除信息孤岛，提供强大的数据管理和自动化功能，从而最大限度地减少繁琐的任务。实时指标和可施工设计等功能支持数据驱动的决策和高效的设计迭代，而演示就绪的图板则可自动生成文档。该平台的目标是促进早期协作，避免在项目生命周期后期出现代价高昂的变更。

一些客户评价突显了Arcol的积极影响。slant/is、Corgan、GWWO Architects和THW Design等公司都赞扬其易用性、改善沟通的能力、提高效率以及简化可行性研究的能力。CDH、GWWO和THW Design的客户成功案例进一步强化了其价值。Arcol通过提供满足其特定需求的工具，来满足建筑师和设计师、开发商、总承包商和业主的需求。该平台允许团队设计复杂的建筑物和楼层平面图，并提供更快的客户体验。

---

## 8. 战争与荒野：英国士兵在革命时期的美国

**原文标题**: War and Wilderness: British Soldiers in Revolutionary America

**原文链接**: [https://www.historytoday.com/archive/feature/war-and-wilderness-british-soldiers-revolutionary-america](https://www.historytoday.com/archive/feature/war-and-wilderness-british-soldiers-revolutionary-america)

沃恩·斯克里布纳的《战争与荒野：美国独立战争中的英国士兵》探讨了美国环境对独立战争（1775-1783）期间英国和黑森士兵的有害影响。除了战斗之外，这些欧洲军队还面临着一个充满敌意的自然世界，严重影响了他们的身心健康。

文章着重强调了具体的环境挑战，主要集中在美国景观中的动植物。广阔的沼泽地，尤其是在南方战区，带来了巨大的困难。士兵们遇到了黑水、化脓的泥浆、令人窒息的炎热和危险的野生动物，包括鳄鱼。弗朗西斯·马里昂（绰号“沼泽狐狸”）等人物利用这些环境对英国人发动游击战。

鳄鱼构成了持续的威胁，引发了恐惧，并迫使士兵采取预防措施，例如生起大火。蚊子是另一个长期存在的问题，传播疟疾和黄热病等疾病，这些疾病比战斗更致命。这些疾病大量削减了英军的力量，尤其是在约克镇战役中，疟疾极大地削弱了康沃利斯率领的军队。

由霍雷肖·纳尔逊率领的圣胡安远征进一步说明了这些挑战。当他们穿越中美洲“蚊子海岸”的雨林时，纳尔逊和他的士兵与压迫性的环境作斗争，遇到了各种陌生而危险的生物。恶劣的地形、携带疾病的昆虫和危险的野生动物，共同造成了英国士兵在美国独立战争中所面临的整体痛苦和挑战。

---

## 9. 无人问津时如何发帖

**原文标题**: How to post when no one is reading

**原文链接**: [https://www.jeetmehta.com/posts/thrive-in-obscurity](https://www.jeetmehta.com/posts/thrive-in-obscurity)

本文探讨了在无人关注时创作内容的常见困境，并认为这段“默默无闻”的时期是通往创作精通的关键一步。文章强调，成功往往需要多年的持续努力、实践，甚至“失败的表演”，突出了许多创作者在获得认可之前，默默耕耘了很长时间的现实。

作者不鼓励创作者仅仅追求外部认可，如赞扬、粉丝或名声，因为这会导致倦怠。相反，作者提供了三个维持动力的框架：

1.  **做你喜欢的事，有时世界会认同：** 受迈克·波斯纳的经历启发，作者建议专注于创作能引起个人共鸣的内容，而不是追逐潮流或感知到的受众偏好。这种方法可以培养真正的乐趣，并提高作品的质量。

2.  **把自己推出去：** 创作你喜欢的东西会吸引志同道合的追随者，并确保即使观众很少或不存在，内容对创作者来说仍然是有吸引力的。

3.  **建立你的“狂看银行”：** 将早期未被赏识的内容视为对“狂看银行”的投资有助于保持动力。这些内容对于未来想要探索创作者全部作品的粉丝来说将变得有价值。这些早期的作品在创作时没有获得观看，但后来作为档案获得了观看。

最终，本文鼓励创作者坚持不懈，将最初的默默无闻时期视为构建可持续且令人满意的创作实践的必要阶段。

---

## 10. 智能代理技术：芝麻开门！（1993）

**原文标题**: Intelligent Agent Technology: Open Sesame! (1993)

**原文链接**: [https://blog.gingerbeardman.com/2025/05/31/intelligent-agent-technology-open-sesame-1993/](https://blog.gingerbeardman.com/2025/05/31/intelligent-agent-technology-open-sesame-1993/)

本文讲述了作者长期以来寻找一款名为“Open Sesame!”的 Macintosh 应用程序的历程，这是一款 1993 年开创性的智能软件助手。多年来，作者一直记得看过该应用程序的演示，该应用程序旨在学习和自动化重复性任务，但一直难以找到它的名称或任何相关信息。经过多次使用传统搜索引擎的失败尝试后，作者最终通过使用人工智能，特别是 Gemini，成功地识别了该应用程序并提供了相关的参考文献。

本文重点介绍了 Open Sesame! 的核心功能：观察用户行为，学习重复模式，并提供自动化这些任务的功能。作者发现具有讽刺意味的是，在 2025 年，人工智能帮助发现了关于一款构建于 1993 年机器学习概念之上的应用程序的信息。作者链接到了 Macintosh Garden 网站上 Open Sesame! 1.1 的下载链接，并提供了来自 MacWorld 和 NASA 的关于该应用程序及其技术的进一步阅读材料列表。本文强调了该应用程序作为早期智能代理技术尝试之一的历史地位。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 2 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 3 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 4 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 5 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 6 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 7 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 8 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 9 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 10 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 11 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 12 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 13 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 14 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 15 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 16 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 17 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 18 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 19 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 20 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 21 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 22 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 23 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 24 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 25 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 26 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 27 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 28 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 29 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 30 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 31 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 32 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 33 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 34 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 35 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 36 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 37 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 38 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 39 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 40 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 41 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 42 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 43 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 44 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 45 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 46 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 47 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 48 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 49 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 50 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 51 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 52 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 53 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 54 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 55 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 56 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 57 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 58 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 59 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 60 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 61 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 62 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 63 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 64 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 65 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 66 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 67 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 68 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 69 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 70 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 71 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 72 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 73 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 74 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 75 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
