# Hacker News 热门文章摘要 (2025-07-24)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 关于人工智能的两种叙事

**原文标题**: Two narratives about AI

**原文链接**: [https://calnewport.com/no-one-knows-anything-about-ai/](https://calnewport.com/no-one-knows-anything-about-ai/)

本文呈现了关于人工智能（尤其是大型语言模型）对计算机编程行业影响的两种相互冲突的叙述。

**叙述一：** 人工智能凭借其生成结构良好的文本的能力，有望彻底改变编程。人工智能驱动的编码工具大幅缩短任务完成时间以及大量与人工智能相关的裁员声明等案例，都支持这一观点。本文引用了一些消息来源，表明人工智能正在取代程序员，甚至学术计算机科学领域也感受到了压力。

**叙述二：** 这种观点反驳了末日预言。一项研究表明，经验丰富的开发人员在使用人工智能工具时速度较慢。一些工程师认为，人工智能是一种增强而非取代程序员的工具，将其比作木匠的台锯。微软人工智能驱动裁员的说法已被驳斥，该公司澄清裁员范围更广，旨在将资金重新分配给人工智能计划。计算机科学专业人数的下降归因于疫情时代支出后科技市场的更广泛调整。

文章最后得出结论，人工智能的影响是不确定的，并建议读者对极端说法持怀疑态度。它建议忽略过于热情和不屑一顾的观点，关注感兴趣领域中与人工智能相关的切实变化，并谨慎对待人工智能新闻，因为对其真正影响的理解仍然有限。虽然承认人工智能的重要性，但作者强调，其全部潜力和后果仍然很大程度上未知。

---

## 12. Lslvr/mwm: 最小（可用）的X11窗口管理器

**原文标题**: Lslvr/mwm: The smallest (usable) X11 window manager

**原文链接**: [https://github.com/lslvr/mwm](https://github.com/lslvr/mwm)

本文介绍了"mwm"，一款极简的X11窗口管理器，仅有20行代码，专为那些优先考虑简洁性和可修改性，而非功能和标准兼容性的用户设计。Mwm摒弃了所有常见的窗口管理器元素，如标题栏、边框、鼠标控制和虚拟桌面，一次只呈现一个全屏窗口。

作者强调该项目的重点是创建易于理解和修改的软件，与现代软件的复杂性形成对比。Mwm旨在实现基本的窗口管理功能：启动应用程序、切换窗口和关闭窗口。

用户可以使用`grab`和`map`宏来自定义mwm，为启动应用程序或执行其他操作分配快捷键，`mwm-custom.c`中提供了一个示例配置。构建过程通过`build.sh`脚本简化。作者暗示mwm提供了比TinyWM等其他小型窗口管理器更简约的替代方案，同时提供了一定程度的功能。本质上，mwm被定位为一款工具，适用于那些寻求完全控制窗口管理，并且最看重可定制性和最小资源使用的用户。

---

## 13. 用翻唱学习音乐和代码

**原文标题**: Covers as a way of learning music and code

**原文链接**: [https://ntietz.com/blog/covers-as-a-way-of-learning/](https://ntietz.com/blog/covers-as-a-way-of-learning/)

本文认为创作翻唱作品（音乐或代码）是一种宝贵的学习工具，能提供原创作品中无法获得的客观性和洞见。在学习音乐时，翻唱一首歌曲可以提供一个演奏基准，使音乐家能够识别需要改进的领域并理解原作者的选择。通过简化或改变元素，并将其与原作进行比较，学习者可以深入了解特定技术背后的“原因”。

类似地，在编程中，用 C++ 重新实现像 Boost 这样的现有库，可以让开发者理解像模板和数据结构这样复杂的概念。从头开始重新创建功能迫使他们面对设计决策，并理解特定实现背后的原理，从而通过代理向经验丰富的程序员学习。

作者解决了由于认为缺乏原创性而对创作衍生作品的常见犹豫，鼓励学习者“无论如何都要去做”。参考点的存在为比较、学习和成长提供了宝贵的机会。关键是要始终向原作者致谢，承认该作品是翻唱或重新实现，而不是完全原创的发明。作者随后提出了各种行动号召：分享帖子、订阅时事通讯、直接联系他们、寻求辅导服务，或通过 Recurse Center 加入/雇用。

---

## 14. Show HN: Nia - 为编码 Agent 提供更多上下文信息的 MCP 服务器

**原文标题**: Show HN: Nia – MCP server that gives more context to coding agents

**原文链接**: [https://www.trynia.ai/](https://www.trynia.ai/)

无法访问文章链接。

---

## 15. 兽医是高风险 curl | bash 模式的安全网

**原文标题**: Vet is a safety net for the risky curl | bash pattern

**原文链接**: [https://github.com/vet-run/vet](https://github.com/vet-run/vet)

`vet` 旨在降低常见 `curl | bash` 安装模式带来的安全风险，它是一个命令行工具。这种模式虽然方便，但涉及盲目信任和执行远程脚本，由于潜在的恶意代码、受损的服务器或不完整的下载，可能非常危险。

`vet` 提供了一种更安全的替代方案：

1.  **获取** 远程脚本到临时位置。
2.  **差异比较 & 审查** 脚本，显示自上次执行以来的更改。
3.  **代码检查** 脚本（如果安装了 `shellcheck`）以识别潜在的错误或恶意模式。
4.  **确认** 执行，需要明确的用户批准。

建议通过 Homebrew 安装（`brew tap vet-run/vet && brew install vet-run`），但也为注重安全的用户提供了手动安装。手动安装强调在执行前审查安装脚本，这体现了 `vet` 的核心原则。用法很简单：`vet <URL>`。选项包括 `--force`，用于在受信任环境中进行非交互式执行。

`vet` 需要 Bash 4+ 才能利用现代功能来提高健壮性和安全性。欢迎贡献，并提供了有关 fork、创建特性分支、测试和提交 pull request 的指南。

---

## 16. AI概览导致搜索点击量大幅下降

**原文标题**: AI overviews cause massive drop in search clicks

**原文链接**: [https://arstechnica.com/ai/2025/07/research-shows-google-ai-overviews-reduce-website-clicks-by-almost-half/](https://arstechnica.com/ai/2025/07/research-shows-google-ai-overviews-reduce-website-clicks-by-almost-half/)

皮尤研究中心新分析显示，谷歌AI概览正显著减少搜索结果中的网站点击量。该研究基于900名用户的数据，发现没有AI概览的搜索点击率为15%，而有AI概览的搜索点击率仅为8%。研究还表明，只有1%的AI概览会导致对引用来源的点击，且主要流向维基百科、YouTube或Reddit。

文章强调，用户在查看AI概览后更可能结束搜索会话，可能因AI“幻觉”而接受不准确的信息。AI概览的日益普及，尤其是在更长和基于问题的搜索中（出现在20%的搜索中），加剧了这一担忧。

谷歌对研究结果提出异议，声称该研究的方法存在缺陷，并表示AI功能为网站连接创造了新的机会。他们坚称每天有数十亿次点击导向网站，且未观察到显著的流量下降。然而，文章总结称，该研究进一步证明了谷歌的AI整合正在改变人们在线收集信息的方式，在经济上使谷歌受益，却可能损害网络出版业。该研究已于7月23日更新，包含谷歌的官方声明。

---

## 17. Thunder Compute (YC S24) 正在招聘 C++ 系统工程师

**原文标题**: Thunder Compute (YC S24) Is Hiring a C++ Systems Engineer

**原文链接**: [https://www.ycombinator.com/companies/thunder-compute/jobs/DhML6Uf-c-systems-engineer](https://www.ycombinator.com/companies/thunder-compute/jobs/DhML6Uf-c-systems-engineer)

雷霆计算(YC S24)，一家种子轮融资、收入快速增长的GPU云平台，现招聘一名C++系统工程师加入其4人团队。公司计划在6个月内将总部从亚特兰大迁至旧金山或纽约市。

核心技术挑战在于构建一个定制化的虚拟化层，通过TCP将GPU网络连接，以提高资源利用率，目标是比Lambda Labs等竞争对手提高5倍的利润率。该职位专注于优化此平台的C++核心，包括性能优化、系统调试以及对超额认购和检查点技术的研究。

理想的候选人应具备顶尖的C++能力，优化NIC/GPU性能的经验，对底层网络有深刻的理解，以及在对延迟敏感的环境中的经验。 强大的沟通能力和自我驱动的态度至关重要。 拥有美国排名前50大学的计算机科学博士/硕士学位，以及在贸易公司或像NVIDIA这样的硬件公司的经验者优先。

该职位为全职，薪资在10万至15万美元之间，外加0.5-1%的股权。 C++系统工程师将向联合创始人/首席技术官Brian（前Citadel量化开发人员）汇报。雷霆计算的目标是成为世界上最便宜的GPU云平台。

---

## 18. CARA – 使用绳索的高精度机器狗

**原文标题**: CARA – High precision robot dog using rope

**原文链接**: [https://www.aaedmusa.com/projects/cara](https://www.aaedmusa.com/projects/cara)

CARA（绞盘真的很棒）是作者最新的四足机器人，其显著特点是使用带绳索的绞盘驱动装置，而不是齿轮或滑轮来进行关节运动。这种设计具有零间隙、高扭矩透明度和安静运行等优点。

一个关键的重点是在绞盘驱动器中实现精确的8:1齿轮比，通过使用基于绳索有效直径的数值方法来克服最初的精度不足。该机器人的腿部设计采用紧凑的五杆联动机构，由绞盘驱动器提供动力，每个关节由BLDC电机驱动，并由ODrive控制。该机器人的结构框架使用碳纤维管，以获得其高强度重量比。

CARA 采用归位序列、逆/正/旋转运动学进行精确运动，并采用摆线步长轨迹实现平稳、自然的步态。至关重要的是，CARA 具有稳定性控制，使其能够在斜坡上保持平衡，并在站立和行走时从外力中恢复。

未来的改进包括更大容量的电池、更耐用的足部材料（可能是硅胶）以及改进的步态序列以克服障碍物。作者还设想增加诸如轮子、GoPro 或 LiDAR 传感器之类的附件，以及通过物体检测来增强自主能力。计划的下一个项目是 CARA 的更小、更便于构建的版本，并附带构建指南。

---

## 19. 写作即思考

**原文标题**: Writing is thinking

**原文链接**: [https://www.nature.com/articles/s44222-025-00323-4](https://www.nature.com/articles/s44222-025-00323-4)

这篇题为《写作即思考》的文章论证了在大语言模型（LLM）时代，人工撰写科学文章仍然至关重要。虽然LLM可以快速生成科学文章，但作者认为写作行为本身对于科学思考至关重要。写作使研究人员能够构建他们的思想，明确其工作的核心信息，并以更深入、更有意义的方式参与他们的发现。这一观点得到了科学证据的支持，这些证据表明手写可以增强大脑的连接性和记忆力。

文章承认LLM的潜在好处，例如辅助语法、文献检索、集思广益和克服写作障碍。然而，文章告诫不要仅仅依赖LLM进行写作，因为这些模型缺乏责任感，并且可能生成不准确的信息（“幻觉”）。编辑LLM生成的文本可能比从头开始写作更耗时，因为它需要理解LLM的推理过程。

作者认为，将整个写作过程外包给LLM剥夺了研究人员反思其领域并将他们的发现塑造成引人入胜的叙述的机会，而这种技能在科学写作之外也具有价值。文章最终倡导一种平衡的方法，即使用LLM作为工具来增强而不是取代人工科学写作。

---

## 20. 有效的HTML压缩炸弹

**原文标题**: A valid HTML zip bomb

**原文链接**: [https://ache.one/notes/html_zip_bomb](https://ache.one/notes/html_zip_bomb)

本文描述了一种有效的HTML zip炸弹的创建和实现，旨在耗尽侵略性网络爬虫的资源。作者旨在通过创建一个小型、预压缩的文件来对抗无视`robots.txt`的LLM网络爬虫，该文件解压缩后会扩展到很大的尺寸，从而压垮爬虫的RAM。

作者创建了一个Gzip炸弹，包含10MB的重复“H”字符，包裹在HTML注释中，以确保初始HTML解析有效。然后使用Nginx和`ngx_http_gzip_static_module`来提供此炸弹，预压缩该文件并防止服务器解压缩它。如果客户端支持该编码，Nginx配置会直接提供预压缩文件（Gzip或Brotli）。

作者在Firefox和Chrome中测试了该炸弹，两者都因内存不足错误而崩溃，证明了其崩溃Selenium类型网络爬虫的潜力。他们确保在`robots.txt`中禁止该炸弹，以避免影响合法的爬虫。

文章最后讨论了潜在的改进，例如改变HTML结构以防止解析器优化，并指出Brotli版本的炸弹可用于更高的压缩效率。

---

## 21. 利用安卓手机进行全球地震探测和预警

**原文标题**: Global earthquake detection and warning using Android phones

**原文链接**: [https://doi.org/10.1126/science.ads4779](https://doi.org/10.1126/science.ads4779)

无法访问文章链接。

---

## 22. AMD CEO表示，美国产台积电芯片贵5%-20%，但物有所值。

**原文标题**: AMD CEO says U.S.-made TSMC chips are 5%-20% more expensive, but worth it

**原文链接**: [https://www.tomshardware.com/tech-industry/amd-ceo-says-u-s-made-tsmc-chips-are-more-expensive-but-worth-it-costs-more-than-5-percent-but-less-than-20-percent-higher-than-taiwan-sourced-alternative](https://www.tomshardware.com/tech-industry/amd-ceo-says-u-s-made-tsmc-chips-are-more-expensive-but-worth-it-costs-more-than-5-percent-but-less-than-20-percent-higher-than-taiwan-sourced-alternative)

AMD CEO苏姿丰表示，台积电亚利桑那州工厂生产的芯片比台湾工厂生产的芯片成本更高（5%-20%）。虽然承认成本较高，但苏姿丰强调了弹性供应链的重要性，并强调了疫情期间的教训，即仅仅依靠最低成本是不够的。她认为美国制造是值得为可靠性和安全性进行的投资。

据报道，台积电亚利桑那州工厂已开始生产质量与台湾相当的4纳米芯片，尽管成本略高（估计高出10%左右），但客户愿意支付溢价，产品已售罄至2027年底。AMD预计将在今年年底前收到来自台积电亚利桑那州工厂的芯片，与苹果一起成为“美国制造”芯片的早期接收者。英伟达也正在从该基地采购一些Blackwell系统的生产。

这些进展标志着美国政府振兴国内半导体制造业的努力取得了胜利，尽管随之而来的是成本的增加。

---

## 23. Web指纹比我想象的更糟糕 (2023)

**原文标题**: Web fingerprinting is worse than I thought (2023)

**原文链接**: [https://www.bitestring.com/posts/2023-03-19-web-fingerprinting-is-worse-than-I-thought.html](https://www.bitestring.com/posts/2023-03-19-web-fingerprinting-is-worse-than-I-thought.html)

本文探讨了网站指纹识别的问题。网站指纹识别是一种网站用来识别不同会话中的用户，而无需依赖 Cookie 或其他持久性存储的技术。作者强调指纹识别如何收集有关用户浏览器和硬件配置（浏览器版本、CPU 数量、屏幕尺寸等）的数据，以生成唯一的 ID。

文章重点介绍了 FingerprintJS 这家将指纹识别作为一种服务出售的公司，展示了他们的技术如何能够准确地识别用户，即使在隐私浏览模式下或清除浏览器数据后也是如此。作者在不同的浏览器上测试了 FingerprintJS 的演示：Firefox、Chromium (Chrome) 和 Tor Browser。

结果表明，默认配置下的 Firefox 和 Chromium 容易受到指纹识别的攻击，使得 FingerprintJS 能够关联浏览会话。在 Firefox 中启用 `privacy.resistFingerprinting = true` 可以有效地缓解指纹识别，方法是屏蔽某些浏览器属性。专为隐私设计的 Tor Browser 也成功地阻止了指纹识别。

作者得出结论，网站指纹识别破坏了在线隐私，仅仅清除 Cookie 或使用隐私浏览模式不足以提供保护。为了防御指纹识别，作者建议使用 Tor Browser 或启用 `privacy.resistFingerprinting = true` 的 Firefox。 Brave 浏览器被提及作为 Chromium 用户的替代方案，但由于其对 Google 引擎的依赖，并未完全认可。 VPN 被认为对指纹识别无效，因为它们仅屏蔽 IP 地址。

---

## 24. BGP.Tools：浏览互联网生态系统

**原文标题**: BGP.Tools: Browse the Internet Ecosystem

**原文链接**: [https://bgp.tools/](https://bgp.tools/)

BGP.Tools 是一个网站，提供浏览和分析互联网生态系统的工具，尤其侧重于 BGP（边界网关协议）数据。它提供了一个用户友好的界面，包含频繁更新的外部数据，旨在成为理解互联网路由的宝贵资源。

该网站识别用户的连接详情，包括 IPv4 地址 (172.200.183.244)、相关组织（Microsoft Corporation - AS8075）和分配的 IP 范围 (172.200.0.0/13)。 它还尝试测量延迟（第 7 层和第 4 层）和 MSS（最大分段大小），但结果最初不可用，并标记为“探测中...”。

该网站提供“Looking Glass”功能，并提供 Cloudflare、LINX LON1 和 Google DNS Prefix 等示例。 它还维护一个变更日志，记录最近的更新，条目从 2025 年 7 月到 2024 年 10 月不等。

BGP.Tools 免费提供近乎实时的 BGP 数据和用户友好的界面。 付费用户可以访问额外的服务，如 BGP 网络监控和 IRR（互联网路由注册表）数据库监控。

---

## 25. 打造优美宜居街区的一系列改进建议

**原文标题**: A list of changes to make it easier to build beautiful and walkable places

**原文链接**: [https://chrisbarber.co/A+list+of+changes+to+make+it+easier+to+build+beautiful+%26+walkable+places](https://chrisbarber.co/A+list+of+changes+to+make+it+easier+to+build+beautiful+%26+walkable+places)

克里斯·巴伯的这篇文章可能概述了一系列为促进美观且利于行人的环境建设所需的变革。虽然提示中未提供具体变更，但我们可以根据城市规划和步行友好性的总体原则推断出一些常见主题和建议：

这篇文章可能认为，当前的法规和实践常常阻碍了理想城市空间的创造。潜在的变更可能包括：

*   **分区改革：** 摆脱严格的单一用途分区，允许混合用途开发，在步行距离内结合住宅、商业和休闲空间。这可能涉及在适当区域允许更高密度住宅，并减少停车位要求。

*   **简化许可流程：** 减少官僚障碍，简化开发商建设步行友好型混合用途项目的审批流程。这可能涉及更快的审查时间和更清晰、更可预测的法规。

*   **优先发展行人和自行车基础设施：** 投资建设人行道、自行车道和人行横道，为非机动交通创造安全舒适的环境。

*   **鼓励公共交通：** 扩大和改善公共交通选择，以减少对汽车的依赖，并促进交通枢纽附近的步行友好性。

*   **设计指南：** 实施优先考虑美学吸引力、人体尺度和社区特征的设计指南，确保新开发项目有助于公共领域的美丽和活力。

*   **停车改革：** 减少或取消最低停车位要求，允许开发商建设更少的停车位，并将更多资金投入到利于行人的设施中。

*   **财政激励：** 为建设步行友好型混合用途项目的开发商提供税收减免或其他财政激励。

核心论点是，实施这些变更将带来更宜居、经济更具活力、环境更可持续的社区。

---

## 26. Apache HTTP服务器：“RewriteCond expr”总是求值为真

**原文标题**: Apache HTTP Server: 'RewriteCond expr' always evaluates to true

**原文链接**: [https://github.com/apache/httpd/commit/8abb3d06b23975705ebcf4bf4476464fd0b9bd0b](https://github.com/apache/httpd/commit/8abb3d06b23975705ebcf4bf4476464fd0b9bd0b)

本文重点介绍了 Apache HTTP 服务器 `mod_rewrite` 模块中的一个 bug 修复，具体位于 `mod_rewrite.c` 文件中。该问题表现为 'RewriteCond expr' 总是评估为 true，而忽略了实际被测试的条件。

该修复解决了一个 `apply_rewrite_cond` 函数中的缺陷。原始代码无条件地将返回代码（`rc`）设置为 `COND_RC_MATCH`，如果该条件不是正则表达式。修正后的代码引入了一个检查，以确保条件评估的结果（`rc`）大于 0，然后才将 `rc` 设置为 `COND_RC_MATCH`。这确保了 RewriteCond 表达式能够正确反映条件的实际结果，从而解决了“总是为真”的评估问题。此更改还更新了反向引用信息 (`briRC`)。

本质上，添加了一行代码来正确处理非 regex `RewriteCond` 指令的评估，防止它们总是评估为 true，从而避免了意外的重写行为。这确保了 `RewriteCond` 指令能够按预期工作，从而实现更准确和可控的 URL 重写。

---

## 27. 不使用归一化的Transformer

**原文标题**: Transformers Without Normalization

**原文链接**: [https://arxiv.org/abs/2503.10622](https://arxiv.org/abs/2503.10622)

这篇题为“无归一化Transformer”的arXiv文章提出了一种构建Transformer网络的新方法，该方法消除了对传统归一化层的需求。作者朱嘉晨、陈新磊、何恺明、Yann LeCun和刘壮提出了一种简单而有效的替代方案：动态Tanh (DyT)。 DyT是一种逐元素操作，定义为`DyT(x) = tanh(alpha * x)`，其灵感来自于Transformer层归一化中常见的S形输入-输出映射。

核心发现是，包含DyT的Transformer可以在各种任务中实现与归一化Transformer相当甚至超过的性能。 研究人员证明了DyT在从图像识别到文本生成，以及从监督学习到自监督学习等设置中的有效性。 重要的是，这种性能提升主要是在没有进行大量超参数调整的情况下实现的。

作者认为，这些结果挑战了长期以来认为归一化层在现代神经网络中必不可少的观点，并为它们在深度学习中的作用提供了新的见解。 该论文已提交至CVPR 2025，并包含一个项目页面（链接在摘要中）。 该文章被归类于机器学习（cs.LG），以及人工智能（cs.AI）、计算与语言（cs.CL）和计算机视觉与模式识别（cs.CV）类别下。 该文章自首次提交以来已经过一次修订。

---

## 28. XOR_singleheader: 仅头文件的二进制融合和XOR过滤器库

**原文标题**: XOR_singleheader: Header-only binary fuse and XOR filter library

**原文链接**: [https://github.com/FastFilter/xor_singleheader](https://github.com/FastFilter/xor_singleheader)

此仅头文件C库提供了Binary Fuse和Xor Filter的实现，为成员资格测试提供了比Bloom Filter更快更紧凑的替代方案。与Bloom Filter不同，这些过滤器易于压缩。该库支持8位(`binary_fuse8_t`)和16位(`binary_fuse16_t`)版本，以内存使用换取更低的假阳性概率。

该库提供了过滤器分配、填充、包含测试和释放的函数。序列化和反序列化支持解包（更快）和打包（可能更小）两种格式，并提供了示例代码。该库假定使用64位整数键，对于其他数据类型需要进行哈希处理。

文档还提供了C++示例以及关于内存需求（构建期间每个条目24字节）、测试和基准测试说明的信息。它强调了错误报告和修复的重要性，同时不鼓励仅基于静态分析器警告的问题，除非识别出真正的错误。最后，它包含了指向其他编程语言实现的链接。

---

## 29. 蒸馏让AI模型更小更便宜

**原文标题**: Distillation makes AI models smaller and cheaper

**原文链接**: [https://www.quantamagazine.org/how-distillation-makes-ai-models-smaller-and-cheaper-20250718/](https://www.quantamagazine.org/how-distillation-makes-ai-models-smaller-and-cheaper-20250718/)

知识蒸馏：AI模型瘦身的利器

Quanta Magazine的这篇文章探讨了知识蒸馏，这是一种AI领域的基础技术，用于创建更小、更高效的AI模型。其核心思想是使用一个大型、昂贵的“教师”模型来训练一个较小、资源消耗较少的“学生”模型。

这个概念源于Geoffrey Hinton等人于2015年发表的一篇谷歌论文，他们试图将“暗知识”（关于错误答案的相对可能性的信息）从复杂的集成模型转移到一个更精简的单一模型。这是通过使用“软目标”实现的，软目标是不同分类的概率分布，而不是仅仅是最可能的答案。这使得学生能够理解类别之间的关系。

尽管最初被忽视，但随着AI模型规模和成本的增长，蒸馏变得越来越重要。它成为一种流行的减少大型模型（如BERT）计算负担的方法，从而促成了DistilBERT等更高效版本的开发。蒸馏现在被广泛使用，并被主要科技公司作为一项服务提供。

这篇文章还探讨了DeepSeek R1聊天机器人引发的担忧，据传该机器人使用了蒸馏来模仿OpenAI的o1模型。文章澄清说，直接蒸馏需要访问教师模型的内部运作方式，但学生模型可以通过精心设计的提示和答案从教师那里学习。

文章最后指出，目前正在进行对蒸馏新应用的研究，例如训练思维链推理模型，突显了其在AI领域中的持续重要性。

---

## 30. 电动汽车产生的刹车粉尘污染远低于燃油车。

**原文标题**: Electric cars produce far less brake dust pollution than combustion-engine cars

**原文链接**: [https://modernengineeringmarvels.com/2025/07/22/surprising-science-how-electric-cars-quietly-transform-urban-air/](https://modernengineeringmarvels.com/2025/07/22/surprising-science-how-electric-cars-quietly-transform-urban-air/)

电动汽车显著减少刹车粉尘污染：研究表明再生制动大幅降低排放

---

## 31. 约定的局域网

**原文标题**: The Promised LAN

**原文链接**: [https://tpl.house/](https://tpl.house/)

应许之地局域网是一个私有的、永久在线的局域网聚会网络，于2021年建立，并在一个网站上记录，作为成员和潜在成员的资源。它强调社交和技术方面的平衡，并在其宣言中详细说明。

该网络采用骨干架构来保持可扩展性。各个局域网段连接到最近的骨干节点，这些节点使用strongSwan和iked独立运行，并且这些节点通过IPSec链接使用特定的加密算法进行IKE和子SA（分别为HMAC SHA2 512、AES 256/ChaCha20 Poly1305和Curve25519）进行对等互联。骨干网在一个专用的/24分配上运行，并使用BGP (bird/bgpd)来广播用户局域网。

DNS使用非标准的".tpl" TLD进行管理，授权域名服务器托管在不同的局域网中以实现冗余。每个局域网都应以固定的IP运行其自己的授权域名服务器，并且运行unbound的递归解析器在骨干网上进行任播。

对于启用TLS的服务，该局域网运行自己的x509证书颁发机构，其生命周期为三年，使用ECDSA P-384密钥和SHA384签名颁发根证书，限制为DNS:.tpl和email:.tpl。证书颁发通过SSH自动完成，根据包含OpenSSH公钥的DNS TXT记录验证请求的SAN。这种方法避免了ACME的复杂性，同时仍在应许之地局域网的受控环境中提供安全的证书管理。

---

## 32. WiX工具集：引入开源维护费

**原文标题**: WiX Toolset: Introduce the Open Source Maintenance Fee

**原文链接**: [https://github.com/wixtoolset/issues/issues/8974](https://github.com/wixtoolset/issues/issues/8974)

本文件概述了一项提议，旨在为 WiX 工具集引入“开源维护费”，自 2025 年 4 月 5 日发布的 6.0 版本开始实施。该费用旨在为持续维护工作提供可持续的资金。

对于所有通过 WiX 工具集产生收入的消费者，该费用是强制性的，并将通过包含在 GitHub 和 NuGet.org 二进制发布版本中的 EULA 来执行。用户可以通过 GitHub Sponsors 支付，费用分级基于公司规模：小型组织（20 人以下）每月 10 美元，中型组织（20-100 人）每月 40 美元，大型组织（100 人以上）每月 60 美元。

WiX Developer Direct 的客户免除维护费，因为它已包含在他们的支持协议中。

该提议包括以下行动项目：与律师最终确定 EULA、将 EULA 添加到 .nupkgs、设置 GitHub Sponsorship 等级以及更新 README。对此提议的初步反应褒贬不一，通过 GitHub 议题的反应表达了各种正面和负面的意见。

---

## 33. OpenAI 预计八月发布 GPT-5。

**原文标题**: OpenAI prepares to launch GPT-5 in August

**原文链接**: [https://www.theverge.com/notepad-microsoft-newsletter/712950/openai-gpt-5-model-release-date-notepad](https://www.theverge.com/notepad-microsoft-newsletter/712950/openai-gpt-5-model-release-date-notepad)

本文报道了OpenAI预计将于8月初发布的GPT-5。据消息人士和OpenAI首席执行官Sam Altman的暗示，新模型拥有改进的功能，包括高级推理(o3)，并将推出可通过API访问的迷你版和纳米版。GPT-5旨在统一OpenAI的模型，并有可能实现AGI，这将影响微软在OpenAI利润中的股份。

文章还提到，OpenAI即将发布一个开源语言模型，与"o3 mini"类似，预计在GPT-5发布之前。

除了OpenAI的新闻之外，文章还强调了微软最近的安全问题，包括中国黑客组织利用的SharePoint漏洞，以及对微软雇佣位于中国的工程师协助美国国防部计算机系统的做法的担忧。微软正在通过限制护送计划，仅限于位于美国的员工进入政府云数据中心来回应后者的担忧。

其他涵盖的主题包括：

* 微软致力于Windows 11的性能改进。
* 微软电影和电视商店的突然关闭。
* 英伟达和联发科基于Arm的Windows CPU可能延期。
* 《天外世界2》放弃79.99美元的价格标签。
* GitHub推出其AI应用制作工具GitHub Spark。
* Maingear的Retro95 PC，采用复古设计和现代组件。
* 微软新款基于英特尔的Surface Laptop 5G将于8月发布。
* Xbox云游戏集成到跨设备的游戏历史记录中。
* 新的AI功能正在推广到Windows 11。
* WhatsApp从原生Windows应用切换到网页版。
* 通过安卓手机远程锁定PC。
* 微软从谷歌DeepMind聘请AI人才。
* Windows 11即将推出的新共享音频功能。

---

## 34. 英格兰足球主场优势消退

**原文标题**: Vanishing home field advantage in English football

**原文链接**: [https://blog.engora.com/2025/07/vanishing-home-field-advantage-in.html](https://blog.engora.com/2025/07/vanishing-home-field-advantage-in.html)

本博文分析了1888年至2024-2025赛季英格兰足球主场优势减弱的趋势。作者使用了两个主要指标：每场比赛主场进球优势（主场进球数减去客场进球数）和主场胜率（主场获胜的比例）。

分析表明，随着时间的推移，所有英格兰足球联赛的主场优势都呈现明显的下降趋势。一个显著的例外是2020-2021赛季，该赛季大部分时间由于COVID-19而没有观众，主场优势几乎消失。这表明主场球迷的支持是构成优势的主要因素。

2025年，主场优势约为0.25个进球。

作者探讨了长期下降的潜在原因，排除了诸如旅行便利或联赛特定变化等因素。相反，他们提出了球员体能/训练、客队球迷旅行增加以及裁判偏见等可能的促成因素。作者倾向于客队球迷和裁判偏见的假设。

文章总结说，目前的趋势表明主场优势将持续下降，最终可能消失。它还提出了保持球迷对俱乐部的支持的重要性，因为它似乎是创造主场优势的重要因素。

---

## 35. Detekt – Kotlin 静态代码分析器

**原文标题**: Detekt – A static code analyzer for Kotlin

**原文链接**: [https://detekt.dev/](https://detekt.dev/)

Detekt：一款 Kotlin 静态代码分析工具，旨在帮助开发者编写更清晰的代码并专注于软件构建。它能轻松集成到 Gradle、Maven 和 Bazel 等各种构建系统中，并支持包括 Android、JVM、JS、Native 和 Multiplatform 在内的广泛 Kotlin 项目。Detekt 具有高度可扩展性，允许开发者创建自定义规则来识别和修复代码库中的特定反模式。作为一个开源项目，Detekt 由社区驱动，鼓励在 GitHub 上进行贡献和协作，以改进和塑造该工具的未来。本质上，Detekt 旨在简化代码分析，提高代码质量，并促进 Kotlin 项目的更轻松维护。

---

## 36. 美国人工智能行动计划

**原文标题**: US AI Action Plan

**原文链接**: [https://www.ai.gov/action-plan](https://www.ai.gov/action-plan)

本文件概述了“美国人工智能行动计划”，旨在确保美国在人工智能领域的领先地位，以促进经济增长、国家安全和社会进步。该计划基于三大支柱。

**支柱一：加速人工智能创新：** 侧重于通过消除监管障碍、确保人工智能保护言论自由和美国价值观、鼓励开源人工智能以及促进人工智能在各行业的应用来促进私营部门主导的创新。它强调赋能美国工人、支持下一代制造业、投资于人工智能驱动的科学、构建科学数据集以及推进人工智能科学本身。此外，它还促进人工智能的可解释性、稳健性，构建人工智能评估生态系统，加速人工智能在政府部门的应用，保护人工智能创新，并打击合成媒体。

**支柱二：构建美国人工智能基础设施：** 解决对大幅增加能源生产以支持人工智能发展的需求。它包括简化半导体制造和能源基础设施的审批流程、开发与人工智能创新相匹配的电网、恢复美国半导体制造业、建设高安全数据中心、培养技术工人队伍以及加强关键基础设施的网络安全。该计划还提倡安全设计的人工智能技术，并建立成熟的联邦人工智能事件响应能力。

**支柱三：引领国际人工智能外交与安全：** 旨在促进美国人工智能系统、硬件和标准在全球范围内的采用。这包括向盟友出口美国人工智能、抵制中国在国际治理中的影响力、加强对人工智能计算和半导体制造的出口管制、在全球范围内协调保护措施、确保美国政府在评估国家安全风险方面发挥主导作用，以及投资于生物安全。该计划力求防止对手利用美国的创新成果。

---

## 37. 解开童年谜题：BASIC游戏如何学会获胜

**原文标题**: Solving a Childhood Mystery: How BASIC Games Learned to Win

**原文链接**: [https://sublevelgames.github.io/blogs/2025-07-20-basic-game-hexapawn/](https://sublevelgames.github.io/blogs/2025-07-20-basic-game-hexapawn/)

本文深入探讨David H. Ahl的《BASIC电脑游戏》中Hexapawn游戏的BASIC代码，探索看似简单的程序如何学会获胜。Hexapawn是一种迷你象棋变体，涉及各有三个棋子的两名玩家，目标是消灭对方棋子或到达棋盘的另一端。

作者剖析了代码中具有挑战性的DATA部分，解释了它如何存储可能的棋局状态以及计算机可以采取的相应行动。计算机通过最初从预定集合中选择随机行动来“学习”。当计算机失败时，导致失败的特定行动将从其技能中删除，从而有效地从错误中学习。

代码将当前的棋盘状态与存储的状态进行匹配，然后选择一个动作，必要时水平翻转棋盘。AI使用诸如FNM和FNR之类的函数来操纵棋盘和棋子位置。

最终，这种简单地删除失败走法是AI学习的关键。在36场比赛中输掉大约11场之后，AI达到了接近完美的水平。文章将Hexapawn的学习机制与Donald Michie的MENACE联系起来，MENACE是一种用于井字棋的火柴盒学习机器，突出了通过反复试验来加强好棋并消除坏棋的类似原理。

---

## 38. Jitsi隐私漏洞允许一键式隐蔽音视频捕获

**原文标题**: Jitsi privacy flaw enables one-click stealth audio and video capture

**原文链接**: [https://zimzi.substack.com/p/jitsi-privacy-flaw-that-enables-one](https://zimzi.substack.com/p/jitsi-privacy-flaw-that-enables-one)

文章《Jitsi隐私漏洞可一键隐蔽录制音视频》详细描述了在Jitsi Meet开源视频会议平台中发现的一个重大安全漏洞。该漏洞允许恶意行为者在用户不知情或未经同意的情况下，静默地远程激活用户的麦克风和摄像头，从而实现一键隐蔽录制音视频。

该漏洞源于Jitsi对焦点权限的处理方式。当会议参与者获得焦点权限时，他们有权执行某些操作，包括静音/取消静音参与者。该漏洞允许恶意用户操纵这些权限，以在无需任何显式用户交互或许可的情况下，静默地取消目标用户的静音并启用摄像头。这意味着目标用户不会看到任何视觉提示或警告，表明他们的麦克风和摄像头已激活。

该漏洞利用需要攻击者存在于Jitsi会议中。但是，它只需要最少的技术技能，并且一旦攻击者获得焦点权限（或通过利用这些权限分配方式的弱点），就可以相对容易地触发。这使其特别危险。

作者强调了此漏洞的严重隐私影响，突出了窃听、监视和未经授权录制敏感对话和活动的可能性。文章敦促Jitsi用户保持警惕，并在漏洞完全修复和验证之前，可能考虑替代解决方案。它还强调了定期更新软件以减轻安全风险的重要性。

---

## 39. 展示一下：Tinder，但只有我妻子的照片，而且我只能右滑

**原文标题**: Show HN: Tinder but it's only pictures of my wife and I can only swipe right

**原文链接**: [https://trytender.app/](https://trytender.app/)

此“Show HN”帖子展示“Tender”，一个为专门浏览用户配偶照片而设计的Tinder约会应用的个性化版本。其主要功能是用户只能右滑，意味着对展示的图像表达无条件的积极情感。本质上，它是一个以Tinder的滑动界面呈现的数字相册，专门用于欣赏和互动伴侣的图像。该项目是对一个流行应用的趣味性重新构想，将其机制重新用于更亲密和个人的目的。其核心理念是通过熟悉且引人入胜的界面来庆祝和不断确认对爱人的感情。它可以作为一种轻松的，潜在的每日提醒，提醒积极的情感。

---

## 40. 构建更好的AI工具

**原文标题**: Building better AI tools

**原文链接**: [https://hazelweakly.me/blog/stop-building-ai-tools-backwards/](https://hazelweakly.me/blog/stop-building-ai-tools-backwards/)

本文认为当前人工智能工具的构建方式“本末倒置”，导致人类技能退化而非增强其能力。作者认为人工智能应增强人类流程，而非取代它们，并借鉴认知科学的学习原则来支持这一观点。

核心论点围绕人类如何有效学习：通过检索练习（回忆信息），专注于过程而非死记硬背，以及擅长在群体内进行累积迭代。然而，当前的人工智能工具通常跳过人类的检索和启动环节，阻碍知识转移并导致从业者技能退化。

作者提出了一种基于“解释、演示、引导、增强”（EDGE）方法的新型人工智能交互模型，将人工智能重新定义为“心不在焉的指导者”而非同事。人工智能不应自动启动行动，而应建议遗漏的步骤、解释流程、演示查询、在用户遇到困难时提供指导，并通过建议改进和捕获团队学习来增强未来的行动。

本文以可观测性工具的事件管理为例，将常见的反模式（如自动响应）与所提出的EDGE方法进行了对比。作者还简要地谈到了代码生成，提倡人工智能首先生成文档、架构图、测试计划和测试，然后再生成实际的代码。总的主题是加强人类学习、促进协作、加速过程执行以及将团队学习融入工具的输出中。

---

## 41. 矢量瓦片已部署在OpenStreetMap.org上。

**原文标题**: Vector Tiles are deployed on OpenStreetMap.org

**原文链接**: [https://blog.openstreetmap.org/2025/07/22/vector-tiles-are-deployed-on-openstreetmap-org/](https://blog.openstreetmap.org/2025/07/22/vector-tiles-are-deployed-on-openstreetmap-org/)

OpenStreetMap.org 在其基础服务器上部署了矢量瓦片，为 OSM 网站上的地图绘制者和访客提供了更清晰、更快的视觉层。 经过数月的测试和改进，专注于可靠性和速度，这标志着一项重要的技术升级。

矢量瓦片的一个主要优势是其适应性，允许开发者基于现有的 Shortbread 样式创建自定义样式，或者使用 OSMF 托管的瓦片开发新的样式。 鼓励开发者查阅矢量瓦片使用策略以进行项目实施，并注意到该策略在发布后可能会不断发展。

Shortbread 规范和样式将继续发展，欢迎就样式、瓦片生成和瓦片内容规范分别在 spirit、tilekiln 和 shortbread-tiles 存储库中提供反馈。

---

## 42. 前所未有地解析 Protobuf

**原文标题**: Parsing Protobuf like never before

**原文链接**: [https://mcyoung.xyz/2025/07/16/hyperpb/](https://mcyoung.xyz/2025/07/16/hyperpb/)

本文介绍 hyperpb，这是一款新的高性能 Go Protobuf 解析器，其性能优于现有的解决方案，如 Protobuf Go 生成的代码和 vtprotobuf。作者详细介绍了 hyperpb 的设计原则和内部运作机制，从 UPB（一种快速的基于 C 的 Protobuf 运行时）中汲取灵感，同时适应 Go 的独特特性和局限性。

hyperpb 的主要优势包括其运行时动态特性，这意味着它不需要提前编译类型，以及其通过在线剖面引导优化 (PGO) 实现的 Protobuf JIT 编译器。这种方法使 hyperpb 能够适应运行时遇到的特定消息类型，从而提高性能。

本文深入探讨了实现细节，重点介绍了核心组件：`tdp`（对象代码格式）、`tdp/compiler`（用于转换消息描述符）、`tdp/dynamic`（用于动态消息类型）、`tdp/vm`（解释器）和 `tdp/thunks`（布局和解析器的原型）。优化措施包括字段调度、用于不经常设置字段的“冷区域”以及旨在利用 Go 的寄存器 ABI 实现最大性能的解析器 VM。该解析器巧妙地使用函数指针（虚拟调用）来分派解析逻辑，发现由于现代 CPU 的间接分支预测能力，这种方法比复杂的分支迷宫更快。 hyperpb 还利用 PGO 来优化字段排序和冷区域的使用。

---

## 43. 尼尔·阿姆斯特朗的月球岩石报关单 (2016)

**原文标题**: Neil Armstrong's customs form for moon rocks (2016)

**原文链接**: [https://magazine.uc.edu/editors_picks/recent_features/armstrong/moonrocks.html](https://magazine.uc.edu/editors_picks/recent_features/armstrong/moonrocks.html)

本文探讨了一个令人惊讶的事实：尼尔·阿姆斯特朗、巴兹·奥尔德林和迈克尔·柯林斯在阿波罗11号登月任务返回后，被要求填写美国海关申报单。这份“通用申报单”将他们的出发地列为“月球”，目的地列为夏威夷檀香山。他们申报的物品是“月球岩石和月球尘埃样本”。

这份海关申报单幽默地突出了严格的规章制度，询问宇航员是否携带了植物、食物、动物、土壤、病原体、细胞培养物，甚至是蜗牛。值得注意的是，“健康申报”部分包括一个关于船上可能导致疾病传播的任何情况的问题，对此宇航员谨慎地回答说：“待定”。

本文赞扬了加州大学的校友卢阿玛·梅斯，感谢他与《加州大学杂志》分享了这份申报单的副本。梅斯是一名飞行员，在阿姆斯特朗担任加州大学教授期间与他结为好友。阿姆斯特朗曾找到梅斯，想乘坐他那架与他用于登月舱训练的直升机一模一样的旧直升机。本文还包括了关于尼尔·阿姆斯特朗的生活、职业生涯以及与辛辛那提大学的联系的相关报道链接。

---

## 44. Lumo：隐私优先的AI助手

**原文标题**: Lumo: Privacy-first AI assistant

**原文链接**: [https://proton.me/blog/lumo-ai](https://proton.me/blog/lumo-ai)

Lumo：一款注重隐私的AI助手，由Proton（ProtonMail背后的公司）开发，旨在替代那些优先考虑数据收集和监控的大型科技公司提供的AI产品。Lumo强调用户隐私和对数据的控制，确保对话的保密性，永不分享或出售，也不会用于训练AI模型。

关键隐私功能包括：无服务器端日志、保存的聊天记录零访问加密、不与第三方共享数据，以及不使用用户数据进行AI模型训练。Lumo基于开源语言模型，并在Proton的欧洲数据中心运营，提供更高的透明度。

Lumo提供诸如网页搜索、文件上传和Proton Drive集成等生产力功能，同时保持用户隐私。“幽灵模式”允许用户进行在关闭后立即消失的聊天。用户无需帐户即可免费开始使用Lumo。付费的“Lumo Plus”订阅提供对高级功能和无限次查询的访问权限。

由于围绕监控提案存在法律不确定性，Proton正将其包括Lumo在内的物理基础设施迁出瑞士，并在欧盟投资超过1亿欧元，以开发一个主权的EuroStack。

---

## 45. 我喝了每一种鸡尾酒。

**原文标题**: I drank every cocktail

**原文链接**: [https://aaronson.org/blog/i-drank-every-cocktail](https://aaronson.org/blog/i-drank-every-cocktail)

作者记录了自己为了喝遍国际调酒师协会(IBA)官方鸡尾酒单上所有酒品的历程。这份鸡尾酒单被认为是全球“最受欢迎”的经典酒品清单。 从21岁成年后的一份随意“合法鸡尾酒”清单开始，逐渐演变成一项完成IBA清单的使命，当时的清单包含89款鸡尾酒。

作者描述了IBA清单、它的历史、分类（经典永恒、当代经典和新时代经典），以及最初寻找和尝试许多鸡尾酒的容易程度。书中叙述了作者在从简陋酒吧到高端场所的各种酒吧遇到的调酒师。值得一提的是，伦敦的撒旦胡须酒吧之行被证明是宝贵的，因为它拥有丰富的鸡尾酒知识，并且愿意调制冷门饮品。

任务进行到一半时，IBA更新了清单，增加了16种新鸡尾酒，删除了3种，总数达到102种。 这带来了巨大的挑战，尤其是“IBA提基”鸡尾酒的引入，这款鸡尾酒包含9种成分，包括在美国无法获得的古巴朗姆酒，而且关于这款饮品的信息有限。 这一变化重新激发了作者完成更新清单的决心，文章到此结束。

---

## 46. 为什么要用 Elixir？常见误解

**原文标题**: Why Elixir? Common misconceptions

**原文链接**: [https://matthewsinclair.com/blog/0181-why-elixir](https://matthewsinclair.com/blog/0181-why-elixir)

Elixir：现代软件开发的卓越平台

---

## 47. 一个解析意大利邮政PDF账单的Python工具

**原文标题**: A Python tool to parse PDF statements from Poste Italiane

**原文链接**: [https://github.com/genbs/poste-italiane-parser](https://github.com/genbs/poste-italiane-parser)

本文档介绍了一个名为`poste-italiane-parser`的Python工具，该工具旨在自动解析意大利邮政(Poste Italiane)的PDF账单，并将其转换为结构化的JSON或CSV数据。它面向拥有“conto postale”账户的用户，提供了一种从BancoPosta账单和Postepay报告等文档中提取信息的解决方案。

主要功能包括自动文档类型检测、数据验证以确保财务数据完整性，以及对JSON和CSV输出格式的支持。该工具支持批量处理，允许用户分析单个PDF或整个文档目录。

安装过程包括克隆GitHub仓库，导航到该目录，并使用`pip`安装必要的Python依赖项。该脚本从命令行使用，接受输入PDF路径、输出格式（JSON或CSV）和输出路径等参数。还提供详细日志记录选项。

该解析器也可以作为库在Python项目中使用。

输出数据以JSON格式结构化，提供文档类型、货币、期初和期末余额、IBAN、持有人信息、卡号、账号、期间（起始和结束日期）、客户信息（姓名、街道、城市）以及包含会计日期、价值日期、描述、借方和贷方等详细信息的交易列表等信息。

测试需要创建包含每个测试用例的预期输出的`.test.json`文件。然后可以使用`unittest`运行测试套件。欢迎贡献，该项目采用MIT许可证。

---

## 48. Debian/Trixie 有哪些值得期待的

**原文标题**: What to expect from Debian/Trixie

**原文链接**: [https://michael-prokop.at/blog/2025/07/20/what-to-expect-from-debian-trixie-newintrixie/](https://michael-prokop.at/blog/2025/07/20/what-to-expect-from-debian-trixie-newintrixie/)

本文概述了Debian 13 “Trixie”（预计于2025年8月9日发布）的系统管理员关注点，重点介绍了作者为升级所做的准备工作，并指出了需要注意的关键变更。

作者建议查阅官方Debian发布说明以获取全面信息，并敦促读者查看“Debian 13 的新功能”。

文章的大部分内容详细介绍了与Debian 12 “Bookworm”相比的软件包版本升级，涵盖了Ansible、Apache、Docker、各种数据库（MariaDB、Postgres）和编程语言（Python、Go、Ruby、Rust）等重要软件。

文章随后深入探讨了核心系统组件中的具体变更和新功能：

*   **apt:** 引入了彩色输出、改进的可读性、Sequoia签名验证、新的求解器、源列表的现代化（`apt modernize-sources`）、distclean命令、内核管理改进以及`apt-key`的移除。
*   **systemd:** 重点介绍了升级到v257、潜在的命名方案变更，并列出了诸如`run0`、`systemd-ac-power`等新工具以及现有`systemd`工具的众多新选项。 还有几个新的二进制包也随Debian的systemd一起发布。
*   **Linux Kernel:** 文章详细说明了Trixie附带Linux内核版本6.12，列出了新的Debian软件包（linux-bpf-dev、intel-sdsi、virtme-ng），用于内核模块的xz压缩、新的系统调用以及对文件系统、网络和硬件支持的各种改进。

文章还涉及了特定软件，并提及了配置管理，特别是Puppet，以及Debian中可用的版本。

---

## 49. 欧洲自 inflicted 的云危机

**原文标题**: Europe's Self Inflicted Cloud Crisis

**原文链接**: [https://berthub.eu/articles/posts/our-self-inflicted-cloud-crisis/](https://berthub.eu/articles/posts/our-self-inflicted-cloud-crisis/)

欧洲正面临一场自 inflicted 的“云危机”，因为它过度依赖亚马逊、微软和谷歌等美国云服务提供商。文章认为，这种依赖威胁着欧洲的主权，并将敏感数据暴露在美国的控制之下，尤其是在当前的政治气候下。

作者认为，认为没有这些美国云就无法进行计算的说法是错误的。欧洲拥有充足的基础设施来租赁服务器、存储和带宽，但缺乏同等的“预制”云服务，导致供应商锁定和使用美国云的高成本。作者批评了将核心国家服务外包给美国公司的趋势，使其受到美国间谍法的影响。

这篇文章提倡一种双管齐下的方法：首先，欧洲软件开发人员和 IT 专业人员应该重新学习如何在本地可用的服务器和数据库上部署软件，而不是依赖专有的美国云服务。其次，应该支持像 EuroStack 这样开发强大的欧洲云替代方案的努力。

作者驳斥了认为有必要甚至可行完全克隆 AWS 的想法。相反，他鼓励利用现有的欧洲基础设施和能力，并强调了像 OpenTK.nl 这样的系统的成功。他敦促决策者考虑数字殖民的长期成本，并强调做出政治决策以支持欧洲技术独立的重要性。关键是保留本地有效的东西，推广欧洲云选项，并改进内部服务器部署流程。

---

## 50. Itch.io：关于成人内容的更新

**原文标题**: Itch.io: Update on NSFW Content

**原文链接**: [https://itch.io/updates/update-on-nsfw-content](https://itch.io/updates/update-on-nsfw-content)

由于支付处理商的压力，itch.io已将其浏览和搜索页面上所有成人NSFW内容取消索引。这一决定是由组织Collective Shout发起的一项活动引发的，该组织对itch.io上的内容提出了担忧，特别提到了游戏“No Mercy”（此前已被禁止）。

取消索引是一项临时措施，在此期间，itch.io将对其内容进行全面审查，以确保符合支付处理商的政策。审查结束后，他们将实施新的合规措施，包括要求NSFW内容的创作者确认其内容符合其关联支付处理商的政策。部分页面将被永久删除，受影响的帐户持有人将收到电子邮件通知。

itch.io对此次更改的突然性和破坏性表示歉意，并解释说情况发展迅速，需要立即采取行动以保护平台的支付基础设施。他们恳请用户耐心和理解，因为他们正在应对这一充满挑战的时期。他们承诺在情况发展变化时提供进一步的更新。

---

## 51. ICEBlock，iOS 独占

**原文标题**: ICEBlock, an iOS Exclusive

**原文链接**: [https://daringfireball.net/2025/07/iceblock](https://daringfireball.net/2025/07/iceblock)

本文讨论了ICEBlock，这是一款iOS独占应用，旨在允许用户匿名举报其附近的移民及海关执法局（ICE）活动。该应用提供5英里半径范围内的实时更新，并在四小时后自动删除目击报告，通过不存储任何个人数据来优先保护用户隐私。

本文强调了ICE因侵犯公民权利和正当程序而面临的批评，并将ICEBlock定位为一种赋能社区以保持知情的工具。本文将ICEBlock与苹果公司此前将HKmap.live应用从App Store中移除的决定进行了对比，后者曾帮助香港的亲民主人士。作者认为，苹果公司可能面临移除ICEBlock的压力，特别是来自特朗普政府的压力。

一个关键论点是ICEBlock的iOS独占性的技术论证。开发者声称，安卓的推送通知系统需要存储设备ID，这将损害用户匿名性并创建一个脆弱的数据库。另一方面，iOS允许在不存储用户可识别信息的情况下进行推送通知，从而使ICEBlock能够坚持其完全匿名的承诺。作者希望苹果公司能够捍卫该应用的存在及其独特的隐私功能。

---

## 52. 大型面向对象失误：三十五年错误的剖析

**原文标题**: The Big OOPs: Anatomy of a Thirty-Five Year Mistake

**原文链接**: [https://www.computerenhance.com/p/the-big-oops-anatomy-of-a-thirty](https://www.computerenhance.com/p/the-big-oops-anatomy-of-a-thirty)

Casey Muratori 发布了他在 Better Software Conference 上所做的 “重大 OOPs：三十五年错误的剖析” 演示文稿。为了准确地呈现历史原貌，他进行了广泛的研究，查阅了数百页的原始资料，但为了将演示时间控制在两小时以内，他不得不省略了一些引人入胜的故事。

他正在考虑进行直播，讨论演讲中未提及的其他文档，并鼓励读者在评论中表达他们的兴趣。他还提供了四个历史资料的链接，供那些想要进一步探索该主题的人参考：

*   Alan Kay 的 **Smalltalk 的早期历史**：详细介绍了 Smalltalk 的发展，有助于理解 Smalltalk 对“类层次结构”的处理方式的细微差别。
*   Bjarne Stroustrup 的 **C++ 历史**：Stroustrup 对 C++ 的回顾，也可以作为他的书《C++ 的设计与演化》的第一章。
*   Ole-Johan Dahl 和 Kristen Nygaard 的 **Simula 语言的开发**：涵盖了 Simula I 和 Simula 67 的创建，其中首次出现了类和虚函数。
*   Douglass T. Ross 的 **自动编程工具 APT 语言的起源**：强调了 1956 年的 “plex”，作为“使用高度结构化数据进行编程”的早期示例。 Muratori 很好奇 “plex” 是否真的是这种范式的最早实例。他鼓励读者分享他们所知道的任何更早的例子。

---

## 53. 打破旋转错觉：攻击者视角与AWSKeyLockdown (2024)

**原文标题**: Shattering the rotation illusion: The attacker view and AWSKeyLockdown (2024)

**原文链接**: [https://www.clutch.security/blog/shattering-the-rotation-illusion-part-6-the-attackers-perspective-and-introducing-awskeylockdown](https://www.clutch.security/blog/shattering-the-rotation-illusion-part-6-the-attackers-perspective-and-introducing-awskeylockdown)

粉碎轮换幻觉：攻击者视角及AWSKeyLockdown介绍

本文“粉碎轮换幻觉：攻击者视角及AWSKeyLockdown介绍”是揭露传统密钥轮换对AWS密钥不足的一系列文章的总结。它强调了攻击者如何迅速利用泄露的AWS访问密钥，通常在几分钟甚至几秒钟内，即使GitHub的秘密扫描触发了AWSCompromisedKeyQuarantineV2。 文章认为，这种隔离策略提供了一种虚假的安全感，因为攻击者仍然可以进行侦察、数据泄露、权限提升、成本产生，甚至在受损环境中建立后门。

作者强调，仅仅依靠密钥轮换和自动检测是不够的，并提倡从根本上转向积极的安全措施，如零信任和临时身份。他们批评AWS建议删除暴露的密钥，却没有提供立即禁用它们的机制，这与GCP立即撤销暴露的服务帐户密钥的积极方法形成对比。

文章介绍了AWSKeyLockdown，这是作者构建的一个开源工具，一旦应用AWSCompromisedKeyQuarantineV2策略，该工具会立即撤销AWS访问密钥，从而防止攻击者利用它们。 作者最终呼吁组织超越静态密钥，拥抱现代安全方法，以更好地防御暴露凭证的风险，并强调迫切需要保护代码、CI/CD和SaaS应用程序中的非人类身份。

---

## 54. Colodebug：一种改进Bash脚本调试的简单方法 (2021)

**原文标题**: Colodebug: A simple way to improve bash script debugging (2021)

**原文链接**: [https://johannes.truschnigg.info/writing/2021-12_colodebug/](https://johannes.truschnigg.info/writing/2021-12_colodebug/)

本文介绍了一种名为“Colodebug”的简单方法，通过利用冒号（`:`）命令来增强 Bash 脚本调试，以获取运行时上下文信息。它通过将源代码注释纳入调试输出，解决了标准调试技术（如 `set -x` (xtrace)）的局限性。

其核心思想是将标准井号（`#`）注释替换为“冒号注释”（`: This is a colon comment`）。当启用 xtrace (`bash -x`) 时，这些注释会显示出来，从而在脚本执行期间提供有价值的上下文。

本文还通过将冒号命令重新定义为一个充当“详细模式”触发器的函数来进一步增强此功能。通过设置 `COLODEBUG` 环境变量，以 `::` 开头的注释（`: :: verbose message`）将被打印到 stderr。这允许选择性地启用详细调试消息，而无需更改脚本的核心逻辑。

文章末尾提供的脚本允许开发人员为“:”合并一个函数定义，该定义允许冒号注释。如果 COLODEBUG 变量存在于环境中，则所有以“::”为前缀的注释都将打印到 stderr。

文章强调“`: ::`”不应被用作“`#`”的完全替代品，并且注释中可能存在的任何语法错误都将传递给 shell 进行解析。

总而言之，Colodebug 提供了一种最小程度干扰的方式，可以向 Bash 脚本添加上下文和详细模式，通过增强注释可见性和选择性消息输出，提高调试效率。

---

## 55. 警察说罪犯使用搭载石墨烯操作系统的谷歌Pixel手机——我说那是自由。

**原文标题**: Cops say criminals use a Google Pixel with GrapheneOS – I say that's freedom

**原文链接**: [https://www.androidauthority.com/why-i-use-grapheneos-on-pixel-3575477/](https://www.androidauthority.com/why-i-use-grapheneos-on-pixel-3575477/)

尽管有报道称西班牙警方根据个人使用的谷歌Pixel手机和石墨烯操作系统（GrapheneOS）进行侧写，但Calvin Wankhede认为，使用谷歌Pixel手机上的石墨烯操作系统不应自动等同于犯罪活动。Wankhede强调，石墨烯操作系统提供了增强的隐私和安全功能，对任何希望更好地控制自己数据的人都有益，而不仅仅是罪犯。

他详细介绍了他的个人经历，强调了安装的便捷性以及令人惊讶的与Play商店等应用程序的兼容性，尽管它缺少默认的谷歌服务。然而，主要的优势是石墨烯操作系统能够沙盒化谷歌应用程序并限制它们对数据的访问，从而赋予用户对权限的精细控制。诸如紧急密码（duress PIN）之类的功能，该功能会永久删除所有数据，进一步增强了安全性。

Wankhede认为，使用石墨烯操作系统是关于行使对设备的自主权和控制权，而不是隐藏什么。他批评了石墨烯操作系统和Signal等隐私增强工具所面临的审查，并将此与加泰罗尼亚的飞马间谍软件丑闻相提并论，在加泰罗尼亚，政府监视是一个真正的威胁。他总结说，使用隐私工具不应自动使一个人成为嫌疑人，并且基于这种使用的侧写是错误的。作者指出，开源软件的开发者无法控制谁使用他们的软件做好事或坏事，这就是自由的概念的运作方式。

---

## 56. 清单很难，但仍然是好事。

**原文标题**: Checklists are hard, but still a good thing

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/sysadmin/ChecklistsAreHardButGood](https://utcc.utoronto.ca/~cks/space/blog/sysadmin/ChecklistsAreHardButGood)

Chris Siebenmann：“清单很难，但仍然是件好事”是一则通知，解释了部分用户可能被阻止访问其博客 Wandering Thoughts 及相关 CSpace Wiki 的原因。问题源于旨在打击机器人活动激增（尤其是在 2025 年初）的激进反爬虫措施，其目的是收集数据以进行 LLM 训练。

Siebenmann 正在阻止具有可疑旧版 User-Agent 的浏览器（主要是 Chrome），因为许多爬虫会伪装成过时的浏览器身份。这意味着使用旧版浏览器或使用 archive.org 以外的存档服务的合法用户可能会被错误地阻止。

这篇文章专门针对 archive.today、archive.ph 和 archive.is 的用户，指出这些服务通过使用旧版 Chrome User-Agent 值、利用广泛分布的 IP 地址以及有时伪造反向 DNS 条目来模仿恶意爬虫行为。 他建议使用 archive.org 代替，因为它是一个更符合道德规范的爬虫。

如果用户认为他们在使用当前浏览器的情况下被错误地阻止，Siebenmann 鼓励他们通过其大学电子邮件地址与他联系，并提供他们的浏览器详细信息和 User-Agent 字符串。目标是减少恶意爬虫造成的服务器负载，同时尽量减少对真实用户的干扰。

---

## 57. 七姐妹星团掩星将暂时遮蔽星光。

**原文标题**: Seven Sisters eclipse will temporarily block stars from view

**原文链接**: [https://www.discovermagazine.com/the-sciences/the-seven-sisters-eclipse-will-temporarily-block-stars-from-view](https://www.discovermagazine.com/the-sciences/the-seven-sisters-eclipse-will-temporarily-block-stars-from-view)

2025年7月20日，美国和加拿大的天文爱好者可以观测到“七姐妹星食”，届时残月将从昴星团前方经过，暂时遮挡住它们。 这次事件，严格来说是月掩星，并不特别罕见，自2023年9月以来每月都会发生，并将持续到2029年7月，但可见度因地点而异。

要观看这次星食，请在清晨时分看向东方地平线，确保视野清晰且光污染最小。 无需特殊设备；即使是城市居民也能看到，但较暗的地点提供更好的观看效果。

昴星团，也被称为梅西耶45或七姐妹星团，是由一千多颗年轻恒星组成的星团，其中最亮的几颗可以用肉眼看到。 它们位于金牛座，距离地球约445光年。

此外，2025年7月还提供其他天文事件：7月21日和22日，金星将出现在新月附近，木星则在地平线上。 7月28日，火星将在新月附近。 整个前半夜，鹰座也将出现在东方天空。

---

## 58. 关于烹饪肉类的一项主要规则被证明是错误的

**原文标题**: Major rule about cooking meat turns out to be wrong

**原文链接**: [https://www.seriouseats.com/meat-resting-science-11776272](https://www.seriouseats.com/meat-resting-science-11776272)

丹尼尔·格里泽的文章挑战了长期以来人们认为的“静置肉类使其更鲜嫩多汁”的观点。他认为，静置肉类的真正好处在于温度控制，特别是控制后熟效应。

传统观点认为，静置可以让肌肉纤维放松并重新吸收烹饪过程中被挤压到中心的汁液，从而防止切片时汁液流失。然而，格里泽强调了一些对此提出质疑的研究，特别是引用了 AmazingRibs.com 网站的 Meathead 的观点，他认为感知到的多汁性是复杂的，而且与影响酥脆度的因素相比，跳过静置步骤造成的任何汁液流失都微不足道。

克里斯·杨的实验进一步挑战了传统观点。杨使用预测温度计证明，当肉在相同的最终内部温度下切片时，静置对汁液流失没有可测量的影响。格里泽解释说，之前的测试未能考虑到后熟效应，这会导致肉在静置时继续在内部烹饪，从而导致切片时的最终温度不同。

格里泽进行了自己的感官测试，使用猪排和一个受控环境来评估在相同内部温度下切片的静置和未静置样品之间的多汁性。他发现后熟效应被严重低估，并且发生得很快，这使得在遵循传统静置建议时难以实现一致的切片温度。

最终，该文章得出结论，静置肉类应被视为一种控制温度以防止因后熟效应导致过度烹饪的方法，而不是一种保留汁液的方法。

---

## 59. 有轨电车-火车

**原文标题**: Tram Trains

**原文链接**: [https://www.worksinprogress.news/p/tram-trains](https://www.worksinprogress.news/p/tram-trains)

本文倡导采用“有轨电车-火车”作为中小型城市和大型城镇经济高效的公共交通解决方案。“有轨电车-火车”车辆既可以在传统铁路线路上运行，也可以在市中心的有轨电车网络上运行，从而无需乘客换乘，并提高了现有铁路线路的运力。

德国卡尔斯鲁厄市是一个成功的案例，其有轨电车和火车网络的整合显著提高了客流量并扩展了公交系统。本文承认整合不同的铁路和有轨电车系统存在技术挑战，例如不同的电压和信号系统，但认为这些挑战是可以克服的。

文章讨论了几种轻轨的替代模型，包括专用有轨电车线路（如曼彻斯特）和有轨电车-地铁（如杜塞尔多夫），后者涉及城市中心下方的隧道。文章还提到了连接城镇的昔日“城际铁路”，通过在街道上运行解决了“最后一英里问题”。

作者总结认为，通过将郊区铁路线路连接到现有的有轨电车网络，并提供直达市中心的交通，有轨电车-火车为改善牛津（英国）、图尔（法国）和夏洛特（美国）等城市的公共交通提供了一种实用且经济的方式。虽然并不适合所有城市，但有轨电车-火车为许多缺乏更广泛地铁系统资源的城市提供了一种可行的解决方案。

---

## 60. FastVLM：视觉语言模型的高效视觉编码

**原文标题**: FastVLM: Efficient Vision Encoding for Vision Language Models

**原文链接**: [https://machinelearning.apple.com/research/fast-vision-language-models](https://machinelearning.apple.com/research/fast-vision-language-models)

本文介绍了FastVLM，一种新型视觉语言模型(VLM)，旨在改善视觉查询处理中的精度-延迟权衡，使其适用于实时设备端应用。其关键创新是使用一种名为FastViTHD的混合视觉编码器，该编码器针对高分辨率图像进行了优化。

传统的VLM面临一个挑战：更高的图像分辨率提高了精度，但也显著增加了处理时间和token数量，导致性能下降。FastVLM通过使用FastViTHD来解决这个问题，它结合了卷积块和transformer块，从而在精度和速度之间取得更好的平衡。研究人员发现FastViTHD优于纯粹基于transformer或卷积的编码器。

FastVLM优于现有的token剪枝和合并方法，并提供了更简单高效的架构。动态平铺是另一种处理高分辨率图像的方法，只有在极高的分辨率下与FastVLM结合使用时才有效益。对比测试表明，FastVLM比其他类似大小的流行VLM更快、更准确。

一个iOS/macOS演示应用程序展示了FastVLM的设备端效率，突显了其近实时性能的潜力，并实现了新的设备端AI体验。研究人员强调，FastVLM的高效设计使其能够应用于精度和速度都至关重要的实际应用中。

---

## 61. Manticore Search：快速、高效、可替代 Elasticsearch 的即时可用方案

**原文标题**: Manticore Search: Fast, efficient, drop-in replacement for Elasticsearch

**原文链接**: [https://github.com/manticoresoftware/manticoresearch](https://github.com/manticoresoftware/manticoresearch)

Manticore Search 是一款快速的开源搜索数据库，旨在作为 Elasticsearch 的直接替代品。 它在特定用例中拥有比 Elasticsearch 和 MySQL 显著的性能优势，速度比 MySQL 快高达 182 倍，比 Elasticsearch 快高达 29 倍。 它具有现代化的多线程架构、行式和列式存储选项、用于高效索引的 PGM 索引以及基于成本的查询优化器。

Manticore 优先使用 SQL，兼容 MySQL 协议，并提供 PHP、Python、Java、Go 和 Rust 等多种语言的客户端。 它还提供具有 Elasticsearch 兼容写入功能的 HTTP JSON 协议。 Manticore 使用 C++ 构建，内存占用小，支持实时插入、多主复制以及从 MySQL、PostgreSQL 和 CSV 等各种来源的数据同步。

主要功能包括全文搜索、丰富的过滤、模糊搜索、分面搜索、地理空间搜索、向量搜索、表连接、拼写校正、自动完成和 NLP 功能。 它还支持流过滤、高可用性以及通过备份工具实现的数据安全性。

Manticore 集成了 ProxySQL、Grafana 和 Kibana 等各种工具，并提供一个列式库。 安装选项包括 Docker、适用于各种操作系统的软件包以及 Elestio 和 Hosting Ukraine 等云平台。 该项目提供文档、互动课程和社区支持。 用户可以通过捐赠或成为客户来支持 Manticore，该项目已获得 GPLv3 许可。

---

## 62. YouTube 如何赢得电视观众之战

**原文标题**: How YouTube won the battle for TV viewers

**原文链接**: [https://www.wsj.com/business/media/how-youtube-won-the-battle-for-tv-viewers-346d05b8](https://www.wsj.com/business/media/how-youtube-won-the-battle-for-tv-viewers-346d05b8)

无法访问文章链接。

---

## 63. C语言交互式编程 (2014)

**原文标题**: Interactive Programming in C (2014)

**原文链接**: [https://nullprogram.com/blog/2014/12/23/](https://nullprogram.com/blog/2014/12/23/)

本文描述了如何在 C 语言中实现交互式编程，允许在不重启的情况下修改和扩展正在运行的程序。作者受到了 Casey Muratori 的 Handmade Hero 项目的启发。关键技术是将应用程序的大部分构建为共享库。这需要避免全局和静态变量，以防止重新加载时状态丢失。由于潜在的全局状态，C 标准库的使用也可能受到限制。仔细管理函数指针对于防止重新加载后出现问题至关重要。

本文使用生命游戏演示作为示例。该程序分为两个部分：“游戏”共享库和一个“主”包装器。包装器定期加载、重新加载和调用共享库，与游戏的运行无关。

“游戏”通过一个 `game_api` 结构体暴露其 API，该结构体包含用于初始化、最终化、重新加载、卸载和步进游戏的函数指针。该库导出一个全局变量 `GAME_API`，它是这个结构体的已填充实例。

包装器使用 `dlopen()`、`dlsym()` 和 `dlclose()` 来加载和卸载共享库。它使用 `stat()` 跟踪库的 inode，以确定它是否已更新。`game_load()` 函数处理加载库、检查更新以及处理潜在的错误，例如编译仍在进行中。主循环重复调用 `game_load()`，如果成功，则执行游戏的 `step()` 函数。作者总结说，这种技术开启了用 C 语言开发具有交互式开发的完整游戏的可能性。

---

## 64. 小小的七月网络

**原文标题**: A small web July

**原文链接**: [https://smallcypress.bearblog.dev/a-small-web-july/](https://smallcypress.bearblog.dev/a-small-web-july/)

在2025年6月29日发布的题为“小型网络七月”的帖子中，作者“fern_enjoyer”提出了一项自我挑战，旨在减少七月份在“企业网络”上花费的时间，并寻求其他人加入共享问责制结构。目标是通过尽量减少接触算法驱动、引人注意的平台来重塑大脑，并优先考虑现实生活中的互动。

具体规则包括避免像Meta、Reddit和潜在的Bluesky这样的围墙花园式社交媒体，但每天与清醒互助小组进行一次签到除外。作者还计划限制在YouTube（发现页面）、新闻（15分钟）和充满广告的无限滚动网站（如Pinterest）上花费的时间，而是专注于构建他们的RSS阅读器、网站以及使用静态站点生成器的技能。

作者打算将重点转移到现实世界，遵循奥利弗·伯克曼的建议，让自己沉浸在实际活动中。个人策略包括使用新的笔记本电脑来处理滚动浏览的冲动，清理和整理他们的物理环境，使用所需内容（包括通过RSS订阅的YouTube频道）扩展他们的RSS源，增加现实生活中的社交互动，以及追求步行、烘焙、绘画、游泳等技能培养活动。在追求更多积极习惯的同时，作者强调自我同情和方法的灵活性，优先考虑幸福感而不是严格遵守规则。作者将在他们的博客（可通过RSS访问）上发布更新，并邀请读者通过电子邮件（fern_enjoyer at tutamail dot com）或帖子分享的任何地方进行联系。

---

## 65. WebAssembly何时才能获得DOM支持？

**原文标题**: When Is WebAssembly Going to Get DOM Support?

**原文链接**: [https://queue.acm.org/detail.cfm?id=3746174](https://queue.acm.org/detail.cfm?id=3746174)

这篇发表于2025年7月的ACM Queue文章探讨了WebAssembly (Wasm) 何时能获得直接DOM支持。文章认为，虽然真正的直接DOM访问可能并非首要任务，但由于Wasm与JavaScript的互操作性，它已经为Web应用程序做好了生产准备。

Wasm的设计本质上将其与JavaScript分离，这与asm.js不同。文章解释说，无需创建新的Wasm专用Web API（如DOM），现有的JavaScript API就已足够。Wasm模块可以通过编译器生成的粘合代码与JavaScript代码交互。这种粘合代码允许Wasm调用JavaScript函数，进而与DOM交互。

文章详细介绍了Wasm如何通过引用JavaScript数组的整数索引系统来建模复杂的数据结构（如对象）。虽然这引入了一定程度的间接性，但作者认为性能损失通常低于与在浏览器中运行代码相关的其他开销。

文章承认了早期方法（如模拟异常或阻塞I/O）导致的限制和减速。然而，最近的WebAssembly进展侧重于通过优化Wasm和JavaScript之间的调用、添加原生异常处理、启用JavaScript Promises的暂停以及允许直接引用堆栈上的JavaScript值来提高性能。

作者讨论了使用Wasm组件模型来提供对Web API更直接访问的可能性，并将其与Web IDL进行了类比。然而，文章指出，鉴于Web IDL目前以JavaScript为中心以及浏览器实现中的细微差异，调整Web IDL的复杂性。最终，文章得出结论：虽然直接DOM访问仍然是一个长期的可能性，但当前的Wasm和JavaScript集成是实用的，并且还在不断改进。

---

## 66. Kimi-K2 技术报告 [pdf]

**原文标题**: Kimi-K2 Tech Report [pdf]

**原文链接**: [https://github.com/MoonshotAI/Kimi-K2/blob/main/tech_report.pdf](https://github.com/MoonshotAI/Kimi-K2/blob/main/tech_report.pdf)

MoonshotAI的“Kimi-K2技术报告”展示了他们的项目“Kimi-K2”，该项目似乎在技术社区中引起了广泛关注。报告重点介绍了以下关键信息：

*   **来源：** 该报告来自MoonshotAI，一家从事人工智能研发的公司或组织。
*   **项目名称：** 重点是“Kimi-K2”，可能是一个特定的人工智能模型、应用程序或研究计划。
*   **公开可用性：** 该存储库可公开访问，表明MoonshotAI具有一定程度的开放性和透明度。
*   **社区参与：** 该项目已获得相当大的关注，平台上有7000个星标和441个Fork可以证明这一点。这表明社区活跃参与、贡献或使用该项目。
*   **平台功能：** 该报告使用了通知、Fork和Star等平台功能。

本质上，该报告表明MoonshotAI的一个潜在的值得关注的人工智能项目（“Kimi-K2”）已引起了相当数量的开发者和研究人员的共鸣，促使他们公开参与该项目。 Kimi-K2本身的技术或研究细节在提供的文本中未详细说明，但其受欢迎程度表明了创新。

---

## 67. 小妖精、根本原因及其他神话

**原文标题**: Leprechauns, root causes, and other fairy tales

**原文链接**: [https://www.tomdalling.com/blog/software-processes/leprechauns-root-causes-and-other-fairy-tails/](https://www.tomdalling.com/blog/software-processes/leprechauns-root-causes-and-other-fairy-tails/)

This talk challenges the common practice of root cause analysis after incidents, arguing that it's a flawed approach based on a misunderstanding of how complex systems fail. Drawing heavily from Richard Cook's paper "How Complex Systems Fail," the speaker asserts that incidents in complex systems aren't caused by a single "root cause," but rather by the convergence of multiple failures.

Complex systems, like banks or large software systems, are inherently hazardous and constantly operating in a degraded mode, experiencing minor failures all the time. These systems are heavily defended against failure, preventing small issues from escalating into major catastrophes. However, these defenses are imperfect, and major incidents occur when multiple failures align and slip through the defensive layers.

The speaker emphasizes that attributing accidents to a single "root cause" is fundamentally wrong and driven by a social need for blame (scapegoating). Root cause analysis often leads to the addition of new rules and processes, paradoxically increasing complexity and potentially raising the risk of future incidents. Instead of focusing on finding a scapegoat, the speaker suggests exploring alternative models like the Swiss cheese model of accident causation. The core message is that root causes are mythical, akin to leprechauns, and a more nuanced understanding of complex systems is needed for effective incident management and risk reduction.


---

## 68. System View for Inspecting DSM Registry Allocations in PostgreSQL

**原文标题**: System View for Inspecting DSM Registry Allocations in PostgreSQL

**原文链接**: [https://tselai.com/pg-dsm-registry-allocations](https://tselai.com/pg-dsm-registry-allocations)

生成摘要时出错

---

## 69. Reverse engineering GitHub Actions cache to make it fast

**原文标题**: Reverse engineering GitHub Actions cache to make it fast

**原文链接**: [https://www.blacksmith.sh/blog/cache](https://www.blacksmith.sh/blog/cache)

生成摘要时出错

---

## 70. Geocities Backgrounds

**原文标题**: Geocities Backgrounds

**原文链接**: [https://pixelmoondust.neocities.org/archives/archivedtiles/backgroundsindex](https://pixelmoondust.neocities.org/archives/archivedtiles/backgroundsindex)

生成摘要时出错

---

## 71. AI coding agents are removing programming language barriers

**原文标题**: AI coding agents are removing programming language barriers

**原文链接**: [https://railsatscale.com/2025-07-19-ai-coding-agents-are-removing-programming-language-barriers/](https://railsatscale.com/2025-07-19-ai-coding-agents-are-removing-programming-language-barriers/)

生成摘要时出错

---

## 72. A diverse cast of rocky worlds around a small star revealed by astronomers

**原文标题**: A diverse cast of rocky worlds around a small star revealed by astronomers

**原文链接**: [https://nouvelles.umontreal.ca/en/article/2025/07/22/a-udem-team-confirms-a-fifth-potentially-habitable-planet-around-l-98-59-a-red-dwarf-35-l/](https://nouvelles.umontreal.ca/en/article/2025/07/22/a-udem-team-confirms-a-fifth-potentially-habitable-planet-around-l-98-59-a-red-dwarf-35-l/)

生成摘要时出错

---

## 73. Mathematics for Computer Science (2024)

**原文标题**: Mathematics for Computer Science (2024)

**原文链接**: [https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/)

生成摘要时出错

---

## 74. SIMD Perlin Noise: Beating the Compiler with SSE (2014)

**原文标题**: SIMD Perlin Noise: Beating the Compiler with SSE (2014)

**原文链接**: [https://scallywag.software/vim/blog/simd-perlin-noise-i](https://scallywag.software/vim/blog/simd-perlin-noise-i)

生成摘要时出错

---

## 75. Extending Emacs with Fennel (2024)

**原文标题**: Extending Emacs with Fennel (2024)

**原文链接**: [https://andreyor.st/posts/2024-12-20-extending-emacs-with-fennel/](https://andreyor.st/posts/2024-12-20-extending-emacs-with-fennel/)

生成摘要时出错

---

## 76. You can now disable all AI features in Zed

**原文标题**: You can now disable all AI features in Zed

**原文链接**: [https://zed.dev/blog/disable-ai-features](https://zed.dev/blog/disable-ai-features)

生成摘要时出错

---

## 77. I'm Unsatisfied with Easing Functions

**原文标题**: I'm Unsatisfied with Easing Functions

**原文链接**: [https://www.davepagurek.com/blog/easing-functions/](https://www.davepagurek.com/blog/easing-functions/)

生成摘要时出错

---

## 78. Show HN: The missing link of a bookstore's tech stack

**原文标题**: Show HN: The missing link of a bookstore's tech stack

**原文链接**: [https://bookhead.net/](https://bookhead.net/)

生成摘要时出错

---

## 79. Using Radicle CI

**原文标题**: Using Radicle CI

**原文链接**: [https://radicle.xyz/2025/07/23/using-radicle-ci-for-development](https://radicle.xyz/2025/07/23/using-radicle-ci-for-development)

生成摘要时出错

---

## 80. SQL Injection as a Feature

**原文标题**: SQL Injection as a Feature

**原文链接**: [https://idiallo.com/blog/sql-injection-as-a-feature](https://idiallo.com/blog/sql-injection-as-a-feature)

生成摘要时出错

---

## 81. Cerebras launches Qwen3-235B, achieving 1.5k tokens per second

**原文标题**: Cerebras launches Qwen3-235B, achieving 1.5k tokens per second

**原文链接**: [https://www.cerebras.ai/press-release/cerebras-launches-qwen3-235b-world-s-fastest-frontier-ai-model-with-full-131k-context-support](https://www.cerebras.ai/press-release/cerebras-launches-qwen3-235b-world-s-fastest-frontier-ai-model-with-full-131k-context-support)

生成摘要时出错

---

## 82. Qwen3-Coder: Agentic coding in the world

**原文标题**: Qwen3-Coder: Agentic coding in the world

**原文链接**: [https://qwenlm.github.io/blog/qwen3-coder/](https://qwenlm.github.io/blog/qwen3-coder/)

生成摘要时出错

---

## 83. Show HN: TheProtector – Linux Bash script for the paranoid admin on a budget

**原文标题**: Show HN: TheProtector – Linux Bash script for the paranoid admin on a budget

**原文链接**: [https://github.com/IHATEGIVINGAUSERNAME/theProtector](https://github.com/IHATEGIVINGAUSERNAME/theProtector)

生成摘要时出错

---

## 84. 低延迟网络中令人惊讶的 gRPC 客户端瓶颈

**原文标题**: The Surprising gRPC Client Bottleneck in Low-Latency Networks

**原文链接**: [https://blog.ydb.tech/the-surprising-grpc-client-bottleneck-in-low-latency-networks-and-how-to-get-around-it-69d6977a1d02](https://blog.ydb.tech/the-surprising-grpc-client-bottleneck-in-low-latency-networks-and-how-to-get-around-it-69d6977a1d02)

生成摘要时出错

---

## 85. Morally corrupt innovations are the easiest innovations to create

**原文标题**: Morally corrupt innovations are the easiest innovations to create

**原文链接**: [https://ceoretort.com/journal/ethics/2025/05/16/morally-corrupt-innovations-are-the-easiest-innovations-to-create-its-the-lazy-approach-with-dangerous-consequences/](https://ceoretort.com/journal/ethics/2025/05/16/morally-corrupt-innovations-are-the-easiest-innovations-to-create-its-the-lazy-approach-with-dangerous-consequences/)

生成摘要时出错

---

## 86. Rescuing two PDP-11s from a former British Telecom underground shelter (2023)

**原文标题**: Rescuing two PDP-11s from a former British Telecom underground shelter (2023)

**原文链接**: [https://forum.vcfed.org/index.php?threads/rescuing-two-pdp-11-systems-in-uk-from-a-former-big-british-telecom-underground-shelter-in-central-london.1244723/page-2](https://forum.vcfed.org/index.php?threads/rescuing-two-pdp-11-systems-in-uk-from-a-former-big-british-telecom-underground-shelter-in-central-london.1244723/page-2)

生成摘要时出错

---

## 87. The Cells That Breathe Two Ways

**原文标题**: The Cells That Breathe Two Ways

**原文链接**: [https://www.quantamagazine.org/the-cells-that-breathe-two-ways-20250723/](https://www.quantamagazine.org/the-cells-that-breathe-two-ways-20250723/)

生成摘要时出错

---

## 88. Checking Out CPython 3.14's remote debugging protocol

**原文标题**: Checking Out CPython 3.14's remote debugging protocol

**原文链接**: [https://rtpg.co/2025/06/28/checking-out-sys-remote-exec/](https://rtpg.co/2025/06/28/checking-out-sys-remote-exec/)

生成摘要时出错

---

## 89. AI groups spend to replace low-cost 'data labellers' with high-paid experts

**原文标题**: AI groups spend to replace low-cost 'data labellers' with high-paid experts

**原文链接**: [https://www.ft.com/content/e17647f0-4c3b-49b4-a031-b56158bbb3b8](https://www.ft.com/content/e17647f0-4c3b-49b4-a031-b56158bbb3b8)

生成摘要时出错

---

## 90. SETI at the Extremes

**原文标题**: SETI at the Extremes

**原文链接**: [https://www.centauri-dreams.org/2025/07/22/seti-at-the-extremes/](https://www.centauri-dreams.org/2025/07/22/seti-at-the-extremes/)

生成摘要时出错

---

## 91. Reversing a Fingerprint Reader Protocol (2021)

**原文标题**: Reversing a Fingerprint Reader Protocol (2021)

**原文链接**: [https://blog.th0m.as/misc/fingerprint-reversing/](https://blog.th0m.as/misc/fingerprint-reversing/)

生成摘要时出错

---

## 92. Org tutorials

**原文标题**: Org tutorials

**原文链接**: [https://orgmode.org/worg/org-tutorials/index.html](https://orgmode.org/worg/org-tutorials/index.html)

生成摘要时出错

---

## 93. There's a Reason Bar Ice Looks Better Than Yours (and You Can Fix It)

**原文标题**: There's a Reason Bar Ice Looks Better Than Yours (and You Can Fix It)

**原文链接**: [https://www.seriouseats.com/how-to-make-clear-cocktail-ice-11773197](https://www.seriouseats.com/how-to-make-clear-cocktail-ice-11773197)

生成摘要时出错

---

## 94. VectorDB bench now support S3Vector

**原文标题**: VectorDB bench now support S3Vector

**原文链接**: [https://github.com/zilliztech/VectorDBBench/pull/570](https://github.com/zilliztech/VectorDBBench/pull/570)

生成摘要时出错

---

## 95. Vintage Macintosh Programming Book Library (2017)

**原文标题**: Vintage Macintosh Programming Book Library (2017)

**原文链接**: [https://vintageapple.org/macprogramming/index_year.html](https://vintageapple.org/macprogramming/index_year.html)

生成摘要时出错

---

## 96. Robot scans rare library books at 2.5k pages per hour

**原文标题**: Robot scans rare library books at 2.5k pages per hour

**原文链接**: [https://www.popsci.com/technology/book-scanning-robot/](https://www.popsci.com/technology/book-scanning-robot/)

生成摘要时出错

---

## 97. Intel 18A Details and Cost, Future of DRAM 4F2 vs. 3D, Backside Power Adoption

**原文标题**: Intel 18A Details and Cost, Future of DRAM 4F2 vs. 3D, Backside Power Adoption

**原文链接**: [https://semianalysis.com/2025/07/21/vlsi2025/](https://semianalysis.com/2025/07/21/vlsi2025/)

生成摘要时出错

---

## 98. How to increase your surface area for luck

**原文标题**: How to increase your surface area for luck

**原文链接**: [https://usefulfictions.substack.com/p/how-to-increase-your-surface-area](https://usefulfictions.substack.com/p/how-to-increase-your-surface-area)

生成摘要时出错

---

## 99. Using uninitialized memory for fun and profit (2008)

**原文标题**: Using uninitialized memory for fun and profit (2008)

**原文链接**: [https://research.swtch.com/sparse](https://research.swtch.com/sparse)

生成摘要时出错

---

## 100. Show HN: Self-updating MCP server for official pip, uv, poetry and conda docs

**原文标题**: Show HN: Self-updating MCP server for official pip, uv, poetry and conda docs

**原文链接**: [https://github.com/KemingHe/python-dependency-manager-companion-mcp-server](https://github.com/KemingHe/python-dependency-manager-companion-mcp-server)

生成摘要时出错

---

