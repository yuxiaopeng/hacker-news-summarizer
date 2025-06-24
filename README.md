# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-06-24.md)

*最后自动更新时间: 2025-06-24 17:50:54*
## 1. 编写玩具软件是一种乐趣

**原文标题**: Writing toy software is a joy

**原文链接**: [https://blog.jsbarretto.com/post/software-is-joy](https://blog.jsbarretto.com/post/software-is-joy)

约书亚·巴雷托的文章倡导创建“玩具程序”，认为这对软件开发者来说是一项有价值且能带来乐趣的学习活动。他认为，尽管人工智能兴起和软件开发日益商品化，但构建简化的个人项目，以重新发现编码的乐趣并加深理解，仍具有巨大的益处。

其核心原则是“创造以理解”，强调构建自己简陋的复杂系统版本（例如正则表达式引擎或操作系统内核）比单纯地研究它们能提供更深刻的见解。这些玩具程序旨在遵循80/20法则，专注于核心功能，同时积极避免过度设计。

除了固有的学习之外，作者还强调了意想不到的实际好处，即从这些项目中获得的知识经常在专业环境中证明是有价值的。他提供了一份建议的玩具程序清单，按难度和时间投入进行分级，范围从简单的正则表达式引擎到更具雄心的编译器或操作系统内核。这些建议涵盖了各种领域，包括模拟器、游戏开发、解释器和图形渲染。

巴雷托告诫不要依赖大型语言模型来完成这些项目，而是提倡亲身探索和发现。他强调，学习的乐趣在于克服挑战和开发独特的解决方案，而不是仅仅接收预先打包的答案。文章最后呼吁拥抱焦油坑，承认潜在的挫折，但强调了从头开始构建和理解某些东西所带来的令人欣慰的“跑步者高峰”体验。

---

## 2. 在Power Mac G3 ROM中发现一个27年前的彩蛋

**原文标题**: Finding a 27-year-old easter egg in the Power Mac G3 ROM

**原文链接**: [https://www.downtowndougbrown.com/2025/06/finding-a-27-year-old-easter-egg-in-the-power-mac-g3-rom/](https://www.downtowndougbrown.com/2025/06/finding-a-27-year-old-easter-egg-in-the-power-mac-g3-rom/)

道格·布朗详细描述了他对 Power Mac G3 ROM 中一个先前未被记录的彩蛋的发现。在使用 Hex Fiend 和 Eric Harmon 的 ROM Fiend 模板检查 ROM 时，他发现了 Apple 员工的 JPEG 图像（资源类型为 HPOE）以及 SCSI Manager 4.3 代码中的 Pascal 字符串（nitt 资源 ID 为 43），特别是“.Edisk”和“secret ROM image”。

由于对“secret ROM image”文本和隐藏图片之间的联系感兴趣，道格使用 Ghidra 反汇编了代码。他发现代码会检查名为“secret ROM image”的 RAM 磁盘。如果找到，它会从 HPOE 资源加载 JPEG 图像数据，并在 RAM 磁盘中创建一个名为“The Team”的文件，类型为 JPEG。

与 Libera 上 #mac68k 的 ^alex 合作，他们发现，在格式化过程中格式化 RAM 磁盘并将卷命名为“secret ROM image”会触发这个彩蛋。用这个名称格式化 RAM 磁盘后，一个名为“The Team”的文件会出现在 RAM 磁盘中，打开时会包含 JPEG 图像。

该彩蛋适用于高达 Mac OS 9.0.4 的版本，可能在 9.1 中被禁用。布朗认为这是史蒂夫·乔布斯据报道禁止彩蛋之前的最后一个彩蛋之一。他希望与“The Team”中的任何一位成员联系，他们可能还记得这个彩蛋。

---

## 3. 食品塑料含量列表

**原文标题**: PlasticList – Plastic Levels in Foods

**原文链接**: [https://www.plasticlist.org/](https://www.plasticlist.org/)

鉴于内容极其有限，“塑料清单 – 食品中的塑料含量”难以进行简明扼要的总结。但我们可以推断其可能用途并进行概括。

**总结:**

“塑料清单 – 食品中的塑料含量”可能是一种资源（文章、数据库或指南），提供关于各种食品中存在的塑料污染及其含量的信息。它可能旨在告知消费者通过食物摄入塑料的潜在来源，并可能根据食品中的塑料含量对食品进行排名或分类。 这些信息可能来源于关于食品中微塑料和纳米塑料的科学研究、研究结果或报告。该资源还可能提供关于检测到的塑料类型、其潜在健康影响以及通过饮食选择减少塑料暴露的可能缓解策略的见解。最终，“塑料清单”可能作为一种工具，提高人们的意识并使个人能够就与塑料污染相关的食品消费做出更明智的决定。

---

## 4. 星舰：适用于任何 Shell 的极简、快速且可定制的提示符

**原文标题**: Starship: The minimal, fast, and customizable prompt for any shell

**原文链接**: [https://starship.rs/](https://starship.rs/)

Starship：极简、快速、可定制的终端提示符。其主要优势在于广泛的兼容性，可跨多种Shell和操作系统运行，几乎可在任何环境中使用。关键在于其“随处可用”的原则，意味着通用且可移植的提示解决方案。

---

## 5. 北欧半导体收购Memfault

**原文标题**: Nordic Semiconductor Acquires Memfault

**原文链接**: [https://www.nordicsemi.com/Nordic-news/2025/06/Nordic-Semiconductor-acquires-Memfault](https://www.nordicsemi.com/Nordic-news/2025/06/Nordic-Semiconductor-acquires-Memfault)

Nordic Semiconductor于2025年6月24日收购Memfault，标志着Nordic从硬件供应商向提供硬件、软件和云服务的完整解决方案合作伙伴的重要转变。Memfault是市场领先的云平台供应商，专门从事大规模互联产品部署。

此次收购旨在简化产品开发，加速上市时间，并通过持续的软件升级和设备管理，增强互联产品的安全性、性能和功能。Nordic计划将Memfault的功能集成到其产品组合和nRF Cloud服务平台中，从而创建更强大、更有效的解决方案。

Nordic Semiconductor首席执行官Vegard Wollan强调，此举将使客户能够与现场数百万台设备进行交互。Memfault首席执行官François Baldassari强调了为互联产品创建全栈解决方案。

预计此次收购将加强Nordic在边缘人工智能和安全解决方案方面的地位，使开发人员能够满足不断发展的行业和监管标准，例如欧盟网络弹性法案。Nordic致力于支持现有的Memfault客户，无论他们选择何种硬件，确保该平台通过对硬件集成、设备管理和人工智能功能的投资而持续发展。最终目标是缩短上市时间，降低运营成本，并改善互联产品的生命周期管理。

---

## 6. GPU基本知识

**原文标题**: Basic Facts about GPUs

**原文链接**: [https://damek.github.io/random/basic-facts-about-gpus/](https://damek.github.io/random/basic-facts-about-gpus/)

本文概述了GPU架构和优化技术的基础知识，重点介绍了NVIDIA A100 GPU。它解释了计算和内存层次结构，突出了快速计算和较慢内存访问之间的性能不平衡。

核心概念是Roofline模型，它定义了两种性能状态：内存受限和计算受限。内存受限的操作受限于内存带宽，而计算受限的操作受限于SM的算术速度。算术强度 (AI)，即FLOPs与访问字节的比率，决定了性能状态。目标是最大化AI以实现计算受限的性能。

本文介绍了两种关键的优化策略：**算子融合**和**分块**。算子融合将多个内存受限的操作组合成一个内核，消除中间内存流量并减少开销。分块用于计算受限的内核，如矩阵乘法，其中线程协同工作，将数据块加载到共享内存（SRAM）中，以最大化数据重用并增加AI。分块算法包括将数据加载到共享内存、同步线程和执行计算。

最后，本文讨论了来自主机CPU的开销影响，强调内核大小的重要性。如果内核太小或数量过多，则GPU会将时间花费在等待主机上，而不是执行计算。

---

## 7. 痛苦的教训即将降临到Token化领域。

**原文标题**: The Bitter Lesson is coming for Tokenization

**原文链接**: [https://lucalp.dev/bitter-lesson-tokenization-and-blt/](https://lucalp.dev/bitter-lesson-tokenization-and-blt/)

“Tokenization的苦涩教训即将到来”：本文认为，分词（LLM 中的常见做法）是一个瓶颈，应该用更通用、计算和数据驱动的方法来取代。

作者批评了字节对编码 (BPE) 这种流行的分词方法，强调了它的局限性，例如创建建模不佳的“故障标记”和不连贯的数字分词。 虽然承认存在变通方法，但文章质疑由于不完美的分词，有多少模型能力被浪费了。它质疑是否可以完全绕过分词。

文章指出 ByT5 是一个初步答案，表明纯字节建模可以用更少的数据实现相当的性能，但代价是增加了预训练和推理时间。 它还提到了替代架构，如 MambaByte，以绕过注意力的复杂性并减少增加的推理步骤。

文章强调，要成功取代分词，模型应表现出具有竞争力的损失分数，改进下游任务，并在增加计算和数据的情况下表现出更好的缩放曲线。它讨论了无分词模型的设计空间，围绕具有下/上采样的压缩表示和灵活的字节宽度。 探索包括 CANINE、Charformer 和 Hourglass Transformers 等架构，它们使用各种方法来压缩字节表示并减轻计算成本。 作者还提到了通过学习边界预测器来进行动态令牌池化。

---

## 8. Gemini机器人设备端：将AI引入本地机器人设备

**原文标题**: Gemini Robotics On-Device brings AI to local robotic devices

**原文链接**: [https://deepmind.google/discover/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/](https://deepmind.google/discover/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/)

Gemini Robotics On-Device是谷歌推出的一款新型高效AI模型，旨在本地运行于机器人设备上，无需持续的数据网络连接即可实现更强的灵活性和更快的任务适应性。这使其适用于对延迟敏感的应用以及在连接受限区域的稳定性能。

该模型建立在Gemini Robotics模型的功能之上，但针对最小化计算资源进行了优化。主要特点包括快速实验、通过少量（仅50-100个）演示进行微调以适应新任务以及低延迟推理。它擅长视觉、语义和行为泛化，能够遵循自然语言指令并完成复杂的任务，例如拉开拉链和折叠衣服，所有这些都直接在机器人上运行。

谷歌正在通过一个可信测试者计划向开发者提供Gemini Robotics SDK，以促进评估、在物理模拟器中进行测试以及快速适应新领域。该模型已展示了对各种机器人形态的适应性，包括双臂 Franka FR3 机器人和 Apptronik 公司的 Apollo 人形机器人。

谷歌强调负责任的开发和安全，秉承其 AI 原则，整合语义和物理安全措施，并进行红队演练以识别漏洞。该模型最初发布给精选的可信测试者群体，以收集反馈并确保负责任的使用。Gemini Robotics SDK 旨在通过使强大的模型更易于访问来加速机器人技术的创新。

---

## 9. Show HN: Oasis – 一款开源的3D打印智能生态箱

**原文标题**: Show HN: Oasis – an open-source, 3D-printed smart terrarium

**原文链接**: [https://github.com/justbuchanan/oasis](https://github.com/justbuchanan/oasis)

Oasis是一个开源的、主要采用3D打印技术的智能生态缸，旨在为喜湿植物创造理想的环境。它配备高功率LED照明、喷雾器、用于气流循环的风扇以及温湿度传感器。通过WiFi连接，可以使用网页界面进行控制和配置。

该项目完全开源，包括CAD模型（CadQuery）、电子原理图（KiCad）和软件（使用esp-rs的Rust）。虽然拥有3D打印机的DIY爱好者可以使用，但电子组装较为复杂。可以从像JLCPCB这样的公司订购组装好的电子元件，但少量订购可能比较昂贵。经验丰富的用户可以订购裸PCB板和元件进行DIY组装。

创建者计划将来提供组装好的电子元件套件，并邀请有兴趣的人通过Google表单表达兴趣并订阅更新。该网站提供了图片和构建细节。

---

## 10. Timdle – 将历史事件按时间顺序排列

**原文标题**: Timdle – Place historical events in chronological order

**原文链接**: [https://www.timdle.com/](https://www.timdle.com/)

Timdle：一款每日在线游戏，挑战玩家通过按时间顺序排列历史事件来测试他们的历史知识。核心玩法涉及在时间线上安排事件，网站鼓励玩家“玩今天的timeline”。页面还包含“如何玩”的说明，表明其设计旨在易于上手且引人入胜。最后，电子邮件地址(daily.timdle@gmail.com)表明了一个联系点，用于解答疑问或潜在的用户生成内容。总而言之，Timdle被呈现为一款有趣且具有教育意义的游戏，通过时间线排列来测试和加强历史知识。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 2 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 3 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 4 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 5 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 6 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 7 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 8 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 9 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 10 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 11 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 12 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 13 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 14 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 15 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 16 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 17 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 18 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 19 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 20 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 21 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 22 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 23 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 24 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 25 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 26 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 27 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 28 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 29 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 30 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 31 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 32 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 33 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 34 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 35 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 36 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 37 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 38 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 39 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 40 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 41 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 42 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 43 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 44 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 45 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 46 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 47 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 48 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 49 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 50 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 51 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 52 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 53 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 54 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 55 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 56 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 57 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 58 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 59 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 60 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 61 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 62 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 63 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 64 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 65 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 66 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 67 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 68 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 69 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 70 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 71 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 72 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 73 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 74 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 75 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 76 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 77 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 78 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 79 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 80 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 81 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 82 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 83 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 84 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 85 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 86 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 87 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 88 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 89 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 90 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 91 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 92 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 93 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 94 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 95 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 96 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 97 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
