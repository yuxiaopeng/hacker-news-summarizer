# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-11-10.md)

*最后自动更新时间: 2025-11-10 17:55:06*
## 1. Asus Ascent GX10

**原文标题**: Asus Ascent GX10

**原文链接**: [https://www.asus.com/networking-iot-servers/desktop-ai-supercomputer/ultra-small-ai-supercomputers/asus-ascent-gx10/](https://www.asus.com/networking-iot-servers/desktop-ai-supercomputer/ultra-small-ai-supercomputers/asus-ascent-gx10/)

生成摘要时出错

---

## 2. 微服务？不，模块化才是关键。

**原文标题**: Microservices? No, modularity is what matters

**原文链接**: [https://binaryigor.com/modular-monolith-and-microservices-modularity-is-what-truly-matters.html](https://binaryigor.com/modular-monolith-and-microservices-modularity-is-what-truly-matters.html)

本文倡导在软件设计中优先考虑模块化，无论选择单体架构还是微服务架构。模块化被定义为将系统划分为具有清晰API的独立、逻辑模块，它带来了诸如改进组织、理解、资源利用、可重用性和可测试性等好处。

作者使用“奇闻轶事笔记”系统为例，将其拆分为“用户”、“名言”和“笔记”模块来阐述这一概念。关键是首先解决领域理解和功能需求，然后考虑影响实现的非功能性因素。

本文还承认现实世界软件开发中知识不完整的挑战。它建议在高不确定性的情况下采用模块化单体策略，因为与微服务相比，在需求不稳定的情况下，它可以实现更低成本的重新设计。

最后，作者探讨了实际的实施策略，从最简单的开始：将模块组织为具有明确通信约定的文件夹（例如，用于共享接口的“_contracts”文件夹）。一种更严格的方法是使用独立版本控制和可部署的模块，即使只有一个部署单元，也能提供更大的隔离和透明的依赖关系。文章强调，最佳选择取决于具体的上下文、团队纪律以及对领域的确定性。

---

## 3. 启动 HN：Hypercubic (YC F25) – 面向 COBOL 和大型机的 AI

**原文标题**: Launch HN: Hypercubic (YC F25) – AI for COBOL and Mainframes

**原文链接**: [https://www.hypercubic.ai/](https://www.hypercubic.ai/)

Hypercubic：利用人工智能理解并保存复杂大型机系统和COBOL代码中的知识，解决资深开发者退休导致专业知识流失的关键问题。其核心产品为HyperTwin和HyperDocs。HyperTwin通过创建主题专家数字孪生，记录调试过程和操作流程，实现全天候访问，从而捕获机构知识。HyperDocs自动从大型机操作和COBOL代码库中创建结构化文档，提取系统知识并使其与代码库同步。

Hypercubic的混合方法结合了确定性人工智能和生成式人工智能，确保准确性、可审计性和可信度，从而降低与人工智能幻觉相关的风险。这有助于实现无与伦比的风险缓解，防止系统故障和停机，同时通过生产就绪的知识资产加速实现价值。该解决方案可与COBOL和JCL等传统语言互操作。

Hypercubic致力于解决金融服务、零售、航空航天、能源、政府和制造业等行业的知识保留难题。他们帮助这些行业确保核心系统、供应链、工程智慧、电网控制、公共服务和制造流程的关键知识。该平台提供全面的AI驱动现代化，通过捕获数十年的机构知识来降低风险。Hypercubic现提供平台早期访问权限。

---

## 4. Zig (及其设计选择)

**原文标题**: Zig (and the Design Choices Within)

**原文链接**: [https://blueberrywren.dev/blog/on-zig/](https://blueberrywren.dev/blog/on-zig/)

This article is a critical opinion piece on the Zig programming language, focusing on its design choices and their implications. The author, with significant experience in programming language design, expresses concerns about several aspects of Zig.

Chief among these is Zig's lack of memory safety, deemed a significant flaw in a modern language. The author presents data suggesting a higher incidence of crashes in Zig projects compared to projects in memory-safe languages like Rust and even those using JavaScript runtimes like Deno.

The article criticizes Zig's comptime generics for lacking standardization and potentially hindering readability. The verbosity of casting and the unpredictable behavior of float-to-int conversions are also highlighted. Issues with Result Location Semantics (RLS), particularly unexpected behavior when assigning struct members, are explored. The removal of Pointer Reference Optimization (PRO) is viewed as a missed opportunity.

The author acknowledges the ongoing efforts to improve the Zig compiler's speed and tooling but finds the current build system confusing and the unofficial language server (ZLS) subpar. The absence of use-after-realloc detection is a significant concern.

The author also points out the language design choices around undefined behavior, the prohibition of tabs in comments and strings, the limited iteration methods, and the absence of warnings (everything is an error). Finally, they address negative experiences within the Zig community, characterized by unhelpful advice and resistance to alternative approaches.


---

## 5. ClickHouse收购LibreChat：开源Agentic数据栈

**原文标题**: ClickHouse acquires LibreChat: The open-source Agentic Data Stack

**原文链接**: [https://clickhouse.com/blog/librechat-open-source-agentic-data-stack](https://clickhouse.com/blog/librechat-open-source-agentic-data-stack)

生成摘要时出错

---

## 6. 使用iCE40 FPGA实现的有趣的SPI路由

**原文标题**: Interesting SPI Routing with iCE40 FPGAs

**原文链接**: [https://danielmangum.com/posts/spi-routing-ice40-fpga/](https://danielmangum.com/posts/spi-routing-ice40-fpga/)

This article explores the interesting SPI routing design in the Fomu FPGA development board, which uses a Lattice Semiconductor iCE40 UltraPlus 5K FPGA. Unlike many FPGA boards that use a USB-to-Serial IC for configuration, the Fomu implements its USB core in RTL (using ValentyUSB), presenting a challenge for initial configuration.

The iCE40 can be configured via SRAM or non-volatile configuration memory (NVCM), or through an external SPI flash chip (GD25Q16CEIGR) for persistent storage, which is the approach used in the Fomu. The article highlights the challenge of having both the FPGA and flash IC accessible via SPI test points, given that the iCE40 can act as both an SPI controller (when booting from flash) and a peripheral (when being directly programmed).

The author investigates how the Fomu handles this dual functionality, noting that it cleverly uses the GD25Q16CEIGR flash IC's "Deep Power-Down" mode (activated by SPI commands 0xb9 and 0xab), rather than asserting the HOLD pin, to isolate the flash IC from SPI traffic when directly programming the iCE40. This is a contrast to other boards like the iCEstick, which explicitly prevents direct iCE40 programming. The Deep Power-Down method reduces the number of required test points, requiring only seven. The author concludes by highlighting how the unique capabilities of FPGAs can lead to innovative board design decisions.


---

## 7. 意想不到的人形之物

**原文标题**: Unexpected Things that are People

**原文链接**: [https://bengoldhaber.substack.com/p/unexpected-things-that-are-people](https://bengoldhaber.substack.com/p/unexpected-things-that-are-people)

无法访问文章链接。

---

## 8. 姿态动画器 – 一款开源的SVG角色动画工具 (2020)

**原文标题**: Pose Animator – An open source tool to bring SVG characters to life (2020)

**原文链接**: [https://blog.tensorflow.org/2020/05/pose-animator-open-source-tool-to-bring-svg-characters-to-life.html](https://blog.tensorflow.org/2020/05/pose-animator-open-source-tool-to-bring-svg-characters-to-life.html)

本文介绍 Pose Animator，这是一个使用 TensorFlow.js 构建的开源工具，它允许用户通过使用网络摄像头的实时动作捕捉，在浏览器中让 SVG 角色栩栩如生。该工具由 Shan Huang 开发，利用 PoseNet 和 FaceMesh 模型检测人体姿势和面部表情，然后将这些动作转换为 2D 矢量插图。

Pose Animator 采用基于骨骼的动画方法，使用表面（SVG 路径）和基于 PoseNet 和 FaceMesh 关键点的分层骨骼结构来定义角色。该工具采用线性混合蒙皮（LBS）根据骨骼运动变形 SVG 路径，从而提供细致而富有表现力的动画。

绑定过程包括解析 SVG 文件、计算骨骼对矢量段的影响、基于 ML 模型输出实时更新骨骼位置，以及最终计算新的矢量段位置。运动稳定技术，包括基于置信度分数的插值和裁剪，用于减少抖动并提高动画的流畅度。

本文还讨论了未来的改进方向，例如增强的网格绑定算法、浏览器内编辑功能（如蒙皮权重绘制）以及对栅格图像的支持。用户可以使用现有的角色尝试 Pose Animator，或者上传他们自己的 SVG 设计，并鼓励使用 #PoseAnimator 标签分享他们的创作。源代码可在 GitHub 上找到。

---

## 9. 警察可以获取你的私人在线数据

**原文标题**: Cops Can Get Your Private Online Data

**原文链接**: [https://www.eff.org/deeplinks/2025/06/how-cops-can-get-your-private-online-data](https://www.eff.org/deeplinks/2025/06/how-cops-can-get-your-private-online-data)

生成摘要时出错

---

## 10. 开始去应用化

**原文标题**: Time to Start De-Appling

**原文链接**: [https://heatherburns.tech/2025/11/10/time-to-start-de-appling/](https://heatherburns.tech/2025/11/10/time-to-start-de-appling/)

希瑟·伯恩斯的文章讨论了英国政府通过技术能力通知（TCN）要求访问苹果iCloud数据的事件，尤其影响了苹果的端到端加密功能——高级数据保护（ADP）。

由于《调查权力法案》，苹果正在从英国撤回ADP，要求启用ADP的用户手动禁用该功能才能保留其iCloud帐户。英国新用户将无法启用ADP。这意味着10个iCloud数据类别（iCloud备份、iCloud Drive、照片、备忘录、提醒事项、Safari书签、Siri捷径、语音备忘录、钱包凭证和Freeform）将不再在英国享受端到端加密的保护。

作者建议英国用户将这些数据从iCloud迁移到安全的端到端加密服务，并推荐Proton、Standard Notes、Obsidian或Joplin作为替代方案。她强调在迁移后需要清除iCloud上的数据。

文章强调，第一份TCN不仅限于ADP数据，而是寻求访问全球所有iCloud数据，这引发了对信任苹果产品堆栈存储敏感信息（包括密码）的担忧。第二份TCN专门针对英国公民的数据，引发了关于苹果将如何实施国籍检查的问题。

作者鼓励读者，特别是那些在英国以外的读者，如果可用的话，激活ADP。她敦促大家进行“去谷歌化”、“去苹果化”和“去美国堆栈化”，以提高安全性。她强调了主流媒体缺乏相关报道，以及依赖于总部设在具有不利法律的国家/地区的公司所存在的潜在危险。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 2 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 3 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 4 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 5 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 6 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 7 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 8 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 9 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 10 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 11 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 12 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 13 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 14 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 15 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 16 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 17 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 18 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 19 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 20 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 21 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 22 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 23 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 24 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 25 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 26 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 27 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 28 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 29 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 30 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 31 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 32 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 33 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 34 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 35 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 36 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 37 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 38 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 39 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 40 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 41 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 42 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 43 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 44 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 45 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 46 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 47 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 48 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 49 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 50 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 51 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 52 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 53 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 54 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 55 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 56 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 57 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 58 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 59 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 60 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 61 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 62 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 63 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 64 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 65 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 66 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 67 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 68 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 69 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 70 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 71 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 72 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 73 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 74 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 75 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 76 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 77 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 78 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 79 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 80 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 81 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 82 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 83 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 84 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 85 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 86 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 87 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 88 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 89 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 90 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 91 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 92 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 93 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 94 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 95 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 96 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 97 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 98 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 99 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 100 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 101 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 102 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 103 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 104 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 105 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 106 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 107 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 108 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 109 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 110 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 111 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 112 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 113 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 114 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 115 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 116 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 117 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 118 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 119 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 120 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 121 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 122 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 123 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 124 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 125 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 126 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 127 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 128 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 129 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 130 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 131 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 132 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 133 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 134 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 135 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 136 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 137 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 138 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 139 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 140 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 141 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 142 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 143 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 144 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 145 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 146 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 147 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 148 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 149 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 150 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 151 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 152 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 153 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 154 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 155 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 156 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 157 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 158 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 159 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 160 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 161 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 162 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 163 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 164 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 165 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 166 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 167 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 168 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 169 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 170 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 171 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 172 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 173 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 174 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 175 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 176 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 177 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 178 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 179 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 180 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 181 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 182 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 183 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 184 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 185 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 186 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 187 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 188 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 189 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 190 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 191 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 192 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 193 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 194 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 195 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 196 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 197 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 198 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 199 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 200 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 201 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 202 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 203 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 204 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 205 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 206 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 207 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 208 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 209 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 210 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 211 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 212 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 213 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 214 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 215 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 216 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 217 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 218 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 219 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 220 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 221 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 222 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 223 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 224 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 225 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 226 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 227 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 228 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 229 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 230 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 231 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 232 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 233 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 234 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 235 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
