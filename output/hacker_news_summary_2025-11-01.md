# Hacker News 热门文章摘要 (2025-11-01)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 由于大型语言模型（LLM）的出现，arXiv不再接受计算机科学领域的职位或评论文章。

**原文标题**: arXiv No Longer Accepts Computer Science Position or Review Papers Due to LLMs

**原文链接**: [https://blog.arxiv.org/2025/10/31/attention-authors-updated-practice-for-review-articles-and-position-papers-in-arxiv-cs-category/](https://blog.arxiv.org/2025/10/31/attention-authors-updated-practice-for-review-articles-and-position-papers-in-arxiv-cs-category/)

arXiv计算机科学(CS)类别收紧对综述文章和立场论文的审核，原因是提交量激增，尤其是借助LLM生成的文章。虽然这些类型的论文从未被正式接受，但之前如果质量高且对社区有益，则由审核人员酌情允许发表。

现在，综述文章和立场论文要被考虑提交，*必须*首先被期刊或会议接受，并成功通过同行评审。作者在向arXiv提交时必须提供此同行评审的证明文件。缺乏此证明文件的提交很可能会被拒绝。

此项更改旨在应对由LLM推动的大量低质量综述文章（通常是简单的带注释的参考书目）的涌入，这些文章使审核人员不堪重负。新流程使arXiv能够依靠已建立的同行评审场所的质量控制。目标是确保只共享有价值的、专家撰写的综述文章和立场论文，从而解放审核人员，使其能够专注于核心研究论文的提交，并保持科学发现的步伐。研究科学和技术对社会影响的科学研究论文不受此政策限制。如果其他arXiv类别也遇到类似的大量LLM生成的内容，则可能会采取类似措施。

---

## 2. GHC 现在可以在浏览器中运行了

**原文标题**: GHC now runs in the browser

**原文链接**: [https://discourse.haskell.org/t/ghc-now-runs-in-your-browser/13169](https://discourse.haskell.org/t/ghc-now-runs-in-your-browser/13169)

GHC (Glasgow Haskell 编译器) 现已可以直接在 Web 浏览器中运行，完全在客户端进行。这得益于 GHC WebAssembly (wasm) 后端方面的重大进展。一个展示此功能的演示已作为 Haskell 游乐场提供。更多细节和技术解释将在稍后由作者提供。作者强调了 GHC wasm 后端令人印象深刻的进展，使其客户端执行成为可能。

---

## 3. SQLite 并发及为何你应该关心它

**原文标题**: SQLite concurrency and why you should care about it

**原文链接**: [https://jellyfin.org/posts/SQLite-locking/](https://jellyfin.org/posts/SQLite-locking/)

JPVenson的这篇博文讨论了Jellyfin中遇到的SQLite并发问题，并提出了相应的解决方案。由于SQLite基于文件的特性以及潜在的写操作冲突，Jellyfin经历了数据库锁定错误，尤其是在高负载或事务期间。旧版本Jellyfin中的一个错误加剧了这个问题，该错误导致过多的并行写请求。

为了缓解这些问题，Jellyfin使用EF Core拦截器实现了一种锁定机制，提供了三种策略：

*   **无锁 (No-Lock):** 默认行为，正常操作时不进行锁定，优先考虑性能。
*   **乐观锁 (Optimistic Locking):** 使用重试机制（通过Polly库）来处理锁定冲突，重试因锁定而失败的写操作。
*   **悲观锁 (Pessimistic Locking):** 采用`ReaderWriterLockSlim`来确保一次只能发生一个写操作，在写入期间阻止所有其他读写操作，从而最大限度地提高稳定性，但可能会牺牲性能。

该文章建议未来可能采用一种“智能锁定 (Smart Locking)”行为，该行为结合了乐观锁和悲观锁的优点。初步测试证实，两种锁定模式都有效地解决了潜在的并发问题。作者强调，Jellyfin的锁定实现旨在易于集成到其他面临类似SQLite锁定问题的EF Core应用程序中。

---

## 4. 网络上的弃用软件：你知道有HTML表格API吗？

**原文标题**: Abandonware of the web: do you know that there is an HTML tables API?

**原文链接**: [https://christianheilmann.com/2025/10/08/abandonware-of-the-web-do-you-know-that-there-is-an-html-tables-api/](https://christianheilmann.com/2025/10/08/abandonware-of-the-web-do-you-know-that-there-is-an-html-tables-api/)

本文强调了常被忽视的HTML表格API，作为创建和操作HTML表格时常用JavaScript方法的替代方案。作者提倡使用表格专用API（提供诸如`insertRow()`和`insertCell()`等方法），而非通过字符串连接或使用`createElement()`直接进行DOM操作来构建表格。此API允许开发者直接访问和修改表格元素（行、单元格、表头、表尾、标题），而无需重新渲染整个表格，从而可能提高性能和代码可读性。

文章提供了示例，演示了如何使用该API从嵌套数组创建表格，以及如何使用索引访问和修改单个单元格（例如，`t.rows[1].cells[1]`）。文章还指出了该API的一些怪癖，例如使用`-1`将行添加到表格末尾，以及无法直接创建`<th>`元素。

作者认为，如果像HTML表单一样，通过新功能来振兴和扩展HTML表格API，可以将表格的地位从单纯的布局工具提升为Web上合法的数据结构。文章鼓励重新审视和增强这种“废弃软件”，以提高Web开发效率和可访问性。最后，作者还提供了指向其新闻通讯和其他资源的链接。

---

## 5. CharlotteOS – 一款实验性的现代操作系统

**原文标题**: CharlotteOS – An Experimental Modern Operating System

**原文链接**: [https://github.com/charlotte-os/Catten](https://github.com/charlotte-os/Catten)

CharlotteOS：一个实验性现代操作系统，其核心为“Catten”，一个主要用Rust编写并包含部分汇编的单内核。Catten的目标是灵活性，灵感来源于外内核、Plan 9和Fuchsia，提供了一个类型安全的系统命名空间，可通过URI在网络上访问，并使用能力和强制访问控制进行保护。

该内核正处于积极开发阶段，并通过其代码仓库、Discord和Matrix寻求贡献者。目前，它以带有UEFI和ACPI固件的x86_64架构为目标。最低系统要求包括128MB RAM、4GB存储，以及对NVMe、USB大容量存储和带有UEFI图形输出协议的显示适配器等设备的支持。同时支持通过NS16550 UART和USB CDC ACM进行的串行通信。输入选项包括PS/2、USB HID和串口。网络功能包括USB CDC网络控制模型。

虽然允许在维护者批准的情况下使用C依赖，但严格禁止使用Rust、C和汇编以外的语言。该内核采用GNU通用公共许可证版本3.0（或更高版本）授权，且贡献受相同许可条款约束。

---

## 6. 展示HN：奇异吸引子

**原文标题**: Show HN: Strange Attractors

**原文链接**: [https://blog.shashanktomar.com/posts/strange-attractors](https://blog.shashanktomar.com/posts/strange-attractors)

这个“Show HN”帖子介绍了奇异吸引子，这种复杂的数学系统能够生成美丽的混沌图案，并通过Three.js可视化进行探索。作者详细描述了他们如何迷上这些系统，这源于秩序从随机性中涌现出来。

帖子解释了动力系统的基础知识，动力系统使用“相空间”（系统所有可能的状态）和“动力学”（支配状态转换的规则）的概念来模拟事物随时间的变化。然后，它深入研究了混沌理论，这是动力系统的一个分支，专注于表现出随机性和不可预测性，但仍遵循确定性规则的系统。“蝴蝶效应”，即微小的初始变化导致截然不同的结果，被重点强调。

奇异吸引子被定义为系统倾向于稳定下来的一组状态，通常表现出分形结构、对初始条件的敏感性以及不可预测的非周期性轨迹。该帖子使用托马斯吸引子作为示例来演示蝴蝶效应，展示了参数变化如何显著改变粒子轨迹。

实现部分描述了如何使用Three.js的乒乓渲染来高效地在GPU上渲染大量粒子。这涉及到在两个帧缓冲区对象（FBO）之间交替，一个用于当前粒子状态，另一个用于计算下一个状态，从而最大限度地减少CPU和GPU之间的数据传输。着色器程序用于将吸引子动力学应用于每个粒子。最后，作者提供了几个有用的资源和链接，供进一步探索。

---

## 7. 弗兰克·加斯金谈论保存“遗失”游戏

**原文标题**: Frank Gasking on preserving «lost» games

**原文链接**: [https://spillhistorie.no/2025/10/24/frank-gasking-on-preserving-lost-games/](https://spillhistorie.no/2025/10/24/frank-gasking-on-preserving-lost-games/)

本文采访了 Games That Weren’t (GTW) 的创始人弗兰克·加斯金。 GTW 是一个非营利数字档案馆，致力于保存和记录遗失、未发布和未完成的电子游戏。 加斯金的迷恋始于童年时代，当时他拥有一台 Commodore 64 电脑，并且在 Commodore Force 杂志上读到了一篇关于未发布游戏的令人振奋的文章。

GTW 最初是一个 Commodore 64 档案馆，后来扩展到涵盖 Amiga、PC、NES 等多个平台。 该档案馆包括已恢复的游戏、预览、屏幕截图、开发者资源以及有关被放弃或取消发行的游戏的详细信息。 加斯金强调了与开发者、收藏家和爱好者的合作的重要性。

加斯金特别强调了 GTW 在 Commodore 64 上的代表作《达菲鸭：主演油漆大劫案》，并强调了在 Hi-Tec 公司倒闭后，经过 18 年的寻找才得以恢复该游戏。

关于游戏发行商，加斯金提到偶尔会拒绝发布某些游戏，但也提到 GTW 通过提供已恢复的源代码和旧游戏的数字副本，为发行商提供帮助的情况。 他指出，虽然一些发行商积极主动地进行保护工作，但许多发行商才刚刚开始认真对待这个问题。

本文讨论了《THE GAMES THAT WEREN’T》一书，这是加斯金工作的实体化体现，提供了新鲜的内容、详细的研究以及游戏开发者的见解，涵盖了众多平台和几十年。 这本书超越了网站的内容，涵盖了广为人知和以前不为人知的游戏。

---

## 8. 自五月起，更严格的Rust需求

**原文标题**: Hard Rust requirements from May onward

**原文链接**: [https://lists.debian.org/debian-devel/2025/10/msg00285.html](https://lists.debian.org/debian-devel/2025/10/msg00285.html)

Julian Andres Klode宣布计划不早于2026年5月在APT软件包管理器中引入强制性Rust依赖项，包括Rust编译器、标准库和Sequoia生态系统。Klode列举了内存安全语言和改进的单元测试的优势，适用于.deb、.ar、.tar解析以及HTTP签名验证等关键组件。

该声明明确针对缺乏功能性Rust工具链的Debian移植维护者，敦促他们在未来六个月内实施该工具链，或者考虑停止对该移植的维护。给出的理由是Debian项目需要采用现代工具和技术，避免受到旧硬件架构的限制。

该邮件包含PGP签名，指定了首选的回复渠道（链上和链下），并列出了将收到回复通知的个人。它还包括后续消息，用于进行持续讨论。

---

## 9. 对Substrate的调查研究

**原文标题**: An investigation into Substrate

**原文链接**: [https://substack.com/inbox/post/177604037](https://substack.com/inbox/post/177604037)

无法访问文章链接。

---

## 10. 研究越来越多地发现空气污染物与痴呆症之间的联系

**原文标题**: Studies increasingly find links between air pollutants and dementia

**原文链接**: [https://www.nytimes.com/2025/11/01/health/alzheimers-dementia-air-pollution.html](https://www.nytimes.com/2025/11/01/health/alzheimers-dementia-air-pollution.html)

无法访问文章链接。

---

## 11. 我如何停止焦虑并开始热爱汇编语言

**原文标题**: How I stopped worrying and started loving the Assembly

**原文链接**: [https://medium.com/@jonas.eschenburg/how-i-stopped-worrying-and-started-loving-the-assembly-4fd00e786c60](https://medium.com/@jonas.eschenburg/how-i-stopped-worrying-and-started-loving-the-assembly-4fd00e786c60)

乔纳斯·埃申堡讲述了他回归复古编程的旅程，特别是针对雅达利ST。出于怀旧和渴望更多手动控制的愿望，他启动了一个项目，要在雅达利ST上运行VoxelSpace算法（因游戏科曼奇而流行），这在当时被认为是无法完成的壮举。

文章详细介绍了为雅达利ST编程的独特挑战和回报，强调了它与当代PC相比的简洁性。他解释了M68K汇编语言如何提供直接的硬件访问和更少限制的环境。一个关键障碍是理解雅达利ST不寻常的交错位平面图形系统。

埃申堡强调了汇编级优化的重要性，以克服雅达利ST 8MHz处理器的局限性。他分享了他学到的各种优化技术，包括简化算术、使用查找表和最小化寄存器使用。他还强调了令人惊讶的先进现代工具，这些工具可用于复古编程，例如VSCode集成、维护良好的GNU编译器集合（GCC）以及像Hatari这样的模拟器。他提倡使用这些工具在今天创作雅达利ST上的游戏和程序。

---

## 12. 我自制了一个CityMapper。

**原文标题**: I built my own CityMapper

**原文链接**: [https://asherfalcon.com/blog/posts/5](https://asherfalcon.com/blog/posts/5)

Asher Falcone 详细介绍了为伦敦构建个性化 CityMapper 式公共交通路线系统的过程。他的目标是利用公交、地铁和火车的实时到达数据来提供实时路线规划。

他解释了他选择 RAPTOR 算法的原因，该算法在最小化旅行时间的同时优化换乘次数。该算法分轮次工作，每轮搜索具有特定换乘次数的路线，类似于 Dijkstra 算法，但专门为公共交通定制。

一个重要的障碍是获取实时数据。他从 Rail Data Marketplace 获取了铁路数据，包括车站 CRS 代码和到达/出发时间。公交数据来自 TFL 公交到达终点，它提供了每个公交车站和路线的大量到达时间数据集。地铁数据也遵循类似的过程，并仔细考虑以确保不同线路上的车辆 ID 唯一。

步行被作为一个关键要素纳入其中，既可以扩展路线可能性，又可以连接功能相同但技术上独立的站点。他使用带有 OpenStreetMap 数据的 OSRM 路线引擎来计算站点之间的步行时间，并将每次步行视为 RAPTOR 算法中的一次换乘。

最后，Asher 构建了一个快速的后端和前端，以允许搜索路线并显示结果。他指出了一个局限性：与更容易检索公交车的 geoJson 数据不同，显示火车和地铁的路线轨迹证明具有挑战性。尽管由于数据请求需求量大而未公开部署该项目，但他分享了代码存储库，供有兴趣的人使用。

---

## 13. 数据中心推高价格，能源账单激化地方政治

**原文标题**: Data centers contribute to high prices as energy bills electrify local politics

**原文链接**: [https://www.wsj.com/economy/consumers/surging-power-costs-are-putting-the-squeeze-on-customers-f8b2c04b](https://www.wsj.com/economy/consumers/surging-power-costs-are-putting-the-squeeze-on-customers-f8b2c04b)

无法访问文章链接。

---

## 14. 编剧埃里克·海瑟勒谈《关灯以后》与恐怖片法则

**原文标题**: Screenwriter Eric Heisserer on Lights Out, the Rules of Horror

**原文链接**: [https://filmmakermagazine.com/99327-screenwriter-eric-heisserer-lights-out-the-rules-of-horror-and-collaborating-with-james-wan/](https://filmmakermagazine.com/99327-screenwriter-eric-heisserer-lights-out-the-rules-of-horror-and-collaborating-with-james-wan/)

编剧埃里克·海瑟勒讨论恐怖电影《关灯以后》的创作，该片改编自大卫·F·桑德伯格的短片。海瑟勒不喜欢被简单地贴上恐怖编剧的标签，他强调这部电影的重点是人物关系和临床抑郁症的隐喻，而不是仅仅依靠惊吓。

他详细介绍了他的写作过程，包括创建一个结构大纲以及收集各种想法。他还描述了一种写作早期草稿的方法，即优先考虑人物剧情，然后再添加恐怖元素，以确保惊吓是合理的。

海瑟勒讨论了与桑德伯格的合作过程，特别是导演已经为这部电影开发了核心人物和主题概念。他还谈到了预算限制，这迫使他们删除了一个涉及精神病院的支线情节。

访谈进一步探讨了为怪物黛安娜的能力建立规则的过程，以及他们如何努力创造新的东西，而不是依赖已有的超自然比喻。海瑟勒强调了尽早确定观众正在观看哪种类型的电影以及打破恐怖惯例的重要性，例如颠覆一次性男友的设定。他最后强调了用于驱赶黛安娜的合作照明噱头，并指出这些想法大多来自导演大卫·F·桑德伯格。

---

## 15. 讽刺：轻微恼人的魔方自动解法机

**原文标题**: S.A.R.C.A.S.M: Slightly Annoying Rubik's Cube Automatic Solving Machine

**原文链接**: [https://github.com/vindar/SARCASM](https://github.com/vindar/SARCASM)

S.A.R.C.A.S.M，或“轻微烦人的魔方自动解算机”，是一个由Teensy 4.1和ESP32-CAM控制的3D打印机器人，它以健康的讽刺口吻解决魔方问题。该项目仓库包含这个过度设计的作品的代码和原理图。

该机器人使用 ESP32-CAM 进行图像采集，Teensy 4.1 作为其主控制器。它配备了 ILI9341 显示屏，显示自定义的 2D 和 3D 图形、动画以及口型同步。步进电机和舵机负责魔方操作，并利用位置传感器进行故障检测。该构建还集成了与音频同步的 RGBW 照明，并采用设备上的文本到语音（TTS）功能，使用 espeak-ng 传递一系列讽刺性评论。

该项目的论坛帖子和演示视频（短片和完整演示）可供进一步了解。请注意，该项目需要对 Teensy 的核心进行略微修改，方法是从 usb_serial.c 和 usb_serial2.c 中的 txbuffer[] 和 rx_buffer[] 数组定义中删除 DMAMEM 属性，以便适应 RAM。创建者承认该存储库目前仍在进行中，并且可能保持不完整的状态。

---

## 16. 开源Ada：从门硬件到应用

**原文标题**: Open-Source Ada: From Gateware to Application

**原文链接**: [https://blog.adacore.com/open-source-ada-from-gateware-to-application](https://blog.adacore.com/open-source-ada-from-gateware-to-application)

本文旨在推广Ada语言，将其作为C语言在嵌入式系统开发中一种可行的开源替代方案。文章重点介绍Ada在基于ULX3S FPGA板部署的Neorv32软核RISC-V片上系统（SoC）上的应用，目标读者包括探索Ada的开发者、缺乏软核CPU经验的爱好者以及嵌入式系统新手。

作者强调了Neorv32的稳健设计、详尽文档和确定性行为，并将其与其他不太可靠的开源项目进行了对比。文章详细介绍了用于创建Neorv32位流的完全开源的FPGA工具链，包括GHDL、Yosys、Nextpnr和ecppack，并强调了其相比专有工具的速度优势。

文章描述了为ULX3S配置Neorv32、生成位流并将其烧录到FPGA的过程。随后，作者从C语言过渡到Ada语言，解释了如何通过创建一个练习UART RX中断的最小演示来实现中断处理。最后，作者深入研究了如何使用Alire和`bare_runtime`包设置一个最小的Ada运行时环境，定制构建文件，使用`startup_gen`创建链接器脚本和启动代码，以及用Ada语言实现中断处理。文章鼓励读者探索Ada在构建可靠嵌入式系统方面的潜力。

---

## 17. 泄密者揭示哪些Pixel手机容易受到Cellebrite破解

**原文标题**: Leaker reveals which Pixels are vulnerable to Cellebrite phone hacking

**原文链接**: [https://arstechnica.com/gadgets/2025/10/leaker-reveals-which-pixels-are-vulnerable-to-cellebrite-phone-hacking/](https://arstechnica.com/gadgets/2025/10/leaker-reveals-which-pixels-are-vulnerable-to-cellebrite-phone-hacking/)

泄密者披露信息：Cellebrite简报揭示谷歌Pixel手机易受其破解工具攻击。泄露的截图发布在GrapheneOS论坛上，显示Cellebrite可以从运行原生安卓系统的Pixel 6、7、8和9手机中提取数据，即使是在传统的“首次解锁前”（BFU）状态下。但他们无法暴力破解密码或复制eSIM。

文章强调，运行GrapheneOS（一种注重安全的安卓系统）的Pixel手机对Cellebrite的工具具有更强的抵抗力。泄露的信息显示，在2022年末之后更新软件的GrapheneOS Pixel手机，即使解锁后也能免疫数据提取。

泄密事件暴露了GrapheneOS相对于谷歌原生Pixel OS的明显优势。泄密者rogueFed声称在未被发现的情况下参加了两次Cellebrite简报会，但泄露了组织者的名字，表明未来可能会有更严格的筛选流程。文章最后提到，已联系谷歌就GrapheneOS为何显得更安全一事发表评论，如果收到回复，文章将会更新。

---

## 18. Futurelock：异步Rust 中的一个隐蔽风险

**原文标题**: Futurelock: A subtle risk in async Rust

**原文链接**: [https://rfd.shared.oxide.computer/rfd/0609](https://rfd.shared.oxide.computer/rfd/0609)

本文介绍了“未来锁死”，这是一种异步 Rust 编程特有的细微死锁。当一个持有资源的 Future (A) 是另一个 Future (B) 继续执行所必需的，但负责这两者的任务不再主动轮询 Future A 时，就会发生未来锁死。

本文通过一个使用 `tokio::select!` 和 `Mutex` 的实际示例来说明这一点。一个后台任务获取锁。一个主任务使用 `tokio::select!` 并发地轮询 future1（尝试获取相同的锁）和一个睡眠 future。如果睡眠 future 首先完成，则选择 `select!` 的分支，任务继续执行，但 future1 仍然阻塞，等待锁。当后台任务释放锁时，future1 被唤醒，但主任务现在只轮询一个新的 future3（在 `select!` 的选定分支中创建），该 future3 也需要相同的锁。 这就造成了一个死锁，因为 future3 正在等待 future1 持有的锁，而 future1 正在等待任务轮询它，但这种情况永远不会发生。

本文阐明了任务和 Future 之间的区别，强调单个任务可以同时管理多个 Future。当任务将其轮询焦点从一个 Future 切换到另一个 Future 时，会产生未来锁死，从而无意中创建了一个循环依赖，其中一个等待的 Future 永远不会被轮询，从而阻止资源释放。

本文还概述了可能发生未来锁死的其他场景，例如 Streams (FuturesOrdered/FuturesUnordered)，并强调使用 `futures::future::join_all` *不会*出现此问题。最后，本文讨论了调试未来锁死的挑战以及需要注意的迹象。

---

## 19. 程序员们关于CPU缓存的迷思 (2018)

**原文标题**: Myths Programmers Believe about CPU Caches (2018)

**原文链接**: [https://software.rajivprab.com/2018/04/29/myths-programmers-believe-about-cpu-caches/](https://software.rajivprab.com/2018/04/29/myths-programmers-believe-about-cpu-caches/)

本文旨在消除程序员对CPU缓存及其对并发影响的常见误解。它论证道，由于MESI等硬件级协议的存在，现代CPU缓存本质上是具有一致性的，这意味着多个核心访问相同的内存地址不会看到冲突的值。这种一致性对软件开发者来说是被抽象掉的。

文章阐明，缓存并非简单的哑存储，它们会主动通信以保持数据一致性。文章解释了MESI协议（已修改、独占、共享、无效），并提供了多核系统中内存读写操作期间其工作原理的示例。文章强调存在多种缓存设计变体。

文章还解决了这样一种误解：Java等语言中的`volatile`变量会强制直接读/写主内存，这将非常缓慢。实际上，`volatile`确保读/写绕过CPU寄存器并直接与L1缓存交互，从而允许硬件一致性协议有效地处理同步。

文章最后解释了为什么诸如`volatile`之类的同步原语仍然是必要的。虽然缓存具有一致性，但仅保存在CPU寄存器中的数据并非如此。编译器优化寄存器的使用，假设是单线程执行，因此并发构造对于保护有竞争风险的数据至关重要。本质上，`volatile`促进了缓存交互，硬件可确保跨多个线程的一致性。

---

## 20. 国土安全部文件显示，你不能拒绝ICE的面部识别应用扫描。

**原文标题**: You can't refuse to be scanned by ICE's facial recognition app, DHS document say

**原文链接**: [https://www.404media.co/you-cant-refuse-to-be-scanned-by-ices-facial-recognition-app-dhs-document-says/](https://www.404media.co/you-cant-refuse-to-be-scanned-by-ices-facial-recognition-app-dhs-document-says/)

根据404 Media获得的国土安全部(DHS)文件，移民和海关执法局(ICE)不允许个人拒绝其“Mobile Fortify”应用程序的面部扫描，该程序用于验证身份和移民状态。该应用程序还会存储拍摄的所有面部照片，包括美国公民的照片，存储时间为15年。该文件详细介绍了Mobile Fortify背后的技术，数据如何处理和存储，以及DHS使用该技术的理由。此前，404 Media曾报道ICE和海关与边境保护局(CBP)正在公共场所扫描面部以验证公民身份。完整文章仅限404 Media付费会员访问，但注册邮箱可免费访问有限版本。该媒体鼓励订阅和捐款，以支持他们的《信息自由法》报道。

---

## 21. 成瘾市场

**原文标题**: Addiction Markets

**原文链接**: [https://www.thebignewsletter.com/p/addiction-markets-abolish-corporate](https://www.thebignewsletter.com/p/addiction-markets-abolish-corporate)

无法访问文章链接。

---

## 22. 不可能的优化，以及实现它的元编程

**原文标题**: The Impossible Optimization, and the Metaprogramming to Achieve It

**原文链接**: [https://verdagon.dev/blog/impossible-optimization](https://verdagon.dev/blog/impossible-optimization)

埃文·奥瓦迪亚2025年10月27日发表的文章《不可能的优化，以及实现它的元编程》，可能探讨了软件或编程领域中一个具有挑战性或看似无法达成的优化问题。其核心论点是通过元编程可以实现这种“不可能的优化”。

鉴于标题，这篇文章可能深入探讨：

*   **优化的本质：** 描述是什么使得这种优化特别困难或以前被认为是无法实现的。这可能涉及传统方法的局限性、架构约束或问题领域中固有的复杂性。

*   **元编程作为解决方案：** 解释元编程技术如何克服这些局限性。这可能涉及操作其他代码、在运行时生成代码或动态改变程序结构的代码。

*   **实现细节：** 提供元编程如何应用于实现所需优化的具体示例或策略。这可能包括使用的特定编程语言、库或设计模式。

*   **收益与权衡：** 讨论这种元编程方法在性能、效率或其他相关指标方面的优势。文章也可能承认潜在的缺点，例如增加的复杂性、调试挑战或平台依赖性。

本质上，这篇文章认为通过创新性地应用元编程技术，可以实现传统上困难或不可能的优化。作者可能提出了一个具体的案例研究或场景来说明这一点。

---

## 23. 用F#解决纽约时报的“Pips”游戏

**原文标题**: Solving the NY Times "Pips" game with F#

**原文链接**: [https://github.com/brianberns/Pips](https://github.com/brianberns/Pips)

本文概述了使用 F# 实现求解《纽约时报》“Pips”谜题游戏的方案。“Pips”游戏的目标是用多米诺骨牌覆盖由正方形单元格组成的形状，并遵守区域内特定点数之和等约束条件。作者使用回溯算法，并结合几何平铺信息和积极剪枝来优化解决方案的查找过程。

核心算法围绕策略性地放置多米诺骨牌展开，并在每次放置后验证谜题状态。如果放置导致无效状态（违反区域约束），则算法会回溯并尝试不同的多米诺骨牌或放置方案。

为了提高效率，本文介绍了两个关键优化：

1.  **平铺：** 使用预先计算的不同形状的平铺模式来指导多米诺骨牌的放置。 这通过专注于有效的平铺可能性来限制搜索空间。

2.  **剪枝：** 在每次放置多米诺骨牌后，积极检查区域约束。 这包括检查“相等”、“不等”、“总和小于”、“总和大于”和“总和精确”区域，以尽早识别无效路径，并避免探索搜索树中的无效分支。

本文提供了 F# 代码片段，用于定义诸如 `Domino`、`Cell`、`Edge`、`Board` 和 `Region` 等关键数据结构。 它强调了 `Board` 类型中不变性的重要性，每次放置多米诺骨牌时都使用写时复制。 性能结果表明，该求解器能够在总共约 1.8 秒内找到 88 个难度较高的 Pips 谜题的解决方案。 本文还包含一个表格，详细说明了各种谜题所花费的时间和解决方案数量。

---

## 24. 引入架构变体

**原文标题**: Introducing architecture variants

**原文链接**: [https://discourse.ubuntu.com/t/introducing-architecture-variants-amd64v3-now-available-in-ubuntu-25-10/71312](https://discourse.ubuntu.com/t/introducing-architecture-variants-amd64v3-now-available-in-ubuntu-25-10/71312)

Ubuntu 25.10 引入“架构变体”，允许针对特定芯片优化软件包，从 x86-64-v3 (amd64v3) 开始。这使得能够利用现代处理器功能，而不会牺牲与旧硬件的兼容性。

在 25.10 中，一部分软件包（主要来自“main”组件，大约 2000 个源代码包）以 amd64v3 优化版本提供，用户可以选择启用，但它们尚未经过与标准软件包相同的严格测试。完整的 amd64v3 支持，包括重建的软件包和全面的测试，计划在 26.04 LTS 版本中实现。基准测试表明，总体性能提升约 1%，数值应用程序的提升更为显著。

用户可以使用 `ld.so --help | grep '\-v[0-9]'` 检查 x86-64-v3 支持。要启用 amd64v3 软件包，用户必须更新 `dpkg`，然后配置 `apt` 以将 `amd64v3` 作为架构变体包含在内，并执行更新和升级。

一个关键的考虑因素是，安装 amd64v3 软件包可能会阻止在没有 x86-64-v3 支持的旧机器中使用硬盘/SSD。计划在 26.04 LTS 中改进此过程，包括恢复方法。此功能旨在通过利用较新的处理器功能来提高性能。

---

## 25. 绕过安卓开发者验证的一种理论方法

**原文标题**: A theoretical way to circumvent Android developer verification

**原文链接**: [https://enaix.github.io/2025/10/30/developer-verification.html](https://enaix.github.io/2025/10/30/developer-verification.html)

本文探讨了一种理论上的绕过方案，以应对谷歌即将推出的Android开发者验证系统，该系统旨在阻止用户安装未经注册的APK。作者担心该系统（需要支付25美元或使用有限的“业余爱好者”许可）将阻碍像他们这样的小型开发者。谷歌最近将Android开发设为私有以及三星移除引导加载程序解锁，加剧了他们的担忧。

提出的“破解”方法涉及分发一个“已验证加载器APK”，该加载器可以动态加载用户想要的任何APK，从而绕过对每个应用程序进行单独验证的需求。这利用了Dalvik/ART通过`PathClassLoader`实现的动态代码执行能力。该加载器需要在Android的Activity生命周期内初始化目标APK的主Activity，处理文件访问和名称冲突。这可以通过字节码修补（.odex/.dex到.smali）或潜在地使用不安全的Dalvik API来实现。

作者承认实施上的挑战以及缺乏功能性概念验证。文章讨论了使用业余爱好者许可分发加载器APK的后勤障碍，可能需要依靠志愿者或随机用户进行签名。这会引入恶意软件的漏洞，需要进行代码扫描。需要进行混淆以避免谷歌检测到加载器的代码。

作者认识到谷歌可能限制ADB安装，从而进一步限制侧载。他们承认，由于谷歌的不断阻止，维护这样的解决方案将很困难。作者最终的希望在于基于root的解决方案，因为它们绕过了谷歌对原生Android的限制。虽然该解决方案是理论上的并且存在重大障碍，但作者希望能够激发讨论和协作，以寻找解决方案来保护Android上的侧载和开发者自由。

---

## 26. 《杀死死者》影评：守望墓地

**原文标题**: 'Killing the Dead' Review: Watch the Graveyard

**原文链接**: [https://www.wsj.com/arts-culture/books/killing-the-dead-review-watch-the-graveyard-f54e14f4](https://www.wsj.com/arts-culture/books/killing-the-dead-review-watch-the-graveyard-f54e14f4)

无法访问文章链接。

---

## 27. 虎甲模拟器

**原文标题**: Tigerbeetle Simulator

**原文链接**: [https://sim.tigerbeetle.com/](https://sim.tigerbeetle.com/)

“虎甲模拟器”一文介绍了一款针对TigerBeetle的模拟器。TigerBeetle是一个分布式金融会计数据库，其设计目标是安全、高性能和容错。该模拟器可能允许用户为TigerBeetle的部署建模并测试不同的场景和配置。这可能包括模拟各种工作负载、网络条件和故障场景，以评估系统在不同情况下的行为和性能。

这种模拟器的主要好处是通过实现全面的生产前测试来降低TigerBeetle部署的风险。用户可以尝试不同的配置并观察系统对模拟事件的响应，在上线之前识别潜在的瓶颈或漏洞。对于一个旨在处理金融交易的数据库来说，这一点尤其有价值，因为准确性和可靠性至关重要。

虽然文章标题很简短，但它表明该模拟器将帮助用户理解TigerBeetle的行为，针对特定用例优化其配置，并在生产环境中部署之前增强对其稳健性的信心。该模拟器很可能成为开发人员、系统管理员以及任何负责部署和管理TigerBeetle实例的人员的宝贵工具。它提供了一个受控环境，可以探索系统的功能和局限性，而不会冒现实世界数据或金融交易的风险。

---

## 28. 超越平滑分析：按部就班地分析单纯形法

**原文标题**: Beyond Smoothed Analysis: Analyzing the Simplex Method by the Book

**原文链接**: [https://arxiv.org/abs/2510.21613](https://arxiv.org/abs/2510.21613)

本文《超越平滑分析：按部就班分析单纯形法》介绍了一种名为“按部就班分析”的新算法分析框架。作者Eleon Bach、Alexander E. Black、Sophie Huiberts和Sean Kafer提出该框架，旨在弥合理论算法分析与实际性能观察之间的差距。

按部就班分析旨在不仅对输入数据进行建模，还对算法本身进行建模，将分析建立在实现细节、输入建模最佳实践以及来自实际基准实例的测量之上。与现有框架相比，这种方法力求更好地反映真实世界的算法行为。

作者将按部就班分析应用于单纯形法，这是一种线性规划算法，以其卓越的实际性能而闻名，但最坏情况下的理论保证却很差。该论文认为，按部就班分析克服了平滑分析的弱点，平滑分析是之前尝试解释单纯形法效率的一种方法。作者证明，在输入缩放假设、可行性容差以及单纯形法实现中使用的其他设计原则下，按部就班分析预测单纯形法的多项式运行时间。

该论文共42页，归类于数据结构与算法（cs.DS）和优化与控制（math.OC）之下。它包括指向论文PDF、HTML和TeX源代码的全文链接。

---

## 29. 拥有数据对象

**原文标题**: On Having a Data Object

**原文链接**: [https://www.natemeyvis.com/on-having-a-data-object/](https://www.natemeyvis.com/on-having-a-data-object/)

本文批判了常见的数据对象模式，即由一个单独的类来管理与持久层特定部分（例如，一个“帽子”对象管理所有与帽子相关的数据）的交互。虽然这种模式看似简单，且常被诸如 Django 之类的框架强制执行，但作者认为它通常会导致更多问题，而不是解决问题。

核心论点是，代码库的不同部分往往需要对同一真实世界实体进行略有不同的对象表示，而单个数据对象无法充分满足这些需求。在不同上下文中使用同一个“帽子”对象会强制使用具有不正确语义的可选字段，并使验证和测试变得复杂。

此外，该模式鼓励将不同的数据访问模式视为相同，从而导致函数臃肿和混乱，并带有多个标志和参数来满足各种调用者。这破坏了封装性，并重新引入了其旨在避免的复杂性。

因此，中心数据对象变得庞大且难以管理，将不必要的复杂性引入到整个代码库中，并增加了耦合。这还会引入一个额外的故障点，尤其是在对象是自动生成的情况下。

作者的结论是，一个干净的、特定于模块的持久性管理层，针对每个上下文的需求量身定制，通常是一个更好的方法，即使这意味着一些明显的重复。他们提倡准确性和清晰性，而不是合并，并建议采用更精细的方法可以带来更易于维护和测试的代码。

---

## 30. 入侵印度最大汽车制造商：塔塔汽车

**原文标题**: Hacking India's largest automaker: Tata Motors

**原文链接**: [https://eaton-works.com/2025/10/28/tata-motors-hack/](https://eaton-works.com/2025/10/28/tata-motors-hack/)

2025年10月，伊顿公司披露了塔塔汽车系统于2023年发现的重大安全漏洞。这些发现暴露了大量敏感数据以及恶意活动的可能性。

最关键的问题涉及在面向公众的网站（E-Dukaan和FleetEdge）上暴露的AWS密钥，从而允许访问多个AWS存储桶中的超过70TB的数据。这包括客户数据库、财务报告、带有PAN详细信息的发票、车队洞察，甚至能够写入某些网站，从而可能启用恶意软件注入。一个密钥以纯文本形式发现，而另一个密钥则使用简单的客户端解密方法“加密”。

另一个重大漏洞是通过E-Dukaan网站进入塔塔汽车Tableau系统的后门。通过利用绕过密码验证的“信任令牌”机制，研究人员获得了Tableau的管理员权限，暴露了许多内部项目、财务报告和经销商仪表板。

最后，测试驾驶网站的JavaScript代码中暴露的Azuga API密钥允许访问Azuga车队管理平台，从而可能危及用于跟踪塔塔汽车试驾车辆的系统。

研究人员通过CERT-IN向塔塔汽车报告了所有四个问题。虽然最初反应迅速，但塔塔汽车在修复AWS密钥暴露方面进展缓慢，需要持续跟进和数月内的具体说明。作者强调塔塔汽车需要改进其安全措施，以保护客户数据和公司资产，并对这些漏洞如此容易被发现表示担忧。

---

## 31. 我们如何发现闲置的 7 TiB 内存

**原文标题**: How We Found 7 TiB of Memory Just Sitting Around

**原文链接**: [https://render.com/blog/how-we-found-7-tib-of-memory-just-sitting-around](https://render.com/blog/how-we-found-7-tib-of-memory-just-sitting-around)

Brian Stack 讲述了 Render 团队如何发现并解决了 Kubernetes 基础设施中由日志收集守护进程集 Vector 引起的一个重大内存泄漏问题。他们观察到 Calico 和 Vector 等守护进程集的内存消耗很高，在优化 Calico 之后，注意到 Vector 的内存使用量也异常高。

调查显示，Vector 从每个节点 listwatch 命名空间，以便在 Kubernetes 日志中引用命名空间标签，即使这些标签仅用于标识用户命名空间。该团队意识到，他们可以在不 listwatch 命名空间的情况下实现相同的结果。

他们创建了一个配置选项来禁用 Vector 中的命名空间 listwatch，并与 Vector 维护者合作进行了更改。最初，禁用命名空间 listwatch 导致日志发送中断，但 AI 聊天机器人 Claude 帮助识别了代码中的依赖关系问题。修复该问题后，内存使用量下降了 50%，但一位队友观察到仍有 1GiB 未被占用，从而发现第二个 kubernetes_logs 源仍在活动。修复后，内存使用量降至预期水平。

该修复涉及禁用不必要的命名空间标签收集，从而为他们的集群节省了大量内存，总计超过 7 TiB。这也减少了 CPU 和网络 I/O，并提高了推出稳定性。作者强调，基础设施调试是一个逐步改进的过程，突出了质疑假设、坚持调查和协作的重要性。

---

## 32. 我对MacBook Pro M4的印象

**原文标题**: My Impressions of the MacBook Pro M4

**原文链接**: [https://michael.stapelberg.ch/posts/2025-10-31-macbook-pro-m4-impressions/](https://michael.stapelberg.ch/posts/2025-10-31-macbook-pro-m4-impressions/)

非专业用户使用六个月后对 MacBook Pro M4 的评测。作者从 MacBook Air M1 升级，主要是为了纳米纹理显示屏，它可以显著减少反光，这是 Air 型号所没有的功能。

作者选择了标准 M4 芯片，而不是 M4 Pro，以优先考虑减少发热和风扇使用。主要配置包括 14 英寸 Liquid Retina XDR 纳米纹理显示屏、M4 芯片（10 核 CPU，10 核 GPU）、32GB 内存和 2TB 固态硬盘。

作者对电池续航感到印象深刻，认为它甚至比已经非常出色的 M1 Air 还要好。他们也很欣赏其静音运行，风扇很少启动。他们还注意到，即使在挂起和充满电的情况下，笔记本电脑有时也会变热。

120Hz 显示屏的一个令人惊喜的好处是，它可以提高网页浏览等任务的感知速度，因为它减少了操作和视觉响应之间的延迟，尤其是在响应速度快的系统上。

虽然作者理想情况下更喜欢带有纳米纹理显示屏的 MacBook Air，但他们对 Pro 版本也很满意。他们还表达了希望通过 Asahi Linux 运行 Linux 的愿望，但目前对外部显示器和 M4 芯片的支持不足。

总而言之，作者高度评价 MacBook Pro M4 的纳米纹理显示屏和长电池续航。作者鼓励读者订阅他们的博客并支持他们的工作。

---

## 33. 在浏览器中使用 DuckDB-WASM 查询 TB 级数据

**原文标题**: Use DuckDB-WASM to query TB of data in browser

**原文链接**: [https://lil.law.harvard.edu/blog/2025/10/24/rethinking-data-discovery-for-libraries-and-digital-humanities/](https://lil.law.harvard.edu/blog/2025/10/24/rethinking-data-discovery-for-libraries-and-digital-humanities/)

本文探讨了一种提供在线访问和发现大型数据集的新方法，特别关注包含近 18 TB 数据的 Data.gov 档案馆。 传统上，各组织面临着服务器解决方案的高成本和复杂性（功能强大）与静态文件托管的经济性（但功能有限）之间的权衡。

作者探索了一种新模型，该模型使用 DuckDB-Wasm 等客户端数据分析工具，使用户无需专用服务器即可直接在浏览器中查询大型远程数据集。 这种方法利用 WebAssembly 和 HTTP 范围请求等技术来高效地检索和处理仅需的数据。

Data.gov 档案馆搜索项目利用此模型，将元数据存储为静态托管上的压缩 Parquet 文件，并使用 DuckDB-Wasm 在浏览器中执行查询。 这实现了对档案记录的动态浏览、搜索和过滤，同时保持了较低的运营成本和减少的技术开销。

本文重点介绍了这种方法对图书馆、数字人文项目和其他处理大型数据集的组织的益处，包括更低的运营成本、降低的安全风险，以及即使在人员配置或资金发生变化的情况下也能维持访问。 作者鼓励其他人尝试这种模型，分享他们的经验，并协作以进一步开发和改进这些工具。 他们强调开放共享的重要性，并邀请社区提供反馈。

---

## 34. 积极倾听：沟通中的瑞士军刀

**原文标题**: Active listening: the Swiss Army Knife of communication

**原文链接**: [https://togetherlondon.com/insights/active-listening-swiss-army-knife](https://togetherlondon.com/insights/active-listening-swiss-army-knife)

无法访问文章链接。

---

## 35. 盈利的初创公司

**原文标题**: The profitable startup

**原文链接**: [https://linear.app/now/the-profitable-startup](https://linear.app/now/the-profitable-startup)

Karri Saarinen认为，初创企业优先考虑盈利能力而非超高速增长不仅可行，而且更有优势。他挑战了不惜一切代价追求无情增长的传统初创企业教条，倡导一种更可持续和可控的方法。

Saarinen认为，盈利能力使初创企业独立于投资者，使他们能够专注于其核心愿景并决定自己的增长速度。他引用了 Paul Graham 的“拉面盈利”概念，并认为如今，在快速增长的同时实现传统盈利能力越来越容易。

Saarinen 借鉴他在 Linear 的经验，强调了小型、专注团队的好处，强调他们可以提供更高质量和更快的结果。他批评了团队快速扩张的趋势，认为这往往会导致愿景被稀释、进展缓慢和管理费用增加。他建议缓慢、有目的地招聘，以保持质量和文化。

主要结论包括：

*   **盈利能力就是掌控你的命运，并以你想要的方式构建企业。**
*   **每位员工的收入应在 50 万美元至 100 万美元之间。**
*   **在优先考虑利润之前，评估你的风险状况和市场。**
*   **限制团队规模，尤其是在产品市场匹配之前。**
*   **盈利能力使创始人能够按照自己的条件筹集资金。**

Saarinen 总结说，盈利能力可以带来内心的平静，让创始人专注于构建伟大的产品和服务客户，而不是不断追逐资金。他强调，对于许多初创企业来说，这是一个可以实现的目标，主要在于控制招聘速度和数量。

---

## 36. 我为什么要关心自行车棚的颜色？(1999)

**原文标题**: Why should I care what color the bikeshed is? (1999)

**原文链接**: [https://www.bikeshed.com/](https://www.bikeshed.com/)

Poul-Henning Kamp 1999年的文章《我为什么要关心自行车棚的颜色？》探讨了软件开发中对琐碎事务进行无益且过度的辩论现象，并借鉴了帕金森定律中的“自行车棚”类比。

核心论点是，当话题容易被很多人理解时，例如自行车棚的颜色，讨论往往会变得异常冗长和激烈，而像原子能发电站这样复杂的话题则相反。人们很容易对简单的事情发表意见，以表明他们的参与并留下他们的“指纹”。

Kamp用`sleep(1)`命令中关于小数秒的冗长讨论为例来阐述这一点。他认为这种“自行车棚效应”浪费了时间和精力，而这些时间和精力本可以更好地用于更重要的问题。

他进一步感叹这会对新的贡献者产生的影响，可能会因无休止的、有时是激烈的辩论而吓跑他们。Kamp表达了对经验丰富的开发人员可能会无意中劝退初级开发人员的担忧。

Kamp提出了实际的解决方案：通过提示用户重新考虑广泛发送电子邮件的必要性、确认邮件线程的读者、信息的完整性和情绪的镇定来提高电子邮件礼仪。更重要的是，他主张忽略消极情绪，并鼓励为新人创造一个更受欢迎的环境。他鼓励新的开发人员参与进来，尽管可能存在“自行车棚效应”。最终，他希望创造一种文化，让贡献者能够在不受过度干预的情况下“建造一个自行车棚”。

---

## 37. Perfetto：Linux客户端追踪的瑞士军刀

**原文标题**: Perfetto: Swiss army knife for Linux client tracing

**原文链接**: [https://lalitm.com/perfetto-swiss-army-knife/](https://lalitm.com/perfetto-swiss-army-knife/)

本文总结了一次关于使用 Perfetto 工具套件作为调试 Linux 性能问题的“瑞士军刀”的演讲。Perfetto 包含一个 SDK、用于收集数据的守护进程和一个支持各种跟踪格式（包括 perf.data、ftrace 和 Chrome JSON）的跟踪处理器。Perfetto UI 是一个基于 Web 的可视化工具，允许用户使用时间线、选择、聚合和 SQL 查询来分析跟踪数据。

文章演示了如何使用 Perfetto 来诊断 Rust 程序渲染 Julia 集时的性能下降问题。最初，使用了 `perf` 和火焰图，但由于聚合数据丢失了时间维度，因此未能揭示根本原因。Perfetto 实现了基于时间的分析，揭示了工作线程活动中的阶梯模式，表明存在休眠。

通过 `trace-cmd` 收集的调度器跟踪显示线程正在休眠，但原因尚不清楚。在 Rust 中使用 `tracing` 和 `tracing-perfetto` crates 进行的应用级跟踪显示，“更新自适应质量”功能花费了异常长的时间，导致了帧丢失。文章重点介绍了 Perfetto 的功能，如区域选择、改进的火焰图可视化、自下而上视图和用户空间流可视化。总的来说，它展示了 Perfetto 如何结合系统和应用层面的洞察力来进行有效的调试。

---

## 38. Viagrid – 采用工厂化过孔实现快速PCB原型设计的PCB模板 [视频]

**原文标题**: Viagrid – PCB template for rapid PCB prototyping with factory-made vias [video]

**原文链接**: [https://www.youtube.com/watch?v=A_IUIyyqw0M](https://www.youtube.com/watch?v=A_IUIyyqw0M)

本文简要介绍了“Viagrid”，一种利用工厂制作的过孔实现快速PCB原型设计的PCB模板。结合上下文，它可能源自YouTube视频。其余内容为标准的YouTube法律和版权信息，表明其来源可能是YouTube上推广或讨论Viagrid模板的视频。

总而言之，关键在于存在一种名为“Viagrid”的PCB模板，旨在通过利用预制过孔来加速原型设计过程，这些过孔是PCB不同层之间的电气连接。这意味着与手动制作过孔的方法相比，可以缩短原型设计时间并潜在地提高可靠性。

---

## 39. 科技公司裁员只为“投资AI”，互相烧钱

**原文标题**: Tech companies are firing everyone to "fund AI", spending money on each other

**原文链接**: [https://old.reddit.com/r/ArtificialInteligence/comments/1oj52xx/tech_companies_are_firing_everyone_to_fund_ai_but/](https://old.reddit.com/r/ArtificialInteligence/comments/1oj52xx/tech_companies_are_firing_everyone_to_fund_ai_but/)

无法访问文章链接。

---

## 40. Show HN: Pipelex – 用于可重复AI工作流程的声明式语言

**原文标题**: Show HN: Pipelex – Declarative language for repeatable AI workflows

**原文链接**: [https://github.com/Pipelex/pipelex](https://github.com/Pipelex/pipelex)

Pipelex 是一种开源语言，用于构建和运行可重复的 AI 工作流，它提供了一种声明式方法，用户可以编写业务逻辑，而不是 API 调用。它通过使用“管道”将复杂任务分解为可管理的步骤，这些“管道”处理特定的转换，并通过结构化和验证的过程确保可靠性和可理解性。

核心工作流程涉及在 `.plx` 文件中定义概念、管道及其交互。用户可以使用单个命令生成初始工作流，并通过安装的流行 IDE 规则集，使用 AI 辅助进一步自定义它们。该工作流程利用概念（具有含义的类型）来确保正确的数据处理。

该过程包括安装步骤 (`pip install pipelex`)、获取 API 密钥（通过 Discord 免费获取 Pipelex 密钥，或使用来自 OpenAI 等提供商的个人密钥），以及使用 CLI 或 Python 运行生成的工作流。文档提供了有关设置 AI 提供商和模型的指南，并且提供了一个 IDE 扩展，用于为 `.plx` 语言提供功能。

摘要还指出了一些可选功能，例如对 Anthropic、Google、Mistral AI、Amazon Bedrock 和 FAL 的支持，这些可以作为额外内容安装。Pipelex 使用可选的匿名遥测来改进，用户可以自定义数据共享的级别。该项目鼓励贡献，并提供 Discord 社区以获得支持。

---

## 41. Nix 派生疯狂

**原文标题**: Nix Derivation Madness

**原文链接**: [https://fzakaria.com/2025/10/29/nix-derivation-madness](https://fzakaria.com/2025/10/29/nix-derivation-madness)

本文探讨了 Nix 中一个令人困惑的问题：尽管 derivation 的输出存在并被 Nix 存储和缓存引用，但仍然找不到该 derivation。作者最初难以理解为什么 Ruby 二进制文件存在，但其对应的 derivation 却缺失且无法实现。

关键在于理解固定输出 derivation (FOD)。FOD 基于其*内容*而不是 derivation 的属性，具有固定的输出哈希。对 FOD 属性的更改（例如，添加“garbage”属性）会更改 `.drv` 文件路径，但如果内容保持不变，则*不会*更改输出路径。

这造成了一种脱节：二进制缓存可能将特定输出（例如，Ruby 二进制文件）链接到 FOD 的*旧* `.drv`，该 `.drv` 在 FOD 的属性修改后不再存在。这可能会导致混淆，因为 `nix-store --query --deriver` 可能会返回不再存在的过时的 `.drv`。

本文进一步说明，多个 `.drv` 文件可以产生相同的输出，并且 derivation 可以被显着更改（甚至通过删除也产生相同输出的输入 derivation！），但仍然产生相同的输出路径。这说明了输出和 derivation 之间的“1:N”关系，以及更改 derivation 的依赖项到具有相同输出的其他 derivation 不会改变最终结果。这种由 FOD 属性更改驱动的 derivation 变动突出了 Nix 包管理的一个复杂方面，并导致存储路径中出现大量膨胀和混淆。

---

## 42. 香菇菌丝制可持续忆阻器用于高频生物电子学

**原文标题**: Sustainable memristors from shiitake mycelium for high-frequency bioelectronics

**原文链接**: [https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0328965](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0328965)

本文探讨了香菇（Lentinula edodes）作为神经形态计算中可持续且稳健的传统半导体忆阻器替代品的潜力。作者证明，香菇菌丝网络可以与电极连接以创建真菌忆阻器，该忆阻器可以生长、训练和保存，在高频率（高达 5.85 kHz）和高精度（90 ± 1%）下保持功能。

该研究突出了真菌忆阻器的几个优势：它们具有环境可持续性和生物可降解性，动态地调整其电气特性，可能消耗更少的功率，并模拟生物神经元网络。与通常需要稀土矿物和昂贵制造工艺的传统忆阻器相比，香菇提供了一种低成本、可扩展且环保的选择。

此外，本文还讨论了香菇固有的抗辐射性，表明其适用于传统电子产品可能易受攻击的航空航天应用。这种抗性归因于香菇多糖等化合物以及真菌适应不同辐射水平的能力。作者得出结论，真菌计算机可以为神经形态任务提供一个可行的平台，连接生物电子学和非常规计算，并为利用能够承受环境压力的生物实体提供一种可持续的方法。

---

## 43. 安特卫普圣约瑟夫教堂船 – 二战德国混凝土油轮

**原文标题**: Kerkship St. Jozef, Antwerp – WWII German Concrete Tanker

**原文链接**: [https://thecretefleet.com/blog/f/kerkship-st-jozef-antwerp-%E2%80%93-wwii-german-concrete-tanker](https://thecretefleet.com/blog/f/kerkship-st-jozef-antwerp-%E2%80%93-wwii-german-concrete-tanker)

本文介绍“圣约瑟夫教堂号”(Kerkship St. Jozef)，一艘位于安特卫普的混凝土油轮，二战期间由德国人建造。 这篇文章似乎来自“克里特舰队”博客，该网站致力于介绍一战和二战时期的混凝土船和桑葚港组件。该博客使用 Cookie 来分析网站流量并改善用户体验。 接受使用 Cookie 即表示用户数据与其他所有用户数据聚合。“混凝土船视频”为该网站提供支持，并强调版权保护。

---

## 44. 穿山甲 (YC S25) 正在招聘全栈软件工程师 (开源)

**原文标题**: Pangolin (YC S25) is hiring a full stack software engineer (open-source)

**原文链接**: [https://docs.pangolin.net/careers/software-engineer-full-stack](https://docs.pangolin.net/careers/software-engineer-full-stack)

Pangolin（一家YC S25创业公司，致力于构建以身份识别为导向的远程访问解决方案，专注于开源和自托管）正在旧金山招聘一名全栈软件工程师。该职位提供 12.5万-16万美元的年薪，外加 0.5%-1.5% 的股权。理想的候选人将拥有 3 年以上的工作经验，并精通 TypeScript、Go、SQL (PostgreSQL, SQLite)、NextJS 和 AWS。

该职位涉及架构设计、构建和维护 Pangolin 核心系统，重点在于管理 UI、API 和 Schema 的容器。职责包括设计、开发和测试自托管平台的前端（NextJS、Tailwind、ShadCN）和后端（Express APIs、SQL、Drizzle ORM），管理 CICD 和内部工具，解决复杂的系统问题，以及与开源社区互动。

Pangolin 正在寻找适应早期创业公司环境、拥有自己想法并且熟悉 Web 身份标准（OAuth2、OIDC、SSO）、云基础设施（Docker、Kubernetes、Linux、AWS）和基本网络概念的人。

福利包括具有竞争力的薪资、混合办公环境、搬迁援助、无限制 PTO 以及一支小型且相互信任的团队。申请流程包括在 LinkedIn 上与 Owen 联系，提交简历和 GitHub 个人资料，并完成一项有偿的 OSS 项目贡献。该公司强调迭代速度和来自其开源基础的直接用户反馈。

---

## 45. AI爬虫请求带注释的脚本

**原文标题**: AI scrapers request commented scripts

**原文链接**: [https://cryptography.dog/blog/AI-scrapers-request-commented-scripts/](https://cryptography.dog/blog/AI-scrapers-request-commented-scripts/)

亚伦·P·麦克斯温的文章详细描述了他发现AI爬虫请求仅在HTML注释中引用的JavaScript文件，表明一种非人类的解析行为，可能用于LLM训练数据收集。他根据这些爬虫的复杂程度对其进行分类，从使用基本HTTP库的爬虫到模仿真实浏览器的爬虫。麦克斯温提出算法破坏作为一种对策，利用这些机器人的可预测行为。他概述了几种潜在的应对措施：

1.  **公开披露：** 分享机器人行为的见解，以鼓励防御措施。
2.  **IP过滤：** 使用fail2ban等工具，根据识别的模式阻止恶意IP地址。
3.  **解压炸弹（Zip炸弹）：** 提供恶意制作的存档文件，以破坏或崩溃机器人系统，但承认潜在的资源成本和有限的有效性。
4.  **数据投毒：** 提供被投毒的数据，以破坏基于抓取内容训练的LLM，可能导致不正确或被操纵的输出。麦克斯温提倡这种方法，引用研究表明，相对少量的投毒样本就可以显著影响即使是大型模型。他支持使用免费的数据投毒工具，认为鉴于许多机器学习系统不道德的数据收集行为，这是合理的。他承认将数据投毒与机器人访问限制相结合时可能存在复杂情况。

麦克斯温最后强调了积极参与破坏大型科技公司反社会活动的重要性，特别是那些在未经同意的情况下收集数据并训练模型的公司。

---

## 46. 电子护照背后的密码学

**原文标题**: The cryptography behind electronic passports

**原文链接**: [https://blog.trailofbits.com/2025/10/31/the-cryptography-behind-electronic-passports/](https://blog.trailofbits.com/2025/10/31/the-cryptography-behind-electronic-passports/)

本文深入探讨电子护照 (eMRTDs) 背后的密码学原理，解释它们如何防止未经授权的读取、窃听、伪造和复制。eMRTDs 包含一个芯片，其中存储着个人信息和安全特性等数字数据，这些数据按照 ICAO Doc 9303 定义的文件系统结构进行组织。

核心威胁模型区分了拥有和不拥有物理护照访问权限的攻击者，并概述了针对每种攻击者的不同安全目标。本文随后详细介绍了各种密码学机制，重点介绍了从传统协议到现代增强功能的演变。

诸如用于保密的 Basic Access Control (BAC) 等传统方法，由于 MRZ 的低熵和易受暴力破解攻击，已被证明存在缺陷。Passive Authentication (PA) 使用数字签名验证数据真实性，依然稳健。Active Authentication (AA) 旨在通过挑战护照使用私钥签署数据来防止复制。

诸如 Extended Access Control (EAC) 等现代增强功能解决了这些缺点。Chip Authentication (CA) 使用 Diffie-Hellman 密钥交换来加强安全通道。Terminal Authentication (TA) 保护敏感的指纹和虹膜数据 (DG3 和 DG4)。Password Authenticated Connection Establishment (PACE) 替换了 BAC，使用 MRZ 作为密码来防止离线暴力破解攻击。

本文最后强调，总体安全性不仅取决于护照的密码学能力，还取决于与护照交互的检查系统的行动和安全措施。如果系统仅实施基本身份验证方法，则电子复制的风险仍然存在。

---

## 47. 苹果发布第四季度财报

**原文标题**: Apple reports fourth quarter results

**原文链接**: [https://www.apple.com/newsroom/2025/10/apple-reports-fourth-quarter-results/](https://www.apple.com/newsroom/2025/10/apple-reports-fourth-quarter-results/)

苹果公司公布了强劲的2025财年第四季度业绩，营收达到1025亿美元，同比增长8%。经调整后的摊薄后每股收益增长13%，至1.85美元。公司在总营收和iPhone营收方面均创下了9月季度营收纪录，同时服务业务营收也创下了历史新高。

首席执行官蒂姆·库克强调了iPhone 17系列（包括Pro和Pro Max型号）、AirPods Pro 3以及新款Apple Watch系列的成功发布。他还提到了搭载M5芯片的更新版MacBook Pro和iPad Pro。

首席财务官凯文·帕雷克指出，第四季度业绩为创纪录的财年画上了句号，全年营收达到4160亿美元，每股收益实现两位数增长。他还强调了客户的高度满意度和忠诚度，从而使所有产品类别和地理区域的活跃设备安装基数创下历史新高。

苹果公司董事会宣布派发每股0.26美元的现金股息，于2025年11月13日支付给截至2025年11月10日登记在册的股东。财报电话会议于2025年10月30日直播，重播将提供约两周。

---

## 48. Llamafile 回归

**原文标题**: Llamafile Returns

**原文链接**: [https://blog.mozilla.ai/llamafile-returns/](https://blog.mozilla.ai/llamafile-returns/)

Mozilla.ai 采纳 llamafile 项目，以进一步发展开放、本地和注重隐私的 AI 解决方案。Llamafile 允许用户通过单个可执行文件轻松地在本地运行大型语言模型 (LLM)，该文件结合了服务器代码和模型权重。

Mozilla.ai 计划更新 llamafile 代码库，使其基础现代化，整合来自 llama.cpp 的新功能，并根据社区的意见改进其功能。 Llamafile 代码库已正式迁移到 GitHub 上的 Mozilla.ai 组织。

Mozilla.ai 正在积极寻求社区反馈，以塑造下一代 llamafile 的路线图。他们有兴趣了解用户选择 llamafile 的原因、哪些功能最重要、用户可能切换到其他工具的原因，以及哪些改进会使其更有用。反馈可以在 GitHub 讨论区、Mozilla Discord llamafile 频道或 Hacker News 上分享。

现有的 llamafile 用户不会遇到任何变化，他们的工作流程将继续如常。 Mozilla.ai 鼓励当前和潜在用户提供意见并为项目的开发做出贡献。他们将此视为一个社区驱动的努力，以共同构建 llamafile 的下一阶段。

---

## 49. 尼苏斯作家：薛定谔的文字处理器

**原文标题**: Nisus Writer: Schrödinger's Word Processor

**原文链接**: [https://tidbits.com/2025/10/25/nisus-writer-schrodingers-word-processor/](https://tidbits.com/2025/10/25/nisus-writer-schrodingers-word-processor/)

乔·基塞尔的文章将Nisus Writer——一款历史悠久且拥有忠实用户群的Mac文字处理器——描绘成一种岌岌可危的状态，并将其比作薛定谔的猫。Nisus网站经历过宕机，该应用程序也已从Mac App Store消失，引发了人们对该公司未来的担忧。

基塞尔对Nisus Writer有着深厚的个人感情，他详细描述了自己试图联系该公司关键人物（包括创始人耶日·莱瓦克）的尝试，但收效甚微。虽然网站在遭受DDoS攻击后已恢复，并且该应用程序仍然可以运行，但自2024年11月以来，开发和支持似乎已经停止。

基塞尔表达了他对Nisus Writer在未来macOS更新中的兼容性的担忧，因为缺乏积极的维护。他认为，由于市场饱和和软件开发成本，出售该应用程序或吸引投资者是不太可能的。他还批评了Nisus Software缺乏与客户的沟通，强调了支持和更新对于企业生存的重要性。

最终，基塞尔呼吁Nisus Software开源代码，允许社区维护该应用程序并防止其消亡。他提出免费协助进行此过渡。这篇文章描绘了一款备受喜爱但濒临灭绝的软件，突显了Nisus Software迫切需要做出决定以确保其生存。

---

## 50. 拍摄罕见的棕鬣狗潜行于钻石矿业鬼城

**原文标题**: Photographing the rare brown hyena stalking a diamond mining ghost town

**原文链接**: [https://www.bbc.com/future/article/20251014-the-rare-hyena-stalking-a-diamond-mining-ghost-town](https://www.bbc.com/future/article/20251014-the-rare-hyena-stalking-a-diamond-mining-ghost-town)

野生动物摄影师维姆·范登·希弗花了十年时间，试图在纳米比亚废弃的钻石矿镇科尔曼斯科普拍摄到罕见的棕鬣狗。这项努力最终获得了年度野生动物摄影师大奖。

文章重点介绍了棕鬣狗，这种最稀有的鬣狗物种，以及它对利用废弃矿镇作为庇护所和觅食地的非凡适应能力。来自棕鬣狗研究项目的玛丽·勒梅尔强调了鬣狗在沙漠生态系统中至关重要的作用，它们通过食腐海豹幼崽将营养从沿海地区带到内陆。

范登·希弗的坚持不懈包括克服恶劣的沙漠条件、不可靠的风和雾以及鬣狗难以捉摸的本性等挑战。他有策略地放置了相机陷阱，设想鬣狗可能穿过城镇的路线。

虽然鬣狗种群被认为是“近危”，但据信在保护区内，即以前的钻石矿区，相对稳定。然而，由于开发和人类冲突造成的栖息地丧失仍然是持续的威胁。文章表明，像范登·希弗的作品这样的照片可以帮助改变公众对鬣狗的看法，突显它们的生态重要性。

尽管取得了成功，范登·希弗并没有止步，他表示希望继续拍摄鬣狗和鬼城，以获得更引人入胜的图像。

---

## 51. 计划弃用并移除XSLT

**原文标题**: Intent to Deprecate and Remove XSLT

**原文链接**: [https://groups.google.com/a/chromium.org/g/blink-dev/c/CxL4gYZeSJA/m/yNs4EsD5AQAJ](https://groups.google.com/a/chromium.org/g/blink-dev/c/CxL4gYZeSJA/m/yNs4EsD5AQAJ)

本文档概述了从Chromium浏览器中弃用和移除XSLT（可扩展样式表转换语言）的意图。此决定的主要原因是安全考虑以及客户端XSLT的使用量下降，它已被基于JavaScript的技术在很大程度上取代。

浏览器中实现的XSLT v1.0于1999年标准化。存在更新的版本（v2.0、v3.0），但不受支持，导致功能停滞。Chromium使用的libxslt库是一个老化的、复杂的C代码库，容易受到内存安全漏洞的影响。低使用率加上安全风险使XSLT成为一个潜在的攻击面。

计划在M143（2025年12月）中弃用XSLT，并在M155（2026年11月）中移除它，届时将提供Origin Trial和企业策略，以便在M164（2027年8月）之前继续使用。正在开发一个polyfill来缓解兼容性问题。

虽然一些Web开发者会受到不利影响，但存在替代解决方案，并且很大一部分使用XSLT的网站具有回退或在禁用XSLT的情况下保持功能。其他浏览器引擎（Gecko和WebKit）也计划弃用XSLT。

谷歌工程师已经审查了该计划。普遍认为，比之前计划更早地在Canary、Dev和Beta通道中禁用XSLT有助于发现中断。

重要的是，`document.evaluate()`和XPath *不会*作为此过程的一部分被移除。

---

## 52. 睡眠不足导致大脑冲洗液体，进而导致注意力不集中

**原文标题**: Attention lapses due to sleep deprivation due to flushing fluid from brain

**原文链接**: [https://news.mit.edu/2025/your-brain-without-sleep-1029](https://news.mit.edu/2025/your-brain-without-sleep-1029)

麻省理工新闻：睡眠不足后的注意力不集中与脑脊液流动相关

---

## 53. 大型语言模型中的内省迹象

**原文标题**: Signs of introspection in large language models

**原文链接**: [https://www.anthropic.com/research/introspection](https://www.anthropic.com/research/introspection)

本文探讨了像Claude这样的大型语言模型（LLMs）涌现出的内省能力，即思考并报告其自身内部思维过程的能力。研究人员使用可解释性技术，特别是“概念注入”来测试这一点。他们将已知的神经活动模式（代表诸如“全部大写”之类的概念）注入到模型中，然后在不相关的提示中询问模型是否注意到任何异常。

结果表明，最先进的模型（Claude Opus 4和4.1）有时可以检测到这些注入的概念并识别它们，表明其对内部状态具有一定程度的意识。进一步的实验表明，模型可以根据指令或激励调整其内部表示，并且可以通过回顾性地将其输出与其过去的神经活动进行比较，来检测其输出何时与其“意图”不符。

然而，作者强调，这种内省能力是有限的、不可靠的（仅在约20%的时间内有效），并且不一定意味着意识。当内省失败时，模型要么会错过注入，要么会产生幻觉，这表明其对注入强度的敏感性。此外，研究人员表示，通用内省系统的存在是不太可能的，并且他们预计特定的内省任务由狭窄的回路处理。

尽管存在这些局限性，但这些发现意义重大，因为它们挑战了对LLMs能力的假设，并表明随着模型的改进，内省可能会变得更加复杂。这对于通过允许AI系统解释其推理来提高AI系统的透明度、可靠性和可调试性具有重要意义，尽管需要谨慎验证这些自我报告。这项研究还提出了关于AI思维的本质及其潜在道德地位的更广泛的问题。

---

## 54. Show HN: 解决纷争 – 一款点击式冒险节奏游戏

**原文标题**: Show HN: Settling the Score – A point-and-click adventure rhythm game

**原文链接**: [https://easel.games/@raysplaceinspace/settling-the-score/](https://easel.games/@raysplaceinspace/settling-the-score/)

了结恩怨》是一款使用EaselLoading构建的点击式冒险节奏游戏。"Show HN"标志表明创建者正在向Hacker News社区展示他们的项目。 标题暗示了一个通过点击式冒险框架内的节奏游戏来解决冲突（“了结恩怨”）的游戏。

---

## 55. Rouille – 法语中的 Rust 编程

**原文标题**: Rouille – Rust Programming, in French

**原文链接**: [https://github.com/bnjbvr/rouille](https://github.com/bnjbvr/rouille)

Rouille：用法语编写Rust程序的趣味项目

Rouille是一个有趣的开源项目，允许开发者使用法语关键字和语法编写Rust程序。它旨在以幽默的方式看待编程中的本地化，设想未来法国开发出一个完全用法语编写的主权操作系统。

该项目纯粹是玩笑，但也承认了本地化编程语言的潜在用途。Rouille完全兼容标准的英语Rust，允许开发者混合使用这两种语言。本文提供了代码示例，包括`trait`和`impl`分别如何翻译成`convention`和`réalisation`。它还支持法语地区性表达和脏话（魁北克法语也有变体）。

欢迎贡献，重点是添加更多的法语标识符。作者恳请贡献者不要引入过多的亵渎性内容。“但你为什么要这么做？”一节幽默地解释了该项目背后的动机：将对过程宏的有趣实验与对本地化编程语言的严肃应用的调侃结合起来。

文章最后列出了“rust”在其他各种语言中的翻译，最终以“unirust”（所有语言翻译的组合）结尾。感谢VentGrey提供的logo，以及指向“License Publique Rien à Branler”（WTFPL的法语翻译）的链接。

---

## 56. 在英伟达的引领下，人工智能产业计划重振美国工业。

**原文标题**: Led by Nvidia, the AI industry has plans to reindustrialise America

**原文链接**: [https://www.economist.com/united-states/2025/10/30/led-by-nvidia-the-ai-industry-has-plans-to-reindustrialise-america](https://www.economist.com/united-states/2025/10/30/led-by-nvidia-the-ai-industry-has-plans-to-reindustrialise-america)

无法访问文章链接。

---

## 57. 作威作福：一部现代英国贵族的新历史

**原文标题**: Lording it, over: A new history of the modern British aristocracy

**原文链接**: [https://newcriterion.com/article/lording-it-over/](https://newcriterion.com/article/lording-it-over/)

西蒙·赫弗对埃莉诺·多蒂《继承人与恩典：现代英国贵族史》的评论探讨了英国贵族阶层不断变化的命运和生存之道。多蒂的著作考察了世袭贵族的生活，尤其是在1999年上议院改革后，他们大多被从立法机构中移除。

赫弗强调了该书对“真正”贵族的定义，即那些拥有悠久历史头衔和庄园的人，并将他们与较新的贵族区分开来。多蒂探讨了贵族生活的不同现实，不仅展示了贵族义务的例子，还突出了贵族阶层内部的犯罪、怪癖和财政困境。

评论指出，20世纪的重大事件，如世界大战和遗产税，对许多大型庄园的衰落产生了重大影响。它还涉及一些贵族家庭为维持其财产而采取的创造性适应措施，例如向公众开放他们的家园。评论还讨论了贵族在面对挑战时的韧性以及社会对他们角色不断变化的看法。最后，评论承认了贵族阶层在历史上遭受的迫害，引用了伊曼纽尔·辛韦尔的行动等例子，但结论是，这种公然的阶级仇恨时代基本上已经结束。

---

## 58. 蠢货，是“硬件”！

**原文标题**: It's the “hardware”, stupid

**原文链接**: [https://haebom.dev/archive?post=4w67rj24q76nrm5yq8ep](https://haebom.dev/archive?post=4w67rj24q76nrm5yq8ep)

时代周刊2025年度最佳发明（硬件篇）：涵盖机器人、航空航天、农业及无障碍领域。

**机器人：**重点包括家用机器人(EufyMake E1)、纹理家居打印(UV Printer)、个人摄像无人机(HoverAir X1 ProMax)和超敏捷人形机器人(Unitree R1)。

**无障碍：**值得关注的发明包括盲文及图形平板电脑(American Printing House Monarch)、智能家居戒指(Lotus Ring)和易于使用的润唇膏涂抹器(Tilt Grip Stick)。

**航空航天：**创新聚焦于太空互联网(AST SpaceMobile BlueBird)、月球任务(Firefly Blue Ghost)、野火探测卫星(FireSat)和先进的天文观测(Vera C. Rubin Observatory)。

**农业：**特色进展包括减少牲畜甲烷排放(FutureFeed Asparagopsis Supplement)、气候智能型咖啡品种(Innovea Global Coffee Breeding Network)、电动除草(RootWave eWeeder)、自动化葡萄园管理(Scout Gen 5)、高效收割(Thunderstruck Razors Edge Concaves)和数据驱动的香草固化(Vanilla Vida)。

该榜单展示了一种趋势，即专门的硬件解决方案正在解决各个领域中的特定问题，强调创新和实用性。“关键在于‘硬件’，笨蛋”的标题暗示，文章将阐述这些有形的、物理的发明的重要性及影响。

---

## 59. 软盘 // retrocmp / 复古计算

**原文标题**: Floppy Disk / Diskettes // retrocmp / retro computing

**原文链接**: [https://retrocmp.de/fdd/diskette/diskette.htm](https://retrocmp.de/fdd/diskette/diskette.htm)

本文全面概述了软盘（也称磁盘），这是一种现已过时的数据存储技术，主要用于 20 世纪末。文章涵盖了各种方面，包括不同尺寸（8 英寸、5.25 英寸、3.5 英寸和 3 英寸）、硬扇区和软扇区磁盘的区别，以及具有不同扇区孔数的硬扇区磁盘的具体示例。

文章详细介绍了索引孔和写保护/启用槽口的功能，解释了这些物理特征如何控制不同软盘类型的写入权限。具体而言，文章阐明了 8 英寸和 5.25 英寸磁盘之间写保护机制的差异。

文章提供了硬扇区磁盘的示例，重点介绍了具有 10 个和 16 个扇区孔的磁盘，并指出了它们在特定计算机系统中的使用，如 Heathkit H89、North Star Horizon、AES Data Inc.、Honeywell Bull 和 Vector Graphic。作者分享了获得一个罕见的带有 10 个扇区孔的 5.25 英寸硬扇区磁盘的个人轶事。

文章还包括来自 3M 和 boeder 等制造商的交付程序/产品清单链接，列出了他们生产的各种类型的软盘。最后，文章指向外部资源，例如维基百科上关于软盘历史的条目以及 Herb Johnson 撰写的详细技术文章，以提供进一步阅读和更深入的技术见解。

---

## 60. 如果飞行员弹射，自动驾驶系统会被编程为做什么？ (2018)

**原文标题**: If a pilot ejects, what is the autopilot programmed to do? (2018)

**原文链接**: [https://aviation.stackexchange.com/questions/52862/if-a-pilot-ejects-what-is-the-autopilot-programmed-to-do](https://aviation.stackexchange.com/questions/52862/if-a-pilot-ejects-what-is-the-autopilot-programmed-to-do)

Stack Exchange 上的这个帖子讨论了飞行员从军用飞机弹射后，自动驾驶系统会发生什么。最初的问题提出，理想情况下，自动驾驶系统应该尝试自动降落飞机，或者引导飞机飞往人口较少的地区，以节省资金并可能避免伤害。

一些回答指出，弹射是最后的手段，表明飞机已经失控或接近失控。弹射本身也会破坏飞机的稳定性。因此，期望自动驾驶系统成功降落或控制受损飞机是不现实的。弹射本身也具有内在的危险性，存在不可忽略的失败率，弹射会对身体施加高重力加速度。

一些回答建议，根据情况和飞机的位置（例如，在敌方领土上空），自动驾驶系统可能会被编程为启动自毁程序，以防止敌人回收敏感技术。另一些人指出，在某些情况下，如果时间和条件允许，飞行员可能会对自动驾驶系统进行编程，使其“直线飞行并保持水平”或飞向水面，以尽量减少损失。普遍的看法是，自动驾驶系统基本上会继续执行弹射前编程的指令。考虑到可能造成的损害，自动驾驶系统不太可能阻止坠机。增加复杂的弹射触发式自动驾驶行为会带来关于误判的安全问题，并且不会显著改善情况。

---

## 61. 克劳德中断

**原文标题**: Claude outage

**原文链接**: [https://status.claude.com/incidents/s5f75jhwjs6g](https://status.claude.com/incidents/s5f75jhwjs6g)

2025年10月31日，Claude.ai出现错误率升高现象。事件调查始于UTC时间09:25。至UTC时间10:18，问题被确认并开始实施修复。修复后于UTC时间10:23开始监控。UTC时间10:55和15:06发布了进一步的监控更新。事件于UTC时间18:32解决，平台将持续受到监控，以防潜在的进一步问题。该事件仅影响claude.ai。

---

## 62. 约翰·卡马克论可变变量

**原文标题**: John Carmack on mutable variables

**原文链接**: [https://twitter.com/id_aa_carmack/status/1983593511703474196](https://twitter.com/id_aa_carmack/status/1983593511703474196)

提供的文本并非关于约翰·卡马克或可变变量的文章，而是X公司（原推特）的一段声明，指出用户的浏览器禁用了JavaScript。它提供了启用JavaScript或切换到受支持的浏览器的说明，以便使用该平台。其中还包含帮助中心、服务条款、隐私政策、Cookie政策、版本说明、广告信息和版权声明的链接。

因此，没有关于约翰·卡马克或可变变量的信息可供总结。核心信息是一个技术问题，阻止用户访问该平台。

---

## 63. 1924年新墨西哥州区域性银行挤兑

**原文标题**: The 1924 New Mexico regional banking panic

**原文链接**: [https://nodumbideas.com/p/labor-day-special-the-1924-new-mexico](https://nodumbideas.com/p/labor-day-special-the-1924-new-mexico)

本文探讨了1924年新墨西哥州的银行挤兑事件，并将其与2023年硅谷银行（SVB）的倒闭相提并论。这次挤兑源于过度杠杆化的养牛户在战时价格虚高期间贷款，却遭遇了商品价格暴跌和20年代的严重干旱。这导致了广泛的银行倒闭，而许多州特许银行并非联邦储备系统成员，无法获得最后贷款人，更使情况恶化。流动性是银行生存的主要驱动因素，持有更多流动资产的银行能更好地度过难关。

联邦储备局采取了引人注目的干预措施，空运了50万美元现金到阿尔伯克基的银行。这与财政部和战争金融公司强有力的支持声明相结合，恢复了对银行体系的信心。美联储还通过贴现窗口向陷入困境的银行提供了谨慎的贷款，间接支持了州特许银行。

作者将此与SVB危机进行比较，强调了涉及恐慌、溢出效应和后续干预的金融恐慌的周期性。他还注意到，州特许银行缺乏美联储准入与当前去中心化金融（DeFi）领域之间存在相似之处，并暗示传统银行和DeFi之间日益增长的相互依赖性可能导致未来需要类似干预策略的危机。

---

## 64. .arpa、反向域名解析和一些神奇的ICMP技巧

**原文标题**: .arpa, rDNS and a few magical ICMP hacks

**原文链接**: [https://sdomi.pl/weblog/24-arpa-hacks/](https://sdomi.pl/weblog/24-arpa-hacks/)

本文探讨了.arpa域的非常规用法，这些域通常保留给反向DNS（rDNS），并深入研究了ICMP（Internet控制消息协议）黑客技术。作者从其ISP处获得了ip6.arpa区域的委派，这引发了一系列实验，推动了这些域通常用途的界限。

文章解释了.arpa的历史，其用于传统ARPANET服务的最初目的，以及其目前在反向DNS中的作用，即将IP地址映射到域名。然后，作者演示了如何将rDNS区域用于正向DNS，托管Web内容，甚至运行GoToSocial（联邦宇宙）实例和邮件服务器。 这是通过创造性地使用DNS记录并绕过典型的安全限制来实现的。 Cloudflare为.arpa子域名颁发的TLS证书在运行GoToSocial实例中发挥了关键作用。

然后，作者深入研究了ICMP，特别是探索了使用ICMP Echo请求创建虚假traceroute响应的潜力。这涉及到用Bash编写自定义IPv6协议栈，利用socat创建TUN接口，并操纵ICMP数据包，以根据标识符和序列号生成定制的响应。这需要一种无状态的方法来避免状态管理问题，并涉及到校验和计算。 该项目突出了限制如何激发网络编程中的创造性解决方案。

---

## 65. Typst: 从一开始就创建可访问的PDF

**原文标题**: Typst: How to create accessible PDFs from the start

**原文链接**: [https://typst.app/blog/2025/accessible-pdf/](https://typst.app/blog/2025/accessible-pdf/)

本文重点介绍了Typst从一开始就创建无障碍PDF的方法，并将其与需要大量后期处理和手动调整的传统方法进行对比。作者认为，在其他软件中，无障碍性通常是事后才考虑的问题，导致耗时且昂贵的修正。

Typst是一个基于标记的写作平台，它通过使用语义元素来优先考虑无障碍性。这些元素，例如标题、图形和表格，会自动生成必要的PDF标签，这对于屏幕阅读器兼容性至关重要。与其他软件不同，Typst鼓励使用这些元素，确保无障碍性成为写作过程的自然组成部分。

本文强调了PDF中语义数据对于正确阅读顺序、图像描述和语言设置等功能的重要性。它将Typst的方法与缺乏语义意义并阻碍无障碍性的手动格式化进行对比。

促成Typst无障碍性的关键功能包括：使用特定的表格元素来表示标题和页脚，使用`table`来显示数据，使用`grid`来进行设计，使用`list`、`enum`或`terms`元素来表示列表，以及使用`alt`参数为图像提供替代文本描述。

Typst还提供PDF/UA-1导出功能，并内置验证，以检查诸如缺少替代描述之类的无障碍问题，并在发现问题时阻止PDF创建。通过利用语义元素和内置验证，Typst使创建无障碍PDF成为一个无缝且高效的过程，将无障碍性从合规负担转变为使用该平台的自然优势。本文鼓励用户探索Typst的功能和无障碍指南，以创建普遍可访问的文档。

---

## 66. 在轨道上，减速才能加速。

**原文标题**: In orbit you have to slow down to speed up

**原文链接**: [https://www.wired.com/story/in-orbit-you-have-to-slow-down-to-speed-up/](https://www.wired.com/story/in-orbit-you-have-to-slow-down-to-speed-up/)

本文解释了轨道力学违反直觉的特性，重点说明了在轨道上加速实际上会导致你落后于目标，而减速可以帮助你赶上目标。关键概念是轨道速度与轨道半径直接相关。

文章首先解释了圆轨道受向心加速度、引力和牛顿第二定律支配。它推导出一个公式，表明在给定半径下，稳定的圆轨道需要特定的速度。

文章随后模拟了一次对接操作，演示了简单地启动推进器加速以追赶空间站，实际上会增加轨道半径，并使航天器相对于目标减速。相反，减速会减小轨道半径，使航天器能够赶上并超过空间站。

为了实现成功的轨道转移，文章介绍了霍曼转移。这种操作包括减速进入一个椭圆轨道，使航天器更接近所需的轨道半径。一旦到达椭圆轨道上的最近点（近拱点），航天器再次加速，以达到在新半径下的稳定圆轨道所需的正确速度。这项技术也适用于行星际旅行。简而言之，轨道导航非常违反直觉，类似于一个“相反的世界”，加速和减速不会产生你期望的效果。

---

## 67. 结果是我唯一需要的。

**原文标题**: Result is all I need

**原文链接**: [https://rockyj-blogs.web.app/2025/10/25/result-monad.html](https://rockyj-blogs.web.app/2025/10/25/result-monad.html)

本文探讨了人工智能对软件开发的影响，以及如何在人工智能辅助的环境中保持代码质量，特别是代码组织。文章强调，虽然人工智能可以生成代码，但适当的代码组织对于可读性和可维护性至关重要。

作者提出了一种以以下几点为中心的代码组织策略：

*   **按角色分组：** 使用类、模块或命名空间根据其目的对函数进行分组。
*   **数据与逻辑：** 将数据持有类与包含逻辑的类分开。
*   **分而治之：** 将接口和基础代码（控制器、数据库访问、外部连接）与服务层业务逻辑隔离。
*   **无状态性：** 强调基础和Service层代码的无状态性。
*   **小函数：** 保持Service函数简洁并专注于单个任务。

文章随后介绍了使用“Result”单子的概念来将这些组织良好的、隔离的函数联系起来。“Result”单子被呈现为一个包装器，用于处理异常和空值检查，从而在组合函数时实现更简洁和更具声明性的代码。文章提供了代码示例，展示了“Result”单子如何通过链接函数并一致地处理潜在的错误和空值，来提高身份验证逻辑的可读性和安全性。该代码展示了如何使用功能块的成功和失败，从而通过使用Result和函数式编程安全地将其全部连接起来，从而改进错误处理以获得出色的结果！

---

## 68. Nutella maker in hazelnut stand-off with Turkish dealers

**原文标题**: Nutella maker in hazelnut stand-off with Turkish dealers

**原文链接**: [https://www.ft.com/content/4826dfd2-8d8e-4316-931f-974f604a3899](https://www.ft.com/content/4826dfd2-8d8e-4316-931f-974f604a3899)

生成摘要时出错

---

## 69. Wheels for free-threaded Python now available for psutil

**原文标题**: Wheels for free-threaded Python now available for psutil

**原文链接**: [https://gmpy.dev/blog/2025/wheels-for-free-threaded-python-now-available-in-psutil](https://gmpy.dev/blog/2025/wheels-for-free-threaded-python-now-available-in-psutil)

生成摘要时出错

---

## 70. Bertie the Brain

**原文标题**: Bertie the Brain

**原文链接**: [https://en.wikipedia.org/wiki/Bertie_the_Brain](https://en.wikipedia.org/wiki/Bertie_the_Brain)

生成摘要时出错

---

## 71. x86 architecture 1 byte opcodes

**原文标题**: x86 architecture 1 byte opcodes

**原文链接**: [https://www.sandpile.org/x86/opc_1.htm](https://www.sandpile.org/x86/opc_1.htm)

生成摘要时出错

---

## 72. Just use a button

**原文标题**: Just use a button

**原文链接**: [https://gomakethings.com/just-use-a-button/](https://gomakethings.com/just-use-a-button/)

生成摘要时出错

---

## 73. History's first public hack: rats, rats, rats

**原文标题**: History's first public hack: rats, rats, rats

**原文链接**: [https://www.rigb.org/explore-science/explore/blog/historys-first-public-hack-rats-rats-rats](https://www.rigb.org/explore-science/explore/blog/historys-first-public-hack-rats-rats-rats)

生成摘要时出错

---

## 74. A Closer Look at Piezoelectric Crystal

**原文标题**: A Closer Look at Piezoelectric Crystal

**原文链接**: [https://www.samaterials.com/content/a-closer-look-at-stressed-piezo-crystals.html](https://www.samaterials.com/content/a-closer-look-at-stressed-piezo-crystals.html)

生成摘要时出错

---

## 75. It's insulting to read AI-generated blog posts

**原文标题**: It's insulting to read AI-generated blog posts

**原文链接**: [https://blog.pabloecortez.com/its-insulting-to-read-your-ai-generated-blog-post/](https://blog.pabloecortez.com/its-insulting-to-read-your-ai-generated-blog-post/)

生成摘要时出错

---

## 76. Canva’s affinity strategy: Normies over power users

**原文标题**: Canva’s affinity strategy: Normies over power users

**原文链接**: [https://tedium.co/2025/10/30/canva-affinity-free-loss-leader-strategy/](https://tedium.co/2025/10/30/canva-affinity-free-loss-leader-strategy/)

生成摘要时出错

---

## 77. AMD could enter ARM market with Sound Wave APU built on TSMC 3nm process

**原文标题**: AMD could enter ARM market with Sound Wave APU built on TSMC 3nm process

**原文链接**: [https://www.guru3d.com/story/amd-enters-arm-market-with-sound-wave-apu-built-on-tsmc-3nm-process/](https://www.guru3d.com/story/amd-enters-arm-market-with-sound-wave-apu-built-on-tsmc-3nm-process/)

生成摘要时出错

---

## 78. Israel demanded Google and Amazon use secret 'wink' to sidestep legal orders

**原文标题**: Israel demanded Google and Amazon use secret 'wink' to sidestep legal orders

**原文链接**: [https://www.theguardian.com/us-news/2025/oct/29/google-amazon-israel-contract-secret-code](https://www.theguardian.com/us-news/2025/oct/29/google-amazon-israel-contract-secret-code)

生成摘要时出错

---

## 79. Show HN: Quibbler – A critic for your coding agent that learns what you want

**原文标题**: Show HN: Quibbler – A critic for your coding agent that learns what you want

**原文链接**: [https://github.com/fulcrumresearch/quibbler](https://github.com/fulcrumresearch/quibbler)

生成摘要时出错

---

## 80. How to build silos and decrease collaboration on purpose

**原文标题**: How to build silos and decrease collaboration on purpose

**原文链接**: [https://www.rubick.com/how-to-build-silos-and-decrease-collaboration/](https://www.rubick.com/how-to-build-silos-and-decrease-collaboration/)

生成摘要时出错

---

## 81. Denmark reportedly withdraws Chat Control proposal following controversy

**原文标题**: Denmark reportedly withdraws Chat Control proposal following controversy

**原文链接**: [https://therecord.media/demark-reportedly-withdraws-chat-control-proposal](https://therecord.media/demark-reportedly-withdraws-chat-control-proposal)

生成摘要时出错

---

## 82. Show HN: In a single HTML file, an app to encourage my children to invest

**原文标题**: Show HN: In a single HTML file, an app to encourage my children to invest

**原文链接**: [https://roberdam.com/en/dinversiones.html](https://roberdam.com/en/dinversiones.html)

生成摘要时出错

---

## 83. Spinning Up an Onion Mirror Is Stupid Easy

**原文标题**: Spinning Up an Onion Mirror Is Stupid Easy

**原文链接**: [https://flower.codes/2025/10/23/onion-mirror.html](https://flower.codes/2025/10/23/onion-mirror.html)

生成摘要时出错

---

## 84. Lenses in Julia

**原文标题**: Lenses in Julia

**原文链接**: [https://juliaobjects.github.io/Accessors.jl/stable/lenses/](https://juliaobjects.github.io/Accessors.jl/stable/lenses/)

生成摘要时出错

---

## 85. Fungus: The Befunge CPU (2015)

**原文标题**: Fungus: The Befunge CPU (2015)

**原文链接**: [https://www.bedroomlan.org/hardware/fungus/](https://www.bedroomlan.org/hardware/fungus/)

生成摘要时出错

---

## 86. Launch HN: Propolis (YC X25) – Browser agents that QA your web app autonomously

**原文标题**: Launch HN: Propolis (YC X25) – Browser agents that QA your web app autonomously

**原文链接**: [https://app.propolis.tech/#/launch](https://app.propolis.tech/#/launch)

生成摘要时出错

---

## 87. How the cochlea computes (2024)

**原文标题**: How the cochlea computes (2024)

**原文链接**: [https://www.dissonances.blog/p/the-ear-does-not-do-a-fourier-transform](https://www.dissonances.blog/p/the-ear-does-not-do-a-fourier-transform)

生成摘要时出错

---

## 88. Who needs Graphviz when you can build it yourself?

**原文标题**: Who needs Graphviz when you can build it yourself?

**原文链接**: [https://spidermonkey.dev/blog/2025/10/28/iongraph-web.html](https://spidermonkey.dev/blog/2025/10/28/iongraph-web.html)

生成摘要时出错

---

## 89. Rotating Workforce Scheduling in MiniZinc

**原文标题**: Rotating Workforce Scheduling in MiniZinc

**原文链接**: [https://zayenz.se/blog/post/rotating-workforce-scheduling/](https://zayenz.se/blog/post/rotating-workforce-scheduling/)

生成摘要时出错

---

## 90. Jack Kerouac, Malcolm Cowley, and the difficult birth of On the Road

**原文标题**: Jack Kerouac, Malcolm Cowley, and the difficult birth of On the Road

**原文链接**: [https://theamericanscholar.org/scrolling-through/](https://theamericanscholar.org/scrolling-through/)

生成摘要时出错

---

## 91. Reasoning models reason well, until they don't

**原文标题**: Reasoning models reason well, until they don't

**原文链接**: [https://arxiv.org/abs/2510.22371](https://arxiv.org/abs/2510.22371)

生成摘要时出错

---

## 92. 987654321 / 123456789

**原文标题**: 987654321 / 123456789

**原文链接**: [https://www.johndcook.com/blog/2025/10/26/987654321/](https://www.johndcook.com/blog/2025/10/26/987654321/)

生成摘要时出错

---

## 93. Taking money off the table

**原文标题**: Taking money off the table

**原文链接**: [https://zachholman.com/posts/money-off-the-table](https://zachholman.com/posts/money-off-the-table)

生成摘要时出错

---

## 94. I Love My Wife, My Wife Is Dead (1946)

**原文标题**: I Love My Wife, My Wife Is Dead (1946)

**原文链接**: [https://www.bingqiangao.com/poetry/i-love-my-wife-my-wife-is-dead](https://www.bingqiangao.com/poetry/i-love-my-wife-my-wife-is-dead)

生成摘要时出错

---

## 95. Phone numbers for use in TV shows, films and creative works

**原文标题**: Phone numbers for use in TV shows, films and creative works

**原文链接**: [https://www.acma.gov.au/phone-numbers-use-tv-shows-films-and-creative-works](https://www.acma.gov.au/phone-numbers-use-tv-shows-films-and-creative-works)

生成摘要时出错

---

## 96. Minecraft removing obfuscation in Java Edition

**原文标题**: Minecraft removing obfuscation in Java Edition

**原文链接**: [https://www.minecraft.net/en-us/article/removing-obfuscation-in-java-edition](https://www.minecraft.net/en-us/article/removing-obfuscation-in-java-edition)

生成摘要时出错

---

## 97. Independently verifying Go's reproducible builds

**原文标题**: Independently verifying Go's reproducible builds

**原文链接**: [https://www.agwa.name/blog/post/verifying_go_reproducible_builds](https://www.agwa.name/blog/post/verifying_go_reproducible_builds)

生成摘要时出错

---

## 98. Tips for stroke-surviving software engineers

**原文标题**: Tips for stroke-surviving software engineers

**原文链接**: [https://blog.j11y.io/2025-10-29_stroke_tips_for_engineers/](https://blog.j11y.io/2025-10-29_stroke_tips_for_engineers/)

生成摘要时出错

---

## 99. Warp Terminal changes pricing model

**原文标题**: Warp Terminal changes pricing model

**原文链接**: [https://www.warp.dev/blog/warp-new-pricing-flexibility-byok](https://www.warp.dev/blog/warp-new-pricing-flexibility-byok)

生成摘要时出错

---

## 100. New analog chip capable of outperforming top-end GPUs by as much as 1000x

**原文标题**: New analog chip capable of outperforming top-end GPUs by as much as 1000x

**原文链接**: [https://www.livescience.com/technology/computing/china-solves-century-old-problem-with-new-analog-chip-that-is-1-000-times-faster-than-high-end-nvidia-gpus](https://www.livescience.com/technology/computing/china-solves-century-old-problem-with-new-analog-chip-that-is-1-000-times-faster-than-high-end-nvidia-gpus)

生成摘要时出错

---

