# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-02.md)

*最后自动更新时间: 2026-04-02 18:11:51*
## 1. 阿耳忒弥斯2号发射日动态

**原文标题**: Artemis II Launch Day Updates

**原文链接**: [https://www.nasa.gov/blogs/missions/2026/04/01/live-artemis-ii-launch-day-updates/](https://www.nasa.gov/blogs/missions/2026/04/01/live-artemis-ii-launch-day-updates/)

2026年4月1日东部夏令时间下午6:35，美国国家航空航天局（NASA）在肯尼迪航天中心成功发射了“阿耳忒弥斯2号”任务，标志着“阿耳忒弥斯”计划实现了首次载人飞行。此次任务搭载了NASA宇航员里德·怀斯曼、维克多·格洛弗、克里斯蒂娜·科赫以及加拿大航天局宇航员杰里米·汉森，开展为期10天的绕月测试飞行。

发射前顺利完成了一系列关键里程碑，包括解决了飞行中止系统的通信问题，并排除了一个微小的电池传感器异常。尽管为了进行最后准备，T-10分钟的停表时间有所延长，但任务最终获得了发射总监的一致批准。

太空发射系统（SLS）火箭在起飞时产生了880万磅的推力。关键的上升里程碑均按计划达成，包括固体火箭助推器分离、整流罩抛离及核心级分离。发射后约24分钟，被命名为“诚信号”（Integrity）的猎户座飞船成功展开了四块太阳能电池翼，确认其已开始供电并准备好进行深空作业。

发射结束后，机组人员开始为接下来的主要机动任务做准备：近地点抬升机动（PRM）和远地点抬升点火（ARB）。这些操作将优化猎户座飞船的轨道，随后机组人员将进行近距离操作演示，以测试相对于火箭末级的手动操控能力。

该任务是对持续月球探测及未来载人火星任务所需系统的关键测试，旨在验证飞船能否在深空中安全地保障人类生命。

---

## 2. 订阅轰炸及其缓解措施

**原文标题**: Subscription bombing and how to mitigate it

**原文链接**: [https://bytemash.net/posts/subscription-bombing-your-signup-form-is-a-weapon/](https://bytemash.net/posts/subscription-bombing-your-signup-form-is-a-weapon/)

Suga 团队最近在注意到有一波名称乱码且持续增加的非活跃账户后，发现了一次“订阅轰炸”（subscription bombing）攻击。订阅轰炸是一种恶意手段，机器人会同时将受害者的电子邮箱注册到成千上万个时事通讯和服务中。其目的是让大量干扰信息充斥受害者的收件箱，从而掩盖关键的安全警报——例如银行密码重置或未经授权的购买通知——使攻击者能够悄无声息地进行欺诈。

攻击者采用了复杂的手段来保持隐蔽，包括：
*   **低频流量：** 每小时仅请求 1-2 次注册，以绕过传统的速率限制。
*   **模拟人类行为：** 使用随机、缓慢的输入速度和多变的页面浏览间隔。
*   **全球分布：** 通过不同国家的路由转发流量，以规避基于 IP 的封锁。

虽然此次攻击对 Suga 的服务器或邮件信誉影响微乎其微，但团队意识到其平台正被利用来骚扰无辜受害者。为了减轻这一威胁，他们实施了两项主要解决方案：

1.  **Cloudflare Turnstile：** 这种隐形验证码替代方案通过分析浏览器信号来拦截机器人，无需用户手动解题。它通过 Better Auth 集成，用以阻止自动化注册和密码重置请求。
2.  **严格的邮件策略：** 系统进行了更新，确保未验证账户仅会收到一封邮件（即验证链接）。在用户证明对邮箱的所有权之前，“欢迎”邮件和产品更新将被暂缓发送。

作者总结道，网站所有者有责任防止其注册表单成为骚扰工具。通过在发送后续通信前要求邮件验证，开发者可以保护更广泛的互联网社区免受恶意干扰信息的侵扰。

---

## 3. 因为主板 PWM 功能一直无法正常使用，我自制了一个廉价的风扇控制器。

**原文标题**: Built a cheap DIY fan controller because my motherboard never had working PWM

**原文链接**: [https://www.himthe.dev/blog/msi-forgot-my-fans](https://www.himthe.dev/blog/msi-forgot-my-fans)

面对微星 (MSI) 970 Gaming 主板的一个硬件缺陷——其 Super IO 芯片未接线，导致温度传感器失效且风扇始终以 100% 全速运转——作者利用 Arduino Nano 和自定义软件开发了一款 DIY 风扇控制器。

**硬件方案**
作者编写了一个开源 Arduino 脚本 (**ArduinoFanX**)，用于生成 25kHz 相位校正 PWM 信号（PC 风扇标准）。与 Arduino 默认的低频 PWM 不同，此方案可防止风扇产生啸叫。该装置通过 USB 连接 Nano 兼容板，仅需一个引脚即可控制风扇集线器。它具备优先级系统：可遵循 PC 应用程序指令、镜像主板信号，或通过物理按钮（如复用电脑的重启键）切换手动预设。

**软件方案**
为了管理风扇曲线，作者开发了 **DummyFanX**。该程序起初由 Rust 编写，后改为 C++ 和 DirectX 9 开发，以确保从 Windows XP 到 Windows 11 的极广系统兼容性。应用通过 HWiNFO 或内核驱动程序 (PawnIO) 读取 CPU 温度，并支持高级自定义功能，包括迟滞、速率限制和零转速模式。若温度读取失败，系统将默认切换至 100% 转速以确保安全。

**项目意义**
该项目为 Corsair iLink 等昂贵的私有控制器提供了一种廉价、非垄断的替代方案。对于使用较旧插槽（如 LGA 775、AM2 或 Socket 939）且通常缺乏现代 4 针 PWM 接口的老硬件爱好者来说，它具有很高的实用价值。

目前，Arduino 固件已在 GitHub 上基于 MIT 协议免费开源，而配套应用 DummyFanX 则通过 Gumroad 发售。

---

## 4. 帕姆·邦迪被免去总检察长职务

**原文标题**: Pam Bondi ousted as Attorney General

**原文链接**: [https://www.cnn.com/2026/04/02/politics/pam-bondi-role-trump](https://www.cnn.com/2026/04/02/politics/pam-bondi-role-trump)

总统唐纳德·特朗普已解除了帕姆·邦迪（Pam Bondi）的美国司法部长职务，并任命副司法部长托德·布兰奇（Todd Blanche）担任代理部长。尽管特朗普在Truth Social上公开赞扬了邦迪，称其将转任“私营部门的新职位”，并提到她任职期间犯罪率有所下降，但消息人士指出，此次解职的主要原因是总统对其表现感到不满。

主要撤职原因包括：

*   **政治起诉：** 据报道，特朗普对邦迪未能充分调查或起诉其政治对手感到沮丧。尽管司法部曾对前联邦调查局局长詹姆斯·科米和纽约州总检察长莱蒂西亚·詹姆斯提起诉讼，但由于负责检察官被判定为非法任职，两起案件均被撤销。
*   **爱泼斯坦案调查：** 内部对邦迪处理杰弗里·爱泼斯坦案卷的方式产生了分歧。她曾因公开声称桌上有一份“客户名单”而面临批评，但司法部随后澄清并不存在此类具体的名单。目前，她正因该事件面临众议院监督委员会的传票。
*   **布伦南调查案：** 据称，关于前中情局局长约翰·布伦南是否在2016年俄罗斯干预选举案中作虚假陈述的调查进展缓慢，这令特朗普感到恼火。

邦迪是继国土安全部长克里斯蒂·诺姆之后，近几周内第二位被撤职的内阁部长。消息人士透露，特朗普正考虑由环境保护局局长李·泽尔丁担任司法部长的正式继任者。据报道，在邦迪离职前，特朗普曾考虑为她提供一个司法职位的任命，但最终公告显示她将彻底离开政府部门。

---

## 5. SpaceX IPO：散户投资笔记

**原文标题**: The SpaceX IPO: retail investor notes

**原文链接**: [https://report.bearblog.dev/the-spacex-ipo-will-be-the-perfect-storm-of-retail-investor-fallacies/](https://report.bearblog.dev/the-spacex-ipo-will-be-the-perfect-storm-of-retail-investor-fallacies/)

文章**《SpaceX IPO：散户投资笔记》**探讨了未来 SpaceX（或 Starlink）公开募股时可能出现的心理陷阱。作者在承认 SpaceX 拥有真正技术霸权地位的同时，认为这次 IPO 将是一场散户投资者认知谬误的“完美风暴”，可能导致后来者遭受重大的财务损失。

核心要点包括：

*   **“马斯克因素”与好感偏差：** 散户的大量关注很大程度上是由围绕埃隆·马斯克的“个人崇拜”驱动的。这种偏差导致投资者为了表达对创始人的崇拜，而忽视了传统的财务指标。
*   **错失恐惧症 (FOMO) 与社会认同：** “人类的未来”和火星殖民的叙事营造了强烈的错失恐惧。作者指出，铺天盖地的媒体报道和社会认同将驱动散户不顾估值，以任何价格买入。
*   **叙事谬误：** 投资者往往沉向于 SpaceX 的“故事”，而忽视了星舰 (Starship) 和星链 (Starlink) 星座所需的巨额资本支出。作者警告说，如果买入价格过高，一家“革命性公司”并不能自动转化为一只“优质股票”。
*   **财富转移：** 文章认为，这次 IPO 很可能成为一个“退出事件”或财富转移手段，让早期风险投资人和内部人士在由散户热情推高的溢价中套现。
*   **锚定效应：** 散户投资者可能会将预期“锚定”在特斯拉的历史性崛起上，认为 SpaceX 会遵循相同的轨迹，却忽略了航空航天工业截然不同的市场动态和资本需求。

最后，作者警告说，虽然 SpaceX 是一家改变世界的公司，但其 IPO 注定会是一场感性事件，届时炒作和心理偏差极有可能导致股价与其基本面价值脱节。

---

## 6. 重塑 Pull Request

**原文标题**: Reinventing the Pull Request

**原文链接**: [https://lubeno.dev/blog/reinventing-the-pull-request](https://lubeno.dev/blog/reinventing-the-pull-request)

在《重塑 Pull Request》一文中，Luben Popov 指出，由 GitHub 普及的传统 Pull Request（PR）模式已成为现代软件工程的主要瓶颈。虽然 PR 最初是为异步开源协作而设计的，但它们往往会鼓励大型、单体式的代码变更，导致难以审查且合并缓慢，从而阻碍了快速的内部开发。

作者强调了现状的几个核心问题：
*   **高认知负荷：** 一次性审查数百行代码会导致审查者疲劳，并产生流于表面的 “LGTM”（看起来不错）式批准。
*   **同步阻塞：** 开发者在等待单个庞大分支的反馈时，经常被迫处于闲置状态或进行破坏性的上下文切换。
*   **集成复杂性：** 大型 PR 增加了合并冲突的可能性，并使识别 Bug 来源变得更加困难。

为了解决这些问题，文章提倡采用**堆栈式变更**（Stacked Changes，或称堆栈式 PR）。这种工作流将单个功能拆分为一系列小型、原子化且相互依赖的增量。开发者不再提交一个庞大的申请，而是提交由一系列相互关联的小型 Diff 组成的“堆栈”。

**该方法的主要优势包括：**
1.  **提高开发速度：** 开发者可以继续进行功能的后续开发，而无需等待之前的部分完成合并。
2.  **更高质量的审查：** 较小的变更更易于消化，从而带来更彻底、更有意义的反馈。
3.  **持续集成：** 该流程鼓励一种更流畅、流式的代码集成，而非“停停走走”的循环。

Popov 总结道，通过采用支持堆栈式变更的工具和工作流（如 Graphite 或专门的 CLI 工具），团队可以摆脱“合并或不合并”的二元思维，转向更高效、持续的开发生命周期。

---

## 7. New laws to make it easier to cancel subscriptions and get refunds

**原文标题**: New laws to make it easier to cancel subscriptions and get refunds

**原文链接**: [https://www.bbc.co.uk/news/articles/cvg0v36ek2go](https://www.bbc.co.uk/news/articles/cvg0v36ek2go)

生成摘要时出错

---

## 8. Artemis II astronaut finds two Outlook instances running on computers

**原文标题**: Artemis II astronaut finds two Outlook instances running on computers

**原文链接**: [https://www.tomshardware.com/software/microsoft-office/artemis-ii-astronaut-finds-two-outlook-instances-running-on-computers-call-on-houston-to-fix-microsoft-anomaly-puzzled-caller-describes-two-outlooks-and-neither-one-of-those-are-working](https://www.tomshardware.com/software/microsoft-office/artemis-ii-astronaut-finds-two-outlook-instances-running-on-computers-call-on-houston-to-fix-microsoft-anomaly-puzzled-caller-describes-two-outlooks-and-neither-one-of-those-are-working)

生成摘要时出错

---

## 9. What Gödel Discovered (2020)

**原文标题**: What Gödel Discovered (2020)

**原文链接**: [https://stopa.io/post/269](https://stopa.io/post/269)

生成摘要时出错

---

## 10. Order and Tension

**原文标题**: Order and Tension

**原文链接**: [https://slab.org/2026/03/22/order-and-tension/](https://slab.org/2026/03/22/order-and-tension/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 2 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 3 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 4 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 5 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 6 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 7 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 8 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 9 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 10 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 11 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 12 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 13 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 14 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 15 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 16 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 17 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 18 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 19 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 20 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 21 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 22 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 23 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 24 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 25 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 26 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 27 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 28 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 29 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 30 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 31 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 32 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 33 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 34 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 35 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 36 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 37 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 38 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 39 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 40 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 41 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 42 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 43 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 44 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 45 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 46 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 47 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 48 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 49 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 50 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 51 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 52 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 53 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 54 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 55 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 56 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 57 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 58 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 59 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 60 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 61 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 62 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 63 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 64 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 65 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 66 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 67 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 68 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 69 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 70 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 71 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 72 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 73 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 74 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 75 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 76 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 77 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 78 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 79 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 80 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 81 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 82 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 83 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 84 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 85 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 86 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 87 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 88 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 89 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 90 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 91 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 92 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 93 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 94 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 95 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 96 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 97 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 98 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 99 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 100 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 101 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 102 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 103 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 104 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 105 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 106 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 107 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 108 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 109 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 110 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 111 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 112 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 113 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 114 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 115 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 116 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 117 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 118 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 119 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 120 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 121 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 122 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 123 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 124 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 125 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 126 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 127 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 128 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 129 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 130 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 131 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 132 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 133 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 134 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 135 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 136 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 137 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 138 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 139 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 140 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 141 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 142 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 143 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 144 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 145 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 146 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 147 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 148 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 149 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 150 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 151 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 152 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 153 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 154 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 155 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 156 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 157 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 158 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 159 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 160 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 161 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 162 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 163 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 164 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 165 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 166 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 167 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 168 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 169 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 170 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 171 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 172 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 173 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 174 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 175 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 176 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 177 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 178 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 179 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 180 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 181 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 182 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 183 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 184 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 185 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 186 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 187 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 188 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 189 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 190 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 191 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 192 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 193 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 194 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 195 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 196 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 197 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 198 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 199 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 200 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 201 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 202 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 203 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 204 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 205 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 206 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 207 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 208 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 209 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 210 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 211 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 212 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 213 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 214 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 215 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 216 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 217 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 218 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 219 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 220 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 221 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 222 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 223 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 224 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 225 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 226 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 227 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 228 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 229 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 230 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 231 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 232 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 233 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 234 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 235 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 236 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 237 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 238 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 239 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 240 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 241 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 242 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 243 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 244 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 245 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 246 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 247 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 248 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 249 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 250 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 251 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 252 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 253 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 254 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 255 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 256 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 257 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 258 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 259 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 260 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 261 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 262 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 263 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 264 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 265 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 266 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 267 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 268 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 269 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 270 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 271 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 272 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 273 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 274 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 275 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 276 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 277 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 278 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 279 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 280 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 281 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 282 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 283 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 284 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 285 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 286 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 287 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 288 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 289 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 290 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 291 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 292 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 293 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 294 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 295 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 296 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 297 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 298 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 299 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 300 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 301 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 302 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 303 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 304 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 305 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 306 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 307 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 308 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 309 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 310 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 311 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 312 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 313 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 314 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 315 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 316 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 317 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 318 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 319 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 320 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 321 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 322 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 323 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 324 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 325 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 326 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 327 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 328 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 329 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 330 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 331 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 332 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 333 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 334 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 335 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 336 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 337 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 338 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 339 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 340 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 341 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 342 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 343 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 344 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 345 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 346 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 347 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 348 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 349 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 350 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 351 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 352 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 353 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 354 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 355 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 356 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 357 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 358 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 359 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 360 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 361 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 362 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 363 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 364 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 365 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 366 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 367 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 368 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 369 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 370 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 371 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 372 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 373 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 374 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 375 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 376 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 377 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 378 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
