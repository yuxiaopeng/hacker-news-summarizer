# Hacker News 热门文章摘要 (2025-12-22)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 将大语言模型扩展至更大型代码库

**原文标题**: Scaling LLMs to Larger Codebases

**原文链接**: [https://blog.kierangill.xyz/oversight-and-guidance](https://blog.kierangill.xyz/oversight-and-guidance)

将大语言模型（LLM）应用于更大规模的代码库，需要超越简单的提示词工程，转向由“**引导**（Guidance）”与“**监督**（Oversight）”构成的双支柱策略。

“**引导**”的核心在于提供给模型的上下文。其目标是实现“一次成型”（one-shotting），即在单次尝试中生成高质量、可用的代码，以避免手动返工带来的低效。为此，团队应当建立“提示词库”：通过不断迭代文档、代码库映射和最佳实践，为模型提供必要的背景信息。此外，作者强调“整洁代码”原则在当下尤为重要。由于模型的表现受限于输入质量，一个充斥着技术债和模块化程度差的代码库会诱发模型幻觉。如果人类工程师都无法理清某个模块，模型也同样做不到。

“**监督**”则侧重于验证模型决策所需的人类技能。企业不应追求用自动化取代工程师，而应投资培养他们的设计与架构直觉。合格的监督者必须具备辨别技术决策优劣的“品味”，以判断模型的决策（如数据库选型）是否符合长期目标。这种直觉源于对经典著作的研读以及深度的开发实践。

最后，文章建议尽可能实现**监督自动化**。通过引入强类型系统和“架构逻辑”测试等程序化“护栏”，工程师可以保护抽象层，确保模型在既定边界内运行。随着模型产出的代码量剧增，团队还必须通过优化 QA 流程并将常见的代码评审反馈沉淀为文档来突破“验证瓶颈”，从而在规模化生产中维持代码质量。

---

## 2. 史上最大的CRT：索尼PVM-4300

**原文标题**: The biggest CRT ever made: Sony's PVM-4300

**原文链接**: [https://dfarq.homeip.net/the-biggest-crt-ever-made-sonys-pvm-4300/](https://dfarq.homeip.net/the-biggest-crt-ever-made-sonys-pvm-4300/)

1989年，索尼推出了 PVM-4300（在日本被称为 KV-45ED1），这是有史以来制造的最大的传统 CRT（阴极射线管）电视。该机型拥有 45 英寸显像管和 43 英寸可视屏幕，堪称一项宏大的工程壮举：其重量约 450 磅（约 204 公斤），高度为 27 英寸，且往往因为宽度过大而无法通过标准的门框。

1990年，索尼仅向美国进口了 20 台，零售价高达惊人的 4 万美元。与索尼量产的小型机型不同，PVM-4300 是手工打造的。为了匹配其昂贵的身价，它采用了改良清晰度电视（IDTV）技术。该系统利用缓冲区存储并对连续帧进行插值处理，从而提供比标准隔行扫描 CRT 更清晰、更稳定的图像，成为通往高清电视（HDTV）时代的奢华桥梁。

数十年来，这款电视一直被视为“谜一般”的稀缺品，一些发烧友甚至怀疑是否还有存世实例。然而，在 2024 年 12 月，YouTuber Shank Mods 记录了他从日本一家餐厅购得一台幸存机器的过程。尽管其庞大的尺寸和重量带来了物流挑战，该设备还是被成功运抵美国。这一发现证实，这种高端复古技术至少有一个功能完好的实例，如今保存在一位热衷于此的爱好者手中。

---

## 3. 礼赞冬至的古代遗迹

**原文标题**: The ancient monuments saluting the winter solstice

**原文链接**: [https://www.bbc.com/culture/article/20251219-the-ancient-monuments-saluting-the-winter-solstice](https://www.bbc.com/culture/article/20251219-the-ancient-monuments-saluting-the-winter-solstice)

本文探讨了人类对冬至持久的迷恋，这体现在具有5000年历史的新石器时代纪念碑和当代大地艺术中。在整个北半球，各种建筑结构都经过精确对齐，以在一年中白天最短的那天框取太阳，标志着季节循环重置时“死亡与重生”的关键时刻。

**古代意义**
对于古代文明而言，追踪冬至关乎生存。它使狩猎采集者和早期农民能够预测动物迁徙和对收割至关重要的季节变化。奥克尼的**梅肖韦古墓**、爱尔兰的**纽格莱奇墓**以及法国的**仙女岩**等纪念碑利用长廊来“捕捉”阳光，在仲冬时节照亮黑暗的墓室。这些遗址体现了精神上的“岁之子夜”，提醒人们时间的循环属性以及春天回归的承诺。

**现代诠释**
近几十年来，艺术家们复兴了这种“新石器时代美学”，让现代人类重新建立起与自然节奏的联系。
*   **南希·霍尔特的《太阳隧道》**（犹他州）利用巨大的混凝土管来框取冬至日出和日落的景象，将辽阔的沙漠带回到人类的尺度。
*   **詹姆斯·特瑞尔的《罗登火山口》**（亚利桑那州）在火山锥中挖掘了一条隧道，作为暗箱将仲冬的阳光投射到大理石板上。
*   **杉本博司的“江之浦测候所”**（日本）包含一条“礼光隧道”，旨在帮助访客在浩瀚的宇宙中找到自己的位置。

无论是为了生存还是艺术表达，这些建筑都赞美了从黑暗到光明的过渡。它们唤起了一种原始的认知：一年中最黑暗的时刻已经过去，预示着春天即将到来的温暖与复苏。

---

## 4. Show HN: Netrinos – 专为小团队打造的极简 Mesh VPN

**原文标题**: Show HN: Netrinos – A keep it simple Mesh VPN for small teams

**原文链接**: [https://netrinos.com](https://netrinos.com)

**Netrinos** 是一款简化的网状 (mesh) VPN 服务，旨在为小型团队和个人提供安全、私密的网络访问，而无需复杂的传统 IT 配置。其核心价值在于能够无缝穿透防火墙和路由器，消除了对端口转发或手动网络调整的需求。

**核心特性：**
*   **零配置：** 该服务旨在实现即时设置——用户只需安装应用程序并登录，软件便会自动处理设备发现和网络配置。
*   **安全性：** 采用行业标准的 **WireGuard** 协议，提供企业级的点对点加密。
*   **无缝漫游：** 设备在办公局域网、家庭网络、公共 Wi-Fi 和蜂窝热点等不同环境之间切换时，能保持稳定的连接。
*   **跨平台支持：** Netrinos 支持 Windows、Mac 和 Linux，并兼容台式机、笔记本电脑、服务器、树莓派 (Raspberry Pi)、云虚拟机和物联网 (IoT) 设备。

**定价方案：**
*   **个人版（免费）：** 供非商业用途，支持 1 名用户和多达 100 台设备。
*   **专业版（10 美元/月）：** 为团队设计，支持多达 10 名用户和 100 台设备，提供 14 天免费试用。
*   **高级版（定制）：** 为企业需求量身定制，提供物联网集成、硬件解决方案和白标品牌定制。

总之，Netrinos 将自己定位为一种“化繁为简”的替代方案，适用于那些希望本地网络能够全球随行、且无需处理繁琐网络管理难题的用户。

---

## 5. 氛围感的一年

**原文标题**: A year of vibes

**原文链接**: [https://lucumr.pocoo.org/2025/12/22/a-year-of-vibes/](https://lucumr.pocoo.org/2025/12/22/a-year-of-vibes/)

在《氛围之年》（A Year of Vibes）中，Armin Ronacher 对 2025 年进行了反思。这是充满变革的一年，他离开了 Sentry 创立了一家新公司，并从根本上改变了自己的编程方式。他描述了从手动编码向“智能体化编码”（agentic coding）的转变：在这种模式下，他扮演工程负责人的角色，利用 Claude Code、Amp 和 Pi 等工具监督 AI “虚拟实习生”。

文章的核心主题和见解包括：

*   **智能体工作流的兴起：** Ronacher 强调了具备记忆和工具执行能力的 AI 工具如何成为他的工作常态。然而，他对于人类与这些机器之间形成的“准社交关系”（parasocial bonds）感到不安，并认为“智能体”这一术语存在问题，因为责任必须始终由人类承担。
*   **氛围胜于数据：** 他指出，由于该领域发展极快，许多行业讨论是基于主观的“氛围”（vibes）和偏好，而非成熟的工程证据。
*   **自建还是外包：** 尽管目前的趋势是外包核心服务（如认证、SDK），但 Ronacher 认为 AI 赋予了开发者自行构建这些工具的能力，从而可能减少对外部依赖的需求。
*   **基础设施的不足：** 他认为 Git 和 GitHub 等传统工具已无法适应智能体时代。他呼吁建立一种新型的版本控制系统，能够追踪提示词（prompts）、失败的尝试以及“失败中的价值”，以防止 AI 重复错误。
*   **可观测性与伦理的未来：** AI 处理 eBPF 和 SQL 查询等复杂任务的能力可能会彻底改变可观测性领域。与此同时，他警告要警惕“垃圾代码”（slop）的兴起——即开源项目中未经审查的 AI 代码，并强调需要为 AI 辅助的贡献建立新的社会契约和高标准。

最终，Ronacher 将 2025 年视为软件工程数十年根基开始受到“氛围驱动、智能体主导”这一新现实挑战的一年。

---

## 6. 世上没有假羽毛 [视频]

**原文标题**: There's no such thing as a fake feather [video]

**原文链接**: [https://www.youtube.com/watch?v=N5yV1Q9O6r4](https://www.youtube.com/watch?v=N5yV1Q9O6r4)

基于标题《世界上没有假羽毛》（科普频道 Veritasium 的热门视频），以下是内容的简要总结：

**内容提要**
该视频探讨了鸟类羽毛背后复杂的工程学和物理学原理，重点区分了**色素色**与**结构色**。

要点包括：

*   **结构显色：** 不同于大多数依靠化学色素（通过吸收特定波长的光显色）获取颜色的物体，鸟类许多鲜艳的颜色——尤其是蓝色和虹彩光泽——是由羽毛在微观层面的物理形状产生的。例如，冠蓝鸦体内并没有“蓝色”色素，其颜色是由光线在羽毛羽支内部结构上发生散射而产生的。
*   **“假”的概念：** 标题寓指这些结构极其复杂且独特，简单的染料无法轻易模仿。如果一个结构产生了羽毛的光学效果，那么它在本质上就等同于这种生物技术。视频认为，“颜色”是羽毛物理形态中不可分割的属性。
*   **微观复杂性：** 视频利用高倍显微镜展示了羽支和羽小支的层级排列。它解释了光干涉和“相干散射”如何让鸟类能够极其精确地操纵光线。
*   **进化壮举：** 这种生物“纳米技术”使鸟类能够展示出比色素更明亮、更持久的颜色，而色素往往会随时间褪色。

**注：** 您在提示中提供的文本是标准的 YouTube 网页页脚（版权和法律链接），不包含视频的实际逐字稿。本总结是基于与该特定标题相关的视频内容编写的。

---

## 7. Uplane (YC F25) 招聘创始工程师（全栈与 AI）

**原文标题**: Uplane (YC F25) Is Hiring Founding Engineers (Full-Stack and AI)

**原文链接**: [https://www.useparallel.com/uplane1/careers](https://www.useparallel.com/uplane1/careers)

**Uplane** 是 Y Combinator 2025 冬季（F25）批次的入选初创公司，目前正在招聘专注于**全栈**和 **AI** 开发的**创始工程师**职位。

作为新一届 YC 成员，Uplane 正在寻找具有高影响力的开发者，在最早期阶段加入其核心团队。“创始”职位的定位意味着这些工程师将对公司的技术架构、产品方向和企业文化产生深远影响。

此次招聘的核心亮点包括：

*   **岗位：** 创始全栈工程师和创始 AI 工程师。
*   **阶段：** 早期阶段（YC F25），提供从零开始构建产品的机会。
*   **技术重点：** 虽然目前信息较少，但“**ParallelLoading**”一词暗示产品可能专注于性能优化、高速数据传输或创新的 Web 架构。

对于希望进入初创生态系统并在风投支持的公司中担任领导角色的工程师来说，这是一个典型的高增长机会。

---

## 8. Programming languages used for music

**原文标题**: Programming languages used for music

**原文链接**: [https://timthompson.com/plum/cgi/showlist.cgi?sort=name&concise=yes](https://timthompson.com/plum/cgi/showlist.cgi?sort=name&concise=yes)

生成摘要时出错

---

## 9. Microsoft will kill obsolete cipher that has wreaked decades of havoc

**原文标题**: Microsoft will kill obsolete cipher that has wreaked decades of havoc

**原文链接**: [https://arstechnica.com/security/2025/12/microsoft-will-finally-kill-obsolete-cipher-that-has-wreaked-decades-of-havoc/](https://arstechnica.com/security/2025/12/microsoft-will-finally-kill-obsolete-cipher-that-has-wreaked-decades-of-havoc/)

生成摘要时出错

---

## 10. A guide to local coding models

**原文标题**: A guide to local coding models

**原文链接**: [https://www.aiforswes.com/p/you-dont-need-to-spend-100mo-on-claude](https://www.aiforswes.com/p/you-dont-need-to-spend-100mo-on-claude)

生成摘要时出错

---

## 11. Debian's Git Transition

**原文标题**: Debian's Git Transition

**原文链接**: [https://diziet.dreamwidth.org/20436.html](https://diziet.dreamwidth.org/20436.html)

生成摘要时出错

---

## 12. Jimmy Lai Is a Martyr for Freedom

**原文标题**: Jimmy Lai Is a Martyr for Freedom

**原文链接**: [https://reason.com/2025/12/19/jimmy-lai-is-a-martyr-for-freedom/](https://reason.com/2025/12/19/jimmy-lai-is-a-martyr-for-freedom/)

生成摘要时出错

---

## 13. If you don't design your career, someone else will (2014)

**原文标题**: If you don't design your career, someone else will (2014)

**原文链接**: [https://gregmckeown.com/if-you-dont-design-your-career-someone-else-will/](https://gregmckeown.com/if-you-dont-design-your-career-someone-else-will/)

生成摘要时出错

---

## 14. How I protect my Forgejo instance from AI web crawlers

**原文标题**: How I protect my Forgejo instance from AI web crawlers

**原文链接**: [https://her.esy.fun/posts/0031-how-i-protect-my-forgejo-instance-from-ai-web-crawlers/index.html](https://her.esy.fun/posts/0031-how-i-protect-my-forgejo-instance-from-ai-web-crawlers/index.html)

生成摘要时出错

---

## 15. Deliberate Internet Shutdowns

**原文标题**: Deliberate Internet Shutdowns

**原文链接**: [https://www.schneier.com/blog/archives/2025/12/deliberate-internet-shutdowns.html](https://www.schneier.com/blog/archives/2025/12/deliberate-internet-shutdowns.html)

生成摘要时出错

---

## 16. Benn Jordan – This Flock Camera Leak Is Like Netflix for Stalkers [video]

**原文标题**: Benn Jordan – This Flock Camera Leak Is Like Netflix for Stalkers [video]

**原文链接**: [https://www.youtube.com/watch?v=vU1-uiUlHTo](https://www.youtube.com/watch?v=vU1-uiUlHTo)

生成摘要时出错

---

## 17. Show HN: Backlog – a public repository of real work problems

**原文标题**: Show HN: Backlog – a public repository of real work problems

**原文链接**: [https://www.worldsbacklog.com/](https://www.worldsbacklog.com/)

生成摘要时出错

---

## 18. Decompiling the Synergy: Human–LLM Teaming in Reverse Engineering [pdf]

**原文标题**: Decompiling the Synergy: Human–LLM Teaming in Reverse Engineering [pdf]

**原文链接**: [https://www.zionbasque.com/files/papers/dec-synergy-study.pdf](https://www.zionbasque.com/files/papers/dec-synergy-study.pdf)

生成摘要时出错

---

## 19. The U.S. Is Funding Fewer Grants in Every Area of Science and Medicine

**原文标题**: The U.S. Is Funding Fewer Grants in Every Area of Science and Medicine

**原文链接**: [https://www.nytimes.com/interactive/2025/12/02/upshot/trump-science-funding-cuts.html](https://www.nytimes.com/interactive/2025/12/02/upshot/trump-science-funding-cuts.html)

生成摘要时出错

---

## 20. Show HN: Books mentioned on Hacker News in 2025

**原文标题**: Show HN: Books mentioned on Hacker News in 2025

**原文链接**: [https://hackernews-readings-613604506318.us-west1.run.app](https://hackernews-readings-613604506318.us-west1.run.app)

生成摘要时出错

---

## 21. Disney Imagineering Debuts Next-Generation Robotic Character, Olaf

**原文标题**: Disney Imagineering Debuts Next-Generation Robotic Character, Olaf

**原文链接**: [https://disneyparksblog.com/disney-experiences/robotic-olaf-marks-new-era-of-disney-innovation/](https://disneyparksblog.com/disney-experiences/robotic-olaf-marks-new-era-of-disney-innovation/)

生成摘要时出错

---

## 22. Webb observes exoplanet that may have an exotic helium and carbon atmosphere

**原文标题**: Webb observes exoplanet that may have an exotic helium and carbon atmosphere

**原文链接**: [https://science.nasa.gov/missions/webb/nasas-webb-observes-exoplanet-whose-composition-defies-explanation/](https://science.nasa.gov/missions/webb/nasas-webb-observes-exoplanet-whose-composition-defies-explanation/)

生成摘要时出错

---

## 23. Aliasing

**原文标题**: Aliasing

**原文链接**: [https://xania.org/202512/15-aliasing-in-general](https://xania.org/202512/15-aliasing-in-general)

生成摘要时出错

---

## 24. Build Android apps using Rust and Iced

**原文标题**: Build Android apps using Rust and Iced

**原文链接**: [https://github.com/ibaryshnikov/android-iced-example](https://github.com/ibaryshnikov/android-iced-example)

生成摘要时出错

---

## 25. Functional Flocking Quadtree in ClojureScript

**原文标题**: Functional Flocking Quadtree in ClojureScript

**原文链接**: [https://www.lbjgruppen.com/en/posts/flocking-quadtrees](https://www.lbjgruppen.com/en/posts/flocking-quadtrees)

生成摘要时出错

---

## 26. I'm just having fun

**原文标题**: I'm just having fun

**原文链接**: [https://jyn.dev/i-m-just-having-fun/](https://jyn.dev/i-m-just-having-fun/)

生成摘要时出错

---

## 27. CO2 batteries that store grid energy take off globally

**原文标题**: CO2 batteries that store grid energy take off globally

**原文链接**: [https://spectrum.ieee.org/co2-battery-energy-storage](https://spectrum.ieee.org/co2-battery-energy-storage)

生成摘要时出错

---

## 28. Cartoon Network channel errors (1995 – 2025)

**原文标题**: Cartoon Network channel errors (1995 – 2025)

**原文链接**: [https://cnas.fandom.com/wiki/Channel_Errors](https://cnas.fandom.com/wiki/Channel_Errors)

生成摘要时出错

---

## 29. Kernighan's Lever

**原文标题**: Kernighan's Lever

**原文链接**: [https://linusakesson.net/programming/kernighans-lever/index.php](https://linusakesson.net/programming/kernighans-lever/index.php)

生成摘要时出错

---

## 30. Inverse Parentheses

**原文标题**: Inverse Parentheses

**原文链接**: [https://kellett.im/a/inverse-parentheses](https://kellett.im/a/inverse-parentheses)

生成摘要时出错

---

## 31. Rue: Higher level than Rust, lower level than Go

**原文标题**: Rue: Higher level than Rust, lower level than Go

**原文链接**: [https://rue-lang.dev/](https://rue-lang.dev/)

生成摘要时出错

---

## 32. More on whether useful quantum computing is “imminent”

**原文标题**: More on whether useful quantum computing is “imminent”

**原文链接**: [https://scottaaronson.blog/?p=9425](https://scottaaronson.blog/?p=9425)

生成摘要时出错

---

## 33. Spotify reportedly investigating Anna's Archive's scraping of their library

**原文标题**: Spotify reportedly investigating Anna's Archive's scraping of their library

**原文链接**: [https://www.billboard.com/business/streaming/spotify-music-library-leak-1236143970/](https://www.billboard.com/business/streaming/spotify-music-library-leak-1236143970/)

生成摘要时出错

---

## 34. Well being in times of algorithms

**原文标题**: Well being in times of algorithms

**原文链接**: [https://www.ssp.sh/blog/well-being-algorithms/](https://www.ssp.sh/blog/well-being-algorithms/)

生成摘要时出错

---

## 35. Larry Ellison provides personal guarantee for Paramount takeover of Warner Bros

**原文标题**: Larry Ellison provides personal guarantee for Paramount takeover of Warner Bros

**原文链接**: [https://www.theguardian.com/business/2025/dec/22/larry-ellison-40-billion-paramount-warner-bros](https://www.theguardian.com/business/2025/dec/22/larry-ellison-40-billion-paramount-warner-bros)

生成摘要时出错

---

## 36. Italian Competition Authority Fines Apple $115M for Abusing Dominant Position

**原文标题**: Italian Competition Authority Fines Apple $115M for Abusing Dominant Position

**原文链接**: [https://en.agcm.it/en/media/press-releases/2025/12/A561](https://en.agcm.it/en/media/press-releases/2025/12/A561)

生成摘要时出错

---

## 37. Finland gave two groups identical payments – one saw better mental health

**原文标题**: Finland gave two groups identical payments – one saw better mental health

**原文链接**: [https://scottsantens.substack.com/p/finland-basic-income-experiment-mental-health-ubi](https://scottsantens.substack.com/p/finland-basic-income-experiment-mental-health-ubi)

生成摘要时出错

---

## 38. Flock Exposed Its AI-Powered Cameras to the Internet. We Tracked Ourselves

**原文标题**: Flock Exposed Its AI-Powered Cameras to the Internet. We Tracked Ourselves

**原文链接**: [https://www.404media.co/flock-exposed-its-ai-powered-cameras-to-the-internet-we-tracked-ourselves/](https://www.404media.co/flock-exposed-its-ai-powered-cameras-to-the-internet-we-tracked-ourselves/)

生成摘要时出错

---

## 39. ONNX Runtime and CoreML May Silently Convert Your Model to FP16

**原文标题**: ONNX Runtime and CoreML May Silently Convert Your Model to FP16

**原文链接**: [https://ym2132.github.io/ONNX_MLProgram_NN_exploration](https://ym2132.github.io/ONNX_MLProgram_NN_exploration)

生成摘要时出错

---

## 40. Mystery as YouTube creator's finance livestream appears on White House website

**原文标题**: Mystery as YouTube creator's finance livestream appears on White House website

**原文链接**: [https://apnews.com/article/white-house-website-youtube-livestream-88d79b896ca6e5ecea33f3bf3e5c9278](https://apnews.com/article/white-house-website-youtube-livestream-88d79b896ca6e5ecea33f3bf3e5c9278)

生成摘要时出错

---

## 41. Show HN: WalletWallet – create Apple passes from anything

**原文标题**: Show HN: WalletWallet – create Apple passes from anything

**原文链接**: [https://walletwallet.alen.ro/](https://walletwallet.alen.ro/)

生成摘要时出错

---

## 42. I program on the subway

**原文标题**: I program on the subway

**原文链接**: [https://www.scd31.com/posts/programming-on-the-subway](https://www.scd31.com/posts/programming-on-the-subway)

生成摘要时出错

---

## 43. Toxic Fumes on Planes Blamed for Deaths of Pilots and Crew

**原文标题**: Toxic Fumes on Planes Blamed for Deaths of Pilots and Crew

**原文链接**: [https://www.wsj.com/business/airlines/toxic-fumes-airplane-pilot-crew-death-739fa3bb](https://www.wsj.com/business/airlines/toxic-fumes-airplane-pilot-crew-death-739fa3bb)

生成摘要时出错

---

## 44. A Guide to Magnetizing N48 Magnets in Ansys Maxwell

**原文标题**: A Guide to Magnetizing N48 Magnets in Ansys Maxwell

**原文链接**: [https://blog.ozeninc.com/resources/from-datasheet-to-demagnetization-a-guide-to-magnetizing-n48-magnets-in-ansys-maxwell](https://blog.ozeninc.com/resources/from-datasheet-to-demagnetization-a-guide-to-magnetizing-n48-magnets-in-ansys-maxwell)

生成摘要时出错

---

## 45. When the Power Went Out in San Francisco, So Did Waymo's Robotaxis

**原文标题**: When the Power Went Out in San Francisco, So Did Waymo's Robotaxis

**原文链接**: [https://insideevs.com/news/782523/waymo-robotaxi-san-francisco-outage-power/](https://insideevs.com/news/782523/waymo-robotaxi-san-francisco-outage-power/)

生成摘要时出错

---

## 46. Waymo halts service during S.F. blackout after causing traffic jams

**原文标题**: Waymo halts service during S.F. blackout after causing traffic jams

**原文链接**: [https://missionlocal.org/2025/12/sf-waymo-halts-service-blackout/](https://missionlocal.org/2025/12/sf-waymo-halts-service-blackout/)

生成摘要时出错

---

## 47. I wish people were more public

**原文标题**: I wish people were more public

**原文链接**: [https://borretti.me/article/i-wish-people-were-more-public](https://borretti.me/article/i-wish-people-were-more-public)

生成摘要时出错

---

## 48. Show HN: Rust/WASM lighting data toolkit – parses legacy formats, generates SVGs

**原文标题**: Show HN: Rust/WASM lighting data toolkit – parses legacy formats, generates SVGs

**原文链接**: [https://eulumdat.icu](https://eulumdat.icu)

生成摘要时出错

---

## 49. America's monopoly crisis hits the military

**原文标题**: America's monopoly crisis hits the military

**原文链接**: [https://www.theamericanconservative.com/americas-monopoly-crisis-hits-the-military/](https://www.theamericanconservative.com/americas-monopoly-crisis-hits-the-military/)

生成摘要时出错

---

## 50. The Going Dark initiative or ProtectEU is a Chat Control 3.0 attempt

**原文标题**: The Going Dark initiative or ProtectEU is a Chat Control 3.0 attempt

**原文链接**: [https://mastodon.online/@mullvadnet/115742530333573065](https://mastodon.online/@mullvadnet/115742530333573065)

生成摘要时出错

---

## 51. Making the most of bit arrays in Gleam

**原文标题**: Making the most of bit arrays in Gleam

**原文链接**: [https://gearsco.de/blog/bit-array-syntax/](https://gearsco.de/blog/bit-array-syntax/)

生成摘要时出错

---

## 52. The gift card accountability sink

**原文标题**: The gift card accountability sink

**原文链接**: [https://www.bitsaboutmoney.com/archive/gift-card-accountability-sink/](https://www.bitsaboutmoney.com/archive/gift-card-accountability-sink/)

生成摘要时出错

---

## 53. New Trump envoy says he will serve to make Greenland part of US

**原文标题**: New Trump envoy says he will serve to make Greenland part of US

**原文链接**: [https://www.bbc.com/news/articles/ckgmd132ge4o](https://www.bbc.com/news/articles/ckgmd132ge4o)

生成摘要时出错

---

## 54. Lightning: Real-time editing for tiled map data

**原文标题**: Lightning: Real-time editing for tiled map data

**原文链接**: [https://felt.com/blog/lightning-tiles](https://felt.com/blog/lightning-tiles)

生成摘要时出错

---

## 55. E.W.Dijkstra Archive

**原文标题**: E.W.Dijkstra Archive

**原文链接**: [https://www.cs.utexas.edu/~EWD/welcome.html](https://www.cs.utexas.edu/~EWD/welcome.html)

生成摘要时出错

---

## 56. The rise of deepfake cyberbullying poses a growing problem for schools

**原文标题**: The rise of deepfake cyberbullying poses a growing problem for schools

**原文链接**: [https://apnews.com/article/deepfake-ai-school-cyberbullying-takeaways-bf65455142a088824d3571a727d9a8c7](https://apnews.com/article/deepfake-ai-school-cyberbullying-takeaways-bf65455142a088824d3571a727d9a8c7)

生成摘要时出错

---

## 57. Evaluating chain-of-thought monitorability

**原文标题**: Evaluating chain-of-thought monitorability

**原文链接**: [https://openai.com/index/evaluating-chain-of-thought-monitorability/](https://openai.com/index/evaluating-chain-of-thought-monitorability/)

生成摘要时出错

---

## 58. Show HN: Jmail – Google Suite for Epstein files

**原文标题**: Show HN: Jmail – Google Suite for Epstein files

**原文链接**: [https://www.jmail.world](https://www.jmail.world)

生成摘要时出错

---

## 59. Structured outputs create false confidence

**原文标题**: Structured outputs create false confidence

**原文链接**: [https://boundaryml.com/blog/structured-outputs-create-false-confidence](https://boundaryml.com/blog/structured-outputs-create-false-confidence)

生成摘要时出错

---

## 60. You’re not burnt out, you’re existentially starving

**原文标题**: You’re not burnt out, you’re existentially starving

**原文链接**: [https://neilthanedar.com/youre-not-burnt-out-youre-existentially-starving/](https://neilthanedar.com/youre-not-burnt-out-youre-existentially-starving/)

生成摘要时出错

---

## 61. Lua 5.5.0 Released

**原文标题**: Lua 5.5.0 Released

**原文链接**: [https://lua.org/versions.html#5.5](https://lua.org/versions.html#5.5)

生成摘要时出错

---

## 62. Autoland saves King Air, everyone reported safe

**原文标题**: Autoland saves King Air, everyone reported safe

**原文链接**: [https://avbrief.com/autoland-saves-king-air-everyone-reported-safe/](https://avbrief.com/autoland-saves-king-air-everyone-reported-safe/)

生成摘要时出错

---

## 63. QBasic64 Phoenix 4.3.0 Released

**原文标题**: QBasic64 Phoenix 4.3.0 Released

**原文链接**: [https://qb64phoenix.com/forum/showthread.php?tid=4244](https://qb64phoenix.com/forum/showthread.php?tid=4244)

生成摘要时出错

---

## 64. I can't upgrade to Windows 11, now leave me alone

**原文标题**: I can't upgrade to Windows 11, now leave me alone

**原文链接**: [https://idiallo.com/byte-size/cant-update-to-windows-11-leave-me-alone](https://idiallo.com/byte-size/cant-update-to-windows-11-leave-me-alone)

生成摘要时出错

---

## 65. Single-Pass Huffman Coding

**原文标题**: Single-Pass Huffman Coding

**原文链接**: [https://doisinkidney.com/posts/2018-02-17-single-pass-huffman.html](https://doisinkidney.com/posts/2018-02-17-single-pass-huffman.html)

生成摘要时出错

---

## 66. Backing up Spotify

**原文标题**: Backing up Spotify

**原文链接**: [https://annas-archive.li/blog/backing-up-spotify.html](https://annas-archive.li/blog/backing-up-spotify.html)

生成摘要时出错

---

## 67. Measuring AI Ability to Complete Long Tasks

**原文标题**: Measuring AI Ability to Complete Long Tasks

**原文链接**: [https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)

生成摘要时出错

---

## 68. ARIN Public Incident Report – 4.10 Misissuance Error

**原文标题**: ARIN Public Incident Report – 4.10 Misissuance Error

**原文链接**: [https://www.arin.net/announcements/20251212/](https://www.arin.net/announcements/20251212/)

生成摘要时出错

---

## 69. Coarse is better

**原文标题**: Coarse is better

**原文链接**: [https://borretti.me/article/coarse-is-better](https://borretti.me/article/coarse-is-better)

生成摘要时出错

---

## 70. 24/192 Music Downloads are Silly Indeed (2012)

**原文标题**: 24/192 Music Downloads are Silly Indeed (2012)

**原文链接**: [https://people.xiph.org/~xiphmont/demo/neil-young.html](https://people.xiph.org/~xiphmont/demo/neil-young.html)

生成摘要时出错

---

## 71. Does Software Piracy Exist?

**原文标题**: Does Software Piracy Exist?

**原文链接**: [https://matthewbutterick.com/chron/does-software-piracy-exist.html](https://matthewbutterick.com/chron/does-software-piracy-exist.html)

生成摘要时出错

---

## 72. Cursed circuits #3: true mathematics

**原文标题**: Cursed circuits #3: true mathematics

**原文链接**: [https://lcamtuf.substack.com/p/cursed-circuits-3-true-mathematics](https://lcamtuf.substack.com/p/cursed-circuits-3-true-mathematics)

生成摘要时出错

---

## 73. Get an AI code review in 10 seconds

**原文标题**: Get an AI code review in 10 seconds

**原文链接**: [https://oldmanrahul.com/2025/12/19/ai-code-review-trick/](https://oldmanrahul.com/2025/12/19/ai-code-review-trick/)

生成摘要时出错

---

## 74. New mathematical framework reshapes debate over simulation hypothesis

**原文标题**: New mathematical framework reshapes debate over simulation hypothesis

**原文链接**: [https://www.santafe.edu/news-center/news/new-mathematical-framework-reshapes-debate-over-simulation-hypothesis](https://www.santafe.edu/news-center/news/new-mathematical-framework-reshapes-debate-over-simulation-hypothesis)

生成摘要时出错

---

## 75. Show HN: Shittp – Volatile Dotfiles over SSH

**原文标题**: Show HN: Shittp – Volatile Dotfiles over SSH

**原文链接**: [https://github.com/FOBshippingpoint/shittp](https://github.com/FOBshippingpoint/shittp)

生成摘要时出错

---

## 76. James Webb Space Telescope confirms first 'runaway' supermassive black hole

**原文标题**: James Webb Space Telescope confirms first 'runaway' supermassive black hole

**原文链接**: [https://www.space.com/astronomy/black-holes/james-webb-space-telescope-confirms-1st-runaway-supermassive-black-hole-rocketing-through-cosmic-owl-galaxies-at-2-2-million-mph-it-boggles-the-mind](https://www.space.com/astronomy/black-holes/james-webb-space-telescope-confirms-1st-runaway-supermassive-black-hole-rocketing-through-cosmic-owl-galaxies-at-2-2-million-mph-it-boggles-the-mind)

生成摘要时出错

---

## 77. Three ways to solve problems

**原文标题**: Three ways to solve problems

**原文链接**: [https://andreasfragner.com/writing/three-ways-to-solve-problems](https://andreasfragner.com/writing/three-ways-to-solve-problems)

生成摘要时出错

---

## 78. (Social) media manipulation in one image

**原文标题**: (Social) media manipulation in one image

**原文链接**: [https://kerkour.com/social-media-manipulation](https://kerkour.com/social-media-manipulation)

生成摘要时出错

---

## 79. 86Box v5.3

**原文标题**: 86Box v5.3

**原文链接**: [https://86box.net/2025/12/21/86box-v5-3.html](https://86box.net/2025/12/21/86box-v5-3.html)

生成摘要时出错

---

## 80. Exploring Speculative JIT Compilation for Emacs Lisp with Java

**原文标题**: Exploring Speculative JIT Compilation for Emacs Lisp with Java

**原文链接**: [https://kyo.iroiro.party/en/posts/juicemacs-exploring-jit-for-elisp/](https://kyo.iroiro.party/en/posts/juicemacs-exploring-jit-for-elisp/)

生成摘要时出错

---

## 81. Show HN: RenderCV – Open-source CV/resume generator, YAML to PDF

**原文标题**: Show HN: RenderCV – Open-source CV/resume generator, YAML to PDF

**原文链接**: [https://github.com/rendercv/rendercv](https://github.com/rendercv/rendercv)

生成摘要时出错

---

## 82. Show HN: HN Wrapped 2025 - an LLM reviews your year on HN

**原文标题**: Show HN: HN Wrapped 2025 - an LLM reviews your year on HN

**原文链接**: [https://hn-wrapped.kadoa.com?year=2025](https://hn-wrapped.kadoa.com?year=2025)

生成摘要时出错

---

## 83. Ruby website redesigned

**原文标题**: Ruby website redesigned

**原文链接**: [https://www.ruby-lang.org/en/](https://www.ruby-lang.org/en/)

生成摘要时出错

---

## 84. Inca Stone Masonry

**原文标题**: Inca Stone Masonry

**原文链接**: [https://www.earthasweknowit.com/pages/inca_construction](https://www.earthasweknowit.com/pages/inca_construction)

生成摘要时出错

---

## 85. Indoor tanning makes youthful skin much older on a genetic level

**原文标题**: Indoor tanning makes youthful skin much older on a genetic level

**原文链接**: [https://www.ucsf.edu/news/2025/12/431206/indoor-tanning-makes-youthful-skin-much-older-genetic-level](https://www.ucsf.edu/news/2025/12/431206/indoor-tanning-makes-youthful-skin-much-older-genetic-level)

生成摘要时出错

---

## 86. I doubt that anything resembling genuine AGI is within reach of current AI tools

**原文标题**: I doubt that anything resembling genuine AGI is within reach of current AI tools

**原文链接**: [https://mathstodon.xyz/@tao/115722360006034040](https://mathstodon.xyz/@tao/115722360006034040)

生成摘要时出错

---

## 87. Decompiling the New C# 14 field Keyword

**原文标题**: Decompiling the New C# 14 field Keyword

**原文链接**: [https://blog.ivankahl.com/decompiling-the-new-csharp-14-field-keyword/](https://blog.ivankahl.com/decompiling-the-new-csharp-14-field-keyword/)

生成摘要时出错

---

## 88. Why do people leave comments on OpenBenches?

**原文标题**: Why do people leave comments on OpenBenches?

**原文链接**: [https://shkspr.mobi/blog/2025/12/why-do-people-leave-comments-on-openbenches/](https://shkspr.mobi/blog/2025/12/why-do-people-leave-comments-on-openbenches/)

生成摘要时出错

---

## 89. History LLMs: Models trained exclusively on pre-1913 texts

**原文标题**: History LLMs: Models trained exclusively on pre-1913 texts

**原文链接**: [https://github.com/DGoettlich/history-llms](https://github.com/DGoettlich/history-llms)

生成摘要时出错

---

## 90. Privacy doesn't mean anything anymore, anonymity does

**原文标题**: Privacy doesn't mean anything anymore, anonymity does

**原文链接**: [https://servury.com/blog/privacy-is-marketing-anonymity-is-architecture/](https://servury.com/blog/privacy-is-marketing-anonymity-is-architecture/)

生成摘要时出错

---

## 91. Show HN: The Official National Train Map Sucked, So I Made My Own

**原文标题**: Show HN: The Official National Train Map Sucked, So I Made My Own

**原文链接**: [https://www.bdzmap.com/](https://www.bdzmap.com/)

生成摘要时出错

---

## 92. Isengard in Oxford

**原文标题**: Isengard in Oxford

**原文链接**: [https://lareviewofbooks.org/article/isengard-in-oxford/](https://lareviewofbooks.org/article/isengard-in-oxford/)

生成摘要时出错

---

## 93. Evolution by natural induction

**原文标题**: Evolution by natural induction

**原文链接**: [https://royalsocietypublishing.org/rsfs/article/15/6/20250025/366156/Evolution-by-natural-induction](https://royalsocietypublishing.org/rsfs/article/15/6/20250025/366156/Evolution-by-natural-induction)

生成摘要时出错

---

## 94. CD Extended Graphics

**原文标题**: CD Extended Graphics

**原文链接**: [https://extended.graphics/](https://extended.graphics/)

生成摘要时出错

---

## 95. That's Not a Blobfish: Deep Sea Social Media Is Flooded by AI Slop

**原文标题**: That's Not a Blobfish: Deep Sea Social Media Is Flooded by AI Slop

**原文链接**: [https://www.southernfriedscience.com/thats-not-a-blobfish-deep-sea-social-media-is-flooded-by-ai-slop/](https://www.southernfriedscience.com/thats-not-a-blobfish-deep-sea-social-media-is-flooded-by-ai-slop/)

生成摘要时出错

---

## 96. Go ahead, self-host Postgres

**原文标题**: Go ahead, self-host Postgres

**原文链接**: [https://pierce.dev/notes/go-ahead-self-host-postgres#user-content-fn-1](https://pierce.dev/notes/go-ahead-self-host-postgres#user-content-fn-1)

生成摘要时出错

---

## 97. You have reached the end of the internet (2006)

**原文标题**: You have reached the end of the internet (2006)

**原文链接**: [https://hmpg.net/](https://hmpg.net/)

生成摘要时出错

---

## 98. Archive.org Is Down

**原文标题**: Archive.org Is Down

**原文链接**: [https://www.archive.org](https://www.archive.org)

生成摘要时出错

---

## 99. Europe gets serious about cutting digital umbilical chord with US big tech

**原文标题**: Europe gets serious about cutting digital umbilical chord with US big tech

**原文链接**: [https://www.theregister.com/2025/12/22/europe_gets_serious_about_cutting/](https://www.theregister.com/2025/12/22/europe_gets_serious_about_cutting/)

生成摘要时出错

---

## 100. The uncertain origins of aspirin

**原文标题**: The uncertain origins of aspirin

**原文链接**: [https://www.asimov.press/p/aspirin](https://www.asimov.press/p/aspirin)

生成摘要时出错

---

