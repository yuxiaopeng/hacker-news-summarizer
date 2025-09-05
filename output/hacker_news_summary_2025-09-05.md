# Hacker News 热门文章摘要 (2025-09-05)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Protobuf是错误的

**原文标题**: Protobuffers Are Wrong

**原文链接**: [https://reasonablypolymorphic.com/blog/protos-are-wrong/](https://reasonablypolymorphic.com/blog/protos-are-wrong/)

本文反对使用 Protocol Buffers (Protobufs)，认为它们设计拙劣、临时拼凑，并且仅对 Google 规模的运营真正有益。作者，一位前 Google 员工，断言 Protobufs 存在缺陷的类型系统和缺乏可组合性导致了武断的限制和样板代码。

强调的核心问题包括：

*   **类型系统糟糕：** Protobufs 具有限制性和不合理的类型系统，存在诸多局限，尤其是在 `oneof` 和 `map` 字段方面。它未能利用现代类型系统概念。
*   **设计选择存在疑问：** 对标量类型和消息类型的处理不一致，导致意想不到的行为。标量字段始终存在默认值，从而无法区分未设置值和默认值。消息字段提供默认初始化的副本，但也破坏了赋值法则，可能导致意想不到的副作用。
*   **兼容性的虚假承诺：** Protobufs 通过过于宽松的方式实现向后和向前兼容，导致可能不正确的数据解释，且缺乏显式的健全性检查。作者批评了为未来演进而内联定义的建议（违反 DRY 原则）。
*   **代码库污染：** 由于 Protobufs 的限制，开发人员经常在应用程序逻辑中直接使用 Protobuf 类型，导致代码僵化，并阻止了最佳实践技术的使用。
*   **Google 规模的优化：** Protobufs 优化以节省字节，这可能对 Google 有益，但对大多数其他公司来说是浪费工程时间。

作者提倡更简单、更具可组合性的类型系统，这些系统提供更多的控制和可靠性，并认为 Protobufs 会导致容易出错、非通用和非多态的代码。文章认为，大多数公司并非 Google 规模，不应盲目采用他们的技术。

---

## 12. 菲尔的不可思议的垃圾回收器

**原文标题**: Fil's Unbelievable Garbage Collector

**原文链接**: [https://fil-c.org/fugc](https://fil-c.org/fugc)

FUGC (Fil 的难以置信的垃圾回收器) 是一种并行、并发、即时、灰栈 Dijkstra 精确非移动垃圾回收器，用于 Fil-C 中。它旨在通过以下几个关键特性最大限度地减少停顿并最大限度地提高效率：

*   **并行 & 并发：** 利用多个线程进行标记和清除，而不会暂停 mutator 线程。
*   **即时：** 采用“软握手”和轮询检查来实现异步线程协作，避免全局停止所有线程的暂停。线程只会体验到由堆栈高度限制的短暂回调。
*   **灰栈 Dijkstra：** 重新扫描线程堆栈以达到不动点，仅需要一个简单的存储屏障（Dijkstra 屏障）而不是加载屏障。在 GC 期间新分配的对象会被预先标记。
*   **精确 & 非移动：** 精确地识别指向对象的所有指针，不会在内存中移动对象以简化并发，但会将已释放对象的capability指针“移动”到空闲单例。
*   **推进波前：** 通过确保已标记的对象保持标记状态，防止 mutator 操作为回收器创建更多工作。
*   **快速清除：** 使用位向量 SIMD，使清除非常高效（通常不到 GC 时间的 5%）。

FUGC 还支持高级内存管理功能：

*   **释放对象：** 将对象标记为空闲，捕获后续访问，并将capability指针重定向到空闲单例以确保回收。
*   **终结器：** 提供类似于 Java 的终结器队列。
*   **弱引用 & 弱映射：** 提供 Java 风格的弱引用和 JavaScript 风格的 WeakMaps。

FUGC 提供强大的内存误用保证：保证捕获 use-after-free 和 double-free 错误，未能释放内存会导致自动回收。

---

## 13. 韩国：多名国民在ICE突袭乔治亚州现代工厂时被拘留

**原文标题**: South Korea: 'many' of its nationals detained in ICE raid on GA Hyundai facility

**原文链接**: [https://www.nbcnews.com/news/us-news/ice-hyundai-plant-georgia-enforcement-action-rcna229148](https://www.nbcnews.com/news/us-news/ice-hyundai-plant-georgia-enforcement-action-rcna229148)

韩国就现代汽车集团在佐治亚州埃拉贝尔Metaplant施工现场发生的移民局突袭事件向美国大使馆表达了关切，该突袭导致“许多”韩国公民被拘留。此次突袭涉及移民及海关执法局、国土安全调查局和其他联邦机构，是对“非法雇佣行为和其他严重联邦犯罪”调查的一部分。被针对的地点是现代汽车和LG新能源共同建设电池工厂的所在地。

国土安全调查局已证实该施工现场存在非法行为，并逮捕了无证人员。虽然被拘留的确切人数尚不清楚，但报告显示这是一次大规模行动，现场有许多执法车辆和巴士。现代汽车正在配合调查，并已暂停施工。

调查的时间线还在继续，当局强调需要追究责任并维护法律。韩国是美国的主要盟友和投资者，渴望保护其国民和公司在美国运营的权利和利益，尤其是在现代汽车最近承诺投资数十亿美元并在该国创造数千个就业岗位的情况下。

---

## 14. 什么是傅里叶变换？

**原文标题**: What Is the Fourier Transform?

**原文链接**: [https://www.quantamagazine.org/what-is-the-fourier-transform-20250903/](https://www.quantamagazine.org/what-is-the-fourier-transform-20250903/)

本文阐述了傅里叶变换，一种将任何函数分解为其组成频率或“类波构建块”的数学工具。 傅里叶变换由让-巴蒂斯特·约瑟夫·傅里叶在 19 世纪初研究热传导时开发，它允许数学家将复杂函数分解为更简单的正弦和余弦波，从而更容易解决问题。

文章用人耳将声波分离成不同音调的类比来阐述这个概念。它解释了变换的机制，描述了它如何通过将原始函数乘以不同频率的正弦和余弦波来扫描每个可能频率的贡献。

傅里叶变换对数学产生了深远的影响，催生了调和分析领域，并在数论、微分方程、量子力学、图像压缩（如 JPEG）、音频处理和医学成像（MRI）等不同领域中得到应用。 20 世纪 60 年代快速傅里叶变换的开发使其应用更加广泛。

文章重点介绍了变换在量子力学中用于说明不确定性原理及其与理解数论中素数分布的联系。 像查尔斯·费弗曼这样的数学家强调了傅里叶变换的巨大影响，认为如果没有它，很大一部分数学将会消失。

---

## 15. 使用 Roc 构建 WASM 编译器 (系列)

**原文标题**: Building a WASM compiler in Roc (series)

**原文链接**: [https://dusty.phillips.codes/roc/](https://dusty.phillips.codes/roc/)

本文介绍一系列博文，重点在于使用 Roc 编程语言构建 WebAssembly (WASM) 编译器。该系列从 2024 年 8 月 17 日开始，将引导读者完成整个过程，从项目设置和语言基础到代码生成和编译器完成。 该系列结构如下：

*   **初始设置:** 介绍 Roc 和 WASM，处理 Roc 中的参数和 IO，并设置词法分析器的样板代码。
*   **词法分析:** 处理错误处理，词法分析器中的位置跟踪以及综合测试。
*   **语法分析:** 介绍语法分析概念并实现语法分析技术，重点是重构。
*   **转换:** 将解析后的表示形式转换为适合代码生成的格式。
*   **代码生成:** 生成最终的 WASM 代码，涵盖数据、类型、导入、函数、代码和导出部分。
*   **结论:** 以生成导出和总结结束本系列。

本文重点介绍了 GitHub 上提供的完整源代码，并将内容标记为“Roc”、“Compiler”和“Tutorial”。 本系列提供了一个使用 Roc 构建编译器的实用、动手指南，使其易于对编译器设计和函数式编程感兴趣的人们访问。

---

## 16. 展示一下：Vapor - 一款随打字逐渐消失的记事本

**原文标题**: Show HN: Vapor – A notepad that fades away as you type

**原文链接**: [https://enda.sh/vapor/](https://enda.sh/vapor/)

Vapor：鼓励前瞻性思维的瞬时便笺应用。它的核心理念是文本随输入逐渐消逝，防止用户纠结于已写内容。这种强制专注旨在通过消除编辑的诱惑来促进创造性思维和写作。

用户只能专注于当前输入的内容，因为之前的文本会逐渐消失。这种短暂性促进了一种意识流写作风格，并鼓励用户思考下一个想法，而不是完善上一个。

应用允许用户在完成后保存他们的作品，从而保留最终输出。此功能提供了一个安全保障，允许用户在想法完全消失之前捕获它们。 Vapor 鼓励用户开始使用并体验这种独特的写作方式。

---

## 17. Stripe推出L1区块链：Tempo

**原文标题**: Stripe Launches L1 Blockchain: Tempo

**原文链接**: [https://tempo.xyz](https://tempo.xyz)

Stripe 推出 Tempo：专为支付设计的全新 Layer-1 区块链

---

## 18. 维提纳里的钟 (2011)

**原文标题**: Vetinari's Clock (2011)

**原文链接**: [https://www.waitingforfriday.com/?p=264](https://www.waitingforfriday.com/?p=264)

西蒙·茵斯的“维提纳里的时钟”一文详细介绍了他的项目，该项目旨在复制特里·普拉切特的碟形世界系列小说中那种不规则走动的时钟，以此来让访客感到不安。他的设计基于Hackaday上的一篇文章，并提到Akafugu.jp网站出售套件版本。

该时钟的控制器取代了标准的石英机芯控制器。它使用一个由32.768kHz晶振计时的PIC12F683微控制器，利用timer0中断进行精确计时，同时节省电力。

该固件实现了跨越128步的32秒“随机”脉冲序列，以不同的增量推进秒针，从而产生不规则的滴答声效果。一个辅助延迟进一步随机化了这些运动。

该电路包含限流电阻以保护PIC和时钟模块，由两节AA电池供电。肖特基二极管用于钳制来自线圈的电压尖峰。

作者展示了如何将控制器板连接到时钟机芯的线圈，固定连接，并将控制板和电池固定到时钟背面。他还指出，该设计是可定制的，并且可以重新编程。他提供了可下载的项目文件，包括Eagle CAD原理图和PCB文件，以及HiTech C固件源代码。

---

## 19. LLM可视化

**原文标题**: LLM Visualization

**原文链接**: [https://bbycroft.net/llm](https://bbycroft.net/llm)

这篇题为“LLM可视化”的“文章”本质上是标题的重复，表明这是一个占位符或非常基础的着陆页。关键信息在于其预期主题：**LLM（大型语言模型）可视化。**

鉴于缺乏实质内容，总结必须侧重于这种隐含的意图：

这个条目表明一个以大型语言模型可视化为中心的主题。虽然文档本身没有提供关于可视化的*方式*或*原因*的信息，但它清楚地指出了主题。目的可能涉及创建LLM的视觉表示，以更好地理解它们的内部运作、能力、局限性或性能。这可能包括可视化模型架构、数据流、注意力机制、输出分布或其他相关方面。最终，目标大概是通过视觉手段来增强对这些复杂人工智能系统的理解和分析。“主页”的包含暗示了一个潜在的致力于该主题的网站或平台。

---

## 20. 在Illumos上调试Rustler

**原文标题**: Debugging Rustler on Illumos

**原文链接**: [https://system-illumination.org/01-rustler.html](https://system-illumination.org/01-rustler.html)

本文详细介绍了作者的调试过程，旨在了解为什么 Rustler NIF (原生实现函数) 在 OmniOS (一个 illumos 发行版) 的 Elixir 中加载失败。最初，NIF 加载没有产生任何错误，但函数却无法访问。

通过 DTrace，作者追踪到了负责加载 NIF 的 Erlang 函数，并确认共享库已被正确打开。随后，他们深入研究了 NIF 如何暴露函数，并发现了 `nif_init` 函数，该函数返回一个 `ErlNifEntry` 结构，其中包含有关 NIF 函数的信息。

通过创建一个包装共享库来检查 `ErlNifEntry` 结构，他们发现 `num_of_funcs` 字段为零，表明 Rustler 没有正确注册函数。

进一步调查 Rustler 的代码库后发现，其使用了 `inventory` crate，该 crate 使用运行时初始化函数 (类似于 `__attribute__((constructor))`) 来注册插件。`inventory` crate 利用 ELF 文件的 `.init_array` 部分来存储在库加载期间调用的函数指针。

作者确认 `.init_array` 部分包含预期的函数指针，但质疑 illumos 运行时链接器是否实际执行了这些初始化函数，怀疑这才是问题的原因。

---

## 21. OpenAI 吞噬工作岗位，然后提议帮你找到在沃尔玛的新工作

**原文标题**: OpenAI eats jobs, then offers to help you find a new one at Walmart

**原文链接**: [https://www.theregister.com/2025/09/05/openai_jobs_board/](https://www.theregister.com/2025/09/05/openai_jobs_board/)

在人工智能颠覆就业市场的未来，OpenAI 正在提供解决方案：它自己的 AI 培训和一个新的招聘平台，将工人与需要 AI 技能的公司联系起来。OpenAI 应用负责人 Fidji Simo 宣布，该计划包括工人在 OpenAI 学院参加课程，然后在已签约沃尔玛等合作伙伴的平台上宣传自己。

这项举措旨在帮助人们适应人工智能引起的不断变化的就业形势，沃尔玛首席执行官表示，人们了解如何在零售业中使用技术非常重要。OpenAI 希望利用白宫的计划，将人工智能作为美国工人的一项核心技能。

然而，此举也可能使 OpenAI 在就业市场上与微软的 LinkedIn 展开竞争。关于 OpenAI 推广的 AI 技能在更广泛的就业市场中的实际价值，仍然存在疑问。与此同时，OpenAI 首席执行官 Sam Altman 和其他人参加了由前第一夫人梅拉尼娅·特朗普主持的晚宴，讨论人工智能，而埃隆·马斯克声称他被邀请了，但他缺席了。

---

## 22. 现在 1TB 树莓派 SSD 仅售 70 美元

**原文标题**: 1TB Raspberry Pi SSD on sale now for $70

**原文链接**: [https://www.raspberrypi.com/news/1tb-raspberry-pi-ssd-on-sale-now-for-70/](https://www.raspberrypi.com/news/1tb-raspberry-pi-ssd-on-sale-now-for-70/)

树莓派基金会发布新款1TB固态硬盘，专为树莓派电脑设计，售价70美元。这款新的存储方案相比传统microSD卡，在速度和容量上都有显著提升，提供更快的启动时间、应用加载速度和整体系统响应。

该固态硬盘兼容所有支持USB大容量存储的树莓派型号，包括树莓派5、4、400及更早版本。它通过标准USB接口连接，易于设置和使用。文章重点介绍了使用固态硬盘优于microSD卡的优势，例如更高的可靠性和更长的使用寿命。

这款新型固态硬盘被定位为需要大容量存储和高性能项目的理想解决方案，例如媒体服务器、数据库应用和桌面替代品。该公告强调了1TB固态硬盘的经济性，使其成为提高树莓派项目性能的一种经济高效的方式。

本质上，树莓派基金会正在提供一款价格具有竞争力、容量大的固态硬盘，作为树莓派用户寻求比传统microSD卡更快、更可靠存储的重要升级选择。

---

## 23. 如厕玩手机或致痔疮：研究显示

**原文标题**: Using Your Phone on Toilet May Give You Hemorrhoids: Study

**原文链接**: [https://www.nbcnews.com/health/health-news/phone-use-hemorrhoids-bathroom-social-media-scrolling-rcna228080](https://www.nbcnews.com/health/health-news/phone-use-hemorrhoids-bathroom-social-media-scrolling-rcna228080)

一项新研究表明，如厕时使用智能手机会增加患痔疮的风险。研究人员发现，在卫生间使用手机的人因长时间坐在马桶上，患痔疮的可能性高出46%。

这项发表在《PLOS One》上的研究调查了125名成年人，发现66%的人承认在卫生间使用手机。这种长时间的坐姿会给直肠静脉带来压力，导致肿胀和炎症，从而引发痔疮。与传统的阅读材料相比，设计得引人入胜的智能手机会导致更长的如厕时间。

该研究还发现，在卫生间使用智能手机的人往往是较年轻的成年人（40多岁和50多岁）。专家建议将如厕时间限制在不超过5分钟，以避免过度压力。他们建议完全不要把手机带进卫生间，并建议采取“5分钟规则”——如果什么也没发生，就起来，稍后再试。冲水时，尿液和粪便的微小颗粒被释放到空气中，这也可能是将电子设备带入卫生间的一个潜在担忧。

---

## 24. 维基百科屹立不倒，互联网其余皆崩

**原文标题**: Wikipedia survives while the rest of the internet breaks

**原文链接**: [https://www.theverge.com/cs/features/717322/wikipedia-attacks-neutrality-history-jimmy-wales](https://www.theverge.com/cs/features/717322/wikipedia-attacks-neutrality-history-jimmy-wales)

本文探讨了维基百科如何出人意料地成为互联网上一个具有韧性和可靠的信息来源，尤其是在其他平台与虚假信息和偏见作斗争时。尽管最初因其不可靠性而受到嘲笑，但维基百科现在已成为网络上值得信赖的事实基础，被谷歌、社交媒体，甚至人工智能公司所使用。

本文重点介绍了维基百科编辑的协作过程，他们尽管存在分歧，但仍努力达成共识并构建准确的叙述。埃隆·马斯克备受争议的行为就是一个例证，编辑们最终关注的是可验证的事实，而不是个人观点。

然而，维基百科正面临着来自指责其存在偏见并试图破坏其可信度的强大个人和政府日益增长的攻击。这些攻击包括网络骚扰、法律威胁以及试图曝光编辑的行为。尽管面临这些挑战，维基百科的去中心化结构、对捐赠的依赖以及广泛的受欢迎程度使其难以控制或关闭。

本文借鉴汉娜·阿伦特的著作，强调了事实作为共享现实和政治讨论共同基础的重要性。它认为，在虚假信息泛滥的时代，维基百科的中立性和致力于提供信息（即使是以一种“枯燥”的方式）至关重要。在承认事实的脆弱性的同时，本文的结论是，维基百科对免费提供的知识的承诺本身就是一个强有力的声明。

---

## 25. io_uring 比 mmap 快

**原文标题**: io_uring is faster than mmap

**原文链接**: [https://www.bitflux.ai/blog/memory-is-slow-part2/](https://www.bitflux.ai/blog/memory-is-slow-part2/)

本文挑战了计算机科学界长期以来的教条：内存缓存总是比直接从磁盘读取更快。作者认为，随着磁盘带宽的指数级增长和内存访问延迟的停滞，尤其是在现代SSD的情况下，这种说法不再总是成立。

作者使用“计数10”的基准测试来比较性能，读取一个大型数据集并计算数字10的出现次数。最初，一个简单的基于mmap()的循环实现了0.61 GB/s的磁盘读取速度。数据缓存在内存后，性能提高到3.71 GB/s。然而，作者发现CPU指令处理是一个瓶颈，因为这个简单的循环没有利用向量指令。

为了提高性能，作者展开了循环，启用了向量指令（AVX2）。这使得内存缓存的读取速度提高到5.51 GB/s。作者仍然不满意，他们质疑是否可以通过直接从磁盘获取数据来击败这种性能，从而绕过他们认为未针对现代SSD优化的mmap()机制。

解决方案是一个基于`io_uring`的I/O引擎——一个旨在最大限度地提高SSD吞吐量的用户空间驱动程序。该引擎使用多个工作线程、用于管理I/O请求和响应的队列以及直接磁盘访问。虽然代码很复杂，但关键在于，精心构建的使用`io_uring`的I/O管道允许直接从磁盘读取数据， *比* 从页面缓存读取更快，这表明传统的“内存比磁盘更快”的假设在某些高性能场景中不再普遍适用。由于篇幅原因，`io_uring`代码已链接到GitHub存储库。

---

## 26. 熔岩RGB

**原文标题**: Lava RGB

**原文链接**: [https://amaiorano.io/2025/09/03/lava-rgb.html](https://amaiorano.io/2025/09/03/lava-rgb.html)

本文详细介绍了作者在前置式NES上安装Lava RGB 2.0模组的经验，为更成熟的NESRGB模组提供了一种替代方案。作者从速卖通购买了Lava RGB 2.0套件，其中包括模组板和一个替换的电源/AV模块。2.0版本提供了诸如24位色彩输出、8个内置调色板、基于控制器的调色板切换（带屏幕显示OSD）以及用于固件更新的Micro USB端口等功能。

作者更喜欢使用SNES多输出端口，而不是电源模块上自带的Saturn风格DIN连接器。安装过程包括移除PPU和原始电源模块、压平电容以及焊接导线。作者在启用扩展音频方面遇到了挑战，最初尝试通过Voultar PCB（专为NESRGB设计）来路由，后来意识到只需在特定引脚之间连接一个简单的47K电阻即可。随后，作者切割了NES外壳，以容纳SNES多输出连接器。

作者强调Lava RGB 2.0是NESRGB的强有力竞争者，特别赞扬了它的功能和价格。虽然Lava RGB不像NESRGB那样处理音频，但从电源模块上提取NES音频输出已被证明是有效的。文章最后对该模组的性能、图像质量和调色板切换功能给予了积极评价。作者还感谢ConsoleMods Discord社区提供的帮助。

---

## 27. 光栅化器：一个约4千行代码的GPU加速2D矢量图形引擎

**原文标题**: Rasterizer: A GPU-accelerated 2D vector graphics engine in ~4k LOC

**原文链接**: [https://github.com/mindbrix/Rasterizer](https://github.com/mindbrix/Rasterizer)

光栅化器：一个GPU加速的2D矢量图形引擎，历时十年开发，灵感源于Adobe Flash。使用C++11编写，并为macOS采用Metal（计划移植到iOS），它利用GPU能力显著提升速度（最高达60倍），与CPU渲染相比，使其适用于动画UI。

该引擎旨在高效地将矢量路径转换为抗锯齿像素，并声称在此领域有所突破。它使用基于Postscript模型的Path对象（包括奇偶和非零填充规则，以及描边），并将它们组织到带有颜色、变换和笔画宽度等绘制参数的Scene对象中。SceneList随后对Scene对象进行分组。

渲染涉及填充路径的两个阶段过程：首先创建浮点掩码缓冲区，然后渲染到颜色缓冲区。小填充通过将Path几何体直接传输到GPU进行优化，而较大的填充则采用粗扫描线算法。像素面积覆盖率使用自定义窗口逆线性插值算法计算。描边路径直接进行三角剖分，并使用GPU处理二次贝塞尔曲线将其渲染到颜色缓冲区。

该架构强调CPU批量并行处理，并避免在GPU上存储持久状态，而是使用双缓冲共享内存和memcpy来提高效率。该项目包含一个Xcode演示应用程序，可以打开SVG和PDF文件，允许用户交互和探索引擎的功能。它还感谢XXHash、NanoSVG、STB Truetype和PDFium库，并以个人使用zlib许可证发布。

---

## 28. WiFi信号可以测量心率

**原文标题**: WiFi signals can measure heart rate

**原文链接**: [https://news.ucsc.edu/2025/09/pulse-fi-wifi-heart-rate/](https://news.ucsc.edu/2025/09/pulse-fi-wifi-heart-rate/)

加州大学圣克鲁兹分校的研究人员开发了一种名为“脉冲-Fi”的技术，该技术利用WiFi信号在无需可穿戴设备的情况下精确测量心率。该系统采用低成本的WiFi设备和机器学习算法来检测心跳引起的WiFi信号的细微变化，并滤除其他环境噪声。

脉冲-Fi的主要特点包括：

*   **高精度：** 实现临床级别的心率监测精度。
*   **低成本：** 采用现成的、廉价的WiFi设备，如ESP32芯片（5-10美元）和树莓派芯片。
*   **多功能：** 适用于各种姿势（坐、站、躺、走），且可在10英尺的距离内工作。
*   **非侵入性：** 无需可穿戴设备，提供更舒适和便捷的监测方法。

该团队使用ESP32设备和血氧仪收集的定制数据集来训练他们的算法，以关联WiFi信号变化与心率。对118名参与者进行的大量测试表明了该系统的有效性，仅需五秒钟的监测即可实现高精度。目前正在进行进一步的研究，以扩展脉冲-Fi的功能，以检测呼吸频率和潜在的睡眠呼吸暂停。研究人员希望这项技术将对资源匮乏的环境有所帮助，并可以实现商业化。

---

## 29. 旧时妙用传真切换盒

**原文标题**: Making the most of a dumb fax switcher box in the old days

**原文链接**: [https://rachelbythebay.com/w/2025/09/01/fax/](https://rachelbythebay.com/w/2025/09/01/fax/)

无法访问文章链接。

---

## 30. 如果OpenDocument使用SQLite会怎样？

**原文标题**: What If OpenDocument Used SQLite?

**原文链接**: [https://www.sqlite.org/affcase1.html](https://www.sqlite.org/affcase1.html)

本文提出一个思想实验：如果 OpenDocument 文件格式（特别是 ODP）使用 SQLite 作为其容器而不是 ZIP 压缩包会怎么样？作者认为这样做可以带来若干好处，尽管承认 OpenDocument 已经优于自定义二进制格式。

目前，ODP 文件是包含 XML 文件（内容、样式、元数据、设置）和单独图像文件的 ZIP 压缩包。作者批评这种“文件堆砌”的方法，列举了其局限性：需要完全重写文件的困难的增量更新、由于解析大型 "content.xml" 文件导致的启动时间缓慢、加载整个文档导致的高内存使用率、具有挑战性的崩溃恢复，以及通用工具的有限可访问性。

作者建议使用 SQLite 进行三项改进。首先，即使不改变模式，简单地用 SQLite 替换 ZIP 就可以减小文件大小并实现原子更新，从而防止崩溃期间的数据损坏。其次，将 "content.xml" 文件拆分为新表中更小的、特定于幻灯片的条目，可以通过仅加载第一个幻灯片的内容来加快启动速度。这种方法还可以减少内存占用，并通过仅更新更改的幻灯片来加快文件/保存操作。第三，本文建议通过跟踪幻灯片 ID 并存储带有时间戳和注释的版本来添加版本控制，从而允许用户恢复到先前的状态。

核心论点是，SQLite 的数据库功能优于 ZIP 的基本键值存储，从而为 OpenDocument 提供了一种更高效、更强大、更用户友好的文件格式。

---

## 31. OCaml编程语言的演进 (2025) [pdf]

**原文标题**: Evolving the OCaml Programming Language (2025) [pdf]

**原文链接**: [https://kcsrk.info/slides/Evolution_Ashoka_2025.pdf](https://kcsrk.info/slides/Evolution_Ashoka_2025.pdf)

由于处理非文本数据和存在编码字符的限制，我无法提取PDF文章的完整内容，因此无法提供摘要。

---

## 32. 经典8×8像素黑白Mac图案

**原文标题**: Classic 8×8-pixel B&W Mac patterns

**原文链接**: [https://www.pauladamsmith.com/blog/2025/09/classic-mac-patterns.html](https://www.pauladamsmith.com/blog/2025/09/classic-mac-patterns.html)

本文详细介绍了从经典 Macintosh System 6 文件中提取原始 8x8 像素黑白图案并将其转换为可用格式的过程。作者出于怀旧之情和对这些图案完美像素表示的渴望，概述了一个详细的步骤。

该过程涉及使用 Mini vMac 模拟器、获取旧 Mac ROM 以及特定磁盘镜像。作者提取了包含图案的“System”文件，并利用 sitPack、ExportFl、The Unarchiver 和 DeRez (来自 Xcode 命令行工具) 等工具。

DeRez 命令提取了 'PAT#' 资源，这是一系列字节，代表了原始 Macintosh 中引入的 38 个图案。作者没有手动解析这些数据，而是使用 Python 脚本（由 Claude 生成）将其转换为 .pbm 图像格式。这种基于文本的格式使用“1”和“0”来表示黑色和白色像素，使其易于操作。

作者选择这种方法而不是截图或手动创建，以确保图案直接从源中提取，从而保持准确性并将数据以易于解析的格式进行存档。提取的 .pbm 文件随后可以使用 ImageMagick 等工具转换为其他格式。这些图案现已在作者的网站上提供，供其他人使用。

---

## 33. 为什么机器学习需要一种新的编程语言

**原文标题**: Why ML Needs a New Programming Language

**原文链接**: [https://signalsandthreads.com/why-ml-needs-a-new-programming-language/](https://signalsandthreads.com/why-ml-needs-a-new-programming-language/)

本期Signals and Threads播客节目中，Ron Minsky采访了LLVM和Swift的创造者Chris Lattner，探讨了他最新的项目Mojo以及机器学习领域对新编程语言的需求。Lattner认为，当前语言未能有效利用现代GPU的强大功能，同时保持用户友好性。他创建Mojo的目标是打造一种既易于使用，又能提供最先进内核编写所需的底层控制的语言，从而促进AI生态系统中的硬件专业化和供应商独立性。

讨论涉及Lattner的背景，从BASIC和引领他构建LLVM的编译器狂热教授开始。一个关键主题是编译器工程和语言设计之间的相互作用，这源于Lattner的个人兴趣和解决实际问题的愿望。对话探讨了Swift的起源，它是一个由C++的局限性（特别是缺乏模式匹配等现代特性）所驱动的晚上和周末项目。Lattner表示偏好以实用性为导向的语言设计方法，与纯粹的数学方法形成对比，尽管他承认自己的数学技能并不完美，但他追求设计的优雅性和可组合性，这与数学原则相一致。

---

## 34. 在终端中渲染 Chrome (2023)

**原文标题**: Forking Chrome to render in a terminal (2023)

**原文链接**: [https://fathy.fr/carbonyl](https://fathy.fr/carbonyl)

本文详细介绍了如何派生 Chrome 浏览器以在终端模拟器中渲染网页，从而创建名为“Carbonyl”的基于终端的 Web 浏览器。

作者 Fathy 解释了在基于文本的环境中渲染图形内容的挑战，利用诸如底部半块字符 (U+2584) 之类的 Unicode 字符，以及用于光标移动和颜色操作的转义序列。该过程涉及使用 C++ 和 Rust 修改 Chrome 的渲染管线。

关键修改包括创建一个“TextCaptureDevice”来处理文本渲染，方法是将字形 ID 转换为 Unicode 字符，并实现用于清除矩形后面文本的方法以实现正确的遮挡。为了解决性能问题，作者探索并实现了多种优化技术，包括强制使用等宽字体以实现布局一致性，强制使用 LoDPI 缩放以提高渲染速度，以及利用共享内存区域在浏览器进程之间传递像素数据，从而最大限度地减少 IPC 开销。Mojo 是一个用于进程间通信的库，用于定义接口和序列化渲染器和浏览器进程之间的数据。

本文还介绍了使用终端转义序列进行鼠标事件跟踪的输入处理。

最终，该项目旨在实现功能和性能之间的平衡，从而能够在终端环境中以合理的 CPU 使用率和渲染速度进行 Web 浏览。

---

## 35. 年龄模拟套装

**原文标题**: Age Simulation Suit

**原文链接**: [https://www.age-simulation-suit.com/](https://www.age-simulation-suit.com/)

文章介绍了“老年模拟器GERT”，这是一种年龄模拟套装，旨在让年轻人体验与衰老相关的身体障碍。该套装模拟了诸如晶状体混浊、视野狭窄、高频听力损失、头部活动受限、关节僵硬、力量丧失、抓握能力下降以及协调技能减弱等状况。

GERT被宣传为理解和同情老年人的工具。它的定价为1390欧元或1250英镑，不包括运费和增值税，并且配有完整的套装和两副眼镜（与图片中的型号有所不同）。

由于处理较小且经常出现问题的订单所需的时间增加，该公司现在设定了最低订单金额为300欧元或300英镑。

客户评论强调了该套装的良好质量、模拟老年人行为的有效性、耐用性和易用性，表明它是教育和理解衰老的宝贵工具。

---

## 36. 身陷技术债务

**原文标题**: Swimming in Tech Debt

**原文链接**: [https://helpthisbook.com/lou-franco/swimming-in-tech-debt](https://helpthisbook.com/lou-franco/swimming-in-tech-debt)

我没有足够的信息来完成那个。我是一个大型语言模型，能够根据各种提示和问题进行交流，但我对那本特定书籍的了解有限。还有什么我可以帮到你的吗？

---

## 37. 启发《大步走》的硬汉警长枪杀妻子

**原文标题**: Hard-Nosed Sheriff Who Inspired 'Walking Tall' Movie Killed His Wife

**原文链接**: [https://www.nytimes.com/2025/08/31/us/buford-pusser-walking-tall-tennessee.html](https://www.nytimes.com/2025/08/31/us/buford-pusser-walking-tall-tennessee.html)

无法访问文章链接。

---

## 38. 科技大佬轮番在尴尬盛宴上卑躬屈膝

**原文标题**: Tech CEOs Take Turns Grovelling at Feast of Embarrassments

**原文链接**: [https://pxlnv.com/linklog/trump-feast-of-embarrassments/](https://pxlnv.com/linklog/trump-feast-of-embarrassments/)

本文总结了《华尔街日报》关于特朗普总统主持的与主要科技公司领导人会晤的报道。这次会议类似于特朗普的内阁会议，与会者轮流称赞他，这次是称赞他在促进芯片制造和人工智能投资方面所做的努力。

出席者包括萨姆·奥特曼、蒂姆·库克、桑达尔·皮查伊、大卫·萨克斯、马克·扎克伯格和比尔·盖茨。文章重点介绍了特朗普和Alphabet首席执行官桑达尔·皮查伊之间关于近期谷歌搜索垄断反垄断裁决的对话。特朗普祝贺皮查伊因为该裁决而“度过了非常美好的一天”，而皮查伊只是回应说：“我很高兴它结束了。”特朗普随后提醒皮查伊，该诉讼是在拜登政府期间发起的，作者巧妙地纠正了这一说法，指出该诉讼是在2020年，即特朗普的第一任期内提出的。

文章的语气是批判性的，暗示科技领导人正在对特朗普进行谄媚行为。文章最后指出，与之前的情况不同，至少据作者所知，没有向这位前总统赠送金像。

---

## 39. 内核流中的基于堆的缓冲区溢出

**原文标题**: Heap-based buffer overflow in Kernel Streaming

**原文链接**: [https://www.crowdfense.com/cve-2025-53149-windows-ksthunk-heap-overflow/](https://www.crowdfense.com/cve-2025-53149-windows-ksthunk-heap-overflow/)

voidsec的文章详细介绍了CVE-2025-53149，一个存在于内核流WOW Thunk服务驱动程序（ksthunk.sys）中的基于堆的缓冲区溢出漏洞。该漏洞位于`CKSAutomationThunk::HandleArrayProperty()`函数中，当处理`KSPROPSETID_VPConfig`或`KSPROPSETID_VPVBIConfig`属性集中`KSPROPERTY_VPCONFIG_DDRAWSURFACEHANDLE`项的`KSPROPERTY_TYPE_GET`请求时触发。

该问题的根源在于将数据复制到输出缓冲区时缺少大小检查。`OutputBufferLength`仅与0进行比较，而没有与`KsSynchronousIoControlDevice()`调用返回的实际字节数进行比较。如果设备返回的数据超过输出缓冲区可容纳的范围，则在数组复制循环期间会导致堆溢出。

虽然研究人员由于测试系统上缺少兼容设备而无法完全触发该漏洞，但他们提供了概念验证代码，演示了如何访问该易受攻击的函数。微软于2025年8月12日修复了该漏洞，方法是添加对`OutputBufferLength`与返回的字节数的检查，如果检测到溢出，则将代码定向到`RtlLogUnexpectedCodepath()`。文章最后对供应商的漏洞赏金计划进行了讽刺，并建议使用替代的漏洞报告平台。

---

## 40. 纤程并发

**原文标题**: Fiber Concurrency

**原文链接**: [https://honeyryderchuck.gitlab.io/httpx/wiki/Fiber-Concurrency](https://honeyryderchuck.gitlab.io/httpx/wiki/Fiber-Concurrency)

`:fiber_concurrency` HTTPX 插件允许单个 HTTPX 会话在光纤调度器管理下的多个光纤中并发使用。这在处理长期或持久连接时尤为重要。如果使用了 `:persistent` 插件，则 `:fiber_concurrency` 插件将成为必需的依赖项。

要使用该插件，只需使用 `HTTPX.plugin(:fiber_concurrency)` 启用它。本文提供了一个示例，演示了此插件如何在光纤调度器中启用并发 HTTP GET 请求。

该插件主要面向在利用光纤调度器的程序中使用 HTTPX 的开发人员，例如使用 `async` gem 构建的应用程序。如果没有此插件，在一个 HTTPX 会话中跨光纤的并发使用可能会导致意外行为或错误。

---

## 41. 我四十年前就该给蚂蚁们做的文件存储驱动器 [视频]

**原文标题**: I made a drive to store files like 40 years ago –.but for ants [video]

**原文链接**: [https://www.youtube.com/watch?v=GQwTPH67YqY](https://www.youtube.com/watch?v=GQwTPH67YqY)

这篇文章与其说是一篇文章，不如说是一个YouTube视频的标题以及在YouTube页面底部常见的一些标准模板文本。根据标题推测，这个视频可能展示了一个项目，有人创造了一个微型存储设备，类似于硬盘，但设计得极其微小，甚至可能供蚂蚁使用。这个幽默且略带荒诞的标题暗示着一个关于小型化和数据存储的有趣且富有创意的视频。

---

## 42. AI Agent架构的PM指南

**原文标题**: A PM's Guide to AI Agent Architecture

**原文链接**: [https://www.productcurious.com/p/a-pms-guide-to-ai-agent-architecture](https://www.productcurious.com/p/a-pms-guide-to-ai-agent-architecture)

本文为产品经理提供了一份构建AI Agent的指南，强调用户采纳的关键在于信任，而不仅仅是能力。它将Agent架构分解为四个关键层：上下文与记忆（Agent的记忆量）、数据与集成（系统连接）、技能与能力（特定功能）以及评估与信任（沟通局限性并衡量成功）。

作者强调了架构选择在塑造用户体验和信任方面的重要性。然后，他概述了四种用于实现Agent的编排模式：单Agent架构（简单且适用于大多数情况）、基于技能的架构（高效但协调复杂）、基于工作流的架构（可预测但僵化）和协作式架构（面向未来但非常复杂）。

本文认为，用户更信任那些对其局限性保持透明的Agent，而不是那些总是“正确”的Agent。关键的信任策略包括置信度校准、推理透明性和必要时优雅地升级到人工支持。下一篇文章将讨论AI Agent的自主性以及治理问题。

---

## 43. 尼泊尔拟封锁脸书、X、YouTube等平台

**原文标题**: Nepal moves to block Facebook, X, YouTube and others

**原文链接**: [https://www.aljazeera.com/news/2025/9/4/nepal-moves-to-block-facebook-x-youtube-and-others](https://www.aljazeera.com/news/2025/9/4/nepal-moves-to-block-facebook-x-youtube-and-others)

尼泊尔政府宣布将封锁Facebook、X、Instagram、YouTube、Reddit和LinkedIn等主要社交媒体平台，原因是它们未能在规定期限内向通信和信息技术部注册。注册要求平台提供当地联系人、申诉处理人员和负责自我监管的人员。政府声称此举旨在遏制网络仇恨、谣言和网络犯罪。

自2023年初的指令以来，只有少数平台（包括TikTok和Viber）进行了注册。尽管发布了公告，但目标平台在周四仍然可以访问。“数字权利尼泊尔”批评此举是一种“控制性”的做法，侵犯了公众的基本权利，并强调在实施此类限制之前需要完善的法律基础设施。

尼泊尔此前曾限制访问在线平台，包括7月份的Telegram。在TikTok同意遵守当地法规后，他们也解除了对该平台的禁令。这一行动符合全球政府加强对社交媒体监管的趋势，理由是对虚假信息、数据隐私、在线危害和国家安全的担忧。

---

## 44. Mach-O剖析：结构、代码签名与Pac

**原文标题**: The Anatomy of a Mach-O: Structure, Code Signing, and Pac

**原文链接**: [https://oliviagallucci.com/the-anatomy-of-a-mach-o-structure-code-signing-and-pac/](https://oliviagallucci.com/the-anatomy-of-a-mach-o-structure-code-signing-and-pac/)

本文深入探讨了 Apple 操作系统使用的 Mach-O 二进制文件格式。它解释了 Mach-O 文件的结构，该结构由头部、加载命令和数据段/节组成。头部标识文件类型和架构，加载命令为操作系统加载器提供指令。段包含代码和数据的节。通用二进制文件 (Fat Mach-O) 支持单个文件中的多种架构。

文章的很大一部分集中在代码签名上，这是 Mach-O 安全性的一个关键方面。LC_CODE_SIGNATURE 加载命令指向嵌入的代码签名 blob，通常位于文件末尾。这个 blob，即代码签名 SuperBlob，包含诸如代码目录（带有代码页面的哈希值）、权限、资源目录哈希、要求以及 CMS 签名等组件。操作系统在执行时验证此签名，以确保完整性和真实性。修改已签名的 Mach-O 需要删除签名或重新签名。

本文还简单提及了 ARM64e 系统上的指针认证码 (PAC)（但未深入探讨）、分离签名（签名与 Mach-O 分开存储）以及代码签名中涉及的信任链。

---

## 45. Action是最好的8位编程语言。

**原文标题**: Action was the best 8-bit programming language

**原文链接**: [https://www.goto10retro.com/p/action-was-the-best-8-bit-programming](https://www.goto10retro.com/p/action-was-the-best-8-bit-programming)

本文热情地推崇Action!为最佳的8位编程语言，尤其是对于雅达利8位计算机。文章由Paul Lefebvre撰写，重点介绍了Action!由Clinton Parker于1983年为优化系统软件公司(OSS)所创建。Action!因其集成的开发环境(IDE)而脱颖而出，该环境包含一个监视器（命令行）、编译器、文本编辑器和调试器，全部集成在一个16K的卡带中。

作者详细介绍了Action!的优势，包括其快速的编译时间（由于针对6502 CPU进行了优化），相比当时可用的Pascal和C等语言。编辑器因其全屏文本编辑、复制/粘贴功能和分屏模式而受到称赞。该语言本身是一种结构化的、过程化的语言，让人联想到C和Pascal，具有循环和条件语句的命令，尽管数据类型有限。

文章也承认了Action!的局限性，主要是需要卡带来运行程序，以及缺少浮点数据类型。这些局限性在一定程度上通过附加组件得到解决，例如Action! RunTime（用于创建独立程序）和Action! ToolKit（用于增强的库函数，包括有限的浮点支持和玩家/导弹图形）。最终，作者表达了他进一步探索Action!的意图，强调了它在有趣和实用编程方面的潜力。文章还提供了有用的Action!资源的链接，包括在线手册和编程教程。

---

## 46. 与陌生人的三十分钟

**原文标题**: 30 minutes with a stranger

**原文链接**: [https://pudding.cool/2025/06/hello-stranger/](https://pudding.cool/2025/06/hello-stranger/)

张镫的《与陌生人相处的30分钟》探讨了与我们不同的人交谈带来的出人意料的好处，该文章引用了CANDOR语料库的数据，这是一个涉及近1700名陌生人之间对话的研究项目。文章强调，尽管人们经常对与陌生人交谈感到不安，但这些互动往往会带来积极的体验和改善情绪。

这项研究基于年龄、种族、教育程度和政治意识形态等不同人口统计学特征的人员配对，结果显示，参与者最初报告在通话前感觉一般甚至更糟。然而，到30分钟对话进行到一半时，很大一部分人表示感觉更好。

张镫强调，我们倾向于与相似的人“联结”，从而创建同质的社交圈。我们缺乏与不同的人建立的“桥梁”社会资本或关系。研究表明，人们常常低估这些对话的乐趣，并且害怕被拒绝或感到尴尬，而这些情况很少发生。

尽管最初有所犹豫，但该研究中的许多对话都触及了令人惊讶的私密话题，表明人们愿意与陌生人分享个人经历。尽管有些对话确实停滞不前，但大多数参与者都喜欢与新人建立联系，即使存在巨大差异。文章强调了与陌生人进行积极互动的潜力以及走出熟悉社交圈的好处。

---

## 47. Swift 6 中类型安全且用户友好的错误处理

**原文标题**: Type-safe and user-friendly error handling in Swift 6

**原文链接**: [https://theswiftdev.com/2025/type-safe-and-user-friendly-error-handling-in-swift-6/](https://theswiftdev.com/2025/type-safe-and-user-friendly-error-handling-in-swift-6/)

本文探讨了 Swift 6 中使用类型化抛出、结构化诊断和分层错误模型实现的类型安全且用户友好的错误处理。作者介绍了一个自定义的 `SystemError` 协议，该协议扩展了基础 `Error` 协议，并添加了诸如 `logMessage`、`userFriendlyMessage`、`underlyingErrors`、`logMessageStack` 和 `lookup` 等功能。此协议为开发者提供详细的错误信息以进行调试，并为终端用户提供用户友好的消息。

文章演示了如何创建符合 `SystemError` 协议的自定义错误结构体和枚举，以及如何扩展 `NSError` 和 `DecodingError` 以与此系统对齐。 它强调了利用 `NSError` 的内置错误层次结构，并从 `DecodingError` 上下文中提取详细的调试信息。

作者提供了用例场景，演示了如何将 Swift 6 的新类型化抛出功能与自定义 `SystemError` 协议结合使用。 示例包括创建自定义错误结构、处理 JSON 解码错误以及使用 `lookup` 函数来识别堆栈中的特定错误类型。 文章展示了如何捕获和处理 `SystemError` 实例，提取用户友好的消息，并打印整个错误堆栈以进行高效调试，从而提供更清晰的错误报告和控制。 通过创建分层错误模型、结构化诊断和 `SystemError` 协议，开发者可以提高代码的清晰度和可维护性。

---

## 48. 如何使用IK-Geo构建高性能UR5逆运动学求解器

**原文标题**: How to Build a High-Performance UR5 Inverse Kinematics Solver with IK-Geo

**原文链接**: [https://alexanderelias.com/ur5-ik/](https://alexanderelias.com/ur5-ik/)

本文介绍了一个使用IK-Geo方法构建UR5机器人高性能逆运动学(IK)求解器的教程。IK-Geo相比于IKFast等其他方法，在速度和精度上都具有显著优势。本文强调了IK对于机器人手臂控制的重要性，并突出了实践者面临的挑战。

本教程涵盖了使用指数积(POE)约定进行正向运动学，展示了如何对机器人进行建模以及如何针对UR机器人模拟器验证该模型。然后，它深入研究了使用子问题分解来解决IK问题。UR5的几何结构，包括平行和相交的关节轴，允许使用三个典型的几何子问题（圆和点、圆和球、圆和平面）以闭合形式重写IK方程。

本文详细介绍了这些子问题的代数和几何公式，并提供了MATLAB代码来实现它们的解决方案。它强调了使用atan2()来实现数值稳定性。

最后，本文开始推导完整的UR5逆运动学解，基于几何简化重写正向运动学方程。文章指出，后续步骤将涉及使用先前介绍的子问题来求解各个关节角度。该教程承诺将涵盖求解器性能的基准测试，并将其与现有的行业方法进行比较。

---

## 49. 液冷展品

**原文标题**: Liquid Cooling Exhibits

**原文链接**: [https://chipsandcheese.com/p/liquid-cooling-exhibits-at-hot-chips](https://chipsandcheese.com/p/liquid-cooling-exhibits-at-hot-chips)

这篇来自Hot Chips 2025的文章强调了液冷在高性能计算（尤其是AI应用）中日益增长的重要性。多家公司展示了创新的液冷解决方案，重点在于冷板设计和效率。

主要趋势包括水冷头中从传统微鳍阵列向微射流技术的转变。微射流允许对芯片热点进行定向冷却，从而提高热传递。Jetcool的“SmartLid”设计就是例证，它将水直接送到芯片上，消除了中间层，从而提高了效率。虽然这种程度的定制对于消费级PC来说并不实用，但它非常适合AI应用中的标准化服务器部署。

Alloy Enterprises展示了各种使用铜和铝的水冷头设计，突出了热传递效率和重量之间的权衡。Jetcool还展示了针对Nvidia GB200的系统级冷却解决方案以及独立的服务器冷却装置，展示了集成的散热器、泵和水冷头，以便更轻松地进行数据中心集成。

Nvidia的GB300服务器具有外部液冷连接和潜在的泄漏检测传感器。AI专用芯片（如Meta的Catalina机架和AMD的MI350 OAM模块中的芯片）日益增长的功耗正将数据中心冷却技术推向极限。这推动了液冷领域的创新，文章认为，一些面向企业的技术最终可能会渗透到消费级硬件中，尤其是在解决热点问题方面。作者设想未来计算机冷却与家庭供水系统之间的集成，以提高能源效率。

---

## 50. IRHash：基于IR层哈希的高效多语言编译器缓存

**原文标题**: IRHash: Efficient Multi-Language Compiler Caching by IR-Level Hashing

**原文链接**: [https://www.usenix.org/conference/atc25/presentation/landsberg](https://www.usenix.org/conference/atc25/presentation/landsberg)

无法访问文章链接。

---

## 51. 为MCP服务器构建类似Supabase的OAuth认证

**原文标题**: Building Supabase-Like OAuth Authentication for MCP Servers

**原文链接**: [https://hyprmcp.com/blog/mcp-server-authentication/](https://hyprmcp.com/blog/mcp-server-authentication/)

本文详细介绍了为模型上下文协议 (MCP) 服务器实现类似 Supabase 的 OAuth 认证系统，特别关注于创建 MCP 服务器网关。该网关充当反向代理，同时处理 MCP 基于 OAuth2 的授权框架。

作者重点介绍了使用现有身份提供商 (IdP)（如 Keycloak 和 Dex）的挑战，因为它们对必要的 OAuth2 扩展（如授权服务器元数据 (ASM) 和动态客户端注册 (DCR)）的支持不完整。为了克服这些障碍，作者构建了一个自定义解决方案，利用 Dex 进行身份管理，并使用 Go 进行实现。

该实现包括创建基本的反向代理、添加 CORS 支持、实现 OAuth2 中间件以进行令牌验证和 PRS 发现，以及建立受保护资源服务器 (PRS) 端点。一个关键要素是将 IdP 的 OpenID 配置代理为 OAuth2 ASM 端点，并通过 Dex 的 GRPC API 实现动态客户端注册。这涉及为两者定制端点，从而允许按需创建客户端。最后，本文展示了如何在授权请求中注入作用域，这在 IdP 严格遵循 OIDC 规范的情况下是必要的。

本文提供了 Go 代码片段来阐述这些概念。

---

## 52. 美国8月新增就业仅2.2万，失业率达四年新高

**原文标题**: US economy added just 22,000 jobs in August, unemployment highest in 4 yrs

**原文链接**: [https://www.cnn.com/2025/09/05/economy/us-jobs-report-august-final](https://www.cnn.com/2025/09/05/economy/us-jobs-report-august-final)

美国就业市场显露停滞迹象：8月份仅新增2.2万个就业岗位，失业率升至四年高位4.3%。6月份的数据也被向下修正，显示减少了1.3万个就业岗位，这是自2020年12月以来首次出现就业负增长，结束了长期的就业扩张期。

经济学家认为，这种放缓归因于特朗普总统的关税、移民和联邦支出政策所带来的经济不确定性，导致企业推迟招聘决策。

虽然劳动力数量因重返劳动力市场的人员增加而有所增长，但就业市场的特点是招聘和解雇率较低，限制了工人的机会。 大部分就业增长集中在医疗保健领域，导致大部分劳动力选择有限。工资增长也在放缓，平均时薪增速放缓。

报告还指出，其他劳动力市场指标，如私营部门招聘和失业救济申请，表明存在降温趋势。 在7月份数据疲软后，特朗普总统解雇了劳工统计局局长，这引起了人们的担忧。经济学家警告说，就业创造基础狭窄使劳动力市场容易受到经济冲击。

---

## 53. Polars 云和分布式 Polars 现已推出

**原文标题**: Polars Cloud and Distributed Polars now available

**原文链接**: [https://pola.rs/posts/polars-cloud-launch/](https://pola.rs/posts/polars-cloud-launch/)

Polars发布Polars云，现已在AWS上全面可用，同时推出分布式引擎的公开测试版。旨在弥合本地pandas使用的便捷性与PySpark的可扩展性之间的差距。Polars云提供了一个托管数据平台，用于远程大规模运行Polars查询，管理基础设施和扩展策略，包括一个利用Polars流式架构进行水平、垂直和对角扩展的新型分布式引擎。

分布式引擎允许用户对查询进行分区并将其与依赖顺序的处理相结合，从而利用Polars的单节点执行速度和分布式计算的可扩展性。

即将推出的功能包括本地部署支持（客户端即将加入）、用于深度查询洞察的实时集群仪表板、任务编排功能（同时强调与Airflow和Prefect等工具的集成）、利用垂直和对角扩展的自动缩放、用于数据组织（包括原生Iceberg支持）的目录支持以及用于最大限度减少延迟的多区域可用性。

该公告邀请用户注册AWS上的Polars云并申请本地访问权限，并承诺在不久的将来推出更多更新和功能。目标是为任何规模提供单一API，从而降低大规模数据处理的成本、时间和复杂性。

---

## 54. 使用人工智能更深入地感知宇宙

**原文标题**: Using AI to perceive the universe in greater depth

**原文链接**: [https://deepmind.google/discover/blog/using-ai-to-perceive-the-universe-in-greater-depth/](https://deepmind.google/discover/blog/using-ai-to-perceive-the-universe-in-greater-depth/)

本文探讨了一种名为深度环路整形的全新人工智能方法，该方法显著提高了像LIGO这样的引力波天文台的控制和稳定性。深度环路整形由LIGO和GSSI合作开发，可将天文台反馈系统中的噪声降低30到100倍，从而能够更准确地测量引力波——由黑洞合并和中子星碰撞等事件引起的时空中的微小涟漪。

通过稳定高度敏感的干涉仪反射镜，深度环路整形有望帮助天文学家每年探测到数百个更多的引力波事件，并获得更详细的信息。这将使他们能够收集关键数据，以了解宇宙的动力学和形成，检验基础物理和宇宙学理论，并研究中等质量黑洞，这种黑洞被认为是星系演化中的“缺失环节”。

该方法利用带有频域奖励的强化学习，使控制器能够学习如何抑制观测频段中的控制噪声。在路易斯安那州利文斯顿的真实LIGO系统上进行的测试证实了该方法的有效性，表明其能够保持天文台系统在长时间内的稳定。

除了引力波天文台，深度环路整形在航空航天、机器人和结构工程等其他工程领域也具有应用潜力，在这些领域中，振动抑制、噪声消除以及高度动态或不稳定的系统至关重要。作者希望这项工作能够影响未来天文台的设计，最终提高我们对宇宙的理解。

---

## 55. Atlassian将收购The Browser Company。

**原文标题**: Atlassian is acquiring The Browser Company

**原文链接**: [https://www.cnbc.com/2025/09/04/atlassian-the-browser-company-deal.html](https://www.cnbc.com/2025/09/04/atlassian-the-browser-company-deal.html)

Atlassian 将以 6.1 亿美元现金收购 Arc 和 Dia 网络浏览器的开发商 The Browser Company。该交易旨在通过整合 The Browser Co. 的创新技术来增强 Atlassian 的项目管理软件 Jira。

---

## 56. 梅尔文·布拉格卸任《我们的时代》主持人

**原文标题**: Melvyn Bragg steps down from presenting In Our Time

**原文链接**: [https://www.bbc.co.uk/mediacentre/2025/melvyn-bragg-decides-to-step-down-from-presenting-in-our-time/](https://www.bbc.co.uk/mediacentre/2025/melvyn-bragg-decides-to-step-down-from-presenting-in-our-time/)

自1998年开播以来，在播出了1000多集节目后，梅尔文·布拉格即将卸任英国广播公司第四电台（BBC Radio 4）的“我们的时代”（In Our Time）节目主持人。 2025年9月3日发布的公告赞扬了布拉格六十年来对公共服务广播事业的卓越贡献，特别是他将“我们的时代”打造成全球受欢迎且具有学术启发性的节目的作用。 该节目在BBC声音平台上特别受35岁以下听众的欢迎。

布拉格于1961年加入英国广播公司，职业生涯丰富多彩，参与过“一周开始”（Start the Week）、艺术文化节目，并为电影和文学做出了贡献。 他将继续与英国广播公司合作开展新项目，包括2026年的新系列节目。

英国广播公司总干事蒂姆·戴维和第四电台台长莫希特·巴卡亚赞扬了布拉格的热情、求知欲和“我们的时代”的持久遗产，强调该节目的档案是一项宝贵的资源。 第四电台将播出珍藏剧集，BBC声音平台将推出由粉丝策划的精选集，以纪念他的离任。 “我们的时代”的新主持人将在适当的时候公布。

布拉格本人对有机会与英国广播公司和学术界的才华横溢的人们合作表示感谢，并强调了他对第四电台的持续承诺。

---

## 57. Le Chat: 自定义MCP连接器、内存

**原文标题**: Le Chat: Custom MCP Connectors, Memories

**原文链接**: [https://mistral.ai/news/le-chat-mcp-connectors-memories](https://mistral.ai/news/le-chat-mcp-connectors-memories)

Mistral AI的Le Chat新增企业集成和个性化上下文记忆功能。该平台现推出超过20个安全、企业级连接器的Beta目录，由MCP（Mistral自定义协议）驱动，允许用户在Databricks、Snowflake、GitHub等工具中进行搜索、总结和操作。用户还可以添加自己的自定义MCP连接器以扩大覆盖范围。部署灵活，支持移动、浏览器、本地或云环境。

该平台还推出了“记忆”（测试版）功能，旨在通过保留先前对话的上下文来提供更个性化和相关的响应。用户可以完全控制他们的记忆，能够添加、编辑、删除和管理隐私设置。ChatGPT用户还可以将他们的记忆导入Le Chat。

Le Chat的连接器涵盖数据、生产力、开发、自动化和商业类别。具体示例包括从Databricks总结客户评论并创建Asana工单，审查GitHub拉取请求并在Notion中生成Jira问题，以及总结活跃的Jira问题以起草Confluence冲刺概览。

管理员用户可以通过代表身份验证来控制其组织内的连接器访问权限。

Mistral AI将于9月9日举办网络研讨会，讨论Le Chat的MCP功能，并于9月13日至14日在巴黎举办黑客马拉松，供AI工程师使用Le Chat中的自定义MCP构建项目。所有Le Chat用户均可免费使用连接器和记忆功能。

---

## 58. 我本应该喜欢上电气工程的。

**原文标题**: I should have loved electrical engineering

**原文链接**: [https://blog.tdhttt.com/post/love-ee/](https://blog.tdhttt.com/post/love-ee/)

在这篇历时数年写成的反思性文章中，作者回顾了他们在计算机科学与工程（CSE）专业的本科经历。最初，受SixthSense项目启发，怀揣着革新人机交互的愿景而选择CSE，作者很快对该专业的工程方面感到失望。他们觉得课程重复，缺乏推导和惊喜，过于依赖记忆。参与RC汽车和微型鼠标等实践工程项目的尝试均未成功，HKN荣誉学会也令人失望。

相反，作者在计算机科学方面表现出色，尤其是在Web应用程序开发方面，能够获得即时反馈和成就感。这促成了诸如课程注册UI之类的项目。与此同时，他们寻求研究机会，最初是在水文软件方面，后来转向物理学。涉及机器学习并最终前往CERN的物理学研究更具吸引力。

作者意识到一个根本性的脱节：工程学感觉与现实世界的创新脱节，工具和方法过时。另一方面，软件开发提供了使用尖端技术并产生直接影响的机会。这种认识，加上对物理学日益增长的兴趣，促使作者将专业转为计算机科学+物理学。

在他们的大四期间，一个应用物理实验室提供了一个更引人入胜的电子学体验，使他们能够通过定制的无线提醒来解决个人问题。总之，尽管最初认为他们*应该*热爱电气工程，但作者最终对自己的道路感到满意，承认在其他地方可能会有不同的体验，但肯定了他们对计算机科学和物理学的偏爱。

---

## 59. 使用微流体的可编程显示器[视频]

**原文标题**: A programmable display using microfluidics [video]

**原文链接**: [https://www.youtube.com/watch?v=rf-efIZI_Dg](https://www.youtube.com/watch?v=rf-efIZI_Dg)

利用微流体技术的可编程显示器

---

## 60. 我放弃了Spotify，搭建了自己的音乐系统。

**原文标题**: I ditched Spotify and set up my own music stack

**原文链接**: [https://leshicodes.github.io/blog/spotify-migration/](https://leshicodes.github.io/blog/spotify-migration/)

本文详细介绍了作者因担心艺术家报酬、数据隐私以及缺乏音乐所有权而放弃 Spotify，转而采用自托管音乐流媒体系统的过程。作者概述了其系统的组成部分：

*   **Navidrome：** 一个开源音乐服务器，用于流式传输其个人音乐收藏，并通过 Cloudflare Tunnel 访问以实现安全的远程访问。客户端应用程序包括 Web 播放器、Play:Sub (iOS)、Symfonium (Android) 和 Feishin (Desktop)。
*   **Lidarr：** 一款音乐收藏管理工具，可自动跟踪和下载音乐（合法购买），并与 sabnzbd 集成以进行下载。
*   **lrcget-kasm：** 用于下载同步歌词，由于缺少 CLI 版本，因此在容器化环境中运行。
*   **Lidify：** 通过利用 Last.fm scrobbles 和 Lidarr 库数据进行音乐发现，并可能与 ListenBrainz 集成。

作者强调了此设置的优点：更高的音乐质量、完全所有权、完全隐私以及直接通过购买来支持艺术家的能力。虽然承认初始设置需要技术技能和时间，但作者强调了摆脱企业流媒体平台的长期回报。文章还强调了通过合法渠道获取音乐的重要性，例如直接购买音乐、翻录购买的 CD 或使用免费的合法下载。未来的改进包括自动化歌词流程和探索其他音乐发现工具。

---

## 61. 火箭和弹弓

**原文标题**: Rocketships and Slingshots

**原文链接**: [https://postround.substack.com/p/rocketships-and-slingshots](https://postround.substack.com/p/rocketships-and-slingshots)

无法访问文章链接。

---

## 62. Étoilé – 基于GNUStep的桌面环境

**原文标题**: Étoilé – desktop built on GNUStep

**原文链接**: [http://etoileos.com/](http://etoileos.com/)

Étoilé是一个基于GNUstep的开源桌面环境，旨在提供以用户为中心的体验，专注于创造、协作和学习。它力求从用户界面中抽象出文件和操作系统进程等技术细节。

该项目的目标包括为所有对象启用修订历史，促进各种文档类型（文本、绘图、代码等）的实时协作，并允许用户通过组合提供的服务来定制他们的工作流程。Étoilé致力于创建一个更符合用户对计算机应如何运作的直观理解的系统。

Étoilé构建于GNUstep之上，并以MIT/BSD许可授权，因此被设计为可跨多种操作系统移植。 近期更新和新闻包括CoreObject预览版发布（2014年6月）以及关于改进和相关项目（如XMPPKit和StepChat）的公告。该项目还在2012年4月发布了Étoilé 0.4.2版本。该项目提供了联系方式，包括联系我们、RSS订阅、媒体资料包和一个商店。

---

## 63. Unix阴谋 (1991)

**原文标题**: Unix Conspiracy (1991)

**原文链接**: [http://www.catb.org/~esr/jargon/html/U/Unix-conspiracy.html](http://www.catb.org/~esr/jargon/html/U/Unix-conspiracy.html)

1991年的“Unix阴谋论”描述了一种在ITS和TOPS-20等老式操作系统爱好者中流行的阴谋论。该理论声称，贝尔实验室在20世纪70年代故意创建Unix，以削弱AT&T的竞争对手。其目的是让公司依赖Unix，一个看似廉价且可移植但本质上有缺陷（不可靠且不安全）的系统，从而需要由AT&T控制的持续升级。

文章将Unix比作计算机病毒，但它是通过市场力量和人类采用传播的，而不是直接感染。该理论的支持者指出，DEC总裁肯尼斯·奥尔森据称说过“Unix是蛇油”，之后不久DEC就开始推广自己的Unix工作站，以此作为证据。

文章最后指出，如果这种阴谋曾经存在过，那么在1990年后就变得难以控制，这与AT&T将其Unix业务出售给Novell以及Linux等免费Unix发行版的兴起同时发生。

---

## 64. ICPC 2025 世界总决赛结果

**原文标题**: ICPC 2025 World Finals Results

**原文链接**: [https://worldfinals.icpc.global/scoreboard/2025/index.html](https://worldfinals.icpc.global/scoreboard/2025/index.html)

本文档展示了2025年在巴库举行的第49届ICPC世界总决赛的最终结果。这是一个于2025年9月4日生成的实时记分牌，表明比赛已经结束。记分牌根据解决的问题数量和总用时对参赛大学队伍进行排名。

结果列出了139支队伍的排名、名称、解决问题数量、总用时以及他们在每个问题（A到L）上的详细表现，包括尝试次数和解题时间（如果已解决）。该文档还包括亚洲东部、拉丁美洲、非洲和阿拉伯、北欧亚、亚洲西部、亚太地区、北美洲和欧洲的区域排名。

排名前列的队伍是圣彼得堡国立大学（解决11个问题）、东京大学（解决10个问题）和北京交通大学（解决10个问题）。许多队伍解决了8个问题，排名通过时间区分。在榜单底部，一些队伍只解决了0到7个问题。该文档包括一个图例，定义了奖牌获得者和荣誉类别的颜色代码。记分牌还包括一些统计数据，例如每个问题的提交总数以及有多少个“首次解答”和总成功提交数。

---

## 65. 反转 Xorshift128 随机数生成器

**原文标题**: Inverting the Xorshift128 random number generator

**原文链接**: [https://littlemaninmyhead.wordpress.com/2025/08/31/inverting-the-xorshift128-random-number-generator/](https://littlemaninmyhead.wordpress.com/2025/08/31/inverting-the-xorshift128-random-number-generator/)

本文详细介绍了一种反转 JavaScript 中 `Math.random()` 使用的 Xorshift128+ 随机数生成器的方法，可能优于现有的基于 Z3 的方法。作者展示了一种高效算法（226 次运算），该算法可以在至少两个完整的 64 位输出的情况下确定 Xorshift128+ 的内部状态，与蛮力破解（2^128 次运算）相比，这是一个显著的改进。

关键的见解是，通过知道一个状态变量 (R1) 的最低有效 26 位，可以使用基于 Xorshift128+ 算法的归纳方程推导出其他状态变量 (L1, R2) 的剩余位。这显著减少了搜索空间。该算法涉及猜测这 26 位，使用归纳方程推导出候选状态值，然后通过将生成的输出与观察到的输出进行比较来验证猜测。

作者还讨论了潜在的速度优化，并提出了如何通过暴力破解额外的 24 位来扩展此方法以反转完整的 `Math.random()` 函数（该函数仅提供 52 位输出）。这需要三个观察到的输出进行验证，并导致 2^50 的搜索空间。

最后，作者反思了他们使用 ChatGPT 进行研究和编码辅助的经验，强调了其在头脑风暴和提供反馈方面的潜在价值，以及其在生成可靠代码方面的局限性。

---

## 66. 我们如何构建了一个 Swift 解释器

**原文标题**: How we built an interpreter for Swift

**原文链接**: [https://www.bitrig.app/blog/swift-interpreter](https://www.bitrig.app/blog/swift-interpreter)

Bitrig构建了一个Swift解释器，可在iPhone上动态运行Swift应用，这通常需要通过Xcode进行编译和签名（在设备本身上不可能）。该解释器通过使用SwiftSyntax解析Swift代码并将其直接评估到Swift中来工作。

解释器通过将字面量表示为`InterpreterValue`枚举中的Swift实例来处理运行时值。它通过将开发者定义的类型存储为`CustomInstance`结构体来扩展这一点，本质上是字典，将属性名称映射到运行时值。

为了利用现有的框架API（如SwiftUI），解释器使用预编译的“桥接”函数。例如，它预编译一个接受动态参数并调用`Text`初始化器的函数。通过解析`.swiftinterface`文件来自动为各种框架API生成桥接代码，从而推广了这种方法。令人惊讶的是，即使是基本操作也可以调用到框架实现中。

为了处理自定义类型的协议一致性（例如，使自定义SwiftUI `View`），解释器会创建符合该协议的“桩”类型。然后，这些桩会将它们的实现逻辑委托回解释器。例如，符合`Shape`协议的`ShapeStub`使其`path(in:)`函数调用解释器以确定路径。类似地，`ViewStub`处理`body`属性。

本质上，该解释器充当桥梁，将动态Swift代码转换为对已编译的Swift API和框架功能的调用。

---

## 67. 一次海豹六队闯入朝鲜的最高机密任务失败了

**原文标题**: A Top Secret Seal Team 6 Mission into North Korea Fell Apart

**原文链接**: [https://www.nytimes.com/2025/09/05/us/navy-seal-north-korea-trump-2019.html](https://www.nytimes.com/2025/09/05/us/navy-seal-north-korea-trump-2019.html)

无法访问文章链接。

---

## 68. Wal3: A Write-Ahead Log for Chroma, Built on Object Storage

**原文标题**: Wal3: A Write-Ahead Log for Chroma, Built on Object Storage

**原文链接**: [https://trychroma.com/engineering/wal3](https://trychroma.com/engineering/wal3)

生成摘要时出错

---

## 69. Reverse engineering Solos smart glasses

**原文标题**: Reverse engineering Solos smart glasses

**原文链接**: [https://jfloren.net/b/2025/8/28/0](https://jfloren.net/b/2025/8/28/0)

生成摘要时出错

---

## 70. Zola: One-stop static site engine

**原文标题**: Zola: One-stop static site engine

**原文链接**: [https://www.getzola.org/](https://www.getzola.org/)

生成摘要时出错

---

## 71. We already live in social credit, we just don't call it that

**原文标题**: We already live in social credit, we just don't call it that

**原文链接**: [https://www.thenexus.media/your-phone-already-has-social-credit-we-just-lie-about-it/](https://www.thenexus.media/your-phone-already-has-social-credit-we-just-lie-about-it/)

生成摘要时出错

---

## 72. Saquon Barkley is playing for equity

**原文标题**: Saquon Barkley is playing for equity

**原文链接**: [https://www.readtheprofile.com/p/saquon-barkley-investment-portfolio](https://www.readtheprofile.com/p/saquon-barkley-investment-portfolio)

生成摘要时出错

---

## 73. AR Fluid Simulation Demo

**原文标题**: AR Fluid Simulation Demo

**原文链接**: [https://danybittel.ch/fluid](https://danybittel.ch/fluid)

生成摘要时出错

---

## 74. A high schooler writes about AI tools in the classroom

**原文标题**: A high schooler writes about AI tools in the classroom

**原文链接**: [https://www.theatlantic.com/technology/archive/2025/09/high-school-student-ai-education/684088/](https://www.theatlantic.com/technology/archive/2025/09/high-school-student-ai-education/684088/)

生成摘要时出错

---

## 75. A Website Is a Room

**原文标题**: A Website Is a Room

**原文链接**: [https://a-website-is-a-room.net/](https://a-website-is-a-room.net/)

生成摘要时出错

---

## 76. When can I reuse this calendar?

**原文标题**: When can I reuse this calendar?

**原文链接**: [https://whencanireusethiscalendar.com](https://whencanireusethiscalendar.com)

生成摘要时出错

---

## 77. AI not affecting job market much so far, New York Fed says

**原文标题**: AI not affecting job market much so far, New York Fed says

**原文链接**: [https://money.usnews.com/investing/news/articles/2025-09-04/ai-not-affecting-job-market-much-so-far-new-york-fed-says](https://money.usnews.com/investing/news/articles/2025-09-04/ai-not-affecting-job-market-much-so-far-new-york-fed-says)

生成摘要时出错

---

## 78. SAP splashes €20B on Euro sovereign cloud push

**原文标题**: SAP splashes €20B on Euro sovereign cloud push

**原文链接**: [https://www.theregister.com/2025/09/04/sap_sovereign_cloud/](https://www.theregister.com/2025/09/04/sap_sovereign_cloud/)

生成摘要时出错

---

## 79. I bought the cheapest EV, a used Nissan Leaf

**原文标题**: I bought the cheapest EV, a used Nissan Leaf

**原文链接**: [https://www.jeffgeerling.com/blog/2025/i-bought-cheapest-ev-used-nissan-leaf](https://www.jeffgeerling.com/blog/2025/i-bought-cheapest-ev-used-nissan-leaf)

生成摘要时出错

---

## 80. Farewell to Meshnet

**原文标题**: Farewell to Meshnet

**原文链接**: [https://nordvpn.com/blog/meshnet-shutdown/](https://nordvpn.com/blog/meshnet-shutdown/)

生成摘要时出错

---

## 81. Amazon RTO policy is costing it top tech talent, according to internal document

**原文标题**: Amazon RTO policy is costing it top tech talent, according to internal document

**原文链接**: [https://www.businessinsider.com/amazon-rto-policy-costing-it-top-tech-talent-ai-recruiters-2025-9](https://www.businessinsider.com/amazon-rto-policy-costing-it-top-tech-talent-ai-recruiters-2025-9)

生成摘要时出错

---

## 82. 16-inch softball

**原文标题**: 16-inch softball

**原文链接**: [https://en.wikipedia.org/wiki/16-inch_softball](https://en.wikipedia.org/wiki/16-inch_softball)

生成摘要时出错

---

## 83. New knot theory discovery overturns long-held mathematical assumption

**原文标题**: New knot theory discovery overturns long-held mathematical assumption

**原文链接**: [https://www.scientificamerican.com/article/new-knot-theory-discovery-overturns-long-held-mathematical-assumption/](https://www.scientificamerican.com/article/new-knot-theory-discovery-overturns-long-held-mathematical-assumption/)

生成摘要时出错

---

## 84. How to build vector tiles from scratch

**原文标题**: How to build vector tiles from scratch

**原文链接**: [https://www.debuisne.com/writing/geo-tiles/](https://www.debuisne.com/writing/geo-tiles/)

生成摘要时出错

---

## 85. Eels are fish

**原文标题**: Eels are fish

**原文链接**: [https://eocampaign1.com/web-version?p=495827fa-8295-11f0-8687-8f5da38390bd&pt=campaign&t=1756227062&s=033ffe0494c7a7084332eb6e164c4feeeb6b4612e0de0df1aa1bf5fd59ce2d08](https://eocampaign1.com/web-version?p=495827fa-8295-11f0-8687-8f5da38390bd&pt=campaign&t=1756227062&s=033ffe0494c7a7084332eb6e164c4feeeb6b4612e0de0df1aa1bf5fd59ce2d08)

生成摘要时出错

---

## 86. The Color of the Future: A history of blue

**原文标题**: The Color of the Future: A history of blue

**原文链接**: [https://www.hopefulmons.com/p/the-color-of-the-future](https://www.hopefulmons.com/p/the-color-of-the-future)

生成摘要时出错

---

## 87. Almost anything you give sustained attention to will begin to loop on itself

**原文标题**: Almost anything you give sustained attention to will begin to loop on itself

**原文链接**: [https://www.henrikkarlsson.xyz/p/attention](https://www.henrikkarlsson.xyz/p/attention)

生成摘要时出错

---

## 88. Interrupts – The Heartbeat of a Unix Kernel

**原文标题**: Interrupts – The Heartbeat of a Unix Kernel

**原文链接**: [https://leftasexercise.com/2018/11/05/interrupts-the-heartbeat-of-a-unix-kernel/](https://leftasexercise.com/2018/11/05/interrupts-the-heartbeat-of-a-unix-kernel/)

生成摘要时出错

---

## 89. What is it like to be a bat?

**原文标题**: What is it like to be a bat?

**原文链接**: [https://en.wikipedia.org/wiki/What_Is_It_Like_to_Be_a_Bat%3F](https://en.wikipedia.org/wiki/What_Is_It_Like_to_Be_a_Bat%3F)

生成摘要时出错

---

## 90. Thunk: Build Rust program to support Windows XP, Vista and more

**原文标题**: Thunk: Build Rust program to support Windows XP, Vista and more

**原文链接**: [https://github.com/felixmaker/thunk](https://github.com/felixmaker/thunk)

生成摘要时出错

---

## 91. Lit: a library for building fast, lightweight web components

**原文标题**: Lit: a library for building fast, lightweight web components

**原文链接**: [https://lit.dev](https://lit.dev)

生成摘要时出错

---

## 92. Claude Code: Now in Beta in Zed

**原文标题**: Claude Code: Now in Beta in Zed

**原文链接**: [https://zed.dev/blog/claude-code-via-acp](https://zed.dev/blog/claude-code-via-acp)

生成摘要时出错

---

## 93. Experimental Hook-and-Loop Attachment System for Walls and Floors

**原文标题**: Experimental Hook-and-Loop Attachment System for Walls and Floors

**原文链接**: [https://www.core77.com/posts/138350/Experimental-Hook-and-Loop-Attachment-System-for-Walls-and-Floors](https://www.core77.com/posts/138350/Experimental-Hook-and-Loop-Attachment-System-for-Walls-and-Floors)

生成摘要时出错

---

## 94. Interview with US Digital Service's First Administrator

**原文标题**: Interview with US Digital Service's First Administrator

**原文链接**: [https://usdigitalserviceorigins.org/interviews/mikey-dickerson/](https://usdigitalserviceorigins.org/interviews/mikey-dickerson/)

生成摘要时出错

---

## 95. Speeding up PyTorch inference on Apple devices with AI-generated Metal kernels

**原文标题**: Speeding up PyTorch inference on Apple devices with AI-generated Metal kernels

**原文链接**: [https://gimletlabs.ai/blog/ai-generated-metal-kernels](https://gimletlabs.ai/blog/ai-generated-metal-kernels)

生成摘要时出错

---

## 96. The wall confronting large language models

**原文标题**: The wall confronting large language models

**原文链接**: [https://arxiv.org/abs/2507.19703](https://arxiv.org/abs/2507.19703)

生成摘要时出错

---

## 97. One of the last, best hopes for saving the open web and a free press is dead

**原文标题**: One of the last, best hopes for saving the open web and a free press is dead

**原文链接**: [https://www.bloodinthemachine.com/p/one-of-the-last-best-hopes-for-saving](https://www.bloodinthemachine.com/p/one-of-the-last-best-hopes-for-saving)

生成摘要时出错

---

## 98. Say Bye with JavaScript Beacon

**原文标题**: Say Bye with JavaScript Beacon

**原文链接**: [https://hemath.dev/blog/say-bye-with-javascript-beacon/](https://hemath.dev/blog/say-bye-with-javascript-beacon/)

生成摘要时出错

---

## 99. Show HN: A roguelike game that runs inside Notepad++

**原文标题**: Show HN: A roguelike game that runs inside Notepad++

**原文链接**: [https://github.com/thelowsunoverthemoon/NeuroPriest](https://github.com/thelowsunoverthemoon/NeuroPriest)

生成摘要时出错

---

## 100. Airbus B612 Cockpit Font

**原文标题**: Airbus B612 Cockpit Font

**原文链接**: [https://github.com/polarsys/b612](https://github.com/polarsys/b612)

生成摘要时出错

---

