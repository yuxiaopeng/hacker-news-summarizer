# Hacker News 热门文章摘要 (2026-01-23)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Gas Town 的智能体模式、设计瓶颈与大规模氛围感编码

**原文标题**: Gas Town's Agent Patterns, Design Bottlenecks, and Vibecoding at Scale

**原文链接**: [https://maggieappleton.com/gastown](https://maggieappleton.com/gastown)

Steve Yegge 的“Gas Town”是一个雄心勃勃的、“氛围感驱动”（vibecoded）的智能体编排器，能够同时运行数十个编程智能体。尽管作者将其批评为一个混乱、低效且昂贵的“烂摊子”，但他们认为这是一件至关重要的“设计虚构”（design fiction）作品，揭示了未来智能体软件开发所面临的约束。

文章强调了编程本质的两个主要转变：

1. **设计成为新瓶颈：** 当智能体几乎可以瞬间实现代码时，瓶颈便从开发转移到了高层设计和规划。如果没有人类的品味、远见和架构意图，智能体的高速产出将导致“氛围感设计”出的系统——即建立在糟糕抽象之上的、庞大且令人费解的“工业垃圾”。
2. **新兴的编排模式：** 尽管过程混乱，但 Gas Town 通过专业化、层级化的角色为未来的智能体系统勾勒了蓝图：
    * **市长 (The Mayor)：** 充当人类管家，负责协调工作而不直接编写代码。
    * **臭鼬 (Polecats)：** 负责孤立任务的临时底层苦力。
    * **见证者与精炼厂 (The Witness & Refinery)：** 负责排除故障并管理复杂合并队列的监管智能体。

为了解决“上下文腐烂”问题，Gas Town 引入了 “Beads”——以 JSON 格式存储在 Git 中的可追踪工作单元。这使得智能体的身份和任务即使在单个 LLM 会话终止并重启后仍能保持持久性，从而实现“永续”编排。

最终，Gas Town 表明工程开发的未来不仅在于更好的代码自动补全，更在于管理一个专业智能体的“动物园”。虽然 Gas Town 本身“用起来是一场噩梦”，但其层级化监管和持久化任务追踪的模式，很可能成为未来更成熟、专业的工具标准。

---

## 2. Radicle：主权锻造场

**原文标题**: Radicle: The Sovereign Forge

**原文链接**: [https://radicle.xyz](https://radicle.xyz)

Radicle 是一个去中心化的点对点 (P2P) 代码协作平台，旨在作为中心化托管服务的“主权”替代方案。它直接构建在 Git 之上，通过在独立节点网络中复制仓库，消除了对第三方中间机构的依赖，确保用户对其数据和工作流拥有完整的所有权。

该平台具有以下核心特征：
* **主权与自治：** 通过运行自己的节点，用户可以创建一个抗审查的环境。没有任何单一实体能够控制网络或其数据。
* **本地优先架构：** Radicle 提供全功能的离线能力。由于所有社交制品（Social Artifacts）都以 Git 对象的形式存储，数据所有权使迁移和备份变得简单。
* **加密安全性：** 该协议利用公钥加密技术对所有交互进行签名，允许系统验证代码和社交元数据的真实性与作者身份。
* **可扩展性：** 通过“协作对象”(COBs)，议题（Issues）、讨论和代码审查等社交功能被实现为 Git 对象。这种模块化设计允许开发者扩展平台，并更换命令行界面 (CLI)、Web 界面或终端用户界面 (TUI) 等组件。

Radicle 技术栈包括 Radicle 节点和 HTTP 守护进程。它目前兼容 Linux、macOS 和 BSD。自 2024 年底发布 1.0 版本以来，该项目保持着稳定的发布周期，并在 2026 年初达到 1.6.0 版本。Radicle 是采用 MIT 和 Apache 2.0 协议的免费开源软件，旨在培育一个具有韧性的社区驱动生态系统，以实现安全的代码协作。

---

## 3. 从黑胶唱片启动 (2020)

**原文标题**: Booting from a vinyl record (2020)

**原文链接**: [https://boginjr.com/it/sw/dev/vinyl-boot/](https://boginjr.com/it/sw/dev/vinyl-boot/)

在这个技术项目中，Jozef Bogin 展示了一项创意十足的复古计算壮举：使用黑胶唱片作为存储介质来启动一台 IBM PC（具体为原始的 Model 5150 型号）。

该项目利用了 IBM 5150 一个被很大程度上遗忘的功能——内置磁带接口。在软盘成为标准之前，早期个人电脑的设计初衷是使用标准音频磁带录音机来保存和加载数据。Bogin 意识到，既然 PC 将这些数据流视为简单的音频信号，那么理论上任何能够再现声音的模拟介质都可以承载数字数据。

为了实现这一目标，Bogin 使用频移键控（FSK）技术将一个小程序编码为音频音调，其中不同的频率代表二进制的 0 和 1。随后，这些“数据”被压制到黑胶唱片上。硬件连接方面，他使用一根自定义电缆将标准黑胶唱机连接到 PC 的磁带端口（5 针 DIN 接口），以确保信号电平匹配。

当 IBM PC 在没有软盘的情况下启动时，它会默认进入存储在 ROM 中的“磁带 BASIC”（Cassette BASIC）。通过输入 `LOAD` 命令并将唱针放在唱片上，PC 会将来自黑胶唱片的音频频率解析为数字代码，并将其直接加载到内存中。

尽管面临信噪比和黑胶唱片物理缺陷（可能导致数据损坏）等挑战，Bogin 仍成功加载并运行了一个“Hello World”程序和一个小型图形演示。该项目突显了 20 世纪 80 年代硬件的灵活性，并在模拟音乐文化与数字计算历史之间搭建了一座奇妙的桥梁。

---

## 4. AI是一匹马 (2024)

**原文标题**: AI is a horse (2024)

**原文链接**: [https://kconner.com/2024/08/02/ai-is-a-horse.html](https://kconner.com/2024/08/02/ai-is-a-horse.html)

《人工智能是马》（2024）利用马这一隐喻，定义了人工智能当前的能力与局限。该作品指出，虽然人工智能在速度和效率上超越了人类，但它缺乏像火车等工业系统那样的可靠性和结构性。

核心论点包括：
*   **资源密集型：** 像马一样，人工智能的维护成本高昂，且“消耗”大量资源。
*   **缺乏自主性：** 人工智能无法独立运行；它需要持续的人工引导和具体指令才能到达目的地或保持在正轨。
*   **人工监督：** 即使人工智能看似运行正常，用户也必须保持掌控，以防止其偏离目标。
*   **有限的能动性：** 作者指出，虽然你可以为人工智能提供数据或提示词（将其领到水边），但你无法强迫其产生特定的高质量产出或“思考”过程。
*   **响应性：** 高性能人工智能的特征在于其对细微提示或“鞭影”的敏感度。
*   **警惕拟人化：** 文章最后警告人们要警惕那些过度模仿人类语言或意识的人工智能（“会说话的那些”）。

总体而言，该摘要将人工智能描述为一种功能强大但性情多变的工具，它需要的是熟练的“骑手”，而非完全自主的智能体。

---

## 5. KORG phase8 – Acoustic Synthesizer

**原文标题**: KORG phase8 – Acoustic Synthesizer

**原文链接**: [https://www.korg.com/us/products/dj/phase8/](https://www.korg.com/us/products/dj/phase8/)

KORG推出了phase8，这是一款开创性的八复音“声学合成器”，架起了物理发声与电子控制之间的桥梁。利用KORG专有的声学合成技术，该乐器通过物理振动体而非传统的振荡器产生声音，从而打造出一种有机且灵敏的体验，能够对触摸和声学反馈做出实时响应。

phase8的核心是八个独立的机电声部，配备了可更换且可调律的钢制谐振器。该合成器随附13个按半音阶调律的谐振器，可同时安装其中8个，支持自定义音阶和音色。用户可以通过包络控制、模拟波形折叠和音高相关调制等电子参数来塑造声音。

phase8强调实时的物理交互。除了调节旋钮，音乐家还可以直接拨动、敲击或弹奏谐振器。内置的“AIR”滑块可用于增强或减弱这些物理交互的声学响应。在序列编排方面，该乐器配备了直观的多律动节奏序列器，支持步进编程、非量化实时录音以及跨8个存储槽的参数自动化。

接口配置十分强大，拥有MIDI、USB-MIDI、CV和Sync接口，可与外部设备无缝集成。这使得phase8既能由外部设备触发，也能作为控制器操控其他乐器。

KORG还提供预售专属礼包，其中包括三个限量版打击乐谐振器，专为实验性的触感声音探索而设计。phase8代表了对“模拟 vs 数字”界限的超越，提供了一种乐器仿佛具有“生命力”并能对环境做出独特响应的触觉体验。

---

## 6. Show HN: Zsweep – Play Minesweeper using only Vim motions

**原文标题**: Show HN: Zsweep – Play Minesweeper using only Vim motions

**原文链接**: [https://zsweep.com](https://zsweep.com)

**Zsweep** is a specialized version of the classic game Minesweeper designed for developers and power users who prefer keyboard-centric navigation. Its primary feature is the integration of **Vim motions**, allowing players to navigate the grid and interact with the game without using a mouse.

Key features and controls include:
*   **Grid Sizes:** Supports standard configurations, including 9x9, 16x16, and 30x16.
*   **Vim Integration:** Movement is handled via standard Vim directional keys.
*   **Action Commands:** Players use the **Spacebar** to reveal cells and the **forward slash (/)** to flag mines or perform "chords" (clearing surrounding non-mine squares).
*   **Game Management:** Quick shortcuts are available for restarting (Tab) and accessing settings (Esc).

By replacing traditional mouse clicks with efficient keyboard shortcuts, Zsweep offers a fast-paced, "mouse-free" experience tailored to the workflow of Vim enthusiasts.

---

## 7. Proton Spam and the AI Consent Problem

**原文标题**: Proton Spam and the AI Consent Problem

**原文链接**: [https://dbushell.com/2026/01/22/proton-spam/](https://dbushell.com/2026/01/22/proton-spam/)

生成摘要时出错

---

## 8. Show HN: Whosthere: A LAN discovery tool with a modern TUI, written in Go

**原文标题**: Show HN: Whosthere: A LAN discovery tool with a modern TUI, written in Go

**原文链接**: [https://github.com/ramonvermeulen/whosthere](https://github.com/ramonvermeulen/whosthere)

生成摘要时出错

---

## 9. I built a light that reacts to radio waves [video]

**原文标题**: I built a light that reacts to radio waves [video]

**原文链接**: [https://www.youtube.com/watch?v=moBCOEiqiPs](https://www.youtube.com/watch?v=moBCOEiqiPs)

生成摘要时出错

---

## 10. Three RCEs in Ilias Learning Management System

**原文标题**: Three RCEs in Ilias Learning Management System

**原文链接**: [https://srlabs.de/blog/breaking-ilias-part-2-three-to-rce](https://srlabs.de/blog/breaking-ilias-part-2-three-to-rce)

生成摘要时出错

---

## 11. Updates to our web search products and  Programmable Search Engine capabilities

**原文标题**: Updates to our web search products and  Programmable Search Engine capabilities

**原文链接**: [https://programmablesearchengine.googleblog.com/2026/01/updates-to-our-web-search-products.html](https://programmablesearchengine.googleblog.com/2026/01/updates-to-our-web-search-products.html)

生成摘要时出错

---

## 12. European Alternatives

**原文标题**: European Alternatives

**原文链接**: [https://european-alternatives.eu](https://european-alternatives.eu)

生成摘要时出错

---

## 13. Show HN: isometric.nyc – giant isometric pixel art map of NYC

**原文标题**: Show HN: isometric.nyc – giant isometric pixel art map of NYC

**原文链接**: [https://cannoneyed.com/isometric-nyc/](https://cannoneyed.com/isometric-nyc/)

生成摘要时出错

---

## 14. Flying with Photons: Rendering Novel Views of Propagating Light

**原文标题**: Flying with Photons: Rendering Novel Views of Propagating Light

**原文链接**: [https://anaghmalik.com/FlyingWithPhotons/](https://anaghmalik.com/FlyingWithPhotons/)

生成摘要时出错

---

## 15. What has Docker become?

**原文标题**: What has Docker become?

**原文链接**: [https://tuananh.net/2026/01/20/what-has-docker-become/](https://tuananh.net/2026/01/20/what-has-docker-become/)

生成摘要时出错

---

## 16. GPTZero finds 100 new hallucinations in NeurIPS 2025 accepted papers

**原文标题**: GPTZero finds 100 new hallucinations in NeurIPS 2025 accepted papers

**原文链接**: [https://gptzero.me/news/neurips/](https://gptzero.me/news/neurips/)

生成摘要时出错

---

## 17. AI Usage Policy

**原文标题**: AI Usage Policy

**原文链接**: [https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md](https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md)

生成摘要时出错

---

## 18. Capital One to acquire Brex for $5.15B

**原文标题**: Capital One to acquire Brex for $5.15B

**原文链接**: [https://www.reuters.com/legal/transactional/capital-one-buy-fintech-firm-brex-515-billion-deal-2026-01-22/](https://www.reuters.com/legal/transactional/capital-one-buy-fintech-firm-brex-515-billion-deal-2026-01-22/)

生成摘要时出错

---

## 19. Why does SSH send 100 packets per keystroke?

**原文标题**: Why does SSH send 100 packets per keystroke?

**原文链接**: [https://eieio.games/blog/ssh-sends-100-packets-per-keystroke/](https://eieio.games/blog/ssh-sends-100-packets-per-keystroke/)

生成摘要时出错

---

## 20. I was banned from Claude for scaffolding a Claude.md file?

**原文标题**: I was banned from Claude for scaffolding a Claude.md file?

**原文链接**: [https://hugodaniel.com/posts/claude-code-banned-me/](https://hugodaniel.com/posts/claude-code-banned-me/)

生成摘要时出错

---

## 21. Presence in Death

**原文标题**: Presence in Death

**原文链接**: [https://rubinmuseum.org/presence-in-death/](https://rubinmuseum.org/presence-in-death/)

生成摘要时出错

---

## 22. The state of modern AI text to speech systems for screen reader users

**原文标题**: The state of modern AI text to speech systems for screen reader users

**原文链接**: [https://stuff.interfree.ca/2026/01/05/ai-tts-for-screenreaders.html](https://stuff.interfree.ca/2026/01/05/ai-tts-for-screenreaders.html)

生成摘要时出错

---

## 23. Microsoft mishandling example.com

**原文标题**: Microsoft mishandling example.com

**原文链接**: [https://tinyapps.org/blog/microsoft-mishandling-example-com.html](https://tinyapps.org/blog/microsoft-mishandling-example-com.html)

生成摘要时出错

---

## 24. Qwen3-TTS family is now open sourced: Voice design, clone, and generation

**原文标题**: Qwen3-TTS family is now open sourced: Voice design, clone, and generation

**原文链接**: [https://qwen.ai/blog?id=qwen3tts-0115](https://qwen.ai/blog?id=qwen3tts-0115)

生成摘要时出错

---

## 25. Replacing Protobuf with Rust to go 5 times faster

**原文标题**: Replacing Protobuf with Rust to go 5 times faster

**原文链接**: [https://pgdog.dev/blog/replace-protobuf-with-rust](https://pgdog.dev/blog/replace-protobuf-with-rust)

生成摘要时出错

---

## 26. Douglas Adams on the English–American cultural divide over "heroes"

**原文标题**: Douglas Adams on the English–American cultural divide over "heroes"

**原文链接**: [https://shreevatsa.net/post/douglas-adams-cultural-divide/](https://shreevatsa.net/post/douglas-adams-cultural-divide/)

生成摘要时出错

---

## 27. Why medieval city-builder video games are historically inaccurate (2020)

**原文标题**: Why medieval city-builder video games are historically inaccurate (2020)

**原文链接**: [https://www.leidenmedievalistsblog.nl/articles/why-medieval-city-builder-video-games-are-historically-inaccurate](https://www.leidenmedievalistsblog.nl/articles/why-medieval-city-builder-video-games-are-historically-inaccurate)

生成摘要时出错

---

## 28. Your app subscription is now my weekend project

**原文标题**: Your app subscription is now my weekend project

**原文链接**: [https://rselbach.com/your-sub-is-now-my-weekend-project](https://rselbach.com/your-sub-is-now-my-weekend-project)

生成摘要时出错

---

## 29. Show HN: S2-lite, an open source Stream Store

**原文标题**: Show HN: S2-lite, an open source Stream Store

**原文链接**: [https://github.com/s2-streamstore/s2](https://github.com/s2-streamstore/s2)

生成摘要时出错

---

## 30. The lost art of XML

**原文标题**: The lost art of XML

**原文链接**: [https://marcosmagueta.com/blog/the-lost-art-of-xml/](https://marcosmagueta.com/blog/the-lost-art-of-xml/)

生成摘要时出错

---

## 31. TI-99/4A: Leaning More on the Firmware

**原文标题**: TI-99/4A: Leaning More on the Firmware

**原文链接**: [https://bumbershootsoft.wordpress.com/2026/01/17/ti-99-4a-leaning-more-heavily-on-the-firmware/](https://bumbershootsoft.wordpress.com/2026/01/17/ti-99-4a-leaning-more-heavily-on-the-firmware/)

生成摘要时出错

---

## 32. Isometric NYC

**原文标题**: Isometric NYC

**原文链接**: [https://cannoneyed.com/projects/isometric-nyc](https://cannoneyed.com/projects/isometric-nyc)

生成摘要时出错

---

## 33. Scaling PostgreSQL to power 800M ChatGPT users

**原文标题**: Scaling PostgreSQL to power 800M ChatGPT users

**原文链接**: [https://openai.com/index/scaling-postgresql/](https://openai.com/index/scaling-postgresql/)

生成摘要时出错

---

## 34. Variation on Iota

**原文标题**: Variation on Iota

**原文链接**: [https://www.toolofthought.com/posts/variation-on-iota](https://www.toolofthought.com/posts/variation-on-iota)

生成摘要时出错

---

## 35. Scientists used the same data, but their politics predicted the results

**原文标题**: Scientists used the same data, but their politics predicted the results

**原文链接**: [https://www.psypost.org/158-scientists-used-the-same-data-but-their-politics-predicted-the-results/](https://www.psypost.org/158-scientists-used-the-same-data-but-their-politics-predicted-the-results/)

生成摘要时出错

---

## 36. What Will You Do When AI runs Out of Money and Disappear?

**原文标题**: What Will You Do When AI runs Out of Money and Disappear?

**原文链接**: [https://louwrentius.com/what-will-you-do-when-ai-will-run-out-of-money-and-disappear.html](https://louwrentius.com/what-will-you-do-when-ai-will-run-out-of-money-and-disappear.html)

生成摘要时出错

---

## 37. Improving the usability of C libraries in Swift

**原文标题**: Improving the usability of C libraries in Swift

**原文链接**: [https://www.swift.org/blog/improving-usability-of-c-libraries-in-swift/](https://www.swift.org/blog/improving-usability-of-c-libraries-in-swift/)

生成摘要时出错

---

## 38. Our collective obsession with boredom: Interview with a boredom lab researcher

**原文标题**: Our collective obsession with boredom: Interview with a boredom lab researcher

**原文链接**: [https://nautil.us/why-the-do-nothing-challenge-doesnt-do-much-for-you-1262005/](https://nautil.us/why-the-do-nothing-challenge-doesnt-do-much-for-you-1262005/)

生成摘要时出错

---

## 39. 'Askers' vs. 'Guessers' (2010)

**原文标题**: 'Askers' vs. 'Guessers' (2010)

**原文链接**: [https://www.theatlantic.com/national/2010/05/askers-vs-guessers/340891/](https://www.theatlantic.com/national/2010/05/askers-vs-guessers/340891/)

生成摘要时出错

---

## 40. In Europe, wind and solar overtake fossil fuels

**原文标题**: In Europe, wind and solar overtake fossil fuels

**原文链接**: [https://e360.yale.edu/digest/europe-wind-solar-fossil-fuels](https://e360.yale.edu/digest/europe-wind-solar-fossil-fuels)

生成摘要时出错

---

## 41. RT Superconductivity at 298K in Ternary LaScH System at High-Pressure Conditions

**原文标题**: RT Superconductivity at 298K in Ternary LaScH System at High-Pressure Conditions

**原文链接**: [https://arxiv.org/abs/2510.01273](https://arxiv.org/abs/2510.01273)

生成摘要时出错

---

## 42. CSS Optical Illusions

**原文标题**: CSS Optical Illusions

**原文链接**: [https://alvaromontoro.com/blog/68091/css-optical-illusions](https://alvaromontoro.com/blog/68091/css-optical-illusions)

生成摘要时出错

---

## 43. AnswerThis (YC F25) Is Hiring

**原文标题**: AnswerThis (YC F25) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/answerthis/jobs/r5VHmSC-ai-agent-orchestration](https://www.ycombinator.com/companies/answerthis/jobs/r5VHmSC-ai-agent-orchestration)

生成摘要时出错

---

## 44. Writing First, Tooling Second

**原文标题**: Writing First, Tooling Second

**原文链接**: [https://susam.net/writing-first-tooling-second.html](https://susam.net/writing-first-tooling-second.html)

生成摘要时出错

---

## 45. Bugs Apple Loves

**原文标题**: Bugs Apple Loves

**原文链接**: [https://www.bugsappleloves.com](https://www.bugsappleloves.com)

生成摘要时出错

---

## 46. Design Thinking Books (2024)

**原文标题**: Design Thinking Books (2024)

**原文链接**: [https://www.designorate.com/design-thinking-books/](https://www.designorate.com/design-thinking-books/)

生成摘要时出错

---

## 47. Tech Is Fun Again: The Tech Monoculture Is Finally Breaking

**原文标题**: Tech Is Fun Again: The Tech Monoculture Is Finally Breaking

**原文链接**: [http://www.jasonwillems.com/technology/2025/12/17/Tech-Is-Fun-Again/](http://www.jasonwillems.com/technology/2025/12/17/Tech-Is-Fun-Again/)

生成摘要时出错

---

## 48. Yann LeCun's new venture is a contrarian bet against large language models

**原文标题**: Yann LeCun's new venture is a contrarian bet against large language models

**原文链接**: [https://www.technologyreview.com/2026/01/22/1131661/yann-lecuns-new-venture-ami-labs/](https://www.technologyreview.com/2026/01/22/1131661/yann-lecuns-new-venture-ami-labs/)

生成摘要时出错

---

## 49. Stunnel

**原文标题**: Stunnel

**原文链接**: [https://www.stunnel.org/](https://www.stunnel.org/)

生成摘要时出错

---

## 50. 'Active' sitting is better for brain health: review of studies

**原文标题**: 'Active' sitting is better for brain health: review of studies

**原文链接**: [https://www.sciencealert.com/not-all-sitting-is-equal-one-type-was-just-linked-to-better-brain-health](https://www.sciencealert.com/not-all-sitting-is-equal-one-type-was-just-linked-to-better-brain-health)

生成摘要时出错

---

## 51. Recent discoveries on the acquisition of the highest levels of human performance

**原文标题**: Recent discoveries on the acquisition of the highest levels of human performance

**原文链接**: [https://www.science.org/doi/abs/10.1126/science.adt7790](https://www.science.org/doi/abs/10.1126/science.adt7790)

生成摘要时出错

---

## 52. Show HN: BrowserOS – "Claude Cowork" in the browser

**原文标题**: Show HN: BrowserOS – "Claude Cowork" in the browser

**原文链接**: [https://github.com/browseros-ai/BrowserOS](https://github.com/browseros-ai/BrowserOS)

生成摘要时出错

---

## 53. Tree-sitter vs. Language Servers

**原文标题**: Tree-sitter vs. Language Servers

**原文链接**: [https://lambdaland.org/posts/2026-01-21_tree-sitter_vs_lsp/](https://lambdaland.org/posts/2026-01-21_tree-sitter_vs_lsp/)

生成摘要时出错

---

## 54. Show HN: Text-to-video model from scratch (2 brothers, 2 years, 2B params)

**原文标题**: Show HN: Text-to-video model from scratch (2 brothers, 2 years, 2B params)

**原文链接**: [https://huggingface.co/collections/Linum-AI/linum-v2-2b-text-to-video](https://huggingface.co/collections/Linum-AI/linum-v2-2b-text-to-video)

生成摘要时出错

---

## 55. Doctors in Brazil using tilapia fish skin to treat burn victims (2017)

**原文标题**: Doctors in Brazil using tilapia fish skin to treat burn victims (2017)

**原文链接**: [https://www.pbs.org/newshour/health/brazilian-city-uses-tilapia-fish-skin-treat-burn-victims](https://www.pbs.org/newshour/health/brazilian-city-uses-tilapia-fish-skin-treat-burn-victims)

生成摘要时出错

---

## 56. Why I don't have fun with Claude Code

**原文标题**: Why I don't have fun with Claude Code

**原文链接**: [https://brennan.io/2026/01/23/claude-code/](https://brennan.io/2026/01/23/claude-code/)

生成摘要时出错

---

## 57. ISO PDF spec is getting Brotli – ~20 % smaller documents with no quality loss

**原文标题**: ISO PDF spec is getting Brotli – ~20 % smaller documents with no quality loss

**原文链接**: [https://pdfa.org/want-to-make-your-pdfs-20-smaller-for-free/](https://pdfa.org/want-to-make-your-pdfs-20-smaller-for-free/)

生成摘要时出错

---

## 58. eBay explicitly bans AI "buy for me" agents in user agreement update

**原文标题**: eBay explicitly bans AI "buy for me" agents in user agreement update

**原文链接**: [https://www.valueaddedresource.net/ebay-bans-ai-agents-updates-arbitration-user-agreement-feb-2026/](https://www.valueaddedresource.net/ebay-bans-ai-agents-updates-arbitration-user-agreement-feb-2026/)

生成摘要时出错

---

## 59. Show HN: Txt2plotter – True centerline vectors from Flux.2 for pen plotters

**原文标题**: Show HN: Txt2plotter – True centerline vectors from Flux.2 for pen plotters

**原文链接**: [https://github.com/malvarezcastillo/txt2plotter](https://github.com/malvarezcastillo/txt2plotter)

生成摘要时出错

---

## 60. Keeping 20k GPUs healthy

**原文标题**: Keeping 20k GPUs healthy

**原文链接**: [https://modal.com/blog/gpu-health](https://modal.com/blog/gpu-health)

生成摘要时出错

---

## 61. €5k Swiss cameras with zero electronics

**原文标题**: €5k Swiss cameras with zero electronics

**原文链接**: [https://www.alpa.swiss](https://www.alpa.swiss)

生成摘要时出错

---

## 62. Composing APIs and CLIs in the LLM era

**原文标题**: Composing APIs and CLIs in the LLM era

**原文链接**: [https://walters.app/blog/composing-apis-clis](https://walters.app/blog/composing-apis-clis)

生成摘要时出错

---

## 63. 30 Years of ReactOS

**原文标题**: 30 Years of ReactOS

**原文链接**: [https://reactos.org/blogs/30yrs-of-ros/](https://reactos.org/blogs/30yrs-of-ros/)

生成摘要时出错

---

## 64. Show HN: I've been using AI to analyze every supplement on the market

**原文标题**: Show HN: I've been using AI to analyze every supplement on the market

**原文链接**: [https://pillser.com/](https://pillser.com/)

生成摘要时出错

---

## 65. Turso is an in-process SQL database, compatible with SQLite

**原文标题**: Turso is an in-process SQL database, compatible with SQLite

**原文链接**: [https://github.com/tursodatabase/turso](https://github.com/tursodatabase/turso)

生成摘要时出错

---

## 66. Project Mercury and the Sofar Bomb

**原文标题**: Project Mercury and the Sofar Bomb

**原文链接**: [https://www.thequantumcat.space/p/project-mercury-and-the-sofar-bomb](https://www.thequantumcat.space/p/project-mercury-and-the-sofar-bomb)

生成摘要时出错

---

## 67. Show HN: Interactive physics simulations I built while teaching my daughter

**原文标题**: Show HN: Interactive physics simulations I built while teaching my daughter

**原文链接**: [https://www.projectlumen.app/](https://www.projectlumen.app/)

生成摘要时出错

---

## 68. Show HN: AskUCP – UCP protocol explorer showing all products on Shopify

**原文标题**: Show HN: AskUCP – UCP protocol explorer showing all products on Shopify

**原文链接**: [https://askucp.com/](https://askucp.com/)

生成摘要时出错

---

## 69. It looks like the status/need-triage label was removed

**原文标题**: It looks like the status/need-triage label was removed

**原文链接**: [https://github.com/google-gemini/gemini-cli/issues/16728](https://github.com/google-gemini/gemini-cli/issues/16728)

生成摘要时出错

---

## 70. Satya Nadella: "We need to find something useful for AI"

**原文标题**: Satya Nadella: "We need to find something useful for AI"

**原文链接**: [https://www.pcgamer.com/software/ai/microsoft-ceo-warns-that-we-must-do-something-useful-with-ai-or-theyll-lose-social-permission-to-burn-electricity-on-it/](https://www.pcgamer.com/software/ai/microsoft-ceo-warns-that-we-must-do-something-useful-with-ai-or-theyll-lose-social-permission-to-burn-electricity-on-it/)

生成摘要时出错

---

## 71. Extracting a UART Password via SPI Flash Instruction Tracing

**原文标题**: Extracting a UART Password via SPI Flash Instruction Tracing

**原文链接**: [https://zuernerd.github.io/blog/2026/01/07/switch-password.html](https://zuernerd.github.io/blog/2026/01/07/switch-password.html)

生成摘要时出错

---

## 72. The mushroom making people hallucinate tiny humans

**原文标题**: The mushroom making people hallucinate tiny humans

**原文链接**: [https://www.bbc.com/future/article/20260121-the-mysterious-mushroom-that-makes-you-see-tiny-people](https://www.bbc.com/future/article/20260121-the-mysterious-mushroom-that-makes-you-see-tiny-people)

生成摘要时出错

---

## 73. SpaceX lowering orbits of 4,400 Starlink satellites for safety's sake

**原文标题**: SpaceX lowering orbits of 4,400 Starlink satellites for safety's sake

**原文链接**: [https://www.space.com/space-exploration/satellites/spacex-lowering-orbits-of-4-400-starlink-satellites-for-safetys-sake](https://www.space.com/space-exploration/satellites/spacex-lowering-orbits-of-4-400-starlink-satellites-for-safetys-sake)

生成摘要时出错

---

## 74. Tesla fined for repeatedly failing to help UK police over driving offences

**原文标题**: Tesla fined for repeatedly failing to help UK police over driving offences

**原文链接**: [https://www.bbc.co.uk/news/articles/c0r44zpprg7o](https://www.bbc.co.uk/news/articles/c0r44zpprg7o)

生成摘要时出错

---

## 75. Skill.md: An open standard for agent skills

**原文标题**: Skill.md: An open standard for agent skills

**原文链接**: [https://www.mintlify.com/blog/skill-md](https://www.mintlify.com/blog/skill-md)

生成摘要时出错

---

## 76. The Uncomfortable Math of Working for Yourself

**原文标题**: The Uncomfortable Math of Working for Yourself

**原文链接**: [https://thomasunise.com/the-uncomfortable-math-of-working-for-yourself/](https://thomasunise.com/the-uncomfortable-math-of-working-for-yourself/)

生成摘要时出错

---

## 77. Pandas 3.0

**原文标题**: Pandas 3.0

**原文链接**: [https://pandas.pydata.org/community/blog/pandas-3.0.html](https://pandas.pydata.org/community/blog/pandas-3.0.html)

生成摘要时出错

---

## 78. Mote: An Interactive Ecosystem Simulation [video]

**原文标题**: Mote: An Interactive Ecosystem Simulation [video]

**原文链接**: [https://www.youtube.com/watch?v=Hju0H3NHxVI](https://www.youtube.com/watch?v=Hju0H3NHxVI)

生成摘要时出错

---

## 79. Your brain on ChatGPT: Accumulation of cognitive debt when using an AI assistant

**原文标题**: Your brain on ChatGPT: Accumulation of cognitive debt when using an AI assistant

**原文链接**: [https://www.media.mit.edu/publications/your-brain-on-chatgpt/](https://www.media.mit.edu/publications/your-brain-on-chatgpt/)

生成摘要时出错

---

## 80. From stealth blackout to whitelisting: Inside the Iranian shutdown

**原文标题**: From stealth blackout to whitelisting: Inside the Iranian shutdown

**原文链接**: [https://www.kentik.com/blog/from-stealth-blackout-to-whitelisting-inside-the-iranian-shutdown/](https://www.kentik.com/blog/from-stealth-blackout-to-whitelisting-inside-the-iranian-shutdown/)

生成摘要时出错

---

## 81. Reverse engineering Lyft Bikes for fun (and profit?)

**原文标题**: Reverse engineering Lyft Bikes for fun (and profit?)

**原文链接**: [https://ilanbigio.com/blog/lyft-bikes.html](https://ilanbigio.com/blog/lyft-bikes.html)

生成摘要时出错

---

## 82. In Praise of APL (1977)

**原文标题**: In Praise of APL (1977)

**原文链接**: [https://www.jsoftware.com/papers/perlis77.htm](https://www.jsoftware.com/papers/perlis77.htm)

生成摘要时出错

---

## 83. Miami, your Waymo ride is ready

**原文标题**: Miami, your Waymo ride is ready

**原文链接**: [https://waymo.com/blog/2026/01/miami-your-waymo-ride-is-ready](https://waymo.com/blog/2026/01/miami-your-waymo-ride-is-ready)

生成摘要时出错

---

## 84. Show HN: Synesthesia, make noise music with a colorpicker

**原文标题**: Show HN: Synesthesia, make noise music with a colorpicker

**原文链接**: [https://visualnoise.ca](https://visualnoise.ca)

生成摘要时出错

---

## 85. Show HN: First Claude Code client for Ollama local models

**原文标题**: Show HN: First Claude Code client for Ollama local models

**原文链接**: [https://github.com/21st-dev/1code](https://github.com/21st-dev/1code)

生成摘要时出错

---

## 86. Anthropic Economic Index economic primitives

**原文标题**: Anthropic Economic Index economic primitives

**原文链接**: [https://www.anthropic.com/research/anthropic-economic-index-january-2026-report](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)

生成摘要时出错

---

## 87. Lix – universal version control system for binary files

**原文标题**: Lix – universal version control system for binary files

**原文链接**: [https://lix.dev/blog/introducing-lix/](https://lix.dev/blog/introducing-lix/)

生成摘要时出错

---

## 88. Claude Chill: Fix Claude Code's flickering in terminal

**原文标题**: Claude Chill: Fix Claude Code's flickering in terminal

**原文链接**: [https://github.com/davidbeesley/claude-chill](https://github.com/davidbeesley/claude-chill)

生成摘要时出错

---

## 89. TrustTunnel: AdGuard VPN protocol goes open-source

**原文标题**: TrustTunnel: AdGuard VPN protocol goes open-source

**原文链接**: [https://adguard-vpn.com/en/blog/adguard-vpn-protocol-goes-open-source-meet-trusttunnel.html](https://adguard-vpn.com/en/blog/adguard-vpn-protocol-goes-open-source-meet-trusttunnel.html)

生成摘要时出错

---

## 90. JPEG XL Test Page

**原文标题**: JPEG XL Test Page

**原文链接**: [https://tildeweb.nl/~michiel/jxl/](https://tildeweb.nl/~michiel/jxl/)

生成摘要时出错

---

## 91. Show HN: Sweep, Open-weights 1.5B model for next-edit autocomplete

**原文标题**: Show HN: Sweep, Open-weights 1.5B model for next-edit autocomplete

**原文链接**: [https://huggingface.co/sweepai/sweep-next-edit-1.5B](https://huggingface.co/sweepai/sweep-next-edit-1.5B)

生成摘要时出错

---

## 92. Can you slim macOS down?

**原文标题**: Can you slim macOS down?

**原文链接**: [https://eclecticlight.co/2026/01/21/can-you-slim-macos-down/](https://eclecticlight.co/2026/01/21/can-you-slim-macos-down/)

生成摘要时出错

---

## 93. Why are there so many CPU bugs nowadays

**原文标题**: Why are there so many CPU bugs nowadays

**原文链接**: [https://mas.to/@gabrielesvelto/115939583202357863](https://mas.to/@gabrielesvelto/115939583202357863)

生成摘要时出错

---

## 94. Nested code fences in Markdown

**原文标题**: Nested code fences in Markdown

**原文链接**: [https://susam.net/nested-code-fences.html](https://susam.net/nested-code-fences.html)

生成摘要时出错

---

## 95. Bootstrapping Bun

**原文标题**: Bootstrapping Bun

**原文链接**: [https://walters.app/blog/bootstrapping-bun](https://walters.app/blog/bootstrapping-bun)

生成摘要时出错

---

## 96. Joe Armstrong and Jeremy Ruston – Intertwingling the Tiddlywiki with Erlang [video]

**原文标题**: Joe Armstrong and Jeremy Ruston – Intertwingling the Tiddlywiki with Erlang [video]

**原文链接**: [https://www.youtube.com/watch?v=Uv1UfLPK7_Q](https://www.youtube.com/watch?v=Uv1UfLPK7_Q)

生成摘要时出错

---

## 97. Show HN: CLI for working with Apple Core ML models

**原文标题**: Show HN: CLI for working with Apple Core ML models

**原文链接**: [https://github.com/schappim/coreml-cli](https://github.com/schappim/coreml-cli)

生成摘要时出错

---

## 98. Without benchmarking LLMs, you're likely overpaying

**原文标题**: Without benchmarking LLMs, you're likely overpaying

**原文链接**: [https://karllorey.com/posts/without-benchmarking-llms-youre-overpaying](https://karllorey.com/posts/without-benchmarking-llms-youre-overpaying)

生成摘要时出错

---

## 99. Autodesk burns the village to feed AI and the Cloud – cuts 7% of workforce

**原文标题**: Autodesk burns the village to feed AI and the Cloud – cuts 7% of workforce

**原文链接**: [https://blog.adafruit.com/2026/01/22/autodesk-burns-the-village-to-feed-ai-and-the-cloud-cuts-7-of-workforce/](https://blog.adafruit.com/2026/01/22/autodesk-burns-the-village-to-feed-ai-and-the-cloud-cuts-7-of-workforce/)

生成摘要时出错

---

## 100. Vibe a Guitar Pedal

**原文标题**: Vibe a Guitar Pedal

**原文链接**: [https://polyend.com/endless/](https://polyend.com/endless/)

生成摘要时出错

---

