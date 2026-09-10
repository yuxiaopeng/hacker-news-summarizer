# Hacker News 热门文章摘要 (2026-09-10)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Rust 是微软的一级语言

**原文标题**: Rust is tier-1 language at Microsoft

**原文链接**: [https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/)

微软已正式将 Rust 提升为内部开发的“一级”（Tier-1）语言，使其与 C++、C# 和 TypeScript 并列。这一定位为微软团队提供了通往生产环境的“铺就之路”（paved path），包括安全的工具链、深度的平台集成，以及完全符合公司安全开发生命周期（SDL）要求的能力。

此次转型的基石是引入了 **rustc_codegen_utc**，这是一个将 Rust 编译器（`rustc`）连接到 MSVC (UTC) 后端的新编译器后端。这使得 Rust 在 Windows 上能够超越其传统的基于 LLVM 的根基，直接参与到原生 Windows 工程生态系统中。这种统一后端的主要优势包括：

*   **无缝互操作性：** Rust 与 C++ 之间的高保真 ABI 兼容性和跨语言内联，这对于混合项目至关重要。
*   **平台特性：** 可调用 Windows 特有的功能，如热补丁（Hotpatching）、二进制加固以及样本配置文件引导优化（SPGO）。
*   **统一工具链：** 共享现有的 MSVC 基础设施，用于调试、崩溃转储分析和性能剖析。

微软的策略旨在通过为两种语言利用共同的基础来降低维护成本。这确保了 Windows 平台或 MSVC 编译器的任何创新都能自动惠及 Rust 和 C++ 开发者。截至 2026 年底，`rustc_codegen_utc` 已达到生产就绪状态，自 Rust 1.90 起实现自托管，并已集成到 100 多个微软内部仓库中。这一举措代表了对微软软件栈进行“氧化”（oxidizing）的重大长期承诺——从固件和内核到云微服务——同时保持其现有 C++ 代码库的性能和稳定性。

---

## 2. 我有一个理论：软件能把人逼疯。

**原文标题**: I have a theory that software drives people insane

