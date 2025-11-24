# Hacker News 热门文章摘要 (2025-11-24)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 我们暂停了路线图工作一周，并修复了漏洞。

**原文标题**: We stopped roadmap work for a week and fixed bugs

**原文链接**: [https://lalitm.com/fixits-are-good-for-the-soul/](https://lalitm.com/fixits-are-good-for-the-soul/)

本文详细介绍了作者参与“修复周”的经验。“修复周”是一项季度性活动，他们约45人的软件工程团队会暂停所有路线图工作，专注于修复小缺陷、可用性问题以及提高开发者生产力。规则很简单：缺陷修复时间不得超过两天，重点应放在最终用户体验改进或开发者效率提升上。积分系统和带有T恤奖励的排行榜增加了一种游戏化的元素。

作者强调了最近一次修复周的实际成果，包括修复了189个缺陷，平均每人修复4个缺陷。具体例子包括实现了一个存在了四年的功能需求，自动化了UI团队的工作流程，并创建了一个新的SDK版本。

作者强调了修复周的多重好处：通过解决经常被忽视的细节，提高产品的完善度和用户满意度；通过专注于即时改进，重新燃起工程师的成就感；以及通过协作解决问题和分享成功，提高团队士气。

成功举办修复周的关键要素包括：细致的准备工作（缺陷标记和优先级排序）、严格的两天时间限制以防止范围蔓延、产生能量的关键参与人数，以及小心处理游戏化以避免绩效驱动行为。人工智能工具被认为可以显著提高开发者在修复周期间的效率。作者还讨论了关于暂停路线图工作的批评，并倡导将该概念应用于较小的团队。最终，修复周对于提高产品质量、开发者生产力以及培养工匠精神非常有价值。

---

## 12. 切片即一切：迈向通用的单边分布式矩阵乘法

**原文标题**: Slicing Is All You Need: Towards a Universal One-Sided Distributed MatMul

**原文链接**: [https://arxiv.org/abs/2510.08874](https://arxiv.org/abs/2510.08874)

本文提出了一种新颖的通用单边分布式矩阵乘法算法，旨在解决现有算法针对特定数据分区的局限性。该算法名为“切片即万能”，通过支持所有分区和复制因子的组合，克服了对多种算法实现和代价高昂的数据重分布的需求。

其核心创新在于使用“切片”（索引算术）来确定局部矩阵乘法所需的重叠块。这种方法使算法能够适应任何分区方案。这些局部乘法可以直接执行，或者通过重新排序和降级到中间表示（IR）来优化，以最大限度地提高重叠和性能。

该算法使用基于高级C++的PGAS框架实现，并利用节点内互连的直接GPU到GPU通信来提高效率。作者展示了该算法在各种分区和复制因子下，与高度优化的分布式张量库PyTorch DTensor的竞争力。这表明这种“通用”算法有潜力简化和增强各种科学、数据分析和AI工作负载中的分布式矩阵乘法。

---

## 13. RuBee

**原文标题**: RuBee

**原文链接**: [https://computer.rip/2025-11-22-RuBee.html](https://computer.rip/2025-11-22-RuBee.html)

本文探讨了由Visible Assets Inc.(VAI)开发的鲜为人知的个人区域网络协议RuBee，及其在武器追踪中出人意料的利基应用。VAI由John K. Stevens创立，最初旨在解决医疗保健物流中的冷藏挑战。然而，RuBee的独特特性，特别是其使用低频磁场进行通信，使其非常适合在具有挑战性的环境中跟踪资产。

与RFID不同，RuBee在131 kHz的近场中运行，通信范围可达30米，并且更能抵抗金属或水的屏蔽。这种稳健性对于跟踪存储在金属容器中、金属货架上或靠近人体携带的枪支至关重要。RuBee标签可以直接嵌入到枪支中，并整合诸如基于加速计的子弹计数等功能。

尽管RuBee具有智能枪支应用的潜力，但由于围绕枪支管制的政治敏感性，VAI有策略地避免强调这些能力。相反，他们专注于维护跟踪和防盗。RuBee受到军事和安全部队等机构用户的欢迎，并获得了军方批准直接附加到军械上。值得注意的是，海军水面作战中心于2010年选择了RuBee用于步枪标记。然而，RuBee最重要的市场是原子能设施的保护部队，这主要是因为严格的会计要求和严格的研发标准。橡树岭国家实验室在21世纪中期评估了RuBee在其军械库中进行枪支标记的应用，进一步巩固了其在该利基市场的地位。

---

## 14. 迪士尼失去了谁陷害了兔子罗杰

**原文标题**: Disney Lost Roger Rabbit

**原文链接**: [https://pluralistic.net/2025/11/18/im-not-bad/](https://pluralistic.net/2025/11/18/im-not-bad/)

本文主要探讨版权法中的“著作权转让终止权”概念，强调其对创意工作者的重要性。作者Cory Doctorow解释了1976年《版权法》中的这一条款如何允许创作者在35年后收回其版权许可，从而解决创作者与大型媒体公司之间的权力失衡问题。他认为，版权扩张往往更有利于媒体集团，而非个体艺术家，因为公司可以决定条款并攫取新的权利。

Doctorow引用了《谁审查了兔子罗杰》的作者Gary K Wolf的例子，他成功终止了向迪士尼转让的版权，重新获得了对其角色的权利。这使他能够探索新的项目，比如由杰西卡兔子主演的续集。

本文还涉及媒体公司削弱或消除著作权转让终止权的历史尝试，特别是音乐家权利几乎被一项偷偷加入立法的修正案取消的情况。Doctorow强调，终止权是创作者重新谈判交易和解决过去不公正现象的宝贵工具，他引用了斯蒂芬·金、安·M·马丁和放克传奇人物乔治·克林顿的案例。他向读者推荐了来自知识共享组织和作家联盟的资源，以帮助他们行使自己的权利。

除了兔子罗杰案例和著作权转让终止权之外，本文还包括作者认为有趣的其他文章的链接集合，以及作者即将进行的演讲活动列表。

---

## 15. AV Pro Designs 的历史还原机场模型

**原文标题**: Historically Accurate Airport Dioramas by AV Pro Designs

**原文链接**: [https://www.core77.com/posts/138995/Historically-Accurate-Airport-Dioramas-by-AV-Pro-Designs](https://www.core77.com/posts/138995/Historically-Accurate-Airport-Dioramas-by-AV-Pro-Designs)

这篇Core77文章重点介绍了AV Pro Designs，这家公司由退休的航空公司飞行员兼高管Brian Keene创立，专门制作具有历史精确性的机场透视模型。Keene痴迷于机场，利用他的经验和档案照片，以1:400的比例精心重建特定时代的著名机场。

这些透视模型被出售给博物馆、机构和透视模型爱好者，其中包括肯尼迪机场（20世纪70-80年代）、洛杉矶国际机场（20世纪80-90年代）以及孟买机场令人惊叹的夜景。AV Pro Designs还制作了希思罗机场和纽瓦克机场的模型，香港启德机场和法国戴高乐机场正在开发中。

文章包含了读者Roger ak的评论，他澄清说“透视模型社区”指的是那些制作、收集和欣赏透视模型的人，并以马尔科姆·福布斯的大量收藏为例。他还指出正确的比例是1:400，而不是1:1400。

---

## 16. 日本豪赌将北海道打造成全球芯片中心

**原文标题**: Japan's gamble to turn island of Hokkaido into global chip hub

**原文链接**: [https://www.bbc.com/news/articles/c8676qpxgnqo](https://www.bbc.com/news/articles/c8676qpxgnqo)

日本押重注振兴半导体产业，欲将北海道打造为“北海道硅谷”。核心是政府支持的Rapidus公司，斥资120亿美元在千岁市建设尖端芯片代工厂。Rapidus与IBM合作取得突破，成功生产2纳米芯片原型，跻身台积电和三星等行业巨头之列。

尽管取得了进展，挑战依然存在。资金可能不足以支持大规模生产，且Rapidus缺乏制造经验。由于台积电和三星已建立稳固的客户关系，争取客户也可能面临困难。

然而，政府致力于大力投资芯片产业和人工智能。此举旨在扭转日本半导体产业自20世纪80年代达到顶峰后的衰落，并通过与大学的合作以及对外国人才的依赖来解决工程师短缺问题。

该计划包括通过吸引全球企业来建立一个生态系统。台积电在九州的扩张，以及铠侠、东芝、美光和三星的投资，都显示出了希望。Rapidus计划通过比竞争对手更快地生产定制芯片来脱颖而出，以满足人工智能驱动的日益增长的全球需求以及对可靠的国内供应链的需求。这场豪赌被视为对国家安全和经济复苏至关重要，旨在恢复日本的技术实力并确保其在全球市场中的地位。

---

## 17. Rust编写的快速Lua运行时

**原文标题**: Fast Lua runtime written in Rust

**原文链接**: [https://astra.arkforge.net/](https://astra.arkforge.net/)

Astra：基于 Rust 的高性能 Lua 运行时，专为速度、容错性和易用性而设计。它利用 Rust 的零成本抽象能力，提供异步、多线程的运行时环境。与传统实现相比，这带来了明显更快的 Lua 环境。

Astra 拥有与 Lua 脚本的无缝集成，允许开发者利用现有的 Lua 代码。其模块化设计具有容错性且易于扩展，使其适用于不断增长的应用程序。它以包含所有必要组件的单个二进制文件形式提供，并且可以作为常规 Lua 运行时运行，从而简化了部署和使用。

示例代码演示了如何使用 Astra 创建一个简单的 HTTP 服务器。它展示了路由注册（包括 GET 请求）、访问请求正文、设置响应状态代码和标头以及返回 JSON 响应。该示例突出了开发者使用 Astra 的 Lua 集成创建和管理 Web 服务器的便利性。本质上，Astra 通过将 Rust 的优势与 Lua 的简洁性相结合，为运行 Lua 代码（尤其是在服务器端应用程序中）提供了一个强大而高效的平台。

---

## 18. µcad：可生成2D草图和3D模型的新开源编程语言

**原文标题**: µcad: New open source programming language that can generate 2D sketches and 3D

**原文链接**: [https://microcad.xyz/](https://microcad.xyz/)

µcad：一款用于生成2D草图和3D对象的新型开源编程语言。该项目尚处于早期阶段，但正在积极开发，每周都会添加新功能，开发者旨在通过博客让用户了解其进展。

最近的更新通过诸如（由五个部分组成的）螺线仪和通过实时编码视频生成乐高积木和齿轮的演示等示例，展示了该语言的功能。 这些示例可供下载（代码）和3D打印（打印），并与最新更新一起发布。 最初的版本，Alpha Release 0.2.14，以错误修复和故障排除为标志。 开发者正在积极致力于提高语言的稳定性和功能。

---

## 19. Lambda演算 – Lambda图的Beta归约动画演示

**原文标题**: Lambda Calculus – Animated Beta Reduction of Lambda Diagrams

**原文链接**: [https://cruzgodar.com/applets/lambda-calculus](https://cruzgodar.com/applets/lambda-calculus)

本文似乎是一个通过交互式Lambda图可视化和理解Lambda演算的资源。它特别使用JavaScript来动画演示β归约，这是Lambda演算中的一个核心操作。本文旨在通过提供归约过程的动态和可视化表示，帮助用户了解Lambda演算的工作原理。重点是通过观察Lambda图中发生的转换来理解β归约。

---

## 20. Rust性能指南 (2020)

**原文标题**: The Rust Performance Book (2020)

**原文链接**: [https://nnethercote.github.io/perf-book/](https://nnethercote.github.io/perf-book/)

《Rust性能指南》，由尼古拉斯·内瑟科特主要撰写并由他人贡献，于2020年11月出版，是一本专注于优化Rust代码性能的资源。该书指导Rust开发者识别和解决应用程序中的性能瓶颈。尽管提供的摘录很少，但标题和介绍信息清楚地表明了该书的目的。

根据标题和作者推断，本书的主要内容可能包括：

*   **性能分析:** 用于识别 Rust 代码中慢速部分的技术，可能涉及分析器和基准测试框架等工具。
*   **内存管理优化:** 用于有效分配和释放内存以最大限度地减少开销并防止内存泄漏的策略。
*   **数据结构和算法:** 关于为特定性能要求选择合适的数据结构和算法的建议。
*   **并发与并行:** 利用多线程和并行来提高应用程序速度的方法。
*   **编译器优化:** 了解 Rust 编译器如何优化代码以及如何编写可以从这些优化中受益的代码。
*   **最佳实践:** 在 Rust 应用程序中实现更好性能的通用编码实践。

"Source code" 一行表明可以获得随附的代码示例，以说明书中讨论的概念。本质上，《Rust性能指南》旨在为开发人员提供编写高性能 Rust 应用程序所需的知识和工具。

---

## 21. 我用Rust构建了一个更快的Notion。

**原文标题**: I built an faster Notion in Rust

**原文链接**: [https://imedadel.com/outcrop/](https://imedadel.com/outcrop/)

Imed用Rust构建了Outcrop，这是一个比Notion/Confluence更快更简单的知识库替代方案，此前尝试使用Go未能成功。由于对现有解决方案不满意，他专注于速度、简洁性和实时协作。

主要改进包括：

*   **速度和简洁性：** 旨在提供比现有平台更快、更易于使用的知识库。
*   **基于Rust的架构：** 用Rust重写项目带来了更高效的代码，并可以访问强大的crate进行宏生成和工具构建。
*   **自定义授权系统：** 实现了轻量级的、受Zanzibar启发的授权系统（持久化到Postgres），用于高效的权限检查。
*   **Elastic Search：** 集成了一个快速的、使用tantivy和语言检测构建的自定义搜索引擎，并结合了授权机制，仅索引可访问的资源。
*   **基于Rust的ProseMirror：** 将ProseMirror移植到Rust，以实现更快的文档编辑、实时协作，并能够更轻松地提取内容，以及实现诸如Tab补全和结构化建议等高级功能的潜力。
*   **现代前端：** 利用Solid.js构建了性能更强的用户界面，并与ProseMirror集成。

Imed设想Outcrop是一种超越简单文本的工具，可以集成图表、绘图，甚至可能是电子表格。他还计划将其与任务管理工具连接，并利用语言模型来改进工作流程。Outcrop计划在六个月内发布，并提供早期访问注册和赞助机会。

---

## 22. Show HN: Docker Compose 中的虚拟 SLURM HPC 集群

**原文标题**: Show HN: Virtual SLURM HPC cluster in a Docker Compose

**原文链接**: [https://github.com/exactlab/vhpc](https://github.com/exactlab/vhpc)

本文介绍vHPC，一个基于Docker的虚拟HPC集群，使用SLURM和OpenMPI，专为学习和测试HPC环境而设计。它允许用户在单台机器上模拟一个生产就绪的多容器HPC设置。

主要特性包括MPI支持（节点内和节点间）、头节点和工作节点之间的用户同步、共享SLURM配置，以及通过MariaDB实现可选的完整作业记账。

本文提供了一个使用`docker compose up -d`的快速入门指南，以及通过SSH（使用生成的SSH密钥或密码身份验证）访问集群节点的说明。它还包括用于作业提交、队列查看和记账的示例SLURM命令。

用户可以通过使用`packages.yml`文件（适用于Python、RPM和任意命令）安装额外的软件包来定制集群，并通过修改`./slurm-config/`目录中的文件来覆盖默认的SLURM配置。文章还说明了如何添加更多工作节点。

技术细节涵盖了集群架构（头节点、工作节点、可选数据库节点）、MPI传输配置以及用于用户同步、作业数据和SLURM配置的共享卷。文章强调，由于默认密码和启用的SSH root登录，该项目仅用于教育目的，不适用于生产。它包括所用软件的版本信息（Rocky Linux 9、SLURM 22.05.9、OpenMPI 4.1.1、MariaDB 10.9）、故障排除技巧，并以MIT许可证授权。

---

## 23. 法拉第效应中发现新的磁性成分

**原文标题**: New magnetic component discovered in the Faraday effect

**原文链接**: [https://phys.org/news/2025-11-magnetic-component-faraday-effect-centuries.html](https://phys.org/news/2025-11-magnetic-component-faraday-effect-centuries.html)

无法访问文章链接。

---

## 24. Show HN: 用数千个不可见的Unicode字符让LLM崩溃

**原文标题**: Show HN: Stun LLMs with thousands of invisible Unicode characters

**原文链接**: [https://gibberifier.com](https://gibberifier.com)

Gibberifier：一种通过在文本字符间插入不可见的零宽度Unicode字符来混淆大型语言模型(LLM)的工具。此举不影响人类阅读，但会大幅增加文本长度，并导致许多AI模型混淆或崩溃。

建议对关键文本部分（如500字以内的论文提示）使用此工具，以干扰AI抄袭检测、文本抓取，甚至像Flint AI这样的评分系统。目标是浪费AI的处理token并触发速率限制。

该工具已针对多个知名AI模型进行测试，结果如下：

*   **ChatGPT:** 混淆或忽略混淆文本。
*   **Claude & Meta AI:** 遇到混淆文本时崩溃或出错。
*   **Gemini:** 无法处理不可见字符。
*   **Grok & Perplexity AI:** 困惑并产生乱码或不完整的响应。

Gibberifier提供诸如反抄袭、混淆LLM抓取工具的文本以及干扰AI驱动工具的方法，同时保持人类可读性。该工具的源代码可在GitHub上获取。

---

## 25. 构建已知最大的 Kubernetes 集群，拥有 13 万个节点

**原文标题**: Building the largest known Kubernetes cluster, with 130k nodes

**原文链接**: [https://cloud.google.com/blog/products/containers-kubernetes/how-we-built-a-130000-node-gke-cluster/](https://cloud.google.com/blog/products/containers-kubernetes/how-we-built-a-130000-node-gke-cluster/)

2025年11月，谷歌云宣布成功在实验模式下运行了一个拥有13万个节点的 Kubernetes 集群，使其 GKE 的官方支持上限翻倍。 此次扩展不仅增加了节点数量，还提高了 Pod 创建和调度吞吐量，维持每秒 1000 个 Pod 的速度，并在分布式存储中管理超过 100 万个对象。

对如此大规模集群的需求源于高要求的 AI 工作负载，已有客户在运行 2 万到 6.5 万个节点的集群。 实现此规模的关键架构创新包括通过缓存一致性读取和可快照 API 服务器缓存功能优化读取可扩展性，以及基于谷歌 Spanner 的专有分布式存储后端。

文章重点介绍了 Kueue，一种用于高级作业级别管理的作业队列控制器，并讨论了 Kubernetes 中面向工作负载的调度技术的未来。 具有并行下载和区域性 Anywhere Cache 的 GCS FUSE 为 AI 工作负载提供高效的数据访问。

为了验证 GKE 的性能，一个四阶段基准测试模拟了一个包含混合工作负载（低、中和高优先级）的动态 AI 环境。 该基准测试测试了 Pod 启动延迟、调度吞吐量、资源抢占和集群弹性等性能维度。 GKE 展示了其通过抢占较低优先级作业来管理波动需求的能力，实现了高达每秒 1000 个 Pod 的稳定吞吐量。 Kueue 在工作负载优先级排序和动态资源分配方面发挥了关键作用，抢占了大量 Pod 以适应更高优先级的任务。

---

## 26. Fran Sans – 一款受旧金山轻轨显示屏启发的字体

**原文标题**: Fran Sans – font inspired by San Francisco light rail displays

**原文链接**: [https://emilysneddon.com/fran-sans-essay](https://emilysneddon.com/fran-sans-essay)

艾米丽·斯内登创作了“Fran Sans”，这是一款受旧金山Muni Breda轻轨车辆上LCD目的地显示屏启发的展示字体。她被这些字符的机械感和个性化感觉所吸引，这些字符由3x5网格上的几何模块组成，反映了这座城市实用与魅力的独特融合。

斯内登参观了SFMTA的电子商店，向技术员Armando Lumbad了解了Trans-Lite公司于1999年设计的显示屏编码系统。她与高级工程师Gary Wallberg交流，Gary解释了为了效率而创建的字母表，由于其局限性而产生了独特的字符。受此启发，斯内登与Dave Foster合作开发了Fran Sans，其中包括大写字母、数字和核心标点符号。

Fran Sans有三种样式：实心、瓦片和面板。她的设计过程还受到了字体档案馆的影响，她在那里研究了模块化排版，如Joan Trochut的Tipo Veloz和Zuzana Licko的Lo-Res。她旨在她的字体中保留原始显示屏的不完美魅力，并意识到随着Breda车辆的更换，这些显示屏即将被移除。斯内登希望Fran Sans能够激发人们对定义城市和生活特征的不完美之处的欣赏。文章最后是致谢以及一首受旧金山启发的诗歌。

---

## 27. 工作中：自我、共情与谦逊

**原文标题**: Ego, empathy, and humility at work

**原文链接**: [https://matthogg.fyi/a-unified-theory-of-ego-empathy-and-humility-at-work/](https://matthogg.fyi/a-unified-theory-of-ego-empathy-and-humility-at-work/)

Matt Hogg的文章认为，自我是自我意识的必要组成部分，但在职场中，尤其对于开发者和技术领导者而言，可能是有害的。他提出，同理心和谦逊是抵消自我负面影响、培养更具协作性和生产力的环境的关键技能。

Hogg将自我定义为自我辩解的驱动力，它可以体现在细微之处，如过度使用术语、把关和防御性陈述。他强调，不受控制的自我会抵制新信息并阻碍问题解决。

同理心，即理解他人观点的能力，被视为收集新信息的工具，而谦逊，即抵制竞争性反应，则允许信息改变我们的行为。这些并非关于自我牺牲，而是关于有效地与他人合作。

作者强调，解决方案需要尚未掌握的信息，而同理心和谦逊是从同事、用户甚至管理层获取信息的关键。他以泰德·拉索为例，说明无自我领导，提倡好奇心而非评判。

他承认，控制自我是持续不断的努力，即使对于那些看似冷静的人来说也是如此。然而，回报是改善人际关系、增加信任，以及创建一个更好的协作环境，让人们感到有力量并渴望一起工作。文章最后鼓励持续改进，强调即使是微小的改变也能产生重大影响。

---

## 28. 带类型的集合论

**原文标题**: Set theory with types

**原文链接**: [https://lawrencecpaulson.github.io//2025/11/21/Typed_Set_Theory.html](https://lawrencecpaulson.github.io//2025/11/21/Typed_Set_Theory.html)

本文探讨了集合论和类型论在数学中的作用，重点介绍了N.G. de Bruijn的“带类型限制的集合论”这一折衷概念。它对比了传统上对策梅洛-弗兰克尔(ZF)集合论的依赖（即“一切皆为集合”），以及类型论更为结构化的方法（即给数学对象分配类型）。De Bruijn认为，将所有事物强行塞进一个集合是不自然的，并且会导致不必要的复杂性，他更倾向于更接近直觉的类型化集合论。

作者解释了高阶逻辑，特别是Isabelle/HOL中实现的高阶逻辑，如何体现这种方法。集合被视为布尔值函数，实际上是类型化的集合，从而避免了诸如x ∈ x这样的悖论。本文概述了类型化集合论的基本要素，包括类型化的并集、交集、幂集和函数空间。

虽然类型化集合论被认为足以满足大多数数学目的，但本文承认偶尔需要ZF集合论，尤其是在处理超限序数和基数时。文章描述了如何通过假定具有所有ZF公理的ZF集合类型，将ZF纳入高阶逻辑。本文还介绍了世袭有限集（hf）作为一种更简单的替代方案，它足以处理诸如整数、有理数和有限状态机等有限结构。

---

## 29. Cloudflare宕机也许是件好事

**原文标题**: The Cloudflare outage might be a good thing

**原文链接**: [https://gist.github.com/jbreckmckye/32587f2907e473dd06d68b0362fb0048](https://gist.github.com/jbreckmckye/32587f2907e473dd06d68b0362fb0048)

Cloudflare宕机事件：互联网中心化的警示

---

## 30. Show HN: 我用 C 语言写了一个极简内存分配器

**原文标题**: Show HN: I wrote a minimal memory allocator in C

**原文链接**: [https://github.com/t9nzin/memory](https://github.com/t9nzin/memory)

这篇“Show HN”帖子介绍了一个由@t9nzin用C语言编写的极简内存分配器。它使用`sbrk`进行小内存分配，`mmap`进行大内存分配，并结合了块分割和合并以优化内存管理。该分配器明确声明为非线程安全。

帖子提供了构建和使用该分配器库的说明，包括先决条件（GCC、Make、POSIX兼容系统）、构建命令（`make`、`make tests`、`make bench`、`make lib`）以及示例编译命令。

项目结构包括Makefile、README、示例（my_program.c）、包含目录（allocator.h）、源代码目录（allocator.c）和测试（benchmark.c、test_basic.c、test_edge_cases.c）。

重要的局限性包括缺乏线程安全、碎片整理和压缩。该项目采用MIT许可证，欢迎贡献。

作者感谢Dan Luu的malloc()教程作为参考，并感谢Joshua Zhou和Abdul Fatir对随附博客文章的反馈，该文章提供了该分配器开发的逐步解释。

---

## 31. 陶哲轩：在埃尔德什问题网站，人工智能辅助渐成常态

**原文标题**: Terence Tao: At the Erdos problem website, AI assistance now becoming routine

**原文链接**: [https://mathstodon.xyz/@tao/115591487350860999](https://mathstodon.xyz/@tao/115591487350860999)

陶哲轩注意到埃尔德什问题网站上“AI辅助”变得普遍。

---

## 32. 气象局新局长被要求审查9600万美元的网站改版费用

**原文标题**: Bureau of Meteorology's new boss asked to examine $96M bill for website redesign

**原文链接**: [https://www.abc.net.au/news/2025-11-23/bureau-of-meteorology-new-website-cost-blowout-to-96-million/106042202](https://www.abc.net.au/news/2025-11-23/bureau-of-meteorology-new-website-cost-blowout-to-96-million/106042202)

气象局(BOM)因其耗资9650万澳元重新设计的网站而面临审查，这远高于最初声称的410万澳元。网站上线后，公众和利益相关者立即提出了批评，原因在于导航问题以及雷达图的有问题更改，尤其影响了依赖降雨数据的农民。

环境部长穆雷·瓦特已责成气象局新任首席执行官斯图尔特·明钦调查成本超支和网站功能问题，并要求就此事提交报告。虽然气象局声称为了安全、可用性和可访问性，“完全重建”是必要的，但部长对此次过渡和总体成本表示失望。

此后，气象局已经恢复了一些更改，包括恢复旧雷达图的视觉风格，并计划根据用户反馈进行进一步更新，尽管其中一些已经暂停。国家党领袖大卫·利特普劳德批评该项目是“工党灾难”，强调了对该网站影响访问重要本地化数据的担忧，并指责气象局隐瞒了真实成本。瓦特表示，在收到明钦的报告之前，他将保留对该项目是否浪费资金的判断。

---

## 33. 传递火炬 – 我作为加密官 4 的最后一次根 DNSSEC KSK 仪式

**原文标题**: Passing the Torch – My Last Root DNSSEC KSK Ceremony as Crypto Officer 4

**原文链接**: [https://technotes.seastrom.com/2025/11/23/passing-the-torch.html](https://technotes.seastrom.com/2025/11/23/passing-the-torch.html)

本文讲述了作者作为KMF-East的4级密码官，参与ICANN根域名DNSSEC KSK仪式的15年经历。文章首先简要介绍了互联网历史和DNS的演变，解释了为何安全最初并非首要任务。作者详细描述了卡明斯基漏洞后DNSSEC的开发和部署，强调了ICANN通过地理位置分散的安全站点、多层安全协议和公开直播的仪式来确保信任和透明度的努力。

作为最初的密码官之一，作者描述了自己自2010年第一次仪式以来的参与情况，强调了其中的冒险经历以及多年来见证的积极变化，包括可信社区代表选拔的改进。

文章最终讲述了作者最近从该职位退休，将接力棒传递给安全研究员和教育家Lodrina Cherne。作者澄清说，他们的离开是由于在长期服务后计划的轮换、流程改进的成功实施以及成功过渡到新的HSM。作者强调了DNSSEC验证的广泛采用，并对有机会为DNS根的安全性和完整性做出贡献表示感谢。最后，作者提供了仪式脚本和日志以供参考，并提到未来可能作为外部证人参加仪式。

---

## 34. Show HN: Gitlogue – 一个以动画回放 Git 提交的终端工具

**原文标题**: Show HN: Gitlogue – A terminal tool that replays your Git commits with animation

**原文链接**: [https://github.com/unhappychoice/gitlogue](https://github.com/unhappychoice/gitlogue)

Gitlogue是一个终端工具，能以动画形式呈现你的 Git 提交历史，以视觉上引人入胜的方式重现代码更改。它模拟真实的打字、光标移动、文件操作，并为 26 种语言提供语法高亮显示。功能包括带更改统计的项目文件树、屏幕保护模式、可自定义的主题以及因使用 Rust 构建而带来的快速性能。

安装选项包括安装脚本、Homebrew、Cargo、Arch Linux 包管理器以及从源代码构建。

常见用途包括编码屏幕保护程序、用于可视化代码演变的教育工具、演示辅助工具、内容创建工具以及有趣的终端装饰。它提供查看特定提交、重播范围、更改顺序、循环、自定义主题、调整打字速度以及忽略文件的选项。通过 `config.toml` 进行配置。

该工具支持许多流行的语言。提供安装、使用、配置、主题和贡献的文档。列出了与 Git 可视化、编码游戏和终端屏幕保护程序相关的项目。欢迎贡献，并且该项目已获得 ISC 许可。

---

## 35. 法国威胁石墨烯操作系统，若拒绝开设后门，将逮捕相关人员/没收服务器

**原文标题**: France threatens GrapheneOS with arrests / server seizure for refusing backdoors

**原文链接**: [https://grapheneos.social/@watchfulcitizen@goingdark.social/115605398547420414](https://grapheneos.social/@watchfulcitizen@goingdark.social/115605398547420414)

该帖子的核心论点，基于其标题“法国威胁GrapheneOS，若拒绝后门则逮捕/查封服务器”，是法国当局正威胁隐私至上的移动操作系统GrapheneOS，若其拒绝在软件中植入后门，将对其采取法律行动（逮捕和查封服务器）。

该帖子链接至Mastodon用户“@watchfulcitizen”在“goingdark.social”实例上的帖子。要提供更完整的总结，需要Mastodon帖子本身。在缺乏其链接的Mastodon帖子提供的背景信息的情况下，这是目前最完整的总结。

---

## 36. 用于隔离、并行代理式开发的桌面应用

**原文标题**: A desktop app for isolated, parallel agentic development

**原文链接**: [https://github.com/coder/mux](https://github.com/coder/mux)

Mux是一款桌面应用程序，旨在促进并行智能体开发。它允许开发者在隔离的工作空间中同时运行多个编码智能体，通过上下文连续性、不同方法的A/B测试以及探索分支而不中断主要工作流程等功能，从而提高生产力。

Mux支持多种LLM，包括GPT-5-Pro，以及通过Ollama支持的本地LLM，并通过OpenRouter支持大量模型。主要功能包括：

*   **隔离工作空间：** 利用本地git工作树或远程SSH克隆。
*   **多模型支持：** 支持各种LLM并启用A/B测试。
*   **后台运行：** 允许长时间运行的进程，并在中断后自动恢复。
*   **VS Code集成：** 提供VS Code扩展程序，方便访问工作空间。
*   **高效UI：** 提供支持性UI和快捷键，用于管理智能体。
*   **丰富输出：** 支持Markdown、Mermaid图表和LaTeX。
*   **智能体循环：** 自定义智能体循环，具有Plan/Exec模式、Vim输入和机会性压缩。
*   **追踪：** 跟踪成本和token消耗。

该应用程序包括Git差异UI、智能体状态报告和集成代码审查。 它的目标是提供一个环境，让开发者能够利用AI智能体来加速开发过程。 Mux目前处于预览状态，并且预构建的二进制文件可用于macOS和Linux。

---

## 37. 皮克斯：早期岁月

**原文标题**: Pixar: The Early Days

**原文链接**: [https://stevejobsarchive.com/stories/pixar-early-days](https://stevejobsarchive.com/stories/pixar-early-days)

这篇来自史蒂夫·乔布斯档案馆的文章通过发布一段此前未公开的 1996 年史蒂夫·乔布斯访谈，庆祝皮克斯《玩具总动员》上映 30 周年。 访谈深入探讨了皮克斯早期的成功，以及在开创性的全电脑动画长片《玩具总动员》发布后所取得的成就。

这篇文章重点介绍了该电影的影响，包括皮克斯成功的首次公开募股（IPO）以及随后通过关闭其商业部门而专注于长篇电影。 访谈本身揭示了乔布斯对皮克斯商业模式的看法，强调了该模式如何赋能艺术家和工程师。 他讨论了从迪士尼学到的关于专注和纪律的经验教训，以及领导一支才华横溢的团队所面临的挑战。

乔布斯还反思了皮克斯通过激励和共同目标（创造为文化做出贡献的持久故事）来留住人才的策略。 文章强调了乔布斯与总裁埃德·卡特穆尔之间合作的重要性，从而形成了一种以培养人才为中心的管理方法。 最后，文章指出，乔布斯在皮克斯的经历极大地影响了他重返苹果后的领导风格，塑造了他基于永恒理念和技术创新来建立公司的愿景。

---

## 38. 爱荷华市公交免费，交通顺畅，空气清新。

**原文标题**: Iowa City made its buses free. Traffic cleared, and so did the air

**原文链接**: [https://www.nytimes.com/2025/11/18/climate/iowa-city-free-buses.html](https://www.nytimes.com/2025/11/18/climate/iowa-city-free-buses.html)

无法访问文章链接。

---

## 39. 复数乐事

**原文标题**: Having Fun with Complex Numbers

**原文链接**: [https://mathwonder.org/Having-Fun-with-Complex-Numbers/](https://mathwonder.org/Having-Fun-with-Complex-Numbers/)

卢秋江博士的《复数真好玩：高年级小学生的生活之旅》旨在让8-12岁的儿童轻松有趣地学习复数。本书有别于传统教科书方法，将复数定义为“表面数”，并将其与触摸屏交互和现实世界中的运动直观地联系起来。

本书强调宏观思维、创造性方法和动态演示，寓教于乐，而非死记硬背。它利用现实生活中的例子、隐喻和互动元素，自然地引入并建立对数学概念的信心。学生将在复数的背景下探索数轴、数格以及加法和乘法等基本数学运算。

本书面向寻求有趣和创新的数学学习资源的儿童、家庭学校、家长和教师。卢博士的研究从根本上重新开发了复数理论，使其适合小学生。他的方法解决了传统数学教育的局限性，旨在激发年轻学习者对数学的热情。一本面向教师和年龄较大学生的姊妹篇《在日常生活中发现虚数》也已出版。

---

## 40. Hyperoptic：IPv6与乱序数据包

**原文标题**: Hyperoptic: IPv6 and Out-of-Order Packets

**原文链接**: [https://blog.zakkemble.net/hyperoptic-ipv6-and-out-of-order-packets/](https://blog.zakkemble.net/hyperoptic-ipv6-and-out-of-order-packets/)

使用定制RouterPi设置Hyperoptic网络服务时遇到的两个IPv6相关问题及解决方案

本文详细介绍了在使用定制RouterPi设置的Hyperoptic网络服务时遇到的两个与IPv6相关的问题，并提供了解决方法。

首先，作者发现，在路由器重启或WAN线重新插拔后，由于Hyperoptic的上游路由器没有立即响应路由器请求（RS）数据包，IPv6连接会变得断断续续。相反，路由器仅每隔15-30分钟发送一次未经请求的路由器通告（RA），导致网络拥有IPv6地址但没有默认路由。一种解决方法是更改WAN接口的MAC地址，这将触发立即的RA。作者建议使用`macchanger`或通过`dhcpcd` hook脚本使用`ip -6 route`手动添加默认网关作为潜在的解决方案。他们还建议从`dhcpcd.conf`中删除`ia_na`以防止日志泛滥。

其次，作者遇到了频繁的乱序（OOO）数据包。调查显示，这很可能是由于Hyperoptic的设备错误地将WAN接口的目标MAC地址（以“4”开头）解释为IPv4数据包头。将WAN接口的MAC地址更改为不以“4”或“6”开头的地址解决了这个问题。作者提供了使用`systemd` link文件永久更改MAC地址的说明。文章最后推测，有多少其他用户可能因为其路由器的MAC地址而遇到类似的OOO数据包问题。

---

## 41. 人工智能代理的经济

**原文标题**: An Economy of AI Agents

**原文链接**: [https://arxiv.org/abs/2509.01063](https://arxiv.org/abs/2509.01063)

这篇arXiv论文，题为“AI代理的经济”，于2025年9月1日提交，探讨了日益自主的AI代理对经济的潜在影响。该论文由Gillian K. Hadfield和Andrew Koh撰写，综述了人工智能领域的最新进展，重点关注能够独立规划并在较长时间内执行复杂任务的代理。

该论文探讨的核心问题是，这些AI代理如何与人类以及彼此互动，如何重塑现有市场和组织，以及需要哪些新的制度来确保在这个新兴经济中市场良好运作。

该论文属于一般经济学(econ.GN)、人工智能(cs.AI)和多智能体系统(cs.MA)学科分类，突出了其跨学科性质。它表明了由人工智能驱动的经济动态的重大转变，要求经济学家考虑将自主代理作为经济行为者所带来的影响。作者强调了围绕这一转变的几个悬而未决的问题，并为理解和驾驭这一不断变化的格局提出了未来的研究方向。该论文提供PDF和实验性HTML格式，并提供TeX源代码链接。

---

## 42. 使用 rclone 和 systemd 在 Linux 上挂载 Proton Drive

**原文标题**: Mount Proton Drive on Linux using rclone and systemd

**原文链接**: [https://github.com/dadtronics/protondrive-linux](https://github.com/dadtronics/protondrive-linux)

本指南详细介绍了如何使用rclone和systemd在Linux系统上自动挂载Proton Drive，确保驱动器在登录时挂载。它适用于大多数Linux发行版，尽管主要是在Arch Linux上测试的。

该过程包括以下几个步骤：

1.  **安装依赖项：** 这包括用于挂载的`fuse3`和用于与Proton Drive交互的`rclone`（1.64.0或更高版本）。本指南提供了使用预编译二进制文件安装rclone的说明。

2.  **配置Proton Drive远程：** 该指南指导用户使用`rclone config`创建一个新的远程，指定“protondrive”作为类型并通过浏览器进行身份验证。

3.  **运行设置脚本：** 提供的脚本（`setup-proton-mount.sh`）可以自动完成大部分设置。它创建挂载点（`~/ProtonDrive`），写入systemd用户服务文件，修改`/etc/fuse.conf`以启用`user_allow_other`，并将用户添加到fuse组（如果需要）。最后，它启用并启动systemd服务。

4.  **重启或注销/登录：** 这是使fuse组成员身份更改生效所必需的。

5.  **验证：** 该指南提供了用于检查驱动器是否已挂载以及验证systemd服务状态的命令。

该指南还包括卸载设置的说明，列出相关文件，概述要求（rclone、fuse3、Proton Drive帐户），并提供故障排除技巧和相关文档的参考。rclone配置利用`--vfs-cache-mode writes`以获得更好的兼容性。该服务在后台运行，并启用日志记录以进行调试。

---

## 43. macOS上的原生安全隔离区支持的SSH密钥

**原文标题**: Native Secure Enclave backed SSH keys on macOS

**原文链接**: [https://gist.github.com/arianvp/5f59f1783e3eaf1a2d4cd8e952bb4acf](https://gist.github.com/arianvp/5f59f1783e3eaf1a2d4cd8e952bb4acf)

本文详细介绍了如何利用macOS的安全隔离区原生存储和使用SSH密钥，从而无需像Secretive这样的第三方工具。它利用了现有的`/usr/lib/ssh-keychain.dylib`库，该库传统上用于智能卡支持，但现在也支持通过其`SecurityKeyProvider`接口直接从安全隔离区加载密钥。

本文提供了使用`sc_auth`创建由安全隔离区支持的SSH密钥的分步说明，包括设置生物识别认证。涵盖的关键命令包括：

*   `sc_auth create-ctk-identity`: 创建一个新的由安全隔离区支持的密钥。
*   `sc_auth list-ctk-identities`: 列出现有的由安全隔离区支持的密钥。
*   `sc_auth delete-ctk-identity`: 删除一个由安全隔离区支持的密钥。
*   `ssh-keygen -w`: 下载公钥/私钥对（私钥只是一个引用）。
*   `ssh-add -K -S`: 直接从安全隔离区将密钥添加到ssh-agent。

文章解释了如何将这些密钥与`ssh`和`ssh-agent`一起使用，强调需要指定`SecurityKeyProvider`才能正常工作。 文章建议设置`SSH_SK_PROVIDER`环境变量以实现无缝集成。

最后，文章提到了创建“可导出”密钥，其中私钥由安全隔离区加密以进行备份，尽管这可能被认为安全性较低。可以使用`sc_auth export-ctk-identity`和`sc_auth import-ctk-identities`在不同的设备上导出和重新导入这些密钥。

---

## 44. 面向对象编程的五十道阴影

**原文标题**: Fifty Shades of OOP

**原文链接**: [https://lesleylai.info/en/fifty_shades_of_oop/](https://lesleylai.info/en/fifty_shades_of_oop/)

面向对象编程的五十道阴影

本文《面向对象编程的五十道阴影》探讨了面向对象编程（OOP）的多面性，认为它是一系列相互关联的思想的集合，而非一个单一、明确定义的概念。它避免了对OOP的辩护或攻击，而是选择对其核心要素进行细致的剖析。

作者剖析了关键的OOP概念，如类、方法语法、信息隐藏、封装、接口、延迟绑定、动态分派、继承和子类型多态。对于每个概念，文章都概述了其目的、优点、缺点和替代方法。

**要点：**

*   **类：** 提供结构，可以被视为对象的蓝图，但原型提供了另一种选择。
*   **方法语法：** 提高代码可读性和IDE自动补全功能，但可能导致权力失衡以及与隐式`this`混淆。
*   **信息隐藏：** 保护不变式并将实现与接口分离，但可能导致样板代码。
*   **封装：** 捆绑数据和功能，但可能导致不良的数据局部性。
*   **接口：** 提供了一种有纪律的继承替代方案，支持多态性，但可能具有运行时成本。
*   **延迟绑定：** 启用运行时灵活性，但引入了性能成本和潜在错误。
*   **动态分派：** 在运行时选择实现，但会阻碍编译器优化。
*   **继承：** 允许代码重用和多态性，但缺乏灵活性，并且可能违反里氏替换原则。
*   **子类型多态：** 定义“是一种”关系，但需要仔细遵守里氏替换原则。

最终，文章强调了与每个OOP概念相关的权衡，表明平衡的理解对于有效的软件开发至关重要。

---

## 45. 使用Go和Web技术构建桌面应用

**原文标题**: Build desktop applications using Go and Web Technologies

**原文链接**: [https://github.com/wailsapp/wails](https://github.com/wailsapp/wails)

Wails 是一种工具，它允许 Go 开发者通过将 Go 代码与 Web 前端（HTML/JS/CSS）捆绑到一个单独的二进制文件中来构建桌面应用程序，从而提供了一种替代传统 Web 服务器方法的方案。它简化了创建、编译和捆绑过程，使开发者能够专注于创作。

主要功能包括使用标准 Go 作为后端，使用任何前端技术作为 UI，并使用模板快速创建丰富的前端。它还提供诸如从 Javascript 轻松调用 Go 方法、自动生成 Typescript 定义、原生对话框和菜单、深色/浅色模式支持、半透明效果和统一的事件系统等功能。 CLI 工具简化了项目生成和构建。 Wails 是多平台的，并使用原生渲染引擎，避免了嵌入式浏览器。

Wails 旨在成为 Electron 的轻量级替代品，面向希望将 Web 前端与他们的应用程序捆绑在一起而无需单独服务器的 Go 程序员。 该项目在官方网站上提供了未来发展路线图和安装说明，并且还有一个 FAQ 部分解答常见问题。

---

## 46. 苔藓在国际空间站外存活了9个月

**原文标题**: Moss survived outside of the International Space Station for 9 months

**原文链接**: [https://www.livescience.com/space/scientists-put-moss-on-the-outside-of-the-international-space-station-for-9-months-then-kept-it-growing-back-on-earth](https://www.livescience.com/space/scientists-put-moss-on-the-outside-of-the-international-space-station-for-9-months-then-kept-it-growing-back-on-earth)

一种苔藓，小立碗藓 (*Physcomitrium patens*)，在国际空间站（ISS）外存活了九个月，展现了非凡的韧性。研究人员测试了苔藓孢子承受太空严酷环境的能力，包括温度波动、重力改变和高辐射暴露。返回地球后，超过 80% 的孢子仍然能够繁殖，证明了该苔藓在极端环境中茁壮成长的卓越能力。

研究人员发现，孢蒴，即包裹孢子的细胞结构，表现出最强的耐逆性，特别是对紫外线、冰冻和高温。虽然大多数太空条件的影响有限，但暴露于紫外线被证明最具破坏性，降低了叶绿素水平并影响了后期的生长。然而，小立碗藓的表现仍然优于在类似条件下测试的其他植物。

藤田智道教授认为，孢子周围的海绵状外壳可能提供对紫外线和脱水的保护，这种特性可能在陆地植物早期进化过程中形成。该研究表明，苔藓孢子可能在太空中存活长达 15 年。

这项研究不仅扩展了对植物在极端条件下生存能力的理解，也暗示了利用像苔藓这样具有韧性的物种在地球以外建立生态系统的潜力。藤田计划继续探索其他物种在太空中的生存能力，以进一步了解它们的适应机制。

---

## 47. 在欧洲核子研究中心使用人工智能的通用原则

**原文标题**: General principles for the use of AI at CERN

**原文链接**: [https://home.web.cern.ch/news/official-news/knowledge-sharing/general-principles-use-ai-cern](https://home.web.cern.ch/news/official-news/knowledge-sharing/general-principles-use-ai-cern)

这篇欧洲核子研究中心（CERN）2025年11月13日发布的新闻文章，概述了在欧洲核子研究中心所有活动中负责任地且合乎伦理地使用人工智能（AI）的一般原则，该原则是在全欧洲核子研究中心范围内的人工智能战略获得批准后制定的。这些原则适用于嵌入在设备、软件、云服务和内部开发中的人工智能，涵盖科学/技术研究以及行政/生产力应用。

核心原则强调：

*   **透明度和可解释性：** 记录并沟通人工智能的使用情况。
*   **责任和问责制：** 保持人为监督和责任。
*   **合法性和行为规范：** 遵守法律框架和欧洲核子研究中心的行为准则。
*   **公平性、非歧视性和“不造成伤害”：** 促进公平并防止偏见。
*   **安全和保障：** 保护人工智能系统免受网络安全威胁并确保安全使用。
*   **可持续性：** 评估并减轻与人工智能使用相关的环境和社会风险。
*   **人为监督：** 持续评估和验证人工智能的功能和输出。
*   **数据隐私：** 尊重隐私并保护个人数据。
*   **非军事目的：** 限制人工智能的使用于非军事应用。

该文章还包含有关欧洲核子研究中心人工智能战略的相关文章，并展示了欧洲核子研究中心的技术。它提醒工作人员注意官方新闻，并强调外部复制此信息需要获得欧洲核子研究中心管理层的批准。

---

## 48. 麦克马斯特-卡 – 你可能没听过的最智能的网站 (2022)

**原文标题**: McMaster Carr – The Smartest Website You Haven't Heard Of (2022)

**原文链接**: [https://www.bedelstein.com/post/mcmaster-carr](https://www.bedelstein.com/post/mcmaster-carr)

本文赞扬了 McMaster-Carr 的电商网站 (mcmaster.com)，称其功能卓越、以用户为中心，尤其适合需要工业用品的工程师。该网站优先考虑效率而非美观，采用极简的灰度设计，没有任何分散注意力的元素，如弹出窗口或动画。其核心优势在于强大的搜索界面，允许用户通过精确的规格（如螺纹尺寸、长度、材料和硬度）快速筛选 70 万种产品。

作者强调了该网站直观的筛选系统，通过示意图和有用的下拉解释（如同内置的工程师手册）进行了增强。McMaster 的优势源于其产品的高度可量化性，无需主观品牌推广或营销策略。这与亚马逊形成了鲜明对比，亚马逊因其繁琐的筛选和通用设计元素而受到批评。

一个关键特性是几乎每个产品都有 CAD 文件，这使得工程师能够将 McMaster-Carr 组件无缝集成到其 3D 模型中，从而大大加快了设计过程。作者建议唯一的改进之处是让搜索栏在主页上更加突出。文章总结说，McMaster-Carr 是了解用户需求的网站设计典范，专注于功能和效率，证明了美可以源于纯粹的功能。

---

## 49. X意外曝光了一个针对美国人的秘密影响力网络

**原文标题**: X Just Accidentally Exposed a Covert Influence Network Targeting Americans

**原文链接**: [https://weaponizedspaces.substack.com/p/x-just-accidentally-exposed-a-vast](https://weaponizedspaces.substack.com/p/x-just-accidentally-exposed-a-vast)

无法访问文章链接。

---

## 50. 粒子生命

**原文标题**: Particle Life

**原文链接**: [https://sandbox-science.com/particle-life](https://sandbox-science.com/particle-life)

粒子生命似乎描述了一个模拟环境，可能是一款软件应用，允许用户创建和操控粒子系统。该界面看起来高度可定制，可以根据模拟的力（排斥、吸引）、半径和其他物理属性（如摩擦力）修改粒子行为。

该模拟的关键功能包括：

*   **环境控制：** 用户可以使用矩形、圆形或无边界来定义世界边界，从而实现环绕效果。他们还可以调整屏幕缩放。
*   **物理引擎设置：** 控制力（排斥力、力因子）、摩擦力和粒子属性的随机化。
*   **粒子属性：** 控制粒子半径、颜色、数量和深度（用于 3D 模拟）。
*   **图形定制：** 用户可以更改粒子的形状、大小、深度和不透明度以获得视觉效果。提供 2D 和 3D 模拟的选择。
*   **调试工具：** 提供显示单元格和跟踪性能指标的选项，例如每秒帧数 (FPS)、单元格计数和处理负载。“跟随”选项可能允许相机跟随粒子。
*   **笔刷工具：** 用于将粒子行为直接绘制到模拟中的交互式工具（吸引、排斥）。
*   **保存和分享：** 截取屏幕截图的功能。
*   **性能指标：** 显示有关 FPS、单元格计数和处理的实时信息。

总而言之，“粒子生命”应用程序似乎是一个多功能的工具，可以通过可定制的物理和图形参数来试验粒子模拟并创建视觉上有趣的效果。

---

## 51. Meta巨型新数据中心：AI遇上激进会计

**原文标题**: AI Meets Aggressive Accounting at Meta's Gigantic New Data Center

**原文链接**: [https://www.wsj.com/tech/meta-ai-data-center-finances-d3a6b464](https://www.wsj.com/tech/meta-ai-data-center-finances-d3a6b464)

无法访问文章链接。

---

## 52. 在 Emacs 中编辑代码

**原文标题**: Editing Code in Emacs

**原文链接**: [https://redpenguin101.github.io/html/posts/2025_11_23_emacs_for_code_editing.html](https://redpenguin101.github.io/html/posts/2025_11_23_emacs_for_code_editing.html)

本文旨在指导如何在Emacs中高效编辑代码，重点在于最小化击键次数，最大程度地专注于代码本身。文章提倡一种模态编辑方法，区分“命令”模式（用于移动和操作）和“插入”模式（用于键入）。作者强调使用主行、重新映射方向键，甚至禁用鼠标。

文章详细介绍了各种导航技巧，包括：

*   **垂直移动：** 使用相对行号，'n'和'p'用于行导航，'r'和't'用于半页滚动，'l'和'L'用于重新定位光标或屏幕。
*   **水平移动：** 推荐子词模式和更大的单位，例如“单词”或理想情况下“表达式”（sexps），而不是单个字符。
*   **按表达式 (Sexps) 移动：** 使用'j'和'h'跳过或在语法块内跳转，以及'd'和'u'进入和退出块。
*   **按搜索移动：** 使用增量搜索（C-s和C-r）和'occur'模式（so）查找和跳转到术语的多个实例。

作者还介绍了使用寄存器和标记在位置之间快速跳转。查找和替换使用标准的Emacs功能（sq）和项目范围内的查找和替换（vpq）进行处理。最后，文章强调了剪切/复制/粘贴操作在代码编辑中的重要性。

---

## 53. 牙买加雷鬼歌手、演员和文化偶像吉米·克里夫去世，享年81岁

**原文标题**: Jimmy Cliff, Jamaican reggae singer, actor and cultural icon, dies aged 81

**原文链接**: [https://www.theguardian.com/music/2025/nov/24/jimmy-cliff-jamaican-reggae-singer-actor-and-cultural-icon-dies-aged-81](https://www.theguardian.com/music/2025/nov/24/jimmy-cliff-jamaican-reggae-singer-actor-and-cultural-icon-dies-aged-81)

影响力深远的牙买加雷鬼歌手、演员和文化偶像吉米·克利夫去世，享年 81 岁，死因是癫痫和肺炎并发症。 他的妻子拉蒂法·钱伯斯在 Instagram 上分享了这一消息，表达了对他的歌迷和合作者的感谢。 克利夫以其乐观和社会意识的音乐而闻名，代表作包括《只要你真的想，你就能得到》、《我现在看得清清楚楚》和《美好的世界，美丽的人们》。

克利夫的职业生涯始于 20 世纪 60 年代初在牙买加金斯敦，此前他从圣詹姆斯搬来。 他与 Island Records 签约，最初面向摇滚观众进行营销，后来凭借融合斯卡风格的雷鬼音乐取得了主流成功。 他在 1972 年的电影《越难越爱》中的主角对将雷鬼音乐带给全球观众起到了关键作用。

克利夫备受赞誉，荣获牙买加功绩勋章。 牙买加总理安德鲁·霍尔尼斯称克利夫为“真正的文化巨人”，他通过音乐分享了国家的心声。 他曾短暂休息，前往非洲重新与他的根源联系，并且他还皈依了伊斯兰教。

克利夫在他的职业生涯中继续录制和巡回演出，与滚石乐队和斯汀等艺术家合作。 1994 年，他在电影《冰上轻喜剧》中翻唱的《我现在看得清清楚楚》使他的职业生涯焕发了生机。 他赢得了两项格莱美奖，其中包括与 Rancid 乐队的蒂姆·阿姆斯特朗合作的专辑。 他的最后一张专辑《Refugees》于 2022 年发行。 除了《越难越爱》，克利夫偶尔也会回归演艺事业，最著名的是 1986 年的《天堂俱乐部》。

---

## 54. 半条命2中的时空旅行门漏洞

**原文标题**: A time-travelling door bug in Half Life 2

**原文链接**: [https://mastodon.gamedev.place/@TomF/115589875974658415](https://mastodon.gamedev.place/@TomF/115589875974658415)

Tom Forsyth的Mastodon帖子提到了游戏开发中门的危险性讨论。核心背景可能是半条命2中的一个bug，特别是“时间旅行门”bug。帖子本身很简短，暗示这个bug涉及一扇门的行为以一种导致游戏中出现意想不到且可能具有时间效应的方式，可能与其物理或脚本有关。主要的结论是，即使是像门这样看似简单的元素也可能引入复杂且可能破坏游戏的bug，突显了游戏开发的挑战。该帖子还巧妙地推广了使用专用的Mastodon应用程序而不是网页版本。

---

## 55. 漏洞带

**原文标题**: Band of Holes

**原文链接**: [https://en.wikipedia.org/wiki/Band_of_Holes](https://en.wikipedia.org/wiki/Band_of_Holes)

秘鲁皮斯科山谷“洞穴带”
（又称蒙特谢尔佩或塞罗维鲁埃拉）是纳斯卡高原上的一个考古遗址。它由大约5000至6000个人大小的洞穴组成，这些洞穴排列成南北向的带状，延伸约1.5公里至山坡上。这些洞穴（实际上是边缘凸起的坑）直径约为1米，深50-100厘米，排列在一个平均宽度为19米的带状区域内。

该遗址在1933年因《国家地理》上发表的一张航拍照片而引起现代关注。早期的理论认为这些洞穴是坟墓、防御阵地或储藏地。维克多·沃尔夫冈·冯·哈根于1953年考察了该地区，认为它们是印加前时期的坟墓。约翰·海斯洛普认为它们可能被用于储藏，可能被印加帝国使用，因为它们的位置靠近重要的印加遗址和道路。

最近的考古调查，包括2015年的无人机摄影，已经导致了一种假设，即这些洞穴被用来测量进贡给印加国家的农业贡品，测量结果可能记录在奇普上。一篇发表于2025年的文章推测，蒙特谢尔佩最初是一个易货市场，后来是一个贡品会计设备。计划进行进一步的研究，以分析花粉或植物硅酸体，以支持这些理论。

---

## 56. 面向数学家、计算机科学家和物理学家的微积分 [pdf]

**原文标题**: Calculus for Mathematicians, Computer Scientists, and Physicists [pdf]

**原文链接**: [https://mathcs.holycross.edu/~ahwang/print/calc.pdf](https://mathcs.holycross.edu/~ahwang/print/calc.pdf)

此PDF文档似乎是一本名为《数学家、计算机科学家和物理学家微积分》的微积分教材的目录和前几页。内容主要由定义文档内超链接（注释）的PDF标记组成，方便浏览。

目录概述了本书的结构，从基础数学概念开始：数学语言（集合、逻辑）和不同类型的数字（自然数、整数、有理数、实数、复数）。然后进入核心微积分主题：函数、极限和连续性、区间上的连续性、积分、微分、中值定理和微积分基本定理。高级主题包括函数序列、对数和指数函数、三角函数、泰勒近似和初等函数。还列出了一个简短的复分析课程。本书以跋、参考书目和索引结尾。PDF代码还定义了与渲染相关的元素，例如字体和页面结构。

---

## 57. 着色器：如何仅用 x 和 y 坐标绘制高保真图形

**原文标题**: Shaders: How to draw high fidelity graphics with just x and y coordinates

**原文链接**: [https://www.makingsoftware.com/chapters/shaders](https://www.makingsoftware.com/chapters/shaders)

无法访问文章链接。

---

## 58. Supermaven 日落

**原文标题**: Sunsetting Supermaven

**原文链接**: [https://supermaven.com/blog/sunsetting-supermaven](https://supermaven.com/blog/sunsetting-supermaven)

Supermaven将于2025年11月21日停止服务，即被收购一年后。现有客户将获得剩余使用时间和订阅时间的退款。虽然不再支持代理对话，但鼓励用户在Cursor中使用前沿模型。特别建议VS Code用户迁移到Cursor，因为Supermaven的功能已集成，并且Cursor中的自动补全模型已显著改进。重要的是，Neovim和JetBrains用户在可预见的未来将继续获得免费的自动补全推断，以感谢他们对产品的强烈反馈和喜爱。

---

## 59. Racket v9.0

**原文标题**: Racket v9.0

**原文链接**: [https://blog.racket-lang.org/2025/11/racket-v9-0.html](https://blog.racket-lang.org/2025/11/racket-v9-0.html)

Racket v9.0 发布，新增重大特性：并行线程。本次发布在绿色线程、future 和 place 之外，进一步增强了 Racket 的并发能力。主要特性和改进包括：

*   **并行线程:** 可通过在 `thread` 创建中使用 `:pool` 参数来创建。使用 `:keep set to 'results` 的线程将记录其结果，以便稍后使用 `thread-wait` 检索。
*   **黑盒包装器:** 防止基准测试期间出现不必要的优化。
*   **Linklet 反编译:** `decompile-linklet` 函数现在将 linklet 映射回 s-表达式。
*   **BC Racket 更新:** `processor-count` 函数现在返回并行计数。
*   **AArch64 包:** 现在为 AArch64 架构分发 “natipkg” 包。
*   **语法跟踪:** Check Syntax 现在在语法对象的 origin 字段中更深入地跟踪标识符。
*   **数学库:** 包括 Weibull 分布。
*   **其他改进:** 已实施各种修复和文档更新。

此次发布还感谢了该项目的众多贡献者，并鼓励新的开发人员加入开源社区。请访问 https://download.racket-lang.org/ 下载 Racket 9.0。有关此版本的更多信息，请访问 https://blog.racket-lang.org/2025/11/racket-v9-0.html。

---

## 60. 法庭文件指控Meta淡化儿童风险并误导公众。

**原文标题**: Court filings allege Meta downplayed risks to children and misled the public

**原文链接**: [https://time.com/7336204/meta-lawsuit-files-child-safety/](https://time.com/7336204/meta-lawsuit-files-child-safety/)

一份近期解封的法庭文件指控Meta淡化其平台对儿童的风险，并误导公众和国会。该文件是一项涉及超过1800名原告的更大诉讼的一部分，声称Meta知晓性交易、精神健康问题以及未成年人不希望的成人互动等危害，但将增长和利润置于安全之上。

关键指控包括：对性交易账户采取宽松的“17次”违规政策，缺乏举报儿童性虐待内容的简便方式，压制一项显示使用Facebook和Instagram产生负面精神健康影响的研究，以及就此向国会提供误导性信息。诉讼还称，Meta明知成年陌生人正在联系青少年，并多年来抵制默认将青少年账户设置为私密，据称导致青少年遭受数百万次不必要的互动。

原告指控Meta积极瞄准年轻用户，甚至研究“准少年”的心理，且无法可靠地知晓数百万用户的年龄。据称，对安全性的内部担忧被优先考虑用户参与度和增长的高管们否决。Meta否认了这些指控，称其已做出重大改变以保护青少年。然而，原告的简报引用了前Meta高管的话，称该公司并未将用户安全放在首位。

---

## 61. 墨菲柔术 (2018)

**原文标题**: Murphyjitsu (2018)

**原文链接**: [https://www.lesswrong.com/posts/N47M3JiHveHfwdbFg/hammertime-day-10-murphyjitsu](https://www.lesswrong.com/posts/N47M3JiHveHfwdbFg/hammertime-day-10-murphyjitsu)

无法访问文章链接。

---

## 62. 新丹·卡林 – 常识

**原文标题**: New Dan Carlin – Common Sense

**原文链接**: [https://www.dancarlin.com/product/common-sense-325-whos-the-boss/](https://www.dancarlin.com/product/common-sense-325-whos-the-boss/)

丹·卡林的《常识325：谁是老大？》关注这样一个情境：总统对民主党议员提醒军人注意其宪法誓词和责任感到不满。卡林认为，士兵的个体能动性，即他们根据誓词和良知思考和行动的能力，是所有人的一项至关重要的社会保障。他暗示，盲目服从命令而不考虑宪法原则可能是危险的。

该集于2025年11月23日发布，时长约39分钟，可供下载，大小为29.2mb。 由于价格标为0.00美元，因此也可以免费获取。 节目注释中提到了“美国诉基南”一案，暗示这可能是讨论的一个相关参考点。 该文章还宣传了其他“常识”节目。

---

## 63. Posthog NPM 包被入侵

**原文标题**: Posthog NPM packages are compromised

**原文链接**: [https://twitter.com/posthog/status/1992894777524674642](https://twitter.com/posthog/status/1992894777524674642)

本文报道了Posthog NPM包被入侵的事件。然而，标题下的内容与此无关，似乎是X（前身为Twitter）的错误信息，表明用户的浏览器禁用了JavaScript，导致无法使用该网站。

因此，我无法根据提供的内容总结关于Posthog NPM包被入侵的报告。提供的内容仅涉及X网站上的JavaScript问题，不包含任何关于Posthog NPM包被入侵的信息。

---

## 64. Syd – 蓝队离线优先的AI增强工作站

**原文标题**: Syd – An offline-first, AI-augmented workstation for blue teams

**原文链接**: [https://www.sydsec.co.uk](https://www.sydsec.co.uk)

Syd：面向网络安全蓝红队的离线AI增强工作站

---

## 65. 基于ncurses的高性能命令行Torrent客户端

**原文标题**: A ncurses-based command line torrent client for high performance

**原文链接**: [https://github.com/rakshasa/rtorrent](https://github.com/rakshasa/rtorrent)

RTorrent 是一个基于 ncurses 构建的高性能命令行 BitTorrent 客户端。它需要安装相同版本的 libtorrent，并提供一个无依赖的 bencode 编辑器 rbedit。要构建 rTorrent，用户必须导航到克隆的目录，安装构建依赖项，并使用 `autoreconf -ivf` 生成配置脚本。可以选择使用 `docbook2man rtorrent.1.xml` 生成 man 页面。

该项目强调 rTorrent 和 libtorrent 之间版本同步的关键性。项目 Wiki 上的用户指南提供了使用说明。

RTorrent 在 GNU GPL 许可下发布，但允许链接到 OpenSSL，并允许使用 Mozilla 的 NSS 进行 SHA1 编译。关键依赖项包括 libcurl (>= 7.12.0)、libtorrent（相同版本）和 ncurses。构建依赖项包括 libtoolize、aclocal、autoconf、autoheader 和 automake。

作者鼓励通过 Paypal、Patreon、SubscribeStar、Bitcoin、Ethereum、Litecoin 和 Cardano 进行捐赠，以支持持续开发。

---

## 66. After my dad died, we found the love letters

**原文标题**: After my dad died, we found the love letters

**原文链接**: [https://www.jenn.site/after-my-dad-died-we-found-the-love-letters/](https://www.jenn.site/after-my-dad-died-we-found-the-love-letters/)

生成摘要时出错

---

## 67. 辫式算术

**原文标题**: Braided Arithmetic

**原文链接**: [https://mathcenter.oxford.emory.edu/site/math108/braid_arithmetic/](https://mathcenter.oxford.emory.edu/site/math108/braid_arithmetic/)

生成摘要时出错

---

## 68. MCP应用：用交互式用户界面扩展服务器

**原文标题**: MCP Apps: Extending servers with interactive user interfaces

**原文链接**: [http://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/](http://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/)

生成摘要时出错

---

## 69. Markdown is holding you back

**原文标题**: Markdown is holding you back

**原文链接**: [https://newsletter.bphogan.com/archive/issue-45-markdown-is-holding-you-back/](https://newsletter.bphogan.com/archive/issue-45-markdown-is-holding-you-back/)

生成摘要时出错

---

## 70. The privacy nightmare of browser fingerprinting

**原文标题**: The privacy nightmare of browser fingerprinting

**原文链接**: [https://kevinboone.me/fingerprinting.html](https://kevinboone.me/fingerprinting.html)

生成摘要时出错

---

## 71. Booking.com cancels $4K hotel reservation, offers same rooms again for $17K

**原文标题**: Booking.com cancels $4K hotel reservation, offers same rooms again for $17K

**原文链接**: [https://www.cbc.ca/news/gopublic/go-public-booking-com-hotel-rates-9.6985480](https://www.cbc.ca/news/gopublic/go-public-booking-com-hotel-rates-9.6985480)

Erika Mann booked a $4,300 hotel through Booking.com for the 2026 Montreal Formula One Grand Prix. Weeks later, Booking.com cancelled the reservation, claiming the price was a mistake, and offered the same rooms for over $17,000.

Mann contacted Go Public, leading to an investigation. Digital rights lawyer David Fewer highlights how online booking platforms often shift risks and costs onto consumers, exploiting weak consumer protection laws and relying on automated pricing systems prone to errors.

The Holland Hotel blamed the price discrepancy on a "synchronization error" with Booking.com's system and its inability to manually override automated pricing updates. Booking.com initially sided with the hotel, citing its policy allowing cancellations for "obvious errors."

Fewer argues that the price difference wasn't a minor error like a misplaced decimal and that consumers should benefit from the deal they found. He stresses the need for stronger consumer protection laws to address surge pricing and after-the-fact event pricing.

After Go Public intervened, Booking.com reversed its decision and agreed to honor Mann's original booking at the initial price. While Mann is relieved, she believes such resolutions shouldn't require media intervention. Fewer advises travelers to take precautions like screenshots, direct hotel confirmation, and using credit cards with strong dispute policies to protect themselves when booking accommodations for major events.


---

## 72. Boy with rare condition amazes doctors after world-first gene therapy

**原文标题**: Boy with rare condition amazes doctors after world-first gene therapy

**原文链接**: [https://www.bbc.com/news/articles/c5y0y56x6veo](https://www.bbc.com/news/articles/c5y0y56x6veo)

Three-year-old Oliver Chu, suffering from the rare and devastating Hunter syndrome (MPSII), has amazed doctors with his progress after receiving a world-first gene therapy. Hunter syndrome, caused by a faulty gene that prevents the production of a crucial enzyme, leads to progressive damage to the body and brain, often resulting in death before the age of 20.

Oliver, the first of five boys worldwide to undergo the experimental treatment at Royal Manchester Children's Hospital, received an infusion of his own stem cells, genetically modified to carry the missing gene. The gene therapy aims to halt the disease's progression by enabling Oliver's cells to produce the missing enzyme, iduronate-2-sulfatase (IDS), which breaks down harmful sugar molecules.

A year after treatment, Oliver is developing normally, showing improvements in speech, mobility, and cognitive abilities. He has also been able to discontinue weekly enzyme infusion treatments. His parents express immense gratitude and hope that the same therapy will become available for his older brother, Skyler, who also suffers from Hunter syndrome.

The development of the gene therapy was led by researchers at the University of Manchester. The clinical trial almost didn't happen due to funding issues after the initial biotech partner withdrew. However, the charity LifeArc stepped in to provide crucial funding, enabling the trial to proceed. The success of Oliver's treatment offers hope for other children with Hunter syndrome and paves the way for similar gene therapy approaches for other genetic disorders.


---

## 73. 唯一公开出售的GM EV1，以及它的下一站

**原文标题**: The only GM EV1 ever publicly sold, and where it's going next

**原文链接**: [https://www.theautopian.com/how-the-only-gm-ev1-ever-sold-didnt-get-crushed-and-where-its-going-now/](https://www.theautopian.com/how-the-only-gm-ev1-ever-sold-didnt-get-crushed-and-where-its-going-now/)

生成摘要时出错

---

## 74. "Good engineering management" is a fad

**原文标题**: "Good engineering management" is a fad

**原文链接**: [https://lethain.com/good-eng-mgmt-is-a-fad/](https://lethain.com/good-eng-mgmt-is-a-fad/)

生成摘要时出错

---

## 75. Intel Working on Linux Support for New Power Savings Feature with Xe3P_LPD

**原文标题**: Intel Working on Linux Support for New Power Savings Feature with Xe3P_LPD

**原文链接**: [https://www.phoronix.com/news/Intel-Xe3P-LPD-System-Cache-FBC](https://www.phoronix.com/news/Intel-Xe3P-LPD-System-Cache-FBC)

生成摘要时出错

---

## 76. We Induced Smells With Ultrasound

**原文标题**: We Induced Smells With Ultrasound

**原文链接**: [https://writetobrain.com/olfactory](https://writetobrain.com/olfactory)

生成摘要时出错

---

## 77. Host a website from an old phone using PostmarketOS

**原文标题**: Host a website from an old phone using PostmarketOS

**原文链接**: [https://far.computer/how-to/](https://far.computer/how-to/)

生成摘要时出错

---

## 78. Giving the Jakks Atari Paddle a Spin

**原文标题**: Giving the Jakks Atari Paddle a Spin

**原文链接**: [https://nicole.express/2025/paddle-me-atari.html](https://nicole.express/2025/paddle-me-atari.html)

生成摘要时出错

---

## 79. Ruby Was Ready from the Start

**原文标题**: Ruby Was Ready from the Start

**原文链接**: [https://obie.medium.com/ruby-was-ready-from-the-start-4b089b17babb](https://obie.medium.com/ruby-was-ready-from-the-start-4b089b17babb)

生成摘要时出错

---

## 80. Elon Musk's Worthless, Poisoned Hall of Mirrors

**原文标题**: Elon Musk's Worthless, Poisoned Hall of Mirrors

**原文链接**: [https://www.theatlantic.com/technology/2025/11/x-about-this-account/685042/](https://www.theatlantic.com/technology/2025/11/x-about-this-account/685042/)

生成摘要时出错

---

## 81. Ubuntu LTS releases to 15 years with Legacy add-on

**原文标题**: Ubuntu LTS releases to 15 years with Legacy add-on

**原文链接**: [https://canonical.com/blog/canonical-expands-total-coverage-for-ubuntu-lts-releases-to-15-years-with-legacy-add-on](https://canonical.com/blog/canonical-expands-total-coverage-for-ubuntu-lts-releases-to-15-years-with-legacy-add-on)

生成摘要时出错

---

## 82. Show HN: Build the habit of writing meaningful commit messages

**原文标题**: Show HN: Build the habit of writing meaningful commit messages

**原文链接**: [https://github.com/arpxspace/smartcommit](https://github.com/arpxspace/smartcommit)

生成摘要时出错

---

## 83. First kiss dates back 21M years

**原文标题**: First kiss dates back 21M years

**原文链接**: [https://www.bbc.com/news/articles/cr43gq61g2qo](https://www.bbc.com/news/articles/cr43gq61g2qo)

生成摘要时出错

---

## 84. Bytes before FLOPS: your algorithm is (mostly) fine, your data isn't

**原文标题**: Bytes before FLOPS: your algorithm is (mostly) fine, your data isn't

**原文链接**: [https://www.bitsdraumar.is/bytes-before-flops/](https://www.bitsdraumar.is/bytes-before-flops/)

生成摘要时出错

---

## 85. 1M Downloads of Zorin OS 18

**原文标题**: 1M Downloads of Zorin OS 18

**原文链接**: [https://blog.zorin.com/2025/11/18/test-the-upgrade-from-zorin-os-17-to-18-and-celebrating-1-million-downloads-of-zorin-os-18/](https://blog.zorin.com/2025/11/18/test-the-upgrade-from-zorin-os-17-to-18-and-celebrating-1-million-downloads-of-zorin-os-18/)

生成摘要时出错

---

## 86. The realities of being a pop star

**原文标题**: The realities of being a pop star

**原文链接**: [https://itscharlibb.substack.com/p/the-realities-of-being-a-pop-star](https://itscharlibb.substack.com/p/the-realities-of-being-a-pop-star)

生成摘要时出错

---

## 87. Build a Compiler in Five Projects

**原文标题**: Build a Compiler in Five Projects

**原文链接**: [https://kmicinski.com/functional-programming/2025/11/23/build-a-language/](https://kmicinski.com/functional-programming/2025/11/23/build-a-language/)

生成摘要时出错

---

## 88. Why Crypto's Slide Is Rattling Wall Street

**原文标题**: Why Crypto's Slide Is Rattling Wall Street

**原文链接**: [https://www.nytimes.com/2025/11/24/business/dealbook/bitcoin-crypto-wall-street.html](https://www.nytimes.com/2025/11/24/business/dealbook/bitcoin-crypto-wall-street.html)

生成摘要时出错

---

## 89. Git 3.0 will use main as the default branch

**原文标题**: Git 3.0 will use main as the default branch

**原文链接**: [https://thoughtbot.com/blog/git-3-0-will-use-main-as-the-default-branch](https://thoughtbot.com/blog/git-3-0-will-use-main-as-the-default-branch)

生成摘要时出错

---

## 90. Several core problems with Rust

**原文标题**: Several core problems with Rust

**原文链接**: [https://bykozy.me/blog/rust-is-a-disappointment/](https://bykozy.me/blog/rust-is-a-disappointment/)

生成摘要时出错

---

## 91. Unusual circuits in the Intel 386's standard cell logic

**原文标题**: Unusual circuits in the Intel 386's standard cell logic

**原文链接**: [https://www.righto.com/2025/11/unusual-386-standard-cell-circuits.html](https://www.righto.com/2025/11/unusual-386-standard-cell-circuits.html)

生成摘要时出错

---

## 92. GCC SC approves inclusion of Algol 68 Front End

**原文标题**: GCC SC approves inclusion of Algol 68 Front End

**原文链接**: [https://gcc.gnu.org/pipermail/gcc/2025-November/247020.html](https://gcc.gnu.org/pipermail/gcc/2025-November/247020.html)

生成摘要时出错

---

## 93. Typing an AI prompt is not 'active' music creation

**原文标题**: Typing an AI prompt is not 'active' music creation

**原文链接**: [https://www.theverge.com/report/825141/sunos-ceo-ai-text-prompt-really-active-music-creation](https://www.theverge.com/report/825141/sunos-ceo-ai-text-prompt-really-active-music-creation)

生成摘要时出错

---

## 94. Show HN: Forty.News – Daily news, but on a 40-year delay

**原文标题**: Show HN: Forty.News – Daily news, but on a 40-year delay

**原文链接**: [https://forty.news](https://forty.news)

生成摘要时出错

---

## 95. Insurers retreat from AI cover as risk of multibillion-dollar claims mounts

**原文标题**: Insurers retreat from AI cover as risk of multibillion-dollar claims mounts

**原文链接**: [https://www.ft.com/content/abfe9741-f438-4ed6-a673-075ec177dc62](https://www.ft.com/content/abfe9741-f438-4ed6-a673-075ec177dc62)

生成摘要时出错

---

## 96. McDonald's is losing its low-income customers

**原文标题**: McDonald's is losing its low-income customers

**原文链接**: [https://www.latimes.com/business/story/2025-11-16/mcdonalds-is-losing-its-low-income-customers](https://www.latimes.com/business/story/2025-11-16/mcdonalds-is-losing-its-low-income-customers)

生成摘要时出错

---

## 97. Gordon Bell finalist team pushes scale of rocket simulation on El Capitan

**原文标题**: Gordon Bell finalist team pushes scale of rocket simulation on El Capitan

**原文链接**: [https://www.llnl.gov/article/53626/gordon-bell-finalist-team-pushes-scale-rocket-simulation-el-capitan](https://www.llnl.gov/article/53626/gordon-bell-finalist-team-pushes-scale-rocket-simulation-el-capitan)

生成摘要时出错

---

## 98. Personal blogs are back, should niche blogs be next?

**原文标题**: Personal blogs are back, should niche blogs be next?

**原文链接**: [https://disassociated.com/personal-blogs-back-niche-blogs-next/](https://disassociated.com/personal-blogs-back-niche-blogs-next/)

生成摘要时出错

---

## 99. Helping Valve to power up Steam devices

**原文标题**: Helping Valve to power up Steam devices

**原文链接**: [https://www.igalia.com/2025/11/helpingvalve.html](https://www.igalia.com/2025/11/helpingvalve.html)

生成摘要时出错

---

## 100. Moss Survives 9 Months in Space Vacuum

**原文标题**: Moss Survives 9 Months in Space Vacuum

**原文链接**: [https://scienceclock.com/moss-survives-9-months-in-space-vacuum/](https://scienceclock.com/moss-survives-9-months-in-space-vacuum/)

生成摘要时出错

---

