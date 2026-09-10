# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-09-10.md)

*最后自动更新时间: 2026-09-10 19:55:45*
## 1. Rust 是微软的一级语言

**原文标题**: Rust is tier-1 language at Microsoft

**原文链接**: [https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/)

微软已正式将 Rust 提升为内部开发的“一级”（Tier-1）语言，使其与 C++、C# 和 TypeScript 并列。这一定位为微软团队提供了通往生产环境的“铺就之路”（paved path），包括安全的工具链、深度的平台集成，以及完全符合公司安全开发生命周期（SDL）要求的能力。

此次转型的基石是引入了 **rustc_codegen_utc**，这是一个将 Rust 编译器（`rustc`）连接到 MSVC (UTC) 后端的新编译器后端。这使得 Rust 在 Windows 上能够超越其传统的基于 LLVM 的根基，直接参与到原生 Windows 工程生态系统中。这种统一后端的主要优势包括：

*   **无缝互操作性：** Rust 与 C++ 之间的高保真 ABI 兼容性和跨语言内联，这对于混合项目至关重要。
*   **平台特性：** 可调用 Windows 特有的功能，如热补丁（Hotpatching）、二进制加固以及样本配置文件引导优化（SPGO）。
*   **统一工具链：** 共享现有的 MSVC 基础设施，用于调试、崩溃转储分析和性能剖析。

微软的策略旨在通过为两种语言利用共同的基础来降低维护成本。这确保了 Windows 平台或 MSVC 编译器的任何创新都能自动惠及 Rust 和 C++ 开发者。截至 2026 年底，`rustc_codegen_utc` 已达到生产就绪状态，自 Rust 1.90 起实现自托管，并已集成到 100 多个微软内部仓库中。这一举措代表了对微软软件栈进行“氧化”（oxidizing）的重大长期承诺——从固件和内核到云微服务——同时保持其现有 C++ 代码库的性能和稳定性。

---

## 2. 我有一个理论：软件能把人逼疯。

**原文标题**: I have a theory that software drives people insane

