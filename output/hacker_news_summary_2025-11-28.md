# Hacker News 热门文章摘要 (2025-11-28)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 荷兰大学能否摆脱微软？

**原文标题**: Can Dutch universities do without Microsoft?

**原文链接**: [https://dub.uu.nl/en/news/can-dutch-universities-do-without-microsoft](https://dub.uu.nl/en/news/can-dutch-universities-do-without-microsoft)

荷兰大学能否摆脱微软？（一篇Hoger Onderwijs Persbureau文章探讨荷兰大学减少或消除对微软产品和服务依赖的可能性和挑战，可能深入探讨以下因素：

*   微软的主导地位：荷兰大学目前在教育、研究和行政任务方面对微软软件（如Windows、Office 365、Teams）的依赖程度。
*   成本考量：使用微软产品的财务影响，包括许可费以及切换到替代解决方案可能节省的成本。
*   隐私担忧：与使用微软云服务相关的数据隐私和安全担忧，尤其是在欧洲数据保护法规（GDPR）的背景下。
*   替代方案的可用性：文章可能讨论现有的开源或其他商业替代方案，这些方案可能满足大学的需求。它可能会提到具体的软件套件，如LibreOffice，或协作平台，如Nextcloud。
*   技术可行性：迁移离开微软的技术挑战，包括兼容性问题、员工培训以及新系统的集成。
*   对研究的影响：文章将考虑摆脱微软对研究活动的潜在影响，特别是那些依赖于特定微软工具或平台的研究。
*   利益相关者的观点：它可能包括大学管理人员、IT人员、研究人员和学生关于减少对微软依赖的可行性和愿望的观点。
*   赞成和反对的论点：文章可能提出了一个平衡的论点，概述了这种转变的优点（例如，节省成本、提高数据隐私）和缺点（例如，技术挑战、用户采用）。
*   大学试点/案例：它可能会提到已经采取措施减少对微软依赖或正在考虑这样做的具体荷兰大学。）

---

## 2. 基于Yggdrasil网络的真正P2P邮件

**原文标题**: True P2P Email on Top of Yggdrasil Network

**原文链接**: [https://github.com/JB-SelfCompany/Tyr](https://github.com/JB-SelfCompany/Tyr)

Tyr：一款利用Yggdrasil网络的真正点对点电子邮件通讯安卓应用。与传统电子邮件不同，Tyr无需中心化邮件服务器、消息加密层（Yggdrasil已处理）和端口转发。它具有抗审查性，并允许用户控制其电子邮件基础设施。

主要功能包括与DeltaChat和ArcaneChat集成、本地SMTP/IMAP服务器、用于电子邮件身份的自动Ed25519密钥生成、可配置的Yggdrasil对等连接、开机自启动、加密备份/恢复以及自动从Android Keystore问题中恢复。

Tyr直接在Android设备上运行一个完整的电子邮件服务器（Yggmail，用Go编写），在localhost上暴露标准SMTP/IMAP协议。电子邮件地址通过用户的公钥加密派生（`<64位十六进制字符>@yggmail`），确保可验证的身份并防止欺骗。

将Tyr与DeltaChat/ArcaneChat配合使用，可以实现完全去中心化的消息传递体验，消息通过Yggdrasil直接在用户之间发送，绕过中心服务器。可以通过按钮自动设置，也可以通过配置DeltaChat/ArcaneChat配置文件以指向本地Tyr服务器来手动设置。

该项目包括安全功能，如用于密码的Android Keystore加密、自动Keystore恢复、Yggdrasil网络加密、本地专用端口访问、加密身份以及加密备份。Tyr是开源的。

---

## 3. 别拽那个，你永远不知道它连着什么。

**原文标题**: Don't tug on that, you never know what it might be attached to

**原文链接**: [https://blog.plover.com/2016/07/01/#tmpdir](https://blog.plover.com/2016/07/01/#tmpdir)

马克·多米努斯讲述了他的调试历程：他的 `also` 脚本（使用 `emacsclient` 在 Emacs 中打开文件）停止工作，并显示错误信息，指示无法找到服务器套接字。问题根源在于 Emacs 和 `emacsclient` 查找套接字的位置不匹配。

他发现，系统管理员脚本设置的 `TMPDIR` 环境变量导致 `emacsclient` 在 `/mnt/tmp` 中查找套接字，而 Emacs 则在 `/tmp` 中创建它。 最初，他怀疑 Emacs 不尊重 `TMPDIR`，但进一步调查显示，通过 Git 调用的 Perl 脚本 `git-re-edit` 以某种方式取消设置了 `TMPDIR`。

核心问题是为什么 Perl 会删除 `TMPDIR`。 令人困惑的是，它只影响 `TMPDIR`，而不影响其他环境变量。 最终，在其他人的帮助下，问题被追溯到 Perl 安装中的一项安全措施，该措施会剥离 `TMPDIR` 以防止权限提升攻击。 设置 `TMPDIR` 可能会诱使程序将临时文件写入攻击者控制的位置，从而可能覆盖重要文件。

多米努斯设计了两种解决方法：使用 TCP 套接字代替 Unix 域套接字用于 Emacs，以及设置自定义环境变量 `EMACS_SERVER_SOCKET`，以明确告诉 `emacsclient` 在哪里找到 Unix 域套接字。

---

## 4. 200行Python代码胜过5000万美元的超级计算机 – Re=10⁸下的Navier-Stokes方程 [pdf]

**原文标题**: 200 Lines of Python beats $50M supercomputer – Navier-Stokes at Re=10⁸ [pdf]

**原文链接**: [https://philpapers.org/archive/CAMIIA-3.pdf](https://philpapers.org/archive/CAMIIA-3.pdf)

基于标题，该文章做出了大胆的声明：仅用200行Python代码实现的基于纳维-斯托克斯方程的流体动力学模拟，其性能可以媲美价值5000万美元的超级计算机。雷诺数(Re)为10⁸表明存在高度湍流状态，使得模拟在计算上具有挑战性。

然而，所提供的文档似乎是一个被截断和损坏的PDF文档，主要由二进制数据和PDF对象定义组成，没有实际的文本内容来证实或反驳标题的声明。 无法确定模拟的准确性、所采用的方法、所使用的具体硬件，或者与超级计算机进行比较的细节。

因此，由于缺少文本内容，无法总结文章的内容。 唯一显而易见的是文章的标题以及PDF文档的格式。

---

## 5. Atuin 的新 Runbook 执行引擎

**原文标题**: Atuin’s New Runbook Execution Engine

**原文链接**: [https://blog.atuin.sh/introducing-the-new-runbook-execution-engine/](https://blog.atuin.sh/introducing-the-new-runbook-execution-engine/)

Atuin Desktop发布重大架构更新，重新设计了runbook执行引擎，解决了诸如上下文不稳定和执行不一致等问题。新引擎提供持久且可复现的runbook，在应用程序重启后保持状态并确保可预测的行为。

主要改进包括：

*   **持久上下文：** Runbook保留执行状态，无需重新运行代码块。
*   **可复现执行：** 代码块仅影响其下方的代码块，从而创建可预测的工作流程。
*   **模板无处不在：** 模板系统应用于所有用户输入，包括变量名和上下文代码块。
*   **自引用变量：** 变量可以引用自身以进行转换。
*   **两种类型的上下文：** 被动上下文（工作目录、环境变量）自动持久化。 主动上下文（代码块输出）在执行期间设置。

此次更新移除了全局上下文依赖性，并将编辑器变量同步替换为手动更新。 脚本变量现在仅捕获stdout。

未来的计划包括一个用于在没有Atuin Desktop的情况下执行runbook的CLI运行器、改进的串行执行、秘密管理以及基于Markdown的runbook。 新引擎为实时协作执行奠定了基础，并已在v0.2.0中提供。

---

## 6. Meta用高等几何隐藏270亿美元债务

**原文标题**: Meta hiding $27B in debt using advanced geometry

**原文链接**: [https://stohl.substack.com/p/exclusive-credit-report-shows-meta](https://stohl.substack.com/p/exclusive-credit-report-shows-meta)

无法访问文章链接。

---

## 7. Show HN: 用眼镜检测带摄像头的智能眼镜

**原文标题**: Show HN: Glasses to detect smart-glasses that have cameras

**原文链接**: [https://github.com/NullPxl/banrays](https://github.com/NullPxl/banrays)

这个“Show HN”帖子详细介绍了“Ban-Rays”的开发，这是一款旨在检测带有摄像头的智能眼镜（如Meta Raybans）的眼镜。该项目探索了两种主要的检测方法：光学和网络。

光学方法利用相机镜头的逆反射性，红外（IR）光会直接反射回光源。使用红外LED和光电二极管的初步实验表明，在区分相机镜头和其他反射表面方面效果不稳定。虽然测试了不同的波长和扫描模式，但产生的信号微弱且不可靠。

网络方法侧重于低功耗蓝牙（BLE）指纹识别。开发者发现Meta Raybans在配对和开机期间会广播可检测的BLE广播，其中包含Meta特定的标识符。挑战在于在使用过程中检测这些广播，这需要捕获特定的通信数据包。开发者正在探索使用nRF模块进行更高级的蓝牙分析。蓝牙经典（BTC）流量分析也在考虑之中，但需要更专业且昂贵的硬件。

作者以日志形式更新，详细介绍了迄今为止的挑战和发现，并概述了两种方法的未来步骤，包括试验扫描模式、来自不同波长的数据以及主动探测。该帖子最后感谢了为测试提供指导和借用设备的人员。

---

## 8. 人工智能采纳率开始趋于平缓

**原文标题**: AI Adoption Rates Starting to Flatten Out

**原文链接**: [https://www.apolloacademy.com/ai-adoption-rates-starting-to-flatten-out/](https://www.apolloacademy.com/ai-adoption-rates-starting-to-flatten-out/)

人工智能普及率趋于平缓

这篇文章由阿波罗首席经济学家托斯滕·斯洛克于2025年11月28日发表，报告指出各种规模的公司采用人工智能的比率开始趋于平缓。该分析使用了美国人口普查局和Ramp的数据，特别是Ramp人工智能指数，该指数衡量了超过4万家美国企业对人工智能产品和服务的采用情况。Ramp人工智能指数利用公司信用卡和账单支付数据，涵盖数十亿美元的支出。这些数据以双周调查的六次调查移动平均线形式呈现。

文章强调，未经阿波罗全球管理公司明确同意，不得分发所提供的信息。 它还包括一份全面的免责声明，声明阿波罗不保证信息的准确性，这些信息可能会发生变化。它明确指出，该演示文稿不是投资建议，读者应咨询自己的顾问。 最后，它提醒读者注意前瞻性陈述及其固有的不确定性。

---

## 9. 请愿书：正式承认开源工作为德国公民服务

**原文标题**: Petition to formally recognize open source work as civic service in Germany

**原文链接**: [https://www.openpetition.de/petition/online/anerkennung-von-open-source-arbeit-als-ehrenamt-in-deutschland#petition-main](https://www.openpetition.de/petition/online/anerkennung-von-open-source-arbeit-als-ehrenamt-in-deutschland#petition-main)

德国请愿活动呼吁正式承认开源工作为志愿服务

---

## 10. 重塑性感：网络监控扼杀了情色。

**原文标题**: Bringing Sexy Back. Internet surveillance has killed eroticism

**原文链接**: [https://lux-magazine.com/article/privacy-eroticism/](https://lux-magazine.com/article/privacy-eroticism/)

无法访问文章链接。

---

## 11. 科技巨头囤积数百万美元资金对抗人工智能监管

**原文标题**: Tech Titans Amass Multimillion-Dollar War Chests to Fight AI Regulation

**原文链接**: [https://www.wsj.com/tech/ai/tech-titans-amass-multimillion-dollar-war-chests-to-fight-ai-regulation-88c600e1](https://www.wsj.com/tech/ai/tech-titans-amass-multimillion-dollar-war-chests-to-fight-ai-regulation-88c600e1)

无法访问文章链接。

---

## 12. Moss: 一个用 Rust 编写的 Linux 兼容内核，仅需 26000 行代码

**原文标题**: Moss: a Rust Linux-compatible kernel in 26,000 lines of code

**原文链接**: [https://github.com/hexagonal-sun/moss](https://github.com/hexagonal-sun/moss)

Moss：用 Rust 和 Aarch64 汇编写成的类 Unix、Linux 兼容内核，旨在与 Linux 用户空间应用程序实现二进制兼容。其核心是异步的，利用 Rust 的 async/await 实现并发，防止常见的内核死锁。该内核采用模块化架构，具有硬件抽象层 (HAL)，便于移植到不同的架构，如 x86_64 和 RISC-V。

主要特性包括完整的 Aarch64 支持、MMU 启用、写时复制页面以及内核/用户空间页面错误管理。它实现了带有调度、任务迁移和 51 个 Linux 系统调用的进程管理，足以运行大多数 BusyBox 命令。VFS 和文件系统支持包括 Ramdisk、FAT32（只读）和 devtmpfs 驱动程序。

Moss 依赖于 `libkernel`，一个架构无关的实用程序库，可以在部署到裸机之前在主机上进行逻辑测试。它包括地址类型、容器、同步原语的强类型和一个全面的测试套件。

构建和运行涉及使用 QEMU 进行 Aarch64 仿真以及 `dosfstools` 创建虚拟文件系统。提供的脚本简化了 QEMU 中镜像创建和内核执行的过程。测试套件可以在 x86_64 Linux 上运行。

该项目路线图包括扩展系统调用兼容性、开发网络堆栈 (TCP/IP)、改进调度器以及实现读/写文件系统驱动程序。欢迎在 MIT 许可证下进行贡献。

---

## 13. Pocketbase – 单文件开源实时后端

**原文标题**: Pocketbase – open-source realtime back end in 1 file

**原文链接**: [https://pocketbase.io/](https://pocketbase.io/)

Pocketbase：单文件实时后端解决方案，简单易用。访问演示，查阅文档。

---

## 14. Stellantis用弹窗广告轰炸车主屏幕，推销新车折扣

**原文标题**: Stellantis Is Spamming Owners' Screens with Pop-Up Ads for New Car Discounts

**原文链接**: [https://www.thedrive.com/news/stellantis-is-spamming-owners-screens-with-pop-up-ads-for-new-car-discounts](https://www.thedrive.com/news/stellantis-is-spamming-owners-screens-with-pop-up-ads-for-new-car-discounts)

Stellantis因在其车辆的信息娱乐屏幕上显示弹出广告，提供新车购买折扣而面临强烈反对。 汽车爱好者Zerin Dube在他的吉普大切诺基屏幕上发布了一张营销通知照片，宣传1500美元的忠诚度优惠，该问题由此曝光。

虽然Dube最终使用了该优惠购买了一辆新的吉普牧马人，但许多其他车主表达了不满和批评，并誓言未来将避免购买该品牌。 他们分享了在克莱斯勒和Ram车辆上出现类似广告的截图。

Stellantis为这种做法辩护，称他们使用车载消息系统与车主保持联系，并提供重要的更新，例如召回通知。 他们声称这些营销通知旨在尽可能减少干扰，仅在汽车静止时出现并迅速消失。 该公司还表示，驾驶员可以通过联系客服选择退出这些消息。

尽管面临负面反应，Stellantis声称这些优惠在推动销售方面取得了成功。 文章指出，Stellantis正在叠加折扣，包括忠诚度奖励，以在竞争激烈的市场中促进销售，尤其是在与福特Bronco竞争时。 然而，使用车载屏幕进行广告宣传的做法引发了对隐私和驾驶员潜在分心的担忧。 这并非Stellantis首次使用车载屏幕进行广告宣传，他们之前也以类似的方式推广过延长保修期。

---

## 15. 四个模糊测试器的故事

**原文标题**: A Tale of Four Fuzzers

**原文链接**: [https://tigerbeetle.com/blog/2025-11-28-tale-of-four-fuzzers/](https://tigerbeetle.com/blog/2025-11-28-tale-of-four-fuzzers/)

本文详细介绍了TigerBeetle如何使用多种模糊测试器来测试其自适应复制路由 (ARR) 算法。ARR动态优化分布式数据库集群中的复制拓扑，通过将数据路由到副本环来提高性能和弹性。

作者认为，仅依靠单个、全系统的模糊测试器是不够的。针对每个子系统的有针对性的模糊测试器对于更深入的探索和特定的断言至关重要。为了实现这一点，他们主张在目标组件和系统的其余部分之间创建最小的接口，从而实现隔离和高效的模糊测试。

本文重点介绍了ARR接口的设计，通过传递表示时间和标识符的整数而不是复杂的数据结构来关注简洁性。这种依赖性的减少使系统更容易进行模糊测试。

本文介绍了用于ARR的四种不同类型的模糊测试器：

1. **穷举正空间模糊测试器:** 通过生成随机排列并验证往返编码，确保路由的序列化和反序列化工作正常。

文章的这部分到此结束，并表明下一节将详细说明其他3个模糊测试器的用法。

---

## 16. 掌上游戏砖：口袋里的游戏平台

**原文标题**: Playtiles: The Pocket-Sized Gaming Platform

**原文链接**: [https://get.playtil.es](https://get.playtil.es)

Playtiles：一款专为厌倦当下手游趋势的现代玩家设计的掌上游戏机。它面向那些怀念实体按键触感、对庞大游戏库、侵入式广告和掠夺性微交易感到厌烦的玩家。Playtiles也旨在吸引那些没有时间投入长时间游戏体验的个人。其主要卖点是以实惠的价格每周提供精选的新鲜、即时乐趣游戏。本质上，Playtiles承诺回归更简单、更愉快的掌上游戏体验，摆脱与手游相关的常见挫折。

---

## 17. A16Z的惊人论断

**原文标题**: A Remarkable Assertion from A16Z

**原文链接**: [https://nealstephenson.substack.com/p/a-remarkable-assertion-from-a16z](https://nealstephenson.substack.com/p/a-remarkable-assertion-from-a16z)

无法访问文章链接。

---

## 18. 瑞典出版商举报扎克伯格涉嫌欺诈

**原文标题**: Swedish publishers file police report against Meta's Zuckerberg for fraud

**原文链接**: [https://www.sverigesradio.se/artikel/swedish-publishers-file-police-report-against-metas-zuckerberg-for-fraud](https://www.sverigesradio.se/artikel/swedish-publishers-file-police-report-against-metas-zuckerberg-for-fraud)

瑞典出版商协会已向警方举报Meta创始人马克·扎克伯格涉嫌欺诈。该报告已提交瑞典警方。文章作者为Roza Bicerroza.bicer@sverigesradio.se，新闻类别为瑞典新闻、国际新闻、犯罪、IT与媒体新闻。提供的文本未详细说明涉嫌欺诈的具体细节。

---

## 19. 拥有44年Unix演进历史的仓库

**原文标题**: A Repository with 44 Years of Unix Evolution

**原文链接**: [https://www.spinellis.gr/pubs/conf/2015-MSR-Unix-History/html/Spi15c.html](https://www.spinellis.gr/pubs/conf/2015-MSR-Unix-History/html/Spi15c.html)

本文介绍了如何创建一个公开可用的Git仓库，用于追踪Unix操作系统44年的演变历史，从1972年到2015年。该仓库包含65.9万次提交和2306次合并，代表了来自贝尔实验室、伯克利大学和FreeBSD项目的约850位个人的贡献。

该仓库通过合成24个不同Unix版本的快照、遗留仓库（CSRG SCCS、FreeBSD 1 CVS）和现代FreeBSD Git仓库构建而成。一个关键方面是通过原始研究重建作者信息，因为早期的快照缺乏这些数据。这涉及到分析文档、代码，并与参与Unix开发的人员沟通。

该仓库结构使用标签和分支来标记重要的发布版本（Research版、BSD版本、FreeBSD发布版）和开发阶段。一项值得注意的技术是使用“.ref”目录来存储先前的快照。这确保了`git blame`可以通过检测代码移动来追踪跨版本的代码出处，而无需显示引用文件。该仓库还准确地表示了版本之间的合并。

本文强调了该仓库对于软件工程、信息系统和软件考古学领域的实证研究价值。该仓库以及用于创建它的工具都是公开可用的，使研究人员能够详细地重现和分析Unix的演变。

---

## 20. 人工智能计算

**原文标题**: Artificial Computation

**原文链接**: [https://cultureandcommunication.org/galloway/artificial-computation](https://cultureandcommunication.org/galloway/artificial-computation)

本文探讨了“人工计算”的概念，将其作为数字计算主导范式的激进替代方案，该范式由“充分计算原则”定义。这一原则源于图灵对计算机的广泛定义，认为任何逻辑上可定义的事物都可以通过计算来执行。这导致了：以行动为中心，思想与执行的混淆，实践上的全知，以及基于模仿精确性的判断体系。

然而，本文提出，拉鲁埃尔发现的人工计算*与*标准计算*并行*运作，而非*超越*标准计算。它从根本上挑战了充分计算原则，具体体现为：倾向于纯粹的、内在的过程，而非先发制人地执行可执行的命令；将思想与行动分离；拥抱基于公理的、彻底有限的知识；以及利用非模仿性的内在性技术。

本质上，人工计算代表着从传统计算的总体化潜力中撤退，寻求一种从传统控制论和神经科学中“解放”出来的思维形式。尽管人工计算机尚未被发明，但人工计算的理论框架提出了一种超越标准计算和哲学探究中固有限制和假设的通用思维。人工计算的同义词包括非计算、非标准计算、计算小说和计算机小说。

---

## 21. 写作通过改变大脑来增强应对日常挑战的韧性

**原文标题**: Writing Builds Resilience in Everyday Challenges by Changing Your Brain

**原文链接**: [https://scienceclock.com/writing-builds-resilience-in-everyday-challenges-by-changing-your-brain/](https://scienceclock.com/writing-builds-resilience-in-everyday-challenges-by-changing-your-brain/)

写作如何通过改变大脑来建立应对日常挑战的韧性

---

## 22. SQLite作为应用程序文件格式

**原文标题**: SQLite as an Application File Format

**原文链接**: [https://sqlite.org/appfileformat.html](https://sqlite.org/appfileformat.html)

本文提倡使用SQLite数据库作为应用程序文件格式，认为其相对于传统方法（如自定义格式、文件堆和封装文件堆格式）具有显著优势。

核心论点是SQLite提供了一种通用、结构良好且易于访问的方式来存储应用程序状态和数据。它强调了诸如简化应用程序开发（减少代码、经验证的可靠性）、单文件文档（易于复制和移动）、高级查询语言（SQL）以及可访问的内容（使用标准工具）等优点。

其他优势包括跨平台兼容性、原子事务（数据完整性）、增量和持续更新（性能和数据安全）、易于扩展（添加功能而不破坏兼容性）以及整体性能优势（更快的读/写和启动时间）。SQLite数据库避免了自定义格式的“不透明blob”性质，并提供了比简单文件堆更强的结构和查询能力。文章强调，SQLite数据库可以高效紧凑地处理复杂的关系和数据结构，使其成为许多应用程序文件格式需求的更佳选择。

---

## 23. 从文本生成3D网格

**原文标题**: Generating 3D Meshes from Text

**原文链接**: [https://cprimozic.net/notes/posts/generating-3d-meshes-from-text/](https://cprimozic.net/notes/posts/generating-3d-meshes-from-text/)

本文详细介绍了将文本转换为3D网格的过程，以用于作者的Geotoy项目和Geoscript语言。作者概述了一个三阶段流程：SVG路径生成、细分和拉伸。

首先，使用JavaScript库`svg-text-to-path`将文本和字体参数转换为SVG路径。这是通过利用Google Fonts和fontkit后端的小型后端服务完成的。该服务缓存路径并从生成的SVG中提取它。

接下来，使用Rust库`lyon`将SVG路径细分为三角形。`lyon_extra` crate解析SVG路径，而`lyon_tessellation`为2D网格生成顶点和索引缓冲区。实现了一个WebAssembly包装器，以便从主应用程序与该库进行交互。作者调整了`FillTessellator`选项，以确保正确处理自相交路径。

最后，将2D网格拉伸为3D。这包括将2D顶点转换为3D，翻转三角形的绕组顺序，创建具有偏移的重复顶点，并生成三角条以连接顶部和底部面。作者自己的网格表示用于此步骤。正确处理顶点索引对于确保输出网格是2-流形且水密的至关重要。

作者将此功能集成到Geoscript中，并报告该过程在各种字体甚至复杂脚本中都表现出高性能和可靠性。他们对结果感到满意，从文本输入中获得了高质量的3D网格。

---

## 24. Show HN: Spikelog – 脚本、定时任务和MVP的简单指标服务

**原文标题**: Show HN: Spikelog – A simple metrics service for scripts, cron jobs, and MVPs

**原文链接**: [https://spikelog.com](https://spikelog.com)

Spikelog：简易指标服务，专为脚本、定时任务和MVP设计，简化关键绩效指标的跟踪。无需复杂的监控堆栈，Spikelog提供单一API端点，用户可POST与图表名称关联的数值数据。服务自动生成随时间变化的图表，免去繁琐配置、查询语言或仪表盘构建。

Spikelog的核心优势包括易用性（只需复制API密钥并发送POST请求即可设置）、自动绘图和AI集成（使用提示自动识别并实施跟踪）。Spikelog尤其适用于快速确定作业是否成功运行、用户注册是否发生，或指标是增加还是减少。

Spikelog提供免费层级，包含10个图表，每个图表1,000个数据点，使用滚动窗口确保始终提供近期数据，无需保留管理。专为业余项目、MVP和小规模生产系统构建，是Grafana等完整监控堆栈或Axiom等更全面解决方案的轻量级替代方案（建议用于长期保留、复杂查询和合规性需求）。简单的阈值警报计划在未来开发。

---

## 25. 苹果和英特尔传闻合作开发Mac芯片

**原文标题**: Apple and Intel Rumored to Partner on Mac Chips

**原文链接**: [https://www.macrumors.com/2025/11/28/intel-rumored-to-supply-new-mac-chip/](https://www.macrumors.com/2025/11/28/intel-rumored-to-supply-new-mac-chip/)

该文章报道了苹果供应链分析师郭明錤的传言，称苹果最早可能在2027年中期再次与英特尔合作，生产其低端M系列芯片（可能为M6或M7）。该合作将涉及英特尔使用其18A工艺（2纳米以下节点）制造苹果设计的基于Arm架构的芯片，这与之前Mac中使用的英特尔设计的x86芯片有所不同。

台积电预计仍将是苹果M系列芯片的主要供应商，而英特尔的参与将仅限于制造。该传言暗示苹果可能利用英特尔生产MacBook Air、iPad Air和iPad Pro等设备的芯片。

郭明錤认为，此举可能有两个目的：满足对“美国制造”产品的需求（可能呼应特朗普政府的倡议），以及使苹果的制造供应链多样化。苹果于2020年开始摆脱英特尔处理器，其内部M系列芯片提供更高的每瓦性能。文章还指出，macOS Tahoe将是最后一个支持基于英特尔芯片的Mac的主要macOS版本。

---

## 26. 信号与噪声

**原文标题**: The Signal Is the Noise

**原文链接**: [https://www.magazine.dirt.fyi/p/the-signal-is-the-noise](https://www.magazine.dirt.fyi/p/the-signal-is-the-noise)

Nishanth Bhargava的文章《信号即噪声》探讨了预测市场（如Kalshi和Polymarket）的兴起及其对政治分析和报道的影响。由于人们对传统民调的信任度下降，尤其是在2016年大选之后，这些市场作为集体智慧的来源越来越受欢迎，允许个人押注政治事件的结果。

文章强调了这些市场产生的巨大交易量，例如在纽约市长选举中投注的数亿美元。它们变得如此受欢迎，以至于可以与传统政治竞选活动筹集的资金相媲美。这种转变的驱动力是人们认为市场价格比专家意见或传统民调更能提供对现实的可靠评估。

然而，文章警告说，预测市场日益增长的影响力模糊了市场赔率和实际现实之间的界限。随着选举博彩成为一个更大的产业，存在市场本身开始影响其应预测的事件的风险。这篇文章质疑，用鲍德里亚的话来说，市场的“地图”是否开始先于并塑造政治现实的“领土”。

文章将新型预测市场的逐利模式与爱荷华电子市场(IEM)的学术和研究导向模式进行了对比。 它表明，这些市场的兴起是一种更广泛的“认知危机”的症状，在这种危机中，人们对传统政治分析师的信任已经减弱。

---

## 27. 工作时无法集中注意力的数学原理

**原文标题**: The Math of Why You Can't Focus at Work

**原文链接**: [https://justoffbyone.com/posts/math-of-why-you-cant-focus-at-work/](https://justoffbyone.com/posts/math-of-why-you-cant-focus-at-work/)

本文探讨了为什么在工作中越来越难以集中注意力，并使用数学模型来说明中断的影响。作者认为，由Slack等技术和持续连接所引发的持续中断正在显著降低生产力。

该模型侧重于三个关键参数：λ（lambda），每小时的中断率；Δ（delta），中断后的恢复时间（分钟）；以及θ（theta），进行有意义的工作所需的最小不间断时间。本文提供了可视化，展示了这些参数的不同值如何影响8小时工作日，突出了具有长时间、不间断的“专注时间段”的高效工作日，与充满中断和恢复时间的碎片化工作日之间的鲜明对比。

“产能公式”表明，即使总工作时间不变，由于需要持续专注，增加中断和恢复时间也会大大降低实际产出。作者模拟了100天在各种条件下的情况，以显示λ、Δ和θ的不同组合如何影响整体生产力。

最后，本文引用研究表明，中断频率和恢复时间各不相同，但始终很高，尤其是在现代工作场所。一些研究表明，知识工作者每3分钟切换一次任务，并且需要10-16分钟才能从中断中恢复，而更新的数据表明，重度协作者的中断时间间隔为2分钟。本文强调了理解和管理这些因素对于提高专注力和生产力的重要性。

---

## 28. 用于实时流式会话音频的开源（Apache 2.0）TTS模型

**原文标题**: Open (Apache 2.0) TTS model for streaming conversational audio in realtime

**原文链接**: [https://github.com/nari-labs/dia2](https://github.com/nari-labs/dia2)

Dia2：一种实时流式对话TTS模型

Dia2由南瑞实验室开发，是一款开源、Apache 2.0 许可的流式对话TTS模型，专为实时对话音频生成而设计。与传统的TTS模型不同，Dia2在收到最初几个词后就开始生成音频，使其适用于交互式应用。该模型支持音频条件控制，通过结合先前的上下文来实现自然的对话流程。

目前提供两个模型检查点（10亿和20亿参数）以及推理代码，以方便研究。该模型目前支持英语，并且限制为2分钟的生成。质量和语音特征可能有所不同，因此需要使用前缀或进行微调以获得一致的输出。

主要特点包括：

*   **实时流式：** 随着文本输入，即时生成音频。
*   **音频条件控制：** 根据先前的音频输入（说话人声音）调整输出。
*   **开源：** 在 Apache 2.0 许可下发布，促进可访问性和修改。
*   **使用简单：** 可以使用 Gradio 或直接从命令行轻松测试

本文提供了安装、有/无音频条件控制的音频生成、程序化使用示例以及模型仓库链接的快速入门说明。

该项目明确禁止滥用，例如身份冒充、生成欺骗性内容或任何非法或恶意活动。它强调道德使用并遵守法律标准。

---

## 29. 用于构建工作流的开源n8n替代方案（包含GUI和Docker）

**原文标题**: Open-Source n8n Alternative for Workflow Building (GUI and Docker Included)

**原文链接**: [https://github.com/empowerd-cms/nyno](https://github.com/empowerd-cms/nyno)

Nyno 3.0是一款开源、多语言工作流引擎，旨在替代n8n等平台，用于构建自动化工作流。它允许用户使用Python、PHP、JavaScript和Ruby创建并连接自动化步骤。每种语言都在其自身的高性能worker引擎中运行，工作流使用人类可读的YAML文件（.nyno）定义。

该引擎使用多进程worker以提高性能，并根据CPU核心数为每种语言生成多个worker。Nyno允许用户将受支持语言的脚本转换为可在工作流中调用的可重用命令。这通过导出脚本中接受参数和上下文的函数来实现。

可以通过Docker/Podman轻松安装，并提供构建和运行容器的说明。文章还描述了在Linux主机上进行更复杂的安装，并指出对Best.js的依赖。文章提供了用每种受支持语言创建扩展的示例代码片段，演示了如何访问参数和上下文以在工作流中的步骤之间传递数据。最后，Nyno自豪地使用Best.JS构建，它是Next.JS的更快替代方案。

---

## 30. 用于构建工作流程的开源n8n替代方案（包含图形界面和Docker）

**原文标题**: Open-Source n8n Alternative for Workflow Building (GUI and Docker Included)

**原文链接**: [https://github.com/empowerd-cms/nyno](https://github.com/empowerd-cms/nyno)

Nyno 3.0 是一个开源、多语言的工作流引擎，专为构建自动化，尤其是 AGI 应用而设计。它允许用户使用 YAML 文件 (.nyno) 创建工作流，并使用 Python、PHP、JavaScript 和 Ruby 对其进行扩展。每种语言都在其自身的高性能工作引擎中执行，从而提高速度和效率。Nyno 利用多进程，为每种语言和 CPU 核心生成多个工作进程。

用户可以通过导出函数，从支持的语言编写的脚本中创建可重用的命令，从而实现与工作流的无缝集成。本文提供了如何定义命令并在 YAML 工作流中使用它们的示例，展示了如何通过上下文对象在步骤之间传递数据。它还提供了用 Python 和 PHP 编写的扩展示例。

Nyno 可以使用 Docker/Podman 安装，方便设置，包括可通过 Web 浏览器访问的 GUI。或者，它可以直接安装在 Linux 主机上，但这需要更多手动依赖项管理（包括 Best.js）。提供的安装说明指导用户完成克隆存储库、构建容器和运行容器的过程。本文还展示了示例工作流和输出，强调了其灵活性和易用性。Nyno 构建于 Best.js 之上，有望成为 Next.js 的更快替代方案。

---

## 31. 如何精密制作钣金零件（光化学蚀刻）[视频]

**原文标题**: How to make precise sheet metal parts (photochemical machining) [video]

**原文链接**: [https://www.youtube.com/watch?v=bR9EN3kUlfg](https://www.youtube.com/watch?v=bR9EN3kUlfg)

这个名为“如何制造精密钣金件（光化学蚀刻）”的YouTube视频，看似是一个演示如何使用光化学蚀刻工艺制造精密钣金件的信息视频。然而，提供的内容仅是标准的YouTube页脚信息（版权、条款、政策等），并未提供关于视频本身的任何具体信息。因此，无法对*视频内容*进行真正的总结。

我们可以根据标题推断，该视频可能涵盖以下内容：

*   **光化学蚀刻（PCM）：** 一种制造工艺，使用化学蚀刻剂从钣金上移除材料，露出由光刻胶掩模定义的区域。这就是它如何制造“精密钣金件”的方式。
*   **工艺步骤：** 该视频可能会详细介绍PCM中涉及的不同步骤，例如：
    *   准备钣金。
    *   涂覆光刻胶涂层。
    *   通过掩模（零件的图案）将光刻胶暴露在紫外线下。
    *   显影暴露的光刻胶。
    *   蚀刻暴露区域的金属。
    *   剥离剩余的光刻胶。
*   **PCM的优势：** 该视频可能还会讨论使用PCM优于其他方法的优势，例如：
    *   高精度和严格的公差。
    *   能够创建复杂的形状和精细的设计。
    *   金属上没有机械应力。
    *   对于中小批量生产具有成本效益。
*   **应用：** 该视频可能会展示使用PCM制造的钣金零件的不同应用。

在没有观看实际视频的情况下，这是基于提供的标题和关于光化学蚀刻的常识所能给出的最佳总结。所列的YouTube页脚信息没有提供任何实际的内容摘要。

---

## 32. 欧盟理事会批准新的“聊天控制”授权，推动大规模监控

**原文标题**: EU Council Approves New "Chat Control" Mandate Pushing Mass Surveillance

**原文链接**: [https://reclaimthenet.org/eu-council-approves-new-chat-control-mandate-pushing-mass-surveillance](https://reclaimthenet.org/eu-council-approves-new-chat-control-mandate-pushing-mass-surveillance)

Reclaimthenet.org网站上的一篇文章报道称，欧盟理事会已批准一项新的“聊天控制”授权，该授权引发了人们对大规模监控的严重担忧。这项授权允许扫描私人通信——包括消息应用程序和电子邮件——以检测和防止在线分享儿童性虐待材料（CSAM）。

批评人士认为，该授权实际上强制对欧盟公民进行大规模监控，侵犯了他们基本的隐私权。他们认为，用于扫描这些通信的技术容易出错，可能导致虚假指控和不必要的调查。有人担心，不加区分的扫描也可能扼杀言论自由，并限制记者和活动人士安全通信的能力。

该文章强调，该授权不能保证端到端加密会得到尊重，因为扫描旨在*在*消息加密*之前*或*之后*在设备上解密*之后*进行。人们还担心，该授权的范围将来可能会扩展到CSAM检测之外，可能涵盖当局认为非法或有害的其他类型的内容。

最终，该文章将欧盟理事会批准“聊天控制”授权视为在欧盟内部加强在线通信监控的重要一步，其既定目标是打击CSAM，但对隐私和言论自由构成重大风险。作者强调了滥用的可能性以及这项立法可能对在线通信产生的寒蝉效应。

---

## 33. 回顾疫情模拟器

**原文标题**: Looking Back at a Pandemic Simulator

**原文链接**: [https://www.raphkoster.com/2025/11/16/looking-back-at-a-pandemic-simulator/](https://www.raphkoster.com/2025/11/16/looking-back-at-a-pandemic-simulator/)

本文讲述了作者在新冠疫情初期时的经历，以及他们如何试图通过一款疫情模拟游戏设计来解决公众对病毒传播的误解。由于公众普遍无法理解疫情的指数级增长以及感染死亡率 (IFR) 和合并症等因素的重要性，作者感到沮丧，于是在 2020 年 3 月在 Facebook 上概述了一个简单的游戏概念。

该游戏旨在模拟病毒的传播、检测、社交隔离和资源管理，并通过个人的姓名和特征来突出人类付出的代价。该帖子引起了游戏开发者的共鸣，促使两个不同的团队创建了可玩的游戏：John Albano 的 “Covid Ops” 和 Khail Santia 领导的 “In the Time of Pandemia”。“In the Time of Pandemia” 获得了广泛的关注，尤其是在菲律宾，因其准确性、教育价值以及传达管理疫情挑战的能力而备受赞誉。作者回顾了他们最初的设计草图的影响，肯定了开发者的辛勤工作，并为将这些游戏包含在他们的简历中辩护，尽管他们没有直接参与开发。最终，作者认为该项目是成功的，其源于提高公众对疫情复杂性和后果的理解的愿望。

---

## 34. GitLab发现大规模NPM供应链攻击

**原文标题**: GitLab discovers widespread NPM supply chain attack

**原文链接**: [https://about.gitlab.com/blog/gitlab-discovers-widespread-npm-supply-chain-attack/](https://about.gitlab.com/blog/gitlab-discovers-widespread-npm-supply-chain-attack/)

GitLab发现大规模供应链攻击，利用进化版“沙虫(Shai-Hulud)”恶意软件针对npm生态系统。该恶意软件通过受感染的npm包传播，并表现出蠕虫般的行为，自动入侵受感染开发者维护的其他包。它会收集GitHub、npm、AWS、GCP和Azure的凭据，并将数据泄露到攻击者控制的GitHub仓库。

该恶意软件的一个关键方面是其“死人开关”机制。如果该恶意软件失去对GitHub（用于数据泄露）和npm（用于传播）的访问权限，它将触发受感染机器上的数据销毁，可能删除用户文件并覆盖磁盘扇区。

初始感染通过一个多阶段加载过程发生，该过程涉及一个修改后的`package.json`文件，其中包含一个指向`setup_bun.js`的preinstall脚本。该加载器下载了一个看似合法的工具，即Bun JavaScript运行时，但实际上执行了一个名为`bun_environment.js`的混淆恶意负载。该恶意软件利用被盗的GitHub令牌创建描述为“Sha1-Hulud: The Second Coming”的公共仓库，用于数据泄露。它还利用被盗的npm令牌，将恶意代码注入到其他包中进行传播。

GitLab建议使用其依赖项扫描功能和Duo Chat的安全分析师代理来检测项目中的受感染包。他们正在积极监控新的感染和攻击变种，并分享调查结果以帮助社区有效应对，同时强调在补救尝试期间触发破坏性“死人开关”的危险。

---

## 35. 虎式编码哲学 (2024)

**原文标题**: Tiger Style: Coding philosophy (2024)

**原文链接**: [https://tigerstyle.dev/](https://tigerstyle.dev/)

虎式编程是一种强调安全性、性能和开发者体验的编码哲学，旨在创建健壮、高效且易于维护的软件。

**核心原则：**

*   **安全性：** 优先编写在所有情况下都能正常工作的代码，减少错误，并值得信赖。
*   **性能：** 专注于高效的资源利用，以实现快速响应的软件。
*   **开发者体验：** 致力于编写可读且易于维护的代码，以鼓励协作并最大限度地减少错误。

**主要设计目标：**

*   **安全性：** 清晰、结构化的实践以防止错误。包括可预测的控制流、有界资源、显式类型、静态内存分配、最小化变量作用域、使用断言进行彻底的错误处理，以及将编译器警告视为错误。
*   **性能：** 在设计中尽早考虑性能，使用“草稿纸估算”进行快速估计。优先考虑高效的资源使用（网络、磁盘、内存、CPU）和可预测的代码执行，以利用 CPU 缓存和分支预测。
*   **开发者体验：** 清晰且一致的命名、对代码背后“原因”的透彻文档记录、逻辑性的代码组织、简单的函数签名以及一致的代码风格。它强调避免重复、干净利落地管理缓冲区分配以及处理差一错误。

该哲学还提倡零技术债务，即第一次就把事情做对，主动解决问题，并通过可靠的代码来建立动力。 通过草稿纸估算进行性能估计有助于早期的设计决策。

---

## 36. Vsora Jotunn-8 5纳米欧洲推理芯片

**原文标题**: Vsora Jotunn-8 5nm European inference chip

**原文链接**: [https://vsora.com/products/jotunn-8/](https://vsora.com/products/jotunn-8/)

Vsora Jotunn-8是一款5纳米欧洲AI推理芯片，专为数据中心内高性能、高性价比和可持续的AI部署而设计。它旨在满足各种应用中对实时AI服务日益增长的需求。该芯片优先考虑超低延迟、极高吞吐量、成本效益和功率效率，以实现大规模AI应用。

Jotunn-8的主要特点和优势包括：

*   **高性能：** 该芯片专为速度、效率和可扩展性而设计，以更低的运营成本实现最大影响。
*   **超低延迟：** 对于聊天机器人、欺诈检测和搜索等实时应用至关重要。
*   **极高吞吐量：** 对于推荐引擎或LLM API等高需求服务至关重要。
*   **成本效益：** 降低每次推理的成本对于业务可行性至关重要。
*   **功率效率：** 每瓦性能是主要关注点，将功耗作为关键的运营支出和碳足迹驱动因素来解决。

Jotunn-8架构支持集成不同的AI模型，包括推理模型、LLM/生成式AI和Agentic AI，从而实现接近理论的性能，以构建更强大和可靠的系统。它允许平滑组合这些算法，利用每种类型的优势，同时减轻它们的劣势。该芯片强调成本效益，为投资提供更高的速度，这对于大规模AI推理至关重要。

---

## 37. 如何使用Linux vsock实现快速虚拟机通信

**原文标题**: How to use Linux vsock for fast VM communication

**原文链接**: [https://popovicu.com/posts/how-to-use-linux-vsock-for-fast-vm-communication/](https://popovicu.com/posts/how-to-use-linux-vsock-for-fast-vm-communication/)

本文介绍了如何使用 Linux vsock 在宿主机和虚拟机 (VM) 之间进行快速高效的通信，特别是使用 gRPC。Vsock 消除了对传统 TCP/IP 网络的需求，为 VM 通信提供了一种简化的方法。

作者演示了一个使用 Bazel 构建 gRPC 服务的实际示例，其中服务器在 VM 内部运行，客户端在宿主机上运行。服务器公开了一个简单的“加法”服务，用于对两个整数求和。本文介绍了处理外部依赖项、从 Protobuf 定义生成 gRPC 库以及构建静态链接的服务器和客户端二进制文件所需的 Bazel 设置。

强调的关键概念包括：

* **Vsock 地址:** 用于指定服务器地址的 `vsock:CID:port` 格式，其中 CID 标识 VM（宿主机为 CID 2，访客通常从 CID 3 开始）。
* **静态链接:** 将服务器和客户端二进制文件进行静态链接简化了到 VM 的部署。
* **QEMU 配置:** 演示了如何使用 `vhost-vsock-pci` 配置带有 vsock 设备的 QEMU VM 并分配 CID。
* **基于 Vsock 的 gRPC:** 展示了 gRPC 如何抽象底层 vsock 实现，从而实现结构化的 RPC 通信。

作者强调了使用 vsock 和 gRPC 创建隔离环境、组合不同操作系统以及利用各种编程语言进行客户端/服务器实现的好处，而无需网络虚拟化的开销。完整的代码可在 GitHub 上找到以供参考。

---

## 38. 瑞士：数据保护官员对当局实施广泛的云禁令

**原文标题**: Switzerland: Data Protection Officers Impose Broad Cloud Ban for Authorities

**原文链接**: [https://www.heise.de/en/news/Switzerland-Data-Protection-Officers-Impose-Broad-Cloud-Ban-for-Authorities-11093477.html](https://www.heise.de/en/news/Switzerland-Data-Protection-Officers-Impose-Broad-Cloud-Ban-for-Authorities-11093477.html)

瑞士数据保护官员禁止瑞士当局使用超大规模云服务，理由是数据安全问题。核心问题是外国政府，特别是美国，可能通过诸如《云法案》之类的法律访问瑞士数据。

该禁令涵盖了亚马逊、微软和谷歌等主要云服务提供商的服务，即使数据存储在瑞士境内。数据保护官员担心这些公司受到外国法律的约束，这些法律可能迫使他们向外国情报机构披露瑞士公民的数据，从而凌驾于瑞士数据保护法之上。

该禁令并非绝对。如果当局实施适当的安全措施并能证明数据得到充分保护以防止未经授权的外国访问，他们仍然可以使用云服务。这可能涉及加密、匿名化或有效阻止外国政府访问的合同协议。然而，要让数据保护官员满意地证明这一点正变得困难。

数据保护官员对数据保护的要求更加严格，导致一些州暂停或推迟云迁移项目。此举突显了对数字化转型的渴望与保护瑞士数据主权和隐私的需求之间的紧张关系。该决定可能对瑞士当局的数字化努力以及该国公共部门云采用的未来产生重大影响。

---

## 39. 欧洲终于开始意识到其经济危机了吗？

**原文标题**: Is Europe Awakening at Last to Its Economic Peril?

**原文链接**: [https://www.wsj.com/opinion/is-europe-awakening-at-last-to-its-economic-peril-2ecfd61b](https://www.wsj.com/opinion/is-europe-awakening-at-last-to-its-economic-peril-2ecfd61b)

无法访问文章链接。

---

## 40. 查尔斯·M·舒尔茨如何创造了查理·布朗和史努比 (2024)

**原文标题**: How Charles M Schulz created Charlie Brown and Snoopy (2024)

**原文链接**: [https://www.bbc.com/culture/article/20241205-how-charles-m-schulz-created-charlie-brown-and-snoopy](https://www.bbc.com/culture/article/20241205-how-charles-m-schulz-created-charlie-brown-and-snoopy)

本文探讨了查尔斯·M·舒尔茨如何创作出备受欢迎的漫画《花生漫画》，重点关注查理·布朗和史努比的塑造。尽管舒尔茨为人谦逊，但他凭借这些引起儿童和成人共鸣的简单绘画建立了一个价值数十亿美元的帝国。他将专注于儿童归因于商业吸引力，并利用他们来探索诸如爱、恨、不信任、恐惧和不安全感等普遍主题。

特别是，史努比是舒尔茨表达想法的出口，常常被描绘得比漫画中的孩子们更聪明。舒尔茨自己作为一个害羞孩子的经历影响了人物和主题。

尽管出版日程很紧张，舒尔茨仍通过排除干扰并专注于创作有趣的东西来保持一致性。他从自己的生活中汲取灵感，旨在反映日常问题。虽然他认为自己作为漫画家的角色是指出问题，而不是解决问题，但《花生漫画》永恒的教训是查理·布朗的毅力。

本文还涉及该漫画的流行程度、美国宇航局对其的使用以及舒尔茨因癌症退休所带来的影响。他死后发表的最后一篇漫画表达了对编辑和粉丝的感谢，以及他对角色的持久喜爱。

---

## 41. 气隙流媒体是什么？以及政府如何在没有互联网的情况下进行流媒体播放

**原文标题**: What Is Air-Gapped Streaming and How Government Streams Without Internet

**原文链接**: [https://www.red5.net/blog/what-is-air-gapped-streaming/](https://www.red5.net/blog/what-is-air-gapped-streaming/)

Red5 CEO Chris Allen谈论气隙流媒体：一种适用于与公共互联网隔离环境（如政府机构或关键基础设施）的解决方案。这些系统需要在保持严格安全和数据主权的同时，进行实时视频、音频或数据流传输。

气隙系统应用于军事、金融网络、工业控制系统、彩票系统以及核电站等生命攸关系统。随着各组织寻求实时查看摄像头画面、按需访问内容以及在安全环境中使用人工智能驱动的分析，对这些解决方案的需求正在增加。

Red5通过其Red5 Pro的“Castaway”插件提供解决方案，该插件允许系统完全离线运行，绕过标准许可检查。这使得可以在无需依赖互联网连接或过时的USB加密狗的情况下进行本地硬件部署。

加州交通局（Caltrans）就是一个实际应用案例，Red5和Nomad Media与AWS合作，将来自气隙网络的实时交通摄像头画面提供给执法部门。这实现了低于500毫秒的延迟，将延迟降低了14到29秒，并实现了跨部门的内容共享。Red5的解决方案使团队能够在维护其隔离系统的同时，添加安全、实时的功能。文章最后强调了气隙流媒体的优势，并推广了Red5的流媒体解决方案。

---

## 42. 使用SIMD加速的C11快速EDN（可扩展数据表示）读取器

**原文标题**: A fast EDN (Extensible Data Notation) reader written in C11 with SIMD boost

**原文链接**: [https://github.com/DotFox/edn.c](https://github.com/DotFox/edn.c)

本文档介绍 `EDN.C`，一个用 C11 编写的快速、零拷贝的 EDN (可扩展数据表示法) 读取器库。EDN 是一种类似于 JSON 的数据格式，但具有更丰富的类型和可扩展性，提供诸如关键字、符号、集合和带标签的字面量等功能。`EDN.C` 具有 SIMD 加速（NEON、SSE4.2、SIMD128）以提高速度，支持 WebAssembly，内存分配极少，API 简单，通过 arena 分配器保证内存安全，零依赖，全面的测试，以及 UTF-8 原生编码。

该库支持各种功能，包括带标签的字面量、映射命名空间语法、扩展字符字面量、元数据、文本块、比率数、扩展整数格式以及数值字面量中的下划线，其中许多是可选的。本文档详细介绍了 macOS、Linux 和 Windows 的安装说明，包括 CMake 和 Make 构建过程。提供了一个快速入门指南，其中包含示例代码，演示如何解析 EDN 字符串、访问值以及处理错误。

本文档广泛介绍了 API 参考，详细说明了核心函数，如 `edn_read` (用于解析 EDN)、`edn_free` (用于内存管理) 和 `edn_type` (用于类型识别)。它还详细阐述了类型系统、错误代码以及如何访问标量类型（字符串、布尔值、整数、大整数、浮点数、大十进制数和比率数）和集合。至关重要的是，它解释了 EDN.C 如何根据 Clojure 规范处理空白字符和控制字符。

---

## 43. 开源Nouveau+NVK对比Nvidia 580 Linux游戏与计算驱动性能

**原文标题**: Open-Source Nouveau+NVK vs. Nvidia 580 Linux Gaming&Compute Driver Performance

**原文链接**: [https://www.phoronix.com/review/nvidia-nvk-linux-618-mesa-26](https://www.phoronix.com/review/nvidia-nvk-linux-618-mesa-26)

2025年11月28日 Phoronix 文章对比了开源 NVIDIA Linux 驱动栈（Nouveau 内核驱动搭配 Mesa NVK Vulkan 驱动、Zink OpenGL-on-Vulkan 和 Rusticl OpenCL）与 NVIDIA 官方 580 系列 Linux 驱动的性能。对比涵盖了游戏/图形和计算工作负载。

文章测试了三种驱动配置：Ubuntu 25.10 的默认 Nouveau/NVK、使用更新的内核和 Mesa 驱动的 NVK Git 版本，以及 NVIDIA 的官方 580.95.05 驱动。这些测试在 GeForce RTX 4070 SUPER、RTX 4080 SUPER 和更新的 RTX 5080 Blackwell 显卡上进行。

目标是深入了解开源 NVIDIA 驱动的当前状态，基于 7 月份的先前测试，突出 NVK、Rusticl 和 Zink 的进展。文章指出先前 Blackwell 显卡测试的问题已得到解决。基准测试套件包括 OpenGL、Vulkan 和 OpenCL 工作负载，以及 OpenCL 峰值性能。

文章分为十页，后续页面详细介绍了 GravityMark、3DMark、DiRT Rally 2、Llama.cpp、Vulkan Compute、OpenCL、FluidX3D 和 ViennaCL 等特定基准测试，最终得出关于性能对比的结论。

---

## 44. 在Linux系统上实现蓝牙LE音频和Auracast

**原文标题**: Implementing Bluetooth LE Audio and Auracast on Linux Systems

**原文链接**: [https://www.collabora.com/news-and-blog/blog/2025/11/24/implementing-bluetooth-le-audio-and-auracast-on-linux-systems/](https://www.collabora.com/news-and-blog/blog/2025/11/24/implementing-bluetooth-le-audio-and-auracast-on-linux-systems/)

本文探讨了在Linux系统上实施蓝牙LE Audio和Auracast，并突出了其相对于蓝牙Classic的优势。LE Audio基于蓝牙低功耗技术，与蓝牙Classic的局限性（导致音质下降和高功耗）相比，LE Audio具有更低的功耗、更低的延迟以及模块化的配置文件框架。Auracast通过公共广播配置文件实现，允许音频同时广播到多个接收器。

在Linux上，LE Audio支持由BlueZ管理蓝牙主机堆栈，PipeWire管理音频路由。设置LE Audio需要较新的Linux内核（6.4或更高版本）、BlueZ和PipeWire版本。硬件支持各不相同，一些控制器支持LE Audio，但不支持Auracast。配置涉及在BlueZ中启用实验性功能，并确保正确的PipeWire设置。

一个挑战在于支持蓝牙Classic和LE Audio的双栈设备，因为在它们之间切换需要断开并重新连接。目前正在改进以解决这个问题。正在进行的开发工作侧重于通过命令行和GUI工具增强可用性，创建统一的呼叫控制API，并进行蓝牙SIG认证测试。Collabora提供在嵌入式Linux系统上部署LE Audio的协助，利用其在软件堆栈方面的专业知识以及对BlueZ和PipeWire的贡献。

---

## 45. OS Malevich – 我们如何打造一个体现简约理念的系统 (2017)

**原文标题**: OS Malevich – how we made a system that embodies the idea of simplicity (2017)

**原文链接**: [https://www.ajax-systems.uz/blog/hub-os-malevich-story/](https://www.ajax-systems.uz/blog/hub-os-malevich-story/)

本文详细介绍了Ajax Systems公司为其安全中心开发的新操作系统OS Malevich的历程，该系统旨在实现简洁性和可扩展性。最初，团队选择了实时操作系统(RTOS)，因为它具有可靠性和严格的时间框架，这对于安全系统至关重要。由于可扩展性问题，团队拒绝了C语言，并因为潜在的漏洞和不可预测的运行时间而拒绝了Linux。

虽然最初基于RTOS的系统满足了基本要求，但来自不同市场的大量功能请求暴露了可扩展性和开发速度的局限性。添加新功能既缓慢又难以测试。为了克服这个问题，团队开始了对操作系统的全面改造，代号为“Malevich”，灵感来源于卡济米尔·马列维奇的“黑色方块”，以强调简洁性。

OS Malevich融合了Linux的元素，例如CPU时间分配和具有标准API的模块化设计，同时保持了RTOS的可靠性。这种混合方法允许更快的开发、更容易的测试和改进的可扩展性。通过分离硬件和软件，并标准化中心、服务器和移动应用程序的开发，Ajax Systems旨在快速实施新功能，而不会影响系统稳定性。即使在执行资源密集型任务时，新操作系统也允许中心最多使用20%的CPU。最终，OS Malevich的目标是为Ajax安全生态系统内的未来增长和创新提供灵活而强大的基础。

---

## 46. 展示 HN：研究论文做成梗图

**原文标题**: Show HN: Research Papers as Memes

**原文链接**: [https://near.tl/tech](https://near.tl/tech)

“Show HN: 研究论文表情包化” 提交介绍了一个名为Neartale的项目，该项目旨在以表情包的形式呈现研究论文。 内容表明这是一种使复杂的学术信息更易于访问和理解的新颖方法，有可能打破更广泛的受众理解研究的障碍。 通过使用流行的、易于消化的表情包格式，Neartale可能试图简化并突出研究论文中的关键发现或概念。 简洁的呈现方式表明该项目处于早期阶段，“Loading...” 表明潜在的持续开发或有限的初始内容。 本质上，Neartale试图将密集的学术写作转化为幽默、可分享且易于理解的视觉格式。

---

## 47. 构建一个NPM蠕虫 (2016)

**原文标题**: Building an NPM Worm (2016)

**原文链接**: [https://contolini.com/building-an-npm-worm](https://contolini.com/building-an-npm-worm)

该2016年的文章探讨了npm由于在包安装期间执行任意脚本而易受自复制蠕虫攻击的漏洞。作者强调了一个恶意包在安装后如何扫描其他node模块，将相同的恶意脚本注入其中，增加其版本号，并尝试将感染版本发布到npm。

作者创建了一个概念验证“pizza-party”来演示这一点。虽然大多数发布尝试都会失败，但感染一些广泛使用软件包的维护者可能会引发大规模爆发，因为开发者通常在其`package.json`文件中使用宽松的语义版本范围说明符。这意味着当感染版本可用时，使用`^`或`~`安装具有依赖项的软件包的用户可能会无意中下载感染版本。

文章强调了撤销蠕虫破坏的难度，需要精确识别和清除感染版本。建议的保护措施包括在不主动管理模块时注销npm，以及使用`npm shrinkwrap`锁定依赖项。作者承认使用开源代码和盲目信任依赖项的固有风险，并建议npm Inc.需要加强安全措施，并呼吁开发者负责任地行动。尽管存在风险，但文章认识到npm和GitHub对开源软件开发的积极影响。

---

## 48. 切尔诺贝利的神秘黑真菌或可吞噬辐射

**原文标题**: The mysterious black fungus from Chernobyl that may eat radiation

**原文链接**: [https://www.bbc.com/future/article/20251125-the-mysterious-black-fungus-from-chernobyl-that-appears-to-eat-radiation](https://www.bbc.com/future/article/20251125-the-mysterious-black-fungus-from-chernobyl-that-appears-to-eat-radiation)

本文探讨了在切尔诺贝利发现的黑真菌的非凡现象，这些真菌似乎能在辐射中茁壮成长。Nelli Zhdanova的研究表明，这些富含黑色素的真菌表现出“放射趋性”，即它们会向放射性粒子生长，而不是受到其伤害。

在此基础上，Ekaterina Dadachova的研究表明，这些真菌可能正在利用辐射获取能量，她将这一过程称为“放射合成”。虽然确切的机制仍是一种理论，但含黑色素的真菌在辐射存在下生长得更快。

美国宇航局的科学家正在探索这些真菌在辐射屏蔽方面的潜力，特别是对于太空中的宇航员。国际空间站的一项研究表明，切尔诺贝利真菌——球孢枝孢菌——在太空中的生长情况更好，因为它暴露于银河宇宙射线。此外，该真菌似乎可以阻挡辐射，这表明黑色素具有保护能力。

使用基于真菌的材料，称为“真菌建筑”，为传统的辐射屏蔽材料（如水或金属）提供了一种潜在的更轻、可自我再生的替代方案，而这些传统材料的运输成本很高。这可以实现更安全的长期太空任务以及月球或火星基地。本质上，已经占领废弃切尔诺贝利的黑霉菌可能掌握着保护未来太空探险家的关键。

---

## 49. 250MWh 'Sand Battery' to start construction in Finland

**原文标题**: 250MWh 'Sand Battery' to start construction in Finland

**原文链接**: [https://www.energy-storage.news/250mwh-sand-battery-to-start-construction-in-finland-for-both-heating-and-ancillary-services/](https://www.energy-storage.news/250mwh-sand-battery-to-start-construction-in-finland-for-both-heating-and-ancillary-services/)

生成摘要时出错

---

## 50. 一个对程序员友好的io_uring和kqueue I/O抽象层 (2022)

**原文标题**: A programmer-friendly I/O abstraction over io_uring and kqueue (2022)

**原文链接**: [https://tigerbeetle.com/blog/2022-11-23-a-friendly-abstraction-over-iouring-and-kqueue/](https://tigerbeetle.com/blog/2022-11-23-a-friendly-abstraction-over-iouring-and-kqueue/)

本文详细介绍了如何在`io_uring`(Linux)和`kqueue`(FreeBSD/macOS)之上构建一个程序员友好的I/O抽象层，其灵感来自libuv和TigerBeetle的I/O库。文章首先对比了阻塞式I/O与使用`io_uring`和`kqueue`的批量I/O，突出了性能优势。文章提倡使用带有I/O完成回调的中央调度器将I/O处理与业务逻辑分离。这种抽象处理了提交和完成队列的复杂性，并使用用户数据字段来跟踪回调。该抽象包括一个`flush`函数，用于提交请求和轮询完成事件，并由`run_for_ns`封装，以便在事件循环中进行时间限制的执行。溢出队列管理无法立即提交的请求。文章对比了 Darwin/macOS (kqueue) 和 Linux (io_uring) 的实现，展示了 macOS 中如何需要用户态的 `send` 调用。最后，文章简要提及了 Windows IOCP，并讨论了单线程与多线程事件循环架构，然后暗示了未来用 Zig 编写的独立、跨平台 I/O 库。

---

## 51. PocketBase MCP服务器

**原文标题**: PocketBase MCP Server

**原文链接**: [https://github.com/ssakone/pb_mcp_server](https://github.com/ssakone/pb_mcp_server)

本文档介绍了PocketBase MCP服务器，该工具允许AI助手和其他MCP客户端与PocketBase数据库进行交互。它提供了对PocketBase功能的全面访问，包括身份验证、数据管理和管理操作。

主要功能包括：具有会话持久性的管理员和用户身份验证，启动时自动身份验证，集合和记录管理（CRUD操作），用户管理，自定义HTTP标头，原始HTTP请求发送，查询支持（过滤、排序、分页），一致的错误处理，多实例支持，以及可选的TOON输出格式，用于减少LLM的token。

服务器可以通过`git`和`npm`安装。配置通过环境变量或`pocketbase.config.json`文件处理，指定PocketBase URL、管理员token和输出格式。它可以在`stdio`模式下为MCP客户端运行，也可以在HTTP/SSE模式下为Web客户端运行。

本文档详细介绍了可用工具，包括身份验证、集合管理、记录CRUD、用户管理和自定义HTTP请求。每个工具描述都包括参数、类型和描述。 `send_custom_request`工具因其与任何PocketBase API端点交互的灵活性而突出显示。 提供了过滤、批处理操作、验证和运行状况检查的使用示例。 错误处理已标准化，带有信息丰富的消息和错误代码。 本文档还提供了有关PocketBase过滤器语法和开发设置的详细信息。

---

## 52. 肖尔算法：明日终结RSA/ECC的量子算法

**原文标题**: Shor's algorithm: the one quantum algo that ends RSA/ECC tomorrow

**原文链接**: [https://blog.ellipticc.com/posts/what-is-shors-algorithm-and-why-its-the-single-biggest-threat-to-classical-cryptography/](https://blog.ellipticc.com/posts/what-is-shors-algorithm-and-why-its-the-single-biggest-threat-to-classical-cryptography/)

肖尔算法，正如文章所述，是一种量子算法，对广泛使用的经典密码系统，如RSA和椭圆曲线密码学（ECC）构成了重大威胁。这些系统依赖于大数分解（对于RSA）或求解椭圆曲线离散对数问题（对于ECC）的数学难度。

肖尔算法利用量子力学的原理来高效地解决这些问题。它使量子计算机能够以比已知最佳经典算法快指数级的速度分解大数。这意味着使用RSA和ECC加密数据的密钥，用经典计算机需要数百年甚至数千年才能破解，而用足够强大的量子计算机可能只需数小时、数天或数周即可破解。

文章可能解释了肖尔算法通过将分解问题转化为周期查找问题来工作。量子计算机擅长查找模式和周期性，这归功于它们能够同时存在于多种状态（叠加）并干扰这些状态（量子干涉）。该算法使用量子傅里叶变换来有效地识别周期，从而得到原始数字的因子。

量子计算机成功运行肖尔算法的后果将是安全通信和数据存储系统的广泛脆弱性。这包括金融交易、政府机密以及受RSA或ECC保护的任何其他敏感信息。文章可能最后强调开发后量子密码学（PQC）的紧迫性，后量子密码学是能够抵抗经典计算机和量子计算机攻击的密码算法，以减轻这种威胁。

---

## 53. 展示HN：DB Pro – 一款适用于Postgres、MySQL、SQLite和LibSQL的现代桌面客户端

**原文标题**: Show HN: DB Pro – A Modern Desktop Client for Postgres, MySQL, SQLite and LibSQL

**原文链接**: [https://www.dbpro.app/](https://www.dbpro.app/)

DB Pro 是一款全新的桌面应用程序，专为开发者设计，用于管理 PostgreSQL、MySQL、SQLite、Supabase 和 Turso 数据库。它提供了一个现代化的界面，具有可视化变更审查、内联数据编辑、原始 SQL 编辑器、完整数据库活动日志和可视化模式浏览器等功能。用户还可以标记表以实现更好的组织。

该应用程序旨在成为一个全面的数据库工作台，并计划在未来添加仪表板、工作流以及对更多数据库（包括 MongoDB、MariaDB、Redis 和 Neon）的支持。公开路线图详细介绍了即将推出的功能，涵盖查询工作台、仪表板与洞察、工作流构建器、集成、AI驱动的聊天、性能测试、DB Pro 云、可视化 ERD 设计器和触发器等类别。

DB Pro 提供包含基本功能的免费层级，以及每月 9.99 美元的付费“Solo”层级，该层级可解锁无限连接、选项卡、表标签、导出，并支持最多 3 个设备和电子邮件支持。具有团队协作功能的“Team”层级和具有专属支持的“Enterprise”层级即将推出。该应用程序目前适用于 macOS，并计划推出 Windows 和 Linux 版本。用户可以下载免费版本以开始使用。

---

## 54. TPUv7：谷歌剑指王者

**原文标题**: TPUv7: Google Takes a Swing at the King

**原文链接**: [https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the](https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the)

TPUv7：谷歌挥拳挑战AI芯片霸主地位

---

## 55. Maxduino 评测：多款复古电脑磁带盒仿真器

**原文标题**: Maxduino Review: Tape Cassette Emulator for Multiple Retro Computers

**原文链接**: [https://retrogamecoders.com/maxduino-review/](https://retrogamecoders.com/maxduino-review/)

Maxduino是一款磁带盒式录音机模拟器，适用于各种复古电脑，旨在用现代SD卡接口取代缓慢且不可靠的磁带加载过程。 RetroGameCoders的评测强调了其广泛的兼容性，通过可互换的固件支持 Commodore 64、ZX Spectrum、Amstrad CPC、Atari 8位电脑等机器。

Maxduino 的主要优势在于其加载游戏和程序的速度明显快于传统磁带驱动器。它可以从 SD 卡读取 .TAP、.CDT、.TZX 和其他常见的磁带映像格式，并输出一个模仿磁带驱动器的信号，使复古电脑能够加载数据。

评测提到该设备设置相对容易，只需连接到电脑的磁带端口即可。 SD 卡内容的导航通过 Maxduino 上的按钮和小屏幕进行。 Maxduino 的不同型号提供各种功能，例如用于输出音频的内置放大器和扬声器，以及不同的外壳设计。

虽然评测没有明确说明任何主要缺点，但它含蓄地指出 Maxduino 依赖于容易获得且兼容的磁带映像格式。评测侧重于其功能、兼容性和易用性，将其定位为复古计算爱好者寻找便捷高效的软件加载方式的宝贵工具。源于其多系统兼容性的多功能性进一步增强了其吸引力。

---

## 56. 模拟两个六面骰子的十一面骰子

**原文标题**: The Eleven-Faced Die That Emulates Two Six-Sided Dice

**原文链接**: [https://hackaday.com/2025/11/28/the-eleven-faced-die-that-emulates-two-six-sided-dice/](https://hackaday.com/2025/11/28/the-eleven-faced-die-that-emulates-two-six-sided-dice/)

研究人员创造了一种十一面骰子，它可以复制掷两个六面骰子（2d6）的概率分布。这意味着，该骰子在掷出时，会产生从2到12的结果，其概率分布与2d6的钟形曲线相同，使得7是最可能的结果，而2和12是最不可能的结果。

这项开发源于一项研究，该研究致力于预测刚体的稳定静止状态，而无需依赖模拟。这种新方法是可微的，从而可以设计具有特定概率分布的形状。例如，该团队还能够设计一个具有25%-50%-25%自定义分布的三面骰子。

创造者侯赛因·巴克塔什已经提供了用于打印的3D模型。初步的物理测试表明，该骰子的性能与理论预测相符，尤其是在硬表面上滚动时。然而，尚未进行自动化测试来最终确认这种新型骰子的准确性和可靠性。

---

## 57. 骁龙 8 Gen 5 精英版当日上游 Linux 支持

**原文标题**: Same-day upstream Linux support for Snapdragon 8 Elite Gen 5

**原文链接**: [https://www.qualcomm.com/developer/blog/2025/10/same-day-snapdragon-8-elite-gen-5-upstream-linux-support](https://www.qualcomm.com/developer/blog/2025/10/same-day-snapdragon-8-elite-gen-5-upstream-linux-support)

本文宣布骁龙8 Elite Gen 5处理器现已支持同日上游Linux。

关键在于，这款新型骁龙处理器通过标准渠道（上游）即可快速、完整地获得Linux支持。 这表明了对开源兼容性的承诺，并使Linux开发者和用户能够立即在其Linux环境中使用骁龙8 Elite Gen 5的全部功能，而无需依赖自定义补丁或等待延迟的驱动程序开发。

---

## 58. 独立，孤身，独自摸索

**原文标题**: Indie, alone, and figuring it out

**原文链接**: [https://danijelavrzan.com/posts/2025/11/indie-dev/](https://danijelavrzan.com/posts/2025/11/indie-dev/)

本文探讨了独立应用开发者的现实情况，将最初对自由的向往与迈出这一步后遇到的挑战进行了对比。虽然摆脱朝九晚五的工作很有吸引力，但独立开发者很快发现他们要负责业务的方方面面：开发、设计、产品管理、营销、分析和客户支持。

作者强调了独自工作的孤独和压力，突出了持续的决策和情境切换需求。虽然在线社区提供支持，但这与团队环境不同。

文章的很大一部分重点介绍了对成功至关重要的非编码任务，例如营销、应用商店优化（ASO）和付费墙实施。用户反馈至关重要，它塑造了应用程序的方向，并要求开发人员在各种意见与他们自己的愿景之间取得平衡。

时间管理变得至关重要，需要在功能开发、错误修复、用户支持和营销之间进行仔细的优先级排序。尽管要求很高，但作者发现独立生活是有回报的，提供了灵活性和持续学习的机会。

文章简要地提到了人工智能的作用，承认其有潜力加速开发并协助调试和文案撰写等任务，同时告诫不要过度依赖，尤其是在新技术方面。

最后，作者分享了有抱负的独立开发者的宝贵资源，包括ASO工具、独立开发课程以及涵盖应用程序开发基本非编码方面的书籍。 尽管面临挑战，作者仍然享受这段旅程，并在它提供的自主权和学习机会中找到满足感。

---

## 59. 2025年安装Java及版本管理器

**原文标题**: Installing Java in 2025, and Version Managers

**原文链接**: [https://blog.hakanserce.com/post/version_managers/](https://blog.hakanserce.com/post/version_managers/)

本文探讨了在现代开发环境中安装和管理Java的复杂性，这与过去简单的流程形成了鲜明对比。Java供应商（Oracle、Amazon、Red Hat、Eclipse等）的激增以及多种长期支持(LTS)版本（8、11、17、21等）的可用性，使得选择和管理正确的版本成为一项重大挑战，尤其是在不同项目通常需要不同版本的情况下。

本文对比了手动安装（下载安装程序，管理PATH）与使用诸如SDKMAN!之类的版本管理器。版本管理器为安装、更新和切换不同语言和运行时版本提供了一个统一的界面，充当针对版本控制进行优化的软件包管理器。SDKMAN! 的例子演示了用于列出、安装和选择Java版本的命令，包括全局和基于项目的版本。

版本管理器的优势包括简单性、可重现性、隔离性、轻松升级、清理和发现。本文重点介绍了各种语言的流行版本管理器：用于Python的pyenv，用于Node.js的nvm，用于Java/Kotlin/Scala/Groovy的SDKMAN!，以及用于Ruby的rbenv。像asdf-vm和vfox这样的工具可以处理多种语言。本文鼓励开发人员采用版本管理器以改进工作流程，并得出结论，版本管理器对于现代软件开发至关重要，简化了多种语言版本和发行版的管理。

---

## 60. 男子用1000块回收笔记本电脑电池供电自家8年

**原文标题**: A Man Powers His Home for 8 Years Using 1k Recycled Laptop Batteries

**原文链接**: [https://scienceclock.com/a-man-powers-his-home-for-8-years-using-1000-recycled-laptop-batteries/](https://scienceclock.com/a-man-powers-his-home-for-8-years-using-1000-recycled-laptop-batteries/)

八年来，一位名叫格鲁布克斯的男子一直用自制系统为他的家供电，该系统由1000多块回收的笔记本电脑电池组成。他于2016年启动该项目，旨在通过太阳能电池板和再利用的电池相结合来实现电网独立。

最初的设置包括一个1.4千瓦的太阳能电池板系统、一个叉车电池和逆变器。格鲁布克斯通过收集和再利用废弃的笔记本电脑电池来扩展系统，他认识到这些电池作为可再生能源的潜力。他建造了一个单独的仓库来存放不断增长的电池组、充电控制器和逆变器。

这个过程包括拆卸笔记本电脑电池，取出单个电芯，并将它们整理到定制的机架中。这项劳动密集型的工作解决了放电率不均的问题，并确保了高效运行。该系统从一个小型的装置发展到中间阶段由650块电池供电，最终超过了1000块电池。

目前的系统配备了24块太阳能电池板，每块额定功率为440瓦。值得注意的是，格鲁布克斯声称八年来没有电池需要更换，也没有发生火灾或电池膨胀等重大问题。该系统成功地为他的家庭和电器供电，证明了再利用电子垃圾来获得可持续能源解决方案的潜力。

---

## 61. TPU vs. GPU：以及为何谷歌有望赢得长期人工智能竞赛

**原文标题**: TPUs vs. GPUs and why Google is positioned to win AI race in the long term

**原文链接**: [https://www.uncoveralpha.com/p/the-chip-made-for-the-ai-inference](https://www.uncoveralpha.com/p/the-chip-made-for-the-ai-inference)

深入剖析谷歌张量处理器 (TPU)：人工智能竞赛中的长期优势

---

## 62. 珠子 – 为你的编码代理提供的内存升级

**原文标题**: Beads – A memory upgrade for your coding agent

**原文链接**: [https://github.com/steveyegge/beads](https://github.com/steveyegge/beads)

Beads：编码代理的“记忆升级”，轻量级图结构问题追踪器，旨在提升组织性、专注度和长期任务处理能力。0.20.1版本引入多工作者支持的重大升级，通过将顺序问题ID切换为防冲突的哈希ID（例如，bd-a1b2）实现。这消除了多代理或多分支工作流中的合并冲突。

主要功能包括零配置、依赖追踪、就绪工作检测、git版本控制、分布式设计、可选代理邮件、受保护分支支持、可扩展性、依赖树、审计追踪和记忆衰减。Beads主要为AI编码代理设计，而非直接的人工交互。代理自动提交和管理问题，改善长期规划并防止工作丢失。它以git为后盾，就像一个由所有代理共享的托管SQL数据库。

安装简单，可通过npm、快速安装脚本和Homebrew进行安装。设置包括在项目根目录下运行`bd init`。本文强调配置`AGENTS.md`文件以及会话结束协议的重要性，以确保代理正确管理问题追踪和数据库同步。Beads自动将本地数据库与git同步，并提供手动或禁用自动同步的选项。隐身模式提供隔离的使用，对合作者隐藏与beads相关的文件。

---

## 63. 汇丰银行估计，OpenAI到2030年将无法盈利，并且还需要额外2070亿美元。

**原文标题**: OpenAI won't make money by 2030 and needs another $207B, HSBC estimates

**原文链接**: [https://fortune.com/2025/11/26/is-openai-profitable-forecast-data-center-200-billion-shortfall-hsbc/](https://fortune.com/2025/11/26/is-openai-profitable-forecast-data-center-200-billion-shortfall-hsbc/)

汇丰银行预计OpenAI到2030年都无法实现盈利，并需要额外2070亿美元的资金来支持其增长计划，主要原因是基础设施成本（数据中心和计算）飙升。尽管汇丰银行承认人工智能是一个重要趋势，并预计OpenAI将保持领先的收入地位，但该公司面临着巨大的财务障碍才能实现其雄心壮志。

OpenAI的累计自由现金流预计到2030年仍将为负，从2025年末到2030年，云和人工智能基础设施成本将达到7920亿美元，到2033年，总计算承诺将达到1.4万亿美元。即使拥有不断增长的订阅用户群和潜在的数字广告收入，预计收入也无法弥补这一差距。

汇丰银行提出了几种弥补这一差距的方案，包括增加付费订阅用户、获取更多广告收入或提高计算效率。然而，即使在乐观的情况下，2030年以后仍需要更多资金。

OpenAI的生存高度依赖于微软和亚马逊等支持者以及整个AI生态系统。潜在的风险包括未经证实的收入模式、市场饱和、监管审查以及所需资本注入的巨大规模。发行更多债务是一种可能的途径，但当前的市场状况充满挑战。

文章还提到了关于技术实际生产力提升的争论，并指出有人担心互联网革命并没有显著提高办公室或工厂的生产力。对数据中心和硬件日益增长的关注引发了人们对基于未来、可能不确定的AI回报的增长可持续性的质疑。

---

## 64. Mixpanel 安全漏洞

**原文标题**: Mixpanel Security Breach

**原文链接**: [https://mixpanel.com/blog/sms-security-incident/](https://mixpanel.com/blog/sms-security-incident/)

2025年11月8日，Mixpanel检测并响应了一起短信钓鱼攻击，该攻击导致少量客户账户遭到未授权访问。他们立即启动事件响应，控制了漏洞，并在外部网络安全合作伙伴的帮助下保护了受影响的用户账户。

Mixpanel主动联系了所有受影响的客户。如果客户没有收到来自Mixpanel的通知，则其账户未受影响。

该公司采取了多项措施来减轻损失，包括：

*   保护受影响的账户
*   撤销活动会话和登录
*   轮换被盗凭据
*   阻止恶意IP地址
*   在其SIEM平台中注册入侵指标（IOC）
*   为员工执行全局密码重置
*   聘请第三方取证公司
*   对日志进行取证审查
*   实施额外的安全控制
*   与执法部门和网络安全顾问合作

Mixpanel建议收到通知的客户查看通知中的具体说明。 其他客户未受影响。如有任何问题，请发送至support@mixpanel.com。 在首席执行官Jen Taylor的领导下，该公司强调其对安全和透明沟通的承诺。

---

## 65. 2D光线步进软阴影 (2020)

**原文标题**: Ray Marching Soft Shadows in 2D (2020)

**原文链接**: [https://www.rykap.com/2020/09/23/distance-fields/](https://www.rykap.com/2020/09/23/distance-fields/)

本文阐述了如何使用距离场在2D中实现光线步进软阴影。作者的演示程序从文本生成距离场，并使用光线步进来确定每个像素的阴影强度。

光线步进涉及从像素向光源投射光线。距离场提供到最近形状的距离，允许光线安全地前进，而不会跳过对象。核心算法检查光线在到达光源之前是否与任何形状相交。

为了实现软阴影，作者使用了三个规则：

1.  **接近交点：** 光线越接近与形状相交，像素应该越阴暗。这可以通过光线步进期间到形状的最小距离（sceneDist）来近似。
2.  **远离交点：** 像素距离光线几乎与形状相交的点越远，阴影应该扩散得越多。这可以通过光线的进程（rayProgress）来近似。
3.  **光衰减：** 光线随着与光源距离的增加而减弱。

这些规则通过在每个步骤中计算 `sceneDist / rayProgress` 来实现，保持最小值，然后将其乘以基于光线衰减的距离因子。

本文还提到了常见的伪影，例如条带，这是由于采取的光线步进步骤太少时，距离近似不准确而造成的。作者引入随机抖动来减轻条带，但承认这是一种权衡。作者最后邀请进一步讨论，并暗示未来的文章将涵盖对演示程序的额外调整。

---

## 66. Penpot：开源的Figma

**原文标题**: Penpot: The Open-Source Figma

**原文链接**: [https://github.com/penpot/penpot](https://github.com/penpot/penpot)

Penpot 是一款开源设计和代码协作工具，定位为 Figma 的替代品。它允许设计师创建设计、交互式原型和设计系统，同时为开发者提供可直接使用的代码，从而简化设计到开发的流程。它可以在浏览器上使用或进行自托管，并支持 SVG、CSS、HTML 和 JSON 等开放标准。Penpot 可以免费使用。

主要功能包括用于单一数据源的原生设计令牌、CSS Grid Layout、重新设计的 UI 和新的组件系统。它还拥有一个插件系统，用于扩展功能并与其他应用程序集成。开发者可以受益于实时协作或单人工作选项、提供即时代码片段访问的检查模式，以及通过 Webhook 和 API 与开发工具链的集成。

Penpot 支持使用设计令牌、组件和变体构建设计系统。用户可以通过 SaaS 部署 Penpot，也可以通过 Docker、Kubernetes 或 Elestio 自行安装。

Penpot 社区积极鼓励通过设计、代码和想法参与、贡献和改进该平台。《行为准则》确保了积极的环境。贡献方式包括创建库和模板、邀请团队、提供反馈、报告错误、成为翻译者以及为代码库做出贡献。提供文档、教程和开发日记等资源。Penpot Fest 计划于 2025 年 10 月 9 日至 10 日在西班牙马德里举行。

---

## 67. 比较 xeus-Haskell 和 ihaskell 内核

**原文标题**: Comparing xeus-Haskell and ihaskell kernels

**原文链接**: [https://www.datahaskell.org/blog/2025/11/25/a-tale-of-two-kernels.html](https://www.datahaskell.org/blog/2025/11/25/a-tale-of-two-kernels.html)

本文比较了两个用于Jupyter Notebook的Haskell内核：IHaskell和xeus-haskell。IHaskell采用单体式方法，直接实现Jupyter协议并使用GHC API。这使其能够利用完整的GHC生态系统，但同时也将其与特定的GHC版本紧密联系在一起，导致潜在的安装和包管理复杂性。

Xeus-haskell采用中间件方法，将协议处理委托给Xeus C++库，并使用MicroHs，一个更小的Haskell解释器。这带来了更小的运行时占用空间、更快的启动速度和更简便的部署，尤其是在WebAssembly等环境中。然而，它仅支持与MicroHs兼容的Haskell特性和库的有限子集。

两者之间的主要区别在于它们的生态系统、易用性、性能和部署场景。IHaskell凭借其对完整GHC生态系统的访问和原生性能，在服务器端数据科学方面表现出色。Xeus-haskell在客户端执行、交互式文档和快速原型设计方面表现出色，并提供更简单的安装体验。IHaskell的GHC依赖性使其更适合繁重的工作负载，而xeus-haskell非常适合Haskell功能的轻量级嵌入。选择取决于具体的用例：IHaskell适用于已建立的服务器设置和完整的GHC支持，xeus-haskell适用于可移植性和简单性，尤其是在JupyterLite中。

---

## 68. Voyager 1 is about to reach one light-day from Earth

**原文标题**: Voyager 1 is about to reach one light-day from Earth

**原文链接**: [https://scienceclock.com/voyager-1-is-about-to-reach-one-light-day-from-earth/](https://scienceclock.com/voyager-1-is-about-to-reach-one-light-day-from-earth/)

生成摘要时出错

---

## 69. The three thousand year journey of colchicine

**原文标题**: The three thousand year journey of colchicine

**原文链接**: [https://www.worksinprogress.news/p/the-three-thousand-year-journey-of](https://www.worksinprogress.news/p/the-three-thousand-year-journey-of)

生成摘要时出错

---

## 70. DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning [pdf]

**原文标题**: DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning [pdf]

**原文链接**: [https://github.com/deepseek-ai/DeepSeek-Math-V2/blob/main/DeepSeekMath_V2.pdf](https://github.com/deepseek-ai/DeepSeek-Math-V2/blob/main/DeepSeekMath_V2.pdf)

生成摘要时出错

---

## 71. Lap around Australia in a small electric car

**原文标题**: Lap around Australia in a small electric car

**原文链接**: [https://thedriven.io/2025/11/27/fun-and-easy-our-lap-around-australia-with-a-family-of-four-in-a-small-electric-dolphin/](https://thedriven.io/2025/11/27/fun-and-easy-our-lap-around-australia-with-a-family-of-four-in-a-small-electric-dolphin/)

生成摘要时出错

---

## 72. Great Math Software: List of fun visual math programs

**原文标题**: Great Math Software: List of fun visual math programs

**原文链接**: [http://xahlee.info/math_software/mathPrograms.html](http://xahlee.info/math_software/mathPrograms.html)

生成摘要时出错

---

## 73. Africa's forests have switched from absorbing to emitting carbon

**原文标题**: Africa's forests have switched from absorbing to emitting carbon

**原文链接**: [https://phys.org/news/2025-11-africa-forests-absorbing-emitting-carbon.html](https://phys.org/news/2025-11-africa-forests-absorbing-emitting-carbon.html)

生成摘要时出错

---

## 74. Experimenting with Robin Hood Hashing

**原文标题**: Experimenting with Robin Hood Hashing

**原文链接**: [https://twdev.blog/2025/11/robin_hood/](https://twdev.blog/2025/11/robin_hood/)

生成摘要时出错

---

## 75. Giving the Jakks Atari Paddle a Spin

**原文标题**: Giving the Jakks Atari Paddle a Spin

**原文链接**: [https://nicole.express/2025/paddle-me-atari.html](https://nicole.express/2025/paddle-me-atari.html)

生成摘要时出错

---

## 76. Optery (YC W22) Hiring CISO, Release Manager, Tech Lead (Node), Full Stack Eng

**原文标题**: Optery (YC W22) Hiring CISO, Release Manager, Tech Lead (Node), Full Stack Eng

**原文链接**: [https://www.optery.com/careers/](https://www.optery.com/careers/)

生成摘要时出错

---

## 77. Quake Engine Indicators

**原文标题**: Quake Engine Indicators

**原文链接**: [https://fabiensanglard.net/quake_indicators/index.html](https://fabiensanglard.net/quake_indicators/index.html)

生成摘要时出错

---

## 78. Designing a Mechanical Calculator

**原文标题**: Designing a Mechanical Calculator

**原文链接**: [https://signoregalilei.com/2025/11/22/designing-a-mechanical-calculator/](https://signoregalilei.com/2025/11/22/designing-a-mechanical-calculator/)

生成摘要时出错

---

## 79. Linux Kernel Explorer

**原文标题**: Linux Kernel Explorer

**原文链接**: [https://reverser.dev/linux-kernel-explorer](https://reverser.dev/linux-kernel-explorer)

生成摘要时出错

---

## 80. Physicists drive antihydrogen breakthrough at CERN

**原文标题**: Physicists drive antihydrogen breakthrough at CERN

**原文链接**: [https://phys.org/news/2025-11-physicists-antihydrogen-breakthrough-cern-technique.html](https://phys.org/news/2025-11-physicists-antihydrogen-breakthrough-cern-technique.html)

生成摘要时出错

---

## 81. Feedback doesn't scale

**原文标题**: Feedback doesn't scale

**原文链接**: [https://another.rodeo/feedback/](https://another.rodeo/feedback/)

生成摘要时出错

---

## 82. Willis Whitfield: Creator of clean room technology still in use today (2024)

**原文标题**: Willis Whitfield: Creator of clean room technology still in use today (2024)

**原文链接**: [https://www.sandia.gov/labnews/2024/04/04/willis-whitfield-a-simple-man-with-a-simple-solution-that-changed-the-world/](https://www.sandia.gov/labnews/2024/04/04/willis-whitfield-a-simple-man-with-a-simple-solution-that-changed-the-world/)

生成摘要时出错

---

## 83. Interactive λ-Reduction

**原文标题**: Interactive λ-Reduction

**原文链接**: [https://deltanets.org/](https://deltanets.org/)

生成摘要时出错

---

## 84. G0-G3 corners, visualised: learn what "Apple corners" are

**原文标题**: G0-G3 corners, visualised: learn what "Apple corners" are

**原文链接**: [https://www.printables.com/model/1490911-g0-g3-corners-visualised-learn-what-apple-corners](https://www.printables.com/model/1490911-g0-g3-corners-visualised-learn-what-apple-corners)

生成摘要时出错

---

## 85. A $1M Dollar Apple Macintosh PowerBook 170

**原文标题**: A $1M Dollar Apple Macintosh PowerBook 170

**原文链接**: [https://www.ebay.ca/itm/326104837538](https://www.ebay.ca/itm/326104837538)

生成摘要时出错

---

## 86. Inspired by Spider-Man, scientists recreate web-slinging technology

**原文标题**: Inspired by Spider-Man, scientists recreate web-slinging technology

**原文链接**: [https://scienceclock.com/inspired-by-spider-man-scientists-recreate-web-slinging-technology/](https://scienceclock.com/inspired-by-spider-man-scientists-recreate-web-slinging-technology/)

生成摘要时出错

---

## 87. The current state of the theory that GPL propagates to AI models

**原文标题**: The current state of the theory that GPL propagates to AI models

**原文链接**: [https://shujisado.org/2025/11/27/gpl-propagates-to-ai-models-trained-on-gpl-code/](https://shujisado.org/2025/11/27/gpl-propagates-to-ai-models-trained-on-gpl-code/)

生成摘要时出错

---

## 88. The current state of the theory that GPL propagates to AI models

**原文标题**: The current state of the theory that GPL propagates to AI models

**原文链接**: [https://shujisado.org/2025/11/27/gpl-propagates-to-ai-models-trained-on-gpl-code/](https://shujisado.org/2025/11/27/gpl-propagates-to-ai-models-trained-on-gpl-code/)

生成摘要时出错

---

## 89. Memories of .us

**原文标题**: Memories of .us

**原文链接**: [https://computer.rip/2025-11-11-dot-us.html](https://computer.rip/2025-11-11-dot-us.html)

生成摘要时出错

---

## 90. Cats became our companions way later than you think

**原文标题**: Cats became our companions way later than you think

**原文链接**: [https://www.bbc.co.uk/news/articles/cq8dvdp9gn7o](https://www.bbc.co.uk/news/articles/cq8dvdp9gn7o)

生成摘要时出错

---

## 91. Humans Have Tilted the Earth 31.5 Inches Since 1993, Study Finds (2023)

**原文标题**: Humans Have Tilted the Earth 31.5 Inches Since 1993, Study Finds (2023)

**原文链接**: [https://scienceclock.com/humans-have-titled-the-earth-31-5-inches-since-1993-study-finds/](https://scienceclock.com/humans-have-titled-the-earth-31-5-inches-since-1993-study-finds/)

生成摘要时出错

---

## 92. Show HN: KiDoom – Running DOOM on PCB Traces

**原文标题**: Show HN: KiDoom – Running DOOM on PCB Traces

**原文链接**: [https://www.mikeayles.com/#kidoom](https://www.mikeayles.com/#kidoom)

生成摘要时出错

---

## 93. Underrated reasons to be thankful V

**原文标题**: Underrated reasons to be thankful V

**原文链接**: [https://dynomight.net/thanks-5/](https://dynomight.net/thanks-5/)

生成摘要时出错

---

## 94. ML-KEM Mythbusting

**原文标题**: ML-KEM Mythbusting

**原文链接**: [https://keymaterial.net/2025/11/27/ml-kem-mythbusting/](https://keymaterial.net/2025/11/27/ml-kem-mythbusting/)

生成摘要时出错

---

## 95. Indie game developers have a new sales pitch: being 'AI free'

**原文标题**: Indie game developers have a new sales pitch: being 'AI free'

**原文链接**: [https://www.theverge.com/entertainment/827650/indie-developers-gen-ai-nexon-arc-raiders](https://www.theverge.com/entertainment/827650/indie-developers-gen-ai-nexon-arc-raiders)

生成摘要时出错

---

## 96. Functional Data Structures and Algorithms: a Proof Assistant Approach

**原文标题**: Functional Data Structures and Algorithms: a Proof Assistant Approach

**原文链接**: [https://fdsa-book.net/](https://fdsa-book.net/)

生成摘要时出错

---

## 97. 10 years of writing a blog nobody reads

**原文标题**: 10 years of writing a blog nobody reads

**原文链接**: [https://flowtwo.io/post/on-10-years-of-writing-a-blog-nobody-reads](https://flowtwo.io/post/on-10-years-of-writing-a-blog-nobody-reads)

生成摘要时出错

---

## 98. Technical Deflation

**原文标题**: Technical Deflation

**原文链接**: [https://benanderson.work/blog/technical-deflation/](https://benanderson.work/blog/technical-deflation/)

生成摘要时出错

---

## 99. Janet Yellen Says the US Is Undermining Its Economic Success

**原文标题**: Janet Yellen Says the US Is Undermining Its Economic Success

**原文链接**: [https://www.bloomberg.com/news/articles/2025-11-14/janet-yellen-warns-about-economic-risk-of-trump-s-tariffs-funding-cuts](https://www.bloomberg.com/news/articles/2025-11-14/janet-yellen-warns-about-economic-risk-of-trump-s-tariffs-funding-cuts)

生成摘要时出错

---

## 100. Show HN: Runprompt – run .prompt files from the command line

**原文标题**: Show HN: Runprompt – run .prompt files from the command line

**原文链接**: [https://github.com/chr15m/runprompt](https://github.com/chr15m/runprompt)

生成摘要时出错

---

