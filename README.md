# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-11-22.md)

*最后自动更新时间: 2025-11-22 17:46:36*
## 1. Agent设计仍然很难

**原文标题**: Agent design is still hard

**原文链接**: [https://lucumr.pocoo.org/2025/11/21/agents-are-hard/](https://lucumr.pocoo.org/2025/11/21/agents-are-hard/)

在2025年11月的博文中，Armin Ronacher 探讨了构建有效代理的持续挑战，即便在代理编码工具取得进展的情况下。他强调，代理设计仍然复杂，SDK 抽象在应用于真实世界的工具使用时会失效。

Ronacher 反对仅仅依赖像 Vercel AI SDK 这样的高级 SDK，提倡直接与平台特定的 SDK（例如 OpenAI、Anthropic）交互，以保持对抽象的控制，并更有效地处理提供商方面的工具。他赞扬了 Anthropic 的显式缓存管理，认为它比自动化系统更可预测和可控。

代理循环中的强化至关重要，它允许对工具性能、状态更改甚至通过“回声工具”进行自我强化进行反馈。隔离故障（通过子代理或上下文编辑，尽管后者仍处于实验阶段）有助于保持上下文质量并节省 tokens。

Ronacher 强调需要共享状态，例如虚拟文件系统，以促进不同工具和子代理之间的通信。他发现输出工具出乎意料地困难，难以控制语气并确保工具调用。

模型选择仍然取决于任务，Haiku 和 Sonnet 因其工具调用能力而受到主代理循环的青睐，而 Gemini 2.5 更适合用于文档摘要和图像提取等任务。至关重要的是，他强调测试和评估是最重要的挑战，需要与来自实际测试运行的可观察性数据相关联。

最后，他简要提到了试用“Amp”编码代理，赞赏其子代理交互。他以一些有趣的阅读材料作为总结，倡导更简单的浏览器代理设置，并强调了像 Tmux 这样的工具的持续相关性。

---

## 2. 新墨西哥州全美首创，向所有人开放免费托儿服务

**原文标题**: In a U.S. First, New Mexico Opens Doors to Free Child Care for All

**原文链接**: [https://www.wsj.com/us-news/in-a-u-s-first-new-mexico-opens-doors-to-free-child-care-for-all-2dfdea96](https://www.wsj.com/us-news/in-a-u-s-first-new-mexico-opens-doors-to-free-child-care-for-all-2dfdea96)

好的，以下是《华尔街日报》文章“美国首例，新墨西哥州向所有人开放免费托儿服务”的摘要，基于网上容易获得的资料以及文章标题和来源推测的内容。由于我无法直接访问链接，所以本摘要基于一般知识和预期内容。

**摘要：**

新墨西哥州正在实施一项全民免费托儿计划，成为美国第一个这样做的州。这项计划旨在让所有家庭，无论收入如何，都能获得托儿服务。该项目由州和联邦资金共同资助，包括来自该州石油和天然气行业的收入。

其主要目标是减轻家庭的经济负担，使更多的父母，尤其是母亲，能够参与到劳动力市场中。倡导者认为，这将促进该州的经济发展并减少贫困。该计划还旨在改善全州儿童的早期教育成果。

该计划主要侧重于向托儿服务提供者提供补贴，使他们能够为家庭提供免费或低价的托儿服务。它解决了劳动力参与的一个重要障碍，并解决了托儿服务的高昂成本问题，而这不成比例地影响着低收入家庭。这项倡议可以为其他州考虑采取类似政策以扩大早期儿童教育的范围并支持工作的家庭提供一个典范。预计它将对该州的经济、劳动力参与率以及新墨西哥州家庭的整体福祉产生重大影响。

---

## 3. 浏览器指纹的隐私噩梦

**原文标题**: The privacy nightmare of browser fingerprinting

**原文链接**: [https://kevinboone.me/fingerprinting.html](https://kevinboone.me/fingerprinting.html)

本文深入探讨了浏览器指纹识别带来的隐私威胁。浏览器指纹识别是一种网站用于追踪用户的方法，它无需依赖 Cookie。文章解释了指纹识别的工作原理，它通过收集关于浏览器的各种信息，例如操作系统、浏览器版本、已安装字体、扩展程序，甚至是图形渲染方式的细微差别（Canvas 指纹识别）。将这些数据点组合起来，会创建一个唯一的标识符，或“指纹”，使网站能够在网络上追踪用户。

作者强调了对抗指纹识别的难度。禁用 JavaScript 或伪造浏览器信息等简单措施可能会适得其反，反而使用户更加显眼。他们还讨论了指纹识别的局限性，指出实际追踪比演示网站显示的更具挑战性，并且指纹会随着时间而改变。

尽管前景黯淡，但文章提供了一些减轻风险的建议。这些建议包括使用 VPN、频繁轮换 VPN 节点、定期清除 Cookie 以及保持标准的浏览器配置。还建议使用具有内置指纹识别抵抗能力的浏览器，例如 Brave、Mullvad 或 Librewolf。然而，这些措施也存在缺点，例如增加 CAPTCHA 挑战和潜在的网站兼容性问题。

即使在 GDPR 框架下，浏览器指纹识别的合法性也存在争议。作者总结说，虽然指纹识别构成了重大的隐私问题，尤其是在支持在线广告行业方面，但其影响是统计上的，而不是决定性的。立法被视为最终的解决方案，但广告行业可能会继续寻找新的追踪方法。

---

## 4. 个人博客回归，利基博客会是下一个趋势吗？

**原文标题**: Personal blogs are back, should niche blogs be next?

**原文链接**: [https://disassociated.com/personal-blogs-back-niche-blogs-next/](https://disassociated.com/personal-blogs-back-niche-blogs-next/)

这篇博文探讨了随着近期个人博客的复兴，利基博客可能再度兴起的潜力。作者回顾了博客的“黄金时代”，并提及Problogger及其专注于帮助博主通过利基专业化实现内容变现。虽然承认利基博客的成功，但作者指出这种形式并不适合所有人，像Kottke这样的通才博客也蓬勃发展。

作者认为，当前的网络环境被社交媒体和人工智能生成的内容所主导，缺乏可靠和值得信任的信息。因此，需要回归到撰写精良、主题聚焦的利基博客。作者倡导独立写作者创作高质量的内容，并获得公平的报酬，同时不通过侵入式广告来损害用户体验。目标是恢复可访问和值得信赖的信息流，摆脱社交媒体上的虚假信息和人工智能生成的摘要。

作者澄清说，当前的独立网络/小型网络运动正在推动个人网站的复苏。他们希望这是一个起点，利基博客紧随其后，重建一个充满活力的网络，让值得信赖的信息唾手可得。

---

## 5. 如何见死者

**原文标题**: How to See the Dead

**原文链接**: [https://www.asimov.press/p/see-the-dead](https://www.asimov.press/p/see-the-dead)

在《如何看见死者》中，视网膜植入体设计师斯宾塞·尼特基接到了一位名叫艾普丽的客户提出的一个 необычный

斯宾塞与想象技术专家奥克斯合作，开发了一个由三部分组成的模块化系统。视网膜植入体作为屏幕，皮层桥作为投影仪，海马体回忆界面作为播放设备。目标是将艾普丽因悲伤而产生的记忆转化为视觉蓝图，并将其与她的实时视觉相结合。

他们对艾普丽进行了大量的访谈，记录她在回忆起爱人的记忆时的大脑活动，重点关注感官细节。奥克斯利用这些数据构建了一个AI编码器，将她的记忆转化为视觉图像，而斯宾塞则专注于植入体和皮层桥。

经过数周的开发，他们使用一个“幻影皮层”（一种合成的艾普丽视觉皮层的替代品）来测试集成系统。在测试过程中，他们发现AI重建的内容会降解和出现故障，揭示了记忆和现实融合的复杂性。文章在留下悬念的情况下结束，让读者自行判断接下来会发生什么，以及这一切是否值得。

---

## 6. 帮助Valve公司增强Steam设备的能力

**原文标题**: Helping Valve to power up Steam devices

**原文链接**: [https://www.igalia.com/2025/11/helpingvalve.html](https://www.igalia.com/2025/11/helpingvalve.html)

Igalia与Valve的合作在为Valve的新Steam设备提供动力方面发挥了重要作用，这些设备包括：Steam Frame（无线VR头显）、Steam Machine（游戏主机）和Steam Controller。 Igalia的工作主要集中在两个关键领域：使x86游戏能够在基于ARM的Steam Frame上流畅运行，以及优化Qualcomm Adreno GPU的Vulkan图形驱动程序。

为了克服游戏PC（x86）和Steam Frame（ARM）之间的架构差异，Igalia正在改进FEX翻译层。这使得为x86编译的游戏可以通过翻译机器代码在ARM上运行。这个过程通常需要细致的手动测试。

Igalia还为 Mesa3D Turnip（一个FOSS Vulkan驱动程序）做出了重大贡献，确保了Steam Frame的 Qualcomm Adreno 750 GPU上高性能且无错误的图形效果。他们增加了对Adreno 700系列GPU的支持，实现了诸如LRZ和自动调谐器等关键优化，并通过DXVK、vkd3d-proton和Zink等项目确保了与各种图形API的兼容性。他们的贡献甚至提高了在Android手机上运行的PC游戏的性能并减少了故障。

Valve对开源软件的承诺使得这次合作特别有益。Igalia的改进和优化使所有使用相同开源项目的人都可以使用。此外，Igalia正在开发一个定制的CPU调度器（LAVD），该调度器可在性能和功耗之间取得平衡，这对于Steam Frame的电池寿命至关重要。他们还在为Steam Machine开发AMD内核显示驱动程序。 Igalia的工作确保了新Steam设备上流畅、高效且图形效果出色的游戏体验，并增强了更广泛的Linux游戏生态系统。

---

## 7. 刚刚发射的两颗火星探测器携带了一个彩蛋。

**原文标题**: The twin probes just launched toward Mars have an Easter egg on board

**原文链接**: [https://arstechnica.com/space/2025/11/the-twin-probes-just-launched-toward-mars-have-an-easter-egg-on-board/](https://arstechnica.com/space/2025/11/the-twin-probes-just-launched-toward-mars-have-an-easter-egg-on-board/)

双子ESCAPADE探测器搭乘蓝色起源公司的新格伦火箭发射升空，将用22个月的时间前往火星，研究空间天气如何影响火星大气层。这两颗由火箭实验室设计和制造的探测器，分别名为“蓝色”和“金色”，携带有一个隐藏的彩蛋：几维鸟的图案，这象征着火箭实验室的 New Zealand 起源。这些几维鸟与火箭实验室的标志、座右铭（“这个世界还不够”）以及象征该公司全球影响力的美国秃鹰图标一同出现在铭牌上。

这项由加州大学伯克利分校的空间科学实验室领导的任务，旨在了解火星为何失去了曾经稠密的大气层和潜在的宜居环境。在从新格伦火箭部署后，探测器将在拉格朗日点2周围环绕，然后在2027年9月利用引力辅助到达火星。随后，它们将进入轨道并进行协同观测，以研究太阳风对火星磁层的影响。

除了装饰有几维鸟的铭牌外，航天器还装有列出为该任务做出贡献的火箭实验室团队成员的铭牌。文章还重点介绍了任务的标志和徽章，代表了包括加州大学伯克利分校、火箭实验室、安柏瑞德航空大学、Advanced Space和美国宇航局戈达德太空飞行中心在内的各个合作伙伴。

---

## 8. 三星DRAM涨价60%预示全球内存供应进一步收紧

**原文标题**: Samsung's 60% DRAM price hike signals a new phase of global memory tightening

**原文链接**: [https://www.buysellram.com/blog/samsungs-memory-price-surge-sends-shockwaves-through-the-global-dram-market/](https://www.buysellram.com/blog/samsungs-memory-price-surge-sends-shockwaves-through-the-global-dram-market/)

自2025年9月以来，三星已将DRAM价格提高了高达60%，这表明全球内存市场因人工智能数据中心需求的激增而趋紧。 此次价格上涨，影响了高密度服务器DRAM模块，是近年来涨幅最大的一次，预计将对PC、服务器和IT硬件行业产生影响，直至2026年。

文章强调，主要驱动因素是人工智能基础设施的爆炸式增长，消耗了大量的DDR5和HBM内存。 三星以及SK海力士和美光等其他制造商正在优先生产用于人工智能服务器的高端芯片，从而减少了传统DRAM的产能。

这种供应限制，加上消费者需求的复苏和有限的制造利用率，正在造成一场“完美风暴”，推动整个市场价格上涨。 价格飙升始于合约市场，现在正在影响零售渠道，DDR5套件的价格同比翻了一番，而较旧的DDR4模块的价格也在上涨。

分析师预测，除非DRAM产量大幅增加，否则这种价格上涨周期将持续到2026年。 二手DRAM的二级市场也在做出反应，随着经销商持有库存的时间延长，价格也在上涨。

文章建议系统构建商、数据中心运营商和组件经销商仔细规划，建议尽早签订供应合同，以避免潜在的短缺。 消费者和小型IT运营商应预期价格持续波动。 总之，人工智能的繁荣正在将DRAM从一种商品转变为计算供应链中的一个战略瓶颈。

---

## 9. 柯达曾在地下室运行核装置数十年。

**原文标题**: Kodak ran a nuclear device in its basement for decades

**原文链接**: [https://www.popularmechanics.com/science/energy/a69147321/kodak-film-nuclear-reactor/](https://www.popularmechanics.com/science/energy/a69147321/kodak-film-nuclear-reactor/)

三十年来，柯达公司在其纽约州罗切斯特市的地下室运营一台锎中子通量倍增器(CFX)，该设备使用少量锎-252和高浓铀(HEU)来产生中子，用于材料分析。CFX利用中子活化分析来测试化学品中的杂质，并利用中子射线照相术，与X射线不同，它可以有效地对水和胶片等较轻元素进行成像，使柯达能够识别X射线会遗漏的泄漏。

该设备是次临界的，意味着它无法独立维持链式反应，使其比核反应堆更安全。虽然柯达公司使用高浓铀的消息在2012年公开时引起了恐慌，但CFX在严格的政府监管下运行。主要担忧出现在2007年退役期间，原因是存在3.5磅高浓铀，如果被恶意行为者获取，则存在潜在的安全风险。在高能物理部的监督下，高浓铀被小心地运送到政府设施，并制定了严格的协议。文章强调，CFX代表了一种冷战时期的技术奇观，突出了那个时代的核乐观主义，当时此类设备在大学和私营公司中更为常见。该建筑此后已被出售并宣布安全。

---

## 10. Show HN: Wealthfolio 2.0 - 开源投资跟踪器。现已支持移动端和Docker

**原文标题**: Show HN: Wealthfolio 2.0- Open source investment tracker. Now Mobile and Docker

**原文链接**: [https://wealthfolio.app/?v=2.0](https://wealthfolio.app/?v=2.0)

Wealthfolio 2.0：一款注重隐私的开源投资追踪器，现已推出桌面、移动和网页版，并支持Docker部署。它旨在通过安全的本地应用程序，替代混乱的电子表格和隐私担忧。主要功能包括通过CSV导入进行账户聚合，提供包含资产配置洞察的全面投资组合概览，以及针对标普500等基准的业绩追踪。

它还提供股息和利息的收入追踪、个人账户的历史业绩分析、目标设定和进度监控，以及税务优惠账户的供款限额追踪。用户可以定义财务目标，追踪进度，并避免过度供款。

该应用程序拥有美观且用户友好的界面，并提供可选的一次性付费，无需定期订阅费用。其可扩展性体现在可选的附加组件上，例如投资费用追踪器、目标进度追踪器和股票交易追踪器。它通过将数据保存在用户设备上，优先考虑用户隐私。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 2 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 3 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 4 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 5 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 6 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 7 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 8 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 9 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 10 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 11 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 12 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 13 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 14 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 15 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 16 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 17 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 18 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 19 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 20 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 21 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 22 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 23 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 24 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 25 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 26 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 27 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 28 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 29 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 30 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 31 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 32 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 33 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 34 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 35 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 36 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 37 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 38 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 39 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 40 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 41 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 42 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 43 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 44 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 45 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 46 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 47 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 48 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 49 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 50 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 51 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 52 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 53 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 54 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 55 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 56 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 57 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 58 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 59 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 60 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 61 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 62 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 63 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 64 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 65 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 66 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 67 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 68 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 69 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 70 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 71 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 72 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 73 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 74 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 75 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 76 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 77 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 78 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 79 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 80 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 81 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 82 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 83 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 84 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 85 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 86 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 87 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 88 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 89 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 90 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 91 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 92 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 93 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 94 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 95 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 96 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 97 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 98 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 99 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 100 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 101 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 102 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 103 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 104 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 105 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 106 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 107 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 108 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 109 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 110 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 111 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 112 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 113 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 114 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 115 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 116 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 117 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 118 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 119 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 120 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 121 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 122 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 123 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 124 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 125 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 126 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 127 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 128 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 129 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 130 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 131 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 132 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 133 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 134 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 135 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 136 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 137 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 138 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 139 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 140 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 141 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 142 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 143 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 144 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 145 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 146 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 147 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 148 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 149 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 150 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 151 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 152 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 153 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 154 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 155 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 156 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 157 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 158 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 159 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 160 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 161 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 162 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 163 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 164 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 165 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 166 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 167 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 168 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 169 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 170 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 171 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 172 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 173 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 174 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 175 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 176 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 177 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 178 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 179 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 180 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 181 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 182 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 183 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 184 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 185 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 186 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 187 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 188 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 189 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 190 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 191 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 192 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 193 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 194 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 195 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 196 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 197 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 198 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 199 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 200 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 201 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 202 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 203 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 204 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 205 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 206 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 207 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 208 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 209 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 210 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 211 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 212 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 213 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 214 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 215 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 216 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 217 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 218 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 219 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 220 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 221 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 222 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 223 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 224 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 225 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 226 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 227 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 228 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 229 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 230 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 231 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 232 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 233 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 234 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 235 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 236 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 237 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 238 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 239 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 240 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 241 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 242 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 243 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 244 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 245 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 246 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 247 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
