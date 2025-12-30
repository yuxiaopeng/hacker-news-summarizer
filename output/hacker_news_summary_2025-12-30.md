# Hacker News 热门文章摘要 (2025-12-30)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Public Sans —— 一款强健、中性的字体

**原文标题**: Public Sans – A strong, neutral typeface

**原文链接**: [https://public-sans.digital.gov/](https://public-sans.digital.gov/)

**Public Sans** 是一款由美国网络设计系统 (USWDS) 设计的稳重且中性的字体，适用于界面、正文和标题等多种场景。该项目目前版本为 2.001，是一个托管在 GitHub 上的开源项目，公众可以下载该字体并为其持续开发做出贡献。

---

## 2. Toro：将应用程序部署为单内核

**原文标题**: Toro: Deploy Applications as Unikernels

**原文链接**: [https://github.com/torokernel/torokernel](https://github.com/torokernel/torokernel)

**Toro** 是一个专为将应用程序部署为微型虚拟机 (microVMs) 而设计的极简 Unikernel。通过利用 **virtio-fs** 进行文件系统访问以及 **virtio-vsocket** 进行网络通信，Toro 实现了针对性能和效率优化的轻量级架构。

**核心特性：**
*   **架构与硬件：** 支持 x86-64 系统和高达 512GB 的内存。
*   **虚拟化：** 兼容 QEMU-KVM microvm 和 Firecracker。
*   **性能：** 具备极速启动、微型镜像体积，以及协作式 I/O 密集型线程调度器。
*   **调试：** 内置 gdbstub，便于故障排查。

**部署与使用：**
开发者可以使用预配置的 Docker 镜像 (`torokernel/torokernel-dev`) 快速测试 Toro，该镜像包含了所有必要工具。部署由 `CloudIt.py` 脚本管理。该项目提供了几个实际示例：
1.  **HelloWorld：** Unikernel 运行的基础演示。
2.  **StaticWebServer：** 演示使用 `virtiofsd` 提供文件服务，并通过 `socat` 在 vsock 上进行端口转发。
3.  **Intercore Communication：** 演示多核如何利用 VirtIOBus 设备进行通信。

**社区与开发：**
Toro 是一个采用 **GPLv3** 协议的开源项目。它拥有悠久的开发历史，在 2015 年至 2024 年间的 FOSDEM、KVM Forum 和 Open Source Summit 等会议上均有相关技术分享。最近的更新包括对 MPI（消息传递接口）应用程序的支持。用户可以通过 GitHub 仓库为项目做出贡献，或加入专门的 Google Group 参与讨论。

---

## 3. Netflix: Open Content

**原文标题**: Netflix: Open Content

**原文链接**: [https://opencontent.netflix.com/](https://opencontent.netflix.com/)

生成摘要时出错

---

## 4. 非零和博弈

**原文标题**: Non-Zero-Sum Games

**原文链接**: [https://nonzerosum.games/](https://nonzerosum.games/)

**非零和博弈**（Non-Zero-Sum Games）是一个由“非零和詹姆斯”（Non-Zero-Sum James）主持的“助益世界”型网站和播客。该平台致力于探索“双赢局面”的概念——即通过合作实现互利的场景——并探讨这些动态机制对于解决复杂的全球问题和构建美好未来为何至关重要。

其内容聚焦于几个核心领域，包括：
*   **博弈论：** 分析策略互动与协作博弈。
*   **道德哲学与伦理经济学：** 使金融和社会体系与人类价值观及伦理保持一致。
*   **人工智能：** 探索技术的未来及其在社会中的作用。
*   **自然与复杂性：** 研究自然界中的合作以及意识与历史的基础。

网站设有丰富多样的类别，从面向新手的“趣味区”，到对“非零和英雄”（合作的倡导者）的深度探讨以及互动模拟。詹姆斯凭借其创意背景，将该项目定位为一场协作之旅。他鼓励通过分享、辩论和共同创作来进行社区参与，这一切都植根于这样一个哲学信念：我们的成功与他人的福祉密不可分。

---

## 5. 大英帝国的韧性海底电报网络

**原文标题**: The British Empire's Resilient Subsea Telegraph Network

**原文链接**: [https://subseacables.blogspot.com/2025/12/the-british-empires-resilient-subsea.html](https://subseacables.blogspot.com/2025/12/the-british-empires-resilient-subsea.html)

By 1902, the British Empire had established the "Red Line," a global subsea telegraph network that revolutionized imperial communication by reducing delivery times to minutes or hours. As highlighted by Dr. Michael Delaunay, the network's defining characteristic was its extreme resilience.

This reliability was achieved through several strategic layers:
*   **Redundant Topology:** The network utilized a ring configuration, allowing traffic to be rerouted in the opposite direction if a disruption occurred.
*   **Multiple Links:** By placing numerous cables between endpoints, the British military ensured that total communication failure was nearly impossible. For instance, the Committee of Imperial Defense estimated that isolating the British Isles would require severing 57 separate cables.
*   **Self-Sufficiency:** The Empire controlled the entire lifecycle of the network, possessing the sole capability to manufacture and repair all components.
*   **Naval Protection:** The security of this infrastructure was further guaranteed by the British Navy, which at the time had no equal.

Ultimately, the Red Line provided a secure, redundant, and independently maintained communication backbone that was vital to the administration and defense of the British Empire.

---

## 6. 海底电缆的遗产

**原文标题**: The Legacy of Undersea Cables

**原文链接**: [https://blog.sciencemuseumgroup.org.uk/the-legacy-of-undersea-cables/](https://blog.sciencemuseumgroup.org.uk/the-legacy-of-undersea-cables/)

海底电缆是全球通信的支柱，承载着全球97%的互联网数据。虽然现代用户往往将其归功于卫星或“云端”，但这一关键基础设施实际上依赖于长达120万公里的光缆，它们支撑着全球商业、政府及军事运作。

本文强调了当今的网络是如何植根于19世纪的帝国主义。由英美两国开创的首批电报电缆曾是地缘政治影响力的工具，旨在加强殖民联系。这些早期电缆的一种关键材料是古塔胶，这是一种从马来亚树木中提取的天然防水塑料。对这种树液的巨大需求几乎导致该物种灭绝。此外，尽管西方声称取得了技术上的成功，但马来人提供的关键环境知识和劳动力在很大程度上被忽视了。

在地缘政治上，电缆被战略性地布置在斐济等“网络化岛屿”上，这些岛屿曾是英国“全红线”（all red line）的枢纽——这是一套从未触及外国领土的安全通信系统。现代光缆通常沿袭这些相同的帝国路线。

如今，尽管99%的海底电缆由私人所有，但它们仍处于全球权力格局的中心。正如近期波罗的海发生的干扰事件所反映的那样，它们极易受到自然灾害和蓄意破坏的影响。然而，电缆也蕴含着巨大的经济潜力；例如谷歌的“太平洋连接”（Pacific Connect）等项目，旨在为太平洋岛屿提升数字化韧性并创造就业机会。归根结底，海底电缆的历史反映了殖民控制的遗产、对环境的影响，以及在数字时代物理连接持续存在的战略重要性。

---

## 7. Postgres 扩展补充 pgvector，提升性能与扩展性。

**原文标题**: Postgres extension complements pgvector for performance and scale

**原文链接**: [https://github.com/timescale/pgvectorscale](https://github.com/timescale/pgvectorscale)

**pgvectorscale** 是由 Timescale 使用 Rust 开发的一款开源 PostgreSQL 扩展，旨在补充 **pgvector**，显著提升 AI 应用的性能和可扩展性。它引入了三大核心创新：

1. **StreamingDiskANN：** 一种受微软 DiskANN 研究启发的新型索引类型，专为高性能嵌入（embedding）搜索而设计。
2. **统计二值量化 (SBQ)：** 一种在标准二值量化基础上改进的压缩方法，旨在优化存储并提升速度。
3. **基于标签的过滤搜索：** 基于微软的 Filtered DiskANN，允许用户将向量相似度搜索与标签过滤（使用 smallint 数组）相结合，以获得更精确、更高效的结果。

**性能基准测试**
在 5000 万条嵌入的数据集上，配备 `pgvectorscale` 的 PostgreSQL 表现优于 Pinecone 的存储优化型 (s1) 索引。在 AWS 自托管环境下，其 **p95 延迟降低了 28 倍**，**查询吞吐量提升了 16 倍**，且**成本降低了 75%**。

**核心功能**
* **索引：** 支持使用 `diskann` 索引进行余弦、L2 和内积距离计算。
* **过滤：** 提供两种方法——集成在索引中的优化版标签过滤，以及通过任意 `WHERE` 子句进行的标准后置过滤。
* **调优：** 为索引构建阶段（如 `num_neighbors`、`storage_layout`）和查询阶段（如 `query_rescore`）提供可调参数，以平衡准确性与性能。
* **可扩展性：** 支持大规模数据集的并行索引构建，并针对内存效率进行了存储优化。

**安装与获取**
该扩展使用 PGRX 框架编写。可以通过预构建的 Docker 容器、源码编译或作为 Timescale Cloud 的托管服务进行安装。在创建扩展时，使用 `CASCADE` 命令会自动安装所需的 `pgvector` 依赖项。

---

## 8. 易于上手的 Swift 并发

**原文标题**: Approachable Swift Concurrency

**原文链接**: [https://fuckingapproachableswiftconcurrency.com/en/](https://fuckingapproachableswiftconcurrency.com/en/)

本文概述了一种现代且简化的 Swift 并发处理方法，即从复杂的回调和手动线程管理转向由编译器强制执行的“隔离”模型。

**Async/Await 与任务 (Tasks)**
Swift 使用 `async/await` 来处理对 I/O 密集型工作的等待，而不会阻塞线程。代码在 `await` 处暂停（挂起），并在工作完成后恢复。对于并行工作，`async let` 和 `TaskGroup` 提供了结构化并发，确保子任务得到正确的管理、取消和清理。`Tasks` 充当了同步代码与异步代码之间的桥梁。

**隔离域 (Isolation Domains)**
该系统通过隔离边界取代了传统的线程管理：
*   **MainActor**：一个用于 UI 相关工作的全局 Actor，确保所有更新都在主线程上进行。
*   **Actors**：保护其自身的可变状态，一次只允许一段代码访问数据，以防止数据竞争。
*   **Nonisolated**：针对通用工具函数，选择退出隔离的代码。

**通过 Sendable 确保数据安全**
为了防止数据竞争，Swift 使用了 `Sendable` 协议。它确保只有线程安全的数据——如值类型（结构体）、不可变类或 Actor——才能跨越隔离边界。非 Sendable 类型（如可变类）会受到限制，以防止多个线程修改同一块内存。

**易于上手的并发模型 (Xcode 26)**
本文强调了 Xcode 26 中新的“易于上手并发（Approachable Concurrency）”设置（`SWIFT_DEFAULT_ACTOR_ISOLATION = MainActor`），该设置显著减少了编译器阻力。通过将代码默认隔离到 `MainActor` 并防止不必要的“线程跳转”，编译器在处理标准应用开发时的报错将不再那么激进。开发者只需针对 CPU 密集型任务使用 `@concurrent` 选择进入后台执行，这使得并发模型对普通开发者来说更加直观。

---

## 9. Go away Python

**原文标题**: Go away Python

**原文链接**: [https://lorentz.app/blog-item.html?id=go-shebang](https://lorentz.app/blog-item.html?id=go-shebang)

生成摘要时出错

---

## 10. Reverse Engineering a Mysterious UDP Stream in My Hotel (2016)

**原文标题**: Reverse Engineering a Mysterious UDP Stream in My Hotel (2016)

**原文链接**: [https://www.gkbrk.com/hotel-music](https://www.gkbrk.com/hotel-music)

生成摘要时出错

---

## 11. GOG is getting acquired by its original co-founder

**原文标题**: GOG is getting acquired by its original co-founder

**原文链接**: [https://www.gog.com/blog/gog-is-getting-acquired-by-its-original-co-founder-what-it-means-for-you/](https://www.gog.com/blog/gog-is-getting-acquired-by-its-original-co-founder-what-it-means-for-you/)

生成摘要时出错

---

## 12. Hive (YC S14) Is Hiring a Staff Software Engineer (Data Systems)

**原文标题**: Hive (YC S14) Is Hiring a Staff Software Engineer (Data Systems)

**原文链接**: [https://jobs.ashbyhq.com/hive.co/cb0dc490-0e32-4734-8d91-8b56a31ed497](https://jobs.ashbyhq.com/hive.co/cb0dc490-0e32-4734-8d91-8b56a31ed497)

生成摘要时出错

---

## 13. What Happened to Abit Motherboards

**原文标题**: What Happened to Abit Motherboards

**原文链接**: [https://dfarq.homeip.net/what-happened-to-abit-motherboards/](https://dfarq.homeip.net/what-happened-to-abit-motherboards/)

生成摘要时出错

---

## 14. Stranger Things creator says turn off "garbage" settings

**原文标题**: Stranger Things creator says turn off "garbage" settings

**原文链接**: [https://screenrant.com/stranger-things-creator-turn-off-settings-premiere/](https://screenrant.com/stranger-things-creator-turn-off-settings-premiere/)

生成摘要时出错

---

## 15. Show HN: One clean, developer-focused page for every Unicode symbol

**原文标题**: Show HN: One clean, developer-focused page for every Unicode symbol

**原文链接**: [https://fontgenerator.design/symbols](https://fontgenerator.design/symbols)

生成摘要时出错

---

## 16. No strcpy either

**原文标题**: No strcpy either

**原文链接**: [https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/](https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/)

生成摘要时出错

---

## 17. Times New American: A Tale of Two Fonts

**原文标题**: Times New American: A Tale of Two Fonts

**原文链接**: [https://hsu.cy/2025/12/times-new-american/](https://hsu.cy/2025/12/times-new-american/)

生成摘要时出错

---

## 18. Tesla's 4680 battery supply chain collapses as partner writes down deal by 99%

**原文标题**: Tesla's 4680 battery supply chain collapses as partner writes down deal by 99%

**原文链接**: [https://electrek.co/2025/12/29/tesla-4680-battery-supply-chain-collapses-partner-writes-down-dea/](https://electrek.co/2025/12/29/tesla-4680-battery-supply-chain-collapses-partner-writes-down-dea/)

生成摘要时出错

---

## 19. Charm Ruby – Glamorous Terminal Libraries for Ruby

**原文标题**: Charm Ruby – Glamorous Terminal Libraries for Ruby

**原文链接**: [https://charm-ruby.dev/](https://charm-ruby.dev/)

生成摘要时出错

---

## 20. Hacking Washing Machines [video]

**原文标题**: Hacking Washing Machines [video]

**原文链接**: [https://media.ccc.de/v/39c3-hacking-washing-machines](https://media.ccc.de/v/39c3-hacking-washing-machines)

生成摘要时出错

---

## 21. Concurrent Hash Table Designs

**原文标题**: Concurrent Hash Table Designs

**原文链接**: [https://bluuewhale.github.io/posts/concurrent-hashmap-designs/](https://bluuewhale.github.io/posts/concurrent-hashmap-designs/)

生成摘要时出错

---

## 22. Nicolas Guillou, French ICC judge sanctioned by the US and “debanked”

**原文标题**: Nicolas Guillou, French ICC judge sanctioned by the US and “debanked”

**原文链接**: [https://www.lemonde.fr/en/international/article/2025/11/19/nicolas-guillou-french-icc-judge-sanctioned-by-the-us-you-are-effectively-blacklisted-by-much-of-the-world-s-banking-system_6747628_4.html](https://www.lemonde.fr/en/international/article/2025/11/19/nicolas-guillou-french-icc-judge-sanctioned-by-the-us-you-are-effectively-blacklisted-by-much-of-the-world-s-banking-system_6747628_4.html)

生成摘要时出错

---

## 23. The future of software development is software developers

**原文标题**: The future of software development is software developers

**原文链接**: [https://codemanship.wordpress.com/2025/11/25/the-future-of-software-development-is-software-developers/](https://codemanship.wordpress.com/2025/11/25/the-future-of-software-development-is-software-developers/)

生成摘要时出错

---

## 24. ManusAI Joins Meta

**原文标题**: ManusAI Joins Meta

**原文链接**: [https://manus.im/blog/manus-joins-meta-for-next-era-of-innovation](https://manus.im/blog/manus-joins-meta-for-next-era-of-innovation)

生成摘要时出错

---

## 25. UNIX Fourth Edition

**原文标题**: UNIX Fourth Edition

**原文链接**: [http://squoze.net/UNIX/v4/README](http://squoze.net/UNIX/v4/README)

生成摘要时出错

---

## 26. AI is forcing us to write good code

**原文标题**: AI is forcing us to write good code

**原文链接**: [https://bits.logic.inc/p/ai-is-forcing-us-to-write-good-code](https://bits.logic.inc/p/ai-is-forcing-us-to-write-good-code)

生成摘要时出错

---

## 27. Graph Algorithms in Rayon

**原文标题**: Graph Algorithms in Rayon

**原文链接**: [https://davidlattimore.github.io/posts/2025/11/27/graph-algorithms-in-rayon.html](https://davidlattimore.github.io/posts/2025/11/27/graph-algorithms-in-rayon.html)

生成摘要时出错

---

## 28. Turning an old Amazon Kindle into a eInk development platform (2021)

**原文标题**: Turning an old Amazon Kindle into a eInk development platform (2021)

**原文链接**: [https://blog.lidskialf.net/2021/02/08/turning-an-old-kindle-into-a-eink-development-platform/](https://blog.lidskialf.net/2021/02/08/turning-an-old-kindle-into-a-eink-development-platform/)

生成摘要时出错

---

## 29. Singapore Study Links Heavy Infant Screen Time to Teen Anxiety

**原文标题**: Singapore Study Links Heavy Infant Screen Time to Teen Anxiety

**原文链接**: [https://www.bloomberg.com/news/articles/2025-12-30/singapore-study-links-heavy-infant-screen-time-to-teen-anxiety](https://www.bloomberg.com/news/articles/2025-12-30/singapore-study-links-heavy-infant-screen-time-to-teen-anxiety)

生成摘要时出错

---

## 30. Google is dead. Where do we go now?

**原文标题**: Google is dead. Where do we go now?

**原文链接**: [https://www.circusscientist.com/2025/12/29/google-is-dead-where-do-we-go-now/](https://www.circusscientist.com/2025/12/29/google-is-dead-where-do-we-go-now/)

生成摘要时出错

---

## 31. 'Commuting Is Bad'–Particularly for Women

**原文标题**: 'Commuting Is Bad'–Particularly for Women

**原文链接**: [https://www.theatlantic.com/family/2025/12/commute-gender-wage-gap-mothers/685265/](https://www.theatlantic.com/family/2025/12/commute-gender-wage-gap-mothers/685265/)

生成摘要时出错

---

## 32. MongoDB Server Security Update, December 2025

**原文标题**: MongoDB Server Security Update, December 2025

**原文链接**: [https://www.mongodb.com/company/blog/news/mongodb-server-security-update-december-2025](https://www.mongodb.com/company/blog/news/mongodb-server-security-update-december-2025)

生成摘要时出错

---

## 33. Outside, Dungeon, Town: Integrating the Three Places in Videogames (2024)

**原文标题**: Outside, Dungeon, Town: Integrating the Three Places in Videogames (2024)

**原文链接**: [https://keithburgun.net/outside-dungeon-town-integrating-the-three-places-in-videogames/](https://keithburgun.net/outside-dungeon-town-integrating-the-three-places-in-videogames/)

生成摘要时出错

---

## 34. 2025 Was Another Exceptionally Hot Year

**原文标题**: 2025 Was Another Exceptionally Hot Year

**原文链接**: [https://e360.yale.edu/digest/2025-second-hottest-year](https://e360.yale.edu/digest/2025-second-hottest-year)

生成摘要时出错

---

## 35. Incremental Backups of Gmail Takeouts

**原文标题**: Incremental Backups of Gmail Takeouts

**原文链接**: [https://baecher.dev/stdout/incremental-backups-of-gmail-takeouts/](https://baecher.dev/stdout/incremental-backups-of-gmail-takeouts/)

生成摘要时出错

---

## 36. Kidnapped by Deutsche Bahn

**原文标题**: Kidnapped by Deutsche Bahn

**原文链接**: [https://www.theocharis.dev/blog/kidnapped-by-deutsche-bahn/](https://www.theocharis.dev/blog/kidnapped-by-deutsche-bahn/)

生成摘要时出错

---

## 37. Linux DAW: Help Linux musicians to quickly and easily find the tools they need

**原文标题**: Linux DAW: Help Linux musicians to quickly and easily find the tools they need

**原文链接**: [https://linuxdaw.org/](https://linuxdaw.org/)

生成摘要时出错

---

## 38. Static Allocation with Zig

**原文标题**: Static Allocation with Zig

**原文链接**: [https://nickmonad.blog/2025/static-allocation-with-zig-kv/](https://nickmonad.blog/2025/static-allocation-with-zig-kv/)

生成摘要时出错

---

## 39. Show HN: Stop Claude Code from forgetting everything

**原文标题**: Show HN: Stop Claude Code from forgetting everything

**原文链接**: [https://github.com/mutable-state-inc/ensue-skill](https://github.com/mutable-state-inc/ensue-skill)

生成摘要时出错

---

## 40. What an unprocessed photo looks like

**原文标题**: What an unprocessed photo looks like

**原文链接**: [https://maurycyz.com/misc/raw_photo/](https://maurycyz.com/misc/raw_photo/)

生成摘要时出错

---

## 41. Parsing Advances

**原文标题**: Parsing Advances

**原文链接**: [https://matklad.github.io/2025/12/28/parsing-advances.html](https://matklad.github.io/2025/12/28/parsing-advances.html)

生成摘要时出错

---

## 42. When someone says they hate your product

**原文标题**: When someone says they hate your product

**原文链接**: [https://www.getflack.com/p/responding-to-negative-feedback](https://www.getflack.com/p/responding-to-negative-feedback)

生成摘要时出错

---

## 43. MH370 vanished in 2014.New search aims to find answers families desperately want

**原文标题**: MH370 vanished in 2014.New search aims to find answers families desperately want

**原文链接**: [https://www.abc.net.au/news/2025-12-30/mh370-search-resumes-for-malaysia-airlines-missing-plane/106186962](https://www.abc.net.au/news/2025-12-30/mh370-search-resumes-for-malaysia-airlines-missing-plane/106186962)

生成摘要时出错

---

## 44. I migrated to an almost all-EU stack and saved 500€ per year

**原文标题**: I migrated to an almost all-EU stack and saved 500€ per year

**原文链接**: [https://www.zeitgeistofbytes.com/p/bye-bye-big-tech-how-i-migrated-to](https://www.zeitgeistofbytes.com/p/bye-bye-big-tech-how-i-migrated-to)

生成摘要时出错

---

## 45. Flame Graphs vs Tree Maps vs Sunburst (2017)

**原文标题**: Flame Graphs vs Tree Maps vs Sunburst (2017)

**原文链接**: [https://www.brendangregg.com/blog/2017-02-06/flamegraphs-vs-treemaps-vs-sunburst.html](https://www.brendangregg.com/blog/2017-02-06/flamegraphs-vs-treemaps-vs-sunburst.html)

生成摘要时出错

---

## 46. Easily Dealing with Any-Dimensional Planes

**原文标题**: Easily Dealing with Any-Dimensional Planes

**原文链接**: [https://gpfault.net/posts/hyperplanes.html](https://gpfault.net/posts/hyperplanes.html)

生成摘要时出错

---

## 47. Quickemu: Quickly create and run optimised Windows, macOS and Linux VMs

**原文标题**: Quickemu: Quickly create and run optimised Windows, macOS and Linux VMs

**原文链接**: [https://github.com/quickemu-project/quickemu](https://github.com/quickemu-project/quickemu)

生成摘要时出错

---

## 48. Vitest Browser Mode Guide

**原文标题**: Vitest Browser Mode Guide

**原文链接**: [https://howtotestfrontend.com/resources/vitest-browser-mode-guide-and-setup-info](https://howtotestfrontend.com/resources/vitest-browser-mode-guide-and-setup-info)

生成摘要时出错

---

## 49. List of domains censored by German ISPs

**原文标题**: List of domains censored by German ISPs

**原文链接**: [https://cuiiliste.de/domains](https://cuiiliste.de/domains)

生成摘要时出错

---

## 50. Libgodc: Write Go Programs for Sega Dreamcast

**原文标题**: Libgodc: Write Go Programs for Sega Dreamcast

**原文链接**: [https://github.com/drpaneas/libgodc](https://github.com/drpaneas/libgodc)

生成摘要时出错

---

## 51. Stanford Lecture: Dr. Don Knuth – Adventures with Knight's Tours [video]

**原文标题**: Stanford Lecture: Dr. Don Knuth – Adventures with Knight's Tours [video]

**原文链接**: [https://www.youtube.com/watch?v=MKiRte-tnMY](https://www.youtube.com/watch?v=MKiRte-tnMY)

生成摘要时出错

---

## 52. A production bug that made me care about undefined behavior

**原文标题**: A production bug that made me care about undefined behavior

**原文链接**: [https://gaultier.github.io/blog/the_production_bug_that_made_me_care_about_undefined_behavior.html](https://gaultier.github.io/blog/the_production_bug_that_made_me_care_about_undefined_behavior.html)

生成摘要时出错

---

## 53. Show HN: A 45x45 Connections Puzzle To Commemorate 2025=45*45

**原文标题**: Show HN: A 45x45 Connections Puzzle To Commemorate 2025=45*45

**原文链接**: [https://thomaswc.com/2025.html](https://thomaswc.com/2025.html)

生成摘要时出错

---

## 54. The Signature Flicker

**原文标题**: The Signature Flicker

**原文链接**: [https://steipete.me/posts/2025/signature-flicker](https://steipete.me/posts/2025/signature-flicker)

生成摘要时出错

---

## 55. Groq investor sounds alarm on data centers

**原文标题**: Groq investor sounds alarm on data centers

**原文链接**: [https://www.axios.com/2025/12/29/groq-alex-davis-data-center-concerns](https://www.axios.com/2025/12/29/groq-alex-davis-data-center-concerns)

生成摘要时出错

---

## 56. Show HN: Superset – Terminal to run 10 parallel coding agents

**原文标题**: Show HN: Superset – Terminal to run 10 parallel coding agents

**原文链接**: [https://superset.sh/](https://superset.sh/)

生成摘要时出错

---

## 57. Harvard Youth Poll (51st Edition – Fall 2025)

**原文标题**: Harvard Youth Poll (51st Edition – Fall 2025)

**原文链接**: [https://iop.harvard.edu/youth-poll/51st-edition-fall-2025](https://iop.harvard.edu/youth-poll/51st-edition-fall-2025)

生成摘要时出错

---

## 58. All Delisted Steam Games

**原文标题**: All Delisted Steam Games

**原文链接**: [https://delistedgames.com/all-delisted-steam-games/](https://delistedgames.com/all-delisted-steam-games/)

生成摘要时出错

---

## 59. Geology of the Gulf of the Farallones National Marine Sanctuary

**原文标题**: Geology of the Gulf of the Farallones National Marine Sanctuary

**原文链接**: [https://pubs.usgs.gov/fs/farallones/](https://pubs.usgs.gov/fs/farallones/)

生成摘要时出错

---

## 60. Streaming compression beats framed compression

**原文标题**: Streaming compression beats framed compression

**原文链接**: [https://bou.ke/blog/compressed/](https://bou.ke/blog/compressed/)

生成摘要时出错

---

## 61. Huge Binaries

**原文标题**: Huge Binaries

**原文链接**: [https://fzakaria.com/2025/12/28/huge-binaries](https://fzakaria.com/2025/12/28/huge-binaries)

生成摘要时出错

---

## 62. Show HN: Aroma: Every TCP Proxy Is Detectable with RTT Fingerprinting

**原文标题**: Show HN: Aroma: Every TCP Proxy Is Detectable with RTT Fingerprinting

**原文链接**: [https://github.com/Sakura-sx/Aroma](https://github.com/Sakura-sx/Aroma)

生成摘要时出错

---

## 63. Win32 is the stable Linux ABI

**原文标题**: Win32 is the stable Linux ABI

**原文链接**: [https://loss32.org/](https://loss32.org/)

生成摘要时出错

---

## 64. Feynman's Hughes Lectures: 950 pages of notes

**原文标题**: Feynman's Hughes Lectures: 950 pages of notes

**原文链接**: [https://thehugheslectures.info/the-lectures/](https://thehugheslectures.info/the-lectures/)

生成摘要时出错

---

## 65. Karpathy on Programming: “I've never felt this much behind”

**原文标题**: Karpathy on Programming: “I've never felt this much behind”

**原文链接**: [https://twitter.com/karpathy/status/2004607146781278521](https://twitter.com/karpathy/status/2004607146781278521)

生成摘要时出错

---

## 66. Why is calling my asm function from Rust slower than calling it from C?

**原文标题**: Why is calling my asm function from Rust slower than calling it from C?

**原文链接**: [https://ohadravid.github.io/posts/2025-12-rav1d-faster-asm/](https://ohadravid.github.io/posts/2025-12-rav1d-faster-asm/)

生成摘要时出错

---

## 67. Show HN: See what readers who loved your favorite book/author also loved to read

**原文标题**: Show HN: See what readers who loved your favorite book/author also loved to read

**原文链接**: [https://shepherd.com/bboy/2025](https://shepherd.com/bboy/2025)

生成摘要时出错

---

## 68. 1Password extension is injecting Prism.js and breaking all <code> highlighting

**原文标题**: 1Password extension is injecting Prism.js and breaking all <code> highlighting

**原文链接**: [https://twitter.com/youyuxi/status/2005904473332564339](https://twitter.com/youyuxi/status/2005904473332564339)

生成摘要时出错

---

## 69. My First Meshtastic Network

**原文标题**: My First Meshtastic Network

**原文链接**: [https://rickcarlino.com/notes/electronics/my-first-meshtastic-network.html](https://rickcarlino.com/notes/electronics/my-first-meshtastic-network.html)

生成摘要时出错

---

## 70. Asking Gemini 3 to generate Brainfuck code results in an infinite loop

**原文标题**: Asking Gemini 3 to generate Brainfuck code results in an infinite loop

**原文链接**: [https://teodordyakov.github.io/brainfuck-agi/](https://teodordyakov.github.io/brainfuck-agi/)

生成摘要时出错

---

## 71. Developing a Beautiful and Performant Block Editor in Qt C++ and QML

**原文标题**: Developing a Beautiful and Performant Block Editor in Qt C++ and QML

**原文链接**: [https://rubymamistvalove.com/block-editor](https://rubymamistvalove.com/block-editor)

生成摘要时出错

---

## 72. Show HN: Euclidle – Guess the Coordinates in N‑Dimensional Space

**原文标题**: Show HN: Euclidle – Guess the Coordinates in N‑Dimensional Space

**原文链接**: [https://euclidle.com/](https://euclidle.com/)

生成摘要时出错

---

## 73. CIA Star Gate Project: An Overview (1993) [pdf]

**原文标题**: CIA Star Gate Project: An Overview (1993) [pdf]

**原文链接**: [https://www.cia.gov/readingroom/docs/CIA-RDP96-00789R002800180001-2.pdf](https://www.cia.gov/readingroom/docs/CIA-RDP96-00789R002800180001-2.pdf)

生成摘要时出错

---

## 74. You can make up HTML tags

**原文标题**: You can make up HTML tags

**原文链接**: [https://maurycyz.com/misc/make-up-tags/](https://maurycyz.com/misc/make-up-tags/)

生成摘要时出错

---

## 75. Intelligence – A Mystery Investigation Game

**原文标题**: Intelligence – A Mystery Investigation Game

**原文链接**: [https://intelligencegame.tech/](https://intelligencegame.tech/)

生成摘要时出错

---

## 76. Which Humans? (2023)

**原文标题**: Which Humans? (2023)

**原文链接**: [https://osf.io/preprints/psyarxiv/5b26t_v1](https://osf.io/preprints/psyarxiv/5b26t_v1)

生成摘要时出错

---

## 77. Rich Hickey: Thanks AI

**原文标题**: Rich Hickey: Thanks AI

**原文链接**: [https://gist.github.com/richhickey/ea94e3741ff0a4e3af55b9fe6287887f](https://gist.github.com/richhickey/ea94e3741ff0a4e3af55b9fe6287887f)

生成摘要时出错

---

## 78. Show HN: Z80-μLM, a 'Conversational AI' That Fits in 40KB

**原文标题**: Show HN: Z80-μLM, a 'Conversational AI' That Fits in 40KB

**原文链接**: [https://github.com/HarryR/z80ai](https://github.com/HarryR/z80ai)

生成摘要时出错

---

## 79. Show HN: Tetris Time

**原文标题**: Show HN: Tetris Time

**原文链接**: [https://tetris-time.koenvangilst.nl/?mode=countdown&to=2026-01-01T00:00:00.000Z&speed=3](https://tetris-time.koenvangilst.nl/?mode=countdown&to=2026-01-01T00:00:00.000Z&speed=3)

生成摘要时出错

---

## 80. Nvidia takes $5B stake in Intel under September agreement

**原文标题**: Nvidia takes $5B stake in Intel under September agreement

**原文链接**: [https://www.reuters.com/legal/transactional/nvidia-takes-5-billion-stake-intel-under-september-agreement-2025-12-29/](https://www.reuters.com/legal/transactional/nvidia-takes-5-billion-stake-intel-under-september-agreement-2025-12-29/)

生成摘要时出错

---

## 81. You can't design software you don't work on

**原文标题**: You can't design software you don't work on

**原文链接**: [https://www.seangoedecke.com/you-cant-design-software-you-dont-work-on/](https://www.seangoedecke.com/you-cant-design-software-you-dont-work-on/)

生成摘要时出错

---

## 82. Show HN: My not-for-profit search engine with no ads, no AI, & all DDG bangs

**原文标题**: Show HN: My not-for-profit search engine with no ads, no AI, & all DDG bangs

**原文链接**: [https://nilch.org](https://nilch.org)

生成摘要时出错

---

## 83. Benchmarking Self-Hosted S3-Compatible Storage

**原文标题**: Benchmarking Self-Hosted S3-Compatible Storage

**原文链接**: [https://www.repoflow.io/blog/benchmarking-self-hosted-s3-compatible-storage-a-practical-performance-comparison](https://www.repoflow.io/blog/benchmarking-self-hosted-s3-compatible-storage-a-practical-performance-comparison)

生成摘要时出错

---

## 84. Show HN: Lazy-image – Node.js image library with static binaries (Rust/NAPI)

**原文标题**: Show HN: Lazy-image – Node.js image library with static binaries (Rust/NAPI)

**原文链接**: [https://github.com/albert-einshutoin/lazy-image](https://github.com/albert-einshutoin/lazy-image)

生成摘要时出错

---

## 85. Obelisk 0.32: Cancellation, WebAPI, Postgres

**原文标题**: Obelisk 0.32: Cancellation, WebAPI, Postgres

**原文链接**: [https://obeli.sk/blog/announcing-obelisk-0-32/](https://obeli.sk/blog/announcing-obelisk-0-32/)

生成摘要时出错

---

## 86. Static Allocation for Compilers

**原文标题**: Static Allocation for Compilers

**原文链接**: [https://matklad.github.io/2025/12/23/static-allocation-compilers.html](https://matklad.github.io/2025/12/23/static-allocation-compilers.html)

生成摘要时出错

---

## 87. High-performance C++ hash table using grouped SIMD metadata scanning

**原文标题**: High-performance C++ hash table using grouped SIMD metadata scanning

**原文链接**: [https://github.com/Cranot/grouped-simd-hashtable](https://github.com/Cranot/grouped-simd-hashtable)

生成摘要时出错

---

## 88. Election betting on prediction markets apps is set to boom ahead of midterms

**原文标题**: Election betting on prediction markets apps is set to boom ahead of midterms

**原文链接**: [https://www.npr.org/2025/12/23/nx-s1-5647749/rise-of-prediction-markets](https://www.npr.org/2025/12/23/nx-s1-5647749/rise-of-prediction-markets)

生成摘要时出错

---

## 89. Still using Firefox – but not because of its vision

**原文标题**: Still using Firefox – but not because of its vision

**原文链接**: [https://blog.kulman.sk/stuck-with-firefox/](https://blog.kulman.sk/stuck-with-firefox/)

生成摘要时出错

---

## 90. Fast GPU Interconnect over Radio

**原文标题**: Fast GPU Interconnect over Radio

**原文链接**: [https://spectrum.ieee.org/rf-over-fiber](https://spectrum.ieee.org/rf-over-fiber)

生成摘要时出错

---

## 91. UK accounting body to halt remote exams amid AI cheating

**原文标题**: UK accounting body to halt remote exams amid AI cheating

**原文链接**: [https://www.theguardian.com/business/2025/dec/29/uk-accounting-remote-exams-ai-cheating-acca](https://www.theguardian.com/business/2025/dec/29/uk-accounting-remote-exams-ai-cheating-acca)

生成摘要时出错

---

## 92. My coworker's 36 key Corne open-source keyboard setup

**原文标题**: My coworker's 36 key Corne open-source keyboard setup

**原文链接**: [https://nuon.co/blog/nuon-keyboard-culture/](https://nuon.co/blog/nuon-keyboard-culture/)

生成摘要时出错

---

## 93. Swapping SIM cards used to be easy, and then came eSIM

**原文标题**: Swapping SIM cards used to be easy, and then came eSIM

**原文链接**: [https://arstechnica.com/gadgets/2025/12/i-switched-to-esim-in-2025-and-i-am-full-of-regret/](https://arstechnica.com/gadgets/2025/12/i-switched-to-esim-in-2025-and-i-am-full-of-regret/)

生成摘要时出错

---

## 94. IUseLinux: Access iMessage from your Linux (or windows) computer

**原文标题**: IUseLinux: Access iMessage from your Linux (or windows) computer

**原文链接**: [https://www.iuselinux.com/](https://www.iuselinux.com/)

生成摘要时出错

---

## 95. Calendar

**原文标题**: Calendar

**原文链接**: [https://neatnik.net/calendar/?year=2026](https://neatnik.net/calendar/?year=2026)

生成摘要时出错

---

## 96. 2025 Was Another Exceptionally Hot Year

**原文标题**: 2025 Was Another Exceptionally Hot Year

**原文链接**: [https://e360.yale.edu/digest/2025-second-hottest-year](https://e360.yale.edu/digest/2025-second-hottest-year)

生成摘要时出错

---

## 97. Why I think Valve’s retiring the Steam Deck LCD

**原文标题**: Why I think Valve’s retiring the Steam Deck LCD

**原文链接**: [https://gardinerbryant.com/why-valves-retiring-the-steam-deck-lcd/](https://gardinerbryant.com/why-valves-retiring-the-steam-deck-lcd/)

生成摘要时出错

---

## 98. Ruby Array Pack Bleed – Impacts Ruby 1.6.7 to 4.0.0

**原文标题**: Ruby Array Pack Bleed – Impacts Ruby 1.6.7 to 4.0.0

**原文链接**: [https://nastystereo.com/security/ruby-pack.html](https://nastystereo.com/security/ruby-pack.html)

生成摘要时出错

---

## 99. As AI gobbles up chips, prices for devices may rise

**原文标题**: As AI gobbles up chips, prices for devices may rise

**原文链接**: [https://www.npr.org/2025/12/28/nx-s1-5656190/ai-chips-memory-prices-ram](https://www.npr.org/2025/12/28/nx-s1-5656190/ai-chips-memory-prices-ram)

生成摘要时出错

---

## 100. Binance's Trust Wallet extension hacked; users lose $7M

**原文标题**: Binance's Trust Wallet extension hacked; users lose $7M

**原文链接**: [https://www.web3isgoinggreat.com/?id=trust-wallet-hack](https://www.web3isgoinggreat.com/?id=trust-wallet-hack)

生成摘要时出错

---

