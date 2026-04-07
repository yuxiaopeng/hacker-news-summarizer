# Hacker News 热门文章摘要 (2026-04-07)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. GLM-5.1：迈向长时程任务

**原文标题**: GLM-5.1: Towards Long-Horizon Tasks

**原文链接**: [https://z.ai/blog/glm-5.1](https://z.ai/blog/glm-5.1)

智谱 AI 最近发布了 **GLM-5.1**，这是其模型系列的重大升级，专为胜任“长程任务”（long-horizon tasks）而设计。这类任务通常涉及复杂问题，需要多步推理、长期规划和自主执行。

**核心信息与亮点：**

*   **聚焦长程推理：** GLM-5.1 针对无法一蹴而就的任务进行了优化。它采用了“推理模式”（类似于 OpenAI 的 o1 系列），利用扩展的思维链（CoT）处理能力来拆解并解决复杂难题。
*   **增强的智能体能力：** 该模型在“智能体（agentic）”工作流中表现卓越，能够自主使用工具、进行深度网页搜索，并整合多方信息以完成深度研究或软件开发等专业级任务。
*   **性能基准：** GLM-5.1-Preview 在与 GPT-4o 和 o1-mini 等全球领先模型的对比中展现出强劲的竞争力。它在数学、编程和逻辑推理方面有显著提升，并具备遵循复杂、多层级指令的能力。
*   **系统性智能：** 此次更新不仅关注“下一词预测”，更强调系统性智能。这包括推理过程中的纠错能力，以及处理长上下文信息时更高的稳定性。
*   **可用性：** 该模型正被整合至智谱清言平台并提供 API 接入，目标群体是希望构建自主 AI 智能体的开发者和企业。

通过将规划和执行置于简单的内容生成之上，GLM-5.1 代表了智谱 AI 向“系统 2”思维的转变——即打造更慢、更深思熟虑且更可靠的 AI，以应对现实世界的专业工作流。

---

## 2. Show HN：粗野主义混凝土笔记本电脑支架 (2024)

**原文标题**: Show HN: Brutalist Concrete Laptop Stand (2024)

**原文链接**: [https://sam-burns.com/posts/concrete-laptop-stand/](https://sam-burns.com/posts/concrete-laptop-stand/)

受20世纪60年代野兽派建筑和“城市衰败”理念的启发，作者创作了一款独特的DIY“清水混凝土”（beton brut）笔记本电脑支架。这款支架被戏称为“全球最重”，将硬朗的工业美学与现代功能性融为一体。

**主要特点与设计**
该支架集成了多项功能：
*   **电源连接：** 配有一个三脚插座和两个2.1安培的USB充电口。
*   **城市美学：** 设计元素包括“破损”的墙角、锈迹斑斑的钢筋和被腐蚀的铜线，旨在模拟废弃建筑的景象。
*   **内置配件：** 一个由酥油罐改造的嵌入式花盆，种有“珍珠吊兰”；以及一个经过人工做旧、表面涂有混沙丙烯颜料以模仿青苔质感的生锈笔筒。

**制作过程**
该项目涉及两次主要的混凝土浇筑。为了营造饱经风霜的观感，混凝土的搅拌并不均匀，并在后期经过打磨以露出内部的碎石。作者强调了震动处理的重要性——具体是使用振动器作为动力工具，以去除中型模具中的气泡。

为了强化破旧感，作者利用化学工艺对材料进行了老化处理。铜线经过氨水溶液处理产生蓝色铜绿，而钢筋和笔筒则使用盐、水和过氧化氢的混合液制造锈迹。出于安全考虑，那些“破损”的外露电线纯粹是装饰性的，实际通电的电源线被安全地隐藏在结构内部。

**结论**
虽然支架极重，搬运时甚至需要动用手推车，但作者认为该项目取得了成功。它不仅是一件功能性的艺术品，更捕捉到了“城市探险”和清水混凝土建筑的独特之美。

---

## 3. Cloudflare 计划到 2029 年实现全面后量子安全

**原文标题**: Cloudflare targets 2029 for full post-quantum security

**原文链接**: [https://blog.cloudflare.com/post-quantum-roadmap/](https://blog.cloudflare.com/post-quantum-roadmap/)

Cloudflare 已加速其后量子（PQ）路线图，目标是在 **2029 年** 实现全线产品的完整后量子安全。这一转变是由 Google 和 Oratomic 最近的突破推动的，相关研究表明，“Q-Day”（即量子计算机能够破解标准密码学的时刻）可能早在 2029 年或 2030 年到来，远早于此前预测的 2035 年。

**关键技术驱动因素**
近期研究表明，中性原子量子计算机破解 RSA-2048 和 P-256 加密所需的量子比特（低至 10,000 个）和纠错能力可能远低于此前预期。Google 最近展示的一种能大幅提升椭圆曲线密码学破解效率的算法，进一步增强了紧迫感。

**从加密转向身份验证**
尽管 Cloudflare 已通过后量子加密保护了 65% 的流量免受“先抓取、后解密”攻击，但现在的焦点已转向**后量子身份验证**。如果身份验证被攻破，攻击者可以伪造数字签名、冒充服务器并获得系统的持久访问权。Cloudflare 将根证书和 API 凭据等长效密钥列为迁移的最高优先级目标。

**路线图与建议**
Cloudflare 的转型包含一项多年计划，包括升级内部系统、管理第三方依赖关系，并最终禁用易受量子攻击的传统密码学，以防止降级攻击。

Cloudflare 建议：
*   **企业：** 将后量子支持作为所有新技术采购的必要条件。
*   **政府：** 授权牵头机构设定明确的迁移时间表，并采用国际标准。
*   **客户：** 针对 Cloudflare 服务无需采取立即行动，因为后量子安全将默认启用且不收取额外费用。不过，完全的安全性仍取决于浏览器和源站服务器的后续升级。

---

## 4. 柬埔寨为著名扫雷鼠马加瓦的雕像揭幕。

**原文标题**: Cambodia unveils a statue of famous landmine-sniffing rat Magawa

**原文链接**: [https://www.bbc.com/news/articles/c0rx7xzd10xo](https://www.bbc.com/news/articles/c0rx7xzd10xo)

柬埔寨在暹粒揭幕了一座石像，以纪念传奇的非洲巨鼠马加瓦（Magawa），表彰其在探测地雷方面拯救生命的卓越贡献。该纪念碑在“国际提高地雷意识日”（4月4日）前夕揭幕，旨在纪念历史上首只获得PDSA黄金奖章（相当于动物界的乔治十字勋章）的老鼠。

在比利时慈善机构Apopo服役的五年间（2016–2021年），马加瓦共发现100多枚地雷和未爆炸弹药，清理土地面积超过14.1万平方米。他的工作效率极高：搜索一个网球场大小的区域仅需20分钟，而人工排雷员则需要数天。马加瓦于2021年退役，并于2022年去世，终年八岁。

这座雕像深刻地警示着柬埔寨面临的持续威胁——目前仍有100多万人生活在受爆炸物污染的土地上。柬埔寨政府已设定目标，计划到2030年实现全境无雷。Apopo的“英雄鼠”因其体重极轻（不足以触发地雷）且嗅觉灵敏，非常适合此类工作。除排雷外，这些老鼠还接受了探测肺结核和打击非法野生动物贸易的训练。

虽然马加瓦是这些啮齿动物中最负盛名的一只，但文章提到，一只名为罗宁（Ronin）的新老鼠近期打破了他的纪录，自2021年以来已发现109枚地雷。这座雕像不仅是对马加瓦传奇功绩的致敬，也肯定了这些动物在全球人道主义事业中所发挥的关键作用。

---

## 5. 谷歌开源实验性智能体编排测试平台 Scion

**原文标题**: Google open-sources experimental agent orchestration testbed Scion

**原文链接**: [https://www.infoq.com/news/2026/04/google-agent-testbed-scion/](https://www.infoq.com/news/2026/04/google-agent-testbed-scion/)

Google 开源了 Scion，这是一个实验性的多智能体编排测试平台，旨在管理跨本地和远程计算环境的并发 AI 智能体。Google 将其描述为“智能体的 Hypervisor”，Scion 允许开发者在隔离的容器内运行 Gemini、Claude Code 和 Codex 等专用模型，确保它们可以在项目的不同部分协同工作而互不干扰。

Scion 的一个核心特征是“隔离优于限制”。Scion 并不通过复杂的提示词规则来限制智能体的行为，而是鼓励智能体以“--yolo 模式”运行。安全性在基础设施层面得到强化：每个智能体都拥有独立的容器、git 工作树和凭据，并受到网络策略和安全护栏的监管。

该平台的主要特性包括：
*   **动态任务管理：** Scion 管理着一个并行演进的任务图，支持长期存在的专用智能体和临时的任务特定工作者。
*   **广泛的兼容性：** 通过名为“harnesses”的适配器，它支持各种流行智能体，并集成了 Docker、Podman 和 Kubernetes 等容器运行时。
*   **基础设施灵活性：** 智能体可以在本地、远程虚拟机或跨 Kubernetes 集群运行。

为了展示 Scion 的功能，Google 发布了《雅典娜神庙遗迹》（Relics of the Athenaeum），这是一款多组智能体通过共享工作区和即时消息协作解决计算难题的游戏。该示例展示了中央“游戏运行器”如何动态产生专用智能体来处理复杂的多层挑战。通过提供这一测试平台，Google 旨在简化复杂多智能体系统中记忆、任务管理和通信的集成。

---

## 6. 硬件提速：从实验室到1亿美元ARR的经验启示

**原文标题**: Moving fast in hardware: lessons from lab to $100M ARR

**原文链接**: [https://blog.zacka.io/p/simplify-then-add-lightness-bc4](https://blog.zacka.io/p/simplify-then-add-lightness-bc4)

在《硬件领域的快速推进》一文中，ClearMotion 联合创始人 Zack Anderson 概述了硬科技公司如何通过减少“学习循环的质量”（mass of the learning loop）来实现从实验室原型到 1 亿美元年度经常性收入（ARR）的规模化扩张。硬件领域的提速通过三大核心原则实现：

**1. 删减需求：**
工程效率往往源于“减法”而非“优化”。多数项目进度缓慢是因为承担了不必要的“需求负载”。ClearMotion 通过针对实际驾驶场景而非极端的教科书级边缘案例进行设计，将成本降低了 90%。同样，NASA 的阿波罗计划也是在放弃将整个航天器降落在月球的要求后，才得以在截止日期前完成。Anderson 还以 SpaceX 使用冗余商业部件替代昂贵的航天级组件，以及 Gossamer Condor 的“一次性”设计为例，说明了移除传统需求如何能实现快速迭代。

**2. 原型即实验：**
原型的设计初衷应是化解特定风险，而非充当缩微版的量产单元。Boom Supersonic 和特斯拉等成功企业会通过风险排序，一次解决一个主要未知项（例如：先解决空气动力学，再解决制造，最后实现规模化）。相比之下，Lilliputian Systems 等公司的失败则源于试图并行解决技术、监管和制造等挑战。Anderson 强调，应利用现代仿真技术和人工智能在投入物理硬件开发之前对设计进行筛选。

**3. 自主处理不确定性：**
一个关键错误是在完全掌握装配流程之前，就将制造外包给成熟的供应商。外部一级供应商（Tier-1）的官僚作风会拖慢学习循环。为了快速行动，团队应让早期生产线贴近工程师，以确保即时反馈和快速故障排除。

归根结底，硬件领域的成功需要有“先简化，后轻量化”的勇气，并确保学习速率超过资源消耗速率。

---

## 7. AI 助力 OldNYC 新增 1 万张照片

**原文标题**: AI helps add 10k more photos to OldNYC

**原文链接**: [https://www.danvk.org/2026/03/08/oldnyc-updates.html](https://www.danvk.org/2026/03/08/oldnyc-updates.html)

生成摘要时出错

---

## 8. Rescuing old printers with an in-browser Linux VM bridged to WebUSB over USB/IP

**原文标题**: Rescuing old printers with an in-browser Linux VM bridged to WebUSB over USB/IP

**原文链接**: [https://printervention.app/details](https://printervention.app/details)

生成摘要时出错

---

## 9. We found an undocumented bug in the Apollo 11 guidance computer code

**原文标题**: We found an undocumented bug in the Apollo 11 guidance computer code

**原文链接**: [https://www.juxt.pro/blog/a-bug-on-the-dark-side-of-the-moon/](https://www.juxt.pro/blog/a-bug-on-the-dark-side-of-the-moon/)

生成摘要时出错

---

## 10. A new Postcrossing stamp from the USA

**原文标题**: A new Postcrossing stamp from the USA

**原文链接**: [https://www.postcrossing.com/blog/2026/03/31/a-new-postcrossing-stamp-from-the-usa](https://www.postcrossing.com/blog/2026/03/31/a-new-postcrossing-stamp-from-the-usa)

生成摘要时出错

---

## 11. Good Taste the Only Real Moat Left

**原文标题**: Good Taste the Only Real Moat Left

**原文链接**: [https://rajnandan.com/posts/taste-in-the-age-of-ai-and-llms/](https://rajnandan.com/posts/taste-in-the-age-of-ai-and-llms/)

生成摘要时出错

---

## 12. 12k Tons of Dumped Orange Peel Grew into a Landscape Nobody Expected (2017)

**原文标题**: 12k Tons of Dumped Orange Peel Grew into a Landscape Nobody Expected (2017)

**原文链接**: [https://www.sciencealert.com/how-12-000-tonnes-of-dumped-orange-peel-produced-something-nobody-imagined](https://www.sciencealert.com/how-12-000-tonnes-of-dumped-orange-peel-produced-something-nobody-imagined)

生成摘要时出错

---

## 13. Dropping Cloudflare for Bunny.net

**原文标题**: Dropping Cloudflare for Bunny.net

**原文链接**: [https://jola.dev/posts/dropping-cloudflare](https://jola.dev/posts/dropping-cloudflare)

生成摘要时出错

---

## 14. John Coltrane Illustrates the Mathematics of Jazz

**原文标题**: John Coltrane Illustrates the Mathematics of Jazz

**原文链接**: [https://www.americanjazzmusicsociety.com/blog/john-coltrane-draws](https://www.americanjazzmusicsociety.com/blog/john-coltrane-draws)

生成摘要时出错

---

## 15. 9 Mothers (YC P26) Is Hiring – Lead Robotics and More

**原文标题**: 9 Mothers (YC P26) Is Hiring – Lead Robotics and More

**原文链接**: [https://jobs.ashbyhq.com/9-mothers?utm_source=x8pZ4B3P3Q](https://jobs.ashbyhq.com/9-mothers?utm_source=x8pZ4B3P3Q)

生成摘要时出错

---

## 16. Emotion Concepts and Their Function in a Large Language Model

**原文标题**: Emotion Concepts and Their Function in a Large Language Model

**原文链接**: [https://transformer-circuits.pub/2026/emotions/index.html](https://transformer-circuits.pub/2026/emotions/index.html)

生成摘要时出错

---

## 17. Show HN: A cartographer's attempt to realistically map Tolkien's world

**原文标题**: Show HN: A cartographer's attempt to realistically map Tolkien's world

**原文链接**: [https://www.intofarlands.com/atlasofarda](https://www.intofarlands.com/atlasofarda)

生成摘要时出错

---

## 18. Every GPU That Mattered

**原文标题**: Every GPU That Mattered

**原文链接**: [https://sheets.works/data-viz/every-gpu](https://sheets.works/data-viz/every-gpu)

生成摘要时出错

---

## 19. You can't cancel a JavaScript promise (except sometimes you can)

**原文标题**: You can't cancel a JavaScript promise (except sometimes you can)

**原文链接**: [https://www.inngest.com/blog/hanging-promises-for-control-flow](https://www.inngest.com/blog/hanging-promises-for-control-flow)

生成摘要时出错

---

## 20. SQLite in Production: Lessons from Running a Store on a Single File

**原文标题**: SQLite in Production: Lessons from Running a Store on a Single File

**原文链接**: [https://ultrathink.art/blog/sqlite-in-production-lessons](https://ultrathink.art/blog/sqlite-in-production-lessons)

生成摘要时出错

---

## 21. Identify a London Underground Line just by listening to it

**原文标题**: Identify a London Underground Line just by listening to it

**原文链接**: [https://tubesoundquiz.com/](https://tubesoundquiz.com/)

生成摘要时出错

---

## 22. Show HN: Finalrun – Spec-driven testing using English and vision for mobile apps

**原文标题**: Show HN: Finalrun – Spec-driven testing using English and vision for mobile apps

**原文链接**: [https://github.com/final-run/finalrun-agent](https://github.com/final-run/finalrun-agent)

生成摘要时出错

---

## 23. My Experience as a Rice Farmer

**原文标题**: My Experience as a Rice Farmer

**原文链接**: [https://xd009642.github.io/2026/04/01/My-Experience-as-a-Rice-Farmer.html](https://xd009642.github.io/2026/04/01/My-Experience-as-a-Rice-Farmer.html)

生成摘要时出错

---

## 24. Global Physics Photowalk: 2025 winners revealed

**原文标题**: Global Physics Photowalk: 2025 winners revealed

**原文链接**: [https://www.quantamagazine.org/global-physics-photowalk-2025-winners-revealed-20260401/](https://www.quantamagazine.org/global-physics-photowalk-2025-winners-revealed-20260401/)

生成摘要时出错

---

## 25. A whole civilization might die tonight

**原文标题**: A whole civilization might die tonight

**原文链接**: [https://www.nbcnews.com/politics/white-house/trump-threat-whole-civilization-will-die-iran-war-deadline-hormuz-rcna267059](https://www.nbcnews.com/politics/white-house/trump-threat-whole-civilization-will-die-iran-war-deadline-hormuz-rcna267059)

生成摘要时出错

---

## 26. Wi-Fi That Can Withstand a Nuclear Reactor: This receiver chip can take it

**原文标题**: Wi-Fi That Can Withstand a Nuclear Reactor: This receiver chip can take it

**原文链接**: [https://spectrum.ieee.org/robotics-in-nuclear-industry](https://spectrum.ieee.org/robotics-in-nuclear-industry)

生成摘要时出错

---

## 27. Haunting Photos Show the Aftermath of the Kursk Submarine Disaster in 2000

**原文标题**: Haunting Photos Show the Aftermath of the Kursk Submarine Disaster in 2000

**原文链接**: [https://rarehistoricalphotos.com/kursk-submarine-disaster-photos/](https://rarehistoricalphotos.com/kursk-submarine-disaster-photos/)

生成摘要时出错

---

## 28. Kindle to end store downloads and registering for 1st-5th gen kindles in May

**原文标题**: Kindle to end store downloads and registering for 1st-5th gen kindles in May

**原文链接**: [https://www.reddit.com/r/kindle/s/xg8uCdAWU3](https://www.reddit.com/r/kindle/s/xg8uCdAWU3)

生成摘要时出错

---

## 29. Blackholing My Email

**原文标题**: Blackholing My Email

**原文链接**: [https://www.johnsto.co.uk/blog/blackholing-my-email/](https://www.johnsto.co.uk/blog/blackholing-my-email/)

生成摘要时出错

---

## 30. DeiMOS – A Superoptimizer for the MOS 6502

**原文标题**: DeiMOS – A Superoptimizer for the MOS 6502

**原文链接**: [https://aransentin.github.io/deimos/](https://aransentin.github.io/deimos/)

生成摘要时出错

---

## 31. Sam Altman may control our future – can he be trusted?

**原文标题**: Sam Altman may control our future – can he be trusted?

**原文链接**: [https://www.newyorker.com/magazine/2026/04/13/sam-altman-may-control-our-future-can-he-be-trusted](https://www.newyorker.com/magazine/2026/04/13/sam-altman-may-control-our-future-can-he-be-trusted)

生成摘要时出错

---

## 32. Breaking the console: a brief history of video game security

**原文标题**: Breaking the console: a brief history of video game security

**原文链接**: [https://sergioprado.blog/breaking-the-console-a-brief-history-of-video-game-security/](https://sergioprado.blog/breaking-the-console-a-brief-history-of-video-game-security/)

生成摘要时出错

---

## 33. Show HN: Pion/handoff – Move WebRTC out of browser and into Go

**原文标题**: Show HN: Pion/handoff – Move WebRTC out of browser and into Go

**原文链接**: [https://github.com/pion/handoff](https://github.com/pion/handoff)

生成摘要时出错

---

## 34. AI may be making us think and write more alike

**原文标题**: AI may be making us think and write more alike

**原文链接**: [https://dornsife.usc.edu/news/stories/ai-may-be-making-us-think-and-write-more-alike/](https://dornsife.usc.edu/news/stories/ai-may-be-making-us-think-and-write-more-alike/)

生成摘要时出错

---

## 35. Show HN: Stop paying for Dropbox/Google Drive, use your own S3 bucket instead

**原文标题**: Show HN: Stop paying for Dropbox/Google Drive, use your own S3 bucket instead

**原文链接**: [https://locker.dev](https://locker.dev)

生成摘要时出错

---

## 36. Show HN: A (marginally) useful x86-64 ELF executable in 298 bytes

**原文标题**: Show HN: A (marginally) useful x86-64 ELF executable in 298 bytes

**原文链接**: [https://github.com/meribold/btry](https://github.com/meribold/btry)

生成摘要时出错

---

## 37. Three hundred synths, 3 hardware projects, and one app

**原文标题**: Three hundred synths, 3 hardware projects, and one app

**原文链接**: [https://midi.guide/blog/three-hunded-synths-one-app/](https://midi.guide/blog/three-hunded-synths-one-app/)

生成摘要时出错

---

## 38. An AI robot in my home

**原文标题**: An AI robot in my home

**原文链接**: [https://allevato.me/2026/04/07/an-ai-robot-in-my-home](https://allevato.me/2026/04/07/an-ai-robot-in-my-home)

生成摘要时出错

---

## 39. Floating point from scratch: Hard Mode

**原文标题**: Floating point from scratch: Hard Mode

**原文链接**: [https://essenceia.github.io/projects/floating_dragon/](https://essenceia.github.io/projects/floating_dragon/)

生成摘要时出错

---

## 40. Second Revision of 6502 Laptop

**原文标题**: Second Revision of 6502 Laptop

**原文链接**: [https://codeberg.org/TechPaula/LT6502b](https://codeberg.org/TechPaula/LT6502b)

生成摘要时出错

---

## 41. Claude Code is locking people out for hours

**原文标题**: Claude Code is locking people out for hours

**原文链接**: [https://github.com/anthropics/claude-code/issues/44257](https://github.com/anthropics/claude-code/issues/44257)

生成摘要时出错

---

## 42. Launch HN: Freestyle – Sandboxes for Coding Agents

**原文标题**: Launch HN: Freestyle – Sandboxes for Coding Agents

**原文链接**: [https://www.freestyle.sh/](https://www.freestyle.sh/)

生成摘要时出错

---

## 43. Solod – A subset of Go that translates to C

**原文标题**: Solod – A subset of Go that translates to C

**原文链接**: [https://github.com/solod-dev/solod](https://github.com/solod-dev/solod)

生成摘要时出错

---

## 44. Running Out of Disk Space in Production

**原文标题**: Running Out of Disk Space in Production

**原文链接**: [https://alt-romes.github.io/posts/2026-04-01-running-out-of-disk-space-on-launch.html](https://alt-romes.github.io/posts/2026-04-01-running-out-of-disk-space-on-launch.html)

生成摘要时出错

---

## 45. Peptides: where to begin?

**原文标题**: Peptides: where to begin?

**原文链接**: [https://www.science.org/content/blog-post/ah-peptides-where-begin](https://www.science.org/content/blog-post/ah-peptides-where-begin)

生成摘要时出错

---

## 46. A Fire Sale Has U.S. Office Buildings Going for 90% Off

**原文标题**: A Fire Sale Has U.S. Office Buildings Going for 90% Off

**原文链接**: [https://www.wsj.com/real-estate/commercial/a-fire-sale-has-u-s-office-buildings-going-for-90-off-8fa8b5d8](https://www.wsj.com/real-estate/commercial/a-fire-sale-has-u-s-office-buildings-going-for-90-off-8fa8b5d8)

生成摘要时出错

---

## 47. Show HN: GovAuctions lets you browse government auctions at once

**原文标题**: Show HN: GovAuctions lets you browse government auctions at once

**原文链接**: [https://www.govauctions.app/](https://www.govauctions.app/)

生成摘要时出错

---

## 48. Apollo Guidance Computer restoration videos

**原文标题**: Apollo Guidance Computer restoration videos

**原文链接**: [https://www.curiousmarc.com/space/apollo-guidance-computer](https://www.curiousmarc.com/space/apollo-guidance-computer)

生成摘要时出错

---

## 49. This Spillway Failed on Purpose [video]

**原文标题**: This Spillway Failed on Purpose [video]

**原文链接**: [https://www.youtube.com/watch?v=UF63eFJmbrQ](https://www.youtube.com/watch?v=UF63eFJmbrQ)

生成摘要时出错

---

## 50. Record wind and solar saved UK from gas imports worth £1B in March 2026

**原文标题**: Record wind and solar saved UK from gas imports worth £1B in March 2026

**原文链接**: [https://www.carbonbrief.org/analysis-record-wind-and-solar-saved-uk-from-gas-imports-worth-1bn-in-march-2026/](https://www.carbonbrief.org/analysis-record-wind-and-solar-saved-uk-from-gas-imports-worth-1bn-in-march-2026/)

生成摘要时出错

---

## 51. Claude is having another moment, again

**原文标题**: Claude is having another moment, again

**原文链接**: [https://downdetector.co.uk/status/claude-ai/](https://downdetector.co.uk/status/claude-ai/)

生成摘要时出错

---

## 52. Show HN: AdaShape-3D modeler for intuitive 3D printing parts / Windows 11

**原文标题**: Show HN: AdaShape-3D modeler for intuitive 3D printing parts / Windows 11

**原文链接**: [https://adashape.com](https://adashape.com)

生成摘要时出错

---

## 53. Show HN: Ghost Pepper – Local hold-to-talk speech-to-text for macOS

**原文标题**: Show HN: Ghost Pepper – Local hold-to-talk speech-to-text for macOS

**原文链接**: [https://github.com/matthartman/ghost-pepper](https://github.com/matthartman/ghost-pepper)

生成摘要时出错

---

## 54. Show HN: Anos – a hand-written ~100KiB microkernel for x86-64 and RISC-V

**原文标题**: Show HN: Anos – a hand-written ~100KiB microkernel for x86-64 and RISC-V

**原文链接**: [https://github.com/roscopeco/anos](https://github.com/roscopeco/anos)

生成摘要时出错

---

## 55. Sky – an Elm-inspired language that compiles to Go

**原文标题**: Sky – an Elm-inspired language that compiles to Go

**原文链接**: [https://github.com/anzellai/sky](https://github.com/anzellai/sky)

生成摘要时出错

---

## 56. NanoClaw's architecture is a masterclass in doing less

**原文标题**: NanoClaw's architecture is a masterclass in doing less

**原文链接**: [https://jonno.nz/posts/nanoclaw-architecture-masterclass-in-doing-less/](https://jonno.nz/posts/nanoclaw-architecture-masterclass-in-doing-less/)

生成摘要时出错

---

## 57. "The new Copilot app for Windows 11 is really just Microsoft Edge"

**原文标题**: "The new Copilot app for Windows 11 is really just Microsoft Edge"

**原文链接**: [https://twitter.com/TheBobPony/status/2041112541909205001](https://twitter.com/TheBobPony/status/2041112541909205001)

生成摘要时出错

---

## 58. Issue: Claude Code is unusable for complex engineering tasks with Feb updates

**原文标题**: Issue: Claude Code is unusable for complex engineering tasks with Feb updates

**原文链接**: [https://github.com/anthropics/claude-code/issues/42796](https://github.com/anthropics/claude-code/issues/42796)

生成摘要时出错

---

## 59. Anthropic expands partnership with Google and Broadcom for next-gen compute

**原文标题**: Anthropic expands partnership with Google and Broadcom for next-gen compute

**原文链接**: [https://www.anthropic.com/news/google-broadcom-partnership-compute](https://www.anthropic.com/news/google-broadcom-partnership-compute)

生成摘要时出错

---

## 60. Kiwi Farms challenges DMCA subpoenas as tools to unmask anonymous speech

**原文标题**: Kiwi Farms challenges DMCA subpoenas as tools to unmask anonymous speech

**原文链接**: [https://reclaimthenet.org/kiwi-farms-dmca-subpoena-anonymous-speech-case](https://reclaimthenet.org/kiwi-farms-dmca-subpoena-anonymous-speech-case)

生成摘要时出错

---

## 61. Show HN: Hippo, biologically inspired memory for AI agents

**原文标题**: Show HN: Hippo, biologically inspired memory for AI agents

**原文链接**: [https://github.com/kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)

生成摘要时出错

---

## 62. A cryptography engineer's perspective on quantum computing timelines

**原文标题**: A cryptography engineer's perspective on quantum computing timelines

**原文链接**: [https://words.filippo.io/crqc-timeline/](https://words.filippo.io/crqc-timeline/)

生成摘要时出错

---

## 63. The team behind a pro-Iran, Lego-themed viral-video campaign

**原文标题**: The team behind a pro-Iran, Lego-themed viral-video campaign

**原文链接**: [https://www.newyorker.com/culture/infinite-scroll/the-team-behind-a-pro-iran-lego-themed-viral-video-campaign](https://www.newyorker.com/culture/infinite-scroll/the-team-behind-a-pro-iran-lego-themed-viral-video-campaign)

生成摘要时出错

---

## 64. VOID: Video Object and Interaction Deletion

**原文标题**: VOID: Video Object and Interaction Deletion

**原文链接**: [https://github.com/Netflix/void-model](https://github.com/Netflix/void-model)

生成摘要时出错

---

## 65. Show HN: Tusk for macOS and Gnome

**原文标题**: Show HN: Tusk for macOS and Gnome

**原文链接**: [https://shapemachine.xyz/tusk/](https://shapemachine.xyz/tusk/)

生成摘要时出错

---

## 66. Emotion in AI Is Not Noise – It's Signal

**原文标题**: Emotion in AI Is Not Noise – It's Signal

**原文链接**: [https://twitter.com/fabianfranz/status/2041541955662774434](https://twitter.com/fabianfranz/status/2041541955662774434)

生成摘要时出错

---

## 67. Battle for Wesnoth: open-source, turn-based strategy game

**原文标题**: Battle for Wesnoth: open-source, turn-based strategy game

**原文链接**: [https://www.wesnoth.org](https://www.wesnoth.org)

生成摘要时出错

---

## 68. Build web apps for smart glasses

**原文标题**: Build web apps for smart glasses

**原文链接**: [https://hub.evenrealities.com/docs/getting-started/overview](https://hub.evenrealities.com/docs/getting-started/overview)

生成摘要时出错

---

## 69. Dear Heroku: Uhh What's Going On?

**原文标题**: Dear Heroku: Uhh What's Going On?

**原文链接**: [https://judoscale.com/blog/heroku-whats-going-on](https://judoscale.com/blog/heroku-whats-going-on)

生成摘要时出错

---

## 70. The cult of vibe coding is dogfooding run amok

**原文标题**: The cult of vibe coding is dogfooding run amok

**原文链接**: [https://bramcohen.com/p/the-cult-of-vibe-coding-is-insane](https://bramcohen.com/p/the-cult-of-vibe-coding-is-insane)

生成摘要时出错

---

## 71. German police name alleged leaders of GandCrab and REvil ransomware groups

**原文标题**: German police name alleged leaders of GandCrab and REvil ransomware groups

**原文链接**: [https://krebsonsecurity.com/2026/04/germany-doxes-unkn-head-of-ru-ransomware-gangs-revil-gandcrab/](https://krebsonsecurity.com/2026/04/germany-doxes-unkn-head-of-ru-ransomware-gangs-revil-gandcrab/)

生成摘要时出错

---

## 72. Show HN: TTF-DOOM – A raycaster running inside TrueType font hinting

**原文标题**: Show HN: TTF-DOOM – A raycaster running inside TrueType font hinting

**原文链接**: [https://github.com/4RH1T3CT0R7/ttf-doom](https://github.com/4RH1T3CT0R7/ttf-doom)

生成摘要时出错

---

## 73. Agent Reading Test

**原文标题**: Agent Reading Test

**原文链接**: [https://agentreadingtest.com](https://agentreadingtest.com)

生成摘要时出错

---

## 74. Wikipedia's AI agent row likely just the beginning of the bot-ocalypse

**原文标题**: Wikipedia's AI agent row likely just the beginning of the bot-ocalypse

**原文链接**: [https://www.malwarebytes.com/blog/ai/2026/04/wikipedias-ai-agent-row-likely-just-the-beginning-of-the-bot-ocalypse](https://www.malwarebytes.com/blog/ai/2026/04/wikipedias-ai-agent-row-likely-just-the-beginning-of-the-bot-ocalypse)

生成摘要时出错

---

## 75. AI singer now occupies eleven spots on iTunes singles chart

**原文标题**: AI singer now occupies eleven spots on iTunes singles chart

**原文链接**: [https://www.showbiz411.com/2026/04/05/itunes-takeover-by-fake-ai-singer-eddie-dalton-now-occupies-eleven-spots-on-chart-despite-not-being-human-or-real-exclusive](https://www.showbiz411.com/2026/04/05/itunes-takeover-by-fake-ai-singer-eddie-dalton-now-occupies-eleven-spots-on-chart-despite-not-being-human-or-real-exclusive)

生成摘要时出错

---

## 76. Intelligent people are better judges of the intelligence of others

**原文标题**: Intelligent people are better judges of the intelligence of others

**原文链接**: [https://www.psypost.org/intelligent-people-are-better-judges-of-the-intelligence-of-others/](https://www.psypost.org/intelligent-people-are-better-judges-of-the-intelligence-of-others/)

生成摘要时出错

---

## 77. The Hacker News Tarpit

**原文标题**: The Hacker News Tarpit

**原文链接**: [https://www.joanwestenberg.com/the-hacker-news-tarpit/](https://www.joanwestenberg.com/the-hacker-news-tarpit/)

生成摘要时出错

---

## 78. Wireless Festival cancelled after government stops Kanye West entering UK

**原文标题**: Wireless Festival cancelled after government stops Kanye West entering UK

**原文链接**: [https://www.bbc.co.uk/news/live/c77e60v0my1t](https://www.bbc.co.uk/news/live/c77e60v0my1t)

生成摘要时出错

---

## 79. Linux extreme performance H1 load generator

**原文标题**: Linux extreme performance H1 load generator

**原文链接**: [https://www.gcannon.org/](https://www.gcannon.org/)

生成摘要时出错

---

## 80. What being ripped off taught me

**原文标题**: What being ripped off taught me

**原文链接**: [https://belief.horse/notes/what-being-ripped-off-taught-me/](https://belief.horse/notes/what-being-ripped-off-taught-me/)

生成摘要时出错

---

## 81. After 20 years I turned off Google Adsense for my websites (2025)

**原文标题**: After 20 years I turned off Google Adsense for my websites (2025)

**原文链接**: [https://blog.ericgoldman.org/archives/2025/06/after-20-years-i-turned-off-google-adsense-for-my-websites.htm](https://blog.ericgoldman.org/archives/2025/06/after-20-years-i-turned-off-google-adsense-for-my-websites.htm)

生成摘要时出错

---

## 82. Show HN: I built a tiny LLM to demystify how language models work

**原文标题**: Show HN: I built a tiny LLM to demystify how language models work

**原文链接**: [https://github.com/arman-bd/guppylm](https://github.com/arman-bd/guppylm)

生成摘要时出错

---

## 83. Microsoft hasn't had a coherent GUI strategy since Petzold

**原文标题**: Microsoft hasn't had a coherent GUI strategy since Petzold

**原文链接**: [https://www.jsnover.com/blog/2026/03/13/microsoft-hasnt-had-a-coherent-gui-strategy-since-petzold/](https://www.jsnover.com/blog/2026/03/13/microsoft-hasnt-had-a-coherent-gui-strategy-since-petzold/)

生成摘要时出错

---

## 84. SOM: A minimal Smalltalk for teaching of and research on Virtual Machines

**原文标题**: SOM: A minimal Smalltalk for teaching of and research on Virtual Machines

**原文链接**: [http://som-st.github.io/](http://som-st.github.io/)

生成摘要时出错

---

## 85. France pulls last gold held in US

**原文标题**: France pulls last gold held in US

**原文链接**: [https://www.mining.com/france-pulls-last-gold-held-in-us-for-15b-gain/](https://www.mining.com/france-pulls-last-gold-held-in-us-for-15b-gain/)

生成摘要时出错

---

## 86. Book review: There Is No Antimemetics Division

**原文标题**: Book review: There Is No Antimemetics Division

**原文链接**: [https://www.stephendiehl.com/posts/no_antimimetics/](https://www.stephendiehl.com/posts/no_antimimetics/)

生成摘要时出错

---

## 87. Why a new computer is slower than an old computer [video]

**原文标题**: Why a new computer is slower than an old computer [video]

**原文链接**: [https://www.youtube.com/watch?v=t992ul_IKtc](https://www.youtube.com/watch?v=t992ul_IKtc)

生成摘要时出错

---

## 88. Lunar Flyby

**原文标题**: Lunar Flyby

**原文链接**: [https://www.nasa.gov/gallery/lunar-flyby/](https://www.nasa.gov/gallery/lunar-flyby/)

生成摘要时出错

---

## 89. Sheets: Terminal based spreadsheet tool

**原文标题**: Sheets: Terminal based spreadsheet tool

**原文链接**: [https://github.com/maaslalani/sheets](https://github.com/maaslalani/sheets)

生成摘要时出错

---

## 90. The Last Quiet Thing

**原文标题**: The Last Quiet Thing

**原文链接**: [https://www.terrygodier.com/the-last-quiet-thing](https://www.terrygodier.com/the-last-quiet-thing)

生成摘要时出错

---

## 91. Eighteen Years of Greytrapping – Is the Weirdness Finally Paying Off?

**原文标题**: Eighteen Years of Greytrapping – Is the Weirdness Finally Paying Off?

**原文链接**: [https://nxdomain.no/~peter/eighteen_years_of_greytrapping.html](https://nxdomain.no/~peter/eighteen_years_of_greytrapping.html)

生成摘要时出错

---

## 92. Signals, the push-pull based algorithm

**原文标题**: Signals, the push-pull based algorithm

**原文链接**: [https://willybrauner.com/journal/signal-the-push-pull-based-algorithm](https://willybrauner.com/journal/signal-the-push-pull-based-algorithm)

生成摘要时出错

---

## 93. Show HN: Real-time AI (audio/video in, voice out) on an M3 Pro with Gemma E2B

**原文标题**: Show HN: Real-time AI (audio/video in, voice out) on an M3 Pro with Gemma E2B

**原文链接**: [https://github.com/fikrikarim/parlor](https://github.com/fikrikarim/parlor)

生成摘要时出错

---

## 94. Adobe modifies hosts file to detect whether Creative Cloud is installed

**原文标题**: Adobe modifies hosts file to detect whether Creative Cloud is installed

**原文链接**: [https://www.osnews.com/story/144737/adobe-secretly-modifies-your-hosts-file-for-the-stupidest-reason/](https://www.osnews.com/story/144737/adobe-secretly-modifies-your-hosts-file-for-the-stupidest-reason/)

生成摘要时出错

---

## 95. Some iPhone Apps Receive Mysterious Update 'From Apple'

**原文标题**: Some iPhone Apps Receive Mysterious Update 'From Apple'

**原文链接**: [https://www.macrumors.com/2026/04/06/iphone-apps-from-apple-update/](https://www.macrumors.com/2026/04/06/iphone-apps-from-apple-update/)

生成摘要时出错

---

## 96. Gemma 4 on iPhone

**原文标题**: Gemma 4 on iPhone

**原文链接**: [https://apps.apple.com/nl/app/google-ai-edge-gallery/id6749645337](https://apps.apple.com/nl/app/google-ai-edge-gallery/id6749645337)

生成摘要时出错

---

## 97. The 1987 game “The Last Ninja” was 40 kilobytes

**原文标题**: The 1987 game “The Last Ninja” was 40 kilobytes

**原文链接**: [https://twitter.com/exQUIZitely/status/2040777977521398151](https://twitter.com/exQUIZitely/status/2040777977521398151)

生成摘要时出错

---

## 98. Drop, formerly Massdrop, ends most collaborations and rebrands under Corsair

**原文标题**: Drop, formerly Massdrop, ends most collaborations and rebrands under Corsair

**原文链接**: [https://drop.com/](https://drop.com/)

生成摘要时出错

---

## 99. When Small Parquet Files Become a Big Problem (and How I Wrote a Compactor)

**原文标题**: When Small Parquet Files Become a Big Problem (and How I Wrote a Compactor)

**原文链接**: [https://www.datobra.com/when-small-parquet-files-become-a-big-problem-and-how-i-ended-up-writing-a-compactor-in-pyarrow/](https://www.datobra.com/when-small-parquet-files-become-a-big-problem-and-how-i-ended-up-writing-a-compactor-in-pyarrow/)

生成摘要时出错

---

## 100. Show HN: Gemma Gem – AI model embedded in a browser – no API keys, no cloud

**原文标题**: Show HN: Gemma Gem – AI model embedded in a browser – no API keys, no cloud

**原文链接**: [https://github.com/kessler/gemma-gem](https://github.com/kessler/gemma-gem)

生成摘要时出错

---

