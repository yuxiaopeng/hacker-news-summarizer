# Hacker News 热门文章摘要 (2025-09-19)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 我后悔搭建了这个价值3000美元的树莓派AI集群。

**原文标题**: I regret building this $3000 Pi AI cluster

**原文链接**: [https://www.jeffgeerling.com/blog/2025/i-regret-building-3000-pi-ai-cluster](https://www.jeffgeerling.com/blog/2025/i-regret-building-3000-pi-ai-cluster)

杰夫·吉尔林搭建了一个价值3000美元的树莓派5计算刀片集群，包含10个节点，每个节点配备一个16GB CM5 Lite模块，旨在探索其在HPC和AI任务中的可行性。经过两年的等待，并因不可靠的固态硬盘和散热问题多次重建后，他使用高性能Linpack（HPL）和AI推理基准测试了集群的性能。

该集群在HPL测试中达到了325 Gflops，比单个CM5提升了10倍。虽然比他价值8000美元的Framework桌面集群更节能，但对于HPC而言，速度明显更慢且成本效益更低。

在AI方面，该集群表现不佳。在单个Pi上运行Llama 3.2:3B产生了每秒6个token，与Intel N100相比表现较弱。使用llama.cpp RPC在多个Pi上运行Llama 3.3:70B导致速度极慢，仅为每秒0.28个token。使用分布式llama将性能提升到8个节点上每秒0.85个token，但仍然比Framework集群慢得多且更不稳定。

吉尔林总结说，虽然该集群高效、安静且紧凑，但其性能并非强大，对于大多数用户来说也不是最佳选择。他认为其可能适用于CI作业或高安全性边缘部署等小众用例。他指出，Unredacted Labs使用Pi集群作为Tor出口中继，因为它们效率高且节点密度大。尽管性能不尽如人意，但吉尔林打算继续探索该集群的潜力，受到加州大学圣巴巴拉分校更大的Pi集群的启发。

---

## 2. 蚂蚁似乎违背生物学规律：它们产下的卵孵化成另一种物种

**原文标题**: Ants Seem to Defy Biology: They Lay Eggs That Hatch into Another Species

**原文链接**: [https://www.smithsonianmag.com/smart-news/these-ant-queens-seem-to-defy-biology-they-lay-eggs-that-hatch-into-another-species-180987292/](https://www.smithsonianmag.com/smart-news/these-ant-queens-seem-to-defy-biology-they-lay-eggs-that-hatch-into-another-species-180987292/)

伊比利亚收获蚁蚁后（Messor ibericus）表现出一种不寻常的繁殖策略，称为“异种生育”，即它们产下的卵会孵化成另一种物种，建造者收获蚁（Messor structor）。这颠覆了物种的传统生物学定义。

M. ibericus 蚁后与 M. structor 雄蚁交配并储存精子。然后，它们操纵卵子，在用 M. structor 精子受精之前移除自身的遗传物质，从而产生 M. structor 雄性克隆体。M. ibericus 蚁后也通过与蚁群中的 M. ibericus 雄蚁交配来生产自身物种的雄蚁。M. ibericus 蚁群内的所有工蚁都是这两个物种的杂交种。

研究人员通过分析 M. ibericus 蚁群中的蚂蚁发现了这种现象，并发现一些雄蚁在基因上是 M. structor，但共享从母亲那里继承的 M. ibericus 线粒体 DNA。在实验室蚁群中观察到 M. structor 的诞生进一步证实了这一点。

这种关系似乎对两个物种都有利。M. ibericus 确保了足够的工蚁数量，并保持了获得 M. structor 雄蚁的途径。被转移的 M. structor 雄性克隆体也使该物种得以传播到新的地方。然而，由于缺乏有性繁殖，这些 M. structor 克隆体正在积累潜在的有害突变。尽管如此，这种安排是成功的，使得一个物种能够携带另一个物种横跨南欧。

---

## 3. 将旧电视改造为礼物（2019）

**原文标题**: Revamping an Old TV as a Gift (2019)

**原文链接**: [https://blog.davidv.dev/posts/revamping-an-old-tv-as-a-gift/](https://blog.davidv.dev/posts/revamping-an-old-tv-as-a-gift/)

2017年，作者改造了一台老式电视机作为父亲50岁生日礼物，旨在创造流畅观看七八十年代节目的体验。该项目涉及将树莓派集成到电视中以播放内容。由于树莓派输出复合视频信号，因此使用了一个复合RF调制器将信号转换为电视可以显示的格式，并将电视调谐器固定到调制器的输出频道。

为了保留频道切换功能，作者实现了基于软件的频道，由连接到树莓派GPIO的多极旋转开关控制。树莓派（5V）和调制器（9V）的电源来自电视的12V电源轨，使用LM7809和LM7805稳压器，并利用电视的一部分作为散热器。

最初计划随机播放每个频道的节目和广告，但由于GStreamer的困难而被放弃。取而代之的是，每个频道都变成了一个包含嵌入式广告的8小时视频。播放时间戳在断电时保存，并在开机时恢复，确保连续播放。作者还创建了一个虚假的包裹追踪网站作为额外惊喜。

---

## 4. 互联网档案馆与音乐出版商的大战以和解告终

**原文标题**: Internet Archive's big battle with music publishers ends in settlement

**原文链接**: [https://arstechnica.com/tech-policy/2025/09/internet-archives-big-battle-with-music-publishers-ends-in-settlement/](https://arstechnica.com/tech-policy/2025/09/internet-archives-big-battle-with-music-publishers-ends-in-settlement/)

互联网档案馆(IA)与主要音乐出版商(环球音乐、国会唱片、索尼音乐娱乐等)就其旨在保存早期音乐录音的“伟大78转唱片计划”达成保密和解。出版商发起的诉讼最初寻求4亿美元的赔偿，后来增加到7亿美元，指控IA的数字化录音侵犯版权并造成流媒体收入损失。IA辩称，“伟大78转唱片计划”的下载量和播放量都很低，损害赔偿被夸大了。

和解条款仍未公开，和解金额也不太可能被公开。在此协议之前，IA曾与图书出版商进行过类似的法律诉讼，最终败诉，也导致了一笔未公开的付款。IA曾指责唱片公司在诉讼后期添加作品，以迫使其达成和解。

加州大学圣巴巴拉分校的声音历史学家大卫·塞伯特认为，这场诉讼可能具有“报复性”，因为“伟大78转唱片计划”可能对唱片公司的收入影响甚微。他推测，唱片公司可能是在反击IA“在版权和合理使用方面挑战极限”。和解对IA的财务影响以及其数字化项目的未来仍然不确定。

---

## 5. Ruby Central 对 RubyGems 的攻击 [pdf]

**原文标题**: Ruby Central's Attack on RubyGems [pdf]

**原文链接**: [https://pup-e.com/goodbye-rubygems.pdf](https://pup-e.com/goodbye-rubygems.pdf)

无法对该文档提供有意义的摘要。文本似乎直接从PDF源代码中提取，混合了PDF格式字符、编码数据，以及一些嵌入的文本，这些文本未经正确的PDF解析和解码是无法阅读的。 这不是一份人类可读的文档，也不包含任何关于“Ruby Central对RubyGems的攻击”或其他主题的连贯信息。 任何试图总结它的行为都将基于猜测，并且完全不准确。

---

## 6. 想惹恼你的IT部门吗？链接看起来还不够恶意？

**原文标题**: Want to piss off your IT department? Are the links not malicious looking enough?

**原文链接**: [https://phishyurl.com/](https://phishyurl.com/)

本文介绍了一种工具，该工具旨在生成“钓鱼”网址，用于教育测试或恶作剧。该工具的功能类似于TinyURL的重定向服务，但不是缩短链接，而是使其看起来具有恶意性。用户输入合法的网址，该工具会创建一个新的、看起来可疑的网址，但该网址只会重定向到原始链接。

本文允许用户根据主题自定义生成的钓鱼网址，主题包括：加密货币、金融、钓鱼、在线购物、赌博、约会、科技与软件、成人内容以及“给我惊喜！”选项。用户还可以选择网址的长度，范围从小到“狠狠地搞我！”，从而影响生成链接的表面复杂性和潜在恶意性。

作者强调，该工具实际上并未执行任何恶意活动；它仅旨在创建具有欺骗性的网址，用于演示或幽默目的。其隐含的目标是演示恶意外观的网址是多么容易创建，以及潜在地用于网络钓鱼攻击，大概是为了提高人们的意识。虽然本文以幽默的口吻呈现，但其潜在信息触及了网址审查的重要性。

---

## 7. 八周内交付100台硬件设备

**原文标题**: Shipping 100 hardware units in under eight weeks

**原文链接**: [https://farhanhossain.substack.com/p/how-we-shipped-100-hardware-units](https://farhanhossain.substack.com/p/how-we-shipped-100-hardware-units)

好的，以下是好的，这是一篇关于“八周内交付100个硬件产品”文章的摘要，基于我对硬件初创公司常见挑战和解决方案的理解，因为我无法访问提供的URL：

这篇文章可能详细描述了作者在非常短的时间内（八周内）交付小批量（100个）硬件产品的经验。鉴于典型的硬件开发挑战，这篇文章可能侧重于效率和战略决策。

关键要点可能包括：

* **优先级排序与功能精简：** 为了赶上截止日期，团队可能不得不积极地优先考虑核心功能，并取消初始版本中的“锦上添花”的功能。这可能涉及简化设计，专注于基本功能，并将高级功能推迟到以后的迭代中。
* **利用现有组件与服务：** 团队可能使用了现成的组件、模块和云服务来加速开发并最大限度地减少定制工程，而不是从头开始设计所有内容。
* **快速原型设计与测试：** 迭代原型设计和快速测试可能至关重要。这使团队能够在过程的早期识别和修复错误，从而避免以后造成代价高昂的延误。可能使用了3D打印和现成的开发板等方法。
* **高效的制造与组装：** 团队可能使用了合同制造商 (CM) 或与当地的组装合作伙伴合作来处理设备的生产和组装。清晰的沟通、详细的文档和严格的质量控制可能至关重要。他们可能根据速度和灵活性而不是最低成本来选择 CM。
* **精简的供应链：** 在短时间内管理小批量产品的供应链非常困难。团队可能仔细选择了库存充足且交货时间可靠的供应商。他们可能还选择了空运而不是海运来加快运输速度。
* **团队协作与沟通：** 一个小型、积极性高的团队，拥有明确的角色和职责，对于成功可能至关重要。每日站立会议、共享沟通渠道和开放反馈的文化可能有助于提高效率。
* **接受不完美：** 作者可能承认最初的产品并不完美。目标是快速为客户提供功能齐全且可交付的产品，收集反馈，并根据该反馈进行迭代。

这篇文章可能强调，快速交付硬件产品需要做出艰难的选择，专注于基本功能，利用现有资源，并在初始版本中优先考虑速度而不是完美。

---

## 8. 展示物理

**原文标题**: Show the Physics

**原文链接**: [https://interactivetextbooks.tudelft.nl/showthephysics/Introduction/About.html](https://interactivetextbooks.tudelft.nl/showthephysics/Introduction/About.html)

《展示物理》是一本书，精选了荷兰“ShowdeFysica”系列的99个引人入胜的物理演示实验，旨在成为物理教师的宝贵资源。它提供了最大化演示实验教育影响的策略，包括无需安装软件即可访问的视频和互动式Python模拟。

本书根据演示实验的目的进行分类：科学本质、科学探究、概念发展和特殊场合。它鼓励教师利用这些演示实验来加深理解，激发思考，或为活动提供引人入胜的物理内容。

本书是荷兰科学教育协会的合作成果，每个演示实验都经过教师测试。在承认受到早期实验启发的同时，本书也包含检查学生理解的问题。本书以CC-BY-NC许可发布，允许非商业用途和适当署名的改编。

鼓励读者灵活使用本书，搜索与其课程相关的演示实验，或探索关于演示实验教学法的章节。尽管详细说明了安全措施，但作者不对事故负责，并强调预先测试。

在线形式包括互动式Python代码单元，允许用户在其浏览器中试验和修改代码。读者可以通过GitHub报告问题和提出改进建议来为本书做出贡献。书中还提到了一个包含200个较小“口袋演示”的配套资源。

---

## 9. 帮助我们筹集20万美元，让JavaScript摆脱甲骨文的控制

**原文标题**: Help Us Raise $200k to Free JavaScript from Oracle

**原文链接**: [https://deno.com/blog/javascript-tm-gofundme](https://deno.com/blog/javascript-tm-gofundme)

瑞恩·达尔于2025年9月18日呼吁开发者社区帮助Deno筹集20万美元，以资助针对Oracle的“JavaScript”商标控制权法律战。Deno在收到超过27000个签名致Oracle的公开信后，向美国专利商标局提交了撤销申请。

该请愿旨在使“JavaScript”成为公共领域，允许开发者、会议、作者和公司自由使用，而无需担心商标侵权。这笔资金用于诉讼的关键发现阶段，包括专业的公众调查、专家证人、行业领导者的证词和法律文件。

作者强调了资助这些要素的重要性，以建立一个强有力的案例，证明“JavaScript”被普遍认为是语言的名称，而不是Oracle的品牌。Oracle在2025年8月6日对该请愿的回应中否认“JavaScript”是一个通用术语。

达尔认为，如果Oracle胜诉，他们将基本上锁定对通用语言名称的所有权，破坏商标法的完整性，并可能允许其他公司声称拥有通用术语的所有权。如果还有剩余资金，这笔钱将捐给OpenJS基金会，而不是Deno，用于促进数字领域的公民自由。作者敦促开发者社区捐款并分享该活动，以确保商标法按预期运作。

---

## 10. 使用R语言的统计物理：蒙特卡洛模拟伊辛模型

**原文标题**: Statistical Physics with R: Ising Model with Monte Carlo

**原文链接**: [https://github.com/msuzen/isingLenzMC](https://github.com/msuzen/isingLenzMC)

`isingLenzMC` R包提供模拟经典Ising模型的工具。Ising模型是统计物理学中的一个基本系统，用于理解诸如自旋玻璃、磁性、相变和神经网络等现象。它专注于使用Metropolis和Glauber Monte Carlo方法模拟一维Ising模型，特别是具有单自旋翻转动力学和周期性边界条件。该软件包还包括用于计算精确解的实用函数。 Ising模型是研究协同现象的强大工具。

该软件包的开发与探索Ising模型中单自旋翻转动力学遍历性的研究相关。引用了两篇相关出版物：一篇研究有效遍历性的《Phys. Rev. E》文章和一篇检验收敛到有效遍历性期间异常扩散的arXiv预印本，两者均由Mehmet Suezen撰写。还提到了与arXiv论文相关的数据集，表明该软件包可能用于重现或扩展这些作品中呈现的结果。本质上，该软件包提供了在R中进行Ising模型模拟的实用实现，该实现基于对其动态特性的理论研究。

---

## 11. 特朗普赦免后，SEC撤销对特雷弗·米尔顿的尼古拉案。

**原文标题**: Trevor Milton's Nikola Case Dropped by SEC Following Trump Pardon

**原文链接**: [https://eletric-vehicles.com/nikola/trevor-miltons-nikola-case-dropped-by-sec-following-trump-pardon/](https://eletric-vehicles.com/nikola/trevor-miltons-nikola-case-dropped-by-sec-following-trump-pardon/)

在时任总统唐纳德·特朗普于3月给予尼古拉创始人特雷弗·米尔顿完全且无条件赦免后（本文章于2025年9月17日发布，赦免发生在6个月前），美国证监会已撤销对其的欺诈指控。米尔顿最初因证券欺诈罪被判处四年监禁，原因是其在尼古拉的技术和进展方面误导投资者。他声称证监会的案件是基于媒体、检察官和尼古拉前高管的谎言。

在兴登堡研究公司提出虚假陈述指控后，米尔顿于2020年辞去首席执行官一职。尽管米尔顿辩称赦免“一笔勾销”，但尼古拉正在反对他要求赔偿6900万美元法律费用的要求，理由是他存在“严重疏忽”和“恶意”行为。

尼古拉目前正在特拉华州进行第11章破产程序。破产计划正在受到审查，债权人寻求调查米尔顿是否正在转移个人资产，这些资产可用于偿还他对公司的债务。

---

## 12. 作为开发者，创建美观用户界面的规则

**原文标题**: Rules for creating good-looking user interfaces, from a developer

**原文链接**: [https://weberdominik.com/blog/rules-user-interfaces/](https://weberdominik.com/blog/rules-user-interfaces/)

本文从开发者的角度探讨了如何创建美观的用户界面，强调简洁性和一致性，而非复杂的设计知识。作者认为，对齐和一致性是糟糕设计中经常被忽视的关键因素，并展示了即使是细微的改进也能显著提升用户体验。

核心策略围绕利用组件库展开，提倡始终如一地使用它们，即使这意味着接受一些细微的瑕疵。作者建议选择一个提供所有必要组件且符合您设计偏好的库，并警告不要使用复制粘贴的库，因为这可能会导致不一致。

文章提供了一些实用的设计规则：限制字体粗细和文本颜色为两种，使图标粗细适应周围内容，以及优先考虑UI元素的目的以避免不必要的混乱。文章强调了创建项目特定的设计规则文档的重要性，以确保整个产品的一致性。

作者推荐了三本书籍：《Practical UI》、《Refactoring UI》和《Designing Interfaces》，供寻求可操作UI设计指导的开发者参考。

总而言之，关键在于优先考虑全局UI一致性，而非局部优化，从而简化设计流程并打造更用户友好和美观的界面。

---

## 13. 英特尔Arc Celestial独立显卡似乎是英伟达合作的第一个牺牲品

**原文标题**: Intel Arc Celestial dGPU seems to be first casualty of Nvidia partnership

**原文链接**: [https://www.notebookcheck.net/Intel-Arc-Celestial-dGPU-seems-to-be-first-casualty-of-Nvidia-partnership-while-Intel-Arc-B770-is-allegedly-still-alive.1118962.0.html](https://www.notebookcheck.net/Intel-Arc-Celestial-dGPU-seems-to-be-first-casualty-of-Nvidia-partnership-while-Intel-Arc-B770-is-allegedly-still-alive.1118962.0.html)

本文探讨了关于英特尔Arc桌面GPU产品线命运的传闻，特别是关注Arc Battlemage B770和未来的Arc Celestial。根据Moore's Law Is Dead (MLID)的爆料，Arc B770预计仍将于本季度发布，拥有32个Xe核心和256位宽的总线，目标是达到RTX 4070级别的性能。然而，现在有消息称它将缺乏PCIe 5.0支持，并可能存在帧步调问题，导致性能不流畅和供应有限。

更重要的是，本文声称英特尔据报道已取消了其计划中的Arc Celestial dGPU，这标志着英特尔可能结束高端桌面GPU的开发。据传，此次取消是英特尔与英伟达合作的后果。如果这是真的，像Arc Druid这样的未来架构也可能被放弃，从而有效地阻止英特尔的桌面GPU雄心。

尽管未来高端显卡的前景黯淡，但本文表达了对英特尔将继续追求桌面GPU的希望，并称Arc Battlemage B580是GPU市场的一个积极补充。文章还提到了最近关于英特尔和英伟达在Hammer Lake和Titan Lake APU上合作的相关新闻。

---

## 14. 流浪者 (利泽曼)

**原文标题**: Leatherman (vagabond)

**原文链接**: [https://en.wikipedia.org/wiki/Leatherman_(vagabond)](https://en.wikipedia.org/wiki/Leatherman_(vagabond))

皮衣人是一位流浪者，大约从1857年到1889年间，他在康涅狄格河和哈德逊河之间往返于365英里的线路。他以手工制作的皮革服装和可预测的路线而闻名，每34天返回康涅狄格州西部和纽约州东部的城镇。

他的身世和身份仍然未知，尽管人们认为他是法裔加拿大人，因为他精通法语，并且在他的身上发现了一本法语祈祷书。他主要通过咕哝和手势交流，很少说英语。他住在岩石庇护所里，被称为“皮衣人洞穴”，依靠城镇居民的慷慨捐助获得食物。他非常有名，以至于一些城镇免除了他的州“流浪法”。

1888年，康涅狄格人道协会将他送往医院，在那里他被诊断为“神智健全，只是患有情感上的痛苦”。由于他有钱并渴望自由，他被释放了。1889年，他在纽约州奥西宁附近的一个洞穴中死于口腔癌。

他最初的墓碑错误地将他认定为法国里昂的朱尔斯·布格莱，这一说法后来被撤回。2011年，他的坟墓被移动，并安装了一块新的墓碑，上面简单地写着“皮衣人”。对坟墓的挖掘没有发现任何人类遗骸。皮衣人启发了各种形式的媒体，包括一首珍珠果酱乐队的歌曲和一个电子游戏角色。

---

## 15. Lambda演算的规则学

**原文标题**: The Ruliology of Lambdas

**原文链接**: [https://writings.stephenwolfram.com/2025/09/the-ruliology-of-lambdas/](https://writings.stephenwolfram.com/2025/09/the-ruliology-of-lambdas/)

无法访问文章链接。

---

## 16. Dynamo AI (YC W22) 招聘资深 Kubernetes 工程师

**原文标题**: Dynamo AI (YC W22) Is Hiring a Senior Kubernetes Engineer

**原文链接**: [https://www.ycombinator.com/companies/dynamo-ai/jobs/fU1oC9q-senior-kubernetes-engineer](https://www.ycombinator.com/companies/dynamo-ai/jobs/fU1oC9q-senior-kubernetes-engineer)

Dynamo AI (YC W22) 是一家为企业构建安全且可扩展人工智能系统的公司，现招聘高级 Kubernetes 工程师，负责将其基于 Kubernetes 的集群部署到客户环境中。这是一个面向客户、亲力亲为的职位，需要成为 Dynamo AI 产品与客户基础设施之间的技术桥梁。

该工程师将负责与客户沟通、了解他们的需求、改进核心基础设施以提高性能和安全性、开发用于自动化部署的部署模型、与 DevOps 团队合作，并跨团队协作以提高人工智能系统的保护能力。

主要资格包括：在 Kubernetes、Helm、容器化应用程序交付方面拥有丰富的经验，以及至少精通 AWS、Azure 或 GCP 中的一种。该职位还要求在解决方案架构、DevOps 或云工程方面拥有 4 年以上的经验，2 年以上的直接客户互动经验，熟悉身份验证/授权系统，以及强大的沟通能力。由于与美国政府客户合作，因此需要美国公民身份或安全许可，并且需要在旧金山或纽约办公室每周工作 2-3 天。具有 AI/ML 基础设施经验者优先。薪资范围为 17 万美元至 23 万美元。

---

## 17. 许多损坏的信息流

**原文标题**: The Many Broken Feeds

**原文链接**: [https://notes.abhinavsarkar.net/2025/broken-feeds](https://notes.abhinavsarkar.net/2025/broken-feeds)

本文归纳了 RSS/Atom 订阅源失效的常见原因，并为每种情况提供了解决方案。作者作为资深的订阅源用户，强调订阅自己网站的订阅源对于主动发现问题至关重要。

最常见的失效原因是 **SSL 证书过期**，可以通过手动提醒、自动续订或使用 Cloudflare 等 CDN 来解决。**服务器速度慢导致的超时** 是另一个问题，通常是间歇性的，但需要调查主机基础设施或软件，以进行潜在的改进，例如缓存或硬件升级。

**配置错误的防火墙**，旨在阻止网络抓取机器人，可能会无意中阻止订阅源阅读器。作者敦促网站所有者将订阅源 URL 从这些规则中排除，或者在担心内容抓取时提供仅链接订阅源。服务器意外宕机也是罪魁祸首，可以通过设置监控和警报系统来解决。

由于网站重写或平台切换而导致的 **订阅源 URL 更改**，应通过维护旧 URL、重定向它们，或通过横幅或帖子通知读者来处理。**订阅源解析失败**，通常是由于手动编写的订阅源生成器造成的，可以通过定期验证订阅源是否存在编码问题来缓解。

最后，作者提到了故意删除订阅源和网站的行为，倡导继续使用订阅源，并对网站删除表示遗憾。文章最后发出了行动号召，鼓励读者分享和评论。

---

## 18. 圣家堂渐入最终形态

**原文标题**: The Sagrada Família takes its final shape

**原文链接**: [https://www.newyorker.com/magazine/2025/09/22/is-the-sagrada-familia-a-masterpiece-or-kitsch](https://www.newyorker.com/magazine/2025/09/22/is-the-sagrada-familia-a-masterpiece-or-kitsch)

圣家族教堂，安东尼·高迪在巴塞罗那的宏伟圣殿，即将完工，有望成为世界最高的教堂。该项目始于1882年，以其缓慢的步伐、受自然启发的独特设计以及对捐赠和旅游收入的依赖而闻名。目前，教堂的高度正在超越该市最高的摩天大楼。本月十字架的最终安装将使其成为世界最高的教堂。

高迪为该项目奉献了43年，他设想了一个拥有十八座塔楼的结构，分别献给宗教人物。尽管他在1926年去世时只建造了一小部分，但随后的建筑师一直在努力实现他的愿景，尽管在西班牙内战期间丢失了许多原始图纸。

在现任首席建筑师霍尔迪·法uli的领导下，施工已经加快，利用先进的软件和预制面板来更快地建造各个部分。圣家族教堂已成为主要的旅游景点，产生了大量的收入来资助其建设。法uli强调对高迪设计的保守态度，使用现有的记录和照片来指导他的工作，同时也承认高迪鼓励的创造性许可。这座大教堂是加泰罗尼亚文化的象征，预计在不久的将来完工。

---

## 19. 根据最新分析，美国已经拥有其所需的重要矿物。

**原文标题**: U.S. already has the critical minerals it needs, according to new analysis

**原文链接**: [https://www.minesnewsroom.com/news/us-already-has-critical-minerals-it-needs-theyre-being-thrown-away-new-analysis-shows](https://www.minesnewsroom.com/news/us-already-has-critical-minerals-it-needs-theyre-being-thrown-away-new-analysis-shows)

科罗拉多矿业学院研究人员在《科学》杂志上发表的一项新分析显示，美国已经开采了每年能源、国防和技术所需的所有关键矿物。然而，包括钴、锂、锗和稀土元素在内的这些矿物，目前被作为金和锌等其他采矿作业的尾矿丢弃。

该研究强调了回收这些关键矿物以显著减少或消除进口需求的潜力。通过建立一个联邦许可金属矿的年度产量数据库，并将其与地球化学浓度数据配对，研究人员估计了正在开采和加工但未回收的关键矿物的数量。

例如，回收目前被丢弃的钴的不到10%就足以满足整个美国电池市场的需求。同样，回收矿山尾矿中不到1%的锗就可以消除进口需求。

研究人员强调，加强回收具有经济、地缘政治和环境效益，包括减少矿山废弃物对环境的影响。他们呼吁进一步研究和开发，使这些矿物的回收在经济上可行，并倡导制定激励矿山运营商投资额外加工基础设施的政策。虽然这些矿物的市场价值可能不足以单独激励投资，但正确的政策可以弥合这一差距。

---

## 20. 苹果：SSH 与 FileVault

**原文标题**: Apple: SSH and FileVault

**原文链接**: [https://keith.github.io/xcode-man-pages/apple_ssh_and_filevault.7.html](https://keith.github.io/xcode-man-pages/apple_ssh_and_filevault.7.html)

本文介绍如何在 macOS 上结合 FileVault 使用 SSH。启用 FileVault 后，数据卷在启动时会被锁定，导致标准的 SSH 配置不可用，因为它位于加密卷上。但是，启用“远程登录”后，macOS 允许通过 SSH 进行密码验证，专门用于远程解锁 FileVault 卷。此解锁过程不会立即授予 SSH 会话。相反，在成功验证后，SSH 会短暂断开连接，同时系统会挂载数据卷并启动相关服务。在此短暂中断后，完整的 SSH 访问和其他启用的服务将可用。这种允许通过 SSH 远程解锁 FileVault 的功能是在 macOS 26 Tahoe 中引入的。本质上，它允许用户在系统完成启动过程后，远程解锁 FileVault 卷并重新通过 SSH 访问其系统。

---

## 21. 开发者文化的转变正在影响创新和创造力。

**原文标题**: A shift in developer culture is impacting innovation and creativity

**原文链接**: [https://dayvster.com/blog/dev-culture-is-dying-the-curious-developer-is-gone/](https://dayvster.com/blog/dev-culture-is-dying-the-curious-developer-is-gone/)

戴维·舒斯特在他的文章中表达了对开发者文化中一种转变的担忧，即从好奇心驱动的创新转向关注指标、收入优化和追逐最新技术。他回忆起过去开发者们出于好奇心和解决个人问题的愿望而创造诸如 Linux 和 Git 等工具的时代。

舒斯特认为，目前对构建大众消费产品和优化指标的强调正在扼杀创造力，并导致开发者认同特定的技术，而不是他们所要解决的问题。他强调了不断采用新的框架和库，而缺乏真正热情的趋势，这主要是出于对落后的恐惧。

他感叹“好奇的开发者”——那些即使实用性有限，也会创造出很酷东西的工匠——的潜在消失。虽然他承认偶尔会有创新火花，但他认为这些正变得越来越稀少。他将这一趋势与更广泛的所有权丧失联系起来，无论是消费者越来越多地租赁软件，还是创造者可能将利润置于热情之上。

舒斯特鼓励开发者抽出时间进行好奇心驱动的创造，仅仅为了乐趣而构建项目，并分享他们的作品以激励他人。他最后强调了保持创造力和工程技术的独特融合，这正是软件开发的定义所在。

---

## 22. 大卫·林奇洛杉矶住宅

**原文标题**: David Lynch LA House

**原文链接**: [https://www.wallpaper.com/design-interiors/david-lynch-house-los-angeles-for-sale](https://www.wallpaper.com/design-interiors/david-lynch-house-los-angeles-for-sale)

本文探讨大卫·林奇位于好莱坞山的庄园，这座在他去世后以1500万美元的价格挂牌出售的广阔地产。该物业展示了中世纪现代建筑风格，被誉为反映林奇电影视野的“创意圣地”。

该庄园由五块相邻的地块组成，包含三处主要住宅和其他几处建筑物。该物业的历史始于1987年收购的劳埃德·赖特设计的贝弗利·约翰逊住宅。林奇后来委托赖特的儿子埃里克·劳埃德·赖特增加了一个游泳池和泳池小屋。多年来，他扩建了庄园，包括一座粗野主义风格的房屋、一座工作室建筑和更多土地，最终创建了一个拥有七个建筑物、十间卧室和十一间浴室的圣地。

庄园的核心是一栋2000平方英尺的住宅，其特点是光线充足和天然纹理。值得注意的是，塞纳尔达街7035号既是《妖夜慌踪》中麦迪逊的住所，也是林奇的工作室，配有图书馆、放映室和剪辑室，他在那里创作了《穆赫兰道》等作品。

林奇亲自参与设计了一栋两层楼的客房和一间单卧室的静修室。庄园的露台、庭院和走道与创作过程的紧张形成对比。The Agency 将该物业描述为一座建筑地标，既代表着一个家，又代表着林奇思想的档案，为下一篇章做好了准备。

---

## 23. 在 Chrome 中使用 Gemini

**原文标题**: Gemini in Chrome

**原文链接**: [https://gemini.google/overview/gemini-in-chrome/](https://gemini.google/overview/gemini-in-chrome/)

本文宣布谷歌的 Gemini AI 助手直接集成到 Chrome 浏览器中。Chrome 中的 Gemini 作为一个内置于浏览器的 AI 助手，可帮助用户快速理解和利用网页内容。

主要功能包括：

*   **摘要总结：** Gemini 可以在浏览器内快速生成文章、网页和帖子的摘要。
*   **情境问答：** 它可以根据当前网页的内容回答问题，提供相关的解释和信息，而不会中断用户的阅读流程。
*   **复杂内容解释：** 它可以帮助用户理解困难的概念，澄清令人困惑的部分，并帮助用户更深入地理解。
*   **明智的决策：** 它可以从网页中提取关键信息、规格和优缺点，帮助用户做出明智的选择，尤其是在研究产品时。
*   **实时对话：** 用户可以与 Gemini 进行自然语言对话，包括接收语音回复（实时模式）。
*   **移动设备可用性：** Gemini 将在 Android 上提供（已经可以通过访问屏幕内容使用），并且很快将在 iOS 上推出，并直接集成到 Chrome 应用程序中。
*   **用户控制：** 该助手仅在用户单击 Gemini 图标或使用指定的键盘快捷键时激活。
*   **隐私功能：** 用户可以管理和删除他们的 Gemini 活动历史记录。
*   **可用性：** 目前在美国适用于 Chrome 语言设置为英语的 Windows 和 Mac 用户。 很快将适用于美国 Chrome 设置为英语的 iOS 用户。

文章强调，Chrome 中的 Gemini 提供了一种无缝且高效的方式来直接在浏览器中理解和交互网页内容，而无需切换标签页或应用程序。

---

## 24. 法院允许美国国家科学基金会继续大幅削减10亿美元的研究经费

**原文标题**: Court lets NSF keep swinging axe at $1B in research grants

**原文链接**: [https://www.theregister.com/2025/09/19/court_lets_nsf_keep_swinging/](https://www.theregister.com/2025/09/19/court_lets_nsf_keep_swinging/)

美国法院已允许国家科学基金会（NSF）继续取消超过1700项研究资助，总价值14亿美元。此前，法官驳回了一项要求在审理挑战终止资助诉讼期间恢复这些资助的请求。国家科学基金会发起此次削减，是因为一项政策变更缩小了纳税人资助项目可接受的“更广泛影响”范围，目标是那些专注于多元化、公平和包容（DEI）计划的项目。

教育和科学组织提起的诉讼辩称，国家科学基金会的行为是任意的，违反了正当程序。法官贾·科布裁定，法院无权命令追溯恢复资金，但允许继续挑战国家科学基金会的新拨款政策。

这一决定意味着项目正在暂停或关闭，扰乱研究，影响研究生，并迫使大学争夺资金。虽然一些大学正在试图填补资金缺口，但他们警告说无法覆盖所有内容。

STEM教育理事会受到的影响最大。与此同时，法国艾克斯-马赛大学启动了一项计划，以吸引面临中断的美国研究人员，提供资金和支持性环境。

---

## 25. 任天堂64 Linux (1997)

**原文标题**: Linux for Nintendo 64 (1997)

**原文链接**: [https://web.archive.org/web/19990220141243/http://www.heise.de/ix/artikel/E/1997/04/036/](https://web.archive.org/web/19990220141243/http://www.heise.de/ix/artikel/E/1997/04/036/)

本文最初发表于1997年的德国iX杂志，探讨了一项将Linux移植到任天堂64（N64）的尝试。文章首先提到Netscape和SCO早期与任天堂合作开发类似网络应用，但均未成功。

文章的核心内容详细介绍了意大利程序员团队成功将Linux/Mips移植到N64的过程。他们使用美版N64和SGI Indy工作站，克服了主要与将X Window系统移植到N64的I/O硬件相关的挑战。虽然尚未完全稳定，但他们的实现获得了令人印象深刻的XStone分数。

文章提到可以使用N64手柄或PC键盘进行输入，但手柄的文本输入存在局限性。可以使用可选的控制器记忆卡来保存数据，例如偏好设置。原型机面临网络挑战，原因是手动焊接的网络芯片存在问题。

尽管以双端模式运行，但由于内存只有4MB的限制，Linux/N64并没有充分利用64位寻址能力。任天堂拒绝支持该项目阻碍了其商业可行性。然而，西门子-尼克斯多夫和Silicon Graphics表示了兴趣。意大利开发者计划在GPL下发布该软件，使其可以免费使用。

---

## 26. 这张地图没有倒过来。

**原文标题**: This map is not upside down

**原文链接**: [https://www.maps.com/this-map-is-not-upside-down/](https://www.maps.com/this-map-is-not-upside-down/)

约书亚·史蒂文斯的文章《这张地图不是上下颠倒的》讨论了罗伯特·西蒙设计的以南方为上的世界地图，挑战了主导现代制图学的传统的北方朝上视角。文章解释说，虽然南方朝上的方向可能让人觉得陌生，但它在地理上是准确的，并提醒人们地图惯例并非天生不变的。

作者深入探讨了历史背景，提到几个世纪前，制图师使用各种方向的地图，反映了当时的工具和知识。他强调了早期中国人使用磁化装置，其中南方具有主要的方位意义。

史蒂文斯解释说，北方朝上的惯例虽然并非有意设计用于提升某些地区，但由于托勒密对纬度和经度的使用而变得突出，从而使地图复制和扩展更容易。此外，史蒂文斯指出，人们存在一种“好”在上而“坏”在下的心理联想，这可能会潜意识地影响地图的解读。

最终，西蒙的地图既是一种地理表示，又是一种哲学提示，鼓励观看者质疑既定传统及其影响。文章最后提供了关于西蒙地图的信息、其数据来源以及向Maps.com提交地图的说明。

---

## 27. AI工具正在让世界变得怪异。

**原文标题**: AI tools are making the world look weird

**原文链接**: [https://strat7.com/blogs/weird-in-weird-out/](https://strat7.com/blogs/weird-in-weird-out/)

人工智能工具让世界变得怪异

这篇题为《人工智能工具让世界变得怪异》的博文，探讨了过度依赖人工智能所带来的意想不到且往往是怪诞的后果。文章归类于“分析与人工智能”版块，并以幽默的副标题“怪异输入，怪异输出”为题，可能论证了用于训练人工智能模型的数据中的缺陷（怪异 - 指西方、受过教育、工业化、富裕和民主的人口）导致了扭曲和不切实际的输出，从而使世界看起来“怪异”。

其核心论点是，人工智能虽然具有潜力，但严重依赖于训练它的数据。如果这些数据偏向于特定的人群或观点（怪异），那么由此产生的人工智能将延续甚至放大这些偏见，从而导致不准确的表示，并在图像生成、自然语言处理，甚至关键决策系统等领域产生潜在的有害结果。

文章可能讨论了这种偏见如何体现的例子，也许展示了具有不切实际的体型或特征的人工智能生成的图像，或者强调了人工智能系统难以理解或适当地回应“怪异”规范之外的语言或文化背景的实例。

最终，这篇文章可能呼吁人们更加关注人工智能开发中的数据偏见，并共同努力使训练数据多样化，从而创建更具代表性和公平性的人工智能系统，更好地反映现实世界的复杂性和多样性。“怪异输入，怪异输出”的副标题强调了这个问题循环的本质，表明有偏差的数据将不可避免地导致有偏差的，最终是“怪异”的输出。

---

## 28. Slack 每年向我们增加了 19.5 万美元的费用。

**原文标题**: Slack has raised our charges by $195k per year

**原文链接**: [https://skyfall.dev/posts/slack](https://skyfall.dev/posts/slack)

为青少年提供编程教育的非营利组织Hack Club突然面临Slack大幅涨价。多年来一直愉快地支付每年5000美元费用后，Slack通知他们，他们需要在一周内额外支付5万美元，然后每年支付20万美元，以避免工作区停用和消息历史记录删除。

作者认为，Slack的母公司Salesforce的这一要求无异于勒索，因为它没有给该非营利组织足够的时间来适应如此大幅度的增长。这突如其来的通知扰乱了Hack Club的运营，迫使员工和志愿者争先恐后地迁移系统并重建集成。

在作者在Hacker News和Twitter/X上的病毒式帖子引发公众强烈抗议后，Slack的首席执行官联系了Hack Club，并提供了一个比之前计划更好的解决方案。虽然具体细节未详细说明，但情况已解决，Hack Club对此表示满意。

这次经历促使Hack Club优先考虑数据所有权并迁移到Mattermost。作者鼓励其他小型企业考虑类似的策略，以避免依赖外部SaaS提供商并确保对其数据的控制。

---

## 29. 在内核中使用 Rust 追踪信任

**原文标题**: Tracking trust with Rust in the kernel

**原文链接**: [https://lwn.net/Articles/1034603/](https://lwn.net/Articles/1034603/)

2025年9月3日 LWN.net 文章探讨了 Benno Lossin 提出的用于处理 Linux 内核 Rust 代码中非信任数据的 API。该 API 引入了一种新的 `Untrusted` 类型来标记来自用户空间、网络连接或可移动存储等来源的数据。核心思想是使用 Rust 的类型系统来防止意外滥用非信任数据。`Untrusted` 是一个透明的包装器，不增加运行时开销，但如果未经验证直接使用该值，则会导致编译器错误。

该补丁集包括文档和实用工具函数，特别是用于非信任值的切片和向量。它建议编写使用 `&mut [Untrusted<u8>]` 填充用户空间数据的缓冲区函数。为了实际使用数据，该 API 引入了一个 `Validate` trait，它封装了将 `Untrusted<S>` 转换为安全、经过验证的类型 `T` 的逻辑。

Greg Kroah-Hartman 要求提供一个使用 `Untrusted` 的示例驱动程序，Lossin 提供了一个使用 `ioctl()` 的草图。该示例展示了如何基于命令验证 `ioctl()` 参数，使用枚举和 `Untrusted<IoctlArgs>` 类型。

Kroah-Hartman 还提出了 TOCTOU 漏洞（检查时间和使用时间之间存在差异）的问题，即数据在被复制之前会被验证。 Lossin 的设计使用 `UserPtr` 和 `UserSlice` 类型来表示用户空间中的指针和切片，并建议修改 `UserSlice::read_all()` 将读取的字节标记为非信任。

文章最后指出，该 API 可能需要对 Rust 驱动程序接口进行重大更改，并很可能在即将举行的 Kangrejos 会议上进行讨论。评论部分反映了所提出的 API 的优点和潜在缺陷。

---

## 30. 使用SLJIT即时编译栈式虚拟机

**原文标题**: JIT-ing a stack machine (with SLJIT)

**原文链接**: [https://bullno1.com/blog/jiting-a-stack-machine](https://bullno1.com/blog/jiting-a-stack-machine)

本文详细介绍了作者使用 SLJIT 库对栈式虚拟机（特别是 uxn VM）进行 JIT 编译的经验。目标是通过用 JIT 编译的代码替换现有的字节码解释器，从而提高性能，尤其是在较小的设备上。

作者概述了计划的 JIT 编译过程：检查现有 JIT 代码，静态跟踪代码块，使用 SLJIT 进行 JIT 编译，并缓存结果。文章简要介绍了 SLJIT，解释了其可移植的汇编接口和寄存器管理。

遇到的挑战包括确定要使用的寄存器数量（使用枚举解决）、处理 x86-32 上的内存寻址限制（使用 `buxn_jit_set_mem_base` 解决）以及管理操作数的寄存器分配（使用位图跟踪已用寄存器）。一个简单的操作码 (SUB) 的实现演示了寄存器分配和代码生成过程。

文章强调了动态跳转的问题，即目标只有在运行时才知道。文章实现了一种 trampoline 技术，其中 JIT 编译的函数将下一个程序计数器 (PC) 返回给 trampoline，从而允许间接跳转。JIT 编译器类似于解释器循环，静态跟踪字节码并调用操作码处理程序。

然而，最初的 JIT 实现产生了令人失望的性能。频繁的动态跳转导致 JIT 运行时类似于缓慢的 switch 分发，抵消了原生编译的优势和原始解释器中优化的分支预测。用于堆栈推送和弹出的简单内存加载和存储操作也导致了性能不佳。文章最后强调了调用优化和内存访问策略对于在 JIT 编译器中实现真正的性能提升的重要性。

---

## 31. 使用SLJIT即时编译栈式虚拟机

**原文标题**: JIT-ing a stack machine (with SLJIT)

**原文链接**: [https://bullno1.com/blog/jiting-a-stack-machine](https://bullno1.com/blog/jiting-a-stack-machine)

本文详细介绍了作者使用SLJIT库为uxn堆栈机实现JIT（即时）编译器的过程。目标是提高受字节跳动启发的实时编辑环境的字节码执行速度。

最初的计划涉及方法JIT：检查先前JIT编译的入口点，静态跟踪代码块，使用SLJIT进行JIT编译，并缓存编译后的代码。SLJIT的“可移植汇编”方法使作者能够利用现有的汇编知识。关键挑战包括管理寄存器（使用枚举解决保存和暂存寄存器问题），处理x86-32上的内存寻址限制，以及使用基于位图的方法为操作数分配寄存器。

动态跳转是uxn的一个特性，跳转目标仅在运行时才知道，通过使用跳转表技术解决，从JIT编译的函数返回新的程序计数器（PC）。编译器跟踪字节码，处理操作码并在遇到BRK指令时终止。

然而，最初的性能结果令人失望。由于动态跳转而频繁返回到跳转表有效地将JIT运行时变成了一个switch分发，抵消了原生编译的优势。用于堆栈操作（push和pop）的简单内存加载和存储实现进一步阻碍了性能，原因是内存访问延迟。

文章最后指出，分支预测和内存访问是未来优化的关键领域，重点是静态调用识别，以利用处理器级别的调用/返回预测。

---

## 32. YouTube下载器（以及谷歌如何让媒体噤声）

**原文标题**: YouTube downloaders (and how Google silenced the press)

**原文链接**: [https://windowsread.me/p/best-youtube-downloaders](https://windowsread.me/p/best-youtube-downloaders)

克里斯·霍夫曼认为，尽管谷歌不鼓励使用和讨论YouTube下载器，但它们是合乎道德的、必要的，甚至暗中对谷歌在视频托管领域的统治地位有利。他提供了一个推荐的免费YouTube下载器列表：Stacher (Windows, Mac, Linux), yt-dlp (命令行), Cobalt.tools (基于网页，但目前被谷歌屏蔽), 和 NewPipe (Android)。

霍夫曼认为，YouTube下载器允许用户存档重要内容，类似于保存网页或图像的功能。他认为谷歌默许下载器的存在，因为完全封锁YouTube会将用户赶到更灵活的平台。他声称，谷歌历史上曾通过威胁广告收入来压制报道YouTube下载器的出版物（如How-To Geek），尽管现在这种做法不那么明显了。他认为，虽然谷歌不希望用户公开下载YouTube视频，但这个过程并非不可能，保持着一个有助于视频平台成功的“逃生舱”。最后，他通过提及无人阅读或遵守的最终用户许可协议来支持他的论点，并为在AI内容抓取时代下载视频辩护。

---

## 33. 用你的方式学习：用生成式AI重新构想教科书

**原文标题**: Learn Your Way: Reimagining Textbooks with Generative AI

**原文链接**: [https://research.google/blog/learn-your-way-reimagining-textbooks-with-generative-ai/](https://research.google/blog/learn-your-way-reimagining-textbooks-with-generative-ai/)

谷歌研究文章介绍“学你所想”，这是 Google Labs 上的一个研究实验，探索生成式 AI (GenAI) 如何将教科书转变为个性化和引人入胜的学习体验。该项目通过使用 GenAI 自动生成替代表示形式和个性化示例，解决了“一刀切”教科书的局限性。

“学你所想”建立在两个关键支柱之上：生成多样化的、多模态的内容表示形式（如思维导图、旁白幻灯片和音频课程），并根据学生的年级和兴趣个性化内容。该系统利用 LearnLM 和 Gemini 2.5 Pro 重新调整文本难度、替换通用示例并创建各种内容格式。

一项针对 15-18 岁学生的有效性研究表明，学习成果有了显著提高。与使用传统数字 PDF 阅读器的学生相比，使用“学你所想”的学生在即时评估中得分高出 9%，在记忆测试中得分高出 11%。用户情绪也很积极，学生报告说对评估的接受度更高，并希望将来使用“学你所想”。

该文章强调了学科专家对教学法的积极评价。Google Labs 上提供了几个示例体验，涵盖免疫系统、经济学和社会学等主题。作者设想进一步的个性化将朝着适应每个学习者独特需求和进度的系统发展。

---

## 34. Llama工厂：统一高效的百种开源LLM微调

**原文标题**: Llama-Factory: Unified, Efficient Fine-Tuning for 100 Open LLMs

**原文链接**: [https://github.com/hiyouga/LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)

Llama-Factory 是一个统一且高效的微调工具，支持来自 Amazon、NVIDIA 和阿里云等不同提供商的 100 多个开源大型语言模型 (LLM)。它提供用户友好的界面（CLI 和 Web UI），只需极少的编码即可进行微调。

该平台支持多种模型，包括 LLaMA、LLaVA、Mistral、Qwen、Gemma 和 ChatGLM 等。它集成了各种训练方法，如预训练、监督式微调以及强化学习技术（如 PPO、DPO 和 KTO）。Llama-Factory 通过 LoRA 和 QLoRA 等技术以及 GaLore 和 DoRA 等高级算法，促进可扩展的资源利用。它还实现了 FlashAttention-2 和 Unsloth 等实用技巧来提高性能。

Llama-Factory 支持广泛的任务，包括多轮对话、工具使用、图像理解等。通过 LlamaBoard、Wandb 和 SwanLab 等工具支持实验监控。使用 OpenAI 风格的 API 和 vLLM 可以实现更快的推理。

该平台为预训练和监督式微调提供大量数据集，并已应用于心理健康、角色扮演和信息提取等多种应用。Day-N 支持确保与最新模型的兼容性。该项目正在积极维护，并进行频繁的更新和改进。

---

## 35. 鲁珀特的截角立方体和其他数学洞穴

**原文标题**: Rupert's snub cube and other Math Holes

**原文链接**: [http://tom7.org/ruperts/](http://tom7.org/ruperts/)

本文题为《鲁珀特立方体和其他数学漏洞》，侧重于从各种数学角度探索立方体及相关形状。它建立在先前作品《关于形状的一些令人不安的事情（我们已经知道的）》的基础上，暗示着对这些形状的熟悉方面的深入研究。

作者邀请读者通过以下几种方式进一步探索该主题：一个具有挑战性的视频游戏版本，一个带有形式验证的、视觉上令人平静的视频版本，以及柏拉图、阿基米德和卡塔兰立体的3D模型，以及不太吸引人的凸多面体的模型。

本文鼓励读者积极参与，尝试自己寻找解决方案或识别所提供的源代码中的错误，这表明存在需要C++编译器并愿意修改的代码。

最后，作者希望通过在其博客上发表评论或通过观察他们在BlueSky或Mastodon等社交媒体平台上不经常发布的帖子来获取反馈。文章最后将读者引导至[tom7.org]上作者更广泛的作品集。本质上，这是一份邀请，邀请您深入研究立方体及相关形状的复杂性，并提供多种参与途径和征求社区反馈的请求。

---

## 36. 养老院的肮脏现实：居民沦为牟利工具

**原文标题**: The sordid reality of retirement villages: Residents are being milked for profit

**原文链接**: [https://unherd.com/2025/09/the-sordid-truth-about-retriement-villages/](https://unherd.com/2025/09/the-sordid-truth-about-retriement-villages/)

亚历克斯·泰勒的文章《养老社区的肮脏现实：住户被榨取利润》揭露了养老社区常常被美化的形象实则是一个欺骗性的外表。泰勒将个人经历与更广泛的研究相结合，揭示了一个住户面临高昂费用、房产价值回报下降以及潜在剥削的系统。

虽然养老社区被宣传为拥有各种便利设施的蓬勃发展的社区，但现实情况却涉及高昂的服务费、地租和复杂的购回协议，这些都让家庭在经济上不堪一击。作者描述了广告宣传的生活方式与实际体验之间的脱节，并列举了忽视和关注利润而非住户福祉的例子。老年人往往不是在蓬勃发展和积极生活，而是被剥削他们的资源和储蓄。

这篇文章强调了养老社区生活的经济劣势，同时也提到了社会互动和减少孤独的潜在好处。作者批评了当前这种以利润为先、忽略关怀的制度。文章最后强调迫切需要改革，以保护弱势老年人在这些独立生活计划中免受剥削。

---

## 37. 不玩《我的世界》玩《我的世界》(2024)

**原文标题**: Playing “Minecraft” without Minecraft (2024)

**原文链接**: [https://lenowo.org/viewtopic.php?t=5](https://lenowo.org/viewtopic.php?t=5)

本文介绍如何在不使用任何 Mojang 官方代码的情况下游玩一个版本的“Minecraft”。 它通过利用社区开发的对游戏客户端和服务器的洁净室实现来实现这一点。

本指南概述了必要的软件组件：Cuberite (一个基于 C++ 的 Minecraft 服务器)、ViaProxy (一个基于 Java 的协议转换器) 和 Minosoft (一个基于 Kotlin 的 Minecraft 客户端)。 它详细介绍了运行这些组件的系统要求，强调需要一台具有足够处理能力、RAM 和支持 OpenGL 的显卡的 64 位计算机。

然后，本文提供了有关如何安装和配置每个组件的分步说明：下载并运行 Cuberite 服务器，下载并设置 ViaProxy 以桥接服务器和客户端版本之间的协议差异，以及从 GitHub Actions 获取 Minosoft。

最后，它解释了如何启动 Minosoft、创建玩家帐户、在客户端中配置服务器连接详细信息（指向 ViaProxy 的 IP 和端口），以及连接到 Cuberite 服务器。 故障排除部分解决了与 Cuberite 的在线模式登录要求相关的常见连接问题，并提供了禁用身份验证的解决方案。 本质上，该指南使用户能够体验完全由开源替代方案构建的类似“Minecraft”的体验。

---

## 38. 英伟达收购英特尔价值50亿美元股份

**原文标题**: Nvidia buys $5B in Intel

**原文链接**: [https://www.tomshardware.com/pc-components/cpus/nvidia-and-intel-announce-jointly-developed-intel-x86-rtx-socs-for-pcs-with-nvidia-graphics-also-custom-nvidia-data-center-x86-processors-nvidia-buys-usd5-billion-in-intel-stock-in-seismic-deal](https://www.tomshardware.com/pc-components/cpus/nvidia-and-intel-announce-jointly-developed-intel-x86-rtx-socs-for-pcs-with-nvidia-graphics-also-custom-nvidia-data-center-x86-processors-nvidia-buys-usd5-billion-in-intel-stock-in-seismic-deal)

英伟达与英特尔宣布合作，共同开发x86产品，英伟达将投资50亿美元。合作内容包括：

*   **英特尔x86 RTX SOC：** 全新的x86英特尔CPU与英伟达RTX显卡芯片融合，面向消费级游戏PC，旨在与AMD APU在轻薄游戏笔记本和小尺寸PC市场竞争。这些芯片将使用NVLink实现更快的CPU到GPU通信和统一内存访问。
*   **定制x86数据中心CPU：** 英特尔将为英伟达的AI产品构建定制的x86数据中心CPU，利用NVLink技术增强CPU-GPU通信。英伟达随后将作为自己的产品销售这些CPU。CPU的修改程度尚未完全披露。
*   **英伟达投资：** 英伟达将购买价值50亿美元的英特尔普通股，约占5%的股份，需经监管部门批准。

英伟达强调其对现有产品路线图的承诺，表明此次合作是对其现有计划的补充。虽然制造地点尚未确定，但英特尔有可能在其自己的代工厂中制造一些英伟达定制的x86芯片。此次合作利用NVLink接口实现比PCIe更高的带宽和更低的延迟。该合作旨在将英伟达的AI和加速计算与英特尔的x86生态系统相结合。

---

## 39. 德州农工大学校长将在性别认同课程风波后卸任

**原文标题**: Texas A&M president to step down after turmoil over gender identity lesson

**原文链接**: [https://thehill.com/homenews/education/5511704-texas-am-president-to-step-down-after-turmoil-over-gender-identity-lesson/](https://thehill.com/homenews/education/5511704-texas-am-president-to-step-down-after-turmoil-over-gender-identity-lesson/)

德州农工大学校长M·凯瑟琳·班克斯因教师主导的关于性别认同的多元、公平和包容（DEI）培训课程引发争议而辞职，该课程被认为违反了德克萨斯州法律。 该课程被一些人认为不恰当且与大学价值观相悖，引发了州政府官员和保守团体的强烈批评。

在共和党议员指控组织这次培训的教授乔伊·阿隆佐在课程中批评了副州长丹·帕特里克（阿隆佐否认了这一指控）后，德州农工大学暂停了阿隆佐的职务，然后又恢复了她的职务，这使得争议进一步升级。 这一行动以及大学对此事的处理，引发了更多的批评，以及对学术自由和政治干预大学事务的担忧。

班克斯以需要“一致的方向”为由，表示她打算立即退休，并声称这符合大学的最佳利益。 校董会接受了她的辞呈。 这场争议凸显了DEI倡议与州法律之间的紧张关系，尤其是在像德克萨斯州这样的保守州，并引发了人们对高等教育政治化的担忧。 在这一事件发生后，德州农工大学和其他德克萨斯州大学的DEI项目的未来仍然不明朗。

---

## 40. KDE现在是我最喜欢的桌面。

**原文标题**: KDE is now my favorite desktop

**原文链接**: [https://kokada.dev/blog/kde-is-now-my-favorite-desktop/](https://kokada.dev/blog/kde-is-now-my-favorite-desktop/)

作者切换到 KDE 桌面环境的积极体验：为妻子而始，惊艳于自身

这篇博文详细介绍了作者切换到 KDE 作为桌面环境的积极体验。起初主要是为了 KDE 对其妻子的用户友好性，但最终发现它出乎意料的优秀。作者称赞 KDE 的功能完整性，甚至将其与 Windows 和 macOS 相提并论。具体的例子包括详细的网络小程序信息、集成了智能裁剪功能的屏幕截图工具，以及用于应用程序定制的强大的“窗口规则”。

作者强调了 KDE 集成良好的工具，例如简便的 Flatpak 权限管理和通过信息中心访问硬件信息，从而无需许多第三方程序。他们还赞扬了 KDE 的速度，发现它在相同的硬件上比 Windows 11 更快，并且与 MacBook Pro 上的 macOS 相媲美。虽然注意到由于多个显示器导致的任务栏放置出现了一个小问题，但作者最终得出结论，KDE 提供了他们在 Linux 上第一次真正令人愉快的桌面环境体验。他们赞扬 KDE 开发者创造了如此精致且功能丰富的体验。

---

## 41. 菲利珀零盖革计数器

**原文标题**: Flipper Zero Geiger Counter

**原文链接**: [https://kasiin.top/blog/2025-08-04-flipper_zero_geiger_counter_module/](https://kasiin.top/blog/2025-08-04-flipper_zero_geiger_counter_module/)

本文档介绍了两款用于与盖革计数器交互的 Flipper Zero 应用程序：标准盖革计数器应用程序和原子骰子滚动应用程序。两款应用程序都需要第三方固件（推荐 Unleashed 或 Momentum）。

盖革计数器应用程序以每秒计数 (CPS) 和每分钟计数 (CPM) 显示实时放射性测量值，并提供更改显示单位的选项（μSv/h、mSv/y 等）。它包括将数据记录到 CSV 文件（存储在 SD 卡上）、缩放图形和清除显示的功能。它还具有使用 A4 和 A7 GPIO 引脚的测试功能。按钮分配控制这些功能。该应用程序旨在检测贝塔射线和伽马射线，可用于测量各种来源的放射性，包括铀矿石、镭表盘、铀陶器和烟雾探测器中的镅。它指出 Sv 或 Rad 的测量值不精确，并根据发射的辐射类型提供了可用和不可用的放射源列表。

原子骰子滚动应用程序使用盖革计数器根据检测到的贝塔射线或伽马射线生成真正的随机数。它使用 CRC32（用于低活动）或 MD5（用于高活动）算法对来自这些检测的时间戳进行哈希处理。它使用生成的随机数提供掷骰子 (1-6) 或抛硬币 (0-1)。该应用程序在左角显示 CPS，在右角显示可用滚动次数。文章还包括一个免责声明，声明这两款应用程序仅用于教育目的，应负责任地在用户自己的设备上使用。

---

## 42. TernFS – 艾字节级，多区域分布式文件系统

**原文标题**: TernFS – An exabyte scale, multi-region distributed filesystem

**原文链接**: [https://www.xtxmarkets.com/tech/2025-ternfs/](https://www.xtxmarkets.com/tech/2025-ternfs/)

本文介绍了TernFS，一个由算法交易公司XTX开发的、定制的、EB级别、多区域分布式文件系统，旨在解决其不断增长的存储需求。由于现有解决方案存在局限性，XTX设计了TernFS来处理海量数据、高并发以及跨地理分散数据中心的冗余。

TernFS架构包含四个主要服务：元数据分片（管理目录结构和文件元数据）、跨目录协调器(CDC)（处理跨分片事务）、块服务（以块的形式存储文件内容）以及注册表（跟踪服务位置和状态）。该设计强调解耦，服务直接与客户端通信。元数据被分割成256个分片以实现可扩展性，CDC促进跨多个分片的事务。块服务利用标准TCP API进行文件读/写访问。注册表存储其他服务的位置数据。

TernFS的关键特性包括数据保护的冗余、元数据服务中无单点故障、文件快照、多区域支持、硬件无关性以及最小化的依赖集。虽然TernFS是为大型文件（中位数大小为2MB）和不可变数据设计的，但在目录创建/删除吞吐量方面存在局限性，并且是无权限的。目前，TernFS在多个数据中心存储超过500PB的数据，并在高峰时提供每秒数TB的数据服务。XTX已在GitHub上开源TernFS。

---

## 43. 发布 HN：Cactus (YC S25) – 智能手机上的AI推理

**原文标题**: Launch HN: Cactus (YC S25) – AI inference on smartphones

**原文链接**: [https://github.com/cactus-compute/cactus](https://github.com/cactus-compute/cactus)

Cactus (YC S25) 发布面向智能手机的节能型 AI 推理框架及内核，专为占据市场主导地位但常被现有优化工作忽略的经济型和中端设备设计。与现有框架不同，Cactus 从零开始构建，不依赖外部依赖项，因此适用于所有移动设备。

该框架采用分层架构，包括 Cactus FFI (OpenAI 兼容 C API)、用于 Transformer 推理的高级 Cactus 引擎、用于通用数值计算的统一零拷贝 Cactus 图，以及底层的 ARM 特定 SIMD Cactus 内核。这使得开发者能够在手机上实现自定义模型和科学计算任务，类似于 JAX。

Launch HN 重点介绍了易于集成性，并提供了示例代码片段，演示了 C++ 和通过 Foreign Function Interface 进行语言绑定的用法。

性能基准测试显示，Qwen3-600m-INT8 在旧款手机（Pixel 6a、Galaxy S21、iPhone 11 Pro）上实现了 16-20 t/s，在即将推出的旗舰型号（Pixel 9、Galaxy S25、iPhone 16）上实现了 50-70 t/s。在 Apple 芯片上，同一模型以 60-70 toks/秒的速度运行。

Cactus SDK 已经在生产环境中运行超过 50 万个每周推理任务。路线图包括支持更多模型（Gemma、SmolVLM 等），以及通过 SMMLA、NPU & DSP 实现高端手机的硬件加速，以及支持更大模型的 INT4。该公司建议传统计算机用户继续使用现有的 x86 优化推理解决方案，如 HuggingFace、Llama.cpp 等。

---

## 44. Show HN: Asxiv.org – 通过聊天提问 ArXiv 论文

**原文标题**: Show HN: Asxiv.org – Ask ArXiv papers questions through chat

**原文链接**: [https://asxiv.org/](https://asxiv.org/)

无法访问文章链接。

---

## 45. Luau - 快速、小巧、安全、渐进式类型的脚本语言，源自Lua。

**原文标题**: Luau – Fast, small, safe, gradually typed scripting language derived from Lua

**原文链接**: [https://luau.org/](https://luau.org/)

Luau是一种脚本语言，源自Lua 5.1，由Roblox开发，旨在满足其平台不断发展的需求，包括大型代码库、性能和工具。在努力保持与Lua 5.1的向后兼容性并融入更高版本的功能的同时，Luau在设计决策和用例不同的地方有所偏离。

Luau的主要特点包括：

*   **沙盒化：** Luau强制执行严格的沙盒化，以保护特权代码，限制用户编写的脚本对标准库的访问。
*   **语法扩展：** Luau引入了语法改进，以实现更好的用户体验，同时保持与Lua 5.1的兼容性。
*   **分析工具：** 内置的linting和类型检查工具（脚本分析）有助于识别和防止常见的编码错误。
*   **性能优先：** Luau具有自定义前端、新的字节码、与LuaJIT竞争的解释器以及可选的JIT编译器（x64/arm64），以优化运行时性能。
*   **库修改：** 虽然Luau在语言上是Lua 5.1的超集，但它修改了标准库，移除了一些函数并添加了其他函数。嵌入Luau的应用程序通常提供额外的、特定于应用程序的库。

本质上，Luau旨在成为一种快速、小巧、安全且逐渐类型的脚本语言，在保留Lua熟悉性的同时，满足Roblox环境的特定要求。

---

## 46. 西尔维娅·普拉斯的无花果树遇上机器学习

**原文标题**: Sylvia Plath's fig tree meets machine learning

**原文链接**: [https://dontlognow.substack.com/p/sylvia-plaths-fig-tree-meets-machine](https://dontlognow.substack.com/p/sylvia-plaths-fig-tree-meets-machine)

无法访问文章链接。

---

## 47. 守护生命的死亡射线

**原文标题**: The death rays that guard life

**原文链接**: [https://worksinprogress.co/issue/the-death-rays-that-guard-life/](https://worksinprogress.co/issue/the-death-rays-that-guard-life/)

本文论证了广泛采用远紫外线(far-UVC)作为改善室内空气质量和对抗空气传播疾病的关键工具，并将其与水过滤和氯化在根除水传播疾病方面的历史性成功相提并论。

文章强调了历史背景，指出伤寒流行促成了有效的水净化方法，但肺结核和COVID-19等空气传播疾病并未受到同等重视。 传统的杀菌紫外线（254nm）有效，但存在健康风险，随着抗生素的兴起而逐渐衰落。

远紫外线（特别是222nm）提供了一种更安全的替代方案。 由于其短波长和有限的穿透力，它可以有效地使病原体失效，而不会损害人体皮肤或眼睛。 研究表明，它可以有效降低占用空间中的空气病毒浓度。

文章承认了通风和过滤等替代空气净化方法，但强调了它们的局限性。 通风能源消耗大，并且可能引入受污染或温度不适宜的空气。 过滤也需要能源，并且成本可能很高。 远紫外线凭借其定向消毒，可以克服这些局限性。

虽然远紫外线系统最初可能比过滤更昂贵，但文章认为，更安全的室内空气带来的长期益处证明了这项投资是合理的，并提倡将其整合到公共场所，以保护公众健康免受空气传播威胁。

---

## 48. OpenTelemetry Collector：它是什么，何时需要，何时不需要

**原文标题**: OpenTelemetry collector: What it is, when you need it, and when you don't

**原文链接**: [https://oneuptime.com/blog/post/2025-09-18-what-is-opentelemetry-collector-and-why-use-one/view](https://oneuptime.com/blog/post/2025-09-18-what-is-opentelemetry-collector-and-why-use-one/view)

本文介绍了 OpenTelemetry (OTel) Collector，一个厂商中立的遥测流水线，它接收、处理和导出来自应用程序的遥测数据（链路、指标、日志）到诸如 OneUptime 的后端。文章对比了直接导出（应用程序直接发送数据到后端）和使用中央 Collector 的方式。

直接导出对于小型应用来说更简单，但缺乏集中式策略控制，使得厂商迁移、成本优化和安全性更加困难。Collector 集中配置采样、数据清理、丰富、路由到多个目的地，并提供安全边界。虽然增加了一个额外的组件，但它将应用程序与厂商解耦，并处理扩展压力。

Collector 使用接收器（摄取数据）、处理器（转换、批处理、采样）、导出器（发送到后端）和扩展（身份验证、健康检查），通过管道连接。文章提供了一个管道配置的 YAML 示例。

Collector 对于尾部采样、多目的地路由、敏感数据剥离、成本治理、厂商独立性、网络隔离和中央重试至关重要。对于遥测需求有限的小型简单应用程序，可以跳过它。

至关重要的是，Collector 通过批处理数据、丢弃低价值 span、尾部采样、剥离属性以及在导出前聚合指标来优化成本。监控 Collector 的内部指标对于性能和故障排除至关重要。Collector 充当遥测的控制平面，从而能够高效地管理和存储可观测性数据。

---

## 49. 鸡尾酒会创意

**原文标题**: Cocktail Party Ideas

**原文链接**: [https://danluu.com/cocktail-ideas/](https://danluu.com/cocktail-ideas/)

本文批判了一种现象：人们对某个主题仅有肤浅的了解，却在复杂问题上提出过于简化的解决方案，尤其是在社交场合。作者观察到，这种情况经常发生在诸如搜索引擎开发和交通建设等热门话题上，这些人自信地提出解决方案，却不了解潜在的挑战和子问题。

作者认为，核心问题在于人们假设有限的理解反映了该领域的全部复杂性。这导致了最终不切实际的“鸡尾酒会式解决方案”。作者以程序员对“传统”工程领域提出天真的看法为例，来说明这一点。

本文强调了流行程序员的认知与工程师面临的现实之间的差异，指出人们常常高估自己领域之外的领域的简单性。通过将土木工程（桥梁建设）与软件开发进行比较，作者认为每个领域都有独特的约束和复杂性，而这些约束和复杂性常常被外行人忽视。

作者最后强调了大型项目固有的复杂性以及所涉及的众多相互作用的子领域。他将此与基于不完全理解而轻松创建简单解决方案形成对比，并引用了一项关于人们对自行车工作原理的错误理解以及“选择悖论”研究的错误应用的研究。文章倡导在提出解决方案之前，应更深入地了解不同领域中的复杂性。

---

## 50. Pnpm 有了一个新设置来防范供应链攻击

**原文标题**: Pnpm has a new setting to stave off supply chain attacks

**原文链接**: [https://pnpm.io/blog/releases/10.16](https://pnpm.io/blog/releases/10.16)

本文重点介绍 pnpm 包管理器中的新特性和修复，着重关注安全增强和改进的依赖管理。

一项关键的新特性是 `minimumReleaseAge` 设置，旨在通过延迟安装新发布的依赖项来缓解供应链攻击。这为检测和从注册表中删除恶意版本留出了时间。该设置指定要安装的依赖项的最小存在时间（以分钟为单位），`minimumReleaseAgeExclude` 设置允许例外，以便始终安装特定软件包的最新版本。

本文还介绍了“查找器函数”，用于使用 `pnpm list` 和 `pnpm why` 命令进行高级依赖项过滤。这些在 `.pnpmfile.cjs` 中定义的函数，能够基于名称和版本之外的属性搜索依赖项（例如，查找在其对等依赖项中具有特定 React 版本的包）。查找器函数还可以从包清单返回附加信息，以便在输出中显示。

最后，本文指出了一些补丁更改，包括修复 Node.js 24 中的弃用警告、强制执行 `nodeVersion` 设置的精确语义版本、使 `pnpm publish` 能够处理 `.tar.gz` 文件，以及确保在使用 Ctrl-C 取消进程时返回正确的退出代码。

---

## 51. TIC-80 – 迷你电脑

**原文标题**: TIC-80 – Tiny Computer

**原文链接**: [https://tic80.com/](https://tic80.com/)

TIC-80是一款免费开源的梦幻计算机，专为创作、游玩和分享迷你复古风格游戏而设计。它提供了内置工具，涵盖游戏开发的各个方面，包括代码编辑器、精灵编辑器、地图编辑器、声音编辑器和命令行界面。目标是创建一个完整的迷你游戏，输出一个可以在网站上存储和游玩的卡带文件，或者打包成适用于各种平台的独立播放器。

该平台强制执行类似于复古游戏机的技术限制，例如240x136像素的显示屏、16色调色板、有限数量的精灵和4声道声音，鼓励在约束条件下进行创造性的问题解决。

文章还重点介绍了使用TIC-80创建的几个“最新热门游戏”（carts），展示了该平台上各种可能的项目，从射击游戏和冒险游戏到重制游戏和简单演示。提及的例子包括“Retro Gunner”、“Orbit Defender”、“A Story for the Night”和“Pacman 80”等。文章邀请用户查看所有可用的游戏。

---

## 52. 北美洲中世纪餐厅餐垫

**原文标题**: Midcentury North American Restaurant Placemats

**原文链接**: [https://casualarchivist.substack.com/p/order-up](https://casualarchivist.substack.com/p/order-up)

无法访问文章链接。

---

## 53. 悲伤如同我们，终有期限。

**原文标题**: Grief gets an expiration date, just like us

**原文链接**: [https://bessstillman.substack.com/p/oh-fuck-youre-still-sad](https://bessstillman.substack.com/p/oh-fuck-youre-still-sad)

无法访问文章链接。

---

## 54. 展示一下：我做了一个关于蚂蚁的小型2D游戏

**原文标题**: Show HN: I created a small 2D game about an ant

**原文链接**: [https://aanthonymax.github.io/ant-and-apples/](https://aanthonymax.github.io/ant-and-apples/)

此Show HN帖子展示了一款简单的2D游戏“蚂蚁与苹果”，玩家通过方向键控制蚂蚁收集所有苹果。游戏的目标是帮助蚂蚁填饱肚子。开发者aanthonymax出于无聊，并利用几天时间，部分使用hmpl-js创建了这款小项目。帖子还提供了游戏GitHub仓库的链接：https://github.com/aanthonymax/ant-and-apples。

---

## 55. 我曾是个怪小孩：少年黑客的监狱自白

**原文标题**: I Was a Weird Kid: Jailhouse Confessions of a Teen Hacker

**原文链接**: [https://www.bloomberg.com/news/features/2025-09-19/multimillion-dollar-hacking-spree-scattered-spider-teen-s-jailhouse-confessions](https://www.bloomberg.com/news/features/2025-09-19/multimillion-dollar-hacking-spree-scattered-spider-teen-s-jailhouse-confessions)

文章《我曾是个怪异的孩子：少年黑客的狱中忏悔》详细讲述了一个名叫“T”的青少年与臭名昭著的黑客组织“分散蜘蛛”扯上关系的故事。这篇文章基于狱中采访，描绘了一个不善社交、孤立无援的年轻人，在黑客组织的犯罪活动中找到了认同感和目标感。

T回忆了他早期对计算机的迷恋，以及他从无害的黑客行为发展到日益复杂和有利可图的网络犯罪的过程。他描述了“分散蜘蛛”如何招募他和其他人，强调了该组织的等级结构和激励他们的经济利益。该组织以大型企业为目标，窃取数据并勒索数百万美元。

这篇文章强调了这些黑客行为造成的毁灭性影响，不仅对目标公司，也对个人信息被泄露的个人造成了影响。文章还深入探讨了可能导致T参与网络犯罪的心理因素，探讨了孤立、归属感以及网络黑客社区中权力和地位的诱惑等主题。

叙述跟随了T最终被捕以及他在狱中反思过去行为的过程。这篇文章提出了关于科技公司是否有责任更好地保护自己免受此类攻击，以及是否需要改进针对参与网络犯罪的年轻罪犯的改造计划的问题。最终，它描绘了一个被自己编织的网困住的复杂个体，努力应对自己选择的后果，并对高风险网络犯罪的世界进行了令人不寒而栗的描述。

---

## 56. XKB配置不可靠指南

**原文标题**: An Unreliable Guide to XKB Configuration

**原文链接**: [https://www.charvolant.org/doug/xkb/html/xkb.html](https://www.charvolant.org/doug/xkb/html/xkb.html)

道格·帕尔默所著的《XKB配置不可靠指南》旨在阐释使用XKB系统配置键盘的复杂性。作者坦承缺乏专业知识，因此本文可视为他为了理解该主题而撰写的自学指南。

该文档似乎是XKB的全面概述，从修饰键、层、组、键码和键符号等基础知识入手。它概述了选择XKB配置的各种方法，从简单、用户友好的方法到涉及直接操作配置文件的更复杂、更手动的方法。

文档的很大一部分致力于XKB配置文件，分解了键码、符号、组和层处理、修饰符、控制键、特殊字符、死键、ISO键、组合键、类型、兼容性映射和几何结构等不同方面。它还通过目录文件、分组组件、语义、键映射和规则来阐述XKB的组织结构。

该文档进一步涉及XKB程序，并通过详细介绍Happy Hacking Keyboard Lite的配置来提供一个实际示例。最后，它以参考书目和关于文档本身的信息作为结尾。虽然标榜“不可靠”，但该文档似乎致力于对XKB键盘配置进行彻底（即使可能存在缺陷）的探索。

---

## 57. 嫌疑人要求“律师，狗”，罔顾事实法庭拒绝逗号和律师

**原文标题**: Suspect Asks for a 'Lawyer, Dog,' Willfully Ignorant Court Denies Comma, Counsel

**原文链接**: [https://abovethelaw.com/2017/10/suspect-asks-for-a-lawyer-dog-willfully-ignorant-court-denies-comma-counsel/](https://abovethelaw.com/2017/10/suspect-asks-for-a-lawyer-dog-willfully-ignorant-court-denies-comma-counsel/)

埃利·米斯塔尔在他的“Above the Law”文章中指责路易斯安那州最高法院故意剥夺了一位非裔美国人刑事被告沃伦·德梅斯梅获得律师的宪法权利。德梅斯梅在警方讯问期间要求律师，他说：“要不你给我找个律师狗吧，因为这事不对劲。”

法院以8比1的裁决认为德梅斯梅的要求含糊不清，特别强调了“律师狗”的措辞。米斯塔尔认为，法院是在故意曲解德梅斯梅的陈述，声称他实际上说的是“律师，伙计（lawyer, dawg）”，这是一个明确的法律代表要求。他指责法院利用对“狗”的误解来制造原本不存在的歧义，从而为拒绝德梅斯梅获得律师的权利辩护。

米斯塔尔进一步辩称，即使接受法院不正确的笔录，警方也应该做出合理的反应，即澄清德梅斯梅的要求，或者讽刺地去找一只拥有法学学位的狗，而不是在没有法律代表的情况下继续审讯。他断言，法院的行为根植于种族偏见，反映了路易斯安那州系统性地剥夺黑人被告权利的模式。他最后指出，涉案法官应该感到羞耻，但他们可能不会，因为他们认为这种行为是他们工作的一部分。

---

## 58. 灾难数学

**原文标题**: The Math of Catastrophe

**原文链接**: [https://www.quantamagazine.org/the-math-of-climate-change-tipping-points-20250915/](https://www.quantamagazine.org/the-math-of-climate-change-tipping-points-20250915/)

格雷戈里·巴伯的文章《灾难的数学》探讨了气候科学中关于临界点复杂性和不确定性，特别是数学家试图对其进行建模和预测时所面临的问题。文章强调了历史背景，提及米哈伊尔·布迪科的雪球地球模型以及对核冬天的恐惧，以说明剧烈气候转变的可能性。

文章讨论了将数学模型应用于地球气候所面临的挑战，地球气候远比彼得湖等简化系统复杂，生态学家通过关注关键变量成功预测了彼得湖的体制转变。文章指出，由于过度简化和在复杂社会系统建模中不切实际的假设，“突变理论”最初备受推崇，随后遭到摒弃。

尽管存在挑战，数学家们仍在寻求使临界点预测更有用的方法。分岔的概念，即渐进的变化导致突然的转变，是理解这些临界点的关键。蒂姆·伦顿推广了“临界点”一词，以更好地传达气候变化的紧迫性。文章还强调了在数学严谨性和实际应用之间取得平衡的重要性，承认现有数据的局限性以及模型可能对初始假设过于敏感。在承认不确定性的同时，文章强调了使用数学来理解并可能缓解灾难性气候情景的重要性。

---

## 59. 从 1970 年代至今的消费者美学视觉词典

**原文标题**: Visual lexicon of consumer aesthetics from the 1970s until now

**原文链接**: [https://cari.institute/](https://cari.institute/)

无法访问文章链接。

---

## 60. 这个网站毫无品味。

**原文标题**: This website has no class

**原文链接**: [https://aaadaaam.com/notes/no-class/](https://aaadaaam.com/notes/no-class/)

作者在一篇自我反思的文章中描述了他们重构网站以消除CSS类的方法，旨在实现更简洁、更语义化的方法。受他们自己先前关于将HTML元素视为预构建组件的建议的启发，他们挑战自己构建网站而不依赖于类。

作者最初尝试广泛使用上下文样式，嵌套选择器并使用`:where()`和`:has()`，但发现这种方法变得过于复杂和深奥。然后，他们转向自定义标签和属性，利用Web组件的模式而不使用JavaScript。这涉及到使用自定义元素名称（如`<note-pad>`）和自定义属性（如`shape-type="1"`）来应用样式，用键值对替换BEM修饰符的功能。

作者发现了一些积极的结果，包括CSS大小的减少以及由于更加关注语义标记而提高的可访问性。标记也变得更干净、更易读。然而，这种方法需要更仔细的规划和对网站的整体观察，使其可能不太适合具有多样化前端技能水平的大型项目。

虽然承认自定义标签和属性在某种程度上是“重新发明”类，但作者认为这种方法感觉更连贯，并且可以无缝增强为真正的Web组件。尽管作者并没有完全确信这是最终的解决方案，但他们相信这个实验将极大地影响他们未来的工作。由于实际限制，他们最终只保留了用于语法高亮插件的类。

---

## 61. 渔夫和他的妻子 (1857)

**原文标题**: The Fisherman and His Wife (1857)

**原文链接**: [https://sites.pitt.edu/~dash/grimm019.html](https://sites.pitt.edu/~dash/grimm019.html)

渔夫和他的妻子：一个关于无度贪婪和野心的警示故事。渔夫捕获了一条神奇的比目鱼，比目鱼答应用满足愿望来换取自由。渔夫的妻子伊尔斯比尔，最初对他们贫困的生活感到满足，但她却迫使丈夫向比目鱼索要越来越奢侈的愿望。

从用一个简陋的茅屋来代替他们肮脏的小屋开始，伊尔斯比尔的野心迅速升级。她要求一座宫殿，然后成为国王，然后是皇帝，最后是教皇。每一个愿望都实现了，但随着每一次满足，大海变得更加汹涌，反映了伊尔斯比尔永不满足的欲望所造成的日益增长的混乱和道德沦丧。

渔夫最初犹豫不决，但渐渐地，他越来越为妻子的要求感到苦恼，认识到这些要求的内在错误。他继续服从她，但内心沉重，预感到厄运即将来临。

最终，伊尔斯比尔的野心没有止境。她宣称她想变得像上帝一样，控制太阳和月亮。这最后一个离谱的要求打破了魔法。比目鱼厌倦了她无情的贪婪，收回了之前所有的礼物。故事的结尾是这对夫妇回到了他们最初肮脏的小屋，这鲜明地提醒人们无度野心的危险以及知足的重要性。

---

## 62. 英国侦探小说的兴衰 (2010)

**原文标题**: The Rise and Fall of the British Detective Novel (2010)

**原文链接**: [https://www.historytoday.com/archive/feature/rise-and-fall-british-detective-novel](https://www.historytoday.com/archive/feature/rise-and-fall-british-detective-novel)

威廉·鲁宾斯坦的《英国侦探小说的兴衰》探讨了该类型的“黄金时代”（1910-1950）、其起源以及其衰落。他认为埃德加·爱伦·坡和亚瑟·柯南·道尔（及夏洛克·福尔摩斯）确立了侦探小说的地位，并指出福尔摩斯对后世作家产生了重大影响。这些故事通常以社会上层阶级为背景，与现实世界的犯罪形成对比，并侧重于聪明的业余侦探智胜苏格兰场。

这篇文章重点介绍了塞西尔·斯特里特、弗里曼·威尔斯·克罗夫茨和多萝西·L·塞耶斯等杰出的“黄金时代”英国侦探小说家，强调了他们的中产阶级出身和受众。这些小说反映了两次世界大战期间英国中产阶级的价值观，如理性、正义和特定的社会偏见。

鲁宾斯坦将英国侦探小说与美国“硬汉派”类型进行对比，后者以达希尔·哈米特和雷蒙德·钱德勒为代表，其特点是暴力、反权威主义和左翼政治议程，这些在更保守的英国作品中是缺失的。

文章认为，古典英国侦探小说在1960年左右衰落，原因包括情节耗尽、社会对性和暴力态度的转变、间谍惊悚片（詹姆斯·邦德）的兴起，以及英国社会对理性、正义和惩罚确定性的核心信念的瓦解。它表明了该类型与英国历史和社会转型之间的联系。

---

## 63. TBM 377：时间分配 ≠ 能力分配

**原文标题**: TBM 377: Time Allocation ≠ Capacity Allocation

**原文链接**: [https://cutlefish.substack.com/p/tbm-377-time-allocation-capacity](https://cutlefish.substack.com/p/tbm-377-time-allocation-capacity)

文章《TBM 377：时间分配 ≠ 能力分配》认为，简单地为任务分配时间并不能保证这些任务能够有效完成或达到预期结果。文章强调了分配时间与分配*能力*之间的关键区别。

核心论点是，仅仅安排会议或设定截止日期并不能自动转化为高效的工作。精力水平、注意力、干扰、先验知识以及任务的复杂性等因素都会影响在分配的时间内可用于高效工作的实际*能力*。

作者举例说明，比如安排一个小时写作，但由于缺乏专注力，却花了一半的时间盯着空白屏幕，或者在真正开始写作任务之前需要先研究一个主题。 这说明所分配的时间并不能反映实际使用的*能力*。

文章建议关注管理*能力*，而不是仅仅管理时间。 这包括了解你的最佳表现时间、减少干扰、将复杂的任务分解成更小、更易于管理的块，并在开始任务之前确保你拥有必要的资源和知识。

最终，文章提倡一种更全面的生产力方法，承认时间是一种资源，但不是影响产出的唯一因素。 成功完成任务不仅依赖于有效分配和管理时间，还依赖于有效分配和管理执行任务所需的精神、情感和身体*能力*。

---

## 64. 蓝鳍 LTS 发布

**原文标题**: Bluefin LTS Is Released

**原文链接**: [https://docs.projectbluefin.io/blog/bluefin-lts-ga/](https://docs.projectbluefin.io/blog/bluefin-lts-ga/)

基于 CentOS Stream 10 的 Bluefin LTS 和 Bluefin GDX 现已正式发布。Bluefin LTS 提供现代桌面体验，具有长期支持（每个版本 3-5 年），并具备一流的 Flathub 支持、Homebrew、ZFS 和反向移植的 GNOME 48 桌面等功能。它包含一个可选的硬件启用 (HWE) 分支，其中包含更新的 Linux 内核，可通过 `ujust rebase-helper` 和适用于较新硬件的专用 ISO 访问。

Bluefin GDX 设计为 AI 工作站，集成了 Nvidia 驱动程序和 CUDA，并包含 VSCode 集成、用于 AI 模型管理的 Ramalama 以及用于 Python 包管理的 uv 等功能。它是与 Red Hat Enterprise Linux Command Line Assistant 团队合作开发的，专注于开源 AI/ML 工具。

该版本强调开发者的可持续性，Bluefin LTS 的更新频率低于其他 Bluefin 版本。文章还讨论了 Bluefin GTS 的未来，由于与 Bluefin LTS HWE 重叠，可能会从网站上隐藏。新的 Anaconda webui 正被用于安装，更新将于每周二发布。Bluefin LTS 和 GDX 的下载均已提供，并附带校验和以供验证。该团队还推出了一个新的 Bluefin 商店，销售商品以支持古生物艺术。

---

## 65. Tldraw SDK 4.0

**原文标题**: Tldraw SDK 4.0

**原文链接**: [https://tldraw.dev/blog/tldraw-sdk-4-0](https://tldraw.dev/blog/tldraw-sdk-4-0)

Tldraw SDK 4.0 has been released, featuring new starter kits, accessibility improvements, and licensing changes. The release introduces a new CLI tool (`npm create tldraw@latest`) for creating projects using templates and starter kits. These starter kits include: agent (chatbot), workflow (node-and-wire apps), branching chat (AI chats), chat (image annotation for chatbots), and multiplayer (multiplayer backend via tldraw sync). All starter kits are MIT licensed.

Licensing has been updated, requiring either a trial, commercial, or hobby license for production environments. The SDK is free for development environments. A free 100-day trial license is available, and commercial license sign-ups before the end of 2025 will receive a discount based on the remaining trial period.

The SDK now complies with WCAG 2.2 AA accessibility standards, benefiting downstream users. Tldraw encourages users to explore the new features via `npm create tldraw@latest` or the tldraw.dev website. The project has achieved significant milestones, including 40,000 GitHub stars, 70,000 weekly installs, and a $10M series A funding. Tldraw is also actively hiring.


---

## 66. Aaron Levie: Startups win in the AI era [video]

**原文标题**: Aaron Levie: Startups win in the AI era [video]

**原文链接**: [https://www.youtube.com/watch?v=uqc_vt95GJg](https://www.youtube.com/watch?v=uqc_vt95GJg)

生成摘要时出错

---

## 67. WASM 3.0 Completed

**原文标题**: WASM 3.0 Completed

**原文链接**: [https://webassembly.org/news/2025-09-17-wasm-3.0/](https://webassembly.org/news/2025-09-17-wasm-3.0/)

生成摘要时出错

---

## 68. When Knowing Someone at Meta Is the Only Way to Break Out of "Content Jail"

**原文标题**: When Knowing Someone at Meta Is the Only Way to Break Out of "Content Jail"

**原文链接**: [https://www.eff.org/pages/when-knowing-someone-meta-only-way-break-out-content-jail](https://www.eff.org/pages/when-knowing-someone-meta-only-way-break-out-content-jail)

生成摘要时出错

---

## 69. PostgreSQL Maintenance Without Superuser

**原文标题**: PostgreSQL Maintenance Without Superuser

**原文链接**: [https://boringsql.com/posts/postgresql-predefined-roles/](https://boringsql.com/posts/postgresql-predefined-roles/)

生成摘要时出错

---

## 70. iTerm2 网页浏览器

**原文标题**: iTerm2 Web Browser

**原文链接**: [https://iterm2.com/documentation-web.html](https://iterm2.com/documentation-web.html)

生成摘要时出错

---

## 71. 美国草原保护区在蒙大拿州新增7万英亩土地

**原文标题**: American Prairie unlocks another 70k acres in Montana

**原文链接**: [https://earthhope.substack.com/p/victory-for-public-access-american](https://earthhope.substack.com/p/victory-for-public-access-american)

Unable to access the article link.


---

## 72. The quality of AI-assisted software depends on unit of work management

**原文标题**: The quality of AI-assisted software depends on unit of work management

**原文链接**: [https://blog.nilenso.com/blog/2025/09/15/ai-unit-of-work/](https://blog.nilenso.com/blog/2025/09/15/ai-unit-of-work/)

生成摘要时出错

---

## 73. 苹果照片应用损坏图像

**原文标题**: Apple Photos app corrupts images

**原文链接**: [https://tenderlovemaking.com/2025/09/17/apple-photos-app-corrupts-images/](https://tenderlovemaking.com/2025/09/17/apple-photos-app-corrupts-images/)

生成摘要时出错

---

## 74. Fast Fourier Transforms Part 1: Cooley-Tukey

**原文标题**: Fast Fourier Transforms Part 1: Cooley-Tukey

**原文链接**: [https://connorboyle.io/2025/09/11/fft-cooley-tukey.html](https://connorboyle.io/2025/09/11/fft-cooley-tukey.html)

Connor Boyle's article, "Fast Fourier Transforms Part 1: Cooley-Tukey," provides an introduction to the Cooley-Tukey algorithm, a widely used method for efficiently computing the Discrete Fourier Transform (DFT). The DFT transforms a sequence of complex numbers into its frequency components.

The article begins by defining the DFT and introducing the notation \(W_N\) to simplify complex exponentiation. It explains that a naive DFT implementation has a time complexity of \(O(\lvert x \rvert^2)\), where \(|x|\) is the length of the input sequence.

The Cooley-Tukey algorithm improves this by exploiting the composite nature of the input length (\(\lvert x \rvert = r \cdot d\)), breaking down the single DFT summation into nested summations. This allows splitting the input sequence into subsequences \(x_r^{j_0}\) based on modulo classes. By recursively applying this decomposition, particularly when the input length is a power of 2 (\(\lvert x \rvert = 2^n\)), the algorithm achieves a significantly faster time complexity of \(O (\lvert x \rvert \cdot \log(\lvert x \rvert))\).

The article also notes that the Cooley-Tukey algorithm can be adapted for inverse DFT calculations and highlights its limitations with prime-length inputs, suggesting the need for algorithms like Bluestein's for broader applicability. The author includes an interactive visualization to illustrate the Cooley-Tukey process. Finally, Boyle expresses frustration with the common misuse of "FFT" to mean "DFT," clarifying that FFT refers to the *algorithm* used to compute the DFT, not the result itself.


---

## 75. Classic recessive-or-dominant gene dynamics may not be so simple

**原文标题**: Classic recessive-or-dominant gene dynamics may not be so simple

**原文链接**: [https://news.stanford.edu/stories/2025/09/classic-recessive-dominant-gene-dynamics-pesticide-resistance-research](https://news.stanford.edu/stories/2025/09/classic-recessive-dominant-gene-dynamics-pesticide-resistance-research)

生成摘要时出错

---

## 76. Meta Ray-Ban Display

**原文标题**: Meta Ray-Ban Display

**原文链接**: [https://www.meta.com/blog/meta-ray-ban-display-ai-glasses-connect-2025/](https://www.meta.com/blog/meta-ray-ban-display-ai-glasses-connect-2025/)

生成摘要时出错

---

## 77. Show HN: The text disappears when you screenshot it

**原文标题**: Show HN: The text disappears when you screenshot it

**原文链接**: [https://unscreenshottable.vercel.app/?text=Hello](https://unscreenshottable.vercel.app/?text=Hello)

生成摘要时出错

---

## 78. EU ministers reach 'compromise' on digital euro roadmap

**原文标题**: EU ministers reach 'compromise' on digital euro roadmap

**原文链接**: [https://www.reuters.com/business/finance/eu-ministers-seek-agreement-digital-euro-be-independent-visa-mastercard-2025-09-19/](https://www.reuters.com/business/finance/eu-ministers-seek-agreement-digital-euro-be-independent-visa-mastercard-2025-09-19/)

生成摘要时出错

---

## 79. Show HN: One prompt generates an app with its own database

**原文标题**: Show HN: One prompt generates an app with its own database

**原文链接**: [https://www.manyminiapps.com/](https://www.manyminiapps.com/)

生成摘要时出错

---

## 80. Nvmath-Python: Nvidia Math Libraries for the Python Ecosystem

**原文标题**: Nvmath-Python: Nvidia Math Libraries for the Python Ecosystem

**原文链接**: [https://github.com/NVIDIA/nvmath-python](https://github.com/NVIDIA/nvmath-python)

生成摘要时出错

---

## 81. Automatic differentiation can be incorrect

**原文标题**: Automatic differentiation can be incorrect

**原文链接**: [https://www.stochasticlifestyle.com/the-numerical-analysis-of-differentiable-simulation-automatic-differentiation-can-be-incorrect/](https://www.stochasticlifestyle.com/the-numerical-analysis-of-differentiable-simulation-automatic-differentiation-can-be-incorrect/)

生成摘要时出错

---

## 82. 已绘制：6千次火箭发射

**原文标题**: Mapped: 6k Rocket Launches

**原文链接**: [https://www.maps.com/6000-rocket-launches-mapped/](https://www.maps.com/6000-rocket-launches-mapped/)

生成摘要时出错

---

## 83. Stepping Down as Libxml2 Maintainer

**原文标题**: Stepping Down as Libxml2 Maintainer

**原文链接**: [https://discourse.gnome.org/t/stepping-down-as-libxml2-maintainer/31398](https://discourse.gnome.org/t/stepping-down-as-libxml2-maintainer/31398)

The maintainer of libxml2 is stepping down, effectively leaving the project unmaintained for the foreseeable future. While full support is ending, the maintainer will continue to address regressions specifically in the 2.15 release until the end of 2025. This means that no new features, enhancements, or bug fixes (beyond regressions in 2.15) are expected, and the project's long-term stability and development are uncertain without a new maintainer.


---

## 84. Russian warplanes breach NATO airspace over Estonia

**原文标题**: Russian warplanes breach NATO airspace over Estonia

**原文链接**: [https://www.politico.eu/article/russian-fighter-jets-breach-estonian-airspace-near-tallinn/](https://www.politico.eu/article/russian-fighter-jets-breach-estonian-airspace-near-tallinn/)

生成摘要时出错

---

## 85. Orange Pi RV2 $40 RISC-V SBC: Friendly Gateway to IoT and AI Projects

**原文标题**: Orange Pi RV2 $40 RISC-V SBC: Friendly Gateway to IoT and AI Projects

**原文链接**: [https://riscv.org/ecosystem-news/2025/09/orange-pi-rv2-40-risc-v-sbc-friendly-gateway-to-iot-and-ai-projects/](https://riscv.org/ecosystem-news/2025/09/orange-pi-rv2-40-risc-v-sbc-friendly-gateway-to-iot-and-ai-projects/)

生成摘要时出错

---

## 86. Daily Aspirin intake slashes colon cancer relapse risk by 55%

**原文标题**: Daily Aspirin intake slashes colon cancer relapse risk by 55%

**原文链接**: [https://news.ki.se/common-inexpensive-drug-halves-recurrence-in-colorectal-cancer](https://news.ki.se/common-inexpensive-drug-halves-recurrence-in-colorectal-cancer)

生成摘要时出错

---

## 87. The Asus gaming laptop ACPI firmware bug

**原文标题**: The Asus gaming laptop ACPI firmware bug

**原文链接**: [https://github.com/Zephkek/Asus-ROG-Aml-Deep-Dive](https://github.com/Zephkek/Asus-ROG-Aml-Deep-Dive)

生成摘要时出错

---

## 88. Hypervisor 101 in Rust

**原文标题**: Hypervisor 101 in Rust

**原文链接**: [https://tandasat.github.io/Hypervisor-101-in-Rust/](https://tandasat.github.io/Hypervisor-101-in-Rust/)

生成摘要时出错

---

## 89. Apollo laser takes down 200 drones unplugged

**原文标题**: Apollo laser takes down 200 drones unplugged

**原文链接**: [https://newatlas.com/military/apollo-laser-drones-weapon/](https://newatlas.com/military/apollo-laser-drones-weapon/)

生成摘要时出错

---

## 90. I Built an Event-Sourcing Database Engine: Meet Genesis DB

**原文标题**: I Built an Event-Sourcing Database Engine: Meet Genesis DB

**原文链接**: [https://www.genesisdb.io](https://www.genesisdb.io)

生成摘要时出错

---

## 91. Tinycolor supply chain attack post-mortem

**原文标题**: Tinycolor supply chain attack post-mortem

**原文链接**: [https://sigh.dev/posts/ctrl-tinycolor-post-mortem/](https://sigh.dev/posts/ctrl-tinycolor-post-mortem/)

生成摘要时出错

---

## 92. What's New in C# 14: Null-Conditional Assignments

**原文标题**: What's New in C# 14: Null-Conditional Assignments

**原文链接**: [https://blog.ivankahl.com/csharp-14-null-conditional-assignments/](https://blog.ivankahl.com/csharp-14-null-conditional-assignments/)

生成摘要时出错

---

## 93. Keeping SSH sessions alive with systemd-inhibit

**原文标题**: Keeping SSH sessions alive with systemd-inhibit

**原文链接**: [https://kd8bny.com/posts/session_inhibit/](https://kd8bny.com/posts/session_inhibit/)

生成摘要时出错

---

## 94. CERN Animal Shelter for Computer Mice (2011)

**原文标题**: CERN Animal Shelter for Computer Mice (2011)

**原文链接**: [https://computer-animal-shelter.web.cern.ch/index.shtml](https://computer-animal-shelter.web.cern.ch/index.shtml)

生成摘要时出错

---

## 95. Meta’s live demo fails; “AI” recording plays before the actor takes the steps

**原文标题**: Meta’s live demo fails; “AI” recording plays before the actor takes the steps

**原文链接**: [https://www.reddit.com/r/LivestreamFail/comments/1nkbig7/metas_live_staged_demo_fails_the_ai_recording/](https://www.reddit.com/r/LivestreamFail/comments/1nkbig7/metas_live_staged_demo_fails_the_ai_recording/)

生成摘要时出错

---

## 96. Launch HN: RunRL (YC X25) – Reinforcement learning as a service

**原文标题**: Launch HN: RunRL (YC X25) – Reinforcement learning as a service

**原文链接**: [https://runrl.com](https://runrl.com)

生成摘要时出错

---

## 97. Chandra finds black hole that's growing at 2.4 times the Eddington limit

**原文标题**: Chandra finds black hole that's growing at 2.4 times the Eddington limit

**原文链接**: [https://phys.org/news/2025-09-chandra-black-hole-eddington-limit.html](https://phys.org/news/2025-09-chandra-black-hole-eddington-limit.html)

生成摘要时出错

---

## 98. Configuration files are user interfaces

**原文标题**: Configuration files are user interfaces

**原文链接**: [https://ochagavia.nl/blog/configuration-files-are-user-interfaces/](https://ochagavia.nl/blog/configuration-files-are-user-interfaces/)

生成摘要时出错

---

## 99. DeepMind and OpenAI win gold at ICPC

**原文标题**: DeepMind and OpenAI win gold at ICPC

**原文链接**: [https://codeforces.com/blog/entry/146536](https://codeforces.com/blog/entry/146536)

生成摘要时出错

---

## 100. Slow social media

**原文标题**: Slow social media

**原文链接**: [https://herman.bearblog.dev/slow-social-media/](https://herman.bearblog.dev/slow-social-media/)

生成摘要时出错

---

