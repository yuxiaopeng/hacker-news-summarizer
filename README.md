# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-10-14.md)

*最后自动更新时间: 2026-10-14 20:58:29*
## 1. 2026年癌症患病须知

**原文标题**: Things to know if you get cancer in 2026

**原文链接**: [https://jjmaxwell4.com/writing/things-to-know-when-you-get-cancer/](https://jjmaxwell4.com/writing/things-to-know-when-you-get-cancer/)

基于作者2026年的口腔癌确诊经历，作者强调，患者必须成为自己最坚定的捍卫者，才能在医疗体系中高效周旋。核心要点包括：

*   **坚持预约：** 不要被动接受漫长的等待。频繁致电诊室询问是否有预约取消，这往往能让就诊时间提前数周。
*   **主动检测与寻求多方意见：** 尽早要求进行全面的基因检测，并确保在初次活检时完成。始终去顶级癌症中心寻求“第二诊疗意见”和第二次病理评估，即便需要奔波也在所不惜。
*   **善用资源：** 参考NCCN指南研究“标准治疗方案”，以掌握治疗流程。咨询Sijbrandij基金会以获取更多指导及面诊提问清单。
*   **策略性使用人工智能：** 虽然AI在记录诊疗过程、总结笔记和生成随访问题方面很有帮助，但作者警告，AI模型最初可能会淡化症状的严重性。
*   **术前尽职调查：** 在手术前，询问主刀医生的具体经验和并发症发生率。最重要的是，与既往患者交流，真实了解手术对身体的损耗及康复过程。

核心思想是：由于没有人比患者本人更在乎治疗结果，因此必须全面掌控诊疗进程，保持详尽记录，绝不要指望医疗系统会自动高效或全面地运作。

---

## 2. Go 1.27 中更好的 HTTP/1 连接复用

**原文标题**: Better HTTP/1 connection reuse in Go 1.27

**原文链接**: [https://go.dev/blog/http-connection-reuse](https://go.dev/blog/http-connection-reuse)

在 Go 1.27 中，`net/http` 包针对 HTTP/1.x 连接复用引入了重大的性能优化，在某些请求模式下，速度提升可达五倍。

**问题所在**
在 HTTP/1.x 中，连接是顺序执行的。为了复用连接，客户端必须在开始下一个请求之前准确读到当前响应体的末尾。在 Go 1.27 之前，如果开发人员在未读完整个响应的情况下调用 `resp.Body.Close()`——哪怕只剩一个字节——Go 也会丢弃该连接并开启一个新连接。这导致应用程序在后续的每个请求中都必须承担由新的 TCP 和 TLS 握手带来的高延迟成本（通常需要 3 次以上的往返时间）。

**手动规避方案**
为了避免这种“隐性”的性能退化，开发人员以前必须编写复杂的样板代码，通过特定的超时和字节限制手动“耗尽”（drain）响应体（将其读入 `io.Discard`）。这种方式非常繁琐且容易出错，例如在 HTTP/2 连接上进行不必要的耗尽操作（而多路复用技术使之并无必要）。

**Go 1.27 的解决方案**
Go 1.27 在 `net/http.Transport` 中实现了这一过程的自动化。当响应体被提前关闭时，标准库现在会在后台异步耗尽剩余内容，耗时上限为 50 毫秒，大小上限为 256 KB。如果服务器指定了 `Connection: close`，它还会智能地跳过此过程。

**结论**
开发人员不再需要为了保持高性能而编写复杂的耗尽逻辑。只需简单地使用 `defer resp.Body.Close()`，Go 1.27 就能确保在可行时自动复用连接，在保持代码简洁的同时显著降低网络延迟。

---

## 3. 波兰发生疑似破坏活动后，保加利亚星链站点起火

**原文标题**: Fire at Starlink site in Bulgaria after suspected sabotage in Poland

**原文链接**: [https://dpa-international.com/politics/urn:newsml:dpa.com:20090101:261014-930-839530/](https://dpa-international.com/politics/urn:newsml:dpa.com:20090101:261014-930-839530/)

保加利亚总理鲁门·拉德夫证实，索非亚附近的一处“星链”卫星互联网设施遭到疑似蓄意破坏。这起火灾发生于2026年10月9日，导致该站点的17个天线中有11个被毁。鉴于“星链”网络是乌克兰抵御俄罗斯入侵的关键防务组成部分，当局正将此事件作为战略安全事项处理。

周一，两名年龄分别为20岁和21岁的嫌疑人在保加利亚被拘留。两人均持有德国护照，据报道是从希腊入境。调查人员正在探究这两人与一个更大规模破坏网络之间的潜在联系，并特别提到9月23日在波兰华沙以南发生的一起类似的“星链”地面终端袭击事件。与波兰事件有关的另外两名嫌疑人近期已在德国尼尔廷根被捕。

尽管索非亚的设施属于私有，但保加利亚内政部长伊万·德梅吉耶夫宣布，已加强全国范围内类似设施的安保措施。保加利亚国家安全局（DANS）局长普拉门·通切夫正式将此次火灾定性为蓄意破坏，并警告称仍存在进一步袭击的可能性。

此事具有重大的地缘政治影响：保加利亚的亲西方反对党和波兰政府均暗示，俄罗斯情报部门可能在策划这些袭击，旨在破坏支持乌克兰的通信基础设施。

---

## 4. Phloem：像黏菌一样生长的 Git 历史

**原文标题**: Phloem: Git history grown like a slime mold

**原文链接**: [https://phloem.stemdeck.app/](https://phloem.stemdeck.app/)

**Phloem** 是一款基于 Web 的可视化工具，它将 Git 历史渲染为一种类似于**黏菌**生长过程的动态有机结构。

该项目采用 **WebGL 和 JavaScript** 开发，旨在将版本控制数据转化为流畅且具有生物启发感的动画。通过模拟自然生物的分支与扩张模式，Phloem 为代码库随时间的演进与互联提供了一个充满艺术感且非传统的独特视角。

---

## 5. Neckbeard —— 适用于您代理的 DevOps/平台/SRE 插件

**原文标题**: Neckbeard – a DevOps/platform/SRE plugin for your agent

**原文链接**: [https://github.com/bealesh/neckbeard](https://github.com/bealesh/neckbeard)

**Neckbeard** is a DevOps and SRE plugin designed for coding agents (such as Claude Code and Cursor) that automates the transition from application code to reviewable cloud infrastructure. It addresses a common flaw in AI agents—the tendency to "hallucinate" broken or insecure Infrastructure-as-Code (IaC)—by using a deterministic core of tested OpenTofu modules rather than letting the agent "freehand" configurations.

**Key Functionality:**
The tool operates through a series of slash commands:
*   **`/analyze`**: Scans the repository to create an evidence-backed app profile and identifies infrastructure needs.
*   **`/estimate`**: Generates detailed monthly cost projections via Infracost, comparing different clouds (AWS, GCP, Azure) and runtimes (Serverless vs. Kubernetes).
*   **`/sync`**: Scaffolds the infrastructure, validates it, and sets up CI/CD pipelines (GitHub Actions or GitLab CI) without overwriting manual edits.

**Core Features:**
*   **Security First:** It enforces OIDC federation to eliminate static cloud keys and utilizes "private-by-default" networking. Any security policy skips (via Checkov) require an explicit, written reason.
*   **Transparency:** Neckbeard categorizes validation into three tiers (V0–V2), distinguishing between static checks and live deployment proofs. It prioritizes "honesty as architecture," explicitly naming unpriced resources or unsupported workload requirements.
*   **Human-in-the-Loop:** While the agent analyzes and parameterizes, the final deployment remains a human-controlled process guided by a generated bootstrap runbook.

**Status:**
Currently in **pre-alpha**, Neckbeard is highly effective at the "onboarding half" of the lifecycle—generating validated scaffolds, pipelines, and cost estimates. While live deployment features for some providers are implemented, they remain experimental. The project is open-source under the Apache-2.0 license.

---

## 6. Iosevka is an open-source, sans-serif and slab-serif monospace font

**原文标题**: Iosevka is an open-source, sans-serif and slab-serif monospace font

**原文链接**: [https://typeof.net/Iosevka/](https://typeof.net/Iosevka/)

生成摘要时出错

---

## 7. Show HN: Petal, open-source CoScreen/ScreenHero finally free

**原文标题**: Show HN: Petal, open-source CoScreen/ScreenHero finally free

**原文链接**: [https://petal.live/](https://petal.live/)

生成摘要时出错

---

## 8. Banks are now trying to offload the AI data center debt they just underwrote

**原文标题**: Banks are now trying to offload the AI data center debt they just underwrote

**原文链接**: [https://startupfortune.com/banks-are-now-trying-to-offload-the-ai-data-center-debt-they-just-underwrote/](https://startupfortune.com/banks-are-now-trying-to-offload-the-ai-data-center-debt-they-just-underwrote/)

生成摘要时出错

---

## 9. Submarine cable resilience

**原文标题**: Submarine cable resilience

**原文链接**: [https://blog.apnic.net/2026/10/14/submarine-cable-resilience/](https://blog.apnic.net/2026/10/14/submarine-cable-resilience/)

生成摘要时出错

---

## 10. Suicide rates highest ever among middle-aged men

**原文标题**: Suicide rates highest ever among middle-aged men

**原文链接**: [https://www.telegraph.co.uk/news/2026/10/13/suicide-rates-highest-ever-among-middle-aged-men/](https://www.telegraph.co.uk/news/2026/10/13/suicide-rates-highest-ever-among-middle-aged-men/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 2 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 3 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 4 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 5 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 6 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 7 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 8 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 9 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 10 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 11 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 12 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 13 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 14 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 15 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 16 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 17 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 18 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 19 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 20 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 21 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 22 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 23 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 24 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 25 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 26 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 27 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 28 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 29 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 30 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 31 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 32 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 33 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 34 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 35 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 36 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 37 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 38 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 39 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 40 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 41 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 42 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 43 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 44 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 45 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 46 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 47 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 48 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 49 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 50 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 51 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 52 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 53 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 54 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 55 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 56 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 57 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 58 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 59 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 60 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 61 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 62 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 63 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 64 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 65 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 66 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 67 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 68 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 69 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 70 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 71 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 72 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 73 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 74 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 75 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 76 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 77 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 78 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 79 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 80 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 81 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 82 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 83 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 84 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 85 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 86 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 87 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 88 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 89 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 90 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 91 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 92 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 93 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 94 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 95 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 96 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 97 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 98 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 99 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 100 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 101 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 102 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 103 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 104 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 105 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 106 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 107 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 108 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 109 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 110 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 111 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 112 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 113 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 114 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 115 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 116 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 117 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 118 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 119 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 120 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 121 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 122 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 123 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 124 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 125 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 126 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 127 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 128 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 129 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 130 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 131 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 132 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 133 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 134 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 135 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 136 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 137 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 138 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 139 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 140 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 141 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 142 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 143 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 144 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 145 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 146 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 147 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 148 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 149 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 150 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 151 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 152 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 153 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 154 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 155 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 156 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 157 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 158 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 159 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 160 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 161 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 162 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 163 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 164 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 165 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 166 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 167 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 168 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 169 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 170 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 171 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 172 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 173 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 174 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 175 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 176 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 177 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 178 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 179 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 180 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 181 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 182 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 183 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 184 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 185 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 186 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 187 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 188 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 189 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 190 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 191 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 192 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 193 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 194 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 195 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 196 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 197 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 198 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 199 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 200 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 201 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 202 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 203 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 204 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 205 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 206 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 207 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 208 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 209 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 210 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 211 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 212 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 213 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 214 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 215 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 216 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 217 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 218 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 219 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 220 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 221 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 222 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 223 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 224 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 225 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 226 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 227 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 228 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 229 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 230 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 231 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 232 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 233 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 234 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 235 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 236 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 237 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 238 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 239 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 240 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 241 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 242 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 243 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 244 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 245 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 246 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 247 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 248 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 249 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 250 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 251 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 252 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 253 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 254 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 255 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 256 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 257 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 258 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 259 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 260 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 261 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 262 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 263 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 264 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 265 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 266 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 267 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 268 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 269 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 270 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 271 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 272 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 273 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 274 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 275 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 276 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 277 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 278 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 279 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 280 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 281 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 282 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 283 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 284 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 285 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 286 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 287 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 288 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 289 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 290 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 291 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 292 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 293 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 294 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 295 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 296 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 297 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 298 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 299 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 300 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 301 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 302 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 303 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 304 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 305 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 306 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 307 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 308 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 309 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 310 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 311 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 312 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 313 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 314 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 315 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 316 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 317 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 318 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 319 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 320 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 321 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 322 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 323 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 324 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 325 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 326 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 327 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 328 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 329 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 330 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 331 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 332 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 333 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 334 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 335 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 336 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 337 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 338 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 339 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 340 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 341 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 342 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 343 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 344 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 345 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 346 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 347 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 348 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 349 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 350 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 351 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 352 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 353 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 354 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 355 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 356 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 357 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 358 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 359 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 360 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 361 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 362 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 363 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 364 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 365 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 366 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 367 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 368 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 369 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 370 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 371 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 372 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 373 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 374 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 375 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 376 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 377 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 378 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 379 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 380 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 381 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 382 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 383 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 384 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 385 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 386 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 387 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 388 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 389 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 390 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 391 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 392 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 393 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 394 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 395 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 396 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 397 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 398 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 399 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 400 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 401 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 402 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 403 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 404 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 405 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 406 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 407 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 408 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 409 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 410 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 411 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 412 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 413 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 414 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 415 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 416 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 417 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 418 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 419 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 420 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 421 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 422 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 423 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 424 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 425 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 426 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 427 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 428 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 429 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 430 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 431 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 432 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 433 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 434 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 435 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 436 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 437 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 438 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 439 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 440 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 441 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 442 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 443 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 444 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 445 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 446 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 447 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 448 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 449 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 450 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 451 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 452 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 453 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 454 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 455 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 456 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 457 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 458 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 459 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 460 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 461 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 462 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 463 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 464 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 465 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 466 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 467 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 468 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 469 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 470 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 471 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 472 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 473 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 474 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 475 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 476 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 477 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 478 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 479 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 480 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 481 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 482 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 483 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 484 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 485 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 486 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 487 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 488 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 489 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 490 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 491 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 492 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 493 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 494 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 495 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 496 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 497 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 498 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 499 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 500 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 501 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 502 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 503 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 504 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 505 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 506 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 507 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 508 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 509 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 510 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 511 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 512 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 513 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 514 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 515 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 516 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 517 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 518 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 519 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 520 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 521 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 522 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 523 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 524 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 525 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 526 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 527 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 528 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 529 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 530 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 531 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 532 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 533 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 534 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 535 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 536 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 537 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 538 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 539 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 540 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 541 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 542 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 543 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 544 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 545 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 546 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 547 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 548 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 549 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 550 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 551 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 552 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 553 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 554 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 555 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 556 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 557 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 558 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 559 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 560 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 561 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 562 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 563 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 564 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 565 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 566 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 567 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 568 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 569 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 570 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 571 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
