# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-12-18.md)

*最后自动更新时间: 2025-12-18 17:51:24*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 2 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 3 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 4 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 5 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 6 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 7 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 8 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 9 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 10 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 11 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 12 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 13 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 14 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 15 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 16 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 17 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 18 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 19 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 20 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 21 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 22 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 23 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 24 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 25 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 26 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 27 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 28 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 29 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 30 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 31 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 32 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 33 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 34 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 35 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 36 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 37 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 38 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 39 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 40 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 41 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 42 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 43 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 44 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 45 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 46 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 47 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 48 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 49 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 50 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 51 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 52 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 53 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 54 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 55 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 56 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 57 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 58 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 59 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 60 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 61 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 62 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 63 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 64 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 65 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 66 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 67 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 68 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 69 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 70 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 71 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 72 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 73 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 74 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 75 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 76 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 77 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 78 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 79 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 80 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 81 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 82 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 83 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 84 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 85 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 86 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 87 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 88 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 89 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 90 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 91 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 92 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 93 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 94 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 95 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 96 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 97 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 98 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 99 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 100 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 101 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 102 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 103 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 104 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 105 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 106 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 107 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 108 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 109 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 110 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 111 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 112 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 113 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 114 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 115 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 116 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 117 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 118 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 119 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 120 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 121 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 122 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 123 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 124 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 125 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 126 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 127 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 128 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 129 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 130 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 131 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 132 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 133 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 134 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 135 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 136 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 137 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 138 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 139 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 140 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 141 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 142 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 143 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 144 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 145 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 146 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 147 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 148 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 149 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 150 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 151 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 152 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 153 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 154 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 155 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 156 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 157 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 158 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 159 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 160 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 161 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 162 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 163 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 164 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 165 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 166 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 167 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 168 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 169 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 170 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 171 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 172 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 173 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 174 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 175 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 176 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 177 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 178 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 179 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 180 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 181 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 182 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 183 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 184 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 185 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 186 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 187 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 188 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 189 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 190 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 191 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 192 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 193 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 194 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 195 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 196 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 197 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 198 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 199 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 200 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 201 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 202 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 203 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 204 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 205 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 206 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 207 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 208 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 209 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 210 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 211 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 212 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 213 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 214 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 215 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 216 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 217 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 218 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 219 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 220 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 221 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 222 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 223 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 224 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 225 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 226 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 227 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 228 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 229 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 230 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 231 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 232 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 233 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 234 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 235 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 236 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 237 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 238 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 239 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 240 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 241 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 242 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 243 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 244 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 245 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 246 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 247 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 248 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 249 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 250 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 251 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 252 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 253 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 254 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 255 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 256 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 257 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 258 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 259 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 260 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 261 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 262 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 263 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 264 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 265 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 266 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 267 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 268 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 269 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 270 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 271 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 272 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 273 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
