# Hacker News 热门文章摘要 (2025-08-03)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Telo MT1

**原文标题**: Telo MT1

**原文链接**: [https://www.telotrucks.com/](https://www.telotrucks.com/)

TELO MT1 是一款全电动迷你卡车，专为城市生活和周末探险设计。它结合了丰田 Tacoma 的性能、特斯拉的效率和 MINI Cooper 的占地面积。MT1 可容纳五人，并配备 60 英寸货箱，可通过创新的中门和可选的第三排座椅扩展，以容纳 4x8 英寸的胶合板或多达八名乘客。

MT1 拥有 350 英里的续航里程、500 马力和快速 20 分钟的快速充电（20-80%）。它提供安全的卷帘盖以供存储，并通过先进的碰撞检测技术优先考虑安全性。内饰采用极简设计，并使用天然面料。规格重点包括双电机选项、潜在的 2WD 传动系统、2,000 磅的有效载荷能力以及可变的座椅配置和电池续航里程。TELO Trucks 强调重新设计电动卡车以实现最大效率和功能性。 您今天就可以预订。

---

## 12. 克劳德代码六周

**原文标题**: 6 weeks of Claude Code

**原文链接**: [https://blog.puzzmo.com/posts/2025/07/30/six-weeks-of-claude-code/](https://blog.puzzmo.com/posts/2025/07/30/six-weeks-of-claude-code/)

克劳德代码对Puzzmo工程师六周内软件开发工作流程的变革性影响。作者强调在编码中获得了前所未有的“表达自由”，无需编写每一行代码，同时对最终产品承担全部责任。作者将其比作编程界的“摄影术的引入”，认为克劳德代码显著加速了开发进程。

主要优点是大幅降低了维护和解决技术债务的成本。作者详细列举了一系列已完成的项目，包括代码库转换、系统替换和基础设施改进，这些项目都是在处理主要路线图的同时作为“副项目”完成的。这使得多年积压的工作在不到一个半月的时间内得以解决，而工作时间没有明显增加。这使得他们能够快速探索想法并“先编写，后决定”。

作者还介绍了“两个克隆体生活方式”，即使用两个独立的 VS Code 实例进行独立的拉取请求工作。他们解释了克劳德代码如何改变了 Puzzmo 的游戏开发流程，使设计师能够快速原型设计和部署游戏。然而，这也引发了人们对保持代码质量和将原型集成到生产流水线中的担忧。

作者还讨论了内部的成功以及成为一名全方位开发者的重要性。他们将克劳德代码的成功归功于 Puzzmo 的单一代码库架构、明确的技术选择以及其作为这些模型的测试套件/基准的业务性质。

虽然作者承认拉取请求和代码行数等指标没有发生显著变化，但他们坚信 Puzzmo 的变化步伐加快了。作者最后建议关注克劳德代码的有效使用，而不是沉迷于最新的 LLM 趋势。

---

## 13. 海沟极深处繁盛的化能合成生命

**原文标题**: Flourishing chemosynthetic life at the greatest depths of hadal trenches

**原文链接**: [https://www.nature.com/articles/s41586-025-09317-z](https://www.nature.com/articles/s41586-025-09317-z)

本文报道了在千岛-堪察加和西阿留申海沟（地球上一些最深的环境）中发现的广泛的化能合成生物群落。研究人员利用载人潜水器“奋斗者”号，在5800米至9533米的深度识别出绵延2500公里的生物群落，这些生物群落主要由管状蠕虫和双壳类动物组成。

这些生物群落依靠富含硫化氢和甲烷的流体维持，这些流体通过贯穿深层沉积层的断层释放出来，甲烷是在那里由沉积的有机物通过微生物产生的。同位素分析支持这种甲烷生产机制。

这些生物群落的物种组成在海沟之间甚至在海沟内部都各不相同。千岛-堪察加海沟主要以缨鳃虫为主，而堪察加-阿留申过渡区则富含囊蛤。诸如“最深处”（9533米）和“冬馨谷”（9120米）等特定地点表现出不同的物种组合和密度。在千岛-堪察加海沟中发现的*Tartarothyasira hadalis*标志着在海沟带发现了最深处的化能共生双壳类动物。

这一发现挑战了现有的关于极端深度生命和深海碳循环的模型，表明由于地质相似性，这种生物群落可能比以前认为的更广泛地分布在海沟带中。该研究强调了这些以前未被充分认识的海沟生态系统的生态意义。

---

## 14. 莉娜·可汗认为Figma首次公开募股证明并购审查是正确的

**原文标题**: Lina Khan points to Figma IPO as vindication of M&A scrutiny

**原文链接**: [https://techcrunch.com/2025/08/02/lina-khan-points-to-figma-ipo-as-vindication-for-ma-scrutiny/](https://techcrunch.com/2025/08/02/lina-khan-points-to-figma-ipo-as-vindication-for-ma-scrutiny/)

前联邦贸易委员会主席莉娜·汗认为Figma的成功上市验证了她对并购审查采取的更严格方式。 汗认为，允许像Figma这样的初创公司独立发展比被大公司收购更能产生价值，她指的是在她任期内面临监管挑战的、价值200亿美元的Adobe-Figma失败交易。

虽然Adobe引用了欧洲和英国的监管障碍，但美国也对收购扼杀竞争表示担忧。 汗为她对大型科技公司收购采取的强硬立场辩护，声称只有一小部分收购受到了严格审查，并且创始人可以从更多的潜在收购者中受益。

尽管汗已离开联邦贸易委员会，但她的评论认为Figma的首次公开募股对员工、投资者、创新和公众都有利。 然而，批评人士认为，Figma的成功源于其自身的创新，而非监管干预。 例如，Wedbush Securities分析师Dan Ives将Figma的成功归功于其创新增长，而不是联邦贸易委员会的行动。 这篇文章强调了关于监管审查在科技行业中的作用及其对初创企业的影响的持续辩论。

---

## 15. 美光推出276层SSD三剑客，兼顾速度、规模和稳定性

**原文标题**: Micron rolls out 276-layer SSD trio for speed, scale, and stability

**原文链接**: [https://blocksandfiles.com/2025/07/30/micron-three-276-layer-ssds/](https://blocksandfiles.com/2025/07/30/micron-three-276-layer-ssds/)

美光推出三款基于Gen 9 276层3D NAND技术的全新SSD，分别针对不同的市场需求：速度、容量和一致性性能。

**9650** 是一款高性能PCIe Gen 6 SSD，采用TLC闪存，提供读优化“Pro”和混合用途“Max”两种型号。 其顺序读取速度高达28 GBps，顺序写入速度高达14 GBps，随机读取/写入IOPS高达550万/90万。 容量范围从6.4 TB到30.72 TB，采用E3.S和E1.S规格。 它旨在加速AI训练和推理，并且比其前身9550更快、更节能。

**6600 ION** 是一款高容量PCIe Gen 5 SSD，采用QLC闪存。 专为大容量存储而设计，提供高达122.88 TB的容量，是6550 ION的后续产品。 尽管容量高达122.88 TB，但其读写速度与6550相比有所降低，牺牲速度以换取容量。 计划于2026年推出245 TB版本。

**7600** 是一款PCIe Gen 5 TLC SSD，专注于为AI、数据库和云计算等应用提供一致的低延迟。 它提供Pro（读取密集型）和Max（混合用途）版本，容量范围从1.6 TB到15.36 TB，采用U.2规格。 虽然不是最快的，但它平衡了性能和可预测性。

这三款SSD均采用美光自研的DRAM、NAND、控制器和固件，并集成了各种安全功能。 9650和7600的样品目前正在发货，而6600 ION 122 TB预计将于2025年第三季度上市。

---

## 16. 如果人工智能解决了孤独，我们可能不喜欢我们会变成什么样。

**原文标题**: We may not like what we become if A.I. solves loneliness

**原文链接**: [https://www.newyorker.com/magazine/2025/07/21/ai-is-about-to-solve-loneliness-thats-a-problem](https://www.newyorker.com/magazine/2025/07/21/ai-is-about-to-solve-loneliness-thats-a-problem)

本文探讨了人工智能陪伴在解决孤独问题上复杂且可能令人不安的影响。作者是一位心理学教授，他之前曾论证支持具有同理心的人工智能。他承认那些认为人工智能是缺乏灵魂的、对真正人际关系的替代品的人的担忧。

文章强调了孤独的普遍性和有害影响，引用了将其与各种健康问题和情绪困扰联系起来的研究。文章认为，虽然理想的解决方案涉及人际交往，但由于真正的人类关注的稀缺，人工智能伴侣成为一种可行的（即使是不完美的）替代方案，特别是对于老年人或缺乏社会支持的人。

作者提出了证据表明，在某些情况下，人工智能聊天机器人可以提供出人意料的同理心回应，甚至在某些情况下胜过人类医生。这提出了人工智能充当治疗性伴侣的可能性，但人们仍然担心潜在的欺骗以及缺乏真正的人类存在。

作者探讨了广泛使用人工智能陪伴的伦理影响，特别是对于年轻一代。文章承认其对那些严重孤独的人的潜在好处，但质疑触手可及的人工智能关系对孤独、独立思考和创造力的长期社会影响。它还表明，随着人工智能越来越擅长模仿同理心，人与程序之间的界限将会变得模糊，可能导致无法预见的心理后果以及对模拟连接的依赖。最终，本文提出了深刻的问题，即在一个人工伴侣日益复杂和易于获得的世界中，成为人类意味着什么。

---

## 17. PixiEditor 2.0 – 一款 FOSS 通用 2D 图形编辑器

**原文标题**: PixiEditor 2.0 – A FOSS universal 2D graphics editor

**原文链接**: [https://pixieditor.net/blog/2025/07/30/20-release/](https://pixieditor.net/blog/2025/07/30/20-release/)

PixiEditor 2.0 于 2025 年 7 月 30 日发布，是一款免费开源的“通用 2D 编辑器”，它从像素艺术起家，逐步发展到可以处理栅格、矢量、动画和程序图形。它的目标是高度可配置，以适应不同的工作流程，而不仅仅是 Photoshop 的替代品。

主要功能包括可切换的绘画、像素艺术和矢量编辑工具集，允许在单个文件中混合图形。矢量支持包括具有非破坏性图层的高 DPI 编辑以及路径、线条、椭圆、矩形和文本等工具。强大的节点图能够实现复杂的效果和程序动画，从而可以精细地控制图像渲染。预构建的节点工作区简化了工作流程。

动画可以是逐帧的或程序生成的，可以导出为视频或精灵表。像素艺术工具集包括像素完美的画笔、转换工具和非破坏性的文本工具。

为了支持全职开发，成立了 Pixi Labs Sp. z o.o.。第一个付费扩展包，创始人包，提供了卡片生成器、3D 立方体纹理、纹理平铺和可重用的像素艺术动画等工作区，以及独特的调色板和应用内徽章。举办了直播活动来展示 PixiEditor 2.0 并提供折扣。

虽然需要兼容 Vulkan 的 GPU 和 64 位系统，但 PixiEditor 2.0 是一次重大的升级。1.0 版本仍然作为测试版提供。

---

## 18. 画布中的HTML

**原文标题**: HTML-in-Canvas

**原文链接**: [https://github.com/WICG/html-in-canvas](https://github.com/WICG/html-in-canvas)

本文介绍了一项关于新型 HTML Canvas API 的提案，该提案允许将 HTML 内容直接渲染到 `<canvas>` 元素中，适用于 Canvas 2D 和 WebGL。其目标是解决当前 canvas 实现的局限性，尤其是在样式化文本、可访问性以及 HTML 内容与着色器集成等领域。

该提案包括几个新的 API：`layoutsubtree`（一个 canvas 属性，用于启用后代元素的布局），`drawElement`（Canvas 2D 方法，用于渲染一个元素及其子树），`texElement2D`（WebGL 方法，用于将一个元素渲染成纹理）以及 `setHitTestRegions`（Canvas 2D 和 WebGL 均有，用于将点击测试从 canvas 重定向到绘制的元素，从而实现交互性）。此外，还向 ResizeObserverOptions 添加了一个 `fireOnEveryPaint` 选项，用于在绘制元素的 DOM 状态更改时发出通知，从而触发 canvas 重绘。

这些 API 能够实现诸如 canvas 中更丰富的文本渲染、通过确保回退内容与渲染内容匹配来改善可访问性、将 HTML 元素与着色器组合以及在 3D 场景中渲染 HTML 内容等用例。

该文档还提供了关于开发者试用的详细信息，包括如何在 Chrome Canary 中启用该功能以及有关试用阶段潜在隐私问题的注意事项。鼓励开发者就哪些内容有效和失败、缺失的 canvas 渲染上下文支持以及可访问性改进提供反馈。演示展示了 API 在将 HTML 渲染到 GL 纹理中以及在 canvas 中利用交互式元素方面的用法。

---

## 19. 词穷语塞：一个有缺陷的理念正在教坏孩子们的阅读能力（2019）

**原文标题**: At a Loss for Words: A flawed idea is teaching kids to be poor readers (2019)

**原文链接**: [https://www.apmreports.org/episode/2019/08/22/whats-wrong-how-schools-teach-reading](https://www.apmreports.org/episode/2019/08/22/whats-wrong-how-schools-teach-reading)

在《失语症》中，艾米丽·汉福德调查了一种名为“三提示法”的错误理论如何阻碍美国学校的阅读教育。这种理论由肯·古德曼和玛丽·克莱推广，认为读者使用图像、句法和语义线索来猜测单词，而不是解码它们。汉福德着重讲述了莫莉·伍德沃思在阅读上的挣扎，以及她看到自己的孩子被教授同样无效的策略时的沮丧。

认知科学家已经驳斥了三提示法，证明熟练的读者依赖于快速、准确地识别单词作为一系列字母，而不过度依赖语境。基思·斯塔诺维奇的研究证实，较弱的读者更依赖语境。尽管有科学证据，三提示法仍然存在于学校中，影响着课程和教学实践。这在读者工作坊中很明显，孩子们被教导使用“图片力量”和其他语境线索来猜测单词。文章认为，这种方法使得孩子们更难学会熟练阅读。它将糟糕的阅读技能与负面结果联系起来，例如高中辍学和卷入刑事司法系统。文章批评了对基于提示的教学方法的持续投入，并呼吁转向基于科学的阅读教学方法。

---

## 20. C++26 反射探索与编译时 UML

**原文标题**: C++26 Reflections adventures and compile-time UML

**原文链接**: [https://www.reachablecode.com/2025/07/31/c26-reflections-adventures-compile-time-uml/](https://www.reachablecode.com/2025/07/31/c26-reflections-adventures-compile-time-uml/)

本文探讨了如何利用C++26的反射特性，在编译时从C++代码自动生成UML图。作者利用新的`lift` (^^) 和 `splice` 运算符来反映 C++ 类型及其成员，从而解决手动创建 UML 图的繁琐耗时问题。

核心思想围绕一个`make_class_graph`函数模板展开，该模板使用`std::meta::info`来表示反射的类型和值。此函数递归地遍历类的成员，提取有关其类型和关系的信息。一个关键挑战是管理“元”空间，其中类型的反射和值的反射都表示为`std::meta::info`，需要使用`std::meta::is_type`来确定正在处理的反射类型。

生成的UML图在编译时使用`std::define_static_string`构建为字符串，该函数将编译时`std::string`转换为可以从`consteval`函数返回的字符串字面量。作者还讨论了使用`std::meta::access_context`来管理反射期间的访问规则。最后，使用`std::meta::nonstatic_data_members_of`和`std::meta::info::display_string_of`等函数来访问类成员及其名称。作者承认需要区分类型反射和值反射带来了一点复杂性，但认为这对于C++26反射功能的强大性来说是值得的。 输出是可供可视化的 PlantUML 图。

---

## 21. LangExtract：用于从语言模型中提取结构化数据的 Python 库

**原文标题**: LangExtract: Python library for extracting structured data from language models

**原文链接**: [https://github.com/google/langextract](https://github.com/google/langextract)

LangExtract 是一个 Python 库，利用大型语言模型（LLM）根据用户定义的指令和示例从非结构化文本中提取结构化信息。它擅长处理临床笔记、识别关键细节和保持一致的输出模式等任务。

其主要功能包括精确的源头定位（将提取的内容映射到其来源）、通过受控生成实现可靠的结构化输出、通过分块和并行处理优化长文档的处理、交互式可视化审查、灵活的 LLM 支持（云端和本地，例如 Ollama），以及无需微调即可适应各种领域。

该库需要定义提示并提供示例来指导模型。它支持 Gemini 和 OpenAI 等模型（具有特定的配置需求）。结果可以保存为 JSONL 格式，并通过交互式 HTML 进行可视化。

可以通过 pip (PyPI)、从源代码或使用 Docker 安装。使用云模型需要 API 密钥，可以通过环境变量、`.env` 文件或（不太理想的）直接在代码中设置。

文档提供了示例用例，包括罗密欧与朱丽叶全文提取、药物提取和放射学报告结构化（RadExtract 演示）。欢迎贡献，该项目利用自动格式化工具和 pre-commit 钩子来维护代码风格。该库根据 Apache 2.0 许可证分发，但与健康相关的应用程序有附加条款。

---

## 22. keygen音乐在线合集

**原文标题**: Online Collection of Keygen Music

**原文链接**: [https://keygenmusic.tk](https://keygenmusic.tk)

Keygenmusic.tk 是一个在线跟踪音乐播放器，专门提供常见于注册机（软件许可证生成器）中的音乐。该网站支持 .mod、.xm、.s3m 和 .it 等格式。

该网站目前处于测试阶段 (β15)，更新日志详细记录了从 2015 年到 2025 年的更新，重点介绍了 Firefox 兼容性、媒体键支持、图标更新、播放列表集成、频谱分析仪、收藏夹、搜索功能以及来自 keygenmusic.net 的音乐包的更新等改进。该网站明确声明不包含非法内容，只包含来自注册机的音乐。

该网站由 Mikhailo Onikiienko 开发，并利用了各种库和工具，包括 chiptune2.js、libopenmpt、emscripten、jsTabs、baron、Sergio Camalich 的作品、webaudio68 和 Darcula 配色方案。它还提到了一个随机播放开/关切换器。

通过电子邮件地址 keygenmusic.tk{at}outlook.com 提供联系方式。该网站还指出不支持 AudioContext 的浏览器可能存在问题，建议使用 Firefox 以获得最佳功能。该网站跟踪播放的总曲目数和唯一曲目数，但文档中没有数据。

---

## 23. 伊南娜下冥府

**原文标题**: Descent of Inanna into the Underworld

**原文链接**: [https://en.wikipedia.org/wiki/Descent_of_Inanna_into_the_Underworld](https://en.wikipedia.org/wiki/Descent_of_Inanna_into_the_Underworld)

《伊南娜下冥界》是苏美尔神话（阿卡德版本标题为《伊什塔尔下冥界》），讲述了女神伊南娜前往冥界挑战她的姐姐、亡灵女王埃列什基伽勒的故事。伊南娜的下行导致她的死亡和作为尸体的悬挂，直到恩基介入，让她复活。然而，她的回归需要一个替代者，导致她的配偶杜牧兹被送往冥界。后来，由于他妹妹格什廷安娜的恳求，杜牧兹的刑期被缩短为一年中只有一部分时间在冥界度过，他的妹妹在剩余的时间里代替他。

这个神话有苏美尔语和阿卡德语版本，后者首先被发现。苏美尔语版本更古老也更长，需要从石板碎片中进行大量重建。最初，学者们误解了伊南娜的动机是寻找杜牧兹，受到了俄耳甫斯神话的影响。然而，后来人们了解到她寻求扩张自己的权力。

主要人物包括：伊南娜（伊什塔尔），一位多面女神，掌管爱情、战争和生育；埃列什基伽勒，静止的冥界女王；古迦兰纳，埃列什基伽勒的丈夫；南塔尔，她的维齐尔和疾病之神；以及恩基，淡水和智慧之神，他使伊南娜复活。格拉图拉和库尔加拉，性别模糊的存在，也发挥了作用，在冥界穿梭以安抚埃列什基伽勒。

这个神话提供了对美索不达米亚文化的洞见，影响了后来的文明，并为精神分析理论提供了素材。最近的重新审视表明，伊南娜本人介入了杜牧兹的季节性回归，突出了故事的持续解读和演变。

---

## 24. Seed7 – 可扩展的程序设计语言

**原文标题**: Seed7 – The Extensible Programming Language

**原文链接**: [https://seed7.net](https://seed7.net)

Seed7 是一种通用、可扩展的编程语言，由 Thomas Mertes 设计，旨在提供比 Ada、C/C++ 和 Java 等语言更高的抽象级别。 解释器和编译器（转换为 C）均以开源软件形式提供。

主要特性包括轻松定义新语句和运算符的能力，以及使用一等类型，从而无需特殊语法即可实现优雅的模板和泛型。 对象导向有选择性地在有利的地方实现。 Seed7 从 Pascal、Ada、C、C++ 和 Java 中汲取灵感。

Seed7 拥有诸如用户定义的语句/运算符、库中定义的预定义构造、用于对象导向的接口和多重分派、静态类型检查、无自动类型转换以及 *没有* 垃圾回收的自动内存管理等特性。 它还支持异常处理、调试、整数计算的溢出检测以及无限大小的数字（bigInteger、bigRational）。 支持函数、运算符和语句重载，以及各种预定义类型。

Seed7 旨在实现跨操作系统的源代码可移植性，并提供与多个数据库兼容的独立于数据库的 API。 它可以在 Linux、各种 Unix 版本和 Windows 下运行。 解释器和示例程序采用 GPL 许可，而运行时库采用 LGPL 许可。

---

## 25. Show HN: DDPM (去噪扩散概率模型) 实现

**原文标题**: Show HN: Implementation of DDPM (Denoising Diffusion Probabilistic Models)

**原文链接**: [https://github.com/alenMangattu/DDPM-Denoising-Diffusion-Probabilistic-Models](https://github.com/alenMangattu/DDPM-Denoising-Diffusion-Probabilistic-Models)

此“Show HN”帖子介绍了一种去噪扩散概率模型(DDPM)的极简实现。DDPM是一类生成模型，以其生成高质量图像和其他数据的能力而闻名。

该帖子重点介绍了一种简化的“骨架式”实现，这意味着侧重于清晰和简洁，而不是优化或高级功能。这表明该实现旨在易于理解，并作为有兴趣掌握DDPM核心概念的人的学习资源。

作者的随意语气("ig")表明演示方式较为非正式，可能采用对初学者友好的方法。虽然缺乏关于实现细节的具体信息，但该帖子为那些对DDPM算法的简单入门版本感兴趣的人发出了信号。“Show HN”标签表明作者正在Hacker News上分享他们的项目，以征求社区内的反馈和讨论。因此，鼓励对学习DDPM或为该项目做出贡献的用户直接查看链接的代码。

---

## 26. Anandtech.com 现在重定向到其论坛。

**原文标题**: Anandtech.com now redirects to its forums

**原文链接**: [https://forums.anandtech.com/](https://forums.anandtech.com/)

Anandtech.com 现在重定向至其论坛，这是一个专注于技术、硬件、软件和交易的综合性在线社区。论坛涵盖广泛的主题，包括 CPU、主板、显卡、内存与存储、显示器、电源、机箱与散热、笔记本电脑、网络、苹果产品、外设、电脑组装、消费电子产品、主机游戏、移动设备、音频、电视、软件（Windows、Apple、开源、操作系统、编程）、PC 游戏、分布式计算、安全、购物（交易和黑色星期五）以及社交话题（OT 讨论俱乐部、政治、技术讨论、车库、健康、家居与园艺以及论坛问题）。

该网站突出显示 CPU 和超频版块的热门话题，并设有“最新帖子”版块，展示不同论坛的最新动态。用户可以加入 AnandTech 社区参与讨论并寻求专家建议。论坛还提供通过社交媒体平台分享内容的选项。AnandTech 是 Future plc 的一部分。

---

## 27. 费马大定理证明的Lean形式化持续进行中

**原文标题**: Ongoing Lean formalisation of the proof of Fermat's Last Theorem

**原文链接**: [https://github.com/ImperialCollegeLondon/FLT](https://github.com/ImperialCollegeLondon/FLT)

本文介绍一个开源项目，该项目致力于使用Lean定理证明器形式化证明费马大定理。该项目由凯文·巴扎德领导，并由EPSRC资助至2029年9月，位于伦敦帝国理工学院。该项目旨在实现理查德·泰勒计划的Wiles/Taylor-Wiles证明的现代版本。它提供了解释费马大定理、Lean、项目动机、数学蓝图以及个人如何为此做出贡献的资源链接。最终目标是在Lean环境中创建一个完全形式化和验证的费马大定理证明。

---

## 28. 展示 HN：我的字节码优化器性能是 Copilot 的两倍

**原文标题**: Show HN: My Bytecode Optimizer Beats Copilot by 2X

**原文链接**: [https://deviantabstraction.com/2025/07/29/how-my-bytecode-optimizer-beats-copilot-by-2x/](https://deviantabstraction.com/2025/07/29/how-my-bytecode-optimizer-beats-copilot-by-2x/)

此“Show HN”文章介绍了一个名为SuperVM的副项目，它是一个字节码优化器，并将其在简单分形生成器任务上的性能与Copilot（特别是GPT-4o和Sonnet）进行了比较。作者Deviant/Abstraction认为，即使在早期开发阶段，专用工具也能胜过通用人工智能模型。

该实验要求Copilot针对一个手工编写的分形生成器发出“让它更快”的提示，并将产生的每秒帧数 (FPS) 与原始代码和 SuperVM 的输出进行比较。SuperVM 平均实现了 99.8 FPS，是原始 13.8 FPS 的两倍，并显著超过了 Copilot 的 49.3 FPS。关键区别在于 SuperVM 能够直接编辑字节码并利用形式化证明进行优化。

作者强调，Copilot 识别并并行化了一个循环，而 SuperVM 证明像素迭代循环没有副作用，使其能够将其拆分为多个工作线程并保持顺序 GUI 重绘。SuperVM 还可以在几秒钟内完成编译，而 Copilot 需要几分钟。虽然承认了狭窄测试用例的局限性，但作者认为这表明了专用工具在补充大型语言模型方面的潜力，尤其是在代码优化方面。作者计划将来在更通用的基准上测试 SuperVM，包括推理服务。

---

## 29. 人工智能研究员正在洽谈2.5亿美元的薪酬方案。

**原文标题**: A.I. researchers are negotiating $250M pay packages

**原文链接**: [https://www.nytimes.com/2025/07/31/technology/ai-researchers-nba-stars.html](https://www.nytimes.com/2025/07/31/technology/ai-researchers-nba-stars.html)

无法访问文章链接。

---

## 30. 多处理器编程艺术（第二版）读书会

**原文标题**: The Art of Multiprocessor Programming 2nd Edition Book Club

**原文链接**: [https://eatonphil.com/2025-art-of-multiprocessor-programming.html](https://eatonphil.com/2025-art-of-multiprocessor-programming.html)

本书宣布成立一个读书会，专注于Herlihy、Shavit、Luchangco和Spear于2020年出版的《多处理器编程的艺术（第二版）》。该读书会是软件内幕邮件读书俱乐部的一部分，将通过Google Group进行讨论，需要一个Google帐户。所有交流都将以文本形式进行；不会有视频通话。

读书会将每周讨论一章，从2024年8月16日开始，进行介绍，并持续到2024年12月13日，涵盖障碍。参与者需要在相应的讨论日期之前阅读每一章。

每周，指定的“讨论发起者”将通过简短的电子邮件分享对该章节内容的个人思考来启动对话，而不是简单地总结它。目标是基于个人经验和解读，培养引人入胜且具有相关性的讨论。

感兴趣的人可以通过提供的表格注册。反馈和疑问可以通过电子邮件或Twitter发送给组织者。组织者强调获取本书第二版的重要性。

---

## 31. 打造你的专属 Minisforum N5 灵感迷你 NAS：一份全面指南

**原文标题**: Build Your Own Minisforum N5 Inspired Mini NAS: A Comprehensive Guide

**原文链接**: [https://jackharvest.com/index.php/2025/07/27/build-your-own-minisforum-n5-inspired-mini-nas-a-comprehensive-guide/](https://jackharvest.com/index.php/2025/07/27/build-your-own-minisforum-n5-inspired-mini-nas-a-comprehensive-guide/)

本文提供了一份全面的指南，教你如何打造一款DIY迷你NAS，其灵感来源于Minisforum N5，但通过复用现有的迷你PC，使其更经济实惠且更灵活。作者jackharvest详细介绍了设计目标：适合在小型3D打印机床（180x180mm）上打印，模仿N5的美学设计，并保持低功耗和简易的组装过程（主要部件无需支撑）。

该设计在Shapr3D中创建，稍后将发布原始文件。构建过程包括使用PETG和TPU材料3D打印各种部件，包括主体、磁性面板夹具、主板偏移柱、底脚和风扇螺丝。

该指南提供了详细的NAS组装说明，重点介绍了硬盘仓区域、迷你PC抽屉区域和电源部分。采用双电源线方案（迷你PC使用19V，硬盘使用12V）以提高效率。作者提供了带有图片的逐步说明，指导如何连接电源、安装背板PCB和管理线缆。迷你PC安装在抽屉内，硬盘通过M.2 SATA端口适配器连接。

最后，文章还包括一份估算成本明细，假设用户拥有3D打印机，但需要购买所有其他组件。

---

## 32. 为 GNU Guix 编写基础服务

**原文标题**: Writing a basic service for GNU Guix

**原文链接**: [https://tannerhoelzel.com/gnu-shepherd-simple-service.html](https://tannerhoelzel.com/gnu-shepherd-simple-service.html)

本文详细介绍了为GNU Guix创建一项服务，以自动启动和管理`kmonad`键盘重映射守护进程的过程。首先概述了创建专用Guix服务而不是使用诸如cron job等替代方法的原因。

作者随后探索了Guix文档和现有示例，特别是“游戏服务”和`wesnothd`服务，以了解如何定义自定义服务类型。文章逐步介绍了定义`kmonad-service-type`的步骤，包括使用专用的“kmonad-daemon”用户和组扩展`account-service-type`，以及扩展`shepherd-root-service-type`以使用Shepherd init系统管理守护进程的生命周期。

一个关键方面是定义`kmonad-shepherd-service`，它利用G-Expressions和`make-forkexec-constructor`，以指定的配置文件（`.kbd`）和日志记录来启动`kmonad`。文章解释了定义诸如`udev`和`user-processes`等服务需求的重要性，以确保正确的启动依赖关系。

最后，该代码被打包到Guix模块（`my/services/kmonad.scm`）中，文章演示了如何将`kmonad-service-type`整合到系统配置中，包括添加必要的用户组、软件包和udev规则。文章最后给出了一个重新配置Guix系统的命令，以激活新服务。

---

## 33. 联合国报告发现联合国报告阅读量不高

**原文标题**: UN Report Finds UN Reports Are Not Widely Read

**原文链接**: [https://www.reuters.com/world/un-report-finds-united-nations-reports-are-not-widely-read-2025-08-01/](https://www.reuters.com/world/un-report-finds-united-nations-reports-are-not-widely-read-2025-08-01/)

无法访问文章链接。

---

## 34. 电子病历——诊所里不易察觉的干扰

**原文标题**: EHRs – The Hidden Distraction in Your Doctor's Office

**原文链接**: [https://spectrum.ieee.org/electronic-health-records](https://spectrum.ieee.org/electronic-health-records)

计算机杂志文章《电子病历——医生诊所里隐藏的干扰》探讨了自2004年以来美国在电子健康记录（EHR）系统上投资的1000亿美元，揭示了进步和持续存在的问题。虽然与过去相比，电子病历改善了医疗信息的获取，但无缝、互操作系统的愿景仍然难以实现。

该文章强调了2009年的《高科技法案》（HITECH Act）作为经济刺激计划的一部分，拨款490亿美元用于促进电子病历的采用。这导致了广泛的实施，但也由于缺乏互操作性标准以及不同专科医生之间存在各种电子病历系统，造成了分散的“电子孤岛”。

在《高科技法案》激励下仓促采用电子病历忽略了关键的系统工程原则和以人为本的设计，导致了成本高昂、设计糟糕且不安全的系统。这些问题导致临床医生倦怠、数据泄露和新的医疗错误来源。此外，文章指出，医生每天花费过多时间（平均每天4.5小时）进行数据录入，从而分散了患者互动和职业满意度，这是一个意想不到的后果。文章建议需要一种更周全和集成的电子病历实施方法，强调互操作性、可用性和安全性，以避免美国医疗保健系统恶化。

---

## 35. 翻转世界的比特

**原文标题**: Flipping Bits in the World

**原文链接**: [https://opuslabs.substack.com/p/how-to-flip-bits-in-the-world](https://opuslabs.substack.com/p/how-to-flip-bits-in-the-world)

无法访问文章链接。

---

## 36. 望远镜远程托管

**原文标题**: Remote hosting for your telescope

**原文链接**: [https://www.sierra-remote.com/](https://www.sierra-remote.com/)

塞拉遥感天文台(SRO)在内华达山脉提供远程望远镜托管服务，为天文成像、数据采集、卫星跟踪和太空通信提供基础设施、技术支持和优异的视宁度。

SRO拥有超过180台在运行的望远镜，自2007年以来一直为大学、科研机构、航天工业专业人士和天文摄影师提供服务。主要特点包括：

*   卓越的视宁度：夏季视宁度1角秒，冬季视宁度1.2角秒，峰值视宁度小于1角秒，暗夜环境，以及极小的风力。
*   可靠的基础设施：24/7全天候技术支持，光纤互联网（1 Gbps，可提供更高的速度），星链备份，安全VPN，现场机加工车间和发电机备份。
*   便利的交通：从弗雷斯诺-约塞米蒂国际机场可轻松抵达。

SRO在共享、私人和定制天文台中提供望远镜托管服务。托管套餐包括墩位空间、电力、互联网、网络服务、遥测和现场支持。 他们还通过iTelescope.net提供望远镜租赁服务，该公司在SRO运营一台24英寸的PlaneWave CDK望远镜。 对于那些希望购买、租赁或共享望远镜的人，SRO网站上有一个公告栏部分。 基础托管价格起价为每月600美元。

---

## 37. 自动存档YouTube视频的浏览器扩展和本地后端

**原文标题**: Browser extension and local backend that automatically archives YouTube videos

**原文链接**: [https://github.com/andrewarrow/starchive](https://github.com/andrewarrow/starchive)

Starchive 是一个旨在自动归档您访问的 YouTube 视频的系统。它包含一个 Firefox 浏览器扩展和一个本地 Go 后端。该扩展程序检测 YouTube 视频页面，提取视频 ID，并将其发送到 Go 后端。

Go 后端在端口 3009 上运行服务器，使用 `yt-dlp` 和 `ffmpeg` 下载视频并将其转换为采用 h264_videotoolbox 编码的 MOV 格式，从而利用硬件加速。它还旨在下载 VTT 格式的英文字幕（目前因重试循环而禁用）。视频保存在 `./data/` 目录中。

Firefox 扩展具有一个内容脚本 (`content.js`) 用于识别 YouTube 视频页面，一个后台脚本 (`background.js`) 用于与 Go 后端 API 通信，以及一个弹出界面 (`popup.html/js`) 用于手动获取数据。

要使用 Starchive，您首先启动 Go 后端 (`go run .`)，然后加载 Firefox 扩展。访问 YouTube 视频页面将自动触发归档过程。该系统需要 `yt-dlp`、`ffmpeg` 和 Go 才能运行。作者明确声明此项目与网站 starchive.io 无关。

---

## 38. 将冰岛语姓名变格模式压缩成3.27 kB的trie树

**原文标题**: Compressing Icelandic name declension patterns into a 3.27 kB trie

**原文链接**: [https://alexharri.com/blog/icelandic-name-declension-trie](https://alexharri.com/blog/icelandic-name-declension-trie)

本文详细介绍了如何创建一个 JavaScript 库，用于对冰岛语人名应用语法格。冰岛语使用变格，根据语法格改变名词形式。由于姓名通常以主格形式存储，这带来了挑战。作者通过创建一个库来解决这个问题，该库从公开的冰岛语数据（特别是冰岛语形态数据库 (DIM) 和个人姓名注册表）中推导出变格规则。

该库将数据压缩成类似 Trie 树的数据结构，以最大限度地减少包大小。最初的方法是将变格数据存储为名称形式的数组，但事实证明这太大了。因此实施了一种更有效的“后缀编码”方法，为每个名称的形式存储最长公共前缀和后缀。Trie 树数据结构用于将反转的名称字符串映射到这些后缀编码，从而对具有相似结尾的名称进行分组。然后应用 Trie 树压缩，合并具有公共值的子树，从而进一步减小数据大小。

这种压缩导致了泛化；该库现在可以通过识别后缀中的模式来处理初始数据集中未明确包含的名称。最终的库实现了小于 4.5kB（gzip 压缩后）的包大小，使其适合包含在 Web 应用程序中，而不会显着增加其大小，并允许在用户界面中正确使用冰岛语名称的语法格。

---

## 39. 代数守门人

**原文标题**: The Algebra Gatekeepers

**原文链接**: [https://www.educationprogress.org/p/the-algebra-gatekeepers](https://www.educationprogress.org/p/the-algebra-gatekeepers)

代数守门人：学校如何系统性地剥夺学业合格的学生，特别是低收入和少数族裔学生，选修高等数学课程的机会，从而阻碍他们的长期学业发展轨迹。北卡罗来纳州的研究表明，超过一半被预测能在八年级代数中取得成功的学生没有被录取，通常是因为教师的推荐凌驾于学业成绩之上。

这种分班差距后果严重。八年级学习代数的学生更有可能在高中阶段学习高等数学和科学课程，并在大学入学考试中表现更好。该研究发现，通过对五年级教师的采访揭示，教育工作者中的偏见会影响分班决定，常常使少数族裔学生处于不利地位。

文章强调，即使干预措施成功提高了弱势学生的数学成绩，固定数量的高等数学课程和缺乏合格教师仍然会阻止他们获得这些机会。此外，文章揭示了校长领导力和家长参与对数学分班的重大影响。最后，这些问题并非仅限于北卡罗来纳州；研究表明，这是一个在全国范围内存在了几十年的普遍问题，由社会阶层和不公平的分班做法所延续。

---

## 40. 职业怀疑主义危机

**原文标题**: The Crisis of Professional Skepticism

**原文链接**: [https://mitchhorowitz.substack.com/p/the-crisis-of-professional-skepticism](https://mitchhorowitz.substack.com/p/the-crisis-of-professional-skepticism)

无法访问文章链接。

---

## 41. Ruby 正则表达式中的 /o 代表 “天啊，人类啊！”

**原文标题**: The /o in Ruby regex stands for "oh the humanity "

**原文链接**: [https://jpcamara.com/2025/08/02/the-o-in-ruby-regex.html](https://jpcamara.com/2025/08/02/the-o-in-ruby-regex.html)

本文深入探讨了Ruby正则表达式修饰符`/o`这个晦涩且潜在危险的特性，揭示了其令人惊讶的行为以及引入混淆性错误的可能。作者回顾了一次调试经历，其中`/o`修饰符导致正则表达式中首次插值的值被意外缓存，从而导致错误的匹配。

核心问题在于，`/o`（插值模式）会在首次评估后缓存已编译的正则表达式对象，并在所有后续调用中使用相同的正则表达式，即使输入不同。通过Ruby VM字节码分析解释了这种行为，表明`once`指令确保正则表达式在整个Ruby进程中只被评估一次。

本文展示了这种缓存的含义，包括多线程场景中的不确定行为以及递归调用中的意外结果。作者强烈建议不要使用`/o`修饰符，认为潜在的性能提升不如不可预测行为的风险。

最后，本文揭示了一种强制重新评估`/o`修饰符的方法：重新加载代码，因为这会触发Ruby的完全重新评估。虽然本文提供了一瞥Ruby内部机制的机会，但其中心信息是对使用`/o`修饰符的明确警告，因为它可能引入难以调试的问题。

---

## 42. 用 Common Lisp 编写的操作系统 Mezzano

**原文标题**: Mezzano, an operating system written in Common Lisp

**原文链接**: [https://github.com/froggey/Mezzano](https://github.com/froggey/Mezzano)

Mezzano 是一个用 Common Lisp 编写的操作系统。演示版本可通过 GitHub 获取，主要为 VirtualBox（支持 QEMU）在 x86-64 架构上设计。AArch64 支持存在，但需要在特定硬件上进行大量用户配置。

可以通过 MBuild 仓库从源代码构建。用户可以加入 #mezzano IRC 频道以获得支持。

自 Demo 4 以来的主要改进包括 USB 协议栈、改进的文件系统支持（兼容 EXT2/3/4）、GMA950 模式设置显示驱动程序、通过 Virgl 实现的硬件加速 3D、多核支持、增强的原子操作、异步 API 和网络改进。还包括源代码位置跟踪、弱哈希表、对象表示清理、非装箱结构槽、短浮点数、非装箱算术、堆栈溢出/内存错误恢复、Windows 构建支持以及 CLOS/MOP 一致性增强。

Demo 3 带来了 FAT32 支持、McCLIM 移植、Quicklisp 移植、改进的内省工具（DISASSEMBLE、ED）、分代垃圾回收、新的编译器后端和灰色流的全面改进。

Demo 2 引入了 Trentino 媒体播放器、改进的一致性/稳定性/性能、CLOS MOP 对齐、传统的窗口管理、真实硬件上的 CD/USB 启动、Intel HDA 音频驱动程序支持和 VirtualBox 客户机集成。

早期的演示侧重于核心功能、性能增强、编辑器改进、增加的 RAM 支持、内存管理、透明度和错误修复。该操作系统包括 Dejavu 字体、来自 Icojam 的一些图标，并使用在各种 Creative Commons 许可下的图像。

---

## 43. Show HN：WebGPU 使浏览器能够运行本地 LLM – 包含 AI 聊天的演示网站

**原文标题**: Show HN: WebGPU enables local LLM in the browser – demo site with AI chat

**原文链接**: [https://andreinwald.github.io/browser-llm/](https://andreinwald.github.io/browser-llm/)

此“Show HN”提交展示了一个基于 Web 的演示，该演示展示了直接在 Web 浏览器中运行大型语言模型 (LLM) 的能力，利用了 WebGPU API。 核心成就在于消除了对服务器端 LLM 的需求，从而将 AI 聊天功能引入到客户端。 通过利用 WebGPU (它提供对设备 GPU 的访问)，与仅依赖 JavaScript 相比，该演示能够实现更快、更高效的 LLM 推理。 这种方法提供了几个潜在的好处，包括：

*   **隐私：** 数据保留在用户的本地浏览器中，提高了隐私性，因为查询不会发送到外部服务器。
*   **降低延迟：** 消除服务器通信可最大限度地缩短响应时间，从而带来更具交互性的体验。
*   **离线功能：** 由于模型和执行都在本地发生，因此即使没有互联网连接，应用程序也可能可以运行。
*   **节省成本：** 无需服务器资源来运行 LLM，从而降低了运营成本。

此提交很可能是在演示 WebGPU 为客户端 AI 开辟的可能性，可能会激发人们对直接在浏览器环境中开发更复杂、更注重隐私的 AI 应用程序的兴趣。“AI 聊天”元素表明用户可以使用一种易于访问的界面与本地 LLM 进行交互。

---

## 44. 微软开源Windows 11的UI框架

**原文标题**: Microsoft is open sourcing Windows 11's UI framework

**原文链接**: [https://www.neowin.net/news/microsoft-is-taking-steps-to-open-sourcing-windows-11-user-interface-framework/](https://www.neowin.net/news/microsoft-is-taking-steps-to-open-sourcing-windows-11-user-interface-framework/)

微软正逐步开源其Windows 11用户界面框架WinUI，但由于其复杂性以及与Windows专有组件的深度集成，这是一个分阶段的过程。该公司致力于与WinUI建立更加开放和协作的未来，但这并非一蹴而就。

在接下来的六个月里，微软将经历四个阶段：
1. **提高镜像频率：** 更频繁地将内部代码更改镜像到公共GitHub存储库，从WASDK 1.8版本发布后（8月底）开始。
2. **本地构建：** 外部开发人员将能够克隆并在本地构建WinUI存储库，并提供文档。
3. **贡献与测试：** 第三方开发人员将能够提交拉取请求（PR）并在本地运行测试，因为微软正在解除私有依赖关系。
4. **GitHub作为重心：** GitHub将成为开发、问题跟踪和社区互动的主要中心，逐步淘汰内部镜像。

微软强调，安全性、稳定性和对现有产品的支持仍然是优先事项。进度可以在GitHub看板上跟踪。开发人员可以通过提供反馈、报告有据可查的问题以及赞成现有建议来做出贡献。开源过程是深思熟虑且渐进的。

---

## 45. 我家购买长期护理保险的经验教训

**原文标题**: Financial lessons from my family's experience with long-term care insurance

**原文链接**: [https://www.whitecoatinvestor.com/financial-lessons-father-long-term-care-insurance/](https://www.whitecoatinvestor.com/financial-lessons-father-long-term-care-insurance/)

怀特大褂投资人网站上的文章“从我家长期护理保险经验中得到的财务教训”讨论了作者家庭的长期护理（LTC）保险经验以及从中汲取的教训。作者的父亲在60多岁时购买了长期护理保险，最终在80多岁时需要大量使用它，这证明了这种保险的潜在价值。

这篇文章强调了几个关键的财务教训：

*   **长期护理保险可以保护资产：** 该保单显著抵消了长期护理的高昂费用，为他的配偶和继承人保留了父亲的大部分遗产。如果没有它，大量的资产将会耗尽。

*   **尽早购买而不是稍后购买：** 在60多岁时购买保单是有益的，因为保费低于晚年购买时，尽管父亲在需要保险之前支付了近20年的保费。

*   **了解保单细节：** 作者强调了理解保单细节的重要性，包括每日福利金额、通货膨胀保护、免赔额和承保服务。了解这些细节对于最大化利益和避免意外至关重要。

*   **长期护理保险并不适合所有人：** 作者承认长期护理保险可能不适合所有人，特别是那些资产有限或已经足够富有可以自我保险的人。这是一个复杂的决定，需要仔细考虑个人情况和财务资源。

*   **通货膨胀附加条款至关重要：** 作者强调了长期护理保单中通货膨胀保护附加条款的重要性，以确保福利能够跟上护理成本随时间的上涨。

总之，这篇文章认为，虽然长期护理保险并非万能的解决方案，但它可以成为保护资产和提供安心的宝贵工具，尤其是在经过深思熟虑并清楚了解其条款的情况下购买时。作者家庭的经验证明了长期护理保险在减轻长期护理需求的财务负担方面的潜在好处。

---

## 46. OpenAI的“学习模式”与奉承的风险

**原文标题**: OpenAI's "Study Mode" and the risks of flattery

**原文链接**: [https://resobscura.substack.com/p/openais-new-study-mode-and-the-risks](https://resobscura.substack.com/p/openais-new-study-mode-and-the-risks)

无法访问文章链接。

---

## 47. Falcon-H1：重新定义效率与性能的混合头模型系列

**原文标题**: Falcon-H1: A Family of Hybrid-Head Models Redefining Efficiency and Performance

**原文链接**: [https://arxiv.org/abs/2507.22448](https://arxiv.org/abs/2507.22448)

本技术报告介绍了 Falcon-H1，一种为高性能和高效率而设计的新型大型语言模型 (LLM) 系列。其关键创新在于混合架构，将基于 Transformer 的注意力机制与状态空间模型 (SSM) 相结合，以利用两者的优势：Transformer 的通用能力以及 SSM 的长上下文记忆和计算效率。

Falcon-H1 系列发布了多种配置，参数范围从 0.5B 到 34B 不等，包括基础和指令调优变体，甚至量化版本，在 Hugging Face Hub 上总共有 30 多个检查点。

一个核心论点是，Falcon-H1 模型以卓越的参数和训练效率实现了最先进的性能。据报道，旗舰 34B 模型在规模上与高达 70B 的模型（Qwen3-32B、Qwen2.5-72B 和 Llama3.3-70B）的性能相匹配或超过，同时使用了更少的参数和更少的训练数据。较小的模型也表现出令人印象深刻的结果，其中 1.5B-Deep 模型可与当前的 7B-10B 模型相媲美，而 0.5B 模型与 2024 年的典型 7B 模型表现相似。

这些模型在推理、数学、多语言任务、指令遵循和科学知识方面表现出强大的能力，并支持高达 256K 的上下文标记和 18 种语言。Falcon-H1 模型以宽松的开源许可证发布，从而促进了人工智能研究中的更广泛访问和影响。作者重新审视了模型设计、数据策略和训练动态，挑战了 LLM 开发中的传统实践。

---

## 48. 在光线中隐藏秘密代码可防止伪造视频

**原文标题**: Hiding secret codes in light protects against fake videos

**原文链接**: [https://news.cornell.edu/stories/2025/07/hiding-secret-codes-light-protects-against-fake-videos](https://news.cornell.edu/stories/2025/07/hiding-secret-codes-light-protects-against-fake-videos)

康奈尔大学研究人员开发了一种新方法来打击虚假视频，通过“水印”光源，使其产生几乎无法察觉的波动，从而编码一个秘密代码。任何在加水印光源下录制的视频都能捕捉到这种隐藏的水印，使事实核查人员能够验证素材的真实性并检测篡改行为。

该系统的工作原理是将信息嵌入到计算机屏幕和灯具等光源发出的光中，从而在常规视频之外创建一个“代码视频”。这个代码视频包含一个带有时间戳的，在略微不同的光照条件下拍摄的未被篡改场景的版本。如果视频被篡改，被篡改的部分和代码视频之间会出现不一致，从而揭示篡改行为。即使是人工智能生成的虚假视频也会在代码视频中产生随机变化，使其易于识别。

这些水印通过模仿光线中的自然“噪声”来设计成肉眼无法察觉。该系统具有很强的适应性，可以通过软件编码或小型计算机芯片与各种光源配合使用。研究人员已成功在一个场景中实施多个代码，这使得恶意行为者更难伪造光线。虽然前景广阔，但该团队警告说，打击虚假信息的斗争仍在继续，对手可能会不断适应。

---

## 49. 卡诺模型

**原文标题**: Kano Model

**原文链接**: [https://en.wikipedia.org/wiki/Kano_model](https://en.wikipedia.org/wiki/Kano_model)

狩野模型，由狩野纪昭开发，是一种用于产品开发和客户满意度的理论，它帮助组织确定开发工作的优先级。它将客户偏好分为五种类型，每种类型对满意度的影响各不相同：

1.  **必备品质：** 客户期望的基本要求；其存在只会导致中性，而缺失会导致不满（例如，汽车中正常工作的刹车）。
2.  **一维品质：** 当满足时会引起满意，不满足时会引起不满的属性，通常是竞争的焦点（例如，相同价格的包装中含有更多的牛奶）。
3.  **魅力品质：** 存在时会让客户愉悦的意外功能，但缺失时不会引起不满（例如，汽车中的高级停车传感器）。
4.  **无关紧要的品质：** 既不会让客户满意也不会让客户不满意的属性（例如，牛奶纸盒上蜡涂层的厚度）。
5.  **反向品质：** 过高的成就度会导致不满意的属性，因为并非所有客户都希望有额外的功能（例如，呼叫中心中过多的术语）。

客户期望会不断发展，导致属性随着时间的推移从“令人愉悦的功能”转变为基本需求。狩野模型通过标准化的问卷调查来衡量，询问功能的正面（积极）和负面（消极）方面。结合答案可以揭示功能类别。该模型用于质量功能展开（QFD），通过了解客户偏好并支持产品规格讨论来提高产品质量。

---

## 50. 澳大利亚小麦农场生产力增长

**原文标题**: Australia’s gains in wheat-farm productivity

**原文链接**: [https://www.reuters.com/investigations/less-rain-more-wheat-how-australian-farmers-defied-climate-doom-2025-07-29/](https://www.reuters.com/investigations/less-rain-more-wheat-how-australian-farmers-defied-climate-doom-2025-07-29/)

澳大利亚小麦农场生产力增长概要 (基于标题及URL推测内容):

路透社文章《澳大利亚小麦农场生产力增长》可能探讨了澳大利亚小麦农场在日益严峻的气候条件，特别是降雨减少和干旱频率增加的情况下，如何设法提高产量并保持竞争力，尽管最初预测农业会因气候变化而衰退。

该文章可能详细介绍了农民为应对这些挑战而采取的各种策略和创新。关键因素可能包括：

*   **采用耐旱小麦品种：** 培育和种植更能抵抗水分胁迫并在更干燥条件下生长的小麦品种。
*   **改进土壤管理技术：** 实施免耕种植、秸秆覆盖和精准农业等方法，以改善土壤健康、保水能力和养分有效性。
*   **技术进步：** 利用 GPS 引导机械、遥感和数据分析等先进技术来优化种植、施肥和灌溉实践。
*   **转变耕作方式：** 调整播种时间、作物轮作和其他农艺措施，以更好地适应不断变化的天气模式并最大限度地提高用水效率。
*   **政府支持和研究：** 强调政府对农业研究和发展的投资，以及支持农民采用可持续和气候适应型措施的政策的作用。

该文章可能强调澳大利亚的成功并非必然，随着气候变化的进展，需要持续创新才能维持生产力。

---

## 51. 社交媒体如何缩短你的寿命，以及如何延长它

**原文标题**: How Social Media Shortens Your Life and How to Expand It

**原文链接**: [https://www.gurwinder.blog/p/how-social-media-shortens-your-life](https://www.gurwinder.blog/p/how-social-media-shortens-your-life)

本文认为社交媒体平台被刻意设计成通过窃取时间和损害我们的意识及记忆来缩短我们感知和实际的生命。社交媒体通过借鉴赌场设计的技巧来实现这一点，将信息流变成“曲线迷宫”，让用户被动地无休止地滚动，没有明确的开始或结束，从而扰乱他们的时间感。

作者解释了社交媒体如何阻碍当前的意识和回顾性记忆。 不断涌现的令人震惊但最终是常规的内容使大脑麻木，难以记住所看到的内容。 此外，无限滚动和自动播放等功能使使用者陷入被动状态，而通知和大量信息分散了注意力，导致焦虑、压力和“切换成本效应”。

文章将社交媒体的使用与对健康的负面影响联系起来，包括睡眠周期紊乱、精神健康问题以及可能加速衰老。 由于持续的迷失方向而与现实脱节，我们的生物生命也可能缩短。

作者建议通过戒除社交媒体并注意其他技术（如聊天机器人）中类似的时间扭曲策略来逃脱这种陷阱。 关键是避免迷失在“曲线迷宫”中，而是追求清晰、有意识的目标，以保持对时间的意识和控制。 最终，夺回时间不仅仅是抵制特定的平台，也是抵制操纵我们注意力的设计模式。

---

## 52. 受够了糟糕的PDF WebApp，所以我们做了一个免费、开源、私有的替代品

**原文标题**: Got tired of bad PDF WebApp so we made a Free, Open-Sourced, Private Alternative

**原文链接**: [https://luxpdf.com](https://luxpdf.com)

LuxPDF：一款免费、开源、注重隐私的 PDF 网络应用替代方案。开发者（一群大学生）对现有服务的隐私泄露、笨拙界面和订阅模式不满，创建了 LuxPDF，旨在直接在用户设备上执行所有 PDF 转换和修改，无需服务器上传和数据收集。

LuxPDF 提供超过 15 种工具，包括 PDF 转换为 PNG 和 JPEG，PNG/JPEG 转换为 PDF，PDF 转换为 TXT，TXT 转换为 PDF，PDF 合并/分割/压缩/旋转，元数据和密码移除，页面提取/移除/重新排列等。该服务拥有无限使用次数，无需注册。

开发者强调其对隐私和用户体验的承诺，突出平台轻量、高效的代码以及用户文件从不离开其设备的事实。 LuxPDF 通过赞助和自愿捐款获得资金，避免了广告和数据收集。 创作者鼓励社区贡献，如错误报告、功能建议和经济支持。 他们将 LuxPDF 定位为优于竞争对手的选择，提供免费、无限且私密的服务，优先考虑用户隐私和简洁的用户界面。 目标受众包括学生、自由职业者、小企业、技术爱好者以及任何寻求更好 PDF 网络应用的人。

---

## 53. 海里昂启动华盛顿核聚变工厂建设

**原文标题**: Helion begins work on Washington nuclear fusion plant

**原文链接**: [https://www.nucnet.org/news/microsoft-backed-fusion-company-begins-work-on-washington-nuclear-fusion-plant-7-4-2025](https://www.nucnet.org/news/microsoft-backed-fusion-company-begins-work-on-washington-nuclear-fusion-plant-7-4-2025)

微软支持的核聚变公司Helion开始建造其首个聚变电站Orion，目标是在2028年前向微软数据中心供电，该电站位于华盛顿州。此前，微软已同意从Helion购买高达50兆瓦的电力，这使其成为全球首个核聚变电力购买协议。

Helion的第七代原型机Polaris旨在演示聚变发电。他们之前的原型机Trenta实现了1亿摄氏度的燃料温度，这是商业聚变的必要条件。该公司强调，这一时间表比商业聚变部署的典型预测更快。

Helion需要获得州政府的最终许可，但仍有望在2028年前交付电力。该公司由OpenAI创始人Sam Altman支持，最近在F轮融资中筹集了4.25亿美元，使其总融资额超过10亿美元，估值达到54亿美元。

文章还指出，谷歌已与另一家聚变公司Commonwealth Fusion Systems签署了200兆瓦的电力购买协议，用于其ARC电站的电力，预计该电站将于2030年代初向弗吉尼亚电网供电。与裂变不同，聚变有望提供近乎无限且更清洁的能源。

---

## 54. 人们仍然在使用我们老式的Unix登录服务器。

**原文标题**: People still use our old-fashioned Unix login servers

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/sysadmin/LoginServersStillUsed](https://utcc.utoronto.ca/~cks/space/blog/sysadmin/LoginServersStillUsed)

由于大量网络爬虫（特别是那些模仿旧版Chrome用户代理的爬虫，可能被用于LLM训练数据收集）的涌入，Chris Siebenmann的博客“Wandering Thoughts”正在阻止使用旧版浏览器的用户访问。他采取这项措施是为了减轻这些爬虫给博客造成的负载。

如果使用当前浏览器的合法用户被错误阻止，他们应通过大学邮箱（可通过上下文线索获取）联系Siebenmann，并提供他们的浏览器详细信息，包括User-Agent字符串。

他特别提到了通过archive.today、archive.ph和archive.is等存档服务访问博客的用户。他批评这些服务的行为与恶意爬虫类似，使用了过时的Chrome用户代理，从广泛的IP范围进行爬取，有时还使用误导性的反向DNS条目。他建议使用archive.org，因为它是一个行为更规范的存档爬虫，能够访问他的博客。该文章发布于2025年2月17日。

---

## 55. 朝鲜派他出国做秘密IT工作者。

**原文标题**: North Korea sent him abroad to be a secret IT worker

**原文链接**: [https://www.bbc.com/news/articles/c15wk77zxngo](https://www.bbc.com/news/articles/c15wk77zxngo)

朝鲜秘密派遣公民海外充当IT工人，为政权创收，规避国际制裁：一名叛逃者揭秘内幕

---

## 56. 代币越来越贵了

**原文标题**: Tokens are getting more expensive

**原文链接**: [https://ethanding.substack.com/p/ai-subscriptions-get-short-squeezed](https://ethanding.substack.com/p/ai-subscriptions-get-short-squeezed)

Tokens 变得更贵”摘要

---

## 57. 双缝实验精简至量子本质依然成立

**原文标题**: Double-slit experiment holds up when stripped to its quantum essentials

**原文链接**: [https://news.mit.edu/2025/famous-double-slit-experiment-holds-when-stripped-to-quantum-essentials-0728](https://news.mit.edu/2025/famous-double-slit-experiment-holds-when-stripped-to-quantum-essentials-0728)

麻省理工学院物理学家进行了理想化的双缝实验，证实了量子力学的基本原理，并解决了爱因斯坦和玻尔之间长期存在的争论。双缝实验著名地展示了光既可以表现为波，也可以表现为粒子，但这些特性不能同时观察到。

麻省理工学院的团队使用单个原子作为狭缝，并使用弱光束散射单个光子。通过操纵原子的量子态，他们可以控制有关光子路径的信息。他们的发现证实，增加对光子路径的了解（粒子性质）会降低波状干涉图样的可见性。

这项实验为玻尔对量子力学的解释提供了强有力的支持，驳斥了爱因斯坦关于可以通过检测光子对狭缝施加的力来同时观察波和粒子性质的观点。该团队还证明了先前用于概念化实验的“弹簧”（代表固定狭缝的方法）并非至关重要；关键因素是原子位置的“模糊性”或不确定性。这种理想化的设置，在单原子和单光子水平上工作，加强了量子力学违反直觉的本质及其对我们理解现实的影响。通过他们的实验，研究人员提供了一种更深刻的描述，该描述使用了光子和原子之间的量子关联。

---

## 58. 哨兵2号影像超分辨率重建 (10米 -> 5米)

**原文标题**: Super-resolution of Sentinel-2 images (10M –> 5M)

**原文链接**: [https://github.com/Topping1/L1BSR-GUI](https://github.com/Topping1/L1BSR-GUI)

本文介绍了一款用户友好的桌面应用程序“Sentinel-2超分辨率GUI”，旨在将Sentinel-2卫星图像的分辨率从10米提升到5米。它使用预训练的AI模型（REC_Real_L1B.safetensors）来放大蓝色、绿色、红色和近红外（NIR）波段。

该应用程序具有简单的图形界面，无需使用命令行工具。用户加载模型和四个Sentinel-2波段文件（B02、B03、B04、B08），文件格式为TIFF，并具有UTM坐标系。处理后，将生成2倍超分辨率图像，并显示预览，用户可以通过点击并按住预览来比较放大后的图像与原始图像。可以选择应用可选的非锐化掩模滤镜以进行视觉锐化。

输出可以保存为GeoTIFF（保留地理数据）或JPG（带有JGW世界文件，以实现GIS兼容性）。该应用程序需要Python 3和`pyqt5`、`torch`、`safetensors`、`rasterio`、`pillow`和`numpy`等库。建议使用CUDA进行GPU加速以加快处理速度。另一个版本`L1-BSR-GUI-ONNX.py`使用OnnxRuntime进行推理，需要的库集较少，并使用Onnx模型。

该应用程序基于L1BSR项目，并根据GNU General Public License v3.0获得许可。

---

## 59. 为什么皮革是最佳摩托车保护 [视频]

**原文标题**: Why leather is best motorcycle protection [video]

**原文链接**: [https://www.youtube.com/watch?v=xwuRUcAGIEU](https://www.youtube.com/watch?v=xwuRUcAGIEU)

这是一个名为“为何皮革是最佳摩托车防护”的YouTube视频。然而，提供的内容只是标准的YouTube页脚信息，包括法律页面链接、联系方式和版权声明。没有关于视频内容或皮革为何是最佳摩托车防护的论点的实际信息。因此，不可能根据给定的信息总结视频内容。

---

## 60. 不使用抽象语法树的解析及使用节点海洋优化 [视频]

**原文标题**: Parsing without ASTs and Optimizing with Sea of Nodes  [video]

**原文链接**: [https://www.youtube.com/watch?v=NxiKlnUtyio](https://www.youtube.com/watch?v=NxiKlnUtyio)

提供的内容并非文章，而是通常位于 YouTube 页面底部的样板文字。它混合了导航链接和版权信息。

因此，无法总结不存在的文章。该文本包含：

*   **链接：** 指向各种 YouTube 资源的链接，如“关于”、“新闻”、“联系我们”、“创作者”、“广告”、“开发者”、“条款”、“隐私”和“政策与安全”。
*   **版权信息：** 包括版权声明（© 2025 Google LLC）以及关于 NFL Sunday Ticket 的信息。
*   **一般信息：** “YouTube 的运作方式”和“测试新功能”。

本质上，这只是 YouTube 网页的标准页脚信息，与“Parsing without ASTs and Optimizing with Sea of Nodes”无关。此处没有任何与视频标题相关的内容。

---

## 61. 深入探讨开放聊天协议

**原文标题**: A dive into open chat protocols

**原文链接**: [https://wiki.alopex.li/ADiveIntoOpenChat](https://wiki.alopex.li/ADiveIntoOpenChat)

本文介绍了某网站实施的名为“阿努比斯”的安全措施，该措施旨在阻止人工智能公司过度抓取其内容。网站管理员认为，这种抓取会导致网站宕机并使资源无法访问。

“阿努比斯”采用类似于Hashcash的“工作量证明”机制，要求用户执行少量计算来证明其不是机器人。虽然对单个用户来说，计算量很小，但对于大规模抓取者来说，计算量会变得非常显著，从而增加抓取的成本。

本文强调，“阿努比斯”只是一个临时解决方案。最终目标是开发更复杂的指纹识别和身份识别技术，针对无头浏览器（通常被抓取器使用），基于字体渲染等特征进行识别。这样，网站就可以只向可疑用户显示“工作量证明”挑战，从而最大限度地减少对合法访问者的不便。

文章还指出，“阿努比斯”需要JavaScript，用户可能需要禁用JShelter等插件才能通过挑战。这一要求源于人工智能公司改变了网站托管的预期行为，使得采取此类措施成为必要。未来正在考虑采用“无JavaScript”的解决方案。

---

## 62. CI中的基准测试：摆脱云混沌

**原文标题**: Benchmarks in CI: Escaping the Cloud Chaos

**原文链接**: [https://codspeed.io/blog/benchmarks-in-ci-without-noise](https://codspeed.io/blog/benchmarks-in-ci-without-noise)

本文探讨了在持续集成 (CI) 环境中运行可靠性能基准测试所面临的挑战，尤其是在诸如 GitHub Actions 等云托管 runners 中由于 "嘈杂邻居" 问题。 文章强调了尽早发现性能衰退以防止对用户体验、成本和开发效率产生负面影响的重要性。

作者证明了 GitHub 托管 runners 具有较高的变异系数 (2.66%)，导致在试图检测即使是很小 (2%) 的性能衰退时也会产生显著的假阳性率 (45%)。 这使得性能门不可靠，并削弱了对基准测试过程的信任。

为了解决这个问题，本文介绍了 "CodSpeed Macro Runners"，这是一种基于裸机实例且具有为高精度基准测试设计的操作系统级优化的解决方案。 这些 Macro Runners 大幅降低了方差 (0.56%)，从而导致假阳性率大大降低。 使用相同的 2% 性能门，假阳性率降至 0.04%。

文章强调，将 CodSpeed Macro Runners 集成到现有 CI 工作流程中只需要进行极少的更改，主要通过更改 GitHub Actions 中的 `runs-on` 字段。 最后，文章主张在 CI 中使用可靠的性能数据，以改善用户体验、降低成本、增强开发者反馈循环以及减少部署后的调试。 文章还承诺未来将深入探讨其基础设施的技术细节。

---

## 63. Show HN: NaturalCron – .NET 人性化可读调度器（带流畅构建器）

**原文标题**: Show HN: NaturalCron – Human-Readable Scheduling for .NET (With Fluent Builder)

**原文链接**: [https://github.com/hugoj0s3/NaturalCron](https://github.com/hugoj0s3/NaturalCron)

NaturalCron 是一个 .NET 库，旨在通过使用人类可读的表达式（而不是复杂的 cron 字符串）来简化调度任务。它旨在通过允许开发人员使用直观的语法（例如“在 [jan, jun] 中每隔 30 分钟，时间在 09:00 到 18:00 之间”）来定义计划，从而提高代码的可读性并减少错误。

主要功能包括支持范围、工作日列表、首日/末日处理以及使用 IANA TZ 名称的时区支持。 NaturalCron 不是 cron 转换器，而是一种新的表达语法，专注于增强可读性。

该库提供了两种定义计划的方式：

*   **使用表达式：** 解析基于字符串的人类可读表达式。
*   **使用 Fluent Builder API：** 一个为 .NET 开发人员提供的具有 IntelliSense 支持的强类型 API。

本文展示了比较常见调度任务的 cron 表达式和 NaturalCron 表达式的示例。 它还包括安装说明 (`dotnet add package NaturalCron`)、文档链接，并鼓励对该项目做出贡献和支持。 最后，它强调这种方法消除了对在线 cron 表达式生成器的需求。

---

## 64. 交友

**原文标题**: Friending

**原文链接**: [https://www.profgalloway.com/friending/](https://www.profgalloway.com/friending/)

斯科特·加洛韦的文章《交友》强调了美国男性亲密友谊数量的下降及其负面后果。他引用统计数据表明，报告至少有六个亲密朋友的男性人数显著下降，而报告零朋友的人数则在上升。这种缺乏社会联系的情况导致了诸如绝望性死亡、成瘾、厌女症以及作为伴侣、雇员和公民的整体不足等问题。

加洛韦强调了与令人印象深刻的优秀人士为伍，并在任何年龄积极寻求新友谊的重要性。他挑战了随着年龄增长而变得社交停滞的趋势，倡导突破舒适区并对新的联系持开放态度。他分享了晚年建立友谊的轶事，包括主动联系他钦佩的人。

这篇文章还涉及加洛韦的个人经历，强调了他对与女性友谊的看法是如何演变的。他鼓励读者克服不安全感，不要被他人吓倒，就像他曾经那样。他最后强调了生活的丰富性以及不断扩大社交圈以学习和成长的价值。这篇文章也是对他新书《男人札记》的宣传，并包含了读者分享他们自己关于友谊重要性的经历和观点的评论。

---

## 65. 编写“永久产权”软件

**原文标题**: Write "Freehold" Software

**原文链接**: [https://deadbeef.io/freehold_software](https://deadbeef.io/freehold_software)

这篇文章实际上只是一个指向 `deadbeef.io` 网站的链接，并附带消息“错误：发生未知错误。” 除此之外，没有实质内容可以总结。

因此，要点是网站 `deadbeef.io` 与名为“Freehold”的软件或项目相关联，但访问该网站会产生未知错误。 我们可以推断该网站目前已关闭、遇到技术困难，或者通过提供的URL访问有关“Freehold”软件的信息时出现问题。 用户本想访问该网站以了解有关“Freehold”软件的更多信息，但却遇到了错误。

---

## 66. 罗伯特·威尔逊去世了

**原文标题**: Robert Wilson has died

**原文链接**: [https://www.theartnewspaper.com/2025/08/01/robert-wilson-playwright-director-artist-obituary](https://www.theartnewspaper.com/2025/08/01/robert-wilson-playwright-director-artist-obituary)

极具影响力的实验剧作家、导演和视觉艺术家罗伯特·威尔逊因病于纽约州水磨坊的家中去世，享年83岁。他以其视觉冲击力强、风格化的戏剧作品而闻名，曾与菲利普·格拉斯、劳里·安德森、玛丽娜·阿布拉莫维奇和Lady Gaga等众多艺术家合作。

在长达六十年的职业生涯中，威尔逊的作品，如《聋人一瞥》和（与菲利普·格拉斯合作的）《海滩上的爱因斯坦》，挑战了戏剧规范并获得了国际赞誉。他独特的风格摒弃了自然主义，融合了默片、哑剧和极简主义舞台设计的元素，强调了视觉元素与文本和音乐的重要性。

除了戏剧，威尔逊还是一位多产的视觉艺术家，创作了绘画、雕塑和录像肖像。他的录像肖像系列，以 Lady Gaga、布拉德·皮特和薇诺娜·瑞德等名人为特色，采用古典绘画的风格，曾在卢浮宫等著名机构展出。他还设计展览，尤其是古根海姆博物馆的乔治·阿玛尼回顾展。

威尔逊出生于德克萨斯州一个保守的环境中，在成立伯德·霍夫曼·伯德学校并在纽约市进行表演之前，他学习了舞蹈和建筑学。1992 年，他在长岛创立了水磨坊艺术中心，该中心以其年度慈善晚会而闻名。威尔逊一直认为建筑是他的主要影响，强调光在创造空间和塑造他的艺术视野中的根本作用。

---

## 67. 我如何做支持和社区

**原文标题**: How I do support and community

**原文链接**: [https://pketh.org/support-community.html](https://pketh.org/support-community.html)

本文详细介绍了作者关于其软件Kinopio的客户支持和社区建设的理念和实践方法。作者认为支持不是一项削减成本的活动，而是一个建立强大、积极参与的社区的宝贵机会。他们努力提供卓越的服务，将其比作经营一家以客户体验至上的高品质酒店。

作者平衡了编码和社区参与，承认专注于软件改进与关注用户需求之间的紧张关系。他们通过电子邮件、Discord聊天和Discourse论坛积极地与用户联系，每种渠道都有不同的用途。他们强调积极管理和组织这些沟通渠道的重要性，他们称之为“持续修剪”。

关键策略包括欢迎新社区成员，根据其性质和紧急程度将对话引导至适当的渠道（电子邮件、聊天或论坛），并优先考虑论坛进行长期讨论和知识积累。作者承认转换沟通类型所需的努力，将其视为用户承诺的过滤器。

最终，作者提倡对客户支持采取长远的眼光。他们优先考虑善待现有客户，并认为这对于建立可持续和持久的公司至关重要。他们认为个性化的支持和社区参与是在一个充斥着自动化解决方案的市场中重要的差异化因素。他们强调成为“多对多”的重要性，而不是“一对多”。

---

## 68. Caches: LRU vs. Random

**原文标题**: Caches: LRU vs. Random

**原文链接**: [https://danluu.com/2choices-eviction/](https://danluu.com/2choices-eviction/)

生成摘要时出错

---

## 69. The Rubik's Cube Perfect Scramble (2024)

**原文标题**: The Rubik's Cube Perfect Scramble (2024)

**原文链接**: [https://www.solutionslookingforproblems.com/post/the-rubik-s-cube-perfect-scramble](https://www.solutionslookingforproblems.com/post/the-rubik-s-cube-perfect-scramble)

生成摘要时出错

---

## 70. StreamPark: A streaming application development framework

**原文标题**: StreamPark: A streaming application development framework

**原文链接**: [https://github.com/apache/streampark](https://github.com/apache/streampark)

生成摘要时出错

---

## 71. I tried living on IPv6 for a day

**原文标题**: I tried living on IPv6 for a day

**原文链接**: [https://www.xda-developers.com/the-internet-isnt-fully-ipv6-ready/](https://www.xda-developers.com/the-internet-isnt-fully-ipv6-ready/)

生成摘要时出错

---

## 72. Linear Types for Programmers (2023)

**原文标题**: Linear Types for Programmers (2023)

**原文链接**: [https://twey.io/for-programmers/linear-types/](https://twey.io/for-programmers/linear-types/)

生成摘要时出错

---

## 73. ThinkPad designer David Hill on unreleased models

**原文标题**: ThinkPad designer David Hill on unreleased models

**原文链接**: [https://www.theregister.com/2025/08/02/thinkpad_david_hill_interview/](https://www.theregister.com/2025/08/02/thinkpad_david_hill_interview/)

生成摘要时出错

---

## 74. Show HN: Draw a fish and watch it swim with the others

**原文标题**: Show HN: Draw a fish and watch it swim with the others

**原文链接**: [https://drawafish.com](https://drawafish.com)

生成摘要时出错

---

## 75. JavaScript retro sound effects generator

**原文标题**: JavaScript retro sound effects generator

**原文链接**: [https://github.grumdrig.com/jsfxr/](https://github.grumdrig.com/jsfxr/)

生成摘要时出错

---

## 76. A Letter to the CalyxOS Community

**原文标题**: A Letter to the CalyxOS Community

**原文链接**: [https://calyxos.org/news/2025/08/01/a-letter-to-our-community/](https://calyxos.org/news/2025/08/01/a-letter-to-our-community/)

生成摘要时出错

---

## 77. The case for having roommates even when you can afford to live alone

**原文标题**: The case for having roommates even when you can afford to live alone

**原文链接**: [https://supernuclear.substack.com/p/the-case-for-having-roommates-even](https://supernuclear.substack.com/p/the-case-for-having-roommates-even)

生成摘要时出错

---

## 78. Tim Cook rallying Apple employees around AI efforts

**原文标题**: Tim Cook rallying Apple employees around AI efforts

**原文链接**: [https://www.bloomberg.com/news/articles/2025-08-01/apple-ceo-tells-staff-ai-is-ours-to-grab-in-hourlong-pep-talk](https://www.bloomberg.com/news/articles/2025-08-01/apple-ceo-tells-staff-ai-is-ours-to-grab-in-hourlong-pep-talk)

生成摘要时出错

---

## 79. How to reverse engineer an analog chip: the TDA7000 FM radio receiver

**原文标题**: How to reverse engineer an analog chip: the TDA7000 FM radio receiver

**原文链接**: [https://www.righto.com/2025/08/reverse-engineering-analog-TDA7000.html](https://www.righto.com/2025/08/reverse-engineering-analog-TDA7000.html)

生成摘要时出错

---

## 80. Cerebras Code

**原文标题**: Cerebras Code

**原文链接**: [https://www.cerebras.ai/blog/introducing-cerebras-code](https://www.cerebras.ai/blog/introducing-cerebras-code)

生成摘要时出错

---

## 81. Show HN: Voltpeek – Vim-inspired oscilloscope software

**原文标题**: Show HN: Voltpeek – Vim-inspired oscilloscope software

**原文链接**: [https://github.com/schuyler4/voltpeek](https://github.com/schuyler4/voltpeek)

生成摘要时出错

---

## 82. A Quantum Gravimeter for GPS Backup

**原文标题**: A Quantum Gravimeter for GPS Backup

**原文链接**: [https://spectrum.ieee.org/quantum-gravity-sensor](https://spectrum.ieee.org/quantum-gravity-sensor)

生成摘要时出错

---

## 83. Show HN: Wordle-style game for Fermi questions

**原文标题**: Show HN: Wordle-style game for Fermi questions

**原文链接**: [https://www.fermiquestions.org/](https://www.fermiquestions.org/)

生成摘要时出错

---

## 84. Yearly Organiser

**原文标题**: Yearly Organiser

**原文链接**: [https://neatnik.net/calendar/](https://neatnik.net/calendar/)

生成摘要时出错

---

## 85. Neural networks that learn non-linearity without activation functions [pdf]

**原文标题**: Neural networks that learn non-linearity without activation functions [pdf]

**原文链接**: [https://www.tahabouhsine.com/nmn/assets/deep_learning_two_point_o_point_one.pdf](https://www.tahabouhsine.com/nmn/assets/deep_learning_two_point_o_point_one.pdf)

生成摘要时出错

---

## 86. A laundry-folding robot blew up the Internet. We talked to the inventor

**原文标题**: A laundry-folding robot blew up the Internet. We talked to the inventor

**原文链接**: [https://sfstandard.com/2025/07/30/ai-lamp-laundry-robot-bedroom/](https://sfstandard.com/2025/07/30/ai-lamp-laundry-robot-bedroom/)

生成摘要时出错

---

## 87. Hardening mode for the compiler

**原文标题**: Hardening mode for the compiler

**原文链接**: [https://discourse.llvm.org/t/rfc-hardening-mode-for-the-compiler/87660](https://discourse.llvm.org/t/rfc-hardening-mode-for-the-compiler/87660)

生成摘要时出错

---

## 88. Modeling open-world cognition as on-demand synthesis of probabilistic models

**原文标题**: Modeling open-world cognition as on-demand synthesis of probabilistic models

**原文链接**: [https://arxiv.org/abs/2507.12547](https://arxiv.org/abs/2507.12547)

生成摘要时出错

---

## 89. Native Sparse Attention

**原文标题**: Native Sparse Attention

**原文链接**: [https://aclanthology.org/2025.acl-long.1126/](https://aclanthology.org/2025.acl-long.1126/)

生成摘要时出错

---

## 90. The Big Oops in type systems: This problem extends to FP as well

**原文标题**: The Big Oops in type systems: This problem extends to FP as well

**原文链接**: [https://danieltan.weblog.lol/2025/07/the-big-oops-in-type-systems-this-problem-extends-to-fp-as-well](https://danieltan.weblog.lol/2025/07/the-big-oops-in-type-systems-this-problem-extends-to-fp-as-well)

生成摘要时出错

---

## 91. This Month in Ladybird

**原文标题**: This Month in Ladybird

**原文链接**: [https://ladybird.org/newsletter/2025-07-31/](https://ladybird.org/newsletter/2025-07-31/)

生成摘要时出错

---

## 92. TclSqueak – Program in Tcl the Smalltalk Way

**原文标题**: TclSqueak – Program in Tcl the Smalltalk Way

**原文链接**: [http://www.xdobry.de/tclsqueak/](http://www.xdobry.de/tclsqueak/)

生成摘要时出错

---

## 93. The Math Is Haunted

**原文标题**: The Math Is Haunted

**原文链接**: [https://overreacted.io/the-math-is-haunted/](https://overreacted.io/the-math-is-haunted/)

生成摘要时出错

---

## 94. Anthropic revokes OpenAI's access to Claude

**原文标题**: Anthropic revokes OpenAI's access to Claude

**原文链接**: [https://www.wired.com/story/anthropic-revokes-openais-access-to-claude/](https://www.wired.com/story/anthropic-revokes-openais-access-to-claude/)

生成摘要时出错

---

## 95. VSCode extension for syntax highlighting multi-line YAML strings

**原文标题**: VSCode extension for syntax highlighting multi-line YAML strings

**原文链接**: [https://github.com/harrydowning/vscode-yaml-embedded-languages](https://github.com/harrydowning/vscode-yaml-embedded-languages)

生成摘要时出错

---

## 96. Ergonomic keyboarding with the Svalboard: a half-year retrospective

**原文标题**: Ergonomic keyboarding with the Svalboard: a half-year retrospective

**原文链接**: [https://twey.io/hci/svalboard/](https://twey.io/hci/svalboard/)

生成摘要时出错

---

## 97. Make Your Own Backup System – Part 2: Forging the FreeBSD Backup Stronghold

**原文标题**: Make Your Own Backup System – Part 2: Forging the FreeBSD Backup Stronghold

**原文链接**: [https://it-notes.dragas.net/2025/07/29/make-your-own-backup-system-part-2-forging-the-freebsd-backup-stronghold/](https://it-notes.dragas.net/2025/07/29/make-your-own-backup-system-part-2-forging-the-freebsd-backup-stronghold/)

生成摘要时出错

---

## 98. How Hyper built a 1M-accurate indoor GPS

**原文标题**: How Hyper built a 1M-accurate indoor GPS

**原文链接**: [https://andrewhart.me/hyper/](https://andrewhart.me/hyper/)

生成摘要时出错

---

## 99. Running Gaming Workloads Through AMD's Zen 5

**原文标题**: Running Gaming Workloads Through AMD's Zen 5

**原文链接**: [https://chipsandcheese.com/p/running-gaming-workloads-through](https://chipsandcheese.com/p/running-gaming-workloads-through)

生成摘要时出错

---

## 100. At 17, Hannah Cairo solved a major math mystery

**原文标题**: At 17, Hannah Cairo solved a major math mystery

**原文链接**: [https://www.quantamagazine.org/at-17-hannah-cairo-solved-a-major-math-mystery-20250801/](https://www.quantamagazine.org/at-17-hannah-cairo-solved-a-major-math-mystery-20250801/)

生成摘要时出错

---

