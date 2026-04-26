# Hacker News 热门文章摘要 (2026-04-26)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. The Nintendo Switch Switch (2019)

**原文标题**: The Nintendo Switch Switch (2019)

**原文链接**: [https://blog.cynthia.re/post/nintendo-switch-ethernet-switch](https://blog.cynthia.re/post/nintendo-switch-ethernet-switch)

生成摘要时出错

---

## 12. GitHub unwanted UX change: issue links now open in a popup

**原文标题**: GitHub unwanted UX change: issue links now open in a popup

**原文链接**: [https://github.com/orgs/community/discussions/192666](https://github.com/orgs/community/discussions/192666)

生成摘要时出错

---

## 13. The West forgot how to make things, now it’s forgetting how to code

**原文标题**: The West forgot how to make things, now it’s forgetting how to code

**原文链接**: [https://techtrenches.dev/p/the-west-forgot-how-to-make-things](https://techtrenches.dev/p/the-west-forgot-how-to-make-things)

生成摘要时出错

---

## 14. USB Cheat Sheet (2022)

**原文标题**: USB Cheat Sheet (2022)

**原文链接**: [https://fabiensanglard.net/usbcheat/index.html](https://fabiensanglard.net/usbcheat/index.html)

生成摘要时出错

---

## 15. Cheating at Tetris

**原文标题**: Cheating at Tetris

**原文链接**: [https://chalkdustmagazine.com/features/cheating-at-tetris/](https://chalkdustmagazine.com/features/cheating-at-tetris/)

生成摘要时出错

---

## 16. GnuPG – post-quantum crypto landing in mainline

**原文标题**: GnuPG – post-quantum crypto landing in mainline

**原文链接**: [https://lists.gnupg.org/pipermail/gnupg-announce/2026q2/000504.html](https://lists.gnupg.org/pipermail/gnupg-announce/2026q2/000504.html)

生成摘要时出错

---

## 17. Mine, a Coalton and Common Lisp IDE

**原文标题**: Mine, a Coalton and Common Lisp IDE

**原文链接**: [https://coalton-lang.github.io/20260424-mine/](https://coalton-lang.github.io/20260424-mine/)

生成摘要时出错

---

## 18. Mahjong: A Visual Guide

**原文标题**: Mahjong: A Visual Guide

**原文链接**: [https://themahjong.guide/](https://themahjong.guide/)

生成摘要时出错

---

## 19. Flickr: The first and last great photo platform

**原文标题**: Flickr: The first and last great photo platform

**原文链接**: [https://petapixel.com/2026/04/22/flickr-the-first-and-last-great-photo-platform/](https://petapixel.com/2026/04/22/flickr-the-first-and-last-great-photo-platform/)

生成摘要时出错

---

## 20. Exposing Floating Point – Bartosz Ciechanowski (2019)

**原文标题**: Exposing Floating Point – Bartosz Ciechanowski (2019)

**原文链接**: [https://ciechanow.ski/exposing-floating-point/](https://ciechanow.ski/exposing-floating-point/)

生成摘要时出错

---

## 21. Terra API (YC W21) 招聘：应用人工智能策略师（健康智能）

**原文标题**: Terra API (YC W21) Hiring: Applied AI Strategist(Health Intelligence)

**原文链接**: [https://www.ycombinator.com/companies/terra-api/jobs/DY7BCZU-applied-ai-strategist-market-intelligence-health](https://www.ycombinator.com/companies/terra-api/jobs/DY7BCZU-applied-ai-strategist-market-intelligence-health)

生成摘要时出错

---

## 22. QNX on the Commodore 900 – Raiders of the lost hard drive [video]

**原文标题**: QNX on the Commodore 900 – Raiders of the lost hard drive [video]

**原文链接**: [https://archive.fosdem.org/2025/schedule/event/fosdem-2025-5479-raiders-of-the-lost-hard-drive/](https://archive.fosdem.org/2025/schedule/event/fosdem-2025-5479-raiders-of-the-lost-hard-drive/)

This article details a presentation by Michal Pleban at FOSDEM 2025 regarding the restoration of the **Commodore 900 (C900)**, a rare piece of computing history.

Introduced in 1984 as a budget Unix workstation, the C900 utilized the obscure Zilog Z8000 processor. However, the project was canceled shortly after Commodore acquired Amiga, leaving only a few dozen prototypes in existence. 

The talk chronicles Pleban's "digital archaeology" efforts to revive a non-functional prototype that lacked a power supply, monitor, and keyboard, and suffered from a failing hard drive showing a cryptic "0xFF" error. To bring the machine back to life, Pleban performed several complex technical tasks, including:
*   Disassembling the Z8000 BIOS.
*   Reverse-engineering the proprietary keyboard interface.
*   Deciphering the hard disk’s low-level format to recover data.

Ultimately, the project was a success. Beyond restoring his own unit, Pleban has used his findings to help other C900 owners repair their machines, ensuring the survival of this nearly lost chapter of Commodore’s legacy.

---

## 23. OpenAI Privacy Filter

**原文标题**: OpenAI Privacy Filter

**原文链接**: [https://openai.com/index/introducing-openai-privacy-filter/](https://openai.com/index/introducing-openai-privacy-filter/)

生成摘要时出错

---

## 24. Using coding assistance tools to revive projects you never were going to finish

**原文标题**: Using coding assistance tools to revive projects you never were going to finish

**原文链接**: [https://blog.matthewbrunelle.com/its-ok-to-use-coding-assistance-tools-to-revive-the-projects-you-never-were-going-to-finish/](https://blog.matthewbrunelle.com/its-ok-to-use-coding-assistance-tools-to-revive-the-projects-you-never-were-going-to-finish/)

生成摘要时出错

---

## 25. The Free Universal Construction Kit

**原文标题**: The Free Universal Construction Kit

**原文链接**: [https://fffff.at/free-universal-construction-kit/](https://fffff.at/free-universal-construction-kit/)

生成摘要时出错

---

## 26. The route from Prussian military headquarters to Gary Gygax’s basement

**原文标题**: The route from Prussian military headquarters to Gary Gygax’s basement

**原文链接**: [https://asteriskmag.com/issues/14/shall-we-play-a-game](https://asteriskmag.com/issues/14/shall-we-play-a-game)

生成摘要时出错

---

## 27. My .config Ship of Theseus

**原文标题**: My .config Ship of Theseus

**原文链接**: [https://shift1w.com/blog/config-of-theseus/](https://shift1w.com/blog/config-of-theseus/)

生成摘要时出错

---

## 28. The Super Nintendo Cartridges (2024)

**原文标题**: The Super Nintendo Cartridges (2024)

**原文链接**: [https://fabiensanglard.net/snes_carts/](https://fabiensanglard.net/snes_carts/)

生成摘要时出错

---

## 29. The Joy of Folding Bikes

**原文标题**: The Joy of Folding Bikes

**原文链接**: [https://blog.korny.info/2026/04/19/the-joy-of-folding-bikes](https://blog.korny.info/2026/04/19/the-joy-of-folding-bikes)

生成摘要时出错

---

## 30. America's Geothermal Breakthrough

**原文标题**: America's Geothermal Breakthrough

**原文链接**: [https://oilprice.com/Alternative-Energy/Geothermal-Energy/Americas-Geothermal-Breakthrough-Could-Unlock-a-150-Gigawatt-Energy-Revolution.html](https://oilprice.com/Alternative-Energy/Geothermal-Energy/Americas-Geothermal-Breakthrough-Could-Unlock-a-150-Gigawatt-Energy-Revolution.html)

生成摘要时出错

---

## 31. EU Age Control: The trojan horse for digital IDs

**原文标题**: EU Age Control: The trojan horse for digital IDs

**原文链接**: [https://juraj.bednar.io/en/blog-en/2026/04/17/eu-age-control-the-trojan-horse-for-digital-ids/](https://juraj.bednar.io/en/blog-en/2026/04/17/eu-age-control-the-trojan-horse-for-digital-ids/)

生成摘要时出错

---

## 32. Math Is Hard – OpenBSD Stories

**原文标题**: Math Is Hard – OpenBSD Stories

**原文链接**: [http://miod.online.fr/software/openbsd/stories/vaxfp.html](http://miod.online.fr/software/openbsd/stories/vaxfp.html)

生成摘要时出错

---

## 33. Show HN: I remade my blog into a Windows 3.1 environment

**原文标题**: Show HN: I remade my blog into a Windows 3.1 environment

**原文链接**: [https://passo.uno/](https://passo.uno/)

生成摘要时出错

---

## 34. Show HN: A free ESG stock screener that publishes its losses and methodology

**原文标题**: Show HN: A free ESG stock screener that publishes its losses and methodology

**原文链接**: [https://jumpstartsignal.com/](https://jumpstartsignal.com/)

生成摘要时出错

---

## 35. Simulacrum of Knowledge Work

**原文标题**: Simulacrum of Knowledge Work

**原文链接**: [https://blog.happyfellow.dev/simulacrum-of-knowledge-work/](https://blog.happyfellow.dev/simulacrum-of-knowledge-work/)

生成摘要时出错

---

## 36. Hokusai and Tesselations

**原文标题**: Hokusai and Tesselations

**原文链接**: [https://dl.ndl.go.jp/pid/1899550/1/11/](https://dl.ndl.go.jp/pid/1899550/1/11/)

生成摘要时出错

---

## 37. What async promised and what it delivered

**原文标题**: What async promised and what it delivered

**原文链接**: [https://causality.blog/essays/what-async-promised/](https://causality.blog/essays/what-async-promised/)

生成摘要时出错

---

## 38. Eden AI – European Alternative to OpenRouter

**原文标题**: Eden AI – European Alternative to OpenRouter

**原文链接**: [https://www.edenai.co](https://www.edenai.co)

生成摘要时出错

---

## 39. APL is more French than English

**原文标题**: APL is more French than English

**原文链接**: [https://www.jsoftware.com/papers/perlis78.htm](https://www.jsoftware.com/papers/perlis78.htm)

生成摘要时出错

---

## 40. DeepSeek-V4 on Day 0: From Fast Inference to Verified RL with SGLang and Miles

**原文标题**: DeepSeek-V4 on Day 0: From Fast Inference to Verified RL with SGLang and Miles

**原文链接**: [https://www.lmsys.org/blog/2026-04-25-deepseek-v4/](https://www.lmsys.org/blog/2026-04-25-deepseek-v4/)

生成摘要时出错

---

## 41. Optimizing Datalog for the GPU

**原文标题**: Optimizing Datalog for the GPU

**原文链接**: [https://dl.acm.org/doi/10.1145/3669940.3707274](https://dl.acm.org/doi/10.1145/3669940.3707274)

生成摘要时出错

---

## 42. A populist wave is rising to end the 'captive' repair economy

**原文标题**: A populist wave is rising to end the 'captive' repair economy

**原文链接**: [https://www.cnbc.com/2026/04/25/right-to-repair-consumer-prices-affordability-economy-elections.html](https://www.cnbc.com/2026/04/25/right-to-repair-consumer-prices-affordability-economy-elections.html)

生成摘要时出错

---

## 43. 1-Bit Hokusai's "The Great Wave" (2023)

**原文标题**: 1-Bit Hokusai's "The Great Wave" (2023)

**原文链接**: [https://www.hypertalking.com/2023/05/08/1-bit-pixel-art-of-hokusais-the-great-wave-off-kanagawa/](https://www.hypertalking.com/2023/05/08/1-bit-pixel-art-of-hokusais-the-great-wave-off-kanagawa/)

生成摘要时出错

---

## 44. Mine, an IDE for Coalton and Common Lisp

**原文标题**: Mine, an IDE for Coalton and Common Lisp

**原文链接**: [https://coalton-lang.github.io/mine/](https://coalton-lang.github.io/mine/)

生成摘要时出错

---

## 45. Discret 11, the French TV encryption of the 80s (2020)

**原文标题**: Discret 11, the French TV encryption of the 80s (2020)

**原文链接**: [https://fabiensanglard.net/discret11/](https://fabiensanglard.net/discret11/)

生成摘要时出错

---

## 46. I spent 6 years building my Kanban as I hated how managers run the boards

**原文标题**: I spent 6 years building my Kanban as I hated how managers run the boards

**原文链接**: [https://www.npmjs.com/package/ooko](https://www.npmjs.com/package/ooko)

生成摘要时出错

---

## 47. The Long Reply

**原文标题**: The Long Reply

**原文链接**: [https://ironicsans.ghost.io/the-long-reply/](https://ironicsans.ghost.io/the-long-reply/)

生成摘要时出错

---

## 48. The George Business, by Roger Zelazny (1980)

**原文标题**: The George Business, by Roger Zelazny (1980)

**原文链接**: [https://www.eternal-flame.org/library/oldlibrary/georgebusiness.html](https://www.eternal-flame.org/library/oldlibrary/georgebusiness.html)

生成摘要时出错

---

## 49. New 10 GbE USB adapters are cooler, smaller, cheaper

**原文标题**: New 10 GbE USB adapters are cooler, smaller, cheaper

**原文链接**: [https://www.jeffgeerling.com/blog/2026/new-10-gbe-usb-adapters-cooler-smaller-cheaper/](https://www.jeffgeerling.com/blog/2026/new-10-gbe-usb-adapters-cooler-smaller-cheaper/)

生成摘要时出错

---

## 50. Rediscovering the Handcart

**原文标题**: Rediscovering the Handcart

**原文链接**: [https://solar.lowtechmagazine.com/2026/04/rediscovering-the-handcart/](https://solar.lowtechmagazine.com/2026/04/rediscovering-the-handcart/)

生成摘要时出错

---

## 51. Reviving BrowserID in 2026

**原文标题**: Reviving BrowserID in 2026

**原文链接**: [https://wakamoleguy.com/p/reviving-browserid-in-2026](https://wakamoleguy.com/p/reviving-browserid-in-2026)

生成摘要时出错

---

## 52. GPT‑5.5 Bio Bug Bounty

**原文标题**: GPT‑5.5 Bio Bug Bounty

**原文链接**: [https://openai.com/index/gpt-5-5-bio-bug-bounty/](https://openai.com/index/gpt-5-5-bio-bug-bounty/)

生成摘要时出错

---

## 53. DeepSeek v4

**原文标题**: DeepSeek v4

**原文链接**: [https://api-docs.deepseek.com/news/news260424](https://api-docs.deepseek.com/news/news260424)

生成摘要时出错

---

## 54. Quirks of Human Anatomy

**原文标题**: Quirks of Human Anatomy

**原文链接**: [https://www.sdbonline.org/sites/fly/lewheldquirk/figlegq6.htm](https://www.sdbonline.org/sites/fly/lewheldquirk/figlegq6.htm)

生成摘要时出错

---

## 55. A web-based RDP client built with Go WebAssembly and grdp

**原文标题**: A web-based RDP client built with Go WebAssembly and grdp

**原文链接**: [https://github.com/nakagami/grdpwasm](https://github.com/nakagami/grdpwasm)

生成摘要时出错

---

## 56. Lute: A Standalone Runtime for Luau

**原文标题**: Lute: A Standalone Runtime for Luau

**原文链接**: [https://lute.luau.org/](https://lute.luau.org/)

生成摘要时出错

---

## 57. Martin Galway's music source files from 1980's Commodore 64 games

**原文标题**: Martin Galway's music source files from 1980's Commodore 64 games

**原文链接**: [https://github.com/MartinGalway/C64_music](https://github.com/MartinGalway/C64_music)

生成摘要时出错

---

## 58. How Hard Is It to Open a File?

**原文标题**: How Hard Is It to Open a File?

**原文链接**: [https://blog.sebastianwick.net/posts/how-hard-is-it-to-open-a-file/](https://blog.sebastianwick.net/posts/how-hard-is-it-to-open-a-file/)

生成摘要时出错

---

## 59. The Knight Programming Language

**原文标题**: The Knight Programming Language

**原文链接**: [https://github.com/knight-lang/knight-lang/tree/master](https://github.com/knight-lang/knight-lang/tree/master)

生成摘要时出错

---

## 60. AGPLv3§74 Empowers Users to Thwart Badgeware Like OnlyOffice

**原文标题**: AGPLv3§74 Empowers Users to Thwart Badgeware Like OnlyOffice

**原文链接**: [https://sfconservancy.org/blog/2026/apr/16/badgeware-onlyoffice-nextcloud-affero-gpl/](https://sfconservancy.org/blog/2026/apr/16/badgeware-onlyoffice-nextcloud-affero-gpl/)

生成摘要时出错

---

## 61. Just How Much Should You Worry About Eating That Burnt Toast?

**原文标题**: Just How Much Should You Worry About Eating That Burnt Toast?

**原文链接**: [https://www.mcgill.ca/oss/article/medical-critical-thinking-health-and-nutrition/just-how-much-should-you-worry-about-eating-burnt-toast](https://www.mcgill.ca/oss/article/medical-critical-thinking-health-and-nutrition/just-how-much-should-you-worry-about-eating-burnt-toast)

生成摘要时出错

---

## 62. AI Might Be Lying to Your Boss

**原文标题**: AI Might Be Lying to Your Boss

**原文链接**: [https://williamoconnell.me/blog/post/ai-ide/](https://williamoconnell.me/blog/post/ai-ide/)

生成摘要时出错

---

## 63. GPT-5.5

**原文标题**: GPT-5.5

**原文链接**: [https://openai.com/index/introducing-gpt-5-5/](https://openai.com/index/introducing-gpt-5-5/)

生成摘要时出错

---

## 64. Paraloid B-72

**原文标题**: Paraloid B-72

**原文链接**: [https://en.wikipedia.org/wiki/Paraloid_B-72](https://en.wikipedia.org/wiki/Paraloid_B-72)

生成摘要时出错

---

## 65. Insights into firewood use by early Middle Pleistocene hominins

**原文标题**: Insights into firewood use by early Middle Pleistocene hominins

**原文链接**: [https://www.sciencedirect.com/science/article/pii/S0277379126001824](https://www.sciencedirect.com/science/article/pii/S0277379126001824)

生成摘要时出错

---

## 66. Which one is more important: more parameters or more computation? (2021)

**原文标题**: Which one is more important: more parameters or more computation? (2021)

**原文链接**: [https://parl.ai/projects/params_vs_compute/](https://parl.ai/projects/params_vs_compute/)

生成摘要时出错

---

## 67. Microsoft Reportedly Looking at Rebasing Azure Linux on Fedora

**原文标题**: Microsoft Reportedly Looking at Rebasing Azure Linux on Fedora

**原文链接**: [https://www.phoronix.com/news/MS-Azure-Linux-Fedora-Based](https://www.phoronix.com/news/MS-Azure-Linux-Fedora-Based)

生成摘要时出错

---

## 68. The mail sent to a video game publisher

**原文标题**: The mail sent to a video game publisher

**原文链接**: [https://www.gamefile.news/p/panic-mail-arco-despelote-time-flies-thank-goodness-teeth](https://www.gamefile.news/p/panic-mail-arco-despelote-time-flies-thank-goodness-teeth)

生成摘要时出错

---

## 69. Only one side will be the true successor to MS-DOS – Windows 2.x

**原文标题**: Only one side will be the true successor to MS-DOS – Windows 2.x

**原文链接**: [https://blisscast.wordpress.com/2026/04/21/windows-2-gui-wonderland-12a/](https://blisscast.wordpress.com/2026/04/21/windows-2-gui-wonderland-12a/)

生成摘要时出错

---

## 70. Colorado Adds Open-Source Exemption to Age-Verification Bill

**原文标题**: Colorado Adds Open-Source Exemption to Age-Verification Bill

**原文链接**: [https://fosstodon.org/@carlrichell/116460505717380644](https://fosstodon.org/@carlrichell/116460505717380644)

生成摘要时出错

---

## 71. I have officially retired from Emacs

**原文标题**: I have officially retired from Emacs

**原文链接**: [https://nullprogram.com/blog/2026/04/26/](https://nullprogram.com/blog/2026/04/26/)

生成摘要时出错

---

## 72. Lambda Calculus Benchmark for AI

**原文标题**: Lambda Calculus Benchmark for AI

**原文链接**: [https://victortaelin.github.io/lambench/](https://victortaelin.github.io/lambench/)

生成摘要时出错

---

## 73. Show HN: Browse GitHub repos in Emacs without cloning

**原文标题**: Show HN: Browse GitHub repos in Emacs without cloning

**原文链接**: [https://github.com/agzam/remoto.el](https://github.com/agzam/remoto.el)

生成摘要时出错

---

## 74. Open source memory layer so any AI agent can do what Claude.ai and ChatGPT do

**原文标题**: Open source memory layer so any AI agent can do what Claude.ai and ChatGPT do

**原文链接**: [https://alash3al.github.io/stash?_v01](https://alash3al.github.io/stash?_v01)

生成摘要时出错

---

## 75. A 3D Body from Eight Questions – No Photo, No GPU

**原文标题**: A 3D Body from Eight Questions – No Photo, No GPU

**原文链接**: [https://clad.you/blog/posts/questionnaire-mlp/](https://clad.you/blog/posts/questionnaire-mlp/)

生成摘要时出错

---

## 76. Work with the garage door up (2024)

**原文标题**: Work with the garage door up (2024)

**原文链接**: [https://notes.andymatuschak.org/Work_with_the_garage_door_up](https://notes.andymatuschak.org/Work_with_the_garage_door_up)

生成摘要时出错

---

## 77. Show HN: Kloak, A secret manager that keeps K8s workload away from secrets

**原文标题**: Show HN: Kloak, A secret manager that keeps K8s workload away from secrets

**原文链接**: [https://getkloak.io/](https://getkloak.io/)

生成摘要时出错

---

## 78. Alberta startup sells no-tech tractors for half price

**原文标题**: Alberta startup sells no-tech tractors for half price

**原文链接**: [https://wheelfront.com/this-alberta-startup-sells-no-tech-tractors-for-half-price/](https://wheelfront.com/this-alberta-startup-sells-no-tech-tractors-for-half-price/)

生成摘要时出错

---

## 79. Mise-En-Place

**原文标题**: Mise-En-Place

**原文链接**: [https://mise.jdx.dev/](https://mise.jdx.dev/)

生成摘要时出错

---

## 80. Diatec, known for its mechanical keyboard brand FILCO, has ceased operations

**原文标题**: Diatec, known for its mechanical keyboard brand FILCO, has ceased operations

**原文链接**: [https://gigazine.net/gsc_news/en/20260424-filco-diatec/](https://gigazine.net/gsc_news/en/20260424-filco-diatec/)

生成摘要时出错

---

## 81. Cosmology with Geometry Nodes

**原文标题**: Cosmology with Geometry Nodes

**原文链接**: [https://www.blender.org/user-stories/cosmology-with-geometry-nodes/](https://www.blender.org/user-stories/cosmology-with-geometry-nodes/)

生成摘要时出错

---

## 82. Can you stop beans from making you gassy?

**原文标题**: Can you stop beans from making you gassy?

**原文链接**: [https://www.seriouseats.com/how-to-reduce-bean-gas-tested-11883862](https://www.seriouseats.com/how-to-reduce-bean-gas-tested-11883862)

生成摘要时出错

---

## 83. Panipat: The rise of the Mughals

**原文标题**: Panipat: The rise of the Mughals

**原文链接**: [https://www.historytoday.com/archive/feature/panipat-rise-mughals](https://www.historytoday.com/archive/feature/panipat-rise-mughals)

生成摘要时出错

---

## 84. Sabotaging projects by overthinking, scope creep, and structural diffing

**原文标题**: Sabotaging projects by overthinking, scope creep, and structural diffing

**原文链接**: [https://kevinlynagh.com/newsletter/2026_04_overthinking/](https://kevinlynagh.com/newsletter/2026_04_overthinking/)

生成摘要时出错

---

## 85. How to Implement an FPS Counter

**原文标题**: How to Implement an FPS Counter

**原文链接**: [https://vplesko.com/posts/how_to_implement_an_fps_counter.html](https://vplesko.com/posts/how_to_implement_an_fps_counter.html)

生成摘要时出错

---

## 86. Commenting and approving pull requests

**原文标题**: Commenting and approving pull requests

**原文链接**: [https://www.jakeworth.com/posts/on-commenting-and-approving-pull-requests/](https://www.jakeworth.com/posts/on-commenting-and-approving-pull-requests/)

生成摘要时出错

---

## 87. Plain text has been around for decades and it’s here to stay

**原文标题**: Plain text has been around for decades and it’s here to stay

**原文链接**: [https://unsung.aresluna.org/plain-text-has-been-around-for-decades-and-its-here-to-stay/](https://unsung.aresluna.org/plain-text-has-been-around-for-decades-and-its-here-to-stay/)

生成摘要时出错

---

## 88. US special forces soldier arrested after allegedly winning $400k on Maduro raid

**原文标题**: US special forces soldier arrested after allegedly winning $400k on Maduro raid

**原文链接**: [https://www.cnn.com/2026/04/23/politics/us-special-forces-soldier-arrested-maduro-raid-trade](https://www.cnn.com/2026/04/23/politics/us-special-forces-soldier-arrested-maduro-raid-trade)

生成摘要时出错

---

## 89. Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown and Git)

**原文标题**: Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown and Git)

**原文链接**: [https://github.com/nex-crm/wuphf](https://github.com/nex-crm/wuphf)

生成摘要时出错

---

## 90. Replace IBM Quantum back end with /dev/urandom

**原文标题**: Replace IBM Quantum back end with /dev/urandom

**原文链接**: [https://github.com/yuvadm/quantumslop/blob/25ad2e76ae58baa96f6219742459407db9dd17f5/URANDOM_DEMO.md](https://github.com/yuvadm/quantumslop/blob/25ad2e76ae58baa96f6219742459407db9dd17f5/URANDOM_DEMO.md)

生成摘要时出错

---

## 91. PCR is a surprisingly near-optimal technology

**原文标题**: PCR is a surprisingly near-optimal technology

**原文链接**: [https://nikomc.com/2026/04/22/pcr/](https://nikomc.com/2026/04/22/pcr/)

生成摘要时出错

---

## 92. Protovac Retro Terminal (2025)

**原文标题**: Protovac Retro Terminal (2025)

**原文链接**: [https://tanner.vc/protovac-retro-terminal/](https://tanner.vc/protovac-retro-terminal/)

生成摘要时出错

---

## 93. HEALPix

**原文标题**: HEALPix

**原文链接**: [https://en.wikipedia.org/wiki/HEALPix](https://en.wikipedia.org/wiki/HEALPix)

生成摘要时出错

---

## 94. MacBook Neo and how the iPad should be

**原文标题**: MacBook Neo and how the iPad should be

**原文链接**: [https://craigmod.com/essays/ipad_neo/](https://craigmod.com/essays/ipad_neo/)

生成摘要时出错

---

## 95. Firefox Has Integrated Brave's Adblock Engine

**原文标题**: Firefox Has Integrated Brave's Adblock Engine

**原文链接**: [https://itsfoss.com/news/firefox-ships-brave-adblock-engine/](https://itsfoss.com/news/firefox-ships-brave-adblock-engine/)

生成摘要时出错

---

## 96. I'm done making desktop applications (2009)

**原文标题**: I'm done making desktop applications (2009)

**原文链接**: [https://www.kalzumeus.com/2009/09/05/desktop-aps-versus-web-apps/](https://www.kalzumeus.com/2009/09/05/desktop-aps-versus-web-apps/)

生成摘要时出错

---

## 97. North American Millets Alliance

**原文标题**: North American Millets Alliance

**原文链接**: [https://milletsalliance.org/](https://milletsalliance.org/)

生成摘要时出错

---

## 98. Show HN: I've built a nice home server OS

**原文标题**: Show HN: I've built a nice home server OS

**原文链接**: [https://lightwhale.asklandd.dk/](https://lightwhale.asklandd.dk/)

生成摘要时出错

---

## 99. Show HN: DDoS detection in 0.9s, tested against a 48 Gbps attack live

**原文标题**: Show HN: DDoS detection in 0.9s, tested against a 48 Gbps attack live

**原文链接**: [https://flowtriq.com/blog/lorikeet-security-case-study](https://flowtriq.com/blog/lorikeet-security-case-study)

生成摘要时出错

---

## 100. Google Flow Music

**原文标题**: Google Flow Music

**原文链接**: [https://www.flowmusic.app/](https://www.flowmusic.app/)

生成摘要时出错

---

