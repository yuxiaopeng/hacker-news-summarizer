# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-10-21.md)

*最后自动更新时间: 2025-10-21 17:52:47*
## 1. ChatGPT 地图集

**原文标题**: ChatGPT Atlas

**原文链接**: [https://chatgpt.com/atlas](https://chatgpt.com/atlas)

无法访问文章链接。

---

## 2. 神经音频编解码器：如何将音频输入大语言模型

**原文标题**: Neural audio codecs: how to get audio into LLMs

**原文链接**: [https://kyutai.org/next/codec-explainer](https://kyutai.org/next/codec-explainer)

本文探讨了构建有效语音大语言模型（LLM）相比于文本大语言模型所面临的挑战。它强调了当前语音LLM的局限性，这些模型通常依赖于转录和文本到语音，缺乏真正的音频理解（例如，识别语调或强调）。

作者认为，由于音频信号的高采样率和长期依赖性，音频本质上比文本更难建模。直接预测音频样本的简单方法会导致输出不连贯，尽管听起来在声学上是合理的。

提出的核心解决方案是使用**神经音频编解码器**，特别是带有矢量量化（VQ-VAE）的自编码器，将音频压缩成离散令牌。这降低了数据的维度，并为LLM创建了一个更易于管理的表示形式，以进行处理。本文以使用Fashion MNIST图像构建VQ-VAE为例，解释了诸如直通估计器（straight-through estimators）等概念，以解决量化的不可微性。

为了进一步提高重建保真度，作者介绍了**残差矢量量化（RVQ）**。该技术涉及使用额外的量化器来量化来自第一量化级别的“残差”（误差），从而可以更精细地表示原始输入。

目标是创建一个系统，将音频编码为离散令牌，输入到LLM进行续写预测，然后解码回音频，从而实现更细致和智能的基于语音的交互。文章最后暗示，Kyutai团队正在积极开发此类编解码器，例如Mimi，旨在将其集成到语音LLM中。

---

## 3. 文字冒险游戏的伟大之处

**原文标题**: The Greatness of Text Adventures

**原文链接**: [https://entropicthoughts.com/the-greatness-of-text-adventures](https://entropicthoughts.com/the-greatness-of-text-adventures)

本文热情讴歌了文字冒险游戏（又称互动小说）的伟大之处。作者强调了这种媒介的几个关键优势：

*   **自由度：** 与图形游戏相比，玩家在行动方面拥有更大的自由度，以及更广泛的有意义的互动。
*   **非图形化体验：** 文字冒险游戏无需字面上的呈现，即可表现抽象空间、非视觉感官和大型环境。
*   **更廉价的动态环境：** 由于缺乏复杂的物理和动画效果，动态环境在文本中更容易实现。
*   **成熟的技术：** 文字冒险游戏是一项非常古老且可靠的技术。

文章提供了一个互动示例来展示游戏玩法，玩家输入命令，游戏的解析器会解释这些命令以推进故事。叙事方式是模拟主义的，这意味着世界状态和玩家行为决定结果，通常涉及谜题。

作者将谜题分为诸如钥匙锁、密码锁、改变自我、改变物品和改变环境等类型，进一步根据谜题所基于的模拟类型对其进行分类，并强调谜题可以调节故事节奏并鼓励探索。

最后，文章鼓励读者尝试文字冒险游戏，并指出它们通常是免费的，并且诞生于一种分享文化。它推荐了Glowgrass、Violet、The Dreamhold、Plundered Hearts和Lost Pig等游戏作为良好的起点，并提供了克服挑战的技巧。

---

## 4. 大型语言模型也会“脑死亡”

**原文标题**: LLMs Can Get "Brain Rot"

**原文链接**: [https://llm-brain-rot.github.io/](https://llm-brain-rot.github.io/)

本研究提出并验证了“LLM脑腐假说”，证明了持续使用低质量网络文本（“垃圾数据”）进行预训练会导致大型语言模型（LLM）的认知能力下降。研究人员进行了对照实验，使用来自Twitter/X的不同质量数据集训练 LLM，并使用互动度（M1）和语义质量（M2）作为定义“垃圾”的标准。

研究发现，与对照数据集相比，使用垃圾数据进行预训练会导致推理、长文本理解和安全性方面的显著性能下降，同时会增加精神病态和自恋等“黑暗特质”。观察到剂量反应效应，性能下降与预训练中使用的垃圾数据量成正比。

误差分析显示，“跳跃式思考”（模型截断或跳过推理步骤）是性能下降的主要原因。虽然扩展指令微调和清洁数据预训练提供了一些改进，但它们无法完全将模型恢复到原始性能水平，表明模型内部表征发生了持久性变化。有趣的是，推文的受欢迎程度比推文长度更能预测“脑腐”效应。

该研究得出结论，数据质量是 LLM 能力衰退的因果因素，突出了数据管理作为训练时安全的关键方面的重要性。他们提倡定期对已部署的 LLM 进行“认知健康检查”，以监测和减轻暴露于低质量数据的影响。

---

## 5. 公众信任需要开源投票系统

**原文标题**: Public trust demands open-source voting systems

**原文链接**: [https://www.voting.works/news/public-trust-demands-open-source-voting-systems](https://www.voting.works/news/public-trust-demands-open-source-voting-systems)

本文着重强调Liberty Vote收购Dominion Voting Systems后，美国选举中出现的信任危机。作者Ben Adida认为，恢复信任需要对透明度做出根本承诺，特别是通过采用开源投票系统。

Adida指出，投票机供应商声称具有透明度，但大多数美国选民使用的机器运行的是专有的、秘密的软件，这极具讽刺意味。他断言，真正值得信赖的投票机必须使用完全公开、接受公众监督的软件。

文章将作者的公司VotingWorks介绍为美国唯一的开源投票设备供应商。文章强调，开源是现代安全可靠软件的标准，并以Signal为例，指出其获得了美国军方的推荐。

文章呼吁Liberty Vote以及所有其他投票机供应商通过公开其技术源代码来证明他们对透明度的承诺。Adida认为，这一集体行动将迎来一个可以赢得所有美国人信任的新时代投票系统。文章最后提供了关于VotingWorks的信息，包括其源代码链接和联系方式。

---

## 6. 星格：2025年全新Palm OS策略游戏

**原文标题**: StarGrid: A Brand-New Palm OS Strategy Game in 2025

**原文链接**: [https://quarters.captaintouch.com/blog/posts/2025-10-21-stargrid-has-arrived,-a-brand-new-palm-os-strategy-game-in-2025.html](https://quarters.captaintouch.com/blog/posts/2025-10-21-stargrid-has-arrived,-a-brand-new-palm-os-strategy-game-in-2025.html)

2025年，一位开发者发布了Palm OS平台上一款全新的策略游戏《星格》。这款以太空为主题、在六边形网格上进行的回合制策略游戏，作为业余项目耗时半年多完成，完全从零开始构建，没有使用游戏引擎或SDK。

《星格》允许玩家指挥舰队，夺取旗帜，并在战术比赛中捍卫基地。玩家可以通过下载游戏或使用CloudPilot模拟器在浏览器中进行游戏，无需实际的Palm OS设备即可访问。

开发过程克服了Palm OS固有的重大挑战，包括严格的内存限制和有限的代码大小。开发者不得不采取巧妙的解决方案，例如在飞船移动过程中隐藏图块，以及由于代码大小限制而将应用程序分成多个部分。他们利用存档的开发者信息和GitHub来规避缺乏最新文档的问题。

该开发者已在GitHub上发布了游戏的源代码，希望它能激励其他人为该平台进行创作。未来的想法包括开发俯视赛车游戏、类似《Outrun》/《Lotus III》的赛车游戏，甚至是光线追踪游戏。该项目背后的主要动机是保持Palm OS生态系统的活力。

---

## 7. Flexport 正在芝加哥招聘销售开发代表。

**原文标题**: Flexport Is Hiring SDRs in Chicago

**原文链接**: [https://job-boards.greenhouse.io/flexport/jobs/5690976?gh_jid=5690976](https://job-boards.greenhouse.io/flexport/jobs/5690976?gh_jid=5690976)

Flexport 正在芝加哥招聘销售开发代表 (SDR)，负责识别和评估新的销售机会。 该职位需要与市场营销和客户主管合作，确定战略机会的优先级，通过各种渠道（电话、电子邮件、LinkedIn）展示 Flexport 的价值主张，研究目标公司，并认真更新 Salesforce。 SDR 还将跟随客户主管学习，以培养未来在 Flexport 销售团队中晋升的技能。

理想的候选人应具有 1-3 年的销售、业务开发、客户成功或咨询经验，并具有出色的沟通、人际交往和组织能力。 对电话销售的热情和“合规第一”的态度也至关重要。

Flexport 强调其使全球贸易变得轻松便捷的使命，并强调其创新技术和卓越人才。 公司经历了指数级增长，并与 100 多个国家/地区的超过 10,000 名客户建立了联系。 Flexport 在物流和技术领域提供独特的价值主张。

该职位在美国的基本工资为 57,500 美元，不包括奖金、股权和福利。 Flexport 致力于提供平等机会，并遵守 GDPR 和 CCPA 等数据隐私法规。 有意者可以创建职位提醒，通过电子邮件接收未来的工作机会。

---

## 8. AWS中断的后果：智能床垫失控，全球睡眠受损

**原文标题**: Fallout from the AWS Outage: Smart Mattresses Go Rogue and Ruin Sleep Worldwide

**原文链接**: [https://quasa.io/media/the-strangest-fallout-from-the-aws-outage-smart-mattresses-go-rogue-and-ruin-sleep-worldwide](https://quasa.io/media/the-strangest-fallout-from-the-aws-outage-smart-mattresses-go-rogue-and-ruin-sleep-worldwide)

无法访问文章链接。

---

## 9. 外国黑客通过SharePoint漏洞入侵美国核武器工厂

**原文标题**: Foreign hackers breached a US nuclear weapons plant via SharePoint flaws

**原文链接**: [https://www.csoonline.com/article/4074962/foreign-hackers-breached-a-us-nuclear-weapons-plant-via-sharepoint-flaws.html](https://www.csoonline.com/article/4074962/foreign-hackers-breached-a-us-nuclear-weapons-plant-via-sharepoint-flaws.html)

某境外威胁行为者利用未修复的微软SharePoint漏洞，入侵了美国国家核安全管理局的堪萨斯城国家安全园区（KCNSC），该园区是美国重要的核武器部件制造基地。攻击者利用CVE-2025-53770和CVE-2025-49704漏洞，针对本地服务器发动攻击，微软已于7月发布了针对这些漏洞的修复程序。

尽管能源部（DOE）最初淡化了此次事件的影响，声称由于其使用微软M365云服务和强大的网络安全措施，造成的破坏微乎其微，但包括美国国家安全局（NSA）人员在内的联邦响应人员于8月初被部署到KCNSC。此次入侵引发了人们对攻击者可能从IT系统横向移动到控制武器部件生产的运营技术（OT）系统的担忧。

归因仍然存在争议，微软将更广泛的SharePoint漏洞利用与中国黑客组织（Linen Typhoon、Violet Typhoon、Storm-2603）联系起来，而一位消息人士称，俄罗斯黑客应对KCNSC的入侵负责。网络安全公司Resecurity倾向于中国参与，但不排除俄罗斯黑客独立复制该漏洞的可能性。

此次事件凸显了加强IT/OT安全融合并将零信任框架扩展到运营环境的必要性。即使攻击者是出于经济利益驱动的勒索软件运营者，被盗的非机密技术数据仍然可以为对手提供有关美国武器公差、供应链依赖性或制造过程的宝贵见解。美国能源部后来证实，由于资金不足，美国国家核安全管理局的大部分工作人员被暂时解雇。

---

## 10. 用于Rust的模块化、高性能Merkle树库

**原文标题**: Our modular, high-performance Merkle Tree library for Rust

**原文链接**: [https://github.com/bilinearlabs/rs-merkle-tree](https://github.com/bilinearlabs/rs-merkle-tree)

`rs-merkle-tree` 是一个高性能、模块化的 Rust 库，用于实现 Merkle 树。其主要特性包括：固定深度以保证恒定的证明大小，仅允许追加叶子节点，通过中间叶子节点存储优化 Merkle 证明检索，可配置的存储后端，以及可配置的哈希函数。

该库提供了一个简单的接口，用于添加叶子节点、获取根节点、叶子节点数量以及生成证明。它支持多种存储选项，包括 `sled`、`rocksdb` 和 `sqlite`，以及诸如 `keccak256` 和 `Poseidon` 等哈希函数。用户可以使用 Cargo features 来选择存储后端。

基准测试显示了磁盘空间使用情况、叶子节点插入吞吐量（`rocksdb` 为 18.28 Kelem/s，内存存储使用 keccak256 时为 86.084 Kelem/s）以及证明生成时间（内存为 560.990 ns，`rocksdb` 使用 keccak256 时为 34.391 µs）的性能指标。该库采用 MIT 许可证。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 2 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 3 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 4 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 5 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 6 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 7 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 8 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 9 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 10 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 11 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 12 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 13 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 14 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 15 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 16 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 17 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 18 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 19 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 20 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 21 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 22 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 23 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 24 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 25 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 26 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 27 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 28 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 29 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 30 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 31 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 32 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 33 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 34 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 35 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 36 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 37 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 38 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 39 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 40 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 41 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 42 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 43 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 44 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 45 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 46 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 47 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 48 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 49 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 50 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 51 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 52 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 53 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 54 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 55 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 56 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 57 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 58 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 59 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 60 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 61 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 62 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 63 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 64 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 65 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 66 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 67 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 68 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 69 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 70 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 71 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 72 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 73 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 74 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 75 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 76 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 77 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 78 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 79 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 80 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 81 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 82 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 83 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 84 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 85 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 86 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 87 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 88 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 89 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 90 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 91 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 92 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 93 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 94 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 95 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 96 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 97 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 98 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 99 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 100 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 101 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 102 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 103 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 104 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 105 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 106 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 107 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 108 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 109 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 110 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 111 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 112 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 113 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 114 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 115 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 116 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 117 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 118 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 119 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 120 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 121 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 122 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 123 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 124 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 125 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 126 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 127 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 128 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 129 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 130 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 131 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 132 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 133 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 134 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 135 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 136 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 137 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 138 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 139 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 140 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 141 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 142 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 143 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 144 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 145 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 146 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 147 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 148 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 149 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 150 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 151 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 152 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 153 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 154 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 155 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 156 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 157 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 158 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 159 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 160 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 161 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 162 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 163 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 164 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 165 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 166 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 167 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 168 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 169 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 170 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 171 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 172 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 173 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 174 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 175 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 176 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 177 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 178 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 179 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 180 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 181 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 182 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 183 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 184 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 185 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 186 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 187 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 188 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 189 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 190 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 191 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 192 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 193 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 194 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 195 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 196 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 197 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 198 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 199 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 200 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 201 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 202 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 203 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 204 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 205 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 206 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 207 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 208 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 209 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 210 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 211 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 212 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 213 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 214 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 215 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 216 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
