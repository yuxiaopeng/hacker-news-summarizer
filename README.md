# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-10-03.md)

*最后自动更新时间: 2025-10-03 17:46:03*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 2 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 3 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 4 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 5 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 6 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 7 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 8 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 9 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 10 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 11 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 12 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 13 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 14 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 15 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 16 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 17 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 18 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 19 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 20 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 21 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 22 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 23 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 24 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 25 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 26 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 27 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 28 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 29 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 30 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 31 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 32 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 33 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 34 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 35 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 36 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 37 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 38 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 39 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 40 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 41 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 42 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 43 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 44 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 45 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 46 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 47 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 48 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 49 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 50 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 51 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 52 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 53 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 54 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 55 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 56 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 57 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 58 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 59 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 60 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 61 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 62 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 63 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 64 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 65 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 66 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 67 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 68 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 69 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 70 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 71 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 72 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 73 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 74 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 75 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 76 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 77 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 78 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 79 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 80 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 81 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 82 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 83 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 84 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 85 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 86 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 87 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 88 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 89 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 90 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 91 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 92 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 93 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 94 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 95 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 96 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 97 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 98 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 99 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 100 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 101 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 102 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 103 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 104 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 105 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 106 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 107 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 108 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 109 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 110 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 111 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 112 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 113 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 114 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 115 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 116 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 117 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 118 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 119 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 120 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 121 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 122 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 123 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 124 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 125 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 126 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 127 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 128 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 129 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 130 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 131 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 132 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 133 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 134 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 135 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 136 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 137 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 138 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 139 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 140 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 141 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 142 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 143 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 144 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 145 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 146 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 147 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 148 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 149 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 150 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 151 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 152 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 153 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 154 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 155 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 156 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 157 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 158 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 159 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 160 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 161 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 162 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 163 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 164 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 165 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 166 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 167 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 168 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 169 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 170 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 171 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 172 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 173 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 174 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 175 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 176 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 177 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 178 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 179 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 180 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 181 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 182 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 183 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 184 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 185 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 186 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 187 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 188 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 189 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 190 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 191 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 192 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 193 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 194 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 195 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 196 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 197 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 198 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
