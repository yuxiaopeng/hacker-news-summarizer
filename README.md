# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-03-09.md)

*最后自动更新时间: 2026-03-09 18:23:26*
## 1. 使用波函数折叠构建程序化六边形地图

**原文标题**: Building a Procedural Hex Map with Wave Function Collapse

**原文链接**: [https://felixturner.github.io/hex-map-wfc/article/](https://felixturner.github.io/hex-map-wfc/article/)

本文详细介绍了如何利用波函数坍缩算法（WFC）、Three.js 和 WebGPU 创建一个过程化中世纪岛屿生成器。受《龙与地下城》（D&D）随机地牢表的启发，作者构建了一个能够生成包含约 4,100 个六边形单元格的复杂、确定性地图的系统。

**关键技术洞察：**
*   **WFC 算法：** 与桌游《卡卡颂》类似，WFC 通过匹配边缘（道路、河流、草地）来放置图块。由于六边形图块具有六个边缘和五个海拔等级，每个单元格会产生 900 种可能的状态，这显著增加了复杂性。
*   **缩放与恢复：** 为防止网格因陷入“死胡同”而无法求解，地图被拆分为 19 个模块化网格。一套三层恢复系统用于处理失败情况：解除邻近约束、运行“局部 WFC”重新求解小型问题区域，以及利用山脉图块掩盖剩余接缝。
*   **WFC 与噪声：** 虽然 WFC 擅长局部边缘匹配，但在生成大规模模式时效果不佳。因此，作者使用柏林噪声（Perlin noise）来处理森林和村庄的自然聚类，而让 WFC 专注于地形的连通性。
*   **视觉与性能：** 该项目采用了 Three.js 全新的 TSL（Three.js 着色语言）编写自定义 WebGPU 着色器。高级水体效果（包括动画焦散和适配海岸线的海浪）通过“环绕度”探测器实现，解决了海湾处的视觉拉伸问题。
*   **优化：** 通过使用 BatchedMesh 减少绘制调用，并为所有资产使用基于共享调色板的材质，系统得以维持 60fps 的高性能。

最终系统在大约 20 秒内即可生成一张完整且精美的地图，成功率达 100%，将数学约束与环境光遮蔽、移轴景深等艺术化后期处理完美结合。

---

## 2. Fixfest 是一场维修人员、修补爱好者和行动主义者的全球盛会。

**原文标题**: Fixfest is a global gathering of repairers, tinkerers, and activists

**原文链接**: [https://fixfest.therestartproject.org/](https://fixfest.therestartproject.org/)

**总结：Fixfest 修复节**

Fixfest 是由 The Restart Project 组织的一场全球盛会，汇聚了维修人员、活动人士、设计师和政策制定者等多元群体。该活动是国际维修运动的核心枢纽，致力于促进可持续的循环经济，并应对日益严重的电子垃圾危机。

该盛会面向广泛的参与者，包括运营本地“维修咖啡馆”（Repair Cafés）和“重启派对”（Restart Parties）的志愿者“修理工”，以及学者和专业维修人员。其核心目标是分享技术技能，弘扬维修文化，并建立一个更强大的倡导者网络，共同推动开发更耐用、更易维修的产品。

Fixfest 的一个主要重点是政策和倡导，特别是“维修权”（Right to Repair）运动。与会者讨论了影响立法的策略，旨在要求制造商提供更便捷的零配件、维修手册和诊断工具。通过应对“计划性报废”造成的障碍，该活动力求降低维修成本，提高公众进行维修的便利性。

最近一次重大的 Fixfest 2024 在比利时布鲁塞尔举行。这一地点的选择具有战略意义，旨在环境和消费者权利立法的关键时期直接与欧洲政策制定者进行交流。归根结底，Fixfest 不仅仅是一个技术研讨会，更是一个协作平台，旨在将全球与技术的关系从“即弃式消费”模式转变为“维护与长久使用”的模式。

---

## 3. Sun SPARCstation IPX 修复（一）：电源与 NVRAM

**原文标题**: Restoring a Sun SPARCstation IPX Part 1: PSU and Nvram

**原文链接**: [https://www.rs-online.com/designspark/restoring-a-sun-sparcstation-ipx-part-1-psu-and-nvram](https://www.rs-online.com/designspark/restoring-a-sun-sparcstation-ipx-part-1-psu-and-nvram)

在本文中，Andrew Back 详细介绍了对一台 1991 年产 Sun SPARCstation IPX 的初步修复过程，这是一款紧凑型“午餐盒”式 UNIX 工作站。该项目重点解决了老式 Sun 系统中常见的两个主要硬件故障：电源单元 (PSU) 和 NVRAM。

**电源修复**
IPX 因电解电容失效而臭名昭著，这些电容会发生漏液并导致电路板腐蚀。在尝试修复一台腐蚀严重的电源失败后，作者使用尼吉康 (Nichicon)、松下 (Panasonic) 和伍尔特 (Wurth Elektronik) 的多种电容，成功为第二台电源更换了电容。这成功恢复了工作站的供电。

**NVRAM 更换与编程**
Sun 工作站使用一种“TIMEKEEPER”芯片，该芯片集成了 SRAM、实时时钟和内置电池。当电池耗尽时，系统会丢失其配置、MAC 地址和唯一的“主机 ID (hostid)”。作者用 M48T02（后来还测试了 M48T12）更换了失效的芯片。通过使用 OpenBoot PROM (OBP) Forth 解释器，他手动重新编写了 IDPROM 数据，以恢复机器的身份信息。尽管更换了新芯片，但“更换 NVRAM (replace NVRAM)”的错误提示依然存在，这需要用户手动启动引导程序，但并不影响系统运行。

**当前状态与后续计划**
该工作站已成功从其内部 SCSI 驱动器引导至 Solaris 7 (SunOS 5.7)。作者在最后概述了未来的计划，包括对发黄的塑料外壳进行“去黄处理 (retrobrighting)”，调查持续存在的 NVRAM 错误，并将操作系统降级到更符合时代的 Solaris 1.x 版本，以更好地匹配该硬件 1991 年的原始风貌。

---

## 4. 佛罗里达州法官裁定闯红灯监控罚单违宪

**原文标题**: Florida Judge Rules Red Light Camera Tickets Are Unconstitutional

**原文链接**: [https://cbs12.com/news/local/florida-news-judge-rules-red-light-camera-tickets-unconstitutional](https://cbs12.com/news/local/florida-news-judge-rules-red-light-camera-tickets-unconstitutional)

2026年3月3日，布劳沃德县法官史蒂文·P·德卢卡（Steven P. DeLuca）做出了一项重大裁决，驳回了一张闯红灯自动执法罚单，并宣布佛罗里达州的自动执法法律违宪。该裁决挑战了《马克·旺德尔交通安全法》（佛罗里达州法规 316.0083）的框架。

法院长达21页的裁决书认定，该法规通过不当地转移举证责任，违反了宪法规定的正当程序。根据佛罗里达州现行法律，除非登记车主提供宣誓书指认另一名驾驶员，否则其将被推定为摄像记录违规行为的责任人。德卢卡法官裁定，由于此类传票属于“准刑事”诉讼——涉及罚金并影响驾驶记录——州政府必须“排除合理怀疑”地证明违规行为的所有要素。这包括证明谁是当时的实际驾驶人，而不是强迫车主证明自己无罪。

**核心影响：**
*   **举证责任：** 裁决强化了在交通案件中必须由政府而非公民提供有罪证据的原则。
*   **适用范围：** 虽然该裁决目前仅适用于布劳沃德县的这一特定案件，但法律专家表示，它可能会引发佛罗里达州全境的类似挑战。
*   **全州影响：** 如果该案提起上诉并获得地区上诉法院维持原判，该裁决可能在全州范围内产生约束力，从而可能导致全州闯红灯摄像执法系统的瓦解。

维权团体称赞该裁决是正当程序的重大胜利，而摄像头的支持者则坚持认为这些系统对路口安全至关重要。该裁决已促使棕榈滩县等邻近地区的驾驶员呼吁地方官员重新评估或拆除自动执法系统。

---

## 5. 闪存介质寿命测试——六年后

**原文标题**: Flash media longevity testing – 6 years later

**原文链接**: [https://old.reddit.com/r/DataHoarder/comments/1q6xnun/flash_media_longevity_testing_6_years_later/](https://old.reddit.com/r/DataHoarder/comments/1q6xnun/flash_media_longevity_testing_6_years_later/)

这篇 Reddit 帖子更新了一项长期实验的结果，该实验测试了断电状态下的闪存介质（USB 闪存盘、SD 卡和 SSD）在六年时间里的数据保存能力。

实验始于作者将各种闪存设备写入数据并记录 MD5 校验和后，将其存放在抽屉中。其实验目的是为了验证业界常见的警告，即闪存不适合“冷存储”，因为它需要定期通电以维持 NAND 存储单元中的电荷。

**关键发现：**
*   **高可靠性：** 尽管断电长达六年，几乎所有设备（包括廉价的 USB 盘和旧 SD 卡）都通过了验证测试，未出现任何数据损坏。
*   **SSD 性能：** SSD 也完美地保留了数据，其表现超出了作者基于 JEDEC 标准的最初预期（该标准建议数据可能会在一年内丢失，具体取决于存储温度）。
*   **环境因素：** 作者指出这些设备存放在稳定且有空调调节的环境中。他强调，热量是闪存寿命的主要敌人，高温会显著加速电荷流失。

**结论：**
虽然实验结果非常乐观，但作者提醒这只是一个小样本测试。该实验表明，对于普通用户而言，闪存介质在多年冷存储方面的韧性比理论模型预测的要强。然而，对于关键的长期归档，仍然建议遵循“3-2-1 备份原则”，而不是依赖单一的闪存设备。

---

## 6. Fontcrafter：将你的手写体转化为真实的字体

**原文标题**: Fontcrafter: Turn Your Handwriting into a Real Font

**原文链接**: [https://arcade.pirillo.com/fontcrafter.html](https://arcade.pirillo.com/fontcrafter.html)

**FontCrafter** is a free, browser-based application created by Chris Pirillo that allows users to transform their handwriting into professional, installable font files. Distinguishing itself from competitors, FontCrafter requires no account registration and processes all data locally within the user's browser. This ensures complete privacy, as handwriting scans are never uploaded to a server or stored remotely.

The workflow is designed for simplicity:
1.  **Template:** Users download and print a provided template (A4 or US Letter).
2.  **Creation:** Users fill the boxes with a felt-tip pen. The template includes three rows for each character to capture natural handwriting variations.
3.  **Digitization:** Users upload a scan or photo of the sheet. The app uses JavaScript to detect characters and trace vector outlines.
4.  **Customization:** Users can name their font, adjust character spacing (kerning), set descender depths, and enable advanced OpenType features.

A key highlight of the tool is its support for sophisticated typography features at no cost. It can auto-generate **ligatures** (connected letter pairs like "ff" and "th") and **contextual alternates**, which cycle through the three different handwritten versions of a letter to prevent the font from looking "robotic." It also supports over 100 extended characters, including currency symbols and European diacritics.

FontCrafter exports to four major formats: **OTF** (desktop apps), **TTF** (universal), **WOFF2** (web-optimized), and **Base64** (CSS embedding). Users retain full ownership of their generated fonts for both personal and commercial use. The project is supported by optional donations, keeping all premium features free and accessible.

---

## 7. The 1979 Design Choice Breaking AI Workloads

**原文标题**: The 1979 Design Choice Breaking AI Workloads

**原文链接**: [https://www.cerebrium.ai/blog/rethinking-container-image-distribution-to-eliminate-cold-starts](https://www.cerebrium.ai/blog/rethinking-container-image-distribution-to-eliminate-cold-starts)

生成摘要时出错

---

## 8. Show HN: DenchClaw – Local CRM on Top of OpenClaw

**原文标题**: Show HN: DenchClaw – Local CRM on Top of OpenClaw

**原文链接**: [https://github.com/DenchHQ/DenchClaw](https://github.com/DenchHQ/DenchClaw)

生成摘要时出错

---

## 9. Jolla on track to ship new phone with Sailfish OS, user-replaceable battery

**原文标题**: Jolla on track to ship new phone with Sailfish OS, user-replaceable battery

**原文链接**: [https://liliputing.com/the-new-jolla-phone-with-sailfish-os-is-on-track-to-start-shipping-in-the-first-half-of-2026/](https://liliputing.com/the-new-jolla-phone-with-sailfish-os-is-on-track-to-start-shipping-in-the-first-half-of-2026/)

生成摘要时出错

---

## 10. Reverse-engineering the UniFi inform protocol

**原文标题**: Reverse-engineering the UniFi inform protocol

**原文链接**: [https://tamarack.cloud/blog/reverse-engineering-unifi-inform-protocol](https://tamarack.cloud/blog/reverse-engineering-unifi-inform-protocol)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 2 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 3 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 4 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 5 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 6 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 7 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 8 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 9 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 10 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 11 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 12 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 13 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 14 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 15 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 16 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 17 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 18 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 19 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 20 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 21 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 22 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 23 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 24 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 25 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 26 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 27 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 28 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 29 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 30 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 31 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 32 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 33 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 34 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 35 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 36 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 37 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 38 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 39 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 40 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 41 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 42 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 43 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 44 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 45 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 46 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 47 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 48 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 49 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 50 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 51 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 52 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 53 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 54 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 55 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 56 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 57 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 58 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 59 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 60 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 61 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 62 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 63 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 64 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 65 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 66 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 67 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 68 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 69 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 70 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 71 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 72 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 73 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 74 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 75 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 76 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 77 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 78 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 79 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 80 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 81 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 82 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 83 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 84 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 85 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 86 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 87 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 88 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 89 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 90 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 91 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 92 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 93 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 94 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 95 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 96 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 97 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 98 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 99 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 100 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 101 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 102 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 103 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 104 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 105 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 106 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 107 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 108 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 109 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 110 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 111 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 112 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 113 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 114 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 115 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 116 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 117 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 118 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 119 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 120 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 121 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 122 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 123 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 124 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 125 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 126 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 127 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 128 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 129 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 130 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 131 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 132 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 133 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 134 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 135 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 136 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 137 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 138 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 139 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 140 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 141 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 142 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 143 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 144 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 145 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 146 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 147 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 148 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 149 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 150 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 151 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 152 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 153 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 154 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 155 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 156 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 157 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 158 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 159 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 160 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 161 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 162 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 163 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 164 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 165 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 166 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 167 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 168 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 169 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 170 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 171 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 172 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 173 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 174 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 175 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 176 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 177 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 178 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 179 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 180 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 181 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 182 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 183 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 184 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 185 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 186 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 187 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 188 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 189 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 190 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 191 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 192 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 193 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 194 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 195 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 196 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 197 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 198 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 199 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 200 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 201 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 202 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 203 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 204 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 205 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 206 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 207 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 208 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 209 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 210 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 211 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 212 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 213 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 214 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 215 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 216 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 217 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 218 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 219 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 220 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 221 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 222 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 223 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 224 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 225 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 226 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 227 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 228 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 229 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 230 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 231 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 232 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 233 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 234 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 235 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 236 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 237 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 238 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 239 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 240 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 241 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 242 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 243 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 244 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 245 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 246 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 247 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 248 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 249 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 250 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 251 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 252 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 253 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 254 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 255 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 256 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 257 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 258 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 259 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 260 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 261 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 262 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 263 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 264 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 265 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 266 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 267 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 268 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 269 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 270 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 271 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 272 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 273 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 274 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 275 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 276 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 277 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 278 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 279 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 280 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 281 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 282 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 283 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 284 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 285 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 286 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 287 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 288 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 289 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 290 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 291 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 292 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 293 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 294 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 295 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 296 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 297 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 298 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 299 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 300 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 301 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 302 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 303 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 304 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 305 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 306 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 307 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 308 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 309 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 310 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 311 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 312 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 313 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 314 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 315 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 316 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 317 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 318 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 319 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 320 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 321 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 322 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 323 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 324 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 325 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 326 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 327 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 328 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 329 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 330 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 331 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 332 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 333 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 334 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 335 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 336 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 337 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 338 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 339 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 340 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 341 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 342 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 343 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 344 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 345 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 346 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 347 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 348 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 349 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 350 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 351 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 352 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 353 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 354 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
