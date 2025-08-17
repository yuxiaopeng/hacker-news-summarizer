# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-08-17.md)

*最后自动更新时间: 2025-08-17 17:46:30*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 2 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 3 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 4 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 5 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 6 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 7 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 8 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 9 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 10 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 11 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 12 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 13 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 14 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 15 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 16 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 17 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 18 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 19 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 20 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 21 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 22 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 23 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 24 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 25 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 26 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 27 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 28 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 29 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 30 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 31 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 32 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 33 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 34 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 35 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 36 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 37 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 38 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 39 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 40 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 41 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 42 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 43 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 44 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 45 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 46 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 47 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 48 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 49 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 50 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 51 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 52 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 53 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 54 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 55 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 56 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 57 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 58 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 59 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 60 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 61 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 62 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 63 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 64 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 65 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 66 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 67 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 68 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 69 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 70 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 71 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 72 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 73 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 74 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 75 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 76 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 77 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 78 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 79 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 80 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 81 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 82 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 83 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 84 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 85 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 86 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 87 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 88 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 89 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 90 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 91 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 92 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 93 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 94 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 95 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 96 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 97 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 98 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 99 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 100 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 101 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 102 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 103 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 104 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 105 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 106 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 107 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 108 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 109 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 110 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 111 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 112 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 113 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 114 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 115 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 116 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 117 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 118 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 119 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 120 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 121 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 122 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 123 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 124 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 125 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 126 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 127 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 128 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 129 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 130 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 131 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 132 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 133 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 134 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 135 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 136 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 137 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 138 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 139 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 140 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 141 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 142 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 143 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 144 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 145 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 146 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 147 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 148 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 149 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 150 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 151 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
