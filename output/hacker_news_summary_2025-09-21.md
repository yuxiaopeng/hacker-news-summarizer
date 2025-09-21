# Hacker News 热门文章摘要 (2025-09-21)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Sj.h: 一个用约150行C99代码编写的微型JSON解析库

**原文标题**: Sj.h: A tiny little JSON parsing library in ~150 lines of C99

**原文链接**: [https://github.com/rxi/sj.h](https://github.com/rxi/sj.h)

本文介绍 `sj.h`，这是一个极简的 JSON 解析库，用大约 150 行 C99 代码编写。它拥有零内存分配的特性，使其适用于资源受限的环境。该库提供的错误信息能精确定位 JSON 文本中错误的准确位置（行和列）。

关键的设计选择强调灵活性：`sj.h` 避免了内置的数字和字符串解析。开发者需要使用诸如 `strtod` 或 `atoi` 的函数来处理数字转换，从而允许自定义行为。类似地，字符串处理，包括 Unicode 代理对处理，留给用户自行实现。

提供的代码示例演示了如何使用 `sj.h` 解析表示矩形的 JSON 字符串，并在 C 中填充相应的 `Rect` 结构体。该示例遍历 JSON 对象，提取与 "x"、"y"、"w" 和 "h" 等键关联的值，并使用 `atoi` 将这些值转换为整数。

该库以公共领域许可发布，鼓励广泛采用和修改。"demo" 文件夹中可以找到更多使用示例。

---

## 2. 创伤、药物滥用与寻求慰藉之间的关联

**原文标题**: The link between trauma, drug use, and our search to feel better

**原文链接**: [https://lithub.com/the-link-between-trauma-drug-use-and-our-search-to-feel-better/](https://lithub.com/the-link-between-trauma-drug-use-and-our-search-to-feel-better/)

仅凭提供的标题（“创伤、药物使用以及我们寻求感觉更好的联系”）以及Lit Hub页面上展示的热门文章和帖子的附带内容，不可能提供文章内容的摘要。所提供的文本是围绕文章的元数据，而不是文章的实质内容。

然而，我们可以*推断*文章*可能*是关于什么的，基于其标题：

文章可能探讨了创伤经历与随后使用药物作为应对机制之间的联系。它可能深入探讨了经历过创伤的个体可能会转向药物，以此来减轻痛苦、麻木情绪或逃避痛苦记忆的观点。文章可能触及了人类渴望感觉更好的潜在愿望，表明药物使用，虽然最终是有害的，但源于寻求摆脱痛苦的自然本能。它也可能讨论导致这种联系的神经生物学和心理机制，可能参考有关成瘾和创伤的研究或理论。最终，文章可能旨在阐明创伤、药物使用和人类对幸福的追求之间复杂的关系。

要获得真正的摘要，你需要提供文章的实际内容。

---

## 3. DXGI调试：微软把我列入黑名单了

**原文标题**: DXGI debugging: Microsoft put me on a list

**原文链接**: [https://slugcat.systems/post/25-09-21-dxgi-debugging-microsoft-put-me-on-a-list/](https://slugcat.systems/post/25-09-21-dxgi-debugging-microsoft-put-me-on-a-list/)

Luna记录了他们调试Space Station 14 (SS14)在Windows ARM64上运行的历程。该游戏在ARM64上崩溃，但在x64上没有，这阻碍了两种架构的启动器构建。

使用WinDbg进行初始调试令人沮丧，因为存在符号加载问题和ARM64EC模拟混淆。解决这些问题后，崩溃被追溯到`USER32!GetDC`，这是一个基本的Windows函数。深入挖掘后，罪魁祸首被确定为`DXGI!My_GetDC`，它是DirectX图形基础结构（DXGI）中的Microsoft绕行。

该绕行是Windows 11中“窗口化游戏优化”的一部分，它对使用效率较低的位块传输模型的旧游戏强制使用翻转模型（一种现代DirectX交换链效果）。这种优化破坏了ARM64上的SS14。

意想不到的转折是，这种行为仅在可执行文件命名为“SS14.Loader.exe”时才会发生。事实证明，Microsoft有一个启用这些优化的游戏列表，而SS14恰好在该列表上。似乎在测试中遗漏了这种情况，因为没有太多使用位块传输交换链模型的ARM64 Windows游戏。

此外，文章还提到了Windows ARM64上的OpenGL问题，默认的“D3D12上的OpenGL”驱动程序对SS14有图形故障，因此需要使用ANGLE（一个将OpenGL转换为DirectX的兼容性层）。这是一种临时解决方案，最终应该修复。

由于这些问题，SS14的官方Windows ARM64支持被推迟，直到D3D12上的OpenGL驱动程序得到修复，或者ARM64 DXGI绕行问题得到解决。

---

## 4. 牛津大学跌出英国前三名大学之列。

**原文标题**: The University of Oxford has fallen out of the top three universities in the UK

**原文链接**: [https://hotminute.co.uk/2025/09/19/oxford-loses-top-3-university-ranking-for-the-first-time/](https://hotminute.co.uk/2025/09/19/oxford-loses-top-3-university-ranking-for-the-first-time/)

根据《泰晤士报》和《星期日泰晤士报》2026年优秀大学指南，英国大学排名出现重大变化，牛津大学首次跌出前三。杜伦大学超越牛津大学和剑桥大学，位居第三。牛津大学和剑桥大学并列第四，原因是他们在全国学生调查中的表现相对较差。

伦敦政治经济学院（LSE）连续第二年蝉联英国排名第一的大学，其次是圣安德鲁斯大学，也保持了第二名的位置。虽然圣安德鲁斯大学在学生体验和教学质量方面表现出色，但伦敦政治经济学院在毕业生前景和研究质量方面领先。

杜伦大学的崛起归功于学生对教学质量的评价大幅提升了30位。杜伦大学校长凯伦·奥布莱恩教授强调了大学对学生成长和毕业生令人印象深刻的职业前景的承诺。文章包含一份表格，列出了根据《泰晤士报》2026年大学排名得出的英国前20名大学。

---

## 5. 西甲反盗版行动引发西班牙大范围网络中断

**原文标题**: LaLiga's Anti-Piracy Crackdown Triggers Widespread Internet Disruptions in Spain

**原文链接**: [https://reclaimthenet.org/laligas-anti-piracy-crackdown-triggers-widespread-internet-disruptions](https://reclaimthenet.org/laligas-anti-piracy-crackdown-triggers-widespread-internet-disruptions)

**摘要：**

西甲联赛组织方实施了一项旨在屏蔽非法流媒体网站的反盗版系统。据报道，该系统已导致西班牙各地合法用户遭遇大范围网络中断。该系统通过识别和屏蔽涉嫌托管盗版内容的域名来运作。

文章声称，西甲联赛的屏蔽措施过于激进，导致与盗版无关的合法网站和服务也受到影响。这种“附带损害”影响了试图访问各种在线资源的互联网用户，引起了不满，并引发了对西甲联赛措施的比例性和有效性的担忧。

批评人士认为，这种一刀切的屏蔽方法缺乏精确性，无法区分合法内容和侵权内容。他们还对该系统的透明度和问责制以及潜在的滥用行为提出了质疑。文章强调，这次反盗版行动为审查和互联网控制开创了一个危险的先例，即私人实体可以在没有充分监督或正当程序的情况下单方面中断互联网访问。这种情况引发了关于保护知识产权和维护互联网自由之间平衡的辩论，并引发了对在其他地方实施类似措施的可能性的担忧。

---

## 6. 我强迫自己花一周时间刷Instagram，而不是写代码。

**原文标题**: I forced myself to spend a week in Instagram instead of Xcode

**原文链接**: [https://www.pixelpusher.club/p/i-forced-myself-to-spend-a-week-in](https://www.pixelpusher.club/p/i-forced-myself-to-spend-a-week-in)

丹尼尔·豪尔记录了他为期一周的实验，期间他完全专注于Instagram营销来推广他的Lagree Buddy应用程序，放弃了编码和功能开发。起初，他对于优先考虑社交媒体而不是代码感到不适，但他记录了他的每日努力，突出了挑战和意想不到的成功。

他创建了每日Instagram故事线，通过陌生私信联系工作室和教练，甚至参加了由塞巴斯蒂安·拉格雷本人教授的课程来展示该应用程序。丹尼尔低估了内容创作所需的时间和精力，发现它比他预期的更耗费精力。

尽管在应用程序销售额方面没有看到立竿见影的量化结果，但这一周产生了有意义的联系。他与Lagreeing at Home达成了潜在的合作，并获得了塞巴斯蒂安·拉格雷的关注，这些机会是仅靠编码无法实现的。他还收到了工作室老板的积极回应，这位老板记得他之前在Reddit上发布的帖子。

丹尼尔总结说，虽然内容创作比他预期的耗时得多，但像陌生私信和面对面互动这样的营销活动对于建立知名度和关系至关重要，可以补充核心开发工作。他强调了积极推广他的应用程序的重要性，而不是仅仅依靠其功能来吸引用户。

---

## 7. 磁盘工具仍无法检查和修复APFS卷和容器 (2021)

**原文标题**: Disk Utility still can't check and repair APFS volumes and containers (2021)

**原文链接**: [https://eclecticlight.co/2021/11/19/disk-utility-still-cant-check-and-repair-apfs-volumes-and-containers/](https://eclecticlight.co/2021/11/19/disk-utility-still-cant-check-and-repair-apfs-volumes-and-containers/)

本文探讨了macOS中磁盘工具在检查和修复APFS宗卷和容器时持续存在的问题，特别强调了在Monterey 12.0.1中观察到的问题。核心问题在于磁盘工具无法卸载宗卷或容器，从而阻止`fsck_apfs`工具正确运行。作者指出，此错误自Catalina和Big Sur以来一直存在。

虽然磁盘工具的急救功能经常失效，但作者提供了几种解决方法。主要建议是完全绕过磁盘工具，直接使用命令行工具`fsck_apfs`。该过程包括：

1. 在磁盘工具或终端中识别APFS容器或宗卷的设备名称。
2. 使用磁盘工具的卸载工具卸载宗卷或容器。
3. 在终端中执行`fsck_apfs`，并使用适当的选项，例如`-n`（仅检查）、`-y`（自动修复）、`-S`（排除快照）。作者提供了不同命令的示例。
4. 使用磁盘工具的挂载工具重新挂载宗卷或容器。

或者，启动到恢复模式允许磁盘工具正常工作，因为它避免了卸载问题。

文章还提到，虽然Apple建议在检查容器本身之前检查容器内的宗卷，但这会重复检查。作者对这个错误的持续存在以及磁盘工具无法备份Time Machine备份宗卷的讽刺意味表示沮丧。

---

## 8. 同态加密入门教材

**原文标题**: The Beginner's Textbook for Homomorphic Encryption

**原文链接**: [https://arxiv.org/abs/2503.05136](https://arxiv.org/abs/2503.05136)

这篇arXiv文章，题为“全同态加密入门教程”，介绍了全同态加密(FHE)，一种允许直接在加密数据上进行计算的密码学方案。解密计算结果与将相同计算应用于明文数据所得到的结果一致。

该教程解释说，FHE支持加法和乘法等基本运算，从而可以构建更复杂的功能，包括减法、除法、逻辑门以及ReLU、sigmoid和三角函数等高级数学函数。这些函数可以是精确的或近似的。

FHE的一个关键应用是保护隐私的机器学习，服务器可以在不了解明文数据或推理结果的情况下处理加密的客户端数据。FHE还应用于机密区块链服务、安全数据分析外包、加密数据库查询、保护隐私的搜索以及安全多方计算。

该教程是一个开放项目，欢迎FHE专家合作。 该文章提供了提交历史、作者信息（Ronny Ko）、学科分类（密码学和安全、离散数学）以及指向PDF、TeX源代码和其他资源的链接。它还提供了指向各种书目、引文、代码、数据、媒体、演示和相关论文资源的链接。

---

## 9. Spectral Labs 发布 SGS-1：首个结构化 CAD 生成模型

**原文标题**: Spectral Labs releases SGS-1: the first generative model for structured CAD

**原文链接**: [https://www.spectrallabs.ai/research/SGS-1](https://www.spectrallabs.ai/research/SGS-1)

Spectral Labs发布SGS-1，一款能够生成完全可制造和参数化STEP格式3D几何体的新型基础模型。与现有生成模型不同，SGS-1可从图像或“哑”3D网格生成精确且可编辑的CAD B-Rep零件。

SGS-1表现出强大的通用性能，创造比当前方法更复杂的CAD形状。它可用于实际工程任务，例如设计装配支架，并且在给定部分装配上下文和文本描述时表现良好。

文章将SGS-1与OpenAI的GPT-5和开源HoLa模型进行了比较，使用了包含75张图像的基准数据集。SGS-1的性能优于这两个模型，展示了卓越的空间理解能力和几何精度。虽然GPT-5难以生成可用的输出，但SGS-1准确地捕捉了几何特征，并无缝集成到具有可编辑尺寸的装配上下文中。

SGS-1还可以自动将草图、工程图和STL文件转换为参数化STEP文件，从而简化逆向工程。

该模型的局限性包括难以处理创意资产、有机形状、薄结构和完整装配体的生成。未来的模型将解决这些局限性，支持更复杂的空间背景，并通过强化学习和物理模拟反馈来整合高级物理推理。Spectral Labs欢迎那些有兴趣部署SGS-1、合作研究或加入其团队的人员联系。

---

## 10. 热电制冷新突破，效率近翻倍

**原文标题**: New thermoelectric cooling breakthrough nearly doubles efficiency

**原文链接**: [https://www.sciencedaily.com/releases/2025/09/250919085242.htm](https://www.sciencedaily.com/releases/2025/09/250919085242.htm)

约翰·霍普金斯APL研究人员开发出新型热电冷却技术CHESS，在室温下效率几乎是传统材料的两倍。这种固态制冷技术采用纳米工程材料，为基于压缩机的冷却系统提供了一种可扩展且更高效的替代方案。

最初为国家安全而开发的CHESS薄膜技术，在标准化测试中表现出比传统热电材料近100%的效率提升。这转化为设备层面效率提高75%，以及完全集成的制冷系统中效率提高70%。

CHESS的一个关键优势是其可扩展性。该技术使用少量材料，并可使用半导体芯片生产工具进行大规模生产。它采用金属有机化学气相沉积(MOCVD)工艺，该工艺已用于太阳能电池和LED的生产。

除了制冷之外，CHESS材料还可以将温差转化为可用电力，为能量收集、假肢和人机界面等应用打开了大门。APL正在与各组织合作，进一步改进这些材料，目标是达到传统机械系统的效率水平，并探索在大型制冷系统和HVAC设备中的应用。他们还在研究整合人工智能以优化能源效率。

---

## 11. iFixit iPhone Air 拆解

**原文标题**: iFixit iPhone Air teardown

**原文链接**: [https://www.ifixit.com/News/113171/iphone-air-teardown](https://www.ifixit.com/News/113171/iphone-air-teardown)

iFixit拆解iPhone Air：纤薄设计未损可修复性，暂评7分（满分10分）。苹果通过巧妙地重新排列内部组件，特别是将逻辑板置于电池上方，实现了这一目标，创造了“扁平化的拆解树”，更容易接触到关键部件。

由于苹果的双入口设计，电池可以通过后玻璃轻松访问，使用电解脱胶粘合剂进行安全移除，并且令人惊讶的是，它与Apple MagSafe电池包中使用的电池芯相同。虽然电池续航时间可能比其他iPhone短，但更换过程很简单。USB-C端口也是模块化的，尽管苹果目前不提供内部维修或更换部件。该端口的壳体采用了独特的3D打印钛工艺，iFixit在显微镜下对其进行了检查。

手机的结构完整性由钛金属框架支撑，但在塑料天线过孔处较为脆弱，这在弯曲测试中得到了证实。总的来说，iFixit赞扬了苹果在纤薄外形中优先考虑可修复性的设计选择，强调了电池更换的简易性、易于访问的组件以及对维修手册的承诺。他们总结说，iPhone Air是卓越工程如何创造耐用且可修复的纤薄设备的成功典范，尽管他们仍在等待苹果确认零件的可用性，以便最终确定评分。

---

## 12. 人工智能本应帮助新人脱颖而出，为何大多时候却让资深人士更强？

**原文标题**: AI was supposed to help juniors shine. why does it mostly make seniors stronger?

**原文链接**: [https://elma.dev/notes/ai-makes-seniors-stronger/](https://elma.dev/notes/ai-makes-seniors-stronger/)

本文探讨了人工智能赋能初级开发者的最初期望与人工智能主要使高级开发者受益的现实之间的差距。作者认为，尽管人工智能擅长生成样板代码、自动化例程和快速原型设计等任务，但其在代码审查、提示词质量、架构设计、代码质量和安全性方面的不足使其更有利于经验丰富的开发者。

高级开发者受益于人工智能加速日常任务和快速交付功能的能力，因为他们具备有效利用这些能力并减轻潜在风险的基础知识和批判性思维能力。缺乏经验的初级开发者更容易遇到人工智能生成的代码问题，导致错误、技术债务和安全漏洞。

作者建议将人工智能的重点放在快速原型设计、自动化重复性任务、跨学科工作（填补知识空白）和功能测试等领域，并强调需要人工监督和验证。文章总结说，目前的人工智能能力虽然对未来充满希望，但尚未成熟到足以实现编码民主化，反而放大了高级开发者的专业知识。作者提倡重置对软件开发中人工智能的期望，以避免对初级开发者造成不切实际的负担并保持代码质量。

---

## 13. 换个说法的抛硬币 (2023)

**原文标题**: A coin flip by any other name (2023)

**原文链接**: [https://cgad.ski/blog/a-coin-flip-by-any-other-name.html](https://cgad.ski/blog/a-coin-flip-by-any-other-name.html)

本文探讨了两个看似无关的问题都导致1/2概率的可能性：特定图中随机移除边后路径仍然存在，以及原点位于单位圆上四个随机点的凸包内。作者认为这种偶数概率表明存在潜在的对称性。

对于图的问题，引入了一个“对偶”技巧，证明了顶部和底部节点之间存在路径当且仅当左右节点之间不存在路径。由于配置是对称的，所以每个事件（存在路径或不存在路径）发生的概率均为1/2。

对于四点问题，定义了一个保测变换，将((a,b),(c,d))转换为(normal(a,b),normal(-c,-d))，其中'normal'返回正交单位向量。这种变换保持概率，并将原点位于凸包内的事件与原点不位于凸包内的事件互换，再次导致1/2的概率。

文章随后将问题推广到*n*维空间中的*k*个点，并将其与使用超平面划分空间的问题联系起来。它提供了一个组合公式来计算原点位于R^n中*k*个随机向量的凸包内的概率，假设向量的分布在符号取反下是不变的。这个概率与*k*-1个独立伯努利变量的和有关。最后，文章将问题框架化为半球覆盖单位球，突出了不同维度中随机点何时可能包含原点的反直觉性质。

---

## 14. 评：世外桃源计划——本可能出现的互联网

**原文标题**: Review: Project Xanadu – The Internet That Might Have Been

**原文链接**: [https://www.astralcodexten.com/p/your-review-project-xanadu-the-internet](https://www.astralcodexten.com/p/your-review-project-xanadu-the-internet)

本文回顾了超文本和互联网的起源，以泰德·尼尔森构想的富有远见的Xanadu计划为视角。首先介绍了范内瓦尔·布什1945年提出的“Memex”概念，这是一种用于组织和连接知识的理论机器。道格·恩格尔巴特于1968年推出的oN-Line System (NLS) 展示了超媒体、鼠标和协同编辑，被认为是实现Memex愿景的早期尝试。然而，恩格尔巴特的研究逐渐被埋没。

接下来，本文重点介绍了泰德·尼尔森，他将Xanadu设想为一个通用的超文本系统，能够以复杂的方式存储和连接文档。尼尔森的雄心是创建一个支持版本历史、复杂链接和知识创造性探索的平台。本文强调了尼尔森对Xanadu的哲学方法，以及它与传统数据处理的不同之处。文章还提到了该项目面临的一些挑战。

---

## 15. 禁止批评公司后，Meta 曝光作者面临破产

**原文标题**: Meta exposé author faces bankruptcy after ban on criticising company

**原文链接**: [https://www.theguardian.com/technology/2025/sep/21/meta-expose-author-sarah-wynn-williams-faces-bankruptcy-after-ban-on-criticising-company](https://www.theguardian.com/technology/2025/sep/21/meta-expose-author-sarah-wynn-williams-faces-bankruptcy-after-ban-on-criticising-company)

前Meta高管、《轻率之辈》一书的作者萨拉·温-威廉姆斯在Meta获得禁止其诋毁公司的命令后，面临破产的可能。该书包含关于Meta与中国的交易、对青少年的待遇以及性骚扰指控，所有指控均遭到该公司否认。

议员路易丝·海格在议会提出了这个问题，指责Meta试图“压制和惩罚”温-威廉姆斯的发声，她可能因每次违反该命令而面临5万美元的罚款。海格认为，Meta正在利用英国的仲裁系统在经济上摧毁温-威廉姆斯，尽管此前Meta曾声明不在性骚扰案件中使用保密协议。

Meta坚持认为，温-威廉姆斯在2017年离职时自愿签署了非贬低协议，并且她尚未支付任何款项。他们声称她的参议院证词是虚假的，并且在调查得出她提出了毫无根据的骚扰指控后，她因“表现不佳和有毒行为”而被解雇。他们还将她的书描述为过时的说法和虚假指控的集合。

虽然该裁决阻止了温-威廉姆斯宣传这本书，但Pan Macmillan已售出超过15万册。温-威廉姆斯的律师表示，尽管国会呼吁结束仲裁程序，她仍然保持沉默。

---

## 16. 如何停止函数式编程 (2016)

**原文标题**: How to stop functional programming (2016)

**原文链接**: [https://brianmckenna.org/blog/howtostopfp](https://brianmckenna.org/blog/howtostopfp)

这篇讽刺文章讲述了这样一种情况：由于同事缺乏理解以及经理的回避冲突决策，开发者被告知停止使用函数式编程（FP）。作者强调了*完全*避免FP的荒谬性，论证了即使是看似简单的任务也不可避免地涉及到函数式概念。

作者用创建一个列出用户同事的函数的例子来说明。最初使用`flatMap`以纯粹的函数式风格编写，然后作者试图通过引入可变状态（`ListBuffer`）和副作用（日志记录）来避免FP。幽默之处在于，即使进行了这些更改，该函数仍然包含函数式元素，“没有函数式编程”的定义也很模糊。

文章随后通过引入产品需求变更（显示同事的数量而不是列表）进一步推进了讽刺。这迫使开发者考虑*如何*在不“纯粹”的情况下执行简单的算术运算，暗示了避免FP的指令最终是不切实际的，并且阻碍了生产力。结论表明，经理的决定可能会导致荒谬的情况，即由于被迫避免有效的编程范例，即使是基本操作也会变得复杂。主要信息是，一概而论地禁止编程风格可能是有害且适得其反的。

---

## 17. 超声波厨刀

**原文标题**: Ultrasonic Chef's Knife

**原文链接**: [https://seattleultrasonics.com/](https://seattleultrasonics.com/)

本广告宣传西雅图超声波C-200超声波8寸厨师刀，声称其为世界首款家用超声波厨师刀。该刀利用超声波使刀刃轻松滑过食物，从而实现干净利落的切割、最小的力气和减少粘连。

主要特点包括采用日本三枚钢AUS-10钢材制成的200毫米刀刃，以及可通过USB-C和无线充电充电的电池。

目前提供两种预购选项：单独一把刀售价399.00美元；刀和充电器套装售价499.00美元（低于原价组合价548.00美元）。 两者目前已售罄，可预订，预计发货日期为2026年1月（第一批）。 顾客可以在订单发货前的任何时间取消预购。 该广告鼓励感兴趣的人士注册以获取更多信息。

---

## 18. WeAct Display FS 为你的电脑增加一个0.96英寸的USB信息显示屏

**原文标题**: $2 WeAct Display FS adds a 0.96-inch USB information display to your computer

**原文链接**: [https://www.cnx-software.com/2025/09/18/2-weact-display-fs-adds-a-0-96-inch-usb-information-display-to-your-computer/](https://www.cnx-software.com/2025/09/18/2-weact-display-fs-adds-a-0-96-inch-usb-information-display-to-your-computer/)

本文介绍 WeAct Display FS V1，一款小巧的 2 美元 USB 加密狗，配备 0.96 英寸全彩显示屏（160x80 分辨率），旨在为计算机和 SBC 添加信息屏幕或辅助显示器。USB-A 端口是可逆的，允许用户以任一方向定向显示屏。

WeAct 为该设备提供了两个软件程序。 "WeAct Studio System Monitor" 基于开源的 Turing Smart Screen 项目，允许用户创建自定义 UI，显示文本、图像、天气和其他信息。虽然 WeAct 声称该程序仅适用于 Windows，但原始项目支持 macOS、Linux 和其他 Python 3.9+ 兼容的操作系统。

第二个程序 "WeAct Studio Screen Projection" 模拟显示器，使用户能够将窗口和程序移动到微型屏幕上。然而，由于 160x80 的极低分辨率，它的实际用途令人质疑。第二个程序仅适用于 Windows，并且是闭源的。

WeAct Display FS V1 在速卖通上有售，价格约为 2 美元加上运费。文章还提到了一款更大的 3.5 英寸型号，分辨率为 480x320，价格约为 11 美元。

---

## 19. 几天内从头开始用Ada编写一个有竞争力的BZip2编码器 - 第3部分

**原文标题**: Writing a competitive BZip2 encoder in Ada from scratch in a few days – part 3

**原文链接**: [https://gautiersblog.blogspot.com/2025/09/writing-competitive-bzip2-encoder-in.html](https://gautiersblog.blogspot.com/2025/09/writing-competitive-bzip2-encoder-in.html)

无法访问文章链接。

---

## 20. Postgres 18 中的 UUIDv7，带时间提取功能

**原文标题**: UUIDv7 in Postgres 18. With time extraction

**原文链接**: [https://www.thenile.dev/blog/uuidv7](https://www.thenile.dev/blog/uuidv7)

无法访问文章链接。

---

## 21. 嗨，野兽前辈

**原文标题**: Hi No Youjin

**原文链接**: [https://aethermug.com/posts/hi-no-youjin](https://aethermug.com/posts/hi-no-youjin)

马可·詹科蒂反思了他与过去产生联系的经历，最初是由古罗马遗址触发的。触摸古老的石头，他感到敬畏和永恒，想象着几千年前站在同一地点的人们的生活。他最初认为这种体验仅限于石头和金属等耐用材料。

然而，搬到日本后，他发现即使是木制建筑也能唤起这种感觉，他特别引用了道格拉斯·亚当斯关于京都金阁寺的轶事，金阁寺不断重建，但仍被认为是同一座建筑。这让他意识到，这种联系的关键在于建筑背后持久的“理念”或“意图”，而不是原始材料。

他进一步完善了自己的理解，认为仅仅是年代久远或重建是不够的。伊势神宫每20年重建一次，但它比现代建筑更能引起更深层次的联系，突出了超越物理年龄的重要性。

作者随后分享了他在东京的经历，听到邻里里“火の用心”（“小心火烛”）的巡逻声。他了解到这种防火警戒的做法可以追溯到1648年，每天晚上听到同样的短语，唤起了一种与过去强大的连续感，将他带到了江户时代的日本。詹科蒂总结说，与过去联系的本质在于持久的传统和共同的人类体验，超越了物体或实践的物理材料和年龄。

---

## 22. Linux 准备向上游提交对 Google PSP 加密 TCP 连接的支持

**原文标题**: Linux Ready to Upstream Support for Google's PSP Encryption for TCP Connections

**原文链接**: [https://www.phoronix.com/news/PSP-Encryption-Linux-6.18](https://www.phoronix.com/news/PSP-Encryption-Linux-6.18)

谷歌的PSP（PSP安全协议），旨在加密传输中的TCP网络连接，预计将在即将发布的6.18版本中集成到主线Linux内核中。经过十三轮审查，该代码已成功通过支持PSP的CX7 NIC的测试，预计将被合并。

PSP由谷歌于2022年开源，作为IP之上的加密封装层，旨在满足大型数据中心的需求。谷歌开发PSP是为了替代IPsec ESP，使其更简单、更实用、更具可扩展性。

最初的实现侧重于启用PSP以实现高效的TLS卸载，利用该协议卓越的卸载特性。核心代码公开设备信息，供各种PSP实现（xfrm、隧道等）使用，通过将加密状态附加到套接字并将skb标记为“已解密”，以TLS的方式集成TCP。

第一个迭代版本包括针对NVIDIA-Mellanox MLX5网络驱动程序的设备特定实现。未来的发展目标是使用PSP作为更高效的TLS卸载，在同一TCP连接中内联执行TLS握手，然后切换到PSP。该代码将作为即将到来的Linux 6.18合并窗口的一部分提交。

---

## 23. 胶质母细胞瘤中染色体外DNA驱动的癌基因演化

**原文标题**: Extrachromosomal DNA–Driven Oncogene Evolution in Glioblastoma

**原文链接**: [https://aacrjournals.org/cancerdiscovery/article/doi/10.1158/2159-8290.CD-24-1555/764257/Extrachromosomal-DNA-Driven-Oncogene-Spatial](https://aacrjournals.org/cancerdiscovery/article/doi/10.1158/2159-8290.CD-24-1555/764257/Extrachromosomal-DNA-Driven-Oncogene-Spatial)

无法访问文章链接。

---

## 24. 苹果40W动态功率适配器拆解（最大功率60W）

**原文标题**: Teardown of Apple 40W dynamic power adapter with 60W max

**原文链接**: [https://www.chargerlab.com/teardown-of-apple-40w-dynamic-power-adapter-with-60w-max-a3365/](https://www.chargerlab.com/teardown-of-apple-40w-dynamic-power-adapter-with-60w-max-a3365/)

本文拆解了苹果新款40W动态电源适配器 (A3365)，它能动态提供高达60W的功率。该适配器与iPhone 17系列一同发布，以其紧凑的尺寸（类似于苹果20W充电器）和可折叠插脚而著称。它可在20分钟内将iPhone 17充电至50%，并可为 MacBook Air M3 等设备提供高达 60W 的功率。

拆解显示其内部设计精良。外壳采用卡扣式夹子和超声波焊接。内部组件采用石墨散热垫、泡沫缓冲垫和耐高温胶带进行绝缘，以实现散热和保护。

主要组件包括PI主控芯片（ZN1612F）、RECTRON同步整流器（RM85N100DF）、英飞凌协议芯片（CYPDC1185B2-32E）以及用于滤波的NCC和尼吉康电容。热敏电阻可实现基于温度的动态功率切换。该设计具有两个共模扼流圈、一个安全X2电容，并同时使用电解电容和固态电容。

文章总结称，该适配器的动态功率输出能根据设备需求智能调节，使其适用于iPhone和MacBook。ChargerLAB强调了组件的高度集成、有效的散热以及坚固的制造质量。

---

## 25. 为何身为负责任的成年人，《模拟城市2000》给人的感受如此不同

**原文标题**: Why, as a responsible adult, SimCity 2000 hits differently

**原文链接**: [https://arstechnica.com/gaming/2025/09/thirty-years-later-simcity-2000-hasnt-changed-but-i-have/](https://arstechnica.com/gaming/2025/09/thirty-years-later-simcity-2000-hasnt-changed-but-i-have/)

在本文中，凯尔·奥兰德反思了成年后重玩《模拟城市2000》的经历，对比了他童年时期的体验和一种新的责任感。童年时，这款游戏是肆意妄为的乐园，充斥着无限金钱作弊码和对虚拟城市的鲁莽实验。他会兴高采烈地摧毁街区，优先考虑美观而非功能，并且无视模拟市民的福祉。

然而，作为一名成年房主、父母和城市居民重返游戏时，奥兰德发现自己开始思考游戏中决策的现实影响。提高税收、赌博合法化以及忽视基础设施建设现在都承载着个人经验和对社会后果的理解带来的沉重感。他纠结于与社会项目、环境问题和城市规划相关的权衡。

文章还突出了《模拟城市2000》的理想化方面，将其简化的建造过程与现实世界城市发展的现实进行了对比。尽管存在一些古老的UI元素，但这款游戏的复古未来主义美学仍然充满魅力。最终，作为一名负责任的成年人，奥兰德渴望为他的虚拟市民创造一个繁荣宜居的环境，即使他承认内心深处仍然存在放纵他内心孩子破坏冲动的诱惑。作者最后强调了《模拟城市2000》在GOG上的可用性，并公开了他作为Ars Technica高级游戏编辑的身份。

---

## 26. 自由，平等，放射性

**原文标题**: Liberté, égalité, Radioactivité

**原文链接**: [https://worksinprogress.co/issue/liberte-egalite-radioactivite/](https://worksinprogress.co/issue/liberte-egalite-radioactivite/)

本文探讨了法国在20世纪70年代成功采用核能的案例，并将其与其他西方国家核计划的衰落进行了对比。尽管起步缓慢，且法国原子能委员会（CEA，核武器计划）与法国电力公司（EDF，电网）之间存在内部冲突，但由于一项将廉价、可靠电力置于完全依赖本土技术之上的政治驱动决策，法国最终拥抱了核能。

梅斯梅尔计划是为应对1973年石油危机而启动的，它率先进行了快速的核能建设，其特点是标准化反应堆设计、长期规划和简化的法规。这使得法国能够以美国成本的一小部分快速高效地建造反应堆。

法国成功的关键因素在于相对较弱的反核运动。法国的政治体制拥有强大的行政部门和薄弱的立法机构，几乎没有提供反对的法律途径。此外，共产党作为潜在的反核情绪来源，依赖于核工业工人的支持，因此采取了支持核能的立场。

法国的税收制度也将工业收入导向东道社区，这也发挥了至关重要的作用。市政当局从运营核电站中获得了巨大的财政收益，使他们能够降低税收、改善基础设施并促进当地对核能的支持。这种财政激励措施将地方市长转变为核能扩张的积极倡导者，最终为法国电网的成功脱碳做出了贡献。

---

## 27. 优先考虑极端情况的首发库的臃肿

**原文标题**: The bloat of edge-case first libraries

**原文链接**: [https://43081j.com/2025/09/bloat-of-edge-case-libraries](https://43081j.com/2025/09/bloat-of-edge-case-libraries)

本文批判了软件开发中“边缘情况优先”的库的普遍现象，认为它们会导致臃肿的依赖树。作者认为，许多库为了不太可能或不必要的边缘情况而过度设计，导致过度细化的依赖关系。

作者用例子说明了这一点，例如一个过度设计的`clamp`函数，它处理字符串输入，尽管它是为数字设计的，最终讽刺了像`is-number`这样的库的存在。他们提倡专注于常见用例并假定正确输入类型的库，将验证留给数据边界处的应用程序级别。

有问题的库的例子包括`is-arrayish`、`is-number`、`pascalcase`和`is-regexp`，突出了它们对大多数用户不会遇到的晦涩边缘情况（如跨领域的RegExp对象）的处理。相比之下，作者赞扬了像`scule`和`dlv`这样的库，它们更专注，并对输入类型做出假设。

本文还提到了像`shebang-regex`和`is-whitespace`这样过度细化的库，批评了将功能拆分为原子单元的趋势。

作者建议维护者应该审查他们的依赖关系，考虑使用原生功能或性能更高的替代方案，并且对输入类型更加严格。鼓励用户监控他们的依赖关系，并确保验证发生在数据边界。核心论点是，库应该优先考虑主要用例，边缘情况支持应由替代方案或插件提供，而不是将边缘情况处理的成本强加给每个人。

---

## 28. 血糖数据处理器：在安卓设备上接收和可视化血糖数据

**原文标题**: Gluco data handler: Receive and visualize glucose data on Android

**原文链接**: [https://github.com/pachi81/GlucoDataHandler](https://github.com/pachi81/GlucoDataHandler)

GlucoDataHandler (GDH) 是一款 Android 应用程序，可集中并可视化来自智能手机、智能手表（Wear OS、小米手环、华米）和汽车（通过 GlucoDataAuto）等各种来源的葡萄糖数据。

它支持多种数据源，包括 LibreLinkUp、Dexcom Share、Medtrum 和 Nightscout 等云服务，以及 AndroidAPS、Juggluco、xDrip+、Eversense (ESEL) 和 Dexcom BYODA 等本地应用。一项 Beta 功能可以通过 Android 通知接收葡萄糖值。

GDH 通过小部件、浮动小部件、带有可自定义图标的可选通知、锁屏壁纸和息屏显示 (AOD) 支持提供全面的可视化。它包括针对极低、低、高、极高和过期葡萄糖值的可自定义警报，具有单独的声音设置和全屏锁屏警报。

Wear OS 集成提供适用于其他表盘的复杂功能，并在手表上直接接收警报（需要手机应用程序）。 WatchDrip+ 支持可用于特定的小米手环和华米设备。该应用具有 TalkBack 辅助功能。它还通过 GlucoDataAuto 兼容 Android Auto，并支持 Tasker 集成。数据转发允许将血糖数据广播到其他应用程序。

GDH 不提供独立的 Wear OS 表盘，但两位用户提供了与 GDH 复杂功能兼容的专用表盘。

---

## 29. 蓝鳍LTS已发布

**原文标题**: Bluefin LTS Is Released

**原文链接**: [https://docs.projectbluefin.io/blog/bluefin-lts-ga/](https://docs.projectbluefin.io/blog/bluefin-lts-ga/)

经过九个月的开发，Bluefin LTS 和 Bluefin GDX 现已正式发布。Bluefin LTS 是一个基于 CentOS Stream 10 的工作站操作系统，专为喜欢长期支持且拥有现代 GNOME 48 桌面以及 Flathub、Homebrew 和 ZFS 支持等功能的用户而设计。它提供一个可选的硬件支持 (HWE) 分支，该分支具有更新的 Linux 内核 (6.15.9)，适用于更新的硬件，例如 Framework 12 和 Framework Desktop。

Bluefin GDX 是一个衍生自 Bluefin LTS 的 AI 工作站，专注于为 AI 和机器学习专业人士提供 Nvidia 驱动程序和 CUDA。它包括 Nvidia CUDA 和 VSCode 集成、用于 AI 模型管理的 Ramalama 以及用于 Python 包管理的 uv 等功能，并且该项目已与 Red Hat Enterprise Linux 命令行助手团队合作。

这些版本具有新的 Anaconda webui 安装程序，并将每周收到更新。Bluefin LTS 对开发者来说将更具可持续性，虽然 Bluefin GTS 可能会在网站上隐藏，但仍将提供。与 Bluefin 和 Bluefin GTS 不同，Bluefin LTS 不支持本地分层或 AppImages。

文章还宣布了一家新的 Bluefin 商店，其中包含用于支持古生物艺术品的商品。此次发布是 Yulian Kuncheff、Ahmed Adan 和 M. Gopal 等人共同努力的结果，并得到了 Carl George、Laura Santamaria、Shaun McCance 和 bootc 团队的支持。Bluefin LTS 和 GDX 的下载适用于 AMD/Intel 和 ARM (aarch64) 架构。

---

## 30. 氛围代码清理即服务

**原文标题**: Vibe coding cleanup as a service

**原文链接**: [https://donado.co/en/articles/2025-09-16-vibe-coding-cleanup-as-a-service/](https://donado.co/en/articles/2025-09-16-vibe-coding-cleanup-as-a-service/)

AI代码生成催生新服务类别：Vibe Coding 清理

---

## 31. 镁、微生物组与降低结肠癌风险

**原文标题**: Magnesium, the microbiome, and reducing the risk of colon cancer

**原文链接**: [https://newatlas.com/health-wellbeing/magnesium-supplements-gut-bacteria-colorectal-cancer/](https://newatlas.com/health-wellbeing/magnesium-supplements-gut-bacteria-colorectal-cancer/)

2025年文章：镁补充剂、肠道细菌与降低结肠癌风险的潜在联系

该2025年文章探讨了镁补充剂、肠道细菌与降低结肠癌风险之间的潜在联系。范德堡大学医学中心领导的一项临床试验发现，镁补充剂可以促进有益肠道细菌的生长，特别是*麦芽糖肉杆菌(Carnobacterium maltaromaticum)*，并在较小程度上促进*粪杆菌(Faecalibacterium prausnitzii)*的生长，这可能有助于抑制结直肠癌的生长。

然而，这种效果因基因和性别而异。TRPM7基因（调节镁）中没有特定“错义变异”(Thr1482Ile)的个体对镁补充剂反应良好，这些有益细菌有所增加，尤其是女性。*有*这种变异的个体有时会产生相反的效果。

后续的结肠镜检查显示，直肠组织活检中较高水平的*麦芽糖肉杆菌*与较低的发生锯齿状息肉（与较高的结直肠癌风险相关）的风险有关，而较高水平的*粪杆菌*与较高的息肉风险有关，尽管这一发现不太具有确定性。

该研究提出了一种“精准营养”方法，通过基因检测可以帮助识别最能从镁补充剂中获益的个体。尽管该研究存在局限性（持续时间短，特定人群），但它突出了镁和肠道微生物群在预防结直肠癌方面的潜在作用，特别是对于女性和那些没有特定TRPM7基因变异的人。还需要进一步的研究来证实这些发现，并将其转化为临床建议。

---

## 32. 设计 NotebookLM

**原文标题**: Designing NotebookLM

**原文链接**: [https://jasonspielman.com/notebooklm](https://jasonspielman.com/notebooklm)

文章“设计NotebookLM”侧重于NotebookLM（可能是一款用于笔记、知识整理或信息管理的工具）背后的设计过程的用户旅程和带注释的概述。

标题表明以设计为中心的视角，强调用户体验以及界面的概念化和开发过程。提及“用户旅程”表明重点在于绘制用户在与软件交互时所采取的步骤，突出痛点和需要改进的领域。这可能包括对引导、导航和核心功能的考虑。

包含“带注释的概述”意味着对产品功能和特性的详细检查。这可能涉及直观地解释用户界面的关键元素，为设计选择提供背景信息，并展示该工具如何满足特定的用户需求。这表明文章将把产品分解为各个组件，提供深刻的解释，并可能提供视觉辅助。

本质上，这篇文章可能深入探讨NotebookLM以用户为中心的设计过程，详细说明创建者如何通过明确定义的用户旅程和对产品功能和界面的彻底注释检查来理解和满足目标受众的需求。它可能旨在全面了解创建NotebookLM的设计选择背后的原理。

---

## 33. 自由，平等，放射性

**原文标题**: Liberté, égalité, Radioactivité

**原文链接**: [https://worksinprogress.co/issue/liberte-egalite-radioactivite/](https://worksinprogress.co/issue/liberte-egalite-radioactivite/)

本文探讨了法国在 20 世纪 70 年代成功采用核能的案例，并将其与其他西方国家核电衰落的情况进行了对比。 当其他国家苦于应对成本上升、监管问题和公众反对时，法国在梅斯梅尔计划下启动了快速的核电建设，最终以高度依赖核能的方式实现了电网的脱碳。

这种成功并非命中注定。 法国早期的核电努力因技术选择和内部冲突而受阻。尽管 CEA 存在抵制，但法国电力公司 (EDF) 倡导转向压水反应堆 (PWR) 至关重要。 在戴高乐卸任总统后，法国采用了该技术。 1973 年的石油危机进一步推动了这一进程，导致大量订购新的反应堆。

法国成功的因素有以下几个：简化的监管流程、长期规划、标准化设计和专业的供应链。 关键在于，文章强调了法国反核运动相对薄弱的原因，包括强大的行政部门、主要政党之间亲核的共识以及与核能就业相关的工会支持。

此外，法国的商业税收制度通过将工业收入导向当地社区，从而鼓励当地社区接受核电。 这与政府补贴以及法国电力公司对当地基础设施和文化活动的投资相结合，将市长们转变为核电扩张的积极支持者。 文章强调，法国的经验为其他寻求将核能作为脱碳战略的国家提供了宝贵的经验。

---

## 34. 利用算法学习语言

**原文标题**: Learning Languages with the Help of Algorithms

**原文链接**: [https://www.johndcook.com/blog/2025/09/17/learning-languages-with-the-help-of-algorithms/](https://www.johndcook.com/blog/2025/09/17/learning-languages-with-the-help-of-algorithms/)

本文探讨了使用算法来高效提升新语言学习中的词汇习得，特别是通过选择具有高词汇影响力的书籍。该问题被形式化为从一组书籍中找到最佳书籍，其中“最佳”的定义是存在于书中的词汇单词的加权总和，并根据它们在该语言中的频率进行加权。

虽然找到单本最佳书籍可以在线性时间内解决，但选择最佳的 *k* 本书籍以获得最佳的联合词汇覆盖是一个 NP 难题，这意味着对于较大的 *k*，精确解在计算上变得不可行。然而，该问题可以被视为子模问题空间中的最大加权覆盖问题，从而允许使用近似算法，其精度在最佳解决方案的某个因子内得到保证。

本文重点介绍了一种贪婪方法：迭代地将单本最具影响力的书籍添加到选择中，利用 Python 的 `submodlib` 等库来提高速度。对这种贪婪方法的改进，例如阻止策略、前瞻策略和启发式方法（例如，丢弃具有冗余词汇的书籍），可以提高结果质量，但会增加计算量。尽管有这些改进，除非 P=NP，否则找到一个 *精确* 解仍然具有挑战性。最终，本文提出了一种实用的、算法驱动的方法，通过策略性地选择阅读材料来优化语言学习。

---

## 35. 激光雷达、光学测距和飞行时间传感器

**原文标题**: Lidar, optical distance and time of flight sensors

**原文链接**: [https://ams-osram.com/innovation/technology/depth-and-3d-sensing/lidar-optical-distance-and-time-of-flight-sensors](https://ams-osram.com/innovation/technology/depth-and-3d-sensing/lidar-optical-distance-and-time-of-flight-sensors)

本文重点介绍三种类型的传感器：激光雷达 (LIDAR)、光学测距传感器和飞行时间 (ToF) 传感器。文章着重强调了全集成直接飞行时间 (dToF) 模块和间接飞行时间 (iToF) VCSEL 照明器的可用性，特别适用于短程应用。文章还提到了适用于远程激光雷达系统的激光源，暗示了它们在实现更广泛的传感能力方面的重要性。总而言之，本文总结了使用各种技术进行短程和远程距离及深度感测的组件和解决方案的可用性。

---

## 36. EA 作为敌基督：理解彼得·蒂尔

**原文标题**: EA as Antichrist: Understanding Peter Thiel

**原文链接**: [https://forum.effectivealtruism.org/posts/hGwAohPbwCrDT5ynY/ea-as-antichrist-understanding-peter-thiel](https://forum.effectivealtruism.org/posts/hGwAohPbwCrDT5ynY/ea-as-antichrist-understanding-peter-thiel)

本文阐述了彼得·蒂尔对有效利他主义（EA）颇具争议的观点，即EA可能体现了敌基督。蒂尔认为敌基督不一定是个人，而是一种体系或意识形态，它承诺和平与安全，但实际上导致全球停滞和极权主义。

他的论点基于这样一种理念：由于安全考虑，有效利他主义者倡导放缓人工智能的发展，但这最终会阻碍技术进步，而技术进步是唯一剩余的增长动力。蒂尔认为停滞会导致冲突和社会崩溃。

本文介绍了吉拉德的模仿理论，这是对蒂尔产生关键影响的理论。该理论认为人类的欲望是基于对他人模仿，从而导致冲突，而冲突可以通过替罪羊来解决。根据吉拉德的说法，基督教揭示了替罪羊行为的错误。蒂尔担心现代“觉醒”版本的替罪羊行为，会导致新的极权主义。

蒂尔认为政府和全球化本质上存在问题。他强调了人工智能等生存风险与在和平与安全的幌子下，一个停滞不前、受到全球监管的“世界政府”的危险之间的权衡。他认为像FDA和核管理委员会这样监管技术的组织可能体现了这种危险趋势，反映了敌基督以牺牲进步为代价，对和平的欺骗性承诺。因此，他认为有效利他主义及其对人工智能安全监管的关注，无意中促成了这种反乌托邦的结果。

---

## 37. 为互换辩护：常见误解 (2018)

**原文标题**: In defence of swap: common misconceptions (2018)

**原文链接**: [https://chrisdown.name/2018/01/02/in-defence-of-swap.html](https://chrisdown.name/2018/01/02/in-defence-of-swap.html)

本文为在现代 Linux 系统中使用交换空间辩护，反驳了一种常见的误解，即它仅仅是缓慢的、紧急情况下的内存。文章认为，交换空间的主要目的是实现“回收平等”，通过将不常用的匿名页（未由文件支持的内存分配）分页到磁盘，从而有效地管理内存，释放 RAM 以供更积极的使用。

作者解释说，如果没有交换空间，这些匿名页将保持锁定在内存中，可能会通过取代页面缓存（文件内存）中更重要的数据来阻碍性能。禁用交换空间并不能消除内存压力下的磁盘 I/O 问题；它只是将抖动从匿名页转移到文件页。

本文解决了对交换空间性能的担忧，指出在 SSD 上，交换匿名页与回收文件页相当。对于较旧的旋转磁盘，建议使用较低的 `vm.swappiness` 值。此外，作者还强调了 4.0 及更高版本内核中交换空间管理的改进。

文章认为，虽然交换空间可以在接近 OOM 的情况下延长病态行为，但禁用它并不能阻止它。文章建议在 cgroup v2 中使用 `memory.low` 来对交换空间行为进行细粒度控制，允许管理员在内存压力下优先回收某些应用程序。

作者的结论是，拥有更多的交换空间通常比更少好，尤其是在最新的内核上，并提倡机会主义的、主动的内存管理，而不是仅仅依赖 OOM killer。他提到需要更好的内存压力指标，目前正在 Facebook 开发，以促进更明智的调整。

---

## 38. 针织解剖

**原文标题**: Knitted Anatomy

**原文链接**: [https://www.knitted-anatomy.at/cardiovascular-system/](https://www.knitted-anatomy.at/cardiovascular-system/)

无法访问文章链接。

---

## 39. 黑客攻击扰乱运营，欧洲机场竞相修复值机故障

**原文标题**: European airports race to fix check-in glitch after hacking disruption

**原文链接**: [https://www.cnn.com/2025/09/21/europe/europe-airports-hack-operations-intl](https://www.cnn.com/2025/09/21/europe/europe-airports-hack-operations-intl)

由于针对RTX旗下科林斯宇航的黑客攻击事件，包括希思罗、柏林和布鲁塞尔在内的欧洲机场的自动值机系统于周六遭遇严重中断。旅客面临长时间排队、延误和取消。

虽然中断情况在周日已显著缓解，但一些延误仍然存在，地区监管机构正在调查此次黑客攻击的来源。RTX公司确认该问题是影响多家航空公司使用的MUSE软件的“网络相关中断”。

柏林勃兰登堡机场报告了持续存在的问题，但表示已采取手动解决方法，从而最大限度地减少了重大延误或取消。布鲁塞尔机场承认其航班时刻表受到重大影响，持续出现延误和取消。希思罗机场报告了持续的恢复工作，并指出大多数航班继续运营。

Cirium的分析表明，希思罗机场延误程度较低，柏林机场延误程度中等，布鲁塞尔机场延误程度较高，但呈下降趋势。该事件是近期一系列针对各个行业的网络攻击事件中的最新一起，凸显了人们对数字安全漏洞日益增长的担忧。

---

## 40. 逃逸验孕蛙在威尔士殖民50年 (2019)

**原文标题**: Escapee pregnancy test frogs colonised Wales for 50 years (2019)

**原文链接**: [https://www.bbc.com/news/uk-wales-44886585](https://www.bbc.com/news/uk-wales-44886585)

本文详述了非洲爪蟾的故事。这种青蛙最初被用于妊娠测试，后来从圈养环境中逃脱，并在南威尔士建立了繁殖地约50年。20世纪60年代初，这些青蛙，*Xenopus laevis*，在布里真德和格拉摩根谷地区找到了适宜的栖息地，1966年首次被记录到。

科学家和研究人员研究了这个种群，甚至在1981年至2010年间标记并释放了数千只青蛙。尽管这些青蛙能够在寒冷的气候中生存，但人们并未对其保护提出任何担忧。

到2008年，威尔士政府担心壶菌可能传播给本地两栖动物，于2010年启动了一项根除计划。然而，在计划完全实施之前，青蛙种群神秘地消失了。研究人员认为，2009年和2010年的严冬，包括干旱条件，导致蝌蚪数量锐减，并由于食物资源有限而加剧了同类相食。

虽然诱捕工作持续到2014年，但在2010年后仅捕获了一只青蛙。威尔士政府认为这些青蛙已从其主要栖息地被根除，但也承认在其他地方可能存在少量孤立的种群。尽管近期缺乏目击记录，但近年来并未进行调查以明确确认它们的消失。

---

## 41. 丹·布朗：人类从未创造出未被武器化的科技。

**原文标题**: Dan Brown: The human species has never created a technology it hasn't weaponized

**原文链接**: [https://english.elpais.com/culture/2025-09-21/dan-brown-the-human-species-has-never-created-a-technology-that-it-hasnt-weaponized.html](https://english.elpais.com/culture/2025-09-21/dan-brown-the-human-species-has-never-created-a-technology-that-it-hasnt-weaponized.html)

本文是对《达芬奇密码》等畅销惊悚小说作者丹·布朗的采访，探讨了他的新书《秘密的秘密》，以及他对宗教、科学和人性的不断演变的看法。

布朗的新书深入探讨了人类意识和濒死体验，探索了意识可能存在于身体之外的可能性。 这与他对科学挑战精神领域日益增长的兴趣有关，这与他早期作品中突出的宗教主题有所转变。 他对有组织的宗教表示怀疑，这源于他小时候对宗教教条的质疑的个人经历。

布朗认为，人类天生容易将技术武器化，使知识在缺乏善良的情况下变得危险。 他认为邪恶不如爱普遍，但指出当邪恶与权力结合时，其影响不成比例。 他还讨论了宗教与科学之间的冲突，认为科学的进步逐渐揭穿了宗教神话。

采访触及了布朗生活的个人方面，包括他的离婚以及与一位年轻女性的新订婚。 他强调了他对坚强、独立的女性的偏爱，这反映了他小说中的女性角色。 他还透露了他对哥斯达黎加的热爱，在那里他发现了缺乏物质主义和真正的联系。

最终，布朗将写作视为自我发现的旅程，使他能够探索复杂的问题并以易于理解的方式进行交流。 他强调在追求知识的过程中，感恩、同情和拥抱怀疑的重要性。

---

## 42. 女士的牛顿学 (1737) – 牛顿主义 vs. 笛卡尔主义

**原文标题**: Newton for Ladies (1737) – Newtonianism vs. Cartesianism

**原文链接**: [https://www.whipplelib.hps.cam.ac.uk/special/exhibitions-and-displays/exhibitions-archive/newton-and-newtonianism/ladies](https://www.whipplelib.hps.cam.ac.uk/special/exhibitions-and-displays/exhibitions-archive/newton-and-newtonianism/ladies)

弗朗切斯科·阿尔加罗蒂的《献给女士的牛顿》（1737年）以叙述者和侯爵夫人对话的形式写成，旨在通过将侯爵夫人从笛卡尔主义“转化”过来，普及牛顿主义。该书模仿丰特奈尔的笛卡尔对话录，展示了牛顿思想日益增长的统治地位。伊丽莎白·卡特后来将其翻译成英文，名为《艾萨克·牛顿爵士的光学理论》。

虽然阿尔加罗蒂的目标是娱乐和普及，而不是严谨的教学，这体现在书中收录了献给玛丽·沃特利·蒙塔古等人物的诗歌，但该文本侧重于光和颜色理论，避免了牛顿物理学中更复杂的机械方面。牛顿主义的这种性别化引发了人们对其女性形象塑造的质疑。

一些人认为，这本书将侯爵夫人描绘成知识的被动接受者，无法掌握复杂的理论，从而强化了传统的性别角色。另一些人则认为，它证明了女性既可以具有求知欲，又可以时尚，突显了社会变革的景象，即科学兴趣对女性来说变得更加可接受。《献给女士的牛顿》因此为了解科学思想的传播、女性在智力讨论中不断变化的角色以及18世纪笛卡尔主义和牛顿主义世界观之间的竞争提供了深刻的见解。

---

## 43. 他们以为他们是自由的 (1955)

**原文标题**: They Thought They Were Free (1955)

**原文链接**: [https://press.uchicago.edu/Misc/Chicago/511928.html](https://press.uchicago.edu/Misc/Chicago/511928.html)

在米尔顿·迈耶的《他们以为自己是自由的》中，一位德国语文学家反思了纳粹政权如何逐渐控制德国社会。他解释说，这个过程是微妙的，涉及通过保密、紧急措施和爱国主义呼吁，扩大政府与人民之间的差距。再加上持续不断的活动和干扰，使人们无法认识到周围发生的根本性变化。

这位语文学家承认，即使像他这样受过教育的人，也陷入了日常事务，缺乏时间和意愿去批判性地思考政权的轨迹。他强调，在没有预见到结局的情况下，很难抵制压迫的开始，而普通人很少具备这种远见。

他回忆说，微小的、渐进式的步骤使日益压迫性的措施正常化，使民众麻木，难以确定采取行动的时机。不确定性和缺乏公众抗议进一步阻止了个人发声，导致孤立和原则的逐渐丧失。

这位语文学家最后感叹了不作为造成的灾难性后果，强调了该政权最终、最可怕的行为之所以成为可能，是因为无数次较小妥协的累积效应。他描述了最终意识到道德堕落的全部程度，导致绝望、原则妥协或生活在羞耻中。赦免一名犹太男子的法官就是这个概念的具体例子。他还解释说，战争为政府提供了借口，使他们能够比以往任何时候都走得更远。

---

## 44. MapSCII – 终端中的世界地图

**原文标题**: MapSCII – World map in terminal

**原文链接**: [https://github.com/rastapasta/mapscii](https://github.com/rastapasta/mapscii)

MapSCII 是一个命令行工具，它使用盲文和 ASCII 字符在您的终端中渲染世界地图。它允许用户使用简单的命令或鼠标控制（如果支持）直接从控制台浏览地图。

主要功能包括：鼠标驱动的平移和缩放，兴趣点发现，支持 Mapbox Styles 的可自定义地图样式，连接到各种矢量瓦片服务器（包括优化的 OSM2VectorTiles），使用本地 VectorTile/MBTiles 的离线功能，以及与大多数 Linux 和 OSX 终端的兼容性。

该工具可以通过 `npm` (Node Package Manager) 或 `snap`（适用于 Linux 发行版）全局安装。基本用法包括简单地在终端中运行 `mapscii` 命令。键盘快捷键提供导航和控制，按 'q' 退出。

MapSCII 利用各种 JavaScript 库进行控制台操作（如 `x256`、`term-mouse` 和 `keypress`），矢量瓦片解析（`vector-tile`、`pbf`、`mbtiles`），空间索引和几何计算（`earcut`、`rbush`、`bresenham`、`simplify-js`）以及数据处理（`node-fetch`）。

该项目感谢 lukasmartinelli & manuelroth (OSM2VectorTiles) 和 mourner (GIS 算法) 的贡献。地图数据使用开放数据共享通用数据库许可 (ODbL)，制图根据知识共享署名-相同方式共享 2.0 (CC BY-SA) 许可。

---

## 45. 青少年嫌疑人在2023年拉斯维加斯赌场网络攻击案中自首

**原文标题**: Teen suspect surrenders in 2023 Las Vegas casino cyberattack case

**原文链接**: [https://www.casino.org/news/teen-suspect-surrenders-in-2023-las-vegas-strip-cyberattack-case/](https://www.casino.org/news/teen-suspect-surrenders-in-2023-las-vegas-strip-cyberattack-case/)

一名青少年嫌疑犯已向拉斯维加斯当局自首，他涉嫌参与了2023年针对多家拉斯维加斯赌场（包括米高梅国际度假集团和凯撒娱乐）的网络攻击。这些攻击被归咎于黑客组织“分散蜘蛛”，他们通过语音钓鱼获取了赌场内部系统的访问权限，造成了巨大的经济损失。

由于年龄原因，嫌疑人姓名未予公布，他面临六项重罪指控，包括获取个人信息、敲诈勒索和与计算机相关的犯罪行为。检察官正在寻求以成年人身份审判他。这次逮捕是联邦调查局对类似网络攻击进行更广泛调查的一部分，此前该调查导致四名男子被起诉。

据报道，米高梅拒绝支付赎金，损失估计达1亿美元，并遭受了严重的系统中断。相比之下，凯撒据称支付了3000万美元赎金要求中的1500万美元，受到的干扰较小。

---

## 46. 全息发光显示器

**原文标题**: Hololuminescent Display

**原文链接**: [https://lookingglassfactory.com/hld-overview](https://lookingglassfactory.com/hld-overview)

本文介绍了Looking Glass公司的新型显示技术——全息发光™显示器（HLD），该技术能够从标准的2D视频内容中创造出具有3D临场感的全息幻象。HLD旨在无需笨重设备即可在全息舞台上使角色、人物和产品栩栩如生，为沉浸式体验提供可扩展的解决方案。

HLD具有固定的全息蚀刻背景，并结合了高分辨率的4K屏幕，经过优化，可展示具有深度和维度的内容。该技术使用标准的2D工作流程，通过背景移除、阴影和反射来创造逼真的空间存在感。

该显示器有三种型号：16英寸、27英寸和86英寸，价格从1500美元到15000美元不等（限时预购享25%折扣）。所有型号均为纵向显示，并提供不同的分辨率和厚度，预计发货日期为2025年末和2026年初。

HLD专为各种应用而设计，包括在娱乐场所展示动画角色、为远程通信展示演示者以及改变零售环境中的产品演示。其目标是在娱乐、零售、博物馆和活动等行业进行安装、集成和激活。本文还提供了一个FAQ部分，解答关于HLD的常见问题和技术问题。

---

## 47. 均热板技术让iPhone 17 Pro保持低温

**原文标题**: Vapor chamber tech keeps iPhone 17 Pro cool

**原文链接**: [https://spectrum.ieee.org/iphone-17-pro-vapor-chamber](https://spectrum.ieee.org/iphone-17-pro-vapor-chamber)

苹果预计将在iPhone 17 Pro中采用均热板散热技术以控制温度，据Gwendolyn Rak在IEEE Spectrum上发表的文章称。这将使苹果与三星和谷歌等竞争对手保持一致，这些公司已经使用类似的方法来冷却其设备。文章强调，这种散热技术可能比像新iPhone颜色这样的表面变化更重要。本质上，文章表明苹果正在优先考虑内部改进，专注于通过温度调节来提升设备性能。

---

## 48. 循环神经网络是我们所需要的全部吗？一个GPU编程的视角

**原文标题**: Were RNNs all we needed? A GPU programming perspective

**原文链接**: [https://dhruvmsheth.github.io/projects/gpu_pogramming_curnn/](https://dhruvmsheth.github.io/projects/gpu_pogramming_curnn/)

本文总结了一个GPU编程项目，该项目基于论文“Were RNNs All We Needed?”，实现了并基准测试了可并行化的GRU和LSTM模型（“minGRU”和“minLSTM”）。其核心思想是通过简化RNN架构以消除隐藏状态之间的直接依赖性，它们的递归可以表达为适合并行扫描算法的形式，从而实现$O(\log T)$的并行处理，而不是$O(T)$的顺序处理。

作者比较了三种实现：CPU-seq（标准PyTorch循环）、CPU-scan（向量化的门计算但顺序扫描）和GPU-scan（带有并行Blelloch扫描的自定义CUDA实现）。在RTX 4090上的基准测试表明，对于短序列，由于优化的BLAS库和CUDA开销，CPU-scan有时更快。然而，对于较长的序列（$T > 8192$），GPU-scan的对数缩放占据主导地位，在$T=65,536$时实现了比CPU-scan快2倍的速度。

使用Nsight进行的GPU内核分析揭示了门计算中的初始瓶颈，这些瓶颈通过使用共享内存平铺将门计算融合到单个内核中得到解决。这使得瓶颈转移到最终的输出投影层（matvec_kernel），作者计划通过用单个cuBLAS GEMM调用替换多个内核启动来优化该层。

作者得出结论，该论文的论点成立：RNN可以通过递归重构进行并行化，从而为长序列带来显着的GPU性能提升。他们还参考了对该论文关于模型性能与Transformer相比的批评，并讨论了架构在深度学习中的更广泛作用。

---

## 49. DNS上的图像

**原文标题**: Images over DNS

**原文链接**: [https://dgl.cx/2025/09/images-over-dns](https://dgl.cx/2025/09/images-over-dns)

本文探讨了通过 DNS TXT 记录传输图像的可能性，并展示了如何绕过传统的 255 字节限制。作者解释说，虽然 TXT 记录中的单个字符串受到限制，但可以将多个字符串组合起来，从而允许更大的有效负载，尤其是在使用 TCP 而不是 UDP 进行 DNS 查询时。TCP 允许传输高达 64KB 的数据，而 UDP 只能传输约 1232 字节。

作者成功地使用 Google Public DNS 的 JSON API 和一个自定义的 Go 服务器来提供图像，该服务器通过 TCP 提供大型 TXT 响应。关键挑战在于处理 JSON 格式中的二进制数据，这需要自定义解析以避免 Base64 编码开销。作者演示了如何使用 `dig` 和 Perl 脚本检索和重构图像数据。

作者强调了这种技术的潜在安全隐患，指出攻击者可以通过 DNS 将大型有效负载隧道传输到浏览器，从而可能绕过 DNS 过滤，尤其是在 IP 地址证书日益普及的情况下。作者还讨论了将 DNS 递归缓存用作免费分布式 CDN 的可能性，尽管他们承认递归器可能会实施自适应 TTL 限制以防止滥用。服务器端代码主要由 ChatGPT 生成，但作者纠正了一些错误。作者最后将该项目定义为一种“可爱的黑客行为”，并侧重于该想法的新颖性。

---

## 50. Google Gemini 照片编辑提示示例

**原文标题**: Examples of Google Gemini Photo Editing Prompts

**原文链接**: [https://curateclick.com/blog/10-examples-of-google-gemini-photo-editing-prompt](https://curateclick.com/blog/10-examples-of-google-gemini-photo-editing-prompt)

本文探讨了 Google Gemini 的照片编辑功能，重点介绍了其 AI 如何根据自然语言提示转换图像。文章强调，清晰而具体的提示对于获得理想效果至关重要。

文章的核心部分提供了 10 个 Google Gemini 照片编辑提示的实用示例，包括编辑前后的图像、解释和最佳实践。这些例子包括：

1. **3D 手办：** 将照片转换为逼真的手办。
2. **宝丽来照片：** 创建复古宝丽来效果。
3. **戏剧性天空替换：** 用戏剧性的云景替换天空。
4. **情侣复古照片：** 将情侣照片转换为 20 世纪 90 年代的复古电影风格。
5. **AI 纱丽：** 为照片中的人物披上传统的印度纱丽。
6. **超现实主义艺术品：** 增强照片以达到超现实主义艺术品的质量。
7. **给他穿上这件衬衫：** 更换服装，同时保持逼真的贴合度。
8. **妆容分析 + 优化建议：** 提供视觉反馈和改进妆容的建议。
9. **涂鸦叠加：** 为照片添加创意手绘元素。
10. **姿势参考：** 在不同的图像之间转移姿势。

文章还提供了获得更好效果的高级技巧，包括迭代优化、结合多种技术、提示优化策略和批量处理建议。文章强调，从高质量的原始图像开始，并针对提示进行具体说明，对于获得最佳效果至关重要。最后，文章建议读者参考 nano banana 的提示和教程以获取更多灵感。

---

## 51. 那个缉毒署探员的“信用卡”可能正在窃听你

**原文标题**: That DEA agent's 'credit card' could be eavesdropping on you

**原文链接**: [https://www.independent.co.uk/news/world/americas/dea-surveillance-hidden-cameras-federal-law-enforcement-b2828606.html](https://www.independent.co.uk/news/world/americas/dea-surveillance-hidden-cameras-federal-law-enforcement-b2828606.html)

缉毒局购入信用卡式秘密录音录像设备，扩大隐蔽监控范围。采购数据显示，缉毒局从瑞士Nagra公司购买了57台此类设备：30台具备录音录像功能，27台仅具备录音功能。这些录音设备外观与普通信用卡无异，可定制印刷覆膜以通过近距离检查。它们配备16GB内存、内置麦克风和锂电池。

虽然缉毒局未明确说明这些设备的用途，但过往行动表明，它们可能被用于卧底行动，例如2022年逮捕一名被指控的雅库扎头目，他被诱骗至一场会面。此次采购还包括证件夹，暗示可能用作伪装身份证。

此次采购是缉毒局使用非常规监控方法这一更大趋势的一部分。此前，该机构曾将摄像头隐藏在路灯、工具箱和吸尘器等物品中，突显了其不断增强监控能力的努力。文章指出，缉毒局正日益侧重于协助移民和海关执法局进行驱逐行动。该机构尚未回应置评请求。

---

## 52. 英式钟乐的革新

**原文标题**: A revolution in English bell ringing

**原文链接**: [https://harpers.org/archive/2025/10/a-change-of-tune-veronique-greenwood-bell-ringing/](https://harpers.org/archive/2025/10/a-change-of-tune-veronique-greenwood-bell-ringing/)

薇罗妮克·格林伍德的文章《英国钟乐变革》很可能探讨了英国传统钟乐演奏发生的重大变化。这篇文章计划在2025年10月刊发表，预示着一场变革性的转变，可能会影响这种艺术形式的方法、技术或文化层面。

鉴于薇罗妮克·格林伍德作为作家和居住在英国的钟乐演奏者的背景，她对该主题带来了知识渊博且可能带有个人视角的观点。“钟乐”和“英国”的标签明确定义了文章的范围和地域重点。

“调整”和“分享”按钮的存在表明该文章旨在具有互动性，并鼓励读者参与内容并将其传播给他人。

本质上，这篇文章承诺探索英国钟乐演奏的开创性演变，作者对该主题非常熟悉。

---

## 53. 清洁氢正面临严峻的现实检验。

**原文标题**: Clean hydrogen is facing a big reality check

**原文链接**: [https://www.technologyreview.com/2025/09/18/1123818/hydrogen-reality-check-china/](https://www.technologyreview.com/2025/09/18/1123818/hydrogen-reality-check-china/)

文章《清洁氢能正面临严峻的现实检验》强调了当前影响清洁氢能行业的复杂性和挑战。尽管氢能被誉为能源转型的关键组成部分，但国际能源署（IEA）报告称，由于项目取消和延误，特别是美国和欧洲，对2030年清洁氢能产量的预期正在缩减。

文章强调了三个要点：

1.  **预期缩减：** 国际能源署已将其2030年清洁氢能产量预测从每年4900万吨下调至3700万吨，理由是多个地区取消了电解和碳捕获项目。
2.  **中国的主导地位：** 中国是电解槽制造和开发领域的领先力量，占全球产能的很大一部分。到本十年末，中国有望生产出具有成本竞争力的绿色氢能，这可能使其成为化石燃料制氢的有吸引力的替代品。
3.  **东南亚作为新兴市场：** 东南亚因其不断增长的经济、能源需求以及石油炼制和化工等行业中现有的氢能使用，为低排放氢能提供了一个有希望的市场。该地区主要的航运业也为氢能燃料提供了潜力。

总的来说，文章表明清洁氢能行业正面临现实检验，未来几年对于确定其可行性和成功实现雄心勃勃的气候目标至关重要。

---

## 54. 线程及线程简史

**原文标题**: A brief history of threads and threading

**原文链接**: [https://eclecticlight.co/2025/09/20/a-brief-history-of-threads-and-threading/](https://eclecticlight.co/2025/09/20/a-brief-history-of-threads-and-threading/)

本文概述了macOS上线程和线程的历史发展，从1984年初代 Macintosh 及其单处理器的局限性开始。它追溯了从一次只能运行一个应用程序到如今的Mac可以同时处理多个应用程序和后台任务的演变，这得益于多核处理器。

文章重点介绍了从Andy Hertzfeld的Switcher到MultiFinder的转变，后者在经典Mac OS中引入了协作式多任务处理，这是一种在程序之间快速切换以产生同时运行的错觉的方法。随后，A/UX以及后来的System 7.5.3引入了抢占式多任务处理，解决了行为不端的任务占用处理器的问题。

2000年PowerPC G4中多核处理器的引入标志着一个转折点，它可以使用各种线程类型（Mach、POSIX、Java、Cocoa）来管理跨多个内核的处理。进程、线程和任务在macOS环境中得到了明确的定义。

Mac OS X 10.6 Snow Leopard中的Grand Central Dispatch（GCD）是一项重大进步，它是一个调度器，用于管理任务队列并优化它们在多核系统上的执行。随着Apple Silicon Mac的出现，GCD现在管理性能（P）和效率（E）内核的线程，并根据服务质量（QoS）对任务进行优先级排序。

总而言之，本文记录了从单任务到现代macOS复杂线程功能的演变过程，从而可以优化多核处理器上多个任务和进程的性能。

---

## 55. 我不是机器人

**原文标题**: I’m Not a Robot

**原文链接**: [https://neal.fun/not-a-robot/](https://neal.fun/not-a-robot/)

无法访问文章链接。

---

## 56. 2025年评估：超越简单基准，构建人们可用的模型

**原文标题**: Evals in 2025: going beyond simple benchmarks to build models people can use

**原文链接**: [https://github.com/huggingface/evaluation-guidebook/blob/main/yearly_dives/2025-evaluations-for-useful-models.md](https://github.com/huggingface/evaluation-guidebook/blob/main/yearly_dives/2025-evaluations-for-useful-models.md)

2025年的评估：超越简单基准，构建人们可用的模型

---

## 57. 巴别鱼之后：网络速度下的廉价翻译前景

**原文标题**: After Babel Fish: The promise of cheap translations at the speed of the Web

**原文链接**: [https://hedgehogreview.com/issues/lessons-of-babel/articles/after-babel-fish](https://hedgehogreview.com/issues/lessons-of-babel/articles/after-babel-fish)

本文探讨了机器翻译（MT）的演变，从AltaVista的Babel Fish早期的承诺和缺陷开始。尽管Babel Fish提供了免费、即时的翻译，但正如翁贝托·埃科所强调的那样，其不准确性表明了机械同义词替换的局限性，以及在有效翻译中上下文和“世界知识”的重要性。

文章随后讨论了机器翻译的进步，特别是谷歌翻译的统计方法以及随后的神经网络升级和生成式人工智能，从而导致人们声称机器翻译对于像英语和西班牙语这样的高资源语言来说“几乎是一个已解决的问题”。然而，文章告诫人们不要抱有过高的期望，并指出在处理大量全球语言、许多语言的训练数据稀缺以及较长文本、习语表达和敏感语法问题中存在的持续性错误。

作者承认机器翻译在日常使用中的便利性和日益提高的准确性，尤其是在例行任务中，但对行业推动完全取代人工翻译的做法表示保留。虽然机器翻译擅长自动化可重复的流程，但复杂的翻译需要人类的细微差别、情境理解和文化意识。文章警告说，不要将翻译视为一项“只适合机器”的任务，并强调人类专业知识在确保跨语言和文化的准确和有意义的沟通方面的持久价值。

---

## 58. Mesda 工匠数据库

**原文标题**: Mesda Craftsman Database

**原文链接**: [http://test0.dlibrary.org/en/nodes/4066-craftsman-database](http://test0.dlibrary.org/en/nodes/4066-craftsman-database)

MESDA工匠数据库是一个宝贵的资源，包含1861年前南方早期（马里兰州、弗吉尼亚州、南北卡罗来纳州、佐治亚州、肯塔基州和田纳西州）工匠的信息。该数据库从报纸、名录、法院记录和私人文件等原始资料中收集，记录了127个行业的工匠信息。记录详细程度各异，提供了关于他们的工作、土地交易、重要统计数据、生产方法和销售的见解。

该数据库旨在收集并提供关于工匠生活和工作习惯的数据，并为众多博物馆展览、文章和书籍提供了信息。该数据库的一个独特之处在于其包容性方法，记录了妇女和非裔美国人（奴隶和自由人）的信息，并提供信息以帮助追踪工匠的迁徙。

虽然主要关注南方早期，但该数据库也包含一些来自新英格兰和大西洋中部各州的工匠，主要来自城市名录。MESDA正在不断扩充数据库，目前仅完成现有文件调查的一半。包含的信息只是包含50个结果的数据库结果的第一页，数据库每页最多可以显示200个结果。

---

## 59. 如果你擅长代码审查，你也会擅长使用AI代理。

**原文标题**: If you are good at code review, you will be good at using AI agents

**原文链接**: [https://www.seangoedecke.com/ai-agents-and-code-review/](https://www.seangoedecke.com/ai-agents-and-code-review/)

强大的代码审查能力是有效使用AI编码助手（如Claude Code、Codex和Copilot）的关键。本文认为，虽然这些工具可以生成大量代码，但它们往往缺乏经验丰富的软件工程师的判断力，并可能导致次优的设计选择。

作者通过其自身项目的例子说明了这一点，在这些项目中，AI助手提出了过于复杂的解决方案，例如逆向工程现有代码或在可以使用更简单替代方案时实施完整的后台作业基础设施。这些情况凸显了需要人工监督来引导AI朝着更高效和可维护的解决方案发展。

有效使用AI助手的核心在于结构化代码审查：不仅要关注编写的代码，还要关注*可以*编写的代码。这涉及超越直接的更改，并考虑更广泛的代码库上下文，以识别简化、重用和更好架构选择的机会。吹毛求疵的审查者可能会陷入细枝末节，而忽略了更大的图景，而橡皮图章式的审查者则过于信任AI。

作者认为我们正处于“人机混合象棋”模式中，人类和AI协同工作，而代码审查是成功指导这些助手的关键技能。这并非盲目地在所有地方采用AI，而是像指导初级工程师一样，对其进行智能的监督和指导。他们还思考了当前AI工具的快速发展是否可以与人类软件工程师在经验和效率方面的增长相提并论。

---

## 60. 许珀里翁：用于自定义事件的 Minecraft 游戏引擎

**原文标题**: Hyperion: Minecraft game engine for custom events

**原文链接**: [https://hyperion.rs/](https://hyperion.rs/)

Hyperion：为大规模定制活动稳定运行而设计的Minecraft游戏引擎。其核心优势在于稳定性，源于使用Rust构建。这使得活动组织者可以高度确信他们的活动不会被内存泄漏或段错误等常见问题中断，这些问题可能会困扰其他系统。本质上，Hyperion优先考虑大型定制Minecraft活动管理的稳定性和健壮性。

---

## 61. 克劳德有时可以证明这一点。

**原文标题**: Claude can sometimes prove it

**原文链接**: [https://www.galois.com/articles/claude-can-sometimes-prove-it](https://www.galois.com/articles/claude-can-sometimes-prove-it)

迈克·多兹的文章《克劳德（有时）可以证明它》探讨了Anthropic公司的Claude Code，一种AI编码代理，在交互式定理证明（ITP）方面的惊人能力，它可以使用像Lean这样的工具。虽然ITP通常具有复杂性和吹毛求疵的特点，即使对于专家来说也极具挑战性，但Claude Code却表现出完成复杂证明步骤的能力。

多兹强调，ITP除了证明定理之外，还需要各种技能，包括概念数学、将概念映射到Lean、分解定理和调试失败——类似于“证明工程”。他将此与SMT求解器等自动化推理工具进行了对比，后者范围有限但高度自动化。

Claude Code不同于简单的聊天机器人，它可以将复杂的任务分解为子任务，使其适用于软件工程，并且令人惊讶地适用于ITP。它可以分析代码、运行工具并提出解决方案，根据Lean编译器的反馈进行迭代。这种迭代过程，即代理尝试、失败并自我纠正，是其成功的原因。

多兹成功地使用Claude Code在Lean中形式化了一篇研究论文，充当“项目经理”来指导代理。虽然代理可以在形式化过程的各个级别工作，包括重构，但多兹指出，由于诸如抖动、持续性错误以及代理容易卡住等问题，AI辅助形式化比手动工作慢。然而，他认为更好的工具可以缓解这些问题。他总结说，尽管存在局限性，但Claude Code执行ITP的能力很有希望，并建议转向专门为AI代理设计工具，重点是提供详细的反馈，而不是避免失败。

---

## 62. 仰望U9 Xtreme 极速达496公里/小时，成为最快量产车

**原文标题**: Yangwang U9 Xtreme hits 308mph(496km/h), becomes fastest production car

**原文链接**: [https://www.topgear.com/car-news/electric/yangwang-u9-xtreme-hits-308mph-becomes-worlds-fastest-ever-production-car](https://www.topgear.com/car-news/electric/yangwang-u9-xtreme-hits-308mph-becomes-worlds-fastest-ever-production-car)

本文介绍了两个不同的汽车新闻。第一个引人注目的消息是量产车仰望U9 Xtreme达到了308英里/小时（496公里/小时）的最高速度。如果得到验证，这将使其成为世界上最快的量产车。 虽然文章提到了这一成就，但没有提供有关地点、条件或官方验证过程的详细信息。

文章的第二部分将重点转移到对“方程式传奇”的评论上，这很可能是一款与复古一级方程式赛车相关的游戏、纪录片或其他媒体。文章将此来源描述为“宝库”，表明它包含有关旧式F1赛车、车手和赛事的重要且有价值的信息。但是，该评论没有提供有关“方程式传奇”内容的具体细节。重点在于其整体价值以及对经典F1赛车爱好者的潜在价值。

---

## 63. 科马克·麦卡锡关于如何撰写科学论文的建议 (2019) [pdf]

**原文标题**: Cormac McCarthy's tips on how to write a science paper (2019) [pdf]

**原文链接**: [https://gwern.net/doc/science/2019-savage.pdf](https://gwern.net/doc/science/2019-savage.pdf)

无法总结所提供文本的内容。该文档似乎是以原始、编码格式表示的PDF文件（可能包括用于压缩的FlateDecode和DCTDecode过滤器）。这种格式并非人类可读，并且包含PDF阅读器应如何解释和渲染文件的指令，而不是文章本身的实际文本。如果没有工具来正确解码和解释PDF结构，就无法从科马克·麦卡锡那里提取关于撰写科学论文的所谓技巧。

---

## 64. 具有可再激活能量存储的活性微生物水泥超级电容器

**原文标题**: Living microbial cement supercapacitors with reactivatable energy storage

**原文链接**: [https://www.cell.com/cell-reports-physical-science/fulltext/S2666-3864(25)00409-6](https://www.cell.com/cell-reports-physical-science/fulltext/S2666-3864(25)00409-6)

无法访问文章链接。

---

## 65. 亚马逊将停止混储，此前品牌和卖家已投诉多年。

**原文标题**: Amazon to end commingling after years of complaints from brands and sellers

**原文链接**: [https://www.modernretail.co/operations/amazon-to-end-commingling-program-after-years-of-complaints-from-brands-and-sellers/](https://www.modernretail.co/operations/amazon-to-end-commingling-program-after-years-of-complaints-from-brands-and-sellers/)

亚马逊将停止其“混储”计划。该计划长期以来将不同卖家的相同商品混合存放于同一条形码下，多年来一直受到品牌和卖家的诟病。该决定在亚马逊加速卖家大会上宣布，获得了热烈掌声。

混储旨在加快交付速度并节省仓库空间，但却导致假冒或过期商品与正品混杂，损害了品牌声誉，并使追踪问题到特定卖家变得困难。结束该做法标志着亚马逊对品牌保护的承诺，以及摆脱转售商的举措。

亚马逊高管表示，由于物流网络的进步，混储的经济效益已不再有意义。该公司估计，由于混储系统，品牌所有者每年花费 6 亿美元重新粘贴产品标签。现在，在无需混合库存的情况下即可实现更快的运输速度，资源可以重新投资于卖家的增长。

Marketplace Pulse 的 Ben Donovan 等行业分析师认为，这是支持品牌的重要一步，使亚马逊成为对转售商更严峻的环境。这一举措符合亚马逊优先发展与主要品牌直接合作的战略，耐克恢复批发合作伙伴关系就是例证，该合作限制了独立转售商销售某些耐克商品。

虽然亚马逊大力推广其全新的人工智能卖家助手，但结束混储的决定在卖家中引起了更强烈的共鸣。混储的逐步淘汰计划定于今年晚些时候进行。

---

## 66. 大学不应只是收费站

**原文标题**: Universities should be more than toll gates

**原文链接**: [https://www.waliddib.com/posts/universities-should-be-more-than-toll-gates/](https://www.waliddib.com/posts/universities-should-be-more-than-toll-gates/)

作者反思其在约旦的环境工程教育经历，认为其更像是一个资格认证过程（“收费站”），而非真正的学习体验。他们批判了死记硬背的强调、无用的必修课程，以及大学作为输送劳动力到德国的“劳务传送带”的角色。他们的大学经历毫无启发性，这与他们在德国海外交流项目中所遇到的充满激情的学习环境形成了鲜明对比。

多年以后，受到哈佛CS50课程的启发，作者重新发现了独立学习的热爱，出于纯粹的好奇心探索了计算机科学、Arduino、游戏开发和API创建。然而，这种自主学习也带来了挫折感和因知识浩瀚而产生的不足感。

最终，作者重塑了他们对学习的看法。他们拥抱了自我教育的不完美性，接受遗忘和迷失方向是过程的一部分。他们得出结论，发现的乐趣和对新知识的追求才是主要目标，并渴望实现财务自由，以设计自己的终身课程，按照自己的方式学习。作者的经历突显了对大学体制的批判，即优先考虑资格认证而非真正的理解，以及充满激情、自主学习的潜力。

---

## 67. Slack每年向我们提高了19.5万美元的费用。

**原文标题**: Slack has raised our charges by $195k per year

**原文链接**: [https://skyfall.dev/posts/slack](https://skyfall.dev/posts/slack)

面向青少年提供编程教育的非营利组织 Hack Club 面临来自 Slack 的突如其来的大幅涨价。在使用 Slack 11 年后，即便在之前从免费非营利计划过渡后每年支付 5000 美元，Slack 仍要求立即支付 50000 美元，并持续每年支付 20 万美元，总计每年增加 19.5 万美元。若在一周内不遵守，工作区将被停用并删除数据。

作者认为，Slack 的母公司 Salesforce 的这一举动是不合理的，尤其是考虑到时间紧迫以及它给小型非营利组织带来的负担。直接影响是巨大的，迫使 Hack Club 的员工和志愿者紧急更新系统、重建集成并迁移多年的机构知识。

文章强调了数据所有权的重要性，促使 Hack Club 过渡到 Mattermost。作者鼓励其他小型企业因这次经历考虑从 Slack 迁移。

文章以积极的结尾结束。由于该帖子在 Hacker News 和 Twitter/X 上的广泛传播，Slack 的 CEO 联系了 Hack Club 并提供了一个解决方案，作者称该方案“比我们之前使用的计划更好”。虽然细节未公开，但作者对公众在解决问题方面的支持表示感谢。

---

## 68. Bazel and Glibc Versions

**原文标题**: Bazel and Glibc Versions

**原文链接**: [https://blogsystem5.substack.com/p/glibc-versions-bazel](https://blogsystem5.substack.com/p/glibc-versions-bazel)

生成摘要时出错

---

## 69. Less is safer: Reducing the risk of supply chain attacks

**原文标题**: Less is safer: Reducing the risk of supply chain attacks

**原文链接**: [https://obsidian.md/blog/less-is-safer/](https://obsidian.md/blog/less-is-safer/)

生成摘要时出错

---

## 70. Scream cipher

**原文标题**: Scream cipher

**原文链接**: [https://sethmlarson.dev/scream-cipher](https://sethmlarson.dev/scream-cipher)

生成摘要时出错

---

## 71. Solving a wooden puzzle using Haskell

**原文标题**: Solving a wooden puzzle using Haskell

**原文链接**: [https://glocq.github.io/en/blog/20250428/](https://glocq.github.io/en/blog/20250428/)

生成摘要时出错

---

## 72. 100% Repairable Laptop, DIY Project, Introductory First Video

**原文标题**: 100% Repairable Laptop, DIY Project, Introductory First Video

**原文链接**: [https://www.youtube.com/watch?v=kobUTW_QiII](https://www.youtube.com/watch?v=kobUTW_QiII)

生成摘要时出错

---

## 73. PyPI Blog: Token Exfiltration Campaign via GitHub Actions Workflows

**原文标题**: PyPI Blog: Token Exfiltration Campaign via GitHub Actions Workflows

**原文链接**: [https://blog.pypi.org/posts/2025-09-16-github-actions-token-exfiltration/](https://blog.pypi.org/posts/2025-09-16-github-actions-token-exfiltration/)

生成摘要时出错

---

## 74. The unbearable slowness of being: Why do we live at 10 bits/s? [pdf]

**原文标题**: The unbearable slowness of being: Why do we live at 10 bits/s? [pdf]

**原文链接**: [https://meisterlab.caltech.edu/documents/30100/Zheng_2024_The_unbearable_slowness_of_being-_Why_do_we_live_at_10_bitss.pdf](https://meisterlab.caltech.edu/documents/30100/Zheng_2024_The_unbearable_slowness_of_being-_Why_do_we_live_at_10_bitss.pdf)

生成摘要时出错

---

## 75. Representing Heterogeneous Data (2023)

**原文标题**: Representing Heterogeneous Data (2023)

**原文链接**: [https://journal.stuffwithstuff.com/2023/08/04/representing-heterogeneous-data/](https://journal.stuffwithstuff.com/2023/08/04/representing-heterogeneous-data/)

生成摘要时出错

---

## 76. I once appeared in The Old New Thing

**原文标题**: I once appeared in The Old New Thing

**原文链接**: [https://mtlynch.io/my-old-new-thing-cameo/](https://mtlynch.io/my-old-new-thing-cameo/)

生成摘要时出错

---

## 77. US companies laid off 40k+ US tech workers, replaced them with H-1B visa holders

**原文标题**: US companies laid off 40k+ US tech workers, replaced them with H-1B visa holders

**原文链接**: [https://www.hindustantimes.com/world-news/american-companies-laid-off-over-40-000-us-tech-workers-replaced-them-with-h-1b-visa-holders-white-house-101758431251767.html](https://www.hindustantimes.com/world-news/american-companies-laid-off-over-40-000-us-tech-workers-replaced-them-with-h-1b-visa-holders-white-house-101758431251767.html)

生成摘要时出错

---

## 78. LLM-Deflate: Extracting LLMs into Datasets

**原文标题**: LLM-Deflate: Extracting LLMs into Datasets

**原文链接**: [https://www.scalarlm.com/blog/llm-deflate-extracting-llms-into-datasets/](https://www.scalarlm.com/blog/llm-deflate-extracting-llms-into-datasets/)

生成摘要时出错

---

## 79. Dynamo AI (YC W22) Is Hiring a Senior Kubernetes Engineer

**原文标题**: Dynamo AI (YC W22) Is Hiring a Senior Kubernetes Engineer

**原文链接**: [https://www.ycombinator.com/companies/dynamo-ai/jobs/fU1oC9q-senior-kubernetes-engineer](https://www.ycombinator.com/companies/dynamo-ai/jobs/fU1oC9q-senior-kubernetes-engineer)

生成摘要时出错

---

## 80. Bezier Curve as Easing Function in C++

**原文标题**: Bezier Curve as Easing Function in C++

**原文链接**: [https://asawicki.info/news_1790_bezier_curve_as_easing_function_in_c](https://asawicki.info/news_1790_bezier_curve_as_easing_function_in_c)

生成摘要时出错

---

## 81. PYREX vs. pyrex: What's the difference?

**原文标题**: PYREX vs. pyrex: What's the difference?

**原文链接**: [https://www.corning.com/worldwide/en/products/life-sciences/resources/stories/in-the-field/pyrex-vs-pyrex-whats-the-difference.html](https://www.corning.com/worldwide/en/products/life-sciences/resources/stories/in-the-field/pyrex-vs-pyrex-whats-the-difference.html)

生成摘要时出错

---

## 82. Nostr

**原文标题**: Nostr

**原文链接**: [https://nostr.com/](https://nostr.com/)

生成摘要时出错

---

## 83. The best YouTube downloaders, and how Google silenced the press

**原文标题**: The best YouTube downloaders, and how Google silenced the press

**原文链接**: [https://windowsread.me/p/best-youtube-downloaders](https://windowsread.me/p/best-youtube-downloaders)

生成摘要时出错

---

## 84. Want to piss off your IT department? Are the links not malicious looking enough?

**原文标题**: Want to piss off your IT department? Are the links not malicious looking enough?

**原文链接**: [https://phishyurl.com/](https://phishyurl.com/)

生成摘要时出错

---

## 85. Is Zig's new writer unsafe?

**原文标题**: Is Zig's new writer unsafe?

**原文链接**: [https://www.openmymind.net/Is-Zigs-New-Io-Unsafe/](https://www.openmymind.net/Is-Zigs-New-Io-Unsafe/)

生成摘要时出错

---

## 86. Are touchscreens in cars dangerous?

**原文标题**: Are touchscreens in cars dangerous?

**原文链接**: [https://www.economist.com/science-and-technology/2025/09/19/are-touchscreens-in-cars-dangerous](https://www.economist.com/science-and-technology/2025/09/19/are-touchscreens-in-cars-dangerous)

生成摘要时出错

---

## 87. TV Time Machine: A Raspberry Pi That Plays Random 90s TV

**原文标题**: TV Time Machine: A Raspberry Pi That Plays Random 90s TV

**原文链接**: [https://quarters.captaintouch.com/blog/posts/2025-09-20-tv-time-machine-a-raspberry-pi-that-plays-random-90s-tv.html](https://quarters.captaintouch.com/blog/posts/2025-09-20-tv-time-machine-a-raspberry-pi-that-plays-random-90s-tv.html)

生成摘要时出错

---

## 88. Overcoming barriers of hydrogen storage with a low-temperature hydrogen battery

**原文标题**: Overcoming barriers of hydrogen storage with a low-temperature hydrogen battery

**原文链接**: [https://www.isct.ac.jp/en/news/okmktjxyrvdc](https://www.isct.ac.jp/en/news/okmktjxyrvdc)

生成摘要时出错

---

## 89. Git: Introduce Rust and announce it will become mandatory in the build system

**原文标题**: Git: Introduce Rust and announce it will become mandatory in the build system

**原文链接**: [https://lore.kernel.org/git/20250904-b4-pks-rust-breaking-change-v1-0-3af1d25e0be9@pks.im/](https://lore.kernel.org/git/20250904-b4-pks-rust-breaking-change-v1-0-3af1d25e0be9@pks.im/)

生成摘要时出错

---

## 90. Plausibility is not truth: Do you really understand AI?

**原文标题**: Plausibility is not truth: Do you really understand AI?

**原文链接**: [https://thecritic.co.uk/plausibility-is-not-truth/](https://thecritic.co.uk/plausibility-is-not-truth/)

生成摘要时出错

---

## 91. Why do some gamers invert their controls?

**原文标题**: Why do some gamers invert their controls?

**原文链接**: [https://www.theguardian.com/games/2025/sep/18/why-do-some-gamers-invert-their-controls-scientists-now-have-answers-but-theyre-not-what-you-think](https://www.theguardian.com/games/2025/sep/18/why-do-some-gamers-invert-their-controls-scientists-now-have-answers-but-theyre-not-what-you-think)

生成摘要时出错

---

## 92. Systemd can be a cause of restrictions on daemons

**原文标题**: Systemd can be a cause of restrictions on daemons

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/linux/SystemdCanBeRestrictionCause](https://utcc.utoronto.ca/~cks/space/blog/linux/SystemdCanBeRestrictionCause)

生成摘要时出错

---

## 93. Node 20 will be deprecated on GitHub Actions runners

**原文标题**: Node 20 will be deprecated on GitHub Actions runners

**原文链接**: [https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/](https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/)

生成摘要时出错

---

## 94. Thoth Blueprint: software to visualize and modify database schema

**原文标题**: Thoth Blueprint: software to visualize and modify database schema

**原文链接**: [https://github.com/AHS12/thoth-blueprint](https://github.com/AHS12/thoth-blueprint)

生成摘要时出错

---

## 95. Multi-Kernel Architecture Proposed for the Linux Kernel

**原文标题**: Multi-Kernel Architecture Proposed for the Linux Kernel

**原文链接**: [https://www.phoronix.com/news/Linux-Multi-Kernel-Patches](https://www.phoronix.com/news/Linux-Multi-Kernel-Patches)

生成摘要时出错

---

## 96. 对象存储的高性能透读缓存

**原文标题**: High-performance read-through cache for object storage

**原文链接**: [https://github.com/s2-streamstore/cachey](https://github.com/s2-streamstore/cachey)

生成摘要时出错

---

## 97. Help us raise $200k to free JavaScript from Oracle

**原文标题**: Help us raise $200k to free JavaScript from Oracle

**原文链接**: [https://deno.com/blog/javascript-tm-gofundme](https://deno.com/blog/javascript-tm-gofundme)

生成摘要时出错

---

## 98. The SAT Game

**原文标题**: The SAT Game

**原文链接**: [https://www.cril.univ-artois.fr/~roussel/satgame/satgame.php?level=5&lang=eng](https://www.cril.univ-artois.fr/~roussel/satgame/satgame.php?level=5&lang=eng)

生成摘要时出错

---

## 99. Nvidia buys $5B in Intel

**原文标题**: Nvidia buys $5B in Intel

**原文链接**: [https://www.tomshardware.com/pc-components/cpus/nvidia-and-intel-announce-jointly-developed-intel-x86-rtx-socs-for-pcs-with-nvidia-graphics-also-custom-nvidia-data-center-x86-processors-nvidia-buys-usd5-billion-in-intel-stock-in-seismic-deal](https://www.tomshardware.com/pc-components/cpus/nvidia-and-intel-announce-jointly-developed-intel-x86-rtx-socs-for-pcs-with-nvidia-graphics-also-custom-nvidia-data-center-x86-processors-nvidia-buys-usd5-billion-in-intel-stock-in-seismic-deal)

生成摘要时出错

---

## 100. Show the Physics

**原文标题**: Show the Physics

**原文链接**: [https://interactivetextbooks.tudelft.nl/showthephysics/Introduction/About.html](https://interactivetextbooks.tudelft.nl/showthephysics/Introduction/About.html)

生成摘要时出错

---

