# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-12-30.md)

*最后自动更新时间: 2025-12-30 17:49:25*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 2 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 3 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 4 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 5 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 6 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 7 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 8 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 9 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 10 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 11 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 12 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 13 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 14 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 15 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 16 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 17 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 18 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 19 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 20 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 21 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 22 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 23 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 24 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 25 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 26 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 27 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 28 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 29 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 30 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 31 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 32 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 33 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 34 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 35 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 36 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 37 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 38 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 39 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 40 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 41 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 42 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 43 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 44 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 45 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 46 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 47 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 48 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 49 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 50 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 51 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 52 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 53 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 54 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 55 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 56 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 57 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 58 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 59 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 60 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 61 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 62 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 63 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 64 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 65 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 66 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 67 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 68 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 69 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 70 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 71 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 72 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 73 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 74 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 75 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 76 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 77 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 78 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 79 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 80 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 81 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 82 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 83 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 84 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 85 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 86 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 87 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 88 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 89 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 90 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 91 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 92 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 93 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 94 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 95 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 96 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 97 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 98 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 99 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 100 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 101 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 102 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 103 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 104 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 105 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 106 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 107 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 108 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 109 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 110 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 111 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 112 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 113 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 114 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 115 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 116 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 117 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 118 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 119 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 120 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 121 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 122 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 123 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 124 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 125 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 126 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 127 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 128 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 129 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 130 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 131 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 132 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 133 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 134 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 135 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 136 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 137 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 138 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 139 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 140 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 141 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 142 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 143 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 144 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 145 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 146 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 147 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 148 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 149 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 150 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 151 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 152 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 153 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 154 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 155 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 156 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 157 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 158 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 159 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 160 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 161 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 162 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 163 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 164 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 165 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 166 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 167 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 168 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 169 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 170 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 171 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 172 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 173 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 174 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 175 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 176 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 177 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 178 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 179 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 180 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 181 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 182 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 183 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 184 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 185 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 186 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 187 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 188 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 189 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 190 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 191 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 192 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 193 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 194 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 195 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 196 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 197 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 198 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 199 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 200 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 201 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 202 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 203 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 204 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 205 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 206 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 207 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 208 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 209 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 210 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 211 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 212 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 213 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 214 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 215 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 216 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 217 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 218 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 219 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 220 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 221 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 222 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 223 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 224 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 225 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 226 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 227 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 228 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 229 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 230 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 231 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 232 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 233 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 234 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 235 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 236 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 237 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 238 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 239 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 240 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 241 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 242 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 243 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 244 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 245 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 246 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 247 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 248 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 249 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 250 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 251 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 252 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 253 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 254 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 255 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 256 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 257 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 258 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 259 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 260 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 261 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 262 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 263 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 264 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 265 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 266 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 267 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 268 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 269 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 270 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 271 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 272 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 273 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 274 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 275 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 276 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 277 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 278 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 279 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 280 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 281 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 282 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 283 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 284 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 285 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
