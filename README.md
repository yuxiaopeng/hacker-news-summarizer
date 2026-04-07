# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-07.md)

*最后自动更新时间: 2026-04-07 18:29:58*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 2 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 3 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 4 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 5 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 6 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 7 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 8 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 9 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 10 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 11 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 12 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 13 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 14 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 15 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 16 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 17 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 18 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 19 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 20 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 21 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 22 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 23 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 24 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 25 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 26 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 27 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 28 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 29 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 30 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 31 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 32 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 33 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 34 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 35 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 36 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 37 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 38 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 39 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 40 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 41 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 42 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 43 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 44 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 45 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 46 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 47 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 48 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 49 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 50 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 51 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 52 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 53 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 54 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 55 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 56 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 57 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 58 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 59 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 60 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 61 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 62 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 63 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 64 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 65 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 66 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 67 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 68 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 69 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 70 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 71 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 72 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 73 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 74 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 75 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 76 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 77 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 78 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 79 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 80 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 81 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 82 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 83 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 84 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 85 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 86 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 87 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 88 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 89 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 90 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 91 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 92 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 93 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 94 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 95 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 96 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 97 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 98 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 99 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 100 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 101 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 102 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 103 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 104 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 105 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 106 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 107 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 108 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 109 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 110 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 111 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 112 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 113 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 114 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 115 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 116 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 117 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 118 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 119 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 120 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 121 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 122 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 123 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 124 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 125 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 126 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 127 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 128 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 129 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 130 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 131 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 132 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 133 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 134 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 135 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 136 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 137 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 138 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 139 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 140 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 141 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 142 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 143 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 144 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 145 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 146 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 147 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 148 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 149 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 150 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 151 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 152 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 153 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 154 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 155 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 156 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 157 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 158 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 159 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 160 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 161 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 162 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 163 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 164 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 165 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 166 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 167 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 168 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 169 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 170 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 171 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 172 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 173 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 174 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 175 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 176 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 177 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 178 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 179 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 180 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 181 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 182 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 183 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 184 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 185 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 186 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 187 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 188 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 189 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 190 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 191 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 192 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 193 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 194 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 195 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 196 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 197 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 198 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 199 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 200 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 201 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 202 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 203 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 204 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 205 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 206 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 207 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 208 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 209 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 210 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 211 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 212 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 213 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 214 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 215 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 216 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 217 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 218 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 219 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 220 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 221 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 222 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 223 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 224 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 225 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 226 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 227 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 228 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 229 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 230 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 231 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 232 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 233 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 234 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 235 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 236 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 237 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 238 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 239 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 240 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 241 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 242 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 243 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 244 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 245 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 246 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 247 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 248 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 249 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 250 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 251 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 252 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 253 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 254 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 255 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 256 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 257 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 258 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 259 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 260 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 261 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 262 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 263 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 264 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 265 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 266 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 267 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 268 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 269 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 270 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 271 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 272 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 273 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 274 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 275 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 276 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 277 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 278 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 279 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 280 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 281 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 282 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 283 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 284 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 285 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 286 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 287 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 288 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 289 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 290 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 291 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 292 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 293 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 294 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 295 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 296 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 297 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 298 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 299 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 300 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 301 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 302 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 303 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 304 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 305 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 306 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 307 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 308 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 309 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 310 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 311 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 312 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 313 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 314 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 315 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 316 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 317 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 318 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 319 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 320 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 321 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 322 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 323 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 324 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 325 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 326 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 327 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 328 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 329 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 330 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 331 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 332 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 333 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 334 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 335 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 336 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 337 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 338 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 339 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 340 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 341 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 342 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 343 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 344 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 345 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 346 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 347 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 348 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 349 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 350 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 351 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 352 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 353 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 354 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 355 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 356 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 357 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 358 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 359 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 360 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 361 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 362 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 363 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 364 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 365 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 366 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 367 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 368 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 369 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 370 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 371 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 372 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 373 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 374 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 375 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 376 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 377 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 378 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 379 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 380 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 381 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 382 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 383 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
