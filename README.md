# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-05-05.md)

*最后自动更新时间: 2025-05-05 17:50:00*
## 1. 展示一下：VectorVFS，将你的文件系统作为向量数据库

**原文标题**: Show HN: VectorVFS, your filesystem as a vector database

**原文链接**: [https://vectorvfs.readthedocs.io/en/latest/](https://vectorvfs.readthedocs.io/en/latest/)

VectorVFS：将 Linux 文件系统转换为向量数据库。它利用虚拟文件系统 (VFS) 扩展属性将向量嵌入直接存储在文件中，无需单独的索引或外部数据库。这使得现有的目录结构能够作为语义可搜索的嵌入存储。

初始版本专注于支持 Meta 的感知编码器 (PE) 以进行图像嵌入，声称在零样本图像任务方面优于 InternVL3 和 Qwen2.5VL 等模型。虽然同时支持 CPU 和 GPU，但建议对大型图像集合使用 GPU 加速，以加快初始嵌入过程。

主要功能包括零开销索引、基于嵌入相似性的文件无缝检索、对不同嵌入模型的灵活支持，以及基于原生 Linux VFS 功能构建的轻量级和可移植设计。该软件包利用每个文件上的扩展属性 (xattrs) 来存储嵌入。该文档还详细介绍了安装说明、提供的“vfs”脚本的使用、包括 inode 理解和 Ext4 文件系统中的扩展属性存储在内的设计架构，以及关于“vfs search”命令的详细信息。

---

## 2. 白日梦之死：当手机带走无聊时，我们失去了什么

**原文标题**: The Death of Daydreaming: What we lose when phones take away boredom

**原文链接**: [https://www.afterbabel.com/p/on-the-death-of-daydreaming](https://www.afterbabel.com/p/on-the-death-of-daydreaming)

克里斯汀·罗森的文章《白日梦之死》探讨了我们持续依赖智能手机来缓解无聊所带来的负面后果。她认为，虽然智能手机提供了即时满足和刺激，但它们也导致焦虑、抑郁和孤独的发生率上升，并削弱了我们做白日梦、练习耐心和体验期待的能力。

罗森将她自己X世代的童年（那时无聊很常见且被接受）与当今由于技术的普及而认为儿童不应该感到无聊的期望进行了对比。她强调，智能手机已经占据了间隙时间——一天中零星的安静反思时刻——并用持续的干扰取代了它。

罗森引用了皮尤的研究，指出智能手机使用的普遍性和面对面社交互动的减少。她认为，这种持续的刺激，看似优化了我们的体验，却降低了我们的注意力、同理心和情绪调节能力。

这篇文章还涉及了文化上对效率高于一切的推崇，导致对闲散的怀疑。罗森认为，闲散时刻对于反思和更新至关重要，并建议收回我们的闲暇时间并远离屏幕可以提高我们日常生活的质量。最终，白日梦的丧失，作为这种持续连接的副产品，对创造力产生了负面影响。

---

## 3. 没有Instagram，没有隐私

**原文标题**: No Instagram, No Privacy

**原文链接**: [https://blog.wouterjanleys.com/blog/no-instagram-no-privacy/](https://blog.wouterjanleys.com/blog/no-instagram-no-privacy/)

即使没有Instagram账号，讽刺的隐私缺失

本文探讨了一个讽刺现象：即使没有Instagram账号，作者仍然体验到隐私的缺失。虽然避免了个人广播的压力，但作者仍然间接受到他人发布关于他们共同活动的影响。

作者和妻子过着社交生活，朋友们经常来来往往，他们注意到人们常常通过他人的Instagram帖子了解他们生活的细节。这引发了对信息传递方式和潜在误解的担忧。作者指出，在线帖子缺乏面对面谈话的细微差别和敏感性，可能造成无意的伤害，尤其是在将某些人排除在共同经历之外时。

虽然庆幸能够避免管理自己在线形象的压力，但作者承认，知道自己的行踪和行为可能在未经同意或控制的情况下被记录和分享，感到不安。这引出了对隐私的思考，将其定义为“控制他人对你的了解”。与大型公司收集个人数据相比，作者对这种无法控制朋友们了解的信息的情况感到更加不安。

文章最后，作者思考潜在的解决方案，例如一种社交礼仪，不鼓励公开发布关于私人聚会的帖子。与此同时，作者承认了幸福无知的益处，使他们能够投入到人际关系中，而不会受到潜在的社交媒体引发的失望情绪的干扰。作者表达了希望，尽管在线帖子可能产生误解，友谊仍能长存。

---

## 4. Show HN: TextQuery – 用 SQL 查询 CSV、JSON、XLSX 文件

**原文标题**: Show HN: TextQuery – Query CSV, JSON, XLSX Files with SQL

**原文链接**: [https://textquery.app/](https://textquery.app/)

TextQuery：一款桌面应用程序，旨在简化数据分析，允许用户使用 SQL 查询 CSV、JSON 和 XLSX 文件。它提供了一个用户友好的界面，无需定义模式或编码即可导入数据。支持的格式包括 .xlsx、.xls、.csv、.tsv、.json、.jsonld、.zip、.gz、.tgz 和 .tar。

该应用程序具有强大的 SQL 编辑器，具备自动完成、查询历史、格式化和多项选择功能。用户可以创建可定制的图表（折线图、柱状图、面积图、散点图、饼图），并导出或直接分享。

TextQuery 提供多项周到的功能，以实现高效的工作流程，包括内联编辑器、过滤器、用于管理多个查询和表格的选项卡，以及各种格式（CSV、JSON、Excel、SQL）的数据导出。

该软件提供一流的桌面体验，一次性购买即可获得永久许可证和免费更新。它在构建时考虑了隐私和安全性，不会记录或传输用户数据。常用功能可通过键盘快捷键访问，并且该应用程序会根据用户反馈不断改进。提供具有限制的免费版本用于评估，并可以选择升级到 Pro 版本。

---

## 5. 几何理解反函数微积分（2023）

**原文标题**: Geometrically understanding calculus of inverse functions (2023)

**原文链接**: [https://tobylam.xyz/2023/11/27/inverse-functions-legendre-part-1](https://tobylam.xyz/2023/11/27/inverse-functions-legendre-part-1)

本文探讨了从几何角度理解反函数的微积分，特别是导数和积分。它避免了死记硬背公式的应用，强调直觉。

对于导数，本文回顾了反函数定理（IFT），并通过关于直线 y=x 的反射进行几何说明。原始函数 f(x) 上的切线镜像成为其反函数 f⁻¹(x) 上的切线，斜率倒置。本文还提出了图变换的视角，突出了映射 (x, y) -> (y, x) 如何将 f(x) 的图转换为 f⁻¹(x) 的图。

对于积分，本文采用了类似的几何方法，利用勒让德变换。该变换应用于函数的积分，提供了一种确定其反函数的积分的方法。它展示了如何反射导数的图来帮助找到反函数的原函数。本文详细推导了勒让德变换，并将其应用于计算 ln(x) 和 arctan(x) 的积分，从它们对应的非反函数的积分出发，从而提供了一种思考反函数积分的新方法。

总而言之，本文使用几何解释和勒让德变换来理解反函数的导数和积分，提供了一种视觉和概念性的替代方案，以替代基于标准公式的方法。

---

## 6. 泰克TDS 684B示波器采用CCD模拟存储器

**原文标题**: A Tektronix TDS 684B Oscilloscope Uses CCD Analog Memory

**原文链接**: [https://tomverbeure.github.io/2025/05/04/TDS684B-CCD-Memory.html](https://tomverbeure.github.io/2025/05/04/TDS684B-CCD-Memory.html)

本文探讨了泰克TDS 684B示波器的内部运作原理，重点关注其在20世纪90年代的高采样率能力。作者低价购得该示波器，并研究了其如何在15k小容量存储器的限制下实现5 Gsps的采样率。

TDS 684B由采集板和CPU板组成。采集板包含模拟前端、信号调理、模数转换和存储器。核心发现是使用CCD（电荷耦合器件）作为模拟存储缓冲器。这使得示波器能够以非常高的速率（高达5 GHz）捕获数据，然后以相对较慢的速率（25 MHz）将其读出到8位ADC。

测量结果证实，在CCD缓冲器之后，ADC的采样频率要低得多（约8 MHz）。测试还表明，无论设置的采集长度如何，示波器总是采集大约完整的CCD存储器（约16k个样本），并在选择较小样本大小时丢弃数据。作者观察到采样信号的不连续性，表明CCD存储器不是线性扫描的。尽管ADC的输入噪声较大，但CRT上显示的信号却很干净，作者无法解释这一现象。

---

## 7. Instant (YC S22) 正在招聘创始 TypeScript 工程师

**原文标题**: Instant (YC S22) Is Hiring a Founding TypeScript Engineer

**原文链接**: [https://www.instantdb.com/hiring/ts-hacker](https://www.instantdb.com/hiring/ts-hacker)

Instant（YC S22）正在寻找一位创始TypeScript工程师加入其位于旧金山的4人团队。Instant正在构建一个类似于Firebase和Supabase的实时前端数据库，旨在为Figma和Notion等复杂应用提供卓越的同步引擎。

理想的候选人应热衷于类型人体工程学，乐于构建用户界面，并对构建强大的同步引擎充满热情。该职位涉及改进TypeScript类型定义以获得更好的开发者体验（自动完成、安全性），增强Instant CLI工具和仪表板的UI/UX（迁移、沙箱、浏览器），以及优化SDK中的客户端数据库（连接、索引、自省、本地存储、重新渲染）。

该团队由来自Facebook、Airbnb和Wit.ai的创始人和工程师组成，重视正直、乐观和以原则为导向的黑客。虽然后端开发主要使用Clojure和Postgres，但扎实的TypeScript背景至关重要。Instant强调快节奏、协作和以用户为中心的环境。

薪酬包括0.5%-2%的股权（滑动比例）和15万至20万美元的基本工资，以及医疗、牙科和视力福利。该职位要求在旧金山进行现场工作或搬迁至旧金山。有兴趣的候选人请发送简短的介绍和他们参与过的项目至founders@instantdb.com。具有TypeScript库经验者优先。

---

## 8. 2025年网络罪犯如何发财？

**原文标题**: How are cyber criminals rolling in 2025?

**原文链接**: [https://vin01.github.io/piptagole/cybcecrime/security/cybersecurity/2025/05/05/state-cyber-security.html](https://vin01.github.io/piptagole/cybcecrime/security/cybersecurity/2025/05/05/state-cyber-security.html)

本文探讨网络犯罪分子在2025年可能采取的行动方式，重点关注他们分发恶意链接和规避安全措施的方法。他们不再直接托管恶意内容，而是利用合法网站和平台的漏洞来创建重定向链，最终指向联盟网络和钓鱼网站。

文章强调，攻击者利用政府网站、大学和谷歌服务（例如Looker Studio）等可信平台作为免费托管和重定向点。他们利用常见的安全漏洞，如过时的WordPress插件、缓存中毒、撞库攻击和悬挂DNS记录来入侵这些站点。

目标内容通常围绕流行的在线需求，如“免费”Robux币、OnlyFans账号、亚马逊礼品卡和免费电影，吸引了大量容易受到网络钓鱼诈骗的受众。

一个重要的结论是，传统的安全措施，如杀毒软件、VPN和允许域名列表通常是无效的。犯罪分子擅长操纵链接信誉分析，并将恶意链接隐藏在可信域名中。

文章强调，这些攻击主要由联盟营销和网络钓鱼的盈利驱动。目标是通过每次重定向赚取少量资金，同时试图窃取凭据，特别是来自寻求游戏币的儿童的凭据。这个问题并不新鲜，几年前就有类似的事件报道。作者还谈到了向受影响方报告这些漏洞的困难，因为他们不一定能及时响应或保持透明。

---

## 9. AWS 构建了一款安全工具，却带来了安全风险。

**原文标题**: AWS Built a Security Tool. It Introduced a Security Risk

**原文链接**: [https://www.token.security/blog/aws-built-a-security-tool-it-introduced-a-security-risk](https://www.token.security/blog/aws-built-a-security-tool-it-introduced-a-security-risk)

本文详细介绍了一个由 AWS 自身AWS Organizations 账户评估工具无意中引入的权限提升风险。该工具旨在审计跨账户访问，但它建议用户在安全性较低的 AWS 账户中（而不是管理账户）部署其中心“hub”角色，从而创建了从不安全环境（如开发环境）到高度敏感环境（如生产环境和管理账户）的危险信任路径。

Token Security 的安全研究人员发现，通过在安全性较低的账户中部署 hub 角色，攻击者一旦攻陷该账户，就可以代入其他更敏感账户中的角色，从而获得对关键资源的访问权限。攻击者可以枚举 IAM 角色、策略、S3 存储桶和 KMS 密钥。

本文解释了这些风险，并提供了组织检测是否受到影响的方法，包括检查该工具创建的特定 IAM 角色并检查其创建日期。文章建议卸载该工具，并在与管理账户安全性相当的高安全性账户中重新部署 hub 角色。

Token Security 向 AWS 报告了该问题，AWS 迅速承认了这一问题，并在 2025 年 1 月 28 日更新了其文档，明确建议在高安全性账户中部署 hub 角色。本文强调了理解 AWS 中的信任关系的重要性，以及看似简单的配置如何造成重大的安全漏洞。文章最后推广了 Token Security 的平台，用于检测信任策略风险。

---

## 10. 蠢朋克的音效

**原文标题**: The vocal effects of Daft Punk

**原文链接**: [https://bjango.com/articles/daftpunkvocaleffects/](https://bjango.com/articles/daftpunkvocaleffects/)

本文深入探讨Daft Punk使用的声音效果，旨在识别其标志性机器人声音背后的特定硬件和技术。文章消除了常见的误解，例如DigiTech Vocalist是声码器，并强调了声码器之外的各种效果的使用，包括对讲盒和和声器。

作者根据访谈和个人实验，确定了各种音轨上使用的特定设备。Homework依赖于 Roland SVC-350 和 Ensoniq DP/4+，而 Discovery 则包含了 Auto-Tune、DigiTech Vocalist 和 Talker。Human After All 大量依赖 DigiTech Talker。Random Access Memories 大量展示了 Sennheiser VSM201，以及对讲盒和 Auto-Tune。

文章解释了对讲盒、声码器和和声器之间的区别。对讲盒用嘴物理地塑造声音，声码器用调制器（声音）过滤载波信号（如合成器），而和声器则以数字方式改变单个音频源的音高。

作者还讨论了声码器的历史，重点介绍了标志性型号以及其他艺术家的使用情况。他们研究了 DigiTech Talker 的谱系及其与 IVL Technologies 和 TC Helicon 的联系。他们还证实 Imogen Heap 使用了 DigiTech Vocalist Workstation EX 来创作 Hide and Seek。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 2 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 3 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 4 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 5 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 6 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 7 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 8 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 9 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 10 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 11 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 12 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 13 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 14 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 15 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 16 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 17 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 18 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 19 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 20 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 21 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 22 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 23 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 24 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 25 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 26 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 27 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 28 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 29 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 30 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 31 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 32 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 33 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 34 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 35 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 36 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 37 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 38 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 39 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 40 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 41 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 42 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 43 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 44 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 45 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 46 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 47 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
