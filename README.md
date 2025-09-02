# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-09-02.md)

*最后自动更新时间: 2025-09-02 17:46:24*
## 1. 静态网站提供良好的时间旅行体验。

**原文标题**: Static sites enable a good time travel experience

**原文链接**: [https://hamatti.org/posts/static-sites-enable-a-good-time-travel-experience/](https://hamatti.org/posts/static-sites-enable-a-good-time-travel-experience/)

无法访问文章链接。

---

## 2. Anthropic 完成 130 亿美元 F 轮融资，投后估值达 1830 亿美元

**原文标题**: Anthropic raises $13B Series F at $183B post-money valuation

**原文链接**: [https://www.anthropic.com/news/anthropic-raises-series-f-at-usd183b-post-money-valuation](https://www.anthropic.com/news/anthropic-raises-series-f-at-usd183b-post-money-valuation)

Anthropic 获得 130 亿美元 F 轮融资，投后估值达 1830 亿美元。本轮融资由 ICONIQ 领投，富达管理研究公司和光速创投共同领投。该投资反映了对 Anthropic 作为领先 AI 平台地位的信心。

重要投资者包括 Altimeter、Baillie Gifford、BlackRock 关联基金、Blackstone、Coatue、D1 Capital Partners、General Atlantic、General Catalyst、GIC、高盛另类投资的成长股权部门、Insight Partners、Jane Street、安大略教师退休金计划、卡塔尔投资局、TPG、普信集团、普信投资管理公司、WCM Investment Management 和 XN。

自 2023 年 3 月推出 Claude 以来，Anthropic 经历了快速增长。到 2025 年初，年化收入达到 10 亿美元，到 2025 年 8 月飙升至超过 50 亿美元。该公司为超过 30 万家企业客户提供服务，大型客户（> 10 万美元年化收入）显著增加。

增长涵盖 Anthropic 的平台，包括面向企业的 API 和行业特定产品、面向开发者的 Claude Code（产生超过 5 亿美元的年化收入）以及面向个人用户的 Pro/Max 计划。F 轮融资将扩大产能，深化安全研究，并支持国际扩张。

---

## 3. 线性代数小书

**原文标题**: The Little Book of Linear Algebra

**原文链接**: [https://github.com/the-litte-book-of/linear-algebra](https://github.com/the-litte-book-of/linear-algebra)

《线性代数小书》是一本面向初学者的线性代数核心概念入门读物。它首先定义标量和向量，强调它们作为基本构建块的作用。向量被表示为标量的有序集合，并在几何上可视化为n维空间中的点、位移或抽象元素。

本书随后介绍了向量加法和标量乘法，定义了这些运算并阐述了它们的几何解释（平行四边形法则、缩放）。线性组合被呈现为生成新向量的机制，从而引出子空间的概念。

点积被引入作为连接代数和几何的一种方式，允许计算长度（范数）、角度和正交性。正交性被进一步探索，定义了正交集和标准正交集，并介绍了将一个向量投影到另一个向量上的概念。

最后，初始部分通过介绍矩阵作为中心对象的概念来结束。矩阵使用示例符号进行正式定义。

本书强调了这些基本概念对于理解向量空间、线性变换和求解方程组的重要性，预示着它们在数据科学、物理学和机器学习等领域的应用。每个部分都包含练习以巩固理解。

---

## 4. Show HN: Moribito – 用于 LDAP 查看/查询的 TUI 工具

**原文标题**: Show HN: Moribito – A TUI for LDAP Viewing/Queries

**原文链接**: [https://github.com/ericschmar/moribito](https://github.com/ericschmar/moribito)

Moribito 是一款基于终端 (TUI) 的 LDAP 服务器浏览器，使用 Go 和 BubbleTea 构建，旨在交互式浏览、查看和查询 LDAP 目录。它具有交互式树状导航、带有剪贴板集成的详细记录查看器、带有实时结果和分页的自定义查询界面、灵活的配置、使用 SSL/TLS 的安全身份验证以及自动更新通知。

可通过 Homebrew (macOS/Linux)、带有安装脚本的直接二进制下载 (Linux, macOS, Windows) 或从源代码构建进行安装。 命令行选项和配置文件允许自定义连接详细信息、分页和重试行为。 配置文件会自动定位在特定于操作系统的位置，并且可以手动或通过命令创建。

导航由键盘和鼠标驱动，允许用户在树、记录和查询视图之间切换。 查询视图包括用于格式化复杂查询以提高可读性和自动分页以有效处理大型结果集的功能。 它支持各种身份验证方法（简单绑定、基于 OU 的绑定、Active Directory、匿名绑定）和安全选项（SSL/LDAPS、StartTLS）。

该项目使用语义化版本控制并提供由 DocPress 生成的完整文档。 欢迎通过 fork 和 pull request 贡献。 它包含一个 Homebrew 公式，便于安装，并根据 MIT 许可证获得许可。

---

## 5. 从Debian移除Guix

**原文标题**: Removing Guix from Debian

**原文链接**: [https://lwn.net/SubscriberLink/1035491/d8100135a8ae4246/](https://lwn.net/SubscriberLink/1035491/d8100135a8ae4246/)

LWN.net文章讨论了即将从 Debian 稳定版和旧稳定版（Debian 13 “trixie” 和 Debian 12 “bookworm”）中移除 Guix 包管理器。Guix 项目的 `guix-daemon` 在 2025 年 6 月披露了安全漏洞，但 Guix 项目的滚动发布模式和缺乏稳定分支使得 Debian 包维护者 Vagrant Cascadian 难以进行补丁回溯。这些修复与其他上游更改交织在一起，使得回溯成为一项重大挑战。

Cascadian 最终提交了错误报告，要求从 Debian 11 (“bullseye”)、bookworm 和 trixie 中移除 Guix。虽然由于 bullseye 的 LTS 状态，移除是不可能的，但 Guix 很可能会从 trixie 和 bookworm 的小版本更新中移除。已经安装了 Guix 的用户将只能使用旧的、易受攻击的版本，除非他们手动更新。

这篇文章强调了在像 Debian 这样的稳定发行版中维护像 Guix 这样的滚动发布包所面临的挑战。Cascadian 指出，在 Debian 上维护 Guix 需要付出巨大的努力，包括管理 Guile 依赖和处理不同的 GCC 版本。尽管被移除，Guix 包含在 Debian 中仍然是有益的，因为它帮助发现并修复了错误。

Guix 项目已经采用了年度发布周期，但这并没有解决发行版对稳定分支的需求。Debian 用户仍然可以通过上游二进制文件使用 Guix，但这可能会排除某些架构。文章最后指出，移除对于稳定版本来说是不寻常的，影响的用户数量相对较少（根据 popcon 统计数据估计约为 230 人）。

---

## 6. 通行密钥与现代认证

**原文标题**: Passkeys and Modern Authentication

**原文链接**: [https://lucumr.pocoo.org/2025/9/2/passkeys/](https://lucumr.pocoo.org/2025/9/2/passkeys/)

Armin Ronacher的博客文章探讨了向通行密钥和现代身份验证的转变，在强调其优点的同时也指出了潜在的缺点。虽然通行密钥旨在提高普通消费者的安全性，但Ronacher对底层标准及其潜在的滥用提出了担忧。

他批评了证明系统，该系统允许网站收集有关验证器的信息，可能导致供应商锁定，并以奥地利政府要求使用白名单硬件令牌访问eID服务为例。他还担心密码管理器之间缺乏私钥导出，这会造成“身份验证锁定”，并使切换生态系统变得困难。

Ronacher还指出了“偷偷摸摸的入门”问题，即用户在没有明确通知的情况下自动注册通行密钥，亚马逊的实施就是一个例子。他进一步表达了对日益依赖谷歌等科技巨头的担忧，这些公司可以终止账户并撤销对第三方网站凭据的访问权限，且无法追索。他认为，这在家庭中，尤其是在丧失行为能力或死亡的情况下，可能会特别麻烦。

最后，他指出，OAuth和通行密钥等身份验证方案日益复杂，使得个人和开源项目更难从头开始构建基本内容，从而可能导致个人能动性的丧失。虽然他承认通行密钥的潜在好处，但他在文章结尾呼吁人们反思，鉴于日益依赖大型公司控制的复杂系统以及数据丢失和访问受限的可能性，这是否真的是我们想要的发展方向。

---

## 7. X（推特）暗中封禁土耳其总统候选人

**原文标题**: X(Twitter) Shadow Bans Turkish Presidential Candidate

**原文链接**: [https://utkusen.substack.com/p/xtwitter-secretly-shadow-bans-turkish](https://utkusen.substack.com/p/xtwitter-secretly-shadow-bans-turkish)

乌特库·森的文章声称，X（前身为Twitter）在关键的2023年土耳其总统选举前夕，秘密对土耳其总统候选人凯末尔·基利奇达罗格鲁进行了屏蔽。作者提出了数据和分析，表明基利奇达罗格鲁的推文和账户可见度受到了显著压制。

核心论点是，基利奇达罗格鲁的影响力和参与度通过未经承认的算法操纵被人为地限制了。森强调了候选人的粉丝数量与他的帖子实际可见度之间的观察到的差异，特别是鉴于他的粉丝基础，本应产生重大影响的推文缺乏自然互动（点赞、转发、回复）。

森声称，这构成了一种政治审查形式，微妙地影响了关键选举期间的信息环境。文章详细介绍了据称如何通过操纵X的推荐算法来实施屏蔽，从而降低了基利奇达罗格鲁的推文出现在用户时间线和搜索结果中的可能性。

作者强调X在土耳其的内容审核政策和算法实践方面缺乏透明度，引发了人们对潜在偏见和干预民主进程的担忧。文章暗示X的行为可能影响了公众舆论，并可能影响了选举结果，呼吁加强对社交媒体平台在塑造政治话语，特别是在选举期间的作用的审查。文章没有直接指责X进行有意的操纵，但强调了表明可能存在干预的强烈关联性。

---

## 8. 在微控制器和嵌入式 Linux 上运行 Erlang/Elixir

**原文标题**: Run Erlang/Elixir on Microcontrollers and Embedded Linux

**原文链接**: [https://www.grisp.org/software](https://www.grisp.org/software)

GRiSP 提供开源工具，用于在微控制器和嵌入式 Linux 上运行 Erlang/Elixir，从而实现实时性能并降低嵌入式应用的复杂性。它提供三种主要堆栈：

*   **GRiSP Metal（原 GRiSP）：** 直接启动到基于 RTEMS 的 Erlang/Elixir VM 中，以在微控制器上实现确定性的实时行为，并最大限度地减少资源使用（适用于 16MB 内存）。它提供直接的硬件访问和监督树以提高可靠性。
*   **GRiSP Alloy：** 启动到基于精简 Buildroot 的实时 Linux 上的 Erlang/Elixir VM 中。 支持多个具有优先级分离和核心关联的 VM，通过安全的分布式 Erlang 链接连接。
*   **GRiSP Forge：** 类似于 Alloy，但使用 Yocto，为长期企业部署提供可定制的 Linux 堆栈和 BSP 集成。

所有三个堆栈都利用通过分布式 Erlang 实现的高效安全本地链接，并优先考虑快速启动时间和较小的攻击面。

**GRiSP-io** 是一个云和边缘平台，用于远程部署、监控和管理使用 GRiSP 堆栈构建的分布式嵌入式系统。它有助于无线更新、实时系统洞察以及云/边缘工作流程集成。

本质上，GRiSP 提供了一个可扩展的生态系统，从原型设计到生产，能够实现针对自动化、机器人和互联设备等嵌入式环境优化的强大分布式应用程序。

---

## 9. 在文本到图像扩散中重用计算以实现高效图像生成

**原文标题**: Reusing Computation in Text-to-Image Diffusion for Efficient Image Generation

**原文链接**: [https://arxiv.org/abs/2508.21032](https://arxiv.org/abs/2508.21032)

Decatur等人在2025年8月28日提交的arXiv论文《在文本到图像扩散中重用计算以高效生成图像集》旨在解决文本到图像扩散模型计算成本高昂的问题。作者并非专注于单次推理的优化，而是探索如何减少从*相关*提示词（即，相似提示词）生成图像时的冗余。

他们的方法利用了扩散模型由粗到精的特性，其中早期的去噪步骤处理相似提示词之间的共享结构。该方法无需训练，包括基于语义相似性对提示词进行聚类，从而允许在初始扩散步骤中共享计算。这意味着模型仅对一组相似的提示词执行一次计算量大的早期去噪步骤。

实验表明，该方法显著降低了计算成本，同时*提高*了图像质量，尤其是在使用经过图像嵌入训练的模型时。它利用UnClip的文本到图像先验来优化扩散步骤的分配，从而提高效率。

作者强调了其方法与现有流程的无缝集成、对提示词集的可扩展性以及减少大规模文本到图像生成对环境和财务负担的潜力。项目页面链接在文档中。该论文已被ICCV 2025接收。

---

## 10. 收集所有因果知识

**原文标题**: Collecting All Causal Knowledge

**原文链接**: [https://causenet.org/](https://causenet.org/)

CauseNet：一个大规模因果知识库

CauseNet是一个从网络提取的大规模因果知识库，旨在表示所有人类因果知识，并将其与单纯的信念区分开来。它包含超过1100万个概念之间的因果关系，这些关系从ClueWeb12、维基百科句子、列表和信息框等来源提取，估计精度为83%。

CauseNet提供三个版本可供下载：完整数据集（CauseNet-Full）、更高精度子集（CauseNet-Precision）和样本数据集（CauseNet-Sample）。每个因果关系都包含全面的出处数据，指定来源和提取方法。例如，来自自然语言句子的关系包括原始句子、使用的语言路径模式以及页面ID和时间戳等源标识符。

数据模型由因果概念和连接它们的因果关系组成，例如“疾病”导致“死亡”。该数据可以加载到Neo4j等图数据库中。为了帮助识别句子中的因果概念，还提供了用于不同数据源的概念识别数据集。

CauseNet项目为因果推理、问答、计算论证和其他领域的研究提供了宝贵的资源。该代码以MIT许可发布，数据以Creative Commons Attribution 4.0 International许可发布。该项目与一篇CIKM 2020论文相关。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 2 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 3 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 4 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 5 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 6 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 7 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 8 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 9 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 10 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 11 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 12 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 13 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 14 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 15 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 16 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 17 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 18 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 19 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 20 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 21 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 22 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 23 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 24 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 25 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 26 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 27 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 28 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 29 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 30 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 31 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 32 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 33 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 34 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 35 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 36 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 37 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 38 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 39 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 40 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 41 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 42 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 43 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 44 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 45 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 46 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 47 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 48 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 49 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 50 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 51 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 52 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 53 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 54 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 55 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 56 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 57 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 58 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 59 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 60 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 61 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 62 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 63 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 64 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 65 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 66 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 67 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 68 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 69 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 70 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 71 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 72 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 73 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 74 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 75 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 76 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 77 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 78 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 79 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 80 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 81 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 82 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 83 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 84 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 85 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 86 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 87 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 88 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 89 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 90 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 91 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 92 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 93 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 94 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 95 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 96 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 97 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 98 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 99 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 100 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 101 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 102 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 103 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 104 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 105 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 106 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 107 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 108 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 109 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 110 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 111 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 112 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 113 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 114 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 115 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 116 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 117 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 118 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 119 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 120 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 121 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 122 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 123 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 124 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 125 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 126 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 127 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 128 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 129 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 130 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 131 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 132 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 133 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 134 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 135 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 136 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 137 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 138 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 139 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 140 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 141 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 142 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 143 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 144 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 145 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 146 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 147 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 148 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 149 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 150 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 151 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 152 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 153 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 154 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 155 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 156 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 157 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 158 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 159 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 160 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 161 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 162 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 163 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 164 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 165 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 166 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 167 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
