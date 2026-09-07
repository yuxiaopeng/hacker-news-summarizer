# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-09-07.md)

*最后自动更新时间: 2026-09-07 20:47:58*
## 1. 见证洛杉矶一栋接一栋地建成 (1880–2026)

**原文标题**: Watch Los Angeles get built, one building at a time (1880–2026)

**原文链接**: [https://lax-skyline.parcelscope.net/](https://lax-skyline.parcelscope.net/)

**Parcelscope 洛杉矶**是一款交互式数据可视化工具，展示了从 1880 年到 2026 年洛杉矶建筑的演变过程。该项目利用 LARIAC 2020 的建筑轮廓及洛杉矶县估价官办公室的数据，全面且按时间顺序呈现了这座城市的发展历程。

该工具将城市中的每座建筑表现为一个 3D 长方体，并根据其建造年代进行颜色编码。这让用户能够“目睹”城市在近 150 年间的填充过程，见证其从 19 世纪末的稀疏景观转变为今日的高密度大都市。

界面提供的主要功能和信息包括：
*   **年代增长：** 展示从 1880 年至今建设进程的时间轴。
*   **详细指标：** 单体建筑的数据，包括建造年份、总高度、占地面积和建筑类型。
*   **交互式导航：** 用户可以平移、缩放和倾斜地图以探索城市天际线。
*   **视觉辅助：** 在较宽的缩放级别下，建筑高度会被适当拉伸，以帮助用户在广阔的洛杉矶盆地中区分低层和高层建筑。

最终，该项目作为城市扩张与密度的数字记录，生动地展示了在过去的一个半世纪里，洛杉矶是如何通过一座座建筑的更迭而发生蜕变的。

---

## 2. 随机梯度方法 (2024)

**原文标题**: Methods for Random Gradients (2024)

**原文链接**: [https://justinjay.wang/methods-for-random-gradients/](https://justinjay.wang/methods-for-random-gradients/)

在《随机渐变的方法》（2024）一文中，作者回顾了用于塑造 OpenAI 视觉形象的渐变生成技术的演变。文章详细介绍了三种主要方法：

**1. 高度图渐变**
该方法使用 Processing 开发，利用平滑的柏林噪声创建“高度图”（0 到 1 之间的数值网格）。通过将随机颜色刻度映射到这些数值，作者创作出了具有有机感且引人注目的渐变效果。虽然在美学上令人愉悦，但这种方法最终被认为不适合 OpenAI 的正式品牌视觉。

**2. 分层径向渐变 (SVG)**
为了取代静态、低分辨率的图像，作者开发了一套使用可缩放矢量图形 (SVG) 的动态系统。通过叠加多个 `<radialGradient>` 元素并随机化其焦点、缩放和旋转，该系统在 2020 年至 2022 年间为 OpenAI 官网的每位访问者提供了一个独特且轻量（6 KB）的渐变效果。这种方法将高性能与无限的可扩展性结合在了一起。

**3. AI 生成渐变**
DALL·E 2 等生成式模型的出现引入了一种“老虎机”式的设计方法。通过使用特定的提示词——如“梦幻氛围”、“花卉的宏观摄影”或“日落天空”——作者可以生成具有质感和氛围感的渐变，这些效果既不可预测又充满创意。

文章总结道，早期的设计方法侧重于程序化控制和性能，而现代 AI 工具则为视觉实验开辟了广阔的新前沿，使设计师的角色从精准的执行者转变为创意的引导者。

---

## 3. Finding a bug in Dummit and Foote's Abstract Algebra

**原文标题**: Finding a bug in Dummit and Foote's Abstract Algebra

**原文链接**: [https://kallus.org/blog/dummit_and_foote.html](https://kallus.org/blog/dummit_and_foote.html)

生成摘要时出错

---

## 4. 未来天气 3

**原文标题**: WeatherNext 3

**原文链接**: [https://deepmind.google/science/weathernext/](https://deepmind.google/science/weathernext/)

WeatherNext 3 通过利用原始卫星图像生成逐小时预报，引入了一种全新的气象学方法。与以往模型不同，这种直接的数据集成实现了更频繁的更新，使用户能够精准追踪雨雪等快速变化的天气状况。

---

## 5. 简单并不渺小

**原文标题**: Simple Is Not Small

**原文链接**: [https://jyn.dev/simple-is-not-the-same-as-small/](https://jyn.dev/simple-is-not-the-same-as-small/)

在《简单并非精简》（Simple Is Not Small）一文中，作者指出开发者经常误将简洁（精简）视为简单。借鉴 Rich Hickey 的定义，文章将**简单**（Simplicity）定义为“解耦”（sim-plex：单辫），而将**复杂**（Complexity）定义为“耦合”（com-plex：多辫）。

作者以 Unix 管道为例，说明了一个“精简但耦合”的系统。虽然统计词频的 Unix 命令非常简短，但它与特定的数据格式和行为耦合（例如，`uniq` 要求输入必须是已排序的）。这种耦合使得一些简单的修改——例如保持单词的原始顺序——在 Bash 中变得异常困难且代码“丑陋”，而相比之下，在 Clojure 等语言中则更易实现。Clojure 通过将数据表示与类型检查解耦来实现简单，从而兼具了记录的结构性和映射（map）的灵活性。

核心观点包括：
*   **精简 vs. 简单**：精简通常是对资源受限（如开发时间或硬件）的反应，而简单则是一种优先考虑解耦的设计选择。
*   **简单的代价**：构建真正解耦的系统（如 SQL 或 CSS）往往需要巨大的工程投入——作者称之为“硬着头皮编写攻克难题”。
*   **用户体验**：庞大的程序（如 Google Drive）在用户看来可能很简单，因为它们在处理复杂的后台任务时，没有将这些复杂性与用户界面耦合。

最终，作者鼓励开发者优先考虑简单而非精简。即便程序体积更大，简单的代码也更容易维护且更具灵活性。复杂性并非源自代码行数，而是源自各部分之间隐藏的依赖关系。

---

## 6. Decoding the NEC V20 Microcode

**原文标题**: Decoding the NEC V20 Microcode

**原文链接**: [https://martypc.blogspot.com/2026/09/decoding-nec-v20-microcode.html](https://martypc.blogspot.com/2026/09/decoding-nec-v20-microcode.html)

生成摘要时出错

---

## 7. 加州理工数学马拉松 —— 史上首个致力于研究级数学的黑客松

**原文标题**: Caltech Mathathon – first hackathon ever devoted to research level mathematics

**原文链接**: [https://mathathonchallenge.com/index.html](https://mathathonchallenge.com/index.html)

**加州理工数学马拉松**

加州理工数学马拉松（Caltech Mathathon）定于10月30日至11月1日在加州理工学院举行，是全球首个致力于研究级数学的黑客松。在40小时的时间里，100支入选团队将利用总额超过200万美元AI算力额度支持的前沿AI模型，致力于攻克开放数学猜想并开发新的数学理论。

此次活动源于近期该领域一系列由AI主导的突破性进展，例如2026年对埃尔德什（Erdős）平面单位距离猜想的证伪。组织者旨在探索两个核心问题：AI能在多大程度上加速从灵感构思到同行评审发表的过程，以及当AI能够高速解决猜想时，数学家的角色将如何转变。

参赛者须向由顶尖数学家组成的评审团答辩其研究发现，评审团将评估他们对问题的理解以及成果的质量。比赛设有两级奖金制度：
1. **即时奖**：授予活动现场最具潜力且阐述最清晰的成果。
2. **第二轮奖项**：在更广泛的数学界有足够时间对发现进行正式验证后颁发。

通过汇聚全球顶尖人才，数学马拉松旨在定义纯数学领域人类智慧与人工智能协同研究的未来。

---

## 8. bzip3

**原文标题**: bzip3

**原文链接**: [https://github.com/iczelia/bzip3](https://github.com/iczelia/bzip3)

**bzip3** 是一款高性能压缩工具，被设计为 bzip2 的“精神续作”。它由 Kamila Szewczyk 开发，通过结合 0 阶上下文混合熵编码、Burrows-Wheeler 变换（通过 libsais 库）以及 LZP（Lempel-Ziv+Prediction）预处理阶段，提供了卓越的压缩率和速度。它特别针对文本和源代码进行了优化。

**关键性能指标：**
针对 Perl 5 源代码完整历史记录的基准测试证明了 bzip3 的高效性。在这些测试中，bzip3 的压缩率显著优于 LZMA (xz)、bzip2 和 Zstandard。例如，在使用 511MB 分块大小时，bzip3 将数据集压缩至约 546MB，而 LZMA 和 Zstandard 生成的文件大小分别为 2GB 和 3GB。当配合 `lrzip` 进行长距离去重时，文件大小进一步降至约 60MB。其解压速度也极具竞争力，通常超过 bzip2 并可与 Zstandard 媲美。

**技术细节与兼容性：**
*   **安装：** 可通过 autotools 从源码构建，或通过 macOS 上的 Homebrew 等包管理器进行安装。
*   **兼容性：** 支持广泛的架构，包括 x86、ARM、PowerPC、MIPS 和 s390x。
*   **许可协议：** 项目采用 LGPLv3 协议授权，同时包含部分采用 Apache 2.0 和 BSD 协议的组件。
*   **可靠性：** 虽然经过广泛测试，但开发者提供了一份免责声明：由于算法的复杂性，用户应意识到存在极小但非零的数据丢失风险。

总之，bzip3 为传统压缩工具提供了一个现代化、高效率的替代方案，特别适合处理大量文本数据并追求高压缩率与快速解压平衡的用户。

---

## 9. Trusting-Trust Attack against an Entire Linux Distribution

**原文标题**: Trusting-Trust Attack against an Entire Linux Distribution

**原文链接**: [https://arxiv.org/abs/2607.24888](https://arxiv.org/abs/2607.24888)

生成摘要时出错

---

## 10. 数据流模型再探

**原文标题**: The Dataflow Model Revisited

**原文链接**: [https://www.vldb.org/pvldb/volumes/19/paper/The%20Dataflow%20Model%20Revisited](https://www.vldb.org/pvldb/volumes/19/paper/The%20Dataflow%20Model%20Revisited)

在《Dataflow 模型再审视》（The Dataflow Model Revisited）中，作者回顾了原始 Dataflow 模型十一年来的历程，评估了其对流处理和批处理领域的影响。虽然论文的核心基础——特别是事件时间的重要性、强一致性以及处理不完整数据的必要性——经受住了时间的考验，但作者也指出了原始愿景中存在的几处不足。

这次回顾强调了对原始模型的三点主要反思：
1. **过度设计**：窗口和触发器过于复杂，迫使用户去处理本应被抽象掉的运维细节。
2. **流表二象性**：作者错失了一个基本事实，即流和表仅仅是相同数据的不同表现形式。
3. **侧重机制**：最初的研究过于关注流处理的底层机制，而未能利用 SQL 和增量视图维护等成熟的数据库概念来隐藏复杂性。

作者指出，业界已转向“快照一致性刷新”和带有明确新鲜度约定的物化视图，这些技术比复杂的水位线（watermarking）机制更受欢迎，因为它们对用户的要求更低。他们认为，“批处理与流处理”之争在很大程度上是语义层面的，而对低延迟处理的需求已沿着传统的 OLTP 和 OLAP 线路发生分化。

最后，论文为该模型提出了一个新的框架——“保留、剔除、加强”（leave in, leave out, push harder），并建议流处理的未来在于它作为一个独立、复杂实体的“消失”。相反，它应当融入更广泛的数据库生态系统中，使分析型流处理的复杂性对终端用户几乎完全不可见。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 2 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 3 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 4 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 5 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 6 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 7 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 8 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 9 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 10 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 11 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 12 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 13 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 14 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 15 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 16 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 17 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 18 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 19 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 20 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 21 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 22 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 23 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 24 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 25 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 26 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 27 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 28 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 29 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 30 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 31 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 32 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 33 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 34 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 35 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 36 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 37 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 38 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 39 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 40 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 41 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 42 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 43 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 44 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 45 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 46 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 47 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 48 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 49 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 50 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 51 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 52 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 53 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 54 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 55 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 56 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 57 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 58 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 59 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 60 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 61 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 62 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 63 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 64 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 65 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 66 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 67 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 68 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 69 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 70 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 71 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 72 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 73 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 74 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 75 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 76 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 77 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 78 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 79 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 80 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 81 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 82 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 83 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 84 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 85 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 86 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 87 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 88 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 89 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 90 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 91 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 92 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 93 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 94 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 95 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 96 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 97 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 98 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 99 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 100 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 101 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 102 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 103 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 104 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 105 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 106 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 107 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 108 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 109 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 110 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 111 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 112 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 113 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 114 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 115 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 116 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 117 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 118 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 119 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 120 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 121 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 122 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 123 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 124 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 125 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 126 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 127 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 128 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 129 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 130 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 131 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 132 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 133 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 134 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 135 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 136 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 137 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 138 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 139 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 140 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 141 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 142 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 143 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 144 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 145 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 146 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 147 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 148 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 149 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 150 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 151 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 152 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 153 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 154 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 155 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 156 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 157 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 158 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 159 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 160 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 161 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 162 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 163 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 164 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 165 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 166 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 167 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 168 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 169 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 170 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 171 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 172 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 173 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 174 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 175 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 176 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 177 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 178 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 179 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 180 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 181 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 182 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 183 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 184 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 185 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 186 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 187 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 188 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 189 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 190 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 191 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 192 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 193 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 194 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 195 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 196 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 197 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 198 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 199 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 200 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 201 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 202 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 203 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 204 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 205 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 206 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 207 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 208 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 209 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 210 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 211 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 212 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 213 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 214 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 215 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 216 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 217 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 218 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 219 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 220 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 221 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 222 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 223 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 224 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 225 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 226 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 227 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 228 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 229 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 230 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 231 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 232 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 233 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 234 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 235 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 236 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 237 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 238 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 239 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 240 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 241 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 242 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 243 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 244 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 245 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 246 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 247 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 248 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 249 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 250 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 251 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 252 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 253 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 254 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 255 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 256 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 257 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 258 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 259 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 260 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 261 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 262 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 263 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 264 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 265 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 266 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 267 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 268 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 269 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 270 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 271 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 272 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 273 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 274 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 275 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 276 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 277 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 278 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 279 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 280 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 281 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 282 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 283 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 284 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 285 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 286 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 287 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 288 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 289 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 290 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 291 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 292 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 293 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 294 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 295 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 296 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 297 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 298 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 299 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 300 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 301 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 302 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 303 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 304 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 305 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 306 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 307 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 308 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 309 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 310 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 311 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 312 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 313 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 314 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 315 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 316 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 317 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 318 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 319 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 320 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 321 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 322 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 323 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 324 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 325 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 326 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 327 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 328 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 329 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 330 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 331 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 332 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 333 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 334 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 335 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 336 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 337 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 338 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 339 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 340 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 341 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 342 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 343 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 344 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 345 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 346 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 347 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 348 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 349 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 350 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 351 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 352 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 353 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 354 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 355 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 356 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 357 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 358 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 359 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 360 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 361 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 362 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 363 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 364 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 365 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 366 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 367 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 368 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 369 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 370 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 371 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 372 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 373 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 374 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 375 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 376 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 377 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 378 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 379 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 380 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 381 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 382 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 383 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 384 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 385 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 386 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 387 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 388 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 389 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 390 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 391 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 392 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 393 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 394 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 395 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 396 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 397 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 398 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 399 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 400 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 401 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 402 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 403 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 404 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 405 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 406 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 407 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 408 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 409 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 410 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 411 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 412 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 413 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 414 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 415 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 416 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 417 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 418 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 419 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 420 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 421 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 422 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 423 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 424 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 425 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 426 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 427 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 428 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 429 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 430 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 431 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 432 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 433 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 434 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 435 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 436 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 437 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 438 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 439 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 440 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 441 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 442 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 443 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 444 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 445 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 446 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 447 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 448 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 449 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 450 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 451 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 452 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 453 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 454 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 455 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 456 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 457 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 458 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 459 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 460 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 461 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 462 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 463 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 464 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 465 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 466 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 467 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 468 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 469 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 470 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 471 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 472 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 473 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 474 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 475 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 476 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 477 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 478 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 479 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 480 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 481 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 482 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 483 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 484 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 485 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 486 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 487 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 488 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 489 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 490 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 491 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 492 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 493 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 494 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 495 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 496 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 497 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 498 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 499 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 500 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 501 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 502 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 503 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 504 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 505 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 506 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 507 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 508 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 509 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 510 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 511 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 512 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 513 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 514 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 515 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 516 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 517 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 518 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 519 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 520 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 521 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 522 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 523 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 524 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 525 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 526 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 527 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 528 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 529 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 530 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 531 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 532 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 533 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 534 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
