# Hacker News 热门文章摘要 (2026-04-11)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 小模型也发现了 Mythos 发现的漏洞。

**原文标题**: Small models also found the vulnerabilities that Mythos found

**原文链接**: [https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier](https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier)

在本文中，作者斯坦尼斯拉夫·福特（Stanislav Fort，来自 AISLE）分析了 Anthropic 发布的“Mythos”模型，该模型展示了 AI 自主发现并利用零日漏洞的能力。福特认为，尽管 Mythos 的成就意义重大，但 AI 的网络安全能力呈现出“锯齿状”特征——即能力并不会随模型规模平滑扩展，且前沿模型并不总是表现最佳。

AISLE 的研究表明，小型、廉价且开源权重的模型（部分参数量仅为 36 亿）可以复制 Mythos 的大部分核心分析工作。在测试中，八个小型模型全部成功检测到了 Anthropic 所强调的一项关键 FreeBSD NFS 漏洞。此外，在专门的 OWASP 推理任务中，小型模型的表现实际上优于包括 GPT-4 和 Claude 各版本在内的多个大型前沿模型，准确识别出了大型模型所遗漏的误报 SQL 注入。

作者得出结论，AI 网络安全的真正“护城河”在于系统而非模型。其核心价值体现在专家设计的“脚手架”中——即对发现、验证、分类及维护者协作的流程编排——而非单纯的模型规模。这预示着 AI 防御经济学的转变：组织无需依赖单一昂贵且“博学”的模型，而是可以通过部署数千个廉价的专用模型进行全谱扫描，从而获得更优的效果。最终，AISLE 的研究表明，虽然 Anthropic 证实了 AI 驱动安全这一领域的潜力，但最有效的解决方案将是模型无关的，且建立在深厚的领域专业知识之上。

---

## 2. Cirrus Labs 将加入 OpenAI

**原文标题**: Cirrus Labs to join OpenAI

