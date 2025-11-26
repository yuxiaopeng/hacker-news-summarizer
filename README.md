# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-11-26.md)

*最后自动更新时间: 2025-11-26 17:50:27*
## 1. 旅行者1号即将抵达距离地球一光日处

**原文标题**: Voyager 1 Is About to Reach One Light-Day from Earth

**原文链接**: [https://scienceclock.com/voyager-1-is-about-to-reach-one-light-day-from-earth/](https://scienceclock.com/voyager-1-is-about-to-reach-one-light-day-from-earth/)

美国宇航局的旅行者1号，于1977年发射，正接近一个重要的里程碑：到2026年11月15日，它将距离地球一个光日（无线电信号24小时的传播时间），即161亿英里（259亿公里）。虽然一个光日仅是光年的一小部分，但这标志着深空探索的一项重大成就。

旅行者1号于2012年进入星际空间，目前是距离我们最远的人造物体。它以大约每秒11英里的速度飞行，每年与太阳的距离增加约3.5个天文单位。尽管年代久远且环境恶劣，旅行者1号仍继续传输数据，由预计能持续到2030年代的放射性同位素热电发电机供电。

与旅行者1号的通信是一个缓慢的过程。指令需要整整一天才能到达，再过一天才能得到确认，这与和月球的近乎瞬时通信，或者与火星和冥王星的相对较短的延迟形成了鲜明对比。

除了创纪录的距离外，旅行者1号的任务还具有历史意义。它的行星飞掠和著名的“暗淡蓝点”图像突显了我们太阳系的巨大规模和这艘探索宇宙飞船的卓越耐久性。

---

## 2. Cloudflare 停机本不该发生

**原文标题**: Cloudflare outage should not have happened

**原文链接**: [https://ebellani.github.io/blog/2025/cloudflare-outage-should-not-have-happened-and-they-seem-to-be-missing-the-point-on-how-to-avoid-it-in-the-future/](https://ebellani.github.io/blog/2025/cloudflare-outage-should-not-have-happened-and-they-seem-to-be-missing-the-point-on-how-to-avoid-it-in-the-future/)

爱德华多·贝拉尼批评了Cloudflare最近一次重大故障的根本原因分析报告，他认为，虽然他们对技术原因的解释（由于安全变更，数据库查询返回了意外的重复列）是准确的，但他们提出的预防措施却忽略了根本问题。

贝拉尼断言，问题主要不是物理复制或资源管理，而是应用程序逻辑和数据库模式之间的逻辑不匹配。核心问题源于应用程序和数据库之间不受控制的交互，这无法通过更多的测试或功能标志来可靠地修复。

他批评Cloudflare过度依赖ClickHouse来提高速度，而没有充分关注数据的正确性和一致性。他呼应了他之前关于GCP故障的建议，强调需要进行分析设计：无空字段、完全数据库规范化和形式验证的应用程序代码。他认为这些技术对于通过设计来防止类似故障至关重要。

虽然承认FAANG风格的公司可能不愿意完全采用形式化方法，但贝拉尼倡导在关键系统中使用它们，以确保故障变得不可能发生，而不仅仅是减少发生的可能性。他认为这种方法对于维护互联网稳定和保护云用户至关重要。这次故障突出了一个逻辑上的单点故障，尽管已经进行了物理复制。

---

## 3. OpenAI需要在2030年前筹集至少2070亿美元，以便继续亏损。

**原文标题**: OpenAI needs to raise at least $207B by 2030 so it can continue to lose money

**原文链接**: [https://ft.com/content/23e54a28-6f63-4533-ab96-3756d9c88bad](https://ft.com/content/23e54a28-6f63-4533-ab96-3756d9c88bad)

据英国《金融时报》Alphaville专栏文章报道，汇丰银行估计，OpenAI到2030年需要筹集至少2070亿美元才能维持运营，这意味着该公司预计将继续亏损运营。该文章本身需要付费阅读，需要注册或付费订阅才能访问全部内容。现有文本重点介绍了英国《金融时报》（FT）提供的各种订阅选项，包括试用期、标准数字访问和高级数字访问，每种订阅都包含不同级别的内容和功能。这些订阅选项提供对全球新闻、专家观点、FT应用程序、精选新闻通讯、视频、播客以及Lex和FT数字版等高级功能的访问权限。

---

## 4. 我不在乎你的“人工智能”有多好。

**原文标题**: I don't care how well your "AI" works

**原文链接**: [https://fokus.cool/2025/11/25/i-dont-care-how-well-your-ai-works.html](https://fokus.cool/2025/11/25/i-dont-care-how-well-your-ai-works.html)

2025年11月25日的一篇博文中，作者对人工智能，特别是大型语言模型（LLM）在日常生活，尤其是在进步黑客圈子中的普遍融合表示深切担忧。他们哀叹观察到的LLM“脑虫”效应，导致熟练的程序员过度依赖这些工具，作者将其比作一种有害的应对机制，类似于养成酗酒的习惯。

作者承认由于人工智能，像编码这样的熟练技艺正在贬值，类似于历史上对设计师、作家和其他人的影响。作者承认自己有避免使用LLM的特权，但同时指出那些选择不采用它们的人所面临的社会压力和劣势。

中心论点是，仅仅关注人工智能输出的质量忽略了根本问题：人工智能强化了现有的权力结构和控制。作者认为，工具成为我们自身的延伸，塑造着我们的思想，而允许人工智能渗透到这个过程中，就等于将控制权让给了那些拥有和控制人工智能基础设施的人。

作者认为人工智能是资本主义和法西斯主义的梦想，需要巨大的资源才能将资本转化为权力并循环，同时摧毁手工艺和熟练劳动力。他们认为，手工艺和表达对于自我控制至关重要，而人工智能正在积极地破坏它们。

该帖子最后呼吁在“转移性资本主义”下生存，敦促读者支持朋友，组织工会，通过减少社交媒体的使用来优先考虑心理健康，并创造新的事物。作者强调，蓬勃发展是最终的违抗行为。

---

## 5. 挑战生命定义的极简细胞

**原文标题**: A cell so minimal that it challenges definitions of life

**原文链接**: [https://www.quantamagazine.org/a-cell-so-minimal-that-it-challenges-definitions-of-life-20251124/](https://www.quantamagazine.org/a-cell-so-minimal-that-it-challenges-definitions-of-life-20251124/)

本文探讨了*Candidatus Sukunaarchaeum mirabile* (Sukunaarchaeum) 的发现，这是一种基因组异常微小的微生物，挑战了我们对生命最低需求的理解。Sukunaarchaeum 由中山拓郎及其团队发现，是一种寄生古菌，其基因组缺乏基础代谢所需的基因，这意味着它完全依赖宿主细胞获取营养和生长。这很不寻常，因为即使是共生细菌中基因组高度简化的生物，也保留了一些代谢能力。

研究人员通过测序与单细胞甲藻 *Citharistes regius* 相关的基因组，发现了 Sukunaarchaeum。该古菌的基因组只有 238,000 个碱基对，远小于其他古菌，分析表明它主要编码复制所需的蛋白质，缺乏代谢基因。它属于 DPANN 古菌群，该菌群以体积小和共生生活方式而闻名。

这一发现表明，细胞生命的多样性远大于之前的认识，可能很大一部分微生物生物多样性存在于寄生关系中。它也引发了关于生命定义的疑问，因为 Sukunaarchaeum 占据了自给自足细胞和病毒之间的灰色地带。虽然它并没有进化成病毒，因为它仍然拥有自己的基因表达机制，但它突破了生物体可以有多简单的界限。关于该古菌的真正宿主及其如何与之相互作用，以及其对人们知之甚少的蛋白质的依赖，仍然存在许多问题。

---

## 6. Python中的统计过程控制

**原文标题**: Statistical Process Control in Python

**原文链接**: [https://timothyfraser.com/sigma/statistical-process-control-in-python.html](https://timothyfraser.com/sigma/statistical-process-control-in-python.html)

本文提供了一份实战指南，介绍如何使用 `pandas`、`plotnine` 和 `scipy` 在 Python 中执行统计过程控制 (SPC)。它强调了 SPC 在监控和改进产品质量，以及识别何时需要干预方面的重要性。

本教程以一家日本温泉业务为例，该业务需要监控温度、pH 值和硫含量，以维持其质量标准。教程涵盖了以下关键步骤：

1.  **数据准备和描述性统计:** 导入数据，使用自定义函数计算均值和标准差。
2.  **过程概览图:** 创建过程概览图，包含单个测量值、子组均值和整体过程平均值，并用直方图可视化温度测量值的分布。
3.  **子组统计:** 计算每个子组的关键统计量 (xbar, 极差, 标准差) 和整体过程统计量。
4.  **控制图:** 生成均值和标准差控制图，以监控过程稳定性并检测失控状态。
5.  **移动极差图:** 在处理单个测量值而非子组时应用移动极差图，展示如何估计过程变异。

本教程包含一个学习检查问题，以巩固概念。结论强调了 SPC 可视化和统计在理解过程行为以及推动数据驱动的过程改进决策方面的重要性。文章为每个步骤都提供了代码片段，使其成为在 Python 中实施 SPC 的实用资源。

---

## 7. Optery (YC W22) 招聘首席信息安全官、发布经理、技术负责人（Node）、全栈工程师

**原文标题**: Optery (YC W22) Hiring CISO, Release Manager, Tech Lead (Node), Full Stack Eng

**原文链接**: [https://www.optery.com/careers/](https://www.optery.com/careers/)

Optery (YC W22) 现正招聘多个职位：首席信息安全官 (CISO)、发布经理、Node.js 技术主管和全栈工程师。公司招聘页面可能需要启用“个性化” cookies（通过左下角的 cookie 横幅）才能完整显示职位列表和内容。

---

## 8. 展示HN：我把藻类变成生物高度计，并把它放在气象气球上

**原文标题**: Show HN: I turned algae into a bio-altimeter and put it on a weather balloon

**原文链接**: [https://radi8.dev/blog/stratospore/](https://radi8.dev/blog/stratospore/)

作者 radi8.dev 在 Show HN 帖子中介绍了他们的项目，该项目旨在使用藻类创建一个“生物高度计”并将其用气象气球发射到平流层。 核心思想是利用藻类的光合作用作为海拔高度的指标，特别是紫外线辐射暴露。

该项目涉及几个关键步骤：

*   **培养藻类：** 作者培养了对紫外线敏感的 *眼虫藻*。
*   **生物高度计设计：** 他们设计了一个定制容器来容纳藻类并测量氧气水平的变化，这直接与光合作用活动以及紫外线暴露相关。 该容器配备了传感器来监测氧气、温度和压力，以及一个用于混合藻类培养物的泵。
*   **电子设备和数据记录：** 使用 ESP32 微控制器来控制传感器、泵并将数据记录到 SD 卡。 还包括一个 GPS 模块来跟踪气球的位置。
*   **气象气球发射：** 生物高度计被连接到气象气球并发射，上升到平流层。
*   **数据分析：** 在检索有效载荷后，作者分析了收集的数据，重点关注海拔高度（从压力得出）与藻类培养物中氧气水平之间的相关性。 结果表明紫外线暴露与藻类活性之间存在关系，验证了生物高度计的概念。

该项目被展示为一个实验性的概念验证，展示了在极端环境中使用生物系统作为传感器的潜力。 作者还开源了硬件和软件设计，鼓励其他人在此基础上进行构建。 该帖子包括技术细节、代码片段和数据可视化，说明了该项目的开发和结果。

---

## 9. Slashdot Effect:

Slashdot效应

**原文标题**: Slashdot Effect

**原文链接**: [https://en.wikipedia.org/wiki/Slashdot_effect](https://en.wikipedia.org/wiki/Slashdot_effect)

Slashdot效应，又称“slashdotting”或“死亡之拥”，指的是当一个小型网站被Slashdot、Reddit或Twitter等热门网站链接后，访问量激增的现象。这种涌入通常会压垮小型网站的资源，导致速度减慢或暂时无法访问。其核心原因包括带宽不足、服务器限制以及流量配额限制，这通常会影响托管在共享服务上的网站。

虽然最初与Slashdot相关，但该术语已扩展到包括来自其他平台的类似影响，从而产生了“being farked”或“Reddit效应”等术语。“突发流量”这一通用术语概括了突如其来的、压倒性的流量的本质。

这种效应可能是有害的，类似于拒绝服务攻击，但并非有意为之。虽然大型网站的设计可以处理大量的流量，但资源有限、包含大型媒体文件或动态内容生成效率低下的小型网站更容易受到影响。

虽然随着云计算的兴起和类似网站的出现，Slashdot效应的影响已经减弱，但它仍然可能发生，尤其是在被受欢迎的社交媒体用户提及时。这种现象也可能影响社区网站，带来新用户，从而导致不良行为，如钓鱼。解决方案包括镜像内容或使用可以处理增加流量的服务。

---

## 10. JOPA：用C++编写的Java编译器，Jikes现代化至Java 6，并使用Claude

**原文标题**: JOPA: Java compiler in C++, Jikes modernized to Java 6 with Claude

**原文链接**: [https://github.com/7mind/jopa](https://github.com/7mind/jopa)

JOPA (Java 对象程序汇编器) 是对 Jikes 的现代化改造，Jikes 是一个历史悠久的、用 C++ 编写的独立 Java 编译器。该项目旨在使 Jikes 与 Java 5 和 Java 6 的特性保持同步，使其有可能用于引导 Java 开发。

更新后的 JOPA 支持关键的 Java 5 特性，例如泛型、增强型 for 循环、可变参数、枚举、自动装箱/拆箱、静态导入和注解。它还包括 Java 6 特性，如类文件版本 50.0 和增强的调试信息。

构建 JOPA 需要 CMake 3.20+ 和 C++17 编译器，以及用于编码支持的 iconv/ICU。 该项目提供了使用 Nix 构建和通用 CMake 方法的说明，详细说明了用于调试、浮点仿真、编码和 JVM 测试的有用 CMake 选项。

最初的 Jikes 编译器以其速度、错误纠正能力和高质量的错误消息而闻名，通常优于标准的 `javac` 编译器。由于泛型的引入，Jikes 的开发于 2005 年停止，使其不再那么重要。这个 JOPA 项目旨在通过添加对这些特性的支持来复兴 Jikes，使其再次可用。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 2 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 3 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 4 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 5 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 6 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 7 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 8 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 9 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 10 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 11 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 12 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 13 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 14 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 15 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 16 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 17 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 18 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 19 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 20 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 21 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 22 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 23 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 24 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 25 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 26 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 27 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 28 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 29 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 30 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 31 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 32 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 33 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 34 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 35 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 36 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 37 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 38 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 39 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 40 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 41 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 42 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 43 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 44 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 45 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 46 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 47 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 48 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 49 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 50 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 51 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 52 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 53 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 54 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 55 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 56 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 57 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 58 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 59 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 60 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 61 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 62 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 63 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 64 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 65 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 66 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 67 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 68 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 69 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 70 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 71 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 72 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 73 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 74 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 75 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 76 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 77 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 78 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 79 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 80 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 81 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 82 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 83 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 84 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 85 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 86 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 87 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 88 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 89 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 90 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 91 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 92 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 93 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 94 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 95 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 96 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 97 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 98 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 99 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 100 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 101 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 102 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 103 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 104 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 105 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 106 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 107 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 108 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 109 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 110 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 111 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 112 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 113 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 114 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 115 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 116 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 117 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 118 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 119 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 120 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 121 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 122 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 123 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 124 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 125 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 126 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 127 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 128 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 129 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 130 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 131 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 132 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 133 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 134 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 135 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 136 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 137 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 138 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 139 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 140 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 141 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 142 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 143 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 144 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 145 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 146 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 147 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 148 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 149 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 150 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 151 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 152 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 153 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 154 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 155 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 156 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 157 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 158 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 159 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 160 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 161 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 162 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 163 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 164 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 165 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 166 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 167 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 168 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 169 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 170 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 171 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 172 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 173 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 174 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 175 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 176 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 177 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 178 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 179 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 180 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 181 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 182 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 183 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 184 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 185 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 186 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 187 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 188 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 189 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 190 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 191 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 192 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 193 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 194 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 195 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 196 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 197 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 198 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 199 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 200 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 201 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 202 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 203 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 204 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 205 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 206 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 207 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 208 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 209 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 210 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 211 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 212 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 213 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 214 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 215 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 216 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 217 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 218 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 219 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 220 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 221 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 222 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 223 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 224 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 225 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 226 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 227 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 228 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 229 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 230 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 231 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 232 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 233 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 234 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 235 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 236 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 237 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 238 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 239 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 240 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 241 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 242 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 243 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 244 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 245 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 246 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 247 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 248 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 249 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 250 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 251 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
