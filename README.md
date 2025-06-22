# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-06-22.md)

*最后自动更新时间: 2025-06-22 17:49:45*
## 1. 机械手表：分解图

**原文标题**: Mechanical Watch: Exploded View

**原文链接**: [https://fellerts.no/projects/epoch.html](https://fellerts.no/projects/epoch.html)

本文详细介绍了作者受Bartosz Ciechanowski博客中的互动插图启发，创建机械手表机芯实体爆炸图模型的历程。由于缺乏现成模型，作者在缺乏专业知识的情况下，决定亲自构建一个。

该过程始于探索不同的手表机芯类型，并因怀表机芯的组件较大而选择相对简单的怀表机芯。最初的方法是分层树脂浇注，但由于可见的接缝、凌乱的应用和气泡的形成，结果并不理想。放弃分层浇注后，作者转而使用鱼线将每个组件单独悬挂在单个树脂浇注体中。

作者试验了各种树脂、用于去除气泡的真空泵和用于组装的CA胶，模仿了制表技术。1号原型展示了鱼线的最小可见性，但也揭示了圆柱形铸件的不适用性。2号原型引入了一个结构化的流程：拆卸、清洁、齿轮系组装以及逐步的组件悬挂。表盘侧的组装方式类似，并创建了一个用于树脂浇注的模具。

2号原型面临的挑战包括子组件的连接和因过热导致的树脂收缩。为了解决这些问题，3号原型采用了剪刀式升降实验台，用于精确的组件放置，并用磁铁固定螺丝。目标是创建一个视觉上清晰且准确的爆炸图模型，并克服沿途的技术障碍。

---

## 2. Git Notes：Git最酷，却最不受待见的特性 (2022)

**原文标题**: Git Notes: Git's coolest, most unloved­ feature (2022)

**原文链接**: [https://tylercipriani.com/blog/2022/11/19/git-notes-gits-coolest-most-unloved-feature/](https://tylercipriani.com/blog/2022/11/19/git-notes-gits-coolest-most-unloved-feature/)

本文探讨了Git Notes，它是Git一项强大但经常被忽视的功能，允许用户将元数据附加到Git对象（如提交、blob和树）上，而无需修改对象本身。Git Notes可用于跟踪代码审查状态、测试结果、提交花费的时间或邮件列表上的讨论等信息。

文章重点介绍了实际用例，包括Git项目本身使用Notes将提交链接到邮件列表讨论，以及Gerrit的`reviewnotes`插件，该插件允许开发人员直接在Git log中查看代码审查信息。它还提到了`git-appraise`，这是一个基于Git Notes构建的完全分布式的代码审查系统。

尽管Git Notes具有潜力，但其可用性较差且采用率有限。GitHub已于2014年停止显示提交Notes。作者指出，处理blob或树的Notes需要深入研究Git的底层机制，这使得许多用户无法使用它们。

尽管存在挑战，但作者认为Git Notes提供了一条通往forge独立性的道路，它能够将项目历史记录和元数据与代码本身一起分发，而无需依赖GitHub或GitLab等平台。他总结说，如果Git Notes更易于使用，它们就可以开启一种更加分布式和协作的软件开发方法。

---

## 3. LibRedirect - 将热门网站重定向到注重隐私的替代前端

**原文标题**: LibRedirect – Redirects popular sites to alternative privacy-friendly frontends

**原文链接**: [https://libredirect.github.io](https://libredirect.github.io)

LibRedirect：一款通过将流量从热门网站重定向到注重隐私的替代前端来增强用户隐私的网络浏览器扩展。它支持各种平台，包括YouTube、Instagram、Reddit、TikTok、Twitter等等。

该扩展程序将官方网站替换为尊重隐私的替代方案。例如，YouTube被重定向到像Invidious、Piped或FreeTube这样的前端；Twitter转到Nitter；Reddit到Libreddit或Teddit；Instagram到Proxigram。这些替代前端通常会去除跟踪器、最大限度地减少数据收集，并提供更清洁、更私密的浏览体验。

LibRedirect涵盖了广泛的网站，包括视频、社交媒体、音乐、内容共享、代码托管、参考资料、翻译等平台。其目标是通过使用这些替代服务，为用户提供对其数据和在线隐私的更大控制权。该扩展程序可供下载，用户可以在LibRedirect网站上找到源代码、联系方式、常见问题解答、文档和捐赠链接。

---

## 4. 展示HN：用人工智能举报纽约市怠速车辆（并获得罚款分成）

**原文标题**: Show HN: Report idling vehicles in NYC (and get a cut of the fines) with AI

**原文链接**: [https://apps.apple.com/us/app/idle-reporter-for-nyc-dep/id6747315971](https://apps.apple.com/us/app/idle-reporter-for-nyc-dep/id6747315971)

闲置车辆举报器是一款iPhone应用程序，旨在简化在纽约市举报闲置商用车辆的过程，并有可能获得部分罚款。该应用程序旨在尽可能地加快举报过程，声称可以在五分钟内完成。

主要功能包括：

*   **时间戳相机：** 记录带有日期、时间和位置叠加的视频，并显示剩余录制时间。
*   **AI驱动的表格填写（需要订阅）：** 使用人工智能自动填写投诉表格，无需手动数据录入。
*   **手动编辑器：** 提供手动填写报告表格的方式。
*   **截图生成器：** 自动从视频中提取车牌和车主信息的屏幕截图。
*   **状态追踪器：** 允许用户追踪其提交报告的状态。

该应用程序可免费下载，但提供应用内购买以使用AI驱动的表格填写功能，提供每周、每月和每年订阅选项。开发者Proof by Induction LLC强调该应用程序是一个非官方实用程序，用户应对其报告的准确性负责。该应用程序支持iOS、macOS（Apple M1芯片或更高版本）和visionOS。根据列出的隐私惯例，该应用程序不收集任何用户数据。

---

## 5. 文学小说的文化衰落

**原文标题**: The Cultural Decline of Literary Fiction

**原文链接**: [https://oyyy.substack.com/p/the-cultural-decline-of-literary](https://oyyy.substack.com/p/the-cultural-decline-of-literary)

无法访问文章链接。

---

## 6. TPU深度解析

**原文标题**: TPU Deep Dive

**原文链接**: [https://henryhmko.github.io/posts/tpu/tpu.html](https://henryhmko.github.io/posts/tpu/tpu.html)

本文深入探讨谷歌张量处理器（TPU）的架构和设计理念，并将其与GPU进行对比。TPU通过软硬件协同设计，利用脉动阵列和提前编译（AoT），优先考虑可扩展性、能源效率和高矩阵乘法吞吐量。

以芯片级别（例如TPUv4）为例，TPU具有两个TensorCore，每个TensorCore包含一个矩阵乘法单元（MXU）、向量单元（VPU）和专用内存缓冲区（VMEM、SMEM）。与拥有大量较小内核和广泛缓存的GPU不同，TPU具有更大的片上内存和更小的HBM，强调通过脉动阵列实现高效的数据流。

设计理念围绕用于高效矩阵运算的脉动阵列以及通过XLA编译器进行AoT编译，以最大限度地减少能量密集型缓存访问。XLA预先分析计算图，从而实现优化的无缓存执行。这与GPU的灵活性形成对比。

TPU通过多芯片配置实现可扩展性。托盘（板）包含4个芯片，机架由64个芯片组成，排列在3D环形网络中，超级集群（完整集群）包含数千个芯片（例如，TPUv4中的4096个，TPUv7中的9216个）。光路交换（OCS）连接机架，从而实现环绕通信，并创建非连续的TPU切片（集群的子集），从而提高运营稳定性和资源分配的灵活性。可以配置不同的切片拓扑（立方体、雪茄形、矩形），以优化不同并行策略（数据、张量、流水线）的性能。

---

## 7. 如何协商你的薪酬待遇

**原文标题**: How to negotiate your salary package

**原文链接**: [https://www.complexsystemspodcast.com/episodes/how-to-negotiate-your-salary-package/](https://www.complexsystemspodcast.com/episodes/how-to-negotiate-your-salary-package/)

本文为薪资谈判提供了一份全面的指南，主要面向不擅长此过程的工程师和技术专业人员。文章强调薪资谈判至关重要，会对长期收入和职业发展轨迹产生重大影响。

作者认为，人们往往对谈判抱有消极心态，认为其令人厌恶或不必要，这在职业领域是不利的。文章鼓励读者转变视角，认识到谈判是成功人士的常见做法。

要点包括：

*   **谈判至关重要：** 薪资上的微小差异会随着时间的推移而累积，从而带来可观的经济收益。
*   **心态转变：** 通过了解谈判的重要性并将其作为一项技能来接受，克服对谈判的不适感。
*   **雇主的角度：** 认识到公司从完全负担的成本（工资、福利、税收）来看待员工，这使得较小的工资增长对他们来说意义不大。
*   **研究的重要性：** 收集可比薪资的数据，以加强您的谈判地位。
*   **不要先出价：** 让公司先出价。

总而言之，本文鼓励专业人士积极进行薪资谈判，揭穿常见的误解，并提供一个框架，以便以信心和战略意识来处理这一过程。

---

## 8. 分配器是拿着打字机的猴子

**原文标题**: Allocators Are Monkeys with Typewriters

**原文链接**: [https://tgmatos.github.io/allocators-are-for-monkeys-with-typewriters/](https://tgmatos.github.io/allocators-are-for-monkeys-with-typewriters/)

本文探讨如何创建一个简单的内存分配器，该分配器管理一个预先分配的内存区域，其灵感来源于 Microsoft 的 mimalloc 中的一个限制。作者幽默地表示，即使专业知识有限，构建一个基本的分配器也是可以实现的，因此有了这个标题。

核心概念围绕着理解分配器在分配、释放和重新分配内存方面的作用，模仿标准 C 库函数（如 `malloc`、`free` 和 `resize`）的功能。分配器需要解决的一个关键挑战是内存碎片，包括内部碎片（已分配块内的浪费空间）和外部碎片（分散在内存中的小的、无法使用的空闲块）。

本文重点介绍如何实现一个“伙伴系统”分配器，这是一种相对简单且可靠的方法，也被 Linux 内核所采用。该系统的工作原理是递归地将一个连续的内存块分成两半（伙伴），直到找到适合请求分配的大小。虽然有效，但这种方法可能会导致内部碎片。

作者通过一个示例解释了伙伴系统中的分配和释放，说明了内存是如何分割和合并的。`resize` 函数留给读者作为练习。作者对分配器的相对简单性感到惊讶，即使是像 mimalloc 这样复杂的分配器，作者也认为其复杂性主要归功于多线程管理。

最终，作者的目标是为 mimalloc 贡献一个允许它使用预先分配的内存的功能，并计划在未来更深入地研究分配器的内部结构。作者实现的的代码可在 GitHub 上找到。

---

## 9. 玻璃的低温增材制造

**原文标题**: Low-Temperature Additive Manufacturing of Glass

**原文链接**: [https://www.ll.mit.edu/research-and-development/advanced-technology/microsystems-prototyping-foundry/low-temperature](https://www.ll.mit.edu/research-and-development/advanced-technology/microsystems-prototyping-foundry/low-temperature)

本文重点介绍了林肯实验室在玻璃低温增材制造（3D打印）方面的创新方法，与传统方法相比，这是一项重大进步。他们的技术无需超过1000°C的温度，仅需250°C即可固化玻璃结构，该技术采用定制工程墨水，由硅酸盐溶液和无机纳米颗粒组成。

该工艺的核心是直接墨水书写，可以通过修改墨水的成分，实现具有定制光学、化学和电气特性的复杂玻璃结构的精确逐层构建。这种低温方法克服了传统玻璃3D打印的局限性，传统玻璃3D打印存在成本高、需要专用设备以及与温度敏感材料不兼容等问题。

本文强调了这种方法的优势，包括使用容易获得的墨水成分、设计中的几何自由度以及创建稳定的玻璃结构。通过解决传统3D打印中使用的塑料和金属复合材料固有的不稳定性问题，林肯实验室的玻璃结构展示了高分辨率、热稳定性和最小收缩率。潜在的应用包括微流体系统、自由曲面光学透镜、光纤和高温电子元件。目前的研究重点是通过墨水开发来提高光学清晰度并扩大可实现的化学和电气特性范围。

---

## 10. 纯粹形式之声：受Supercollider、APL和Forth启发的音乐语言

**原文标题**: Sound As Pure Form: Music Language Inspired by Supercollider, APL, and Forth

**原文链接**: [https://github.com/lfnoise/sapf](https://github.com/lfnoise/sapf)

纯粹形式之声 (sapf) 是一种类似 Forth 的、基于堆栈的编程语言，专为音频合成和处理而设计，灵感来源于 SuperCollider、APL 和 Forth。它强调函数式方法，使用惰性的、潜在无限的序列来处理音频和控制事件，类似于 APL 的数组运算。该语言旨在通过自动映射、扫描和归约运算符来实现简洁的表达能力，从而最大限度地减少对显式循环的需求。

主要功能包括：

*   **连接式风格：** 函数组合即连接，自然管道化，以及从左到右的函数应用。
*   **极简语法：** 后缀表示法减少了语法开销。
*   **数据类型：** 实数、字符串、列表（流和信号）、形式（具有继承的字典）、函数和可变引用（Refs）。
*   **自动映射：** 内置运算符自动映射到列表上，无需手动迭代即可对整个结构进行操作。
*   **"Each" 运算符：** `@` 运算符允许函数对嵌套列表中的单个元素进行操作。
*   **形式：** 字典可以从一个或多个其他形式继承。
*   **安装：** 该文档提供了有关安装和设置环境变量的指导，包括采样率和序言文件的选项。

该文档还包括语法和用法的详细示例，包括注释、数字、字符串、单词、引号、函数、列表、形式和自动映射，以帮助用户开始使用 sapf。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 2 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 3 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 4 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 5 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 6 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 7 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 8 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 9 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 10 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 11 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 12 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 13 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 14 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 15 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 16 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 17 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 18 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 19 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 20 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 21 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 22 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 23 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 24 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 25 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 26 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 27 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 28 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 29 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 30 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 31 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 32 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 33 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 34 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 35 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 36 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 37 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 38 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 39 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 40 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 41 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 42 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 43 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 44 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 45 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 46 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 47 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 48 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 49 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 50 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 51 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 52 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 53 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 54 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 55 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 56 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 57 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 58 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 59 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 60 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 61 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 62 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 63 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 64 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 65 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 66 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 67 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 68 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 69 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 70 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 71 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 72 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 73 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 74 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 75 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 76 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 77 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 78 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 79 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 80 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 81 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 82 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 83 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 84 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 85 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 86 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 87 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 88 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 89 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 90 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 91 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 92 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 93 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 94 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 95 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
