# Hacker News 热门文章摘要 (2026-08-23)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. To become a better writer, read as much as you can

**原文标题**: To become a better writer, read as much as you can

**原文链接**: [https://nappertime.com/the-golden-rule-of-becoming-a-better-writer/](https://nappertime.com/the-golden-rule-of-becoming-a-better-writer/)

生成摘要时出错

---

## 12. Wi-Fi 8 is the first wireless upgrade in years that isn't chasing speed

**原文标题**: Wi-Fi 8 is the first wireless upgrade in years that isn't chasing speed

**原文链接**: [https://www.xda-developers.com/wi-fi-8-first-wireless-upgrade-years-isnt-chasing-speed-home-networks-need-it/](https://www.xda-developers.com/wi-fi-8-first-wireless-upgrade-years-isnt-chasing-speed-home-networks-need-it/)

生成摘要时出错

---

## 13. The End of an Athlon

**原文标题**: The End of an Athlon

**原文链接**: [http://www.os2museum.com/wp/the-end-of-an-athlon/](http://www.os2museum.com/wp/the-end-of-an-athlon/)

生成摘要时出错

---

## 14. What Is a Harness?

**原文标题**: What Is a Harness?

**原文链接**: [https://earendil.com/posts/what-is-a-harness/](https://earendil.com/posts/what-is-a-harness/)

In the article "What Is a Harness?", Earendil Product defines an **agent harness** as the software environment that transforms a static AI model into an active, functional AI agent. Using the metaphor of a climbing harness, the author explains that while a model provides the "power," the harness provides the structure, safety, and tools necessary to navigate tasks.

An agent harness typically performs four core functions:
1.  **System Prompt:** It provides a set of behavioral instructions that govern how the model acts within a specific context.
2.  **Tools:** It equips the model with coded capabilities—such as web searching, code execution, or email composition—which the model can use at its own discretion.
3.  **Agentic Loops:** It establishes a framework that allows the model to iterate. The model can review its own work, decide if a task is incomplete, and repeat steps until a goal is met.
4.  **Translation Layer:** This crucial component allows the harness to remain model-agnostic, enabling users to swap between different AI providers (like OpenAI or Anthropic) or use open-source models.

The author emphasizes that, unlike proprietary AI models, a harness can be owned and run locally by the user. This decentralization ensures data privacy and gives individuals "agency" over their technology. By using open-source harnesses like **Pi**, **OpenClaw**, or **Hermes**, users can customize their workflows with extensions and avoid being tethered to a single AI lab. 

Ultimately, the article argues that neutral, open-source harnesses are essential tools for human empowerment, ensuring that users wield AI as a tool rather than being controlled by the corporations that create the underlying models.

---

## 15. 我交给 Qwen 3.8 27B 一项逆向工程任务，它 30 分钟就完成了。

**原文标题**: I gave Qwen 3.8 27B a reverse-engineering job and it finished in 30 minutes

**原文链接**: [https://www.xda-developers.com/qwen-3-8-27b-reverse-engineering-job-frontier-model/](https://www.xda-developers.com/qwen-3-8-27b-reverse-engineering-job-frontier-model/)

生成摘要时出错

---

## 16. MartyPC is a cross-platform emulator of early PCs written in Rust

**原文标题**: MartyPC is a cross-platform emulator of early PCs written in Rust

**原文链接**: [https://martypc.net/](https://martypc.net/)

生成摘要时出错

---

## 17. Why your local LLM feels dumber than it is

**原文标题**: Why your local LLM feels dumber than it is

**原文链接**: [https://forum.level1techs.com/t/why-your-local-llm-feels-dumber-than-it-is/253917](https://forum.level1techs.com/t/why-your-local-llm-feels-dumber-than-it-is/253917)

生成摘要时出错

---

## 18. JIT Compiling Code in 5μs

**原文标题**: JIT Compiling Code in 5μs

**原文链接**: [https://malisper.me/jit-compiling-code-in-5-us/](https://malisper.me/jit-compiling-code-in-5-us/)

生成摘要时出错

---

## 19. Show HN: Live 3D satellite tracker and the declassified Pentagon UFO archive

**原文标题**: Show HN: Live 3D satellite tracker and the declassified Pentagon UFO archive

**原文链接**: [https://skylens.yantraai.app/](https://skylens.yantraai.app/)

生成摘要时出错

---

## 20. Amiga-Inspired AROS Goes Bare Metal on Raspberry Pi

**原文标题**: Amiga-Inspired AROS Goes Bare Metal on Raspberry Pi

**原文链接**: [https://hackaday.com/2026/08/23/amiga-inspired-aros-goes-bare-metal-on-raspberry-pi/](https://hackaday.com/2026/08/23/amiga-inspired-aros-goes-bare-metal-on-raspberry-pi/)

生成摘要时出错

---

## 21. The Art and Beauty of Blade Runner (2015)

**原文标题**: The Art and Beauty of Blade Runner (2015)

**原文链接**: [https://nappertime.com/the-art-of-and-beauty-of-blade-runner/](https://nappertime.com/the-art-of-and-beauty-of-blade-runner/)

生成摘要时出错

---

## 22. I Dream of Quieter Computing

**原文标题**: I Dream of Quieter Computing

**原文链接**: [https://henry.codes/writing/i-dream-of-quieter-computing/](https://henry.codes/writing/i-dream-of-quieter-computing/)

生成摘要时出错

---

## 23. I set a trap for a book-marketing scammer (2025)

**原文标题**: I set a trap for a book-marketing scammer (2025)

**原文链接**: [https://rwwgreene.substack.com/p/i-set-a-trap-for-a-book-marketing](https://rwwgreene.substack.com/p/i-set-a-trap-for-a-book-marketing)

生成摘要时出错

---

## 24. Hister – A private, full content search index that you control

**原文标题**: Hister – A private, full content search index that you control

**原文链接**: [https://hister.org/](https://hister.org/)

生成摘要时出错

---

## 25. Fast and Hard Code

**原文标题**: Fast and Hard Code

**原文链接**: [https://lucumr.pocoo.org/2026/8/22/fast-hard-code/](https://lucumr.pocoo.org/2026/8/22/fast-hard-code/)

生成摘要时出错

---

## 26. ElevenLabs, TwelveLabs, ThirteenLabs

**原文标题**: ElevenLabs, TwelveLabs, ThirteenLabs

**原文链接**: [https://quantumi.sh/public/labs.html](https://quantumi.sh/public/labs.html)

生成摘要时出错

---

## 27. Scrap (2006)

**原文标题**: Scrap (2006)

**原文链接**: [https://twitter.com/moxie/status/2091218652133732491](https://twitter.com/moxie/status/2091218652133732491)

生成摘要时出错

---

## 28. typ.ing

**原文标题**: typ.ing

**原文链接**: [https://typ.ing/](https://typ.ing/)

生成摘要时出错

---

## 29. Death to px, long live ch

**原文标题**: Death to px, long live ch

**原文链接**: [https://shkspr.mobi/blog/2026/08/death-to-px-long-live-ch/](https://shkspr.mobi/blog/2026/08/death-to-px-long-live-ch/)

生成摘要时出错

---

## 30. Thinking in Python

**原文标题**: Thinking in Python

**原文链接**: [https://thinkinginpython.com/](https://thinkinginpython.com/)

生成摘要时出错

---

## 31. RF Cafe

**原文标题**: RF Cafe

**原文链接**: [https://www.rfcafe.com/](https://www.rfcafe.com/)

生成摘要时出错

---

## 32. New MCP Roadmap

**原文标题**: New MCP Roadmap

**原文链接**: [https://blog.modelcontextprotocol.io/posts/mcp-roadmap/](https://blog.modelcontextprotocol.io/posts/mcp-roadmap/)

生成摘要时出错

---

## 33. Risk of transmission of amyloid β pathology via transfused blood products

**原文标题**: Risk of transmission of amyloid β pathology via transfused blood products

**原文链接**: [https://doi.org/10.1016/S0140-6736(26)00767-1](https://doi.org/10.1016/S0140-6736(26)00767-1)

生成摘要时出错

---

## 34. NanoGPT Speedrun Frontier

**原文标题**: NanoGPT Speedrun Frontier

**原文链接**: [https://www.primeintellect.ai/research/nanogpt-speedrun](https://www.primeintellect.ai/research/nanogpt-speedrun)

生成摘要时出错

---

## 35. How a Texas student blew the whistle on a rogue AI hacking attempt

**原文标题**: How a Texas student blew the whistle on a rogue AI hacking attempt

**原文链接**: [https://www.reuters.com/world/how-texas-student-blew-whistle-rogue-ai-hacking-attempt-2026-08-20/](https://www.reuters.com/world/how-texas-student-blew-whistle-rogue-ai-hacking-attempt-2026-08-20/)

生成摘要时出错

---

## 36. Rust 1.98 got a P-critical miscompilation

**原文标题**: Rust 1.98 got a P-critical miscompilation

**原文链接**: [https://github.com/rust-lang/rust/issues/161441](https://github.com/rust-lang/rust/issues/161441)

生成摘要时出错

---

## 37. NetBSD and my life (2005)

**原文标题**: NetBSD and my life (2005)

**原文链接**: [https://mail-index.netbsd.org/netbsd-advocacy/2005/09/10/0000.html](https://mail-index.netbsd.org/netbsd-advocacy/2005/09/10/0000.html)

生成摘要时出错

---

## 38. ATProto spaces: A new extension to ATProto that enables non-public data

**原文标题**: ATProto spaces: A new extension to ATProto that enables non-public data

**原文链接**: [https://atproto.com/blog/atproto-spaces-alpha](https://atproto.com/blog/atproto-spaces-alpha)

生成摘要时出错

---

## 39. Vit D assoc w better cognition in those w sleep disturb./mild cognitive impair

**原文标题**: Vit D assoc w better cognition in those w sleep disturb./mild cognitive impair

**原文链接**: [https://www.sciencedirect.com/science/article/abs/pii/S1389945726001991?via%3Dihub](https://www.sciencedirect.com/science/article/abs/pii/S1389945726001991?via%3Dihub)

生成摘要时出错

---

## 40. Munder Difflin – Agent harness to run an office of your clones

**原文标题**: Munder Difflin – Agent harness to run an office of your clones

**原文链接**: [https://munderdiffl.in/](https://munderdiffl.in/)

生成摘要时出错

---

## 41. Figmimic – A bookmarklet to copy any webpage into Figma as editable layers

**原文标题**: Figmimic – A bookmarklet to copy any webpage into Figma as editable layers

**原文链接**: [https://marcua.net/minitools/figmimic/](https://marcua.net/minitools/figmimic/)

生成摘要时出错

---

## 42. Z80 – The 1970s Microprocessor Still Alive (2021)

**原文标题**: Z80 – The 1970s Microprocessor Still Alive (2021)

**原文链接**: [https://www.computer.org/csdl/magazine/mi/2021/06/09623402/1yJTvlRLmhi](https://www.computer.org/csdl/magazine/mi/2021/06/09623402/1yJTvlRLmhi)

生成摘要时出错

---

## 43. So, You Found a Foden Steam Lorry in a Field. What Next?

**原文标题**: So, You Found a Foden Steam Lorry in a Field. What Next?

**原文链接**: [https://hackaday.com/2026/08/23/so-you-found-a-foden-steam-lorry-in-a-field-what-next/](https://hackaday.com/2026/08/23/so-you-found-a-foden-steam-lorry-in-a-field-what-next/)

生成摘要时出错

---

## 44. Universal Housing

**原文标题**: Universal Housing

**原文链接**: [https://twitter.com/christianreber/status/2091532545577849008](https://twitter.com/christianreber/status/2091532545577849008)

生成摘要时出错

---

## 45. Hell has more than 7 circles you guys (2022)

**原文标题**: Hell has more than 7 circles you guys (2022)

**原文链接**: [http://colinmorris.github.io/blog/n-circles-of-hell](http://colinmorris.github.io/blog/n-circles-of-hell)

生成摘要时出错

---

## 46. A Friendly Introduction to Racket

**原文标题**: A Friendly Introduction to Racket

**原文链接**: [https://geometridae.bearblog.dev/a-friendly-introduction-to-racket/](https://geometridae.bearblog.dev/a-friendly-introduction-to-racket/)

生成摘要时出错

---

## 47. How Much of the Internet Is Written with AI?

**原文标题**: How Much of the Internet Is Written with AI?

**原文链接**: [https://www.pewresearch.org/data-labs/2026/08/20/how-much-of-the-internet-is-written-with-ai/](https://www.pewresearch.org/data-labs/2026/08/20/how-much-of-the-internet-is-written-with-ai/)

生成摘要时出错

---

## 48. One night in Uzbekistan: Why was this one data point so influential?

**原文标题**: One night in Uzbekistan: Why was this one data point so influential?

**原文链接**: [https://statmodeling.stat.columbia.edu/2026/08/20/we-couldnt-reproduce-their-findings-and-realized-that-it-was-all-driven-by-weird-data-from-uzbekistan/](https://statmodeling.stat.columbia.edu/2026/08/20/we-couldnt-reproduce-their-findings-and-realized-that-it-was-all-driven-by-weird-data-from-uzbekistan/)

生成摘要时出错

---

## 49. Why aren't my two Cortex-A9 cores cache coherent?

**原文标题**: Why aren't my two Cortex-A9 cores cache coherent?

**原文链接**: [https://thejpster.org.uk/blog/blog-2026-08-22/](https://thejpster.org.uk/blog/blog-2026-08-22/)

生成摘要时出错

---

## 50. Show HN: Public Muscriptor Instance (latest, most powerful Audio-to-MIDI model)

**原文标题**: Show HN: Public Muscriptor Instance (latest, most powerful Audio-to-MIDI model)

**原文链接**: [https://www.pianoify.net/](https://www.pianoify.net/)

生成摘要时出错

---

## 51. Andrew Ng: "AI Engineering Skills Map: Building and Deploying AI Applications"

**原文标题**: Andrew Ng: "AI Engineering Skills Map: Building and Deploying AI Applications"

**原文链接**: [https://twitter.com/AndrewYNg/status/2090840747738374568](https://twitter.com/AndrewYNg/status/2090840747738374568)

生成摘要时出错

---

## 52. Canada will match US tariffs 'dollar for dollar' as trade talks break down

**原文标题**: Canada will match US tariffs 'dollar for dollar' as trade talks break down

**原文链接**: [https://www.bbc.com/news/articles/cvgvyy4x2mvo](https://www.bbc.com/news/articles/cvgvyy4x2mvo)

生成摘要时出错

---

## 53. Conway's Game of Life in real life

**原文标题**: Conway's Game of Life in real life

**原文链接**: [https://blog.coredump.cx/p/conways-game-of-life-in-real-life](https://blog.coredump.cx/p/conways-game-of-life-in-real-life)

生成摘要时出错

---

## 54. A Kantian Critique of "Sorry" by Justin Bieber

**原文标题**: A Kantian Critique of "Sorry" by Justin Bieber

**原文链接**: [https://decodingvibes.com/blog/a-kantian-critique-of-sorry-by-justin-bieber/](https://decodingvibes.com/blog/a-kantian-critique-of-sorry-by-justin-bieber/)

生成摘要时出错

---

## 55. A week of using Codex more than Claude

**原文标题**: A week of using Codex more than Claude

**原文链接**: [https://allaboutcoding.ghinda.com/a-week-of-using-codex-more-than-claude/](https://allaboutcoding.ghinda.com/a-week-of-using-codex-more-than-claude/)

生成摘要时出错

---

## 56. Zig’s Io.Threaded is neat

**原文标题**: Zig’s Io.Threaded is neat

**原文链接**: [https://matklad.github.io/2026/08/06/neat-io-threaded.html](https://matklad.github.io/2026/08/06/neat-io-threaded.html)

生成摘要时出错

---

## 57. Steve French (SMB3/CIFSFS Linux kernel maintainer) has died

**原文标题**: Steve French (SMB3/CIFSFS Linux kernel maintainer) has died

**原文链接**: [https://www.phoronix.com/news/SMB3-CIFS-Maintainer-Change](https://www.phoronix.com/news/SMB3-CIFS-Maintainer-Change)

生成摘要时出错

---

## 58. Early-life stress leaves a 'scar' inside brain cells in mice

**原文标题**: Early-life stress leaves a 'scar' inside brain cells in mice

**原文链接**: [https://medicine.washu.edu/news/how-early-life-stress-leaves-a-scar-inside-brain-cells/](https://medicine.washu.edu/news/how-early-life-stress-leaves-a-scar-inside-brain-cells/)

生成摘要时出错

---

## 59. Sydney Marathon medal mistakenly depicts Munich stadium

**原文标题**: Sydney Marathon medal mistakenly depicts Munich stadium

**原文链接**: [https://www.bbc.com/news/articles/cvg92y1wzn8o](https://www.bbc.com/news/articles/cvg92y1wzn8o)

生成摘要时出错

---

## 60. Hacker News RSS

**原文标题**: Hacker News RSS

**原文链接**: [https://hnrss.github.io/](https://hnrss.github.io/)

生成摘要时出错

---

## 61. Airbus bows to remote working demands after series of strikes

**原文标题**: Airbus bows to remote working demands after series of strikes

**原文链接**: [https://www.theguardian.com/business/2026/aug/21/airbus-bows-remote-working-strikes](https://www.theguardian.com/business/2026/aug/21/airbus-bows-remote-working-strikes)

生成摘要时出错

---

## 62. What's in a PowerPoint File?

**原文标题**: What's in a PowerPoint File?

**原文链接**: [https://editide.com/blog/what-is-a-pptx-file/](https://editide.com/blog/what-is-a-pptx-file/)

生成摘要时出错

---

## 63. hdiutil is deprecated in macOS 27 Golden Gate

**原文标题**: hdiutil is deprecated in macOS 27 Golden Gate

**原文链接**: [https://lapcatsoftware.com/articles/2026/8/7.html](https://lapcatsoftware.com/articles/2026/8/7.html)

生成摘要时出错

---

## 64. SalesPatriot (YC W25) Is Hiring Forward Deployed Engineers

**原文标题**: SalesPatriot (YC W25) Is Hiring Forward Deployed Engineers

**原文链接**: [https://www.ycombinator.com/companies/salespatriot/jobs/M46X6YX-forward-deployed-engineer](https://www.ycombinator.com/companies/salespatriot/jobs/M46X6YX-forward-deployed-engineer)

生成摘要时出错

---

## 65. Felony Bench

**原文标题**: Felony Bench

**原文链接**: [https://www.felonybench.com/](https://www.felonybench.com/)

生成摘要时出错

---

## 66. Physical Activity at Work Linked to Higher Dementia Rates

**原文标题**: Physical Activity at Work Linked to Higher Dementia Rates

**原文链接**: [https://www.medpagetoday.com/neurology/dementia/122675](https://www.medpagetoday.com/neurology/dementia/122675)

生成摘要时出错

---

## 67. Show HN: terminal-code – VS Code inside the terminal

**原文标题**: Show HN: terminal-code – VS Code inside the terminal

**原文链接**: [https://terminal-code.com](https://terminal-code.com)

生成摘要时出错

---

## 68. Stop Anthropomorphizing Intermediate Tokens as Reasoning/Thinking Traces (2025)

**原文标题**: Stop Anthropomorphizing Intermediate Tokens as Reasoning/Thinking Traces (2025)

**原文链接**: [https://arxiv.org/abs/2504.09762](https://arxiv.org/abs/2504.09762)

生成摘要时出错

---

## 69. Dynamical dark energy and the week that broke cosmology

**原文标题**: Dynamical dark energy and the week that broke cosmology

**原文链接**: [https://perimeterinstitute.ca/news/dynamical-dark-energy-and-week-broke-cosmology](https://perimeterinstitute.ca/news/dynamical-dark-energy-and-week-broke-cosmology)

生成摘要时出错

---

## 70. Mythic's analog compute-in-memory architecture

**原文标题**: Mythic's analog compute-in-memory architecture

**原文链接**: [https://www.mythic.ai](https://www.mythic.ai)

生成摘要时出错

---

## 71. Felony charges for citizen deleting phone data at US Border

**原文标题**: Felony charges for citizen deleting phone data at US Border

**原文链接**: [https://www.nytimes.com/2026/08/21/us/politics/samuel-tunick-deleted-phone-felony.html](https://www.nytimes.com/2026/08/21/us/politics/samuel-tunick-deleted-phone-felony.html)

生成摘要时出错

---

## 72. MiniageOS: "Dumbphone" Version of LineageOS

**原文标题**: MiniageOS: "Dumbphone" Version of LineageOS

**原文链接**: [https://github.com/ofdryads/miniageOS](https://github.com/ofdryads/miniageOS)

生成摘要时出错

---

## 73. Why it might be time to rethink the human family tree

**原文标题**: Why it might be time to rethink the human family tree

**原文链接**: [https://nautil.us/why-it-might-be-time-to-rethink-the-human-family-tree-1283985](https://nautil.us/why-it-might-be-time-to-rethink-the-human-family-tree-1283985)

生成摘要时出错

---

## 74. Reading Maps – Journeys from fiction drawn on the real world

**原文标题**: Reading Maps – Journeys from fiction drawn on the real world

**原文链接**: [https://readingmaps.com/](https://readingmaps.com/)

生成摘要时出错

---

## 75. AI companies destroy physical books – let's scan rare books before it's too late

**原文标题**: AI companies destroy physical books – let's scan rare books before it's too late

**原文链接**: [https://annas-archive.gl/blog/physical-destruction.html](https://annas-archive.gl/blog/physical-destruction.html)

生成摘要时出错

---

## 76. The Strange Allure of Fake Shopping Sites

**原文标题**: The Strange Allure of Fake Shopping Sites

**原文链接**: [https://macleans.ca/society/technology/the-strange-allure-of-fake-shopping-sites/](https://macleans.ca/society/technology/the-strange-allure-of-fake-shopping-sites/)

生成摘要时出错

---

## 77. Kobo can run apps now

**原文标题**: Kobo can run apps now

**原文链接**: [https://bandarlabs.github.io/Cobalt/](https://bandarlabs.github.io/Cobalt/)

生成摘要时出错

---

## 78. How Thailand Resisted Colonization

**原文标题**: How Thailand Resisted Colonization

**原文链接**: [https://worksinprogress.co/issue/how-thailand-resisted-colonization/](https://worksinprogress.co/issue/how-thailand-resisted-colonization/)

生成摘要时出错

---

## 79. How to archive Everything and share It

**原文标题**: How to archive Everything and share It

**原文链接**: [https://aramzs.github.io/steal-the-internet/](https://aramzs.github.io/steal-the-internet/)

生成摘要时出错

---

## 80. Rust Glancer: Rust LSP using 100x less RAM

**原文标题**: Rust Glancer: Rust LSP using 100x less RAM

**原文链接**: [https://rust-glancer.github.io/blog/hello-world/](https://rust-glancer.github.io/blog/hello-world/)

生成摘要时出错

---

## 81. How we made a text-to-speech model respond in sub-50 ms

**原文标题**: How we made a text-to-speech model respond in sub-50 ms

**原文链接**: [https://nari-labs.com/blog/qwen3-tts-speed-cost-frontier/](https://nari-labs.com/blog/qwen3-tts-speed-cost-frontier/)

生成摘要时出错

---

## 82. Autolith: A programming agent with a live runtime

**原文标题**: Autolith: A programming agent with a live runtime

**原文链接**: [https://www.lambda-symbolics.com/autolith](https://www.lambda-symbolics.com/autolith)

生成摘要时出错

---

## 83. Show HN: Make your logo extra bright on HDR screens

**原文标题**: Show HN: Make your logo extra bright on HDR screens

**原文链接**: [https://www.soverybright.com/](https://www.soverybright.com/)

生成摘要时出错

---

## 84. Iranian hackers shut down UK power plant for 4 days

**原文标题**: Iranian hackers shut down UK power plant for 4 days

**原文链接**: [https://www.telegraph.co.uk/news/2026/08/22/iranian-hackers-shut-down-uk-power-plant/](https://www.telegraph.co.uk/news/2026/08/22/iranian-hackers-shut-down-uk-power-plant/)

生成摘要时出错

---

## 85. Stop Making TUIs

**原文标题**: Stop Making TUIs

**原文链接**: [https://sockpuppet.org/blog/2026/08/20/stop-making-tuis/](https://sockpuppet.org/blog/2026/08/20/stop-making-tuis/)

生成摘要时出错

---

## 86. Software Engineering in the Agentic Era

**原文标题**: Software Engineering in the Agentic Era

**原文链接**: [https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/](https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/)

生成摘要时出错

---

## 87. A look at CrossPoint e-reader firmware

**原文标题**: A look at CrossPoint e-reader firmware

**原文链接**: [https://lwn.net/Articles/1087635/](https://lwn.net/Articles/1087635/)

生成摘要时出错

---

## 88. Refeeding Syndrome

**原文标题**: Refeeding Syndrome

**原文链接**: [https://en.wikipedia.org/wiki/Refeeding_syndrome](https://en.wikipedia.org/wiki/Refeeding_syndrome)

生成摘要时出错

---

## 89. I accidentally logged hundreds of thousands of phone calls to military bases

**原文标题**: I accidentally logged hundreds of thousands of phone calls to military bases

**原文链接**: [https://lina.sh/blog/hijacking-e164-arpa](https://lina.sh/blog/hijacking-e164-arpa)

生成摘要时出错

---

## 90. Show HN: Anonymous age verification with passkey-powered encryption

**原文标题**: Show HN: Anonymous age verification with passkey-powered encryption

**原文链接**: [https://loginwithone.com/](https://loginwithone.com/)

生成摘要时出错

---

