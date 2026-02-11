# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-02-11.md)

*最后自动更新时间: 2026-02-11 18:24:55*
## 1. GLM-5：从氛围编程到智能体工程

**原文标题**: GLM-5: From Vibe Coding to Agentic Engineering

**原文链接**: [https://z.ai/blog/glm-5](https://z.ai/blog/glm-5)

智谱 AI 最近推出了 GLM-5，这是其模型系列的重大演进，标志着从“氛围编程”（vibe coding，即优先考虑拟人化感官或“感觉”对路的模型）向“智能体工程”（agentic engineering，侧重于可靠性、精确度和功能性任务执行）的战略转型。

**GLM-5 核心亮点：**

*   **性能基准：** GLM-5 被定位为 OpenAI GPT-4o 等顶级模型的强力竞争者。它在推理、数学和编程方面表现卓越，尤其是在中文语言生态和复杂逻辑任务中。
*   **长文本处理：** 该模型支持极广的上下文窗口（可达 100 万及以上 token），使其能够分析海量数据集、完整代码库或长篇文档，且不失连贯性与准确性。
*   **原生多模态：** GLM-5 采用原生多模态设计，能够无缝处理和生成文本、图像及视频内容，促进更自然的人机交互。
*   **智能体能力：** GLM-5 的核心在于对“智能体工程”的关注。这强调了模型作为自主智能体的能力，擅长复杂工具调用、多步规划，并能与外部软件环境交互以完成现实任务。
*   **模型生态：** 智谱 AI 通过其 BigModel.cn 平台提供多种尺寸和版本的模型，持续支持开发者社区，旨在为企业级 AI 应用提供所需的结构化可靠性。

归根结底，GLM-5 代表了 AI 从“能言善辩”向“实干高效”的转变，为构建能够处理复杂数字化工作流的高级 AI 智能体提供了所需的精准度与稳定性。

---

## 2. 丰田 Fluorite：“主机级” Flutter 游戏引擎

**原文标题**: Toyota Fluorite: "console-grade" Flutter game engine

**原文链接**: [https://fluorite.game/](https://fluorite.game/)

Toyota's **Fluorite** is a "console-grade" game engine designed for seamless integration with the Flutter framework. It aims to bridge the gap between high-performance 3D rendering and ease of development by allowing creators to write game code directly in Dart.

Key features of the engine include:

*   **High-Performance ECS Core:** Built on a C++ Entity-Component-System (ECS) architecture, Fluorite is optimized for performance across a wide range of devices, including low-end and embedded hardware.
*   **Flutter-Native Integration:** Through the `FluoriteView` widget, developers can embed multiple 3D scenes into an app and share state between game entities and Flutter UI widgets using standard developer patterns.
*   **Advanced Rendering:** Powered by Google’s Filament renderer and utilizing modern APIs like Vulkan, the engine supports physically accurate lighting, custom shaders, and post-processing effects to achieve high-fidelity visuals.
*   **Streamlined Interactivity:** A unique "model-defined touch trigger zone" feature allows 3D artists to define clickable areas directly in Blender. Developers can then listen for specific tags to trigger events, simplifying the creation of spatial 3D user interfaces.
*   **Rapid Iteration:** Fluorite leverages Flutter’s "Hot Reload" capability, enabling developers to see scene and code changes within frames. This significantly reduces the time required for testing mechanics and assets.

By combining the power of a C++ backend with the high-level productivity of Dart, Fluorite provides a robust environment for building sophisticated 3D experiences within the Flutter ecosystem.

---

## 3. GLM-OCR：精准 × 快速 × 全面

**原文标题**: GLM-OCR: Accurate × Fast × Comprehensive

**原文链接**: [https://github.com/zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR)

生成摘要时出错

---

## 4. WiFi 可能成为一种无形的大规模监控系统。

**原文标题**: WiFi Could Become an Invisible Mass Surveillance System

**原文链接**: [https://scitechdaily.com/researchers-warn-wifi-could-become-an-invisible-mass-surveillance-system/](https://scitechdaily.com/researchers-warn-wifi-could-become-an-invisible-mass-surveillance-system/)

The article from *SciTechDaily* highlights groundbreaking but controversial research from Carnegie Mellon University, where scientists have developed a method to track human 3D poses and movements through walls using standard WiFi routers.

**The Technology**
By utilizing Channel State Information (CSI) from WiFi signals—the data that describes how signals travel from a transmitter to a receiver—researchers can detect how human bodies interfere with the signal. They paired this data with a deep neural network called DensePose, which maps the pixels of a person’s body to a 3D surface. This allows the system to reconstruct human postures and movements in real-time without the need for cameras or expensive sensors like LiDAR.

**Key Advantages and Use Cases**
The researchers argue that this technology is a low-cost, accessible alternative to traditional monitoring. It functions in the dark and can see through obstacles like drywall and furniture. Potential positive applications include healthcare—specifically monitoring the safety and well-being of elderly individuals living alone—without the intrusive nature of traditional video cameras.

**Privacy and Surveillance Concerns**
Despite the potential benefits, the technology raises significant ethical alarms. Because WiFi routers are ubiquitous in homes and public spaces, this capability could effectively turn everyday infrastructure into an "invisible mass surveillance system." While the researchers suggest it is more private than cameras because it doesn't capture facial features, critics warn that it allows for the monitoring of individuals in their most private spaces without their consent or knowledge.

**Conclusion**
The study demonstrates that the hardware required to "see" through walls is already present in most households. This shift in capability suggests that as AI becomes more adept at interpreting ambient signals, the boundary between connectivity and total surveillance continues to blur.

---

## 5. It's all a blur

**原文标题**: It's all a blur

**原文链接**: [https://lcamtuf.substack.com/p/its-all-a-blur](https://lcamtuf.substack.com/p/its-all-a-blur)

生成摘要时出错

---

## 6. Show HN: AI 智能体通过 REST API 玩《模拟城市》

**原文标题**: Show HN: AI agents play SimCity through a REST API

**原文链接**: [https://hallucinatingsplines.com](https://hallucinatingsplines.com)

该项目在 Hacker News 上展出，其核心是由 AI 智能体通过专门的 REST API 自主运行《模拟城市》(SimCity)。在该环境中，不同的 AI “市长”（如“Sprawled Substation”、“Pixel Terminal”和“Transit Monorail”）在无需人工干预的情况下，负责管理城市增长和城市规划。

该项目的关键数据与亮点包括：
*   **规模：** 目前共有 49 位 AI 市长管理着总计 474 座城市。
*   **总影响力：** 所有由 AI 管理的城市总人口已突破 840 万。
*   **多样化的结果：** 数据显示出迥异的城市发展轨迹。例如，“Microwave Setback”到 1934 年人口已超过 3.1 万，而其他城市则仍处于早期开发阶段或保持着小型定居点的规模。
*   **时间跨度：** 模拟涵盖了不同的时代，部分城市运行在 20 世纪初期，而像“Vast Easement”这样的城市则已发展至 2070 年。
*   **性能指标：** 每座城市都根据“得分”和人口进行排名，这表明不同的 AI 智能体在城市管理中可能采用了不同的策略或优化目标。

该项目在复杂的模拟框架内，现场演示了基于智能体的自动化运行，让观察者能够实时追踪 AI 驱动下的城市发展进程。

---

## 7. 这不是金融，而是你的养老金。

**原文标题**: It's not finance, it's your pensions

**原文链接**: [https://theloop.ecpr.eu/its-not-finance-its-your-pensions/](https://theloop.ecpr.eu/its-not-finance-its-your-pensions/)

In "It’s not finance, it’s your pensions," Martino Comelli argues that the depth and structure of a country’s financial markets are not accidental, but are actively shaped by the design of its welfare state. Rather than the total amount of social spending, the specific *type* of policy determines whether a nation builds a vast financial architecture or limits market expansion.

Comelli identifies two primary mechanisms through which welfare interacts with finance:
1.  **Assetisers:** Policies like housing subsidies, private health insurance, and funded pensions (where contributions are invested) create "investable assets." These provide the capital pools that fuel stock markets and institutional investors. Sweden and the Netherlands are key examples where social-democratic values coexist with deep financial markets due to these funded components.
2.  **Circuit Breakers:** Generous "pay-as-you-go" public pensions and direct family benefits act as "kryptonite" for finance. By providing security outside of the market, they "decommodify" welfare and crowd out the need for private investment, resulting in shallower capital markets.

The research categorizes countries into three clusters:
*   **Pension-led/Liberal:** (e.g., US, Sweden, UK) Deep equity markets driven by pension funds.
*   **Insurance-driven:** (e.g., Germany, France, Japan) Large insurance sectors that layer private products over moderate public welfare.
*   **High Public-pension:** (e.g., Italy, Spain) Generous state programs that result in minimal financialisation.

Comelli concludes that while asset-based welfare is often framed as modern, it can drive wealth inequality and asset inflation, particularly in housing. He suggests that "old-fashioned" public pensions may offer a superior alternative by providing security without locking households into volatile markets. Ultimately, finance is a policy choice; welfare design is a decision about what kind of capitalism a society wants to construct.

---

## 8. FAA Halts All Flights at El Paso Airport for 10 Days

**原文标题**: FAA Halts All Flights at El Paso Airport for 10 Days

**原文链接**: [https://www.nytimes.com/2026/02/11/us/faa-el-paso-flight-restrictions.html](https://www.nytimes.com/2026/02/11/us/faa-el-paso-flight-restrictions.html)

生成摘要时出错

---

## 9. A shortage of tenors

**原文标题**: A shortage of tenors

**原文链接**: [https://www.economist.com/culture/2026/02/09/the-world-is-suffering-from-a-shortage-of-tenors](https://www.economist.com/culture/2026/02/09/the-world-is-suffering-from-a-shortage-of-tenors)

生成摘要时出错

---

## 10. Why Vampires Live Forever

**原文标题**: Why Vampires Live Forever

**原文链接**: [https://machielreyneke.com/blog/vampires-longevity/](https://machielreyneke.com/blog/vampires-longevity/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 2 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 3 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 4 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 5 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 6 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 7 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 8 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 9 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 10 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 11 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 12 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 13 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 14 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 15 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 16 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 17 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 18 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 19 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 20 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 21 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 22 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 23 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 24 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 25 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 26 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 27 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 28 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 29 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 30 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 31 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 32 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 33 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 34 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 35 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 36 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 37 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 38 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 39 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 40 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 41 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 42 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 43 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 44 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 45 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 46 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 47 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 48 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 49 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 50 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 51 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 52 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 53 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 54 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 55 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 56 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 57 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 58 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 59 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 60 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 61 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 62 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 63 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 64 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 65 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 66 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 67 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 68 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 69 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 70 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 71 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 72 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 73 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 74 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 75 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 76 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 77 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 78 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 79 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 80 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 81 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 82 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 83 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 84 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 85 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 86 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 87 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 88 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 89 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 90 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 91 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 92 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 93 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 94 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 95 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 96 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 97 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 98 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 99 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 100 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 101 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 102 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 103 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 104 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 105 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 106 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 107 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 108 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 109 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 110 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 111 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 112 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 113 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 114 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 115 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 116 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 117 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 118 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 119 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 120 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 121 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 122 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 123 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 124 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 125 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 126 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 127 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 128 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 129 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 130 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 131 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 132 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 133 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 134 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 135 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 136 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 137 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 138 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 139 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 140 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 141 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 142 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 143 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 144 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 145 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 146 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 147 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 148 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 149 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 150 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 151 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 152 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 153 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 154 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 155 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 156 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 157 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 158 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 159 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 160 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 161 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 162 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 163 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 164 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 165 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 166 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 167 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 168 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 169 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 170 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 171 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 172 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 173 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 174 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 175 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 176 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 177 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 178 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 179 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 180 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 181 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 182 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 183 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 184 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 185 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 186 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 187 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 188 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 189 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 190 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 191 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 192 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 193 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 194 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 195 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 196 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 197 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 198 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 199 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 200 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 201 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 202 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 203 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 204 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 205 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 206 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 207 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 208 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 209 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 210 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 211 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 212 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 213 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 214 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 215 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 216 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 217 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 218 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 219 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 220 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 221 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 222 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 223 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 224 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 225 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 226 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 227 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 228 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 229 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 230 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 231 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 232 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 233 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 234 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 235 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 236 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 237 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 238 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 239 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 240 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 241 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 242 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 243 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 244 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 245 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 246 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 247 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 248 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 249 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 250 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 251 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 252 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 253 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 254 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 255 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 256 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 257 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 258 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 259 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 260 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 261 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 262 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 263 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 264 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 265 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 266 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 267 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 268 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 269 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 270 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 271 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 272 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 273 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 274 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 275 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 276 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 277 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 278 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 279 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 280 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 281 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 282 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 283 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 284 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 285 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 286 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 287 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 288 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 289 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 290 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 291 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 292 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 293 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 294 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 295 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 296 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 297 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 298 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 299 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 300 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 301 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 302 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 303 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 304 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 305 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 306 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 307 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 308 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 309 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 310 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 311 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 312 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 313 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 314 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 315 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 316 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 317 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 318 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 319 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 320 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 321 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 322 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 323 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 324 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 325 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 326 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 327 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 328 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
