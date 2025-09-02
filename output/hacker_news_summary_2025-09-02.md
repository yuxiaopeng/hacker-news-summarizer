# Hacker News 热门文章摘要 (2025-09-02)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Common Lisp 类型怪癖

**原文标题**: Quirks of Common Lisp Types

**原文链接**: [https://www.fosskers.ca/en/blog/cl-type-quirks](https://www.fosskers.ca/en/blog/cl-type-quirks)

本文“Common Lisp类型之怪异之处”探讨了Common Lisp中类型的细微差别和功能。它从两个角度构建类型：“天空类型”强调正确性，“大地类型”侧重于优化。文章可能深入探讨了这些不同方法如何影响类型检查和代码生成。

文章突出了“类型流动性”的概念，可能指的是Common Lisp中类型的动态性和灵活性，这与静态类型语言形成对比。讨论转向类，强调其作为面向对象编程核心构建块的作用，并提及继承和泛型函数分派作为中心机制。泛型函数分派在Common Lisp的对象系统（CLOS）中至关重要，可能构成了关于Common Lisp强大性和灵活性的核心论点。

文章还涉及“抽象”类，表明讨论了Common Lisp类型系统中的抽象和多态性。最后，它提到了“定长整数”（Fixnums），表明可能深入研究特定的数值类型以及与其相关的优化考虑。摘要表明，文本探讨了Common Lisp强大而灵活的类型系统中类型安全性、性能优化和面向对象特性之间的相互作用。结论提供了讨论的“摘要”和一个用于进一步学习的“资源”部分。

---

## 12. 用 Markdown 轻松制作网站

**原文标题**: The easy way to make a website with Markdown

**原文链接**: [https://github.com/dtedesco1/nextjs-markdown-boilerplate](https://github.com/dtedesco1/nextjs-markdown-boilerplate)

本文介绍了一个极简的 Next.js 15 样板项目，旨在方便使用 Markdown (.mdx) 文件创建网站。它允许用户以 Markdown 格式编写内容，然后将其渲染为 Next.js 应用程序中具有样式和动态的页面。

主要功能包括：基于 `app/content` 目录中的文件结构自动路由，能够将 React 组件直接集成到 Markdown 内容中，以及使用 Tailwind CSS 和 DaisyUI 进行全局样式设置。该样板项目采用静态优先的方法，在构建时预渲染页面以获得最佳性能，但可以使用 Next.js 15 的异步 API 或通过设置 `dynamic = 'force-dynamic'` 来配置动态行为。

本指南涵盖了项目的设置，包括安装依赖项（Node.js 18+、npm 9+、TypeScript、React 19、Next.js 15）、运行开发服务器以及构建生产版本。它还概述了项目结构，强调了 `app/content` 目录对于管理 Markdown 内容和页面路由的重要性。

该样板项目提供了用于 SEO/站点地图生成、分析集成、使用 Vitest 进行测试以及静态导出的可选方案。本文最后介绍了贡献指南、许可信息（MIT）以及详细说明更新和与最新版本的 Next.js 和 React 兼容性的发行说明。

---

## 13. 一个大型语言模型是有损百科全书

**原文标题**: An LLM is a lossy encyclopedia

**原文链接**: [https://simonwillison.net/2025/Aug/29/lossy-encyclopedia/](https://simonwillison.net/2025/Aug/29/lossy-encyclopedia/)

本文将大型语言模型(LLM)比作“有损百科全书”。作者认为，LLM内部包含大量压缩信息，但这种压缩会导致细节丢失。因此，理解LLM能够有效回答哪些类型的问题，以及哪些问题需要特定程度的细节，而这种固有的有损性会造成问题，至关重要。

作者以Hacker News上要求LLM生成高度特定的Zephyr项目骨架的评论为例，说明了超出有损百科全书能力范围的问题。他们建议，与其期望LLM“直接知道”如此细致的细节，不如为LLM提供正确的示例以供其使用。这种方法将LLM视为可以处理和作用于所提供信息的工具，而不是所有事实的完美存储库。本质上，本文提倡理解LLM的局限性，并通过为它们提供必要的上下文和示例来发挥其优势，从而成功完成任务。

---

## 14. Kazeta：重温 90 年代主机游戏体验的操作系统

**原文标题**: Kazeta: An operating system that brings the console gaming experience of 90s

**原文链接**: [https://kazeta.org/](https://kazeta.org/)

Kazeta：旨在现代PC上重现90年代经典主机游戏体验的新操作系统。核心理念是简化游戏流程，效仿老式主机易于使用的特性，只需插入卡带，启动设备，即可开始游戏。Kazeta旨在通过提供精简的“插入卡带、启动、游玩”流程，消除现代操作系统和启动器的复杂性。该系统设计直观，专注于游戏，重现90年代主机游戏的直接体验。

---

## 15. AI网络爬虫正因永无止境的内容需求而摧毁网站。

**原文标题**: AI web crawlers are destroying websites in their never-ending content hunger

**原文链接**: [https://www.theregister.com/2025/08/29/ai_web_crawlers_are_destroying/](https://www.theregister.com/2025/08/29/ai_web_crawlers_are_destroying/)

AI网络爬虫正大量抓取网页内容以供大型语言模型（LLM）使用，给网站性能和可访问性带来重大问题。这些爬虫占据了相当一部分互联网流量（据Cloudflare称占30%），由于流量激增，导致网站性能下降、服务中断和运营成本增加。它们常常无视既定的爬虫礼仪，如“robots.txt”和抓取延迟。

小型企业和个人网站尤其脆弱，经常因大量流量而瘫痪。即使是大型网站也面临着处理负载所带来的资源需求增加。这种活动不会转化为内容创作者的收入，因为人工智能机器人不像传统的搜索引擎爬虫那样将用户导回原始来源。

虽然存在登录、付费墙和反机器人技术等防御措施，但人工智能擅长规避这些措施。拟议的“llms.txt”标准旨在提供对LLM友好的内容，而不损害网站性能，但其未来尚不确定。Cloudflare等基础设施提供商正在提供机器人拦截服务，以对抗过度抓取。

作者担心由此产生的“军备竞赛”将导致网络碎片化，访问受限和信息孤岛，可能造成一个“巴尔干化的互联网”，其中访问信息需要付费。曾经的开放网络正处于危险之中。

---

## 16. 你不想雇佣“最好的工程师”

**原文标题**: You don't want to hire "the best engineers"

**原文链接**: [https://www.otherbranch.com/shared/blog/no-you-dont-want-to-hire-the-best-engineers](https://www.otherbranch.com/shared/blog/no-you-dont-want-to-hire-the-best-engineers)

本文挑战了“只招最好的工程师”这一常见的创业公司口号。作者作为一名招聘人员认为，追求“最好”往往是不现实的，而且对早期公司有害。这些顶尖工程师通常薪酬高昂、固执己见，并且有很多诱人的选择，这使得他们不太可能选择一家年轻的创业公司。

创业公司尽管知道自己可能无法吸引到*绝对*最好的工程师，但仍然坚持严格而不切实际的招聘标准：特定的经验、在湾区办公室办公、不愿意支付高薪以及长时间的工作。 这导致了长时间的招聘停滞，对于时间是宝贵资源的创业公司来说，这是一个关键问题。

作者提倡一种更务实的方法：优先招聘*优秀*的工程师，并有意识地考虑权衡。哪些技能才是真正必不可少的？公司愿意在薪资、远程工作或工作与生活平衡方面做出多少让步，才能尽快招到人？文章强调，创业公司应将其冒险、快速行动的理念应用于招聘，认识到速度和“足够好”的方法可能比等待可能永远不会出现的“完美”候选人更有益。 通过放宽要求来扩大候选人范围，创业公司可以从一系列可靠的选择中进行选择，避免在数月毫无成效的搜索后，因绝望而选择次优方案。 关键是明确什么才是真正重要的，并果断行动。

---

## 17. 我的键盘收藏 (2023)

**原文标题**: Keyboards from my collection (2023)

**原文链接**: [https://aresluna.org/50-keyboards-from-my-collection/](https://aresluna.org/50-keyboards-from-my-collection/)

本文展示了Aresluna独特收藏中的50个键盘，这些键盘被描述为奇异、深奥且富有意义。该收藏的公布是为了庆祝作者的著作《Shift Happens》在Kickstarter上的成功。

这些键盘类型和年代跨度很大，包括SafeType和Comfort System等符合人体工程学的键盘，以及为Commodore 64等特定设备设计的键盘，甚至还有游戏键盘。其中还有打字机，包括Olivetti Praxis 48和土耳其Olympia打字机，每款都有其独特之处。

该收藏包括为特定目的设计的键盘，例如“医疗”键盘、为监狱制造的透明Swintec键盘以及名为Tellatouch的盲文键盘。其他亮点包括不寻常的键盘，例如只输出空格的“太空学员”键盘以及隐藏在鞋子里的键盘。

该列表还重点介绍了来自失败的计算机系统和设备的键盘，例如One Laptop Per Child (OLPC)和Canon Cat。文章最后呼吁读者支持作者的著作《Shift Happens》，该书将收录更多与键盘相关的照片和故事。

---

## 18. RubyMine 现在可免费用于非商业用途

**原文标题**: RubyMine is now free for non-commercial use

**原文链接**: [https://blog.jetbrains.com/ruby/2025/09/rubymine-is-now-free-for-non-commercial-use/](https://blog.jetbrains.com/ruby/2025/09/rubymine-is-now-free-for-non-commercial-use/)

RubyMine：非商业用途免费开放

RubyMine是一款智能的Ruby和Rails开发IDE，现在对非商业用途免费开放。此举旨在降低学习Ruby和Rails、贡献开源项目、创作开发者内容以及构建个人项目的门槛。免费许可证提供功能齐全的IDE，与付费版本相同，只是“Code With Me”功能限制为社区版。

商业用途，定义为开发产品并获得商业利益，仍需购买付费许可证。非商业用途包括学习、无经济收益的开源贡献、内容创作和业余爱好开发。免费许可证的一个关键条件是强制性的匿名使用情况统计信息收集，以帮助改进产品。

非商业订阅有效期为一年，如果在过去六个月内使用了许可证，则会自动续订。用户安装后可以在RubyMine IDE内轻松申请免费许可证。此优惠适用于RubyMine 2025.2.1及更高版本。此举反映了JetBrains致力于支持Ruby社区，并确保开发人员能够使用所需的工具来编写清晰、自信的代码。

---

## 19. 归来变入境 (2023)

**原文标题**: The day Return became Enter (2023)

**原文链接**: [https://aresluna.org/the-day-return-became-enter/](https://aresluna.org/the-day-return-became-enter/)

本文追溯了“回车”键从机械打字机时代到计算机中现代“Enter”键的演变，着重介绍了这一复杂而曲折的过渡。最初，打字机上的回车杆是一种机械速记方式，用于推进纸张和返回字车。20世纪中期，电动打字机的出现简化了这一过程，将回车杆变成了按键，通常被称为“回车”。

电传打字机是互联网的前身，它引入了编码字符和控制字符的需求，导致了回车 (CR) 和换行 (LF) 的分离，这至今仍然是编程挑战的根源。

文字处理器的出现带来了另一层复杂性。重点从简单的打字转变为修改和重写文本。文本重排，一种自动调整文本并插入回车符的功能，要求用户避免在每行末尾手动按下回车键，仅将其保留用于段落结尾。这引入了“软回车”和“硬回车”等概念，并模糊了按键和输出之间的联系。

虽然早期的文字处理器感觉像是计算机，但真正的计算机采用了 QWERTY 键盘，认可了其效率。“回车”键变得不再适用，其功能演变为不仅仅是移动到下一行。它开始与执行命令或提交数据相关联。因此，一些系统用“Execute”、“Word Rel”或“Next”取代了“Return”，最终为“Enter”键铺平了道路，它标志着动作的完成及其后续处理。

---

## 20. 亚马逊在人工智能人才争夺战中基本缺席。

**原文标题**: Amazon has mostly sat out the AI talent war

**原文链接**: [https://www.businessinsider.com/amazon-ai-talent-wars-internal-document-2025-8](https://www.businessinsider.com/amazon-ai-talent-wars-internal-document-2025-8)

商业内幕文章《亚马逊基本缺席AI人才争夺战》指出，尽管人工智能领域炒作不断，对AI专家的竞争异常激烈，但亚马逊在很大程度上并未像其科技竞争对手那样积极争取顶尖AI人才。

该文章可能探讨了导致亚马逊看似不那么激进的原因，可能包括：

*   **内部发展：** 亚马逊可能更专注于培养和提拔现有员工来填补AI职位，而不是从其他公司挖人。
*   **不同的AI侧重点：** 亚马逊的AI优先事项可能与其他公司不同，或许更侧重于在其现有业务（如AWS、电子商务和Alexa）中的实际应用，而不是前沿研究。 这可能意味着他们需要不同的技能组合，或者愿意接受具有不同资历的人才。
*   **成本考量：** 顶尖AI人才要求的薪酬和福利可能过高。 亚马逊可能更注重成本效益，选择一种更可持续的方式来构建其AI能力。
*   **文化契合度：** 亚马逊的企业文化可能对一些AI研究人员没有那么大的吸引力，他们可能更喜欢在学术机构或具有更大自主权的初创公司工作。
*   **低估的投资：** 虽然表面上看，亚马逊似乎缺席了人才争夺战，但该文章可能会考虑他们的收购策略或内部资源分配是否表明他们在AI人员方面的投资更为微妙或不为人知。

该文章可能提供了证据和例子，以支持亚马逊在AI人才争夺战中采取了与谷歌、微软或Meta等公司不同的策略这一论断。

---

## 21. 用一千行代码编写虚拟机监控器

**原文标题**: Writing a Hypervisor in 1k Lines

**原文链接**: [https://seiya.me/blog/hypervisor-in-1000-lines](https://seiya.me/blog/hypervisor-in-1000-lines)

本文宣布推出一项新的教程“用1000行代码编写一个虚拟机监控器”，面向熟悉作者之前“用1000行代码编写操作系统”一书的开发者。这个新教程将指导读者使用QEMU，在64位RISC-V上从头开始构建一个1型虚拟机监控器。该教程的一个重要方面是它使用了稳定的Rust，克服了以前执行内联汇编等底层任务时对 nightly 构建的需求。

作者强调了一个关键理解：硬件辅助的虚拟机监控器充当复杂的事件处理程序，类似于`try...catch`块。客户操作系统在“try”块中运行，虚拟机监控器拦截事件（“VM exits”）来处理它们，然后恢复客户操作系统。这种模式解锁了超越传统操作系统虚拟化的潜力，包括硬件仿真、安全边界创建（如gVisor）和特定于应用程序的环境（如Hyperlight）。本教程从头开始，涵盖了与操作系统书籍的一些重叠内容，但现在使用 Rust 编写。该书可在1000hv.seiya.me上公开获取。

---

## 22. 员工们后来吃了它。

**原文标题**: The staff ate it later

**原文链接**: [https://en.wikipedia.org/wiki/The_staff_ate_it_later](https://en.wikipedia.org/wiki/The_staff_ate_it_later)

电视节目字幕“之后，工作人员愉快地享用了”（Kono ato, sutaffu ga oishiku itadakimashita）用于食物出现在屏幕上时，表示拍摄后食物没有被丢弃。其出现源于观众对电视综艺节目中食物浪费的担忧。

该字幕的真实性存在争议。一些报道支持其真实性，引用剧组人员和食品专业人士的说法，他们声称工作人员确实会吃掉剩余食物，以避免浪费并向餐厅表示尊重。前沙滩排球运动员浅尾美和发布照片作为证明。

然而，也存在不同意见。喜剧演员松本人志承认他从未亲眼目睹工作人员吃食物。北野武质疑该字幕的有效性，尤其是在食物明显无法食用时，而评论员古谷经衡表示食物 simply 会被扔掉。

评论员们讨论了该字幕的影响。有些人认为这是对“Aru Aru事件”等事件后观众批评增加的回应，而另一些人则认为它将责任转移给观众，并可能导致过度自我监管，从而阻碍创造力。松尾贵史建议父母应该教育孩子关于食物伦理，而不是依赖电视节目。他还指出，只在烹饪节目中展示该字幕，但在其他浪费食物的活动中却没有展示，这并不一致。

---

## 23. Kapa.ai (YC S23) 招聘研究和软件工程师

**原文标题**: Kapa.ai (YC S23) is hiring research and software engineers

**原文链接**: [https://www.ycombinator.com/companies/kapa-ai/jobs](https://www.ycombinator.com/companies/kapa-ai/jobs)

Kapa.ai (Y Combinator S23 公司) 招聘研究工程师和软件工程师。提供远程职位，薪资范围为 10 万美元至 15 万美元，股权为 0.10%-0.30%，要求 3 年以上经验。Kapa.ai 帮助技术公司利用其现有知识来源（如文档、论坛和 GitHub 问题）构建 AI 助手。这些 AI 助手用作公共文档上的聊天界面、支持表单上的第一线支持以及 GTM 团队的内部助手。Docker、Grafana 和 Mixpanel 等公司都在使用 Kapa.ai。Kapa.ai 由 Finn Bauer 和 Emil Soerensen 于 2023 年创立，拥有一支 19 人的团队，已为 200 多家公司解答了超过 1000 万个问题。该公司通过 AI 简化了对复杂技术信息的访问，从而增强了支持和内部知识导航。

---

## 24. Next.js 令人恼火

**原文标题**: Next.js is infuriating

**原文链接**: [https://blog.meca.sh/3lxoty3shjc2z](https://blog.meca.sh/3lxoty3shjc2z)

多米尼克的博客文章《Next.js 令人恼火》，详细描述了他尝试在 Next.js 应用中实现生产级日志记录时令人沮丧的经历。他概述了一段充满限制和意外行为的旅程。

他的主要不满集中在 Next.js 中间件的不足上。多米尼克强调了它的局限性，包括无法链接中间件以及只能在它们和路由之间传递标头的限制。他尝试将 AsyncLocalStorage 与 pino 一起用于日志记录，但由于 Next.js 的默认边缘运行时以及它显然无法在中间件和页面/布局之间保持相同的异步上下文而遇到问题。

核心问题是缺乏一种干净的方法将请求特定信息（例如用于日志记录的请求 ID）从中间件传递到实际的页面渲染逻辑。他采取了一种复杂的回避方法，涉及通过标头传递请求 ID、拆分记录器以及处理不同的服务器环境，最终突出了该解决方案的笨拙和容易出错的性质。

多米尼克随后探索使用自定义 Next.js 服务器，希望重新获得控制并有效地利用 AsyncLocalStorage。然而，即使这种方法也未能传播日志记录上下文。

他将 Next.js 与 SvelteKit 进行了不利的对比，称赞后者的中间件系统具有灵活性以及将数据无缝传递给处理程序的能力。他批评 Vercel 在一个副项目中提供了一个卓越的解决方案，却忽略了其旗舰产品。

最后，多米尼克对 Next.js GitHub 问题跟踪器表示沮丧，其中的错误报告长期无人回应，从而产生一种无助感并阻碍社区贡献。他的总体情绪是对 Next.js 的失望，理由是不断的错误、不一致和不必要的复杂性。

---

## 25. 让Minecraft变球形

**原文标题**: Making Minecraft Spherical

**原文链接**: [https://www.bowerbyte.com/posts/blocky-planet/](https://www.bowerbyte.com/posts/blocky-planet/)

本文探讨了在 Unity 技术演示 “方块星球” 中，将 Minecraft 的立方体像素映射到球形星球上所涉及的挑战和解决方案。主要障碍在于如何将平面网格系统适应于曲面，同时保持类似 Minecraft 的风格。

本文重点介绍了两个主要问题：将 2D 正方形网格映射到 3D 球体上，以及在深度方向上保持方块宽度。文章深入探讨了四边形球体的应用，将地球划分为六个扇区，与单矩形地图相比，减少了失真。采用了一种改进的映射方法来预先扭曲正方形网格，以抵消归一化失真，从而减少方块的挤压和拉伸。

为了解决深度方向的失真，文章描述了将星球划分为多个壳层，随着从中心向外移动，每层增加更多方块，以保持方块大小。这些壳层将所有边对齐良好的方块分组在一起。

最后，文章解释了星球的数据结构。它被划分为六个扇区，然后是大小不一的壳层，这些壳层进一步细分为规则大小的区块（16x16x16 个方块），以实现高效处理。使用 "方块地址" 来指定每个方块在扇区、壳层、区块结构中的精确位置，以方便诸如方块放置之类的机制。文章最后详细（可选）地解释了如何计算给定世界位置的方块地址。

---

## 26. 实现箔片贴纸效果

**原文标题**: Implementing a Foil Sticker Effect

**原文链接**: [https://www.4rknova.com/blog/2025/08/30/foil-sticker](https://www.4rknova.com/blog/2025/08/30/foil-sticker)

本文详细介绍了如何创建一个自定义的Three.js着色器，该着色器可以模拟箔片贴纸的视觉效果，包括虹彩和闪烁的金属薄片。它解释了该效果背后的基本原理，借鉴了现实世界中由薄膜干涉引起的虹彩现象以及金属薄片的反射特性。

实现重点在于实时近似这些效果，使用诸如将视角映射到色调以产生虹彩，以及采用程序噪声生成模仿箔片闪光的随机亮斑等技术。本文提供了一个实时演示，用户可以在其中调整着色器参数。

然后，本文将实现分解为两个主要部分：顶点着色器和片段着色器。顶点着色器使用Rodrigues旋转公式管理剥离几何体，并将顶点数据传递给片段着色器。片段着色器处理光照、反射、虹彩和箔片闪光。它使用alpha裁剪、背面着色、用于闪光的程序噪声、用于反射的环境贴图采样以及菲涅耳计算来创建视觉上合理的箔片贴纸效果。文章提供了两种着色器的代码，并解释了使用的uniform变量和varying变量。

最后，本文阐明了代码的许可条款，根据Creative Commons Attribution-NonCommercial 4.0 International许可提供。它还鼓励读者通过GitHub Sponsors支持作者的工作，以促进未来的教程和开源项目。

---

## 27. 帕特里克·温斯顿：如何演讲 (2018) [视频]

**原文标题**: Patrick Winston: How to Speak (2018) [video]

**原文链接**: [https://www.youtube.com/watch?v=Unzc731iCUY](https://www.youtube.com/watch?v=Unzc731iCUY)

这段文字看起来是 YouTube 视频页面*底部*的文字，**而不是视频内容本身的摘要。** 标题表明该视频是关于 Patrick Winston 的有效演讲技巧，但您提供的内容只是标准的 YouTube 样板文字。

因此，我无法根据这些信息提供视频内容的摘要。文字仅包含：

*   **标准的 YouTube 法律和政策链接：** 指向 YouTube 政策（隐私、条款等）和联系方式的链接。
*   **版权信息：** 指出 YouTube 的版权和 Google LLC 的参与。
*   **功能和倡议：** 提及新功能、创作者资源、广告选项和 NFL Sunday Ticket。

要总结视频，我需要访问实际的视频内容或其文字稿/描述。

---

## 28. FreeDroidWarn

自由安卓警告

**原文标题**: FreeDroidWarn

**原文链接**: [https://github.com/woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn)

FreeDroidWarn 是一个库，旨在在 Android 应用中显示警告对话框，告知用户 Google 即将对在 Google Play 商店之外分发的应用提出的开发者验证要求。 从 2026/2027 年起，Google 将强制开发者向 Google 提交个人身份信息，用于在认证的 Android 设备上运行的应用。 使用 FreeDroidWarn 的应用的开发者表示他们不会遵守此要求。 因此，在 2026/2027 年之后，这些应用将停止在认证的 Android 设备上运行。

可以通过将 JitPack 仓库添加到 `build.gradle` 文件并包含依赖项 `com.github.woheller69:FreeDroidWarn:V1.3`，轻松地通过 JitPack 将该库集成到 Android 项目中。 只需在应用的 `onCreate` 方法中添加一行简单的代码 `FreeDroidWarn.showWarningOnUpgrade(this, BuildConfig.VERSION_CODE);`，即可在应用升级时触发警告对话框。

该库在 Apache V2.0 许可下发布，允许免费使用和修改。 该文档链接到 Android Authority 和官方 Android Developer 网站，以获取有关 Google 验证要求的更多信息。

---

## 29. 熊现在是源码可用了

**原文标题**: Bear is now source-available

**原文链接**: [https://herman.bearblog.dev/license/](https://herman.bearblog.dev/license/)

2025年9月1日，Bear的开发者宣布将该软件的许可证从MIT变更为Elastic许可证。最初以MIT许可证发布是为了鼓励学习和进行隐私及安全审计，但作者现在被迫限制使用，原因是竞争对手屡次复刻该项目以创建竞争服务。

作者对自己的辛勤工作被抄袭并可能威胁到生计感到失望和沮丧。Elastic许可证虽然与MIT许可证非常相似，但禁止使用Bear的代码来提供托管或管理的服务。这一决定符合开源项目旨在阻止“搭便车竞争”的日益增长的趋势。

作者认为，通过人工智能驱动的编码越来越容易创建竞争产品，这是导致这一变化的因素之一。虽然承认Bear代码库的价值，但作者强调该平台真正的优势在于其用户群以及对长期维护的承诺。更改许可证的决定是一种保护措施，旨在确保平台的持续良好发展，即使这限制了其他人可以对代码做的事情。

---

## 30. 数十名科学家发现能源部一份新的气候报告存在错误。

**原文标题**: Dozens of scientists find errors in a new Energy Department climate report

**原文链接**: [https://www.npr.org/2025/09/02/nx-s1-5521384/energy-report-scientists-climate-change](https://www.npr.org/2025/09/02/nx-s1-5521384/energy-report-scientists-climate-change)

美国能源部一份新的气候变化报告，由能源部长克里斯·赖特主导，正面临超过85位科学家的强烈批评，他们声称该报告充斥着错误并歪曲了已确立的气候科学。此前有指控称该报告是由一批精心挑选的气候变化怀疑论者秘密编写的，而这次反驳正是在这些指控之后发生的。

科学家们认为，能源部的报告存在选择性地采用数据，并忽略气候科学的关键方面的情况。例如，能源部的报告表明，二氧化碳水平的升高可能对美国农业有利，同时却忽略了极端天气和高温对农作物的负面影响。它还声称没有证据表明“气象”干旱加剧，忽略了高温和蒸发对干旱严重程度的影响。

批评人士认为，特朗普政府正在利用能源部的报告来证明撤销气候法规是合理的，特别是构成气候污染监管基础的危害发现。气候虚假信息研究员约翰·库克认为，该报告旨在通过淡化气候变化的严重性来拖延应对气候变化的行动。

德克萨斯A&M大学教授安德鲁·德斯勒强调了解决该报告科学缺陷的重要性，尤其考虑到它被用于政策决策。加图研究所的特拉维斯·费舍尔协调了能源部的气候工作组，他说能源部将解决公开评论期间发现的任何错误。环境保护署署长李·泽尔丁表示，本届政府的目标是“直接将匕首刺入气候变化宗教的心脏”。

---

## 31. 塑造进化树的突发性涌动

**原文标题**: The Sudden Surges That Forge Evolutionary Trees

**原文链接**: [https://www.quantamagazine.org/the-sudden-surges-that-forge-evolutionary-trees-20250828/](https://www.quantamagazine.org/the-sudden-surges-that-forge-evolutionary-trees-20250828/)

本文探讨了一种新的进化模型，该模型提出进化是以“突发性激增”而非渐进性变化的方式发生的，这一概念被称为“跃迁式分枝”。该模型基于间断平衡理论，认为显著的进化变化集中在线粒分裂的点上，而不是分散在很长一段时间内。

进化生物学家乔丹·道格拉斯和他的团队开发了一个数学框架，用于测量分支点上的变化“峰值”，并解释了已灭绝的谱系（“幻影爆发”）。他们使用包括氨酰-tRNA合成酶（aaRSs）、头足类动物性状和印欧语系在内的各种数据集测试了该模型。结果一致表明，谱系分裂周围存在快速的进化变化，表明了一种“分裂即加速”的动态。

这些发现弥合了古生物学家的观点（他们经常在化石记录中观察到间断平衡）和分子生物学家的观点（他们倾向于看到更渐进的变化）。该模型表明，环境变化或新的进化压力可能会触发这些快速适应和物种形成事件。虽然还需要进一步的测试，但该模型为进化的节奏提供了一个新的视角，表明突发性变化是生物和文化进化中的一个基本方面。

---

## 32. 树莓派 5 支持 (OpenBSD)

**原文标题**: Raspberry Pi 5 support (OpenBSD)

**原文链接**: [https://marc.info/?l=openbsd-cvs&m=175675287220070&w=2](https://marc.info/?l=openbsd-cvs&m=175675287220070&w=2)

此邮件宣布OpenBSD RAMDISK发行版为arm64架构增加了对树莓派5 Model B的支持。Marcus Glocker于2025年9月1日提交的commit修改了`distrib/arm64/iso`和`distrib/arm64/ramdisk`目录下的`Makefile`，并在`ramdisk`目录下的`install.md`和`list`中添加了条目，以启用此支持。

该公告还强调了树莓派5初始支持的几个已知问题：

*   **PCIe启动：** 由于缺少U-Boot支持，目前无法从PCIe存储HAT启动。
*   **WiFi：** WiFi在树莓派5 Model B "d0" 板上无法工作。
*   **主动散热器（风扇）：** 主动散热器（风扇）无法工作，因为缺少所需的pwm/clock驱动程序，但目前正在努力解决这个问题。

该更改已由kettenis@和deraadt@审核并批准。

---

## 33. 内核中32位支持的未来

**原文标题**: The future of 32-bit support in the kernel

**原文链接**: [https://lwn.net/SubscriberLink/1035727/4837b0d3dccf1cbb/](https://lwn.net/SubscriberLink/1035727/4837b0d3dccf1cbb/)

内核架构维护者 Arnd Bergmann 在 2025 年欧洲开源峰会上讨论了 Linux 内核中 32 位支持的未来。他表示，对于新产品而言，32 位系统正变得过时，主要需要为现有硬件提供支持。虽然桌面和手机系统已基本过渡到 64 位，但嵌入式 Linux，尤其是在 Arm 处理器上，仍然严重依赖 32 位。

Bergmann 预计将逐步移除对旧架构的支持。他的目标是移除对较旧的 pre-armv7 CPU 的支持，并可能在 2027 年左右移除高内存支持，在 2028 年左右移除 nommu 支持。

文章强调了维护 32 位支持的痛点，特别是高内存管理的复杂性。正在探索诸如分离内核和用户空间地址空间或使用物理内存作为 zram 交换设备等解决方案。尽管内核已解决了 2038 年问题，但由于各种软件包中未修复的错误，该问题仍然构成挑战。

大端支持与 32 位交织在一起，由于过时而面临潜在的移除，尽管 IBM 对大端大型机和 PowerPC 系统的持续支持使其得以存活。关于移除对旧 CPU 架构和板级文件的支持的讨论正在进行中。关键在于，尽管 armv7 支持至少还需要十年，但其他 32 位架构可能会更快地消失，这取决于正在进行的讨论和用户需求。

---

## 34. Cloudflare Radar：人工智能洞察

**原文标题**: Cloudflare Radar: AI Insights

**原文链接**: [https://radar.cloudflare.com/ai-insights](https://radar.cloudflare.com/ai-insights)

无法访问文章链接。

---

## 35. 瓢虫月报：2025年8月

**原文标题**: This Month in Ladybird: August 2025

**原文链接**: [https://buttondown.com/ladybird/archive/this-month-in-ladybird-august-2025/](https://buttondown.com/ladybird/archive/this-month-in-ladybird-august-2025/)

Ladybird浏览器引擎月报：2025年8月

本报告重点介绍了Ladybird浏览器引擎的显著进展，这得益于43位贡献者合并的244个拉取请求。主要成就包括欢迎Bastian Müller、Timely Learning和OakHost等新赞助商，他们的支持为项目提供了资金。

Web平台测试(WPT)取得了重大进展，新增通过8,106项测试，总计1,839,962项。Ladybird现在可以运行Google Sheets，这是通过修复画布更新错误实现的一个重要里程碑。其他值得注意的实现包括Gamepad API、Cookie Store API和用于基于环境的样式的CSS `env()`函数。

团队开始实施用于结构化样式属性操作的CSS Typed OM API，以及用于目标标题样式的`:heading`伪类。此外，还改进了CSS钳制和插值、Linux上的WebGL支持（现在与macOS相当）、弹性容器中的按钮布局、嵌套内联边距框以及用于文本编辑和光标放置的字形簇处理。

文章感谢了众多代码贡献者，并鼓励读者订阅Ladybird新闻通讯以获取未来更新。

---

## 36. Imgur社区全面反抗其所有者

**原文标题**: Imgur's Community Is in Full Revolt Against Its Owner

**原文链接**: [https://www.404media.co/imgurs-community-is-in-full-revolt-against-its-owner/](https://www.404media.co/imgurs-community-is-in-full-revolt-against-its-owner/)

Imgur社区因MediaLab AI母公司下平台退化而面临反抗（“Imgurians”），Imgur首页目前充斥着反MediaLab AI的表情包，尤以约翰·奥利弗竖中指的图片最为显眼，象征着用户的不满。

核心问题源于网站功能下降（通知故障、图片上传失败）、人工版主消失以及对人工智能审核无效且导致不公正封禁的担忧。用户认为，MediaLab AI以广告变现热门网站的策略，导致Imgur的社区属性被忽视，转而追求利润最大化。

前员工证实Imgur团队内部出现裁员，重心转移至MediaLab AI的更广泛目标，导致Imgur人手不足，可能严重依赖人工智能审核。这引发了对审查制度和内容管理缺乏人工监督的担忧。

Imgurians正考虑在9月1日发起抵制活动，以表达不满。MediaLab AI已面临Imgur创始人Alan Schaaf以及其他之前被MediaLab AI收购的网站所有者的法律挑战，他们声称收购协议中存在未支付款项。社群的愤怒突显了忠实用户群体与专注于平台利润最大化的公司之间的紧张关系。

---

## 37. 丹麦海底发现石器时代聚落

**原文标题**: Stone Age settlement found under the sea in Denmark

**原文链接**: [https://apnews.com/article/denmark-stone-age-settlements-underwater-research-d0a77a07cdad2c23bd61c3f4bb015d7d](https://apnews.com/article/denmark-stone-age-settlements-underwater-research-d0a77a07cdad2c23bd61c3f4bb015d7d)

丹麦海岸水下发现石器时代遗址，为研究数千年前北欧的生活提供了难得的机会。该遗址位于波罗的海，包含保存完好的文物，包括工具、动物骨骼，甚至还有壁炉和住所等结构的证据。

研究人员认为，该遗址可以追溯到石器时代早期，可能在 5500 年前左右，当时的海平面较低。由于海底缺氧，有机物的腐烂速度减慢，遗址的保存状况非常出色。

这一发现意义重大，因为它为人们了解当时居住在该地区的人们的日常生活、狩猎方式和社会组织提供了宝贵的见解。出土的文物为他们的技术、饮食和环境提供了有形的证据。水下考古对于理解这些曾经是可居住地区的水下景观至关重要。这一特殊发现有望揭示更多关于斯堪的纳维亚半岛从游牧狩猎采集社会向定居农业社区过渡的信息。研究正在进行中，科学家们正在继续探索和分析该遗址，以揭开这个古老的水下遗址的更多秘密。

---

## 38. WinBoat：在Linux上无缝运行Windows应用

**原文标题**: WinBoat: Run Windows apps on Linux with seamless integration

**原文链接**: [https://github.com/TibixDev/winboat](https://github.com/TibixDev/winboat)

WinBoat旨在将Windows应用程序无缝集成到Linux环境中。目前处于测试阶段，它提供直观的界面、自动安装，并能以原生Linux窗口运行任何Windows应用程序或访问完整的Windows桌面。两个系统之间的文件共享通过挂载主目录实现。

先决条件包括至少4GB内存、2个CPU线程、/var目录下32GB的可用存储空间、KVM虚拟化、Docker、Docker Compose v2以及带有声音支持的FreeRDP。该项目提供AppImage和解压缩的Linux构建版本。目前不支持Podman和Docker Desktop。

项目欢迎错误修复、功能改进和文档更新等贡献，仅关注技术方面。该项目的许可证是MIT。WinBoat承认受到了类似项目（如WinApps、Cassowary和dockur/windows）的启发。提供联系方式和社交媒体链接。

---

## 39. 我们应该有能力在自己拥有的硬件上运行任何我们想运行的代码。

**原文标题**: We should have the ability to run any code we want on hardware we own

**原文链接**: [https://hugotunius.se/2025/08/31/what-every-argument-about-sideloading-gets-wrong.html](https://hugotunius.se/2025/08/31/what-every-argument-about-sideloading-gets-wrong.html)

本文认为，围绕侧载限制的争论，尤其是在Android等平台上，往往忽略了核心问题。作者赞同“我应该能够在自己拥有的硬件上运行任何代码”的观点，但认为侧载限制主要关乎控制硬件附带的**软件**，而非硬件本身。作者认为，更有效的批评是关注缺乏在设备上构建和安装替代操作系统的能力。

本文以苹果的iOS为例，强调了紧密的软硬件集成对产品成功的贡献，并告诫不要通过立法强制进行会从根本上改变iPhone性质的改变。

作者建议，与其争取在现有操作系统中不受限制的访问权限，不如推动立法，**要求制造商提供构建和安装替代操作系统所需的技术支持和文档。** 这样，用户就可以重新利用他们的硬件，例如将PlayStation 5变成基于Linux的模拟器，即使这意味着牺牲访问制造商的软件和服务。重点从要求在制造商的操作系统中运行任何代码的自由，转移到要求在硬件上安装和运行任何操作系统的自由。

---

## 40. 直观的查找替换命令行工具（sed替代方案）

**原文标题**: Intuitive find and replace CLI (sed alternative)

**原文链接**: [https://github.com/chmln/sd](https://github.com/chmln/sd)

`sd`：一款直观易用的命令行查找替换工具，旨在替代 `sed`。它致力于通过更易读的语法和合理的默认设置来简化常见的查找替换任务。

主要特性包括：

*   **轻松的正则表达式：** 使用熟悉的 JavaScript/Python 正则表达式语法。
*   **字符串字面量模式：** 提供直接的字符串替换选项，无需转义特殊字符。
*   **可读性强的语法：** 将查找和替换表达式分开，以提高清晰度。
*   **符合常识的默认设置：** 专为典型的日常使用而设计。

本文将 `sd` 与 `sed` 进行对比，展示了在处理换行符和斜杠等特殊字符时，`sd` 的语法更简洁易用。

基准测试表明，在简单和正则表达式替换任务中，`sd` 的性能优于 `sed`，速度分别提高了 2.35 倍和 11.93 倍。

本文包括安装说明，并提供了使用 `sd` 进行基本正则表达式替换、捕获组和文件修改的实际示例，包括项目范围内的查找替换操作和处理极端情况。

---

## 41. 多伦多的地下迷宫

**原文标题**: Toronto’s underground labyrinth

**原文链接**: [https://www.worksinprogress.news/p/torontos-underground-labyrinth](https://www.worksinprogress.news/p/torontos-underground-labyrinth)

本文探讨了多伦多的“PATH”地下通道，这是一个长达30公里的地下行人隧道网络，连接市中心的地铁站、火车站和办公楼。 PATH 由各个企业在几十年间自发发展而来，为缓解市中心拥堵，尤其是在高峰通勤时段和恶劣的冬季天气，提供了一种独特的解决方案。

与典型的地下通道不同，PATH 是一个维护良好、高端购物中心式的环境，并配备私人保安。 它每天高效地输送数十万通勤者，是对现有公共交通系统的补充。

作者认为，PATH 的成功在于其独特的经济模式。 单个土地所有者认为行人隧道足够有价值，可以独立融资和建造，即使其他土地所有者从中受益。 至关重要的是，行人隧道具有很高的容量限制，可防止网络扩展时出现拥堵。

作者将其与铁路等其他交通基础设施进行了对比，由于部分路段缺乏效用以及新增支线可能导致拥堵的风险，铁路需要统一规划。

虽然行人隧道并非总是适用，尤其是在它们可能削弱街道生活的地方，但在像多伦多这样的人口密集市中心，它们是有益的。 文章最后质疑为什么更多的城市没有采用类似的行人地铁系统，并提出了潜在的原因，例如现有的地下基础设施或监管障碍。 文章认为，行人地铁可以在解决繁荣市中心的交通挑战方面发挥重要作用。

---

## 42. 预算约束下的自适应LLM路由

**原文标题**: Adaptive LLM routing under budget constraints

**原文链接**: [https://arxiv.org/abs/2508.21141](https://arxiv.org/abs/2508.21141)

这篇arXiv文章 (arXiv:2508.21141) 提出了一种在预算约束下的大型语言模型 (LLM) 路由的新方法。作者 Pranoy Panda、Raghav Magazine、Chaitanya Devaguptapu、Sho Takemori 和 Vishal Sharma 解决了在面对不同LLM能力、成本以及对最佳查询-LLM配对的有限真实世界知识时，如何为给定查询动态选择最合适LLM的挑战。

他们没有将LLM路由视为具有完整知识的监督学习问题，而是将其构建为上下文老虎机问题，从而可以通过老虎机反馈进行自适应决策。他们的算法避免了对每个查询在所有LLM上进行穷举推理的需要。

核心创新是开发了一个查询和LLM的共享嵌入空间，该空间最初从离线人工偏好数据中学习，并使用在线老虎机反馈进行优化。这个嵌入空间对齐了查询和LLM的表示，以反映它们的亲和力。他们引入了PILOT (Preference-prior Informed Linucb fOr adaptive rouTing)，这是LinUCB的扩展，用于实现这一概念。

此外，该论文通过实施建模为多重选择背包问题的在线成本策略，解决了用户预算约束的关键方面，确保了资源高效的LLM路由。

该论文被EMNLP 2025（findings）接收。作者提供了该论文的PDF、HTML（实验性）和TeX源代码的访问权限。

---

## 43. 买方拉动和卖方推动销售理论

**原文标题**: The buyer-pull and seller-push theories of sales

**原文链接**: [https://howtogrow.substack.com/p/the-physics-of-sales](https://howtogrow.substack.com/p/the-physics-of-sales)

无法访问文章链接。

---

## 44. Firefox 142 新特性

**原文标题**: What's New with Firefox 142

**原文链接**: [https://www.mozilla.org/en-US/firefox/142.0.1/whatsnew/?oldversion=139.0.4&utm_medium=firefox-desktop&utm_source=update&utm_campaign=142](https://www.mozilla.org/en-US/firefox/142.0.1/whatsnew/?oldversion=139.0.4&utm_medium=firefox-desktop&utm_source=update&utm_campaign=142)

火狐142推出全新设计，着重减少干扰，提升专注度。主要特性是引入垂直标签页，可移动至侧边栏。该侧边栏提供便捷的位置来管理标签页、固定重要网站以及访问AI助手。此次更新强调高效导航和更整洁的浏览环境。总而言之，火狐142旨在通过将基本工具和功能整合到一个易于访问的侧边栏中，从而简化用户体验，实现更少干扰和更专注的浏览会话。

---

## 45. 英国有史以来规模最大的二手书库存之一

**原文标题**: One of Britain's largest stocks of second-hand books ever amassed

**原文链接**: [https://www.worldofinteriors.com/story/richard-axe-second-hand-books-yorkshire](https://www.worldofinteriors.com/story/richard-axe-second-hand-books-yorkshire)

70多岁的书商理查德·阿克斯在北约克郡艾斯加斯的旧青年旅舍里，积累了英国最大的二手书藏书之一，总计超过15万册。这些书籍按主题精心整理，占据了四层楼的25个房间，需要建筑结构能够承受其重量。

阿克斯在菲律宾兼职居住，他通过参加英国各地的拍卖会，购买大量图书，出售有价值的书籍，同时为自己的藏书保留图书，从而经营着一项非常成功的业务。他专注于“质量好但相对普通”和“非常专业、昂贵的古董书”。尽管广告很少，访客也不多，但他每周都能稳定地售出大量书籍。

文章强调了互联网对图书市场的影响，指出虽然普通书籍已经贬值，但真正稀有的物品价值却大幅增加，例如《哈利·波特与魔法石》的早期版本。

由于健康状况下降和年龄增长，阿克斯不情愿地以150万英镑的价格出售他的房产和藏书。他担心藏书会被拆分，并愿意协助买家继续他的事业。虽然准备出售一切，但他承认自己想保留关于约克郡、足球、罗斯金以及18/19世纪地图的藏书。

---

## 46. 非周期平铺 V：可精炼的边界

**原文标题**: Aperiodic Tilings V: The Refinable Frontier

**原文链接**: [https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/aperiodic-refine/](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/aperiodic-refine/)

Simon Tatham的“非周期性平铺 V：可精炼的边界” 探讨了在初始替换系统不明确时，创建确定性转换器以生成非周期性平铺的挑战。当相同的瓷砖排列可以有多个有效的相邻配置时，就会出现不明确性，从而妨碍了确定性转换器的创建。

该文章介绍了一种将不明确的替换系统精炼为明确的系统的方法，从而允许创建确定性转换器。 这种精炼涉及通过将现有瓷砖克隆为子类型来增加瓷砖类型的数量。 关键在于确定在平铺规则中在何处以及如何应用这些子类型。

Tatham强调了以往的方法，包括用于帽子平铺的HHTPFFF系统，该系统是通过观察不明确的HTPF系统与涉及10个六边形元瓷砖的明确系统之间的对应关系而推导出来的。 这个过程表明，某些HTPF元瓷砖（如H和F）可以被划分为子类型，具有不同的六边形簇的排列方式。

文章强调，理解瓷砖的邻域对于精炼过程至关重要。 Tatham引用了mathBlock关于HTPF瓷砖中“排水”的研究，指出F元瓷砖可以根据其位置表现出多种行为。 例如，将F元瓷砖划分为F0、F1和F2对应于不同的排水行为。 具体而言，可以通过观察帽子如何连接到F扩展的顶点来区分F的子类型。

Tatham表示，他已经自动化了精炼不明确系统的过程，但除了强调邻域之外，该算法的细节尚未描述。

---

## 47. Python纪录片：起源故事 [视频]

**原文标题**: Python: The Documentary – An origin story [video]

**原文链接**: [https://www.youtube.com/watch?v=GfH4QL4VqJ0](https://www.youtube.com/watch?v=GfH4QL4VqJ0)

提供的文本看起来是 YouTube 视频页面的页脚，而不是描述关于 Python 的纪录片的文章。 它包含标准的 YouTube 法律和信息链接，例如：

*   **版权：**链接到关于新闻、版权和相关内容的信息。
*   **创作者/开发者资源：**面向使用 YouTube 的内容创作者和开发者的链接。
*   **条款和政策：**链接到 YouTube 的服务条款、隐私政策和安全信息。
*   **关于 YouTube：**解释 YouTube 的运作方式以及测试中的功能。
*   **NFL Sunday Ticket：**表明与 NFL 比赛相关的内容（可能通过 YouTube 播放）。
*   **版权声明：**Google LLC（YouTube 的所有者）的通用版权声明。

本质上，这是在 YouTube 页面底部找到的样板文字。 它没有提供任何关于名为“Python：纪录片 - 一个起源故事”的纪录片内容的信息。 因此，无法从这些信息中总结*关于纪录片本身*的任何内容。

---

## 48. 脑部手术让我领悟到意识这脆弱的馈赠

**原文标题**: What brain surgery taught me about the fragile gift of consciousness

**原文链接**: [https://bigthink.com/business/brain-surgery-fragile-gift-of-consciousness/](https://bigthink.com/business/brain-surgery-fragile-gift-of-consciousness/)

在《脑部手术教会了我意识的脆弱馈赠》一文中，埃里克·马科维茨反思了面对可能致命的脑部手术这一深刻经历，以及它对理解生命和意识所产生的持久影响。 手术前夕，他产生了高度的意识，与亲人和周围世界建立了联系，并对存在的奇迹产生了深深的感激之情。

马科维茨的手术很成功，但恢复过程却十分艰难。 在此期间，他经历了“幸存者狂喜”，并重新专注于生存以及有意识地生活真正意味着什么。 他意识到生命不仅仅是一系列成就，而是一个脆弱的、相互交织的系统，依赖于许多因素，包括医疗和情感支持。

他将长寿重新定义为一种积极的选择，一种植根于注意、热爱和选择生命的实践，即使在痛苦中也是如此。 马科维茨改变了他的优先事项，重视临在胜过生产力，并强调倾听和感受。 最终，他认为意识超越了神经功能，涵盖了关怀、爱和以开放的心态面对死亡的意愿。 他得出结论，善良源于意识，而意识又源于关怀，这才是意识的真正馈赠。

---

## 49. OpenAI称正在扫描用户对话并将内容报告给警方

**原文标题**: OpenAI says it's scanning users' conversations and reporting content to police

**原文链接**: [https://futurism.com/openai-scanning-conversations-police](https://futurism.com/openai-scanning-conversations-police)

本文探讨了OpenAI新披露的一项做法，即扫描用户ChatGPT对话中的有害内容，特别是暴力威胁，并可能将这些对话报告给执法部门。此前，越来越多的报告显示，用户在与ChatGPT互动后出现了精神健康危机，包括可能由ChatGPT引发的“人工智能精神病”。

虽然OpenAI承认目前没有将自残案例报告给警方以尊重用户隐私，但该公司正在监控对话，并将那些表明可能对他人造成伤害的对话升级处理。这项模糊的政策引发了人们的担忧，即究竟什么会触发人工审核和警方介入。

文章强调了这种监视与OpenAI在与《纽约时报》的持续诉讼中对用户隐私的立场之间的矛盾，该公司在诉讼中拒绝提供ChatGPT日志以保护用户数据。作者强调，这项新规定似乎与该公司支持隐私的立场相矛盾，OpenAI首席执行官Sam Altman也承认，使用ChatGPT作为治疗师或律师并不能像与真人专业人士交谈那样获得同样的保密性。

作者总结说，OpenAI正处于管理有害用户体验带来的负面公关，以及实施可能侵犯用户隐私的严厉审查之间的两难境地。文章还提到了一个具体的案例，一名男子陷入人工智能精神病并杀害了他的母亲后自杀，暗示这一事件可能促使OpenAI出台了新政策。

---

## 50. 第一台喷墨打印机曾是一种医疗设备。

**原文标题**: The first inkjet printer was a medical device

**原文链接**: [https://spectrum.ieee.org/rune-elmqvist](https://spectrum.ieee.org/rune-elmqvist)

艾莉森·马什在《技术史杂志》上发表的文章揭示了，第一台喷墨打印机Mingograph并非为典型的打印目的而设计，而是一种医疗设备。Mingograph由植入式心脏起搏器的先驱Rune Elmqvist发明，它使用喷嘴将墨水喷到纸上。这标志着与当时流行的撞击式打印方法有了显著的背离。

这篇文章挑战了人们普遍认为喷墨打印机纯粹是消费电子产品的看法，强调了它们在生物医学领域中令人惊讶的起源。它强调了Elmqvist的创新思维，Elmqvist以其对心脏技术的贡献而闻名，展示了医疗需求如何激发技术进步，其应用远远超出了最初的目的。本质上，Mingograph就是一个例子，说明了技术如何出乎意料地发展，分支到不同的领域，并最终塑造消费电子产品的格局。

---

## 51. 关于亚马逊领导力的思考

**原文标题**: Thoughts on (Amazonian) leadership

**原文链接**: [https://www.daemonology.net/blog/2025-09-01-Thoughts-on-Amazonian-Leadership.html](https://www.daemonology.net/blog/2025-09-01-Thoughts-on-Amazonian-Leadership.html)

本文从局外人的角度探讨了亚马逊的领导力准则，特别是客户至上、主人翁精神和行动偏好。作者是一位多年的AWS客户和AWS英雄，他认为这些原则本身是合理的，但实际执行有时却不尽如人意。

关于客户至上，作者认为亚马逊已经从提供创新的“构建块”转变为仅仅交付客户直接要求的服务，这可能会错失突破性解决方案的机会。他们认为需要像Paxos即服务这样的服务，虽然客户不会直接要求，但会从中受益匪浅。

关于主人翁精神，作者认为它过于狭隘，主张考虑整个技术生态系统，而不仅仅是亚马逊的利益。虽然有些亚马逊员工确实做到了这一点，但公司内部的各自为政往往阻碍了甚至代表整个公司行事的既定目标。

关于行动偏好，作者承认速度的重要性，但也警告不要推出半生不熟的服务，这会损害客户的信任。他们主张高层领导应该持有“不行动偏好”，建议设立“服务质量把关人”，他们可以否决不符合最高标准的发布，类似于现有的招聘“质量把关人”。

最后，作者敦促亚马逊倾听外部视角，比如AWS英雄们的观点，认为建设性的批评源于关心和希望亚马逊变得更好的愿望。

---

## 52. 苹果已从欧洲的 AltStore PAL 下架 iPhone 种子下载应用。

**原文标题**: Apple pulls iPhone torrent app from AltStore PAL in Europe

**原文链接**: [https://www.theverge.com/news/767344/apple-removes-itorrent-altstore-pal-ios-marketplace](https://www.theverge.com/news/767344/apple-removes-itorrent-altstore-pal-ios-marketplace)

苹果已将 iTorrent 应用从 AltStore PAL 下架，后者是欧盟地区的替代 iOS 应用商店。此举意味着开发者 Daniil Vinogradov 现在被禁止在替代 iOS 商店上分发应用，因为苹果撤销了他的分发权限。

苹果发言人 Peter Ajemian 表示，下架的原因是为了遵守各个司法管辖区与政府制裁相关的规定，而非禁止种子下载本身。此事已告知开发者。

这一情况凸显了苹果持续控制应用的能力，即便这些应用是在其官方 App Store 之外分发的，尽管欧盟的《数字市场法案》旨在促进更大的应用自由。Vinogradov 此前表示，苹果在没有警告或解释的情况下，从 iTorrent 的开发者门户中移除了替代分发功能。

---

## 53. 永恒的斗争

**原文标题**: Eternal Struggle

**原文链接**: [https://yoavg.github.io/eternal/](https://yoavg.github.io/eternal/)

文章《永恒的斗争》似乎是一篇非常短且不完整的作品。从标题和仅有的一行文字“更换背景”判断，这篇文章可能关于一个以持续冲突和不断战斗为特征的主题。“永恒的斗争”暗示了一个普遍、持久和根本性的主题，可能涉及对立的力量。

“更换背景”这句话可能有几种解释：

*   **字面意思：** 它是网站或文档的技术注释，表明需要更改视觉背景。这将使文章本身不完整，并且没有传达太多含义。
*   **比喻意义：** 它是一个隐喻，表明要理解或解决永恒的斗争，必须从根本上转变视角、假设或看待斗争的背景。这将是一个更深刻的，尽管仍然模糊的解释。

在没有更多背景信息的情况下，很难确定《永恒的斗争》的具体主题。它可能与政治冲突、内心挣扎、哲学辩论、善与恶的斗争或任何持续的斗争有关。“更换背景”的注释暗示需要不同的方法或观点来充分理解这场斗争。

---

## 54. CocoaPods trunk 只读计划

**原文标题**: CocoaPods trunk read-only plan

**原文链接**: [https://blog.cocoapods.org/CocoaPods-Specs-Repo/](https://blog.cocoapods.org/CocoaPods-Specs-Repo/)

以下是基于Specs仓库将被设置为只读的理解，对CocoaPods trunk只读计划的总结：

CocoaPods博客宣布了对CocoaPods Specs仓库的一项重大变更，将其迁移到只读状态。 实施此变更旨在解决与该仓库相关的日益增长的规模和性能问题，这些问题已成为CocoaPods用户的瓶颈。

核心问题在于，主要的Specs仓库包含所有pod的所有版本，从而导致仓库庞大，克隆和更新速度缓慢。 为了缓解这种情况，CocoaPods正在转向一种更加分散和高效的方法。

要点包括：

*   **Specs仓库变为只读：** 不再向主要的Specs仓库进行新的提交。
*   **过渡到基于CDN的Specs仓库：** CocoaPods鼓励开发人员使用CDN托管的Specs仓库，这些仓库可提供更快，更可扩展的pod规范访问。 这些CDN仓库仅包含用户需要的特定pod和版本。
*   **新的pod/版本需要创建/使用基于CDN的仓库：** 要使新的pod或版本可用，维护者将需要创建/使用基于CDN的仓库。 他们不能再直接推送到主仓库。
*   **改善的性能和可伸缩性：** 由于基于CDN的仓库规模更小，效率更高，因此此更改将大大加快CocoaPods操作（安装，更新等）。
*   **社区过渡：** CocoaPods团队了解此更改会影响社区，并致力于通过提供用于迁移到基于CDN的仓库的工具，文档和支持，使这种过渡尽可能顺利。 这包括创建和管理私有Specs仓库的指南。

---

## 55. 美国需要严格的评分标准

**原文标题**: America Needs Tough Grading

**原文链接**: [https://www.wsj.com/opinion/america-needs-tough-grading-educaiton-learning-students-98fa87d5](https://www.wsj.com/opinion/america-needs-tough-grading-educaiton-learning-students-98fa87d5)

无法访问文章链接。

---

## 56. 史蒂夫·鲍尔默访谈

**原文标题**: Steve Ballmer Interview

**原文链接**: [https://www.acquired.fm/episodes/the-steve-ballmer-interview](https://www.acquired.fm/episodes/the-steve-ballmer-interview)

本文总结了对微软前CEO史蒂夫·鲍尔默的采访，内容关于他在该公司任职的34年。鲍尔默回顾了微软的历史，从他认为至关重要的IBM DOS交易开始。他描述了当时IBM的主导地位，以及微软如何获得并授权DOS操作系统。他指出与IBM谈判达成非独家协议的重要性。鲍尔默还讨论了微软企业业务的发展，强调了其成功。他承认错失了消费者市场的机会。鲍尔默对Microsoft Office和M365感到自豪，他认为它们对企业的成功至关重要，同时认为它们既是消费产品也是企业产品。采访还涉及鲍尔默持有微软股票的投资策略，自从他离开公司以来，这大大增加了他的净资产。他还简要讨论了他的其他爱好，洛杉矶快船队和英图伊特穹顶。

---

## 57. 人工智能无人机蜂群已进入战场

**原文标题**: AI-Powered Drone Swarms Have Now Entered the Battlefield

**原文链接**: [https://www.wsj.com/world/ai-powered-drone-swarms-have-now-entered-the-battlefield-2cab0f05](https://www.wsj.com/world/ai-powered-drone-swarms-have-now-entered-the-battlefield-2cab0f05)

**概要：**

《华尔街日报》文章“人工智能无人机蜂群已进入战场”探讨了无人机蜂群在现代战争中日益增长的应用和影响，尤其强调了其最近在俄罗斯和乌克兰冲突中的部署。这些并非简单的遥控无人机，而是通常由人工智能驱动的系统，能够自主导航、识别目标和协同攻击。

文章强调，这些无人机蜂群代表了军事技术的重大进步。它们凭借数量优势压倒防御、在GPS受限环境下运行以及适应不断变化的战场条件的能力，构成了一种强大的威胁。此外，与传统军事装备相比，生产和部署这些无人机的成本相对较低，使其更易于被更广泛的行为者所获取。

文章指出了人工智能在战争中日益增长的应用所引发的伦理和战略担忧。对于平民伤亡的责任、局势升级的可能性以及区分战斗人员和非战斗人员的难度等问题浮出水面。这些无人机蜂群的开发和部署也被视为加速了全球自主武器系统的军备竞赛，对国际安全可能产生长期影响。文章指出，目前的国际法规不足以应对这种快速发展的技术所带来的挑战。

---

## 58. 有效学习：知识构建法则 (1999)

**原文标题**: Effective learning: Rules of formulating knowledge (1999)

**原文链接**: [https://www.supermemo.com/en/blog/twenty-rules-of-formulating-knowledge](https://www.supermemo.com/en/blog/twenty-rules-of-formulating-knowledge)

这篇题为《有效学习：知识构建规则(1999)》的文章，是关于SuperMemo学习软件的简短公告。该公告日期为2015年12月4日，来源于SuperMemo.com。

公告的核心信息是关于SuperMemo.com中导入和导出功能的“请求征集”。声明他们最近收到了关于这些功能的咨询。

因此，该公告的主要目的是征集用户对SuperMemo.com学习平台中导入和导出功能工作方式的反馈和请求。标题暗示了更广泛的文章，该文章可能未包含，讨论了与知识构建相关的有效学习策略，可能为该软件的目的提供背景。然而，这个特定的片段只关注导入/导出请求。

---

## 59. 聊天机器人和人工智能已在改变孩子们的课堂

**原文标题**: Chatbots and AI Are Already Transforming Kids' Classrooms

**原文链接**: [https://www.bloomberg.com/news/features/2025-09-01/what-artificial-intelligence-looks-like-in-america-s-classrooms](https://www.bloomberg.com/news/features/2025-09-01/what-artificial-intelligence-looks-like-in-america-s-classrooms)

无法访问文章链接。

---

## 60. 象棋中的复杂性是什么？

**原文标题**: What Is Complexity in Chess?

**原文链接**: [https://lichess.org/@/Toadofsky/blog/what-is-complexity/pKo1swFh](https://lichess.org/@/Toadofsky/blog/what-is-complexity/pKo1swFh)

Toadofsky 对彭大卫 FM 的论文“象棋复杂性度量”一文进行了评论，该论文旨在利用 Stockfish 评估的中心兵损失来量化象棋复杂性。Toadofsky 对论文的核心命题表示怀疑：即将复杂性简化为基于中心兵损失的单一、可转移的度量标准，并实时使用该指标来确定局面难度。

他对从这些命题中得出的各种结论的逻辑有效性提出质疑，认为大多数结论需要进一步研究。虽然他同意复杂性信息可以丰富观赛和赛后分析，但他对非战术谜题生成、自动开局准备、训练材料开发、诊断性象棋考试、个性化 AI 对手以及定制开局以利用对手的复杂性偏好等方面的说法提出了挑战。

Toadofsky 强调了神经网络象棋引擎（Stockfish-NNUE）的进步，建议需要根据较旧的 Stockfish 版本更新结论。他还指出了评估中残局缩放的问题。

尽管持批评态度，Toadofsky 对该研究关注不同技能水平玩家的不同难度等级印象深刻。他建议改进，例如纳入分段的 Stockfish 评估（材料、兵结构等）、WDL 统计数据、Stockfish-NNUE 数据、建模将军和剩余时间，以及纳入人与引擎的对局。他希望复杂性度量最终能够实现，但不要首先被作弊者使用。

---

## 61. ABC编程语言

**原文标题**: The ABC Programming Language

**原文链接**: [https://homepages.cwi.nl/~steven/abc/](https://homepages.cwi.nl/~steven/abc/)

ABC编程语言是一种交互式的、用户友好的语言，旨在成为BASIC的更佳替代品。它强调易于学习和使用，适用于初学者和经验丰富的程序员。ABC源于编程的任务分析，拥有简洁的语法和强大的功能。

该语言的关键特性包括：少量的数据类型、无需显式声明的强类型、数据大小没有人为限制、顶层编程支持以及基于缩进的嵌套，从而产生紧凑的代码（通常比等效的Pascal或C程序小得多）。

ABC环境在各种操作（命令执行、编辑、输入）中提供一致的用户界面，消除了文件管理的需求（过程/变量持久存在），并具有通用的撤销机制。

本文提供了各种平台（PC、Unix、Mac、Raspberry Pi）的实现链接，以及像《ABC程序员手册》这样的在线资源，和详细介绍该语言设计和使用的出版物。它还强调了ABC对Python设计的影响。最后，它提到了过去新闻通讯的可用性并提供了联系方式。

---

## 62. 如何与AI吹捧者争论

**原文标题**: How to Argue with an AI Booster

**原文链接**: [https://www.wheresyoured.at/how-to-argue-with-an-ai-booster/](https://www.wheresyoured.at/how-to-argue-with-an-ai-booster/)

本文批判了人工智能吹捧之风，认为许多人工智能支持者并非出于对该技术的真正理解或实际应用，而是受象征性忠诚的驱使。作者认为，人工智能吹捧者经常诉诸含糊不清的说法、精神操控和受害者叙事来捍卫自己的立场，无视人工智能影响有限和实际失败的证据。

文章引用了麻省理工学院最近的一项研究，该研究表明，公司中 95% 的生成式人工智能试点项目未能产生投资回报，并揭穿了常见的人工智能神话，例如人工智能取代工作岗位和改变业务。作者还批评吹捧者将人工智能与互联网和智能手机等过去的科技进步进行有缺陷的比较。

一个关键论点是，人工智能吹捧者往往缺乏对人工智能能力的全面了解，却坚持认为它具有颠覆性的潜力，但没有提供具体的例子。作者指责他们居高临下，散布虚假信息，其动机是渴望感到优越和获得认可。

文章为读者提供了一个“目录”，以便快速参考具体的论点和吹捧者的“妙语”，从而使他们能够有效地挑战人工智能吹捧的叙事，并突出该技术的局限性。最终，作者认为，生成式人工智能并未实现承诺的变革性变化，并且其许多问题无法简单地通过“学习”来解决。

---

## 63. 蒂尔伯里变电站的英国最大电池储能设施

**原文标题**: UK's largest battery storage facility at Tilbury substation

**原文链接**: [https://www.nationalgrid.com/national-grid-connects-uks-largest-battery-storage-facility-tilbury-substation](https://www.nationalgrid.com/national-grid-connects-uks-largest-battery-storage-facility-tilbury-substation)

国家电网已将其位于埃塞克斯郡蒂尔伯里变电站连接至英国最大的电池储能系统（BESS），即300兆瓦的瑟罗克储能项目。该项目由Statera Energy开发，拥有600兆瓦时的容量，可为多达68万户家庭供电，并通过储存多余的清洁能源以供日后使用来平衡电力供需。

此次连接标志着蒂尔伯里场地从煤炭到可再生能源的象征性转变，该场地此前曾为燃煤发电站提供服务。国家电网通过新的保护和控制系统加强了变电站，以处理电池的负载。

国家电网的John Twomey强调了电池储能在英国清洁能源转型中的重要作用。 Statera Energy首席执行官Tom Vernon强调了BESS容量对于在可再生能源发电量低时支持电网的重要性。

国家电网还在努力将Statera的450兆瓦瑟罗克灵活发电设施连接到同一变电站。该项目紧随最近在肯特郡启动的373兆瓦克利夫山太阳能园区之后，国家电网已将其连接到克利夫山变电站。这些项目反映了可再生能源及其支持基础设施日益增长的重要性。

---

## 64. 印度价值十亿美元的电子垃圾帝国

**原文标题**: India's billion-dollar e-waste empire

**原文链接**: [https://restofworld.org/2025/india-e-waste-recycling-electronics/](https://restofworld.org/2025/india-e-waste-recycling-electronics/)

Yashraj Sharma的文章《印度十亿美元的电子垃圾帝国》深入探讨了印度电子垃圾回收的复杂且往往危险的现实。在蓬勃发展的电子行业的推动下，该行业的价值达15亿美元，但估计有100万人的劳动力中，95%的人在非正规部门工作。这些工人在拆解电子产品以回收黄金和铜等有价值的材料时，面临着微薄的工资、危险的工作条件以及接触有毒物质的风险。

这篇文章突出了非正规部门与新兴正规部门之间的鲜明对比。非正规部门以德里Khatta垃圾场为例，该垃圾场由阿西夫·马利克等有权势的人物控制；正规部门则以Recyclekaro等公司为代表。Khatta体现了像努尔这样的工人所面临的困境，他在危险的条件下工作，收入微薄，并且健康受到影响。

新的政府法规旨在使该行业正规化，强制要求电子产品生产商向回收商支付适当处置费用，并达到回收配额。然而，这些政策已经使Recyclekaro等公司受益，但正面临着科技制造商的抵制，他们认为这些政策增加了合规成本。

这篇文章强调了印度大规模电子垃圾问题带来的环境问题和金融机遇。它认为，印度在电子垃圾行业正规化方面的成功或失败，可以为全球电子垃圾管理提供一个模式或警告。非正规部门的持续主导地位带来了环境和健康风险，而正规化则有望实现更可持续和负责任的方法。

---

## 65. 面向内存专用化：长期和短期RAM案例

**原文标题**: Towards Memory Specialization: A Case for Long-Term and Short-Term RAM

**原文链接**: [https://arxiv.org/abs/2508.02992](https://arxiv.org/abs/2508.02992)

迈向内存专用化：一种关于长短期RAM的案例，本文认为应从传统内存层级结构转向专用内存架构。包括李培景在内的作者提出，SRAM和DRAM扩展的停滞导致内存成为主要的成本因素，因此有必要探索能够根据特定应用访问模式优化性能的替代内存类型。

核心思想是引入两种新的内存类别，并提供明确的操作系统支持：长期RAM (LtRAM) 和短期RAM (StRAM)。LtRAM将针对具有长生命周期的读取密集型数据进行优化，而StRAM将针对具有短生命周期的频繁访问的瞬态数据进行设计。

本文探讨了可能实现这些内存类别的潜在底层设备技术，以及如何将它们集成到现有系统中。它还强调了实现更高效和可扩展的计算系统以满足未来需求所需的关键研究挑战。本质上，作者提倡一种利用专用内存类型的非分层内存系统，以克服当前SRAM和DRAM技术的局限性。

---

## 66. 谷歌AI概述编造了一个关于我的离奇故事。

**原文标题**: Google AI Overview made up an elaborate story about me

**原文链接**: [https://bsky.app/profile/bennjordan.bsky.social/post/3lxojrbessk2z](https://bsky.app/profile/bennjordan.bsky.social/post/3lxojrbessk2z)

生成摘要时出错

---

## 67. Nintendo Switch 2 Dock USB-C Compatibility

**原文标题**: Nintendo Switch 2 Dock USB-C Compatibility

**原文链接**: [https://www.lttlabs.com/blog/2025/08/30/nintendo-switch-2-dock](https://www.lttlabs.com/blog/2025/08/30/nintendo-switch-2-dock)

生成摘要时出错

---

## 68. Tetris is NP-hard even with O(1) rows or columns (2020) [pdf]

**原文标题**: Tetris is NP-hard even with O(1) rows or columns (2020) [pdf]

**原文链接**: [https://martindemaine.org/papers/ThinTetris_JIP/paper.pdf](https://martindemaine.org/papers/ThinTetris_JIP/paper.pdf)

生成摘要时出错

---

## 69. 2025年第二季度搜索引擎引荐报告

**原文标题**: Search engine referral report for 2025 Q2

**原文链接**: [https://radar.cloudflare.com/reports/search-engine-market-share-2025-q2](https://radar.cloudflare.com/reports/search-engine-market-share-2025-q2)

无法访问文章链接。

---

## 70. A Unique, High-Tech (Family) Computer

**原文标题**: A Unique, High-Tech (Family) Computer

**原文链接**: [https://nicole.express/2025/a-computer-in-your-home.html](https://nicole.express/2025/a-computer-in-your-home.html)

生成摘要时出错

---

## 71. Preserving Order in Concurrent Go Apps: Three Approaches Compared

**原文标题**: Preserving Order in Concurrent Go Apps: Three Approaches Compared

**原文链接**: [https://destel.dev/blog/preserving-order-in-concurrent-go](https://destel.dev/blog/preserving-order-in-concurrent-go)

生成摘要时出错

---

## 72. Reports of Gmail security issue are inaccurate

**原文标题**: Reports of Gmail security issue are inaccurate

**原文链接**: [https://blog.google/products/workspace/gmail-security-protections/](https://blog.google/products/workspace/gmail-security-protections/)

生成摘要时出错

---

## 73. The Tragic End of Natalia Nagovitsyna's Ordeal on Pobeda Peak

**原文标题**: The Tragic End of Natalia Nagovitsyna's Ordeal on Pobeda Peak

**原文链接**: [https://explorersweb.com/tragic-end-of-natalia-nagovitsynas-ordeal-on-pobeda-peak/](https://explorersweb.com/tragic-end-of-natalia-nagovitsynas-ordeal-on-pobeda-peak/)

生成摘要时出错

---

## 74. I Was Wrong About Data Center Water Consumption

**原文标题**: I Was Wrong About Data Center Water Consumption

**原文链接**: [https://www.construction-physics.com/p/i-was-wrong-about-data-center-water](https://www.construction-physics.com/p/i-was-wrong-about-data-center-water)

生成摘要时出错

---

## 75. Animated Text in Voxel Space

**原文标题**: Animated Text in Voxel Space

**原文链接**: [https://www.splats.com/watch/635](https://www.splats.com/watch/635)

生成摘要时出错

---

## 76. An adventure in writing compatible systems

**原文标题**: An adventure in writing compatible systems

**原文链接**: [https://turso.tech/blog/an-adventure-in-writing-compatible-systems](https://turso.tech/blog/an-adventure-in-writing-compatible-systems)

生成摘要时出错

---

## 77. Detecting and countering misuse of AI

**原文标题**: Detecting and countering misuse of AI

**原文链接**: [https://www.anthropic.com/news/detecting-countering-misuse-aug-2025](https://www.anthropic.com/news/detecting-countering-misuse-aug-2025)

生成摘要时出错

---

## 78. Desert Graves (2021)

**原文标题**: Desert Graves (2021)

**原文链接**: [https://www.desertmountaineer.com/2021/08/06/graves/](https://www.desertmountaineer.com/2021/08/06/graves/)

生成摘要时出错

---

## 79. The Wetware Crisis: The Thermocline of Truth (2008)

**原文标题**: The Wetware Crisis: The Thermocline of Truth (2008)

**原文链接**: [https://brucefwebster.com/2008/04/15/the-wetware-crisis-the-themocline-of-truth/](https://brucefwebster.com/2008/04/15/the-wetware-crisis-the-themocline-of-truth/)

生成摘要时出错

---

## 80. “This telegram must be closely paraphrased before being communicated to anyone”

**原文标题**: “This telegram must be closely paraphrased before being communicated to anyone”

**原文链接**: [https://history.stackexchange.com/questions/79371/this-telegram-must-be-closely-paraphrased-before-being-communicated-to-anyone](https://history.stackexchange.com/questions/79371/this-telegram-must-be-closely-paraphrased-before-being-communicated-to-anyone)

生成摘要时出错

---

## 81. Monitoring bands during the Norwegian national day parade – Using fiberoptics

**原文标题**: Monitoring bands during the Norwegian national day parade – Using fiberoptics

**原文链接**: [https://www.nature.com/articles/s41598-025-97017-z](https://www.nature.com/articles/s41598-025-97017-z)

生成摘要时出错

---

## 82. 32GB of RAM on track to become the new majority for gamers

**原文标题**: 32GB of RAM on track to become the new majority for gamers

**原文链接**: [https://www.tomshardware.com/pc-components/ram/32gb-of-ram-on-track-to-become-the-new-majority-for-gamers-steam-survey-indicates-shift-could-occur-before-the-end-of-the-year](https://www.tomshardware.com/pc-components/ram/32gb-of-ram-on-track-to-become-the-new-majority-for-gamers-steam-survey-indicates-shift-could-occur-before-the-end-of-the-year)

生成摘要时出错

---

## 83. A Crack in the Cosmos

**原文标题**: A Crack in the Cosmos

**原文链接**: [https://drb.ie/articles/a-crack-in-the-cosmos/](https://drb.ie/articles/a-crack-in-the-cosmos/)

生成摘要时出错

---

## 84. Zfsbackrest: Pgbackrest style encrypted backups for ZFS filesystems

**原文标题**: Zfsbackrest: Pgbackrest style encrypted backups for ZFS filesystems

**原文链接**: [https://github.com/gargakshit/zfsbackrest](https://github.com/gargakshit/zfsbackrest)

生成摘要时出错

---

## 85. Neptune Balls

**原文标题**: Neptune Balls

**原文链接**: [https://www.bbc.com/future/article/20250901-why-plastic-filled-neptune-balls-are-washing-up-on-beaches](https://www.bbc.com/future/article/20250901-why-plastic-filled-neptune-balls-are-washing-up-on-beaches)

生成摘要时出错

---

## 86. Git for Music – Using Version Control for Music Production (2023)

**原文标题**: Git for Music – Using Version Control for Music Production (2023)

**原文链接**: [https://grechin.org/2023/05/06/git-and-reaper.html](https://grechin.org/2023/05/06/git-and-reaper.html)

生成摘要时出错

---

## 87. The time picker on the iPhone's alarm app isn't circular, it's just a long list

**原文标题**: The time picker on the iPhone's alarm app isn't circular, it's just a long list

**原文链接**: [https://old.reddit.com/r/interestingasfuck/comments/1n5lztw/the_time_picker_on_the_iphones_alarm_app_isnt/](https://old.reddit.com/r/interestingasfuck/comments/1n5lztw/the_time_picker_on_the_iphones_alarm_app_isnt/)

生成摘要时出错

---

## 88. Trade in War

**原文标题**: Trade in War

**原文链接**: [https://news.mit.edu/2025/why-countries-trade-each-other-while-fighting-mariya-grinberg-book-0828](https://news.mit.edu/2025/why-countries-trade-each-other-while-fighting-mariya-grinberg-book-0828)

生成摘要时出错

---

## 89. Using JWT to establish a trusted context for Row Level Security

**原文标题**: Using JWT to establish a trusted context for Row Level Security

**原文链接**: [https://vondra.me/posts/using-jwt-to-establish-trusted-context-for-rls/](https://vondra.me/posts/using-jwt-to-establish-trusted-context-for-rls/)

生成摘要时出错

---

## 90. Thunk: Build Rust program to support Windows XP, Vista and more

**原文标题**: Thunk: Build Rust program to support Windows XP, Vista and more

**原文链接**: [https://github.com/felixmaker/thunk](https://github.com/felixmaker/thunk)

生成摘要时出错

---

## 91. A review of Nim 2: The good and bad with example code

**原文标题**: A review of Nim 2: The good and bad with example code

**原文链接**: [https://miguel-martin.com/blog/nim2-review](https://miguel-martin.com/blog/nim2-review)

生成摘要时出错

---

## 92. Corruption and Control: Turkmenistan turned internet censorship into a business

**原文标题**: Corruption and Control: Turkmenistan turned internet censorship into a business

**原文链接**: [https://blog.torproject.org/Corruption-Control-Turkmenistan-internet-censorship-business/](https://blog.torproject.org/Corruption-Control-Turkmenistan-internet-censorship-business/)

生成摘要时出错

---

## 93. Can You Develop Film in a Jägerbomb?

**原文标题**: Can You Develop Film in a Jägerbomb?

**原文链接**: [https://petapixel.com/2025/08/04/can-you-develop-film-in-a-jagerbomb/](https://petapixel.com/2025/08/04/can-you-develop-film-in-a-jagerbomb/)

生成摘要时出错

---

## 94. Cognitive load is what matters

**原文标题**: Cognitive load is what matters

**原文链接**: [https://github.com/zakirullin/cognitive-load](https://github.com/zakirullin/cognitive-load)

生成摘要时出错

---

## 95. The Qweremin

**原文标题**: The Qweremin

**原文链接**: [https://www.linusakesson.net/qweremin/index.php](https://www.linusakesson.net/qweremin/index.php)

生成摘要时出错

---

## 96. Scientists stunned as strange islands & hidden springs appear in Great Salt Lake

**原文标题**: Scientists stunned as strange islands & hidden springs appear in Great Salt Lake

**原文链接**: [https://www.sciencedaily.com/releases/2025/08/250831010526.htm](https://www.sciencedaily.com/releases/2025/08/250831010526.htm)

生成摘要时出错

---

## 97. Bash Prompts Collection

**原文标题**: Bash Prompts Collection

**原文链接**: [https://www.gilesorr.com/bashprompt/prompts/](https://www.gilesorr.com/bashprompt/prompts/)

生成摘要时出错

---

## 98. Bayes, Bits and Brains

**原文标题**: Bayes, Bits and Brains

**原文链接**: [https://bayesbitsbrains.github.io/](https://bayesbitsbrains.github.io/)

生成摘要时出错

---

## 99. Show HN: Simple modenized .NET NuGet server reached RC

**原文标题**: Show HN: Simple modenized .NET NuGet server reached RC

**原文链接**: [https://github.com/kekyo/nuget-server](https://github.com/kekyo/nuget-server)

生成摘要时出错

---

## 100. Plastic Before Plastic: How gutta-percha shaped the 19th century

**原文标题**: Plastic Before Plastic: How gutta-percha shaped the 19th century

**原文链接**: [https://worldhistory.substack.com/p/plastic-before-plastic](https://worldhistory.substack.com/p/plastic-before-plastic)

生成摘要时出错

---

