# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-11.md)

*最后自动更新时间: 2026-04-11 18:01:01*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 2 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 3 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 4 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 5 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 6 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 7 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 8 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 9 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 10 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 11 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 12 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 13 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 14 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 15 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 16 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 17 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 18 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 19 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 20 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 21 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 22 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 23 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 24 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 25 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 26 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 27 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 28 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 29 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 30 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 31 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 32 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 33 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 34 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 35 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 36 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 37 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 38 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 39 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 40 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 41 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 42 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 43 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 44 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 45 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 46 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 47 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 48 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 49 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 50 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 51 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 52 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 53 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 54 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 55 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 56 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 57 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 58 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 59 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 60 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 61 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 62 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 63 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 64 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 65 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 66 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 67 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 68 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 69 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 70 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 71 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 72 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 73 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 74 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 75 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 76 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 77 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 78 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 79 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 80 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 81 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 82 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 83 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 84 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 85 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 86 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 87 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 88 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 89 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 90 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 91 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 92 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 93 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 94 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 95 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 96 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 97 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 98 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 99 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 100 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 101 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 102 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 103 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 104 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 105 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 106 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 107 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 108 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 109 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 110 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 111 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 112 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 113 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 114 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 115 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 116 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 117 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 118 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 119 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 120 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 121 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 122 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 123 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 124 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 125 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 126 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 127 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 128 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 129 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 130 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 131 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 132 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 133 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 134 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 135 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 136 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 137 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 138 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 139 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 140 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 141 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 142 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 143 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 144 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 145 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 146 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 147 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 148 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 149 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 150 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 151 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 152 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 153 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 154 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 155 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 156 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 157 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 158 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 159 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 160 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 161 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 162 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 163 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 164 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 165 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 166 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 167 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 168 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 169 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 170 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 171 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 172 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 173 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 174 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 175 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 176 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 177 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 178 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 179 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 180 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 181 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 182 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 183 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 184 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 185 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 186 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 187 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 188 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 189 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 190 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 191 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 192 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 193 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 194 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 195 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 196 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 197 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 198 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 199 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 200 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 201 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 202 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 203 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 204 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 205 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 206 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 207 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 208 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 209 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 210 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 211 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 212 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 213 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 214 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 215 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 216 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 217 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 218 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 219 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 220 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 221 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 222 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 223 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 224 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 225 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 226 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 227 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 228 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 229 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 230 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 231 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 232 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 233 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 234 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 235 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 236 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 237 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 238 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 239 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 240 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 241 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 242 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 243 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 244 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 245 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 246 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 247 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 248 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 249 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 250 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 251 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 252 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 253 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 254 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 255 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 256 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 257 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 258 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 259 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 260 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 261 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 262 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 263 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 264 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 265 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 266 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 267 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 268 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 269 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 270 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 271 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 272 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 273 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 274 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 275 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 276 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 277 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 278 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 279 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 280 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 281 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 282 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 283 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 284 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 285 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 286 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 287 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 288 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 289 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 290 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 291 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 292 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 293 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 294 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 295 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 296 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 297 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 298 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 299 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 300 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 301 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 302 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 303 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 304 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 305 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 306 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 307 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 308 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 309 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 310 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 311 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 312 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 313 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 314 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 315 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 316 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 317 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 318 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 319 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 320 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 321 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 322 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 323 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 324 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 325 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 326 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 327 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 328 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 329 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 330 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 331 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 332 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 333 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 334 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 335 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 336 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 337 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 338 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 339 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 340 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 341 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 342 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 343 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 344 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 345 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 346 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 347 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 348 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 349 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 350 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 351 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 352 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 353 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 354 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 355 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 356 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 357 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 358 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 359 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 360 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 361 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 362 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 363 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 364 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 365 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 366 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 367 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 368 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 369 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 370 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 371 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 372 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 373 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 374 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 375 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 376 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 377 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 378 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 379 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 380 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 381 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 382 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 383 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 384 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 385 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 386 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 387 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
