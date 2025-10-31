# Hacker News 热门文章摘要 (2025-10-31)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Ubuntu 推出架构变体

**原文标题**: Ubuntu Introduces Architecture Variants

**原文链接**: [https://lwn.net/Articles/1044383/](https://lwn.net/Articles/1044383/)

Ubuntu 25.10引入“架构变体”，允许针对特定x86-64架构级别（如x86-64-v3）构建和优化软件包。这种由Michael Hudson-Doyle倡导的方法为现代硬件提供性能改进，同时避免像RHEL放弃x86-64-v2支持那样强制淘汰旧系统。

用户可以选择使用优化的x86-64-v3软件包。然而，评论区显示了对该方法相关成本的担忧，包括仓库和镜像的存储需求增加、构建多个变体导致的构建时间延长，以及与支持和二进制混合相关的潜在复杂性。一些评论员指出，RHEL/Fedora由于这些基础设施和支持负担而选择不实施类似的变体，认为彻底的决裂更为可取，尽管会对遗留硬件用户产生影响。总体情绪倾向于赞赏Ubuntu方法的灵活性，但也承认其在资源、维护和支持复杂性方面的潜在挑战。

---

## 2. Nix 衍生品疯狂

**原文标题**: Nix Derivation Madness

**原文链接**: [https://fzakaria.com/2025/10/29/nix-derivation-madness](https://fzakaria.com/2025/10/29/nix-derivation-madness)

本文探讨了Nix包管理系统令人惊讶的方面，重点关注固定输出派生(FOD)及其对依赖关系图的影响。作者最初遇到一种情况：Ruby二进制文件存在，但其对应的派生文件在他们的系统或NixOS缓存中不可用。

调查表明，FOD虽然为给定哈希生成一致的输出，但可能会在派生中引入意外的变动。对FOD属性的更改，例如添加“垃圾”，会改变其派生路径（.drv文件），而不会影响最终输出。这意味着依赖于FOD的派生也会获得新的.drv路径，即使它们的输出保持不变。如果输出之前被缓存，则到更新后的.drv的链接会丢失，从而产生差异。

此外，作者展示了一个场景：两个具有*相同*输出的FOD可以用作另一个派生的输入。值得注意的是，可以从派生的JSON表示中*删除*其中一个输入，并且修改后的派生仍然会产生相同的输出。这突出了派生和输出之间的多对一关系，允许看似不同的派生产生相同的结果，并展示了固定输出派生引入的复杂动态。文章强调，理解FOD对于理解Nix的行为以及与依赖管理和缓存相关的潜在陷阱至关重要。

---

## 3. 因脑部排液导致睡眠不足，注意力涣散。

**原文标题**: Attention lapses due to sleep deprivation due to flushing fluid from brain

**原文链接**: [https://news.mit.edu/2025/your-brain-without-sleep-1029](https://news.mit.edu/2025/your-brain-without-sleep-1029)

麻省理工学院新闻报道：研究揭示睡眠不足后注意力涣散与脑脊液流动有关。研究人员发现，注意力短暂失效（常被描述为“走神”）与脑脊液*流出*大脑的波浪式流动相一致，而这种过程通常只发生在睡眠期间，用于清除废物。

该研究发表于《自然·神经科学》，让睡眠不足和睡眠充足的参与者在接受fMRI和脑电图监测的同时执行注意力任务。睡眠不足的参与者表现更差，并且关键的是，研究人员观察到脑脊液流动与注意力涣散同时发生。具体来说，当注意力失效时，脑脊液就*流出*大脑，而当注意力恢复时，脑脊液又*流回*大脑。

研究人员推测，睡眠不足的大脑试图通过在清醒时启动这些脑脊液脉冲来补偿夜间清洁的不足，但代价是损害了注意力。他们还注意到同步的生理变化，包括心率和呼吸频率降低以及瞳孔收缩，这表明存在一个统一的回路控制着注意力和身体功能。该回路可能涉及去甲肾上腺素系统。 研究结果表明，大脑对睡眠的需求非常关键，以至于它甚至会在清醒时启动类似睡眠的清洁过程，从而暂时损害注意力表现。

---

## 4. AI爬虫请求注释脚本

**原文标题**: AI scrapers request commented scripts

**原文链接**: [https://cryptography.dog/blog/AI-scrapers-request-commented-scripts/](https://cryptography.dog/blog/AI-scrapers-request-commented-scripts/)

Aaron P. MacSween的文章详细描述了人工智能抓取器请求JavaScript文件的发现，这些文件仅在HTML注释中引用（因此不应由合法浏览器请求）。 这些抓取器很可能正在收集用于LLM训练的数据，它们表现出不同程度的复杂性，一些使用真实的浏览器用户代理字符串，而另一些使用默认的HTTP库值。 MacSween将此行为归类为根本性的，这意味着修复它需要抓取器从根本上改变其行为，使其成为有价值的反制目标。

然后，他探讨了潜在的响应，从使用fail2ban进行简单的IP过滤，到更激进的策略，如提供解压炸弹和毒害训练数据。 他认为，公开披露此类抓取器行为可以帮助其他人阻止它们。

MacSween提倡数据投毒，强调最近的研究表明，相对少量的中毒样本可以显著损害LLM训练。 他认为数据投毒是对不道德收集数据以训练人工智能模型的合理回应，并鼓励使用免费的数据投毒工具。 他承认在将机器人拦截与数据投毒结合使用时可能存在复杂性，但最终强调需要创造性和积极地破坏大型科技公司的反社会活动。 他最后指出，基于行为怪癖识别机器人并不新鲜，但这种特定的怪癖尚未被广泛讨论。

---

## 5. 香菇菌丝制备的可持续忆阻器用于高频生物电子学

**原文标题**: Sustainable memristors from shiitake mycelium for high-frequency bioelectronics

**原文链接**: [https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0328965](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0328965)

本文探讨了香菇（Lentinula edodes）作为一种可持续且稳健的材料，用于创建神经形态计算忆阻器的潜力。作者证明，香菇菌丝网络可以与电极连接，从而创建可以生长、训练和保存的功能性忆阻器。这些真菌忆阻器在高达5.85 kHz的频率下表现出功能性，且精度很高（90±1%）。

该研究强调了使用真菌材料相对于传统半导体忆阻器的优势，包括可持续性、生物降解性和低功耗潜力。与需要稀土矿物和昂贵制造工艺的传统忆阻器生产不同，香菇提供了一种可扩展、环保的替代方案。真菌的天然成分和适应性为神经网络提供了更自然的模型。

此外，本文强调了香菇的耐辐射性，使其成为航空航天应用的可行选择，在这些应用中，传统电子设备可能会受到损害。作者认为，这种韧性归因于香菇多糖等化合物以及真菌的普遍适应性。通过展示真菌计算机的潜力，该研究连接了生物电子学和非常规计算，为神经形态硬件开发提供了一种新颖的方法。

---

## 6. AMD或将携台积电3纳米工艺声波APU进军ARM市场

**原文标题**: AMD Could Enter ARM Market with Sound Wave APU Built on TSMC 3nm Process

**原文链接**: [https://www.guru3d.com/story/amd-enters-arm-market-with-sound-wave-apu-built-on-tsmc-3nm-process/](https://www.guru3d.com/story/amd-enters-arm-market-with-sound-wave-apu-built-on-tsmc-3nm-process/)

据报道，AMD正在开发其首款基于ARM的APU，代号“声波”，旨在低功耗计算市场与高通骁龙X Elite竞争。泄露的信息显示，它将采用台积电的3纳米工艺制造，目标TDP范围为5W-10W。

“声波”采用BGA-1074封装，适用于移动设备，并且据传将为2026年未来的微软Surface产品提供动力。它采用2+4混合核心设计（两个性能核心和四个效率核心），4MB的三级缓存，以及受AMD GPU Infinity Cache启发的16MB MALL缓存。

该APU集成了四个RDNA 3.5计算单元，用于轻量级游戏和机器学习加速，以及一个128位LPDDR5X-9600内存控制器和16GB的板载RAM，反映了ARM SoC中统一内存的趋势。它还包括AMD的第四代AI引擎，用于设备上的推理任务。

虽然AMD之前曾尝试过ARM，“声波”代表着一种新的、更具战略意义的方式进入ARM市场，利用其在图形和AI方面的优势。预计将于2025年末开始生产，商业设备预计将于2026年上市。

---

## 7. 穿山甲 (YC S25) 正在招聘全栈软件工程师（开源）

**原文标题**: Pangolin (YC S25) Is Hiring a Full Stack Software Engineer (Open-Source)

**原文链接**: [https://docs.pangolin.net/careers/software-engineer-full-stack](https://docs.pangolin.net/careers/software-engineer-full-stack)

穿山甲 (YC S25) 正在招聘全栈软件工程师，以帮助构建和维护其身份感知远程访问平台。该平台专注于安全反向隧道，并正在向零信任网络演进，强调开源原则和自托管。

该职位涉及核心穿山甲容器的工作，包括 UI、API、模式等。工程师将设计、开发和测试前端 (NextJS、Tailwind、ShadCN) 和后端 (Express API、SQL、Drizzle ORM) 的功能，以及从事 CICD 和内部工具等流程。一项关键职责是在 GitHub 和 Discord 等平台上与开源社区互动。

穿山甲希望招聘具有 3 年以上经验、强大的 TypeScript 技能以及一些 Go 经验的候选人。熟悉 Web 身份 (OAuth2、OIDC、SSO)、云基础设施 (Docker、Kubernetes、AWS) 和基本网络概念者优先。他们必须位于旧金山或愿意搬迁。

该职位提供 12.5 万美元至 16 万美元的薪资，外加 0.5% 至 1.5% 的股权、搬迁补助、无限带薪休假以及混合办公环境。招聘流程包括初步面试、带薪开源项目贡献和入职。有意者请在 LinkedIn 上与 Owen 联系，发送简历/CV，并突出显示相关的 GitHub 项目。

---

## 8. 又一欧洲机构摆脱美国科技，数字主权势头渐起

**原文标题**: Another European agency shifts off US Tech as digital sovereignty gains steam

**原文链接**: [https://www.zdnet.com/article/another-european-agency-ditches-big-tech-as-digital-sovereignty-movement-gains-steam/](https://www.zdnet.com/article/another-european-agency-ditches-big-tech-as-digital-sovereignty-movement-gains-steam/)

欧洲政府机构和组织正逐渐摆脱对微软等美国大型科技供应商的依赖，转而采用欧洲本土的开源解决方案，以实现数字主权。例如，奥地利经济部正将其1200名员工迁移到基于Nextcloud的平台，以保障数据安全和控制。此举旨在保护敏感数据、遵守GDPR，并降低与外国监控相关的风险。

非营利组织EuroStack倡议通过推广欧洲科技解决方案来鼓励这一趋势。尽管美国政府对此转变表示担忧，但一些迁移，例如奥地利经济部和交通部（BMWET）的迁移，已取得成功，将开源解决方案与Teams等现有系统相结合。

然而，文章也警告称，仓促的过渡可能会带来问题。奥地利司法部向LibreOffice的过渡就出现了问题，导致文档格式不兼容和用户不满。关键在于，虽然开源解决方案具有增强安全性和控制等优势，但周密的计划和执行对于从专有软件成功迁移至关重要。文章总结道，精心设计的自主云解决方案在公共部门具有实用性和用户友好性。

---

## 9. 约翰·卡马克谈可变变量

**原文标题**: John Carmack on mutable variables

**原文链接**: [https://twitter.com/id_aa_carmack/status/1983593511703474196](https://twitter.com/id_aa_carmack/status/1983593511703474196)

未提供文章内容。文本仅包含：

*   一个标题暗示主题是关于约翰·卡马克对可变变量的看法。
*   一个错误信息，表明JavaScript已禁用，导致页面无法访问。
*   标准的网站页脚信息，例如服务条款、隐私政策等。

由于没有文章的实际内容，因此无法提供摘要。

---

## 10. psutil 的免线程 Python Wheels 包现已可用

**原文标题**: Wheels for free-threaded Python now available for psutil

**原文链接**: [https://gmpy.dev/blog/2025/wheels-for-free-threaded-python-now-available-in-psutil](https://gmpy.dev/blog/2025/wheels-for-free-threaded-python-now-available-in-psutil)

本文宣布自 7.1.2 版本起，`psutil` 提供支持自由线程 Python 的预编译 “wheel” 包。自由线程 Python 自 Python 3.13 起可用，禁用了全局解释器锁（GIL），从而允许在多核处理器上真正并行执行 Python 代码。

这些 wheel 包的开发需要对 `psutil` 的 C 代码进行大量的内部重构，这主要得益于社区的贡献。作者特别感谢 Lysandros Nikolaou 的工作。

本文强调，虽然自由线程 wheel 包的应用正在增长，但它在带有 C 扩展的流行 Python 包中仍然有限。

提供 wheel 包简化了用户的安装过程，特别是对于像 `psutil` 这样严重依赖 C 代码且具有复杂构建要求的包，避免了用户安装 C 编译器和相关工具的需求。

然而，本文也指出了库作者面临的一个挑战：缺乏通用的自由线程 wheel 包。必须为每个 Python 版本（例如 3.13 和 3.14）和平台构建单独的 wheel 包，这大大增加了要分发的文件数量并减慢了测试过程。文中提到了两个提案 PEP 803 和 PEP 809，它们有望在 Python 3.15 中通过启用通用 wheel 包来支持多个 Python 版本，从而解决此问题。

最后，它提供了使用 `pip install psutil --only-binary=:all:` 安装自由线程版本的 `psutil` 的说明。

---

## 11. Nim 2.2.6

**原文标题**: Nim 2.2.6

**原文链接**: [https://nim-lang.org//blog/2025/10/31/nim-226.html](https://nim-lang.org//blog/2025/10/31/nim-226.html)

Nim 2.2.6发布，修复Bug并提升性能

Nim 2.2稳定版的补丁版本2.2.6已于2025年10月31日发布。此版本包含141个提交，提供了Bug修复和性能改进。主要亮点包括改进了异步处理中异常处理的稳定性，以及编译器优化，可为`return obj.field`生成移动操作而不是复制操作。

可以通过操作系统软件包管理器或使用`choosenim`进行安装。文章建议将choosenim更新到最新版本（v.0.8.16），然后再更新Nim。

该版本解决了大量的Bug修复，涵盖了与内存管理、代码生成、编译器错误以及不同后端（C、JavaScript）的VM行为相关的问题。具体修复解决了销毁钩子、词法作用域、全局变量初始化、循环收集、asyncnet、闭包迭代器、泛型类型、借用字符串、开放数组、静态参数、范围检查、双端队列等问题。完整的更新日志可通过提供的链接获取。

---

## 12. MiniZinc中的轮换劳动力调度

**原文标题**: Rotating Workforce Scheduling in MiniZinc

**原文链接**: [https://zayenz.se/blog/post/rotating-workforce-scheduling/](https://zayenz.se/blog/post/rotating-workforce-scheduling/)

本文演示如何在MiniZinc中构建轮班排班（RWS）模型，从基本实现开始，逐步添加约束，使其更具现实性和可用性。RWS涉及为一组工人创建一套每周班表，其中每个工人每周轮换不同的班表，以确保公平性。该模型考虑了白班（D）、晚班（E）、夜班（N）和休息日。

基本模型定义了日期、班次、员工和班次需求的数据结构。它使用变量来表示班表，并使用`global_cardinality`确保每天每个班次都有所需的人数工作。但是，最初的解决方案通常由于长时间工作而没有休息而无法使用。

然后，本文添加了更实际的劳动规则：

1.  **连续休息日：** 使用带有正则表达式的`regular`约束强制执行每周至少有两天连续休息。
2.  **最长无休天数：** 使用辅助布尔变量和`sliding_sum`约束，将最长连续工作日限制为五天。
3.  **周末休息

每个添加的规则都完善了班表，使其更实用并解决了常见的排班问题。本文还提供了MiniZinc代码片段、示例数据和求解器统计信息，说明了每个约束对解决方案和求解时间的影响。最终模型生成了一个更加平衡并符合典型劳动力法规的班表。

---

## 13. Affinity Studio 现已免费

**原文标题**: Affinity Studio now free

**原文链接**: [https://www.affinity.studio/get-affinity](https://www.affinity.studio/get-affinity)

Affinity Studio 现已免费，由 Canva 荣誉呈现。这款一体化创意应用提供设计、图像编辑和页面排版工具，无需任何费用。下载需要使用 Canva 帐户（免费或付费）登录。该应用提供工作室级别的工具、可自定义的工作区、无损编辑和像素完美的导出选项。

使用 Affinity，您可以免费获得专业的设计、照片编辑和页面排版工具。Canva 高级用户可以在 Affinity 中解锁 Canva AI 工具。主要功能包括矢量设计、实时照片编辑、高级页面排版以及与各种文件格式的兼容性。

新的 Affinity 版本包括图像追踪、ePub 支持、网格渐变和可自定义的工作室等功能。虽然 Affinity V2 许可证仍然有效，但不会收到未来的更新。为了获得最佳体验，Canva 建议使用新的 Affinity 应用。

Affinity 支持 Windows 和 macOS，iPad 版本即将推出。它针对 Apple 芯片进行了优化。该应用可以打开旧版 Affinity 文件，但反之则不然。它支持多种语言，并允许在多个设备上安装。

您需要在线下载、激活和更新您的许可证，但主要功能可离线使用。需要 Canva 高级计划才能解锁 AI 功能。联系 Canva 企业版或教育版，分别为大型组织或教育机构获取 Affinity。

---

## 14. 智能创建分支名称的Git CLI工具

**原文标题**: Git CLI tool for intelligently creating branch names

**原文链接**: [https://github.com/ytreister/gibr](https://github.com/ytreister/gibr)

`gibr` 是一个命令行工具，旨在通过与问题跟踪器集成来简化 Git 分支的创建。它基于问题详情自动生成一致且描述性强的分支名称，从而改善工作流程和团队协作。

**主要特性和用法：**

*   **问题跟踪集成：** 支持 GitHub、GitLab、Jira 和 Linear（即将支持 Monday.com）。
*   **分支名称生成：** 基于可配置的格式创建分支名称，使用诸如问题类型、问题 ID 和标题之类的占位符。
*   **命令：**
    *   `gibr issues`: 列出您配置的跟踪器中的未解决问题。
    *   `gibr <issue_id>` 或 `gibr create <issue_id>`: 为特定问题创建并检出一个分支。
    *   `gibr init`: 指导您设置包含问题跟踪器凭据和设置的 `.gibrconfig` 文件。
    *   `gibr alias`: 创建 Git 别名（如 `git create`）以简化命令使用。
*   **安装：** 通过 `uv pip install gibr` 或 `pip install gibr` 安装。
*   **配置：** 使用 `.gibrconfig` 文件存储设置，包括分支名称格式和问题跟踪器详细信息。
*   **Git 别名：** 允许使用 Gibr 命令扩展 Git CLI，以便于使用。
*   **特殊的Jira处理：** 它可以自动获取配置的Jira项目密钥。

`gibr` 旨在通过自动化分支命名、确保一致性以及将分支直接链接到问题来改善开发人员的工作流程。

---

## 15. 软盘 // 复古计算

**原文标题**: Floppy Disk / Diskettes // retrocmp / retro computing

**原文链接**: [https://retrocmp.de/fdd/diskette/diskette.htm](https://retrocmp.de/fdd/diskette/diskette.htm)

本文全面概述了软盘（或称磁盘），一种复古计算的关键组成部分。内容涵盖多个方面，包括尺寸（8英寸、5.25英寸、3.5英寸和3英寸），以及硬扇区和软扇区磁盘之间的区别。3.5英寸和3英寸磁盘始终为软扇区，而带有多个索引孔的硬扇区磁盘则用于较旧的、IBM PC之前的系统中。

本文深入探讨了索引孔的功能，以3M磁盘为例说明其不同类型，并解释了8英寸和5.25英寸磁盘上写保护/启用缺口的不同工作方式。8英寸磁盘在缺口被覆盖时受到写保护，而5.25英寸磁盘在未覆盖时启用写入。

本文提供了具体示例，突出了硬扇区5.25英寸磁盘的稀有性，特别是那些具有10个扇区孔的磁盘，这些磁盘用于Heathkit H89和North Star Horizon等系统中。本文还提到了带有16个扇区孔的软盘，并列出了使用它们的计算机系统。同时列出了带有32个扇区孔的8英寸磁盘的示例。

最后，本文包含一个产品列表，展示了来自3M和boeder等制造商提供的8英寸和5.25英寸软盘，并提供了相关文档、外部资源和维基百科文章的链接，以供进一步探索。对于那些对软盘的历史和技术方面感兴趣的人来说，本文是一份宝贵的资源。

---

## 16. 不可变发布现已在 GitHub 上全面推出

**原文标题**: Immutable releases are now generally available on GitHub

**原文链接**: [https://github.blog/changelog/2025-10-28-immutable-releases-are-now-generally-available/](https://github.blog/changelog/2025-10-28-immutable-releases-are-now-generally-available/)

GitHub 宣布正式推出不可变版本，增强软件供应链安全。此功能确保版本发布后，其资产和标签受到保护，免受篡改，从而保证软件的完整性。

不可变版本的主要功能包括：

*   **不可变资产：** 防止发布后添加、修改或删除资产，防范供应链攻击。
*   **标签保护：** 保护与不可变版本关联的标签，防止删除或移动。
*   **版本证明：** 提供 Sigstore 捆绑格式的签名证明，便于在 GitHub 和外部环境中使用 GitHub CLI 等工具轻松验证真实性和完整性。

可以在存储库或组织级别启用不可变性，自动应用于所有新版本。现有版本保持可变，除非重新发布。禁用此功能不会影响现有的不可变版本。提供的文档概述了如何验证不可变版本的完整性。GitHub 鼓励用户在 GitHub Community 论坛上提供反馈。

---

## 17. 人工智能如何让我重获声音——一位艺术家对Suno Studio的评测

**原文标题**: How AI gave me my voice back – an artist's review of Suno Studio

**原文链接**: [https://blog.andyshand.com/blog/how-ai-gave-me-my-voice-back](https://blog.andyshand.com/blog/how-ai-gave-me-my-voice-back)

安迪·尚德的博客文章《AI如何让我重获声音——一位艺术家对Suno Studio的评测》探讨了AI音乐生成平台Suno对其创作过程和艺术表达产生的变革性影响。尚德，推测是一位音乐家或艺术家，讨论了Suno如何帮助他克服创作瓶颈，并重新找回对音乐的热情。

文章强调了Suno的易用性和可访问性，使所有技能水平的艺术家都能创作原创音乐。尚德强调了该平台基于简单文本提示生成各种音乐风格和流派的能力，使他能够探索未知的创作领域。

他详细阐述了Suno如何作为实验和构思的宝贵工具，为他自己的艺术诠释提供跳板。Suno并没有取代他的创作投入，而是对其进行了增强，提供了新的视角并激发了新的方向。

中心主题围绕着AI在创作过程中可以成为强大的合作者，而不是竞争对手的观点。尚德认为Suno释放了他的创作潜力，让他能够以以前无法想象的方式进行音乐表达，实际上是让他重获“声音”。他很可能以对Suno Studio的积极评价结束，倡导其他寻求重振创作力的艺术家使用它。

---

## 18. 伯蒂大脑

**原文标题**: Bertie the Brain

**原文链接**: [https://en.wikipedia.org/wiki/Bertie_the_Brain](https://en.wikipedia.org/wiki/Bertie_the_Brain)

伯蒂大脑是早期电子游戏之一，是由约瑟夫·凯茨在多伦多为1950年加拿大国家展览会建造的井字棋电脑。 这台13英尺高的机器允许参观者在灯光网格上与人工智能对手进行井字棋游戏，难度可调。玩家通过键盘输入走法。

凯茨设计伯蒂是为了展示他的加法管，一种微型真空管。 然而，专利问题和晶体管的兴起限制了它仅用于这台机器。 尽管它有可能成为第一个具有视觉显示的电子游戏，但伯蒂在展览后被拆除，并被人们遗忘。

凯茨曾在雷达管上工作并帮助建造了UTEC，他在罗杰斯·马杰斯蒂克的敦促下创造了伯蒂，以推广加法管。 该游戏在展览会上取得了成功，人们排队玩。

游戏玩法包括玩家在发光按钮的网格上选择位置，走法显示为X或O灯。 计算机反应迅速，并且被设计为在最高难度下是不可战胜的。

尽管伯蒂曾在《生活》杂志上刊登，但随着凯茨转向其他项目，它的遗产逐渐消失。 加法管的商业前景受到专利延误和晶体管兴起的阻碍。 尽管由于使用了灯泡而不是屏幕，从所有定义上来说它都不是电子游戏，但伯蒂仍然是作为最早的具有视觉输出的计算机游戏之一的一个重要里程碑。

---

## 19. Fire TV：亚马逊未来将屏蔽盗版应用

**原文标题**: Fire TV: Amazon to block piracy apps in the future

**原文链接**: [https://www.heise.de/en/news/Fire-TV-Amazon-to-block-piracy-apps-in-the-future-10964878.html](https://www.heise.de/en/news/Fire-TV-Amazon-to-block-piracy-apps-in-the-future-10964878.html)

亚马逊计划未来阻止在Fire TV设备上安装助长盗版的应用程序。此举旨在打击未经授权的版权内容流媒体播放和分发。

虽然在Fire TV上侧载应用程序一直可行，但亚马逊正在采取措施使其变得更加困难，实际上阻碍了用于访问盗版内容的应用程序的使用。文章中没有详细说明具体的阻止方法，但暗示亚马逊将采取积极措施来阻止这些应用程序的安装或功能。

这一决定符合亚马逊保护知识产权和遵守版权法的持续努力。通过打击盗版应用程序，亚马逊旨在为其用户和内容提供商创造一个更安全、更合法的流媒体环境。预计此项变更将影响依赖侧载应用程序来访问未经授权的电影、电视节目和其他媒体的用户。

---

## 20. 用于电视节目、电影和创意作品的电话号码

**原文标题**: Phone numbers for use in TV shows, films and creative works

**原文链接**: [https://www.acma.gov.au/phone-numbers-use-tv-shows-films-and-creative-works](https://www.acma.gov.au/phone-numbers-use-tv-shows-films-and-creative-works)

无法访问文章链接。

---

## 21. 耳蜗如何计算 (2024)

**原文标题**: How the cochlea computes (2024)

**原文链接**: [https://www.dissonances.blog/p/the-ear-does-not-do-a-fourier-transform](https://www.dissonances.blog/p/the-ear-does-not-do-a-fourier-transform)

本文解释了耳蜗（内耳中的听觉器官）如何处理声音。它驳斥了一种常见的误解，即耳蜗执行傅里叶变换。相反，它将耳蜗的功能描述为由基底膜促进的频率分离过程，其中不同的位置与不同的频率产生共振（音位定位）。

该过程始于声波振动鼓膜，然后由中耳骨放大并传递到充满液体的耳蜗。基底膜具有不同的硬度和重量，可在空间上分离频率。膜上的毛细胞随后通过涉及“活板门”离子通道的机械电转导过程将这些振动转化为电信号。

耳蜗采用滤波器来提取时间和频率信息，表现出一种权衡：高频以更好的时间分辨率进行处理，而低频具有更好的频率分辨率。这种权衡符合小波或Gabor滤波方案，而不是傅里叶变换的均匀频率分解。

本文重点介绍了Lewicki的研究，该研究表明，这种特定的时频权衡是自然声音的一种有效编码策略，可减少其表示中的冗余。最佳滤波器特性因声音类型（环境、动物发声或人类语音）而异，其中人类语音占据独特的时频空间。最终，本文认为耳朵已经进化为创造与生态相关的表征，优化其对生存和交流至关重要的声音的处理。 本文暗示将在下次讲座中深入探讨神经元计算的生物物理学。

---

## 22. OpenAI利用复杂循环交易推动其数十亿美元的崛起

**原文标题**: OpenAI Uses Complex and Circular Deals to Fuel Its Multibillion-Dollar Rise

**原文链接**: [https://www.nytimes.com/interactive/2025/10/31/technology/openai-fundraising-deals.html](https://www.nytimes.com/interactive/2025/10/31/technology/openai-fundraising-deals.html)

OpenAI：复杂循环融资驱动人工智能发展

文章详细介绍了在CEO萨姆·奥特曼领导下，OpenAI如何利用复杂和循环的金融交易来资助其雄心勃勃的人工智能开发。OpenAI没有采用传统的融资模式，而是从微软、软银、甲骨文、英伟达和AMD等科技公司获得数十亿美元的资金，然后利用这些资金向这些公司支付云计算、数据中心和驱动其人工智能模型所需的专用芯片费用。

微软向OpenAI投资了130亿美元，其中大部分资金又回流到微软，用于支付云计算服务费用。与CoreWeave（220亿美元用于计算能力，3.5亿美元的CoreWeave股票给OpenAI）、软银（400亿美元融资，1000亿美元数据中心）、甲骨文（3000亿美元数据中心支出由OpenAI付款回报）、阿联酋（200亿美元数据中心投资）和英伟达（1000亿美元投资）也存在类似的安排。

这些不寻常的安排引发了人们对潜在金融泡沫的担忧，因为OpenAI实际上是在抬高其表面价值，并刺激对其生存所需服务的需求。虽然专家们认识到这种创新方法，但这些交易引发了人们对财务稳定性的质疑，如果人工智能进展放缓，或者OpenAI无法产生足够的收入来抵消其巨额亏损。一些公司，如英伟达和AMD，正在对冲风险，但如果人工智能市场没有按预期扩张，CoreWeave等规模较小的公司将面临破产风险，可能造成经济连锁反应。

---

## 23. Kimi线性：一种表达力强、效率高的注意力架构

**原文标题**: Kimi Linear: An Expressive, Efficient Attention Architecture

**原文链接**: [https://github.com/MoonshotAI/Kimi-Linear](https://github.com/MoonshotAI/Kimi-Linear)

Kimi Linear：一种用于长文本任务的新型线性注意力架构

---

## 24. 亚马逊称裁员并非因为缺钱，而是因为“文化”。

**原文标题**: Amazon says it didn't cut people because of money. But because of 'culture'

**原文链接**: [https://www.cnn.com/2025/10/30/tech/amazon-layoffs-andy-jassy-ai-culture](https://www.cnn.com/2025/10/30/tech/amazon-layoffs-andy-jassy-ai-culture)

亚马逊CEO贾西将近期裁员14000人归因于文化因素，而非财务困境或人工智能的直接影响。他声称，近年来快速扩张导致员工人数增加、管理层级增多以及员工主人翁意识减弱。贾西认为，这阻碍了公司作为领导团队的敏捷性和速度。

贾西表示，亚马逊的目标是像大型初创企业一样运作，因此需要移除官僚主义层级。虽然该公司强调需要保持敏捷，以应对未来人工智能效率的提升，但裁员引发了人们对技术取代人类劳动的担忧。

尽管裁员，亚马逊季度销售额同比增长13%至1800亿美元，财报发布后，公司股价盘后上涨13%。该公司员工人数在2021年达到160万的峰值，去年年底为150万。文章强调了亚马逊裁员的声明原因（文化）与科技行业中日益增长的对人工智能影响就业保障的担忧之间的差异。

---

## 25. 自由软件吓坏普通人

**原文标题**: Free software scares normal people

**原文链接**: [https://danieldelaney.net/normal/](https://danieldelaney.net/normal/)

这篇短文认为自由软件会令“普通人”感到畏惧和害怕。虽然原文未提供任何支持细节或解释，但其隐含的假设是自由软件的某些方面令普通用户感到反感。

基于常见误解和担忧，这种恐惧的可能原因包括：

*   **复杂性：** 自由软件通常被认为比专有软件更难使用和配置。技术术语和缺乏完善的用户界面可能会让人望而却步。
*   **缺乏支持：** 用户可能会担心遇到问题时，无法获得可靠的支持。基于社区的支持模式虽然通常有效，但可能不如专门的客户服务那样令人安心。
*   **安全顾虑：** 一些人可能会将自由软件与缺乏安全性联系起来，担心由于其开源性质，它更容易受到恶意软件或黑客攻击（尽管情况往往恰恰相反）。
*   **“免费”被视为劣质：** “免费”一词可能会让一些人认为该软件的质量或可靠性低于付费替代品。
*   **许可和自由：** 对于那些只想软件能用的人来说，软件许可和用户自由的概念可能令人困惑或被认为是不必要的。
*   **伦理考量：** 一些人并不优先考虑自由软件的伦理和哲学方面，认为这与他们的需求无关。

由于源文章中没有进一步的阐述，对这种被感知到的恐惧的原因仍然是推测性的，但核心在于“普通人”的用户期望与自由软件的感知现实之间存在脱节。

---

## 26. 压电晶体的深入观察

**原文标题**: A Closer Look at Piezoelectric Crystal

**原文链接**: [https://www.samaterials.com/content/a-closer-look-at-stressed-piezo-crystals.html](https://www.samaterials.com/content/a-closer-look-at-stressed-piezo-crystals.html)

本文全面概述了压电晶体，重点介绍其特性、原理和应用。文章首先将压电晶体定义为非中心对称材料，该材料在受到机械应力时会产生电场，反之亦然。这种在机械能和电能之间转换的独特能力使其在传感器技术和能量转换方面具有重要价值。

文章解释了压电效应，即机械力使晶体变形并产生表面电荷，以及逆压电效应，即电场引起机械变形。它还详细介绍了晶体结构的特征，强调了非中心对称结构和极化处理对于最大化压电性能的重要性。

文章详细描述了极化过程，即通过加热并施加强电场来排列电偶极子。然后，文章重点介绍了两种常见的压电材料：石英和钛酸钡，并讨论了它们的特性和各种应用。石英因其稳定性和在振荡器、滤波器和传感器中的应用而备受重视。钛酸钡因其高压电常数而用于电容器、压力传感器和医疗超声。

本质上，文章强调了压电晶体在现代技术中的重要作用，涵盖电子、传感器到医疗和工业应用。

---

## 27. NPM恶意软件包泛滥，下载次数超过8.6万次

**原文标题**: NPM flooded with malicious packages downloaded more than 86k times

**原文链接**: [https://arstechnica.com/security/2025/10/npm-flooded-with-malicious-packages-downloaded-more-than-86000-times/](https://arstechnica.com/security/2025/10/npm-flooded-with-malicious-packages-downloaded-more-than-86000-times/)

安全公司Koi发现了一场广泛的恶意活动，代号“幻影渡鸦”(PhantomRaven)，利用了NPM处理“远程动态依赖”(RDD)的漏洞。自8月以来，攻击者已向NPM仓库上传了126个恶意软件包，下载次数超过86000次，截至周三，大约还有80个处于活跃状态。

该漏洞在于NPM允许软件包通过潜在未加密的HTTP连接自动从不受信任的来源下载依赖项，绕过传统的安全扫描，并使恶意依赖项对开发人员“隐形”。这些依赖项在每次安装时都会“新鲜”下载，使攻击者能够根据请求源提供不同的有效载荷，从而实现有针对性的攻击。

这些恶意依赖项会在受感染的系统中搜寻敏感数据，包括环境变量、GitHub、Jenkins和NPM凭据，以及整个持续集成/持续交付环境，为后续的供应链攻击打开了大门。数据外泄采用了多种方法以实现冗余。

“幻影渡鸦”还使用了由AI聊天机器人识别的幻觉依赖项名称，以进一步混淆其活动。NPM代表尚未回应置评请求。经常从NPM下载软件包的读者应查看Koi的帖子，了解入侵指标。

---

## 28. 原生 CSS 中的弹簧和反弹效果

**原文标题**: Springs and bounces in native CSS

**原文链接**: [https://www.joshwcomeau.com/animation/linear-timing-function/](https://www.joshwcomeau.com/animation/linear-timing-function/)

本文探讨了在 CSS 中使用 `linear()` 时间函数创建更复杂的动画，如弹簧和弹跳效果，这些效果以前只能通过 JavaScript 实现。

`linear()` 函数允许开发者通过在图表上指定一系列点来定义自定义缓动曲线，并在这些点之间创建直线段。这使得创建非贝塞尔曲线动画（如过冲和弹跳的弹簧）成为可能。虽然可以手动创建这些动画，但本文建议使用诸如 Linear() Easing Generator 和 Easing Wizard 之类的工具，这些工具可以从弹簧参数动态生成优化的 `linear()` 字符串。这些工具通常使用高级语法，其中包含时间百分比，以便进行战略性点放置。

本文承认了一些局限性，包括需要固定持续时间（与基于物理的 JS 动画不同）以及 CSS 过渡中潜在的中断处理问题。性能测试表明，复杂的 `linear()` 值不会显着影响帧速率，并且只会增加少量 CSS 包大小。

本文建议将常用的 `linear()` 时间函数存储在 CSS 变量中以供重用，并为旧版浏览器提供使用 `cubic-bezier()` 曲线的后备方案。它还强调了尊重用户运动偏好的重要性。

---

## 29. Show HN: Quibbler – 一个能学习你需求的编码代理的评论家

**原文标题**: Show HN: Quibbler – A critic for your coding agent that learns what you want

**原文链接**: [https://github.com/fulcrumresearch/quibbler](https://github.com/fulcrumresearch/quibbler)

Quibbler: 一个代码审查工具，自动观察并纠正代码代理的行为，以提高代码质量和用户指令的遵循度。它能防止常见的代理错误，如捏造结果、跳过测试、忽略编码风格和虚构信息。

Quibbler 集成有两种模式：Hook 模式，专为 Claude Code 用户设计，利用其 Hook 系统进行被动事件监控和反馈注入；以及 MCP 模式，与其它代码代理普遍兼容，使用模型上下文协议进行同步代码审查和即时反馈。

设置包括配置 MCP 服务器设置或在项目中添加 Hook。 Quibbler 为每个项目或会话维护一个持久审查代理，审查代码更改、验证声明、检查文件更改并验证测试步骤。它会学习项目模式并随时间保存规则，从而改进其审查能力。 用户可以通过模型全局或项目特定的配置文件和自定义提示来自定义代理的行为。 Quibbler 默认使用 Claude Haiku 4.5，但可以配置为使用其他 Claude 模型。

该工具向代理提供反馈，然后代理会调整其行为。 Hook 模式会将反馈写入代理读取的特定消息文件，并由代理系统提示中的占位符引导。目标是自动化代码审查，并确保编码代理始终如一地遵循指令并保持代码质量。

---

## 30. 弗洛里安·施耐德收藏：乐器及设备拍卖

**原文标题**: Florian Schneider Collection: Instruments and equipment up for auction

**原文链接**: [https://www.juliensauctions.com/en/articles/the-florian-schneider-collection-rare-instruments-and-iconic-equipment-from-kraftwerk](https://www.juliensauctions.com/en/articles/the-florian-schneider-collection-rare-instruments-and-iconic-equipment-from-kraftwerk)

无法访问文章链接。

---

## 31. 结果是我唯一需要的

**原文标题**: Result is all I need

**原文链接**: [https://rockyj-blogs.web.app/2025/10/25/result-monad.html](https://rockyj-blogs.web.app/2025/10/25/result-monad.html)

本文探讨了软件开发向人工智能辅助的转变，以及即使在使用人工智能生成的代码的情况下，代码组织对于可维护性和质量的重要性。作者建议将代码结构化为不同的层：接口层（控制器、数据库、HTTP客户端）和服务层（业务逻辑切片）。关键是保持每一层无状态、隔离，并专注于单一职责。

文章随后介绍了“Result”monad，作为在连接这些服务函数时处理异常和空值的一种方法。作者认为，使用“Result”通过提供一致的错误处理和空值检查方法，使代码更具声明性、更安全且更易于维护。

“Result”允许使用`flatMap`将函数链接在一起，透明地处理潜在的错误和空值，而不是嵌套的if/else和try/catch块。文章提供了一个使用“Result”进行用户注册和登录功能的Kotlin示例，并将其与命令式方法进行了对比。

作者强调，“Result”是一个促进函数式编程原则的包装器，从而产生更简洁、更模块化和可测试的代码。虽然最初看起来更复杂，但可以一致地应用“Result”模式，从而减少样板代码并提高整体代码质量。最后，作者建议该代码可以用各种其他语言实现，并且可以将基础和服务层代码以安全的方式链接起来，以获得良好的结果。

---

## 32. 只需一个按钮

**原文标题**: Just Use a Button

**原文链接**: [https://gomakethings.com/just-use-a-button/](https://gomakethings.com/just-use-a-button/)

本文反对一种常见做法，尤其是在 React 和 HTMX 开发者中，即使用带有 `onclick` 属性的 `<div>` 元素来模仿按钮功能，而不是使用原生的 `<button>` 元素。

作者强调了这种做法存在的若干可访问性和可用性问题。`<div>` 本身并不能向屏幕阅读器表明其交互性质，默认情况下无法通过键盘聚焦，且不响应 Enter 或 Spacebar 键的按下。

虽然开发者经常尝试通过添加 `role="button"` 和 `tabindex="0"` 等属性，以及附加键盘输入事件监听器来“修复”这些缺陷，但作者认为这些修复既繁琐又容易出错，最终只是重新创建了 `<button>` 元素已有的功能。本文批评了手动使用 `tabindex` 管理焦点顺序的做法，因为这有破坏预期导航流程的风险。此外，键盘交互性的修复涉及到复杂的事件处理。

作者强调了开发中的懒惰原则：使用正确的 HTML 元素来实现其预期目的可以避免不必要的代码和潜在问题。一个 `<button>` 元素本身就具备正确的角色，可以自动聚焦，并在按下 Enter 和 Spacebar 键时触发点击事件，与自定义的 `<div>` 相比，提供了卓越的可访问性和易于实现的特性。本质上，建议很简单：利用 HTML 元素的内置功能，而不是重复造轮子。

---

## 33. Minecraft HDL，红石的硬件描述语言

**原文标题**: Minecraft HDL, an HDL for Redstone

**原文链接**: [https://github.com/itsfrank/MinecraftHDL](https://github.com/itsfrank/MinecraftHDL)

Minecraft HDL 是一个工具，它可以从 Verilog 代码中合成数字电路，并将其转化为 Minecraft 环境中可工作的红石电路。 作为本科毕业设计，它的目的是以宏观尺度展示数字电路设计的原理，使其成为初学者和本科工程学生的教育工具。

尽管该工具几乎可以合成任何 Verilog 电路，但它也存在局限性。 与手工搭建的红石电路相比，它生成的电路效率较低，并且由于 Minecraft 中的尺寸限制，不适合改装的生存模式。 此外，它无法合成时序电路（带有反馈回路的电路），这意味着无法实现内存或有状态的设计。

尽管存在这些局限性，Minecraft HDL 仍然为数字设计过程提供了一个实践演示，弥合了理论概念和有形的、交互式环境之间的差距。 创作者通过一个 GIF 展示了 2 位加法器电路的快速创建和实现，证明了其易用性。 该项目旨在作为一个教育工具，说明微电子数字电路是如何设计的，并强调软件和硬件设计之间的差异。

---

## 34. 改进类型检查器的路线图

**原文标题**: Roadmap for Improving the Type Checker

**原文链接**: [https://forums.swift.org/t/roadmap-for-improving-the-type-checker/82952](https://forums.swift.org/t/roadmap-for-improving-the-type-checker/82952)

本文概述了 Swift 团队改进编译器表达式类型检查的路线图，特别是解决常见的“无法在合理时间内检查此表达式的类型”错误。核心问题源于基于类型的重载，编译器通过约束求解来处理它。这个过程涉及创建类型变量和约束，包括重载声明的“析取约束”。析取约束的固有复杂性导致指数级最坏情况算法复杂度。

编译器通过操作计数器和内存池大小来限制处理时间。抢救模式有助于为无效表达式生成诊断信息。主要目标是开发通用启发式方法，通过优先考虑析取选择和避免矛盾来快速解决实际问题，而不是为特定情况硬编码解决方案。次要目标是优化约束求解器的数据结构和算法。

Swift 6.2 最近的改进侧重于分析和解决回溯和图算法等领域的瓶颈，从而带来了一些性能提升。Swift 6.3 引入了优化的析取选择，使编译器能够快速解决以前无法进行类型检查的表达式，尤其是涉及数学运算符和文字的表达式。此外，一项正在开发中的优化（默认情况下禁用）旨在通过预先生成泛型重载的类型变量和约束来减少内存池使用量，从而可能将指数空间问题转换为多项式空间问题。

---

## 35. Show HN: 我做了一个用于代码审查的热图差异查看器

**原文标题**: Show HN: I made a heatmap diff viewer for code reviews

**原文链接**: [https://0github.com](https://0github.com)

这个“Show HN”帖子介绍了一个名为 cmux 的“热图差异查看器”，旨在通过突出显示需要更多人工关注的行/标记来提高代码审查效率。与典型的错误查找机器人不同，cmux 的目标是突出显示值得再三检查的代码段，即使它们不是明显的错误（例如，硬编码的密钥、复杂的逻辑）。

该工具的工作原理是在 GitHub pull request URL 中将 "github.com" 替换为 "0github.com"。这会触发一个流程，将存储库克隆到 VM 中，GPT-5-codex 分析每个差异，并输出一个 JSON 数据结构，用于生成彩色热图。

该帖子提供了可测试 cmux 的示例 pull request，包括 `tinygrad`、`datasette` 和 `cmux` 本身的 pull request。 热图差异查看器是开源的，并且提供了 GitHub 存储库链接。 基本上，cmux 旨在引导审查者专注于代码更改中最关键的部分，从而可能节省时间并提高代码质量。

---

## 36. 丹麦据报在争议后撤回聊天控制提案

**原文标题**: Denmark reportedly withdraws Chat Control proposal following controversy

**原文链接**: [https://therecord.media/demark-reportedly-withdraws-chat-control-proposal](https://therecord.media/demark-reportedly-withdraws-chat-control-proposal)

丹麦在面临强烈争议后，撤回了其强制扫描包括端到端加密平台在内的电子信息的欧盟法律提案。该提案名为“聊天控制”，旨在打击儿童性虐待材料 (CSAM) 贩运。

德国政府决定反对该提案，实际上结束了丹麦的努力。丹麦司法部长彼得·胡梅尔高宣布，他的办公室将转而支持自愿CSAM检测，并强调如果不采取行动，可能会失去打击儿童性虐待的关键工具，因为当前的自愿扫描模式将于四月到期。

Signal基金会主席梅瑞狄斯·惠特克强烈反对最初的措施，警告说如果该措施获得通过，Signal将退出欧洲市场。她批评这是大规模监控，会损害包括政府官员、记者和活动家在内的各类人士的隐私。文章强调了在数字时代打击CSAM和保护隐私权之间的紧张关系。

---

## 37. 杰克·凯鲁亚克、马尔科姆·考利与《在路上》的艰难诞生

**原文标题**: Jack Kerouac, Malcolm Cowley, and the difficult birth of On the Road

**原文链接**: [https://theamericanscholar.org/scrolling-through/](https://theamericanscholar.org/scrolling-through/)

杰拉尔德·霍华德的文章深入探讨了杰克·凯鲁亚克的小说《在路上》从构思到出版的艰难历程，打破了其纯粹自发创作的神话。 凯鲁亚克的确曾在狂热的20天里用打字机打出了一卷120英尺长的纸卷，但这建立在多年的准备工作之上，包括详细的笔记、人物年表和早期的草稿。 这部小说反映了垮掉的一代在战后美国寻找意义，受爵士乐和凯鲁亚克与尼尔·卡萨迪的横跨美国旅行的影响。

在遭到多家出版社的拒绝后，这份手稿最终落到了维京出版社，编辑马尔科姆·考利对它表示支持。 考利认识到凯鲁亚克的天赋以及这部小说作为垮掉一代声音的重要性，堪比海明威对迷惘一代的代表。 然而，由于书中露骨的性内容、潜在的诽谤问题以及非传统的风格，维京出版社犹豫不决。 考利花了四年时间为出版辩护，最终说服维京冒险出版这部小说。 他认为这是一部开创性的作品，捕捉了新一代的躁动不安和对身份的追寻。 在凯鲁亚克成功之前，约翰·克莱隆·福尔摩斯已经通过他的小说《走》和一篇《纽约时报杂志》的文章，将垮掉的一代带到了公众的视野中。

---

## 38. Julia 中的透镜

**原文标题**: Lenses in Julia

**原文链接**: [https://juliaobjects.github.io/Accessors.jl/stable/lenses/](https://juliaobjects.github.io/Accessors.jl/stable/lenses/)

Julia中的Lens（使用Accessors.jl包）提供了一种以非破坏性方式访问和修改复杂对象中深层嵌套部分的机制。 Lens允许您`get`对象的特定部分，并为该部分`set`一个新值，从而创建原始对象的修改副本。

可以使用`@optic`宏以简洁的语法（例如，`@optic _.a[1]`）创建Lens，也可以使用`opcompose`、`PropertyLens`和`IndexLens`等函数以编程方式构建Lens。可以使用`opcompose`、`⨟`或`∘`创建组合的Lens。

要定义自定义Lens，您需要实现两个函数：`Accessors.set(obj, lens, val)`（返回`obj`的修改副本，并具有指定的值）和`lens(obj)`（检索Lens针对的值）。

至关重要的是，Lens的实现必须遵守三个定律：“您得到了您所设置的”，“设置已经存在的内容不会改变任何内容”和“最后一次设置获胜”。这些定律确保了在使用Lens时，特别是在多次设置值时，可预测和一致的行为。 相等（`≅`）的概念可以是灵活的，可以根据上下文和数据类型使用`==`，`===`，`isequal`或`≈`。

---

## 39. 鲁伊勒 – 法语中的 Rust 编程

**原文标题**: Rouille – Rust Programming, in French

**原文链接**: [https://github.com/bnjbvr/rouille](https://github.com/bnjbvr/rouille)

Rouille：一个幽默的 Rust 法语化项目，旨在创建一个法语版本的 Rust 编程语言。它允许开发者使用法语关键字、函数名和习惯用语来编写 Rust 代码，甚至可以与标准的英语 Rust 混合使用。作者将其设想为一个未来法国主权操作系统中略带戏谑的提案。

该项目提供了诸如 `trait` 变为 `convention`、`impl` 变为 `réalisation` 等关键字的翻译示例。它还包括针对不同法语地区的本地化脏话，以实现“真正的法语体验”。

该项目鼓励以添加更多法语标识符的形式进行贡献，同时也提醒贡献者不要包含过多的亵渎性语言。作者解释说，该项目是对原始过程宏的一种轻松探索，并且是对具有本地化语法的编程语言的一种幽默诠释，同时也承认了它们的潜在效用。

除了法语之外，该文档还列出了许多其他语言中的“rust”一词，暗示了一个潜在的“unirust”项目，以在多种语言中本地化 Rust。

该项目徽标由 @VentGrey 创建，许可协议为“License Publique Rien à Branler”，即 WTFPL 的法语翻译。

---

## 40. 改装辐射计用于（放射性）岩石收集

**原文标题**: Modifying a radiation meter for (radioactive) rock collecting

**原文链接**: [https://maurycyz.com/projects/ludlum3/](https://maurycyz.com/projects/ludlum3/)

本文详细介绍了一种改进 Ludlum Model 3 辐射仪的方法，以提高其在放射性岩石收集中的实用性，尤其是在与灵敏闪烁探测器一起使用时。问题在于，闪烁探测器虽然擅长探测穿过泥土和岩石的伽马射线，但会产生很高的本底计数率，导致音频反馈过于强烈，并且模拟仪表读数难以解读。

解决方案是将微控制器与 Ludlum Model 3 连接。微控制器测量计数率，减去校准后的本底读数，并输出一个音频音调，其频率对应于高于本底的辐射水平。这使得用户可以通过声音追踪辐射水平的细微增加，而这些增加原本会被本底噪声所掩盖。

本文提供了关于接入 Ludlum Model 3 电源和事件信号的详细说明，包括不同仪表版本之间的潜在差异。它强调了在高压元件上工作时的电气安全的重要性，并建议进行仔细的布线和绝缘。

作者提供了微控制器程序的源代码和预构建二进制文件，以及关于如何编程微控制器的说明，甚至使用容易获得的零件即兴制作了一个 UPDI 编程器。这种改进对于具有中等本底计数率的较大闪烁探测器尤其有效。最终产品会发出一种音调，其频率引导用户找到辐射源，从而改善寻石体验。本文还包括常见问题的故障排除技巧。

---

## 41. 从BitTorrent导入Node模块

**原文标题**: Importing Node Modules from BitTorrent

**原文链接**: [https://evanhahn.com/node-torrent-import/](https://evanhahn.com/node-torrent-import/)

Evan Hahn 的文章探讨了使用 Node.js 的新自定义钩子功能直接从 BitTorrent 导入 Node.js 模块的可能性。他创建了一个名为“torrent-import”的模块，该模块允许从 .torrent 文件或磁力链接导入 JavaScript 文件。

Hahn 选择 BitTorrent 来试验内容寻址模块，它提供了诸如保存（绕过对 npm 等中心化注册表的依赖）以及通过哈希实现内置数据完整性等优势。他详细介绍了自定义钩子如何允许覆盖 Node.js 中的默认模块加载行为。

该文章解释了如何创建和注册自定义钩子，并通过一个简化的示例演示了如何将 .torrent 导入重定向到伪造文件。然后，他说明了如何在钩子中使用 WebTorrent 将 torrent 数据下载到磁盘并解析到已下载 JavaScript 文件的路径。他还提到将一个简单的模块作为 torrent 发布到 Internet Archive 以进行测试。

尽管具有功能，Hahn 承认 torrent-import 只是一个具有局限性的概念验证。他指出了由于自定义钩子的新生性质导致的不稳定性、与 SHA-1 相关的潜在安全漏洞、非同构行为、缺乏工具支持、依赖 seeder 可用性、与 torrent 相关的负面含义以及普遍缺乏润色等问题。他希望这项实验能够引发关于自定义钩子以及类似 BitTorrent 的技术在包管理中的潜力的讨论。

---

## 42. 发布 HN：蜂胶 (YC X25) - 自动 QA 您的 Web 应用程序的浏览器代理

**原文标题**: Launch HN: Propolis (YC X25) – Browser agents that QA your web app autonomously

**原文链接**: [https://app.propolis.tech/#/launch](https://app.propolis.tech/#/launch)

Propolis推出自主QA工具，利用浏览器代理自动测试Web应用。

---

## 43. 手性物质的卓越测量

**原文标题**: Exceptional Measurement of Chirality

**原文链接**: [https://www.rsc.org/news/2019/july/exceptional-measurement-of-chirality](https://www.rsc.org/news/2019/july/exceptional-measurement-of-chirality)

本文重点介绍振动圆二色性(VCD)光谱学的一项突破，该突破能够在实际条件下对分子手性（旋向性）进行更准确和可靠的测量。手性分子或对映异构体彼此互为镜像，并且与生物系统相互作用的方式可能不同，因此它们的识别至关重要，尤其是在制药领域。沙利度胺药物惨痛地提醒我们，不了解手性的危害。

这项新技术克服了传统VCD方法的局限性，这些方法难以处理柔性和动态分子。 以前，VCD依赖于跨可能分子构型的理论指纹图谱的平均值，从而导致可能错误地识别手性。 研究人员开发了一种算法，该算法将不确定性而不是平均值引入到计算的分子能量中。 这种基于进化原理的“遗传”算法，可以更准确地分配手性，并提供手性分配可靠性的定量衡量标准。

通讯作者Wybren Jan Buma表示，这种新方法为确定分子的手性提供了一种更可靠的方法。 该研究表明，VCD是一种易于使用且用途广泛的技术，为实时监测生化过程和药物化合物的高通量筛选打开了大门。 该研究发表在《化学科学》杂志上，DOI：10.1039/C9SC02866H1。

---

## 44. 推理模型：行则善，不行则败

**原文标题**: Reasoning Models Reason Well, Until They Don't

**原文链接**: [https://arxiv.org/abs/2510.22371](https://arxiv.org/abs/2510.22371)

Rameshkumar 等人的 arXiv 文章《推理模型擅长推理，直到它们不再擅长》调查了大型推理模型 (LRM) 的局限性，这些 LRM 是针对逐步推理和自我验证进行微调的 LLM。虽然 LRM 在现有的推理基准上表现出良好的性能，但作者认为这些基准的复杂性有限。

为了解决这个问题，作者引入了深度推理数据集 (DeepRD)，它具有生成过程，可以提供具有可扩展复杂性的无限示例。使用 DeepRD 来评估 LRM 在图连通性和自然语言证明规划方面的能力，他们发现一旦问题复杂度超过某个阈值，LRM 的性能就会急剧下降，表明缺乏泛化能力。

该研究进一步将 LRM 的性能与现实世界知识图谱、交互图谱和证明数据集的复杂性分布进行了比较。分析表明，虽然许多现实世界的例子都落在 LRM 的能力范围内，但很大一部分存在于 LRM 无法处理的“长尾”中。

总而言之，该论文强调了 LRM 目前在推理任务中的实用性，但强调了开发新方法的关键需求，这些方法可以推广到训练数据中存在的复杂性之外，以处理更复杂、现实世界的场景。该研究表明，LRM 尽管取得了进展，但在处理具有足够深度和复杂性的问题时仍然存在困难，敦促该领域突破当前的局限性。

---

## 45. 陶哲轩在联邦政府暂停对加州大学洛杉矶分校的资助后，专注于筹款。

**原文标题**: Terence Tao focused on fundraising after federal funding to UCLA was suspended

**原文链接**: [https://www.washingtonpost.com/science/2025/09/07/science-math-trump-federal-cuts-grants/](https://www.washingtonpost.com/science/2025/09/07/science-math-trump-federal-cuts-grants/)

无法访问文章链接。

---

## 46. 像大佬一样调试：开发者、质量工程师和测试人员的10个调试技巧

**原文标题**: Debug like a boss: 10 debugging hacks for developers, quality engineers, testers

**原文链接**: [https://www.ministryoftesting.com/articles/debug-like-a-boss-10-debugging-hacks-for-developers-quality-engineers-and-testers](https://www.ministryoftesting.com/articles/debug-like-a-boss-10-debugging-hacks-for-developers-quality-engineers-and-testers)

像老板一样调试：10个给开发者、质量工程师和测试人员的实用调试技巧。核心信息是系统地进行调试并质疑假设。

以下是这些技巧的总结：

1. **质疑假设：** 在深入代码之前，识别并测试关于 API 响应、配置和条件的假设。
2. **使用打印语句：** 即使不够优雅，也使用打印语句来输出原始数据，以揭示变量的实际状态。
3. **识别变更：** 利用版本控制工具，如 `git diff` 和 `git blame`，来精确定位可能引入 bug 的最新代码变更。
4. **故意破坏：** 有意地破坏代码以隔离问题区域并了解其依赖关系。
5. **解释 Bug：** 向某人（或像橡皮鸭这样的东西）清楚地表达问题会迫使你清晰地思考，并且常常能揭示解决方案。
6. **信任堆栈跟踪：** 优先考虑堆栈跟踪而非错误消息，因为它们能指向问题的根源。
7. **重现 Bug：** 一致的重现是修复 bug 的关键。
8. **有效使用日志：** 过滤日志，使用关联 ID，并设置警报。
9. **检查外部组件：** 验证 API、数据库和内容交付系统的行为。
10. **适当休息：** 暂时远离问题，让你的大脑重新思考问题。

文章强调了事后分析、完善的文档记录和测试用例创建的重要性。文章最后鼓励读者开发自己的调试技术，并与社区分享。最后，文章鼓励读者尝试“橡皮鸭调试法”，故意破坏，并测量自己的速度下降情况，以提高调试效率。

---

## 47. 埃及大博物馆即将盛大开放，历经延误后。

**原文标题**: After delays, Egypt set for lavish opening of grand museum

**原文链接**: [https://phys.org/news/2025-10-delays-egypt-lavish-grand-museum.html](https://phys.org/news/2025-10-delays-egypt-lavish-grand-museum.html)

埃及大埃及博物馆（GEM）将于周六正式开放，此前已延误多年。 盛大的开幕式旨在促进该国的旅游业。 这座耗资超过10亿美元、历时二十年打造的超现代博物馆，可欣赏吉萨金字塔的全景，并收藏了数千件跨越5000年的埃及文物，包括前所未见的文物。 当局预计每年将有500万游客。

就职典礼笼罩在神秘之中，承诺有“国王、王子、国家元首和政府领导人”出席。 图坦卡蒙黄金面具的新展览也尚未公开。 从周二开始，博物馆将向公众开放，展示4500件丧葬物品。

塞西总统强调了GEM的“象征意义”，设想它成为一个促进旅游业的国际文化和科学中心。 马德布利总理通过GEM强调了埃及作为“文明摇篮”的作用。

原计划于七月开放，但由于地区冲突而被推迟。 该项目此前也因政治动荡和疫情而面临挫折。 为了扩大其影响力，埃及正在与TikTok合作分享其历史。

埃及的旅游业雇佣了大约10%的劳动力，正在复苏，2023-2024财年的收入达到144亿美元。 2025年前九个月接待了1500万游客，创造了125亿美元的收入，比上一年增长了21%。

---

## 48. 圆珠笔80周年：一支简单的笔如何改写日常生活

**原文标题**: The Biro turns 80: How a simple pen rewrote everyday life

**原文链接**: [https://newatlas.com/technology/biro-pen-80th-anniversary/](https://newatlas.com/technology/biro-pen-80th-anniversary/)

本文庆祝比罗圆珠笔问世80周年，突出其对日常生活的变革性影响。20世纪30年代，拉兹洛·比罗发明了圆珠笔，解决了早期书写工具（如羽毛笔和钢笔）的局限性，这些工具既脏乱、昂贵又难以使用。比罗的设计采用在插槽中滚动的小球来分配粘稠、快干的墨水，彻底改变了书写方式。

本文追溯了比罗从匈牙利逃离日益增长的法西斯政权到阿根廷寻求销售其发明的历程。在经历了各种挑战和复杂情况后，圆珠笔因其在二战期间英国皇家空军高海拔地区的可靠性而获得认可。战后，该设计进行了调整，竞争随之而来，但马塞尔·比奇大规模生产的廉价 Bic Cristal 使圆珠笔无处不在。

比罗圆珠笔的影响超越了便利性。它使书写大众化，使其在各种表面上都能轻松访问和使用。这种简单性也巧妙地改变了书写风格，块状字母变得更加普遍，而草书则越来越少。本文最后强调了比罗圆珠笔对书面交流的重大贡献，将其影响与印刷机的发明相提并论。尽管它很简单，但比罗圆珠笔从根本上改变了我们书写和与文字互动的方式。

---

## 49. Show HN: 用单个HTML文件编写的鼓励孩子投资的应用

**原文标题**: Show HN: In a single HTML file, an app to encourage my children to invest

**原文链接**: [https://roberdam.com/en/dinversiones.html](https://roberdam.com/en/dinversiones.html)

作者发布了一个“Show HN”帖子，详细介绍了如何创建一个简单的、单HTML文件的Web应用程序“D-investments”，以教导孩子们关于投资和复利的知识。由于对学校不教授个人理财感到沮丧，作者希望创建一个可视化和互动的方式，让孩子们了解他们的钱如何随着时间的推移而增长。

最初考虑使用带显示器的实体存钱罐，但他选择了更便宜、更快捷的解决方案：使用旧智能手机并创建一个PWA（渐进式Web应用）。该应用程序通过链接访问，像原生应用程序一样安装在手机上，并安装在冰箱上。

该应用程序允许输入关键信息，包括孩子们的姓名、投资金额、利率和开始日期。然后它会自动计算和显示每日、每周和每月的收益，以及更新后的总余额。作者扮演他们“投资代理人”的角色，设定实际的利率。

目标是以可视化的方式展示复利的威力和长期投资的好处，希望在孩子们心中灌输对财务增长的终身理解。作者鼓励提出反馈和改进建议。

---

## 50. Windows KB5067036更新后，任务管理器无法通过关闭按钮退出

**原文标题**: Task Manager won't exit with the close button after Windows KB5067036 update

**原文链接**: [https://old.reddit.com/r/Windows11/comments/1oj7vd1/psa_windows_11_25h2_262007019_taskbar_manager/](https://old.reddit.com/r/Windows11/comments/1oj7vd1/psa_windows_11_25h2_262007019_taskbar_manager/)

无法访问文章链接。

---

## 51. Show HN: 前端模糊、子字符串及前缀搜索

**原文标题**: Show HN: Front End Fuzzy and Substring and Prefix Search

**原文链接**: [https://github.com/m31coding/fuzzy-search](https://github.com/m31coding/fuzzy-search)

此“Show HN”帖子介绍`@m31coding/fuzzy-search`，一个用于模糊搜索、子字符串搜索和前缀搜索的前端库。它旨在快速、准确、多语言、灵活、可靠且通用，可在前端和后端（Node.js）环境中工作。

该库允许按ID和术语（名称、特征）搜索对象。主要功能包括使用名称和特征索引实体、更新/删除实体，以及执行具有可自定义质量阈值的不同类型的搜索（模糊搜索、子字符串搜索、前缀搜索）。

该库使用后缀数组和n-gram以及字符排序来实现准确的结果。它处理规范化，包括小写、NFKC/NFKD规范化和字符替换，这对于多语言支持尤其重要。模糊搜索采用排序的3-gram来改进对换位错误的控制。子字符串和前缀搜索由高效的后缀数组实现提供支持。

该帖子包括安装说明 (npm)、使用 ESM 语法的示例，并解释了重要的配置，如规范化和模糊搜索参数。它还讨论了 upsert/删除优化，以及如何使用 Web Worker 处理大型数据集。作者强调，查询已针对速度进行了优化，但由于内部索引机制，使用大型数据集进行 upsert/删除操作可能会很昂贵。

最后，该帖子鼓励用户为项目点赞支持，并通过创建 GitHub issue 来贡献改进。

---

## 52. 在轨道中，减速才能加速

**原文标题**: In orbit you have to slow down to speed up

**原文链接**: [https://www.wired.com/story/in-orbit-you-have-to-slow-down-to-speed-up/](https://www.wired.com/story/in-orbit-you-have-to-slow-down-to-speed-up/)

本文解释了轨道力学的反直觉性，展示了航天器机动经常产生与陆地经验预期相反的效果的原因。文章首先概述了控制圆形轨道的基本物理原理：向心加速度、引力以及牛顿第二定律，最终得出了一个关联轨道速度和半径的公式。

随后，文章使用一个假想的对接场景来说明其中的挑战。向前启动推进器以“追赶”空间站实际上会增加航天器的轨道半径，导致其反而*更加*落后。相反，向后启动推进器会*减小*轨道半径，从而使航天器（相对于初始轨道）加速并赶上空间站。

文章介绍了霍曼转移作为改变轨道半径的解决方案。这包括两个步骤：首先，减速进入一个更靠近地球的椭圆轨道（为了赶上）。其次，在近拱点（最近点）*再次*减速，使轨道在新高度处圆形化。

最后，文章强调行星际旅行与轨道交会类似，需要类似的操作来在围绕太阳的轨道之间切换。作者最后将此与赛车驾驶中看似矛盾的“向右转才能向左走”的建议进行类比，突出了轨道导航的“相反世界”性质。

---

## 53. 独立验证Go的可复现构建

**原文标题**: Independently verifying Go's reproducible builds

**原文链接**: [https://www.agwa.name/blog/post/verifying_go_reproducible_builds](https://www.agwa.name/blog/post/verifying_go_reproducible_builds)

本文详细介绍了作者为独立验证Go工具链可复现性所做的努力，这是Go 1.21中引入的一项功能。该功能允许`go`命令在模块需要时自动下载和使用更新的Go工具链，通过确保每个Go版本都可以从源代码可复现地构建，从而解决对供应链攻击的担忧。

Go项目在Go校验和数据库中发布工具链校验和。作者使用名为Source Spotter的工具，独立验证从源代码构建的工具链是否与数据库中发布的校验和匹配。 Source Spotter下载Go源代码，构建它，并将结果校验和与数据库中的校验和进行比较，标记任何不匹配。自成立以来，Source Spotter已成功复现自Go 1.21.0以来的所有Go工具链。

作者通过从一个非常早期的Go版本构建一个引导式的Go 1.20工具链来解决需要一个Go工具链来构建一个新的工具链的“信任的信任”问题，多次重复这个过程以增加保证。

本文还重点介绍了诸如从macOS工具链中剥离签名以及处理校验和数据库中的不一致之处等挑战。讨论了验证源代码的替代方法，例如从Go Git存储库构建。作者赞扬Go团队使第三方可以验证该系统，并希望其他生态系统也能效仿。

---

## 54. 启动洋葱镜像非常简单

**原文标题**: Spinning Up an Onion Mirror Is Stupid Easy

**原文链接**: [https://flower.codes/2025/10/23/onion-mirror.html](https://flower.codes/2025/10/23/onion-mirror.html)

在Debian VPS上使用Caddy搭建网站.onion镜像的逐步指南

本文提供了一份在基于Debian的VPS上使用Caddy Web服务器搭建网站.onion镜像的逐步指南。作者解释了其动机（言论自由、反审查，以及“因为我可以”），并强调了该过程的简易性。

该指南涵盖以下关键步骤：

1.  **准备工作：** 作者使用Caddy、DigitalOcean VPS和Debian。
2.  **安装Tor：** 使用`apt`安装Tor软件包。
3.  **配置Tor：** 修改`/etc/tor/torrc`文件以创建隐藏服务，禁用SOCKS代理，设置`RunAsDaemon`，定义`HiddenServiceDir`和`HiddenServicePort`，并禁用`ORPort`和`DirPort`。
4.  **重启Tor：** 重启Tor服务以应用更改。
5.  **获取.onion地址：** 从位于`HiddenServiceDir`中的`hostname`文件检索.onion地址。
6.  **配置Caddy：** 可以在Caddy配置中为.onion地址添加一个新的站点块，通过纯HTTP提供站点。作者指出，由于Tor提供加密，因此HTTPS是不必要的。
7.  **(可选)宣传您的.onion地址：** 将`Onion-Location`标头添加到主站点的Caddy配置中，以告知启用Tor的浏览器有关.onion镜像的信息。

作者包含了一个更新，解释说由于Tor的内置加密，在Tor网络中使用HTTP是可以接受的。作者最后鼓励读者测试其镜像并支持他们的工作。

---

## 55. 987654321 / 123456789

**原文标题**: 987654321 / 123456789

**原文链接**: [https://www.johndcook.com/blog/2025/10/26/987654321/](https://www.johndcook.com/blog/2025/10/26/987654321/)

本文探讨了在不同进制下，由升序和降序排列的数字串联而成的数字之间有趣的关联。具体而言，它研究了对于给定的进制 `b`，`num(b)`（降序排列的数字）与 `denom(b)`（升序排列的数字）的比率。

作者观察到，在十进制中，987654321/123456789 非常接近 8，并想知道这是否适用于其他进制。他们发现，在六进制中，类似数字的比率接近 4，而在十六进制中，由于浮点数的限制，该比率实际上是 14。

核心发现是，对于任何进制 `b > 2`，比率 `num(b) / denom(b)` 几乎等于 `b - 2`，其中小数部分大约为 `1/b`。作者提供了 Python 代码来证明这种关系对于高达 1000 的进制都成立。该代码证实 `num(b) // denom(b) == b-2` 并且 `num(b) % denom(b) == b-1`。

作者认为，提供代码而不是正式证明是合理的，因为代码可以作为一种补充验证方法，有可能发现传统证明中被忽略的错误，并强制达到必要的细节水平。

---

## 56. 以色列要求谷歌和亚马逊使用秘密“暗号”来规避法律命令

**原文标题**: Israel demanded Google and Amazon use secret 'wink' to sidestep legal orders

**原文链接**: [https://www.theguardian.com/us-news/2025/oct/29/google-amazon-israel-contract-secret-code](https://www.theguardian.com/us-news/2025/oct/29/google-amazon-israel-contract-secret-code)

《卫报》、《+972杂志》和Local Call联合调查显示，作为价值12亿美元的“尼姆布斯项目”云计算协议的一部分，以色列要求谷歌和亚马逊使用秘密的“眨眼机制”来规避法律命令。该机制要求两家公司向以色列政府发送伪装成“特殊补偿”付款的编码信息，以表明他们何时被迫根据禁言令将以色列数据交给外国当局。付款金额将与接收数据的国家的区号相对应。

以色列官员担心失去对其存储在云平台上的数据的控制权，而落入外国执法部门手中。他们还担心潜在的员工或股东压力，或者与被占领巴勒斯坦领土上的人权侵犯有关的法律诉讼，导致谷歌和亚马逊限制他们对服务的访问。

因此，“尼姆布斯”协议还禁止谷歌和亚马逊限制以色列对其云平台的访问，即使其技术被用于违反两家公司标准服务条款的方式。这与微软最近因大规模监控担忧而禁用以色列军方对某些服务的访问形成对比。

虽然谷歌和亚马逊否认规避法律义务，但泄露的文件表明，他们同意调整内部流程，并使标准合同条款服从以色列的要求。法律专家称这种“眨眼机制”不同寻常且具有潜在风险，因为它可能违反美国法律。

---

## 57. 波特诺伊的心理学：论菲利普·罗斯开创性小说的创作

**原文标题**: The Psychology of Portnoy: On the Making of Philip Roth's Groundbreaking Novel

**原文链接**: [https://lithub.com/the-psychology-of-portnoy-on-the-making-of-philip-roths-groundbreaking-novel/](https://lithub.com/the-psychology-of-portnoy-on-the-making-of-philip-roths-groundbreaking-novel/)

史蒂文·J·齐珀斯坦的文章探讨了菲利普·罗斯开创性的长篇小说《波特诺伊的怨诉》的创作和影响。 这本小说于1969年出版，最初在《时尚先生》和《党派评论》等杂志上摘录，引起了广泛的关注和争议。 它立即产生了巨大的影响，引发了全国性的讨论和评论界的好评，甚至有人将波特诺伊比作基督般的形象。

罗斯从早期的作家，如华莱士·马克菲尔德、布鲁斯·杰伊·弗里德曼，特别是艾萨克·罗森菲尔德那里汲取了灵感，他们探索了犹太生活和性压抑之间的联系。 罗斯自己与来自中欧的弗洛伊德学派人物，心理分析学家汉斯·J·克莱因施密特的疗程，极大地塑造了小说的主题。 克莱因施密特对罗斯童年创伤的洞察，特别是他与母亲的关系，都被融入了书中。

《波特诺伊的怨诉》被认为是经过大量改写的产物，塑造了一个既是讲故事的人，又是笑柄的复杂角色。 这本小说对纽瓦克犹太生活的描写，以及对性毫不妥协的探索，被认为是既大胆又令人不安的。

虽然罗斯不愿将自己与喜剧演员相提并论，但他认为《波特诺伊的怨诉》让读者可以表达以前难以启齿的想法。 索菲·波特诺伊这个角色虽然不是直接的复制品，但借鉴了罗斯自己母亲的某些方面。 这本小说的持久影响在于它解放了禁忌话题，并邀请读者拥抱自己的复杂性。

---

## 58. Show HN: 在 gVisor 沙箱中运行 GitHub Actions 步骤

**原文标题**: Show HN: Run a GitHub Actions step in a gVisor sandbox

**原文链接**: [https://github.com/geomys/sandboxed-step](https://github.com/geomys/sandboxed-step)

此“Show HN”提交介绍了 `sandboxed-step`，这是一个在 gVisor 沙箱中执行命令的 GitHub Action。该 Action 旨在解决 GitHub Actions 中固有的安全漏洞，特别是缓存中毒的风险以及即使具有只读权限，各个步骤之间也缺乏隔离的问题。

其主要动机是为运行不受信任的代码提供更安全的环境，例如针对最新依赖项版本的 CI 流程，从而降低供应链攻击的风险。

该 Action 利用 gVisor 创建一个隔离环境，使用类似于 Ubuntu 24.04 的根文件系统，并提供对 `GITHUB_WORKSPACE`、主机网络和来自 `setup-*` Actions 的已安装工具的访问权限。它在与 GitHub Actions runner 相同的用户下运行，并具有 sudo 访问权限。

用户可以通过 `run` 输入指定要在沙箱中运行的命令。它提供了控制网络访问、持久化工作区更改（强烈不建议）以及配置环境变量的选项。它还可以防止意外暴露 GitHub 令牌，如果 `actions/checkout` 持久化凭据，则会检测并报错，除非明确允许（同样不建议）。

示例工作流程演示了如何使用 `sandboxed-step` 进行沙箱化的 Go 测试（使用不同的 Go 版本和依赖管理策略），以及运行 `staticcheck` 和 `govulncheck` 工具。作者强调使用 GitHub 的 Immutable Releases 来保证标签安全性。

---

## 59. 笨蛋，关键在“硬件”！

**原文标题**: It's the "Hardware", Stupid

**原文链接**: [https://haebom.dev/archive?post=4w67rj24q76nrm5yq8ep](https://haebom.dev/archive?post=4w67rj24q76nrm5yq8ep)

本文介绍了《时代》杂志评选的2025年最佳发明，重点关注各个领域的硬件进步。这些发明被分为机器人、航空航天和农业三个类别。

在**机器人**领域，亮点包括实现纹理打印的EufyMake E1 UV打印机，用于个人录像的HoverAir X1 ProMax，敏捷的人形机器人宇树R1，以及提供盲文和图形可访问性的美国印刷之家Monarch。Lotus Ring可以实现智能家居控制，Tilt Grip Stick简化了润唇膏的涂抹。

**航空航天**类别包括承诺提供来自太空的超高速互联网的AST SpaceMobile BlueBird，促进月球任务的Firefly Blue Ghost，提供早期野火探测的FireSat，以及增强天空观测的维拉·C·鲁宾天文台。

最后，**农业**领域展示了诸如FutureFeed的海藻补充剂Asparagopsis以减少牲畜的甲烷排放，Innovea Global Coffee Breeding Network开发的适应气候变化的咖啡品种，提供电力除草以节省除草剂的RootWave eWeeder，自动化葡萄园管理的Scout Gen 5，提高收获效率的Thunderstruck Razors Edge Concaves，以及使用数据驱动的室内固化来增强香草生产的Vanilla Vida等创新。

共同点在于依靠物理硬件解决方案来解决各个领域中的当代挑战，强调了有形技术进步的持续重要性。

---

## 60. 汇编语言实现的Hello-World iOS应用

**原文标题**: Hello-World iOS App in Assembly

**原文链接**: [https://gist.github.com/nicolas17/966a03ce49f949dd17b0123415ef2e31](https://gist.github.com/nicolas17/966a03ce49f949dd17b0123415ef2e31)

本文介绍了一个直接用 ARM 汇编语言实现的 "Hello-World" iOS 应用程序。 该代码名为 `yellow.asm`，旨在创建一个具有黄色背景的简单 iOS 应用程序。

该汇编代码专注于手动创建必要的 Objective-C 运行时环境，包括设置自动释放池、初始化应用程序委托、创建应用程序窗口、视图控制器，并将视图的背景颜色设置为黄色。 该代码直接与 Objective-C 运行时函数交互，例如 `objc_getClass`、`objc_msgSend`、`class_addMethod` 和 `UIApplicationMain`。

该代码初始化了 `AppDelegate`，动态创建了一个 `UIWindow` 和 `UIViewController`，设置了背景颜色，并使窗口可见。 核心逻辑位于 `didFinishLaunching` 函数中。 它检索主屏幕的边界，使用这些边界创建一个 `UIWindow`，实例化一个 `UIViewController`，将其视图的背景设置为黄色，并将 `UIViewController` 设置为窗口的根视图控制器。

一些评论者讨论了潜在的改进和需要考虑的点。 mraniki 询问构建/部署步骤。 Nukoooo 询问为局部变量分配的大小。 hirschsn 澄清了 ARM 架构上下文中“word”的含义。 pguyot 提出了关于寄存器保护的担忧并建议进行优化。 ozanyasindogan 对将该应用程序作为付费应用程序部署到 App Store 提出了幽默的评论。

---

## 61. 没有速度限制

**原文标题**: There's No Speed Limit

**原文链接**: [https://sive.rs/kimo](https://sive.rs/kimo)

德里克·西弗斯回忆了与伯克利音乐学院校友兼前导师基莫·威廉姆斯的一次偶然相遇如何深刻地影响了他的生活。即将进入伯克利学习的西弗斯联系了一家当地录音棚，威廉姆斯为他提供了速成的音乐理论和编曲课程。

威廉姆斯强调学习“没有速度限制”，并以一种紧张而个性化的学习方式挑战西弗斯。通过五节课，西弗斯涵盖了伯克利六个学期的和声与编曲课程内容。这使他能够在入学时免修这些课程。

受到威廉姆斯高期望的启发，西弗斯继续自学并免修其他课程，同时还完成了全部的课程负担。结果，他用两年半的时间而非通常的四年毕业，并在二十岁时获得了学士学位。

西弗斯将他后来的成功归功于威廉姆斯的影响，他说自己学会了突破传统限制，并在生活的各个方面超越期望。他认为威廉姆斯向他灌输了一种信念，即有进取心的人可以取得远超预期的成就。二十年后，西弗斯受邀向伯克利新生发表主题演讲，这证明了威廉姆斯指导的持久影响。直到今天，他们仍然是朋友。

---

## 62. Zig 的新型异步 I/O

**原文标题**: Zig's New Async I/O

**原文链接**: [https://andrewkelley.me/post/zig-new-async-io-text-version.html](https://andrewkelley.me/post/zig-new-async-io-text-version.html)

本文介绍了 Zig 0.16.0 版本中新增的异步 I/O 原语。通过一系列示例，演示了核心同步 API。初始示例确立了基本的 async/await 用法，重点说明了其如何解耦函数调用和返回。

文章强调了 async/await 在表达异步方面的强大功能，允许 I/O 实现优化执行（例如，`std.Io.Threaded` 同时执行多个任务）。然而，它也指出了错误处理和资源泄漏方面的潜在陷阱，尤其是在 `try` 与多个 awaits 结合使用时。

提出的关键解决方案是 `cancel` 原语。通过延迟 `cancel` 调用，即使发生错误，资源也能得到妥善清理，从而产生更健壮和优化的代码。`cancel` 是幂等的，并从 I/O 实现请求取消操作。

文章随后区分了异步和并发。在需要真正并发的场景中，使用 `io.async` 可能会导致死锁。解决方案是使用 `io.concurrent`，它允许 I/O 实现（例如，`std.Io.Threaded`）过度订阅线程，确保任务可以同时运行。如果真正无法实现并发，`io.concurrent` 可能会失败并返回 `error.ConcurrencyUnavailable`。本质上，使用 `io.concurrent` 明确表明程序*需要*实际并发。

文章展示了这些新的原语如何使开发人员能够编写符合 Zig 习惯的代码，同时有效地管理异步操作和资源。

---

## 63. 美国拒绝加入联合国网络犯罪条约，该条约已有70余国签署。

**原文标题**: US declines to join more than 70 countries in signing UN cybercrime treaty

**原文链接**: [https://therecord.media/us-declines-signing-cybercrime-treaty?](https://therecord.media/us-declines-signing-cybercrime-treaty?)

包括英国、欧盟、中国和俄罗斯在内的70多个国家在河内签署了联合国打击网络犯罪公约，旨在建立一个打击数字犯罪的全球框架。联合国秘书长安东尼奥·古特雷斯强调该公约在解决非法资金流动、勒索软件攻击以及协助全球南方国家打击网络犯罪方面的重要性，据估计，网络犯罪每年造成的损失达10.5万亿美元。

该公约旨在改善协调，建设能力，追踪网络犯罪分子，并建立一个全天候的国际合作和证据共享网络。

值得注意的是，美国尚未签署该条约，称仍在审查中。科技行业和人权组织批评该条约，认为它可能将网络安全研究定为犯罪，并导致广泛的电子监控，可能被专制政权滥用以压制异议。此外，人们还对数据保护和“网络威权主义”的可能性表示担忧。

尽管受到批评，古特雷斯承认人权方面的担忧，并坚持认为该公约解决了跨境共享数字证据这一关键问题，旨在将肇事者绳之以法，无论其身在何处。联合国指出，该公约提供了第一个全球框架，将未经同意传播私密图像的行为认定为犯罪。

---

## 64. 经典图表揭示自然界最高效的旅行者

**原文标题**: A classic graphic reveals nature's most efficient traveler

**原文链接**: [https://www.scientificamerican.com/article/a-human-on-a-bicycle-is-among-the-most-efficient-forms-of-travel-in-the/](https://www.scientificamerican.com/article/a-human-on-a-bicycle-is-among-the-most-efficient-forms-of-travel-in-the/)

《科学美国人》通过重温并更新一个比较各种动物物种运动能量效率的经典图表，庆祝杂志创刊180周年。文章强调，人类自身行动效率不高，但使用自行车后却能成为非常高效的陆地旅行者。

文章解释说，旅行需要消耗能量来对抗重力并推动自身前进。陆地动物需要消耗能量来站立和移动，而飞行和游泳的生物则可以滑翔，利用气流或浮力来最大限度地减少能量消耗。文章认为，自行车让人类能够通过使用轮子滑行和使用刚性框架来抵消重力，从而模仿游泳的效率。

比较生理学家泰森·海德里克被引用说，自行车基本上使人类的陆地旅行更类似于游泳。文章承认了人类体型不利的一面，即为骑自行车的人造成阻力。海德里克还建议，带有空气动力学外壳的自行车（机动车）可以进一步提高人类的效率，甚至超过水生效率。

文章最后呼吁通过订阅《科学美国人》来支持科学新闻，强调该杂志长期倡导科学的历史以及其在当今世界中的重要作用。

---

## 65. 谁还需要Graphviz，自己就能建一个了？

**原文标题**: Who needs Graphviz when you can build it yourself?

**原文链接**: [https://spidermonkey.dev/blog/2025/10/28/iongraph-web.html](https://spidermonkey.dev/blog/2025/10/28/iongraph-web.html)

本文详细介绍了`iongraph`的开发过程，`iongraph`是一款定制工具，用于可视化SpiderMonkey的Ion优化编译器的内部图，取代了标准的Graphviz输出。作者发现Graphviz存在不足，包括布局不稳定、与源代码结构缺乏直观联系，以及静态PDF在复杂图探索方面的局限性。

`iongraph`的核心是受到Sugiyama方法启发的定制布局算法。该算法分解为四个关键步骤：

1. **分层：**根据块在图中的深度，将块排序到水平层中，循环结构会影响层分配，以反映源代码结构。
2. **创建虚拟节点：**为跨越多个层的边插入虚拟节点，以确保清晰的路由。
3. **拉直边：**通过一系列步骤，水平对齐节点，"缩进"循环中的代码，并最大限度地减少边的摆动。
4. **跟踪水平边：**将重叠的水平边排序到平行的"轨道"中，以避免视觉混乱。

通过利用控制流图的特性（可约控制流、明确定义的循环）并简化Sugiyama算法（避免边缘交叉最小化），作者创建了一个简单、快速且稳定的布局算法。由此产生的`iongraph`工具提供了一种交互式、直观且高效的方式来可视化和调试编译器图，从而改善了SpiderMonkey开发人员的工作流程。文章证明了在满足特定需求时，定制解决方案通常可以胜过通用工具。

---

## 66. 用吸血鬼学习多平台Z80汇编编程

**原文标题**: Learn Multiplatform Z80 Assembly Programming with Vampires

**原文链接**: [https://www.chibiakumas.com/z80/](https://www.chibiakumas.com/z80/)

本文是一篇全面的指南，以独特的“吸血鬼”主题为框架，教授在多个复古平台上学习 Z80 汇编编程。它提供了一条结构化的学习路径，从绝对初学者的概念开始，逐步发展到多平台开发和游戏创建等高级技术。

内容分为以下几个系列：

*   **绝对初学者系列：** 介绍基本的编程概念。
*   **Z80 汇编系列：** 通过示例教授基本的 Z80 指令。
*   **Hello World 系列：** 为各种平台提供简单的“Hello World”示例。
*   **简单系列：** 涵盖在不同系统上创建精灵等基本任务。
*   **平台特定系列：** 侧重于 Amstrad CPC、MSX、ZX Spectrum、Gameboy 等系统的硬件特定细节。
*   **高级系列：** 介绍更复杂的 Z80 编程技术。
*   **多平台系列：** 指导用户创建可在多个平台上运行的代码。
*   **Yquest 系列 (Xquest 克隆) 和 Photon 系列 (Tron 克隆)：** 提供实际的游戏开发示例。
*   **ChibiAkumas 系列：** 分析这款游戏的源代码。

本教程强调实践学习，为每节课提供实际示例和配套的 YouTube 视频。它建议使用 VASM 汇编器以获得多语言支持，并建议从 Winape 开始进行 Amstrad CPC 开发。其目标是使学习者能够创建与 20 世纪 80 年代游戏相媲美的游戏，同时获得宝贵的编程知识。

---

## 67. 医院行业整合导致医疗保健成本上升，研究发现

**原文标题**: Consolidation in Hospital Sector Leading to Higher Health Care Costs, Study Find

**原文链接**: [https://harris.uchicago.edu/news-events/news/consolidation-hospital-sector-leading-higher-health-care-costs-study-finds](https://harris.uchicago.edu/news-events/news/consolidation-hospital-sector-leading-higher-health-care-costs-study-finds)

一项新研究表明，由于反垄断执法不力，美国医院整合正在推高医疗成本。 研究人员发现，尽管有证据表明20%的医院合并案可能减少竞争并提高价格，但在2000年至2020年期间，联邦贸易委员会(FTC)仅对1%的医院合并案提出质疑。

该研究由助理教授Zarek Brot-Goldberg共同撰写，估计2010年至2015年间未受挑战的合并导致价格上涨5%或更多，每年给私人保险者带来2.04亿美元的损失。 研究人员认为，联邦贸易委员会的执法不力源于资金不足，因为医院合并造成的经济损失几乎与该机构的全部预算相当。

副教授Zack Cooper强调，自2000年以来，医院价格的上涨速度超过了所有其他行业，现在住院费用平均接近2.5万美元。 他强调需要加强竞争维护工作。

该研究还表明，由于缺乏竞争诊所，农村和低收入地区的合并导致了更大的价格上涨，尤其是在门诊服务方面。 鉴于90%的医院市场已经高度集中，研究人员强调了解决这一问题的紧迫性。 Brot-Goldberg和他的同事认为，增加对联邦贸易委员会的资金投入可以带来更好的执法并遏制医疗成本的上涨。

---

## 68. Minecraft removing obfuscation in Java Edition

**原文标题**: Minecraft removing obfuscation in Java Edition

**原文链接**: [https://www.minecraft.net/en-us/article/removing-obfuscation-in-java-edition](https://www.minecraft.net/en-us/article/removing-obfuscation-in-java-edition)

生成摘要时出错

---

## 69. Maryland's new privacy law puts strict limits on how companies use your data

**原文标题**: Maryland's new privacy law puts strict limits on how companies use your data

**原文链接**: [https://technical.ly/civics/maryland-data-privacy-act/](https://technical.ly/civics/maryland-data-privacy-act/)

生成摘要时出错

---

## 70. It's insulting to read AI-generated blog posts

**原文标题**: It's insulting to read AI-generated blog posts

**原文链接**: [https://blog.pabloecortez.com/its-insulting-to-read-your-ai-generated-blog-post/](https://blog.pabloecortez.com/its-insulting-to-read-your-ai-generated-blog-post/)

生成摘要时出错

---

## 71. Too Cruel Too Soon

**原文标题**: Too Cruel Too Soon

**原文链接**: [https://paulkrugman.substack.com/p/too-cruel-too-soon](https://paulkrugman.substack.com/p/too-cruel-too-soon)

生成摘要时出错

---

## 72. NaN, the not-a-number number that isn't NaN

**原文标题**: NaN, the not-a-number number that isn't NaN

**原文链接**: [https://piccalil.li/blog/nan-the-not-a-number-number-that-isnt-nan/](https://piccalil.li/blog/nan-the-not-a-number-number-that-isnt-nan/)

生成摘要时出错

---

## 73. Rats Caught on Camera Hunting Flying Bats

**原文标题**: Rats Caught on Camera Hunting Flying Bats

**原文链接**: [https://scienceclock.com/rats-caught-on-camera-hunting-flying-bats-for-the-first-time/](https://scienceclock.com/rats-caught-on-camera-hunting-flying-bats-for-the-first-time/)

生成摘要时出错

---

## 74. A Defense of Philosophical Intuitions

**原文标题**: A Defense of Philosophical Intuitions

**原文链接**: [https://hilariusbookbinder.substack.com/p/a-defense-of-philosophical-intuitions](https://hilariusbookbinder.substack.com/p/a-defense-of-philosophical-intuitions)

生成摘要时出错

---

## 75. Typst's Math Mode Problem

**原文标题**: Typst's Math Mode Problem

**原文链接**: [https://laurmaedje.github.io/posts/math-mode-problem/](https://laurmaedje.github.io/posts/math-mode-problem/)

生成摘要时出错

---

## 76. Frozen DuckLakes for Multi-User, Serverless Data Access

**原文标题**: Frozen DuckLakes for Multi-User, Serverless Data Access

**原文链接**: [https://ducklake.select/2025/10/24/frozen-ducklake/](https://ducklake.select/2025/10/24/frozen-ducklake/)

生成摘要时出错

---

## 77. Tips for stroke-surviving software engineers

**原文标题**: Tips for stroke-surviving software engineers

**原文链接**: [https://blog.j11y.io/2025-10-29_stroke_tips_for_engineers/](https://blog.j11y.io/2025-10-29_stroke_tips_for_engineers/)

生成摘要时出错

---

## 78. uBlock Origin Lite in Apple App Store

**原文标题**: uBlock Origin Lite in Apple App Store

**原文链接**: [https://apps.apple.com/in/app/ublock-origin-lite/id6745342698](https://apps.apple.com/in/app/ublock-origin-lite/id6745342698)

生成摘要时出错

---

## 79. The cryptography behind electronic passports

**原文标题**: The cryptography behind electronic passports

**原文链接**: [https://blog.trailofbits.com/2025/10/31/the-cryptography-behind-electronic-passports/](https://blog.trailofbits.com/2025/10/31/the-cryptography-behind-electronic-passports/)

生成摘要时出错

---

## 80. Signs of introspection in large language models

**原文标题**: Signs of introspection in large language models

**原文链接**: [https://www.anthropic.com/research/introspection](https://www.anthropic.com/research/introspection)

生成摘要时出错

---

## 81. PlanetScale Offering $5 Databases

**原文标题**: PlanetScale Offering $5 Databases

**原文链接**: [https://planetscale.com/blog/5-dollar-planetscale](https://planetscale.com/blog/5-dollar-planetscale)

生成摘要时出错

---

## 82. ZOZO's Contact Solver for physics-based simulations

**原文标题**: ZOZO's Contact Solver for physics-based simulations

**原文链接**: [https://github.com/st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver)

生成摘要时出错

---

## 83. Estimating the perceived 'claustrophobia' of New York City's streets (2024)

**原文标题**: Estimating the perceived 'claustrophobia' of New York City's streets (2024)

**原文链接**: [http://mfranchi.net/posts/claustrophobic-streets/](http://mfranchi.net/posts/claustrophobic-streets/)

生成摘要时出错

---

## 84. What we talk about when we talk about sideloading

**原文标题**: What we talk about when we talk about sideloading

**原文链接**: [https://f-droid.org/2025/10/28/sideloading.html](https://f-droid.org/2025/10/28/sideloading.html)

生成摘要时出错

---

## 85. Today I Learned: Binfmt_misc

**原文标题**: Today I Learned: Binfmt_misc

**原文链接**: [https://dfir.ch/posts/today_i_learned_binfmt_misc/](https://dfir.ch/posts/today_i_learned_binfmt_misc/)

生成摘要时出错

---

## 86. Show HN: ekoAcademic – Convert ArXiv papers to interactive podcasts

**原文标题**: Show HN: ekoAcademic – Convert ArXiv papers to interactive podcasts

**原文链接**: [https://www.wadamczyk.io/projects/ekoacademic/index.html](https://www.wadamczyk.io/projects/ekoacademic/index.html)

生成摘要时出错

---

## 87. Language models are injective and hence invertible

**原文标题**: Language models are injective and hence invertible

**原文链接**: [https://arxiv.org/abs/2510.15511](https://arxiv.org/abs/2510.15511)

生成摘要时出错

---

## 88. Deadly storm shatters NYC rainfall records

**原文标题**: Deadly storm shatters NYC rainfall records

**原文链接**: [https://www.cbsnews.com/newyork/news/nyc-flooding-record-rainfall-totals/](https://www.cbsnews.com/newyork/news/nyc-flooding-record-rainfall-totals/)

生成摘要时出错

---

## 89. A change of address led to our Wise accounts being shut down

**原文标题**: A change of address led to our Wise accounts being shut down

**原文链接**: [https://shaun.nz/why-were-never-using-wise-again-a-cautionary-tale-from-a-business-burned/](https://shaun.nz/why-were-never-using-wise-again-a-cautionary-tale-from-a-business-burned/)

生成摘要时出错

---

## 90. Some Smalltalk about Ruby Loops

**原文标题**: Some Smalltalk about Ruby Loops

**原文链接**: [https://tech.stonecharioteer.com/posts/2025/ruby-loops/](https://tech.stonecharioteer.com/posts/2025/ruby-loops/)

生成摘要时出错

---

## 91. Grammarly rebrands to 'Superhuman,' launches a new AI assistant

**原文标题**: Grammarly rebrands to 'Superhuman,' launches a new AI assistant

**原文链接**: [https://techcrunch.com/2025/10/29/grammarly-rebrands-to-superhuman-launches-a-new-ai-assistant/](https://techcrunch.com/2025/10/29/grammarly-rebrands-to-superhuman-launches-a-new-ai-assistant/)

生成摘要时出错

---

## 92. New Covid virus found in wild Brazilian bats

**原文标题**: New Covid virus found in wild Brazilian bats

**原文链接**: [https://www.telegraph.co.uk/global-health/science-and-disease/new-covid-virus-with-furin-cleavage-site-found-in-wild-braz/](https://www.telegraph.co.uk/global-health/science-and-disease/new-covid-virus-with-furin-cleavage-site-found-in-wild-braz/)

生成摘要时出错

---

## 93. China has added forest the size of Texas since 1990

**原文标题**: China has added forest the size of Texas since 1990

**原文链接**: [https://e360.yale.edu/digest/china-new-forest-report](https://e360.yale.edu/digest/china-new-forest-report)

生成摘要时出错

---

## 94. More than DNS: Learnings from the 14 hour AWS outage

**原文标题**: More than DNS: Learnings from the 14 hour AWS outage

**原文链接**: [https://thundergolfer.com/blog/aws-us-east-1-outage-oct20](https://thundergolfer.com/blog/aws-us-east-1-outage-oct20)

生成摘要时出错

---

## 95. I have released a 69.0MB version of Windows 7 x86

**原文标题**: I have released a 69.0MB version of Windows 7 x86

**原文链接**: [https://twitter.com/XenoPanther/status/1983477707968291075](https://twitter.com/XenoPanther/status/1983477707968291075)

生成摘要时出错

---

## 96. Composer: Building a fast frontier model with RL

**原文标题**: Composer: Building a fast frontier model with RL

**原文链接**: [https://cursor.com/blog/composer](https://cursor.com/blog/composer)

生成摘要时出错

---

## 97. AWS to bare metal two years later: Answering your questions about leaving AWS

**原文标题**: AWS to bare metal two years later: Answering your questions about leaving AWS

**原文链接**: [https://oneuptime.com/blog/post/2025-10-29-aws-to-bare-metal-two-years-later/view](https://oneuptime.com/blog/post/2025-10-29-aws-to-bare-metal-two-years-later/view)

生成摘要时出错

---

## 98. Show HN: Status of my favorite bike share stations

**原文标题**: Show HN: Status of my favorite bike share stations

**原文链接**: [https://blog.alexboden.ca/toronto-bike-share-status/](https://blog.alexboden.ca/toronto-bike-share-status/)

生成摘要时出错

---

## 99. Extropic is building thermodynamic computing hardware

**原文标题**: Extropic is building thermodynamic computing hardware

**原文链接**: [https://extropic.ai/](https://extropic.ai/)

生成摘要时出错

---

## 100. I made a 10¢ MCU Talk

**原文标题**: I made a 10¢ MCU Talk

**原文链接**: [https://www.atomic14.com/2025/10/29/CH32V003-talking](https://www.atomic14.com/2025/10/29/CH32V003-talking)

生成摘要时出错

---

