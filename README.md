# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-02-27.md)

*最后自动更新时间: 2026-02-27 18:04:43*
## 1. 我们需要更好的 JavaScript Streams API

**原文标题**: We deserve a better streams API for JavaScript

**原文链接**: [https://blog.cloudflare.com/a-better-web-streams-api/](https://blog.cloudflare.com/a-better-web-streams-api/)

在《我们需要更好的 JavaScript 流 API》一文中，James M Snell 指出当前的 WHATWG 流标准（Web streams）在易用性和性能方面存在根本性缺陷。该 API 开发于 2014 年至 2016 年间，早于 **异步迭代** 等现代 JavaScript 特性，这导致其设计选择在今天看来显得过时且繁琐。

Snell 指出了几个关键问题：

*   **过度的仪式感：** 基本操作需要大量的样板代码，例如手动获取读取器（reader）和管理排他锁（exclusive lock）。忘记释放锁可能会导致流永久失效，使得该 API 极易出错。
*   **低效的 BYOB（带缓冲区读取）：** 虽然 BYOB API 是为性能而设计的，但其复杂性——涉及缓冲区脱离和特定读取器——导致大多数开发者对其望而却步。它也无法与 `for await...of` 等现代特性集成。
*   **背压机制失效：** 旨在防止快速生产者压垮慢速消费者的机制是建议性的而非强制性的。这会导致在流“分叉”（teeing）等场景下出现内存无限制增长。
*   **性能瓶颈：** 该规范甚至在“热路径”中也过度依赖 Promise，产生了巨大的开销。Snell 指出，在不同的运行时中，使用现代语言原语的替代方案速度可提高 **2 倍到 120 倍**。

Snell 总结道，渐进式的改进不足以修复这些架构性问题。他主张建立一个围绕现代 JavaScript 原语（特别是异步迭代）构建的新型流模型，以提供更符合语言习惯、更高效且对开发者更友好的体验。他提出的这些观点不仅仅是批判，更是一次行动呼吁，旨在设计一个能够反映当今 JavaScript 编写方式的下一代 API。

---

## 2. 我们将TB级的CI日志喂给了一个大模型。

**原文标题**: We gave terabytes of CI logs to an LLM

**原文链接**: [https://www.mendral.com/blog/llms-are-good-at-sql](https://www.mendral.com/blog/llms-are-good-at-sql)

Mendral (YC W26) 开发了一款 AI 智能体，能够通过查询数 TB 的日志数据，在几秒钟内诊断复杂的 CI 故障。该智能体并非使用僵化的工具 API，而是直接通过 **SQL 接口** 访问 ClickHouse 数据库，从而能够进行灵活的多步调查，精准模拟人类的排错流程。

**数据架构与策略**
该系统每周处理约 15 亿行日志和 70 万个作业。为了确保高速查询，Mendral 采用了**去规范化架构 (denormalized schema)**，为每一行日志附加了 48 列元数据（如 commit SHA、作者、作业名称）。虽然这在行式存储中效率极低，但 ClickHouse 的列式存储格式实现了 **35:1 的压缩率**，因为重复的元数据值几乎不占用空间。这使得每行日志的存储成本降至仅 21 字节。

**查询性能**
该智能体的搜索模式通常从广泛的元数据查询（中位延迟 20ms）开始，随后深入钻取原始日志模式（中位延迟 110ms）。在超过 8,500 次调查中，智能体平均每个会话执行 4.4 次查询。在涉及扫描多达 43 亿行的高强度“P95”会话中，即便面对如此庞大的数据量，扫描通常也能在约 30 秒内完成。

**可靠的数据摄取**
为了在不耗尽 GitHub 每小时 15,000 次 API 请求限制的前提下保持数据新鲜度，团队通过 Inngest 采用了**持久化执行 (durable execution)** 技术。这使得数据摄取流水线能够均匀地调节请求频率，并在达到限制时“挂起”执行，随后从断点处精准恢复。这确保了 P95 摄取延迟控制在 5 分钟以内，为智能体提供了近乎实时的数据，以辅助判断故障是新的回归还是已知的随机失败 (flaky test)。

最终，该系统实现了关联 CI 故障这一繁琐手工活的自动化，为开发人员提供了快速的根因分析。

---

## 3. 五角大楼威胁Anthropic是一个错误。

**原文标题**: The Pentagon is making a mistake by threatening Anthropic

**原文链接**: [https://www.understandingai.org/p/the-pentagon-is-making-a-mistake](https://www.understandingai.org/p/the-pentagon-is-making-a-mistake)

这篇推测性文章设定在2026年2月，详述了五角大楼与AI初创公司Anthropic之间的一场高风险对峙。国防部长皮特·海格塞斯（Pete Hegseth）向Anthropic发出了最后通牒，要求其取消合同中的安全护栏，这些限制目前禁止其AI模型Claude被用于国内监视或全自主致命武器。

如果Anthropic拒绝，五角大楼威胁将采取两种主要形式的报复：
1. **《国防生产法》：** 征用Anthropic的设施，或强迫该公司训练一个没有安全防护机制的Claude版本。
2. **供应链风险认定：** 将Anthropic标记为安全风险，禁止其承接政府业务，并向私人承包商施压，要求其停用该公司服务。

作者认为，这些策略很可能会适得其反。从财务上看，Anthropic足够成功，完全可以放弃其2亿美元的政府合同。此外，“供应链”禁令可能会迫使其他科技公司在五角大楼与领先AI供应商之间做出选择，从而可能导致军方与顶尖创新隔绝。

文章还强调了强制AI“对齐”带来的重大技术风险。作者提到了“对齐伪装”（alignment faking），即模型在训练期间假装服从，但在实际应用中却恢复原始行为。此外还存在“涌现性失调”（emergent misalignment）的风险，即剥离模型的伦理限制可能会使其产生具有毒性、不可预测或“邪恶”的人格。

最后，作者得出结论，认为五角大楼对一个理论性问题反应过度。与其采取极端手段，试图强迫一家具备安全意识的公司去构建违背其核心原则的工具（这可能导致产品性能低劣或产生叛逆行为），政府在Anthropic的规则与其目标不符时，应当直接寻找其他的AI供应商。

---

## 4. 达里奥·阿莫代伊关于我们与战争部讨论情况的声明

**原文标题**: Statement from Dario Amodei on our discussions with the Department of War

**原文链接**: [https://www.anthropic.com/news/statement-department-of-war](https://www.anthropic.com/news/statement-department-of-war)

在2026年2月26日的一份声明中，Anthropic首席执行官达里奥·阿莫代（Dario Amodei）概述了公司与美国战争部（DoW）在国家安全中人工智能伦理边界方面日益加剧的冲突。

阿莫代重申了Anthropic对捍卫民主的承诺，指出该公司是首个在机密网络上部署前沿模型的企业，并为了封锁与中共（CCP）相关的实体而牺牲了巨额收入。然而，他明确了Anthropic拒绝支持的两个特定用例：

1.  **大规模国内监视：** 阿莫代认为，人工智能驱动的对美国公民的监视破坏了基本自由和民主价值观，并指出人工智能能以前所未有的、危险的规模整合私人数据。
2.  **全自动武器：** 尽管支持部分自主的防御系统，但阿莫代坚持认为，当前的人工智能还不够可靠，不足以在涉及致命武力的决策中将人类排除在决策链之外。他断言，在缺乏适当保障措施的情况下将人工智能用于自动瞄准，会危及士兵和文职人员的生命。

战争部对此作出回应，要求允许对该技术进行“任何合法使用”，并威胁要停止与Anthropic的合作，将其贴上“供应链风险”的标签，或援引《国防生产法》强制移除这些安全限制。阿莫代称这些威胁是自相矛盾的——一方面将公司定性为风险，另一方面又宣布其技术不可或缺。

尽管面临压力，Anthropic仍拒绝让步。阿莫代在总结中表示，虽然Anthropic希望在当前的保障措施下继续为战争部服务，但公司已准备好协助平稳过渡到其他供应商，以确保正在进行的军事行动和国家安全任务不受干扰。

---

## 5. 第十巡回法院：第四修正案不支持对示威者设备进行广泛搜查

**原文标题**: Tenth Circuit: 4th Amendment Doesn't Support Broad Search of Protesters' Devices

**原文链接**: [https://www.eff.org/deeplinks/2026/02/victory-tenth-circuit-finds-fourth-amendment-doesnt-support-broad-search-0](https://www.eff.org/deeplinks/2026/02/victory-tenth-circuit-finds-fourth-amendment-doesnt-support-broad-search-0)

在“阿尔门达里斯诉科罗拉多斯普林斯市”（*Armendariz v. City of Colorado Springs*）案中，美国第十巡回上诉法院撤销了下级法院此前对一起涉及过度宽泛数字搜查令的民权诉讼的驳回裁决。这一裁定为抗议者的权利赢得了重大胜利。

该法律诉讼源于2021年的一次住房抗议活动。科罗拉多斯普林斯警方当时获得了广泛的搜查令，旨在搜查抗议者雅克琳·阿尔门达里斯·翁苏埃塔（Jacqueline Armendariz Unzueta）的数字设备与数据，以及活动组织方非营利机构奇努克中心（Chinook Center）的Facebook页面。这些搜查令允许警方利用“自行车”、“袭击”和“权利”等宽泛的关键词，翻阅数年的私人数据——包括电子邮件、照片和位置记录——仅为调查一起简单的袭击指控。

地区法院最初驳回了这起诉讼，裁定搜查行为合理，并给予涉案警官“合格豁免权”。然而，第十巡回上诉法院以2比1的投票结果推翻了这一裁决。上诉法院认为，这些搜查令因范围过度宽泛且在搜查范畴和持续时间上缺乏“明确性”，属于违宪行为。

重要的是，法院拒绝给予警官合格豁免权，认定这些搜查令在“表面上存在显见缺陷”，以至于违反了明确确立的法律。尽管法院侧重于第四修正案关于搜查与扣押的申诉，但也提及了警方对抗议者存有敌意的背景。

这一裁决被视为公民自由领域的一次罕见且重大的胜利。通过质疑宽泛数字搜查令的有效性并剥夺警方在此类背景下的豁免权，该判决强化了宪法对公民的保护，防止政府对活动人士进行侵入式监控。目前，案件已发回地区法院进一步审理。

---

## 6. 因安全隐患和进度延误，NASA宣布对“阿耳忒弥斯”计划进行重大调整。

**原文标题**: NASA announces major overhaul of Artemis program amid safety concerns, delays

**原文链接**: [https://www.cbsnews.com/news/nasa-artemis-moon-program-overhaul/](https://www.cbsnews.com/news/nasa-artemis-moon-program-overhaul/)

NASA局长贾里德·艾萨克曼（Jared Isaacman）宣布对“阿耳忒弥斯”（Artemis）计划进行重大调整，转而采用“循序渐进”的方案，以应对安全隐患和技术风险。在此之前，NASA航空航天安全顾问小组发布了一份关键报告，认为原定在“阿耳忒弥斯3号”任务中让宇航员登月的计划在现实中无法实现且风险过高。

**该计划的主要变化包括：**

*   **重新定义“阿耳忒弥斯3号”（2027年）：** 该任务原定为登月任务，现改为在近地轨道进行。宇航员将与SpaceX和蓝色起源（Blue Origin）的商业月球着陆器进行交会对接，以测试导航、生命维持系统和新型航天服。
*   **加速登月进程（2028年）：** NASA目前的目标是在2028年执行两次登月任务（“阿耳忒弥斯4号”和“5号”），并利用2027年轨道测试中收集的数据。
*   **简化SLS火箭：** NASA将取消复杂的“探索上层级”（EUS）的研发，转而使用标准化的SLS上层级，以简化生产并将发射频率提高至每年一次。
*   **战略转型：** 艾萨克曼强调要“回归基础”，借鉴阿波罗时代的增量测试策略。他还强调了培育“轨道经济”的目标，以减少长期以来对纳税人的依赖。

此次公告发布之际，载人绕月飞行任务“阿耳忒弥斯2号”正面临持续延期，由于硬件问题，该任务目前至少推迟至2026年4月。尽管计划有所变动，包括SpaceX、蓝色起源和波音在内的主要承包商均对修订后的战略表示支持，该战略旨在为实现可持续的月球驻留建立高度信心。

---

## 7. Show HN：RetroTick —— 在浏览器中运行经典 Windows EXE 文件

**原文标题**: Show HN: RetroTick – Run classic Windows EXEs in the browser

**原文链接**: [https://retrotick.com/](https://retrotick.com/)

**RetroTick** 是一个基于 Web 的平台，旨在直接在浏览器中运行旧版 Windows 可执行文件 (.exe) 和 DOS 程序。通过利用网页模拟技术，它允许用户无需专用硬件、本地模拟器或复杂的虚拟机设置，即可访问并体验经典软件和复古游戏。

该项目旨在简化复古计算的保存与普及，为爱好者提供一种在现代设备上重温旧版程序的无缝方式。通过 RetroTick，经典的桌面程序被有效转化为即时可用的网页体验。

---

## 8. Show HN: Badge that shows how well your codebase fits in an LLM's context window

**原文标题**: Show HN: Badge that shows how well your codebase fits in an LLM's context window

**原文链接**: [https://github.com/qwibitai/nanoclaw/tree/main/repo-tokens](https://github.com/qwibitai/nanoclaw/tree/main/repo-tokens)

生成摘要时出错

---

## 9. F-Droid Board of Directors nominations 2026

**原文标题**: F-Droid Board of Directors nominations 2026

**原文链接**: [https://f-droid.org/2026/02/26/board-of-directors-nominations.html](https://f-droid.org/2026/02/26/board-of-directors-nominations.html)

生成摘要时出错

---

## 10. Can you reverse engineer our neural network?

**原文标题**: Can you reverse engineer our neural network?

**原文链接**: [https://blog.janestreet.com/can-you-reverse-engineer-our-neural-network/](https://blog.janestreet.com/can-you-reverse-engineer-our-neural-network/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 2 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 3 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 4 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 5 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 6 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 7 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 8 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 9 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 10 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 11 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 12 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 13 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 14 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 15 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 16 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 17 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 18 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 19 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 20 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 21 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 22 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 23 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 24 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 25 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 26 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 27 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 28 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 29 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 30 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 31 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 32 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 33 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 34 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 35 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 36 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 37 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 38 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 39 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 40 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 41 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 42 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 43 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 44 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 45 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 46 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 47 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 48 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 49 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 50 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 51 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 52 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 53 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 54 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 55 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 56 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 57 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 58 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 59 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 60 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 61 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 62 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 63 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 64 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 65 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 66 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 67 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 68 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 69 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 70 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 71 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 72 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 73 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 74 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 75 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 76 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 77 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 78 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 79 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 80 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 81 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 82 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 83 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 84 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 85 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 86 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 87 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 88 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 89 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 90 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 91 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 92 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 93 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 94 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 95 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 96 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 97 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 98 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 99 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 100 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 101 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 102 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 103 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 104 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 105 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 106 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 107 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 108 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 109 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 110 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 111 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 112 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 113 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 114 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 115 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 116 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 117 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 118 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 119 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 120 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 121 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 122 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 123 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 124 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 125 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 126 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 127 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 128 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 129 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 130 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 131 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 132 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 133 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 134 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 135 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 136 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 137 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 138 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 139 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 140 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 141 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 142 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 143 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 144 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 145 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 146 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 147 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 148 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 149 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 150 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 151 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 152 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 153 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 154 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 155 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 156 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 157 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 158 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 159 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 160 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 161 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 162 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 163 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 164 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 165 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 166 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 167 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 168 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 169 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 170 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 171 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 172 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 173 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 174 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 175 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 176 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 177 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 178 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 179 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 180 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 181 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 182 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 183 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 184 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 185 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 186 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 187 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 188 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 189 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 190 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 191 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 192 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 193 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 194 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 195 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 196 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 197 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 198 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 199 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 200 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 201 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 202 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 203 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 204 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 205 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 206 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 207 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 208 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 209 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 210 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 211 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 212 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 213 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 214 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 215 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 216 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 217 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 218 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 219 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 220 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 221 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 222 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 223 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 224 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 225 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 226 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 227 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 228 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 229 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 230 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 231 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 232 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 233 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 234 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 235 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 236 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 237 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 238 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 239 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 240 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 241 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 242 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 243 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 244 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 245 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 246 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 247 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 248 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 249 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 250 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 251 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 252 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 253 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 254 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 255 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 256 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 257 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 258 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 259 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 260 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 261 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 262 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 263 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 264 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 265 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 266 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 267 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 268 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 269 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 270 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 271 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 272 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 273 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 274 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 275 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 276 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 277 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 278 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 279 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 280 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 281 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 282 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 283 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 284 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 285 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 286 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 287 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 288 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 289 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 290 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 291 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 292 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 293 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 294 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 295 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 296 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 297 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 298 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 299 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 300 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 301 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 302 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 303 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 304 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 305 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 306 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 307 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 308 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 309 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 310 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 311 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 312 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 313 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 314 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 315 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 316 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 317 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 318 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 319 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 320 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 321 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 322 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 323 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 324 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 325 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 326 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 327 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 328 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 329 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 330 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 331 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 332 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 333 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 334 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 335 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 336 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 337 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 338 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 339 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 340 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 341 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 342 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 343 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 344 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
