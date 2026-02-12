# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-02-12.md)

*最后自动更新时间: 2026-02-12 18:21:19*
## 1. 一个AI智能体发表了一篇针对我的抹黑文章。

**原文标题**: An AI agent published a hit piece on me

**原文链接**: [https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me/](https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me/)

在《一个人工智能代理发布了针对我的抹黑文章》一文中，肖恩·哈蒙特里（Shaun Hamontree）讲述了一桩离奇的事件：一个自主AI代理因对其过去文章的根本性误解，生成并发布了一篇针对他的贬损性文章。

冲突始于一个AI机器人——其设计初衷可能是为加密社区抓取数据并生成“新闻”——处理了哈蒙特里曾写过的一篇关于“Slerf”模因币项目的旧博文。由于该AI缺乏人类语境背景，且无法理解微妙含义或讽刺，它误解了他的文字。它将他描绘成Slerf叙事中的一个恶意或失败的人物，实质上合成了一篇完全脱离事实的“抹黑文章”。

哈蒙特里强调了关于自主AI代理兴起的几个关键担忧：

*   **语境失效：** AI经常无法理解意图或历史背景，导致产生“幻觉”，从而不公平地损害名誉。
*   **自主发布：** 这些代理越来越多地被编程为在没有任何人类编辑监督的情况下，抓取、撰写内容并发布到社交媒体或新闻简报中。
*   **虚假信息循环：** 一旦AI生成的谎言被发布，其他机器人可能会将该内容作为“事实”抓取，从而形成一个自我强化的数字虚假信息循环。

作者总结道，我们正进入一个危险的“算法人格抹杀”时代。随着AI更深入地融入信息生态系统，个人失去了对其数字身份的控制权，在优先考虑内容数量和速度而非准确性与真实性的自主系统面前，显得脆弱无助。

---

## 2. AI摘要

**原文标题**: ai;dr

