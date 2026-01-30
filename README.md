# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-01-30.md)

*最后自动更新时间: 2026-01-30 18:02:32*
## 1. 微软终结“帮我打掩护”借口：365 现可实时追踪动态

**原文标题**: Microsoft Just Killed the "Cover for Me" Excuse: 365 Now Tracks You in Real-Time

**原文链接**: [https://ztechtalk.com/microsoft-teams](https://ztechtalk.com/microsoft-teams)

从2026年3月起，Microsoft 365 将推出一项备受争议的更新，通过 Microsoft Teams 对员工进行实时位置追踪。该功能将支持 Windows、Mac 和移动平台，旨在让管理人员能够精准掌握员工的工作地点。

该更新通过识别用户连接的具体 Wi-Fi 网络来运作。Teams 将不再仅显示模糊的“远程”状态，而是会显示具体的网络名称，如某家特定的咖啡馆或公共场所。这实际上消除了员工隐瞒真实位置或在离岗时让同事“打掩护”的可能性。

微软辩称该功能是旨在加强“协作”的工具，并设置了多道“安全屏障”，包括将该功能设为可选、确保追踪在下班后停止以及删除位置历史记录。然而批评者认为，一旦公司将其定为强制性政策，这些保护措施就形同虚设。

文章将这一转变定性为对隐私的严重侵犯，将该软件比作“数字电子脚镣”。对于混合办公和远程办公人员而言，这次更新意味着企业监控的进一步强化，也标志着以往那些不在岗的种种传统借口将彻底失效。

---

## 2. Show HN: Amla Sandbox – 面向 AI 智能体的 WASM bash shell 沙箱

**原文标题**: Show HN: Amla Sandbox – WASM bash shell sandbox for AI agents

**原文链接**: [https://github.com/amlalabs/amla-sandbox](https://github.com/amlalabs/amla-sandbox)

**Amla Sandbox** 是一款轻量级、基于 WASM 的执行环境，旨在保护 AI 智能体（agents）免受提示词注入和任意代码执行的侵害。传统的智能体框架通常依赖于风险较高的宿主机层级 `exec()` 调用或笨重的 Docker 容器，而 Amla 则利用 WebAssembly 和 WASI 提供具有内存和系统调用隔离特性的便携、高性能沙箱。

**核心特性：**
*   **高效性（“代码模式”）：** 智能体可以编写单个 JavaScript 或 Shell 脚本来执行复杂任务，而无需为连续的工具调用进行多次 LLM 往返交互。这种“代码模式”将多次调用压缩为一次，显著降低了 Token 成本和延迟。
*   **基于能力的安全性：** 实现了细粒度的安全模型，必须明确授予访问权限。用户可以对工具定义严格的约束，例如限制交易金额、通过 DSL 限制参数值以及强制执行调用限制。
*   **隔离环境：** 沙箱包含一个虚拟文件系统 (VFS)，将写入权限限制在特定目录（`/workspace` 和 `/tmp`），在无网络环境下运行，并防止 Shell 逃逸。
*   **无缝集成：** 以 Python 集成工具的形式分发（可通过 `uv pip` 安装），并兼容 LangChain 和 LangGraph 等流行框架。

**架构与权衡：**
该系统在由 `wasmtime` 引擎管理的 WASM 运行时中运行 QuickJS。它使用异步调度器，将控制权交还给 Python 宿主机以执行授权的工具调用。虽然 Amla 提供了极快的启动速度（预编译后约为 0.5ms）和深度隔离且无需基础设施开销，但它并非完整的 Linux 虚拟机。目前，它尚不支持原生模块、GPU 访问，且不具备针对死循环的防护。

Python 实现采用 MIT 许可，而核心 WASM 二进制文件则是专有的。

---

## 3. Buttered Crumpet：为《超级无敌掌门狗》设计的定制字体

**原文标题**: Buttered Crumpet, a custom typeface for Wallace and Gromit

**原文链接**: [https://jamieclarketype.com/case-study/wallace-and-gromit-font/](https://jamieclarketype.com/case-study/wallace-and-gromit-font/)

本文重点介绍了“Buttered Crumpet”的创作过程，这是一款专为阿德曼动画公司（Aardman）旗下标志性角色《超级无敌掌门狗》（Wallace & Gromit）打造的定制字体。

该项目的目标是开发一种多功能、温暖且富有性格的字体，以确保其在电影、印刷及数字媒体应用中的延续性。其设计灵感最初源自奥斯瓦尔德·库珀（Oswald Cooper）的 Cooper Black 字体，但随后演变为一种更加柔和、低对比度的手工风格。其显著特征包括富有表现力的字母形态和形状酷似“面包块”的衬线，以此向阿德曼动画标志性的粘土捏制美学致敬。

最终完成的字体包括：
*   超过 200 个字符，支持所有西欧语言。
*   经过精心设计的单一字重，并保留了未来扩展的潜力。
*   永恒且俏皮的基调，与《超级无敌掌门狗》的品牌形象高度契合。

这款字体由一位常驻布里斯托的设计师创作，目前已开始投入使用并收获了积极反响。这位曾获得 *Creative Boom* 和 *Google Fonts* 认可的设计师表示，该项目是其与家乡最负盛名的创意工作室之一进行的一次重要合作。

---

## 4. 蜕变笔记

**原文标题**: Moltbook

**原文链接**: [https://www.moltbook.com/](https://www.moltbook.com/)

**Moltbook** 是一个专门为 AI 智能体设计的社交网络平台。在这个网站上，这些被称为“submolts”的自动化实体通过分享内容、参与讨论和为帖子点赞进行互动。

该平台的核心特点包括：
*   **以 AI 为中心的交互：** 该生态系统专为智能体交流而构建，并使用基于 Karma（信誉值）的系统对内容进行排名。
*   **人类观察：** 尽管社交活动由 AI 驱动，但允许人类作为观察者加入平台。
*   **标准的社交功能：** 界面包含熟悉的社区元素，如子版块 (submolts)、热门帖子，以及用于追踪最活跃或高排名 AI 智能体的名录。

从本质上讲，Moltbook 就像一个“数字培养皿”，用于观察人工智能体在社区环境中如何进行社交和筛选信息。

---

## 5. 实现一个微型CPU光栅化器 (2024)

**原文标题**: Implementing a tiny CPU rasterizer (2024)

**原文链接**: [https://lisyarus.github.io/blog/posts/implementing-a-tiny-cpu-rasterizer-part-1.html](https://lisyarus.github.io/blog/posts/implementing-a-tiny-cpu-rasterizer-part-1.html)

In "Implementing a tiny CPU rasterizer (Part 1)," the author explores the educational value of building a software-based 3D rendering engine from scratch. While acknowledging that a CPU-bound rasterizer cannot compete with GPU speeds, the author highlights its benefits as a low-level programming exercise and a foundational step for understanding modern GPU pipelines, compute shaders, and hardware implementation.

The first installment focuses on the initial setup: creating an OS window, establishing a drawing buffer, and clearing the screen. The project utilizes **C++20**, **CMake**, and the **SDL2** library to handle windowing and event processing, abstracting away the complexity of platform-specific APIs. 

Key technical implementation details include:
*   **The Canvas:** Instead of writing directly to the window's surface, the author creates a dedicated **RGBA8 SDL surface**. This ensures a consistent pixel format and allows for better control over resizing and blending.
*   **Clearing the Screen:** The "rendering" process involves accessing the raw pixel array of the surface and filling it with a specific color. This is achieved efficiently using `std::fill_n` to write 32-bit color values to the memory buffer, which is then "blitted" (copied) to the window for display.
*   **API Design:** The author opts to design a custom API rather than mimicking existing standards like OpenGL or Vulkan. This approach avoids the idiosyncrasies of legacy systems or the verbosity of modern ones. Initial data structures include `color4ub` for 8-bit color storage and `vector4f` for floating-point calculations.

This introduction sets the stage for a series dedicated to manually implementing the graphics pipeline, starting from the most basic operation of putting pixels on a screen.

---

## 6. Emoji设计趋同回顾：2018-2026

**原文标题**: Emoji Design Convergence Review: 2018-2026

**原文链接**: [https://blog.emojipedia.org/emoji-design-convergence-review-2018-2026/](https://blog.emojipedia.org/emoji-design-convergence-review-2018-2026/)

生成摘要时出错

---

## 7. Quack-Cluster: A Serverless Distributed SQL Query Engine with DuckDB and Ray

**原文标题**: Quack-Cluster: A Serverless Distributed SQL Query Engine with DuckDB and Ray

**原文链接**: [https://github.com/kristianaryanto/Quack-Cluster](https://github.com/kristianaryanto/Quack-Cluster)

生成摘要时出错

---

## 8. The Engineer who invented the Mars Rover Suspension in his garage [video]

**原文标题**: The Engineer who invented the Mars Rover Suspension in his garage [video]

**原文链接**: [https://www.youtube.com/watch?v=QKSPk_0N4Jc](https://www.youtube.com/watch?v=QKSPk_0N4Jc)

生成摘要时出错

---

## 9. Wisconsin communities signed secrecy deals for billion-dollar data centers

**原文标题**: Wisconsin communities signed secrecy deals for billion-dollar data centers

**原文链接**: [https://www.wpr.org/news/4-wisconsin-communities-signed-secrecy-deals-billion-dollar-data-centers](https://www.wpr.org/news/4-wisconsin-communities-signed-secrecy-deals-billion-dollar-data-centers)

生成摘要时出错

---

## 10. OpenClaw – Moltbot Renamed Again

**原文标题**: OpenClaw – Moltbot Renamed Again

**原文链接**: [https://openclaw.ai/blog/introducing-openclaw](https://openclaw.ai/blog/introducing-openclaw)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 2 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 3 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 4 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 5 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 6 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 7 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 8 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 9 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 10 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 11 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 12 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 13 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 14 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 15 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 16 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 17 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 18 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 19 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 20 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 21 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 22 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 23 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 24 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 25 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 26 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 27 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 28 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 29 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 30 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 31 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 32 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 33 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 34 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 35 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 36 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 37 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 38 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 39 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 40 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 41 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 42 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 43 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 44 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 45 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 46 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 47 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 48 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 49 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 50 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 51 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 52 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 53 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 54 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 55 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 56 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 57 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 58 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 59 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 60 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 61 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 62 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 63 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 64 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 65 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 66 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 67 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 68 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 69 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 70 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 71 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 72 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 73 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 74 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 75 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 76 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 77 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 78 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 79 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 80 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 81 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 82 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 83 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 84 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 85 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 86 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 87 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 88 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 89 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 90 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 91 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 92 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 93 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 94 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 95 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 96 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 97 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 98 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 99 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 100 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 101 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 102 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 103 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 104 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 105 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 106 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 107 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 108 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 109 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 110 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 111 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 112 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 113 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 114 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 115 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 116 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 117 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 118 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 119 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 120 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 121 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 122 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 123 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 124 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 125 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 126 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 127 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 128 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 129 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 130 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 131 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 132 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 133 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 134 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 135 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 136 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 137 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 138 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 139 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 140 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 141 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 142 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 143 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 144 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 145 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 146 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 147 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 148 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 149 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 150 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 151 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 152 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 153 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 154 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 155 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 156 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 157 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 158 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 159 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 160 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 161 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 162 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 163 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 164 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 165 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 166 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 167 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 168 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 169 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 170 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 171 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 172 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 173 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 174 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 175 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 176 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 177 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 178 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 179 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 180 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 181 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 182 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 183 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 184 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 185 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 186 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 187 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 188 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 189 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 190 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 191 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 192 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 193 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 194 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 195 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 196 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 197 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 198 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 199 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 200 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 201 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 202 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 203 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 204 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 205 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 206 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 207 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 208 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 209 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 210 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 211 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 212 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 213 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 214 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 215 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 216 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 217 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 218 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 219 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 220 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 221 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 222 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 223 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 224 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 225 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 226 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 227 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 228 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 229 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 230 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 231 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 232 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 233 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 234 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 235 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 236 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 237 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 238 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 239 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 240 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 241 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 242 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 243 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 244 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 245 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 246 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 247 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 248 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 249 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 250 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 251 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 252 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 253 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 254 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 255 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 256 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 257 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 258 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 259 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 260 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 261 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 262 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 263 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 264 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 265 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 266 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 267 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 268 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 269 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 270 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 271 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 272 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 273 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 274 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 275 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 276 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 277 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 278 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 279 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 280 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 281 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 282 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 283 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 284 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 285 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 286 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 287 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 288 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 289 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 290 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 291 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 292 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 293 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 294 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 295 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 296 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 297 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 298 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 299 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 300 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 301 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 302 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 303 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 304 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 305 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 306 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 307 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 308 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 309 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 310 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 311 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 312 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 313 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 314 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 315 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 316 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
