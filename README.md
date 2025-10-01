# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-10-01.md)

*最后自动更新时间: 2025-10-01 17:48:29*
## 1. Codeberg项目数量突破30万

**原文标题**: Codeberg Reaches 300k Projects

**原文链接**: [https://codeberg.org/](https://codeberg.org/)

无法访问文章链接。

---

## 2. 展示一下：自闭症模拟器

**原文标题**: Show HN: Autism Simulator

**原文链接**: [https://autism-simulator.vercel.app/](https://autism-simulator.vercel.app/)

“自闭症模拟器”是一款互动式教育工具，旨在模拟自闭症人士在职场中的体验。该模拟旨在提高人们对自闭症人士在专业环境中的理解和同情。通过让用户体验自闭症人士经常遇到的感官超载、社交挑战和认知处理差异，该模拟器希望促进更具包容性和支持性的工作环境。它可能是一种沉浸式体验，包含各种互动元素，以模仿自闭症人士面临的具体挑战，从而深入了解如何更好地适应工作场所以及同事如何提供更有效的支持。该工具的最终目的是教育和培养一个更具包容性和理解性的自闭症人士职场文化。

---

## 3. 构建堆：为预训练堆叠30拍字节硬盘

**原文标题**: Building the heap: racking 30 petabytes of hard drives for pretraining

**原文链接**: [https://si.inc/posts/the-heap/](https://si.inc/posts/the-heap/)

本文详细介绍了某公司如何在旧金山托管中心构建自己的 30PB 存储集群，用于在视频数据上预训练机器学习模型。他们选择这条路线是为了大幅降低成本，与 AWS 和 Cloudflare 等云存储选项相比。核心思想是，机器学习训练数据可以容忍更高的数据损坏率，从而使云的高冗余性和可用性变得不必要。

自建方案将每月成本显著降低至 29,500 美元（包括折旧），而 AWS 为 1,130,000 美元，Cloudflare 为 270,000 美元。该集群由安装在 NetApp 机箱中的二手企业级硬盘驱动器组成，由英特尔 CPU 头节点提供支持，并通过 100Gbps 网络连接。

本文概述了成本构成，涵盖互联网、电力、硬盘驱动器、机箱、服务器、数据中心设置和人工。他们强调了简单软件堆栈对于管理存储的重要性，选择了一个定制的 200 行 Rust 脚本，而不是像 Ceph 或 MinIO 这样更复杂的解决方案。

本文还包括设置过程中吸取的经验教训，包括硬件选择的技巧（避免前置加载器、选择更密集的阵列、避免菊花链连接）、兼容性的重要性以及 IPMI/KVM 的实用性。最后，本文列出了复制该设置所需的组件，包括具体的硬件建议。

---

## 4. Fossabot：针对Dependabot/Renovate中重大变更和影响的AI代码审查

**原文标题**: Fossabot: AI code review for Dependabot/Renovate on breaking changes and impacts

**原文链接**: [https://fossa.com/blog/fossabot-dependency-upgrade-ai-agent/](https://fossa.com/blog/fossabot-dependency-upgrade-ai-agent/)

FOSSA 宣布 Fossabot，一款旨在自动化 JavaScript 和 TypeScript 项目战略性依赖更新的 AI 代理，解决依赖频繁变动和更新停滞的问题。与 Dependabot 和 Renovate 等现有更新工具通常依赖简单的补丁级更新不同，Fossabot 分析代码库以了解更新的影响，提出适配方案，并通过拉取请求交付完成的任务。

Fossabot 通过理解应用上下文中的重大变更来平衡风险和收益，利用 EdgeBit 收购带来的静态分析能力来防止错误并提供准确的推理。这使其能够处理通常需要高级工程师才能完成的复杂升级。

该 AI 代理通过进行广泛的研究、参考文档并保持对代码库、依赖项和发行说明的全面记忆，从而超越了人类的能力。 Fossabot 使用准确性、一致性、正确性 (ACC) 框架进行评估，优先避免误报。

Fossabot 目前通过 GitHub 应用以公开预览版形式提供，每月提供免费额度，并与 Dependabot、Renovate 和 Snyk 集成，计划未来开放其自身的拉取请求。目标是减轻与依赖更新相关的繁琐工作，使开发团队能够专注于更高级别的任务。

---

## 5. Unix 哲学和文件系统访问让 Claude Code 变得出色。

**原文标题**: Unix philosophy and filesystem access makes Claude Code amazing

**原文链接**: [https://www.alephic.com/writing/the-magic-of-claude-code](https://www.alephic.com/writing/the-magic-of-claude-code)

诺亚·布里尔对 Claude Code 赞不绝口，称其为他主要的操作系统，尤其是在与 Obsidian 结合进行笔记记录时。他强调了使 Claude Code 卓越的两个关键要素：遵循 Unix 哲学和文件系统访问。

Unix 哲学强调简单、可组合的工具，专注做好一件事，这与 LLM 通过将输出“管道”到输入来有效利用工具的方式完美契合。这与复杂的工具形成对比，后者通常会阻碍 AI 性能。

文件系统访问解决了标准浏览器式 AI（如 ChatGPT 和 Claude）的局限性，这些 AI 存在内存不足和上下文窗口狭窄的问题。Claude Code 通过使用文件系统来编写笔记、积累知识和保持状态的能力，使其能够“思考”超出单个对话的范围。布里尔强调，模型有能力利用此功能，但其他界面限制了它们的能力。

他引用了 Boris Cherney 对“产品悬垂”的观察，即由于产品设计的限制，模型的性能未得到充分利用。布里尔通过开源 "Claudesidian" 和开发由 Claude Code 驱动的电子邮件助手 "Inbox Magic"，扩展了他的 Claude Code + Obsidian 设置。

总之，布里尔倡导利用文件系统来克服 LLM 中的内存限制，并坚持 Unix 哲学进行工具设计。他认为 Claude Code 的架构为构建可靠且可调试的 AI 代理提供了一个蓝图。

---

## 6. 展示HN：ChartDB Agent – 数据库模式设计的Cursor

**原文标题**: Show HN: ChartDB Agent – Cursor for DB schema design

**原文链接**: [https://app.chartdb.io/ai](https://app.chartdb.io/ai)

这篇“Show HN”帖子介绍了 ChartDB Agent，一个定位为“数据库模式设计的 Cursor”的工具。其核心理念是 ChartDB 帮助用户可视化数据库模式。它可能提供一个可视化界面或代理（可能是AI驱动的），以促进数据库模式的创建、理解和操作。

虽然帖子简短，但我们可以推断出以下几点：

*   **解决的问题：** 数据库模式设计可能很复杂且难以可视化，导致错误和效率低下。
*   **解决方案：** ChartDB 提供了一种可视化呈现和交互数据库模式的方式。
*   **主要功能：** 数据库模式的可视化。
*   **目标受众：** 开发人员、数据库管理员以及任何参与数据库设计的人员。
*   **潜在优势：** 提高理解、简化设计、减少数据库模式中的错误。
*   **“数据库模式设计的 Cursor”** 暗示 ChartDB 旨在成为数据库模式设计的首选工具，类似于 Cursor 是一款流行的代码编辑器。这表明其非常注重用户体验和效率。

本质上，ChartDB Agent 可能会通过可视化和直观的界面来简化和改进数据库模式的工作流程。

---

## 7. 麻省理工技术可远距离探测90米外的微生物

**原文标题**: MIT technology can see microbes from 90 meters away

**原文链接**: [https://www.asimov.press/p/hyperspectral](https://www.asimov.press/p/hyperspectral)

尼科·麦卡锡的文章探讨了生物传感器的进展，重点关注能够让我们从远处“看到”微生物的传感器开发。虽然自然界提供了多种多样的生物传感器，但生物工程师主要依赖于有限的报告蛋白，如GFP，这需要近距离观察。

最近，麻省理工学院的科学家开发了一种新型传感器，使用安装在无人机上的高光谱相机，可在高达90米远的距离内进行检测。这项技术在《自然·生物技术》杂志上进行了详细介绍，它能够监测工程细菌在生态系统中感应到的分子。

该突破涉及使用最初由美国宇航局开发的高光谱相机，来检测工程微生物产生的特定分子的独特光吸收和反射模式。研究人员确定胆绿素IXα和细菌叶绿素a为有效的“高光谱报告蛋白”。他们对恶臭假单胞菌和明胶红细菌进行了工程改造，使其产生这些分子，将微生物喷洒在土壤上，并成功地使用高光谱成像从空中检测到它们。

尽管具有潜力，但这种工程微生物的环境释放面临监管障碍。美国环保署监督的《有毒物质控制法》(TSCA)基于其工程方法而非安全性来监管这些微生物。虽然像Pivot Bio这样的一些公司已经克服了这些监管，但文章强调，过时的规则阻碍了环境生物传感器的商业化。文章强调了推进传感器技术以测量以前无法到达的位置的生物学的重要性，以及更新法规以促进这些技术负责任应用的需求。

---

## 8. 我们的努力，部分地，定义了我们。

**原文标题**: Our efforts, in part, define us

**原文链接**: [https://weakty.com/posts/efforts/](https://weakty.com/posts/efforts/)

本文探讨了作者作为软件顾问，对人工智能在其工作中日益增长的作用所产生的矛盾情绪，以及自动化对身份和成就感的更广泛影响。作者纠结于“我们的努力在某种程度上定义了我们”的观点，并质疑当技术使原本费力的任务变得毫不费力时会发生什么。

作者以摄影师因数码摄影的普及而失去热情为例，说明了技术简化任务时可能出现的“隐性损失”。他们担心，在编码中越来越多地使用人工智能，虽然可能是有益的，但会降低从这项技能中获得的价值和乐趣，从而导致一种悲伤和意义丧失的感觉。

作者注意到领导层推动在工作场所整合人工智能，并对员工体验的贬值以及对生产优先于个人视角的担忧表示关注。他们承认人工智能仅仅是一种工具的观点，但仍然强调他们的匮乏感和失落感。

最终，作者对日益自动化的世界中工作和身份的未来感到疑惑。他们质疑人们是否会被驱使去从事更小众、更费力的活动，还是会变得沮丧和模糊不清。他们也承认，对于某些人来说，人工智能可能会让他们自由地追求生活中其他有意义的方面。然而，作者仍然怀疑，除非对工作的期望得到改革，否则这些技术进步是否会提高士气。作者以质疑的口吻结束，即是否值得付出努力。

---

## 9. 我只用谷歌表格。

**原文标题**: I only use Google Sheets

**原文链接**: [https://mayberay.bearblog.dev/why-i-only-use-google-sheets/](https://mayberay.bearblog.dev/why-i-only-use-google-sheets/)

为什么我只用 Google Sheets

---

## 10. 激光网络协议

**原文标题**: IP over Lasers

**原文链接**: [https://www.mikekohn.net/micro/ip_over_lasers.php](https://www.mikekohn.net/micro/ip_over_lasers.php)

迈克·科恩的文章《激光上的IP协议》描述了一个使用激光链路通过互联网协议（IP）传输数据的项目。该项目旨在建立一种使用光而不是无线电波的无线网络连接。

作者详细介绍了所使用的硬件和软件组件。硬件包括激光器、光电二极管、用于聚焦激光束的透镜和微控制器（本例中为PIC微控制器）来调制和解调数据。该项目使用简单的开关键控（OOK）调制，其中激光器要么打开（表示“1”），要么关闭（表示“0”）。

该软件涉及将IP数据包编码成可以通过激光链路传输的比特流。PIC微控制器被编程为处理串行通信、调制和解调。作者使用一台PC来生成和接收IP数据包，然后将其发送到微控制器，以便通过激光链路传输。

文章重点介绍了项目过程中遇到的一些挑战。这些挑战包括精确对准激光器和光电二极管、处理环境光干扰以及确保可靠的数据传输。作者还讨论了简单OOK调制方案的局限性，并建议更复杂的调制技术可以提高性能。

本质上，这篇文章记录了作者创建基于激光的基本、低带宽IP通信系统的实验，说明了这种无线通信中涉及的基本原理和挑战。它作为IP通信概念和微控制器在独特网络环境中的应用的实际演示。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 2 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 3 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 4 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 5 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 6 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 7 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 8 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 9 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 10 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 11 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 12 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 13 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 14 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 15 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 16 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 17 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 18 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 19 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 20 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 21 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 22 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 23 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 24 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 25 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 26 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 27 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 28 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 29 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 30 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 31 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 32 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 33 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 34 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 35 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 36 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 37 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 38 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 39 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 40 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 41 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 42 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 43 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 44 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 45 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 46 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 47 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 48 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 49 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 50 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 51 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 52 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 53 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 54 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 55 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 56 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 57 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 58 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 59 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 60 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 61 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 62 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 63 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 64 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 65 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 66 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 67 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 68 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 69 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 70 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 71 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 72 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 73 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 74 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 75 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 76 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 77 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 78 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 79 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 80 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 81 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 82 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 83 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 84 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 85 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 86 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 87 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 88 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 89 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 90 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 91 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 92 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 93 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 94 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 95 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 96 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 97 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 98 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 99 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 100 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 101 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 102 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 103 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 104 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 105 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 106 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 107 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 108 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 109 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 110 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 111 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 112 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 113 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 114 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 115 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 116 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 117 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 118 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 119 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 120 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 121 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 122 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 123 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 124 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 125 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 126 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 127 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 128 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 129 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 130 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 131 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 132 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 133 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 134 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 135 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 136 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 137 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 138 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 139 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 140 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 141 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 142 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 143 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 144 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 145 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 146 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 147 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 148 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 149 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 150 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 151 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 152 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 153 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 154 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 155 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 156 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 157 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 158 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 159 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 160 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 161 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 162 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 163 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 164 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 165 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 166 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 167 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 168 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 169 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 170 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 171 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 172 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 173 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 174 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 175 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 176 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 177 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 178 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 179 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 180 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 181 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 182 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 183 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 184 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 185 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 186 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 187 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 188 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 189 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 190 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 191 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 192 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 193 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 194 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 195 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 196 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
