# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-02-10.md)

*最后自动更新时间: 2026-02-10 18:31:14*
## 1. 逐个子系统简化 Vulkan

**原文标题**: Simplifying Vulkan one subsystem at a time

**原文链接**: [https://www.khronos.org/blog/simplifying-vulkan-one-subsystem-at-a-time](https://www.khronos.org/blog/simplifying-vulkan-one-subsystem-at-a-time)

在本文中，AMD 软件架构师 Tobias Hector 概述了管理 Vulkan 复杂性的新策略：**子系统替换 (Subsystem Replacement)**。

长期以来，Vulkan 依靠扩展来提供快速更新，但这导致了“扩展爆炸问题”。大量相互作用的扩展使得该 API 在不同厂商之间的导航、优化和支持变得困难。为了解决这一问题，Vulkan 工作组正在摒弃渐进式的微调，转而采用现代、精简的替代方案来彻底替换整个旧版子系统。

这种方法的首次重大实现是 **`VK_EXT_descriptor_heap`** 扩展。该扩展旨在全面取代现有的描述符集子系统——包括布局 (layouts)、推送描述符 (push descriptors) 和描述符缓冲 (descriptor buffers)。新系统不再通过不透明的 API 命令和限制性的绑定来管理描述符，而是将描述符视为简单的数据和内存，借鉴了主机开发中更直接的处理方式。

关于 `VK_EXT_descriptor_heap` 的关键点包括：
* **行业认可：** 历经三年开发，汇集了全行业的重大投入，以确保跨厂商的可移植性。
* **发布策略：** 目前作为 `EXT`（扩展）发布，以便收集社区反馈并进行改进。工作组计划在接下来的九个月内吸收这些反馈，随后敲定 `KHR` 版本并最终整合进核心标准。
* **未来路线图：** 这一方法论将应用于 Vulkan API 的其他关键部分，以提升开发者体验并减少碎片化。

这一转变的最终目标是通过为最复杂的系统提供推倒重来的契机，使 Vulkan 变得更加直观且“让人乐于使用”。

---

## 2. 数学家们对复数的本质结构存在分歧。

**原文标题**: Mathematicians disagree on the essential structure of the complex numbers

**原文链接**: [https://www.infinitelymore.xyz/p/complex-numbers-essential-structure](https://www.infinitelymore.xyz/p/complex-numbers-essential-structure)

在这篇文章中，乔尔·大卫·汉金斯（Joel David Hamkins）探讨了关于复数（$\mathbb{C}$）“本质结构”的哲学与数学分歧。他指出，通常被视为单一数学对象的复数，实际上是通过几种截然不同且不等价的结构概念来审视的，每种概念都由其对称程度及其自同构群所定义。

汉金斯识别出四种主要视角，并将其归纳为三种不同的结构类型：

1. **分析与平滑视角：** 这些观点将 $\mathbb{C}$ 视为实数域 $\mathbb{R}$ 上的域或拓扑域。汉金斯认为两者是等价的，因为其拓扑性质与实数子域是可以相互定义的。这种结构仅承认“复共轭”为唯一的非平凡对称，这意味着 $i$ 与 $-i$ 在代数上是不可辨识的。
2. **刚性视角（复平面）：** 这种观点引入了完整的坐标结构（实部与虚部），或将虚数单位 $i$ 固定为常数。这消除了 $i$ 与 $-i$ 之间的对称性，从而形成了一个没有任何非平凡自同构的刚性结构。
3. **代数视角：** 这种观点纯粹将 $\mathbb{C}$ 视为一个域。它被定义为特征为零且基数为连续统的唯一代数闭域。这一概念具有最强的对称性，允许在简单的共轭之外存在大量“野性”自同构。

汉金斯总结道，这些差异不仅是教学上的，还代表了不同的数学承诺。视角的选择决定了人们认为 $i$ 的身份是固定的还是对称的，这与**结构主义**哲学有着深刻的关联。文章最终指出，复数并不存在单一的“本质”结构，因为不同的数学语境会侧重于不同的结构特征。

---

## 3. 基于 Quake 1 引擎的《半条命 2》净室实现

**原文标题**: Clean-room implementation of Half-Life 2 on the Quake 1 engine

**原文链接**: [https://code.idtech.space/fn/hl2](https://code.idtech.space/fn/hl2)

提供的文本并不包含关于“在 Quake 1 引擎上以净室方式实现《半条命 2》”的信息。相反，该内容是一则来自名为 **Anubis** 的安全系统的通知，旨在保护网站免受 AI 爬虫的侵害。

核心要点如下：

*   **目的：** 网站使用 Anubis 来防止 AI 公司恶意抓取数据，这种行为经常导致服务器宕机并使人类用户无法访问资源。
*   **机制：** Anubis 采用了类似于 Hashcash 的**工作量证明 (PoW)** 方案。虽然单个用户的计算负载微不足道，但对于大规模爬虫而言，其成本将变得极其高昂。
*   **未来目标：** 该系统是一个临时方案。开发人员正致力于研究更先进的“指纹识别”技术（如分析字体渲染），以便在不干扰合法用户的情况下识别自动化“无头”浏览器。
*   **

总之，这段内容是对读者为何被机器人防护网关拦截或质询的技术解释，而非文章本身。

---

## 4. 奇点将发生在一个星期二。

**原文标题**: The Singularity will occur on a Tuesday

**原文链接**: [https://campedersen.com/singularity](https://campedersen.com/singularity)

本文通过双曲模型提出了一种对 AI “奇点”的数据驱动预测。与仅在 $t = \infty$ 时达到无穷大的指数增长不同，双曲模型识别出一个“极点”——即数学逻辑失效的一个有限时间点。

作者分析了五个指标：MMLU 分数、单位美元代币量、发布间隔、arXiv 上关于“涌现”的论文以及 Copilot 代码份额。分析揭示了一个惊人的差异：虽然技术能力指标（如模型性能和成本）目前正以**线性**速度提高，但以涌现行为研究论文频率衡量的人类注意力，正在以**双曲**速度加速。

**核心发现包括：**
*   **奇点在于人类：** 只有 arXiv 上的“涌现”论文指标显示出真正的双曲曲线。这表明奇点并非机器智能的垂直飙升，而是一个“社会奇点”，即 AI 带来的冲击速度超过了人类处理或治理它们的能力。
*   **一个具体日期：** 模型确定了 2034 年的某个星期二，作为当前轨迹变得难以为继的时间点。
*   **先发制人的影响：** 作者认为社会结构已经开始瓦解。我们正目睹劳动力市场中的“预防性”取代、制度在监管方面的滞后、极端的资本集中以及心理困扰（FOBO：担心被时代淘汰的恐惧）。

最终，文章得出结论：虽然机器在稳步提升，但人类的歇斯底里和制度崩溃才是真正“走向垂直”的因素。奇点并非未来的物理事件，而是对人类集体决策在加速的技术变革压力下崩溃时刻的描述——作者声称这一过程在 2026 年便已全面开启。

---

## 5. 谷歌向ICE移交学生记者的银行及信用卡号

**原文标题**: Google Handed ICE Student Journalist's Bank and Credit Card Numbers

**原文链接**: [https://theintercept.com/2026/02/10/google-ice-subpoena-student-journalist/](https://theintercept.com/2026/02/10/google-ice-subpoena-student-journalist/)

根据《拦截》（The Intercept）的一项调查，谷歌向美国移民及海关执法局（ICE）提供了属于英国学生运动人士兼记者阿曼德拉·托马斯-约翰逊（Amandla Thomas-Johnson）的大量个人数据。虽然此前已知谷歌曾与国土安全部共享元数据，但一份新披露的传票显示，该公司还移交了托马斯-约翰逊的银行账号、信用卡号、地址以及IP掩码信息。

此次监控始于托马斯-约翰逊在2024年短暂参与康奈尔大学的一次挺巴勒斯坦抗议活动。在特朗普政府发布针对学生抗议者的行政命令后，托马斯-约翰逊转入藏匿状态，并最终逃往塞内加尔以躲避可能的拘留。此案的一个关键争议点在于，谷歌在未事先通知托马斯-约翰逊的情况下便配合了ICE的传票，剥夺了他依法对数据披露提出抗辩的机会。

作为回应，电子前沿基金会（EFF）和北加州美国公民自由联盟（ACLU）向包括谷歌、Meta和亚马逊在内的主要科技公司发出正式信函，敦促它们抵制缺乏法院干预的国土安全部传票。这些团体呼吁相关公司在配合要求前通知用户，并反击那些阻碍透明度的禁言令。

法律专家表示，此案凸显了大型科技公司与国家权力之间合作日益加深，这一转变令人担忧。尽管谷歌的公开政策声称公司会“回绝”过度宽泛的请求，但数据显示，谷歌绝大多数情况下都会配合政府要求，且此类要求在近年来激增。民权倡导者目前正呼吁对《存储通信法》进行立法改革，以确立政府访问数字数据的更高标准，保护个人免受不受约束的国家监控。

---

## 6. Show HN: 我制作了 paperboat.website，一个面向朋友与创造力的平台。

**原文标题**: Show HN: I made paperboat.website, a platform for friends and creativity

**原文链接**: [https://paperboat.website/home/](https://paperboat.website/home/)

**paperboat.website** 是一个极简、无干扰的平台，专为创建简单的个人网站和博客而设计。该服务由德国莱比锡的 Marv 开发，旨在通过提供一个无广告、无追踪的空间，为现代互联网提供一种友好的替代方案。

**核心特点：**
*   **简约与性能：** 平台无需 JavaScript，支持全键盘操作，并兼容富文本和 Markdown 编辑。
*   **互联互通：** 用户可以关注平台上的其他博客，并获取每个站点的 RSS 订阅源。
*   **易用性：** 专注于轻量化设计，确保所有用户都能轻松导航。

**支持与高级权益：**
虽然基础服务允许用户立即开始分享故事，但通过 5 欧元的“维持小船航行”捐助，可以解锁以下增强功能：
*   创建多达 10 个独立站点。
*   获得 3 个免费的好友邀请名额。
*   支持上传图片和音频文件。
*   支持使用自定义域名和个性化配色方案。

总的来说，paperboat.website 被定位为一个“轻量且友好”的数字溪流，用于承载个人故事、项目和创意表达，彻底摆脱了传统社交媒体的杂乱感和复杂建站工具的繁琐。

---

## 7. Parse, Don't Validate (2019)

**原文标题**: Parse, Don't Validate (2019)

**原文链接**: [https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)

In "Parse, Don't Validate," the author outlines a core philosophy of type-driven design: software should be structured to transform less-structured data into more-structured data, rather than simply checking properties of the data and throwing the results away.

The central argument is that **validation** is often a "leaky" process. When we validate an input (e.g., checking if a list is non-empty) and return a simple boolean or unit type, we force subsequent code to re-verify those same properties or handle "impossible" error cases. This leads to redundant checks, potential performance hits, and "shotgun parsing"—a dangerous antipattern where validation logic is scattered throughout the program, increasing the risk of bugs and security vulnerabilities.

By contrast, **parsing** preserves the information gained during the check. For example, instead of validating that a list is non-empty and then using a partial function to get its first element, a developer should parse the list into a `NonEmpty` type. This "strengthens" the argument type, ensuring that the rest of the program can safely operate on the data without further checks.

Key benefits of this approach include:
*   **Total Functions:** It turns partial functions (which can crash) into total functions (which are guaranteed to return a result).
*   **Compile-time Safety:** If validation logic changes at the system boundary, the type system will force updates throughout the program, preventing runtime errors.
*   **Preservation of Knowledge:** It encodes "proofs" about the data directly into the types.

Ultimately, parsing allows developers to discharge checks at the boundaries of an application, leading to cleaner, more robust, and more maintainable code.

---

## 8. Oxide raises $200M Series C

**原文标题**: Oxide raises $200M Series C

**原文链接**: [https://oxide.computer/blog/our-200m-series-c](https://oxide.computer/blog/our-200m-series-c)

生成摘要时出错

---

## 9. Show HN: I built a macOS tool for network engineers – it's called NetViews

**原文标题**: Show HN: I built a macOS tool for network engineers – it's called NetViews

**原文链接**: [https://www.netviews.app](https://www.netviews.app)

生成摘要时出错

---

## 10. Qwen-Image-2.0: Professional infographics, exquisite photorealism

**原文标题**: Qwen-Image-2.0: Professional infographics, exquisite photorealism

**原文链接**: [https://qwen.ai/blog?id=qwen-image-2.0](https://qwen.ai/blog?id=qwen-image-2.0)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 2 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 3 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 4 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 5 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 6 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 7 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 8 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 9 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 10 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 11 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 12 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 13 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 14 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 15 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 16 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 17 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 18 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 19 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 20 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 21 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 22 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 23 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 24 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 25 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 26 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 27 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 28 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 29 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 30 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 31 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 32 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 33 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 34 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 35 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 36 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 37 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 38 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 39 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 40 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 41 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 42 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 43 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 44 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 45 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 46 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 47 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 48 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 49 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 50 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 51 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 52 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 53 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 54 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 55 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 56 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 57 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 58 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 59 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 60 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 61 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 62 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 63 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 64 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 65 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 66 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 67 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 68 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 69 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 70 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 71 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 72 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 73 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 74 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 75 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 76 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 77 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 78 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 79 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 80 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 81 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 82 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 83 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 84 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 85 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 86 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 87 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 88 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 89 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 90 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 91 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 92 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 93 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 94 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 95 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 96 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 97 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 98 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 99 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 100 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 101 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 102 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 103 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 104 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 105 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 106 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 107 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 108 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 109 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 110 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 111 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 112 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 113 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 114 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 115 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 116 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 117 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 118 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 119 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 120 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 121 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 122 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 123 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 124 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 125 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 126 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 127 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 128 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 129 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 130 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 131 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 132 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 133 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 134 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 135 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 136 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 137 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 138 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 139 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 140 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 141 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 142 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 143 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 144 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 145 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 146 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 147 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 148 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 149 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 150 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 151 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 152 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 153 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 154 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 155 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 156 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 157 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 158 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 159 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 160 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 161 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 162 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 163 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 164 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 165 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 166 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 167 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 168 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 169 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 170 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 171 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 172 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 173 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 174 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 175 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 176 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 177 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 178 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 179 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 180 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 181 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 182 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 183 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 184 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 185 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 186 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 187 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 188 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 189 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 190 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 191 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 192 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 193 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 194 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 195 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 196 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 197 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 198 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 199 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 200 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 201 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 202 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 203 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 204 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 205 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 206 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 207 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 208 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 209 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 210 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 211 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 212 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 213 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 214 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 215 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 216 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 217 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 218 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 219 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 220 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 221 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 222 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 223 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 224 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 225 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 226 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 227 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 228 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 229 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 230 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 231 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 232 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 233 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 234 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 235 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 236 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 237 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 238 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 239 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 240 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 241 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 242 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 243 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 244 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 245 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 246 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 247 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 248 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 249 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 250 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 251 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 252 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 253 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 254 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 255 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 256 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 257 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 258 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 259 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 260 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 261 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 262 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 263 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 264 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 265 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 266 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 267 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 268 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 269 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 270 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 271 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 272 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 273 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 274 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 275 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 276 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 277 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 278 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 279 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 280 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 281 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 282 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 283 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 284 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 285 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 286 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 287 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 288 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 289 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 290 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 291 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 292 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 293 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 294 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 295 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 296 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 297 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 298 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 299 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 300 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 301 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 302 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 303 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 304 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 305 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 306 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 307 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 308 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 309 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 310 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 311 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 312 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 313 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 314 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 315 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 316 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 317 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 318 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 319 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 320 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 321 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 322 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 323 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 324 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 325 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 326 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 327 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
