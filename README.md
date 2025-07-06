# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-07-06.md)

*最后自动更新时间: 2025-07-06 17:47:18*
## 1. 使用 DNS 获取国际空间站位置

**原文标题**: Get the location of the ISS using DNS

**原文链接**: [https://shkspr.mobi/blog/2025/07/get-the-location-of-the-iss-using-dns/](https://shkspr.mobi/blog/2025/07/get-the-location-of-the-iss-using-dns/)

本文详细介绍了一个奇特的项目，该项目使用 DNS LOC 记录来追踪国际空间站 (ISS) 的大致位置。作者利用 RFC 1876 中定义的实验性 DNS LOC 记录类型来存储国际空间站的纬度、经度和海拔。

该项目使用 N2YO API，该 API 提供 JSON 格式的国际空间站位置数据。然后，作者转换这些数据，特别是将纬度/经度从十进制转换为度、分、秒，并将海拔从千米转换为米，以适应 LOC 记录格式。

更新后的位置存储在域名 `where-is-the-iss.dedyn.io` 的 LOC 记录中，可以使用 Linux 和 macOS 上的 `dig` 命令查询。作者使用 deSEC DNS 提供商，因为他们拥有允许更新 LOC 记录的 API。初始记录通过 POST 请求创建，然后通过 PATCH 请求发送更新。生存时间 (TTL) 设置为 900 秒，每 15 分钟更新一次，以保持在 API 限制范围内。

本文重点介绍了 DNS 在典型域名解析之外的非常规用途，展示了它存储其他类型数据的能力。作者还建议可以使用 DNS TXT 记录作为分发静态或不经常更新的数据的一种手段。该项目作为 DNS 技术多种应用的概念验证。

---

## 2. 函数是向量 (2023)

**原文标题**: Functions Are Vectors (2023)

**原文链接**: [https://thenumb.at/Functions-are-Vectors/](https://thenumb.at/Functions-are-Vectors/)

本文论证了函数可以被视为无限维向量，从而可以将线性代数应用于各种问题。文章首先强调了向量空间的抽象本质，以及向量如何从通常被视为数字列表的形式，推广到包含诸如复数、图循环和幻方等实体。然后，作者探讨了将这一概念扩展到函数，最初是可数无限个索引，然后是不可数无限个索引，将实数映射到值。这使得人们意识到，在这种背景下，函数*就是*一个向量。

文章随后通过概述一个函数向量空间来形式化这一概念，使用从ℝ到ℝ的实函数，并为函数定义标量乘法和向量加法。文章提供了证明，以表明这些定义满足必要的向量空间公理。

作者进一步将此与标准基联系起来，将坐标轴的思想扩展到在特定索引处为1，在其他地方为0的函数。最后，文章介绍了线性算子，类似于矩阵，并展示了这些算子如何变换函数。微分作为一种线性运算，被用作多项式子空间的一个例子，展示了微分如何作为线性变换起作用。

---

## 3. 汉娜·开罗解决了溝畑-竹内猜想。

**原文标题**: Hannah Cairo has solved the Mizohata-Takeuchi conjecture

**原文链接**: [https://english.elpais.com/science-tech/2025-07-01/a-17-year-old-teen-refutes-a-mathematical-conjecture-proposed-40-years-ago.html](https://english.elpais.com/science-tech/2025-07-01/a-17-year-old-teen-refutes-a-mathematical-conjecture-proposed-40-years-ago.html)

本文详细介绍了来自巴哈马的 17 岁高中生 Hannah Cairo，在加州大学伯克利分校学习期间，如何解决了调和分析领域几十年来的 Mizohata-Takeuchi 猜想。如果该猜想被证实为真，将验证该领域中其他几个重要的结果。然而，Cairo 在意识到证明该猜想的难度后，利用分形找到了一个反例。她使她的教授张瑞祥信服了她的解决方案。

Mizohata-Takeuchi 猜想属于调和分析范畴，该分析将复杂的函数分解为更简单的成分，例如正弦函数。这个领域被应用于音频/视频压缩和电信等领域。Cairo 解释说，调和分析本质上是用波构建一切，而傅里叶限制理论研究的是用有限的波集可以构建什么。该猜想的重点是使用特定波所产生的由线条构成的形状。

Cairo 在西班牙埃尔埃斯科里亚尔举行的第 12 届调和分析和偏微分方程国际大会上展示了她的发现。她喜欢教学和公开演讲，并将在张瑞祥的指导下，在马里兰大学开始她的博士学位，她也希望在那里建立自己的数学小组。她的旅程始于独立探索高级数学教科书和参加伯克利数学圈夏令营。

---

## 4. GIS过度思考 (2024)

**原文标题**: Overthinking GIS (2024)

**原文链接**: [https://scottsexton.co/post/overthinking_gis/](https://scottsexton.co/post/overthinking_gis/)

过度思考GIS：作者尝试定义和计算土地可用性指标，具体指“坡度不宜建筑”，利用公开GIS数据。因现有GIS工具未能直接提供此指标，作者决定从美国地质调查局(USGS)高程数据中推导得出。

作者下载了高分辨率数字高程模型(DEM)数据，并使用OpenCV的拉普拉斯算子计算高程数据的二阶导数，突显坡度变化率，有效模拟地形线所传达的信息（密集线=陡峭，疏散线=平坦）。

为了量化可用性，作者采用滑动窗口方法，计算每个窗口内的平均拉普拉斯值。基于已知“陡峭”和“平坦”区域设置阈值，生成二元“可用性”地图（陡峭=0.75，平坦=0）。

作者承认该过程过于复杂，本质上是对拉普拉斯数据进行降采样。他们推测直接模糊拉普拉斯数据可能会更有效地产生类似结果。尽管意识到这一点，他们仍然看到其方法的灵活性对于未来参数调整的价值。文章最后提出了“可用性公式”，并暗示将在后续文章中进行改进。

---

## 5. Metriport (YC S22) 正在招聘工程师，以改善医疗保健数据交换。

**原文标题**: Metriport (YC S22) is hiring engineers to improve healthcare data exchange

**原文链接**: [https://www.ycombinator.com/companies/metriport/jobs/Rn2Je8M-software-engineer](https://www.ycombinator.com/companies/metriport/jobs/Rn2Je8M-software-engineer)

Metriport (YC S22)，一个医疗数据智能开源平台，正在招聘软件工程师，以改进医疗数据交换。他们帮助医疗机构实时访问、分析和交换患者数据，与美国主要的医疗IT系统集成，并利用超过3亿人的数据。

他们正在寻找一位具有创业精神、经验丰富（6年以上）、全栈“通才”工程师，位于旧金山湾区，能够构建可扩展的系统，承担责任，并优先交付价值。 医疗保健经验者优先，但非必需。

该职位包括端到端地驱动项目，编写设计文档，审查PR，并参与计划会议和每日站会。 示例项目包括使用LLM进行医疗数据转换，以及构建用于患者病史搜索的OpenSearch集群。

Metriport提供具有竞争力的薪资（12.5万至25万美元），股权（0.10%至0.50%），全额福利，带匹配的401(k)计划，灵活的工作安排以及无限制的PTO。 他们的技术栈包括Node.js、React、PostgreSQL、DynamoDB、HAPI FHIR和AWS。

面试流程包括初步电话沟通、居家编程挑战、技术和文化面试，以及与创始人进行现场会面。 Metriport强调紧密的、高性能的、以工程为主的团队，具有扁平的结构和高度的自主性。 他们是一家资金充足、年经常性收入达数百万美元的公司，拥有80多家客户。

---

## 6. 影响可用性的隐藏界面控件

**原文标题**: Hidden interface controls that affect usability

**原文链接**: [https://interactions.acm.org/archive/view/july-august-2025/stop-hiding-my-controls-hidden-interface-controls-are-affecting-usability](https://interactions.acm.org/archive/view/july-august-2025/stop-hiding-my-controls-hidden-interface-controls-are-affecting-usability)

Philip Kortum 的文章《别再隐藏我的控件：隐藏式界面控件正在影响可用性》认为，现代界面越来越依赖于“隐藏式控件”，要求用户具备特定的知识（“头脑中的知识”）才能执行基本的任务，这是一种倒退，背离了早期图形用户界面中下拉菜单所倡导的、用户友好的“世界中的知识”原则。

作者用 iPhone 隐藏的闪光灯控制、隐藏在神秘按钮组合后的汽车功能以及 Apple CarPlay 的导航界面（其中基本功能被隐藏，直到触摸屏幕特定区域）等例子来说明这一点。需要按住按钮等操作的时间控制进一步加剧了这个问题。即使是专业人士也受到了影响，统计学家由于认为菜单驱动的统计软件的可用性下降，而转而使用命令行界面。

Kortum 将这种趋势归因于功能的激增和对美学极简设计的渴望，他认为，对于设计师来说，过度编码现有控件或完全隐藏它们，比为所有状态创建可见的、持久的控件更容易。他将此与任务关键型系统进行对比，后者优先考虑可见且持久的控件以便立即访问。

作者最后倡导回归到可发现的界面，用户无需事先了解即可轻松理解和访问系统的功能。目标应该是为每个人提供可用性，而不仅仅是那些通过外部来源发现隐藏功能的人。

---

## 7. 本地优先软件 (2019)

**原文标题**: Local-first software (2019)

**原文链接**: [https://www.inkandswitch.com/essay/local-first/](https://www.inkandswitch.com/essay/local-first/)

本文倡导“本地优先软件”，这是一种应用设计范式的转变，它优先考虑本地数据存储和所有权，同时保留基于云的协作的优势。作者认为，虽然云应用提供了无缝协作和可访问性，但它们牺牲了用户对其数据的所有权和控制权，使用户容易受到服务中断、关闭以及定价或功能变更的影响。

本地优先软件旨在通过将主要数据副本保存在用户设备上，结合“老式”本地应用和云应用的优点。 这使得：

*   **速度和响应性：** 消除服务器往返造成的延迟，提供近乎即时的反馈。
*   **跨设备同步：** 使用后台同步来保持数据在多个设备上的一致性。
*   **离线功能：** 即使没有互联网连接，也允许用户不间断地工作。
*   **无缝协作：** 通过无冲突复制数据类型（CRDT）等技术，支持与云应用相当的实时协作。
*   **数据长期性：** 通过在本地存储数据和使用数据所需的软件，确保数据的长期可访问性。
*   **增强的安全性和隐私：** 通过最小化集中式数据存储来降低数据泄露的风险。

本文概述了本地优先软件的七个理想，倡导一个用户拥有对其数据的完全所有权和控制权，同时又不牺牲现代应用的便利性和协作能力的未来。

---

## 8. 使用CGI-bin每天处理2亿次请求

**原文标题**: Serving 200M requests per day with a CGI-bin

**原文链接**: [https://simonwillison.net/2025/Jul/5/cgi-bin-performance/](https://simonwillison.net/2025/Jul/5/cgi-bin-performance/)

尽管在 20 世纪 90 年代末人们普遍认为 CGI（通用网关接口）效率低下，但本文探讨了在 2025 年使用 CGI 处理 Web 请求的令人惊讶的可行性。Jake Gold 在 16 线程 AMD 3700X 上测试了一个 Go + SQLite CGI 程序，发现它每天能够处理超过 2 亿个请求（每秒 2400 多个请求）。

作者回顾了 CGI 如何因为每个请求启动一个新进程而被迅速认为效率低下，从而导致了 PHP 和 FastCGI 等技术的发展。 然而，硬件方面的显著进步，特别是 CPU 速度和核心数量的增加，再加上使用像 Go 和 Rust 这样更快的语言，使得 CGI 成为一个更可行的选择。 他指出，由于 CGI 程序基于进程的架构，因此擅长利用多个 CPU 核心。

作者强调，他并不一定提倡广泛采用 CGI，而是强调它不再像过去那样不切实际。 本文建议使用现代工具和硬件重新审视旧技术，并认识到过去的性能瓶颈可能不再具有相关性。

---

## 9. 玩具/延迟：抖动监控器

**原文标题**: Toys/Lag: Jerk Monitor

**原文链接**: [https://nothing.pcarrier.com/posts/lag/](https://nothing.pcarrier.com/posts/lag/)

作者升级到240 Hz显示器后对延迟非常敏感，在更换无线鼠标接收器USB端口后，注意到了延迟。由于找不到现有工具来分析这些细微的延迟，他们创建了一个自定义工具，地址为 found.as/l，名为“Jerk Monitor”。该工具测量浏览器渲染帧和报告的指针移动之间的延迟，并详细说明了指针事件批处理和偏移。为了为该工具启用高精度计时器，作者在其 xmit.toml 配置中添加了特定的跨域标头。该工具证实了观察到的 USB 端口延迟问题，促使作者避免使用该端口。此外，他们还发现了鼠标 8 kHz 轮询率的好处，因为即使在高 DPI 和快速鼠标移动的情况下，某些帧也可能会错过指针更新。本质上，作者构建了一个工具来量化和解决影响其计算体验的细微延迟问题。

---

## 10. 在Notebook中使用人类反馈强化学习

**原文标题**: Reinforcement Learning from Human Feedback (RLHF) in Notebooks

**原文链接**: [https://github.com/ash80/RLHF_in_notebooks](https://github.com/ash80/RLHF_in_notebooks)

本仓库提供了一个使用notebook实现的基于人类反馈的强化学习(RLHF)的实践方案，与YouTube视频中详述的方法相呼应。RLHF通过三个步骤将大型语言模型(LLMs)与人类偏好对齐：监督式微调(SFT)、奖励模型训练，以及通过近端策略优化(PPO)进行强化学习。

该实现专注于微调GPT-2，使其使用stanfordnlp/sst2电影评论数据集生成表达积极情感的句子。 该过程涉及三个notebook:

1.  **1-SFT.ipynb:** 在数据集上微调GPT-2以生成相似的句子。 生成的模型将保存为SFT模型。
2.  **2-RM Training.ipynb:** 通过向GPT-2添加奖励头来创建奖励模型。 该模型经过训练以预测句子的情感（正面/负面）。
3.  **3-RLHF.ipynb:** 实施PPO以优化SFT模型，鼓励其生成从奖励模型获得高奖励（积极情感得分）的句子。

要开始使用，用户需要一个Hugging Face访问令牌，并且可以在本地将其设置为环境变量，或在Google Colab Secrets中设置。 应按顺序运行notebook，以实现GPT-2生成积极情感句子的预期结果。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 2 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 3 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 4 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 5 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 6 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 7 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 8 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 9 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 10 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 11 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 12 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 13 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 14 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 15 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 16 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 17 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 18 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 19 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 20 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 21 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 22 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 23 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 24 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 25 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 26 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 27 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 28 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 29 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 30 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 31 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 32 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 33 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 34 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 35 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 36 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 37 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 38 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 39 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 40 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 41 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 42 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 43 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 44 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 45 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 46 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 47 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 48 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 49 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 50 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 51 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 52 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 53 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 54 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 55 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 56 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 57 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 58 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 59 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 60 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 61 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 62 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 63 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 64 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 65 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 66 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 67 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 68 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 69 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 70 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 71 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 72 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 73 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 74 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 75 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 76 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 77 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 78 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 79 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 80 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 81 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 82 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 83 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 84 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 85 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 86 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 87 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 88 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 89 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 90 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 91 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 92 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 93 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 94 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 95 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 96 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 97 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 98 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 99 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 100 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 101 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 102 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 103 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 104 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 105 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 106 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 107 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 108 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 109 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
