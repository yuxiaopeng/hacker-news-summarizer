# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-10-17.md)

*最后自动更新时间: 2026-10-17 19:38:02*
## 1. 7.2 内核开发统计

**原文标题**: Development statistics for the 7.2 kernel

**原文链接**: [https://lwn.net/Articles/1088776/](https://lwn.net/Articles/1088776/)

2026年8月17日发布的 Linux 7.2 内核代表了该项目历史上最活跃的开发周期之一。凭借 16,418 个非合并提交和近 60 万行新代码，它成为有史以来第二忙碌的发布版本。此次开发周期得到了创纪录的 2,652 名开发者的支持，其中包括前所未有的 613 名首次贡献者。

核心贡献者包括在提交总数上领先的 Uwe Kleine-König，以及因处理大量自动化硬件头文件而在“更改行数”类别中位列榜首的 Matthew Stewart。虽然英特尔、谷歌、红帽和 AMD 等传统雇主仍是开发的主要驱动力，但所属机构不明的贡献者数量有了显著增加。

7.2 版本中最具变革性的趋势是大语言模型（LLM）使用的爆炸式增长。与上一版本相比，“Assisted-by”标签增加了近四倍，基于 LLM 的“Sashiko”评审系统被认为发现了数百个漏洞。这种 AI 辅助的涌入导致“Fixes”标签急剧增加，表明 LLM 正在有效识别长期存在的问题。

然而，这一转变引发了社区内部的担忧。数据显示，许多新开发者正在其可能并不完全了解的各个子系统中提交 AI 生成的补丁。内核开发过程中的这一“大规模实验”引发了人们对长期可维护性以及人工评审深度可能下降的质疑。鉴于 7.3 版本已有超过 14,000 项更改在排队中，社区现在必须适应这种没有任何放缓迹象的高速、受 AI 影响的开发环境。

---

## 2. 白化珊瑚与健康邻居接触后数日内即可恢复生机

**原文标题**: Bleached corals thrive within days when touching healthy neighbour

**原文链接**: [https://www.nature.com/articles/d41586-026-03266-x](https://www.nature.com/articles/d41586-026-03266-x)

斯坦福大学的研究人员发现，当白化的珊瑚与来自同一基因个体（genet）的健康片段发生直接物理接触时，可以迅速恢复。这种“愈合之触”为扭转因海水温度升高导致的珊瑚退化提供了一种潜在的新策略。

珊瑚白化发生在热应激导致珊瑚排出其共生藻（虫黄藻，*Symbiodiniaceae*）时，这些藻类为珊瑚提供必要的养分。失去这些藻类后，珊瑚通常会因饥饿而死亡。然而，发表在《科学进展》（*Science Advances*）上的一项研究表明，当细枝鹿角杯形珊瑚（*Pocillopora damicornis*）的白化片段与健康片段接触时，它们会通过建立组织桥融合在一起。这种桥梁使共生藻能够从健康片段转移到白化片段。

该研究的关键发现包括：
*   **快速恢复：** 与健康片段接触的白化珊瑚在八周内即可恢复。到第二周时，其共生体数量每四天翻一番，显著快于野外的自然恢复速度。
*   **独立性：** 仅经过一周的物理接触后，白化片段即便与健康宿主分离，也能继续完全恢复。
*   **遗传特异性：** 融合仅发生在具有相同遗传组成的片段之间。来自不同物种或同物种不同个体的片段无法融合或共享共生体。
*   **分离的后果：** 仅相隔几毫米的白化片段未能恢复，并在20周内死亡。

虽然目前该结果仅在实验室环境下得到证实，但研究人员认为，这可能为修复垂死的珊瑚礁以及对抗气候变化对海洋生态系统的影响提供可扩展的解决方案。

---

## 3. Commodore 64 硬件模拟器：破坏芯片与引脚，观察结果。

**原文标题**: The Commodore 64 hardware simulator: break chips and pins, see the results

**原文链接**: [https://github.com/antirez/c64-hw-simulator](https://github.com/antirez/c64-hw-simulator)

**c64-hw-sim** 是由 "antirez" 设计的一款专门的硬件模拟器，它在引脚级别对 Commodore 64 主板 (ASSY 250407) 进行建模。与旨在运行游戏的标准模拟器不同，该工具模拟了机器真实的电气网表和组件行为。

该模拟器允许用户通过抬起芯片引脚、将引脚短路至地线或电压、从插座中拔出芯片或断开电阻等操作，以交互方式“损坏”硬件。由于它是基于电路逻辑而非预定义的错误画面来计算结果，因此它能真实地展示硬件故障在实际显示器上的表现。

**核心功能与应用场景：**
*   **教育：** 它提供了对 C64 内部结构的深入观察，允许用户在不损坏稀有物理硬件的情况下进行实验。
*   **维修诊断：** 维修人员可以在模拟器上测试假设，将症状与真实的故障 C64 进行匹配，从而帮助他们仅拆焊必要的组件。
*   **技术深度：** 它模拟了浮空网络、信号冲突和电源故障等复杂行为。它集成了 "floooh" 的时钟精确级芯片核心（6510、VIC-II、SID），并使用了源自该主板 KiCad 复制版本的网表。
*   **界面：** 该程序包括主板的可视化呈现、一个监视器、一个控制面板以及用于实时信号分析的示波器。

**性能与限制：**
由于模拟每个引脚的计算强度极大，该程序对计算资源要求很高，即使在 Apple M5 Max 等高端硬件上，运行速度也仅为实时速度的 31% 到 48% 左右。目前它专注于数字逻辑；视频输出滤波器、SID 滤波器和电源等模拟元件尚未模拟。该程序适用于 macOS 和 Linux。

---

## 4. Furifont：一款可显示振假名的日文字体。

**原文标题**: Furifont, a Japanese font that shows furigana

**原文链接**: [https://furifont.antfu.me/](https://furifont.antfu.me/)

**Furifont** 是一款专为日语设计的字体，通过将振假名（读音辅助）直接嵌入字体内部，实现了注音的自动显示。

与需要手动格式化或复杂 HTML “ruby” 标签的传统方法不同，Furifont 将振假名整合进了字形设计中。这使用户能够在标准文本编辑器和设计软件中无缝显示读音，无需专门的排版工具，即可让学习者和儿童更轻松地阅读日语文本。

---

## 5. Making chicken transparent using Dorito dust

**原文标题**: Making chicken transparent using Dorito dust

**原文链接**: [https://chillphysicsenjoyer.substack.com/p/making-chicken-transparent-using](https://chillphysicsenjoyer.substack.com/p/making-chicken-transparent-using)

在最近发表于《科学》杂志的一项重大突破中，斯坦福大学的研究人员展示了一种利用 FD&C 食用黄色 5 号（通称柠檬黄，即赋予多利多姿玉米片橙亮色泽的色素）使活体组织变透明的方法。

这项技术解决了生物组织不透明的根本物理原因：光散射。组织由水和脂质（脂肪）组成，两者的折射率各不相同。当光线照射到这些物质之间的界面时会产生散射，导致我们无法看透皮肤。传统上，“透明化”组织需要使用强效化学试剂，且仅对死亡标本有效。

研究人员利用了克拉默斯-克勒尼希关系（Kramers-Kronig relations），这一数学原理描述了物质在某些频率下的光吸收如何影响其在其他频率下的折射率。通过引入能吸收蓝光和紫外光的柠檬黄，他们成功提高了组织中水分的折射率，使其与脂质相匹配。当折射率达成一致时，光线便能穿过组织而不产生散射，从而实现透明化。

在实验室测试中，将柠檬黄溶液涂抹在活体小鼠的皮肤上，研究人员得以实时观察其内脏器官、肌肉收缩和血液流动。至关重要的是，该过程具有生物相容性且可逆：一旦洗掉染料，皮肤就会恢复不透明状态，而被吸收的染料也会被安全排出。

虽然该技术尚未应用于人体（人类皮肤明显比小鼠厚），但它代表了医学成像领域的一次重大飞跃。这种“光学透明化”技术最终可能让医生无需进行侵入性程序或昂贵的放射性扫描，即可观察损伤、监测深层肿瘤或辅助静脉采血定位。

---

## 6. DeepSeek-v4.1-Flash-1017

**原文标题**: DeepSeek-v4.1-Flash-1017

**原文链接**: [https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)

根据提供的元数据，**DeepSeek-v4.1-Flash-1017** 指的是 DeepSeek-AI 团队近期更新的一系列 AI 模型或资源（可能托管在 Hugging Face 或 GitHub 等平台上）。

以下是关键信息的简要总结：

**概述与范围**
该集合包含 **11 个不同的项目**，通常包括各种模型权重、量化版本（如 GGUF 或 AWQ 格式）以及配置文件。“1017”后缀暗示发布或重大更新日期为 10 月 17 日。

**核心技术亮点**
*   **性能优化：** “Flash”名称表明这些模型是专为**高速推理和低延迟**而设计的。它们可能是大型模型的蒸馏或剪枝版本，旨在保持高准确性的同时提供快速响应。
*   **版本迭代：** 作为 4.1 版本，本次发布代表了 DeepSeek 系列的增量改进，可能增强了模型在编程、数学或多步推理等领域的能力。
*   **灵活性：** 通过提供 11 个不同的项目，本次发布让开发者能够根据硬件限制灵活选择特定的模型大小或优化级别。

**结论**
DeepSeek-v4.1-Flash-1017 是一次专注于**效率和部署就绪性**的重大更新。它旨在为开发者社区提供高性能的开源大语言模型，在复杂的语言能力与实时应用所需的响应速度之间取得平衡。

---

## 7. 黄金现已成为美国最大出口商品

**原文标题**: Gold is now the top U.S. export

**原文链接**: [https://www.numismaticnews.net/gold-now-top-u-s-export](https://www.numismaticnews.net/gold-now-top-u-s-export)

As of May 2026, gold has overtaken traditional leaders like oil and pharmaceuticals to become the top U.S. export. According to Patrick A. Heller, this shift began in late 2025, with export volumes in February 2026 potentially setting all-time records. The primary destinations for these exports are Switzerland, Hong Kong (serving as a gateway to China), and the United Kingdom.

The surge is attributed to a global decline in confidence regarding the U.S. dollar’s future purchasing power. For the first time, the combined value of gold reserves held by foreign central banks exceeds their holdings of U.S. Treasury debt. China is a major driver of this trend; the nation has aggressively liquidated its U.S. Treasury holdings—dropping from $1.1 trillion in 2021 to roughly $693 billion in early 2026—and replaced them with gold.

Heller speculates that because China possesses the economic leverage to demand payment in assets other than dollars, a significant portion of U.S. gold exports may be used to settle international trade or secure political concessions. Despite this massive outflow, official U.S. gold reserves remain reportedly unchanged, suggesting the exported gold originates from domestic mining and recycling operations rather than government vaults.

The article highlights a broader movement by the BRICS consortium to develop alternative payment systems and reduce reliance on the dollar. Heller concludes by noting that while his theory regarding political concessions cannot be proven, the data clearly shows a historic restructuring of global reserve assets in favor of gold.

---

## 8. tsc-ts: TypeScript written in TypeScript

**原文标题**: tsc-ts: TypeScript written in TypeScript

**原文链接**: [https://github.com/vercel-labs/tsc-ts](https://github.com/vercel-labs/tsc-ts)

**Summary: tsc-ts – TypeScript written in TypeScript**

`tsc-ts` is an experimental project by Vercel Labs that provides a version of the TypeScript compiler (`tsc`) refactored to run as a standalone, portable TypeScript module. While the official TypeScript compiler is written in TypeScript, it traditionally relies on Node.js-specific APIs (such as `fs` and `path`) to interact with the file system and the host environment.

The primary objective of `tsc-ts` is to decouple the compiler’s core logic from these Node.js dependencies. By doing so, the project enables the TypeScript compiler to function in environments where Node.js is unavailable, such as:

*   **Web Browsers:** Allowing for client-side type-checking and transpilation.
*   **Edge Runtimes:** Enabling TypeScript processing within Vercel Edge Functions or other serverless environments.
*   **Alternative Runtimes:** Running on any JavaScript engine that lacks standard Node.js modules.

**Key Information:**
*   **Portability:** The project bundles the compiler into a single, self-contained file that can be imported and executed in diverse JavaScript environments.
*   **Self-Hosting:** It represents an effort toward a "pure" TypeScript implementation of the compiler that is agnostic of the underlying operating system.
*   **Use Cases:** It is particularly valuable for developers building web-based IDEs, online playgrounds, or high-performance edge applications that require real-time TypeScript compilation without the overhead of a full Node.js environment.

Essentially, `tsc-ts` transforms the TypeScript compiler into a truly platform-independent library, expanding the language's utility across the modern web stack.

---

## 9. Dam removals are bringing fish back across the northeastern United States

**原文标题**: Dam removals are bringing fish back across the northeastern United States

**原文链接**: [https://www.smithsonianmag.com/science-nature/dam-removals-are-bringing-fish-back-across-the-northeastern-united-states-striking-down-one-tiny-barrier-at-a-time-180989679/](https://www.smithsonianmag.com/science-nature/dam-removals-are-bringing-fish-back-across-the-northeastern-united-states-striking-down-one-tiny-barrier-at-a-time-180989679/)

生成摘要时出错

---

## 10. Artie (YC S23) Is Hiring Enterprise AES and Senior Engineers

**原文标题**: Artie (YC S23) Is Hiring Enterprise AES and Senior Engineers

**原文链接**: [https://www.artie.com/careers](https://www.artie.com/careers)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 2 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 3 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 4 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 5 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 6 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 7 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 8 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 9 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 10 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 11 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 12 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 13 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 14 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 15 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 16 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 17 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 18 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 19 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 20 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 21 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 22 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 23 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 24 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 25 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 26 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 27 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 28 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 29 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 30 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 31 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 32 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 33 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 34 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 35 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 36 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 37 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 38 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 39 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 40 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 41 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 42 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 43 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 44 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 45 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 46 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 47 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 48 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 49 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 50 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 51 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 52 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 53 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 54 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 55 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 56 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 57 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 58 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 59 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 60 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 61 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 62 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 63 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 64 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 65 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 66 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 67 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 68 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 69 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 70 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 71 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 72 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 73 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 74 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 75 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 76 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 77 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 78 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 79 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 80 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 81 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 82 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 83 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 84 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 85 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 86 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 87 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 88 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 89 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 90 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 91 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 92 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 93 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 94 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 95 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 96 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 97 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 98 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 99 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 100 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 101 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 102 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 103 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 104 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 105 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 106 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 107 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 108 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 109 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 110 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 111 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 112 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 113 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 114 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 115 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 116 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 117 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 118 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 119 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 120 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 121 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 122 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 123 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 124 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 125 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 126 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 127 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 128 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 129 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 130 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 131 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 132 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 133 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 134 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 135 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 136 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 137 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 138 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 139 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 140 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 141 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 142 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 143 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 144 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 145 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 146 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 147 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 148 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 149 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 150 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 151 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 152 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 153 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 154 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 155 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 156 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 157 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 158 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 159 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 160 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 161 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 162 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 163 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 164 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 165 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 166 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 167 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 168 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 169 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 170 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 171 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 172 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 173 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 174 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 175 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 176 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 177 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 178 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 179 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 180 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 181 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 182 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 183 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 184 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 185 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 186 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 187 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 188 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 189 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 190 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 191 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 192 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 193 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 194 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 195 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 196 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 197 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 198 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 199 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 200 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 201 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 202 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 203 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 204 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 205 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 206 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 207 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 208 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 209 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 210 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 211 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 212 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 213 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 214 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 215 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 216 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 217 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 218 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 219 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 220 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 221 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 222 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 223 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 224 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 225 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 226 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 227 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 228 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 229 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 230 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 231 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 232 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 233 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 234 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 235 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 236 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 237 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 238 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 239 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 240 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 241 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 242 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 243 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 244 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 245 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 246 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 247 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 248 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 249 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 250 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 251 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 252 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 253 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 254 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 255 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 256 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 257 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 258 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 259 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 260 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 261 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 262 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 263 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 264 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 265 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 266 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 267 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 268 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 269 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 270 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 271 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 272 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 273 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 274 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 275 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 276 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 277 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 278 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 279 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 280 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 281 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 282 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 283 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 284 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 285 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 286 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 287 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 288 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 289 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 290 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 291 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 292 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 293 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 294 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 295 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 296 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 297 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 298 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 299 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 300 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 301 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 302 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 303 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 304 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 305 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 306 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 307 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 308 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 309 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 310 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 311 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 312 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 313 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 314 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 315 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 316 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 317 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 318 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 319 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 320 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 321 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 322 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 323 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 324 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 325 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 326 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 327 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 328 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 329 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 330 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 331 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 332 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 333 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 334 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 335 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 336 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 337 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 338 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 339 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 340 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 341 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 342 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 343 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 344 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 345 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 346 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 347 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 348 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 349 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 350 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 351 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 352 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 353 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 354 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 355 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 356 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 357 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 358 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 359 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 360 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 361 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 362 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 363 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 364 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 365 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 366 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 367 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 368 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 369 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 370 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 371 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 372 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 373 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 374 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 375 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 376 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 377 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 378 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 379 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 380 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 381 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 382 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 383 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 384 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 385 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 386 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 387 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 388 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 389 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 390 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 391 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 392 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 393 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 394 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 395 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 396 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 397 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 398 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 399 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 400 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 401 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 402 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 403 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 404 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 405 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 406 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 407 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 408 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 409 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 410 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 411 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 412 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 413 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 414 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 415 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 416 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 417 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 418 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 419 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 420 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 421 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 422 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 423 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 424 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 425 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 426 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 427 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 428 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 429 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 430 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 431 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 432 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 433 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 434 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 435 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 436 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 437 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 438 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 439 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 440 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 441 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 442 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 443 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 444 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 445 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 446 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 447 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 448 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 449 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 450 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 451 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 452 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 453 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 454 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 455 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 456 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 457 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 458 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 459 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 460 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 461 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 462 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 463 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 464 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 465 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 466 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 467 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 468 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 469 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 470 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 471 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 472 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 473 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 474 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 475 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 476 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 477 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 478 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 479 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 480 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 481 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 482 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 483 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 484 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 485 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 486 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 487 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 488 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 489 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 490 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 491 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 492 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 493 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 494 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 495 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 496 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 497 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 498 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 499 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 500 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 501 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 502 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 503 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 504 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 505 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 506 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 507 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 508 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 509 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 510 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 511 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 512 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 513 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 514 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 515 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 516 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 517 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 518 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 519 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 520 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 521 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 522 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 523 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 524 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 525 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 526 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 527 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 528 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 529 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 530 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 531 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 532 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 533 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 534 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 535 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 536 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 537 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 538 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 539 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 540 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 541 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 542 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 543 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 544 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 545 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 546 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 547 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 548 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 549 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 550 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 551 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 552 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 553 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 554 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 555 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 556 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 557 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 558 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 559 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 560 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 561 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 562 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 563 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 564 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 565 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 566 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 567 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 568 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 569 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 570 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 571 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 572 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 573 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 574 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