**原文链接**: [https://graybeard.ing/software-drives-people-insane/](https://graybeard.ing/software-drives-people-insane/)

在《软件让人发疯》一文中，作者指出，软件开发独特的工作环境——极高的速度、巨大的财务投入以及无限的可变性——导致了人们心理上分寸感的丧失。与物理建筑不同，软件缺乏自然阻力；由于改动在技术上可行且没有“可见”成本（如材料损耗），领导层往往认为这些改动是免费的。这导致了一个恶性循环：“可以做”变成了“必须做”，每一个微小的功能都被赋予了生死存亡般的紧迫感。

文章强调了导致这种“疯狂”的几个核心驱动因素：
*   **隐形成本：** 移动房屋的一堵墙有明显的代价，但软件变更的成本却隐藏在上下文切换、架构侵蚀和开发势头的丧失中。
*   **没有“完工”之说：** 与完工的橱柜不同，软件总能被优化、扩展或重构，从而陷入永久的不完整状态。
*   **将复杂性视为地位象征：** 复杂的系统能提供心理回报并营造重要感，导致团队将简单的工具（往往只是“高级电子表格”）过度设计成庞大的分布式平台。
*   **组织异变：** 最终，公司开始像对待软件一样对待自身的组织结构：使其处于永久可变的状态，总觉得只要再经历一次“重构”就能达到完美。

作者总结道，最被低估的工程技能是“不去动它”。为了保持理智，行业必须拥抱“分寸感”——即意识到并非每个想法都应该出现在路线图中，耐心往往比持续的瞎忙更有价值。与其追逐“统治世界”或无限规模，我们应当记住，软件本质上是让生活更轻松的工具，而不是用来进行不必要折腾的意识形态战场。

---

## 3. Cognition 发布全新 SWE-2 模型，对标 Fable 5.1 和 GPT-Astra

**原文标题**: Cognition launches new SWE-2 model, Rivaling Fable 5.1 and GPT-Astra

**原文链接**: [https://cognition.com/blog/swe-2](https://cognition.com/blog/swe-2)

Cognition 宣布推出其迄今为止最先进的代码模型 **SWE-2**，旨在最大化能力与成本的“帕累托前沿”。基于拥有 2.8 万亿参数的 **Kimi K3** 进行后期训练，SWE-2 在 FrontierCode 1.1 Main 基准测试中取得了 50.0% 的评分。这一性能可与 Fable 5.1 和 GPT-5.6 Sol 等行业领先模型相媲美，同时其运行成本比 Fable 低 64%，仅为 GPT-6 Astra 的四分之一。

**核心技术创新：**
*   **多万亿参数强化学习 (RL)：** Cognition 首次将强化学习扩展到了多万亿参数规模。他们引入了一种 RL 算法，通过应用根据模型性能曲线调整的线性成本惩罚，在单次运行中即可完成所有推理力度（中、高、最高）的训练。
*   **训练稳定性：** 团队实施了“长度加权奖励基准”，以减少梯度方差并稳定 RL 过程，在确保模型保持高性能的同时，降低推理与训练之间的差异。
*   **基础设施效率：** 为了最大化吞吐量，SWE-2 采用了带有在线草图模型训练的 DSpark 推测性解码以及 NVFP4/FP8 量化技术。这些优化使得 2.8T 规模的模型尽管体量巨大，仍能保持高效运行。

**行为与性能提升：**
SWE-2 显著提升了工程判断力。与前代模型 SWE-1.7 在处理简单任务时偶尔会“过度思考”不同，SWE-2 能更快速地识别相关的代码库区域。在 FrontierCode 基准测试中，其解决问题的对话轮数比 SWE-1.7 减少了 58%，平均成本降低了 81%。它还展示了卓越的测试覆盖率、在受阻时更强的应变能力，以及一种“验证纪律”——即重新推导结论而非盲目信任表层证据。

SWE-2 即日起在 **Devin** 桌面端和 CLI 中上线，Web 端和 Fusion 平台也正在陆续推出。

---

## 4. 关于研究人员能否信任 OpenAI 处理未发表数学研究的更多质疑

**原文标题**: More questions about whether researchers can trust OpenAI with unpublished math

**原文链接**: [https://mathstodon.xyz/@andreasthom/117240535270608201](https://mathstodon.xyz/@andreasthom/117240535270608201)

本文及 Mathstodon 上的相关讨论凸显了数学研究界对于在未发表的工作中使用 OpenAI 高级模型（特别是 o1 系列）日益增长的焦虑。

这场由 Tristan Buckmaster 发起并经 Andreas Thom 传播的讨论集中在几个核心关切点上：

*   **数据隐私与训练：** 研究人员担心，将技术性的、未发表的证明或原创问题输入 OpenAI 模型，可能会导致这些数据被摄取用于训练。这增加了 AI 随后向其他用户“泄露”或重新生成这些专有想法的风险。
*   **“o1”事件：** Buckmaster 分享了一次经历，他用一篇未发表论文中的问题测试了 o1 模型。该模型极高的表现水平及其处理复杂、新颖推理的能力引发了人们的担忧，即私人研究与 AI 训练集之间的界限已变得极其模糊。
*   **知识产权风险：** 存在关于“数学抄袭”的重大担忧。如果研究人员使用 AI 协助完成证明，社区尚不清楚由此产生的见解归谁“所有”，以及研究人员是否在无意中将其发现置于公共领域或 OpenAI 之手。
*   **对服务条款的信任：** 尽管 OpenAI 提供了一定的数据隐私设置，但数学家们正在讨论这些保护措施对于高风险、原创性的突破是否足够。

**结论：**
目前的共识反映了一个困境：虽然 AI 工具在证明检查和头脑风暴方面提供了强大的辅助，但潜在的代价——即失去对原创数学发现的控制——正促使许多研究人员建议，不要在敏感的、未发表的工作中使用这些模型。

---

## 5. NASA原为火星设计的色彩技术，现正揭开地球岩画的面纱。

**原文标题**: NASA Color Trick Was Meant for Mars. Now It's Unveiling Rock Art on Earth

**原文链接**: [https://gizmodo.com/this-nasa-color-trick-was-meant-for-mars-now-its-unveiling-rock-art-on-earth-2000809844](https://gizmodo.com/this-nasa-color-trick-was-meant-for-mars-now-its-unveiling-rock-art-on-earth-2000809844)

一项最初为帮助美国国家航空航天局（NASA）探索火星表面而设计的软件技术，如今正彻底改变考古学家研究地球古代岩画的方式。

这款名为 **DStretch**（去相关拉伸）的工具由研究员乔恩·哈曼（Jon Harman）开发。它利用一种算法来增强数字图像中肉眼几乎不可见的细微颜色差异。NASA 最初在火星探测器任务中应用了这种“色彩技巧”，使科学家能够在原本色彩单调的火星景观中区分不同的矿物成分和地质特征。

在地球上，这项技术已成为记录褪色的彩色岩画和岩刻的变革性工具。几千年来，许多古代岩画因风化、矿物结壳或自然褪色而变得模糊不清。通过对这些遗址的照片应用 DStretch 技术，研究人员可以“拉伸”光谱，从而揭示此前被隐藏的鲜艳红色、黄色和黑色。

该方法的主要优势在于它完全是非侵入性的。考古学家无需接触或可能损坏脆弱的文化遗产遗址，就能发现复杂的图案和历史叙事。从欧洲的洞穴到美国西南部偏远的峡谷，DStretch 正在帮助专家识别失传的艺术作品，并更深入地了解创造这些作品的文化。

通过重新利用这项旨在探索太空前沿的技术，科学家们获得了一个审视人类历史的强大新视角，这证明了为探索未来而设计的工具在揭示遥远的过去时同样卓有成效。

---

## 6. Shopify moves back to Native from React Native

**原文标题**: Shopify moves back to Native from React Native

**原文链接**: [https://shopify.engineering/back-to-native](https://shopify.engineering/back-to-native)

Shopify has announced a strategic shift from React Native back to native development (Swift for iOS and Kotlin for Android), citing a fundamental change in the economics of mobile development driven by AI coding agents. 

While Shopify’s 2020 move to React Native was successful in reducing the cost of maintaining feature parity, the company argues that LLMs have invalidated the core assumption that building for two platforms requires twice the work. Modern AI agents can now handle significant portions of implementation, translation, and testing, making the benefits of native performance and first-party tooling more attractive than the convenience of a shared codebase.

**Key highlights of the transition include:**

*   **AI-Driven Migration:** Shopify is opting for a "greenfield" rewrite of its major apps. Using a proprietary system called **Helix**, they ensure code quality through an iterative loop of checkpoints, automated tests, and human reviews. This process allowed them to rebuild the **Shop app** from scratch in just 12 weeks.
*   **Agent-Addressable Architecture:** To accelerate feedback loops, Shopify is decoupling business logic from UI. This allows AI agents to test and iterate via a CLI in milliseconds rather than relying on slow mobile simulators.
*   **Sunsetting Open-Source Libraries:** Shopify will wind down its support for popular React Native libraries. **FlashList** and **React Native Skia** will be transitioned to new stewards or forks, while **Restyle** will be archived by the end of 2026.

The flagship **Shopify app** is currently being migrated, with other apps to follow. Ultimately, Shopify views this move as a way to leverage the superior capabilities of native platforms while utilizing AI to maintain high product velocity.

---

## 7. Neki

**原文标题**: Neki

**原文链接**: [https://planetscale.com/blog/introducing-neki](https://planetscale.com/blog/introducing-neki)

生成摘要时出错

---

## 8. Forgejo <=16.0.3 Critical RCE

**原文标题**: Forgejo <=16.0.3 Critical RCE

**原文链接**: [https://codeberg.org/forgejo/forgejo/src/branch/forgejo/release-notes-published/16.0.4.md](https://codeberg.org/forgejo/forgejo/src/branch/forgejo/release-notes-published/16.0.4.md)

生成摘要时出错

---

## 9. Douglas Hofstadter: Analogy as the Core of Cognition [video]

**原文标题**: Douglas Hofstadter: Analogy as the Core of Cognition [video]

**原文链接**: [https://www.youtube.com/watch?v=n8m7lFQ3njk](https://www.youtube.com/watch?v=n8m7lFQ3njk)

生成摘要时出错

---

## 10. Music Theory for the 21st-Century Classroom

**原文标题**: Music Theory for the 21st-Century Classroom

**原文链接**: [https://musictheory.pugetsound.edu/mt21c/MusicTheory.html](https://musictheory.pugetsound.edu/mt21c/MusicTheory.html)

生成摘要时出错

---

## 11. JEP 544: Ahead-of-Time Code Compilation

**原文标题**: JEP 544: Ahead-of-Time Code Compilation

**原文链接**: [https://openjdk.org/jeps/544](https://openjdk.org/jeps/544)

生成摘要时出错

---

## 12. Cognition's SWE-2 achieves 92.8 on Terminal-Bench 2.1

**原文标题**: Cognition's SWE-2 achieves 92.8 on Terminal-Bench 2.1

**原文链接**: [https://tokenstead.ai/models/swe-2](https://tokenstead.ai/models/swe-2)

生成摘要时出错

---

## 13. >10x More Efficient Pretraining

**原文标题**: >10x More Efficient Pretraining

**原文链接**: [https://magic.dev/blog/pretraining#](https://magic.dev/blog/pretraining#)

生成摘要时出错

---

## 14. DeepSeek v4.1 Flash

**原文标题**: DeepSeek v4.1 Flash

**原文链接**: [https://twitter.com/deepseek_ai/status/2097930608790167907](https://twitter.com/deepseek_ai/status/2097930608790167907)

生成摘要时出错

---

## 15. Silicon Valley Is Transforming the Military-Industrial Complex

**原文标题**: Silicon Valley Is Transforming the Military-Industrial Complex

**原文链接**: [https://costsofwar.watson.brown.edu/paper/how-big-tech-and-silicon-valley-are-transforming-military-industrial-complex](https://costsofwar.watson.brown.edu/paper/how-big-tech-and-silicon-valley-are-transforming-military-industrial-complex)

生成摘要时出错

---

## 16. Hitachi launches CO2 heat pump water heaters with solar-friendly tariff controls

**原文标题**: Hitachi launches CO2 heat pump water heaters with solar-friendly tariff controls

**原文链接**: [https://www.pv-magazine.com/2026/09/07/hitachi-launches-co2-heat-pump-water-heaters-with-solar-friendly-tariff-controls/](https://www.pv-magazine.com/2026/09/07/hitachi-launches-co2-heat-pump-water-heaters-with-solar-friendly-tariff-controls/)

生成摘要时出错

---

## 17. Neki is sharded Postgres by PlanetScale

**原文标题**: Neki is sharded Postgres by PlanetScale

**原文链接**: [https://neki.dev/](https://neki.dev/)

生成摘要时出错

---

## 18. Schemy Lisp En DOS

**原文标题**: Schemy Lisp En DOS

**原文链接**: [https://sled.neocities.org/](https://sled.neocities.org/)

生成摘要时出错

---

## 19. Genuine Creativity Is Your New Moat (2026)

**原文标题**: Genuine Creativity Is Your New Moat (2026)

**原文链接**: [https://www.inventbuild.studio/blog/genuine-creativity-is-your-new-moat](https://www.inventbuild.studio/blog/genuine-creativity-is-your-new-moat)

生成摘要时出错

---

## 20. What algorithm did Windows XP use to choose your initial user picture?

**原文标题**: What algorithm did Windows XP use to choose your initial user picture?

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20260909-00/?p=112683](https://devblogs.microsoft.com/oldnewthing/20260909-00/?p=112683)

生成摘要时出错

---

## 21. List of references on Sony websites to players "owning" their digital games

**原文标题**: List of references on Sony websites to players "owning" their digital games

**原文链接**: [https://consumerrights.wiki/w/Sony_PlayStation_digital_game_ownership_lawsuit](https://consumerrights.wiki/w/Sony_PlayStation_digital_game_ownership_lawsuit)

生成摘要时出错

---

## 22. Macbeth and His Problems

**原文标题**: Macbeth and His Problems

**原文链接**: [https://porticoquarterly.com/essay/macbeth-and-his-problems/](https://porticoquarterly.com/essay/macbeth-and-his-problems/)

生成摘要时出错

---

## 23. Python sets and dictionaries can have quadratic-time performance

**原文标题**: Python sets and dictionaries can have quadratic-time performance

**原文链接**: [https://lemire.me/blog/2026/09/03/python-sets-and-dictionaries-can-have-quadratic-time-performance/](https://lemire.me/blog/2026/09/03/python-sets-and-dictionaries-can-have-quadratic-time-performance/)

生成摘要时出错

---

## 24. iPhone Duo

**原文标题**: iPhone Duo

**原文链接**: [https://www.apple.com/iphone-duo/](https://www.apple.com/iphone-duo/)

生成摘要时出错

---

## 25. Stockfish 19

**原文标题**: Stockfish 19

**原文链接**: [https://stockfishchess.org/blog/2026/stockfish-19/](https://stockfishchess.org/blog/2026/stockfish-19/)

生成摘要时出错

---

## 26. Casablanca: How an unproduced play marched into movie history

**原文标题**: Casablanca: How an unproduced play marched into movie history

**原文链接**: [https://www.thecollector.com/casablanca-unproduced-play-movie-history/](https://www.thecollector.com/casablanca-unproduced-play-movie-history/)

生成摘要时出错

---

## 27. To write non-fiction, draw the trunk, then the rest of the tree

**原文标题**: To write non-fiction, draw the trunk, then the rest of the tree

**原文链接**: [https://devz.cl/posts/how-to-write/](https://devz.cl/posts/how-to-write/)

生成摘要时出错

---

## 28. Show HN: DOOM in the kernel, or fibers in eBPF

**原文标题**: Show HN: DOOM in the kernel, or fibers in eBPF

**原文链接**: [https://ayles.github.io/doom-in-kernel/](https://ayles.github.io/doom-in-kernel/)

生成摘要时出错

---

## 29. Show HN: MultiMatte, a Promptable Image Background Removal Model

**原文标题**: Show HN: MultiMatte, a Promptable Image Background Removal Model

**原文链接**: [https://usefeyn.com/blog/multimatte/](https://usefeyn.com/blog/multimatte/)

生成摘要时出错

---

## 30. AI 2027 (2025)

**原文标题**: AI 2027 (2025)

**原文链接**: [https://ai-2027.com](https://ai-2027.com)

生成摘要时出错

---

## 31. Show HN: Syq – copy files between machines fast (better than rsync)

**原文标题**: Show HN: Syq – copy files between machines fast (better than rsync)

**原文链接**: [https://greaber.github.io/syq/](https://greaber.github.io/syq/)

生成摘要时出错

---

## 32. Detecting and countering misuse of AI: September 2026

**原文标题**: Detecting and countering misuse of AI: September 2026

**原文链接**: [https://www.anthropic.com/threat-intelligence-report-september-2026](https://www.anthropic.com/threat-intelligence-report-september-2026)

生成摘要时出错

---

## 33. The Four-Color Theorem Gets a Rare New Proof

**原文标题**: The Four-Color Theorem Gets a Rare New Proof

**原文链接**: [https://www.quantamagazine.org/the-four-color-theorem-gets-a-rare-new-proof-20260910/](https://www.quantamagazine.org/the-four-color-theorem-gets-a-rare-new-proof-20260910/)

生成摘要时出错

---

## 34. The first drink-driving conviction may have happened in London

**原文标题**: The first drink-driving conviction may have happened in London

**原文链接**: [https://www.ianvisits.co.uk/articles/the-worlds-first-drink-driving-conviction-may-have-happened-in-london-92107/](https://www.ianvisits.co.uk/articles/the-worlds-first-drink-driving-conviction-may-have-happened-in-london-92107/)

生成摘要时出错

---

## 35. Show HN: Filament – Fast data movement engine in Go

**原文标题**: Show HN: Filament – Fast data movement engine in Go

**原文链接**: [https://github.com/galaxy-io/filament](https://github.com/galaxy-io/filament)

生成摘要时出错

---

## 36. AI Is Breaking This Thing We Call Trust

**原文标题**: AI Is Breaking This Thing We Call Trust

**原文链接**: [https://terriblesoftware.org/2026/09/10/ai-is-breaking-this-thing-we-call-trust/](https://terriblesoftware.org/2026/09/10/ai-is-breaking-this-thing-we-call-trust/)

生成摘要时出错

---

## 37. Show HN: Art – draw one stroke, let symmetry complete it

**原文标题**: Show HN: Art – draw one stroke, let symmetry complete it

**原文链接**: [https://mrdee.in/mandala/](https://mrdee.in/mandala/)

生成摘要时出错

---

## 38. Larger Pacific striped octopus

**原文标题**: Larger Pacific striped octopus

**原文链接**: [https://en.wikipedia.org/wiki/Larger_Pacific_striped_octopus](https://en.wikipedia.org/wiki/Larger_Pacific_striped_octopus)

生成摘要时出错

---

## 39. Liesegang Rings

**原文标题**: Liesegang Rings

**原文链接**: [https://chillphysicsenjoyer.substack.com/p/liesegang-rings](https://chillphysicsenjoyer.substack.com/p/liesegang-rings)

生成摘要时出错

---

## 40. Serverless DTLS

**原文标题**: Serverless DTLS

**原文链接**: [https://proxylity.com/docs/listeners/dtls.html](https://proxylity.com/docs/listeners/dtls.html)

生成摘要时出错

---

## 41. Don't Get in a Crash in a Cybercab

**原文标题**: Don't Get in a Crash in a Cybercab

**原文链接**: [https://schwarztech.net/snippets/dont-get-in-a-crash-in-a-cybercab](https://schwarztech.net/snippets/dont-get-in-a-crash-in-a-cybercab)

生成摘要时出错

---

## 42. Who Dung It? (Turdle.fun)

**原文标题**: Who Dung It? (Turdle.fun)

**原文链接**: [https://turdle.fun/](https://turdle.fun/)

生成摘要时出错

---

## 43. Study: A burst of "pink noise" may lead to more restorative sleep

**原文标题**: Study: A burst of "pink noise" may lead to more restorative sleep

**原文链接**: [https://news.mit.edu/2026/pink-noise-burst-may-mean-more-restorative-sleep-0909](https://news.mit.edu/2026/pink-noise-burst-may-mean-more-restorative-sleep-0909)

生成摘要时出错

---

## 44. X86S with IGZO BEOL EDRAM

**原文标题**: X86S with IGZO BEOL EDRAM

**原文链接**: [https://inavoyage.blogspot.com/2026/09/x86s-w-igzo-beol-edram.html](https://inavoyage.blogspot.com/2026/09/x86s-w-igzo-beol-edram.html)

生成摘要时出错

---

## 45. Show HN: What if the speed of light was 5 km/h?

**原文标题**: Show HN: What if the speed of light was 5 km/h?

**原文链接**: [https://rivendell.dmitrybrant.com/relativity/](https://rivendell.dmitrybrant.com/relativity/)

生成摘要时出错

---

## 46. CERN Renounces RHEL in Favor of Debian

**原文标题**: CERN Renounces RHEL in Favor of Debian

**原文链接**: [https://www.infoq.com/news/2026/09/cern-debian-infra/](https://www.infoq.com/news/2026/09/cern-debian-infra/)

生成摘要时出错

---

## 47. Galaxy Z Fold 8 get the same folding animation as iPhone Duo

**原文标题**: Galaxy Z Fold 8 get the same folding animation as iPhone Duo

**原文链接**: [https://forgeeks.net/iphone-duo-galaxy-fold-animation/](https://forgeeks.net/iphone-duo-galaxy-fold-animation/)

生成摘要时出错

---

## 48. Roame (YC S23) Is Hiring Viral Content Editor

**原文标题**: Roame (YC S23) Is Hiring Viral Content Editor

**原文链接**: [https://www.ycombinator.com/companies/roame/jobs/KuVVqSh-content-systems-builder-editor](https://www.ycombinator.com/companies/roame/jobs/KuVVqSh-content-systems-builder-editor)

生成摘要时出错

---

## 49. Samsung Debuts zHBM Prototype, Stacking Memory Directly on AI Accelerators

**原文标题**: Samsung Debuts zHBM Prototype, Stacking Memory Directly on AI Accelerators

**原文链接**: [https://www.thelec.net/news/articleView.html?idxno=12835](https://www.thelec.net/news/articleView.html?idxno=12835)

生成摘要时出错

---

## 50. Automattic's board forces CEO Matt Mullenweg into leave of absence

**原文标题**: Automattic's board forces CEO Matt Mullenweg into leave of absence

**原文链接**: [https://techcrunch.com/2026/09/09/automattics-board-forces-ceo-matt-mullenweg-into-leave-of-absence/](https://techcrunch.com/2026/09/09/automattics-board-forces-ceo-matt-mullenweg-into-leave-of-absence/)

生成摘要时出错

---

## 51. Don't Let Anyone Take Away Your Big Box of Cables

**原文标题**: Don't Let Anyone Take Away Your Big Box of Cables

**原文链接**: [https://blog.jim-nielsen.com/2026/hands-off-my-cables/](https://blog.jim-nielsen.com/2026/hands-off-my-cables/)

生成摘要时出错

---

## 52. A Crash Course in Predicate Logic

**原文标题**: A Crash Course in Predicate Logic

**原文链接**: [https://www.hillelwayne.com/post/predicate-logic/](https://www.hillelwayne.com/post/predicate-logic/)

生成摘要时出错

---

## 53. Discrete Dipole Approximation Code Ddscat 7.2 (2012)

**原文标题**: Discrete Dipole Approximation Code Ddscat 7.2 (2012)

**原文链接**: [https://arxiv.org/abs/1202.3424](https://arxiv.org/abs/1202.3424)

生成摘要时出错

---

## 54. Hear Me Out: If We Find Life Out There Maybe We Should Kill It

**原文标题**: Hear Me Out: If We Find Life Out There Maybe We Should Kill It

**原文链接**: [https://joecmarshall.com/posts/hear-me-out-if-we-find-life-out-there-maybe-we-should-kill-it/](https://joecmarshall.com/posts/hear-me-out-if-we-find-life-out-there-maybe-we-should-kill-it/)

生成摘要时出错

---

## 55. Shopify acquires Tailwind

**原文标题**: Shopify acquires Tailwind

**原文链接**: [https://tailwindcss.com/blog/tailwind-is-joining-shopify](https://tailwindcss.com/blog/tailwind-is-joining-shopify)

生成摘要时出错

---

## 56. Sub-second Postgres replication to ClickHouse from physical WAL

**原文标题**: Sub-second Postgres replication to ClickHouse from physical WAL

**原文链接**: [https://clickhouse.com/blog/introducing-walshadow](https://clickhouse.com/blog/introducing-walshadow)

生成摘要时出错

---

## 57. Aardman (Wallace and Gromit) Is Selling Its Original Movie Puppets

**原文标题**: Aardman (Wallace and Gromit) Is Selling Its Original Movie Puppets

**原文链接**: [https://gizmodo.com/aardman-is-selling-its-original-movie-puppets-this-month-2000807968](https://gizmodo.com/aardman-is-selling-its-original-movie-puppets-this-month-2000807968)

生成摘要时出错

---

## 58. Kagi Translate Is Back

**原文标题**: Kagi Translate Is Back

**原文链接**: [https://blog.kagi.com/translate-is-back](https://blog.kagi.com/translate-is-back)

生成摘要时出错

---

## 59. Native Python and TypeScript Drivers for ArcadeDB, from OpenAPI and Protobuf

**原文标题**: Native Python and TypeScript Drivers for ArcadeDB, from OpenAPI and Protobuf

**原文链接**: [https://arcadedb.com/blog/arcadedb-native-drivers-python-typescript/](https://arcadedb.com/blog/arcadedb-native-drivers-python-typescript/)

生成摘要时出错

---

## 60. I'm a Proud Luddite. That's Why I Use Linux

**原文标题**: I'm a Proud Luddite. That's Why I Use Linux

**原文链接**: [https://thelibre.news/im-a-proud-luddite-thats-why-i-use-linux/](https://thelibre.news/im-a-proud-luddite-thats-why-i-use-linux/)

生成摘要时出错

---

## 61. Astra for Coding: Why Are We Doing This Again?

**原文标题**: Astra for Coding: Why Are We Doing This Again?

**原文链接**: [https://lucumr.pocoo.org/2026/9/7/astra-why/](https://lucumr.pocoo.org/2026/9/7/astra-why/)

生成摘要时出错

---

## 62. Show HN: We served 5k dynamic websites from a 2-vCPU, 4 GB VPS

**原文标题**: Show HN: We served 5k dynamic websites from a 2-vCPU, 4 GB VPS

**原文链接**: [https://github.com/Kooboo/Kooboo/blob/main/Docs/5000-sites-benchmark.md](https://github.com/Kooboo/Kooboo/blob/main/Docs/5000-sites-benchmark.md)

生成摘要时出错

---

## 63. Visa和Mastercard是做什么的？卡组织简介

**原文标题**: What do Visa and Mastercard do? An intro to card networks

**原文链接**: [https://tautology.town/2026/06/01/card-networks.html](https://tautology.town/2026/06/01/card-networks.html)

生成摘要时出错

---

## 64. 闹翻全村：Bevy 的 6 岁生日

**原文标题**: It Breaks a Village: Bevy's 6th Birthday

**原文链接**: [https://blog.fallible.net/it-breaks-a-village/](https://blog.fallible.net/it-breaks-a-village/)

生成摘要时出错

---

## 65. The UN challenges five centuries of cartography

**原文标题**: The UN challenges five centuries of cartography

**原文链接**: [https://www.not-ship.com/united-nations-map/](https://www.not-ship.com/united-nations-map/)

生成摘要时出错

---

## 66. Show HN: Compute polynomials twice as fast

**原文标题**: Show HN: Compute polynomials twice as fast

**原文链接**: [https://thomasahle.com/fast-polynomials/](https://thomasahle.com/fast-polynomials/)

生成摘要时出错

---

## 67. Training a 3.8B LLM to 0.384 CORE for $998

**原文标题**: Training a 3.8B LLM to 0.384 CORE for $998

**原文链接**: [https://hugovergnes.github.io/little-lm-3-8b/](https://hugovergnes.github.io/little-lm-3-8b/)

生成摘要时出错

---

## 68. Apple Watch Series 12

**原文标题**: Apple Watch Series 12

**原文链接**: [https://www.apple.com/newsroom/2026/09/introducing-apple-watch-series-12-with-the-all-new-health-sensing-system/](https://www.apple.com/newsroom/2026/09/introducing-apple-watch-series-12-with-the-all-new-health-sensing-system/)

生成摘要时出错

---

## 69. Postgres Calculations and the Ambiguity of Null

**原文标题**: Postgres Calculations and the Ambiguity of Null

**原文链接**: [https://www.crunchydata.com/blog/postgres-calculations-and-the-ambiguity-of-null](https://www.crunchydata.com/blog/postgres-calculations-and-the-ambiguity-of-null)

生成摘要时出错

---

## 70. GNU Radio in the browser

**原文标题**: GNU Radio in the browser

**原文链接**: [https://gnuradioworld.com/](https://gnuradioworld.com/)

生成摘要时出错

---

## 71. Factoring RSA 260

**原文标题**: Factoring RSA 260

**原文链接**: [https://cognition.com/blog/factoring-rsa-260](https://cognition.com/blog/factoring-rsa-260)

生成摘要时出错

---

## 72. Growing proof that autonomous cars save lives

**原文标题**: Growing proof that autonomous cars save lives

**原文链接**: [https://spectrum.ieee.org/are-self-driving-cars-safe](https://spectrum.ieee.org/are-self-driving-cars-safe)

生成摘要时出错

---

## 73. We Are Still Living in the Broken World Sept. 11 Created

**原文标题**: We Are Still Living in the Broken World Sept. 11 Created

**原文链接**: [https://www.bloomberg.com/opinion/articles/2026-09-10/sept-11-still-shapes-us-constitutional-rights-and-presidential-power](https://www.bloomberg.com/opinion/articles/2026-09-10/sept-11-still-shapes-us-constitutional-rights-and-presidential-power)

生成摘要时出错

---

## 74. Meta tried to shrink engineering teams around AI

**原文标题**: Meta tried to shrink engineering teams around AI

**原文链接**: [https://leaddev.com/ai/meta-tried-to-shrink-engineering-teams-around-ai](https://leaddev.com/ai/meta-tried-to-shrink-engineering-teams-around-ai)

生成摘要时出错

---

## 75. Show HN: Dbmask – Discover, mask, and verify sensitive data in SQL databases

**原文标题**: Show HN: Dbmask – Discover, mask, and verify sensitive data in SQL databases

**原文链接**: [https://github.com/sealandseacat/dbmask](https://github.com/sealandseacat/dbmask)

生成摘要时出错

---

## 76. Michael Levin: Ingressing Minds

**原文标题**: Michael Levin: Ingressing Minds

**原文链接**: [https://www.mdpi.com/2409-9287/11/5/161](https://www.mdpi.com/2409-9287/11/5/161)

生成摘要时出错

---

## 77. Planet Labs' open satellite feed

**原文标题**: Planet Labs' open satellite feed

**原文链接**: [https://tech.marksblogg.com/planet-labs-open-satellite-feed.html](https://tech.marksblogg.com/planet-labs-open-satellite-feed.html)

生成摘要时出错

---

## 78. Rivian's gambit for full autonomy

**原文标题**: Rivian's gambit for full autonomy

**原文链接**: [https://spectrum.ieee.org/rivian-self-driving](https://spectrum.ieee.org/rivian-self-driving)

生成摘要时出错

---

## 79. Understanding the recent DDoS attack against Read the Docs

**原文标题**: Understanding the recent DDoS attack against Read the Docs

**原文链接**: [https://about.readthedocs.com/blog/2026/09/2026-ddos-attack/](https://about.readthedocs.com/blog/2026/09/2026-ddos-attack/)

生成摘要时出错

---

## 80. OpenAI Targets Work of Wall Street with New ChatGPT for Financial Services

**原文标题**: OpenAI Targets Work of Wall Street with New ChatGPT for Financial Services

**原文链接**: [https://www.cnbc.com/2026/09/10/openai-chatgpt-for-financial-services-targets-work-of-junior-bankers.html](https://www.cnbc.com/2026/09/10/openai-chatgpt-for-financial-services-targets-work-of-junior-bankers.html)

生成摘要时出错

---

## 81. ChatGPT Pro 20x plan is now unavailable for purchase

**原文标题**: ChatGPT Pro 20x plan is now unavailable for purchase

**原文链接**: [https://twitter.com/aimaddie/status/2098128761388716353](https://twitter.com/aimaddie/status/2098128761388716353)

生成摘要时出错

---

## 82. GPT-6 Astra, looped transformers, and hidden reasoning

**原文标题**: GPT-6 Astra, looped transformers, and hidden reasoning

**原文链接**: [https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and](https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and)

生成摘要时出错

---

## 83. No Man's Sky Cosmos

**原文标题**: No Man's Sky Cosmos

**原文链接**: [https://www.nomanssky.com/cosmos-update/](https://www.nomanssky.com/cosmos-update/)

生成摘要时出错

---

## 84. Oslo bans smart glasses in schools

**原文标题**: Oslo bans smart glasses in schools

**原文链接**: [https://www.thelocal.no/20260910/oslo-bans-smart-glasses-in-schools](https://www.thelocal.no/20260910/oslo-bans-smart-glasses-in-schools)

生成摘要时出错

---

## 85. Bespoke: A programming language for people who say please

**原文标题**: Bespoke: A programming language for people who say please

**原文链接**: [https://blog.hofstede.it/bespoke-a-programming-language-for-people-who-say-please/](https://blog.hofstede.it/bespoke-a-programming-language-for-people-who-say-please/)

生成摘要时出错

---

## 86. Show HN: Math Gambling

**原文标题**: Show HN: Math Gambling

**原文链接**: [https://kuber.studio/math-gambling/](https://kuber.studio/math-gambling/)

生成摘要时出错

---

## 87. Coyote v. Acme (1990)

**原文标题**: Coyote v. Acme (1990)

**原文链接**: [https://www.newyorker.com/magazine/1990/02/26/coyote-v-acme](https://www.newyorker.com/magazine/1990/02/26/coyote-v-acme)

生成摘要时出错

---

## 88. All grown-ups were once children, but only few of them remember it

**原文标题**: All grown-ups were once children, but only few of them remember it

**原文链接**: [https://mathstodon.xyz/@tao/117244102901892965](https://mathstodon.xyz/@tao/117244102901892965)

生成摘要时出错

---

## 89. Thanks to Siri Recaps, your Apple Watch is always listening

**原文标题**: Thanks to Siri Recaps, your Apple Watch is always listening

**原文链接**: [https://www.techradar.com/health-fitness/smartwatches/thanks-to-siri-recaps-your-apple-watch-is-always-listening-as-you-go-about-your-day-but-apple-may-be-risking-a-meta-glasses-style-backlash](https://www.techradar.com/health-fitness/smartwatches/thanks-to-siri-recaps-your-apple-watch-is-always-listening-as-you-go-about-your-day-but-apple-may-be-risking-a-meta-glasses-style-backlash)

生成摘要时出错

---

## 90. USPS Failed to Properly Handle Some Primary Election Ballots, Audit Finds

**原文标题**: USPS Failed to Properly Handle Some Primary Election Ballots, Audit Finds

**原文链接**: [https://www.propublica.org/article/postal-service-audit-primary-election-ballots](https://www.propublica.org/article/postal-service-audit-primary-election-ballots)

生成摘要时出错

---

## 91. Tor VPN Beta: What we've learned building our own VPN for Android from scratch

**原文标题**: Tor VPN Beta: What we've learned building our own VPN for Android from scratch

**原文链接**: [https://blog.torproject.org/tor-vpn-beta/](https://blog.torproject.org/tor-vpn-beta/)

生成摘要时出错

---

## 92. Show HN: Calmscroll – a reader that shows the current paragraph in the library

**原文标题**: Show HN: Calmscroll – a reader that shows the current paragraph in the library

**原文链接**: [https://calmscroll.com](https://calmscroll.com)

生成摘要时出错

---

## 93. Amazon pilots ad services in ChatGPT

**原文标题**: Amazon pilots ad services in ChatGPT

**原文链接**: [https://www.marketingdive.com/news/amazon-pilots-ad-services-in-chatgpt-what-marketers-need-to-know/829945/](https://www.marketingdive.com/news/amazon-pilots-ad-services-in-chatgpt-what-marketers-need-to-know/829945/)

生成摘要时出错

---

## 94. Lotus Notes and the dangers of starting from scratch

**原文标题**: Lotus Notes and the dangers of starting from scratch

**原文链接**: [https://buttondown.com/blog/lotus-notes-email](https://buttondown.com/blog/lotus-notes-email)

生成摘要时出错

---

## 95. AirPods 5

**原文标题**: AirPods 5

**原文链接**: [https://www.apple.com/newsroom/2026/09/apple-introduces-airpods-5-with-best-in-class-open-ear-active-noise-cancellation/](https://www.apple.com/newsroom/2026/09/apple-introduces-airpods-5-with-best-in-class-open-ear-active-noise-cancellation/)

生成摘要时出错

---

## 96. Bending Spoons buying Miro for $1.355B

**原文标题**: Bending Spoons buying Miro for $1.355B

**原文链接**: [https://investors.bendingspoons.com/newsroom/bending-spoons-agrees-to-acquire-miro](https://investors.bendingspoons.com/newsroom/bending-spoons-agrees-to-acquire-miro)

生成摘要时出错

---

## 97. iPhone 18 Pro and iPhone 18 Pro Max

**原文标题**: iPhone 18 Pro and iPhone 18 Pro Max

**原文链接**: [https://www.apple.com/newsroom/2026/09/apple-debuts-iphone-18-pro-and-iphone-18-pro-max/](https://www.apple.com/newsroom/2026/09/apple-debuts-iphone-18-pro-and-iphone-18-pro-max/)

生成摘要时出错

---

## 98. Object storage is all you need

**原文标题**: Object storage is all you need

**原文链接**: [https://www.tigrisdata.com/blog/object-storage-all-need/](https://www.tigrisdata.com/blog/object-storage-all-need/)

生成摘要时出错

---

## 99. ESP32 Bit Pirate Hardware Hacking Kit with Web Tools That Speaks Every Protocol

**原文标题**: ESP32 Bit Pirate Hardware Hacking Kit with Web Tools That Speaks Every Protocol

**原文链接**: [https://geo-tp.github.io/ESP32-Bit-Pirate/](https://geo-tp.github.io/ESP32-Bit-Pirate/)

生成摘要时出错

---

## 100. Sort Your Perl Imports

**原文标题**: Sort Your Perl Imports

**原文链接**: [https://www.olafalders.com/2026/09/10/sort-your-perl-imports/](https://www.olafalders.com/2026/09/10/sort-your-perl-imports/)

生成摘要时出错

---

