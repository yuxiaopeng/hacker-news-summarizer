# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-02-06.md)

*最后自动更新时间: 2026-02-06 18:12:03*
## 1. Waymo 世界模型：自动驾驶仿真的新前沿

**原文标题**: The Waymo World Model: A New Frontier for Autonomous Driving Simulation

**原文链接**: [https://waymo.com/blog/2026/02/the-waymo-world-model-a-new-frontier-for-autonomous-driving-simulation](https://waymo.com/blog/2026/02/the-waymo-world-model-a-new-frontier-for-autonomous-driving-simulation)

Waymo 推出了 Waymo 世界模型 (Waymo World Model)，这是一个旨在通过超现实模拟推动自动驾驶发展的生成式人工智能前沿模型。该模型由 Waymo 与 Google DeepMind 合作开发，并基于 Genie 3 模型构建，能够创建可同时生成摄像头和激光雷达数据的交互式 3D 环境。

该模型通过模拟“长尾”场景（即难以大规模获取的罕见、高风险事件），解决了现实世界数据的局限性。这些场景包括极端天气（龙卷风、洪水）、安全关键型危害（逆行驾驶员）以及异常物体（穿奇装异服的动物或行人）。

**核心特性包括：**
*   **高度可控性：** 工程师可以使用语言提示、驾驶输入和场景布局来修改模拟。这实现了“假设性”反事实测试，例如评估 Waymo 驱动系统在采取不同路径时的反应。
*   **多模态逼真度：** 通过将海量视频数据集中的知识转化为 3D 激光雷达输出，该模型提供了自动驾驶硬件所必需的精确深度和视觉细节。
*   **视频转模拟：** 该模型可以将标准的行车记录仪或手机视频转换为多模态模拟，使 Waymo 能够利用来自全球各地的真实影像测试其驱动系统。
*   **可扩展性：** 该模型的一个高效变体能够在降低计算需求的同时实现长时间模拟，从而助力大规模安全基准测试。

通过模拟“不可能”的情况，Waymo 让其驱动系统在应对公共道路上的复杂现实挑战之前就做好了准备。这项技术是实现可证明的安全人工智能的关键支柱，有助于 Waymo 以更高的信心和安全性将其服务推广到新环境。

---

## 2. 微软开源 LiteBox：一款专注于安全的库操作系统

**原文标题**: Microsoft open-sources LiteBox, a security-focused library OS

**原文链接**: [https://github.com/microsoft/litebox](https://github.com/microsoft/litebox)

微软开源了 **LiteBox**，这是一个专注于安全的库操作系统（LibOS），旨在通过显著减少应用程序与宿主系统之间的接口来增强沙箱功能。通过缩小这一通信面，LiteBox 有效地降低了漏洞的潜在攻击面。

该库操作系统采用灵活的架构，专注于“北向”适配层（面向应用的接口）与“南向”平台（宿主环境）之间的互操作性。LiteBox 提供了一个基于 Rust 的接口（受 nix/rustix 启发），并且具有极高的通用性，可部署在内核及非内核场景中。

**LiteBox 的核心用例包括：**
*   在 Windows 上运行未经修改的 Linux 程序。
*   在 Linux 环境中对 Linux 应用程序进行沙箱隔离。
*   在 SEV SNP 和 OP-TEE 等安全技术上执行程序。
*   在 LVBS（基于 Linux 虚拟化的安全）上运行。

目前，LiteBox 处于活跃的演进阶段。微软指出，该项目尚未发布稳定版本，这意味着 API 和接口可能会发生变化。虽然鼓励开发者尝试使用该库，但应准备好随着设计的成熟而适应后续更新。LiteBox 采用 MIT 许可证开源，并欢迎社区贡献。

---

## 3. 我现在认为 Apple News 上的所有广告都是诈骗。

**原文标题**: I now assume that all ads on Apple news are scams

**原文链接**: [https://kirkville.com/i-now-assume-that-all-ads-on-apple-news-are-scams/](https://kirkville.com/i-now-assume-that-all-ads-on-apple-news-are-scams/)

本文作者认为，在苹果于 2024 年与广告网络 Taboola 达成协议后，Apple News 已沦为诈骗广告的平台。尽管 Apple News+ 的订阅费用昂贵（每月 13 英镑），但用户仍会看到作者所形容的“垃圾广告堆（chumbox）”式的内容——这类广告不仅重复性高、质量低劣，而且日益呈现出掠夺性的特征。

作者提供的证据表明，该平台上当前的许多广告极有可能是诈骗。通过调查 WHOIS 域名数据，作者发现几家被重点推荐的公司（如 MUSTYLEVO.COM 和 TIDENOX.COM）虽然声称拥有悠久的经营历史，但其实际使用的域名都是近期才注册的。例如，“Tidenox”在广告中宣称拥有 26 年的品牌底蕴，其域名却是在几个月前才在中国注册的。

此外，文章还强调了利用 AI 生成内容误导用户的现象。其中一则广告展示了一位由 AI 生成的“即将退休的老板”，画面中甚至粗心地留下了明显的 Google Gemini 标志。作者指出，这种“结业清仓”的手段被商业改进局（BBB）认定为典型的诈骗套路，旨在卷钱跑路。

最终，作者得出结论：苹果和 Taboola 都没有对这些广告进行妥善审核。作者断言，苹果在所谓的高级服务中纵容此类欺骗行为，已经损害了其自身信誉，其在生态系统内的广告管理已不再值得信任。

---

## 4. 可视化理解神经网络

**原文标题**: Understanding Neural Network, Visually

**原文链接**: [https://visualrambling.space/neural-network/](https://visualrambling.space/neural-network/)

《视觉化理解神经网络》是一份入门指南，通过对手写数字识别任务的逐步视觉化呈现，解释了人工智能的基础运行机制。

文章将该过程分解为几个关键阶段：

*   **输入数据：** 以手写数字为例，网络根据像素亮度将图像转化为数据。像素颜色越深，输入神经元获得的值就越高。
*   **权重与求和：** 当数据在各层间传递时，每个输入值都会乘以一个“权重”——这是一个决定连接强度和方向的变量。接收神经元会对这些加权值进行求和。
*   **激活与阈值：** 每个神经元都遵循一种称为“激活函数”的规则。如果输入总和超过特定的“阈值”，神经元就会激活，表明它识别出了特定的模式（如线条或曲线）。
*   **分层处理：** 这一过程在多个层级中重复进行。每一层都以其前一层检测到的模式为基础，从简单形状过渡到复杂结构。
*   **输出：** 在最后一层中，激活水平最高的神经元代表了网络对手写数字的预测结果。

作者总结道，神经网络本质上是一系列将输入映射到输出的数学运算。虽然本文重点介绍了网络如何处理信息，但它也为后续探讨这些系统如何通过寻找最优权重和阈值来实现“学习”奠定了基础。

---

## 5. Sheldon Brown 自行车技术信息

**原文标题**: Sheldon Brown's Bicycle Technical Info

**原文链接**: [https://www.sheldonbrown.com/](https://www.sheldonbrown.com/)

本文是“谢尔顿·布朗自行车技术信息网”（Sheldon Brown’s Bicycle Technical Information）的主页和核心索引。作为一个深受自行车爱好者和技师推崇的在线资源，该网站提供了由已故的谢尔顿·布朗及其他撰稿人编写的详尽文章库，内容几乎涵盖了自行车维修、理论和文化的方方面面。

**主要特色和类别包括：**
*   **技术指南：** 涵盖刹车、变速器、传动系统、车轮和车架等部件的深度技术信息。
*   **专业骑行：** 设有死飞和单速自行车、双人自行车、通勤骑行以及长途旅行的专门板块。
*   **教育资源：** 包含海量的按字母顺序排列的自行车词汇表、DIY维修技巧以及针对初学者的专项指南。
*   **个人内容：** 记录谢尔顿·布朗个人生活的链接，包括其日志、摄影作品、音乐和家族史。
*   **其他杂项：** 随笔、自行车幽默，以及关于“巴黎-布雷斯特-巴黎”（Paris-Brest-Paris）等国际自行车赛事的资讯。

该网站目前由约翰·艾伦（John Allen）负责更新和维护。对于寻求可靠技术数据和自行车历史知识的骑行者来说，它依然是核心的参考资源。

---

## 6. 金钱点滴：欺诈调查就是相信你那双“撒谎”的眼睛

**原文标题**: Bits About Money: Fraud Investigation Is Believing Your Lying Eyes

**原文链接**: [https://www.bitsaboutmoney.com/archive/fraud-investigation/](https://www.bitsaboutmoney.com/archive/fraud-investigation/)

在《反欺诈调查：相信你“说谎”的眼睛》一文中，帕特里克·麦肯齐（Patrick McKenzie，网名 patio11）指出，有效的欺诈检测需要承认那些显而易见、但往往因政治敏感性和体制惯性而被忽视的残酷现实。

麦肯齐以近期明尼苏达州托儿服务欺诈案的争议为案例，批评了“主流媒体”和政府官员对系统性洗劫的证据视而不见。他指出，在某些项目中，调查人员发现超过50%的报销款属于欺诈，但在未对每一起案例进行刑事定罪之前，官员们往往拒绝承认问题的严重规模。

麦肯齐对欺诈的本质提出了三个核心观察：

1.  **重复博弈：** 与利用黑名单管理风险的金融业不同，政府在每个新项目中往往将惯犯视为“白板”。这种对过往记录的“记忆缺失”（缺乏客体永久性），使得同一批行为人能够接连剥削多个社会福利项目。
2.  **欺诈供应链：** 规模化欺诈是一种商业流程，而非业余行为。它利用专业化的基础设施——共享相同的律师、公司注册代理人和邮政信箱。麦肯齐认为，现代数据工具和大型语言模型（LLM）使调查人员现在能够轻松勾勒出这些网络。
3.  **族裔与熟人圈集聚：** 欺诈团伙通常在特定社区内活动，因为犯罪组织需要高度的信任和忠诚才能生存。麦肯齐主张，调查人员必须克服承认这些集聚现象时产生的“本能抵触”，因为如果不这样做，实际上是在为犯罪活动提供“掩护”，而这些活动最终伤害的正是这些社区本身。

最后，麦肯齐呼吁采取一种更加工业化、更少政治化的反欺诈方法，敦促调查人员顶住社会压力，相信自己的观察结果。

---

## 7. TikTok's 'Addictive Design' Found to Be Illegal in Europe

**原文标题**: TikTok's 'Addictive Design' Found to Be Illegal in Europe

**原文链接**: [https://www.nytimes.com/2026/02/06/business/tiktok-addictive-design-europe.html](https://www.nytimes.com/2026/02/06/business/tiktok-addictive-design-europe.html)

Unable to access the article link.

---

## 8. Invention of DNA "Page Numbers" Opens Up Possibilities for the Bioeconomy

**原文标题**: Invention of DNA "Page Numbers" Opens Up Possibilities for the Bioeconomy

**原文链接**: [https://www.caltech.edu/about/news/invention-dna-page-numbers-synthesis-kaihang-wang](https://www.caltech.edu/about/news/invention-dna-page-numbers-synthesis-kaihang-wang)

生成摘要时出错

---

## 9. Hackers (1995) Animated Experience

**原文标题**: Hackers (1995) Animated Experience

**原文链接**: [https://hackers-1995.vercel.app/](https://hackers-1995.vercel.app/)

生成摘要时出错

---

## 10. GPT-5.3-Codex

**原文标题**: GPT-5.3-Codex

**原文链接**: [https://openai.com/index/introducing-gpt-5-3-codex/](https://openai.com/index/introducing-gpt-5-3-codex/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 2 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 3 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 4 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 5 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 6 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 7 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 8 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 9 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 10 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 11 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 12 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 13 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 14 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 15 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 16 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 17 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 18 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 19 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 20 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 21 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 22 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 23 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 24 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 25 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 26 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 27 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 28 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 29 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 30 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 31 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 32 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 33 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 34 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 35 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 36 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 37 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 38 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 39 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 40 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 41 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 42 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 43 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 44 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 45 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 46 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 47 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 48 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 49 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 50 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 51 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 52 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 53 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 54 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 55 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 56 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 57 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 58 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 59 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 60 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 61 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 62 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 63 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 64 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 65 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 66 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 67 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 68 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 69 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 70 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 71 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 72 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 73 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 74 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 75 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 76 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 77 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 78 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 79 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 80 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 81 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 82 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 83 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 84 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 85 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 86 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 87 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 88 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 89 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 90 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 91 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 92 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 93 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 94 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 95 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 96 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 97 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 98 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 99 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 100 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 101 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 102 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 103 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 104 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 105 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 106 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 107 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 108 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 109 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 110 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 111 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 112 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 113 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 114 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 115 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 116 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 117 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 118 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 119 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 120 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 121 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 122 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 123 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 124 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 125 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 126 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 127 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 128 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 129 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 130 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 131 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 132 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 133 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 134 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 135 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 136 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 137 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 138 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 139 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 140 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 141 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 142 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 143 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 144 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 145 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 146 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 147 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 148 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 149 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 150 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 151 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 152 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 153 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 154 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 155 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 156 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 157 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 158 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 159 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 160 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 161 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 162 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 163 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 164 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 165 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 166 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 167 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 168 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 169 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 170 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 171 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 172 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 173 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 174 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 175 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 176 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 177 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 178 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 179 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 180 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 181 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 182 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 183 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 184 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 185 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 186 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 187 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 188 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 189 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 190 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 191 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 192 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 193 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 194 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 195 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 196 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 197 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 198 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 199 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 200 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 201 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 202 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 203 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 204 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 205 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 206 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 207 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 208 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 209 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 210 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 211 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 212 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 213 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 214 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 215 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 216 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 217 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 218 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 219 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 220 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 221 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 222 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 223 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 224 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 225 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 226 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 227 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 228 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 229 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 230 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 231 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 232 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 233 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 234 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 235 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 236 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 237 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 238 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 239 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 240 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 241 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 242 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 243 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 244 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 245 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 246 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 247 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 248 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 249 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 250 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 251 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 252 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 253 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 254 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 255 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 256 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 257 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 258 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 259 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 260 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 261 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 262 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 263 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 264 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 265 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 266 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 267 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 268 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 269 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 270 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 271 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 272 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 273 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 274 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 275 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 276 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 277 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 278 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 279 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 280 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 281 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 282 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 283 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 284 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 285 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 286 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 287 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 288 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 289 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 290 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 291 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 292 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 293 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 294 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 295 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 296 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 297 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 298 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 299 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 300 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 301 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 302 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 303 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 304 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 305 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 306 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 307 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 308 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 309 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 310 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 311 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 312 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 313 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 314 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 315 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 316 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 317 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 318 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 319 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 320 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 321 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 322 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 323 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
