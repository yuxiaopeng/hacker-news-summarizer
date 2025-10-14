# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-10-14.md)

*最后自动更新时间: 2025-10-14 17:48:35*
## 1. 天文学家“拍摄”到遥远宇宙中的神秘黑暗物体

**原文标题**: Astronomers 'image' a mysterious dark object in the distant Universe

**原文链接**: [https://www.mpg.de/25518363/1007-asph-astronomers-image-a-mysterious-dark-object-in-the-distant-universe-155031-x](https://www.mpg.de/25518363/1007-asph-astronomers-image-a-mysterious-dark-object-in-the-distant-universe-155031-x)

天文学家利用引力透镜“拍摄”到遥远宇宙中的神秘暗物质。引力透镜是一种大质量物体的引力扭曲和偏转来自更远光源的光线的现象。这个距离地球约100亿光年的暗物质，质量是太阳的100万倍，是利用该技术发现的质量最小的暗物质。

一个国际团队利用包括绿岸望远镜在内的射电望远镜网络进行了这项发现，有效地创建了一个地球大小的“超级望远镜”。这使他们能够探测到背景星系的光线由于暗物质的引力而产生的细微扭曲。为了分析复杂的数据，该团队开发了需要超级计算机的新建模算法。

这项发现支持了“冷暗物质理论”，该理论认为暗物质是成团的，而不是均匀分布的。该发现为研究暗物质的性质和理解星系如何形成提供了一种新工具。该团队计划继续寻找更多此类低质量暗物质，这可能会排除一些现有的暗物质理论。

---

## 2. ADS-B 暴露

**原文标题**: ADS-B Exposed

**原文链接**: [https://adsb.exposed/](https://adsb.exposed/)

本文题为“ADS-B 曝光”，介绍了一个名为“ADS-B 大规模可视化器”的项目。顾名思义，该项目专注于可视化与ADS-B（广播式自动相关监视）技术相关的大量数据。 ADS-B是一种监视技术，飞机通过该技术广播其身份、位置和其他信息。

文章强调该可视化器是“自豪地使用 ClickHouse 开源数据库制作的”，表明 ClickHouse 在处理和处理潜在的巨型 ADS-B 数据方面的作用。包含来自维基百科的图片表明该文章将提供有关 ADS-B 的上下文或背景信息，可能依赖维基百科作为基础知识的来源。

本质上，这篇文章很可能是关于一个利用 ClickHouse 数据库可视化大量 ADS-B 数据集的项目。 这种可视化可能旨在提供对空中交通模式、飞机跟踪或其他航空相关信息的见解。

---

## 3. 为什么一切都如此可扩展？

**原文标题**: Why is everything so scalable?

**原文链接**: [https://www.stavros.io/posts/why-is-everything-so-scalable/](https://www.stavros.io/posts/why-is-everything-so-scalable/)

本文批评了初创公司过早采用复杂、可扩展的架构（如微服务和分布式系统）的趋势，他们常常模仿 FAANG 公司，即使有限的资源和客户群并不足以支撑由此带来的额外开销。作者认为，初创公司应该专注于创收和产品与市场的匹配，而不是立即着手解决可扩展性问题，因为这既昂贵又增加了不必要的复杂性。

核心论点是，对于早期公司来说，一个更简单的“单体”架构，分解为具有严格 API 协议和静态类型的良好定义的模块，通常更有效且易于维护。这种方法允许快速迭代、更轻松的调试和显着降低的基础设施成本。虽然它最终可能会限制单个组件的独立扩展，但作者认为，对于大多数初创公司来说，垂直扩展和向单体添加更多工作人员就足够了。

模块化单体方法的主要优势包括：

*   模块之间清晰的分离，防止代码库变得混乱。
*   整个代码库中的原子API更改，确保一致性。
*   调用点的丰富类型信息，消除歧义。
*   与网络调用相比，进程内通信速度明显更快。

作者承认独立组件扩展受限的缺点，但认为对于许多初创公司来说，收益大于成本，并敦促读者推迟采用复杂的分布式架构，直到绝对必要时。最后，作者强调，即使代码驻留在单个单元中，如果需要，模块仍然可以在单独的存储库中进行管理，从而在开发灵活性与原子部署的优势之间取得平衡。

---

## 4. 数组语言动物园

**原文标题**: Zoo of Array Languages

**原文链接**: [https://ktye.github.io/](https://ktye.github.io/)

本文档是一个“数组语言动物园”，主要关注数组编程语言K的实现和变体，源自APL。它重点介绍了不同的K实现（ktye/k、ngn/k、k7、k9等），以及对相关数组语言（如APL\360、BQN、KAP和APL的变体）的引用。

该文档提供了K语法和功能的快速参考。这包括基本算术运算（+、-、*、%）、运算符（如over(/)、scan(\)、eachleft、eachright）和一元函数（如floor(_)、ceiling、take(#)和drop(_)）。它展示了条件语句（`$[a;b;...]`）、循环结构（while[c;a;b;d;e;..]）和函数定义（f:{x+y}）。数据类型、数组操作和字典操作也进行了简要介绍。 还有一个关于“jtye/k：五十个函数中的k”的部分，它以简洁的方式分解了该语言的功能。turbo.k 图形进一步强调了一种对语言实现的底层方法。总的来说，这似乎是一个探索K和相关数组编程语言世界的笔记、链接和代码片段的集合。

---

## 5. 超声技术开启无创癌症治疗新纪元

**原文标题**: Ultrasound is ushering a new era of surgery-free cancer treatment

**原文链接**: [https://www.bbc.com/future/article/20251007-how-ultrasound-is-ushering-a-new-era-of-surgery-free-cancer-treatment](https://www.bbc.com/future/article/20251007-how-ultrasound-is-ushering-a-new-era-of-surgery-free-cancer-treatment)

超声技术：非侵入性癌症治疗的新希望

---

## 6. 自动K8s Pod放置匹配外部服务区域

**原文标题**: Automatic K8s pod placement to match external service zones

**原文链接**: [https://github.com/toredash/automatic-zone-placement](https://github.com/toredash/automatic-zone-placement)

本文提出了一种解决方案，通过使调度器了解网络拓扑，来优化Kubernetes Pod的放置，从而优化与外部资源通信的应用程序。问题：Kubernetes调度器不了解外部资源位置（例如，RDS实例），导致Pod随机放置以及潜在的跨可用区延迟问题。

该解决方案涉及一个查找服务和一个突变Webhook（使用Kyverno）。查找服务将外部资源域名解析为IP，并基于CIDR范围将其映射到可用区。突变Webhook拦截Pod创建请求，查询查找服务，并将节点亲和性规则注入到Pod规范中，从而确保将其放置在与外部资源相同的区域中。

其优点包括显著提高的性能（在pgbench测试中为175％-375％），这归功于降低的延迟以及通过最大程度地减少跨可用区数据传输而带来的潜在成本节省。该实施指南提供了收集区域信息，部署查找服务，应用Kyverno策略以及测试解决方案的步骤。

本文还讨论了常见问题，讨论了局限性（单A记录端点），并提出了未来的工作，包括支持多个A记录和GCP/Azure中的应用程序。它还承认该解决方案可以应用于本地环境。

---

## 7. Pyrefly: 用 Rust 编写的 Python 类型检查器和语言服务器

**原文标题**: Pyrefly: Python type checker and language server in Rust

**原文链接**: [https://pyrefly.org/?featured_on=talkpython](https://pyrefly.org/?featured_on=talkpython)

无法访问文章链接。

---

## 8. mmap()文件操作的逐步淘汰

**原文标题**: The phaseout of the mmap() file operation

**原文链接**: [https://lwn.net/Articles/1038715/](https://lwn.net/Articles/1038715/)

2025年9月25日LWN.net文章：Linux内核中`mmap()`文件操作的逐步淘汰
这篇文章讨论了Linux内核中`mmap()`文件操作的逐步淘汰，该过程始于内核6.17。`mmap()`允许用户空间将文件描述符的底层对象映射到其地址空间，但它对VMA（vm_area_struct）的直接访问导致了问题，从而可能导致意外的修改和潜在的错误。

替代方案是使用`vm_area_desc`结构的新`mmap_prepare()`回调。`mmap_prepare()`在映射过程的早期，VMA设置之前被调用，简化了发生故障时的清理工作。它向驱动程序提供有限的信息，并允许指定由内存管理层进行的VMA更改，从而限制了驱动程序的直接访问。

文章随后详细介绍了Lorenzo Stoakes正在进行的通过`mmap_action`结构扩展`mmap_prepare()`以适应更复杂用例的工作。该结构允许驱动程序在VMA设置后请求重映射操作（例如用于页帧号重映射的`MMAP_REMAP_PFN`），以及用于处理完成或错误的`success_hook`和`error_hook`回调。提到的一个特殊用例是复制某些当前驱动程序（如/dev/zero）执行的一些“独特”行为。这些更改是否会进入6.18合并窗口仍然不确定，但迁移数百个`mmap()`实现的总过程将需要相当长的时间。

---

## 9. 别往上看：地球静止轨道卫星上未加密的敏感内部链接 [pdf]

**原文标题**: Don’t Look Up: Sensitive internal links in the clear on GEO satellites [pdf]

**原文链接**: [https://satcom.sysnet.ucsd.edu/docs/dontlookup_ccs25_fullpaper.pdf](https://satcom.sysnet.ucsd.edu/docs/dontlookup_ccs25_fullpaper.pdf)

该文档似乎是对地球静止轨道(GEO)卫星上以明文形式暴露的敏感内部链接相关的安全漏洞的技术分析。它似乎描述了与暴露的内部链接相关的潜在风险。

该分析可能详细描述了如何发现这些链接以及这种暴露的潜在影响，可能包括未经授权访问卫星系统或敏感数据。包含 PDF 文件头和编码数据流 (FlateDecode) 表明其技术性质。

该文章包含技术数据（可能包括潜在的敏感信息）以及漏洞分析。

---

## 10. Wireshark 4.6.0 支持 macOS Pktap 元数据（PID、进程名等）

**原文标题**: Wireshark 4.6.0 Supports macOS Pktap Metadata (PID, Process Name, etc.)

**原文链接**: [https://nuxx.net/blog/2025/10/14/wireshark-4-6-0-supports-macos-pktap-metadata-pid-process-name-etc/](https://nuxx.net/blog/2025/10/14/wireshark-4-6-0-supports-macos-pktap-metadata-pid-process-name-etc/)

本文宣布发布 Wireshark 4.6.0 版本，该版本现已支持解析 macOS pktap 元数据，包括进程 ID (PID) 和进程名称。 这是基于之前一篇关于在 macOS 上使用进程 ID 捕获网络数据的文章构建的。

关键在于，由于 Wireshark 的原生支持，现在捕获带有进程信息的网络流量更加容易。 要使用此功能，文章指示用户使用带有 `tcpdump` 的 `pktap` 接口参数。 例如，`tcpdump -i pktap,en0 -w outfile.pcapng` 会捕获 `en0` 接口上的流量，而 `tcpdump -i pktap,all host 192.168.0.6 -w outfile.pcapng` 会捕获特定主机的所有流量。

捕获的数据以 Pcap-ng 格式保存。 文件在 Wireshark 中打开后，可以在“帧 → 进程信息”下找到进程信息。 文章还提供了使用 `frame.darwin.process_info` 的 Wireshark 过滤示例，例如 `frame.darwin.process_info.pname == "firefox"` 过滤来自 Firefox 进程的流量，或者 `frame.darwin.process_info.pid == 92046` 按 PID 过滤。 作者强调了此功能对于识别网络流量的来源（无论是预期的还是意外的）以及理解进程的网络活动非常有用。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 2 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 3 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 4 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 5 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 6 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 7 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 8 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 9 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 10 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 11 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 12 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 13 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 14 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 15 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 16 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 17 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 18 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 19 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 20 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 21 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 22 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 23 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 24 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 25 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 26 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 27 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 28 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 29 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 30 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 31 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 32 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 33 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 34 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 35 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 36 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 37 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 38 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 39 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 40 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 41 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 42 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 43 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 44 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 45 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 46 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 47 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 48 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 49 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 50 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 51 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 52 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 53 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 54 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 55 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 56 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 57 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 58 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 59 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 60 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 61 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 62 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 63 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 64 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 65 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 66 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 67 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 68 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 69 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 70 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 71 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 72 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 73 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 74 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 75 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 76 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 77 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 78 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 79 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 80 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 81 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 82 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 83 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 84 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 85 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 86 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 87 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 88 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 89 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 90 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 91 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 92 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 93 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 94 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 95 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 96 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 97 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 98 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 99 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 100 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 101 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 102 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 103 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 104 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 105 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 106 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 107 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 108 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 109 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 110 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 111 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 112 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 113 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 114 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 115 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 116 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 117 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 118 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 119 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 120 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 121 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 122 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 123 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 124 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 125 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 126 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 127 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 128 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 129 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 130 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 131 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 132 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 133 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 134 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 135 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 136 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 137 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 138 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 139 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 140 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 141 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 142 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 143 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 144 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 145 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 146 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 147 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 148 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 149 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 150 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 151 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 152 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 153 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 154 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 155 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 156 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 157 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 158 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 159 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 160 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 161 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 162 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 163 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 164 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 165 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 166 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 167 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 168 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 169 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 170 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 171 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 172 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 173 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 174 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 175 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 176 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 177 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 178 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 179 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 180 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 181 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 182 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 183 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 184 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 185 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 186 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 187 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 188 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 189 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 190 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 191 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 192 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 193 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 194 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 195 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 196 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 197 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 198 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 199 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 200 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 201 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 202 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 203 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 204 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 205 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 206 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 207 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 208 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 209 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
