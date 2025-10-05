# Hacker News 热门文章摘要 (2025-10-05)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 语言无关编程：为何你可能仍然需要代码

**原文标题**: Language Agnostic Programming: Why you may still need code

**原文链接**: [https://joaquimrocha.com/2025/08/31/language-agnostic-programming-why-you-may-still-need-code/](https://joaquimrocha.com/2025/08/31/language-agnostic-programming-why-you-may-still-need-code/)

无法访问文章链接。

---

## 2. Show HN: Pyscn – 专为有感觉的程序员打造的Python代码质量分析器

**原文标题**: Show HN: Pyscn – Python code quality analyzer for vibe coders

**原文链接**: [https://github.com/ludo-technologies/pyscn](https://github.com/ludo-technologies/pyscn)

Pyscn 是一款 Python 代码质量分析工具，专为使用 Cursor、Claude 或 ChatGPT 等 AI 编码助手的开发者设计。它通过结构分析来提高代码可维护性。主要功能包括基于 CFG 的死代码检测、使用 APTED 和 LSH 的克隆检测、耦合度指标 (CBO) 以及圈复杂度分析。它使用 Go 和 tree-sitter 构建，实现快速分析（100,000+ 行/秒）。

该工具提供两个主要命令：`pyscn analyze` 用于生成 HTML 报告的全面分析，以及 `pyscn check` 用于快速、CI 友好的质量门禁。配置通过 `.pyscn.toml` 或 `pyproject.toml` 文件处理，允许自定义分析阈值和输出目录。

推荐使用 `pipx install pyscn` 进行安装，但也提供其他方法，如从源代码构建或使用 `go install`。本文档提供了使用 GitHub Actions 进行 CI/CD 集成的示例。它重点介绍了文档资源，包括开发指南、架构概述和测试信息。Pyscn 采用 MIT 许可证。

---

## 3. 基于监督学习框架的RLVR隐式Actor-Critic耦合

**原文标题**: Implicit Actor Critic Coupling via a Supervised Learning Framework for RLVR

**原文链接**: [https://arxiv.org/abs/2507.15855](https://arxiv.org/abs/2507.15855)

该arXiv文章于2025年7月21日提交，2025年9月30日最后修订，题为“使用模型无关的验证与精炼流程赢得2025年IMO金牌”，作者为黄一辰和杨林F.，探讨了大型语言模型（LLM）在解决国际数学奥林匹克（IMO）问题中的应用。作者承认，虽然LLM在许多数学基准测试中表现出熟练的水平，但它们经常难以应对IMO中发现的复杂和新颖的问题。

核心贡献是开发了一种模型无关的验证与精炼流程，旨在提高LLM在IMO级别问题上的表现。该流程利用精心设计的提示来引导LLM完成解决问题的过程。

作者在2025年IMO上测试了他们的流程，使用了Gemini 2.5 Pro、Grok-4和GPT-5。他们发现该流程显著提高了所有三个模型的准确性，使其能够正确解决6道问题中的5道，达到约85.7%的准确率。与仅从32个生成的解决方案中选择最佳方案获得的31.6%（Gemini 2.5 Pro）、21.4%（Grok-4）和38.1%（GPT-5）的基线准确率相比，这是一个显著的提高。

该论文的结论是，增强人工智能在复杂任务中的推理能力不仅需要开发更强大的基础模型，还需要设计有效的方法来充分发挥其潜力。所提出的验证与精炼流程是朝着这个方向迈出的一个有希望的方法。

---

## 4. 莉娜·可汗我早就说过：收购动视暴雪损害玩家和开发者利益

**原文标题**: Lina Khan I told you so: The Activision-Blizzard buyout harms gamers&developers

**原文链接**: [https://www.pcgamer.com/gaming-industry/as-microsoft-lays-off-thousands-and-jacks-up-game-pass-prices-former-ftc-chair-says-i-told-you-so-the-activision-blizzard-buyout-is-harming-both-gamers-and-developers/](https://www.pcgamer.com/gaming-industry/as-microsoft-lays-off-thousands-and-jacks-up-game-pass-prices-former-ftc-chair-says-i-told-you-so-the-activision-blizzard-buyout-is-harming-both-gamers-and-developers/)

本文探讨了微软收购动视暴雪后的影响，强调了对玩家和开发者潜在的负面后果。 前联邦贸易委员会主席莉娜·汗指出，裁员、涨价和游戏取消等事件证明了联邦贸易委员会最初的担忧，即此次收购将损害竞争。

文章详细介绍了微软收购后的行动，包括动视暴雪和 Xbox 的裁员（数千人）、项目取消以及 Game Pass Ultimate 和 PC Game Pass 的价格上涨。 尽管微软和动视保证合并将使消费者和工人受益，并促进竞争，但这些事态发展依然发生了。

文章指出，联邦贸易委员会在汗的领导下，于 2022 年提起诉讼，试图阻止该交易，理由是该交易可能会减少竞争并造成垄断。 尽管该交易于 2023 年 10 月在联邦贸易委员会的法律行动 pending 的情况下完成，但随后的事件似乎验证了联邦贸易委员会早期的担忧。

虽然汗在被取代为联邦贸易委员会主席后，目前的评论缺乏监管权力，但文章作者认为，鉴于事态的发展，她的评估是合理的“我早就告诉你了”。文章最后附有网站上其他与游戏相关内容的链接。

---

## 5. GoboLinux 017.01 – 火炬传递

**原文标题**: GoboLinux 017.01 – Passing the Torch

**原文链接**: [https://gobolinux.org//news/119.html](https://gobolinux.org//news/119.html)

GoboLinux 发布 017.01 版本，这是自上次 ISO 版本发布五年后推出的一个错误修复更新。更重要的是，GoboLinux 的创始人及过去 25 年来的管理者 Hisham Muhammad 即将卸任，Philip Pok (@nuc1eon) 将接管该项目。

公告肯定了 Hisham 在将 GoboLinux 塑造成挑战传统 Unix 概念的创新发行版中的关键作用。同时感谢 Lucas Correia Villa Real，他与 Hisham 一起维护该发行版直到 2021 年 6 月。

本次发布表达了对 Philip Pok 领导下 GoboLinux 未来发展方向的兴奋之情，并感谢参与此次发布的众多贡献者，包括 Sage I. Hendricks、Anto、Rune Morling、@TheBitStick、Jean-Michel T.Dydak 和 Samuel Dionne-Riel。 详细信息请参阅发行说明，ISO 可以从提供的链接下载。

---

## 6. 使用ARM SIMD的86 GB/s 位打包 (单线程)

**原文标题**: 86 GB/s bitpacking with ARM SIMD (single thread)

**原文链接**: [https://github.com/ashtonsix/perf-portfolio/tree/main/bytepack](https://github.com/ashtonsix/perf-portfolio/tree/main/bytepack)

此GitHub仓库“perf-portfolio”展示了一个优化的位压缩实现，在使用ARM SIMD的单线程上实现了 86 GB/s 的吞吐量。“86 GB/s 位压缩，基于 ARM SIMD (单线程)”的标题清晰地表明了该项目的重点及其令人印象深刻的性能指标。作者“ashtonsix”已将该仓库公开，允许其他人访问并可能利用或学习该位压缩代码。该仓库已获得一定关注，拥有 2 个 fork 和 26 个 star 表明了社区的兴趣。本质上，这是一个代码仓库，展示了用于 ARM 架构的高性能位压缩实现，利用 SIMD 指令在单个核心上实现可观的数据处理速度。

---

## 7. 如果芝加哥大学都不捍卫人文科学，谁会捍卫？

**原文标题**: If the University of Chicago Won't Defend the Humanities, Who Will?

**原文链接**: [https://www.theatlantic.com/culture/archive/2025/08/university-chicago-humanities-doctorate/684004/](https://www.theatlantic.com/culture/archive/2025/08/university-chicago-humanities-doctorate/684004/)

泰勒·奥斯汀·哈珀在《大西洋月刊》上发表的文章《如果芝加哥大学都不捍卫人文学科，谁来捍卫？》探讨了芝加哥大学近期决定减少或冻结包括古典学、艺术史和英语在内的几个人文学科博士招生所带来的影响。这一决定引发了学术界的愤怒和难以置信，他们认为芝加哥大学是人文研究的堡垒。

该大学以“不确定性”和“不断变化的财政现实”（包括63亿美元的债务）为由，解释了削减的原因。然而，批评者认为这是一种玩世不恭的举动，旨在将资源从人文学科转移到 STEM 领域。教授们担心，如果大学不支持研究生的继续培养，将导致专业知识的丧失以及整个研究领域的潜在消失。他们认为，无论就业市场压力如何，人文主义者在保存和传播文化知识方面都发挥着关键作用。

这篇文章突出了这一举动与人文学科在保存文化和知识、抵制纯粹经济考量方面的公认作用之间的对比。为了应对最初分配不均的削减，各人文学科系主任集体要求暂停所有院系的招生，以防止某些领域优先于其他领域。虽然这导致了整个院系暂停博士招生，但这仍然是一场苦乐参半的胜利，并没有解决更大的担忧：如果像芝加哥大学这样的大学放弃了对人文学科的承诺，这些学科的未来还有什么希望？作者最后担心，其他知名机构可能会效仿，进一步危及人文学科。

---

## 8. 个人数据存储，时机已到。

**原文标题**: Personal data storage is an idea whose time has come

**原文链接**: [https://blog.muni.town/personal-data-storage-idea/](https://blog.muni.town/personal-data-storage-idea/)

个人数据存储：正当其时

---

## 9. 巨型动物曾是南美洲猎人首选的猎物。

**原文标题**: Megafauna was the meat of choice for South American hunters

**原文链接**: [https://arstechnica.com/science/2025/10/ice-age-hunters-in-south-america-preferred-now-extinct-megafauna/](https://arstechnica.com/science/2025/10/ice-age-hunters-in-south-america-preferred-now-extinct-megafauna/)

本文探讨了一项最新研究，该研究表明，在冰河时代晚期，人类猎手在南美洲巨型动物群灭绝中发挥了重要作用。考古学家检查了阿根廷、智利和乌拉圭20个遗址的动物骨骼，这些遗址的历史可以追溯到灭绝事件（11600年前）之前。他们发现在其中15个遗址中，大部分被屠宰的骨骼都属于现在已灭绝的巨型动物群，如巨型树懒、巨型犰狳和大象的近亲。在其中13个遗址中，已灭绝的巨型动物群占发现的动物骨骼总数的80%以上。

这些发现挑战了先前关于气候变化是导致灭绝的唯一原因的假设。该研究认为，由于巨型动物群的体型和它们提供的卡路里回报，它们是首选猎物，正如“猎物选择模型”所解释的那样。从本质上讲，就狩猎努力与食物产量而言，已灭绝的巨型动物群提供了更多的“性价比”。

虽然之前的论点认为，由于缺乏确凿的证据，人类并未大量参与，但该研究认为，考古层有限的保存和混合歪曲了之前的数据。通过关注时间线清晰的遗址，研究人员发现人类活动与食用已灭绝的巨型动物群之间存在很强的相关性。该研究得出结论，人类猎手很可能处于南美洲巨型动物群灭绝“辩论的核心”。

---

## 10. 在框架笔记本电脑和磁盘上自托管S3中的10TB数据

**原文标题**: Self hosting 10TB in S3 on a framework laptop and disks

**原文链接**: [https://jamesoclaire.com/2025/10/05/self-hosting-10tb-in-s3-on-a-framework-laptop-disks/](https://jamesoclaire.com/2025/10/05/self-hosting-10tb-in-s3-on-a-framework-laptop-disks/)

作者成功地使用一台二手Framework笔记本电脑和一个JBOD（磁盘簇）外接盒搭建了一个自托管的S3存储方案，用于存储10TB的数据。由于AppGoblin的SDK追踪需要廉价存储，作者选择了ZFS进行文件系统管理，并使用Garage S3来实现S3兼容。

该设置运行了四个月，无需维护。作者欣慰地发现，系统在一段时间的闲置后仍然可以运行并准备好升级。操作系统和Garage S3都已成功更新，包括从v1到v2的主要版本升级。

作者承认ZFS与笔记本电脑和JBOD之间的USB连接可能是一种非常规用法。这最初在大量读写操作期间导致问题，但通过将SQLite元数据移动到笔记本电脑的内部存储来解决。总而言之，自托管的S3解决方案已被证明是可靠的，并且满足了作者对经济实惠的存储需求。

---

## 11. NFS四十周年：追忆太阳微系统公司的网络文件系统

**原文标题**: NFS at 40 – Remembering the Sun Microsystems Network File System

**原文链接**: [https://nfs40.online/](https://nfs40.online/)

本网站纪念Sun Microsystems网络文件系统(NFS)40周年，庆祝活动于2025年9月举行。它作为一个NFS相关资料的存储库，NFS自1983年诞生以来，一直是分布式计算机系统的基础技术。

本网站旨在收集与NFS相关的设计文档、规范、论文、标准、营销材料，甚至纪念品。这些资料分为四个部分：源代码和规范、NFS相关文档、先前和竞争性工作的文档以及照片。所有内容均可下载，除非另有说明。

本网站还提供了一个全面的NFS相关互联网RFC列表的链接。在提及nfsv4bat.org作为1995年之后NFS材料（尤其是Connectathon）的资源时，它提醒用户注意潜在的安全问题、缓慢的加载时间和不确定的维护。

本网站由Russel Berg、Russ Cox、Steve Kleiman等人贡献创建。Geoff Arnold维护本网站，并通过电子邮件欢迎评论和建议。

---

## 12. 四千年前的白蚁丘空间格局

**原文标题**: A 4k-year-old spatial pattern of termite mounds

**原文链接**: [https://www.cell.com/current-biology/fulltext/S0960-9822(18)31287-9](https://www.cell.com/current-biology/fulltext/S0960-9822(18)31287-9)

好的，我已阅读了来自提供的URL的文章“四千年前的白蚁丘空间格局”。以下是一个摘要：

这项研究调查了巴西北部干旱森林景观中白蚁丘的空间格局，揭示了一种非常一致且古老的有组织的 spatial distribution。研究人员分析了一片广阔的 landscape，上面点缀着大约 2 亿个*Syntermes dirus* 物种的白蚁丘。

通过广泛的实地调查、航空摄影和白蚁丘沉积物的放射性碳测年，研究人员发现证据表明，白蚁丘的空间排列非常规则，并且延伸到 23 万平方公里的广大区域。重要的是，这些土墩并非只是随机分布；它们表现出一种自组织的、相对均匀的间距，类似于六边形或蜂窝状的图案。

放射性碳测年表明，其中一些土墩已有 4000 年的历史，这表明这种空间格局已经维持了数千年。研究人员认为，这种空间组织是由白蚁群体之间对资源（主要是落叶层）的竞争驱动的。间距的规律性可能最大限度地提高资源获取，同时最大限度地减少领土重叠。

该研究强调了白蚁工程令人印象深刻的寿命和规模，以及生物相互作用（竞争）在塑造大规模景观格局中的作用。它证明了一个物种如何在大片区域和较长时期内显着改变和维持一个生态系统。这些发现对于理解社会性昆虫空间组织的生态和进化驱动因素，以及生物活动对景观动态的长期影响具有重要意义。

---

## 13. .NET 10 GC 的变化对开发者的意义

**原文标题**: What .NET 10 GC Changes Mean for Developers

**原文链接**: [https://roxeem.com/2025/09/30/what-net-10-gc-changes-mean-for-developers/](https://roxeem.com/2025/09/30/what-net-10-gc-changes-mean-for-developers/)

.NET 10 中的垃圾回收 (GC) 显著改进

本文探讨了 .NET 10 中垃圾回收 (GC) 的显著改进，强调了许多关于 .NET 内存管理的传统假设已经过时。这些改进可以通过运行时开关和新的优化行为，显著提高内存使用率和速度。

本文首先回顾了 .NET 垃圾回收的基本原理，包括分代回收（Gen 0、Gen 1、Gen 2 和 LOH）、GC 回收阶段（标记、重定位、压缩）以及 GC 模式（工作站 GC 与服务器 GC）。然后深入探讨了 .NET 中 GC 的演变过程，重点介绍了每个主要版本中所做的增强。

.NET 10 的主要变化包括：

*   **逃逸分析和栈分配：** 小型、生命周期短的对象现在可以在栈上分配，从而减少 GC 压力。
*   **DATAS（动态适应应用程序大小）：** 默认启用，DATAS 动态调整堆/GC 阈值以适应应用程序内存需求。
*   **区域大小/范围配置：** 允许调整内存区域大小，以降低开销或减少映射。
*   **委托和闭包优化：** 更多“非逃逸”委托被栈分配，从而减少开销。
*   **写屏障优化：** 消除不必要的写屏障，降低 CPU 使用率。
*   **去虚化和内联改进：** 更积极地优化常见集合操作。
*   **堆硬限制和 LOH 调优：** 为内存受限的环境（如容器）提供细粒度的控制。

本文解释了这些变化背后的原理，并提供了使用 `dotnet-counters` 等工具测量 GC 行为的指南。最后，它指出了在哪些情况下可能需要调整默认设置，特别是对于吞吐量敏感的应用程序、实时系统或遗留配置文件。强调在采用任何更改之前，彻底的基准测试至关重要。

---

## 14. 停止 Test-Ipv6.com 服务

**原文标题**: Retiring Test-Ipv6.com

**原文链接**: [https://retire.test-ipv6.com/](https://retire.test-ipv6.com/)

test-ipv6.com将于2025年12月关闭

test-ipv6.com的拥有者jfesler将于2025年12月停止该服务，以便重新分配家庭内部资源。该网站自2010年以来一直运营，是一个不产生收入的产品，需要大量工程、支持、设备和托管方面的投入。

要点：

*   **关闭日期：** test-ipv6.com将于2025年“寒假期间”（12月）关闭。
*   **镜像站点运营者：** 镜像站点将在2025年12月停止接收更新。
*   **服务提供商：** 更新依赖test-ipv6.com或RIPE-631的支持手册。
*   **源代码：** 大部分代码已通过GitHub链接公开。由于合同义务，地理位置和运营商查找组件不可用。
*   **域名转让：** jfesler会考虑将域名转让给服务于公共利益的信誉良好的RIR或NIC组织。
*   **镜像站点：** 建议镜像站点也停止服务，因为主站将停止提供功能和数据更新。
*   **问题咨询：** 如果有机会，可以当面进行进一步咨询。

---

## 15. 在Claude开发者平台上管理上下文

**原文标题**: Managing context on the Claude Developer Platform

**原文链接**: [https://www.anthropic.com/news/context-management](https://www.anthropic.com/news/context-management)

本文宣布Claude开发者平台新增上下文管理功能：**上下文编辑**和**记忆工具**，旨在提升AI代理的性能和效率，尤其是在处理长期任务时。

**上下文编辑**会在代理接近token限制时，自动从上下文窗口中移除过时的工具调用和结果。 这有效地延长了代理的运行寿命，无需手动干预，并提高对相关信息的关注度。

**记忆工具**使Claude能够通过开发者控制的基于文件的系统，在活动上下文窗口之外存储和检索信息。 这允许代理构建知识库、跨会话维护项目状态，以及引用先前的学习内容，而无需不断地将其重新加载到上下文中。

Claude Sonnet 4.5的内置上下文感知能力增强了这两项功能，优化了token使用。 它们共同实现了更长的对话，通过跨会话保存和重用关键信息来提高准确性，并为代理在各种用例中解锁了新的可能性，例如编码（管理大型代码库）、研究（构建知识库）和数据处理（处理超出token限制的工作流程）。

内部评估表明，性能得到了显著提升，当同时使用这两种工具时，代理搜索任务的性能提高了39%，而单独使用上下文编辑的性能提高了29%。 在网络搜索评估中，上下文编辑允许代理完成因上下文耗尽而本应失败的任务，同时减少了84%的token消耗。 这些功能现已推出公开测试版。

---

## 16. 歧义图

**原文标题**: Ambigr.am

**原文链接**: [https://ambigr.am/hall-of-fame](https://ambigr.am/hall-of-fame)

Ambigr.am是一个网站或应用，需要启用JavaScript才能运行。未提供关于其用途或内容的更多信息。

---

## 17. 哪种表格格式最适合大语言模型理解？

**原文标题**: Which Table Format Do LLMs Understand Best?

**原文链接**: [https://www.improvingagents.com/blog/best-input-data-format-for-llms](https://www.improvingagents.com/blog/best-input-data-format-for-llms)

本文探讨了不同数据格式在大型语言模型 (LLM) 基于表格数据回答问题时对准确性的影响。作者使用 GPT-4.1-nano 进行了一项实验，回答关于 1000 条合成员工记录的 1000 个随机问题，测试了 11 种数据格式，包括 CSV、JSON、XML、YAML、HTML、Markdown（表格和 KV）、INI、管道分隔、JSONL 和自然语言。

主要发现揭示了 LLM 对不同格式的理解存在显著差异。Markdown-KV（一种自定义键值 Markdown 格式）实现了最高的准确率（60.7%），明显优于 CSV（44.3%）和 JSONL（45.0%）。虽然 Markdown-KV 提供了更高的准确性，但它使用的 token 比 token 效率高的 CSV 多得多。

本文强调了在数据管道架构中选择格式以实现最佳 AI 理解、性能和成本管理的重要性。它建议考虑将 Markdown-KV 用于对准确性至关重要的任务，并将 Markdown 表格用于可读性和成本之间的平衡。作者警告不要默认使用 CSV 或 JSONL，因为它们在测试中表现不佳。

本文承认了实验的局限性，包括使用单一 LLM 模型、特定数据模式以及专注于简单的数据检索问题。未来的研究可以探索其他模型、数据模式、嵌套数据、表大小、标题重复以及不同的问题类型，以进一步完善我们对 LLM 中格式敏感性的理解。

---

## 18. VPS Hetzner 和 Coolify 新手指南

**原文标题**: Beginner Guide to VPS Hetzner and Coolify

**原文链接**: [https://bhargav.dev/blog/VPS_Setup_and_Security_Checklist_A_Complete_Self_Hosting_Guide](https://bhargav.dev/blog/VPS_Setup_and_Security_Checklist_A_Complete_Self_Hosting_Guide)

本文是一篇关于使用Hetzner和Coolify搭建安全且可用于生产环境的VPS（虚拟专用服务器）的综合指南。它被设计为一个可重复的自托管部署流程，为初学者提供详细的检查清单，并为经验丰富的用户提供参考。

本指南首先介绍预配置注意事项，推荐Hetzner，因为它具有成本效益和欧洲数据中心优势，并将其与DigitalOcean、AWS Lightsail和Linode等替代方案进行比较。

初始服务器设置清单涵盖了关键步骤，例如：

* 使用强密码保护root账户。
* 创建具有sudo权限的辅助用户。
* 设置SSH密钥身份验证并禁用密码身份验证以增强安全性。
* 使用UFW配置防火墙，包括SSH、HTTP和HTTPS的规则。
* 通过无人值守升级启用自动更新。

然后，本指南深入研究生产应用程序的部署，特别关注Node.js应用程序。这包括：

* 安装Node.js和PM2。
* 上传应用程序文件。
* 配置PM2进行进程管理和集群。
* 将Nginx设置为反向代理。

使用Let's Encrypt和Certbot设置SSL证书可确保安全通信。通过基本监控工具和使用cron作业的备份策略来解决监控和维护问题。

文中概述了常见问题的故障排除、安全验证和性能测试步骤。最后，提供了系统信息、进程管理、安全性和服务相关的快速参考命令。作者强调了自托管的优势，包括节省成本、控制权以及获得宝贵的DevOps经验。

---

## 19. Show HN: 重写 macOS Spatial Finder

**原文标题**: Show HN: Re-Implementing the macOS Spatial Finder

**原文链接**: [https://github.com/everydayanchovies/SpatialFinder](https://github.com/everydayanchovies/SpatialFinder)

该“Show HN”帖子介绍了一个旨在重现 macOS 中“Spatial Finder”功能的项目，类似于 2003 年 Ars Technica 文章中讨论的概念。其核心思想是让 Finder 记住屏幕上每个文件夹窗口的大小和位置，并在重新访问该文件夹时恢复它。

该实现涉及一些脚本，安装后会自动将 Finder 窗口（在“文档”文件夹中）的大小和位置保存到每个文件夹中的隐藏 `.framedata.json` 文件中。它利用 macOS 的 `yabai` 窗口管理器来操作窗口位置和大小。

要安装，用户需要将提供的脚本链接到系统 PATH 中的一个目录，并执行 `install.sh` 脚本来创建必要的 `yabai` 规则。

一个已知的限制是，系统无法正确处理同名文件夹，导致无法在这种情况下保存或恢复窗口状态。演示视频 (demo.webm) 展示了该功能。

---

## 20. α-Pu中共价键的实验与理论证实

**原文标题**: Experimental and Theoretical Confirmation of Covalent Bonding in α-Pu

**原文链接**: [https://advanced.onlinelibrary.wiley.com/doi/10.1002/adfm.202501798](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adfm.202501798)

无法访问文章链接。

---

## 21. 思辨证明：基于Z3定理证明的LLM推理

**原文标题**: ProofOfThought: LLM-based reasoning using Z3 theorem proving

**原文链接**: [https://github.com/DebarghaG/proofofthought](https://github.com/DebarghaG/proofofthought)

ProofOfThought是一个结合大型语言模型(LLMs)与Z3定理证明的系统，用于执行推理任务。它允许用户使用自然语言进行查询，系统利用LLM和Z3求解器来生成逻辑证明并提供答案。

该系统包含两个主要层：一个提供用户友好的Python接口的高级API（`z3dsl.reasoning`），以及一个作为基于JSON的Z3定理证明器接口的低级领域特定语言（DSL）（`z3dsl`）。大多数用户预计将通过高级API与系统交互。

本文提供了一个快速入门示例，演示如何使用高级API查询LLM。它还演示了批量评估，允许用户评估系统在数据集上的性能。

要开始使用，本文概述了必要的安装步骤，需要`z3-solver`、`openai`、`scikit-learn`和`numpy`。包括Azure OpenAI的具体实现示例可在`examples/`目录下找到。总的来说，ProofOfThought通过结合LLM和形式化定理证明器的优势，提供了一种强大的推理方法。

---

## 22. 社交冷却 (2017)

**原文标题**: Social Cooling (2017)

**原文链接**: [https://www.socialcooling.com/](https://www.socialcooling.com/)

“社交寒蝉效应”认为，过度的数据收集和分析正在对社会产生一种寒蝉效应，类似于石油消费导致全球变暖。 其核心思想是，当个人感到自己 постоянно被监控时，他们会改变自己的行为，从而导致自我审查、规避风险和顺从。

文章强调了数据经纪人如何收集大量个人信息并利用它来创建详细的个人资料，预测宗教、政治观点甚至性取向等各个方面。 这些资料随后会影响工作申请、贷款审批甚至约会应用匹配等机会，往往会加剧偏见和不平等。

这种“声誉经济”的后果被概括为：一种人们犹豫表达不受欢迎意见的顺从文化； 一种个人避免可能对其分数产生负面影响的行动的规避风险文化； 以及日益增长的社会僵化，限制了抗议不公正现象的能力。 文章引用中国的社会信用体系作为警示性的例子。

文章最后强调，需要提高公众意识，并对数据和隐私有细致的理解。 它呼吁在一个数据驱动的世界中保护犯错的权利和被遗忘的权利，并将此与解决全球变暖的缓慢进展相提并论。 作者倡导分享信息并推广保护隐私的做法。

---

## 23. 使用 Ada 和 Rust 解决 Advent of Code 问题的比较

**原文标题**: A comparison of Ada and Rust, using solutions to the Advent of Code

**原文链接**: [https://github.com/johnperry-math/AoC2023/blob/master/More_Detailed_Comparison.md](https://github.com/johnperry-math/AoC2023/blob/master/More_Detailed_Comparison.md)

文章《使用解决 Advent of Code 的方案比较 Ada 和 Rust》展示了一个名为 AoC2023 的项目，该项目由 johnperry-math 创建。该项目很可能使用 Ada 和 Rust 两种编程语言实现了 Advent of Code 2023 谜题的解决方案。其主要目的是比较这两种语言，可能涉及以下方面：

*   **语法和语义：** 同一算法在每种语言中的表达方式，突出显示语法、数据结构和控制流的差异。
*   **性能：** 对 Ada 和 Rust 实现的解决方案的运行时和内存使用情况进行比较分析。
*   **安全性和安全性：** Ada 和 Rust 都以强大的安全特性而闻名；该比较可能深入探讨这些特性如何在解决 Advent of Code 谜题的过程中帮助防止错误和漏洞。
*   **开发者体验：** 作者可能会分享他们使用每种语言的个人体验，涵盖易用性、库的可用性、调试工具和整体生产力等方面。
*   **代码结构和可维护性：** 该比较可能会探讨不同的语言特性如何影响代码的组织、可读性和长期可维护性。

本质上，这篇文章使用 Advent of Code 挑战作为实际基准，以探索 Ada 和 Rust 在实际编码场景中的优势和劣势。该存储库是公开的，这表明作者打算与社区分享他们的发现和代码示例。

---

## 24. 选择电子邮件而非即时通讯的优势

**原文标题**: Benefits of choosing email over messaging

**原文链接**: [https://www.spinellis.gr/blog/20250926/?li](https://www.spinellis.gr/blog/20250926/?li)

Diomidis Spinellis 认为电子邮件相对于现代消息平台仍具有持续价值。他更喜欢电子邮件，因为它具有统一的收件箱，可将所有通信整合在一个地方，以及统一的存档，可提供单一的可搜索历史记录。电子邮件提供长期可用性，因为服务和平台会消失，这与许多消息服务的短暂性不同。Spinellis 强调了 Thunderbird 等电子邮件客户端的丰富功能，包括文件夹、过滤器、稍后发送、标签、地址簿宏、排序、高级搜索和离线处理。

他重视电子邮件客户端的单一界面，这允许深度掌握和自定义。电子邮件还有助于异步通信，最大限度地减少中断。与一些“免费”消息应用程序不同，电子邮件没有广告和令人上瘾的内容。电子邮件允许根据提供商控制机密性，这与经常扫描消息的消息平台不同。电子邮件依赖于开放协议（SMTP、IMAP），从而在客户端和操作系统选择以及开放存储格式方面授予自由，从而提高生产力和可靠性。作者自 1986 年以来一直在本地存储电子邮件，从而可以进行自定义处理、备份以及在客户端之间迁移。

---

## 25. 鹦鹉 - Gleam 中的类型安全 SQL，支持 SQLite、PostgreSQL 和 MySQL

**原文标题**: Parrot – type-safe SQL in Gleam, supports SQlite, PostgreSQL and MySQL

**原文链接**: [https://github.com/daniellionel01/parrot](https://github.com/daniellionel01/parrot)

Parrot 是一个 Gleam 库，提供类型安全的 SQL 功能，支持 SQLite、PostgreSQL 和 MySQL。它利用 `sqlc` 进行繁重的工作，提供诸如模式推断、自动 `sqlc` 二进制文件下载以及直接从 SQL 查询列名派生的命名参数等功能。

要使用 Parrot，您需要将其作为 Gleam 依赖项安装，并在项目的 `src` 目录中的 `.sql` 文件中定义 SQL 查询。`parrot` 命令行工具会生成一个包含查询的类型安全函数的 `sql.gleam` 模块。您可以通过环境变量或命令行参数指定数据库连接字符串。

Parrot 包含流行的 Gleam 数据库库（如 `lpil/pog` 和 `lpil/sqlight`）的实用程序包装器，以便更轻松地集成。PostgreSQL、MySQL 和 SQLite 的集成测试中提供了示例。

虽然功能强大，但它也有一些怪癖：Postgres 中的多维数组可能无法完全支持，动态数据类型将被包装在动态类型中。Parrot 旨在 Erlang Gleam 环境中执行，但是生成的模块可以复制过来，并且也可以在 JavaScript 环境中工作。

---

## 26. 美国人越来越认为合法体育博彩对社会不利。

**原文标题**: Americans increasingly see legal sports betting as a bad thing for society

**原文链接**: [https://www.pewresearch.org/short-reads/2025/10/02/americans-increasingly-see-legal-sports-betting-as-a-bad-thing-for-society-and-sports/](https://www.pewresearch.org/short-reads/2025/10/02/americans-increasingly-see-legal-sports-betting-as-a-bad-thing-for-society-and-sports/)

皮尤研究中心最新调查显示，越来越多的美国人对合法体育博彩持负面看法，无论对社会还是体育运动而言。2025年，43%的人认为它对社会有害（2022年为34%），40%的人认为它对体育运动有害（2022年为33%）。虽然负面看法正在增长，但许多人仍然认为它既不好也不坏。

尽管担忧日益增加，但美国人参与体育博彩的比例仅略有上升，从2022年的19%上升到2025年的22%。然而，博彩方式发生了转变。在线体育博彩显著增加，去年有10%的成年人在网上投注，而2022年为6%。

这项基于9916名美国成年人回复的调查强调，人们对合法体育博彩的意识日益增强，这得益于广告的增加。包括男性、女性、大学毕业生和不同政治派别在内的各个群体中，负面态度正变得越来越普遍。值得注意的是，年轻的美国人，尤其是30岁以下的男性，对体育博彩的负面情绪显著增加。

文章还指出，运动员和工作人员因违反体育博彩规则而面临纪律处分的案例，引发了人们对体育运动诚信的担忧。最后，文章指出，年轻人以及非裔和西班牙裔美国人更有可能参与体育博彩。

---

## 27. 拯救我们的最糟糕的妙招

**原文标题**: The best worst hack that saved our bacon

**原文链接**: [https://jeffersonheard.ghost.io/the-best-worst-hack-that-saved-our-bacon/](https://jeffersonheard.ghost.io/the-best-worst-hack-that-saved-our-bacon/)

该文章讲述了一次因一个巧妙但略显“愚蠢”的临时方案而避免的灾难。该公司的日历平台正迅速逼近其事件发生次数的32位整数主键的上限。计划迁移到大整数的方案几乎已准备就绪，但团队发现这些整数键暴露在一些集成至关重要的公共API中，而这些客户的IT部门的更新积压时间长达数月。

面对迫在眉睫的键耗尽风险，作者提出了一个临时解决方案：将主键序列重置为32位整数范围的负极限，从而有效地使可用键空间翻倍。尽管最初存在怀疑和多次审查，但团队还是实施了这个“大胆的权宜之计”，为他们争取了6-8个月的时间来完全迁移到BigInt并解决API依赖关系。

长远解决方案包括切换到不透明的键句柄，防止字典攻击并允许后端灵活性。他们与客户成功团队合作，通知受影响的客户并为API变更做好准备。虽然通常不建议这样做，但这个临时方案是那一刻的正确决定，它提供了一个固定的时间表和计划来解决问题，并防止了潜在的平台范围内的故障，同时允许为他们的用户进行受控和沟通的过渡。

---

## 28. 博客订阅

**原文标题**: Blog Feeds

**原文链接**: [https://blogfeeds.net](https://blogfeeds.net)

本文介绍“博客订阅源”，作为社交媒体令人沉迷的信息流的替代方案，提倡回归更个性化和互联的Web体验。它不是一个需要注册的平台，而是一个依赖于三个要素的概念：博客、RSS和订阅源页面。

本文鼓励读者创建简单的博客作为个人在线空间。它推荐了各种易于使用的托管服务（Bear Blog、Pika.page、Substack、Ghost、Wordpress、Squarespace）和自托管框架（Astro、Hugo、Zola、11ty、Jekyll）用于博客创建。

RSS被解释为一种订阅方法，类似于电子邮件新闻通讯，读者使用RSS阅读器应用程序订阅博客并接收更新。本文推荐了Feedly、Inoreader、NetNewsWire、Feeeed和Reader作为RSS阅读器。

博客订阅源的核心在于在博客上创建一个“订阅源页面”，列出所有订阅的RSS源。这个公开共享的页面允许其他人发现新的博客，并建立一个有机的连接网络。

本文强调，博客订阅源是一个去中心化的想法，不受中央权威和大科技公司控制数据。它回答了常见问题，澄清它是免费的（尽管平台和阅读器可能提供付费选项），不一定取代社交媒体，并且可以货币化。它建议使用博客评论或BlueSky等平台，甚至电子邮件进行对话。

---

## 29. 牛顿：基于 NVIDIA Warp 的物理模拟引擎

**原文标题**: Newton: physics simulation engine built upon NVIDIA Warp

**原文链接**: [https://github.com/newton-physics/newton](https://github.com/newton-physics/newton)

Newton：基于GPU加速的物理模拟引擎

Newton是一个基于NVIDIA Warp构建的GPU加速物理模拟引擎，面向机器人和仿真研究。它扩展了Warp的仿真能力，并集成了MuJoCo Warp，着重于GPU计算、OpenUSD支持、可微性以及可扩展性，以实现快速迭代和可扩展的仿真。

目前处于Beta阶段，API不稳定且可能更改。Newton是由迪士尼研究院、Google DeepMind和NVIDIA发起，并在Apache-2.0许可证下由Linux基金会托管的项目。

快速入门指南建议使用`uv` Python包管理器。用户可以克隆存储库，设置`uv`环境，并运行各种示例（basic、robot、cloth、inverse kinematics、MPM、selection和DiffSim）。每个类别都提供了示例命令。

这些示例支持命令行参数来控制查看器类型（OpenGL、USD输出、ReRun或无）、计算设备、帧数和输出路径。 提供了示例用法。

有关贡献、开发指南、支持、社区讨论、行为准则、项目治理、法律和成员的信息，请参见链接的资源。

---

## 30. NSA和IETF：攻击者能否通过购买实现弱化密码学的标准化？

**原文标题**: NSA and IETF: Can an attacker purchase standardization of weakened cryptography?

**原文链接**: [https://blog.cr.yp.to/20251004-weakened.html](https://blog.cr.yp.to/20251004-weakened.html)

来自cr.yp.to的这篇文章对美国国家安全局（NSA）可能通过经济激励和营销手段影响弱化密码学标准的制定表示担忧，特别是互联网工程任务组（IETF）中关于传输层安全协议（TLS）的标准。作者关注TLS的“混合”（使用ECC+PQ的双重加密）和“非混合”（仅使用PQ的单一加密）后量子加密提案之间的争论。

文章认为，尽管量子算法已证实存在漏洞，且混合方法在数据安全方面具有明显优势，但NSA和英国政府通信总部（GCHQ）仍在推动采用单一加密（仅PQ）。作者指出，NSA官员和思科员工的声明表明他们倾向于并愿意购买单一加密解决方案，这与NSA渴望“纯”ML-KEM标准相一致。

作者将此事与NSA历史上操纵数据加密标准（DES）的行为相提并论，当时该机构推广了一种弱化的标准，同时秘密地在内部使用更强大的多层加密。这可以作为一个例子，说明NSA可能如何在战略上提倡安全性较低的公共标准，同时为其自身的敏感数据保持更强的安全性。作者总结道，NSA的影响可能导致弱化密码学的标准化，从而可能危及用户数据的安全。

---

## 31. 爱好希尔伯特单纯形

**原文标题**: Hobby Hilbert Simplex

**原文链接**: [https://nedbatchelder.com/blog/202509/hobby_hilbert_simplex.html](https://nedbatchelder.com/blog/202509/hobby_hilbert_simplex.html)

本文详细介绍了作者重现一件令人欣赏的生成艺术作品的旅程，重点介绍了三个关键算法：Hobby 曲线、希尔伯特排序和单纯形噪声。该艺术作品涉及绘制多条穿过略微移动的随机点的曲线，从而产生一种流畅、烟雾般的效果。

Hobby 曲线是一种以“自然”方式绘制穿过点的曲线的算法，用于连接这些点。然而，简单地连接随机生成的点会产生一种不希望有的“涂鸦”效果。为了解决这个问题，采用了希尔伯特排序，以反映空间邻近性的方式对点进行排序，从而产生更平滑、更直观的曲线。单纯形噪声用于生成点的运动。这种噪声函数在点位置产生平滑、连续但不可预测的变化，从而有助于艺术作品的流畅外观。

作者还讨论了为什么线条偶尔会“分离又重新结合”。这归因于 Hobby 曲线的性质，它会随着点位置的微小变化而急剧改变形状，以及希尔伯特排序，其中点移动到不同的网格正方形会改变排序顺序，从而改变曲线的形状。文章最后提到了作者的 Python 实现，使用 Jupyter Notebook 进行实验，以及对未来动画探索的预告。

---

## 32. OpenAI对算力的渴求

**原文标题**: OpenAI's hunger for computing power

**原文链接**: [https://www.wsj.com/tech/ai/openai-sam-altman-asia-middle-east-7b660809](https://www.wsj.com/tech/ai/openai-sam-altman-asia-middle-east-7b660809)

无法访问文章链接。

---

## 33. 比较具有相似硬件结构的 RISC 和 CISC (1991)

**原文标题**: Comparing a RISC and a CISC with Similar Hardware Organization (1991)

**原文链接**: [https://dl.acm.org/doi/pdf/10.1145/106972.107003](https://dl.acm.org/doi/pdf/10.1145/106972.107003)

无法访问该文章链接。

---

## 34. 展示一下：用于游戏的 2D Spine 动画 AI

**原文标题**: Show HN: 2D Spine Animation AI for Game

**原文链接**: [https://www.godmodeai.co/ai-spine-animation](https://www.godmodeai.co/ai-spine-animation)

上帝模式AI：一款利用人工智能的2D骨骼动画生成器，旨在简化游戏开发流程。该工具承诺以10倍的速度和简易度创建游戏就绪的动画，无需手动绑定。它具备自动绑定、骨骼生成功能，并可应用超过2000个动画库中的动画。用户上传角色图片（目前仅限人形），选择动画类型（行走、跑步等）和视角风格（横版卷轴、平台跳跃），人工智能即可处理绑定和动画。

该过程首先生成一个3D模型以了解骨骼结构，然后将其转换为2D骨骼格式。输出分层，便于后期编辑，并可导出至Spine、Unity、Godot及其他游戏引擎。

上帝模式AI采用按需付费的信用点系统，并提供包月订阅选项，最多可生成250个动画，并支持社区分享。此外还提供信用点套餐。用户可以通过在社交媒体上分享上帝模式AI来赚取免费信用点。针对大型游戏工作室，还提供企业解决方案和定制AI模型。网站突出显示了积极的用户反馈并解答了常见问题。该工具旨在显著提高动画制作效率和游戏开发者角色创建速度。

---

## 35. AMD GPU 上的矩阵核心编程

**原文标题**: Matrix Core Programming on AMD GPUs

**原文链接**: [https://salykova.github.io/matrix-cores-cdna](https://salykova.github.io/matrix-cores-cdna)

本文全面介绍了在 AMD GPU 上对 Matrix Cores 进行编程的指南，重点关注低精度数据类型（FP16、FP8、FP6 和 FP4）以及 CDNA™4 架构中引入的指数块缩放特性。它解释了使用 Matrix Cores 实现的显著性能提升，尤其是在使用较低精度输入时，强调在 CDNA™4 上与 FP32 相比，速度提升高达 64 倍。

本文详细介绍了浮点数的二进制表示以及各种低精度类型的特性，包括指数偏差、范围和特殊值（如 NaN 和 Infinity）。它还解释了 FP8 变体（如 E4M3FN 和 E4M3FNUZ）之间的差异，以及它们在 CDNA™3 和 CDNA™4 架构中的用法。

该指南涵盖了 Matrix Core 指令 (MFMA)，列出了 CDNA™3 和 CDNA™4 的可用浮点指令。它详细介绍了 LLVM 中 MFMA 编译器内联函数的语法，包括数据类型和矩阵维度。 至关重要的是，本文强调 MFMA 指令是 wavefront 级别的，需要了解操作数如何在 wavefront 内的线程之间分布。 最后，它提供了代码示例，说明如何在 HIP 内核中实现 MFMA 操作，演示了数据布局和内存访问模式，用于诸如 `__builtin_amdgcn_mfma_f32_32x32x2f32` 和 `__builtin_amdgcn_mfma_f32_16x16x16f16` 等指令。

---

## 36. 截止日期不是人工智能超越我们之时，而是我们停止使用自己大脑之日。

**原文标题**: The deadline isn't when AI outsmarts us – it's when we stop using our own minds

**原文链接**: [https://www.theargumentmag.com/p/you-have-18-months](https://www.theargumentmag.com/p/you-have-18-months)

德里克·汤普森在他的文章中认为，人工智能真正的危险并非在于它超越我们的智能，而是我们过度依赖它而导致的自我技能退化。他认为，由于ChatGPT等人工智能工具加速了阅读和写作能力的下降，正在侵蚀我们深度思考的能力，而这在现代经济中至关重要。

汤普森强调了教育工作者对学生使用人工智能在学校作弊的担忧，这会导致文盲和批判性思维能力的下降。他引用研究表明，识字率和算术能力得分下降，甚至在成绩优异的学生中，对阅读书籍的兴趣也在降低。

汤普森借鉴了卡尔·纽波特和沃尔特·翁格的研究，强调阅读和写作对于发展“深度符号思考的超能力”至关重要。他认为，识字在历史上重塑了人类的思想，促进了复杂思想和知识的传递。汤普森警告说，这些技能的下降正在“解开”我们的认知能力，而人工智能正是在此时兴起。

汤普森总结说，未来几代人最有价值的技能是进行深度阅读、写作和批判性思考的能力。随着人工智能日益普及，深刻的人类思想能力有成为稀缺商品的风险。因此，面对技术进步，个人必须优先发展和保持他们的认知技能。

---

## 37. 侦察和减缓小行星2024 YR4的空间任务方案

**原文标题**: Space Mission Options for Reconnaissance and Mitigation of Asteroid 2024 YR4

**原文链接**: [https://arxiv.org/abs/2509.12351](https://arxiv.org/abs/2509.12351)

这篇于2025年9月15日提交的arXiv文章探讨了小行星2024 YR4的太空任务选项。最初，该小行星在2032年12月撞击地球的概率为3%，但后来被排除。然而，撞击月球的概率增加到4%，可能会在近地轨道产生大量微流星体碎片，对宇航员和航天器构成风险。通过JWST观测，其直径估计为60 +/- 7米。

该论文研究了应对这一威胁的各种任务概念，包括飞越和交会侦察、偏转以及对小行星的强力摧毁。它分析了截至2032年的快速响应和延迟发射情景，评估了化学和太阳能电力推进、运载火箭、深空机动和引力辅助。还考虑了重新部署现有航天器的可能性。

研究发现，在2028年末发射的侦察任务是最可行的，而偏转任务似乎不切实际。动能和核能强力摧毁任务是可行的选择，发射窗口在2029年至2032年之间。作者强调，即使月球撞击威胁被排除，对小行星进行特性描述的侦察任务仍然具有价值。该研究对减轻或了解与小行星2024 YR4相关的风险的潜在策略进行了全面评估。

---

## 38. 人工智能驱动的开源代码清洗

**原文标题**: AI-powered open-source code laundering

**原文链接**: [https://github.com/SudoMaker/rEFui/blob/main/HALL_OF_SHAME.md](https://github.com/SudoMaker/rEFui/blob/main/HALL_OF_SHAME.md)

该文章描述了一个名为 "rEFui" 的开源项目，托管在 SudoMaker 的 GitHub 仓库中。标题“AI驱动的开源代码清洗”具有挑衅性，暗示该项目旨在混淆或修改代码，很可能是为了绕过版权检测或隐藏恶意功能。虽然描述很少，但项目细节表明这是一个公共仓库，有一个 fork 和 55 个 star，表明存在一定的社区兴趣，尽管标题可能具有争议性。使用“AI驱动的”进一步暗示了人工智能参与了修改或混淆代码的过程。在没有更多背景信息的情况下，无法确定代码清洗的确切性质，但名称和标题强烈暗示该项目旨在以使其看起来原创或隐藏其真实目的的方式修改代码。

---

## 39. Microsoft Surface Pen兼容性/互操作性常见问题解答 (2024)

**原文标题**: Microsoft Surface Pen Compatibility / Interoperability FAQ (2024)

**原文链接**: [https://dancharblog.wordpress.com/2017/05/29/surface-pen-compatibility-interoperability-faq/](https://dancharblog.wordpress.com/2017/05/29/surface-pen-compatibility-interoperability-faq/)

本FAQ全面介绍了Microsoft Surface Pen在不同Surface设备上的兼容性和功能。它详细说明了不同代笔（Wacom Ver.1、n-trig Ver.2、Ver.3、Ver.4、Classroom Pen、Slim Pen、Slim Pen 2和Hub Pens）之间的区别，概述了它们的压力感应级别、延迟、初始激活力（IAF）、倾斜支持和触觉反馈。

图表总结了笔与特定Surface型号（Surface Pro、Book、Go、Studio、Laptop等）的兼容性，并注明了每种组合支持的功能。主要细节包括压力级别数（256-4096）、延迟（13-100毫秒）和初始激活力（9-42克）。较新型号，如SLS、SP8、SP9、SLS、SLS2等，具有更低的延迟和零力度墨迹书写支持。

本FAQ解答了常见问题，例如哪些设备附带特定笔、颜色可用性、可更换笔尖、电池类型、按钮功能、笔夹/笔绳以及兼容性问题（例如，抖动、波浪线、笔尖偏移）。Slim Pen 2增加了触觉反馈。Surface Laptop Go系列不支持笔输入。它还解释了不同笔和设备的磁铁配置，以及笔代际之间的互换性。最后，它列出了兼容的第三方触控笔品牌。

---

## 40. Mod. 5140 - IBM首款笔记本电脑

**原文标题**: Mod. 5140 - IBM's First Laptop Computer

**原文链接**: [https://richardsapperdesign.com/products/mod-5140/](https://richardsapperdesign.com/products/mod-5140/)

本文介绍了IBM公司1985年发布的第一款笔记本电脑IBM Mod. 5140。这款笔记本电脑在佛罗里达州博卡拉顿的IBM实验室开发，其设计因形似鳄鱼头而闻名，尤其是从侧面看时。加上打印机和纸张，便形成了一个完整的鳄鱼外观，纸张充当了尾巴。Mod. 5140荣获多项著名设计奖项，包括1986年的Premio SMAU奖、1988年的IF Industrie Forum Design Award Hannover奖，以及1987年入选的Compasso d’Oro奖。本文还赞扬了Colleen Sweeney，强调了该电脑的功能创新及其独特（尽管是无意的）的爬行动物美学。

---

## 41. 你不能用正则表达式解析XML。但我们还是试试吧。

**原文标题**: You can't parse XML with regex. Let's do it anyways

**原文链接**: [https://sdomi.pl/weblog/26-nobody-here-is-free-of-sin/](https://sdomi.pl/weblog/26-nobody-here-is-free-of-sin/)

本文戏谑地论证了，虽然通常认为用正则表达式解析XML和HTML是不良实践，但在某些情况下（特别是网络抓取时），它可能是一种务实的解决方案。

作者首先概述了普遍的观点：XML是复杂的，应该使用专门的解析器进行解析。他们阐述了一个简单的基于堆栈的解析器如何处理XML，突出了该格式的结构化特性。然而，他们将此与人类通常将XML视为字符串的方式进行对比，从而导致人们倾向于使用正则表达式来处理更简单的任务。

然后，文章深入探讨了HTML，将其描述为“古怪的XML”，因为它对格式错误的标记具有容错性，这是为了可访问性而做出的刻意设计。这使得解析HTML比解析XML更具挑战性。

尽管存在复杂性，作者还是提出了在特定网络抓取场景中使用正则表达式的理由。他们认为，在处理不可预测或略微损坏的标记时，正则表达式可以提供更快的开发速度和更大的适应性。他们提供了一个使用命令行工具和正则表达式从网站提取火车站名称的例子，展示了一个快速的单行代码有时比编写复杂的选择器更有效。

最终，本文并不提倡用正则表达式取代合适的解析器。相反，它表明正则表达式可以成为快速而粗略的数据提取的宝贵工具，尤其是在处理混乱的网络现实时。

---

## 42. 1Password CLI 漏洞 (2023)

**原文标题**: 1Password CLI Vulnerability (2023)

**原文链接**: [https://codeberg.org/manchicken/1password-cli-vuln-disclosure](https://codeberg.org/manchicken/1password-cli-vuln-disclosure)

无法访问该文章链接。

---

## 43. 比亚迪打造全球最快汽车

**原文标题**: BYD Builds World's Fastest Car

**原文链接**: [https://www.autotrader.co.uk/content/news/byd-builds-world-s-fastest-car](https://www.autotrader.co.uk/content/news/byd-builds-world-s-fastest-car)

无法访问文章链接。

---

## 44. 宇宙碰撞使地球从一片干燥变为蓝色星球。

**原文标题**: Earth was born dry until a cosmic collision made it a blue planet

**原文链接**: [https://www.sciencedaily.com/releases/2025/09/250928095654.htm](https://www.sciencedaily.com/releases/2025/09/250928095654.htm)

伯尔尼大学2025年9月29日发布的这篇科学新闻文章详细介绍了研究，该研究表明地球最初是一个干燥、不适宜居住的星球，缺乏水和必需的碳化合物。这项发表在《科学进展》上的研究使用了陨石和地球岩石中的同位素和元素数据，并采用基于锰-53衰变的精确时钟，来确定太阳系形成后三百万年内地球凝固的化学成分。

这些发现支持了一个假设，即后来与一颗名为忒伊亚的行星发生的巨大碰撞从根本上改变了地球。忒伊亚行星形成于太阳系更外围，并积累了水等挥发性物质。这次撞击可能带来了生命出现所必需的关键水和其他挥发性元素。

该研究强调，地球适宜生命生存的环境并非一个持续的过程，而是这次偶然事件的结果。它强调了宇宙中的宜居性并非必然，并表明地球目前的状况要归功于一场宇宙巧合。研究人员现在正专注于更详细地了解忒伊亚的碰撞，旨在创建能够解释地球和月球（据信是由这次事件的碎片形成的）的物理、化学和同位素性质的模型。

---

## 45. 机器学习能力作为非周期序列有序性的一种度量

**原文标题**: Machine Learnability as a Measure of Order in Aperiodic Sequences

**原文链接**: [https://arxiv.org/abs/2509.18103](https://arxiv.org/abs/2509.18103)

该 arXiv 论文于 2025 年 9 月 9 日提交，探讨了利用机器学习量化非周期序列中的有序性，特别是 Ulam 螺旋上可视化的素数。由 Jennifer Dodgson 和 Surender Suresh Kumar 领导的作者提出，机器学习模型对模式的“可学习性”可以作为衡量这些序列规律性的标准。

核心实验包括在从 Ulam 螺旋不同区域提取的区块上训练以图像为中心的机器学习模型。结果表明，在代表较大数字（约 5 亿）区域的区块上训练的模型比在代表较小数字（低于 2500 万）区域的区块上训练的模型获得更高的准确率。这表明在 Ulam 螺旋中，更高的数字尺度下存在更大程度的可学习有序性。

此外，对精确率和召回率的分析表明，该模型在不同区域采用不同的素数分类策略。在较小的数字范围内，该模型侧重于识别素数模式，而在较大的数字范围内，它侧重于排除合数。这种分类策略的转变与现有的数论猜想相符，这些猜想表明，素数分布在更大的尺度上表现出递减的噪声和增加的规律性（密度、AP 等分布）。

作者得出结论，机器学习有望成为数论研究的一种新型实验工具，尤其是在研究与用于密码学应用的强素数和弱素数相关的模式方面。这项研究突出了非周期序列中机器学习的可学习性和内在数学有序性之间的潜在联系。

---

## 46. 香山向量浮点单元设计

**原文标题**: XiangShan Vector Floating-Point Unit Design

**原文链接**: [https://docs.xiangshan.cc/projects/design/en/latest/backend/VFPU/](https://docs.xiangshan.cc/projects/design/en/latest/backend/VFPU/)

本文档详细描述了香山向量浮点单元(VFPU)V2R2版本的设计。该VFPU支持向量浮点Mul、FMA、Div和Sqrt计算，兼容fp32、fp64和fp16格式以及RV-V1.0向量浮点指令。

VFPU分为四个模块：VFAlu、VFMA、VFDivSqrt和VFCvt，每个模块处理特定类型的指令。VFAlu处理fadd相关指令，VFMA管理乘法和乘加运算，VFDivSqrt处理除法和平方根，VFCvt处理格式转换。

一个关键挑战是支持多种单精度和混合精度格式。虽然标量单元可能会分别处理f64、f32和f16加法，但VFPU通过在64位接口上同时执行1、2或4个操作来利用硬件重用，从而在使用较低精度格式时最大限度地提高带宽利用率。它处理诸如`f64 = f64 + f64`、`2 f32 = f32 + f32`和`4 f16 = f16 + f16`之类的格式。混合精度计算更加复杂，需要先进行格式转换，然后才能进行计算，尤其是对于非规格化数。

本文档重点关注浮点加法的优化，比较单路径和双路径算法，并提出一种改进的双路径方法，以实现更高的速度。改进的双路径算法优化了`d <= 1`和`d > 1`情况的处理，使用并行执行和预计算等技术来减少延迟。它描述了所提出的加法算法的远路径，重点介绍了指数差异和操作数选择的并行计算。

---

## 47. 提升我的家庭实验室

**原文标题**: Leveling Up My Homelab

**原文链接**: [https://cweagans.net/2025/09/leveling-up-my-homelab/](https://cweagans.net/2025/09/leveling-up-my-homelab/)

作者讨论了其家庭实验室的演变，从基础设置过渡到更健壮且接近生产环境的状态。他们对旧设置的局限性感到沮丧（Synology NAS瓶颈、有限的编排、计算限制、缺乏灾难恢复以及困难的远程访问），因此概述了现代基础设施的目标，包括Kubernetes、GitOps、可观察性、弹性和可扩展性。

新的设置具有显著的升级：一个22U机架、更强大的计算能力（Beelink SER5 MAX和SER9 Pro迷你PC）、一个替代Synology NAS的UniFi UNAS PRO、升级的网络（UniFi U7 Pro和10G连接）、冗余电源，以及用于远程访问的BliKVM/KVM切换器。

作者正在使用Talos Linux实现Kubernetes，使用Argo CD实现GitOps，并计划探索AI工作负载、使用Kubespan的多站点Kubernetes、用于身份验证的Pocket ID以及利用Cloudflare Tunnels。其动机不仅仅是获取设备，而是构建一个用于实际工作、学习和实验的弹性且可扩展的系统，这与他们对基础设施和职业发展的态度相符。未来的文章将详细介绍PXE引导、自动化、GitOps设置、身份验证、GPU调度和灾难恢复策略。

---

## 48. 乐高搭建问题优化的数学模型/算法 [pdf]

**原文标题**: Mathematical Models/Algorithms for Optimization of Lego Construction Problems [pdf]

**原文链接**: [https://backend.orbit.dtu.dk/ws/portalfiles/portal/236623063/PhD_Thesis_Torkil_Kollsker.pdf](https://backend.orbit.dtu.dk/ws/portalfiles/portal/236623063/PhD_Thesis_Torkil_Kollsker.pdf)

该文档看似为PDF文件，很可能是题为“乐高构建问题优化的数学模型/算法”的研究论文或技术文档。然而，由于内容采用二进制格式或经过高度压缩，难以对其内容进行精确解读。

根据标题和对PDF内文本的有限分析，我们可以推断出以下几点：

*   **重点：** 本文重点在于应用数学模型和算法来解决与乐高构建相关的优化问题。
*   **方法：** 它可能探讨不同的数学建模技术（例如，整数规划、图论、约束满足）和算法方法（例如，启发式算法、元启发式算法、精确求解器）来解决这些问题。
*   **优化问题：** 乐高构建问题可能包括：
    *   找到用给定的砖块构建的最稳定结构。
    *   最小化特定设计所需的砖块数量。
    *   优化乐高结构中的重量分布。
    *   自动化乐高设计和指令生成。
*   **目标受众：** 该文档可能面向对计算设计、机器人技术或优化技术感兴趣的研究人员、工程师或爱好者，特别是乐高构建领域。

由于主要内容无法读取，因此无法提供模型、算法和结果的详细摘要。该文档可能展示了与优化乐高构建相关的数学公式、计算方法以及可能的实验结果。

---

## 49. 笔记本创造系统，手机喂养算法。这种不对称性决定了权力。

**原文标题**: Laptops create systems. Phones feed algorithms. The asymmetry determines power

**原文链接**: [https://zakelfassi.com/command-interface-device-power](https://zakelfassi.com/command-interface-device-power)

本文认为，我们使用的设备类型——笔记本电脑与手机——显著影响我们与技术的关系，并最终影响我们的权力和能动性。文章断言，笔记本电脑主要作为命令界面，针对创造、系统级思考和控制进行了优化。相比之下，手机被设计用于快速消费，巧妙地引导用户进入顺从模式，让他们为算法和平台提供数据。

作者强调，虽然手机可以用于创作（视频、照片等），但创作能力被限制在平台控制的“沙盒”中，限制了用户构建和修改系统的能力。另一方面，笔记本电脑允许用户*在*系统之上进行创作，使他们能够编写代码、设计工具和修改基础设施。

文章指出，在各个领域都存在不对称现象，例如交易大厅和军事指挥中心，它们利用多屏幕工作站进行创作和控制，而它们的对应方（客户、现场单位）则被降级到消费界面。文章强调，这种划分并非偶然，而是旨在创造和维持等级制度。

文章鼓励有意识地选择设备，提倡使用笔记本电脑进行系统级思考、长篇写作和学习，同时建议使用手机进行快速信息收集和社交连接。文章最后强调，这不仅仅是关于设备，而是关于所有领域更广泛的创造/消费分裂，敦促读者认识到并抵制被动地被归类到消费模式中。作者提出了两种潜在的未来情景：融合，即设备在功能上变得等同；或分化，即创造和消费界面进一步分离，可能加剧权力梯度。

---

## 50. 912亿美元：摆脱繁文缛节的能源独立

**原文标题**: $912 energy independence without red tape

**原文链接**: [https://sunboxlabs.com/](https://sunboxlabs.com/)

本文概述了一个DIY的912美元太阳能系统，旨在实现能源独立，无需复杂的并网。该系统本质上充当设备和墙壁之间的中介，优先使用太阳能，仅在必要时才切换到电网电力。

作者详细介绍了所需的组件，并提供了亚马逊链接，用于购买电缆、充电器和可选的远程跟踪器。该系统的核心与Will Prowse的48V 3000W离网太阳能系统指南相似，作者建议参考该指南进行组装。

本文强调了经济和环境效益。根据旧金山的电价，该系统初始成本（2024年为1124美元，现在为912美元）的预计回收期约为2年。对系统隐含能源（生产过程中使用的能源）的计算表明，环境回收期约为3.5年。

常见问题解答解决了关键问题：该系统需要将延长线连接到中央“太阳能盒”，它不会将电力反馈回电网，其合法性源于其作为电器简单电源的功能，类似于直接将它们插入墙壁。

---

## 51. 如何高效注入知识？大型语言模型的知识注入扩展规律

**原文标题**: How to inject knowledge efficiently? Knowledge infusion scaling law for LLMs

**原文链接**: [https://arxiv.org/abs/2509.19371](https://arxiv.org/abs/2509.19371)

这篇2025年9月提交的arXiv文章，研究了在大型语言模型（LLM）预训练期间注入领域特定知识的最佳方法。由吕康涛领导的作者们旨在解决平衡知识注入的挑战，以避免专业化不足和灾难性遗忘。

该论文重点关注由过度注入领域特定数据引起的“记忆坍塌”现象。通过实验，作者们发现了两个关键观察结果：（1）每个模型都存在一个“临界坍塌点”，代表知识保留急剧下降的阈值；（2）这些坍塌点表现出“规模相关性”，与模型规模一致地缩放。

基于这些观察结果，作者们提出了一个“知识注入缩放定律”。该定律旨在通过分析较小模型的行为来预测注入大型LLM的最佳领域知识量。该论文展示了跨不同模型大小和预训练token预算的大量实验验证，证明了所提出的缩放定律的有效性和通用性。最终，这项研究提供了一种将知识有效注入LLM同时避免有害记忆坍塌的方法，从而提高在领域特定任务上的性能。

---

## 52. Paged Out 第七期 [pdf]

**原文标题**: Paged Out Issue #7 [pdf]

**原文链接**: [https://pagedout.institute/download/PagedOut_007.pdf](https://pagedout.institute/download/PagedOut_007.pdf)

此文档似乎是一个PDF文件，具体为“Paged Out Issue #7”。但提供的内容是PDF的原始数据，并非人类可读的文本。它是由编码字节、指令和图像数据组成的流。

因此，我无法提供文章内容的摘要。要总结文章，我需要“Paged Out Issue #7”的实际文本或内容。我只能确认该文件以PDF结构存在，其中包含元数据、页面布局、图像数据，以及可能以某种方式编码的文本，需要通过PDF阅读器进行解释。

---

## 53. Clavier: 基于 FPGA 的机械键盘，带 USB 集线器和通信接口

**原文标题**: Clavier: An FPGA-based mechanical keyboard with USB hub and comms interfaces

**原文链接**: [https://github.com/lsartory/Clavier](https://github.com/lsartory/Clavier)

Clavier：基于FPGA的开源机械键盘，采用全尺寸ISO布局、全键无冲，以及无鬼键的1000Hz轮询率。它包含一个双端口USB 2.0集线器和各种通信接口（JTAG、SPI、I²C、UART、GPIO），全部由VHDL编程的FPGA控制，无需ALU。

该项目具有完整的开源设计文件，包括用于4层PCB的KiCad文件（但由于小型元件，组装可能具有挑战性）以及用于键盘外壳的FreeCAD/OpenSCAD文件。存在两种外壳版本：第一种用于通用3D打印，第二种以8°角倾斜，旨在通过CNC加工实现更佳的人体工程学。

FPGA固件可以使用OSS CAD Suite构建，并通过JTAG进行编程，可以编程到SRAM用于临时配置，也可以编程到闪存中用于永久存储。一个专用的“咖啡键”可以锁定计算机或通过长按来重置FPGA。通信接口主要由CH347F芯片管理，直接GPIO连接除外。

硬件设计（PCB和外壳）在CERN开放硬件许可证版本2 - 许可下发布，FPGA代码在MIT许可证下发布，图像在CC BY 4.0许可证下发布。

---

## 54. 柏林字母博物馆即将关闭

**原文标题**: The Buchstabenmuseum Berlin is closing

**原文链接**: [https://www.buchstabenmuseum.de/en/](https://www.buchstabenmuseum.de/en/)

根据提供的信息，柏林字母博物馆即将关闭。然而，提供的文本片段并未明确说明关闭的原因或确切日期，而是强调了持续的存在和合作：精选的“Ks”（可能指博物馆藏品中的特定物品）正在柏林国家图书馆菩提树下大街分馆展出。这些展品旨在引导参观者前往国家图书馆内的“Kulturwerk”博物馆。这表明字母博物馆的部分藏品已转移或搬迁至国家图书馆。

---

## 55. 神笔公司发现降低笔成本的方法——在美国生产。

**原文标题**: Sharpie Found a Way to Make Pens More Cheaply–By Manufacturing Them in the U.S.

**原文链接**: [https://www.wsj.com/business/sharpie-us-production-cost-cutting-d9ba2abd](https://www.wsj.com/business/sharpie-us-production-cost-cutting-d9ba2abd)

好的，我将阅读提供的URL中的文章并提供摘要。

**摘要:**

《华尔街日报》的文章《夏比找到了一种更廉价的制笔方法——通过在美国生产》详细介绍了纽威品牌旗下的夏比如何通过将其大部分生产转移回美国来降低生产成本。这一举动与公司将生产外包给低工资国家的常见趋势形成对比。

夏比的成本降低战略涉及几个关键举措。首先，他们对美国工厂的自动化和先进制造技术进行了大量投资。这包括实施机器人装配线和优化生产流程，以提高效率并降低劳动力成本。他们还重新设计了一些制造流程，使其更精简、更快速。

其次，他们专注于简化笔的设计并减少组件数量。这不仅降低了材料成本，还简化了组装过程。

第三，他们实施了“本地化生产，服务本地”的制造方法，这使他们能够更接近消费者生产产品，从而降低运输成本并提高对市场需求的响应速度。

文章强调，这些变化使夏比的美国生产在全球市场上具有竞争力，即使劳动力成本更高。夏比战略的成功为其他希望将生产带回国内并在全球市场上竞争的美国制造商提供了一个潜在的模式。它表明，投资于自动化、流程优化和产品重新设计可以抵消外包的成本优势，并带来显著的成本节约。此举也对美国的就业和当地经济产生了积极影响。

---

## 56. Show HN: Cobalt – Nintendo DS 像素艺术绘画工作室

**原文标题**: Show HN: Cobalt – a pixel-art painting studio for the Nintendo DS

**原文链接**: [https://benbridle.com/projects/cobalt.html](https://benbridle.com/projects/cobalt.html)

Cobalt：一款像素艺术绘画程序，旨在创作富有表现力、纹理丰富的艺术作品。它可在Windows、Linux和Nintendo DS上运行。该软件强调速度和易用性，同时提供用于像素艺术创作的全面功能集。

主要功能包括可自定义画笔、用于纹理的随机散射、直线和曲线绘制、颜色和形状随机化、用于草稿的草图层、纹理填充和GIF导出。图像最多可使用八种用户选择的颜色，最大尺寸约为400x320像素。

用户可以在项目网站上试用在线演示，或从itch.io商店下载各种平台的演示。Cobalt的完整版本可在Windows、Linux、Nintendo DS和Bedrock上使用，可在itch.io上以5美元购买。

全面的文档可通过用户手册页面和可打印的快速入门指南（彩色和灰度）获得。 通过电子邮件提供支持。

---

## 57. DEC PDP-1 2025年手册

**原文标题**: A 2025 manual to the DEC PDP-1

**原文链接**: [https://obsolescence.dev/pdp1-manual.html](https://obsolescence.dev/pdp1-manual.html)

本文档是DEC PDP-1计算机的2025年手册，重点介绍其历史背景和现代实用方法，包括使用PiDP-1复制品。它强调该软件可在任何具有虚拟前面板的Linux机器上运行，欢迎没有复制品的用户。

本手册涵盖了PDP-1的历史，它作为早期交互式计算机的意义，以及PiDP-1项目复兴相关知识和社区的目标。它感谢Norbert Landsteiner、计算机历史博物馆和Al Kossow的bitsavers.org的贡献。

本文档提供了构建PiDP-1复制品和安装软件的说明，可以选择Raspberry Pi Zero 2W或Pi 5。该软件提供GUI、Web界面和外围应用程序，以满足不同的使用偏好。解释了`pdp1control`和`pdp1`命令，用于管理模拟器和外围设备。还包括有关使用USB存储器作为纸带以及为PiDP-1 Rack用户自定义GUI布局的说明。

该指南还详细介绍了使用感应开关，通过预配置的游戏、图形演示和软件实现快速启动选项。提供了在PDP-1和现代计算机之间交换文件的说明。

最后，附录解释了PiDP-1的软件架构，包括目录结构、启动选项和面板驱动程序，以实现用户自定义。

---

## 58. 雷霆扫描：妙用装置将打印机变扫描仪 (2004)

**原文标题**: Thunderscan: A clever device transforms a printer into a scanner (2004)

**原文链接**: [https://www.folklore.org/Thunderscan.html](https://www.folklore.org/Thunderscan.html)

这篇Folklore.org的文章详细介绍了Thunderscan的开发过程，这是一种巧妙的设备，它在20世纪80年代中期将ImageWriter打印机变成了Apple电脑的扫描仪。作者Andy Hertzfeld回忆说，他被Thunderware公司的Victor Bull和Tom Petrie招募，为该产品编写Macintosh软件。

Thunderscan的工作原理是用光学传感器取代打印机的色带盒，利用打印机精确的步进电机进行高分辨率扫描，成本远低于专用平板扫描仪。虽然具有创新性，但它也有局限性，特别是扫描速度慢，因为它每次扫描只捕获一条扫描线。

Hertzfeld描述了克服技术挑战的过程，例如通过实施Bill Atkinson修改的Floyd-Steinberg抖动算法来解决纸张堆积和Macintosh上的灰度渲染问题。他还添加了惯性滚动和可选双向扫描等功能。

Thunderscan于1984年12月发布，取得了商业上的成功，销售了约10万台，为Macintosh用户提供了经济实惠的扫描解决方案。虽然最终被平板扫描仪超越，但Thunderscan产生了持久的影响，使用户能够经济地捕获高分辨率图形。这篇文章还收录了用户们对该设备的美好回忆。

---

## 59. Prettier 的诞生

**原文标题**: Birth of Prettier

**原文链接**: [https://blog.vjeux.com/2025/javascript/birth-of-prettier.html](https://blog.vjeux.com/2025/javascript/birth-of-prettier.html)

文章《Prettier 的诞生》从其创建者 vjeux 的角度讲述了流行的代码格式化工具 Prettier 的起源故事。故事始于作者在大学期间对严格的代码格式化规则的早期体验，这启发了他将该过程自动化。后来，在 Facebook，他看到了团队之间需要一致的代码风格，并开始研究现有的解决方案，如 lint 修复器、gofmt 和 dartfmt，但这些方案都未能完全解决问题，通常是因为实现近乎完美的格式化需要大量的工作。

在寒假期间，两位同事开始构建 JavaScript 美化打印器，作者通过测试基础设施和竞争环境促进了他们的进展。当他们搁置该项目时，他全身心投入到完成它，利用了他在 Facebook 的政治资本。他选择基于 James Long 的 JavaScript 项目进行构建，以便更容易地进行社区贡献。

Prettier 成功的关键是使用 Jest 快照测试的严格测试过程，这使得格式化更改的轻松可视化和验证成为可能。基于“A prettier printer”论文的核心算法被证明具有非凡的通用性。他专注于通过使用幂等性测试来确保正确性：`prettier(input) == prettier(prettier(input))`。为了避免“空格与制表符圣战”，他战略性地选择了基于 Facebook 代码库中最常见的风格的格式化默认值，并提供了最少数量的选项。尽管在打印注释和链式方法方面存在挑战，Prettier 还是获得了广泛采用，并对 JavaScript 代码格式化实践产生了重大影响。

---

## 60. 伊利诺伊州推出通用电动汽车充电器，全州快充统一价15美元。

**原文标题**: Universal EV Chargers debuts $15 flat-rate fast charging across Illinois

**原文链接**: [https://electrek.co/2025/10/03/universal-ev-chargers-debuts-15-flat-rate-fast-charging-across-illinois/](https://electrek.co/2025/10/03/universal-ev-chargers-debuts-15-flat-rate-fast-charging-across-illinois/)

Universal EV Chargers 在伊利诺伊州推出15美元统一价快充模式。这种新定价取消了按时收费和意外附加费，为电动汽车驾驶员提供可预测且简单的充电体验。大多数电动汽车只需约30分钟即可达到80%的电量，费用为统一价。

驾驶员可以在 Universal EV Chargers 站点使用 CCS 或 NACS 连接器并通过扫描二维码来使用充电桩。无需会员资格，但 Universal EV 应用程序提供地图和收据等附加功能。该公司正在积极扩展其在伊利诺伊州主要高速公路和目的地附近的直流快充网络。

对于需要大量充电的驾驶员来说，统一收费模式是有利的，与按千瓦时收费相比，可节省大量费用。但是，对于快速补电来说，这可能不划算。行业评论员认为，需要类似于加油站的简化定价模式来刺激更广泛的电动汽车普及。

---

## 61. 像1984年那样自托管电子邮件

**原文标题**: Self-hosting email like it's 1984

**原文链接**: [https://maxadamski.com/blog/2025/10/email.html](https://maxadamski.com/blog/2025/10/email.html)

本文详细介绍了如何使用 Postfix 和 OpenDKIM 自行托管邮件服务器，重点是简化设置，无需网页邮件或用户帐户。作者认为，对于已经运行服务器的人来说，自行托管几乎是免费的，并且尽管最初的印象，但它并非过于复杂。

设置的核心包括将 Postfix 配置为 SMTP 服务器，以及使用 OpenDKIM 通过验证发件人的域来提高电子邮件的送达率。关键配置包括设置 `myhostname`、`myorigin`，以及使用 Let's Encrypt 证书为 MX 记录域启用 TLS 加密。

作者强调了 DNS 中 DKIM、SPF 和 DMARC 记录在建立电子邮件可信度方面的重要性。DKIM 涉及生成密钥对、发布公钥以及配置 OpenDKIM 以签署外发邮件。SPF 和 DMARC 记录指定授权的发送主机，并指示接收服务器如何处理未验证的邮件。

虽然最初尝试通过 Dovecot 实现 POP3/IMAP，但作者选择跳过它，转而通过 SSH 和 `mailx` 直接访问电子邮件。文章还提到了反向 DNS (PTR) 记录的重要性，尽管在没有它的情况下也可能实现 10/10 的声誉。

文章演示了向 Gmail 发送一封通过 SPF、DKIM 和 DMARC 检查的测试邮件。作者最后暗示了未来一篇关于使用 Python 构建电子邮件应用程序的文章，并邀请读者发送电子邮件反馈。

---

## 62. 法律专家谴责苹果屈服于白宫要求下架ICEBlock

**原文标题**: Legal experts condemn Apple bowing to White House's request to remove ICEBlock

**原文链接**: [https://text.npr.org/nx-s1-5561999](https://text.npr.org/nx-s1-5561999)

2025年，在检察长帕姆·邦迪施压后，苹果公司从其应用商店下架了ICEBlock应用程序，该程序可提醒用户注意移民和海关执法人员的存在。这一决定引发争议，法律专家指责苹果屈服于政府压力，通过“劝诱”进行审查。

ICEBlock应用程序被描述为“ICE目击事件的Waze”，是约书亚·艾伦为了应对日益加强的移民执法而创建的。苹果公司以“安全风险”为由将其下架，谷歌也下架了类似的应用。艾伦批评苹果此举是向独裁政权屈服，并辩称该应用促进了受保护的言论。

批评人士认为，苹果的举动开创了一个危险的先例，侵蚀了第一修正案的保护。民主与技术中心自由表达项目的凯特·鲁安认为，这是政府利用其影响力来扼杀自由表达。苹果首席执行官蒂姆·库克为维持与特朗普总统的良好关系所做的努力，以及可能受到影响苹果海外生产的关税政策的影响，加剧了人们的担忧。

康奈尔大学法学教授高塔姆·汉斯认为，苹果有理由提起劝诱诉讼，但他怀疑该公司会这样做，担心会引来政府进一步的要求。ICEBlock的下架被视为硅谷对特朗普政府的顺从的标志，并引发了对政府权力过度扩张和审查的担忧。

---

## 63. 斯德哥尔摩老电话塔

**原文标题**: Old Stockholm Telephone Tower

**原文链接**: [https://en.wikipedia.org/wiki/Old_Stockholm_telephone_tower](https://en.wikipedia.org/wiki/Old_Stockholm_telephone_tower)

斯德哥尔摩老电话塔，由Stockholms Allmänna Telefon AB于1887年建造，是一座80米高的金属结构，旨在连接瑞典斯德哥尔摩约5500条电话线。最初不受欢迎，后来建筑师弗里茨·埃克特为塔楼增添了角楼。

随着电话公司转向地下电缆，其主要功能变得多余，地下电缆于1913年完成。1939年后，该塔被改造成展示Nordiska Kompaniet广告的场所。1952年7月的一场火灾削弱了塔的结构，导致其因安全问题于1953年被拆除。该塔的历史和图像记录在各种来源中，包括维基共享资源和《瑞典日报》。

---

## 64. 钻孔振荡器

**原文标题**: Borehole Oscillators

**原文链接**: [https://www.gregegan.net/SCIENCE/Borehole/Borehole.html](https://www.gregegan.net/SCIENCE/Borehole/Borehole.html)

格雷格·伊根的《钻孔振荡器》探讨了落入穿过均匀密度球体的钻孔中的测试粒子的行为，比较了牛顿模型和广义相对论模型。

在牛顿物理学中，落入钻孔的粒子会经历简谐运动，其周期与在掠射圆形轨道上的粒子相同。文章提供了控制这种运动的方程，证明了它们的等价性。然后，它分析了这种球体周围真空中的径向运动，表明下降速度比穿过固体球体更快。点质量的极限情况允许两种延续：一种是摆动运动（椭圆轨道极限），另一种是“穿透”（下落-上升解），两者都接近达到r=0的相同时间。

文章随后深入研究了广义相对论，引入了两个史瓦西度规：一个用于球形质量外部的真空，另一个用于不可压缩流体球（均匀密度）。它解释了如何使用爱因斯坦方程推导出这些度规，强调了球体内部压力对引力吸引的自动平衡。文章讨论了相对论模型中质量、密度和半径之间的关系，并指出了由于组装过程中动能的增加而导致质量计算的反直觉方面。最后，它开始构建分析这些相对论系统中轨道的数学框架，使用测地线和基灵矢量场的概念来定义守恒量，如能量（E）和角动量（L）。文章为更深入地探索这些广义相对论背景下的径向运动奠定了基础。

---

## 65. 经济学博士就业市场的崩溃

**原文标题**: The collapse of the econ PhD job market

**原文链接**: [https://www.chrisbrunet.com/p/the-collapse-of-the-econ-phd-job](https://www.chrisbrunet.com/p/the-collapse-of-the-econ-phd-job)

克里斯托弗·布鲁内特的文章描绘了2025年经济学博士就业市场的严峻景象，认为其正自由落体。他利用美国经济协会的JOE和Econ Job Market（EJM）的数据，强调了职位发布的显著下降，尤其是终身教职，尽管经济学博士毕业生人数在不断增加。职位发布在三年内下降了约30%，而申请人数却达到历史最高水平，导致新博士的就业率很低。

除了学术界，政府和国际组织也减少了招聘，曾经可靠的备选方案——科技行业也在萎缩。布鲁内特指出了导致这种下降的四个结构性原因：本科经济学入学人数减少、即将到来的人口悬崖、人工智能自动化任务的兴起，以及由于经济学家在疫情期间对通货膨胀的错误描述而导致的公众信任丧失。

他总结说，对于大多数人来说，经济学博士不再是一项值得的投资，而是一场胜算很小的赌博，除非你来自顶尖院校。布鲁内特呼应了包括《纽约时报》文章在内的其他人提出的类似担忧，并认为知识分子生活的未来可能在于Substack等去中心化平台，因为传统的学术体系由于过度供给和博士项目之间缺乏协调而面临潜在的崩溃。他敦促该领域的从业者考虑非学术性选择。

---

## 66. 投球计时器后的棒球比赛时长

**原文标题**: Baseball durations after the pitch clock

**原文链接**: [https://leancrew.com/all-this/2025/09/baseball-durations-after-the-pitch-clock/](https://leancrew.com/all-this/2025/09/baseball-durations-after-the-pitch-clock/)

生成摘要时出错

---

## 67. Battery Buffered EV Charging

**原文标题**: Battery Buffered EV Charging

**原文链接**: [https://insideevs.com/news/774075/battery-buffered-tesla-chargers-explained/](https://insideevs.com/news/774075/battery-buffered-tesla-chargers-explained/)

生成摘要时出错

---

## 68. TrueVault (YC W14) Is Hiring a BDR (Ex-ECommerce Manager)

**原文标题**: TrueVault (YC W14) Is Hiring a BDR (Ex-ECommerce Manager)

**原文链接**: [https://www.ycombinator.com/companies/truevault/jobs/FaC8Apo-ecommerce-manager-bdr](https://www.ycombinator.com/companies/truevault/jobs/FaC8Apo-ecommerce-manager-bdr)

生成摘要时出错

---

## 69. Whiteboarding with AI

**原文标题**: Whiteboarding with AI

**原文链接**: [https://jrfernandez.com/whiteboarding-with-ai/](https://jrfernandez.com/whiteboarding-with-ai/)

生成摘要时出错

---

## 70. 作为创业公司CTO的五年：如何做、为何做、以及是否值得？(2024)

**原文标题**: Five years as a startup CTO: How, why, and was it worth it? (2024)

**原文链接**: [https://distinctplace.com/2024/09/11/five-years-as-startup-cto-was-it-all-worth-it/](https://distinctplace.com/2024/09/11/five-years-as-startup-cto-was-it-all-worth-it/)

This article is a reflection on the author's five-year journey as CTO of an early-stage startup. He recounts joining the company with a problematic Salesforce-based product and no tech team, and his initial hesitation, leading to his decision to give it a try.

He highlights the challenges of fixing the existing product and the necessity of building a new platform. He shares his approach of using Salesforce as a frontend while migrating the backend to their own APIs. This led to his full commitment to the startup.

The author emphasizes the importance of experienced, hands-on initial hires to build the team across Platform, Backend, Frontend, QA, and Design. He discusses tech stack choices (AWS, Golang, React) and the crucial role of QA and good designers. He also touches on the importance of leadership in creating a supportive environment for the team.

The author reflects on the importance of personal well-being. He concludes by sharing key takeaways from his startup experience, emphasizing the need for financial reserves, realistic timelines, living in the present, early team building, asking questions, understanding business problems, proactive ownership, prioritizing remote work, and continuous learning. He also notes his availability for fractional CTO roles.


---

## 71. Fluid Glass

**原文标题**: Fluid Glass

**原文链接**: [https://chiuhans111.github.io/fluidglass/](https://chiuhans111.github.io/fluidglass/)

生成摘要时出错

---

## 72. Show HN: Run – a CLI universal code runner I built while learning Rust

**原文标题**: Show HN: Run – a CLI universal code runner I built while learning Rust

**原文链接**: [https://github.com/Esubaalew/run](https://github.com/Esubaalew/run)

生成摘要时出错

---

## 73. Offline card payments should be possible no later than 1 July 2026

**原文标题**: Offline card payments should be possible no later than 1 July 2026

**原文链接**: [https://www.riksbank.se/en-gb/press-and-published/notices-and-press-releases/press-releases/2025/offline-card-payments-should-be-possible-no-later-than-1-july-2026/](https://www.riksbank.se/en-gb/press-and-published/notices-and-press-releases/press-releases/2025/offline-card-payments-should-be-possible-no-later-than-1-july-2026/)

生成摘要时出错

---

## 74. Zig builds are getting faster

**原文标题**: Zig builds are getting faster

**原文链接**: [https://mitchellh.com/writing/zig-builds-getting-faster](https://mitchellh.com/writing/zig-builds-getting-faster)

生成摘要时出错

---

## 75. Modern Font Stacks

**原文标题**: Modern Font Stacks

**原文链接**: [https://modernfontstacks.com/](https://modernfontstacks.com/)

生成摘要时出错

---

## 76. EasyOS – An experimental Linux distribution (2025)

**原文标题**: EasyOS – An experimental Linux distribution (2025)

**原文链接**: [https://easyos.org/about/how-and-why-easyos-is-different.html](https://easyos.org/about/how-and-why-easyos-is-different.html)

生成摘要时出错

---

## 77. Study confirms that pianists can shape piano timbre through touch

**原文标题**: Study confirms that pianists can shape piano timbre through touch

**原文链接**: [https://neurosciencenews.com/piano-touch-timbre-neuroscience-29755/](https://neurosciencenews.com/piano-touch-timbre-neuroscience-29755/)

A recent study by the NeuroPiano Institute has scientifically confirmed that pianists can consciously alter the timbre of piano notes through subtle variations in their touch. Researchers used a high-speed sensor system to capture key movements of professional pianists as they played with different timbre intentions (e.g., bright/dark, light/heavy). The recordings showed that listeners, both trained and untrained, were able to distinguish the intended timbres.

The study identified specific key movement features, like acceleration during escapement and hand synchronization, directly linked to perceived timbre differences. Critically, by manipulating only these specific movement features, researchers were able to elicit changes in perceived timbre in listeners, proving a causal relationship. This validates a long-debated idea that pianists' touch can indeed shape sound beyond pitch and volume.

This research reveals that timbre manipulation isn't just a metaphor, but a demonstrable motor skill. This discovery has implications for music education, offering the potential for more efficient training methods and personalized recommendations. Furthermore, the understanding of how refined body movement shapes artistic perception could be applied to fields like rehabilitation, skill transfer, and human interface design, showcasing the broader significance of this research beyond music.


---

## 78. How I influence tech company politics as a staff software engineer

**原文标题**: How I influence tech company politics as a staff software engineer

**原文链接**: [https://www.seangoedecke.com/how-to-influence-politics/](https://www.seangoedecke.com/how-to-influence-politics/)

生成摘要时出错

---

## 79. Social anxiety isn't about being liked

**原文标题**: Social anxiety isn't about being liked

**原文链接**: [https://chrislakin.blog/p/social-anxiety](https://chrislakin.blog/p/social-anxiety)

生成摘要时出错

---

## 80. Microsoft 365 Copilot's commercial failure

**原文标题**: Microsoft 365 Copilot's commercial failure

**原文链接**: [https://www.perspectives.plus/p/microsoft-365-copilot-commercial-failure](https://www.perspectives.plus/p/microsoft-365-copilot-commercial-failure)

生成摘要时出错

---

## 81. Scientists are discovering a powerful new way to prevent cancer

**原文标题**: Scientists are discovering a powerful new way to prevent cancer

**原文链接**: [https://www.economist.com/science-and-technology/2025/09/02/scientists-are-discovering-a-powerful-new-way-to-prevent-cancer](https://www.economist.com/science-and-technology/2025/09/02/scientists-are-discovering-a-powerful-new-way-to-prevent-cancer)

生成摘要时出错

---

## 82. Asked to do something illegal at work? Here's what these software engineers did

**原文标题**: Asked to do something illegal at work? Here's what these software engineers did

**原文链接**: [https://blog.pragmaticengineer.com/asked-to-do-something-illegal-at-work/](https://blog.pragmaticengineer.com/asked-to-do-something-illegal-at-work/)

生成摘要时出错

---

## 83. The Beer Can (2023)

**原文标题**: The Beer Can (2023)

**原文链接**: [https://brr.fyi/posts/beer-can](https://brr.fyi/posts/beer-can)

生成摘要时出错

---

## 84. The Faroes

**原文标题**: The Faroes

**原文链接**: [https://photoblog.nk412.com/Faroe2025/Faroes/n-cPCNFr](https://photoblog.nk412.com/Faroe2025/Faroes/n-cPCNFr)

生成摘要时出错

---

## 85. Exploring .NET Core platform intrinsics: Accelerating SHA-256 on ARMv8 (2018)

**原文标题**: Exploring .NET Core platform intrinsics: Accelerating SHA-256 on ARMv8 (2018)

**原文链接**: [https://mijailovic.net/2018/06/06/sha256-armv8/](https://mijailovic.net/2018/06/06/sha256-armv8/)

生成摘要时出错

---

## 86. Where it's at://

**原文标题**: Where it's at://

**原文链接**: [https://overreacted.io/where-its-at/](https://overreacted.io/where-its-at/)

生成摘要时出错

---

## 87. Sora Update #1

**原文标题**: Sora Update #1

**原文链接**: [https://blog.samaltman.com/sora-update-number-1](https://blog.samaltman.com/sora-update-number-1)

生成摘要时出错

---

## 88. Binary Formats Gallery

**原文标题**: Binary Formats Gallery

**原文链接**: [https://formats.kaitai.io/](https://formats.kaitai.io/)

生成摘要时出错

---

## 89. Alibaba cloud FPGA: the $200 Kintex UltraScale+

**原文标题**: Alibaba cloud FPGA: the $200 Kintex UltraScale+

**原文链接**: [https://essenceia.github.io/projects/alibaba_cloud_fpga/](https://essenceia.github.io/projects/alibaba_cloud_fpga/)

生成摘要时出错

---

## 90. The UK is still trying to backdoor encryption for Apple users

**原文标题**: The UK is still trying to backdoor encryption for Apple users

**原文链接**: [https://www.eff.org/deeplinks/2025/10/uk-still-trying-backdoor-encryption-apple-users](https://www.eff.org/deeplinks/2025/10/uk-still-trying-backdoor-encryption-apple-users)

生成摘要时出错

---

## 91. Answering questions about Android developer verification

**原文标题**: Answering questions about Android developer verification

**原文链接**: [https://android-developers.googleblog.com/2025/09/lets-talk-security-answering-your-top.html](https://android-developers.googleblog.com/2025/09/lets-talk-security-answering-your-top.html)

生成摘要时出错

---

## 92. Litestream v0.5.0

**原文标题**: Litestream v0.5.0

**原文链接**: [https://fly.io/blog/litestream-v050-is-here/](https://fly.io/blog/litestream-v050-is-here/)

生成摘要时出错

---

## 93. The Art of Color... Science?

**原文标题**: The Art of Color... Science?

**原文链接**: [https://nikonrumors.com/2025/09/30/the-art-of-color-science.aspx/](https://nikonrumors.com/2025/09/30/the-art-of-color-science.aspx/)

生成摘要时出错

---

## 94. PEP 810 – Explicit lazy imports

**原文标题**: PEP 810 – Explicit lazy imports

**原文链接**: [https://peps.python.org/pep-0810/](https://peps.python.org/pep-0810/)

生成摘要时出错

---

## 95. Why Developer Experience Is More Than Just Better Tooling

**原文标题**: Why Developer Experience Is More Than Just Better Tooling

**原文链接**: [https://blog.pragmaticdx.com/p/why-developer-experience-is-more](https://blog.pragmaticdx.com/p/why-developer-experience-is-more)

生成摘要时出错

---

## 96. Low-dose radiation offers relief to people with knee osteoarthritis

**原文标题**: Low-dose radiation offers relief to people with knee osteoarthritis

**原文链接**: [https://www.astro.org/news-and-publications/news-and-media-center/news-releases/2025/low-dose-radiation-therapy-offers-substantial-relief-to-people-with-painful-knee-osteoarthritis](https://www.astro.org/news-and-publications/news-and-media-center/news-releases/2025/low-dose-radiation-therapy-offers-substantial-relief-to-people-with-painful-knee-osteoarthritis)

生成摘要时出错

---

## 97. Advanced Matrix Multiplication Optimization on Multi-Core Processors (2024)

**原文标题**: Advanced Matrix Multiplication Optimization on Multi-Core Processors (2024)

**原文链接**: [https://salykova.github.io/gemm-cpu](https://salykova.github.io/gemm-cpu)

生成摘要时出错

---

## 98. Niri – A scrollable-tiling Wayland compositor

**原文标题**: Niri – A scrollable-tiling Wayland compositor

**原文链接**: [https://github.com/YaLTeR/niri](https://github.com/YaLTeR/niri)

生成摘要时出错

---

## 99. Jeff Bezos says AI is in a bubble but society will get 'gigantic' benefits

**原文标题**: Jeff Bezos says AI is in a bubble but society will get 'gigantic' benefits

**原文链接**: [https://www.cnbc.com/2025/10/03/jeff-bezos-ai-in-an-industrial-bubble-but-society-to-benefit.html](https://www.cnbc.com/2025/10/03/jeff-bezos-ai-in-an-industrial-bubble-but-society-to-benefit.html)

生成摘要时出错

---

## 100. California needs to learn from Houston and Dallas about homelessness

**原文标题**: California needs to learn from Houston and Dallas about homelessness

**原文链接**: [https://www.governance.fyi/p/california-needs-to-learn-from-houston](https://www.governance.fyi/p/california-needs-to-learn-from-houston)

生成摘要时出错

---

