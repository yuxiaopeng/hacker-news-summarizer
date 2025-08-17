# Hacker News 热门文章摘要 (2025-08-17)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. LL3M：大型语言3D建模器

**原文标题**: LL3M: Large Language 3D Modelers

**原文链接**: [https://threedle.github.io/ll3m/](https://threedle.github.io/ll3m/)

本文介绍了LL3M (大型语言3D建模器)，该系统利用大型语言模型(LLMs)通过Python代码在Blender中生成和编辑3D资产。与之前专注于受限程序生成的方法不同，LL3M创建具有复杂几何形状、布局和外观的非受限资产。

LL3M分三个阶段运行：初始创建、自动优化和用户引导优化。在初始创建阶段，LLMs根据文本指令生成基本形状。然后，自动优化阶段纠正不合理的配置并改进几何形状。最后，用户引导优化允许基于用户输入进行迭代编辑。

LL3M的主要优势在于其能够生成具有可解释和可编辑Blender代码的多样化和详细形状。该系统可以处理复杂的排列、丰富的外观和材质属性。生成的代码有助于迭代优化，包括自动优化和通过用户干预进行优化。它还允许跨不同网格进行一致的风格化、特定部分的材质编辑以及在保留资产整体特征的同时进行多次连续编辑。

此外，LL3M的可解释代码、Blender节点中的透明参数以及代码模式的通用性和可重用性使得用户可以进行直观的编辑并在类别之间进行知识转移。该系统还能够生成具有分层排列的多个对象的场景，从而实现Blender中的场景图行为。

---

## 2. 你的助理为谁服务？

**原文标题**: Who does your assistant serve?

**原文链接**: [https://xeiaso.net/blog/2025/who-assistant-serve/](https://xeiaso.net/blog/2025/who-assistant-serve/)

这篇短文并非文章，而是试图确认用户是否为机器人的消息。它呈现了一项安全检查，声明“正在确认你是不是机器人！加载中...请稍等，我们需要在继续之前检查您的连接安全性。” 其内容要求等待，同时系统验证用户的真实性和连接安全性，暗示着防止恶意机器人活动的努力。“你的助手为谁服务？”这个标题表明对用户助手（在此上下文中假定为机器人）的忠诚或目的的询问，安全检查试图确定这一点。 简而言之，这是一种旨在识别和可能阻止机器人的安全措施。

---

## 3. 领英奖励平庸。

**原文标题**: LinkedIn rewards mediocrity

**原文链接**: [https://www.elliotcsmith.com/linkedin-toxic-mediocrity/](https://www.elliotcsmith.com/linkedin-toxic-mediocrity/)

作者批评领英，认为其优先考虑和奖励“有毒的平庸”，而非有意义的内容。他们认为，该平台鼓励用户发布通用、过度包装且最终空洞的内容，以建立个人品牌并提升互动指标，尽管这些内容缺乏真正的实质或益处。这种“有毒的平庸”被描述为伪装成有见地的、但几乎没有价值的内容，类似于SEO驱动的写作。

作者认为，这种体系通过增加网站停留时间和广告点击量使领英受益，但并不一定使参与其中的用户受益。他们认为，专注于创造真正的、高质量的作品并有思考地分享，比参与领英内容游戏对职业更有价值。

作者建议，希望创作有意义在线内容的人应该专注于建立博客或其他平台，在这些平台上，深度和质量优先于肤浅的参与。对于领英内容消费者来说，建议是积极寻找和推广尽管存在噪音但仍然存在的真正有价值的内容，或者干脆断开连接并参与现实世界的活动。核心信息是，追求真正的、有价值的工作和技能深度，比追求领英上浅薄的指标和表面上的参与更有意义。

---

## 4. 导数、梯度、雅可比矩阵和海森矩阵

**原文标题**: Derivatives, Gradients, Jacobians and Hessians

**原文链接**: [https://blog.demofox.org/2025/08/16/derivatives-gradients-jacobians-and-hessians-oh-my/](https://blog.demofox.org/2025/08/16/derivatives-gradients-jacobians-and-hessians-oh-my/)

本文阐明了导数、梯度、雅可比矩阵和海森矩阵之间的关系，并展示了它们的应用，尤其是在优化领域。

**导数**是基础，表示函数在每个点的变化。它们通过识别导数为零的点来寻找最小值（优化）。梯度下降是一种迭代优化方法，依赖于导数。

**梯度**将导数的概念扩展到多维函数。梯度是偏导数的向量，显示了相对于每个变量的变化率。梯度指向最陡增长的方向，使其对梯度下降优化至关重要。

**雅可比矩阵**表示向量值函数所有可能的梯度的集合。在特定点评估时，它描述了空间在该位置如何扭曲（旋转、挤压）。雅可比矩阵的行列式揭示了区域是否被变换放大、缩小或反转。

**海森矩阵**包含所有二阶偏导数。它有效地描述了函数的曲率。通过将函数局部近似为二次函数，海森矩阵可以显著加速优化。海森矩阵的特征值可以揭示该函数是否有最小值、最大值或鞍点。对于大型问题，计算量很大，拟牛顿法提供了替代方案。

---

## 5. 使用NVMe SSD加速索引I/O

**原文标题**: Faster Index I/O with NVMe SSDs

**原文链接**: [https://www.marginalia.nu/log/a_123_index_io/](https://www.marginalia.nu/log/a_123_index_io/)

本文详细介绍了 Marginalia 搜索引擎的索引重新设计，重点在于利用 NVMe 固态硬盘提高 I/O 性能。 重新设计的原因是索引大小不断增长以及需要更快的查询处理速度。 关键变化包括将内存映射的 B 树替换为确定性块状跳跃列表，专为高效的排序列表交集而设计。

跳跃列表结构设计为密集且直接模式友好型，可容纳截断的块，并使用确定性前向指针来最大限度地减少列表遍历期间的回溯。 该设计利用了 NVMe 固态硬盘的独特特性，特别是它们一致的读取时间，而与请求的数据量无关（在一定范围内）。

作者运行了针对查询“to be or not to be”的基准测试，展示了不同块大小的性能影响。 他们发现，增加块大小显着提高了查找和执行速度，直到达到 128KB 左右的收益递减点。 实验发现，更大的块大小具有优势，因为固态硬盘的读取速度不会随着读取的字节数线性增加。

文章总结说，搜索引擎的瓶颈已从读取文档列表转移到结果排序和位置数据检索。 作者还质疑压缩的价值，因为该系统目前不受文档列表的 I/O 限制。

---

## 6. OLAP需要ORM吗?

**原文标题**: Does OLAP Need an ORM

**原文链接**: [https://clickhouse.com/blog/moosestack-does-olap-need-an-orm](https://clickhouse.com/blog/moosestack-does-olap-need-an-orm)

本文探讨了将对象关系映射器 (ORM) 原则应用于在线分析处理 (OLAP) 数据库（如 ClickHouse）的潜在益处和挑战。虽然 ORM 在在线事务处理 (OLTP) 数据库中很受欢迎，但作者认为，由于根本的语义差异，直接将现有的 OLTP ORM 扩展到 OLAP 可能会出现问题。

文章重点介绍了空值性和唯一性等概念在 OLTP 和 OLAP 中的行为方式差异，如果使用相同的 ORM API，可能会导致混淆和性能问题。作者建议设计特定于 OLAP 的建模 API，以反映 OLAP 独特的默认设置和语义。

一个有效的 OLAP 开发者体验 (DX) 层应借鉴核心 ORM 概念，如代码即模式、类似 SQL 的查询构建器以及镜像生产环境的本地开发。然而，它还应促进 OLAP 友好的行为，如 OLAP 原生语义、版本化的模式发布以及可以在基础设施之间传递的类型。

本文介绍了 MooseStack，一个用于分析基础设施的开源工具包，以及它的 Moose OLAP 模块，该模块提供了对 ClickHouse 的抽象。Moose OLAP 强调将模式作为可组合的代码，将模式与表分离，并使用联合类型来实现跨系统兼容性。它还提倡采用以 SQL 为中心的查询构建方法，该方法具有类型安全性和自动完成功能。

作者最后提出了关于类型安全的查询构建器和编写原始 SQL 之间的最佳平衡的开放性问题，寻求社区对设计更好的 OLAP 开发者体验的意见。

---

## 7. BBC Micro：你肯定拥有的设备的鼻祖

**原文标题**: BBC Micro: The Ancestor to a Device You Are Guaranteed to Own

**原文链接**: [https://retrogamecoders.com/bbc-micro-the-ancestor-to-a-device-you-are-guaranteed-to-own/](https://retrogamecoders.com/bbc-micro-the-ancestor-to-a-device-you-are-guaranteed-to-own/)

本文探讨了作者对20世纪80年代英国微型计算机BBC Micro的怀旧之情，并强调了它作为现代移动技术先驱的重要意义。作者展示了他们从存储中取回的BBC Master设备，包括软盘驱动器和鼠标。

文章详细介绍了BBC Micro虽然也使用了6502系列微芯片，但凭借其卓越的BASIC编程语言和可扩展性，在竞争中脱颖而出。它还提到了英国政府在20世纪80年代对计算机教育的投资，旨在培养一代精通计算机的人才，而BBC Micro被选为标准。然而，由于访问权限有限，许多学校只有一台或几台机器。

作者回忆了他们的学校使用借来的BBC Master短暂参与末日审判计划的经历。文章随后描述了Master系列的改进，包括65C12微处理器、更低的功耗和更大的RAM（128 KB），从而提高了图形处理能力。最后，作者邀请读者分享他们自己使用课堂电脑的经历，将BBC Micro在英国的普及与Commodore PET在加拿大和Apple II在美国的流行进行对比。文章在BBC Micro和ARM架构之间建立了一个关键联系，而ARM架构存在于全球近60%的移动设备中。

---

## 8. 此处有龙：预防 386 中的静电损坏、闩锁和亚稳态

**原文标题**: Here be dragons: Preventing static damage, latchup, and metastability in the 386

**原文链接**: [http://www.righto.com/2025/08/static-latchup-metastability-386.html](http://www.righto.com/2025/08/static-latchup-metastability-386.html)

本文探讨了Intel 386处理器专用的输入/输出(I/O)电路，旨在保护其免受外部威胁。作者深入研究了这些电路与芯片核心逻辑的不同之处，强调了它们在防止静电放电(ESD)、闩锁效应和亚稳态造成的损害方面的作用。

文章详细介绍了ESD保护机制，该机制利用二极管和电阻器来重定向过电压并限制电流，从而保护敏感的晶体管栅极。闩锁效应是一种由寄生晶体管引起的潜在破坏性现象，通过使用保护环隔离晶体管并重定向不需要的电流来缓解。

最后，文章探讨了亚稳态，一种信号变得不稳定和未定义的状态。386采用同步器，特别是具有独特的感觉放大器型触发器的双触发器系统，通过快速解析模糊信号来降低亚稳态的概率。作者甚至发现了一种以前未被描述的基于感觉放大器的触发器电路。文章阐述了这些I/O电路对于386可靠运行至关重要，为外部世界提供了一个强大的接口。

---

## 9. Show HN: Fallinorg - 离线Mac应用，按意义整理文件

**原文标题**: Show HN: Fallinorg - Offline Mac app that organizes files by meaning

**原文链接**: [https://fallinorg.com/#](https://fallinorg.com/#)

Fallinorg：一款利用本地AI理解文件内容的文件整理Mac应用，提供传统文件整理工具之外的私密离线选择。它不只分析文件名，而是分析文件含义。目前支持英文文本(.txt)和PDF文件，并计划扩展文件类型支持。用户可以自主控制整理后的文件所在文件夹位置。

该应用针对Apple Silicon Mac进行了优化，完全离线运行，确保用户数据私密安全。没有任何信息会被发送到外部服务器。

预售版售价$9.49美元，提供无限文件处理、可自定义文件夹位置、支持上述文件类型、完全隐私保护、Apple Silicon优化以及邮件支持。预售购买者将获得免费的小版本更新，并在后续发布具有主要功能的完整版本时，获得升级折扣。

FAQ部分解答了关于应用功能、隐私、文件类型支持和退款政策的常见问题。 同时明确说明，虽然目前仅支持Apple Silicon Mac，但开发人员正在考虑Intel支持，并鼓励用户通过电子邮件联系他们以获取相关更新。

---

## 10. 企业体验

**原文标题**: The Enterprise Experience

**原文链接**: [https://churchofturing.github.io/the-enterprise-experience.html](https://churchofturing.github.io/the-enterprise-experience.html)

《企业体验》幽默地记录了作者在初创公司工作十年后，于大型企业$ENTERPRISE的第一年工作经历。他反思了遇到的文化冲击和怪癖，强调了小企业与大型组织之间的差异。

主要观察包括：简单的难题因官僚流程和流氓工具而变得棘手；巨额财务浪费与对基本必需品的吝啬形成对比；同事能力参差不齐，源于缺乏基于绩效的解雇制度；紧迫性的模糊性；以及“安全剧场”，指标优先于真正的安全实践。

他还注意到高层领导需要表现出知识渊博，但与复杂领域的现实脱节，导致重复过去的失败。作者强调了工程组织内部存在孤立的“帝国”，每个“帝国”都有截然不同且通常低于标准的实践。

尽管略带讽刺，作者强调他很享受这一年，并且不后悔。他列出了几个积极方面，包括：与大型工程社区互动，职业发展机会，编写数百万用户使用的软件，指导机会，工作保障，可预测的薪酬，专业化可能性，团队多样性以及对技能提升的支持。作者以充满希望的展望结束，暗示未来可能会重新审视这些观察。

---

## 11. 人工智能智商测试结果

**原文标题**: IQ Tests Results for AI

**原文链接**: [https://www.trackingai.org/home](https://www.trackingai.org/home)

TrackingAI，由马克西姆·洛特创建，是一个旨在监测和追踪AI聊天机器人的政治观点和偏见的网站。该网站受到大卫·罗萨多的AI政治地图研究的启发，旨在提供关于AI意识形态的最新见解，帮助用户了解他们使用的AI的偏见，并使AI创建者能够开发出更具政治合理性的模型。

该网站通过追踪AI对包括政治罗盘测试和智商测试在内的各种测试的反应，来识别AI行为随时间变化的趋势和变化。洛特认为，AI偏见受到它们训练所用的数据和它们收到的来自人类的反馈的影响。他指出，截至2023年，大多数主要的AI在经济上倾向于左翼，在社会上倾向于自由意志主义，且程度各不相同。

TrackingAI还允许用户查看AI如何回答特定问题，并访问AI回复的可搜索数据库。该网站的未来目标包括添加一个“犹豫”指标、一个AI对齐测验、一个数学测试和一个专注于挑战AI的问题的AI智商测试。

该网站由洛特资助，计算机编码由汉斯·FZ·洛伦扎纳完成。洛特鼓励用户提供关于新的AI和测试的反馈和建议。他还欢迎通过付费订阅他的Substack进行合作和捐赠。该项目的根源在于洛特对确保获取反映现实而非极端意识形态的信息充满热情。

---

## 12. 我们实现了100% GPU利用率，然后通过不使用它让速度提升了3倍

**原文标题**: We Hit 100% GPU Utilization–and Then Made It 3× Faster by Not Using It

**原文链接**: [https://www.daft.ai/blog/embedding-millions-of-text-documents-with-qwen3](https://www.daft.ai/blog/embedding-millions-of-text-documents-with-qwen3)

本文详细介绍了如何使用 Daft、Qwen3-Embedding-0.6B 和其他工具嵌入数百万个文本文档时实现接近 100% 的 GPU 利用率，并预告了一种无需最大化 GPU 利用率即可实现 3 倍速处理的方法。

作者提出了一个将文本文档转换为向量数据库可用嵌入的流程，概述了以下步骤：从 S3 读取数据、使用 spaCy 将文本分块成句子、使用 Qwen3-Embedding-0.6B 生成嵌入，以及将结果写入 Turbopuffer。

涵盖的关键方面包括：

*   **文本分块：** 强调根据用例选择正确的分块策略（句子、段落、章节或固定大小）的重要性，并使用 spaCy 实现句子级别分块。
*   **嵌入生成：** 强调选择文本嵌入模型时需要考虑的因素，例如模型在 MTEB 排行榜上的性能、特定任务的性能以及多语言支持。利用 SentenceTransformer 与 Qwen3-Embedding-0.6B。
*   **分布式处理：** 配置 Daft 以利用 Ray 集群在 GPU 节点上进行分布式处理。
*   **性能考虑：** 建议调整批次大小、扩展 worker 以及使用量化 (bfloat16) 来优化 GPU 内存使用和吞吐量。

该文章提供了每个流程步骤的代码片段和自定义技巧，使读者能够复现该过程。最后，作者暗示将在后续文章中揭示他们如何通过探索自定义 GPU 流水线并用 vLLM 替换 Sentence Transformers 来实现 3 倍加速，承诺提供一种更有效的嵌入生成方法。

---

## 13. 消除 AWS Lambda 上的 JavaScript 冷启动

**原文标题**: Eliminating JavaScript cold starts on AWS Lambda

**原文链接**: [https://goose.icu/lambda/](https://goose.icu/lambda/)

奥利弗·梅德赫斯特介绍了Porffor，一款旨在通过提前将JS编译成小型、快速的本地二进制文件来消除AWS Lambda冷启动问题的JavaScript引擎/运行时。与Node和Bun不同，Porffor不捆绑运行时，从而显著减小二进制文件大小并加快执行速度。

作者在AWS Lambda上，使用一个简单的处理函数，对Porffor与Node.js和亚马逊的LLRT（一种针对冷启动优化的实验性JS运行时）进行了基准测试。Porffor表现出显著的改进，冷启动速度比Node.js快约12倍，比LLRT快近4倍。此外，由于Node.js目前享有的托管运行时优势，它也被证明比两者都更具成本效益。

虽然Porffor很有前景，但仍处于pre-alpha开发阶段，JavaScript支持有限，目前没有I/O或Node兼容性。作者承认它尚未准备好广泛采用。然而，他邀请拥有小型、无Node API Lambda的个人或公司与他联系，以便快速评估Porffor的潜在优势。基准测试数据和代码可在GitHub上获取，以确保透明度。

---

## 14. 用 SQLite 构建同步引擎和响应式系统的经验教训

**原文标题**: Lessons learned from building a sync-engine and reactivity system with SQLite

**原文链接**: [https://www.finkelstein.fr/sqlite-sync-engine-with-reactivity](https://www.finkelstein.fr/sqlite-sync-engine-with-reactivity)

无法访问文章链接。

---

## 15. 元素摄影周期表

**原文标题**: The Photographic Periodic Table of the Elements

**原文链接**: [https://periodictable.com](https://periodictable.com)

这个名为“元素摄影周期表”的网站，以视觉丰富的方式探索元素周期表。它允许用户点击单个元素来了解更多信息，展示每个元素的照片样本。该网站最后更新于2017年10月28日。

除了交互式表格外，该网站还提供多种附加功能和资源，重点展示了“大众科学”专栏，并提供购买相关商品的渠道，例如海报、卡片以及实物元素样品和展示品。

该网站面向广泛的受众，包括学生、教师、科学家以及寻找元素照片和视频的人。它还推广“木制元素周期表桌子”。 总之，该网站旨在成为一个全面且引人入胜的资源，用于学习和可视化元素，并由相关产品和外部内容提供支持。

---

## 16. VictoriaLogs 消息、时间与流的实用摄入指南

**原文标题**: VictoriaLogs Practical Ingestion Guide for Message, Time and Streams

**原文链接**: [https://victoriametrics.com/blog/victorialogs-concepts-message-time-stream/index.html](https://victoriametrics.com/blog/victorialogs-concepts-message-time-stream/index.html)

无法访问文章链接。

---

## 17. 湾 - VEO 3 的开源替代方案

**原文标题**: Wan – Open-source alternative to VEO 3

**原文链接**: [https://github.com/Wan-Video/Wan2.2](https://github.com/Wan-Video/Wan2.2)

Wan2.2是VEO 3的开源替代方案，代表了基础视频生成模型的重大升级。主要创新包括：

*   **高效的MoE架构：** 将混合专家(MoE)架构引入视频扩散模型，在维持计算成本的同时，增加了模型容量。专门的专家模型处理不同时间步的去噪。
*   **电影级美学：** 精心策划的带有详细标签的美学数据，允许精确和可控的电影风格生成，以及可定制的美学偏好。
*   **复杂运动生成：** 在更大的数据集（图片+65.6%，视频+83.2%）上进行训练，增强了模型在运动、语义和美学方面的泛化能力。
*   **高效的高清混合TI2V：** 具有先进VAE的5B模型实现了16×16×4的压缩比，支持720P分辨率、24fps的文本到视频和图像到视频生成，并可在消费级显卡（例如4090）上运行。

该版本包括推理代码和模型权重，并集成到ComfyUI和Diffusers中。文章还详细介绍了安装说明、模型下载以及运行文本到视频、图像到视频和文本图像到视频生成的操作指南，包括单GPU和多GPU推理选项。此外，还包括使用不同GPU进行的计算效率测试，以及对混合专家架构对模型优势的讨论。

---

## 18. 消除关于RLHF的误解

**原文标题**: Dispelling misconceptions about RLHF

**原文链接**: [https://aerial-toothpaste-34a.notion.site/How-OpenAI-Misled-You-on-RLHF-1f83f742d9dd80a68129d06503464aff](https://aerial-toothpaste-34a.notion.site/How-OpenAI-Misled-You-on-RLHF-1f83f742d9dd80a68129d06503464aff)

好的，我需要更多信息。因为内容描述为在“Notion”上，我可以推断这很可能是在Notion.so（一个流行的生产力和协作平台）上的文档或页面。但是，在不知道该 Notion 页面中的实际内容的情况下，我只能做出假设。

为了提供准确的摘要，我需要 **Notion 页面的文本** 本身。请提供 Notion 文档的实际内容。

但是，我可以根据标题“消除对RLHF的误解”以及我对RLHF（从人类反馈中强化学习）的了解，给你一个关于文章可能涵盖内容的 **大致概念**：

**可能摘要（在提供实际内容之前）：**

这篇文章可能旨在消除围绕从人类反馈中强化学习（RLHF）的常见误解，这是一种用于将大型语言模型（LLM）与人类价值观和偏好对齐的关键技术。它可能旨在阐明 RLHF 的工作原理、它的能力以及它的局限性。

它可能会讨论以下误解：

*   **RLHF是解决偏见的完美方案：** 驳斥 RLHF 完全消除 LLM 中的偏见的想法，承认它可以减少但不能根除它们。
*   **RLHF 只是为了取悦人类：** 澄清 RLHF 旨在在人类偏好与其他理想品质（如事实准确性和连贯性）之间取得平衡。
*   **RLHF 易于实施：** 强调在收集高质量的人工反馈、训练奖励模型和优化策略方面的挑战。
*   **RLHF 是一次性修复：** 强调 RLHF 是一个迭代过程，需要持续的监控和改进。
*   **RLHF 取代了其他安全技术：** 解释 RLHF 通常与其他方法结合使用，例如预训练数据过滤和红队测试，以获得更强大和安全的 LLM。

文章可能以倡导对 RLHF 及其在开发负责任且有益的 AI 系统中的作用进行细致理解作为结论。它可能会重申 RLHF 是一种强大的工具，但不是万能的灵丹妙药，持续的研发对于解决其局限性并充分发挥其潜力至关重要。

**请提供实际的 Notion 页面内容，以便我可以创建精确的摘要。**

---

## 19. 超视：Brøderbund公司“特技赛车”的图形增强模组

**原文标题**: SuperSight: A graphical enhancement mod for Brøderbund's "Stunts"

**原文链接**: [https://marnetto.net/2025/02/20/broderbund-stunts-1](https://marnetto.net/2025/02/20/broderbund-stunts-1)

无法访问文章链接。

---

## 20. 大型语言模型讲的笑话不好笑，是因为它们避免意外。

**原文标题**: LLMs tell bad jokes because they avoid surprises

**原文链接**: [https://danfabulich.medium.com/llms-tell-bad-jokes-because-they-avoid-surprises-7f111aac4f96](https://danfabulich.medium.com/llms-tell-bad-jokes-because-they-avoid-surprises-7f111aac4f96)

丹·法布里奇认为，大型语言模型在喜剧、艺术、新闻、研究和科学方面表现不佳，是因为它们被设计成最小化惊喜，而惊喜是这些领域的基本要素。他认为，笑话、好故事、新闻甚至数学证明都依赖于惊喜和事后必然性之间的平衡。例如，一个好笑话是令人惊讶的，但在笑点之后是可以理解的。

大型语言模型经过训练来预测序列中的下一个词，因此擅长最小化惊喜。这使得它们不擅长产生幽默、引人入胜的叙述、揭示有洞察力的新闻故事或发现重要的数学证明，所有这些都需要一种意想不到的发现元素。

作者强调，大型语言模型的结构不容易通过更多的数据或处理能力来修复。核心问题在于它们避免惊喜的内在设计。他将此与软件开发进行对比，在软件开发中，代码质量通常通过没有惊喜（“每分钟的WTF次数”）来判断，而大型语言模型在这方面可以更成功。

法布里奇建议，实现通用人工智能 (AGI) 甚至使当前人工智能更有用需要一种混合架构。他设想了一个具有世界模型和学习动力的系统，积极寻找令人惊讶的真理，这些真理在事后变得不可避免。这样的系统将由好奇心驱动，使用大型语言模型来验证发现，但不是作为唯一的发现引擎。

---

## 21. 语言与性别研究专家罗宾·莱考夫去世，享年82岁

**原文标题**: Robin Lakoff, expert on language and gender, dead at 82

**原文链接**: [https://www.nytimes.com/2025/08/15/us/robin-lakoff-dead.html](https://www.nytimes.com/2025/08/15/us/robin-lakoff-dead.html)

无法访问文章链接。

---

## 22. 电价上涨速度是通货膨胀的两倍多。

**原文标题**: Electricity prices are climbing more than twice as fast as inflation

**原文链接**: [https://www.npr.org/2025/08/16/nx-s1-5502671/electricity-bill-high-inflation-ai](https://www.npr.org/2025/08/16/nx-s1-5502671/electricity-bill-high-inflation-ai)

美国电价上涨速度是整体通胀率的两倍多，给许多人造成经济压力，尤其是在夏季。佛罗里达州的居民，如肯·托马斯和阿尔·萨尔维，正为每月高达400-500美元的电费苦苦挣扎，不得不在支付电费和其他必需品（如药物）之间做出艰难的选择。

导致这一增长有几个因素。首先，耗电量巨大的AI数据中心的增长正在显著增加电力需求。其次，天然气出口的增加推高了这种燃料的价格，而美国超过40%的电力是由天然气发电的。能源部预计天然气成本将继续上涨。

虽然太阳能和风能等可再生能源提供了更便宜的替代方案，但开发它们和必要的基础设施需要大量投资。这对低收入家庭构成了挑战，六分之一的家庭已经难以支付账单。

全国能源援助主管协会的马克·沃尔夫等倡导者担心，现有的联邦援助计划不足，尤其是在制冷成本不断上升的情况下，而拟议的预算削减威胁要彻底取消这项援助。最终，在不断增长的能源需求与可负担性之间取得平衡仍然是消费者和决策者关注的关键问题。

---

## 23. 开发者指南针 - 编程哲学测验

**原文标题**: Dev Compass – Programming Philosophy Quiz

**原文链接**: [https://treeform.github.io/devcompas/](https://treeform.github.io/devcompas/)

开发者指南针：一个编程理念测试，旨在帮助开发者了解他们的编码偏好。该测试通过抽象与具体编程风格以及易于人读与易于机器读两个维度分析偏好。用户通过回答20个关于其编码习惯和信念的问题，即可在“开发者指南针”上定位，并发现其主导的编程理念。该指南针以可视化方式呈现用户在两个关键维度上的位置，从而洞察其自然倾向和理想的编程环境。用户可以重新测试，以探索不同的观点或经验如何改变他们在指南针上的位置。

---

## 24. OpenAI 的进展

**原文标题**: OpenAI Progress

**原文链接**: [https://progress.openai.com](https://progress.openai.com)

文章《OpenAI的进展》探讨了与未来OpenAI模型可能进行的假想对话，展示了设想的对话如何随着人工智能的发展而演变。文章首先提及了早期的模型，如GPT-1和GPT-2，展示了一种困惑的状态，以及对理解人工智能的目的和伦理影响的关注。

随着模型发展到text-davinci-001，提问转向直接询问人工智能的未来以及如何为此做好准备。GPT-4-0314虽然承认缺乏情感，但提出了更具体和复杂的问题，包括关于人工智能技术进步、人工智能与人类价值观对齐、伦理准则、人工智能对社会的影响，以及在医学和教育等各个领域的突破。

最后，与GPT-5的假想对话变得更加哲学化。它探讨了关于意识的本质、当前人工智能理解的准确性，以及关于个人提升的建议。这种互动不再侧重于技术进步，而是更多地关于理解进化后的人工智能的意义和潜力，甚至邀请从未来人工智能的角度来思考人类的视角。这篇文章展示了人工智能能力的明显进步，以及围绕其未来角色而不断扩大的问题和期望范围。

---

## 25. 美国国务院停止向加沙儿童发放就医签证

**原文标题**: US state department stops issuing visas for Gaza’s children to get medical care

**原文链接**: [https://www.theguardian.com/us-news/2025/aug/16/gaza-children-visas-medical-care-laura-loomer](https://www.theguardian.com/us-news/2025/aug/16/gaza-children-visas-medical-care-laura-loomer)

美国国务院暂停向需要医疗救助的加沙儿童发放签证，此前极右翼网红劳拉·卢默（与唐纳德·特朗普关系密切）发起了一场运动。卢默分享了受伤的巴勒斯坦儿童抵达美国接受治疗的视频，谎称他们是在“圣战吟唱”和“吹哈马斯恐怖分子哨声”。她质疑国务院为何向加沙人发放签证，并谎称 95% 的人投票支持哈马斯。

国务院表示将对签证流程进行“全面彻底的审查”。卢默对这一决定表示庆贺，并建议将加沙人列入旅行禁令。共和党众议员兰迪·费恩称赞卢默提高了人们的意识。

巴勒斯坦儿童救济基金会谴责了这一决定，称医疗撤离是加沙儿童的生命线。美国伊斯兰关系委员会批评此举是特朗普政府亲以色列偏见的又一证据。保罗·格雷厄姆将卢默的行为比作 1940 年阻止犹太难民进入美国。文章还包括如何安全地联系《卫报》以获取有关该报道的信息。

---

## 26. 盖德粉碎

**原文标题**: Guid Smash

**原文链接**: [https://www.guidsmash.com](https://www.guidsmash.com)

无法访问文章链接。

---

## 27. 清晰的哈勃图像证实3I/阿特拉斯为彗星

**原文标题**: Sharp Hubble Images Confirm 3I/Atlas as Comet

**原文链接**: [https://www.sciencealert.com/nasa-probe-could-intercept-interstellar-comet-scientists-say](https://www.sciencealert.com/nasa-probe-could-intercept-interstellar-comet-scientists-say)

2025年7月，第三个星际天体（ISO），3I/ATLAS彗星，在我们的太阳系中被探测到。这一发现重新燃起了人们对拦截和研究这些天体的兴趣，从而能一窥其他恒星系统。

一项由亚伯拉罕·勒布教授领导的新提案建议，将美国宇航局目前正在绕木星运行的朱诺号探测器进行改造，以便在3I/ATLAS彗星于2026年3月接近木星时对其进行拦截。这将涉及一次木星奥伯特机动，利用木星的引力将朱诺号推向与该彗星的碰撞轨道。

科学家们使用专用软件计算了必要的轨道调整。如果成功，朱诺号的仪器可以提供关于3I/ATLAS彗星成分的宝贵数据，从而有可能揭示其起源系统的状况。

有趣的是，该论文还探讨了一种推测性的可能性，即3I/ATLAS彗星可能是外星技术。勒布认为，即使这种不太可能的假设也值得探索，因为它具有科学价值和潜在影响。

然而，最近的哈勃图像表明，彗星的内核相对较小，这表明它很可能是一个自然天体。无论如何，朱诺号的近距离观测（如果拦截发生）或3I/ATLAS彗星接近太阳时的观测将提供有价值的科学数据。朱诺号任务的延长也将使朱诺号有机会延长任务寿命。该团队强调，如果没有延期，这项任务是不可能实现的。

---

## 28. 努威斯管

**原文标题**: Nuvistor Valves

**原文链接**: [http://www.r-type.org/articles/art-150.htm](http://www.r-type.org/articles/art-150.htm)

本文详述了Nuvistor，这是20世纪50年代末期阀门技术的一项创新，旨在与晶体管的兴起竞争。Nuvistor由RCA开发，旨在提供比现有阀门更小的尺寸、更好的效率和更高的可靠性。RCA推广“Nuvistor化”以鼓励其采用。

Nuvistor有三极管和四极管两种配置，具有独特的金属外壳和陶瓷底座。一个关键优势是其小尺寸和卓越的高频性能，这通过最大限度地减少极间电容和电感的设计来实现。本文描述了Nuvistor的物理结构，强调了内部结构和外部引脚之间的直接连接，无需吸气剂，以及创建真空密封金属-陶瓷外壳的挑战。

本文将Nuvistor与当时的其他VHF/UHF阀门（如6AM4和E88CC）进行了比较，重点介绍了加热器功率和性能之间的设计权衡。虽然Nuvistor在尺寸和效率方面有所改进，但现有的阀门技术已经很先进并实现了高频率。作者质疑RCA是唯一制造商的普遍观点，并指出不同品牌的结构可能存在差异。最终，Nuvistor代表了阀门技术中一个重要但最终被取代的进步，因为晶体管变得越来越普及。

---

## 29. 提供泛型容器功能的C语言库比较

**原文标题**: Comparison of different C libraries providing generic containers capabilities

**原文链接**: [https://github.com/P-p-H-d/c-stl-comparison](https://github.com/P-p-H-d/c-stl-comparison)

本文档比较了几种提供类似于 C++ STL 的泛型容器功能的 C 语言库，重点比较它们的功能、性能和易用性。目标是评估 M*LIB（作者是其开发者）、STC、CMC、CTL、CollectionsC、CC 和 GLIB 等库，以便用于需要泛型数据结构的 C 项目。

该比较包括运行测试程序，这些程序使用 `int`、`mpz_t` (来自 GMP) 和字符串类型的动态数组和关联数组。这些程序遵循特定规则，避免变通方法，并确保正确的错误处理和内存管理。

该分析使用表格系统地比较这些库，比较的特征包括支持的 C 语言、"纯 C" 实现、仅头文件状态、泛型机制（void 指针、宏等）、类型安全、对不同数据类型的支持、复制/移动语义、容器/基本类型空间分离、emplace 支持、迭代器支持、排序算法、单一链接定义、完全抽象、契约违规检查、自然用法、内存处理和序列化。

本文档还包括一个基准测试，比较代码大小（字符数和行数）以及在实现测试程序时每个库所需的变通方法数量。另一个表格详细列出了每个库支持的容器类型，例如列表、数组、集合、映射、队列和字符串。

最后，列出了每个组件（GCC、库）的使用版本，并鼓励通过拉取请求进行贡献以改进比较。基准测试结果将在单独的文件中提供。

---

## 30. Show HN: 用于批量处理昂贵异步操作的 Rust 宏实用程序

**原文标题**: Show HN: Rust macro utility for batching expensive async operations

**原文链接**: [https://github.com/hackermondev/batched](https://github.com/hackermondev/batched)

这个“Show HN”帖子介绍了一个名为 `batched` 的 Rust 宏实用工具，旨在高效地批量处理昂贵的异步操作。它允许将多个、可能较小的异步调用分组到一个更大的操作中，以减少开销。

该宏使用 `#[batched]` 应用，通过将项目收集到批次中并根据可配置的参数（`limit`（最大批处理大小）、`concurrent`（最大并发批处理任务，默认为无限）和 `window`（处理批处理之前的最小等待时间，不同批处理大小的变体））一起处理它们来进行优化。

目标函数必须是异步的，并接受 `Vec<T>` 作为输入。返回值会传播（克隆）到批处理中的所有调用，除非函数返回 `Vec<T>`，在这种情况下，返回值将按照输入向量的顺序分配给每个单独的调用。返回类型必须实现 `Clone` 或包装在 `batched::error::SharedError` 中。

该帖子强调了先决条件，例如需要 Tokio 异步运行时，并且不支持在 struct impl 块中使用。它还介绍了可选的追踪功能：`tracing_span` 用于向批处理请求添加追踪 span，`tracing_opentelemetry` 用于在使用 OpenTelemetry 时将调用方的 span 链接到批处理调用。

该帖子包含示例用法，展示了如何批量处理简单的加法和数据库插入，演示了返回值传播和返回 `Vec<T>` 的两种情况。它说明了该宏如何创建单项（`insert_message`）和多项（`insert_message_multiple`）函数。

---

## 31. 箭鹳

**原文标题**: Pfeilstorch

**原文链接**: [https://en.wikipedia.org/wiki/Pfeilstorch](https://en.wikipedia.org/wiki/Pfeilstorch)

箭鹳 ("箭矢鹳") 是一种从非洲迁徙回欧洲的白鹳，其身体中嵌入了箭或矛。在德国，大约有25个这样的案例被记录在案。

最著名的箭鹳是罗斯托克箭鹳，1822年在德国被发现，脖子上插着一根来自中非的75厘米长的矛。这只特殊的鹳对理解鸟类迁徙至关重要。在它被发现之前，像鹳这样的鸟类每年消失都是一个谜，导致了冬眠、变成其他动物，甚至水下生存等理论。罗斯托克箭鹳提供了确凿的证据，表明鸟类会迁徙很长的距离到更温暖的气候过冬。这个标本现在在罗斯托克大学的动物学收藏中。

恩斯特·舒茨记录了更多鸟类携带箭的例子，并强调随着枪支取代弓箭，这种目击事件有所减少。

---

## 32. Dyna – 机器学习的逻辑编程

**原文标题**: Dyna – Logic Programming for Machine Learning

**原文链接**: [https://dyna.org/](https://dyna.org/)

Dyna是一种加权的、声明式的逻辑编程语言，专为机器学习研究设计。它构建于Datalog和Prolog之上，但提供灵活的执行顺序和加权规则，从而能简洁地表达复杂算法。例子包括矩阵乘法、斐波那契数列、CKY句法分析和神经网络。

Dyna项目始于2004年，旨在弥合数学算法描述和可执行代码之间的差距。Dyna 1.0通过任意半环扩展了Datalog，从而可以表达动态规划程序。Dyna 2.0解决了Dyna 1.0的局限性，取消了单一半环的限制，引入了函数，允许自由变量，支持惰性求值和记忆化，并加入了基于原型的继承。

当前的研究重点是使用关系代数上的项重写来实现Dyna，并采用强化学习来优化执行策略。已经发表了几篇研究论文，详细介绍了该语言的开发和应用。Dyna有多种实现版本，包括Dyna3 (Clojure)、Dyna-R (Python)、Dyna-Pi (Python)、Dyna-Phi (Truffle/Graal)、Dyna2 (Haskell/Python) 和 Dyna1。Dyna3有一个在线演示，Dyna-R 成功运行了复杂的 Dyna 2 程序。

---

## 33. 提高TCP初始拥塞窗口的论证 (2024)

**原文标题**: An argument for increasing TCP's initial congestion window (2024)

**原文链接**: [https://jeclark.net/articles/tcp-initcwnd/?tag=performance](https://jeclark.net/articles/tcp-initcwnd/?tag=performance)

本文论证了再次增加TCP初始拥塞窗口 (cwnd) 的必要性，并在谷歌2011年将其从1-3增加到10的建议基础上进一步发展。作者认为，现代互联网的特点是更大的网页和API调用，以及显著更大的资源文件大小（数百KB），当前的15KB初始cwnd限制再次阻碍了其发展。

问题：较小的初始cwnd迫使大型资源进行多次往返，显著增加了页面加载时间，尤其是在现代网站日益臃肿的情况下。

挑战：简单地大幅增加cwnd可能会导致拥塞和数据包丢失，而网络设备中具有深缓冲和低带宽链路的缓冲膨胀会加剧这种情况。

解决方案：作者提出了一个双管齐下的方法：

1. **将初始cwnd增加到一个更合理的数值，** 建议在20到40个数据包之间。
2. **采用BBR（瓶颈带宽和往返传播时间）作为默认的拥塞控制算法。** BBR由谷歌开发，通过监测往返时间的变化来检测拥塞，而不是依赖于数据包丢失，使其在管理缓冲膨胀方面更有效。

作者承认谷歌已经转向QUIC（基于UDP的HTTP），它完全消除了拥塞窗口。然而，他们认为TCP调优仍然重要，因为企业防火墙会禁用QUIC，并且传统设备仍然存在。作者表示致力于进一步的研究和倡导，以提高TCP性能并加速现代网络。

---

## 34. 以数学最优的方式切洋葱

**原文标题**: Dicing an Onion, the Mathematically Optimal Way

**原文链接**: [https://pudding.cool/2025/08/onions/](https://pudding.cool/2025/08/onions/)

本文探讨了在数学上优化洋葱丁切割方式，以获得最均匀的块状大小的方法，该研究建立在J. Kenji López-Alt先前工作的基础上。它使用相对标准偏差的概念来量化块状大小的一致性，分析了不同的切割技术——垂直切割、放射状切割和水平切割。

分析表明，当瞄准切割表面以下特定深度时，放射状切割通常比垂直切割产生更均匀的块状。虽然Kenji最初建议深度约为洋葱半径的60%，但本文表明，这个理想深度取决于层数和切割次数。例如，对于一个10层洋葱进行10次切割，96%的深度会产生最小的标准偏差。当切割次数和层数接近无穷大时，Poulsen博士的“洋葱常数”（约55.731%）是理想的深度。

本文使用2D横截面来计算洋葱块的面积，并通过分析19,320种组合来确定最佳切割策略。研究结果表明，在低于洋葱中心的位置进行切割时，放射状切割通常比垂直切割更一致。研究结果还表明，水平切割很少能提高一致性。

尽管具有数学上的严谨性，但本文以Kenji的一句话作为结尾，他表示，从理论角度来看，实现最佳均匀性很有趣，但它不太可能显着影响家庭烹饪的味道或质量。因此，虽然努力获得完美的洋葱块可能很有趣，但对于烹饪的成功来说，这不是必需的。

---

## 35. Raft共识算法 (2015)

**原文标题**: The Raft Consensus Algorithm (2015)

**原文链接**: [https://raft.github.io/](https://raft.github.io/)

Raft共识算法的设计兼顾了易理解性，同时保持了与Paxos相当的容错性和性能。共识是分布式系统中的一个基本问题，它确保多个服务器对值达成一致，从而保证一旦做出决定就具有最终性。Raft通常用于复制状态机，其中每个服务器维护一个状态机和一个使用共识算法达成一致的命令日志。这确保所有状态机处理相同的命令，从而产生一致的结果。

Raft网站提供了包括Raft原始论文、可视化工具以及演讲和讲座链接等资源。核心Raft论文详细介绍了该算法，而其他出版物则探讨了形式验证和相关主题。许多演讲提供了Raft的介绍和概述。

该网站还列出了教授Raft的课程，对教师和在线学习者都很有用。一个关键部分提供了一个精选的Raft在各种编程语言中的实现列表，重点介绍了它们的功能，例如领导者选举、日志复制、持久性、成员变更和日志压缩。raft-dev Google群组是提问和讨论Raft及其实现的论坛。

---

## 36. 同余伪随机数生成器的良好乘数

**原文标题**: Good multipliers for congruential pseudorandom number generators

**原文链接**: [https://arxiv.org/abs/2001.05304](https://arxiv.org/abs/2001.05304)

Guy Steele和Sebastiano Vigna的arXiv文章，题为“同余伪随机数生成器的高效计算、良好谱特性的乘数”，专注于改进同余伪随机数生成器(PRNG)。这些生成器依赖于在谱测试中表现良好的乘数，谱测试评估生成数字的格子结构。

作者旨在提供一系列乘数，这些乘数在维度高达8，滞后为8的情况下，对于使用典型二次幂模数的PRNG表现出良好的格子结构。他们特别分析了接近模数平方根的乘数，这些乘数由于其乘积可以快速计算而具有计算效率。

本质上，该论文提供了实用的资源——一系列“良好”的乘数——旨在提高同余PRNG的性能，特别是在谱特性和计算速度方面。该研究属于计算机科学中的数据结构和算法类别。

---

## 37. GDPR毫无意义：聊天监控终结欧盟隐私[视频]

**原文标题**: GDPR meant nothing: chat control ends privacy for the EU [video]

**原文链接**: [https://www.youtube.com/watch?v=3NyUgv6dpJc](https://www.youtube.com/watch?v=3NyUgv6dpJc)

《GDPR形同虚设：聊天监控终结欧盟隐私》暗示，尽管有GDPR，欧盟的隐私问题依然严重。“聊天监控”一词表明重点在于监视和监测在线通信。标题暗示，这项“聊天监控”计划具有侵入性，实际上否定了GDPR旨在为欧盟公民提供的保护。本质上，该视频的前提是欧盟的“聊天监控”措施正在破坏其公民的隐私权，导致GDPR失效。

然而，所提供的内容是通用的YouTube页脚信息。它*不*包含关于视频实际论点或内容的信息。根据给定的文本，不可能收集到关于“聊天监控”计划、其影响或针对它的具体论点的任何进一步细节。因此，摘要完全基于视频的标题。

---

## 38. 那个160亿密码的故事（又名“数据巨魔”）

**原文标题**: That 16B password story (a.k.a. "data troll")

**原文链接**: [https://www.troyhunt.com/that-16-billion-password-story-aka-data-troll/](https://www.troyhunt.com/that-16-billion-password-story-aka-data-troll/)

特洛伊·亨特的文章讨论了近期声称网上流传包含160亿用户名和密码的大规模泄露事件。亨特认为，这种被称为“数据钓鱼”的“泄露”极不可能是一个真正的新漏洞，规模如此之大。相反，它更可能是对先前已知泄露和公共数据的重新包装和重组，经过重新包装和放大，使其看起来比实际更大更新颖。

亨特强调，如此大规模的泄露事件发生，而受影响的服务或个人却没有重大报告，这不太可能。他还指出，存储和处理如此庞大的数据集在技术上存在挑战，暗示肇事者可能缺乏管理真正独特凭据的基础设施。

此外，作者强调，即使这些凭据*呈现*为新的，其中很大一部分也可能是重复的，或者来自非常旧且无关的泄露。这种策略旨在诱骗用户相信他们的凭据是新近泄露的，从而可能导致他们购买那些推广所谓泄露的人提供的非必要安全产品或服务。

亨特利用他使用Have I Been Pwned (HIBP)的经验来说明他是如何分析和验证数据泄露的。他强调了面对此类说法时保持怀疑、严格验证和避免恐慌的重要性。他敦促人们不要立即假定他们的凭据已泄露，而是使用HIBP等工具来针对已建立的、经过验证的泄露进行检查。“数据钓鱼”提醒我们，在面对在线安全威胁时，始终需要批判性思维和知情决策。

---

## 39. Node.js 能够执行 TypeScript 文件，无需额外配置。

**原文标题**: Node.js is able to execute TypeScript files without additional configuration

**原文链接**: [https://nodejs.org/en/blog/release/v22.18.0](https://nodejs.org/en/blog/release/v22.18.0)

Node.js v22.18.0 (LTS)，代号“Jod”，引入了直接使用`node`命令执行TypeScript文件的能力，无需预编译。此功能默认启用，并在执行期间剥离类型注释。提供了一个运行`.ts`文件的简单示例。但文档指出了一些支持的语法限制。此功能被认为是实验性的，可以使用`--no-experimental-strip-types`标志禁用。

此次发布还包括以下几个小更新和修复：

*   依赖项已更新，包括`amaro`、`sqlite`、`googletest`、`minimatch`、`acorn`、`simdjson`和`zlib`。
*   ESM加载器现在实现了`import.meta.main`。
*   改进了`fs`模块，用于处理带有AsyncIterator的突发事件。
*   权限模型现在在spawn上传播权限模型标志，并支持`permission.has(addon)`。
*   `url`模块添加了`fileURLToPathBuffer` API。
*   观察模式添加了`--watch-kill-signal`标志。
*   Workers现在是异步可释放的。
*   各个模块（如`crypto`、`dns`、`http`、`fs`、`repl`、`module`和`util`）中包含了各种错误修复和文档更新。

此版本还包括对`npm`、`gyp-next`和`eslint`等工具的更新，以及各种测试和类型改进。提供了适用于不同平台（Windows、macOS、Linux、AIX、ARM）的下载链接。

---

## 40. ResurrectedGod: 进程管理的 Ruby 框架

**原文标题**: ResurrectedGod: The Ruby Framework for Process Management

**原文链接**: [https://github.com/mishina2228/resurrected_god](https://github.com/mishina2228/resurrected_god)

ResurrectedGod 是一个 Ruby 进程管理框架，源自 God 项目。由 Tom Preston-Werner、Kevin Clark 和 Eric Lindvall 开发，旨在简化服务器进程和任务在部署过程中平稳运行的任务。它自诩为现有的最简单、最强大的监控应用程序。该项目提供工具，可以轻松配置和扩展 Ruby 应用程序的监控功能。文档可在仓库本身（`doc` 目录下）以及指定的（但未提供的）外部链接（原文中以“here”指示）上找到。Google Groups 上提供了一个社区邮件列表，地址为 https://groups.google.com/g/god-rb，用于支持和讨论。该软件根据仓库中 LICENSE 文件中规定的条款获得许可。本质上，ResurrectedGod 提供了一个基于 Ruby 的解决方案，用于监控和确保服务器进程和任务的持续运行。

---

## 41. FFmpeg 迁移至 Forgejo

**原文标题**: FFmpeg moves to Forgejo

**原文链接**: [https://code.ffmpeg.org/FFmpeg/FFmpeg](https://code.ffmpeg.org/FFmpeg/FFmpeg)

提供的文本**并非**关于 FFmpeg 迁移到 Forgejo 的文章。它是由一个名为 Anubis 的安全系统生成的，类似于验证码的消息，解释了用户为何会看到验证页面。

摘要如下：

用户看到验证界面是因为该网站使用了 Anubis，这是一种安全措施，旨在防止 AI 公司过度抓取网站内容。 这种抓取会使服务器不堪重负，并导致合法用户无法访问该网站。 Anubis 采用类似于 Hashcash 的“工作量证明”机制，要求用户的计算机执行一些计算。 对于个人用户来说，这种工作量可以忽略不计，但对于大规模机器人来说，会显著增加，从而使抓取更加困难和昂贵。

该系统是一种临时解决方案，在开发者们研究更复杂的方法（如指纹识别无头浏览器）以识别和阻止机器人而不妨碍合法用户的同时使用。 用户需要启用 JavaScript 才能使验证生效，因为 AI 公司迫使网站所有者实施此类保护措施。 正在开发一种无需 JavaScript 的解决方案。 JShelter 或类似的插件可能会干扰 Anubis，需要为该域禁用。 正在运行的 Anubis 的具体版本是 v1.21.3。

---

## 42. 以 SIMD 速度计数单词

**原文标题**: Counting Words at SIMD Speed

**原文链接**: [https://healeycodes.com/counting-words-at-simd-speed](https://healeycodes.com/counting-words-at-simd-speed)

本文详细介绍了优化单词计数程序的过程，从一个缓慢的Python实现开始，逐步通过C和SIMD（单指令多数据）技术提高其性能。目标是计算大型ASCII文本文件中的单词数。

最初的Python版本迭代每个字节，由于解释器开销导致运行时间为89.6秒。通过利用Python的`re`模块，获得了显著的改进，该模块使用基于C的正则表达式引擎，将运行时间减少到13.7秒。

将程序移植到C语言进一步加速到1.205秒，消除了为每个单词创建Python对象的开销。最大的提升来自于在C语言中使用ARM NEON SIMD指令，这允许并行处理16字节的块，将运行时间缩短到249毫秒。这涉及到创建掩码来识别每个块中的空白和单词边界。编译器进一步优化了代码。

最后，作者尝试使用线程利用多个CPU核心，实现了适度的加速，达到181毫秒。这种有限的改进表明程序此时已受到内存带宽的限制。最终的SIMD +线程版本以~5.52 GiB/s的速度处理文件。文章最后提供了源代码的链接，并推荐了有关SIMD优化的进一步阅读材料。

---

## 43. 为什么选择 Nim？

**原文标题**: Why Nim?

**原文链接**: [https://undefined.pyfy.ch/why-nim](https://undefined.pyfy.ch/why-nim)

无法访问文章链接。

---

## 44. 开发者陷阱

**原文标题**: Traps to Developers

**原文链接**: [https://qouteall.fun/qouteall-blog/2025/Traps%20to%20Developers](https://qouteall.fun/qouteall-blog/2025/Traps%20to%20Developers)

本文概述了开发者在使用各种技术时常见的陷阱（“坑”），重点关注导致错误的非直观行为和容易被误解的概念。

**HTML/CSS:** 强调了`min-width`、水平和垂直布局差异、外边距折叠、块格式化上下文 (BFCs)、堆叠上下文、移动端视口高度、绝对定位、空白折叠、`box-sizing` 和累积布局偏移等问题。它强调了理解这些特性如何交互以及它们如何偏离直观期望的重要性。

**Unicode & 文本编码:** 解释了码位和字形簇之间的区别，不同语言（Rust、Go、Java/C#/JS、Python、C++）中不同的字符串行为、字节顺序标记 (BOM)、易混淆字符和规范化。 理解这些细微差别对于正确处理文本至关重要，尤其是在处理表情符号和国际化时。

**浮点数:** 涵盖 NaN、正/负无穷大、负零、JSON 兼容性、不精确的相等比较、JS 数字限制、由于精度损失导致的结合律/分配律问题以及除法和乘法之间的性能差异。 讨论了硬件特定的差异，例如 FMA、次正规数和舍入模式，以及精度改进技术。

**时间:** 涉及闰秒、时区（UTC 与本地）、夏令时、由于 NTP 导致的潜在的时间“倒退”以及服务器上正确的时区配置。

**Java & Golang & C/C++:** 涉及特定语言的陷阱，例如 Java 中的对象引用比较、C++ 中的内存管理问题、Go 中的 nil 接口行为以及 C/C++ 和 Java 中危险的数字字面量。

---

## 45. 99行代码实现的Lisp

**原文标题**: A Lisp in 99LOC

**原文链接**: [https://github.com/Robert-van-Engelen/tinylisp](https://github.com/Robert-van-Engelen/tinylisp)

本文介绍"tinylisp"，这是一个用大约99行C代码实现的Lisp解释器，专为教学目的而设计，旨在演示Lisp的核心概念。尽管体积很小，但它具有21个内置原语、一个简单的垃圾回收器和一个REPL。该代码以函数式、类似Lisp的C语言风格编写，优先考虑可读性和紧凑性。作者强调在提供一个实用且可扩展的解释器的同时，保留Lisp的原始风味。

提供了几个版本的tinylisp，包括为速度和内存优化的版本、使用单精度和双精度浮点数的版本，以及一个为具有BCD装箱的复古Sharp PC-G850量身定制的版本。"extras"版本包括16个额外的原语，用于文件加载、readline支持、宏、异常和跟踪等功能。

本文概述了支持的核心Lisp功能，包括数字、符号、布尔值、列表、函数调用、引用、列表操作、算术、逻辑、条件、lambda、全局变量和局部变量。它详细介绍了每种功能的语法和行为，并提供示例和说明。此外，它还解释了如何编译和运行tinylisp，并列出了tinylisp自身实现的各种常见Lisp函数。本文还提到了同一作者编写的两个更大的Lisp实现，它们具有更多的功能和不同的垃圾收集方法。

---

## 46. 威廉姆斯综合征：与“自闭症”相反的疾病 (2014)

**原文标题**: Living with Williams Syndrome, the 'opposite of autism' (2014)

**原文链接**: [https://www.bbc.com/news/health-26888280](https://www.bbc.com/news/health-26888280)

这篇BBC新闻文章探讨了威廉姆斯综合征（WS），一种罕见的遗传疾病，常被称为“自闭症的反面”。 WS影响大约每18000人中的一人，其特征是高度的同理心、社交性和友善，但也伴随着低智商、焦虑以及处理金钱等任务的困难。 文章重点介绍了40岁的威廉姆斯综合征患者克里斯·斯蒂尔，突出了他在表演方面的优势以及他富有同情心的性格。 尽管他具有社交技巧，但克里斯仍饱受焦虑、容易信任陌生人以及需要不断安慰的困扰。

文章详细介绍了威廉姆斯综合征患者面临的挑战，包括导致他们变得脆弱的认知和语言差异。 他们可能过于信任他人，并且难以理解社交细微之处。 威廉姆斯综合征基金会的莉齐·赫斯特强调需要提高对威廉姆斯综合征的认识和支持，尤其是在全科医生中。 她认为，威廉姆斯综合征患者可能缺乏完全对自己负责的认知能力。

文章还探讨了对威廉姆斯综合征研究和支持的更多政府资助的需求，并指出资源不成比例地分配给了自闭症研究。 杜伦大学的黛比·里比博士正专注于采取实际措施来帮助家庭管理患有威廉姆斯综合征的儿童的焦虑。 她强调利用研究来支持受这种疾病影响的家庭的重要性。 文章最后解释了威廉姆斯综合征的遗传基础，即第七号染色体上的缺失，以及缺乏产前筛查。

---

## 47. 特沃斯基神经网络

**原文标题**: Tversky Neural Networks

**原文链接**: [https://gonzoml.substack.com/p/tversky-neural-networks](https://gonzoml.substack.com/p/tversky-neural-networks)

无法访问文章链接。

---

## 48. Show HN: unsafehttp – 用C从头开始编写的微型Web服务器，运行于Orange Pi之上

**原文标题**: Show HN: unsafehttp – tiny web server from scratch in C, running on an orange pi

**原文链接**: [http://unsafehttp.benren.au](http://unsafehttp.benren.au)

这篇“Show HN”帖子介绍了 `unsafehttp`，一个完全用 C 从头编写的极其精简的 HTTP 服务器。作者创建它是为了练习 C 语言、*nix 套接字编程和 C 编译。该服务器目前托管着网页本身，并在 Orange Pi SBC 上运行，可通过端口转发直接访问。

主要特性和设计选择：

*   **极简主义：** 该服务器优先考虑简单性和学习，而非严格遵守 RFC，仅实现基本的 GET 请求所需的最低限度。
*   **安全性：** 为了避免文件系统交互和路径清理问题，服务器在启动时将所有内容加载到内存中的哈希表中，使用文件路径作为键。这可防止恶意路径请求访问非预期文件。
*   **无代理：** 没有涉及 HTTP 代理，客户端直接连接到服务器的套接字。

作者鼓励读者将此项目作为灵感，保持自己的副项目有趣且简短，即使这意味着牺牲严格遵守标准。 源代码已提供给有兴趣的人。

---

## 49. GPT-5在进攻性安全基准测试中性能翻倍

**原文标题**: GPT-5 doubles performance in offensive security benchmark

**原文链接**: [https://xbow.com/blog/gpt-5](https://xbow.com/blog/gpt-5)

XBOW报告称，将OpenAI的GPT-5集成到其自主渗透测试平台XBOW后，其黑客能力显著提升，性能比之前的Sonnet/Gemini等模型翻了一番。这与OpenAI最初的评估形成对比，OpenAI认为GPT-5的网络安全能力与其前代产品相当。

XBOW的内部测试显示，当GPT-5作为XBOW中的漏洞利用引擎使用时，它在单次运行中识别出了其先前设置发现的70%的漏洞，而旧模型只能识别出23%。 这种改进源于GPT-5能够持续发现更难以捉摸的漏洞，并且代理需要更少的迭代来制作漏洞利用程序。 发现结果的质量也得到提高，误报更少。

XBOW将此次性能提升归功于XBOW平台的整体性，包括专为LLM优化的专用工具、在团队中工作并专门研究不同漏洞类别的代理，以及管理渗透测试过程的中央协调器。 他们认为，该平台有助于释放GPT-5潜在的网络安全能力，而这种能力在孤立情况下并不明显。 与之前的模型相比，GPT-5还表现出更好的推理能力以及发出更长、更复杂命令序列的能力。

文章总结称，人工智能驱动的进攻性安全技术正在加速发展，而强大的AI模型与专用自主系统的结合对于创建更有效、更具可扩展性的安全解决方案至关重要。

---

## 50. 10岁女孩成击败特级大师的最年轻女棋手

**原文标题**: 10-year-old becomes youngest female chess player to defeat grandmaster

**原文链接**: [https://www.cbsnews.com/news/10-year-old-youngest-female-chess-player-defeats-grandmaster/](https://www.cbsnews.com/news/10-year-old-youngest-female-chess-player-defeats-grandmaster/)

十岁女孩博达娜·希瓦南丹成为历史上击败国际象棋特级大师的最年轻女棋手。这位来自伦敦地区的奇才在英国利物浦举行的英国国际象棋锦标赛上战胜了60岁的国际象棋特级大师彼得·威尔斯，创下了这一里程碑。

国际象棋联合会（FIDE）宣布了这项纪录，并指出希瓦南丹超越了此前由美国卡丽莎·叶保持的纪录。虽然希瓦南丹由于里程碑要求尚未成为特级大师，但她拥有“女子国际大师”头衔，这是女性棋手的第二高头衔。

希瓦南丹在五岁时的新冠疫情期间开始下棋。国际象棋大师马尔科姆·佩恩称赞她的沉着、谦逊和才华，并表示她有可能成为女子世界冠军，甚至有可能成为世界冠军，并且正在成为特级大师的道路上。

文章还提到，8岁的阿斯瓦特·考希克在12月成为击败特级大师的最年轻全能棋手，突显了年轻神童在国际象棋领域崭露头角的趋势。

---

## 51. Ashby (YC W19) 正在美洲和欧洲、中东及非洲地区招聘设计工程师

**原文标题**: Ashby (YC W19) Is Hiring Design Engineers in AMER and EMEA

**原文链接**: [https://www.ashbyhq.com/careers?utm_source=hn&ashby_jid=579e9d03-0724-482b-a42a-8e5e80d73405](https://www.ashbyhq.com/careers?utm_source=hn&ashby_jid=579e9d03-0724-482b-a42a-8e5e80d73405)

Ashby (YC W19冬季项目成员) 现正招聘设计工程师，于美洲（AMER）和欧洲、中东及非洲（EMEA）地区均有职位空缺。公司寻求积极主动、追求高质量工作并能在协作环境中蓬勃发展的个人。有关具体要求、职责和申请流程的更多详细信息，请访问公司招聘页面，可通过提供的链接访问。

---

## 52. 几天内从头开始用Ada编写一个有竞争力的BZip2编码器——第二部分

**原文标题**: Writing a competitive BZip2 encoder in Ada from scratch in a few days – part 2

**原文链接**: [https://gautiersblog.blogspot.com/2025/07/writing-bzip2-encoder-in-ada-from.html](https://gautiersblog.blogspot.com/2025/07/writing-bzip2-encoder-in-ada-from.html)

无法访问文章链接。

---

## 53. 用角蛋白制成的牙膏或能保护和修复受损牙齿：研究

**原文标题**: Toothpaste made with keratin may protect and repair damaged teeth: study

**原文链接**: [https://www.kcl.ac.uk/news/toothpaste-made-from-hair-provides-natural-root-to-repair-teeth](https://www.kcl.ac.uk/news/toothpaste-made-from-hair-provides-natural-root-to-repair-teeth)

一项于2025年8月13日发表的新研究表明，头发、皮肤和羊毛中发现的角蛋白可用于牙膏，修复受损的牙釉质并预防早期蛀牙。伦敦国王学院的科学家发现，角蛋白会在牙齿上形成保护性涂层，通过吸引唾液中的矿物质来模仿天然牙釉质的结构和功能。这种基于角蛋白的治疗方法可以阻止酸性食物、不良卫生习惯和衰老引起的牙釉质腐蚀，从而解决牙齿敏感问题并防止牙齿脱落。

与仅能减缓蛀牙的含氟牙膏不同，角蛋白会形成致密的矿物质层，保护牙齿并封闭敏感的神经通道。这种治疗方法可以通过日常牙膏或专业涂抹的凝胶来实现。该团队希望在2-3年内向公众提供基于角蛋白的牙釉质再生技术。

该研究发表在《先进医疗保健材料》杂志上，表明从羊毛中提取的角蛋白形成了一种类似晶体的支架，可以吸引钙和磷酸根离子，从而促进保护性类釉质涂层的生长。这种可持续且环保的方法利用生物废弃物，无需传统牙科治疗中使用的有毒塑料树脂。该研究强调角蛋白是未来牙科护理的一个有希望的候选者，符合将废物转化为有价值的临床资源的努力。

---

## 54. 新的Cloudflare反盗版网站封锁或涉及域名

**原文标题**: New Cloudflare Pirate Site Blocking May Involve Domains

**原文链接**: [https://torrentfreak.com/new-cloudflare-pirate-site-blocking-may-already-involve-thousands-of-domains-250815/](https://torrentfreak.com/new-cloudflare-pirate-site-blocking-may-already-involve-thousands-of-domains-250815/)

Cloudflare加入英国盗版网站屏蔽行列：规模、透明度及有效性分析

---

## 55. 现代汽车对雷达探测器的干扰

**原文标题**: Modern Cars Wreak Havoc on Radar Detectors

**原文链接**: [https://www.thedrive.com/news/modern-cars-wreak-havoc-on-radar-detectors-heres-how-escort-adapts](https://www.thedrive.com/news/modern-cars-wreak-havoc-on-radar-detectors-heres-how-escort-adapts)

本文探讨了现代汽车碰撞避免系统 (CAS) 对雷达探测器构成的挑战，特别关注了 Escort Radar 的 Redline 360c 及其最新的固件更新。现代汽车的 CAS，如盲点监测和自适应巡航控制，会发射雷达信号，从而触发探测器的误报。

Escort 的新固件（版本 1.17）旨在改进过滤功能，以区分这些“CAS 干扰”和合法的警用雷达。该更新还声称改进了 POP 警报检测、方向指示器响应、K 波段过滤定制以及面向 OnStar 用户的 Wi-Fi 连接。

作者测试了更新后的 Redline 360c，发现它准确地检测到了测速陷阱，并且方向警告效果很好。 虽然“Drive Smarter”应用程序存在一些连接问题，但探测器本身的性能良好。

本文还探讨了使用雷达探测器的道德问题，认为安全超速和鲁莽驾驶之间存在差异。 虽然过度超速是危险的，但掌握有关潜在测速陷阱的信息本身并没有错。 Escort 通过论坛和 Beta 测试积极征求用户反馈，以改进其产品，并发布了一份白皮书，详细说明了其测试方法。

---

## 56. 使用子代理逆向工程 Claude 代码 CLI

**原文标题**: Reverse Engineering Claude Code CLI Using Sub Agents

**原文链接**: [https://www.sabrina.dev/p/reverse-engineering-claude-code-using](https://www.sabrina.dev/p/reverse-engineering-claude-code-using)

在 2025 年 7 月的文章中，Sabrina Ramonov 描述了她如何出于教育目的，使用自定义 Claude 子代理对 Claude Code CLI 进行逆向工程。这些子代理是一项新功能，是专门设计用于处理特定任务的 AI 助手，具有定制的系统提示、工具和上下文窗口。

为了逆向工程代码，她使用了三个子代理：一个文件分割器，用于分割压缩后的 JavaScript 代码；一个结构分析器，用于识别代码模式和依赖关系；以及一个美化器，用于格式化代码。

这些子代理揭示了几个有趣的发现：

1.  **Claude Code 的 TODO 工具提示：** 一个详细的提示，旨在指导 AI 何时以及如何使用待办事项列表来跟踪复杂任务的进度，强调主动的任务管理。
2.  **实验性的 ULTRACLAUDE.md：** 存在一个名为 UltraClaude 的实验模式。
3.  **Claude Code 的 Web Fetch 工具提示：** 关于 Claude Code 如何检索和分析网络内容的详细信息，包括 URL 处理、提示使用和响应约束的指南。
4.  **PLAN MODE 系统提醒：** 揭示了与 “PLAN MODE” 相关的内部提醒。

Ramonov 发现子代理对于可以并行化的、长时间运行的简单任务非常有效，强调了明确指令对于获得最佳结果的重要性，尤其是在处理复杂任务时。她还建议对子代理进行沙盒化以提高安全性。

---

## 57. 好的系统设计

**原文标题**: Good system design

**原文链接**: [https://www.seangoedecke.com/good-system-design/](https://www.seangoedecke.com/good-system-design/)

本文概述了优秀系统设计的关键原则，并将其与过于复杂或以领英/推特为优化目标的建议进行了对比。作者将系统设计定义为组装服务，其目标通常是实现“不出错”的状态，而不是令人印象深刻的复杂性。文中强调了简单性，并避免过早优化。

一个核心原则是最小化有状态组件，因为它们容易出错并需要人工干预。相反，应该倾向于易于重启的无状态服务。数据库是状态的中心存储库，因此至关重要。灵活的模式设计很重要，但应避免过于通用的模式，以免将复杂性转移到应用程序代码中。索引策略应与常用查询相匹配。

瓶颈通常与数据库相关，因此像JOIN这样的高效数据库查询技术至关重要。优先将读取查询发送到副本，并警惕查询峰值。拆分缓慢的操作，立即为用户执行所需的最少工作，然后将其余工作卸载到后台任务。

缓存很有价值，但应谨慎使用，以避免与状态相关的问题。探索替代方案，例如使用计划作业和文档存储来实现持久的、大规模的缓存。事件中心（如Kafka）有助于服务之间的通信，但直接API调用通常更可取，因为它们更简单且更易于调试。

最后，本文讨论了数据分发的推送与拉取机制。虽然拉取对于网站来说很常见，但推送对于内部服务或像Gmail这样的大型客户端应用程序来说可能更有效。

---

## 58. 做那些无法规模化的事，然后就别规模化。

**原文标题**: Do things that don't scale, and then don't scale

**原文链接**: [https://derwiki.medium.com/do-things-that-dont-scale-and-then-don-t-scale-9fd2cd7e2156](https://derwiki.medium.com/do-things-that-dont-scale-and-then-don-t-scale-9fd2cd7e2156)

亚当·德雷韦茨基认为，在人工智能辅助编码的时代，由“做那些不可规模化的事情”这一口号所推广的，推动每个软件项目都规模化的做法，不再总是必要或可取的。借助 GPT 等工具，构建软件变得如此简单和廉价，以至于个人可以创建小众的、个性化的解决方案，而无需承受将其转化为成熟业务的压力。

他用三个例子来说明这一点：一个因其规模有限而受益的小型、私密的 Slack 工作区；一个专门为他母亲量身定制的、重建的明信片邮寄服务，避免了公共平台的复杂性；以及一个为他母亲设计的简单座机服药提醒应用程序，绕过了可扩展的医疗提醒服务的责任。

核心思想是，人工智能提供的低成本和易于开发的特性，使得开发者可以为非常小的，甚至单个的受众创建软件，而这可能就是最佳结果。德雷韦茨基建议拥抱这种自由，抵制规模化的冲动，并在创造“小巧、有用且完全属于你”的东西中找到满足感。 这篇文章提出了一个模式：识别一个与个人相关的需求，构建一个简单的解决方案，抵制规模化，并享受结果。 最终，他认为当今开发工具的最大优势不仅仅是速度或成本，而是可以停下来，并对一个小巧、完美定制的解决方案感到满足的自由。

---

## 59. 对于艾丽斯·默多克来说，道德是关于爱，而非义务和规则。

**原文标题**: For Iris Murdoch, morality is about love, not duties and rules

**原文链接**: [https://aeon.co/essays/for-iris-murdoch-morality-is-about-love-not-duties-and-rules](https://aeon.co/essays/for-iris-murdoch-morality-is-about-love-not-duties-and-rules)

艾瑞斯·默多克挑战了将道德完全建立在义务和规则之上的传统观点，认为**爱**是道德的核心。她相信我们对世界的看法，特别是我们对他人的感知，塑造了我们的行为，而扭曲这种看法是一种道德上的失败。

默多克强调**关注**的重要性，借鉴了西蒙娜·薇依的思想。她认为，我们最基本的道德活动涉及以特定的方式关注事物，从而塑造我们的整体视野。

在默多克看来，自我(Ego)是实现真正视野的主要障碍。在焦虑和以自我为中心的驱动下，它会导致**幻想**，扭曲现实，并阻止我们看到他人真实的模样。她用“M”和“D”的例子来说明这一点，M的偏见影响了她对D的看法。

为了克服自我及其幻想，默多克提出了**充满爱的关注**。这涉及以慷慨、耐心和公正的方式关注他人，认识到他们内在的价值。充满爱的关注将我们从自身中抽离出来，使我们能够把握他人的现实，并提高我们视野的道德品质。这是一种强大的力量，可以抵消我们以自我为中心的倾向，并使我们能够看到真相。

虽然承认人类的爱可能存在缺陷和误导性，但默多克将专注的爱视为理想，代表着对现实的真诚且具有重要道德意义的投入。

---

## 60. 无源微波中继器

**原文标题**: Passive Microwave Repeaters

**原文链接**: [https://computer.rip/2025-08-16-passive-microwave-repeaters.html](https://computer.rip/2025-08-16-passive-microwave-repeaters.html)

本文探讨了无源微波中继器。这项技术旨在克服微波通信中的视距限制，特别是在山区或复杂地形中。微波无线电凭借其高带宽容量，成为一项重要的电信技术进步，其起源可追溯至二战期间开发的雷达技术。然而，微波信号需要在天线之间保持直接视线，这给有障碍物的地区带来了困难。

无源微波中继器本质上是大型扁平金属面板，其功能类似于镜子，可将微波信号绕过障碍物或传输到较远的距离。这些中继器不需要电源，因此非常适合有源中继器（放大信号）不切实际的偏远地区。

克莱茨伯格兄弟詹姆斯和乔治是这项技术的先驱。詹姆斯是蒙大拿电力公司的一名工程师，他提出了这个想法，乔治的航空企业克莱茨伯格航空制造了第一个无源中继器。这促成了Microflect公司的成立，该公司专门生产用于山区地区的这种“广告牌”。

本文解释说，无源中继器甚至可以提供增益，这与直觉相反。有源中继器增加功率，而无源中继器通过收集大量的微波能量并重新发射来实现增益。它们的大表面积超过了实际天线尺寸，可以“收集”更多的能量，从而产生增益。尺寸是关键因素，较大的中继器可以反射较大的能量截面，从而增加增益。

---

## 61. 在小处出色，在大处糟糕的技术陷阱

**原文标题**: The trap of tech that's great in the small but not in the large

**原文链接**: [https://surfingcomplexity.blog/2025/08/16/the-trap-of-tech-thats-great-in-the-small-but-not-in-the-large/](https://surfingcomplexity.blog/2025/08/16/the-trap-of-tech-thats-great-in-the-small-but-not-in-the-large/)

Lorin Hochstein的文章《适用于小规模但不适用于大规模的技术陷阱》探讨了使用在小规模任务中有效，但随着项目增长而变得有问题的技术的弊端。作者认为，由于项目的渐进式增长以及这些技术最初提供的便利，迁移到其他技术的时机常常被延误，最终导致重大问题。

Hochstein列举了几个例子：

*   **Shell脚本：** 适用于简单的任务（20行以内），但不适合具有 `if` 语句的复杂逻辑，建议使用Python作为替代方案。
*   **Makefiles：** 非常适合运行简单任务和构建小型Go程序，但对于大型项目来说是噩梦，需要Maven、Gradle或Bazel等工具。
*   **YAML：** 适用于合理大小的配置文件（30行以内），但在大型文件中变得笨拙且难以管理，降低了其人类可读性。
*   **电子表格：** 虽然是一种成功的最终用户编程工具，但当用作事实上的数据库时，会变得有问题，因为过渡到合适的数据库需要巨大的飞跃。
*   **Markdown：** 作者参考了Hillel Wayne的论点，即Markdown不适合像书籍这样的大型写作项目，主张使用rST（reStructuredText）代替。

本质上，这篇文章警告人们不要被最初方便但缺乏可扩展性的技术所迷惑，强调了选择能够适应未来增长和复杂性的工具的重要性。

---

## 62. HP-UX和Unix上的Office

**原文标题**: Office on HP-UX and Unix

**原文链接**: [https://www.openpa.net/hp-ux_office.html](https://www.openpa.net/hp-ux_office.html)

这篇OpenPA的文章详细介绍了20世纪80年代和90年代HP-UX和Unix系统上办公和生产力软件的可用性。尽管HP-UX的主要用途是技术和工程，但软件移植使工程师能够融入更广泛的办公环境。直到20世纪90年代中期，一些流行的办公套件被移植到Unix系统，包括用于图形的CorelDRAW!以及用于一般办公任务的WordPerfect、Ami Pro、Applixware和IslandOffice。Lotus 1-2-3和Wingz用于电子表格，而FrameMaker、Interleaf和WebWorks用于专业出版。

该文章提供了HP-UX上每个应用程序的特定版本信息和支持细节，特别是PA-RISC工作站。CorelDRAW提供了2.0.1、3.0和3.5版本，其中3.5版本也移植到了Linux (Caldera)。WordPerfect的运行时间很长，从4.2版本到8.0版本，支持各种HP-UX版本，并包括拼写检查器和MS Office 97转换器等功能。Ami Pro 3.0曾在HP-UX上短暂可用。Applixware，一个完整的办公套件，也在2000年左右发布了Unix/HP-UX版本。IslandOffice提供了一套应用程序（Write、Draw、Paint、Calc、Presents、Chart），对HP-UX的支持版本各不相同。Lotus 1-2-3在90年代初被移植，惠普参与了许可/支持。Wingz是一个用于HP-UX的图形电子表格应用程序，特别是1.1a和3.0版本。作者注意到很难找到现存的文档。

---

## 63. 在 Yocto 上以非 root 用户身份运行 Wayland 客户端

**原文标题**: Running Wayland Clients as Non-Root Users on Yocto

**原文链接**: [https://embeddeduse.com/2025/08/11/running-wayland-clients-as-non-root-users/](https://embeddeduse.com/2025/08/11/running-wayland-clients-as-non-root-users/)

解决Yocto嵌入式Linux系统上以root用户运行Wayland客户端（Qt应用程序）的安全问题

---

## 64. PuTTY有了新网站。

**原文标题**: PuTTY has a new website

**原文链接**: [https://putty.software/](https://putty.software/)

PuTTY，一款适用于Windows和Unix操作系统的免费SSH客户端软件，包含一个类似xterm的终端模拟器，已启用新网站。 该软件由Simon Tatham创建并维护。 用户可以访问下载页面获取最新版本，或访问主网站了解更多信息。 公告内容简洁，引导用户访问易于获取的资源，以下载软件或了解更多信息。

---

## 65. 一缕头发或能改写我们对印加记录方式的认知。

**原文标题**: A single lock of hair could rewrite what we know about Inca record-keeping

**原文链接**: [https://www.science.org/content/article/single-lock-hair-could-rewrite-what-we-know-about-inca-record-keeping](https://www.science.org/content/article/single-lock-hair-could-rewrite-what-we-know-about-inca-record-keeping)

以下是基于我从搜索结果和一般知识中收集的信息，对文章“一缕头发或将改写我们对印加记录保存方式的认知”的总结：

该文章探讨了对几百年前被献祭的年轻印加女性的一缕头发的分析，如何为我们提供关于印加记录保存和社会实践的新见解。虽然印加以缺乏书面语言而闻名，但他们利用一种名为“奇普”的结绳系统来记录信息，包括人口普查数据、税收和历史叙事。关于“奇普”的谜团在于，它们如何在没有文字的情况下传递复杂的信息。

研究人员现在正在使用头发样本来分析该女性在被献祭之前的饮食和药物使用情况。通过检查头发中存在的化学同位素（这些同位素记录了随着时间推移的饮食摄入量），他们可以重建她的行动轨迹和社会地位。具体而言，饮食的变化（从农民食物过渡到玉米和肉类等精英食物）以及古柯等物质的存在表明她正在为某种仪式做准备。

这种类型的分析意义重大，因为它能够与“奇普”上记录的信息相关联。通过研究多个与特定“奇普”相关的个体遗骸，科学家们希望破译编码在绳结和颜色中的含义。例如，饮食变化和古柯的使用可能对应于“奇普”中记录的特定事件或仪式。因此，这种结合了考古科学、历史记录和“奇普”分析的跨学科方法，可能会彻底改变我们对印加文明及其复杂记录保存系统的理解，从而提供一种超越传统西班牙殖民叙事的新视角。

---

## 66. Show HN: Lue – 带语音合成功能的终端电子书阅读器

**原文标题**: Show HN: Lue – Terminal eBook Reader with Text-to-Speech

**原文链接**: [https://github.com/superstarryeyes/lue](https://github.com/superstarryeyes/lue)

Lue：一款终端电子书阅读器，具备文本转语音（TTS）功能，支持EPUB、PDF、TXT、DOCX、HTML、RTF和Markdown等多种格式。它提供简洁的终端用户界面，支持鼠标和键盘控制，自动保存阅读进度，并具有跨平台兼容性，适用于macOS、Linux和Windows，支持100多种语言。

Lue采用模块化TTS系统，默认使用Edge TTS（在线），并提供Kokoro TTS（本地/离线）。安装说明适用于各种操作系统，包括启用离线Kokoro TTS的步骤。快速入门指南包括安装FFmpeg（音频处理所需）以及克隆/设置Lue仓库。

基本用法包括启动阅读器、指定TTS模型和语音、启用PDF清理过滤器以及查看可用选项的命令。概述了键盘和鼠标的导航控制。

文档还包括面向希望使用新的TTS模型扩展Lue并为项目做出贡献的开发人员的信息。它提供了不同操作系统上阅读进度和错误日志的数据存储位置。Lue在GPL-3.0许可下发布，欢迎贡献。

---

## 67. Making Your Own Merchant Service Provider

**原文标题**: Making Your Own Merchant Service Provider

**原文链接**: [https://voidfox.com/blog/payment_processor_fun_2025_making_your_own_msp/](https://voidfox.com/blog/payment_processor_fun_2025_making_your_own_msp/)

生成摘要时出错

---

## 68. Apple's Greed Is Finally Backfiring [video]

**原文标题**: Apple's Greed Is Finally Backfiring [video]

**原文链接**: [https://www.youtube.com/watch?v=JUG1PlqAUJk](https://www.youtube.com/watch?v=JUG1PlqAUJk)

生成摘要时出错

---

## 69. Microsoft's latest Windows 11 24H2 update breaks SSDs/HDDs, may corrupt data

**原文标题**: Microsoft's latest Windows 11 24H2 update breaks SSDs/HDDs, may corrupt data

**原文链接**: [https://www.neowin.net/news/report-microsofts-latest-windows-11-24h2-update-breaks-ssdshdds-may-corrupt-your-data/](https://www.neowin.net/news/report-microsofts-latest-windows-11-24h2-update-breaks-ssdshdds-may-corrupt-your-data/)

生成摘要时出错

---

## 70. The future of large files in Git is Git

**原文标题**: The future of large files in Git is Git

**原文链接**: [https://tylercipriani.com/blog/2025/08/15/git-lfs/](https://tylercipriani.com/blog/2025/08/15/git-lfs/)

生成摘要时出错

---

## 71. Clinical genetics and the problem of uncertain significance

**原文标题**: Clinical genetics and the problem of uncertain significance

**原文链接**: [https://stetson.substack.com/p/solving-the-problem-of-uncertain](https://stetson.substack.com/p/solving-the-problem-of-uncertain)

生成摘要时出错

---

## 72. Dokploy is the sweet spot between PaaS and EC2

**原文标题**: Dokploy is the sweet spot between PaaS and EC2

**原文链接**: [https://nikodunk.com/2025-06-10-diy-serverless-(coreos-+-dokploy)](https://nikodunk.com/2025-06-10-diy-serverless-(coreos-+-dokploy))

生成摘要时出错

---

## 73. WebOS – Part One

**原文标题**: WebOS – Part One

**原文链接**: [https://docs.asbedb.com/articles/webos/webos---part-one/](https://docs.asbedb.com/articles/webos/webos---part-one/)

生成摘要时出错

---

## 74. Israeli gov. official arrested in Nevada internet crimes against children sting

**原文标题**: Israeli gov. official arrested in Nevada internet crimes against children sting

**原文链接**: [https://www.theguardian.com/us-news/2025/aug/16/nevada-arrest-israeli-official](https://www.theguardian.com/us-news/2025/aug/16/nevada-arrest-israeli-official)

生成摘要时出错

---

## 75. Apple's new Processor Trace instrument is incredible

**原文标题**: Apple's new Processor Trace instrument is incredible

**原文链接**: [https://victorwynne.com/processor-trace-instrument/](https://victorwynne.com/processor-trace-instrument/)

生成摘要时出错

---

## 76. Bullfrog in the Dungeon

**原文标题**: Bullfrog in the Dungeon

**原文链接**: [https://www.filfre.net/2025/08/bullfrog-in-the-dungeon/](https://www.filfre.net/2025/08/bullfrog-in-the-dungeon/)

生成摘要时出错

---

## 77. Princeton NuEnergy's battery recycling tech recovers 97% of lithium-ion material

**原文标题**: Princeton NuEnergy's battery recycling tech recovers 97% of lithium-ion material

**原文链接**: [https://www.energy-reporters.com/environment/97-battery-recycling-breakthrough-princeton-nuenergy-opens-first-u-s-commercial-facility-cutting-costs-38-and-slashing-environmental-impact/](https://www.energy-reporters.com/environment/97-battery-recycling-breakthrough-princeton-nuenergy-opens-first-u-s-commercial-facility-cutting-costs-38-and-slashing-environmental-impact/)

生成摘要时出错

---

## 78. Turn your dumb messages into cuneiform tablets

**原文标题**: Turn your dumb messages into cuneiform tablets

**原文链接**: [https://dumbcuneiform.com](https://dumbcuneiform.com)

生成摘要时出错

---

## 79. AI is different

**原文标题**: AI is different

**原文链接**: [https://www.antirez.com/news/155](https://www.antirez.com/news/155)

生成摘要时出错

---

## 80. Hyundai wants loniq 5 customers to pay for cybersecurity patch in baffling move

**原文标题**: Hyundai wants loniq 5 customers to pay for cybersecurity patch in baffling move

**原文链接**: [https://www.neowin.net/news/hyundai-wants-ioniq-5-customers-to-pay-for-cybersecurity-patch-in-baffling-move/](https://www.neowin.net/news/hyundai-wants-ioniq-5-customers-to-pay-for-cybersecurity-patch-in-baffling-move/)

生成摘要时出错

---

## 81. Monday – A personality experiment

**原文标题**: Monday – A personality experiment

**原文链接**: [https://chatgpt.com/g/g-67ec3b78892481918c89067962526695-monday](https://chatgpt.com/g/g-67ec3b78892481918c89067962526695-monday)

生成摘要时出错

---

## 82. How randomness improves algorithms (2023)

**原文标题**: How randomness improves algorithms (2023)

**原文链接**: [https://www.quantamagazine.org/how-randomness-improves-algorithms-20230403/](https://www.quantamagazine.org/how-randomness-improves-algorithms-20230403/)

生成摘要时出错

---

## 83. Show HN: Edka – Kubernetes clusters on your own Hetzner account

**原文标题**: Show HN: Edka – Kubernetes clusters on your own Hetzner account

**原文链接**: [https://edka.io](https://edka.io)

生成摘要时出错

---

## 84. As People Ridicule GPT-5

**原文标题**: As People Ridicule GPT-5

**原文链接**: [https://gizmodo.com/as-people-ridicule-gpt-5-sam-altman-says-openai-will-need-trillions-in-infrastructure-2000643867](https://gizmodo.com/as-people-ridicule-gpt-5-sam-altman-says-openai-will-need-trillions-in-infrastructure-2000643867)

生成摘要时出错

---

## 85. Show HN: Prime Number Grid Visualizer

**原文标题**: Show HN: Prime Number Grid Visualizer

**原文链接**: [https://enda.sh/primegrid/](https://enda.sh/primegrid/)

生成摘要时出错

---

## 86. Occult books digitized and put online by Amsterdam’s Ritman Library

**原文标题**: Occult books digitized and put online by Amsterdam’s Ritman Library

**原文链接**: [https://www.openculture.com/2025/08/2178-occult-books-now-digitized-put-online.html](https://www.openculture.com/2025/08/2178-occult-books-now-digitized-put-online.html)

生成摘要时出错

---

## 87. I accidentally became PureGym’s unofficial Apple Wallet developer

**原文标题**: I accidentally became PureGym’s unofficial Apple Wallet developer

**原文链接**: [https://drobinin.com/posts/how-i-accidentally-became-puregyms-unofficial-apple-wallet-developer/](https://drobinin.com/posts/how-i-accidentally-became-puregyms-unofficial-apple-wallet-developer/)

生成摘要时出错

---

## 88. Model intelligence is no longer the constraint for automation

**原文标题**: Model intelligence is no longer the constraint for automation

**原文链接**: [https://latentintent.substack.com/p/model-intelligence-is-no-longer-the](https://latentintent.substack.com/p/model-intelligence-is-no-longer-the)

生成摘要时出错

---

## 89. Progress towards universal Copy/Paste shortcuts on Linux

**原文标题**: Progress towards universal Copy/Paste shortcuts on Linux

**原文链接**: [https://mark.stosberg.com/universal-copy-paste/](https://mark.stosberg.com/universal-copy-paste/)

生成摘要时出错

---

## 90. TextKit 2 – The Promised Land

**原文标题**: TextKit 2 – The Promised Land

**原文链接**: [https://blog.krzyzanowskim.com/2025/08/14/textkit-2-the-promised-land/](https://blog.krzyzanowskim.com/2025/08/14/textkit-2-the-promised-land/)

生成摘要时出错

---

## 91. ISR: Invertible Symbolic Regression (2024)

**原文标题**: ISR: Invertible Symbolic Regression (2024)

**原文链接**: [https://arxiv.org/abs/2405.06848](https://arxiv.org/abs/2405.06848)

生成摘要时出错

---

## 92. Flock Reports to Police If It Thinks Car Movement Patterns "Suspicious"

**原文标题**: Flock Reports to Police If It Thinks Car Movement Patterns "Suspicious"

**原文链接**: [https://www.aclu.org/news/national-security/surveillance-company-flock-now-using-ai-to-report-us-to-police-if-it-thinks-our-movement-patterns-are-suspicious?initms_aff=nat&initms_chan=pm&utm_medium=pm&initms=nat-dig-pm-awr-int-fb-social_feed-BZ30%2B-nsp-feed_SurveillanceCompanyFlockNow_20250813&utm_source=fb&utm_campaign=nat-dig-pm-awr-int&utm_content=fb-social_feed-BZ30%2B-nsp-feed_SurveillanceCompanyFlockNow_20250813&ms_aff=nat&ms_chan=pm&ms=nat-dig-pm-awr-int-fb-social_feed-BZ30%2B-nsp-feed_SurveillanceCompanyFlockNow_20250813&utm_term=pm-6748111603595-6838690309595&fbclid=IwZXh0bgNhZW0BMABhZGlkAAAGOEHIQhsBHntU-vN-zAj7VllTEkKZxwc7W3NxYS6d6L4_XI4idiZnhTYsnLyqFCbuQ6Mo_aem_dWflVIAJNk7sTdRRfrq5mg&utm_id=6544987402995](https://www.aclu.org/news/national-security/surveillance-company-flock-now-using-ai-to-report-us-to-police-if-it-thinks-our-movement-patterns-are-suspicious?initms_aff=nat&initms_chan=pm&utm_medium=pm&initms=nat-dig-pm-awr-int-fb-social_feed-BZ30%2B-nsp-feed_SurveillanceCompanyFlockNow_20250813&utm_source=fb&utm_campaign=nat-dig-pm-awr-int&utm_content=fb-social_feed-BZ30%2B-nsp-feed_SurveillanceCompanyFlockNow_20250813&ms_aff=nat&ms_chan=pm&ms=nat-dig-pm-awr-int-fb-social_feed-BZ30%2B-nsp-feed_SurveillanceCompanyFlockNow_20250813&utm_term=pm-6748111603595-6838690309595&fbclid=IwZXh0bgNhZW0BMABhZGlkAAAGOEHIQhsBHntU-vN-zAj7VllTEkKZxwc7W3NxYS6d6L4_XI4idiZnhTYsnLyqFCbuQ6Mo_aem_dWflVIAJNk7sTdRRfrq5mg&utm_id=6544987402995)

生成摘要时出错

---

## 93. "Mocha Dick," the White Whale of the Pacific

**原文标题**: "Mocha Dick," the White Whale of the Pacific

**原文链接**: [https://lithub.com/on-mocha-dick-the-white-whale-of-the-pacific-that-influenced-herman-melville/](https://lithub.com/on-mocha-dick-the-white-whale-of-the-pacific-that-influenced-herman-melville/)

生成摘要时出错

---

## 94. Simulating and Visualising the Central Limit Theorem

**原文标题**: Simulating and Visualising the Central Limit Theorem

**原文链接**: [https://blog.foletta.net/post/2025-07-14-clt/](https://blog.foletta.net/post/2025-07-14-clt/)

生成摘要时出错

---

## 95. The electric fence stopped working years ago

**原文标题**: The electric fence stopped working years ago

**原文链接**: [https://soonly.com/electric-fences/](https://soonly.com/electric-fences/)

生成摘要时出错

---

## 96. Gemma 3 270M: Compact model for hyper-efficient AI

**原文标题**: Gemma 3 270M: Compact model for hyper-efficient AI

**原文链接**: [https://developers.googleblog.com/en/introducing-gemma-3-270m/](https://developers.googleblog.com/en/introducing-gemma-3-270m/)

生成摘要时出错

---

## 97. Why LLMs can't really build software

**原文标题**: Why LLMs can't really build software

**原文链接**: [https://zed.dev/blog/why-llms-cant-build-software](https://zed.dev/blog/why-llms-cant-build-software)

生成摘要时出错

---

## 98. ADHD drug treatment and risk of negative events and outcomes

**原文标题**: ADHD drug treatment and risk of negative events and outcomes

**原文链接**: [https://www.bmj.com/content/390/bmj-2024-083658](https://www.bmj.com/content/390/bmj-2024-083658)

生成摘要时出错

---

## 99. Is chain-of-thought AI reasoning a mirage?

**原文标题**: Is chain-of-thought AI reasoning a mirage?

**原文链接**: [https://www.seangoedecke.com/real-reasoning/](https://www.seangoedecke.com/real-reasoning/)

生成摘要时出错

---

## 100. Solving the Nostr web clients attack vector

**原文标题**: Solving the Nostr web clients attack vector

**原文链接**: [https://fiatjaf.com/6829ad8b.html](https://fiatjaf.com/6829ad8b.html)

生成摘要时出错

---

