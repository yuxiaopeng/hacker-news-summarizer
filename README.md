# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-26.md)

*最后自动更新时间: 2026-04-26 18:11:50*
## 1. Asahi Linux 进展：Linux 7.0

**原文标题**: Asahi Linux Progress Linux 7.0

**原文链接**: [https://asahilinux.org/2026/04/progress-report-7-0/](https://asahilinux.org/2026/04/progress-report-7-0/)

Linux 7.0 的发布标志着 Asahi Linux 的一个重要里程碑，为安装程序自动化、能效以及 Apple Silicon 硬件支持带来了重大更新。

**安装程序与固件更新**
Asahi 安装程序 (v0.8.0) 已转型为通过 GitHub 工作流实现的自动化部署系统，确保了更频繁的更新。它现在支持 Mac Pro 并引入了“固件更新模式”。这允许安装程序从 macOS 中提取专有的校准数据，从而通过常驻处理器 (AOP) 启用环境光传感器 (ALS) 和原彩显示 (True Tone) 功能。

**电源管理**
通过启用电源管理处理器 (PMP)，能效方面取得了重大突破。新驱动程序允许 SoC 正确报告电源状态，使待机功耗降低了约 20%（在 M1 Pro MacBook Pro 上可节省约 0.5W）。虽然目前仍处于实验阶段，但这是迈向匹配 macOS 电池续航表现的关键一步。

**连接性与显示增强**
*   **蓝牙：** 通过在内核中实现博通 (Broadcom) 特定的共存命令，解决了音频中断问题。这些命令会将音频流等延迟敏感型流量的优先级置于 WiFi 扫描等后台任务之上。
*   **可变刷新率 (VRR)：** 开发人员发现，显示控制器 (DCP) 固件中此前一个被误解的参数实际上是 VRR 的开关。这一发现为 MacBook Pro 带来了 ProMotion 支持，并为外接显示器启用了自适应同步。由于苹果对切换 VRR 的“模式设置 (modeset)”有非标准要求，该功能目前需要通过手动内核参数 (`appledrm.force_vrr`) 开启。

总体而言，Linux 7.0 报告标志着开发重点已从基础硬件适配转向精细的电源优化和流线化的用户体验。

---

## 2. 粘土 PCB 教程

**原文标题**: Clay PCB Tutorial

**原文链接**: [https://feministhackerspaces.cargo.site/Clay-PCB-Tutorial](https://feministhackerspaces.cargo.site/Clay-PCB-Tutorial)

《黏土 PCB 教程》概述了一种利用风干黏土和铜箔胶带制作电子电路的创新方法。这种方法为传统的刚性 PCB 制造提供了一种低成本、易于获取的替代方案，将工业电子与触感手工结合在一起。

**材料与工具**
制作过程需要基础且廉价的材料：风干黏土（如 DAS）、背胶铜箔胶带、电子元件（LED、电阻、电池）、擀面杖和美工刀。

**制作流程**
1.  **准备：** 将黏土擀成所需厚度的平整薄片。
2.  **电路设计：** 根据电路图，将铜箔胶带直接贴在潮湿的黏土上，制作出导电走线。
3.  **塑形：** 使用美工刀或黏土切割器根据电路布局对基底进行塑形，从而创作出具有装饰性或有机形态的形状。
4.  **干燥：** 让黏土完全风干。教程指出，黏土在干燥过程中可能会轻微收缩，因此走线应粘贴牢固。
5.  **组装：** 待黏土硬化后，安装电子元件。指南建议将元件直接焊接在铜箔上，或使用机械连接实现免焊接。

**核心要点**
该教程强调电子产品不一定必须是扁平、绿色或刚性的。通过使用黏土，创客可以尝试标准玻璃纤维板无法实现的三维形态和极具表现力的形状。这种方法特别适用于教学工作坊、艺术装置，以及希望通过手工创作视角探索电子技术的爱好者。最终，该项目通过使用常见的、亲和力强的材料降低了进入电子领域的门槛，弘扬了“女性主义黑客空间”的精神。

---

## 3. 为什么 SWE-bench Verified 不再能衡量前沿编程能力

**原文标题**: Why SWE-bench Verified no longer measures frontier coding capabilities

**原文链接**: [https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)

OpenAI 宣布将不再使用 **SWE-bench Verified** 作为评估前沿编程能力的主要指标。尽管 SWE-bench Verified 最初旨在通过过滤掉无法解决或定义不明确的 GitHub 问题来提高原始 SWE-bench 的可靠性，但 OpenAI 认为该基准测试已达到“**饱和**”状态。

核心问题在于，随着像 **o1** 这样的模型取得更高的成功率，剩余未解决的任务往往涉及“隐性知识”（即问题描述中未包含的信息）或规格设定不当。因此，分数的微小提升已无法可靠地区分前沿模型之间的推理能力差异。相反，高性能可能反映的是模型处理数据集噪声或对特定模式过拟合的能力，而非展现出卓越的软件工程逻辑。

此外，OpenAI 指出，SWE-bench 侧重于解决孤立的单个 GitHub 问题，无法充分体现现实世界大规模软件开发所需的**长程推理**和复杂的架构规划。

为了更好地衡量下一代 AI，OpenAI 正将重心转向更严谨的多步基准测试。这些新的评估旨在测试**智能体行为（agentic behavior）**以及在更长时间跨度内处理持续、复杂工程任务的能力，以确保性能提升反映的是通用问题解决能力的实质性进步，而非针对特定基准测试的优化。

---

## 4. 状态图：分层状态机

**原文标题**: Statecharts: hierarchical state machines

**原文链接**: [https://statecharts.dev/](https://statecharts.dev/)

本文介绍了**状态图（statecharts）**，它是状态机的“增强版”，旨在为复杂系统提供一种可视化形式语言。通过将逻辑组织为分层状态，状态图解决了传统状态机中常见的“状态爆炸”问题。

**主要优缺点**
状态图的主要优势在于行为与组件的解耦。这使得代码更易于测试、理清逻辑和维护。它们是强大的沟通工具，能让非开发人员和测试团队理解系统逻辑。研究表明，基于状态图的代码 Bug 更少，且能更好地处理异常情况。

然而，其应用也面临挑战，包括开发人员面临陡峭的学习曲线，以及可能导致团队抵触的“异质”编码风格。对于小型项目，在库体积和代码行数上还可能存在潜在的额外开销。

**实现与标准**
状态图由 W3C 通过 **SCXML**（状态图可扩展标记语言）实现标准化，该标准定义了处理进入和退出动作等边缘情况的语义。许多跨平台库都支持这些标准。

**可执行状态图**
文章重点介绍了“可执行状态图”，即由单一事实来源（通常是 JSON 或 XML）同时驱动运行时行为和可视化图表。这确保了文档与代码完美同步，消除了人工转换错误。虽然这提高了精准度，但可能导致图表过于复杂，并在类型安全方面带来困难。

总之，状态图被视为管理复杂性和提高软件可靠性的稳健方案，并得到了 Gitter 和 GitHub 等平台上活跃社区的支持。

---

## 5. 亲爱的朋友，你已经搭建了一个 Kubernetes (2024)

**原文标题**: Dear friend, you have built a Kubernetes (2024)

**原文链接**: [https://www.macchaffee.com/blog/2024/you-have-built-a-kubernetes/](https://www.macchaffee.com/blog/2024/you-have-built-a-kubernetes/)

文章《亲爱的朋友，你已经构建了一个 Kubernetes》探讨了一个常见的讽刺现象：开发者往往以“过度设计”为由拒绝 Kubernetes，结果却通过一系列日益复杂的变通方案，手动重建了其完整的架构。

作者描述了一个典型的演进轨迹：开发者最初为了避开 Kubernetes 的复杂性，选择使用简单的 Shell 脚本等“枯燥技术”。然而，随着生产需求的增长，他们被迫逐一添加功能。他们从 Shell 脚本转向 Docker Compose，随后为多服务器部署编写自定义参数；为了处理网络和服务发现，他们引入了 Tailscale 等覆盖网络；为了确保服务器的不可变性和版本控制，他们采用了 Ansible；最后，他们甚至构建了自定义 API 服务来以编程方式管理容器。

在这段旅程的终点，开发者实际上已经构建了一套由标准配置格式、部署方法、覆盖网络、服务发现、不可变节点和 API 服务组成的“定制化 Kubernetes”。作者指出，这种 DIY 方式往往会产生一个脆弱、缺乏文档且难以维护的“补丁堆”，其维护成本甚至高于他们最初想要避开的 Kubernetes 平台。

其核心观点带有警示意义：虽然自定义部署方法有其适用场景，但在拒绝 Kubernetes 之前，开发者应充分理解它所解决的基础设施问题。否则，他们极易陷入拙劣地“重复造轮子”的困境，而不是专注于交付业务功能。

---

## 6. Free Textbook on Engineering Thermodynamics

**原文标题**: Free Textbook on Engineering Thermodynamics

**原文链接**: [https://thermodynamicsbook.com/](https://thermodynamicsbook.com/)

**《工程热力学》**（**Engineering Thermodynamics**）是由 Olivier Cleynen 博士编写的一本详尽的大学教材，旨在帮助学生和工程师掌握热机与制冷系统背后的物理原理。这本 330 页的著作对该领域进行了严谨而清晰的介绍，全书共十章，涵盖了基本概念、热力学定律、理想气体以及复杂的动力循环（包括水蒸汽动力和空气动力循环）。

本教材的一个核心特色是强调实际应用，其内容包括：
*   **59 个带有详尽注释的例题解析**。
*   **96 道附有完整答案的练习题**。
*   **配图丰富的理论部分**以及历史背景探索，旨在为重大科学思想提供语境。

本书属于**开放教育资源（OER）**，采用知识共享署名-相同方式共享许可协议（CC-by-sa）。这允许用户免费下载、重用和重新混编内容。虽然 40 MB 的 PDF 版本完全免费，但读者也可以选择以 2 欧元购买数字版或以 49 欧元购买黑白印刷版，以支持作者。

这一 2025 国际版（采用国际单位制 SI）译自法语原著 *Thermodynamique de l’ingénieur* 的第三版。相关教学材料历经十余年的打磨，目前已被索邦大学和多家法国工程师学院等众多知名机构采用。Cleynen 博士拥有流体力学博士学位，并拥有 15 年的教学经验；他注重培养物理直觉，并致力于将复杂的课题转化为易于处理的工程挑战。

---

## 7. Databases Were Not Designed for This

**原文标题**: Databases Were Not Designed for This

**原文链接**: [https://arpitbhayani.me/blogs/defensive-databases/](https://arpitbhayani.me/blogs/defensive-databases/)

生成摘要时出错

---

## 8. Amateur armed with ChatGPT solves an Erdős problem

**原文标题**: Amateur armed with ChatGPT solves an Erdős problem

**原文链接**: [https://www.scientificamerican.com/article/amateur-armed-with-chatgpt-vibe-maths-a-60-year-old-problem/](https://www.scientificamerican.com/article/amateur-armed-with-chatgpt-vibe-maths-a-60-year-old-problem/)

生成摘要时出错

---

## 9. Show HN: Turning a Gaussian Splat into a videogame

**原文标题**: Show HN: Turning a Gaussian Splat into a videogame

**原文链接**: [https://blog.playcanvas.com/turning-a-gaussian-splat-into-a-videogame/](https://blog.playcanvas.com/turning-a-gaussian-splat-into-a-videogame/)

生成摘要时出错

---

## 10. Why has there been so little progress on Alzheimer's disease?

**原文标题**: Why has there been so little progress on Alzheimer's disease?

**原文链接**: [https://freakonomics.com/podcast/why-has-there-been-so-little-progress-on-alzheimers-disease/](https://freakonomics.com/podcast/why-has-there-been-so-little-progress-on-alzheimers-disease/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 2 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 3 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 4 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 5 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 6 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 7 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 8 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 9 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 10 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 11 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 12 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 13 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 14 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 15 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 16 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 17 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 18 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 19 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 20 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 21 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 22 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 23 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 24 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 25 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 26 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 27 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 28 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 29 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 30 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 31 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 32 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 33 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 34 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 35 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 36 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 37 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 38 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 39 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 40 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 41 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 42 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 43 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 44 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 45 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 46 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 47 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 48 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 49 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 50 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 51 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 52 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 53 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 54 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 55 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 56 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 57 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 58 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 59 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 60 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 61 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 62 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 63 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 64 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 65 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 66 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 67 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 68 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 69 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 70 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 71 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 72 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 73 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 74 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 75 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 76 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 77 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 78 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 79 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 80 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 81 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 82 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 83 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 84 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 85 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 86 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 87 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 88 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 89 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 90 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 91 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 92 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 93 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 94 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 95 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 96 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 97 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 98 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 99 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 100 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 101 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 102 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 103 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 104 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 105 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 106 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 107 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 108 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 109 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 110 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 111 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 112 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 113 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 114 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 115 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 116 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 117 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 118 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 119 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 120 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 121 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 122 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 123 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 124 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 125 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 126 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 127 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 128 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 129 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 130 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 131 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 132 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 133 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 134 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 135 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 136 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 137 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 138 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 139 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 140 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 141 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 142 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 143 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 144 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 145 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 146 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 147 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 148 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 149 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 150 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 151 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 152 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 153 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 154 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 155 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 156 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 157 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 158 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 159 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 160 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 161 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 162 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 163 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 164 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 165 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 166 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 167 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 168 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 169 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 170 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 171 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 172 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 173 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 174 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 175 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 176 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 177 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 178 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 179 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 180 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 181 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 182 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 183 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 184 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 185 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 186 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 187 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 188 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 189 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 190 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 191 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 192 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 193 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 194 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 195 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 196 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 197 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 198 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 199 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 200 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 201 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 202 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 203 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 204 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 205 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 206 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 207 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 208 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 209 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 210 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 211 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 212 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 213 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 214 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 215 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 216 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 217 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 218 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 219 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 220 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 221 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 222 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 223 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 224 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 225 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 226 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 227 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 228 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 229 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 230 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 231 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 232 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 233 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 234 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 235 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 236 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 237 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 238 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 239 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 240 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 241 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 242 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 243 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 244 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 245 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 246 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 247 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 248 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 249 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 250 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 251 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 252 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 253 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 254 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 255 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 256 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 257 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 258 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 259 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 260 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 261 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 262 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 263 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 264 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 265 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 266 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 267 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 268 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 269 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 270 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 271 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 272 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 273 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 274 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 275 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 276 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 277 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 278 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 279 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 280 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 281 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 282 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 283 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 284 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 285 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 286 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 287 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 288 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 289 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 290 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 291 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 292 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 293 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 294 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 295 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 296 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 297 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 298 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 299 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 300 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 301 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 302 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 303 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 304 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 305 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 306 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 307 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 308 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 309 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 310 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 311 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 312 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 313 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 314 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 315 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 316 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 317 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 318 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 319 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 320 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 321 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 322 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 323 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 324 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 325 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 326 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 327 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 328 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 329 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 330 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 331 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 332 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 333 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 334 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 335 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 336 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 337 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 338 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 339 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 340 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 341 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 342 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 343 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 344 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 345 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 346 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 347 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 348 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 349 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 350 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 351 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 352 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 353 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 354 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 355 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 356 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 357 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 358 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 359 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 360 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 361 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 362 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 363 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 364 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 365 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 366 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 367 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 368 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 369 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 370 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 371 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 372 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 373 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 374 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 375 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 376 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 377 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 378 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 379 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 380 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 381 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 382 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 383 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 384 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 385 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 386 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 387 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 388 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 389 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 390 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 391 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 392 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 393 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 394 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 395 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 396 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 397 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 398 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 399 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 400 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 401 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 402 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
