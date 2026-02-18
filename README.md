# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-02-18.md)

*最后自动更新时间: 2026-02-18 18:19:44*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 2 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 3 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 4 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 5 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 6 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 7 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 8 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 9 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 10 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 11 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 12 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 13 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 14 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 15 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 16 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 17 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 18 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 19 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 20 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 21 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 22 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 23 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 24 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 25 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 26 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 27 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 28 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 29 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 30 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 31 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 32 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 33 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 34 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 35 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 36 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 37 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 38 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 39 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 40 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 41 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 42 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 43 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 44 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 45 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 46 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 47 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 48 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 49 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 50 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 51 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 52 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 53 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 54 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 55 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 56 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 57 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 58 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 59 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 60 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 61 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 62 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 63 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 64 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 65 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 66 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 67 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 68 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 69 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 70 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 71 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 72 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 73 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 74 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 75 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 76 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 77 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 78 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 79 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 80 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 81 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 82 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 83 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 84 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 85 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 86 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 87 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 88 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 89 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 90 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 91 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 92 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 93 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 94 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 95 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 96 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 97 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 98 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 99 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 100 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 101 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 102 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 103 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 104 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 105 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 106 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 107 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 108 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 109 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 110 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 111 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 112 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 113 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 114 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 115 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 116 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 117 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 118 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 119 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 120 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 121 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 122 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 123 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 124 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 125 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 126 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 127 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 128 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 129 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 130 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 131 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 132 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 133 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 134 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 135 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 136 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 137 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 138 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 139 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 140 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 141 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 142 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 143 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 144 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 145 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 146 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 147 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 148 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 149 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 150 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 151 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 152 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 153 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 154 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 155 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 156 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 157 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 158 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 159 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 160 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 161 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 162 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 163 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 164 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 165 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 166 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 167 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 168 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 169 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 170 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 171 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 172 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 173 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 174 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 175 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 176 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 177 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 178 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 179 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 180 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 181 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 182 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 183 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 184 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 185 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 186 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 187 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 188 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 189 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 190 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 191 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 192 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 193 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 194 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 195 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 196 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 197 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 198 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 199 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 200 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 201 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 202 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 203 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 204 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 205 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 206 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 207 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 208 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 209 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 210 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 211 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 212 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 213 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 214 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 215 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 216 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 217 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 218 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 219 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 220 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 221 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 222 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 223 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 224 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 225 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 226 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 227 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 228 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 229 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 230 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 231 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 232 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 233 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 234 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 235 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 236 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 237 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 238 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 239 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 240 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 241 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 242 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 243 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 244 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 245 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 246 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 247 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 248 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 249 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 250 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 251 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 252 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 253 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 254 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 255 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 256 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 257 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 258 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 259 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 260 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 261 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 262 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 263 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 264 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 265 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 266 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 267 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 268 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 269 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 270 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 271 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 272 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 273 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 274 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 275 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 276 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 277 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 278 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 279 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 280 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 281 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 282 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 283 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 284 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 285 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 286 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 287 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 288 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 289 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 290 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 291 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 292 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 293 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 294 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 295 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 296 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 297 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 298 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 299 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 300 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 301 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 302 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 303 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 304 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 305 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 306 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 307 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 308 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 309 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 310 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 311 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 312 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 313 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 314 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 315 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 316 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 317 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 318 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 319 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 320 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 321 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 322 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 323 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 324 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 325 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 326 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 327 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 328 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 329 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 330 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 331 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 332 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 333 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 334 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 335 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
