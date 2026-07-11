# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-07-11.md)

*最后自动更新时间: 2026-07-11 18:17:52*
## 1. 现代装饰或正让人们的大脑不堪重负。

**原文标题**: Modern Decor May Be Straining People's Brains

**原文链接**: [https://studyfinds.com/modern-decor-may-be-straining-peoples-brains/](https://studyfinds.com/modern-decor-may-be-straining-peoples-brains/)

发表在《视觉》（*Vision*，2026）杂志上的一项全面科学综述表明，现代建筑和照明设计可能因使人脑过度劳累而导致显著的身体不适。这项由32名研究人员组成的全球团队撰写的研究提出了一个假设，即“视觉不适”——包括头痛、恶心和眼睛疲劳等症状——源于视觉皮层的代谢过载。

核心理论认为，由于人类大脑进化的目的是处理自然界中可预测的有机构造，因此它难以高效地编码城市环境中常见的具有高度重复性、高对比度和闪烁特性的刺激。诸如条纹地板、网格化建筑外立面以及密集文本等特征，需要过度的神经活动和氧气消耗，这在本质上触发了生理警报。

虽然视觉不适影响广泛，但某些群体尤其脆弱。这包括神经多样性人士（如自闭症、多动症或阅读障碍患者）以及偏头痛或癫痫患者。研究人员认为，这些群体抑制过度活跃神经信号的能力可能较弱，使其更易受“编码效率低下”的影响。文中强调的具体诱因包括由闪烁的LED灯引起的“幻影阵列”效应，以及现代汽车大灯中的高频调制。

为应对这些挑战，该综述提出了几项基于证据的干预措施：
*   **建筑设计转型：** 设计具有较低对比度图案的建筑，并在施工前利用软件评估设计的“压力性”。
*   **个人辅助：** 使用精密染色镜片或彩色覆盖片，使大脑对复杂刺激的反应恢复正常。
*   **照明标准：** 减少LED系统中的快速闪烁（时间光调制）。

研究人员最终指出，视觉不适是一种可衡量的物理现象，而非主观诉求。通过使现代设计符合大脑的进化预期，建筑师和工程师可以创造出更具包容性、更注重健康的环境。

---

## 2. 我们将 PgBouncer 的吞吐量提升了 4 倍

**原文标题**: We scaled PgBouncer to 4x throughput

**原文链接**: [https://clickhouse.com/blog/pgbouncer-clickhouse-managed-postgres](https://clickhouse.com/blog/pgbouncer-clickhouse-managed-postgres)

本文解释了如何克服 PgBouncer 的性能限制。传统上，PgBouncer 是单线程的，无论机器配置如何，都只能利用单个 CPU 核心。这在高吞吐量环境中造成了瓶颈，导致连接池在 PostgreSQL 数据库达到负载极限之前就已触及性能天花板。

**解决方案：多进程集群**
为了提升吞吐量，ClickHouse Managed Postgres 部署了与可用 CPU 核心数成比例的 PgBouncer 进程集群。通过利用内核的 `so_reuseport` 特性，所有进程都绑定到同一个端口。随后，内核在进程集群间对传入的客户端连接进行负载均衡，使这种多进程设置对用户透明。

**解决查询取消的“难题”**
这种方法面临的一个重大挑战是查询取消。由于取消请求通过新连接到达，内核可能会将请求路由到与处理原始查询不同的进程。为了解决这个问题，作者实现了 **对等通信 (peering)**，允许进程相互感知并将取消请求转发给正确的会话所有者。

**资源管理与性能**
为了保护数据库，连接限制（如 `max_client_conn`）被分配到整个集群中。在 16 核 vCPU 的 AWS 实例上进行的测试证明了该架构的有效性：
*   **吞吐量：** 单个 PgBouncer 进程的峰值约为每秒 8.7 万次事务 (TPS)，而集群达到了约 33.6 万次 TPS——提升了 **4 倍**。
*   **CPU 利用率：** 当单个进程被限制在单个核心（导致 15 个核心闲置）时，集群成功实现了硬件级扩展，利用了 16 核总容量的约 50%。

**结论**
通过根据可用核心数配置 PgBouncer 集群规模，并使用对等通信处理取消请求，连接池从系统瓶颈转变为可扩展的基础设施。此配置目前已成为 ClickHouse Managed Postgres 的默认设置。

---

## 3. 奇异值分解的早期历史 (1993) [pdf]

**原文标题**: The early History of the Singular Value Decomposition (1993) [pdf]

**原文链接**: [https://www.math.ucdavis.edu/~saito/courses/229A/stewart-svd.pdf](https://www.math.ucdavis.edu/~saito/courses/229A/stewart-svd.pdf)

生成摘要时出错

---

## 4. 美国女划艇运动员完成从加州到夏威夷的历史性单人航行。

**原文标题**: Female US rower completes historic solo journey from California to Hawaii

**原文链接**: [https://www.theguardian.com/us-news/2026/jul/04/california-hawaii-rowing-solo-journey](https://www.theguardian.com/us-news/2026/jul/04/california-hawaii-rowing-solo-journey)

大峡谷职业漂流向导凯尔西·普芬德勒（Kelsey Pfendler）完成了一项具有历史意义的单人划船航行，从加利福尼亚州蒙特雷出发，成功抵达夏威夷州檀香山。普芬德勒驾驶着她那艘21英尺长的“莉莉”号（Lily）船，在海上航行了近一个半月，跨越2400多英里后抵达威基基海滩。

根据国际海洋赛艇协会（Ocean Rowing Society International）的记录，普芬德勒不到44天的完赛时间似乎打破了多项纪录。她不仅是首位完成该单人跨洋航行的美国女性，也是完成此举最年轻的女性。此外，她的成绩还同时超越了此前86天的女性纪录和52天的男性纪录。

在整个航行过程中，普芬德勒向社交媒体上的数十万粉丝记录了她的经历，分享了单人海洋航行在后勤和体力上的重重挑战。她详细描述了与手部水泡、不利洋流以及睡眠不足的搏斗，同时也展示了海上的日常生活——从烹饪、淡化海水，到幽默地自嘲额头上因戴帽子留下的晒痕。

周五晚上抵达檀香山后，普芬德勒表示，希望自己的成就能够激励他人去挑战那些“宏大、艰难且令人畏惧”的目标。她指出，虽然一个人最初可能觉得自己没有足够的力量去完成挑战，但“绝对有足够的力量去开启它”。

她的这项创纪录壮举也正值该地区其他显著的耐力挑战进行之际，其中包括马拉松游泳运动员凯瑟琳·布里德（Catherine Breed）正在尝试游完整个900英里长的加利福尼亚海岸线。

---

## 5. AI Can't Recreate the Thrust Game (But It Can Help You Understand It)

**原文标题**: AI Can't Recreate the Thrust Game (But It Can Help You Understand It)

**原文链接**: [https://www.jamesdrandall.com/posts/thrust_ai_powered_software_archaeology/](https://www.jamesdrandall.com/posts/thrust_ai_powered_software_archaeology/)

在本文中，作者详细介绍了他在现代浏览器上重现 1986 年 BBC Micro 经典游戏《Thrust》的过程。尽管最初尝试让 AI (Claude) 根据规格说明直接生成游戏只得到了无法运行的“垃圾代码”，但该项目随后演变成了一次深度的“考古”探索，AI 在其中成为了解析 6502 汇编代码的强大工具。

作者发现，《Thrust》的“魔力”并非源于标准的物理定律，而是源于其特定的时序和硬件特性。通过利用 AI 分析原始源码，他发现游戏物理逻辑并非以系统的 50Hz 垂直同步频率运行，而是被限制在约 12.5Hz，且旋转动作每四个刻度会跳过一次。他还发现了非对称阻力——即水平移动比垂直移动更具“粘滞感”——这赋予了飞船独特的重量感。

为了确保真实性，作者不仅停留于表面的模仿：
*   **音频：** 他模拟了 SN76489 声音芯片和 BBC Micro 的 MOS 包络处理器，而非使用采样音频，从而确保引擎轰鸣声和爆炸声与原版完全一致。
*   **图形：** 他提取了原始的手工优化精灵图，并实现了扫描线奇偶校验多边形填充，以还原 BBC 的视觉风格。
*   **验证：** 他实现了依靠定时按键运行的原始“演示模式”。演示画面在他的版本中能够准确重放，证明了其物理逻辑和时序得到了完美还原。

最终，作者得出结论：虽然 AI 目前还无法仅通过提示词直观地复制经典游戏的“灵魂”或“手感”，但它在技术分析和加速特定子系统开发方面是极其出色的工具。最终的成品是对 Jeremy C. Smith 原始杰作的忠实复刻，完美契合了原版的优雅。

---

## 6. 含铅汽油自发明之日起就是已知的毒物 (2016)

**原文标题**: Leaded Gas Was a Known Poison the Day It Was Invented (2016)

**原文链接**: [https://www.smithsonianmag.com/smart-news/leaded-gas-poison-invented-180961368/](https://www.smithsonianmag.com/smart-news/leaded-gas-poison-invented-180961368/)

1921年，通用汽车工程师托马斯·米基利（Thomas Midgley Jr.）发现四乙基铅（TEL）可以消除发动机的“爆震”现象。尽管当时已存在乙醇等更安全且有效的替代品，但通用汽车和杜邦等公司仍强力推行四乙基铅，因为它具有专利权，能确保企业对燃料市场的控制。

四乙基铅的毒性从一开始就已有详尽记载。米基利本人曾患铅中毒，多名炼油厂工人在早期生产过程中丧生。然而，企业利益集团成功淡化了这些危险。1926年的一份公共卫生报告得出结论称，虽然存在铅接触情况，但对公众的直接风险微乎其微，这实际上是将长期的健康后果转嫁给了后代。

直到20世纪70年代，美国环保署（EPA）才启动了为期数年的淘汰含铅汽油的法律和监管程序。这种延误导致了长达数十年的广泛环境污染和灾难性的公共卫生后果。此后的研究将铅接触（对儿童伤害最大）与永久性神经损伤、智商降低、行为问题以及更高的暴力犯罪率联系在一起。

虽然全球车辆使用含铅汽油的历史在2021年正式宣告结束，但文章强调，20世纪排放到大气中的铅依然存在于环境中，时至今日仍对人类健康构成持续威胁。

---

## 7. 新研究显示：爱因斯坦的相对论主宰重元素中的化学键

**原文标题**: Einstein's relativity rules chemical bonds in heavy elements, new research shows

**原文链接**: [https://www.brown.edu/news/2026-07-09/chemical-bonds-relativity](https://www.brown.edu/news/2026-07-09/chemical-bonds-relativity)

Researchers at Brown University have provided direct spectroscopic evidence that Einstein’s theory of relativity alters the nature of triple chemical bonds in heavy elements, challenging a fundamental principle taught in chemistry textbooks.

Traditional chemistry states that a triple bond consists of one "head-on" sigma bond and two "side-by-side" pi bonds. However, this study, published in *Science*, reveals that this model breaks down at the bottom of the periodic table. Using bismuth—a heavy element adjacent to lead—the team led by Professor Lai-Sheng Wang analyzed bismuth-carbon bonds using photoelectron spectroscopy at near-absolute zero temperatures.

The researchers found that the massive nuclei of heavy elements cause orbiting electrons to reach speeds significant enough for relativistic effects to take hold. This triggers a state known as **spin-orbit coupling**, where an electron’s spin and orbit are no longer independent. This coupling blurs the distinction between sigma and pi bonds, resulting in a hybridized structure that behaves more like one pi bond and two "smeared" sigma-pi bonds.

This discovery is more than a theoretical correction; it has practical implications for materials science. Bismuth is currently being researched as a non-toxic alternative to lead in next-generation solar cells and as a candidate for quantum computing and quantum materials. As heavy element chemistry becomes increasingly vital, the researchers suggest these findings may lead to a rewriting of chemistry textbooks to better reflect how the universe operates at the relativistic level.

---

## 8. Sixtyfour (YC P25) Is Hiring

**原文标题**: Sixtyfour (YC P25) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/sixtyfour/jobs/bIbgQkL-operations-associate-data-samples-customer-success](https://www.ycombinator.com/companies/sixtyfour/jobs/bIbgQkL-operations-associate-data-samples-customer-success)

生成摘要时出错

---

## 9. QuadRF 能发现无人机并穿透墙壁看到 WiFi

**原文标题**: QuadRF can spot drones and see WiFi through my wall

**原文链接**: [https://www.jeffgeerling.com/blog/2026/quadrf-can-spot-drones-and-see-wifi-through-my-wall/](https://www.jeffgeerling.com/blog/2026/quadrf-can-spot-drones-and-see-wifi-through-my-wall/)

**QuadRF** is an open-source, handheld phased-array radio system designed for advanced signal processing, beamforming, and RF visualization. Built around a **Raspberry Pi 5** and an FPGA board, the device operates in the 4.9–6 GHz range, allowing users to track drones in flight and visualize WiFi signals—even through walls.

Developed by former SpaceX engineer Martin McCormick, the QuadRF is a scaled-down iteration of a larger project aimed at building a "Moon-scale" antenna array for radio astronomy. A key technical innovation is its use of the Raspberry Pi 5’s **MIPI lanes** for high-bandwidth (over 5 Gbps) I/Q data streaming. By reverse-engineering the MIPI protocol, the developers achieved low-latency data transfer that outperforms traditional USB connections, enabling the device to handle hundreds of millions of samples per second without loss.

The system features a web-based interface and an **Augmented Reality (AR) visualizer** that displays RF frequencies as colorful "blobs." In hands-on testing, the author successfully tracked a DJI Mini Pro 4 drone and identified specific 5 GHz WiFi channels. While the reviewer noted that the current UI is somewhat unrefined, the hardware's ability to perform sophisticated beamforming on a hobbyist platform was described as "blown away."

The QuadRF is currently in the crowdfunding stage on **Crowd Supply**, with a basic kit priced at $499. Future versions plan to move from 3D-printed to injection-molded enclosures. The project highlights how professional-grade surveillance and radio tools are becoming increasingly accessible to the open-source community.

---

## 10. Google Search lets creators know more about their reach

**原文标题**: Google Search lets creators know more about their reach

**原文链接**: [https://www.theverge.com/tech/961955/google-search-console-reach-platform-properties](https://www.theverge.com/tech/961955/google-search-console-reach-platform-properties)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 2 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 3 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 4 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 5 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 6 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 7 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 8 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 9 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 10 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 11 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 12 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 13 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 14 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 15 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 16 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 17 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 18 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 19 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 20 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 21 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 22 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 23 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 24 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 25 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 26 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 27 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 28 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 29 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 30 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 31 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 32 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 33 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 34 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 35 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 36 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 37 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 38 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 39 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 40 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 41 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 42 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 43 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 44 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 45 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 46 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 47 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 48 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 49 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 50 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 51 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 52 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 53 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 54 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 55 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 56 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 57 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 58 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 59 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 60 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 61 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 62 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 63 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 64 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 65 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 66 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 67 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 68 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 69 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 70 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 71 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 72 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 73 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 74 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 75 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 76 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 77 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 78 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 79 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 80 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 81 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 82 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 83 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 84 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 85 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 86 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 87 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 88 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 89 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 90 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 91 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 92 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 93 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 94 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 95 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 96 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 97 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 98 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 99 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 100 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 101 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 102 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 103 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 104 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 105 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 106 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 107 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 108 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 109 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 110 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 111 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 112 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 113 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 114 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 115 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 116 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 117 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 118 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 119 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 120 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 121 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 122 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 123 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 124 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 125 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 126 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 127 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 128 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 129 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 130 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 131 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 132 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 133 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 134 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 135 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 136 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 137 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 138 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 139 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 140 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 141 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 142 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 143 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 144 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 145 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 146 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 147 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 148 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 149 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 150 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 151 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 152 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 153 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 154 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 155 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 156 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 157 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 158 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 159 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 160 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 161 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 162 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 163 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 164 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 165 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 166 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 167 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 168 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 169 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 170 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 171 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 172 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 173 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 174 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 175 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 176 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 177 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 178 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 179 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 180 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 181 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 182 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 183 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 184 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 185 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 186 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 187 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 188 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 189 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 190 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 191 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 192 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 193 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 194 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 195 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 196 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 197 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 198 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 199 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 200 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 201 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 202 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 203 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 204 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 205 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 206 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 207 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 208 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 209 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 210 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 211 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 212 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 213 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 214 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 215 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 216 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 217 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 218 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 219 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 220 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 221 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 222 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 223 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 224 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 225 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 226 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 227 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 228 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 229 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 230 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 231 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 232 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 233 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 234 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 235 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 236 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 237 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 238 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 239 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 240 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 241 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 242 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 243 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 244 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 245 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 246 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 247 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 248 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 249 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 250 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 251 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 252 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 253 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 254 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 255 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 256 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 257 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 258 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 259 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 260 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 261 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 262 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 263 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 264 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 265 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 266 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 267 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 268 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 269 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 270 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 271 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 272 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 273 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 274 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 275 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 276 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 277 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 278 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 279 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 280 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 281 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 282 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 283 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 284 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 285 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 286 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 287 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 288 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 289 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 290 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 291 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 292 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 293 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 294 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 295 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 296 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 297 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 298 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 299 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 300 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 301 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 302 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 303 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 304 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 305 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 306 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 307 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 308 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 309 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 310 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 311 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 312 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 313 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 314 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 315 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 316 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 317 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 318 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 319 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 320 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 321 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 322 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 323 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 324 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 325 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 326 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 327 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 328 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 329 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 330 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 331 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 332 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 333 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 334 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 335 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 336 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 337 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 338 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 339 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 340 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 341 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 342 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 343 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 344 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 345 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 346 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 347 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 348 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 349 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 350 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 351 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 352 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 353 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 354 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 355 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 356 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 357 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 358 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 359 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 360 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 361 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 362 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 363 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 364 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 365 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 366 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 367 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 368 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 369 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 370 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 371 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 372 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 373 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 374 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 375 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 376 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 377 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 378 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 379 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 380 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 381 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 382 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 383 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 384 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 385 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 386 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 387 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 388 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 389 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 390 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 391 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 392 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 393 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 394 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 395 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 396 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 397 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 398 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 399 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 400 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 401 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 402 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 403 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 404 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 405 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 406 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 407 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 408 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 409 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 410 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 411 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 412 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 413 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 414 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 415 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 416 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 417 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 418 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 419 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 420 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 421 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 422 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 423 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 424 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 425 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 426 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 427 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 428 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 429 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 430 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 431 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 432 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 433 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 434 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 435 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 436 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 437 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 438 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 439 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 440 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 441 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 442 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 443 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 444 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 445 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 446 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 447 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 448 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 449 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 450 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 451 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 452 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 453 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 454 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 455 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 456 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 457 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 458 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 459 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 460 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 461 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 462 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 463 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 464 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 465 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 466 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 467 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 468 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 469 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 470 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 471 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 472 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 473 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 474 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 475 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 476 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 477 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 478 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
