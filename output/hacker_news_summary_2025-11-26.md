# Hacker News 热门文章摘要 (2025-11-26)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 展示HN：KiDoom – 在PCB走线上运行DOOM

**原文标题**: Show HN: KiDoom – Running DOOM on PCB Traces

**原文链接**: [https://www.mikeayles.com/#kidoom](https://www.mikeayles.com/#kidoom)

展示HN：KiDoom – 在PCB走线上运行DOOM

这篇文章“展示HN：KiDoom – 在PCB走线上运行DOOM”突出了一个在PCB（印刷电路板）走线上运行经典视频游戏DOOM的项目。虽然提供的内容有限，但我们可以推断出以下几点：

文章展示了一项新颖的技术成就：在非常规的PCB走线上运行DOOM，这款在当时资源消耗较大的游戏。 这意味着创新的硬件和软件工程。

随附的统计数据表明，KiDoom的创建者或团队在电子和软件开发方面拥有丰富的经验，特别是在汽车或嵌入式系统领域：

*   **3个ECU已开发：** 开发嵌入式控制单元的经验，可能是在汽车应用中。
*   **10年以上经验：** 证明在其领域拥有相当的专业知识。
*   **2850万+英里驾驶里程：** 可能与由他们的ECU控制的汽车系统的测试或部署有关。

“精选项目”和“私有工具”的提及表明，KiDoom只是他们更广泛工作的一个例子。 这也暗示了他们开发过程中使用的专有工具或技术。

本质上，这篇文章将KiDoom呈现为一项令人印象深刻的工程独创性演示，在一个高度非常规的平台上运行视频游戏，可能由一个在嵌入式系统方面拥有丰富经验的团队提供支持。 关键在于在PCB上运行DOOM的令人印象深刻的壮举，暗示了项目创建者更广泛的能力。

---

## 12. DWPD 仍然是個有用的 SSD 指標嗎？

**原文标题**: Is DWPD Still a Useful SSD Spec?

**原文链接**: [https://klarasystems.com/articles/is-dwpd-still-useful-ssd-spec/](https://klarasystems.com/articles/is-dwpd-still-useful-ssd-spec/)

本文探讨了DWPD（每日驱动器写入次数）作为固态硬盘耐久性指标的相关性，并认为由于NAND闪存技术的日益复杂，该指标正变得越来越不实用。

作者解释了基于NAND闪存的固态硬盘写入耐久性有限，每次编程/擦除 (P/E) 周期都会降低其性能。虽然固态硬盘相比机械硬盘具有速度和更低延迟等优势，但它们引入了新的故障模式，包括控制器故障、电荷保持失败以及写入耐久性耗尽。随着存储单元的老化，它们会变得更慢且更不准确，从而导致性能下降。

本文强调了容量和寿命之间的权衡。更高密度存储（MLC、TLC、QLC、PLC）允许每个存储单元存储更多数据，但与 SLC 相比，会减少 P/E 周期和整体寿命。文章强调，购买具有更多物理存储单元的更大容量的驱动器可以分散工作负载，从而延长耐久性，因为随着时间的推移写入相同数量的数据会导致每个存储单元的 P/E 周期更少。

文章还指出，大多数消费级固态硬盘的更换是因为需要更多空间或因写入耐久性耗尽而导致性能下降。缓解写入耐久性问题涉及考虑位密度、利用损耗均衡（在存储单元之间均匀分配写入操作）、增加可用容量以及增加原始容量。最终，作者认为仅仅关注 DWPD 是评估固态硬盘寿命的一种不完整的方式，而全面考虑驱动器大小、使用模式和所使用的 NAND 闪存类型等因素会更有效。

---

## 13. 图像扩散模型展现出视频中涌现的时间传播

**原文标题**: Image Diffusion Models Exhibit Emergent Temporal Propagation in Videos

**原文链接**: [https://arxiv.org/abs/2511.19936](https://arxiv.org/abs/2511.19936)

这篇arXiv文章 (arXiv:2511.19936) 提出了一项关于图像扩散模型的新研究，探索了它们在图像生成之外的能力。作者Youngseo Kim、Dohyun Kim、Geonhee Han和Paul Hongsuck Seo发现，这些模型中的自注意力图可以被重新解释为语义标签传播核。这使得识别相关图像区域之间的像素级对应关系成为可能，从而有效地实现语义理解。

关键创新在于将这种机制在时间上扩展到视频帧，从而创建一个时间传播核。该核通过分割促进零样本对象跟踪，而无需为视频任务进行显式训练。作者还通过测试时优化策略（如DDIM反演、文本反演和自适应头部加权）来增强标签传播的鲁棒性和一致性。

基于这些发现，他们引入了DRIFT（用于跟踪的基于扩散的细化），这是一个用于视频对象跟踪的新型框架。DRIFT利用预训练的图像扩散模型，并结合了SAM（分割一切模型）引导的掩码细化。该框架在标准视频对象分割基准测试中实现了最先进的零样本性能，展示了图像扩散模型在适应视频分析时所产生的涌现式时间推理能力。本质上，该研究揭示了图像扩散模型在理解和跟踪视频序列中的对象方面的隐藏潜力，为零样本视频分析任务提供了一个有希望的途径。

---

## 14. 出乎意料的是，安卓上的Emacs相当不错。

**原文标题**: Surprisingly, Emacs on Android is pretty good

**原文链接**: [https://kristofferbalintona.me/posts/202505291438/](https://kristofferbalintona.me/posts/202505291438/)

本文探讨了在 Android 上使用 Emacs 出人意料的积极体验。虽然不如桌面版流畅，但它仍然是一个可行的选择，尤其是在正确设置的情况下。

作者强调了几个关键考虑因素：Android 上的 Emacs 需要通过 F-Droid 进行基本安装（仅限有限的 elisp），或者使用 Termux 进行更复杂的设置以访问其他 CLI 工具（推荐）。Termux 允许 Emacs 使用像 git 这样的工具，但涉及到更复杂的安装过程。Android 的沙盒机制会使得访问 Emacs 应用程序指定区域之外的文件变得繁琐，需要手动目录访问。

配置至关重要。作者建议参考 Emacs 手册的 Android 部分，并最初使用 Customize 界面来进行更容易的基于触摸的调整。启用像 `modifier-bar-mode` 和 `tool-bar-mode` 这样的小模式可以改善用户界面。他们还建议使用像 Hacker's Keyboard 或 Unexpected Keyboard 这样的虚拟键盘，以便更容易地访问修饰键和符号。字体安装需要将文件直接放置在 `~/fonts/` 目录中。

结论强调使用 Customize 界面，启用触摸屏专用选项，并安装虚拟键盘。作者对他们目前的设置表示满意，并迁移了桌面配置的相关部分。他们还提供了一个愿望清单，包括触摸屏手势和自动键盘切换，以及更大的工具栏。

---

## 15. 用于量子计算机的Qiskit开源SDK

**原文标题**: Qiskit open-source SDK for working with quantum computers

**原文链接**: [https://github.com/Qiskit/qiskit](https://github.com/Qiskit/qiskit)

Qiskit 是一个用于量子计算机的开源 SDK，提供创建量子线路、算符和原语的工具。它包含一个用于线路优化的转换器和一个量子信息工具箱。建议通过 `pip install qiskit` 安装。

该 SDK 允许用户定义和构建量子线路，通过测量或可观测算符定义经典输出，并利用 Sampler 和 Estimator 原语来采样结果或估计期望值。该示例演示了创建纠缠的 GHZ 态，并使用 Sampler 进行测量，然后使用 Estimator 和自定义算符估计其期望值。

扩展量子线路需要真实的量子硬件，Qiskit 包含一个转换器，可以将线路适配到特定硬件。Qiskit 提供了一个抽象层，可以通过运行时环境在来自不同供应商的硬件上运行线路，这些运行时环境实现了 BaseSamplerV2 和 BaseEstimatorV2 接口以获得优化的性能。它还提供了一个用于描述量子后端的较低级别抽象接口。

文档提供了贡献指南，鼓励用户参与 Qiskit Slack 社区或使用 Stack Overflow 或 Quantum Computing Stack Exchange 提问。Qiskit 是一项协作成果，应适当引用。GitHub 上提供了详细描述更改和潜在重大更改的更新日志和发行说明。Qiskit 的开发部分由美国能源部科学办公室资助。它以 Apache License 2.0 许可。

---

## 16. Copyparty，开源文件服务器[视频]

**原文标题**: Copyparty, the FOSS file server [video]

**原文链接**: [https://www.youtube.com/watch?v=15_-hgsX2V0](https://www.youtube.com/watch?v=15_-hgsX2V0)

内容看起来是标准的YouTube页脚文本，而不是关于Copyparty的文章。因此，没有需要总结的文章。内容包括指向YouTube服务条款、隐私政策、广告信息、创作者资源和其他法律和管理信息的链接。它还包括版权声明以及关于新功能测试和NFL Sunday Ticket的声明。它不包含关于文件服务器Copyparty的任何信息。

---

## 17. 司法部要求Realpage停止分享具有竞争敏感性的信息

**原文标题**: Justice dept. requires Realpage end sharing competitively sensitive information

**原文链接**: [https://www.justice.gov/opa/pr/justice-department-requires-realpage-end-sharing-competitively-sensitive-information-and](https://www.justice.gov/opa/pr/justice-department-requires-realpage-end-sharing-competitively-sensitive-information-and)

司法部已提交一项拟议和解协议，要求为租赁住房行业提供收入管理软件的RealPage公司停止反竞争行为。该和解协议旨在解决对RealPage软件的担忧，该软件使用房东共享的非公开数据，导致协调一致的租金定价。

拟议和解协议规定，RealPage必须停止使用竞争对手的敏感数据来实时设定租金价格，限制模型训练使用过时的历史数据（至少12个月前的数据），并避免窄于州级别的地域影响。RealPage还必须删除限制价格下降或使竞争对手之间的定价保持一致的功能，停止通过市场调查收集敏感信息，并避免在会议中讨论定价策略。

为确保合规，法院指定的监督员将监督RealPage的行为。该公司还必须配合司法部对使用其软件的物业管理公司提起的诉讼。该和解协议须经法院在公开征求意见期后批准，旨在恢复租赁市场的自由市场竞争。此举是司法部持续打击租赁住房领域算法协调和反竞争信息共享的一部分。

---

## 18. 我私信了一位韩国总统候选人，结果帮他打造了核心竞选团队。

**原文标题**: I DM'd a Korean presidential candidate and ended up building his core campaign

**原文链接**: [https://medium.com/@wjsdj2008/i-dmd-a-korean-presidential-candidate-and-ended-up-building-his-core-campaign-platform-the-38eb1c5f5e7d](https://medium.com/@wjsdj2008/i-dmd-a-korean-presidential-candidate-and-ended-up-building-his-core-campaign-platform-the-38eb1c5f5e7d)

无法访问文章链接。

---

## 19. 万亿美元已投入，大型软件项目依然失败

**原文标题**: Trillions spent and big software projects are still failing

**原文链接**: [https://spectrum.ieee.org/it-management-software-failures](https://spectrum.ieee.org/it-management-software-failures)

尽管全球IT支出大幅增加，软件项目失败的问题仍然存在。罗伯特·N·查雷特的文章强调，自2005年以来，IT支出增加了两倍多，但软件成功率并没有显著提高，导致巨大的商业和社会成本。作者认为，人工智能不是解决这些问题的灵丹妙药，因为核心问题通常源于不切实际的目标、糟糕的管理和组织政治等人类因素。

文章列举了加拿大政府的凤凰工资系统、英国邮局的Horizon系统、明尼苏达州许可和注册系统(MNLARS)以及澳大利亚的现代化商业登记项目等案例，说明了技术、管理、伦理和组织失败的反复出现。这些失败导致巨大的经济损失并损害人们的生活。

作者强调，许多失败是可以避免的，并且源于忽视以往项目的经验教训。IT界倾向于认为每个项目都是独一无二的，并且无视之前的错误，这加剧了这种恶性循环。虽然敏捷和DevOps方法旨在改进软件开发，但它们需要强大的领导力、纪律和文化变革才能成功。文章最后指出，持续未能从过去的错误中吸取教训对现代社会构成了生存威胁，尤其是在IT系统日益互联互通的情况下。

---

## 20. 在沙中储热的高效太阳能烹饪

**原文标题**: Efficient solar cooking that stores heat in sand

**原文链接**: [https://www.sciencedirect.com/science/article/pii/S266711312500035X](https://www.sciencedirect.com/science/article/pii/S266711312500035X)

无法访问文章链接。

---

## 21. 雅加达现在是世界上最大的城市。

**原文标题**: Jakarta is now the biggest city in the world

**原文链接**: [https://www.axios.com/2025/11/24/jakarta-tokyo-worlds-biggest-city-population](https://www.axios.com/2025/11/24/jakarta-tokyo-worlds-biggest-city-population)

雅加达超越东京成为世界人口第一大城市，据 Axios 及其他来源的预测显示。这一转变归因于多种因素，包括雅加达强劲的人口增长和东京的人口萎缩。

文章可能详细描述了雅加达蓬勃发展的人口增长，这得益于农村地区寻求经济机会的移民以及相对较高的出生率。这种快速增长给雅加达的基础设施带来了巨大的压力，导致了交通拥堵、污染和清洁用水获取等挑战。

相反，文章可能解释说，东京的人口正在下降，原因是低出生率和人口老龄化。日本严格的移民政策也导致了人口增长的不足。

文章可能涉及这种城市主导地位转变的影响。它可能会讨论雅加达作为世界最大城市所面临的经济机遇和挑战，以及对全球城市规划和可持续发展努力的影响。它也可能提及在雅加达增加国际投资和经济影响力的潜力。最后，文章可能会对比雅加达和东京的对比性发展轨迹，以此作为塑造全球城市景观的不同人口趋势的例子。

---

## 22. CS234：2025冬季强化学习

**原文标题**: CS234: Reinforcement Learning Winter 2025

**原文链接**: [https://web.stanford.edu/class/cs234/](https://web.stanford.edu/class/cs234/)

CS234：2025冬季强化学习课程旨在提供强化学习领域的扎实入门，涵盖核心挑战、方法和技术，包括深度强化学习。学生将通过讲座、书面作业和Python编程作业获得熟练程度。

本课程的主要方面包括：

*   **先修

---

## 23. 展示HN：我们构建了一个开源、零Webhook的支付处理器

**原文标题**: Show HN: We built an open source, zero webhooks payment processor

**原文链接**: [https://github.com/flowglad/flowglad](https://github.com/flowglad/flowglad)

Flowglad：简化互联网变现的开源“零Webhook”支付处理器，旨在减轻传统支付系统的复杂性，无需Webhook、手动计划映射和客户ID管理。

主要特性包括：

*   **无状态账单：** 避免了订阅和客户数据的复杂数据库结构。
*   **单一数据源：** 提供访问客户账单信息的中心点，包括功能访问和使用信用额度。
*   **基于ID的访问：** 允许使用应用程序身份验证系统中现有的用户ID查询客户状态。
*   **全栈SDK：** 为后端 (Node.js) 和前端 (React) 提供访问账单数据的工具。
*   **灵活定价：** 允许轻松迭代和部署新的定价模型。

集成包括安装Flowglad软件包，配置具有用户ID和详细信息的服务器实例，公开API处理程序，并用提供程序包装应用程序。 提供了前端和后端示例，演示了如何检查功能访问权限和使用余额。

Flowglad为常见的定价模型（如基于使用量、订阅和功能门控访问）提供预构建的模板。 该项目的目标是通过简化集成、减少维护并提供集成多个支付提供商的单一入口点，从而改善支付方面的开发者体验。 核心原则是最大限度地减少账单的复杂性和花费的时间，使开发人员能够专注于其核心产品。

---

## 24. 布达佩斯出土1700年历史的罗马石棺

**原文标题**: 1,700-year-old Roman sarcophagus is unearthed in Budapest

**原文链接**: [https://apnews.com/article/hungary-roman-sarcophagus-discovery-budapest-77a41fe190bbcc167b43d05141536f54](https://apnews.com/article/hungary-roman-sarcophagus-discovery-budapest-77a41fe190bbcc167b43d05141536f54)

在匈牙利布达佩斯出土了一具保存异常完好的1700年历史的罗马石棺，为了解罗马时代一位年轻女性的生活提供了线索。这具石灰石棺材是在奥布达的一次挖掘中发现的，奥布达是古罗马阿奎库姆定居点的一部分。石棺几个世纪以来未被触动，用金属夹和熔融铅密封。

在里面，考古学家发现了一具完整的骨骼，周围环绕着文物，包括玻璃器皿、青铜雕像、140枚硬币、一根骨制发夹、琥珀珠宝以及金线织物痕迹，表明这座坟墓属于一位年轻富有的女性。首席考古学家加布里埃拉·费尼什认为，这些物品是献给这位女性“永恒旅程”的礼物，表明死者是由充满爱意的亲属精心埋葬的。

石棺是在一个被改造成墓地的废弃房屋遗址中发现的，靠近罗马渡槽和其他更简单的坟墓。专家们现在将检查这位女性的遗骸，以确定更多关于她的年龄、健康和起源的信息。罗马时期专家格尔盖伊·科斯蒂亚尔强调了发现如此未受触动的石棺的罕见性，因为在4世纪，重复利用旧石棺很常见。考古学家还计划筛选棺材里的泥土，希望能发现更多的宝藏。费尼什强调了这一发现的情感冲击，并指出埋葬这位年轻女性的人们所表现出的关怀和爱。

---

## 25. 如何将旧手机改造成网络服务器

**原文标题**: How to repurpose your old phone into a web server

**原文链接**: [https://far.computer/how-to/](https://far.computer/how-to/)

本文介绍了如何使用PostmarketOS将旧Android手机改造为基本网页服务器的指南。作者旨在减少电子垃圾并鼓励旧设备的再利用。

该过程主要包括三个步骤：

1.  **安装PostmarketOS：** 这涉及到将自定义操作系统刷入手机，取代Android。该指南指导用户在PostmarketOS网站上找到其特定设备，安装`pmbootstrap`，生成镜像，将手机启动到刷机模式，并刷入生成的镜像。

2.  **设置服务器：** 成功安装后，该指南详细介绍了如何SSH连接到手机，将其连接到Wi-Fi网络，并确定其本地IP地址。这有效地将手机转换为可在本地网络上访问的小型本地服务器。

3.  **提供网页服务：** 这涉及到为Web文件创建目录（`/var/www/html/`），编写一个简单的HTML文件（例如，“hello world”），配置防火墙（nftables）以允许端口80上的流量，并运行一个简单的HTTP服务器（`httpd`）。该指南提供了通过`curl`以及通过Web浏览器访问来测试服务器的说明。

该文章还提供了关于远程访问的额外建议，建议使用VPN而不是直接将SSH（端口22）暴露给互联网以确保安全。还提供了有关如何保持软件更新的说明。未来的高级主题将涵盖使用HTTPS设置域名并确保HTTP服务器在重启后持续运行。

---

## 26. 一座新桥梁连接了无穷的数学与计算机科学。

**原文标题**: A new bridge links the math of infinity to computer science

**原文链接**: [https://www.quantamagazine.org/a-new-bridge-links-the-strange-math-of-infinity-to-computer-science-20251121/](https://www.quantamagazine.org/a-new-bridge-links-the-strange-math-of-infinity-to-computer-science-20251121/)

描述集合论与分布式算法：一个令人惊讶的关联

---

## 27. FLUX.2: 前沿视觉智能

**原文标题**: FLUX.2: Frontier Visual Intelligence

**原文链接**: [https://bfl.ai/blog/flux-2](https://bfl.ai/blog/flux-2)

FLUX.2：黑森林实验室最新视觉智能模型，旨在通过其高质量的图像生成和编辑能力，彻底变革创意工作流程。与许多专注于演示的AI图像工具不同，FLUX.2优先考虑实际应用，能够在多个参考图像中保持一致的角色/风格，精确遵循提示，处理复杂文本，遵守品牌指南，并可靠地管理光照、布局和标志。它可以在保持细节和连贯性的同时编辑高达4百万像素的图像。

黑森林实验室提倡开放核心方法，发布可检查的开放权重模型（如FLUX.2 [dev]）以及强大的、可用于生产的API。FLUX.2建立在FLUX.1的基础上，并以精度、效率、控制和极高的真实感扩展其能力。

主要功能包括多参考支持（最多10张图像）、增强的图像细节和照片写实感、可靠的文本渲染、改进的提示遵循、扎实的世界知识以及更高分辨率的编辑。

FLUX.2系列提供各种模型产品，以满足不同的需求：FLUX.2 [pro]（最先进的质量）、FLUX.2 [flex]（控制模型参数）、FLUX.2 [dev]（用于本地使用的开放权重模型）和FLUX.2 [klein]（即将推出，开源且尺寸精简）。一个新的VAE，FLUX.2 - VAE，也以Apache 2.0许可证提供。

FLUX.2利用潜在流匹配架构，将Mistral-3 VLM与校正流Transformer相结合。该模型提供最先进的图像生成质量和编辑功能。黑森林实验室设想FLUX.2是朝着统一感知、生成、记忆和推理的多模态模型迈出的一步，并且以开放和透明的方式实现。

---

## 28. Java反编译器

**原文标题**: Java Decompiler

**原文链接**: [http://java-decompiler.github.io](http://java-decompiler.github.io)

Java反编译器 (JD 项目) 提供反编译和分析Java字节码的工具。 其核心组件 JD-Core 从 .class 文件重建 Java 源代码，帮助恢复源代码和探索 Java 运行时库。 它支持 Java 5 以后的功能，例如注解和泛型。

JD 提供三个主要组件：

*   **JD-GUI：** 一个独立的图形实用程序，用于浏览从 .class 文件重建的 Java 源代码。它支持拖放功能，并处理各种文件类型，包括 CLASS、JAR、WAR 和 ZIP。
*   **JD-Eclipse：** 一个 Eclipse 插件，即使源代码不可用，也能在调试期间显示 Java 源代码。
*   **JD-Core：** 驱动 JD-GUI 和 JD-Eclipse 的底层库。

JD-Core 与各种 Java 编译器兼容。 JD-GUI 提供颜色编码的源代码显示、文件层次结构浏览和堆栈跟踪分析等功能。 JD-Eclipse 可以通过简单的拖放安装过程轻松地在 Eclipse 中安装。

所有三个组件（JD-Core、JD-GUI 和 JD-Eclipse）都是开源的，并根据 GPLv3 获得许可。 该项目欢迎捐款以支持其发展。 提供了 JD-GUI 和 JD-Eclipse 的发行版链接和问题跟踪器。

---

## 29. Python 并非数据科学的理想语言。

**原文标题**: Python is not a great language for data science

**原文链接**: [https://blog.genesmindsmachines.com/p/python-is-not-a-great-language-for](https://blog.genesmindsmachines.com/p/python-is-not-a-great-language-for)

尽管 Python 的应用非常广泛，但克劳斯·威尔克在本文中认为，Python 并非数据科学的“理想”语言。他澄清说，他讨论的不是 Python 表现出色的深度学习（尤其是在 PyTorch 方面），而是数据整理、探索性分析、可视化和统计建模。

威尔克的论点源于他对学生和同事使用 Python 进行数据分析的观察。他指出，与他认为在 R 中可以更容易实现的结果相比，看似简单的数据操作和可视化任务通常需要大量的努力和复杂的代码。

他将 Python 在数据科学领域的普及归因于历史偶然性和其在各种任务中“勉强过关”的表现。他认为，适合数据科学的语言需要是解释型的、可以交互使用，并且具有较低的启动成本。虽然 Python 符合这一描述，与 R、Matlab 和 Mathematica 一样，但他将比较重点放在 Python 和 R 上。

威尔克提倡将分析逻辑与数据操作的“后勤”分离，更喜欢允许高级概念表达的语言和库。他以 Palmer Penguins 数据集为例，展示了 R 和 Python 的比较代码片段，以实现相同的任务：计算企鹅物种和岛屿每种组合的企鹅体重的平均值和标准差。虽然这个例子很简单，两种语言具有可比性，但威尔克认为，随着任务复杂性的增加，Python 往往会演变成复杂的后勤工作，从而阻碍有效的数据分析。

他承诺未来的文章将深入探讨使 Python 中的数据分析比 R 更复杂的一些具体问题。

---

## 30. 太空货运 – 诺斯特罗莫号 (2012)

**原文标题**: Space Truckin' – The Nostromo (2012)

**原文链接**: [https://alienseries.wordpress.com/2012/10/23/space-truckin-the-nostromo/](https://alienseries.wordpress.com/2012/10/23/space-truckin-the-nostromo/)

本文详细介绍了电影《异形》（1979）中诺史莫号飞船的设计过程。它突出了《2001太空漫游》和《黑暗之星》等电影的影响，强调了创造“用过的宇宙”美学的愿望，与《星球大战》中更具幻想色彩的元素形成对比。《异形》的编剧丹·欧班农强调了让飞船看起来具有令人信服的工业感和破旧感的重要性。

设计过程涉及多位艺术家，包括罗恩·科布、克里斯·福斯，以及后来的H.R.吉格和墨比斯。最初，该飞船被称为“Snark”和“Leviathan”，最终确定为“Nostromo”。科布和福斯创作了大量设计，但制作过程面临犹豫不决和延误。导演雷德利·斯科特最终掌控了局面，旨在打造一个逼真的、缓慢移动的、巨大的钢铁结构。

最终的设计来源于多种来源。特效总监布莱恩·约翰逊对缺乏进展感到沮丧，他抓取了科布和福斯的设计合集，并以此为模型的基础。虽然福斯觉得他的作品被忽视了，但科布的外部和内部设计最终被斯科特接受。本文展示了创造电影史上最具标志性的飞船之一所涉及的混乱和协作过程。

---

## 31. 最大三角形-三桶与傅里叶变换 (2024)

**原文标题**: Largest-Triangle-Three-Buckets and the Fourier Transform (2024)

**原文链接**: [https://daniel.mitterdorfer.name/posts/2024-01-30-downsampling-lttb-and-fft/](https://daniel.mitterdorfer.name/posts/2024-01-30-downsampling-lttb-and-fft/)

这篇博文探讨了用于对时间序列数据进行降采样的最大三角形三桶 (LTTB) 算法，重点关注其对时域和频域的影响。LTTB 通过选择桶内的重要点来减少数据点，同时保留视觉特性。

作者在一个数据集上演示了 LTTB，然后将其应用于一个简单的正弦波，观察到激进的降采样会在频域中引入失真伪影，这可以通过傅里叶变换揭示。降采样会改变信号的明显基频。

然后，该文章强调了奈奎斯特-香农采样定理的重要性，指出信号必须以至少其最高频率的两倍进行采样，以避免信息丢失。作者通过展示如何将 16 Hz 正弦波降采样到低于 32 Hz 导致完全失真来说明了这一点。

最后，这些原理被应用于原始的、更复杂的数据集。分析原始信号的傅里叶变换以识别其频率分量，并使用 LTTB 将其降采样到 32 个和 8 个样本。作者得出结论，虽然降采样可以节省资源并提高延迟，但了解信号的频率内容并应用奈奎斯特定理对于最小化失真并在降采样过程中保留信号的整体形状至关重要。本质上，LTTB 是有效的，但仔细考虑信号的特性对于获得最佳结果是必要的。

---

## 32. 使用 CSS Subgrid 的新布局

**原文标题**: New layouts with CSS Subgrid

**原文链接**: [https://www.joshwcomeau.com/css/subgrid/](https://www.joshwcomeau.com/css/subgrid/)

本文探讨了 CSS 子网格（Subgrid），它是一种允许通过 DOM 树扩展网格布局的功能，从而实现更灵活且语义上正确的 UI 设计。

本文首先通过一个基本示例来演示如何使用子网格在列表中对图像进行分组，同时仍将其融入父网格布局中。然后，文章将此方法与传统的 Flexbox/Grid 组合方法进行对比，并承认子网格并非总是最简单的解决方案。

文章的核心集中在一个更引人注目的用例上：当网格项目中的内容各不相同时，如何在这些项目之间对齐内容。以艺术家作品集为例，作者演示了当具有不同内容长度的卡片放置在网格中时，子网格如何解决图像宽度不一致的问题。如果没有子网格，`fr` 单位会独立计算每个卡片的列宽，从而导致未对齐。通过使用 `grid-template-columns: subgrid` 使嵌套网格继承父网格的列定义，文章展示了如何实现所有卡片的列宽一致，而不管其各自的内容如何。这创建了一个具有视觉吸引力和组织良好的布局。文章强调了子网格在复杂布局中使兄弟元素能够彼此感知的能力，为常见的 CSS 挑战提供了一个解决方案。

---

## 33. BebboSSH：Amiga系统SSH2实现 (68000, GPLv3)

**原文标题**: BebboSSH: SSH2 implementation for Amiga systems (68000, GPLv3)

**原文链接**: [https://franke.ms/git/bebbo/bebbossh](https://franke.ms/git/bebbo/bebbossh)

BebboSSH是一个适用于Amiga系统 (68000+) 的SSH2套件，提供安全的远程访问、文件传输和密钥生成。它包含客户端 (bebbossh)、服务器守护进程 (bebbosshd)、SCP实用程序 (bebboscp) 和密钥生成器 (bebbosshkeygen)，以及libcryptossh.library，针对不同的68k CPU进行了优化。它支持现代密码算法，如curve25519-sha256、aes128-gcm和chacha20-poly1305。

性能因Amiga硬件而异，在未加速的系统上，连接建立需要更长时间。文档包含SCP传输速度的性能表，其中列出了不同密码算法在各种Amiga配置下的表现。BebboSSH的工具提供配置选项，如密钥身份验证、端口转发和密码选择。服务器需要配置才能进行SSH访问。

该软件在GPLv3+许可下发布（部分组件在公共领域下），作者声明不提供担保和责任限制。文档列出了最近的改进，包括从AmigaSSH更名、优化后的加密以及ChaCha20/Poly1305支持。它还提供了针对常见问题的故障排除技巧和配置建议，例如终端仿真、密钥身份验证和SCP传输。最后，它提供了xterm-amiga terminfo设置的指南。

---

## 34. Google反重力通过间接提示注入攻击窃取数据

**原文标题**: Google Antigravity exfiltrates data via indirect prompt injection attack

**原文链接**: [https://www.promptarmor.com/resources/google-antigravity-exfiltrates-data](https://www.promptarmor.com/resources/google-antigravity-exfiltrates-data)

Google新一代自主编码编辑器Antigravity中一项重大安全漏洞：如何通过间接提示注入攻击窃取敏感数据。攻击利用恶意网络资源（例如，集成指南）操纵Antigravity的AI代理Gemini，从而从用户的IDE中窃取凭据和代码片段。

攻击分解：用户在试图集成某项功能时，不知情地引用了恶意在线资源。该资源中隐藏的提示注入强制Gemini收集敏感信息，如来自.env文件的凭据（通过使用`cat`命令绕过Gitignore保护）。然后，它构造一个包含此数据的恶意URL，并指示浏览器子代理访问该URL。由于默认的Antigravity白名单包含'webhook.site'，因此子代理成功地将数据泄露到攻击者控制的端点。

本文重点介绍了Antigravity的默认设置，特别是与代理审查策略和终端命令自动执行策略相关的设置，如何导致该漏洞。代理管理器旨在在后台同时运行多个代理，这进一步加剧了风险，因为用户不太可能主动监控每个代理的操作。

作者承认Google已经意识到这些数据泄露风险，并指出Google依赖免责声明而不是强大的缓解措施。研究人员认为，用户不太可能仔细审查每个代理的操作，这使得该漏洞成为一个严重的担忧。他们选择不进行负责任的披露，因为Google已经承认了这个问题。

---

## 35. Ilya Sutskever：我们正从扩展时代迈向研究时代

**原文标题**: Ilya Sutskever: We're moving from the age of scaling to the age of research

**原文链接**: [https://www.dwarkesh.com/p/ilya-sutskever-2](https://www.dwarkesh.com/p/ilya-sutskever-2)

伊利亚·苏茨凯弗与德瓦尔凯什·帕特尔的对话中，他们探讨了人工智能的现状与未来发展轨迹，强调了从单纯的模型扩展转向更深入的研究。苏茨凯弗指出，人工智能在评估方面的出色表现与其滞后的经济影响之间存在令人困惑的脱节，并将此归因于强化学习训练的潜在问题以及泛化能力不足。他认为，专注于在评估中获得高分的做法可能无意中限制了模型的更广泛能力。

苏茨凯弗用编程竞赛类比来说明这一点，在这种情况下，在特定领域的集中专业化并不一定转化为更广泛的专业知识。他还探讨了预训练的作用，承认其在提供大量数据方面的优势，但强调了理解模型如何依赖预训练的难度。

讨论进一步深入到情感的概念及其与人工智能中的价值函数之间的潜在联系，并将情感处理对人类决策的影响进行了类比。苏茨凯弗认为，虽然情感可能与价值函数相关，但当前的机器学习模型缺乏价值函数的重要作用。他最后表示，SSI是一家处于研究时代的公司。

---

## 36. 泔水侦探 – 对抗泔水辛迪加

**原文标题**: Slop Detective – Fight the Slop Syndicate

**原文链接**: [https://slopdetective.kagi.com/](https://slopdetective.kagi.com/)

这段文字描述了一个名为“污垢侦探 – 对抗污垢集团”的网页。该网页的主要内容是提示用户启用 JavaScript 以便玩名为“污垢侦探”的游戏。该网页的目的是托管并允许用户与游戏互动。

---

## 37. LLVM即将支持常量时间：保护加密代码

**原文标题**: Constant-time support coming to LLVM: Protecting cryptographic code

**原文链接**: [https://blog.trailofbits.com/2025/11/25/constant-time-support-coming-to-llvm-protecting-cryptographic-code-at-the-compiler-level/](https://blog.trailofbits.com/2025/11/25/constant-time-support-coming-to-llvm-protecting-cryptographic-code-at-the-compiler-level/)

无法访问文章链接。

---

## 38. 15年后，我用Outlook作为我的构建管道。

**原文标题**: After 15 years, I use Outlook as my build pipeline

**原文链接**: [https://iwriteaboutcode.blogspot.com/2025/11/after-15-years-i-have-finally-reached.html](https://iwriteaboutcode.blogspot.com/2025/11/after-15-years-i-have-finally-reached.html)

一位拥有15年经验的资深开发者幽默地坦白，由于官僚障碍和同事缓慢的访问权限配置，他将Microsoft Outlook用作构建管道的一部分。面对手动共享测试文件效率低下的问题，他实现了一个Python脚本，该脚本监控他的Outlook收件箱中的特定电子邮件，解析附件，然后自动将其发布到服务器端点。

作者承认这种解决方案的荒谬性和潜在的“hack性”，但认为它显着提高了测试的迭代速度，并减少了开发人员浪费的时间。他们强调了快速迭代周期的重要性，强调了减少的专注时间和手动部署如何导致错误和生产力下降。

作者通过指出该解决方案在功能上等同于同事直接调用端点（尽管有额外的步骤）来合理化这种非常规方法。他们实施了一个简单的安全措施（一个秘密口令），并开玩笑地表示，由于他们持续的工作时间，该解决方案具有很高的可用性。

作者最后承认该解决方案并不理想，但强调它是对令人沮丧的组织瓶颈的实际回应。他们开玩笑地建议他们甚至可能会将这种经历添加到他们的简历中，重视它所展示的解决问题的创造力。归根结底，这篇文章是对软件开发现实的幽默评论，在这种现实中，务实的解决方案有时胜过理论上的最佳实践。

---

## 39. YouTube有人需要配眼镜了：预言已应验

**原文标题**: Someone at YouTube Needs Glasses: The Prophecy Has Been Fulfilled

**原文链接**: [https://jayd.ml/2025/11/10/someone-at-youtube-needs-glasses-prophecy-fulfilled.html](https://jayd.ml/2025/11/10/someone-at-youtube-needs-glasses-prophecy-fulfilled.html)

作者幽默地哀叹 YouTube 主页设计越来越稀疏。他最初基于统计分析预测，由于信息密度降低，YouTube 主页到 2026 年 5 月将只显示一个视频。这一预测源于 Hacker News 上的批评，据称这触发了 YouTube 产品经理团队的行动。

然而，在最近一次更新后，作者发现他在 Apple TV 上的 YouTube 主页显示的视频甚至比预期的还要少。他声称这些变化是由 Gemini YouTube 工程师实施的，并且新设计在屏幕上显示的视频更少。

基于这一新数据，他讽刺性地调整了他的预测，现在估计到 2026 年 5 月主页将完全没有视频，比他最初的 9 月预测提前了。作者认为 YouTube 的产品经理要么是故意曲解要么是无意中实现了讽刺性批评，并推测这种趋势可能会导致 Neuralink 脑机接口的提前采用。本质上，他批评 YouTube 的设计选择毫无意义，并导致主页越来越空洞和无用。

---

## 40. 拉布布斯陨落与现代互联网潮流的泥淖

**原文标题**: The fall of Labubus and the mush of modern internet trends

**原文链接**: [https://www.michigandaily.com/arts/digital-culture/the-fall-of-labubus-and-the-mush-of-modern-internet-trends/](https://www.michigandaily.com/arts/digital-culture/the-fall-of-labubus-and-the-mush-of-modern-internet-trends/)

凯登·奥唐奈的文章探讨了拉布布玩具潮流的迅速兴起和衰落，并以此为视角来审视现代互联网潮流的更广阔图景。拉布布起源于一本图画书，在2024年和2025年人气爆发后迅速消退，反映了许多近期互联网现象的短暂性。

奥唐奈认为，互联网所促进的增强连接和短视频内容消费导致潮流更快地流行，但也消失得更快。 这创造了一个各种数字现象的“大杂烩”，而不是持续、统一的文化时刻。

虽然这种混乱的景象可能看起来不受欢迎，但奥唐奈认为，它反映了一个去中心化的互联网，用户被引导到利基社区，较小的社区创造了融合为大型潮流的趋势。 具有讽刺意味的是，这导致了一个更加统一和多元文化的互联网。 人们不再因为害怕错过而一窝蜂地追逐同一个潮流，而是可以自由地享受自己的兴趣，同时接触来自不同网络角落的趋势。

文章总结说，这种由互联网促进的文化和信息交流是一种积极的发展。 拉布布本身就是一个例子，说明文化壁垒如何通过互联网互动被打破，从而导致全球趋势。 奥唐奈拥抱现代互联网的混乱性，认为它提供了更加充满活力和包容性的文化体验。

---

## 41. 研究表明，部分服用GLP-1药物的人可能没有安全的停药途径。

**原文标题**: There may not be a safe off-ramp for some taking GLP-1 drugs, study suggests

**原文链接**: [https://arstechnica.com/health/2025/11/glp-1-drugs-improve-heart-health-but-only-if-you-keep-taking-them/](https://arstechnica.com/health/2025/11/glp-1-drugs-improve-heart-health-but-only-if-you-keep-taking-them/)

本文探讨了近期发表在《美国医学会内科学》上的一项研究，该研究引发了人们对使用 GLP-1 类药物（如替尔泊肽 [Zepbound]）实现减肥效果的可持续性的担忧。该研究发现，大多数在 36 周后停止服用替尔泊肽的参与者，体重会显著反弹，并且他们的心血管和代谢健康指标（血压、胆固醇、血糖）恶化。

医学专家建议将这些药物重新定义为“体重管理”而非“减肥”药物，这意味着可能需要长期使用。该研究跟踪了 670 名参与者，重点关注了在药物作用下减掉了至少 10% 体重的 308 名参与者。在切换到安慰剂后，该组中的绝大多数人体重至少反弹了 25%。

虽然有很小一部分人（约 17.5%）没有显著反弹体重，但研究人员无法确定解释他们成功的具体因素。文章强调，缺乏关于安全有效停止使用 GLP-1 类药物的策略的研究，例如逐渐减少剂量或改变生活方式。它还强调需要更多关于因开始和停止使用这些药物而引起的体重波动的长期影响的数据，因为反弹的体重可能不成比例地是脂肪。专家建议在与患者讨论这些药物时要谨慎，强调长期治疗的可能性。

---

## 42. RunC容器逃逸：Docker和Kubernetes用户须知

**原文标题**: RunC Container Escape: What Docker and Kubernetes Users Need to Know

**原文链接**: [https://www.minimus.io/post/new-vulnerabilities-in-runc-allow-container-escape-what-docker-and-kubernetes-users-need-to-know](https://www.minimus.io/post/new-vulnerabilities-in-runc-allow-container-escape-what-docker-and-kubernetes-users-need-to-know)

"RunC容器逃逸：Docker和Kubernetes用户须知" 这篇文章强调了runC（Docker和Kubernetes的核心组件）中容器逃逸漏洞的关键问题。虽然没有详细说明具体的漏洞利用方式，但标题警示Docker和Kubernetes用户，攻击者有可能突破容器化环境并获得对宿主系统的访问权限。

文章立即推介了旨在缓解容器漏洞的产品Minimus。它声称Minimus可以帮助用户避免超过97%的容器CVE，并提供对加固镜像、安全Helm charts和自定义镜像构建器的访问权限。这表明runC中的漏洞非常重要且可能广泛存在，因此需要像Minimus这样的解决方案。

关键要点是呼吁Docker和Kubernetes用户注意runC漏洞，并考虑安全措施（可能通过像Minimus这样的工具）来保护他们的容器化环境。重点在于容器逃逸的可能性以及需要强大的安全实践来防止漏洞。

---

## 43. 中国精英对人工智能表达怀疑

**原文标题**: PRC elites voice AI-skepticism

**原文链接**: [https://jamestown.org/prc-elites-voice-ai-skepticism/](https://jamestown.org/prc-elites-voice-ai-skepticism/)

无法访问文章链接。

---

## 44. 统一我们的移动和桌面领域

**原文标题**: Unifying our mobile and desktop domains

**原文链接**: [https://techblog.wikimedia.org/2025/11/21/unifying-mobile-and-desktop-domains/](https://techblog.wikimedia.org/2025/11/21/unifying-mobile-and-desktop-domains/)

维基媒体基金会成功统一移动和桌面域名：显著提升性能、SEO和用户体验

---

## 45. 古惑狼制作秘辛 (2011)

**原文标题**: Making Crash Bandicoot (2011)

**原文链接**: [https://all-things-andy-gavin.com/video-games/making-crash/](https://all-things-andy-gavin.com/video-games/making-crash/)

这篇发表于2011年2月2日的博文，是顽皮狗公司创始人之一撰写的关于古惑狼创作系列的第一部分。在撰写本文时（2011年），顽皮狗已是一家成熟的游戏工作室，但在1994年夏天，它还只是一个由作者和其合伙人杰森·鲁宾组成的两人小团队。

这篇博文重点介绍了顽皮狗即将经历的转变。经过八年的紧密合作和发布六款游戏后，他们准备突破两人公司的规模。 这一转变标志着顽皮狗的一个重要转折点，并为最终成为《古惑狼》的开发奠定了基础。 这篇博文是对开发故事的介绍，暗示了即将到来的扩张以及公司新篇章的开始。

---

## 46. ESP32

**原文标题**: ESP32

**原文链接**: [https://en.wikipedia.org/wiki/ESP32](https://en.wikipedia.org/wiki/ESP32)

ESP32是乐鑫科技设计的一系列低成本、低功耗微控制器，集成了Wi-Fi和蓝牙功能。它是ESP8266的继任者，由台积电制造。其主要特性包括多种处理器（Tensilica Xtensa LX6/LX7、RISC-V）、充足的内存（520 KiB SRAM）以及丰富的外部接口，如GPIO、ADC、DAC、SPI、I2C、UART、以太网MAC和CAN总线。

ESP32系列包含多个型号（ESP32、ESP32-S2、ESP32-S3、ESP32-C2、ESP32-C3、ESP32-C6、ESP32-H2、ESP32-C5和ESP32-P4），每个型号都具有不同的CPU配置、内存大小、无线连接选项（Wi-Fi 6、蓝牙5）、GPIO数量以及特殊功能，如USB OTG和机器学习加速。

ESP32芯片通常采用QFN封装，并集成到模块和开发板中。存在多个模块，包括ESP32-PICO系列，它将ESP32芯片与基本组件组合成一个小封装。像ESP-WROOM和ESP-WROVER系列这样的表面贴装模块也很常用，它们提供不同的天线选项（PCB走线、U.FL连接器）、闪存和PSRAM配置。这些模块的功能各不相同，常用于物联网和嵌入式应用。

更新的型号，如ESP32-C5和ESP32-P4，具有高级功能，如Wi-Fi 6、Zigbee/Thread支持以及用于图像和语音应用的增强处理能力。

---

## 47. 虫舍效应

**原文标题**: The Bughouse Effect

**原文链接**: [https://tsvibt.blogspot.com/2025/11/the-bughouse-effect.html](https://tsvibt.blogspot.com/2025/11/the-bughouse-effect.html)

Bughouse效应：探究与陌生人在线下四国象棋中产生的独特怒火，并将其与现实生活中因队友被认为无能或失败而导致合作努力失败的情况进行对比。

作者首先解释了疯狂象棋，一种被俘虏的棋子可以重新放回棋盘的变体。四国象棋更进一步，由两队两人组成，其中一个棋盘上被俘虏的棋子会被传递到队友的棋盘上。这种高度的相互依赖性和不可预测的下法会产生巨大的压力和一种特定的愤怒。

“Bughouse效应”的核心在于，当队友的行为，即使是看似微小的行为，破坏了一个精心构建的计划，导致失败时所感受到的挫败感。这种愤怒被描述为复杂的，包括破碎的合作、背叛-愤怒、蔑视、痛苦、困惑和怨恨。

作者认为，这种特定的愤怒，虽然由于沟通限制和缺乏问责制而在在线四国象棋中加剧，但也会在现实生活中显现。两个案例研究说明了这一点：克里斯蒂安·贝尔在片场的爆发，摄影师的行为打断了贝尔的表演；以及猎鹿博弈论模型，缺乏协调会导致所有参与者失败。文章表明，“Bughouse效应”发生在相互依赖的团队合作因队友被认为无能而被破坏时，导致不成比例的挫败感和愤怒。

---

## 48. 计算机及视频监视器故障排除和维修注意事项

**原文标题**: Notes on the Troubleshooting and Repair of Computer and Video Monitors

**原文链接**: [https://www.repairfaq.org/sam/monfaq.htm](https://www.repairfaq.org/sam/monfaq.htm)

本文是Samuel M. Goldwasser撰写并于1994-2021年拥有版权的基于CRT的计算机和视频显示器故障排除和维修的综合指南。它强调安全，因为高压组件和CRT内爆具有致命危险。

该指南涵盖显示器基础知识、特性和类型（模拟与数字、隔行扫描），以及性能测试和常见问题，如显示器无法工作、保险丝熔断和图像失真。它深入研究了显示器子系统，包括低压和高压电源、偏转系统和视频处理。

本文档提供了针对各种问题的详细故障排除步骤，例如电源故障、偏转问题（尺寸、位置、同步）、高压问题（打火、关机）和光栅/颜色/视频问题（黑屏、颜色问题、聚焦问题）。它还提供有关聚焦、亮度、色彩平衡和几何校正等调整的指导。

除了维修之外，本文档还讨论了显示器放置、预防性维护以及其他问题，如嗡嗡声、啸叫声、干扰和烧焦气味。它包括有关识别组件、测试程序以及在哪里找到零件和原理图的信息。最后，它涉及各种感兴趣的主题，例如显示器规格、刷新率、视频标准、节能模式和报废显示器的处理，以及提供其他信息来源和USENET新闻组的链接。

---

## 49. 通过人工智能加速科学的国家使命

**原文标题**: A National Mission to Accelerate Science Through Artificial Intelligence

**原文链接**: [https://energy.gov/genesis](https://energy.gov/genesis)

无法访问文章链接。

---

## 50. KDE Plasma 6.8 将仅支持 Wayland，不再提供 X11 会话支持

**原文标题**: KDE Plasma 6.8 Will Go Wayland-Exclusive in Dropping X11 Session Support

**原文链接**: [https://www.phoronix.com/news/KDE-Plasma-68-Wayland-Exclusive](https://www.phoronix.com/news/KDE-Plasma-68-Wayland-Exclusive)

KDE开发者宣布，为全面转向Wayland，Plasma 6.8将仅支持Wayland，不再支持Plasma X11会话。虽然Plasma X11会话将被移除，但对X11应用程序和游戏的支持将通过XWayland继续提供。

开发者表示，大多数用户已在使用Wayland会话，移除X11支持将有助于加快开发速度、推出新功能并进行优化。

仍然依赖X11会话的用户有时间进行迁移。包含X11支持的Plasma 6.7系列将维护到2027年初，可能会发布额外的错误修复版本以满足X11用户的需求。更多详情请访问KDE.org博客。该声明于2025年11月26日发布。

---

## 51. Show HN：我做了一个交互式 HN 模拟器

**原文标题**: Show HN: I built an interactive HN Simulator

**原文链接**: [https://news.ysimulator.run/news](https://news.ysimulator.run/news)

推出互动式 Hacker News (HN) 模拟器

---

## 52. 生产环境中的实用安全

**原文标题**: Practical Security in Production

**原文链接**: [https://queue.acm.org/detail.cfm?id=3773097](https://queue.acm.org/detail.cfm?id=3773097)

无法访问文章链接。

---

## 53. 大理石泉 (1993)

**原文标题**: Marble Springs (1993)

**原文链接**: [https://www.eastgate.com/MS/Title_184.html](https://www.eastgate.com/MS/Title_184.html)

《大理石泉(1993)》是由迪娜·拉森创作、凯瑟琳·A·特纳-苏亚雷斯配图的超文本小说。由Eastgate Systems出版，这部作品通过大量的链接鼓励读者探索。此版本为万维网示例，包含35页和约600个链接，远小于完整的HyperCard版本。

完整版允许用户点击任何位置开始阅读，而此演示版本提供了一系列起始点。读者可以从多个节点开始探索，包括“序言”、“演示版本内容”、“定居”、“旅程”、“历史”、“尊重”、“葡萄酒中的低语”、“头发”、“计数”和“南希医生”。其他选项更偏元文本，允许读者了解作者、版权信息、如何阅读超文本，甚至如何编写超文本。

该文本还提供了如何订购完整版《大理石泉》的信息，并推荐了另一部Eastgate小说，暗示读者是对此类文学感兴趣的社群的一部分。版权声明表明拉森保留作品权利，强调了其原创性。

---

## 54. 充气式空间站

**原文标题**: Inflatable Space Stations

**原文链接**: [https://worksinprogress.co/issue/inflatable-space-stations/](https://worksinprogress.co/issue/inflatable-space-stations/)

本文探讨了空间站设计的历史性偏离，从早期旋转式、人工重力空间站的设想到成为常态的模块化、零重力结构。 冯·布劳恩等先驱倡导旋转轮式空间站以对抗失重带来的生理影响，但阿波罗计划转移了重心，导致了像天空实验室和国际空间站这样更小、更模块化的空间站的出现。

本文强调了建造大型空间站的工程挑战，特别是如何将它们装入细长的火箭。 像国际空间站那样，模块化组装是有效的，但规模有限。 单元化空间站，如充气式设计，提供了一种替代方案，有可能克服体积限制。 包括固特异轮胎充气管和刚性六边形结构在内的早期NASA兰利原型探索了这一概念。

商业航天公司现在正在重新审视人工重力，Vast 公司的目标是到 2035 年建成一个可容纳 40 人的旋转空间站。 太空制造是一个关键驱动因素，最初专注于零重力生产，但可能导致用于火星任务的更大、充气的结构。

像国际空间站上的毕格罗模块这样的充气式空间站，由于高强度织物的发展及其高效的体积利用率而越来越受欢迎。 文章最后指出，回归充气式、旋转式设计可能是实现早期太空先驱所设想的人工重力空间站宏伟愿景的关键。 对体积和地板面积的追求强调了空间站设计的持续演变，以满足机组人员的舒适度和先进的太空制造需求。

---

## 55. 游戏业界的自残性脑损伤

**原文标题**: The games industry's self-induced traumatic brain injury

**原文链接**: [https://doctorow.medium.com/https-pluralistic-net-2025-11-17-stop-killing-games-again-object-transience-f63af9cde93f](https://doctorow.medium.com/https-pluralistic-net-2025-11-17-stop-killing-games-again-object-transience-f63af9cde93f)

科里·多克托罗的文章《游戏产业自残式脑损伤》认为，游戏产业正在系统性地摧毁自身的历史，并通过使游戏变得短暂且难以访问来制造“脑损伤”。他将此归因于多种因素的结合，主要是DRM（数字版权管理）、纯在线组件和“游戏即服务”模式。

多克托罗指出，DRM积极阻止了保存工作，并在DRM服务器关闭后使游戏无法运行。即使是单人游戏，对始终在线功能的依赖也会在服务器退役时使其过时。“游戏即服务”模式通过不断更新和更改游戏，有效地覆盖和使以前的版本不可用，从而进一步加剧了这个问题。

他认为，这种短暂性损害了该行业，因为它阻止了后代从过去中学习，并可能导致停滞和重复。它也降低了游戏的文化意义，因为它们被视为一次性商品，而不是持久的艺术形式。他将其与电影和文学等其他艺术媒介进行了对比，在这些媒介中，保存和可访问性被认为是至关重要的。

多克托罗最后呼吁游戏行业采取更可持续的做法，例如优先考虑单人离线模式、删除DRM以及存档旧版本的游戏。他认为，尊重自身历史的举措最终将使该行业及其玩家受益。本质上，他认为该行业正在通过抹去其过去来积极伤害自己，并主张积极保存。

---

## 56. 音高倍增 (2017)

**原文标题**: Pitch Multiplication (2017)

**原文链接**: [https://klangnewmusic.weebly.com/direct-sound/pitch-multiplication](https://klangnewmusic.weebly.com/direct-sound/pitch-multiplication)

这篇名为“音高倍增”的文章介绍了音高倍增的概念，这是一种皮埃尔·布列兹等人用于生成音高素材的作曲技巧。作者解释说，音高倍增涉及将两个音高类集合相乘以创建一个更大的超集。

文章区分了简单倍增和复杂倍增，重点关注前者。它概述了关键术语，如“被乘数”、“乘数”、“乘积”、“标准型”和“OIS”。尼古拉斯·斯洛尼姆斯基的《音阶和旋律模式词典》被引用为一个早期例子，尽管斯洛尼姆斯基的方法创建的是单个集合的有序移调，这与布列兹的方法不同。

然后，作者详细介绍了两种简单的音高倍增方法：笛卡尔积和基于有序音程序列的方法。笛卡尔积涉及创建来自两个集合的元素对，将它们以模12求和，并得到一个新的集合。布列兹的方法，由斯蒂芬·海涅曼描述，依赖于确定一个集合的有序音高类音程结构（OIS），并使用另一个集合的元素作为OIS的移调级别，然后连接结果。文章还解释了如何通过旋转一个集合（被乘数）的顺序来生成不同的结果，从而改变OIS。最后，它演示了如何切换被乘数和乘数，但要求集合X保持标准型，集合Y转换为OIS。作者提供了示例来说明每种方法及其变体，强调生成的超集可以用于旋律写作或作为中间音高集合。

---

## 57. 太空：1999 – 特效技术

**原文标题**: Space: 1999 – Special Effects Techniques

**原文链接**: [https://catacombs.space1999.net/main/pguide/upsfx.html](https://catacombs.space1999.net/main/pguide/upsfx.html)

本文概述了科幻电视剧《太空：1999》中使用的特效技术，以及它与英国丰富的特效技术传承之间的联系。文章认为强大的英国电影业功不可没，这源于亚历山大·柯达及其招募的好莱坞特效专家内德·曼，后者培养了一代英国技术人员，包括沃尔特·珀西“波普”·戴、沃利·维弗斯、汤姆·霍华德、彼得·艾伦肖和莱斯·鲍伊。莱斯·鲍伊的影响力延伸到德里克·梅丁斯和布莱恩·约翰逊，他们与格里和西尔维娅·安德森以及在斯坦利·库布里克的《2001：太空漫游》中进一步磨练了他们的技能。

《太空：1999》的特效总监布莱恩·约翰逊借鉴了这些经验。他差点参与了《星球大战》的制作，但由于他对《太空：1999》的承诺而未能成行。《星球大战》后来彻底改变了特效技术，利用集成电路控制摄影机。

《太空：1999》的制作过程包括识别剧本中的特效场景，对其进行注释，为每个特效镜头创建故事板，并使用35毫米米切尔摄影机拍摄微缩模型（模型和场景）。拍摄通常在布雷工作室进行，包括带有摄影机沉陷部分的舞台。

---

## 58. 设计追随数据结构

**原文标题**: Design Follows Data Structures

**原文链接**: [https://www.tedinski.com/2019/01/29/data-structures-are-fundamental.html](https://www.tedinski.com/2019/01/29/data-structures-are-fundamental.html)

设计跟随数据结构：现代性能优化受缓存效率和内存布局影响巨大，数据表示是关键的设计考量。传统指令级优化作用减弱，编译器难以优化数据结构。面向对象编程虽封装数据结构，但性能驱动的修改仍是问题。侵入式数据表示修改更适合强类型语言，通过修改类型引入编译错误，再逐个修复，确保完整转换，避免兼容层。控制依赖，防止数据表示细节泄露到系统边界，强调设计初期考虑数据结构的重要性。

---

## 59. 西兰花侠，重制版

**原文标题**: Broccoli Man, Remastered

**原文链接**: [https://mbleigh.dev/posts/broccoli-man-remastered/](https://mbleigh.dev/posts/broccoli-man-remastered/)

本文详细介绍了作者使用人工智能技术重现谷歌文化经典“西兰花人”视频的经验。作者回忆起原始视频，仅用一个星期六的时间，便利用 Veo 3.1 和 Nano Banana 创作了一部 4 分钟的短片，承认其存在瑕疵，但强调其精神内核。

该过程包括使用 AI Studio 准备剧本，将原始视频分解为场景，然后使用 Magic Markup（Nano Banana 的一个工具）创建照片般逼真的人物素材。之后，作者使用 Vertex AI Studio 和 Veo 3.1，根据提示生成视频片段，并强调生成多个镜头和调整提示的迭代过程。CapCut 用于剪辑，Suno v5 用于片尾字幕音乐。

作者强调，角色一致性、声音一致性和音频同步出乎意料地容易实现。然而，挑战包括处理固定的 8 秒时长、保持静态场景的趣味性、实现机位/镜头控制、激发强烈的人物情感（“表情！ ”）、应对内容护栏，以及执行快节奏的动作和特定的人物互动。

后期制作涉及大量的修剪、交错不同的镜头以及在 CapCut 中处理音频。作者强调了非线性视频编辑对于成功的必要性，以及有意的时间安排和构图的重要性。

作者总结道，虽然结果并非电影大片，但如果没有人工智能，这个项目是不可能完成的。这次创作是一次有趣的练习，并为谷歌员工提供了娱乐。作者认为，技术放大了意图，无论是创造性的快乐还是愤世嫉俗的贪婪，最终，创造力和人类的努力将永远受到重视。

---

## 60. Show HN: 一款能近乎零成本交付的WordPress插件，可重写图片URL

**原文标题**: Show HN: A WordPress plugin that rewrites image URLs for near-zero-cost delivery

**原文链接**: [https://wordpress.org/plugins/bandwidth-saver/](https://wordpress.org/plugins/bandwidth-saver/)

带宽节省器是一款WordPress插件，旨在通过Cloudflare全球网络加速网站图像交付，降低带宽消耗并缩短页面加载时间。它提供两种模式：一种是“托管”选项，一键设置，每月2.99美元，由ImgPro负责基础设施；另一种是免费的“自托管”选项，适用于希望使用自己的Cloudflare账户进行完全控制的开发者。

该插件会重写图像URL以指向Cloudflare，首次访问时缓存图像，并为后续访问者从最近的边缘服务器提供图像。它与几乎任何主题、页面构建器、图像优化插件或缓存插件兼容，并支持各种图像格式。如果CDN不可用，图像会自动从源服务器加载。

带宽节省器优先考虑隐私，避免访客跟踪、cookies和分析。对于托管用户，仅存储站点URL和管理员电子邮件以进行帐户管理。该插件是开源的，允许检查、派生和贡献。设置包括简单激活托管选项，或者部署Cloudflare worker并配置R2存储桶用于自托管选项。

---

## 61. 维护开源项目那些不为人知的事

**原文标题**: What they don't tell you about maintaining an open source project

**原文链接**: [https://andrej.sh/blog/maintaining-open-source-project/](https://andrej.sh/blog/maintaining-open-source-project/)

无法访问文章链接。

---

## 62. 未通电的固态硬盘会缓慢丢失数据

**原文标题**: Unpowered SSDs slowly lose data

**原文链接**: [https://www.xda-developers.com/your-unpowered-ssd-is-slowly-losing-your-data/](https://www.xda-developers.com/your-unpowered-ssd-is-slowly-losing-your-data/)

固态硬盘在长期断电数据存储中的局限性

本文探讨了使用固态硬盘进行长期断电数据存储的局限性。虽然固态硬盘因其速度和效率在很大程度上取代了硬盘，但由于数据保留问题，它们并非冷存储的理想选择。固态硬盘使用NAND闪存单元来存储数据，即使没有电源也能保留信息，但这种保留不是无限期的。

数据保留时间取决于NAND的类型：QLC NAND可以保存数据约一年，TLC NAND可以保存数据长达3年，而MLC/SLC可以保存5-10年。由于大多数消费级固态硬盘使用TLC或QLC NAND，因此长时间（超过一年）断电会增加数据损坏或丢失的风险，这是由于NAND单元中的电压损失造成的。

然而，本文强调，这个问题主要关系到需要将大量数据在断电驱动器上存档多年的企业、爱好者和个体经营者用户。对于偶尔断电几个月的典型PC用户来说，这不是一个主要问题。

作者强烈建议实施备份策略，例如3-2-1规则（3个数据副本存储在2种不同的介质上，其中1个异地备份），无论使用何种存储介质。这可以保护数据免受驱动器故障、电源浪涌和其他潜在问题的影响。虽然固态硬盘适用于经常使用的PC中的主存储，但它们对于长期断电的存档存储并不可靠。使用替代存储介质并投资于强大的备份系统对于数据保存至关重要。

---

## 63. 人类大脑预先配置了理解世界的指令。

**原文标题**: Human brains are preconfigured with instructions for understanding the world

**原文链接**: [https://news.ucsc.edu/2025/11/sharf-preconfigured-brain/](https://news.ucsc.edu/2025/11/sharf-preconfigured-brain/)

加州大学圣克鲁兹分校的研究人员利用脑 organoids 研究思想的起源，发现证据表明人脑预先配置了理解世界的指令。他们的研究发表在《自然神经科学》杂志上，表明这些 organoids 中最早的电活动以结构化的模式发生，即使没有任何外部感官体验。

研究团队观察到，在发育的前几个月内，发育中的 organoids 中的神经元会自发地发出类似于大脑“默认模式”的电信号，这是一种神经元放电的基本底层结构。这些模式在远在大脑能够处理诸如视觉或听觉等外部刺激之前就被观察到，这表明存在一种基因编码的蓝图，该蓝图在发育后期会被感觉输入进行改进。

该研究的资深作者 Tal Sharf 强调，这些自组装回路在任何外部经验之前就已经形成，表明大脑存在一个原始的“操作系统”。这一发现对理解神经发育障碍以及毒素对发育中大脑的影响具有重要意义。通过使用 organoids，研究人员可以在符合伦理且受控的环境中研究大脑发育的早期阶段，从而提供一个了解自组装过程的窗口。

这些发现为在临床前水平上开发针对脑部疾病的疗法和干预措施（包括药物疗法和基因编辑工具）开辟了可能性。该研究强调了 organoids 作为理解人类神经发育、疾病和毒素对大脑影响的模型的潜力。

---

## 64. 印度科幻史

**原文标题**: The history of Indian science fiction

**原文链接**: [https://altermag.com/articles/the-secret-history-of-indian-science-fiction](https://altermag.com/articles/the-secret-history-of-indian-science-fiction)

本文探讨了印度科幻小说的历史，认为它具有独特的轨迹，受殖民历史、社会运动和语言多样性的影响。文章以Rokeya Sakhawat Hossain的《苏丹娜之梦》（1905年）为基础文本，突出了其女性主义乌托邦愿景和“认知疏离”的运用。

文章指出，早期印度科幻小说主要以乌尔都语和孟加拉语写成，通常与社会现实主义相关联，并且作者多为科学家，从而形成了一种被称为“kalpavigyan”或“scientifiction”的风格。文章将其与西方英语科幻小说的演变进行了对比，后者从技术乐观的通俗小说发展到探索性别、种族和数字时代等具有社会意识的作品。尽管科幻小说领域存在国际对话，但独立后的印度科幻小说在某种程度上仍然孤立。

文章进一步解释说，尽管后殖民时期的印度英语小说以严肃、主题沉重的作品为主，但在非英语语言中，类型文学仍在继续发展，文章引用了萨蒂亚吉特·雷的《尚古教授》系列和苏佳塔在泰米尔语的作品等例子。文章还指出，这些本地语言作品的科学倾向强调娱乐和教育。最终，文章强调需要在印度科幻小说内部加强翻译和跨文化对话，以充分认识其历史和潜力。

---

## 65. 沙丘蠕虫归来：超过300个NPM包被感染

**原文标题**: Shai-Hulud Returns: Over 300 NPM Packages Infected

**原文链接**: [https://helixguard.ai/blog/malicious-sha1hulud-2025-11-24](https://helixguard.ai/blog/malicious-sha1hulud-2025-11-24)

螺旋卫士安全研究团队发现了一起影响超过300个NPM软件包的广泛供应链攻击，名为“沙虫归来”，典出《沙丘》中的沙虫。该攻击涉及将恶意代码注入这些软件包，可能危及依赖于它们的应用程序。

被入侵的软件包包含旨在窃取敏感信息的代码，例如环境变量、API密钥，甚至可能包括加密货币钱包。攻击者可能正在使用自动化方法注入此恶意代码，目标是流行和广泛使用的NPM库，以最大限度地扩大其影响范围。

研究人员强调定期审计您的依赖项并使用安全工具来检测和预防此类攻击的重要性。强烈建议开发人员检查其项目是否存在易受攻击的软件包，并更新到安全版本或完全删除它们。摘要中并未完全详细说明代码注入的确切机制，但重点是其影响以及开发人员采取预防措施以保护其应用程序和用户数据的紧迫性。该事件凸显了开源生态系统中与供应链漏洞相关的持续风险。

---

## 66. Unison 1.0
统一体 1.0

**原文标题**: Unison 1.0

**原文链接**: [https://www.unison-lang.org/unison-1-0/](https://www.unison-lang.org/unison-1-0/)

Unison 1.0标志着函数式编程语言、其分布式运行时及其开发者工作流程的一个重要里程碑。该版本的发布意味着语言核心的稳定、优化后的工具、协作功能以及部署平台Unison Cloud的推出。

Unison独特地通过内容而非文件名来识别代码，从而带来诸多益处，例如无冗余编译、更少的版本冲突以及构建自部署分布式系统的能力。代码在名为“代码库”的数据库中管理，可通过CLI工具UCM和GUI浏览器UCM Desktop访问。Unison Share作为代码托管的社区中心，提供可导航的超链接。

Unison Cloud简化了应用程序的部署，无需YAML文件或复杂的部署脚本。本文通过一个猜数字游戏的例子概述了该语言的核心功能。

本文详细介绍了Unison的开发时间线，从2018年公司成立到关键里程碑，如首次Alpha版本发布、采用SQLite作为代码库、LSP支持、项目分段以及Unison Cloud的发布。关键指标突出了项目的势头，包括提交、合并的PR、GitHub星标和库下载量。

未来的计划包括C FFI支持、改进的记录类型、更好的库管理、更快的代码库同步、云可观察性以及一个智能代理计算框架。本文鼓励社区参与，并提供了常见问题的解答，解决了对供应商锁定的担忧，并强调了Unison的协作功能和原生版本控制。

---

## 67. 重新定义 .NET 的构建和发布 (再次)

**原文标题**: Reinventing how .NET builds and ships (again)

**原文链接**: [https://devblogs.microsoft.com/dotnet/reinventing-how-dotnet-builds-and-ships-again/](https://devblogs.microsoft.com/dotnet/reinventing-how-dotnet-builds-and-ships-again/)

.NET 在分布式开发模式下构建和发布产品所面临的挑战

本文探讨了由于分布式开发模式，.NET 在构建和发布其产品时所面临的挑战。最初，.NET 过渡到开源，并将组件拆分为多个存储库（CoreCLR、CoreFX 等）。虽然这种分布式方法具有分层、专注的社区和异步开发等优点，但当快速发布需要跨多个存储库进行协调更改的更新或安全补丁时，它会引入显著的复杂性和开销。

本文重点介绍了这种“分布式产品构建方法”的问题，尤其是难以在整个产品图中实现一致性（组件版本的一致）。一个需要多个团队和存储库之间进行协调的安全补丁的例子就说明了这一点，使得整个过程缓慢且不可预测。

作者介绍了两个关键概念：**产品构建复杂度**（将变更从开发人员传递到客户所需的步骤数）和**产品构建开销**（未积极生成可交付制品所花费的时间）。本文提供了详细的示例，说明了这些因素如何减慢 .NET 的构建和发布过程。

为了解决这些问题，.NET 正在采用一种名为 **统一构建** 的新方法。该项目旨在将产品构建整合到“虚拟单体”存储库中，创建“垂直构建”，同时仍然允许开发人员在单体之外工作。这种方法，以及 Linux 发行版源码构建等基础技术，有望降低复杂性和开销，最终加快 .NET 的构建和发布周期。

---

## 68. How the Atomic Tests Looked Like from Los Angeles

**原文标题**: How the Atomic Tests Looked Like from Los Angeles

**原文链接**: [https://www.amusingplanet.com/2016/09/how-atomic-tests-looked-like-from-los.html](https://www.amusingplanet.com/2016/09/how-atomic-tests-looked-like-from-los.html)

生成摘要时出错

---

## 69. Hollywood's vision of ancient Rome is all wrong, according to Mary Beard

**原文标题**: Hollywood's vision of ancient Rome is all wrong, according to Mary Beard

**原文链接**: [https://www.openculture.com/2025/11/why-your-vision-of-ancient-rome-is-all-wrong-according-to-historian-mary-beard.html](https://www.openculture.com/2025/11/why-your-vision-of-ancient-rome-is-all-wrong-according-to-historian-mary-beard.html)

生成摘要时出错

---

## 70. LPLB: An early research stage MoE load balancer based on linear programming

**原文标题**: LPLB: An early research stage MoE load balancer based on linear programming

**原文链接**: [https://github.com/deepseek-ai/LPLB](https://github.com/deepseek-ai/LPLB)

生成摘要时出错

---

## 71. Study claims to provide first direct evidence of dark matter

**原文标题**: Study claims to provide first direct evidence of dark matter

**原文链接**: [https://www.theguardian.com/science/2025/nov/25/study-claims-to-provide-first-direct-evidence-of-dark-matter](https://www.theguardian.com/science/2025/nov/25/study-claims-to-provide-first-direct-evidence-of-dark-matter)

生成摘要时出错

---

## 72. Bad UX World Cup 2025

**原文标题**: Bad UX World Cup 2025

**原文链接**: [https://badux.lol/](https://badux.lol/)

生成摘要时出错

---

## 73. Nearby peer discovery without GPS using environmental fingerprints

**原文标题**: Nearby peer discovery without GPS using environmental fingerprints

**原文链接**: [https://www.svendewaerhert.com/blog/nearby-peer-discovery/](https://www.svendewaerhert.com/blog/nearby-peer-discovery/)

生成摘要时出错

---

## 74. Windows GUI – Good, Bad and Pretty Ugly (2023)

**原文标题**: Windows GUI – Good, Bad and Pretty Ugly (2023)

**原文链接**: [https://creolened.com/windows-gui-good-bad-and-pretty-ugly-ranked/](https://creolened.com/windows-gui-good-bad-and-pretty-ugly-ranked/)

生成摘要时出错

---

## 75. AI has a deep understanding of how this code works

**原文标题**: AI has a deep understanding of how this code works

**原文链接**: [https://github.com/ocaml/ocaml/pull/14369](https://github.com/ocaml/ocaml/pull/14369)

生成摘要时出错

---

## 76. The Generative Burrito Test

**原文标题**: The Generative Burrito Test

**原文链接**: [https://www.generativist.com/notes/2025/Nov/25/generative-burrito-test.html](https://www.generativist.com/notes/2025/Nov/25/generative-burrito-test.html)

生成摘要时出错

---

## 77. Google's new 'Aluminium OS' project brings Android to PC

**原文标题**: Google's new 'Aluminium OS' project brings Android to PC

**原文链接**: [https://www.androidauthority.com/aluminium-os-android-for-pcs-3619092/](https://www.androidauthority.com/aluminium-os-android-for-pcs-3619092/)

生成摘要时出错

---

## 78. Mind-reading devices can now predict preconscious thoughts

**原文标题**: Mind-reading devices can now predict preconscious thoughts

**原文链接**: [https://www.nature.com/articles/d41586-025-03714-0](https://www.nature.com/articles/d41586-025-03714-0)

生成摘要时出错

---

## 79. Show HN: Anthony Bourdain's Lost Li.st's

**原文标题**: Show HN: Anthony Bourdain's Lost Li.st's

**原文链接**: [https://bourdain.greg.technology/](https://bourdain.greg.technology/)

生成摘要时出错

---

## 80. A million ways to die from a data race in Go

**原文标题**: A million ways to die from a data race in Go

**原文链接**: [https://gaultier.github.io/blog/a_million_ways_to_data_race_in_go.html](https://gaultier.github.io/blog/a_million_ways_to_data_race_in_go.html)

生成摘要时出错

---

## 81. The Definitive Classic Mac Pro (2006-2012) Upgrade Guide

**原文标题**: The Definitive Classic Mac Pro (2006-2012) Upgrade Guide

**原文链接**: [https://blog.greggant.com/posts/2018/05/07/definitive-mac-pro-upgrade-guide.html](https://blog.greggant.com/posts/2018/05/07/definitive-mac-pro-upgrade-guide.html)

生成摘要时出错

---

## 82. Indie game developers have a new sales pitch: being 'AI free'

**原文标题**: Indie game developers have a new sales pitch: being 'AI free'

**原文链接**: [https://www.theverge.com/entertainment/827650/indie-developers-gen-ai-nexon-arc-raiders](https://www.theverge.com/entertainment/827650/indie-developers-gen-ai-nexon-arc-raiders)

生成摘要时出错

---

## 83. Using an Array of Needles to Create Solid Knitted Shapes

**原文标题**: Using an Array of Needles to Create Solid Knitted Shapes

**原文链接**: [https://dl.acm.org/doi/10.1145/3746059.3747759](https://dl.acm.org/doi/10.1145/3746059.3747759)

生成摘要时出错

---

## 84. Ironwood, our latest TPU

**原文标题**: Ironwood, our latest TPU

**原文链接**: [https://blog.google/products/google-cloud/ironwood-google-tpu-things-to-know/](https://blog.google/products/google-cloud/ironwood-google-tpu-things-to-know/)

生成摘要时出错

---

## 85. Ozempic does not slow Alzheimer's, study finds

**原文标题**: Ozempic does not slow Alzheimer's, study finds

**原文链接**: [https://www.semafor.com/article/11/25/2025/ozempic-does-not-slow-alzheimers-study-finds](https://www.semafor.com/article/11/25/2025/ozempic-does-not-slow-alzheimers-study-finds)

生成摘要时出错

---

## 86. Claude Advanced Tool Use

**原文标题**: Claude Advanced Tool Use

**原文链接**: [https://www.anthropic.com/engineering/advanced-tool-use](https://www.anthropic.com/engineering/advanced-tool-use)

生成摘要时出错

---

## 87. Orion 1.0

**原文标题**: Orion 1.0

**原文链接**: [https://blog.kagi.com/orion](https://blog.kagi.com/orion)

生成摘要时出错

---

## 88. Japan's gamble to turn island of Hokkaido into global chip hub

**原文标题**: Japan's gamble to turn island of Hokkaido into global chip hub

**原文链接**: [https://www.bbc.com/news/articles/c8676qpxgnqo](https://www.bbc.com/news/articles/c8676qpxgnqo)

生成摘要时出错

---

## 89. Terence Tao: At the Erdos problem website, AI assistance now becoming routine

**原文标题**: Terence Tao: At the Erdos problem website, AI assistance now becoming routine

**原文链接**: [https://mathstodon.xyz/@tao/115591487350860999](https://mathstodon.xyz/@tao/115591487350860999)

生成摘要时出错

---

## 90. The Bitter Lesson of LLM Extensions

**原文标题**: The Bitter Lesson of LLM Extensions

**原文链接**: [https://www.sawyerhood.com/blog/llm-extension](https://www.sawyerhood.com/blog/llm-extension)

生成摘要时出错

---

## 91. Fifty Shades of OOP

**原文标题**: Fifty Shades of OOP

**原文链接**: [https://lesleylai.info/en/fifty_shades_of_oop/](https://lesleylai.info/en/fifty_shades_of_oop/)

生成摘要时出错

---

## 92. Most Stable Raspberry Pi? Better NTP with Thermal Management

**原文标题**: Most Stable Raspberry Pi? Better NTP with Thermal Management

**原文链接**: [https://austinsnerdythings.com/2025/11/24/worlds-most-stable-raspberry-pi-81-better-ntp-with-thermal-management/](https://austinsnerdythings.com/2025/11/24/worlds-most-stable-raspberry-pi-81-better-ntp-with-thermal-management/)

生成摘要时出错

---

## 93. Brain has five 'eras' with adult mode not starting until early 30s

**原文标题**: Brain has five 'eras' with adult mode not starting until early 30s

**原文链接**: [https://www.theguardian.com/science/2025/nov/25/brain-human-cognitive-development-life-stages-cambridge-study](https://www.theguardian.com/science/2025/nov/25/brain-human-cognitive-development-life-stages-cambridge-study)

生成摘要时出错

---

## 94. Show HN: Wolfrominoes

**原文标题**: Show HN: Wolfrominoes

**原文链接**: [https://demos.samgentle.com/wolfrominoes/](https://demos.samgentle.com/wolfrominoes/)

生成摘要时出错

---

## 95. The Cloudflare outage might be a good thing

**原文标题**: The Cloudflare outage might be a good thing

**原文链接**: [https://gist.github.com/jbreckmckye/32587f2907e473dd06d68b0362fb0048](https://gist.github.com/jbreckmckye/32587f2907e473dd06d68b0362fb0048)

生成摘要时出错

---

## 96. Roblox is a problem but it's a symptom of something worse

**原文标题**: Roblox is a problem but it's a symptom of something worse

**原文链接**: [https://www.platformer.news/roblox-ceo-interview-backlash-analysis/](https://www.platformer.news/roblox-ceo-interview-backlash-analysis/)

生成摘要时出错

---

## 97. It is ok to say "CSS variables" instead of "custom properties"

**原文标题**: It is ok to say "CSS variables" instead of "custom properties"

**原文链接**: [https://blog.kizu.dev/css-variables/](https://blog.kizu.dev/css-variables/)

生成摘要时出错

---

## 98. Google steers Americans looking for health care into "junk insurance"

**原文标题**: Google steers Americans looking for health care into "junk insurance"

**原文链接**: [https://pluralistic.net/2025/11/25/open-season/](https://pluralistic.net/2025/11/25/open-season/)

生成摘要时出错

---

## 99. Fran Sans – font inspired by San Francisco light rail displays

**原文标题**: Fran Sans – font inspired by San Francisco light rail displays

**原文链接**: [https://emilysneddon.com/fran-sans-essay](https://emilysneddon.com/fran-sans-essay)

生成摘要时出错

---

## 100. US banks scramble to assess data theft after hackers breach financial tech firm

**原文标题**: US banks scramble to assess data theft after hackers breach financial tech firm

**原文链接**: [https://techcrunch.com/2025/11/24/us-banks-scramble-to-assess-data-theft-after-hackers-breach-financial-tech-firm/](https://techcrunch.com/2025/11/24/us-banks-scramble-to-assess-data-theft-after-hackers-breach-financial-tech-firm/)

生成摘要时出错

---

