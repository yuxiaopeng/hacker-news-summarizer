# Hacker News 热门文章摘要 (2026-06-25)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 赫库兰尼姆卷轴首次被成功解读

**原文标题**: A Herculaneum scroll has been read for the first time

**原文链接**: [https://scrollprize.org/firstscroll](https://scrollprize.org/firstscroll)

研究人员首次成功对一整卷碳化的赫库兰尼姆卷轴进行了虚拟展开与阅读，达成了历史性的里程碑。PHerc. 1667（卷轴4）自公元79年维苏威火山爆发以来一直处于密封状态，如今通过欧洲同步辐射装置（ESRF）的高分辨率X射线显微断层扫描技术，结合用于识别古代墨水的机器学习模型，实现了数字化重建。

修复后的文本长约1.4米，包含22栏希腊文字，是一部公元前2世纪的斯多葛学派伦理学著作。该作品探讨了人性与道德进步，并特别提到了哲学家克律西波斯的弟子阿里斯托克雷翁。

该项目还宣布了两项额外突破：
* **PHerc. Paris 4：** 新的3D墨水分割技术为先前的解读提供了独立验证。
* **PHerc. 139：** 研究人员成功阅读了卷轴的标题和作者——菲洛德穆的《论神》第8卷，证明了无需阅读正文即可识别卷轴内容。

这一成功是“维苏威挑战赛”（Vesuvius Challenge）的成果。该挑战赛是由Brent Seales教授、Nat Friedman和Daniel Gross共同发起的开放科学计划。其方法论依托于从项目公开竞赛中脱颖而出的全球研究人员和开发人员社区。为了推动进一步的发现，所有数据、代码和转录文本均已根据知识共享（Creative Commons）许可协议发布。这一成就证明，数百卷仍处于密封状态的卷轴是可以被修复的，为重现整座失落的古代哲学与文学图书馆提供了可能。

---

## 2. IBM发布1纳米以下芯片技术

**原文标题**: IBM debuts sub-1 nanometer chip technology

**原文链接**: [https://newsroom.ibm.com/2026-06-25-ibm-debuts-worlds-first-sub-1-nanometer-chip-technology](https://newsroom.ibm.com/2026-06-25-ibm-debuts-worlds-first-sub-1-nanometer-chip-technology)

2026年6月25日，IBM宣布了半导体技术的重大突破：推出全球首款亚1纳米（nm）芯片，具体为0.7纳米（7埃米）制程。这一里程碑由名为“nanostack”的新型3D晶体管架构驱动，标志着行业从纳米时代向原子级缩放的跨越。

nanostack架构基于IBM之前的纳米片（nanosheet）技术，通过垂直堆叠和交错排列晶体管实现。该设计使IBM能够在指甲盖大小的芯片上集成近1000亿个晶体管，其密度是2纳米技术的两倍。与2纳米制程相比，这款新芯片预计性能可提升50%，或能效提高70%。此外，它在SRAM缩放方面实现了40%的提升，这对于满足先进人工智能和云基础设施的高带宽需求至关重要。

该创新由位于纽约奥尔巴尼的IBM研究设施与ASML、泛林集团（Lam Research）以及东京电子（Tokyo Electron）等合作伙伴共同开发。该工艺利用高数值孔径（High NA）极紫外（EUV）光刻技术，实现了超高精度的电路印刷。

IBM预计该技术将使半导体缩放路线图至少再延长十年。公司预计nanostack架构将在未来五年内投入生产。此外，IBM还强调了其通过“Anderon”对未来计算的承诺——这是一家新成立的独立公司，也是全球首家纯代工模式的量子晶圆厂。

---

## 3. Oxide 计算机 3D 机架导览

**原文标题**: Oxide computer 3D rack guided tour

**原文链接**: [https://explorer.oxide.computer/](https://explorer.oxide.computer/)

Oxide Computer 的 “Explorer” 是一项交互式 3D 导览，展示了该公司垂直集成的机架级计算机。该系统旨在将超大规模云的效率引入本地数据中心，它将整个机架视为一个单一、统一的机器，而非零散服务器的集合。

**关键信息与设计特性：**

*   **集成机架架构：** 机架采用统一背板，消除了传统的乱糟糟布线。它使用盲插连接器，使计算节点能够直接滑入电源和数据织网，便于安装和维护。
*   **计算节点：** 这些高密度节点搭载 AMD EPYC 处理器，并配备大容量本地 NVMe 存储和内存。它们专为高性能工作负载设计，且完全无风扇，依靠机架的集中冷却系统散热。
*   **网络与电源：** 系统将基于 Tofino 的高速交换直接集成到机架架构中，无需外部机架顶置（ToR）交换机。电力通过高效直流母线分配，减少了能量转换损耗。
*   **垂直软件栈：** 核心优势在于协同设计的软件。Oxide 使用自研的开源固件（**Hubris**）、专用操作系统（**Helios**，基于 illumos）以及全面的控制平面（**Omicron**）。这实现了 API 驱动的硬件管理，提供了类似于公有云提供商的使用体验。

**主要结论：**
Oxide 机架旨在解决传统企业硬件的复杂性和可靠性问题。通过掌握从机械节点设计到底层固件再到管理软件的整个技术栈，Oxide 提供了一种“盒中云（cloud-in-a-box）”，在具备本地基础设施的控制力与安全性的同时，提供了公有云的自动化和可扩展性。

---

## 4. Zig 的新 bitCast 语义与 LLVM 后端改进

**原文标题**: Zig's new bitCast semantics and LLVM back end improvements

**原文链接**: [https://ziglang.org/devlog/2026/#2026-06-25](https://ziglang.org/devlog/2026/#2026-06-25)

2026 年中期的 Zig 开发日志重点介绍了在迈向 0.17.0 版本过程中，编译器性能、链接器能力以及构建系统架构方面取得的重大进展。

**新 @bitCast 语义与 LLVM 改进**
Matthew Lugg 针对 LLVM 后端实现了筹备已久的改进，涉及任意位宽整数（如 `u4`、`u40`）。这些类型在存储到内存时，现在会根据 ABI 大小进行零扩展或符号扩展，从而与 Clang 的行为保持一致并减少误编译。这一变化促使开发者对 `@bitCast` 进行了重新定义。`@bitCast` 此前是一种内存重新解释（因此依赖于字节序），现在则基于类型的“逻辑位布局”运行。这使得该内置函数与字节序无关，并在所有后端保持一致。这些优化为 Zig 编译器自身带来了 5% 的性能提升。

**ELF 链接器进展**
最初在 0.16.0 版本中引入的新 ELF 链接器，现在已经可以链接包含外部库（包括 libc 和 LLVM）的复杂项目。其核心优势在于高速增量编译；在 x86_64 Linux 上，某些项目的重新构建时间缩短至仅 30 毫秒。虽然目前尚不支持 Zig 代码的 DWARF 调试信息，但它显著加速了侧重于打印调试和快速迭代的开发周期。

**构建系统重构**
Andrew Kelley 宣布了构建系统的根本性架构转变，将“配置器 (configurer)”与“执行器 (maker)”分离。此前，整个构建系统会随 `build.zig` 一起重新编译。现在，`build.zig` 被编译成一个产生序列化二进制配置的小型“配置器”，而预编译且优化过的“执行器”负责执行实际的构建图。这一改变大幅降低了开销；`zig build -h` 的基准测试显示，总耗时（wall time）减少了 90%，CPU 周期减少了 95%。

---

## 5. OS9地图

**原文标题**: OS9Map

**原文链接**: [https://yllan.org/software/OS9Map/](https://yllan.org/software/OS9Map/)

**OS9Map** 是由 yllan 开发的一款软件应用，旨在为老旧的 Mac OS 9 操作系统引入 OpenStreetMap 功能。该工具于 2026 年 6 月 21 日发布，允许用户在复古硬件上浏览全球地图、搜索地标并管理地理位置。

**主要功能：**
*   **交互式地图画布：** 支持平滑滚动和平移，地图瓦片随用户移动动态加载。
*   **搜索功能：** 内置 Nominatim 查询功能，允许用户快速跳转至特定地址或地标。
*   **书签：** 用户可以将常用地点保存至专用菜单，以便快速访问。

**系统

该软件目前版本为 1.0.0，开发者提供了直接下载选项，并支持通过“Buy Me a Coffee”进行捐赠。

---

## 6. Show HN：受国际象棋启发的 Roguelike 游戏

**原文标题**: Show HN: Chess-Inspired Roguelike

**原文链接**: [https://princechazz.com](https://princechazz.com)

**CHAZZ** 是一款基于浏览器的回合制 Roguelike 游戏，它将国际象棋的战术深度与经典的地牢探险机制完美结合。这款由 Prince Chazz 开发的游戏，挑战玩家利用直接源自传统国际象棋棋子的移动和攻击模式，在一系列网格化的关卡中穿行。

核心玩法围绕着一名主角展开，其能力涵盖了兵（Pawn）、马（Knight）、象（Bishop）、车（Rook）和后（Queen）的特点。玩家必须运用策略，穿梭于布满同样遵循国际象棋规则的敌方单位的房间。胜利取决于谨慎的走位，在躲避敌人致命攻击线的同时“吃掉”对手。

秉承 Roguelike 类型的传统，游戏具有随机生成和永久死亡机制。随着玩家向更深层的关卡推进，遇到的敌人配置会愈发棘手。为了生存，玩家可以收集各种道具和强化物品来获得必要的增益，例如增加生命值、防御护甲或增强移动能力。这些元素使得每一局游戏都能产生多样的角色构建和不同的战略手段。

凭借极简的像素画风和直观的界面，*CHAZZ* 提供了独特的“易于上手，难于精通”的体验。它要求玩家提前预判数步走位，有效地将地牢探险转化为一场关乎空间布局与战术牺牲的高风险、快节奏谜题。

---

## 7. Apple raises prices of MacBooks, iPads

**原文标题**: Apple raises prices of MacBooks, iPads

**原文链接**: [https://www.reuters.com/world/asia-pacific/apple-raises-prices-macbooks-ipads-memory-costs-skyrocket-2026-06-25/](https://www.reuters.com/world/asia-pacific/apple-raises-prices-macbooks-ipads-memory-costs-skyrocket-2026-06-25/)

Unable to access the article link.

---

## 8. 品味无法通过单元测试。

**原文标题**: You can't unit test for taste

**原文链接**: [https://dev.karltryggvason.com/you-cant-unit-test-for-taste/](https://dev.karltryggvason.com/you-cant-unit-test-for-taste/)

In the blog post "You can't unit test for taste," the creator of the virtual running app **In the Long Run** details the development of a data pipeline designed to enrich global running routes with Points of Interest (POIs). 

Using **GeoNames** as a primary data source, the author collaborated with the AI agent **Claude** to build a processing stack featuring **Python, Apache Parquet, and DuckDB**. The pipeline filters millions of locations down to notable landmarks by using Wikipedia links and Wikidata language counts as signals for notoriety. 

A central theme of the article is the evolving role of AI in development. While the author initially intended for the LLM (Anthropic’s Haiku) to generate descriptive summaries and "solve" the feature, **hallucinations**—such as the AI misidentifying minor local parks as world-famous landmarks—forced a pivot. The LLM was ultimately relegated to a supporting role, providing subjective "significance scores" to help rank locations, while factual descriptions were pulled directly from Wikipedia.

The author also highlights the difficulty of automating "taste." Early iterations suffered from **geographical and linguistic biases**, often cluttering maps with every minor hamlet in English-speaking regions while overlooking significant sites elsewhere. To fix this, the author implemented per-route tuning and geographic radius filters to ensure a balanced mix of nature, history, and culture.

Ultimately, the author concludes that while AI is a powerful "senior mentor" for technical implementation, it cannot replace human judgment. Because there is no objective "ground truth" for what makes a landmark interesting, developers cannot rely on unit tests; instead, they must embrace manual iteration and subjective refinement to achieve a high-quality user experience.

---

## 9. Show HN: I made Google Trends for Hacker News by indexing 18 years of comments

**原文标题**: Show HN: I made Google Trends for Hacker News by indexing 18 years of comments

**原文链接**: [https://hackernewstrends.com](https://hackernewstrends.com)

生成摘要时出错

---

## 10. Besimple AI (YC P25) 正在招聘

**原文标题**: Besimple AI (YC P25) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/besimple-ai/jobs/yWfhhOR-strategic-projects-lead-audio-data](https://www.ycombinator.com/companies/besimple-ai/jobs/yWfhhOR-strategic-projects-lead-audio-data)

生成摘要时出错

---

## 11. I built a GPU back end for Emacs

**原文标题**: I built a GPU back end for Emacs

**原文链接**: [https://en.andros.dev/blog/4b707a03/how-i-built-a-gpu-backend-for-emacs/](https://en.andros.dev/blog/4b707a03/how-i-built-a-gpu-backend-for-emacs/)

生成摘要时出错

---

## 12. Half-Life 2 in a Browser

**原文标题**: Half-Life 2 in a Browser

**原文链接**: [https://hl2.slqnt.dev/](https://hl2.slqnt.dev/)

The provided text describes a project or interface designed to run the classic video game **Half-Life 2** directly within a web browser. 

The content "web hl2Downloading..." indicates the initialization phase of the software, where the browser fetches the necessary game assets and engine components to execute the game without a local installation. This project typically utilizes modern web technologies, such as **WebAssembly (WASM)** and **WebGL**, to port the Source Engine's capabilities to a browser environment.

**Key Points:**
*   **Browser Porting:** The project aims to make a historically resource-intensive PC game accessible through a standard web URL.
*   **Loading Process:** The "Downloading" status reflects the real-time transfer of data required to render the game’s 3D environments and physics.
*   **Technological Feasibility:** It highlights the advancement of web standards, allowing complex AAA titles to run cross-platform with minimal setup.

---

## 13. Early adversity leaves lasting molecular imprint across the body: primate study

**原文标题**: Early adversity leaves lasting molecular imprint across the body: primate study

**原文链接**: [https://medicalxpress.com/news/2026-06-early-life-adversity-molecular-imprint.html](https://medicalxpress.com/news/2026-06-early-life-adversity-molecular-imprint.html)

生成摘要时出错

---

## 14. 52-hertz whale

**原文标题**: 52-hertz whale

**原文链接**: [https://en.wikipedia.org/wiki/52-hertz_whale](https://en.wikipedia.org/wiki/52-hertz_whale)

生成摘要时出错

---

## 15. Tw-fade: pure CSS scroll-driven edge masking

**原文标题**: Tw-fade: pure CSS scroll-driven edge masking

**原文链接**: [https://pete.design/tw-fade](https://pete.design/tw-fade)

生成摘要时出错

---

## 16. Windows 10 quietly gets one more year of support and updates

**原文标题**: Windows 10 quietly gets one more year of support and updates

**原文链接**: [https://www.neowin.net/news/windows-10-quietly-gets-one-more-year-of-support-and-updates/](https://www.neowin.net/news/windows-10-quietly-gets-one-more-year-of-support-and-updates/)

生成摘要时出错

---

## 17. Show HN: Turn native language audio into flashcards and shadowing practice

**原文标题**: Show HN: Turn native language audio into flashcards and shadowing practice

**原文链接**: [https://lingochunk.com/try](https://lingochunk.com/try)

生成摘要时出错

---

## 18. Advanced Nintendo Entertainment System (ANES) – NES Modded to Use 2 PPUs

**原文标题**: Advanced Nintendo Entertainment System (ANES) – NES Modded to Use 2 PPUs

**原文链接**: [https://github.com/decrazyo/anes](https://github.com/decrazyo/anes)

生成摘要时出错

---

## 19. How to get your first customers [video]

**原文标题**: How to get your first customers [video]

**原文链接**: [https://www.ycombinator.com/library/SF-how-to-get-your-first-10-customers](https://www.ycombinator.com/library/SF-how-to-get-your-first-10-customers)

生成摘要时出错

---

## 20. Physicists Track and Trap the Elusive Neutrino

**原文标题**: Physicists Track and Trap the Elusive Neutrino

**原文链接**: [https://www.quantamagazine.org/how-physicists-track-and-trap-the-elusive-neutrino-20260624/](https://www.quantamagazine.org/how-physicists-track-and-trap-the-elusive-neutrino-20260624/)

生成摘要时出错

---

## 21. The disappearance of Japan's animators

**原文标题**: The disappearance of Japan's animators

**原文链接**: [https://economist.com/interactive/1843/2026/06/19/the-strange-disappearance-of-japans-animators](https://economist.com/interactive/1843/2026/06/19/the-strange-disappearance-of-japans-animators)

生成摘要时出错

---

## 22. LastPass notifies users of yet another data breach

**原文标题**: LastPass notifies users of yet another data breach

**原文链接**: [https://9to5mac.com/2026/06/23/lastpass-notifies-users-of-yet-another-data-breach/](https://9to5mac.com/2026/06/23/lastpass-notifies-users-of-yet-another-data-breach/)

生成摘要时出错

---

## 23. Political bias in AI: Where the AI models stand

**原文标题**: Political bias in AI: Where the AI models stand

**原文链接**: [https://trakkr.ai/bias](https://trakkr.ai/bias)

生成摘要时出错

---

## 24. Show HN: Persona.js – a vanilla-JS agent UI library with native WebMCP (MIT)

**原文标题**: Show HN: Persona.js – a vanilla-JS agent UI library with native WebMCP (MIT)

**原文链接**: [https://github.com/runtypelabs/persona](https://github.com/runtypelabs/persona)

生成摘要时出错

---

## 25. Cloudflare launched self-managed OAuth for all

**原文标题**: Cloudflare launched self-managed OAuth for all

**原文链接**: [https://blog.cloudflare.com/oauth-for-all/](https://blog.cloudflare.com/oauth-for-all/)

生成摘要时出错

---

## 26. The annotated PyTorch training loop

**原文标题**: The annotated PyTorch training loop

**原文链接**: [https://idlemachines.co.uk/essays/pytorch-training-loop](https://idlemachines.co.uk/essays/pytorch-training-loop)

生成摘要时出错

---

## 27. Show HN: MiniPCs.zip – Charting the Pareto frontier of Mini PCs

**原文标题**: Show HN: MiniPCs.zip – Charting the Pareto frontier of Mini PCs

**原文链接**: [https://minipcs.zip](https://minipcs.zip)

生成摘要时出错

---

## 28. Mixing Visual and Textual Code

**原文标题**: Mixing Visual and Textual Code

**原文链接**: [https://arxiv.org/abs/2603.15855](https://arxiv.org/abs/2603.15855)

生成摘要时出错

---

## 29. Show HN: Bible as RAG Database

**原文标题**: Show HN: Bible as RAG Database

**原文链接**: [https://www.crosscanon.com/](https://www.crosscanon.com/)

生成摘要时出错

---

## 30. Blogging can just be stating the obvious

**原文标题**: Blogging can just be stating the obvious

**原文链接**: [https://blog.jim-nielsen.com/2026/blogging-stating-the-obvious/](https://blog.jim-nielsen.com/2026/blogging-stating-the-obvious/)

生成摘要时出错

---

## 31. The unbearable cheapness of open weight models

**原文标题**: The unbearable cheapness of open weight models

**原文链接**: [https://jamesoclaire.com/2026/06/25/the-unbearable-cheapness-of-open-weight-models/](https://jamesoclaire.com/2026/06/25/the-unbearable-cheapness-of-open-weight-models/)

生成摘要时出错

---

## 32. SoftBank 2026 AGM [pdf]

**原文标题**: SoftBank 2026 AGM [pdf]

**原文链接**: [https://group.softbank/media/Project/sbg/sbg/pdf/ir/investors/shareholders/2026/shareholders-meeting_46_05_en.pdf](https://group.softbank/media/Project/sbg/sbg/pdf/ir/investors/shareholders/2026/shareholders-meeting_46_05_en.pdf)

生成摘要时出错

---

## 33. European Commission lines up Amazon and Microsoft for cloud gatekeeper status

**原文标题**: European Commission lines up Amazon and Microsoft for cloud gatekeeper status

**原文链接**: [https://www.theregister.com/legal/2026/06/25/european-commission-lines-up-amazon-and-microsoft-for-cloud-gatekeeper-status/5262127](https://www.theregister.com/legal/2026/06/25/european-commission-lines-up-amazon-and-microsoft-for-cloud-gatekeeper-status/5262127)

生成摘要时出错

---

## 34. Deno 2.9

**原文标题**: Deno 2.9

**原文链接**: [https://deno.com/blog/v2.9](https://deno.com/blog/v2.9)

生成摘要时出错

---

## 35. Puzzling Success of Overparameterization: Lottery Tickets or Escape Dimensions?

**原文标题**: Puzzling Success of Overparameterization: Lottery Tickets or Escape Dimensions?

**原文链接**: [https://infoscience.epfl.ch/entities/publication/9a49779b-f9f8-448d-b3d1-737c78455309](https://infoscience.epfl.ch/entities/publication/9a49779b-f9f8-448d-b3d1-737c78455309)

生成摘要时出错

---

## 36. LuaJIT 3.0 proposed syntax extensions

**原文标题**: LuaJIT 3.0 proposed syntax extensions

**原文链接**: [https://github.com/LuaJIT/LuaJIT/issues/1475](https://github.com/LuaJIT/LuaJIT/issues/1475)

生成摘要时出错

---

## 37. Ford AI hiccups push carmaker to rehire ‘gray beard’ inspectors

**原文标题**: Ford AI hiccups push carmaker to rehire ‘gray beard’ inspectors

**原文链接**: [https://www.bloomberg.com/news/articles/2026-06-25/ford-has-been-rehiring-quality-inspectors-after-ai-fell-short](https://www.bloomberg.com/news/articles/2026-06-25/ford-has-been-rehiring-quality-inspectors-after-ai-fell-short)

生成摘要时出错

---

## 38. Medical students are using popular research tool to pump out misleading studies

**原文标题**: Medical students are using popular research tool to pump out misleading studies

**原文链接**: [https://www.science.org/content/article/medical-students-are-using-popular-research-tool-pump-out-misleading-studies](https://www.science.org/content/article/medical-students-are-using-popular-research-tool-pump-out-misleading-studies)

生成摘要时出错

---

## 39. Anthropic says Alibaba illicitly extracted Claude AI model capabilities

**原文标题**: Anthropic says Alibaba illicitly extracted Claude AI model capabilities

**原文链接**: [https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/)

生成摘要时出错

---

## 40. Bohemia Interactive: Cold War Assault Remastered Source Code on GitHub

**原文标题**: Bohemia Interactive: Cold War Assault Remastered Source Code on GitHub

**原文链接**: [https://github.com/BohemiaInteractive/CWR](https://github.com/BohemiaInteractive/CWR)

生成摘要时出错

---

## 41. Supreme Court Gives Pesticide Corporations Immunity from Cancer Lawsuits

**原文标题**: Supreme Court Gives Pesticide Corporations Immunity from Cancer Lawsuits

**原文链接**: [https://www.foodandwaterwatch.org/2026/06/25/supreme-court-gives-pesticide-corporations-immunity-from-cancer-lawsuits/](https://www.foodandwaterwatch.org/2026/06/25/supreme-court-gives-pesticide-corporations-immunity-from-cancer-lawsuits/)

生成摘要时出错

---

## 42. Show HN: Secs-man, a secrets manager you can (not) rely on

**原文标题**: Show HN: Secs-man, a secrets manager you can (not) rely on

**原文链接**: [https://github.com/Fran314/secrets-manager-rs](https://github.com/Fran314/secrets-manager-rs)

生成摘要时出错

---

## 43. Markdy: Like Mermaid Diagrams, but for Motion

**原文标题**: Markdy: Like Mermaid Diagrams, but for Motion

**原文链接**: [https://markdy.com](https://markdy.com)

生成摘要时出错

---

## 44. Zombie unicorns are haunting Silicon Valley

**原文标题**: Zombie unicorns are haunting Silicon Valley

**原文链接**: [https://www.economist.com/business/2026/06/21/zombie-unicorns-are-haunting-silicon-valley](https://www.economist.com/business/2026/06/21/zombie-unicorns-are-haunting-silicon-valley)

生成摘要时出错

---

## 45. Dostoyevsky isn't difficult

**原文标题**: Dostoyevsky isn't difficult

**原文链接**: [https://www.autodidacts.io/dostoyevsky-isnt-difficult/](https://www.autodidacts.io/dostoyevsky-isnt-difficult/)

生成摘要时出错

---

## 46. Older tech workers are tapping out early

**原文标题**: Older tech workers are tapping out early

**原文链接**: [https://www.seattletimes.com/business/local-business/older-tech-workers-are-tapping-out-early-heres-what-that-looks-like/](https://www.seattletimes.com/business/local-business/older-tech-workers-are-tapping-out-early-heres-what-that-looks-like/)

生成摘要时出错

---

## 47. Lianda and the Long March

**原文标题**: Lianda and the Long March

**原文链接**: [https://blog.georeactor.com/books-06-26b](https://blog.georeactor.com/books-06-26b)

生成摘要时出错

---

## 48. OpenAI unveils its first custom chip, built by Broadcom

**原文标题**: OpenAI unveils its first custom chip, built by Broadcom

**原文链接**: [https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/)

生成摘要时出错

---

## 49. Show HN: StartupsBR – A map of Brazilian startups

**原文标题**: Show HN: StartupsBR – A map of Brazilian startups

**原文链接**: [https://www.startupsbr.com/sao-paulo](https://www.startupsbr.com/sao-paulo)

生成摘要时出错

---

## 50. Qualcomm to Acquire Modular

**原文标题**: Qualcomm to Acquire Modular

**原文链接**: [https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/](https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/)

生成摘要时出错

---

## 51. Lies, Damn Lies and Database Benchmarks

**原文标题**: Lies, Damn Lies and Database Benchmarks

**原文链接**: [https://questdb.com/blog/lies-damn-lies-and-database-benchmarks/](https://questdb.com/blog/lies-damn-lies-and-database-benchmarks/)

生成摘要时出错

---

## 52. Linux Cache Aware Scheduling Extended for Better Performance: 360% in MySQL

**原文标题**: Linux Cache Aware Scheduling Extended for Better Performance: 360% in MySQL

**原文链接**: [https://www.phoronix.com/news/Extended-Cache-Aware-Sched](https://www.phoronix.com/news/Extended-Cache-Aware-Sched)

生成摘要时出错

---

## 53. Updated Xbox Console Prices

**原文标题**: Updated Xbox Console Prices

**原文链接**: [https://news.xbox.com/en-us/2026/06/25/xbox-console-price-update/](https://news.xbox.com/en-us/2026/06/25/xbox-console-price-update/)

生成摘要时出错

---

## 54. The AI Data-Center Boom Is Sparking a Third Wave of Inflation

**原文标题**: The AI Data-Center Boom Is Sparking a Third Wave of Inflation

**原文链接**: [https://www.wsj.com/economy/the-data-center-boom-is-sparking-a-third-wave-of-inflation-926adc6e](https://www.wsj.com/economy/the-data-center-boom-is-sparking-a-third-wave-of-inflation-926adc6e)

生成摘要时出错

---

## 55. Words, Words, Words

**原文标题**: Words, Words, Words

**原文链接**: [https://aeon.co/essays/literature-fans-should-welcome-ai-as-a-fellow-wordsmith](https://aeon.co/essays/literature-fans-should-welcome-ai-as-a-fellow-wordsmith)

生成摘要时出错

---

## 56. Matt's Script Archive: The Scripts That Reshaped the Web

**原文标题**: Matt's Script Archive: The Scripts That Reshaped the Web

**原文链接**: [https://tedium.co/2026/06/22/matts-script-archive-retrospective/](https://tedium.co/2026/06/22/matts-script-archive-retrospective/)

生成摘要时出错

---

## 57. 45°C cooling design cuts data center water use to near zero

**原文标题**: 45°C cooling design cuts data center water use to near zero

**原文链接**: [https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/](https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/)

生成摘要时出错

---

## 58. Show HN: Nimic – Pure Python as a systems language with AOT compilation

**原文标题**: Show HN: Nimic – Pure Python as a systems language with AOT compilation

**原文链接**: [https://github.com/dima-quant/nimic](https://github.com/dima-quant/nimic)

生成摘要时出错

---

## 59. Dolphin Emulator Progress Release 2606

**原文标题**: Dolphin Emulator Progress Release 2606

**原文链接**: [https://dolphin-emu.org/blog/2026/06/25/dolphin-progress-report-release-2606/](https://dolphin-emu.org/blog/2026/06/25/dolphin-progress-report-release-2606/)

生成摘要时出错

---

## 60. Apple to Skip High-End M6 Mac Chips in Favor of AI-Focused M7 Line

**原文标题**: Apple to Skip High-End M6 Mac Chips in Favor of AI-Focused M7 Line

**原文链接**: [https://www.bloomberg.com/news/articles/2026-06-25/apple-to-skip-high-end-m6-mac-chips-to-launch-m7-pro-m7-max-m7-ultra-instead](https://www.bloomberg.com/news/articles/2026-06-25/apple-to-skip-high-end-m6-mac-chips-to-launch-m7-pro-m7-max-m7-ultra-instead)

生成摘要时出错

---

## 61. Show HN: Write SaaS apps where users control where their data is stored

**原文标题**: Show HN: Write SaaS apps where users control where their data is stored

**原文链接**: [https://github.com/wolfoo2931/linkedrecords/](https://github.com/wolfoo2931/linkedrecords/)

生成摘要时出错

---

## 62. We’re making Bunny DNS free

**原文标题**: We’re making Bunny DNS free

**原文链接**: [https://bunny.net/blog/were-making-bunny-dns-free/](https://bunny.net/blog/were-making-bunny-dns-free/)

生成摘要时出错

---

## 63. GLM-5.2 is a step change for open agents

**原文标题**: GLM-5.2 is a step change for open agents

**原文链接**: [https://www.interconnects.ai/p/glm-52-is-the-step-change-for-open](https://www.interconnects.ai/p/glm-52-is-the-step-change-for-open)

生成摘要时出错

---

## 64. As banks close accounts, experts point to immigration crackdown

**原文标题**: As banks close accounts, experts point to immigration crackdown

**原文链接**: [https://www.americanbanker.com/news/as-banks-close-accounts-experts-point-to-immigration-crackdown](https://www.americanbanker.com/news/as-banks-close-accounts-experts-point-to-immigration-crackdown)

生成摘要时出错

---

## 65. I can haz smoller NixOS ISOs?

**原文标题**: I can haz smoller NixOS ISOs?

**原文链接**: [https://natkr.com/2026-06-19-nixos-but-smol/](https://natkr.com/2026-06-19-nixos-but-smol/)

生成摘要时出错

---

## 66. Stealing Is a Skill

**原文标题**: Stealing Is a Skill

**原文链接**: [https://ben-mini.com/2026/stealing-is-a-skill](https://ben-mini.com/2026/stealing-is-a-skill)

生成摘要时出错

---

## 67. There are a few things that I look back on as my mistakes in the early days

**原文标题**: There are a few things that I look back on as my mistakes in the early days

**原文链接**: [https://twitter.com/ID_AA_Carmack/status/2069799283369345247](https://twitter.com/ID_AA_Carmack/status/2069799283369345247)

生成摘要时出错

---

## 68. Show HN: Monolisa v3 – a typeface for developers and creatives

**原文标题**: Show HN: Monolisa v3 – a typeface for developers and creatives

**原文链接**: [https://www.monolisa.dev/](https://www.monolisa.dev/)

生成摘要时出错

---

## 69. Crawling BitTorrent DHTs for Fun and Profit [pdf]

**原文标题**: Crawling BitTorrent DHTs for Fun and Profit [pdf]

**原文链接**: [https://www.usenix.org/legacy/event/woot10/tech/full_papers/Wolchok.pdf](https://www.usenix.org/legacy/event/woot10/tech/full_papers/Wolchok.pdf)

生成摘要时出错

---

## 70. The A.I.-Design Aesthetic That's Taking over the Internet

**原文标题**: The A.I.-Design Aesthetic That's Taking over the Internet

**原文链接**: [https://www.newyorker.com/culture/infinite-scroll/the-ai-design-aesthetic-thats-taking-over-the-internet](https://www.newyorker.com/culture/infinite-scroll/the-ai-design-aesthetic-thats-taking-over-the-internet)

生成摘要时出错

---

## 71. Countries are competing to see which can carry out mass surveillance the best

**原文标题**: Countries are competing to see which can carry out mass surveillance the best

**原文链接**: [https://mullvad.net/en/why-privacy-matters/state-mass-surveillance](https://mullvad.net/en/why-privacy-matters/state-mass-surveillance)

生成摘要时出错

---

## 72. Federal agents track down woman, demand she remove Instagram post about ICE

**原文标题**: Federal agents track down woman, demand she remove Instagram post about ICE

**原文链接**: [https://www.syracuse.com/news/2026/06/federal-agents-track-down-syracuse-woman-demand-she-remove-instagram-post-about-ice.html](https://www.syracuse.com/news/2026/06/federal-agents-track-down-syracuse-woman-demand-she-remove-instagram-post-about-ice.html)

生成摘要时出错

---

## 73. RubyLLM: A Ruby framework for all major AI providers

**原文标题**: RubyLLM: A Ruby framework for all major AI providers

**原文链接**: [https://rubyllm.com/](https://rubyllm.com/)

生成摘要时出错

---

## 74. Oracle Opens MySQL Governance

**原文标题**: Oracle Opens MySQL Governance

**原文链接**: [https://blogs.oracle.com/mysql/the-next-phase-of-mysql-community-engagement-accelerating-participation-and-collaboration](https://blogs.oracle.com/mysql/the-next-phase-of-mysql-community-engagement-accelerating-participation-and-collaboration)

生成摘要时出错

---

## 75. Why eval startups fail (2025)

**原文标题**: Why eval startups fail (2025)

**原文链接**: [https://thomasliao.com/eval-startups](https://thomasliao.com/eval-startups)

生成摘要时出错

---

## 76. Complete text of carbonised Herculaneum scroll unlocked for first time

**原文标题**: Complete text of carbonised Herculaneum scroll unlocked for first time

**原文链接**: [https://www.reuters.com/science/complete-text-carbonised-herculaneum-scroll-unlocked-first-time-2026-06-25/](https://www.reuters.com/science/complete-text-carbonised-herculaneum-scroll-unlocked-first-time-2026-06-25/)

生成摘要时出错

---

## 77. Ending respiratory infections

**原文标题**: Ending respiratory infections

**原文链接**: [https://blog.interceptfund.com/p/ending-respiratory-infections](https://blog.interceptfund.com/p/ending-respiratory-infections)

生成摘要时出错

---

## 78. Elastic lays off 7% of employees

**原文标题**: Elastic lays off 7% of employees

**原文链接**: [https://www.elastic.co/blog/ceo-ash-kulkarni-announcement-to-elastic-employees](https://www.elastic.co/blog/ceo-ash-kulkarni-announcement-to-elastic-employees)

生成摘要时出错

---

## 79. 15 sorting algorithms in 6 minutes (2013) [video]

**原文标题**: 15 sorting algorithms in 6 minutes (2013) [video]

**原文链接**: [https://www.youtube.com/watch?v=kPRA0W1kECg](https://www.youtube.com/watch?v=kPRA0W1kECg)

生成摘要时出错

---

## 80. "Fix" MacBook Neo Cursor Lag: Record 1 Pixel of the Screen Every 10 Seconds

**原文标题**: "Fix" MacBook Neo Cursor Lag: Record 1 Pixel of the Screen Every 10 Seconds

**原文链接**: [https://gist.github.com/retroplasma/ec21767d0a8380c7ea9c2fbee1c7d6bf](https://gist.github.com/retroplasma/ec21767d0a8380c7ea9c2fbee1c7d6bf)

生成摘要时出错

---

## 81. PR spam today looks like email spam in the early 2000s

**原文标题**: PR spam today looks like email spam in the early 2000s

**原文链接**: [https://www.greptile.com/blog/prs-on-openclaw](https://www.greptile.com/blog/prs-on-openclaw)

生成摘要时出错

---

## 82. Pull request limits are cutting down the noise

**原文标题**: Pull request limits are cutting down the noise

**原文链接**: [https://github.blog/open-source/maintainers/how-pull-request-limits-are-cutting-down-the-noise/](https://github.blog/open-source/maintainers/how-pull-request-limits-are-cutting-down-the-noise/)

生成摘要时出错

---

## 83. Zero-Downtime Deployments with Docker Compose – No Kubernetes Required

**原文标题**: Zero-Downtime Deployments with Docker Compose – No Kubernetes Required

**原文链接**: [https://statusdude.com/blog/zero-downtime-docker-compose](https://statusdude.com/blog/zero-downtime-docker-compose)

生成摘要时出错

---

## 84. Running Windows Games on a Hobby OS with Wine

**原文标题**: Running Windows Games on a Hobby OS with Wine

**原文链接**: [https://astral-os.org/posts/2026/04/03/wine-on-astral.html](https://astral-os.org/posts/2026/04/03/wine-on-astral.html)

生成摘要时出错

---

## 85. Show HN: Wordit – Change One Letter, Keep the Chain Going

**原文标题**: Show HN: Wordit – Change One Letter, Keep the Chain Going

**原文链接**: [https://victorribeiro.com/wordit/](https://victorribeiro.com/wordit/)

生成摘要时出错

---

## 86. The Xteink X4 E-Ink Reader

**原文标题**: The Xteink X4 E-Ink Reader

**原文链接**: [https://blog.omgmog.net/post/xteink-x4-e-ink-reader/](https://blog.omgmog.net/post/xteink-x4-e-ink-reader/)

生成摘要时出错

---

## 87. Exploiting vulnerabilities in Johnson and Johnson web apps

**原文标题**: Exploiting vulnerabilities in Johnson and Johnson web apps

**原文链接**: [https://eaton-works.com/2026/06/24/jnj-webapp-hacks/](https://eaton-works.com/2026/06/24/jnj-webapp-hacks/)

生成摘要时出错

---

## 88. Minimus container images are now free

**原文标题**: Minimus container images are now free

**原文链接**: [https://images.minimus.io/](https://images.minimus.io/)

生成摘要时出错

---

## 89. Genuinely, my all-time favourite image: Mamenchisaurus hochuanensis

**原文标题**: Genuinely, my all-time favourite image: Mamenchisaurus hochuanensis

**原文链接**: [https://svpow.com/2026/06/04/genuinely-my-all-time-favourite-image-mamenchisaurus-hochuanensis/](https://svpow.com/2026/06/04/genuinely-my-all-time-favourite-image-mamenchisaurus-hochuanensis/)

生成摘要时出错

---

## 90. Meta forced engineers into AI training. Now it's giving some a way out

**原文标题**: Meta forced engineers into AI training. Now it's giving some a way out

**原文链接**: [https://www.businessinsider.com/meta-lets-engineers-leave-ai-training-unit-after-mass-reassignment-2026-6](https://www.businessinsider.com/meta-lets-engineers-leave-ai-training-unit-after-mass-reassignment-2026-6)

生成摘要时出错

---

## 91. Too many R packages: CRAN is inundated with submissions

**原文标题**: Too many R packages: CRAN is inundated with submissions

**原文链接**: [https://rworks.dev/posts/too-many-R-packages/](https://rworks.dev/posts/too-many-R-packages/)

生成摘要时出错

---

## 92. Computer use in Gemini 3.5 Flash

**原文标题**: Computer use in Gemini 3.5 Flash

**原文链接**: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/)

生成摘要时出错

---

## 93. Show HN: Brain Frog – Can you be random enough for 11 lines of JavaScript?

**原文标题**: Show HN: Brain Frog – Can you be random enough for 11 lines of JavaScript?

**原文链接**: [https://brainfrog.lol](https://brainfrog.lol)

生成摘要时出错

---

## 94. How the Fifth Lateran Council unlocked financial theory

**原文标题**: How the Fifth Lateran Council unlocked financial theory

**原文链接**: [https://sebastiangarren.com/2026/06/17/lending-is-meritorious-and-should-be-praised-how-the-fifth-lateran-council-unlocked-financial-theory/](https://sebastiangarren.com/2026/06/17/lending-is-meritorious-and-should-be-praised-how-the-fifth-lateran-council-unlocked-financial-theory/)

生成摘要时出错

---

## 95. Qwen-AgentWorld: Language World Models for General Agents

**原文标题**: Qwen-AgentWorld: Language World Models for General Agents

**原文链接**: [https://arxiv.org/abs/2606.24597](https://arxiv.org/abs/2606.24597)

生成摘要时出错

---

## 96. Pondering routing more of my traffic via nodes outside the UK

**原文标题**: Pondering routing more of my traffic via nodes outside the UK

**原文链接**: [https://neilzone.co.uk/2026/06/pondering-routing-more-of-my-traffic-via-nodes-outside-the-uk-because-of-the-direction-of-uk-online-safety-policy/](https://neilzone.co.uk/2026/06/pondering-routing-more-of-my-traffic-via-nodes-outside-the-uk-because-of-the-direction-of-uk-online-safety-policy/)

生成摘要时出错

---

## 97. I rewrote PostHog's SQL parser, 70x faster, while barely looking at the code

**原文标题**: I rewrote PostHog's SQL parser, 70x faster, while barely looking at the code

**原文链接**: [https://posthog.com/blog/sql-parser](https://posthog.com/blog/sql-parser)

生成摘要时出错

---

## 98. A Practical Guide to SSH Tunnels: Local and Remote Port Forwarding

**原文标题**: A Practical Guide to SSH Tunnels: Local and Remote Port Forwarding

**原文链接**: [https://labs.iximiuz.com/tutorials/ssh-tunnels](https://labs.iximiuz.com/tutorials/ssh-tunnels)

生成摘要时出错

---

## 99. Show HN: LookAway, a Mac break reminder that knows when not to interrupt

**原文标题**: Show HN: LookAway, a Mac break reminder that knows when not to interrupt

**原文链接**: [https://lookaway.com](https://lookaway.com)

生成摘要时出错

---

## 100. Millimeter wave technology drills 100 meters into granite

**原文标题**: Millimeter wave technology drills 100 meters into granite

**原文链接**: [https://www.thinkgeoenergy.com/quaise-energy-achieves-100-meters-of-drilling-using-millimeter-wave-technology/](https://www.thinkgeoenergy.com/quaise-energy-achieves-100-meters-of-drilling-using-millimeter-wave-technology/)

生成摘要时出错

---

