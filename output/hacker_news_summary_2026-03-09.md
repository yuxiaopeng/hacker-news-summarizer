# Hacker News 热门文章摘要 (2026-03-09)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Ireland shuts last coal plant, becomes 15th coal-free country in Europe (2025)

**原文标题**: Ireland shuts last coal plant, becomes 15th coal-free country in Europe (2025)

**原文链接**: [https://www.pv-magazine.com/2025/06/20/ireland-coal-free-ends-coal-power-generation-moneypoint/](https://www.pv-magazine.com/2025/06/20/ireland-coal-free-ends-coal-power-generation-moneypoint/)

生成摘要时出错

---

## 12. FreeBSD Capsicum vs. Linux Seccomp Process Sandboxing

**原文标题**: FreeBSD Capsicum vs. Linux Seccomp Process Sandboxing

**原文链接**: [https://vivianvoss.net/blog/capsicum-vs-seccomp](https://vivianvoss.net/blog/capsicum-vs-seccomp)

生成摘要时出错

---

## 13. DARPA's new X-76 Experimental Plane

**原文标题**: DARPA's new X-76 Experimental Plane

**原文链接**: [https://www.darpa.mil/news/2026/darpa-new-x-76-speed-of-jet-freedom-of-helicopter](https://www.darpa.mil/news/2026/darpa-new-x-76-speed-of-jet-freedom-of-helicopter)

生成摘要时出错

---

## 14. What I Always Wanted to Know about Second Class Values

**原文标题**: What I Always Wanted to Know about Second Class Values

**原文链接**: [https://dl.acm.org/doi/epdf/10.1145/3759427.3760373](https://dl.acm.org/doi/epdf/10.1145/3759427.3760373)

生成摘要时出错

---

## 15. US Court of Appeals: TOS may be updated by email, use can imply consent [pdf]

**原文标题**: US Court of Appeals: TOS may be updated by email, use can imply consent [pdf]

**原文链接**: [https://cdn.ca9.uscourts.gov/datastore/memoranda/2026/03/03/25-403.pdf](https://cdn.ca9.uscourts.gov/datastore/memoranda/2026/03/03/25-403.pdf)

生成摘要时出错

---

## 16. Algebraic topology: knots links and braids

**原文标题**: Algebraic topology: knots links and braids

**原文链接**: [https://aeb.win.tue.nl/at/algtop-5.html](https://aeb.win.tue.nl/at/algtop-5.html)

生成摘要时出错

---

## 17. The Window Chrome of Our Discontent

**原文标题**: The Window Chrome of Our Discontent

**原文链接**: [https://pxlnv.com/blog/window-chrome-of-our-discontent/](https://pxlnv.com/blog/window-chrome-of-our-discontent/)

生成摘要时出错

---

## 18. Show HN: VS Code Agent Kanban: Task Management for the AI-Assisted Developer

**原文标题**: Show HN: VS Code Agent Kanban: Task Management for the AI-Assisted Developer

**原文链接**: [https://www.appsoftware.com/blog/introducing-vs-code-agent-kanban-task-management-for-the-ai-assisted-developer](https://www.appsoftware.com/blog/introducing-vs-code-agent-kanban-task-management-for-the-ai-assisted-developer)

生成摘要时出错

---

## 19. JSLinux Now Supports x86_64

**原文标题**: JSLinux Now Supports x86_64

**原文链接**: [https://bellard.org/jslinux/](https://bellard.org/jslinux/)

生成摘要时出错

---

## 20. The optimal age to freeze eggs is 19

**原文标题**: The optimal age to freeze eggs is 19

**原文链接**: [https://www.lesswrong.com/posts/dxffBxGqt2eidxwRR/the-optimal-age-to-freeze-eggs-is-19](https://www.lesswrong.com/posts/dxffBxGqt2eidxwRR/the-optimal-age-to-freeze-eggs-is-19)

生成摘要时出错

---

## 21. Agent Safehouse – macOS-native sandboxing for local agents

**原文标题**: Agent Safehouse – macOS-native sandboxing for local agents

**原文链接**: [https://agent-safehouse.dev/](https://agent-safehouse.dev/)

生成摘要时出错

---

## 22. Show HN: I gave my robot physical memory – it stopped repeating mistakes

**原文标题**: Show HN: I gave my robot physical memory – it stopped repeating mistakes

**原文链接**: [https://github.com/robotmem/robotmem](https://github.com/robotmem/robotmem)

生成摘要时出错

---

## 23. Kuwaiti F/A-18's Triple Friendly Fire Shootdown Gets Stranger by the Day

**原文标题**: Kuwaiti F/A-18's Triple Friendly Fire Shootdown Gets Stranger by the Day

**原文链接**: [https://www.twz.com/air/kuwaiti-f-a-18s-triple-friendly-fire-shootdown-gets-stranger-by-the-day](https://www.twz.com/air/kuwaiti-f-a-18s-triple-friendly-fire-shootdown-gets-stranger-by-the-day)

生成摘要时出错

---

## 24. No leap second will be introduced at the end of June 2026

**原文标题**: No leap second will be introduced at the end of June 2026

**原文链接**: [https://lists.iana.org/hyperkitty/list/tz@iana.org/thread/P6D36VZSZBUSSTSMZKFXKF4T4IXWN23P/](https://lists.iana.org/hyperkitty/list/tz@iana.org/thread/P6D36VZSZBUSSTSMZKFXKF4T4IXWN23P/)

生成摘要时出错

---

## 25. FFmpeg at Meta: Media Processing at Scale

**原文标题**: FFmpeg at Meta: Media Processing at Scale

**原文链接**: [https://engineering.fb.com/2026/03/02/video-engineering/ffmpeg-at-meta-media-processing-at-scale/](https://engineering.fb.com/2026/03/02/video-engineering/ffmpeg-at-meta-media-processing-at-scale/)

生成摘要时出错

---

## 26. Is legal the same as legitimate: AI reimplementation and the erosion of copyleft

**原文标题**: Is legal the same as legitimate: AI reimplementation and the erosion of copyleft

**原文链接**: [https://writings.hongminhee.org/2026/03/legal-vs-legitimate/](https://writings.hongminhee.org/2026/03/legal-vs-legitimate/)

生成摘要时出错

---

## 27. Microscopes can see video on a laserdisc

**原文标题**: Microscopes can see video on a laserdisc

**原文链接**: [https://www.youtube.com/watch?v=qZuR-772cks](https://www.youtube.com/watch?v=qZuR-772cks)

生成摘要时出错

---

## 28. Lazy JWT Key Rotation in .NET: Redis-Powered JWKS That Just Works

**原文标题**: Lazy JWT Key Rotation in .NET: Redis-Powered JWKS That Just Works

**原文链接**: [https://www.aaronpina.com/lazy-jwt-key-rotation-in-net-redis-powered-jwks-that-just-works/](https://www.aaronpina.com/lazy-jwt-key-rotation-in-net-redis-powered-jwks-that-just-works/)

生成摘要时出错

---

## 29. Segagaga Has Been Translated into English

**原文标题**: Segagaga Has Been Translated into English

**原文链接**: [https://www.thedreamcastjunkyard.co.uk/2026/02/segagaga-has-finally-been-translated.html](https://www.thedreamcastjunkyard.co.uk/2026/02/segagaga-has-finally-been-translated.html)

生成摘要时出错

---

## 30. Revealed: UK's multibillion AI drive is built on 'phantom investments'

**原文标题**: Revealed: UK's multibillion AI drive is built on 'phantom investments'

**原文链接**: [https://www.theguardian.com/technology/2026/mar/09/revealed-uks-multibillion-ai-drive-is-built-on-phantom-investments](https://www.theguardian.com/technology/2026/mar/09/revealed-uks-multibillion-ai-drive-is-built-on-phantom-investments)

生成摘要时出错

---

## 31. Grammarly is offering ‘expert’ AI reviews from famous dead and living writers

**原文标题**: Grammarly is offering ‘expert’ AI reviews from famous dead and living writers

**原文链接**: [https://www.wired.com/story/grammarly-is-offering-expert-ai-reviews-from-your-favorite-authors-dead-or-alive/](https://www.wired.com/story/grammarly-is-offering-expert-ai-reviews-from-your-favorite-authors-dead-or-alive/)

生成摘要时出错

---

## 32. Show HN: Zenòdot – Find if a book has been translated into your language

**原文标题**: Show HN: Zenòdot – Find if a book has been translated into your language

**原文链接**: [https://www.zenodot.app/](https://www.zenodot.app/)

生成摘要时出错

---

## 33. Promptfoo Is Joining OpenAI

**原文标题**: Promptfoo Is Joining OpenAI

**原文链接**: [https://www.promptfoo.dev/blog/promptfoo-joining-openai/](https://www.promptfoo.dev/blog/promptfoo-joining-openai/)

生成摘要时出错

---

## 34. PCB devboard the size of a USB-C plug

**原文标题**: PCB devboard the size of a USB-C plug

**原文链接**: [https://github.com/Dieu-de-l-elec/AngstromIO-devboard](https://github.com/Dieu-de-l-elec/AngstromIO-devboard)

生成摘要时出错

---

## 35. Every single board computer I tested in 2025

**原文标题**: Every single board computer I tested in 2025

**原文链接**: [https://bret.dk/every-single-board-computer-i-tested-in-2025/](https://bret.dk/every-single-board-computer-i-tested-in-2025/)

生成摘要时出错

---

## 36. FrameBook

**原文标题**: FrameBook

**原文链接**: [https://fb.edoo.gg](https://fb.edoo.gg)

生成摘要时出错

---

## 37. The engine of Germany's wealth is blocking its future

**原文标题**: The engine of Germany's wealth is blocking its future

**原文链接**: [https://europeancorrespondent.com/en/r/the-engine-of-germanys-wealth-is-blocking-its-future](https://europeancorrespondent.com/en/r/the-engine-of-germanys-wealth-is-blocking-its-future)

生成摘要时出错

---

## 38. My Homelab Setup

**原文标题**: My Homelab Setup

**原文链接**: [https://bryananthonio.com/blog/my-homelab-setup/](https://bryananthonio.com/blog/my-homelab-setup/)

生成摘要时出错

---

## 39. A modder runs GTA V in Linux on PS5

**原文标题**: A modder runs GTA V in Linux on PS5

**原文链接**: [https://www.notebookcheck.net/A-modder-has-successfully-ported-Linux-to-the-PS5-running-GTA-5-Enhanced-with-ray-tracing.1244367.0.html](https://www.notebookcheck.net/A-modder-has-successfully-ported-Linux-to-the-PS5-running-GTA-5-Enhanced-with-ray-tracing.1244367.0.html)

生成摘要时出错

---

## 40. The Finger and the Moon

**原文标题**: The Finger and the Moon

**原文链接**: [https://taylor.town/finger-moon](https://taylor.town/finger-moon)

生成摘要时出错

---

## 41. Linux Internals: How /proc/self/mem writes to unwritable memory (2021)

**原文标题**: Linux Internals: How /proc/self/mem writes to unwritable memory (2021)

**原文链接**: [https://offlinemark.com/an-obscure-quirk-of-proc/](https://offlinemark.com/an-obscure-quirk-of-proc/)

生成摘要时出错

---

## 42. Artificial-life: A simple (300 lines of code) reproduction of Computational Life

**原文标题**: Artificial-life: A simple (300 lines of code) reproduction of Computational Life

**原文链接**: [https://github.com/Rabrg/artificial-life](https://github.com/Rabrg/artificial-life)

生成摘要时出错

---

## 43. Why can't you tune your guitar? (2019)

**原文标题**: Why can't you tune your guitar? (2019)

**原文链接**: [https://www.ethanhein.com/wp/2019/why-cant-you-tune-your-guitar/](https://www.ethanhein.com/wp/2019/why-cant-you-tune-your-guitar/)

生成摘要时出错

---

## 44. Living human brain cells play DOOM on a CL1 [video]

**原文标题**: Living human brain cells play DOOM on a CL1 [video]

**原文链接**: [https://www.youtube.com/watch?v=yRV8fSw6HaE](https://www.youtube.com/watch?v=yRV8fSw6HaE)

生成摘要时出错

---

## 45. I made a programming language with M&Ms

**原文标题**: I made a programming language with M&Ms

**原文链接**: [https://mufeedvh.com/posts/i-made-a-programming-language-with-mnms/](https://mufeedvh.com/posts/i-made-a-programming-language-with-mnms/)

生成摘要时出错

---

## 46. Z80 Sans – a disassembler in a font (2024)

**原文标题**: Z80 Sans – a disassembler in a font (2024)

**原文链接**: [https://github.com/nevesnunes/z80-sans](https://github.com/nevesnunes/z80-sans)

生成摘要时出错

---

## 47. Peter Thiel and Jeffrey Epstein Had a Yearslong Relationship

**原文标题**: Peter Thiel and Jeffrey Epstein Had a Yearslong Relationship

**原文链接**: [https://jacobin.com/2026/03/thiel-epstein-barak-ai-israel/](https://jacobin.com/2026/03/thiel-epstein-barak-ai-israel/)

生成摘要时出错

---

## 48. We should revisit literate programming in the agent era

**原文标题**: We should revisit literate programming in the agent era

**原文链接**: [https://silly.business/blog/we-should-revisit-literate-programming-in-the-agent-era/](https://silly.business/blog/we-should-revisit-literate-programming-in-the-agent-era/)

生成摘要时出错

---

## 49. WSL Manager

**原文标题**: WSL Manager

**原文链接**: [https://github.com/bostrot/wsl2-distro-manager](https://github.com/bostrot/wsl2-distro-manager)

生成摘要时出错

---

## 50. How the Sriracha guys screwed over their supplier

**原文标题**: How the Sriracha guys screwed over their supplier

**原文链接**: [https://old.reddit.com/r/KitchenConfidential/comments/1ro61g2/how_the_sriracha_guys_screwed_over_their_supplier/](https://old.reddit.com/r/KitchenConfidential/comments/1ro61g2/how_the_sriracha_guys_screwed_over_their_supplier/)

生成摘要时出错

---

## 51. Anthropic sues to block Pentagon blacklisting over AI use restrictions

**原文标题**: Anthropic sues to block Pentagon blacklisting over AI use restrictions

**原文链接**: [https://www.reuters.com/world/anthropic-sues-block-pentagon-blacklisting-over-ai-use-restrictions-2026-03-09/](https://www.reuters.com/world/anthropic-sues-block-pentagon-blacklisting-over-ai-use-restrictions-2026-03-09/)

生成摘要时出错

---

## 52. The Arrogance of Ignorance. – By James Fallows

**原文标题**: The Arrogance of Ignorance. – By James Fallows

**原文链接**: [https://fallows.substack.com/p/the-arrogance-of-ignorance](https://fallows.substack.com/p/the-arrogance-of-ignorance)

生成摘要时出错

---

## 53. Show HN: I built a real-time OSINT dashboard pulling 15 live global feeds

**原文标题**: Show HN: I built a real-time OSINT dashboard pulling 15 live global feeds

**原文链接**: [https://github.com/BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker)

生成摘要时出错

---

## 54. Show HN: Skir – like Protocol Buffer but better

**原文标题**: Show HN: Skir – like Protocol Buffer but better

**原文链接**: [https://skir.build/](https://skir.build/)

生成摘要时出错

---

## 55. The death of social media is the renaissance of RSS (2025)

**原文标题**: The death of social media is the renaissance of RSS (2025)

**原文链接**: [https://www.smartlab.at/rss-revival-life-after-social-media/](https://www.smartlab.at/rss-revival-life-after-social-media/)

生成摘要时出错

---

## 56. The legendary Mojave Phone Booth is back (2013)

**原文标题**: The legendary Mojave Phone Booth is back (2013)

**原文链接**: [https://dailydot.com/mojave-phone-booth-back-number](https://dailydot.com/mojave-phone-booth-back-number)

生成摘要时出错

---

## 57. Pushing and Pulling: Three reactivity algorithms

**原文标题**: Pushing and Pulling: Three reactivity algorithms

**原文链接**: [https://jonathan-frere.com/posts/reactivity-algorithms/](https://jonathan-frere.com/posts/reactivity-algorithms/)

生成摘要时出错

---

## 58. Humanoid robot: The evolution of Kawasaki’s challenge

**原文标题**: Humanoid robot: The evolution of Kawasaki’s challenge

**原文链接**: [https://kawasakirobotics.com/in/blog/202511_kaleido/](https://kawasakirobotics.com/in/blog/202511_kaleido/)

生成摘要时出错

---

## 59. Beagle, a source code management system that stores AST trees

**原文标题**: Beagle, a source code management system that stores AST trees

**原文链接**: [https://github.com/gritzko/librdx/tree/master/be](https://github.com/gritzko/librdx/tree/master/be)

生成摘要时出错

---

## 60. SigNoz (YC W21) is hiring for engineering, growth and product roles

**原文标题**: SigNoz (YC W21) is hiring for engineering, growth and product roles

**原文链接**: [https://signoz.io/careers](https://signoz.io/careers)

生成摘要时出错

---

## 61. What if the Apple ][ had run on Field-Sequential?

**原文标题**: What if the Apple ][ had run on Field-Sequential?

**原文链接**: [https://nicole.express/2026/the-apple-that-wasnt.html](https://nicole.express/2026/the-apple-that-wasnt.html)

生成摘要时出错

---

## 62. Terence Tao: Formalizing a proof in Lean using Claude Code [video]

**原文标题**: Terence Tao: Formalizing a proof in Lean using Claude Code [video]

**原文链接**: [https://www.youtube.com/watch?v=JHEO7cplfk8](https://www.youtube.com/watch?v=JHEO7cplfk8)

生成摘要时出错

---

## 63. SWE-CI: Evaluating Agent Capabilities in Maintaining Codebases via CI

**原文标题**: SWE-CI: Evaluating Agent Capabilities in Maintaining Codebases via CI

**原文链接**: [https://arxiv.org/abs/2603.03823](https://arxiv.org/abs/2603.03823)

生成摘要时出错

---

## 64. Anthropic sues US defense department over blacklisting

**原文标题**: Anthropic sues US defense department over blacklisting

**原文链接**: [https://www.theguardian.com/technology/2026/mar/09/anthropic-defense-department-lawsuit-ai](https://www.theguardian.com/technology/2026/mar/09/anthropic-defense-department-lawsuit-ai)

生成摘要时出错

---

## 65. LibreOffice Writer now supports Markdown

**原文标题**: LibreOffice Writer now supports Markdown

**原文链接**: [https://blog.documentfoundation.org/blog/2026/02/04/libreoffice-26-2-is-here/](https://blog.documentfoundation.org/blog/2026/02/04/libreoffice-26-2-is-here/)

生成摘要时出错

---

## 66. Warn about PyPy being unmaintained

**原文标题**: Warn about PyPy being unmaintained

**原文链接**: [https://github.com/astral-sh/uv/pull/17643](https://github.com/astral-sh/uv/pull/17643)

生成摘要时出错

---

## 67. My “grand vision” for Rust

**原文标题**: My “grand vision” for Rust

**原文链接**: [https://blog.yoshuawuyts.com/a-grand-vision-for-rust/](https://blog.yoshuawuyts.com/a-grand-vision-for-rust/)

生成摘要时出错

---

## 68. Case Study: lynnandtonic.com 2025 refresh

**原文标题**: Case Study: lynnandtonic.com 2025 refresh

**原文链接**: [https://lynnandtonic.com/thoughts/entries/case-study-2025-refresh/](https://lynnandtonic.com/thoughts/entries/case-study-2025-refresh/)

生成摘要时出错

---

## 69. Ambient Light Sensor working on M2 MacBook in Asahi

**原文标题**: Ambient Light Sensor working on M2 MacBook in Asahi

**原文链接**: [https://github.com/AsahiLinux/docs/issues/248](https://github.com/AsahiLinux/docs/issues/248)

生成摘要时出错

---

## 70. Russia targets Signal and WhatsApp accounts in cyber campaign

**原文标题**: Russia targets Signal and WhatsApp accounts in cyber campaign

**原文链接**: [https://english.aivd.nl/latest/news/2026/03/09/russia-targets-signal-and-whatsapp-accounts-in-cyber-campaign](https://english.aivd.nl/latest/news/2026/03/09/russia-targets-signal-and-whatsapp-accounts-in-cyber-campaign)

生成摘要时出错

---

## 71. Show HN: I built a site where strangers leave kind voice notes for each other

**原文标题**: Show HN: I built a site where strangers leave kind voice notes for each other

**原文链接**: [https://kindvoicenotes.com](https://kindvoicenotes.com)

生成摘要时出错

---

## 72. LLM Writing Tropes.md

**原文标题**: LLM Writing Tropes.md

**原文链接**: [https://tropes.fyi/tropes-md](https://tropes.fyi/tropes-md)

生成摘要时出错

---

## 73. Blacksky AppView

**原文标题**: Blacksky AppView

**原文链接**: [https://github.com/blacksky-algorithms/atproto](https://github.com/blacksky-algorithms/atproto)

生成摘要时出错

---

## 74. Anthropic Sues Pentagon over 'Supply Chain Risk' Label

**原文标题**: Anthropic Sues Pentagon over 'Supply Chain Risk' Label

**原文链接**: [https://www.nytimes.com/2026/03/09/technology/anthropic-defense-artificial-intelligence-lawsuit.html](https://www.nytimes.com/2026/03/09/technology/anthropic-defense-artificial-intelligence-lawsuit.html)

生成摘要时出错

---

## 75. Show HN: Husky hook that blocks Git push until you do your pushups

**原文标题**: Show HN: Husky hook that blocks Git push until you do your pushups

**原文链接**: [https://git-push.app](https://git-push.app)

生成摘要时出错

---

## 76. Show HN: Mcp2cli – One CLI for every API, 96-99% fewer tokens than native MCP

**原文标题**: Show HN: Mcp2cli – One CLI for every API, 96-99% fewer tokens than native MCP

**原文链接**: [https://github.com/knowsuchagency/mcp2cli](https://github.com/knowsuchagency/mcp2cli)

生成摘要时出错

---

## 77. The changing goalposts of AGI and timelines

**原文标题**: The changing goalposts of AGI and timelines

**原文链接**: [https://mlumiste.com/general/openai-charter/](https://mlumiste.com/general/openai-charter/)

生成摘要时出错

---

## 78. Some Words on WigglyPaint

**原文标题**: Some Words on WigglyPaint

**原文链接**: [https://beyondloom.com/blog/onwigglypaint.html](https://beyondloom.com/blog/onwigglypaint.html)

生成摘要时出错

---

## 79. Crow Watch: A Hacker News Alternative

**原文标题**: Crow Watch: A Hacker News Alternative

**原文链接**: [https://crow.watch](https://crow.watch)

生成摘要时出错

---

## 80. CLI RSS/Atom feed reader inspired by Taskwarrior, synced using Git

**原文标题**: CLI RSS/Atom feed reader inspired by Taskwarrior, synced using Git

**原文链接**: [https://github.com/kantord/blogtato](https://github.com/kantord/blogtato)

生成摘要时出错

---

## 81. I ported Linux to the PS5 and turned it into a Steam Machine

**原文标题**: I ported Linux to the PS5 and turned it into a Steam Machine

**原文链接**: [https://xcancel.com/theflow0/status/2030011206040256841](https://xcancel.com/theflow0/status/2030011206040256841)

生成摘要时出错

---

## 82. Lil Finder Guy

**原文标题**: Lil Finder Guy

**原文链接**: [https://basicappleguy.com/basicappleblog/lil-finder-guy](https://basicappleguy.com/basicappleblog/lil-finder-guy)

生成摘要时出错

---

## 83. LibreOffice: Request to the European Commission to adhere to its own guidances

**原文标题**: LibreOffice: Request to the European Commission to adhere to its own guidances

**原文链接**: [https://blog.documentfoundation.org/blog/2026/03/05/cra-guidances/](https://blog.documentfoundation.org/blog/2026/03/05/cra-guidances/)

生成摘要时出错

---

## 84. Apple's 512GB Mac Studio vanishes, a quiet acknowledgment of the RAM shortage

**原文标题**: Apple's 512GB Mac Studio vanishes, a quiet acknowledgment of the RAM shortage

**原文链接**: [https://arstechnica.com/gadgets/2026/03/apples-512gb-mac-studio-vanishes-a-quiet-acknowledgement-of-the-ram-shortage/](https://arstechnica.com/gadgets/2026/03/apples-512gb-mac-studio-vanishes-a-quiet-acknowledgement-of-the-ram-shortage/)

生成摘要时出错

---

## 85. Show HN: Reviving a 20-year-old puzzle game Chromatron with Ghidra and AI

**原文标题**: Show HN: Reviving a 20-year-old puzzle game Chromatron with Ghidra and AI

**原文链接**: [https://quesma.com/blog/chromatron-recompiled/](https://quesma.com/blog/chromatron-recompiled/)

生成摘要时出错

---

## 86. How to run Qwen 3.5 locally

**原文标题**: How to run Qwen 3.5 locally

**原文链接**: [https://unsloth.ai/docs/models/qwen3.5](https://unsloth.ai/docs/models/qwen3.5)

生成摘要时出错

---

## 87. A basket of new fruit varieties is coming your way

**原文标题**: A basket of new fruit varieties is coming your way

**原文链接**: [https://www.economist.com/science-and-technology/2026/03/04/a-basket-of-new-fruit-varieties-is-coming-your-way](https://www.economist.com/science-and-technology/2026/03/04/a-basket-of-new-fruit-varieties-is-coming-your-way)

生成摘要时出错

---

## 88. Sem – Semantic version control. Entity-level diffs on top of Git

**原文标题**: Sem – Semantic version control. Entity-level diffs on top of Git

**原文链接**: [https://github.com/ataraxy-labs/sem](https://github.com/ataraxy-labs/sem)

生成摘要时出错

---

## 89. AMD Expands Ryzen AI Embedded P100 Family with 8 to 12 Core Parts – ServeTheHome

**原文标题**: AMD Expands Ryzen AI Embedded P100 Family with 8 to 12 Core Parts – ServeTheHome

**原文链接**: [https://www.servethehome.com/amd-expands-ryzen-ai-embedded-p100-family-with-8-to-12-core-parts/](https://www.servethehome.com/amd-expands-ryzen-ai-embedded-p100-family-with-8-to-12-core-parts/)

生成摘要时出错

---

## 90. Show HN: Run 500B+ Parameter LLMs Locally on a Mac Mini

**原文标题**: Show HN: Run 500B+ Parameter LLMs Locally on a Mac Mini

**原文链接**: [https://github.com/opengraviton/graviton](https://github.com/opengraviton/graviton)

生成摘要时出错

---

## 91. If It Quacks Like a Package Manager

**原文标题**: If It Quacks Like a Package Manager

**原文链接**: [https://nesbitt.io/2026/03/08/if-it-quacks-like-a-package-manager.html](https://nesbitt.io/2026/03/08/if-it-quacks-like-a-package-manager.html)

生成摘要时出错

---

## 92. SQG (SQL to Code Generator) v0.10: Java Streams and List Type Support

**原文标题**: SQG (SQL to Code Generator) v0.10: Java Streams and List Type Support

**原文链接**: [https://sqg.dev/blog/java-streams-and-list-types/](https://sqg.dev/blog/java-streams-and-list-types/)

生成摘要时出错

---

## 93. MonoGame: A .NET framework for making cross-platform games

**原文标题**: MonoGame: A .NET framework for making cross-platform games

**原文链接**: [https://github.com/MonoGame/MonoGame](https://github.com/MonoGame/MonoGame)

生成摘要时出错

---

## 94. Corpus Christi careens toward water catastrophe

**原文标题**: Corpus Christi careens toward water catastrophe

**原文链接**: [https://www.texastribune.org/2026/03/08/texas-corpus-christi-water-crisis/](https://www.texastribune.org/2026/03/08/texas-corpus-christi-water-crisis/)

生成摘要时出错

---

## 95. Emacs internals: Deconstructing Lisp_Object in C (Part 2)

**原文标题**: Emacs internals: Deconstructing Lisp_Object in C (Part 2)

**原文链接**: [https://thecloudlet.github.io/blog/project/emacs-02/](https://thecloudlet.github.io/blog/project/emacs-02/)

生成摘要时出错

---

## 96. The new Apple begins to emerge

**原文标题**: The new Apple begins to emerge

**原文链接**: [https://parkerortolani.blog/2026/03/07/the-new-apple-finally-begins.html](https://parkerortolani.blog/2026/03/07/the-new-apple-finally-begins.html)

生成摘要时出错

---

## 97. How Brembo Redesigned F1 Brakes for the 2026 Power Unit Revolution

**原文标题**: How Brembo Redesigned F1 Brakes for the 2026 Power Unit Revolution

**原文链接**: [https://www.thedrive.com/news/how-brembo-redesigned-f1-brakes-for-the-2026-power-unit-revolution](https://www.thedrive.com/news/how-brembo-redesigned-f1-brakes-for-the-2026-power-unit-revolution)

生成摘要时出错

---

## 98. Anthropic sues Defense Department over supply chain risk designation

**原文标题**: Anthropic sues Defense Department over supply chain risk designation

**原文链接**: [https://techcrunch.com/2026/03/09/anthropic-sues-defense-department-over-supply-chain-risk-designation/](https://techcrunch.com/2026/03/09/anthropic-sues-defense-department-over-supply-chain-risk-designation/)

生成摘要时出错

---

## 99. How Big Diaper absorbs billions of extra dollars from American parents

**原文标题**: How Big Diaper absorbs billions of extra dollars from American parents

**原文链接**: [https://thehustle.co/originals/how-big-diaper-absorbs-billions-of-extra-dollars-from-american-parents](https://thehustle.co/originals/how-big-diaper-absorbs-billions-of-extra-dollars-from-american-parents)

生成摘要时出错

---

## 100. Show HN: Eyot, A programming language where the GPU is just another thread

**原文标题**: Show HN: Eyot, A programming language where the GPU is just another thread

**原文链接**: [https://cowleyforniastudios.com/2026/03/08/announcing-eyot/](https://cowleyforniastudios.com/2026/03/08/announcing-eyot/)

生成摘要时出错

---

