# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-09-19.md)

*最后自动更新时间: 2025-09-19 17:45:44*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 2 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 3 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 4 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 5 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 6 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 7 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 8 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 9 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 10 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 11 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 12 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 13 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 14 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 15 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 16 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 17 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 18 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 19 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 20 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 21 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 22 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 23 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 24 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 25 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 26 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 27 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 28 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 29 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 30 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 31 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 32 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 33 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 34 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 35 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 36 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 37 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 38 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 39 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 40 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 41 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 42 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 43 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 44 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 45 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 46 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 47 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 48 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 49 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 50 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 51 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 52 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 53 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 54 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 55 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 56 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 57 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 58 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 59 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 60 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 61 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 62 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 63 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 64 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 65 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 66 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 67 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 68 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 69 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 70 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 71 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 72 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 73 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 74 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 75 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 76 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 77 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 78 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 79 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 80 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 81 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 82 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 83 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 84 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 85 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 86 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 87 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 88 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 89 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 90 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 91 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 92 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 93 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 94 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 95 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 96 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 97 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 98 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 99 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 100 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 101 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 102 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 103 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 104 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 105 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 106 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 107 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 108 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 109 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 110 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 111 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 112 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 113 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 114 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 115 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 116 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 117 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 118 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 119 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 120 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 121 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 122 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 123 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 124 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 125 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 126 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 127 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 128 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 129 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 130 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 131 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 132 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 133 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 134 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 135 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 136 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 137 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 138 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 139 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 140 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 141 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 142 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 143 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 144 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 145 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 146 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 147 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 148 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 149 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 150 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 151 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 152 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 153 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 154 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 155 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 156 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 157 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 158 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 159 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 160 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 161 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 162 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 163 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 164 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 165 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 166 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 167 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 168 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 169 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 170 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 171 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 172 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 173 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 174 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 175 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 176 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 177 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 178 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 179 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 180 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 181 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 182 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 183 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 184 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
