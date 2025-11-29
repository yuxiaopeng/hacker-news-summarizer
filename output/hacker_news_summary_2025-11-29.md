# Hacker News 热门文章摘要 (2025-11-29)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 总是流程，笨蛋！

**原文标题**: It's Always the Process, Stupid

**原文链接**: [https://its.promp.td/its-always-the-process-stupid/](https://its.promp.td/its-always-the-process-stupid/)

本文认为，人工智能在商业中的成功应用取决于扎实的业务流程优化（BPO），而不是简单地将人工智能作为解决现有问题的“魔杖”。文章批评了当前只关注人工智能战略而忽略根本流程效率低下的做法，并警告说人工智能只会加速现有垃圾流程的运行速度。

核心问题在于非结构化数据。人工智能擅长处理诸如电子邮件和PDF之类的混乱数据，这表明依赖非结构化数据的流程通常本身就是非结构化的，未被记录，而是存在于资深员工的专业知识中。在有效应用人工智能之前，需要将这些隐藏流程揭示出来，进行分析和结构化。

文章强调了在自动化之前理解流程中的触发、转换和结构化输出的重要性。它区分了“更智能”和“更快”，解释说人工智能主要加速模式匹配，而真正的智能（智慧、背景）仍然需要人工监督。

最终，作者主张回归基本的BPO原则。企业在考虑将人工智能作为加速器之前，应先梳理其价值链，识别瓶颈和浪费，并简化流程。关键信息是，技术在不断变化，但业务效率的规则始终不变：流程永远是关键。作者还提到了由业务IT（合规性、效率）和社会IT（社交互动）组成的IT鸿沟，并解释了为什么企业在人工智能应用方面举步维艰。

---

## 2. 冰岛宣布洋流不稳定为国家安全风险。

**原文标题**: Iceland declares ocean-current instability a national security risk

**原文链接**: [https://www.dagens.com/news/iceland-declares-ocean-current-instability-a-national-security-risk](https://www.dagens.com/news/iceland-declares-ocean-current-instability-a-national-security-risk)

冰岛将大西洋经向翻转环流（AMOC）潜在崩溃列为国家安全风险，理由是越来越多的证据表明该环流不稳定，并可能造成剧烈的气候和经济后果。 这是冰岛首次将气候影响指定为国家安全风险。

该决定是基于一项新的研究，该研究对AMOC提出了“严重关切”，AMOC是一个重要的洋流系统，调节着整个大西洋的天气。官员们担心，崩溃可能会扰乱运输，破坏基础设施，并摧毁渔业。

专家警告说，气温升高和盐度水平紊乱正在减缓AMOC，可能会导致本世纪出现临界点。崩溃可能会引发美国和欧洲沿海地区海平面急剧上升，非洲和亚洲季风中断，以及欧洲部分地区，特别是冰岛的深度冻结，冰岛可能会被海冰包围。

国家安全指定将触发一项协调一致的高级别政府努力，以分析威胁并制定策略来管理或减轻潜在后果。冰岛环境、能源和气候部长强调了生存威胁，称剧烈的气候变化可能会使适应变得不可能，国家生存和安全受到威胁。鼓励其他国家以类似的紧迫性对待这一风险。

---

## 3. DNS LOC记录 (2014)

**原文标题**: DNS LOC Record (2014)

**原文链接**: [https://blog.cloudflare.com/the-weird-and-wonderful-world-of-dns-loc-records/](https://blog.cloudflare.com/the-weird-and-wonderful-world-of-dns-loc-records/)

本文探讨了在Cloudflare权威DNS服务器RRDNS中支持鲜为人用的DNS LOC记录的实现与挑战。作者John Graham-Cumming解释说，LOC记录指定一个物理位置，尽管它们很少见，但Cloudflare遇到了一种情况，即客户的LOC记录未被正确提供。

调查显示，RRDNS缺少将LOC记录的文本表示形式（纬度、经度、海拔、大小、精度）解析为传输所需的二进制格式的代码。本文详细介绍了RFC 1876中定义的文本和二进制格式，重点介绍了用于大小和精度的复杂编码，该编码允许有效地表示各种值。

作者随后描述了解决方案：编写LOC文本记录类型的解析器以及相关测试。修复程序推出后，现有的LOC记录已由RRDNS正确提供。文章最后提供了一个成功的LOC记录查询示例，并简要概述了Cloudflare的使命和服务。主要结论是在大规模运营时处理即使是晦涩的DNS记录类型也很重要，以及确保与RFC 1876等旧标准兼容所涉及的挑战。

---

## 4. 八公：图像搜索引擎

**原文标题**: Hachi: An Image Search Engine

**原文链接**: [https://eagledot.xyz/hachi.md.html](https://eagledot.xyz/hachi.md.html)

Hachi：一个图像搜索引擎 详细介绍了以图像为中心的自托管个人搜索引擎的开发，未来计划扩展到视频、文本和音频。作者的动机源于现有搜索引擎的局限性，这些搜索引擎无法适应人类查询的随机性以及改进结果所需的用户反馈。Hachi旨在向用户展示资源的多个属性，从而允许递归查询细化。

该项目的关键原则包括极简主义（减少外部依赖）、实验性（融合确定性和语义属性）和易hack性（使代码易于修改）。作者的目标是通过使用元数据索引引擎与用于语义搜索的向量搜索引擎相结合来避免数据重复。该系统使用Python和Nim构建，Nim用于性能关键的部分。

元索引是一个用Nim编写的单线程、面向列的数据库，用于存储和查询元数据。作者讨论了在Nim中进行字符串查询的挑战，以及使用ShortString数据类型进行潜在的性能改进。

一个重要的功能是面部识别，涉及检测面部、识别地标以及生成用于最近邻搜索的嵌入。作者承认在选择平衡延迟、准确性和硬件要求的实现方案方面存在困难。

---

## 5. 哈萨克斯坦青铜时代大型聚落拥有先进的城市规划和冶金术

**原文标题**: Bronze Age mega-settlement in Kazakhstan has advanced urban planning, metallurgy

**原文链接**: [https://archaeologymag.com/2025/11/bronze-age-mega-settlement-in-kazakhstan/](https://archaeologymag.com/2025/11/bronze-age-mega-settlement-in-kazakhstan/)

无法访问文章链接。

---

## 6. Mac mini G4 原生启动 System 7

**原文标题**: System 7 natively boots on the Mac mini G4

**原文链接**: [https://macos9lives.com/smforum/index.php?topic=7711.0](https://macos9lives.com/smforum/index.php?topic=7711.0)

该论坛帖子宣布System 7已成功在Mac mini G4上原生启动。这具有重要意义，因为Mac mini G4最初并非设计用于运行System 7。该帖子位于一个专门在不支持的硬件上运行Mac OS 9及更早操作系统的论坛上。该帖子是讨论与Mac OS 9相关的破解和升级的更广泛主题的一部分。论坛上最近的主题包括关于在Mac mini G4上启动Mac OS 9的讨论，其中包含详细的帖子，寻找完美的启动器，与Mac OS 9兼容的SSD，Mac OS 9.2.2中的1.5GB内存限制，在旧系统上编写软件，购买旧硬件以及解决启动问题。该论坛还提供XHTML、RSS和WAP2订阅源。

---

## 7. AccessOwl (YC S22) 招聘技术客户经理 (IAM)

**原文标题**: AccessOwl (YC S22) Is Hiring a Technical Account Manager (IAM)

**原文链接**: [https://www.ycombinator.com/companies/accessowl/jobs/dGC3pcO-technical-account-manager-identity-access-management](https://www.ycombinator.com/companies/accessowl/jobs/dGC3pcO-technical-account-manager-identity-access-management)

AccessOwl (YC S22) 是一家构建 AI 原生访问治理套件的初创公司，现招聘技术客户经理 (IAM)，负责售后客户关系，指导客户进行产品导入和实施，并将客户需求转化为技术解决方案。该职位包括故障排除、主动监控账户健康状况，并提供客户反馈以塑造产品路线图。

理想的候选人拥有 3 年以上 IT 管理或帮助台经验（有 MSP 经验者优先），对 IT、身份和 SaaS 生态系统（Google Workspace、Okta 等）有扎实的理解，并具备与技术和非技术利益相关者沟通的优秀沟通能力。最好是具有实践经验、具有构建者思维并在初创环境中蓬勃发展的解决问题的人。

AccessOwl 在北美提供远程优先的工作环境，工作时间灵活，每年有国际团队旅行，并有机会在早期、盈利的初创公司中塑造客户管理职能。他们注重影响力、实用主义和构建以客户为中心的流程。申请者应包含三句话，说明他们对该职位的个人兴趣。

AccessOwl 旨在利用 RPA 和代理式 AI 工作流程简化 SaaS 访问、支出和合规性，取代 Okta 等传统解决方案、过时的工单系统和电子表格。他们是一支以客户为中心的团队，致力于解决 IT 和安全团队的实际问题。

---

## 8. CRDT字典：无冲突复制数据类型的实地指南

**原文标题**: The CRDT Dictionary: A Field Guide to Conflict-Free Replicated Data Types

**原文链接**: [https://www.iankduncan.com/engineering/2025-11-27-crdt-dictionary/](https://www.iankduncan.com/engineering/2025-11-27-crdt-dictionary/)

无冲突复制数据类型（CRDT）实战指南：为分布式系统设计的数据结构，可应对并发写入和网络分区。与依赖共识或“后写胜出”的传统方法不同，CRDT 确保跨副本的数据确定性合并，无需协调。

本文强调 CRDT 的工作原理在于其合并操作满足交换律、结合律和幂等律，从而保证最终一致性。介绍了格的概念，即数据结构状态构成偏序关系，从而实现仅在排序中“向上”移动的更新。CRDT 主要分为基于状态（CvRDT）和基于操作（CmRDT）两种类型，本指南主要关注基于状态的方法。

本文通过交互式演示，探讨了几种特定的 CRDT，包括：

*   **G-Counter：** 只增计数器，适用于仅递增的场景。
*   **PN-Counter：** 允许递增和递减，使用两个 G-Counter 实现。
*   **G-Set：** 只增集合，非常适合仅追加的集合。
*   **2P-Set：** 支持添加和删除，但一旦元素被删除，就无法重新添加。
*   **LWW-Element-Set：** 使用时间戳来解决添加和删除操作之间的冲突，从而可以重新添加元素。

对于每个 CRDT，本文解释了核心思想、实现细节、底层数学原理、权衡（优点和缺点）以及理想的用例。

---

## 9. WinApps: 像运行原生Linux应用一样运行Windows应用

**原文标题**: WinApps: Run Windows apps as if they were a part of the native Linux OS

**原文链接**: [https://github.com/winapps-org/winapps](https://github.com/winapps-org/winapps)

WinApps 让你能够在 Linux (KDE Plasma、GNOME、XFCE) 上无缝运行 Windows 应用程序，就像它们是原生应用一样。它通过在 Docker、Podman 或 libvirt 虚拟机中运行 Windows，并使用 FreeRDP 将应用程序与 Linux 应用一同渲染来实现这一点。

主要功能包括从 Windows 访问 Linux 的 /home 目录、使用 Nautilus 集成来通过 Windows 应用程序打开文件、用于管理 Windows 子系统的任务栏小部件，以及在 Windows 子系统中自动打开 Microsoft Office 链接。WinApps 支持几乎所有 Windows 应用程序，但依赖于内核级反作弊系统的应用除外。它使用经过社区测试的列表和注册表扫描自动检测已安装的应用程序，并在可用时提供高分辨率图标和 MIME 类型。

安装过程包括：1) 使用 Docker/Podman 或 libvirt 配置 Windows VM（推荐使用 Docker/Podman 以方便使用），2) 根据您的 Linux 发行版安装依赖项，3) 创建一个包含凭据和设置（如后端（Docker、Podman 或 libvirt）、IP 地址、缩放因子和 FreeRDP 标志）的配置文件（`~/.config/winapps/winapps.conf`），以及 4) 测试 FreeRDP 连接以确保正确配置和证书注册。强调了安全预防措施，例如限制对配置文件的访问和使用有效的 Windows 凭据。

---

## 10. 使用 Cricut 机器在家制作道路标志

**原文标题**: Building road signs at home using a Cricut Machine

**原文链接**: [https://annanay.dev/build-a-signboard/](https://annanay.dev/build-a-signboard/)

本文详细介绍了一个在家使用Cricut Maker 2制作标牌的DIY项目。作者受到TheSignGuy的启发，概述了制作过程和所需材料。

核心工具是Cricut Maker 2，用于根据使用Cricut软件创建的设计切割乙烯基材料。Cricut的尺寸及其底板（在本例中为1英尺 x 2英尺）限制了标牌的最大尺寸。该过程包括在切割前将乙烯基材料对齐并压在底板切割板上。

对于标牌的底板，作者使用了4x16铝板和12x12有机玻璃板。一个关键步骤涉及使用转移胶带将切割好的乙烯基材料从其塑料背衬转移到所选的底板材料上。

最初，作者在手动贴乙烯基材料时遇到了气泡问题。为了解决这个问题，他们投资了一台冷裱机，以确保将乙烯基材料压到基材上时获得光滑、无气泡的表面。文章最后提到了作者使用此方法制作的一些标牌。

---

## 11. WebR - 浏览器中的R

**原文标题**: WebR – R in the Browser

**原文链接**: [https://webr.sh/](https://webr.sh/)

WebR – 浏览器中的 R

文章“WebR – 浏览器中的 R”介绍了 webR，一个可以直接在网页浏览器中运行的 R 编程语言版本。主要内容是 webR 允许用户执行 R 代码，而无需服务器端的 R 安装或连接。文章强调需要 JavaScript 才能运行该应用程序。本质上，webR 将 R 强大的统计计算能力带到了客户端环境。

---

## 12. 大型人工智能会议充斥着AI撰写的同行评审。

**原文标题**: Major AI conference flooded with peer reviews written by AI

**原文链接**: [https://www.nature.com/articles/d41586-025-03506-6](https://www.nature.com/articles/d41586-025-03506-6)

机器学习国际会议（ICLR）2026面临危机：同行评审中AI使用泛滥。 学术界注意到评论中出现异常冗长和模糊的反馈，甚至出现捏造的引文，引发担忧。 AI 研究员 Graham Neubig 使用 Pangram Labs 的 AI 检测工具进行众包分析，结果显示，在提交的 75,800 份同行评审中，约 21% 是完全由 AI 生成的，超过一半显示出 AI 辅助的迹象。

分析还表明，在提交的 19,490 份稿件中，1% 完全由 AI 生成，9% 包含超过 50% 的 AI 生成文本。 这种对同行评审中涉嫌使用 AI 的确认，引起了研究人员的不满，因为它会对他们工作的评估产生负面影响。 一位研究人员发现，一份完全由 AI 生成的评论，对其论文的评分很低，几乎导致其论文被拒。

会议组织者现在正在实施自动化工具，以检测提交内容和评审中违反 AI 政策的行为。 这是 ICLR 首次如此大规模地遇到这个问题，他们旨在恢复对同行评审过程的信任。 该事件凸显了与 AI 在科学出版中的作用相关的日益增长的挑战和伦理考量。

---

## 13. 空中客车A320 – 强烈太阳辐射可能破坏飞行关键数据

**原文标题**: Airbus A320 – intense solar radiation may corrupt data critical for flight

**原文链接**: [https://www.airbus.com/en/newsroom/press-releases/2025-11-airbus-update-on-a320-family-precautionary-fleet-action](https://www.airbus.com/en/newsroom/press-releases/2025-11-airbus-update-on-a320-family-precautionary-fleet-action)

空客发现大量在役A320系列飞机存在潜在安全问题：强烈太阳辐射可能导致飞行控制数据损坏。在近期发生一起事故后，空客正采取积极措施降低风险。

该公司已发布警示运营商电报（AOT），要求运营商立即采取预防措施，实施软件和/或硬件保护。此AOT之后，欧洲联盟航空安全局（EASA）将发布紧急适航指令。

空客承认这些建议将对乘客和客户的运营造成中断，并对此造成的不便表示歉意。公司致力于与运营商紧密合作，确保机队飞行安全，并将安全置于首位。

---

## 14. Show HN: 探索浏览器暴露的关于你的信息

**原文标题**: Show HN: Explore what the browser exposes about you

**原文链接**: [https://neberej.github.io/exposedbydefault/](https://neberej.github.io/exposedbydefault/)

ExposedByDefault 是一个项目，旨在展示浏览器仅通过访问网页就能出人意料地泄露大量用户信息。它允许用户实时查看他们的浏览器在未经任何明确操作的情况下暴露的数据。这包括以下信息：

*   **基本浏览器和操作系统详情：** 所使用的浏览器和操作系统类型、版本号和设备详情。
*   **硬件信息：** CPU核心数、内存容量和其他硬件规格。
*   **网络信息：** IP地址、网络连接类型（例如，Wi-Fi、以太网），甚至可能包括位置信息。
*   **已安装字体：** 系统上安装的所有字体的列表。
*   **屏幕分辨率和颜色深度：** 屏幕分辨率、颜色深度和其他显示相关设置。
*   **已安装插件和扩展：** 关于浏览器插件和扩展的信息，这些信息可以揭示所使用的特定软件或服务。
*   **用户偏好：** 语言设置、时区和其他个性化偏好。

该项目突出了网站基于这些信息跟踪用户的可能性，即使没有cookies或其他传统跟踪方法。这可能导致浏览器指纹识别，这是一种基于用户特定浏览器配置来唯一识别用户的技术。该演示提醒人们与网络浏览相关的隐私风险，以及了解哪些信息正在自动共享的重要性。它隐式地鼓励用户考虑增强隐私的工具和浏览器配置。

---

## 15. 经营企业意味着接触现实

**原文标题**: Running a Business Means Contact with Reality

**原文链接**: [https://fredkozlowski.com/2025/11/02/running-a-business-means-contact-with-reality/](https://fredkozlowski.com/2025/11/02/running-a-business-means-contact-with-reality/)

无法访问文章链接。

---

## 16. 加菲尔德对勾股定理的证明

**原文标题**: Garfield's Proof of the Pythagorean Theorem

**原文链接**: [https://en.wikipedia.org/wiki/Garfield%27s_proof_of_the_Pythagorean_theorem](https://en.wikipedia.org/wiki/Garfield%27s_proof_of_the_Pythagorean_theorem)

加菲尔德对勾股定理的证明：美国总统的数学贡献

加菲尔德在1876年担任美国国会议员期间发表的勾股定理证明，是对著名定理的一种原创且“巧妙”的论证。加菲尔德后来成为美国第20任总统，也是唯一一位为数学贡献原创概念的总统。

该证明涉及用两个全等的直角三角形（ABC和BDE）和一个等腰直角三角形（ABD）构造一个梯形。这些三角形共享边a、b和斜边c。梯形ACED的面积随后以两种方式计算：首先，作为高乘以平行边的平均值，结果为1/2(a+b)(a+b)；其次，作为三个三角形面积的总和，结果为1/2(ab) + 1/2(c^2) + 1/2(ab)。

将梯形面积的这两个表达式相等：1/2(a+b)(a+b) = 1/2(ab) + 1/2(c^2) + 1/2(ab)。简化该方程即可得出勾股定理：a^2 + b^2 = c^2。该证明因其独创性而受到认可，并被收录在勾股定理证明的合集中。

---

## 17. Chainalysis成功破解门罗币匿名性

**原文标题**: Chainalysis Successful Deanonymization Attack on Monero

**原文链接**: [https://darkwebinformer.com/chainalysis-successful-deanonymization-attack-on-monero-2/](https://darkwebinformer.com/chainalysis-successful-deanonymization-attack-on-monero-2/)

据称Chainalysis成功破解Monero的匿名性：一种可能的攻击方式

该文章最初发布在Dread论坛上，详细描述了一种据称由Chainalysis对Monero发起的成功去匿名化攻击。作者称，Chainalysis在全球运行一个“有毒”的Monero节点网络，利用这些节点来去匿名化用户。这些节点可以提供有毒的RingCT诱饵，有效地将连接到这些用户的交易匿名性降低到1:1。

该攻击依赖于收集元数据（IP地址、时间戳、交易大小、费用）、联系ISP获取用户数据，并将区块链活动与现实世界身份联系起来。即使使用Tor或VPN，如果您的原始IP与您的真实身份相关联，也并非万无一失。然后，这些信息被用来将交易与中心化交易所联系起来，导致资金冻结和KYC请求。

文章的主要对策建议是**运行您自己的完整或修剪过的Monero节点**。 这将启用Dandelion++功能并防止有毒诱饵。 其他对策包括从未与您的真实身份相关联的位置使用Tor，使用DEX而不是CEX，正确地混合Monero，以及通常尽可能地混淆您的交易。 该文章强调了使用远程节点的危险，尤其是那些可能由Chainalysis等恶意行为者控制的节点。 最后，该文章提供了一个示例场景，说明了即使使用Tor，组合攻击如何能够去匿名化Monero用户。 作者敦促用户采取预防措施，并在需要时寻求帮助。

---

## 18. 使用URLPattern()构建你自己的路由器

**原文标题**: Build Your Own Router with URLPattern()

**原文链接**: [https://jschof.dev/posts/2025/11/build-your-own-router/](https://jschof.dev/posts/2025/11/build-your-own-router/)

本文阐述了如何使用新推出的`URLPattern()`浏览器 API 和原生 JavaScript 构建一个简单的单页应用 (SPA) 路由器。其核心思想是使用 `URLPattern()` 将浏览器 URL 与配置的一组路由进行匹配，并渲染相应的 Web 组件。

作者强调了 `URLPattern()` 在精确测试浏览器 URL 和捕获路由动态部分方面的重要性。路由器配置是一个对象数组，每个对象都将 URL 路由（使用 `URLPattern()`）与特定的 Web 组件相关联。路由器组件遍历这些配置，并将第一个匹配的组件渲染为子组件。

本文接着探讨了处理 SPA 导航的问题，包括服务器配置，以确保所有路径都提供索引 HTML 文件。它演示了如何拦截链接点击 (`preventDefault()`)，通过手动设置 URL 并使用 `window.pushState()` 更新浏览器历史记录来模拟页面转换。为此，设置了一个点击处理程序。

最后，本文介绍了通过监听 `popstate` 事件并根据更新后的 URL 渲染相应的组件来处理浏览器后退/前进按钮点击。StackBlitz 中提供了一个可用的示例。

本文最后讨论了构建自定义路由器时的安全注意事项（XSS 漏洞），强调了保持路由器配置私有以及避免仅根据查询参数或动态片段进行渲染的重要性。它还提出了 Web 组件是否是构建路由器的理想选择的问题。

---

## 19. 测试显示汽车玻璃破碎器无法击碎现代汽车玻璃

**原文标题**: Testing Shows Automotive Glassbreakers Can't Break Modern Automotive Glass

**原文链接**: [https://www.core77.com/posts/138925/Testing-Shows-Automotive-Glassbreakers-Cant-Break-Modern-Automotive-Glass](https://www.core77.com/posts/138925/Testing-Shows-Automotive-Glassbreakers-Cant-Break-Modern-Automotive-Glass)

Core77文章：现代车辆的车窗击破器是否有效？
该文章认为，价值5亿美元的汽车逃生工具市场是由恐惧驱动的，源于人们幻想在发生火灾或车辆落水的事故中需要这些工具。然而，这些情况在统计上非常罕见。

关键在于，由于“弹出缓解规则”，现代车辆越来越多地使用夹层玻璃作为侧窗，这使得专为钢化玻璃设计的传统车窗击破器失效。美国汽车协会（AAA）的研究证实，常见的车窗击破器对夹层玻璃无效。虽然并非所有汽车制造商都使用夹层玻璃（有些选择使用先进的侧面安全气囊），但讴歌、宝马、雪佛兰、福特、本田和丰田等主要品牌现在广泛使用夹层玻璃。

因此，车窗击破器主要只对使用钢化玻璃的旧款车辆有效。然而，安全带切割器对于需要快速解救昏迷事故受害者的急救人员仍然有用。文章总结说，虽然车窗击破器在很大程度上已不适用于现代汽车，但安全带切割器在特定的紧急救援情况下仍然具有价值。

---

## 20. 每个数学家只有几个诀窍 (2020)

**原文标题**: Every mathematician has only a few tricks (2020)

**原文链接**: [https://mathoverflow.net/questions/363119/every-mathematician-has-only-a-few-tricks](https://mathoverflow.net/questions/363119/every-mathematician-has-only-a-few-tricks)

这个MathOverflow帖子讨论了吉安-卡洛·罗塔的论断，即“每位数学家只有少数几个反复使用的技巧”。该问题征求这些常见数学技巧的例子。

许多回答建议的是核心原则，而非具体技术。这些包括：

*   改变求和/积分的顺序（富比尼定理的变体）。
*   简化或复杂化问题以使其可证明。
*   向问题添加参数以进行推广并找到解决方案。
*   使用三角不等式。
*   分部积分法。
*   将最大值/最小值与平均值相关联（鸽巢原理）。
*   采用概率方法（尝试随机对象/构造）。
*   使用莫比乌斯函数代替容斥原理。
*   使用连续性证明整数值函数的常数性。
*   在OEIS中查找序列。

一些评论表明，罗塔的观点可能是，每位数学家都会发展出一套他们深刻理解并反复应用的个性化技术，而不是所有人都知道的通用技巧。该帖子强调，即使是著名的数学家也可能依赖于一套有限的核心思想，并在各种问题中巧妙地应用它们。

---

## 21. Imgur对英国进行了地理封锁，所以我对我的网络进行了地理解锁。

**原文标题**: Imgur geo-blocked the UK, so I geo-unblocked my network

**原文链接**: [https://blog.tymscar.com/posts/imgurukproxy/](https://blog.tymscar.com/posts/imgurukproxy/)

奥斯卡·莫尔纳对Imgur封锁英国地区感到沮丧，导致嵌入式图片在整个互联网上无法访问（例如，Minecraft着色器预览）。他没有在单个设备上安装VPN并承受2.5 Gbps互联网连接的速度损失，而是实施了一个网络级解决方案。

他使用Pi-hole拦截对i.imgur.com的DNS请求，并将其路由到他的Traefik反向代理。Traefik将此流量定向到一个Gluetun容器，该容器建立一个VPN连接。在Gluetun的网络内部，一个Nginx容器充当一个简单的TCP代理，通过VPN隧道将请求传递到真正的i.imgur.com。然后，图像通过隧道返回到请求设备。

此设置只需要最少的Nginx配置即可进行带有SNI的TCP直通。Docker Compose管理Gluetun（用于VPN）和Nginx容器。Traefik配置为使用TCP路由和TLS直通来路由i.imgur.com流量。莫尔纳使用NixOS和Agenix来声明式地配置和管理系统，包括加密的VPN凭据。

结果是，他网络上的每个设备都可以访问Imgur图像，而无需单独的VPN或客户端配置。延迟影响很小，并且仅影响Imgur流量。他承认这种设置有些过度，但他欣赏它的简洁性、最少的维护以及最终能够看到那些Minecraft着色器的能力。

---

## 22. 软件开发者的自白：不再自我审查

**原文标题**: Confessions of a Software Developer: No More Self-Censorship

**原文链接**: [https://kerrick.blog/articles/2025/confessions-of-a-software-developer-no-more-self-censorship/](https://kerrick.blog/articles/2025/confessions-of-a-software-developer-no-more-self-censorship/)

软件开发者Kerrick Long解释了他近期停止更新博客的原因，坦承了导致他自我审查的恐惧。他现在计划更加透明地分享他的学习历程和职业经验。

他坦露了一些知识缺口：尽管有多年的面向对象编程经验，却对多态缺乏理解；由于缺乏使用而忘记了SQL技能；并且忽略了为大部分生产代码编写自动化测试（他现在认为这种做法在道德上是有问题的）。他还承认，在公司技术栈策略转变后，他放弃了学习Blazor。

Kerrick随后分享了个人的恐惧，包括因想编写更多Ruby代码而被雇主负面看待，以及在未经披露的情况下向开源项目贡献了AI辅助代码后受到网络骚扰。网络欺凌事件深深地影响了他，导致他害怕进一步的在线互动。

最后，他谈到了工作场所问题，反对自定义软件开发流程，赞成像Scrum或Kanban这样的成熟方法，并表达了他对在办公室工作的偏好，尽管他有一份远程工作。他担心承认自己的偏好可能会危及他目前和未来的工作。

现在他已经开始了，Kerrick计划在他的写作中更加开放，并鼓励读者通过Mastodon、RSS或电子邮件与他互动并订阅他的博客。

---

## 23. 安东尼·波登遗失的清单

**原文标题**: Anthony Bourdain's Lost Li.st's

**原文链接**: [https://bourdain.greg.technology/](https://bourdain.greg.technology/)

本文是已关闭的网站li.st上安东尼·布尔丹列表的部分存档，从互联网档案馆恢复而来。它汇编了布尔丹的各种观点和偏好，展示了他对不同主题的独特见解。

这些列表涵盖了广泛的范围，包括他最喜欢的80年代播放列表、唐纳德·特朗普图像的幽默标题以及“美食犯罪”，他在其中幽默地批评了诸如奶油面包汉堡和松露油等烹饪冒犯行为。

他还详细介绍了他在假想的纽约市场渴望的菜肴，重点介绍了来自他在新加坡、越南、香港和墨西哥旅行中的特定供应商。他的“电影中的食物”列表赞扬了那些准确描绘烹饪行业或美食乐趣的电影，例如《饮食男女》和《料理鼠王》。

其他列表探讨了潜在的乐队名称、完美的专辑、他认为可怕的事物（小丑、哑剧、瑞士）、超越原作的续集以及在河内与奥巴马总统共进晚餐的六个难忘的方面。他还分享了一个来自标准收藏的电影列表和他喜欢的网站。

最后，文章介绍了布尔丹关于“被低估的、无混蛋的目的地”的建议，倡导像乌拉圭、马赛、老挝、撒丁岛和贝鲁特这样的地方，赞扬它们的真实性、美食和缺乏主流旅游业。

---

## 24. 所以你想搭建一个本地RAG？

**原文标题**: So you wanna build a local RAG?

**原文链接**: [https://blog.yakkomajuri.com/blog/local-rag](https://blog.yakkomajuri.com/blog/local-rag)

本文详细介绍了作者使用Skald构建本地、完全开源的RAG（检索增强生成）系统的经验，重点关注数据隐私和自托管。作者概述了RAG系统的关键组件（向量数据库、嵌入模型、LLM、重排序器、文档解析），并为每个组件提供了开源替代方案。

作者的初始设置使用Postgres + pgvector作为向量数据库，Sentence Transformers用于嵌入，GPT-OSS 20B作为LLM，Sentence Transformers交叉编码器用于重排序，Docling用于文档解析。目标是创建一个功能完善且易于部署的系统，并计划进行广泛的基准测试以进一步优化。

随后，作者使用基于PostHog网站内容的自定义问答数据集，将此本地设置的性能与基于云的设置（Voyage AI嵌入和重排序器，Claude Sonnet LLM）进行了比较。云设置表现出色。本地设置虽然最初得分较低，但显示出潜力，尤其是在英语的点查询方面。切换到bge-m3和mmarco-mMiniLMv2-L12-H384-v1等多语言模型后，性能显着提高，但从多个文档中聚合信息仍然面临挑战。

文章总结说，构建本地RAG系统是可行且不断改进的，随着更好的开源模型出现，性能将会提高。作者鼓励大家参与和协作，以进一步开发和优化开源RAG解决方案，特别是对于那些具有严格数据隐私要求的组织。

---

## 25. 高空气污染或使运动益处减半——研究

**原文标题**: High air pollution could diminish exercise benefits by half – study

**原文链接**: [https://scienceclock.com/exercise-may-protect-less-when-air-pollution-is-high-study-finds/](https://scienceclock.com/exercise-may-protect-less-when-air-pollution-is-high-study-finds/)

研究表明：空气污染严重或使运动益处减半

---

## 26. 展示 HN: 我搭建了 Magiclip – 一体化 AI 工作室

**原文标题**: Show HN: I built Magiclip – an all-in-one AI studio

**原文链接**: [https://magiclip.io/](https://magiclip.io/)

Magiclip：一款由人工智能驱动的平台，旨在将现有视频内容转化为引人入胜的短视频，适用于 TikTok、Instagram Reels 和 YouTube Shorts 等平台。它简化了创作过程，声称用户只需点击两下即可创建病毒式短片。

主要功能包括：

*   **人工智能视频生成：** 使用 Veo 3 AI 通过文本提示创建专业外观的视频。
*   **自动剪辑和优化：** 将较长的视频（如 YouTube 视频）转换为更短、优化的片段，并自动添加字幕，旨在吸引社交媒体上的注意力。
*   **人工智能语音生成：** 将文本转换为逼真、自然的多种语言语音，用于旁白或解释。
*   **人工智能图像生成：** 通过文本描述创建独特的图像。
*   **分屏视频：** 允许添加游戏画面或动画背景。

Magiclip 提供分级定价方案（创作者、专家和专业人士），每个月在 AI 视频生成数量、图像积分和语音积分方面有不同的限制。 这些方案适用于不同的使用级别，从个人创作者到管理多个帐户的专业人士。 该平台还根据观看次数提供潜在收入估算，表明其关注货币化。

常见问题解答部分回答了有关功能、支持的格式、使用限制、语言可用性、社交媒体优化和订阅取消的常见问题。 Magiclip 旨在通过人工智能驱动的工具简化视频内容创作，这些工具通过字幕、效果和声音增强视频，使其适用于短视频平台。

---

## 27. Molly：一款改进的Signal应用

**原文标题**: Molly: An Improved Signal App

**原文链接**: [https://molly.im/](https://molly.im/)

Molly是一款增强型的、完全开源 (FOSS) 的安卓 Signal 应用替代品。它提供了改进的功能，专注于安全性、隐私和定制化。

主要改进包括：

*   **开源和加密：** 与 Signal 不同，Molly 完全开源，并使用密码保护加密数据库。
*   **多设备支持：** 用户可以将多个设备绑定到一个账户。
*   **定制化：** 提供 Material You 主题，可适应设备的配色方案。
*   **增强的隐私：** 集成 UnifiedPush 进行通知（避免使用 Google 服务），具有基于非活动状态的自动锁定功能，并通过 RAM 碎片安全地粉碎敏感数据。
*   **Tor 支持：** 允许通过 Orbot 集成 SOCKS 代理和 Tor，以提高匿名性。

文章鼓励用户从 GitHub 下载 Molly，并提供捐赠选项。文章还表明，未来计划进行更多改进。

---

## 28. DMT诱导的临界性转变与自我溶解相关

**原文标题**: DMT-induced shifts in criticality correlate with self-dissolution

**原文链接**: [https://www.jneurosci.org/content/early/2025/10/24/JNEUROSCI.0344-25.2025](https://www.jneurosci.org/content/early/2025/10/24/JNEUROSCI.0344-25.2025)

这篇2025年《神经科学杂志》的文章“DMT诱导的临界性转变与自我消解相关”研究了迷幻物质DMT如何影响人类的大脑动力学和主观体验。研究人员侧重于“临界性”这一概念，这是一种大脑振荡在不同尺度上表现出波动的状态，被认为对健康的大脑功能至关重要。

该研究发现，DMT使大脑振荡偏离临界性，特别是在α波和相邻的频段。这种转变的特征是脑活动中的熵（无序）增加和复杂性降低。重要的是，α波和θ波频段中这种临界性转变的程度与自我消解的强度相关，自我消解是迷幻体验的一个常见特征。此外，该研究表明，DMT诱导的转变将大脑振荡推向亚临界状态，意味着较低的兴奋性状态。

本质上，这项研究表明，DMT改变了大脑动力学，特别是使大脑振荡偏离临界状态，这与自我消解的主观体验有关。这些发现有助于理解迷幻剂诱导的意识改变状态背后的神经机制以及临界性在大脑功能中的作用。这项研究获得了多个组织的资助，并包含一位作者的潜在利益冲突声明。

---

## 29. 临床实践中整数和锐性阈值的风险

**原文标题**: The risk of round numbers and sharp thresholds in clinical practice

**原文链接**: [https://www.nature.com/articles/s41746-025-02079-y](https://www.nature.com/articles/s41746-025-02079-y)

本文探讨了在临床实践中普遍存在的采用整数阈值进行决策的方法，指出这种简化方式虽然方便，但可能会扭曲风险评估，并对患者的治疗结果产生负面影响。作者证明，即使在医学进步的情况下，这些阈值也可能导致死亡风险出现不连续性和反因果悖论等异常现象。

该研究使用一种可解释的机器学习模型来识别真实世界数据、模拟和纵向研究中由阈值引起的这些人为偏差。研究强调，基于错位的整数阈值做出的治疗决策可能因治疗不足或过度治疗而导致额外的风险。该研究展示了肺炎患者和MIMIC-IV数据集中的案例，其中血清肌酐和血尿素氮水平揭示了与APACHE II等预测模型不同的惊人风险模式。

作者将这些异常现象分为不连续性（阈值附近风险的突然变化）和反因果非单调性（即治疗反而能改善高风险患者的治疗结果）。他们提出了一种“玻璃盒”机器学习方法，以系统地识别这些人为偏差，并建议持续重新评估临床协议，使阈值与风险的连续性相一致，尤其是在重症监护环境中，从而改善患者的治疗结果。该研究强调了人工智能驱动的协议可能会被这些扭曲的风险曲线所误导，突出了对细致风险评估方法的需求。

---

## 30. 泄露证实OpenAI正准备在ChatGPT上推出广告

**原文标题**: Leak confirms OpenAI is preparing ads on ChatGPT for public roll out

**原文链接**: [https://www.bleepingcomputer.com/news/artificial-intelligence/leak-confirms-openai-is-preparing-ads-on-chatgpt-for-public-roll-out/](https://www.bleepingcomputer.com/news/artificial-intelligence/leak-confirms-openai-is-preparing-ads-on-chatgpt-for-public-roll-out/)

泄露的ChatGPT安卓应用测试版暗示OpenAI计划引入广告，可能颠覆当前的网页广告模式。X用户Tibor发现，该泄露版本在代码中引用了“广告功能”、“集市内容”、“搜索广告”和“搜索广告轮播”。

此举标志着ChatGPT从当前无广告体验的转变，效仿了谷歌的搜索引擎模式，引入赞助商结果。文章认为，ChatGPT庞大的用户数据能够实现高度个性化和有效的广告投放，可能超越谷歌的能力。最初，广告预计仅限于ChatGPT内部的搜索体验。

文章强调了ChatGPT令人印象深刻的用户增长，引用了每周8亿用户和每天处理25亿条提示。印度现在是最大的用户群体，超过了美国。如此庞大的用户基础为成功的广告实施奠定了坚实的基础。

文章还包含一个“2026年CISO预算基准”报告的推广部分，并链接到有关OpenAI未来计划和产品发布的文章。

---

## 31. 内角和为零的三角形

**原文标题**: A triangle whose interior angles sum to zero

**原文链接**: [https://www.johndcook.com/blog/2025/11/28/tricusp-triangle/](https://www.johndcook.com/blog/2025/11/28/tricusp-triangle/)

本文探讨了球面几何和双曲几何中三角形内角和与欧几里得几何的不同之处。在球面几何中，三角形内角和总是*大于*π弧度（180度），三角形的面积与超过π的盈余直接相关。在双曲几何中，内角和总是*小于*π，三角形的面积与“亏损”有关，即π与角和之间的差值。

文章强调，虽然两种几何中的小三角形都接近欧几里得几何行为（角和接近π），但较大的三角形可能出现显著差异。在双曲几何中，角和可以接近于零。这引出了一个有趣的“三角形”概念，其角和为0，面积为π。尽管从技术上讲，它是一个“不规则三角形”，因为它的顶点位于双曲平面（由半圆定义）上的无穷远处（实轴上的理想点），但文章解释说，平面内可以存在角和任意接近于零的三角形。至关重要的是，文章指出，形成该三角形的半圆的具体半径并不影响其面积，这突出了双曲几何的独特属性。最后，文章指出，这种“零角”三角形具有无限的周长，但面积有限（π）。

---

## 32. 语言主要是一种交流工具，而非思考工具 (2024) [pdf]

**原文标题**: Language is primarily a tool for communication rather than thought (2024) [pdf]

**原文链接**: [https://gwern.net/doc/psychology/linguistics/2024-fedorenko.pdf](https://gwern.net/doc/psychology/linguistics/2024-fedorenko.pdf)

无法总结该文章。

（提供的文本是PDF文件的内部代码，而非文章的实际内容。它包含PDF语法、压缩数据流以及定义文档结构和外观的其他技术元素。它不是可供处理以理解文章主题的人类可读文本。）

---

## 33. Airloom – 3D 飞行追踪器

**原文标题**: Airloom – 3D Flight Tracker

**原文链接**: [https://objectiveunclear.com/airloom.html](https://objectiveunclear.com/airloom.html)

Airloom是一款3D飞行追踪应用程序，可在三维空间中可视化飞行路径。初始化后，它提供一系列功能供用户探索和分析飞行数据。用户可以通过机场搜索航班，利用当前位置或指定搜索半径。还提供航班/飞机搜索功能。

该应用程序提供可自定义的显示设置，包括轨迹长度、线条粗细、按速度进行颜色编码以及机场/城市标签。用户可以选择不同的地图图层，包括深色主题、卫星图像和线框视图。还支持空域可视化，允许用户查看B、C和D类空域，并具有可调节的不透明度和过滤选项。

数据设置包括可调节的更新速率和基于呼号、飞机类型和高度的过滤器。录制和回放功能允许用户捕获飞行数据并以不同速度回放。高级设置可自定义高度比例、地面高度、雾距离、坐标轴显示和地图亮度。此外，用户可以使用WASD键和鼠标在“飞行模式”中控制他们的视点进行导航。包括重置视图、清除飞行轨迹和调整自动旋转的控件，以及飞行跟随和“冲浪模式”（根据点击自动切换航班）的功能。最后，还有共享选项可以共享当前视图或加入邮件列表以获取更新。

---

## 34. ABC语言，Python的前身 (1991)

**原文标题**: The original ABC language, Python's predecessor (1991)

**原文链接**: [https://github.com/gvanrossum/abc-unix](https://github.com/gvanrossum/abc-unix)

本文档描述了最初的ABC编程语言，它是Python的前身，大约在1983年至1986年间由CWI（荷兰数学与计算机科学研究中心）开发。Python的创建者Guido van Rossum在此期间参与了ABC的开发。从cwi.nl下载的源代码，其修改日期主要为1991年，少数为1996年或2021年，也可在Luciano Ramalho的GitHub上找到。Van Rossum希望比较和统一这些版本。

目前，该代码假定为32位系统；计划升级以支持64位系统。尽管CWI从未正式授权ABC，但他们保留版权。Van Rossum打算与Steven Pemberton协商一个宽松的许可协议，理想情况下是MIT许可。

ABC的作者包括Eddy Boeve、Frank van Dijk、Leo Geurts、Timo Krijnen、Lambert Meertens、Steven Pemberton和Guido van Rossum。本文档还提供了参考文献，包括《ABC程序员手册》以及Pemberton和Meertens的文章，阐明了该语言及其对Python的影响。此外，还包括Steven Pemberton的主页链接和Lambert Meertens关于Python起源的文章。

---

## 35. 2800万 Hacker News 评论向量嵌入搜索数据集

**原文标题**: 28M Hacker News comments as vector embedding search dataset

**原文链接**: [https://clickhouse.com/docs/getting-started/example-datasets/hackernews-vector-search-dataset](https://clickhouse.com/docs/getting-started/example-datasets/hackernews-vector-search-dataset)

本文档描述了如何使用包含 2874 万篇帖子及其向量嵌入的 Hacker News 数据集，利用 ClickHouse 构建大规模向量搜索应用程序。这些嵌入是使用 SentenceTransformers 模型 all-MiniLM-L6-v2 生成的。步骤包括：创建 ClickHouse 表来存储数据，从 S3 存储桶中的 Parquet 文件加载数据，使用 `vector_similarity` 函数构建向量相似度索引，以及使用余弦距离执行近似最近邻 (ANN) 搜索。

本文档还提供了一个 Python 脚本，该脚本使用 Sentence Transformers 为搜索查询生成嵌入，然后用于搜索 Hacker News 数据。它提供了一个如何运行脚本的示例，并展示了示例结果。

最后，介绍了一个摘要应用程序。它以一个主题作为输入，生成其嵌入，通过向量搜索检索相关的 Hacker News 帖子/评论，然后使用 LangChain 和 OpenAI gpt-3.5-turbo Chat API 来总结检索到的内容。摘要是通过将检索到的帖子/评论作为上下文传递给 Chat API 来生成的。包含了摘要应用程序的代码，演示了一个基本的生成式 AI 用例，以及一个用例示例。

---

## 36. 用户强烈抵制微软 Edge 和 Windows 11 中的“工作版 Copilot”

**原文标题**: Users brutually reject Microsoft's "Copilot for work" in Edge and Windows 11

**原文链接**: [https://www.windowslatest.com/2025/11/28/you-heard-wrong-users-brutually-reject-microsofts-copilot-for-work-in-edge-and-windows-11/](https://www.windowslatest.com/2025/11/28/you-heard-wrong-users-brutually-reject-microsofts-copilot-for-work-in-edge-and-windows-11/)

微软因其在Edge和Windows 11中激进整合“工作助手”人工智能功能而面临Windows用户的强烈反对。用户抗议这种被认为是强行实施人工智能的行为，特别是“助手模式”，该模式旨在自动化任务，但被视为不受欢迎且不必要的。

文章强调了用户在社交媒体上表达的沮丧情绪，许多人表示他们从未要求这些人工智能功能，并且正在积极寻找删除它们的方法。批评的焦点在于人们感觉微软脱离了用户需求，不顾广泛的反对意见而强行推进人工智能整合。虽然微软有选择性地回应积极反馈，但它在很大程度上忽略了负面评论。

人们还对这些人工智能代理的准确性和可靠性提出了担忧，IT专业人士质疑它们在专业环境中的价值。用户对助手准确执行复杂任务的能力表示怀疑，并指出了人工智能“幻觉”的风险。

文章还提到了微软过去整合人工智能的尝试，包括迫使一位Windows主管锁定社交媒体回复并承诺倾听反馈的强烈反对。尽管如此，该公司仍在继续推动人工智能整合，甚至在Windows 11任务栏中展示人工智能代理。文章将这种推动与微软承认需要改进Windows 11的可靠性和设计一致性形成对比，进一步加剧了用户的怀疑情绪。

---

## 37. Django 新后台任务初探

**原文标题**: A first look at Django's new background tasks

**原文链接**: [https://roam.be/notes/2025/a-first-look-at-djangos-new-background-tasks/](https://roam.be/notes/2025/a-first-look-at-djangos-new-background-tasks/)

本文介绍了 Django 6.0 新增的内置后台任务框架 `django.tasks`。 虽然其目的不是为了取代像 Celery 这样的成熟解决方案，但它为任务队列实现提供了一个通用的 API。 核心思想是使用 Django 的标准 API 定义任务，使其与后端无关。

作者通过创建一个使用 ntfy.sh 的通知应用来说明了这一点，重点介绍了使用 `@task` 装饰器定义任务以及使用 `enqueue` 方法将其加入队列的过程。 一个主要的限制是缺少内置的 worker；执行需要外部基础设施。 Django 6.0 仅提供 `ImmediateBackend` 和 `DummyBackend` 用于立即执行或不执行。

文章随后详细介绍了如何构建一个自定义的、基于数据库的任务后端和 worker。 它涵盖了必要的数据库模型（`Task`、`Attempt`、`Error`）来存储任务信息、尝试次数和错误。 该模型设计强调 worker 快速检索、声明和处理任务。 主要功能包括用于任务调度的 `available_after` 和用于管理重试的 `attempt_count`。

文章还解释了指定最大尝试次数和退避因子的配置选项。 进一步阐述了负责任务检索和入队的 `QueueStore` 类，以及负责声明和处理任务的 `Worker` 类。

---

## 38. 基于Yggdrasil网络的真P2P邮件

**原文标题**: True P2P Email on Top of Yggdrasil Network

**原文链接**: [https://github.com/JB-SelfCompany/Tyr](https://github.com/JB-SelfCompany/Tyr)

Tyr 是一款安卓平台的点对点邮件系统，利用 Yggdrasil 网络提供真正去中心化和私密的邮件体验。与传统邮件不同，Tyr 不依赖中心化的邮件服务器，而是提供直接的 P2P 连接、内置的网络加密以及通过 Yggdrasil 实现自动 NAT 穿透。

主要功能包括与 DeltaChat/ArcaneChat 的无缝集成以实现 P2P 消息体验、设备上运行的本地 SMTP/IMAP 服务器、通过 Ed25519 密钥进行加密身份验证、自动启动以保证持续可用性以及加密备份。

Tyr 的工作原理是在 Android 应用中嵌入一个 Yggmail 服务器（用 Go 编写），在 localhost 上提供标准的 SMTP/IMAP 协议。它使用从您的公钥派生的加密密钥作为您的电子邮件地址，从而确保可验证的身份。

设置 Tyr 涉及安装应用程序、配置 Yggdrasil 对等节点，然后设置 DeltaChat/ArcaneChat 以连接到本地 SMTP/IMAP 服务器。

安全功能包括使用 AES-256-GCM 的 Android Keystore 加密、自动密钥库恢复、Yggdrasil 网络加密、本地专用端口访问、加密身份以及加密备份。

Tyr 旨在提供抗审查、私密和去中心化的邮件通信，将控制权交还给用户。该项目是开源的，并鼓励贡献。

---

## 39. 鸽巢原理的盛名之累 (1991)

**原文标题**: The undeserved status of the pigeon-hole principle (1991)

**原文链接**: [https://www.cs.utexas.edu/~EWD/transcriptions/EWD10xx/EWD1094.html](https://www.cs.utexas.edu/~EWD/transcriptions/EWD10xx/EWD1094.html)

本文批判了“鸽巢原理”(PHP)，认为其传统表述过于具体，且笼罩着不必要的神秘感。作者认为，PHP通常使用的“物体”和“盒子”这种措辞笨拙，掩盖了其根本的算术性质。这种措辞引入了无关的“噪音”，例如需要可视化“分配”和“接收”，并诱导产生误导性的可视化（过度拥挤与未充分利用的盒子），从而掩盖了等价的表述。

相反，作者提出了一个更简单、更通用的替代方案：“对于一个非空的有限实数集合，最大值至少是平均值（且最小值至多是平均值）。” 这种表述消除了对隐喻的需求，突出了该原理的核心算术本质。

作者认为，传统的PHP是这一广义原理的弱化版本。为了证明这一点，他们提出了“德国足球彩票问题”，该问题需要更强大的广义原理才能得到直接的解决方案。通过鸽巢原理获得的该问题看似令人惊讶的解决方案，归因于问题参数中幸运的算术巧合（5是大于等于13/3的最小整数）。作者得出结论，用PHP轻松解决这个问题是一种运气，而需要稍大数值的问题则更具挑战性。本质上，作者主张对PHP进行去神秘化和重新表述，倡导将其视为平均值和极值之间简单的算术关系，而不是一种复杂而巧妙的工具。

---

## 40. Show HN: Mu – 微型网络

**原文标题**: Show HN: Mu – The Micro Network

**原文链接**: [https://github.com/asim/mu](https://github.com/asim/mu)

Mu：微型网络 是一个旨在重建在线服务的新项目，摆脱了大型科技公司令人上瘾的算法、广告和剥削性做法。它是一个基于会员制的网络，旨在实现可持续发展和以用户为中心，提供无广告和无算法的体验。订阅者可以获得功能、支持，并直接参与平台的开发。

目前，Mu提供基本的API、PWA、LLM驱动的聊天UI、RSS新闻源、YouTube搜索和微型博客功能。未来的计划包括私人电子邮件、用于平台积分的钱包、二维码扫描仪等实用工具以及服务市场。

该项目旨在通过每月固定的订阅费来支持，旨在维持开发，而不是追加销售功能。用户可以在mu.xyz免费试用Mu。

对于开发者来说，该项目是开源的，并使用Go构建。要本地运行Mu，您需要安装Go，克隆Mu存储库并通过`go install`安装，并将YouTube Data和Fanar（用于LLM查询）的API密钥设置为环境变量。然后可以使用`mu --serve`启动应用程序，并通过localhost:8081访问。

---

## 41. Electron与Tauri

**原文标题**: Electron vs. Tauri

**原文链接**: [https://www.dolthub.com/blog/2025-11-13-electron-vs-tauri/](https://www.dolthub.com/blog/2025-11-13-electron-vs-tauri/)

本文以 Dolt Workbench 为例，比较了 Electron 和 Tauri 这两个使用 Web 技术构建桌面应用程序的框架。作者强调了 Electron 的流行性及其与现有 Web 项目（例如使用 Next.js 的项目）轻松集成的特点，尤其是借助 Nextron 等工具。然而，Electron 因捆绑完整的 Chromium 浏览器引擎而存在严重的臃肿问题。

Tauri 是一个较新的框架，通过利用系统的原生 Webview 而不是捆绑浏览器引擎来解决臃肿问题。虽然这会引入潜在的兼容性问题，但作者发现这些问题很小。Tauri 还使用 Rust 作为主应用程序进程，这对 Web 开发人员来说可能不太容易上手，但与 Electron 基于 Node.js 的方法相比，它提供了更自然的 API。然而，Electron 简化了辅助进程的使用，因为它附带了 Node.js 运行时，而 Tauri 需要将 Node.js 应用程序编译为单独的二进制文件。

尽管 Tauri 在大小和 API 方面具有优势，但由于 Windows 捆绑支持（.appx 和 .msix）的限制以及 macOS 通用二进制文件的问题，作者暂缓全面迁移。作者总结说，Tauri 是 Electron 的一个很有前途的替代方案，它提供了一种更轻量级的解决方案，可以与现有代码库很好地集成，但一些实际问题需要首先解决。

---

## 42. 我用数学证明了“猜猜我是谁？”的最佳策略 [视频]

**原文标题**: I mathematically proved the best "Guess Who?" strategy [video]

**原文链接**: [https://www.youtube.com/watch?v=_3RNB8eOSx0](https://www.youtube.com/watch?v=_3RNB8eOSx0)

这个YouTube视频，标题为“我用数学证明了最佳的‘猜猜我是谁？’策略”，很可能深入探讨了一种数据驱动的方法，以优化棋盘游戏“猜猜我是谁？”的策略。 该标题表明创作者使用了数学原理来确定最有效的提问方式，从而缩小潜在角色范围并最终赢得游戏。

然而，“内容”部分只是YouTube的页脚信息，其中包含指向版权声明、联系信息、广告、开发者资源、服务条款、隐私政策、安全、YouTube运作方式、测试版功能和NFL Sunday Ticket等内容的链接。

因此，提供的内容实际上并未总结*视频*的内容。 相反，它是YouTube政策和功能的样板列表。 **在没有更多信息的情况下，无法准确概括视频对“猜猜我是谁？”策略的数学分析。**

---

## 43. 别拽那个，你永远不知道它连着什么 (2016)

**原文标题**: Don't tug on that, you never know what it might be attached to (2016)

**原文链接**: [https://blog.plover.com/2016/07/01/#tmpdir](https://blog.plover.com/2016/07/01/#tmpdir)

Mark Dominus 讲述了追踪一个令人沮丧的 bug 的过程，该 bug 涉及 Emacs、emacsclient 和 TMPDIR 环境变量。他使用一个名为 `also` 的 shell 脚本（依赖 `emacsclient` 在 Emacs 中打开文件）的工作流突然中断，`emacsclient` 无法找到服务器套接字。

调查显示，`emacsclient` 在 `/mnt/tmp/emacs2017/server` 中寻找套接字，而 Emacs 在 `/tmp/emacs2017/server` 中创建它。差异源于 `TMPDIR` 环境变量被设置为 `/mnt/tmp`。

Dominus 随后发现，当直接查询时，Emacs 本身正确识别了 `TMPDIR` 变量，这使他怀疑 Emacs 和 `emacsclient` 之间的环境存在差异。他将问题追溯到一个 Git 工作流中使用的 Perl 程序 (`git-re-edit`)，该程序以某种方式在调用 Emacs 之前取消设置了 `TMPDIR` 变量。进一步调查显示，Perl 本身是罪魁祸首，奇怪的是，仅针对 `TMPDIR` 变量。

Dominus 实现了两个解决方法：配置 Emacs 使用 TCP 套接字而不是 Unix 域套接字，以及通过自定义的 `EMACS_SERVER_SOCKET` 环境变量手动将正确的套接字路径传递给 `emacsclient`。

在 Perl 社区其他人的帮助下，发现的根本原因是安全措施。为了防止具有提升权限的程序被诱骗将临时文件写入不安全的位置，某些 Perl 安装中的动态加载器将在加载程序时取消设置 TMPDIR。

---

## 44. 布料项目

**原文标题**: Fabric Project

**原文链接**: [https://github.com/Fabric-Project/Fabric](https://github.com/Fabric-Project/Fabric)

Fabric：一个用于交互式视觉效果、图像和视频处理、3D内容创作以及使用现代技术进行高保真渲染的创意编码环境和快速原型工具。受Quartz Composer启发，它提供了一个可视化的基于节点的界面、通过插件进行自定义节点创建的SDK支持，以及加载通用交换文件格式的能力。

Fabric旨在成为一个对初学者友好的创意编码工具，同时也是一个创建可重用视觉资源（可嵌入第三方应用程序）的专业环境。它利用Satin 3D引擎和Lygia着色器库进行基于物理的渲染、场景图管理、实时着色器编辑、GPU计算、基于图像的光照、3D模型加载和材质系统。

主要功能包括创作交互式3D图形、图像处理和特效、音频响应场景以及图像/视频分析管道。 Fabric支持诸如基于ML的实时分割和关键点检测、基于着色器的图像处理以及本地LLM调用等技术。

目前正在大力开发中，需要macOS 14+和Xcode 15+，Fabric是一个使用Swift、SwiftUI和C++构建的Apple平台专用工具。 创作者Anton Marini希望建立一个让人想起Quartz Composer时代的开发者社区。 目标是提供符合其设计理念的用户体验，并提供所需的抽象级别，使其与其他基于节点的工具区分开来。

---

## 45. 比利时警方被曝利用僵尸网络操纵欧盟数据法影响评估

**原文标题**: Belgian Police exposed using botnets to manipulate EU data law impact assessment

**原文链接**: [https://old.reddit.com/r/europe/comments/1p9kxhm/belgian_federal_police_forgot_to_turn_their_vpn/](https://old.reddit.com/r/europe/comments/1p9kxhm/belgian_federal_police_forgot_to_turn_their_vpn/)

无法访问文章链接。

---

## 46. 工作时无法集中注意力的数学原理

**原文标题**: The Math of Why You Can't Focus at Work

**原文链接**: [https://justoffbyone.com/posts/math-of-why-you-cant-focus-at-work/](https://justoffbyone.com/posts/math-of-why-you-cant-focus-at-work/)

工作难以集中注意力的数学原理：中断与恢复时间

本文探讨了工作时难以集中注意力的数学原理，将其归因于中断和恢复时间。文章认为，通过Slack、Teams等工具进行的持续连接，以及即时响应的文化，加剧了这个问题。

作者使用了一个包含三个关键参数的数学模型：λ (lambda)，每小时的中断率；Δ (delta)，中断后的恢复时间（分钟）；以及θ (theta)，进行有意义工作所需的最小不间断时间。文章将工作日可视化为时间线，用绿色表示专注时间段，红色表示中断，灰色表示恢复时间。

文章引入了“产能”的概念，量化了基于这三个参数所实现的生产性工作量。它展示了即使总专注时间相同，改变这些参数也可能对产能产生巨大影响。模拟100个工作日在不同条件下的情况，突出了高中断率和长恢复时间如何导致生产力低下，专注时间段短的工作日。

最后，文章引用了关于真实工作中断频率和恢复时间的研究，指出员工经常每隔几分钟就被打断一次，并且需要大量时间才能重新集中注意力。作者认为，理解和建模这些参数可以帮助个人和组织解决注意力碎片化的问题。

---

## 47. Show HN: 自选冒险式演示

**原文标题**: Show HN: Choose your own adventure style Presentation

**原文链接**: [https://github.com/Skarlso/adventure-voter](https://github.com/Skarlso/adventure-voter)

冒险投票者是一个互动演示系统，它将传统幻灯片演示转变为“选择你自己的冒险”体验。演示者将他们的内容编写为带有决策点的 Markdown 文件。在演示过程中，观众通过手机上的 WebSocket 进行投票，实时影响演示的路径。

该系统由用于处理 WebSocket 连接和投票聚合的 Go 后端以及用于用户界面的 Alpine.js 前端组成。演示者拥有一个专用视图来控制演示，而观众则使用单独的 URL（投票者视图）来参与。

要使用冒险投票者，你可以使用 Docker Compose 或从源代码构建。演示逻辑定义在一个 `story.yaml` 文件中，该文件将包含内容和决策点的 Markdown 文件链接在一起。决策点包括计时器和一组带有标签和相应“下一章”ID 的选项。

该系统被设计为部署在反向代理（如 Nginx 或 Traefik）之后，并提供可选的演示者身份验证，以防止未经授权的控制。 虽然功能齐全，但该工具目前处于 Alpha 阶段，可能包含错误。 它包括基本安全功能，如线程安全状态管理和文件路径清理，但不适用于关键任务应用程序。 通过命令行标志进行配置，以设置服务器地址、内容和故事路径以及演示者密钥。

---

## 48. 门罗币中的隐形地址如何运作

**原文标题**: How stealth addresses work in Monero

**原文链接**: [https://www.johndcook.com/blog/2025/11/24/monero-stealth-addresses/](https://www.johndcook.com/blog/2025/11/24/monero-stealth-addresses/)

门罗币如何使用隐匿地址确保交易隐私
此文阐述了门罗币如何使用隐匿地址来确保交易隐私。餐厅老板Alice展示她的公钥查看密钥（A）和公钥消费密钥（S）。当Bob想付款时，他的软件会生成一个随机数（r）并计算R = rG。它还会计算k = H(rA)，其中H是一个哈希函数。隐匿地址P随后被计算为P = kG + S，Bob将(P, R)发送给Alice。

Alice可以计算k，因为她知道她的私钥查看密钥（a），且A = aG。她计算aR，这等于rA。然后Alice和Bob都对aR（或rA）进行哈希运算以获得k，使用椭圆曲线迪菲-赫尔曼密钥交换。Alice扫描区块链，查找支付给P的款项。

关键点在于P在区块链上，但只有Alice和Bob知道k。因为只有Alice知道她的私钥消费密钥（s），她可以推导出对应于P的私钥，即(k + s)，从而允许她花费这笔钱。即使Bob将钱发送到P，门罗币的环签名也会混淆发送者在一组可能性中。本质上，隐匿地址确保每笔交易都发送到一个唯一、不可追踪的地址，从而增强了隐私，因为只有发送者和接收者可以将交易与他们联系起来。反向计算椭圆曲线乘法的困难性阻止了Alice的私钥查看密钥被确定。

---

## 49. 大型公司里的优秀工程师如何编写糟糕的代码

**原文标题**: How good engineers write bad code at big companies

**原文链接**: [https://www.seangoedecke.com/bad-code-at-big-companies/](https://www.seangoedecke.com/bad-code-at-big-companies/)

大型科技公司中令人惊讶的糟糕代码，并非源于工程师能力不足，而是高员工流动率和频繁重组所导致的系统性问题。这导致工程师经常在不熟悉的代码库中工作，使其大部分时间实际上都像“新手”。

虽然有经验丰富的“老手”负责代码审查，但他们往往负担过重，并且缺乏正式机制来保留或有效利用他们的专业知识。文章认为，公司优先考虑内部“易读性”（便于重新分配工程师），而不是长期的代码质量。这是一种有意的权衡，接受一定程度的糟糕代码，以换取将工程师快速部署到新问题的能力。

作者区分了“纯粹”的工程（独立的、技术性项目）和“不纯粹”的工程（在不熟悉的系统中，以截止日期为导向的工作），认为大型科技公司的工程师常常被迫从事后者，这使得犯错不可避免。

个人工程师改变这种动态的力量有限。成为“老手”会有所帮助，但即使如此，改进代码质量的努力也可能充满挑战。文章总结说，指出糟糕的代码有助于修复具体问题，但主要责任在于迫使工程师在不熟悉的环境中工作的系统性问题。

---

## 50. GitLab 发现大规模 NPM 供应链攻击

**原文标题**: GitLab discovers widespread NPM supply chain attack

**原文链接**: [https://about.gitlab.com/blog/gitlab-discovers-widespread-npm-supply-chain-attack/](https://about.gitlab.com/blog/gitlab-discovers-widespread-npm-supply-chain-attack/)

GitLab发现大规模NPM供应链攻击，涉及“沙丘蠕虫”恶意软件的进化版本，该恶意软件具有蠕虫式传播和破坏性的“死者开关”。该恶意软件感染NPM包，从GitHub、npm、AWS、GCP和Azure收集凭据，将数据泄露到攻击者控制的GitHub存储库，并自动感染其他包。

感染过程涉及一个多阶段加载器，最初看似无害，但会执行一个高度混淆的有效载荷`bun_environment.js`。被盗的GitHub令牌用于创建公开存储库以进行数据泄露，并且关键的是，用于在受感染系统之间共享访问令牌，从而形成一个有弹性的僵尸网络。该恶意软件通过将恶意代码注入受害者的包并将其重新发布到npm上来传播。

如果无法访问GitHub（数据泄露）和npm（传播），“死者开关”会触发受感染系统上的数据销毁，如果尝试进行删除，可能会导致大范围的数据丢失。

GitLab建议使用依赖项扫描和GitLab Duo Chat来检测恶意软件。主要入侵指标包括`bun_environment.js`文件、`.truffler-cache/`目录以及特定的命令，如`shred -uvz -n 1`。GitLab的系统正在监控新的感染，该公司分享了其发现，以帮助社区有效应对。攻击的“死者开关”需要谨慎的补救策略，以避免触发数据销毁。

---

## 51. 在我自制的业余操作系统上的C++ Web服务器

**原文标题**: C++ Web Server on my custom hobby OS

**原文链接**: [https://oshub.org/projects/retros-32/posts/getting-a-webserver-running](https://oshub.org/projects/retros-32/posts/getting-a-webserver-running)

作者详述了在自制 Hobby 操作系统 RetrOS-32 上构建 Web 服务器的历程。中断一段时间后，作者重新开始解决网络难题，特别是 TCP 和 HTTP 方面的问题。最初的障碍包括终端缓冲区损坏以及 E1000 网络驱动程序对传入数据包处理不正确，这两个问题最终都得到了解决。

由于未处理的 RST 数据包导致 TCP 出现性能问题，通过解决这些问题提高了在高负载浏览器刷新下的稳定性。随后，作者开发了一个自定义的 HTTP 引擎，利用了之前项目 (c-web-modules) 中的解析器。 之后开发了一个专注于路由的 Web 引擎，能够定义路由、HTTP 方法和处理函数（lambda 表达式）。

Web 服务器的实现涉及使用 `HTTPEngine` 和 `FileRepository` 的 `WebEngine`。 `FileRepository` 实现了静态文件的缓存服务。文章提供了代码片段，演示了从操作系统文件系统中进行路由和提供文件。作者最后概述了未来的步骤，包括更高级的 Web 服务器 UI、优雅的关闭功能，以及最终为操作系统构建 Web 浏览器。该项目的完整源代码可在 Github 上找到。

---

## 52. JSON Schema 解密：方言、词汇表和元模式

**原文标题**: JSON Schema Demystified: Dialects, Vocabularies and Metaschemas

**原文链接**: [https://www.iankduncan.com/engineering/2025-11-24-json-schema-demystified/](https://www.iankduncan.com/engineering/2025-11-24-json-schema-demystified/)

本文旨在通过清晰易懂的方式解释核心概念及其关系，从而揭开 JSON Schema 术语的神秘面纱。它分解了schemas、metaschemas、方言和词汇表等常令人困惑的术语，阐述了它们如何协同工作来定义和验证 JSON 数据。

**Schema（模式）**是一个 JSON 文档，它定义了对其他 JSON 文档的约束，指定数据类型、允许的值和必需的属性。 **Metaschema（元模式）**是一种模式，用于描述其他模式的结构，验证模式是否格式良好并符合规范。

**Dialect（方言）**是 JSON Schema 的特定版本，由特定的元模式定义。不同的方言支持不同的关键字和行为，通过 URI（在您的模式中使用 `$schema` 关键字）进行标识。

**Vocabularies（词汇表）**，在 Draft 2019-09 中引入，是提供特定功能的命名关键字集合。它们提高了模块化，允许您选择和组合相关的关键字。本文重点介绍了核心、应用器、验证和元数据词汇表作为关键示例。

本文还强调了 JSON Schema 通过自定义词汇表的可扩展性。这允许开发人员为诸如 API 描述之类的任务定义特定于领域的关键字。

关键结论是，JSON Schema 是一种强大而灵活的数据验证工具，它建立在定义明确的概念和关系的基础上，并支持自定义扩展。理解这些概念对于在各种应用程序中有效使用和扩展 JSON Schema 至关重要。

---

## 53. 找回性感。互联网监控扼杀了情色。

**原文标题**: Bringing Sexy Back. Internet surveillance has killed eroticism

**原文链接**: [https://lux-magazine.com/article/privacy-eroticism/](https://lux-magazine.com/article/privacy-eroticism/)

无法访问文章链接。

---

## 54. 如何在Word模板中让Pandoc识别自定义表格样式

**原文标题**: How to get Pandoc to respect custom table styles in Word templates

**原文链接**: [https://johnathandos.com/posts/2025-11-24-custom-tables-with-pandoc/](https://johnathandos.com/posts/2025-11-24-custom-tables-with-pandoc/)

使用Pandoc自定义Markdown转.docx的表格样式

本文介绍了如何在使用Pandoc和自定义参考文档将Markdown转换为.docx时自定义表格样式。关键在于，Pandoc会专门查找参考文档中名为“Table”的表格样式，并将其应用于转换输出中的表格。

作者最初遇到了困难，因为提供的参考文档缺少明确命名为“Table”的表格样式。他们也忽略了Pandoc文档中提到“Table”样式的要求，并且不信任基于LLM的故障排除，导致使用样式管理器从新的Word文档中提取默认“Table”样式的更复杂变通方法。

最终，作者发现了最简单的解决方案：直接在Word中的参考文档中创建一个新的表格样式，并将其命名为“Table”。对该“Table”样式所做的任何修改都将被Pandoc应用于Markdown到.docx转换期间生成的表格。本文旨在避免替代方法的不必要复杂性，强调在Pandoc工作流程中使用“Table”样式名称进行自定义表格格式设置的重要性。

---

## 55. Atuin 的全新 Runbook 执行引擎

**原文标题**: Atuin’s New Runbook Execution Engine

**原文链接**: [https://blog.atuin.sh/introducing-the-new-runbook-execution-engine/](https://blog.atuin.sh/introducing-the-new-runbook-execution-engine/)

Atuin Desktop 发布重大架构更新，完全重新设计的 Runbook 执行引擎，解决了上下文不稳定和执行不一致等问题。新引擎引入了持久化的 Runbook 状态，这意味着关闭标签或重启应用后，无需再重建或重新运行代码块。现在，Runbook 的行为可预测，上下文仅向下流动。

主要改进包括：

*   **持久化上下文：** Runbook 跨重启记住其状态。
*   **可重现的执行：** 代码块仅影响其下方的代码块。
*   **模板无处不在：** 模板可用于变量名、上下文块和任何输入字段。
*   **自引用变量：** 变量现在可以引用自身。
*   **两种类型的上下文：** 被动（自动设置）和主动（执行期间设置），后者在重启后持续存在，并可使用新按钮清除。

此次更新为实时协作奠定了基础。更改包括移除全局上下文，用手动更新 UI 替换编辑器变量同步切换，以及脚本输出变量仅捕获 stdout。

在底层，执行系统已用 Rust 重写，使其更具可移植性和可靠性。新的架构为 CLI 运行器、改进的串行执行、密钥管理和基于 Markdown 的 Runbook 铺平了道路。该更新现已在 v0.2.0 中提供。

---

## 56. 空客请求改装6千架飞机，航班中断预警

**原文标题**: Flight disruption warning as Airbus requests modifications to 6k planes

**原文链接**: [https://www.bbc.com/news/live/cvg4y6g74ert](https://www.bbc.com/news/live/cvg4y6g74ert)

空中客车警告：超过6000架飞机（主要为A320型号）因必要的软件更新预计将出现航班中断。问题源于飞机电脑容易受到强烈太阳辐射干扰的漏洞，可能导致数据损坏并影响飞机高度。此前，捷蓝航空一架飞机在10月份经历了一次突然的高度下降，据信是由太阳干扰引起的，此问题由此被曝光。此次中断的时间恰逢美国的主要假日周末，将影响美国航空、达美航空、捷蓝航空和联合航空等主要A320运营商。虽然英国机场受到的影响有限，但全球多家航空公司已报告航班取消。

---

## 57. SQLite 作为应用程序文件格式

**原文标题**: SQLite as an Application File Format

**原文链接**: [https://sqlite.org/appfileformat.html](https://sqlite.org/appfileformat.html)

生成摘要时出错

---

## 58. 荷兰大学能否摆脱微软？

**原文标题**: Can Dutch universities do without Microsoft?

**原文链接**: [https://dub.uu.nl/en/news/can-dutch-universities-do-without-microsoft](https://dub.uu.nl/en/news/can-dutch-universities-do-without-microsoft)

HOP文章《荷兰大学能否摆脱微软？》可能探讨了荷兰大学内部关于其对微软软件和服务依赖性的持续争论。该文章可能讨论了迁移到开源替代方案的挑战和潜在益处。

可能涵盖的关键点包括：

*   **现状：** 大多数荷兰大学在核心运营、研究和教育方面严重依赖微软产品，如Windows、Office 365和Azure。
*   **担忧：** 该文章可能涉及对供应商锁定、数据隐私（特别是涉及云法案时）、成本以及对所使用软件缺乏控制的担忧。
*   **替代方案的论据：** 该文章可能强调开源替代方案的优势，例如更高的安全性、透明度、成本节约、定制可能性以及创新潜力。
*   **迁移挑战：** 该文章可能讨论了切换到替代方案所涉及的障碍，包括兼容性问题、用户培训、所需的技术专业知识以及对现有工作流程的潜在中断。
*   **例子：** 该文章可能会引用已经开始试验开源解决方案的特定大学或部门，以及从这些经验中获得的教训。
*   **潜在的解决方案/策略：** 该文章可能涉及大学可以采取的减少对微软依赖的可能方法，例如逐步迁移，首先关注特定用例，投资于开源专业知识，以及与其他机构合作。

本质上，该文章可能提出了这样一个问题：荷兰大学在独立于微软生态系统的未来是否可行，并探讨了这种转型所涉及的复杂性和考量因素。

---

## 59. 长期运行代理的有效工具

**原文标题**: Effective harnesses for long-running agents

**原文链接**: [https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

本文探讨了构建高效长期运行AI代理的挑战，特别是对于软件开发等需要在多个上下文窗口中持续努力的复杂任务。核心问题在于，代理通常难以保持连续性并取得持续进展，因为每个会话都是从头开始，缺乏对先前工作的记忆。

作者提出了一个由两部分组成的解决方案，以实现跨上下文窗口的有效工作：

1.  **初始化代理（Initializer Agent）：** 此代理设置初始环境，包括用于服务器设置的 `init.sh` 脚本，用于跟踪进度的 `claude-progress.txt` 文件，初始git提交，以及将所有功能最初标记为“失败”的全面功能列表（JSON格式）。

2.  **编码代理（Coding Agent）：** 此代理在每个会话中逐步取得进展，一次专注于一个功能，并将环境保持在适合合并的“干净状态”。它首先读取进度注释、git日志和功能列表，以了解当前状态，然后运行基本测试。提示该代理将进度提交到git，并附带描述性消息，以及更新进度文件。浏览器自动化工具用于端到端测试和功能验证。

该解决方案解决了常见的故障模式：代理过早地宣布胜利，将环境置于错误状态，在没有适当测试的情况下将功能标记为已完成，以及难以运行应用程序。

文章表明，虽然这种方法展示了进展，但关于最佳代理架构的问题仍然存在：通用代理还是专用代理（测试、QA、代码清理）更有效。此外，将解决方案从Web应用程序开发推广到科学研究或金融建模等其他领域是未来工作的方向。

---

## 60. 哥本哈根指数2025：全球自行车友好城市排名

**原文标题**: Copenhagenize Index 2025: The Global Ranking of Bicycle-Friendly Cities

**原文链接**: [https://copenhagenizeindex.eu/](https://copenhagenizeindex.eu/)

哥本哈根化指数2025，EIT城市交通版：对全球100座城市的自行车友好度进行排名。这项综合排名评选出前30名城市，着重展示自行车基础设施和文化领域的全球领导者。

该指数还提供区域排名，展示北美（蒙特利尔）、拉丁美洲（尼泰罗伊）、欧洲（乌得勒支）、非洲（奎利马内）以及亚洲和大洋洲（基督城）的领先城市。值得注意的是，乌得勒支、哥本哈根和根特名列总榜单前茅。

该文件列出了前30名城市及其相应的排名和指数得分，从而可以根据促进自行车友好度的因素对城市进行比较。

提供的信息声明，通过表格提交收集的数据将仅用于处理询问和后续跟进，并遵守概述的隐私政策。

该文件还重点介绍了“成功案例”，详细介绍了布莱恩特大道和内罗毕等城市因自行车友好倡议而产生的积极转变，以及布尔诺的交通教育计划。联系方式已提供，以供进一步查询。

---

## 61. 显示 HN：检测带有摄像头的智能眼镜的眼镜

**原文标题**: Show HN: Glasses to detect smart-glasses that have cameras

**原文链接**: [https://github.com/NullPxl/banrays](https://github.com/NullPxl/banrays)

此篇“Show HN”帖子详细介绍了一项实验，旨在制作一种眼镜（“Ban-Rays”）来检测带有隐藏摄像头的智能眼镜，特别是针对Meta Rayban。该项目探索了两种主要的检测方法：光学和网络。

光学方法利用相机镜头的逆反射性（猫眼效应），通过照射红外光并检测反射信号来实现。作者最初难以区分相机反射与其他表面的反射，使用简单的红外扫描和光电二极管时，信号强度不一致。他们正在尝试结构化的扫描模式和不同的波长来提高区分度。

网络方法侧重于蓝牙低功耗（BLE）指纹识别。作者成功地通过识别配对或开机期间的制造商数据（Meta的SIG分配ID 0x01AB）和服务UUID（0xFD5F）来检测Meta Rayban。然而，在活跃使用期间（与配对手机通信时）检测它们被证明很困难，需要更高级的BLE流量分析。作者正在探索使用nRF模块来解决这个问题，并承认由于硬件成本的原因，使用经典蓝牙具有挑战性。作者引用了相关的研究论文，并感谢合作者的投入。

---

## 62. 对“Glauert最佳旋翼盘重访”的评论

**原文标题**: Comments on "Glauert's optimum rotor disk revisited"

**原文链接**: [https://wes.copernicus.org/preprints/wes-2025-105/](https://wes.copernicus.org/preprints/wes-2025-105/)

本文详细阐述了围绕J. Gordon Leishman对Tyagi和Schmitz (2025)发表在《风能科学》上的论文“Glauert最佳转子盘再探”的评论所展开的公开讨论。Leishman的评论批判了该论文的实际相关性、物理可实现性和新颖性，并对高低叶尖速比限制以及动量理论的应用提出了质疑。

Leishman认为该论文在高叶尖速比限制下存在根本性矛盾，即消失的旋涡意味着零扭矩和功率，并批评了在低叶尖速比限制下动量理论的使用，因为此时其假设已经失效。他还质疑了变分法的新颖性。

回复包括匿名审稿人（RC1和RC2）、评论作者（AC1和AC4）以及《风能科学》主编（CEC1）的回复。审稿人认为Leishman的批评主要基于对该论文实用性的主观意见。Leishman则指责审稿人（认为他是编辑）是在为发表决定辩护，而不是提供公正的科学评论。他坚持认为，他指出的问题是事实且可验证的，而不仅仅是意见。

主编澄清说，审稿人是独立的专家，并且处理该评论审查的编辑与原始论文不同。此外，还发表了一篇社论，涉及Tyagi和Schmitz论文的某些方面。此次讨论突显了对原始论文的解释和价值的争议，Leishman认为该论文包含错误和不实之处。

---

## 63. 信用报告显示Meta通过高级几何技术将270亿美元隐藏在账外

**原文标题**: Credit report shows Meta keeping $27B off its books through advanced geometry

**原文链接**: [https://stohl.substack.com/p/exclusive-credit-report-shows-meta](https://stohl.substack.com/p/exclusive-credit-report-shows-meta)

无法访问文章链接。

---

## 64. 正式请愿：在德国正式承认开源工作为公民服务

**原文标题**: Petition to formally recognize open source work as civic service in Germany

**原文链接**: [https://www.openpetition.de/petition/online/anerkennung-von-open-source-arbeit-als-ehrenamt-in-deutschland#petition-main](https://www.openpetition.de/petition/online/anerkennung-von-open-source-arbeit-als-ehrenamt-in-deutschland#petition-main)

德国一项请愿旨在正式承认开源工作为公民服务（“Ehrenamt” - 常译为志愿工作或荣誉职务）。主要论点是开源贡献与传统志愿活动一样，对社会具有显著益处，应得到相应认可。

该请愿似乎源于开源开发者希望与从事传统志愿工作（如在俱乐部和协会工作）的人们获得同等待遇的愿望。与公民服务认可相关的福利可能包括税收优惠、获得特定资源或对贡献的正式认可。

这些文章表明，开源社区内部正在兴起一场争取这种正式认可的运动，突显了其工作的社会价值，并寻求与其他形式的公民参与的同等地位。报道该主题的大量新闻文章表明公众对此有浓厚的兴趣和潜在的支持。

---

## 65. Moss：一个用26000行代码编写的Rust Linux兼容内核

**原文标题**: Moss: a Rust Linux-compatible kernel in 26,000 lines of code

**原文链接**: [https://github.com/hexagonal-sun/moss](https://github.com/hexagonal-sun/moss)

Moss：一个用 Rust 和 Aarch64 汇编编写的 Linux 兼容内核，旨在实现现代化的异步核心和模块化架构。它与 Linux 用户空间应用程序二进制兼容，目前能够运行大多数 BusyBox 命令。其关键特性是在内核中使用 Rust 的 async/await 模型来防止死锁。

该内核拥有诸如完整 aarch64 支持（带有便于移植的 HAL）、完整 MMU 启用、写时复制页、安全用户空间交互以及用于内存管理的伙伴分配器等特性。进程管理包括调度、任务迁移以及 51 个 Linux 系统调用的实现。

Moss 利用带有异步抽象的虚拟文件系统，并包含 Ramdisk、只读 FAT32 和 devtmpfs 的驱动程序。该项目构建在 libkernel（一个与架构无关的实用程序库）之上，提供了一个全面的测试套件，可以在部署之前在主机上测试逻辑。

本文档概述了使用 QEMU 构建和运行 Moss 的说明，包括准备镜像以及运行内核和测试套件的命令。

该项目路线图侧重于扩展 Linux 系统调用兼容性、实现网络堆栈 (TCP/IP)、改进调度器以实现任务负载均衡、开发可读/写文件系统以及扩展支持的系统调用数量。鼓励贡献，该项目已获得 MIT 许可证。

---

## 66. “标普493”揭示了不同的美国经济

**原文标题**: The 'S&P 493' reveals a different U.S. economy

**原文链接**: [https://www.msn.com/en-us/money/markets/the-s-p-493-reveals-a-very-different-us-economy/ar-AA1R1VUJ](https://www.msn.com/en-us/money/markets/the-s-p-493-reveals-a-very-different-us-economy/ar-AA1R1VUJ)

这篇题为《“标普493”揭示不同的美国经济》的MSN文章，可能认为，如果将标普500指数中领先的公司（在剔除占主导地位的“七巨头”或类似的高绩效科技公司群体后，被称为“标普493”）排除在外，就能看到一幅不同的，且可能不那么乐观的美国经济图景。

其核心论点可能是，标普500指数的整体强劲表现，是由少数几家超大型科技股不成比例地推动的。这种集中掩盖了更大一部分公司的困境或表现不佳，而这些公司代表了美国经济更为多样化的横截面。这些其他公司可能正面临着通货膨胀、利率上升、供应链问题以及消费者需求变化等挑战。

这篇文章可能突出了少数科技巨头蓬勃发展的利润与标普500指数中大多数公司所经历的较为温和或负增长之间的差异。它可能暗示这种差异令人担忧，可能表明更广泛的经济存在脆弱性，而这种脆弱性正被少数公司的优异表现所掩盖。

这篇文章可能还建议，不要仅仅依赖标普500指数作为衡量整体经济健康的指标，并倡导对构成美国经济的各个行业和公司规模有更细致的了解。此外，它还可以探讨对投资者的潜在影响，这些投资者可能过度暴露于这些高科技股票，并错失了其他市场领域的机遇或风险。

---

## 67. Pocketbase – 单文件开源实时后端

**原文标题**: Pocketbase – open-source realtime back end in 1 file

**原文链接**: [https://pocketbase.io/](https://pocketbase.io/)

本文介绍 PocketBase，一个打包成单个可执行文件的开源、实时后端。主要内容包括：

*   **简洁性：** PocketBase 旨在通过在单个文件中提供完整的后端解决方案来实现简洁性，从而简化部署和管理。

*   **实时功能：** 它提供实时功能，使应用程序能够立即对数据更改做出反应。

*   **开源：** 作为开源软件，用户可以自由地检查、修改和分发代码。

*   **资源：** 本文提供了实时演示和官方文档的链接，鼓励用户探索 PocketBase 的功能并了解更多关于其特性的信息。

本质上，PocketBase 为寻求快速、易于部署且具有实时功能的后端解决方案的开发人员提供了一个简化的开源替代方案。提供的资源邀请用户尝试该软件并深入研究其文档，以获得全面的理解和使用。

---

## 68. A Repository with 44 Years of Unix Evolution

**原文标题**: A Repository with 44 Years of Unix Evolution

**原文链接**: [https://www.spinellis.gr/pubs/conf/2015-MSR-Unix-History/html/Spi15c.html](https://www.spinellis.gr/pubs/conf/2015-MSR-Unix-History/html/Spi15c.html)

生成摘要时出错

---

## 69. Show HN: An LLM-Powered Tool to Catch PCB Schematic Mistakes

**原文标题**: Show HN: An LLM-Powered Tool to Catch PCB Schematic Mistakes

**原文链接**: [https://netlist.io/](https://netlist.io/)

生成摘要时出错

---

## 70. A Tale of Four Fuzzers

**原文标题**: A Tale of Four Fuzzers

**原文链接**: [https://tigerbeetle.com/blog/2025-11-28-tale-of-four-fuzzers/](https://tigerbeetle.com/blog/2025-11-28-tale-of-four-fuzzers/)

生成摘要时出错

---

## 71. Show HN: Pulse 2.0 – Live co-listening rooms where anyone can be a DJ

**原文标题**: Show HN: Pulse 2.0 – Live co-listening rooms where anyone can be a DJ

**原文链接**: [https://473999.net/pulse](https://473999.net/pulse)

生成摘要时出错

---

## 72. Tiger Style: Coding philosophy (2024)

**原文标题**: Tiger Style: Coding philosophy (2024)

**原文链接**: [https://tigerstyle.dev/](https://tigerstyle.dev/)

生成摘要时出错

---

## 73. KDE going all-in on a Wayland future

**原文标题**: KDE going all-in on a Wayland future

**原文链接**: [https://blogs.kde.org/2025/11/26/going-all-in-on-a-wayland-future/](https://blogs.kde.org/2025/11/26/going-all-in-on-a-wayland-future/)

生成摘要时出错

---

## 74. How to use Linux vsock for fast VM communication

**原文标题**: How to use Linux vsock for fast VM communication

**原文链接**: [https://popovicu.com/posts/how-to-use-linux-vsock-for-fast-vm-communication/](https://popovicu.com/posts/how-to-use-linux-vsock-for-fast-vm-communication/)

生成摘要时出错

---

## 75. Datacenters in space are a terrible, horrible, no good idea

**原文标题**: Datacenters in space are a terrible, horrible, no good idea

**原文链接**: [https://taranis.ie/datacenters-in-space-are-a-terrible-horrible-no-good-idea/](https://taranis.ie/datacenters-in-space-are-a-terrible-horrible-no-good-idea/)

生成摘要时出错

---

## 76. Space: 1999 – Special Effects Techniques

**原文标题**: Space: 1999 – Special Effects Techniques

**原文链接**: [https://catacombs.space1999.net/main/pguide/upsfx.html](https://catacombs.space1999.net/main/pguide/upsfx.html)

生成摘要时出错

---

## 77. How to make precise sheet metal parts (photochemical machining) [video]

**原文标题**: How to make precise sheet metal parts (photochemical machining) [video]

**原文链接**: [https://www.youtube.com/watch?v=bR9EN3kUlfg](https://www.youtube.com/watch?v=bR9EN3kUlfg)

生成摘要时出错

---

## 78. Open (Apache 2.0) TTS model for streaming conversational audio in realtime

**原文标题**: Open (Apache 2.0) TTS model for streaming conversational audio in realtime

**原文链接**: [https://github.com/nari-labs/dia2](https://github.com/nari-labs/dia2)

生成摘要时出错

---

## 79. Implementing Bluetooth LE Audio and Auracast on Linux Systems

**原文标题**: Implementing Bluetooth LE Audio and Auracast on Linux Systems

**原文链接**: [https://www.collabora.com/news-and-blog/blog/2025/11/24/implementing-bluetooth-le-audio-and-auracast-on-linux-systems/](https://www.collabora.com/news-and-blog/blog/2025/11/24/implementing-bluetooth-le-audio-and-auracast-on-linux-systems/)

生成摘要时出错

---

## 80. Lobsters Interview

**原文标题**: Lobsters Interview

**原文链接**: [https://susam.net/my-lobsters-interview.html](https://susam.net/my-lobsters-interview.html)

生成摘要时出错

---

## 81. Writing Builds Resilience in Everyday Challenges by Changing Your Brain

**原文标题**: Writing Builds Resilience in Everyday Challenges by Changing Your Brain

**原文链接**: [https://scienceclock.com/writing-builds-resilience-in-everyday-challenges-by-changing-your-brain/](https://scienceclock.com/writing-builds-resilience-in-everyday-challenges-by-changing-your-brain/)

生成摘要时出错

---

## 82. Tech Titans Amass Multimillion-Dollar War Chests to Fight AI Regulation

**原文标题**: Tech Titans Amass Multimillion-Dollar War Chests to Fight AI Regulation

**原文链接**: [https://www.wsj.com/tech/ai/tech-titans-amass-multimillion-dollar-war-chests-to-fight-ai-regulation-88c600e1](https://www.wsj.com/tech/ai/tech-titans-amass-multimillion-dollar-war-chests-to-fight-ai-regulation-88c600e1)

生成摘要时出错

---

## 83. A Remarkable Assertion from A16Z

**原文标题**: A Remarkable Assertion from A16Z

**原文链接**: [https://nealstephenson.substack.com/p/a-remarkable-assertion-from-a16z](https://nealstephenson.substack.com/p/a-remarkable-assertion-from-a16z)

生成摘要时出错

---

## 84. Generalizing Printf in C

**原文标题**: Generalizing Printf in C

**原文链接**: [https://webb.is-a.dev/articles/generalizedprintf/](https://webb.is-a.dev/articles/generalizedprintf/)

生成摘要时出错

---

## 85. Rock Paper Scissors Solitaire

**原文标题**: Rock Paper Scissors Solitaire

**原文链接**: [https://klezlab.it/rock-paper-scissors-solitaire.html](https://klezlab.it/rock-paper-scissors-solitaire.html)

生成摘要时出错

---

## 86. Voyager 1 is about to reach one light-day from Earth

**原文标题**: Voyager 1 is about to reach one light-day from Earth

**原文链接**: [https://scienceclock.com/voyager-1-is-about-to-reach-one-light-day-from-earth/](https://scienceclock.com/voyager-1-is-about-to-reach-one-light-day-from-earth/)

生成摘要时出错

---

## 87. AltSendme: Another Alternative to MAgic Wormhole?

**原文标题**: AltSendme: Another Alternative to MAgic Wormhole?

**原文链接**: [https://github.com/tonyantony300/alt-sendme](https://github.com/tonyantony300/alt-sendme)

生成摘要时出错

---

## 88. A brief history of NSA backdoors. (2013)

**原文标题**: A brief history of NSA backdoors. (2013)

**原文链接**: [https://www.ethanheilman.com/x/12/index.html](https://www.ethanheilman.com/x/12/index.html)

生成摘要时出错

---

## 89. The GitHub Infrastructure Powering North Korea's Contagious Interview NPM Attack

**原文标题**: The GitHub Infrastructure Powering North Korea's Contagious Interview NPM Attack

**原文链接**: [https://socket.dev/blog/north-korea-contagious-interview-npm-attacks](https://socket.dev/blog/north-korea-contagious-interview-npm-attacks)

生成摘要时出错

---

## 90. Anti-patterns while working with LLMs

**原文标题**: Anti-patterns while working with LLMs

**原文链接**: [https://instavm.io/blog/llm-anti-patterns](https://instavm.io/blog/llm-anti-patterns)

生成摘要时出错

---

## 91. The Great Downzoning

**原文标题**: The Great Downzoning

**原文链接**: [https://worksinprogress.co/issue/the-great-downzoning/](https://worksinprogress.co/issue/the-great-downzoning/)

生成摘要时出错

---

## 92. Shor's algorithm: the one quantum algo that ends RSA/ECC tomorrow

**原文标题**: Shor's algorithm: the one quantum algo that ends RSA/ECC tomorrow

**原文链接**: [https://blog.ellipticc.com/posts/what-is-shors-algorithm-and-why-its-the-single-biggest-threat-to-classical-cryptography/](https://blog.ellipticc.com/posts/what-is-shors-algorithm-and-why-its-the-single-biggest-threat-to-classical-cryptography/)

生成摘要时出错

---

## 93. Open-Source n8n Alternative for Workflow Building (GUI and Docker Included)

**原文标题**: Open-Source n8n Alternative for Workflow Building (GUI and Docker Included)

**原文链接**: [https://github.com/empowerd-cms/nyno](https://github.com/empowerd-cms/nyno)

生成摘要时出错

---

## 94. Same-day upstream Linux support for Snapdragon 8 Elite Gen 5

**原文标题**: Same-day upstream Linux support for Snapdragon 8 Elite Gen 5

**原文链接**: [https://www.qualcomm.com/developer/blog/2025/10/same-day-snapdragon-8-elite-gen-5-upstream-linux-support](https://www.qualcomm.com/developer/blog/2025/10/same-day-snapdragon-8-elite-gen-5-upstream-linux-support)

生成摘要时出错

---

## 95. Mixpanel Security Breach

**原文标题**: Mixpanel Security Breach

**原文链接**: [https://mixpanel.com/blog/sms-security-incident/](https://mixpanel.com/blog/sms-security-incident/)

生成摘要时出错

---

## 96. A programmer-friendly I/O abstraction over io_uring and kqueue (2022)

**原文标题**: A programmer-friendly I/O abstraction over io_uring and kqueue (2022)

**原文链接**: [https://tigerbeetle.com/blog/2022-11-23-a-friendly-abstraction-over-iouring-and-kqueue/](https://tigerbeetle.com/blog/2022-11-23-a-friendly-abstraction-over-iouring-and-kqueue/)

生成摘要时出错

---

## 97. Maxduino Review: Tape Cassette Emulator for Multiple Retro Computers

**原文标题**: Maxduino Review: Tape Cassette Emulator for Multiple Retro Computers

**原文链接**: [https://retrogamecoders.com/maxduino-review/](https://retrogamecoders.com/maxduino-review/)

生成摘要时出错

---

## 98. Penpot: The Open-Source Figma

**原文标题**: Penpot: The Open-Source Figma

**原文链接**: [https://github.com/penpot/penpot](https://github.com/penpot/penpot)

生成摘要时出错

---

## 99. How to Never Get Overstimulated Again

**原文标题**: How to Never Get Overstimulated Again

**原文链接**: [https://substack.com/home/post/p-177511410](https://substack.com/home/post/p-177511410)

生成摘要时出错

---

## 100. Airbus grounds A320 aircraft amid solar radiation risk

**原文标题**: Airbus grounds A320 aircraft amid solar radiation risk

**原文链接**: [https://aerospaceglobalnews.com/news/a320-grounding-radiation/](https://aerospaceglobalnews.com/news/a320-grounding-radiation/)

生成摘要时出错

---

