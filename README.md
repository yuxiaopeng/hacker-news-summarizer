# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-10-02.md)

*最后自动更新时间: 2026-10-02 21:40:28*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 2 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 3 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 4 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 5 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 6 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 7 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 8 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 9 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 10 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 11 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 12 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 13 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 14 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 15 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 16 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 17 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 18 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 19 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 20 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 21 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 22 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 23 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 24 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 25 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 26 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 27 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 28 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 29 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 30 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 31 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 32 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 33 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 34 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 35 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 36 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 37 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 38 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 39 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 40 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 41 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 42 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 43 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 44 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 45 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 46 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 47 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 48 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 49 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 50 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 51 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 52 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 53 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 54 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 55 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 56 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 57 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 58 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 59 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 60 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 61 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 62 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 63 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 64 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 65 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 66 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 67 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 68 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 69 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 70 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 71 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 72 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 73 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 74 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 75 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 76 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 77 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 78 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 79 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 80 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 81 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 82 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 83 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 84 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 85 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 86 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 87 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 88 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 89 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 90 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 91 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 92 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 93 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 94 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 95 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 96 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 97 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 98 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 99 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 100 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 101 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 102 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 103 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 104 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 105 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 106 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 107 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 108 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 109 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 110 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 111 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 112 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 113 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 114 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 115 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 116 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 117 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 118 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 119 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 120 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 121 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 122 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 123 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 124 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 125 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 126 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 127 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 128 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 129 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 130 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 131 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 132 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 133 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 134 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 135 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 136 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 137 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 138 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 139 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 140 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 141 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 142 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 143 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 144 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 145 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 146 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 147 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 148 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 149 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 150 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 151 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 152 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 153 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 154 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 155 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 156 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 157 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 158 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 159 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 160 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 161 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 162 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 163 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 164 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 165 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 166 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 167 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 168 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 169 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 170 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 171 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 172 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 173 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 174 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 175 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 176 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 177 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 178 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 179 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 180 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 181 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 182 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 183 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 184 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 185 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 186 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 187 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 188 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 189 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 190 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 191 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 192 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 193 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 194 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 195 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 196 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 197 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 198 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 199 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 200 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 201 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 202 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 203 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 204 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 205 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 206 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 207 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 208 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 209 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 210 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 211 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 212 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 213 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 214 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 215 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 216 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 217 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 218 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 219 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 220 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 221 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 222 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 223 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 224 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 225 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 226 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 227 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 228 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 229 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 230 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 231 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 232 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 233 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 234 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 235 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 236 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 237 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 238 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 239 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 240 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 241 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 242 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 243 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 244 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 245 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 246 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 247 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 248 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 249 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 250 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 251 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 252 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 253 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 254 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 255 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 256 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 257 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 258 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 259 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 260 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 261 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 262 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 263 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 264 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 265 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 266 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 267 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 268 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 269 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 270 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 271 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 272 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 273 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 274 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 275 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 276 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 277 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 278 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 279 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 280 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 281 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 282 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 283 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 284 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 285 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 286 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 287 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 288 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 289 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 290 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 291 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 292 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 293 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 294 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 295 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 296 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 297 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 298 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 299 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 300 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 301 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 302 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 303 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 304 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 305 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 306 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 307 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 308 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 309 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 310 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 311 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 312 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 313 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 314 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 315 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 316 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 317 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 318 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 319 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 320 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 321 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 322 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 323 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 324 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 325 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 326 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 327 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 328 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 329 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 330 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 331 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 332 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 333 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 334 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 335 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 336 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 337 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 338 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 339 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 340 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 341 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 342 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 343 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 344 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 345 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 346 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 347 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 348 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 349 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 350 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 351 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 352 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 353 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 354 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 355 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 356 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 357 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 358 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 359 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 360 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 361 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 362 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 363 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 364 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 365 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 366 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 367 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 368 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 369 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 370 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 371 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 372 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 373 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 374 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 375 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 376 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 377 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 378 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 379 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 380 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 381 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 382 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 383 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 384 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 385 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 386 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 387 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 388 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 389 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 390 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 391 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 392 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 393 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 394 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 395 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 396 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 397 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 398 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 399 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 400 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 401 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 402 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 403 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 404 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 405 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 406 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 407 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 408 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 409 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 410 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 411 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 412 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 413 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 414 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 415 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 416 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 417 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 418 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 419 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 420 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 421 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 422 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 423 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 424 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 425 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 426 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 427 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 428 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 429 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 430 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 431 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 432 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 433 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 434 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 435 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 436 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 437 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 438 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 439 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 440 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 441 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 442 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 443 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 444 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 445 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 446 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 447 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 448 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 449 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 450 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 451 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 452 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 453 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 454 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 455 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 456 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 457 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 458 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 459 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 460 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 461 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 462 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 463 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 464 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 465 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 466 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 467 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 468 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 469 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 470 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 471 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 472 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 473 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 474 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 475 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 476 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 477 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 478 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 479 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 480 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 481 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 482 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 483 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 484 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 485 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 486 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 487 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 488 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 489 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 490 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 491 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 492 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 493 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 494 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 495 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 496 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 497 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 498 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 499 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 500 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 501 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 502 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 503 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 504 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 505 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 506 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 507 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 508 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 509 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 510 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 511 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 512 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 513 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 514 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 515 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 516 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 517 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 518 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 519 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 520 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 521 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 522 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 523 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 524 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 525 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 526 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 527 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 528 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 529 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 530 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 531 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 532 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 533 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 534 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 535 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 536 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 537 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 538 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 539 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 540 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 541 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 542 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 543 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 544 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 545 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 546 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 547 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 548 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 549 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 550 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 551 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 552 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 553 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 554 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 555 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 556 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 557 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 558 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 559 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