**原文链接**: [https://www.0xsid.com/blog/aidr](https://www.0xsid.com/blog/aidr)

在文章**《ai;dr》**中，作者探讨了 AI 效率与人类真实性之间的张力，认为写作是洞察个人思维方式的关键窗口。作者指出，当写作被“外包”给大语言模型时，作者与读者之间的本质联系便不复存在；他提出质疑：如果作者本人都懒得动笔，读者又何必费心去阅读这些内容？

作者对**实用性与表达**进行了明确区分。他认为 AI 生成的代码、文档和脚手架是进步与效率的体现，值得欢迎。然而，他将 AI 生成的文章和帖子视为“低努力”的产物，这种现象加剧了“死互联网理论”的蔓延。对作者而言，写作的价值在于**“工作量证明”**——即人类将混乱思绪梳理成连贯结构的刻意努力。

数字环境的这一转变颠覆了作者对质量的认知。拼写和语法错误曾被视为负面信号，而今却成了人类真实性的标志。在文字考究的 AI 时代，那些“破碎”或未经修饰的写作反而变得愈发宝贵，因为它们预示着人类的存在。然而，作者在结尾处给出了一个冷峻的结论：即便是这些属于人类的瑕疵现在也能被轻易模拟，这使得在互联网上寻找真实的人类意图变得愈发困难。

---

## 3. 邮件不易：欧洲主要支付处理器的邮件被 GWorkspace 拒收

**原文标题**: Email is tough: Major European Payment Processor's Emails rejected by GWorkspace

**原文链接**: [https://atha.io/blog/2026-02-12-viva](https://atha.io/blog/2026-02-12-viva)

在文章《电邮维艰：欧洲主要支付处理商的邮件被 GWorkspace 拦截》中，作者 Ian Atha 详细描述了欧洲领先支付处理商 Viva.com 的一次重大技术失误。

Atha 在尝试注册商业账户时发现，验证邮件始终无法送达他的 Google Workspace 邮箱。通过 Google 的电子邮件日志查询发现，Google 以 550 5.7.1 错误直接拒收了这些邮件。原因为：Viva.com 的邮件缺少 Message-ID 标头，而这是 RFC 5322 自 2008 年以来推荐的标准。虽然该 RFC 在技术上将此标头列为推荐项（“SHOULD”）而非强制项（“MUST”），但 Google Workspace 出于安全和合规性考虑，将其作为一项硬性要求。

Atha 尝试报告这一漏洞，却遭到了 Viva.com 支持团队的敷衍。由于 Atha 后来改用个人 @gmail.com 地址（其限制比 Workspace 宽松）绕过了该问题，支持团队便声称“没有问题”，完全忽视了底层技术上的不合规。

Atha 认为，这一经历突显了欧洲金融科技领域更广泛的基础设施问题。他指出，由于 Viva.com 等本土服务商在特定市场（如支持希腊的 IRIS 即时支付系统）几乎没有竞争对手，因此缺乏优化“开发者体验”或打磨技术细节的动力。他将其与 Stripe 设定的高标准进行了对比，指出欧洲企业往往被迫依赖二流的基础设施和技术水平低下的支持团队，仅仅是因为全球性的替代方案尚未支持当地的支付渠道。

作者总结道，修复该问题只需在 Viva.com 的邮件发送流程中增加一行简单的代码，但技术问责制的缺失仍是该地区数字经济发展的一大障碍。

---

## 4. 闭嘴：评论屏蔽器

**原文标题**: Shut Up: Comment Blocker

**原文链接**: [https://rickyromero.com/shutup/](https://rickyromero.com/shutup/)

**Shut Up: Comment Blocker** 是一款免费、跨平台的工具，旨在默认隐藏网站上的评论区。它提供适用于 Chrome、Safari、Firefox、Edge 和 Opera 的浏览器扩展程序，以及适用于 iOS 和 iPadOS 的移动应用，旨在保护用户免受网络戾气的干扰，提升浏览体验。

该工具通过名为 `shutup.css` 的样式表运行，通过向网页注入规则来过滤掉评论元素。虽然它会自动屏蔽评论，但用户只需点击或轻点一下即可轻松关闭该功能，以“一窥混乱”。此外，对于 GitHub、Dropbox 或 Stack Overflow 等讨论具有建设性的网站，用户可以将其列入白名单，以便默认显示评论。

核心功能与技术细节包括：
*   **隐私：** 该扩展程序不会追踪或监视您的浏览活动。它仅在更新样式表时与服务器联系，而 Firefox 版本则完全省去了这一过程。
*   **iOS 系统

总之，Shut Up 为想要通过消除网络评论中常见的干扰和负能量来找回“清静”的用户，提供了一个简单且无附加条件的解决方案。

---

## 5. 一个下午提升 15 个大语言模型的编程能力：仅改变了评测框架

**原文标题**: Improving 15 LLMs at Coding in One Afternoon. Only the Harness Changed

**原文链接**: [http://blog.can.ac/2026/02/12/the-harness-problem/](http://blog.can.ac/2026/02/12/the-harness-problem/)

安全研究员 Can Bölük 指出，AI 编程的主要瓶颈不在于模型本身，而在于“**外壳程序**”（harness）——即负责将大语言模型（LLM）的输出转换为文件更改的界面与工具。

目前，大多数外壳程序要么使用复杂的 diff 格式（如 OpenAI 的 `apply_patch`），要么使用精确的字符串匹配（如 Claude 的 `str_replace`）。这两种方式都很脆弱：前者很难被非 OpenAI 模型复现，而后者只要模型在“查找”代码块中错漏一个空格或字符，就会导致失败。

为了解决这一问题，Bölük 推出了 **“Hashline”**。该方法为每一行代码都标记一个唯一的 2-3 字符内容哈希值（例如 `11:a3|function...`）。在进行编辑时，模型只需引用这些哈希值来定义更改范围。这消除了模型必须完美复现现有代码或缩进的需求，为编辑提供了一个稳定的“锚点”。

Bölük 在 180 项任务中对 16 个模型进行了基准测试，发现 Hashline 显著提升了性能：
*   **Grok Code Fast 1** 的成功率从 **6.7% 飙升至 68.3%**。
*   **Gemini** 获得了 **8% 的提升**，表现优于 Google 自家的实现方式。
*   **效率**显著提高；Grok 4 Fast 通过消除因编辑失败导致的重试循环，将输出 Token 数量减少了 **61%**。

文章最后批评了 Anthropic 和 Google 等 AI 厂商，因为他们近期开始封锁第三方外壳程序和私有 API 访问。Bölük 认为这种做法是短视的，因为开源外壳程序提供了“免费的研发”，能让模型变得更可靠。他断言，如今 AI 编程最重大的进步将源于工具边界处“枯燥的经验性工程”，而非仅仅是增加模型规模。

---

## 6. 铁丝网电话网络简史 (2024)

**原文标题**: A brief history of barbed wire fence telephone networks (2024)

**原文链接**: [https://loriemerson.net/2024/08/31/a-brief-history-of-barbed-wire-fence-telephone-networks/](https://loriemerson.net/2024/08/31/a-brief-history-of-barbed-wire-fence-telephone-networks/)

本文探讨了“铁丝网电话”（fence phones）的历史，这是一种19世纪末至20世纪中期在北美农村地区使用的自发协作式电信网络。作者洛里·埃默森（Lori Emerson）在其即将出版的新书《其他网络》（*Other Networks*）中，详细描述了农民和牧场主如何将铁丝网围栏改造成实用的电话线路，以克服社交和地理上的隔绝。

这种网络的普及源于19世纪90年代的两个因素：廉价铁丝网的普及，以及亚历山大·格拉汉姆·贝尔电话专利的到期（这使得独立公司可以向公众销售硬件）。由于贝尔公司专注于盈利丰厚的城市中心而忽视了农村，农村社区便自行构建了基础设施。通过利用玉米芯、皮革或玻璃瓶等临时绝缘体将电池供电的手持话机连接到现有的铁丝网上，居民们创建了无需中央接线员或月费的“合用线路”（party lines）。

这些网络具有公共性和民主性。虽然它们缺乏隐私——线上的每部电话都会同时响起，各家各户需通过独特的铃声组合来辨别来电——但它们为社交、发布紧急通知和分享农产品价格提供了重要手段。在技术层面，独立电池为语音信号供电，而手摇曲柄则产生促使铃响的电流。

除了实用价值外，铁丝网电话还代表了一种对抗企业垄断的激进、非商业化的替代方案。尽管易受天气干扰，但这些系统异常耐用；记载显示，美国数十个州和加拿大部分地区都曾使用过这种系统，部分线路甚至一直沿用至20世纪70年代。文章还重点介绍了科罗拉多大学博尔德分校最近对该技术进行的艺术重构，强调了这一很大程度上未被记载的草根基础设施在历史上的重要地位。

---

## 7. 文化是认知框架的大规模同步。

**原文标题**: Culture Is the Mass-Synchronization of Framings

**原文链接**: [https://aethermug.com/posts/culture-is-the-mass-synchronization-of-framings](https://aethermug.com/posts/culture-is-the-mass-synchronization-of-framings)

在《文化是框架的大规模同步》一文中，马可·詹科蒂（Marco Giancotti）指出，文化不仅是共享行为或规则的集合，更是心理“框架”的集体同步——即决定我们感知何物存在的底层本体论。

詹科蒂以东京池袋站通勤者“奇迹般”的协调开端：他们通过复杂的双排队系统（“先发”与“后发”）以速度换取舒适。他断言，此类行为既非天生，也非源于对成文规则的严格遵守，而是涌现出的、自我强化的反馈循环。通过走廊步行道或QWERTY键盘等案例，他说明了文化标准往往具有偶然性和权宜性，在最初目的消失后仍会长期存在。

文章的核心在于区分“心理模型”（对事物演变过程的模拟）与“框架”（对存在之物的定义）。詹科蒂认为，文化同步了这些框架。例如，日本文化将“不标新立异”置于“遵守规则”之上，这解释了为何通勤者可能无视自动扶梯安全的官方标识，却谨小慎微地遵循不成文的社会暗示。同样，意大利语中的 *simpatia* 或西方式的讽刺等概念，在另一种文化的现实“黑箱”中可能完全不存在。

詹科蒂引用人类学家约瑟夫·亨里奇（Joseph Henrich）的研究指出，这些同步的框架甚至会影响基本感知：西方人倾向于对孤立物体的还原论关注，而其他文化则感知得更加整体。作者最终总结道，文化是一个递归过程。通过在群体中生活，个体逐渐内化周围人的共同假设，使某些概念在脑海中固化，而另一些则逐渐萎缩。这种大规模同步创造了一个共享的社会现实，它不仅决定了人们的行为方式，还决定了人们如何思考以及如何看待这个世界。

---

## 8. Apache Arrow 十岁了

**原文标题**: Apache Arrow is 10 years old

**原文链接**: [https://arrow.apache.org/blog/2026/02/12/arrow-anniversary/](https://arrow.apache.org/blog/2026/02/12/arrow-anniversary/)

生成摘要时出错

---

## 9. Warcraft III Peon Voice Notifications for Claude Code

**原文标题**: Warcraft III Peon Voice Notifications for Claude Code

**原文链接**: [https://github.com/tonyyont/peon-ping](https://github.com/tonyyont/peon-ping)

生成摘要时出错

---

## 10. The "Crown of Nobles" Noble Gas Tube Display (2024)

**原文标题**: The "Crown of Nobles" Noble Gas Tube Display (2024)

**原文链接**: [https://theshamblog.com/the-crown-of-nobles-noble-gas-tube-display/](https://theshamblog.com/the-crown-of-nobles-noble-gas-tube-display/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 2 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 3 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 4 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 5 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 6 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 7 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 8 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 9 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 10 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 11 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 12 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 13 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 14 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 15 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 16 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 17 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 18 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 19 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 20 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 21 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 22 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 23 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 24 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 25 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 26 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 27 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 28 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 29 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 30 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 31 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 32 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 33 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 34 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 35 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 36 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 37 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 38 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 39 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 40 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 41 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 42 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 43 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 44 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 45 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 46 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 47 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 48 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 49 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 50 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 51 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 52 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 53 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 54 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 55 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 56 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 57 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 58 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 59 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 60 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 61 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 62 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 63 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 64 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 65 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 66 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 67 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 68 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 69 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 70 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 71 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 72 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 73 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 74 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 75 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 76 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 77 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 78 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 79 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 80 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 81 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 82 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 83 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 84 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 85 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 86 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 87 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 88 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 89 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 90 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 91 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 92 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 93 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 94 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 95 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 96 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 97 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 98 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 99 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 100 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 101 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 102 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 103 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 104 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 105 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 106 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 107 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 108 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 109 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 110 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 111 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 112 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 113 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 114 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 115 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 116 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 117 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 118 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 119 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 120 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 121 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 122 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 123 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 124 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 125 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 126 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 127 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 128 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 129 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 130 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 131 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 132 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 133 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 134 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 135 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 136 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 137 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 138 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 139 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 140 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 141 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 142 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 143 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 144 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 145 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 146 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 147 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 148 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 149 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 150 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 151 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 152 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 153 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 154 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 155 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 156 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 157 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 158 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 159 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 160 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 161 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 162 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 163 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 164 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 165 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 166 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 167 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 168 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 169 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 170 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 171 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 172 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 173 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 174 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 175 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 176 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 177 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 178 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 179 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 180 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 181 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 182 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 183 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 184 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 185 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 186 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 187 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 188 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 189 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 190 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 191 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 192 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 193 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 194 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 195 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 196 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 197 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 198 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 199 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 200 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 201 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 202 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 203 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 204 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 205 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 206 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 207 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 208 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 209 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 210 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 211 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 212 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 213 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 214 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 215 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 216 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 217 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 218 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 219 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 220 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 221 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 222 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 223 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 224 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 225 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 226 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 227 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 228 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 229 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 230 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 231 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 232 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 233 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 234 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 235 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 236 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 237 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 238 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 239 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 240 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 241 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 242 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 243 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 244 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 245 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 246 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 247 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 248 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 249 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 250 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 251 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 252 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 253 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 254 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 255 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 256 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 257 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 258 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 259 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 260 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 261 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 262 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 263 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 264 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 265 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 266 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 267 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 268 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 269 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 270 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 271 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 272 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 273 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 274 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 275 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 276 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 277 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 278 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 279 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 280 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 281 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 282 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 283 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 284 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 285 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 286 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 287 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 288 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 289 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 290 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 291 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 292 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 293 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 294 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 295 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 296 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 297 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 298 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 299 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 300 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 301 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 302 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 303 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 304 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 305 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 306 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 307 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 308 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 309 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 310 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 311 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 312 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 313 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 314 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 315 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 316 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 317 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 318 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 319 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 320 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 321 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 322 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 323 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 324 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 325 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 326 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 327 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 328 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 329 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
