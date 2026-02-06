# Hacker News 热门文章摘要 (2026-02-06)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. A new bill in New York would require disclaimers on AI-generated news content

**原文标题**: A new bill in New York would require disclaimers on AI-generated news content

**原文链接**: [https://www.niemanlab.org/2026/02/a-new-bill-in-new-york-would-require-disclaimers-on-ai-generated-news-content/](https://www.niemanlab.org/2026/02/a-new-bill-in-new-york-would-require-disclaimers-on-ai-generated-news-content/)

生成摘要时出错

---

## 12. The Monad Called Free

**原文标题**: The Monad Called Free

**原文链接**: [http://blog.sigfpe.com/2014/04/the-monad-called-free.html](http://blog.sigfpe.com/2014/04/the-monad-called-free.html)

生成摘要时出错

---

## 13. Things Unix can do atomically (2010)

**原文标题**: Things Unix can do atomically (2010)

**原文链接**: [https://rcrowley.org/2010/01/06/things-unix-can-do-atomically.html](https://rcrowley.org/2010/01/06/things-unix-can-do-atomically.html)

生成摘要时出错

---

## 14. My AI Adoption Journey

**原文标题**: My AI Adoption Journey

**原文链接**: [https://mitchellh.com/writing/my-ai-adoption-journey](https://mitchellh.com/writing/my-ai-adoption-journey)

生成摘要时出错

---

## 15. Animated Engines

**原文标题**: Animated Engines

**原文链接**: [https://animatedengines.com/](https://animatedengines.com/)

生成摘要时出错

---

## 16. The overlooked evolution of the humble car door handle

**原文标题**: The overlooked evolution of the humble car door handle

**原文链接**: [https://newatlas.com/automotive/evolution-car-door-handle/](https://newatlas.com/automotive/evolution-car-door-handle/)

生成摘要时出错

---

## 17. DNS Explained – How Domain Names Get Resolved

**原文标题**: DNS Explained – How Domain Names Get Resolved

**原文链接**: [https://www.bhusalmanish.com.np/blog/posts/dns-explained.html](https://www.bhusalmanish.com.np/blog/posts/dns-explained.html)

生成摘要时出错

---

## 18. Show HN: Smooth CLI – Token-efficient browser for AI agents

**原文标题**: Show HN: Smooth CLI – Token-efficient browser for AI agents

**原文链接**: [https://docs.smooth.sh/cli/overview](https://docs.smooth.sh/cli/overview)

生成摘要时出错

---

## 19. Systems Thinking

**原文标题**: Systems Thinking

**原文链接**: [http://theprogrammersparadox.blogspot.com/2026/02/systems-thinking.html](http://theprogrammersparadox.blogspot.com/2026/02/systems-thinking.html)

生成摘要时出错

---

## 20. LLMs could be, but shouldn't be compilers

**原文标题**: LLMs could be, but shouldn't be compilers

**原文链接**: [https://alperenkeles.com/posts/llms-could-be-but-shouldnt-be-compilers/](https://alperenkeles.com/posts/llms-could-be-but-shouldnt-be-compilers/)

生成摘要时出错

---

## 21. We tasked Opus 4.6 using agent teams to build a C Compiler

**原文标题**: We tasked Opus 4.6 using agent teams to build a C Compiler

**原文链接**: [https://www.anthropic.com/engineering/building-c-compiler](https://www.anthropic.com/engineering/building-c-compiler)

生成摘要时出错

---

## 22. Nixie-clock using neon lamps as logic elements (2007)

**原文标题**: Nixie-clock using neon lamps as logic elements (2007)

**原文链接**: [https://www.pa3fwm.nl/projects/neonclock/](https://www.pa3fwm.nl/projects/neonclock/)

生成摘要时出错

---

## 23. Claude Opus 4.6

**原文标题**: Claude Opus 4.6

**原文链接**: [https://www.anthropic.com/news/claude-opus-4-6](https://www.anthropic.com/news/claude-opus-4-6)

生成摘要时出错

---

## 24. Solving Shrinkwrap: New Experimental Technique

**原文标题**: Solving Shrinkwrap: New Experimental Technique

**原文链接**: [https://kizu.dev/shrinkwrap-solution/](https://kizu.dev/shrinkwrap-solution/)

生成摘要时出错

---

## 25. Stay Away from My Trash

**原文标题**: Stay Away from My Trash

**原文链接**: [https://tldraw.dev/blog/stay-away-from-my-trash](https://tldraw.dev/blog/stay-away-from-my-trash)

生成摘要时出错

---

## 26. Recreating Epstein PDFs from raw encoded attachments

**原文标题**: Recreating Epstein PDFs from raw encoded attachments

**原文链接**: [https://neosmart.net/blog/recreating-epstein-pdfs-from-raw-encoded-attachments/](https://neosmart.net/blog/recreating-epstein-pdfs-from-raw-encoded-attachments/)

生成摘要时出错

---

## 27. Plasma Effect (2016)

**原文标题**: Plasma Effect (2016)

**原文链接**: [https://www.4rknova.com/blog/2016/11/01/plasma](https://www.4rknova.com/blog/2016/11/01/plasma)

生成摘要时出错

---

## 28. Show HN: Artifact Keeper – Open-Source Artifactory/Nexus Alternative in Rust

**原文标题**: Show HN: Artifact Keeper – Open-Source Artifactory/Nexus Alternative in Rust

**原文链接**: [https://github.com/artifact-keeper](https://github.com/artifact-keeper)

生成摘要时出错

---

## 29. The time I didn't meet Jeffrey Epstein

**原文标题**: The time I didn't meet Jeffrey Epstein

**原文链接**: [https://scottaaronson.blog/?p=9534](https://scottaaronson.blog/?p=9534)

生成摘要时出错

---

## 30. Animated Knots

**原文标题**: Animated Knots

**原文链接**: [https://www.animatedknots.com/](https://www.animatedknots.com/)

生成摘要时出错

---

## 31. The RCE that AMD won't fix

**原文标题**: The RCE that AMD won't fix

**原文链接**: [https://mrbruh.com/amd/](https://mrbruh.com/amd/)

生成摘要时出错

---

## 32. Bytes as Braille

**原文标题**: Bytes as Braille

**原文链接**: [https://www.engrenage.ch/i18n/scripts/bytes_as_braille/](https://www.engrenage.ch/i18n/scripts/bytes_as_braille/)

生成摘要时出错

---

## 33. Unlocking high-performance PostgreSQL with key memory optimizations

**原文标题**: Unlocking high-performance PostgreSQL with key memory optimizations

**原文链接**: [https://stormatics.tech/blogs/unlocking-high-performance-postgresql-key-memory-optimizations](https://stormatics.tech/blogs/unlocking-high-performance-postgresql-key-memory-optimizations)

生成摘要时出错

---

## 34. How to carry more than your own bodyweight (2025)

**原文标题**: How to carry more than your own bodyweight (2025)

**原文链接**: [https://www.bbc.com/future/article/20250124-how-to-carry-more-than-your-own-bodyweight](https://www.bbc.com/future/article/20250124-how-to-carry-more-than-your-own-bodyweight)

生成摘要时出错

---

## 35. Coding Agents and Use Cases

**原文标题**: Coding Agents and Use Cases

**原文链接**: [https://justsitandgrin.im/posts/coding-agents-use-cases/](https://justsitandgrin.im/posts/coding-agents-use-cases/)

生成摘要时出错

---

## 36. Orchestrate teams of Claude Code sessions

**原文标题**: Orchestrate teams of Claude Code sessions

**原文链接**: [https://code.claude.com/docs/en/agent-teams](https://code.claude.com/docs/en/agent-teams)

生成摘要时出错

---

## 37. Waiting for Postgres 19: Better planner hints with path generation strategies [video]

**原文标题**: Waiting for Postgres 19: Better planner hints with path generation strategies [video]

**原文链接**: [https://www.youtube.com/watch?v=QLb3nhIy2Lc](https://www.youtube.com/watch?v=QLb3nhIy2Lc)

生成摘要时出错

---

## 38. Review of 1984 by Isaac Asimov (1980)

**原文标题**: Review of 1984 by Isaac Asimov (1980)

**原文链接**: [https://www.newworker.org/ncptrory/1984.htm](https://www.newworker.org/ncptrory/1984.htm)

生成摘要时出错

---

## 39. I reversed Tower of Fantasy's anti-cheat driver: a BYOVD toolkit never loaded

**原文标题**: I reversed Tower of Fantasy's anti-cheat driver: a BYOVD toolkit never loaded

**原文链接**: [https://vespalec.com/blog/tower-of-flaws/](https://vespalec.com/blog/tower-of-flaws/)

生成摘要时出错

---

## 40. Uber Found Liable in Rape by Driver, Setting Stage for Cases

**原文标题**: Uber Found Liable in Rape by Driver, Setting Stage for Cases

**原文链接**: [https://www.nytimes.com/2026/02/05/business/uber-safety-rape-verdict.html](https://www.nytimes.com/2026/02/05/business/uber-safety-rape-verdict.html)

生成摘要时出错

---

## 41. MenuetOS – a GUI OS that boots from a single floppy disk

**原文标题**: MenuetOS – a GUI OS that boots from a single floppy disk

**原文链接**: [https://www.menuetos.net/](https://www.menuetos.net/)

生成摘要时出错

---

## 42. Claude Opus 4.6 extra usage promo

**原文标题**: Claude Opus 4.6 extra usage promo

**原文链接**: [https://support.claude.com/en/articles/13613973-claude-opus-4-6-extra-usage-promo](https://support.claude.com/en/articles/13613973-claude-opus-4-6-extra-usage-promo)

生成摘要时出错

---

## 43. LinkedIn checks for 2953 browser extensions

**原文标题**: LinkedIn checks for 2953 browser extensions

**原文链接**: [https://github.com/mdp/linkedin-extension-fingerprinting](https://github.com/mdp/linkedin-extension-fingerprinting)

生成摘要时出错

---

## 44. Maihem (YC W24): hiring senior robotics perception engineer (London, on-site)

**原文标题**: Maihem (YC W24): hiring senior robotics perception engineer (London, on-site)

**原文链接**: [https://jobs.ashbyhq.com/maihem/8da3fa8b-5544-45de-a99e-888021519758](https://jobs.ashbyhq.com/maihem/8da3fa8b-5544-45de-a99e-888021519758)

生成摘要时出错

---

## 45. The Color of Safety

**原文标题**: The Color of Safety

**原文链接**: [https://protocolized.summerofprotocols.com/p/the-color-of-safety](https://protocolized.summerofprotocols.com/p/the-color-of-safety)

生成摘要时出错

---

## 46. Hypernetworks: Neural Networks for Hierarchical Data

**原文标题**: Hypernetworks: Neural Networks for Hierarchical Data

**原文链接**: [https://blog.sturdystatistics.com/posts/hnet_part_I/](https://blog.sturdystatistics.com/posts/hnet_part_I/)

生成摘要时出错

---

## 47. What if writing tests was a joyful experience? (2023)

**原文标题**: What if writing tests was a joyful experience? (2023)

**原文链接**: [https://blog.janestreet.com/the-joy-of-expect-tests/](https://blog.janestreet.com/the-joy-of-expect-tests/)

生成摘要时出错

---

## 48. India's female workers watching hours of abusive content to train AI

**原文标题**: India's female workers watching hours of abusive content to train AI

**原文链接**: [https://www.theguardian.com/global-development/2026/feb/05/in-the-end-you-feel-blank-indias-female-workers-watching-hours-of-abusive-content-to-train-ai](https://www.theguardian.com/global-development/2026/feb/05/in-the-end-you-feel-blank-indias-female-workers-watching-hours-of-abusive-content-to-train-ai)

生成摘要时出错

---

## 49. Sealos – AI Native Cloud Cloud Operating System

**原文标题**: Sealos – AI Native Cloud Cloud Operating System

**原文链接**: [https://github.com/labring/sealos](https://github.com/labring/sealos)

生成摘要时出错

---

## 50. U.S. asks American citizens to 'leave Iran now'

**原文标题**: U.S. asks American citizens to 'leave Iran now'

**原文链接**: [https://www.cnbc.com/2026/02/06/us-asks-american-citizens-to-leave-iran-now-ahead-of-high-stakes-talks-with-tehran-.html](https://www.cnbc.com/2026/02/06/us-asks-american-citizens-to-leave-iran-now-ahead-of-high-stakes-talks-with-tehran-.html)

生成摘要时出错

---

## 51. Don't rent the cloud, own instead

**原文标题**: Don't rent the cloud, own instead

**原文链接**: [https://blog.comma.ai/datacenter/](https://blog.comma.ai/datacenter/)

生成摘要时出错

---

## 52. The New Collabora Office for Desktop

**原文标题**: The New Collabora Office for Desktop

**原文链接**: [https://www.collaboraonline.com/collabora-office/](https://www.collaboraonline.com/collabora-office/)

生成摘要时出错

---

## 53. 'Ripping' Clips for YouTube Reaction Videos Can Violate the DMCA, Court Rules

**原文标题**: 'Ripping' Clips for YouTube Reaction Videos Can Violate the DMCA, Court Rules

**原文链接**: [https://torrentfreak.com/ripping-clips-for-youtube-reaction-videos-can-violate-the-dmca-court-rules/](https://torrentfreak.com/ripping-clips-for-youtube-reaction-videos-can-violate-the-dmca-court-rules/)

生成摘要时出错

---

## 54. The rise of one-pizza engineering teams

**原文标题**: The rise of one-pizza engineering teams

**原文链接**: [https://www.jampa.dev/p/the-rise-of-one-pizza-engineering](https://www.jampa.dev/p/the-rise-of-one-pizza-engineering)

生成摘要时出错

---

## 55. Ad blocking is alive and well, despite Chrome's attempts to make it harder

**原文标题**: Ad blocking is alive and well, despite Chrome's attempts to make it harder

**原文链接**: [https://www.theregister.com/2026/02/06/chrome_mv3_no_harm_ad_blocking/](https://www.theregister.com/2026/02/06/chrome_mv3_no_harm_ad_blocking/)

生成摘要时出错

---

## 56. Anna's Archive Loses .PM Domain, Adds Greenland (.GL) Backup

**原文标题**: Anna's Archive Loses .PM Domain, Adds Greenland (.GL) Backup

**原文链接**: [https://torrentfreak.com/annas-archive-loses-pm-domain-adds-greenland-gl-backup/](https://torrentfreak.com/annas-archive-loses-pm-domain-adds-greenland-gl-backup/)

生成摘要时出错

---

## 57. GitHub Actions is slowly killing engineering teams

**原文标题**: GitHub Actions is slowly killing engineering teams

**原文链接**: [https://www.iankduncan.com/engineering/2026-02-05-github-actions-killing-your-team/](https://www.iankduncan.com/engineering/2026-02-05-github-actions-killing-your-team/)

生成摘要时出错

---

## 58. Amazon Shares Sink as Company Boosts AI Spending by Nearly 60%

**原文标题**: Amazon Shares Sink as Company Boosts AI Spending by Nearly 60%

**原文链接**: [https://www.wsj.com/business/earnings/amazon-earnings-q4-2025-amzn-stock-996e5cc2](https://www.wsj.com/business/earnings/amazon-earnings-q4-2025-amzn-stock-996e5cc2)

生成摘要时出错

---

## 59. Generative Pen-Trained Transformer

**原文标题**: Generative Pen-Trained Transformer

**原文链接**: [https://theodore.net/projects/Polargraph/](https://theodore.net/projects/Polargraph/)

生成摘要时出错

---

## 60. Free Bespoke Sewing Patterns – FreeSewing

**原文标题**: Free Bespoke Sewing Patterns – FreeSewing

**原文链接**: [https://freesewing.eu/](https://freesewing.eu/)

生成摘要时出错

---

## 61. Ardour 9.0

**原文标题**: Ardour 9.0

**原文链接**: [https://ardour.org/whatsnew.html](https://ardour.org/whatsnew.html)

生成摘要时出错

---

## 62. C isn't a programming language anymore (2022)

**原文标题**: C isn't a programming language anymore (2022)

**原文链接**: [https://faultlore.com/blah/c-isnt-a-language/](https://faultlore.com/blah/c-isnt-a-language/)

生成摘要时出错

---

## 63. Show HN: Local task classifier and dispatcher on RTX 3080

**原文标题**: Show HN: Local task classifier and dispatcher on RTX 3080

**原文链接**: [https://github.com/resilientworkflowsentinel/resilient-workflow-sentinel](https://github.com/resilientworkflowsentinel/resilient-workflow-sentinel)

生成摘要时出错

---

## 64. PsiACE/Skills – A small, shared skill library

**原文标题**: PsiACE/Skills – A small, shared skill library

**原文链接**: [https://github.com/PsiACE/skills](https://github.com/PsiACE/skills)

生成摘要时出错

---

## 65. Show HN: Micropolis/SimCity Clone in Emacs Lisp

**原文标题**: Show HN: Micropolis/SimCity Clone in Emacs Lisp

**原文链接**: [https://github.com/vkazanov/elcity](https://github.com/vkazanov/elcity)

生成摘要时出错

---

## 66. GB Renewables Map

**原文标题**: GB Renewables Map

**原文链接**: [https://renewables-map.robinhawkes.com/](https://renewables-map.robinhawkes.com/)

生成摘要时出错

---

## 67. Making Ferrite Core Inductors at Home

**原文标题**: Making Ferrite Core Inductors at Home

**原文链接**: [https://danielmangum.com/posts/making-ferrite-core-inductors-home/](https://danielmangum.com/posts/making-ferrite-core-inductors-home/)

生成摘要时出错

---

## 68. Wirth's Revenge

**原文标题**: Wirth's Revenge

**原文链接**: [https://jmoiron.net/blog/wirths-revenge/](https://jmoiron.net/blog/wirths-revenge/)

生成摘要时出错

---

## 69. Show HN: Agent Arena – Test How Manipulation-Proof Your AI Agent Is

**原文标题**: Show HN: Agent Arena – Test How Manipulation-Proof Your AI Agent Is

**原文链接**: [https://wiz.jock.pl/experiments/agent-arena/](https://wiz.jock.pl/experiments/agent-arena/)

生成摘要时出错

---

## 70. Psychometric Jailbreaks Reveal Internal Conflict in Frontier Models

**原文标题**: Psychometric Jailbreaks Reveal Internal Conflict in Frontier Models

**原文链接**: [https://arxiv.org/abs/2512.04124](https://arxiv.org/abs/2512.04124)

生成摘要时出错

---

## 71. CIA suddenly stops publishing, removes archives of The World Factbook

**原文标题**: CIA suddenly stops publishing, removes archives of The World Factbook

**原文链接**: [https://simonwillison.net/2026/Feb/5/the-world-factbook/](https://simonwillison.net/2026/Feb/5/the-world-factbook/)

生成摘要时出错

---

## 72. Voxtral Transcribe 2

**原文标题**: Voxtral Transcribe 2

**原文链接**: [https://mistral.ai/news/voxtral-transcribe-2](https://mistral.ai/news/voxtral-transcribe-2)

生成摘要时出错

---

## 73. When internal hostnames are leaked to the clown

**原文标题**: When internal hostnames are leaked to the clown

**原文链接**: [https://rachelbythebay.com/w/2026/02/03/badnas/](https://rachelbythebay.com/w/2026/02/03/badnas/)

生成摘要时出错

---

## 74. Company as Code

**原文标题**: Company as Code

**原文链接**: [https://blog.42futures.com/p/company-as-code](https://blog.42futures.com/p/company-as-code)

生成摘要时出错

---

## 75. What Every Programmer Should Know About Memory [pdf] (2007)

**原文标题**: What Every Programmer Should Know About Memory [pdf] (2007)

**原文链接**: [https://people.freebsd.org/~lstewart/articles/cpumemory.pdf](https://people.freebsd.org/~lstewart/articles/cpumemory.pdf)

生成摘要时出错

---

## 76. If you've got Nothing to Hide (2015)

**原文标题**: If you've got Nothing to Hide (2015)

**原文链接**: [https://jacquesmattheij.com/if-you-have-nothing-to-hide/](https://jacquesmattheij.com/if-you-have-nothing-to-hide/)

生成摘要时出错

---

## 77. Monty - A minimal, secure Python interpreter written in Rust

**原文标题**: Monty - A minimal, secure Python interpreter written in Rust

**原文链接**: [https://github.com/pydantic/monty](https://github.com/pydantic/monty)

生成摘要时出错

---

## 78. Opus 4.6 uncovers 500 zero-day flaws in open-source code

**原文标题**: Opus 4.6 uncovers 500 zero-day flaws in open-source code

**原文链接**: [https://www.axios.com/2026/02/05/anthropic-claude-opus-46-software-hunting](https://www.axios.com/2026/02/05/anthropic-claude-opus-46-software-hunting)

生成摘要时出错

---

## 79. $300B Evaporated. The SaaS -Pocalypse Has Begun

**原文标题**: $300B Evaporated. The SaaS -Pocalypse Has Begun

**原文链接**: [https://www.forbes.com/sites/donmuir/2026/02/04/300-billion-evaporated-the-saaspocalypse-has-begun/](https://www.forbes.com/sites/donmuir/2026/02/04/300-billion-evaporated-the-saaspocalypse-has-begun/)

生成摘要时出错

---

## 80. OpenAI Frontier

**原文标题**: OpenAI Frontier

**原文链接**: [https://openai.com/index/introducing-openai-frontier/](https://openai.com/index/introducing-openai-frontier/)

生成摘要时出错

---

## 81. The browser catches homograph attacks, the terminal doesn't

**原文标题**: The browser catches homograph attacks, the terminal doesn't

**原文链接**: [https://github.com/sheeki03/tirith](https://github.com/sheeki03/tirith)

生成摘要时出错

---

## 82. Nanobot: Ultra-Lightweight Alternative to OpenClaw

**原文标题**: Nanobot: Ultra-Lightweight Alternative to OpenClaw

**原文链接**: [https://github.com/HKUDS/nanobot](https://github.com/HKUDS/nanobot)

生成摘要时出错

---

## 83. UUP dump – download UUP files from Windows Update servers with ease

**原文标题**: UUP dump – download UUP files from Windows Update servers with ease

**原文链接**: [https://uupdump.net/](https://uupdump.net/)

生成摘要时出错

---

## 84. Flock CEO calls Deflock a “terrorist organization” (2025) [video]

**原文标题**: Flock CEO calls Deflock a “terrorist organization” (2025) [video]

**原文链接**: [https://www.youtube.com/watch?v=l-kZGrDz7PU](https://www.youtube.com/watch?v=l-kZGrDz7PU)

生成摘要时出错

---

## 85. Data centers in space makes no sense

**原文标题**: Data centers in space makes no sense

**原文链接**: [https://civai.org/blog/space-data-centers](https://civai.org/blog/space-data-centers)

生成摘要时出错

---

## 86. Pandoc for the people: Convert documents without leaving the browser

**原文标题**: Pandoc for the people: Convert documents without leaving the browser

**原文链接**: [https://pandoc.org/app/](https://pandoc.org/app/)

生成摘要时出错

---

## 87. Advancing finance with Claude Opus 4.6

**原文标题**: Advancing finance with Claude Opus 4.6

**原文链接**: [https://claude.com/blog/opus-4-6-finance](https://claude.com/blog/opus-4-6-finance)

生成摘要时出错

---

## 88. Using Microvm.nix to Sandbox OpenClaw

**原文标题**: Using Microvm.nix to Sandbox OpenClaw

**原文链接**: [https://buduroiu.com/blog/openclaw-microvm/](https://buduroiu.com/blog/openclaw-microvm/)

生成摘要时出错

---

## 89. AI bot gives customer 80% discount, supplier can't deliver

**原文标题**: AI bot gives customer 80% discount, supplier can't deliver

**原文链接**: [https://old.reddit.com/r/LegalAdviceUK/comments/1qxc7x9/an_ai_chatassist_created_and_offered_a_customer/](https://old.reddit.com/r/LegalAdviceUK/comments/1qxc7x9/an_ai_chatassist_created_and_offered_a_customer/)

生成摘要时出错

---

## 90. Why Elixir is the best language for AI – Dashbit Blog

**原文标题**: Why Elixir is the best language for AI – Dashbit Blog

**原文链接**: [https://dashbit.co/blog/why-elixir-best-language-for-ai](https://dashbit.co/blog/why-elixir-best-language-for-ai)

生成摘要时出错

---

## 91. Volkswagen overtook Tesla as Europe's top EV seller in 2025

**原文标题**: Volkswagen overtook Tesla as Europe's top EV seller in 2025

**原文链接**: [https://www.reuters.com/business/autos-transportation/volkswagen-overtook-tesla-europes-top-ev-seller-2025-2026-02-05/](https://www.reuters.com/business/autos-transportation/volkswagen-overtook-tesla-europes-top-ev-seller-2025-2026-02-05/)

生成摘要时出错

---

## 92. An interactive version of Byrne's The Elements of Euclid (1847)

**原文标题**: An interactive version of Byrne's The Elements of Euclid (1847)

**原文链接**: [https://c82.net/euclid/](https://c82.net/euclid/)

生成摘要时出错

---

## 93. A few CPU hardware bugs

**原文标题**: A few CPU hardware bugs

**原文链接**: [https://www.taricorp.net/2026/a-few-cpu-bugs/](https://www.taricorp.net/2026/a-few-cpu-bugs/)

生成摘要时出错

---

## 94. A case study in PDF forensics: The Epstein PDFs

**原文标题**: A case study in PDF forensics: The Epstein PDFs

**原文链接**: [https://pdfa.org/a-case-study-in-pdf-forensics-the-epstein-pdfs/](https://pdfa.org/a-case-study-in-pdf-forensics-the-epstein-pdfs/)

生成摘要时出错

---

## 95. Top downloaded skill in ClawHub contains malware

**原文标题**: Top downloaded skill in ClawHub contains malware

**原文链接**: [https://1password.com/blog/from-magic-to-malware-how-openclaws-agent-skills-become-an-attack-surface](https://1password.com/blog/from-magic-to-malware-how-openclaws-agent-skills-become-an-attack-surface)

生成摘要时出错

---

## 96. Housman's Introductory Lecture (1892)

**原文标题**: Housman's Introductory Lecture (1892)

**原文链接**: [https://worrydream.com/refs/Housman_1892_-_Introductory_Lecture.html](https://worrydream.com/refs/Housman_1892_-_Introductory_Lecture.html)

生成摘要时出错

---

## 97. The Great Unwind

**原文标题**: The Great Unwind

**原文链接**: [https://occupywallst.com/yen](https://occupywallst.com/yen)

生成摘要时出错

---

## 98. Adobe Animate will be discontinued

**原文标题**: Adobe Animate will be discontinued

**原文链接**: [https://helpx.adobe.com/uk/animate/kb/end-of-life.html](https://helpx.adobe.com/uk/animate/kb/end-of-life.html)

生成摘要时出错

---

## 99. Latest VirtualBox Code Begins Supporting KVM Back End

**原文标题**: Latest VirtualBox Code Begins Supporting KVM Back End

**原文链接**: [https://www.phoronix.com/news/VirtualBox-Upstream-With-KVM](https://www.phoronix.com/news/VirtualBox-Upstream-With-KVM)

生成摘要时出错

---

## 100. Triton Bespoke Layouts

**原文标题**: Triton Bespoke Layouts

**原文链接**: [https://www.lei.chat/posts/triton-bespoke-layouts/](https://www.lei.chat/posts/triton-bespoke-layouts/)

生成摘要时出错

---

