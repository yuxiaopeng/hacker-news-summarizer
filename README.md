# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-10-26.md)

*最后自动更新时间: 2025-10-26 17:45:59*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 2 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 3 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 4 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 5 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 6 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 7 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 8 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 9 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 10 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 11 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 12 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 13 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 14 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 15 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 16 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 17 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 18 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 19 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 20 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 21 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 22 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 23 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 24 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 25 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 26 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 27 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 28 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 29 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 30 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 31 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 32 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 33 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 34 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 35 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 36 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 37 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 38 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 39 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 40 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 41 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 42 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 43 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 44 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 45 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 46 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 47 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 48 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 49 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 50 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 51 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 52 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 53 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 54 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 55 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 56 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 57 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 58 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 59 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 60 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 61 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 62 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 63 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 64 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 65 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 66 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 67 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 68 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 69 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 70 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 71 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 72 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 73 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 74 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 75 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 76 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 77 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 78 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 79 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 80 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 81 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 82 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 83 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 84 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 85 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 86 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 87 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 88 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 89 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 90 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 91 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 92 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 93 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 94 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 95 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 96 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 97 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 98 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 99 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 100 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 101 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 102 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 103 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 104 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 105 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 106 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 107 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 108 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 109 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 110 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 111 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 112 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 113 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 114 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 115 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 116 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 117 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 118 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 119 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 120 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 121 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 122 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 123 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 124 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 125 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 126 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 127 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 128 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 129 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 130 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 131 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 132 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 133 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 134 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 135 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 136 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 137 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 138 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 139 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 140 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 141 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 142 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 143 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 144 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 145 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 146 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 147 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 148 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 149 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 150 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 151 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 152 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 153 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 154 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 155 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 156 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 157 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 158 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 159 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 160 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 161 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 162 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 163 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 164 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 165 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 166 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 167 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 168 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 169 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 170 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 171 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 172 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 173 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 174 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 175 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 176 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 177 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 178 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 179 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 180 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 181 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 182 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 183 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 184 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 185 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 186 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 187 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 188 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 189 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 190 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 191 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 192 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 193 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 194 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 195 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 196 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 197 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 198 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 199 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 200 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 201 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 202 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 203 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 204 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 205 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 206 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 207 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 208 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 209 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 210 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 211 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 212 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 213 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 214 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 215 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 216 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 217 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 218 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 219 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 220 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 221 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
