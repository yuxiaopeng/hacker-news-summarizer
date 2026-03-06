# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-03-06.md)

*最后自动更新时间: 2026-03-06 18:05:02*
## 1. Show HN：Moongate —— 基于 .NET 10 并支持 Lua 脚本的《网络创世纪》服务器模拟器

**原文标题**: Show HN: Moongate – Ultima Online server emulator in .NET 10 with Lua scripting

**原文链接**: [https://github.com/moongate-community/moongatev2](https://github.com/moongate-community/moongatev2)

**Moongate v2** 是一个基于 **.NET 10** 构建的现代化、从零开发的《网络创世纪》(UO) 服务器模拟器。它旨在实现高性能和高可维护性，并非直接克隆 RunUO 或 ServUO 等传统模拟器，而是专注于针对 **Native AOT**（提前编译）优化的清晰模块化架构。

**核心技术特性：**
*   **性能驱动内核：** 引擎采用确定性游戏循环，通过源生成器（Source Generators）消除运行时反射，并使用专用网络线程来减少对游戏循环的争用。
*   **空间策略：** 不同于传统的 UO 服务器，Moongate 采用了类似于《我的世界》的**基于扇区/区块的流式模型**。世界数据以 16x16 扇区进行索引并实现延迟加载，以确保可预测的内存占用和更好的 CPU 缓存局部性。
*   **持久化：** 状态管理采用基于 **MessagePack-CSharp** 的二进制快照和仅追加（append-only）日志系统，确保快速、线程安全的数据恢复与完整性。
*   **脚本与工具：** 内置强大的 **Lua 脚本运行时**用于处理指令和游戏逻辑，同时集成 HTTP 主机以提供管理健康检查端点和 OpenAPI 文档。

**当前状态：**
项目正处于活跃开发中。虽然目前已支持核心功能（包括身份验证、移动、世界同步以及基础物品/容器交互），但**完整战斗循环、NPC AI 和经济系统**等重大系统尚未实现。

Moongate 是开源项目，诚邀开发者参与代码审查和功能开发。它面向希望以现代 C# 方式实现经典 MMORPG 模拟的开发者，强调开发迭代速度和正确性，而非对旧系统的兼容。

---

## 2. Open Camera 是一款安卓平台的自由开源相机应用。

**原文标题**: Open Camera is a FOSS Camera App for Android

**原文链接**: [https://opencamera.org.uk/](https://opencamera.org.uk/)

**Open Camera**是一款由Mark Harman开发的适用于Android设备（5.0及以上版本）的免费开源相机应用。该应用基于GPL v3协议发布，其显著特点是完全没有任何第三方广告和应用内购买。

该应用提供了一套专为摄影和摄像设计的专业级功能，主要亮点包括：

*   **高级成像：** 支持HDR、全景模式、曝光包围、对焦包围以及自动水平校准，确保照片构图平直。
*   **手动控制：** 利用Camera2 API，提供对ISO、曝光、白平衡和对焦的手动调节。它还支持RAW (DNG) 格式文件和慢动作视频拍摄。
*   **远程功能：** 用户可以通过定时器、语音倒计时，甚至通过发出特定的声音来触发快门。
*   **自定义与界面：** 界面高度可定制，提供屏幕直方图、斑马纹、对焦峰值和裁剪指南。它还具备“倒置”预览模式，以配合外接镜头使用。
*   **数据与隐私：** 支持详尽的GPS地理标记以及在照片上添加自定义文本或时间戳。同时，它也提供移除EXIF元数据的选项，以加强隐私保护。

尽管Open Camera功能丰富，但开发者提示硬件兼容性因设备而异，建议在用于重要场合前先进行测试。该项目使用了多种开源库和图标（主要来自Google的Material Design套件），并托管在SourceForge上。总体而言，它是系统自带相机应用的一个功能强大且注重隐私的理想替代品。

---

## 3. 健康可穿戴设备的CT扫描

**原文标题**: CT Scans of Health Wearables

**原文链接**: [https://www.lumafield.com/scan-of-the-month/health-wearables](https://www.lumafield.com/scan-of-the-month/health-wearables)

本文通过 CT 扫描揭示了四款现代健康可穿戴设备精密的内部工程设计，重点展示了小型化趋势以及技术与人体生物学的无缝集成。

*   **Oura Ring (智能戒指)：** Oura Ring 嵌入在无缝防水的钛金属环形外壳内，利用弯曲柔性电路承载脉搏和温度监测传感器。它配备了定制形状的锂聚合物电池和无线充电线圈，实现了无接口、无螺钉的光滑外观。
*   **Dexcom G7 (连续血糖监测仪)：** 这款一次性贴片通过一根发丝般纤细的柔性感测丝从组织间液中采集葡萄糖样本。其设计包含用于蓝牙通信的螺旋铜天线和锌空纽扣电池，所有组件均针对支持 10 天持续佩戴的小型化外形进行了优化。
*   **Omnipod (贴敷式注射泵)：** 这是一款火柴盒大小的一次性自动给药泵。其机械系统包括用于植入针头的弹簧驱动执行器，以及一套精密棘轮轮系，该轮系能以微升增量推动活塞，以确保精准给药。
*   **Jabra Enhance Select 50 (助听器)：** 该设备在超紧凑的框架内集成了双麦克风阵列、数字信号处理器和微型扬声器。它采用分层 PCB 将音频信号与电源组件隔离，从而保持极高的声学保真度和噪声过滤效果。

文章总结指出，这些设备开启了“隐形”技术的新时代。通过应用柔性基板和无线感应等微米级精密组件，工程师们正在打造能够在人体耐受范围内运行的关键生命体征穿戴设备，有效地模糊了工业制造与生物学之间的界限。

---

## 4. 公用电话 Go

**原文标题**: Payphone Go

**原文链接**: [https://walzr.com/payphone-go/](https://walzr.com/payphone-go/)

**Payphone Go** 是一款由开发者 Riley Walz 开发的互动式、基于地理位置的游戏，它将纽约市残存的、仍可使用的公用电话转变为一场数字寻宝之旅。该项目受怀旧情结以及模拟基础设施迅速消亡的启发，鼓励玩家追踪并“占领”实体公用电话，以提升其在全球排行榜上的名次。

参与者需通过该项目的地图定位一部幸存的公用电话。抵达现场后，玩家拨打网页应用提供的特定号码。随后系统会回拨该公用电话；当玩家接听响铃的电话时，该位置即被验证为“已占领”，玩家随之获得积分。这种独特的验证方式确保了参与者本人必须亲临现场，将这一时代的遗迹变成了一个现代城市游乐场。

在智能手机和 LinkNYC 服务亭占据主导地位的时代，该项目凸显了公用电话惊人的生命力。虽然纽约市已经拆除了大部分著名的电话亭，但仍有数千部独立或路边电话在运行，且往往就隐藏在人们的视线之中。Walz 投入了大量精力整理和测试活跃号码数据库，以确保游戏的正常运作。

归根结底，《Payphone Go》既是一款竞技游戏，也是一份数字档案。它在最后一批机器被彻底移除之前，为城市探索提供了趣味性的动力，同时也记录了一段正在消亡的电信历史。

---

## 5. 热衷于“协同范式”的员工，可能并不擅长自己的工作。

**原文标题**: Workers who love 'synergizing paradigms' might be bad at their jobs

**原文链接**: [https://news.cornell.edu/stories/2026/03/workers-who-love-synergizing-paradigms-might-be-bad-their-jobs](https://news.cornell.edu/stories/2026/03/workers-who-love-synergizing-paradigms-might-be-bad-their-jobs)

由康奈尔大学认知心理学家谢恩·利特雷尔（Shane Littrell）领导的一项新研究表明，那些容易被“企业废话”（即“协同范式”等模糊、抽象的流行词）打动的员工，在实际工作表现中可能会遇到困难。

为开展这项研究，利特雷尔开发了“企业废话易感性量表”（CBSR），旨在衡量个人对组织空洞辞令的易感程度。与能够简化沟通的技术术语不同，“企业废话”被定义为利用听起来高大上的词汇来制造困惑而非阐明意义的语言。

研究结果揭示了一个令人不安的悖论：虽然对企业黑话接受度更高的员工拥有更高的工作满意度，并认为他们的领导更具“远见”，但他们在分析思维、流体智力和有效决策测试中的得分也明显更低。此外，那些轻信企业废话的人更有可能亲自传播这些话，从而形成一种“负反馈循环”。这种循环会提拔那些利用黑话掩盖无能或传达坏消息的失职领导者，例如臭名昭著的2014年微软备忘录，该文件在长达十段的晦涩黑话中掩盖了1.25万人的裁员消息。

利特雷尔警告称，这种“信息遮眼布”可能导致“效率低下的塞马桶效应”，对公司的声誉和财务造成实质性损害。该研究强调了批判性思维的重要性，建议员工和消费者都应“慢下来”，评估企业信息是包含实质性内容，还是仅仅为空洞的辞令。最终，CBSR 可能会成为招聘人员评估应聘者分析倾向和决策能力的工具。

---

## 6. Astra: An open-source observatory control software

**原文标题**: Astra: An open-source observatory control software

**原文链接**: [https://github.com/ppp-one/astra](https://github.com/ppp-one/astra)

**Astra**（基于 Alpaca 的自动化巡天机器人天文台）是一款开源软件套件，专为机器人天文台的全面自动化与管理而设计。该平台基于 Python 构建，具有跨平台特性，支持 Windows、Linux 和 macOS。

该软件的核心优势在于其**全自动化运行**，允许用户安排观测计划并由系统自动执行。这包括内置的错误处理协议以及针对恶劣天气条件的安全保护措施。在硬件集成方面，Astra 采用 **ASCOM Alpaca** 标准，确保了与各种现有天文设备的兼容性。

核心特性包括：
*   **基于 Web 的界面：** 支持通过任何浏览器进行远程管理，提供对天文台状态、系统日志、天气监测和硬件控制的实时访问。
*   **易于使用：** 配有完善的文档，涵盖了安装设置、使用说明及模块参考。
*   **开源开发：** 该项目在 GNU GPL v3 协议下发布，鼓励社区通过 GitHub 参与贡献。

Astra 由 Peter P. Pedersen 领导的团队开发，适用于业余爱好者和专业科研人员。鼓励使用该软件的研究人员通过其注册的 DOI (10.5281/zenodo.18890151) 进行引用。总的来说，Astra 提供了一个稳健且易于获取的解决方案，能够将标准望远镜设备转化为自主运行、可远程访问的机器人天文台。

---

## 7. Multifactor (YC F25) Is Hiring an Engineering Lead

**原文标题**: Multifactor (YC F25) Is Hiring an Engineering Lead

**原文链接**: [https://www.ycombinator.com/companies/multifactor/jobs/lcpd60A-engineering-lead](https://www.ycombinator.com/companies/multifactor/jobs/lcpd60A-engineering-lead)

生成摘要时出错

---

## 8. Analytic Fog Rendering with Volumetric Primitives (2025)

**原文标题**: Analytic Fog Rendering with Volumetric Primitives (2025)

**原文链接**: [https://matejlou.blog/2025/02/11/analytic-fog-rendering-with-volumetric-primitives/](https://matejlou.blog/2025/02/11/analytic-fog-rendering-with-volumetric-primitives/)

生成摘要时出错

---

## 9. Global warming has accelerated significantly

**原文标题**: Global warming has accelerated significantly

**原文链接**: [https://www.researchgate.net/publication/389855619_Global_Warming_has_Accelerated_Significantly](https://www.researchgate.net/publication/389855619_Global_Warming_has_Accelerated_Significantly)

生成摘要时出错

---

## 10. LibreSprite – open-source pixel art editor

**原文标题**: LibreSprite – open-source pixel art editor

**原文链接**: [https://libresprite.github.io/](https://libresprite.github.io/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 2 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 3 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 4 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 5 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 6 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 7 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 8 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 9 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 10 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 11 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 12 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 13 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 14 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 15 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 16 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 17 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 18 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 19 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 20 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 21 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 22 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 23 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 24 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 25 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 26 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 27 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 28 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 29 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 30 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 31 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 32 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 33 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 34 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 35 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 36 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 37 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 38 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 39 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 40 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 41 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 42 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 43 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 44 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 45 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 46 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 47 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 48 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 49 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 50 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 51 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 52 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 53 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 54 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 55 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 56 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 57 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 58 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 59 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 60 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 61 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 62 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 63 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 64 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 65 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 66 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 67 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 68 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 69 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 70 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 71 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 72 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 73 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 74 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 75 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 76 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 77 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 78 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 79 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 80 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 81 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 82 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 83 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 84 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 85 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 86 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 87 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 88 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 89 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 90 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 91 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 92 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 93 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 94 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 95 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 96 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 97 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 98 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 99 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 100 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 101 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 102 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 103 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 104 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 105 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 106 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 107 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 108 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 109 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 110 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 111 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 112 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 113 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 114 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 115 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 116 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 117 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 118 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 119 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 120 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 121 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 122 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 123 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 124 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 125 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 126 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 127 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 128 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 129 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 130 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 131 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 132 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 133 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 134 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 135 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 136 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 137 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 138 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 139 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 140 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 141 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 142 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 143 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 144 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 145 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 146 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 147 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 148 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 149 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 150 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 151 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 152 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 153 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 154 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 155 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 156 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 157 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 158 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 159 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 160 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 161 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 162 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 163 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 164 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 165 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 166 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 167 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 168 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 169 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 170 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 171 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 172 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 173 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 174 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 175 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 176 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 177 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 178 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 179 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 180 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 181 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 182 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 183 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 184 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 185 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 186 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 187 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 188 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 189 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 190 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 191 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 192 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 193 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 194 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 195 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 196 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 197 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 198 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 199 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 200 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 201 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 202 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 203 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 204 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 205 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 206 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 207 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 208 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 209 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 210 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 211 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 212 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 213 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 214 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 215 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 216 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 217 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 218 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 219 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 220 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 221 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 222 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 223 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 224 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 225 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 226 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 227 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 228 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 229 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 230 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 231 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 232 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 233 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 234 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 235 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 236 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 237 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 238 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 239 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 240 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 241 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 242 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 243 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 244 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 245 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 246 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 247 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 248 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 249 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 250 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 251 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 252 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 253 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 254 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 255 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 256 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 257 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 258 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 259 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 260 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 261 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 262 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 263 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 264 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 265 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 266 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 267 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 268 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 269 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 270 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 271 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 272 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 273 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 274 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 275 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 276 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 277 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 278 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 279 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 280 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 281 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 282 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 283 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 284 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 285 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 286 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 287 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 288 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 289 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 290 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 291 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 292 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 293 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 294 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 295 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 296 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 297 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 298 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 299 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 300 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 301 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 302 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 303 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 304 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 305 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 306 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 307 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 308 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 309 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 310 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 311 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 312 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 313 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 314 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 315 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 316 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 317 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 318 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 319 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 320 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 321 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 322 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 323 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 324 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 325 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 326 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 327 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 328 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 329 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 330 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 331 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 332 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 333 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 334 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 335 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 336 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 337 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 338 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 339 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 340 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 341 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 342 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 343 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 344 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 345 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 346 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 347 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 348 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 349 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 350 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 351 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
