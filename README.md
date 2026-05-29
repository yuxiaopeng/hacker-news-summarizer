# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-05-29.md)

*最后自动更新时间: 2026-05-29 20:01:06*
## 1. 实现持久化工作流，SQLite 就够了

**原文标题**: SQLite is all you need for durable workflows

**原文链接**: [https://obeli.sk/blog/sqlite-is-all-you-need-for-durable-workflows/](https://obeli.sk/blog/sqlite-is-all-you-need-for-durable-workflows/)

在博客文章《SQLite 是实现持久化工作流的全部所需》中，作者指出，现代工作流编排（通常由 Temporal 或 Cadence 等复杂的分布式系统处理）可以有效地利用 SQLite 进行管理。持久化工作流是必须在硬件或软件故障中保持存续的长期运行过程。虽然此类工作流传统上与沉重的基础设施相关联，但作者认为 SQLite 的 ACID 特性使其成为执行此任务的理想引擎。

文章介绍了 **Obelisk**，这是一个基于 SQLite 构建的持久化执行引擎。其核心思想是将 SQLite 作为集中的事件存储，用以追踪工作流的状态和历史。通过以事务方式记录过程中的每一步，系统可以在崩溃或重启后可靠地从上次中断的地方恢复。

**该方法的主要优势包括：**
*   **运维简单性：** 它取代了对外部数据库、消息队列和复杂网络管理的需求。
*   **性能：** 通过使用 SQLite 的预写日志（WAL）模式，系统实现了高吞吐量和低延迟，在许多用例中往往优于分布式替代方案。
*   **成本效益：** 在单台服务器或小型实例上运行可显著降低基础设施开销。

为了解决单点故障风险，作者建议利用 **Litestream** 或 **LiteFS** 等工具将数据实时复制到云存储或其他节点。

文章的核心论点是对“默认分布式”思维模式的批判。对于绝大多数企业而言，大规模分布式集群的可扩展性并非必需。相反，作者倡导使用“乏味”但稳健的技术，证明了 SQLite 能够为可靠的工作流执行提供必要的持久性和顺序，而无需承担沉重的运维“复杂度税”。

---

## 2. Mistral AI Now 巴黎峰会笔记

**原文标题**: Notes from the Mistral AI Now Summit in Paris

**原文链接**: [https://koenvangilst.nl/lab/mistral-ai-now-summit](https://koenvangilst.nl/lab/mistral-ai-now-summit)

在巴黎举行的 Mistral AI Now 峰会上，Mistral AI 宣布其已从模型开发商向**全栈 AI 提供商**转型，业务涵盖算力、平台及咨询服务。作为美国科技巨头的欧洲替代方案，Mistral 的核心优势在于**数据主权**、高效的开源模型，以及支持企业**本地部署** (on-premise) 运行 AI 的能力。

峰会核心要点包括：

*   **基础设施与独立性：** Mistral 正在法国和瑞典建立自有的数据中心。这一基础设施支持其“主权 AI”战略，使银行（如法巴银行、Abanca）等受监管行业能够在本地处理敏感数据。
*   **专业化小模型：** Mistral 并非盲目追求通用人工智能 (AGI)，而是优先开发快速且针对特定任务的模型。典型案例包括 **Document AI** (OCR)、**Voxtral**（为亚马逊 Alexa+ 提供的多语言语音模型）以及 **Robostral**（为 ASML 提供的工业机器人模型）。
*   **智能体 AI (Agentic AI)：** 公司推出了“智能体框架”(agentic harness) 的概念，旨在增强模型的上下文理解、推理和持久性。此外，他们还发布了面向企业的办公生产力工具 **Vibe for Work**。
*   **人文与伦理：** 在一个亮眼的案例中，奥地利科学院利用 **Codestral** 转录了 18 万份古代莎草纸碎片，这项任务若按传统方式完成将耗时数千年。

**结论：**
Mistral 的愿景是成为寻求实际投资回报的欧洲机构不可或缺的合作伙伴。通过专注于透明度、效率和本地控制，他们旨在结束欧洲市场对美国超大规模云厂商的盲目依赖，并提供一套稳健、企业级的 AI 技术栈。

---

## 3. 死亡经济理论

**原文标题**: The dead economy theory

**原文链接**: [https://www.owenmcgrann.com/p/the-dead-economy-theory](https://www.owenmcgrann.com/p/the-dead-economy-theory)

在《死亡经济理论》中，欧文·麦格雷恩（Owen McGrann）指出，人工智能公司目前高达数万亿美元的巨额估值，迫使它们必须从“辅助”劳动力转向系统性地“取代”劳动力。他断言，AI产业正将全球专业劳动力市场视为主要收入来源，从而形成了一种威胁资本主义根基的寄生式循环。

麦格雷恩概述了一个“三部曲”经济陷阱：
1. **自动化：** 企业用AI取代工人以提高利润率和股价。
2. **需求毁灭：** 被取代的工人失去购买力，导致消费需求萎缩。
3. **市场崩溃：** 推进自动化的企业最终会倒闭，因为其客户（即工人）再也买不起它们的产品。

这形成了一个“囚徒困境”：单个企业为了保持竞争力会理性地选择自动化，尽管其总体结果是集体的毁灭。麦格雷恩指出，与历史上农业或制造业的转型不同，AI是通用型的，且进化速度极快，使劳动力市场无法适应。他引用了诺贝尔奖得主达隆·阿西莫格鲁（Daron Acemoglu）关于“过度自动化”的警告，即AI被用于消灭工作岗位，却未能带来显著的生产力增长。

此外，麦格雷恩还指出了一场深刻的政治危机：民主依赖于一种契约，即被统治者提供劳动力和税收以换取制衡力。如果AI使人类劳动力变得多余，精英阶层将不再需要大众，从而切断了资本与人类贡献之间的联系。这促使科技领袖形成的“兄弟寡头政治”（broligarchy）更倾向于专制，而非被他们视为阻碍的民主监督。

最终，麦格雷恩驳斥了AI乐观主义者所承诺的“休闲经济”乌托邦。他提到了制造业空心化地区的“绝望之死”，并警告称，剥夺经济目标会导致社会崩溃。文章总结道，我们正在资助一场旨在消灭人类客户群的革命，这不仅威胁到经济，也威胁到民主治理。

---

## 4. Bijou64：一种变长整数编码

**原文标题**: Bijou64: A variable-length integer encoding

**原文链接**: [https://www.inkandswitch.com/tangents/bijou64/](https://www.inkandswitch.com/tangents/bijou64/)

**Bijou64** is a novel variable-length integer (varint) encoding developed for the Subduction CRDT protocol. It was designed to solve a critical security flaw in traditional encodings like LEB128: the lack of structural **canonicality**.

### The Problem
In standard encodings like LEB128, a single integer can be represented by multiple different byte sequences (e.g., by adding redundant "continuation" bytes). This ambiguity is a major vulnerability for signed data and content-addressed systems, as an attacker can alter the byte string without changing the decoded value, thereby breaking digital signatures.

### The Solution: Canonical by Construction
Bijou64 ensures that every integer has exactly one valid representation through two primary mechanisms:
1.  **First-Byte Tagging:** The first byte handles values 0–247 directly. Values 248–255 serve as tags indicating the number of following data bytes. This allows the decoder to know the payload length immediately (O(1)) rather than scanning for continuation bits (O(n)).
2.  **Tiered Offsets:** Each length "tier" is offset by the maximum value of the preceding tier. This mathematical approach prevents the redundancy found in LEB128, ensuring no overlap between representations.

### Performance Gains
Despite being designed for security, Bijou64 significantly outperforms LEB128. Benchmarks on ARM and x86 architectures show it decodes **2–10 times faster** than LEB128. This efficiency is due to:
*   **Predictable Branching:** CPUs can easily predict the fixed-length reads.
*   **Native Instructions:** It uses contiguous big-endian payloads, allowing compilers to utilize high-speed CPU `bswap` (byte-swap) instructions.
*   **Zero-Cost Validation:** Because the format is structurally canonical, no additional runtime checks are required to reject "overlong" encodings.

While the encoded size is comparable to LEB128, Bijou64 offers a safer, faster alternative for modern binary protocols, especially those requiring cryptographic signatures or high-performance data syncing. The library is currently available as a Rust crate.

---

## 5. On Rendering Diffs

**原文标题**: On Rendering Diffs

**原文链接**: [https://pierre.computer/writing/on-rendering-diffs](https://pierre.computer/writing/on-rendering-diffs)

生成摘要时出错

---

## 6. Rothko for your current weather conditions

**原文标题**: Rothko for your current weather conditions

**原文链接**: [https://rothko.joonas.wtf/](https://rothko.joonas.wtf/)

生成摘要时出错

---

## 7. It's hard to justify buying a Framework 12

**原文标题**: It's hard to justify buying a Framework 12

**原文链接**: [https://www.jeffgeerling.com/blog/2026/its-hard-to-justify-framework-12/](https://www.jeffgeerling.com/blog/2026/its-hard-to-justify-framework-12/)

生成摘要时出错

---

## 8. GTA 6 Developers Unionize

**原文标题**: GTA 6 Developers Unionize

**原文链接**: [https://rockstarintel.com/gta-6-developers-announce-rockstar-games-union/](https://rockstarintel.com/gta-6-developers-announce-rockstar-games-union/)

生成摘要时出错

---

## 9. Liquid AI reveals 8B-A1B MoE trained on 38T

**原文标题**: Liquid AI reveals 8B-A1B MoE trained on 38T

**原文链接**: [https://www.liquid.ai/blog/lfm2-5-8b-a1b](https://www.liquid.ai/blog/lfm2-5-8b-a1b)

生成摘要时出错

---

## 10. CAPTCHAs can still detect AI agents

**原文标题**: CAPTCHAs can still detect AI agents

**原文链接**: [https://research.roundtable.ai/captchas-detect-ai/](https://research.roundtable.ai/captchas-detect-ai/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 2 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 3 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 4 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 5 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 6 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 7 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 8 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 9 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 10 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 11 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 12 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 13 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 14 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 15 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 16 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 17 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 18 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 19 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 20 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 21 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 22 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 23 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 24 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 25 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 26 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 27 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 28 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 29 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 30 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 31 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 32 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 33 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 34 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 35 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 36 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 37 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 38 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 39 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 40 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 41 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 42 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 43 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 44 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 45 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 46 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 47 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 48 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 49 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 50 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 51 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 52 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 53 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 54 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 55 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 56 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 57 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 58 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 59 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 60 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 61 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 62 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 63 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 64 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 65 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 66 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 67 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 68 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 69 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 70 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 71 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 72 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 73 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 74 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 75 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 76 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 77 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 78 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 79 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 80 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 81 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 82 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 83 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 84 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 85 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 86 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 87 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 88 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 89 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 90 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 91 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 92 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 93 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 94 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 95 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 96 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 97 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 98 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 99 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 100 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 101 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 102 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 103 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 104 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 105 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 106 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 107 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 108 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 109 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 110 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 111 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 112 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 113 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 114 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 115 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 116 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 117 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 118 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 119 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 120 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 121 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 122 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 123 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 124 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 125 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 126 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 127 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 128 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 129 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 130 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 131 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 132 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 133 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 134 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 135 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 136 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 137 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 138 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 139 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 140 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 141 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 142 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 143 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 144 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 145 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 146 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 147 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 148 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 149 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 150 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 151 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 152 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 153 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 154 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 155 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 156 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 157 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 158 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 159 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 160 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 161 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 162 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 163 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 164 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 165 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 166 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 167 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 168 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 169 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 170 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 171 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 172 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 173 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 174 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 175 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 176 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 177 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 178 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 179 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 180 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 181 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 182 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 183 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 184 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 185 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 186 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 187 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 188 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 189 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 190 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 191 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 192 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 193 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 194 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 195 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 196 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 197 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 198 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 199 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 200 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 201 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 202 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 203 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 204 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 205 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 206 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 207 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 208 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 209 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 210 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 211 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 212 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 213 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 214 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 215 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 216 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 217 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 218 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 219 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 220 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 221 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 222 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 223 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 224 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 225 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 226 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 227 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 228 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 229 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 230 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 231 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 232 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 233 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 234 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 235 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 236 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 237 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 238 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 239 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 240 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 241 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 242 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 243 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 244 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 245 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 246 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 247 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 248 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 249 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 250 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 251 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 252 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 253 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 254 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 255 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 256 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 257 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 258 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 259 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 260 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 261 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 262 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 263 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 264 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 265 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 266 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 267 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 268 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 269 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 270 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 271 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 272 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 273 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 274 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 275 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 276 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 277 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 278 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 279 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 280 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 281 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 282 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 283 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 284 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 285 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 286 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 287 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 288 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 289 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 290 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 291 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 292 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 293 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 294 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 295 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 296 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 297 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 298 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 299 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 300 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 301 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 302 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 303 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 304 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 305 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 306 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 307 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 308 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 309 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 310 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 311 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 312 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 313 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 314 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 315 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 316 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 317 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 318 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 319 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 320 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 321 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 322 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 323 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 324 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 325 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 326 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 327 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 328 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 329 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 330 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 331 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 332 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 333 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 334 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 335 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 336 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 337 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 338 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 339 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 340 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 341 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 342 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 343 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 344 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 345 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 346 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 347 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 348 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 349 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 350 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 351 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 352 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 353 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 354 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 355 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 356 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 357 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 358 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 359 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 360 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 361 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 362 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 363 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 364 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 365 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 366 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 367 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 368 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 369 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 370 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 371 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 372 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 373 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 374 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 375 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 376 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 377 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 378 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 379 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 380 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 381 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 382 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 383 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 384 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 385 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 386 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 387 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 388 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 389 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 390 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 391 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 392 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 393 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 394 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 395 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 396 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 397 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 398 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 399 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 400 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 401 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 402 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 403 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 404 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 405 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 406 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 407 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 408 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 409 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 410 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 411 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 412 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 413 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 414 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 415 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 416 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 417 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 418 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 419 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 420 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 421 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 422 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 423 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 424 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 425 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 426 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 427 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 428 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 429 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 430 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 431 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 432 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 433 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 434 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 435 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
