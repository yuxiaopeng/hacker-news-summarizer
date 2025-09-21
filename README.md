# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-09-21.md)

*最后自动更新时间: 2025-09-21 17:43:53*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 2 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 3 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 4 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 5 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 6 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 7 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 8 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 9 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 10 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 11 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 12 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 13 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 14 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 15 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 16 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 17 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 18 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 19 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 20 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 21 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 22 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 23 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 24 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 25 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 26 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 27 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 28 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 29 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 30 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 31 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 32 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 33 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 34 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 35 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 36 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 37 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 38 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 39 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 40 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 41 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 42 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 43 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 44 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 45 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 46 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 47 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 48 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 49 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 50 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 51 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 52 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 53 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 54 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 55 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 56 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 57 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 58 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 59 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 60 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 61 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 62 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 63 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 64 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 65 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 66 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 67 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 68 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 69 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 70 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 71 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 72 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 73 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 74 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 75 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 76 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 77 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 78 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 79 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 80 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 81 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 82 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 83 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 84 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 85 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 86 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 87 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 88 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 89 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 90 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 91 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 92 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 93 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 94 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 95 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 96 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 97 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 98 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 99 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 100 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 101 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 102 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 103 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 104 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 105 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 106 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 107 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 108 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 109 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 110 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 111 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 112 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 113 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 114 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 115 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 116 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 117 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 118 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 119 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 120 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 121 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 122 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 123 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 124 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 125 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 126 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 127 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 128 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 129 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 130 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 131 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 132 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 133 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 134 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 135 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 136 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 137 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 138 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 139 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 140 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 141 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 142 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 143 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 144 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 145 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 146 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 147 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 148 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 149 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 150 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 151 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 152 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 153 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 154 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 155 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 156 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 157 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 158 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 159 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 160 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 161 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 162 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 163 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 164 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 165 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 166 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 167 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 168 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 169 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 170 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 171 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 172 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 173 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 174 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 175 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 176 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 177 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 178 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 179 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 180 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 181 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 182 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 183 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 184 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 185 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 186 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
