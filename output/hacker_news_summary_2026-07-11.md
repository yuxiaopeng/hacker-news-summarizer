# Hacker News 热门文章摘要 (2026-07-11)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Amber the programming language compiled to Bash/Ksh/Zsh

**原文标题**: Amber the programming language compiled to Bash/Ksh/Zsh

**原文链接**: [https://amber-lang.com/](https://amber-lang.com/)

生成摘要时出错

---

## 12. Speculations Concerning the First Ultraintelligent Machine (1965) [pdf]

**原文标题**: Speculations Concerning the First Ultraintelligent Machine (1965) [pdf]

**原文链接**: [https://languagelog.ldc.upenn.edu/myl/Good1964.pdf](https://languagelog.ldc.upenn.edu/myl/Good1964.pdf)

生成摘要时出错

---

## 13. Apple sues OpenAI, accuses ex-employees of stealing trade secrets

**原文标题**: Apple sues OpenAI, accuses ex-employees of stealing trade secrets

**原文链接**: [https://9to5mac.com/2026/07/10/apple-sues-openai-trade-secret-theft/](https://9to5mac.com/2026/07/10/apple-sues-openai-trade-secret-theft/)

生成摘要时出错

---

## 14. Book: RISC-V System-on-Chip Design

**原文标题**: Book: RISC-V System-on-Chip Design

**原文链接**: [https://www.amazon.com/RISC-V-Microprocessor-System-Chip-Design/dp/0323994989](https://www.amazon.com/RISC-V-Microprocessor-System-Chip-Design/dp/0323994989)

生成摘要时出错

---

## 15. Digital Deli, 1984 book by early PC hackers and enthusiasts

**原文标题**: Digital Deli, 1984 book by early PC hackers and enthusiasts

**原文链接**: [https://www.atariarchives.org/deli/](https://www.atariarchives.org/deli/)

生成摘要时出错

---

## 16. Show HN: Learn by rebuilding Redis, Git, a database from scratch

**原文标题**: Show HN: Learn by rebuilding Redis, Git, a database from scratch

**原文链接**: [https://shipthatcode.com](https://shipthatcode.com)

生成摘要时出错

---

## 17. Otary – Image and Geometry Python Library Now Has Tutorials

**原文标题**: Otary – Image and Geometry Python Library Now Has Tutorials

**原文链接**: [https://alexandrepoupeau.com/otary/learn/](https://alexandrepoupeau.com/otary/learn/)

生成摘要时出错

---

## 18. BLISS

**原文标题**: BLISS

**原文链接**: [https://en.wikipedia.org/wiki/BLISS](https://en.wikipedia.org/wiki/BLISS)

生成摘要时出错

---

## 19. The Victorian War on Rabies

**原文标题**: The Victorian War on Rabies

**原文链接**: [https://www.historytoday.com/archive/feature/mad-dogs-and-englishmen-winning-war-rabies](https://www.historytoday.com/archive/feature/mad-dogs-and-englishmen-winning-war-rabies)

生成摘要时出错

---

## 20. Tropical forests facing increasing risks of exposure to critical temp thresholds

**原文标题**: Tropical forests facing increasing risks of exposure to critical temp thresholds

**原文链接**: [https://www.pnas.org/doi/10.1073/pnas.2528622123](https://www.pnas.org/doi/10.1073/pnas.2528622123)

生成摘要时出错

---

## 21. An update on residential proxies and the scraper situation

**原文标题**: An update on residential proxies and the scraper situation

**原文链接**: [https://lwn.net/SubscriberLink/1080822/990a8a5e2d379085/](https://lwn.net/SubscriberLink/1080822/990a8a5e2d379085/)

生成摘要时出错

---

## 22. Ghost Font: A font that humans can read but AI cannot

**原文标题**: Ghost Font: A font that humans can read but AI cannot

**原文链接**: [https://www.mixfont.com/ghost-font](https://www.mixfont.com/ghost-font)

生成摘要时出错

---

## 23. SpaceX wants to launch 100k more Starlink satellites for 100x the bandwidth

**原文标题**: SpaceX wants to launch 100k more Starlink satellites for 100x the bandwidth

**原文链接**: [https://www.zdnet.com/home-and-office/networking/spacex-wants-to-launch-100000-more-starlink-satellites/](https://www.zdnet.com/home-and-office/networking/spacex-wants-to-launch-100000-more-starlink-satellites/)

生成摘要时出错

---

## 24. FCC approves test of space mirror to light night sky

**原文标题**: FCC approves test of space mirror to light night sky

**原文链接**: [https://theconversation.com/the-u-s-just-approved-a-giant-space-mirror-to-test-sunlight-on-demand-low-earth-orbit-is-getting-weird-283482](https://theconversation.com/the-u-s-just-approved-a-giant-space-mirror-to-test-sunlight-on-demand-low-earth-orbit-is-getting-weird-283482)

生成摘要时出错

---

## 25. An iroh powered smart fan

**原文标题**: An iroh powered smart fan

**原文链接**: [https://www.iroh.computer/blog/an-iroh-powered-smart-fan](https://www.iroh.computer/blog/an-iroh-powered-smart-fan)

生成摘要时出错

---

## 26. Earendel (Astronomical Object)

**原文标题**: Earendel (Astronomical Object)

**原文链接**: [https://en.wikipedia.org/wiki/Earendel_(astronomical_object)](https://en.wikipedia.org/wiki/Earendel_(astronomical_object))

生成摘要时出错

---

## 27. Reverse centaurs are the answer to the AI paradox

**原文标题**: Reverse centaurs are the answer to the AI paradox

**原文链接**: [https://pluralistic.net/2025/09/11/vulgar-thatcherism/#there-is-an-alternative](https://pluralistic.net/2025/09/11/vulgar-thatcherism/#there-is-an-alternative)

生成摘要时出错

---

## 28. The mask that compiles to nothing: how HotSpots JIT learned to reason about bits

**原文标题**: The mask that compiles to nothing: how HotSpots JIT learned to reason about bits

**原文链接**: [https://questdb.com/blog/jvm-jit-known-bits/](https://questdb.com/blog/jvm-jit-known-bits/)

生成摘要时出错

---

## 29. Good Tools Are Invisible

**原文标题**: Good Tools Are Invisible

**原文链接**: [https://www.gingerbill.org/article/2026/07/10/good-tools-are-invisible/](https://www.gingerbill.org/article/2026/07/10/good-tools-are-invisible/)

生成摘要时出错

---

## 30. Why it's so difficult to produce American-made medical gloves

**原文标题**: Why it's so difficult to produce American-made medical gloves

**原文链接**: [https://www.bloomberg.com/news/features/2026-07-07/why-it-s-so-difficult-to-produce-100-american-made-medical-gloves](https://www.bloomberg.com/news/features/2026-07-07/why-it-s-so-difficult-to-produce-100-american-made-medical-gloves)

生成摘要时出错

---

## 31. AI 2040: Plan A

**原文标题**: AI 2040: Plan A

**原文链接**: [https://ai-2040.com/](https://ai-2040.com/)

生成摘要时出错

---

## 32. Late Bronze Age Collapse

**原文标题**: Late Bronze Age Collapse

**原文链接**: [https://acoup.blog/2026/01/30/collections-the-late-bronze-age-collapse-a-very-brief-introduction/](https://acoup.blog/2026/01/30/collections-the-late-bronze-age-collapse-a-very-brief-introduction/)

生成摘要时出错

---

## 33. The vintage beauty of Soviet control rooms (2018)

**原文标题**: The vintage beauty of Soviet control rooms (2018)

**原文链接**: [https://designyoutrust.com/2018/01/vintage-beauty-soviet-control-rooms/](https://designyoutrust.com/2018/01/vintage-beauty-soviet-control-rooms/)

生成摘要时出错

---

## 34. Silent speech with ultrasound

**原文标题**: Silent speech with ultrasound

**原文链接**: [https://alephneuro.com/blog/silent-speech](https://alephneuro.com/blog/silent-speech)

生成摘要时出错

---

## 35. The tech of 'Terminator 2' – an oral history (2017)

**原文标题**: The tech of 'Terminator 2' – an oral history (2017)

**原文链接**: [https://vfxblog.com/2017/08/23/the-tech-of-terminator-2-an-oral-history/](https://vfxblog.com/2017/08/23/the-tech-of-terminator-2-an-oral-history/)

生成摘要时出错

---

## 36. After 7 years in production, Scarf has reluctantly moved away from Haskell

**原文标题**: After 7 years in production, Scarf has reluctantly moved away from Haskell

**原文链接**: [https://avi.press/posts/2026-07-10-after-7-years-in-production-scarf-has-reluctantly-moved-away-from-haskell.html](https://avi.press/posts/2026-07-10-after-7-years-in-production-scarf-has-reluctantly-moved-away-from-haskell.html)

生成摘要时出错

---

## 37. Theories of Deep Learning

**原文标题**: Theories of Deep Learning

**原文链接**: [https://astledsa.substack.com/p/theories-of-deep-learning](https://astledsa.substack.com/p/theories-of-deep-learning)

生成摘要时出错

---

## 38. Combustion engine web-based simulator

**原文标题**: Combustion engine web-based simulator

**原文链接**: [https://combustionlab.net](https://combustionlab.net)

生成摘要时出错

---

## 39. Alternate clock designs and time systems

**原文标题**: Alternate clock designs and time systems

**原文链接**: [https://serialc.github.io/altClocks/](https://serialc.github.io/altClocks/)

生成摘要时出错

---

## 40. Your code is fast – if you're lucky

**原文标题**: Your code is fast – if you're lucky

**原文链接**: [https://tiki.li/blog/lucky_code.html](https://tiki.li/blog/lucky_code.html)

生成摘要时出错

---

## 41. Show HN: Getting GLM 5.2 running on my slow computer

**原文标题**: Show HN: Getting GLM 5.2 running on my slow computer

**原文链接**: [https://github.com/JustVugg/colibri](https://github.com/JustVugg/colibri)

生成摘要时出错

---

## 42. Inference Optimization for MiMo v2.5: Pushing Hybrid SWA Efficiency to the Limit

**原文标题**: Inference Optimization for MiMo v2.5: Pushing Hybrid SWA Efficiency to the Limit

**原文链接**: [https://mimo.xiaomi.com/blog/mimo-v2-5-inference](https://mimo.xiaomi.com/blog/mimo-v2-5-inference)

生成摘要时出错

---

## 43. Is There Any End to the Atlantic's "End-Ism" Fetish?

**原文标题**: Is There Any End to the Atlantic's "End-Ism" Fetish?

**原文链接**: [https://newrepublic.com/article/212923/the-atlantic-magazine-endism-fetish](https://newrepublic.com/article/212923/the-atlantic-magazine-endism-fetish)

生成摘要时出错

---

## 44. Snails' teeth beats spider silk as nature's strongest material (2015)

**原文标题**: Snails' teeth beats spider silk as nature's strongest material (2015)

**原文链接**: [https://www.smithsonianmag.com/smart-news/spider-silk-loses-top-spot-natures-strongest-material-snails-teeth-180954346/](https://www.smithsonianmag.com/smart-news/spider-silk-loses-top-spot-natures-strongest-material-snails-teeth-180954346/)

生成摘要时出错

---

## 45. A love letter to flashcards

**原文标题**: A love letter to flashcards

**原文链接**: [https://lesleylai.info/en/flashcards/](https://lesleylai.info/en/flashcards/)

生成摘要时出错

---

## 46. New York City to ban deceptive subscription practices

**原文标题**: New York City to ban deceptive subscription practices

**原文链接**: [https://www.theguardian.com/us-news/2026/jul/10/new-york-city-deceptive-subscriptions-ban](https://www.theguardian.com/us-news/2026/jul/10/new-york-city-deceptive-subscriptions-ban)

生成摘要时出错

---

## 47. Computation as a universal and fundamental concept

**原文标题**: Computation as a universal and fundamental concept

**原文链接**: [https://ergo.org/courses/computation-as-a-universal-and-fundamental-concept](https://ergo.org/courses/computation-as-a-universal-and-fundamental-concept)

生成摘要时出错

---

## 48. GPT-5.6 Sol Ultra produces proof of the Cycle Double Cover Conjecture [pdf]

**原文标题**: GPT-5.6 Sol Ultra produces proof of the Cycle Double Cover Conjecture [pdf]

**原文链接**: [https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_proof.pdf](https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_proof.pdf)

生成摘要时出错

---

## 49. Show HN: 18 Words

**原文标题**: Show HN: 18 Words

**原文链接**: [https://18words.com/](https://18words.com/)

生成摘要时出错

---

## 50. War Atlas: An interactive cartography of every named war in human history

**原文标题**: War Atlas: An interactive cartography of every named war in human history

**原文链接**: [https://waratlas.org](https://waratlas.org)

生成摘要时出错

---

## 51. Successful companies go blind

**原文标题**: Successful companies go blind

**原文链接**: [https://ianreppel.org/how-successful-companies-go-blind/](https://ianreppel.org/how-successful-companies-go-blind/)

生成摘要时出错

---

## 52. GhostLock, a stack-UAF that has existed in ALL Linux distributions for 15 years

**原文标题**: GhostLock, a stack-UAF that has existed in ALL Linux distributions for 15 years

**原文链接**: [https://nebusec.ai/research/ionstack-part-2/](https://nebusec.ai/research/ionstack-part-2/)

生成摘要时出错

---

## 53. Reimplementing pf as an eBPF/XDP dataplane on Linux

**原文标题**: Reimplementing pf as an eBPF/XDP dataplane on Linux

**原文链接**: [https://blog.nfsensei.org/the-packet-filter-reborn.html](https://blog.nfsensei.org/the-packet-filter-reborn.html)

生成摘要时出错

---

## 54. LisaFPGA: The Apple Lisa computer implemented inside an FPGA

**原文标题**: LisaFPGA: The Apple Lisa computer implemented inside an FPGA

**原文链接**: [https://github.com/alexthecat123/LisaFPGA](https://github.com/alexthecat123/LisaFPGA)

生成摘要时出错

---

## 55. GPT-5.6

**原文标题**: GPT-5.6

**原文链接**: [https://openai.com/index/gpt-5-6/](https://openai.com/index/gpt-5-6/)

生成摘要时出错

---

## 56. How Container Networking Works: Building a Bridge Network from Scratch

**原文标题**: How Container Networking Works: Building a Bridge Network from Scratch

**原文链接**: [https://labs.iximiuz.com/tutorials/container-networking-from-scratch](https://labs.iximiuz.com/tutorials/container-networking-from-scratch)

生成摘要时出错

---

## 57. Punk, or why I don't stream anymore

**原文标题**: Punk, or why I don't stream anymore

**原文链接**: [https://geohot.github.io//blog/jekyll/update/2026/05/03/punk-or-why-i-dont-stream.html](https://geohot.github.io//blog/jekyll/update/2026/05/03/punk-or-why-i-dont-stream.html)

生成摘要时出错

---

## 58. Preemption is GC for memory reordering (2019)

**原文标题**: Preemption is GC for memory reordering (2019)

**原文链接**: [https://pvk.ca/Blog/2019/01/09/preemption-is-gc-for-memory-reordering/](https://pvk.ca/Blog/2019/01/09/preemption-is-gc-for-memory-reordering/)

生成摘要时出错

---

## 59. Microsoft admits Windows 11 has a GDID tracker with no off switch

**原文标题**: Microsoft admits Windows 11 has a GDID tracker with no off switch

**原文链接**: [https://www.windowslatest.com/2026/07/10/you-cant-fully-disable-microsofts-gdid-windows-11-tracker-but-these-settings-limit-what-it-captures/](https://www.windowslatest.com/2026/07/10/you-cant-fully-disable-microsofts-gdid-windows-11-tracker-but-these-settings-limit-what-it-captures/)

生成摘要时出错

---

## 60. Show HN: Abralo – Free, easy way to run several Claude Code agents in one window

**原文标题**: Show HN: Abralo – Free, easy way to run several Claude Code agents in one window

**原文链接**: [https://abralo.com/](https://abralo.com/)

生成摘要时出错

---

## 61. TLS certificates for internal services done right

**原文标题**: TLS certificates for internal services done right

**原文链接**: [https://tuxnet.dev/posts/tls-for-internal-services/](https://tuxnet.dev/posts/tls-for-internal-services/)

生成摘要时出错

---

## 62. AI-generated videos to maximally drive a target brain region

**原文标题**: AI-generated videos to maximally drive a target brain region

**原文链接**: [https://nevo-project.epfl.ch/](https://nevo-project.epfl.ch/)

生成摘要时出错

---

## 63. Google Opposes Site Blocking in Europe as US Piracy Blocking Plans Gain Momentum

**原文标题**: Google Opposes Site Blocking in Europe as US Piracy Blocking Plans Gain Momentum

**原文链接**: [https://torrentfreak.com/google-opposes-site-blocking-in-europe-as-u-s-piracy-blocking-plans-gain-momentum/](https://torrentfreak.com/google-opposes-site-blocking-in-europe-as-u-s-piracy-blocking-plans-gain-momentum/)

生成摘要时出错

---

## 64. Postgres locks do not scale

**原文标题**: Postgres locks do not scale

**原文链接**: [https://www.recall.ai/blog/postgres-locks-do-not-scale](https://www.recall.ai/blog/postgres-locks-do-not-scale)

生成摘要时出错

---

## 65. El Niño Is Wreaking Havoc on Pacific Fisheries

**原文标题**: El Niño Is Wreaking Havoc on Pacific Fisheries

**原文链接**: [https://www.wired.com/story/el-nino-wreaking-havoc-on-pacific-fisheries/](https://www.wired.com/story/el-nino-wreaking-havoc-on-pacific-fisheries/)

生成摘要时出错

---

## 66. EU Commission: addictive design Instagram and Facebook in breach of the DSA

**原文标题**: EU Commission: addictive design Instagram and Facebook in breach of the DSA

**原文链接**: [https://ec.europa.eu/commission/presscorner/home/en](https://ec.europa.eu/commission/presscorner/home/en)

生成摘要时出错

---

## 67. We tried London's first driverless bus

**原文标题**: We tried London's first driverless bus

**原文链接**: [https://www.londoncentric.media/p/londons-first-driverless-bus](https://www.londoncentric.media/p/londons-first-driverless-bus)

生成摘要时出错

---

## 68. Ryanair passenger sucked toward broken window after midair engine failure

**原文标题**: Ryanair passenger sucked toward broken window after midair engine failure

**原文链接**: [https://simpleflying.com/ryanair-thessaloniki-diversion-window-damage/](https://simpleflying.com/ryanair-thessaloniki-diversion-window-damage/)

生成摘要时出错

---

## 69. Show HN: Runloom – Go-style coroutines for Python free-threaded

**原文标题**: Show HN: Runloom – Go-style coroutines for Python free-threaded

**原文链接**: [https://github.com/robertsdotpm/runloom](https://github.com/robertsdotpm/runloom)

生成摘要时出错

---

## 70. Parental device use and the adolescent-caregiver attachment bond

**原文标题**: Parental device use and the adolescent-caregiver attachment bond

**原文链接**: [https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1766665/full](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1766665/full)

生成摘要时出错

---

## 71. Decoding the obfuscated bash script on a Uniqlo t-shirt

**原文标题**: Decoding the obfuscated bash script on a Uniqlo t-shirt

**原文链接**: [https://tris.sherliker.net/blog/obfuscated-self-evaluating-bash-script-by-cdn-akamai-being-supplied-to-consumers-via-retail-stores/](https://tris.sherliker.net/blog/obfuscated-self-evaluating-bash-script-by-cdn-akamai-being-supplied-to-consumers-via-retail-stores/)

生成摘要时出错

---

## 72. Why American ambulance rides are so expensive

**原文标题**: Why American ambulance rides are so expensive

**原文链接**: [https://davidoks.blog/p/why-american-ambulance-rides-are](https://davidoks.blog/p/why-american-ambulance-rides-are)

生成摘要时出错

---

## 73. Ofcom Wants American Police to Collect Its Speech Fine

**原文标题**: Ofcom Wants American Police to Collect Its Speech Fine

**原文链接**: [https://reclaimthenet.org/ofcom-wants-american-police-to-collect-its-speech-fine](https://reclaimthenet.org/ofcom-wants-american-police-to-collect-its-speech-fine)

生成摘要时出错

---

## 74. Chinese courts allow heirs to inherit accounts of deceased gamers

**原文标题**: Chinese courts allow heirs to inherit accounts of deceased gamers

**原文链接**: [https://www.tomshardware.com/tech-industry/big-tech/chinese-courts-allow-heirs-to-inherent-accounts-of-deceased-gamers-multiple-cases-spanning-years-establish-precedent-for-digital-ownership-of-games-in-game-items-and-microtransactions](https://www.tomshardware.com/tech-industry/big-tech/chinese-courts-allow-heirs-to-inherent-accounts-of-deceased-gamers-multiple-cases-spanning-years-establish-precedent-for-digital-ownership-of-games-in-game-items-and-microtransactions)

生成摘要时出错

---

## 75. Hy3

**原文标题**: Hy3

**原文链接**: [https://hy.tencent.com/research/hy3](https://hy.tencent.com/research/hy3)

生成摘要时出错

---

## 76. SimPolitics: America’s quest to solve politics with computers

**原文标题**: SimPolitics: America’s quest to solve politics with computers

**原文链接**: [https://mitpress.mit.edu/9780262053198/simpolitics/](https://mitpress.mit.edu/9780262053198/simpolitics/)

生成摘要时出错

---

## 77. Make Europe Cool Again

**原文标题**: Make Europe Cool Again

**原文链接**: [https://jacek.migdal.pl/2026/07/07/make-europe-cool-again](https://jacek.migdal.pl/2026/07/07/make-europe-cool-again)

生成摘要时出错

---

## 78. Interview with Mitchell Hashimoto about Ghostty and Zig

**原文标题**: Interview with Mitchell Hashimoto about Ghostty and Zig

**原文链接**: [https://alexalejandre.com/programming/interview-with-mitchell-hashimoto/](https://alexalejandre.com/programming/interview-with-mitchell-hashimoto/)

生成摘要时出错

---

## 79. Show HN: SubjectiveZero, an open-source agentic node editor for creative coding

**原文标题**: Show HN: SubjectiveZero, an open-source agentic node editor for creative coding

**原文链接**: [https://sxp.studio/apps/subz](https://sxp.studio/apps/subz)

生成摘要时出错

---

## 80. Buried Apple feature turns an iPhone into the perfect kids' dumb phone

**原文标题**: Buried Apple feature turns an iPhone into the perfect kids' dumb phone

**原文链接**: [https://www.wired.com/story/this-buried-apple-feature-turns-an-iphone-into-the-perfect-kids-dumb-phone/](https://www.wired.com/story/this-buried-apple-feature-turns-an-iphone-into-the-perfect-kids-dumb-phone/)

生成摘要时出错

---

## 81. I Built the Only 2026 WWII Jeep

**原文标题**: I Built the Only 2026 WWII Jeep

**原文链接**: [https://www.theautopian.com/i-bet-my-company-on-an-impossible-jeep-build-then-a-miracle-happened/](https://www.theautopian.com/i-bet-my-company-on-an-impossible-jeep-build-then-a-miracle-happened/)

生成摘要时出错

---

## 82. Meta reuses old RAM in new servers with custom bridge chip

**原文标题**: Meta reuses old RAM in new servers with custom bridge chip

**原文链接**: [https://www.theregister.com/systems/2026/06/29/zuck-saves-meta-bucks-by-reusing-memory-from-old-servers-with-a-custom-cxl-asic/5263483](https://www.theregister.com/systems/2026/06/29/zuck-saves-meta-bucks-by-reusing-memory-from-old-servers-with-a-custom-cxl-asic/5263483)

生成摘要时出错

---

## 83. Show HN: Phobos – A tiny scale-free kernel language with tile-DAG support

**原文标题**: Show HN: Phobos – A tiny scale-free kernel language with tile-DAG support

**原文链接**: [https://www.joa-ebert.com/posts/2026-07-07-phobos-lang/](https://www.joa-ebert.com/posts/2026-07-07-phobos-lang/)

生成摘要时出错

---

## 84. What's slowing down the AI buildout

**原文标题**: What's slowing down the AI buildout

**原文链接**: [https://www.worksinprogress.news/p/ai-is-bottlenecked-by-the-grid](https://www.worksinprogress.news/p/ai-is-bottlenecked-by-the-grid)

生成摘要时出错

---

## 85. Opinionated and easy Pi.dev configuration

**原文标题**: Opinionated and easy Pi.dev configuration

**原文链接**: [https://lazypi.org/](https://lazypi.org/)

生成摘要时出错

---

## 86. The glass backbone: Why the Army's logistics will break in the next war

**原文标题**: The glass backbone: Why the Army's logistics will break in the next war

**原文链接**: [https://mwi.westpoint.edu/the-glass-backbone-why-the-armys-logistics-will-break-in-the-next-war/](https://mwi.westpoint.edu/the-glass-backbone-why-the-armys-logistics-will-break-in-the-next-war/)

生成摘要时出错

---

## 87. Prismata: Confining cross-site prompt injection in web agents

**原文标题**: Prismata: Confining cross-site prompt injection in web agents

**原文链接**: [https://arxiv.org/abs/2607.08147](https://arxiv.org/abs/2607.08147)

生成摘要时出错

---

## 88. Life with Hazard Ratios

**原文标题**: Life with Hazard Ratios

**原文链接**: [https://dynomight.net/hazard-ratios/](https://dynomight.net/hazard-ratios/)

生成摘要时出错

---