**原文链接**: [https://graybeard.ing/software-drives-people-insane/](https://graybeard.ing/software-drives-people-insane/)

在《软件让人发疯》一文中，作者指出，软件开发独特的工作环境——极高的速度、巨大的财务投入以及无限的可变性——导致了人们心理上分寸感的丧失。与物理建筑不同，软件缺乏自然阻力；由于改动在技术上可行且没有“可见”成本（如材料损耗），领导层往往认为这些改动是免费的。这导致了一个恶性循环：“可以做”变成了“必须做”，每一个微小的功能都被赋予了生死存亡般的紧迫感。

文章强调了导致这种“疯狂”的几个核心驱动因素：
*   **隐形成本：** 移动房屋的一堵墙有明显的代价，但软件变更的成本却隐藏在上下文切换、架构侵蚀和开发势头的丧失中。
*   **没有“完工”之说：** 与完工的橱柜不同，软件总能被优化、扩展或重构，从而陷入永久的不完整状态。
*   **将复杂性视为地位象征：** 复杂的系统能提供心理回报并营造重要感，导致团队将简单的工具（往往只是“高级电子表格”）过度设计成庞大的分布式平台。
*   **组织异变：** 最终，公司开始像对待软件一样对待自身的组织结构：使其处于永久可变的状态，总觉得只要再经历一次“重构”就能达到完美。

作者总结道，最被低估的工程技能是“不去动它”。为了保持理智，行业必须拥抱“分寸感”——即意识到并非每个想法都应该出现在路线图中，耐心往往比持续的瞎忙更有价值。与其追逐“统治世界”或无限规模，我们应当记住，软件本质上是让生活更轻松的工具，而不是用来进行不必要折腾的意识形态战场。

---

## 3. Cognition 发布全新 SWE-2 模型，对标 Fable 5.1 和 GPT-Astra

**原文标题**: Cognition launches new SWE-2 model, Rivaling Fable 5.1 and GPT-Astra

**原文链接**: [https://cognition.com/blog/swe-2](https://cognition.com/blog/swe-2)

Cognition 宣布推出其迄今为止最先进的代码模型 **SWE-2**，旨在最大化能力与成本的“帕累托前沿”。基于拥有 2.8 万亿参数的 **Kimi K3** 进行后期训练，SWE-2 在 FrontierCode 1.1 Main 基准测试中取得了 50.0% 的评分。这一性能可与 Fable 5.1 和 GPT-5.6 Sol 等行业领先模型相媲美，同时其运行成本比 Fable 低 64%，仅为 GPT-6 Astra 的四分之一。

**核心技术创新：**
*   **多万亿参数强化学习 (RL)：** Cognition 首次将强化学习扩展到了多万亿参数规模。他们引入了一种 RL 算法，通过应用根据模型性能曲线调整的线性成本惩罚，在单次运行中即可完成所有推理力度（中、高、最高）的训练。
*   **训练稳定性：** 团队实施了“长度加权奖励基准”，以减少梯度方差并稳定 RL 过程，在确保模型保持高性能的同时，降低推理与训练之间的差异。
*   **基础设施效率：** 为了最大化吞吐量，SWE-2 采用了带有在线草图模型训练的 DSpark 推测性解码以及 NVFP4/FP8 量化技术。这些优化使得 2.8T 规模的模型尽管体量巨大，仍能保持高效运行。

**行为与性能提升：**
SWE-2 显著提升了工程判断力。与前代模型 SWE-1.7 在处理简单任务时偶尔会“过度思考”不同，SWE-2 能更快速地识别相关的代码库区域。在 FrontierCode 基准测试中，其解决问题的对话轮数比 SWE-1.7 减少了 58%，平均成本降低了 81%。它还展示了卓越的测试覆盖率、在受阻时更强的应变能力，以及一种“验证纪律”——即重新推导结论而非盲目信任表层证据。

SWE-2 即日起在 **Devin** 桌面端和 CLI 中上线，Web 端和 Fusion 平台也正在陆续推出。

---

## 4. 关于研究人员能否信任 OpenAI 处理未发表数学研究的更多质疑

**原文标题**: More questions about whether researchers can trust OpenAI with unpublished math

**原文链接**: [https://mathstodon.xyz/@andreasthom/117240535270608201](https://mathstodon.xyz/@andreasthom/117240535270608201)

本文及 Mathstodon 上的相关讨论凸显了数学研究界对于在未发表的工作中使用 OpenAI 高级模型（特别是 o1 系列）日益增长的焦虑。

这场由 Tristan Buckmaster 发起并经 Andreas Thom 传播的讨论集中在几个核心关切点上：

*   **数据隐私与训练：** 研究人员担心，将技术性的、未发表的证明或原创问题输入 OpenAI 模型，可能会导致这些数据被摄取用于训练。这增加了 AI 随后向其他用户“泄露”或重新生成这些专有想法的风险。
*   **“o1”事件：** Buckmaster 分享了一次经历，他用一篇未发表论文中的问题测试了 o1 模型。该模型极高的表现水平及其处理复杂、新颖推理的能力引发了人们的担忧，即私人研究与 AI 训练集之间的界限已变得极其模糊。
*   **知识产权风险：** 存在关于“数学抄袭”的重大担忧。如果研究人员使用 AI 协助完成证明，社区尚不清楚由此产生的见解归谁“所有”，以及研究人员是否在无意中将其发现置于公共领域或 OpenAI 之手。
*   **对服务条款的信任：** 尽管 OpenAI 提供了一定的数据隐私设置，但数学家们正在讨论这些保护措施对于高风险、原创性的突破是否足够。

**结论：**
目前的共识反映了一个困境：虽然 AI 工具在证明检查和头脑风暴方面提供了强大的辅助，但潜在的代价——即失去对原创数学发现的控制——正促使许多研究人员建议，不要在敏感的、未发表的工作中使用这些模型。

---

## 5. NASA原为火星设计的色彩技术，现正揭开地球岩画的面纱。

**原文标题**: NASA Color Trick Was Meant for Mars. Now It's Unveiling Rock Art on Earth

**原文链接**: [https://gizmodo.com/this-nasa-color-trick-was-meant-for-mars-now-its-unveiling-rock-art-on-earth-2000809844](https://gizmodo.com/this-nasa-color-trick-was-meant-for-mars-now-its-unveiling-rock-art-on-earth-2000809844)

一项最初为帮助美国国家航空航天局（NASA）探索火星表面而设计的软件技术，如今正彻底改变考古学家研究地球古代岩画的方式。

这款名为 **DStretch**（去相关拉伸）的工具由研究员乔恩·哈曼（Jon Harman）开发。它利用一种算法来增强数字图像中肉眼几乎不可见的细微颜色差异。NASA 最初在火星探测器任务中应用了这种“色彩技巧”，使科学家能够在原本色彩单调的火星景观中区分不同的矿物成分和地质特征。

在地球上，这项技术已成为记录褪色的彩色岩画和岩刻的变革性工具。几千年来，许多古代岩画因风化、矿物结壳或自然褪色而变得模糊不清。通过对这些遗址的照片应用 DStretch 技术，研究人员可以“拉伸”光谱，从而揭示此前被隐藏的鲜艳红色、黄色和黑色。

该方法的主要优势在于它完全是非侵入性的。考古学家无需接触或可能损坏脆弱的文化遗产遗址，就能发现复杂的图案和历史叙事。从欧洲的洞穴到美国西南部偏远的峡谷，DStretch 正在帮助专家识别失传的艺术作品，并更深入地了解创造这些作品的文化。

通过重新利用这项旨在探索太空前沿的技术，科学家们获得了一个审视人类历史的强大新视角，这证明了为探索未来而设计的工具在揭示遥远的过去时同样卓有成效。

---

## 6. Shopify moves back to Native from React Native

**原文标题**: Shopify moves back to Native from React Native

**原文链接**: [https://shopify.engineering/back-to-native](https://shopify.engineering/back-to-native)

Shopify has announced a strategic shift from React Native back to native development (Swift for iOS and Kotlin for Android), citing a fundamental change in the economics of mobile development driven by AI coding agents. 

While Shopify’s 2020 move to React Native was successful in reducing the cost of maintaining feature parity, the company argues that LLMs have invalidated the core assumption that building for two platforms requires twice the work. Modern AI agents can now handle significant portions of implementation, translation, and testing, making the benefits of native performance and first-party tooling more attractive than the convenience of a shared codebase.

**Key highlights of the transition include:**

*   **AI-Driven Migration:** Shopify is opting for a "greenfield" rewrite of its major apps. Using a proprietary system called **Helix**, they ensure code quality through an iterative loop of checkpoints, automated tests, and human reviews. This process allowed them to rebuild the **Shop app** from scratch in just 12 weeks.
*   **Agent-Addressable Architecture:** To accelerate feedback loops, Shopify is decoupling business logic from UI. This allows AI agents to test and iterate via a CLI in milliseconds rather than relying on slow mobile simulators.
*   **Sunsetting Open-Source Libraries:** Shopify will wind down its support for popular React Native libraries. **FlashList** and **React Native Skia** will be transitioned to new stewards or forks, while **Restyle** will be archived by the end of 2026.

The flagship **Shopify app** is currently being migrated, with other apps to follow. Ultimately, Shopify views this move as a way to leverage the superior capabilities of native platforms while utilizing AI to maintain high product velocity.

---

## 7. Neki

**原文标题**: Neki

**原文链接**: [https://planetscale.com/blog/introducing-neki](https://planetscale.com/blog/introducing-neki)

生成摘要时出错

---

## 8. Forgejo <=16.0.3 Critical RCE

**原文标题**: Forgejo <=16.0.3 Critical RCE

**原文链接**: [https://codeberg.org/forgejo/forgejo/src/branch/forgejo/release-notes-published/16.0.4.md](https://codeberg.org/forgejo/forgejo/src/branch/forgejo/release-notes-published/16.0.4.md)

生成摘要时出错

---

## 9. Douglas Hofstadter: Analogy as the Core of Cognition [video]

**原文标题**: Douglas Hofstadter: Analogy as the Core of Cognition [video]

**原文链接**: [https://www.youtube.com/watch?v=n8m7lFQ3njk](https://www.youtube.com/watch?v=n8m7lFQ3njk)

生成摘要时出错

---

## 10. Music Theory for the 21st-Century Classroom

**原文标题**: Music Theory for the 21st-Century Classroom

**原文链接**: [https://musictheory.pugetsound.edu/mt21c/MusicTheory.html](https://musictheory.pugetsound.edu/mt21c/MusicTheory.html)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 2 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 3 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 4 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 5 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 6 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 7 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 8 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 9 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 10 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 11 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 12 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 13 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 14 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 15 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 16 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 17 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 18 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 19 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 20 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 21 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 22 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 23 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 24 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 25 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 26 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 27 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 28 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 29 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 30 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 31 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 32 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 33 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 34 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 35 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 36 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 37 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 38 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 39 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 40 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 41 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 42 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 43 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 44 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 45 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 46 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 47 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 48 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 49 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 50 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 51 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 52 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 53 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 54 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 55 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 56 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 57 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 58 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 59 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 60 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 61 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 62 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 63 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 64 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 65 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 66 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 67 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 68 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 69 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 70 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 71 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 72 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 73 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 74 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 75 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 76 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 77 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 78 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 79 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 80 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 81 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 82 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 83 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 84 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 85 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 86 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 87 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 88 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 89 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 90 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 91 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 92 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 93 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 94 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 95 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 96 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 97 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 98 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 99 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 100 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 101 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 102 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 103 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 104 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 105 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 106 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 107 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 108 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 109 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 110 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 111 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 112 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 113 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 114 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 115 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 116 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 117 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 118 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 119 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 120 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 121 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 122 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 123 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 124 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 125 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 126 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 127 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 128 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 129 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 130 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 131 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 132 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 133 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 134 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 135 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 136 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 137 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 138 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 139 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 140 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 141 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 142 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 143 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 144 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 145 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 146 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 147 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 148 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 149 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 150 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 151 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 152 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 153 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 154 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 155 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 156 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 157 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 158 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 159 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 160 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 161 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 162 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 163 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 164 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 165 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 166 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 167 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 168 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 169 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 170 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 171 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 172 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 173 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 174 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 175 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 176 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 177 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 178 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 179 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 180 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 181 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 182 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 183 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 184 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 185 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 186 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 187 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 188 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 189 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 190 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 191 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 192 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 193 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 194 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 195 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 196 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 197 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 198 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 199 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 200 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 201 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 202 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 203 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 204 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 205 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 206 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 207 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 208 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 209 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 210 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 211 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 212 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 213 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 214 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 215 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 216 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 217 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 218 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 219 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 220 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 221 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 222 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 223 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 224 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 225 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 226 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 227 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 228 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 229 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 230 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 231 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 232 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 233 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 234 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 235 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 236 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 237 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 238 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 239 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 240 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 241 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 242 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 243 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 244 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 245 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 246 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 247 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 248 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 249 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 250 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 251 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 252 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 253 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 254 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 255 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 256 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 257 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 258 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 259 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 260 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 261 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 262 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 263 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 264 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 265 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 266 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 267 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 268 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 269 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 270 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 271 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 272 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 273 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 274 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 275 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 276 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 277 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 278 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 279 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 280 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 281 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 282 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 283 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 284 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 285 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 286 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 287 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 288 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 289 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 290 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 291 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 292 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 293 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 294 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 295 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 296 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 297 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 298 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 299 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 300 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 301 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 302 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 303 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 304 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 305 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 306 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 307 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 308 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 309 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 310 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 311 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 312 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 313 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 314 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 315 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 316 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 317 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 318 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 319 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 320 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 321 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 322 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 323 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 324 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 325 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 326 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 327 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 328 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 329 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 330 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 331 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 332 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 333 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 334 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 335 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 336 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 337 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 338 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 339 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 340 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 341 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 342 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 343 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 344 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 345 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 346 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 347 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 348 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 349 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 350 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 351 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 352 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 353 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 354 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 355 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 356 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 357 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 358 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 359 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 360 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 361 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 362 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 363 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 364 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 365 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 366 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 367 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 368 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 369 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 370 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 371 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 372 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 373 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 374 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 375 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 376 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 377 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 378 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 379 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 380 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 381 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 382 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 383 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 384 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 385 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 386 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 387 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 388 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 389 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 390 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 391 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 392 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 393 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 394 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 395 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 396 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 397 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 398 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 399 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 400 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 401 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 402 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 403 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 404 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 405 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 406 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 407 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 408 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 409 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 410 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 411 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 412 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 413 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 414 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 415 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 416 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 417 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 418 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 419 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 420 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 421 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 422 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 423 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 424 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 425 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 426 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 427 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 428 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 429 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 430 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 431 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 432 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 433 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 434 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 435 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 436 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 437 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 438 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 439 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 440 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 441 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 442 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 443 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 444 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 445 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 446 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 447 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 448 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 449 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 450 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 451 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 452 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 453 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 454 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 455 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 456 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 457 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 458 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 459 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 460 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 461 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 462 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 463 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 464 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 465 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 466 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 467 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 468 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 469 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 470 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 471 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 472 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 473 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 474 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 475 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 476 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 477 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 478 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 479 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 480 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 481 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 482 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 483 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 484 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 485 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 486 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 487 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 488 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 489 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 490 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 491 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 492 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 493 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 494 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 495 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 496 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 497 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 498 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 499 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 500 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 501 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 502 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 503 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 504 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 505 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 506 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 507 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 508 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 509 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 510 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 511 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 512 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 513 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 514 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 515 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 516 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 517 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 518 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 519 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 520 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 521 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 522 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 523 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 524 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 525 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 526 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 527 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 528 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 529 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 530 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 531 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 532 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 533 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 534 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 535 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 536 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 537 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
