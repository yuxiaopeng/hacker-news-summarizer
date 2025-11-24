# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-11-24.md)

*最后自动更新时间: 2025-11-24 17:51:27*
## 1. SHA1-Hulud二度降临 – Postman、Zapier、PostHog全部因NPM遭入侵

**原文标题**: SHA1-Hulud the Second Comming – Postman, Zapier, PostHog All Compromised via NPM

**原文链接**: [https://www.aikido.dev/blog/shai-hulud-strikes-again-hitting-zapier-ensdomains](https://www.aikido.dev/blog/shai-hulud-strikes-again-hitting-zapier-ensdomains)

2025年11月24日，针对npm软件包的沙丘蠕虫供应链攻击第二波，代号“第二次降临”，被检测到。 这次攻击恰逢npm撤销经典令牌的最后期限之前，导致492个软件包被入侵，总计每月下载量达1.32亿次，其中包括属于Postman、Zapier、ENS、AsyncAPI和PostHog的软件包。

沙丘蠕虫是一种自我复制的npm蠕虫，会感染开发人员环境，使用TruffleHog搜索暴露的密钥（如API密钥和令牌），将其发布到公共GitHub存储库，并在npm生态系统中传播自身。

第二波攻击与第一波攻击有几处不同：它安装bun并使用它来执行恶意代码，为窃取的数据创建随机命名的存储库，并感染多达100个npm软件包（之前为20个）。如果它无法通过GitHub或NPM进行身份验证，它会擦除用户主目录中的所有文件。该恶意软件还会使用以下存储库描述将密钥发布到GitHub：“Sha1-Hulud: The Second Coming”。目前，已暴露2.63万个存储库。

文章还指出，某些受感染的软件包仅包含初始暂存代码，表明感染已在社区传播。

---

## 2. 美国国家安全局与互联网工程任务组，第三部分：回避当前问题

**原文标题**: NSA and IETF, part 3: Dodging the issues at hand

**原文链接**: [https://blog.cr.yp.to/20251123-dodging.html](https://blog.cr.yp.to/20251123-dodging.html)

这篇cr.yp.to博客文章，是题为“NSA和IETF”系列文章的第三篇，详细描述了互联网工程任务组（IETF）内部在标准化由NSA推动的后量子密码（PQ密码）文档过程中，据称存在的程序违规和阻挠行为。

作者认为，IETF的TLS工作组主席不当宣布就采纳一份“非混合”PQ密码文档（不带ECC的PQ）达成“共识”，尽管在采纳讨论中存在重大反对意见。作者强调，主席们声称达成共识，但只有20人明确表示支持，而7人明确表示反对。

该博客文章指责一位IETF“安全领域主管”回避核心问题，并宣传虚假的“明确共识”来推动该文档。当作者对采纳决定提出申诉时，该领域主管最初找借口不处理申诉，后来处理了申诉，确认该文档的采纳达到了“大致共识”。

作者批评该领域主管没有处理最初关于“共识”的说法，而是转为较弱的“大致共识”，并且未能按照法律对标准制定组织的要求，清晰地定义和应用“大致共识”一词。作者认为，对申诉的处理构成了违反正当程序，并暗示IESG内部存在协同努力，为该文档的“最后征求意见稿”提供掩护。

---

## 3. 法国威胁 GrapheneOS，若拒不提供后门将逮捕相关人员/查封服务器。

**原文标题**: France threatens GrapheneOS with arrests / server seizure for refusing backdoors

**原文链接**: [https://grapheneos.social/@watchfulcitizen@goingdark.social/115605398547420414](https://grapheneos.social/@watchfulcitizen@goingdark.social/115605398547420414)

根据标题和GrapheneOS Mastodon提供的链接文本，文章声称法国政府威胁GrapheneOS，如果他们拒绝在其操作系统中植入后门，将逮捕相关人员并没收服务器。

Mastodon链接表明用户正被引导离开GrapheneOS官方Mastodon服务器，前往另一个服务器上的帖子。 这暗示信息来源于外部，并由一个名为“watchfulcitizen”的用户分享。

在未访问链接的Mastodon帖子的情况下，无法验证标题中的说法。 然而，核心指控是法国政府正试图强迫GrapheneOS（一个注重隐私和安全的操作系统）通过创建后门来损害其安全性，并威胁采取法律行动来实现这一目标。

---

## 4. 法国威胁 GrapheneOS，若拒绝后门将逮捕相关人员/查封服务器

**原文标题**: France threatens GrapheneOS with arrests / server seizure for refusing backdoors

**原文链接**: [https://mamot.fr/@LaQuadrature/115581775965025042](https://mamot.fr/@LaQuadrature/115581775965025042)

一篇来自 La Quadrature du Net 在 Mastodon 上的帖子，引用了《巴黎人报》发表的两篇文章，声称法国威胁 GrapheneOS，若拒绝植入后门，将对其进行逮捕并没收服务器。

这是一个严重的指控，暗示法国政府试图胁迫注重隐私的安卓操作系统 GrapheneOS 的开发者，以损害他们软件的安全性。GrapheneOS 拒绝创建后门，从而坚持了其对用户隐私和安全的承诺，因为后门可能被恶意行为者利用。

该 Mastodon 帖子指出了情况的紧迫性和潜在严重性，暗示法国政府的行动可能对隐私和安全倡导者产生深远的影响。如果属实，这将代表着在关于加密和政府访问用户数据这一持续争论中，事态的显著升级。

---

## 5. Rust 标准库和 parking_lot 互斥锁对比：谁更胜一筹？

**原文标题**: Inside Rust's std and parking_lot mutexes – who wins?

**原文链接**: [https://blog.cuongle.dev/p/inside-rusts-std-and-parking-lot-mutexes-who-win](https://blog.cuongle.dev/p/inside-rusts-std-and-parking-lot-mutexes-who-win)

Rust中`std::sync::Mutex`和`parking_lot::Mutex`的性能比较

---

## 6. Chrome Jpegxl 问题重新开启

**原文标题**: Chrome Jpegxl Issue Reopened

**原文链接**: [https://issues.chromium.org/issues/40168998](https://issues.chromium.org/issues/40168998)

Chrome Jpegxl 议题重启：简述及潜在影响

---

## 7. Show HN: Cynthia – 可靠播放 MIDI 音乐文件 – MIT 许可 / 便携 / Windows

**原文标题**: Show HN: Cynthia – Reliably play MIDI music files – MIT / Portable / Windows

**原文链接**: [https://www.blaizenterprises.com/cynthia.html](https://www.blaizenterprises.com/cynthia.html)

Cynthia是一款可靠的MIDI音乐文件播放器，它是一个便携式Windows应用程序。它支持格式0和1的“.mid”、“.midi”和“.rmi”格式，并具有诸如实时调整播放速度、音量和输出设备等功能。它包含25个MIDI示例，并支持“.m3u”播放列表。

主要功能包括双播放系统（文件夹和列表）、时间读数、设备状态、播放列表支持（复制、粘贴、打开、保存、构建）、拖放功能、多种播放模式（一次、单曲循环、全部循环、全部一次、随机）、速度控制（标准50%-200%，扩展10%-1000%）、前奏模式、快退/快进选项、自动淡入和播放进度条。

它还提供带增强的音量控制、“混音器”链接到Windows音量合成器、滚动歌词、详细的MIDI信息、带有静音选项的音轨和通道面板、独立通道音量混音器、音符面板、带有可定制按键照明的钢琴面板、音量条和移调选项。包含Xbox控制器支持，用于控制播放和导航。

该应用程序允许在最多10个MIDI播放设备之间切换，并具有诸如时间偏移和设备音量等多设备选项。它具有自动MIDI设备重新同步、自定义播放引擎、自动紧凑模式和可自定义的外观选项。

Cynthia以MIT许可证提供。本文还为首次用户提供了使用说明，解释了工具栏功能、如何从文件夹和播放列表播放，以及各种选项和设置的详细说明。

---

## 8. 英国是最富有的国家之一，为何还有儿童生活在贫困之中？

**原文标题**: Britain is one of the richest countries. So why do children live in poverty?

**原文链接**: [https://www.cnn.com/2025/11/24/uk/britain-child-poverty-intl-scli](https://www.cnn.com/2025/11/24/uk/britain-child-poverty-intl-scli)

英国儿童贫困问题日益严峻：一个富裕国家的困境

尽管英国是一个富裕国家，但令人担忧的是，儿童贫困现象日益严重。 惊人的是，有三分之一的英国儿童（450万）生活在相对贫困中，其中一百万人生活困苦，缺乏温暖、食物和衣物等基本必需品。

本文重点介绍了苦苦挣扎的家庭的个人故事，包括一位全职工作的母亲仍然依靠婴儿银行来获取必需品。 即使对于工作的家庭来说，高昂的生活成本，特别是住房和托儿费用，也对这个问题造成了重大影响。 英国的托儿费用是发达国家中最高的。

本文将贫困率上升归因于经济增长缓慢、顽固的通货膨胀以及2008年金融危机后实施的政府紧缩政策。诸如福利上限和两孩福利限制等关键政策被认为是导致儿童贫困加剧的主要因素，尤其对大家庭产生了影响。

本文指出，黑人和亚裔儿童受到的影响尤为严重，存在着明显的社会不平等现象。 虽然现任工党政府表示关注并采取了一些措施，但它面临着平衡社会优先事项与有限资金以及反对增税承诺的挑战。 倡导者认为，社会保障体系不足，“安全网”几乎消失，导致家庭没有任何财务弹性。

---

## 9. Serflings是《工人物语1》的重制版

**原文标题**: Serflings is a remake of The Settlers 1

**原文链接**: [https://www.simpleguide.net/serflings.xhtml](https://www.simpleguide.net/serflings.xhtml)

《农奴》是对经典策略游戏《工人物语1》（也称《农奴之城》）的重制。目标是在重现原汁原味体验的同时，添加更高分辨率和网络多人游戏等现代功能。

要游玩，你需要来自原版《工人物语1》游戏的数据文件（SPAE.PA、SPAD.PA 或 SPAF.PA）。该重制版支持 DOS 版本和“历史典藏版”的文件。游戏将在当前目录、“data”子目录或 Windows 上的默认“历史典藏版”安装路径中搜索这些文件。

本文提供了《农奴》稳定版和开发版的下载链接，包括带有和不带有集成 Java 运行时环境的版本。如果选择不带 Java 的版本，你需要安装 Java 17。升级版本之前，建议删除之前安装的“jre”和“lib”文件夹。

该重制版拥有许多原始功能，包括训练、任务、AI、保存/加载功能、地图功能和统计菜单。它包含德语、英语、法语和波兰语等语言。新增功能包括平滑滚动、缩放、寻路预览、网络游戏和工作半径指示器。

目前该重制版缺少的功能包括替换现有建筑物、菜单/建筑物的计时器、建造路径时滚动以及工具提示。计划支持最多四名玩家的多人游戏和更多语言。

本文还列出了游戏的控制方式和命令行参数。你可以从原版游戏中复制保存的游戏文件，以继续玩你之前的存档。

---

## 10. 沙丘蠕虫归来：超过 300 个 NPM 包被感染

**原文标题**: Shai-Hulud Returns: Over 300 NPM Packages Infected

**原文链接**: [https://helixguard.ai/blog/malicious-sha1hulud-2025-11-24](https://helixguard.ai/blog/malicious-sha1hulud-2025-11-24)

螺旋卫士（HelixGuard）是一个开源安全研究小组，他们发现了一次广泛的感染，影响了超过300个NPM软件包。这次恶意活动被称为“沙丘之虫归来”，表明这是一次复杂且可能持续很久的攻击，目标是开发者及其项目。

攻击途径涉及包含恶意代码的受损NPM软件包。一旦安装，这些代码很可能试图窃取敏感信息、注入更多恶意软件，或以其他方式危害受影响的系统。超过300个受感染软件包的巨大规模表明软件供应链面临重大风险。

虽然恶意活动的具体性质和攻击者的动机仍在调查中，“沙丘之虫归来”活动突显了NPM生态系统持续存在的供应链攻击漏洞。 敦促开发者保持警惕，仔细检查其依赖项，并利用安全工具来检测和减轻来自受损软件包的潜在威胁。 有关涉及的特定软件包和潜在的缓解策略的更多详细信息可能来自螺旋卫士（HelixGuard）的研究。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 2 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 3 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 4 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 5 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 6 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 7 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 8 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 9 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 10 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 11 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 12 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 13 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 14 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 15 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 16 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 17 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 18 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 19 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 20 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 21 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 22 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 23 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 24 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 25 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 26 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 27 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 28 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 29 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 30 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 31 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 32 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 33 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 34 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 35 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 36 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 37 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 38 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 39 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 40 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 41 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 42 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 43 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 44 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 45 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 46 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 47 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 48 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 49 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 50 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 51 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 52 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 53 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 54 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 55 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 56 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 57 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 58 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 59 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 60 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 61 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 62 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 63 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 64 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 65 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 66 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 67 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 68 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 69 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 70 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 71 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 72 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 73 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 74 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 75 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 76 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 77 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 78 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 79 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 80 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 81 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 82 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 83 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 84 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 85 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 86 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 87 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 88 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 89 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 90 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 91 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 92 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 93 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 94 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 95 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 96 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 97 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 98 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 99 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 100 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 101 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 102 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 103 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 104 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 105 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 106 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 107 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 108 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 109 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 110 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 111 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 112 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 113 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 114 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 115 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 116 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 117 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 118 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 119 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 120 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 121 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 122 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 123 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 124 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 125 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 126 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 127 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 128 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 129 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 130 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 131 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 132 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 133 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 134 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 135 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 136 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 137 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 138 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 139 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 140 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 141 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 142 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 143 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 144 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 145 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 146 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 147 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 148 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 149 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 150 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 151 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 152 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 153 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 154 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 155 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 156 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 157 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 158 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 159 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 160 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 161 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 162 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 163 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 164 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 165 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 166 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 167 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 168 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 169 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 170 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 171 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 172 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 173 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 174 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 175 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 176 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 177 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 178 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 179 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 180 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 181 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 182 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 183 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 184 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 185 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 186 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 187 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 188 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 189 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 190 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 191 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 192 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 193 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 194 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 195 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 196 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 197 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 198 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 199 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 200 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 201 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 202 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 203 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 204 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 205 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 206 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 207 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 208 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 209 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 210 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 211 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 212 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 213 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 214 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 215 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 216 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 217 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 218 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 219 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 220 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 221 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 222 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 223 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 224 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 225 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 226 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 227 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 228 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 229 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 230 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 231 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 232 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 233 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 234 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 235 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 236 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 237 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 238 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 239 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 240 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 241 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 242 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 243 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 244 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 245 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 246 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 247 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 248 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 249 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