**原文链接**: [https://cirruslabs.org/](https://cirruslabs.org/)

Cirrus Labs 是一家由 Fedor Korotkov 于 2017 年创立的自筹资金基础设施公司，现已宣布加入 OpenAI，成为其**智能体基础设施团队**（Agent Infrastructure team）的一员。

Cirrus Labs 以其在持续集成和虚拟化领域的创新（特别是针对 Apple Silicon 的热门虚拟化解决方案 **Tart**）而闻名。目前，该公司正将其重心从以人为核心的云端工具转向新兴的“**智能体工程**”（agentic engineering）时代。Korotkov 解释称，正如人类工程师需要新环境在云端大展身手一样，AI 智能体现在也需要专门的基础设施和工具来提高生产力。加入 OpenAI 将使团队能够在 AI 开发的最前沿构建这些环境。

此次收购将立即改变 Cirrus Labs 现有的产品体系：
*   **开源工具**：包括 **Tart、Vetu 和 Orchard** 在内的工具将以更宽松的条款重新授权，并已取消所有许可费用。
*   **Cirrus Runners**：该服务不再接受新客户，但现有合同在剩余期限内将继续履行。
*   **Cirrus CI**：该平台将于 **2026 年 6 月 1 日**正式关停。

这一公告标志着该公司九年独立征程的结束。自成立以来，该公司始终坚持自筹资金，以保持对工程主导型解决方案的专注。

---

## 3. Advanced Mac Substitute is an API-level reimplementation of 1980s-era Mac OS

**原文标题**: Advanced Mac Substitute is an API-level reimplementation of 1980s-era Mac OS

**原文链接**: [https://www.v68k.org/advanced-mac-substitute/](https://www.v68k.org/advanced-mac-substitute/)

生成摘要时出错

---

## 4. Surelock：Rust 无死锁互斥锁

**原文标题**: Surelock: Deadlock-Free Mutexes for Rust

**原文链接**: [https://notes.brooklynzelenka.com/Blog/Surelock](https://notes.brooklynzelenka.com/Blog/Surelock)

**Surelock** 是一个新的 Rust 库，旨在消除死锁。它确保只要代码能通过编译，就在数学上证明了其无死锁性。虽然 Rust 以防止数据竞争而闻名，但传统上它并不提供针对死锁的编译时保护。Surelock 通过两种主要机制破坏了科夫曼条件（Coffman Conditions）中的“循环等待”条件：

1.  **LockSet（同级）：** 对于同时获取多个锁的情况，Surelock 使用 `LockSet` 在运行时根据唯一且稳定的 ID 对锁进行排序，从而确保无论锁如何传递，其获取顺序都是确定性的。
2.  **Levels（跨级）：** 对于增量获取锁的情况，Surelock 采用类型级排序（`Level<N>`）。它通过编译时 Trait 约束强制执行严格的全序关系，拒绝任何试图以非递增顺序获取锁的代码。

该库的核心创新是 **MutexKey**，这是一种仅移动（move-only）的“线性作用域令牌”。当获取锁时，旧令牌被消耗并重新发回一个新的令牌，其中携带了当前状态的类型级记录。这种令牌的“串联”机制使得在锁层级结构中进行回溯变得不可能。

**核心特性：**
*   **全序安全性：** 与基于 DAG 的模型不同，Surelock 使用严格的全序关系来确保所有线程的绝对安全。
*   **零运行时开销：** 不需要全局分析或运行时跟踪，所有工作均由编译器完成。
*   **广泛的兼容性：** 兼容 `no_std`，并支持没有原生 CAS（比较并交换）的嵌入式目标。
*   **易用性：** 为标准用途提供 `lock_scope`，并为嵌入式环境中的显式控制提供 `Locksmith` 单例。
*   **逃生舱：** 包含一个受特性门控（feature-gated）的 `unchecked_lock`，用于必须绕过严格规则的极少数情况。

Surelock 旨在让死锁预防变得足够易用，以便在日常开发中使用，将不可见的运行时故障转化为直观的编译器错误。

---

## 5. 手机之旅

**原文标题**: Phone Trips

**原文链接**: [http://www.wideweb.com/phonetrips/](http://www.wideweb.com/phonetrips/)

**“电话之旅” (Phone Trips)** 是一个致力于保存机电式电话网络声音和历史的数字档案馆，内容主要涵盖 20 世纪 60 年代和 70 年代。该网站由马克·伯内 (Mark Bernay) 策划，并收录了埃文·多贝尔 (Evan Doorbell) 的大量贡献。多贝尔是一位著名的“电话黑客” (phone phreak) 和解说员，以其详尽的技术讲解和广播级的录音质量而闻名。

该档案馆作为以下几类内容的数字化存储库：

*   **现场录音：** 这些被称为“电话之旅”的录音记录了美国各地区（特别是华盛顿州、加利福尼亚州和北卡罗来纳州）以及英国和加拿大的独特交换机声音和信令。
*   **技术教育：** 网站深入解析了老式交换技术，包括步进式 (SXS)、纵横制和面板制系统。埃文·多贝尔的《长途电话之声》(Sounds of Long Distance) 等主要系列详细讲解了旧贝尔系统的运行机制。
*   **社交与幽默内容：** 除了技术数据，馆藏还包括“贝尔小组” (Group Bell) 的幽默短剧（如“Dom Tuffy”录音带）、早期会议电话录音以及 20 世纪 70 年代的“笑话热线”。
*   **博物馆保护：** 档案馆包含来自老式电话设备博物馆和新英格兰电话博物馆的录音，捕捉了经过修复且功能正常的硬件声音。

为了确保易用性，所有录音均已转换为 MP3 格式，方便在线播放和下载。虽然该网站目前仍是核心的历史资源，但作者指出，埃文·多贝尔最新的解说素材现已托管在其专门的 YouTube 频道上。归根结底，“电话之旅”作为一个至关重要的文化和技术档案，记录了一个已经消逝的电信时代。

---

## 6. 磨平我的 MacBook 边角

**原文标题**: Filing the corners off my MacBooks

**原文链接**: [https://kentwalters.com/posts/corners/](https://kentwalters.com/posts/corners/)

在这篇文章中，作者描述了他们通过锉平 MacBook 锋利的铝制边缘来对其进行物理改造的实践。出于对工具个性化的追求和对人体工程学舒适度的需求，作者认为苹果的工业设计虽然外观精致，但在使用过程中会令手腕感到不适。

作者概述了这一改造的具体技术流程：
*   **防护：** 用胶带封住键盘和扬声器，防止铝屑进入内部组件。
*   **固定：** 以“适度的压力”将机器固定在工作台上。
*   **精修：** 先用粗锉刀将边缘（特别是掌托和凹口处）锉圆，随后使用 150 目和 400 目的砂纸打磨，以实现光滑的触感。

尽管那些担心机器转手价值或美学完整性的科技爱好者可能会对此感到“抓狂”，但作者对最终效果表示完全满意。他们在结尾处鼓励他人克服对改装昂贵硬件的恐惧，并倡导一种“尽管去折腾”的哲学，以确保工具是服务于用户，而不是让用户去迁就工具。

---

## 7. 保持 Postgres 队列健康

**原文标题**: Keeping a Postgres Queue Healthy

**原文链接**: [https://planetscale.com/blog/keeping-a-postgres-queue-healthy](https://planetscale.com/blog/keeping-a-postgres-queue-healthy)

在《保持 Postgres 队列健康》一文中，Simeon Griggs 探讨了在 Postgres 数据库中管理作业队列的挑战，特别是在混合负载环境下。虽然 Postgres 是实现队列的可靠选择，但其多版本并发控制（MVCC）架构带来了一个特定风险：即“死元组”（dead tuples）的堆积。

在队列中，数据行是瞬态的——被插入、读取后迅速删除。然而，Postgres 并不会立即移除已删除的行，而是将其标记为死元组，待后续由 `autovacuum` 进程回收。如果这些元组持续堆积，就会导致“膨胀”（bloat），迫使数据库扫描大量不可见数据，从而降低堆扫描和索引扫描的性能。

清理工作的核心障碍是 **MVCC 水平线**（MVCC horizon）。Postgres 无法回收任何对当前活跃事务可能仍然可见的死元组。在混合负载的数据库中，长时间运行的分析查询或连续不断的重叠事务可能会“钉住”这一水平线。这会阻碍 `autovacuum` 回收空间，导致失控的膨胀，最终可能威胁到整个应用的稳定性。

虽然调优 `autovacuum` 设置或实施标准超时（如 `statement_timeout` 或 Postgres 17 中新增的 `transaction_timeout`）有所帮助，但这些手段往往过于粗放。它们无法解决因多个查询重叠而共同导致 MVCC 水平线停滞的问题。

文章最后介绍了 **PlanetScale 的 Database Traffic Control™**，这是其 Insights 扩展的一项功能。该工具支持细粒度的资源预算，允许用户限制低优先级负载。通过防止这些查询消耗过多资源或无限期运行，开发人员可以确保 MVCC 水平线正常推进，从而保持高优先级作业队列的健康与高性能。

---

## 8. 造就了一个行业的问题

**原文标题**: The Problem That Built an Industry

**原文链接**: [https://ajitem.com/blog/iron-core-part-1-the-problem-that-built-an-industry/](https://ajitem.com/blog/iron-core-part-1-the-problem-that-built-an-industry/)

在《造就一个行业的难题》一文中，Ajitem Sahasrabuddhe 探讨了支撑全球航空业、已有 60 年历史的“铁芯”基础设施。尽管行业正向现代云原生系统转型，但航班预订依然依赖于 20 世纪 60 年代建立的技术基石。

故事始于 1964 年 SABRE 的创建，这是美国航空与 IBM 的合作成果，旨在取代效能低下的手动卡片式预订系统。这促使全行业采用了 IBM 的**事务处理设施 (TPF)**。与现代操作系统不同，TPF 是一种专门针对海量交易处理而优化的运行时环境，响应时间不到一毫秒。它每秒可处理高达 5 万笔交易，通过摒弃线程或动态内存分配等标准抽象概念的精简设计，其性能超越了许多现代替代方案。

Sahasrabuddhe 展示了单次预订如何触发一个复杂的链条，涉及 Amadeus 等**全球分销系统 (GDS)** 和印度航空 Altéa 等**旅客服务系统 (PSS)**。他还指出，像 IndiGo 这样的低成本航空公司在架构上有所不同，它们使用 Navitaire 等系统，优先考虑效率而非复杂的航司间联运。

本文总结了三个核心教训：
1. **目标契合度**：针对特定的工作负载，经过良好维护的专用传统工具往往优于时髦的现代架构。
2. **趋同演化**：由于 TPF 是处理高交易量的最优方案，主要行业参与者不约而同地选择了它。
3. **迁移难度**：航空公司系统之间深层的相互依赖，使得现代化改造“铁芯”技术成为一项艰巨且高风险的任务。

最终，六位字符的旅客订座记录 (PNR) 成为了连接全球各异构系统的“纽带”，将这些跨越数十年构建的系统紧紧维系在一起。

---

## 9. Starfling: A one-tap endless orbital slingshot game in a single HTML file

**原文标题**: Starfling: A one-tap endless orbital slingshot game in a single HTML file

**原文链接**: [https://playstarfling.com](https://playstarfling.com)

生成摘要时出错

---

## 10. Optimal Strategy for Connect 4

**原文标题**: Optimal Strategy for Connect 4

**原文链接**: [https://2swap.github.io/WeakC4/explanation/](https://2swap.github.io/WeakC4/explanation/)

生成摘要时出错

---

## 11. South Korea introduces universal basic mobile data access

**原文标题**: South Korea introduces universal basic mobile data access

**原文链接**: [https://www.theregister.com/2026/04/10/south_korea_data_access_universal/](https://www.theregister.com/2026/04/10/south_korea_data_access_universal/)

生成摘要时出错

---

## 12. Every plane you see in the sky – you can now follow it from the cockpit in 3D

**原文标题**: Every plane you see in the sky – you can now follow it from the cockpit in 3D

**原文链接**: [https://flight-viz.com/cockpit.html?lat=40.64&lon=-73.78&alt=3000&hdg=220&spd=130&cs=DAL123](https://flight-viz.com/cockpit.html?lat=40.64&lon=-73.78&alt=3000&hdg=220&spd=130&cs=DAL123)

生成摘要时出错

---

## 13. Volunteers turn a fan's recordings of 10K concerts into an online treasure trove

**原文标题**: Volunteers turn a fan's recordings of 10K concerts into an online treasure trove

**原文链接**: [https://apnews.com/article/aadam-jacobs-collection-concerts-internet-archive-chicago-b1c9c4466a2db409a83523ad84b79d62](https://apnews.com/article/aadam-jacobs-collection-concerts-internet-archive-chicago-b1c9c4466a2db409a83523ad84b79d62)

生成摘要时出错

---

## 14. Cooperative Vectors Introduction

**原文标题**: Cooperative Vectors Introduction

**原文链接**: [https://www.evolvebenchmark.com/blog-posts/cooperative-vectors-introduction](https://www.evolvebenchmark.com/blog-posts/cooperative-vectors-introduction)

生成摘要时出错

---

## 15. The future of everything is lies, I guess – Part 5: Annoyances

**原文标题**: The future of everything is lies, I guess – Part 5: Annoyances

**原文链接**: [https://aphyr.com/posts/415-the-future-of-everything-is-lies-i-guess-annoyances](https://aphyr.com/posts/415-the-future-of-everything-is-lies-i-guess-annoyances)

生成摘要时出错

---

## 16. Previously unknown verses by Empedocles found on papyrus

**原文标题**: Previously unknown verses by Empedocles found on papyrus

**原文链接**: [https://www.thehistoryblog.com/archives/75792](https://www.thehistoryblog.com/archives/75792)

生成摘要时出错

---

## 17. 1D Chess

**原文标题**: 1D Chess

**原文链接**: [https://rowan441.github.io/1dchess/chess.html](https://rowan441.github.io/1dchess/chess.html)

生成摘要时出错

---

## 18. How Much Linear Memory Access Is Enough?

**原文标题**: How Much Linear Memory Access Is Enough?

**原文链接**: [https://solidean.com/blog/2026/how-much-linear-memory-access-is-enough/](https://solidean.com/blog/2026/how-much-linear-memory-access-is-enough/)

生成摘要时出错

---

## 19. How Passive Radar Works

**原文标题**: How Passive Radar Works

**原文链接**: [https://www.passiveradar.com/how-passive-radar-works/](https://www.passiveradar.com/how-passive-radar-works/)

生成摘要时出错

---

## 20. Installing every* Firefox extension

**原文标题**: Installing every* Firefox extension

**原文链接**: [https://jack.cab/blog/every-firefox-extension](https://jack.cab/blog/every-firefox-extension)

生成摘要时出错

---

## 21. Chimpanzees in Uganda locked in eight-year 'civil war', say researchers

**原文标题**: Chimpanzees in Uganda locked in eight-year 'civil war', say researchers

**原文链接**: [https://www.bbc.com/news/articles/cr71lkzv49po](https://www.bbc.com/news/articles/cr71lkzv49po)

生成摘要时出错

---

## 22. Rockstar Games Hacked, Hackers Threaten a Massive Data Leak If Not Paid Ransom

**原文标题**: Rockstar Games Hacked, Hackers Threaten a Massive Data Leak If Not Paid Ransom

**原文链接**: [https://kotaku.com/rockstar-games-reportedly-hacked-massive-data-leak-ransom-gta-6-shinyhunters-2000686858](https://kotaku.com/rockstar-games-reportedly-hacked-massive-data-leak-ransom-gta-6-shinyhunters-2000686858)

生成摘要时出错

---

## 23. AI assistance when contributing to the Linux kernel

**原文标题**: AI assistance when contributing to the Linux kernel

**原文链接**: [https://github.com/torvalds/linux/blob/master/Documentation/process/coding-assistants.rst](https://github.com/torvalds/linux/blob/master/Documentation/process/coding-assistants.rst)

生成摘要时出错

---

## 24. Artemis II safely splashes down

**原文标题**: Artemis II safely splashes down

**原文链接**: [https://www.cbsnews.com/live-updates/artemis-ii-splashdown-return/](https://www.cbsnews.com/live-updates/artemis-ii-splashdown-return/)

生成摘要时出错

---

## 25. France's government is ditching Windows for Linux, says US tech a strategic risk

**原文标题**: France's government is ditching Windows for Linux, says US tech a strategic risk

**原文链接**: [https://www.xda-developers.com/frances-government-ditching-windows-for-linux/](https://www.xda-developers.com/frances-government-ditching-windows-for-linux/)

生成摘要时出错

---

## 26. Bitcoin miners are losing on every coin produced as difficulty drops

**原文标题**: Bitcoin miners are losing on every coin produced as difficulty drops

**原文链接**: [https://www.coindesk.com/markets/2026/03/22/bitcoin-miners-are-losing-usd19-000-on-every-btc-produced-as-difficulty-drops-7-8](https://www.coindesk.com/markets/2026/03/22/bitcoin-miners-are-losing-usd19-000-on-every-btc-produced-as-difficulty-drops-7-8)

生成摘要时出错

---

## 27. The disturbing white paper Red Hat is trying to erase from the internet

**原文标题**: The disturbing white paper Red Hat is trying to erase from the internet

**原文链接**: [https://www.osnews.com/story/144776/the-disturbing-white-paper-red-hat-is-trying-to-erase-from-the-internet/](https://www.osnews.com/story/144776/the-disturbing-white-paper-red-hat-is-trying-to-erase-from-the-internet/)

生成摘要时出错

---

## 28. WireGuard makes new Windows release following Microsoft signing resolution

**原文标题**: WireGuard makes new Windows release following Microsoft signing resolution

**原文链接**: [https://lists.zx2c4.com/pipermail/wireguard/2026-April/009561.html](https://lists.zx2c4.com/pipermail/wireguard/2026-April/009561.html)

生成摘要时出错

---

## 29. Borges' cartographers and the tacit skill of reading LM output

**原文标题**: Borges' cartographers and the tacit skill of reading LM output

**原文链接**: [https://galsapir.github.io/sparse-thoughts/2026/04/11/map-and-territory/](https://galsapir.github.io/sparse-thoughts/2026/04/11/map-and-territory/)

生成摘要时出错

---

## 30. Industrial design files for Keychron keyboards and mice

**原文标题**: Industrial design files for Keychron keyboards and mice

**原文链接**: [https://github.com/Keychron/Keychron-Keyboards-Hardware-Design](https://github.com/Keychron/Keychron-Keyboards-Hardware-Design)

生成摘要时出错

---

## 31. The disturbing white paper Red Hat is trying to erase from the internet

**原文标题**: The disturbing white paper Red Hat is trying to erase from the internet

**原文链接**: [https://www.osnews.com/story/144776/the-disturbing-white-paper-red-hat-is-trying-to-erase-from-the-internet/](https://www.osnews.com/story/144776/the-disturbing-white-paper-red-hat-is-trying-to-erase-from-the-internet/)

生成摘要时出错

---

## 32. "AI polls" are fake polls

**原文标题**: "AI polls" are fake polls

**原文链接**: [https://www.natesilver.net/p/ai-polls-are-fake-polls](https://www.natesilver.net/p/ai-polls-are-fake-polls)

生成摘要时出错

---

## 33. CPU-Z and HWMonitor compromised

**原文标题**: CPU-Z and HWMonitor compromised

**原文链接**: [https://www.theregister.com/2026/04/10/cpuid_site_hijacked/](https://www.theregister.com/2026/04/10/cpuid_site_hijacked/)

生成摘要时出错

---

## 34. Can It Resolve Doom? Game Engine in 2k DNS Records

**原文标题**: Can It Resolve Doom? Game Engine in 2k DNS Records

**原文链接**: [https://blog.rice.is/post/doom-over-dns/](https://blog.rice.is/post/doom-over-dns/)

生成摘要时出错

---

## 35. Helium is hard to replace

**原文标题**: Helium is hard to replace

**原文链接**: [https://www.construction-physics.com/p/helium-is-hard-to-replace](https://www.construction-physics.com/p/helium-is-hard-to-replace)

生成摘要时出错

---

## 36. Bevy game development tutorials and in-depth resources

**原文标题**: Bevy game development tutorials and in-depth resources

**原文链接**: [https://taintedcoders.com/](https://taintedcoders.com/)

生成摘要时出错

---

## 37. JSON formatter Chrome plugin now closed and injecting adware

**原文标题**: JSON formatter Chrome plugin now closed and injecting adware

**原文链接**: [https://github.com/callumlocke/json-formatter](https://github.com/callumlocke/json-formatter)

生成摘要时出错

---

## 38. Polymarket gamblers betting millions on war

**原文标题**: Polymarket gamblers betting millions on war

**原文链接**: [https://www.theguardian.com/business/2026/apr/11/polymarket-gamblers-betting-iran-war-ukraine-news-truth](https://www.theguardian.com/business/2026/apr/11/polymarket-gamblers-betting-iran-war-ukraine-news-truth)

生成摘要时出错

---

## 39. Italo Calvino: A traveller in a world of uncertainty

**原文标题**: Italo Calvino: A traveller in a world of uncertainty

**原文链接**: [https://www.historytoday.com/archive/portrait-author-historian/italo-calvino-traveller-world-uncertainty](https://www.historytoday.com/archive/portrait-author-historian/italo-calvino-traveller-world-uncertainty)

生成摘要时出错

---

## 40. Show HN: Hormuz Havoc, a satirical game that got overrun by AI bots in 24 hours

**原文标题**: Show HN: Hormuz Havoc, a satirical game that got overrun by AI bots in 24 hours

**原文链接**: [https://www.hormuz-havoc.com/](https://www.hormuz-havoc.com/)

生成摘要时出错

---

## 41. Quien – A better WHOIS lookup tool

**原文标题**: Quien – A better WHOIS lookup tool

**原文链接**: [https://github.com/retlehs/quien/](https://github.com/retlehs/quien/)

生成摘要时出错

---

## 42. Sybilproof reputation mechanisms (2005) [pdf]

**原文标题**: Sybilproof reputation mechanisms (2005) [pdf]

**原文链接**: [https://dl.acm.org/doi/pdf/10.1145/1080192.1080202](https://dl.acm.org/doi/pdf/10.1145/1080192.1080202)

生成摘要时出错

---

## 43. Intel 486 CPU announced April 10, 1989

**原文标题**: Intel 486 CPU announced April 10, 1989

**原文链接**: [https://dfarq.homeip.net/intel-486-cpu-announced-april-10-1989/](https://dfarq.homeip.net/intel-486-cpu-announced-april-10-1989/)

生成摘要时出错

---

## 44. The Bra-and-Girdle Maker That Fashioned the Impossible for NASA

**原文标题**: The Bra-and-Girdle Maker That Fashioned the Impossible for NASA

**原文链接**: [https://thereader.mitpress.mit.edu/the-bra-and-girdle-maker-that-fashioned-the-impossible-for-nasa/](https://thereader.mitpress.mit.edu/the-bra-and-girdle-maker-that-fashioned-the-impossible-for-nasa/)

生成摘要时出错

---

## 45. A practical guide for setting up Zettelkasten method in Obsidian

**原文标题**: A practical guide for setting up Zettelkasten method in Obsidian

**原文链接**: [https://desktopcommander.app/blog/zettelkasten-obsidian/](https://desktopcommander.app/blog/zettelkasten-obsidian/)

生成摘要时出错

---

## 46. 20 years on AWS and never not my job

**原文标题**: 20 years on AWS and never not my job

**原文链接**: [https://www.daemonology.net/blog/2026-04-11-20-years-on-AWS-and-never-not-my-job.html](https://www.daemonology.net/blog/2026-04-11-20-years-on-AWS-and-never-not-my-job.html)

生成摘要时出错

---

## 47. Watgo – A WebAssembly Toolkit for Go

**原文标题**: Watgo – A WebAssembly Toolkit for Go

**原文链接**: [https://eli.thegreenplace.net/2026/watgo-a-webassembly-toolkit-for-go/](https://eli.thegreenplace.net/2026/watgo-a-webassembly-toolkit-for-go/)

生成摘要时出错

---

## 48. Launch HN: Twill.ai (YC S25) – Delegate to cloud agents, get back PRs

**原文标题**: Launch HN: Twill.ai (YC S25) – Delegate to cloud agents, get back PRs

**原文链接**: [https://twill.ai](https://twill.ai)

生成摘要时出错

---

## 49. OpenClaw’s memory is unreliable, and you don’t know when it will break

**原文标题**: OpenClaw’s memory is unreliable, and you don’t know when it will break

**原文链接**: [https://blog.nishantsoni.com/p/ive-seen-a-thousand-openclaw-deploys](https://blog.nishantsoni.com/p/ive-seen-a-thousand-openclaw-deploys)

生成摘要时出错

---

## 50. Investigating Split Locks on x86-64

**原文标题**: Investigating Split Locks on x86-64

**原文链接**: [https://chipsandcheese.com/p/investigating-split-locks-on-x86](https://chipsandcheese.com/p/investigating-split-locks-on-x86)

生成摘要时出错

---

## 51. A compelling title that is cryptic enough to get you to take action on it

**原文标题**: A compelling title that is cryptic enough to get you to take action on it

**原文链接**: [https://ericwbailey.website/published/a-compelling-title-that-is-cryptic-enough-to-get-you-to-take-action-on-it/](https://ericwbailey.website/published/a-compelling-title-that-is-cryptic-enough-to-get-you-to-take-action-on-it/)

生成摘要时出错

---

## 52. Don't Be Evil

**原文标题**: Don't Be Evil

**原文链接**: [https://pluralistic.net/2026/04/11/obvious-terrible-ideas/](https://pluralistic.net/2026/04/11/obvious-terrible-ideas/)

生成摘要时出错

---

## 53. Elizabeth Holmes is tweeting from jail. How? (2025)

**原文标题**: Elizabeth Holmes is tweeting from jail. How? (2025)

**原文链接**: [https://sfstandard.com/2025/09/02/elizabeth-holmes-bryan-johnson-prison-tweets/](https://sfstandard.com/2025/09/02/elizabeth-holmes-bryan-johnson-prison-tweets/)

生成摘要时出错

---

## 54. Clojure on Fennel Part One: Persistent Data Structures

**原文标题**: Clojure on Fennel Part One: Persistent Data Structures

**原文链接**: [https://andreyor.st/posts/2026-04-07-clojure-on-fennel-part-one-persistent-data-structures/](https://andreyor.st/posts/2026-04-07-clojure-on-fennel-part-one-persistent-data-structures/)

生成摘要时出错

---

## 55. Nowhere is safe

**原文标题**: Nowhere is safe

**原文链接**: [https://steveblank.com/2026/04/09/nowhere-is-safe/](https://steveblank.com/2026/04/09/nowhere-is-safe/)

生成摘要时出错

---

## 56. Meta is set to pay its top AI executives almost a billion each in bonuses

**原文标题**: Meta is set to pay its top AI executives almost a billion each in bonuses

**原文链接**: [https://www.msn.com/en-my/news/other/meta-is-set-to-pay-its-top-ai-executives-almost-a-billion-each-in-bonuses-if-they-hit-their-targets/ar-AA1ZszqA](https://www.msn.com/en-my/news/other/meta-is-set-to-pay-its-top-ai-executives-almost-a-billion-each-in-bonuses-if-they-hit-their-targets/ar-AA1ZszqA)

生成摘要时出错

---

## 57. Show HN: FluidCAD – Parametric CAD with JavaScript

**原文标题**: Show HN: FluidCAD – Parametric CAD with JavaScript

**原文链接**: [https://fluidcad.io/](https://fluidcad.io/)

生成摘要时出错

---

## 58. Now is the best time to write code by hand

**原文标题**: Now is the best time to write code by hand

**原文链接**: [https://sitebloom.ch/writing/now-is-the-best-time-to-write-code-by-hand/](https://sitebloom.ch/writing/now-is-the-best-time-to-write-code-by-hand/)

生成摘要时出错

---

## 59. Hungary Is a Laboratory for Illiberal Nationalism. The Results Are In

**原文标题**: Hungary Is a Laboratory for Illiberal Nationalism. The Results Are In

**原文链接**: [https://www.cato.org/commentary/hungary-laboratory-illiberal-nationalism-results-are](https://www.cato.org/commentary/hungary-laboratory-illiberal-nationalism-results-are)

生成摘要时出错

---

## 60. Hungary Is a Laboratory for Illiberal Nationalism. The Results Are In

**原文标题**: Hungary Is a Laboratory for Illiberal Nationalism. The Results Are In

**原文链接**: [https://www.cato.org/commentary/hungary-laboratory-illiberal-nationalism-results-are](https://www.cato.org/commentary/hungary-laboratory-illiberal-nationalism-results-are)

生成摘要时出错

---

## 61. You can't trust macOS Privacy and Security settings

**原文标题**: You can't trust macOS Privacy and Security settings

**原文链接**: [https://eclecticlight.co/2026/04/10/why-you-cant-trust-privacy-security/](https://eclecticlight.co/2026/04/10/why-you-cant-trust-privacy-security/)

生成摘要时出错

---

## 62. France to ditch Windows for Linux to reduce reliance on US tech

**原文标题**: France to ditch Windows for Linux to reduce reliance on US tech

**原文链接**: [https://techcrunch.com/2026/04/10/france-to-ditch-windows-for-linux-to-reduce-reliance-on-us-tech/](https://techcrunch.com/2026/04/10/france-to-ditch-windows-for-linux-to-reduce-reliance-on-us-tech/)

生成摘要时出错

---

## 63. Penguin 'Toxicologists' Find PFAS Chemicals in Remote Patagonia

**原文标题**: Penguin 'Toxicologists' Find PFAS Chemicals in Remote Patagonia

**原文链接**: [https://www.ucdavis.edu/health/news/penguin-toxicologists-find-pfas-chemicals-remote-patagonia](https://www.ucdavis.edu/health/news/penguin-toxicologists-find-pfas-chemicals-remote-patagonia)

生成摘要时出错

---

## 64. Code is run more than read (2023)

**原文标题**: Code is run more than read (2023)

**原文链接**: [https://olano.dev/blog/code-is-run-more-than-read/](https://olano.dev/blog/code-is-run-more-than-read/)

生成摘要时出错

---

## 65. Team from ETH Zurich make high quality quantum swap gate using a geometric phase

**原文标题**: Team from ETH Zurich make high quality quantum swap gate using a geometric phase

**原文链接**: [https://ethz.ch/en/news-and-events/eth-news/news/2026/04/a-new-trick-brings-stability-to-quantum-operations.html](https://ethz.ch/en/news-and-events/eth-news/news/2026/04/a-new-trick-brings-stability-to-quantum-operations.html)

生成摘要时出错

---

## 66. We've raised $17M to build what comes after Git

**原文标题**: We've raised $17M to build what comes after Git

**原文链接**: [https://blog.gitbutler.com/series-a](https://blog.gitbutler.com/series-a)

生成摘要时出错

---

## 67. Show HN: Eve – Managed OpenClaw for work

**原文标题**: Show HN: Eve – Managed OpenClaw for work

**原文链接**: [https://eve.new/login](https://eve.new/login)

生成摘要时出错

---

## 68. A New Way to Spray Paint Color

**原文标题**: A New Way to Spray Paint Color

**原文链接**: [https://spectrum.ieee.org/spray-paint-color-creator](https://spectrum.ieee.org/spray-paint-color-creator)

生成摘要时出错

---

## 69. 40x Faster Binary Search

**原文标题**: 40x Faster Binary Search

**原文链接**: [https://www.p99conf.io/session/40x-faster-binary-search/](https://www.p99conf.io/session/40x-faster-binary-search/)

生成摘要时出错

---

## 70. What is RISC-V and why it matters to Canonical

**原文标题**: What is RISC-V and why it matters to Canonical

**原文链接**: [https://ubuntu.com/blog/risc-v-101-what-is-it-and-what-does-it-mean-for-canonical](https://ubuntu.com/blog/risc-v-101-what-is-it-and-what-does-it-mean-for-canonical)

生成摘要时出错

---

## 71. PGLite Evangelism

**原文标题**: PGLite Evangelism

**原文链接**: [https://substack.com/home/post/p-193415720](https://substack.com/home/post/p-193415720)

生成摘要时出错

---

## 72. Show HN: A WYSIWYG word processor in Python

**原文标题**: Show HN: A WYSIWYG word processor in Python

**原文链接**: [https://codeberg.org/chrisecker/miniword](https://codeberg.org/chrisecker/miniword)

生成摘要时出错

---

## 73. FBI used iPhone notification data to retrieve deleted Signal messages

**原文标题**: FBI used iPhone notification data to retrieve deleted Signal messages

**原文链接**: [https://9to5mac.com/2026/04/09/fbi-used-iphone-notification-data-to-retrieve-deleted-signal-messages/](https://9to5mac.com/2026/04/09/fbi-used-iphone-notification-data-to-retrieve-deleted-signal-messages/)

生成摘要时出错

---

## 74. Mysteries of Dropbox: Testing of a Distributed Sync Service (2016) [pdf]

**原文标题**: Mysteries of Dropbox: Testing of a Distributed Sync Service (2016) [pdf]

**原文链接**: [https://www.cis.upenn.edu/~bcpierce/papers/mysteriesofdropbox.pdf](https://www.cis.upenn.edu/~bcpierce/papers/mysteriesofdropbox.pdf)

生成摘要时出错

---

## 75. Sam Altman's response to Molotov cocktail incident

**原文标题**: Sam Altman's response to Molotov cocktail incident

**原文链接**: [https://blog.samaltman.com/2279512](https://blog.samaltman.com/2279512)

生成摘要时出错

---

## 76. Vinyl Cache and Varnish Cache

**原文标题**: Vinyl Cache and Varnish Cache

**原文链接**: [https://vinyl-cache.org/organization/on_vinyl_cache_and_varnish_cache.html](https://vinyl-cache.org/organization/on_vinyl_cache_and_varnish_cache.html)

生成摘要时出错

---

## 77. Flashback to a time when government reports were works of art

**原文标题**: Flashback to a time when government reports were works of art

**原文链接**: [https://www.chicagotribune.com/2026/04/08/transportation-library-northwestern/](https://www.chicagotribune.com/2026/04/08/transportation-library-northwestern/)

生成摘要时出错

---

## 78. The difficulty of making sure your website is broken

**原文标题**: The difficulty of making sure your website is broken

**原文链接**: [https://letsencrypt.org/2026/04/10/test-sites.html](https://letsencrypt.org/2026/04/10/test-sites.html)

生成摘要时出错

---

## 79. Bringing Rust to the Pixel Baseband

**原文标题**: Bringing Rust to the Pixel Baseband

**原文链接**: [https://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html](https://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html)

生成摘要时出错

---

## 80. Raising Carthaginian Armies, Part I: Finding Carthaginians

**原文标题**: Raising Carthaginian Armies, Part I: Finding Carthaginians

**原文链接**: [https://acoup.blog/2026/04/10/collections-raising-carthaginian-armies-part-i-finding-carthaginians/](https://acoup.blog/2026/04/10/collections-raising-carthaginian-armies-part-i-finding-carthaginians/)

生成摘要时出错

---

## 81. How NASA built Artemis II’s fault-tolerant computer

**原文标题**: How NASA built Artemis II’s fault-tolerant computer

**原文链接**: [https://cacm.acm.org/news/how-nasa-built-artemis-iis-fault-tolerant-computer/](https://cacm.acm.org/news/how-nasa-built-artemis-iis-fault-tolerant-computer/)

生成摘要时出错

---

## 82. Molotov cocktail is hurled at home of Sam Altman

**原文标题**: Molotov cocktail is hurled at home of Sam Altman

**原文链接**: [https://www.nytimes.com/2026/04/10/us/open-ai-sam-altman-molotov-cocktail.html](https://www.nytimes.com/2026/04/10/us/open-ai-sam-altman-molotov-cocktail.html)

生成摘要时出错

---

## 83. Simulating a 2D Quadcopter from Scratch

**原文标题**: Simulating a 2D Quadcopter from Scratch

**原文链接**: [https://mrandri19.github.io/2026/04/03/2d-quadcopter-simulation.html](https://mrandri19.github.io/2026/04/03/2d-quadcopter-simulation.html)

生成摘要时出错

---

## 84. I ported Mac OS X to the Nintendo Wii

**原文标题**: I ported Mac OS X to the Nintendo Wii

**原文链接**: [https://bryankeller.github.io/2026/04/08/porting-mac-os-x-nintendo-wii.html](https://bryankeller.github.io/2026/04/08/porting-mac-os-x-nintendo-wii.html)

生成摘要时出错

---

## 85. LittleSnitch for Linux

**原文标题**: LittleSnitch for Linux

**原文链接**: [https://obdev.at/products/littlesnitch-linux/index.html](https://obdev.at/products/littlesnitch-linux/index.html)

生成摘要时出错

---

## 86. The best seat in town

**原文标题**: The best seat in town

**原文链接**: [https://www.torched.la/the-best-seat-in-town/](https://www.torched.la/the-best-seat-in-town/)

生成摘要时出错

---

## 87. Instant 1.0, a backend for AI-coded apps

**原文标题**: Instant 1.0, a backend for AI-coded apps

**原文链接**: [https://www.instantdb.com/essays/architecture](https://www.instantdb.com/essays/architecture)

生成摘要时出错

---

## 88. I still prefer MCP over skills

**原文标题**: I still prefer MCP over skills

**原文链接**: [https://david.coffee/i-still-prefer-mcp-over-skills/](https://david.coffee/i-still-prefer-mcp-over-skills/)

生成摘要时出错

---

## 89. Git commands I run before reading any code

**原文标题**: Git commands I run before reading any code

**原文链接**: [https://piechowski.io/post/git-commands-before-reading-code/](https://piechowski.io/post/git-commands-before-reading-code/)

生成摘要时出错

---

## 90. Native Instant Space Switching on macOS

**原文标题**: Native Instant Space Switching on macOS

**原文链接**: [https://arhan.sh/blog/native-instant-space-switching-on-macos/](https://arhan.sh/blog/native-instant-space-switching-on-macos/)

生成摘要时出错

---

## 91. Kagi Product Tips – Customize Your Search Results with URL Redirects

**原文标题**: Kagi Product Tips – Customize Your Search Results with URL Redirects

**原文链接**: [https://blog.kagi.com/tips/redirects](https://blog.kagi.com/tips/redirects)

生成摘要时出错

---

## 92. Show HN: Marimo pair – Reactive Python notebooks as environments for agents

**原文标题**: Show HN: Marimo pair – Reactive Python notebooks as environments for agents

**原文链接**: [https://github.com/marimo-team/marimo-pair](https://github.com/marimo-team/marimo-pair)

生成摘要时出错

---

## 93. Sam Altman may control our future – can he be trusted?

**原文标题**: Sam Altman may control our future – can he be trusted?

**原文链接**: [https://www.newyorker.com/magazine/2026/04/13/sam-altman-may-control-our-future-can-he-be-trusted](https://www.newyorker.com/magazine/2026/04/13/sam-altman-may-control-our-future-can-he-be-trusted)

生成摘要时出错

---

## 94. RSoC 2026: A new CPU scheduler for Redox OS

**原文标题**: RSoC 2026: A new CPU scheduler for Redox OS

**原文链接**: [https://www.redox-os.org/news/rsoc-dwrr/](https://www.redox-os.org/news/rsoc-dwrr/)

生成摘要时出错

---

## 95. Why do we tell ourselves scary stories about AI?

**原文标题**: Why do we tell ourselves scary stories about AI?

**原文链接**: [https://www.quantamagazine.org/why-do-we-tell-ourselves-scary-stories-about-ai-20260410/](https://www.quantamagazine.org/why-do-we-tell-ourselves-scary-stories-about-ai-20260410/)

生成摘要时出错

---

## 96. Researchers used AI to analyze 400k Reddit posts, revealing GLP-1 side effects

**原文标题**: Researchers used AI to analyze 400k Reddit posts, revealing GLP-1 side effects

**原文链接**: [https://www.seas.upenn.edu/stories/penn-researchers-use-ai-to-surface-unreported-glp-1-side-effects-in-reddit-posts/](https://www.seas.upenn.edu/stories/penn-researchers-use-ai-to-surface-unreported-glp-1-side-effects-in-reddit-posts/)

生成摘要时出错

---

## 97. We gave an AI a 3-year Lease. It opened a store

**原文标题**: We gave an AI a 3-year Lease. It opened a store

**原文链接**: [https://andonlabs.com/blog/andon-market-launch](https://andonlabs.com/blog/andon-market-launch)

生成摘要时出错

---

## 98. Bluesky April 2026 Outage Post-Mortem

**原文标题**: Bluesky April 2026 Outage Post-Mortem

**原文链接**: [https://pckt.blog/b/jcalabro/april-2026-outage-post-mortem-219ebg2](https://pckt.blog/b/jcalabro/april-2026-outage-post-mortem-219ebg2)

生成摘要时出错

---

## 99. A WebGPU implementation of Augmented Vertex Block Descent

**原文标题**: A WebGPU implementation of Augmented Vertex Block Descent

**原文链接**: [https://github.com/jure/webphysics](https://github.com/jure/webphysics)

生成摘要时出错

---

## 100. Hegel, a universal property-based testing protocol and family of PBT libraries

**原文标题**: Hegel, a universal property-based testing protocol and family of PBT libraries

**原文链接**: [https://hegel.dev](https://hegel.dev)

生成摘要时出错

---

