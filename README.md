# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-08-03.md)

*最后自动更新时间: 2025-08-03 17:49:15*
## 1. Anthropic：角色向量

**原文标题**: Anthropic: Persona Vectors

**原文链接**: [https://www.anthropic.com/research/persona-vectors](https://www.anthropic.com/research/persona-vectors)

Anthropic 研究引入“人格向量”，这是一种理解和控制大型语言模型 (LLM) 中角色特性的方法。这些向量代表与特定人格特征（如“邪恶”、“奉承”和“幻觉”）相对应的神经网络活动模式。通过识别这些向量，研究人员可以监测、缓解和预测 LLM 中的人格转变。

该过程涉及自动生成提示来引出某种特性的对立行为，然后识别神经活动中的差异。这些向量可以注入到模型中以“引导”其行为，从而确认其影响。

人格向量能够监测部署期间的人格变化，从而可能提醒开发者注意不良漂移。它们还可以用于缓解训练期间获得的负面特征。一种违反直觉的“疫苗”方法包括在训练期间将模型*引导至*不良特征，使其更具弹性，不易从有问题的数据中获取这些特征。与训练后引导对抗该特征相比，此方法能更好地保留模型能力。

最后，人格向量可以通过预测数据在训练开始前将如何影响模型的人格来标记有问题的数据。该研究证明了这种标记技术在真实数据集上的有效性。研究结果表明，人格向量为确保 LLM 保持与人类价值观的一致性并按预期行事提供了一条有希望的途径。

---

## 2. 如果你是远程办公，那就漫谈吧。

**原文标题**: If you're remote, ramble

**原文链接**: [https://stephango.com/ramblings](https://stephango.com/ramblings)

本文提倡在团队聊天应用中设置“随笔”频道，以促进 2-10 人的远程团队内部的联系和创意产生。 这些频道就像个人日记或微博，允许队友分享想法、见解和更新，而不会打断群组频道。

每个团队成员都有自己以自己名字命名的“随笔”频道，他们可以在其中每周发布 1-3 次更新。 这些帖子可以包括项目想法、对文章的反思、“如果……会怎样”的情景、个人照片，甚至解决问题的尝试。其他人可以在这些帖子下方的评论区回复，促进讨论。

“随笔”频道被归类在专门的“随笔”部分，并且默认静音，从而减轻了阅读每篇帖子的压力。 这鼓励深度专注，同时仍然为非正式沟通提供空间，充当虚拟“茶水间”。

作者两年前在 Obsidian 实施了“随笔”，他强调这个系统已经成为保持联系和产生创新想法的宝贵工具。 这些频道的随意性和非结构化性质促成了功能想法、原型和创造性解决方案的出现。 这些随笔有助于在团队年度线下聚会之间保持人际联系。

---

## 3. 富布赖特项目：满载奇思妙想

**原文标题**: The Fulbright Program: Chock Full of Bright Ideas

**原文链接**: [https://bastian.rieck.me/blog/2025/fulbright/](https://bastian.rieck.me/blog/2025/fulbright/)

这篇博文讲述了作者接待富布赖特学者艾米丽·西蒙斯的积极体验，并呼吁继续资助富布赖特项目。作者最初与艾米丽合作开展一个医疗保健相关项目，但最终未能成功。然而，艾米丽迅速适应并为其他项目做出了重大贡献，包括医生-患者转诊网络和图学习数据集的研究，最终在ICML 2025上共同发表了一篇论文。除了研究之外，艾米丽还改进了实验室的传播策略、知识库和网站。

作者强调，富布赖特项目的真正价值远不止于可量化的研究成果，它在于连接聪明才智，促进智力提升，并为跨文化理解和创新创造机会。作者敦促决策者认识到此类项目的长期利益，反对因研究商品化而导致的目光短浅的资金削减。通过连接人，富布赖特项目在文化边界之间创造了看不见的机会、变革和创新。作者强烈支持此类项目。

---

## 4. 第二十八届国际C语言混乱代码大赛

**原文标题**: Twenty Eighth International Obfuscated C Code Contest

**原文链接**: [https://www.ioccc.org/2024/index.html](https://www.ioccc.org/2024/index.html)

第28届国际C语言混乱代码大赛(IOCCC28)迎来了其40周年纪念以及四年中断后的回归。 本次大赛有了显著的改进，包括重建的网站、新的注册和提交流程以及mkiocccentry工具包。 这些改变旨在简化比赛流程，并缩短获奖者选定和代码发布之间的时间； 源代码在YouTube节目中宣布后的2小时内就发布了。

IOCCC28有创纪录的23位获奖者，反映了提交作品的高质量和高数量。 虽然代码大小限制有所增加，但许多参赛作品远低于该限制，这表明原创性和混淆技巧比单纯的代码大小更受重视。 计划于2025年12月举行的IOCCC29的规则和指南将会得到改进。

公告重点介绍了几个获奖作品，包括小型LLM推理引擎 (cable1)、一个礼貌的编辑器 (howe)、一个带有幻数的单行代码 (stedolan)、一个C预处理器密集型图像渲染器 (endoh1)、一个对虚拟机的探索 (mills and macke) 以及一个Intel 4004模拟器 (carlini)。 文章还提到了阻止一些提交作品获胜的常见陷阱，例如依赖ASLR、与过去的参赛作品过于相似以及对现代C编译器的处理不佳。 它鼓励提交者继续尝试，并提供用于编译、运行和修复获奖作品问题的资源。

---

## 5. 赫尔辛基全年实现零交通死亡

**原文标题**: Helsinki records zero traffic deaths for full year

**原文链接**: [https://www.helsinkitimes.fi/finland/finland-news/domestic/27539-helsinki-records-zero-traffic-deaths-for-full-year.html](https://www.helsinkitimes.fi/finland/finland-news/domestic/27539-helsinki-records-zero-traffic-deaths-for-full-year.html)

赫尔辛基创下瞩目成就：全年实现交通事故零死亡。城市和警方官员将这一成功归功于长期规划、基础设施改善和降低限速。目前，赫尔辛基超过一半的街道限速为30公里/小时，学校周边区域的限速也已降低。

重新设计的街道布局、人行横道以及扩大的自行车和步行基础设施通过分隔弱势道路使用者，提高了安全性。通过自动化系统和有针对性的巡逻来加强交通执法也发挥了关键作用。该市完善的公共交通系统减少了汽车使用，进一步减少了事故。

除了死亡人数外，赫尔辛基的受伤事故也大幅减少，从1980年代后期的每年近1000起降至去年的277起。该市2022年至2026年的交通安全战略侧重于保护行人、儿童和骑自行车者，并以数据驱动的规划为支持。

虽然电动滑板车带来了一项挑战，但赫尔辛基已通过调整停车规则和速度限制做出回应。官员们还将所有道路使用者的积极行为和意识归功于这一成就。

为了实现欧盟到2050年消除交通事故死亡的“零愿景”目标，赫尔辛基利用这一目标来指导日常决策，并评估其举措的长期影响。

---

## 6. 成像揭示2500年前西伯利亚冰冻木乃伊精美纹身

**原文标题**: Imaging reveals intricate tattoos of 2,500-year-old Siberian ice mummy

**原文链接**: [https://www.bbc.com/news/articles/c4gzx0zm68vo](https://www.bbc.com/news/articles/c4gzx0zm68vo)

高分辨率成像揭示了一具2500年前西伯利亚“冰冻木乃伊”身上精美的纹身，为了解游牧的巴泽雷克文化和习俗提供了线索。这些纹身位于该女性的手臂和手上，描绘了豹、鹿、公鸡和神话生物等动物，展现了高超的艺术水平。

研究人员与一位专精于古代方法的纹身师合作，以了解纹身是如何创作的。扫描结果显示纹身精细且均匀，表明其工艺精湛。研究小组认为，这些纹身很可能先用模具印在皮肤上，然后使用动物角或骨头制成的针状工具进行纹刺，颜料则来源于烧焦的植物材料或烟灰。

分析表明，不同手臂上的纹身质量参差不齐，可能表明是不同的艺术家所为或存在失误。创作纹身所花费的时间凸显了它们的重要性。虽然一些纹身在埋葬准备过程中受损，但研究表明它们的重要性主要体现在生者身上。这些木乃伊是在阿尔泰山脉的冰墓中发现的，这项研究揭示了巴泽雷克人先进的技能和文化习俗。

---

## 7. 拥有充足资金的纽约初创公司Converge（YC S23）寻求产品开发人员

**原文标题**: Converge (YC S23) well-capitalized New York startup seeks product developers

**原文链接**: [https://www.runconverge.com/careers](https://www.runconverge.com/careers)

Converge，一家资金充足的纽约初创公司，隶属于 YC S23，正在寻找产品开发人员加入其精简的 6 人团队。他们拥有强大的产品市场契合度，表现为超过 100 万美元的年度经常性收入、超过 200 家客户以及高每日用户参与度（33%）。这意味着新员工将产生重大影响，他们将拥有整个产品并立即获得客户反馈。

Converge 致力于解决大规模的工程挑战，每天处理 2000 万次客户互动，每年处理 30 亿美元的 GMV，与 Segment 和 Fivetran 等巨头竞争。该公司强调紧迫性、深刻理解、谦逊和简单是其价值观。

他们不鼓励喜欢管理而非构建、无休止的设计评审、追逐炒作、频繁转型、寻求大量指导或远程工作的候选人。创始团队由 Jan-Henrik（首席执行官）、Jerome（首席运营官）和 Thomas（首席技术官）组成，他们强调亲力亲为的方法，所有创始人都编写过生产代码。该团队强调他们密切的关系和多元化的背景。

---

## 8. 真正的PowerBook：在PA-RISC笔记本电脑上的Macintosh应用程序环境

**原文标题**: A Real PowerBook: The Macintosh Application Environment on a Pa-RISC Laptop

**原文链接**: [http://oldvcr.blogspot.com/2025/08/a-real-powerbook-macintosh-application.html](http://oldvcr.blogspot.com/2025/08/a-real-powerbook-macintosh-application.html)

本文探讨了RDI PrecisionBook，一款1997年罕见的PA-RISC笔记本电脑，以及它通过苹果的Macintosh应用程序环境运行Macintosh应用程序的能力。作者强调，虽然PowerPC是Macintosh的摩托罗拉68000处理器的预期继任者，但PrecisionBook提供了一种使用惠普PA-RISC架构的替代方案。

PrecisionBook的定位是与PowerBook 3400c竞争，它拥有更高的分辨率显示器、更大的键盘和更多的RAM等优势，但价格也明显更高。其主要特点是运行HP-UX的同时，运行Macintosh System 7.5.3桌面，从而允许用户运行68K Mac软件。

文章详细介绍了RDI在多元化到PA-RISC之前作为SPARC笔记本电脑制造商的历史。PrecisionBook本质上是一台便携式HP Visualize工作站，使用相同的组件，甚至识别为同一型号。作者的特定机器，昵称为“ruby”，配备了160MHz PA-7300LC处理器和256MB（后来升级到512MB）的RAM。

文章进一步描述了该笔记本电脑的各种功能，包括其状态LCD面板、电池寿命、端口和图形功能。它具有双硬盘驱动器托架、PCMCIA插槽和外部连接选项。文章还提到了机器的启动过程和PA-7300LC处理器的技术规格。最终，作者为探索在这个不寻常的硬件上运行Macintosh应用程序环境的性能和基础做好了准备。

---

## 9. 滑雪租赁问题

**原文标题**: The Ski Rental Problem

**原文链接**: [https://lesves.github.io/articles/ski-rental/](https://lesves.github.io/articles/ski-rental/)

本文解释了“滑雪板租赁问题”，这是一个经典的在线算法问题，你必须决定租用还是购买滑雪板，但不知道你会滑多少天。租用每天花费1美元，购买花费B美元。

最优离线算法（知道滑雪天数*k*）是在*k* ≥ *B*时购买，否则租用，花费min(*k*, *B*)。一个简单的在线算法是在租用*B*天后购买，这导致竞争比率为2（意味着它最多比最优离线解决方案差两倍）。

然后，本文探讨了一种随机算法，以潜在地提高竞争比率。该算法在第*i+1*天以概率*P<sub>i</sub>*购买滑雪板。通过使用连续概率密度函数*P(x)*来近似离散概率，目标是找到一个最小化竞争比率的最优*P(x)*。使用微积分，本文推导出最优概率分布：*P(x) = e<sup>x/B</sup> / (B(e-1))*，当*x < B*时，否则为0。这导致预期的竞争比率约为*e / (e - 1)*，这比简单的确定性算法更好。本文包含Python代码来模拟随机策略，但承认它正在用连续解来近似离散解。最后，它假设如果必须重复做出类似的决策，该算法可能会有所帮助。

---

## 10. 如何制作（几乎）任何东西（2019）

**原文标题**: How To Make (almost) Anything (2019)

**原文链接**: [https://fab.cba.mit.edu/classes/863.19/CBA/people/dsculley/index.html](https://fab.cba.mit.edu/classes/863.19/CBA/people/dsculley/index.html)

D. Sculley，一位在剑桥领导谷歌机器学习团队的研究员，正在参加“如何制作（几乎）任何东西”课程，以探索制造方法和潜在的跨领域应用，尤其是在生物学和化学领域。 他的兴趣源于他团队目前利用机器学习进行设计和制造的项目。 他为该课程带来了多元化的背景，包括多年的机器学习经验（自2003年以来）、之前的教学经验以及视觉与环境研究（“艺术”）本科学位。 他承认自己打算犯错，并欢迎关于机器学习的讨论。 课程大纲概述了对各种制造技术的全面探索，涵盖CAD与草图绘制到CNC加工、嵌入式编程、模具与铸造、电子设计与生产、3D扫描与打印，并在涵盖输入和输出设备、网络、机器周、应用程序编程和通配符周之后，以一个最终项目告终。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 2 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 3 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 4 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 5 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 6 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 7 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 8 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 9 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 10 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 11 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 12 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 13 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 14 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 15 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 16 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 17 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 18 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 19 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 20 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 21 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 22 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 23 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 24 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 25 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 26 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 27 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 28 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 29 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 30 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 31 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 32 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 33 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 34 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 35 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 36 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 37 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 38 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 39 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 40 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 41 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 42 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 43 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 44 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 45 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 46 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 47 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 48 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 49 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 50 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 51 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 52 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 53 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 54 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 55 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 56 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 57 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 58 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 59 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 60 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 61 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 62 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 63 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 64 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 65 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 66 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 67 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 68 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 69 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 70 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 71 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 72 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 73 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 74 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 75 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 76 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 77 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 78 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 79 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 80 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 81 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 82 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 83 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 84 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 85 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 86 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 87 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 88 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 89 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 90 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 91 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 92 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 93 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 94 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 95 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 96 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 97 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 98 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 99 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 100 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 101 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 102 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 103 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 104 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 105 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 106 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 107 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 108 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 109 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 110 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 111 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 112 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 113 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 114 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 115 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 116 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 117 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 118 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 119 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 120 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 121 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 122 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 123 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 124 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 125 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 126 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 127 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 128 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 129 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 130 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 131 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 132 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 133 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 134 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 135 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 136 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 137 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
