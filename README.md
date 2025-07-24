# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-07-24.md)

*最后自动更新时间: 2025-07-24 17:51:52*
## 1. 没有线程安全就没有内存安全

**原文标题**: There is no memory safety without thread safety

**原文链接**: [https://www.ralfj.de/blog/2025/07/24/memory-safety.html](https://www.ralfj.de/blog/2025/07/24/memory-safety.html)

Ralf的漫谈认为，传统上将“内存安全”和“线程安全”分开是具有误导性的，因为线程不安全可以直接导致内存安全违规，最终导致未定义行为（UB）。作者以Go为例，展示了Go中的数据竞争，特别是接口和切片中的数据竞争，如何导致内存损坏和崩溃，从而打破了该语言对内存安全的承诺。

虽然Java等其他语言允许数据竞争，但它们的设计旨在确保这些竞争产生可预测的、定义明确的结果，从而防止导致段错误的内存损坏。像Rust和Swift这样的语言采用强大的类型系统来在很大程度上消除数据竞争，并安全地处理剩余的情况。

然而，Go没有采用这两种方法中的任何一种，而是允许可能导致内存安全问题的数据竞争。虽然Go有数据竞争检测工具，但依靠测试来发现所有潜在的并发问题是不够的。作者批评了Go的内存模型文档，因为它淡化了数据竞争的严重性，并将其与具有更强线程安全保证的Java和JavaScript进行了有利的比较。

核心论点是，“安全”应该被定义为不存在未定义行为。如果一个程序可以违反语言的规范和抽象，它就会为漏洞创造温床。虽然Go可能比C等语言更安全，但它对损害内存安全的数据竞争的敏感性使其处于一个有问题的中间地带。

---

## 2. PSA: SQLite WAL校验和静默失败并可能丢失数据

**原文标题**: PSA: SQLite WAL checksums fail silently and may lose data

**原文链接**: [https://avi.im/blag/2025/sqlite-wal-checksum/](https://avi.im/blag/2025/sqlite-wal-checksum/)

本文重点介绍 SQLite 的预写式日志 (WAL) 模式及其校验和验证的一个关键问题。虽然 WAL 模式提高了写入吞吐量并包含校验和，但 SQLite 在检测到校验和不匹配时的行为可能导致静默数据丢失。

具体来说，当 SQLite 在 WAL 索引（.db-shm 文件）重建期间（这会在不干净的关闭后或 .db-shm 文件丢失时发生）检测到 WAL 中的损坏帧时，它会丢弃损坏的帧*以及所有后续帧*，即使这些后续帧未损坏。这是有意为之的行为，而不是错误。

问题在于 SQLite 在检测到损坏时不会抛出错误。相反，它会将可能不完整的 WAL 静默地检查点到主数据库文件并截断 WAL，从而导致数据丢失。当 .db-shm 文件不存在时，可能会发生这种情况，这在从其他来源接收数据库或在 WAL 写入期间系统崩溃后是一种常见情况。

作者对这种默认行为表示失望，认为应该引发一个错误，以便允许自定义错误处理和潜在的数据恢复。他们认为，当前这种“勉强维持”的方法可能适用于嵌入式环境，但对于数据完整性至关重要的应用程序来说是有问题的。虽然这种行为可能部分受到 SQLite 在存储可靠性较低的移动设备上的普及的影响，但缺乏错误报告仍然是一个问题。

---

## 3. 青少年使量子计算的重大进展过时

**原文标题**: Major Quantum Computing Advance Made Obsolete by Teenager

**原文链接**: [https://www.quantamagazine.org/teenager-finds-classical-alternative-to-quantum-recommendation-algorithm-20180731/](https://www.quantamagazine.org/teenager-finds-classical-alternative-to-quantum-recommendation-algorithm-20180731/)

本文详细介绍了18岁的唐一文如何推翻了量子加速在“推荐问题”上的一个重要论断。“推荐问题”对于亚马逊和奈飞等使用的推荐系统至关重要。

2016年，计算机科学家Kerenidis和Prakash开发了一种量子算法，据信该算法解决推荐问题的速度比任何现有的经典算法都要快指数级。这被认为是量子计算的一项重大胜利，展示了其在现实世界应用中的潜力。

然而，唐一文在Scott Aaronson指导的一个研究项目中，发现了一种经典算法，其性能几乎与量子算法一样好。这一发现基本上消除了量子霸权在推荐问题上最强有力的论据之一。

唐一文的经典算法受到了Kerenidis和Prakash使用的量子技术的启发，展示了量子算法和经典算法之间有价值的相互作用。虽然这一结果代表了量子计算的感知优势的一次挫折，但也突显了这两个领域的快速发展。该算法在量子计算研讨会上进行了非正式审查，目前正在等待正式的同行评审。尽管量子计算遭遇挫折，但这项工作突显了经典算法在响应量子创新时具有改进的潜力。

---

## 4. 使用你的类型系统

**原文标题**: Use Your Type System

**原文链接**: [https://www.dzombak.com/blog/2025/07/use-your-type-system/](https://www.dzombak.com/blog/2025/07/use-your-type-system/)

本文倡导利用编程语言的类型系统来预防因不正确使用整数、字符串和UUID等基本类型而产生的错误。作者指出，对不同实体（例如，UserID与AccountID，或华氏度与摄氏度）使用泛型会导致一种类型的错误地代替另一种类型。

解决方案是为每个实体定义特定的、不同的类型，即使它们基于相同的底层基本类型。这样可以使编译器在编译时捕获类型不匹配，从而防止运行时错误。

作者提供了使用Go的例子，展示了如何创建基于UUID的`AccountID`和`UserID`类型可以防止它们被互换使用。同样，使用`TempF`和`RelHumidity`等特定类型可以避免混淆温度刻度或意外地交换函数中的参数。

核心信息是，不同的实体应该具有不同的类型，即使它们共享相同的底层表示。这种简单的技术虽然在生产代码中很少见到，但可以显著减少一类常见的错误并提高代码的可靠性。作者鼓励开发人员充分利用类型系统，尤其是在处理ID和测量值时。

---

## 5. 英国：电话网络瘫痪：EE、BT、Three、Vodafone、O2大规模中断

**原文标题**: UK: Phone networks down: EE, BT, Three, Vodafone, O2 not working in mass outage

**原文链接**: [https://www.the-independent.com/tech/ee-bt-three-vodafone-o2-down-phone-networks-outage-latest-b2795260.html](https://www.the-independent.com/tech/ee-bt-three-vodafone-o2-down-phone-networks-outage-latest-b2795260.html)

英国主要电话网络发生大范围中断，包括英国电信、EE、Three和沃达丰，导致数百万人无法拨打或接听电话。用户在社交媒体上报告了相关问题，称无法连接通话。沃达丰和EE已承认存在问题，沃达丰表示正在努力修复。DownDetector报告显示，伦敦、伯明翰、曼彻斯特和格拉斯哥是受影响最严重的地区。虽然一些O2客户报告了问题，但该公司声称其网络运行正常，这些报告可能是由于用户试图联系受影响网络的用户造成的。目前，此次大范围中断的原因尚未得到证实。

---

## 6. 滑动取代剪刀：触摸屏的隐性成本

**原文标题**: When swiping supplants scissors: The hidden cost of touchscreens

**原文链接**: [https://caseorganic.medium.com/when-swiping-supplants-scissors-the-hidden-cost-of-touchscreens-and-how-designers-can-help-dba0fa65f5b7](https://caseorganic.medium.com/when-swiping-supplants-scissors-the-hidden-cost-of-touchscreens-and-how-designers-can-help-dba0fa65f5b7)

Amber Case 的文章《当滑动取代剪刀：触摸屏的隐性成本》探讨了过度使用触摸屏对儿童精细运动技能和认知发展可能产生的负面影响。作者认为，随着 Chromebook 等设备在课堂上占据主导地位，向数字化互动的转变减少了触觉学习体验的机会，而这些体验对于培养手眼协调能力和空间意识至关重要。

Case 引用研究、个人轶事和访谈来强调这个问题。她引用一项调查表明，教育工作者注意到年轻学生在书写和系鞋带等任务方面越来越困难。她将此与自己充满焊接和建造等动手活动的童年进行对比，强调了触觉创造力对于解决问题和未来成功的重要性。她采访了一位老师，这位老师亲眼目睹了学校的艺术和手工艺项目减少，而数字化整合却在增加。

作者引用了切斯特顿栅栏（Chesterton’s Fence）来阐述，在不理解其潜在重要性的情况下移除触觉体验可能会导致意想不到的后果。她警告说，过度依赖触摸屏可能会增加焦虑、近视以及对外部软件的依赖，从而可能阻碍认知发展。

Case 呼吁恢复触觉互动，并提出了学校、设计师和公司可以做出贡献的方式。她强调了支持手写和实体工艺认知益处的科学证据，并指出基于手写的设备具有创新潜力，并以 reMarkable 为例。她鼓励设计师探索当前技术迷恋（如 XR 头显和 AI 别针）之外的替代外形尺寸，并暗示下一个重大创新可能来自那些深入参与触觉创意活动的人。

---

## 7. 伟大的AI幻想正在破灭

**原文标题**: The great AI delusion is falling apart

**原文链接**: [https://www.mikemcbrideonline.com/2025/07/worth-reading-the-great-ai-delusion-is-falling-apart/](https://www.mikemcbrideonline.com/2025/07/worth-reading-the-great-ai-delusion-is-falling-apart/)

本文质疑了围绕人工智能生产力效益的普遍炒作，认为承诺的收益尚未在实际应用中完全实现。文章引用了一项研究，其中使用人工智能工具的经验丰富的程序员实际上比没有使用这些工具的程序员*更慢*，突显了一种“自我欺骗”，即感知的速度并未转化为实际效率。

作者批判了只关注人工智能加速的个体任务（如起草电子邮件或创建商业计划）的倾向，而没有考虑到审查、更正和验证所需的额外时间。电子邮件通信的例子说明了这一点：虽然人工智能可以快速起草回复，但缺乏清晰度或完整性可能会导致冗长的交流，从而抵消最初节省的时间。

核心论点是，真正的生产力衡量需要评估*整个*过程，从人工智能生成的输出到最终的、经过验证的产品。如果没有这种整体方法，人工智能所谓的生产力提升可能是虚幻的。文章表达了对基于未实现的生产力增长而对人工智能基础设施进行大量投资的担忧，这可能会给公司和员工带来负面后果。虽然承认人工智能在某些领域提供了真正的生产力效益，但作者强调需要对人工智能对整体生产力的影响进行更现实和全面的评估。

---

## 8. 其他

**原文标题**: Everything Else

**原文链接**: [https://newleftreview.org/sidecar/posts/everything-else](https://newleftreview.org/sidecar/posts/everything-else)

在《其他一切》中，凯特琳·多赫蒂叙述了她前往迪拜报道一场小提琴比赛的幻灭之旅。起初，她被古怪的作曲家和观察奇特景象的承诺所吸引，但很快就被这座城市奢华的表象与对其外来劳工的剥削之间鲜明对比所淹没。

多赫蒂描述了迪拜的人造现实，从用进口沙子建造的人工棕榈岛到由居住在沙漠营地的工人提供服务的豪华度假村。她将游客和富裕居民的奢华生活方式，与来自印度、巴基斯坦和其他国家的劳工的朝不保夕的生活进行了对比，这些劳工遭受恶劣的工作条件和有限的权利。

作者对参与迪拜的消费主义文化表示羞愧，在这种文化中，对其他人的剥削被常态化，甚至通过社交媒体帖子和奢侈体验来庆祝。她批判了这座城市的肤浅，强调除了沉迷于财富和被人服务之外，缺乏有意义的文化体验。

多赫蒂还反思了迪拜存在的地缘政治影响，指出该酋长国与以色列之间的牢固关系，以及该城市在为国际消费粉饰犹太复国主义方面的作用。最终，她放弃了撰写有关这次旅行的幽默叙事的尝试，意识到这只会美化一个建立在不平等和人类苦难之上的体系。相反，她认为迪拜体现了一个一切都可以出售的世界，除了爱、尊严和自由等基本价值观，这些价值观值得为之奋斗。

---

## 9. FastLanes文件格式 [pdf]

**原文标题**: The FastLanes File Format [pdf]

**原文链接**: [https://github.com/cwida/FastLanes/blob/dev/docs/specification.pdf](https://github.com/cwida/FastLanes/blob/dev/docs/specification.pdf)

这篇题为《FastLanes文件格式》的“文章”信息非常有限，主要关注一个基于网络的平台（可能为GitHub或类似代码仓库）上的FastLanes项目。内容显示，用户名“cwida”下有一个位于“Public”仓库中的“FastLanes”项目。

核心要点是，这似乎是一个公开项目，可以公开访问。此外，“Fork 19”和“Star 261”这两个指标表明该项目具有一定程度的社区参与度，说明其他人认为它有用或有趣，并Fork了该仓库（复制供自己使用）或Star了它（将其标记为收藏）。通知提示意味着用户可以登录以接收有关该项目的更新。

总而言之，该内容未提供有关文件格式本身、其用途或其技术规范的任何详细信息。它更像是指向项目的指针，而不是解释FastLanes文件格式的技术文档。要了解文件格式，需要访问仓库中的实际项目文件。

---

## 10. 我浪费了几个星期手工优化汇编，因为我用随机数据做了基准测试。

**原文标题**: I wasted weeks hand optimizing assembly because I benchmarked on random data

**原文链接**: [https://www.vidarholen.net/contents/blog/?p=1160](https://www.vidarholen.net/contents/blog/?p=1160)

作者讲述了其优化大规模分布式Java平台的VarInt编码的经历。 受益于即使是微小的性能提升的潜在影响以及利用自定义JVM优化的机会的驱动，他们开发了一种手写汇编实现，该实现使用随机数在基准测试中明显优于现有的Java版本。

然而，当部署在生产环境中时，该优化没有产生可衡量的改进。 根本原因追溯到基准测试中使用随机数，这使得数据偏向需要更多字节进行VarInt编码的大数值。 实际上，系统中处理的数据主要由小数值组成。 原始的Java实现已经可以有效地处理小数值，从而抵消了优化后的汇编代码带来的任何好处。

作者学到了关于在基准测试中使用真实数据的必要性的宝贵一课。 他们为包含大量随机数的最坏情况设计的优化，与小数值占主导地位的实际用例无关。 该更改最终被回滚，并且该努力被认为是概念验证，而不是实际的优化。 该经历突出了基于不切实际的基准进行优化的缺陷。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 2 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 3 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 4 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 5 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 6 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 7 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 8 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 9 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 10 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 11 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 12 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 13 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 14 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 15 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 16 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 17 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 18 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 19 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 20 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 21 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 22 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 23 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 24 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 25 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 26 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 27 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 28 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 29 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 30 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 31 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 32 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 33 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 34 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 35 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 36 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 37 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 38 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 39 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 40 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 41 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 42 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 43 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 44 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 45 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 46 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 47 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 48 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 49 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 50 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 51 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 52 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 53 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 54 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 55 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 56 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 57 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 58 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 59 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 60 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 61 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 62 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 63 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 64 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 65 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 66 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 67 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 68 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 69 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 70 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 71 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 72 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 73 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 74 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 75 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 76 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 77 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 78 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 79 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 80 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 81 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 82 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 83 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 84 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 85 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 86 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 87 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 88 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 89 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 90 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 91 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 92 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 93 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 94 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 95 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 96 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 97 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 98 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 99 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 100 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 101 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 102 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 103 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 104 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 105 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 106 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 107 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 108 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 109 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 110 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 111 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 112 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 113 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 114 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 115 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 116 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 117 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 118 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 119 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 120 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 121 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 122 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 123 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 124 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 125 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 126 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 127 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
