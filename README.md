# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-06-21.md)

*最后自动更新时间: 2026-06-21 18:43:08*
## 1. 15分钟居家莱姆病蜱虫检测

**原文标题**: 15-minute at-home Lyme disease tick test

**原文链接**: [https://www.bostonglobe.com/2026/06/17/business/lyme-disease-tick-test/](https://www.bostonglobe.com/2026/06/17/business/lyme-disease-tick-test/)

**LymeAlert** 是一款新型的 15 分钟居家诊断工具，旨在检测蜱虫是否携带莱姆病细菌。该工具由儿科骨科助理医师、麻省理工学院毕业生 Erin Dawicki 开发，为传统的实验室检测提供了一种更快速、更实惠的选择。传统实验室检测费用最高可达 450 美元，且处理时间通常需要一周以上。

该测试售价为 40 美元，操作时用户需将最多五只蜱虫放入一个内置研磨器的专用容器中。在蜱虫被研磨成浆状后，插入一条经过化学处理的试纸，若检测到莱姆病细菌，试纸便会变色。Dawicki 的目标是减少不必要的就医和抗生素的过度处方，同时确保被受感染蜱虫叮咬的人群能在关键的 72 小时黄金窗口期内获得治疗。

尽管医学专家承认快速测试的潜在益处，但也有人提醒，假阳性结果可能会引起不必要的恐慌。此外，目前的版本仅能检测莱姆病，无法检测引起 α-半乳糖综合征（Alpha-gal syndrome）等其他蜱传病原体。Dawicki 计划在未来开发能够检测多种感染的升级版本。

除了实体测试工具，该公司还将推出一款智能手机应用程序，允许用户匿名报告受感染蜱虫的发现位置。这些数据将结合美国国家航空航天局（NASA）的卫星图像和人工智能算法，绘制社区级别的蜱传疾病传播预测图。LymeAlert 预计将于今年 8 月正式上市。

---

## 2. 谁拥有你的 ATProto 身份？

**原文标题**: Who owns your ATProto identity?

**原文链接**: [https://kevinak.se/blog/who-actually-owns-your-atproto-identity-hint-its-probably-not-you](https://kevinak.se/blog/who-actually-owns-your-atproto-identity-hint-its-probably-not-you)

本文探讨了 AT Protocol (ATProto) 生态系统中的一个关键安全漏洞：密钥管理的中心化。虽然 ATProto 的设计初衷是去中心化，但作者认为目前的实现方式（如 Bluesky 所使用的）要求用户对个人数据服务器 (PDS) 运营商寄予极高的信任。

核心问题在于 PDS 同时持有用户的**签名密钥**和**轮换密钥**。这赋予了运营商以下权力：

*   **冒充用户**：PDS 可以发布帖文、点赞并提交 commit，而这些操作在加密层面与用户本人的活动无法区分。 
*   **武器化跨应用身份**：由于 ATProto 为多个应用（如社交类的 Bluesky、Git 类的 Tangled、写作类的 Leaflet）提供统一身份，一旦 PDS 遭到攻击，攻击者就可以在用户的整个数字生态系统中冒充该用户。
*   **撤销身份**：运营商可以使用轮换密钥更改用户的去中心化标识符 (DID)，从而有效地将用户拒之门外，并剥夺其与网络中任何应用交互的能力。

作者指出，虽然“自主控制的轮换密钥”可以防止运营商封锁用户，但该功能目前隐藏在 API 中，并非标准注册流程的一部分。为了解决这一问题，作者建议将备份轮换密钥的注册设为账号创建过程中面向用户的默认环节。

最后，文章警告称，ATProto 目前以真正的自主权换取了用户的便利。通过将“核心权力”交给 PDS 运营商，用户面临着从内鬼员工到国家行为体等各种风险，这与该协议的去中心化承诺相违背。

---

## 3. 谷歌 IPv6 采用率达 50%

**原文标题**: Google Hits 50% IPv6

**原文链接**: [https://blog.apnic.net/2026/04/28/google-hits-50-ipv6/](https://blog.apnic.net/2026/04/28/google-hits-50-ipv6/)

本文探讨了谷歌 IPv6 采用率达到 50% 这一里程碑，指出虽然这并未改变技术功能，但它提供了一个强有力的倡导工具，鼓励互联网服务提供商（ISP）和相关组织认真对待这一转型。

尽管取得了进展，作者仍指出了目前阻碍全面部署的几个关键障碍：

*   **可见性与工具：** 搜索引擎和浏览器通常无法让使用 IPv4 连接的用户找到仅支持 IPv6 的网站，而测速和在线率检查器等性能工具也经常误报或忽略 IPv6 数据。
*   **技术限制：** 目前 Linux 内核的局限性导致在不包含 IPv4 组件的情况下无法编译 IPv6。
*   **行业惯性：** 许多 ISP 仍缺乏明确的部署时间表，且主要平台（最典型的是 GitHub）尚未采用 IPv6。
*   **教育：** IT 相关课程通常未能对 IPv6 进行全面覆盖。

作者总结道，解决这些具体障碍对于加速全球向 IPv6 的转型至关重要。

---

## 4. 巴西全国手机收到未经授权警报

**原文标题**: Unauthorized alert sent to cell phones across Brazil

**原文链接**: [https://www.cnn.com/2026/06/20/americas/brazil-hackers-unauthorized-alert-latam](https://www.cnn.com/2026/06/20/americas/brazil-hackers-unauthorized-alert-latam)

周六上午，包括圣保罗和里约热内卢等中心城市在内的巴西多个州的手机用户收到了一条未经授权的“极端警报”，疑为黑客所为。

信息内容为“misantropi4”，是葡萄牙语中“厌世”（misanthropy）一词的数字字母混写（leetspeak）版本。这些警报是通过国家民防部的应急预警平台（类似于美国安珀警报、可直接广播至移动设备的系统）以及短信发送的。

**此次事件的关键细节包括：**
*   **地理范围：** 警报最初出现在南部的巴拉那州，随后蔓延至人口稠密的圣保罗和里约热内卢。
*   **政府回应：** 巴西国家民防部证实，该系统被未经授权的人员远程触发。作为应对，预警平台已暂时下线，当局正在努力重建安全协议。
*   **并无实际威胁：** 受影响各州的民防机构确认，并未发生任何实际的紧急情况、自然灾害或需要发布极端警报的事件。
*   **调查情况：** 巴西国家电信管理局（Anatel）及其他联邦机构正在调查入侵来源以及小区广播（Cellbroadcast）工具的不稳定性。

政府目前正致力于在确保安全的前提下恢复该工具。目前尚无任何组织声称对此次入侵负责。

---

## 5. DOS 游戏《F-15 攻击鹰 II》逆向项目招募 DOS 测试飞行员

**原文标题**: DOS Game "F-15 Strike Eagle II" reversing project needs DOS test pilots

**原文链接**: [https://neuviemeporte.github.io/f15-se2/2026/06/20/needyou.html](https://neuviemeporte.github.io/f15-se2/2026/06/20/needyou.html)

针对1989年DOS游戏《F-15鹰式攻击机II》（F-15 Strike Eagle II）的C语言源码重构逆向工程项目已迎来重大里程碑。经过一段时间的飞速进展，团队已成功重构了所有可执行文件的C代码，完成了汇编数据的迁移，并为绝大多数例程创建了功能性的C语言替代方案。

随着项目重点从匹配汇编操作码转向维持游戏的可玩性，开发者现正招募“测试飞行员”来查找Bug，尤其是那些与数据布局相关的错误。当前发布的版本（v0.9.1）兼容游戏451.03版（包含“沙漠风暴”资料片）。测试者可以通过将原版可执行文件替换为新版本来参与测试。虽然当前构建版本默认采用VGA/MCGA显示，且暂不支持声音和摇杆，但完整的游戏循环——任务简报、飞行及任务总结——现已可以正常运行。

该项目目前的目标是实现“Bug级还原”（bug-for-bug reconstruction），这意味着测试者应仅报告原版游戏中不存在的新问题，如程序崩溃、图形花屏或输入失效。报告应包含对触发问题前操作的描述，并尽可能附带截图。这一里程碑标志着该项目开始向未来多平台移植阶段转型。

---

## 6. UHF X11：专为 visionOS 和 Apple Vision Pro 打造的 X11

**原文标题**: UHF X11: X11 Built for VisionOS and Apple Vision Pro

**原文链接**: [https://www.lispm.net/apps/uhf-x11/](https://www.lispm.net/apps/uhf-x11/)

**UHF X11** 是一款专门为 **visionOS** 和 **Apple Vision Pro** 设计的 X11 窗口系统实现。

该软件的核心功能是**无根空间窗口** (Rootless Spatial Windows)，它使单个 X11 应用程序能够像 visionOS 原生应用一样运行。每个顶级 X11 窗口都会作为一个独立的窗口打开，而不是被限制在单一的虚拟桌面中，用户可以在其 3D 空间环境内的任何位置自由地放置和排列这些窗口。

---

## 7. SMPTE 免费开放其标准

**原文标题**: SMPTE Makes Its Standards Freely Accessible

**原文链接**: [https://www.smpte.org/blog/smpte-makes-its-standards-freely-accessible-openingstandards-library-to-the-global-media-technology-community](https://www.smpte.org/blog/smpte-makes-its-standards-freely-accessible-openingstandards-library-to-the-global-media-technology-community)

**SMPTE 标准开放获取公告摘要**

2026年6月17日，电影与电视工程师协会（SMPTE）宣布了一项具有里程碑意义的举措：将其全面的技术标准库向全球媒体技术社区免费开放。该协会总部位于纽约州怀特普莱恩斯，是全球领先的媒体专业人士、技术专家和工程师组织。

该举措的主要目标是推动全行业的标准采用、简化实施流程，并提高媒体与娱乐领域的互操作性。通过提供标准的开放获取，SMPTE 旨在为创作者和工程师消除障碍，确保所有人都能获得基础性技术框架，例如用于 IP 现场制作的 ST 2110 系列标准和媒体微服务术语。

除了标准制定工作外，该公告还强调了 SMPTE 通过以下方式推进媒体技术的广泛使命：
*   **教育：** 通过 SMPTE 学院提供专业培训，包括“ST 2110 训练营”和色彩管理工作流课程。
*   **出版物：** 通过《电影成像期刊》（*Motion Imaging Journal*）提供行业见解和经过同行评审的研究。
*   **社区：** 通过个人和企业会员、全球活动以及媒体技术峰会支持专业成长。

这一向开放获取的转型标志着该组织支持行业方式的重大转变，旨在迈向一种更具包容性的模式，从而促进全球范围内的创新和卓越技术。

---

## 8. Building reliable agentic AI systems

**原文标题**: Building reliable agentic AI systems

**原文链接**: [https://martinfowler.com/articles/reliable-llm-bayer.html](https://martinfowler.com/articles/reliable-llm-bayer.html)

生成摘要时出错

---

## 9. Whole cross-sectional human ultrasound tomography

**原文标题**: Whole cross-sectional human ultrasound tomography

**原文链接**: [https://www.nature.com/articles/s41551-026-01660-4](https://www.nature.com/articles/s41551-026-01660-4)

生成摘要时出错

---

## 10. 罕见中世纪书签拍卖成交价超出预期

**原文标题**: Rare medieval bookmark exceeds expectations at auction

**原文链接**: [https://www.thehistoryblog.com/archives/76314](https://www.thehistoryblog.com/archives/76314)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 2 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 3 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 4 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 5 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 6 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 7 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 8 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 9 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 10 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 11 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 12 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 13 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 14 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 15 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 16 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 17 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 18 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 19 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 20 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 21 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 22 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 23 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 24 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 25 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 26 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 27 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 28 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 29 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 30 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 31 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 32 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 33 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 34 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 35 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 36 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 37 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 38 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 39 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 40 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 41 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 42 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 43 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 44 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 45 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 46 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 47 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 48 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 49 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 50 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 51 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 52 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 53 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 54 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 55 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 56 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 57 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 58 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 59 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 60 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 61 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 62 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 63 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 64 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 65 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 66 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 67 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 68 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 69 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 70 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 71 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 72 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 73 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 74 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 75 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 76 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 77 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 78 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 79 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 80 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 81 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 82 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 83 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 84 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 85 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 86 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 87 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 88 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 89 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 90 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 91 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 92 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 93 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 94 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 95 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 96 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 97 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 98 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 99 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 100 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 101 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 102 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 103 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 104 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 105 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 106 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 107 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 108 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 109 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 110 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 111 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 112 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 113 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 114 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 115 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 116 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 117 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 118 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 119 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 120 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 121 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 122 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 123 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 124 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 125 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 126 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 127 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 128 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 129 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 130 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 131 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 132 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 133 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 134 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 135 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 136 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 137 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 138 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 139 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 140 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 141 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 142 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 143 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 144 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 145 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 146 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 147 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 148 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 149 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 150 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 151 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 152 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 153 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 154 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 155 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 156 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 157 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 158 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 159 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 160 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 161 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 162 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 163 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 164 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 165 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 166 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 167 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 168 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 169 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 170 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 171 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 172 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 173 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 174 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 175 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 176 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 177 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 178 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 179 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 180 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 181 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 182 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 183 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 184 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 185 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 186 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 187 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 188 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 189 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 190 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 191 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 192 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 193 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 194 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 195 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 196 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 197 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 198 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 199 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 200 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 201 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 202 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 203 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 204 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 205 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 206 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 207 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 208 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 209 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 210 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 211 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 212 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 213 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 214 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 215 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 216 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 217 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 218 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 219 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 220 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 221 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 222 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 223 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 224 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 225 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 226 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 227 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 228 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 229 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 230 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 231 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 232 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 233 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 234 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 235 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 236 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 237 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 238 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 239 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 240 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 241 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 242 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 243 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 244 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 245 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 246 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 247 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 248 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 249 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 250 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 251 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 252 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 253 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 254 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 255 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 256 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 257 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 258 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 259 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 260 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 261 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 262 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 263 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 264 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 265 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 266 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 267 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 268 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 269 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 270 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 271 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 272 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 273 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 274 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 275 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 276 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 277 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 278 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 279 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 280 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 281 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 282 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 283 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 284 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 285 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 286 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 287 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 288 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 289 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 290 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 291 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 292 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 293 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 294 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 295 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 296 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 297 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 298 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 299 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 300 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 301 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 302 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 303 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 304 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 305 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 306 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 307 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 308 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 309 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 310 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 311 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 312 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 313 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 314 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 315 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 316 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 317 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 318 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 319 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 320 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 321 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 322 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 323 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 324 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 325 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 326 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 327 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 328 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 329 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 330 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 331 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 332 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 333 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 334 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 335 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 336 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 337 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 338 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 339 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 340 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 341 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 342 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 343 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 344 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 345 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 346 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 347 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 348 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 349 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 350 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 351 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 352 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 353 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 354 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 355 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 356 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 357 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 358 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 359 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 360 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 361 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 362 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 363 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 364 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 365 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 366 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 367 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 368 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 369 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 370 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 371 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 372 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 373 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 374 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 375 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 376 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 377 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 378 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 379 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 380 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 381 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 382 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 383 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 384 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 385 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 386 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 387 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 388 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 389 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 390 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 391 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 392 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 393 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 394 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 395 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 396 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 397 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 398 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 399 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 400 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 401 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 402 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 403 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 404 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 405 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 406 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 407 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 408 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 409 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 410 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 411 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 412 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 413 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 414 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 415 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 416 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 417 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 418 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 419 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 420 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 421 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 422 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 423 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 424 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 425 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 426 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 427 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 428 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 429 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 430 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 431 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 432 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 433 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 434 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 435 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 436 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 437 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 438 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 439 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 440 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 441 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 442 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 443 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 444 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 445 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 446 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 447 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 448 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 449 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 450 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 451 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 452 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 453 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 454 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 455 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 456 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 457 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 458 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
