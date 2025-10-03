# Hacker News 热门文章摘要 (2025-10-03)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 德国必须坚决反对聊天监控中的客户端扫描 [pdf]

**原文标题**: Germany must stand firmly against client-side scanning in Chat Control [pdf]

**原文链接**: [https://signal.org/blog/pdfs/germany-chat-control.pdf](https://signal.org/blog/pdfs/germany-chat-control.pdf)

题为“德国必须坚决反对聊天控制中的客户端扫描”的文件是一份包含二进制数据的PDF文件。虽然PDF的结构清晰，但其内容经过混淆处理，且大多包含非人类可读字符。标题表明该文件反对“聊天控制”中的“客户端扫描”，这可能是一种为监控在线通信而提出或实施的系统。

在此背景下，客户端扫描可能指的是在用户设备上*发送之前*扫描消息的方法，而不是在中央服务器上扫描。这引发了重大的隐私问题。该文件的标题认为，德国应该抵制这种类型的监控。

由于PDF内容本质上是乱码，因此无法提供关于该文件推理的具体论点或细节。但是，标题清楚地表明了其立场：反对聊天控制中的客户端扫描。该文件可能深入探讨了这种系统的隐私影响和潜在滥用，特别是从德国法律和伦理的角度来看。

---

## 2. Litestream v0.5.0

**原文标题**: Litestream v0.5.0

**原文链接**: [https://fly.io/blog/litestream-v050-is-here/](https://fly.io/blog/litestream-v050-is-here/)

本文宣布发布 Litestream v0.5.0，这是 SQLite 开源备份/恢复系统的重要更新。本次更新着重于速度提升和高效的时间点恢复 (PITR)。

核心变更是采用了 LTX 文件格式，该格式之前用于另一个 SQLite 项目 LiteFS。LTX 允许 Litestream 在页面级别捕获和压缩更改，而不是仅仅依赖 WAL 文件。这带来了更快的恢复时间，通过分层压缩系统（30 秒、5 分钟和 1 小时窗口）实现。

本次更新还消除了“代”的概念，简化了使用多个 Litestream 实例时的备份过程。现在它使用单调递增的事务 ID 来跟踪数据库状态。

从 v0.3.x 升级非常简单——只需开始使用新版本即可。配置文件向后兼容，但为了简单和可靠性，现在每个数据库强制执行单个副本目标。

其他改进包括 LTX 文件中的每页压缩和索引，从而实现未来的功能，例如无需下载整个数据库即可进行时间点查询。CGO 已被移除，现在使用 modernc.org/sqlite，并添加了 NATS JetStream 的副本类型。S3、Google Storage 和 Azure Blob Storage 的客户端已更新。

下一个正在开发的主要功能是 Litestream VFS，用于只读副本，在数据库的其余部分从对象存储中恢复时，能够立即访问数据库副本。

---

## 3. 经济学博士就业市场的崩溃

**原文标题**: The Collapse of the Econ PhD Job Market

**原文链接**: [https://www.chrisbrunet.com/p/the-collapse-of-the-econ-phd-job](https://www.chrisbrunet.com/p/the-collapse-of-the-econ-phd-job)

克里斯托弗·布鲁内特的文章《经济学博士就业市场的崩溃》指出，经济学博士学位曾经是获得终身教职或其他高薪职位的可靠途径，但现在却成了一场高风险的赌博。该文章利用美国经济学会的“经济学家职位空缺”(JOE)和经济学就业市场(EJM)的数据，证明了过去三年职位发布和面试邀请的数量大幅下降。自2022年以来，终身教职的数量减少了大约35%。

在职位需求暴跌的同时，博士毕业生的数量却在上升，同时还有大量的博士后和访问学者积压。文章引用数据显示，只有一小部分美国博士生能获得终身教职。

布鲁内特将这种下降归因于几个结构性因素：经济学本科生入学人数下降、迫在眉睫的人口断崖、人工智能的兴起正在自动化以前由经济学家完成的任务，以及由于对通货膨胀的错误信息而导致的公众信任丧失。他还指出，政府、国际组织和科技行业对经济学家的招聘正在萎缩。

作者的结论是，经济学博士学位不再是一项安全的投资，并认为随着传统学术职位的日益稀缺，经济学讨论的未来可能会转向Substack等去中心化平台。他呼吁博士项目减少招生，以避免进一步淹没市场。

---

## 4. 社交焦虑并非在于被人喜欢。

**原文标题**: Social anxiety isn't about being liked

**原文链接**: [https://chrislakin.blog/p/social-anxiety](https://chrislakin.blog/p/social-anxiety)

克里斯·莱金的文章挑战了一种常见的假设，即社交焦虑源于被喜欢的渴望。相反，他认为其根本在于避免被讨厌。社交焦虑行为，例如退缩、缺乏自信和避免冒险，如果目标是被人喜欢，似乎适得其反，但它们是最大限度地减少负面关注或评判机会的有效策略。

作者使用财务不安全感作类比，重点在于避免破产而不是最大化利润。同样，社交焦虑的人优先考虑避免负面的社交结果，而不是追求受欢迎。亲密友谊中的“反信号”概念进一步说明了这一点，因为这些关系中的舒适感允许进行风险较高、可能尴尬的互动。

文章认为，理解这种视角的转变可以带来解放。经历社交焦虑的人常常觉得自己是失败者，因为他们认为自己未能被人喜欢。然而，如果根本目标是避免被讨厌，他们的行为就变得合乎逻辑。认识到这一点使他们能够重新构建自己的经历，并专注于解决根本原因：对被讨厌可能性的不适。因此，解决方案不是更加努力地争取认可，而是变得更能接受潜在的不赞同。

---

## 5. Webbol：一个用COBOL编写的极简静态Web服务器

**原文标题**: Webbol: A minimal static web server written in COBOL

**原文链接**: [https://github.com/jmsdnns/webbol](https://github.com/jmsdnns/webbol)

Webbol：使用GnuCOBOL编写的极简开源COBOL静态Web服务器。它从当前目录提供文件，自动检测常见文件格式的MIME类型，并提供标准HTTP状态码。安全特性包括路径遍历防护和目录访问限制。

要使用Webbol，需要在POSIX兼容系统（Linux、macOS、BSD）上安装GnuCOBOL。服务器使用`make`构建，并运行`webserver`可执行文件启动。默认情况下，它在8080端口提供内容，并在根目录中查找`index.html`。可以通过修改`config.cpy`并重新编译来更改端口等配置。

Webbol支持常见的MIME类型，如HTML、CSS、JavaScript、JSON、图像和文本。可以通过编辑`mime-types.cbl`文件添加其他MIME类型。

局限性包括单线程操作、无SSL/TLS支持、64KB文件大小限制以及无缓存或压缩。它专为提供简单的静态内容而设计。项目结构包括用于配置、套接字定义、HTTP和文件结构定义、路径实用程序、MIME类型处理、文件操作以及HTTP请求/响应处理的文件。Webbol证明了COBOL可用于现代系统编程任务。

---

## 6. 我把乐高Game Boy变成了能用的Game Boy

**原文标题**: I Turned the Lego Game Boy into a Working Game Boy

**原文链接**: [https://blog.nataliethenerd.com/i-turned-the-lego-game-boy-into-a-working-game-boy-part-1/](https://blog.nataliethenerd.com/i-turned-the-lego-game-boy-into-a-working-game-boy-part-1/)

娜塔莉（网名@natalie_thenerd）正在记录她将乐高Game Boy套装改造成完全可用的Game Boy的宏伟项目。凭借其Game Boy硬件的渊博知识（详见她的电路板扫描维基），她正在设计一个定制PCB，使其能够安装在乐高套装内。

娜塔莉选择了Game Boy Pocket (MGB) CPU，因为它具有内部VRAM、成本效益和可用性，与原始DMG CPU相比，更适合这种空间受限的构建。

娜塔莉利用新闻图片并将它们缩放到实际尺寸，战略性地计划将Game Boy组件放置在乐高构建的屏幕插入区域内。 PCB设计包含一个定制电源电路（源自她的Safer Charger电路板）、一个软锁电源按钮以及按钮矩阵和音频的引脚。

考虑到乐高按钮的功能，她将它们连接到定制的3D打印“玩具砖”部件，以便与Game Boy连接。 同样，她还集成了一个USB-C端口。

该项目仍在开发中，娜塔莉目前正在获得实体乐高套装后改进电路板。她计划在完成后发布完整的项目细节，并鼓励读者继续关注更新。

---

## 7. Depot (YC W23) 招聘首席设计工程师（美国/欧盟 远程办公）

**原文标题**: Depot (YC W23) Is Hiring a Principal Design Engineer (Remote US/EU)

**原文链接**: [https://www.ycombinator.com/companies/depot/jobs/qg8iVTz-principal-design-engineer](https://www.ycombinator.com/companies/depot/jobs/qg8iVTz-principal-design-engineer)

Depot（YC W23）是一家致力于通过提升构建性能来加速软件开发的公司，现招聘首席设计工程师。该职位为远程办公，面向美国和欧洲的候选人开放，薪资范围为 20 万美元至 25 万美元，并提供股权期权（0.05% - 0.15%）。

Depot 旨在通过一个集性能、共情和集中式协作为一体的平台，重新定义软件协作。首席设计工程师将是关键贡献者，与工程团队和创始人紧密合作，负责从概念到完成的项目。职责包括亲身参与路线图项目的设计和交付、收集客户反馈、重新设计关键产品流程、创建原型和高保真视觉效果、实施轻量级设计系统，以及协助未来的团队招聘。

理想的候选人拥有 7 年以上的软件设计经验，是能够适应模糊性的自启动者，能够将复杂问题转化为专注的设计解决方案，并具有强大的原型设计和沟通能力。Depot 重视主人翁精神、数据驱动的决策和异步协作。

Depot 的平台通过加速构建过程，帮助 PostHog 和 Wistia 等公司节省大量时间，从而提高开发人员的生产力和幸福感。他们的使命是坚持不懈地加速软件开发，消除缓慢构建的“障碍”。

---

## 8. Niri - 一款可滚动平铺的Wayland合成器

**原文标题**: Niri – A scrollable-tiling Wayland compositor

**原文链接**: [https://github.com/YaLTeR/niri](https://github.com/YaLTeR/niri)

Niri 是一个稳定的、可滚动平铺的 Wayland 合成器，从头开始构建，专为多显示器设置和动态工作区而设计。与传统的平铺窗口管理器不同，Niri 在每个显示器的无限条带上以列排列窗口，防止窗口在屏幕之间溢出。它具有动态工作区、可缩放的概览、内置屏幕截图 UI、显示器/窗口屏幕广播、触摸板/鼠标手势、选项卡式窗口和可配置的布局选项。

Niri 支持分数缩放、NVIDIA GPU 和浮动窗口。它还与 Xwayland 集成。它支持平板电脑、触摸板和触摸屏等输入设备，并实现了重要的 Wayland 协议，如 layer-shell 和 screencopy。

该合成器正在积极开发中，并被许多人日常使用。该项目提供诸如入门页面、相关项目列表 (awesome-niri) 和用于支持的 Matrix 频道等资源。

Niri 的一些媒体报道包括在 2024 年莫斯科 RustCon 上的演讲、在德国播客 Das Triumvirat 上的采访以及 LWN 上的一篇文章。

欢迎对 Niri 做出贡献，该项目从 PaperWM 中汲取灵感，后者在 GNOME Shell 上实现了可滚动平铺。该项目还列出了其他类似的平铺项目，如 karousel、scroll、papersway、hyprscrolling、hyprslidr 和 PaperWM.spoon。

---

## 9. 安杜里尔和帕兰提尔战场通信系统存在严重缺陷：陆军

**原文标题**: Anduril and Palantir battlefield comms system has deep flaws: Army

**原文链接**: [https://www.cnbc.com/2025/10/03/anduril-palantir-ngc2-deep-flaws-army.html](https://www.cnbc.com/2025/10/03/anduril-palantir-ngc2-deep-flaws-army.html)

一份美国陆军备忘录揭示了由安杜里尔、帕兰提尔和其他承包商开发的下一代战场通信系统（NGC2）存在严重的安全漏洞。该备忘录由陆军首席技术官撰写，将该系统描述为构成“极高风险”，原因是存在“根本性安全”问题和漏洞。

NGC2平台旨在将士兵、传感器、车辆和指挥官与实时数据连接起来，但存在诸多问题，例如缺乏访问控制，这意味着任何授权用户都可以访问所有数据，而无需考虑权限级别。该系统还缺乏用户活动跟踪和安全软件验证。该系统允许用户在没有适当日志记录的情况下访问敏感信息。

该报告强调了几个安全漏洞，包括托管未经陆军适当安全评估的第三方应用程序，其中一些应用程序包含数百个漏洞。

尽管备忘录提出了强烈的批评，但陆军首席信息官表示，该报告是识别和缓解漏洞过程的一部分。安杜里尔和帕兰提尔尚未置评。

---

## 10. 法罗群岛

**原文标题**: Faroes

**原文链接**: [https://photoblog.nk412.com/Faroe2025/Faroes/n-cPCNFr](https://photoblog.nk412.com/Faroe2025/Faroes/n-cPCNFr)

纳加尔朱纳·库马尔的《法罗群岛》生动地描绘了丹麦境内的自治地区法罗群岛。这些岛屿以其壮丽的景色、恶劣的天气和浓厚的北欧文化为特色。在持续不断的风暴和汹涌的海浪作用下，火山岩被塑造成高耸的玄武岩悬崖，陡峭地坠入大西洋。天气变化莫测，在雾、雨和短暂的阳光之间快速切换。

羊是法罗群岛的标志性特征，其数量超过人类，并在岛屿上自由漫游。“法罗群岛”这个名字本身就源于“羊”和“岛屿”这两个词。岛民通过建造草皮屋顶的房屋来适应环境，以达到隔热和防水的目的。徒步旅行路线通常只是羊道，这种体验原始而狂野，没有护栏或警告标志。

卡尔索伊岛上的卡卢尔灯塔是一个著名的地标，可以通过沿着刀刃般的山脊进行具有挑战性的徒步旅行到达。这些岛屿最近也因作为詹姆斯·邦德电影《无暇赴死》的拍摄地而声名鹊起。作者强调了法罗群岛的崎岖之美和独特个性，使其成为冒险旅行者引人注目的目的地。

---

## 11. 微软首席技术官表示希望用自研芯片替换大部分AMD和英伟达GPU。

**原文标题**: Microsoft CTO says he wants to swap most AMD and Nvidia GPUs for homemade chips

**原文链接**: [https://www.theregister.com/2025/10/02/microsoft_maia_dc/](https://www.theregister.com/2025/10/02/microsoft_maia_dc/)

为优化性能并降低成本，微软首席技术官凯文·斯科特宣布计划将其大部分人工智能数据中心工作负载从AMD和英伟达GPU转移到其自身定制设计的芯片上，首先从其Maia AI加速器开始。虽然目前依赖英伟达以获得最佳性价比，但微软寻求对系统设计有更大的控制权，以优化工作负载。

微软首款内部AI加速器Maia 100于2023年末推出，转移了OpenAI的GPT-3.5工作负载，释放了GPU容量，但其性能不及竞争对手的GPU。据报道，第二代Maia加速器正在开发中，计划明年推出。

尽管微软的目标是让自己的芯片主导其数据中心，但文章表明英伟达和AMD的GPU可能仍然是必需的。其他云提供商，如亚马逊和谷歌，已经部署了他们自己的定制芯片（TPU和Trainium），但他们仍然使用英伟达和AMD的GPU，因为客户对这些芯片的需求持续存在。

除了AI加速器，微软还在开发定制CPU（Cobalt）和安全芯片，以进一步定制其基础设施并保护其数据中心。

---

## 12. 现代字体堆栈

**原文标题**: Modern Font Stacks

**原文链接**: [https://modernfontstacks.com/](https://modernfontstacks.com/)

这是刘易斯·卡罗尔的《爱丽丝梦游仙境》的开篇。爱丽丝和姐姐坐在河边，感到无聊。姐姐正在读一本没有图画或对话的书，爱丽丝认为这本书毫无用处。她正在考虑采摘雏菊是否值得，这时，一只长着粉红色眼睛的白兔跑过去，嘟囔着自己要迟到了，并从背心口袋里掏出一块怀表。

对于爱丽丝来说，这非常不寻常，她从未见过穿着背心或戴着怀表的兔子。出于强烈的好奇心，她跟着兔子跳进了一个兔子洞。这个洞像隧道一样下降，然后突然坠落，导致爱丽丝掉进一口似乎很深的井里。

在漫长的下落过程中，爱丽丝观察到水井的侧面排列着橱柜、书架、地图和图片。她抓住一个空空的“橘子酱”罐子，并设法把它放回架子上。随着无休止的下落继续，爱丽丝开始自言自语，想着她的猫黛娜是否会想念她，并希望她能得到她的牛奶碟。最后，她落在一堆树枝和干树叶上，结束了她的坠落。

---

## 13. OpenAI不过是一家平庸且孤注一掷的AI初创公司

**原文标题**: OpenAI Is Just Another Boring, Desperate AI Startup

**原文链接**: [https://www.wheresyoured.at/sora2-openai/](https://www.wheresyoured.at/sora2-openai/)

本文认为，OpenAI并非其宣扬的那样是一家具有革命性的人工智能巨头，而是一家被炒作和巨额融资所掩盖的战略不集中且绝望的人工智能初创公司。作者认为，OpenAI缺乏连贯的愿景，追逐着太多不同的项目，如社交媒体、生产力软件、招聘门户、广告、云计算、硬件和浏览器，同时严重依赖媒体泄露来抬高其估值。

OpenAI的核心业务ChatGPT被认为是LLM的简单“包装”，其API销售额表现平平，表明其模型在现实世界中的集成有限。作者批评了令人失望的GPT-5升级，并质疑OpenAI昂贵的研发的效用，特别是考虑到LLM固有的局限性，例如幻觉。

作者认为，OpenAI营收增长放缓、产品商品化以及对创新“神话”的依赖，都是一家苦苦挣扎的公司的迹象。它的商业模式主要依赖于ChatGPT订阅，但却消耗了巨额资金。最终，作者认为OpenAI是由一位魅力非凡但最终具有误导性的CEO，Sam Altman领导的剥削性“骗局”，正在绝望地寻找可持续的方式来将生成式AI货币化，而整个行业都在努力实现盈利。结论是，尽管有炒作，OpenAI很可能会错过其收入预测，并消耗比预期更多的资金。

---

## 14. 当内核名称包含“cutlass”时，Fp8的运行速度大约快100 tflops。

**原文标题**: Fp8 runs ~100 tflops faster when the kernel name has "cutlass" in it

**原文链接**: [https://github.com/triton-lang/triton/pull/7298](https://github.com/triton-lang/triton/pull/7298)

此GitHub议题讨论了基于Triton的Attention Kernel的性能改进，特别关注使用FP8数据类型。作者Mogball实现了持久性Attention，提升了短上下文长度下的性能。然而，他们发现了一个奇怪的现象：当内核名称包含子字符串“cutlass”时，FP8性能显著提升（约100 TFLOPS）。

性能基准测试比较了“triton-fp16”和“triton-fp8”在不同上下文长度 (N_CTX) 和嵌入维度 (D) 下的因果和非因果Attention实现。初步结果表明，持久性Attention对fp16的性能产生了负面影响，而“cutlass”命名技巧显著提高了fp8的性能。

审阅者对内核命名依赖性表示惊讶和好奇。通过反汇编 `ptxas` (Nvidia 的 PTX 汇编器) 发现，编译器确实包含硬编码逻辑，以根据内核名称中是否存在“cutlass”来应用特定的优化。

讨论总结道，这种“cutlass”优化很可能是NVIDIA的一个不稳定的实验性功能。如果强制使用（通过修补`ptxas`），则存在稳定性问题。有人建议Nvidia提供一种更正式的方式来启用此优化，例如PTX指令。

---

## 15. CVE-2025-59489：Unity Runtime自2017年起存在任意代码执行漏洞

**原文标题**: CVE-2025-59489: Arbitrary Code Execution in Unity Runtime since 2017

**原文链接**: [https://flatt.tech/research/posts/arbitrary-code-execution-in-unity-runtime/](https://flatt.tech/research/posts/arbitrary-code-execution-in-unity-runtime/)

本文详细介绍了 CVE-2025-59489 漏洞，该漏洞存在于 Unity Runtime 中，影响基于 Unity 2017.1 及更高版本构建的游戏和应用程序。该漏洞允许任意代码执行，原因是 Unity 处理传递给 Unity 应用程序的 intents 和命令行参数的方式存在缺陷。具体而言，恶意 intent 可以控制 `xrsdk-pre-init-library` 参数，使攻击者能够加载任意共享库（.so 文件）并在 Unity 应用程序的上下文中执行恶意代码。

作者概述了两种攻击场景：本地和远程。在本地，同一设备上的任何恶意应用程序都可以利用此漏洞。远程利用需要满足特定条件，包括应用程序导出可浏览的 activity 并将攻击者控制的内容写入其私有存储。虽然 SELinux 限制缓解了大多数远程场景，但本文解释了可能的绕过方法。

Unity 已在 2019.1 及更高版本中解决了此问题，并提供了二进制补丁工具。强烈建议开发人员更新 Unity、重新编译并重新发布其应用程序。文章最后强调了了解依赖项中的安全隐患的重要性，并推广了作者所在公司 GMO Flatt Security 的渗透测试及其 AI 安全工程师 Takumi。

---

## 16. 测量量子性的温度计

**原文标题**: A Thermometer for Measuring Quantumness

**原文链接**: [https://www.quantamagazine.org/a-thermometer-for-measuring-quantumness-20251001/](https://www.quantamagazine.org/a-thermometer-for-measuring-quantumness-20251001/)

本文探讨了“反常热流”这一引人入胜的概念，即由于量子力学，热量从冷物体流向热物体，看似违反了热力学第二定律。文章重点介绍了Alexssandre de Oliveira Jr.及其同事的研究，他们提出使用这种反常热流作为“温度计”来检测叠加态和纠缠等量子现象，且不会破坏它们。

文章解释了热力学与信息之间的联系，提到了麦克斯韦妖和兰道尔原理，该原理表明擦除信息需要能量。量子力学引入了复杂性，因为信息可以以经典物理学无法实现的方式进行处理。纠缠，即量子物体具有相互依赖的状态，可以实现更高效的操纵，正如Brukner、Vedral和Partovi的研究所示。

关键创新在于使用“量子存储器”（类似于麦克斯韦妖的系统）来调节量子系统和散热器之间的热流。量子存储器与两者纠缠，催化热传递，将量子系统中的纠缠转化为散热器中的额外热量。测量散热器的能量可以揭示纠缠的存在，而无需直接测量（从而破坏）量子系统。

这种方法提供了一种简单通用的方法来验证量子设备的量子性，例如量子计算机，并有可能探测引力的量子方面。虽然需要精确控制且无法检测所有纠缠态，但它为量子诊断提供了一条有希望的途径。

---

## 17. 赞美RSS和可控的信息流

**原文标题**: In Praise of RSS and Controlled Feeds of Information

**原文链接**: [https://blog.burkert.me/posts/in_praise_of_syndication/](https://blog.burkert.me/posts/in_praise_of_syndication/)

本文提倡使用RSS（简易信息聚合）作为比算法推荐更优越的在线内容获取方式。作者认为，社交媒体平台优先考虑用户参与度和广告收入，而非提供平衡和可控的信息，导致了“糟糕”的媒体饮食。相比之下，RSS允许用户完全控制信息来源，并按照时间倒序显示其选择的网站的更新。

作者分享了自己对使用Facebook关注乐队感到失望的个人经历，突出了该平台的诱导互动和付费推广模式。他们详细介绍了自己的RSS之旅，目前在手机上使用FeedMe应用程序，并强调了预先选择内容、阅读较长文章以及对兴趣进行分类的好处。RSS阅读器提供一致、无干扰的阅读体验，避免了许多网站上的视觉混乱和参与陷阱。

本文提供了开始使用RSS的实用技巧，包括在网站上寻找RSS图标、使用Muspy等工具跟踪新音乐发行，以及从The Old Reader或Feedly等用户友好的聚合器开始。它还建议创建类别、利用离线阅读功能、探索用于特定内容过滤的高级RSS API（例如在arXiv上）以及定期清理订阅。最后，它推荐了一些资源，用于查找流行的RSS源，以开始构建个性化的信息生态系统。

---

## 18. Glide，一款可扩展、以键盘操作为主的网页浏览器

**原文标题**: Glide, an extensible, keyboard-focused web browser

**原文链接**: [https://blog.craigie.dev/introducing-glide/](https://blog.craigie.dev/introducing-glide/)

Glide：一款基于键盘操作、高度可定制的浏览器

---

## 19. 被困在苏联核掩体中的蚂蚁存活多年

**原文标题**: Ants Trapped in a Soviet Nuclear Bunker Survived for Years

**原文链接**: [https://www.sciencealert.com/ants-trapped-in-an-old-soviet-nuclear-bunker-survived-for-years-by-turning-on-their-own](https://www.sciencealert.com/ants-trapped-in-an-old-soviet-nuclear-bunker-survived-for-years-by-turning-on-their-own)

在波兰一处废弃的苏联核掩体中，研究人员发现了一个大型的林蚁（Formica polyctena）群落，它们被困在完全黑暗的环境中，没有蚁后或典型资源，却奇迹般地生存了下来。这个群落数量高达一百万只活工蚁和数百万只死蚁，并没有繁殖。相反，它们的种群是通过从上方更大的蚁群中掉下来的蚂蚁来维持的，这些蚂蚁是通过连接掩体和森林的锈蚀通风管道掉进来的。

最初，研究人员对蚂蚁在缺乏光、热和食物的情况下还能生存感到困惑，后来确定这些蚂蚁在同类相食，啃食死去的同伴。对掩体内的“墓地”中发现的尸体进行检查后显示，大约93%的尸体有咬痕和啮咬的洞，表明存在大规模的同类相食现象。

研究人员得出结论，来自上方巢穴的源源不断的新工蚁和对同伴尸体的消费提供了取之不尽的食物来源，使得这个掩体群落能够在极其不利的条件下生存下来。蚂蚁的韧性凸显了它们非凡的适应和忍受逆境的能力。

2016年，研究人员安装了一个木制栈道，将通风管道连接到掩体地面，为被困的蚂蚁提供了一条逃生路线。几个月内，这些蚂蚁就离开了掩体地面，结束了它们对同类相食的依赖。现在，任何掉进掩体的蚂蚁都可以轻松地走回上方的蚁群。

---

## 20. 低剂量辐射缓解膝骨关节炎患者的症状

**原文标题**: Low-dose radiation offers relief to people with knee osteoarthritis

**原文链接**: [https://www.astro.org/news-and-publications/news-and-media-center/news-releases/2025/low-dose-radiation-therapy-offers-substantial-relief-to-people-with-painful-knee-osteoarthritis](https://www.astro.org/news-and-publications/news-and-media-center/news-releases/2025/low-dose-radiation-therapy-offers-substantial-relief-to-people-with-painful-knee-osteoarthritis)

**摘要：**

根据美国放射肿瘤学会（ASTRO）年会上发布的研究，低剂量放射治疗（LDRT）可为膝骨关节炎（OA）患者提供显著的疼痛缓解和功能改善。这项研究是对多项临床试验的荟萃分析，表明LDRT是一种安全有效的膝骨关节炎非侵入性治疗选择，其益处与其他传统疗法相当，且没有与手术或强效止痛药相关的风险。

研究发现，与安慰剂或假治疗相比，LDRT显著降低了膝骨关节炎患者的疼痛评分并改善了关节功能。观察到积极作用在治疗后持续存在一段时间。虽然确切的作用机制仍在研究中，但研究人员认为LDRT可减少关节炎症，从而缓解疼痛并改善活动能力。

研究作者强调，对于那些未从其他保守治疗中获得充分缓解或不适合手术的患者，LDRT可能提供一种有价值的替代方案。结果突显了LDRT作为一种有前景的治疗选择，可用于控制膝骨关节炎的衰弱症状。目前正在进行进一步的研究，以优化治疗方案并确定最能从这种方法中受益的患者。

---

## 21. 啤酒罐 (2023)

**原文标题**: The Beer Can (2023)

**原文链接**: [https://brr.fyi/posts/beer-can](https://brr.fyi/posts/beer-can)

本文赞颂南极站的“啤酒罐”，它是连接地上生活区与地下工业区的重要基础设施。作者着重强调了这两个区域之间的鲜明对比：现代化、舒适的地上站与实用主义的、埋藏在厚厚冰雪之下的老旧“拱顶”。

于2008年启用的地上站，容纳了所有生活设施，如住宿、餐饮和娱乐。相比之下，拱顶则包含重要的工业基础设施，包括发电、水过滤、仓储和重型设备维护。

“啤酒罐”是一个50英尺长的波纹金属圆柱体和楼梯间，连接了这两个区域的高度差，这是由于南极站逐渐被不断积聚的冰雪掩埋造成的。它设有冷藏门，用于隔离加热的生活区与未加热的“啤酒罐”和拱顶。它包含90级台阶以及一个货运电梯，对于运输物资和废物至关重要。

作者强调了穿越“啤酒罐”楼梯的身体挑战，尤其是在高海拔地区。这导致了“做啤酒罐”这种作为一种锻炼方式的奇特传统。

最终，“啤酒罐”不仅仅被视为一个楼梯间，更被视为一个概念边界，分隔了舒适的生活和维持南极站正常运转的必要工作。

---

## 22. 金牛座共振群中的小型近地天体

**原文标题**: Small Near-Earth Objects in the Taurid Resonant Swarm

**原文链接**: [https://arxiv.org/abs/2509.22602](https://arxiv.org/abs/2509.22602)

题为“金牛座共振群中的小型近地天体”的论文研究了金牛座共振群（TRS）内的小行星级天体群，该区域是与金牛座复合体相关的动态聚集的碎片区域。由叶泉志领导的作者分析了2022年TRS遭遇期间来自兹维基瞬变设施（ZTF）活动的数据。

该研究旨在确定TRS中已知存在的亚米级粒子丰度是否也适用于更大的天体。他们的研究结果表明，TRS内可能存在约100个通古斯卡大小的天体和1000个车里雅宾斯克大小的天体。这种对车里雅宾斯克大小天体的估计与之前从火流星记录中得出的结果一致。基于这些数字，作者估计撞击频率低于每400万年一次。

然而，作者强调，这些结果是基于TRS中小行星的轨道分布与较小的火球大小的流星体相似的假设，这一假设尚未得到证实。该论文提出，未来的广域观测设施，如维拉·C·鲁宾天文台，可以通过在2020年代和2030年代观测TRS的近距离接近来验证这些发现，从而更好地约束星群中小行星级天体的大小分布，从而发挥关键作用。该论文已被《宇航学报》接受发表，作为PDC 2025特刊的一部分。

---

## 23. 我花了一天教老年人如何使用iPhone。

**原文标题**: I spent the day teaching seniors how to use an iPhone

**原文链接**: [https://forums.macrumors.com/threads/i-spent-the-day-trying-to-teach-seniors-how-to-use-an-iphone-and-it-was-a-nightmare.2468117/](https://forums.macrumors.com/threads/i-spent-the-day-trying-to-teach-seniors-how-to-use-an-iphone-and-it-was-a-nightmare.2468117/)

作者scaramoosh讲述了他们教老年人使用iPhone的沮丧经历。他们认为，尽管有辅助功能，但iPhone对老年人来说过于复杂，苹果需要简化用户体验。最初的设置过程是一个重大障碍，老年人在创建账户、理解密码（即使是熟悉的生日）以及使用Touch ID或Face ID方面都感到困难。

作者指出，应用程序过多、电话应用缺少默认键盘以及触摸屏的敏感性是造成困惑的原因。由于难以稳定握住手机，老年人很容易发生误操作。虽然辅助访问有所帮助，但作者认为这应该是65岁以上用户的标准设置选项。他们认为密码和大量信息对这个群体来说是不必要的。

作者还指出了“假”Touch ID按钮和Face ID手机上的滑动手势的问题，因为缺乏触觉反馈使它们难以使用。最终，培训失败了，因为老年人甚至无法掌握iPhone的基本解锁功能。根本问题是他们以前的诺基亚手机上的口袋拨号999（紧急服务）。作者的结论是，简单的翻盖手机，开盖接听/关盖结束通话，是更好的解决方案，尽管很难找到没有不必要功能的。文章最后呼吁苹果改进辅助功能，并减少其手机对老年人的繁琐操作。

---

## 24. Radicle：基于Git的P2P协作 (2024)

**原文标题**: Radicle: Peer-to-Peer Collaboration with Git (2024)

**原文链接**: [https://lwn.net/Articles/966869/](https://lwn.net/Articles/966869/)

这篇 LWN.net 文章介绍了 Radicle，一个构建在 Git 上的点对点协作平台，它为像 GitHub 和 GitLab 这样的中心化代码托管平台提供了一种去中心化的替代方案。Radicle 旨在解决中心化系统相关的单点故障和潜在审查问题。

Radicle 的工作方式是让每个用户运行一个节点，该节点存储仓库的副本并与其他节点同步更改。它直接在 Git 仓库中增加了对议题（issues）和拉取请求（“补丁”）的支持。虽然它可能看起来类似于主流的代码托管平台，但主要区别在于所有用户都能够使用命令行界面和 Web 用户界面克隆项目。

主要特性包括自签名仓库，确保无论存储位置如何都能保证真实性，以及用于无冲突合并议题和补丁数据的“协作对象”（COB）机制。该平台利用 gossip 协议进行节点和仓库发现，并利用 Git v2 智能传输协议进行内容交换。Radicle 通过公开可访问的种子节点解决了 NAT 问题。

虽然仍在开发中，但 Radicle 面临着诸如成熟的 CI/CD 支持、更通用的身份系统、代码审查功能以及使不熟悉 Radicle 的用户更容易报告问题等挑战。它还需要一个可靠的代码审核系统，以防止恶意代码被推送和拉取到 git 仓库等问题。

文章总结说，Radicle 呈现了一个有前景的去中心化 Git 托管解决方案。

---

## 25. Kairos：边缘 K8s 的不可变发行版

**原文标题**: Kairos: Immutable Distro for K8s at the Edge

**原文链接**: [https://kairos.io/](https://kairos.io/)

Kairos：专为边缘 Kubernetes 打造的不可变 Linux 发行版。它允许用户通过选择所需的操作系统和 Kubernetes 发行版，构建用于边缘设备的可定制可引导操作系统镜像，这些都以可定制的容器镜像形式提供。主要优势包括：通过不可变镜像实现集群间的一致性，通过减少攻击面和数据加密来增强安全性，以及简化安装方法。

Kairos 针对 Kubernetes 工作负载进行了优化，支持通过 Kubernetes 进行升级，并使用 cloud-init 进行配置管理。它是一个云原生计算基金会沙箱项目。

该发行版提供 X86 和 RPi4 版本，可作为 Docker 镜像下载。DeEEP Network 等公司正在使用它来构建具有可信启动的安全系统。Spectro Cloud 通过其 Palette 平台为 Kairos 提供企业级 Kubernetes 管理。

本文鼓励通过 GitHub 和 LinkedIn 进行社区参与，并邀请采用者与他们联系。同时提供了安装指南、架构细节和使用示例的链接。

---

## 26. 信号协议与后量子棘轮

**原文标题**: Signal Protocol and Post-Quantum Ratchets

**原文链接**: [https://signal.org/blog/spqr/](https://signal.org/blog/spqr/)

本文探讨了通过引入稀疏后量子棘轮（SPQR）将后量子密码学集成到Signal协议中的方法，从而增强其抵抗未来量子计算威胁的能力，同时保持前向安全性（FS）和后泄露安全性（PCS）。

目前的Signal协议使用哈希函数（量子安全）来实现FS，并使用椭圆曲线Diffie-Hellman（ECDH）（非量子安全）来实现PCS。 SPQR增加了一个定期推进的后量子棘轮，该棘轮与Signal现有的双棘轮混合，形成一个“三棘轮”。

其核心思想是持续生成并混合来自量子安全密钥封装机制（KEM）的密钥。 KEM的简单实现方式，即每次消息都发送大量的封装密钥（EK）和密文（CT），效率低下。 本文探讨了解决这些问题的方法，重点关注状态机和节省带宽的策略。

为了缓解数据量大的问题，本文提出以块的形式发送EK和CT，并使用纠删码。 即使丢失了一些块，纠删码也允许重建原始消息（EK或CT），从而减轻消息丢失或恶意中间人攻击丢弃特定块的影响。本文还提到了对消息容量的有效利用，并指出当Alice发送EK块时，Bob没有数据要发送，因此该容量未被使用，应该更频繁地使用以加速协议。

---

## 27. 字母表中最怪异的字母：约赫字母的兴衰

**原文标题**: The strangest letter of the alphabet: The rise and fall of yogh

**原文链接**: [https://www.deadlanguagesociety.com/p/history-of-letter-yogh](https://www.deadlanguagesociety.com/p/history-of-letter-yogh)

科林·戈里的文章探讨了鲜为人知的中世纪字母“约赫”(ȝ)的历史及其对英语拼写复杂性的影响。文章首先概述了英语拼写的令人困惑之处，包括无声字母和多种发音。

文章追溯了字母“g”从古英语的岛屿体“ᵹ”到用于拉丁语的卡洛林体“g”的演变。诺曼入侵使情况更加复杂，因为诺曼抄写员引入了新的书写传统。这导致了源自岛屿体“ᵹ”的约赫 (ȝ) 重新出现，成为中古英语中一个独特的字母。

约赫用于表示两个声音： "y" 音和 "gh" 音（如 "loch" 中）。这种双重性反映了字母 "c" 和 "g" 已经存在的矛盾之处，由于颚化现象（一种后部发音前移的语音变化），它们也有双重发音。

文章解释说，“gh” 音起源于原始日耳曼语中的一个声音，在古英语中用“ᵹ”表示。诺曼抄写员随后采用约赫来表示法语中不存在的“y”和“gh”音。尽管约赫很有用，但由于替代拼写方式的出现以及印刷术带来的标准化，约赫最终从英语中消失了，因为印刷术更喜欢容易获得的字体。然而，约赫在苏格兰持续的时间更长，通常用 "z" 表示，因为两者在视觉上相似，这导致了 Menzies 和 Mackenzie 等名字的发音变化。作者表明，虽然约赫造成了一些混乱，但约赫的历史揭示了对英语书写演变的宝贵见解。

---

## 28. FyneDesk: 用 Go 编写的 Linux 完整桌面环境

**原文标题**: FyneDesk: A full desktop environment for Linux written in Go

**原文链接**: [https://github.com/FyshOS/fynedesk](https://github.com/FyshOS/fynedesk)

FyneDesk 是一个使用 Fyne 工具包和 Go 编程语言构建的 Linux/Unix 桌面环境，旨在实现易用性和易开发性，并遵循 Material Design 原则。它依赖 arandr、xbacklight/brightnessctl、connman-gtk 和 compton 等外部工具来实现完整的桌面体验，尽管没有它们也可以运行，但体验会降低。

安装涉及使用 `go get` 安装 `fynedesk` 命令。要将其设置为可选择的桌面选项，需要从 GitHub 克隆项目，并执行 `make` 命令将其安装在登录管理器中。如果安装了 Xephyr，可以使用 `make embed` 命令在嵌入式 X 窗口中测试窗口管理器组件。

提供了 `fynedesk_runner` 实用程序来增强韧性，在 alpha/beta 测试期间自动从崩溃中恢复。可以通过 `go get` 安装它。

设计理念和壁纸由 Jost Grant 贡献。对于发布 FyneDesk 的发行版，建议捆绑 “fin” 显示管理器应用程序。如果开发者为他们的系统打包了 FyneDesk，欢迎通知项目。

---

## 29. Amazon Vega OS 和 Vega 开发者工具

**原文标题**: Amazon Vega OS and Vega Developer Tools

**原文链接**: [https://developer.amazon.com/apps-and-games/vega](https://developer.amazon.com/apps-and-games/vega)

此Amazon应用商店开发者门户页面介绍Vega OS和Vega开发者工具，着重于帮助开发者创建优质的电视体验。Vega OS专为下一代Fire TV Stick设计，并利用React Native进行开发。

要点包括：

*   **Vega OS和工具介绍：** 旨在利用熟悉的工具和框架创建电视体验。
*   **Vega开发者工具：** 这些工具提供在Vega OS上开发、测试和分发应用程序的资源，包括CLI、模拟器和VS Code扩展，以及用于导航、焦点和状态管理的Vega库和API。
*   **利用现有技能：** 鼓励React Native和Web开发者使用其现有技能为Vega OS构建应用。
*   **Fire TV集成：** 提供关于Fire TV设计原则、硬件特定元素和服务集成的信息。
*   **测试与调试：** 提供使用Vega Studio进行调试以及在模拟器或物理设备上进行整个开发周期测试的工具，包括Live App Testing。
*   **应用分发：** 指导开发者完成准备和提交应用程序以进行分发的过程，重点介绍要求、步骤和最佳实践。
*   **社区资源：** 提供对参考应用程序、示例、发行说明和开发者新闻通讯的访问。
*   **其他资源：** 链接到Fire平板电脑和电视设备规格、变现工具、开发者控制台和各种开发者支持渠道。

---

## 30. 使用AI辅助工具发现的curl潜在问题

**原文标题**: Potential issues in curl found using AI assisted tools

**原文链接**: [https://mastodon.social/@bagder/115241241075258997](https://mastodon.social/@bagder/115241241075258997)

丹尼尔·斯滕贝格可能发布了一篇社交媒体帖子，称约书亚·罗杰斯发送了一份“大量”的关于curl潜在问题的列表。这是一个简短的公告，表明curl这个广泛使用的命令行URL数据传输工具可能存在一些新发现的漏洞或错误。该帖子没有具体说明这些问题的性质或严重程度，仅说明已报告了大量问题。末尾的Mastodon消息提供的上下文表明用户正在Mastodon网站上查看内容，需要启用JavaScript，或者应该考虑使用专门的Mastodon应用程序。这与curl公告本身无关。总之，核心信息是一个初步通知，表明curl内部已发现大量潜在问题，需要进一步调查和潜在修复。

---

## 31. 肯塔基州离婚率骤降，父亲平分监护权是重要原因。

**原文标题**: Divorce Plunged in Kentucky. Equal Custody for Fathers Is a Big Reason Why

**原文链接**: [https://www.wsj.com/us-news/law/the-equal-custody-experiment-41e1f7a6](https://www.wsj.com/us-news/law/the-equal-custody-experiment-41e1f7a6)

以下是《华尔街日报》文章“肯塔基州离婚率骤降，父亲平等监护权是重要原因”的摘要：

文章探讨了肯塔基州在2018年实施一项法律后离婚率显著下降的情况，该法律规定在涉及子女的离婚案件中，共同（平等）育儿时间是默认安排。文章认为，这一变化是离婚率下降的主要驱动因素。

主要论点是，转向平等监护权通过使离婚过程对父母双方的吸引力降低、经济负担加重，从而抑制了离婚。潜在的离婚者知道他们很可能需要分享监护权和育儿时间，因此在寻求分居时更加犹豫，尤其是在孩子年幼时。这是因为该法律增加了划分时间和资源相关的干扰和成本。

文章强调了来自肯塔基州律师和家庭法院专业人士的轶事证据，表明该法律导致人们更加深思熟虑地考虑离婚的后果。一些律师报告说，他们看到的轻率离婚案件减少了。

虽然支持者认为该法律加强了父亲的作用，并确保儿童能从父母双方受益，但一些批评者担心，如果平等监护权不符合儿童的最佳利益，尤其是在涉及家庭暴力或忽视的案件中，该法律可能会迫使儿童进入不舒服甚至不安全的境地。文章承认，该法律的全部长期影响仍有待观察，但表明它代表了肯塔基州看待和处理离婚方式的重大变化。

---

## 32. 一致性哈希

**原文标题**: Consistent hashing

**原文链接**: [https://eli.thegreenplace.net/2025/consistent-hashing/](https://eli.thegreenplace.net/2025/consistent-hashing/)

本文介绍了 Consistent Hashing（一致性哈希），一种旨在最小化哈希表大小调整影响的算法。它解决了朴素哈希的问题，即在分布式系统（如缓存 Web 代理）中添加或删除节点会导致键的完全重新洗牌，从而导致大范围的缓存未命中和性能下降，尤其是在高峰负载期间。

Consistent Hashing 通过将节点和项目都映射到单位圆上来解决这个问题。一个项目被分配给顺时针方向上最近的节点。当添加或删除节点时，只有会被分配给该节点的项目才会被重新映射，从而显著减少整体中断。这就是“单调性属性”。

本文详细介绍了使用排序数组中的二分查找来查找负责节点的实现方法。一个关键的实际考虑是“量化”单位圆到一个离散范围 [0, ringSize) 以避免冲突。

文章进一步讨论了即使使用良好的哈希函数，项目在节点间分布不均的问题。为了缓解这个问题，文章提出了“虚拟节点”的概念，即每个节点被映射到圆上的多个位置。这通过平均节点之间的距离来改善分布。

附录深入探讨了项目分布背后的数学原理以及虚拟节点对减少分配给每个节点的项目数量的方差的影响。本文包含一个指向 GitHub 存储库的链接，该存储库包含 Consistent Hashing 的 Go 代码实现，包括带虚拟节点和不带虚拟节点的版本。

---

## 33. Playball – 在终端观看MLB比赛

**原文标题**: Playball – Watch MLB games from a terminal

**原文链接**: [https://github.com/paaatrick/playball](https://github.com/paaatrick/playball)

Playball 是一款命令行工具，用户可以通过终端直接观看 MLB 比赛，为 MLB Gameday 和 MLB.tv 提供了一种低调的替代方案。它可以使用 npm 全局安装 (`npm install -g playball`)，也可以通过 Docker 运行。该工具提供多种视图：赛程视图、积分榜视图和实际比赛视图，可以使用键盘快捷键进行导航。

赛程视图允许浏览比赛和跳转到特定日期，而比赛视图则显示逐场比赛信息。Playball 可以使用 `playball config` 子命令进行高度配置。用户可以自定义各种游戏元素的颜色，例如好球、坏球、出局和垒上跑者。他们还可以设置自己喜欢的球队，以便在赛程和积分榜视图中突出显示。

配置选项包括 `color.ball`、`color.strike`、`color.out`、`color.on-base` 和 `favorites` 等设置。颜色可以使用标准颜色名称（red、green、blue）、前缀变体（bright-green）、十六进制代码（#FFA500）或“default”来指定。收藏夹设置为逗号分隔的球队缩写。配置值可以检索、更改或恢复为默认值。该项目是开源的，欢迎贡献。

---

## 34. 琥珀屋

**原文标题**: Amber Room

**原文链接**: [https://en.wikipedia.org/wiki/Amber_Room](https://en.wikipedia.org/wiki/Amber_Room)

琥珀屋，一个装饰着琥珀板、金箔和镜子的房间，最初于18世纪初在普鲁士创作。它最初是为夏洛滕堡宫设计的，后来被赠送给俄罗斯的彼得大帝，并安装在圣彼得堡附近的凯瑟琳宫。它被誉为“世界第八大奇迹”。

二战期间，琥珀屋被纳粹德国掠夺并运往柯尼斯堡，在那里展出。随着盟军逼近，这个房间被拆卸并装箱。然而，柯尼斯堡在1944年遭到猛烈轰炸，琥珀屋的下落和命运成了一个谜。苏联官方报告称，该房间在1945年4月9日至11日的轰炸中被摧毁。

尽管人们进行了无数次的搜索，并提出了关于它幸存和下落的理论，但没有找到它继续存在的确凿证据。有些人认为它在柯尼斯堡的轰炸中被摧毁，而另一些人则推测它被藏在其他地方。

1979年，在凯瑟琳宫启动了一个重建琥珀屋的项目。经过俄罗斯和德国工匠数十年的努力，并在大量捐款的支持下，复制品于2003年竣工并落成。

---

## 35. 标准库：技术领导力的框架、模板和指南库

**原文标题**: Stdlib: A library of frameworks, templates, and guides for technical leadership

**原文链接**: [https://debuggingleadership.com/stdlib](https://debuggingleadership.com/stdlib)

Stdlib是一个社区构建的库，提供超过1000种资源——框架、模板、指南、文章和视频——旨在提升技术领导力技能。它涵盖了与工程管理和技术领导力相关的广泛主题。

最近新增和精选的内容侧重于当前的挑战和趋势：注释驱动开发、干扰对工程师的影响、处理不道德的请求、快速流动的团队拓扑、事件响应中的委派、管理冲刺中的计划外工作，以及对过程的过度强调。

该平台还涉及关键的领导力能力：科技高管的商业思维、人工智能对初级开发人员职业道路的影响、衡量团队绩效、培养承认错误的文化、认可个人工程师的贡献、参与组织政治、避免过度工程设计，以及软件维护的重要性。

Stdlib重点介绍了多本书籍，包括《原子习惯》、《凤凰项目》、《团队拓扑》、《代码整洁之道》和《加速》，涵盖了个人效率、DevOps、团队组织、代码质量和高性能技术组织等领域。

最后，它提供了关于以下主题的见解：创业公司中的隐私、裁员后支持团队、领导力中的故事讲述、工程生产力的可衡量性、澄清领导者的思维、产品战略、管理困难的团队成员、工程赋能、事件升级、压力管理和战略思维。来自Dropbox的职业框架和关于《人件》的资源也丰富了这个库。

---

## 36. Babel 是我坚持使用 Emacs 写作的原因。

**原文标题**: Babel is why I keep blogging with Emacs

**原文链接**: [https://entropicthoughts.com/why-stick-to-emacs-blog](https://entropicthoughts.com/why-stick-to-emacs-blog)

作者描述了他们在使用Org mode和Emacs进行博客写作时的矛盾心理。虽然他们承认创建更简单、自定义的静态站点生成器（可能大约2000行代码）的诱惑力，但他们仍然主要因为Babel功能而依赖于Org mode。

作者承认没有完全理解Org的发布流程，觉得其底层代码（超过2万行）复杂且令人畏惧。尽管如此，Babel在Org文档中执行代码块并显示结果（包括表格和图像）的强大功能实在太有价值，无法放弃。

Babel支持会话、注入变量以及提供特定于语言的代码执行和样式的能力被强调为一个显著优势。作者特别提到使用它与R语言结合，直接在博客文章中生成绘图。这种数据、可视化和文本的紧密集成使得起草过程连贯且高效。

最终，虽然自定义博客引擎可能看起来很吸引人，但复制Babel的功能需要大量的时间投入，使其成为一个不切实际的项目。因此，作者最终还是选择使用更复杂但功能强大的Org mode和Babel来满足其博客需求，尽管偶尔会对它的复杂性感到沮丧。他们认为集成代码执行的优势超过了复杂性的成本。

---

## 37. 英格兰如何失去了它的第一位国王

**原文标题**: How England misplaced its first king

**原文链接**: [https://www.bbc.com/future/article/20250926-why-england-forgot-its-first-king](https://www.bbc.com/future/article/20250926-why-england-forgot-its-first-king)

本文认为，英格兰首位国王埃塞尔斯坦尽管成就斐然，但在历史上却被不公正地忽视了。他于公元925年加冕，统一了分裂的王国，建立了英格兰，与欧洲大陆建立了牢固的关系，并建立了一个多元化、面向外部的社会。他甚至开创了英国君主佩戴王冠的先河。

埃塞尔斯坦在祖父阿尔弗雷德大帝和父亲爱德华长者奠定的基础上，通过征服诺森布里亚，巩固了一个统一的英格兰王国。他在布鲁南堡战役中的胜利进一步巩固了他的统治。本文挑战了“盎格鲁-撒克逊”英格兰同质化的概念，强调了埃塞尔斯坦统治时期的文化多样性和国际联系。

尽管取得了成就，但埃塞尔斯坦后来被阿尔弗雷德大帝的光芒所掩盖，后者拥有更容易获得的史料，并在有生之年就有了强大的传记。然而，近年来，历史学家已经开始拼凑他的生平和遗产。

虽然埃塞尔斯坦的王国在他于公元939年去世后分裂，但统一英格兰的概念仍然存在。他的统治也见证了更有效的政府实践的建立，至今仍有文凭、令状和协议的证据留存。文章最后强调了埃塞尔斯坦作为王权先驱的重要性，并指出查理三世国王在2023年使用的一些加冕仪式源于1100年前埃塞尔斯坦的加冕典礼。

---

## 38. 我为什么选择Lua来写博客

**原文标题**: Why I chose Lua for this blog

**原文链接**: [https://andregarzia.com/2025/03/why-i-choose-lua-for-this-blog.html](https://andregarzia.com/2025/03/why-i-choose-lua-for-this-blog.html)

这篇博文解释了作者决定使用Lua来搭建个人博客的原因，取代了之前基于Racket的方案。 主要动机是降低复杂性，并确保长期可维护性。 作者批评了JavaScript生态系统快速变化的节奏，这经常导致依赖问题和代码迅速过时。 他们强调Lua的稳定性和缓慢演进是其显著优势。

Lua的简洁、小巧和极少的依赖项使作者能够完全理解和管理整个博客系统。 这种方法与现代JavaScript框架中常见的令人头晕目眩的依赖树形成对比。 作者赞赏Lua的“不含电池”理念，该理念鼓励构建针对特定需求的定制解决方案。 他们描述了使用CGI脚本和SQLite数据库来动态地提供博客，强调了一种简单、老派的方法。

作者承认Node.js可能在资源使用方面更有效率，但优先考虑易于维护和长期可行性，而不是单纯的性能。 他们享受自己实现诸如CGI、Micropub、IndieAuth和WebMentions等功能，从而更深入地了解底层技术。 最终，选择Lua是为了掌控、简洁以及能够长期维护博客，而无需不断追逐最新的趋势。 他们提倡“选择无聊”，即选择稳定性和可维护性，从而可以将精力集中在内容创作上，而不是与不断发展的技术栈作斗争。

---

## 39. 微型计算机：迈向大众市场的第二次浪潮

**原文标题**: Microcomputers – The Second Wave: Toward a Mass Market

**原文链接**: [https://technicshistory.com/2025/10/03/microcomputers-the-second-wave-towards-a-mass-market/](https://technicshistory.com/2025/10/03/microcomputers-the-second-wave-towards-a-mass-market/)

本文记录了 20 世纪 70 年代末微型计算机的崛起，重点关注由 Apple II、Commodore PET 和 Tandy/Radio Shack TRS-80 引领的“第二波浪潮”，它们被统称为“三巨头”。 这些机器通过提供面向更广泛消费市场的用户友好型“家电”计算机，打破了该行业的业余爱好者根基。

这一“第二波浪潮”的成功需要技术专长、商业头脑和资本投资，以及承担风险的意愿。 老牌大型机和小型计算机公司最初将微型计算机视为玩具，甚至一些业余爱好者也怀疑大众市场的潜力。

本文重点介绍了苹果公司独特的地位，这源于其在业余爱好者社区的深厚根基。 它详细介绍了联合创始人史蒂夫·沃兹尼亚克和史蒂夫·乔布斯的背景。 沃兹尼亚克是一位电子天才，他出于个人兴趣而非市场需求，设计了 Apple I 和 II 计算机。 乔布斯缺乏沃兹尼亚克的技术专长，但拥有创业愿景，推动了商业化。

本文讲述了 Apple I 的创建、其有限的成功，以及随后 Apple II 及其彩色图形功能的开发。 面对资金挑战，乔布斯获得了经验丰富的商业人士迈克·马库拉的投资，马库拉提供了关键的资金、商业计划和对家用计算潜力的信心。 马库拉的参与，加上沃兹尼亚克的工程技术和乔布斯的远见卓识，最终使苹果公司走向成功，尽管 Apple II 最初的销售额增长缓慢。

---

## 40. 最高桥梁揭幕，离地超2000英尺

**原文标题**: Highest bridge unveiled at more than 2,000ft above ground

**原文链接**: [https://www.independent.co.uk/tv/news/china-worlds-highest-bridge-video-b2835886.html](https://www.independent.co.uk/tv/news/china-worlds-highest-bridge-video-b2835886.html)

世界最高桥梁花江峡谷大桥在中国贵州省正式开通。该桥高出地面2000多英尺，长2890米，将峡谷两岸的通行时间从两小时缩短至仅两分钟。大桥耗时三年多建造完成。

在开通之前，工程师进行了严格的测试，部署了96辆卡车在桥上模拟重交通状况。外交部分享的无人机镜头展示了大桥，包括一个“壮观的水幕测试”，在桥下形成一道彩虹。

---

## 41. 有些狗可以通过功能对玩具进行分类。

**原文标题**: Some dogs can classify their toys by function

**原文链接**: [https://arstechnica.com/science/2025/09/some-dogs-can-classify-their-toys-by-function/](https://arstechnica.com/science/2025/09/some-dogs-can-classify-their-toys-by-function/)

本文讨论了发表在《当代生物学》上的一项新研究，该研究揭示了某些狗拥有一种被称为“标签扩展”的复杂认知能力，使其能够根据功能（拉扯或取回）对玩具进行分类，而无需考虑外观，也无需正式训练。

匈牙利布达佩斯罗兰大学的研究人员研究了已经因记忆玩具名称而闻名的“天赋词汇学习者”(GWL)犬。他们发现，这些狗可以将“拉扯”和“取回”的标签从特定玩具推广到玩具在玩耍过程中的功能。这些狗通过涉及拉扯或取回的玩耍环节被介绍给新的、未标记的玩具。当被要求从新的玩具集中选择一个“拉扯”或“取回”的玩具时，这些狗的选择正确率显著高于偶然性。

这表明这些狗根据功能对物体进行分类，类似于儿童理解不同类型的杯子都是“杯子”，尽管它们的外观各不相同。这种能力通常需要在圈养动物中进行大量的训练，但这些狗通过与主人玩耍自然地发展了这种能力。这项研究建立在该小组之前的研究基础上，之前的研究探索了狗如何感知手势，如何使用感官特征来识别玩具，以及如何通过结合视觉和嗅觉来形成物体的“多层心理图像”。该研究结果表明，人们对与语言相关的技能如何在狗和可能其他动物中发挥作用有了更广泛的理解。

---

## 42. 我是如何屏蔽掉你所有 2600 万个 curl 请求的

**原文标题**: How I block all 26M of your curl requests

**原文链接**: [https://foxmoss.com/blog/packet-filtering/](https://foxmoss.com/blog/packet-filtering/)

本文详细介绍了作者探索使用 XDP (Express Data Path) 和 eBPF (Extended Berkeley Packet Filter) 拦截网络请求，特别是来自 `curl` 的请求。作者旨在高效处理网络请求，在消费级硬件上每秒丢弃高达 2600 万个数据包。

核心思想围绕使用名为 FST1 的 JA4 指纹识别的修改版本来识别 TLS 连接。 FST1 利用 TLS 握手期间交换的密码套件来识别客户端。为了避免在 eBPF 有限的栈空间内实现 SHA256 哈希的复杂性，作者对排序后的密码套件列表使用了更简单的 Jenkins 哈希算法。原因是加密哈希的安全性不是必需的，因为攻击者可以简单地模仿合法的浏览器签名。

eBPF 过滤器解析 Ethernet 和 TCP 头部，从 TLS Client Hello 中提取密码套件，计算 FST1 哈希，并将其与存储在 eBPF 映射中的阻止哈希列表进行比较。eBPF 映射允许用户空间（管理阻止列表的地方）和内核（进行过滤的地方）之间的通信。匹配阻止哈希的请求将被丢弃。

作者承认阻止所有 `curl` 请求有些过度，但强调了该方法在检测欺骗用户代理的机器人方面的潜力。虽然 TLS 签名可以被规避，但这需要比简单地更改用户代理付出更多的努力。作者指出初步基准测试表明，这种 XDP/eBPF 方法比在用户空间执行类似过滤更快。该项目的代码已开源。

---

## 43. N8n增加了使用DataTables的原生持久化存储

**原文标题**: N8n added native persistent storage with DataTables

**原文链接**: [https://community.n8n.io/t/data-tables-are-here/192256](https://community.n8n.io/t/data-tables-are-here/192256)

N8n将在1.113版本中为所有计划推出数据表（beta版），提供平台内的原生持久存储。此功能解决了长期以来在工作流执行之间存储数据而无需外部平台或凭据的需求。

数据表使用户能够：

*   保存工作流运行的数据。
*   在执行之间持久化数据。
*   跟踪执行状态以防止重复。
*   存储可重用的提示。
*   收集AI工作流评估数据。
*   执行数据查找、合并和增强。

为确保性能，所有用户都有50MB的大小限制。自托管用户可以通过`N8N_DATA_TABLES_MAX_SIZE_BYTES`环境变量调整此限制。

N8n鼓励用户升级到v1.113，并提供关于数据表功能的反馈，包括缺失的功能和潜在的改进。文档可供查阅，以获取更多信息。

---

## 44. OpenAI 2025年上半年：收入43亿美元，亏损135亿美元

**原文标题**: OpenAI's H1 2025: $4.3B in income, $13.5B in loss

**原文链接**: [https://www.techinasia.com/news/openais-revenue-rises-16-to-4-3b-in-h1-2025](https://www.techinasia.com/news/openais-revenue-rises-16-to-4-3b-in-h1-2025)

提供的文本不足以总结整篇文章。它仅包含一个标题，指出 OpenAI 在 2025 年上半年 (H1 2025) 产生了 43 亿美元的收入，但却产生了高达 135 亿美元的亏损，以及一条片段，表明用户需要启用 JavaScript 才能在 Tech in Asia 网站上查看内容。

因此，我只能根据标题进行总结：

OpenAI 在 2025 年上半年经历了重大的财务活动。尽管该公司产生了高达 43 亿美元的收入，但其亏损远超这一数字，达到 135 亿美元。这表明 OpenAI 在收入产生的同时，正处于积极投资、高运营成本或重大债务负担的时期。 在没有全文的情况下，无法确定造成巨额亏损的原因或围绕这些数字的具体背景。

---

## 45. 以色列的行动如何导致加沙饥荒，可视化呈现

**原文标题**: How Israeli actions caused famine in Gaza, visualized

**原文链接**: [https://www.cnn.com/2025/10/02/middleeast/gaza-famine-causes-vis-intl](https://www.cnn.com/2025/10/02/middleeast/gaza-famine-causes-vis-intl)

根据联合国支持的一份报告和众多人道主义组织的说法，本文详细介绍了以色列的行为如何导致加沙地带出现严重的粮食危机，濒临饥荒。这份被考虑承认巴勒斯坦的国家引用的报告预测，到9月底，近三分之一的加沙人口将面临饥荒状况。联合国食物权问题特别报告员指责以色列利用饥饿作为对付巴勒斯坦人的武器，违反了国际法。

以色列否认这些调查结果，声称该报告带有偏见，并基于哈马斯的数据，并声称他们已经增加了援助物资的进入。然而，援助机构辩称，以色列的战争加剧，尤其是在加沙城，阻碍了救援工作。官僚障碍、武断地拒绝物资以及延误审批严重限制了抵达加沙的援助数量。

本文强调了由于道路损坏、燃料短缺和持续的敌对行动，内部援助分配的困难。替代援助运送方法，如美国和以色列支持的加沙人道主义基金会（GHF）站点和空投，被认为是使人丧失尊严、难以获得且危险的，有报道称在这些站点和车队路线附近发生了多起死亡事件。

此外，以色列的攻势已大大减少了可耕种的农田，进一步限制了食物来源。联合国警告说，对加沙城的全面入侵可能会使已经脆弱的援助供应链崩溃，将局势推向“难以想象的灾难”，强调需要停火、畅通无阻的通道以及恢复当地粮食系统，以扭转饥荒局面。

---

## 46. 研究人员开发出在电信频率下通信的分子量子比特

**原文标题**: Researchers develop molecular qubits that communicate at telecom frequencies

**原文链接**: [https://chicagoquantum.org/news/researchers-develop-molecular-qubits-communicate-telecom-frequencies](https://chicagoquantum.org/news/researchers-develop-molecular-qubits-communicate-telecom-frequencies)

多个机构的研究人员开发出了包含铒的、在电信频率下运行的分子量子比特，弥合了光与磁之间的差距。这一突破使与现有光纤网络无缝集成成为可能，为包括量子网络（“量子互联网”）在内的可扩展量子技术铺平了道路。这些网络可以实现超安全通信、连接量子计算机并分发量子传感器。

分子量子比特还可以用作可嵌入不寻常环境中的高灵敏度量子传感器，并且它们与硅光子的兼容性允许集成到芯片中，用于紧凑型量子器件。 稀土元素铒的使用实现了与光和磁场的强烈相互作用。研究人员使用光学光谱学和微波技术证明了量子比特与硅光子的兼容性，表明混合分子-光子平台的发展将加速。

该团队强调了与加州大学伯克利分校的化学家合作的重要性，突出了合成分子化学在优化稀土离子特性方面的作用。他们设想利用合成化学在分子水平上设计和控制量子材料，从而实现为网络、传感和计算量身定制的量子系统。这项研究得到了美国能源部科学办公室和 Q-NEXT 的支持。

---

## 47. 发布 HN：Simplex (YC S24) - 开发者浏览器自动化平台

**原文标题**: Launch HN: Simplex (YC S24) – Browser automation platform for developers

**原文链接**: [https://www.simplex.sh/](https://www.simplex.sh/)

Simplex 推出一款专为开发者设计的浏览器自动化平台，旨在解决与传统网络门户交互自动化方面的挑战。 它为现代浏览器自动化提供所需的基础设施，包括远程浏览器和可控的网络代理。 该平台经过精心设计，能够可靠地与旧系统协同工作，并自动执行各种类型门户的任务，例如账单、事先授权、ERP、政府以及TMS/WMS系统。

Simplex提供诸如缓存代理操作以提高可靠性和快速流程开发、创建具有低延迟的实时流程以实现电话集成以及生产就绪环境等功能。 主要功能包括用于压力测试工作流程的评估工具、身份验证处理SDK、可扩展的无头浏览器、具有验证码解决方案的隐身模式、可控和优化的工作流程、强大的Python和TypeScript SDK以及具有实时会话重放的详细日志记录。 该平台强调可靠性和可扩展性，承诺提供一致的工作流程和轻松的部署。 用户可以预约通话，讨论具体用例并开始使用。

---

## 48. 你想要带瑕疵的技术吗？

**原文标题**: You Want Technology with Warts

**原文链接**: [https://entropicthoughts.com/you-want-technology-with-warts](https://entropicthoughts.com/you-want-technology-with-warts)

本文总结了一场演讲，该演讲提倡选择技术时，应优先考虑技术的寿命和可维护性，而非最前沿的功能，即使这意味着接受一些公认的“瑕疵”。演讲者专注于构建能够持续数十年的 Web 服务，这给作者留下了深刻的印象，作者将其与桥梁和简单的 HTML/CSS 网站等持久的基础设施相提并论。

演讲建议使用 SQLite 进行数据存储，SQL 查询进行应用逻辑，Express-on-Node.js 进行路由，Jinja2 进行展示，以及基本的 HTML/JS 进行 HTTP 请求。虽然作者建议使用 Perl 作为 Node.js 的后端逻辑的替代方案，因为 Perl 被认为具有长期稳定性，但核心论点在于选择具有经过验证的向后兼容性的技术。

作者强调了浏览器不断演变的渲染行为以及在某些情况下整页重新加载的好处。核心思想是将“瑕疵”（如 SQLite 的灵活类型或可为空的主键）重新定义为技术致力于向后兼容性的证明。每个“瑕疵”代表着有人依赖的功能，它的存在表明该技术不太可能在未来引入重大变更。作者认为，预先针对已知的怪癖进行配置，比面对未来更新造成的意外中断要好。目标是选择那些在历史上优先考虑稳定性和遗留支持而非不断创新的技术。

---

## 49. 伊特比

**原文标题**: Ytterby

**原文链接**: [https://en.wikipedia.org/wiki/Ytterby](https://en.wikipedia.org/wiki/Ytterby)

伊特比是瑞典雷萨勒岛上的一个村庄，因是多种元素发现的来源地而闻名。该名称意为“外村”。元素钇(Y)、铽(Tb)、铒(Er)和镱(Yb)以伊特比命名，钬(Ho)、钪(Sc)、铥(Tm)、钽(Ta)和钆(Gd)也首先在那里被发现。

伊特比矿最初在 17 世纪开采石英，从 1790 年开始开采长石，主要用于瓷器制造。长石开采在 19 世纪 60 年代加剧，使该矿成为瑞典石英和长石产量最高的矿之一，直至 1933 年关闭，历时 177 年。该矿后来被改造，从 20 世纪 40 年代末到 1978 年用于储存航空燃料，随后用于储存柴油。它在 20 世纪 90 年代被清空并进行了修复。

1787 年，卡尔·阿克塞尔·阿雷尼乌斯发现了一种重型黑色矿物，后来被鉴定为钆石，其中含有新元素氧化钇。进一步分析揭示了与该地区相关的其他几种稀土元素。1989 年，美国金属学会 (ASM International) 在矿井入口处放置了一块牌匾，以纪念其历史意义。 欧洲化学会于 2018 年将伊特比矿认定为历史地标。

---

## 50. 自监督学习、JEPA、世界模型与人工智能的未来 [视频]

**原文标题**: Self-supervised learning, JEPA, world models, and the future of AI [video]

**原文链接**: [https://www.youtube.com/watch?v=yUmDRxV0krg](https://www.youtube.com/watch?v=yUmDRxV0krg)

YouTube视频“自监督学习、JEPA、世界模型以及人工智能的未来”很可能探讨人工智能的进展，重点关注自监督学习技术，特别是联合嵌入预测架构（JEPA），以及它们与构建“世界模型”的联系。

自监督学习是一种人工智能系统从无标签数据中学习的方法，本质上是通过发现数据中的模式和关系来自我学习。JEPA是自监督学习中的一种特定架构，可能旨在创建更强大且更具通用性的数据表示。

对“世界模型”的讨论表明该视频探讨了如何使用这些技术来构建能够理解和预测世界运作方式的人工智能系统。这使人工智能能够在复杂的环境中更有效地进行计划、推理和行动。

该视频还涉及人工智能领域这些进展的未来影响。它很可能探讨了自监督学习、JEPA和世界模型将如何促进创建更智能、更适应性更强以及更像人类的人工智能系统。

最后，YouTube末尾的样板文字突出了YouTube的条款和政策，以及它在包括测试新功能和与NFL合作等各个领域的持续创新。 这与人工智能主题没有直接关系，而是标准的YouTube页脚信息。

---

## 51. 一个节省我夜晚时间的简单习惯

**原文标题**: A simple habit that saves my evenings

**原文链接**: [https://alikhil.dev/posts/the-simple-habit-that-saves-my-evenings/](https://alikhil.dev/posts/the-simple-habit-that-saves-my-evenings/)

作者分享一个防止浪费夜晚和保持工作生活平衡的简单习惯。问题在于，接近突破时继续工作到深夜的诱惑，这通常会导致精疲力竭、积极性降低和进展甚微。受解决问题的动力驱使，人们常常低估所需时间，最终工作时间超出预期数小时，导致倦怠和第二天的工作效率下降。

作者建议，与其在最后时刻试图完成任务，不如**写下完成任务的详细的分步行动计划。** 这能让人在清楚了解需要做什么的情况下离开工作，减少焦虑，并促进思维清晰。

这种方法的好处有三方面：

*   **防止过度工作：** 它阻止了工作到深夜和耗尽自己的循环。
*   **促进休息和恢复：** 准时下班可以充分休息，从而提高第二天的精力和生产力。
*   **鼓励更好的解决方案：** 休息和新的视角通常会带来新的见解和更好的解决方案。

作者使用这项技巧超过五年，并强调其在维持工作和个人生活之间的平衡方面的有效性。核心信息是通过在结束工作日之前明确定义下一步，避免过度工作，从而实现休息、提高专注力，并最终更有效地完成任务。

---

## 52. RISC-V 条件移动

**原文标题**: RISC-V Conditional Moves

**原文链接**: [https://www.corsix.org/content/riscv-conditional-moves](https://www.corsix.org/content/riscv-conditional-moves)

本文探讨了RISC-V中缺乏直接条件移动指令的问题，并将其与aarch64等架构中更为全面的`csel`指令进行了对比。虽然RISC-V通过Zbb和Zicond（czero.eqz, czero.nez）等扩展提供了一些有限的条件功能，但缺少通用的条件移动指令。

RISC-V指令集手册建议短前向分支可以有效地替代条件移动，并且微架构可能会将这些分支融合为条件移动以提高性能。然而，作者反驳了这种“融合”的有效性，原因在于RISC-V的内存一致性模型。具体而言，分支会在所有后续存储指令上引入语法控制依赖，而条件移动仅在其结果被使用的存储指令上创建数据或地址依赖。

本文强调，将分支转换为条件移动会消除广泛的语法控制依赖，从而可能违反预期的内存模型行为。因此，如果RISC-V内核将分支融合为条件移动，则生成的“融合”指令需要保留类似于分支的属性，以保留内存模型的语义。本质上，由于定义的控制依赖关系，在RISC-V中简单地用条件移动替换分支并非总是安全的。

---

## 53. 我们买了整个GPU，所以我们他妈的一定要用完它。

**原文标题**: We bought the whole GPU, so we're damn well going to use the whole GPU

**原文链接**: [https://hazyresearch.stanford.edu/blog/2025-09-28-tp-llama-main](https://hazyresearch.stanford.edu/blog/2025-09-28-tp-llama-main)

本文详细介绍了为H100 GPU上的Llama-70B推理开发的高吞吐量巨型内核，在ShareGPT基准测试中，端到端吞吐量比SGLang提高了22%以上。其核心思想是通过重叠计算、内存和通信操作来最大化GPU利用率。

作者之前为Llama-1B开发了一个低延迟巨型内核，专注于内存带宽优化。Llama-70B巨型内核解决了更异构的工作负载，平衡了计算密集型（矩阵乘法）和内存密集型（RMS范数）操作，以及张量并行固有的跨GPU通信瓶颈。其关键创新在于利用巨型内核架构在多个层面上实现细粒度的资源重叠：在SM内部（指令流水线），跨SM（不同操作的并发执行），以及跨GPU（后台通信）。

一种新颖的“分布式转置”操作取代了注意力层之后的传统reduce-scatter，以促进O-projection矩阵乘法与通信的重叠。巨型内核围绕一个指令/解释器模型构建，其中细粒度的指令（RMS范数、矩阵乘法等）由GPU上的解释器执行，该解释器对操作进行流水线处理。解释器专门分配线程用于加载、计算和存储，从而在SM内部实现重叠。特殊的“存储器”线程在后台处理跨GPU通信，进一步提高资源利用率。虽然以支持有限的研究代码形式呈现，但作者希望其基本思想和性能提升能够引起社区的兴趣。

---

## 54. 冰鸟：JavaScript冰山阅读器

**原文标题**: Icebird: JavaScript Iceberg Reader

**原文链接**: [https://github.com/hyparam/icebird](https://github.com/hyparam/icebird)

Icebird是一个JavaScript库，旨在直接在JavaScript环境中读取Apache Iceberg表。它基于`hyparquet`构建，方便读取底层的Parquet文件，从而实现从Web应用程序中的Iceberg表访问数据。

主要特性包括：

*   **基本用法：** 提供简单的函数从Iceberg表中读取数据 (`icebergRead`) 和元数据 (`icebergMetadata`)，并指定表URL和行范围。
*   **性能：** 通过提供从 `icebergMetadata` 获取的元数据，可以加快后续读取速度。
*   **时间旅行：** 支持通过指定元数据文件名来获取表的先前版本。
*   **身份验证：** 允许向HTTP请求添加自定义标头以进行身份验证。
*   **演示：** 提供了一个演示，展示了与使用HighTable的React Web应用程序的集成，用于查看Iceberg数据。
*   **支持的特性：** Icebird支持读取Iceberg v1和v2表、Parquet和Avro存储、基于文件的目录、位置和等式删除、列重命名、所有Parquet压缩编解码器和类型。Icebird目前不支持Iceberg v3表、ORC和Puffin存储、REST、Hive、Glue和服务型目录、二进制删除向量、高效的分区读取查询、Variant、Geometry和Geography类型、排序和加密。

---

## 55. 展示一下：路由追踪可视化工具

**原文标题**: Show HN: Traceroute Visualizer

**原文链接**: [https://kriztalz.sh/traceroute-visualizer/](https://kriztalz.sh/traceroute-visualizer/)

这个“Show HN：路由追踪可视化工具”是一个免费的、基于浏览器的工具，帮助用户以地理方式可视化网络路径。它支持标准的traceroute、tracert、高级飞行路由和MTR输出，显示网络数据包在互联网上的传输路径。

该工具会自动检测用户的IP作为起始点。用户随后将他们的traceroute输出粘贴到文本区域，工具会分析它以创建路由图。结果以表格和交互式地图的形式呈现，显示跳数、IP地址（链接到IPinfo）、主机名、位置、ISP、丢包率（如果适用）和响应时间。飞行路由输出显示替代路径，MTR输出提供丢包率和定时统计信息。互联网交换点（IXP）会被识别并在地图上标记。

主要功能包括延迟热图、路由统计（总单向时间和距离）以及分享路由链接的能力。该工具识别在IXP的跳，并用绿色徽章标记它们。

它对于网络故障排除、安全调查、地理路由分析、理解网络基础设施和教育目的非常有用。该工具强调用户隐私，声明数据在浏览器中处理，不存储在服务器上。该工具依赖IPinfo和PeeringDB API获取地理位置和IXP数据。

---

## 56. 一个三千年前的炼铜遗址可能是了解铁起源的关键。

**原文标题**: A 3K-year-old copper smelting site could be key to understanding origins of iron

**原文链接**: [https://phys.org/news/2025-09-year-copper-smelting-site-key.html](https://phys.org/news/2025-09-year-copper-smelting-site-key.html)

本文详述了克兰菲尔德大学的研究，揭示了炼铜厂可能如何无意中开创了炼铁生产。通过重新分析格鲁吉亚克维莫博尔尼西拥有3000年历史的炼铜遗址的冶金遗骸，研究人员发现氧化铁（赤铁矿）被用作助熔剂以提高铜的产量，这与早期认为该遗址是早期炼铁厂的假设相悖。

研究结果支持了炼铁源于炼铜工人实验的理论。 使用赤铁矿作为助熔剂表明，这些金属工人认识到氧化铁是一种独特的材料，并在炉子中探索了其性质。

冶铁技术的发展是历史上的一个关键时刻。虽然铁器时代之前就存在铁器，但它们是由稀有的陨石铁制成的。 从丰富的铁矿石中提取铁的能力使得铁能够广泛用于工具和武器，从而推动了重大的技术和社会变革。

纳撒尼尔·埃尔布-萨图洛博士强调了克维莫博尔尼西作为铜冶炼中有意使用铁的证据的重要性，突出了它在冶铁技术演变中的作用。 通过检查炉渣（冶炼的废料），现代分析技术被用来了解这些古代金属工人的思维过程。 这项研究强调了铜生产遗址在理解铁技术起源方面的重要性。

---

## 57. 使用OCI/Docker镜像仓库发布和安装私有Python包

**原文标题**: PyOCI – Publish and install private Python packages using OCI/Docker registries

**原文链接**: [https://github.com/AllexVeldman/pyoci](https://github.com/AllexVeldman/pyoci)

PyOCI允许您使用OCI/Docker镜像仓库（如`ghcr.io`和Azure Container Registry）作为私有Python包索引，从而无需依赖专门的私有包托管服务。它充当`pip`和OCI镜像仓库之间的代理，利用现有的访问控制机制（如GitHub Packages）。

要安装软件包，请使用`pip install --index-url="http://<用户名>:<密码>@<pyoci-url>/<OCI-registry-url>/<namespace>/" <软件包名>`。公共PyOCI实例可在`https://pyoci.com`上找到。

您还可以使用Docker容器自托管PyOCI。配置通过环境变量完成，包括`PORT`、`PYOCI_PATH`、`PYOCI_MAX_BODY`、`PYOCI_MAX_VERSIONS`和`OTLP_ENDPOINT`。

可以通过在软件包的元数据中添加格式为`PyOCI :: Label :: <Key> :: <Value>`的自定义分类器来标记软件包。身份验证通过`pip`的基本身份验证处理，该身份验证将转发到OCI镜像仓库。更新软件包需要先删除现有版本。如果底层镜像仓库支持内容管理，则支持通过DELETE请求进行删除。

PyOCI也与Renovate兼容，可用于依赖项更新。使用PyOCI的凭据配置Renovate，可以利用GitHub Actions和`GITHUB_TOKEN`进行身份验证，从而授予Renovate对您的私有软件包的读取权限。

---

## 58. Dbos：使用 Go 和 PostgreSQL 实现的持久化工作流编排

**原文标题**: Dbos: Durable Workflow Orchestration with Go and PostgreSQL

**原文链接**: [https://github.com/dbos-inc/dbos-transact-golang](https://github.com/dbos-inc/dbos-transact-golang)

DBOS（持久化工作流编排系统）是一个轻量级系统，它通过利用 PostgreSQL 简化了向应用程序添加持久化工作流和队列的过程。其目标是可靠地处理支付服务和数据管道等应用程序中的故障，而无需复杂的状态管理或外部编排服务。

主要特性包括：

*   **持久化工作流：** 在 Postgres 中检查点程序状态，以便在发生故障后自动恢复，从而能够编排业务流程并构建容错数据管道。
*   **持久化队列：** 在后台运行任务，保证完成和结果交付，即使在中断后也是如此。队列提供流程控制，并且可以配置超时、速率限制、去重和优先级。
*   **仅一次事件处理：** 可靠地处理诸如 Webhook 和 Kafka 消息之类的事件。
*   **持久化调度：** 使用 cron 语法或持久化睡眠来调度工作流，确保即使在重启后也能在指定时间执行。
*   **持久化通知：** 暂停工作流直到收到通知，或者发出事件以进行进度更新，所有这些都具有仅一次语义。

DBOS 与 Temporal、Airflow 和 Celery/BullMQ 等其他系统进行了比较，突出了它在需要最少架构改造、Postgres 集成、以代码形式编写工作流的灵活性以及可靠性至关重要的场景中的优势。虽然它可能无法与专用队列系统的性能相媲美，但其持久性使其适合于需要围绕任务完成和工作流执行提供强有力保证的应用程序。

---

## 59. 一万个俯卧撑和其他改变我人生的愚蠢健身挑战

**原文标题**: 10k pushups and other silly exercise quests that changed my life

**原文链接**: [https://wjgilmore.com/articles/10000-pushups](https://wjgilmore.com/articles/10000-pushups)

2025年，由于感到身体不适并担忧自己对孩子的榜样作用，作者开始了为期一年的挑战，目标是完成一万个俯卧撑。最初，他用 Google Sheet 记录进度，这项挑战激励他坚持锻炼。他将俯卧撑目标与其他生活方式的改变相结合，包括在一次糟糕的经历后戒掉快餐，并限制酒精摄入。

在这一年中，作者的动力时有起伏，冬季月份运动量下降，但在春夏季节则增加了强度。他加入了其他形式的锻炼，例如举重、跑步，甚至尝试劈叉。工作中友好的俯卧撑比赛和一个自行组织的“5/15/500 挑战”（跑步、骑自行车、自重训练）进一步激发了他的投入。

饮食成为了重点，最初涉及卡路里限制，后来转变为消除含有微塑料和重金属的产品。他报名参加了半程马拉松，购买了一块跑步手表来追踪他的配速，并利用 GU 能量胶来增强耐力。

到 2025 年 9 月，作者完成了他的一万个俯卧撑的目标，并经历了显著的积极变化。他的肌肉明显增加，衣服不再合身，并且他收到了关于他改善后的体格的赞扬。这次旅程培养了自律、更健康的生活方式，以及对运动和正念饮食的新认识。尽管月底小腿受伤，作者的整体健康和福祉得到了显著改善。

---

## 60. 从零开始编写LLM，第20部分：开始训练，以及交叉熵损失

**原文标题**: Writing an LLM from scratch, part 20 – starting training, and cross entropy loss

**原文链接**: [https://www.gilesthomas.com/2025/10/llm-from-scratch-20-starting-training-cross-entropy-loss](https://www.gilesthomas.com/2025/10/llm-from-scratch-20-starting-training-cross-entropy-loss)

在这篇博文中，Giles深入探讨了LLM的训练过程，特别是着重讲解了损失函数和交叉熵损失。他首先引用了Sebastian Raschka所著《从零开始构建大型语言模型》一书的第五章，该章节解释了如何训练LLM。Giles强调了损失函数在梯度下降中的重要性，它能指示模型结果的不准确性。

他解释了LLM如何预测输入序列中每个token的logits（预测值），以及训练目标如何是“左移”的原始序列。这使得从单个输入序列中进行多次训练成为可能。Giles强调，每个前缀序列/目标对都可以被视为独立的，用于计算损失函数。

这篇博文的核心围绕交叉熵损失展开，这是一种衡量模型预测与目标token偏差程度的方法。他解释说，与其比较所有token概率之间的差异，不如只关注分配给目标token的概率，并通过最小化该概率的负对数来有效地训练模型。他分解了交叉熵损失的数学原理，解释了它如何衡量预测概率与实际（one-hot编码）目标之间的差异。

Giles还通过对信息论中熵的高层次解释以及它与概率分布“混乱度”概念的联系，解答了为什么它被称为“交叉熵”。

---

## 61. 你们把这些人工智能风险的争论想得太复杂了。

**原文标题**: Y'all are over-complicating these AI-risk arguments

**原文链接**: [https://dynomight.net/ai-risk/](https://dynomight.net/ai-risk/)

作者认为，人工智能风险论证常常过于复杂，并提出一个更简单的替代方案，基于高智商外星人抵达地球的类比。这个简单论证归结为：如果在未来几十年内具备300智商的人工智能是可能的，而且我们不知道它会是什么样子，那么我们就应该关注人工智能风险，正如我们应该关注这类外星人一样。

作者倾向于这个简单论证，因为它更可能为真（由于假设更少）且更具说服力（依赖于现有直觉）。它也有助于识别核心分歧：人们是否真正相信具备类人能力和超人工智能的人工智能是可能的。

然而，作者也承认复杂论证的合理性，特别是“中间”版本，即*如果*人类出现问题，人工智能*很可能*是原因。这证明了专注于复杂情景是合理的。

最后，作者从战略信息传递的角度探讨了使用哪种论证的问题。虽然最初倾向于简单论证的清晰性，但作者考虑到最近的民意调查显示，人们普遍担忧人工智能。这使得作者推测，一个更自信、尽管复杂的论证可能更有效，鼓励人们摆脱被动的担忧状态并采取行动。作者最后主张，应该论证你真正相信的事情，而不是为了所谓的观感而淡化它。

---

## 62. 为什么大多数产品规划都很糟糕以及如何改进

**原文标题**: Why most product planning is bad and what to do about it

**原文链接**: [https://blog.railway.com/p/product-planning-improvement](https://blog.railway.com/p/product-planning-improvement)

安杰洛·萨拉切诺的文章《为什么大多数产品规划都很糟糕以及如何改进》详细介绍了 Railway 在用户规模扩展到 170 万以上时改进规划流程的历程。他们对传统方法（如 OKR，这种方法形式大于内容）感到失望，因此开发了“问题驱动开发”。

文章认为，传统规划往往依赖于指标驱动的形式主义、阻碍交易的功能请求或创始人直觉，导致工程师不满。Railway 最初尝试了一种轻量级的 SAFE 方法，然后尝试了 OKR，但发现 OKR 缺乏灵活性，并且依赖于具体的、易于衡量的目标，更适合工厂或销售，而不是创造性的工程工作。

他们的解决方案“问题驱动开发”是一个为期 4 天的季度流程，侧重于识别和优先排序问题，而不是解决方案。团队独立记录问题，“规划负责人”分配优先级，然后检查依赖关系和容量。最后，团队公开承诺，并为每个问题分配一名 DRI（直接责任人）。只有在承诺之后，他们才开始 RFC 和 Linear 工单。

主要收获：

*   **最初关注问题，而不是解决方案。** 这可以防止过早地依附于不成熟的解决方案。
*   **独立团队优先级排序** 避免了最吵闹的声音的主导。
*   **提前进行关于依赖关系和容量的艰难对话。**
*   **公开承诺** 培养了责任感。

萨拉切诺强调，这个过程并非高深莫测，但文化至关重要。创造一个人们可以安全地提出问题而不必为解决方案辩护的环境是关键。他们计划开源他们的 Notion 模板，并承认这个过程将继续发展。

---

## 63. Perplexity 在 Windows 和 macOS 上免费发布 Comet 浏览器

**原文标题**: Perplexity releases Comet browser for free on Windows and macOS

**原文链接**: [https://www.ghacks.net/2025/10/03/perplexity-releases-comet-browser-for-free-on-windows-and-macos/](https://www.ghacks.net/2025/10/03/perplexity-releases-comet-browser-for-free-on-windows-and-macos/)

Perplexity 在七月最初面向订阅用户推出后，现已在 Windows 和 macOS 上免费发布其 AI 驱动的“Comet”浏览器。 作者根据有限的测试对该浏览器进行了中立的概述，并强调这不是一篇评测。

Comet 基于 Chromium 构建，可从现有浏览器导入数据。 它具有熟悉的界面，内置广告拦截器和 AI 驱动的功能，如“总结”按钮和“助手”聊天机器人。 一个关键特性是其“智能 AI”，允许用户委托任务，例如查找优惠券或比较产品，然后由浏览器自动执行。

作者指出了一些缺点，包括持续的登录弹出窗口和与 uBlock Origin Lite 等扩展程序相比之下，内置广告拦截器的效果不佳。 他们还批评缺乏自定义新标签页体验的选项。 作者对 AI 表达了隐私担忧，并声明他们在未登录的情况下使用了该浏览器。

文章重点介绍了 Perplexity 的“Comet Plus”订阅服务（包含在 Perplexity Pro Max 中），旨在支持新闻业。 每月 5 美元，它使用户和 AI 浏览器能够访问来自 CNN、Wired 和《华盛顿邮报》等合作新闻出版商的内容。 作者质疑将为其他出版商提供什么样的支持。 作者最后请读者分享他们自己使用 Comet 浏览器的体验。

---

## 64. 工作不是学校：如何在机构愚蠢中求生

**原文标题**: Work is not school: Surviving institutional stupidity

**原文链接**: [https://www.leadingsapiens.com/surviving-institutional-stupidity/](https://www.leadingsapiens.com/surviving-institutional-stupidity/)

本文认为，职场的运行规则与学校不同，仅凭能力无法保证成功。相反，组织常常受到“制度性愚蠢”、有缺陷的心理和相互竞争的利益所驱动。本文旨在为那些在现实中挣扎的高绩效者提供指导。

主要观点包括：将问题归咎于“愚蠢”（惯性、不良激励）而不是恶意，能让人采取更积极主动的态度。能力很重要，但需要可见性和战略定位。感知，尤其是在关键影响者中的感知，与绩效同等重要，需要积极管理个人形象。

本文强调理解组织内部的主观逻辑，并有效定位你的工作，使其与决策者产生共鸣的重要性。它还警告不要将个人标准普遍应用，主张认识并预见他人行事方式的不对称性。

此外，本文承认在更高组织层级存在瓶颈，主观标准占据主导地位。“放长线钓大鱼”需要容忍挫折和清楚了解游戏规则。专注于你的可控范围并保持内在控制点有助于防止倦怠。最后，本文倡导建立工作之外的“平衡意义组合”，以增强应对组织挫折的韧性。文章总结道，驾驭组织的荒谬之处在于理解系统，从而从内部有效做出贡献。

---

## 65. 荷兰法官：Meta必须尊重用户对推荐系统的选择

**原文标题**: NL Judge: Meta must respect user's choice of recommendation system

**原文链接**: [https://www.bitsoffreedom.nl/2025/10/02/judge-in-the-bits-of-freedom-vs-meta-lawsuit-meta-must-respect-users-choice/](https://www.bitsoffreedom.nl/2025/10/02/judge-in-the-bits-of-freedom-vs-meta-lawsuit-meta-must-respect-users-choice/)

荷兰法官裁定Meta违反《数字服务法》，用户对其Facebook和Instagram信息流控制受限。

---

## 66. 让路狄克斯特拉：新算法改写了计算机科学70年历史

**原文标题**: Move over Dijkstra: New Algorithm Just Rewrote 70 Years of Computer Science

**原文链接**: [https://medium.com/@kanishks772/move-over-dijkstra-the-new-algorithm-that-just-rewrote-70-years-of-computer-science-d670696c440d](https://medium.com/@kanishks772/move-over-dijkstra-the-new-algorithm-that-just-rewrote-70-years-of-computer-science-d670696c440d)

清华大学段然团队开发出一种超越Dijkstra算法的新算法，在寻找最短路径方面取得了重大突破。近70年来，Dijkstra算法（1956年创建）一直是该任务的主导方法，支撑着从GPS到网络路由等应用。Dijkstra算法通过使用排序优先级队列贪婪地选择最近的未访问顶点来工作。

新算法实现了确定性的O(m log^(2/3) n)时间复杂度，打破了过去40年来限制最短路径算法的“排序壁垒”。 这一进步被描述为对教科书假设的挑战，也是算法效率方面的一个重大进步。

---

## 67. 下课铃响：乔·利曼德和阿尔法学校侧写

**原文标题**: Class Dismissed: Profile of Joe Liemandt and Alpha School

**原文链接**: [https://joincolossus.com/article/joe-liemandt-class-dismissed/](https://joincolossus.com/article/joe-liemandt-class-dismissed/)

好的，我已阅读了来自所提供URL的文章“课堂解散：Joe Liemandt和Alpha School的简介”。

以下是一个简明扼要的总结：

这篇文章介绍了乔·利曼特(Joe Liemandt)，一位非常成功但相对不为人知的企业家，他在企业软件领域发了财。利曼特从斯坦福大学辍学，创立了Trilogy公司，该公司专门从事复杂产品的配置。Trilogy在20世纪90年代蓬勃发展，使利曼特成为亿万富翁。

这篇文章将利曼特的成功归因于他专注于识别有才华的人、培养一种坚持不懈的努力工作和创新的文化，以及专注于复杂的小众市场。他以雇用年轻、雄心勃勃的人，并挑战他们突破自己的极限而闻名。

在Trilogy之后，利曼特创立了ESW Capital，一家收购并扭转困境软件公司的私募股权公司。ESW的策略包括激进的削减成本、运营效率的提高，以及对标准化流程的重视。ESW与Trilogy一样，以其严苛的工作环境而闻名。

最近，利曼特创立了Alpha School，一项旨在为年轻人提供软件开发、销售和营销方面实用技能的教育事业。Alpha School旨在加速学习过程，并为学生准备科技行业高需求的工作。这篇文章强调了Alpha School通过专注于基于技能的培训和直接就业安置来颠覆传统教育模式的潜力。利曼特的愿景是创建一个能够应对现代科技领域挑战的劳动力队伍。这篇文章将利曼特描述为一个充满动力的人，他对商业和教育有着独特的方法，并不断寻求优化和加速进步。

---

## 68. A primer for using weather surveillance radar to study bird migration

**原文标题**: A primer for using weather surveillance radar to study bird migration

**原文链接**: [https://birdcast.info/news/a-primer-for-using-weather-surveillance-radar-to-study-bird-migration/](https://birdcast.info/news/a-primer-for-using-weather-surveillance-radar-to-study-bird-migration/)

生成摘要时出错

---

## 69. The RAG Obituary: Killed by agents, buried by context windows

**原文标题**: The RAG Obituary: Killed by agents, buried by context windows

**原文链接**: [https://www.nicolasbustamante.com/p/the-rag-obituary-killed-by-agents](https://www.nicolasbustamante.com/p/the-rag-obituary-killed-by-agents)

生成摘要时出错

---

## 70. Anti-aging breakthrough: Stem cells reverse signs of aging in monkeys

**原文标题**: Anti-aging breakthrough: Stem cells reverse signs of aging in monkeys

**原文链接**: [https://www.nad.com/news/anti-aging-breakthrough-stem-cells-reverse-signs-of-aging-in-monkeys](https://www.nad.com/news/anti-aging-breakthrough-stem-cells-reverse-signs-of-aging-in-monkeys)

生成摘要时出错

---

## 71. 'Western Qwen': IBM Wows with Granite 4 LLM Launch and Hybrid Mamba/Transformer

**原文标题**: 'Western Qwen': IBM Wows with Granite 4 LLM Launch and Hybrid Mamba/Transformer

**原文链接**: [https://venturebeat.com/ai/western-qwen-ibm-wows-with-granite-4-llm-launch-and-hybrid-mamba-transformer](https://venturebeat.com/ai/western-qwen-ibm-wows-with-granite-4-llm-launch-and-hybrid-mamba-transformer)

生成摘要时出错

---

## 72. The history of cataract surgery

**原文标题**: The history of cataract surgery

**原文链接**: [https://www.asimov.press/p/cataracts](https://www.asimov.press/p/cataracts)

生成摘要时出错

---

## 73. Pre-record your demos

**原文标题**: Pre-record your demos

**原文链接**: [https://www.steveharrison.dev/pre-record-your-demos/](https://www.steveharrison.dev/pre-record-your-demos/)

生成摘要时出错

---

## 74. Gmail will no longer support checking emails from third-party accounts via POP

**原文标题**: Gmail will no longer support checking emails from third-party accounts via POP

**原文链接**: [https://support.google.com/mail/answer/16604719?hl=en](https://support.google.com/mail/answer/16604719?hl=en)

生成摘要时出错

---

## 75. Which Table Format Do LLMs Understand Best? (Results for 11 Formats)

**原文标题**: Which Table Format Do LLMs Understand Best? (Results for 11 Formats)

**原文链接**: [https://www.improvingagents.com/blog/best-input-data-format-for-llms](https://www.improvingagents.com/blog/best-input-data-format-for-llms)

生成摘要时出错

---

## 76. Two Amazon delivery drones crash into crane in commercial area of Tolleson, AZ

**原文标题**: Two Amazon delivery drones crash into crane in commercial area of Tolleson, AZ

**原文链接**: [https://www.abc15.com/news/region-west-valley/tolleson/two-amazon-delivery-drones-crash-into-crane-in-commercial-area-of-tolleson](https://www.abc15.com/news/region-west-valley/tolleson/two-amazon-delivery-drones-crash-into-crane-in-commercial-area-of-tolleson)

生成摘要时出错

---

## 77. Immich v2.0.0 – First stable release

**原文标题**: Immich v2.0.0 – First stable release

**原文链接**: [https://github.com/immich-app/immich/discussions/22546](https://github.com/immich-app/immich/discussions/22546)

生成摘要时出错

---

## 78. Keyhive – Local-first access control

**原文标题**: Keyhive – Local-first access control

**原文链接**: [https://www.inkandswitch.com/keyhive/notebook/](https://www.inkandswitch.com/keyhive/notebook/)

生成摘要时出错

---

## 79. The Answer (1954)

**原文标题**: The Answer (1954)

**原文链接**: [https://sfshortstories.com/?p=5983](https://sfshortstories.com/?p=5983)

生成摘要时出错

---

## 80. Red Hat confirms security incident after hackers breach GitLab instance

**原文标题**: Red Hat confirms security incident after hackers breach GitLab instance

**原文链接**: [https://www.bleepingcomputer.com/news/security/red-hat-confirms-security-incident-after-hackers-claim-github-breach/](https://www.bleepingcomputer.com/news/security/red-hat-confirms-security-incident-after-hackers-claim-github-breach/)

生成摘要时出错

---

## 81. Sony's New Global Shutter Sensor Captures 105 Megapixels at 100FPS

**原文标题**: Sony's New Global Shutter Sensor Captures 105 Megapixels at 100FPS

**原文链接**: [https://petapixel.com/2025/09/29/sonys-new-global-shutter-sensor-captures-105-megapixels-at-100fps/](https://petapixel.com/2025/09/29/sonys-new-global-shutter-sensor-captures-105-megapixels-at-100fps/)

生成摘要时出错

---

## 82. I built ChatGPT with Minecraft redstone [video]

**原文标题**: I built ChatGPT with Minecraft redstone [video]

**原文链接**: [https://www.youtube.com/watch?v=VaeI9YgE1o8](https://www.youtube.com/watch?v=VaeI9YgE1o8)

生成摘要时出错

---

## 83. Google Workspace Updates: Send Gmail end-to-end encrypted emails to anyone

**原文标题**: Google Workspace Updates: Send Gmail end-to-end encrypted emails to anyone

**原文链接**: [https://workspaceupdates.googleblog.com/2025/10/send-gmail-end-to-end-encrypted-emails-in-gmail.html](https://workspaceupdates.googleblog.com/2025/10/send-gmail-end-to-end-encrypted-emails-in-gmail.html)

生成摘要时出错

---

## 84. Blender 4.5 LTS

**原文标题**: Blender 4.5 LTS

**原文链接**: [https://lwn.net/Articles/1036262/](https://lwn.net/Articles/1036262/)

生成摘要时出错

---

## 85. Gemini 3.0 Pro – early tests

**原文标题**: Gemini 3.0 Pro – early tests

**原文链接**: [https://twitter.com/chetaslua/status/1973694615518880236](https://twitter.com/chetaslua/status/1973694615518880236)

生成摘要时出错

---

## 86. A replica of Citizen Quartz watch based on Harel's paper introducing statecharts

**原文标题**: A replica of Citizen Quartz watch based on Harel's paper introducing statecharts

**原文链接**: [https://andyjakubowski.github.io/statechart-watch/](https://andyjakubowski.github.io/statechart-watch/)

生成摘要时出错

---

## 87. F3: Open-source data file format for the future [pdf]

**原文标题**: F3: Open-source data file format for the future [pdf]

**原文链接**: [https://db.cs.cmu.edu/papers/2025/zeng-sigmod2025.pdf](https://db.cs.cmu.edu/papers/2025/zeng-sigmod2025.pdf)

生成摘要时出错

---

## 88. IP over Lasers

**原文标题**: IP over Lasers

**原文链接**: [https://www.mikekohn.net/micro/ip_over_lasers.php](https://www.mikekohn.net/micro/ip_over_lasers.php)

生成摘要时出错

---

## 89. Throne of the Third Heaven of the Nations' Millennium General Assembly (2021)

**原文标题**: Throne of the Third Heaven of the Nations' Millennium General Assembly (2021)

**原文链接**: [https://americanart.si.edu/blog/throne-james-hampton](https://americanart.si.edu/blog/throne-james-hampton)

生成摘要时出错

---

## 90. Show HN: Autism Simulator

**原文标题**: Show HN: Autism Simulator

**原文链接**: [https://autism-simulator.vercel.app/](https://autism-simulator.vercel.app/)

生成摘要时出错

---

## 91. Make the most of compiled C loops on the 68000

**原文标题**: Make the most of compiled C loops on the 68000

**原文链接**: [https://dciabrin.net/posts/make-the-most-of-compiled-c-loops-on-the-68000/make-the-most-of-compiled-c-loops-on-the-68000/](https://dciabrin.net/posts/make-the-most-of-compiled-c-loops-on-the-68000/make-the-most-of-compiled-c-loops-on-the-68000/)

生成摘要时出错

---

## 92. Show HN: The Unite real time operating system

**原文标题**: Show HN: The Unite real time operating system

**原文链接**: [https://jacquesmattheij.com/unite-operating-system/](https://jacquesmattheij.com/unite-operating-system/)

生成摘要时出错

---

## 93. PortalVR: XR Without a Headset

**原文标题**: PortalVR: XR Without a Headset

**原文链接**: [https://portalvr.io/](https://portalvr.io/)

生成摘要时出错

---

## 94. Show HN: Glide, an extensible, keyboard-focused web browser

**原文标题**: Show HN: Glide, an extensible, keyboard-focused web browser

**原文链接**: [https://blog.craigie.dev/introducing-glide/](https://blog.craigie.dev/introducing-glide/)

生成摘要时出错

---

## 95. Adding a new instruction to RISC-V back end in LLVM

**原文标题**: Adding a new instruction to RISC-V back end in LLVM

**原文链接**: [https://blog.gustavoleite.me/llvm-riscv-instruction](https://blog.gustavoleite.me/llvm-riscv-instruction)

生成摘要时出错

---

## 96. Apple takes down ICE tracking apps after pressure from DOJ

**原文标题**: Apple takes down ICE tracking apps after pressure from DOJ

**原文链接**: [https://www.foxbusiness.com/politics/apple-takes-down-ice-tracking-app-after-pressure-from-ag-bondi](https://www.foxbusiness.com/politics/apple-takes-down-ice-tracking-app-after-pressure-from-ag-bondi)

生成摘要时出错

---

## 97. Increasing your practice surface area

**原文标题**: Increasing your practice surface area

**原文链接**: [https://www.indiehackers.com/post/lifestyle/increasing-your-practice-surface-area-agxYGi9bL0gd1WYYQZAu](https://www.indiehackers.com/post/lifestyle/increasing-your-practice-surface-area-agxYGi9bL0gd1WYYQZAu)

生成摘要时出错

---

## 98. Show HN: BetterBrain – Dementia prevention, covered by insurance

**原文标题**: Show HN: BetterBrain – Dementia prevention, covered by insurance

**原文链接**: [https://www.betterbrain.com/insurance](https://www.betterbrain.com/insurance)

生成摘要时出错

---

## 99. Cormac McCarthy's personal library

**原文标题**: Cormac McCarthy's personal library

**原文链接**: [https://www.smithsonianmag.com/arts-culture/two-years-cormac-mccarthys-death-rare-access-to-personal-library-reveals-man-behind-myth-180987150/](https://www.smithsonianmag.com/arts-culture/two-years-cormac-mccarthys-death-rare-access-to-personal-library-reveals-man-behind-myth-180987150/)

生成摘要时出错

---

## 100. Forth in Zig and WebAssembly

**原文标题**: Forth in Zig and WebAssembly

**原文链接**: [https://zig-wasm.github.io/zorth/](https://zig-wasm.github.io/zorth/)

生成摘要时出错

---

