# Hacker News 热门文章摘要 (2026-10-02)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Apple 凭证设计器

**原文标题**: Apple Pass Designer

**原文链接**: [https://developer.apple.com/pass-designer/](https://developer.apple.com/pass-designer/)

**Apple Pass Designer** 是一款旨在帮助各种规模的企业为 Apple 钱包创建、预览和优化数字凭证的工具。无论是航空公司、咖啡馆还是健身中心，该软件都能通过允许用户使用 Apple 提供的模板或从其他设计工具导入自定义品牌资产，从而简化设计流程。

核心功能包括：

*   **实时渲染：** 该工具使用原生 iOS 和 watchOS 渲染引擎，在进行编辑时，可以精确预览凭证在 iPhone 或 Apple Watch 上的呈现效果。
*   **自定义与布局：** 用户可以调整背景、前景和标签颜色，并编辑标准信息字段。该工具支持现代钱包功能，同时保持对旧设备的向后兼容性。
*   **验证：** 集成验证系统会监控设计过程，提醒用户缺失的必填键或数据错误，以确保凭证功能正常。
*   **语义标签：** 专门针对登机牌和活动门票，Pass Designer 允许编辑语义标签。这增加了结构化数据，从而实现系统级集成，如 Siri 建议、日历条目和地图路线。该工具还可以根据这些语义数据自动生成向后兼容的结构。

Pass Designer 测试版需要 **macOS 27 或更高版本**。如需下载该工具，用户必须使用 Apple 账户登录并接受 Apple 开发者协议。

---

## 2. 法院支持 EFF：犹他州 VPN 法律提出了技术上不可能的要求

**原文标题**: Court agrees with EFF: Utah's VPN law demands a technical impossibility

**原文链接**: [https://www.eff.org/deeplinks/2026/10/court-agrees-eff-utahs-vpn-law-demands-technical-impossibility](https://www.eff.org/deeplinks/2026/10/court-agrees-eff-utahs-vpn-law-demands-technical-impossibility)

一名联邦法官发布了一项初步禁令，封锁了犹他州的 SB 73 法案。该法律旨在通过针对虚拟专用网络（VPN）及其他地理位置遮蔽工具的使用，来监管成人网站。电子前沿基金会（EFF）对这一裁决表示赞赏，认为该裁决承认了该法律的要求在“技术上是无法实现的”。

SB 73 要求成人平台要么屏蔽 VPN 用户，要么准确识别所有访客的物理位置，以确保符合犹他州的年龄验证指令。巴洛法官裁定，由于目前无法实现“完美的地理定位”，该法律本质上向企业施加了严格责任。为了规避法律处罚，网站将被迫对全球每一位用户进行年龄验证，或彻底屏蔽所有 VPN 流量。法院认为，这违宪地加重了犹他州以外企业和个人的负担。

EFF 辩称，该法律拟议的执法规则（建议监控连接延迟和设备时区）将导致侵入式监视，并损害全球数字安全。法院对此表示认同，认为与要求全球遵守特定州的指令相比，犹他州拥有负担更轻的方法来保护未成年人。

虽然该裁决暂时中止了法律的执行，但犹他州立法者可能会在未来的议程中尝试修订该法。EFF 坚称，互联网始终会“绕过”此类审查，且州政府强制追踪隐私工具的行为为数字权利开创了危险的先例。目前，这一判决被视为用户匿名性的胜利，同时也承认了法律不能凌驾于技术现实之上。

---

## 3. Zig v0.17.0

**原文标题**: Zig v0.17.0

**原文链接**: [https://ziglang.org/download/0.17.0/release-notes.html](https://ziglang.org/download/0.17.0/release-notes.html)

Zig 0.17.0 版本历经五个月的开发，汇聚了来自 206 位贡献者的 900 多次提交。此版本专注于通往 1.0 版本的路线图，重点提升了构建系统的成熟度、链接器的稳定性以及语言的精炼度。

**核心亮点：**
*   **构建系统与服务器：** 重构了构建系统，并引入了 **构建服务器协议 (BSP)** 以改进工具链集成。
*   **增量编译：** 对 ELF 链接器的重大增强意味着 **x86_64-linux** 平台上的所有用户现在都可以获得稳定的增量编译体验。
*   **语言演进：** 通过解决数百项语言提案，在稳定性方面取得了显著进展。显著变化包括：重新定义了 `@bitCast`（专注于逻辑位表示）；移除了数组乘法语法和 `i0` 类型；引入了 `@divCeil` 和 `@backingInt` 等内建函数。此外，C 语言转换和 Windows 资源编译已移至外部包。
*   **目标支持：** 扩展了对 **Loongarch32**、**SPARC64** 以及多种游戏主机（包括 Switch、GBA、PSX 和 WiiU）的支持。为 aarch64-openbsd 添加了原生 CI 测试。相反，由于浮点格式不兼容，停止了对某些 PowerPC-linux 目标的支持。
*   **标准库：** 此版本引入了 `SafeAllocator`，重构了 `StackFallbackAllocator`，并更新了 `std.zon.parse`。标准库现在还支持 x32 和 N32 等小众的 ILP32 ABI。
*   **工具链更新：** Zig 现在使用 **LLVM 22**、musl 1.2.5 和 glibc 2.44，同时增强了所有架构的原生 CPU 特性检测。

该版本标志着在缩小语言范围和改进内部基础设施（特别是自研链接器和增量工作流）方面迈出了重要一步。

---

## 4. 一颗恒星及其四颗绕转行星的12年望远镜图像序列

**原文标题**: A 12-year sequence of telescope images of a star and four planets orbiting

**原文链接**: [https://bsky.app/profile/theplanetaryguy.com/post/3mwucf5ert22f](https://bsky.app/profile/theplanetaryguy.com/post/3mwucf5ert22f)

本文展示了一段令人惊叹的、跨度长达12年的真实望远镜影像，记录了一个距离地球133光年的恒星系统。这段影像捕捉到了四颗比木星还要巨大的系外行星，它们正缓慢地绕其宿主恒星公转。这种罕见的直接成像为观测遥远行星系统中的行星运动提供了视觉记录，也为我们观察遥远世界的运行方式提供了独特的视角。

---

## 5. Greg Kroah-Hartman – Security in the LLM Age [video]

**原文标题**: Greg Kroah-Hartman – Security in the LLM Age [video]

**原文链接**: [https://www.youtube.com/watch?v=NnV_cWeoo5Q](https://www.youtube.com/watch?v=NnV_cWeoo5Q)

所提供的内容仅包含标准的 YouTube 模板和法律文本。然而，基于标题**“Greg Kroah-Hartman —— 大语言模型（LLM）时代的安全性”**，以下是这位 Linux 内核维护者通常就该主题讨论的核心主题摘要：

在本次演讲中，Greg Kroah-Hartman 探讨了大语言模型（LLM）给开源软件安全（特别是 Linux 内核）带来的挑战与机遇。

**核心观点：**

*   **LLM 是工具而非作者：** Kroah-Hartman 强调 LLM 是开发者的工具，而非替代品。虽然它们可以辅助生成模版代码，但缺乏对系统逻辑和安全上下文的根本理解。
*   **“幻觉”补丁问题：** 一个重要担忧是 AI 生成代码提交的兴起。这些补丁通常看起来在技术上是正确的，但可能包含微妙且关键的漏洞，或者“虚构”出不存在的 API，这显著增加了人类维护者的审核负担。
*   **安全研究与模糊测试：** 从积极的一面来看，他指出 LLM 在“防御性”安全方面功能强大。它们可用于自动化创建模糊测试（Fuzzing tests），并识别以前难以通过手动检测的漏洞模式。
*   **维护信任模型：** Linux 内核的开发流程建立在人与人之间的“信任链”之上。Kroah-Hartman 认为，由于 AI 无法为安全漏洞承担责任，人类的监督和“Signed-off-by”标签仍然是内核完整性的基石。
*   **强制验证：** 他的核心信息是“信任但要验证”。随着 AI 降低了代码生成的门槛，强大的自动化测试框架和严格的人类同行评审变得比以往任何时候都更加关键，以防止自动化工具引入自动化的漏洞。

---

## 6. From the creator of Redis; run LLM locally with ds4

**原文标题**: From the creator of Redis; run LLM locally with ds4

**原文链接**: [https://dwarfstar.sh/](https://dwarfstar.sh/)

Salvatore Sanfilippo, the creator of Redis, has introduced a method to run Large Language Models (LLMs) locally using a tool called **ds4**. 

The core of this approach is a technique known as **CORE 01 Asymmetric 2-bit quantization**. This method is specifically designed to optimize Mixture-of-Experts (MoE) models for local hardware. The strategy works by heavily compressing the "routed experts" while maintaining high precision for the critical shared paths within the model. 

By selectively applying 2-bit quantization, the system significantly reduces the memory footprint of MoE architectures, allowing large, complex models to fit and run efficiently on consumer-grade target machines without sacrificing the integrity of essential data paths.

---

## 7. With most information hidden, the game Stratego had stumped AI until now

**原文标题**: With most information hidden, the game Stratego had stumped AI until now

**原文链接**: [https://arstechnica.com/science/2026/10/ai-finally-beat-the-best-stratego-player-in-history-and-did-it-on-a-budget/](https://arstechnica.com/science/2026/10/ai-finally-beat-the-best-stratego-player-in-history-and-did-it-on-a-budget/)

生成摘要时出错

---

## 8. Loss of cell identity drives human aging: Two new papers

**原文标题**: Loss of cell identity drives human aging: Two new papers

**原文链接**: [https://erictopol.substack.com/p/loss-of-cell-identity-drives-human](https://erictopol.substack.com/p/loss-of-cell-identity-drives-human)

生成摘要时出错

---

## 9. Show HN: Made an open-source Lego AI generator

**原文标题**: Show HN: Made an open-source Lego AI generator

**原文链接**: [https://github.com/anteloc/ldraw-nova](https://github.com/anteloc/ldraw-nova)

生成摘要时出错

---

## 10. Muse Gadgets

**原文标题**: Muse Gadgets

**原文链接**: [https://gadgets.muse.ai](https://gadgets.muse.ai)

生成摘要时出错

---

## 11. One month coding with GLM 5.3 Flash

**原文标题**: One month coding with GLM 5.3 Flash

**原文链接**: [https://wagtail.org/blog/one-month-on-glm-53-flash/](https://wagtail.org/blog/one-month-on-glm-53-flash/)

生成摘要时出错

---

## 12. Venice’s failed war against Constantinople led to the first bond market

**原文标题**: Venice’s failed war against Constantinople led to the first bond market

**原文链接**: [https://bigthink.com/books/a-fabulous-debt/](https://bigthink.com/books/a-fabulous-debt/)

生成摘要时出错

---

## 13. Everyone's Packing Up

**原文标题**: Everyone's Packing Up

**原文链接**: [https://widdershins.verja.net/everyones-packing-up/](https://widdershins.verja.net/everyones-packing-up/)

生成摘要时出错

---

## 14. Mike Tomlin spent 12 years building a Minecraft city

**原文标题**: Mike Tomlin spent 12 years building a Minecraft city

**原文链接**: [https://www.nytimes.com/athletic/7648198/2026/10/01/mike-tomlin-minecraft-nfl-coach/](https://www.nytimes.com/athletic/7648198/2026/10/01/mike-tomlin-minecraft-nfl-coach/)

生成摘要时出错

---

## 15. Sites in ChatGPT

**原文标题**: Sites in ChatGPT

**原文链接**: [https://chatgpt.com/features/sites/](https://chatgpt.com/features/sites/)

生成摘要时出错

---

## 16. The Legend of von Neumann (1973) [pdf]

**原文标题**: The Legend of von Neumann (1973) [pdf]

**原文链接**: [https://gwern.net/doc/math/1973-halmos.pdf](https://gwern.net/doc/math/1973-halmos.pdf)

生成摘要时出错

---

## 17. Anatomy of a Lean proof for software engineers

**原文标题**: Anatomy of a Lean proof for software engineers

**原文链接**: [https://agostbiro.net/posts/2026-10-anatomy-of-a-lean-proof/](https://agostbiro.net/posts/2026-10-anatomy-of-a-lean-proof/)

生成摘要时出错

---

## 18. Blogging with Gleam, Org-Mode and Pandoc

**原文标题**: Blogging with Gleam, Org-Mode and Pandoc

**原文链接**: [https://byzantine-systems.github.io/blogging-with-gleam-org-mode-and-pandoc/](https://byzantine-systems.github.io/blogging-with-gleam-org-mode-and-pandoc/)

生成摘要时出错

---

## 19. STS-51-F Abort-to-Orbit (1985)

**原文标题**: STS-51-F Abort-to-Orbit (1985)

**原文链接**: [https://en.wikipedia.org/wiki/STS-51-F](https://en.wikipedia.org/wiki/STS-51-F)

生成摘要时出错

---

## 20. FLUX 3 Image

**原文标题**: FLUX 3 Image

**原文链接**: [https://bfl.ai/models/flux-3-image](https://bfl.ai/models/flux-3-image)

生成摘要时出错

---

## 21. GrapheneOS has fixed the Android 17 QPR1 kernel performance regression

**原文标题**: GrapheneOS has fixed the Android 17 QPR1 kernel performance regression

**原文链接**: [https://discuss.grapheneos.org/d/42511-grapheneos-has-fixed-the-massive-android-17-qpr1-kernel-performance-regression](https://discuss.grapheneos.org/d/42511-grapheneos-has-fixed-the-massive-android-17-qpr1-kernel-performance-regression)

生成摘要时出错

---

## 22. Our Project Suncatcher prototype satellite is in orbit

**原文标题**: Our Project Suncatcher prototype satellite is in orbit

**原文链接**: [https://blog.google/innovation-and-ai/models-and-research/google-research/project-suncatcher-prototype/](https://blog.google/innovation-and-ai/models-and-research/google-research/project-suncatcher-prototype/)

生成摘要时出错

---

## 23. The first packet sent via RFC1149 avian carrier is up for auction at Christie's

**原文标题**: The first packet sent via RFC1149 avian carrier is up for auction at Christie's

**原文链接**: [https://onlineonly.christies.com/s/fine-printed-books-manuscripts-science/carrier-pigeon-internet-protocol-150/325216](https://onlineonly.christies.com/s/fine-printed-books-manuscripts-science/carrier-pigeon-internet-protocol-150/325216)

生成摘要时出错

---

## 24. Show HN: Giving Opus 5.5 a simulated paint canvas

**原文标题**: Show HN: Giving Opus 5.5 a simulated paint canvas

**原文链接**: [https://stillwet.art/](https://stillwet.art/)

生成摘要时出错

---

## 25. F.02 Decommission

**原文标题**: F.02 Decommission

**原文链接**: [https://www.figure.ai/news/f-02-decommission](https://www.figure.ai/news/f-02-decommission)

生成摘要时出错

---

## 26. Show HN: Pyxel – A Python retro game engine with built-in art and sound editors

**原文标题**: Show HN: Pyxel – A Python retro game engine with built-in art and sound editors

**原文链接**: [https://github.com/kitao/pyxel](https://github.com/kitao/pyxel)

生成摘要时出错

---

## 27. What if we stopped using GPUs? [video]

**原文标题**: What if we stopped using GPUs? [video]

**原文链接**: [https://www.youtube.com/watch?v=xc2FTBGRSJo](https://www.youtube.com/watch?v=xc2FTBGRSJo)

生成摘要时出错

---

## 28. "The only intuitive interface is the nipple" (2012)

**原文标题**: "The only intuitive interface is the nipple" (2012)

**原文链接**: [https://www.greenend.org.uk/rjk/misc/nipple.html](https://www.greenend.org.uk/rjk/misc/nipple.html)

生成摘要时出错

---

## 29. 100 years of student radio history in the DLARC college radio collections

**原文标题**: 100 years of student radio history in the DLARC college radio collections

**原文链接**: [https://blog.archive.org/2026/10/02/100-years-of-student-radio-history-in-the-dlarc-college-radio-collections/](https://blog.archive.org/2026/10/02/100-years-of-student-radio-history-in-the-dlarc-college-radio-collections/)

生成摘要时出错

---

## 30. Crypto Capture of Foreign Aid

**原文标题**: Crypto Capture of Foreign Aid

**原文链接**: [https://www.nber.org/papers/w35655](https://www.nber.org/papers/w35655)

生成摘要时出错

---

## 31. Three AI agents, two countries, and one uneven world wide web

**原文标题**: Three AI agents, two countries, and one uneven world wide web

**原文链接**: [https://royapakzad.substack.com/p/multilingual-ai-agents](https://royapakzad.substack.com/p/multilingual-ai-agents)

生成摘要时出错

---

## 32. How accurately calibrated is Jev?

**原文标题**: How accurately calibrated is Jev?

**原文链接**: [https://maximumeffort.substack.com/p/jev-is-poorly-calibrated](https://maximumeffort.substack.com/p/jev-is-poorly-calibrated)

生成摘要时出错

---

## 33. Supabase is acquiring Turso

**原文标题**: Supabase is acquiring Turso

**原文链接**: [https://supabase.com/blog/supabase-is-acquiring-turso](https://supabase.com/blog/supabase-is-acquiring-turso)

生成摘要时出错

---

## 34. Tiny Brutalism

**原文标题**: Tiny Brutalism

**原文链接**: [https://placeholders.itch.io/tiny-brutalism](https://placeholders.itch.io/tiny-brutalism)

生成摘要时出错

---

## 35. On social reality in China

**原文标题**: On social reality in China

**原文链接**: [https://www.lesswrong.com/posts/b5cSYh4emQb2qrGmK/on-social-reality-in-china](https://www.lesswrong.com/posts/b5cSYh4emQb2qrGmK/on-social-reality-in-china)

生成摘要时出错

---

## 36. Qubes OS 4.3.2 has been released

**原文标题**: Qubes OS 4.3.2 has been released

**原文链接**: [https://www.qubes-os.org/news/2026/10/02/qubes-os-4-3-2-has-been-released/](https://www.qubes-os.org/news/2026/10/02/qubes-os-4-3-2-has-been-released/)

生成摘要时出错

---

## 37. Show HN: Our space game has a built-in RISC-V emulator that runs Linux

**原文标题**: Show HN: Our space game has a built-in RISC-V emulator that runs Linux

**原文链接**: [https://againstallodds.games/](https://againstallodds.games/)

生成摘要时出错

---

## 38. Dutch computer museums (2022)

**原文标题**: Dutch computer museums (2022)

**原文链接**: [https://aresluna.org/dutch-computer-museums/](https://aresluna.org/dutch-computer-museums/)

生成摘要时出错

---

## 39. Mystery Function

**原文标题**: Mystery Function

**原文链接**: [https://codeset.ai/function](https://codeset.ai/function)

生成摘要时出错

---

## 40. Shimano Bicycle Museum Review

**原文标题**: Shimano Bicycle Museum Review

**原文链接**: [https://inrng.com/2026/10/shimano-bicycle-museum/](https://inrng.com/2026/10/shimano-bicycle-museum/)

生成摘要时出错

---

## 41. To grieve, or not to grieve?

**原文标题**: To grieve, or not to grieve?

**原文链接**: [https://xenaproject.wordpress.com/2026/10/01/to-grieve-or-not-to-grieve/](https://xenaproject.wordpress.com/2026/10/01/to-grieve-or-not-to-grieve/)

生成摘要时出错

---

## 42. SequenceHash: Multihashing for the rest of us

**原文标题**: SequenceHash: Multihashing for the rest of us

**原文链接**: [https://blog.trailofbits.com/2026/10/02/sequencehash-multihashing-for-the-rest-of-us/](https://blog.trailofbits.com/2026/10/02/sequencehash-multihashing-for-the-rest-of-us/)

生成摘要时出错

---

## 43. Hardly Promethean

**原文标题**: Hardly Promethean

**原文链接**: [https://jardo.dev/hardly-promethean](https://jardo.dev/hardly-promethean)

生成摘要时出错

---

## 44. ExplainDB: A Database System Built for Understandability

**原文标题**: ExplainDB: A Database System Built for Understandability

**原文链接**: [https://github.com/explaindb/explaindb](https://github.com/explaindb/explaindb)

生成摘要时出错

---

## 45. Giving friends custom text buzzes based on Morse code

**原文标题**: Giving friends custom text buzzes based on Morse code

**原文链接**: [https://liquidbrain.net/blog/giving-friends-custom-text-buzzes-based-on-morse-code/](https://liquidbrain.net/blog/giving-friends-custom-text-buzzes-based-on-morse-code/)

生成摘要时出错

---

## 46. The Philadelphia Inquirer built Scrape, an AI tool to surface hyperlocal news

**原文标题**: The Philadelphia Inquirer built Scrape, an AI tool to surface hyperlocal news

**原文链接**: [https://www.lenfestinstitute.org/solutions-resources/philadelphia-inquirer-scrape-ai-hyperlocal-news/](https://www.lenfestinstitute.org/solutions-resources/philadelphia-inquirer-scrape-ai-hyperlocal-news/)

生成摘要时出错

---

## 47. Lambda Land

**原文标题**: Lambda Land

**原文链接**: [https://lambdaland.org/posts/2026-10-01-measure/](https://lambdaland.org/posts/2026-10-01-measure/)

生成摘要时出错

---

## 48. Lace and Labor: Lessons from the actual Luddites

**原文标题**: Lace and Labor: Lessons from the actual Luddites

**原文链接**: [https://articlesofinterest.substack.com/p/lace-and-labor](https://articlesofinterest.substack.com/p/lace-and-labor)

生成摘要时出错

---

## 49. On building a worm detector

**原文标题**: On building a worm detector

**原文链接**: [https://bencology.bearblog.dev/mapping-individual-and-collective-worm-movements/](https://bencology.bearblog.dev/mapping-individual-and-collective-worm-movements/)

生成摘要时出错

---

## 50. Magic Switch: Share Apple Magic keyboard/track-pad/mouse between two Macs

**原文标题**: Magic Switch: Share Apple Magic keyboard/track-pad/mouse between two Macs

**原文链接**: [https://joshua.hu/magic-switch-easily-switch-magic-keyboard-trackpad-mouse-between-mac-macbook-macos](https://joshua.hu/magic-switch-easily-switch-magic-keyboard-trackpad-mouse-between-mac-macbook-macos)

生成摘要时出错

---

## 51. Robot Hands for Modern AI and Real Work

**原文标题**: Robot Hands for Modern AI and Real Work

**原文链接**: [https://bostondynamics.com/blog/robot-hands-for-modern-ai-and-real-work/](https://bostondynamics.com/blog/robot-hands-for-modern-ai-and-real-work/)

生成摘要时出错

---

## 52. Now That's an Impurity Story

**原文标题**: Now That's an Impurity Story

**原文链接**: [https://www.science.org/content/blog-post/now-s-impurity-story](https://www.science.org/content/blog-post/now-s-impurity-story)

生成摘要时出错

---

## 53. Scientists untangle the biology of an 'undruggable' cancer gene

**原文标题**: Scientists untangle the biology of an 'undruggable' cancer gene

**原文链接**: [https://www.nytimes.com/2026/10/02/science/scientists-untangle-the-biology-of-an-undruggable-cancer-gene.html](https://www.nytimes.com/2026/10/02/science/scientists-untangle-the-biology-of-an-undruggable-cancer-gene.html)

生成摘要时出错

---

## 54. The Nintendo 64 Partner-N64 Development Kit

**原文标题**: The Nintendo 64 Partner-N64 Development Kit

**原文链接**: [https://www.behindthecode.ca/partner-n64pc-dev-kit/](https://www.behindthecode.ca/partner-n64pc-dev-kit/)

生成摘要时出错

---

## 55. Capcom RE:Dox, open source serialization/deserialization for game engines

**原文标题**: Capcom RE:Dox, open source serialization/deserialization for game engines

**原文链接**: [https://github.com/CAPCOM-TD-OSS/REDox](https://github.com/CAPCOM-TD-OSS/REDox)

生成摘要时出错

---

## 56. Colorectal Cancer Is Rising Among the Young, Even Kids and Teens

**原文标题**: Colorectal Cancer Is Rising Among the Young, Even Kids and Teens

**原文链接**: [https://gizmodo.com/colorectal-cancer-is-rising-among-kids-and-teens-and-its-not-the-same-disease-adults-get-2000818128](https://gizmodo.com/colorectal-cancer-is-rising-among-kids-and-teens-and-its-not-the-same-disease-adults-get-2000818128)

生成摘要时出错

---

## 57. Show HN: Audionaut – an open-source cross-platform multitrack audio editor

**原文标题**: Show HN: Audionaut – an open-source cross-platform multitrack audio editor

**原文链接**: [https://github.com/kvoltmer/Audionaut](https://github.com/kvoltmer/Audionaut)

生成摘要时出错

---

## 58. AI as Normal Technology (2025)

**原文标题**: AI as Normal Technology (2025)

**原文链接**: [https://knightcolumbia.org/content/ai-as-normal-technology](https://knightcolumbia.org/content/ai-as-normal-technology)

生成摘要时出错

---

## 59. Scientists invent underwater umbrellas to protect coral reefs

**原文标题**: Scientists invent underwater umbrellas to protect coral reefs

**原文链接**: [https://gizmodo.com/scientists-invent-underwater-umbrellas-to-protect-coral-reefs-and-it-appears-to-be-working-2000819444](https://gizmodo.com/scientists-invent-underwater-umbrellas-to-protect-coral-reefs-and-it-appears-to-be-working-2000819444)

生成摘要时出错

---

## 60. Fast Blur with Animated Radius

**原文标题**: Fast Blur with Animated Radius

**原文链接**: [https://aras-p.info/blog/2026/10/01/Fast-blur-with-animated-radius/](https://aras-p.info/blog/2026/10/01/Fast-blur-with-animated-radius/)

生成摘要时出错

---

## 61. Show HN: Enki – Write GPU compute kernels in pure stable Rust

**原文标题**: Show HN: Enki – Write GPU compute kernels in pure stable Rust

**原文链接**: [https://github.com/enkiruntime/enki](https://github.com/enkiruntime/enki)

生成摘要时出错

---

## 62. Show HN: Use all Codex Plugins inside Pi

**原文标题**: Show HN: Use all Codex Plugins inside Pi

**原文链接**: [https://github.com/wileai/pi-codex-connectors](https://github.com/wileai/pi-codex-connectors)

生成摘要时出错

---

## 63. SvelteKit 3

**原文标题**: SvelteKit 3

**原文链接**: [https://svelte.dev/blog/sveltekit-3-is-here](https://svelte.dev/blog/sveltekit-3-is-here)

生成摘要时出错

---

## 64. ICE Has Been Dumping Protester Photos into a Palantir Database

**原文标题**: ICE Has Been Dumping Protester Photos into a Palantir Database

**原文链接**: [https://www.wired.com/story/ice-has-been-dumping-protester-photos-into-a-palantir-database/](https://www.wired.com/story/ice-has-been-dumping-protester-photos-into-a-palantir-database/)

生成摘要时出错

---

## 65. Git 3.0's upcoming SHA-256 default will be a costly mistake

**原文标题**: Git 3.0's upcoming SHA-256 default will be a costly mistake

**原文链接**: [https://blog.gitbutler.com/git-3-sha-256](https://blog.gitbutler.com/git-3-sha-256)

生成摘要时出错

---

## 66. Leaderboards and speedrun.com's new terms of service

**原文标题**: Leaderboards and speedrun.com's new terms of service

**原文链接**: [https://therun.gg/blog/leaderboards-speedruncom](https://therun.gg/blog/leaderboards-speedruncom)

生成摘要时出错

---

## 67. Decision models like Jev don't beat LLM-as-a-judge or traditional classifiers

**原文标题**: Decision models like Jev don't beat LLM-as-a-judge or traditional classifiers

**原文链接**: [https://developers.redhat.com/articles/2026/10/02/benchmarking-ai-decision-models-against-traditional-guardrails](https://developers.redhat.com/articles/2026/10/02/benchmarking-ai-decision-models-against-traditional-guardrails)

生成摘要时出错

---

## 68. Martian chaos terrain

**原文标题**: Martian chaos terrain

**原文链接**: [https://en.wikipedia.org/wiki/Martian_chaos_terrain](https://en.wikipedia.org/wiki/Martian_chaos_terrain)

生成摘要时出错

---

## 69. Pi 1.0

**原文标题**: Pi 1.0

**原文链接**: [https://earendil.com/posts/pi-1-0/](https://earendil.com/posts/pi-1-0/)

生成摘要时出错

---

## 70. After 15 years, I am leaving tech

**原文标题**: After 15 years, I am leaving tech

**原文链接**: [https://hey.georgie.nu/end-of-an-era/](https://hey.georgie.nu/end-of-an-era/)

生成摘要时出错

---

## 71. Truemetrics (YC S23) Is Hiring a GTM Founder's Associate

**原文标题**: Truemetrics (YC S23) Is Hiring a GTM Founder's Associate

**原文链接**: [https://www.ycombinator.com/companies/truemetrics/jobs/THLEzXI-gtm-founder-s-associate](https://www.ycombinator.com/companies/truemetrics/jobs/THLEzXI-gtm-founder-s-associate)

生成摘要时出错

---

## 72. Show HN: Graphene – Data analysis toolkit for your coding agent

**原文标题**: Show HN: Graphene – Data analysis toolkit for your coding agent

**原文链接**: [https://github.com/graphene-data/graphene](https://github.com/graphene-data/graphene)

生成摘要时出错

---

## 73. Show HN: Breadcrumb, record everything on your mac + context manager for AI

**原文标题**: Show HN: Breadcrumb, record everything on your mac + context manager for AI

**原文链接**: [https://innerloop.works/breadcrumb](https://innerloop.works/breadcrumb)

生成摘要时出错

---

## 74. Fixing GRPO's credit assignment problem without evaluating every step

**原文标题**: Fixing GRPO's credit assignment problem without evaluating every step

**原文链接**: [https://arxiv.org/abs/2609.36178](https://arxiv.org/abs/2609.36178)

生成摘要时出错

---

## 75. Pi Durable

**原文标题**: Pi Durable

**原文链接**: [https://earendil.com/posts/pi-durable/](https://earendil.com/posts/pi-durable/)

生成摘要时出错

---

## 76. DeepSeek Harness Desktop for macOS and Windows

**原文标题**: DeepSeek Harness Desktop for macOS and Windows

**原文链接**: [https://www.deepseek.com/en/harness/](https://www.deepseek.com/en/harness/)

生成摘要时出错

---

## 77. Show HN: PhreshOS – OS for Web Apps

**原文标题**: Show HN: PhreshOS – OS for Web Apps

**原文链接**: [https://github.com/PhreshOS/system](https://github.com/PhreshOS/system)

生成摘要时出错

---

## 78. Updates to Full Disk Access in macOS

**原文标题**: Updates to Full Disk Access in macOS

**原文链接**: [https://developer.apple.com/news/?id=p6zjojqw](https://developer.apple.com/news/?id=p6zjojqw)

生成摘要时出错

---

## 79. Turbo Haskell

**原文标题**: Turbo Haskell

**原文链接**: [https://comonad.com/reader/2026/turbo-haskell/](https://comonad.com/reader/2026/turbo-haskell/)

生成摘要时出错

---

## 80. ICC judge on what U.S. sanctions mean for her and global courts

**原文标题**: ICC judge on what U.S. sanctions mean for her and global courts

**原文链接**: [https://www.npr.org/2026/10/01/nx-s1-5977815/trump-icc-sanctions-kimberly-prost](https://www.npr.org/2026/10/01/nx-s1-5977815/trump-icc-sanctions-kimberly-prost)

生成摘要时出错

---

## 81. Cancel Your Subscription: a free browser game

**原文标题**: Cancel Your Subscription: a free browser game

**原文链接**: [https://www.fundrstudio.com/games/cancel-your-subscription/](https://www.fundrstudio.com/games/cancel-your-subscription/)

生成摘要时出错

---

## 82. Rai: CPU-only LLM inference engine in pure Rust

**原文标题**: Rai: CPU-only LLM inference engine in pure Rust

**原文链接**: [https://github.com/Classevelabs/rai](https://github.com/Classevelabs/rai)

生成摘要时出错

---

## 83. Using Opus 5.5 to discover a new eyewitness record of the dodo

**原文标题**: Using Opus 5.5 to discover a new eyewitness record of the dodo

**原文链接**: [https://resobscura.substack.com/p/using-opus-55-to-discover-a-new-eyewitness](https://resobscura.substack.com/p/using-opus-55-to-discover-a-new-eyewitness)

生成摘要时出错

---

## 84. Several vulnerabilities have been discovered in the Linux kernel

**原文标题**: Several vulnerabilities have been discovered in the Linux kernel

**原文链接**: [https://lwn.net/Articles/1097401/](https://lwn.net/Articles/1097401/)

生成摘要时出错

---

## 85. Apple is tightening macOS 'Full Disk Access' due to new risks from AI agents

**原文标题**: Apple is tightening macOS 'Full Disk Access' due to new risks from AI agents

**原文链接**: [https://techcrunch.com/2026/10/02/apple-says-its-tightening-macos-full-disk-access-controls-due-to-new-risks-from-ai-agents/](https://techcrunch.com/2026/10/02/apple-says-its-tightening-macos-full-disk-access-controls-due-to-new-risks-from-ai-agents/)

生成摘要时出错

---

## 86. Automatic Transmission – a data-privacy study of connected vehicles

**原文标题**: Automatic Transmission – a data-privacy study of connected vehicles

**原文链接**: [https://automatictransmission.khoury.northeastern.edu/index.html](https://automatictransmission.khoury.northeastern.edu/index.html)

生成摘要时出错

---

## 87. Nazi Germany had no hope of making an atomic bomb, uranium cubes reveal

**原文标题**: Nazi Germany had no hope of making an atomic bomb, uranium cubes reveal

**原文链接**: [https://www.science.org/content/article/nazi-germany-had-no-hope-making-atomic-bomb-uranium-cubes-reveal](https://www.science.org/content/article/nazi-germany-had-no-hope-making-atomic-bomb-uranium-cubes-reveal)

生成摘要时出错

---

## 88. Benchmarking retrieval for agents on messy real-world company knowledge

**原文标题**: Benchmarking retrieval for agents on messy real-world company knowledge

**原文链接**: [https://www.kapa.ai/blog/company-knowledge-bench](https://www.kapa.ai/blog/company-knowledge-bench)

生成摘要时出错

---

## 89. RIP, vector database

**原文标题**: RIP, vector database

**原文链接**: [https://turbopuffer.com/blog/rip-vector-database](https://turbopuffer.com/blog/rip-vector-database)

生成摘要时出错

---

## 90. Various Projects Find Hidden SDR Capabilities in ESP32 Microcontrollers

**原文标题**: Various Projects Find Hidden SDR Capabilities in ESP32 Microcontrollers

**原文链接**: [https://www.rtl-sdr.com/various-projects-independently-find-hidden-sdr-capabilities-in-esp32-microcontrollers/](https://www.rtl-sdr.com/various-projects-independently-find-hidden-sdr-capabilities-in-esp32-microcontrollers/)

生成摘要时出错

---

## 91. CA tech executive arrested for allegedly smuggling $300M in Nvidia chips to CN

**原文标题**: CA tech executive arrested for allegedly smuggling $300M in Nvidia chips to CN

**原文链接**: [https://qz.com/greg-lui-earthmade-nvidia-ai-chips-smuggling-china-100226](https://qz.com/greg-lui-earthmade-nvidia-ai-chips-smuggling-china-100226)

生成摘要时出错

---

## 92. The OpenAI Decisions API needs a confidence you can trust

**原文标题**: The OpenAI Decisions API needs a confidence you can trust

**原文链接**: [https://anth.us/blog/openai-decisions-api-preview/](https://anth.us/blog/openai-decisions-api-preview/)

生成摘要时出错

---

## 93. Vote on which of Hacker News' challenges for AI have been met

**原文标题**: Vote on which of Hacker News' challenges for AI have been met

**原文链接**: [https://stoppels.ch/goalposts/](https://stoppels.ch/goalposts/)

生成摘要时出错

---

## 94. CSS Bed: Classless CSS themes to use as starting points in web development

**原文标题**: CSS Bed: Classless CSS themes to use as starting points in web development

**原文链接**: [https://www.cssbed.com](https://www.cssbed.com)

生成摘要时出错

---

## 95. Show HN: Bise – a multi-agent harness, made for humans

**原文标题**: Show HN: Bise – a multi-agent harness, made for humans

**原文链接**: [https://bise.dev/](https://bise.dev/)

生成摘要时出错

---

## 96. Frog and Toad and the Increasingly Capable Machines

**原文标题**: Frog and Toad and the Increasingly Capable Machines

**原文链接**: [https://www.frogandtoad.ai/](https://www.frogandtoad.ai/)

生成摘要时出错

---

## 97. Clef: Open-weight decision models, and new RL fine-tuning platform

**原文标题**: Clef: Open-weight decision models, and new RL fine-tuning platform

**原文链接**: [https://blog.cloudflare.com/clef-decision-models/](https://blog.cloudflare.com/clef-decision-models/)

生成摘要时出错

---

## 98. LightPanda 1.0

**原文标题**: LightPanda 1.0

**原文链接**: [https://lightpanda.io/blog/posts/lightpanda-1-0](https://lightpanda.io/blog/posts/lightpanda-1-0)

生成摘要时出错

---

## 99. Show HN: We built a real-time desktop companion for patient's telehealth visits

**原文标题**: Show HN: We built a real-time desktop companion for patient's telehealth visits

**原文链接**: [https://openhand.health](https://openhand.health)

生成摘要时出错

---

## 100. Cloudflare K2: serverless event streams

**原文标题**: Cloudflare K2: serverless event streams

**原文链接**: [https://blog.cloudflare.com/cloudflare-k2-streams/](https://blog.cloudflare.com/cloudflare-k2-streams/)

生成摘要时出错

---

