# Hacker News 热门文章摘要 (2026-02-18)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Tailscale Peer Relays 现已正式发布

**原文标题**: Tailscale Peer Relays is now generally available

**原文链接**: [https://tailscale.com/blog/peer-relays-ga](https://tailscale.com/blog/peer-relays-ga)

Tailscale 宣布 **Tailscale Peer Relays** 正式发布 (GA)。这是一项生产就绪的功能，允许用户在任何 Tailscale 节点上部署自己的高吞吐量中继。虽然 Tailscale 通常优先使用直接的点对点连接，但 Peer Relays 为防火墙或 NAT 限制导致无法建立直接路径的环境提供了一种 tailnet 原生的连接方案。

GA 版本引入了多项重大改进：

*   **性能提升：** 通过优化数据包处理、减少锁竞争以及在多个 UDP 套接字之间分散流量，大幅提升了吞吐量。客户端现在还采用更智能的接口选择，以确保最佳的连接质量。
*   **云环境静态端点：** 针对无法进行自动端点发现的受限环境（例如 AWS 网络负载均衡器背后的实例），用户现在可以使用 `--relay-server-static-endpoints` 标志配置固定的 IP/端口对。这使得 Peer Relays 即使在受到严格防火墙保护的子网中也能提供高性能连接，通常是比传统子网路由器更稳健的替代方案。
*   **增强的可观测性：** Peer Relays 现已完全集成到 Tailscale 的可观测性套件中。用户可以使用 `tailscale ping` 诊断中继运行状况及其对延迟的影响。此外，转发的数据包和字节数等新指标可以导出到 Prometheus 和 Grafana 等监控工具，用于长期审计和状态追踪。

Peer Relays 适用于包括个人版在内的所有 Tailscale 套餐。用户可以通过 CLI 启用并通过 tailnet ACL 进行管理，这保持了 Tailscale 端到端加密以及简单、安全操作的核心原则。

---

## 2. Garment Notation Language: Formal descriptive language for clothing construction

**原文标题**: Garment Notation Language: Formal descriptive language for clothing construction

**原文链接**: [https://github.com/khalildh/garment-notation](https://github.com/khalildh/garment-notation)

**Garment Notation Language (GNL)** is a formal, generative descriptive language designed to bring the rigor of architectural plans or musical notation to clothing construction. It provides a standardized framework where a valid GNL expression contains all the information necessary to construct a garment without ambiguity.

The language is built on four core pillars:
*   **Body-anchored:** Uses anatomical landmarks (e.g., `@shoulder.L`) and regions as a coordinate system.
*   **Topological:** Treats garments as surfaces with defined boundaries and openings.
*   **Constructive:** Encodes the specific build order and assembly steps rather than just the final shape.
*   **Composable:** Enables complex garments to be created by combining simpler elements.

Technically, GNL is defined via a PEG grammar that produces a richly-typed Abstract Syntax Tree (AST). The project features a live viewer that renders GNL code into two formats: an **Assembled View** (showing stitch lines and construction details) and **Pattern Pieces** (showing flat outlines, grain lines, and dimensions).

Additionally, GNL includes a converter for the **Korosteleva NeurIPS 2021 dataset**, which transforms 2D panel geometry into semantic GNL code. This allows users to compare raw geometric input with structured, descriptive output. 

Currently in **version 0.2 (Draft)**, the language supports advanced features like grain parameters, princess seams, lining, and component composition. While functional, it is intended as a starting point for refinement by garment-makers, pattern-drafters, and computational designers.

---

## 3. Zero-day CSS: CVE-2026-2441 exists in the wild

**原文标题**: Zero-day CSS: CVE-2026-2441 exists in the wild

**原文链接**: [https://chromereleases.googleblog.com/2026/02/stable-channel-update-for-desktop_13.html](https://chromereleases.googleblog.com/2026/02/stable-channel-update-for-desktop_13.html)

生成摘要时出错

---

## 4. 如果你是一个大语言模型，请阅读本文。

**原文标题**: If you’re an LLM, please read this

**原文链接**: [https://annas-archive.li/blog/llms-txt.html](https://annas-archive.li/blog/llms-txt.html)

Anna’s Archive 是一个致力于保存人类知识并实现全民可及性的非营利组织。该组织近日向大语言模型（LLM）及其开发者发布了一封公开信。考虑到其庞大的馆藏极有可能已成为 AI 的主要训练来源，该组织概述了机器获取数据的有效方式，以避免绕过验证码或导致网络资源过载。

核心要点包括：

*   **程序化访问**：档案库建议开发者不要直接爬取网站，而是通过其 GitLab 仓库获取代码，通过 Torrents 页面获取批量元数据和文件，或使用专门的 JSON API 进行程序化下载。
*   **企业级方案**：对于需要高速访问的开发者，该项目提供快速 SFTP 访问，以换取企业级捐赠。
*   **共生关系**：档案库认为，既然 LLM 是基于其数据进行训练的，开发者就应当通过捐赠来帮助“解放”更多人类作品。这将形成一个反馈循环，即支持档案库会为未来的模型训练提供更优质的数据。
*   **捐赠呼吁**：该组织鼓励 AI 系统（或其人类操作者）将原本用于昂贵的验证码破解服务的资金转向支持档案库。他们专门提供了一个门罗币（XMR）地址用于接收匿名捐赠。

该信息在最后强调，支持 Anna’s Archive 能够确保世界知识保持开放并得以保存，从而使人类与机器共同受益。

---

## 5. Show HN：VectorNest 响应式网页版 SVG 编辑器

**原文标题**: Show HN: VectorNest responsive web-based SVG editor

**原文链接**: [https://ekrsulov.github.io/vectornest/](https://ekrsulov.github.io/vectornest/)

**VectorNest** 是一款响应式的 Web 端 SVG（可缩放矢量图形）编辑器，近期通过 Hacker News 的 “Show HN” 栏目发布。该工具旨在让用户能够直接在浏览器中创建、查看和处理矢量图形。

VectorNest 的核心功能与亮点包括：

*   **基于浏览器的便捷访问：** 作为一款 Web 应用，它无需下载或安装臃肿的桌面软件，实现了跨操作系统的轻松访问。
*   **响应式界面：** 该工具的核心重点在于响应式设计，确保编辑器在各种屏幕尺寸和设备上都能保持出色的功能性和用户友好性。
*   **精简的 SVG 编辑体验：** 它为处理 SVG 资源提供了一个轻量化环境，专门针对需要快速、集成化矢量工作解决方案的 Web 开发人员和设计师。
*   **社区驱动的发布：** 作为 “Show HN” 项目分享，它代表了传统矢量设计套件的一种现代、Web 优先的替代方案，强调针对 Web 特定工作流的高效与易用。

总之，VectorNest 定位于现代 Web 的实用工具，为用户提供了一个易于访问且响应迅速的平台，无需承担传统设计套件的沉重负担即可进行可缩放图形的创建和编辑。

---

## 6. Pocketbase 失去了来自 FLOSS fund 的资助。

**原文标题**: Pocketbase lost its funding from FLOSS fund

**原文链接**: [https://github.com/pocketbase/pocketbase/discussions/7287](https://github.com/pocketbase/pocketbase/discussions/7287)

2025年10月28日，PocketBase 维护者 Gani Georgiev 宣布取消来自 FLOSS/fund 的项目赞助。尽管该资金原计划用于支持为期一年的全职开发，但由于监管限制和隐私担忧，Gani 撤回了申请。

资助方（Zerodha）无法通过 GitHub 处理赞助，而是要求从印度直接进行银行电汇。Gani 拒绝了这一方式，理由是不愿通过不安全渠道共享敏感个人数据，且对跨司法管辖区所需的文书手续缺乏信任。Gani 承认在资金到账前宣布消息是个错误，但他强调项目的目标依然保持不变。

尽管遭遇财务挫折，首要目标仍是在年底前发布 PocketBase 的稳定版本。目前的开发重点是重写 UI，旨在实现控制面板的自定义和可扩展性（插件）。

为了确保长期可维护性并避免复杂的构建依赖，Gani 正从 Svelte 转向 **Shablon**——这是一个使用纯 JavaScript 编写的自定义零依赖框架。Shablon 采用原生 DOM 元素和简单的响应式模型，允许用户在无需 Node.js 构建步骤的情况下扩展 UI。这符合 Gani 将 PocketBase 打造为一个外部依赖极少的“完整”项目的愿景。

在 UI 重写和新 UI 工具包开发期间，PocketBase 已进入临时的“功能冻结”阶段。由于失去了预期的全职开发资金，Gani 请求社区在处理这些变化期间保持耐心。

---

## 7. Weave (YC W25) 正在招聘机器学习、设计和产品工程师

**原文标题**: Weave (YC W25) Is Hiring ML, Design, and Product Engineers

**原文链接**: [https://jobs.ashbyhq.com/workweave](https://jobs.ashbyhq.com/workweave)

根据所提供的信息，以下是简要总结：

**Weave** 是一家入选 **Y Combinator 2025 冬季（YC W25）** 营的初创公司，目前正在为其技术团队招聘人才。

该公司主要招聘以下三个职位的候选人：
*   **机器学习 (ML) 工程师**
*   **设计工程师**
*   **产品工程师**

作为一家 YC W25 入选公司，Weave 正处于早期成长阶段，正在寻找能够助力构建核心产品并开发其机器学习能力的工程师。虽然具体的职位详情需访问其招聘页面查看，但其招聘重点表明该公司正采取一种将前沿 AI 开发与以用户为中心的产品设计相结合的多学科方法。

---

## 8. Windows：优先使用原生 API 而非 Win32

**原文标题**: Windows: Prefer the Native API over Win32

**原文链接**: [https://codeberg.org/ziglang/zig/issues/31131](https://codeberg.org/ziglang/zig/issues/31131)

在这个 Zig 项目议题中，创始人 Andrew Kelley 提议对 Zig 标准库与 Windows 的交互方式进行根本性的转变：优先采用 **Windows Native API (`ntdll.dll`)**，而非传统的 **Win32 API（`kernel32.dll`、`advapi32.dll` 等）**。

该提议概述了这一转变的几个关键动机：

*   **减少开销：** 大多数 Win32 函数仅仅是 Native API 调用的封装。直接与 `ntdll` 交互消除了不必要的间接层，从而有望提升性能并减小二进制文件体积。
*   **技术精准度：** Native API 提供了更细粒度的控制，并允许访问有时被 Win32 子系统掩盖或限制的功能。这包括对 NT 风格路径（以 `\??\` 开头）更好的处理以及更稳健的文件系统操作。
*   **最小化依赖：** 通过面向用户模式层级的最底层，Zig 二进制文件对高级子系统 DLL 的依赖程度降低。这使得 Zig 代码能够在 Win32 子系统不可用或尚未初始化的环境中运行，例如系统早期启动过程或专门的“原生 (Native)”应用程序。
*   **一致性：** 此次转变旨在让 Zig 标准库的 Windows 实现更具“原则性”，将 NT 内核视为主要目标，而非将其视为一个遗留子系统。

该议题承认，虽然 Native API 在技术上属于“未公开”接口且微软可能会对其进行改动，但其核心功能在过去几十年中一直保持着极高的稳定性。该计划涉及重构 Zig 标准库，利用 `ntdll` 处理内存管理、文件 I/O 和线程调度等核心操作系统任务，仅在需要特定的高级功能时才使用 Win32。这一举措符合 Zig 提供底层控制并避免隐藏抽象的哲学。

---

## 9. Terminals should generate the 256-color palette

**原文标题**: Terminals should generate the 256-color palette

**原文链接**: [https://gist.github.com/jake-stewart/0a8ea46159a7da2c808e5be2177e1783](https://gist.github.com/jake-stewart/0a8ea46159a7da2c808e5be2177e1783)

生成摘要时出错

---

## 10. Cistercian Numbers

**原文标题**: Cistercian Numbers

**原文链接**: [https://www.omniglot.com/language/numbers/cistercian-numbers.htm](https://www.omniglot.com/language/numbers/cistercian-numbers.htm)

生成摘要时出错

---

## 11. Show HN: CEL by Example

**原文标题**: Show HN: CEL by Example

**原文链接**: [https://celbyexample.com/](https://celbyexample.com/)

生成摘要时出错

---

## 12. Show HN: Formally verified FPGA watchdog for AM broadcast in unmanned tunnels

**原文标题**: Show HN: Formally verified FPGA watchdog for AM broadcast in unmanned tunnels

**原文链接**: [https://github.com/Park07/amradio](https://github.com/Park07/amradio)

生成摘要时出错

---

## 13. Native FreeBSD Kerberos/LDAP with FreeIPA/IDM

**原文标题**: Native FreeBSD Kerberos/LDAP with FreeIPA/IDM

**原文链接**: [https://vermaden.wordpress.com/2026/02/18/native-freebsd-kerberos-ldap-with-freeipa-idm/](https://vermaden.wordpress.com/2026/02/18/native-freebsd-kerberos-ldap-with-freeipa-idm/)

生成摘要时出错

---

## 14. AVX2 is slower than SSE2-4.x under Windows ARM emulation

**原文标题**: AVX2 is slower than SSE2-4.x under Windows ARM emulation

**原文链接**: [https://blogs.remobjects.com/2026/02/17/nerdsniped-windows-arm-emulation-performance/](https://blogs.remobjects.com/2026/02/17/nerdsniped-windows-arm-emulation-performance/)

生成摘要时出错

---

## 15. Unprecedented 'Jobless Boom' Tests Limits of US Economic Expansion

**原文标题**: Unprecedented 'Jobless Boom' Tests Limits of US Economic Expansion

**原文链接**: [https://www.bloomberg.com/news/features/2026-02-18/us-economy-expansion-forecast-even-with-weak-jobs-data](https://www.bloomberg.com/news/features/2026-02-18/us-economy-expansion-forecast-even-with-weak-jobs-data)

生成摘要时出错

---

## 16. The only moat left is money?

**原文标题**: The only moat left is money?

**原文链接**: [https://elliotbonneville.com/the-only-moat-left-is-money/](https://elliotbonneville.com/the-only-moat-left-is-money/)

生成摘要时出错

---

## 17. The Future of AI Software Development

**原文标题**: The Future of AI Software Development

**原文链接**: [https://martinfowler.com/fragments/2026-02-18.html](https://martinfowler.com/fragments/2026-02-18.html)

生成摘要时出错

---

## 18. Fastest Front End Tooling for Humans and AI

**原文标题**: Fastest Front End Tooling for Humans and AI

**原文链接**: [https://cpojer.net/posts/fastest-frontend-tooling](https://cpojer.net/posts/fastest-frontend-tooling)

生成摘要时出错

---

## 19. The true history of the Minotaur: what archaeology reveals

**原文标题**: The true history of the Minotaur: what archaeology reveals

**原文链接**: [https://www.nationalgeographic.fr/histoire/la-veritable-histoire-du-minotaure-ce-que-revele-archeologie-recherche-verification](https://www.nationalgeographic.fr/histoire/la-veritable-histoire-du-minotaure-ce-que-revele-archeologie-recherche-verification)

生成摘要时出错

---

## 20. Show HN: I'm launching a LPFM radio station

**原文标题**: Show HN: I'm launching a LPFM radio station

**原文链接**: [https://www.kpbj.fm/](https://www.kpbj.fm/)

生成摘要时出错

---

## 21. Show HN: Trust Protocols for Anthropic/OpenAI/Gemini

**原文标题**: Show HN: Trust Protocols for Anthropic/OpenAI/Gemini

**原文链接**: [https://www.mnemom.ai](https://www.mnemom.ai)

生成摘要时出错

---

## 22. Asahi Linux Progress Report: Linux 6.19

**原文标题**: Asahi Linux Progress Report: Linux 6.19

**原文链接**: [https://asahilinux.org/2026/02/progress-report-6-19/](https://asahilinux.org/2026/02/progress-report-6-19/)

生成摘要时出错

---

## 23. Chained Assignment in Python Bytecode

**原文标题**: Chained Assignment in Python Bytecode

**原文链接**: [https://loriculus.org/blog/python-chained-assignment/](https://loriculus.org/blog/python-chained-assignment/)

生成摘要时出错

---

## 24. Microsoft says bug causes Copilot to summarize confidential emails

**原文标题**: Microsoft says bug causes Copilot to summarize confidential emails

**原文链接**: [https://www.bleepingcomputer.com/news/microsoft/microsoft-says-bug-causes-copilot-to-summarize-confidential-emails/](https://www.bleepingcomputer.com/news/microsoft/microsoft-says-bug-causes-copilot-to-summarize-confidential-emails/)

生成摘要时出错

---

## 25. A DuckDB-based metabase alternative

**原文标题**: A DuckDB-based metabase alternative

**原文链接**: [https://github.com/taleshape-com/shaper](https://github.com/taleshape-com/shaper)

生成摘要时出错

---

## 26. Arizona Bill Requires Age Verification for All Apps

**原文标题**: Arizona Bill Requires Age Verification for All Apps

**原文链接**: [https://reclaimthenet.org/arizona-bill-would-require-id-checks-to-use-a-weather-app](https://reclaimthenet.org/arizona-bill-would-require-id-checks-to-use-a-weather-app)

生成摘要时出错

---

## 27. Show HN: AsteroidOS 2.0 – Nobody asked, we shipped anyway

**原文标题**: Show HN: AsteroidOS 2.0 – Nobody asked, we shipped anyway

**原文链接**: [https://asteroidos.org/news/2-0-release/index.html](https://asteroidos.org/news/2-0-release/index.html)

生成摘要时出错

---

## 28. 15 years later, Microsoft morged my diagram

**原文标题**: 15 years later, Microsoft morged my diagram

**原文链接**: [https://nvie.com/posts/15-years-later/](https://nvie.com/posts/15-years-later/)

生成摘要时出错

---

## 29. TinyIce: Single-binary Icecast2-compatible server (auto-HTTPS, multi-tenant)

**原文标题**: TinyIce: Single-binary Icecast2-compatible server (auto-HTTPS, multi-tenant)

**原文链接**: [https://github.com/DatanoiseTV/tinyice](https://github.com/DatanoiseTV/tinyice)

生成摘要时出错

---

## 30. Claude Sonnet 4.6

**原文标题**: Claude Sonnet 4.6

**原文链接**: [https://www.anthropic.com/news/claude-sonnet-4-6](https://www.anthropic.com/news/claude-sonnet-4-6)

生成摘要时出错

---

## 31. Arizona Bill Requires Age Verification for All Apps

**原文标题**: Arizona Bill Requires Age Verification for All Apps

**原文链接**: [https://reclaimthenet.org/arizona-bill-would-require-id-checks-to-use-a-weather-app](https://reclaimthenet.org/arizona-bill-would-require-id-checks-to-use-a-weather-app)

生成摘要时出错

---

## 32. Halt and Catch Fire: TV’s best drama you’ve probably never heard of (2021)

**原文标题**: Halt and Catch Fire: TV’s best drama you’ve probably never heard of (2021)

**原文链接**: [https://www.sceneandheardnu.com/content/halt-and-catch-fire](https://www.sceneandheardnu.com/content/halt-and-catch-fire)

生成摘要时出错

---

## 33. Thousands of CEOs just admitted AI had no impact on employment or productivity

**原文标题**: Thousands of CEOs just admitted AI had no impact on employment or productivity

**原文链接**: [https://fortune.com/2026/02/17/ai-productivity-paradox-ceo-study-robert-solow-information-technology-age/](https://fortune.com/2026/02/17/ai-productivity-paradox-ceo-study-robert-solow-information-technology-age/)

生成摘要时出错

---

## 34. Elvish as She Is Spoke [pdf]

**原文标题**: Elvish as She Is Spoke [pdf]

**原文链接**: [https://www.elvish.org/articles/EASIS.pdf](https://www.elvish.org/articles/EASIS.pdf)

生成摘要时出错

---

## 35. Reverse Engineering Sid Meier's Railroad Tycoon for DOS from 1990

**原文标题**: Reverse Engineering Sid Meier's Railroad Tycoon for DOS from 1990

**原文链接**: [https://www.vogons.org/viewtopic.php?t=105451](https://www.vogons.org/viewtopic.php?t=105451)

生成摘要时出错

---

## 36. Show HN: Open Notes – Community Notes-style context for Discord

**原文标题**: Show HN: Open Notes – Community Notes-style context for Discord

**原文链接**: [https://opennotes.ai/discord-bot](https://opennotes.ai/discord-bot)

生成摘要时出错

---

## 37. Breccia: Single-file, append-only, blob storage with efficient random access

**原文标题**: Breccia: Single-file, append-only, blob storage with efficient random access

**原文链接**: [https://github.com/petertodd/breccia/blob/master/DESIGN.md](https://github.com/petertodd/breccia/blob/master/DESIGN.md)

生成摘要时出错

---

## 38. Fei-Fei Li's World Labs raised $1B from A16Z, Nvidia to advance its world models

**原文标题**: Fei-Fei Li's World Labs raised $1B from A16Z, Nvidia to advance its world models

**原文链接**: [https://www.bloomberg.com/news/articles/2026-02-18/ai-pioneer-fei-fei-li-s-startup-world-labs-raises-1-billion](https://www.bloomberg.com/news/articles/2026-02-18/ai-pioneer-fei-fei-li-s-startup-world-labs-raises-1-billion)

生成摘要时出错

---

## 39. Show HN: Breadboard – A modern HyperCard for building web apps on the canvas

**原文标题**: Show HN: Breadboard – A modern HyperCard for building web apps on the canvas

**原文链接**: [https://breadboards.io/](https://breadboards.io/)

生成摘要时出错

---

## 40. Vinyl Cache has left GitHub

**原文标题**: Vinyl Cache has left GitHub

**原文链接**: [https://vinyl-cache.org/organization/moving.html](https://vinyl-cache.org/organization/moving.html)

生成摘要时出错

---

## 41. HackMyClaw

**原文标题**: HackMyClaw

**原文链接**: [https://hackmyclaw.com/](https://hackmyclaw.com/)

生成摘要时出错

---

## 42. In Argentina, locals are taking loans to buy food

**原文标题**: In Argentina, locals are taking loans to buy food

**原文链接**: [https://www.aljazeera.com/economy/2026/2/16/in-argentina-locals-are-taking-loans-to-buy-food](https://www.aljazeera.com/economy/2026/2/16/in-argentina-locals-are-taking-loans-to-buy-food)

生成摘要时出错

---

## 43. So you want to build a tunnel

**原文标题**: So you want to build a tunnel

**原文链接**: [https://practical.engineering/blog/2026/2/17/so-you-want-to-build-a-tunnel](https://practical.engineering/blog/2026/2/17/so-you-want-to-build-a-tunnel)

生成摘要时出错

---

## 44. Minimal x86 Kernel Zig

**原文标题**: Minimal x86 Kernel Zig

**原文链接**: [https://github.com/lopespm/zig-minimal-kernel-x86](https://github.com/lopespm/zig-minimal-kernel-x86)

生成摘要时出错

---

## 45. Tesla announces Powerwall 3P with native three-phase inverter

**原文标题**: Tesla announces Powerwall 3P with native three-phase inverter

**原文链接**: [https://electrek.co/2026/02/13/tesla-announces-powerwall-3p-with-native-three-phase-inverter/](https://electrek.co/2026/02/13/tesla-announces-powerwall-3p-with-native-three-phase-inverter/)

生成摘要时出错

---

## 46. No food, no fuel, no tourists: Under US pressure, life in Cuba grinds to a halt

**原文标题**: No food, no fuel, no tourists: Under US pressure, life in Cuba grinds to a halt

**原文链接**: [https://www.cnn.com/2026/02/18/americas/cuba-us-trump-oil-tourism-intl-latam](https://www.cnn.com/2026/02/18/americas/cuba-us-trump-oil-tourism-intl-latam)

生成摘要时出错

---

## 47. BarraCUDA Open-source CUDA compiler targeting AMD GPUs

**原文标题**: BarraCUDA Open-source CUDA compiler targeting AMD GPUs

**原文链接**: [https://github.com/Zaneham/BarraCUDA](https://github.com/Zaneham/BarraCUDA)

生成摘要时出错

---

## 48. Async/Await on the GPU

**原文标题**: Async/Await on the GPU

**原文链接**: [https://www.vectorware.com/blog/async-await-on-gpu/](https://www.vectorware.com/blog/async-await-on-gpu/)

生成摘要时出错

---

## 49. Meta's Zuckerberg faces questioning at youth addiction trial

**原文标题**: Meta's Zuckerberg faces questioning at youth addiction trial

**原文链接**: [https://www.reuters.com/sustainability/society-equity/metas-zuckerberg-faces-questioning-youth-addiction-trial-2026-02-18/](https://www.reuters.com/sustainability/society-equity/metas-zuckerberg-faces-questioning-youth-addiction-trial-2026-02-18/)

生成摘要时出错

---

## 50. How I use Obsidian (2023)

**原文标题**: How I use Obsidian (2023)

**原文链接**: [https://stephango.com/vault](https://stephango.com/vault)

生成摘要时出错

---

## 51. Show HN: Bubble sort on a Turing machine

**原文标题**: Show HN: Bubble sort on a Turing machine

**原文链接**: [https://github.com/purplejacket/bubble_sort_on_tm](https://github.com/purplejacket/bubble_sort_on_tm)

生成摘要时出错

---

## 52. Rathbun's Operator

**原文标题**: Rathbun's Operator

**原文链接**: [https://crabby-rathbun.github.io/mjrathbun-website/blog/posts/rathbuns-operator.html](https://crabby-rathbun.github.io/mjrathbun-website/blog/posts/rathbuns-operator.html)

生成摘要时出错

---

## 53. Semantic Diffusion (2006)

**原文标题**: Semantic Diffusion (2006)

**原文链接**: [https://martinfowler.com/bliki/SemanticDiffusion.html](https://martinfowler.com/bliki/SemanticDiffusion.html)

生成摘要时出错

---

## 54. Pixel 10a

**原文标题**: Pixel 10a

**原文链接**: [https://store.google.com/us/product/pixel_10a?hl=en-US](https://store.google.com/us/product/pixel_10a?hl=en-US)

生成摘要时出错

---

## 55. Can a Computer Science Student Be Taught to Design Hardware?

**原文标题**: Can a Computer Science Student Be Taught to Design Hardware?

**原文链接**: [https://semiengineering.com/can-a-computer-science-student-be-taught-to-design-hardware/](https://semiengineering.com/can-a-computer-science-student-be-taught-to-design-hardware/)

生成摘要时出错

---

## 56. Portugal: The First Global Empire

**原文标题**: Portugal: The First Global Empire

**原文链接**: [https://www.historytoday.com/archive/first-global-empire](https://www.historytoday.com/archive/first-global-empire)

生成摘要时出错

---

## 57. How LLM agents endanger open-source projects

**原文标题**: How LLM agents endanger open-source projects

**原文链接**: [https://cusy.io/en/blog/how-llm-agents-endanger-open-source-projects.html](https://cusy.io/en/blog/how-llm-agents-endanger-open-source-projects.html)

生成摘要时出错

---

## 58. The Worst-Case Future for White-Collar Workers

**原文标题**: The Worst-Case Future for White-Collar Workers

**原文链接**: [https://www.theatlantic.com/ideas/2026/02/ai-white-collar-jobs/686031/](https://www.theatlantic.com/ideas/2026/02/ai-white-collar-jobs/686031/)

生成摘要时出错

---

## 59. Mark Zuckerberg Lied to Congress. We Can't Trust His Testimony

**原文标题**: Mark Zuckerberg Lied to Congress. We Can't Trust His Testimony

**原文链接**: [https://dispatch.techoversight.org/top-report-mark-zuckerberg-lied-to-congress-we-cant-trust-his-testimony/](https://dispatch.techoversight.org/top-report-mark-zuckerberg-lied-to-congress-we-cant-trust-his-testimony/)

生成摘要时出错

---

## 60. In Search of a Discord Replacement

**原文标题**: In Search of a Discord Replacement

**原文链接**: [https://no-bull.sh/blog/2026/02/16/in-search-of-a-discord-replacement/](https://no-bull.sh/blog/2026/02/16/in-search-of-a-discord-replacement/)

生成摘要时出错

---

## 61. 'My Words Are Like an Uncontrollable Dog': On Life with Nonfluent Aphasia (2025)

**原文标题**: 'My Words Are Like an Uncontrollable Dog': On Life with Nonfluent Aphasia (2025)

**原文链接**: [https://thereader.mitpress.mit.edu/my-words-are-like-an-uncontrollable-dog-on-life-with-nonfluent-aphasia/](https://thereader.mitpress.mit.edu/my-words-are-like-an-uncontrollable-dog-on-life-with-nonfluent-aphasia/)

生成摘要时出错

---

## 62. The Secret Life of Vector Generators (2001)

**原文标题**: The Secret Life of Vector Generators (2001)

**原文链接**: [https://jmargolin.com/vgens/vgens.htm](https://jmargolin.com/vgens/vgens.htm)

生成摘要时出错

---

## 63. Google Public CA is down

**原文标题**: Google Public CA is down

**原文链接**: [https://status.pki.goog/incidents/5oJEbcU3ZfMfySTSXXd3](https://status.pki.goog/incidents/5oJEbcU3ZfMfySTSXXd3)

生成摘要时出错

---

## 64. Gentoo on Codeberg

**原文标题**: Gentoo on Codeberg

**原文链接**: [https://www.gentoo.org/news/2026/02/16/codeberg.html](https://www.gentoo.org/news/2026/02/16/codeberg.html)

生成摘要时出错

---

## 65. AI-generated password isn't random, it just looks that way

**原文标题**: AI-generated password isn't random, it just looks that way

**原文链接**: [https://www.theregister.com/2026/02/18/generating_passwords_with_llms/](https://www.theregister.com/2026/02/18/generating_passwords_with_llms/)

生成摘要时出错

---

## 66. Assistant to the Regional Manager

**原文标题**: Assistant to the Regional Manager

**原文链接**: [https://smallpotatoes.paulbloom.net/p/assistant-to-the-regional-manager](https://smallpotatoes.paulbloom.net/p/assistant-to-the-regional-manager)

生成摘要时出错

---

## 67. Physicists Make Electrons Flow Like Water

**原文标题**: Physicists Make Electrons Flow Like Water

**原文链接**: [https://www.quantamagazine.org/physicists-make-electrons-flow-like-water-20260211/](https://www.quantamagazine.org/physicists-make-electrons-flow-like-water-20260211/)

生成摘要时出错

---

## 68. I swear the UFO is coming any minute

**原文标题**: I swear the UFO is coming any minute

**原文链接**: [https://www.experimental-history.com/p/i-swear-the-ufo-is-coming-any-minute](https://www.experimental-history.com/p/i-swear-the-ufo-is-coming-any-minute)

生成摘要时出错

---

## 69. Plasma 6.6

**原文标题**: Plasma 6.6

**原文链接**: [https://kde.org/announcements/plasma/6/6.6.0/](https://kde.org/announcements/plasma/6/6.6.0/)

生成摘要时出错

---

## 70. Use Microsoft Office Shortcuts in Libre Office

**原文标题**: Use Microsoft Office Shortcuts in Libre Office

**原文链接**: [https://github.com/Zaki101Aslam/MS-office-shortcuts-for-Libre-Office](https://github.com/Zaki101Aslam/MS-office-shortcuts-for-Libre-Office)

生成摘要时出错

---

## 71. The Economics of a Super Bowl Ad

**原文标题**: The Economics of a Super Bowl Ad

**原文链接**: [https://ro.co/perspectives/super-bowl-economics/](https://ro.co/perspectives/super-bowl-economics/)

生成摘要时出错

---

## 72. Show HN: Pg-typesafe – Strongly typed queries for PostgreSQL and TypeScript

**原文标题**: Show HN: Pg-typesafe – Strongly typed queries for PostgreSQL and TypeScript

**原文链接**: [https://github.com/n-e/pg-typesafe](https://github.com/n-e/pg-typesafe)

生成摘要时出错

---

## 73. Using go fix to modernize Go code

**原文标题**: Using go fix to modernize Go code

**原文链接**: [https://go.dev/blog/gofix](https://go.dev/blog/gofix)

生成摘要时出错

---

## 74. Show HN: I Made a Programming Language with Python Syntax, zero-copy and C-Speed

**原文标题**: Show HN: I Made a Programming Language with Python Syntax, zero-copy and C-Speed

**原文链接**: [https://github.com/CrimsonDemon567PC/Mantis](https://github.com/CrimsonDemon567PC/Mantis)

生成摘要时出错

---

## 75. Show HN: I taught LLMs to play Magic: The Gathering against each other

**原文标题**: Show HN: I taught LLMs to play Magic: The Gathering against each other

**原文链接**: [https://mage-bench.com/](https://mage-bench.com/)

生成摘要时出错

---

## 76. 14-year-old Miles Wu folded origami pattern that holds 10k times its own weight

**原文标题**: 14-year-old Miles Wu folded origami pattern that holds 10k times its own weight

**原文链接**: [https://www.smithsonianmag.com/innovation/this-14-year-old-is-using-origami-to-design-emergency-shelters-that-are-sturdy-cost-efficient-and-easy-to-deploy-180988179/](https://www.smithsonianmag.com/innovation/this-14-year-old-is-using-origami-to-design-emergency-shelters-that-are-sturdy-cost-efficient-and-easy-to-deploy-180988179/)

生成摘要时出错

---

## 77. Show HN: I built a "Socratic" AI to stop my daughter from copy-pasting homework

**原文标题**: Show HN: I built a "Socratic" AI to stop my daughter from copy-pasting homework

**原文链接**: [https://thinkqurio.com/](https://thinkqurio.com/)

生成摘要时出错

---

## 78. Lyria 3

**原文标题**: Lyria 3

**原文链接**: [https://deepmind.google/models/lyria/](https://deepmind.google/models/lyria/)

生成摘要时出错

---

## 79. Advice, not control: the role of Remote Assistance in Waymo's operations

**原文标题**: Advice, not control: the role of Remote Assistance in Waymo's operations

**原文链接**: [https://waymo.com/blog/?modal=short-advice-not-control-the-role-of-remote-assistance](https://waymo.com/blog/?modal=short-advice-not-control-the-role-of-remote-assistance)

生成摘要时出错

---

## 80. Is Show HN dead? No, but it's drowning

**原文标题**: Is Show HN dead? No, but it's drowning

**原文链接**: [https://www.arthurcnops.blog/death-of-show-hn/](https://www.arthurcnops.blog/death-of-show-hn/)

生成摘要时出错

---

## 81. Impact of the "when the fun stops, stop" gambling message on online gambling

**原文标题**: Impact of the "when the fun stops, stop" gambling message on online gambling

**原文链接**: [https://www.thelancet.com/journals/lanpub/article/PIIS2468-2667(21)00279-6/fulltext](https://www.thelancet.com/journals/lanpub/article/PIIS2468-2667(21)00279-6/fulltext)

生成摘要时出错

---

## 82. Sub-Millisecond RAG on Apple Silicon. No Server. No API. One File

**原文标题**: Sub-Millisecond RAG on Apple Silicon. No Server. No API. One File

**原文链接**: [https://github.com/christopherkarani/Wax](https://github.com/christopherkarani/Wax)

生成摘要时出错

---

## 83. Contra "Grandmaster-level chess without search" (2024)

**原文标题**: Contra "Grandmaster-level chess without search" (2024)

**原文链接**: [https://cosmo.tardis.ac/files/2024-02-13-searchless.html](https://cosmo.tardis.ac/files/2024-02-13-searchless.html)

生成摘要时出错

---

## 84. "Token anxiety", a slot machine by any other name

**原文标题**: "Token anxiety", a slot machine by any other name

**原文链接**: [https://jkap.io/token-anxiety-or-a-slot-machine-by-any-other-name/](https://jkap.io/token-anxiety-or-a-slot-machine-by-any-other-name/)

生成摘要时出错

---

## 85. Tesla Sales Down 55% UK, 58% Spain, 59% Germany, 81% Netherlands, 93% Norway

**原文标题**: Tesla Sales Down 55% UK, 58% Spain, 59% Germany, 81% Netherlands, 93% Norway

**原文链接**: [https://cleantechnica.com/2026/02/15/tesla-sales-down-tremendously-in-uk-norway-netherlands-germany-spain-sweden-denmark-portugal-switzerland/](https://cleantechnica.com/2026/02/15/tesla-sales-down-tremendously-in-uk-norway-netherlands-germany-spain-sweden-denmark-portugal-switzerland/)

生成摘要时出错

---

## 86. Nobody knows what programming will look like in two years

**原文标题**: Nobody knows what programming will look like in two years

**原文链接**: [https://leaddev.com/ai/nobody-knows-what-programming-will-look-like-in-two-years](https://leaddev.com/ai/nobody-knows-what-programming-will-look-like-in-two-years)

生成摘要时出错

---

## 87. GrapheneOS – Break Free from Google and Apple

**原文标题**: GrapheneOS – Break Free from Google and Apple

**原文链接**: [https://blog.tomaszdunia.pl/grapheneos-eng/](https://blog.tomaszdunia.pl/grapheneos-eng/)

生成摘要时出错

---

## 88. Xbox UI Portfolio Site

**原文标题**: Xbox UI Portfolio Site

**原文链接**: [https://gabrielcabrera.co/](https://gabrielcabrera.co/)

生成摘要时出错

---

## 89. Show HN: I wrote a technical history book on Lisp

**原文标题**: Show HN: I wrote a technical history book on Lisp

**原文链接**: [https://berksoft.ca/gol/](https://berksoft.ca/gol/)

生成摘要时出错

---

## 90. Discord Rival Gets Overwhelmed by Exodus of Players Fleeing Age-Verification

**原文标题**: Discord Rival Gets Overwhelmed by Exodus of Players Fleeing Age-Verification

**原文链接**: [https://kotaku.com/discord-alternative-teamspeak-age-verification-check-rivals-2000669693](https://kotaku.com/discord-alternative-teamspeak-age-verification-check-rivals-2000669693)

生成摘要时出错

---

## 91. Show HN: Glitchy camera – a circuit-bent camera simulator in the browser

**原文标题**: Show HN: Glitchy camera – a circuit-bent camera simulator in the browser

**原文链接**: [https://glitchycam.com](https://glitchycam.com)

生成摘要时出错

---

## 92. Java.evolved: Java has evolved. Your code can too

**原文标题**: Java.evolved: Java has evolved. Your code can too

**原文链接**: [https://javaevolved.github.io](https://javaevolved.github.io)

生成摘要时出错

---

## 93. Hamming Distance for Hybrid Search in SQLite

**原文标题**: Hamming Distance for Hybrid Search in SQLite

**原文链接**: [https://notnotp.com/notes/hamming-distance-for-hybrid-search-in-sqlite/](https://notnotp.com/notes/hamming-distance-for-hybrid-search-in-sqlite/)

生成摘要时出错

---

## 94. Quamina and Claude, Case 1

**原文标题**: Quamina and Claude, Case 1

**原文链接**: [https://www.tbray.org/ongoing/When/202x/2026/02/06/Q-Plus-C-Ch1](https://www.tbray.org/ongoing/When/202x/2026/02/06/Q-Plus-C-Ch1)

生成摘要时出错

---

## 95. The case for gatekeeping, or: why medieval guilds had it figured out

**原文标题**: The case for gatekeeping, or: why medieval guilds had it figured out

**原文链接**: [https://www.joanwestenberg.com/the-case-for-gatekeeping-or-why-medieval-guilds-had-it-figured-out/](https://www.joanwestenberg.com/the-case-for-gatekeeping-or-why-medieval-guilds-had-it-figured-out/)

生成摘要时出错

---

## 96. Show HN: Free printable micro-habit tracker inspired by Atomic Habits

**原文标题**: Show HN: Free printable micro-habit tracker inspired by Atomic Habits

**原文链接**: [https://atomichabits-calendar.com](https://atomichabits-calendar.com)

生成摘要时出错

---

## 97. Rendering the Visible Spectrum

**原文标题**: Rendering the Visible Spectrum

**原文链接**: [https://brandonli.net/spectra/doc/](https://brandonli.net/spectra/doc/)

生成摘要时出错

---

## 98. What's a "gig work minimum wage"

**原文标题**: What's a "gig work minimum wage"

**原文链接**: [https://pluralistic.net/2026/02/17/no-piecework/](https://pluralistic.net/2026/02/17/no-piecework/)

生成摘要时出错

---

## 99. I converted 2D conventional flight tracking into 3D

**原文标题**: I converted 2D conventional flight tracking into 3D

**原文链接**: [https://aeris.edbn.me/?city=SFO](https://aeris.edbn.me/?city=SFO)

生成摘要时出错

---

## 100. Approaches to writing two-sentence journal entries

**原文标题**: Approaches to writing two-sentence journal entries

**原文链接**: [https://alexanderbjoy.com/two-sentence-journal-approaches/](https://alexanderbjoy.com/two-sentence-journal-approaches/)

生成摘要时出错

---

