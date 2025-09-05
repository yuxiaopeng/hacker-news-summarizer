# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-09-05.md)

*最后自动更新时间: 2025-09-05 17:45:54*
## 1. 我放弃了 Docker，选择了 Podman (你也应该试试)

**原文标题**: I Ditched Docker for Podman (and You Should Too)

**原文链接**: [https://codesmash.dev/why-i-ditched-docker-for-podman-and-you-should-too](https://codesmash.dev/why-i-ditched-docker-for-podman-and-you-should-too)

我已查阅该文章，以下是摘要：

文章《我弃用 Docker 改用 Podman (你也应该这样做)》的作者认为，对于许多用例来说，Podman 是比 Docker 更好的替代方案，主要侧重于安全性和无根执行。

切换的主要原因是 Docker 需要一个 root 拥有的守护进程，这带来了重大的安全风险。 如果 Docker 守护进程受到攻击，整个系统都将变得脆弱。 另一方面，Podman 可以作为非 root 用户（无根）运行容器。 这大大减少了攻击面并提高了安全性。 作者强调，虽然 Docker *可以*配置为以无根方式运行，但它比 Podman 的原生无根支持复杂得多。

文章指出，Podman 与 Docker 镜像和 Dockerfile 兼容，使得过渡相对无缝。 在许多情况下，您可以使用 `alias docker=podman`，并且现有的 Docker Compose 配置可以与 `podman-compose` 一起使用。

此外，Podman 与 systemd 的集成更好，可以轻松地将容器作为 systemd 服务进行管理。 作者还赞赏 Podman 相比 Docker 默认设置的改进的网络配置。

总而言之，作者提倡使用 Podman 是因为它增强的安全功能，特别是无根执行、易用性、与 Docker 标准的兼容性以及更好的 systemd 集成。 他们认为，与 Docker 相比，Podman 提供了更安全且通常更简单的容器化体验，使其成为许多开发人员和系统管理员值得考虑的替代方案。

---

## 2. 你说的完全正确！

**原文标题**: You're absolutely Right!

**原文链接**: [https://absolutelyright.lol/](https://absolutelyright.lol/)

这篇题为《你绝对正确！》的短文，呈现了一个简单且重复的信息，围绕着说话者坚信自己是正确的这一信念展开。文章包含三个强调这种自认为正确的短语：“我绝对正确！”，“绝对正确”，以及“恰恰好”。它还包括语句“Claude Code今天说了0次”，在周围断言的语境下，这可以被解读为一种元评论，突出了原始断言的强度和原创性——或许暗示即使是人工智能（Claude Code）今天也没有提出过同样的声明。其核心信息围绕着一种有力，甚至可能有些幽默的，对坚定不移的确定性的宣告。

---

## 3. 你不需要动画

**原文标题**: You Don't Need Animations

**原文链接**: [https://emilkowal.ski/ui/you-dont-need-animations](https://emilkowal.ski/ui/you-dont-need-animations)

本文强调了在用户界面中使用有目的性和经过深思熟虑的动画的重要性，认为动画如果做得好，可以提高可预测性、速度和用户满意度，但如果实施不当，也可能带来不利影响。

作者强调，在添加动画之前，重要的是要问“目的是什么？” 动画应该服务于功能目的，例如解释某个功能或提供反馈，或者少量使用以增加乐趣。 使用频率是一个关键因素。 重复使用的动画会变得令人讨厌并降低用户体验。 作者建议考虑完全删除常用元素的动画，尤其是那些由键盘操作触发的动画。

速度是另一个重要方面。 UI动画通常应在300毫秒以内，以提高感知性能和响应速度。 例如，工具提示受益于初始延迟以防止意外激活，但后续工具提示应立即显示，以获得更快的体验。

核心信息是，不应为了动画而添加动画。 目标是创建用户喜欢使用的出色用户界面，这有时意味着完全省略动画。 知道何时*不*使用动画与知道如何使用动画同样重要。

---

## 4. 电脑升级导致旧金山湾区捷运系统关闭。

**原文标题**: A computer upgrade has shut down BART

**原文链接**: [https://www.bart.gov/news/articles/2025/news20250905](https://www.bart.gov/news/articles/2025/news20250905)

东湾BART因电脑设备故障导致严重中断，前往旧金山的服务已完全停止。东湾部分线路正在逐步恢复有限服务。黄线在安提阿克和奥克兰12街之间运行，蓝线从都柏林到麦克阿瑟运行，橙线从贝里埃萨到里士满运行。建议往返旧金山的通勤者寻找其他交通方式，因为目前BART无法前往该市。BART网站bart.gov/alternatives提供了替代交通路线和选择的信息。公告强调问题与电脑设备有关，表明技术故障是服务中断的根本原因。

---

## 5. 开发速度从未成为瓶颈

**原文标题**: Development Speed Has Never Been a Bottleneck

**原文链接**: [https://pawelbrodzinski.substack.com/p/development-speed-is-not-a-bottleneck](https://pawelbrodzinski.substack.com/p/development-speed-is-not-a-bottleneck)

无法访问文章链接。

---

## 6. 旧机器人网站

**原文标题**: The Old Robots Website

**原文链接**: [https://www.theoldrobots.com/index2.html](https://www.theoldrobots.com/index2.html)

老式机器人网站

该网站似乎是一个个人收藏和在线资源，致力于机器人，特别是老式型号和玩具机器人。 该网站包含多个部分，包括：

*   **主页、指南、链接、新闻、下载、愿望清单：** 标准网站导航和内容部分。
*   **教育机器人和玩具机器人（多美、其他）：** 侧重于用于教育目的的机器人，以及专门介绍玩具机器人的部分，特别强调多美和其他品牌。
*   **我的机器人：** 网站的核心，展示了所有者的个人机器人收藏。
*   **分类机器人（教育/个人、Omnibot、其他 I-VII）：** 该网站按类别组织，可能基于机器人类型、产地或功能，包括教育/个人机器人、Omnibot 机器人和一系列“其他机器人”类别。
*   **来源 & 更新：** 该收藏被确定为所有者的个人收藏，上次更新于 2008 年 1 月 14 日。

本质上，该网站是一个精选的机器人信息、图像和资源档案，主要由收藏家的个人兴趣驱动，专注于复古和玩具机器人。 该网站旨在为机器人爱好者提供信息。

---

## 7. 日本解景场成员0b5vr访谈

**原文标题**: Interview with Japanese Demoscener – 0b5vr

**原文链接**: [https://6octaves.com/2025/09/interview-with-demoscener-0b5vr.html](https://6octaves.com/2025/09/interview-with-demoscener-0b5vr.html)

本文采访了日本demoscener 0b5vr，他以其64K和4K intro而闻名，特别是他在Revision 2023上发布的“0b5vr GLSL Techno Live Set”。他解释了这个demo背后的灵感，它融合了techno demos、现场编码和64K intro，在64KB的文件中创造了一种现场表演体验。他讨论了单人64K项目面临的挑战以及demoscene的演变，并强调了GLSL在音乐制作、机器现场表演和生成式VJing（“gene-kei”）中日益增长的普及度。

0b5vr分享了他在“draw(tokyo); #2”上表演现场编码set的经验，使用了他定制的GLSL现场编码环境Wavenerd。他还提到了他和Renard合作的4K作品“Architectural Shapeshifter”，该作品使用0x4015的minimalGL创建。

这次采访还探讨了非技术观众如何欣赏demoscene作品，将其比作欣赏艺术或音乐而无需理解底层数据或代码。0b5vr强调了技术技能和艺术表达的重要性，并欢迎非技术方面的scener。最后，他提到了目前4K intro的流行，因为它具有用户友好的工具，并呼吁日本demoscene中进行更多合作。

---

## 8. 还有人还在用摩尔斯电码吗？

**原文标题**: Does anyone still use Morse code?

**原文链接**: [https://morse-coder.com/](https://morse-coder.com/)

本文推广一个全面的莫尔斯电码翻译平台。它详细介绍了其功能，面向从初学者到专业人士的用户，突出了其准确性和多功能性。

该平台提供文本到莫尔斯电码和莫尔斯电码到文本的翻译，使用点(.)和划线(-)以及空格和斜杠分隔符。它包括具有可调节速度和频率的音频播放、可视光指示器以及文本和音频文件（WAV/MP3）的下载选项。

高级功能包括图像处理，用于解码图片中的莫尔斯电码；音频信号分析，用于声音录音；批量文件处理以及具有建议的抗错翻译。它还支持多种语言和历史电报协议。

该平台采用实时字符映射引擎、用于图像的OCR模式识别以及用于音频的数字信号处理。 提供学习教育资源，包括莫尔斯电码字母表、词汇、流程信号以及带有视觉反馈的音频训练。

引用的实际应用包括业余无线电执照、海事和航空紧急通信、历史电报操作以及STEM教育。流行的学习主题包括编码浪漫信息和掌握紧急信号。该平台支持全面的莫尔斯电码字母表精通。

---

## 9. 为什么大家都赔钱在人工智能上

**原文标题**: Why Everybody Is Losing Money on AI

**原文链接**: [https://www.wheresyoured.at/why-everybody-is-losing-money-on-ai/](https://www.wheresyoured.at/why-everybody-is-losing-money-on-ai/)

本文认为生成式人工智能产业从根本上是无利可图的，正走向一场“次贷AI危机”。作者断言，几乎所有提供生成式人工智能服务的公司，包括像OpenAI和Anthropic这样的模型提供商，都在大量亏损。

核心问题是推理（从提示生成输出）的高成本。由于“推理”模型对token的大量需求（而这些模型对于更好的输出是必需的），这些成本正在增加。文章引用了Cursor（一个编码AI应用程序）的例子，它将其100%的收入发送给Anthropic，以及Perplexity，它将其收入的164%用于计算。OpenAI也在计算上花费了其收入的很大一部分，导致数十亿美元的亏损。

作者批评科技媒体淡化这个问题，并认为成本降低不太可能实现。文章总结说，大型语言模型的经济效益是不可持续的。建立在AI模型之上的公司正在赔钱，甚至模型提供商也在苦苦挣扎。

作者认为，唯一可能的解决方案是公司直接向用户收取他们产生的计算成本，但他怀疑用户是否愿意支付所需的高昂价格。人工智能模型的固有缺陷，例如缺乏“知识”和无法有效执行任务，进一步加剧了这个问题。作者认为，目前形式的生成式人工智能本质上是无利可图的。

---

## 10. ClickHouse实时分析数据建模指南

**原文标题**: Data Modeling Guide for Real-Time Analytics with ClickHouse

**原文链接**: [https://www.ssp.sh/blog/practical-data-modeling-clickhouse/](https://www.ssp.sh/blog/practical-data-modeling-clickhouse/)

本文旨在为使用ClickHouse进行实时分析的数据建模提供指导，面向寻求亚秒级查询响应的数据工程师和从业者。文章着重介绍了ClickHouse相对于传统数据仓库的优势，强调其面向列的存储、高级压缩、矢量化查询执行以及稀疏主键索引以实现卓越性能。

该指南强调了数据流的重要性，提倡以业务需求为中心的数据建模，并回答关键问题。它引入了“左移”的概念，强调在管道早期构建数据结构，以避免昂贵的下游转换。一个关键点是实时分析中数据新鲜度和准确性之间的权衡。

文章探讨了特定的ClickHouse建模策略：反规范化、字典、增量物化视图和可刷新物化视图，所有这些策略都旨在最大限度地减少查询时的连接。文章讨论了在ClickHouse中建模多维OLAP多维数据集，承认缺乏传统的逻辑建模层，并强调需要预定义的优化表。

一个实际演示涉及从S3提取NOAA天气数据，在ClickHouse中对其进行转换和聚合，并使用Rill对其进行可视化。该示例展示了ClickHouse如何充当数据转换引擎和存储层，从而无需传统的ETL工具。YAML配置演示了ClickHouse内的数据提取、转换、分区和表创建，从而优化了用于实时分析的数据。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 2 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 3 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 4 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 5 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 6 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 7 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 8 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 9 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 10 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 11 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 12 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 13 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 14 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 15 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 16 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 17 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 18 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 19 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 20 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 21 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 22 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 23 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 24 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 25 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 26 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 27 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 28 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 29 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 30 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 31 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 32 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 33 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 34 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 35 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 36 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 37 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 38 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 39 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 40 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 41 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 42 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 43 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 44 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 45 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 46 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 47 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 48 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 49 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 50 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 51 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 52 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 53 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 54 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 55 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 56 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 57 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 58 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 59 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 60 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 61 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 62 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 63 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 64 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 65 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 66 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 67 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 68 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 69 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 70 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 71 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 72 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 73 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 74 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 75 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 76 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 77 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 78 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 79 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 80 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 81 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 82 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 83 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 84 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 85 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 86 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 87 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 88 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 89 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 90 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 91 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 92 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 93 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 94 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 95 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 96 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 97 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 98 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 99 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 100 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 101 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 102 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 103 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 104 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 105 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 106 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 107 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 108 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 109 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 110 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 111 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 112 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 113 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 114 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 115 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 116 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 117 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 118 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 119 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 120 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 121 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 122 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 123 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 124 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 125 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 126 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 127 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 128 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 129 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 130 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 131 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 132 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 133 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 134 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 135 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 136 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 137 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 138 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 139 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 140 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 141 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 142 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 143 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 144 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 145 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 146 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 147 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 148 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 149 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 150 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 151 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 152 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 153 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 154 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 155 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 156 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 157 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 158 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 159 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 160 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 161 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 162 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 163 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 164 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 165 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 166 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 167 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 168 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 169 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 170 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
