# Hacker News 热门文章摘要 (2026-04-02)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Show HN: Dull – Instagram Without Reels, YouTube Without Shorts (iOS)

**原文标题**: Show HN: Dull – Instagram Without Reels, YouTube Without Shorts (iOS)

**原文链接**: [https://getdull.app](https://getdull.app)

生成摘要时出错

---

## 12. Show HN: I built a DNS resolver from scratch in Rust – no DNS libraries

**原文标题**: Show HN: I built a DNS resolver from scratch in Rust – no DNS libraries

**原文链接**: [https://github.com/razvandimescu/numa](https://github.com/razvandimescu/numa)

生成摘要时出错

---

## 13. Things I Think I Think... Preferring Local OSS LLMs

**原文标题**: Things I Think I Think... Preferring Local OSS LLMs

**原文链接**: [https://blogs.newardassociates.com/blog/2026/titit-local-ai.html](https://blogs.newardassociates.com/blog/2026/titit-local-ai.html)

生成摘要时出错

---

## 14. Almighty Lisp: Lisp and Emacs Essentials Book

**原文标题**: Almighty Lisp: Lisp and Emacs Essentials Book

**原文链接**: [https://almightylisp.com/](https://almightylisp.com/)

生成摘要时出错

---

## 15. Japanese X is now America's favorite corner of the internet

**原文标题**: Japanese X is now America's favorite corner of the internet

**原文链接**: [https://www.japantimes.co.jp/commentary/2026/04/01/japan/japanese-x-now-americas-favorite/](https://www.japantimes.co.jp/commentary/2026/04/01/japan/japanese-x-now-americas-favorite/)

生成摘要时出错

---

## 16. Quantum computing bombshells that are not April Fools

**原文标题**: Quantum computing bombshells that are not April Fools

**原文链接**: [https://scottaaronson.blog/?p=9665](https://scottaaronson.blog/?p=9665)

生成摘要时出错

---

## 17. ReactOS Shows Improved Stability and 64-Bit Support at Chemnitz Linux Days 2026

**原文标题**: ReactOS Shows Improved Stability and 64-Bit Support at Chemnitz Linux Days 2026

**原文链接**: [https://old.reddit.com/r/reactos/comments/1sa26yu/back_from_chemnitz_linux_days_2026/](https://old.reddit.com/r/reactos/comments/1sa26yu/back_from_chemnitz_linux_days_2026/)

生成摘要时出错

---

## 18. Reverse Engineering Crazy Taxi, Part 2

**原文标题**: Reverse Engineering Crazy Taxi, Part 2

**原文链接**: [https://wretched.computer/post/crazytaxi2](https://wretched.computer/post/crazytaxi2)

生成摘要时出错

---

## 19. EmDash – A spiritual successor to WordPress that solves plugin security

**原文标题**: EmDash – A spiritual successor to WordPress that solves plugin security

**原文链接**: [https://blog.cloudflare.com/emdash-wordpress/](https://blog.cloudflare.com/emdash-wordpress/)

生成摘要时出错

---

## 20. The revenge of the data scientist

**原文标题**: The revenge of the data scientist

**原文链接**: [https://hamel.dev/blog/posts/revenge/](https://hamel.dev/blog/posts/revenge/)

生成摘要时出错

---

## 21. Trap a quantum object in a box – is it hard or soft, or is it black or white?

**原文标题**: Trap a quantum object in a box – is it hard or soft, or is it black or white?

**原文链接**: [https://paradigmsage.com/pop/ch-04-qm/](https://paradigmsage.com/pop/ch-04-qm/)

生成摘要时出错

---

## 22. SpaceX files to go public

**原文标题**: SpaceX files to go public

**原文链接**: [https://www.nytimes.com/2026/04/01/technology/spacex-ipo-elon-musk.html](https://www.nytimes.com/2026/04/01/technology/spacex-ipo-elon-musk.html)

生成摘要时出错

---

## 23. CC leak: skills are better than I thought

**原文标题**: CC leak: skills are better than I thought

**原文链接**: [https://www.dardar.co/articles/skills-arent-just-context](https://www.dardar.co/articles/skills-arent-just-context)

生成摘要时出错

---

## 24. Quad9 Enables DNS over HTTP/3 and DNS over QUIC

**原文标题**: Quad9 Enables DNS over HTTP/3 and DNS over QUIC

**原文链接**: [https://quad9.net/news/blog/quad9-enables-dns-over-http-3-and-dns-over-quic/](https://quad9.net/news/blog/quad9-enables-dns-over-http-3-and-dns-over-quic/)

生成摘要时出错

---

## 25. The Weather Channel – RetroCast

**原文标题**: The Weather Channel – RetroCast

**原文链接**: [https://weather.com/retro/](https://weather.com/retro/)

生成摘要时出错

---

## 26. Protecting Your Host from Malicious Dependencies

**原文标题**: Protecting Your Host from Malicious Dependencies

**原文链接**: [https://www.grepular.com/Protecting_Your_Host_from_Malicious_Dependencies](https://www.grepular.com/Protecting_Your_Host_from_Malicious_Dependencies)

生成摘要时出错

---

## 27. DRAM pricing is killing the hobbyist SBC market

**原文标题**: DRAM pricing is killing the hobbyist SBC market

**原文链接**: [https://www.jeffgeerling.com/blog/2026/dram-pricing-is-killing-the-hobbyist-sbc-market/](https://www.jeffgeerling.com/blog/2026/dram-pricing-is-killing-the-hobbyist-sbc-market/)

生成摘要时出错

---

## 28. A new C++ back end for ocamlc

**原文标题**: A new C++ back end for ocamlc

**原文链接**: [https://github.com/ocaml/ocaml/pull/14701](https://github.com/ocaml/ocaml/pull/14701)

生成摘要时出错

---

## 29. Fast and Gorgeous Erosion Filter

**原文标题**: Fast and Gorgeous Erosion Filter

**原文链接**: [https://blog.runevision.com/2026/03/fast-and-gorgeous-erosion-filter.html](https://blog.runevision.com/2026/03/fast-and-gorgeous-erosion-filter.html)

生成摘要时出错

---

## 30. CERN levels up with new superconducting karts

**原文标题**: CERN levels up with new superconducting karts

**原文链接**: [https://home.cern/news/news/engineering/cern-levels-new-superconducting-karts](https://home.cern/news/news/engineering/cern-levels-new-superconducting-karts)

生成摘要时出错

---

## 31. Show HN: Zerobox – Sandbox any command with file, network, credential controls

**原文标题**: Show HN: Zerobox – Sandbox any command with file, network, credential controls

**原文链接**: [https://github.com/afshinm/zerobox](https://github.com/afshinm/zerobox)

生成摘要时出错

---

## 32. Windows 95 defenses against installers that overwrite a file with an older one

**原文标题**: Windows 95 defenses against installers that overwrite a file with an older one

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20260324-00/?p=112159](https://devblogs.microsoft.com/oldnewthing/20260324-00/?p=112159)

生成摘要时出错

---

## 33. Nvidia rolls out its fix for PC gaming's "compiling shaders" wait times

**原文标题**: Nvidia rolls out its fix for PC gaming's "compiling shaders" wait times

**原文链接**: [https://arstechnica.com/gaming/2026/04/nvidias-new-app-lets-you-precompile-gaming-shaders-during-machine-idle-time/](https://arstechnica.com/gaming/2026/04/nvidias-new-app-lets-you-precompile-gaming-shaders-during-machine-idle-time/)

生成摘要时出错

---

## 34. Is BGP safe yet?

**原文标题**: Is BGP safe yet?

**原文链接**: [https://isbgpsafeyet.com/](https://isbgpsafeyet.com/)

生成摘要时出错

---

## 35. Gemma 4: Byte for byte, the most capable open models

**原文标题**: Gemma 4: Byte for byte, the most capable open models

**原文链接**: [https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/)

生成摘要时出错

---

## 36. Ubuntu Mate Leader Stepping Down, Seeking New Contributors

**原文标题**: Ubuntu Mate Leader Stepping Down, Seeking New Contributors

**原文链接**: [https://www.phoronix.com/news/Ubuntu-MATE-Needs-Leader](https://www.phoronix.com/news/Ubuntu-MATE-Needs-Leader)

生成摘要时出错

---

## 37. Signing data structures the wrong way

**原文标题**: Signing data structures the wrong way

**原文链接**: [https://blog.foks.pub/posts/domain-separation-in-idl/](https://blog.foks.pub/posts/domain-separation-in-idl/)

生成摘要时出错

---

## 38. Apple removes iPhone vibe coding app from app store

**原文标题**: Apple removes iPhone vibe coding app from app store

**原文链接**: [https://gizmodo.com/apple-removes-iphone-vibe-coding-app-from-app-store-2000740084](https://gizmodo.com/apple-removes-iphone-vibe-coding-app-from-app-store-2000740084)

生成摘要时出错

---

## 39. OpenAI closes funding round at an $852B valuation

**原文标题**: OpenAI closes funding round at an $852B valuation

**原文链接**: [https://www.cnbc.com/2026/03/31/openai-funding-round-ipo.html](https://www.cnbc.com/2026/03/31/openai-funding-round-ipo.html)

生成摘要时出错

---

## 40. Bring Back MiniDV with This Raspberry Pi FireWire Hat

**原文标题**: Bring Back MiniDV with This Raspberry Pi FireWire Hat

**原文链接**: [https://www.jeffgeerling.com/blog/2026/minidv-with-raspberry-pi-firewire-hat/](https://www.jeffgeerling.com/blog/2026/minidv-with-raspberry-pi-firewire-hat/)

生成摘要时出错

---

## 41. Tracing goroutines in realtime with eBPF

**原文标题**: Tracing goroutines in realtime with eBPF

**原文链接**: [https://sazak.io/articles/tracing-goroutines-in-realtime-with-ebpf-2026-03-31](https://sazak.io/articles/tracing-goroutines-in-realtime-with-ebpf-2026-03-31)

生成摘要时出错

---

## 42. Article about simple LSB steganography in JavaScript

**原文标题**: Article about simple LSB steganography in JavaScript

**原文链接**: [https://www.yourdev.net/blog.php?post=steganography-hiding-data-in-images](https://www.yourdev.net/blog.php?post=steganography-hiding-data-in-images)

生成摘要时出错

---

## 43. Claude wrote a full FreeBSD remote kernel RCE with root shell

**原文标题**: Claude wrote a full FreeBSD remote kernel RCE with root shell

**原文链接**: [https://github.com/califio/publications/blob/main/MADBugs/CVE-2026-4747/write-up.md](https://github.com/califio/publications/blob/main/MADBugs/CVE-2026-4747/write-up.md)

生成摘要时出错

---

## 44. How-to guide: Commissioning a Sensor Physics R&D Lab

**原文标题**: How-to guide: Commissioning a Sensor Physics R&D Lab

**原文链接**: [https://gist.github.com/nup002/912383615b12dc1ec44ae9004c40b11f](https://gist.github.com/nup002/912383615b12dc1ec44ae9004c40b11f)

生成摘要时出错

---

## 45. From 300KB to 69KB per Token: How LLM Architectures Solve the KV Cache Problem

**原文标题**: From 300KB to 69KB per Token: How LLM Architectures Solve the KV Cache Problem

**原文链接**: [https://news.future-shock.ai/the-weight-of-remembering/](https://news.future-shock.ai/the-weight-of-remembering/)

生成摘要时出错

---

## 46. Solar Balconies Take Europe by Storm

**原文标题**: Solar Balconies Take Europe by Storm

**原文链接**: [https://hackaday.com/2026/03/31/solar-balconies-take-europe-by-storm/](https://hackaday.com/2026/03/31/solar-balconies-take-europe-by-storm/)

生成摘要时出错

---

## 47. A dot a day keeps the clutter away

**原文标题**: A dot a day keeps the clutter away

**原文链接**: [https://scottlawsonbc.com/post/dot-system](https://scottlawsonbc.com/post/dot-system)

生成摘要时出错

---

## 48. Teenage Engineering's PO-32 acoustic modem and synth implementation

**原文标题**: Teenage Engineering's PO-32 acoustic modem and synth implementation

**原文链接**: [https://github.com/ericlewis/libpo32](https://github.com/ericlewis/libpo32)

生成摘要时出错

---

## 49. IPv6 address, as a sentence you can remember

**原文标题**: IPv6 address, as a sentence you can remember

**原文链接**: [https://sentence2ipv6.tib3rius.com/](https://sentence2ipv6.tib3rius.com/)

生成摘要时出错

---

## 50. Default GraphQL response is now HTTP 500

**原文标题**: Default GraphQL response is now HTTP 500

**原文链接**: [https://graphql.org/blog/2026-04-01-a-new-era-for-graphql-observability/](https://graphql.org/blog/2026-04-01-a-new-era-for-graphql-observability/)

生成摘要时出错

---

## 51. StepFun 3.5 Flash is #1 cost-effective model for OpenClaw tasks (300 battles)

**原文标题**: StepFun 3.5 Flash is #1 cost-effective model for OpenClaw tasks (300 battles)

**原文链接**: [https://app.uniclaw.ai/arena?tab=costEffectiveness&via=hn](https://app.uniclaw.ai/arena?tab=costEffectiveness&via=hn)

生成摘要时出错

---

## 52. Show HN: Postgres extension for BM25 relevance-ranked full-text search

**原文标题**: Show HN: Postgres extension for BM25 relevance-ranked full-text search

**原文链接**: [https://github.com/timescale/pg_textsearch](https://github.com/timescale/pg_textsearch)

生成摘要时出错

---

## 53. Cohere Transcribe: Speech Recognition

**原文标题**: Cohere Transcribe: Speech Recognition

**原文链接**: [https://cohere.com/blog/transcribe](https://cohere.com/blog/transcribe)

生成摘要时出错

---

## 54. An Introduction to Writing Systems and Unicode

**原文标题**: An Introduction to Writing Systems and Unicode

**原文链接**: [https://r12a.github.io/scripts/tutorial/part2](https://r12a.github.io/scripts/tutorial/part2)

生成摘要时出错

---

## 55. Ordinary Lab Gloves May Have Skewed Microplastic Data

**原文标题**: Ordinary Lab Gloves May Have Skewed Microplastic Data

**原文链接**: [https://nautil.us/ordinary-lab-gloves-may-have-skewed-microplastic-data-1279386](https://nautil.us/ordinary-lab-gloves-may-have-skewed-microplastic-data-1279386)

生成摘要时出错

---

## 56. Vitalik Buterin – "My self-sovereign / local / private / secure LLM setup"

**原文标题**: Vitalik Buterin – "My self-sovereign / local / private / secure LLM setup"

**原文链接**: [https://vitalik.eth.limo/general/2026/04/02/secure_llms.html](https://vitalik.eth.limo/general/2026/04/02/secure_llms.html)

生成摘要时出错

---

## 57. UK Government unveils rules to end subscription traps

**原文标题**: UK Government unveils rules to end subscription traps

**原文链接**: [https://www.gov.uk/government/news/consumers-to-save-around-400-million-every-year-from-government-crackdown-on-costly-subscription-traps](https://www.gov.uk/government/news/consumers-to-save-around-400-million-every-year-from-government-crackdown-on-costly-subscription-traps)

生成摘要时出错

---

## 58. Swappa.com for GrapheneOS compatible devices – Stay Away

**原文标题**: Swappa.com for GrapheneOS compatible devices – Stay Away

**原文链接**: [https://discuss.grapheneos.org/d/33727-swappacom-for-grapheneos-compatible-devices-stay-away](https://discuss.grapheneos.org/d/33727-swappacom-for-grapheneos-compatible-devices-stay-away)

生成摘要时出错

---

## 59. Salomi, a research repo on extreme low-bit transformer quantization

**原文标题**: Salomi, a research repo on extreme low-bit transformer quantization

**原文链接**: [https://github.com/OrionsLock/SALOMI](https://github.com/OrionsLock/SALOMI)

生成摘要时出错

---

