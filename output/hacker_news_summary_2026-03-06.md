# Hacker News 热门文章摘要 (2026-03-06)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Entomologists use a particle accelerator to image ants at scale

**原文标题**: Entomologists use a particle accelerator to image ants at scale

**原文链接**: [https://spectrum.ieee.org/3d-scanning-particle-accelerator-antscan](https://spectrum.ieee.org/3d-scanning-particle-accelerator-antscan)

生成摘要时出错

---

## 12. GPT-5.4

**原文标题**: GPT-5.4

**原文链接**: [https://openai.com/index/introducing-gpt-5-4/](https://openai.com/index/introducing-gpt-5-4/)

生成摘要时出错

---

## 13. Supertoast Tables

**原文标题**: Supertoast Tables

**原文链接**: [https://hatchet.run/blog/supertoast-tables](https://hatchet.run/blog/supertoast-tables)

生成摘要时出错

---

## 14. Aldus PageMaker Founder Paul Brainerd Has Died

**原文标题**: Aldus PageMaker Founder Paul Brainerd Has Died

**原文链接**: [https://blog.adafruit.com/2026/03/04/pagemaker-and-aldus-founder-pioneer-paul-brainerd-1947-2026/](https://blog.adafruit.com/2026/03/04/pagemaker-and-aldus-founder-pioneer-paul-brainerd-1947-2026/)

生成摘要时出错

---

## 15. Good Bad ISPs

**原文标题**: Good Bad ISPs

**原文链接**: [https://community.torproject.org/relay/community-resources/good-bad-isps/](https://community.torproject.org/relay/community-resources/good-bad-isps/)

生成摘要时出错

---

## 16. 10% of Firefox crashes are caused by bitflips

**原文标题**: 10% of Firefox crashes are caused by bitflips

**原文链接**: [https://mas.to/@gabrielesvelto/116171750653898304](https://mas.to/@gabrielesvelto/116171750653898304)

生成摘要时出错

---

## 17. “I'm obviously taking a risk here by advertising emoji directly”

**原文标题**: “I'm obviously taking a risk here by advertising emoji directly”

**原文链接**: [https://unsung.aresluna.org/im-obviously-taking-a-risk-here-by-advertising-emoji-directly/](https://unsung.aresluna.org/im-obviously-taking-a-risk-here-by-advertising-emoji-directly/)

生成摘要时出错

---

## 18. Hardening Firefox with Anthropic's Red Team

**原文标题**: Hardening Firefox with Anthropic's Red Team

**原文链接**: [https://blog.mozilla.org/en/firefox/hardening-firefox-anthropic-red-team/](https://blog.mozilla.org/en/firefox/hardening-firefox-anthropic-red-team/)

生成摘要时出错

---

## 19. Show HN: Interactive 3D globe of EU shipping emissions

**原文标题**: Show HN: Interactive 3D globe of EU shipping emissions

**原文链接**: [https://seafloor.pages.dev](https://seafloor.pages.dev)

生成摘要时出错

---

## 20. US economy unexpectedly sheds 92,000 jobs in February

**原文标题**: US economy unexpectedly sheds 92,000 jobs in February

**原文链接**: [https://www.bbc.com/news/articles/cjd98091g28o](https://www.bbc.com/news/articles/cjd98091g28o)

生成摘要时出错

---

## 21. System76 on Age Verification Laws

**原文标题**: System76 on Age Verification Laws

**原文链接**: [https://blog.system76.com/post/system76-on-age-verification/](https://blog.system76.com/post/system76-on-age-verification/)

生成摘要时出错

---

## 22. A GitHub Issue Title Compromised 4k Developer Machines

**原文标题**: A GitHub Issue Title Compromised 4k Developer Machines

**原文链接**: [https://grith.ai/blog/clinejection-when-your-ai-tool-installs-another](https://grith.ai/blog/clinejection-when-your-ai-tool-installs-another)

生成摘要时出错

---

## 23. Xous security focused open source on 22nm custom silicon

**原文标题**: Xous security focused open source on 22nm custom silicon

**原文链接**: [https://www.crowdsupply.com/sutajio-kosagi/precursor/updates/xous-0-10-0-introducing-baochip-1x-support](https://www.crowdsupply.com/sutajio-kosagi/precursor/updates/xous-0-10-0-introducing-baochip-1x-support)

生成摘要时出错

---

## 24. GPL upgrades via section 14 proxy delegation

**原文标题**: GPL upgrades via section 14 proxy delegation

**原文链接**: [https://runxiyu.org/comp/gplproxy/](https://runxiyu.org/comp/gplproxy/)

生成摘要时出错

---

## 25. CBP says it can't comply with refund order

**原文标题**: CBP says it can't comply with refund order

**原文链接**: [https://www.cnbc.com/2026/03/06/trump-trade-tariffs-refunds-customs-border-protection.html](https://www.cnbc.com/2026/03/06/trump-trade-tariffs-refunds-customs-border-protection.html)

生成摘要时出错

---

## 26. Show HN: Swarm – Program a colony of 200 ants using a custom assembly language

**原文标题**: Show HN: Swarm – Program a colony of 200 ants using a custom assembly language

**原文链接**: [https://dev.moment.com/](https://dev.moment.com/)

生成摘要时出错

---

## 27. The Brand Age

**原文标题**: The Brand Age

**原文链接**: [https://paulgraham.com/brandage.html](https://paulgraham.com/brandage.html)

生成摘要时出错

---

## 28. We might all be AI engineers now

**原文标题**: We might all be AI engineers now

**原文链接**: [https://yasint.dev/we-might-all-be-ai-engineers-now/](https://yasint.dev/we-might-all-be-ai-engineers-now/)

生成摘要时出错

---

## 29. Image manipulation with convolution using Julia

**原文标题**: Image manipulation with convolution using Julia

**原文链接**: [https://medium.com/@Ahmad_Hamze/image-manipulation-with-convolution-using-julia-f898995ac1e5](https://medium.com/@Ahmad_Hamze/image-manipulation-with-convolution-using-julia-f898995ac1e5)

生成摘要时出错

---

## 30. Good software knows when to stop

**原文标题**: Good software knows when to stop

**原文链接**: [https://ogirardot.writizzy.com/p/good-software-knows-when-to-stop](https://ogirardot.writizzy.com/p/good-software-knows-when-to-stop)

生成摘要时出错

---

## 31. Charging a three-cell nickel-based battery pack with a Li-Ion charger [pdf]

**原文标题**: Charging a three-cell nickel-based battery pack with a Li-Ion charger [pdf]

**原文链接**: [https://www.ti.com/lit/an/slyt468/slyt468.pdf](https://www.ti.com/lit/an/slyt468/slyt468.pdf)

生成摘要时出错

---

## 32. A standard protocol to handle and discard low-effort, AI-Generated pull requests

**原文标题**: A standard protocol to handle and discard low-effort, AI-Generated pull requests

**原文链接**: [https://406.fail/](https://406.fail/)

生成摘要时出错

---

## 33. Nobody ever got fired for using a struct

**原文标题**: Nobody ever got fired for using a struct

**原文链接**: [https://www.feldera.com/blog/nobody-ever-got-fired-for-using-a-struct](https://www.feldera.com/blog/nobody-ever-got-fired-for-using-a-struct)

生成摘要时出错

---

## 34. Labor market impacts of AI: A new measure and early evidence

**原文标题**: Labor market impacts of AI: A new measure and early evidence

**原文链接**: [https://www.anthropic.com/research/labor-market-impacts](https://www.anthropic.com/research/labor-market-impacts)

生成摘要时出错

---

## 35. 70k Books Found in Hidden Library in This Germany Home

**原文标题**: 70k Books Found in Hidden Library in This Germany Home

**原文链接**: [https://bookstr.com/article/70k-books-found-in-hidden-library-in-this-germany-home/](https://bookstr.com/article/70k-books-found-in-hidden-library-in-this-germany-home/)

生成摘要时出错

---

## 36. Show HN: Modembin – A pastebin that encodes your text into real FSK modem audio

**原文标题**: Show HN: Modembin – A pastebin that encodes your text into real FSK modem audio

**原文链接**: [https://www.modembin.com](https://www.modembin.com)

生成摘要时出错

---

## 37. Where things stand with the Department of War

**原文标题**: Where things stand with the Department of War

**原文链接**: [https://www.anthropic.com/news/where-stand-department-war](https://www.anthropic.com/news/where-stand-department-war)

生成摘要时出错

---

## 38. I dropped our production database and now pay 10% more for AWS

**原文标题**: I dropped our production database and now pay 10% more for AWS

**原文链接**: [https://alexeyondata.substack.com/p/how-i-dropped-our-production-database](https://alexeyondata.substack.com/p/how-i-dropped-our-production-database)

生成摘要时出错

---

## 39. Screeching Sound of Peeling Tape

**原文标题**: Screeching Sound of Peeling Tape

**原文链接**: [https://journals.aps.org/pre/abstract/10.1103/p19h-9ysx](https://journals.aps.org/pre/abstract/10.1103/p19h-9ysx)

生成摘要时出错

---

## 40. Wikipedia was in read-only mode following mass admin account compromise

**原文标题**: Wikipedia was in read-only mode following mass admin account compromise

**原文链接**: [https://www.wikimediastatus.net](https://www.wikimediastatus.net)

生成摘要时出错

---

## 41. AI and the Ship of Theseus

**原文标题**: AI and the Ship of Theseus

**原文链接**: [https://lucumr.pocoo.org/2026/3/5/theseus/](https://lucumr.pocoo.org/2026/3/5/theseus/)

生成摘要时出错

---

## 42. A ternary plot of citrus geneology

**原文标题**: A ternary plot of citrus geneology

**原文链接**: [https://www.jlauf.com/writing/citrus/](https://www.jlauf.com/writing/citrus/)

生成摘要时出错

---

## 43. Judge orders government to begin refunding more than $130B in tariffs

**原文标题**: Judge orders government to begin refunding more than $130B in tariffs

**原文链接**: [https://www.wsj.com/politics/policy/judge-orders-government-to-begin-refunding-more-than-130-billion-in-tariffs-fdc1e62c](https://www.wsj.com/politics/policy/judge-orders-government-to-begin-refunding-more-than-130-billion-in-tariffs-fdc1e62c)

生成摘要时出错

---

## 44. Hardware hotplug events on Linux, the gory details

**原文标题**: Hardware hotplug events on Linux, the gory details

**原文链接**: [https://arcanenibble.github.io/hardware-hotplug-events-on-linux-the-gory-details.html](https://arcanenibble.github.io/hardware-hotplug-events-on-linux-the-gory-details.html)

生成摘要时出错

---

## 45. Stupidly Obscure Programming in a Troubled Time (2018)

**原文标题**: Stupidly Obscure Programming in a Troubled Time (2018)

**原文链接**: [https://blog.podsnap.com/apply.html](https://blog.podsnap.com/apply.html)

生成摘要时出错

---

## 46. Remotely unlocking an encrypted hard disk

**原文标题**: Remotely unlocking an encrypted hard disk

**原文链接**: [https://jyn.dev/remotely-unlocking-an-encrypted-hard-disk/](https://jyn.dev/remotely-unlocking-an-encrypted-hard-disk/)

生成摘要时出错

---

## 47. CBP tapped into the online advertising ecosystem to track peoples’ movements

**原文标题**: CBP tapped into the online advertising ecosystem to track peoples’ movements

**原文链接**: [https://www.404media.co/cbp-tapped-into-the-online-advertising-ecosystem-to-track-peoples-movements/](https://www.404media.co/cbp-tapped-into-the-online-advertising-ecosystem-to-track-peoples-movements/)

生成摘要时出错

---

## 48. Show HN: PageAgent, A GUI agent that lives inside your web app

**原文标题**: Show HN: PageAgent, A GUI agent that lives inside your web app

**原文链接**: [https://alibaba.github.io/page-agent/](https://alibaba.github.io/page-agent/)

生成摘要时出错

---

## 49. How to install and start using LineageOS on your phone

**原文标题**: How to install and start using LineageOS on your phone

**原文链接**: [https://lockywolf.net/2026-02-19_How-to-install-and-start-using-LineageOS-on-your-phone.d/index.html](https://lockywolf.net/2026-02-19_How-to-install-and-start-using-LineageOS-on-your-phone.d/index.html)

生成摘要时出错

---

## 50. Show HN: Jido 2.0, Elixir Agent Framework

**原文标题**: Show HN: Jido 2.0, Elixir Agent Framework

**原文链接**: [https://jido.run/blog/jido-2-0-is-here](https://jido.run/blog/jido-2-0-is-here)

生成摘要时出错

---

## 51. Stop Anthropomorphizing the Machine

**原文标题**: Stop Anthropomorphizing the Machine

**原文链接**: [https://pseudosingleton.com/stop-anthropomorphizing-the-machine/](https://pseudosingleton.com/stop-anthropomorphizing-the-machine/)

生成摘要时出错

---

## 52. Async Programming Is Just Inject Time

**原文标题**: Async Programming Is Just Inject Time

**原文链接**: [https://willhbr.net/2026/03/02/async-inject-and-effects/](https://willhbr.net/2026/03/02/async-inject-and-effects/)

生成摘要时出错

---

## 53. The home computer war

**原文标题**: The home computer war

**原文链接**: [https://technicshistory.com/2026/03/06/the-home-computer-war/](https://technicshistory.com/2026/03/06/the-home-computer-war/)

生成摘要时出错

---

## 54. Poor Man's Polaroid

**原文标题**: Poor Man's Polaroid

**原文链接**: [https://boxart.lt/blog/poor_mans_polaroid?locale=en](https://boxart.lt/blog/poor_mans_polaroid?locale=en)

生成摘要时出错

---

## 55. Every Claim from Meta Child Safety Trials

**原文标题**: Every Claim from Meta Child Safety Trials

**原文链接**: [https://meta-trials.vercel.app/](https://meta-trials.vercel.app/)

生成摘要时出错

---

## 56. Data does not speak to you

**原文标题**: Data does not speak to you

**原文链接**: [https://tantaman.com/2026-03-02-data-doesnt-speak.html](https://tantaman.com/2026-03-02-data-doesnt-speak.html)

生成摘要时出错

---

## 57. OpenTitan Shipping in Production

**原文标题**: OpenTitan Shipping in Production

**原文链接**: [https://opensource.googleblog.com/2026/03/opentitan-shipping-in-production.html](https://opensource.googleblog.com/2026/03/opentitan-shipping-in-production.html)

生成摘要时出错

---

## 58. Hacking Super Mario 64 using covering spaces

**原文标题**: Hacking Super Mario 64 using covering spaces

**原文链接**: [https://happel.ai/posts/covering-spaces-geometries-visualized/](https://happel.ai/posts/covering-spaces-geometries-visualized/)

生成摘要时出错

---

## 59. MacBook Neo

**原文标题**: MacBook Neo

**原文链接**: [https://www.apple.com/newsroom/2026/03/say-hello-to-macbook-neo/](https://www.apple.com/newsroom/2026/03/say-hello-to-macbook-neo/)

生成摘要时出错

---

## 60. A radio "laser" from 8B years away lights up Earth

**原文标题**: A radio "laser" from 8B years away lights up Earth

**原文链接**: [https://modernengineeringmarvels.com/2026/03/06/truly-extraordinary-a-radio-laser-from-8-billion-years-away-lights-up-earth/](https://modernengineeringmarvels.com/2026/03/06/truly-extraordinary-a-radio-laser-from-8-billion-years-away-lights-up-earth/)

生成摘要时出错

---

## 61. Cameras built to police Iranians became the regime's Achilles' heel

**原文标题**: Cameras built to police Iranians became the regime's Achilles' heel

**原文链接**: [https://royapakzad.substack.com/p/youre-welcome-mr-supreme-leader](https://royapakzad.substack.com/p/youre-welcome-mr-supreme-leader)

生成摘要时出错

---

## 62. Converting dash cam videos into Panoramax images

**原文标题**: Converting dash cam videos into Panoramax images

**原文链接**: [https://www.openstreetmap.org/user/FeetAndInches/diary/408268](https://www.openstreetmap.org/user/FeetAndInches/diary/408268)

生成摘要时出错

---

## 63. Optimizing Recommendation Systems with JDK's Vector API

**原文标题**: Optimizing Recommendation Systems with JDK's Vector API

**原文链接**: [https://netflixtechblog.com/optimizing-recommendation-systems-with-jdks-vector-api-30d2830401ec](https://netflixtechblog.com/optimizing-recommendation-systems-with-jdks-vector-api-30d2830401ec)

生成摘要时出错

---

## 64. Greg Kroah-Hartman Stretches Support Periods for Key Linux LTS Kernels

**原文标题**: Greg Kroah-Hartman Stretches Support Periods for Key Linux LTS Kernels

**原文链接**: [https://fossforce.com/2026/03/greg-kroah-hartman-stretches-support-periods-for-key-linux-lts-kernels/](https://fossforce.com/2026/03/greg-kroah-hartman-stretches-support-periods-for-key-linux-lts-kernels/)

生成摘要时出错

---

## 65. Google Workspace CLI

**原文标题**: Google Workspace CLI

**原文链接**: [https://github.com/googleworkspace/cli](https://github.com/googleworkspace/cli)

生成摘要时出错

---

## 66. Show HN: Tensor Spy: inspect NumPy and PyTorch tensors in the browser, no upload

**原文标题**: Show HN: Tensor Spy: inspect NumPy and PyTorch tensors in the browser, no upload

**原文链接**: [https://tensorspy.com/](https://tensorspy.com/)

生成摘要时出错

---

## 67. Let's Get Physical

**原文标题**: Let's Get Physical

**原文链接**: [https://m4iler.cloud/posts/lets-get-physical/](https://m4iler.cloud/posts/lets-get-physical/)

生成摘要时出错

---

## 68. Proton Mail Helped FBI Unmask Anonymous 'Stop Cop City' Protester

**原文标题**: Proton Mail Helped FBI Unmask Anonymous 'Stop Cop City' Protester

**原文链接**: [https://www.404media.co/proton-mail-helped-fbi-unmask-anonymous-stop-cop-city-protestor/](https://www.404media.co/proton-mail-helped-fbi-unmask-anonymous-stop-cop-city-protestor/)

生成摘要时出错

---

## 69. Datasets for Reconstructing Visual Perception from Brain Data

**原文标题**: Datasets for Reconstructing Visual Perception from Brain Data

**原文链接**: [https://github.com/seelikat/neuro-visual-reconstruction-dataset-index](https://github.com/seelikat/neuro-visual-reconstruction-dataset-index)

生成摘要时出错

---

## 70. Typst Examples Book

**原文标题**: Typst Examples Book

**原文链接**: [https://sitandr.github.io/typst-examples-book/book/](https://sitandr.github.io/typst-examples-book/book/)

生成摘要时出错

---

## 71. TeX Live 2026 is available for download now

**原文标题**: TeX Live 2026 is available for download now

**原文链接**: [https://www.tug.org/texlive/acquire.html](https://www.tug.org/texlive/acquire.html)

生成摘要时出错

---

## 72. A man who broke into jail

**原文标题**: A man who broke into jail

**原文链接**: [https://www.newyorker.com/magazine/2026/03/09/alexander-friedmann-profile-prison-reform](https://www.newyorker.com/magazine/2026/03/09/alexander-friedmann-profile-prison-reform)

生成摘要时出错

---

## 73. Smalltalk's Browser: Unbeatable, yet Not Enough

**原文标题**: Smalltalk's Browser: Unbeatable, yet Not Enough

**原文链接**: [https://blog.lorenzano.eu/smalltalks-browser-unbeatable-yet-not-enough/](https://blog.lorenzano.eu/smalltalks-browser-unbeatable-yet-not-enough/)

生成摘要时出错

---

## 74. Claude's Cycles [pdf]

**原文标题**: Claude's Cycles [pdf]

**原文链接**: [https://www-cs-faculty.stanford.edu/~knuth/papers/claude-cycles.pdf](https://www-cs-faculty.stanford.edu/~knuth/papers/claude-cycles.pdf)

生成摘要时出错

---

## 75. Parsync, a tool for parallel SSH transfers – 7x faster than rsync

**原文标题**: Parsync, a tool for parallel SSH transfers – 7x faster than rsync

**原文链接**: [https://github.com/AlpinDale/parsync](https://github.com/AlpinDale/parsync)

生成摘要时出错

---

## 76. Jails for NetBSD – Kernel Enforced Isolation and Native Resource Control

**原文标题**: Jails for NetBSD – Kernel Enforced Isolation and Native Resource Control

**原文链接**: [https://netbsd-jails.petermann-digital.de/](https://netbsd-jails.petermann-digital.de/)

生成摘要时出错

---

## 77. GLiNER2: Unified Schema-Based Information Extraction

**原文标题**: GLiNER2: Unified Schema-Based Information Extraction

**原文链接**: [https://github.com/fastino-ai/GLiNER2](https://github.com/fastino-ai/GLiNER2)

生成摘要时出错

---

## 78. Shut Up and Take My Money

**原文标题**: Shut Up and Take My Money

**原文链接**: [https://lorendb.dev/posts/shut-up-and-take-my-money/](https://lorendb.dev/posts/shut-up-and-take-my-money/)

生成摘要时出错

---

## 79. Dulce et Decorum Est (1921)

**原文标题**: Dulce et Decorum Est (1921)

**原文链接**: [https://www.poetryfoundation.org/poems/46560/dulce-et-decorum-est](https://www.poetryfoundation.org/poems/46560/dulce-et-decorum-est)

生成摘要时出错

---

## 80. US tech firms pledge at White House to bear costs of energy for datacenters

**原文标题**: US tech firms pledge at White House to bear costs of energy for datacenters

**原文链接**: [https://www.theguardian.com/us-news/2026/mar/04/us-tech-companies-energy-cost-pledge-white-house](https://www.theguardian.com/us-news/2026/mar/04/us-tech-companies-energy-cost-pledge-white-house)

生成摘要时出错

---

## 81. Fast-Servers

**原文标题**: Fast-Servers

**原文链接**: [https://geocar.sdf1.org/fast-servers.html](https://geocar.sdf1.org/fast-servers.html)

生成摘要时出错

---

## 82. Nvidia PersonaPlex 7B on Apple Silicon: Full-Duplex Speech-to-Speech in Swift

**原文标题**: Nvidia PersonaPlex 7B on Apple Silicon: Full-Duplex Speech-to-Speech in Swift

**原文链接**: [https://blog.ivan.digital/nvidia-personaplex-7b-on-apple-silicon-full-duplex-speech-to-speech-in-native-swift-with-mlx-0aa5276f2e23](https://blog.ivan.digital/nvidia-personaplex-7b-on-apple-silicon-full-duplex-speech-to-speech-in-native-swift-with-mlx-0aa5276f2e23)

生成摘要时出错

---

## 83. Arabic document from 17th-cent. rubbish heap confirms semi-legendary Nubian king

**原文标题**: Arabic document from 17th-cent. rubbish heap confirms semi-legendary Nubian king

**原文链接**: [https://phys.org/news/2026-02-arabic-document-17th-century-rubbish.html](https://phys.org/news/2026-02-arabic-document-17th-century-rubbish.html)

生成摘要时出错

---

## 84. Motorola GrapheneOS devices will be bootloader unlockable/relockable

**原文标题**: Motorola GrapheneOS devices will be bootloader unlockable/relockable

**原文链接**: [https://grapheneos.social/@GrapheneOS/116160393783585567](https://grapheneos.social/@GrapheneOS/116160393783585567)

生成摘要时出错

---

## 85. The L in "LLM" Stands for Lying

**原文标题**: The L in "LLM" Stands for Lying

**原文链接**: [https://acko.net/blog/the-l-in-llm-stands-for-lying/](https://acko.net/blog/the-l-in-llm-stands-for-lying/)

生成摘要时出错

---

## 86. Russia is aiding Iran's war effort by providing Intel on US Military targets

**原文标题**: Russia is aiding Iran's war effort by providing Intel on US Military targets

**原文链接**: [https://www.cnn.com/2026/03/06/politics/russia-aiding-iran-targeting](https://www.cnn.com/2026/03/06/politics/russia-aiding-iran-targeting)

生成摘要时出错

---

## 87. The next generations of Bubble Tea, Lip Gloss, and Bubbles are available now

**原文标题**: The next generations of Bubble Tea, Lip Gloss, and Bubbles are available now

**原文链接**: [https://charm.land/blog/v2/](https://charm.land/blog/v2/)

生成摘要时出错

---

## 88. The remaking of Thomas Mann

**原文标题**: The remaking of Thomas Mann

**原文链接**: [https://www.commonwealmagazine.org/thomas-mann-magic-mountain-jensen](https://www.commonwealmagazine.org/thomas-mann-magic-mountain-jensen)

生成摘要时出错

---

## 89. OpenBSD on SGI: A Rollercoaster Story

**原文标题**: OpenBSD on SGI: A Rollercoaster Story

**原文链接**: [http://miod.online.fr/software/openbsd/stories/sgiall.html](http://miod.online.fr/software/openbsd/stories/sgiall.html)

生成摘要时出错

---

## 90. Relicensing with AI-Assisted Rewrite

**原文标题**: Relicensing with AI-Assisted Rewrite

**原文链接**: [https://tuananh.net/2026/03/05/relicensing-with-ai-assisted-rewrite/](https://tuananh.net/2026/03/05/relicensing-with-ai-assisted-rewrite/)

生成摘要时出错

---

## 91. Building a new Flash

**原文标题**: Building a new Flash

**原文链接**: [https://bill.newgrounds.com/news/post/1607118](https://bill.newgrounds.com/news/post/1607118)

生成摘要时出错

---

## 92. Seventeen Years of Coding and Starting Over

**原文标题**: Seventeen Years of Coding and Starting Over

**原文链接**: [https://www.sunilshenoy.com/2026/03/05/seventeen-years-of-coding-and.html](https://www.sunilshenoy.com/2026/03/05/seventeen-years-of-coding-and.html)

生成摘要时出错

---

## 93. Billy bookshelves as a retro motherboard "rack"

**原文标题**: Billy bookshelves as a retro motherboard "rack"

**原文链接**: [https://rubenerd.com/billy-bookcase-as-a-retro-motherboard-rack/](https://rubenerd.com/billy-bookcase-as-a-retro-motherboard-rack/)

生成摘要时出错

---

## 94. Eating some produce increases pesticide levels in people

**原文标题**: Eating some produce increases pesticide levels in people

**原文链接**: [https://www.ewg.org/news-insights/news-release/2025/09/new-peer-reviewed-ewg-study-finds-eating-some-produce-increases](https://www.ewg.org/news-insights/news-release/2025/09/new-peer-reviewed-ewg-study-finds-eating-some-produce-increases)

生成摘要时出错

---

## 95. Mozilla is working on a big Firefox redesign, here is what it looks like

**原文标题**: Mozilla is working on a big Firefox redesign, here is what it looks like

**原文链接**: [https://www.neowin.net/news/mozilla-is-working-on-a-big-firefox-redesign-here-is-what-it-looks-like/](https://www.neowin.net/news/mozilla-is-working-on-a-big-firefox-redesign-here-is-what-it-looks-like/)

生成摘要时出错

---

## 96. World-first gigabit laser link between aircraft and geostationary satellite

**原文标题**: World-first gigabit laser link between aircraft and geostationary satellite

**原文链接**: [https://www.esa.int/Applications/Connectivity_and_Secure_Communications/World-first_gigabit-per-second_laser_link_between_aircraft_and_geostationary_satellite](https://www.esa.int/Applications/Connectivity_and_Secure_Communications/World-first_gigabit-per-second_laser_link_between_aircraft_and_geostationary_satellite)

生成摘要时出错

---

## 97. Climate change is speeding up

**原文标题**: Climate change is speeding up

**原文链接**: [https://www.nature.com/articles/d41586-026-00745-z](https://www.nature.com/articles/d41586-026-00745-z)

生成摘要时出错

---

## 98. A CPU that runs entirely on GPU

**原文标题**: A CPU that runs entirely on GPU

**原文链接**: [https://github.com/robertcprice/nCPU](https://github.com/robertcprice/nCPU)

生成摘要时出错

---

## 99. MyFirst Kids Watch Hacked. Access to Camera and Microphone

**原文标题**: MyFirst Kids Watch Hacked. Access to Camera and Microphone

**原文链接**: [https://www.kth.se/en/om/nyheter/centrala-nyheter/kth-studenten-hackade-klocka-for-barn-1.1461249](https://www.kth.se/en/om/nyheter/centrala-nyheter/kth-studenten-hackade-klocka-for-barn-1.1461249)

生成摘要时出错

---

## 100. Weight-loss jab could be made for $3 a month, study finds

**原文标题**: Weight-loss jab could be made for $3 a month, study finds

**原文链接**: [https://www.theguardian.com/global-development/2026/mar/06/generic-drugs-weight-loss-semaglutide-ozempic-wegovy-diabetes-obesity-study](https://www.theguardian.com/global-development/2026/mar/06/generic-drugs-weight-loss-semaglutide-ozempic-wegovy-diabetes-obesity-study)

生成摘要时出错

---

