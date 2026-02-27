# Hacker News 热门文章摘要 (2026-02-27)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Experts sound alarm after ChatGPT Health fails to recognise medical emergencies

**原文标题**: Experts sound alarm after ChatGPT Health fails to recognise medical emergencies

**原文链接**: [https://www.theguardian.com/technology/2026/feb/26/chatgpt-health-fails-recognise-medical-emergencies](https://www.theguardian.com/technology/2026/feb/26/chatgpt-health-fails-recognise-medical-emergencies)

生成摘要时出错

---

## 12. Vibe coded Lovable-hosted app littered with basic flaws exposed 18K users

**原文标题**: Vibe coded Lovable-hosted app littered with basic flaws exposed 18K users

**原文链接**: [https://www.theregister.com/2026/02/27/lovable_app_vulnerabilities/](https://www.theregister.com/2026/02/27/lovable_app_vulnerabilities/)

生成摘要时出错

---

## 13. Sprites on the Web

**原文标题**: Sprites on the Web

**原文链接**: [https://www.joshwcomeau.com/animation/sprites/](https://www.joshwcomeau.com/animation/sprites/)

生成摘要时出错

---

## 14. An interactive intro to quadtrees

**原文标题**: An interactive intro to quadtrees

**原文链接**: [https://growingswe.com/blog/quadtrees](https://growingswe.com/blog/quadtrees)

生成摘要时出错

---

## 15. Get free Claude max 20x for open-source maintainers

**原文标题**: Get free Claude max 20x for open-source maintainers

**原文链接**: [https://claude.com/contact-sales/claude-for-oss](https://claude.com/contact-sales/claude-for-oss)

生成摘要时出错

---

## 16. The Hunt for Dark Breakfast

**原文标题**: The Hunt for Dark Breakfast

**原文链接**: [https://moultano.wordpress.com/2026/02/22/the-hunt-for-dark-breakfast/](https://moultano.wordpress.com/2026/02/22/the-hunt-for-dark-breakfast/)

生成摘要时出错

---

## 17. The normalization of corruption in organizations (2003) [pdf]

**原文标题**: The normalization of corruption in organizations (2003) [pdf]

**原文链接**: [https://gwern.net/doc/sociology/2003-ashforth.pdf](https://gwern.net/doc/sociology/2003-ashforth.pdf)

生成摘要时出错

---

## 18. Breaking Free

**原文标题**: Breaking Free

**原文链接**: [https://www.forbrukerradet.no/breakingfree/](https://www.forbrukerradet.no/breakingfree/)

生成摘要时出错

---

## 19. Modeling Cycles of Grift with Evolutionary Game Theory

**原文标题**: Modeling Cycles of Grift with Evolutionary Game Theory

**原文链接**: [https://www.oranlooney.com/post/grifters-skeptics-marks/](https://www.oranlooney.com/post/grifters-skeptics-marks/)

生成摘要时出错

---

## 20. The quixotic team trying to build a world in a 20-year-old game

**原文标题**: The quixotic team trying to build a world in a 20-year-old game

**原文链接**: [https://arstechnica.com/gaming/2026/02/inside-the-quixotic-team-trying-to-build-an-entire-world-in-a-20-year-old-game/](https://arstechnica.com/gaming/2026/02/inside-the-quixotic-team-trying-to-build-an-entire-world-in-a-20-year-old-game/)

生成摘要时出错

---

## 21. How to Allocate Memory

**原文标题**: How to Allocate Memory

**原文链接**: [https://geocar.sdf1.org/alloc.html](https://geocar.sdf1.org/alloc.html)

生成摘要时出错

---

## 22. Ubicloud (YC W24): Software Engineer – $95-$250K in Turkey, Netherlands, CA

**原文标题**: Ubicloud (YC W24): Software Engineer – $95-$250K in Turkey, Netherlands, CA

**原文链接**: [https://www.ycombinator.com/companies/ubicloud/jobs/j4bntEJ-software-engineer](https://www.ycombinator.com/companies/ubicloud/jobs/j4bntEJ-software-engineer)

生成摘要时出错

---

## 23. Reading English from 1000 Ad

**原文标题**: Reading English from 1000 Ad

**原文链接**: [https://lewiscampbell.tech/blog/260224.html](https://lewiscampbell.tech/blog/260224.html)

生成摘要时出错

---

## 24. What Claude Code chooses

**原文标题**: What Claude Code chooses

**原文链接**: [https://amplifying.ai/research/claude-code-picks](https://amplifying.ai/research/claude-code-picks)

生成摘要时出错

---

## 25. Working on Pharo Smalltalk: BPatterns: Rewrite Engine with Smalltalk Style

**原文标题**: Working on Pharo Smalltalk: BPatterns: Rewrite Engine with Smalltalk Style

**原文链接**: [http://dionisiydk.blogspot.com/2026/02/bpatterns-rewrite-engine-with-smalltalk.html](http://dionisiydk.blogspot.com/2026/02/bpatterns-rewrite-engine-with-smalltalk.html)

生成摘要时出错

---

## 26. 80386 Protection

**原文标题**: 80386 Protection

**原文链接**: [https://nand2mario.github.io/posts/2026/80386_protection/](https://nand2mario.github.io/posts/2026/80386_protection/)

生成摘要时出错

---

## 27. What does " 2>&1 " mean?

**原文标题**: What does " 2>&1 " mean?

**原文链接**: [https://stackoverflow.com/questions/818255/what-does-21-mean](https://stackoverflow.com/questions/818255/what-does-21-mean)

生成摘要时出错

---

## 28. AirSnitch: Demystifying and breaking client isolation in Wi-Fi networks [pdf]

**原文标题**: AirSnitch: Demystifying and breaking client isolation in Wi-Fi networks [pdf]

**原文链接**: [https://www.ndss-symposium.org/wp-content/uploads/2026-f1282-paper.pdf](https://www.ndss-symposium.org/wp-content/uploads/2026-f1282-paper.pdf)

生成摘要时出错

---

## 29. The complete Manic Miner disassembly

**原文标题**: The complete Manic Miner disassembly

**原文链接**: [https://skoolkit.ca/disassemblies/manic_miner/](https://skoolkit.ca/disassemblies/manic_miner/)

生成摘要时出错

---

## 30. Layoffs at Block

**原文标题**: Layoffs at Block

**原文链接**: [https://twitter.com/jack/status/2027129697092731343](https://twitter.com/jack/status/2027129697092731343)

生成摘要时出错

---

## 31. New California law requires age verification for all OS accounts

**原文标题**: New California law requires age verification for all OS accounts

**原文链接**: [https://www.pcgamer.com/software/operating-systems/a-new-california-law-says-all-operating-systems-including-linux-need-to-have-some-form-of-age-verification-at-account-setup/](https://www.pcgamer.com/software/operating-systems/a-new-california-law-says-all-operating-systems-including-linux-need-to-have-some-form-of-age-verification-at-account-setup/)

生成摘要时出错

---

## 32. Compact disc story (1998)

**原文标题**: Compact disc story (1998)

**原文链接**: [https://www.researchgate.net/publication/294484774_Compact_disc_story](https://www.researchgate.net/publication/294484774_Compact_disc_story)

生成摘要时出错

---

## 33. The history of knocking on wood

**原文标题**: The history of knocking on wood

**原文链接**: [https://resobscura.substack.com/p/neolithic-habits-machine-age-tools](https://resobscura.substack.com/p/neolithic-habits-machine-age-tools)

生成摘要时出错

---

## 34. OsmAnd’s Faster Offline Navigation (2025)

**原文标题**: OsmAnd’s Faster Offline Navigation (2025)

**原文链接**: [https://osmand.net/blog/fast-routing/](https://osmand.net/blog/fast-routing/)

生成摘要时出错

---

## 35. I rendered 1,418 confusables over 230 fonts. Most aren't confusable to the eye

**原文标题**: I rendered 1,418 confusables over 230 fonts. Most aren't confusable to the eye

**原文链接**: [https://paultendo.github.io/posts/confusable-vision-visual-similarity/](https://paultendo.github.io/posts/confusable-vision-visual-similarity/)

生成摘要时出错

---

## 36. Parakeet.cpp – Parakeet ASR inference in pure C++ with Metal GPU acceleration

**原文标题**: Parakeet.cpp – Parakeet ASR inference in pure C++ with Metal GPU acceleration

**原文链接**: [https://github.com/Frikallo/parakeet.cpp](https://github.com/Frikallo/parakeet.cpp)

生成摘要时出错

---

## 37. Launch HN: Cardboard (YC W26) – Agentic video editor

**原文标题**: Launch HN: Cardboard (YC W26) – Agentic video editor

**原文链接**: [https://www.usecardboard.com/](https://www.usecardboard.com/)

生成摘要时出错

---

## 38. BuildKit: Docker's Hidden Gem That Can Build Almost Anything

**原文标题**: BuildKit: Docker's Hidden Gem That Can Build Almost Anything

**原文链接**: [https://tuananh.net/2026/02/25/buildkit-docker-hidden-gem/](https://tuananh.net/2026/02/25/buildkit-docker-hidden-gem/)

This article highlights **BuildKit** as a versatile, general-purpose build engine that extends far beyond its common use as the backend for Dockerfiles. The author argues that BuildKit is to build systems what LLVM is to compilers—a powerful framework capable of building almost anything that can be described as a directed acyclic graph (DAG) of filesystem operations.

The engine relies on three core concepts:
1.  **LLB (Low-Level Build definition):** An intermediate representation of the build process. Like LLVM IR, LLB is content-addressable and binary-based, enabling aggressive caching and parallel execution.
2.  **Frontends:** Pluggable layers that convert various input formats (like YAML, TOML, or custom DSLs) into LLB. The standard Dockerfile is merely the default frontend; users can specify others using the `# syntax=` directive.
3.  **Solver and Cache:** The execution engine that processes the LLB graph. It supports sophisticated caching (local or remote) and can execute independent build branches simultaneously.

A key advantage of BuildKit is its flexibility in **outputs**. By using the `--output` flag, users can bypass container images entirely and export build artifacts as local directories, tarballs, or OCI images. To demonstrate this, the author showcases a custom frontend that builds Alpine APK packages directly from a YAML specification.

Ultimately, the article posits that BuildKit is a proven, scalable backend for modern CI/CD and orchestration tools (such as Dagger and Earthly). It allows developers to create specialized build tools without having to reinvent the complex logic required for caching, parallelism, and reproducibility.

---

## 39. The Man Who Stole Infinity

**原文标题**: The Man Who Stole Infinity

**原文链接**: [https://www.quantamagazine.org/the-man-who-stole-infinity-20260225/](https://www.quantamagazine.org/the-man-who-stole-infinity-20260225/)

生成摘要时出错

---

## 40. Show HN: Hacker Smacker – Spot great (and terrible) HN commenters at a glance

**原文标题**: Show HN: Hacker Smacker – Spot great (and terrible) HN commenters at a glance

**原文链接**: [https://hackersmacker.org](https://hackersmacker.org)

生成摘要时出错

---

## 41. ChatGPT Health performance in a structured test of triage recommendations

**原文标题**: ChatGPT Health performance in a structured test of triage recommendations

**原文链接**: [https://www.nature.com/articles/s41591-026-04297-7](https://www.nature.com/articles/s41591-026-04297-7)

生成摘要时出错

---

## 42. Palm OS 用户界面指南 (2003) [pdf]

**原文标题**: Palm OS User Interface Guidelines (2003) [pdf]

**原文链接**: [https://cs.uml.edu/~fredm/courses/91.308-spr05/files/palmdocs/uiguidelines.pdf](https://cs.uml.edu/~fredm/courses/91.308-spr05/files/palmdocs/uiguidelines.pdf)

生成摘要时出错

---

## 43. I baked a pie every day for a year

**原文标题**: I baked a pie every day for a year

**原文链接**: [https://www.theguardian.com/lifeandstyle/2026/feb/22/a-new-start-after-60-i-baked-a-pie-every-day-for-a-year-and-it-changed-my-life](https://www.theguardian.com/lifeandstyle/2026/feb/22/a-new-start-after-60-i-baked-a-pie-every-day-for-a-year-and-it-changed-my-life)

生成摘要时出错

---

## 44. OpenAI raises $110B on $730B pre-money valuation

**原文标题**: OpenAI raises $110B on $730B pre-money valuation

**原文链接**: [https://techcrunch.com/2026/02/27/openai-raises-110b-in-one-of-the-largest-private-funding-rounds-in-history/](https://techcrunch.com/2026/02/27/openai-raises-110b-in-one-of-the-largest-private-funding-rounds-in-history/)

生成摘要时出错

---

## 45. This time is different

**原文标题**: This time is different

**原文链接**: [https://shkspr.mobi/blog/2026/02/this-time-is-different/](https://shkspr.mobi/blog/2026/02/this-time-is-different/)

生成摘要时出错

---

## 46. Google API keys weren't secrets, but then Gemini changed the rules

**原文标题**: Google API keys weren't secrets, but then Gemini changed the rules

**原文链接**: [https://trufflesecurity.com/blog/google-api-keys-werent-secrets-but-then-gemini-changed-the-rules](https://trufflesecurity.com/blog/google-api-keys-werent-secrets-but-then-gemini-changed-the-rules)

生成摘要时出错

---

## 47. Implementing a clear room Z80 / ZX Spectrum emulator with Claude Code

**原文标题**: Implementing a clear room Z80 / ZX Spectrum emulator with Claude Code

**原文链接**: [https://antirez.com/news/160](https://antirez.com/news/160)

生成摘要时出错

---

## 48. The Physics and Economics of Moving 44 Tonnes at 56mph

**原文标题**: The Physics and Economics of Moving 44 Tonnes at 56mph

**原文链接**: [https://www.mikeayles.com/blog/heavy-haulage-basics/](https://www.mikeayles.com/blog/heavy-haulage-basics/)

生成摘要时出错

---

## 49. Show HN: Linex – A daily challenge: placing pieces on a board that fights back

**原文标题**: Show HN: Linex – A daily challenge: placing pieces on a board that fights back

**原文链接**: [https://www.playlinex.com/](https://www.playlinex.com/)

生成摘要时出错

---

## 50. Understanding the Go Runtime: The Memory Allocator

**原文标题**: Understanding the Go Runtime: The Memory Allocator

**原文链接**: [https://internals-for-interns.com/posts/go-memory-allocator/](https://internals-for-interns.com/posts/go-memory-allocator/)

生成摘要时出错

---

## 51. Show HN: Deff – Side-by-side Git diff review in your terminal

**原文标题**: Show HN: Deff – Side-by-side Git diff review in your terminal

**原文链接**: [https://github.com/flamestro/deff](https://github.com/flamestro/deff)

生成摘要时出错

---

## 52. Nano Banana 2: Google's latest AI image generation model

**原文标题**: Nano Banana 2: Google's latest AI image generation model

**原文链接**: [https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/](https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/)

生成摘要时出错

---

## 53. Hydroph0bia – fixed SecureBoot bypass for UEFI firmware from Insyde H2O (2025)

**原文标题**: Hydroph0bia – fixed SecureBoot bypass for UEFI firmware from Insyde H2O (2025)

**原文链接**: [https://coderush.me/hydroph0bia-part3/](https://coderush.me/hydroph0bia-part3/)

生成摘要时出错

---

## 54. Dyson settles forced labour suit in landmark UK case

**原文标题**: Dyson settles forced labour suit in landmark UK case

**原文链接**: [https://www.bbc.com/news/articles/cddnry8dnl7o](https://www.bbc.com/news/articles/cddnry8dnl7o)

生成摘要时出错

---

## 55. Steering interpretable language models with concept algebra

**原文标题**: Steering interpretable language models with concept algebra

**原文链接**: [https://www.guidelabs.ai/post/steerling-steering-8b/](https://www.guidelabs.ai/post/steerling-steering-8b/)

生成摘要时出错

---

## 56. OpenAI's $110B funding round (investments from Amazon, Nvidia, SoftBank)

**原文标题**: OpenAI's $110B funding round (investments from Amazon, Nvidia, SoftBank)

**原文链接**: [https://www.reuters.com/business/retail-consumer/amazon-invest-50-billion-openai-2026-02-27/](https://www.reuters.com/business/retail-consumer/amazon-invest-50-billion-openai-2026-02-27/)

生成摘要时出错

---

## 57. Warrant Canary

**原文标题**: Warrant Canary

**原文链接**: [https://en.wikipedia.org/wiki/Warrant_canary](https://en.wikipedia.org/wiki/Warrant_canary)

生成摘要时出错

---

## 58. Will vibe coding end like the maker movement?

**原文标题**: Will vibe coding end like the maker movement?

**原文链接**: [https://read.technically.dev/p/vibe-coding-and-the-maker-movement](https://read.technically.dev/p/vibe-coding-and-the-maker-movement)

生成摘要时出错

---

## 59. Banned in California

**原文标题**: Banned in California

**原文链接**: [https://www.bannedincalifornia.org/](https://www.bannedincalifornia.org/)

生成摘要时出错

---

## 60. Fentanyl makeover: Core structural redesign could lead to safer pain medications

**原文标题**: Fentanyl makeover: Core structural redesign could lead to safer pain medications

**原文链接**: [https://www.scripps.edu/news-and-events/press-room/2026/20260211-janda-molecule.html](https://www.scripps.edu/news-and-events/press-room/2026/20260211-janda-molecule.html)

生成摘要时出错

---

## 61. Just-bash: Bash for Agents

**原文标题**: Just-bash: Bash for Agents

**原文链接**: [https://github.com/vercel-labs/just-bash](https://github.com/vercel-labs/just-bash)

生成摘要时出错

---

## 62. PostmarketOS in 2026-02: generic kernels, bans use of generative AI

**原文标题**: PostmarketOS in 2026-02: generic kernels, bans use of generative AI

**原文链接**: [https://postmarketos.org/blog/2026/02/26/pmOS-update-2026-02/](https://postmarketos.org/blog/2026/02/26/pmOS-update-2026-02/)

生成摘要时出错

---

## 63. Show HN: Terminal Phone – E2EE Walkie Talkie from the Command Line

**原文标题**: Show HN: Terminal Phone – E2EE Walkie Talkie from the Command Line

**原文链接**: [https://gitlab.com/here_forawhile/terminalphone](https://gitlab.com/here_forawhile/terminalphone)

生成摘要时出错

---

## 64. Smartphone market forecast to decline this year due to memory shortage

**原文标题**: Smartphone market forecast to decline this year due to memory shortage

**原文链接**: [https://www.idc.com/resource-center/press-releases/wwsmartphoneforecast4q25/](https://www.idc.com/resource-center/press-releases/wwsmartphoneforecast4q25/)

生成摘要时出错

---

## 65. Jimi Hendrix was a systems engineer

**原文标题**: Jimi Hendrix was a systems engineer

**原文链接**: [https://spectrum.ieee.org/jimi-hendrix-systems-engineer](https://spectrum.ieee.org/jimi-hendrix-systems-engineer)

生成摘要时出错

---

## 66. MitID, Denmarks sole digital ID, has been down for over an hour and counting

**原文标题**: MitID, Denmarks sole digital ID, has been down for over an hour and counting

**原文链接**: [https://www.digitaliser.dk/mitid/nyt-fra-mitid/2026/feb/driftsforstyrrelser-mitid](https://www.digitaliser.dk/mitid/nyt-fra-mitid/2026/feb/driftsforstyrrelser-mitid)

生成摘要时出错

---

## 67. Show HN: Respectify – A comment moderator that teaches people to argue better

**原文标题**: Show HN: Respectify – A comment moderator that teaches people to argue better

**原文链接**: [https://respectify.org/](https://respectify.org/)

生成摘要时出错

---

## 68. I pitched a roller coaster to Disneyland at age 10 in 1978

**原文标题**: I pitched a roller coaster to Disneyland at age 10 in 1978

**原文链接**: [https://wordglyph.xyz/one-piece-at-a-time](https://wordglyph.xyz/one-piece-at-a-time)

生成摘要时出错

---

## 69. Two insider cases we've recently closed

**原文标题**: Two insider cases we've recently closed

**原文链接**: [https://news.kalshi.com/p/kalshi-trading-violation-enforcement-cases](https://news.kalshi.com/p/kalshi-trading-violation-enforcement-cases)

生成摘要时出错

---

## 70. Open Source Endowment – new funding source for open source maintainers

**原文标题**: Open Source Endowment – new funding source for open source maintainers

**原文链接**: [https://endowment.dev/](https://endowment.dev/)

生成摘要时出错

---

## 71. The Om Programming Language

**原文标题**: The Om Programming Language

**原文链接**: [https://www.om-language.com/](https://www.om-language.com/)

生成摘要时出错

---

## 72. Netflix Backs Out of Warner Bros. Bidding, Paramount Set to Win

**原文标题**: Netflix Backs Out of Warner Bros. Bidding, Paramount Set to Win

**原文链接**: [https://www.hollywoodreporter.com/business/business-news/netflix-backs-out-warners-deal-paramount-win-1236516763/](https://www.hollywoodreporter.com/business/business-news/netflix-backs-out-warners-deal-paramount-win-1236516763/)

生成摘要时出错

---

## 73. Cronboard: A terminal-based dashboard for managing cron jobs

**原文标题**: Cronboard: A terminal-based dashboard for managing cron jobs

**原文链接**: [https://github.com/antoniorodr/cronboard](https://github.com/antoniorodr/cronboard)

生成摘要时出错

---

## 74. Show HN: Beehive – Multi-Workspace Agent Orchestrator

**原文标题**: Show HN: Beehive – Multi-Workspace Agent Orchestrator

**原文链接**: [https://storozhenko98.github.io/beehive/](https://storozhenko98.github.io/beehive/)

生成摘要时出错

---

## 75. How will OpenAI compete?

**原文标题**: How will OpenAI compete?

**原文链接**: [https://www.ben-evans.com/benedictevans/2026/2/19/how-will-openai-compete-nkg2x](https://www.ben-evans.com/benedictevans/2026/2/19/how-will-openai-compete-nkg2x)

生成摘要时出错

---

## 76. You Just Need Postgres

**原文标题**: You Just Need Postgres

**原文链接**: [https://youjustneedpostgres.com/](https://youjustneedpostgres.com/)

生成摘要时出错

---

## 77. Scaling AI for Everyone

**原文标题**: Scaling AI for Everyone

**原文链接**: [https://openai.com/index/scaling-ai-for-everyone/](https://openai.com/index/scaling-ai-for-everyone/)

生成摘要时出错

---

## 78. An autopsy of AI-generated 3D slop

**原文标题**: An autopsy of AI-generated 3D slop

**原文链接**: [https://aircada.com/blog/ai-vs-human-3d-ecommerce](https://aircada.com/blog/ai-vs-human-3d-ecommerce)

生成摘要时出错

---

## 79. GNU Texmacs

**原文标题**: GNU Texmacs

**原文链接**: [https://www.texmacs.org/tmweb/home/welcome.en.html](https://www.texmacs.org/tmweb/home/welcome.en.html)

生成摘要时出错

---

## 80. Bus stop balancing is fast, cheap, and effective

**原文标题**: Bus stop balancing is fast, cheap, and effective

**原文链接**: [https://worksinprogress.co/issue/the-united-states-needs-fewer-bus-stops/](https://worksinprogress.co/issue/the-united-states-needs-fewer-bus-stops/)

生成摘要时出错

---

## 81. 56% of CEOs report zero financial return from AI in 2026 (PwC survey, n=4,454)

**原文标题**: 56% of CEOs report zero financial return from AI in 2026 (PwC survey, n=4,454)

**原文链接**: [https://aishortcutlab.com/articles/pwc-ceo-survey-2026-only-12-of-ceos-win-with-ai](https://aishortcutlab.com/articles/pwc-ceo-survey-2026-only-12-of-ceos-win-with-ai)

生成摘要时出错

---

## 82. Tech companies shouldn't be bullied into doing surveillance

**原文标题**: Tech companies shouldn't be bullied into doing surveillance

**原文链接**: [https://www.eff.org/deeplinks/2026/02/tech-companies-shouldnt-be-bullied-doing-surveillance](https://www.eff.org/deeplinks/2026/02/tech-companies-shouldnt-be-bullied-doing-surveillance)

生成摘要时出错

---

## 83. Why isn't LA repaving streets?

**原文标题**: Why isn't LA repaving streets?

**原文链接**: [https://lapublicpress.org/2026/02/why-isnt-la-repaving-streets/](https://lapublicpress.org/2026/02/why-isnt-la-repaving-streets/)

生成摘要时出错

---

## 84. Show HN: CodeLeash: framework for quality agent development, NOT an orchestrator

**原文标题**: Show HN: CodeLeash: framework for quality agent development, NOT an orchestrator

**原文链接**: [https://codeleash.dev/](https://codeleash.dev/)

CodeLeash is an opinionated full-stack framework and toolkit designed to enforce high-quality software development when using coding agents like Claude Code. Distinguishing itself from AI orchestrators, CodeLeash focuses on "guardrails"—external constraints that force agents to follow architectural standards through automation rather than just prompts.

**Key Features:**

*   **Enforced TDD:** The framework mandates the Red-Green-Refactor cycle via a state machine. An agent is blocked from editing implementation files until it has written and witnessed a failing test, preventing shortcuts.
*   **Deterministic Quality Checks:** Instead of burning tokens on AI-driven reviews, CodeLeash uses fast, deterministic scripts (regex, AST) to validate code. These checks block commits upon failure and provide specific instructions for the agent to fix the issue.
*   **Self-Reflection System:** To combat "agent amnesia," CodeLeash forces agents to document insights and workflow friction before a session ends. These notes are later integrated back into the codebase as permanent improvements.
*   **Performance Constraints:** Unit tests are strictly limited to a 10ms timeout. This ensures tests remain pure business logic, enabling parallel execution and an entire suite that runs in seconds.
*   **Worktree Isolation:** The system utilizes git worktrees to allow agents to develop multiple features simultaneously in isolated environments with no port or dependency collisions.

The framework utilizes a monorepo stack featuring **FastAPI (Python)**, **React (TypeScript/Vite)**, and **Supabase**. By codifying quality standards into hooks and loops, CodeLeash aims to remove humans from the loop of supervising agent discipline, ensuring the agent remains productive and "on a leash" even during complex, multi-step tasks.

---

## 85. Show HN: Rev-dep – 20x faster knip.dev alternative build in Go

**原文标题**: Show HN: Rev-dep – 20x faster knip.dev alternative build in Go

**原文链接**: [https://github.com/jayu/rev-dep](https://github.com/jayu/rev-dep)

生成摘要时出错

---

## 86. Danish government agency to ditch Microsoft software (2025)

**原文标题**: Danish government agency to ditch Microsoft software (2025)

**原文链接**: [https://therecord.media/denmark-digital-agency-microsoft-digital-independence](https://therecord.media/denmark-digital-agency-microsoft-digital-independence)

生成摘要时出错

---

## 87. Dissecting the CPU-memory relationship in garbage collection (OpenJDK 26)

**原文标题**: Dissecting the CPU-memory relationship in garbage collection (OpenJDK 26)

**原文链接**: [https://norlinder.nu/posts/GC-Cost-CPU-vs-Memory/](https://norlinder.nu/posts/GC-Cost-CPU-vs-Memory/)

生成摘要时出错

---

## 88. LLM=True

**原文标题**: LLM=True

**原文链接**: [https://blog.codemine.be/posts/2026/20260222-be-quiet/](https://blog.codemine.be/posts/2026/20260222-be-quiet/)

生成摘要时出错

---

## 89. Never buy a .online domain

**原文标题**: Never buy a .online domain

**原文链接**: [https://www.0xsid.com/blog/online-tld-is-pain](https://www.0xsid.com/blog/online-tld-is-pain)

生成摘要时出错

---

## 90. Show HN: A real-time strategy game that AI agents can play

**原文标题**: Show HN: A real-time strategy game that AI agents can play

**原文链接**: [https://llmskirmish.com/](https://llmskirmish.com/)

生成摘要时出错

---

## 91. Windows 11 Notepad to support Markdown

**原文标题**: Windows 11 Notepad to support Markdown

**原文链接**: [https://blogs.windows.com/windows-insider/2026/01/21/notepad-and-paint-updates-begin-rolling-out-to-windows-insiders/](https://blogs.windows.com/windows-insider/2026/01/21/notepad-and-paint-updates-begin-rolling-out-to-windows-insiders/)

生成摘要时出错

---

## 92. He saw an abandoned trailer, then uncovered a surveillance network

**原文标题**: He saw an abandoned trailer, then uncovered a surveillance network

**原文链接**: [https://calmatters.org/justice/2026/02/alpr-border-patrol-caltrans/](https://calmatters.org/justice/2026/02/alpr-border-patrol-caltrans/)

生成摘要时出错

---

## 93. Launch HN: TeamOut (YC W22) – AI agent for planning company retreats

**原文标题**: Launch HN: TeamOut (YC W22) – AI agent for planning company retreats

**原文链接**: [https://app.teamout.com/ai](https://app.teamout.com/ai)

生成摘要时出错

---

## 94. 100M-Row Challenge with PHP

**原文标题**: 100M-Row Challenge with PHP

**原文链接**: [https://github.com/tempestphp/100-million-row-challenge](https://github.com/tempestphp/100-million-row-challenge)

生成摘要时出错

---

## 95. The Longest Line of Sight

**原文标题**: The Longest Line of Sight

**原文链接**: [https://tombh.co.uk/longest-line-of-sight](https://tombh.co.uk/longest-line-of-sight)

生成摘要时出错

---

## 96. OpenAI uncovers Chinese intimidation operation through official's use of ChatGPT

**原文标题**: OpenAI uncovers Chinese intimidation operation through official's use of ChatGPT

**原文链接**: [https://www.cnn.com/2026/02/25/politics/chatgpt-china-intimidation-operation](https://www.cnn.com/2026/02/25/politics/chatgpt-china-intimidation-operation)

生成摘要时出错

---

## 97. RK3588 and RK3576 video decoders support merged in the upstream Linux Kernel

**原文标题**: RK3588 and RK3576 video decoders support merged in the upstream Linux Kernel

**原文链接**: [https://www.collabora.com/news-and-blog/news-and-events/rk3588-and-rk3576-video-decoders-support-merged-in-the-upstream-linux-kernel.html](https://www.collabora.com/news-and-blog/news-and-events/rk3588-and-rk3576-video-decoders-support-merged-in-the-upstream-linux-kernel.html)

生成摘要时出错

---

## 98. The Misuses of the University

**原文标题**: The Misuses of the University

**原文链接**: [https://www.publicbooks.org/the-misuses-of-the-university/](https://www.publicbooks.org/the-misuses-of-the-university/)

生成摘要时出错

---

## 99. Emacs Is a Lisp Runtime in C, Not an Editor

**原文标题**: Emacs Is a Lisp Runtime in C, Not an Editor

**原文链接**: [https://thecloudlet.github.io/blog/project/emacs-01/](https://thecloudlet.github.io/blog/project/emacs-01/)

生成摘要时出错

---

## 100. Learnings from 4 months of Image-Video VAE experiments

**原文标题**: Learnings from 4 months of Image-Video VAE experiments

**原文链接**: [https://www.linum.ai/field-notes/vae-reconstruction-vs-generation](https://www.linum.ai/field-notes/vae-reconstruction-vs-generation)

生成摘要时出错

---

