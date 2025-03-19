# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hn_summary_2025-03-19.md)

*最后自动更新时间: 2025-03-19 11:21:54*
## 1. **休闲研究的失落艺术**

或者，可以稍微调整得更流畅一些：

**作为休闲的研究：失落的艺术**

两种译法都基本保持了原文简洁的风格和意思。 第一种更直译，第二种则稍微更符合中文的表达习惯。


**原文标题**: The Lost Art of Research as Leisure

**原文链接**: [https://kasurian.com/p/research-as-leisure](https://kasurian.com/p/research-as-leisure)

玛丽亚姆·马哈茂德在《作为休闲的研究的失落艺术》中探讨了当代社会文化危机，认为其根源在于注意力分散和肤浅的参与，削弱了共同意义和文化连贯性的基础。作者回顾了弗吉尼亚·伍尔夫、E.B.·怀特和苏珊·桑塔格等人对阅读未来的担忧，他们预见了“视听”对人类大脑和灵魂的腐蚀性影响。

马哈茂德借鉴了T.S.艾略特和约瑟夫·派珀的观点，提出恢复文化的关键在于重拾古老的休闲概念——并非指无所事事，而是指有目的的沉思。派珀认为，休闲是文化的基石，是一种不受约束的研究形式，是对知识的有意识和定向的探索。作者认为，这种“作为休闲的研究”鼓励人们以好奇心和敬畏感来学习和探索，而不是僵化的确定性。

文章最后呼吁转变阅读和探究的视角，将其视为一种充满乐趣和目的的求知行为，而非沉重的负担。 通过拥抱“休闲作为研究”，并与过去伟大的思想家进行思想交流，我们可以重建“社会模式”，并在支离破碎的现代社会中创造一种新的文化想象力。


---

## 2. 两个新款 PebbleOS 手表


**原文标题**: Two new PebbleOS watches

**原文链接**: [https://ericmigi.com/blog/introducing-two-new-pebbleos-watches/](https://ericmigi.com/blog/introducing-two-new-pebbleos-watches/)

文章介绍了两款运行开源 PebbleOS 的新型智能手表：Core 2 Duo 和 Core Time 2。Core 2 Duo 是一款类似 Pebble 2 的升级版，拥有黑白电子墨水屏、聚碳酸酯框架和 30 天电池续航，售价 149 美元，预计 7 月发货。Core Time 2 是作者的梦想之作，配备更大的 64 色电子墨水屏、金属框架和 30 天电池续航（预估），售价 225 美元，预计 12 月发货。两款手表都兼容 Pebble 应用商店中数千款应用，采用标准表带，并具备防水功能。Core Time 2 还加入了触摸屏和心率监测功能。

作者强调，这两款手表的开发目标是打造一款符合自身需求的理想智能手表，具备常显电子墨水屏、长续航、简洁设计、实体按键和可定制性。由于显示屏库存有限，两款手表都将限量生产，建议提前预订。文中还解释了硬件规格选择的考量，并坦承项目可能存在延迟和缺陷。文章明确指出，这款手表并非为追求完美体验或专业运动功能的用户设计，而是面向喜欢 Pebble 风格和开源生态系统的用户。


---

## 3. 当月分子


**原文标题**: The Molecule of the Month

**原文链接**: [https://www.chm.bris.ac.uk/motm/motm.htm](https://www.chm.bris.ac.uk/motm/motm.htm)

“分子月刊”是一个化学网站，自 1996 年 1 月开始每月更新，旨在介绍一种有趣的分子。该网站汇集了来自英国、美国以及世界各地大学化学系或商业网站提供的各种分子信息，力求提供实用且兼具娱乐性的内容。

读者可以通过 Twitter (@MoleculeM) 或 RSS 新闻源获取每月的更新。网站欢迎投稿，并提供了投稿指南文档。为了能够正常浏览页面，可能需要特定的软件和插件，例如 Adobe Acrobat、VRML 查看器、CHIME 插件或支持 HTML5 的浏览器。

网站提供了一个按字母顺序排列的分子列表，点击即可跳转至相应分子的介绍。每个分子的页面都提供 HTML、PDF 等多种格式，部分分子页面还包含 VRML、CHIME 或 Java 结构文件。网站内容已被汇编成书籍。

文章还列出了从 2025 年 3 月到 2019 年 11 月期间的各个分子及其贡献者和所在地，例如硼嗪（Borazine）、二氢茉莉酮酸甲酯（Hedione）、硅烷（Silane）、孕酮（Progesterone）等。每个分子都有 HTML 和 JSmol 格式的版本。


---

## 4. 通过重新构建 Ubuntu 软件包，使构建速度提升 90%


**原文标题**: Make Ubuntu packages 90% faster by rebuilding them

**原文链接**: [https://gist.github.com/jwbee/7e8b27e298de8bbbf8abfa4c232db097](https://gist.github.com/jwbee/7e8b27e298de8bbbf8abfa4c232db097)

这篇文章讲述了如何通过重新编译 Ubuntu 软件包 `jq`，显著提升其性能。作者发现，即使简单地重新编译 `jq` 的源代码，也能获得细微的性能提升。更进一步，通过使用 Clang 编译器，并添加 `-O3` 优化级别、LTO（链接时优化）以及 `-DNDEBUG` 等编译选项，可以将性能提升 20%。

文章指出，内存分配是性能瓶颈，因此作者尝试了不同的内存分配器。通过预加载 (LD_PRELOAD) TCMalloc、jemalloc 和 mimalloc 等分配器，发现 mimalloc 效果最佳，性能提升高达 44%。最终，作者将 mimalloc 集成到 `jq` 的编译过程中，结果表明，重新编译后的 `jq` 比 Ubuntu 官方提供的版本快近 2 倍。

总之，文章证明了通过重新编译 Ubuntu 软件包，并结合更优的编译器、优化选项以及内存分配器，可以显著提高性能。mimalloc 在文中表现突出，为 `jq` 带来了可观的性能提升。


---

## 5. 苹果限制 Pebble 在 iPhone 上的优秀表现


**原文标题**: Apple restricts Pebble from being awesome with iPhones

**原文链接**: [https://ericmigi.com/blog/apple-restricts-pebble-from-being-awesome-with-iphones/](https://ericmigi.com/blog/apple-restricts-pebble-from-being-awesome-with-iphones/)

这篇文章探讨了苹果公司对第三方智能手表，尤其是Pebble，在iPhone上的功能限制。作者指出，由于苹果公司系统性的限制，要在iPhone上构建与Apple Watch体验相当的第三方智能手表体验非常困难，甚至不可能。这些限制包括无法发送短信或iMessage、无法回复通知或执行操作、缺乏进程间通信（IPC）支持、以及对应用商店和第三方开发的严格控制。

作者回顾了Pebble过去为突破这些限制所做的努力，例如与AT&T的SMS-over-IP合作。他还提到了针对苹果公司的反垄断诉讼和相关立法，认为苹果公司利用其市场力量锁定消费者，减少竞争和创新。

尽管面临这些挑战，作者表示他们仍然会为rePebble开发iOS应用，因为大量的用户使用iPhone。但他明确指出，iOS应用的功能将始终不如Android应用，并且某些功能会先在Android上推出。最后，他呼吁iPhone用户积极发声，推动苹果公司改变其限制政策，或者考虑转用Android手机，同时支持相关的反垄断立法。文章的核心观点是，苹果公司通过其封闭的生态系统人为地限制了第三方智能手表在iPhone上的功能，从而维护其Apple Watch的市场地位。


---

## 6. 通过动画可视化数据结构与算法


**原文标题**: Visualising data structures and algorithms through animation

**原文链接**: [https://visualgo.net/en](https://visualgo.net/en)

VisuAlgo.net 是一个通过动画可视化数据结构和算法的在线平台，其目标是帮助用户更深入地理解这些概念。该项目于 2011 年由新加坡国立大学的 Steven Halim 副教授发起，并持续得到 Optiver 的资助。目前，平台提供 24 个可视化模块，并配有在线测验系统，可以自动生成问题并进行评分，帮助学生检验学习效果。

VisuAlgo 具有以下几个关键特性：

*   **动画可视化：** 通过动画生动地展示数据结构和算法的运行过程。
*   **多语言支持：** 支持英语、中文和印尼语三种语言。
*   **用户自定义输入：** 允许用户输入自己的数据进行算法演示。
*   **在线测验系统：** 提供自动生成和评分的在线测验，巩固学习效果。
*   **移动设备友好：** 推出移动 (lite) 版本，可以在智能手机屏幕上使用部分功能。
*   **持续开发：** 仍在不断开发新的可视化模块和功能。

VisuAlgo 不仅适用于在新加坡国立大学学习数据结构和算法的学生，也适用于全球对这些概念感兴趣的用户。该网站鼓励用户通过社交媒体、课程网页等方式分享，但禁止下载和托管其客户端文件。VisuAlgo 项目团队欢迎用户提供关于错误报告和新功能的建议。


---

## 7. 显示 HN: 我做了一个工具，可以将推文移植到 Bluesky，同时保持其原始日期


**原文标题**: Show HN: I made a tool to port tweets to Bluesky mantaining their original date

**原文链接**: [https://bluemigrate.com](https://bluemigrate.com)

这篇 Show HN 帖子介绍了一款名为 BlueMigrate 的工具，它旨在帮助用户将他们的 Twitter 推文迁移到 Bluesky 平台，同时保留推文的原始发布日期。该工具声称能“只需点击几下”即可完成迁移。帖子附带了指向 bluemigrate.com 的链接，并展示了一些精选的 Bluesky 用户个人资料。此外，帖子还提供了一个付费广告位，允许用户支付 9.99 美元/周的费用，使其个人资料在 BlueMigrate 的主页上获得曝光。 总而言之，这篇文章主要是在宣传 BlueMigrate 的功能和便捷性，以及它为 Bluesky 用户提供的增值服务。


---

## 8. Crew-9 Returns to Earth

**原文标题**: Crew-9 Returns to Earth

**原文链接**: [https://www.spacex.com/launches/mission/?missionId=crew-9-return](https://www.spacex.com/launches/mission/?missionId=crew-9-return)

生成摘要时出错

---

## 9. Some notes on Grafana Loki's new "structured metadata"

**原文标题**: Some notes on Grafana Loki's new "structured metadata"

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/sysadmin/GrafanaLokiStructuredMetadata](https://utcc.utoronto.ca/~cks/space/blog/sysadmin/GrafanaLokiStructuredMetadata)

生成摘要时出错

---

## 10. PostgreSQL中的选择性异步提交 – 平衡持久性和性能


**原文标题**: Selective async commits in PostgreSQL – balancing durability and performance

**原文链接**: [https://www.shayon.dev/post/2025/75/selective-asynchronous-commits-in-postgresql-balancing-durability-and-performance/](https://www.shayon.dev/post/2025/75/selective-asynchronous-commits-in-postgresql-balancing-durability-and-performance/)

Shayon Mukherjee 的文章深入探讨了 PostgreSQL 中的 `synchronous_commit` 设置，以及如何在数据持久性与性能之间实现平衡。默认情况下，PostgreSQL 采用同步提交，保证数据安全，但会牺牲性能。异步提交通过在 WAL 记录刷新到磁盘之前确认事务完成，显著提高吞吐量，尤其是在 I/O 受限的系统中。作者通过实验观察到了 I/O 降低、CPU 使用率下降以及 TPS 提升。

然而，异步提交引入了一个“风险窗口”，在此期间数据库崩溃可能导致数据丢失。文章强调，`synchronous_commit` 不必是全局性的“要么全有要么全无”设置，它可以针对会话、事务或特定操作进行调整。例如，可以使用 Ruby on Rails 在代码块中临时禁用同步提交，从而提高非关键批量操作的性能。

文章还提及了 `synchronous_commit` 的中间设置（`remote_apply`、`remote_write`、`local`），这些设置提供了不同的性能和持久性平衡。但作者发现，至少在 Aurora PostgreSQL 中，将 `synchronous_commit` 设置为 `OFF` 带来的收益最大。作者鼓励读者分享他们在生产环境中使用 `synchronous_commit` 的经验。


---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-03-19](output/hn_summary_2025-03-19.md) |
