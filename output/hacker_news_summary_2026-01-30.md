# Hacker News 热门文章摘要 (2026-01-30)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. The National Herbarium of Ireland digital collection of Irish plants

**原文标题**: The National Herbarium of Ireland digital collection of Irish plants

**原文链接**: [https://dri.ie/news/new-collection-in-dri-the-national-herbarium-of-ireland-digital-collection-of-irish-plants/](https://dri.ie/news/new-collection-in-dri-the-national-herbarium-of-ireland-digital-collection-of-irish-plants/)

生成摘要时出错

---

## 12. Richard Feynman Side Hustles

**原文标题**: Richard Feynman Side Hustles

**原文链接**: [https://twitter.com/carl_feynman/status/2016979540099420428](https://twitter.com/carl_feynman/status/2016979540099420428)

生成摘要时出错

---

## 13. How AI assistance impacts the formation of coding skills

**原文标题**: How AI assistance impacts the formation of coding skills

**原文链接**: [https://www.anthropic.com/research/AI-assistance-coding-skills](https://www.anthropic.com/research/AI-assistance-coding-skills)

生成摘要时出错

---

## 14. GOG: Linux "the next major frontier" for gaming as it works on a native client

**原文标题**: GOG: Linux "the next major frontier" for gaming as it works on a native client

**原文链接**: [https://www.xda-developers.com/gog-calls-linux-the-next-major-frontier-for-gaming-as-it-works-on-a-native-client/](https://www.xda-developers.com/gog-calls-linux-the-next-major-frontier-for-gaming-as-it-works-on-a-native-client/)

生成摘要时出错

---

## 15. PlayStation 2 Recompilation Project Is Absolutely Incredible

**原文标题**: PlayStation 2 Recompilation Project Is Absolutely Incredible

**原文链接**: [https://redgamingtech.com/playstation-2-recompilation-project-is-absolutely-incredible/](https://redgamingtech.com/playstation-2-recompilation-project-is-absolutely-incredible/)

生成摘要时出错

---

## 16. Pangolin (YC S25) is hiring software engineers (open-source, Go, networking)

**原文标题**: Pangolin (YC S25) is hiring software engineers (open-source, Go, networking)

**原文链接**: [https://docs.pangolin.net/careers/join-us](https://docs.pangolin.net/careers/join-us)

生成摘要时出错

---

## 17. Netflix Animation Studios Joins the Blender Development Fund as Corporate Patron

**原文标题**: Netflix Animation Studios Joins the Blender Development Fund as Corporate Patron

**原文链接**: [https://www.blender.org/press/netflix-animation-studios-joins-the-blender-development-fund-as-corporate-patron/](https://www.blender.org/press/netflix-animation-studios-joins-the-blender-development-fund-as-corporate-patron/)

生成摘要时出错

---

## 18. Lemonade Autonomous Car Insurance (With Tesla FSD Discount)

**原文标题**: Lemonade Autonomous Car Insurance (With Tesla FSD Discount)

**原文链接**: [https://www.lemonade.com/car/explained/self-driving-car-insurance/](https://www.lemonade.com/car/explained/self-driving-car-insurance/)

生成摘要时出错

---

## 19. Grid: Free, local-first, browser-based 3D printing/CNC/laser slicer

**原文标题**: Grid: Free, local-first, browser-based 3D printing/CNC/laser slicer

**原文链接**: [https://grid.space/stem/](https://grid.space/stem/)

生成摘要时出错

---

## 20. How AI Impacts Skill Formation

**原文标题**: How AI Impacts Skill Formation

**原文链接**: [https://arxiv.org/abs/2601.20245](https://arxiv.org/abs/2601.20245)

生成摘要时出错

---

## 21. Show HN: Kolibri, a DIY music club in Sweden

**原文标题**: Show HN: Kolibri, a DIY music club in Sweden

**原文链接**: [https://kolibrinkpg.com/](https://kolibrinkpg.com/)

生成摘要时出错

---

## 22. Track Your Routine – Open-source app for task management

**原文标题**: Track Your Routine – Open-source app for task management

**原文链接**: [https://github.com/MSF01/TYR](https://github.com/MSF01/TYR)

生成摘要时出错

---

## 23. Godot 4.6 Release: It's all about your flow

**原文标题**: Godot 4.6 Release: It's all about your flow

**原文链接**: [https://godotengine.org/releases/4.6/](https://godotengine.org/releases/4.6/)

生成摘要时出错

---

## 24. AGENTS.md outperforms skills in our agent evals

**原文标题**: AGENTS.md outperforms skills in our agent evals

**原文链接**: [https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals)

生成摘要时出错

---

## 25. Show HN: Cicada – A scripting language that integrates with C

**原文标题**: Show HN: Cicada – A scripting language that integrates with C

**原文链接**: [https://github.com/heltilda/cicada](https://github.com/heltilda/cicada)

生成摘要时出错

---

## 26. Retiring GPT-4o, GPT-4.1, GPT-4.1 mini, and OpenAI o4-mini in ChatGPT

**原文标题**: Retiring GPT-4o, GPT-4.1, GPT-4.1 mini, and OpenAI o4-mini in ChatGPT

**原文链接**: [https://openai.com/index/retiring-gpt-4o-and-older-models/](https://openai.com/index/retiring-gpt-4o-and-older-models/)

生成摘要时出错

---

## 27. Detecting Dementia Using Lexical Analysis: Terry Pratchett's Discworld

**原文标题**: Detecting Dementia Using Lexical Analysis: Terry Pratchett's Discworld

**原文链接**: [https://www.mdpi.com/2076-3425/16/1/94](https://www.mdpi.com/2076-3425/16/1/94)

生成摘要时出错

---

## 28. Doin' It with a 555: One Chip to Rule Them All

**原文标题**: Doin' It with a 555: One Chip to Rule Them All

**原文链接**: [https://aashvik.com/posts/555-revolution/](https://aashvik.com/posts/555-revolution/)

生成摘要时出错

---

## 29. Stargaze: SpaceX's Space Situational Awareness System

**原文标题**: Stargaze: SpaceX's Space Situational Awareness System

**原文链接**: [https://starlink.com/updates/stargaze](https://starlink.com/updates/stargaze)

生成摘要时出错

---

## 30. HumanConsumption.Live – Real-Time Global Animal Consumption Stats

**原文标题**: HumanConsumption.Live – Real-Time Global Animal Consumption Stats

**原文链接**: [https://www.humanconsumption.live/](https://www.humanconsumption.live/)

生成摘要时出错

---

## 31. The WiFi only works when it's raining (2024)

**原文标题**: The WiFi only works when it's raining (2024)

**原文链接**: [https://predr.ag/blog/wifi-only-works-when-its-raining/](https://predr.ag/blog/wifi-only-works-when-its-raining/)

生成摘要时出错

---

## 32. Flameshot

**原文标题**: Flameshot

**原文链接**: [https://github.com/flameshot-org/flameshot](https://github.com/flameshot-org/flameshot)

生成摘要时出错

---

## 33. Backseat Software

**原文标题**: Backseat Software

**原文链接**: [https://blog.mikeswanson.com/backseat-software/](https://blog.mikeswanson.com/backseat-software/)

生成摘要时出错

---

## 34. HTTP Cats

**原文标题**: HTTP Cats

**原文链接**: [https://http.cat/](https://http.cat/)

生成摘要时出错

---

## 35. My Mom and Dr. DeepSeek (2025)

**原文标题**: My Mom and Dr. DeepSeek (2025)

**原文链接**: [https://restofworld.org/2025/ai-chatbot-china-sick/](https://restofworld.org/2025/ai-chatbot-china-sick/)

生成摘要时出错

---

## 36. Two days of oatmeal reduce cholesterol level

**原文标题**: Two days of oatmeal reduce cholesterol level

**原文链接**: [https://www.uni-bonn.de/en/news/017-2026](https://www.uni-bonn.de/en/news/017-2026)

生成摘要时出错

---

## 37. Is the RAM shortage killing small VPS hosts?

**原文标题**: Is the RAM shortage killing small VPS hosts?

**原文链接**: [https://www.fourplex.net/2026/01/29/is-the-ram-shortage-killing-small-vps-hosts/](https://www.fourplex.net/2026/01/29/is-the-ram-shortage-killing-small-vps-hosts/)

生成摘要时出错

---

## 38. Software Pump and Dump

**原文标题**: Software Pump and Dump

**原文链接**: [http://tautvilas.lt/software-pump-and-dump/](http://tautvilas.lt/software-pump-and-dump/)

生成摘要时出错

---

## 39. Spacecurve: A space-filling curve playground

**原文标题**: Spacecurve: A space-filling curve playground

**原文链接**: [https://corte.si/posts/spacecurve/announce/](https://corte.si/posts/spacecurve/announce/)

生成摘要时出错

---

## 40. Project Genie: Experimenting with infinite, interactive worlds

**原文标题**: Project Genie: Experimenting with infinite, interactive worlds

**原文链接**: [https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/)

生成摘要时出错

---

## 41. Long-hidden Leonardo mural opens to the public ahead of 2026 Milan Olympics

**原文标题**: Long-hidden Leonardo mural opens to the public ahead of 2026 Milan Olympics

**原文链接**: [https://news.artnet.com/art-world/leonardo-sforza-castle-olympics-2739171](https://news.artnet.com/art-world/leonardo-sforza-castle-olympics-2739171)

生成摘要时出错

---

## 42. Claude Code daily benchmarks for degradation tracking

**原文标题**: Claude Code daily benchmarks for degradation tracking

**原文链接**: [https://marginlab.ai/trackers/claude-code/](https://marginlab.ai/trackers/claude-code/)

生成摘要时出错

---

## 43. Moltworker: a self-hosted personal AI agent, minus the minis

**原文标题**: Moltworker: a self-hosted personal AI agent, minus the minis

**原文链接**: [https://blog.cloudflare.com/moltworker-self-hosted-ai-agent/](https://blog.cloudflare.com/moltworker-self-hosted-ai-agent/)

生成摘要时出错

---

## 44. Waymo robotaxi hits a child near an elementary school in Santa Monica

**原文标题**: Waymo robotaxi hits a child near an elementary school in Santa Monica

**原文链接**: [https://techcrunch.com/2026/01/29/waymo-robotaxi-hits-a-child-near-an-elementary-school-in-santa-monica/](https://techcrunch.com/2026/01/29/waymo-robotaxi-hits-a-child-near-an-elementary-school-in-santa-monica/)

生成摘要时出错

---

## 45. Nannou – A creative coding framework for Rust

**原文标题**: Nannou – A creative coding framework for Rust

**原文链接**: [https://github.com/nannou-org/nannou](https://github.com/nannou-org/nannou)

生成摘要时出错

---

## 46. Usenet personality

**原文标题**: Usenet personality

**原文链接**: [https://en.wikipedia.org/wiki/Usenet_personality](https://en.wikipedia.org/wiki/Usenet_personality)

生成摘要时出错

---

## 47. Ode to the AA Battery

**原文标题**: Ode to the AA Battery

**原文链接**: [https://www.jeffgeerling.com/blog/2026/ode-to-the-aa-battery/](https://www.jeffgeerling.com/blog/2026/ode-to-the-aa-battery/)

生成摘要时出错

---

## 48. Surely the crash of the US economy has to be soon

**原文标题**: Surely the crash of the US economy has to be soon

**原文链接**: [https://wilsoniumite.com/2026/01/27/surely-it-has-to-be-soon/](https://wilsoniumite.com/2026/01/27/surely-it-has-to-be-soon/)

生成摘要时出错

---

## 49. Tesla’s autonomous vehicles are crashing at a rate much higher tha human drivers

**原文标题**: Tesla’s autonomous vehicles are crashing at a rate much higher tha human drivers

**原文链接**: [https://electrek.co/2026/01/29/teslas-own-robotaxi-data-confirms-crash-rate-3x-worse-than-humans-even-with-monitor/](https://electrek.co/2026/01/29/teslas-own-robotaxi-data-confirms-crash-rate-3x-worse-than-humans-even-with-monitor/)

生成摘要时出错

---

## 50. Deep dive into Turso, the “SQLite rewrite in Rust”

**原文标题**: Deep dive into Turso, the “SQLite rewrite in Rust”

**原文链接**: [https://kerkour.com/turso-sqlite](https://kerkour.com/turso-sqlite)

生成摘要时出错

---

## 51. Show HN: Mystral Native – Run JavaScript games natively with WebGPU (no browser)

**原文标题**: Show HN: Mystral Native – Run JavaScript games natively with WebGPU (no browser)

**原文链接**: [https://github.com/mystralengine/mystralnative](https://github.com/mystralengine/mystralnative)

生成摘要时出错

---

## 52. Employers, please use postmarked letters for job applications (2025)

**原文标题**: Employers, please use postmarked letters for job applications (2025)

**原文链接**: [https://soapstone.mradford.com/employers-use-letters-for-job-applications/](https://soapstone.mradford.com/employers-use-letters-for-job-applications/)

生成摘要时出错

---

## 53. A History of Haggis (2019)

**原文标题**: A History of Haggis (2019)

**原文链接**: [https://www.historytoday.com/archive/historians-cookbook/history-haggis](https://www.historytoday.com/archive/historians-cookbook/history-haggis)

生成摘要时出错

---

## 54. CISA’s acting head uploaded sensitive files into public version of ChatGPT

**原文标题**: CISA’s acting head uploaded sensitive files into public version of ChatGPT

**原文链接**: [https://www.politico.com/news/2026/01/27/cisa-madhu-gottumukkala-chatgpt-00749361](https://www.politico.com/news/2026/01/27/cisa-madhu-gottumukkala-chatgpt-00749361)

生成摘要时出错

---

## 55. Why I Always End Up Going Back to C

**原文标题**: Why I Always End Up Going Back to C

**原文链接**: [https://deplet.ing/why-i-always-end-up-using-c/](https://deplet.ing/why-i-always-end-up-using-c/)

生成摘要时出错

---

## 56. Code is cheap. Show me the talk

**原文标题**: Code is cheap. Show me the talk

**原文链接**: [https://nadh.in/blog/code-is-cheap/](https://nadh.in/blog/code-is-cheap/)

生成摘要时出错

---

## 57. France Just Created Its Own Open Source Alternative to Microsoft Teams and Zoom

**原文标题**: France Just Created Its Own Open Source Alternative to Microsoft Teams and Zoom

**原文链接**: [https://itsfoss.com/news/france-ditches-microsoft-teams-and-zoom/](https://itsfoss.com/news/france-ditches-microsoft-teams-and-zoom/)

生成摘要时出错

---

## 58. Europe’s next-generation weather satellite sends back first images

**原文标题**: Europe’s next-generation weather satellite sends back first images

**原文链接**: [https://www.esa.int/Applications/Observing_the_Earth/Meteorological_missions/meteosat_third_generation/Europe_s_next-generation_weather_satellite_sends_back_first_images](https://www.esa.int/Applications/Observing_the_Earth/Meteorological_missions/meteosat_third_generation/Europe_s_next-generation_weather_satellite_sends_back_first_images)

生成摘要时出错

---

## 59. How to choose colors for your CLI applications (2023)

**原文标题**: How to choose colors for your CLI applications (2023)

**原文链接**: [https://blog.xoria.org/terminal-colors/](https://blog.xoria.org/terminal-colors/)

生成摘要时出错

---

## 60. We can’t send mail farther than 500 miles (2002)

**原文标题**: We can’t send mail farther than 500 miles (2002)

**原文链接**: [https://web.mit.edu/jemorris/humor/500-miles](https://web.mit.edu/jemorris/humor/500-miles)

生成摘要时出错

---

## 61. The Home Computer Hybrids: Atari, TI, and the FCC

**原文标题**: The Home Computer Hybrids: Atari, TI, and the FCC

**原文链接**: [https://technicshistory.com/2026/01/25/the-home-computer-hybrids/](https://technicshistory.com/2026/01/25/the-home-computer-hybrids/)

生成摘要时出错

---

## 62. Apple to soon take up to 30% cut from all Patreon creators in iOS app

**原文标题**: Apple to soon take up to 30% cut from all Patreon creators in iOS app

**原文链接**: [https://www.macrumors.com/2026/01/28/patreon-apple-tax/](https://www.macrumors.com/2026/01/28/patreon-apple-tax/)

生成摘要时出错

---

## 63. Norway EV Push Nears 100 Percent: What's Next?

**原文标题**: Norway EV Push Nears 100 Percent: What's Next?

**原文链接**: [https://spectrum.ieee.org/norway-ev-policy-electric-vehicles](https://spectrum.ieee.org/norway-ev-policy-electric-vehicles)

生成摘要时出错

---

## 64. County pays $600k to pentesters it arrested for assessing courthouse security

**原文标题**: County pays $600k to pentesters it arrested for assessing courthouse security

**原文链接**: [https://arstechnica.com/security/2026/01/county-pays-600000-to-pentesters-it-arrested-for-assessing-courthouse-security/](https://arstechnica.com/security/2026/01/county-pays-600000-to-pentesters-it-arrested-for-assessing-courthouse-security/)

生成摘要时出错

---

## 65. The Sovereign Tech Fund invests in Scala

**原文标题**: The Sovereign Tech Fund invests in Scala

**原文链接**: [https://www.scala-lang.org/blog/2026/01/27/sta-invests-in-scala.html](https://www.scala-lang.org/blog/2026/01/27/sta-invests-in-scala.html)

生成摘要时出错

---

## 66. Health risks of 3D printing – often overlooked

**原文标题**: Health risks of 3D printing – often overlooked

**原文链接**: [https://www.oru.se/english/news/hidden-health-risks-of-3d-printing/](https://www.oru.se/english/news/hidden-health-risks-of-3d-printing/)

生成摘要时出错

---

## 67. The paper model houses of Peter Fritz (2013)

**原文标题**: The paper model houses of Peter Fritz (2013)

**原文链接**: [https://socks-studio.com/2013/12/06/the-imaginary-town-of-an-unconscious-architect-the-387-paper-models-houses-of-peter-fritz/](https://socks-studio.com/2013/12/06/the-imaginary-town-of-an-unconscious-architect-the-387-paper-models-houses-of-peter-fritz/)

生成摘要时出错

---

## 68. Cutting Up Curved Things

**原文标题**: Cutting Up Curved Things

**原文链接**: [https://campedersen.com/tessellation](https://campedersen.com/tessellation)

生成摘要时出错

---

## 69. Drug trio found to block tumour resistance in pancreatic cancer in mouse models

**原文标题**: Drug trio found to block tumour resistance in pancreatic cancer in mouse models

**原文链接**: [https://www.drugtargetreview.com/news/192714/drug-trio-found-to-block-tumour-resistance-in-pancreatic-cancer/](https://www.drugtargetreview.com/news/192714/drug-trio-found-to-block-tumour-resistance-in-pancreatic-cancer/)

生成摘要时出错

---

## 70. A lot of population numbers are fake

**原文标题**: A lot of population numbers are fake

**原文链接**: [https://davidoks.blog/p/a-lot-of-population-numbers-are-fake](https://davidoks.blog/p/a-lot-of-population-numbers-are-fake)

生成摘要时出错

---

## 71. Show HN: Ourguide – OS wide task guidance system that shows you where to click

**原文标题**: Show HN: Ourguide – OS wide task guidance system that shows you where to click

**原文链接**: [https://ourguide.ai](https://ourguide.ai)

生成摘要时出错

---

## 72. Making niche solutions is the point

**原文标题**: Making niche solutions is the point

**原文链接**: [https://ntietz.com/blog/making-niche-solutions-is-the-point/](https://ntietz.com/blog/making-niche-solutions-is-the-point/)

生成摘要时出错

---

## 73. Ubisoft Veteran Says He Was Suspended for Criticizing Return-to-Office Policy

**原文标题**: Ubisoft Veteran Says He Was Suspended for Criticizing Return-to-Office Policy

**原文链接**: [https://www.gamespot.com/articles/ubisoft-veteran-says-he-was-suspended-for-criticizing-its-return-to-office-policy/1100-6537747/](https://www.gamespot.com/articles/ubisoft-veteran-says-he-was-suspended-for-criticizing-its-return-to-office-policy/1100-6537747/)

生成摘要时出错

---

## 74. Nvidia's 10-year effort to make the Shield TV the most updated Android

**原文标题**: Nvidia's 10-year effort to make the Shield TV the most updated Android

**原文链接**: [https://arstechnica.com/gadgets/2026/01/inside-nvidias-10-year-effort-to-make-the-shield-tv-the-most-updated-android-device-ever/](https://arstechnica.com/gadgets/2026/01/inside-nvidias-10-year-effort-to-make-the-shield-tv-the-most-updated-android-device-ever/)

生成摘要时出错

---

## 75. How London became the rest of the world’s startup capital

**原文标题**: How London became the rest of the world’s startup capital

**原文链接**: [https://www.economist.com/britain/2026/01/26/how-london-became-the-rest-of-the-worlds-startup-capital](https://www.economist.com/britain/2026/01/26/how-london-became-the-rest-of-the-worlds-startup-capital)

生成摘要时出错

---

## 76. The Dank Case for Scrolling Window Managers

**原文标题**: The Dank Case for Scrolling Window Managers

**原文链接**: [https://tedium.co/2026/01/29/niri-danklinux-scrolling-window-managers/](https://tedium.co/2026/01/29/niri-danklinux-scrolling-window-managers/)

生成摘要时出错

---

## 77. AI’s impact on engineering jobs may be different than expected

**原文标题**: AI’s impact on engineering jobs may be different than expected

**原文链接**: [https://semiengineering.com/ais-impact-on-engineering-jobs-may-be-different-than-initial-projections/](https://semiengineering.com/ais-impact-on-engineering-jobs-may-be-different-than-initial-projections/)

生成摘要时出错

---

## 78. Skapa, a parametric 3D printing app like an IKEA manual (2025)

**原文标题**: Skapa, a parametric 3D printing app like an IKEA manual (2025)

**原文链接**: [https://nmattia.com/posts/2025-03-24-skapa-intro/](https://nmattia.com/posts/2025-03-24-skapa-intro/)

生成摘要时出错

---

## 79. Tesla ending Models S and X production

**原文标题**: Tesla ending Models S and X production

**原文链接**: [https://www.cnbc.com/2026/01/28/tesla-ending-model-s-x-production.html](https://www.cnbc.com/2026/01/28/tesla-ending-model-s-x-production.html)

生成摘要时出错

---

## 80. Heating homes with the largest particle accelerator

**原文标题**: Heating homes with the largest particle accelerator

**原文链接**: [https://home.cern/news/news/cern/heating-homes-worlds-largest-particle-accelerator](https://home.cern/news/news/cern/heating-homes-worlds-largest-particle-accelerator)

生成摘要时出错

---

## 81. LM Studio 0.4

**原文标题**: LM Studio 0.4

**原文链接**: [https://lmstudio.ai/blog/0.4.0](https://lmstudio.ai/blog/0.4.0)

生成摘要时出错

---

## 82. Decompiling Xbox games using PDB debug info

**原文标题**: Decompiling Xbox games using PDB debug info

**原文链接**: [https://i686.me/blog/csplit/](https://i686.me/blog/csplit/)

生成摘要时出错

---

## 83. FFmpeg is not happy with AI generated patches sent by AMD

**原文标题**: FFmpeg is not happy with AI generated patches sent by AMD

**原文链接**: [https://twitter.com/FFmpeg/status/2016981960015437994](https://twitter.com/FFmpeg/status/2016981960015437994)

生成摘要时出错

---

## 84. Playing Board Games with Deep Convolutional Neural Network on 8bit Motorola 6809

**原文标题**: Playing Board Games with Deep Convolutional Neural Network on 8bit Motorola 6809

**原文链接**: [https://ipsj.ixsq.nii.ac.jp/records/229345](https://ipsj.ixsq.nii.ac.jp/records/229345)

生成摘要时出错

---

## 85. Mermaid ASCII: Render Mermaid diagrams in your terminal

**原文标题**: Mermaid ASCII: Render Mermaid diagrams in your terminal

**原文链接**: [https://github.com/lukilabs/beautiful-mermaid](https://github.com/lukilabs/beautiful-mermaid)

生成摘要时出错

---

## 86. Tesla is committing automotive suicide

**原文标题**: Tesla is committing automotive suicide

**原文链接**: [https://electrek.co/2026/01/29/tesla-committing-automotive-suicide/](https://electrek.co/2026/01/29/tesla-committing-automotive-suicide/)

生成摘要时出错

---

## 87. Solar panels on land used for biofuels could power all cars and trucks electric

**原文标题**: Solar panels on land used for biofuels could power all cars and trucks electric

**原文链接**: [https://ourworldindata.org/biofuel-land-solar-electric-vehicles](https://ourworldindata.org/biofuel-land-solar-electric-vehicles)

生成摘要时出错

---

## 88. Show HN: ShapedQL – A SQL engine for multi-stage ranking and RAG

**原文标题**: Show HN: ShapedQL – A SQL engine for multi-stage ranking and RAG

**原文链接**: [https://playground.shaped.ai](https://playground.shaped.ai)

生成摘要时出错

---

## 89. The most dangerous code: Validating SSL certs in non-browser software (2012) [pdf]

**原文标题**: The most dangerous code: Validating SSL certs in non-browser software (2012) [pdf]

**原文链接**: [https://www.cs.cornell.edu/~shmat/shmat_ccs12.pdf](https://www.cs.cornell.edu/~shmat/shmat_ccs12.pdf)

生成摘要时出错

---

## 90. Vitamin D and Omega-3 have a larger effect on depression than antidepressants

**原文标题**: Vitamin D and Omega-3 have a larger effect on depression than antidepressants

**原文链接**: [https://blog.ncase.me/on-depression/](https://blog.ncase.me/on-depression/)

生成摘要时出错

---

## 91. When Every Network is 192.168.1.x

**原文标题**: When Every Network is 192.168.1.x

**原文链接**: [https://netrinos.com/blog/conflicting-subnets](https://netrinos.com/blog/conflicting-subnets)

生成摘要时出错

---

## 92. Agent-shell: A native Emacs buffer to interact with LLM agents powered by ACP

**原文标题**: Agent-shell: A native Emacs buffer to interact with LLM agents powered by ACP

**原文链接**: [https://github.com/xenodium/agent-shell](https://github.com/xenodium/agent-shell)

生成摘要时出错

---

## 93. 9front OS

**原文标题**: 9front OS

**原文链接**: [https://9front.org/](https://9front.org/)

生成摘要时出错

---

## 94. Networks Hold the Key to a Decades-Old Problem About Waves

**原文标题**: Networks Hold the Key to a Decades-Old Problem About Waves

**原文链接**: [https://www.quantamagazine.org/networks-hold-the-key-to-a-decades-old-problem-about-waves-20260128/](https://www.quantamagazine.org/networks-hold-the-key-to-a-decades-old-problem-about-waves-20260128/)

生成摘要时出错

---

## 95. Show HN: I'm building an AI-proof writing tool. How would you defeat it?

**原文标题**: Show HN: I'm building an AI-proof writing tool. How would you defeat it?

**原文链接**: [https://auth-auth.vercel.app/](https://auth-auth.vercel.app/)

生成摘要时出错

---

## 96. The Hallucination Defense

**原文标题**: The Hallucination Defense

**原文链接**: [https://niyikiza.com/posts/hallucination-defense/](https://niyikiza.com/posts/hallucination-defense/)

生成摘要时出错

---

## 97. iPhone 16 Best-Selling Smartphone in 2025; Apple Takes 7 Spots in Top Models

**原文标题**: iPhone 16 Best-Selling Smartphone in 2025; Apple Takes 7 Spots in Top Models

**原文链接**: [https://counterpointresearch.com/en/insights/iphone-16-worlds-best-selling-smartphone-in-2025-apple-takes-7-spots-in-top-10-models](https://counterpointresearch.com/en/insights/iphone-16-worlds-best-selling-smartphone-in-2025-apple-takes-7-spots-in-top-10-models)

生成摘要时出错

---

## 98. Make.ts

**原文标题**: Make.ts

**原文链接**: [https://matklad.github.io/2026/01/27/make-ts.html](https://matklad.github.io/2026/01/27/make-ts.html)

生成摘要时出错

---

## 99. UN risks 'imminent financial collapse', secretary general warns

**原文标题**: UN risks 'imminent financial collapse', secretary general warns

**原文链接**: [https://www.bbc.co.uk/news/articles/cr579mdv4m7o](https://www.bbc.co.uk/news/articles/cr579mdv4m7o)

生成摘要时出错

---

## 100. Apple buys Israeli startup Q.ai

**原文标题**: Apple buys Israeli startup Q.ai

**原文链接**: [https://techcrunch.com/2026/01/29/apple-buys-israeli-startup-q-ai-as-the-ai-race-heats-up/](https://techcrunch.com/2026/01/29/apple-buys-israeli-startup-q-ai-as-the-ai-race-heats-up/)

生成摘要时出错

---

