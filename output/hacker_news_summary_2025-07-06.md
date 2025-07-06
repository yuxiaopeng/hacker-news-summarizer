# Hacker News 热门文章摘要 (2025-07-06)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 再来一次：Eshell

**原文标题**: Take Two: Eshell

**原文链接**: [http://yummymelon.com/devnull/take-two-eshell.html](http://yummymelon.com/devnull/take-two-eshell.html)

Charles Choi的“再谈Eshell”探讨了他与Emacs中Eshell关系的演变。起初他并未留下深刻印象，但现在发现它是工作流程中不可或缺的一部分，虽然不是直接的Shell替代品。他已经从使用命令行工具进行文件管理和SCM等任务转变为使用Dired和Magit等Emacs模式。

Choi认为，Eshell真正的力量在于掌握Elisp知识，将其转变为一个Elisp REPL，同时也可以作为Shell运行。这允许用户将Shell命令与Elisp函数结合使用，从而促进强大且即兴的工作流程。他将此与更繁琐的Shell语法进行了对比。

一个关键优势是Eshell能够与Emacs缓冲区集成，将它们视为主要数据类型，而不仅仅是文件。他强调Eshell如何用Emacs等效工具（例如，使用Dired进行文件管理，Magit进行SCM）取代常见的Shell工作流程。他还讨论了将`grep`与管道一起使用，警告不要不加选择地在大型文件上使用它，并提倡重定向到缓冲区而不是文件。他指出，目前您无法将输出通过管道传输到Elisp函数，但这可能会改变。

最终，Choi将Eshell视为Elisp/Emacs功能的提示符，为命令行实用程序提供“类似Shell”的体验。他建议学习Elisp以充分利用Eshell的潜力，并强调它不是一个直接替换终端的工具。他建议使用专用终端模拟器进行完全的终端模拟。

---

## 12. 用Claude代码构建Mac应用

**原文标题**: Building a Mac app with Claude code

**原文链接**: [https://www.indragie.com/blog/i-shipped-a-macos-app-built-entirely-by-claude-code](https://www.indragie.com/blog/i-shipped-a-macos-app-built-entirely-by-claude-code)

本文详细介绍了作者在Anthropic的Claude Code（一个专注于自主开发的基于终端的IDE）的帮助下，几乎完全使用该工具构建macOS应用程序“Context”的经验。作者将Claude Code与之前使用Copilot和其他AI驱动的编码工具的经验进行了对比，强调了Claude Code自主处理更复杂任务的能力。

Claude Code擅长理解现有代码、生成新代码和测试、基于编译器和测试失败进行迭代，甚至可以根据屏幕截图或控制台日志修复错误。虽然Claude Code在Swift 5.5版本之前表现良好，但在SwiftUI方面表现出色，使作者能够构建一个可用且设计良好的用户界面。

作者强调了最大化Claude Code效率的关键策略，强调了“上下文工程”而不是传统的提示工程。他介绍了通过向代理提供相关文档和源代码来“启动”代理的概念。详细的规范对于引导模型至关重要，并且提示它在实施之前进行“超思考”并制定计划有助于提高输出质量。

建立用于构建和测试的反馈循环对于Claude Code迭代和改进其代码至关重要。作者总结说，Claude Code极大地加速了开发，使他能够再次发布副项目，并暗示了未来的IDE将以这种类型的交互为中心。

---

## 13. 过度捕捞导致东波罗的海鳕鱼的体型比以往小得多。

**原文标题**: Eastern Baltic cod grow much smaller than they did due to overfishing

**原文链接**: [https://www.smithsonianmag.com/smart-news/these-cod-have-been-shrinking-dramatically-for-decades-now-scientists-say-theyve-solved-the-mystery-180986920/](https://www.smithsonianmag.com/smart-news/these-cod-have-been-shrinking-dramatically-for-decades-now-scientists-say-theyve-solved-the-mystery-180986920/)

东波罗的海过度捕捞导致鳕鱼体型急剧缩小，原因是鱼类基因构成的进化改变。一项发表在《科学进展》上的最新研究表明，数十年来无情的捕捞，特别是对大型鱼类的捕捞，改变了鳕鱼种群的基因库，使其更容易保持较小体型。

历史上，波罗的海鳕鱼可以长到三英尺多长。然而，到2019年，它们的体型减半，体重也大幅下降。虽然污染和温度变化等环境因素可能会产生影响，但研究人员发现，过度捕捞是主要驱动因素，导致与较大体型相关的基因变异变得不那么常见。

科学家分析了1996年至2019年捕捞的鳕鱼的耳石和DNA，揭示了过度捕捞与和更快生长相关的基因减少之间存在明显的相关性。这种由“人类捕捞”驱动的进化转变可能产生持久的影响。遗传多样性的丧失使得鳕鱼更难适应未来的环境变化，恢复可能缓慢甚至不可能。

该研究强调了人类活动驱动进化的速度，并强调了不仅要监测物种的数量，还要监测其基因构成的重要性。

---

## 14. 黑客从我这里偷了什么

**原文标题**: What a Hacker Stole from Me

**原文链接**: [https://mynoise.net/blog.php](https://mynoise.net/blog.php)

myNoise创始人Stéphane的这篇博文详述了最近一次网络攻击未遂事件，有人试图通过重复下载声音文件来压垮服务器。Stéphane反思了创造与破坏之间固有的不平衡，以及破坏行为的令人沮丧，尤其是在最近一次健康事件之后。他将这次经历与对世界现状更广泛的忧郁联系起来，并感叹摧毁事物是如此容易，而建设却需要付出巨大的努力。他分享了一则关于拯救鸽子的暖心轶事，展示了他尽管存在潜在的消极因素，仍致力于积极行动的决心。

虽然黑客没有搞垮服务器，但他们偷走了Stéphane的时间和精力，让他无法创作新的声音。尽管如此，Stéphane重申了他将继续建设积极事物的决心，例如植树、制作声音、帮助动物以及将myNoise作为一个避难所。他表达了希望选择建设的人最终会超过选择破坏的人。

该博客还包括关于myNoise成功迁移到新的私有服务器的更新，强调了来自One.com的Yudhish的杰出支持。Stéphane还谈到了他的美国之行，以及激发新声音灵感的新音景静修，计划整合来自维多利亚瀑布的声音，并鼓励读者订阅电子邮件新闻和使用RSS。最后，他讨论了离开社交媒体。

---

## 15. 1687年7月5日：牛顿解释了你为何不会漂浮

**原文标题**: July 5, 1687: When Newton explained why you don't float away

**原文链接**: [https://multiverseemployeehandbook.com/blog/when-newton-explained-why-you-dont-float-away/](https://multiverseemployeehandbook.com/blog/when-newton-explained-why-you-dont-float-away/)

1687年7月5日，艾萨克·牛顿发表了他开创性的《自然哲学的数学原理》，阐释了运动定律和万有引力定律。这项著作彻底革新了我们对宇宙的理解，阐明了物体为何保持在地面上、行星为何绕轨道运行以及我们为何不会漂浮到太空中。

由于皇家学会资助了一本耗资巨大的鱼类书籍后，资金拮据，这本书的出版几乎未能成行。因彗星而闻名的埃德蒙·哈雷介入并亲自资助了印刷。

牛顿定律在无数应用中发挥了重要作用，从建造桥梁到绘制行星轨道，美国国家航空航天局 (NASA) 至今仍在用它来发射火箭。他的工作为我们理解物体（无论大小）的行为提供了一个框架，为我们提供了一个可预测且稳定的宇宙。

本文庆祝这一科学史上关键时刻的337周年，并肯定了牛顿的持久影响。它还推广了旨在使牛顿物理学易于理解且有趣的“多元宇宙员工手册”播客。

---

## 16. 如何开始学习古英语诗歌

**原文标题**: How to get started with Old English poetry

**原文链接**: [https://www.deadlanguagesociety.com/p/old-english-poetry](https://www.deadlanguagesociety.com/p/old-english-poetry)

科林·戈里的文章《如何入门古英语诗歌》鼓励读者探索除《贝奥武甫》之外，鲜为人知的90%的古英语诗歌。《贝奥武甫》虽有名，但篇幅长、晦涩难懂，且充满学术争论，使其成为一个具有挑战性的入门点。戈里认为，公元700至1066年间创作、主要保存在四份手稿中的古英语诗歌，提供了更容易且同样有价值的体验。

他强调了英雄诗歌之外的四种体裁：哀歌（对失去的冥想）、谜语（通常以会说话的物体为特色）、智慧诗（类似于箴言）和宗教诗（日耳曼语境下的基督教主题）。戈里介绍了五首特定的诗歌，作为易于理解的起点：《马尔顿战役》（英雄）、《漫游者》（哀歌）、《埃克塞特书谜语》（谜语）、《十字架之梦》（宗教）和《迪奥尔》（智慧）。对于每一首诗，他都提供了简要描述、引人入胜的节选，以及对容易获得的翻译的推荐，包括免费在线版（奥菲莉亚·霍斯特特）和印刷版（克雷格·威廉姆森的《古英语诗全集》）。戈里强调了古英语诗歌的新鲜和活力，它避免了后来的中世纪欧洲大陆的影响（韵律、十四行诗、抑扬格五音步）。这篇文章邀请读者去发现一个迷人的世界，那里有流亡者、勇敢的将军和被施了魔法的物体，通过翻译可以很容易地进入这个世界。他还提到一个贝奥武甫读书俱乐部，为那些想要更深入研究的人准备。

---

## 17. 利用遗传算法的像素画生成器

**原文标题**: Show HN: Pixel Art Generator Using Genetic Algorithm

**原文链接**: [https://github.com/Yutarop/ga-pixel-art](https://github.com/Yutarop/ga-pixel-art)

此Show HN帖子展示了一个使用遗传算法实现的像素艺术生成器。该程序通过进化像素艺术来逼近目标图像，并生成进化过程的动画GIF。

该算法将100x100图像中的每个像素表示为一个染色体，该染色体包含红色、绿色和蓝色通道的二进制基因。该算法通过选择（锦标赛选择）、交叉和变异迭代地提高图像质量，试图匹配目标图像。关键参数包括：种群大小为6，迭代次数（代数）为50，变异率为0.05，交叉率为0.8，每个颜色通道的基因长度为8位。该算法还使用精英主义来保留每一代中最好的个体。

要运行该程序，用户需要在`Cargo.toml`依赖项中添加`image`、`rand`和`gif` crates。在运行`cargo run`之前，应将名为“target.png”的目标图像放置在项目目录中。该程序将最终进化的图像输出为“result.png”，动画进化过程输出为“result.gif”，并将用作“target_sample.png”的目标图像副本输出。

---

## 18. 克劳德代码Pro限制？趁你睡觉时破解它

**原文标题**: Claude Code Pro Limit? Hack It While You Sleep

**原文链接**: [https://github.com/terryso/claude-auto-resume](https://github.com/terryso/claude-auto-resume)

本文介绍`claude-auto-resume`，这是一个shell脚本实用工具，旨在自动化恢复因达到使用限制而中断的Claude CLI任务。它允许用户避免手动干预，并无缝地继续工作。

该脚本通过执行`claude -p 'check'`自动检测Claude的使用限制，解析带有时间戳的限制相关消息，计算所需的等待时间，并显示倒计时。一旦限制解除，它会自动恢复之前的会话或启动新的会话，使用`claude --dangerously-skip-permissions -p "<custom-prompt>"`或`claude -c --dangerously-skip-permissions -p "<custom-prompt>"`。

安装方法包括使用Makefile（推荐）、手动复制并更改权限，或直接执行。用法示例涵盖使用自定义提示启动新会话、继续之前的对话以及显示帮助信息。

该脚本需要安装Claude CLI和标准Unix工具。内置错误处理机制，为不同的故障情况提供特定的退出代码。项目结构包括主脚本、Makefile、文档和README.md文件。欢迎通过fork代码库、创建功能分支和提交pull request的方式进行贡献。该项目采用MIT许可证。该脚本的功能依赖于Claude CLI的输出格式，如果该格式发生变化，可能需要更新。

---

## 19. 内向者如何建立人脉

**原文标题**: How to Network as an Introvert

**原文链接**: [https://aginfer.bearblog.dev/how-to-network-as-an-introvert/](https://aginfer.bearblog.dev/how-to-network-as-an-introvert/)

本文提供了一份专为内向者量身定制的人脉拓展指南，强调利用他们自身优势的策略。作者强调活动前做好准备以尽量减少焦虑的重要性：事先吃饭，佩戴一个“话题引发物”来吸引对话，浏览新闻了解时事，并使用六点清单来规划当晚的活动。

进入房间后，重点转移到非语言沟通：停顿一下评估房间情况，保持开放的肢体语言，并运用“延迟温暖”的微笑来展现自信。话题的开端应该超越典型的小范围闲聊，从而激发真诚的参与。与其问“你是做什么的？”，不如问“你大部分时间都在做什么？”。

在对话过程中，积极倾听和记住小细节至关重要。作者建议重复对方的话（“太阳能硬件？”）来鼓励他们详细说明。在适当的时候，分享共同点，但稍微延迟一下，使其感觉更有洞察力。对于主人，提供具体的赞美和小的服务行为。

离开活动和进入一样重要。有意识地用令人难忘的形容词说再见。在24小时内，与你联系过的任何人进行跟进，分享与你谈话相关的内容。记录重要的细节以供将来参考，并在三周后再次联系以巩固关系。 关键要点：内向者有效的人脉拓展在于保持专注，专注倾听，并留下持久而真诚的印象，而不是强迫自己表现出外向的行为。

---

## 20. 晶体管处理器指令集架构板的开发

**原文标题**: Development of a transputer ISA board

**原文链接**: [https://nanochess.org/transputer_board.html](https://nanochess.org/transputer_board.html)

本文详细介绍了作者开发Transputer ISA板卡以运行20世纪90年代遗留软件的历程。在用Javascript创建了一个Transputer模拟器之后，出于好奇和怀旧，作者决定使用现成的TRAM板来构建一个与Inmos B004兼容的物理板。

最初的方法包括设计带有TTL电路的原理图，购买ISA原型板，以及手工布线组件。这产生了一个功能性但嘈杂的板卡，并伴随着一个令人尴尬的反向组装错误。

为了改进设计，作者采用了KiCAD，并创建了原理图和PCB布局。这个过程包括学习KiCAD、设计自定义封装以及克服自动布线器的挑战。创建了多个版本的板卡，每个版本都解决了设计中的错误，如错误的电源线宽度和封装错误配置。

尽管经历了多次迭代和错误，包括短路和错误的组件放置，作者最终成功实现了一个完全功能的Transputer ISA板卡。在纠正了一个反转的错误标志问题后，该板卡成功运行了作者最初的Pascal编译器、光线追踪器，甚至Inmos Occam编译器。

最终的板卡设计，包括原理图和Gerber文件，可在GitHub上找到。作者还提供组装和测试过的板卡出售，但不包括TRAM和C011芯片。本文突出了作者从软件仿真到硬件创建的旅程，展示了复古工程的挑战和乐趣。

---

## 21. 游戏开发两年半

**原文标题**: Two and a Half Years in GameDev

**原文链接**: [https://smyachenkov.com/posts/two-and-half-years-in-gamedev/](https://smyachenkov.com/posts/two-and-half-years-in-gamedev/)

游戏开发行业两年半工作反思：热情、创意与文化冲突

---

## 22. 强行推广不受欢迎的AI功能

**原文标题**: The force-feeding of AI features on an unwilling public

**原文链接**: [https://www.honest-broker.com/p/the-force-feeding-of-ai-on-an-unwilling](https://www.honest-broker.com/p/the-force-feeding-of-ai-on-an-unwilling)

泰德·乔亚的文章《强行喂食不情愿的公众AI》认为，人工智能正被积极地推向那些大多并不需要的消费者，并将其描述为一种“暴政”而非创新。他引用了自己使用微软Copilot和谷歌的AI集成搜索结果的个人经历，作为不想要且无法避免的AI功能的例子。

乔亚强调，只有一小部分人愿意为AI服务付费，导致公司将其与软件和搜索引擎等基本产品捆绑销售。这使他们能够掩盖与AI相关的潜在损失，并人为地夸大其感知价值。他认为这种策略避免了直接的消费者选择，并迫使用户接受AI集成。

他用一家餐厅强迫顾客付费并接受花岗岩石头作为甜点的例子来说明，公司如何在未经消费者同意的情况下添加AI。乔亚批评了日常生活的各个方面缺乏选择，从客户服务到在线零售商，并预测了AI将在医疗保健和法律等关键领域取代人际互动的未来。

这篇文章倡导制定法律，以促进AI的透明度、选择加入选项和责任，并建议将选民倡议和集体诉讼作为潜在的解决方案。最后，乔亚驳斥了美国必须拥抱AI才能超越中国的说法，认为这是一场误入歧途的竞赛，通往一个令人不悦的结果。

---

## 23. macOS 图标历史

**原文标题**: macOS Icon History

**原文链接**: [https://basicappleguy.com/basicappleblog/macos-icon-history](https://basicappleguy.com/basicappleblog/macos-icon-history)

BasicAppleGuy创建了一个文档集，记录了macOS系统图标的演变历程，其灵感源于macOS 26中引入的引人注目的“液态玻璃”UI重新设计。这种新设计以更柔和、更闪亮、更具玻璃质感的图标为特色，矩形边角更圆润，并强制图标内容包含在边界内。

该项目正在社交媒体上推出，旨在记录多年来的变化。文章详细介绍了更新历史，包括2025年6月和7月在不同日期添加的特定图标。

目前，该文档集包含以下图标：

*   系统偏好设置/设置
*   文件夹
*   便笺
*   备忘录
*   信息
*   计算器
*   Game Center
*   词典
*   App Store
*   地图
*   播客
*   Photo Booth
*   国际象棋
*   提醒事项
*   Apple Books

作者强调，由于测试版图标的设计经常是暂时的，因此不会包含在内。该文档集将在整个夏季持续更新。

---

## 24. 华为克隆Qwen和DeepSeek模型，声称是自主研发。

**原文标题**: Huawei cloned Qwen and DeepSeek models, claimed as own

**原文链接**: [https://dilemmaworks.substack.com/p/whistleblower-huawei-cloned-and-renamed](https://dilemmaworks.substack.com/p/whistleblower-huawei-cloned-and-renamed)

困境作品文章指控华为克隆并重新包装了阿里巴巴的Qwen和DeepSeek大型语言模型（LLM），将其作为其自有专有模型展示。 该文章基于举报人声明和文档，表明华为直接复制了模型权重和架构，然后简单地重命名了这些模型。

具体来说，该文章声称华为的盘古模型实际上是大量基于或完全复制了Qwen和DeepSeek。 核心指控是华为并未像其声称的那样独立开发这些模型，而是利用了现有的开源或商业可用的LLM，并欺骗性地将其作为自己的创新成果展示。

该文章强调了此类行为的道德和潜在法律影响，指出可能存在版权侵权、技术能力虚假陈述，以及通过虚假声称原创开发而获得的不公平竞争优势。 据称，举报人的信息包括支持克隆指控的技术细节，尽管除了提及复制的模型权重和架构之外，摘要本身并未详细说明具体细节。

该文章将华为描绘成从事欺骗性行为以增强其人工智能能力和市场地位，从而对华为在LLM领域的技术进步的真实性提出了严重质疑。

---

## 25. 欧洲首颗地球静止轨道探测卫星发射

**原文标题**: Europe's first geostationary sounder satellite is launched

**原文链接**: [https://www.eumetsat.int/europes-first-geostationary-sounder-satellite-launched](https://www.eumetsat.int/europes-first-geostationary-sounder-satellite-launched)

欧洲空间局（ESA）和欧洲气象卫星组织（EUMETSAT）已成功发射第三代气象卫星探测器1号（MTG-S1），这是欧洲首颗地球静止轨道探测卫星。此次发射标志着欧洲在增强应对极端天气事件能力方面迈出了重要一步。MTG-S1将提供高频大气数据，包括温度、湿度和微量气体，从而实现更准确、更及时的天气预警，进而保护生命和基础设施。

该卫星的红外探测器将扫描热红外波长，以创建大气状况的垂直剖面图，这对于探测正在发展的对流天气至关重要。与MTG成像卫星的数据相结合，它将提供风暴生命周期的全面视图，从而增强短期预报并改进天气模型。该卫星还搭载了哥白尼哨兵-4号仪器，该仪器将监测污染物和气溶胶，以改善空气质量预报并支持公共卫生和环境政策。

欧洲气象卫星组织、欧洲空间局和欧盟委员会的官员强调了这项任务在减轻气候变化影响、改善应急响应以及加强整个欧洲的环境监测方面的重要性。MTG-S1是第三代气象卫星计划的一部分，目前正处于发射和早期运行阶段，并正在向其地球静止轨道位置移动。

---

## 26. 我们可以测试吗？是的，我们可以 [视频]

**原文标题**: Can we test it? Yes, was can [video]

**原文链接**: [https://www.youtube.com/watch?v=MqC3tudPH6w](https://www.youtube.com/watch?v=MqC3tudPH6w)

这个YouTube视频，标题可能为“我们可以测试吗？是的，我们可以”，似乎与在YouTube平台上测试新功能有关。 虽然内容有限，但包括在YouTube页面或视频页脚中常见的标准YouTube法律和信息链接。 这些链接指向以下资源：

*   **新闻版权：** 关于版权政策的信息，尤其是在YouTube上新闻内容方面的政策。
*   **联系我们：** 联系YouTube支持或相关部门的方式。
*   **创作者：** 为YouTube内容创作者提供的资源和信息。
*   **广告：** 为平台上的广告商提供的信息。
*   **开发者：** 为与YouTube API交互的开发者提供的资源。
*   **条款：** YouTube的服务条款。
*   **隐私：** YouTube的隐私政策。
*   **安全：** 与平台安全和保障相关的信息。
*   **YouTube运作方式：** 对YouTube算法和运营原则的解释。
*   **测试新功能：** 强调用户可能正在参与测试YouTube的新功能。
*   **NFL Sunday Ticket：** 提及Google LLC拥有的NFL Sunday Ticket。 这表明可能与体育相关的内容或功能有关。
*   **Google LLC：** 表明YouTube归Google LLC所有。

---

## 27. Show HN: 我用 CSS if() 函数实现了逻辑门

**原文标题**: Show HN: I made Logic gates using CSS if() function

**原文链接**: [https://yongsk0066.github.io/css_if_logic_gate/](https://yongsk0066.github.io/css_if_logic_gate/)

使用 CSS `if()` 函数实现的逻辑门电路创意实践。"Show HN" 展示了作者如何完全使用 CSS 构建诸如 AND、OR、NOT 和 XOR 等基本逻辑门及其对应的 NAND 和 NOR 否定逻辑门。

除了基本逻辑门，该项目还包括更复杂的示例，例如二进制转换器、由 CSS 数学控制的 7 段显示器、半加器、全加器和多路复用器 (MUX)。半加器和全加器的实现展示了 CSS 如何执行按位算术，计算总和位和进位位。

多路复用器示例（2:1 和 4:1）说明了如何使用 CSS 根据选择线在多个输入之间进行选择，从而有效地模拟数字电路中的关键组件。4:1 多路复用器尤其有趣，因为它演示了基于先前定义的基本逻辑门构建的更复杂的逻辑功能。

核心技术依赖于 CSS 自定义属性和 `if()` 函数来模拟条件逻辑。输入值作为 CSS 变量传递（例如，`--a`、`--b`、`--cin`、`--s0`、`--s1`、`--i0`、`--i1` 等），`if()` 函数评估这些变量以确定输出值，然后将其分配给另一个名为 `--value` 的自定义属性。这种方法允许仅在样式表中创建视觉上交互的逻辑电路。 这篇文章突出了 CSS 超越样式并进入函数式编程领域的潜力。

---

## 28. ClojureScript 从原理入门 [视频]

**原文标题**: ClojureScript from First Principles [video]

**原文链接**: [https://www.youtube.com/watch?v=An-ImWVppNQ](https://www.youtube.com/watch?v=An-ImWVppNQ)

ClojureScript从第一性原理 [视频]

---

## 29. 算法交易系统中延迟、测量与优化

**原文标题**: On latency, measurement, and optimization in algorithmic trading systems

**原文链接**: [https://www.architect.co/posts/how-fast-is-it-really](https://www.architect.co/posts/how-fast-is-it-really)

本文深入探讨了算法交易系统（ATS）中延迟测量和优化的复杂性，这是高频交易（HFT）中的一个关键问题。文章认为，由于测量工具本身引入的开销（类似于海森堡不确定性原理），准确的延迟测量具有挑战性。

文章通过一个ATS响应市场交易的伪代码示例来说明这个问题，并最初建议使用`datetime.now()`进行计时。随后，文章强调了这种方法的缺陷，包括其速度慢、由于测量所有交易而不仅仅是导致订单的交易而产生的潜在偏差，以及未能考虑完整的关键路径。文章建议使用`time.perf_counter_ns()`作为一种改进。

文章强调，完整的延迟剖析包括网络I/O、解析和协议转换，这些通常被忽略，但可能构成总延迟的很大一部分。文章提出了两种更准确地捕获延迟的方法：一种是使用网卡硬件时间戳，另一种是涉及模拟交易所和ATS进行受控测试。虽然模拟交易所的方法很全面，但也会测量模拟器自身的延迟。文章建议减去使用简单的“ping/pong”模拟测量的延迟，以接近ATS的真实延迟。最后，文章提到了一种更高级的方法，涉及使用专门的网络硬件进行数据包复制和解析，以实现精确的时间戳。

---

## 30. 加速PostgreSQL数据库转储/恢复快照

**原文标题**: Speeding up PostgreSQL dump/restore snapshots

**原文链接**: [https://xata.io/blog/behind-the-scenes-speeding-up-pgstream-snapshots-for-postgresql](https://xata.io/blog/behind-the-scenes-speeding-up-pgstream-snapshots-for-postgresql)

pgstream团队如何显著提升PostgreSQL CDC工具快照性能：pgstream的优化之路

---

## 31. 利用可微编程优化LLM工作流的工具选择

**原文标题**: Optimizing Tool Selection for LLM Workflows with Differentiable Programming

**原文链接**: [https://viksit.substack.com/p/optimizing-tool-selection-for-llm](https://viksit.substack.com/p/optimizing-tool-selection-for-llm)

无法访问文章链接。

---

## 32. 会说语言的人的秘密

**原文标题**: The Mystery of People Who Speak Languages

**原文链接**: [https://www.newyorker.com/magazine/2018/09/03/the-mystery-of-people-who-speak-dozens-of-languages](https://www.newyorker.com/magazine/2018/09/03/the-mystery-of-people-who-speak-dozens-of-languages)

本文通过语言学家路易斯·米格尔·罗哈斯-贝尔西亚的视角，探讨了精通十一门或以上语言的“超多语者”现象。文章考察了人们对这些个体的迷恋，并将他们与其他重新定义人类潜能的“超级”成就者进行比较。

文章追溯了多语现象的历史和文化背景，指出其在世界许多地方的普遍性，并将其与一些西方社会（特别是美国）相对的单语现象进行了对比。文章强调了一个蓬勃发展的语言爱好者在线社区的存在，以理查德·西姆科特等人物为例，他组织了年度多语者大会。

文章深入探讨了超多语者的潜在特征和动机，指出 LGBTQ+ 群体和自闭症谱系人士在社区中的比例过高。文章还涉及定义“流利”的挑战以及围绕语言掌握声明的敏感性。

最终，文章旨在揭开这些杰出个体的“谜团”，超越对所说语言的简单数字评估，探索驱动他们语言追求的潜在热情、动机和社会文化背景。文章还参考了迈克尔·埃拉德对该主题更科学、更深入的研究。

---

## 33. 技术封建主义与通用人工智能的崛起：一个没有经济权利的未来？

**原文标题**: Techno-feudalism and the rise of AGI: A future without economic rights?

**原文链接**: [https://arxiv.org/abs/2503.14283](https://arxiv.org/abs/2503.14283)

Pascal Stiefenhofer 的 arXiv 论文 (2503.14283) 题为“技术封建主义与通用人工智能的崛起：一个没有经济权利的未来？”，认为通用人工智能 (AGI) 的出现代表着对现有经济和政治体系的根本性颠覆。与以往的技术进步不同，AGI 既充当劳动力又充当资本，在创造经济价值的同时，也将权力集中在控制基础设施的人手中。

作者认为，如果不加以解决，这种转变将加剧不平等，削弱民主机构，并导致“技术封建主义”状态。 传统的社会契约以人类劳动为经济参与的基础，正变得过时。 该论文强调了重新谈判经济框架的紧迫性，以确保公平分配 AGI 驱动的繁荣。

Stiefenhofer 倡导积极干预，包括：

*   **全民人工智能红利：** 将 AGI 产生的财富直接分配给民众。
*   **累进税制：** 实施税收政策，重新分配 AGI 驱动的生产力带来的好处。
*   **去中心化治理：** 建立去中心化的系统，以防止对 AGI 的权力集中。

该论文强调，立即采取行动至关重要，以防止智能本身成为最独特的资本形式，从而导致大规模的经济剥夺。 该论文共 28 页，包含 21 个图表。

---

## 34. 随身听之战

**原文标题**: The War on the Walkman

**原文链接**: [https://newsletter.pessimistsarchive.org/p/the-forgotten-war-on-the-walkman](https://newsletter.pessimistsarchive.org/p/the-forgotten-war-on-the-walkman)

这篇来自“悲观主义者档案”通讯的文章回顾了 20 世纪 70 年代末和 80 年代初索尼 Walkman 面世之初受到的强烈抵制。尽管该设备现在具有怀旧吸引力，但其推出却受到了来自各个方面的批评。一些批评家，如艾伦·布鲁姆，认为它是日益增长的个人主义和社会脱节的象征，而另一些批评家，如约翰·泽赞，则认为它是一种社会退缩的形式。

人们的担忧扩展到公共安全，担心使用耳机损害了司机、骑自行车的人和行人的安全，导致许多州提议或颁布了对耳机使用的限制，尤其是在驾驶或骑自行车时。新泽西州伍德布里奇镇甚至禁止佩戴耳机过马路，违者将被处以罚款和可能的监禁。

退休人士奥斯卡·格罗斯故意佩戴耳机过马路，以示公民不服从，结果被开罚单。尽管他准备入狱以挑战这项法律，但他只被罚款，这让他感到失望。他最初计划将此案提交最高法院，但在发生一起涉及耳机的致命事故后放弃了。

这篇文章强调了新技术往往面临阻力，怀旧往往会抹去人们最初的怀疑和负面情绪。它将智能手机及其对青年人的影响与当代的担忧进行了比较，并指出过去也曾围绕着寻呼机展开过类似的辩论。

---

## 35. 沃尔沃交付第5000辆电动半挂卡车

**原文标题**: Volvo delivers 5,000th electric semi

**原文链接**: [https://electrek.co/2025/06/29/volvo-delivers-5000th-electric-semi-with-little-fanfare-sending-a-big-message/](https://electrek.co/2025/06/29/volvo-delivers-5000th-electric-semi-with-little-fanfare-sending-a-big-message/)

这篇Electrek文章重点介绍了沃尔沃卡车在电动半挂卡车市场取得的静悄悄的成功，并将其与宣传更多但产量较少的特斯拉Semi形成了对比。截至2025年6月，沃尔沃已交付了其第5000辆电动半挂卡车，这是自2019年推出首款电动半挂卡车以来取得的重大里程碑。这些卡车已在50多个国家的商业运营中累计行驶超过1亿英里，为减少排放和噪音污染做出了贡献。

沃尔沃总裁罗杰·阿尔姆强调了实际和可持续的效益，这些效益正在鼓励运输公司采用和扩大其电动车队。这篇文章将沃尔沃定位为领导者，尤其是在欧洲，他们在重型电动卡车领域占据了47%的巨大市场份额。在美国和加拿大，他们在2024年的市场份额也达到了可观的40%。

这篇文章还包含一位读者的推测性评论，指出特斯拉Semi可能存在设计缺陷，尤其是在车轴重量分配方面。尽管特斯拉过去在颠覆行业方面取得了成功，但作者认为，鉴于沃尔沃的先发优势、特斯拉的生产延误以及价格上涨，追赶沃尔沃可能证明是困难的。最终，作者认为，无论哪家公司“获胜”，电动汽车的增长和普及都将使每个人受益。

---

## 36. 哥伦比亚查获首艘配备星链天线的无人毒品潜艇

**原文标题**: Colombia seizes first unmanned narco-submarine with Starlink antenna

**原文链接**: [https://www.france24.com/en/americas/20250702-colombia-narco-submarine-starlink](https://www.france24.com/en/americas/20250702-colombia-narco-submarine-starlink)

哥伦比亚缴获首艘无人毒品潜艇，该潜艇被设计用于运输毒品。潜艇在西南部纳里尼奥省的一个乡村地区被发现，该地区受毒品贩运影响严重。当局认为它计划用于向中美洲运输毒品。

行动精密的关键细节是星链天线的存在。这表明毒品贩运者旨在实现可靠、高速的互联网通信，很可能用于远程控制和导航该船只，可能使他们能够远距离操作潜艇或实时跟踪其进度。

参与此次缉获行动的哥伦比亚海军认为，这是对贩毒集团的重大打击。虽然无人毒品潜艇的传闻甚至在虚构故事中有所描述，但这是哥伦比亚当局首次确认缴获。此次发现突显了贩毒集团在走私毒品时所采用的不断演变的战术和技术进步。当局目前正在调查该潜艇的性能以及参与其建造和计划行动的个人。

---

## 37. KiX原子弹戒指，1947 (2020)

**原文标题**: Atomic "Bomb" Ring from KiX, 1947 (2020)

**原文链接**: [https://toytales.ca/atomic-bomb-ring-from-kix-1947/](https://toytales.ca/atomic-bomb-ring-from-kix-1947/)

本文探讨了原子“弹”戒指，这是 KiX 在 1947 年提供的一款流行的谷物赠品，价格为 15 美分和一个谷物盒顶。这款戒指被宣传为一种科学轰动，反映了公众对原子能的迷恋。这款戒指，也被称为“孤胆骑侠原子弹戒指”，具有金色表带、包含可拆卸红色尾翼的弹头（用于秘密消息）以及闪烁镜。

闪烁镜通过移除尾翼才能使用，是关键的原子特征。在黑暗中观察时，塑料镜头会显示出闪光或闪烁，这是由放射性同位素相互作用引起的。该戒指含有痕量的钋-210，一种与硫化锌屏幕相互作用的放射性物质。

尽管使用了放射性物质，但广告向消费者保证其安全性。文章指出，如今这样的玩具是无法接受的。由于钋-210 的半衰期很短，只有 140 天，因此现有的任何戒指都不会再产生可见的闪烁。文章最后披露了通过 eBay 链接进行的购买将获得佣金。

---

## 38. 我们是坏人吗？

**原文标题**: Are we the baddies?

**原文链接**: [https://geohot.github.io//blog/jekyll/update/2025/07/05/are-we-the-baddies.html](https://geohot.github.io//blog/jekyll/update/2025/07/05/are-we-the-baddies.html)

本文深刻表达了对科技公司和现代资本主义所使用的操纵手段的极度失望。作者批判了Hinge的推广系统、Uber的算法以及普遍使用的“助推”等做法，这些做法在每次互动中都会巧妙地从用户那里榨取更多价值。他们认为，这些做法创造了一个“中间人”，剥削个人并扭曲正常的社会互动。

作者否定了市场力量会纠正这一现象的希望，认为公司善于通过人工智能驱动的调整来先发制人地应对消费者的强烈反对，以维持客户的参与度。他们认为，由于最大化参与度的压力和竞争性商业的“红皇后赛跑”，退出是徒劳的。

此外，作者质疑民主制度在遏制这些算法权力方面的有效性，将投票过程比作Uber车费与司机收入之间的脱节。他们考虑了金融崩溃甚至战争等激烈的解决方案，怀疑即使是灾难性事件也能消除操纵剥削的潜在心态。

核心论点是，广告、价格歧视以及利用数据进行大规模操纵从根本上是错误且不可持续的。作者将现代资本主义视为一种“脑电刺激”，它通过算法使消费者不断消费，而这些算法的设计目标是最大化利润，高于一切。

---

## 39. 在 Raspberry Pi Pico RP2040 MCU 上模拟串行 SPI RAM

**原文标题**: Serial SPI RAM Emulation on Raspberry Pi Pico RP2040 MCU

**原文链接**: [https://github.com/MichaelBell/spi-ram-emu](https://github.com/MichaelBell/spi-ram-emu)

此项目在树莓派 Pico 的 RP2040 上模拟一个串行 SPI RAM (例如 23LC512)，使 Pico 可以充当可通过 SPI 访问的 RAM 设备。 它以顺序模式实现 READ (0x03)、WRITE (0x02) 和 FAST READ (0x0B) 命令。 最大 SPI 时钟速度取决于操作和系统时钟，对齐的 READ 操作可实现更高的速度。

集成包括将文件复制到您的项目或使用子模块，配置引脚、DMA 通道和 PIO 状态机 (SM)，并使用 `setup_simulated_sram()` 启动模拟。 需要自定义内存映射。

该实现利用 PIO 和 DMA 进行时间关键型操作，将 core1 专用于 RAM 模拟。 PIO 处理数据输入和输出，而 core1 管理命令处理、地址操作和基于 CS 信号的事务终止。 Core1 驻留在 scratch RAM 中，以实现一致的执行时间。

READ 命令通过在接收到的地址前添加固定的内存位置并使用 DMA 触发写入 PIO 来进行优化。 WRITE 命令组合了 core1 上的地址位，并使用 DMA 将数据从读取 PIO 传输到内存。 FAST READ 命令通过修补写入 PIO 程序以获得延迟周期并重新配置 DMA 来实现。

限制包括未表征的最小 CS 高电平时间和不支持在数据传输开始前中止操作。 该项目有效地利用 RP2040 的 PIO 和 DMA 功能来模拟 SPI RAM 功能，为嵌入式系统中的内存扩展或替换提供了一种实用的解决方案。

---

## 40. Show HN: 一个协作开发副项目的社区

**原文标题**: Show HN: a community for collaborating on sideprojects

**原文链接**: [https://relentlessly.no/](https://relentlessly.no/)

无法访问文章链接。

---

## 41. 注射拒绝 (2006)

**原文标题**: Injection Rejection (2006)

**原文链接**: [https://thedailywtf.com/articles/Injection_Rejection](https://thedailywtf.com/articles/Injection_Rejection)

仅凭提供的标题和内容片段，无法对文章“Injection Rejection (2006)”进行全面总结。片段仅显示：

*   **标题：** Injection Rejection (2006) - 表明该文章可能涉及注入主题，考虑到其他关键词，可能是在技术背景下。"Rejection" 暗示与此注入相关的某种形式的失败、预防或漏洞。
*   **内容分类：** 文章可能被发现的或与托管它的网站相关的类别列表：
    *   **feature articles：** 表明这是一篇重要的文章。
    *   **codesod（可能指 "Code SOD"）：** 暗示它可能与软件开发或系统管理有关。 SOD 可能代表 System Out of Disarray，暗示故障排除或问题解决。
    *   **error'd：** 暗示它处理错误或错误查找。
    *   **forums：** 表明具有交互式社区方面。
    *   **other articles/random article：** 导航元素。

**可能的解释（在没有完整文章的情况下）：**

鉴于标题和相关类别，“Injection Rejection”可能与以下内容有关：

*   **软件安全：** 讨论与注入攻击（如 SQL 注入）相关的漏洞以及预防或“拒绝”它们的方法。它可能详细介绍常见的注入缺陷、防御策略（输入验证、输出编码等）和安全最佳实践。
*   **调试/错误处理：** 描述特定编码环境或系统中特定注入技术的拒绝或失败。它可能侧重于解决与注入相关的错误的故障排除步骤。
*   **医疗背景（鉴于其他关键词可能性较小）：** 一种可能性较小的解释是，关于注射药物或治疗后器官移植排斥反应的医学文章，尽管周围的术语表明了技术重点。

要准确总结文章，需要访问其全文。

---

## 42. 风编织厂

**原文标题**: Wind Knitting Factory

**原文链接**: [https://www.merelkarhof.nl/work/wind-knitting-factory](https://www.merelkarhof.nl/work/wind-knitting-factory)

梅雷尔·卡尔霍夫的“风力针织工厂”描述了一台连接在建筑物外立面的风力驱动针织机。该机器利用风能编织一条长长的围巾，编织速度随风力强度而变化。围巾沿着建筑物下降，直到到达窗户，在那里被拉入室内继续增长。定期地，针织材料会被“收获”并转化为围巾。每条围巾都标有风力为其创作做出贡献的日期和时间。该装置作为一个移动工厂，展示了一个由城市风力驱动的生产过程，在公共和私人空间之间运作。该项目旨在将城市风力的潜力可视化为一种资源。艺术家的其他项目包括但不限于“翼型桌”、“风力针织围巾”、“阴影体量”和“能量收集器”。

---

## 43. 《火星救援》教会我们关于PlanetScale与Neon之争的什么

**原文标题**: What 'Project Hail Mary' teaches us about the PlanetScale vs. Neon debate

**原文链接**: [https://blog.alexoglou.com/posts/database-decisions/](https://blog.alexoglou.com/posts/database-decisions/)

《“火星救援2：玛丽计划”揭示的PlanetScale与Neon之争》一文探讨了主要在X/Twitter上关于Neon性能与PlanetScale相比的在线争论，特别是源于PlanetScale CEO的评论。

作者将此比作小说《火星救援2：玛丽计划》中的一段情节，其中人物讨论了一个优先考虑可扩展性而非效率的繁殖数据库系统。核心论点是，就像在分布式系统设计中一样，存在固有的权衡，没有普遍最佳的解决方案。

作者认为PlanetScale和Neon都有各自的优势，适用于不同的用例。文章承认了在线负面情绪和戏剧的吸引力，但敦促工程师们认识到两种解决方案的价值，避免追求单一、完美的数据库系统。关键在于，可扩展性和效率常常相互矛盾，选择正确的解决方案取决于具体的项目需求。

---

## 44. 地球上最离奇、神秘的闪电形态

**原文标题**: The most otherworldly, mysterious forms of lightning on Earth

**原文链接**: [https://www.nationalgeographic.com/science/article/lightning-sprites-transient-luminous-events-thunderstorms](https://www.nationalgeographic.com/science/article/lightning-sprites-transient-luminous-events-thunderstorms)

本文探讨瞬态发光现象 (TLEs)，一种发生在雷暴云之上的神秘光显示，包括红色精灵、喷流和鬼魅。与传统闪电不同，这些现象转瞬即逝、无声无息，且发生在更高的大气层中，将天气、太空和电力联系起来。

像Angel An和董书畅这样的研究人员和业余摄影师正在合作了解这些现象，捕捉图像和视频。An和董在青藏高原上捕捉到的105个红色精灵，对理解TLEs做出了重大贡献。

由Burcu Kosar领导的NASA“Spritacular”项目正在创建一个TLEs的众包数据库，依靠公民科学家提交图像并分析从地面和国际空间站收集的数据。这个全面的数据库旨在识别TLEs发生中的模式和趋势，并研究更罕见的类型，如喷流和鬼魅。

对TLEs的研究也延伸到地球之外。数据显示，类似的事件也发生在木星上。了解TLEs也可能有助于追踪气候变化的影响，因为气温上升预计会影响雷暴强度和闪电活动，从而可能影响TLEs的发生。科学家们认为，研究这些事件可以深入了解高层大气和我们在地球上经历的暴风雨。

---

## 45. Haskell、逆波兰表示法与解析

**原文标题**: Haskell, Reverse Polish Notation, and Parsing

**原文链接**: [https://mattwills.bearblog.dev/haskell-postfix/](https://mattwills.bearblog.dev/haskell-postfix/)

这篇博文记录了作者受朋友建议和一次关于逆波兰表示法 (RPN) 的网络对话的启发，开始学习 Haskell 的历程。作者最初习惯于 Python 和 C 等命令式语言，但发现 Haskell 的函数式范式是一种重要的思维转变，需要接受不变性、递归和数学抽象。

作者重点介绍了 Haskell 的关键概念，如递归类型（定义自然数）、lambda 函数和柯里化函数。然后，他们通过实现归并排序来展示函数式编程的优雅之处，突显 Haskell 的简洁性和清晰度。

博文随后深入探讨了 RPN，解释了其基于堆栈的求值模型及其在早期计算器中的相关性。在最初实现了一个有限的 RPN 求值器之后，作者向 Graham Hutton 寻求建议，他的解决方案启发作者构建了一个更健壮的解析器。这促使作者探索 monad，首先是用于错误处理的 `Maybe` 类型。

作者随后介绍了 Haskell 中的 `Parser` 类型，展示了 monad 如何促进解析器的组合。博文解释了 bind 运算符 `>>=` 如何链接解析器，自动处理状态管理和错误处理。他们展示了实际示例，如 `item`（读取单个字符）和 `sat`（条件字符解析），说明了 monad 如何实现干净且可组合的解析器代码。博文最后强调了 monadic 解析的强大功能，可以从简单的构建块构建复杂的解析器。

---

## 46. 过于雄心勃勃是一种聪明的自我破坏形式。

**原文标题**: Being too ambitious is a clever form of self-sabotage

**原文链接**: [https://maalvika.substack.com/p/being-too-ambitious-is-a-clever-form](https://maalvika.substack.com/p/being-too-ambitious-is-a-clever-form)

以下是文章“过度雄心是一种巧妙的自我破坏形式”的摘要，基于其标题和可能的内容，假设它探讨了过度雄心的潜在弊端：

文章可能认为，虽然雄心通常被认为是积极的，但 *过度* 的雄心壮志反而会导致自我破坏。它认为，设定过于雄心勃勃的目标会产生巨大的压力、焦虑和对失败的恐惧。这可能会表现为拖延、倦怠或普遍的受困感，最终阻碍了朝着任何目标前进的步伐。

作者可能指出，拥有过于雄心勃勃的目标的个人可能会过于关注遥远、理想化的结果，而忽略了实现目标所需的较小、可实现的步骤。这可能会导致感到不足和气馁，因为当前的现实与想象中的未来之间的差距似乎太大了。

此外，文章可能探讨了完美主义（通常与高度的雄心壮志交织在一起）如何导致自我破坏。害怕达不到高不可攀的标准会使个人瘫痪，阻止他们开始或完成任务。他们也可能对自己所做的努力过于挑剔，从而削弱他们的信心和动力。

最后，这篇文章可能以倡导一种更平衡的雄心方式作为结尾，强调设定现实目标、庆祝小胜利以及专注于过程而非仅仅关注结果的重要性。它可能鼓励读者培养自我同情心，并在追求愿望的同时优先考虑福祉。核心信息是，可持续的进步源于对雄心的专注和适度的态度，而不是对无法实现的理想的无情和压倒性的追求。

---

## 47. Gecode是一个用于开发基于约束系统的开源C++工具包 (2019)

**原文标题**: Gecode is an open source C++ toolkit for developing constraint-based systems (2019)

**原文链接**: [https://www.gecode.org/](https://www.gecode.org/)

Gecode是一款开源C++工具包，专为构建基于约束的系统和应用程序而设计。它提供了一个高性能的约束求解器，该求解器具有模块化和可扩展性，允许与其他系统无缝集成，并创建自定义的约束、分支策略、搜索引擎和变量域。

Gecode拥有一套全面的功能，包括整数、布尔值、集合和浮点数的约束、C++建模层、高级分支启发式、各种搜索引擎（并行、交互式、重启）、自动对称性打破、no-good学习和MiniZinc支持。

该工具包在效率方面表现出色，实现了卓越的运行时性能和内存使用。 这体现在它在2008年至2012年的MiniZinc挑战赛中的统治地位，它赢得了所有类别的所有金牌。

Gecode具有完善的文档，提供全面的教程和完整的参考文档，以指导用户完成建模和编程任务。 Gecode在MIT许可下分发，是免费软件，所有部分（包括源代码）均可下载。

它的C++实现确保了可移植性，允许使用现代编译器进行编译，并在各种机器上运行。 Gecode还支持并行搜索，利用多核处理器来增强性能。 经过严格的测试，拥有超过50,000个测试用例和接近100％的覆盖率，从而保证了其可靠性。

---

## 48. 游戏发行商回应“停止扼杀游戏”的主张，称其限制了开发者的选择。

**原文标题**: Game publishers respond to Stop Killing Games claim it curtails developer choice

**原文链接**: [https://www.pcgamer.com/gaming-industry/european-game-publisher-group-responds-to-stop-killing-games-claims-these-proposals-would-curtail-developer-choice/](https://www.pcgamer.com/gaming-industry/european-game-publisher-group-responds-to-stop-killing-games-claims-these-proposals-would-curtail-developer-choice/)

本文探讨了“停止扼杀游戏”运动与游戏发行商，特别是欧洲电子游戏协会（Video Games Europe），之间关于停止在线游戏服务的冲突。“停止扼杀游戏”运动现已成为一项欧洲公民倡议，它质疑发行商关闭玩家已购买的游戏（使其无法玩）的合法性。他们提倡游戏保存，并认为玩家实际上正在失去他们付费购买的产品。

欧洲电子游戏协会反驳说，停止在线服务是一个复杂的决定，由商业可行性驱动。他们认为，维护服务器和提供私人替代方案的成本可能高得令人望而却步，尤其是对于纯在线游戏而言。他们还对与用户数据安全、非法内容以及私人服务器上的内容审核相关的法律责任表示担忧，而这些问题他们在其官方服务器上处理。他们认为，该运动的提议将限制开发者的选择，使纯在线游戏的创作在财务上不可持续。

虽然“停止扼杀游戏”运动获得了显著的关注，为其欧盟请愿书积累了超过一百万个签名，但任何由此产生的政策变化可能只会适用于欧盟（以及可能的英国），从而让发行商可以自由地在其他地区关闭游戏。本文强调了核心分歧：玩家将购买游戏视为拥有产品，而发行商则将其视为访问服务的许可。

---

## 49. X-向导致意

**原文标题**: X-Clacks-Overhead

**原文链接**: [https://xclacksoverhead.org/home/about](https://xclacksoverhead.org/home/about)

"X-Clacks-Overhead"是一个非标准的HTTP头部，灵感来源于特里·普拉切特的碟形世界系列，特别是“克拉克斯”信号系统。在书中，克拉克斯的发明者罗伯特·迪尔哈特将他已故儿子的名字“GNU John Dearheart”编码到系统的操作信号中，以永久保存他的记忆。“GNU”代码确保消息被传递下去，而不是被记录，并在行尾返回，象征着记忆的持久性。

在普拉切特去世后，Reddit上的碟形世界粉丝们创建了X-Clacks-Overhead头部，以同样的方式纪念他。网站作者可以在其服务器响应中包含此头部，传递类似“GNU Terry Pratchett”的无声纪念，而不会影响网站功能。只有通过分析HTTP头部才能检测到它。

Mozilla.org、Debian.org、XML.com和The Register等著名网站使用该头部来纪念特里·普拉切特和其他人，如莱斯特·海恩斯。提供的链接提供了关于GNU Terry Pratchett、特里·普拉切特本人、碟形世界系列、克拉克斯以及导致头部创建的Subreddit讨论的更多信息。该网站还告知用户其使用cookies来实现功能和个性化内容。

---

## 50. 四个整数就足以编写贪吃蛇游戏。

**原文标题**: Four integers are enough to write a Snake Game

**原文链接**: [https://www.andreinc.net/2022/05/01/4-integers-are-enough-to-write-a-snake-game](https://www.andreinc.net/2022/05/01/4-integers-are-enough-to-write-a-snake-game)

本文介绍了一个用 C 语言实现的极简版贪吃蛇游戏，其限制在于仅使用四个整型变量：`map`、`vars`、`shape` 和 `i`。目标是展示一种扭曲的代码极简主义实践，而非优雅的代码。

*   `map` (uint32_t) 存储游戏棋盘（4x8 网格），用位来表示蛇身节。
*   `vars` (uint32_t) 打包了各种游戏状态：蛇头位置 (`hpos`)、蛇尾位置 (`tpos`)、蛇长 (`len`)、苹果位置 (`apos`) 和方向 (`chdir`)。大量使用宏来访问和修改这些位域。
*   `shape` (uint64_t) 充当方向队列，存储每个蛇身节的移动方向。每个方向用两位表示，最多可存储 32 个方向。
*   `i` (int8_t) 用作循环计数器。

文章详细介绍了用于操作这些整数中的位的宏，包括 `s_set`、`s_get`、`s_hpos_set` 等。游戏循环使用 `curses` 库进行屏幕渲染和键盘输入。`move_snake` 函数更新蛇的位置并管理苹果的消耗，而 `check_*` 函数则防止蛇越界或撞到自身。

作者承认代码的混淆性，并将本文用作演示位操作和将数据压缩到有限内存中的示例。完整的源代码可在 GitHub 上找到。

---

## 51. QSBS限额提高

**原文标题**: QSBS Limits Raised

**原文链接**: [https://www.mintz.com/insights-center/viewpoints/2906/2025-06-25-qsbs-benefits-expanded-under-senate-finance-proposal](https://www.mintz.com/insights-center/viewpoints/2906/2025-06-25-qsbs-benefits-expanded-under-senate-finance-proposal)

本文探讨了参议院财政委员会“一个宏伟法案”版本中，针对《国内税收法》第1202条关于合格小企业股票(QSBS)的拟议修改。

目前，QSBS允许非公司创始人及投资者免除出售QSBS高达100%的收益，但需满足以下限制：收益不得超过1000万美元或股票成本的10倍，取两者中较高者；股票持有时间超过五年；直接从公司获得；公司总资产低于5000万美元；且公司符合积极经营业务的要求。

参议院财政委员会的提案引入了三个主要变更：

1.  **分级收益排除：** 为较短的持有期提供部分收益排除：持有3年以上为50%，持有4年以上为75%，持有5年以上为100%。
2.  **提高单发行人上限：** 将收益排除上限提高至1500万美元，并从2027年开始根据通货膨胀进行调整。
3.  **提高总资产阈值：** 将公司层面的总资产阈值提高至7500万美元，并从2027年开始根据通货膨胀进行调整。

如果这些变更获得通过，将适用于生效日或之后发行或获得的股票。在生效日期之前进行的投资仍将受到现有1000万美元上限的约束。

作者认为，这些变更为创始人及投资者提供了更大的灵活性，允许更早的退出机会并享受部分收益排除。接近5000万美元资产阈值的公司可能会考虑推迟融资，直到该立法的命运更加明朗。作者认为拟议的变更对初创企业和新兴公司生态系统而言是积极的一步。

---

## 52. 为什么最简单的桌面代理抽象能够胜出

**原文标题**: Why the simplest desktop agent abstraction wins

**原文链接**: [https://www.bytebot.ai/blog/designing-bytebot-why-the-simplest-desktop-agent-abstraction-wins](https://www.bytebot.ai/blog/designing-bytebot-why-the-simplest-desktop-agent-abstraction-wins)

本文提倡一种简化的AI桌面代理构建方法，重点关注最通用的界面：键盘、鼠标和屏幕。作者的解决方案Bytebot正是基于此原则构建的。

本文将此方法与依赖API和直接工具集成的传统方法进行对比，作者认为这些方法脆弱、受限，并且由于LLM的快速发展而最终不可持续。他们引用了“惨痛的教训”，强调最显著的AI进步来自于利用算力扩展简单的方法，而不是构建复杂的专用系统。

Bytebot的“远程工作者”抽象允许代理与任何为人类使用而设计的应用程序进行交互，无需自定义集成，并使代理更强大且面向未来。它解决了API和内部逻辑之间的“无人区”任务，例如在应用程序之间跳转、处理身份验证以及与遗留软件交互。

这种简化抽象的优势在于通用性、保真度、可组合性、可观察性和可扩展性。这种方法允许公司集成代理，而无需重组其工作流程或维护自定义API，因为代理只需在现有的计算环境中运行。智能是模型无关的，并随着模型的发展而自动改进。作者强调Bytebot专为长期使用而设计，无论未来的LLM如何发展，都为代理提供了一个稳定的平台。

---

## 53. 看似简单却并不简单的编程问题，乔恩·斯基特参与解答

**原文标题**: Programming problems that seem easy, but aren't, featuring Jon Skeet

**原文链接**: [https://the-stack-overflow-podcast.simplecast.com/episodes/programming-problems-that-seem-easy-but-arent-featuring-jon-skeet/transcript](https://the-stack-overflow-podcast.simplecast.com/episodes/programming-problems-that-seem-easy-but-arent-featuring-jon-skeet/transcript)

好的，我已经分析了提供的Stack Overflow Podcast节目“看似简单，实则不然的编程问题，嘉宾：Jon Skeet”的文字记录。以下是摘要：

该播客节目讨论了看似简单，但在考虑边缘情况、性能和可维护性时却极具复杂性的编程问题。编程界知名人物Jon Skeet参与讨论，提供了深刻的见解和轶事。

核心主题围绕着这样一个观点：许多看似简单的任务，如日期和时间操作、字符串解析、货币格式化，甚至基本计算，都可能因各种因素而迅速变得具有挑战性。这些因素包括：

*   **全球化/本地化：** 处理不同的文化规范，如日期格式、数字分隔符和货币符号，会增加显著的复杂性。处理时区和夏令时尤其麻烦。

*   **边缘情况和极端情况：** 这些是不常见但仍然有效的情况，如果处理不当，通常会导致意外错误。Skeet使用了闰年和不寻常的日期范围等例子。

*   **性能考量：** 简单的解决方案可能适用于小型数据集，但在处理大量数据时可能会变得非常缓慢和低效。

*   **可维护性：** 现在以简单方式解决问题的代码可能在以后变得难以理解、修改或调试，尤其是在添加新需求时。

*   **浮点运算：** 在计算机中表示实数并不总是精确的，这会导致细微的误差积累，并在计算中引起问题。

Skeet强调了在解决这些“简单”编程问题时，进行彻底测试并仔细考虑所有可能的输入和场景的重要性。他提倡尽可能使用经过良好测试的库和框架，而不是试图重新发明轮子。该节目强调，健壮且可靠的代码需要的不仅仅是基本的语法理解；它需要仔细的规划、细致的测试以及对潜在陷阱的认识。播客还简要提到了在这种情况下代码审查的挑战。

---

## 54. 低地位的护城河

**原文标题**: The Moat of Low Status

**原文链接**: [https://usefulfictions.substack.com/p/learn-to-love-the-moat-of-low-status](https://usefulfictions.substack.com/p/learn-to-love-the-moat-of-low-status)

无法访问文章链接。

---

## 55. 按需定制构建系统 (2018) [pdf]

**原文标题**: Build Systems à la Carte (2018) [pdf]

**原文链接**: [https://www.microsoft.com/en-us/research/wp-content/uploads/2018/03/build-systems.pdf](https://www.microsoft.com/en-us/research/wp-content/uploads/2018/03/build-systems.pdf)

我无法总结这篇文章，因为它不是人类可读的格式。提供的文本似乎是一个PDF文件的内部代码，由对象定义和压缩数据流组成。为了总结，我需要访问文章的实际文本内容，而不是其二进制表示。

---

## 56. 电子音乐史：476首精选 (1937–2001)

**原文标题**: The History of Electronic Music in 476 Tracks (1937–2001)

**原文链接**: [https://www.openculture.com/2025/06/the-history-of-electronic-music-in-476-tracks.html](https://www.openculture.com/2025/06/the-history-of-electronic-music-in-476-tracks.html)

本文重点介绍了Ubuweb上一个引人注目的在线汇编：“电子音乐史：476首曲目 (1937–2001)”，它最初是一套62张CD。这个由Caio Barros上传的庞大档案旨在呈现电子/电子声学音乐的历史概览，特别适合对先锋派和音乐学感兴趣的人。

本文承认该收藏的局限性，正如Ubuweb所指出的，特别是缺乏对女性作曲家和非西方传统的代表。然而，它强调了该汇编的可贵努力和其中包含的大量优秀音乐。作者建议将该收藏视为一个起点，鼓励听众策划自己的播放列表，或者将其视为一门沉浸式的西方传统先锋派电子音乐课程。

本文还指出，电子音乐不仅仅包括名人DJ和默默无闻的先锋派作曲家，并突出了那些弥合流行/舞曲/表演和严肃作曲之间差距的艺术家。最终，这篇文章将Ubuweb收藏视为一个宝贵的资源，同时承认其偏见，并倡导对电子音乐历史进行更具包容性和全面性的理解。文章还提供了相关内容的链接，包括电子音乐中的女性历史和达芙妮·奥拉姆对电子音乐的解释。

---

## 57. 瑞内·图尔西奥斯参加过200多个黑客马拉松，但他不会写代码。

**原文标题**: Rene Turcios has attended over 200 hackathons and doesn’t know how to code

**原文链接**: [https://sfstandard.com/2025/07/05/rene-turcios-hackathon-labubu-vibe-coding-chatgpt/](https://sfstandard.com/2025/07/05/rene-turcios-hackathon-labubu-vibe-coding-chatgpt/)

雷内·图尔西奥斯，自称旧金山“黑客马拉松之王”，两年内参加了超过200场黑客马拉松，虽然不懂编程，却赢得了奖品和认可。图尔西奥斯利用AI编程工具，这种做法被称为“氛围编程”，通过自然语言提示快速构建项目。

起初被传统工程师不屑一顾的图尔西奥斯，证明了AI在黑客马拉松中的力量，在他的首次获胜中，他使用ChatGPT将歌曲转换成lo-fi版本。他的成功源于他的竞争精神，这得益于他过去作为职业游戏王牌手的职业生涯，在那里他掌握了高效的策略。

图尔西奥斯不同寻常的背景包括在马戏团家庭长大以及游牧式游戏王职业生涯。由于他的工程师抵制AI，他的元宇宙基础设施公司倒闭后，图尔西奥斯开始专注于黑客马拉松，以探索AI的潜力。

现在，图尔西奥斯为企业承包项目，举办AI编程研讨会，并作为一名独立创始人，正在建立自己的AI代理创业公司，AI处理所有编程工作。他展示了自己的技能，仅用十五分钟就使用AI工具为他的Labubu娃娃创建了一个转售网站。他相信在AI的帮助下，任何人都可以构建他们想要的任何东西。

---

## 58. 芯片上的计算器 (2015)

**原文标题**: The Calculator-on-a-Chip (2015)

**原文链接**: [http://www.vintagecalculators.com/html/the_calculator-on-a-chip.html](http://www.vintagecalculators.com/html/the_calculator-on-a-chip.html)

芯片计算器
        
本文《芯片计算器》详细介绍了20世纪70年代初彻底改变计算器行业的集成电路的开发和推出。在芯片出现之前，计算器体积庞大、结构复杂且价格昂贵，需要多个电路板才能容纳众多元件。

文章重点介绍了Mostek为Busicom于1970年11月开发的MK6010（后来为MK5010），这是第一款“芯片计算器”。该芯片显著减小了计算器的尺寸、成本和复杂性。Busicom Junior是第一款使用该芯片的产品，它用单个芯片取代了两个电路板。低功耗版本（MK6010L）使第一款袖珍计算器Busicom LE-120A“HANDY”的诞生成为可能。

德州仪器（TI）紧随其后推出了TMS1802（后来为TMS0102），这是一款更先进的单芯片微控制器，专为计算器使用而优化。与Mostek的定制芯片不同，TMS1802是“现成的”，可以编程用于各种功能。

这些芯片的引入显著降低了劳动力成本，并为消费级计算器市场铺平了道路。虽然使用这些芯片的初始型号价格昂贵，但价格下降的趋势最终导致了更便宜的型号和广泛的采用。尽管Busicom发挥了先锋作用，但它面临财务困境，并于1974年停止生产，而TI进一步扩展了其微控制器设计。

---

## 59. 迷你NAS结合NVMe与英特尔高效芯片

**原文标题**: Mini NASes marry NVMe to Intel's efficient chip

**原文链接**: [https://www.jeffgeerling.com/blog/2025/mini-nases-marry-nvme-intels-efficient-chip](https://www.jeffgeerling.com/blog/2025/mini-nases-marry-nvme-intels-efficient-chip)

本文评测了三款迷你NAS设备：GMKtec G9、Aiffro K100和Beelink ME mini，它们都专为小型家庭实验室设计，并采用Intel N100/N150芯片。作者正从大型存储设置转型，寻求一种紧凑高效且具有约6TB可用空间的NAS解决方案。

这三款NAS都具有2.5 Gbps网络连接（GMKtec和Beelink为双口），以及多个M.2 NVMe SSD插槽，利用了Intel芯片的PCIe通道。GMKtec G9是经济实惠的选择，但最初存在散热问题，需要进行设计修改。Aiffro K100是最小、最冷静、最节能的设备，拥有金属外壳和全面的通风设计，但缺少eMMC和Wi-Fi，且只有一个2.5Gbps端口。Beelink ME mini具有六个NVMe插槽（尽管大多数被限制为PCIe Gen 3 x1），内置eMMC，以及独特的内部电源设计。它的运行温度略高于K100。

作者强调了这些小型设备固有的妥协。虽然G9提供了最优惠的价格，但其最初的散热问题非常严重。K100在效率和散热方面表现出色，但也是最昂贵的，并且缺少eMMC。Beelink提供了最大的存储扩展性，但代价是单个驱动器的带宽。如果能找到4 TB NVMe SSD的好价钱来满足存储需求，作者倾向于K100。

---

## 60. 7-Zip 25.00

**原文标题**: 7-Zip 25.00

**原文链接**: [https://github.com/ip7z/7zip/releases/tag/25.00](https://github.com/ip7z/7zip/releases/tag/25.00)

文章发布 7-Zip 25.00 版。主要改进包括：

*   **增强 CPU 利用率：** 7-Zip 现在可以利用超过 64 个 CPU 线程进行压缩（zip/7z/xz）和基准测试，并在具有超过 64 个 CPU 线程的 Windows 系统中，将线程分配到不同的处理器组。

*   **压缩速度提升：** bzip2 压缩速度提高 15-40%，deflate (zip/gz) 压缩速度提高 1-3%。

*   **改进的存档支持：** 包括对 zip、cpio 和 fat 存档的更好支持。

*   **漏洞修复：** 此版本修复了各种错误和漏洞。

该版本由 ip7z 发布，有 139 个 fork，1.7k 个 star，并且有 62 人对此作出了反应。文章提到资源加载问题。

---

## 61. OBBB签署：恢复美国本土研发费用立即费用化

**原文标题**: OBBB signed: Reinstates immediate expensing for U.S.-based R&D

**原文链接**: [https://www.kbkg.com/feature/house-passes-tax-bill-sending-to-president-for-signature](https://www.kbkg.com/feature/house-passes-tax-bill-sending-to-president-for-signature)

众议院通过的《大型美丽账单法案》（OBBBA）代表着一项重大的税收政策改革，立即生效或追溯至2025年初。一项关键条款是恢复美国本土研发的立即费用化，允许全额扣除国内研究成本，并有可能追溯扣除2022-2024年资本化的费用。小型企业可以将全额费用化追溯应用于2021年之后的纳税年度。

该法案还恢复了2025年1月19日之后投入使用的合格资产的100%额外折旧，并为符合条件的生产财产引入了截至2029年的额外折旧。

相反，该法案终止了许多IRA清洁能源激励措施，例如179D和45L，并限制了投资税收抵免（ITC）和生产税收抵免（PTC），适用于法案颁布后12个月内开始建设并在2027年12月31日之前投入使用的项目。

其他主要变化包括提高小型企业的第179条费用化上限，保留SALT变通办法，提高SALT上限并为高收入者逐步取消，取消第899条“报复性税收”，放宽超额商业亏损规则，并修订第163(j)条商业利息扣除规则。国际税收规则收紧，LIHTC上限提高以鼓励经济适用房。其中包括亲商业的改进措施，以及新的中产阶级扣除额。税务专业人士和企业需要迅速评估这些变化对其投资组合的影响，建立情景模型，并与利益相关者沟通，以优化税务策略。

---

## 62. 是蛋糕吗？我们的大脑如何解读材质

**原文标题**: Is It Cake? How Our Brain Deciphers Materials

**原文链接**: [https://nautil.us/is-it-cake-how-our-brain-deciphers-materials-1222193/](https://nautil.us/is-it-cake-how-our-brain-deciphers-materials-1222193/)

戴尔·马科维茨的《鹦鹉螺》杂志文章“这是蛋糕吗？我们的大脑如何解读材质”探讨了我们识别物体材质能力背后的神经科学。这种看似简单的技能对于生存至关重要，帮助我们正确地与世界互动，从判断某物是否可食用到评估其作为工具的潜力。

虽然神经科学已经广泛研究了物体识别，但材料感知却相对被忽视。Edward H. Adelson在2001年发表的一篇有影响力的论文推动了该领域的研究。最近的研究集中在诸如木材或金属等特定材料，以及诸如光泽或硬度等属性上。

最近，Schmidt、Hebart、Schmid和Fleming在《美国国家科学院院刊》上发表的一篇论文提出了一种广义方法。他们使用机器学习技术处理了一个材料图像数据集和参与者的相似度评级，识别出了36个“材料感知的核心维度”。这些维度，如“矿物”、“织物状”、“晶体状”和“海绵状”，是大脑用于分类材料的认知轴。

大脑并非依靠专门的“物质”区域，而是依赖于一个分布式网络，将低级视觉特征与高级知识（如背景、记忆和经验）相结合。对“动态点材料”的研究表明，即使没有视觉纹理，大脑也能根据运动推断材料的属性，激活视觉、体感和运动区域。这表明大脑可以填补缺失的信息，并预测材料的行为和触感。

文章总结说，我们的大脑与识别材料的能力深度连接，这解释了我们对“这是蛋糕吗？”这类错觉的着迷，因为该系统中的一个小故障就会扰乱我们与世界的互动。

---

## 63. 英伟达赢了，我们都输了

**原文标题**: Nvidia won, we all lost

**原文链接**: [https://blog.sebin-nyshkim.net/posts/nvidia-is-full-of-shit/](https://blog.sebin-nyshkim.net/posts/nvidia-is-full-of-shit/)

该文章描绘了英伟达当前黯淡的景象，认为其近期的成功是以牺牲消费者利益为代价的。文章批评了 RTX 50 系列的发布，指出存在黄牛机器人、据称人为抬高需求的有限库存，以及零售商捆绑销售导致的价格虚高等问题。作者指出，即使是较老的 RTX 40 系列 GPU，与 AMD 的替代产品相比，价格也过高。

文章重点指出了硬件缺陷，特别是缺少 ROP 的 GPU，以及持续熔化的 12VHPWR 连接器，并将后者归因于英伟达尚未充分解决的设计缺陷。作者质疑为什么英伟达在供应方面不如苹果等其他科技巨头，暗示由于利润丰厚的数据中心市场，英伟达对消费级 GPU 的关注度降低。

文章进一步批评了英伟达的专有技术，如 DLSS、CUDA、NVENC 和 G-Sync，认为它们造成了供应商锁定，迫使用户在性能和更广泛的生态系统兼容性之间做出选择。文章还指出，英伟达通过放弃 32 位 PhysX 支持破坏了向后兼容性，对旧游戏产生了负面影响。

最后，作者认为，虽然 DLSS 应用广泛，但它是一种“灵丹妙药”，掩盖了 GPU 在光线追踪方面性能不足的事实。RTX 5090 仍然难以在原生 4K 分辨率下，在高要求的光线追踪游戏中实现可玩帧率，这意味着英伟达的技术进步被其营销和定价策略所掩盖。最终，文章认为英伟达的统治地位导致了质量和消费者价值的下降。

---

## 64. 新研究揭示让人觉得“酷”的因素

**原文标题**: New study offers clues about what makes someone cool

**原文链接**: [https://www.nytimes.com/2025/06/30/well/mind/cool-people-traits-study.html](https://www.nytimes.com/2025/06/30/well/mind/cool-people-traits-study.html)

无法访问文章链接。

---

## 65. 追求爱好比追求成就更能提升幸福感 (2023)

**原文标题**: Chasing Hobbies over Achievement Boosts Happiness (2023)

**原文链接**: [https://neurosciencenews.com/hedonism-happiness-achievement-23923/](https://neurosciencenews.com/hedonism-happiness-achievement-23923/)

2023年埃塞克斯大学研究：追求享乐和自由与幸福感相关

（或：埃塞克斯大学2023年研究：享乐和自由提升幸福感）

---

## 66. 塞纳河百年禁泳令解除，巴黎泳者重返河中

**原文标题**: Seine reopens to Paris swimmers after century-long ban

**原文链接**: [https://www.lemonde.fr/en/france/article/2025/07/05/seine-reopens-to-paris-swimmers-after-century-long-ban_6743058_7.html](https://www.lemonde.fr/en/france/article/2025/07/05/seine-reopens-to-paris-swimmers-after-century-long-ban_6743058_7.html)

After a century-long ban, the Seine River in Paris reopened to public swimming on July 5, 2025. This milestone follows a major cleanup effort spurred by the Paris 2024 Olympics, where open-water swimming and triathlon events took place in the river. Three supervised swimming zones, equipped with amenities like changing rooms and showers, are now available to the public.

Paris officials have implemented safety measures including daily water quality testing and swim assessments by lifeguards. While water quality is reported as "exceptional," with E. coli and enterococci levels far below safety thresholds, swimmers are warned about potential dangers like strong currents and boat traffic. Fines will be issued to those swimming outside designated areas.

The reopening is the culmination of decades-long efforts, dating back to former Mayor Jacques Chirac's initial advocacy in 1988. President Macron celebrated the reopening, calling it a "collective effort" and a source of "pride" for France.

Authorities invested €1.4 billion to improve the Seine's water quality and plan to close the sites after heavy rainfall due to sewage overflow. Despite the risks, the city is hoping for drier weather this year. Mayor Hidalgo views the Seine cleanup as part of a larger strategy to adapt Paris to climate change and improve the quality of life for its citizens. The swimming spots are free and open to the public until August 31.


---

## 67. Robots move Shanghai city block [video]

**原文标题**: Robots move Shanghai city block [video]

**原文链接**: [https://www.youtube.com/watch?v=7ZccC9BnT8k](https://www.youtube.com/watch?v=7ZccC9BnT8k)

生成摘要时出错

---

## 68. ADXL345 (2024)

**原文标题**: ADXL345 (2024)

**原文链接**: [https://www.tinytransistors.net/2024/08/25/adxl345/](https://www.tinytransistors.net/2024/08/25/adxl345/)

生成摘要时出错

---

## 69. Solve high degree polynomials using Geode numbers

**原文标题**: Solve high degree polynomials using Geode numbers

**原文链接**: [https://www.tandfonline.com/doi/full/10.1080/00029890.2025.2460966](https://www.tandfonline.com/doi/full/10.1080/00029890.2025.2460966)

生成摘要时出错

---

## 70. BYD Seal 06 DM-i Variant: 2,000 Kilometer Range at USD15,340

**原文标题**: BYD Seal 06 DM-i Variant: 2,000 Kilometer Range at USD15,340

**原文链接**: [https://cleantechnica.com/2025/07/05/byd-seal-6-dm-1-variant-2000-kilometer-range-15340-anybody-want-one/](https://cleantechnica.com/2025/07/05/byd-seal-6-dm-1-variant-2000-kilometer-range-15340-anybody-want-one/)

生成摘要时出错

---

## 71. Kepler.gl

**原文标题**: Kepler.gl

**原文链接**: [https://kepler.gl/](https://kepler.gl/)

生成摘要时出错

---

## 72. WinUAE 6 Amiga Emulator

**原文标题**: WinUAE 6 Amiga Emulator

**原文链接**: [https://www.winuae.net/](https://www.winuae.net/)

生成摘要时出错

---

## 73. 幻境：首个由实时世界模型驱动的AI原生UGC游戏引擎

**原文标题**: Mirage: First AI-Native UGC Game Engine Powered by Real-Time World Model

**原文链接**: [https://blog.dynamicslab.ai](https://blog.dynamicslab.ai)

生成摘要时出错

---

## 74. 我为什么离开科技行业，转而研究慢性疼痛

**原文标题**: Why I left my tech job to work on chronic pain

**原文链接**: [https://sailhealth.substack.com/p/why-i-left-my-tech-job-to-work-on](https://sailhealth.substack.com/p/why-i-left-my-tech-job-to-work-on)

生成摘要时出错

---

## 75. 操作员，而非用户和程序员

**原文标题**: Operators, Not Users and Programmers

**原文链接**: [https://jyn.dev/operators-not-users-and-programmers/](https://jyn.dev/operators-not-users-and-programmers/)

生成摘要时出错

---

## 76. Stop killing games and the industry response

**原文标题**: Stop killing games and the industry response

**原文链接**: [https://blog.kronis.dev/blog/stop-killing-games](https://blog.kronis.dev/blog/stop-killing-games)

生成摘要时出错

---

## 77. A Canadian's AI hoax duped the media and propelled a 'band' to success

**原文标题**: A Canadian's AI hoax duped the media and propelled a 'band' to success

**原文链接**: [https://www.cbc.ca/news/entertainment/ai-band-hoax-velvet-sundown-1.7575874](https://www.cbc.ca/news/entertainment/ai-band-hoax-velvet-sundown-1.7575874)

生成摘要时出错

---

## 78. Optimizing typography of insect labels using free fonts and free software (2012) [pdf]

**原文标题**: Optimizing typography of insect labels using free fonts and free software (2012) [pdf]

**原文链接**: [https://www.akentsoc.org/doc/Bowser_ML_2012.pdf](https://www.akentsoc.org/doc/Bowser_ML_2012.pdf)

生成摘要时出错

---

## 79. Problems the AI industry is not addressing adequately

**原文标题**: Problems the AI industry is not addressing adequately

**原文链接**: [https://www.thealgorithmicbridge.com/p/im-losing-all-trust-in-the-ai-industry](https://www.thealgorithmicbridge.com/p/im-losing-all-trust-in-the-ai-industry)

生成摘要时出错

---

## 80. A 37-year-old wanting to learn computer science

**原文标题**: A 37-year-old wanting to learn computer science

**原文链接**: [https://initcoder.com/posts/37-year-old-learning-cs/](https://initcoder.com/posts/37-year-old-learning-cs/)

生成摘要时出错

---

## 81. N-Back – A Minimal, Adaptive Dual N-Back Game for Brain Training

**原文标题**: N-Back – A Minimal, Adaptive Dual N-Back Game for Brain Training

**原文链接**: [https://n-back.net](https://n-back.net)

生成摘要时出错

---

## 82. The ancient invention that ignited game play (2021)

**原文标题**: The ancient invention that ignited game play (2021)

**原文链接**: [https://www.bbc.com/future/article/20210318-the-ancient-invention-that-ignited-game-play](https://www.bbc.com/future/article/20210318-the-ancient-invention-that-ignited-game-play)

生成摘要时出错

---

## 83. The 1960s schools experiment that created a whole new alphabet

**原文标题**: The 1960s schools experiment that created a whole new alphabet

**原文链接**: [https://www.theguardian.com/education/2025/jul/06/1960s-schools-experiment-created-new-alphabet-thousands-children-unable-to-spell](https://www.theguardian.com/education/2025/jul/06/1960s-schools-experiment-created-new-alphabet-thousands-children-unable-to-spell)

生成摘要时出错

---

## 84. Baba Is Eval

**原文标题**: Baba Is Eval

**原文链接**: [https://fi-le.net/baba/](https://fi-le.net/baba/)

生成摘要时出错

---

## 85. Introducing tmux-rs

**原文标题**: Introducing tmux-rs

**原文链接**: [https://richardscollin.github.io/tmux-rs/](https://richardscollin.github.io/tmux-rs/)

生成摘要时出错

---

## 86. Killer whales groom each other with pieces of kelp

**原文标题**: Killer whales groom each other with pieces of kelp

**原文链接**: [https://www.science.org/content/article/killer-whales-groom-each-other-pieces-kelp](https://www.science.org/content/article/killer-whales-groom-each-other-pieces-kelp)

生成摘要时出错

---

## 87. Show HN: AirBending – Hand gesture based macOS app MIDI controller

**原文标题**: Show HN: AirBending – Hand gesture based macOS app MIDI controller

**原文链接**: [https://www.nanassound.com/products/software/airbending](https://www.nanassound.com/products/software/airbending)

生成摘要时出错

---

## 88. Compression Dictionary Transport

**原文标题**: Compression Dictionary Transport

**原文链接**: [https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Compression_dictionary_transport](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Compression_dictionary_transport)

生成摘要时出错

---

## 89. Compression Dictionary Transport

**原文标题**: Compression Dictionary Transport

**原文链接**: [https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Compression_dictionary_transport](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Compression_dictionary_transport)

生成摘要时出错

---

## 90. Scientists capture slow-motion earthquake in action

**原文标题**: Scientists capture slow-motion earthquake in action

**原文链接**: [https://phys.org/news/2025-06-scientists-capture-motion-earthquake-action.html](https://phys.org/news/2025-06-scientists-capture-motion-earthquake-action.html)

生成摘要时出错

---

## 91. Ask HN: I want to leave tech: what do I do?

**原文标题**: Ask HN: I want to leave tech: what do I do?

**原文链接**: [https://write.as/conjure-utopia/lets-say-youre-working-in-tech-and-you-have-a-technical-role-youre-a](https://write.as/conjure-utopia/lets-say-youre-working-in-tech-and-you-have-a-technical-role-youre-a)

生成摘要时出错

---

## 92. The Right Way to Embed an LLM in a Group Chat

**原文标题**: The Right Way to Embed an LLM in a Group Chat

**原文链接**: [https://blog.tripjam.app/the-right-way-to-embed-an-llm-in-a-group-chat/](https://blog.tripjam.app/the-right-way-to-embed-an-llm-in-a-group-chat/)

生成摘要时出错

---

## 93. Umberto Eco's Guide to Thesis Writing and a Guide to Life

**原文标题**: Umberto Eco's Guide to Thesis Writing and a Guide to Life

**原文链接**: [https://www.newyorker.com/books/page-turner/a-guide-to-thesis-writing-that-is-a-guide-to-life](https://www.newyorker.com/books/page-turner/a-guide-to-thesis-writing-that-is-a-guide-to-life)

生成摘要时出错

---

## 94. The messy reality of SIMD (vector) functions

**原文标题**: The messy reality of SIMD (vector) functions

**原文链接**: [https://johnnysswlab.com/the-messy-reality-of-simd-vector-functions/](https://johnnysswlab.com/the-messy-reality-of-simd-vector-functions/)

生成摘要时出错

---

## 95. Volunteer finds Holy Grail of abolitionist-era Baptist documents

**原文标题**: Volunteer finds Holy Grail of abolitionist-era Baptist documents

**原文链接**: [https://www.bostonherald.com/2025/07/03/baptist-anti-slavery-scroll/](https://www.bostonherald.com/2025/07/03/baptist-anti-slavery-scroll/)

生成摘要时出错

---

## 96. Pet ownership and cognitive functioning in later adulthood across pet types

**原文标题**: Pet ownership and cognitive functioning in later adulthood across pet types

**原文链接**: [https://www.nature.com/articles/s41598-025-03727-9](https://www.nature.com/articles/s41598-025-03727-9)

生成摘要时出错

---

## 97. Lens: Lenses, Folds and Traversals

**原文标题**: Lens: Lenses, Folds and Traversals

**原文链接**: [https://hackage.haskell.org/package/lens](https://hackage.haskell.org/package/lens)

生成摘要时出错

---

## 98. Gremllm

**原文标题**: Gremllm

**原文链接**: [https://github.com/awwaiid/gremllm](https://github.com/awwaiid/gremllm)

生成摘要时出错

---

## 99. Sleeping beauty Bitcoin wallets wake up after 14 years to the tune of $2B

**原文标题**: Sleeping beauty Bitcoin wallets wake up after 14 years to the tune of $2B

**原文链接**: [https://www.marketwatch.com/story/sleeping-beauty-bitcoin-wallets-wake-up-after-14-years-to-the-tune-of-2-billion-79f1f11f](https://www.marketwatch.com/story/sleeping-beauty-bitcoin-wallets-wake-up-after-14-years-to-the-tune-of-2-billion-79f1f11f)

生成摘要时出错

---

## 100. Can Large Language Models Play Text Games Well? (2023)

**原文标题**: Can Large Language Models Play Text Games Well? (2023)

**原文链接**: [https://arxiv.org/abs/2304.02868](https://arxiv.org/abs/2304.02868)

生成摘要时出错

---

