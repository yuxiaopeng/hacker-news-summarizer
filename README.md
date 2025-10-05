# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-10-05.md)

*最后自动更新时间: 2025-10-05 17:43:21*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 2 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 3 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 4 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 5 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 6 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 7 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 8 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 9 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 10 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 11 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 12 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 13 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 14 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 15 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 16 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 17 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 18 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 19 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 20 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 21 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 22 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 23 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 24 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 25 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 26 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 27 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 28 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 29 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 30 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 31 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 32 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 33 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 34 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 35 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 36 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 37 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 38 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 39 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 40 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 41 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 42 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 43 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 44 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 45 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 46 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 47 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 48 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 49 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 50 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 51 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 52 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 53 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 54 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 55 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 56 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 57 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 58 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 59 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 60 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 61 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 62 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 63 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 64 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 65 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 66 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 67 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 68 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 69 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 70 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 71 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 72 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 73 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 74 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 75 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 76 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 77 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 78 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 79 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 80 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 81 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 82 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 83 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 84 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 85 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 86 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 87 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 88 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 89 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 90 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 91 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 92 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 93 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 94 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 95 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 96 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 97 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 98 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 99 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 100 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 101 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 102 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 103 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 104 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 105 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 106 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 107 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 108 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 109 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 110 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 111 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 112 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 113 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 114 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 115 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 116 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 117 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 118 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 119 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 120 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 121 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 122 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 123 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 124 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 125 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 126 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 127 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 128 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 129 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 130 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 131 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 132 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 133 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 134 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 135 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 136 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 137 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 138 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 139 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 140 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 141 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 142 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 143 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 144 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 145 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 146 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 147 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 148 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 149 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 150 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 151 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 152 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 153 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 154 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 155 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 156 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 157 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 158 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 159 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 160 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 161 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 162 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 163 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 164 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 165 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 166 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 167 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 168 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 169 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 170 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 171 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 172 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 173 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 174 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 175 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 176 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 177 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 178 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 179 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 180 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 181 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 182 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 183 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 184 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 185 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 186 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 187 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 188 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 189 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 190 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 191 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 192 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 193 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 194 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 195 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 196 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 197 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 198 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 199 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 200 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
