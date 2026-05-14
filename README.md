# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-05-14.md)

*最后自动更新时间: 2026-05-14 19:17:58*
## 1. 拆除我的2024款RAV4混动版上的调制解调器和GPS

**原文标题**: Removing the modem and GPS from my 2024 rav4 hybrid

**原文链接**: [https://arkadiyt.com/2026/05/13/removing-the-modem-and-gps-from-my-rav4/](https://arkadiyt.com/2026/05/13/removing-the-modem-and-gps-from-my-rav4/)

本文提供了针对 2024 款丰田 RAV4 混动版物理禁用追踪与遥测功能的全面指南。作者认为，现代车辆已成为侵入性的监控工具，收集大量个人数据——包括驾驶习惯、位置历史甚至生物识别信息——并将其出售给数据经纪商和保险公司。

为从源头上停止此类数据收集，作者详细介绍了如何拆除数据通信模块（DCM，即调制解调器）和内置 GPS 天线。

**关键信息与技术考量：**
*   **功能权衡：** 移除 DCM 将禁用 OTA 远程更新、云服务和紧急救援（SOS）功能。
*   **麦克风修复：** 由于车内麦克风线路经过 DCM，作者使用“DCM 绕过套件”来维持免提通话功能。
*   **断开 GPS：** 物理断开 GPS 是为了防止一个常见故障，即在使用 CarPlay 时，车辆内部位置数据会与手机导航发生冲突并将其覆盖。
*   **蓝牙隐私泄露：** 作者警告说，即使没有调制解调器，车辆也可能尝试通过蓝牙连接驾驶员的手机来“回传数据”。为防止这种情况，建议使用 USB 有线连接或专门的蓝牙转 USB 适配器。
*   **保修：** 虽然特定的车载信息系统保修可能会失效，但作者指出，《马格努森-莫斯保修法》保护车主，防止整车保修因不相关的机械问题而被取消。

作者总结道，尽管此过程需要大规模拆卸仪表盘，但对于在“车轮上的计算机”时代寻求绝对隐私的人来说，这是必要的一步。

---

## 2. RTX 5090 与 M4 MacBook Air：能玩游戏吗？

**原文标题**: RTX 5090 and M4 MacBook Air: Can It Game?

**原文链接**: [https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/](https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/)

本文详细介绍了一项技术实验：通过 Thunderbolt eGPU 显卡坞将 NVIDIA RTX 5090 桌面显卡连接到 M4 MacBook Air。由于 macOS 缺乏针对 Apple Silicon 的原生 NVIDIA 驱动程序，作者通过在 macOS 主机上运行 ARM64 Linux 虚拟机（VM）并实现 PCI 直通（PCI passthrough）绕过了这一限制。

该项目解决了几个重大的工程难题：

*   **PCI BAR 映射：** 最初尝试映射显卡的内存寄存器（BAR）时导致了主机内核崩溃（kernel panic）。作者发现，在 QEMU 中将该内存映射为“可执行”状态触发了崩溃；解决方案是应用代码补丁，确保设备内存仅保持读/写属性。
*   **DMA 与 DART：** 苹果的 IOMMU（即 DART）存在严格限制，包括 1.5GB 的映射上限且无法控制内存对齐。为了绕过这一限制，作者开发了一个名为 `apple-dma-pci` 的自定义 Linux 内核模块，用于处理虚拟机与主机硬件之间的内存转换以及 NVIDIA 特有的对齐问题。
*   **性能瓶颈：** 受限于 macOS 处理设备内存的方式，该配置无法利用“写合并”（write-combining）。这导致 BAR 写入速度比原生性能慢约 10 倍，但仍明显快于拦截（trapping）每次访问的方案。

尽管存在这些限制，该方案依然可行。作者成功运行了《赛博朋克 2077》、《古墓丽影：暗影》和《地平线：零之曙光》等高负载游戏，以及 Qwen 和 Gemma 等 AI 推理模型。该项目作为一个精妙的概念验证，证明了虽然 Apple Silicon 并非为外接 NVIDIA 硬件而设计，但通过创新的虚拟化技术和自定义驱动工程，可以弥合两者间的鸿沟，以支持高端游戏和 AI 工作负载。

---

## 3. Nginx 最新漏洞利用

**原文标题**: New Nginx Exploit

**原文链接**: [https://github.com/DepthFirstDisclosures/Nginx-Rift](https://github.com/DepthFirstDisclosures/Nginx-Rift)

生成摘要时出错

---

## 4. 该死的 AI 让我变笨了。

**原文标题**: God Damn AI is making me dumb

**原文链接**: [https://jpain.io/god-damn-ai-is-making-me-dumb/](https://jpain.io/god-damn-ai-is-making-me-dumb/)

在《该死的 AI 正在让我变笨》一文中，作者反思了过度依赖人工智能如何侵蚀其专业技能和自信。尽管身为一名软件开发人员，作者坦言在连续两年完全依赖 AI 提示词工作后，自己已基本忘记了如何手动编写代码。这种技能的丧失导致了一种沮丧感，促使作者下定决心重新学习手动编程。

文章重点描述了一场心理层面的挣扎，指出 AI 利用了用户的自我怀疑和“冒名顶替综合征”。虽然 AI 工具带来了便利，但作者认为 AI 生成的内容往往缺乏灵魂，无法体现其独特的个人风格，且经常偏离原意。甚至在不借助辅助撰写本文时，作者依然感到一种强烈的、条件反射般的冲动，想要通过 AI 验证来确保文字“通顺合理”。

从宏观角度，作者探讨了 AI 对软件行业的影响。文中引用了罗伯特·马丁（Uncle Bob）的观点，认为 AI 虽然可能减少对开发者的整体需求，但也有潜力让“专业精神”重回该领域。通过将编程这项技艺重新交还给一小部分专家——正如当年开创该领域的物理学家和数学家那样——AI 或许能扭转过去几十年因需求激增而导致的质量下滑趋势。

归根结底，这篇文章是一份个人行动宣言，号召人们抵制自动化捷径的诱惑，重新夺回个人的自主权、工匠精神和智力独立。

---

## 5. 硬盘固件破解

**原文标题**: HDD Firmware Hacking

**原文链接**: [https://icode4.coffee/?p=1465](https://icode4.coffee/?p=1465)

Ryan Miceli 的文章《HDD 固件破解 第一部分》详细介绍了作者在修改硬盘驱动器 (HDD) 和固态驱动器 (SSD) 固件方面的研究。该项目源于利用 Xbox 360 竞态条件的需要；作者意图修改驱动器固件，在特定扇区读取期间引入时间延迟，从而为触发漏洞提供更大的窗口。

作者概述了针对 Western Digital (WD) 和三星驱动器等多个测试对象的系统化方法：
1. **获取固件：** 通过专业修复工具 (PC-3000)、HDD Guru 等专业论坛，以及从制造商网站上的 OEM 固件更新程序中提取镜像来收集数据。
2. **逆向工程与分析：**
    * **Western Digital：** 作者发现其固件使用了 LZHUF 压缩算法的修改版本。通过在 IDA Pro 中逆向加载程序存根，他们调整了压缩常量，成功解压并分析了完整的固件镜像。
    * **三星 PM871a SSD：** 利用联想的固件更新程序，作者逆向了一种用于保护固件的位操作混淆算法。他们通过将内存地址与 ARM Cortex-M3 内存映射对齐，进一步识别了段头。
    * **三星 HM020GI：** 该驱动器带来了更大的挑战，其似乎使用了字反转数据和未知的指令集架构 (ISA)，作者将其推迟到后续文章中讨论。

最终，尽管作者找到了在不需要修改固件的情况下利用 Xbox 360 的替代方法，但该研究展示了如何利用 OEM 更新程序和逆向工程来绕过固件保护，并为自定义补丁准备驱动器。文章最后将 Western Digital 驱动器作为深度分析的主要成功案例进行了总结。

---

## 6. 加拿大计算机爱好者运动

**原文标题**: Computer Hobby Movement in Canada

**原文链接**: [https://museum.eecs.yorku.ca/exhibits/show/hobby_canada/hobby_canada](https://museum.eecs.yorku.ca/exhibits/show/hobby_canada/hobby_canada)

“加拿大计算机爱好者运动”记录了计算机从专业工业工具向家用必需品转变的十年历程（1976–1985年）。这一转型的核心是由哈罗德·梅兰森（Harold Melanson）于1976年1月创立的**多伦多地区计算机爱好者协会（TRACE）**。

这场运动根植于长达一个世纪的无线电和电子爱好者传统，并受到20世纪70年代微处理器问世的催化。虽然受到美国里程碑事件（如家用电脑俱乐部和Altair 8800）的影响，但加拿大的这场运动保持了独特的身份特征。TRACE成员最初关注本地硬件，特别是国际微系统有限公司（MIL）生产的 **MOD-8 和 MOD-80** 微型计算机。此外，TRACE 的独特之处还在于其对 **APL** 语言的深度参与，这是一种由加拿大人肯尼斯·艾弗森（Kenneth Iverson）构思的编程语言。

随着时间的推移，该运动的参与群体发生了变化，从最初的计算机专业人士扩大到包括新手和学生。这些爱好者通过加拿大科技公司的“后门”渠道获取“规格外”零件，以此应对组件昂贵等挑战。文中提到的重要里程碑包括霍华德·富兰克林（Howard Franklin）于1974年自制的计算机，以及总部位于多伦多的 **MCM/70**——这被认为是第一台专为个人使用而设计的、由微处理器驱动的便携式计算机。

尽管随着个人电脑市场的标准化和商业化，正式的爱好者运动到20世纪80年代末已难以维持其影响力，但其遗产影响深远。它成功弥合了专业电子技术与社会之间的鸿沟，培养了包容性文化，并使个人计算成为了加拿大人的现实。

---

## 7. MIT: 20% drop in incoming graduate students

**原文标题**: MIT: 20% drop in incoming graduate students

**原文链接**: [https://president.mit.edu/writing-speeches/video-transcript-message-president-kornbluth-about-funding-and-talent-pipeline](https://president.mit.edu/writing-speeches/video-transcript-message-president-kornbluth-about-funding-and-talent-pipeline)

In a May 2026 address, MIT President Sally Kornbluth detailed a significant crisis facing the Institute regarding funding and its talent pipeline. 

**Financial Challenges**
MIT is grappling with a heavy 8% tax on endowment returns and a sharp decline in federal support. Despite some restored Congressional appropriations, federal research activity at MIT has dropped by more than 20%, and new federal awards have seen a similar decline. Total sponsored research is down 10%. This is attributed to a slow flow of federal funds and a shift in government policy that may prioritize geography over scientific merit when allocating grants.

**The Talent Pipeline**
These financial uncertainties, combined with restrictive policy changes affecting international scholars, have forced departments to be cautious with admissions. Consequently, incoming graduate student enrollment (excluding the Sloan School and EECS MEng) has dropped by nearly 20%—representing roughly 500 fewer students. President Kornbluth warned that this decline threatens MIT’s research momentum, reduces mentorship for undergraduates, and ultimately "chokes off" the nation’s supply of future scientific solutions.

**Response and Mitigation**
To navigate these challenges, MIT is implementing several strategies:
*   **Aggressive Grant Pursuit:** Faculty recently submitted 176 proposals for the Department of Energy’s Genesis Mission.
*   **Industry Partnerships:** Strengthening ties with the private sector, such as the newly launched MIT-IBM Computing Research Lab.
*   **New Revenue Streams:** Exploring masters-only programs and revitalizing philanthropic efforts through Resource Development.
*   **Advocacy:** Working with policymakers in Washington to oppose the endowment tax and emphasize the importance of curiosity-driven research.

While describing the outlook as "chilly," Kornbluth expressed confidence in the community’s resilience and creativity in sustaining MIT’s mission during this difficult period.

---

## 8. Fossils show millipede and centipede ancestors evolved legs underwater

**原文标题**: Fossils show millipede and centipede ancestors evolved legs underwater

**原文链接**: [https://phys.org/news/2026-05-ancient-sea-fossils-millipede-centipede.html](https://phys.org/news/2026-05-ancient-sea-fossils-millipede-centipede.html)

生成摘要时出错

---

## 9. Understanding the Linux Kernel: The Linux Kernel Startup

**原文标题**: Understanding the Linux Kernel: The Linux Kernel Startup

**原文链接**: [https://internals-for-interns.com/posts/linux-kernel-startup/](https://internals-for-interns.com/posts/linux-kernel-startup/)

生成摘要时出错

---

## 10. Terranox AI (YC W26) Is Hiring a Founding AI/ML Engineer and Summer AI/ML Intern

**原文标题**: Terranox AI (YC W26) Is Hiring a Founding AI/ML Engineer and Summer AI/ML Intern

**原文链接**: [https://www.workatastartup.com/companies/terranox-ai](https://www.workatastartup.com/companies/terranox-ai)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 2 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 3 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 4 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 5 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 6 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 7 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 8 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 9 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 10 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 11 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 12 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 13 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 14 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 15 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 16 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 17 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 18 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 19 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 20 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 21 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 22 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 23 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 24 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 25 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 26 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 27 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 28 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 29 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 30 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 31 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 32 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 33 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 34 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 35 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 36 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 37 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 38 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 39 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 40 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 41 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 42 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 43 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 44 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 45 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 46 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 47 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 48 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 49 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 50 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 51 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 52 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 53 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 54 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 55 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 56 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 57 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 58 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 59 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 60 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 61 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 62 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 63 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 64 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 65 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 66 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 67 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 68 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 69 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 70 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 71 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 72 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 73 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 74 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 75 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 76 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 77 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 78 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 79 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 80 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 81 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 82 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 83 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 84 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 85 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 86 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 87 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 88 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 89 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 90 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 91 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 92 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 93 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 94 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 95 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 96 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 97 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 98 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 99 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 100 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 101 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 102 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 103 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 104 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 105 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 106 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 107 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 108 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 109 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 110 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 111 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 112 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 113 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 114 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 115 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 116 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 117 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 118 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 119 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 120 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 121 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 122 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 123 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 124 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 125 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 126 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 127 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 128 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 129 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 130 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 131 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 132 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 133 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 134 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 135 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 136 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 137 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 138 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 139 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 140 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 141 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 142 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 143 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 144 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 145 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 146 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 147 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 148 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 149 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 150 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 151 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 152 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 153 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 154 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 155 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 156 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 157 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 158 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 159 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 160 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 161 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 162 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 163 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 164 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 165 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 166 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 167 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 168 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 169 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 170 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 171 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 172 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 173 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 174 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 175 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 176 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 177 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 178 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 179 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 180 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 181 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 182 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 183 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 184 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 185 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 186 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 187 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 188 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 189 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 190 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 191 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 192 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 193 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 194 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 195 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 196 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 197 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 198 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 199 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 200 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 201 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 202 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 203 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 204 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 205 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 206 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 207 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 208 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 209 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 210 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 211 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 212 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 213 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 214 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 215 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 216 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 217 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 218 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 219 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 220 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 221 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 222 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 223 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 224 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 225 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 226 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 227 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 228 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 229 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 230 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 231 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 232 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 233 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 234 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 235 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 236 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 237 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 238 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 239 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 240 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 241 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 242 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 243 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 244 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 245 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 246 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 247 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 248 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 249 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 250 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 251 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 252 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 253 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 254 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 255 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 256 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 257 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 258 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 259 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 260 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 261 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 262 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 263 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 264 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 265 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 266 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 267 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 268 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 269 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 270 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 271 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 272 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 273 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 274 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 275 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 276 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 277 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 278 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 279 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 280 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 281 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 282 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 283 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 284 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 285 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 286 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 287 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 288 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 289 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 290 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 291 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 292 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 293 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 294 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 295 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 296 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 297 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 298 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 299 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 300 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 301 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 302 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 303 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 304 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 305 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 306 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 307 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 308 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 309 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 310 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 311 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 312 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 313 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 314 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 315 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 316 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 317 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 318 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 319 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 320 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 321 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 322 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 323 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 324 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 325 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 326 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 327 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 328 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 329 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 330 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 331 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 332 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 333 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 334 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 335 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 336 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 337 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 338 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 339 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 340 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 341 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 342 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 343 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 344 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 345 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 346 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 347 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 348 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 349 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 350 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 351 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 352 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 353 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 354 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 355 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 356 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 357 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 358 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 359 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 360 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 361 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 362 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 363 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 364 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 365 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 366 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 367 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 368 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 369 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 370 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 371 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 372 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 373 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 374 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 375 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 376 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 377 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 378 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 379 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 380 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 381 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 382 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 383 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 384 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 385 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 386 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 387 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 388 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 389 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 390 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 391 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 392 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 393 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 394 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 395 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 396 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 397 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 398 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 399 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 400 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 401 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 402 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 403 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 404 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 405 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 406 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 407 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 408 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 409 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 410 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 411 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 412 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 413 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 414 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 415 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 416 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 417 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 418 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 419 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 420 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
