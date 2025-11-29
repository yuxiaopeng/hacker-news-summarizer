# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-11-29.md)

*最后自动更新时间: 2025-11-29 17:47:07*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 2 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 3 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 4 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 5 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 6 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 7 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 8 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 9 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 10 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 11 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 12 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 13 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 14 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 15 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 16 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 17 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 18 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 19 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 20 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 21 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 22 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 23 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 24 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 25 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 26 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 27 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 28 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 29 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 30 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 31 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 32 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 33 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 34 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 35 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 36 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 37 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 38 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 39 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 40 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 41 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 42 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 43 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 44 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 45 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 46 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 47 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 48 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 49 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 50 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 51 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 52 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 53 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 54 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 55 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 56 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 57 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 58 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 59 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 60 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 61 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 62 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 63 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 64 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 65 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 66 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 67 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 68 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 69 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 70 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 71 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 72 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 73 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 74 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 75 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 76 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 77 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 78 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 79 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 80 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 81 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 82 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 83 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 84 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 85 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 86 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 87 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 88 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 89 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 90 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 91 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 92 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 93 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 94 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 95 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 96 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 97 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 98 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 99 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 100 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 101 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 102 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 103 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 104 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 105 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 106 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 107 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 108 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 109 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 110 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 111 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 112 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 113 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 114 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 115 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 116 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 117 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 118 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 119 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 120 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 121 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 122 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 123 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 124 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 125 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 126 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 127 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 128 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 129 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 130 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 131 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 132 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 133 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 134 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 135 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 136 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 137 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 138 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 139 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 140 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 141 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 142 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 143 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 144 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 145 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 146 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 147 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 148 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 149 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 150 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 151 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 152 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 153 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 154 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 155 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 156 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 157 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 158 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 159 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 160 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 161 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 162 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 163 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 164 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 165 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 166 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 167 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 168 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 169 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 170 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 171 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 172 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 173 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 174 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 175 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 176 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 177 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 178 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 179 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 180 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 181 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 182 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 183 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 184 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 185 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 186 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 187 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 188 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 189 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 190 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 191 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 192 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 193 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 194 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 195 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 196 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 197 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 198 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 199 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 200 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 201 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 202 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 203 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 204 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 205 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 206 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 207 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 208 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 209 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 210 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 211 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 212 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 213 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 214 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 215 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 216 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 217 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 218 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 219 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 220 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 221 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 222 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 223 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 224 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 225 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 226 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 227 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 228 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 229 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 230 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 231 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 232 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 233 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 234 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 235 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 236 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 237 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 238 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 239 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 240 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 241 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 242 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 243 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 244 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 245 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 246 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 247 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 248 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 249 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 250 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 251 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 252 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 253 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 254 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
