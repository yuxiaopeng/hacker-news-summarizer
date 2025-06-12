# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-06-12.md)

*最后自动更新时间: 2025-06-12 17:52:39*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 2 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 3 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 4 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 5 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 6 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 7 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 8 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 9 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 10 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 11 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 12 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 13 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 14 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 15 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 16 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 17 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 18 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 19 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 20 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 21 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 22 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 23 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 24 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 25 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 26 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 27 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 28 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 29 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 30 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 31 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 32 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 33 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 34 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 35 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 36 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 37 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 38 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 39 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 40 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 41 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 42 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 43 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 44 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 45 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 46 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 47 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 48 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 49 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 50 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 51 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 52 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 53 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 54 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 55 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 56 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 57 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 58 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 59 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 60 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 61 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 62 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 63 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 64 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 65 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 66 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 67 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 68 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 69 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 70 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 71 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 72 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 73 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 74 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 75 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 76 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 77 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 78 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 79 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 80 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 81 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 82 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 83 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 84 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 85 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
