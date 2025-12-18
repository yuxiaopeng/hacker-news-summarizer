# Hacker News 热门文章摘要 (2025-12-18)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 从2026年1月起，所有ACM出版物都将实现开放获取。

**原文标题**: Beginning January 2026, all ACM publications will be made open access

**原文链接**: [https://dl.acm.org/openaccess](https://dl.acm.org/openaccess)

美国计算机协会 (ACM) 宣布，将于 2026 年 1 月正式全面转型为完全开放获取 (OA) 的出版模式。此举标志着自 2020 年启动的五年战略计划进入收官阶段，旨在推动 ACM 数字图书馆彻底脱离基于订阅的“付费阅读”系统。

**此次转型的关键点包括：**

*   **ACM Open 模式：** 变革的核心机制是“ACM Open”，这是一种转换模式。参与机构通过支付一笔年度固定费用，即可为其所属作者提供无限量的 OA 出版支持，并获得对整个 ACM 数字图书馆的永久访问权。
*   **时间表：** 转型目前已在进行中。从 2026 年 1 月起，所有发表在 ACM 期刊、会议论文集和杂志上的新研究文章都将默认以 OA 形式发布。
*   **全球影响：** 通过取消付费墙，ACM 旨在提升计算机科学研究的知名度、覆盖面和影响力，与更广泛的“开放科学”运动保持一致。这确保了全球的研究人员、从业者和学生都能无障碍地获取 70 多年的学术内容。
*   **公平性与包容性：** 为确保模式的可持续性和包容性，ACM 将为来自中低收入国家或所属机构尚未加入 ACM Open 计划的作者提供费用减免和补贴。其目标是确保没有任何作者会因缺乏资金而无法发表论文。

到 2026 年，ACM 数字图书馆预计将成为一个完全开放的资源库，由机构合作伙伴关系而非个人或图书馆订阅提供支持。这一转变代表了科学界在将高质量技术研究转化为公共利益方面迈出的重要里程碑。

---

## 2. 古典雕像的彩绘并不难看。

**原文标题**: Classical statues were not painted horribly

**原文链接**: [https://worksinprogress.co/issue/were-classical-statues-painted-horribly/](https://worksinprogress.co/issue/were-classical-statues-painted-horribly/)

在《古典雕像的彩绘并不丑陋》一文中，作者指出，当代对古希腊和古罗马雕像进行的彩绘复原呈现出一种俗丽且“丑陋”的外观，这其实是当代制作水平低劣所致，而非古代审美取向的反映。

尽管史学界已公认古典大理石雕像最初是经过彩绘的，但一些备受瞩目的复原作品（如文森兹·布林克曼的作品）往往呈现出平淡、无光泽且饱和度过高的色彩，令现代观众在审美上感到不悦。对此，普遍的解释是“审美变迁论”，该理论认为，数百年来看惯了白色大理石雕像的现代人已成为“色彩恐惧症”患者，无法欣赏古代那种“异质”的审美。

作者通过以下证据挑战了这一理论：
1. **古代视觉艺术**：古罗马的壁画和马赛克对雕塑及人物的描绘展现了精妙、自然且细腻的色彩运用，在现代人眼中依然非常美观。
2. **跨文化比较**：其他时代和文化（如古埃及、中世纪尼泊尔和西班牙巴洛克时期）的彩绘雕塑通常被认为令人震撼或带有神秘感，但很少会像现代的古典复原品那样显得“丑陋”。

作者总结道，这些复原作品纯粹是“拙劣的画作”。它们的失败是因为现代专家缺乏古代大师的艺术造诣，且刻板地遵循只复原考古证实部分的保护原则。这导致复原品成了只有“底色”的版本，忽略了原本能提供深度和真实感的细腻叠色、罩染和艺术细节。最后，作者暗示，这些复原作品之所以维持这种博人眼球的丑陋感，可能是因为这比细腻、高水准的艺术再创作更能引发公众的兴趣。

---

## 3. 你的职责是交付经你验证可运行的代码。

**原文标题**: Your job is to deliver code you have proven to work

**原文链接**: [https://simonwillison.net/2025/Dec/18/code-proven-to-work/](https://simonwillison.net/2025/Dec/18/code-proven-to-work/)

在《交付经过验证的代码是你的职责》一文中，作者指出，AI 辅助开发的兴起导致部分工程师出现了“失职”现象——他们提交大量未经测试的拉取请求（PR），将验证负担转嫁给了审查者。文章的核心观点是：开发者的首要责任不仅是生成代码，而是提供代码确实有效的确凿证明。

作者概述了证明代码质量的两个核心步骤：

1.  **手动测试：** 开发者必须亲眼见证代码在预期状态下运行。这种证明应通过终端输出、日志或 UI 更改的录屏记录在 PR 中，且过程必须涵盖“正常路径”和复杂的边缘情况。
2.  **自动化测试：** 既然大语言模型（LLM）已让编写测试变得轻而易举，那么就没有任何理由跳过这一步。每一次代码提交都应包含自动化测试，用以验证更改，并确保在代码被回滚时测试会报错。

展望 2025 年的“编程智能体”（如 Claude Code），作者强调开发者必须教会这些工具证明自己的工作。这包括提示智能体执行其编写的代码、截取 CSS 更改的截图，以及扩展现有的测试模式。

归根结底，虽然 AI 可以“批量炮制”代码，但它无法承担责任。人类开发者的价值现在体现在通过证据确立问责机制，确保每一项提交在交付给同事或维护者之前都经过了充分验证。

---

## 4. 利用开源技术实现 NVIDIA HGX B200 GPU 虚拟化

**原文标题**: Virtualizing Nvidia HGX B200 GPUs with Open Source

**原文链接**: [https://www.ubicloud.com/blog/virtualizing-nvidia-hgx-b200-gpus-with-open-source](https://www.ubicloud.com/blog/virtualizing-nvidia-hgx-b200-gpus-with-open-source)

Ubicloud 最近记录了其利用开源技术栈成功实现 NVIDIA HGX B200 GPU 虚拟化的过程。与前几代产品不同，B200 采用 SXM 架构，依赖高度集成的 NVLink/NVSwitch 互联结构，相比离散的 PCIe 插卡，其在虚拟化方面面临独特挑战。

为了平衡灵活性与性能，Ubicloud 采用了“共享 NVSwitch 多租户”（Shared NVSwitch Multitenancy）模式。该方法允许进行 GPU 分区（分配 1、2、4 或 8 个 GPU），同时在每个分区内保持全额 NVLink 带宽，既避免了完全直通的局限性，也规避了 vGPU 切片带来的性能开销。

**关键技术发现：**

*   **驱动程序同步：** B200 需要 NVIDIA “开源”驱动系列。至关重要的是，宿主机上的 NVIDIA Fabric Manager 版本必须与客户机（Guest VM）内部的驱动程序版本完全匹配，以防止 CUDA 初始化失败。
*   **PCI 拓扑

通过编排这些组件并直接与 Fabric Manager API 交互，Ubicloud 成功为现代 AI 工作负载提供了高性能、私有且开源的 GPU 虚拟化方案。

---

## 5. 苹果礼品卡兑换安全吗？

**原文标题**: Are Apple gift cards safe to redeem?

**原文链接**: [https://daringfireball.net/linked/2025/12/17/are-apple-gift-cards-safe-to-redeem](https://daringfireball.net/linked/2025/12/17/are-apple-gift-cards-safe-to-redeem)

John Gruber 的这篇文章讨论了兑换 Apple 礼品卡的风险，重点介绍了 Paris Buttfield-Addison 的典型案例。在尝试兑换从大型零售商购买的 500 美元礼品卡后，Buttfield-Addison 的整个 Apple 账户（包括 iCloud 数据和多年的媒体购买记录）在没有任何解释的情况下被停用。

Gruber 强调了苹果反欺诈系统“卡夫卡式”的荒诞本质，称其运作如同一个不透明的“黑盒”。即便在案件升级至苹果“高管关系”团队后，也耗时近一周才恢复账户。这种延迟和缺乏透明度的现状，促使 Adam Engst 等技术评论员将兑换礼品卡比作“数字俄罗斯轮盘赌”，并建议消费者完全避免使用，以防账户面临“瓦解”。

核心观点包括：
*   **账户风险：** 单张受损或被篡改的礼品卡就可能导致用户数字生活和购买记录的永久丢失。
*   **系统性不透明：** 苹果不提供停用理由，且最初不提供明确的恢复路径。
*   **自动化担忧：** Gruber 质疑这些关乎重大的决定是否是由存在缺陷的算法而非人工做出的。
*   **安全建议：** 在苹果澄清相关流程之前，Gruber 建议仅在 Apple Store 实体店兑换礼品卡，且仅用于不与主账户关联的消费。

虽然在巨大的公众压力下，Buttfield-Addison 的账户最终得以恢复，但文章总结认为，Apple 礼品卡的安全性依然存疑，用户在这一宁可过度防范欺诈也不惜牺牲消费者安全的系统面前依然脆弱。

---

## 6. 乔纳森·布洛在过去的十年里为你设计了1400个谜题。

**原文标题**: Jonathan Blow has spent the past decade designing 1,400 puzzles for you

**原文链接**: [https://arstechnica.com/gaming/2025/12/jonathan-blow-has-spent-the-past-decade-designing-1400-puzzles-for-you/](https://arstechnica.com/gaming/2025/12/jonathan-blow-has-spent-the-past-decade-designing-1400-puzzles-for-you/)

《见证者》（The Witness）的著名开发者乔纳森·布洛（Jonathan Blow）揭晓了他的最新项目——《沉星之令》（Order of the Sinking Star）。该游戏最初构思于2016年，原计划是一个为期两年的新引擎“概念验证”小项目，但在九年的开发过程中，它已成长为一部计划于2026年发布的宏大解谜史诗。

游戏采用2D网格化移动系统，包含约1,400个独立谜题。布洛估计，大多数玩家需要60至100小时才能达成“第一重结局”，而追求全收集的玩家可能需要花费400至500小时才能掌握其深层内容。

**核心特性与机制：**
*   **四个迥异的世界：** 玩家从中心枢纽出发向四个基准方向探索，每个方向都引入了独特的机制：方块搬运能力、基于镜面的克隆与传送、踏脚石寻路，以及由能量束驱动的外骨骼。
*   **组合复杂性：** 在初期的线性阶段之后，这四个世界的机制将开始交织。布洛将其描述为一种“组合爆炸”，游戏的真正复杂性与“魔力”也由此展开。
*   **开发理念：** 得益于《见证者》在商业上的成功，布洛将延长的开发时间用于“设计研究”。值得注意的是，巨大的游戏规模迫使布洛比以往项目更依赖玩家测试，以管理那种“无法一次性全部装进脑海”的复杂程度。

尽管开发周期漫长且成本高昂，布洛坚称该项目代表了他对探索游戏设计全部潜力的承诺，而非仅仅是为了交付一个“可上市”的产品。

---

## 7. 军用软件控制等级标准

**原文标题**: Military Standard on Software Control Levels

**原文链接**: [https://entropicthoughts.com/mil-std-882e-software-control](https://entropicthoughts.com/mil-std-882e-software-control)

本文简要概述了 **MIL-STD-882E** 标准。该标准根据软件对潜在危险系统的控制程度，将软件风险分为四个等级：

1.  **直接即时控制：** 最高风险等级。软件直接管理系统，一旦发生故障，会立即造成伤害。
2.  **延迟或间接关键控制：** 高风险。表现为软件错误与产生的危险之间存在时间延迟，或者需要人类对软件信号立即做出反应以防止灾难（例如反应堆紧急停堆）。
3.  **经核实的间接控制：** 较低风险。软件仅提供建议，在采取任何行动之前，可以通过独立方法对这些建议进行核实。
4.  **辅助用途：** 最低风险等级。软件仅承担次要功能，不参与关键系统的控制。

作者总结认为，该框架在当今的意义日益凸显。随着大语言模型 (LLMs) 和计算机视觉等技术的进步，软件正被集成到此前完全由人类管理的复杂流程中，这使得明确了解软件控制及其潜在危险变得至关重要。

---

## 8. Using TypeScript to Obtain One of the Rarest License Plates

**原文标题**: Using TypeScript to Obtain One of the Rarest License Plates

**原文链接**: [https://www.jack.bio/blog/licenseplate](https://www.jack.bio/blog/licenseplate)

生成摘要时出错

---

## 9. Dogalog: A realtime Prolog-based livecoding music environment

**原文标题**: Dogalog: A realtime Prolog-based livecoding music environment

**原文链接**: [https://github.com/danja/dogalog](https://github.com/danja/dogalog)

生成摘要时出错

---

## 10. Please Just Try Htmx

**原文标题**: Please Just Try Htmx

**原文链接**: [http://pleasejusttryhtmx.com/](http://pleasejusttryhtmx.com/)

生成摘要时出错

---

## 11. Creating apps like Signal could be 'hostile activity' claims UK watchdog

**原文标题**: Creating apps like Signal could be 'hostile activity' claims UK watchdog

**原文链接**: [https://www.techradar.com/vpn/vpn-privacy-security/creating-apps-like-signal-or-whatsapp-could-be-hostile-activity-claims-uk-watchdog](https://www.techradar.com/vpn/vpn-privacy-security/creating-apps-like-signal-or-whatsapp-could-be-hostile-activity-claims-uk-watchdog)

生成摘要时出错

---

## 12. RCE via ND6 Router Advertisements in FreeBSD

**原文标题**: RCE via ND6 Router Advertisements in FreeBSD

**原文链接**: [https://www.freebsd.org/security/advisories/FreeBSD-SA-25:12.rtsold.asc](https://www.freebsd.org/security/advisories/FreeBSD-SA-25:12.rtsold.asc)

生成摘要时出错

---

## 13. Slowness is a virtue

**原文标题**: Slowness is a virtue

**原文链接**: [https://blog.jakobschwichtenberg.com/p/slowness-is-a-virtue](https://blog.jakobschwichtenberg.com/p/slowness-is-a-virtue)

生成摘要时出错

---

## 14. Microscopic robots that sense, think, act, and compute

**原文标题**: Microscopic robots that sense, think, act, and compute

**原文链接**: [https://www.science.org/doi/10.1126/scirobotics.adu8009](https://www.science.org/doi/10.1126/scirobotics.adu8009)

生成摘要时出错

---

## 15. Hightouch (YC S19) Is Hiring

**原文标题**: Hightouch (YC S19) Is Hiring

**原文链接**: [https://hightouch.com/careers](https://hightouch.com/careers)

生成摘要时出错

---

## 16. Egyptian Hieroglyphs: Lesson 1

**原文标题**: Egyptian Hieroglyphs: Lesson 1

**原文链接**: [https://www.egyptianhieroglyphs.net/egyptian-hieroglyphs/lesson-1/](https://www.egyptianhieroglyphs.net/egyptian-hieroglyphs/lesson-1/)

生成摘要时出错

---

## 17. I got hacked: My Hetzner server started mining Monero

**原文标题**: I got hacked: My Hetzner server started mining Monero

**原文链接**: [https://blog.jakesaunders.dev/my-server-started-mining-monero-this-morning/](https://blog.jakesaunders.dev/my-server-started-mining-monero-this-morning/)

生成摘要时出错

---

## 18. What is an elliptic curve? (2019)

**原文标题**: What is an elliptic curve? (2019)

**原文链接**: [https://www.johndcook.com/blog/2019/02/21/what-is-an-elliptic-curve/](https://www.johndcook.com/blog/2019/02/21/what-is-an-elliptic-curve/)

生成摘要时出错

---

## 19. Show HN: A local-first memory store for LLM agents (SQLite)

**原文标题**: Show HN: A local-first memory store for LLM agents (SQLite)

**原文链接**: [https://github.com/CaviraOSS/OpenMemory](https://github.com/CaviraOSS/OpenMemory)

生成摘要时出错

---

## 20. After ruining a treasured water resource, Iran is drying up

**原文标题**: After ruining a treasured water resource, Iran is drying up

**原文链接**: [https://e360.yale.edu/features/iran-water-drought-dams-qanats](https://e360.yale.edu/features/iran-water-drought-dams-qanats)

生成摘要时出错

---

## 21. systemd v259 Released

**原文标题**: systemd v259 Released

**原文链接**: [https://github.com/systemd/systemd/releases/tag/v259](https://github.com/systemd/systemd/releases/tag/v259)

生成摘要时出错

---

## 22. Heart and Kidney Diseases and Type 2 Diabetes May Be One Ailment

**原文标题**: Heart and Kidney Diseases and Type 2 Diabetes May Be One Ailment

**原文链接**: [https://www.scientificamerican.com/article/heart-and-kidney-diseases-plus-type-2-diabetes-may-be-one-illness-treatable/](https://www.scientificamerican.com/article/heart-and-kidney-diseases-plus-type-2-diabetes-may-be-one-illness-treatable/)

生成摘要时出错

---

## 23. From profiling to kernel patch: the journey to an eBPF performance fix

**原文标题**: From profiling to kernel patch: the journey to an eBPF performance fix

**原文链接**: [https://rovarma.com/articles/from-profiling-to-kernel-patch-the-journey-to-an-ebpf-performance-fix/](https://rovarma.com/articles/from-profiling-to-kernel-patch-the-journey-to-an-ebpf-performance-fix/)

生成摘要时出错

---

## 24. Most parked domains now serving malicious content

**原文标题**: Most parked domains now serving malicious content

**原文链接**: [https://krebsonsecurity.com/2025/12/most-parked-domains-now-serving-malicious-content/](https://krebsonsecurity.com/2025/12/most-parked-domains-now-serving-malicious-content/)

生成摘要时出错

---

## 25. The Big City; Save the Flophouses (1996)

**原文标题**: The Big City; Save the Flophouses (1996)

**原文链接**: [https://www.nytimes.com/1996/01/14/magazine/the-big-city-save-the-flophouses.html](https://www.nytimes.com/1996/01/14/magazine/the-big-city-save-the-flophouses.html)

生成摘要时出错

---

## 26. AI helps ship faster but it produces 1.7× more bugs

**原文标题**: AI helps ship faster but it produces 1.7× more bugs

**原文链接**: [https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report](https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report)

生成摘要时出错

---

## 27. It's all about momentum

**原文标题**: It's all about momentum

**原文链接**: [https://combo.cc/posts/its-all-about-momentum-innit/](https://combo.cc/posts/its-all-about-momentum-innit/)

生成摘要时出错

---

## 28. Working quickly is more important than it seems (2015)

**原文标题**: Working quickly is more important than it seems (2015)

**原文链接**: [https://jsomers.net/blog/speed-matters](https://jsomers.net/blog/speed-matters)

生成摘要时出错

---

## 29. Online Textbook for Braid groups and knots and tangles

**原文标题**: Online Textbook for Braid groups and knots and tangles

**原文链接**: [https://matthematics.com/redoak/redoak.html](https://matthematics.com/redoak/redoak.html)

生成摘要时出错

---

## 30. Breaking Paragraphs into Lines [pdf] (1981)

**原文标题**: Breaking Paragraphs into Lines [pdf] (1981)

**原文链接**: [https://gwern.net/doc/design/typography/tex/1981-knuth.pdf](https://gwern.net/doc/design/typography/tex/1981-knuth.pdf)

生成摘要时出错

---

## 31. Building a High-Performance OpenAPI Parser in Go

**原文标题**: Building a High-Performance OpenAPI Parser in Go

**原文链接**: [https://www.speakeasy.com/blog/building-speakeasy-openapi-go-library](https://www.speakeasy.com/blog/building-speakeasy-openapi-go-library)

生成摘要时出错

---

## 32. GitHub postponing the announced billing change for self-hosted GitHub Actions

**原文标题**: GitHub postponing the announced billing change for self-hosted GitHub Actions

**原文链接**: [https://twitter.com/jaredpalmer/status/2001373329811181846](https://twitter.com/jaredpalmer/status/2001373329811181846)

生成摘要时出错

---

## 33. Gemini 3 Flash: Frontier intelligence built for speed

**原文标题**: Gemini 3 Flash: Frontier intelligence built for speed

**原文链接**: [https://blog.google/products/gemini/gemini-3-flash/](https://blog.google/products/gemini/gemini-3-flash/)

生成摘要时出错

---

## 34. Developers can now submit apps to ChatGPT

**原文标题**: Developers can now submit apps to ChatGPT

**原文链接**: [https://openai.com/index/developers-can-now-submit-apps-to-chatgpt/](https://openai.com/index/developers-can-now-submit-apps-to-chatgpt/)

生成摘要时出错

---

## 35. Spain fines Airbnb €65M: Why the government is cracking down on illegal rentals

**原文标题**: Spain fines Airbnb €65M: Why the government is cracking down on illegal rentals

**原文链接**: [https://www.euronews.com/travel/2025/12/15/spain-fines-airbnb-65-million-why-the-government-is-cracking-down-on-illegal-rentals](https://www.euronews.com/travel/2025/12/15/spain-fines-airbnb-65-million-why-the-government-is-cracking-down-on-illegal-rentals)

生成摘要时出错

---

## 36. Fluent: A Localization System for Natural-Sounding Translations

**原文标题**: Fluent: A Localization System for Natural-Sounding Translations

**原文链接**: [https://projectfluent.org/](https://projectfluent.org/)

生成摘要时出错

---

## 37. AWS CEO says replacing junior devs with AI is 'one of the dumbest ideas'

**原文标题**: AWS CEO says replacing junior devs with AI is 'one of the dumbest ideas'

**原文链接**: [https://www.finalroundai.com/blog/aws-ceo-ai-cannot-replace-junior-developers](https://www.finalroundai.com/blog/aws-ceo-ai-cannot-replace-junior-developers)

生成摘要时出错

---

## 38. The Mysterious Forces Steering Views on Hacker News

**原文标题**: The Mysterious Forces Steering Views on Hacker News

**原文链接**: [https://xn--gckvb8fzb.com/the-mysterious-forces-steering-views-on-hacker-news/](https://xn--gckvb8fzb.com/the-mysterious-forces-steering-views-on-hacker-news/)

生成摘要时出错

---

## 39. Finland Gave Two Groups Identical Payments. One Saw 33% Better Mental Health

**原文标题**: Finland Gave Two Groups Identical Payments. One Saw 33% Better Mental Health

**原文链接**: [https://scottsantens.substack.com/p/finland-basic-income-experiment-mental-health-ubi](https://scottsantens.substack.com/p/finland-basic-income-experiment-mental-health-ubi)

生成摘要时出错

---

## 40. Gut bacteria from amphibians and reptiles achieve tumor elimination in mice

**原文标题**: Gut bacteria from amphibians and reptiles achieve tumor elimination in mice

**原文链接**: [https://www.jaist.ac.jp/english/whatsnew/press/2025/12/17-1.html](https://www.jaist.ac.jp/english/whatsnew/press/2025/12/17-1.html)

生成摘要时出错

---

## 41. Don MacKinnon: Why Simplicity Beats Cleverness in Software Design [audio]

**原文标题**: Don MacKinnon: Why Simplicity Beats Cleverness in Software Design [audio]

**原文链接**: [https://maintainable.fm/episodes/don-mackinnon-why-simplicity-beats-cleverness-in-software-design](https://maintainable.fm/episodes/don-mackinnon-why-simplicity-beats-cleverness-in-software-design)

生成摘要时出错

---

## 42. A Safer Container Ecosystem with Docker: Free Docker Hardened Images

**原文标题**: A Safer Container Ecosystem with Docker: Free Docker Hardened Images

**原文链接**: [https://www.docker.com/blog/docker-hardened-images-for-every-developer/](https://www.docker.com/blog/docker-hardened-images-for-every-developer/)

生成摘要时出错

---

## 43. Judge hints Vizio TV buyers may have rights to source code licensed under GPL

**原文标题**: Judge hints Vizio TV buyers may have rights to source code licensed under GPL

**原文链接**: [https://www.theregister.com/2025/12/05/vizio_gpl_source_code_ruling/](https://www.theregister.com/2025/12/05/vizio_gpl_source_code_ruling/)

生成摘要时出错

---

## 44. Coursera to combine with Udemy

**原文标题**: Coursera to combine with Udemy

**原文链接**: [https://investor.coursera.com/news/news-details/2025/Coursera-to-Combine-with-Udemy-to-Empower-the-Global-Workforce-with-Skills-for-the-AI-Era/default.aspx](https://investor.coursera.com/news/news-details/2025/Coursera-to-Combine-with-Udemy-to-Empower-the-Global-Workforce-with-Skills-for-the-AI-Era/default.aspx)

生成摘要时出错

---

## 45. OBS Studio Gets a New Renderer

**原文标题**: OBS Studio Gets a New Renderer

**原文链接**: [https://obsproject.com/blog/obs-studio-gets-a-new-renderer](https://obsproject.com/blog/obs-studio-gets-a-new-renderer)

生成摘要时出错

---

## 46. Valve Is Running Apple's Playbook in Reverse

**原文标题**: Valve Is Running Apple's Playbook in Reverse

**原文链接**: [https://www.garbagecollected.dev/p/valve-the-reverse-apple](https://www.garbagecollected.dev/p/valve-the-reverse-apple)

生成摘要时出错

---

## 47. Show HN: I built a fast RSS reader in Zig

**原文标题**: Show HN: I built a fast RSS reader in Zig

**原文链接**: [https://github.com/superstarryeyes/hys](https://github.com/superstarryeyes/hys)

生成摘要时出错

---

## 48. Assange brings 'instrument of war' case against Nobel Foundation

**原文标题**: Assange brings 'instrument of war' case against Nobel Foundation

**原文链接**: [https://dailytelegraph.co.nz/news/assange-brings-instrument-of-war-case-against-nobel-foundation/](https://dailytelegraph.co.nz/news/assange-brings-instrument-of-war-case-against-nobel-foundation/)

生成摘要时出错

---

## 49. Explaining the widening divides in us midlife mortality: Is there a smoking gun?

**原文标题**: Explaining the widening divides in us midlife mortality: Is there a smoking gun?

**原文链接**: [https://www.nber.org/papers/w34553](https://www.nber.org/papers/w34553)

生成摘要时出错

---

## 50. Zmij: Faster floating point double-to-string conversion

**原文标题**: Zmij: Faster floating point double-to-string conversion

**原文链接**: [https://vitaut.net/posts/2025/faster-dtoa/](https://vitaut.net/posts/2025/faster-dtoa/)

生成摘要时出错

---

## 51. How SQLite is tested

**原文标题**: How SQLite is tested

**原文链接**: [https://sqlite.org/testing.html](https://sqlite.org/testing.html)

生成摘要时出错

---

## 52. Microsoft kills IntelliCode in favor of the paid Copilot

**原文标题**: Microsoft kills IntelliCode in favor of the paid Copilot

**原文链接**: [https://visualstudiomagazine.com/articles/2025/12/17/microsoft-quietly-kills-intellicode-as-ai-strategy-shifts-to-copilot.aspx](https://visualstudiomagazine.com/articles/2025/12/17/microsoft-quietly-kills-intellicode-as-ai-strategy-shifts-to-copilot.aspx)

生成摘要时出错

---

## 53. Show HN: High-Performance Wavelet Matrix for Python, Implemented in Rust

**原文标题**: Show HN: High-Performance Wavelet Matrix for Python, Implemented in Rust

**原文链接**: [https://pypi.org/project/wavelet-matrix/](https://pypi.org/project/wavelet-matrix/)

生成摘要时出错

---

## 54. EU Launches Multi-Billion "Scaleup Europe Fund"

**原文标题**: EU Launches Multi-Billion "Scaleup Europe Fund"

**原文链接**: [https://eic.ec.europa.eu/eic-fund/scaleup-europe-fund_en](https://eic.ec.europa.eu/eic-fund/scaleup-europe-fund_en)

生成摘要时出错

---

## 55. 'Ghost jobs' are on the rise – and so are calls to ban them

**原文标题**: 'Ghost jobs' are on the rise – and so are calls to ban them

**原文链接**: [https://www.bbc.com/news/articles/clyzvpp8g3vo](https://www.bbc.com/news/articles/clyzvpp8g3vo)

生成摘要时出错

---

## 56. Inside PostHog: SSRF, ClickHouse SQL Escape and Default Postgres Creds to RCE

**原文标题**: Inside PostHog: SSRF, ClickHouse SQL Escape and Default Postgres Creds to RCE

**原文链接**: [https://mdisec.com/inside-posthog-how-ssrf-a-clickhouse-sql-escaping-0day-and-default-postgresql-credentials-formed-an-rce-chain-zdi-25-099-zdi-25-097-zdi-25-096/](https://mdisec.com/inside-posthog-how-ssrf-a-clickhouse-sql-escaping-0day-and-default-postgresql-credentials-formed-an-rce-chain-zdi-25-099-zdi-25-097-zdi-25-096/)

生成摘要时出错

---

## 57. Fast SEQUENCE iteration in Common Lisp

**原文标题**: Fast SEQUENCE iteration in Common Lisp

**原文链接**: [https://world-playground-deceit.net/blog/2025/12/fast-sequence-iteration-in-common-lisp.html](https://world-playground-deceit.net/blog/2025/12/fast-sequence-iteration-in-common-lisp.html)

生成摘要时出错

---

## 58. The Number That Turned Sideways

**原文标题**: The Number That Turned Sideways

**原文链接**: [https://zuriby.github.io/math.github.io/the-number-that-turned-sideways.html](https://zuriby.github.io/math.github.io/the-number-that-turned-sideways.html)

生成摘要时出错

---

## 59. TikTok unlawfully tracks shopping habits and use of dating apps?

**原文标题**: TikTok unlawfully tracks shopping habits and use of dating apps?

**原文链接**: [https://noyb.eu/en/tiktok-unlawfully-tracks-your-shopping-habits-and-your-use-dating-apps](https://noyb.eu/en/tiktok-unlawfully-tracks-your-shopping-habits-and-your-use-dating-apps)

生成摘要时出错

---

## 60. Cloudflare Radar 2025 Year in Review

**原文标题**: Cloudflare Radar 2025 Year in Review

**原文链接**: [https://radar.cloudflare.com/year-in-review/2025](https://radar.cloudflare.com/year-in-review/2025)

生成摘要时出错

---

## 61. AI will make formal verification go mainstream

**原文标题**: AI will make formal verification go mainstream

**原文链接**: [https://martin.kleppmann.com/2025/12/08/ai-formal-verification.html](https://martin.kleppmann.com/2025/12/08/ai-formal-verification.html)

生成摘要时出错

---

## 62. Oasis: Pooling PCIe Devices over CXL to Boost Utilization

**原文标题**: Oasis: Pooling PCIe Devices over CXL to Boost Utilization

**原文链接**: [https://dl.acm.org/doi/10.1145/3731569.3764812](https://dl.acm.org/doi/10.1145/3731569.3764812)

生成摘要时出错

---

## 63. How getting richer made teenagers less free

**原文标题**: How getting richer made teenagers less free

**原文链接**: [https://www.theargumentmag.com/p/how-getting-richer-made-teenagers](https://www.theargumentmag.com/p/how-getting-richer-made-teenagers)

生成摘要时出错

---

## 64. Learning Fortran (2024)

**原文标题**: Learning Fortran (2024)

**原文链接**: [https://uncenter.dev/posts/learning-fortran/](https://uncenter.dev/posts/learning-fortran/)

生成摘要时出错

---

## 65. alpr.watch

**原文标题**: alpr.watch

**原文链接**: [https://alpr.watch/](https://alpr.watch/)

生成摘要时出错

---

## 66. A look back: LANPAR, the first spreadsheet

**原文标题**: A look back: LANPAR, the first spreadsheet

**原文链接**: [https://technicallywewrite.com/2025/12/16/lanpar](https://technicallywewrite.com/2025/12/16/lanpar)

生成摘要时出错

---

## 67. Japan to revise romanization rules for first time in 70 years

**原文标题**: Japan to revise romanization rules for first time in 70 years

**原文链接**: [https://www.japantimes.co.jp/news/2025/08/21/japan/panel-hepburn-style-romanization/](https://www.japantimes.co.jp/news/2025/08/21/japan/panel-hepburn-style-romanization/)

生成摘要时出错

---

## 68. Is Mozilla trying hard to kill itself?

**原文标题**: Is Mozilla trying hard to kill itself?

**原文链接**: [https://infosec.press/brunomiguel/is-mozilla-trying-hard-to-kill-itself](https://infosec.press/brunomiguel/is-mozilla-trying-hard-to-kill-itself)

生成摘要时出错

---

## 69. AI's real superpower: consuming, not creating

**原文标题**: AI's real superpower: consuming, not creating

**原文链接**: [https://msanroman.io/blog/ai-consumption-paradigm](https://msanroman.io/blog/ai-consumption-paradigm)

生成摘要时出错

---

## 70. No Graphics API

**原文标题**: No Graphics API

**原文链接**: [https://www.sebastianaaltonen.com/blog/no-graphics-api](https://www.sebastianaaltonen.com/blog/no-graphics-api)

生成摘要时出错

---

## 71. Nvidia Nemotron 3 Family of Models

**原文标题**: Nvidia Nemotron 3 Family of Models

**原文链接**: [https://research.nvidia.com/labs/nemotron/Nemotron-3/](https://research.nvidia.com/labs/nemotron/Nemotron-3/)

生成摘要时出错

---

## 72. TLA+ Modeling Tips

**原文标题**: TLA+ Modeling Tips

**原文链接**: [http://muratbuffalo.blogspot.com/2025/12/tla-modeling-tips.html](http://muratbuffalo.blogspot.com/2025/12/tla-modeling-tips.html)

生成摘要时出错

---

## 73. Announcing the Beta release of ty

**原文标题**: Announcing the Beta release of ty

**原文链接**: [https://astral.sh/blog/ty](https://astral.sh/blog/ty)

生成摘要时出错

---

## 74. Opencoil – appropriating inductive charging pads in the wild (2020) [video]

**原文标题**: Opencoil – appropriating inductive charging pads in the wild (2020) [video]

**原文链接**: [https://media.ccc.de/v/rc3-11575-opencoil_a_roaming_speedshow](https://media.ccc.de/v/rc3-11575-opencoil_a_roaming_speedshow)

生成摘要时出错

---

## 75. The State of AI Coding Report 2025

**原文标题**: The State of AI Coding Report 2025

**原文链接**: [https://www.greptile.com/state-of-ai-coding-2025](https://www.greptile.com/state-of-ai-coding-2025)

生成摘要时出错

---

## 76. More than half of researchers now use AI for peer review, often against guidance

**原文标题**: More than half of researchers now use AI for peer review, often against guidance

**原文链接**: [https://www.nature.com/articles/d41586-025-04066-5](https://www.nature.com/articles/d41586-025-04066-5)

生成摘要时出错

---

## 77. Show HN: DocsRouter – The OpenRouter for OCR and Vision Models

**原文标题**: Show HN: DocsRouter – The OpenRouter for OCR and Vision Models

**原文链接**: [https://docsrouter.com](https://docsrouter.com)

生成摘要时出错

---

## 78. A16z-backed Doublespeed hacked, revealing what its AI-generated accounts promote

**原文标题**: A16z-backed Doublespeed hacked, revealing what its AI-generated accounts promote

**原文链接**: [https://www.404media.co/hack-reveals-the-a16z-backed-phone-farm-flooding-tiktok-with-ai-influencers/](https://www.404media.co/hack-reveals-the-a16z-backed-phone-farm-flooding-tiktok-with-ai-influencers/)

生成摘要时出错

---

## 79. The World Happiness Report is beset with methodological problems

**原文标题**: The World Happiness Report is beset with methodological problems

**原文链接**: [https://yaschamounk.substack.com/p/the-world-happiness-report-is-a-sham](https://yaschamounk.substack.com/p/the-world-happiness-report-is-a-sham)

生成摘要时出错

---

## 80. Go-boot: bare metal Go UEFI boot manager

**原文标题**: Go-boot: bare metal Go UEFI boot manager

**原文链接**: [https://github.com/usbarmory/go-boot](https://github.com/usbarmory/go-boot)

生成摘要时出错

---

## 81. Introduction to Software Development Tooling (2024)

**原文标题**: Introduction to Software Development Tooling (2024)

**原文链接**: [https://bernsteinbear.com/isdt/](https://bernsteinbear.com/isdt/)

生成摘要时出错

---

## 82. Truth Social Parent to Merge with Nuclear Fusion Firm in $6B Deal

**原文标题**: Truth Social Parent to Merge with Nuclear Fusion Firm in $6B Deal

**原文链接**: [https://www.nytimes.com/2025/12/18/business/trump-media-tae-technologies-fusion-power-deal.html](https://www.nytimes.com/2025/12/18/business/trump-media-tae-technologies-fusion-power-deal.html)

生成摘要时出错

---

## 83. Pornhub extorted after hackers steal Premium member activity data

**原文标题**: Pornhub extorted after hackers steal Premium member activity data

**原文链接**: [https://www.bleepingcomputer.com/news/security/pornhub-extorted-after-hackers-steal-premium-member-activity-data/](https://www.bleepingcomputer.com/news/security/pornhub-extorted-after-hackers-steal-premium-member-activity-data/)

生成摘要时出错

---

## 84. Creating Diagrams in Markdown on GitHub

**原文标题**: Creating Diagrams in Markdown on GitHub

**原文链接**: [https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams)

生成摘要时出错

---

## 85. Modern SID chip substitutes [video]

**原文标题**: Modern SID chip substitutes [video]

**原文链接**: [https://www.youtube.com/watch?v=nooPmXxO6K0](https://www.youtube.com/watch?v=nooPmXxO6K0)

生成摘要时出错

---

## 86. In secret missile factory, Ukraine is ramping up its domestic arms industry

**原文标题**: In secret missile factory, Ukraine is ramping up its domestic arms industry

**原文链接**: [https://www.bbc.co.uk/news/articles/c1dz6wgn2w9o](https://www.bbc.co.uk/news/articles/c1dz6wgn2w9o)

生成摘要时出错

---

## 87. Feather Detective (2016)

**原文标题**: Feather Detective (2016)

**原文链接**: [https://www.audubon.org/magazine/behind-scenes-worlds-top-feather-detective](https://www.audubon.org/magazine/behind-scenes-worlds-top-feather-detective)

生成摘要时出错

---

## 88. No AI* Here – A Response to Mozilla's Next Chapter

**原文标题**: No AI* Here – A Response to Mozilla's Next Chapter

**原文链接**: [https://www.waterfox.com/blog/no-ai-here-response-to-mozilla/](https://www.waterfox.com/blog/no-ai-here-response-to-mozilla/)

生成摘要时出错

---

## 89. Pricing Changes for GitHub Actions

**原文标题**: Pricing Changes for GitHub Actions

**原文链接**: [https://resources.github.com/actions/2026-pricing-changes-for-github-actions/](https://resources.github.com/actions/2026-pricing-changes-for-github-actions/)

生成摘要时出错

---

## 90. Show HN: Sqlit – A lazygit-style TUI for SQL databases

**原文标题**: Show HN: Sqlit – A lazygit-style TUI for SQL databases

**原文链接**: [https://github.com/Maxteabag/sqlit](https://github.com/Maxteabag/sqlit)

生成摘要时出错

---

## 91. Full Unicode Search at 50× ICU Speed with AVX‑512

**原文标题**: Full Unicode Search at 50× ICU Speed with AVX‑512

**原文链接**: [https://ashvardanian.com/posts/search-utf8/](https://ashvardanian.com/posts/search-utf8/)

生成摘要时出错

---

## 92. GPT Image 1.5

**原文标题**: GPT Image 1.5

**原文链接**: [https://openai.com/index/new-chatgpt-images-is-here/](https://openai.com/index/new-chatgpt-images-is-here/)

生成摘要时出错

---

## 93. Thin desires are eating life

**原文标题**: Thin desires are eating life

**原文链接**: [https://www.joanwestenberg.com/thin-desires-are-eating-your-life/](https://www.joanwestenberg.com/thin-desires-are-eating-your-life/)

生成摘要时出错

---

## 94. Bonsai: A Voxel Engine, from scratch

**原文标题**: Bonsai: A Voxel Engine, from scratch

**原文链接**: [https://github.com/scallyw4g/bonsai](https://github.com/scallyw4g/bonsai)

生成摘要时出错

---

## 95. 30 years of <br> tags

**原文标题**: 30 years of <br> tags

**原文链接**: [https://www.artmann.co/articles/30-years-of-br-tags](https://www.artmann.co/articles/30-years-of-br-tags)

生成摘要时出错

---

## 96. Rust GCC backend: Why and how

**原文标题**: Rust GCC backend: Why and how

**原文链接**: [https://blog.guillaume-gomez.fr/articles/2025-12-15+Rust+GCC+backend%3A+Why+and+how](https://blog.guillaume-gomez.fr/articles/2025-12-15+Rust+GCC+backend%3A+Why+and+how)

生成摘要时出错

---

## 97. Mozilla appoints new CEO Anthony Enzor-Demeo

**原文标题**: Mozilla appoints new CEO Anthony Enzor-Demeo

**原文链接**: [https://blog.mozilla.org/en/mozilla/leadership/mozillas-next-chapter-anthony-enzor-demeo-new-ceo/](https://blog.mozilla.org/en/mozilla/leadership/mozillas-next-chapter-anthony-enzor-demeo-new-ceo/)

生成摘要时出错

---

## 98. 40 percent of fMRI signals do not correspond to actual brain activity

**原文标题**: 40 percent of fMRI signals do not correspond to actual brain activity

**原文链接**: [https://www.tum.de/en/news-and-events/all-news/press-releases/details/40-percent-of-mri-signals-do-not-correspond-to-actual-brain-activity](https://www.tum.de/en/news-and-events/all-news/press-releases/details/40-percent-of-mri-signals-do-not-correspond-to-actual-brain-activity)

生成摘要时出错

---

## 99. Security vulnerability found in Rust Linux kernel code

**原文标题**: Security vulnerability found in Rust Linux kernel code

**原文链接**: [https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/commit/?id=3e0ae02ba831da2b707905f4e602e43f8507b8cc](https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/commit/?id=3e0ae02ba831da2b707905f4e602e43f8507b8cc)

生成摘要时出错

---

## 100. Purrtran – ᓚᘏᗢ – A Programming Language for Cat People

**原文标题**: Purrtran – ᓚᘏᗢ – A Programming Language for Cat People

**原文链接**: [https://github.com/cmontella/purrtran](https://github.com/cmontella/purrtran)

生成摘要时出错

---

