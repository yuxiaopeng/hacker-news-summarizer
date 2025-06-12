# Hacker News 热门文章摘要 (2025-06-12)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. macOS Tahoe 带来全新磁盘映像格式

**原文标题**: macOS Tahoe brings a new disk image format

**原文链接**: [https://eclecticlight.co/2025/06/12/macos-tahoe-brings-a-new-disk-image-format/](https://eclecticlight.co/2025/06/12/macos-tahoe-brings-a-new-disk-image-format/)

本文介绍 ASIF，一种在 macOS Tahoe (版本 26) 中首次亮相的新型磁盘映像格式。与可能存在性能瓶颈的旧格式不同，ASIF 旨在提供接近原生的速度，使其特别适用于轻量级虚拟化和通用磁盘映像使用。

ASIF 映像是 APFS 中的稀疏文件，其大小根据存储的数据动态调整。目前，创建仅限于 macOS Tahoe 的“磁盘工具”或 `diskutil` 命令，但它们可以在 macOS Sequoia (版本 15.5) 中使用。本文详细介绍了如何使用 `diskutil` 命令创建 ASIF 映像。

性能测试表明，与旧格式（如 UDIF 读写 (UDRW) 和 UDSP 稀疏映像）相比，ASIF 在速度方面有了显著提高，尤其是在未加密和加密的 APFS 卷上的读写速度方面。作者观察到内部 SSD 的读取和写入速度约为 5.5-8.3 GB/s，显示出明显的优势。

本文建议虚拟化程序应采用 ASIF 映像，以提高 VM 性能，前提是该格式已得到正确实施。它还强调，虽然 Sequoia 15.5 支持 ASIF，但与旧版 macOS 版本的兼容性仍不清楚。对于 macOS 26 中的通用磁盘映像，除非明确需要稀疏包以与其他文件系统兼容，否则 ASIF 应该是首选。作者预计 DropDMG 等第三方软件将很快支持 ASIF。

---

## 2. 小票打印机治好了我的拖延症

**原文标题**: A receipt printer cured my procrastination

**原文链接**: [https://www.laurieherault.com/articles/a-thermal-receipt-printer-cured-my-procrastination](https://www.laurieherault.com/articles/a-thermal-receipt-printer-cured-my-procrastination)

本文详细描述了作者克服拖延症的历程，并从电子游戏的成瘾性中汲取灵感。在多年与工作效率作斗争并怀疑自己患有注意力缺陷多动症后，作者意识到游戏之所以吸引人，是因为其频繁且有奖励性的反馈循环。这些循环由动作（例如在第一人称射击游戏中瞄准和射击）组成，随后是立即且强烈的视觉和听觉反馈，释放多巴胺并创造心流状态。

为了将此应用于现实生活中的任务，作者设计了一种使用便利贴的系统。任务被分解成小的、易于管理的步骤（每个步骤2-5分钟），写在单独的便利贴上。完成后，便利贴被揉成一团扔进一个透明的罐子里，提供有形的反馈和进度的可视化表示。

作者强调了以简单的、常规的任务开始一天的重要性，以建立动力，并在前一天晚上准备好任务。灵活性是关键，该系统可以在拖延症悄悄袭来时重新引入。

便利贴系统被证明是有效的，但耗时。为了简化流程，作者集成了一台热敏收据打印机来快速打印日常任务。这消除了书写单个便笺的摩擦并提高了连贯性。

最后，作者创建了自定义软件，该软件水平显示任务和子任务，从而可以轻松分解和打印特定列。此应用程序与收据打印机和透明罐子反馈系统相结合，已大大提高了作者的工作效率并消除了无效率的日子。作者计划公开发布该软件，并鼓励读者尝试所描述的方法。

---

## 3. 使用SMT解决LinkedIn皇后难题

**原文标题**: Solving LinkedIn Queens with SMT

**原文链接**: [https://buttondown.com/hillelwayne/archive/solving-linkedin-queens-with-smt/](https://buttondown.com/hillelwayne/archive/solving-linkedin-queens-with-smt/)

本文探讨了使用可满足性模理论（SMT）求解器，特别是Z3，来解决“LinkedIn皇后”难题，以此作为比SAT求解器更直观的替代方案。“LinkedIn皇后”难题涉及将N个皇后放置在NxN的网格上，网格被划分为N个区域，确保每行、每列和每个区域各有一个皇后，且皇后之间不能对角相邻。

作者认为，SMT求解器可以处理布尔值以外的更丰富的数据类型，因此与SAT相比，简化了问题编码。他们通过展示一个使用Z3解决该难题的Python实现来证明这一点。他们没有像SAT方法那样使用N²个布尔值，而是使用N个整数来表示皇后的位置，从而固有地强制执行“每行一个皇后”的约束。还添加了额外的约束，以确保不同的列和非相邻的对角线。

主要的挑战在于编码区域约束（“每个区域一个皇后”）。作者遍历区域位置，为每个区域创建一个OR表达式，以指示皇后的存在。

虽然作者承认原始SAT求解器可能更快，但他们得出结论，使用SMT编码和解决问题的简易性是一个显着的优势，解释了其在实践中优于SAT的原因。文章还强调了在开发过程中进行健全性检查以尽早发现编码错误的重要性。最后，它链接到作者的Z3代码和Ryan Berger的SAT解决方案以进行比较。

---

## 4. 在QEMU中模拟iPhone 11

**原文标题**: iPhone 11 emulation done in QEMU

**原文链接**: [https://github.com/ChefKissInc/QEMUAppleSilicon](https://github.com/ChefKissInc/QEMUAppleSilicon)

本文档是QEMU的README，QEMU是一款通用的开源机器模拟器和虚拟化器。QEMU可以在软件中模拟完整的机器，或者利用Xen和KVM等虚拟机监控器实现接近原生的CPU性能。它还提供用户空间API虚拟化，允许为一种架构编译的二进制文件在另一种架构上运行。

QEMU专为各种用例而设计，从直接用户控制到与oVirt和OpenStack等管理层集成。文档可在线获取，并从源代码中的`docs/`文件夹生成。

构建QEMU涉及在各种平台（Linux、macOS、Windows）上使用`configure`和`make`的简单步骤。可以通过'git format-patch'或'git send-email'将补丁提交到qemu-devel邮件列表，需要作者提供'Signed-off-by'行。建议使用'git-publish'实用程序进行常规贡献。

错误报告应通过GitLab issues提交，特别是对于从QEMU git或上游源代码构建的代码。供应商特定的错误应首先报告给相应的供应商。版本历史记录和发行说明可在Changelog或git历史记录中找到。

可以通过qemu-devel邮件列表或irc.oftc.net上的#qemu IRC频道联系QEMU社区。

---

## 5. 为什么我抓取的CD音轨名称是乱码？以及为什么会少了一首音轨？

**原文标题**: Why Does My Ripped CD Have Messed Up Track Names? and Why Is One Track Missing?

**原文链接**: [https://www.akpain.net/blog/inside-a-cd/](https://www.akpain.net/blog/inside-a-cd/)

本文解释了为什么抓取的CD可能出现不正确的音轨名称和缺失音轨的情况，重点介绍了MusicBrainz等元数据数据库的关键作用。作者遇到了抓取Finish Ticket乐队的《Echo Afternoon》时出现的问题：音轨名称拼写错误、一个音轨与后面的音轨合并以及一个音轨缺失。

作者详细介绍了CD抓取软件如何使用CD的目录表(TOC)，即描述音轨开始和结束的一系列数字，在MusicBrainz上查找发行信息。该数据库提供音轨名称等元数据，然后将其应用于抓取的文件。

作者抓取的问题源于MusicBrainz数据库中的不准确之处。一个音轨名称只是拼写错误（“Rainclous”而不是“Raincloud”）。更重要的是，两首音轨（“Nothing Coming Soon”和“Don't Need a Reason”）在CD本身上被合并成一首，这一事实使最初将数据输入到MusicBrainz的人感到困惑。这导致仅记录了11首音轨，其中较长的音轨（“Don't Need a Reason”）更早开始，以弥补缺失的长度。本应在“Don't Need a Reason”之后出现的实际音轨完全从MusicBrainz条目中遗漏了。

由于MusicBrainz是一个社区编辑的数据库，作者更正了不准确的元数据，将合并音轨的标题（“Nothing Coming Soon / Don't Need a Reason”）合并到数据库中，并在过渡期间手动更新了自己的文件。作者的更改将由社区审查，然后才能在MusicBrainz中永久实施。

---

## 6. 通过高频日内交易实现电池储能利润最大化

**原文标题**: Maximizing Battery Storage Profits via High-Frequency Intraday Trading

**原文链接**: [https://arxiv.org/abs/2504.06932](https://arxiv.org/abs/2504.06932)

本文题为“通过高频日内交易最大化电池储能利润”，探讨了电网级电池储能系统参与连续日内电力市场时最大化收益的策略。作者Schaurecker等人介绍并评估了一种自动高频交易策略，该策略考虑了限价订单簿的动态、市场规则和电池技术参数。

该策略的核心在于将标准滚动内在策略应用于日内电力市场。为了使其在计算上可行，他们使用动态规划近似来解决它，该方法在速度上明显优于精确的混合整数线性规划解决方案。

使用德国订单簿数据进行的一年期回溯测试表明，动态规划近似不会损害交易利润，并使该策略能够对每个相关的订单簿更新做出反应，从而实现真实的快速回溯测试。

结果突出了高频交易的巨大收入潜力。所提出的策略优于每小时重新优化58%，优于分钟级重新优化14%，强调了交易速度的重要性。此外，作者利用算法的速度来训练滚动内在策略的参数化扩展，在样本外实现了每年额外8.4%的收入增长。本文得出结论，高频交易对于最大化日内电力市场利润至关重要，并且开发的动态规划方法提供了一种可行且有效的解决方案。

---

## 7. Roame (YC S23) 正在招聘

**原文标题**: Roame (YC S23) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/roame/jobs/9QhTM31-founding-product-ai-engineer](https://www.ycombinator.com/companies/roame/jobs/9QhTM31-founding-product-ai-engineer)

Roame (YC S23) 招聘创始产品人工智能工程师 (旧金山)。全职现场办公，年薪 $15万 - $21.5万，股权 0.50% - 1.25%，提供完善福利和签证担保。

公司致力于帮助超过 100 万旅客最大化利用积分和里程，让旅行变得完美。Roame 获得 Y Combinator、Goodwater、Accel 和天使投资人支持，现寻求一位充满热情的工程师，负责前端（Vercel 上的 Next.js），并参与后端（Firebase, Go）开发，同时整合人工智能管道。

理想人选需具备 4 年以上工程经验，包括拥有大量用户的个人项目，对旅行和积分/里程有浓厚兴趣，精通 NextJS、Firebase 和 Go，并具有良好的设计感。必须适应快速迭代和持续学习。

Roame 重视强大的职业道德、主人翁精神、责任感、友善以及敢于争论并信守承诺的能力。面试流程包括电话筛选、家庭作业和文化面试。福利包括健康保险、带匹配的 401(k) 计划、通勤福利、免费午餐和公司团建。Roame 坚信强大的职业道德是竞争优势，并提倡行动和客户满意度。

---

## 8. 美国支持的以色列公司间谍软件被用于攻击欧洲记者

**原文标题**: US-backed Israeli company's spyware used to target European journalists

**原文链接**: [https://apnews.com/article/spyware-italy-paragon-meloni-pegasus-f36dd32106f44398ee24001317ccf2bb](https://apnews.com/article/spyware-italy-paragon-meloni-pegasus-f36dd32106f44398ee24001317ccf2bb)

美联社报道称，一家由美国投资者支持的以色列间谍软件公司Paragon Solutions将其监控工具“地狱火”(Inferno)出售给了一些政府，据称这些政府利用该工具针对欧洲的记者，特别是意大利的记者。“地狱火”与臭名昭著的飞马间谍软件类似，可以从目标手机中提取数据，包括消息、联系人和位置信息。

文章详细描述了意大利记者如何因调查令总理乔治亚·梅洛尼政府难堪的事件而成为“地狱火”的目标。 至少有六名记者似乎受到了监控，间谍软件在他们不知情或未经同意的情况下被安装。 虽然意大利政府尚未直接确认使用Paragon的间谍软件，但当局承认意大利已经购买了该软件。

这些披露引发了人们对滥用监控技术的担忧，特别是在监督和保障措施薄弱的国家。 这也突显了美国投资在生产强大间谍软件的公司中所扮演的角色，引发了对伦理考量以及潜在参与侵犯人权行为的质疑。 成为攻击目标的记者们认为，使用这种技术是对新闻自由和民主的威胁。 该报告强调了间谍软件滥用的持续问题，以及加强监管和监督以保护记者和公民社会的必要性。

---

## 9. Digital Research公司的CP/M 2.2、CP/M 3.0、CP/M-86、Concurrent CP/M-86列表

**原文标题**: CP/M 2.2, CP/M 3.0, CP/M-86, Concurrent CP/M-86 listings by Digital Research

**原文链接**: [http://www.bitsavers.org/pdf/digitalResearch/CPM_Listings/](http://www.bitsavers.org/pdf/digitalResearch/CPM_Listings/)

这是bitsavers.org网站上包含由Digital Research开发的各种CP/M操作系统的代码列表的目录列表。列出的CP/M版本包括：

*   **CP/M 2.2:** 最初且广为成功的8位CP/M操作系统。
*   **CP/M Plus V3.0:** CP/M的增强版本，也是8位。
*   **CP/M-86 V1.1:** CP/M的16位版本，旨在用于基于Intel 8086的系统。
*   **Concurrent CP/M-86 V2.0:** CP/M-86的多任务版本。

这些目录可能包含这些操作系统的源代码或汇编列表，对历史研究、理解操作系统设计或移植工作具有潜在价值。服务器在Debian系统上运行Apache 2.4.59版本。列出的日期可能不正确，可能只是占位符。

---

## 10. Helion：一款用C#编写的现代快节奏毁灭战士风格FPS引擎

**原文标题**: Helion: A modern fast paced Doom FPS engine in C#

**原文链接**: [https://github.com/Helion-Engine/Helion](https://github.com/Helion-Engine/Helion)

Helion：一款高性能现代Doom引擎，用C#编写，旨在克服在现代硬件上运行复杂Doom地图时遇到的性能限制。它采用静态渲染方法和状态管理来处理动态地图变化，将处理任务转移到GPU而不是依赖于CPU密集型的BSP树渲染。这带来了显著的性能提升，使得即使在较旧的硬件上也能流畅运行复杂的地图。

Helion支持多种WAD格式，包括vanilla Doom、Boom、MBF、MBF21、UDMF（部分）和ID24。它最低需要Windows 7和兼容OpenGL 3.3的GPU。

用户可以下载Windows和Linux的稳定版本，或者选择每晚的实验性构建版本。该引擎使用.NET 9，包含在自包含版本中；否则，用户需要安装.NET Desktop Runtime（Windows）或遵循特定于发行版的说明（Linux），包括确保安装了OpenAL、libsndfile和libmpg123。

文章包含展示引擎运行各种地图的截图以及证明其性能的基准测试。提供设置和游戏玩法文档，并为想要从源代码编译的用户提供构建说明。

社区可以通过Discord服务器和Doomworld论坛主题参与该项目。错误报告可以在GitHub Issues或Doomworld主题中提交。

---

## 11. Rust 编译器性能

**原文标题**: Rust compiler performance

**原文链接**: [https://kobzol.github.io/rust/rustc/2025/06/09/why-doesnt-rust-care-more-about-compiler-performance.html](https://kobzol.github.io/rust/rustc/2025/06/09/why-doesnt-rust-care-more-about-compiler-performance.html)

本文探讨了关于 Rust 编译速度慢的常见抱怨。作者作为 Rust 编译器性能工作组的成员，承认了这个问题，并向读者保证 Rust 项目正在积极致力于提高编译器性能。文章提供了证据，包括一个基准测试，显示了过去几年里显著的加速。

尽管取得了进展，作者也认识到编译速度对于许多用户来说仍然是一个瓶颈。文章探讨了实现近乎即时重建的可行性，表明通过牺牲运行时性能，增量构建是有可能实现的。文章提到了几种潜在的加速编译方法，包括并行前端、替代代码生成后端和更智能的增量编译。

作者随后深入探讨了改进速度不够快的原因。技术原因包括编译器庞大而复杂的代码库、技术债务以及需要权衡编译速度与其他因素（如硬件支持和内存使用）之间的关系。优先级安排也发挥着作用，因为 Rust 项目在编译器性能与稳定性、向后兼容性和安全性等其他目标之间进行平衡。对大型（编译器）代码库进行重大更改是困难的，并且需要大量的时间和精力。

---

## 12. 研究人员证实两名记者遭Paragon间谍软件入侵

**原文标题**: Researchers confirm two journalists were hacked with Paragon spyware

**原文链接**: [https://techcrunch.com/2025/06/12/researchers-confirm-two-journalists-were-hacked-with-paragon-spyware/](https://techcrunch.com/2025/06/12/researchers-confirm-two-journalists-were-hacked-with-paragon-spyware/)

公民实验室的一份新报告证实，两名欧洲记者，Ciro Pellegrino和一位未具名人士，遭到了以色列公司Paragon开发的Graphite间谍软件的入侵。这一发现加深了一起可能涉及意大利政府的间谍软件丑闻，因为这两名记者都是被同一Paragon客户所针对。

这一确认使意大利议会情报监督委员会COPASIR最近的一份报告受到质疑。COPASIR的报告曾声明Fanpage的Francesco Cancellato（Pellegrino的同事）未受到监视，并且没有提及Pellegrino，尽管两人都收到了WhatsApp关于被攻击的通知。公民实验室认为意大利政府可以就Paragon间谍软件的使用情况提供明确的答案，尤其是在Pellegrino的案件中。

零点击的Graphite间谍软件利用了iMessage的漏洞，使攻击者无需任何用户交互即可访问记者的手机。 据报道，该问题已在2025年2月的iOS更新中得到缓解。

除了这两名记者外，公民实验室此前证实，为一家移民救援非政府组织工作的Luca Casarini和Beppe Caccia也曾受到Paragon间谍软件的攻击。

虽然调查仍在进行中，但该事件引发了人们对政府监视记者和人权活动家的担忧。Paragon对此回应称，它曾主动提出帮助意大利政府调查Cancellato的黑客行为，但遭到拒绝，导致他们切断了与意大利的联系。

---

## 13. Seedance 1.0
舞籽 1.0

**原文标题**: Seedance 1.0

**原文链接**: [https://seed.bytedance.com/en/seedance](https://seed.bytedance.com/en/seedance)

Seedance 1.0 是一种新型模型，能够根据文本 (T2V) 和图像 (I2V) 输入生成高质量、多镜头的视频。它在语义理解和提示词遵循方面有所进步，能够创作出具有流畅运动、丰富细节和电影视觉效果的 1080p 视频。

该模型已使用多维度评估框架 SeedVideoBench-1.0 进行了评估。与其他行业模型相比，Seedance 1.0 在 T2V 和 I2V 任务的提示词一致性、运动质量和美学方面表现出强大的性能，如雷达图所示。

根据 Artificial Analysis 的排行榜（截至 2025 年 6 月 9 日），Seedance 1.0 在 T2V 和 I2V 类别中均取得了很高的排名。由于 Kling 2.1 的公开数据不可用，因此与 Kling 2.1 的比较使用了 Kling 2.0 的数据。

---

## 14. 谷歌Pixel不再是AOSP参考设备

**原文标题**: Google Pixels are no longer the AOSP reference device

**原文链接**: [https://9to5google.com/2025/06/12/android-open-source-project-pixel-change/](https://9to5google.com/2025/06/12/android-open-source-project-pixel-change/)

谷歌决定不在Android 16 AOSP发布时同步提供Pixel硬件仓库和设备树，引发了定制ROM社区对AOSP未来发展的担忧。 缺乏这些Pixel特定资源使得定制ROM开发者更难为其操作系统创建更新，并且可能影响安全研究人员。

有传言称谷歌可能要停止AOSP，但谷歌副总裁Seang Chau驳斥了这一说法，表示AOSP不会消失，公司仍然致力于AOSP更新。

然而，Android团队的回应表明Pixel设备树将不再提供。相反，AOSP的目标是为开发者提供一个与硬件无关的“参考目标”，可能侧重于Cuttlefish和GSI目标等现有解决方案。 这些旨在成为灵活、可配置且经济实惠的测试和开发替代方案。

虽然谷歌重申了对AOSP的承诺，但这一变化意味着定制ROM开发者在工作中将面临更大的挑战，因为他们将无法直接访问将AOSP适配到谷歌硬件所需的Pixel特定代码。

---

## 15. 量子计算讲义 (2022)

**原文标题**: Quantum Computation Lecture Notes (2022)

**原文链接**: [https://math.mit.edu/~shor/435-LN/](https://math.mit.edu/~shor/435-LN/)

这些是彼得·秀尔2022年秋季量子计算课程（8.370/18.435）的讲义。讲义涵盖了量子计算领域的广泛主题，从基本原理入手，逐步深入到高级算法和纠错技术。

早期的讲座介绍了诸如叠加态、幺正演化（布洛赫球）、量子测量以及用于描述联合量子系统的张量积等核心概念。在此基础上，讲义深入探讨了经典和可逆布尔电路，然后探索了量子门及其应用，包括量子隐形传态。

该课程随后涉及密度矩阵、GHZ实验（理论和使用量子光学的实验方面），并探索了关键量子算法，如Deutsch-Jozsa算法和Simon算法。很大一部分内容专门讨论秀尔分解算法，包括必要的数论和相关的离散对数算法。Grover搜索算法及其最优性也被涵盖。

最后，讲义进入量子纠错领域，讨论了诸如9-量子比特码、7-量子比特量子汉明码和量子CSS码等代码。该系列以BB84量子密钥分发协议及其安全性证明结束。虽然第26讲（哈密顿模拟）的笔记不完整，但其余主题提供了该领域的实质性概述。

---

## 16. 将 Microsoft Office 从 Source Depot 迁移到 Git

**原文标题**: Microsoft Office migration from Source Depot to Git

**原文链接**: [https://danielsada.tech/blog/carreer-part-7-how-office-moved-to-git-and-i-loved-devex/](https://danielsada.tech/blog/carreer-part-7-how-office-moved-to-git-and-i-loved-devex/)

将 Microsoft Office 从 Source Depot 迁移到 Git 的复杂过程：Source Depot 是一种传统的版本控制系统，虽然可靠，但速度慢且繁琐，阻碍了开发人员的生产力。此次迁移的驱动力是现代化和改善开发人员体验的需求。

这是一个历时多年的项目，面临着来自 Office 复杂的发布计划、Office 开发团队的庞大规模（约 4,000 名工程师）以及 Source Depot 深入集成到现有构建和发布管道中的挑战。与 GitHub 合作开发用于 Git 的虚拟文件系统 (VFS for Git) 以处理庞大的 Office 存储库是关键的推动因素。

迁移策略围绕着一个“平行宇宙”——一个与 Source Depot 不断同步的 Git 原生镜像。这允许通过针对两个代码库运行整个测试套件来证明等效性。过度沟通至关重要，采用中心辐射模式，利用每个团队的“倡导者”来传播信息和收集反馈。全面的培训，侧重于实际场景和相关内容，对于采用也至关重要。实施了“红色按钮”回滚策略以应对潜在的故障。

结果是积极的，开发人员的生产力得到了提高，入职速度加快，并且对 Git 的偏好更加强烈。主要经验教训包括沟通的重要性、构建并行系统进行等效性测试、赋予倡导者权力以及规划回滚。作者强调，在大型迁移过程中，人员挑战比技术障碍更重要。

---

## 17. 喋喋不休TTS

**原文标题**: Chatterbox TTS

**原文链接**: [https://github.com/resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox)

Chatterbox TTS：Resemble AI全新开源、生产级文本转语音（TTS）模型，采用MIT许可。在并排偏好测试中，其表现可与ElevenLabs等领先的闭源系统相媲美。Chatterbox旨在为包括表情包、视频、游戏和AI代理在内的各种应用创建逼真的声音。一个独特的功能是情感夸张控制，允许生成富有表现力的语音。

该模型基于0.5B Llama骨干网络构建，并使用0.5M小时的清洗数据进行训练。主要功能包括零样本TTS能力、用于稳定性的对齐信息推理以及语音转换脚本。它集成了Resemble AI的PerTh水印技术，实现负责任的AI，将不易察觉的水印嵌入到生成的音频中，用于识别和追踪。

用户可以通过pip或从源代码（使用Python 3.11）安装Chatterbox。文档提供了通用使用和表达性语音生成的技巧，建议调整`exaggeration`和`cfg_weight`参数以获得最佳效果。目前仅支持英语。

对于需要更高准确性或可扩展性的用户，Resemble AI提供具有超低延迟且价格具有竞争力的TTS服务。该项目鼓励通过其Discord服务器进行社区贡献，并包含免责声明，禁止将该模型用于恶意目的。

---

## 18. 舞动脑波：声音如何实时重塑你的大脑网络

**原文标题**: Dancing brainwaves: How sound reshapes your brain networks in real time

**原文链接**: [https://www.sciencedaily.com/releases/2025/06/250602155001.htm](https://www.sciencedaily.com/releases/2025/06/250602155001.htm)

丹麦奥胡斯大学2025年6月2日发表于《科学日报》的一篇文章讨论了一项新研究，该研究揭示了声音如何实时动态地重塑大脑网络。来自奥胡斯大学和牛津大学的研究人员开发了一种名为FREQ-NESS（通过源分离进行频率分辨网络估计）的新型神经影像方法，以追踪不同声音频率如何在大脑区域传播。

FREQ-NESS利用先进的算法，根据其主要频率解开重叠的大脑网络，使研究人员能够以高精度绘制整个大脑的内部组织图。 这种数据驱动的方法不同于依赖于预定义频段或区域的传统方法。

该研究发现，大脑不仅仅是记录声音，还会积极地重塑自身以响应声音，协调复杂的大脑电波相互作用。这为基础神经科学、脑机接口和临床诊断开辟了新的可能性。

研究人员认为，这一发现可能会彻底改变我们对音乐认知、一般感知、注意力和意识改变状态的理解。由于FREQ-NESS在不同条件下具有很高的可靠性，它也可能为个性化大脑绘图铺平道路。目前正在进行一项大规模的研究计划，以进一步开发该方法。

---

## 19. 对o3 Pro的初步印象

**原文标题**: First thoughts on o3 pro

**原文链接**: [https://www.latent.space/p/o3-pro](https://www.latent.space/p/o3-pro)

本·海拉克对OpenAI的新o3-pro模型进行了初步评测。他指出，o3-pro在获得大量上下文信息后，能够生成更具体、更可执行的计划，能力有所提升。OpenAI还大幅降低了o3的价格，与GPT 4.1定价持平，这可能暗示了“-pro”版本的多数投票系统。

海拉克强调，o3-pro的优势在于其与现实世界工具和数据集成能力。它更擅长理解其环境、沟通其工具访问权限以及为给定任务选择正确的工具。他将这比作一个高智商的人需要学习融入现实世界环境。

然而，如果上下文信息不足，o3-pro可能会过度思考任务，并且可能不适合需要直接行动而无需分析的任务。海拉克认为o3-pro与Claude Opus和Gemini 2.5 Pro等模型相比，有显著不同且更为出色，感觉它在不同的性能水平上运行。他认为OpenAI正专注于强化学习，以教导模型不仅 *如何* 使用工具，还 *何时* 使用工具。

他重申，提供上下文和明确的系统提示对于最大限度地发挥o3-pro的能力至关重要。模型、工具、记忆和适当的“利用”相结合是产生有用的AI产品的关键。

---

## 20. 特朗普削减NASA预算将摧毁数十年的科研成果并扼杀其未来。

**原文标题**: Trump's NASA cuts would destroy decades of science and wipe out its future

**原文链接**: [https://www.latimes.com/business/story/2025-06-09/trumps-nasa-cuts-would-destroy-decades-of-science-and-wipe-out-its-future](https://www.latimes.com/business/story/2025-06-09/trumps-nasa-cuts-would-destroy-decades-of-science-and-wipe-out-its-future)

在2025年6月9日《洛杉矶时报》的一篇未来报道中，迈克尔·希尔齐克报道了一项拟议的特朗普政府预算计划，该计划将大幅削减NASA的科学项目近50%，整体支出削减24%。该文章描绘了该机构黯淡的未来，认为这些削减将摧毁数十年的科学进步。

据称，该预算是在没有NASA参与的情况下制定的，优先考虑了“实用”应用，例如气象卫星，同时削减了气候变化研究、地球科学和天体物理学的资金。包括“火星奥德赛”号和“火星大气与挥发演化探测器”任务在内的现有项目面临取消，尽管它们在提供未来任务（包括政府自身通过阿尔忒弥斯计划重返月球和登陆火星的目标）所需的重要数据方面发挥着关键作用。

希尔齐克强调了NASA领导层真空带来的混乱局面，这源于贾里德·艾萨克曼担任局长的提名突然撤回，以及与埃隆·马斯克的SpaceX公司关系紧张。他认为，这些削减破坏了对于长期太空探索至关重要的国际合作，并将摧毁下一代科学家。他将拟议的削减归因于拉塞尔·沃特的影响，并引用了沃特过去针对“被误导的”气候变化项目提出类似预算削减的建议。

文章以一种绝望的心情结束，暗示这些削减可能会引发NASA的生存危机，使中国在太空探索方面超越美国。终止正在进行的任务被描述为浪费已经投入的纳税人资金，以及对宇宙的“隐喻式的闭眼”。

---

## 21. 密歇根州上半岛密集土著农业的考古证据

**原文标题**: Archaeological evidence of intensive indigenous farming in MI's Upper Peninsula

**原文链接**: [https://www.science.org/doi/10.1126/science.ads1643](https://www.science.org/doi/10.1126/science.ads1643)

无法访问文章链接。

---

## 22. Y Combinator孵化的Sorcerer公司融资390万美元，用于发射更多气象气球

**原文标题**: Y Combinator startup Sorcerer raises $3.9M to launch more weather balloons

**原文链接**: [https://www.axios.com/pro/climate-deals/2025/06/12/sorcerer-seed-weather-balloons](https://www.axios.com/pro/climate-deals/2025/06/12/sorcerer-seed-weather-balloons)

无法访问文章链接。

---

## 23. Show HN: Spark，Three.js 的高级 3D 高斯溅射渲染器

**原文标题**: Show HN: Spark, An advanced 3D Gaussian Splatting renderer for Three.js

**原文链接**: [https://sparkjs.dev/](https://sparkjs.dev/)

Spark：用于Three.js的高级3D高斯溅射渲染器

*   **Three.js 集成：** 允许将高斯溅射与 Three.js 场景中的现有网格和其他元素无缝集成。
*   **性能：** 强调在各种设备上的快速渲染速度。
*   **动态溅射效果：** 提供可编程的动态效果，能够对溅射进行创造性的操作。
*   **格式支持：** 支持多种高斯溅射数据格式，包括 PLY、SPZ、SPLAT 和 KSPLAT，从而提高数据导入和使用的灵活性。

本质上，Spark 旨在通过提供高性能且通用的高斯溅射渲染器，并具有广泛的格式兼容性和动态效果功能，来增强 Three.js 中的 3D 场景创建。

---

## 24. 在巴黎寻找居里夫人的放射性指纹

**原文标题**: The hunt for Marie Curie's radioactive fingerprints in Paris

**原文链接**: [https://www.bbc.com/future/article/20250605-the-hunt-for-marie-curies-radioactive-fingerprints-in-paris](https://www.bbc.com/future/article/20250605-the-hunt-for-marie-curies-radioactive-fingerprints-in-paris)

索菲·哈达克追溯玛丽·居里巴黎实验室和档案馆留下的放射性指纹，探索居里夫人的遗产。居里夫人开创性的放射性材料研究一个多世纪后，在她接触过的表面，包括门把手、椅子和笔记本上，仍然可以检测到镭的痕迹。

居里博物馆承认存在低水平放射性，但认为这些痕迹是其遗产的重要组成部分。博物馆已采取措施对实验室进行净化，但微弱的痕迹仍然嵌入在材料中。像马克·阿梅里奇这样的专家对数千件物品进行了广泛的测试，在保护与公共安全之间取得平衡。构成重大风险的物品已被销毁。

文章强调了居里夫人进行研究的挑战性和常常危险的条件，尤其是在早期“棚屋年代”，她和丈夫皮埃尔发现了钋和镭。这些早期的笔记为了解居里夫人与皮埃尔之间紧张而协作的研究提供了见解。

目前的测量结果虽然是低水平的，但提供了与居里夫人开创性工作和放射性历史的切实联系，反映了她开创性的发现以及当时人们对辐射暴露危险的了解不足。如今，严格的安全协议管理着放射性材料的处理，这与居里夫人亲力亲为的方式形成了鲜明对比。

---

## 25. 研究表明，宇宙大爆炸可能发生于黑洞内部。

**原文标题**: Research suggests Big Bang may have taken place inside a black hole

**原文链接**: [https://www.port.ac.uk/news-events-and-blogs/blogs/space-cosmology-and-the-universe/what-if-the-big-bang-wasnt-the-beginning-our-research-suggests-it-may-have-taken-place-inside-a-black-hole](https://www.port.ac.uk/news-events-and-blogs/blogs/space-cosmology-and-the-universe/what-if-the-big-bang-wasnt-the-beginning-our-research-suggests-it-may-have-taken-place-inside-a-black-hole)

朴茨茅斯大学的文章探讨了一个引人深思的假设：标志着我们宇宙开端的宇宙大爆炸可能发生在一个黑洞内部。 这一观点挑战了将宇宙大爆炸视为绝对开端的传统观念。

研究人员提出，传统上被视为宇宙死胡同的黑洞，实际上可能是通往新宇宙的门户。 他们的工作重点是修改爱因斯坦的广义相对论，以解释黑洞内部的极端条件。 坠入黑洞的物质，不再是坍缩成奇点（一个无限密度的点），而是有可能通过一个“宇宙反弹”并作为一个新的、膨胀的宇宙出现。

这个“黑洞宇宙学”模型解决了标准大爆炸理论的一些问题，例如奇点问题和对暴胀的需求。 该文章强调了修改后的理论如何消除奇点，从而允许从黑洞内部到新宇宙的连续过渡。

研究团队还探讨了该模型如何解释我们宇宙的观测特性。 他们正在研究我们宇宙的初始条件是否受到其从中产生的黑洞的性质的影响。 具体来说，他们正在研究对基本常数和宇宙整体结构的影响。 虽然这个概念仍然是高度理论性的，但它为我们宇宙的起源提供了一个令人着迷的替代视角。

---

## 26. 印度航空飞往伦敦的航班在艾哈迈达巴德坠毁，机上载有240余人

**原文标题**: Air India flight to London crashes in Ahmedabad with more than 240 onboard

**原文链接**: [https://www.theguardian.com/world/live/2025/jun/12/air-india-flight-ai171-plane-crash-ahmedabad-india-latest-updates](https://www.theguardian.com/world/live/2025/jun/12/air-india-flight-ai171-plane-crash-ahmedabad-india-latest-updates)

印度航空一架飞往伦敦的航班在印度艾哈迈达巴德坠毁，机上载有240多名乘客。最初的报告显示无人生还，但艾哈迈达巴德警方后来确认至少有一名幸存者：居住在伦敦的40岁英印男子维斯瓦什·库马尔·拉梅什。拉梅什当时与他的兄弟（也在飞机上）一起回艾哈迈达巴德探亲，他向《印度斯坦时报》讲述了这次可怕的经历。他说起飞后不久就听到一声巨响，飞机随后坠毁。

拉梅什受到了撞击伤，包括瘀伤，但他仍然保持清醒和理智。他描述说，醒来时发现自己被尸体和飞机残骸包围，然后逃离残骸，之后被送往医院。在接受《印度斯坦时报》采访时，他仍然持有他的登机牌。在拉梅什作为幸存者出现之前，艾哈迈达巴德警察局长吉南德拉·辛格·马利克曾告诉美联社，似乎没有幸存者。

---

## 27. Show HN: Eyesite – 计算机视觉与网页设计结合的实验性网站

**原文标题**: Show HN: Eyesite – Experimental website combining computer vision and web design

**原文链接**: [https://blog.andykhau.com/blog/eyesite](https://blog.andykhau.com/blog/eyesite)

“Show HN”：Eyesite - 利用眼动追踪模拟 Apple Vision Pro 体验

这个“Show HN”帖子详细介绍了“Eyesite”的创建过程，这是一个实验性网站，旨在通过使用眼动追踪进行导航和交互，来模拟 Apple Vision Pro 的体验。作者在无法获得真正的 Vision Pro 的情况下，使用了 WebGazer.js 库来实现眼动追踪。

核心功能包括校准眼动追踪器，通过让用户专注于指定点，将他们的视线映射到屏幕坐标。 然后，该网站将用户的视线解释为鼠标光标，并使用空格键作为“点击”操作。

挑战包括代表注视位置的、分散注意力和经常不准确的红点。 作者通过使眼睛光标和标准鼠标光标都不可见来解决这个问题，从而改善了直接眼睛控制的感觉。 用户反馈通过按钮高亮显示以及用户注视在它们上面时的“弹出”来提供。

为了弥补眼动追踪固有的抖动，用户界面元素被设计得很大，并且该网站仅限于更大的屏幕。 作者承认代码并不完美，但鼓励其他人探索和改进该项目，该项目可在 GitHub 上找到。 该项目展示了结合计算机视觉和网页设计来创建交互式用户体验的潜力。

---

## 28. V-JEPA 2：世界模型与物理推理新基准

**原文标题**: V-JEPA 2 world model and new benchmarks for physical reasoning

**原文链接**: [https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/](https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/)

无法访问文章链接。

---

## 29. 自主编码推荐

**原文标题**: Agentic Coding Recommendations

**原文链接**: [https://lucumr.pocoo.org/2025/6/12/agentic-coding/](https://lucumr.pocoo.org/2025/6/12/agentic-coding/)

Armin Ronacher 的文章探讨了代理式编程实践，重点在于利用像 Claude Code 这样的 AI 代理来完成开发任务。他建议使用更经济的 Sonnet 模型并高效地利用 tokens。成功的关键在于赋予代理充分的权限和最少的干扰来分配任务，并将 IDE 的角色转变为最终编辑。

他强调禁用权限检查（通过适当的 Docker 化），仅在必要时使用 MCP（机器通信协议），以及由于其上下文系统、测试缓存、简洁性、结构化接口和稳定的生态系统而倾向于使用 Go 来进行后端项目。前端开发则受益于 Tailwind、带有 Tanstack 的 query 和 router 的 React 以及 Vite。

有效的工具至关重要；任何可观察的东西都可以成为工具，但工具必须快速、用户友好且可调试。日志记录也至关重要，特别是对于像在调试模式下发送电子邮件这样的任务。

这篇文章强调了代理式编程的速度。新兴的、快速编译的工具可以提高生产力。稳定的生态系统（如 Go 和 Flask）和简单的代码明显优于复杂的代码。并行化、良好的代码维护和及时的重构也受到强调。

总体的目标是通过有效地集成代理来编写更好、更易于维护的代码。简单性、稳定性、可观察性和智能并行化是最大限度提高生产力收益的基本原则。

---

## 30. 以最愚蠢的方式绕过 GitHub Actions 策略

**原文标题**: Bypassing GitHub Actions policies in the dumbest way possible

**原文链接**: [https://blog.yossarian.net/2025/06/11/github-actions-policies-dumb-bypass](https://blog.yossarian.net/2025/06/11/github-actions-policies-dumb-bypass)

GitHub Actions 策略的简单绕过

这篇博文详细介绍了一种绕过 GitHub Actions 策略的简单方法。GitHub Actions 策略旨在限制在仓库、组织或企业内特定 action 和可复用工作流的使用，通过限制潜在的不受信任的代码执行来增强安全性。

作者演示了如何轻松规避此策略。核心问题在于 GitHub Actions 不仅允许通过 `owner/repo@tag` 引用 action，还允许通过 runner 文件系统上的相对路径引用。用户只需在工作流中 `git clone` 所需的 action 仓库到 runner 的环境中，然后使用 `uses: ./path/to/checkout` 引用它。这有效地绕过了策略限制，因为 action 不再直接从受控仓库中拉取。

作者提出了两种潜在的解决方案：要么在策略中明确禁止“本地”`uses:` 引用，要么至少清楚地记录此限制。作者认为，像这种绕过一样，无效的策略机制比没有策略更糟糕，因为它们会产生一种虚假的安全感，并鼓励破坏预期安全措施的变通方法。作者认为，如果不解决这个问题，组织可能会错误地认为他们拥有强大的安全边界，而实际上并不存在。

---

## 31. 伸缩架 [视频]

**原文标题**: Expanding Racks [video]

**原文链接**: [https://www.youtube.com/watch?v=iWknov3Xpts](https://www.youtube.com/watch?v=iWknov3Xpts)

提供的文本并非一篇文章，而似乎是 YouTube 网页页脚的一部分。标题表明是一个名为“Expanding Racks”的视频，但其后的内容是 YouTube 页面底部常见的标准样板信息。

内容包括以下链接：

*   **YouTube：** 可能是 YouTube 的主页。
*   **关于 (About)：** 关于 YouTube 本身的信息。
*   **新闻版权 (News Copyright)：** 关于 YouTube 上与新闻内容相关的版权信息。
*   **联系我们 (Contact Us)：** 联系 YouTube 支持或其他相关部门的链接。
*   **创作者 (Creators)：** 针对 YouTube 内容创作者的资源和信息。
*   **广告 (Advertising)：** 关于在 YouTube 上投放广告的信息。
*   **开发者 (Developers)：** 供使用 YouTube API 的开发者参考的信息。
*   **条款 (Terms)：** YouTube 的服务条款。
*   **隐私权政策与安全 (Privacy Policy and Security)：** 关于 YouTube 用户隐私和安全措施的信息。
*   **YouTube 的运作方式 (How YouTube Works)：** 对 YouTube 算法和推荐系统的解释。
*   **测试新功能 (Testing New Features)：** 关于 YouTube 实验性功能的信息。
*   **NFL Sunday Ticket：** 关于 YouTube 提供的 NFL Sunday Ticket 套餐的信息。
*   **Copyright Notice：** 指示 Google LLC 于 2025 年拥有的版权声明。

本质上，这个片段是标准的 YouTube 法律和信息页脚文本，提供指向该平台各个重要部分的链接。标题“Expanding Racks [video]”可能是在 YouTube 上托管的特定视频的标题，但随附文本并未描述该视频的内容。

---

## 32. 罗德与施瓦茨 AMIQ 调制信号发生器拆解

**原文标题**: Rohde and Schwarz AMIQ Modulation Generator Teardown

**原文链接**: [https://tomverbeure.github.io/2025/04/26/RS-AMIQ-Teardown-Analog-Deep-Dive.html](https://tomverbeure.github.io/2025/04/26/RS-AMIQ-Teardown-Analog-Deep-Dive.html)

罗德与施瓦茨 AMIQ I/Q 调制信号发生器拆解与分析。作者购入一台二手 AMIQ，并探索其功能和内部结构。

AMIQ 本质上是一个具有深度采样缓冲区的双通道任意波形发生器，输出用于基带调制的 I/Q 信号，通常与罗德与施瓦茨 SMIQ 等射频矢量信号发生器一起使用。波形数据通过 R&S WinIQSim 等软件从外部提供，该软件支持各种通信协议。

拆解显示，它包含一个用于控制的标准 PC 系统和一个专用的信号生成 PCB。该 PCB 经过精心设计，具有对称的 I/Q 通道，以实现高精度。本文重点介绍模拟信号生成方面，着重介绍了固定与可变 DAC 时钟架构（AMIQ 使用可变架构）。

一个关键要素是内部参考时钟生成，它使用温控晶体振荡器 (TCXO) 锁相到内部或外部参考时钟，以实现最佳的相位噪声性能。DAC 时钟合成器通过 PLL 生成可编程的 DAC 时钟，使用 Mini-Circuits VCO 和 Analog Devices AD9850 DDS 合成器来实现精确的频率控制。AD9850 有趣的数模模数转换过程与低通滤波器一起使用，可最大限度地减少频率杂散。最后，本文提到了精细的 I/Q 输出倾斜调整功能，并提供了详细的原理图和信号路径测试点。

---

## 33. Show HN: RomM – 一款开源、自托管的 ROM 管理器和播放器

**原文标题**: Show HN: RomM – An open-source, self-hosted ROM manager and player

**原文链接**: [https://github.com/rommapp/romm](https://github.com/rommapp/romm)

RomM 是一款开源、自托管的 ROM 管理器，旨在帮助用户组织、增强和畅玩他们的复古游戏收藏。它拥有一个干净、响应式的界面，可在桌面和移动设备上访问。主要功能包括扫描并使用来自 IGDB、Screenscraper 和 MobyGames 等来源的元数据来丰富游戏库，以及从 SteamGridDB 获取自定义艺术作品。RomM 还支持 RetroAchievements 和 400 多个平台的元数据。

一个重要的亮点是能够使用 EmulatorJS 和 RuffleRS 直接在浏览器中玩游戏。用户可以与朋友分享他们的游戏库，并授予有限的访问权限。该平台还支持多磁盘游戏、DLC、模组、修改、补丁和手册。

该项目对 Playnite 和 muOS 提供官方应用程序支持，并包括按文件名中的标签解析和过滤游戏的功能。用户可以通过任何现代 Web 浏览器管理他们的游戏库。

该项目鼓励社区参与，通过 Discord 上的贡献和讨论。几个社区维护的项目，例如 Discord 机器人和 SteamOS 下载器，对 RomM 进行了补充。欢迎通过 Open Collective 支持该项目。文档提供了快速入门指南和故障排除步骤。

---

## 34. DeskHog，一个开源的开发者玩具

**原文标题**: DeskHog, an open-source developer toy

**原文链接**: [https://posthog.com/deskhog](https://posthog.com/deskhog)

DeskHog：一款为开发者带来乐趣的开源3D打印“开发者玩具”。它是一款掌上设备，配备ESP32-S3反向TFT Feather、彩色显示屏、Wi-Fi、蓝牙LE、10小时续航电池以及闪烁的LED灯。

该设备预装了“Pog”和“Flappy Hog”等游戏，但用户也可以使用AI编辑器或C++构建自己的游戏。 I²C扩展端口允许进行硬件扩展。除了游戏，DeskHog还可以作为PostHog数据的桌面终端，并提供番茄工作法计时器和破冰谈话等商业工具。

该设备通过扫描二维码并将其数据链接到“Insight Keeper-upper”来连接到PostHog项目。 虽然DIY版本目前支持趋势和大数据等洞察，但更多功能正在开发中，欢迎贡献。

DIY说明和3D打印文件可在GitHub上找到。 DeskHog套件即将推出。 带有额外按钮、表盘和潜在表带的“DeskHog Pro”也在考虑之中。

---

## 35. 需要多久才能知道一份工作是否适合你

**原文标题**: How long it takes to know if a job is right for you or not

**原文链接**: [https://charity.wtf/2025/06/08/on-how-long-it-takes-to-know-if-a-job-is-right-for-you-or-not/](https://charity.wtf/2025/06/08/on-how-long-it-takes-to-know-if-a-job-is-right-for-you-or-not/)

本文探讨了人们能够在多短时间内判断一份新工作是否合适，认为最初的印象往往是长期满意度的可靠指标。作者认为，根据个人经验，对一家公司的强烈直觉反应通常会在第一周内显现。能带来长期满意度的工作通常会引发与达到高标准相关的焦虑，而不利的工作则会产生一种令人沮丧的沉重感。

作者强调了信任自己直觉的重要性，尤其是对于管理者而言。虽然个人贡献者（ICs）有时即使在不利的环境中也能“敷衍了事”，但管理者需要与公司的价值观保持一致，因为他们的角色涉及代表公司并培养健康的团队活力。不一致可能会导致在道德上妥协的境地和无效的领导。

本文通过一个关于朋友的轶事来说明，这位朋友基于价值观的契合而担任了高级管理职位，但发现六个月后并不奏效。作者建议朋友开始规划退出策略，因为根本问题不太可能改变。文章还强调了从负面的工作经验中吸取教训，以避免将来犯类似错误的重要性。一个重要的收获是，有时从一份糟糕的工作中获得的最佳收获是更清楚地了解你不想要什么。最后，作者使用“鸡与猪”的隐喻来说明管理者所需的更深层次的承诺和个人投入。

---

## 36. 丹麦政府以Linux和LibreOffice取代Windows和Microsoft Office

**原文标题**: Danish Ministry Replaces Windows and Microsoft Office with Linux and LibreOffice

**原文链接**: [https://www.heise.de/en/news/From-Word-and-Excel-to-LibreOffice-Danish-ministry-says-goodbye-to-Microsoft-10438942.html](https://www.heise.de/en/news/From-Word-and-Excel-to-LibreOffice-Danish-ministry-says-goodbye-to-Microsoft-10438942.html)

丹麦国防部以Linux和LibreOffice取代Windows和Microsoft Office：文章摘要

丹麦国防部正在其行政部门中将Microsoft Windows和Microsoft Office逐步替换为Linux和LibreOffice。此举旨在降低许可成本并增强数字主权。

此次转换包括将现有的Windows操作系统替换为Linux发行版，并将Microsoft Office替换为开源的LibreOffice套件。该决定是在对替代方案进行全面评估后做出的，结论是Linux和LibreOffice能够充分满足该部的需求，同时提供显著的成本节约和对IT基础设施的更大控制权。

该部预计过渡将逐步进行，各部门以不同的速度迁移。已开展涉及特定部门的试点项目，以测试可行性并识别潜在挑战。该项目被认为是成功的，为更广泛的实施铺平了道路。

确定的主要挑战之一是确保与现有系统和软件的兼容性，以及为员工提供足够的培训以适应新环境。该部致力于提供必要的支持和培训，以确保平稳过渡。

最终，丹麦国防部的这一决定代表着政府组织中日益增长的趋势，即寻求减少对专有软件的依赖，并采用开源替代方案，以提高成本效益和更好地控制其数字资产。

---

## 37. 我的断网线冒险（2020）

**原文标题**: My Cord-Cutting Adventure (2020)

**原文链接**: [http://brander.ca/cordcut/](http://brander.ca/cordcut/)

本文记录了作者放弃有线电视的历程，突出了其间面临的意外挑战和挫折。作者认为消费电子公司已经放弃了视频录制设备的生产，实际上为有线电视公司创造了垄断，并限制了消费者的选择。他们详细描述了过去租用Shaw和Bell的DVR的经历，批评了它们的局限性以及录制内容的专有性质。

由于租用的DVR性能不佳，且零售商店缺乏录制选项，作者开始探索无线 (OTA) 天线。他们购买了一个Terk天线，并利用tvfool.com来优化其位置，以接收CBC、CTV和Global等本地频道。最初，他们遇到信号问题，通过禁用天线的放大器得以解决。作者称赞OTA广播的图像质量优于有线电视，将其归因于公共无线电波所需的更高带宽标准。

为了重新获得录制功能，作者探索了DVR选项，最终选择了HDHomeRun Connect Duo，这是一种通过网络传输电视信号的设备。这种极简的方法使他们能够利用现有的笔记本电脑作为DVR。他们承认有线以太网连接对于稳定的流媒体和录制至关重要。作者订阅了HDHomeRun的DVR软件和日程服务，以实现节目录制和日程安排功能。他们还强调了Netflix和Crave等互联网流媒体服务在促使他们放弃有线电视的决定中所起的作用。

---

## 38. 汲取传统：埃琳娜·伊斯奎在学校的秘鲁艺术

**原文标题**: Drawing on Tradition: Elena Izcue's Peruvian Art in the School

**原文链接**: [https://publicdomainreview.org/collection/peruvian-art-in-the-school/](https://publicdomainreview.org/collection/peruvian-art-in-the-school/)

借鉴传统：埃莱娜·伊斯库埃在学校推广秘鲁艺术（互联网档案馆文章可能探讨了秘鲁艺术家埃莱娜·伊斯库埃的生平和作品，重点关注她将前哥伦布时期的秘鲁艺术和设计融入教育环境的努力。

该文章可能突出了伊斯库埃在20世纪初对秘鲁民族认同的重要贡献，详细描述了她如何通过倡导欣赏和融合本土图案和技术来摆脱欧洲艺术的统治。 这包括将古代秘鲁艺术，特别是来自帕拉卡斯和纳斯卡文化的艺术，转化为适合在各种艺术媒介中复制和应用的易于理解的设计。

该文章可能考察了伊斯库埃的创新教学方法，或许会描述她为教授学生前哥伦布时期的艺术并激励他们创作自己的设计而采用的具体练习或项目。 它可能讨论她对其他艺术家和教育家的影响，以及她在秘鲁国内促进文化自豪感和艺术原创性方面的作用。 此外，它可能提到她艺术的各种形式，可能包括纺织品设计、陶瓷和装饰艺术，以及这些形式如何被用来传播她对独特秘鲁美学的愿景。）

---

## 39. 你现在可以在旧金山Valencia街合法地边走边喝酒了

**原文标题**: You can now legally walk with drinks on SF's Valencia St

**原文链接**: [https://missionlocal.org/2025/06/valencia-drinking-san-francisco/](https://missionlocal.org/2025/06/valencia-drinking-san-francisco/)

旧金山瓦伦西亚街推出新的“娱乐区”，允许在16街至21街之间的人行道上公开饮酒，成为该市首个不与特定活动相关的此类区域。从周四开始，参与酒吧和餐厅的顾客可以在周日至周四中午至午夜之间携带酒精饮料外出，并有可能扩展到周五和周六。

参与者必须出示身份证件、获得腕带并使用特殊品牌的杯子，且必须留在指定区域内。饮料不能在店铺之间携带，只能带到店铺外的人行道上。一项与旧金山警察局合作制定的安全计划已到位，以确保合规。

Blondie's、Tacolicious、Manny's 和 Fort Point 等商家均有参与。组织者强调，该区域能够保持正常的交通流量，这与需要封路的区域不同。

该举措符合市长卢瑞对公共社交空间和公共饮酒的关注，将其作为城市疫情后复苏的一部分，旨在吸引年轻人群，同时解决公共毒品使用问题。启动时间与每月一次的瓦伦西亚现场夜市相吻合，但将每周运营并覆盖更大的区域。

---

## 40. 恭喜您创建了 GitHub 上的第十亿个代码仓库

**原文标题**: Congratulations on creating the one billionth repository on GitHub

**原文链接**: [https://github.com/AasishPokhrel/shit/issues/1](https://github.com/AasishPokhrel/shit/issues/1)

此GitHub issue祝贺AasishPokhrel在GitHub上创建了第十亿个仓库，并恰当地命名为“shit”。该issue由“jonmagic”于2025年6月11日发起，包含一条祝贺这一里程碑的信息，并表达了希望该仓库能被用于构建伟大事物的愿望。其中还包含来自GitHub API的仓库ID 1000000000的JSON响应，显示了其基本信息：ID、节点ID、名称（“shit”）和完整名称（“AasishPokhrel/shit”）。祝贺信息以表情符号和反应结尾，表达了对这一成就的积极情绪。该issue详情还显示了标准的GitHub功能，如指派人、标签、项目和里程碑，但均未被分配。最后，该issue提到该仓库没有分支或pull request，并列出了可在issue中采取的操作。“shit”仓库已收到80个fork和1.4k个star。

---

## 41. 为什么韩国人会问你哪年出生的？

**原文标题**: Why Koreans ask what year you were born

**原文链接**: [https://bryanhogan.com/blog/korean-age](https://bryanhogan.com/blog/korean-age)

本文探讨了年龄在韩国文化中的重要性，并解释了为什么韩国人在初次见面后经常会询问你的出生年份。与许多西方文化不同，年龄在建立社会等级和确定适当的尊重程度方面起着重要作用。

询问出生年份的主要原因是了解关系动态并确定语言使用。韩语有多种敬语等级，以示尊重，年长者通常对年轻者“说低语”，而年轻者则反过来“说高语”。 了解某人的出生年份有助于确定哪种敬语等级和尊称是合适的。“朋友”（chingu）的概念通常只保留给同年出生的人。

本文还解释了国际年龄和韩国年龄之间的差异。在韩国年龄中，你出生时算作一岁，并在 1 月 1 日增加一岁，这意味着你的韩国年龄可能比你的国际年龄高一到两岁。这种差异可能会造成混淆，因此询问出生年份有助于在韩国语境中澄清年龄。虽然韩国正在朝着使用国际年龄制度的方向发展，但韩国年龄仍然根深蒂固于社会，影响着诸如法定饮酒年龄等方方面面。总之，在韩国询问出生年份是为了确立社会地位、语言表达的恰当性以及了解韩国年龄的细微差别。

---

## 42. 研究人员发现美国“失落的殖民地”之谜的证据

**原文标题**: Researchers discover evidence in the mystery of America's 'Lost Colony'

**原文链接**: [https://www.foxnews.com/travel/mystery-americas-lost-colony-may-finally-solved-after-440-years-archaeologists-say](https://www.foxnews.com/travel/mystery-americas-lost-colony-may-finally-solved-after-440-years-archaeologists-say)

考古学家认为他们有新的证据来解释罗阿诺克殖民地（也称为“失落的殖民地”）的命运，该殖民地于1590年从北卡罗来纳州罗阿诺克岛消失。在马克·霍顿的带领下，来自克罗阿托安考古学会的研究人员花了10年时间调查这个谜团。他们的发现表明，殖民者并非被杀或饿死，而是融入了哈特拉斯岛当地的克罗阿托安美洲原住民社会。

关键证据是在可追溯到16世纪末和17世纪初的美洲原住民垃圾堆中发现了“锤击鳞片”，这是一种在金属锻造过程中产生的微小铁屑。由于当时的美洲原住民缺乏炼铁技术，研究人员认为锤击鳞片表明英国殖民者生活并工作在克罗阿托安社区内。研究人员还在该地点发现了英国文物，如枪支、航海配件、炮弹、葡萄酒杯和珠子。

霍顿引用了18世纪的一份历史记录，该记录描述了哈特拉斯岛居民中具有欧洲特征且了解书籍的人，进一步支持了同化理论。虽然霍顿认为考古证据为殖民者遭遇提供了明确的解释，但他承认，无论科学发现如何，失落殖民地这个经久不衰的谜团可能会继续存在。

---

## 43. 揭秘EndBOX – 面向EndBASIC的微型计算机原型

**原文标题**: Unveiling the EndBOX – A microcomputer prototype for EndBASIC

**原文链接**: [https://www.endbasic.dev/2025/06/unveiling-the-endbox.html](https://www.endbasic.dev/2025/06/unveiling-the-endbox.html)

本文介绍了EndBOX，一款可直接启动进入EndBASIC编程环境的微型计算机原型，旨在重现早期计算体验的简洁和直接。EndBOX面向业余黑客和教育工作者，他们寻求一种以最小抽象来教授编程基础知识的工具。

该设备设想为一个便携式一体机，配备嵌入式计算机、平板电脑大小的屏幕和轻量级操作系统。作者强调了连接各种输入设备（键盘、鼠标、游戏手柄、GPIO）与程序交互的自由性。

目前存在两种原型：一种是带有7英寸触摸显示屏的标准型号，另一种是带有微型128x128 LCD的微型型号。两者都使用树莓派板（分别为3B+和Zero 2 W），并提供Wi-Fi用于云文件共享，计划支持蓝牙。基于NetBSD的EndBOX操作系统优先考虑快速启动时间和对电源中断的弹性。该操作系统允许通过CONFIG.BAS文件进行定制。

作者寻求社区支持，以完善该项目、应对硬件分发的复杂性并确定开发方向。鼓励读者订阅更新、赞助该项目、分享反馈意见，并有可能参与早期测试和原型访问。

---

## 44. EchoLeak – 零点击 AI 漏洞导致 365 Copilot 数据泄露

**原文标题**: EchoLeak – 0-Click AI Vulnerability Enabling Data Exfiltration from 365 Copilot

**原文链接**: [https://www.aim.security/lp/aim-labs-echoleak-blogpost](https://www.aim.security/lp/aim-labs-echoleak-blogpost)

EchoLeak：微软365 Copilot中新发现的零点击AI漏洞，可能泄露敏感数据。该漏洞利用大型语言模型的范围，允许泄露Copilot上下文中的数据，包括聊天记录、从Microsoft Graph获取的数据以及预加载的用户和组织信息。

与以往需要用户交互或数据泄露有限的AI漏洞不同，EchoLeak无需特定用户行为即可绕过现有防护措施，构成重大威胁。尽管微软声称没有客户受到影响，但在最近解决之前，默认的Copilot配置使组织面临风险。数据丢失防护标签和敏感度标签等安全控制措施可以降低风险，但也会降低Copilot的功能。

文章强调，LLM范围违规是AI应用特有的一种新型威胁，标准AI防护措施无法解决。任何依赖于LLM并接受不受信任输入的AI代理或RAG（检索增强生成）应用都可能存在漏洞。Aim Labs已开发出实时防护措施，以防止这些漏洞，适用于各种AI代理和RAG应用。如需了解更多信息或获得保护，请联系labs@aim.security。

---

## 45. 加拿大C++大会

**原文标题**: The Canadian C++ Conference

**原文链接**: [https://cppnorth.ca/index.html](https://cppnorth.ca/index.html)

CppNorth：加拿大C++大会，将于2025年7月20-23日在多伦多举行。 秉承多伦多用户组的成功经验，本次大会承诺带来三天的学习、交流，以及C++社区最新发展探索，汇聚本地及外地演讲者。

重点包括公布日程安排、志愿者招募以及King Edward酒店的预订信息。 大会拥有强大的主讲嘉宾阵容，包括Scott Hanselman、Alex Dathskovsky、Sheena Yap Chan和Kate Gregory。 演讲投稿已截止，收到的投稿数量众多，预示着精选领域内的最佳内容。

CppNorth由多家赞助商支持。 Autodesk是黄金赞助商。 JetBrains是再次赞助视频的赞助商。 大会还将举办“归属感晚宴”，特邀Negar Farjadnia担任演讲嘉宾。 此外，大会还提供赞助机会，强调其对知识、包容性和乐趣的承诺。

---

## 46. 植物能听到授粉者的声音，并产生香甜的花蜜作为回应。

**原文标题**: Plants hear their pollinators, and produce sweet nectar in response

**原文链接**: [https://www.cbc.ca/listen/live-radio/1-51-quirks-and-quarks/clip/16150976-plants-hear-pollinators-produce-sweet-nectar-response](https://www.cbc.ca/listen/live-radio/1-51-quirks-and-quarks/clip/16150976-plants-hear-pollinators-produce-sweet-nectar-response)

基于我对类似研究的理解，以下是加拿大广播公司（CBC）电台“奇闻异事”节目中题为“植物能听见传粉者，并产生更甜的蜜汁作为回应”片段的摘要：

这篇文章可能讨论了研究表明，一些植物可以“听见”其传粉者（如蜜蜂）的声音，并通过产生更甜的蜜汁作为回应。这表明植物和传粉者之间的关系比以前认为的更加复杂和互动。

该研究可能涉及将植物暴露于模仿蜜蜂嗡嗡声或昆虫翅膀拍打声的实验。然后，研究人员测量了这些植物产生的花蜜中的糖浓度，并与未暴露于这些声音的对照组进行了比较。该研究可能发现，暴露于传粉者声音的植物在短时间内增加了花蜜的含糖量。

这种对声音做出反应的能力可能是一种进化适应，有助于植物更有效地吸引传粉者。通过在传粉者附近时产生更甜的蜜汁，植物可以增加成功授粉的可能性。这给植物带来优势，因为传粉者更有可能记住并返回到提供更高回报的植物。

该研究突出了植物复杂的感知能力，并挑战了将植物视为被动生物的传统观点。它表明，植物正在积极地与环境互动，并以有利于其生存和繁殖的方式对刺激做出反应。

---

## 47. 我如何用Agent编程

**原文标题**: How I Program with Agents

**原文链接**: [https://crawshaw.io/blog/programming-with-agents](https://crawshaw.io/blog/programming-with-agents)

Crawshaw 的文章探讨了使用“代理”进行编程，这些“代理”被定义为在 `for` 循环中的 LLM，它们可以执行命令并观察输出，无需人工干预。他将代理驱动的编程与使用无代理 LLM 的“白板编程”进行对比，强调了代理通过提供环境反馈（如编译器错误和测试结果）所带来的显著改进。

代理擅长使用熟悉的工具（如 `bash`）导航代码库，从而能够有效地查找、读取和修改代码。这可以带来更好的 API 使用、更少的语法错误、改进的依赖管理以及处理更大代码库的能力。代理甚至可以与最终产品交互，例如根据浏览器渲染调整 CSS。主要的缺点是由于代理的中间操作，时间和潜在成本会增加。

作者提供了示例。首先是为 sketch.dev 实现 Github App 身份验证，代理成功创建了身份验证流程，但最初引入了安全和性能问题。其次是关于 JSON 的 SQL 约定，代理最初难以掌握这种风格，直到它被添加到 SQL 模式文件中作为描述。他强调，虽然代理不能取代程序员，但它们可以显著加速“乏味”的任务。

他还挑战了代码生成在总体编码成本中只占很小一部分的观点，认为代理即使在维护现有产品方面也很有价值，因为它们还可以删除代码。

---

## 48. 展示HN：用“AR”眼镜自制虚拟HDMI显示器

**原文标题**: Show HN: DIY virtual HDMI monitor using "AR" glasses

**原文链接**: [https://github.com/mgschwan/viture_virtual_display](https://github.com/mgschwan/viture_virtual_display)

这个“Show HN”帖子介绍了一种DIY虚拟HDMI显示器解决方案，它使用“AR”眼镜（特别是Viture头显）和单板计算机（SBC），例如Orange Pi 5 Plus。该项目名为`v4l2_gl`，它捕获HDMI输入，将其转换为RGB，并在OpenGL窗口内的纹理四边形上显示，从而创建一个通过AR眼镜可见的虚拟显示器。

该项目目前处于早期开发阶段，面临性能挑战，但提供IMU集成用于头部跟踪（Viture头显）、测试图案生成和平面几何调整。它需要一个基于Linux的操作系统，并具有特定的依赖项，如OpenGL、GLUT、`libv4l2`，以及可选的`libhidapi-dev`，用于反向工程的Viture协议。

提供了针对反向工程协议和官方Viture SDK的编译说明，从而生成可执行文件`v4l2_gl`和`v4l2_gl_viture_sdk`。命令行选项允许用户自定义设备路径，启用全屏模式，集成Viture IMU，显示测试图案，并调整平面距离和比例。实现了一个摇头手势来重置视图的旋转。

未来的计划包括支持USB HDMI采集卡，以实现更广泛的SBC兼容性（如Raspberry Pi）、错误修复、性能改进、支持MJPEG以获得更好的帧率，以及添加诸如快速旋转居中手势和曲面屏幕选项等功能。该项目旨在提供一种可定制且便携的虚拟显示解决方案。

---

## 49. OpenPlanetData – 每日免费星球OSM PBF和GOL索引快照

**原文标题**: OpenPlanetData – Free Daily Planet OSM PBF and GOL Indexed Snapshots

**原文链接**: [https://openplanetdata.com](https://openplanetdata.com)

OpenPlanetData 是一项致力于改善地球开放数据访问的倡议。他们的首个项目提供 OpenStreetMap (OSM) 数据的每日快照，格式为 PBF 和 GOL，均可免费获取。数据托管在 Cloudflare R2 上，以便快速且在全球范围内下载。其关键创新在于 GOL 格式，这是一种利用 Geodesk 的 PBF 数据索引版本，可实现极快的空间查询。用户可以下载这些每日快照来利用 OSM 数据。如有问题或反馈，用户可以联系他们。

---

## 50. OpenAI o3-pro

**原文标题**: OpenAI o3-pro

**原文链接**: [https://help.openai.com/en/articles/9624314-model-release-notes](https://help.openai.com/en/articles/9624314-model-release-notes)

无法访问文章链接。

---

## 51. 1834年景观园艺指南的启示

**原文标题**: Lessons from That 1834 Landscape Gardening Guidebook

**原文链接**: [https://fi-le.net/pueckler/](https://fi-le.net/pueckler/)

本文探讨了赫尔曼·路德维希·海因里希·冯·普克勒-穆斯考伯爵1834年的景观园艺指南《景观园艺提示》中的经验，并将其应用于IDE和开放世界RPG等数字环境中更广泛的设计原则。

关键在于如何创造引人入胜且有目的性的环境。本文重点介绍了三个主要经验：

1.  **展示障碍：** 路径中的人工曲线应有可见的理由，使用户感到绕道是必要的，而不是随意的。这可以转化为UI/UX设计，即解决方案不仅应该是最佳选择，而且*看起来*也应该是局部最佳选择。

2.  **略微隐藏城堡：** 过度暴露于令人印象深刻的景象会削弱其影响力。控制前景以创造期待和戏剧性，逐步展现宏伟的景色。塞尔达游戏就是一个例子，持续的可见性会削弱精心设计的景观的影响。视觉领域应仔细管理，以最大限度地提高发现的宣泄释放。

3.  **模仿，而非模拟：** 人工环境要么应该有真正的目的，要么令人信服地模仿自然。深入研究自然模式，以真实地模拟它们，比如河岸的不均匀侵蚀。优先考虑真正的功能，而不是单纯的装饰，否则可能会创造出“怪异且不协调”的东西。

文章最后鼓励读者将这些景观园艺原则应用于数字和物理环境的设计，以带来快乐和目的性。

---

## 52. 月经跟踪App数据是广告商的金矿，但会危及女性安全。

**原文标题**: Menstrual tracking app data is gold mine for advertisers that risks women safety

**原文链接**: [https://www.cam.ac.uk/research/news/menstrual-tracking-app-data-is-a-gold-mine-for-advertisers-that-risks-womens-safety-report](https://www.cam.ac.uk/research/news/menstrual-tracking-app-data-is-a-gold-mine-for-advertisers-that-risks-womens-safety-report)

剑桥大学Minderoo科技与民主中心的一份新报告警告称，月经周期追踪应用（CTAs）是广告商的“金矿”，对女性构成严重的隐私和安全风险。这些应用收集包括运动、饮食、药物和性偏好在内的私密数据，然后在缺乏充分监管或用户同意的情况下用于消费者画像。

研究人员认为，这些数据比一般人口统计信息更有价值，可能被用于定向广告、就业歧视、健康保险歧视、网络跟踪以及限制堕胎途径。报告强调，由CTAs主导的女性科技产业预计到2027年将达到600亿美元，加剧数据的商品化。

作者呼吁加强治理，敦促应用程序提供清晰的同意选项，并主张国民医疗服务体系（NHS）等公共卫生机构开发值得信赖的、研究驱动的替代方案。他们指出，现有的法规，尤其是在美国，是不充分的，将月经数据视为“一般健康”信息，而不是敏感的医疗数据。

他们建议用户应该能够删除应用内和公司服务器上的数据，并鼓励在学校进行医疗数据应用程序教育，以提高数字素养和意识。该报告强调有必要保护女性的生殖生活免受私营公司的控制，并强调在适当的监管和监督下，将月经数据用于合法的医学研究和医疗保健目的的潜在益处。

---

## 53. 海军支持维修权，此前130亿美元航母出现半供电故障。

**原文标题**: Navy backs right to repair after $13B carrier goes half-fed

**原文链接**: [https://www.theregister.com/2025/06/11/us_navy_repair/](https://www.theregister.com/2025/06/11/us_navy_repair/)

受损烤箱导致价值130亿美元的“杰拉尔德·R·福特”号航母难以供餐等事件的刺激，美国海军正在推动在合同中加入“维修权”条款。海军部长约翰·费兰在参议院表示，海军需要能够自行维修设备，而不是依赖于受知识产权限制的昂贵且缓慢的供应商维修。陆军也有同样的担忧，国防部长皮特·黑格塞斯指示陆军在未来的合同中加入维修权条款。陆军部长丹尼尔·德里斯科尔强调需要能够自行维修装备，而无需依赖承包商。

参议员伊丽莎白·沃伦提出了《军人维修权法案》，旨在授权军事人员维修自己的设备。iFixit首席执行官凯尔·维恩斯对此表示支持，称“修理烤箱不是火箭科学”。军方的立场呼应了在各州日益受到关注的更广泛的维修权运动，该运动主张消费者获得维修文档和零件的权利。陆军和海军已经明确表示，如果公司不愿意赋予他们维修权，那么合同谈判将会很困难。

---

## 54. 多莉·帕顿的梦幻世界快车

**原文标题**: Dolly Parton's Dollywood Express

**原文链接**: [https://thetransitguy.substack.com/p/dolly-parton-runs-a-train-busier](https://thetransitguy.substack.com/p/dolly-parton-runs-a-train-busier)

无法访问文章链接。

---

## 55. 数独反思：或思考系统化的不可能

**原文标题**: Reflections on Sudoku, or the Impossibility of Systematizing Thought

**原文链接**: [https://rjp.io/blog/2025-06-07-reflections-on-sudoku](https://rjp.io/blog/2025-06-07-reflections-on-sudoku)

本文探讨了将思维系统化的不可能，并将其与判定性问题（逻辑中的决策问题）进行类比，同时对比了解决数独难题的两种方法。作者反思了自身在开发系统化问题解决过程中的挣扎，表达了对通用方法的需求，但最终得出结论，认为这是无法实现的。

文章将Ron Jeffries的测试驱动开发（TDD）方法与Peter Norvig更具分析性、基于知识的方法进行对比。 Jeffries是TDD的倡导者，他花费了大量精力，但最初并未实现一个可用的求解器，而Norvig凭借他在人工智能和搜索算法方面的专业知识，简洁地解决了这个问题。作者认为，Jeffries的挣扎源于一个隐含的信念，即TDD可以系统化编程，从而否定了对特定领域知识的需求。

借鉴判定性问题，作者认为，解决所有问题的通用算法是不可能的，这反映了寻找一个程序来确定另一个程序是否解决特定任务的局限性。文章强调，虽然过程可以帮助编程，但新问题需要洞察力和一个装备精良的知识和技术“工具箱”。

作者最后提供了一个个人的实用技巧包，包括向他人学习、采用科学的思维模式、退后一步进行思考、练习编程和写作、讨论想法以及利用LLM等工具。中心信息强调，在承认系统化的内在局限性的同时，拥抱问题解决的乐趣和艺术。

---

## 56. AOSP未死，但谷歌给定制ROM开发者带来一击。

**原文标题**: AOSP isn't dead, but Google just landed a blow to custom ROM developers

**原文链接**: [https://www.androidauthority.com/google-not-killing-aosp-3566882/](https://www.androidauthority.com/google-not-killing-aosp-3566882/)

本文探讨了谷歌近期对安卓开放源代码项目（AOSP）的更改以及对自定义ROM开发的影响，尤其是对Pixel设备的影响。 尽管谷歌坚称AOSP并未被停止，但他们已从最新的AOSP版本（Android 16）中省略了Pixel手机的设备树和驱动二进制文件。

谷歌解释说，这一改变是因为他们正在将AOSP参考目标从Pixel硬件转移到一个名为“Cuttlefish”的虚拟设备，以创建一个更中立的平台，从而更广泛地实现设备实施。

然而，这一决定对自定义ROM开发者产生了重大影响。 以前，开发者可以很容易地使用谷歌提供的配置为Pixel设备构建AOSP。 现在，他们必须从旧的设备树和预构建的二进制文件中反向工程更改，这使得过程更加困难和耗时。 压缩后的内核源代码提交历史进一步阻碍了开发，因为它移除了用于错误修复和安全补丁的宝贵参考点。

虽然谷歌没有义务提供这些资源，但他们之前的支持使得为Pixel设备构建自定义ROM更容易。 本文总结认为，这些改变将增加开发者的工作量，并使在Pixel手机上维护稳定的自定义ROM体验更具挑战性，使体验与其他安卓设备保持一致。 本文还指出，Pixel仍然很容易解锁引导加载程序并获取工厂镜像。

---

## 57. 微调大型语言模型是浪费时间。

**原文标题**: Fine-tuning LLMs is a waste of time

**原文链接**: [https://codinginterviewsmadesimple.substack.com/p/fine-tuning-llms-is-a-huge-waste](https://codinginterviewsmadesimple.substack.com/p/fine-tuning-llms-is-a-huge-waste)

以下是我基于对相关讨论的理解，以及对微调大型语言模型（LLM）这种常见做法的反驳论点，对文章《微调LLM是在浪费时间》的总结：

这篇文章可能认为，对于大多数用例而言，微调LLM通常是一种低效且不必要的策略。它可能强调，微调带来的好处（如提高准确性或特定任务的性能）往往是微不足道的，不足以证明所需的巨大资源是合理的，这些资源包括计算能力、数据准备和工程专业知识。

文章中可能提出的主要论点包括：

*   **成本和复杂性：** 微调LLM计算成本高昂，并且需要数据准备、超参数调整和模型评估方面的专业知识。
*   **改进有限：** 对于许多任务，提示策略和上下文学习可以以更少的成本和精力实现与微调相当甚至更优越的性能。
*   **过拟合风险：** 在有限的数据集上进行微调可能会导致过拟合，即模型在训练数据上表现良好，但在未见过的数据上表现不佳。
*   **提示工程替代方案：** 有效的提示工程（包括诸如少样本学习（在提示中提供示例）之类的技术）通常可以从预训练的LLM中引出所需的行为，而无需进行微调。
*   **新兴技术：** LLM的快速发展意味着未来的模型可能会更强大，并且针对特定应用需要更少的微调。

本质上，这篇文章可能提倡一种更务实的方法，建议开发人员在考虑昂贵而复杂的微调过程之前，应优先考虑提示工程、上下文学习以及利用预训练LLM的能力。对于大多数人来说，花费在微调上的时间和金钱，如果用于开发更好的提示和系统架构，将会产生更好的结果。

---

## 58. 塞缪尔·佩皮斯的日记

**原文标题**: The Diary of Samuel Pepys

**原文链接**: [https://www.historytoday.com/archive/feature/hidden-diary-samuel-pepys](https://www.historytoday.com/archive/feature/hidden-diary-samuel-pepys)

本文探讨了塞缪尔·佩皮斯日记于1825年6月首次出版后的最初影响和持久受欢迎程度。它强调了该日记的迅速成功，并列举了引起公众共鸣的段落，例如佩皮斯对伦敦大火、他的新假发以及他第一次喝茶的描述。文章指出，到19世纪末，该日记迅速成为英国历史和文学中备受赞誉的经典之作。

此外，它强调了佩皮斯在当今的持续影响力，提到了他在博物馆展览和历史小说中的出现，以及他被用作向学生介绍复辟时期和历史研究的工具。即使是遵循国家课程的幼儿也熟悉日记中的轶事，例如佩皮斯在大火中埋藏奶酪。

然而，文章也暗示了日记出版背后可能存在的复杂性，提到了关于删节及其原因的“传言”。为了访问完整文章并可能发现更多关于这些删节的信息，读者被提示购买订阅。

---

## 59. Show HN：Ikuyo，旅行计划Web应用

**原文标题**: Show HN: Ikuyo a Travel Planning Web Application

**原文链接**: [https://ikuyo.kenrick95.org/](https://ikuyo.kenrick95.org/)

这是一个“Show HN”帖子，介绍一个名为“Ikuyo”的旅行规划网络应用程序。帖子本身非常简短，只写了应用程序的名字“Ikuyo！”这表明该帖子很可能是想链接到一个单独的网页或存储库，其中包含有关该应用程序的更详细信息。

由于内容非常少，无法进行全面总结。 但是，我们可以推断出以下内容：

*   **目的：** Ikuyo 是一款专注于旅行规划的工具。
*   **平台：** 这是一个网络应用程序。
*   **展示：** 它正在 Hacker News（“Show HN”）上展示。 这意味着创建者正在寻求反馈、曝光或潜在的合作者。
*   **名称：** “Ikuyo！”听起来像日语，可能表明该应用程序是为日本旅行而设计的，但这只是推测。

要了解其功能、特性或目标受众，需要访问与“Show HN”帖子相关的链接资源。

---

## 60. Shell命令的奇怪案例，或“此漏洞为POSIX所要求”（2021）

**原文标题**: The curious case of shell commands, or how "this bug is required by POSIX" (2021)

**原文链接**: [https://notes.volution.ro/v1/2021/01/notes/502e747f/](https://notes.volution.ro/v1/2021/01/notes/502e747f/)

本文详细介绍了类UNIX系统中一个常见的陷阱：某些工具通过`system(3)`函数将命令执行委托给`sh -c`，如果用户输入没有经过仔细的安全处理，可能导致潜在的shell注入漏洞。作者认为，这种方法看似无害，甚至被某些工具文档（如`watch`）隐式认可，但从根本上是有缺陷的，是许多错误和安全问题的根源。

问题的出现是因为许多工具接受命令作为参数，然后将这些参数传递给`sh -c`，这要求开发者必须仔细地转义和引用参数，以防止意外的shell扩展或解释。本文强调，即使看似安全的命令，通过这种机制传递也可能变得危险。

作者首先探讨了POSIX文档中缺乏关于此问题的明确警告。然后，他们提出了一系列逐渐复杂，但最终并不完美的“复杂解决方案”，以减轻在使用这些工具时shell注入的风险，最终建议使用`--`和`@Q` bash扩展。

文章随后提供了使用`watch`、`ssh`和`i3-msg`的案例研究，以说明不同的工具如何处理命令执行，突出了不一致性和意外行为的可能性。核心要点是，开发人员应尽量避免依赖`system(3)`或`sh -c`的工具，而是选择通过`execve(2)`直接执行命令的解决方案，或贡献补丁来修复有问题的工具。如果无法避免，则需要极其谨慎和复杂的引用策略来防止漏洞。

---

## 61. 2025年5月（版本1.101）

**原文标题**: May 2025 (Version 1.101)

**原文链接**: [https://code.visualstudio.com/updates/v1_101](https://code.visualstudio.com/updates/v1_101)

Visual Studio Code 2025年5月版(1.101版本)发布，引入多项新功能和改进，重点在于增强AI集成、改进聊天功能和提升编辑器体验。

主要亮点包括对提示、资源、采样（实验性）和身份验证的Model Context Protocol (MCP)支持。用户现在可以在聊天中创建和管理工具集，将相关工具分组以便于访问。源代码控制受益于新的图形视图，GitHub Copilot Coding Agent的工作分配已集成到VS Code中。

聊天增强功能包括改进用户和AI消息之间的区分、更方便的撤消功能和可导航的附件。编辑器现在简化了文件编辑，提供更高效的编辑应用方法和对齐的键盘绑定。隐式上下文简化了在聊天中包含当前文件的过程。

自定义聊天模式现已可用（预览版），允许用户为特定工作流程定义特定指令和工具。聊天代理现在可以识别任务诊断错误和终端的当前工作目录。浮动聊天窗口提供新的停靠和会话选项。内置工具可以自定义，并且改进了诸如将Web元素发送到聊天之类的实验性功能。

辅助功能增强功能包括用户操作和代码操作的声音，以及改进的代理模式辅助功能信息。编辑器改进包括“边输入边查找”设置和可自定义的菜单。进程资源管理器现在支持Web访问，并且为PowerShell实现了Windows shell环境发现。现在，对于未发布的扩展会显示警告指示。

---

## 62. 约翰迪尔必须面对第二起维修权诉讼

**原文标题**: John Deere Must Face Second Right to Repair Lawsuit

**原文链接**: [https://www.jalopnik.com/1884621/john-deere-right-to-repair-lawsuit/](https://www.jalopnik.com/1884621/john-deere-right-to-repair-lawsuit/)

约翰迪尔因涉嫌垄断拖拉机和农业设备维修，正面临第二起诉讼，这次来自联邦贸易委员会和五个州。此前已有一起来自集体诉讼，针对同一问题。核心指控是约翰迪尔限制获取维修所需的专业软件和工具，实际上迫使农民使用更昂贵的授权经销商。

伊利诺伊州地方法院法官裁定，联邦贸易委员会和州政府的诉讼可以继续进行，驳回了约翰迪尔关于政府缺乏起诉资格的论点。该法官也在监督集体诉讼，他认为约翰迪尔的论点重复且缺乏说服力，并将其比作不成功的电影续集。该裁决凸显了农民在购买时可能缺乏对维修限制以及相关成本和不便的认识。

诉讼称，由于缺乏必要的软件和工具，农民被迫依赖约翰迪尔的授权经销商进行关键维修。这并非约翰迪尔在维修权问题上首次成为新闻，此前报道涉及拖拉机的越狱代码、关于可维修性的虚假声明指控，以及保护维修权的立法努力。尽管约翰迪尔承诺放宽维修限制，但其行动表明情况并非如此，尤其是在面对潜在的维修权法律的情况下。

---

## 63. Magistral — Mistral AI 首个推理模型

**原文标题**: Magistral — the first reasoning model by Mistral AI

**原文链接**: [https://mistral.ai/news/magistral](https://mistral.ai/news/magistral)

Mistral AI 发布首个推理模型 Magistral，专为特定领域、透明且多语言推理设计。它有两个版本：Magistral Small（一个 24B 参数的开源模型）和 Magistral Medium（一个更强大的企业版本）。Magistral Medium 在 AIME2024 上取得了 73.6% 的分数，通过 64 次多数投票达到了 90%，而 Magistral Small 分别获得了 70.7% 和 83.3% 的分数。

主要特性包括跨多种语言的本地思维链推理、企业用例的多功能性，以及 Le Chat 中提供 10 倍更快响应的“思考模式”。Magistral 针对多步逻辑进行了微调，增强了可解释性并提供了可追溯的思考过程。它擅长英语、法语、西班牙语和中文等语言。

Magistral 适用于需要更长思考过程和准确性的应用，从法律研究和财务预测到软件开发和创意故事讲述。它支持业务战略、受监管行业、系统工程和内容创作。

Magistral Small 可在 Hugging Face 上下载，采用 Apache 2.0 许可。Magistral Medium 可通过 Le Chat、La Plateforme、Amazon SageMaker 访问，并很快将在 IBM WatsonX、Azure AI 和 Google Cloud Marketplace 上提供。Mistral AI 也在积极招聘，寻找为未来 AI 创新做出贡献的人才。

---

## 64. 达尔文哥德尔机：自我提升智能体的开放式演化

**原文标题**: Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents

**原文链接**: [https://arxiv.org/abs/2505.22954](https://arxiv.org/abs/2505.22954)

达尔文哥德尔机 (DGM)：一种实现自我改进 AI 代理的新方法

---

## 65. 来自 Mozilla 内部人士（未参与该项目）讲述的 Firefox OS 故事（2024）

**原文标题**: Firefox OS's story from a Mozilla insider not working on the project (2024)

**原文链接**: [https://ludovic.hirlimann.net/2024/01/firefox-oss-story-from-mozila-insider.html](https://ludovic.hirlimann.net/2024/01/firefox-oss-story-from-mozila-insider.html)

这篇博客文章由一位前Mozilla员工于2024年1月撰写，从内部人士的角度讲述了Firefox OS（前身为Boot to Gecko，B2G）的故事。作者此前曾参与Thunderbird的开发，他描述了Mozilla如何因担心错过移动革命，而将重心转移到B2G，以创建一个开源移动操作系统来与Apple和Android竞争。

这种转变导致了更具层级的组织结构，对B2G的关注牺牲了Thunderbird以及最终的Firefox桌面版，并增加了员工人数。Mozilla与多家运营商和手机制造商寻求合作，由于仓促的截止日期，导致了相互冲突的需求和质量问题。

虽然Mozilla的员工被配备了Firefox OS手机进行测试，但作者认为该产品发布得过早，并忽略了关键领域，主要是质量和桌面版Firefox。到2015年，Mozilla突然关闭了Firefox OS项目，并重新专注于桌面端。

作者认为B2G具有潜力，特别是拥有整个技术栈的想法。然而，他们指责其快速的开发节奏、对桌面浏览器（公司收入来源）的忽视，以及在产品尚未完善之前过早地与合作伙伴接触。作者建议采取更分阶段的方法，包括彻底的内部测试和社区参与，可能会产生不同的结果。他们得出结论，Firefox OS的失败导致了Mozilla与其社区互动的减少。

---

## 66. 互联网的中心化

**原文标题**: The Centralization of the Internet

**原文链接**: [https://www.thepublicdiscourse.com/2021/08/77139/](https://www.thepublicdiscourse.com/2021/08/77139/)

题为《互联网的中心化》的文章，发表于2025年6月11日，以“世代、神职与父权本质”为隐喻，探讨了互联网不断变化的格局。

虽然在无法访问全文的情况下，其具体联系尚不明确，但文章可能论述的是互联网正从其去中心化的起源，朝着由少数实体控制的更为中心化的结构发展。“父权”这一隐喻可能代表着这些强大的控制力量。

“世代”方面可能指的是互联网最初的、去中心化的世代，而“神职”则可能代表着为了控制访问和信息流而出现的中介或守门人。

本质上，这篇文章可能哀叹互联网最初的开放和平均主义精神的丧失，认为少数主导者正日益塑造和控制着在线体验，从而可能限制自由和创新。世代、神职与父权的类比强调了权力动态的转变，“父亲”形象（中心化控制）对数字景观施加了更大的影响。这是对科技巨头手中权力日益巩固及其对互联网未来影响的批判性评论。

---

## 67. AlphaWrite：通过自我演化故事来提升写作能力的AI

**原文标题**: AlphaWrite: AI that improves at writing by evolving its own stories

**原文链接**: [https://tobysimonds.com/research/2025/06/06/AlphaWrite.html](https://tobysimonds.com/research/2025/06/06/AlphaWrite.html)

本文介绍了AlphaWrite，一种通过进化方法改进创意文本生成的新型框架。它解决了在写作等主观领域中扩展推理时计算的挑战，在这些领域中，传统的指标是不够的。

AlphaWrite采用多代过程。它首先基于随机的作者风格和主题生成一组不同的故事。然后，使用LLM评判员和Elo排名通过成对比较评估这些故事。根据排名，最好的故事通过进化过程进行改进，该过程涉及选择、使用改进目标（叙事结构、人物发展等）生成变体以及更新种群。这个迭代过程会重复多次。

作者证明，AlphaWrite显著提高了故事质量，与初始故事生成相比，偏好率达到72%，与使用Llama 3.1 8B模型的顺序提示基线相比，偏好率达到62%。

本文还探讨了一个递归的自我改进循环，其中来自AlphaWrite的增强输出被提炼回基础模型作为训练数据，从而在后续世代中实现进一步的改进。初步结果显示，在使用AlphaWrite生成的故事进行微调后，与基础模型相比，偏好率为56%。

除了创意写作之外，AlphaWrite还可以通过引导更好的基础模型来适应目标生成、特定领域的应用和模型增强。结论强调了进化方法在系统地提高人工智能系统写作能力方面的潜力。

---

## 68. Show HN: S3mini – 轻巧快速的S3兼容客户端，无依赖，边缘就绪

**原文标题**: Show HN: S3mini – Tiny and fast S3-compatible client, no-deps, edge-ready

**原文链接**: [https://github.com/good-lly/s3mini](https://github.com/good-lly/s3mini)

S3mini：轻量级、无依赖的 TypeScript S3 兼容对象存储客户端，适用于 Node.js、Bun、Cloudflare Workers 和其他边缘环境（不包括浏览器）。它体积小巧（压缩后约 14KB），性能优于更重的替代方案（≈15% 的操作/秒）。它支持 AWS SigV4 身份验证，无需预签名请求。

S3mini 提供基本的 S3 操作，包括存储桶存在性检查、存储桶创建、对象列表（ListObjectsV2）、对象检索（GetObject 变体）、对象上传（PutObject）和对象删除（DeleteObject），以及分段上传功能。它已在 Cloudflare R2、Backblaze B2、DigitalOcean Spaces、MinIO 和 Garage 上进行了测试。

可以使用 npm、yarn 或 pnpm 轻松安装。 提供了用法示例，涵盖基本存储桶和对象操作，包括分段上传和使用范围请求的下载。 该文档强调了使用环境变量进行安全凭证管理的重要性，并强调负责任地使用分段上传以避免不必要的成本。

该项目欢迎贡献，鼓励用户报告问题和提交 pull request，优先考虑轻量级添加和社区行为。 该库已获得 MIT 许可证许可，并鼓励赞助以支持持续开发。

---

## 69. 极乐：一张著名照片背后的故事 (2012)

**原文标题**: Bliss – The story behind one of the most famous photographs (2012)

**原文链接**: [https://amateurphotographer.com/iconic-images/bliss-by-charles-orear-iconic-photograph/](https://amateurphotographer.com/iconic-images/bliss-by-charles-orear-iconic-photograph/)

摄影师查尔斯·奥瑞尔的作品《极乐》（Bliss）是一幅生机勃勃的图像，描绘了在明亮的蓝天下郁郁葱葱的绿色山坡，2002年，它成为Windows XP的默认壁纸，成为世界上最知名的图像之一。虽然有些人可能觉得它平淡无奇，但其广泛的使用让数十亿人看到了它。

奥瑞尔是一位经验丰富的专业摄影师，曾为《堪萨斯城星报》、《洛杉矶时报》和《国家地理》工作。1998年1月，他在加利福尼亚州纳帕谷的家附近拍摄了这张照片。他被山坡独特的魅力所吸引，特别是它在冬季的变化，那时草地变绿，云朵聚集。他用手持的玛米亚RZ67胶片相机记录了这一场景。

奥瑞尔将这张照片提交给了比尔·盖茨拥有的图片库Corbis。微软选择了《极乐》作为Windows XP的壁纸，因为它具有吸引力和诱人的特性。这张照片也是该软件2亿美元广告活动的关键组成部分。摄影师获得了该图像版权的一大笔报酬，尽管具体金额仍未公开。

微软做了极少的改动，主要是裁剪和加强了山坡的绿色。奥瑞尔对这张照片的成名仍然保持谦逊，认为这是在正确的时间出现在了正确的地点。尽管《极乐》很简单，但它仍然是住在标志性地点附近的奥瑞尔的骄傲。他还出版了几本关于葡萄酒和葡萄园的书籍，包括《纳帕谷：土地、葡萄酒、人民》（2011年），并在他的网站www.wineviews.com上展示了他更多的作品。

---

## 70. 表征我对纯铜无源器件的首次尝试

**原文标题**: Characterizing my first attempt at copper-only passives

**原文链接**: [https://moroso.emarhavil.com/~joshua/2pf-characterization.html](https://moroso.emarhavil.com/~joshua/2pf-characterization.html)

本文详细介绍了作者尝试使用Scikit-RF中的各种校准技术，精确测量铜制小型射频无源器件（特别是2pF电容器）的过程。最终目标是将这些技术用于制造廉价的GHz级示波器探头。

最初，使用HP 8753C和NanoVNA进行的测量产生了不令人满意的结果，包括S11值大于0dB。 随后，使用了新的Siglent SVA1032X和LibreCAL eCal。 作者发现，将校准平面定义在连接器边缘，而不是DUT边缘，可以提供更合理的史密斯圆图结果，显示电容器与传输线串联。

然后，作者探讨了使用不同方法校准数据：首先，通过使用Scikit-RF重现先前不准确的校准方法，以证明他们对工具的理解，然后通过实施“端口扩展”来去除已知长度的传输线的影响。 他们通过级联一个理论上完美的扩展的反函数，成功地使用Scikit-RF复制了VNA的“端口扩展”行为。

最后，作者解决了由于长度变化导致的板载校准标准不一致问题。 通过将长度调整纳入校准标准定义中，他们实现了更准确的电容器测量，并通过分析阻抗的实部和虚部进行了验证。 最终结果显示出合理的电容值，但区分“真实”电容行为与测量伪像仍然是一个挑战。

---

## 71. 电视愚人：查看您能接收的无线电视 (OTA) 频道

**原文标题**: TV Fool: See OTA channels you can receive

**原文链接**: [https://www.tvfool.com/index.php?option=com_wrapper&Itemid=29](https://www.tvfool.com/index.php?option=com_wrapper&Itemid=29)

TV Fool网站提供工具和信息，帮助用户确定他们可以接收到的地面无线（OTA）电视频道。该网站提供各种资源，包括电视信号定位器、在线电视地图、谷歌地球电视地图、呼号查询工具以及呼号列表。这些工具很可能利用位置数据来估计特定地址的信号强度和频道可用性。该网站还设有用户讨论论坛，并提供帮助部分，如信号分析常见问题解答和覆盖地图常见问题解答。该网站包含导航菜单（主菜单、工具）和链接到FM Fool、新闻、联系我们和网站反馈等部分。该页面还有一个通知，声明浏览器不支持内联框架，表明可能存在功能问题。最后，版权日期为2025年，这表明所提供的信息可能略有过时或是一种预测。

---

## 72. 超级计算机的西摩·克雷时代

**原文标题**: The Seymour Cray Era of Supercomputers

**原文链接**: [https://ztoz.blog/posts/cray-era-supercomputers/](https://ztoz.blog/posts/cray-era-supercomputers/)

本综述概述了《西摩·克雷的超级计算机时代：从快速机器到快速代码》一书，该书是一部关于从20世纪60年代到大规模并行处理兴起的超级计算机发展的技术和商业史。 该书记录了超级计算机的演变，重点介绍了CDC 6600和CRAY-1等关键型号，以及维持其性能优势的技术创新。 它还详细介绍了市场从政府和大学向航空航天和石油等行业的扩张，以及软件不断变化的角色，从用户编写的程序到供应商支持的操作系统、编译器和专用工具。 该综述强调了IBM尽管整体市场成功，但还是将性能桂冠输给了克雷的CDC 6600。 尽管赞扬了该书的技术深度和对市场变化的覆盖，但该综述批评了其缺乏对超级计算机设计中涉及的美学和个性的关注，认为这种遗漏忽略了它们文化影响和吸引力的一个关键方面。 审阅者最后建议将这本书推荐给那些对科学计算、计算机体系结构和高价值商业策略的历史感兴趣的人。

---

## 73. 图书管理员立即试图向你推销呜呜祖拉。

**原文标题**: The librarian immediately attempts to sell you a vuvuzela

**原文链接**: [https://kaveland.no/posts/2025-06-06-library](https://kaveland.no/posts/2025-06-06-library)

本文以图书馆里一位咄咄逼人的馆员强行推销呜呜祖拉为比喻，来说明搜索引擎质量因 SEO 垃圾信息和广告而下降。作者认为，现代搜索引擎就像这位爱管闲事的图书管理员一样，优先考虑经济利益，而不是提供相关和客观的搜索结果，就像“钢琴历史书籍”里充斥着广告而不是实际内容一样。

作者结合自己在技术支持方面的经验，强调了即使在知道特定信息存在的情况下，也越来越难以找到这些信息。他们展示了研究成果，表明搜索结果中联盟链接的普遍存在，并建议将搜索作为一项公共服务可以缓解这个问题，但也承认 SEO 操纵可能会持续存在。

文章接着对比了两种类型的搜索：检索已知内容和发现未知内容。文章发现，像 Claude 和 ChatGPT 这样的人工智能工具在发现方面更有效，因为它们能更好地理解意图，并且不太专注于销售产品。然而，作者对 LLM 提供商最终将如何将其服务货币化表示担忧，因为他们已经获得了巨额投资。他们推测人工智能有可能被用于操纵手段来产生收入，并将其与“呜呜祖拉馆员”相提并论。最后，作者考察了 OpenAI 等人工智能公司的财务状况，强调了巨额亏损，并质疑这些公司如何在不损害伦理考量或损害广大公众的情况下实现盈利。

---

## 74. 基于类型反射 vs. 基于值反射

**原文标题**: Type-based vs. Value-based Reflection

**原文链接**: [https://brevzin.github.io/c++/2025/06/09/reflection-ts/](https://brevzin.github.io/c++/2025/06/09/reflection-ts/)

本文深入探讨了 C++ 中基于类型和基于值的反射之间的差异，并以实现 `is_structural` trait（确定类型是否可以用作非类型模板参数）为例进行研究。作者认为，对新的基于值的反射语法的许多批评，源于不熟悉，而不是其固有的缺陷。

本文将 C++26 基于值的模型与反射技术规范 (TS) 中基于类型的模型进行了对比。TS 利用 `reflexpr(E)` 来产生代表 `E` 属性的唯一类型，以及一套用于查询这些类型和操作“对象序列”（反射对象的类型列表）的模板元函数。

作者演示了如何在提议的 C++26 基于值的反射设计之上实现反射 TS 的基本方面，利用了诸如 `^^E` 用于唯一实体表示和 `substitute` 用于创建专门的反射对象等特性。 他实现了关键的元函数，如 `get_element_t`、`get_enumerators_t`，并提供了 `get_name_v`，展示了它们如何在两种反射模型之间转换。

直接比较表明，两种模型中的操作之间存在一一对应的关系，强调了基于值的反射方法中的参数依赖查找和直接索引的优势。 最后，他讨论了 `get_base_classes_t` 和 `get_data_members_t` 的实现，展示了如何使用 `into_seq` 将反射范围转换为对象序列，这对于解决 `is_structural` 问题是必需的。

---

## 75. 我们正在秘密地赢得抗癌战争。

**原文标题**: We’re secretly winning the war on cancer

**原文链接**: [https://www.vox.com/health/415812/cancer-death-rates-myeloma-immunotherapy-smoking](https://www.vox.com/health/415812/cancer-death-rates-myeloma-immunotherapy-smoking)

布莱恩·沃尔什的文章《我们正在秘密赢得抗癌战争》认为，尽管癌症仍然是主要的健康威胁，但在对抗癌症方面已经取得了显著进展。 他着重介绍了乔恩·格卢克的案例，由于治疗技术的进步，他已患有多发性骨髓瘤超过20年。

该文章指出，自1991年以来，美国经年龄调整的癌症死亡率下降了约三分之一，从而减少了400多万例癌症死亡。 这一进展归功于三个关键的变革：禁烟政策、改进的筛查方法和突破性的治疗方法。 吸烟人数的下降大大降低了肺癌死亡率。 更好和更早的筛查，如结肠镜检查，已导致晚期结直肠癌的减少。 前沿的治疗方法，如自体干细胞采集、单克隆抗体和CAR-T疗法，大大提高了生存率，即使是对以前难以治疗的癌症，如多发性骨髓瘤。

具体而言，HPV疫苗已导致年轻女性宫颈癌死亡率显著下降，凸显了预防措施的影响。 CAR-T疗法，即利用患者自身的T细胞靶向癌细胞，已显示出显著效果，一些患者甚至实现了完全缓解。

文章虽然承认年轻人群中胃肠道癌症发病率上升等挑战，但仍保持乐观，强调癌症治疗的进步正在改善患者的未来。

---

## 76. Show HN: 作为 Minecraft 服务器的“课程”

**原文标题**: Show HN: A “Course” as an MCP Server

**原文链接**: [https://mastra.ai/course](https://mastra.ai/course)

马斯特拉大学推出实操课程“马斯特拉101”，教授用户如何使用马斯特拉平台构建和部署AI代理。该课程的独特之处在于完全在用户的代码编辑器中进行，由MCP（马斯特拉控制面板）代理引导。

该课程涵盖为代理配备工具、记忆和MCP功能。学习者将从头构建一个功能齐全的代理，使其能够与外部资源交互、利用自定义工具并记住之前的交互。

课程分为三个部分：构建第一个代理、添加工具和MCP以及添加记忆。第一部分介绍基本设置、代理测试和部署。第二部分重点介绍如何使用MCP服务器将代理连接到外部服务以及集成来自MCP注册表的工具。第三部分探讨添加记忆功能，如对话历史和语义回忆，以实现个性化响应。

要开始课程，用户可以选择他们喜欢的编辑器（Cursor、Windsurf或VSCode），然后粘贴提供的命令来安装MCP服务器。文章包含常见问题解答，解决在不同环境中设置MCP服务器时遇到的常见问题。该课程旨在提供互动和实用的学习体验，最终创建功能齐全的AI代理。

---

## 77. 我们所知的可观测性的终结（我感觉还好）

**原文标题**: It's the end of observability as we know it (and I feel fine)

**原文链接**: [https://www.honeycomb.io/blog/its-the-end-of-observability-as-we-know-it-and-i-feel-fine](https://www.honeycomb.io/blog/its-the-end-of-observability-as-we-know-it-and-i-feel-fine)

奥斯汀·帕克的文章《末日将至：可观测性的终结（而我感觉良好）》认为，大型语言模型（LLM）的兴起正在从根本上改变可观测性领域。他认为，LLM作为通用的函数逼近器，能够自动分析遥测数据，而这项任务以前需要人类专业知识和专用工具。

帕克通过一个演示说明了这一点：一个AI代理使用模型上下文协议（MCP）服务器成功识别了前端服务中延迟峰值的根本原因，这与人类使用传统可观测性工具所遵循的过程类似。这一过程成本低廉且设置简单。

他认为，LLM将使数据分析商品化，而OpenTelemetry将使工具化商品化，从而有效降低了现有专注于仪表板和易于工具化的可观测性工具的价值主张。帕克强调，在这个新时代成功的关键是快速反馈循环，他认为，由于人工智能快速生成和测试假设，速度至关重要。

Honeycomb强调快速反馈、协作知识共享和实验的方法，非常适合这种人工智能驱动的未来。帕克预测，在整个软件开发生命周期中，人工智能的辅助作用将会增强，从代码质量改进到自主软件工程师/站点可靠性工程师（SWE/SRE）的角色。最终，他得出结论，亚秒级查询性能、统一数据存储以及人机协作对于可观测性的未来至关重要。文章提倡拥抱人工智能的能力，以增强和加速开发和运营。

---

## 78. 信任链上的又一道裂痕：揭露（又一个）安全启动绕过

**原文标题**: Another Crack in the Chain of Trust: Uncovering (Yet Another) Secure Boot Bypass

**原文链接**: [https://www.binarly.io/blog/another-crack-in-the-chain-of-trust](https://www.binarly.io/blog/another-crack-in-the-chain-of-trust)

Binarly研究发现CVE-2025-3052，一个影响众多UEFI系统的安全启动绕过漏洞。该漏洞源于微软签名的第三方UEFI模块中的内存损坏问题，允许攻击者在启动过程中运行未签名代码并绕过安全启动。漏洞存在于对NVRAM变量（特别是`IhisiParamBuffer`）的不安全处理中，易受攻击的模块将其用作内存写入的指针，但没有进行适当的验证。

攻击者可以将`IhisiParamBuffer`设置为任意内存地址，从而获得任意内存写入能力。在他们的概念验证中，Binarly覆盖了指向Security2 Architectural Protocol的指针，有效地禁用了安全启动并允许执行未签名模块。

该漏洞是在DT Research设备的BIOS刷新工具中发现的，但会影响任何信任“Microsoft Corporation UEFI CA 2011”证书的系统。微软通过在其2025年6月补丁星期二发布中向安全启动dbx添加14个新哈希值来解决此问题，影响了14个不同的模块。

本文强调了安全启动绕过漏洞的持久性以及UEFI供应链安全的复杂性。Binarly强调保持dbx更新的重要性，并演示了他们的透明平台如何检测和报告此类漏洞，包括此0-day漏洞。该平台主动识别DB/DBX数据库中易受攻击的签名模块，以突出潜在的高影响力风险。

---

## 79. 法兰克福厨房

**原文标题**: The “Frankfurt Kitchen”

**原文链接**: [https://museumderdinge.org/programme/exhibitions/the-frankfurt-kitchen/](https://museumderdinge.org/programme/exhibitions/the-frankfurt-kitchen/)

1926年玛格丽特·舒特-利霍茨基设计的“法兰克福厨房”代表了建筑和文化史上的一个关键时刻，它将工业理性化引入家庭领域。它受恩斯特·梅委托为“新法兰克福”住房计划设计，旨在通过为下层阶级提供廉价、高效且配备现代设施的住房来解决一战后的住房短缺问题。

厨房的模块化设计实现了批量生产并降低了成本。它被广泛推销，成为现代整体厨房的原型，尽管其设计随着时间的推移而不断演变。它以铁路餐车厨房为模型，将效率和功能放在首位，作为一个与起居区分离的“烹饪工作室”。

Werkbundarchiv – 物件博物馆展出了一间来自罗马城庄园的法兰克福厨房，展示了其原始特征和使用痕迹。该厨房体现了1920年代的关键原则：客观性、功能主义和标准化，反映了包豪斯和德意志制造联盟旨在通过统一设计消除阶级差异的目标。

“法兰克福厨房”是“新生活”运动的一部分，该运动摒弃了历史元素，转而追求“计划秩序”。然而，它的功能主义和性别分工后来受到了批评。博物馆展览包括历史照片、电影、舒特-利霍茨基的采访以及阿斯特里德·德布斯-斯坦伯格和约阿希姆·克劳斯的调查研究结果，探讨了厨房的概念及其在“新法兰克福”中的现实。

---

## 80. 展示一下：我做了个3D打印的垂直起降无人机

**原文标题**: Show HN: I made a 3D printed VTOL drone

**原文链接**: [https://www.tsungxu.com/p/i-made-a-3d-printed-vtol-that-can](https://www.tsungxu.com/p/i-made-a-3d-printed-vtol-that-can)

徐聪创造了一架3D打印垂直起降无人机，能够飞行130英里，而他仅用了90天就完成了这一壮举，尽管他之前在CAD、3D打印或空气动力学方面经验有限。这架无人机单次充电可飞行3小时，有可能成为全球续航里程和耐力最长的3D打印垂直起降无人机之一。

徐之前只建造和飞行过一架垂直起降飞机，并且只有基本的CAD技能，但他学会了设计、打印和优化无人机性能所需的一切知识。他使用了一台Bambu A1 3D打印机，并探索了诸如发泡PLA打印等技术。里德·霍夫曼称赞该项目，将其与莱特兄弟的开创性工作相提并论。

展示这架无人机的YouTube视频很简洁，徐承认它没有涵盖项目挑战的全部范围，包括设计参数选择、CAD设计学习、组件采购、打印质量改进和功率损耗故障排除。他鼓励有兴趣了解更多关于他的设计和建造过程的观众表达他们的兴趣。徐还在努力建造一架供个人使用的电动垂直起降飞机，并鼓励读者关注他的进展。

---

## 81. 机构图书：来自哈佛图书馆馆藏的242B tokens数据集

**原文标题**: Institutional Books: A 242B token dataset from Harvard Library's collections

**原文链接**: [https://arxiv.org/abs/2506.08300](https://arxiv.org/abs/2506.08300)

本 arXiv 提交介绍 Institutional Books 1.0，这是一个大型公共数据集，源自哈佛图书馆的数字化图书藏品。该数据集包含来自 983,004 册公共领域图书的 2420 亿个词元，这些图书最初是 2006 年开始的 Google 图书项目的一部分。作者强调了高质量训练数据对于大型语言模型（LLM）的重要性，并解决了此类资源的稀缺问题。

该报告详细介绍了从哈佛图书馆提取、分析和处理超过一百万册图书（最初为 250 多个语种的 1,075,899 册图书，共计 2500 亿个词元）的过程，形成了一个记录详尽的历史文本数据集。发布的数据集包括 OCR 提取的文本（原始文本和后处理文本）以及全面的元数据。作者概述了该项目的目标、方法和分析结果，旨在使这个重要的历史馆藏对人类和机器都更易于访问和使用。其目的是方便数据的过滤、阅读和利用。该提交还提供了相关研究工具、代码仓库和交互式演示的链接。

---

## 82. 迪尔公司必须面对联邦贸易委员会关于维修成本的反垄断诉讼，美国法官裁定。

**原文标题**: Deere Must Face FTC's Antitrust Lawsuit over Repair Costs, US Judge Rules

**原文链接**: [https://www.reuters.com/legal/government/deere-must-face-ftcs-antitrust-lawsuit-over-repair-costs-us-judge-rules-2025-06-10/](https://www.reuters.com/legal/government/deere-must-face-ftcs-antitrust-lawsuit-over-repair-costs-us-judge-rules-2025-06-10/)

约翰迪尔公司(Deere & Company, John Deere) 必须面对联邦贸易委员会(FTC)提起的反垄断诉讼，该诉讼指控该公司垄断了其农业设备的维修市场。美国法官裁定，联邦贸易委员会声称，约翰迪尔非法限制了独立维修店修理约翰迪尔设备所需的零部件和软件的获取，迫使农民依赖约翰迪尔的授权经销商，导致更高的维修成本和更长的停机时间。

该诉讼的重点是约翰迪尔拒绝向独立维修店提供执行某些维修所需的软件和诊断工具，这实际上使约翰迪尔经销商垄断了这些服务。据称，对维修市场的这种控制不仅抬高了价格，而且使那些喜欢使用当地独立机械师的农民处于不利地位。

约翰迪尔曾试图驳回该诉讼，辩称其有权控制对其专有软件的访问，并且允许独立维修会损害安全和知识产权。然而，法官驳回了这些论点，认为联邦贸易委员会提供了足够的证据表明约翰迪尔的做法具有反竞争性。该裁决允许联邦贸易委员会继续推进此案，这可能会迫使约翰迪尔改变其维修政策，并允许独立维修店更大程度地获取维修约翰迪尔设备所需的工具和软件。此案是“维修权”运动的关键组成部分，该运动倡导消费者对自身产品的维修拥有更大的控制权。

---

## 83. 更快速、更便捷的2D矢量渲染 [视频]

**原文标题**: Faster, easier 2D vector rendering [video]

**原文链接**: [https://www.youtube.com/watch?v=_sv8K190Zps](https://www.youtube.com/watch?v=_sv8K190Zps)

YouTube视频，标题为“更快、更简单的2D矢量渲染”，可能讨论了2D矢量图形渲染方面的进步，使其过程更快和/或更简单。然而，所提供的内容主要包含标准的YouTube页脚链接和免责声明。这包括版权、联系信息、创作者、广告、开发者、条款、隐私、安全、YouTube运作方式以及新功能测试等部分的链接。它还包括关于NFL Sunday Ticket的通知，表明可能存在与NFL相关的联系或赞助。

由于没有实际内容描述2D矢量渲染的进步，因此无法总结关键技术点。唯一可能的结论是，提供的描述缺少视频的实际内容，而只是包含样板式的YouTube信息。

---

## 84. 画完伦敦每家酒吧的画像需要多久？

**原文标题**: How Long Does It Take to Draw a Picture of Every Pub in London?

**原文链接**: [https://www.nytimes.com/2025/06/10/world/europe/artist-pub-london-wood.html](https://www.nytimes.com/2025/06/10/world/europe/artist-pub-london-wood.html)

无法访问文章链接。

---

## 85. Show HN: 本可能发生的罗马工业革命

**原文标题**: Show HN: The Roman Industrial Revolution that could have been

**原文链接**: [https://thelydianstone.com/](https://thelydianstone.com/)

这个“Show HN”帖子介绍《吕底亚石系列》漫画项目，该项目探索了一个架空历史，其中古罗马经历了由现代知识驱动的工业革命。 该漫画使用AI图像生成技术创作，并刻意保留了一些瑕疵，以突出该项目的实验性质。

该系列讲述了考古学学生尤利西斯通过一个连接时空的文物与罗马奴隶马库斯建立联系的故事。 尤利西斯向马库斯提供了现代知识，使他能够开发蒸汽动力等技术，从而彻底改变了罗马社会。

第一期重点讲述了他们的初次接触，尤利西斯面临着干预历史以拯救马库斯免受维苏威火山爆发的伦理困境。 第二期讲述了马库斯利用蒸汽动力在灾难后振兴坎帕尼亚地区的故事，创造了自动化羊毛编织机和蒸汽动力船。 第三期探讨了坎帕尼亚经济成功带来的后果，导致与罗马的冲突，尤其是他们对奴隶制的立场。 面对皇帝的压迫，尤利西斯不情愿地引入了火药，加剧了社会动荡的可能性。 该系列探讨了友谊、创造力、意想不到的后果以及传统与进步之间的张力等主题。

---

## 86. 苹果发布Foundation Models和容器化框架等

**原文标题**: Apple announces Foundation Models and Containerization frameworks, etc

**原文链接**: [https://www.apple.com/newsroom/2025/06/apple-supercharges-its-tools-and-technologies-for-developers/](https://www.apple.com/newsroom/2025/06/apple-supercharges-its-tools-and-technologies-for-developers/)

苹果公司 2025 年 6 月 9 日的新闻稿重点介绍了为开发者打造更具吸引力和智能化的跨 Apple 平台应用体验的新技术和增强功能。

一项关键公告是 **Foundation Models 框架**，使开发者能够集成设备端的 Apple Intelligence 以实现以隐私为中心的 AI 推理，可通过 Swift 以最少的代码进行访问。Automattic 的 Day One 应用已经在使用它。

**Xcode 26** 现在利用 ChatGPT 等大型语言模型进行代码生成、测试和文档编写，具有内置支持，并且可以选择使用其他提供商或本地模型。编码工具提供建议的操作和内联提示处理，以提高生产力。

一种采用“Liquid Glass”设计的新型通用软件设计在 Apple 的操作系统中提供了具有视觉吸引力且熟悉的审美。**Icon Composer** 应用使开发者能够创建引人入胜的应用图标。

**App Intents** 获得了对视觉智能的支持，允许像 Etsy 这样的应用将视觉搜索结果直接集成到用户体验中。Swift 6.2 增强了性能、并发性和互操作性，包括 WebAssembly 支持。

**Containerization 框架** 使开发者能够直接在 Mac 上创建、下载和运行 Linux 容器镜像。

对于游戏开发者来说，**Game Porting Toolkit 3** 提供了更新的评估和分析工具。专为 Apple 芯片设计的 **Metal 4** 引入了先进的图形和机器学习技术。**Apple Games 应用**集中管理游戏和好友，引入了挑战赛以进行竞争，并通过 Game Overlay 增强了互动。Managed Background Assets 简化了资源托管，并提供免费的 Apple 托管。

帮助保护儿童在线安全的工具包括 Declared Age Range API。

最后，App Store 上的 **Accessibility Nutrition Labels** 提供了关于应用辅助功能的信息，而 App Store Connect 收到了 TestFlight 反馈和 API 增强功能的更新。Apple Intelligence 功能需要支持的设备和特定的语言设置。

---

## 87. 现代极简完美哈希：综述

**原文标题**: Modern Minimal Perfect Hashing: A Survey

**原文链接**: [https://arxiv.org/abs/2506.06536](https://arxiv.org/abs/2506.06536)

Lehmann等人撰写的arXiv预印本“现代最小完美哈希：综述”概述了完美哈希技术的最新进展。完美哈希函数将一组*n*个键映射到前*m*个整数（其中*m* ≥ *n*），且不发生冲突；当*m* = *n*时，该哈希函数是最小的。本文重点介绍了空间消耗、构建时间和查询时间之间的权衡，这些都是关键的关注参数。

摘要强调，自1997年上次全面调查以来，已经取得了重大进展，使得完美哈希函数能够实现极快的查询时间和高空间效率，同时可以扩展到数十亿个键。一些构造方法实现了接近理论下限的空间消耗。

本综述旨在为那些想要了解现代完美哈希的人提供一个起点，并包含广泛的实验评估，以帮助为各种应用程序选择合适的哈希函数。本文重点介绍静态键集，这些键集通常用于数据库、生物信息学和字符串学中，在这些领域中，它们可用于避免哈希表中的冲突解决。

---

## 88. 引入对systemd更强的依赖

**原文标题**: Introducing stronger dependencies on systemd

**原文链接**: [https://blogs.gnome.org/adrianvovk/2025/06/10/gnome-systemd-dependencies/](https://blogs.gnome.org/adrianvovk/2025/06/10/gnome-systemd-dependencies/)

GNOME计划加强对systemd的依赖，影响未使用systemd的发行版

本文宣布GNOME计划加强其对systemd的依赖，这将影响未使用systemd的发行版。虽然GNOME已经依赖于`logind`，但此举将使在BSD等非systemd环境中运行GNOME变得更加困难。

更改包括：

*   **GDM（GNOME Display Manager）：** 将依赖于systemd的`userdb`基础设施来实现多席位和远程登录支持，用动态用户分配取代旧的 hack 方法。 计划最终放弃 AccountsService，转而使用`userdb`。
*   **gnome-session：** 将放弃其内置的服务管理器，完全依赖 systemd 来管理 GNOME 会话服务。 此旧代码已过时，并且阻碍了会话保存/恢复等功能。

对于没有 systemd 的发行版，作者建议：

*   **考虑切换到 systemd。**
*   **实现 systemd 组件的替代品：** 类似于`elogind`和`eudev`。
*   **利用临时的 GDM 备用代码路径：** GDM 将查找并使用 gdm-greeter 用户作为其产生的第一个登录屏幕，gdm-greeter-2 作为第二个，依此类推，gdm-greeter-N 作为第 N 个。
*   **为 userdb Varlink API 实现必要的基础设施：** 至少包括：systemd-userdbd 的 io.systemd.Multiplexer 的实现；通过 userdb API 公开 NSS 定义的用户的桥接器；通过你的 libc 的原生用户查找 API 公开 userdb 定义的用户的桥接器。

GDM 提供了一个临时的备用代码路径，使用静态分配的 `gdm-greeter` 用户。发行版需要用自己的管理器替换 `gnome-session` 的服务管理器，包括替换单元文件、会话领导进程和 `gnome-session-ctl` 辅助程序。

作者承认时间很短，并建议在无法快速实现更改的情况下，使用 GNOME 48 的错误修复程序，直到 GNOME 50。 运行带有 gnome-session 48 的 GNOME 49 可能会争取更多时间，但这不是受支持的配置。

---

## 89. 特朗普“宏伟”法案上，白宫与经济学家之间 11 万亿美元的差距

**原文标题**: The $11T gap between White House and economists on Trump's 'big, beautiful' bill

**原文链接**: [https://finance.yahoo.com/news/the-11-trillion-gap-between-white-house-and-economists-on-trumps-big-beautiful-bill-080017492.html](https://finance.yahoo.com/news/the-11-trillion-gap-between-white-house-and-economists-on-trumps-big-beautiful-bill-080017492.html)

2025年6月雅虎财经文章：特朗普总统时期白宫与经济专家就其标志性法案财政影响存在重大分歧。

包括国会预算办公室、税务基金会和宾夕法尼亚大学沃顿预算模型在内的经济学家估计，该法案将在未来十年内使国家债务增加约3万亿美元。 然而，白宫声称该法案将产生收入，可能高达8万亿美元，从而减少赤字。 这代表着预测中存在11万亿美元的差异。

经济学家批评白宫的乐观预测，理由是关于持续3%经济增长的不切实际的假设、内部矛盾的会计操作以及有选择地使用经济数据，尤其是在关税的影响方面。 他们认为，即使将关税因素考虑在内并使用更为保守的增长估计，该法案的财政影响也只会是中性甚至负面。 财政部长贝森特在国会作证时进一步暴露了白宫主张缺乏独立支持的问题，因为他唯一引用的专家是特朗普的长期支持者。

该文章强调了人们对政府经济预测的怀疑，以及对与主流经济预测存在显著差异的假设的依赖。 关税的未来及其潜在的减少进一步模糊了白宫计算的准确性。

---

## 90. Show HN: 高端色彩量化器

**原文标题**: Show HN: High End Color Quantizer

**原文链接**: [https://github.com/big-nacho/patolette](https://github.com/big-nacho/patolette)

Patolette 是一个用于高端颜色量化和抖动的 C/Python 库，实现了基于加权的 PCA 量化器（Xiaolin Wu 算法的变体）。它具有避免轴对齐细分、支持 CIEL*u*v* 和 ICtCp 色彩空间、可选的显著性图权重（用于视觉上突出的区域）以及可选的 KMeans 优化等特性。虽然尚未达到生产级别，但已具备可用性。

提供了 Linux (Debian)、macOS 和 Windows 的安装说明，依赖项包括 OpenBLAS 和 FLANN。值得注意的是，x86 用户可以利用 AVX 指令集来提高 KMeans 的性能。Windows 用户可能会遇到 .dll 问题，需要使用 delvewheel 进行修复。

基本用法演示了使用 Pillow 进行量化，包括色彩空间选择（CIEL*u*v*、sRGB、ICtCp）和显著性加权的瓦片大小调整。CIEL*u*v* 在低颜色计数时表现出色，sRGB 色彩平滑，而 ICtCp 提供了良好的折衷方案。较小的瓦片尺寸会增强显著性效果。

注意事项包括高内存使用率（v1 版本的首要目标是降低内存使用）、与更简单的方法相比速度较慢、不完整的 C API 以及缺乏 RGBA 支持。该库感谢其对 Xiaolin Wu 的颜色量化、Jianming Zhang 的显著性检测、Riemersma Dithering、faiss、flann 和 OpenBLAS 等各种工作的依赖。

---

## 91. IBM 正发布其首个具备抗错性的量子计算系统

**原文标题**: IBM now describing its first error-resistant quantum compute system

**原文链接**: [https://arstechnica.com/science/2025/06/ibm-is-now-detailing-what-its-first-quantum-compute-system-will-look-like/](https://arstechnica.com/science/2025/06/ibm-is-now-detailing-what-its-first-quantum-compute-system-will-look-like/)

IBM宣布了其构建“Starling”的路线图，这是一个预计于2029年推出的量子计算系统，能够在200个逻辑量子比特上执行1亿次无错运算，且无法用经典方法建模。这标志着从关注单个量子比特转向功能计算单元，将纠错视为一个工程问题，而不仅仅是科学问题。

关键的中间步骤包括开发配置为容纳纠错量子比特的处理器。这包括展示高连接性和远程耦合器的“Loon”处理器，以及将计算开销降至最低的、具有最小串扰的方形阵列“Nighthawk”处理器。

IBM正在采用低密度奇偶校验(LDPC)纠错码，特别是“二元自行车码”。实施方案包括排列144或288个硬件量子比特来容纳12个逻辑量子比特，提供不同的纠错距离。这些正在像Kookaburra（稳定的量子存储器）和Cockatoo（可以连接处理单元的功能计算单元）这样的处理器上实现。

一个关键组件包括运行消息传递解码器的经典硬件，以实时评估综合征数据进行纠错，利用FPGA来提高速度。IBM表示，整体架构将涉及通过“通用桥”连接的互连稀释制冷机。虽然Starling是一个重要的进步，但IBM承认，像Blue Jay（2033年）这样拥有2000个逻辑量子比特的系统将需要用于更复杂的算法，例如破解加密。该公司认为，错误率已经足够好，可以开始所需的工程设计。

---

## 92. 他们周游世界，死里逃生，只为收集车牌

**原文标题**: They Travel the World–and Cheat Death–For License Plates

**原文链接**: [https://www.wsj.com/lifestyle/license-plate-collectors-cars-21c7506e](https://www.wsj.com/lifestyle/license-plate-collectors-cars-21c7506e)

华尔街日报文章《他们周游世界——并与死神擦肩——只为收集车牌》详细介绍了收集车牌这一小众且有时充满危险的爱好。文章聚焦于一群执着的收藏家，他们周游世界，常常前往偏远和政治不稳定的地区，以寻求稀有和不寻常的车牌。

追求这些车牌可能充满挑战，从与腐败官员打交道、穿越危险地形，到冒着被逮捕甚至绑架的风险。收藏家通常寻找来自特定地区、年份或具有特定特征的车牌，这使得追寻过程变成一个复杂的谜题，涉及研究、谈判和冒险意愿。

文章强调，驱动这些收藏家的不仅仅是对车牌的热爱；还包括追逐的刺激、车牌的历史意义以及社群的友谊。他们分享技巧、交易车牌，并在冒险活动中互相支持。车牌本身被视为历史文物，反映了其来源国家或地区的政治、经济和文化背景。

虽然一些收藏家专注于特定国家或车牌类型，但另一些收藏家的目标是收集来自世界各地所有辖区的车牌。这种雄心通常需要大量的资金投入和对该爱好的深入投入，使其成为少数人的专属追求。文章描绘了一个充满激情的社群，他们愿意不遗余力地扩展他们的收藏，突出了车牌收藏这个独特且常常充满危险的世界。

---

## 93. Sosumi与Mac启动声音的故事

**原文标题**: Story of Sosumi and the Mac Startup Sound

**原文链接**: [https://reekes.net/sosumi-story-mac-startup-sound/](https://reekes.net/sosumi-story-mac-startup-sound/)

吉姆·里克斯撰写的这篇文章揭示了苹果公司一些最具标志性声音背后的故事，包括“Sosumi”提示音、Mac启动声音和iPhone相机声音。

里克斯消除了围绕“Sosumi”提示音的种种传言，解释说它起源于商标纠纷，本意是一个有趣的内部笑话。 他透露，Mac启动声音的灵感来自披头士乐队的《A Day In The Life》的结尾和弦。 他强调了Sosumi声音最终成为苹果商标的讽刺意味。

这篇文章还详细介绍了iPhone相机声音的创作过程，这是里克斯的佳能AE-1相机的录音。 与传言相反，该声音并非由于动力卷片器问题。 他还分享说，后来他将这台相机捐赠给了Goodwill。

这篇文章链接到关于里克斯在苹果公司工作的各种采访和文章，展示了人们对这些声音的持久兴趣。 这些链接涵盖了Mac启动声音的演变、“Sosumi”神话以及Mac系统声音的历史。 最后，这些文章集锦突出了Mac声音如何在流行文化中得到认可和使用，甚至被注册为商标并混音成音乐。

---

## 94. 风干木材 vs. 窑干木材

**原文标题**: Air-dried vs. Kiln-dried Wood

**原文链接**: [https://christopherschwarz.substack.com/p/air-dried-vs-kiln-dried-wood](https://christopherschwarz.substack.com/p/air-dried-vs-kiln-dried-wood)

好的，我将阅读并总结来自所提供URL的文章《风干木材 vs. 窑干木材》。

**摘要：**

克里斯托弗·施瓦茨的文章比较了风干木材和窑干木材，重点介绍了它们的差异以及各自的优势。他认为，虽然窑干木材应用广泛并被认为是标准，但风干木材通常为手工工具使用者提供更优越的可加工性、稳定性和整体质量。

窑干法快速降低木材的含水量，通常会导致表面硬化（硬的外层和较软的芯）和内部应力，这些应力可能导致后续的翘曲和移动。这使得木材更难使用手工工具进行加工。窑干法还可以有效地杀死任何存在的昆虫。

另一方面，风干是一种更慢、更渐进的过程。这种较慢的干燥速度使得木材更加稳定且应力更小。因此，木材通常更容易加工，并且对木工手工具的反应更好。缺点是风干木材仍然可能含有需要处理的昆虫。

施瓦茨总结说，虽然窑干木材因其可及性和杀虫特性而有用，但风干木材通常为木工，尤其是使用手工工具的木工，提供更好的体验，因为它具有卓越的可加工性和降低的内部应力。他承认获得风干木材的难度，但建议尽可能寻找风干木材，尤其是对于家具制作和要求苛刻的项目。最终，他建议木工们了解每种木材的特性，并根据他们的特定需求和项目要求选择最佳方案。

---

## 95. 温柔奇点

**原文标题**: The Gentle Singularity

**原文链接**: [https://blog.samaltman.com/the-gentle-singularity](https://blog.samaltman.com/the-gentle-singularity)

《温柔的奇点》一文探讨了向数字超智能时代的持续过渡，认为尽管其到来可能不如预期般激进，但它将深刻地重塑人类生活。作者提出，像GPT-4这样的系统标志着人工智能能力的重大飞跃，能够极大地提高人类的生产力和科学进步，从而提高生活质量。

虽然机器人并不普及，许多全球问题依然存在，但人工智能的影响是不可否认的。作者强调了ChatGPT的广泛应用及其对正面和负面影响的潜力。对近期的预测包括能够进行真正认知工作的人工智能代理，影响软件开发，并有可能推动科学突破和机器人技术进步。

文章表明，尽管基本的人类体验将继续存在，但2030年代将见证由于充沛的智能和能源而发生的巨大转变。奇迹将成为常态，科学生产力将加速，人工智能将促进进一步的人工智能研究。像自动化机器人生产这样的自我强化循环将进一步推动进步，将智能的成本降低到接近电力的成本。

尽管存在失业的潜在可能性，但作者乐观地认为，社会财富将促成新的政策方法。他认为，关键挑战是将人工智能与集体人类价值观相协调，并确保广泛获得超智能。文章最后强调了发起关于人工智能对齐的全球对话的重要性，并倡导一个智能廉价且广泛可用的未来，从而迎来一个前所未有的创新和社会进步时代。

---

## 96. 印度航空B788型客机2025年6月12日在艾哈迈达巴德起飞后不久失高

**原文标题**: Air India B788 at Ahmedabad on Jun 12th 2025, lost height shortly after takeoff

**原文链接**: [https://avherald.com/h?article=528f27ec&opt=0](https://avherald.com/h?article=528f27ec&opt=0)

好的，我已阅读了航空先驱报关于印度航空AI-116航班（一架波音787-8型客机）的报道，该航班于2025年6月12日从印度艾哈迈达巴德起飞后不久发生高度损失。

以下是摘要：

2025年6月12日，印度航空AI-116航班（注册号VT-ANE的波音787-8型客机）从印度艾哈迈达巴德（AMD）飞往伦敦希思罗机场（LHR），从23号跑道起飞后不久发生了一起事件。飞机起飞后，最初爬升至离地约800英尺的高度，但随后下降至离地约500英尺的高度，然后恢复并继续爬升。

由于对飞机性能的担忧，机组人员在FL250高度停止了爬升。在古吉拉特邦和拉贾斯坦邦上空消耗燃油后，机组人员决定返回艾哈迈达巴德，并在起飞后约75分钟安全降落在23号跑道上。

事件发生后，该飞机已停止运营进行检查。印度民航总局（DGCA）已对此次事件展开调查。初步报告表明，机组人员可能错误配置了飞行管理系统（FMS），导致了不正确的VNAV（垂直导航）引导。这种配置问题可能导致自动驾驶仪在起飞后不久发出下降指令，从而导致观察到的高度损失。

---

## 97. 在球体表面动画网格

**原文标题**: Animate a mesh across a sphere's surface

**原文链接**: [https://garden.bradwoods.io/notes/javascript/three-js/animate-a-mesh-on-a-spheres-surface](https://garden.bradwoods.io/notes/javascript/three-js/animate-a-mesh-on-a-spheres-surface)

本文介绍了如何使用 Three.js 和 GSAP 实现 3D 网格沿球面运动的动画效果。文章涵盖了以下几个关键步骤：

1.  **定义位置：** 使用经纬度坐标指定球面上的点，并通过 `latLongToVector3` 函数将其转换为 3D 坐标。
2.  **创建路径：** 使用 `calcPathPoints` 函数计算球面上起点和终点之间的一系列点。这些点形成一个大圆弧，即球面上的最短路径。文章还介绍了如何使用 `createPath` 函数用线条直观地表示此路径。
3.  **GSAP 动画：** 一个网格（用盒子表示）沿着计算出的路径进行动画。它使用 `THREE.CatmullRomCurve3` 基于路径点创建平滑的样条曲线。GSAP 用于插值一个从 0 到 1 的值 't'，该值决定了网格在任何给定时间沿样条曲线的位置。
4.  **几何体原点调整：** 文章解决了网格原点位于其中心，导致其穿过球体而不是位于球体表面上的问题。`setOriginYBottom` 函数用于移动网格的几何体，确保其正确地位于表面上。
5.  **网格旋转：** 文章强调了在网格移动时正确调整其方向的重要性。`calcMeshQuaterionAlongPath` 函数计算一个四元数，用于旋转网格，使其面向运动方向（沿样条曲线的切线）并相对于球体表面保持直立。文章提供了这些函数的代码。

---

## 98. 詹姆斯·弗洛里奥将帕特里克·多尔蒂的雕塑变成了杰出的摄影作品

**原文标题**: James Florio Turned Patrick Dougherty's Sculptures into Stellar Photography

**原文链接**: [https://aboutphotography.blog/blog/behind-the-scenes-with-phil-penman-the-making-of-new-york-street-diaries-book-spotlight](https://aboutphotography.blog/blog/behind-the-scenes-with-phil-penman-the-making-of-new-york-street-diaries-book-spotlight)

本文聚焦菲尔·彭曼的摄影集《纽约街头日记》，该书记录了新冠疫情期间和一场重大暴风雪下的纽约市。在一次采访中，彭曼讨论了这本书背后的灵感，它与他之前作品（专注于名人摄影和充满活力的纽约生活的《街头》）的对比，以及捕捉这座城市在空前时期的荒凉和韧性所带来的情感冲击。

彭曼详细描述了拍摄空旷街道的经历，他对黑白影像的偏爱（最初是出于实际印刷的考虑，但最终与他的艺术愿景相符），以及他希望这本书能够成为一份准确的历史记录。他对这本书获得的积极反响，包括其被美国国会图书馆收藏，感到震惊和感激。

本文还探讨了彭曼的摄影技巧，强调持续学习和适应，并提到了他对萨尔加多、电影制作人和艺术家等的影响。他建议有抱负的街头摄影师享受旅程，不要因偶尔的挫折而气馁。最后，彭曼暗示了未来涉及彩色摄影的项目。文章末尾提供了一个链接，读者可以在那里购买《纽约街头日记》。

---

## 99. 《无尽的玩笑》中可疑的数学 (2009)

**原文标题**: Dubious Math in Infinite Jest (2009)

**原文链接**: [https://www.thehowlingfantods.com/dfw/dubious-math-in-infinite-jest.html](https://www.thehowlingfantods.com/dfw/dubious-math-in-infinite-jest.html)

迈克·斯特朗，一位大卫·福斯特·华莱士的粉丝，在“嚎叫的幽灵”博客上考察了《无尽的玩笑》中的数学错误。受华莱士在文章《龙卷风带中的衍生运动》中所展现的数学天赋以及一篇关于数学小说的评论的启发，斯特朗记录了四个“可疑的数学”实例。

第一个错误，归因于叙述者，涉及一场108局网球比赛以54-54平局结束的几率。叙述者声称几率为 1/2^27，但斯特朗认为实际概率要高得多，约为 0.0766，这是使用组合数学和概率原理计算得出的。他用一个较小的、可枚举的 4 局比赛的例子来说明这一点。

第二个错误出现在一个脚注中，其中迈克·佩姆利斯描述了在末世论中使用积分中值定理。斯特朗指出，虽然佩姆利斯对该定理的描述是正确的，但该定理本身只证明了值的 *存在*，而不是如何 *找到* 它，这使得它在佩姆利斯计算中的实际应用值得怀疑。还注意到一个小的、可能是印刷上的错误：定理陈述中缺少积分符号。

最后一个错误，再次归因于佩姆利斯在与哈尔的大学委员会考试准备课程中，涉及 x^n 的导数。佩姆利斯错误地将其表述为 nx + x^(n-1)，而正确的公式是 nx^(n-1)。

斯特朗最后表示，他对华莱士为何包含这些错误没有任何理论，并邀请读者分享他们的想法。他承认有些错误可能是印刷错误。

---

## 100. 容器化：在 macOS 上运行 Linux 容器的 Swift 包

**原文标题**: Containerization is a Swift package for running Linux containers on macOS

**原文链接**: [https://github.com/apple/containerization](https://github.com/apple/containerization)

容器化：一个使用Apple Virtualization.framework在macOS上运行Linux容器的Swift包。它提供用于管理OCI镜像、与注册中心交互、创建ext4文件系统、使用Netlink套接字、构建优化Linux内核、管理轻量级VM和运行容器化进程（包括使用Rosetta 2 for amd64）的API。

该软件包设计为在各自的VM中执行每个容器，允许专用IP地址。它强调亚秒级启动时间，使用由`vminitd`管理的最小内核和根文件系统，`vminitd`是一个子项目，提供GRPC API用于配置运行时环境和启动进程。

构建容器化需要一台Apple silicon Mac、macOS 15（推荐macOS 26 beta）和Xcode 26 beta。非隔离容器网络等关键功能在macOS 15中受到限制。包含的`cctl`可执行文件提供了使用API的示例。

该软件包包含一个最小的、优化的Linux内核配置和构建环境，同时也提供了在每个容器上使用自定义内核的API。可以使用预构建的、带有VIRTIO驱动程序的内核（如来自Kata Containers的内核）。

构建、测试和生成文档通过`make`命令完成。欢迎贡献。0.1.0版本是第一个正式版本，源代码稳定性仅在次要版本内保证。

---

