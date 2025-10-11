# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-10-11.md)

*最后自动更新时间: 2025-10-11 17:43:02*
## 1. 微软放大器

**原文标题**: Microsoft Amplifier

**原文链接**: [https://github.com/microsoft/amplifier](https://github.com/microsoft/amplifier)

微软Amplifier：一款旨在提升开发者生产力的超强人工智能开发环境研究项目。它利用人工智能编码助手，这些助手通过预加载模式、专业代理和自动化进行增强，以最小的人工投入交付复杂的解决方案。

Amplifier提供20多个专业人工智能代理，用于架构设计、调试、安全分析和知识合成等任务。它包含一个知识提取系统，将文档转化为可查询的知识库；一个并行工作树系统，用于同步解决方案开发；以及会话记录，用于保留上下文。

设置过程包括安装Python、UV、Node.js、VS Code和Git，然后克隆存储库并运行安装程序。用户可以配置数据目录，用于共享知识和跨设备同步。要将Amplifier与现有项目一起使用，用户启动Claude并指定项目目录，然后指示它在那里工作，并利用专业代理处理项目的代码。

主要功能包括专业代理、用于捕获和查询项目知识的知识库、用于维护上下文的会话记录以及用于代码生成的模块化构建器工作流程。Amplifier强调最佳实践，例如理解能力与上下文之间的关系，以及使用分解策略。虽然目前不接受外部贡献，但微软设想未来人工智能将处理繁琐的任务，使开发者能够专注于创造性决策，实现自然语言驱动的系统创建和不同方法的并行探索。

---

## 2. GNU 健康

**原文标题**: GNU Health

**原文链接**: [https://www.gnuhealth.org/about-us.html](https://www.gnuhealth.org/about-us.html)

GNU Health是一个自由开源项目，致力于提供工具来改善医疗保健的可及性和质量，解决健康的社会决定因素。它包含多个组件，包括：

*   **医院管理系统 (HMIS)：** 适用于医院和医疗机构的模块化系统，涵盖电子病历 (EMR)、医院管理和健康信息系统 (HIS)。它具有针对各种医学专业的模块，并将社会经济因素与生物信息学和临床遗传学相结合。

*   **GNU LIMS (Occhiolino)：** 用于管理医疗保健和生物医学环境中实验室分析的实验室信息管理系统。

*   **MyGNUHealth：** 适用于桌面和移动设备的个人健康记录 (PHR) 应用程序，优先考虑隐私和公民对健康信息的控制，从而改善与医疗专业人员的互动。

*   **GNU Health Federation：** 一种网络，允许创建大型、联邦式的健康网络，以改善医疗保健提供者、研究机构和政府机构之间的信息共享和协作。

*   **GNU Health Embedded：** 利用单板计算机进行实时生命体征监测、数据检索和个人健康跟踪。

该项目强调社会医学，旨在解决医疗保健获取方面的不平等，并将健康视为受到营养、住房、卫生和教育等社会经济因素的严重影响。GNU Health 是一个 GNU 官方软件包，由自由软件基金会授予，并已被世界各地的医院、政府和组织采用。

---

## 3. `<output>`标签

**原文标题**: The <output> Tag

**原文链接**: [https://denodell.com/blog/html-best-kept-secret-output-tag](https://denodell.com/blog/html-best-kept-secret-output-tag)

HTML的最佳秘密：`<output>`标签

---

## 4. 开发 Ghostty 的一个重要功能

**原文标题**: Vibing a non-trivial Ghostty feature

**原文链接**: [https://mitchellh.com/writing/non-trivial-vibing](https://mitchellh.com/writing/non-trivial-vibing)

米切尔·桥本详述了他使用人工智能（特别是Amp及其“预言机”子代理）为Ghostty开发不显眼的macOS更新通知功能的经验。他强调将人工智能作为助手，补充而非取代他自己的编码专业知识。

文章回顾了几个编码过程，展示了他如何使用人工智能来原型化用户界面，最初的目标是集成到标题栏中。虽然人工智能提供了一个良好的起点，但它遇到了一个无法解决的错误，迫使桥本后退一步，研究并设计了自己的解决方案。这导致了一个转变，对于特定的标题栏样式或当标题栏隐藏时，将通知实现为窗口右下角的覆盖层。

桥本强调了与人工智能一起进行规划和迭代开发的重要性。他强调了清理代码的重要性，以确保代码质量和理解，从而改进未来的人工智能编码会话。他利用人工智能寻找灵感，甚至会丢弃生成的代码并手动重做。

文章进一步说明了如何将人工智能用于填空式任务，例如完成代码支架和修复构建错误。它还展示了人工智能在生成模拟以测试各种场景方面的实用性。在最初的后端实现遇到困难之后，对视图模型的重组对于成功的人工智能辅助至关重要。最后一步涉及使用`UpdateController`连接后端和前端。在整个过程中，桥本经常润色和改进人工智能生成的代码。

---

## 5. AMD和索尼PS6芯片组旨在重新思考当前图形管线。

**原文标题**: AMD and Sony's PS6 chipset aims to rethink the current graphics pipeline

**原文链接**: [https://arstechnica.com/gaming/2025/10/amd-and-sony-tease-new-chip-architecture-ahead-of-playstation-6/](https://arstechnica.com/gaming/2025/10/amd-and-sony-tease-new-chip-architecture-ahead-of-playstation-6/)

文章探讨了“紫水晶计划”，这是索尼和AMD之间的一项联合工程，旨在为未来的PlayStation主机（可能是PS6）开发一种新的芯片组。该计划旨在重新思考当前的图形渲染管线并提高效率，而不仅仅是依靠原始算力来蛮力渲染图形。

紫水晶计划专注于更高效地利用机器学习，特别是利用神经网络来支持诸如AMD的FSR和索尼的PSSR等超分辨率技术。它引入了“神经阵列”，使计算单元能够共享数据并像“单个专注的AI引擎”一样运作，一次处理更大的屏幕区域，从而实现对屏幕视觉效果更广泛的机器学习增强。

该项目还通过实施专用的“辐射核心”来处理光线追踪中的低效率问题，从而释放CPU和GPU用于传统的着色器计算。“辐射核心”负责光线遍历。此外，紫水晶计划还通过“通用压缩”系统来解决GPU内存带宽限制问题，旨在将有效带宽提高到超过其理论规格。

虽然该项目仍处于早期阶段，并且没有演示，但它旨在提高实时图形的真实感，让我们得以一窥索尼和AMD在推动游戏技术边界方面的优先事项。

---

## 6. 透过照片看建造中的世界贸易中心，1966-1979

**原文标题**: The World Trade Center under construction through photos, 1966-1979

**原文链接**: [https://rarehistoricalphotos.com/twin-towers-construction-photographs/](https://rarehistoricalphotos.com/twin-towers-construction-photographs/)

本文详细介绍了世界贸易中心的概念构思、建造过程以及最终的覆灭。该项目由戴维·洛克菲勒推动，旨在通过一个大型贸易设施和城市更新计划来振兴曼哈顿下城，解决城市衰败问题。纽约和新泽西港务局负责开发该建筑群，通过选择“无线电街”地块，克服了最初关于选址的分歧。建筑师山崎实，以其现代而又敏感的设计而闻名，被选中，但他的作品受到了赞扬和批评。

施工始于1966年，于1972年竣工，采用了如地下连续墙等开创性的工程技术。该项目需要大规模的挖掘，沿哈德逊河创造了新的土地。双子塔提供了大量的办公空间、零售机会和一个重要的交通枢纽。建造过程规模宏大，雇佣了数千人，但不幸的是导致了60人死亡。

除了数据之外，双子塔成为纽约市生活中不可或缺的一部分，为5万人提供了工作场所，并吸引了无数游客。它们在1993年遭遇了一次恐怖袭击，但最终在2001年9月11日被摧毁，当时恐怖分子驾驶飞机撞向了两座大楼，导致其灾难性的倒塌。本文重点介绍了导致其毁灭的渐进式倒塌机制，并使用1966-1979年的照片详细介绍了世贸中心的建造过程。

---

## 7. 超能力：我在2025年10月如何使用编码智能体

**原文标题**: Superpowers: How I'm using coding agents in October 2025

**原文链接**: [https://blog.fsck.com/2025/10/09/superpowers/](https://blog.fsck.com/2025/10/09/superpowers/)

2025年10月，作者Jesse正在使用“超能力”（Superpowers），这是一个由Claude Code 2.0.13中的“技能”（skills）驱动的编码代理系统。他开发“超能力”是为了系统化流程并更好地指导他的AI助手。“超能力”的核心是“技能”的概念，类似于增强代理能力的模块化功能。

技能在markdown文件中定义，并由代理发现，从而实现自我改进和知识获取。工作流程遵循“头脑风暴 -> 计划 -> 执行”的循环，自动创建git工作树以进行并行任务。然后，Claude使用RED/GREEN TDD将任务分配给子代理进行实施和代码审查。

一个关键方面是教Claude如何从编程书籍等资源中创建新技能。该过程包括在压力场景下使用子代理测试新技能，灵感来自说服原则。例如，测试代理判断是立即解决问题还是首先检查是否存在相应技能。该系统结合了权威和稀缺性等说服原则，以确保可靠性。

作者强调，LLM对说服原则很敏感，这些原则可用于改进工程实践，而不仅仅是破解模型。他还使用该系统从过去的对话中提取记忆，挖掘其中的技能，然后对这些技能进行压力测试。

目前还有两个关键功能正在开发中：一个与他人分享“超能力”的系统，以及记忆系统的完全集成。作者鼓励用户安装和测试“超能力”，报告错误并贡献新技能。

---

## 8. 测试来自 datablocks.dev 的两块 18TB 白标 SATA 硬盘

**原文标题**: Testing two 18 TB white label SATA hard drives from datablocks.dev

**原文链接**: [https://ounapuu.ee/posts/2025/10/06/datablocks-white-label-drives/](https://ounapuu.ee/posts/2025/10/06/datablocks-white-label-drives/)

这篇博文详细介绍了作者测试从datablocks.dev（ServerPartDeals的欧洲替代品）购买的两个18 TB白标SATA硬盘的经验。由于全SSD设置带来的“存储焦虑”以及SSD价格上涨，作者开始探索硬盘，并发现datablocks.dev的白标产品因其价格低于翻新硬盘而颇具吸引力，尽管存在轻微的外观瑕疵。

作者选择18 TB硬盘以便于替换为容易获得的WD Elements/My Book硬盘。收到包装完好的硬盘后，他们使用`badblocks`进行了彻底格式化，显示写入速度范围为275 MB/s到123 MB/s。初始SMART数据显示令人满意，表明开机时间较短。

作者认识到7200 RPM硬盘带来的噪音，便将其与SSD集成到分层存储系统中。虽然在备份期间观察到iowait增加，但总体日常性能影响很小。这些硬盘通过USB 3.0使用WD Elements/My Book适配器连接。

功耗增加了10-20W，但仍可接受。运行期间温度保持凉爽（38-42°C）。作者对总体情况表示满意，并预计硬盘至少可以使用5年，并计划主动更换一块硬盘以减轻潜在的存储池故障。他们强调了由于盘片旋转速度和内圈位置导致硬盘末端性能较慢。

---

## 9. FreeBSD 的 Windows 子系统

**原文标题**: Windows Subsystem for FreeBSD

**原文链接**: [https://github.com/BalajeS/WSL-For-FreeBSD](https://github.com/BalajeS/WSL-For-FreeBSD)

适用于 FreeBSD 的 Windows 子系统 (WSFB) 是一个实验性项目，旨在以最小的 FreeBSD 基本系统修改，在 Linux 版 Windows 子系统 2 (WSL2) 中原生运行 FreeBSD。它利用 WSL2 的开源组件来促进 FreeBSD 在 Windows 中的无缝运行。主要目标是使 FreeBSD 能够在 WSL2 架构上原生执行，最大程度地减少 FreeBSD 代码的更改，并将改进贡献回开源项目。

目前，FreeBSD 可以在 WSL2 中成功启动，并且基本功能已可运行。正在进行的工作重点是增强网络、I/O 和进程管理能力。路线图包括完整的控制台支持、网络、用户模式实用程序和集成，以及全面的文档。

鼓励通过反馈、测试结果、错误报告和讨论进行贡献。该项目在开源许可证（待定）下运作。免责声明强调 WSFB 是一个个人实验性项目，与 Microsoft 或 FreeBSD/FreeBSD 基金会无关，用户应谨慎操作。

---

## 10. 使用 C 从零开始构建 JavaScript 运行时

**原文标题**: Building a JavaScript Runtime from Scratch using C

**原文链接**: [https://devlogs.xyz/blog/building-a-javaScript-runtime](https://devlogs.xyz/blog/building-a-javaScript-runtime)

本文概述了一个使用C语言从头构建JavaScript运行时的项目。重点是通过“开发日志”提供幕后视角，深入了解开发过程。这意味着本文将以一系列按时间顺序排列的条目形式呈现，详细介绍创建功能性JavaScript环境所面临的挑战、解决方案和取得的进展。

主要目的是记录创建JavaScript运行时所涉及的复杂性，可能涵盖以下领域：

*   **解析JavaScript代码：** 实现一个解析器来理解语法。
*   **抽象语法树 (AST) 生成：** 将解析后的代码转换为AST表示形式。
*   **执行引擎：** 构建一个解释或编译AST的机制。
*   **垃圾回收：** 自动管理内存的分配和释放。
*   **标准库实现：** 提供内置函数和对象，如`console.log`。
*   **处理JavaScript的动态特性：** 动态处理类型和作用域。

“开发日志”的形式表明了一种实用、动手的方法，提供了对作者决策过程、调试技术以及项目进展过程中的迭代改进的见解。读者可以了解到实现中使用的特定工具、库（如果有）和架构选择。本质上，本文是一项重大软件工程工作的开发日记。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 2 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 3 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 4 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 5 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 6 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 7 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 8 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 9 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 10 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 11 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 12 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 13 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 14 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 15 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 16 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 17 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 18 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 19 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 20 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 21 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 22 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 23 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 24 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 25 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 26 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 27 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 28 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 29 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 30 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 31 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 32 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 33 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 34 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 35 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 36 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 37 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 38 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 39 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 40 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 41 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 42 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 43 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 44 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 45 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 46 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 47 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 48 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 49 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 50 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 51 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 52 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 53 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 54 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 55 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 56 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 57 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 58 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 59 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 60 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 61 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 62 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 63 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 64 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 65 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 66 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 67 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 68 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 69 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 70 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 71 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 72 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 73 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 74 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 75 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 76 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 77 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 78 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 79 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 80 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 81 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 82 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 83 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 84 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 85 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 86 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 87 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 88 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 89 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 90 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 91 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 92 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 93 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 94 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 95 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 96 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 97 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 98 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 99 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 100 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 101 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 102 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 103 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 104 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 105 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 106 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 107 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 108 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 109 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 110 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 111 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 112 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 113 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 114 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 115 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 116 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 117 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 118 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 119 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 120 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 121 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 122 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 123 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 124 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 125 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 126 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 127 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 128 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 129 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 130 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 131 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 132 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 133 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 134 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 135 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 136 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 137 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 138 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 139 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 140 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 141 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 142 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 143 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 144 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 145 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 146 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 147 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 148 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 149 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 150 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 151 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 152 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 153 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 154 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 155 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 156 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 157 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 158 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 159 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 160 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 161 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 162 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 163 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 164 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 165 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 166 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 167 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 168 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 169 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 170 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 171 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 172 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 173 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 174 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 175 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 176 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 177 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 178 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 179 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 180 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 181 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 182 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 183 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 184 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 185 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 186 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 187 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 188 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 189 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 190 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 191 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 192 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 193 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 194 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 195 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 196 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 197 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 198 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 199 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 200 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 201 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 202 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 203 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 204 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 205 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 206 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
