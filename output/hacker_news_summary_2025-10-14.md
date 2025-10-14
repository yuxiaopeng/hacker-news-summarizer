# Hacker News 热门文章摘要 (2025-10-14)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 暂缓使用 Litestream 0.5.0

**原文标题**: Hold Off on Litestream 0.5.0

**原文链接**: [https://mtlynch.io/notes/hold-off-on-litestream-0.5.0/](https://mtlynch.io/notes/hold-off-on-litestream-0.5.0/)

本文探讨了作者迁移到Litestream 0.5.0的经验，Litestream是一款用于将SQLite数据库备份到云存储的工具。虽然作者赞扬了Litestream及其重新开发，但由于在迁移过程中遇到几个错误，他们建议在生产环境中部署0.5.0版本之前要谨慎。

迁移过程包括更新备份格式和配置文件（将“replicas”数组替换为单个“replica”）。作者最初由于端点URI错误而面临将数据上传到Backblaze的问题，该问题很快被Litestream开发者修复。

部署Litestream 0.5.0后出现了更多问题，包括缺少命令标志（-if-replica-exists）以及恢复期间出现“transaction not available”错误。最后，作者遇到了Litestream无法创建必要目录的错误，需要对Litestream源代码进行自定义修复。

尽管通过自定义构建成功使Litestream 0.5.x正常工作，但由于剩余错误的严重性以及尚未在生产版本中修复的最新问题，作者建议等待更稳定的版本。作者强调这并非批评，而是一个避免潜在数据丢失或服务中断的实际警告。文章最后宣传了作者关于为开发者写作的书籍。

---

## 12. 荷兰政府接管中资芯片制造商安世半导体

**原文标题**: Dutch government takes control of Chinese-owned chipmaker Nexperia

**原文链接**: [https://www.cnbc.com/2025/10/13/dutch-government-takes-control-of-chinese-owned-chipmaker-nexperia.html](https://www.cnbc.com/2025/10/13/dutch-government-takes-control-of-chinese-owned-chipmaker-nexperia.html)

荷兰政府已接管总部位于荷兰的中资半导体制造商安世半导体(Nexperia)，理由是担心国家和欧洲经济安全。政府援引《商品供应法》，旨在防止欧洲关键芯片供应可能中断，特别是对汽车行业。此次干预是在观察到安世半导体内部存在“严重的治理缺陷和行为”，威胁到关键技术知识的连续性之后采取的。

安世半导体是中国闻泰科技的子公司，专门从事大批量芯片生产。荷兰政府宣布这一消息后，闻泰科技的股价暴跌。政府已暂停安世半导体资产、业务或人员变更最多一年，闻泰科技董事长已被解除其在安世半导体中的职务。

闻泰科技批评此举是出于地缘政治偏见的过度干预，并声称自2019年收购安世半导体以来，一直遵守当地法律法规。安世半导体表示，其遵守所有现行法律法规。荷兰政府的决定正值美中贸易战日益紧张以及中国最近对稀土元素出口实施限制之际，这可能会影响欧洲的汽车行业。此举进一步加剧了中国与荷兰之间的贸易关系，由于荷兰对阿斯麦(ASML)向中国出口半导体设备的限制，中荷贸易关系已经受到了考验。

---

## 13. 颠覆Telegram的端到端加密（2023）

**原文标题**: Subverting Telegram's end-to-end encryption (2023)

**原文链接**: [https://tosc.iacr.org/index.php/ToSC/article/view/10302](https://tosc.iacr.org/index.php/ToSC/article/view/10302)

Cogliati, Ethan, 和 Jha 的论文《颠覆 Telegram 的端到端加密》分析了 Telegram 端到端加密 (E2EE) 协议的安全性，特别是针对潜在的大规模监控。作者证明，尽管官方客户端因其开源性和可复现构建的设计而具有抵抗性，但 Telegram 的 E2EE 容易受到算法替换攻击的影响。

核心漏洞在于底层的认证加密方案 MTProto2.0。作者提出了一种高效的算法替换攻击，该攻击利用 MTProto2.0 在选择随机填充长度和值方面的灵活性。这种攻击允许以相对较少的查询和低延迟，高概率地恢复重要的加密密钥材料，从而可能实现国家支持的对私人通信的监控，无论是通过有针对性的攻击还是通过受损的第三方客户端。

作者建议 Telegram 修改 MTProto2.0 的填充方法以缓解此漏洞。他们提出了对填充描述进行微小更改，这将使其在大多数实际情况下具有抗颠覆性。作为一个有益的副作用，他们将 MTProto2.0 的操作模式推广为 MTProto-G，并证明了其作为多用户安全确定性认证加密方案的安全性。总而言之，该论文指出了 Telegram 的 E2EE 中的一个重大弱点，提出了一种实用的攻击，并提出了一个易于实施的解决方案。

---

## 14. 能够编辑线粒体DNA的类CRISPR工具

**原文标题**: CRISPR-like tools that finally can edit mitochondria DNA

**原文链接**: [https://www.nature.com/articles/d41586-025-03307-x](https://www.nature.com/articles/d41586-025-03307-x)

本文探讨了近期编辑线粒体DNA（mtDNA）的进展，这在以前由于该细胞器的双层膜结构，使用CRISPR-Cas9技术是无法实现的。 线粒体疾病由mtDNA突变引起，影响大约五千分之一的人，并且由于mtDNA的难以接近性而难以治疗。

早期编辑mtDNA的尝试包括使用锌指核酸酶（ZFNs）和转录激活因子样效应子核酸酶（TALENs）切割突变的mtDNA，导致细胞消除它并复制健康的副本。 然而，对于所有mtDNA副本都发生突变的疾病，此方法无效。

DddA的发现是一项突破，DddA是一种将胞嘧啶（C）转化为胸腺嘧啶（T）的细菌酶。 David Liu及其同事修改了DddA，将其分成两个非活性部分，并使用TALENs将其引导至特定的mtDNA序列。 这允许进行靶向碱基编辑，而无需依赖引导RNA，从而克服了阻碍基于CRISPR方法的线粒体膜屏障。 这种新工具有望创建准确的线粒体疾病动物模型，并可能在未来治疗或治愈这些疾病。

---

## 15. Show HN: Metorial (YC F25) – MCP 的 Vercel

**原文标题**: Show HN: Metorial (YC F25) – Vercel for MCP

**原文链接**: [https://github.com/metorial/metorial](https://github.com/metorial/metorial)

Metorial (YC F25) 被定位为“MCP 的 Vercel”，是一个集成平台，旨在简化使用模型上下文协议 (MCP) 将 AI 模型连接到庞大的 API、数据源和工具生态系统的过程。 它为使用 JavaScript/TypeScript 和 Python SDK 的开发人员提供了一个简化的统一界面，抽象化了 MCP 实现的复杂性。

该平台旨在解决 AI 应用程序与外部系统轻松集成的问题。 Metorial 拥有诸如用于简化集成的一行代码 SDK、包含超过 5000 个 MCP 服务器的大型服务器目录、用于在仪表板中进行测试的嵌入式 MCP 浏览器以及强大的监控和调试工具（用于跟踪 MCP 会话和识别错误）等功能。

驱动 Metorial 的技术栈包括 MCP、Docker、TypeScript、Bun、Go、PostgreSQL、Redis、MongoDB 和 React。 它强调以开发者为中心的功能，例如可定制性、开源可用性、多实例支持、广泛的文档、完整的 API 访问权限以及用于管理集成的先进仪表板。 核心目标是赋能开发者构建能够可靠、简单和安全地与各种系统交互的 Agentic AI 应用程序。 Metorial 根据 FSL-1.1 许可协议获得许可。

---

## 16. Kyber (YC W23) 招聘企业级客户经理

**原文标题**: Kyber (YC W23) Is Hiring an Enterprise AE

**原文链接**: [https://www.ycombinator.com/companies/kyber/jobs/BQRRSrZ-enterprise-account-executive-ae](https://www.ycombinator.com/companies/kyber/jobs/BQRRSrZ-enterprise-account-executive-ae)

Kyber招聘驻纽约企业客户主管

Kyber是一家由Y Combinator支持的初创公司，正在构建一个由人工智能驱动的企业文档平台。现招聘一名驻纽约的企业客户主管（AE）。Kyber的解决方案专注于改变监管文档工作流程，为客户带来显著的时间和成本节约，尤其是在保险行业。他们已经实现了快速的收入增长，获得了多年的合同，并与Guidewire等公司建立了战略合作伙伴关系。

该企业客户主管将负责完整的销售周期，从寻找和筛选潜在客户到合同执行。这包括与利益相关者建立关系，执行外联策略，参加行业活动，以及利用人工智能工具。他们还将参与销售运营，提供反馈以完善信息传递并塑造新的销售模式。

Kyber正在寻找具有强烈职业道德、经验证的销售记录、出色的沟通技巧、足智多谋和团队合作精神的人。公司重视客户至上、以工作为荣、超越期望以及营造积极的工作环境。

福利包括有竞争力的薪资、股票期权和全面的健康保险。为了脱颖而出，鼓励申请人让推荐人将对其简历或LinkedIn个人资料的简短认可直接发送至Arvind [at] askkyber.com。该职位提供了帮助塑造人工智能驱动的企业文档领域中具有行业定义意义的公司的机会。

---

## 17. 帕利塞兹大火嫌疑人ChatGPT历史记录将被用作证据

**原文标题**: Palisades Fire suspect's ChatGPT history to be used as evidence

**原文链接**: [https://www.rollingstone.com/culture/culture-news/chatgpt-palisades-fire-suspect-1235443216/](https://www.rollingstone.com/culture/culture-news/chatgpt-palisades-fire-suspect-1235443216/)

佛罗里达州29岁的乔纳森·林德克内希特因涉嫌与2025年1月洛杉矶县发生的造成12人死亡、摧毁数千座建筑的毁灭性帕利塞德斯大火有关，已被逮捕并被联邦政府指控犯有“纵火破坏财产罪”。

针对林德克内希特的关键“数字证据”是他使用ChatGPT的历史记录，据称他在火灾发生几个月前曾提示AI生成燃烧的森林和人们逃离森林的图像。虽然尚不清楚这是否是此类证据首次在刑事案件中使用，但这引发了关于AI用户数据隐私以及OpenAI等科技公司与执法部门之间合作的问题。OpenAI的政策声明，他们需要法律依据才能披露用户数据。

检方还引用了林德克内希特的手机证据、涉嫌虚假陈述以及他参与早期的拉赫曼火灾（该火灾一直闷烧到帕利塞德斯火灾）作为支持他们案件的证据。他被指控恶意引发拉赫曼火灾，报告了火灾，然后拍摄了紧急响应。检察官可能会使用ChatGPT图像来证明预谋纵火的意图，尽管尚未说明动机。林德克内希特在拉赫曼火灾当晚作为Uber司机的行为也正在受到审查。使用ChatGPT日志作为证据是一个新的法律前沿，有可能提供对一个人精神状态和关注点的洞察。

---

## 18. 特斯拉或因电池大范围故障而失去韩国补贴。

**原文标题**: Tesla is at risk of losing subsidies in Korea over widespread battery failures

**原文链接**: [https://electrek.co/2025/10/14/tesla-is-at-risk-of-lossing-subsidies-in-korea-over-widespread-battery-failures/](https://electrek.co/2025/10/14/tesla-is-at-risk-of-lossing-subsidies-in-korea-over-widespread-battery-failures/)

特斯拉在韩国面临潜在危机：近4500辆汽车电池故障，或失补贴

---

## 19. KDE庆祝成立29周年并启动年度筹款活动

**原文标题**: KDE celebrates the 29th birthday and kicks off the yearly fundraiser

**原文链接**: [https://kde.org/fundraisers/yearend2025/](https://kde.org/fundraisers/yearend2025/)

KDE庆祝成立29周年并启动年度筹款活动，目标是筹集5万欧元。这些资金将支持KDE自由软件的开发和维护，这些软件在各个领域越来越受欢迎。KDE强调其致力于通过注重隐私的软件和财务独立，让用户掌控自己的数字生活。

此次筹款活动还强调了KDE对环境可持续性的承诺，提及国际电子废物日及其旨在对抗计划报废并推广使用旧的、功能正常的设备的“End of 10”活动。KDE批评微软停止对Windows 10的支持，迫使用户更换完全正常的计算机，从而加剧了电子垃圾的产生。

此外，KDE旨在支持那些缺乏最新硬件或可靠互联网的用户，提供满足他们需求的软件。最后，KDE寻求协助公共机构采用自由软件，确保政府保持对其系统和公民数据的控制。捐赠者可以下载数字徽章和可打印贺卡等礼品，以感谢他们的贡献。

---

## 20. 美国迎来人工智能淘金热，而非工厂繁荣

**原文标题**: America is getting an AI gold rush instead of a factory boom

**原文链接**: [https://www.washingtonpost.com/business/2025/10/13/manufacturing-artificial-intelligence/](https://www.washingtonpost.com/business/2025/10/13/manufacturing-artificial-intelligence/)

无法访问文章链接。

---

## 21. GPT-5o-mini捏造医学生住院医师申请成绩

**原文标题**: GPT-5o-mini hallucinates medical residency applicant grades

**原文链接**: [https://www.thalamusgme.com/blogs/cortex-core-clerkship-grades-and-transcript-normalization](https://www.thalamusgme.com/blogs/cortex-core-clerkship-grades-and-transcript-normalization)

Thalamus 2025年10月6日发布的文章，旨在解决社区对Cortex核心住院医师轮转成绩单标准化功能（用于住院医师招聘）的反馈。Thalamus承认Cortex内显示的自动提取的轮转成绩存在不准确的报告，但强调官方成绩单和申请文件仍然准确且未被篡改。

Cortex使用OCR和NLP技术解析医学院成绩单中的轮转成绩，并生成用于比较的参考报告。Thalamus强调该工具仅用于提供比较背景信息，不应用于单独筛选或自动拒绝申请者。强烈建议审核者对照官方成绩单核实提取的成绩。

主要关注的问题是因不准确而可能对申请者造成的不利影响。Thalamus保证项目主任也会审查官方文件（成绩单、MSPE），并在调查案例中发现并纠正任何差异。

文章为项目提供了将成绩单标准化用作参考并对照官方文件核实成绩的指南。建议申请人其官方记录是正确的，并建议不要就成绩单事宜联系项目。鼓励医学院分享此指南，并与Thalamus合作完善针对独特评分系统的映射。

Thalamus承诺根据反馈不断改进Cortex，强调该工具旨在提供额外的背景信息，而不是取代官方文件或全面审查。他们欢迎与申请人、项目和医学院合作，以改善招聘体验。

---

## 22. “蜂群”揭示地球磁场日益增长的薄弱点

**原文标题**: Swarm reveals growing weak spot in Earth's magnetic field

**原文链接**: [https://phys.org/news/2025-10-swarm-reveals-weak-earth-magnetic.html](https://phys.org/news/2025-10-swarm-reveals-weak-earth-magnetic.html)

欧洲航天局“雨燕”卫星群揭示南大西洋异常区自2014年以来显著扩大。受影响区域已扩大至近半个欧洲大陆的面积。这种减弱对穿越该区域的卫星尤为令人担忧，因为它们面临更高的辐射，可能导致故障。

“雨燕”任务已收集磁场测量数据11年，结果表明异常区正在以不同的速度减弱，非洲西南部的区域自2020年以来经历了更快的衰减。这与地球核心和地幔边界的“反向磁通斑块”有关，那里的磁力线正在进入地核而不是离开。

此外，“雨燕”数据表明，虽然南大西洋的磁场正在减弱，但西伯利亚的磁场正在增强。加拿大强磁场区域已经缩小，而西伯利亚区域已经扩大，影响了导航。

“雨燕”的长期数据收集对于理解地球磁场的动态特性至关重要，并为导航、空间天气监测以及理解从地核到大气层的地球系统提供了宝贵的信息。该任务预计将持续提供数据到2030年以后。

---

## 23. DDoS僵尸网络Aisuru以创纪录DDoS覆盖美国ISP

**原文标题**: DDoS Botnet Aisuru Blankets US ISPs in Record DDoS

**原文链接**: [https://krebsonsecurity.com/2025/10/ddos-botnet-aisuru-blankets-us-isps-in-record-ddos/](https://krebsonsecurity.com/2025/10/ddos-botnet-aisuru-blankets-us-isps-in-record-ddos/)

Aisuru僵尸网络，现为全球规模最大、破坏性最强的僵尸网络，正在发起破纪录的DDoS攻击，其大部分火力源自美国互联网服务提供商（ISP）如AT&T、Comcast和Verizon上被入侵的物联网设备。 近期攻击已达到近30太比特每秒，造成广泛的网络中断，特别是针对在线游戏社区及其ISP。

该僵尸网络基于2016年泄露的Mirai代码构建，利用消费级路由器、安全摄像头和其他固件过时的物联网设备中的漏洞。Aisuru的运营者积极扫描易受攻击的设备，并将其奴役以进行DDoS攻击。

Global Secure Layer (GSL) 的 Steven Ferguson 等安全专家观察到 Aisuru 的构成发生了变化，美国 ISP 为攻击流量贡献了很大一部分。来自受感染设备的这种出站DDoS流量正在导致同一网络上的其他客户的服务降级。

Aisuru僵尸网络还被怀疑被出租作为分布式代理网络，允许网络犯罪分子匿名化恶意流量。Aisuru 的一位所有者正在使用与 Mirai 之前的目标相关的 Telegram 账号，表明长期参与 DDoS 出租行业。

该僵尸网络的迅速蔓延归因于利用物联网设备中的零日漏洞以及吸收来自已拆除的 Rapper Bot 僵尸网络的孤立设备。尽管“Forky”是 DDoS 出租领域的知名人物，但据称参与 Aisuru 的个人之一仍然否认参与攻击。

---

## 24. 复制粘贴补丁：一个复制粘贴补丁教程

**原文标题**: Copy-and-Patch: A Copy-and-Patch Tutorial

**原文链接**: [https://transactional.blog/copy-and-patch/tutorial](https://transactional.blog/copy-and-patch/tutorial)

本文是一篇关于“复制与修补”编译的教程，这是一种快速且可维护的创建基线 JIT（即时编译器）的方法。其核心思想是编写被称为“模板”的小型 C 函数，这些函数旨在编译成可连接的本机代码片段。在运行时，这些预编译的片段会被首尾相接地复制，并根据需要使用特定的常量或地址进行修补（修改）。

本教程通过创建一个用于简单函数 `int add_a_b(int a, int b)` 的 JIT 编译器来演示该过程，该编译器在运行时专门用于计算 `1 + 2`。它将该过程分解为以下几个步骤：

1. **模板：** 使用“孔”（占位符）在 C 中实现基本操作（加载、加法、返回），这些占位符用于稍后进行修补的值。
2. **编译与检查：** 将模板编译为本机代码，并使用 `objdump` 检查汇编代码以识别重定位偏移量。
3. **模板生成库：** 创建 C 函数，将编译后的模板复制到内存缓冲区中，并使用运行时特定的值来修补“孔”。
4. **JIT 引擎：** 实现 JIT 编译器，该编译器以正确的顺序连接模板、修补占位符并执行生成的函数。

本教程包括每个步骤的示例代码，包括 `stencils.c`、`cnp_stencils.c` 和 `cnp_jit.c`。它还展示了如何使用 `mmap` 和 `mprotect` 在运行时分配可执行内存。最后，它提供了一个头文件 (`cnp_stencils.h`)，其中包含简化重定位孔声明的宏，从而允许更复杂的模板。

---

## 25. Show HN: SQLite Online – 独立开发11年，日活用户1.1万

**原文标题**: Show HN: SQLite Online – 11 years of solo development, 11K daily users

**原文链接**: [https://sqliteonline.com/](https://sqliteonline.com/)

SQLite Online 是一个由一位开发者历时11年开发的在线SQLite工具，目前每日服务11000名用户。它允许用户导入、导出、运行SQL查询，以及查看表语法和历史记录。一个关键特性是使用专门的QLINE、QAREA、QBAR、QPIE和QBUBBLE SELECT语句生成数据科学图表，并支持轴和颜色自定义。

开发历史突出了持续的改进，包括添加DuckDB和PGLite集成、虚拟表支持（联邦查询）、改进的图表解析、AI帮助、实时错误高亮显示、XLSX导出、OpFS支持、新设计、云数据库保存，以及迁移到sqlite.org/wasm。性能增强包括无4MB查询限制、regexp函数支持和大整数支持。

该工具在设置中提供各种自定义选项，包括SQLite存储（内存、OpFS、IndexDB）、左侧菜单排序和搜索、编辑器首选项和颜色皮肤。它还包括一个SQL Online AiDE组件。该平台使用各种开源库，如Sql.js、DuckDB、PGLite、MariaDB、PostgreSQL、MS SQL Server Express、Font-Awesome、CodeMirror、Toastify和Chart.js。该服务不承担上传内容的责任，并遵守开源许可。

---

## 26. 基于“光学热力学”的首个设备无需开关即可路由光线

**原文标题**: First device based on 'optical thermodynamics' can route light without switches

**原文链接**: [https://phys.org/news/2025-10-device-based-optical-thermodynamics-route.html](https://phys.org/news/2025-10-device-based-optical-thermodynamics-route.html)

南加州大学研究人员开发出首个基于“光学热力学”的无开关光路设备。 这种新方法利用热力学原理引导光通过非线性光学系统，无需传统光路路由器中复杂的开关阵列和电子控制。 该设备使光能够自然地找到正确的输出通道，模拟膨胀和平衡等热力学过程。

这项技术对高性能计算、电信和安全信息处理具有重要意义，因为它提供了一种更快、更高效的信息传输方式。 这种技术可以加速芯片设计师（如英伟达）以及其他探索传统电子产品替代方案的公司开发光互连技术。

这项关键创新在于重构了非线性多模光学系统的混沌特性。 通过认识到这些系统中的光达到了一种热平衡状态，研究人员开发了一种“光学热力学”理论。 这使得设备设计成为可能，在这种设备中，光可以自行组织并流入指定的输出通道，而无需外部引导。 这一发展为新型光子器件和光管理策略打开了大门。

---

## 27. 智能手机与当下

**原文标题**: Smartphones and being present

**原文链接**: [https://herman.bearblog.dev/being-present/](https://herman.bearblog.dev/being-present/)

本文探讨了作者有意识地减少智能手机使用，并最大化日常生活存在感的方法。他强调了一个令人震惊的统计数据，即人们每天花费大量时间在手机上，这使他们远离了有意义的体验，并分散了他们的注意力。他感叹智能手机具有成瘾性，在其实用功能之外，还设计了无数的“注意力陷阱”。

作者强调了过有意义的生活的重要性，这种生活充满了现实世界的体验、人际关系和个人成长，而不是陷入短视频和在线争论的循环中。他详细介绍了自己减少数字消费的策略，包括关闭通知和放弃社交媒体。他用“一袋饼干”的比喻来说明智能手机如何诱惑用户分心。

他认为，由于科技公司的说服力和潜在的成瘾性，应用程序上的时间限制是无效的，更有效的策略是让手机尽可能地变得无趣。他分享了具体技巧，例如关闭YouTube观看历史记录以消除算法驱动的推荐，并使用广告拦截器来阻止像YouTube Shorts这样分散注意力的元素。

他强调，通过阻止不需要的信息，最终消除了检查手机的奖励，从而减少了使用频率，并更加注重体验。作者总结说，他的方法使他成为一个更加专注、不易分心、更加乐观的人，并有更多时间进行充实的活动。他鼓励读者尝试类似的策略，以重新获得注意力，并专注于当下。

---

## 28. 索尼 PlayStation 2 维修热潮

**原文标题**: Sony PlayStation 2 fixing frenzy

**原文链接**: [https://retrohax.net/sony-playstation-2-fixing-frenzy/](https://retrohax.net/sony-playstation-2-fixing-frenzy/)

无法访问文章链接。

---

## 29. 展示一下：CSS 扩展

**原文标题**: Show HN: CSS Extras

**原文链接**: [https://github.com/sindresorhus/css-extras](https://github.com/sindresorhus/css-extras)

CSS 扩展功能：一套 CSS 自定义函数，旨在增强样式功能，无需构建步骤。它利用了新的原生 CSS `@function` 规则，为各种用途提供现成的函数。该库分为数学与数字、颜色、排版、布局、间距、动画、网格、滤镜、主题和实用工具等类别，总共约 50 个函数。

**主要特点：**

*   **全面的功能：** 提供从基本数学运算到高级颜色处理和响应式布局的各种功能。
*   **无需构建步骤：** 可以直接导入并在 CSS 文件中使用，或在 HTML 中链接。
*   **主题支持：** 包含用于创建可适应明暗模式的、具有主题意识的组件的函数。
*   **提供示例：** 通过示例代码演示响应式卡片、布局和具有主题意识的元素的使用。

**用法：**

该库可以通过 npm 安装或直接在 HTML 中链接。用户可以在其 CSS 中使用诸如 `--negate()`、`--opacity()`、`--fluid-type()` 等函数。

**浏览器支持：**

目前在 Chrome 141+ 中支持，因为 `@function` 规则仍在标准化过程中。

**许可：**

根据 MIT 或 CC0-1.0 许可提供。

---

## 30. 现代iOS安全特性——SPTM、TXM和安全飞地的深度解析

**原文标题**: Modern iOS Security Features – A Deep Dive into SPTM, TXM, and Exclaves

**原文链接**: [https://arxiv.org/abs/2510.09272](https://arxiv.org/abs/2510.09272)

Steffin和Classen的arXiv论文《现代iOS安全特性——SPTM、TXM和Exclaves深度解析》分析了苹果公司通过内核分层来增强iOS安全性的努力。该论文强调了从单内核XNU向更像微内核设计的转变。

核心论点围绕着SPTM（可能是安全页表管理）的引入，它作为负责内存重塑的关键组件。作者展示了SPTM如何创建隔离的信任域，有效地分离功能并减轻内核漏洞的影响。通过SPTM的关键功能之一是TXM（信任执行监视器），它负责代码签名和授权验证。

该论文随后深入研究了Exclaves的架构和通信机制，这是建立在此基础上的最新安全特性。它确定了多种通信途径，包括`xnuproxy`（安全世界请求处理程序）和Tightbeam IPC框架。

作者得出结论，这些架构变化通过将关键和敏感组件移出XNU内核的直接控制范围，显著提高了系统安全性。这确保了即使在发生内核漏洞时，也能保持最高级别的信任和安全性。该论文代表了对这些相对未公开的iOS安全特性的首次科学而全面的分析。

---

## 31. 美国的未来可能取决于人工智能是否略微令人失望。

**原文标题**: America's future could hinge on whether AI slightly disappoints

**原文链接**: [https://www.noahpinion.blog/p/americas-future-could-hinge-on-whether](https://www.noahpinion.blog/p/americas-future-could-hinge-on-whether)

诺亚·史密斯在2025年10月12日发表的一篇文章中指出，特朗普总统的关税政策下，美国经济出人意料的韧性可能归功于人工智能的繁荣。 尽管制造业步履维艰，消费者信心疲软，但GDP增长仍然出人意料地保持积极态势，一些分析师认为其中很大一部分归因于与人工智能相关的支出。

然而，史密斯警告说，人工智能领域可能是一个泡沫。虽然特朗普在很大程度上避免对人工智能征收关税，但该行业的崩溃可能会引发经济衰退，从而破坏特朗普的经济遗产。史密斯认为，危险并非人工智能彻底失败，而仅仅是“略微让”那些对人工智能抱有极高期望的投资者和分析师失望。他称之为“产业泡沫”——对该技术的真正价值的误判。

文章指出，人们担心组织在人工智能投资上回报甚微，员工使用人工智能生成低质量的“工作废料”，规模化努力的回报递减，以及难以匹配围绕新人工智能模型的大肆炒作。文章还提到了由于大规模数据中心建设而导致国家电网紧张的风险。史密斯总结说，即使人工智能有用，略低于预期的表现也可能引发崩盘，并极大地改变美国的经济和政治格局。

---

## 32. 容器为何出现？

**原文标题**: Why did containers happen?

**原文链接**: [https://buttondown.com/justincormack/archive/ignore-previous-directions-8-devopsdays/](https://buttondown.com/justincormack/archive/ignore-previous-directions-8-devopsdays/)

为何容器会应运而生？

这篇博文探讨了容器兴起背后的原因及其对软件开发领域的影响。作者回顾了与联邦贸易委员会（FTC）关于容器和虚拟机之间竞争格局的讨论。

作者认为，虚拟机解决了管理和整合未充分利用的物理服务器的问题，从而节省了硬件和许可费用。另一方面，容器的出现是为了解决管理由越来越多的开发人员编写的越来越多的应用程序的问题。Docker 最初是为了管理 PaaS 公司的应用程序部署而创建的，它强调的是打包而不是隔离。

对于企业而言，容器促进了向云的迁移并推动了现代化，通常促使从 Windows 转向 Linux。Docker 易于采用，加上 Docker Hub 作为可共享镜像的中央存储库，被证明至关重要。容器强制执行的不可变性，需要重建和重新部署，简化了部署并增强了安全性。

作者还讨论了 Kubernetes 最初专注于调度，后来演变为部署工具。此外，删除容器的便利性也影响了向云提供商管理数据库的转变。

这篇文章批评了对部署的关注以及 Kubernetes 的复杂性如何导致 DevOps 成为围绕部署技术的专门角色。虽然从开源组件构建应用程序变得占主导地位，但通用的构建抽象未能实现。尽管具有不可变性，但依赖项的规模限制了其效用。

作者总结说，虽然容器在某些领域提高了效率，但仍然存在大量的资源浪费。他认为，采用包括容器在内的“乏味”技术正变得越来越普遍，这可能是由于人工智能占据了“变革预算”以及零利率政策（ZIRP）时代的结束。作者认为，未来的创新将需要对变革进行新的投资。

---

## 33. NanoChat – 100美元能买到的最佳ChatGPT

**原文标题**: NanoChat – The best ChatGPT that $100 can buy

**原文链接**: [https://github.com/karpathy/nanochat](https://github.com/karpathy/nanochat)

NanoChat：一个全栈、极简实现的类ChatGPT LLM，旨在单节点上运行，成本低至100美元。该仓库提供代码库，涵盖分词、预训练、微调、评估、推理和Web服务，使用户能够训练并与其自己的LLM交互。

"speedrun.sh"脚本有助于在8XH100节点上约4小时内训练和推理一个基本的NanoChat模型。 用户随后可以通过Web UI与模型交互，并使用生成的"report.md"文件评估其性能。

文章还提及以更高成本（例如，300美元和1000美元）训练更大、更强大的模型的可能性，同时承认LLM通常需要大量的资本支出。 它提供了修改"speedrun.sh"脚本以训练GPT-2级别模型的简要说明。

作者强调NanoChat的易用性，旨在提供一个易于理解、修改和派生的代码库，而不是一个详尽的可配置框架。 它包括使用“files-to-prompt”和DeepWiki等实用程序查询代码库本身的说明。 最后，文章感谢其他项目、个人和组织的贡献，并提供了用于研究用途的引用格式。

---

## 34. JIT：你想在现代CPU上比解释器更快？

**原文标题**: JIT: So you want to be faster than an interpreter on modern CPUs

**原文链接**: [https://www.pinaraf.info/2025/10/jit-so-you-want-to-be-faster-than-an-interpreter-on-modern-cpus/](https://www.pinaraf.info/2025/10/jit-so-you-want-to-be-faster-than-an-interpreter-on-modern-cpus/)

这篇博文深入探讨了在现代 CPU 上针对精心编写的解释器优化代码执行速度的复杂性，尤其关注 PostgreSQL。作者解释了乱序执行和超标量 CPU 架构如何最大限度地减少传统解释器瓶颈的影响，例如操作码分派中的分支预测错误。

作者强调了现代 CPU 在优化解释型代码方面的惊人效率，并强调解释器中的简单 switch 语句通常会被分支预测和其他硬件优化所缓解。然后，他们研究了在 PostgreSQL 中优化一个简单的 SQL 查询 ("SELECT a FROM table WHERE a = 42")，分析了解释执行中空值检查和函数调用 (int4eq) 的成本。

性能测试表明，删除冗余的空值检查和内联 int4eq 调用可以带来显著的性能提升。具体来说，内联 int4eq 显示出更显著的影响。作者指出，虽然这些优化也适用于 JIT 编译器，但它们很容易在解释器本身中实现，从而可能抵消 JIT 编译器的优势。

这篇博文最后暗示了未来对解释器中更大瓶颈的讨论，表明仍然存在 JIT 编译可以提供显著收益的领域。作者还呼吁提供支持，理由是用于该项目的时间和资源有限。

---

## 35. 疾控中心受政府停摆解雇重创，部分解雇被撤回

**原文标题**: CDC battered by government shutdown firings, while some are rescinded

**原文链接**: [https://www.statnews.com/2025/10/11/cdc-firings-government-shutdown-hhs/](https://www.statnews.com/2025/10/11/cdc-firings-government-shutdown-hhs/)

本文简述了2025年10月政府停摆对疾控中心（CDC）造成的混乱和不稳定。主要问题是疾控中心“因政府停摆裁员而遭受重创”，表明停摆导致了人员缩减。一个重要细节是，这些削减波及到疾控中心的旗舰出版物《发病率和死亡率周报》(MMWR)，导致“大幅削减”。然而，文章也指出，针对《发病率和死亡率周报》的这些具体削减“在数小时后被撤销”，表明这是一个仓促的决定以及随后的重新考虑或干预。总体印象是，疾控中心内部一片混乱和不确定，其关键职能容易受到政府停摆的影响，并可能受到快速且考虑不周的变更的影响。《发病率和死亡率周报》削减的撤销意味着该出版物对疾控中心核心任务的重要性以及这些突然行动可能造成的损害。

---

## 36. 大型语言模型在字符级别文本处理方面越来越出色。

**原文标题**: LLMs are getting better at character-level text manipulation

**原文链接**: [https://blog.burkert.me/posts/llm_evolution_character_manipulation/](https://blog.burkert.me/posts/llm_evolution_character_manipulation/)

本文探讨了近期大型语言模型(LLMs)在处理字符级文本操作方面能力的提升，这曾经是一个由于基于token的编码而导致的弱点。作者测试了像GPT-5和Claude 4.5这样的模型在字符替换、计数和解密密码等任务上的表现。

文章强调了一代人的进步。较旧的模型在简单的任务（例如在句子中将“r”替换为“l”，反之亦然）上表现不佳，而较新的模型（GPT 4.1及更高版本，Claude Sonnet 4）成功地执行了这一任务，而无需推理。 同样，字符计数是LLM的一个已知弱点，但GPT-5模型和启用推理的Claude Sonnet可以准确地执行此操作。

作者随后检查了Base64和ROT20密码的处理情况。 LLM的任务是解码Base64编码的ROT20加密消息。结果表明，更新、更大的模型在Base64编码/解码方面表现出更好的泛化能力，即使对于“乱码”输入也是如此，这表明它们对算法的理解超出了记忆。像GPT-5 Mini/Standard（无论是否进行推理）、Gemini 2.5 Pro/Flash和Qwen 235B这样的模型在此任务中表现出强大的性能。

文章总结说，尽管LLM采用基于token的架构，但它们在处理字符级文本操作方面变得越来越熟练。虽然字符级操作尚未完全解决，但已经取得了显著进展。推理和工具的使用增强了这些能力，但核心改进源于基础模型本身的进步。

---

## 37. Nexperia – 公司发展最新动态

**原文标题**: Nexperia – Update on Company Developments

**原文链接**: [https://www.nexperia.com/about/news-events/press-releases/update-on-company-developments](https://www.nexperia.com/about/news-events/press-releases/update-on-company-developments)

以下是恩智浦公司更新的简要总结：

由于近期涉及前首席执行官张学政及其母公司闻泰科技的事件，恩智浦正面临重大的治理和运营挑战。荷兰企业商会已暂停张学政的职务，原因是对其稳健管理存在疑虑，并将闻泰科技的投票权置于独立管理人的管理之下。Stefan Tilger将担任临时首席执行官。

荷兰政府已根据《商品供应法》发布紧急命令，禁止恩智浦在一年内未经政府批准迁移业务、解雇高管或做出其他关键决策。 该命令旨在保护对荷兰和欧洲工业至关重要的半导体产品的供应。

此外，由于闻泰科技在实体清单上，恩智浦受到美国对美国实体清单上的公司拥有的实体实施的出口管制限制的影响。 虽然已经为确保业务连续性做出了准备，并且存在宽限期，但恩智浦正在寻求解决方案。

此外，中国商务部发布出口管制通知，禁止恩智浦中国出口特定零部件。恩智浦正积极与中国当局沟通，以获得豁免并减轻影响。

尽管面临这些挑战，恩智浦强调其对业务连续性的承诺，并正积极与相关部门合作以解决问题。 公司仍然是全球领先的半导体公司，在欧洲、亚洲和美国开展业务，专注于创新、效率和可持续发展。

---

## 38. Strudel REPL – 一个基于浏览器的音乐实时编码环境

**原文标题**: Strudel REPL – a music live coding environment living in the browser

**原文链接**: [https://strudel.cc](https://strudel.cc)

本文简要介绍了Strudel REPL，一个直接在网页浏览器中运行的音乐实时编码环境。它强调用户可以使用代码实时创作和操控音乐，并且该工具可通过网页浏览器访问，无需安装软件。文章还提及了在Mastodon社交网络上关于Strudel REPL的存在或公告，暗示可以在那里找到社区或更多信息。总而言之，本文展示了Strudel REPL作为一个方便且易于访问的平台，可直接在网页浏览器中进行音乐实时编码。

---

## 39. 线程优先——一种聊天体验模型

**原文标题**: Thread First – A model for chat experiences

**原文链接**: [https://progressdb.dev/docs/blog-thread-first](https://progressdb.dev/docs/blog-thread-first)

无法访问文章链接。

---

## 40. NVIDIA DGX Spark 深度评测：本地AI推理的新标杆

**原文标题**: NVIDIA DGX Spark In-Depth Review: A New Standard for Local AI Inference

**原文链接**: [https://lmsys.org/blog/2025-10-13-nvidia-dgx-spark/](https://lmsys.org/blog/2025-10-13-nvidia-dgx-spark/)

NVIDIA DGX Spark：紧凑型一体化桌面工作站，专为本地AI推理设计，将超级计算级的性能带到开发者的桌面。本文将重点介绍其特性、性能和用例。

DGX Spark拥有时尚耐用的设计，并配备强大的NVIDIA GB10 Grace Blackwell Superchip，具有20个CPU核心和高达1 PFLOP的稀疏FP4张量性能，在AI能力上介于RTX 5070和5070 Ti之间。一个关键特性是其128 GB的相干统一内存，在CPU和GPU之间共享，无需典型的传输开销即可加载大型模型。双QSFP端口允许集群两个单元以运行更大的模型。

使用SGLang和Ollama的性能基准测试表明，DGX Spark擅长高效运行较小的模型，尤其是在使用批处理时。虽然在原始算力上无法与全尺寸GPU竞争，但它的优势在于处理受益于统一内存的工作负载，例如原型设计、模型实验和边缘AI研究。使用EAGLE3的推测解码显示出显着的加速潜力。系统在满载下保持稳定的温度和噪音水平。

DGX Spark非常适合模型原型设计、轻量级设备端推理以及对内存相干架构的研究。它预装了Docker，可以通过SGLang轻松地进行模型服务，并且可以与Zed和Ollama等工具一起用于编码辅助。

总而言之，DGX Spark是一个精心设计、易于使用的平台，它优先考虑效率和多功能性，使其成为寻求强大的本地开发环境的AI开发者和研究人员的宝贵工具。

---

## 41. JSON River – 增量式解析JSON流

**原文标题**: JSON River – Parse JSON incrementally as it streams in

**原文链接**: [https://github.com/rictic/jsonriver](https://github.com/rictic/jsonriver)

`jsonriver` 是一个 JavaScript 库，可以增量解析流入的 JSON 数据，例如来自网络请求或语言模型的数据流。与标准的 `JSON.parse` 不同，它会在数据到达时提供一系列越来越完整的 JSON 值。 这使得应用程序可以在接收到整个 JSON 之前处理部分数据。

`jsonriver` 的主要特性包括：

*   **增量解析:** 提供一个越来越完整的 JSON 对象流。
*   **标准兼容:** 保证最终解析的值与 `JSON.parse` 的结果完全相同。
*   **错误处理:** 对于无效的输入，匹配 `JSON.parse` 的行为，对不可解析或过早关闭的流抛出错误。
*   **不变性:** 保持数据类型的一致性以及数组和对象的可预测修改模式。
*   **轻量级:** 体积小，无依赖，并使用标准的 JavaScript 功能。
*   **对比:** 虽然比内置的 `JSON.parse` 慢，但它适用于需要流式传输的场景。 它也被认为是更全面的库（如 `stream-json`）的更简单替代方案，在某些用例中提供速度优势。

本文还为开发者提供了安装和测试说明。

---

## 42. 为什么要学习编程语言 (2022)

**原文标题**: Why study programming languages (2022)

**原文链接**: [https://people.csail.mit.edu/rachit/post/why-study-programming-languages/](https://people.csail.mit.edu/rachit/post/why-study-programming-languages/)

本文探讨了我们为何要设计新的编程语言以及构成编程语言的基本问题。文章认为，尽管现有语言可以完成任何可编程的任务，但新语言的创建是为了开启新的思路和探索形式。像抽象、性能和可用性等常见理由被认为过于主观，无法预测语言的成功。

作者提出，语言不仅仅是表达现有概念的工具，更是探索未知计算领域的工具。他们强调了语言通过特征借用实现的融合，但强调掌握语言能解锁独特的能力，正如 C 和 Haskell 这两个对比鲜明的例子所展示的那样。

文章随后深入探讨了编程语言的定义，否定了仅凭语法和语义作为全面定义。虽然语义是至关重要的组成部分，但生态系统（库、社区、并发模型等）对语言的特性具有重要贡献。作者最终的定义认为，编程语言由语法、语义和一个支持探索的生态系统组成。优先考虑的语义和生态系统的具体要素由它们提供的探索工具决定。

因此，编程语言的研究涵盖了从语法和语义到运行时系统和 IDE 等各个方面。作者鼓励学生设计非传统的语言，并强调语言设计的最终目标是探索和创造尚未存在的事物。

---

## 43. 技术乐观主义与适度恐惧

**原文标题**: Technological Optimism and Appropriate Fear

**原文链接**: [https://importai.substack.com/p/import-ai-431-technological-optimism](https://importai.substack.com/p/import-ai-431-technological-optimism)

无法访问文章链接。

---

## 44. 软件更新周末导致部分Jeep 4xe混动车变砖

**原文标题**: Software update bricks some Jeep 4xe hybrids over the weekend

**原文链接**: [https://arstechnica.com/cars/2025/10/software-update-bricks-some-jeep-4xe-hybrids-over-the-weekend/](https://arstechnica.com/cars/2025/10/software-update-bricks-some-jeep-4xe-hybrids-over-the-weekend/)

吉普牧马人4xe混动车型Uconnect信息娱乐系统软件更新导致车辆失去动力并抛锚。这个周末推送的有缺陷的无线更新不会立即损坏汽车，但会导致行驶过程中动力系统故障，有时甚至是在高速公路上。

受影响的车主已经在论坛、Reddit和YouTube上报告了他们的经历。吉普已经撤回了更新，并建议尚未安装的车主忽略弹出通知。已经更新的车主被告知避免使用混合动力和电动模式。修复程序在第二天发布。

该事件凸显了未经充分测试的软件更新的潜在风险，尤其是那些在一周后期推送的更新。Ars Technica已联系Stellantis寻求置评。

---

## 45. 美国太阳能农场

**原文标题**: American solar farms

**原文链接**: [https://tech.marksblogg.com/american-solar-farms.html](https://tech.marksblogg.com/american-solar-farms.html)

本文详细介绍了美国地面安装太阳能（GM-SEUS）数据集的创建和探索，该数据集全面汇集了美国本土48州和哥伦比亚特区的公用事业和商业级太阳能发电场。 GM-SEUS由NOAA、NASA和USGS的研究人员创建，包含两个数据集：阵列和面板，概述了太阳能发电场的物理结构。

作者描述了他们用于分析的强大工作站，包括CPU、RAM、SSD和操作系统设置。 然后，他们概述了安装必要软件（如GDAL和DuckDB）以及用于空间和数据操作的DuckDB扩展的过程。

文章随后重点介绍了准备用于分析的GM-SEUS数据。 这包括下载数据集，提取投影信息，以及使用DuckDB清理数据，创建几何字段，计算边界框，并将数据转换为ZStandard压缩、空间排序的Parquet文件以提高效率。

文章提供了来自阵列数据集的示例记录，并详细介绍了列名、数据类型和统计信息（如NULL百分比、唯一值和最小值/最大值）。 它还介绍了对太阳能阵列数据的一些分析，包括资产位置的热图、按安装年份划分的数据来源细分、安装类型和模块类型之间的关系以及按来源划分的阵列容量计数。 还提供了有关面板数据的相同信息。

---

## 46. 没有科学，就没有初创企业：我们正在关闭的创新引擎

**原文标题**: No science, no startups: The innovation engine we're switching off

**原文链接**: [https://steveblank.com/2025/10/13/no-science-no-startups-the-unseen-engine-were-switching-off/](https://steveblank.com/2025/10/13/no-science-no-startups-the-unseen-engine-were-switching-off/)

在博文中，史蒂夫·布兰克 lament 美国的科学资助下降及其对创新和国家实力的潜在影响。他阐明了科学家、工程师、企业家和风险资本家在创新生态系统中的角色。科学家们受好奇心驱动，进行基础和应用研究，理论家构建模型，实验者验证假设。这项研究主要由政府资助，并在大学（R1、R2和R3）进行，推动了突破性进展。

工程师们在科学发现的基础上，创造有形的产品和系统。然后，企业家将这些创新商业化，迭代开发产品以实现市场契合。风险资本家为企业家提供资金，但他们回避与基础研究相关的长期风险，将其留给政府和大学。

布兰克强调，美国历来表现出色，是因为其对大学研究的投资，这推动了像硅谷这样的产业发展，并提升了国防能力。这在一定程度上得益于外国出生的研究人员的贡献，他们在美国进行了大约40-50%的基础研究。他认为，削减科学经费会削弱长期经济和国家安全，使美国依赖于重视科学的国家。他批评了用人工智能取代科学家的想法，并建议应该用人工智能来提高他们的生产力。

---

## 47. 纽约时报、美联社、Newsmax等表示拒绝签署五角大楼新规

**原文标题**: New York Times, AP, Newsmax and others say they won't sign new Pentagon rules

**原文链接**: [https://apnews.com/article/pentagon-press-access-defense-department-rules-95878bce05096912887701eaa6d019c6](https://apnews.com/article/pentagon-press-access-defense-department-rules-95878bce05096912887701eaa6d019c6)

包括《纽约时报》、《美联社》、《Newsmax》、《华盛顿邮报》、《大西洋月刊》和路透社在内的多家主要新闻机构拒绝签署一份新的国防部文件，该文件概述了新的新闻规则。这些媒体认为，该政策侵犯了第一修正案的权利，并可能因常规的新闻采访而惩罚他们。

新规定将限制记者在没有陪同的情况下进入五角大楼区域，并允许国防部长皮特·赫格塞斯撤销记者因向国防部人员索取未经批准的信息（无论是否保密）而获得的采访许可。

新闻机构认为，签署该文件意味着报道未经批准的信息会损害国家安全，他们对此予以否认。他们坚称，他们已经佩戴胸牌、避开机密区域，并且不会报道危及美国人的信息。

国防部长赫格塞斯和五角大楼发言人肖恩·帕内尔为该政策辩护，声称它建立了“常识性的媒体程序”，并且仅仅要求记者承认理解该政策。帕内尔指责记者们“在网上哭诉”。赫格塞斯转发了一个问题，暗示记者们认为他们应该拥有不受限制地进入五角大楼的权限。

五角大楼记者协会声称该政策含糊不清，可能违宪，而且没有必要。《纽约时报》强调，鉴于军方获得大量纳税人资金，公众有权了解其运作方式。文章还指出，特朗普总统过去曾向新闻机构施压。

---

## 48. 随着麻省理工学院更新的SEAL技术，自提升语言模型正成为现实。

**原文标题**: Self-improving LMs are becoming reality with MIT's updated SEAL technique

**原文链接**: [https://venturebeat.com/ai/self-improving-language-models-are-becoming-reality-with-mits-updated-seal](https://venturebeat.com/ai/self-improving-language-models-are-becoming-reality-with-mits-updated-seal)

自提升语言模型（LMs）正受到越来越多的关注，麻省理工学院更新的SEAL（自对齐语言代理）技术便是其中之一。《VentureBeat》的文章讨论了SEAL如何通过反馈循环迭代地提高自身性能，这与训练后保持静态的传统LMs不同。

SEAL背后的核心思想是允许LM评估其自身对问题的回答，并找出需要改进的地方。然后，它利用这种自我评估来改进其知识和推理能力。更新后的SEAL技术侧重于不仅生成答案，还要生成这些答案的解释。通过明确地证明其推理的合理性，LM可以更清晰地展示其思维过程，从而更容易发现缺陷并从中学习。

SEAL的改进包括生成多样化且相关的提示来挑战LM，使其能够遇到更多不同的场景并从错误中学习。该系统还采用了一些技术来避免陷入局部最优解，这意味着它可以摆脱次优解决方案并继续改进。

这种自我提升能力有可能显著提高LMs的性能和可靠性，减少对持续人工干预和再训练的需求。文章表明，这种方法可能会产生更强大、更适应性强的AI系统，能够随着时间的推移不断学习和改进。虽然这项研究仍处于早期阶段，但像SEAL这样的自提升LMs的进步代表着朝着更自主和更有能力的AI迈出了重要一步。

---

## 49. Passt – 简单套接字传输插件

**原文标题**: Passt – Plug a Simple Socket Transport

**原文链接**: [https://passt.top/passt/about/](https://passt.top/passt/about/)

Passt是一款轻量级的翻译层，位于二层网络接口和容器及虚拟机原生四层套接字之间。它旨在提供一种比Slirp等方案更简单、更高效的替代方案，通过最小化TCP/IP协议栈的遍历并避免使用NAT。Passt提供了一个薄适配层，反射发送窗口和确认，无需大量缓冲，这在缺少CAP_NET_RAW权限时至关重要。

Pasta，与Passt共享同一二进制文件，将此功能扩展到网络命名空间，使用tap接口转发流量，无需提升权限。它为本地连接引入了快速旁路，直接在命名空间之间转发四层套接字的数据，从而提高了性能。

主要功能包括IPv4/IPv6支持（不包括分片）、具有窗口缩放和序列号攻击防御的TCP、UDP、ICMP/ICMPv6回显，以及最小化的DHCP/NDP代理服务器。安全方面，通过沙盒、静态代码分析和不使用动态内存分配来优先考虑。性能方面，通过合并、批处理和pasta中本地连接的零拷贝路径来增强，与现有解决方案相比，可能提供显著的吞吐量改进。Passt与Qemu、libvirt和Podman集成，而pasta作为slirp4netns的替代品并支持无根Docker。针对各种Linux发行版提供软件包和静态构建，并支持多种架构。

---

## 50. Vali，一个用于Varlink的C语言库

**原文标题**: Vali, a C library for Varlink

**原文链接**: [https://emersion.fr/blog/2025/announcing-vali/](https://emersion.fr/blog/2025/announcing-vali/)

本文介绍了一个新的C语言库`vali`，它用于Varlink RPC协议，旨在简化进程间通信。Varlink使用Unix套接字上的JSON消息，供客户端调用服务公开的方法。

作者强调了从接口定义文件生成代码的好处，`vali`支持这一功能，并将其与手动JSON解析进行了对比。如果没有代码生成，与Varlink交互需要大量的样板代码。`vali`基于Varlink接口定义生成类型安全的C结构体和函数，从而简化了客户端和服务端的实现。

在客户端，`vali`为每个方法生成输入和输出结构体，从而增强了代码的清晰度和向后兼容性。服务端代码生成处理异步调用，并使用按调用结构体和处理程序结构体提供类型安全。

本文还解释了`vali`背后的设计选择，例如将回调函数和用户数据捆绑在一个结构体中，这受到了Go的`net/http.Handler`的启发，从而简化了处理程序的管理并促进了中间件的创建。

`vali`库还包括一个服务注册表，允许在单个服务中管理多个接口，包括标准内省接口。

作者承认仍存在一些挑战，例如在生成的结构体中处理`const`正确性，并概述了未来的计划，包括在客户端添加异步支持。文章最后鼓励用户尝试`vali`并报告任何问题。

---

## 51. 使用 ClickHouse、Kafka 和 Vector 扩展请求日志记录

**原文标题**: Scaling request logging with ClickHouse, Kafka, and Vector

**原文链接**: [https://www.geocod.io/code-and-coordinates/2025-10-02-from-millions-to-billions/](https://www.geocod.io/code-and-coordinates/2025-10-02-from-millions-to-billions/)

TJ·米勒讲述Geocodio如何将其请求日志系统从每月数百万扩展到数十亿的过程。 最初，他们使用带有TokuDB存储引擎的MariaDB，并按月对表进行分区以便于管理。 这种设置运行良好多年，但由于TokuDB的弃用、大规模性能下降以及潜在的缓存击穿风险，问题开始出现。

他们首次尝试解决这个问题的方法是简单地用ClickHouse替换MariaDB，ClickHouse是一个以分析而闻名的列式数据库。 然而，该系统被大量的小型、行级插入所淹没，导致“TOO_MANY_PARTS”错误。 第二次尝试使用ClickHouse缓冲表只会使问题更加严重，导致“TOO_MANY_LINKS”错误和服务器无响应。

最终，他们采用了Honeybadger团队推荐的架构，整合了Kafka和Vector。 Kafka作为一个持久的、高吞吐量的事件流平台，用于解耦生产者和消费者，处理巨大的规模。 Vector是一个高性能的可观察性数据管道，有效地从Kafka消费消息，将其批量处理成最佳大小（每次30,000-50,000条记录），并将其插入到ClickHouse中。 这种解决方案提供了可扩展性、容错能力以及有效处理不断增长的请求数据量的能力。 该团队目前并行运行MariaDB和ClickHouse系统以进行审计。

---

## 52. 调试湿度：在现实世界部署软件的经验教训

**原文标题**: Debugging Humidity: Lessons from deploying software in the physical world

**原文链接**: [https://physical-ai.ghost.io/debugging-humidity-lessons-from-deploying-code-to-a-factory-floor/](https://physical-ai.ghost.io/debugging-humidity-lessons-from-deploying-code-to-a-factory-floor/)

文章《湿度调试：在物理世界部署软件的经验教训》讲述了作者在工厂环境中部署代码的经验，以及云计算的理想化世界与物理世界的严酷现实之间的鲜明对比。作者强调，在云计算工程中做出的假设，例如可靠的网络和稳定的电力，在处理物理机械和环境时都会崩溃。

文章突出了关键差异：资源是有限且恶劣的，而不是无限且可靠的；幂等性适用于物理，而不仅仅是 API；“离线优先”是一种生存必需品，而不仅仅是一种用户体验模式；时间同步是不可靠的。作者用机械臂控制和传送带操作等例子来说明这些观点。

文章解释了为什么许多物联网项目在试点阶段失败，因为它们低估了现实世界的约束。作者没有依赖于更高的处理能力或云框架，而是提倡拥抱约束来构建弹性系统。这包括以状态机的思维方式思考，最大限度地减少远程设备上的代码，并将恢复优先于一致性。最终，作者得出结论：为物理世界构建是一个令人谦卑的体验，它通过迫使人们面对混乱、不可预测的现实本质，从而培养更好的工程实践。

---

## 53. Android的侧载限制是最反消费者的举措

**原文标题**: Android's sideloading limits are its most anti-consumer move

**原文链接**: [https://www.makeuseof.com/androids-sideloading-limits-are-anti-consumer-move-yet/](https://www.makeuseof.com/androids-sideloading-limits-are-anti-consumer-move-yet/)

本文认为，谷歌计划于2025年10月开始实施的对侧载应用程序的限制是一项反消费者的举措，威胁着安卓的开放性。谷歌将要求开发者使用政府颁发的文件或联系信息来验证他们的身份，才能让他们的应用程序安装在配备谷歌移动服务（GMS）的设备上，这实际上是为应用程序分发创造了一个由谷歌控制的瓶颈。

作者使用NewPipe和Blokada等例子来说明，依赖Play商店中没有的应用程序的用户可能会失去访问权限。虽然谷歌将此举辩解为是针对恶意应用程序和不良行为者的安全措施，但作者质疑其有效性，并指出现有的安全检查机制，如Google Play Protect。作者认为，身份验证并不能保证完整性，因为之前已经有恶意软件通过Play商店。

文章警告说，这会对F-Droid等生态系统以及可能不愿意或无法进行身份验证的独立开发者造成“附带损害”，从而可能缩小应用程序生态系统并扼杀创新。虽然从技术上讲，侧载仍然可行，但增加的摩擦和潜在的解决方法（例如使用未经认证的设备）会带来权衡，包括技术复杂性和安全风险。作者总结说，这一举动标志着安卓开放性的关闭，引发了人们对其作为真正开源平台的未来的担忧。

---

## 54. 抽象，而非语法

**原文标题**: Abstraction, not syntax

**原文链接**: [https://ruudvanasseldonk.com/2025/abstraction-not-syntax](https://ruudvanasseldonk.com/2025/abstraction-not-syntax)

本文认为，配置文件（尤其是YAML）的问题主要不在于语法，而在于缺乏抽象。虽然像TOML或JSON变体等更简单的格式提供了一些表面上的改进，但它们并没有解决复杂配置中重复和潜在错误的根本问题。作者通过设置云存储桶的例子来说明这一点，强调了复制粘贴如何导致bug和维护挑战。

提出的解决方案是在配置中引入抽象，有效地将配置转化为代码。Cue、Dhall、Jsonnet和RCL等语言能够实现循环和变量等功能，从而减少重复、增强一致性，并使配置更易于维护。作者以RCL为例，展示了如何定义云存储桶，同时消除区域混合并动态计算保留时间。

然而，作者也承认存在权衡。引入配置语言需要一个构建步骤来生成最终的配置文件，并可能使grep变得复杂。此外，还存在过度复杂化的风险。他们建议通过将生成的文件检入源代码控制来保留可搜索性并促进审查，从而缓解这些问题。最终，作者提倡在配置中的数据和代码之间取得平衡，认为对于大型、复杂的配置，正确的方法是使用抽象来消除重复。

---

## 55. 游戏产业传奇人物：罗杰·迪恩

**原文标题**: Legends of the games industry: Roger Dean

**原文链接**: [https://spillhistorie.no/2025/10/03/legends-of-the-games-industry-roger-dean/](https://spillhistorie.no/2025/10/03/legends-of-the-games-industry-roger-dean/)

本文介绍了英国艺术家罗杰·迪恩，他以在音乐和视频游戏行业的作品而闻名，特别是他为Yes和Asia等前卫摇滚乐队创作的标志性设计，以及他对视频游戏发行商Psygnosis视觉形象的重大贡献。迪恩在希腊和香港的早期生活对他的艺术产生了重大影响。

采访重点关注迪恩在20世纪80年代进入游戏行业的情况。他最初为Henk Rogers（后来因俄罗斯方块而闻名）的《黑玛瑙》创作封面艺术，随后为Psygnosis设计了猫头鹰标志和名称，这一合作定义了该公司的视觉风格。迪恩描述了游戏封面通常在游戏本身完成之前就已经完成，他的艺术影响了游戏的内容。他回忆起参与《野蛮人》的制作，以及他的龙的设计是如何被融入游戏中的。他还强调了与蒂姆·怀特等艺术家的合作，他负责绘画，而他们负责上色。

对话还谈到了游戏包装的演变，迪恩对行业放弃高质量、值得作为礼品的包装盒（例如《兽影》的包装盒）表示失望。他回忆起1997年为Henk Rogers设计了官方俄罗斯方块标志，以加强统一的品牌形象。最后，迪恩讨论了一个他正在参与的、被取消的《黑玛瑙》续集，他为此组建了团队，负责游戏的全面设计。

---

## 56. 矩阵可以是你的朋友 (2002)

**原文标题**: Matrices can be your friends (2002)

**原文链接**: [https://www.sjbaker.org/steve/omniv/matrices_can_be_your_friends.html](https://www.sjbaker.org/steve/omniv/matrices_can_be_your_friends.html)

史蒂夫·贝克《矩阵可以成为你的朋友》旨在为OpenGL环境下，特别是对新手图形程序员，揭开矩阵的神秘面纱。他认为，与其将矩阵视为一堆随机数字的集合，不如将其效果可视化为对位于原点的单位立方体的作用，这样更直观。

文章强调，OpenGL矩阵以列优先顺序存储，虽然起初令人困惑，但会变得有利。 对于刚体变换（无缩放或剪切），最后一行通常为 0,0,0,1。 最右边的列（m[12], m[13], m[14]）表示平移——物体在世界中的位置。 左上角的 3x3 部分表示旋转。

通过可视化矩阵如何转换单位立方体的轴 (1,0,0)、(0,1,0) 和 (0,0,1)，程序员可以轻松理解旋转分量。 转换后的轴分别变为 (m[0], m[1], m[2])、(m[4], m[5], m[6]) 和 (m[8], m[9], m[10])。 将平移向量添加到这些变换后的点，即可获得立方体顶点的最终位置。

贝克随后通过可视化单位立方体如何变形，来说明如何使用矩阵进行更复杂的变换，如剪切和缩放。 他将这种方法与使用多个`glRotate/glTranslate/glScale`调用进行了对比，认为使用单个矩阵更有效。 最后，他将单位矩阵定义为“什么都不做”的矩阵，并给出了简单的数值表示。 核心信息是以可视化的方式思考矩阵，从而简化它们在对象定位和操作中的使用。

---

## 57. 纳米聊天

**原文标题**: Nanochat

**原文链接**: [https://simonwillison.net/2025/Oct/13/nanochat/](https://simonwillison.net/2025/Oct/13/nanochat/)

Nanochat是由Andrej Karpathy发起的一个新项目，它提供了一个完整的ChatGPT风格的LLM，训练成本约为100美元。该项目包括训练、推理和一个Web UI，所有这些都在一个单一、简洁且易于修改的代码库中，该代码库大约有8000行Python代码（使用PyTorch）以及一些用于分词器的Rust代码。Karpathy建议使用一个8XH100 NVIDIA节点进行训练，并估计4小时（约100美元）足以训练出一个能够进行对话的模型，而12小时则可以产生略微超过GPT-2的性能。

最终的模型大约有5.61亿个参数，使其适合在Raspberry Pi等设备上运行。该模型在一系列数据集上进行训练，包括FineWeb-Edu、SmolTalk、MMLU辅助训练集、GSM8K和ARC。该项目还包括一个带有简单JavaScript前端的Web服务器。

Hugging Face上提供了一个预构建的模型（sdobson/nanochat），该模型专为CUDA设计，但可以通过自定义脚本适应macOS上的CPU使用。文章演示了如何使用该模型生成文本，并提供了一个对提示“Tell me about dogs.”的示例回复。

---

## 58. Linux 的 MPTCP

**原文标题**: MPTCP for Linux

**原文链接**: [https://www.mptcp.dev/](https://www.mptcp.dev/)

多径TCP (MPTCP) 是标准TCP的扩展，如RFC 8684中所定义，它允许设备同时使用多个网络接口进行单个连接。它实现了带宽聚合、低延迟路径选择和无缝故障转移。

主要用例包括网络之间的无缝切换（如苹果在智能手机中的实现），基于延迟或成本等因素选择最佳网络路径，以及聚合来自多个网络的带宽（例如，结合固定和移动连接）。

从技术上讲，MPTCP通过不同的接口创建子流（常规TCP连接）。MPTCP使用TCP选项字段进行协商，如果对等方或中间盒不支持MPTCP，则回退到标准TCP。该系统利用路径管理器（负责子流管理和地址声明）以及数据包调度器（确定如何在可用子流之间分配数据包）。Linux提供内核内和用户空间路径管理器。

Linux (v6.10) 中的关键特性包括IPPROTO_MPTCP支持、MPTCP到TCP的回退、路径管理选项、标准套接字选项和调试功能。社区资源包括邮件列表、IRC频道以及用于内核和用户空间开发（mptcpd守护进程）的GitHub存储库。一些项目增强了现有工具（如iproute2和Network Manager）的MPTCP功能。

---

## 59. 模型连简单的指令都难以遵循，为何还要大力推行Agentic？

**原文标题**: Why the push for Agentic when models can barely follow a simple instruction?

**原文链接**: [https://forum.cursor.com/t/why-the-push-for-agentic-when-models-can-barely-follow-a-single-simple-instruction/137154](https://forum.cursor.com/t/why-the-push-for-agentic-when-models-can-barely-follow-a-single-simple-instruction/137154)

作者对围绕“自主编码”和“一切自主化”的炒作，特别是使用Cursor等工具进行后台编码的行为，表示怀疑和沮丧。他们的主要问题是：当AI模型甚至难以准确遵循简单的指令时，我们如何信任它们自主地进行更改？

他们引用了使用GPT-5和Gemini Pro的个人经历，这两个模型都未能根据提供的参考代码正确更新Go函数，要么遗漏部分内容，要么忽略更新。这让他们认为“自主炒作机器”主要会带来麻烦，并需要大量的调试工作。

作者认为，只有那些愿意处理由此产生的问题的人才是“自主幻想”的真正信徒。他们特别要求提供成功的自主编码实施的真实案例，试图了解为什么这项技术的核心能力似乎有限，却仍然引起如此多的兴奋。核心论点是，当前AI模型不够可靠，无法有效处理自主代码更改，因此推动自主系统还为时过早。

---

## 60. ImageMagick 领域指南草稿

**原文标题**: A Draft of the ImageMagick Field Guide

**原文链接**: [https://joeldare.com/imagemagick-field-guide.html](https://joeldare.com/imagemagick-field-guide.html)

ImageMagick实用指南草稿，提供常见图像处理任务的实用命令行配方。它强调使用较新的`magick`命令而不是`convert`。

本指南涵盖了为网络调整图像大小，包括在保持宽高比的同时指定宽度、移除元数据以减小文件大小、设置JPEG压缩以及隔行扫描以实现渐进式锐化。

它还涉及通过使用颜色模糊和图层优化技术来优化动画GIF以获得更小的文件大小。提供了将多个图像组合成动画GIF的说明，包括指定帧延迟、循环计数和帧管理处置方法。

此外，本指南还包括垂直堆叠图像（以及使用`+append`水平堆叠）的说明，并展示了如何将ImageMagick与URL结合使用以直接处理来自网络的图像。

本指南遵循特定的约定，例如使用`input.png`和`output.jpg`作为文件名、每行放置一个开关、在描述中使用将来时以及遵守AP样式标题大小写。它还表明了基于常见用例的结构。

最后，它鼓励订阅以接收完整指南和未来更新。

---

## 61. 炫耀一下：我做的AI玩具上架了

**原文标题**: Show HN: AI toy I worked on is in stores

**原文链接**: [https://www.walmart.com/ip/SANTA-SMAGICAL-PHONE/16364964771](https://www.walmart.com/ip/SANTA-SMAGICAL-PHONE/16364964771)

这篇“Show HN”帖子宣布作者开发的一款人工智能玩具现已在零售店，特别是沃尔玛有售。然而，所提供的内容仅集中于一个reCAPTCHA验证界面，其中包含熟悉的提示“机器人还是人类？”以及一个激活和确认人类身份的按钮。它还包括指向沃尔玛使用条款、隐私政策以及管理个人信息选项的标准法律链接。

标题（宣布人工智能玩具上市）与所提供的内容（reCAPTCHA验证）之间存在明显的不一致。内容实际上并未描述人工智能玩具本身、其功能、具体销售地点或与“Show HN”公告相关的任何其他细节。本质上，提供的摘录仅显示作者可能必须完成一个reCAPTCHA才能在沃尔玛网站或相关平台上发布他们的公告。

---

## 62. 根本原因分析？你做错了。

**原文标题**: Root cause analysis? You're doing it wrong

**原文链接**: [https://entropicthoughts.com/root-cause-analysis-youre-doing-it-wrong](https://entropicthoughts.com/root-cause-analysis-youre-doing-it-wrong)

本文批判了传统的事故调查“根本原因分析”（RCA），认为其基于过于简化的世界模型，导致理解不足和表面化的修复。文章提倡一种更彻底的系统思维方法，特别是基于系统理论的因果分析（CAST），该方法承认导致事故的交互因素的复杂性。

作者认为，更深入的分析，即使耗时，也能比RCA产生更有价值的教训，并更有效地预防未来的事故。RCA往往在确定了一个方便的“根本原因”后就停止调查。一个核心观点是，在复杂的系统中，事故是不可避免的，因此应着重于限制事故发生时的负面后果。

CAST强调，事故发生在危险状态的系统遇到不利环境条件时。预防危险是关键，这通过控制器利用技术和社会控制措施来维持系统约束来实现。

文章提供了一个软件故障的例子，最初的“分析”采用了一种肤浅的方法，只关注特定的设置组合。基于CAST的重新分析揭示了更广泛的一系列相关因素，涉及设计选择、沟通问题和运营实践。这个详细的CAST分析包括系统描述、事故时间线、初始问题以及故障和不安全交互的识别。目标是说明系统方法如何揭示更完整的事故真相，并为更全面的预防措施奠定基础。

---

## 63. 2025年诺贝尔经济学奖

**原文标题**: The Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel 2025

**原文链接**: [https://www.nobelprize.org/prizes/economic-sciences/2025/summary/](https://www.nobelprize.org/prizes/economic-sciences/2025/summary/)

2025年诺贝尔经济学纪念奖授予乔尔·莫基尔、菲利普·阿吉翁和彼得·豪伊特，以表彰他们在创新驱动经济增长方面的工作。

乔尔·莫基尔独享一半奖金，“因为他确定了通过技术进步实现持续增长的先决条件”。他的研究侧重于促进持续创新和技术进步，从而带来长期经济繁荣的历史和文化因素。

菲利普·阿吉翁和彼得·豪伊特分享另一半奖金，“因为他们提出了通过创造性破坏实现持续增长的理论”。他们的工作强调了经济增长的动态过程，即新的创新不断取代旧的技术和方法，从而提高生产力并促进整体经济进步，即使这可能会扰乱现有行业和就业。公告强调了他们对理解创新如何推动长期经济扩张的贡献。该页面还提供导航选项，以访问有关获奖者及其工作的摘要、获奖公告、新闻稿、通俗信息和高级信息。

---

## 64. 古代巴塔哥尼亚的狩猎采集者会照顾受伤和残疾的同伴。

**原文标题**: Ancient Patagonian hunter-gatherers took care of their injured and disabled

**原文链接**: [https://phys.org/news/2025-10-ancient-patagonian-hunter-disabled.html](https://phys.org/news/2025-10-ancient-patagonian-hunter-disabled.html)

这篇Phys.org文章报道了一项发表在《国际古病理学杂志》上的研究。维多利亚·罗马诺博士和她的同事分析了巴塔哥尼亚189名全新世晚期狩猎采集者的骨骼遗骸，以了解创伤性损伤的社会影响。通过分析3000多个骨骼元素，研究发现约20%的个体表现出骨骼创伤，男性和女性的发生率相似，成人高于儿童。

虽然确定受伤原因很困难，但研究人员认为大多数是意外事故。这些损伤被分为轻度、中度和重症监护，反映了所需的护理程度和持续时间。轻度损伤，如鼻骨或肋骨骨折，很常见，可能对群体动态影响甚微。中度损伤，如手臂骨折，约占病例的18%，会抑制日常活动数月。重症监护损伤占病例的13%，需要长期护理。

一个值得注意的案例涉及一名髋关节严重损伤的个体。愈合的骨骼表明其受到了长期护理，证明该个体在受伤后存活了多年。这项研究意义重大，因为它是首次针对非定居狩猎采集者群体中的照护行为进行的人口水平分析。虽然早期时代存在一些照护的证据，但这项研究更广泛地了解了流动性限制如何影响这些社区中的照护行为。罗马诺博士建议未来的研究可以探索照护动态如何随时间变化。

---

## 65. CRDT与SQLite：本地优先的值同步

**原文标题**: CRDT and SQLite: Local-First Value Synchronization

**原文链接**: [https://marcobambini.substack.com/p/the-secret-life-of-a-local-first](https://marcobambini.substack.com/p/the-secret-life-of-a-local-first)

我能访问文章链接。以下是摘要：

Marco Bambini的文章《CRDT与SQLite：本地优先的值同步》探讨了本地优先应用的优势和实施策略，特别关注于使用无冲突复制数据类型（CRDT）与SQLite进行数据同步。

作者认为，本地优先应用优先考虑本地数据存储和操作，通过离线功能、更快的响应速度和改进的隐私，提供卓越的用户体验。他们将此与传统客户端-服务器架构进行对比，后者严重依赖网络连接。

核心概念是CRDT的使用。CRDT是可以独立更新和合并而不会发生冲突的数据结构。文章解释说，通过将应用程序数据本地存储在SQLite数据库中，并利用CRDT进行数据操作，更新可以在离线状态下执行，然后在连接恢复时与中央服务器或其他对等方同步。由于CRDT固有地自动解决冲突，因此这种同步过程变得更简单、更可靠。

作者提到了适用于各种数据类型和操作的不同类型的CRDT，例如计数器、集合和文本编辑器，以及如何使用扩展或自定义实现将它们与SQLite集成。

关键要点是，将SQLite的本地存储功能与CRDT的冲突解决特性相结合，为构建强大且用户友好的本地优先应用提供了强大的基础，这些应用可以处理离线场景和无缝数据同步。文章最终倡导开发人员考虑这种方法来构建更具响应性和弹性的应用程序。

---

## 66. 最近学到的一些零碎的家庭实验室知识

**原文标题**: More random home lab things I've recently learned

**原文链接**: [https://chollinger.com/blog/2025/10/more-homelab-things-ive-recently-learned/](https://chollinger.com/blog/2025/10/more-homelab-things-ive-recently-learned/)

本文详述了作者近期的家庭实验室探索经历，重点介绍了其 Proxmox 集群、TrueNAS 备份和整体网络设置的故障排除和学习经验。

主要学习内容包括：

*   **树莓派 5 NVMe SSD 支持：** 发现树莓派 5 可以通过适配器使用 NVMe SSD 来替代老化的 SD 卡，显著提高性能，但需要适当的散热和电源考虑。
*   **在 NVMe 上安装树莓派 OS：** 概述了由于缺少标准安装程序而在 NVMe 驱动器上安装树莓派 OS 的变通方法。
*   **Proxmox ARM 和 OOM 终止：** 解决了 Proxmox 在 ARM 上遇到的问题，特别是内存不足 (OOM) 错误，通过将内核页面大小设置为 4K 并使用 OVMF BIOS 解决。
*   **使用 Kpartx 的 VM Chroot：** 学习了如何通过使用 kpartx 挂载虚拟磁盘来 chroot 进入 QEMU VM 以进行调试。
*   **Proxmox 备份服务器死锁：** 描述了一种完整的 PBS ZFS 卷可能导致死锁，阻止垃圾回收的场景，以及涉及删除 ZFS 快照和设置配额的修复方法。
*   **CyberPower UPS 管理软件：** 强调了 CyberPower 的 PowerPanel Business 软件可用于管理其 UPS 设备和访问 SNMP 数据以进行监控。
*   **DAV 服务器和 Mealie：** 提及了使用 Davis 作为 (CAL)DAV 服务器，并表达了对 Mealie（一个自托管的食谱管理器）的热情。

---

## 67. Putting a dumb weather station on the internet

**原文标题**: Putting a dumb weather station on the internet

**原文链接**: [https://colincogle.name/blog/byo-weather-station/](https://colincogle.name/blog/byo-weather-station/)

Colin Cogle's blog post details how to build a DIY internet-connected weather station using inexpensive components and open-source software. He starts with a cheap, nameless wireless indoor/outdoor thermometer purchased from Temu. By leveraging an RTL-SDR USB dongle and the `rtl_433` software, he intercepts the unencrypted radio transmissions from the thermometer's outdoor sensor.

The intercepted data is then piped into a custom PowerShell script. This script, which he provides and explains, filters the relevant data, parses the temperature and humidity readings, and uses his previously developed command-line tool, `aprs-weather-submit`, to transmit the weather information to the APRS-IS network, making it accessible to amateur radio enthusiasts.

Further extending the project, Cogle integrates a Mastodon bot. The PowerShell script is modified to periodically post the weather data to a dedicated Mastodon account, allowing anyone on the federated social network to follow the weather station's updates. He stresses the importance of proper bot etiquette, limiting the posts to once per hour.

The post highlights the hacker ethos of amateur radio, showcasing how readily available and inexpensive components, combined with open-source software and scripting, can be used to create a useful and informative project. He includes links to the relevant software, APRS resources, and his weather station's APRS.to and Mastodon pages.


---

## 68. StreamingVLM: Real-Time Understanding for Infinite Video Streams

**原文标题**: StreamingVLM: Real-Time Understanding for Infinite Video Streams

**原文链接**: [https://arxiv.org/abs/2510.09608](https://arxiv.org/abs/2510.09608)

生成摘要时出错

---

## 69. Show HN: Daily install trends of AI coding extensions in VS Code

**原文标题**: Show HN: Daily install trends of AI coding extensions in VS Code

**原文链接**: [https://bloomberry.com/coding-tools.html](https://bloomberry.com/coding-tools.html)

生成摘要时出错

---

## 70. Microsoft 'illegally' tracked students via 365 Education, says data watchdog

**原文标题**: Microsoft 'illegally' tracked students via 365 Education, says data watchdog

**原文链接**: [https://www.theregister.com/2025/10/13/microsoft_365_education_gdpr/](https://www.theregister.com/2025/10/13/microsoft_365_education_gdpr/)

生成摘要时出错

---

## 71. Some graphene firms have reaped its potential but others are struggling

**原文标题**: Some graphene firms have reaped its potential but others are struggling

**原文链接**: [https://www.theguardian.com/business/2025/oct/13/lab-to-fab-are-promises-of-a-graphene-revolution-finally-coming-true](https://www.theguardian.com/business/2025/oct/13/lab-to-fab-are-promises-of-a-graphene-revolution-finally-coming-true)

生成摘要时出错

---

## 72. Fastmail desktop app

**原文标题**: Fastmail desktop app

**原文链接**: [https://www.fastmail.com/blog/desktop-app/](https://www.fastmail.com/blog/desktop-app/)

生成摘要时出错

---

## 73. DOJ seizes $15B in Bitcoin from 'pig butchering' scam based in Cambodia

**原文标题**: DOJ seizes $15B in Bitcoin from 'pig butchering' scam based in Cambodia

**原文链接**: [https://www.justice.gov/opa/pr/chairman-prince-group-indicted-operating-cambodian-forced-labor-scam-compounds-engaged](https://www.justice.gov/opa/pr/chairman-prince-group-indicted-operating-cambodian-forced-labor-scam-compounds-engaged)

生成摘要时出错

---

## 74. Tauri binding for Python through Pyo3

**原文标题**: Tauri binding for Python through Pyo3

**原文链接**: [https://github.com/pytauri/pytauri](https://github.com/pytauri/pytauri)

生成摘要时出错

---

## 75. Weekend projects: Chicken Squisher 3000

**原文标题**: Weekend projects: Chicken Squisher 3000

**原文链接**: [https://lcamtuf.substack.com/p/weekend-projects-chicken-squisher](https://lcamtuf.substack.com/p/weekend-projects-chicken-squisher)

生成摘要时出错

---

## 76. RustPython: A Python Interpreter Written in Rust

**原文标题**: RustPython: A Python Interpreter Written in Rust

**原文链接**: [https://rustpython.github.io/](https://rustpython.github.io/)

生成摘要时出错

---

## 77. Modifying a Casio F-Series Digital Watch (2020)

**原文标题**: Modifying a Casio F-Series Digital Watch (2020)

**原文链接**: [https://shellzine.net/casio-f-series-mods/](https://shellzine.net/casio-f-series-mods/)

生成摘要时出错

---

## 78. Wireguard FPGA

**原文标题**: Wireguard FPGA

**原文链接**: [https://github.com/chili-chips-ba/wireguard-fpga](https://github.com/chili-chips-ba/wireguard-fpga)

生成摘要时出错

---

## 79. Clockss: Digital preservation services run by academic publishers and libraries

**原文标题**: Clockss: Digital preservation services run by academic publishers and libraries

**原文链接**: [https://clockss.org/](https://clockss.org/)

生成摘要时出错

---

## 80. Spotlight on pdfly, the Swiss Army knife for PDF files

**原文标题**: Spotlight on pdfly, the Swiss Army knife for PDF files

**原文链接**: [https://chezsoi.org/lucas/blog/spotlight-on-pdfly.html](https://chezsoi.org/lucas/blog/spotlight-on-pdfly.html)

生成摘要时出错

---

## 81. Control your Canon Camera wirelessly

**原文标题**: Control your Canon Camera wirelessly

**原文链接**: [https://github.com/JulianSchroden/cine_remote](https://github.com/JulianSchroden/cine_remote)

生成摘要时出错

---

## 82. LaTeXpOsEd: A Systematic Analysis of Information Leakage in Preprint Archives

**原文标题**: LaTeXpOsEd: A Systematic Analysis of Information Leakage in Preprint Archives

**原文链接**: [https://arxiv.org/abs/2510.03761](https://arxiv.org/abs/2510.03761)

生成摘要时出错

---

## 83. A series of debugging sessions for Strimzi

**原文标题**: A series of debugging sessions for Strimzi

**原文链接**: [https://github.com/fvaleri/strimzi-debugging](https://github.com/fvaleri/strimzi-debugging)

生成摘要时出错

---

## 84. Modern Linux tools

**原文标题**: Modern Linux tools

**原文链接**: [https://ikrima.dev/dev-notes/linux/linux-modern-tools/](https://ikrima.dev/dev-notes/linux/linux-modern-tools/)

生成摘要时出错

---

## 85. Uv overtakes pip in CI

**原文标题**: Uv overtakes pip in CI

**原文链接**: [https://wagtail.org/blog/uv-overtakes-pip-in-ci/](https://wagtail.org/blog/uv-overtakes-pip-in-ci/)

生成摘要时出错

---

## 86. Switch to Jujutsu Already: A Tutorial

**原文标题**: Switch to Jujutsu Already: A Tutorial

**原文链接**: [https://www.stavros.io/posts/switch-to-jujutsu-already-a-tutorial/](https://www.stavros.io/posts/switch-to-jujutsu-already-a-tutorial/)

生成摘要时出错

---

## 87. Riding the Rhine: Europe's first certified long-distance cycle path

**原文标题**: Riding the Rhine: Europe's first certified long-distance cycle path

**原文链接**: [https://www.bbc.com/travel/article/20251010-riding-the-rhine-europes-first-certified-long-distance-cycle-path](https://www.bbc.com/travel/article/20251010-riding-the-rhine-europes-first-certified-long-distance-cycle-path)

生成摘要时出错

---

## 88. Making regular GPS ultra-precise

**原文标题**: Making regular GPS ultra-precise

**原文链接**: [https://norwegianscitechnews.com/2025/10/making-regular-gps-ultra-precise/](https://norwegianscitechnews.com/2025/10/making-regular-gps-ultra-precise/)

生成摘要时出错

---

## 89. Reverse Engineering a 1979 Camera's Spec

**原文标题**: Reverse Engineering a 1979 Camera's Spec

**原文链接**: [https://blog.mano.lol/posts/film/](https://blog.mano.lol/posts/film/)

生成摘要时出错

---

## 90. Systems as Mirrors

**原文标题**: Systems as Mirrors

**原文链接**: [https://iamstelios.com/blog/systems-as-mirrors/](https://iamstelios.com/blog/systems-as-mirrors/)

生成摘要时出错

---

## 91. Windows 10 support ends on October 14, 2025

**原文标题**: Windows 10 support ends on October 14, 2025

**原文链接**: [https://support.microsoft.com/en-us/windows/windows-10-support-ends-on-october-14-2025-2ca8b313-1946-43d3-b55c-2b95b107f281](https://support.microsoft.com/en-us/windows/windows-10-support-ends-on-october-14-2025-2ca8b313-1946-43d3-b55c-2b95b107f281)

生成摘要时出错

---

## 92. A years-long Turkish alphabet bug in the Kotlin compiler

**原文标题**: A years-long Turkish alphabet bug in the Kotlin compiler

**原文链接**: [https://sam-cooper.medium.com/the-country-that-broke-kotlin-84bdd0afb237](https://sam-cooper.medium.com/the-country-that-broke-kotlin-84bdd0afb237)

生成摘要时出错

---

## 93. Hackers can steal 2FA codes and private messages from Android phones

**原文标题**: Hackers can steal 2FA codes and private messages from Android phones

**原文链接**: [https://arstechnica.com/security/2025/10/no-fix-yet-for-attack-that-lets-hackers-pluck-2fa-codes-from-android-phones/](https://arstechnica.com/security/2025/10/no-fix-yet-for-attack-that-lets-hackers-pluck-2fa-codes-from-android-phones/)

生成摘要时出错

---

## 94. Two Paths to Memory Safety: CHERI and OMA

**原文标题**: Two Paths to Memory Safety: CHERI and OMA

**原文链接**: [https://ednutting.com/2025/10/05/cheri-vs-oma.html](https://ednutting.com/2025/10/05/cheri-vs-oma.html)

生成摘要时出错

---

## 95. Show HN: I built a simple ambient sound app with no ads or subscriptions

**原文标题**: Show HN: I built a simple ambient sound app with no ads or subscriptions

**原文链接**: [https://ambisounds.app/](https://ambisounds.app/)

生成摘要时出错

---

## 96. JPMorganChase Launches $1.5T Security and Resiliency Initiative

**原文标题**: JPMorganChase Launches $1.5T Security and Resiliency Initiative

**原文链接**: [https://www.jpmorganchase.com/newsroom/press-releases/2025/jpmc-security-resiliency-initiative](https://www.jpmorganchase.com/newsroom/press-releases/2025/jpmc-security-resiliency-initiative)

生成摘要时出错

---

## 97. 80% of employees say their workplace is toxic

**原文标题**: 80% of employees say their workplace is toxic

**原文链接**: [https://www.fastcompany.com/91418555/80-percent-of-employees-say-their-workplace-is-toxic](https://www.fastcompany.com/91418555/80-percent-of-employees-say-their-workplace-is-toxic)

生成摘要时出错

---

## 98. A $6B Nuclear U.S. Navy Aircraft Carrier 'Sunk' by $100M Diesel 'AIP' Sub

**原文标题**: A $6B Nuclear U.S. Navy Aircraft Carrier 'Sunk' by $100M Diesel 'AIP' Sub

**原文链接**: [https://nationalsecurityjournal.org/a-6000000000-nuclear-u-s-navy-aircraft-carrier-sunk-by-100000000-diesel-aip-sub/](https://nationalsecurityjournal.org/a-6000000000-nuclear-u-s-navy-aircraft-carrier-sunk-by-100000000-diesel-aip-sub/)

生成摘要时出错

---

## 99. Don't Be a Sucker (1943) [video]

**原文标题**: Don't Be a Sucker (1943) [video]

**原文链接**: [https://www.youtube.com/watch?v=vGAqYNFQdZ4](https://www.youtube.com/watch?v=vGAqYNFQdZ4)

生成摘要时出错

---

## 100. KTX – npx for Kotlin and JVM to install jars or Kotlin scripts

**原文标题**: KTX – npx for Kotlin and JVM to install jars or Kotlin scripts

**原文链接**: [https://github.com/mpetuska/ktx](https://github.com/mpetuska/ktx)

生成摘要时出错

---

