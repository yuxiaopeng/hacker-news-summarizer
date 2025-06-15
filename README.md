# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-06-15.md)

*最后自动更新时间: 2025-06-15 17:48:48*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 2 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 3 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 4 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 5 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 6 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 7 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 8 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 9 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 10 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 11 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 12 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 13 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 14 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 15 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 16 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 17 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 18 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 19 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 20 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 21 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 22 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 23 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 24 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 25 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 26 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 27 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 28 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 29 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 30 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 31 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 32 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 33 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 34 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 35 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 36 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 37 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 38 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 39 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 40 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 41 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 42 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 43 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 44 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 45 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 46 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 47 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 48 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 49 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 50 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 51 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 52 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 53 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 54 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 55 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 56 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 57 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 58 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 59 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 60 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 61 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 62 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 63 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 64 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 65 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 66 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 67 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 68 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 69 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 70 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 71 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 72 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 73 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 74 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 75 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 76 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 77 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 78 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 79 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 80 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 81 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 82 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 83 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 84 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 85 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 86 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 87 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 88 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
