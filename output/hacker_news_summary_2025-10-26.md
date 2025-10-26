# Hacker News 热门文章摘要 (2025-10-26)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 非洲烂到极致却又精彩的电影海报

**原文标题**: Movie Posters from Africa That Are So Bad, They're Good

**原文链接**: [https://www.utterlyinteresting.com/post/bizarre-movie-posters-from-africa-that-are-so-bad-they-re-good](https://www.utterlyinteresting.com/post/bizarre-movie-posters-from-africa-that-are-so-bad-they-re-good)

20世纪80年代末至90年代，加纳的电影业因进口的VHS录像带和流动影院而蓬勃发展。由于缺乏宣传材料，当地艺术家受雇创作电影海报。这些艺术家通常在信息有限的情况下工作，创作出充满想象力且往往不准确的好莱坞电影 depiction。这些海报画在回收的面粉袋上，优先考虑引人注目的视觉效果而非现实主义，其特色是夸张的肌肉、额外的肢体、无谓的暴力以及与原电影完全无关的元素。

起初，这些海报被视为“劣质艺术”，但后来因其原始的魅力、朋克精神以及流行文化和民间传说的独特融合而获得认可。Ernie Wolfe 和 Wolfgang Held 等收藏家帮助将其提升为收藏艺术品的地位，并在世界各地的画廊举办展览。Joe Mensah、Heavy J 和 Stoger 等艺术家成为了狂热偶像，因其独创性和视觉叙事而备受赞誉。

例如，一个骑着水上摩托的终结者、一个手持机关枪和胸前恶魔的《鬼玩人》中的艾什、一个手持乌兹冲锋枪的《洛奇4》中的史泰龙以及一个五头喷火的《铁血战士》。这些海报现在的价值不仅仅是猎奇品；它们让我们得以一窥在全球流行文化如何在西非以有限的资源和丰富的创造力被重新诠释。它们代表着韧性、视觉创新以及对现代营销的无菌完美的令人耳目一新的替代方案。

---

## 2. 让我们助力NetBSD在2025年底前冲过终点线

**原文标题**: Let's Help NetBSD Cross the Finish Line Before 2025 Ends

**原文链接**: [https://mail-index.netbsd.org/netbsd-users/2025/10/26/msg033327.html](https://mail-index.netbsd.org/netbsd-users/2025/10/26/msg033327.html)

在2025年10月26日发给NetBSD社区的邮件中，Jay Patel呼吁捐款，以帮助NetBSD基金会达到年度筹款目标5万美元。目前，该基金会已筹集到10,738美元，还需要额外的39,262美元才能完全资助其工作。

该邮件强调了捐款所支持的实际项目，特别提到了扩展NetBSD对RISC-V架构的支持以及正在进行的无线网络堆栈现代化（Wi-Fi更新），这对于笔记本电脑和嵌入式设备的可用性至关重要。

Patel强调了NetBSD在更广泛的技术领域的重要性，特别是其在促进可持续性和对抗计划报废方面的作用。通过支持各种新旧硬件，NetBSD为可能最终成为电子垃圾的设备赋予了新的生命，使其能够用作防火墙、文件服务器，甚至复古游戏机。

该邮件敦促用户考虑通过提供的链接（https://netbsd.org/donations/）进行年终捐赠，以确保NetBSD的持续开发和维护。Patel还鼓励那些已经捐款的人使用#WhyIRunNetBSD标签在社交媒体上分享该消息，以进一步传播对该项目的认识和支持。

---

## 3. 四五十六七十年代的一万张可下载电影海报

**原文标题**: 10k Downloadable Movie Posters From The 40s, 50s, 60s, and 70s

**原文链接**: [https://hrc.contentdm.oclc.org/digital/collection/p15878coll84/search](https://hrc.contentdm.oclc.org/digital/collection/p15878coll84/search)

本文宣布在CONTENTdm上发布一万张可供下载的20世纪40至70年代电影海报合集。文章强调用户需要在浏览器中启用Javascript才能充分互动和访问该合集，这表明该平台是数字或交互式的，可供用户查看和下载海报。核心信息是存在这个庞大的经典电影海报数字化档案，使其成为电影爱好者、研究人员和设计师的宝贵资源。

---

## 4. 那个让我对PyTorch有更深理解的Bug

**原文标题**: The bug that taught me more about PyTorch than years of using it

**原文链接**: [https://elanapearl.github.io/blog/2025/the-bug-that-taught-me-pytorch/](https://elanapearl.github.io/blog/2025/the-bug-that-taught-me-pytorch/)

作者详述了一段令人沮丧的调试历程，其中训练损失平台期最终被证实是PyTorch的一个Bug，而非超参数问题。最初，在使用Adam优化器在Apple Silicon GPU（MPS后端）上训练稀疏自编码器模型时，编码器权重神秘地冻结了。

在穷尽了超参数调整和重写损失函数等常见解决方案后，作者系统地调查了这个问题。他们确认了梯度在流动，但注意到Adam优化器中编码器权重的exp_avg_sq（二阶矩估计）卡在零，鉴于非零梯度，这是不可能的。这表明Adam内部存在一个特定于编码器的问题。

怀疑存在偏差校正问题，作者测试了不同的beta值，甚至绕过了指数平均，但没有发现任何变化。试图通过切换到float64来解决潜在的精度问题似乎解决了问题，但实际上切换到CPU才是解决方案。该Bug发生在MPS上的float32中。

根本原因是PyTorch MPS后端的一个Bug，其中`addcmul_`和`addcdiv_`操作在写入非连续输出张量时会静默失败。编码器权重被初始化为转置，导致Adam的状态张量（exp_avg和exp_avg_sq）继承了非连续的内存布局。修复方案包括在初始化时使权重连续，升级到PyTorch ≥2.4，或更新macOS到15+版本。

---

## 5. 形式推理 [pdf]

**原文标题**: Formal Reasoning [pdf]

**原文链接**: [https://cs.ru.nl/~freek/courses/fr-2025/public/fr.pdf](https://cs.ru.nl/~freek/courses/fr-2025/public/fr.pdf)

此PDF文档，名为“形式推理”，看起来是一个可能与渲染或处理相关的技术文件。其内容主要由PDF流对象组成，特别是使用FlateDecode压缩的XObject Form对象和对象流。

XObject Form对象（对象4、7、9、11、17、20、23和26）都定义了一个100x100单位的矩形边界框（BBox），将FormType设置为1，并使用单位矩阵，这表明它们代表可重用的图形元素或模板。每个XObject Form中的压缩流数据极少，可能包含简单形状或占位符的绘图指令。

对象6和214是对象流，用于存储和压缩大量的PDF对象。这些流表明PDF中可能存在数百个额外的对象，可能描述文档的结构、内容和渲染指令。对象253、298、323、327和338是包含需要进一步处理才能理解的数据的压缩流。

本质上，该PDF文件是使用表示图形元素和结构化对象的压缩数据流构建的。在没有解压缩和进一步分析的情况下，“形式推理”的具体内容或含义仍然不清楚，但该文件的技术性质是显而易见的。

---

## 6. 代码降临 2025：谜题数量首次从25题减少至12题

**原文标题**: Advent of Code 2025: Number of puzzles reduce from 25 to 12 for the first time

**原文链接**: [https://adventofcode.com/2025/about#faq_num_days](https://adventofcode.com/2025/about#faq_num_days)

Eric Wastl，编程解谜日历（Advent of Code，简称AoC）的创建者，宣布了即将到来的活动。AoC是一个编程谜题日历，适合各种技能水平和语言。它用于练习、训练和竞赛，只需最少的编程知识，并且可以在较旧的硬件上访问。

该公告包括解决谜题的通用技巧，例如针对示例进行测试、重新阅读描述以及向朋友或subreddit寻求帮助。它还回答了有关身份验证、谜题难度、谜题解锁时间（美国东部时间/UTC-5午夜）、高对比度模式以及谜题创意（不接受）的常见问题。

关键变更和政策已得到解决：

*   **减少谜题数量：** 为了减轻创建者的工作量，谜题数量首次从25个减少到12个。
*   **移除全球排行榜：** 全球排行榜已被移除，原因是其造成的压力和滥用，但私人排行榜仍然可以只读模式共享。
*   **不鼓励使用人工智能：** 不鼓励使用人工智能解决谜题，因为AoC专为人类解决问题而设计。
*   **版权：** AoC内容不得复制或重新分发。
*   **私人排行榜规则：** 私人排行榜的参与者应遵守管理员设定的规则。

该公告感谢了AoC的贡献者，并包含一项法律声明，声明版权和商标保护。

---

## 7. 通过未加密卫星监听内部网络

**原文标题**: Eavesdropping on Internal Networks via Unencrypted Satellites

**原文链接**: [https://satcom.sysnet.ucsd.edu/](https://satcom.sysnet.ucsd.edu/)

加州大学圣地亚哥分校和马里兰大学帕克分校的研究人员对地球静止轨道(GEO)卫星通信进行了一项全面研究，发现大量未加密的敏感信息正在广播，任何拥有现成且廉价设备的人都可以访问。

暴露的数据包括蜂窝回程流量（通话、短信、用户互联网、加密密钥）、军事和政府通信、飞行中Wi-Fi数据、VoIP通话、内部商业网络流量（登录凭证、电子邮件、库存、ATM信息）以及关键基础设施SCADA数据。

研究小组从一个地点被动观测了39颗GEO卫星上的411个转发器，凸显了这种普遍存在的漏洞。虽然一些受影响的方，例如T-Mobile、沃尔玛和KPU，在接到通知后已经部署了补救措施，但由于缺乏负责卫星通信加密的中央机构，该问题在全球范围内仍未得到解决。

该报告建议使用卫星通信的组织将其视为不安全的网络，并在每一层实施加密。最终用户可以使用VPN和端到端加密的应用程序来保护他们的数据。研究人员正在发布开源工具，以帮助其他人审计他们的网络，并可进行合作和解答疑问。该研究刻意避免对卫星运行造成任何干扰，并侧重于被动观察。

---

## 8. 一名工人掉入核反应堆池中

**原文标题**: A worker fell into a nuclear reactor pool

**原文链接**: [https://www.nrc.gov/reading-rm/doc-collections/event-status/event/2025/20251022en?brid=vscAjql9kZL1FfGE7TYHVw#en57996:~:text=TRANSPORT%20OF%20CONTAMINATED%20PERSON%20OFFSITE](https://www.nrc.gov/reading-rm/doc-collections/event-status/event/2025/20251022en?brid=vscAjql9kZL1FfGE7TYHVw#en57996:~:text=TRANSPORT%20OF%20CONTAMINATED%20PERSON%20OFFSITE)

美国核管理委员会报告：2025年10月21日至22日期间上报的数起非紧急事件

*   **沃尔夫溪（堪萨斯州）：** 由于燃料重装期间的电气问题，控制室应急通风系统的两列火车均无法运行10分钟，导致控制室通风隔离信号并进入技术规范LCO。燃料移动暂停。
*   **帕利塞兹（密歇根州）：** 一名工人跌入充满水的反应堆腔，摄入了一些水，并在去污后被送往场外接受治疗。
*   **北安娜（弗吉尼亚州）：** 1号机组因负速率跳闸从74%功率自动跳闸。辅助给水泵按设计启动。
*   **皮埃蒙特心脏研究所（佐治亚州）：** 在一家医疗机构的例行泄漏测试中，发现了一个泄漏的铯-137源。该源已得到保护，该区域已去污。
*   **通用工程服务公司（内华达州）：** 一个包含镅-241和铯-137的便携式仪表从里诺的一辆卡车上被盗。
*   **埃尔姆赫斯特医院（伊利诺伊州）：** 一瓶镥-177在热实验室中掉落，污染了一名技术员。去污工作正在进行中。
*   **帕利塞兹（密歇根州）：** 向密歇根州报告了有关超过国家污染物排放消除系统联氨许可证限值的情况。
*   **克林顿（伊利诺伊州）：** 1号机组因汽轮机电液控制 (EHC) 油系统泄漏而从 86% 功率手动跳闸。电厂已稳定在模式 3。

所有事件均未对公众或电厂人员的健康和安全产生任何影响。驻厂检查员已在适用情况下收到通知。

---

## 9. 你已经有 Git 服务器了

**原文标题**: You Already Have a Git Server

**原文链接**: [https://maurycyz.com/misc/easy_git/](https://maurycyz.com/misc/easy_git/)

本文认为你可能已经拥有了一个 Git 服务器，并阐述了如何利用 SSH 访问具有 Git 仓库的服务器来进行版本控制、代码同步，甚至发布网站。

作者演示了通过 SSH 克隆仓库，强调了其对于本地开发以及将更改推送回服务器的实用性。他们解决了使用 `git config receive.denyCurrentBranch updateInstead` 命令来防止推送到当前检出分支的常见问题。

文章随后深入探讨了如何将 Git 仓库用作网站的来源。这包括通过 HTTPS 克隆仓库，可能需要重命名 `.git` 目录或重新映射 URL 以实现更简洁的访问。要启用 HTTPS 克隆，`git update-server-info` 至关重要。

为了自动化 `git update-server-info` 过程，作者建议设置一个 `post-update` 钩子，这是一个在每次成功推送后执行的 shell 脚本。此钩子还可以触发其他操作，例如运行静态站点生成器，作者的博客工作流程就是一个例子。

作者最后强调了这种方法的优点：本地开发没有网络延迟，通过 Git 钩子实现自动化部署，在本地机器和服务器上都有内置备份，版本控制可以防止意外数据丢失并有助于调试。

---

## 10. 石棉肺

**原文标题**: Asbestosis

**原文链接**: [https://diamondgeezer.blogspot.com/2025/10/asbestosis.html](https://diamondgeezer.blogspot.com/2025/10/asbestosis.html)

这篇来自diamond geezer的博客文章反思了石棉暴露的遗害，起因是位于巴金的一座新纪念碑，该纪念碑旨在纪念那些死于相关疾病的人们。这篇文章重点介绍了开普石棉公司在巴金的工厂的历史，该工厂从1913年到1968年运营，工人在没有适当保护的情况下处理石棉，导致呼吸道疾病高发，并因“巴金咳嗽”而闻名于当地。

作者将这一历史悲剧与当今联系起来，指出建在原工厂旧址上的哈茨巷议会住宅区，现在正饱受污染土地和易燃包层相关问题的困扰。

随后，这篇文章将问题个人化，分享了作者祖父的故事，他的祖父曾在沃特福德的开普石棉公司担任石棉塑模工，并过早去世，可能死于石棉肺。作者的家人未能成功地将石棉肺确认为死因，这与最近向同一家工厂的前工人支付的赔偿金形成了对比。

作者将他祖父的命运与他自己父亲的长寿进行了对比，将这归功于科学、教育和工人权利的进步，强调了健康和安全法规的重要性。 他最后表达了对与父亲共度更多时光的感激之情，强调了石棉暴露对许多家庭造成的毁灭性影响。 巴金的纪念碑提醒着人们这些损失以及继续为改善工作条件而奋斗的必要性。

---

## 11. Pico-Banana-400k

**原文标题**: Pico-Banana-400k

**原文链接**: [https://github.com/apple/pico-banana-400k](https://github.com/apple/pico-banana-400k)

Pico-Banana-400K是一个新的大型数据集，包含约40万个文本-图像-编辑三元组，专为文本引导图像编辑研究而设计。该数据集由来自Open Images的原始图像、类人文本指令以及由Nano-Banana模型生成和验证的编辑图像组成。它涵盖8个语义类别下的35种不同的编辑操作，范围从基本的颜色调整到复杂的对象和场景操作。

主要特点包括适用于各种训练范式的多样化单轮和多轮数据、高分辨率图像、Gemini-2.5-Flash生成的提示，以及使用Gemini-2.5-Pro的自评估流程以确保编辑质量。数据集构建过程包括从原始图像生成指令，然后使用Nano-Banana模型编辑这些图像，随后进行严格的质量控制。

数据分为对象级别、场景构图、以人为中心、风格、文本和符号、像素和光度、比例和透视以及空间/布局编辑。该数据集分为用于监督微调（SFT）的单轮样本、偏好学习样本（失败案例）以及用于对话编辑的多轮样本。

Pico-Banana-400K旨在促进可控和指令感知图像编辑的研究，包括多轮编辑和基于奖励的训练。该数据集可通过Apple的公共CDN下载，其中包含访问编辑图像和原始Open Images数据集的说明。它以CC BY-NC-ND 4.0许可证发布，供非商业研究使用。

---

## 12. 缅甸军方关闭一大型网络犯罪中心，逮捕逾2000人

**原文标题**: Myanmar military shuts down a major cybercrime center, detains over 2k people

**原文链接**: [https://apnews.com/article/scam-centers-cybercrime-myanmar-a2c9fda85187121e51bd0efdf29c81da](https://apnews.com/article/scam-centers-cybercrime-myanmar-a2c9fda85187121e51bd0efdf29c81da)

缅甸军方关闭了泰缅边境附近的大型网络诈骗园区KK园区，拘留了2000余人，并查获数十个星链卫星互联网终端。该园区从事网络诈骗、非法赌博和跨境网络犯罪活动。这些诈骗中心以虚假工作承诺引诱其他国家的劳工，然后强迫他们从事网络诈骗等犯罪活动，通常涉及浪漫骗局和虚假投资。

KK园区位于妙瓦底，该地区军政府控制力有限，受民族武装影响。军方声称克伦民族联盟（一个民族武装组织）参与了诈骗项目，克伦方面否认了这一说法。

此次突袭发现了260多栋未注册建筑，并查获了30个星链终端。星链虽然在缅甸未经授权，但被用于规避互联网限制，尽管其政策禁止欺诈或欺骗行为。今年早些时候也曾发生过类似的网络诈骗打击行动，在中国、泰国和缅甸的合作下，被拐卖人员从诈骗园区获释。美国和英国也对类似的柬埔寨网络诈骗团伙的组织者实施了制裁。

---

## 13. 用 Rust 编写 RISC-V 模拟器

**原文标题**: Writing a RISC-V Emulator in Rust

**原文链接**: [https://book.rvemu.app/](https://book.rvemu.app/)

本文档介绍了一个使用 Rust 从头开始创建 64 位 RISC-V 模拟器的指南。目标是能够在模拟器中运行 xv6 操作系统。

本书旨在通过模拟器开发的实践过程，教授基本的计算机体系结构概念，包括 ISA、特权架构、异常、中断、外围设备（UART 和 Virtio）以及虚拟内存系统。

第 1 章概述了支持 xv6 所需实现的基本硬件组件。这包括 CPU（具有有限的指令集）、内存和系统总线、控制和状态寄存器 (CSR)、特权架构、异常处理、中断控制器（PLIC 和 CLINT）、UART、中断处理、Virtio 和虚拟内存系统。

第 2 章指定了所需的 RISC-V 指令集扩展：RV64I 基本整数指令集、用于乘法和除法的“M”扩展以及用于原子指令的“A”扩展。

完成本书和模拟器实现后，读者将拥有一个能够运行 xv6 操作系统的功能性模拟器。本书随附的源代码可在 d0iasm/rvemu-for-book 找到。作者 @d0iasm 欢迎通过 Twitter 或 GitHub issues 提供反馈和问题。

---

## 14. 通过网页连接到 20 世纪 80 年代的雅达利 BBS

**原文标题**: Connect to a 1980s Atari BBS through the web

**原文链接**: [https://www.southernamis.com/ataribbsconnect](https://www.southernamis.com/ataribbsconnect)

本文是一个在线雅达利电子公告栏系统（BBS）目录，旨在模拟1980年代的体验。这些BBS让人们怀旧地回顾了在线交流和雅达利电脑文化的早期时代。

该目录展示了各种BBS，每个BBS都有其独特的主题、软件和功能。有些是对历史BBS的恢复，例如Southern Amis BBS和NiteLite BBS，让人们得以一窥那个时代的原始在线环境。另一些，如Basement BBS和Heisenbergs Hideout，则融入了现代主题和功能，同时保留了复古的雅达利外观和感觉。

这些BBS使用不同的软件，包括AMIS（雅达利消息信息系统）、BBS Express Pro!和RatSoft SFHQ。许多BBS强调使用ATASCII图形，这是雅达利BBS的标志。它们还提供各种功能，从在线游戏和联网消息库到文件库和独特的惊喜。该目录重点介绍了维护这些BBS并保持雅达利BBS社区活跃的系统管理员（sysop）。各种各样的可用公告板展示了雅达利BBS持久的吸引力以及活跃的社区。

---

## 15. Linux启动过程：从电源按钮到内核

**原文标题**: The Linux Boot Process: From Power Button to Kernel

**原文链接**: [https://www.0xkato.xyz/linux-boot/](https://www.0xkato.xyz/linux-boot/)

本文详细解释了Linux启动过程，从按下电源按钮开始，直到内核开始初始化。它将该过程分解为三个关键部分。

**第一部分**涵盖了初始步骤，从CPU重置为实模式并执行固件（BIOS或UEFI）开始。固件执行硬件检查并加载引导加载程序（如GRUB）。引导加载程序将Linux内核（包括设置程序）加载到内存中，并传递重要信息。然后，设置程序通过对齐内存段、创建堆栈、清除BSS区域并查询固件以获取可用RAM来建立一致的工作区。

**第二部分**详细介绍了从实模式到现代Linux所需的64位长模式的过渡。这涉及通过保护模式精心策划的切换，利用全局描述符表（GDT）和中断描述符表（IDT）。代码禁用中断，打开A20线，并设置控制寄存器位（CR0）以启用保护模式。然后通过构建身份映射启用分页，最后，设置EFER寄存器中的LME位，使CPU过渡到长模式。

**第三部分**解释了64位存根如何解压缩压缩内核，并在必要时重新定位代码（尤其与内核地址空间布局随机化 - kASLR 相关），并跳转到内核的入口点。它涵盖了存根如何处理潜在的重叠问题，构建临时页面映射，并使用ELF标头将内核放置在正确的内存位置。kASLR 被讨论为一种安全功能，它可以随机化内核的内存地址以阻止攻击。本文最后提供了一个有用的关键术语词汇表。

---

## 16. Clojure乐土 - 探索开源Clojure库和框架

**原文标题**: Clojure Land – Discover open-source Clojure libraries and frameworks

**原文链接**: [https://clojure.land/](https://clojure.land/)

本文档是一个精选的开源Clojure库和框架列表，按功能分类。 它展示了Clojure生态系统的广度，突出了用于各种任务的工具。

一个重要的主题是开发者工具和AI辅助，其中包含多个用于不同编辑器（Emacs, VS Code）的“编辑器代码助手”（ECA）集成。 这些工具提供AI驱动的结对编程功能。 其他开发者实用工具包括改进的调试工具，如“hashp”，以及使用“clojure-cli-config”进行配置管理。

该列表收录了用于Web开发的库，包括Pedestal框架，用于构建OpenAPI服务的Legba和用于数据驱动渲染的Replicant。 它还介绍了使用Tapestry和Lacinia-Pedestal等库进行异步编程。

除了Web开发之外，该汇编还包括用于专门领域的工具，如数据处理（用于并行reducers的Tesser），科学计算（用于概率编程的Daphne），甚至量子计算（QClojure）。 clojure2d涵盖了图形方面，data.json促进了数据序列化。 Component提供了有状态对象的托管生命周期。 总之，它提供了Clojure社区及其开源贡献的多元化和活跃性的快照。

---

## 17. 激光镊子 - 光阱

**原文标题**: LaserTweezer – Optical Trap

**原文链接**: [https://www.gaudi.ch/GaudiLabs/?page_id=578](https://www.gaudi.ch/GaudiLabs/?page_id=578)

本文介绍如何利用回收的消费电子产品构建低成本的“自制光学镊子”（激光镊子）。光学镊子是一种科学仪器，它使用聚焦的激光束来操纵微观物体，如塑料珠或细胞。传统的装置既昂贵又庞大。

自制版本使用DVD驱动器的光头，其中包含激光器、准直透镜和聚焦机构。激光束捕获介电粒子，将它们吸引到光束的中心。一个用倒置透镜改装的USB网络摄像头提供了样品的放大视图。为了防止激光过度曝光，一个旋转的快门盘与间歇性激光切换同步。侧面安装的LED照亮样品。

该设备以显著降低的成本（低于100美元）和尺寸（低于500克）实现了光学捕获。小型苯乙烯珠可以被以良好的精度和图像质量进行操作。DVD驱动器的聚焦机构和一个简单的机械杠杆控制着激光束的移动。

本文引用了一篇详细介绍设置和电路的科学出版物。它还包括原理图、布局和Arduino控制软件的资源。所描述的项目是Hackteria网络的一部分。

---

## 18. Torchcomms：现代 PyTorch 通信 API

**原文标题**: Torchcomms: A modern PyTorch communications API

**原文链接**: [https://pytorch.org/blog/torchcomms/](https://pytorch.org/blog/torchcomms/)

Torchcomms是一个新的、实验性的PyTorch通信API，专为大规模分布式训练设计，旨在扩展到超过10万个GPU。它提供基础API和后端（如Meta开发的NCCLX后端），以实现可靠且高性能的分布式训练。

关键目标包括：更快地进行通信原语原型设计、扩展到大规模GPU部署、支持异构硬件、提供容错能力、启用单边通信以及促进以设备为中心的集合通信。通过将通信与PyTorch核心解耦，torchcomms允许独立迭代通信层并支持树外后端。

Torchcomms通过引入主动初始化、优化资源管理以及为可扩展且容错的训练铺平道路，从而解决了现有c10d API的局限性。它包括初始后端，如NCCLX（Meta对NCCL的扩展）、上游NCCL、用于AMD GPU的RCCL和Gloo。Torchcomms提供与DeviceMesh的兼容性，以便与PyTorch并行库（如FSDP2）集成。

新的API具有集合语义更改、用于远程内存访问的窗口API、用于使用RDMA的点对点操作的传输API以及容错API。该架构设计为可扩展的，允许开发人员轻松添加自定义集合通信和后端。虽然API仍在不断发展并且可能会发生更改，但长期愿景是将所有PyTorch分布式功能迁移到torchcomms基础上。

---

## 19. 主函数前的旅程

**原文标题**: The Journey Before main()

**原文链接**: [https://amit.prasad.me/blog/before-main](https://amit.prasad.me/blog/before-main)

Amit Prasad 的《main() 函数之前的旅程》探讨了程序启动到 `main()` 函数执行之间所经历的步骤。 该过程始于 `execve` 系统调用，该调用将可执行文件路径、参数和环境变量传递给内核。 然后，内核解析可执行文件（通常在 Linux 上为 ELF 格式），识别关键元素，如入口点地址和不同的段（.text、.data、.bss、.plt）。

内核将必要的段加载到内存中，如果存在 shebang，则使用指定的解释器。 ELF 解释器处理动态链接、安全缓解措施（如 ASLR 和 NX 位），并为程序的执行做准备。 一个关键步骤是设置堆栈，该堆栈存储 `argv`、`envp` 以及包含环境信息的 ELF 辅助向量。

该过程最终跳转到程序的入口点，通常是 `_start` 函数。 此函数通常由 glibc 或 musl 等库提供，它初始化语言运行时，设置线程本地存储，并执行其他特定于语言的任务。 最后，在运行时初始化之后，调用标准的 `main()` 函数。 作者强调，运行时初始化的级别在不同语言之间差异很大，Java 和 Python 等语言的运行时比 C/C++“更重”。

---

## 20. D2：图表脚本语言

**原文标题**: D2: Diagram Scripting Language

**原文链接**: [https://d2lang.com/tour/intro/](https://d2lang.com/tour/intro/)

D2是一种声明式图表脚本语言，可将文本描述转换为图表。其核心思想是，您定义想要图表化的*内容*，而D2生成可视化表示。要使用D2，您需要下载CLI，创建`.d2`文件，添加您的图表描述，然后运行命令生成图像。一个D2代码的基本示例展示了元素之间的关系，例如“NETWORKUSER”、“API SERVER”和“LOGS”。此外，还有诸如“watch mode”（持续更新和渲染）之类的功能。文档建议进行一个5-10分钟的快速浏览，并提供可下载的速查表。文档还提供了D2和D2-docs在GitHub上的源代码仓库链接，供进一步探索。文档中的代码片段是交互式的，允许用户在D2 Playground中进行实验，但使用导入的片段除外。该文档旨在快速入门D2，声称“入门”仅需2分钟。

---

## 21. 自由软件基金会认为大型语言模型。

**原文标题**: The FSF considers large language models

**原文链接**: [https://lwn.net/Articles/1040888/](https://lwn.net/Articles/1040888/)

2025年10月，自由软件基金会(FSF)正在努力应对大型语言模型(LLM)对自由软件许可的影响。FSF正在对自由软件项目进行调查，以了解他们对LLM生成的代码的立场，并旨在制定有关该问题的指导。

主要关注的问题包括大多数LLM及其训练数据的非自由性质、LLM生成代码的版权性，以及由于训练数据泄露到输出中而导致的潜在版权侵权。虽然有关于版权性的未决诉讼，但通过人工努力增强LLM输出或使用“创造性提示”可能会使代码具有版权。

FSF还在考虑引用代码灵感的必要性，而LLM目前无法做到这一点。对接受LLM生成代码的项目的建议预防措施包括披露所使用的LLM、其版本、训练数据信息、使用的提示以及任何使用限制。代码还应明确标记为LLM生成。

本文重点介绍了围绕定义“提示”的辩论，因为LLM生成的代码通常来自涉及多个提示和存储库交互的复杂工作流程。一些人认为LLM可以显著扩大项目范围，并且有助于简化设计并快速掌握宏观概念，而另一些人则担心过度依赖这些工具。

---

## 22. PCB边缘USB Type-C连接器库

**原文标题**: PCB Edge USB C Connector Library

**原文链接**: [https://github.com/AnasMalas/pcb-edge-usb-c](https://github.com/AnasMalas/pcb-edge-usb-c)

本文介绍了一个可以直接在PCB边缘创建USB-C连接器的库。该库包括10针和14针版本，适用于KiCAD和EasyEDA。在KiCAD中使用该库，用户应下载zip文件并通过插件和内容管理器(PCM)安装。在EasyEDA Pro中，可以通过.elibz文件导入该库，或者在公共库中搜索“PCBTypeC_10P”或“PCBTypeC_14P”。文章还提到，其他EDA工具（如Altium）可以导入KiCAD封装，而EasyEDA支持导出到Altium和PADS。但是，文章建议将导入的封装与原始KiCAD或EasyEDA封装进行验证，以确保导入过程后的准确性。本质上，该库提供了一种设计原生支持USB-C连接的PCB的方法，从而节省了连接器成本和空间。

---

## 23. Bitmovin（YC S15）正在欧洲招聘工程IC和经理

**原文标题**: Bitmovin (YC S15) Is Hiring Engineering ICs and Managers in Europe

**原文链接**: [https://bitmovin.com/careers](https://bitmovin.com/careers)

Bitmovin（YC S15公司）正在欧洲积极招聘工程领域的个人贡献者和经理，尤其是在维也纳、克拉根福和柏林等地，部分职位提供欧盟范围内的远程工作选择。该公司总部位于旧金山，并在全球设有办事处，致力于塑造视频的未来，使开发者能够轻松地以高质量编码、播放和分析视频内容。

Bitmovin强调“Bitmovers”的健康工作生活平衡，提供额外休假、家庭办公设备支持、员工活动、健康计划、弹性工作时间和慷慨的假期津贴等福利。他们还通过LinkedIn Learning访问、黑客马拉松、职业规划、培训计划、会议和书籍津贴等方式，大力投资于学习和发展。

该公司的核心价值观围绕着客户至上、主人翁精神、建设性批评、坚持不懈的创新和高效执行。Bitmovin是一家提供平等机会的雇主，欢迎有才华的人士提交简历申请，即使没有列出具体职位。他们正在所有部门寻找广泛的技能人才，目前列出的空缺职位包括工程管理（VOD编码）、高级软件工程师Java（LIVE编码）、高级/资深软件工程师C++和高级视频流工程师等工程职位。他们还在招聘客户成功、销售、产品管理和实习生等职位。

---

## 24. 我作为CTO仍然写代码的原因

**原文标题**: Why I code as a CTO

**原文链接**: [https://www.assembled.com/blog/why-i-code-as-a-cto](https://www.assembled.com/blog/why-i-code-as-a-cto)

在他的博文中，首席技术官王先生解释了为何他继续编写代码，尽管传统观点认为高级职位意味着较少的编码。他认为，编码是他作为技术领导者所从事的杠杆效应最高的活动之一。

王先生将他的编码项目分为三个领域：**长期实验性项目**、**关键客户请求**和**错误修复**。他利用实验性项目来推动新想法并进行模糊的赌注，因为他具有独特的优势来做到这一点。他处理关键客户请求以快速解决紧急问题并维护良好关系，并且他通过错误修复来维护代码库的心理地图并识别技术债务。

王先生概述了他的做法的两个主要原因：**与时俱进地了解有效的方法**和**专注于他的优势**。他每天使用人工智能工具来了解它们的功能和局限性，从而为关于工具和招聘的战略决策提供信息。他还更喜欢构建事物和解决技术问题，而不是组织管理。通过编码，他能感觉到架构何时过于复杂或技术债务何时成为问题。他将人员管理方面的工作外包给强大的工程经理。

王先生强调，人工智能工具提高了他的生产力，将他的工作从编写每一行代码转变为提供上下文、做出决策和评估解决方案。最后，他强调首席技术官的角色是灵活的，应该根据个人的优势、兴趣和公司需求进行调整。

---

## 25. NextSilicon发布新处理器芯片，挑战英特尔和AMD

**原文标题**: NextSilicon reveals new processor chip in challenge to Intel, AMD

**原文链接**: [https://www.reuters.com/business/nextsilicon-reveals-new-processor-chip-challenge-intel-amd-2025-10-22/](https://www.reuters.com/business/nextsilicon-reveals-new-processor-chip-challenge-intel-amd-2025-10-22/)

无法访问文章链接。

---

## 26. GenAI图像编辑对决

**原文标题**: GenAI Image Editing Showdown

**原文链接**: [https://genai-showdown.specr.net/](https://genai-showdown.specr.net/)

“GenAI图像编辑对决”文章很可能比较和对比不同的GenAI（生成式人工智能）图像编辑工具。 由于没有全文，无法得知正在测试的具体工具，但我们可以推断出一些可能的主题。

文章可能根据各种GenAI图像编辑平台执行以下任务的能力进行评估：

*   **文本生成图像：** 基于文本提示创建图像。
*   **图像修复/外绘：** 填充图像中缺失的区域或扩展到原始边界之外。
*   **物体移除/替换：** 选择性地移除不需要的物体并用其他东西替换它们。
*   **风格迁移：** 将一个图像的风格应用于另一个图像。
*   **图像增强：** 提高图像质量（分辨率、锐度、色彩校正）。
*   **换脸：** 替换图像中的面部。

“对决”方面表明了竞争性评估。 文章很可能根据以下因素比较这些工具：

*   **准确性和真实感：** 生成/编辑的图像看起来有多真实和令人信服。
*   **易用性：** 这些平台有多直观和用户友好。
*   **速度：** 这些工具处理和生成图像的速度有多快。
*   **自定义选项：** 用户对编辑过程的控制程度。
*   **成本：** 定价模式和可用性（免费与付费）。

文章可能以最佳GenAI图像编辑工具的排名或总结结尾，突出它们的优点和缺点，并可能为不同的用例推荐特定的工具。

---

## 27. 展示 HN：可拖拽定制的图表即代码工具

**原文标题**: Show HN: Diagram as code tool with draggable customizations

**原文链接**: [https://github.com/RohanAdwankar/oxdraw](https://github.com/RohanAdwankar/oxdraw)

Oxdraw是一款旨在弥合代码生成图（如Mermaid）与可定制图表软件（如Lucidchart）之间差距的工具。它允许用户使用Mermaid语法创建和维护图表，同时提供一个Web界面，用于对位置、连接器路径和颜色等元素进行可视化微调。

其主要特点是将可视化调整以声明式代码（存储为注释）的形式持久化回原始Mermaid源文件，从而确保可重现性和版本控制，同时保持与其他Mermaid工具的兼容性。Oxdraw由一个Rust CLI编译器和一个基于React的Web编辑器组成。

CLI工具将`.mmd`文件渲染为图像，并提供输出路径、格式、缩放、编辑器启动、服务器配置和背景颜色等标志。Web界面允许用户删除元素、调整节点/边缘样式（颜色、线条样式、箭头方向）、添加/删除边缘控制点，以及使用网格对齐和对齐参考线拖动节点/子图。

该工具的图表路径算法优先考虑清晰的边缘而不是平滑的线条，有时允许线条重叠以避免过长的连接。作者承认该算法有改进的潜力。

---

## 28. Project Amplify: 跑步和步行的动力鞋履

**原文标题**: Project Amplify: Powered footwear for running and walking

**原文链接**: [https://about.nike.com/en/newsroom/releases/nike-project-amplify-official-images](https://about.nike.com/en/newsroom/releases/nike-project-amplify-official-images)

耐克“放大项目”是一款突破性的动力鞋系统，旨在提升日常运动爱好者的跑步和步行体验。该系统通过增强小腿和脚踝的运动，旨在帮助用户以更少的努力更快、更远地移动。第一代产品将轻型电机、传动带和可充电袖口电池与碳纤维板跑步鞋集成在一起。这项创新面向那些希望使运动更轻松、延长步行通勤或增加跑步里程的运动员。

该技术基于耐克运动研究实验室的运动算法，并非为竞技跑步者设计。相反，“放大项目”专注于以每英里10到12分钟速度跑步的运动员，提供“第二组小腿肌肉”来让运动感觉更轻松。测试表明，该系统可以帮助用户提高速度，使上坡运动感觉像平地。

经过超过400名运动员和240万步的广泛测试，该系统得到了完善，目前正处于测试阶段。耐克正与机器人合作伙伴Dephy合作，为未来几年的广泛消费者上市做准备。“放大项目”代表了耐克对以运动员为中心的创新承诺，旨在增强运动并创造运动的未来，就像华夫饼烤盘开启的创新一样。

---

## 29. 加州投资电池储能，告别轮流停电

**原文标题**: California invests in battery energy storage, leaving rolling blackouts behind

**原文链接**: [https://www.latimes.com/environment/story/2025-10-17/california-made-it-through-another-summer-without-a-flex-alert](https://www.latimes.com/environment/story/2025-10-17/california-made-it-through-another-summer-without-a-flex-alert)

自2020年以来，由于对电池储能系统的大量投资，加州已大幅降低对紧急节能警报（弹性警报）和轮流停电的依赖。电池储能容量增加了3000%以上，使电网能够在太阳能电池板不发电的高峰需求时段储存太阳能。这一转变还减少了对老旧、不可靠且对环境有害的燃气发电厂的依赖。

电池储能的增加是加州到2045年实现100%碳中和目标的关键组成部分，促进了太阳能等可再生能源的整合，并减少了化石燃料的使用。虽然锂离子电池是最常见的类型，但铁-空气和液流电池等更长时长的选择正在成为扩展储能容量的潜在解决方案。

尽管取得了进展，但挑战依然存在。电网正在老化，需要进一步升级，许可审批过程可能漫长。安全问题也依然存在，大型电池储能设施发生火灾就是证明。然而，文章强调，电池储能的益处大于风险，特别是与石油、天然气和煤炭等传统能源相关的健康和环境危害相比。文章还提到了特朗普政府为支持化石燃料工业所做的努力，这与加州的清洁能源转型形成对比。最后，文章指出，即使面临挑战和障碍，CAISO的电网平均每天已有近七个小时由100%清洁能源供电。

---

## 30. 程序如何运行：ELF 二进制文件 (2015)

**原文标题**: How programs get run: ELF binaries (2015)

**原文链接**: [https://lwn.net/Articles/631631/](https://lwn.net/Articles/631631/)

这篇LWN.net文章深入探讨了Linux内核如何执行程序，重点关注ELF（可执行和可链接格式）二进制文件，这是现代Linux系统上的主要格式。该过程由`fs/binfmt_elf.c`中的`load_elf_binary()`函数处理。

内核解析ELF头和程序头表，优先处理`PT_LOAD`（内存段）、`PT_INTERP`（运行时链接器，如果是动态链接）和`PT_GNU_STACK`（堆栈可执行性）。`flush_old_exec()`清除前一个程序的状态，杀死线程，取消共享信号处理，更新可执行文件位置，释放虚拟内存，并移除影响安全性的个性化特征。然后，`setup_new_exec()`配置内核的内部状态，包括核心转储权限、任务名称、信号处理程序和文件描述符关闭。

为新程序设置虚拟内存，包括堆栈随机化。`PT_LOAD`段被映射到进程的地址空间中，BSS段被零填充。诸如vDSO之类的特殊页面也被映射。

通过`install_exec_creds()`设置凭据。最后，`create_elf_tables()`用辅助向量（包含关键的环境信息，如vDSO位置和随机数据）以及参数/环境变量数据填充堆栈。然后，`start_thread()`设置保存的指令指针和堆栈指针以启动程序执行。

对于动态链接程序（由`PT_INTERP`指示），运行时链接器会在主程序之前被加载和执行，使用`load_elf_interp()`。这确保在程序启动之前链接必要的共享库。

---

## 31. TinyKVM 更新

**原文标题**: An Update on TinyKVM

**原文链接**: [https://fwsgonzo.medium.com/an-update-on-tinykvm-7a38518e57e9](https://fwsgonzo.medium.com/an-update-on-tinykvm-7a38518e57e9)

本文更新了TinyKVM的最新进展，重点介绍了其扩展了纯计算能力之外的功能。作者Gonzo重点介绍了通过极简的系统调用模拟方法，增加了对运行未经修改的可执行文件（如Deno和Python WSGI）的有限支持。

一个关键亮点是向Laurence Rowe致敬，感谢他倡导用于TinyKVM服务器的KVM服务器CLI。

文章随后深入探讨了TinyKVM的混合式按请求隔离，它通过两种重置模式实现了速度快和低内存占用。此功能允许在每个请求后高效地将VM重置为原始状态，从而实现接近原生性能。

Gonzo还介绍了一种新颖的远程过程调用（RPC）机制，同一地址空间中的二进制文件可以直接调用彼此的函数，从而实现零拷贝数据传输。在调度器依赖和对抗性内存访问成为问题的情况下，这种方法提供了性能优势。

最后，文章详细介绍了VM快照的实现，允许保存和恢复VM状态，从而可能实现快速冷启动。作者讨论了正在进行的优化快照加载的工作，即仅选择性地预加载必需的页面。

---

## 32. 《神秘博士》档案专家分享遗失剧集积极进展

**原文标题**: Doctor Who archive expert shares positive update on missing episode

**原文链接**: [https://www.radiotimes.com/tv/sci-fi/doctor-who-missing-episodes-update-teases-announcement-newsupdate/](https://www.radiotimes.com/tv/sci-fi/doctor-who-missing-episodes-update-teases-announcement-newsupdate/)

文章标题为《神秘博士档案专家分享遗失剧集积极进展》，可能详细介绍了寻找经典电视剧《神秘博士》遗失剧集的信息。虽然提供的片段中没有包含更新的具体内容，但标题表明，一位《神秘博士》档案材料专家分享了一些积极的消息，内容涉及至少一集先前被认为遗失的剧集可能被找回或发现。

片段中还包含一则与此无关的《广播时报》杂志订阅广告，在限定时间内提供折扣价。这很可能是在网站或平台上与文章一起显示的上下文广告。此广告与报道《神秘博士》遗失剧集的实际新闻是分开的。

---

## 33. 闪电代理：用强化学习训练智能体（无需修改代码）

**原文标题**: Agent Lightning: Train agents with RL (no code changes needed)

**原文链接**: [https://github.com/microsoft/agent-lightning](https://github.com/microsoft/agent-lightning)

Agent Lightning 是一个工具，旨在通过强化学习等技术训练 AI 智能体，只需极少甚至无需代码修改。它适用于各种智能体框架（LangChain、OpenAI Agent SDK、AutoGen 等），甚至在没有框架的情况下也能工作，允许用户在多智能体系统中优化单个或多个智能体。

主要功能包括零代码更改集成、与任何智能体框架兼容、选择性智能体优化以及对强化学习和自动提示优化等算法的支持。

其架构涉及轻量级助手 (agl.emit_xxx()) 或追踪器，用于捕获提示、工具调用和奖励，然后将其存储在 LightningStore 中。算法读取这些跨度，从中学习，并更新提示模板等资源。Trainer 管理数据流、资源以及对推理引擎的更新。

可以通过 `pip install agentlightning` 轻松安装。该项目鼓励社区贡献，遵守 Microsoft 开源行为准则并需要贡献者许可协议。该项目采用 MIT 许可证授权，并已根据 Microsoft 负责任的 AI 标准进行合规性评估。

提到了几个示例项目，包括 DeepWerewolf 和 AgentFlow，展示了 Agent Lightning 在不同应用中的能力。该项目还包括指向已发表论文和博客文章的链接，详细介绍了其使用和功能。

---

## 34. 人工智能、维基百科与弱势语言未经校对的机器翻译

**原文标题**: AI, Wikipedia, and uncorrected machine translations of vulnerable languages

**原文链接**: [https://www.technologyreview.com/2025/09/25/1124005/ai-wikipedia-vulnerable-languages-doom-spiral/](https://www.technologyreview.com/2025/09/25/1124005/ai-wikipedia-vulnerable-languages-doom-spiral/)

本文探讨了未经校正的机器翻译对维基百科脆弱语言版本造成的有害影响。负责管理格陵兰语维基百科的肯尼斯·韦尔发现，大多数文章是由非母语者机器翻译的，错误百出，本质上是一个“海市蜃楼”。这个问题也蔓延到其他较小的语言版本，据估计，一些非洲语言的维基百科页面中有 40-60%的文章，以及超过三分之二的因纽特语页面也受到类似影响。

这个问题源于人工智能翻译模型从在线文本中学习，而维基百科通常是低资源语言的主要来源。这些维基百科页面上的错误随后污染了人工智能的训练数据，形成了一个恶性循环，即使用糟糕的翻译来生成更糟糕的翻译（“垃圾进，垃圾出”）。这可能会产生严重的后果，可能损害这些语言，因为未来的一代人会发现它们越来越不可靠。

虽然维基百科利用机器人进行基本维护，但人工智能的可访问性允许广泛、粗制滥造的贡献。“维基百科劫持者”，即使是那些怀有良好意图的人，也会使用人工智能翻译工具来创建他们不完全理解的内容，从而使脆弱语言版本充斥着错误。维基百科内置的翻译工具Content Translate 也饱受这些问题的困扰。

文章强调了负责任地使用人工智能的必要性以及精通这些语言的人工编辑的重要性。富拉语维基百科编辑阿卜杜勒卡迪尔·阿卜杜勒卡迪尔说明了现实世界的后果，他指出，不准确的机器翻译文章可能会损害依赖维基百科获取农业信息的农民。长期的担忧是，如果这种情况继续下去，可能会损害这些社区和他们的语言。

---

## 35. 展示HN：创建LLM – 60秒训练你自己的LLM

**原文标题**: Show HN: Create-LLM – Train your own LLM in 60 seconds

**原文链接**: [https://github.com/theaniketgiri/create-llm](https://github.com/theaniketgiri/create-llm)

`create-llm` 是一个 CLI 工具，旨在简化并加速定制语言模型 (LLM) 的训练过程。它类似于 `create-next-app`，但用于 LLM 训练，允许用户在几秒钟内创建可用于生产环境的项目。

**主要特性:**

*   **简化设置：** 为模型架构、数据预处理、分词器训练、检查点管理、评估和部署提供预构建的模板和基础设施。
*   **多种模板：** 提供四种模板（NANO、TINY、SMALL、BASE），满足不同的用例，从学习和快速实验到生产级和研究级模型。
*   **完整工具包：** 包括 PyTorch 训练基础设施、分词器训练（BPE、WordPiece、Unigram）、检查点管理、TensorBoard 集成、实时训练仪表板、交互式聊天界面、模型比较工具和部署脚本。
*   **智能默认值：** 采用智能配置，用于词汇表大小检测、序列长度处理、不匹配警告、过拟合检测、超参数建议和跨平台兼容性。
*   **插件系统：** 允许与 WandB、HuggingFace 和 SynthexAI 等工具集成。
*   **部署选项：** 支持部署到 Hugging Face Hub 和 Replicate。
*   **实时训练仪表板：** 提供对训练进度的实时监控。

该工具简化了整个 LLM 工作流程，从项目创建和数据准备到训练、评估和部署。它适用于各种技能水平和硬件配置，使 LLM 训练更易于访问。

---

## 36. 文本去像素化

**原文标题**: Text Depixelization

**原文链接**: [https://github.com/spipm/Depixelization_poc](https://github.com/spipm/Depixelization_poc)

Depix：一种从像素化截图中恢复文本的PoC工具

Depix 是一款“概念验证”(PoC) 工具，旨在从像素化截图中恢复纯文本，特别是那些使用线性盒状滤波器像素化的截图。它的工作原理是将目标图像中的像素化块与“搜索图像”（使用相同字体设置创建的 De Bruijn 序列的屏幕截图）进行比较。该算法识别匹配的块，并通过对周围匹配项的几何分析，重建原始文本。

本文概述了 Depix 的安装和使用方法，提供了使用不同软件（Greenshot 和 Gimp）像素化的图像的示例，并强调了匹配字体设置和颜色平均方法的重要性。 此外，还包含一些可选工具，用于可视化框检测和生成用于测试的像素化图像。

主要局限性包括假设像素级文本定位（亚像素渲染会影响准确性）、需要了解字体规格和屏幕设置，以及与经过额外压缩的图像不兼容。

未来的开发计划包括实现更多滤波器功能、创建模仿流行编辑器的平均滤波器，以及探索用于去像素化的隐马尔可夫模型 (HMM)。本文还参考了相关的研究和工具，包括 DepixHMM、UnRedacter 和一种基于 TensorFlow 的用于去像素化移动图像的解决方案，并认可了该领域的进展。

---

## 37. 任何像样的错误信息都是一种预兆。

**原文标题**: Any decent error message is a kind of oracle

**原文链接**: [https://digitalseams.com/blog/any-decent-error-message-is-a-kind-of-oracle](https://digitalseams.com/blog/any-decent-error-message-is-a-kind-of-oracle)

Bobbie Chen的文章《任何像样的错误信息都是一种预言》指出，看似无用或“可爱”的错误信息通常是经过深思熟虑的权衡设计的结果，尤其是在安全背景下。其核心思想是，错误信息所传达的任何信息，即使是看似微不足道的信息，也可能被恶意行为者利用，使其成为一种“预言”。

文章通过登录页面故意提供模糊错误信息（“用户名或密码不正确”）以防止账户枚举攻击等例子来说明这一点。它还解释了密码学中的填充预言攻击，即使是错误信息中细微的差异也可能被利用来解密被盗信息。

Chen主张理解即使是单个比特的信息也可能对攻击者有用。文章将此与小鸡性别鉴定、监督式机器学习和生成对抗网络（GAN）相提并论，以证明系统如何能够从“预言”中学习和利用信息来实现令人瞩目的成果。

作者强调了Jason Wei的“验证者规则”，即易于验证的任务将被自动化，从而突出了预言的力量。文章最后强调了“意义构建”的重要性，即对不同因素的相对价值做出主观决定的行为。在错误信息的背景下，这意味着在用户体验和安全问题之间取得平衡，权衡信息丰富的错误信息的价值与向攻击者提供有价值信息的风险。最终，Chen认为，理解错误信息的预言潜力对于设计安全且用户友好的系统至关重要。

---

## 38. 滚石抛光机使用说明

**原文标题**: Rock Tumbler Instructions

**原文链接**: [https://rocktumbler.com/tips/rock-tumbler-instructions/](https://rocktumbler.com/tips/rock-tumbler-instructions/)

本文提供了使用旋转式滚筒抛光机将粗糙的岩石转化为抛光石头的全面指南。它强调了三个“黄金法则”：“垃圾进，垃圾出”，突出了使用优质原石的重要性；“避免污染”，强调在每个滚磨步骤之间进行细致的清洁，以防止磨料污染；以及“好的结果需要时间”，建议在整个过程中保持耐心和彻底性。

本文建议使用莫氏硬度介于 6 和 7 之间，尺寸介于 3/8 英寸和 1 1/2 英寸之间的岩石。它列出了合适的材料，包括各种类型的玉髓、石英和常见的岩石类型。在滚磨之前，应检查岩石是否存在孔隙或裂缝，这些孔隙或裂缝可能导致污染。

本文的核心详细介绍了四步滚磨过程：
* **第一步（粗磨）：** 使用粗磨料打磨和磨平粗糙的边缘，大约需要七天时间。
* **第二步（中磨）：** 使用中等磨料进一步平滑岩石，再需要七天时间。 可以添加陶瓷介质以增加体积，尤其是在滚磨易碎材料时。
* **第三步（细磨/预抛光）：** 使用细磨料准备抛光岩石，使它们非常光滑。
* **第四步（抛光）：** 使用抛光剂进行最终抛光，从而产生闪亮的滚磨石。

每个步骤都需要彻底清洁岩石、滚筒和盖子，以防止磨料污染。 本文强调避免将用过的磨料和岩石泥冲入下水道，因为它会导致堵塞。 成功取决于耐心和对每个步骤的仔细执行。

---

## 39. WebDAV 尚未消亡

**原文标题**: WebDAV isn't dead yet

**原文链接**: [https://blog.feld.me/posts/2025/09/webdav-isnt-dead-yet/](https://blog.feld.me/posts/2025/09/webdav-isnt-dead-yet/)

本文提倡继续使用WebDAV作为个人项目和自托管场景中S3的可行替代方案。作者认为，S3已成为Web应用程序中文件存储的默认选择，这为只需要具有身份验证的基本文件存储的用户带来了不必要的复杂性。

作者概述了他们的核心需求：身份验证、写入文件、高效同步、确保文件默认情况下无法公开访问以及在需要时相对容易地进行公开访问。他们强调他们不需要诸如高级ACL、签名URL或分层存储之类的功能，这使得S3显得多余。他们批评像Minio这样的替代方案变得过于复杂。

文章随后展示了WebDAV通过各种工具（如MacOS Finder、Windows Explorer、rclone以及CyberDuck和Filezilla等流行应用程序）的广泛可用性和支持。作者指出，WebDAV已用于通过CardDAV和CalDAV同步联系人和日历。

作者分享了一个带有LDAP身份验证的特定Apache配置示例，演示了如何设置一个多用户WebDAV服务器，其中每个用户都被限制在自己的私有目录中。

最后，他们提到了他们使用WebDAV的几个应用程序，包括Joplin、Keepassium、VLC、Infuse和用于发布静态博客的rclone。他们还强调了一个新项目Altmount的潜力，该项目可以允许直接挂载和访问Usenet的内容。作者最后鼓励读者给WebDAV一个机会，强调其持续的相关性和实用性。

---

## 40. 密码与电钻

**原文标题**: Passwords and Power Drills

**原文链接**: [https://google.github.io/building-secure-and-reliable-systems/raw/ch01.html#on_passwords_and_power_drills](https://google.github.io/building-secure-and-reliable-systems/raw/ch01.html#on_passwords_and_power_drills)

密码与电钻：探讨系统设计中可靠性与安全性的关键交汇，并以谷歌的真实中断事件为例，说明一个可靠性问题（密码管理器因突发流量过载）如何因旨在保护系统的安全措施（硬件安全模块和保险箱组合）而加剧。

作者强调，虽然可靠性和安全性都关注保密性、完整性和可用性（CIA 三要素），但它们的方法不同。可靠性主要处理非恶意风险，如软件错误和硬件故障，而安全性则应对积极尝试利用漏洞的对抗性威胁。这种差异导致了不同的设计考虑，例如“故障安全”与“故障保护”行为。

文章进一步指出，可靠性和安全性都是需要在系统设计的初始阶段考虑的涌现特性。它们在正常运作时很大程度上是不可见的，因此容易被低估，直到发生故障。常见的考虑因素包括使用基于风险的方法进行评估、强调简单性、预测系统演变和复杂性的引入，以及构建处理意外情况的弹性。关键在于，忽视可靠性与安全性之间的相互作用可能会产生严重后果，凸显了整体系统设计和持续警惕的重要性。

---

## 41. 制作微型Linux发行版 (2023)

**原文标题**: Making a micro Linux distro (2023)

**原文链接**: [https://popovicu.com/posts/making-a-micro-linux-distro/](https://popovicu.com/posts/making-a-micro-linux-distro/)

本文指导初学者在RISC-V架构上从零开始构建一个最小的Linux发行版，重点在于理解底层概念。

文章首先解释了操作系统内核的作用：抽象硬件交互、管理资源以及提供编程模型以支持多个程序同时运行。Linux被介绍为一个流行的操作系统内核。

随后，文章将Linux发行版定义为Linux内核加上实际使用所需的用户空间基础设施，并将其与仅有内核的有限功能进行对比。这种“架构之上的架构”处理诸如网络管理之类的任务，并构建于内核的基本功能之上。

init进程被介绍为内核启动的第一个用户空间进程（PID 1）。然后，它充当所有其他用户进程的祖先，启动其他进程和工具，最终引导至一个交互式系统。

内核、init启动的进程和可用工具的组合构成了Linux发行版。作者警告说，由于不必要的软件积累，发行版中存在“臃肿”现象。文章将此与极简主义发行版（如Arch Linux）进行对比，后者赋予用户更大的控制权。

作者承诺将继续并指导读者实际构建一个非常基本的Linux发行版。

---

## 42. 我们与英国的联系不足，不足以适用《网络安全法案》。

**原文标题**: We do not have sufficient links to the UK for Online Safety Act to be applicable

**原文链接**: [https://libera.chat/news/advised](https://libera.chat/news/advised)

Libera.Chat 针对英国《在线安全法案》(OSA) 对其 IRC 网络潜在影响的说明。他们聘请了一家律师事务所，该事务所认为 Libera.Chat 可以辩称其与英国的联系不足，因此 OSA 不适用。理由是其英国用户群相对于英国的在线人口而言并不“显著”，英国并非其“目标市场”，并且他们不会给英国个人带来非典型的伤害风险。

Libera.Chat 强调其对用户隐私的承诺，并声明他们没有实施身份验证的计划。他们认为，考虑到他们已经禁止的内容，数据泄露暴露用户身份的潜在危害大于此类系统的好处。

虽然他们认为 OSA 不适用，但他们承认英国通信办公室 (Ofcom) 可能不同意。然而，他们认为采取强制措施的风险很低，因为 Ofcom 目前的重点是存在高风险 CSAM 的文件和图像托管服务。如果接到 Ofcom 的联系，他们准备与其进行建设性的沟通。

该文章强调了在线社区因应对 OSA 而屏蔽英国 IP 地址的危险，认为这不公平地剥夺了英国用户的服务。Libera.Chat 旨在通过了解 OSA 并辩称其不适用于他们来避免这种情况。他们还承认，未来的立法可能会迫使他们识别用户，但如果此类法案获得支持，他们将评估各种选择。他们鼓励公众继续反对在线过度干预。

---

## 43. Show HN: Chonky – 神经文本语义分块走向多语言

**原文标题**: Show HN: Chonky – a neural text semantic chunking goes multilingual

**原文链接**: [https://huggingface.co/mirth/chonky_mmbert_small_multilingual_1](https://huggingface.co/mirth/chonky_mmbert_small_multilingual_1)

此“Show HN”帖子介绍了Chonky，一种用于将文本智能分割成语义连贯块的多语言Transformer模型，适用于RAG（检索增强生成）系统。该模型`chonky_mmbert_small_multilingual_1`在长度为1024的序列上进行了微调。

该帖子演示了使用Chonky的两种方法。第一种利用名为`chonky`的自定义Python库，方便段落分割。第二种展示了使用标准的Hugging Face `transformers` pipeline，将该任务视为命名实体识别 (NER) 来识别“分隔符”token。

该模型在minipile、bookcorpus和Project Gutenberg等数据集上进行了训练。该帖子提供了基于token的F1分数，涵盖了Project Gutenberg的多种语言以及几个英文数据集。多语言性能各不相同，在俄语和法语等语言上得分特别高，而中文得分较低。该模型在单个H100 GPU上进行了微调。`chonky_mmbert_small_multilingual_1`的基础模型是`jhu-clsp/mmBERT-small`。

---

## 44. Show HN: Shadcn/UI 主题编辑器 – 设计和分享 Shadcn 主题

**原文标题**: Show HN: Shadcn/UI theme editor – Design and share Shadcn themes

**原文链接**: [https://shadcnthemer.com](https://shadcnthemer.com)

这个“Show HN”提交广告了一个 Shadcn/UI 主题编辑器。该工具允许用户发现现有 Shadcn/UI 主题并创建自己的主题。主要功能包括：

*   **主题发现：** 用户可以浏览可用的主题。
*   **主题创建：** 该工具支持创建新的 Shadcn/UI 主题。
*   **导入功能：** 用户可以导入现有主题。
*   **颜色过滤：** 过滤系统允许用户根据主导颜色（红、橙、黄、绿、青、蓝、紫、粉、灰、黑、白）查找主题。

提交内容似乎处于早期阶段，如“正在加载主题...”所示，这意味着主题库仍在填充或开发中。其主要目标是为用户提供一个平台，以便轻松设计和分享流行的 Shadcn/UI 组件库的自定义主题。

---

## 45. 世界模拟器：创建和体验互动式AI世界

**原文标题**: World Simulator: Create and Play Interactive AI Worlds

**原文链接**: [https://worldsimulator.ai/](https://worldsimulator.ai/)

本文介绍了一系列交互式AI世界模拟，这些模拟可以通过名为“世界模拟器”的平台访问。该平台提供了涵盖多种类型的场景，包括奇幻、日常、历史、冒险、搞笑、恐怖和动作。

每个模拟都有一个独特的标题、一个数字标识符、“点赞”数和大致的类型。描述突出了每个世界的核心叙事和玩家目标。例如：

*   **奇幻：** 探索一个神话般的驯兽师试炼，在森林中穿越一个魔法传送门，或者决定最后一位女巫的命运。
*   **日常：** 体验烧烤的混乱动态，或者开始一段公路旅行。
*   **历史：** 沉浸在古老的温达文，见证巴士底狱的陷落，或者调查通古斯事件。
*   **冒险：** 在一个基因怪物岛上生存，逃离一个禁忌岛屿，或者穿越一条被诅咒的时间线。
*   **搞笑：** 体验健身房的滑稽混乱，或者体验眼球的一天。
*   **动作：** 参与阿朱那和卡尔纳之间的战车决斗，或者加入对抗X的数字克隆体的战斗。

这些模拟提供了分支叙事和玩家选择，这些选择会影响故事的结果。本文展示了人工智能在各种背景和主题中创造引人入胜、个性化和互动体验的潜力。

---

## 46. 在你的服务器上设置陷阱机器人

**原文标题**: Trap Bots on Your Server

**原文链接**: [https://maurycyz.com/projects/trap_bots/](https://maurycyz.com/projects/trap_bots/)

本文详细介绍了如何利用基于马尔科夫链的“垃圾服务器”创建“爬虫陷阱”，以阻止机器人抓取合法的网站。该系统生成无意义的文本和链接，用垃圾内容填充爬虫的队列，并阻止其索引真实的站点。

该过程包括准备文本源，使用 Python 脚本 (`process.py`) 处理这些文本源以生成碎片化的文本文件 ("chainX.txt")，以及运行一个基于 C 语言的服务器 (`babble.c`) 来提供生成的垃圾内容。服务器配置为在特定路径下响应请求。

本文提供了 NGINX 配置，用于将流量路由到垃圾服务器并阻止已知的 AI 机器人用户代理。它还建议使用 `robots.txt` 来阻止合法的搜索引擎索引生成的内容。

作者声称该服务器资源消耗低，对性能的影响最小，但警告说与按请求收费的云服务相关的潜在成本。生成的文本基于马尔科夫链，创建看似合理但最终毫无意义的内容。通过在主网站上提供指向垃圾生成服务的链接，任何爬虫都将很快被大量无意义的内容淹没。

---

## 47. 我在代码审查中看到的工程师常犯的错误

**原文标题**: Mistakes I see engineers making in their code reviews

**原文链接**: [https://www.seangoedecke.com/good-code-reviews/](https://www.seangoedecke.com/good-code-reviews/)

本文探讨了工程师在代码审查过程中常犯的错误，尤其是在人工智能生成代码的时代。作者认为，有效的代码审查不仅仅是检查差异（所做的更改）。审查人员应考虑代码如何融入更广泛的代码库，关注一致性，并利用他们对系统的理解。

需要避免的关键错误包括：

*   **只关注差异：** 错失了识别现有解决方案或改进整体代码结构的机会。
*   **留下太多评论：** 削弱了重要反馈的影响；优先考虑高层次的问题，并指导作者保持风格一致。
*   **以“我会怎么写？”的过滤器进行审查：** 导致过多且通常是主观的评论，并阻碍进展。关注代码是否有效且可以接受。
*   **未能恰当使用阻止审查：** 导致对更改是否可以合并的模糊不清；对于重大问题，使用阻止审查。
*   **阻止太多审查：** 在健康的、以功能驱动的环境中，大多数审查应该是批准。过度阻止通常表明存在结构性问题或过度把关。

作者强调“倾向于批准”更改的重要性，除非存在严重问题，这与谷歌的代码审查指南相呼应。文章还承认，由于优先事项不同，存在不同的代码审查实践。

最后，作者指出，这些原则适用于审查人工智能生成的代码，但“倾向于批准”这一点除外，因为人工智能生成的代码应受到严格把关。

---

## 48. SELF (1989) 的高效实现 [pdf]

**原文标题**: An Efficient Implementation of SELF (1989) [pdf]

**原文链接**: [https://courses.cs.washington.edu/courses/cse501/15sp/papers/chambers.pdf](https://courses.cs.washington.edu/courses/cse501/15sp/papers/chambers.pdf)

该PDF似乎是与1989年发表的SELF编程语言的高效实现相关的部分或损坏文档。SELF是一种基于原型的面向对象编程语言，与基于类的语言不同。PDF内容主要由原始PDF代码组成，包括对象定义、交叉引用表和压缩数据流。

关键要素包括：

*   **标题：** "SELF的高效实现 (1989)" 表明侧重于使SELF语言有效运行的实际方面。
*   **PDF结构：** 内容显然被构造为一个PDF文档，具有标准的PDF对象，如目录、页面、字体和图像。
*   **压缩数据：** 内容的大部分包含在FlateDecode压缩流中，可能代表文档中的文本、图像或其他数据。
*   **图像对象：** 有对使用CCITTFaxDecode的图像对象的引用，表明文档的某些部分可能包含扫描的文本或图表。
*   **字体信息：** PDF包括Arial字体的字体描述符和编码信息，表明存在文本。

鉴于1989年的发表日期，该PDF似乎是一份较旧的文档。由于内容的性质，如果没有进一步分析压缩数据和完整文档，则无法深入研究SELF实现的细节。

---

## 49. Tarmageddon：远程代码执行漏洞凸显开源弃用软件的挑战

**原文标题**: Tarmageddon: RCE vulnerability highlights challenges of open source abandonware

**原文链接**: [https://edera.dev/stories/tarmageddon](https://edera.dev/stories/tarmageddon)

Edera博客文章详细介绍了在`async-tar` Rust库及其分支（包括流行的`tokio-tar`）中发现的一个严重远程代码执行(RCE)漏洞，名为TARmageddon(CVE-2025-62518)。该漏洞源于嵌套TAR存档中PAX和ustar标头处理不一致，允许攻击者将恶意文件“走私”到提取目录中，从而导致文件覆盖攻击。

该文章强调了修补废弃开源项目的挑战。`tokio-tar`是一个高下载量的分支，但无人维护，迫使Edera协调多个分支的去中心化披露。他们为受影响的库创建了补丁，并主动联系了uv、testcontainers和opa-wasm等主要下游项目，以确保快速升级。

该漏洞可在多种场景中被利用，包括Python构建后端劫持、容器镜像污染和BOM/清单绕过。补丁优先处理PAX标头，验证标头一致性，并实施严格的边界检查。

该文章强调，Rust虽然增强了内存安全，但并没有消除像这种解析缺陷这样的逻辑错误。它强调了深度防御和强大的安全边界的重要性。Edera提供了补丁，并建议用户升级到已修补的版本或迁移到积极维护的分支。文章最后附上了披露过程的时间表，并感谢合作的研究人员和维护人员。

---

## 50. 你应该喂养机器人

**原文标题**: You Should Feed the Bots

**原文链接**: [https://maurycyz.com/misc/the_cost_of_trash/](https://maurycyz.com/misc/the_cost_of_trash/)

作者详细描述了他们与恶意爬虫的斗争，这些爬虫很可能为了AI训练而抓取数据，并使他们的服务器不堪重负。由于这些爬虫的庞大资源和适应性，传统的IP封锁、速率限制和robots.txt等方法都无效。付费墙和验证码对用户体验不利，而gzip炸弹也被证明效果不佳。

作者意识到，最廉价有效的解决方案是向爬虫提供动态生成的垃圾内容。由于SSD访问时间、图片占用的带宽以及爬虫请求冷僻页面等原因，即使使用缓存，提供静态内容仍然成本高昂。关键的见解是，与磁盘I/O和带宽相比，CPU和RAM相对便宜。

通过使用轻量级优化的马尔可夫胡言乱语生成器，作者以最小的CPU使用率（每次请求约60微秒）和内存占用（约1.2 MB）生成无意义的内容。这使得爬虫能够访问网站，保持它们的满足感，并防止它们变得更具攻击性。该系统还避免了黑名单和规则的维护开销，因为爬虫会自动消耗生成的垃圾。

---

## 51. Jacqueline – 一个用 Pascal 编写的极简 i386 内核 (2019)

**原文标题**: Jacqueline – A minimal i386 kernel written in Pascal (2019)

**原文链接**: [https://github.com/danirod/jacqueline](https://github.com/danirod/jacqueline)

Jacqueline 是一个用 Pascal (使用 Free Pascal 方言) 编写的实验性 i386 引导加载程序。作者将其作为个人挑战而创建，并且在初始编译和成功模拟后，不打算进一步开发。

文章重点介绍了作者选择 Pascal 的原因，强调尽管 Pascal 并非为底层编程而设计，但 Free Pascal 提供了指针、内存地址访问和内联汇编接口等功能，使其适用于系统编程。 这些功能可与 C、C++ 和 Rust 等语言中的功能相媲美。作者甚至更喜欢 Free Pascal 的汇编接口。

作者还指出，Free Pascal 能够生成 PE 和 ELF 格式的标准目标文件，从而可以与使用其他语言（如 C 或汇编）编写的代码进行互操作。

要设置和运行 Jacqueline，文章列出了以下

---

## 52. iOS 26更新移除了飞马和掠食者间谍软件的关键IOC

**原文标题**: Key IOCs for Pegasus and Predator Spyware Removed with iOS 26 Update

**原文链接**: [https://iverify.io/blog/key-iocs-for-pegasus-and-predator-spyware-cleaned-with-ios-26-update](https://iverify.io/blog/key-iocs-for-pegasus-and-predator-spyware-cleaned-with-ios-26-update)

本文探讨了 iOS 26 更新对检测 Pegasus 和 Predator 间谍软件的影响。分析 `shutdown.log` 文件以查找这些间谍软件痕迹的关键检测方法已失效。此前，位于系统诊断中的 `shutdown.log` 文件提供了宝贵的取证证据。特别是 Pegasus，留下了可识别的痕迹，这些痕迹从明显的条目演变为完全擦除日志。`shutdown.log` 中缺少预期条目本身就成了一个警示信号。2023 年活跃的 Predator 间谍软件可能采用了类似的策略。

iOS 26 引入了一项更改，即每次重启时 `shutdown.log` 都会被覆盖，而不是附加。此操作有效地擦除了过去感染的关键证据，阻碍了取证调查。虽然此更改可能旨在进行系统维护，但它在攻击日益增多的时期，无意中掩盖了复杂的威胁。

本文重点介绍了一个针对 Pegasus 2022 年感染的特定 IOC（运行 iOS 26 之前版本的设备）：在 `shutdown.log` 中存在 `/private/var/db/com.apple.xpc.roleaccountd.staging/com.apple.WebKit.Networking` 条目。对于运行 iOS 18 或更早版本的设备，将 `containermanagerd` 日志与 `shutdown.log` 事件相关联也有助于识别差异。

本文建议用户在更新到 iOS 26 *之前*对设备进行系统诊断，以保留 `shutdown.log` 数据，并考虑暂缓更新，直到 Apple 解决此问题。

---

## 53. 立方四边形天线与玛格丽特的信

**原文标题**: Cubical Quad Antennas and Margaret's Letter

**原文链接**: [http://ei3lh.eu/?p=88](http://ei3lh.eu/?p=88)

本文讲述了作者 (EI3LH) 在一本二手《关于方框天线的一切》中令人愉悦的发现。里面夹着一个信封，上面写着“玛格丽特的信”，收信人是 F. Beamond 先生，但信件本身已经丢失。此外，还有一张发黄的纸条，上面写着调频广播频率，以及一张手绘的威斯敏斯特桥站地图。

作者开始了一项历史微观调查，从信封上的线索入手。一张十进制化前的邮票，一张 4 便士的伊丽莎白二世 Machin 邮票（1967 年），表明这封信是在 1971 年之前寄出的。一个宣传什鲁斯伯里音乐和花卉节的邮戳有助于将信件的日期精确到 1968 年 1 月至 8 月之间。作者发现，该节是一个重要的年度活动，有着热气球表演的历史。

进一步的研究表明，什罗普郡直到 1959 年才拥有邮政编码，这又增加了一条线索。作者探索了 Universal Book Co.（该书的零售商）的历史，以及它在“摇摆的六十年代”位于伦敦苏荷区的地理位置。

调查发现，威斯敏斯特桥站曾经是墓地铁路，用于运送死者。最后，在什罗普郡找到三个关于 F. Beamond 的条目后，作者发现了一篇关于来自 Bishop's Castle 的 Frank Beamond 的文章，他是一位活到 92 岁的农民。作者推测这本书来自一位已故的无线电爱好者，并因这个小小的谜团而感到充实，学到的东西远不止关于天线的知识。

---

## 54. 纪念圣诞岛鼩

**原文标题**: In memory of the Christmas Island shrew

**原文链接**: [https://news.mongabay.com/2025/10/in-memory-of-the-christmas-island-shrew/](https://news.mongabay.com/2025/10/in-memory-of-the-christmas-island-shrew/)

这篇文章哀悼了圣诞岛鼩(Crocidura trichura)的灭绝，这是一种曾经在印度洋圣诞岛上数量众多的微小哺乳动物。这种鼩鼱可能起源于爪哇，在19世纪末“极其常见”，但由于黑鼠的引入及其携带的寄生虫，导致该岛本土哺乳动物种群遭受重创，数量迅速下降。该鼩鼱在1908年被推定灭绝，但在1958年和1984年曾短暂被重新发现，其中一只雌性被圈养了一年多。然而，将其与捕获的雄性繁殖的努力失败了，尽管进行了广泛的搜寻，但此后一直没有发现鼩鼱。

官方宣布的灭绝事件增加了澳大利亚在哺乳动物灭绝方面的不幸记录，突显了入侵物种和人类活动对脆弱生态系统的破坏性影响。文章强调了该鼩鼱的韧性，它在人们看不到的情况下生存了几十年，并质疑有多少其他物种正在默默消失。尽管仍有一线希望该鼩鼱可能仍然存在，但作者承认，安静的森林证明了它可能的消亡，这种损失在很大程度上没有引起人们的注意，除了那些重视它存在的人。文章澄清说，虽然圣诞岛在地理和生态上与东南亚一致，但其与澳大利亚的政治联系导致该国的灭绝记录。

---

## 55. Show HN: LLM Rescuer – 修复 Ruby 中价值数十亿美元的错误

**原文标题**: Show HN: LLM Rescuer – Fixing the billion dollar mistake in Ruby

**原文链接**: [https://github.com/barodeur/llm_rescuer](https://github.com/barodeur/llm_rescuer)

LLM Rescuer：一个用AI猜测来解决空指针问题的搞笑Ruby Gem

LLM Rescuer 是一款极其不切实际的 Ruby gem，旨在通过使用 AI 猜测代码在遇到 `nil` 对象上的 `NoMethodError` 时*应该*做什么，从而“修复”空引用问题（Tony Hoare 称之为“价值十亿美元的错误”）。

该 gem 对 `NilClass` 进行 monkey-patch，利用 LLM (据推测是 GPT) 分析周围的代码上下文，并“幻构”出一个合理的响应，从而使程序即使在遇到不应出现的 `nil` 值时也能继续运行。

文章强调了该项目的实验性和高度不可靠性，并明确警告不要在生产环境中使用。它强调了不可预测且可能造成灾难性后果的可能性，例如用户的姓名被替换为无意义的字符串或购物车行为异常。

作者幽默地详细说明了使用该 gem 的成本影响，估计 OpenAI API 会产生巨额费用，并开玩笑地暗示在高流量期间可能会牺牲“长子”。

虽然列出了诸如 `ruby_llm` 和 `binding_of_caller` 之类的依赖项，但核心要求是“幽默感”。这篇文章以一种半开玩笑的方式探讨了使用 AI 来掩盖底层代码问题（而不是直接解决它们）的荒谬性。 最终，LLM Rescuer 是一篇讽刺性的评论，旨在讽刺 AI 炒作以及盲目应用先进技术来解决基本编程问题的危险。

---

## 56. 广义 K 均值聚类

**原文标题**: Generalized K-Means Clustering

**原文链接**: [https://github.com/derrickburns/generalized-kmeans-clustering](https://github.com/derrickburns/generalized-kmeans-clustering)

广义K-Means聚类是一个基于Spark的项目，它扩展了传统的K-Means算法，以支持多种Bregman散度和高级变体，如二分K-Means、X-Means、软/模糊K-Means、流式K-Means、K-Medians和K-Medoids。它提供推荐的DataFrame/ML API以及为向后兼容而保留的传统RDD API。

DataFrame API与Spark ML集成，是新项目的首选。它支持诸如平方欧几里得距离、KL散度、Itakura–Saito距离、L1/曼哈顿距离、广义-I距离和Logistic损失等散度。主要特性包括模型持久性、全面的测试、可执行的文档、确定性行为和持续的CI验证。

该项目强调可扩展性，并提供基于所选散度来管理分配策略的工具。对于平方欧几里得距离，它使用优化的表达式/codegen路径。对于一般Bregman散度，它采用广播+ UDF路径，提供通过分块处理来处理大型集群配置的选项，以避免内存不足错误。

该库包括自动验证输入数据，以确保其满足特定散度的领域要求，并提供可操作的错误消息和转换选项以进行更正。它还为PySpark用户提供了一个Python封装器。

该项目维护一个全面的CI流水线，以确保代码质量、跨版本兼容性和性能健全。传统RDD API仍然可用，但新开发应优先考虑DataFrame API。

---

## 57. 使用BeaconDB测试BLE信标

**原文标题**: Testing out BLE beacons with BeaconDB

**原文链接**: [https://blog.matthewbrunelle.com/testing-out-ble-beacons-with-beacondb/](https://blog.matthewbrunelle.com/testing-out-ble-beacons-with-beacondb/)

本文详细介绍了作者对beaconDB的探索，该项目延续了Mozilla Location Service的工作，利用对蜂窝塔、BLE信标和WiFi接入点的观测结果来提供位置查找服务。作者使用GrapheneOS（支持基于网络的定位），希望向beaconDB贡献BLE信标观测数据。

作者概述了一个计划，购买BLE信标，记录其MAC地址，验证它们未与任何位置关联，将它们部署在院子里，然后使用NeoStumbler在遛狗时记录观测数据。他们深入研究了BLE信标的原理，区分了它们与标准蓝牙的区别，并讨论了iBeacon、URIBeacon/Eddystone和AltBeacon标准。他们选择了Feasy FSC-BP104D信标，并对其进行了配置以进行测试。

作者尝试了beaconDB的geolocate API，成功地使用WiFi接入点检索了位置数据。然而，当尝试使用BLE信标数据时，他们遇到了问题，收到了404错误。尽管禁用了NeoStumbler中的移动设备过滤器，并直接通过geosubmit API提交了观测数据，但这些信标的位置仍然无法解析。

最终，通过检查beaconDB的源代码，作者发现该项目目前接受并存储BLE信标数据，但尚未将其用于地理定位。文章最后总结说，在进行大量的设置和测试之前，应该先检查核心功能，同时也强调了作者获得的关于BLE信标的知识。

---

## 58. Google Pixel 最危险的漏洞：无法拨打911

**原文标题**: Google Pixel's most dangerous bug: failing to call 911

**原文链接**: [https://www.androidpolice.com/google-pixels-most-dangerous-bug-refuses-to-die/](https://www.androidpolice.com/google-pixels-most-dangerous-bug-refuses-to-die/)

这篇文章重点指出一个影响谷歌Pixel手机的、反复出现且危险的漏洞，具体表现为无法成功拨打911。来自Pixel 9和10用户的报告再次浮出水面，特别是在美国主要的网络运营商（如AT&T）上，用户在拨打紧急服务电话时遇到呼叫失败。一位Pixel 8用户报告说，即使移动网络信号良好，也需要启用Wi-Fi通话才能完成911呼叫，这强调了问题并非一般的网络中断。

文章强调这并非孤立事件。多年来，类似问题一直困扰着Pixel手机，使其与iPhone和三星设备区分开来，后两者更为常见，但问题却没有那么多。甚至加拿大运营商贝尔公司也发布了关于Pixel 6-10手机出现此问题的警报（尽管后来已解决）。作者认为，美国运营商本应发布类似的警告。

鉴于其生死攸关的影响，作者强烈批评谷歌未能永久解决此漏洞。文章呼吁谷歌优先与运营商合作，修复问题的根本原因，并强调可靠的紧急呼叫是任何智能手机的基本要求。

---

## 59. 2025年 React 与 Backbone 对比

**原文标题**: React vs. Backbone in 2025

**原文链接**: [https://backbonenotbad.hyperclay.com/](https://backbonenotbad.hyperclay.com/)

文章《2025年React与Backbone之争》认为，尽管经过多年的发展和庞大的生态系统，React并没有像人们期望的那样，在根本上比像Backbone这样的旧框架更好地改进前端开发。虽然React乍一看更简洁易读，但这种简洁是以显著的抽象复杂性为代价的。

作者认为，Backbone虽然冗长，但在操作上更透明——直接的事件处理和DOM操作。相反，React隐藏了实现细节，导致意外行为和调试困难，需要深入了解其内部机制，例如协调算法和渲染阶段。作者强调了常见的React特定问题，如`useEffect`中的无限循环、过时闭包和状态管理复杂性。

文章质疑React的复杂性对于大多数应用，特别是较小的应用是否合理。它认为，虽然React对于大型应用可能是必要的，但其抽象为简单的项目带来了不必要的开销并阻碍了理解。作者最后提出了一个问题，是否存在一个更好的模型：一种结合了DOM的稳定性、直观的编码实践以及类似Backbone和jQuery的可 hack 性，使开发人员能够轻松理解和修改底层机制的模型。

---

## 60. 拉尔夫·布朗文档集（x86中断列表）

**原文标题**: Ralf Brown's Files (The x86 Interrupt List)

**原文链接**: [http://www.cs.cmu.edu/~ralf/files.html](http://www.cs.cmu.edu/~ralf/files.html)

Ralf Brown的文件，托管于FTP.CS.CMU.EDU，主要包含全面的“x86中断列表”(RBIL)，这是一个关于IBM PC及其兼容机的中断调用、I/O端口、内存地址和其他底层细节的大型信息集合。对于使用x86架构和MS-DOS的程序员和系统开发者来说，这个资源非常宝贵。该站点提供可供下载的多个部分的中断列表，以及相关的实用程序和常见问题解答。

除了中断列表之外，该站点还托管了Ralf Brown开发的几个开源项目，包括CMU-EBMT（一个基于实例的机器翻译系统）、ZipRec（一个ZIP存档恢复工具）、LA-Strings（一个语言感知字符串工具）、CanvasLMS.py（一个用于Canvas LMS的Python库）和WordClus（一个词语聚类程序）。

此外，该页面还提供了各种编程库的链接，如SPAWNO（一个用于spawn函数的交换替代品）、AMISLIB（用于创建自高加载TSR）、以及DV-GLUE（用于DESQview API访问）。它还提供应用程序，如RBcomm（一个终端程序）、RBPCI（一个PCI设备信息工具）、DVdevload（一个DESQview的设备驱动程序加载器）、DVPTAME（一个DESQview键盘轮询限制器）、RBdualVGA（用于双VGA配置）、RBkeyswap（CapsLock/Ctrl交换）和RBspeed（Intel芯片组速度控制）。该站点还链接到贡献文件，如RBILVIEW和中断列表的HTML转换版本。

---

## 61. 解锁英国航空免费WiFi

**原文标题**: Unlocking free WiFi on British Airways

**原文链接**: [https://www.saxrag.com/tech/reversing/2025/06/01/BAWiFi.html](https://www.saxrag.com/tech/reversing/2025/06/01/BAWiFi.html)

本文详细介绍了作者对英国航空免费“消息”WiFi的探索，以及如何规避其限制以访问完整互联网。作者发现，英航通过将特定域名加入白名单，使用服务器名称指示（SNI）过滤来判断连接是否与消息应用程序（WhatsApp、Signal、微信）相关。与不在白名单上的域名的连接会被重置。

为了绕过这个限制，作者在VPS上设置了一个HTTPS代理，使用`stunnel`建立与自签名证书的TLS连接。`stunnel`服务器配置为接受任何SNI。客户端通过hosts文件将`wa.me`（一个WhatsApp域名）解析为VPS的IP，从而欺骗英航认为连接是到WhatsApp的。然后，HTTP代理允许浏览其他网站。作者在飞行中成功测试了这一点，浏览了Hacker News。

作者还探索了加密客户端Hello（ECH），它可以加密SNI，从而使其更难被过滤。通过将其测试ECH网站配置为使用`wa.me`作为公共SNI，他们能够在没有英航过滤的情况下浏览其真实的网站。

作者最后指出，SNI不应被盲目信任，因为客户端可以很容易地伪造它。

---

## 62. 适用于安卓的Swift SDK

**原文标题**: The Swift SDK for Android

**原文链接**: [https://www.swift.org/blog/nightly-swift-sdk-for-android/](https://www.swift.org/blog/nightly-swift-sdk-for-android/)

文章宣布了Swift SDK for Android的每夜预览版发布，标志着将Swift开发引入Android平台的重要一步。这一成就归功于Android工作组和更广泛的社区的共同努力，为开发者提供了跨平台开发的新可能性。

Swift SDK for Android可通过Windows安装程序获得，也可单独用于Linux和macOS。文章提供了“入门指南”和示例的链接，以帮助开发者开始在Android上构建原生Swift应用程序。文章还强调了软件包兼容性的进展，Swift Package Index中已有超过25%的软件包可以为Android构建。

swift-java项目被介绍为Java和Swift之间实现无缝互操作的关键工具，允许开发者使用自动生成的绑定在两个方向上集成这两种语言。文章引用了Mads Odgaard的Swift服务端聚会演讲，其中包含有关生成绑定以将业务逻辑集成到Android应用程序中的信息。

作者鼓励开发者在Swift论坛上分享他们的经验和想法，并宣布Android工作组正在起草一份愿景文件，以指导未来的开发工作。项目看板跟踪主要工作的进展情况，并且Swift SDK for Android提供官方CI。文章最后邀请大家加入社区，为不断壮大的Swift on Android生态系统做出贡献。

---

## 63. ARM内存标签：如何提升C/C++内存安全 (2018) [pdf]

**原文标题**: ARM Memory Tagging: how it improves C/C++ memory safety (2018) [pdf]

**原文链接**: [https://llvm.org/devmtg/2018-10/slides/Serebryany-Stepanov-Tsyrklevich-Memory-Tagging-Slides-LLVM-2018.pdf](https://llvm.org/devmtg/2018-10/slides/Serebryany-Stepanov-Tsyrklevich-Memory-Tagging-Slides-LLVM-2018.pdf)

这份2018年的PDF文档探讨了ARM内存标签技术，该技术旨在提高C/C++代码中的内存安全性。虽然该文档本身是一个技术PDF文件，但标题表明了它的目的。内存标签是一种基于硬件的安全机制，它将元数据（标签）与内存位置相关联。这使得处理器能够检测并防止诸如缓冲区溢出、释放后使用错误以及其他困扰C/C++应用程序的常见漏洞等内存安全违规行为。其总体概念是确保内存仅以符合其预期用途的方式被访问。

在无法访问完整内容的情况下，根据标题，该文档可能详细阐述了：

*   **问题：** 解释C/C++中内存安全面临的挑战，从而导致漏洞。
*   **解决方案：** 描述ARM内存标签技术的工作原理（例如，如何分配、检查和使用标签）。
*   **好处：** 强调使用内存标签的优势，例如减少攻击面、提高可靠性和简化调试。
*   **ARMv8.5-A架构：** 在链接的URI中提到，这表明ARM内存标签功能是在此架构中实现的。

由于提供的PDF内容是二进制数据，因此无法对技术细节进行完整的总结。但是，标题和链接的ARM社区博客文章表明，该文档提供了有关ARM内存标签技术及其提供的安全优势的技术信息。

---

## 64. NewPipe迎来十周年

**原文标题**: NewPipe Is Turning 10

**原文链接**: [https://newpipe.net/blog/pinned/announcement/newpipe-turns-10/](https://newpipe.net/blog/pinned/announcement/newpipe-turns-10/)

NewPipe开源YouTube客户端迎来十周年。该项目已从单个开发者发展成拥有数百万用户的大型社区，现在由NewPipe e.V.协会支持。

文章回顾了过去五年，重点介绍了协会的成立以及应用程序正在进行的大规模重构/重写，包括新的提取器设计和播放器（NewPlayer）。该协会现在聘用了开发者（@Profpatsch 和 Schabi）以确保持续的开发和稳定性。

该项目目前专注于重写应用程序，团队欢迎新的贡献者。文章展望了未来，既充满希望又面临挑战。积极的一面是，重构旨在带来现代化的代码库（Kotlin、Compose）和新功能。他们还渴望与内容创作者就YouTube之外的替代变现策略进行对话。

挑战包括需要持续维护的陈旧代码库，需要在项目工作与研究生职业之间取得平衡，以及谷歌构成的持续威胁，谷歌试图限制第三方YouTube客户端。特别是，谷歌试图限制像F-Droid这样的替代应用商店是一个主要问题。

尽管存在这些障碍，NewPipe团队仍然坚定不移，并积极寻求解决方案。文章以乐观的视角结尾，强调了为应对这些挑战和继续改进NewPipe所做的持续努力。他们鼓励社区参与，以克服障碍并保持项目的势头。

---

## 65. 亚马逊筹划如何保守其数据中心用水量的秘密

**原文标题**: Amazon strategised about keeping its datacentres' full water use secret

**原文链接**: [https://www.theguardian.com/technology/2025/oct/25/amazon-datacentres-water-use-disclosure](https://www.theguardian.com/technology/2025/oct/25/amazon-datacentres-water-use-disclosure)

一份泄露的内部文件显示，亚马逊曾策划掩盖其数据中心用水的真实规模，特别是关于“二次使用”——用于发电以供应设施的水。 尽管微软和谷歌等竞争对手披露了用水量数据，但亚马逊历来对此信息保密。

该文件表明，亚马逊的云计算部门 AWS 选择仅计算主要用水（直接用于冷却的水），以避免在启动其“水资源正效益”可持续发展活动时造成声誉损害。高管们担心，完全透明会导致被指控掩盖真相和负面头条新闻。该公司旨在削减其主要用水量，但避免解决更大的二次用水问题。

专家批评了这种选择性披露，认为将主要用水和二次用水都纳入考量是进行准确环境评估的标准做法。文章还强调，亚马逊正在水资源短缺地区建设数据中心。

一位前亚马逊水资源可持续发展经理声称，该公司正在通过资助创建低估流域恢复项目影响的方法来“混淆”其用水足迹。亚马逊还决定对其“间接”用水足迹（其供应链中使用的水，例如农业）保密，因为它构成了其总用水足迹的最大部分。 亚马逊为其做法辩护，称泄露的文件已过时，并表示其用水报告基于第三方保证的数据。

---

## 66. 你CS教育缺失的一学期 (2020)

**原文标题**: The Missing Semester of Your CS Education (2020)

**原文链接**: [https://missing.csail.mit.edu/](https://missing.csail.mit.edu/)

你CS教育中缺失的一学期：本课程旨在为计算机科学专业的学生提供实用的技能，并熟练掌握传统课程中经常被忽视的基本工具。课程重点在于掌握命令行、文本编辑器（Vim）、版本控制（Git）和其他工具，以提高效率和解决问题的能力。它认为，花时间学习这些贯穿整个CS教育和职业生涯的工具，可以显著提高生产力，并使学生能够更有效地应对复杂的挑战。

该课程涵盖shell脚本、数据整理、命令行环境配置、调试、性能分析、元编程、安全和密码学等主题。它由Anish、Jon和Jose教授，并且在麻省理工学院之外也可用，为外部讨论和翻译提供资源。讲座的视频录像可在YouTube上找到。该课程已被翻译成多种语言，例如中文、日语、韩语等等。该课程感谢麻省理工学院各个个人和部门的支持。

---

## 67. Windows 自动深色模式

**原文标题**: Auto Dark Mode for Windows

**原文链接**: [https://github.com/AutoDarkMode/Windows-Auto-Night-Mode](https://github.com/AutoDarkMode/Windows-Auto-Night-Mode)

自动暗黑模式是一款Windows应用程序，旨在根据时间表、日出/日落时间或其他触发器自动切换浅色和深色主题。它模仿了Android、iOS和MacOS上的功能，并将其带到Windows 10和11上。

主要功能包括：基于日出/日落的主题切换，可自定义的延迟，桌面壁纸切换，鼠标光标和强调色切换，任务栏和标题栏强调色控制，触摸键盘主题切换，支持Windows .theme文件，键盘快捷键，灰度滤镜启用，游戏模式（暂停游戏期间的切换），省电功能（如在电池供电时启用深色模式），自定义脚本执行和自动更新。

该应用程序轻巧，易于卸载，并且不需要管理员权限。用户可以从Microsoft Store、GitHub、WinGet、Chocolatey、Scoop下载它，或者下载便携版本。使用提供的.exe文件可以轻松安装。该项目使用Weblate进行翻译，用户也可以手动编辑翻译文件。维基提供了更多信息和故障排除。

---

## 68. Honda's ASIMO (2021)

**原文标题**: Honda's ASIMO (2021)

**原文链接**: [https://www.robotsgottalents.com/post/asimo](https://www.robotsgottalents.com/post/asimo)

生成摘要时出错

---

## 69. Why formalize mathematics – more than catching errors

**原文标题**: Why formalize mathematics – more than catching errors

**原文链接**: [https://rkirov.github.io/posts/why_lean/](https://rkirov.github.io/posts/why_lean/)

生成摘要时出错

---

## 70. Living Dangerously with Claude

**原文标题**: Living Dangerously with Claude

**原文链接**: [https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/](https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/)

生成摘要时出错

---

## 71. 3-way FTP: Pushing files around with silly and unusual methods

**原文标题**: 3-way FTP: Pushing files around with silly and unusual methods

**原文链接**: [http://rachelbythebay.com/w/2020/02/18/ftp/](http://rachelbythebay.com/w/2020/02/18/ftp/)

生成摘要时出错

---

## 72. The future of Python web services looks GIL-free

**原文标题**: The future of Python web services looks GIL-free

**原文链接**: [https://blog.baro.dev/p/the-future-of-python-web-services-looks-gil-free](https://blog.baro.dev/p/the-future-of-python-web-services-looks-gil-free)

生成摘要时出错

---

## 73. Why your social.org files can have millions of lines without performance issues

**原文标题**: Why your social.org files can have millions of lines without performance issues

**原文链接**: [https://en.andros.dev/blog/4e12225f/why-your-socialorg-files-can-have-millions-of-lines-without-any-performance-issues/](https://en.andros.dev/blog/4e12225f/why-your-socialorg-files-can-have-millions-of-lines-without-any-performance-issues/)

生成摘要时出错

---

## 74. Pico Banana: Large-Scale Dataset for Image Editing by Apple

**原文标题**: Pico Banana: Large-Scale Dataset for Image Editing by Apple

**原文链接**: [https://arxiv.org/abs/2510.19808](https://arxiv.org/abs/2510.19808)

生成摘要时出错

---

## 75. The Great SaaS Gaslight

**原文标题**: The Great SaaS Gaslight

**原文链接**: [https://unworkableideas.com/the-great-saas-lighting-how-it-users-got-gaslit/](https://unworkableideas.com/the-great-saas-lighting-how-it-users-got-gaslit/)

生成摘要时出错

---

## 76. ProEnergy repurposes jet engines to power data centers

**原文标题**: ProEnergy repurposes jet engines to power data centers

**原文链接**: [https://www.datacenterdynamics.com/en/news/proenergy-offers-repurposed-jet-engines-to-data-cent/](https://www.datacenterdynamics.com/en/news/proenergy-offers-repurposed-jet-engines-to-data-cent/)

生成摘要时出错

---

## 77. People with blindness can read again after retinal implant and special glasses

**原文标题**: People with blindness can read again after retinal implant and special glasses

**原文链接**: [https://www.nbcnews.com/health/health-news/tiny-eye-implant-special-glasses-legally-blind-patients-can-read-rcna238488](https://www.nbcnews.com/health/health-news/tiny-eye-implant-special-glasses-legally-blind-patients-can-read-rcna238488)

生成摘要时出错

---

## 78. Real Estate Is Entering Its AI Slop Era

**原文标题**: Real Estate Is Entering Its AI Slop Era

**原文链接**: [https://www.wired.com/story/real-estate-is-entering-its-ai-slop-era/](https://www.wired.com/story/real-estate-is-entering-its-ai-slop-era/)

生成摘要时出错

---

## 79. Mesh2Motion – Open-source web application to animate 3D models

**原文标题**: Mesh2Motion – Open-source web application to animate 3D models

**原文链接**: [https://mesh2motion.org/](https://mesh2motion.org/)

生成摘要时出错

---

## 80. "Learn APL" Notes

**原文标题**: "Learn APL" Notes

**原文链接**: [https://luksamuk.codes/pages/learn-apl.html](https://luksamuk.codes/pages/learn-apl.html)

生成摘要时出错

---

## 81. What If Tariffs?

**原文标题**: What If Tariffs?

**原文链接**: [https://www.swatch.com/en-en/what-if-tariffs-so34z106/SO34Z106.html](https://www.swatch.com/en-en/what-if-tariffs-so34z106/SO34Z106.html)

生成摘要时出错

---

## 82. Diamond Thermal Conductivity: A New Era in Chip Cooling

**原文标题**: Diamond Thermal Conductivity: A New Era in Chip Cooling

**原文链接**: [https://spectrum.ieee.org/diamond-thermal-conductivity](https://spectrum.ieee.org/diamond-thermal-conductivity)

生成摘要时出错

---

## 83. Belittled Magazine: Thirty years after the Sokal affair

**原文标题**: Belittled Magazine: Thirty years after the Sokal affair

**原文链接**: [https://thebaffler.com/salvos/belittled-magazine-robbins](https://thebaffler.com/salvos/belittled-magazine-robbins)

生成摘要时出错

---

## 84. Scientists Discover New Path to Room-Temperature Superconductors

**原文标题**: Scientists Discover New Path to Room-Temperature Superconductors

**原文链接**: [https://scitechdaily.com/the-holy-grail-of-physics-scientists-discover-new-path-to-room-temperature-superconductors/](https://scitechdaily.com/the-holy-grail-of-physics-scientists-discover-new-path-to-room-temperature-superconductors/)

生成摘要时出错

---

## 85. How to make a Smith chart

**原文标题**: How to make a Smith chart

**原文链接**: [https://www.johndcook.com/blog/2025/10/23/smith-chart/](https://www.johndcook.com/blog/2025/10/23/smith-chart/)

生成摘要时出错

---

## 86. Load-time relocation of shared libraries (2011)

**原文标题**: Load-time relocation of shared libraries (2011)

**原文链接**: [https://eli.thegreenplace.net/2011/08/25/load-time-relocation-of-shared-libraries/](https://eli.thegreenplace.net/2011/08/25/load-time-relocation-of-shared-libraries/)

生成摘要时出错

---

## 87. Acwj: A Compiler Writing Journey

**原文标题**: Acwj: A Compiler Writing Journey

**原文链接**: [https://github.com/DoctorWkt/acwj](https://github.com/DoctorWkt/acwj)

生成摘要时出错

---

## 88. Debian Technical Committee overrides systemd change

**原文标题**: Debian Technical Committee overrides systemd change

**原文链接**: [https://lwn.net/Articles/1041316/](https://lwn.net/Articles/1041316/)

生成摘要时出错

---

## 89. The geometry of mathematical methods

**原文标题**: The geometry of mathematical methods

**原文链接**: [https://books.physics.oregonstate.edu/GMM/book.html](https://books.physics.oregonstate.edu/GMM/book.html)

生成摘要时出错

---

## 90. First convex polyhedron found that can't pass through itself

**原文标题**: First convex polyhedron found that can't pass through itself

**原文链接**: [https://www.quantamagazine.org/first-shape-found-that-cant-pass-through-itself-20251024/](https://www.quantamagazine.org/first-shape-found-that-cant-pass-through-itself-20251024/)

生成摘要时出错

---

## 91. AWS outage caused by latent race condition in the DynamoDB DNS management system

**原文标题**: AWS outage caused by latent race condition in the DynamoDB DNS management system

**原文链接**: [https://www.bleepingcomputer.com/news/technology/amazon-this-weeks-aws-outage-caused-by-major-dns-failure/](https://www.bleepingcomputer.com/news/technology/amazon-this-weeks-aws-outage-caused-by-major-dns-failure/)

生成摘要时出错

---

## 92. Valetudo: Cloud replacement for vacuum robots enabling local-only operation

**原文标题**: Valetudo: Cloud replacement for vacuum robots enabling local-only operation

**原文链接**: [https://valetudo.cloud/](https://valetudo.cloud/)

生成摘要时出错

---

## 93. The State of Machine Learning Frameworks in 2019

**原文标题**: The State of Machine Learning Frameworks in 2019

**原文链接**: [https://thegradient.pub/state-of-ml-frameworks-2019-pytorch-dominates-research-tensorflow-dominates-industry/](https://thegradient.pub/state-of-ml-frameworks-2019-pytorch-dominates-research-tensorflow-dominates-industry/)

生成摘要时出错

---

## 94. Why can't transformers learn multiplication?

**原文标题**: Why can't transformers learn multiplication?

**原文链接**: [https://arxiv.org/abs/2510.00184](https://arxiv.org/abs/2510.00184)

生成摘要时出错

---

## 95. The Cooperative National Geologic Map

**原文标题**: The Cooperative National Geologic Map

**原文链接**: [https://ngmdb.usgs.gov/nationalgeology/](https://ngmdb.usgs.gov/nationalgeology/)

生成摘要时出错

---

## 96. Modern Perfect Hashing

**原文标题**: Modern Perfect Hashing

**原文链接**: [https://blog.sesse.net/blog/tech/2025-10-23-21-23_modern_perfect_hashing.html](https://blog.sesse.net/blog/tech/2025-10-23-21-23_modern_perfect_hashing.html)

生成摘要时出错

---

## 97. Meet the real screen addicts: the elderly

**原文标题**: Meet the real screen addicts: the elderly

**原文链接**: [https://www.economist.com/international/2025/10/23/meet-the-real-screen-addicts-the-elderly](https://www.economist.com/international/2025/10/23/meet-the-real-screen-addicts-the-elderly)

生成摘要时出错

---

## 98. "ChatGPT said this" Is Lazy

**原文标题**: "ChatGPT said this" Is Lazy

**原文链接**: [https://terriblesoftware.org/2025/10/24/chatgpt-said-this-is-lazy/](https://terriblesoftware.org/2025/10/24/chatgpt-said-this-is-lazy/)

生成摘要时出错

---

## 99. Study: MRI contrast agent causes harmful metal buildup in some patients

**原文标题**: Study: MRI contrast agent causes harmful metal buildup in some patients

**原文链接**: [https://www.ormanager.com/briefs/study-mri-contrast-agent-causes-harmful-metal-buildup-in-some-patients/](https://www.ormanager.com/briefs/study-mri-contrast-agent-causes-harmful-metal-buildup-in-some-patients/)

生成摘要时出错

---

## 100. Alaska Airlines' statement on IT outage

**原文标题**: Alaska Airlines' statement on IT outage

**原文链接**: [https://news.alaskaair.com/on-the-record/alaska-statement-on-it-outage/](https://news.alaskaair.com/on-the-record/alaska-statement-on-it-outage/)

生成摘要时出错

---

