# Hacker News 热门文章摘要 (2025-10-11)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 微软放大器

**原文标题**: Microsoft Amplifier

**原文链接**: [https://github.com/microsoft/amplifier](https://github.com/microsoft/amplifier)

微软Amplifier：一款旨在提升开发者生产力的超强人工智能开发环境研究项目。它利用人工智能编码助手，这些助手通过预加载模式、专业代理和自动化进行增强，以最小的人工投入交付复杂的解决方案。

Amplifier提供20多个专业人工智能代理，用于架构设计、调试、安全分析和知识合成等任务。它包含一个知识提取系统，将文档转化为可查询的知识库；一个并行工作树系统，用于同步解决方案开发；以及会话记录，用于保留上下文。

设置过程包括安装Python、UV、Node.js、VS Code和Git，然后克隆存储库并运行安装程序。用户可以配置数据目录，用于共享知识和跨设备同步。要将Amplifier与现有项目一起使用，用户启动Claude并指定项目目录，然后指示它在那里工作，并利用专业代理处理项目的代码。

主要功能包括专业代理、用于捕获和查询项目知识的知识库、用于维护上下文的会话记录以及用于代码生成的模块化构建器工作流程。Amplifier强调最佳实践，例如理解能力与上下文之间的关系，以及使用分解策略。虽然目前不接受外部贡献，但微软设想未来人工智能将处理繁琐的任务，使开发者能够专注于创造性决策，实现自然语言驱动的系统创建和不同方法的并行探索。

---

## 2. GNU 健康

**原文标题**: GNU Health

**原文链接**: [https://www.gnuhealth.org/about-us.html](https://www.gnuhealth.org/about-us.html)

GNU Health是一个自由开源项目，致力于提供工具来改善医疗保健的可及性和质量，解决健康的社会决定因素。它包含多个组件，包括：

*   **医院管理系统 (HMIS)：** 适用于医院和医疗机构的模块化系统，涵盖电子病历 (EMR)、医院管理和健康信息系统 (HIS)。它具有针对各种医学专业的模块，并将社会经济因素与生物信息学和临床遗传学相结合。

*   **GNU LIMS (Occhiolino)：** 用于管理医疗保健和生物医学环境中实验室分析的实验室信息管理系统。

*   **MyGNUHealth：** 适用于桌面和移动设备的个人健康记录 (PHR) 应用程序，优先考虑隐私和公民对健康信息的控制，从而改善与医疗专业人员的互动。

*   **GNU Health Federation：** 一种网络，允许创建大型、联邦式的健康网络，以改善医疗保健提供者、研究机构和政府机构之间的信息共享和协作。

*   **GNU Health Embedded：** 利用单板计算机进行实时生命体征监测、数据检索和个人健康跟踪。

该项目强调社会医学，旨在解决医疗保健获取方面的不平等，并将健康视为受到营养、住房、卫生和教育等社会经济因素的严重影响。GNU Health 是一个 GNU 官方软件包，由自由软件基金会授予，并已被世界各地的医院、政府和组织采用。

---

## 3. `<output>`标签

**原文标题**: The <output> Tag

**原文链接**: [https://denodell.com/blog/html-best-kept-secret-output-tag](https://denodell.com/blog/html-best-kept-secret-output-tag)

HTML的最佳秘密：`<output>`标签

---

## 4. 开发 Ghostty 的一个重要功能

**原文标题**: Vibing a non-trivial Ghostty feature

**原文链接**: [https://mitchellh.com/writing/non-trivial-vibing](https://mitchellh.com/writing/non-trivial-vibing)

米切尔·桥本详述了他使用人工智能（特别是Amp及其“预言机”子代理）为Ghostty开发不显眼的macOS更新通知功能的经验。他强调将人工智能作为助手，补充而非取代他自己的编码专业知识。

文章回顾了几个编码过程，展示了他如何使用人工智能来原型化用户界面，最初的目标是集成到标题栏中。虽然人工智能提供了一个良好的起点，但它遇到了一个无法解决的错误，迫使桥本后退一步，研究并设计了自己的解决方案。这导致了一个转变，对于特定的标题栏样式或当标题栏隐藏时，将通知实现为窗口右下角的覆盖层。

桥本强调了与人工智能一起进行规划和迭代开发的重要性。他强调了清理代码的重要性，以确保代码质量和理解，从而改进未来的人工智能编码会话。他利用人工智能寻找灵感，甚至会丢弃生成的代码并手动重做。

文章进一步说明了如何将人工智能用于填空式任务，例如完成代码支架和修复构建错误。它还展示了人工智能在生成模拟以测试各种场景方面的实用性。在最初的后端实现遇到困难之后，对视图模型的重组对于成功的人工智能辅助至关重要。最后一步涉及使用`UpdateController`连接后端和前端。在整个过程中，桥本经常润色和改进人工智能生成的代码。

---

## 5. AMD和索尼PS6芯片组旨在重新思考当前图形管线。

**原文标题**: AMD and Sony's PS6 chipset aims to rethink the current graphics pipeline

**原文链接**: [https://arstechnica.com/gaming/2025/10/amd-and-sony-tease-new-chip-architecture-ahead-of-playstation-6/](https://arstechnica.com/gaming/2025/10/amd-and-sony-tease-new-chip-architecture-ahead-of-playstation-6/)

文章探讨了“紫水晶计划”，这是索尼和AMD之间的一项联合工程，旨在为未来的PlayStation主机（可能是PS6）开发一种新的芯片组。该计划旨在重新思考当前的图形渲染管线并提高效率，而不仅仅是依靠原始算力来蛮力渲染图形。

紫水晶计划专注于更高效地利用机器学习，特别是利用神经网络来支持诸如AMD的FSR和索尼的PSSR等超分辨率技术。它引入了“神经阵列”，使计算单元能够共享数据并像“单个专注的AI引擎”一样运作，一次处理更大的屏幕区域，从而实现对屏幕视觉效果更广泛的机器学习增强。

该项目还通过实施专用的“辐射核心”来处理光线追踪中的低效率问题，从而释放CPU和GPU用于传统的着色器计算。“辐射核心”负责光线遍历。此外，紫水晶计划还通过“通用压缩”系统来解决GPU内存带宽限制问题，旨在将有效带宽提高到超过其理论规格。

虽然该项目仍处于早期阶段，并且没有演示，但它旨在提高实时图形的真实感，让我们得以一窥索尼和AMD在推动游戏技术边界方面的优先事项。

---

## 6. 透过照片看建造中的世界贸易中心，1966-1979

**原文标题**: The World Trade Center under construction through photos, 1966-1979

**原文链接**: [https://rarehistoricalphotos.com/twin-towers-construction-photographs/](https://rarehistoricalphotos.com/twin-towers-construction-photographs/)

本文详细介绍了世界贸易中心的概念构思、建造过程以及最终的覆灭。该项目由戴维·洛克菲勒推动，旨在通过一个大型贸易设施和城市更新计划来振兴曼哈顿下城，解决城市衰败问题。纽约和新泽西港务局负责开发该建筑群，通过选择“无线电街”地块，克服了最初关于选址的分歧。建筑师山崎实，以其现代而又敏感的设计而闻名，被选中，但他的作品受到了赞扬和批评。

施工始于1966年，于1972年竣工，采用了如地下连续墙等开创性的工程技术。该项目需要大规模的挖掘，沿哈德逊河创造了新的土地。双子塔提供了大量的办公空间、零售机会和一个重要的交通枢纽。建造过程规模宏大，雇佣了数千人，但不幸的是导致了60人死亡。

除了数据之外，双子塔成为纽约市生活中不可或缺的一部分，为5万人提供了工作场所，并吸引了无数游客。它们在1993年遭遇了一次恐怖袭击，但最终在2001年9月11日被摧毁，当时恐怖分子驾驶飞机撞向了两座大楼，导致其灾难性的倒塌。本文重点介绍了导致其毁灭的渐进式倒塌机制，并使用1966-1979年的照片详细介绍了世贸中心的建造过程。

---

## 7. 超能力：我在2025年10月如何使用编码智能体

**原文标题**: Superpowers: How I'm using coding agents in October 2025

**原文链接**: [https://blog.fsck.com/2025/10/09/superpowers/](https://blog.fsck.com/2025/10/09/superpowers/)

2025年10月，作者Jesse正在使用“超能力”（Superpowers），这是一个由Claude Code 2.0.13中的“技能”（skills）驱动的编码代理系统。他开发“超能力”是为了系统化流程并更好地指导他的AI助手。“超能力”的核心是“技能”的概念，类似于增强代理能力的模块化功能。

技能在markdown文件中定义，并由代理发现，从而实现自我改进和知识获取。工作流程遵循“头脑风暴 -> 计划 -> 执行”的循环，自动创建git工作树以进行并行任务。然后，Claude使用RED/GREEN TDD将任务分配给子代理进行实施和代码审查。

一个关键方面是教Claude如何从编程书籍等资源中创建新技能。该过程包括在压力场景下使用子代理测试新技能，灵感来自说服原则。例如，测试代理判断是立即解决问题还是首先检查是否存在相应技能。该系统结合了权威和稀缺性等说服原则，以确保可靠性。

作者强调，LLM对说服原则很敏感，这些原则可用于改进工程实践，而不仅仅是破解模型。他还使用该系统从过去的对话中提取记忆，挖掘其中的技能，然后对这些技能进行压力测试。

目前还有两个关键功能正在开发中：一个与他人分享“超能力”的系统，以及记忆系统的完全集成。作者鼓励用户安装和测试“超能力”，报告错误并贡献新技能。

---

## 8. 测试来自 datablocks.dev 的两块 18TB 白标 SATA 硬盘

**原文标题**: Testing two 18 TB white label SATA hard drives from datablocks.dev

**原文链接**: [https://ounapuu.ee/posts/2025/10/06/datablocks-white-label-drives/](https://ounapuu.ee/posts/2025/10/06/datablocks-white-label-drives/)

这篇博文详细介绍了作者测试从datablocks.dev（ServerPartDeals的欧洲替代品）购买的两个18 TB白标SATA硬盘的经验。由于全SSD设置带来的“存储焦虑”以及SSD价格上涨，作者开始探索硬盘，并发现datablocks.dev的白标产品因其价格低于翻新硬盘而颇具吸引力，尽管存在轻微的外观瑕疵。

作者选择18 TB硬盘以便于替换为容易获得的WD Elements/My Book硬盘。收到包装完好的硬盘后，他们使用`badblocks`进行了彻底格式化，显示写入速度范围为275 MB/s到123 MB/s。初始SMART数据显示令人满意，表明开机时间较短。

作者认识到7200 RPM硬盘带来的噪音，便将其与SSD集成到分层存储系统中。虽然在备份期间观察到iowait增加，但总体日常性能影响很小。这些硬盘通过USB 3.0使用WD Elements/My Book适配器连接。

功耗增加了10-20W，但仍可接受。运行期间温度保持凉爽（38-42°C）。作者对总体情况表示满意，并预计硬盘至少可以使用5年，并计划主动更换一块硬盘以减轻潜在的存储池故障。他们强调了由于盘片旋转速度和内圈位置导致硬盘末端性能较慢。

---

## 9. FreeBSD 的 Windows 子系统

**原文标题**: Windows Subsystem for FreeBSD

**原文链接**: [https://github.com/BalajeS/WSL-For-FreeBSD](https://github.com/BalajeS/WSL-For-FreeBSD)

适用于 FreeBSD 的 Windows 子系统 (WSFB) 是一个实验性项目，旨在以最小的 FreeBSD 基本系统修改，在 Linux 版 Windows 子系统 2 (WSL2) 中原生运行 FreeBSD。它利用 WSL2 的开源组件来促进 FreeBSD 在 Windows 中的无缝运行。主要目标是使 FreeBSD 能够在 WSL2 架构上原生执行，最大程度地减少 FreeBSD 代码的更改，并将改进贡献回开源项目。

目前，FreeBSD 可以在 WSL2 中成功启动，并且基本功能已可运行。正在进行的工作重点是增强网络、I/O 和进程管理能力。路线图包括完整的控制台支持、网络、用户模式实用程序和集成，以及全面的文档。

鼓励通过反馈、测试结果、错误报告和讨论进行贡献。该项目在开源许可证（待定）下运作。免责声明强调 WSFB 是一个个人实验性项目，与 Microsoft 或 FreeBSD/FreeBSD 基金会无关，用户应谨慎操作。

---

## 10. 使用 C 从零开始构建 JavaScript 运行时

**原文标题**: Building a JavaScript Runtime from Scratch using C

**原文链接**: [https://devlogs.xyz/blog/building-a-javaScript-runtime](https://devlogs.xyz/blog/building-a-javaScript-runtime)

本文概述了一个使用C语言从头构建JavaScript运行时的项目。重点是通过“开发日志”提供幕后视角，深入了解开发过程。这意味着本文将以一系列按时间顺序排列的条目形式呈现，详细介绍创建功能性JavaScript环境所面临的挑战、解决方案和取得的进展。

主要目的是记录创建JavaScript运行时所涉及的复杂性，可能涵盖以下领域：

*   **解析JavaScript代码：** 实现一个解析器来理解语法。
*   **抽象语法树 (AST) 生成：** 将解析后的代码转换为AST表示形式。
*   **执行引擎：** 构建一个解释或编译AST的机制。
*   **垃圾回收：** 自动管理内存的分配和释放。
*   **标准库实现：** 提供内置函数和对象，如`console.log`。
*   **处理JavaScript的动态特性：** 动态处理类型和作用域。

“开发日志”的形式表明了一种实用、动手的方法，提供了对作者决策过程、调试技术以及项目进展过程中的迭代改进的见解。读者可以了解到实现中使用的特定工具、库（如果有）和架构选择。本质上，本文是一项重大软件工程工作的开发日记。

---

## 11. 对RSA的悄然改变

**原文标题**: A Quiet Change to RSA

**原文链接**: [https://www.johndcook.com/blog/2025/10/06/a-quiet-change-to-rsa/](https://www.johndcook.com/blog/2025/10/06/a-quiet-change-to-rsa/)

本文探讨了RSA密码学中一个细微但重要的变化，即私钥的计算方式。最初，私钥`d`是基于欧拉函数φ(n)计算的，满足`ed ≡ 1 mod φ(n)`，其中`e`是公钥指数，`n`是两个大素数`p`和`q`的乘积。

文章揭示，随着时间的推移，计算方式转变为使用卡迈克尔函数λ(n)，从而得到`ed ≡ 1 mod λ(n)`。卡迈克尔函数是满足费马小定理的最小数，并且它总是能整除欧拉函数，意味着λ(n) ≤ φ(n)。

这种改变的动机是为了生成更小的私钥，理论上可以加快解密速度。具体来说，λ(n) = lcm(p-1, q-1) = (p-1)(q-1) / gcd(p-1, q-1)，这使得它比φ(n) = (p-1)(q-1)小了一个因子gcd(p-1, q-1)。至少，这个因子是2，因为p-1和q-1都是偶数。

然而，作者的实验表明，使用卡迈克尔函数带来的实际效率提升通常很小。虽然(p-1)和(q-1)的最大公约数（GCD）可能相当大，但在实际情况下通常只有2或4。文章最后指出，其他技术，如Garner算法，可以提供更大的效率提升。因此，转向卡迈克尔函数，虽然理论上是合理的，但在许多实际应用中只提供了边际性能优势。

---

## 12. 鱼声图书馆

**原文标题**: A Library for Fish Sounds

**原文链接**: [https://nautil.us/a-library-for-fish-sounds-1239697/](https://nautil.us/a-library-for-fish-sounds-1239697/)

文章“鱼类声音图书馆”探讨了一种通过倾听鱼类发出的声音来监测海洋生态系统的新方法。FishEye合作组织正在使用摄像机和麦克风来记录和分析珊瑚礁的声音，特别是在库拉索岛。他们的目标是创建一个全面的物种特异性鱼类声音库。

传统的海洋生物研究方法，如视觉调查和环境DNA分析，在捕捉生态系统的全貌方面存在局限性。分析声音，特别是与视频结合时，可以提供关于鱼类种群的存在、行为和健康的更详细信息。FishEye合作组织的系统旨在将特定噪音分配给不同物种，本质上是创建一个“鱼类声音词典”。然后，可以将此数据与机器学习结合使用，通过它们的叫声来识别物种，类似于鸟类识别应用程序。

研究人员认为，这种声学监测可以成为保护工作的宝贵工具，特别是对于对海洋健康至关重要的珊瑚礁。了解珊瑚礁的声音可以帮助科学家追踪其健康和复原力，特别是在面对气候变化等压力因素时。通过识别海洋的“隐藏声音”，研究人员可以更全面地了解海洋生态系统。这种长期监测有助于确保保护工作的有效性。

---

## 13. 我制作了带有NFC标签的实体专辑卡片来教我儿子发现音乐。

**原文标题**: I built physical album cards with NFC tags to teach my son music discovery

**原文链接**: [https://fulghum.io/album-cards](https://fulghum.io/album-cards)

乔丹·富尔格姆为他10岁的儿子制作了带有NFC标签的实体专辑卡片，以培养积极的音乐发现，灵感来自于他自己童年收集CD的经历。他对现代流媒体被动、背景式的特性感到沮丧，因此寻求一种有形的、引人入胜的替代方案。

他设计了交易卡大小的专辑封面，最初遇到的问题是方形专辑封面不适合矩形卡片格式。他创造性地使用人工智能扩展专辑封面以适应交易卡比例，确保视觉吸引力，从而解决了这个问题。

富尔格姆随后利用NFC标签，使用PlexAmp的内置NFC标签写入功能，将每个标签编程为深度链接到他家庭Plex服务器上的特定MP3专辑。这使得卡片在被点击时可以在他们的家庭扬声器系统上触发相关专辑的播放。

他打印了专辑封面卡片，嵌入了NFC标签，并将它们展示在一个3D打印的交易卡支架上。他的儿子立刻被吸引，根据专辑封面选择专辑，并体验到主动选择和听音乐的满足感。

该项目旨在对抗被动的音乐消费，并鼓励对专辑级别的所有权和探索。富尔格姆认为该项目是成功的，他注意到他儿子的积极参与以及他女儿的热情反应，这证明了有形互动增强音乐鉴赏的潜力。

---

## 14. 重新介绍 Pebble 应用商店

**原文标题**: (Re)Introducing the Pebble Appstore

**原文链接**: [https://ericmigi.com/blog/re-introducing-the-pebble-appstore/](https://ericmigi.com/blog/re-introducing-the-pebble-appstore/)

本文宣布重新推出 Pebble 应用商店，现由 Rebble 托管于 apps.rePebble.com，Rebble 是一个自 2017 年以来一直致力于维持 Pebble 社区活力的非营利组织。与 Rebble 的合作确保了应用商店的功能，并允许开发者通过 dev-portal.rebble.io 提交新的应用程序。无需 Rebble 订阅即可访问应用商店。

该应用商店旨在通过提供各种应用程序和表盘，重现 Pebble 蓬勃发展的开发者社区的精神。已添加了诸如社交链接预览和类似应用程序推荐之类的新功能。正在考虑的未来改进包括 API 警告、更好的分类以及突出显示鲜为人知的应用程序。

本文还提供了 Pebble 2 Duo 和 Pebble Time 2 的生产更新。第一批白色 Pebble 2 Duo 即将发货，而黑色 Pebble 2 的生产面临延误。Pebble Time 2 正在推进开发阶段，计划在今年年底左右开始批量生产，这可能会推迟 12 月的预购。一项关键的软件更新允许现有应用程序缩放到更大的 Pebble Time 2 显示屏。

最后，本文鼓励开发者创建新的应用程序和表盘。SDK 已更新，并且提供基于云的 IDE。还计划增加对 SDK 的更多支持。此外，还发布了一款新的移动应用程序的 Beta 版，适用于 Android 和 iPhone。

---

## 15. 丹尼尔·卡尼曼在瑞士选择协助自杀

**原文标题**: Daniel Kahneman opted for assisted suicide in Switzerland

**原文链接**: [https://www.bluewin.ch/en/entertainment/nobel-prize-winner-opts-for-suicide-in-switzerland-2619460.html](https://www.bluewin.ch/en/entertainment/nobel-prize-winner-opts-for-suicide-in-switzerland-2619460.html)

蓝色新闻报道：诺贝尔奖得主丹尼尔·卡尼曼于2024年3月27日在瑞士选择协助自杀，享年90岁。他做出这一决定是为了避免老年精神和身体衰退，此前他目睹了像他伴侣安妮·特里斯曼（死于血管性痴呆）这样的亲人所遭受的痛苦。

卡尼曼在去世前与家人在巴黎度过了一段时间，享受生活并向亲密的朋友发送了告别邮件。他在邮件中解释了他的理由：他希望保持他的自主权和对自身结局的控制，而不是恶化到生活不再有价值的地步。他承认有些人可能会认为他的决定为时过早，但那正是他的意图。

卡尼曼不希望他的选择引发争论，他表示虽然他不感到羞耻，但他不希望公开讨论此事。他用最后的日子进行反思，享受生活和学习。他对那些帮助他使生活变得美好的人表达了感谢。文章还为有自杀念头的人以及那些因自杀而失去亲人的人提供了资源。

---

## 16. 要打多用力才能把鸡打熟？ (2020)

**原文标题**: How hard do you have to hit a chicken to cook it? (2020)

**原文链接**: [https://james-simon.github.io/blog/chicken-cooking/](https://james-simon.github.io/blog/chicken-cooking/)

文章探讨了一个看似荒谬的问题：需要多用力击打鸡才能将其煮熟。文章首先驳斥了通过拍打速度达到烹饪温度的简单计算，认为维持该温度足够的时间对于实际烹饪至关重要。

真正的挑战在于抵消鸡肉通过黑体辐射造成的热量损失。一只煮熟的鸡（165°F）大约辐射2000瓦的功率。为了保持烹饪温度，能量输入必须等于能量输出。

文章提出了一个假设场景：四个人穿着压力服，在一个真空室内，用棒球棒击打悬挂的鸡。为了煮熟鸡肉，每个人需要每秒一次以 75 英里的时速挥舞球棒击打它。这种持续的能量输入，相当于鸡肉辐射的热量损失，理论上可以在几分钟内煮熟鸡肉，展示了仅通过钝力烹饪鸡肉所需的惊人能量。

---

## 17. 缠结：一个基于atproto构建的Git协作平台

**原文标题**: Tangled, a Git collaboration platform built on atproto

**原文链接**: [https://blog.tangled.org/intro](https://blog.tangled.org/intro)

Tangled：基于AT协议的去中心化Git协作平台，旨在通过赋予开发者代码所有权和支持开源社区自治，重塑社交化和趣味性的编码体验。它通过atproto的中心化身份，结合联邦和P2P模型的优势，从而区别于其他去中心化方案。

Tangled的关键组件是“knots”，一种用于托管Git仓库的轻量级服务器。这些knots可以是单租户或多租户的，适用于自托管或大型社区服务器。Tangled还提供托管knots，用于免费的仓库托管。tangled.sh上的应用视图提供了一个统一的界面，用于访问和贡献于不同knots上的仓库。

目前处于早期阶段的Tangled，遵循三个原则：数据所有权、低准入门槛和不妥协的用户体验。该平台旨在使常见的Git工作流程在去中心化架构中也能感觉自然。

Tangled最初以邀请制推出，现在已在tangled.sh/login上公开可用。

---

## 18. 在阳光下编程：日光计算机的一年

**原文标题**: Programming in the Sun: A Year with the Daylight Computer

**原文链接**: [https://wickstrom.tech/2025-10-10-programming-in-the-sun-a-year-with-the-daylight-computer.html](https://wickstrom.tech/2025-10-10-programming-in-the-sun-a-year-with-the-daylight-computer.html)

本文详细介绍了作者使用Daylight DC-1（一款采用反射式LCD屏幕、专为阳光下可读性设计的安卓平板电脑）在户外编程的经验。作者发现，在阳光下工作可以提高他们的精力和警觉性，这在黑暗的北欧气候中尤为重要。他们的设置包括DC-1、蓝牙机械键盘、Termux（一个终端模拟器）以及SSH、tmux和Neovim等常用工具。他们很欣赏DC-1在写作和简单编程任务中的表现，并使用SSH连接到工作站进行更繁重的任务。他们使用Neovim中的Goyo进行极简设置，以实现专注写作，并使用Chrome的分屏配置进行实时博客预览。

本文还比较了DC-1和Boox Tab Ultra这两款平板电脑，后者是一款E-Ink平板电脑。虽然Boox在阅读书籍和PDF方面更胜一筹，因为它具有更清晰的显示效果和更好的可读性，但DC-1在打字和绘图方面表现出色，因为它具有更快的刷新率和更少的残影。作者指出，DC-1在阳光直射下可能会出现眩光，因此Boox更适合在床头灯下进行夜间阅读。作者甚至尝试将Boox用作辅助显示器。

最终，作者得出结论，这两款设备各有优势。Boox更适合阅读，而Daylight更适合编码和绘图。作者还表示对更大的E-Ink显示器用于工作站感兴趣，并希望未来刷新率能够有所提高。

---

## 19. AV2视频编解码器比特率比AV1低30%，最终规格预计2025年末发布。

**原文标题**: AV2 video codec delivers 30% lower bitrate than AV1, final spec due in late 2025

**原文链接**: [https://videocardz.com/newz/av2-video-codec-delivers-30-lower-bitrate-than-av1-final-spec-due-in-late-2025](https://videocardz.com/newz/av2-video-codec-delivers-30-lower-bitrate-than-av1-final-spec-due-in-late-2025)

文章报道，开放媒体联盟(AOMedia) 在AV2，即AV1视频编解码器的继任者，的开发上取得了显著进展。早期测试表明，AV2在相似视频质量下，相比AV1能够降低30%的比特率。这种改进有望带来更小的文件体积、更低的带宽消耗以及更优的流媒体体验，尤其是在较低比特率下。

AV2的最终规范预计将于2025年末完成。开发工作正在进行中，重点是编码效率、复杂性管理和硬件支持。文章强调了AV2在各种应用中的潜在优势，包括在线视频流媒体、视频会议和内容创作。降低的比特率将特别有利于带宽或数据流量有限的用户。

尽管文章并未详细介绍AV2编解码器的具体技术细节，但标题侧重于预期的比特率改进和完成时间表。文章强调了AV2进一步推动视频压缩技术并改善整体视频体验的潜力。

---

## 20. 学习 Turbo Pascal – 最初以 VHS 发布的视频系列

**原文标题**: Learn Turbo Pascal – a video series originally released on VHS

**原文链接**: [https://www.youtube.com/watch?v=UOtonwG3DXM](https://www.youtube.com/watch?v=UOtonwG3DXM)

本系列视频旨在学习Turbo Pascal，最初以VHS形式发布。内容还包含YouTube的标准页脚信息，包括以下链接：

*   **通用YouTube版块：** 新闻、关于、联系我们、创作者、广告、开发者、条款、隐私、政策与安全、YouTube运作方式、测试新功能。
*   **版权信息：** 与NFL Sunday Ticket和Google LLC相关。

核心信息是关于Turbo Pascal的学习系列。YouTube页脚的存在表明该系列在YouTube上可用或被提及。

---

## 21. 认真对待深奥的编程语言

**原文标题**: Let's Take Esoteric Programming Languages Seriously

**原文链接**: [https://feelingof.com/episodes/078/](https://feelingof.com/episodes/078/)

让我们严肃对待深奥编程语言

---

## 22. 我们对“速度的需求”让我们的无线网络变差了吗？

**原文标题**: Does our “need for speed” make our wi-fi suck?

**原文链接**: [https://orb.net/blog/does-speed-make-wifi-suck](https://orb.net/blog/does-speed-make-wifi-suck)

丹尼尔·博兹曼的文章认为，我们对Wi-Fi速度的痴迷实际上有损整体Wi-Fi体验。他认为，优先考虑原始速度而非响应性和可靠性会导致Wi-Fi路由器和网络的配置不佳。

他解释说，虽然专业的Wi-Fi网络通常使用较窄的信道宽度（5 GHz频段中的20或40 MHz）来最大化信道重用并最小化干扰，但消费级设备和ISP默认使用较宽的信道（5 GHz频段中80 MHz或更高，2.4 GHz频段中40 MHz）以获得更高的速度测试结果，从而牺牲了稳定性和响应性。这是因为消费者将“速度”等同于质量，并且可能会退回性能不佳的产品。

博兹曼进一步认为，即使是执行速度测试本身也会降低Wi-Fi体验。速度测试会造成大量的空口竞争，导致延迟、抖动和丢包增加，最终影响网络上其他设备的响应速度。他通过比较在连接笔记本电脑（通过Wi-Fi和以太网）上进行速度测试时iPhone的响应速度与空闲网络上的响应速度，证明了这一点，结果表明在使用Wi-Fi时性能明显下降。

文章总结认为，需要转变重点。消费者、媒体和行业必须认识到响应性和可靠性比纯粹的速度更重要。他赞扬IEEE 802.11bn (Wi-Fi 8) 工作组优先考虑这些因素。虽然6 GHz频段中更宽的频段会提供一些改进，但专注于配置更改和测量持续网络体验（而不仅仅是某个时间点的速度）的工具，才是改善Wi-Fi的关键。

---

## 23. 合成孔径雷达自动聚焦与校准

**原文标题**: Synthetic aperture radar autofocus and calibration

**原文链接**: [https://hforsten.com/synthetic-aperture-radar-autofocus-and-calibration.html](https://hforsten.com/synthetic-aperture-radar-autofocus-and-calibration.html)

本文探讨了合成孔径雷达（SAR）的自动聚焦和校准技术，特别关注适用于无人机载SAR系统的改进方法。作者重点介绍了一种新的SAR自动聚焦算法，该算法结合了现有方法来提高无人机平台采集的图像质量，以及天线方向图归一化和极化校准技术。

所解决的核心问题是通过校正数据采集期间雷达位置的误差来提高SAR图像质量。本文解释了使用匹配滤波的SAR图像形成过程，并强调了该过程对即使很小的位置误差的敏感性。它介绍了一种广义相位梯度自动聚焦（GPGA）算法，用于估计和校正这些误差。GPGA利用了SAR图像中点目标的恒定相位概念，使用低通滤波来改善相位误差估计并迭代细化校正。

一项关键创新是3D轨迹估计方法，该方法改编自现有研究，以解决具有宽天线波束以及目标位于不同方位角和仰角的情况。该方法将SAR图像划分为子图像，计算每个子图像中的相位误差，并将它们转换为距离误差。通过使用已知的子图像中心位置，它构建了一个超定方程组来求解3D雷达位置误差。线性化简化了解决方案，通过考虑雷达位置和目标位置之间复杂的空间关系，从而可以更准确地重建图像。

---

## 24. 火狐是最好的手机浏览器

**原文标题**: Firefox is the best mobile browser

**原文链接**: [https://kelvinjps.com/blog/firefox-best-mobile-browser/](https://kelvinjps.com/blog/firefox-best-mobile-browser/)

本文力挺 Firefox 为最佳移动浏览器，主要是因为其在安卓系统上支持强大的桌面级扩展程序。作者认为，这些扩展程序对于对抗现代网络浏览的臃肿至关重要，尤其是在资源有限的移动设备上。

作者重点介绍了几个有益的扩展程序：

*   **Ublock:** 广告拦截器，还可以移除烦人的横幅广告（如应用安装提示）、聊天小部件、时事通讯通知和 Cookie 横幅。
*   **LibRedirect:** 用于绕过不需要的网站布局，例如将 Medium 文章重定向到更简洁的 Scribe 前端，并通过 Nitter 启用在 Twitter/X 上的评论查看。
*   **Don't Fuck With Paste:** 允许用户粘贴到限制粘贴的字段中。
*   **Video Background Play Fix:** 在通常不支持的网站上启用后台音频播放。
*   **Web Archives:** 快速查找 404 页面的存档版本。
*   **Leechblock:** 通过阻止或限制对某些网站的访问，帮助用户管理他们在网络上的时间。

除了扩展程序之外，本文还赞扬了 Firefox 在桌面和移动设备之间无缝同步的能力（书签、密码等）以及其可定制的主页，用户可以在其中删除不需要的元素（如赞助内容）。作者还强调了将移动设备上的标签发送到桌面以供稍后查看的功能。总的来说，本文将 Firefox 呈现为一个强大且可定制的移动浏览器，它优先考虑用户体验和控制。

---

## 25. 展示HN：我发明了一种新的生成模型并被ICLR接收了

**原文标题**: Show HN: I invented a new generative model and got accepted to ICLR

**原文链接**: [https://discrete-distribution-networks.github.io/](https://discrete-distribution-networks.github.io/)

这个“Show HN”帖子介绍了离散分布网络（DDN），一种被ICLR 2025接收的新型生成模型。DDN使用分层离散分布来近似数据分布，与现有生成模型相比，提供了一种更简洁的原理和形式。其核心思想是同时生成多个样本，从而更有效地捕获分布信息。

训练的关键组成部分是“分裂与剪枝”优化算法。网络在每一层生成K个样本，选择最接近真实值（GT）的那个，并将其选择作为下一层的输入。此过程迭代地优化生成的图像。对于生成过程，使用随机选择代替“引导采样器”。

该帖子强调了DDN的独特属性，包括无需梯度的零样本条件生成和独特的1D潜在表示。实验证明了其在CIFAR-10和FFHQ上的有效性。作者提出了未来的研究方向，包括扩展到ImageNet、将DDN应用于具有较小生成空间的领域，以及探索其在非生成任务中的应用，例如无监督聚类和改进现有生成模型。作者还解答了关于GPU内存使用和模式崩溃的常见问题。

---

## 26. Show HN: 在浏览器中运行的咖啡烘焙机数字孪生

**原文标题**: Show HN: A Digital Twin of my coffee roaster that runs in the browser

**原文链接**: [https://autoroaster.com/](https://autoroaster.com/)

这个“Show HN”帖子介绍了AutoRoaster，它是作者的Kaleido M1咖啡烘焙机样机的基于浏览器的数字孪生。这是一个数据驱动的模拟，可以预测烘焙机和咖啡豆的物理特性，允许用户像操作真实的烘焙机一样与虚拟烘焙机进行交互。

演示允许用户：

*   **设置:** 开始前调整咖啡豆的质量 (50-200g)。
*   **添加咖啡豆:** 点击“添加咖啡豆”按钮为虚拟烘焙机装料。
*   **控制:** 在烘焙过程中调整加热器功率和风扇速度。
*   **监控:** 观察实时温度曲线和升温速率 (RoR)。

该数字孪生模拟咖啡豆探针、咖啡豆表面、滚筒和环境温度，以及环境探针温度、烘焙时间和升温速率。界面还包括加热器功率、风扇速度、咖啡豆质量和模拟速度的控制。

作者提供为其他咖啡烘焙机创建数字孪生的服务，并提供其联系方式 (james@autoroaster.com)。演示默认设置为埃塞俄比亚古吉咖啡豆、24摄氏度的环境温度、180摄氏度的预热温度和60%的滚筒速度。

---

## 27. 黑客泄露澳航500万客户数据，勒索期限已过。

**原文标题**: Hackers leak Qantas data on 5M customers after ransom deadline passes

**原文链接**: [https://www.theguardian.com/business/2025/oct/11/hackers-leak-qantas-data-containing-5-million-customer-records-after-ransom-deadline-passes](https://www.theguardian.com/business/2025/oct/11/hackers-leak-qantas-data-containing-5-million-customer-records-after-ransom-deadline-passes)

自称“零散Lapsus$猎手”的黑客组织，因勒索要求未得到满足，已在暗网上泄露了500万澳航客户的个人数据。这些数据于六月从Salesforce数据库中窃取，包括电子邮件地址、电话号码、出生日期和常旅客号码，但不包括财务详细信息和护照信息。

澳航是此次数据泄露中受影响的40家公司之一，全球可能涉及10亿条客户记录。该黑客组织以攻击具有互联系统的公司而闻名。网络安全专家Jeremy Kirk指出，盖璞、越南航空、丰田、迪士尼、麦当劳、宜家和阿迪达斯等公司也受到了影响。

澳航表示，他们正在为受影响的客户提供支持和专业的身份保护建议。Salesforce坚称其平台并未受到损害，其调查表明，此次泄露与过去或未经证实的事件有关。被盗数据收集于2024年4月至2025年9月期间，对个性化网络钓鱼攻击以及潜在的欺诈活动（如开设信用卡）构成风险。

澳航此前已获得禁令，以防止滥用被盗数据。专家建议受影响的个人监控自己的账户是否存在可疑活动，并警惕个性化的诈骗邮件。

---

## 28. 如何检查重叠区间

**原文标题**: How to Check for Overlapping Intervals

**原文链接**: [https://zayenz.se/blog/post/how-to-check-for-overlapping-intervals/](https://zayenz.se/blog/post/how-to-check-for-overlapping-intervals/)

本文探讨了如何在编程中高效地检查重叠区间和矩形（二维区间）。文章强调，检查*不*重叠通常比直接检查重叠更简单。

对于区间，文章首先提出了一种直接但复杂的方法，即识别所有可能的重叠情况并将其转化为布尔条件。然后，文章展示了一种更优雅高效的解决方案，重点关注区间*不*重叠的情况。这简化了逻辑，只需检查一个区间是否在另一个区间开始之前结束。这种“反转思路”的方法得出了一个更简单直观的条件：`other.start < self.end and self.start < other.end`。

文章随后将这一概念扩展到二维矩形。尝试直接识别重叠情况变得极其复杂。文章再次提倡关注非重叠情况，即矩形彼此位于左侧、右侧、上方或下方。这产生了一个清晰易懂的矩形重叠条件：当且仅当它们在水平和垂直方向都重叠时，矩形才重叠。

关键在于，使用否定并关注非重叠情况可以显著简化检查区间和矩形重叠所需的逻辑和代码，从而产生更易于维护且不易出错的解决方案。

---

## 29. 1700年孤儿海啸 [pdf]

**原文标题**: The Orphan Tsunami of 1700 [pdf]

**原文链接**: [https://pubs.usgs.gov/pp/pp1707/pp1707.pdf](https://pubs.usgs.gov/pp/pp1707/pp1707.pdf)

此文档似乎是一个损坏或部分编码的PDF文件，标题为“1700年的孤儿海啸”。 由于文件格式包含大量无法读取且看似随机的字符，因此无法提取实际内容或文章的主要观点。 文本包含PDF格式代码和二进制数据，表明文档的结构，但缺乏连贯的文本，导致无法进行概括。 该文件很可能已损坏、不完整或需要特定的软件或解码才能正确解释其内容。 因此，我无法从此信息中提供关于1700年孤儿海啸的摘要。

---

## 30. 展示一下：在美国国家美术馆上的语义搜索

**原文标题**: Show HN: Semantic search over the National Gallery of Art

**原文链接**: [https://nga.demo.mixedbread.com/](https://nga.demo.mixedbread.com/)

此篇“Show HN”帖子介绍了一款语义搜索工具，用于探索美国国家美术馆的藏品。该工具不只依赖关键词匹配，而是允许用户使用自然语言搜索艺术作品。帖子通过提供几个自然语言查询的例子来突出这一功能，例如“静物画”、“花卉绘画”、“风景木刻”、“女性肖像”、“动物雕塑”、“海洋绘画”和“古代钱币”。这些例子展示了该工具理解搜索查询语义含义并返回相关艺术作品的能力，使得用户可以更容易、更直观地根据主题、风格、题材或媒介来发现艺术品。重点在于展示这种语义搜索能力，作为一种新颖且用户友好的艺术收藏探索方式。

---

## 31. 反对30年期抵押贷款的理由

**原文标题**: The Case Against 30-Year Mortgages

**原文链接**: [https://www.wsj.com/opinion/the-case-against-30-year-mortgages-0cbd6d56](https://www.wsj.com/opinion/the-case-against-30-year-mortgages-0cbd6d56)

无法访问文章链接。

---

## 32. 使用 Typesense 在 Rails 中实现智能搜索

**原文标题**: Intelligent Search in Rails with Typesense

**原文链接**: [https://avohq.io/blog/intelligent-search-in-rails-with-typesense](https://avohq.io/blog/intelligent-search-in-rails-with-typesense)

本文介绍了如何在Rails应用中使用Typesense（一种快速且容错的搜索引擎）来实现智能搜索的指南。它将Typesense与基于数据库的搜索解决方案（如Ransack）进行了对比，并强调了其在性能方面的优势，尤其是在处理并发查询时。

本文介绍了Typesense的关键概念，例如文档、集合、模式、节点和集群。它解释说，Typesense最好用作辅助数据存储，索引来自主数据库的数据。

本教程将引导您构建一个简单的Rails应用程序，该应用程序显示电影列表，并带有一个由Typesense驱动的搜索栏。它涵盖了通过Docker或Homebrew安装Typesense，创建Rails应用程序，以及使用Movie、Genre和MovieGenre的模型设置数据库架构。使用AI生成的样本数据可以获得更真实的结果。

文章随后详细介绍了集成过程，包括安装Typesense Ruby gem、配置客户端、创建镜像电影数据的Typesense schema，以及索引电影。它演示了如何使用Typesense API执行基本搜索，并将此功能集成到Rails控制器中，以HTML和JSON格式响应。最后，文章提供了一个在视图中显示搜索结果的起点。

---

## 33. 兰索斯插值详解 (2022)

**原文标题**: Lánczos Interpolation Explained (2022)

**原文链接**: [https://mazzo.li/posts/lanczos.html](https://mazzo.li/posts/lanczos.html)

本文通过剖析其数学基础，解释了流行的图像缩放方法——兰索斯插值。文章首先将插值定义为一个卷积问题，其中插值函数与信号的离散样本进行卷积，以“填补”间隙。

文章介绍了辛格函数，认为它是“最佳”的插值器，因为它能够在采样率足够高时（香农-奈奎斯特定理），从离散样本中完美地重建连续信号。辛格函数在一定范围内具有恒定的频谱，并在插值过程中保留原始样本值。

然而，辛格函数无限延伸，使其在计算上不切实际，并且在处理包含不连续性的信号时表现不佳，导致吉布斯现象（振荡和“振铃”伪影）。

兰索斯插值通过将辛格函数截断到有限窗口来解决这些问题。虽然简单的截断会引入伪影，但兰索斯的关键思想是通过利用截断窗口大小与截断引入的频谱振荡频率之间的关系，来修改这个截断函数（经过调整），以抵消这些伪影。作者详细的数学解释深入了解了兰索斯插值背后的设计选择，最终与线性插值等更简单的方法相比，实现了更清晰、更少块状的图像。

---

## 34. OpenGL：当今时代的网格着色器

**原文标题**: OpenGL: Mesh shaders in the current year

**原文链接**: [https://www.supergoodcode.com/mesh-shaders-in-the-current-year/](https://www.supergoodcode.com/mesh-shaders-in-the-current-year/)

本文宣布发布OpenGL/ES的`GL_EXT_mesh_shader`扩展，这是一个重要的里程碑，也是这十年中为OpenGL发布的最大扩展。作者重点介绍了AMD所做的巨大工作，特别是牵头该项目并编写规范和核心Mesa实现的于强，以及为该扩展创建CTS案例的王世豪。文章还感谢了nvidium项目和Cortex的贡献，尤其是通过Minecraft模组。

该扩展预计很快将获得Minecraft模组支持。扩展的部分内容已经集成到Mesa中，并且正在添加Zink支持。作者优先考虑AMD对该扩展的驱动程序支持，然后再合并Zink支持，以尊重于强的工作。作者强调这是OpenGL向前迈出的重要一步，并感谢所有参与实现这一目标的人。本文写于2025年10月9日。

---

## 35. 经过九年苦耕，Replit找到了市场。它能守住吗？

**原文标题**: After nine years of grinding, Replit found its market. Can it keep it?

**原文链接**: [https://techcrunch.com/2025/10/02/after-nine-years-of-grinding-replit-finally-found-its-market-can-it-keep-it/](https://techcrunch.com/2025/10/02/after-nine-years-of-grinding-replit-finally-found-its-market-can-it-keep-it/)

Replit九年磨砺：从挣扎的初创公司到估值30亿美元

---

## 36. 瑞安航空一航班降落曼彻斯特机场，仅剩六分钟燃油。

**原文标题**: Ryanair flight landed at Manchester airport with six minutes of fuel left

**原文链接**: [https://www.theguardian.com/business/2025/oct/10/ryanair-flight-landed-at-manchester-airport-with-six-minutes-of-fuel-left-flight-log-suggests](https://www.theguardian.com/business/2025/oct/10/ryanair-flight-landed-at-manchester-airport-with-six-minutes-of-fuel-left-flight-log-suggests)

瑞安航空比萨飞往普雷斯蒂克的航班因遭遇艾米风暴期间的强风（高达每小时100英里）被迫降落在曼彻斯特机场，当时仅剩余六分钟的燃料。飞行员在普雷斯蒂克进行了三次不成功的着陆尝试后，宣布紧急求救并转飞曼彻斯特。

根据技术日志，这架波音737-800降落时仅剩余220公斤燃油。该航空公司已向当局报告了该事件，并正在配合航空事故调查局 (AAIB) 发起的调查。

乘客描述了航班的颠簸以及多次中止降落。改道导致他们到达原定目的地普雷斯蒂克延误了 10 个小时，因为他们从曼彻斯特通过其他方式被运送过去。一位经验丰富的飞行员在回顾这起事件时表示，以如此少的燃料降落“非常接近致命事故”。

---

## 37. 基于变异测试的自动化代码审查

**原文标题**: Automated code reviews via mutation testing

**原文链接**: [https://github.com/mbj/mutant](https://github.com/mbj/mutant)

Mutant 是一款自动化代码审查工具，它利用变异测试来提高代码质量并降低不必要的复杂性。它就像一位“专家开发者”，分析代码并提出简化建议，同时确保所有测试仍然通过。这些建议的简化突出了冗余代码（代码执行的操作超过测试要求）或特定需求的缺失测试。通过持续使用 Mutant，代码库变得更精简，并且对代码功能的信心也会提高。

Mutant 支持各种 Ruby 版本，具有不同级别的支持（运行时、语法、变异），并在 Linux 和 macOS 上进行了测试。 它是商业软件，但为托管在公共存储库上的开源项目提供免费使用。 商业用途需要付费订阅。

商业订阅按月或按年定价，并可根据要求提供批量订阅。 要购买商业订阅，潜在客户需要提供其业务发票地址和付款电子邮件。 欧盟客户需要有效的增值税号。

该文档随后提供了各种资源的链接，包括商业用途、命名法、阅读报告、集成指南（RSpec、Minitest）、配置以及 Discord 和 GitHub Issues 等沟通渠道。 它还感谢为特定功能做出贡献的赞助商。 最后，该文档还包括维护 Mutant 的实体 Schirp DSO LTD 的法律信息。

---

## 38. Datastar：构建交互式Web应用的轻量级超媒体框架

**原文标题**: Datastar: Lightweight hypermedia framework for building interactive web apps

**原文链接**: [https://data-star.dev/](https://data-star.dev/)

Datastar是一个轻量级的超媒体框架，旨在构建交互式Web应用程序，范围从简单站点到实时协作平台。它强调后端驱动的方法，将状态管理从前端转移到后端，从而简化前端逻辑，并通过HTML属性（data-*）提供响应式。

主要特性和优势包括：

*   **轻量级:** 使用单个10.75 KiB文件。
*   **后端灵活性:** 支持任何带有SDK的后端语言。
*   **实时功能:** 处理text/html和text/event-stream内容，从而实现流式服务器发送事件 (SSE)。
*   **降低前端复杂性:** 在许多情况下无需JavaScript，从而可以在高性能框架上更快地迭代。
*   **超媒体驱动:** 从后端修改DOM和状态，从而简化前端更新。
*   **简单设置:** 它提倡使用响应式信号通过data-attr-*属性来驱动动态内容。
*   **与其他框架的比较:** 用户将其描述为类似于React，但没有网络开销、虚拟DOM、钩子或JavaScript，但增加了多人和实时功能。它也被描述为比htmx或Alpine.js代码更少。

Datastar旨在通过提供一种更简单、更高效的方式来构建响应式实时应用程序，从而解决前端复杂性，使开发人员能够专注于解决业务问题，而不是与前端框架的复杂性作斗争。由非营利组织支持并手工编写。

---

## 39. 爱 C，恨 C：Web 框架内存问题

**原文标题**: Love C, hate C: Web framework memory problems

**原文链接**: [https://alew.is/lava.html](https://alew.is/lava.html)

本文讨论了在 Hacker News 上新发布的基于 C 的 Web 框架中发现的内存安全漏洞。作者是一位安全研究员和 C 语言爱好者，他指出了该框架解析 HTTP 请求时的一个关键缺陷，特别是关于 `Content-Length` 头部。

该漏洞源于该框架在*未进行适当验证*的情况下，根据 `Content-Length` 的值为请求体分配内存。攻击者可以提供一个大于实际请求的 `Content-Length` 值，从而在数据复制过程中（第[3]行）导致堆缓冲区溢出。这是因为代码使用攻击者控制的 `Content-Length` 作为边界，将数据从 `requestBuffer` (大小有限) 复制到 `parser.request.body` 中。

此外，作者还强调了在 `HttpRequest` 和 `HttpParser` 结构体中使用有符号整数表示长度（如 `headerCount` 和 `bodyLength`）。虽然这并非立即可以利用，但这种设计选择引发了关于负值可能造成的潜在意外行为的疑问。

文章详细说明了一个很大的 `Content-Length` (例如，4294967295) 可能导致 `malloc(0)`，而在 glibc 中会返回一个有效的指针。虽然这不会因为循环条件立即导致缓冲区溢出，但被操纵的 `request.body` 和 `bodyLength` 随后会被传递给应用程序，可能会导致后续问题。作者最后以对 C 语言的赞赏和沮丧的心情结束，强调了它的强大和简洁，但也强调了内存管理的内在风险。

---

## 40. 分子马达最大限度减少能量浪费

**原文标题**: A molecular motor minimizes energy waste

**原文链接**: [https://physics.aps.org/articles/v18/167](https://physics.aps.org/articles/v18/167)

本文探讨了研究ATP合酶能量效率的新实验，ATP合酶是一种为细胞提供能量的关键分子马达。研究人员专注于该酶的F1马达组件，使用电场而非天然的Fo马达人工驱动其旋转。他们比较了两种驱动模式：恒定扭矩和恒定旋转速率。

主要发现是，以恒定旋转速率驱动F1马达比施加恒定扭矩更节能。研究人员将此归因于在恒速旋转模式下，随机热波动的积极和消极影响得到了更好的平衡。他们模拟了这些波动如何影响系统，并指出在使用恒定扭矩时，抵抗波动对效率具有不成比例的负面影响。

结果表明一个普遍的原则：保持恒定速度可以通过抑制随机波动的影响来最大限度地减少分子机器中的能量浪费。虽然Fo马达在其天然细胞环境中的行为可能更复杂，但这项研究提供了对生物马达进化设计的见解，可能有利于更有效的机制。研究团队还进行了没有连接F1马达的对照实验，表明两种驱动模式之间的效率差异是生物活性系统特有的。

---

## 41. 闹鬼屋的超媒体即应用状态引擎

**原文标题**: HATEOAS for Haunted Houses

**原文链接**: [https://www.sanfordtech.xyz/posts/hateoas-for-haunted-houses/](https://www.sanfordtech.xyz/posts/hateoas-for-haunted-houses/)

无法访问文章链接。

---

## 42. 丘脑数据库：查询文本、表格、图像和音频

**原文标题**: ThalamusDB: Query text, tables, images, and audio

**原文链接**: [https://github.com/itrummer/thalamusdb](https://github.com/itrummer/thalamusdb)

ThalamusDB是一个近似处理引擎，它使用语义操作符扩展SQL查询，以分析存储在标准DuckDB数据库中的多模态数据，包括文本、图像和音频。它使用户能够使用自然语言执行复杂查询，并基于语义理解来过滤和连接数据。

主要功能包括`NLfilter`和`NLjoin`操作符，它们允许基于应用于包含图像和音频等非结构化数据路径的数据列的自然语言条件进行过滤和连接。该系统利用来自OpenAI和Google等供应商的语言模型，这些模型可以通过`models.json`文件进行配置，允许用户指定要用于不同模态和操作符的模型，以及温度和推理工作量等参数。

ThalamusDB优先考虑近似处理，在查询执行期间提供带有误差范围的中间结果。对于聚合查询，它显示聚合的下限和上限，而对于检索查询，它显示存在于所有可能结果中的行。该系统允许基于时间、LLM调用、token和误差阈值配置停止条件，从而提供对查询执行的控制。提供了示例查询来演示其在图像数据上的功能，评估基于图像内容的语义条件。总而言之，ThalamusDB以高效和近似的方式促进使用自然语言查询多模态数据。

---

## 43. 展示HN：熄灯游戏：我的类魔方二维游戏

**原文标题**: Show HN: Lights Out: my 2D Rubik's Cube-like Game

**原文链接**: [https://raymondtana.github.io/projects/pages/Lights_Out.html](https://raymondtana.github.io/projects/pages/Lights_Out.html)

这个 "Show HN" 帖子介绍了一个名为 "熄灯" 的 2D 类魔方益智游戏，游戏在一个 n x n 的网格上进行。目标是通过点击单元格将所有单元格变为红色，点击单元格会根据特定规则翻转其他单元格的颜色。

帖子概述了该游戏的三个变体：

*   **相邻：** 点击一个单元格会翻转其颜色以及其北、东、南、西邻居的颜色。
*   **同行同列：** 点击一个单元格会翻转同一行和同一列中所有单元格的颜色。
*   **对角线：** 点击一个单元格会翻转共享同一对角线的所有单元格的颜色。

作者提到了 "同行同列" 规则下的一般解谜策略，特别是当 'n'（网格大小）是奇数或偶数时，但不知道其他变体的通用策略，并邀请读者分享他们发现的任何策略。

该游戏使用 TypeScript 在严格模式下实现，利用了静态类型检查、联合类型和接口。作者还提供了一个使用 Manim 制作的预告视频，并提供了该项目的完整 GitHub 存储库的链接。

---

## 44. 大野字体学校：A (2020)

**原文标题**: Ohno Type School: A (2020)

**原文链接**: [https://ohnotype.co/blog/ohno-type-school-a](https://ohnotype.co/blog/ohno-type-school-a)

这篇博文《Ohno字体学校：A》是字体排印系列文章的一部分，重点关注字母“A”以及偏离严格几何的设计原则。作者认为，严格遵守几何规则，例如将“A”的横杠居中，会导致不美观的“高腰”外观。

相反，关键在于优先考虑负空间中的平衡——横杠上方和下方的区域。这些空间的大小应该大致相等，以创造视觉和谐。

这篇文章还探讨了连接处的笔画粗细问题，解释说均匀的粗细会在视觉上产生沉重的连接。相反，作者建议在连接处巧妙地减细笔画，以获得更精致和平衡的外观。这种减细不应决定对比度。

总而言之，本文旨在告诫读者不要盲目遵循字体排印中的几何规则。作者强调视觉判断的重要性，强调如果某些东西*看起来*不对，那它很可能就是*不对*的。这篇博文使用幽默和非正式的语言来使该主题易于理解，并包含一个号召性用语，鼓励读者在《OH no Book!》中了解更多信息。它是更大系列的一部分，下一篇文章将重点关注字母“B”。

---

## 45. 有争议的Hinge约会应用破解方法正在疯传

**原文标题**: The Controversial Hinge Dating App Hack Going Viral

**原文链接**: [https://www.thecut.com/article/how-to-hack-hinge-rose-jail.html](https://www.thecut.com/article/how-to-hack-hinge-rose-jail.html)

这篇文章探讨了一种旨在操纵Hinge约会应用程序算法的爆红“技巧”。许多用户认为该算法已变得掠夺性，倾向于付费功能而非真正的匹配。TikTok用户Eve Tilley-Coulson推广的这个技巧包括删除你的个人资料，然后在周日使用付费的“超级推广”，但24小时内不要使用该应用程序。然后，在一周内拒绝应用程序上的所有人（包括“优秀用户”选项卡中的用户），以向Hinge发出你很受欢迎的信号。理论是，通过拒绝个人资料，该算法会将你的个人资料展示给更广泛的用户，从而增加匹配。

Tilley-Coulson认为Hinge利用用户数据来榨取金钱，并反对在你的个人资料中过于具体，以避免被归类。这篇文章还强调了吸引尽可能广泛受众的争议性方面，这可能需要女性迎合男性凝视。

虽然一些用户报告说该技巧取得了成功，包括增加了匹配和约会，但另一些用户则经历了喜忧参半或负面的结果，遇到了不合适的匹配或缺乏真正的联系。最终，这篇文章表明，虽然该技巧可以提高可见度，但它无法解决约会的基本挑战，例如性格冲突、不靠谱的行为以及建立持久关系的困难。具有讽刺意味的是，即使是“Hinge技巧的花衣魔笛手”Tilley-Coulson，在她通过该应用程序找到伴侣后不久，就被Hinge永久禁止了。

---

## 46. NanoMi：源开放透射电子显微镜

**原文标题**: NanoMi: Source-available transmission electron microscope

**原文链接**: [https://nanomi.org/](https://nanomi.org/)

NanoMi是由加拿大国家研究委员会(NRC)开发的开源透射电子显微镜(TEM)、扫描透射电子显微镜(STEM)和扫描电子显微镜(SEM)平台，并公开发布以促进显微技术的发展。它采用模块化设计，适用于超高真空环境，易于修改和添加到现有系统中。该项目鼓励贡献，要求对修改和更新以开源许可证的形式回馈社区。

蓝图可应要求提供，并通过NRC获取。NanoMi GitHub仓库托管讨论内容和软件组件，可在GPL v3许可证下下载。开放科学基金会(OSF)网站提供关于该项目的更多信息。

最近的更新包括Mark于2023年12月在Libre HUB的演讲，以及由Xuanhao、ChatGPT和Suno AI创作的NanoMi主题曲。如需更多信息或索取蓝图，请联系NRC.NanoMi.CNRC@nrc-cnrc.gc.ca。 NanoMi项目旨在促进显微技术领域的开放科学和协作开发。

---

## 47. 少量样本即可毒害任意规模的LLM。

**原文标题**: A small number of samples can poison LLMs of any size

**原文链接**: [https://www.anthropic.com/research/small-samples-poison](https://www.anthropic.com/research/small-samples-poison)

本文报道了Anthropic、英国人工智能安全研究所和艾伦·图灵研究所的一项联合研究，该研究表明，无论大型语言模型（LLM）的规模或训练数据量如何，都可以通过数量少得惊人的恶意文档成功地对其进行投毒攻击。研究发现，只需注入少至250个包含特定触发短语(<SUDO>)和无意义文本的投毒文档，就可以创建一个“后门”漏洞，导致模型（参数范围从6亿到130亿）在遇到触发短语时输出随机文本。

这一发现挑战了长期以来的假设，即攻击者需要控制一定比例的训练数据才能使投毒攻击有效。该研究表明，投毒文档的绝对数量比其相对于总训练数据的比例更为关键。研究人员选择了一种“拒绝服务”攻击（产生无意义文本）作为一种简单、可衡量的目标。

虽然测试的具体后门被认为是低风险的，但研究人员分享他们的发现是为了强调数据投毒攻击的潜在可行性，并鼓励进一步研究，既要了解这些漏洞，又要开发有效的防御措施。他们承认公开这些信息的风险，但认为这对于推动开发更强大的数据投毒防御措施至关重要，特别是那些可以在少量投毒样本的情况下大规模工作的防御措施。该研究还探讨了投毒顺序的影响以及模型微调过程中的漏洞。

---

## 48. Nue 2.0 Beta 发布！Web 的 Unix

**原文标题**: Nue 2.0 Beta released! The Unix of the web

**原文链接**: [https://nuejs.org/blog/2.0/](https://nuejs.org/blog/2.0/)

Nue 2.0 Beta版发布：仅1MB的完整Web开发环境。这个“Web领域的Unix”由专注于特定任务的小型工具构建，包括：Nuekit、Nuedom、Nuestate、Nuemark、Nueserver 和 Nueglow。此新版本完全重写，优先考虑简洁性和性能，并且现在仅支持 Bun。

主要变更包括使用 doctype 定义页面类型（服务器渲染、动态等）的更灵活的 HTML 模板系统，以及消除外部依赖，从而完全控制堆栈。

新功能包括带有 HMR 的 SVG 模板处理、自动站点地图生成、RSS 订阅创建，以及利用 Nuestate 进行 URL 优先状态管理的新 SPA 开发模型。新工具包括用于状态管理的 Nuestate、用于边缘优先后端开发的 Nueserver 以及服务器代理选项。提供四个新模板：minimal、blog、spa 和 full。

切换到 Bun 可以提高性能和简化操作。Nue 2.0 不向后兼容，需要本地安装进行测试，然后才能全局采用。目前已在 macOS 上测试，Linux 和 Windows 兼容性尚不确定。文章提供了安装 Bun 和 Nuekit、创建新项目以及启动开发服务器的说明。

---

## 49. 北川，化无用为有用，荣获诺贝尔奖

**原文标题**: Kitagawa, who found a use for the useless, wins the Nobel Prize

**原文链接**: [https://www.asahi.com/ajw/articles/16081940](https://www.asahi.com/ajw/articles/16081940)

朝日新闻报道了北川进因其在金属有机框架（MOFs）方面的开创性工作而获得诺贝尔化学奖。 北川是京都大学的杰出教授，他发现了MOFs，这种材料具有微小且有序的孔隙，能够吸收各种气体，使其可用于应对气候变化和革新能源存储。

这项发现大约在1990年左右，最初因当时普遍认为附着在金属上的有机化合物太不稳定而受到批评。 北川坚持不懈，将MOF的应用扩展到气体分离和转化。 他将自己的灵感归功于老庄的“无用之用”概念，专注于材料中看似空虚的孔隙。

北川设想了一个未来，MOFs可以通过从空气中提取资源来为能源独立做出贡献，从而有可能消除基于资源的冲突。 他认为，在固体（煤）和液体（石油）时代之后，人类正在进入“气体时代”。

文章突出了北川的愿景、毅力和对团队的感激之情。 他强调了准备充分的头脑和珍惜经验的重要性，引用了路易斯·巴斯德的话。 文章还描述了他实验室中积极的氛围，其特点是协作、平等主义以及偶尔的聚餐和饮酒。 北川的同事们对他的成就表示高兴。

---

## 50. Igalia、Servo 与主权技术基金

**原文标题**: Igalia, Servo, and the Sovereign Tech Fund

**原文链接**: [https://www.igalia.com/2025/10/09/Igalia,-Servo,-and-the-Sovereign-Tech-Fund.html](https://www.igalia.com/2025/10/09/Igalia,-Servo,-and-the-Sovereign-Tech-Fund.html)

Igalia，Servo网络引擎的管理者，宣布获得主权技术基金的委托，将在三个关键领域推进该引擎的开发：可访问性、可嵌入性和可持续性。Servo是一个用Rust编写的现代并行化网络引擎，提供对Rust生态系统有价值的模块化设计，但需要持续投资才能充分发挥其潜力。

主权技术基金的投资将使Igalia能够专注于：

*   **初始可访问性支持：** 实现基础可访问性功能，以支持屏幕阅读器和辅助技术，使Servo对所有用户可用，并适用于面向公众的应用程序。

*   **WebView API：** 完成WebView API，使Servo可嵌入到桌面和移动应用程序中，从而解锁新的用例，并使其作为通用引擎得到更广泛的应用。

*   **项目维护：** 提供问题分类、拉取请求审查、版本发布和治理支持，以确保Servo保持活跃、响应迅速，并为开发者和用户提供良好的维护。

Igalia 相信 Servo 在网络引擎的未来发展中具有独特的作用，并致力于在主权技术基金的支持下指导其下一个篇章。 公司将随着工作的进展分享进度更新。

---

## 51. 从 Vim 切换到 Helix 的注意事项

**原文标题**: Notes on switching to Helix from Vim

**原文链接**: [https://jvns.ca/blog/2025/10/10/notes-on-switching-to-helix-from-vim/](https://jvns.ca/blog/2025/10/10/notes-on-switching-to-helix-from-vim/)

本文详述了作者在使用 Vim 长达 20 年后，切换到 Helix 文本编辑器的经历。由于 Helix 易于设置语言服务器，作者对 Helix 内置的语言服务器支持、带上下文的增强搜索功能以及有用的快速参考弹出窗口表示赞赏。

作者为 Vim 用户提供了一份“转换指南”，指出 Ctrl+O 和 Ctrl+I 可以替代标记，多光标优于宏，并且 Helix 使用缓冲区切换器代替选项卡。

作者指出了几个令人烦恼之处，包括不太令人满意的文本重排、无法在 Markdown 中自动继续列表、缺少持久撤消、手动文件重载以及偶尔发生的崩溃。尽管存在这些缺点，作者仍然继续使用 Helix，表明这些问题并非无法克服。

过渡过程出乎意料地顺利，作者建议拥抱“Helix 方式”，而不是强行使用 Vim 键绑定。他们还通过为每个项目分配一个窗口并优先考虑 Helix 选项卡，来调整他们的终端工作流程。

作者强调了其 Helix 配置的简单性，主要包括键绑定调整和特定于语言的设置。他们还提供了一个如何禁用 Python 自动格式化的例子。

虽然承认他们将来可能会回到 Vim，但作者目前对 Helix 感到满意，欣赏它的易用性和开箱即用的功能。

---

## 52. 我研究股票市场API的结果

**原文标题**: My Results from Researching Stock Market APIs

**原文链接**: [https://old.reddit.com/r/fintech/comments/1mpm9ck/gathered_some_real_data_on_stock_apis_like/](https://old.reddit.com/r/fintech/comments/1mpm9ck/gathered_some_real_data_on_stock_apis_like/)

无法访问文章链接。

---

## 53. 利用弗兰克·赫伯特的《沙丘》进行全天然地球工程

**原文标题**: All-natural geoengineering with Frank Herbert's Dune

**原文链接**: [https://www.governance.fyi/p/all-natural-geoengineering-with-frank](https://www.governance.fyi/p/all-natural-geoengineering-with-frank)

本文论证了利用受弗兰克·赫伯特《沙丘》启发的基于自然的解决方案，来进行地球工程和应对气候变化。它强调了“生命即技术”的理念，认为生命能够在行星尺度上进行自我调节和适应，类似于盖亚假说。文章批评了长期生态项目缺乏基础设施和政治意愿。

重点在于利用自然系统进行水文和海岸管理，并提供相关案例和组织：

*   **水文：** 海狸及其筑坝行为充当天然的蓄水和过滤系统。海狸坝类似物 (BDAs) 用于模仿海狸坝，鼓励海狸回归。生物洼地和雨水花园可以过滤雨水径流，补充地下水，并缓解城市热岛效应。印度的Johads是社区拥有的集水系统，可以恢复河流和提高地下水位。利用原生植物的旱地景观可以减少用水量。

*   **海岸与生态系统工程：** 牡蛎礁可以过滤水体，提供栖息地，并减弱波浪能量。红树林提供重要的防风暴服务，储存大量的碳，并提供海洋栖息地。

文章强调了这些解决方案的经济效益，包括降低灾害恢复成本，以及重视生态系统服务对于可持续基础设施发展的重要性。它还展示了致力于牡蛎礁和红树林恢复的创新技术和组织。

---

## 54. 越南航空数据泄露

**原文标题**: Vietnam Airlines Data Breach

**原文链接**: [https://haveibeenpwned.com/Breach/VietnamAirlines](https://haveibeenpwned.com/Breach/VietnamAirlines)

2025年6月，越南航空因Salesforce环境遭到入侵而发生数据泄露。“分散的LAPSUS$猎手”黑客组织窃取了数据，并在2025年10月公开了这些数据。总计750万个唯一的客户电子邮件地址以及姓名、电话号码、出生日期和常旅客计划会员信息遭到泄露。

此次泄露影响了约730万个账户，并于2025年10月11日被添加到HIBP（Have I Been Pwned）数据库中。

建议使用过越南航空服务的人员立即采取行动：

*   **更改您的越南航空密码**，如果您自2025年以来尚未更改过。
*   **在您的越南航空账户上启用双重身份验证**，以增加一层额外的安全保障。

文章还包括密码管理器（1Password）、身份盗窃保护（Aura）和人工智能在线安全（Guardio）的赞助推荐，以帮助用户在数据泄露后保护其账户和个人信息。

---

## 55. 无需穿戴设备，Wi-Fi信号追踪心跳

**原文标题**: Wi-fi signal tracks heartbeat without wearables

**原文链接**: [https://spectrum.ieee.org/wi-fi-signal-heartbeat-detection](https://spectrum.ieee.org/wi-fi-signal-heartbeat-detection)

加州大学圣克鲁兹分校的研究人员开发了一种名为Pulse-Fi的系统，该系统可以使用现有的Wi-Fi信号远程检测人的心跳。这无需佩戴设备或直接接触即可进行心脏监测。该技术提供了一种非接触式测量脉搏率的方法。这一进步为心脏监测开辟了新的可能性，有望在医疗保健和健康领域带来创新，而无需侵入式或不方便的穿戴设备。

---

## 56. Python 3.14 发布了，速度有多快？

**原文标题**: Python 3.14 is here. How fast is it?

**原文链接**: [https://blog.miguelgrinberg.com/post/python-3-14-is-here-how-fast-is-it](https://blog.miguelgrinberg.com/post/python-3-14-is-here-how-fast-is-it)

本文对比了 Python 3.14 与之前版本、PyPy、Node.js 和 Rust 的性能，重点关注纯 Python 代码。作者强调了通用基准测试的局限性，但突出了 Python 3.14 中的性能改进。

测试包括在 Linux 和 macOS 上进行的单线程和多线程 Fibonacci 序列计算以及冒泡排序算法。Python 3.14 相比 3.13 表现出明显的提速，自 3.11 以来的版本明显快于旧版本。PyPy 始终优于 CPython，速度可与 Node.js 相媲美，而 Rust 仍然是最快的。

文章还评估了 CPython 3.13 和 3.14 的即时编译（JIT）和自由线程（FT）变体。JIT 解释器在这些测试中没有提供显著的性能提升。然而，自由线程解释器在多线程场景中表现出显著的改进，尤其是在 Python 3.14 中，使其适用于 CPU 密集型、多线程应用程序。

作者得出结论，CPython 3.14 是最快的 CPython 版本，建议升级到 3.11 及以上版本。JIT 解释器需要进一步开发，而自由线程解释器对特定工作负载有益。最后，PyPy 的出色速度得到了再次确认。

---

## 57. 科技巨头市值蒸发7700亿美元，纳斯达克遭遇四月以来最大跌幅

**原文标题**: Tech megacaps lose $770B in value as Nasdaq suffers steepest drop since April

**原文链接**: [https://www.cnbc.com/2025/10/10/tech-megacaps-market-cap-mag-7.html](https://www.cnbc.com/2025/10/10/tech-megacaps-market-cap-mag-7.html)

科技巨头遭遇重挫，市值蒸发7700亿美元，导致纳斯达克跌幅达3.6%，创下自四月以来的最大跌幅，标普500指数下跌2.7%。 主要原因是特朗普总统威胁要提高对中国商品的关税，随后又宣布自11月1日起对关键软件征收100%的关税并实行出口管制。

英伟达、亚马逊和特斯拉的股价均下跌约5%。 仅英伟达的市值就缩水近2290亿美元。 微软的市值下降了850亿美元。 亚马逊的损失抹去了今年的涨幅，使其在2025年下跌2%，当天市值损失1210亿美元。 特斯拉的市值减少了710亿美元。 谷歌母公司Alphabet和Meta也经历了下跌。

此次下跌中断了科技行业持续的上涨势头，此前的上涨得益于对人工智能基础设施的大量投资。 亚马逊首席执行官安迪·贾西此前曾表达过对关税影响零售价格和消费的担忧，这些担忧再次浮出水面。 文章还提到了英伟达在人工智能训练用GPU领域的主导地位，OpenAI的Sora 2视频创作应用和ChatGPT的需求日益增长，以及特斯拉、微软和英伟达即将发布的财报。

---

## 58. 如何用ZFS和12个U盘拯救世界：四周年纪念视频（2011）

**原文标题**: How to save the world with ZFS and 12 USB sticks: 4th anniversary video (2011)

**原文链接**: [https://constantin.glez.de/posts/2011-01-24-how-to-save-the-world-with-zfs-and-12-usb-sticks-4th-anniversary-video-re-release-edition/](https://constantin.glez.de/posts/2011-01-24-how-to-save-the-world-with-zfs-and-12-usb-sticks-4th-anniversary-video-re-release-edition/)

此博文庆祝作者和同事创作的热门视频四周年，该视频展示了 ZFS 和 Sun X4500 服务器的强大功能。 该视频演示了如何使用 12 个 USB 棒创建 ZFS 阵列，已被下载超过 10 万次，并在演示中得到广泛应用。

作者指出，由于 YouTube 和 Google Video 等平台的限制，以及原始 Sun Mediacast 服务器的退役，该视频已重新上传到 Vimeo，提供英语和德语版本。 提供了指向原始 CSI:Munich 博客文章（英语和德语）的链接，这些文章解释了视频的技术背景。

该文章强调了 ZFS 持久的价值和创新性，突出了其易于配置、数据完整性、类似数据库的事务安全性以及全面的功能集。 作者强调，没有其他文件系统提供相同的功能和优势组合，并对 ZFS 的持续发展和不断扩展的可能性表示兴奋。

---

## 59. 使用PyTorch在Windows上用AMD部署LLM的初学者指南

**原文标题**: A beginner's guide to deploying LLMs with AMD on Windows using PyTorch

**原文链接**: [https://gpuopen.com/learn/pytorch-windows-amd-llm-guide/](https://gpuopen.com/learn/pytorch-windows-amd-llm-guide/)

本文《使用PyTorch在Windows上用AMD部署LLM新手指南》侧重于利用AMD硬件部署大型语言模型（LLM）。虽然提供的片段未详细说明具体的“新手指南”方面，但核心信息围绕着在AMD Radeon GPU上加速生成式AI。

关键点包括：

*   **AMD优化的ONNX模型：** 这些模型可在Hugging Face上找到，专为AMD Ryzen AI APU和Radeon GPU设计。
*   **性能提升：** 该文章强调了AMD Radeon RX 9000系列可实现的显著性能提升，并强调了其先进的AI加速器。

本质上，本文旨在利用预优化模型和新硬件来提高在使用带有PyTorch的Windows平台上AMD产品时LLM部署的速度和效率。这意味着开发者可以通过利用这些特定的AMD资源来体验增强的生成式AI性能。

---

## 60. 铁路的产品是时刻表。

**原文标题**: The product of the railways is the timetable

**原文链接**: [https://springbett.substack.com/p/the-product-of-the-railways-is-the](https://springbett.substack.com/p/the-product-of-the-railways-is-the)

无法访问文章链接。

---

## 61. Google安全浏览事件

**原文标题**: Google Safe Browsing incident

**原文链接**: [https://www.statichost.eu/blog/google-safe-browsing/](https://www.statichost.eu/blog/google-safe-browsing/)

2025年9月25日，整个statichost.eu域名因欺骗性内容被Google安全浏览标记，持续约六小时，影响了依赖Google安全搜索的用户访问，甚至波及到托管在该平台上的自定义域名。statichost.eu的作者在用户报告访问该网站时出现安全警告后发现了这个问题。

调查显示，statichost.eu子域名结构上涌现大量钓鱼网站，导致Google将整个域名列入黑名单。虽然Google提供了违规网站列表，这些网站也已被迅速删除，但与Google沟通解决问题却无从入手，只能依靠“请求审核”按钮。最终，封锁通过Search Console中的自动回复解除。

作者对此事件表达了对Google在互联网上权力与控制的担忧。Google安全浏览旨在保护用户，但它实质上是一个通过监控用户活动（主要通过Google Chrome）构建的庞大黑名单。作者承认黑名单的实用性，但也质疑Google作为救世主的角色，并强调在互联网上浏览时独立判断和批判性思维的重要性。为了减轻类似事件的未来影响，statichost.eu现在使用statichost.page域名来托管新网站，并寻求加入公共后缀列表。

---

## 62. ScribeOCR – 文本识别、OCR 及数字化文档创建的 Web 界面

**原文标题**: ScribeOCR – Web interface for recognizing text, OCR, & creating digitized docs

**原文链接**: [https://github.com/scribeocr/scribeocr](https://github.com/scribeocr/scribeocr)

ScribeOCR是一款免费的、基于网络的应用程序，专为光学字符识别(OCR)、校对和创建数字化文档而设计。它以其对准确性和高效校对的关注而著称。

该工具主要有三个用例：通过添加准确的文本层来创建可搜索的PDF、校对现有的OCR数据以及生成完全数字化的电子书式文档。与其他只是在图像上叠加文本的OCR程序不同，ScribeOCR旨在准确复制原始文档，同时保持较小的文件大小。

一个关键特性是其高效的校对界面。它将可编辑的OCR文本精确地覆盖在源图像上，突出显示潜在的错误。它甚至为每个文档生成自定义字体，优化对齐并使错误更明显，从而显著减少校对时间。

虽然识别依赖于Scribe.js库（可在其自己的存储库中找到），但ScribeOCR提供了一个用户友好的界面，用于纠错和数字化。它可以通过scribeocr.com访问，完全在浏览器中运行，或者使用npm在本地运行。根据用户需求，桌面应用程序正在考虑中。全面的用户文档可在docs.scribeocr.com上找到。

---

## 63. 展示HN：开源、逻辑多主PostgreSQL复制

**原文标题**: Show HN: Open source, logical multi-master PostgreSQL replication

**原文链接**: [https://github.com/pgEdge/spock](https://github.com/pgEdge/spock)

本文档介绍 Spock，一个用于多主逻辑复制的开源 PostgreSQL 扩展（版本 15+）。 它涵盖了先决条件、构建、配置和使用方法。

**要点：**

*   **

---

## 64. 示例是最好的文档。

**原文标题**: Examples are the best documentation

**原文链接**: [https://rakhim.exotext.com/examples-are-the-best-documentation](https://rakhim.exotext.com/examples-are-the-best-documentation)

作者认为，示例往往是开发者最有效的文档形式，但官方文档却经常缺乏示例。他们指出，正式的技术文档通常针对已经深入了解生态系统的专家，对于同时处理多个项目并需要快速理解函数用法的开发者来说，这毫无帮助。

作者以Python的`max()`函数文档为例，强调了其详细的解释需要大量的先验知识，并且对于仅仅需要快速使用示例的人来说可能过于复杂。然后，他们提供了清晰简洁的示例，展示了该函数在不同输入和自定义排序函数下的用法，表明了理解起来有多么容易。

作者赞扬了clojuredocs.org，一个社区驱动的Clojure文档网站，因为它专注于提供实用的示例。他们强调这些示例对于日常编码是多么宝贵，并且经常包含相关函数，从而增加了它们的实际应用性。

作者最后指出，官方文档中缺乏示例常常导致他们寻找教程，即使他们只需要简单的用法演示。他们表达了对官方“文档”链接的普遍犹豫，因为他们期望看到的是简洁的、自动生成的、缺乏实用示例的API参考。

---

## 65. 缠绕：一个基于ATProto和Git构建的社交编码平台

**原文标题**: Tangled: A social coding platform built with ATProto and Git

**原文链接**: [https://tangled.org/](https://tangled.org/)

Tangled 是一个基于 ATProto 协议构建的全新社交编程平台，旨在使编程更具社交性、更有趣，并赋予开发者完整的代码所有权，同时实现开源社区的自治。它是一个促进紧密型社交编程环境的 Git 协作平台。

主要功能包括：

*   **轻量级 Git 仓库托管（结）：** 允许用户使用“结”（一种小型的无头服务器，用于促进 Git 操作）在自己的基础设施上托管仓库。 这包括基于角色的访问控制和 SSH 支持。
*   **改进的 Pull Request 模型：** 使用基于回合的 Pull Request 流程，通过 Jujutsu 变更 ID 实现内部差异化和堆叠 Pull Request，允许通过 git diff 或 git format-patch 进行快速更改。
*   **管道（纺锤）：** 允许用户使用“纺锤”（一种轻量级 CI 运行器，具有原生 Nix 支持和不同执行后端的可扩展性）在自己的基础设施上运行管道。
*   **单体仓库：** Tangled 项目本身是使用单体仓库与社区公开构建的。

文章还重点介绍了平台上的热门仓库，如 `@leaflet.pub/leaflet`、`@danabra.mov/typelex` 和 `@slices.network/slices`，以及时间线中的最新活动，例如加星标和创建事件。 本质上，Tangled 旨在提供一个去中心化、社交化、以开发者为中心的传统代码托管平台的替代方案。

---

## 66. 我构建大型技术项目的方法 (2023)

**原文标题**: My approach to building large technical projects (2023)

**原文链接**: [https://mitchellh.com/writing/building-large-technical-projects](https://mitchellh.com/writing/building-large-technical-projects)

Mitchell Hashimoto 的文章概述了他解决大型技术项目的方法，强调持续进展和切实成果对于保持积极性的重要性。 他提倡将大型任务分解为更小、更易于管理的块，从而带来可演示的成果，从而能够频繁地“演示”工作功能。

Hashimoto 强调，开始往往是最困难的部分，并建议关注可以快速交付可见结果的子项目，例如解析终端转义序列或渲染基本窗口。 他强调在早期阶段进行自动化测试的价值，以提供反馈和成就感。

他方法的核心是“冲刺到演示”，优先考虑进度而不是完美。 他建议不要陷入未来的改进中，并鼓励专注于构建一个“足够好”的子组件，以便继续进行下一个组件。 这些演示即使不是“最小可行产品”，也能尽早提供宝贵的产品反馈。

对于个人项目，他强调为自己构建，尽快采用该软件，并优先考虑直接满足个人需求的功能。 这种方法确保项目保持相关性和动力。

总而言之，Hashimoto 提倡分解、演示驱动开发和迭代改进的循环，优先考虑个人需求并专注于有形成果，以在整个项目生命周期中保持积极性。 他最后说，每个人都需要找到一种以健康的方式加强他们动力的过程。

---

## 67. 硬件斯德哥尔摩综合征

**原文标题**: Hardware Stockholm Syndrome

**原文链接**: [https://programmingsimplicity.substack.com/p/hardware-stockholm-syndrome](https://programmingsimplicity.substack.com/p/hardware-stockholm-syndrome)

无法访问文章链接。

---

## 68. Liquid Glass Is Cracked, and Usability Suffers in iOS 26

**原文标题**: Liquid Glass Is Cracked, and Usability Suffers in iOS 26

**原文链接**: [https://www.nngroup.com/articles/liquid-glass/](https://www.nngroup.com/articles/liquid-glass/)

生成摘要时出错

---

## 69. A major evolution of Apple Security Bounty

**原文标题**: A major evolution of Apple Security Bounty

**原文链接**: [https://security.apple.com/blog/apple-security-bounty-evolved/](https://security.apple.com/blog/apple-security-bounty-evolved/)

生成摘要时出错

---

## 70. Show HN: Gitcasso – Syntax Highlighting and Draft Recovery for GitHub Comments

**原文标题**: Show HN: Gitcasso – Syntax Highlighting and Draft Recovery for GitHub Comments

**原文链接**: [https://github.com/diffplug/gitcasso](https://github.com/diffplug/gitcasso)

生成摘要时出错

---

## 71. My first contribution to Linux

**原文标题**: My first contribution to Linux

**原文链接**: [https://vkoskiv.com/first-linux-patch/](https://vkoskiv.com/first-linux-patch/)

生成摘要时出错

---

## 72. The illegible nature of software development talent

**原文标题**: The illegible nature of software development talent

**原文链接**: [https://surfingcomplexity.blog/2025/10/08/the-illegible-nature-of-software-development-talent/](https://surfingcomplexity.blog/2025/10/08/the-illegible-nature-of-software-development-talent/)

生成摘要时出错

---

## 73. Parallelizing Cellular Automata with WebGPU Compute Shaders

**原文标题**: Parallelizing Cellular Automata with WebGPU Compute Shaders

**原文链接**: [https://vectrx.substack.com/p/webgpu-cellular-automata](https://vectrx.substack.com/p/webgpu-cellular-automata)

生成摘要时出错

---

## 74. Hacker News Live Feed

**原文标题**: Hacker News Live Feed

**原文链接**: [https://jerbear2008.github.io/hn-live/](https://jerbear2008.github.io/hn-live/)

生成摘要时出错

---

## 75. Using a laptop as an HDMI monitor for an SBC

**原文标题**: Using a laptop as an HDMI monitor for an SBC

**原文链接**: [https://danielmangum.com/posts/laptop-hdmi-monitor-sbc/](https://danielmangum.com/posts/laptop-hdmi-monitor-sbc/)

生成摘要时出错

---

## 76. ESP32 and Termux

**原文标题**: ESP32 and Termux

**原文链接**: [https://blog.gavide.dev/blog/esp32-and-termux](https://blog.gavide.dev/blog/esp32-and-termux)

生成摘要时出错

---

## 77. Origami Patterns Solve a Major Physics Riddle

**原文标题**: Origami Patterns Solve a Major Physics Riddle

**原文链接**: [https://www.quantamagazine.org/origami-patterns-solve-a-major-physics-riddle-20251006/](https://www.quantamagazine.org/origami-patterns-solve-a-major-physics-riddle-20251006/)

生成摘要时出错

---

## 78. Vision Pro Future Uncertain as All Headset Development Is Seemingly Paused

**原文标题**: Vision Pro Future Uncertain as All Headset Development Is Seemingly Paused

**原文链接**: [https://www.macrumors.com/2025/10/11/vision-pro-future-uncertain/](https://www.macrumors.com/2025/10/11/vision-pro-future-uncertain/)

生成摘要时出错

---

## 79. Multi-Core by Default

**原文标题**: Multi-Core by Default

**原文链接**: [https://www.rfleury.com/p/multi-core-by-default](https://www.rfleury.com/p/multi-core-by-default)

生成摘要时出错

---

## 80. Patina: a Rust implementation of UEFI firmware

**原文标题**: Patina: a Rust implementation of UEFI firmware

**原文链接**: [https://github.com/OpenDevicePartnership/patina](https://github.com/OpenDevicePartnership/patina)

生成摘要时出错

---

## 81. A History of Large Language Models

**原文标题**: A History of Large Language Models

**原文链接**: [https://gregorygundersen.com/blog/2025/10/01/large-language-models/](https://gregorygundersen.com/blog/2025/10/01/large-language-models/)

生成摘要时出错

---

## 82. CPU cache-friendly data structures in Go

**原文标题**: CPU cache-friendly data structures in Go

**原文链接**: [https://skoredin.pro/blog/golang/cpu-cache-friendly-go](https://skoredin.pro/blog/golang/cpu-cache-friendly-go)

生成摘要时出错

---

## 83. Nobel Peace Prize 2025: María Corina Machado

**原文标题**: Nobel Peace Prize 2025: María Corina Machado

**原文链接**: [https://www.nobelprize.org/prizes/peace/2025/summary/](https://www.nobelprize.org/prizes/peace/2025/summary/)

生成摘要时出错

---

## 84. What is going on with all this radioactive shrimp?

**原文标题**: What is going on with all this radioactive shrimp?

**原文链接**: [https://www.consumerreports.org/health/food-safety/radioactive-shrimp-explained-a5493175857/](https://www.consumerreports.org/health/food-safety/radioactive-shrimp-explained-a5493175857/)

生成摘要时出错

---

## 85. Show HN: I wrote a full text search engine in Go

**原文标题**: Show HN: I wrote a full text search engine in Go

**原文链接**: [https://github.com/wizenheimer/blaze](https://github.com/wizenheimer/blaze)

生成摘要时出错

---

## 86. The Burrows-Wheeler Transform

**原文标题**: The Burrows-Wheeler Transform

**原文链接**: [https://sandbox.bio/concepts/bwt](https://sandbox.bio/concepts/bwt)

生成摘要时出错

---

## 87. The Unknotting Number Is Not Additive

**原文标题**: The Unknotting Number Is Not Additive

**原文链接**: [https://divisbyzero.com/2025/10/08/the-unknotting-number-is-not-additive/](https://divisbyzero.com/2025/10/08/the-unknotting-number-is-not-additive/)

生成摘要时出错

---

## 88. Figure 03, our 3rd generation humanoid robot

**原文标题**: Figure 03, our 3rd generation humanoid robot

**原文链接**: [https://www.figure.ai/news/introducing-figure-03](https://www.figure.ai/news/introducing-figure-03)

生成摘要时出错

---

## 89. Neutts-air – Open-source, on device TTS

**原文标题**: Neutts-air – Open-source, on device TTS

**原文链接**: [https://github.com/neuphonic/neutts-air](https://github.com/neuphonic/neutts-air)

生成摘要时出错

---

## 90. Voyage of the Marigold – Author's Notes

**原文标题**: Voyage of the Marigold – Author's Notes

**原文链接**: [https://sheep.horse/2025/6/voyage_of_the_marigold_author%27s_notes.html](https://sheep.horse/2025/6/voyage_of_the_marigold_author%27s_notes.html)

生成摘要时出错

---

## 91. Show HN: I've built a tiny hand-held keyboard

**原文标题**: Show HN: I've built a tiny hand-held keyboard

**原文链接**: [https://github.com/mafik/keyer](https://github.com/mafik/keyer)

生成摘要时出错

---

## 92. It's OpenAI's world, we're just living in it

**原文标题**: It's OpenAI's world, we're just living in it

**原文链接**: [https://stratechery.com/2025/its-openais-world-were-just-living-in-it/](https://stratechery.com/2025/its-openais-world-were-just-living-in-it/)

生成摘要时出错

---

## 93. An MVCC-like columnar table on S3 with constant-time deletes

**原文标题**: An MVCC-like columnar table on S3 with constant-time deletes

**原文链接**: [https://www.shayon.dev/post/2025/277/an-mvcc-like-columnar-table-on-s3-with-constant-time-deletes/](https://www.shayon.dev/post/2025/277/an-mvcc-like-columnar-table-on-s3-with-constant-time-deletes/)

生成摘要时出错

---

## 94. Financing My Klarna Doritos Locos Taco

**原文标题**: Financing My Klarna Doritos Locos Taco

**原文链接**: [https://theahura.substack.com/p/tech-things-financing-my-klarna-doritos](https://theahura.substack.com/p/tech-things-financing-my-klarna-doritos)

生成摘要时出错

---

## 95. New nanotherapy clears amyloid-β, reversing symptoms of Alzheimer's in mice

**原文标题**: New nanotherapy clears amyloid-β, reversing symptoms of Alzheimer's in mice

**原文链接**: [https://www.drugtargetreview.com/news/189235/new-nanotherapy-clears-amyloid-%CE%B2-reversing-alzheimers-in-mice/](https://www.drugtargetreview.com/news/189235/new-nanotherapy-clears-amyloid-%CE%B2-reversing-alzheimers-in-mice/)

生成摘要时出错

---

## 96. Under the hood: Vec<T>

**原文标题**: Under the hood: Vec<T>

**原文链接**: [https://marma.dev/articles/2025/under-the-hood-vec-t](https://marma.dev/articles/2025/under-the-hood-vec-t)

生成摘要时出错

---

## 97. In a post-truth world truth-seeking is more important

**原文标题**: In a post-truth world truth-seeking is more important

**原文链接**: [https://iai.tv/articles/in-a-post-truth-world-truth-seeking-is-more-important-than-ever-auid-3382](https://iai.tv/articles/in-a-post-truth-world-truth-seeking-is-more-important-than-ever-auid-3382)

生成摘要时出错

---

## 98. You can't build tcc from Nixpkgs if you are in the UK

**原文标题**: You can't build tcc from Nixpkgs if you are in the UK

**原文链接**: [https://github.com/NixOS/nixpkgs/issues/444342](https://github.com/NixOS/nixpkgs/issues/444342)

生成摘要时出错

---

## 99. A story about bypassing air Canada's in-flight network restrictions

**原文标题**: A story about bypassing air Canada's in-flight network restrictions

**原文链接**: [https://ramsayleung.github.io/en/post/2025/a_story_about_bypassing_air_canadas_in-flight_network_restrictions/](https://ramsayleung.github.io/en/post/2025/a_story_about_bypassing_air_canadas_in-flight_network_restrictions/)

生成摘要时出错

---

## 100. The Debugging Book

**原文标题**: The Debugging Book

**原文链接**: [https://www.debuggingbook.org/](https://www.debuggingbook.org/)

生成摘要时出错

---

