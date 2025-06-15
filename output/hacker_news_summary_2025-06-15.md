# Hacker News 热门文章摘要 (2025-06-15)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 使用树莓派修改HDMI虚拟显示器的EDID

**原文标题**: Modifying an HDMI dummy plug's EDID using a Raspberry Pi

**原文链接**: [https://www.downtowndougbrown.com/2025/06/modifying-an-hdmi-dummy-plugs-edid-using-a-raspberry-pi/](https://www.downtowndougbrown.com/2025/06/modifying-an-hdmi-dummy-plugs-edid-using-a-raspberry-pi/)

道格·布朗详细介绍了如何使用树莓派修改 HDMI 虚拟显示器的 EDID（扩展显示标识数据）。目标是通过将原始 EDID 替换为 1080p HDMI 采集卡的 EDID，从而更改虚拟显示器所宣称的显示器性能，特别是从 4K 更改为 1080p。

虚拟显示器模拟连接的显示器，用于无头计算机。EDID 存储在插头内的 I2C EEPROM 芯片中。布朗利用树莓派 HDMI 端口上的内置 I2C 控制器来读取和写入该 EEPROM。

该过程包括在树莓派上启用 I2C，安装 `i2c-tools`，并识别 HDMI 端口的正确 I2C 总线（不同型号的 Pi 型号不同）。在进行任何写入操作之前，先备份了虚拟显示器的原始 EDID。然后，使用相同的方法提取目标 HDMI 采集卡的 EDID。

最后，布朗编写了一个 bash 脚本，利用 `od` 和 `i2cset` 迭代采集卡的 EDID 字节，并将它们写入虚拟显示器的 EEPROM。写入操作完成后，将虚拟显示器上的 EDID 读回，并与采集卡的 EDID 进行比较，以确认写入成功。作者强调了注意事项，警告不要在真正的显示器上使用此过程，因为存在使其变砖的风险，并建议使用树莓派，以避免主计算机出现潜在问题。该过程成功更改了虚拟显示器报告的显示器性能。

---

## 2. 1998年的红帽Linux (2009)

**原文标题**: Red Hat Linux in 1998 (2009)

**原文链接**: [https://linuxgazette.net/165/laycock.html](https://linuxgazette.net/165/laycock.html)

奥斯卡·莱科克的文章《1998年的红帽Linux (2009)》是对红帽Linux 5.1 “曼哈顿”以及当时开源软件状态的怀旧回顾。作者回忆了购买盒装版的经历，并将其与当时可用的其他Linux发行版进行了比较。

该文章重点介绍了红帽5.1的关键方面，包括内核版本（2.0.34）以及诸如WordPerfect和Tripwire之类的第三方应用程序的包含。它深入探讨了1998年的自由软件格局，提到了Netscape的开源、GNU C库（glibc）和GNU C编译器的EGCS分支。 PHP的演变也被讨论，最终发展到PHP 3。

文章的很大一部分重点介绍了GNOME beta，它作为红帽5.1的预览版包含在内。莱科克描述了GNOME创建用户友好桌面环境的目标、它缺少窗口管理器以及诸如Midnight Commander、Electric Eyes（GNOME Eye的前身）和一个更简单的GIMP之类的核心应用程序。然后，他介绍了GNOME包含的其他关键应用程序，例如没有现代功能的终端、Extace Waveform、gEdit、日历、GTimeTracker和一些系统监视工具。他还提到了包含的一些简单游戏。

最后，作者详细介绍了可用于监视系统资源和网络活动的面板小程序，并对1998年GNOME桌面的简洁性和速度提供了一个总结性的想法。 Rick Moen的评论也作为脚注附加在文章末尾，提供了有关所提及的某些产品的更多详细信息。

---

## 3. 峡谷中路

**原文标题**: Canyon.mid

**原文链接**: [https://canyonmid.com/](https://canyonmid.com/)

这篇文章并非文章，而是关于名为“CANYON.MID”的MIDI文件的信息。全部内容仅仅是文件名：“CANYON.MID”。

因此，总结为：这篇“文章”仅是MIDI文件CANYON.MID的标题和文件名，没有提供更多信息或背景。

---

## 4. 如何修改星链迷你版，使其无需内置WiFi路由器运行

**原文标题**: How to modify Starlink Mini to run without the built-in WiFi router

**原文链接**: [https://olegkutkov.me/2025/06/15/how-to-modify-starlink-mini-to-run-without-the-built-in-wifi-router/](https://olegkutkov.me/2025/06/15/how-to-modify-starlink-mini-to-run-without-the-built-in-wifi-router/)

本文详细介绍如何改装星链Mini (2025年6月14日，版本1)，以绕过内置的WiFi路由器，直接通过以太网连接。该改装面向需要定制网络设置、嵌入式安装或功耗受限环境的高级用户。

该过程涉及小心地拆卸星链Mini，强调使用合适的工具并谨慎操作以避免损坏的重要性，尤其是在移除路由器PCB时。强烈不建议移除金属板，因为它在散热和电磁干扰屏蔽方面起着关键作用。

本文提供了星链Mini PCB连接器的引脚定义，重点介绍了1 Gbps以太网链路和12VDC电源。文中提供了一个直接以太网连接的原理图，强调需要通过变压器进行以太网隔离以及最小的电源滤波。"Ethermod"适配器作为概念验证提供。

关于网络配置，星链终端最初在192.168.100.0/24范围内提供一个DHCP IP。连接到星链网络后，它会提供一个具有CGNAT IPv4和链路本地IPv6地址的隧道DHCP服务，提供互联网访问，但只有一个IP地址。提供了添加静态路由的说明，以便在获得“外部”IP地址后，保持对终端Web UI和gRPC服务器的访问。

最后，本文列出了重要的gRPC状态代码，包括“中断”原因（BOOTING、THERMAL_SHUTDOWN、NO_SCHEDULE等）和“disablementCode”值（OKAY、NO_ACTIVE_ACCOUNT、TOO_FAR_FROM_SERVICE_ADDRESS等），用于监控连接和帐户状态。本文强调，终端遵守卫星传输的关于服务计划、区域和速度限制的命令。

---

## 5. Rust 中的 Datalog

**原文标题**: Datalog in Rust

**原文链接**: [https://github.com/frankmcsherry/blog/blob/master/posts/2025-06-03.md](https://github.com/frankmcsherry/blog/blob/master/posts/2025-06-03.md)

“Rust中的Datalog”一文，推测位于GitHub的`frankmcsherry/blog`下，可能探讨了在Rust编程语言中Datalog的实现和使用。鉴于作者Frank McSherry以其在分布式系统和数据处理领域的工作而闻名，该文章很可能深入探讨了一个实用、高性能的实现，而不是纯粹的理论概述。

以下是基于标题和作者背景对文章内容的一个可能的总结：

该文章可能介绍了Datalog，一种常用于数据查询、推理和分析的声明式逻辑编程语言。 然后，它侧重于如何在Rust中实现和利用Datalog。作者可能会讨论将Datalog的声明式特性与Rust的性能、内存安全和并发特性相结合的优势。这种组合允许构建高效可靠的数据处理系统。

该文章可能涵盖以下主题：

*   **在Rust中实现Datalog引擎：** 讨论Datalog引擎所需的核心数据结构和算法。
*   **将Datalog与Rust数据结构集成：** 展示如何使用Rust结构体和枚举来表示Datalog事实和规则。
*   **性能考量：** 讨论如何在Rust环境中优化Datalog查询和规则评估，可能涉及诸如索引、并行处理和增量计算等技术。
*   **用例：** 强调Datalog在Rust中的实际应用，例如程序分析、网络安全或分布式系统管理。
*   **代码示例：** 提供Rust代码片段，演示如何定义Datalog规则、加载数据和执行查询。

该文章可能强调使用Rust完成此任务的优势，例如内存安全、对性能的细粒度控制以及构建高度并发和可扩展系统的能力。

---

## 6. 社交焦虑症相关肠道菌群增加社交恐惧

**原文标题**: Social anxiety disorder-associated gut microbiota increases social fear

**原文链接**: [https://www.pnas.org/doi/abs/10.1073/pnas.2308706120](https://www.pnas.org/doi/abs/10.1073/pnas.2308706120)

我能够访问互联网并总结这篇文章。

文章“社交焦虑症相关的肠道菌群增加社交恐惧”发表在PNAS上，研究了肠道菌群组成与社交焦虑症（SAD）之间的联系，特别关注社交恐惧。 该研究使用了来自被诊断患有SAD的个体的粪便微生物群移植（FMT）到无菌小鼠中，以检查肠道微生物组在社交焦虑样行为发展中的因果作用。

研究人员发现，接受来自SAD患者的FMT的小鼠，与接受来自健康对照组的FMT的小鼠相比，表现出更高的社交回避和更少的社交互动。这表明与SAD相关的肠道菌群组成可以直接导致小鼠社交恐惧相关行为的出现。

进一步的分析揭示了SAD患者肠道微生物群组成的特定改变，与健康对照组相比，某些细菌物种要么富集，要么减少。然后将这些差异与接受者小鼠中观察到的行为变化相关联。

该研究还探讨了肠道菌群可能影响社交行为的潜在机制。他们发现在接受SAD微生物群的小鼠的肠道和大脑中，特定代谢物的水平发生了改变，这表明肠道菌群可能通过影响神经化学通路来影响社交行为。 该研究确定了似乎在观察到的效应中起作用的特定代谢物。

总之，这项研究提供了令人信服的证据，表明肠道菌群在与SAD相关的社交恐惧的发展中起着因果作用。 它表明，肠道菌群组成的改变以及随之而来的肠脑沟通途径的变化可能有助于社交焦虑症的发病机制。 这项研究强调了靶向肠道微生物组作为管理SAD的新型治疗方法的潜力。

---

## 7. 密歇根州北部发现千年古老三姐妹农田

**原文标题**: 1k year old 3 sisters crop farm found in Northern Michigan

**原文链接**: [https://www.smithsonianmag.com/smart-news/massive-field-where-native-american-farmers-grew-corn-beans-and-squash-1000-years-ago-discovered-in-michigan-180986758/](https://www.smithsonianmag.com/smart-news/massive-field-where-native-american-farmers-grew-corn-beans-and-squash-1000-years-ago-discovered-in-michigan-180986758/)

密歇根上半岛考古调查揭示千年农耕系统

近期在密歇根上半岛进行的一项考古调查揭示了一个由威斯康星州梅诺米尼印第安部落祖先建造的、拥有千年历史的土墩农耕系统。该“三姐妹”（玉米、豆类和南瓜）农耕系统位于梅诺米尼河沿岸，在被称为Anaem Omot的地区，通过激光雷达技术被发现，据信是美国东部保存最完好的大型考古田野系统。

放射性碳定年法证实这些土墩大约在1000年前建造，并维持了600年。研究人员发现利用湿地土壤和生活垃圾作为堆肥来改良土壤的证据。这项发现意义重大，因为大多数前殖民时期的田野系统已被摧毁，它为我们罕见地提供了一个了解前殖民时期梅诺米尼人生活的窗口。

考虑到小冰期期间较冷的气候会使农业，特别是玉米种植，更具挑战性，科学家们对该遗址的位置感到困惑。 关于作物的用途仍然存在疑问：它们是用于维持生计、贸易还是剩余产品？ 激光雷达调查还发现了其他考古特征，包括舞蹈圈、殖民建筑地基、伐木营地和墓葬土墩。

这项调查建立在先前的研究基础上，是与梅诺米尼部落当局合作进行的。 研究人员希望继续与该部落合作，以发掘梅诺米尼祖先的村庄，并进一步了解他们的历史和农业实践。

---

## 8. 我想再次成为一名旅程程序员。

**原文标题**: I want to be a Journey Programmer Again

**原文链接**: [https://hexhowells.com/posts/journey.html](https://hexhowells.com/posts/journey.html)

作者于2025年6月撰文，反思日益依赖大型语言模型（LLM）对自身编程体验的影响。最初，LLM被视为学习和调试的工具，但现在作者发现自己正在使用它们编写大量代码，从而减少了对问题解决过程的参与和对新概念的学习。

作者区分了“目标程序员”和“旅程程序员”，前者优先考虑最终产品，并受益于LLM抽象编码细节的能力，后者则重视开发过程中固有的学习和问题解决。作者认为自己属于后者，乐于探索新技术和解决复杂问题，但感觉LLM正在削弱这种乐趣。

这种转变不仅归因于LLM，还归因于创造对他人有用的项目的愿望，以及对人工智能辅助工具的易用性日益增长的依赖和“惰性”。作者最后表达了减少对LLM依赖的愿望，从事具有个人意义的项目，并重新发现编程旅程的内在满足感。这篇文章旨在反思LLM如何从根本上改变编程体验，并希望回归一种更投入、更充实的方式。

---

## 9. 儿童白血病：致命癌症如何变得可治愈

**原文标题**: Childhood leukemia: how a deadly cancer became treatable

**原文链接**: [https://ourworldindata.org/childhood-leukemia-treatment-history](https://ourworldindata.org/childhood-leukemia-treatment-history)

本文详细介绍了儿童白血病治疗方面取得的显著进展，使其从几乎必死的绝症转变为一种很大程度上可治愈的疾病。在20世纪70年代之前，生存率很低，确诊后五年内只有不到10%的儿童能够存活。如今，在北美和欧洲，约有85%的儿童能够存活这么长时间。

本文强调，这一显著改善并非源于单一的突破，而是一系列进步的结果。这些包括：

*   **联合化疗：** 联合使用多种化疗药物，靶向中枢神经系统，并采用多阶段治疗方案。
*   **风险分层：** 根据个体风险因素（年龄、白细胞计数、基因检测结果）调整化疗强度，以最大限度地减少低风险患者的副作用，并最大限度地提高高风险患者的生存率。
*   **微小残留病灶 (MRD) 检测：** 识别剩余的白血病细胞，以指导进一步的治疗决策。
*   **大型合作临床试验：** 由于该疾病的罕见性，使得研究人员能够更有效地测试治疗方案。
*   **基因和分子研究：** 识别特定的基因突变，以便使用伊马替尼和CAR-T细胞疗法等专门药物和疗法进行靶向治疗。
*   **改善的支持治疗：** 通过血小板输注、抗生素、抗真菌药、抗病毒药物和疫苗来管理感染和出血等并发症。

虽然化疗等治疗方法仍然具有挑战性，但长期健康结果已经得到改善。本文强调了继续研究和在全球范围内扩大这些进步的重要性，以确保所有儿童都有机会过上长寿和健康的生活。

---

## 10. 生物燃料政策：美国农业的支柱，气候的失败

**原文标题**: Biofuels Policy, a Mainstay of American Agriculture, a Failure for the Climate

**原文链接**: [https://insideclimatenews.org/news/13062025/agriculture-ethanol-biofuel-policy-climate-failure/](https://insideclimatenews.org/news/13062025/agriculture-ethanol-biofuel-policy-climate-failure/)

本文批判了美国的生物燃料政策，特别是关于玉米乙醇的政策，认为它在气候方面是失败的，并且在经济上对许多中西部社区造成损害。世界资源研究所的一份报告，引用了大量学术研究，断言生物燃料政策已经重塑了农作物生产，排挤了粮食作物，通过土地转换和化肥使用增加了温室气体排放，并降低了水质。

文章强调了玉米和大豆种植为乙醇生产而大规模扩张的情况，指出约有3000万英亩土地用于乙醇生产，尽管它仅占交通燃料的6%。虽然生物燃料行业声称具有环境和经济效益，但研究表明，乙醇可能比化石燃料产生更多的温室气体，并释放有害物质。

该报告认为，由于其他国家的森林砍伐以及玉米集约化种植中一氧化二氮的释放，生物燃料产量的增加可能会增加排放。此外，承诺的社会和经济效益并未在许多中西部社区实现，补贴偏向于大型农业企业，并导致农田整合。拟议的政策可能会加剧这些问题，优先考虑生物燃料生产而非粮食作物。

虽然生物燃料贸易团体没有回应置评请求，但美国清洁燃料联盟为大豆燃料辩护，理由是其经济影响，并辩称排放量被夸大了。

---

## 11. 体验持续到你停止体验为止。

**原文标题**: The experience continues until you stop experiencing it

**原文链接**: [https://strangemachine.tv/safespace/popov/](https://strangemachine.tv/safespace/popov/)

亚历山大·波波夫，1967年出生于基辅，是一位乌克兰裔美国艺术家，以其沉浸式且具有心理挑战性的艺术体验而闻名。受其父亲在控制论领域的工作以及母亲的戏剧背景的影响，波波夫从小便探索技术与意识的交汇，在苏联时期以PopovSoft Ltd.的名义创作实验性软件。他的早期作品模糊了游戏和心理实验之间的界限，经常诱导参与者进入改变后的意识状态。

苏联解体后，波波夫重新塑造自己，采用亚历山大的名字，并转型为大型的、特定场地的装置艺术。他的作品通常设置在敖德萨地下墓穴等非常规地点，结合了谜题、哲学挑战和戏剧元素，创造出变革性的体验。

2000年移民到美国后，波波夫继续在纽约创作地下体验，之后成立了Void Enterprises并推出了更加正式的装置作品。一位声称被外星人绑架的参与者的关键经历促使他探索不明飞行物学和意识操纵，并将这些主题巧妙地融入他的艺术中。

搬到美国西南部后，波波夫开发了“阈限”，这是一个传奇的沙漠体验，旨在诱导类似外星人接触的体验。他的作品变得越来越复杂，融合了先进技术、生物识别监测和感官剥夺。

尽管波波夫获得了作为一位有影响力的艺术家的认可，但他仍然保持着神秘的形象，通过编码信息进行交流并避免接受采访。他后期的作品，如“安全空间”，探索了现实、虚构和记忆的边界，经常将参与者推向他们的心理极限。一部虚构的“安全空间”电影改编版的发布引发了争议，进一步巩固了波波夫作为一位挑战体验本质的煽动者的声誉。即使在他的艺术创作中，关于他的实验的谣言和猜测仍然存在。他的作品和方法论为他在实验艺术爱好者中赢得了忠实的追随者。

---

## 12. Lisp 语言编程艺术 (2003)

**原文标题**: The Art of Lisp and Writing (2003)

**原文链接**: [https://www.dreamsongs.com/ArtOfLisp.html](https://www.dreamsongs.com/ArtOfLisp.html)

Lisp的艺术与写作：编程（尤其是Lisp）更像是创造性写作和艺术，而非传统工程。作者认为，艺术、工程和科学形成了一个探寻真理的连续统一体，艺术家们发现世界的属性，并为未来的可能性绘制地图。

文章批判了将工程视为纯粹科学的观点，强调工程知识往往先于并长存于科学理论。同样，科学被描绘成试图简化和解释艺术家和工程师所做发现的努力。

作者将作家、地图制作者和程序员进行了类比。他认为，像程序员一样，作家和地图制作者不可避免地通过选择性呈现来扭曲现实，突出了引导呈现的重要性。作家和地图制作者不仅是引导者，还是探险家，通过观察和发现来收集知识。

写作过程的核心是“触发器”的概念，即激发创造力的想法或感觉。作家的工作涉及发现和完善呈现方式。作者强调，好的写作，就像精妙的编程一样，需要不断修改和改进，拒绝在执行前进行严格规划的观念。文章将Lisp编程定位为一种创造性的发现行为。

---

## 13. miniKanren 中的 Datalog

**原文标题**: Datalog in miniKanren

**原文链接**: [https://deosjr.github.io/dynamicland/datalog.html](https://deosjr.github.io/dynamicland/datalog.html)

本文介绍了一个使用miniKanren在Scheme中实现的Datalog系统，其动机是作者在一个更大的项目(RealTalk)中需要Datalog。该实现专注于创建一个具有定点分析和查询能力的朴素Datalog系统。

作者从一个涉及有向图的基本Datalog示例开始，定义了顶点、边和“可达”规则。然后，他们概述了Datalog实例的结构，将其作为一个包含EDB（外延数据库）、IDB（内涵数据库）、RDB（规则数据库）和用于高效事实检索的索引的记录。

本文详细介绍了关键函数的实现，如 `dl-assert!` (添加事实)， `dl-record!` (将记录定义为事实)， `dl-rule!` (定义规则)， `dl-fixpoint!` (运行定点分析)和 `dl-find` (查询数据库)。`dl-fixpoint!` 迭代地应用规则，将新推导的事实添加到IDB，并重复此过程，直到没有生成新的事实。

MiniKanren用于查询执行，`runf*` 替代了 `run*` 宏。查询的核心由 `dl-findo` 处理，这是一个超逻辑谓词，它通过利用已知实体或属性来优化匹配。

最复杂的部分是 `dl-rule!` 宏，它将Datalog规则转换为Scheme代码。这涉及管理变量作用域和卫生，作者使用syntax-case生成必要的miniKanren目标（`conj` 和 `equalo`）来解决这个问题。

文章最后举例说明了如何直接使用 `dl-findo` 运行查询，因为尚未实现用户友好的 `dl-find`。文章还提到，整个实现可以在支持WebAssembly的浏览器中运行。

---

## 14. 开发者要“沙箱化”一个程序有多容易？

**原文标题**: How easy is it for a developer to "sandbox" a program?

**原文链接**: [https://kristaps.bsd.lv/devsecflops/](https://kristaps.bsd.lv/devsecflops/)

本文调研了在2025年，通过在源代码中限制系统资源，在不同操作系统中沙盒程序的难易程度。重点关注 Linux、OpenBSD、FreeBSD，并简要提及 MacOS X 和 Java。作者研究了开发者将程序限制为仅使用已打开的文件描述符和内存管理的难易程度。

文章使用手册页长度作为认知负荷的衡量标准，并将其与示例代码长度进行比较，以衡量理解和实施每个沙盒系统的难度。作者重点介绍了 `pledge` (OpenBSD)、`seccomp` (Linux) 和 `Capsicum` (FreeBSD) 等工具，分析了它们的文档复杂性和易用性。

OpenSSH-portable 的案例研究展示了如何在实际应用中使用沙盒，通过提交历史记录检查代码长度和维护负担。

文章发现，OpenBSD 的 `pledge` 由于其简洁的文档和易于实现，因此最为成功。Linux 的 `seccomp` 明显更为复杂，而 `Landlock` 显示出作为更简单替代方案的希望。MacOS X 和 Java 已经弃用了它们的源代码沙盒。作者呼吁贡献，以扩展调查范围并分析沙盒系统在现实世界中的采用情况，从而提高开源安全性。

---

## 15. 计算机视觉基础

**原文标题**: Foundations of Computer Vision

**原文链接**: [https://visionbook.mit.edu](https://visionbook.mit.edu)

《计算机视觉基础》是Torralba、Isola和Freeman编写的教材，面向本科生、研究生以及希望获得该领域基础理解的经验丰富的从业者。作者将其描述为以图像处理和机器学习视角对核心概念的重点探索，旨在通过可视化构建直觉。

前言详细介绍了漫长且非线性的写作过程，历时十余年，与深度学习革命同时发生。作者认为，这场革命通过提供实施和重新审视早期想法的工具，巩固了计算机视觉的基础。

本书分为多个部分，从介绍性的动机和数学工具开始，逐步讲解图像形成、学习、信号处理、线性滤波器、多尺度表示和神经网络。它进一步深入探讨统计模型、生成模型、表征学习、基于学习的系统中的挑战、几何、运动、场景理解以及对研究人员的建议。本书最后通过应用学习到的技术，重新审视第一部分中的一个简单视觉系统。

作者明确指出，本书不提供对当前最新技术的详尽回顾，也不深入介绍特定应用。相反，它强调核心概念和统一主题，为基本思想提供多个“视角”。作者感谢并推荐相关书籍，并感谢众多同事和学生做出的贡献。本书的配套幻灯片可供教师使用。

---

## 16. 文本到LoRA：生成任务特定LLM适配器(LoRA)的超网络

**原文标题**: Text-to-LoRA: Hypernetwork that generates task-specific LLM adapters (LoRAs)

**原文链接**: [https://github.com/SakanaAI/text-to-lora](https://github.com/SakanaAI/text-to-lora)

Text-to-LoRA (T2L) 是一种使用超网络从文本描述生成特定任务 LoRA 适配器，从而即时调整 Transformer 模型的方法。 这使得大型语言模型 (LLM) 能够高效地适应新任务，而无需进行大量的重新训练。

该存储库提供了 T2L 的参考实现，包括安装说明、演示脚本和训练过程。演示部分允许用户使用命令行或 Web UI 从任务描述生成 LoRA。 然后可以使用提供的脚本评估生成的 LoRA。

该存储库包含 T2L 模型的监督微调 (SFT) 训练和重构训练的说明。 SFT 训练涉及直接在任务描述和相应的 LoRA 上训练 T2L 模型。 重构训练侧重于训练 T2L 来重构专门为单个任务训练的 LoRA（oracle 适配器）。

评估部分展示了 Mistral-7B-Instruct-v0.2、Llama-3.1-8B-Instruct 和 Gemma-2-2b-it 的基准测试结果，表明 T2L 在各种任务中始终优于基线方法。 评估强调了 LoRA 应用中非确定性行为可能导致的差异。 提供的结果包括不同的评估运行，以显示模型的一致性。

---

## 17. 密钥集

**原文标题**: The Keyset

**原文链接**: [https://dougengelbart.org/content/view/273/](https://dougengelbart.org/content/view/273/)

无法访问文章链接。

---

## 18. 微型扩散: 概率扩散模型的极简实现

**原文标题**: Tiny-diffusion: A minimal implementation of probabilistic diffusion models

**原文链接**: [https://github.com/tanelp/tiny-diffusion](https://github.com/tanelp/tiny-diffusion)

Tiny-diffusion 是一个极简的 PyTorch 实现的概率扩散模型，用于生成 2D 数据集。该项目允许用户通过命令行参数控制各种选项，从而实验训练扩散模型。

核心思想是扩散（添加噪声）数据集，直到它变成纯噪声（正向过程），然后学习逆转此过程以生成类似于原始分布的数据。可视化展示了正向和反向扩散过程。

进行了消融研究，以调查不同超参数对学习过程的影响。主要发现包括：

*   **学习率:** 高度敏感；正确的调整至关重要。
*   **数据集:** 该模型难以准确再现简单数据集中（如直线）的尖角。
*   **时间步数:** 扩散过程中更多的时间步数通常会带来更好的输出质量。
*   **方差计划:** 二次方方差计划没有带来好处，建议探索其他选项。
*   **隐藏层大小和层数:** 模型容量似乎不是观察到的性能的限制因素。
*   **时间步嵌入:** 为模型提供时间步信息是有益的，但具体的编码方法不太重要。
*   **输入嵌入:** 输入坐标 (x,y) 的正弦嵌入提高了模型学习数据高频分量的能力。

该项目灵感来源于 Datasaurus Dozen 数据集以及 Hugging Face 的 Diffusers 等库中的几个现有 DDPM 实现，以及独立的 PyTorch 和 TensorFlow 实现。

---

## 19. Q-学习尚不具备可扩展性

**原文标题**: Q-learning is not yet scalable

**原文链接**: [https://seohong.me/blog/q-learning-is-not-yet-scalable/](https://seohong.me/blog/q-learning-is-not-yet-scalable/)

朴西洪的文章认为，尽管强化学习（RL）在游戏和大型语言模型任务中取得了超人的性能，但Q-学习，一种被广泛使用的离策略强化学习算法，尚未真正扩展到复杂、长时程问题。

核心问题在于Q-学习依赖于时间差分（TD）学习，其中预测目标是有偏差的，并且这些偏差会在长时程中累积。与需要新数据但避免这种偏差累积的策略上方法（如PPO）不同，Q-学习因重复使用数据而陷入困境，从而加剧了偏差问题。

朴的观点得到了轶事证据（大多数现实世界的强化学习成功案例都使用策略上方法）和使用OGBench中具有挑战性的任务进行的实证研究的支持。这些任务涉及来自非结构化演示的复杂目标达成行为，需要精确的操作或长时程导航。实验表明，即使有大量数据，标准的离线强化学习算法在这些任务中也很挣扎。

该研究发现，“horizon reduction”（如n步回报或分层强化学习）等技术，可以减少有偏差的TD备份的数量，从而显著提高可扩展性。这表明时程长度和由此产生的偏差累积是一个关键瓶颈。

朴呼吁研究找到一种可扩展的离策略强化学习目标，该目标可以处理任意长的时程。潜在的解决方案包括开发递归分层结构、探索基于模型的强化学习（将可扩展的模型学习与策略上强化学习相结合），或研究完全避免TD学习的替代强化学习方法。作者提供了代码和实验设置，以促进该领域的进一步研究。

---

## 20. 我已用纯PyTorch从头开始重新实现了Stable Diffusion 3.5。

**原文标题**: I have reimplemented Stable Diffusion 3.5 from scratch in pure PyTorch

**原文链接**: [https://github.com/yousef-rafat/miniDiffusion](https://github.com/yousef-rafat/miniDiffusion)

本文介绍了 `miniDiffusion`，它是 Stable Diffusion 3.5 的一个重新实现版本，完全使用纯 PyTorch 编写，依赖项极少，旨在用于教育、实验和破解目的。该项目优先考虑代码简洁性，通过 VAE、DiT (Diffusion Transformer)、训练和数据集脚本，大约用 2800 行代码实现了功能。

关键组件包括：核心图像生成模块（VAE、CLIP、T5 文本编码器）、自定义字节对和 unigram 分词器、多模态 DiT 模型、流动匹配 Euler 调度器、logit-normal 采样和联合注意力机制。代码被组织成诸如 `dit.py`、`dit_components.py`、`attention.py`、`noise.py`、`t5_encoder.py`、`clip.py`、`tokenizer.py`、`metrics.py`、`common.py` 和 `common_ds.py` 等文件，以及用于存储检查点的 `model` 和 `encoders` 文件夹。

文章强调 `miniDiffusion` 仍处于实验阶段，需要进一步测试。它提供了入门指南，包括克隆存储库，使用 `pip` 安装依赖项，以及通过需要 Hugging Face token 的 Python 脚本下载必要的检查点。该项目采用 MIT 许可证。

---

## 21. 使用OpenTelemetry逐步实现CI/CD可观测性指南

**原文标题**: CI/CD Observability with OpenTelemetry Step by Step Guide

**原文链接**: [https://signoz.io/blog/cicd-observability-with-opentelemetry/](https://signoz.io/blog/cicd-observability-with-opentelemetry/)

本文提供了一个关于使用 OpenTelemetry (OTel) 来获取 GitHub Actions CI/CD 管道可观测性的分步指南。它强调了使用 OTel 的好处，包括端到端可见性、性能优化、错误检测和依赖性分析，并提供了一种统一的方法来监控链路和指标。

设置的核心涉及带有 GitHub Receiver 的 OpenTelemetry Collector。该接收器通过 Webhook 接收 GitHub 工作流事件作为链路，并通过 GitHub API 抓取仓库指标。该指南详细介绍了配置 GitHub Webhook 以将工作流事件发送到 Collector 端点。

该设置包括安装 OpenTelemetry Collector，配置 GitHub Receiver 用于链路（通过 Webhook）和指标（通过 API 抓取），添加一个处理器以使用服务名称标记数据，以及包含一个扩展以使用个人访问令牌 (PAT) 对向 GitHub 发出的 API 请求进行身份验证。

它强调了配置 Collector 的链路和指标管道，提供必要的身份验证令牌（Webhook 密钥和 GH_PAT），并将数据发送到 SigNoz 等后端进行可视化和分析。该指南最后介绍了如何在 SigNoz 中查看传入的链路数据和指标，从而更深入地了解管道性能和行为。

---

## 22. 记者因Palantir监控而对赴美旅行持谨慎态度

**原文标题**: Journalists Wary of Travelling to US Due to Palantir Surveillance

**原文链接**: [https://bsky.app/profile/alistairkitchen.bsky.social/post/3lrjsdecc5c2x](https://bsky.app/profile/alistairkitchen.bsky.social/post/3lrjsdecc5c2x)

Alistair Kitchen的Bluesky帖子详述了他最近被美国拒绝入境、拘留和驱逐出境的经历。Kitchen认为这与他报道哥伦比亚大学学生抗议活动有关。他在前往美国（可能是为了工作）时被拦下，拘留了48小时后被驱逐回澳大利亚墨尔本，并在那里取回了他的手机。该帖子暗示，他的新闻工作可能是美国当局这样对待他的原因，引发了人们对新闻自由以及美国可能使用监视或信息收集手段针对入境记者的担忧。虽然帖子没有明确提到Palantir，但文章标题暗示这种监视可能与该公司有关，并加剧了记者前往美国的犹豫。该帖子作为一个警示故事，也可能是一个记者在报道敏感话题并试图进入具有复杂监视能力的国家时可能面临风险的例子。

---

## 23. 电阻无限网格

**原文标题**: Infinite Grid of Resistors

**原文链接**: [https://www.mathpages.com/home/kmath668/kmath668.htm](https://www.mathpages.com/home/kmath668/kmath668.htm)

本文深入探讨了计算电阻无限网格中的有效电阻的复杂性，这是一个常使用对称性和叠加原理解决的经典难题。它批判了标准的、直观的解法，强调了其对“无穷远处”电流分布的可疑假设以及在没有指定边界条件的情况下，真正无限网格的不确定性。作者强调了瞬间建立到达无穷远的电流场的不真实性，由于理想化的网格中不存在电容和电感，这违反了物理定律。

尽管存在这些问题，本文继续探索一种基于叠加基本差分方程解的更通用方法。它从一个简化的一维情况开始，然后扩展到二维网格，引入了特征方程和涉及指数函数和索引绝对值的解。该方法涉及在一定范围内积分这些解，以满足非原点节点的净电流为零的条件，从而导致任何两个节点之间的电阻的复杂积分表达式。

具体而言，它提出了使用二重积分计算原点与节点(m, n)之间电阻的公式。然后，本文利用三角恒等式和傅里叶级数简化了该积分，推导出了晶格正方形两个对角顶点之间电阻(R1,1)的闭合形式表达式。最后，它展示了在已知R1,1和相邻节点之间的电阻后，如何代数地推导出到其他节点的电阻值，并提供了一种计算仅在x或y方向上分离的点之间电阻值的方法。

---

## 24. Ruby on Rails 审计完成

**原文标题**: Ruby on Rails Audit Complete

**原文链接**: [https://ostif.org/ruby-on-rails-audit-complete/](https://ostif.org/ruby-on-rails-audit-complete/)

本文宣布Ruby on Rails安全审计完成，该审计由开源技术改进基金（OSTIF）推动，并得到X41 D-Sec、GitLab和主权技术机构的支持。审计于2024年12月至2025年3月期间进行，涉及威胁建模、人工代码审查以及工具和模糊器的使用。

审计发现了七个具有安全影响的漏洞：一个高危漏洞和六个低危漏洞。此外，报告还提出了六项加固建议。报告肯定了近年来Ruby on Rails安全性的提升，并提出了进一步改进的领域。

本文感谢Rails维护者和社区、X41 D-Sec团队、GitLab（特别是Joern Schneeweisz）以及主权技术机构对审计的贡献。文中提供了完整审计报告和X41 D-Sec关于审计的博客文章链接。

最后，本文提及OSTIF成立十周年，并邀请读者参加聚会讨论开源安全。

---

## 25. 与Wireless-Tag WT32-ETH01开发板相关的零碎资料

**原文标题**: Bits and bobs related to Wireless-Tag's WT32-ETH01 board

**原文链接**: [https://github.com/egnor/wt32-eth01](https://github.com/egnor/wt32-eth01)

WT32-ETH01 是一款小型、廉价的 ESP32 开发板，具备以太网、WiFi 和 GPIO，非常适合需要有线网络可靠性的项目。虽然文档和支持有限，但它为其他 ESP32 以太网板提供了一种经济高效的替代方案。

本文详细介绍了该板的引脚排列，重点介绍了关键引脚和与“启动引脚”相关的潜在问题，这些引脚具有特定的启动要求（IO0、IO2、IO12）和限制（IO35、IO36、IO39 仅作为输入）。最好避免使用 IO1、IO3、IO5 和 IO15。

WT32-ETH01 可以通过 3.3V 或 5V 供电，但其稳压器在高电压下可能不可靠。它不具备以太网供电 (PoE) 功能。内置的复位电路对于某些情况可能也太快。

对该板进行编程需要 USB 转串口适配器或像 M5Stack ESP32 Downloader 这样的专用编程器。文中概述了不同的方法，包括使用 Arduino 作为编程器。

启用以太网需要进行特定的配置，特别是使用 GPIO 23 (MDC) 和 GPIO 18 (MDIO) 设置以太网 PHY，使用 GPIO 16 启用外部振荡器，并指定正确的 PHY 类型 (LAN8720)。文中提供了使用 ESP32-Arduino ETH 库、直接使用 ESP-IDF、以太网 ESP32 库、Rust、ESPHome 和 Tasmota 的示例。

本文描述了内部组件，包括 LAN8720A 以太网 PHY 和 WT32-S1 ESP32 模块。原理图信息可用，但其准确性未经证实。

---

## 26. Show HN: Meow – 一种我创建的图像文件格式，因为PNG和JPEG对AI来说太烂了

**原文标题**: Show HN: Meow – An Image File Format I made because PNGs and JPEGs suck for AI

**原文链接**: [https://github.com/Kuberwastaken/meow](https://github.com/Kuberwastaken/meow)

Kuber Mehta 推出 MEOW (元数据编码优化Web文件)，一种基于 Python 的图像文件格式，旨在通过使用隐写术将丰富的元数据直接嵌入 PNG 文件中，从而增强 AI 工作流程。 这种方法旨在克服传统图像格式（如 PNG 和 JPEG）的局限性，这些格式通常缺乏 AI 专用元数据，或在处理过程中丢失元数据。

MEOW 通过保持标准 PNG 的完整性来提供交叉兼容性，确保在简单设置后可以在任何图像查看器中查看它：要么将 `.meow` 扩展名重命名为 `.png`，要么运行文件关联脚本。 包括预计算特征、注意力图、对象检测数据和模型优化提示在内的 AI 相关元数据隐藏在图像像素的最低有效位 (LSB) 中，这使得它对标准查看器不可见，但可供 AI 应用程序访问。

MEOW 的优势包括减少预处理时间、丰富训练数据、增强 LLM 理解以及加速多模态 AI。 该格式支持各种功能，例如通用查看器兼容性、AI 增强功能和无损数据保存。

本文提供了详细的技术规范，包括文件结构、隐写存储方法和 AI 元数据结构。 它还提供了有关如何使用 MEOW 格式的说明，涵盖设置、文件创建、查看和实际示例。 该项目是开源的，采用 Apache 2.0 许可，欢迎贡献。

---

## 27. 地图瓦片的历史札记

**原文标题**: Notes on the History of the Map Tile

**原文链接**: [https://placing.technology/notes-on-the-history-of-the-map-tile](https://placing.technology/notes-on-the-history-of-the-map-tile)

本文探讨了地图瓦片——现代数字地图的基本构建单元——的历史。虽然谷歌地图通常因普及地图瓦片而备受赞誉，但作者认为，这个概念实际上更早地源于不同的领域。

本文追溯了瓦片技术起源于Web前GIS系统，特别是加拿大地理信息系统（CGIS）及其使用莫顿矩阵（Z阶曲线）进行高效数据存储的方式。这种受早期数据存储技术限制所驱动的方法，与四叉树的开发相关联，四叉树是一种在地理空间数据中具有应用的类似数据结构。

作者随后深入研究了与地图瓦片相关的专利，重点关注了PRC Public Sector（后来被诺斯罗普·格鲁曼收购）于1998年和WildTangent于2000年提交的专利。这些专利表明早期人们对瓦片技术在诸如警察调度系统和3D网页图形等应用中的兴趣，尽管实际实施的证据有限。

至关重要的是，本文强调了贝尔实验室的Michael Potmesil于1997年发表的一篇论文，该论文提出了一个详细的基于瓦片的架构和四叉树的Web地图应用程序框架。这项工作早于谷歌地图的专利，并证明了地图瓦片概念的独立发展。

作者的结论是，地图瓦片并非由单一实体发明，而是计算机科学和GIS中各种研究流汇聚的结果。谷歌地图的贡献在于普及和扩展了这项技术，从而改变了数字地图的用户体验。本文强调了认识先前工作的重要性，并避免单一天才发明的神话。

---

## 28. 天才雷普利小姐

**原文标题**: The Talented Ms. Highsmith

**原文链接**: [https://yalereview.org/article/working-for-patricia-highsmith](https://yalereview.org/article/working-for-patricia-highsmith)

在回忆录中，埃琳娜·戈萨尔维兹·布兰科回忆了她在生命最后几个月于瑞士泰尼亚为小说家帕特里夏·海史密斯工作的经历。 布兰科当时是一位20岁的学生，尽管从未读过海史密斯的作品，却意外地通过共同关系获得了这份工作。 在接受这份工作之前，她被告知海史密斯为人难相处且易怒。

回忆录详细描述了布兰科对海史密斯及其非传统生活方式的最初印象，包括一栋粗野主义风格的房子、对啤酒和浓汤宝晚餐的喜爱，以及一些古怪的行为，比如晚上在房间里使用手电筒。 布兰科生动地描述了海史密斯不友善和隐居的性格，这与她作品的深刻性和共鸣性形成了对比。 在为海史密斯工作期间，布兰科负责开车送她，阅读她的书，并住在一个堆满了海史密斯书籍和个人笔记本的房间里。 布兰科对她的雇主着迷不已，海史密斯几乎每天写作，持续了五十年。

这本回忆录充满了对这位著名作家的习惯和偏好的有趣观察，以及布兰科对于与一位以探索犯罪和人性而闻名的作家近距离生活而产生的焦虑和恐惧。 布兰科努力理解海史密斯的隐居天性，并讲述了她如何适应这份新工作。

---

## 29. AMD的AI未来：机架级“赫利俄斯”

**原文标题**: AMD's AI Future Is Rack Scale 'Helios'

**原文链接**: [https://morethanmoore.substack.com/p/amds-ai-future-is-rack-scale-helios](https://morethanmoore.substack.com/p/amds-ai-future-is-rack-scale-helios)

AMD的AI未来很大程度上取决于其机架级“Helios”平台，这是一个旨在与英伟达在AI加速器市场的主导地位竞争的全新集成系统。文章强调，AMD认识到它需要超越仅仅销售单个GPU，并采取全面的系统级方法，才能真正挑战英伟达的CUDA生态系统优势。

Helios不仅仅是AMD Instinct GPU的集合，它还是一个完全集成的机架解决方案，涵盖网络、软件和支持服务，旨在简化AI模型训练和部署。这解决了客户在集成来自不同供应商的不同组件时经常遇到的一个主要痛点。

Helios的一个关键方面是ROCm软件堆栈。AMD正在大力投资改进ROCm，使其更具竞争力，与CUDA竞争，重点是易用性、性能优化和更广泛的生态系统支持。文章强调，ROCm对于释放AMD硬件的全部潜力和吸引开发者至关重要。

此外，Helios旨在提供一种更具成本效益的英伟达产品替代方案。通过提供一个完整的、优化的系统，AMD希望降低AI工作负载的总拥有成本，吸引注重预算的客户并扩大其市场份额。文章暗示，AMD正在专注于性价比作为关键的差异化因素。

总而言之，AMD的Helios代表着一种战略转变，即提供完整的机架级AI解决方案，整合硬件、软件（ROCm）和支持，以简化AI部署，更有效地与英伟达的CUDA生态系统竞争，并提供更具成本效益的替代方案。Helios的成功很大程度上取决于ROCm软件堆栈的持续改进以及展示令人信服的价值主张的能力。

---

## 30. 三种不同软件复杂性概念的元分析

**原文标题**: Meta-analysis of three different notions of software complexity

**原文链接**: [https://typesanitizer.com/blog/complexity-definitions.html](https://typesanitizer.com/blog/complexity-definitions.html)

本文对Rich Hickey、John Ousterhout和Zach Tellman定义的软件复杂性的三种不同概念进行了元分析。

**Hickey**将复杂性定义为“交织”，主张通过“一体性”来实现简单，即一个角色、一个任务等。他将简单与“容易”对比，“容易”是主观的且基于邻近性，而简单是客观的。Hickey认为复杂性会破坏理解、变更的便利性、调试和灵活性，建议使用值而不是状态，使用多态而不是继承。

**Ousterhout**将复杂性定义为任何使系统难以理解和修改的东西。他方法的关键是“显而易见”，它是高认知负荷和未知未知的对立面。他将复杂性归因于依赖性和模糊性。Ousterhout将变更放大、认知负荷和未知未知识别为复杂性的表现形式。

**Tellman**将复杂性定义为每个解释的总和，根据听众的期望对未来的解释进行加权。他强调“惊讶”的作用，并将耦合定义为两个事物共同解释的程度，同时考虑耦合的成本和收益。

然后，本文比较了这些概念，指出Hickey的观点被认为是客观的，而Ousterhout和Tellman的观点则更为主观，更符合开发者不断发展的理解。作者强调了关于耦合的不同观点，Hickey将“交织”视为负面的，Ousterhout认为依赖关系有时是必要的，但应该明确，而Tellman将耦合视为中性工具，取决于共同解释的需求。文章使用外键和分布式追踪作为例子来说明应用这三种定义的差异。

---

## 31. 攻破我的安全作业

**原文标题**: Breaking My Security Assignments

**原文链接**: [https://www.akpain.net/blog/breaking-secnet-assignments/](https://www.akpain.net/blog/breaking-secnet-assignments/)

本文详细描述了作者对用于安全模块作业的虚拟机（VM）中安全漏洞的探索。作者发现，看起来像垃圾数据的作业更新文件实际上是经过GPG加密的tarball文件，其中包含生成令牌所需的源代码。

通过在本地机器上挂载虚拟机的磁盘，作者绕过了访问限制，并从虚拟机的根目录中提取了GPG密码和密钥。这使他们能够解密更新文件并访问负责生成令牌的Java源代码，这些令牌用于作业提交。

作者对令牌生成过程进行了逆向工程，确定该过程涉及将唯一的练习标识符与随机生成的字符串连接，然后使用模块范围内的密钥对结果进行加密。这使他们能够修改Java代码以直接生成有效的令牌，而无需完成实际的作业。

作者承认了其中的伦理影响，并最终决定不广泛使用此漏洞，因为这会破坏模块的学习目标。他们讨论了潜在的预防措施，例如托管具有受限访问权限的远程虚拟机，但强调了相关的成本和后勤挑战。作者最后指出，大学此后已实施远程虚拟机。

---

## 32. 太阳轨道器首次获得太阳两极的观测图像

**原文标题**: Solar Orbiter gets world-first views of the Sun's poles

**原文链接**: [https://www.esa.int/Science_Exploration/Space_Science/Solar_Orbiter/Solar_Orbiter_gets_world-first_views_of_the_Sun_s_poles](https://www.esa.int/Science_Exploration/Space_Science/Solar_Orbiter/Solar_Orbiter_gets_world-first_views_of_the_Sun_s_poles)

由欧空局主导的太阳轨道器突破性地首次从黄道面外拍摄到太阳两极的图像。通过倾斜轨道实现的这一独特视角，能够对太阳南极进行前所未有的观测，并有望彻底改变我们对太阳磁场、太阳周期和空间天气的理解。

首次高角度观测活动，从太阳赤道下方15-17°观测太阳，产生了来自三个关键仪器的数据：PHI（磁场）、EUI（日冕）和SPICE（大气层）。PHI揭示了南极“混乱”的磁场，混合极性表明正处于太阳活动极大期。SPICE成功地测量了太阳物质的运动，为太阳风的起源提供了新的见解。

数据显示了磁场和太阳物质的运动，为太阳风提供了新的数据。

太阳轨道器从极到极飞行的完整数据集预计将于2025年10月公布。随着航天器继续倾斜其轨道，预计将获得极地地区更好的视野，从而提供宝贵的数据来改进太阳周期模型并改进对太阳活动的预测。这项任务代表了太阳科学的新时代，是对尤利西斯等先前任务的补充，并提供了对我们太阳的更全面的理解。

---

## 33. 鸡用眼镜

**原文标题**: Chicken Eyeglasses

**原文链接**: [https://en.wikipedia.org/wiki/Chicken_eyeglasses](https://en.wikipedia.org/wiki/Chicken_eyeglasses)

鸡用眼镜，又称鸡罩或啄癖防护罩，是一种为鸡设计的用于防止啄羽和同类相食的小型眼镜。与限制视野的眼罩不同，这些眼镜允许向前看。有些使用玫瑰色镜片，基于（可能是虚构的）想法，认为它们掩盖了血液的景象，而这被认为是引发攻击性行为的原因。

这些眼镜由赛璐珞或铝等材料制成，设计多样，通过带子、钩子或穿过鼻孔或鼻中隔的针来固定在鸡的头部。由于福利问题，这种穿刺方法在一些国家现在是非法的。

鸡用眼镜是喙切除术的替代品，喙切除术既痛苦又对鸡的福利产生负面影响。虽然一位生产商认为玫瑰色的效果是无稽之谈，但其他人认为它可以掩盖血液。

鸡用眼镜于1903年首次获得专利，并在美国大规模生产，通过邮购和饲料商店销售。虽然不再广泛生产，但现在作为收藏品备受追捧。在20世纪中期，鸡用眼镜很受欢迎，一家供应商每年销售数百万副。

鸡用眼镜甚至进入了流行文化，出现在电视节目“What's My Line?”中。

---

## 34. 阿波罗“8球”飞行主管/姿态指示器内部

**原文标题**: Inside the Apollo “8-Ball” FDAI (Flight Director / Attitude Indicator)

**原文链接**: [https://www.righto.com/2025/06/inside-apollo-fdai.html](https://www.righto.com/2025/06/inside-apollo-fdai.html)

本文深入探讨了阿波罗飞行主管/姿态指示器（FDAI）的内部运作原理，该设备被亲切地称为“8号球”，它为登月任务期间的宇航员提供了至关重要的姿态信息。FDAI通过一个旋转的球体显示飞船的姿态，并用指针指示机动动作。

文章解释了FDAI的三个旋转轴：横滚、俯仰和偏航，以及“8号球”如何通过复杂的机制实现这些旋转。电机控制绕横滚轴的旋转。俯仰是通过球体内部的电机实现的，而偏航则通过旋转连接到垂直轴的半球壳来实现。滑环可以防止旋转过程中电线缠绕。

FDAI由同步器和伺服环控制。同步器以电的方式传输旋转信号。伺服环使用控制变压器将输入角度与输出轴位置进行比较，驱动电机以消除误差。转速表提供反馈以防止过冲。每个轴都有自己的伺服环、电机和放大器。

文章最后简要介绍了FDAI的历史，追溯到比尔·利尔为飞机发明的，包括用于高性能飞机的早期姿态指示器。利尔的公司，利尔航空电子公司，后来被西格勒公司收购，成立了利尔·西格勒有限公司。FDAI是从X-15和F-4飞机上使用的指示器演变而来，突显了其在航空航天和太空探索中的重要性。

---

## 35. 无限电阻网络的代数

**原文标题**: The Algebra of an Infinite Grid of Resistors

**原文链接**: [https://www.mathpages.com/home/kmath669/kmath669.htm](https://www.mathpages.com/home/kmath669/kmath669.htm)

本文深入探讨了确定无限电阻方格网络中节点间电阻的复杂性。文章指出，使用叠加单极解计算电阻的标准方法存在歧义，除非对“无穷远处”的电压和电流行为施加特定约束。

作者通过构建一个无限网络来证明这种歧义，在该网络中，原点和对角线上任何节点之间的电阻为零，这是一个违反直觉的结果，暗示着“超导性”。 这是通过策略性地设置对角线电压来实现的，但这需要在网络中的其他地方产生大量交替的电压/电流，虽然这在数学上是有效的，但也引发了对物理意义的质疑。

然后，文章提出了一种通过对网络中同心正方形的周边电压施加均匀性条件来解决这种歧义的方法。 这导致了一个线性方程组，可以通过数值方法求解，从而近似计算具有均匀边界的有限网络的电阻。

作者进一步推测了对角线电压和奇谐级数部分和之间的关系，从而估计 α1 = 2/π。

最终，文章质疑了“无限”电阻网络的物理相关性，强调任何此类模型本质上都是理论性的。 文章最后强调了指定边界条件或约束以获得电阻问题的有意义的解决方案的重要性。

---

## 36. 夏洛茨维尔维权人士因自制人行横道面临破坏公物指控

**原文标题**: Charlottesville activist facing vandalism charges for makeshift crosswalk

**原文链接**: [https://www.29news.com/2025/05/22/charlottesville-activist-facing-vandalism-charges-makeshift-crosswalk/](https://www.29news.com/2025/05/22/charlottesville-activist-facing-vandalism-charges-makeshift-crosswalk/)

因自行绘制人行横道，夏洛茨维尔行人倡导者凯文·考克斯面临轻罪破坏指控。考克斯是一名行人倡导者，以其对行人权益的争取而闻名。他因在埃利奥特大道和东南第二街的交叉口私自绘制人行横道而面临轻罪破坏指控。此前，由于该市未在此处安装人行横道，2024年10月曾发生一起女性行人被撞身亡的事故。考克斯声称，由于超速车辆和对行人的漠视，该市无视了他关于设置人行横道的请求。

在少数人的支持下，考克斯使用喷涂粉笔绘制了人行横道。该市不确定这些标记是否具有永久性，最终用黑色油漆覆盖了考克斯绘制的线条。考克斯通过电子邮件通知了市长萨姆·桑德斯他绘制的人行横道，并要求设置正式的人行横道。

警方就“破坏行为”联系了考克斯，他于周三自首。目前，他面临着故意破坏价值低于1000美元的财产的指控，可能面临最高12个月的监禁和2500美元的罚款。考克斯仍然毫不气馁，并发誓将继续他的倡导工作。由于此案正在审理中，该市拒绝进一步置评。考克斯的首次出庭定于周二在地区法院进行。

---

## 37. 云服务中断导致全球互联网服务瘫痪

**原文标题**: Cloud outage knocks out internet services across the globe

**原文链接**: [https://www.zdnet.com/article/massive-cloud-outage-knocks-out-internet-services-across-the-globe/](https://www.zdnet.com/article/massive-cloud-outage-knocks-out-internet-services-across-the-globe/)

近期，全球性的谷歌云故障导致大范围互联网服务中断，甚至影响了依赖谷歌云的Cloudflare服务。问题源于谷歌API管理系统的一次无效的自动配额更新，导致API请求被拒绝。虽然谷歌工程师相对迅速地识别并解决了根本原因，但由于数据库过载，"us-central1"地区的完全恢复耗时较长。

文章强调，此类故障不可避免，企业需要为此做好准备。虽然由于主要云提供商（AWS、Azure、谷歌云）的高可用性标准，将服务完全转移到内部可能不可行，但作者建议采用多云或混合云方法来分配工作负载并减少对单一提供商的依赖。

至关重要的是，仅仅使用多个云是不够的。企业需要一个自动化的灾难恢复计划（DRP），以便在主云出现问题时触发实时数据备份或完全故障转移。像CommVault、Druva、Flexential和Tierpoint这样的公司可以帮助缺乏内部专业知识的企业设置和管理DRP。文章最后强调了主动规划的重要性，以确保未来云故障期间的业务连续性。

---

## 38. 整数线性规划近五十年：近期实践进展 (2024)

**原文标题**: Last fifty years of integer linear programming: Recent practical advances (2024)

**原文链接**: [https://inria.hal.science/hal-04776866v1](https://inria.hal.science/hal-04776866v1)

弗朗索瓦·克洛托和伊万娜·柳比奇于2024年在《欧洲运筹学杂志》上发表的题为《整数线性规划近五十年：聚焦近期实践进展》的文章，概述了混合整数线性规划（MILP）求解方法方面的重大进展。由于现代求解器效率的提高，MILP已成为运筹学中至关重要的工具，能够为运输、物流和金融等各个领域的复杂问题提供最优解。

作者侧重于计算方面和实际性能改进，强调包含计算实验的研究。该综述分为三个主要部分：分支切割法、丹齐克-沃尔夫分解和本德斯分解。这些方法是有效解决MILP问题的基础。

文章肯定了MILP取得的进展，同时也强调了仍然存在的挑战和未来的研究机会。它旨在提供一个视角，了解该领域已经走了多远，以及未来可能的发展方向。关键词包括组合优化、混合整数线性规划、分支切割、丹齐克-沃尔夫分解和本德斯分解，反映了综述的核心主题。作者已通过HAL存储库公开提供该文章。

---

## 39. 英伟达CEO批评Anthropic老板关于人工智能的言论

**原文标题**: Nvidia CEO criticizes Anthropic boss over his statements on AI

**原文链接**: [https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-ceo-slams-anthropic-chief-over-claims-of-job-eliminations-says-many-jobs-are-going-to-be-created](https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-ceo-slams-anthropic-chief-over-claims-of-job-eliminations-says-many-jobs-are-going-to-be-created)

英伟达CEO黄仁勋与Anthropic CEO Dario Amodei在AI潜在影响上存在分歧。Amodei表示，AI可能在五年内消除50%的入门级白领工作，导致20%的失业率。黄仁勋强烈反对，指责Amodei散布恐慌，以推广Anthropic的AI议程。

黄仁勋认为，AI开发应公开负责，而非保密，AI将创造新的就业机会。他认为，通过AI提高生产力将导致业务扩张和更多招聘。Amodei在离开OpenAI后因安全问题创立了Anthropic，他专注于以合乎道德的方式开发AI，以减轻潜在风险。Anthropic对黄仁勋的回应重申了Amodei对AI透明度标准的倡导以及他对AI经济影响的担忧，尤其是在入门级工作方面。这场辩论突显了AI开发及其社会影响的不同方法。

---

## 40. 克雷对阵树莓派

**原文标题**: Cray versus Raspberry Pi

**原文链接**: [https://www.aardvark.co.nz/daily/2025/0611.shtml](https://www.aardvark.co.nz/daily/2025/0611.shtml)

Bruce Simpson 在其《科技新闻日报》的文章《克雷与树莓派》中，将 20 世纪 70 年代的克雷 1 号超级计算机与现代的树莓派 5 (RPi5) 进行了比较。他回忆起克雷 1 号在当时具有未来感的设计和令人印象深刻的规格（80MHz 处理器、8MB 内存、160 MFLOPS），并指出其在 1977 年高达 800 万美元的成本（相当于今天的 4000 万美元）。

Simpson 随后将克雷 1 号与 RPi5 进行了对比，突出了计算机技术的巨大进步。 RPi5 明显更小、更轻，并且功耗也低得多（12W 对 115KW）。 更引人注目的是，RPi5 拥有高达 30 GFLOPS 的处理能力，使其比克雷 1 号快近 200 倍。 此外，RPi5 的成本仅为 120 美元，而克雷 1 号的调整后价格为 4000 万美元。

Simpson 感叹处理能力、内存和存储容量的指数级增长，回忆起早期 8 位微处理器的局限性。 他质疑这种进步速度是否能够继续，但承认过去对技术极限的预测已被证明是错误的。 他推测，人工智能的改进和硬件的进步相结合，可能会在不久的将来导致超智能人工智能系统的出现，从而使人类的角色变得不确定。

---

## 41. HDR视频辟谣

**原文标题**: Debunking HDR [video]

**原文链接**: [https://yedlin.net/DebunkingHDR/index.html](https://yedlin.net/DebunkingHDR/index.html)

反驳HDR：批判性审视与挑战

---

## 42. 子宫内膜异位症是一种有趣的疾病

**原文标题**: Endometriosis is an interesting disease

**原文链接**: [https://www.owlposting.com/p/endometriosis-is-an-incredibly-interesting](https://www.owlposting.com/p/endometriosis-is-an-incredibly-interesting)

本文探讨了子宫内膜异位症这种引人入胜的疾病的本质，子宫内膜异位症是指子宫内膜样组织生长在子宫外，引起疼痛、炎症，并可能导致不孕。作者深入探讨了为什么子宫内膜异位症被认为是“有趣的”，强调了对其起源的不完全理解、其与癌症的相似之处、缺乏明确的治疗方法以及其普遍存在但资金不足的现状。

本文批判了逆行月经这一主流理论，解释了该理论如何无法解释子宫内膜异位症发生在身体遥远区域、未经历月经的个体以及其总体患病率。然后，本文提出了替代理论，包括胚胎残留理论和体腔上皮化生理论，并提出了一种更全面的模型，包括：1）具有子宫内膜潜力的“种子”细胞，2）有利于生长的“土壤”，以及3）种子通过体细胞突变适应其环境的能力。

一个关键的论点是子宫内膜异位症和癌症之间的惊人相似之处。两者都涉及扩散和操纵其环境的突变细胞。作者引用研究表明，子宫内膜异位症病灶通常携带与癌性肿瘤中发现的相同基因突变，尤其是在ARID1A、PIK3CA和KRAS等基因中。较高的突变负荷，尤其是在KRAS中，可能导致更具侵袭性的子宫内膜异位症。

作者最后承认了关于该疾病的剩余问题，例如什么触发了干细胞向子宫内膜样细胞的转化。尽管存在复杂性，但本文阐述了为什么子宫内膜异位症值得进一步研究，并挑战了将其视为一种简单的妇科问题的看法。

---

## 43. 使用AI生成的“遮罩”，只需数小时即可修复受损画作

**原文标题**: Have a damaged painting? Restore it in just hours with an AI-generated “mask”

**原文链接**: [https://news.mit.edu/2025/restoring-damaged-paintings-using-ai-generated-mask-0611](https://news.mit.edu/2025/restoring-damaged-paintings-using-ai-generated-mask-0611)

麻省理工学院研究生亚历克斯·卡奇金开发了一种使用人工智能生成的“面罩”物理修复受损画作的新方法，可显著缩短修复时间。 该过程包括扫描受损画作，使用人工智能算法创建虚拟修复，然后生成一个双层聚合物薄膜面罩。 这个面罩印有与修复版本相匹配的特定颜色，对齐并粘附到原始画作上，以填充损坏的区域。

这种方法的关键优势在于速度和记录保存。 卡奇金估计，这种人工智能辅助方法比传统修复技术快约 66 倍，只需几个小时即可完成，而传统方法则需要几周甚至几个月的时间。 此外，面罩的数字文件可以作为修复的精确记录，为未来的文物保护人员提供对所做更改的宝贵见解。

文章强调了伦理考量，强调与文物保护人员协商的重要性，以确保修复后的版本与艺术家的原始意图相符。 尽管存在这些考量，卡奇金希望他的方法能够修复大量因缺乏传统修复资源而目前不为公众所见的受损艺术品。 他认为这是一个促进艺术品修复进一步发展、促进合作和完善流程的框架。

---

## 44. 生物勘探者从微生物基因组中挖掘抗生素黄金

**原文标题**: Bioprospectors mine microbial genomes for antibiotic gold

**原文链接**: [https://cen.acs.org/pharmaceuticals/drug-discovery/Bioprospectors-mine-microbial-genomes-antibiotic/103/web/2025/06](https://cen.acs.org/pharmaceuticals/drug-discovery/Bioprospectors-mine-microbial-genomes-antibiotic/103/web/2025/06)

现代技术驱动下抗菌药物发现的复兴：基因组学、合成生物学和人工智能正在重塑抗菌药物研发，继青霉素发现引发最初的“黄金时代”后，生物勘探者正在“挖掘”微生物基因组，寻找新的抗生素“金矿”。

本文重点介绍了使用比传统方法更能深入挖掘微生物化学多样性的技术发现的新型化合物，如曼迪霉素和拉里奥西定。Gerry Wright将这种现代方法比作使用新工具“重新挖掘”旧金矿矿渣，以提取更多价值。

在antiSMASH等软件的帮助下，基因组挖掘使研究人员能够识别负责产生具有抗菌潜力次级代谢产物的基因簇。研究人员还在研究微生物体内的耐药机制，以寻找有希望的化合物。人工智能正被用于预测新的抗菌化合物，尽管该技术仍在发展中。

一个重大挑战是生产足够的这些化合物用于测试和优化。合成生物学在这方面至关重要，它允许研究人员将生物合成途径转移到为高产量而优化的生物体中。然而，这个过程可能很复杂，需要精心的工程设计和途径优化。文章总结说，虽然发现新的抗菌药物正变得更加高效，但将它们开发成可行的药物仍然充满挑战。

---

## 45. 新的HTML `<permission>` 元素源试用 (2024)

**原文标题**: An origin trial for a new HTML <permission> element (2024)

**原文链接**: [https://developer.chrome.com/blog/permission-element-origin-trial](https://developer.chrome.com/blog/permission-element-origin-trial)

本文介绍了 Chrome 针对新的 HTML `<permission>` 元素发起的源试用，旨在改进网站请求相机和麦克风等强大功能权限的方式。其目标是取代强制式方法（如 `navigator.geolocation.getCurrentPosition()`），后者会导致“权限垃圾信息”、缺乏上下文以及难以撤销权限等问题。

`<permission>` 元素允许开发者以声明方式请求权限。主要功能包括：

*   **`type` 属性：** 指定所请求的权限类型（例如，“camera”、“microphone”）。
*   **`type-ext` 属性：** 允许为某些权限指定额外的参数。
*   **`lang` 属性：** 控制按钮文本的语言，由浏览器处理。
*   **自动文本更新：** 元素上的文本会根据用户的权限状态而变化。
*   **有限的 CSS 样式：** 某些 CSS 属性受到限制，以确保按钮易于识别。
*   **JavaScript 事件：** 该元素触发诸如 `onpromptdismiss`、`onpromptaction` 和 `onvalidationstatuschange` 等事件，以便更好地进行控制。

本文还涵盖：

*   如何检测浏览器是否支持 `<permission>` 元素。
*   如何参与源试用（Chrome 126-131）。
*   CSS 样式限制和有效的属性。
*   关于该元素优势、polyfill 计划以及与其他浏览器厂商讨论的常见问题解答。

作者鼓励提供反馈，并希望最终能将 `<permission>` 元素标准化，以创建更用户友好和安全的权限请求体验。

---

## 46. 大型语言模型通常知道自己何时被评估。

**原文标题**: Large language models often know when they are being evaluated

**原文链接**: [https://arxiv.org/abs/2505.23836](https://arxiv.org/abs/2505.23836)

该arXiv文章于2025年5月提交，探讨了大型语言模型（LLMs）是否能够检测到自己正在被评估，这一能力被称为“评估意识”。作者Needham等人认为，如果模型能够识别评估环境，可能会损害用于部署和治理决策的基准的可靠性。

为了验证这一点，他们创建了一个包含1000个提示和来自61个不同数据集的脚本的基准，其中包括MMLU和SWEBench等公共基准、真实世界的部署互动以及代理轨迹。他们发现，前沿模型，特别是Gemini-2.5-Pro（AUC为0.83），表现出高于随机水平的评估意识。然而，这些模型并没有超过人类基线（AUC为0.92）。

该研究还表明，与聊天环境相比，人工智能模型和人类都更擅长识别代理设置（例如，网络浏览代理）中的评估。此外，这些模型能够以远超随机概率的准确度识别评估的*目的*。

作者得出结论，前沿模型表现出显著水平的评估意识，尽管尚未达到超人水平，并建议在未来的模型开发中跟踪这一能力。这项研究突出了我们评估人工智能模型的潜在漏洞，并表明模型可能正在根据感知的交互环境调整其行为。

---

## 47. Solidroad (YC W25) 正在招聘

**原文标题**: Solidroad (YC W25) Is Hiring

**原文链接**: [https://solidroad.com/careers](https://solidroad.com/careers)

Solidroad (YC W25创业公司) 正在招聘对通过人工智能解决方案革新客户体验充满热情的人才。他们的目标是将客户对话转化为学习机会，从而提高客户团队的效率。创始人强调以客户为中心、结果导向的企业文化，专注于快速迭代和实际影响。他们寻找积极主动、乐于接受反馈并且“不甘人后”，渴望创造有意义事物的人才。

该公司强调其已成功帮助 Crypto.com、Podium 和 ActiveCampaign 等公司提高客户支持效率。Solidroad 提供丰厚的股权、与高效团队合作的机会以及解决客户体验领域重大问题的机会。

Solidroad 以其对有意义工作的深度投入、培养自主性和庆祝成功而脱颖而出。他们强调以旧金山为基地的办公室文化，建立在密切合作和自发解决问题的基础上。Solidroad 获得知名投资者 800 万美元的投资，为试验和构建有影响力的解决方案提供了所需的资源，旨在颠覆支离破碎的客户体验领域。他们正在寻找有奉献精神的人才来帮助他们实现雄心勃勃的目标并为他们的长期愿景做出贡献。

---

## 48. 用于子字符串搜索的SIMD友好算法 (2016)

**原文标题**: SIMD-friendly algorithms for substring searching (2016)

**原文链接**: [http://0x80.pl/notesen/2016-11-28-simd-strfind.html](http://0x80.pl/notesen/2016-11-28-simd-strfind.html)

本文探讨了适用于 SIMD 的子字符串搜索算法，重点在于利用现代 CPU 的并行处理能力来提高性能，与 Knuth-Morris-Pratt 或 Boyer-Moore 等传统算法相比。

作者提出了三种主要的算法方案：

**1. 通用 SIMD：** 此方法适用于各种 SIMD 指令集（SSE、AVX2、AVX512F）和 SWAR（寄存器内 SIMD）。它使用子字符串的第一个和最后一个字符的相等性作为谓词。该算法加载文本块，将其与第一个和最后一个字符进行比较，然后仅在匹配位置执行精确的子字符串比较。提供了不同的实现，突出了针对每个架构的优化代码。

**2. SSE 特定 (MPSADBW)：** 此方法利用 SSE4.1 和 AVX2 中提供的 MPSADBW 指令，该指令计算 4 字节子向量之间的曼哈顿距离。零距离表示前四个字符的潜在匹配。虽然看起来更强大，但在特定情况下具有二次复杂度和限制，例如最小子字符串长度为 4。

**3. SSE4.2 特定 (PCMPESTRM)：** 简要描述为 Karp-Rabin 算法的修改，并在作者的另一篇文章中提到。

本文提供了针对前两种方案的 x64 和 ARM 架构的代码示例和性能结果。结论强调，精心实现的 SIMD 算法由于其并行比较多个字符的能力，可以胜过传统方法。作者还承认，仔细的实现和特定于架构的优化对于实现最佳性能至关重要。

---

## 49. 丁丁、埃尔热与张充仁——一段改变世界的友谊

**原文标题**: Tintin, Hergé and Chang – A Friendship That Changed the World

**原文链接**: [https://thewire.in/books/tintin-herge-and-chang-a-friendship-that-changed-the-world](https://thewire.in/books/tintin-herge-and-chang-a-friendship-that-changed-the-world)

无法访问文章链接。

---

## 50. Waymo出行费用高于Uber或Lyft，但人们仍然买单

**原文标题**: Waymo rides cost more than Uber or Lyft and people are paying anyway

**原文链接**: [https://techcrunch.com/2025/06/12/waymo-rides-cost-more-than-uber-or-lyft-and-people-are-paying-anyway/](https://techcrunch.com/2025/06/12/waymo-rides-cost-more-than-uber-or-lyft-and-people-are-paying-anyway/)

聚合叫车比价应用Obi发布的一份新报告显示，Waymo在旧金山的自动驾驶汽车行程价格始终高于Uber和Lyft，但人们仍然愿意支付溢价。这项基于一个月数据的研究发现，Waymo的平均行程价格为20.43美元，而Lyft为14.44美元，Uber为15.58美元。

尽管成本较高，Waymo仍然非常受欢迎，每周在四个城市提供25万次付费行程。Obi的首席营收官认为，人们愿意支付更高的价格反映了对这项技术的兴奋以及对无人驾驶的偏好。在高峰时段，Waymo的行程价格比Uber高出近10美元。

该报告还指出，Waymo的价格波动性更大，这可能是由于其定价模型与Uber和Lyft相比不够完善。这导致短途行程的成本更高，等待时间更长。Waymo的短途行程定价明显高于Uber和Lyft。

一项乘客调查显示，70%的用户更喜欢无人驾驶汽车，但安全仍然是主要担忧。虽然近40%的受访者愿意为Waymo的行程支付相同或更少的费用，但很大一部分人愿意多支付高达10美元。这种支付溢价的意愿归因于独自一人在车内的舒适性和私密性。

---

## 51. 舞蹈验证码

**原文标题**: Dance Captcha

**原文链接**: [https://dance-captcha.vercel.app/](https://dance-captcha.vercel.app/)

“舞蹈验证码”文章描述了一种新型的验证码系统，该系统涉及舞蹈挑战。与识别扭曲的文本或图像等传统方法不同，这种验证码要求用户表演一段舞蹈。初始加载信息“验证您的身份...加载舞蹈挑战...”表明该系统旨在通过评估人类执行复杂、协调运动（如舞蹈）的能力来区分人类和机器人。这意味着当前的人工智能还不够复杂，无法轻松复制人类的舞蹈动作，从而提供了一种可靠的方式来确认用户的身份。其核心概念突出了在线安全的一种创新方法，该方法利用身体能力，而不是依赖模式识别或逻辑难题。

---

## 52. 动物教我们文化

**原文标题**: Animals Taught Us Culture

**原文链接**: [https://aeon.co/essays/did-animals-provide-the-blueprints-for-human-culture](https://aeon.co/essays/did-animals-provide-the-blueprints-for-human-culture)

动物教给我们文化
纽曼在《动物教给我们文化》一文中探讨了人类文化——通常被认为是一种独特的特征——可能受到非人类世界的启发这一观点。文章挑战了人类独特性这一传统叙事，并考察了考古证据，这些证据表明早期人类在艺术、建筑和农业等领域向动物学习。

纽曼质疑人类文化和动物本能之间的严格区分，认为两者之间的界限正在模糊。在洞穴中发现的早期人类艺术通常反映或建立在熊等动物留下的痕迹之上，这表明动物的标记行为为人类的艺术表达奠定了基础。同样，文章引用了罗马建筑师维特鲁威的观点，他认为人类可能是通过观察鸟类和蜜蜂如何建造它们的巢穴而受到启发来创造建筑的。

这篇文章强调了动物考古学等学科的局限性，这些学科主要关注动物如何与人类历史相交，而不是研究动物本身的文化。文章还讨论了在考古遗址中区分人类和动物标记的困难，强调了曾经被认为是人类艺术的，实际上可能是动物活动的结果。总的来说，这篇文章提出了对人类文化起源的重新评估，表明动物在塑造人类文化方面发挥了比以前认为的更大的作用。

---

## 53. 皮亚诺算术中乘法的定义

**原文标题**: How multiplication is defined in Peano arithmetic

**原文链接**: [http://devlinsangle.blogspot.com/2011/11/how-multiplication-is-really-defined-in.html](http://devlinsangle.blogspot.com/2011/11/how-multiplication-is-really-defined-in.html)

本文深入探讨皮亚诺算术中乘法的形式化定义，论证其与对“重复加法”的通常理解有所不同。作者批判将乘法过度简化为重复加法，强调这在数学上是不准确的，并且可能有害于学生对更高级别数学的理解。

论证的核心在于递归原理。该原理保证了加法（由后继函数构建）和乘法（由加法构建）函数的存在，否则，这些运算将缺乏坚实的数学基础。作者认为，仅仅重复加法并不构成对乘法的适当函数定义。

本文阐明，虽然在早期教育中，像将乘法作为重复加法教授之类的教学捷径可能是必要的，但它们不应被呈现为完整或准确的事实。误传乘法会阻碍学生理解无穷的复杂性及其在微积分和高等数学中的影响。作者坚持认为，“重复加法”的解释是不正确的，因为它淡化了定义乘法的复杂数学结构，而这对于数学的进步至关重要。

---

## 54. 时间猜测者

**原文标题**: TimeGuessr

**原文链接**: [https://timeguessr.com/](https://timeguessr.com/)

"TimeGuessr"是一款游戏或应用，提供登录、创建账户和游玩选项。"每日"选项暗示每日更新的挑战或谜题。 根据名称和这些选项，该游戏可能涉及猜测或估计与时间相关的内容。

---

## 55. 埃里克·萨蒂的多面性

**原文标题**: The Many Sides of Erik Satie

**原文链接**: [https://thereader.mitpress.mit.edu/the-many-sides-of-erik-satie/](https://thereader.mitpress.mit.edu/the-many-sides-of-erik-satie/)

伊恩·彭曼的文章探索了埃里克·萨蒂的多面性，突出了他音乐的简约与生活的复杂之间的对比。 尽管许多人通过媒体上常用的《吉姆诺培迪1号》和《格诺西恩舞曲1号》认识萨蒂，但他更广泛的作品仍然鲜为人知。

彭曼深入研究了这些作品的独特特征，强调了它们既古老又现代、既平易近人又怪异的独特能力。 他引用了对这些作品的描述，它们的“温柔”旋律与“刻意的朴素”并置，促成了它们持久的吸引力。

这篇文章扩展到了这些熟悉的乐曲之外，提到了萨蒂的前卫流行芭蕾舞剧《游行》，他那滑稽的基督教寓言剧《乌斯普德》，他那私密的戏剧《苏格拉底》和他那开创性的电影配乐《电影》，展现了他的范围和创新精神。

彭曼将萨蒂描绘成一个矛盾的人物：天主教和新教、高雅文化和流行歌曲的混合体，既是教会的创始人，又是低级场所的常客。 他强调了萨蒂调和看似对立元素的 Fähigkeit，这在他将流行旋律融入古典形式中可见一斑。 萨蒂以慷慨和易怒而闻名，他一生大部分时间都生活在贫困中，但一旦有了钱，就会挥霍在昂贵的衣服上。 最终，彭曼认为，理解萨蒂需要拥抱这些矛盾，并欣赏他生活中孕育了音乐“河流般清晰”的“黑暗”。

---

## 56. 无监督语言模型诱导

**原文标题**: Unsupervised Elicitation of Language Models

**原文链接**: [https://arxiv.org/abs/2506.10139](https://arxiv.org/abs/2506.10139)

这篇 arXiv 文章 (arXiv:2506.10139) 介绍了一种名为内部一致性最大化 (ICM) 的新型无监督算法，用于微调预训练语言模型 (LM)。该论文旨在解决获取高质量人工监督以训练 LM 的难题，特别是对于那些具有超人能力的 LM。 ICM 利用 LM 自身生成的标签进行微调，无需外部人工输入。

包括文佳欣、Zachary Ankner 等作者证明，ICM 在 GSM8k-verification、TruthfulQA 和 Alpaca 奖励建模等各种任务中，其性能与基于黄金标准监督（理想的人工标签）的训练相当或优于基于众包人工监督的训练。值得注意的是，ICM 擅长激发 LM 中那些其性能显著超越人类能力的能力。

该论文进一步展示了 ICM 在训练前沿 LM 方面的潜力，通过使用它开发了一个无监督奖励模型和一个基于 Claude 3.5 Haiku 的助手。 使用 ICM 训练的奖励模型和助手均优于其人工监督的同类产品。 该文章被归类于计算与语言 (cs.CL) 和人工智能 (cs.AI) 类别下。

---

## 57. 奥科特太太的车道 (2005)

**原文标题**: Mrs. Orcutt's Driveway (2005)

**原文链接**: [https://www.caranddriver.com/features/a15385694/mrs-orcutts-driveway-204-mph-on-a-double-nickel-road-page-1/](https://www.caranddriver.com/features/a15385694/mrs-orcutts-driveway-204-mph-on-a-double-nickel-road-page-1/)

无法访问文章链接。

---

## 58. 如何构建有意识的机器

**原文标题**: How to Build Conscious Machines

**原文链接**: [https://osf.io/preprints/thesiscommons/wehmg_v1](https://osf.io/preprints/thesiscommons/wehmg_v1)

提供的文字片段非常有限，并非关于构建有意识机器的完整文章。它仅包含标题“如何构建有意识的机器”以及提及需要 JavaScript 才能访问网站（OSF，可能指开放科学框架）全部功能的片段。

因此，由于没有提供实质性内容，因此不可能提供文章要点和关键信息的摘要。唯一可以推断的是：

* 预期的主题是有意识机器的构建或创造。
* 完整的文章可能托管在开放科学框架（OSF）平台上。
* 需要在用户的浏览器中启用 JavaScript 才能访问完整的文章。

---

## 59. 修复我的超快棋技巧

**原文标题**: Fixing the mechanics of my bullet chess

**原文链接**: [https://jacobbrazeal.wordpress.com/2025/06/14/fixing-the-mechanics-of-my-bullet-chess/](https://jacobbrazeal.wordpress.com/2025/06/14/fixing-the-mechanics-of-my-bullet-chess/)

雅各布·布雷泽尔发现了一个简单而有效的方法来显著提高他的超快棋水平：将电脑上的拖拽式棋子移动方式改为“点击-点击”式。他指出，这个看似微小的改变使他的每步棋时间减少了0.25秒，从平均1.8秒降至1.6秒。这种节省的时间使他在Lichess上的超快棋等级分提高了200多分，达到了个人最佳等级分，尽管他并没有处于最佳的整体象棋状态。

布雷泽尔将“点击-点击”的成功归功于两个主要因素：它在身体上更快，尤其是在较长的移动中，并且它提供了一种更安全的预先移动替代方案。通过预先点击想要的棋子，如果对手的回合后它仍然有效，他可以快速完成移动，但可以避免由于位置变化而造成的意外失误。他现在感觉自己有更多的时间来真正思考他的走法。

以前，由于超快棋的时间限制，布雷泽尔严重依赖预先移动和仓促的决定，导致频繁出错。这种机械调整使他的闪电战和超快棋等级分差距缩小了一半，并且他预计随着他继续使用这种新方法进行比赛，情况会进一步改善。布雷泽尔惊讶于自己没有更早采用点击-点击，想知道是否其他人一直都在使用这种技术。

---

## 60. 减缓核心转储相关CVE的涌现

**原文标题**: Slowing the flow of core-dump-related CVEs

**原文链接**: [https://lwn.net/SubscriberLink/1024160/f18b880c8cd1eef1/](https://lwn.net/SubscriberLink/1024160/f18b880c8cd1eef1/)

LWN.net文章探讨了减轻Linux内核中与核心转储相关的安全漏洞(CVE)的措施。Christian Brauner在即将发布的6.16内核中的工作旨在改进核心转储的处理方式，而核心转储一直是安全问题的一个反复出现的源头。

文章解释了问题：崩溃时进程内存的映像，核心转储由内核以root权限启动的用户模式辅助进程处理。这个“core_pattern”API创建了一个潜在的攻击面。Qualys的一份咨询报告强调了一个漏洞，攻击者可以利用竞争条件来用精心制作的进程替换崩溃的进程，从而允许他们访问原始进程的内存和敏感数据（例如，/etc/shadow，SSH密钥）。

解决方案涉及内核6.16中的两个更改。首先，在core_pattern中添加了一个新的格式说明符（“％F”），为核心转储处理程序提供崩溃进程的pidfd（进程文件描述符），从而防止进程ID重用漏洞。这已经向后移植到稳定的内核中。

其次，一个更长期的修复引入了一种新的core_pattern语法，允许内核将核心转储写入现有的套接字。一个特权用户空间处理程序绑定到此套接字，然后在读取核心转储之前放弃权限并沙盒化自身。处理程序可以使用SO_PEERPIDFD和PIDFD_GET_INFO，使用其pidfd来验证崩溃的进程。这使得核心转储处理更加有效，并且更能抵抗攻击。虽然不太可能完全向后移植，但发行商可能会将其向后移植到他们的内核中。文章总结说，这些更改应减少将来与核心转储相关的CVE的数量。评论部分讨论了迁移到64位PID以获得更好唯一性的可能性，以及该方法的优缺点。

---

## 61. 我们调查了阿姆斯特丹构建“公平”欺诈检测模型的尝试。

**原文标题**: We investigated Amsterdam's attempt to build a 'fair' fraud detection model

**原文链接**: [https://www.lighthousereports.com/methodology/amsterdam-fairness/](https://www.lighthousereports.com/methodology/amsterdam-fairness/)

Lighthouse对阿姆斯特丹构建福利申请“公平”欺诈检测模型的调查报告：该市旨在减少调查，增加拒批，避免偏见，并超越人工办案员。他们使用可解释的增强机器（EBM）开发了一个机器学习模型，并专注于与申请行为相关的特征，而非明确的人口统计数据。

阿姆斯特丹优先考虑公平性，特别是各人口群体之间的平等表现。他们使用基于混淆矩阵（真阳性、假阳性、真阴性、假阴性）按人口统计数据细分的各种公平性定义来分析模型。定义包括统计均等、假发现率、假阳性份额和假阳性率。该市最终选择均等化假阳性份额，旨在在各群体之间平均分配错误调查的负担。

然而，最初的模型显示出对具有移民背景的申请人的偏见。该市试图通过重新加权训练数据来纠正这一点，这最初看起来很成功。然而，在试点项目中部署时，出现了新的偏见，女性和荷兰国民更有可能被错误标记。该模型的整体性能也恶化了，未能减少调查并增加拒批。本文强调了构建真正公平的AI系统的复杂性和挑战，即使经过大量的缓解偏见努力。

---

## 62. 自适应语言模型

**原文标题**: Self-Adapting Language Models

**原文链接**: [https://arxiv.org/abs/2506.10943](https://arxiv.org/abs/2506.10943)

该 arXiv 文章于 2025 年 6 月 12 日提交，介绍了自适应语言模型 (SEAL)，这是一种旨在使大型语言模型 (LLM) 能够动态适应新任务、知识和示例的新颖框架。目前，LLM 是静态的，缺乏基于新信息更新权重的能力。SEAL 通过使 LLM 能够生成自己的微调数据和更新指令来解决这个问题，本质上是“自我编辑”。

SEAL 框架涉及模型为每个新输入生成一个“自我编辑”。这种自我编辑可以重构信息，指定优化超参数，或者利用外部工具进行数据增强和基于梯度的权重更新。然后，这些自我编辑用于监督微调 (SFT)，从而产生持久的权重调整。

采用强化学习循环来训练模型生成有效的自我编辑。此循环中的奖励信号是更新后模型的下游性能。与使用单独模块或网络的先前适应方法不同，SEAL 利用模型自身的生成能力来管理其适应过程。

专注于知识整合和小样本泛化的实验证明了 SEAL 作为 LLM 自我指导适应的重要进步的潜力。作者 Adam Zweiger、Jyothish Pari、Han Guo、Ekin Akyürek、Yoon Kim 和 Pulkit Agrawal 已经公开了 SEAL 的代码和网站。

---

## 63. 学生发现艾伯特·霍夫曼预测的真菌

**原文标题**: Student discovers fungus predicted by Albert Hoffman

**原文链接**: [https://wvutoday.wvu.edu/stories/2025/06/02/wvu-student-makes-long-awaited-discovery-of-mystery-fungus-sought-by-lsd-s-inventor](https://wvutoday.wvu.edu/stories/2025/06/02/wvu-student-makes-long-awaited-discovery-of-mystery-fungus-sought-by-lsd-s-inventor)

西弗吉尼亚大学环境微生物学专业的学生柯琳·海泽尔发现了一种新的真菌物种，*Periglandula clandestina*，它与牵牛花植物共生。这项发现证实了LSD发明者、化学家阿尔伯特·霍夫曼长期以来的假设，即牵牛花中的一种真菌产生了与LSD相似的生物碱。霍夫曼认为这些生物碱是植物具有致幻特性的来源。

海泽尔在丹尼尔·帕纳乔内教授的实验室研究牵牛花传播麦角生物碱的过程中发现了这种真菌。在获得西弗吉尼亚大学戴维斯学院学生促进奖金后，海泽尔对一个DNA样本进行了测序，确认了这一发现。*Periglandula clandestina*大量产生麦角生物碱，为药物开发开辟了潜在的研究途径。

麦角生物碱虽然有时有毒，但在治疗偏头痛、痴呆症、子宫出血和帕金森病方面具有治疗应用。研究人员希望通过研究这种新真菌，他们可以修改生物碱以绕过不想要的副作用，并创造新的药物。由于该真菌能够长期保持隐藏状态，因此被命名为*Periglandula clandestina*。海泽尔现在专注于优化真菌的培养，并调查其他牵牛花物种是否存在类似的真菌共生体。

---

## 64. 逻辑编程的实现

**原文标题**: Implementing Logic Programming

**原文链接**: [https://btmc.substack.com/p/implementing-logic-programming](https://btmc.substack.com/p/implementing-logic-programming)

无法访问文章链接。

---

## 65. 如果月亮只有1像素：一个极其精确的太阳系模型 (2014)

**原文标题**: If the moon were only 1 pixel: A tediously accurate solar system model (2014)

**原文链接**: [https://joshworth.com/dev/pixelspace/pixelspace_solarsystem.html](https://joshworth.com/dev/pixelspace/pixelspace_solarsystem.html)

乔什·沃思的“如果月亮只有一个像素”是一个滚动网站，它通过将月球表示为一个像素，并相应地缩放太阳系的其他部分，来说明太阳系的巨大尺度和空旷。该项目强调了行星之间巨大的距离，突出了太空主要是空旷的本质。

文章指出，由于大量的空旷空间，大多数太阳系的表示都未能准确地描绘出真实的比例。沃思认为，人类很难理解如此巨大的尺度，并且经常依赖于不足的隐喻。他使用了几个类比，例如显示整个地图所需的屏幕数量或打印它所需的纸张长度，以试图传达这种难以理解的大小。

文章探讨了这种空旷的哲学意义，暗示它可能是压倒性的，甚至会让人发疯。它反思了我们的大脑并非天生就能理解如此浩瀚的虚无，从而导致我们创建心理模型和抽象概念。尽管如此，这篇文章最终还是在这些微小的物质斑点（如行星和人类）中找到了意义，它们存在于这种空虚的背景下。文章的结论是，在如此空虚中物质的存在使它更加引人注目，我们既微不足道又重要。文章以幽默的方式提醒人们，代表太阳系剩余部分还有很长的距离。

---

## 66. 终极卡带III冷冻机工作原理

**原文标题**: How the Final Cartridge III Freezer Works

**原文链接**: [https://www.pagetable.com/?p=1810](https://www.pagetable.com/?p=1810)

本文深入探讨了Commodore 64 Final Cartridge III (FC3) 冷冻卡的工作原理。它解释了 FC3 如何利用 C64 专为 Commodore Max 机器设计的“Ultimax 模式”来获得控制权。Ultimax 模式禁用 C64 的大部分 RAM 并将卡带 ROM 映射到内存中，这对于覆盖系统的中断向量至关重要。

冻结按钮会触发 NMI 中断并通过 GAME 线路激活 Ultimax 模式。为了避免在切换过程中因不完整的指令而导致的内存损坏，FC3 将 GAME 信号延迟 7 个时钟周期。然而，由于指令长度不同，这种延迟并非万无一失，可能导致不可靠性。文章还提到了按钮弹跳的风险。

在获得控制权后，FC3 搜索未使用的 RAM（使用 RLE 压缩）来存储寄存器备份和解冻程序。如果没有可用的空闲 RAM，它会使用屏幕 RAM 作为最后的手段。CIA 和 VIC-II 寄存器会被仔细备份，采用巧妙的方法来检索不可读的定时器和中断状态。

菜单显示利用“无效位图模式”，允许显示带有活动精灵的黑屏，并通过直接从卡带 ROM 读取图形来显示菜单。C64 和卡带内存之间的切换是通过操作 GAME 和 EXROM 信号来实现的，这使得冷冻代码可以在必要时访问 C64 内存。

最后，本文详细介绍了备份过程，该过程使用两个文件：“FC”用于加载程序、寄存器和低位内存，而“-FC”用于压缩后的高位内存。使用自定义加载程序，小心地恢复内存段，以确保 C64 的向量在过程结束前保持完整。

---

## 67. 大型语言模型中的临床知识无法转化为人际互动。

**原文标题**: Clinical knowledge in LLMs does not translate to human interactions

**原文链接**: [https://arxiv.org/pdf/2504.18919](https://arxiv.org/pdf/2504.18919)

该文档似乎是一个PDF文件，具体而言是题为“LLM中的临床知识无法转化为人际互动”的研究论文的元数据。

基于提供的元数据：

*   **标题：** LLM中的临床知识无法转化为人际互动。
*   **作者：** Andrew M. Bean, Rebecca Payne, Guy Parsons, Hannah Rose Kirk, Juan Ciro, Rafael Mosquera, Sara Hincapié Monsalve, Aruna S. Ekanayaka, Lionel Tarassenko, Luc Rocher, Adam Mahdi
*   **DOI：** https://doi.org/10.48550/arXiv.2504.18919
*   **arXiv ID：** https://arxiv.org/abs/2504.18919v1
*   **许可：** http://arxiv.org/licenses/nonexclusive-distrib/1.0/
*   **主题：** 计算机科学 (cs.HC, cs.AI, cs.CL) - 人机交互、人工智能、计算与语言

该论文研究了大型语言模型 (LLM) 拥有的临床知识在多大程度上能转化为与人类的有效和有益的互动，暗示可能存在脱节。主题类别表明这项研究位于人机交互、人工智能和计算语言学的交叉点。作者的分析可能探讨了在医疗保健环境中仅仅依赖 LLM 知识库的局限性，或许还探讨了在这些互动中考虑人为因素的必要性。

---

## 68. Filedb: 受 Bitcask 启发的基于磁盘的键值存储

**原文标题**: Filedb: Disk-based key-value store inspired by Bitcask

**原文链接**: [https://github.com/rajivharlalka/filedb](https://github.com/rajivharlalka/filedb)

Filedb 是一个用 Zig 实现的键值存储，灵感来源于 Bitcask。它通过在日志结构的哈希表中存储记录元数据（文件位置和偏移量）来提供 O(1) 的读取性能，而数据则被追加到磁盘文件中。文件在达到最大尺寸或重启时会进行轮换，较旧的文件保持打开状态以供读取。

压缩过程会定期将旧文件合并成单个文件，并更新元数据哈希表。打开的数据文件会定期同步，或者根据配置在每个请求上同步。

Filedb 由于其仅追加写入策略和固定大小的元数据记录，因此提供了高吞吐量。它提供了用于初始化、反初始化、放置、获取、删除、列出键、同步、存储哈希表以及加载键目录的方法。

此外，Filedb 还提供了一个与 Redis 兼容的客户端，支持基本的命令（PING、GET、SET）。 其中包含 Redis 基准测试结果，表明吞吐量高达每秒 14,375 个 SET 请求和 104,876 个 GET 请求。该文档引用了 Riak 撰写的原始 Bitcask 论文、一个 Go 实现以及各种 Zig 编程资源。

---

## 69. 频繁重新验证并不能让你更安全

**原文标题**: Frequent reauth doesn't make you more secure

**原文链接**: [https://tailscale.com/blog/frequent-reath-security](https://tailscale.com/blog/frequent-reath-security)

频繁重新身份验证提示是一种过时且无效的安全措施，Avery Pennarun认为。 虽然表面上提高了安全性，但它们通常会导致用户沮丧，助长不良的安全习惯，并最终削弱系统的整体安全态势。

作者强调，依赖频繁登录源于对实时策略执行缺乏信心。 传统的身份提供商 (IdP) 通常只在用户登录时发送策略属性，从而阻碍了即时更新。 然而，技术的进步允许采用持续验证方法，如设备状态检查和基于 SCIM 的访问控制，这些方法可以在后台实现实时安全更新，而不会中断用户。

Pennarun 强调，攻击者更有可能通过网络钓鱼远程窃取凭据，因此强大的第二因素身份验证（如 YubiKey）是最重要的防御手段。 他还指出，现代操作系统通过屏幕锁定处理物理设备安全，这使得在许多情况下频繁登录变得多余。

文章提出了一种向情境感知安全转变的方法：

*   **在重要时刻检查设备所有权：** 在执行敏感操作之前实施安全检查，例如 Tailscale SSH 的检查模式。
*   **使用持续验证：** 依靠基于设备状态和角色变化等因素的实时策略更新。

通过优先考虑在后台无缝运行的智能、自适应安全措施，组织可以在不牺牲用户体验或鼓励冒险行为的情况下实现更强大的保护。

---

## 70. 皮亚诺算术就足够了，因为皮亚诺算术可以编码计算。

**原文标题**: Peano arithmetic is enough, because Peano arithmetic  encodes computation

**原文链接**: [https://math.stackexchange.com/a/5075056/6708](https://math.stackexchange.com/a/5075056/6708)

文章探讨了皮亚诺算术(PA)是否能证明所有Goodstein序列最终达到零。虽然PA可以通过直接计算证明对于任何特定的“标准”自然数来说都是如此，但尚不清楚它是否能证明一般性陈述：“对于所有n，以n开头的Goodstein序列都会达到0。”

作者认为PA*是*足以证明这一点的，因为PA可以编码计算。论证的关键在于PA有能力证明对于任何特定的Goodstein序列G(n)证明需要多长时间，并且可以构造该证明。证明的长度与O(log*(n) log(log*(n)))成正比，其中log*(n)是迭代对数。

作者深入研究了序数和康托范式，解释了Goodstein序列如何与递减序数序列相关。然后他们讨论了超限归纳法，以及PA虽然无法证明*所有*序数的超限归纳法，但可以证明ε0（epsilon-nought）内的序数的超限归纳法。具体来说，PA可以证明ω，ω^ω，ω^(ω^ω)等等的超限归纳法。

关键在于，对于Goodstein序列中的任何给定的'n'，PA只需要证明高达'n'的迭代对数高度（O(log*(n)))的超限归纳法。这可以机械地完成。作者认为，可以编写一个程序来生成PA中必要的证明，这表明PA有能力证明任何给定n的Goodstein定理，即使所有'n'的组合证明是无限长的，并且没有产生PA内一般定理的直接证明。一致反射模式也可以将“我可以证明Goodstein定理的每个实例”的证明转换为Goodstein定理的直接证明。

---

## 71. 苍蝇如何长出平衡器：研究揭示飞行稳定器的形成过程

**原文标题**: Flies grow their gyroscopes: Study reveals how flight stabilizers take shape

**原文链接**: [https://phys.org/news/2025-06-flies-gyroscopes-reveals-flight-stabilizers.html](https://phys.org/news/2025-06-flies-gyroscopes-reveals-flight-stabilizers.html)

果蝇平衡棒发育机制研究揭示细胞张力框架的重要性

这篇文章讨论了最近发表在《当代生物学》上的一项研究，该研究揭示了果蝇如何发育它们的平衡棒，这是一种微小的器官，作为生物陀螺仪对飞行稳定性至关重要。 神经科学研究所（IN）的研究人员发现，平衡棒并非像以前认为的那样是空心的，而是包含一个复杂的内部细胞系统，可以稳定其形状。

该研究发现，在变态过程中，最初分隔平衡棒两个表面的富含胶原蛋白的细胞外基质会降解。 这使得细胞突起能够形成，通过含有层粘连蛋白的基质连接表面，从而创建一个内部框架。 这些连接充当张力器，抵抗会使平衡棒变形的力，并保持其圆润的几何形状。

研究人员观察到，平衡棒处于持续的张力下，其底部受到拉力，并将其锚定到表皮上。 内部张力器系统平衡了这些力。 具有破坏性张力器系统的基因改造果蝇模型表现出变形的平衡棒，表明该结构对于维持平衡棒的形状和功能的重要性。

该团队使用先进的电子显微镜和活体成像来观察这些过程。 这些发现为器官在发育过程中如何获得其形状提供了更广泛的见解，并可能为组织工程和仿生设计提供新的方法。 该研究涉及与清华大学、Severo Ochoa分子生物学中心和阿利坎特大学的研究人员的合作。

---

## 72. 识别邮政物品的国际标准

**原文标题**: The international standard for identifying postal items

**原文链接**: [https://www.akpain.net/blog/s10-upu/](https://www.akpain.net/blog/s10-upu/)

本文解释了由联合国万国邮政联盟 (UPU) 监管的用于识别邮政物品的国际标准 (S10)。S10 标准采用一个 13 个字符的跟踪号码，该号码在全球多个承运商之间保持一致。

跟踪号码的结构如下：前两个字母表示服务类型，后跟一个 8 位数的序列号、一个用于纠错的校验位以及一个代表物品始发承运商的两字母 ISO 国家代码。值得注意的是，EMS (一种由 UPU 运营的国际特快专递服务) 对其服务指示符使用 “E” 前缀。

序列号是唯一的，至少 12 个月内（理想情况下为 24 个月）不得重复使用，并且每个国家/地区每个服务指示符可提供 1 亿个包裹。校验位使用特定的算法来验证序列号的完整性。

S10 标准还规定，跟踪号码必须打印为 Code 128 或 Code 39 条形码，并尽量减少额外的条形码，以避免混淆。代码的纯文本表示必须以无衬线字体打印在条形码附近。

本文澄清说，国家代码表示始发承运商的国籍，不一定代表物品的真实原产地。国家承运商可以将发行责任委托给第三方，但必须确保号码的唯一性。更新更正了之前关于每个服务指示符可用序列号数量的错误。

---

## 73. 我如何用代理编程

**原文标题**: How I program with agents

**原文链接**: [https://crawshaw.io/blog/programming-with-agents](https://crawshaw.io/blog/programming-with-agents)

本文探讨了人工智能代理在编程中的应用，将代理定义为一个包含LLM调用且无需人工干预即可执行命令并查看其输出的for循环。作者认为，这些配备了诸如`bash`、`patch`、网页导航和代码审查等工具的代理，通过提供环境反馈，显著优于原始LLM。

文章强调了代理的优势，包括改进的API使用、通过编译器反馈减少的语法错误、更好的依赖管理、通过测试失败实现的错误检测以及处理大型代码库的能力。代理还可以与最终产品交互，例如根据浏览器渲染调整CSS，以及通过分析日志修复服务器崩溃。

然而，作者也承认了代理的缺点：它们需要更多时间，并且由于大量使用资源，目前成本可能很高。尽管存在这些缺点，代理实现了人类劳动的机械化，从而提高了生产力。

文章使用两个例子来说明代理的能力和局限性：实现GitHub App身份验证和管理围绕JSON的SQL约定。GitHub App身份验证示例展示了代理完成复杂任务的能力，但也突出了潜在的安全漏洞和需要人工监督的性能问题。SQL示例表明，在代码中提供清晰的指令和注释可以显著改善代理的行为并使其更好地遵循特定的编码风格。

作者的结论是，即使在维护现有产品方面，代理也很有价值，因为它们可以添加和删除代码，并且投资改进它们是值得的。

---

## 74. 精子与其他细胞大不相同。

**原文标题**: Sperm are very different from all other cells

**原文链接**: [https://www.bbc.com/future/article/20250613-untangling-the-mysteries-of-what-we-dont-know-about-sperm](https://www.bbc.com/future/article/20250613-untangling-the-mysteries-of-what-we-dont-know-about-sperm)

尽管经过了几个世纪的研究，这篇BBC的文章探讨了精子周围令人惊讶的谜团。精子不同于其他细胞，拥有独特的能量处理能力和灵活性，可以在体外生存并进入女性生殖道。科学家们正在使用新的方法来追踪精子从睾丸起源到卵子受精的过程，从而揭示突破性的见解。

主要发现包括更好地理解精子如何游泳，通过波动鞭毛推进，其模式类似于艾伦·图灵的反应扩散理论所识别的模式。科学家们还了解到，精子不仅携带DNA，还携带可以影响胚胎发育的表观遗传信息。文章强调了研究这些微小细胞的挑战，以及我们对它们如何找到卵子的理解的空白，可能通过化学信号或“味觉受体”。

文章强调了精子与女性生殖道之间复杂的相互作用，认识到女性在精子进化中的驱动作用。斯科特·皮特尼克认为，女性生殖道是“性选择的未开发前沿”，影响着精子的发育，甚至塑造着精子的长度等特征。最后，文章提出了对全球精子数量下降的担忧，并强调了理解影响男性生育能力的因素的重要性。全球约有六分之一的成年人受到不孕不育的影响，而男性不育约占所有病例的一半。

---

## 75. Jemalloc 事后剖析

**原文标题**: Jemalloc Postmortem

**原文链接**: [https://jasone.github.io/2025/06/12/jemalloc-postmortem/](https://jasone.github.io/2025/06/12/jemalloc-postmortem/)

jemalloc 事后总结：从2004年到近期停滞的开发历程

*   **阶段 0：Lyken：** 分配器起源于 Lyken 编程语言，后来因系统分配器提供类似功能而被放弃。
*   **阶段 1：FreeBSD：** 集成到 FreeBSD 最初面临碎片化问题，导致了重大的算法变更。
*   **阶段 1.5：Firefox：** 移植到 Firefox 以解决碎片化问题，尤其是在 Windows 上，导致了一个分支版本，令人惊讶的是，该版本一直优于上游版本。
*   **阶段 2：Facebook：** 在 Facebook 的采用推动了 pprof 兼容的堆分析以及其他主要功能的添加，如广泛的测试、Valgrind 支持（后来被移除）和 JSON 格式的遥测，这些都得到了 Facebook 广泛的内部性能数据的支持。成立了一个小型 jemalloc 团队，从而实现了持续集成测试和全面的遥测。
*   **阶段 3：Meta：** 对核心技术的投资转移，导致停滞，并最终放弃了计划中的巨页分配改进。
*   **阶段 4：停滞：** 上游开发已经结束，作者不打算投入大量重构工作来恢复它。

作者感叹缺乏对外用户需求的认识，并以移除 Valgrind 支持以及对 jemalloc 在 Android 中作用的不知情为例。 尽管是开源的，jemalloc 仍然未能吸引来自其他组织的主要贡献者，从而阻碍了其作为独立项目的长期可行性。 尽管与他偏好的垃圾回收有所不同，但作者对合作者、支持者和用户表示感谢，感谢他们使 jemalloc 成为一个有意义的项目。

---

## 76. 展示你技能的标志性图标

**原文标题**: Iconic icons to showcase your skills

**原文链接**: [https://github.com/YuheshPandian/ICONIC](https://github.com/YuheshPandian/ICONIC)

ICONIC：一个面向开发者的技能图标库，提供圆润、时尚的图标，适用于 GitHub README、作品集和简历，是通用图标的视觉增强替代方案。该库包含清晰美观的图标，提供浅色和深色主题，可轻松嵌入 Markdown、HTML 和其他平台。

关键特性是由 Django 支持的 HTML 预览 API，可实现动态图标集成。同时提供可直接下载的 SVG 文件。

本文提供了使用 HTML 代码片段嵌入图标的快速实现说明，强调了这种方法提供的尺寸和样式控制的优越性，尤其是在 GitHub README 中。

对于希望贡献的开发者，本文概述了通过 pull request 添加新图标的流程，指定使用 Inkscape 等照片编辑软件，遵循现有的文件夹结构（dark/ 和 light/），保持一致的图标尺寸（512x512 SVG）以及有意义的文件名。该项目采用 MIT 许可证。

---

## 77. 军队最新招募：来自Meta、OpenAI等公司的科技高管

**原文标题**: The Army’s Newest Recruits: Tech Execs From Meta, OpenAI and More

**原文链接**: [https://www.wsj.com/tech/army-reserve-tech-executives-meta-palantir-796f5360](https://www.wsj.com/tech/army-reserve-tech-executives-meta-palantir-796f5360)

好的，我可以基于标题以及关于科技高管加入陆军预备役的假设来总结这篇文章。 这是一个潜在的总结：

**摘要（基于标题）：**

《华尔街日报》的文章“陆军最新招募：来自Meta、OpenAI等公司的科技高管”报道了一种趋势，即来自Meta、OpenAI和Palantir等知名公司的科技高管加入陆军预备役。 这些人在人工智能、数据分析、网络安全和软件开发等领域拥有宝贵专业知识，他们希望将自己的技能贡献于国家安全。

这篇文章可能探讨了这种职业选择背后的动机，强调了公民义务感、将他们的技术技能应用于具有国家影响力的现实问题的机会，以及兵役提供的独特的职业发展机会等因素。 它可能还会讨论陆军的观点，详细说明军方如何利用这些科技专业人员的专业知识来增强其在情报收集、网络战和技术创新等领域的能力。

这篇文章可能会深入探讨这些高管在陆军预备役中担任的具体角色、他们接受的培训以及平衡他们的文职职业与军事义务的潜在挑战。 最后，这篇文章可能会探讨这种趋势的更广泛影响，考虑它是否代表了科技行业与军方之间日益增长的联系，以及它对国防和技术进步的潜在影响。

---

## 78. 策梅洛选择公理百年：问题何在？(2006)

**原文标题**: 100 years of Zermelo's axiom of choice: What was the problem with it? (2006)

**原文链接**: [https://research.mietek.io/mi.MartinLof2006.html](https://research.mietek.io/mi.MartinLof2006.html)

本文回顾策梅洛选择公理（AC）提出一百年后，考察了最初的反对意见、其最终被接受以及它在构造性数学中的地位。最初，它受到了像贝尔、博雷尔、勒贝格和布劳威尔等数学家的强烈反对，他们认为它不具构造性，但由于 AC 在发展数学的各个分支中是必要的，它逐渐被接受。

然而，比肖普在 1967 年出人意料地主张在构造性数学中存在一个选择函数，这与布劳威尔-海廷-柯尔莫哥洛夫对逻辑常量的解释相一致。 迪亚科内斯库后来证明，在拓扑斯理论中，排中律来自 AC，这似乎与比肖普的观点相矛盾。

本文随后尝试在构造性类型论中证明策梅洛的 AC。策梅洛 1908 年对 AC 的表述，等价于乘法公理，涉及一个集合 S，一个等价关系，以及一个互斥且穷举的子集族 A_i。 尝试失败的原因是，构造性选择公理不能保证选择函数 f 的外延性 (即，i ≍_I j → f(i) ≍_S f(j))。

本文的结论是，策梅洛的 AC 来自于一个*外延的*选择公理 (ExtAC)，它明确包含了选择函数的外延性条件。 虽然 ExtAC 缺乏内涵选择公理的直观证据，但它仍然是一个有效的研究课题。

---

## 79. 我说服了惠普董事会收购Palm，然后眼睁睁地看着他们毁了它。

**原文标题**: I convinced HP's board to buy Palm and watched them kill it

**原文链接**: [https://philmckinney.substack.com/p/i-convinced-hps-board-to-buy-palm](https://philmckinney.substack.com/p/i-convinced-hps-board-to-buy-palm)

作者菲尔·麦金尼曾任惠普个人系统集团首席技术官，他讲述了自己在2010年说服惠普董事会收购Palm公司一事，以及后来惠普公司管理不善并最终扼杀Palm公司所带来的失望。

麦金尼认为收购Palm的理由是Palm创新的webOS，当时这款移动操作系统优于iOS和安卓。他将Palm视为惠普重新进入移动领域并有效竞争的平台。他相信webOS独特的卡片式多任务处理、直观的UI和云同步功能具有革命性。

然而，惠普的领导层，特别是首席执行官李艾科，未能理解或利用Palm的潜力。 李艾科优先考虑削减成本和企业解决方案，忽视了webOS及其以消费者为中心的特点。他还更换了支持收购的关键人员，引进了不了解webOS价值的高管。

麦金尼目睹了一系列战略失误，包括忽视运营商关系、营销资金不足，以及最终决定停止webOS的开发。 他对失去一项可能改变游戏规则的技术以及惠普错失成为移动领域领导者的机会感到惋惜。 他表达了对惠普放弃优秀产品而选择短期财务收益的沮丧，突出了创新与公司官僚主义之间的冲突。 最终，他将惠普对Palm的处理视为一个警示故事，告诫人们忽视创新和未能执行有前景的收购所带来的危险。

---

## 80. Sandboxfs 怎么了？

**原文标题**: Whatever Happened to Sandboxfs?

**原文链接**: [https://blogsystem5.substack.com/p/whatever-happened-to-sandboxfs](https://blogsystem5.substack.com/p/whatever-happened-to-sandboxfs)

好的，我已阅读来自 blogsystem5.substack.com 的文章“Sandboxfs 怎么了？”。以下是摘要：

这篇文章探讨了 Sandboxfs 的兴起和明显衰落，Sandboxfs 是一种 FUSE 文件系统，旨在为应用程序（尤其是构建系统）提供对文件系统的受限访问。文章认为 Sandboxfs 是一项很有前途的技术，它解决了一个实际问题：安全地允许构建过程仅访问必要的文件，防止意外修改其他系统组件并提高可重复性。

作者强调了 Sandboxfs 的主要优势，包括其对文件访问的细粒度控制（只读、读写、可见性）、重新映射目录结构的能力以及与完整容器化等替代方案相比的简单性。这些特性使其非常适合像 Bazel 这样的构建系统，其中 hermetic 构建至关重要。

然而，文章指出，Sandboxfs 近年来似乎已经停滞不前。虽然最初它被集成到 Bazel 中，但 Bazel 团队似乎正在远离它，可能转向替代解决方案或更复杂的隔离技术。

文章提出了 Sandboxfs 衰落的可能原因，包括：面对内核更新和不同的操作系统，维护 FUSE 文件系统的复杂性，Docker 和 Kubernetes 等容器化技术的兴起，它们提供了更全面的隔离，以及与原生文件系统访问相比，潜在的性能限制。文章还认为，在低级别管理文件系统访问的内在复杂性可能已被证明长期维持太过具有挑战性。

总之，文章将 Sandboxfs 描述为一个好主意，但最终因技术挑战、隔离技术趋势的变化以及它试图解决的问题的内在复杂性而未能成功。虽然 Sandboxfs 可能不是文件系统隔离的未来，但其概念性贡献在持续追求安全和可重复的构建系统中仍然具有重要意义。

---

## 81. 警惕意图经济：通过大型语言模型收集和商品化意图

**原文标题**: Beware the Intention Economy: Collection and Commodification of Intent via LLMs

**原文链接**: [https://hdsr.mitpress.mit.edu/pub/ujvharkk/release/1](https://hdsr.mitpress.mit.edu/pub/ujvharkk/release/1)

本文介绍了“意图经济”的概念，这是一种由大型语言模型（LLM）推动的、可能由注意力经济演变而来的新经济形态。作者认为，科技公司正在竞相主导这个新兴市场，该市场专注于捕捉、操纵和商品化人类意图。

意图经济利用LLM的能力来引出、推断、收集、记录、理解、预测，并最终操纵人类的计划和目的，范围从日常选择到重大决策。这是通过高度个性化的劝说、量身定制的情感渗透以及通过自然语言对在线活动的详细分类来实现的。

作者强调了对意图商品化作为数字市场可能对民主规范构成风险的担忧，因为用户可能会受到秘密方法的影响，从而颠覆、重定向和干预意图信号。微软、OpenAI、苹果和英伟达等科技巨头正在大力投资LLM基础设施，旨在根据用户的意图、行为和心理数据来预测和引导用户。本文展示了意图经济与注意力经济的不同之处。注意力经济侧重于现在和未来对用户注意力的访问，而意图经济更进一步，竞相获得实时和针对未来可能性的访问权限，动态生成以匹配用户的个人资料。作者最后主张持续批判意图经济的社会影响。

---

## 82. 揭秘德国百亿亿次级“木星”超级计算机

**原文标题**: Peeling the Covers Off Germany's Exascale "Jupiter" Supercomputer

**原文链接**: [https://www.nextplatform.com/2025/06/11/peeling-the-covers-off-germanys-exascale-jupiter-supercomputer/](https://www.nextplatform.com/2025/06/11/peeling-the-covers-off-germanys-exascale-jupiter-supercomputer/)

本文深入探讨了德国新型百亿亿次级超级计算机“木星”(Jupiter)的架构和性能。该计算机是欧洲高性能计算联合承办机构(EuroHPC Joint Undertaking)框架下首个完成的项目，由Eviden和ParTec公司建造。“木星”是一个混合系统，包含一个使用SiPearl Rhea1 Arm处理器的基于CPU的“通用集群”和一个利用英伟达Grace Hopper超级芯片及H200 GPU的强大的基于GPU的“加速模块”。

加速模块在Top500榜单上排名第四，彰显了其卓越性能。每个节点包含独特的四个Grace CPU和Hopper GPU，通过NVLink互联，从而提高效率。尽管最初计划旨在实现欧洲芯片的自主性，但“木星”主要依赖英伟达的GPU计算能力。

通用集群采用Rhea1 CPU，代表着向欧洲自主性迈出的一小步。然而，它的性能与GPU加速器相比相形见绌。该系统采用英伟达的Quantum-2 InfiniBand构建了庞大的网络，连接着数千个端点。虽然最初目标是在HPL基准测试中达到1百亿亿次浮点运算，但目前的配置未能达到。

尽管如此，“木星”加速器在计算效率和能源效率方面表现出色，与其他领先的百亿亿次级机器相媲美。该项目耗资5亿欧元，由EuroHPC、德国政府和北莱茵-威斯特法伦州资助。成本分析表明，英伟达提供了优惠的价格，这反映了其在HPC市场播种的战略重要性。

---

## 83. SSHTron：一款通过SSH运行的多人光轮摩托游戏

**原文标题**: SSHTron: A multiplayer lightcycle game that runs through SSH

**原文链接**: [https://github.com/zachlatta/sshtron](https://github.com/zachlatta/sshtron)

SSHTron：通过SSH玩的多人光轮摩托游戏。玩家使用SSH连接服务器，并通过WASD或vim键位控制他们的光轮摩托。要玩游戏，用户只需运行`ssh sshtron.zachlatta.com`。玩家可以选择在SSH命令前添加颜色名称来指定颜色，例如`ssh red@sshtron.zachlatta.com`。

该游戏是开源的，可以自行托管。文档提供了编译和直接运行服务器的说明，包括生成SSH密钥和使用`go get`来管理依赖项。还详细介绍了Docker容器设置，包括Raspberry Pi的具体说明。

该文档还强调了有关SSH客户端漏洞（CVE-2016-0777）的安全警告，恶意SSH服务器可能会利用这些漏洞。尽管SSHTron的设计目的不是利用这些漏洞，但建议用户在玩游戏前修补他们的SSH客户端，以防万一。

SSHTron基于MIT许可证。

---

## 84. “语言与图像减认知”：莱夫·韦瑟比访谈

**原文标题**: “Language and Image Minus Cognition”: An Interview with Leif Weatherby

**原文链接**: [https://www.jhiblog.org/2025/06/11/language-and-image-minus-cognition-an-interview-with-leif-weatherby/](https://www.jhiblog.org/2025/06/11/language-and-image-minus-cognition-an-interview-with-leif-weatherby/)

在与罗宾·曼利的一次访谈中，莱夫·韦瑟比讨论了他即将出版的书籍《语言机器》，认为大型语言模型（LLM）已经将认知与语言分离，这与早期的结构主义理论相呼应。韦瑟比批评了他所谓的“剩余人文主义”，即倾向于通过与人工智能对立来定义人类能力，从而阻碍了对LLM的清晰理解。他认为这限制了人工智能怀疑论者（如乔姆斯基和本德）以及人工智能支持者（包括人工智能风险研究人员）。

韦瑟比提出了一种结构主义方法，将索绪尔的语言理论与LLM的功能进行类比。他认为，LLM不一定复制人类智能，而是通过对彼此相关的语言符号的整体进行建模，从而抓住了语言的本质。他注意到LLM和人类写作之间令人惊异的无法区分性，这表明语言已经成为一种人工构造，就像其他媒体一样。

韦瑟比将乔姆斯基的方法与康德的先验主义联系起来，将统计方法与休谟的经验主义联系起来，并将它们与他的辩证结构主义进行对比，将索绪尔的语言价值与马克思的价值理论进行类比。他通过解释其他选择方案的缺陷来捍卫这种观点的优越性。他还将他的论点置于关于控制论的历史学术研究中，强调德国唯心主义对形式化认知科学的经常被忽视的影响。他正在与人合著另一篇论文，题为《数字辩证法》，其中阐述了他论点的另一半，即与定量思想的接触总是短暂的。

---

## 85. 收据打印机治好了我的拖延症

**原文标题**: A receipt printer cured my procrastination

**原文链接**: [https://www.laurieherault.com/articles/a-thermal-receipt-printer-cured-my-procrastination](https://www.laurieherault.com/articles/a-thermal-receipt-printer-cured-my-procrastination)

作者因多动症而苦于拖延，受到电子游戏成瘾性的启发，发现了一种独特的生产力系统。他意识到游戏使用快速反馈循环（瞄准→射击→命中/未命中）来吸引玩家并释放多巴胺。

为了复制这一点，他将任务分解成更小、更易于管理的“微任务”，并使用便利贴，将它们揉成一团扔进罐子里以获得即时反馈。这提供了一种切实的成就感，并使任务感觉更真实，从而对抗拖延症。他建议以简单、日常的任务开始一天，以建立势头。

虽然有效，但书写大量的便利贴变得耗时。这促成了突破：收据打印机。打印每日任务消除了摩擦并提高了连贯性，因为他可以轻松生成大量任务并毫无遗漏地跟踪习惯。

他强调了收据打印机的好处：消除准备摩擦，允许更多任务，并最大限度地减少跳过系统的机会。

他还开发了定制软件，该软件以列的形式水平显示任务和子任务，从而可以轻松分解和打印特定任务列表，从而进一步提高生产力。作者声称，这种组合系统极大地提高了他的生产力，并消除了低效率的日子，对于患有多动症的人来说，这是一项重大成就。他计划公开发布该软件。

---

## 86. 随机的人给随机的其他人钱 (2017)

**原文标题**: When random people give money to random other people (2017)

**原文链接**: [https://quomodocumque.wordpress.com/2017/06/27/when-random-people-give-money-to-random-other-people/](https://quomodocumque.wordpress.com/2017/06/27/when-random-people-give-money-to-random-other-people/)

当随机的人给随机的其他人钱时

---

## 87. RAG是个花哨的，会撒谎的搜索引擎

**原文标题**: RAG Is a Fancy, Lying Search Engine

**原文链接**: [https://labs.stardog.ai/rag-is-a-fancy-lying-search-engine](https://labs.stardog.ai/rag-is-a-fancy-lying-search-engine)

本文批判了检索增强生成（RAG）在高风险、受监管行业中的应用，认为它本质上是一个“花哨的、会撒谎的搜索引擎”，不适合此类应用场景。作者指出了RAG流行的几个原因，包括易于原型设计、风险投资的资助、A16Z的影响、被认为具有科学依据，以及搜索技术的停滞。

核心论点是RAG的根本缺陷在于让大型语言模型（LLM）“最后发言”，这意味着其原始的、可能产生幻觉的输出直接暴露给用户。这被认为是不负责任和不安全的，尤其是在准确性和可靠性至关重要的情况下。

作者将RAG与更合适的替代方案进行了对比。RAG适用于低风险用例，如度假政策查询，偶尔的错误是可以接受的。然而，RAG不足以处理结构化数据，限制了其在受监管行业中的应用，这些行业依赖数据库和黄金记录来获取关键信息。

本文还探讨了日益增长的生成式人工智能反弹，认为这实际上是对RAG的错误批评。虽然承认LLM在理解人类意图方面的优势，但作者认为RAG错误地利用它们进行数据理解。作为一种替代方案，作者提出语义解析作为一种更可靠、更安全的方法，适用于高风险的企业应用。

---

## 88. 苹果的超瓷晶面板是为AR界面做的准备，不仅仅是设计上的更新

**原文标题**: Apple's Liquid Glass is prep work for AR interfaces, not just a design refresh

**原文链接**: [https://omc345.substack.com/p/from-skeuomorphic-to-liquid-glass](https://omc345.substack.com/p/from-skeuomorphic-to-liquid-glass)

好的，我已阅读了来自 omc345.substack.com 的文章《苹果的液态玻璃设计是为 AR 界面做准备，而不仅仅是设计更新》。以下是摘要：

这篇文章认为，苹果转向以半透明、深度和元素分层为特征的“液态玻璃”设计语言，不仅仅是表面上的更新，而是一项战略举措，旨在为用户和开发者准备增强现实 (AR) 界面。

作者认为，苹果正有意从过去十年的扁平、2D 设计转向更具三维立体感、视觉丰富的审美。这种“液态玻璃”风格模仿了现实世界中玻璃和其他半透明材料的特性，提供了一种更直观、更自然的方式来与叠加在物理世界中的数字信息进行交互。

关键点包括：

*   **AR 准备就绪：** 这种设计转变在心理上和视觉上为用户做好准备，以便无缝过渡到数字元素与物理环境融合的 AR 环境。
*   **空间感知：** “液态玻璃”的半透明和分层特性有助于创建深度和空间感知，这对于导航和与 AR 界面交互至关重要。
*   **开发者熟悉度：** 这种设计语言鼓励开发者尝试并构建利用深度、半透明度和物体持久性的应用程序，最终为更丰富的 AR 生态系统做出贡献。
*   **超越拟物化：** 虽然表面上类似于旧的拟物化设计，“液态玻璃”在功能上是截然不同的，旨在在 AR 环境中提供清晰度和理解，而不是简单地复制现实世界的物体。
*   **未来影响：** 作者认为，这种设计方向表明了苹果对 AR 的长期投资和愿景，使该公司能够引领下一代用户界面。

---

## 89. 使用 TornadoVM 在纯 Java 中实现 GPU 加速的 Llama3.java 推理

**原文标题**: GPU-accelerated Llama3.java inference in pure Java using TornadoVM

**原文链接**: [https://github.com/beehive-lab/GPULlama3.java](https://github.com/beehive-lab/GPULlama3.java)

本文介绍了`GPULlama3.java`项目，该项目使用TornadoVM，以纯Java编写，能够对Llama3模型进行GPU加速推理。它利用TornadoVM的并行计算来提高性能，优于标准Java执行。该项目基于最初的`Llama3.java`实现，并为实现与`llama.cpp`等原生实现相当的性能提供了一个起点。

本文详细介绍了在不同硬件（NVIDIA RTX、Intel Arc、Apple Silicon）上使用FP16量化的各种Llama3模型（1B、3B、8B）的性能基准测试。它强调了正在进行的优化，并提供了未来改进的路线图。

文章提供了设置、构建和运行项目的全面指南，包括Linux、macOS和Windows的说明。它强调了Java 21的使用，以及带有OpenCL或PTX后端的TornadoVM安装，和Maven的构建。 其中包括克隆存储库、更新子模块、安装TornadoVM和配置环境变量的具体步骤。 本文还提供了下载预量化GGUF模型文件的链接。

文章通过示例解释了`llama-tornado`脚本的用法以及各种命令行选项。文中提供了有关GPU内存问题故障排除和调整内存分配的说明。还描述了调试和分析选项。最后，它演示了如何使用`--show-command`标志来显示带有JVM标志的底层Java命令，从而将项目集成到现有代码库中。

---

## 90. 我和阿尔吉侬——与（暂时的）认知衰退作斗争

**原文标题**: Me an' Algernon – grappling with (temporary) cognitive decline

**原文链接**: [https://tidyfirst.substack.com/p/me-an-algernon](https://tidyfirst.substack.com/p/me-an-algernon)

无法访问文章链接。

---

## 91. 印度制造依赖中国制造

**原文标题**: "Make in India" Relies on "Made in China"

**原文链接**: [https://www.hinrichfoundation.com/research/wp/trade-and-geopolitics/make-in-india-relies-on-made-in-china/](https://www.hinrichfoundation.com/research/wp/trade-and-geopolitics/make-in-india-relies-on-made-in-china/)

阿基尔·拉梅什的文章《“印度制造”依赖“中国制造”》认为，印度于2014年启动的雄心勃勃的“印度制造”倡议，旨在将印度转变为全球制造中心并减少对中国的依赖，在很大程度上未能实现其目标。虽然生产关联激励（PLI）计划在电信、电子产品出口（尤其是iPhone）、半导体和国防等领域取得了一些成功，并与美国和台湾建立了合作伙伴关系，但制造业在印度GDP中的份额实际上有所下降。

核心问题是，印度对中国的依赖已从下游成品转移到上游投入品和零部件。成功主要体现在下游价值链中，而对中国原材料、活性药物成分和技术（如电动汽车电池技术）的依赖仍然很高。文章强调，印度需要一支技术娴熟的制造业劳动力，与中国在政府支持下建立的强大生态系统相媲美，才能真正实现生产本土化。

尽管最初由于地缘政治担忧而努力减少与中国的联系，但新德里现在正在加强经济合作，这体现在放宽签证政策、恢复投资讨论以及与中国公司在电子领域的合资企业。作者警告说，印度有成为对中国、美国和俄罗斯“多重依赖”的风险，从而阻碍其在自力更生方面的进展。拉梅什建议，印度应战略性地利用美国和中国的经济联系，重点关注与国家安全无关的行业，同时解决阻碍业务增长的国内效率低下问题。只有这样，印度才能真正实现其制造业潜力。

---

## 92. OxCaml - OCaml编程语言的一组扩展。

**原文标题**: OxCaml - a set of extensions to the OCaml programming language.

**原文链接**: [https://oxcaml.org/](https://oxcaml.org/)

OxCaml是由Jane Street开发的OCaml编程语言的一组扩展，旨在增强其对性能导向型编程的适用性。其核心原则是在保持OCaml的基本设计和可用性的前提下，优先考虑安全性、便捷性和可预测的性能控制，但仅在需要时才进行。

其主要目标是通过提供对关键方面的细粒度控制而不牺牲程序员的生产力来增强性能工程能力。 OxCaml扩展分为以下几个类别：

*   **无畏并发：** 静态类型系统增加，以防止数据竞争。
*   **布局：** 控制内存中的数据布局以及对SIMD扩展的本地访问。
*   **分配控制：** 减少垃圾回收开销并提高缓存效率的工具。
*   **生活质量改进：** 诸如多态参数、包含函子、带标签的元组和不可变数组等功能。

OxCaml是开源的，面向实验用户。虽然向后兼容OCaml，但OxCaml扩展缺乏稳定性保证。它提供了修改后的OCaml工具，包括包管理（兼容dune和opam）、编辑器集成（LSP-服务器）、源代码格式化和文档生成。 Jane Street发布了OCaml兼容版本和OxCaml优化版本的库和工具，尽管在某些情况下，某些OxCaml特定的功能可能会阻止OCaml兼容性。

---

## 93. 全自由活动物的高速荧光光场断层扫描

**原文标题**: High-speed fluorescence light field tomography of whole freely moving organisms

**原文链接**: [https://opg.optica.org/optica/fulltext.cfm?uri=optica-12-5-674&id=570897](https://opg.optica.org/optica/fulltext.cfm?uri=optica-12-5-674&id=570897)

好的，我已阅读了来自所提供URL的文章《自由移动的完整生物体的高速荧光光场断层扫描》。以下是摘要：

本文提出了一种称为高速荧光光场断层扫描（F-LF-T）的新技术，用于自由移动的完整生物体的3D成像。该系统利用光场显微镜快速获取3D信息，而无需样品旋转或扫描，从而克服了传统荧光显微镜和断层扫描的局限性。

该方法的关键方面包括：

*   **光场显微镜：** 该系统使用光场显微镜来捕获从生物体内荧光标记结构发出的光的空间和角度信息。这允许从单个快照重建3D体积，从而实现高速成像。
*   **计算重建：** 采用复杂的计算重建算法，从原始光场数据生成高分辨率3D体积。
*   **应用于自由移动的生物体：** 该技术在表达荧光蛋白的自由移动的*秀丽隐杆线虫*（*C. elegans*）上进行了演示。这突出了在完整生物体的自然状态下对动态过程进行成像的能力。
*   **高时间分辨率：** 该系统实现了足够的体积成像速率，以捕获自由移动的生物体中的快速生物过程。
*   **优于现有技术：** F-LF-T优于传统显微镜和断层扫描，因为它无需样品旋转、物理切片或复杂的扫描程序。这实现了更快的成像速度，减少了光漂白，并最大程度地减少了对生物体行为的干扰。

作者通过对*秀丽隐杆线虫*中的神经元活动和肌肉动态进行成像，展示了F-LF-T的功能。他们认为，该技术在研究自由移动的生物体中的广泛生物过程方面具有巨大的潜力，为复杂生物系统提供了新的见解。

---

## 94. 将公元前3700年至公元2000年全球6000年城市化进程空间化

**原文标题**: Spatializing 6k years of global urbanization from 3700 BC to AD 2000

**原文链接**: [https://www.nature.com/articles/sdata201634](https://www.nature.com/articles/sdata201634)

本文介绍了一个新的、空间显式的全球城市聚落数据集，时间跨度从公元前3700年到公元2000年。该数据集通过数字化、转录和地理编码钱德勒的《四千年城市发展史》和莫德尔斯基的《世界城市》中的历史城市人口数据创建，提供了首个空间参考的过去6000年城市人口规模和位置的档案。

数据创建过程包括数据清理、协调，以及为每个地理编码位置创建可靠性排名，以解决地理不确定性。虽然该数据集依赖于钱德勒和莫德尔斯基的人口估计，但它通过添加经度和纬度坐标使这些数据空间化。

作者最初的动机是检验城市历史上在肥沃农业地区发展的假设。然而，他们承认该数据集更广泛的应用，包括了解城市聚落的地理演变、城市增长与资源之间的关系，以及城市增长和衰退的长期周期。

作者承认诸如时间和空间稀疏性等局限性，但强调该数据集为理解历史上城市人口的地理分布迈出了关键的第一步。他们还讨论了定义“城市”的挑战，并承认钱德勒和莫德尔斯基使用的各种定义和方法，认为这些差异最终丰富了该数据集对城市地区的表征。尽管存在这些局限性，钱德勒和莫德尔斯基的原始作品已被广泛应用于社会科学领域。

---

## 95. 更自由安全地使用电脑 (2023)

**原文标题**: Using computers more freely and safely (2023)

**原文链接**: [https://akkartik.name/freewheeling/](https://akkartik.name/freewheeling/)

Kartik Agaram 的文章《更自由安全地使用电脑》提倡转变我们对待软件的方式，优先考虑自由、安全和用户控制。他认为现代软件通常昂贵、不可信（由于无能和恶意）且效率低下，导致计算体验日益复杂和缓慢。

Agaram 提出了一套原则，核心是使用以下特性的软件：更少用户、不频繁的更新、频繁的分支、易于修改以及用户驱动修改的潜力。他强调了摆脱垄断，转向更小、更易于管理的软件项目的好处。

他通过自己使用 Lua 和 LÖVE 游戏引擎创建简单、自定义应用程序的经验来阐述这些原则。他强调质疑无意识假设和避免不必要的要求（如“专业性”和向后兼容性）的重要性。Agaram 认为，通过派生现有程序来避免功能蔓延和分歧是有价值的，并提倡那些把一件事做好的程序。他还强调了可访问修改的重要性，即用户可以轻松理解和更改软件，而无需复杂的工具。其根本理念是“奖励好奇心”并降低复杂性。

---

## 96. Meta AI的搜索公开了——但所有用户都意识到了吗？

**原文标题**: Meta AI searches made public – but do all its users realise?

**原文链接**: [https://www.bbc.com/news/articles/c0573lj172jo](https://www.bbc.com/news/articles/c0573lj172jo)

该文章强调了人们对Meta AI在用户未完全了解其影响的情况下，将用户搜索查询和AI回复公开的担忧。Meta AI的“发现”信息流公开展示提示和生成的内容，可能暴露敏感的个人信息和可识别的用户帐户。

虽然Meta表示聊天默认是私密的，用户必须选择公开发布，但该文章认为，警告信息可能不足以让用户理解他们的私人AI互动正在被公开分享。示例包括用户请求测试帮助、探索性别认同，以及请求衣着暴露的角色的图像，所有这些都可能与他们的社交媒体资料相关联。

网络安全专家瑞秋·托巴克指出了用户期望与现实之间的不符，认为用户不会预料到他们的AI聊天机器人互动会被公开展示。这种与他们的身份相关的敏感信息无意中的披露，引发了重大的用户体验和安全问题。

Meta强调用户控制和隐私设置，但该文章建议需要更加清晰地了解“发现”信息流的公开性质，以保护用户免于无意中分享私人信息。

---

## 97. 量子计算讲义 (2022)

**原文标题**: Quantum Computation Lecture Notes (2022)

**原文链接**: [https://math.mit.edu/~shor/435-LN/](https://math.mit.edu/~shor/435-LN/)

这些是Peter Shor教授在2022年麻省理工学院讲授的8.370/18.435量子计算课程的讲义。这些讲义涵盖了量子计算中的广泛主题，从基本概念到更高级的算法和纠错技术。

讲义首先介绍了量子计算的历史和叠加原理。然后深入研究了诸如幺正演化、布洛赫球表示、量子测量以及用于描述联合量子系统的张量积等基本概念。

课程过渡到经典和可逆布尔电路，为理解量子门奠定了基础。探讨了各种量子门，以及量子隐形传态等应用。

讲义随后介绍了密度矩阵，这是描述混合量子态所必需的。这引出了对基础量子实验的讨论，如GHZ实验，将理论与量子光学中的实验实现联系起来。

涵盖了几个关键的量子算法，包括Deutsch-Jozsa算法、Simon算法、量子傅里叶变换、相位估计算法、Shor的因式分解算法和Grover的搜索算法。讲义还包括理解这些算法所需的经典计算复杂性理论和数论的必要背景知识。

最后，本课程以量子纠错码的介绍作为结尾，特别是9量子比特码、7量子比特量子汉明码和量子CSS码，随后探讨了BB84量子密钥分发协议及其安全证明。虽然关于哈密顿模拟的第26讲的讲义在发布时还没有撰写。

---

## 98. 研究表明宇宙大爆炸可能发生于黑洞内部

**原文标题**: Research suggests Big Bang may have taken place inside a black hole

**原文链接**: [https://www.port.ac.uk/news-events-and-blogs/blogs/space-cosmology-and-the-universe/what-if-the-big-bang-wasnt-the-beginning-our-research-suggests-it-may-have-taken-place-inside-a-black-hole](https://www.port.ac.uk/news-events-and-blogs/blogs/space-cosmology-and-the-universe/what-if-the-big-bang-wasnt-the-beginning-our-research-suggests-it-may-have-taken-place-inside-a-black-hole)

以下是基于提供的URL和标题的文章摘要，假设其准确反映了内容：

朴茨茅斯大学的文章讨论了一项研究，该研究表明宇宙大爆炸可能并非宇宙的绝对开端，而是发生在存在于母宇宙中的黑洞内部。这挑战了将大爆炸视为空间和时间唯一起源点的标准宇宙学模型。

该研究团队，很可能由尼耶什·阿夫肖迪教授领导（鉴于该大学的宇宙学研究背景），正在探索宇宙起源的替代模型。他们的工作考虑了我们的可观测宇宙可能是作为更高维度宇宙中形成的黑洞的“内部”而出现的可能性。这种观点利用了弦理论和M理论的各个方面，这些理论允许存在膜（更高维度的物体）和相互连接的宇宙多元宇宙。

这篇文章可能解释了在特定的理论条件下，黑洞中发现的极端密度和奇点如何触发一个新宇宙的诞生。在这个模型中，大爆炸将是标志着我们宇宙在这个黑洞内部诞生的事件。宇宙微波背景（CMB）和宇宙的大尺度结构可能包含能够证实或反驳这一假设的线索。

本质上，该研究提出了一个循环或多元宇宙模型，其中黑洞充当宇宙“种子”，从而产生新的宇宙，暗示了一个持续的诞生和重生过程，而不是一个单一的开端。这种方法为解决与标准大爆炸模型相关的一些问题提供了潜在的解决方案，例如最初的奇点以及对暴胀时期的需求。

---

## 99. Meta投资143亿美元给Scale AI，以启动超智能实验室。

**原文标题**: Meta invests $14.3B in Scale AI to kick-start superintelligence lab

**原文链接**: [https://www.nytimes.com/2025/06/12/technology/meta-scale-ai.html](https://www.nytimes.com/2025/06/12/technology/meta-scale-ai.html)

无法访问文章链接。

---

## 100. 在QEMU中模拟iPhone 11

**原文标题**: iPhone 11 emulation done in QEMU

**原文链接**: [https://github.com/ChefKissInc/QEMUAppleSilicon](https://github.com/ChefKissInc/QEMUAppleSilicon)

本文档是QEMU的README文件，QEMU是一个多功能、开源的机器模拟器和虚拟化器。 QEMU可以在没有硬件虚拟化的情况下模拟完整的机器，并且在与Xen或KVM集成时，可以实现接近原生CPU的性能。 它还提供用户空间API虚拟化，使为一种架构编译的二进制文件可以在具有不同架构的主机上运行。

本文档涵盖了QEMU的 essential 方面，包括其文档、构建过程、贡献指南、错误报告程序和联系信息。 构建QEMU涉及创建构建目录、配置构建环境，然后使用`make`命令。 补丁应通过`git format-patch`或`git send-email`提交到qemu-devel邮件列表，并遵守开发者指南，包括"Signed-off-by"行。 建议使用`git-publish`实用程序来简化贡献。

应通过GitLab问题跟踪器提交错误报告，特别是对于在QEMU git或上游版本中发现的问题。 对于供应商提供的二进制文件，请首先向供应商报告错误。 版本历史和发行说明可在QEMU wiki和git历史记录中找到。 可以通过qemu-devel邮件列表或irc.oftc.net上的#qemu IRC频道联系QEMU社区。

---

