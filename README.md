# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-08-23.md)

*最后自动更新时间: 2026-08-23 17:46:20*
## 1. GLM-5.3 (开源权重) 以 1/5 的成本击败了 Anthropic/OpenAI 模型

**原文标题**: GLM-5.3 (open-weight) beat Anthropic/OpenAI models – for 1/5 the cost

**原文链接**: [https://reinvently.co.uk/tools/ed-o-meter/](https://reinvently.co.uk/tools/ed-o-meter/)

2026年8月的“Ed-o-meter”排行榜结果显示，AI领域发生了重大转变：权重开放模型 **GLM-5.3** 的表现超越了来自 OpenAI 和 Anthropic 的主要闭源模型。

该基准测试通过五个类别的28项实际任务对模型进行了评估，包括：编程（Coding）、数据（Data）、现实场景（Realworld）、安全（Security）和工具使用（Tool-use）。主要发现包括：

*   **GLM-5.3 表现最佳：** 它是首个在所有五个类别中均实现 100% 通过率的模型。尽管其中值首词响应时间（16.3秒）较慢，但其整套测试方案的成本仅为 0.28 美元，约为 **GPT-5.5**（1.43 美元）的五分之一，而后者在现实场景任务中的通过率仅为 89%。
*   **安全过滤器问题：** Anthropic 的 **Claude 5** 系列（Fable 和 Opus）因过于激进的安全过滤器而受到严重影响。两款模型都拒绝了无害的编程调试任务，导致“测试轮次”失败。尽管存在拒绝现象，Opus-5 仍保持了 9.4 分的高质量评分。
*   **OpenAI 的权衡：** **GPT-5.6** 系列（Luna、Terra 和 Sol）提供了极高的速度和最低的成本（Luna 完成整轮测试仅需 0.064 美元）。然而，它们未能通过安全基准测试，在多达 50% 的测试中被成功“越狱”。
*   **细分领域领先者：** **Kimi-K3** 拥有最高的高质量评分（9.5分），但受限于极高的延迟（26.4秒）。在高速可靠性方面，**Haiku-4.5** 表现出色，拥有 96% 的通过率和近乎瞬时的 0.9 秒响应时间。

报告总结道，对于优先考虑准确性和安全性而非速度的用户来说，GLM-5.3 是目前的“全能”冠军，其成本仅为竞品闭源模型的一小部分，却提供了顶尖的性能表现。

---

## 2. 我花了266美元和四个AI模型才搞定我的平板，而GLM-5.3仅用一天就完成了。

**原文标题**: I spent $266 and four AI models to own my tablet. GLM-5.3 finished it in a day

**原文链接**: [https://ericpardee.github.io/fire-hd-ownership/](https://ericpardee.github.io/fire-hd-ownership/)

文章描述了一位技术专家利用多个先进 AI 模型获取亚马逊 Fire HD 10 平板电脑 root 权限的历程。他最终在 API 调用和订阅上花费了 266 美元，成功解决了持续自动关机的问题。

**问题背景**
作者的平板电脑被用作智能家居控制面板，但由于亚马逊内部软件的原因，开始频繁关机。由于相关软件包受系统保护，禁用这些服务的常规方法均告失败，必须获得 root 权限才能进行修改。此外，该 2021 款机型当时并无公开的 root 方法。

**AI 协作过程**
*   **Claude：** 经过数月的诊断，Claude 的网络安全防护机制最终阻止了作者的进一步技术工作，拒绝协助其标记为潜在恶意任务的操作。
*   **Kimi K3（月之暗面）：** 作者转而使用中国模型。Kimi K3 识别出了 Mali GPU 驱动程序中一个 2022 年的未修补漏洞（CVE-2022-38181）。它花费了 30 小时构建了漏洞利用工具包和触发程序。
*   **GLM-5.2 & 5.3：** 在 Kimi K3 遇到内存偏移量瓶颈后，GLM-5.2 优化了方案。最终，新发布的 GLM-5.3 发现内核地址与标准镜像相比略有偏移。不到一天，GLM-5.3 就成功将 SELinux 状态切换为宽容模式并获得了 root 权限。

**结果与启示**
获得 root 权限后，作者删除了 100 多个亚马逊软件包，成功解决了意外关机问题。作者反思了“提示词小子”（prompt kiddie）现象，即人类充当战略指挥者（“舵手”），引导 AI 代理执行复杂的工程任务。文章还强调了 AI 安全方面的差异：美国模型（如 Claude）利用“生硬”的防护措施完全拦截任务，而中国模型则会结合伦理语境进行推理——认可用户对其硬件的所有权——并提供了必要的技术协助。

---

## 3. 复杂系统如何失效 (1998)

**原文标题**: How Complex Systems Fail (1998)

**原文链接**: [https://how.complexsystems.fail/](https://how.complexsystems.fail/)

**《复杂系统如何失效》摘要**

理查德·库克（Richard Cook）这篇开创性的论文指出，医疗、航空和发电等复杂系统本质上是危险的。由于这些系统至关重要，它们受到技术、组织和人为等多重防御机制的保护。因此，灾难绝非源于单点故障；相反，它是多个微小且潜在缺陷共同作用的结果。这些缺陷单独来看不足以导致崩溃，但集合起来却能绕过所有防御。

一个关键的启示是，复杂系统始终运行在“降级模式”下。它们从未处于无缺陷状态，之所以能持续运行，是依靠冗余机制，更重要的是依靠人类操作员的适应能力。库克认为，“人为错误”和“根本原因”分析是根本性的误解。“根本原因”是一种用于定责的社会建构，忽略了事故是由多重因素共同促成的事实。此外，后见之明偏见（hindsight bias）会误导事后调查，使过去发生的事件在调查者看来，比处于“一线”（sharp end）的从业者当时所面对的情况更具可预测性。

在这些系统中，人类操作员扮演着生产者和防御者的双重角色。他们必须在不确定性面前不断博弈，在生产压力与安全风险之间寻求平衡。库克强调，安全不是一个静态组件或一种商品，而是一种动态的涌现属性，是人们通过不断的调整和消除组织模糊性而创造出来的。

最后，论文警告称，技术变革往往会引入新的、不可预见的失效模式。为了维持安全，操作员需要从失败中积累经验，以理解“性能极限”——即容许表现的边界。最终，无故障运行并非完美系统的产物，而是专家级的人类在本质上充满缺陷的环境中不断创造安全的结果。

---

## 4. 恶意软件感染基于安卓的车机固件

**原文标题**: Malware infects Android-based automotive head unit firmware

**原文链接**: [https://securelist.com/android-head-unit-malware/121106/](https://securelist.com/android-head-unit-malware/121106/)

2026年6月，研究人员发现了一场专门针对汽车中控主机的 Android 恶意软件活动，这是首例记录在案的针对此类设备定制感染链的案例。该活动被高度确信归属于 MoYu Group（与 BADBOX 僵尸网络相关），其主要目标是进行广告欺诈以及将设备纳入代理僵尸网络。

感染通过利用 TWCore 传播，这是 DoFun 中控主机中负责固件更新的合法系统应用。通过操纵更新过程中的 `installNotExists` 标志，攻击者可以在无需用户交互或可见界面的情况下远程安装恶意 APK。

该恶意软件采用了精密的三阶段感染链：
1.  **JarService Dropper：** 一个无界面的应用，负责解密并执行第二阶段负载。
2.  **Loader：** 该组件连接命令与控制 (C2) 服务器以下载最终阶段，并利用反射技术和 XOR 加密来隐藏其活动。
3.  **Clicker/Reverse Proxy：** 最终负载执行各项命令以实施广告欺诈并提供反向代理功能。它每 90 分钟与 C2 服务器通信一次，以更新配置并接收新指令（例如“zhima”模块）。

该恶意软件的功能包括展示广告、实施点击欺诈以及下载额外的恶意代码。发现该威胁后，相关厂商已收到通知，据报道已修复了固件更新机制中的安全漏洞。卡巴斯基将此类威胁检测为 **HEUR:Trojan.AndroidOS.Vo1d** 等名称。

---

## 5. 椰子油航空燃料在发动机测试中的效率与煤油相当

**原文标题**: Coconut Oil Jet Fuel Matches Kerosene's Efficiency in Engine Tests

**原文链接**: [https://studyfinds.com/coconut-oil-jet-fuel-matches-kerosenes-efficiency-in-engine-tests/](https://studyfinds.com/coconut-oil-jet-fuel-matches-kerosenes-efficiency-in-engine-tests/)

大阪公立大学的研究人员证明，从椰子油中提取的生物燃料可以实现与传统煤油相当的热效率，为可持续航空燃料（SAF）提供了一条潜在的低能耗路径。

该研究发表在《燃料》（Fuel）杂志上，利用“共溶剂法”从不可食用的椰子废料中生产出高纯度生物燃料。与需要高温高压的传统SAF生产方式不同，该方法在低温下使用丙酮和酒精，显著降低了生产所需的能耗。

**关键性能研究结果：**
*   **效率：** 在微型喷气发动机中以高达50%的掺混比例进行测试时，该生物燃料的热效率和推力与纯煤油相当。
*   **消耗量：** 由于生物燃料的能量密度较低，发动机需要增加约17%至20%的燃料重量才能维持相同的性能。
*   **排放：** 由于椰子油缺乏化石燃料中的芳香族化合物，混合燃料显著减少了未燃烧碳氢化合物的排放（降幅高达40%）。虽然二氧化碳（$CO_2$）和一氧化氮水平基本保持稳定，但由于着火难度增加，一氧化碳排放量略有上升。

**实施挑战：**
尽管结果令人鼓舞，但仍面临若干障碍。该燃料目前的含氧量超出了国际航空标准，研究人员还指出了吸湿、氧化以及潜在的金属腐蚀等问题。未来的步骤需要进行化学稳定化处理（如加氢），并在全尺寸商业发动机上进行长期测试。

虽然目前还不是一种成熟的即用型替代品，但该研究证明，通过节能方法生产的椰子油基SAF是减少航空业碳足迹的一个可行方案。

---

## 6. 一个提供精简开源替代方案的网站

**原文标题**: A website for debloated open source alternatives

**原文链接**: [https://debloat.dev/](https://debloat.dev/)

**debloat.dev** 是一个社区驱动的目录，致力于用纯净、开源的替代方案来取代专有、臃肿或广告密集的软件和固件。该平台专注于帮助用户重新夺回对硬件的控制权，为包括外设、智能家居系统、媒体流播放器和网络工具在内的各类设备提供“去臃肿化”的解决方案。

该网站对项目进行了分类，以帮助用户针对供应商锁定的生态系统寻找特定的替代品。主要示例包括：

*   **智能家居与物联网：** 诸如 **Home Assistant** 和 **ESPHome** 等替代方案，用于取代涂鸦（Tuya）或 Ring 等品牌的云依赖型应用。
*   **媒体与娱乐：** 诸如 **Jellyfin**、**Kodi** 和 **CoreELEC** 等解决方案，用于取代智能电视的原厂固件以及 Plex 等流媒体服务。
*   **硬件外设：** 诸如 **OpenRazer** 和 **ckb-next** 等驱动程序和配置工具，用于取代 Razer Synapse 或 Corsair iCUE 等资源密集型套件。
*   **存储与同步：** 诸如 **Immich**、**Syncthing** 和 **BorgBackup** 等注重隐私的工具，用于取代专有的云存储和备份软件。

该平台秉持极简主义和隐私优先的理念，不设任何追踪且不使用 Cookie（除非已登录）。用户可以对项目进行评分、参与讨论，并针对尚未找到的特定软件替代方案提交“请求”。目前该网站已列出近 200 个项目，是 DIY 和开源社区寻求提升设备性能与隐私保护的重要资源。

---

## 7. My favorite nonfiction books about cults, scams, and schemes

**原文标题**: My favorite nonfiction books about cults, scams, and schemes

**原文链接**: [https://bookdna.com/best-books/nonfiction-about-cults-scams-and-schemes](https://bookdna.com/best-books/nonfiction-about-cults-scams-and-schemes)

在《我最喜欢的关于邪教、骗局与阴谋的非虚构类书籍》一文中，作者精选了一系列引人入胜的读物，深入探讨了欺骗心理、群体思维以及魅力型领导的影响力。这份书单涵盖了备受瞩目的企业欺诈和封闭的高控制宗教团体两大领域。

作者重点介绍了数部关于金融丑闻的权威著作，最著名的当属约翰·卡雷鲁（John Carreyrou）的《坏血》（*Bad Blood*），该书记录了血液检测初创公司 Theranos 的兴衰。其他聚焦企业的作品还包括《房间里最聪明的人》（安然公司）、《我们之教》（WeWork）以及《鲸吞亿万》（1MDB丑闻），这些书籍都审视了野心与贪婪如何演变为大规模的系统性欺诈。

该选集还深入探讨了信仰与孤立的阴暗面。劳伦斯·赖特（Lawrence Wright）的《大清算》（山达基教）和乔恩·克拉考尔（Jon Krakauer）的《天堂旗帜下》（摩门教基要派）等奠基性著作，因其严谨的深度调查而获推荐。个人叙事也占有重要地位，如塔拉·韦斯特弗（Tara Westover）的《你当像鸟飞往你的山》（*Educated*）和德博拉·费尔德曼（Deborah Feldman）的《不守教规》（*Unorthodox*）等回忆录，提供了逃离极端宗教或生存主义环境的切身视角。

书单中一个独特的补充是阿曼达·蒙特尔（Amanda Montell）的《狂热分子》（*Cultish*），该书将焦点转向了“狂热者的语言”。蒙特尔探讨了从破坏性邪教到像 CrossFit 这样的现代健身品牌，语言模式是如何被用来操纵人心的。

最终，文章将这些书籍定位为研究人类脆弱性的必读书目。无论是通过数十亿美元的阴谋，还是通过极权主义的意识形态，这些叙事都揭示了对归属感的渴望和对“更好出路”的承诺，是多么容易被掌权者所利用。

---

## 8. 为什么萨尔·可汗行不通：论“做中学”与“说中教”的背离

**原文标题**: Why Sal Khan't: On Learning by Making but Teaching by Telling

**原文链接**: [https://punyamishra.com/2026/04/16/why-sal-khant-on-learning-by-making-but-teaching-by-telling/](https://punyamishra.com/2026/04/16/why-sal-khant-on-learning-by-making-but-teaching-by-telling/)

生成摘要时出错

---

## 9. Slovakia finds Russian backdoor in traffic speed cameras

**原文标题**: Slovakia finds Russian backdoor in traffic speed cameras

**原文链接**: [https://risky.biz/risky-bulletin-slovakia-finds-russian-backdoor-in-traffic-speed-cameras/](https://risky.biz/risky-bulletin-slovakia-finds-russian-backdoor-in-traffic-speed-cameras/)

生成摘要时出错

---

## 10. Things I want in a modern relational query language

**原文标题**: Things I want in a modern relational query language

**原文链接**: [https://sporks.space/2026/08/19/things-i-want-in-a-modern-relational-query-language/](https://sporks.space/2026/08/19/things-i-want-in-a-modern-relational-query-language/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 2 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 3 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 4 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 5 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 6 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 7 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 8 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 9 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 10 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 11 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 12 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 13 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 14 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 15 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 16 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 17 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 18 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 19 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 20 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 21 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 22 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 23 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 24 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 25 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 26 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 27 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 28 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 29 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 30 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 31 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 32 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 33 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 34 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 35 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 36 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 37 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 38 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 39 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 40 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 41 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 42 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 43 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 44 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 45 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 46 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 47 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 48 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 49 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 50 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 51 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 52 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 53 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 54 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 55 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 56 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 57 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 58 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 59 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 60 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 61 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 62 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 63 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 64 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 65 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 66 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 67 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 68 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 69 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 70 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 71 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 72 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 73 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 74 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 75 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 76 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 77 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 78 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 79 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 80 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 81 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 82 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 83 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 84 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 85 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 86 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 87 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 88 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 89 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 90 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 91 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 92 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 93 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 94 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 95 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 96 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 97 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 98 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 99 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 100 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 101 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 102 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 103 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 104 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 105 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 106 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 107 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 108 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 109 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 110 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 111 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 112 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 113 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 114 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 115 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 116 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 117 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 118 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 119 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 120 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 121 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 122 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 123 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 124 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 125 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 126 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 127 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 128 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 129 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 130 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 131 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 132 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 133 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 134 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 135 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 136 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 137 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 138 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 139 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 140 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 141 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 142 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 143 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 144 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 145 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 146 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 147 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 148 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 149 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 150 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 151 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 152 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 153 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 154 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 155 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 156 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 157 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 158 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 159 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 160 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 161 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 162 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 163 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 164 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 165 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 166 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 167 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 168 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 169 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 170 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 171 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 172 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 173 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 174 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 175 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 176 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 177 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 178 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 179 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 180 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 181 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 182 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 183 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 184 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 185 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 186 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 187 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 188 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 189 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 190 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 191 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 192 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 193 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 194 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 195 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 196 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 197 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 198 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 199 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 200 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 201 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 202 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 203 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 204 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 205 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 206 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 207 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 208 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 209 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 210 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 211 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 212 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 213 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 214 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 215 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 216 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 217 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 218 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 219 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 220 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 221 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 222 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 223 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 224 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 225 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 226 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 227 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 228 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 229 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 230 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 231 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 232 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 233 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 234 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 235 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 236 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 237 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 238 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 239 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 240 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 241 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 242 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 243 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 244 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 245 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 246 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 247 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 248 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 249 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 250 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 251 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 252 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 253 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 254 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 255 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 256 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 257 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 258 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 259 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 260 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 261 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 262 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 263 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 264 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 265 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 266 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 267 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 268 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 269 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 270 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 271 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 272 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 273 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 274 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 275 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 276 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 277 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 278 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 279 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 280 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 281 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 282 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 283 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 284 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 285 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 286 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 287 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 288 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 289 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 290 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 291 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 292 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 293 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 294 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 295 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 296 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 297 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 298 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 299 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 300 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 301 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 302 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 303 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 304 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 305 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 306 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 307 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 308 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 309 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 310 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 311 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 312 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 313 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 314 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 315 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 316 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 317 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 318 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 319 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 320 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 321 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 322 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 323 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 324 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 325 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 326 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 327 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 328 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 329 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 330 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 331 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 332 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 333 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 334 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 335 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 336 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 337 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 338 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 339 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 340 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 341 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 342 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 343 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 344 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 345 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 346 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 347 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 348 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 349 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 350 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 351 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 352 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 353 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 354 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 355 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 356 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 357 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 358 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 359 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 360 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 361 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 362 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 363 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 364 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 365 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 366 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 367 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 368 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 369 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 370 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 371 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 372 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 373 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 374 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 375 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 376 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 377 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 378 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 379 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 380 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 381 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 382 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 383 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 384 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 385 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 386 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 387 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 388 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 389 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 390 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 391 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 392 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 393 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 394 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 395 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 396 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 397 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 398 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 399 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 400 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 401 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 402 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 403 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 404 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 405 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 406 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 407 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 408 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 409 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 410 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 411 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 412 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 413 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 414 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 415 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 416 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 417 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 418 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 419 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 420 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 421 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 422 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 423 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 424 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 425 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 426 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 427 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 428 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 429 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 430 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 431 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 432 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 433 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 434 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 435 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 436 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 437 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 438 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 439 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 440 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 441 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 442 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 443 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 444 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 445 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 446 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 447 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 448 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 449 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 450 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 451 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 452 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 453 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 454 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 455 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 456 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 457 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 458 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 459 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 460 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 461 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 462 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 463 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 464 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 465 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 466 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 467 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 468 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 469 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 470 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 471 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 472 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 473 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 474 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 475 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 476 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 477 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 478 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 479 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 480 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 481 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 482 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 483 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 484 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 485 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 486 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 487 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 488 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 489 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 490 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 491 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 492 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 493 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 494 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 495 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 496 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 497 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 498 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 499 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 500 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 501 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 502 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 503 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 504 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 505 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 506 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 507 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 508 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 509 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 510 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 511 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 512 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 513 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 514 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 515 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 516 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 517 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 518 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 519 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 520 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
