# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-02-01.md)

*最后自动更新时间: 2026-02-01 17:54:42*
## 1. Adventure Game Studio：用于制作冒险游戏的开源软件

**原文标题**: Adventure Game Studio: OSS software for creating adventure games

**原文链接**: [https://www.adventuregamestudio.co.uk/](https://www.adventuregamestudio.co.uk/)

**Adventure Game Studio (AGS)** 是一款免费、开源的开发套件，专为创作经典的图形化点击式冒险游戏而设计。它提供了一个基于 Windows 的全面集成开发环境 (IDE)，通过整合图形导入、脚本编写和游戏测试等工具来简化创作流程。

主要特点和信息包括：

*   **易用性与兼容性**：AGS 适合所有技能水平的开发者，且无需订阅。虽然编辑器基于 Windows，但制作的游戏可以在包括 Linux、iOS 和 Android 在内的多个平台运行。
*   **游戏展示**：该平台托管了数千款用户创作的作品。推荐游戏涵盖了从近期发布的 *Brainrot!* 和 *Nothmere*，到屡获殊荣的经典之作如 *5 Days a Stranger* 和 *An English Haunting*。
*   **社区与支持**：该软件拥有一个非常活跃且提供支持的社区。开发者可以通过专属论坛、Discord、Facebook 和线下聚会寻求帮助及开展社交。网站还会定期举办“游戏创作大赛”（如 MAGS）和精灵图 (sprite) 竞赛。
*   **可持续性**：AGS 是一个由志愿者运营的项目。虽然软件是免费的，但社区依靠 PayPal 捐款来支付论坛和网站的服务器及托管费用。

目前该软件的稳定版本为 **3.6.2 (Patch 6)**，提供可执行文件或 ZIP 压缩包下载。

---

## 2. Netbird – 开源零信任网络

**原文标题**: Netbird – Open Source Zero Trust Networking

**原文链接**: [https://netbird.io/](https://netbird.io/)

**NetBird** 是一个开源网络平台，旨在简化**零信任**架构的实施。它基于高性能的 **WireGuard** 协议，允许组织创建安全、加密的叠加网络，无论用户、设备和服务器身处何地，都能将其无缝连接。

**核心功能与信息：**

*   **零信任架构：** NetBird 摆脱了传统的“基于边界”的安全模式。它遵循“永不信任，始终验证”的原则，利用细粒度的访问控制策略，确保用户和设备仅能访问其所需的特定资源。
*   **点对点 (P2P) 连接：** 该平台在设备之间建立直接的加密隧道。通过利用先进的 NAT 穿透技术，NetBird 允许设备在防火墙和 NAT 后方实现无缝连接，无需复杂的各种手动配置或开放端口。
*   **简化管理：** 它提供一个中心化的管理控制台（支持云服务或自托管），管理员可以通过用户友好的界面管理对等节点、定义安全规则并监控网络健康状况。
*   **身份集成：** NetBird 与 Google、Microsoft Entra ID (Azure AD) 和 Okta 等主流身份提供商 (IdP) 集成。这确保了网络访问直接与组织现有的用户目录和单点登录 (SSO) 工作流挂钩。
*   **开源透明：** 作为管理开源项目，NetBird 提供了极高的透明度和灵活性。组织可以自托管整个基础设施，从而实现对数据和隐私的完全控制。

**结论：**
NetBird 是传统 VPN 的现代替代方案，在提供卓越安全性的同时显著降低了管理开销。它在保障远程办公安全、管理混合云环境以及建立安全的机器对机器 (M2M) 通信方面尤为高效。

---

## 3. 开发极简且有主见的编程智能体：我的心得体会

**原文标题**: What I learned building an opinionated and minimal coding agent

**原文链接**: [https://mariozechner.at/posts/2025-11-30-pi-coding-agent/](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/)

本文详述了 Mario Zechner 如何开发一套极简且具有“主见”的编码智能体套件，旨在取代他认为日益臃肿且不可预测的 Claude Code 和 Cursor 等主流工具。其核心理念围绕“**上下文工程**”展开：即保持对发送至大语言模型（LLM）信息的绝对控制，以确保输出的高质量与可预测性。

Zechner 构建了四个核心组件：

1.  **pi-ai**：一个统一的 LLM API，标准化了不同服务商（Anthropic、OpenAI、Google 等）之间的交互。它能够处理各服务商在推理痕迹、Token 追踪和工具调用方面的差异。该组件特别支持“**上下文接力**”，允许用户通过将特定服务商的元数据转换为通用格式，在会话中途切换模型（例如从 Claude 切换到 GPT）。
2.  **pi-agent-core**：一个编排循环，负责管理工具执行、使用 TypeBox 模式进行验证以及事件流传输。
3.  **pi-tui**：一个终端 UI 框架，采用差异化渲染技术提供“无闪烁”的用户体验。
4.  **pi-coding-agent**：最终的 CLI 工具，将上述组件集成到一个功能完备的工作区中。

**关键技术见解：**
*   **结构化工具结果**：Zechner 实现了一套系统，将工具输出分为两部分：供 LLM 理解的文本，以及供 UI 渲染的结构化数据/图像。
*   **中止与部分支持**：与许多统一 API 不同，`pi-ai` 支持完整的请求中止，并能在工具流传输过程中解析部分 JSON，以提升用户体验。
*   **透明度**：该套件避免了“隐蔽式”的上下文注入，允许开发者审查交互的每一个细节。

最终，该项目作为一个“极简框架”，拒绝了 MCP 支持或后台任务等现代功能，转而追求极速、可预测性和开发者的自主权。Zechner 总结道，虽然由于服务商 API 存在“泄漏性”，构建统一抽象具有挑战，但对于打造定制化的专业工作流而言，这至关重要。

---

## 4. MicroPythonOS图形操作系统提供类安卓的用户体验。

**原文标题**: MicroPythonOS graphical operating system delivers Android-like user experience

**原文链接**: [https://www.cnx-software.com/2026/01/29/micropythonos-graphical-operating-system-delivers-android-like-user-experience-on-microcontrollers/](https://www.cnx-software.com/2026/01/29/micropythonos-graphical-operating-system-delivers-android-like-user-experience-on-microcontrollers/)

MicroPythonOS is an open-source graphical operating system designed for microcontrollers, set to be featured at FOSDEM 2026. Heavily inspired by Android and iOS, it aims to provide a modern mobile-like user experience on resource-constrained hardware.

The system is written entirely in MicroPython and utilizes a "Thin OS" architecture that handles hardware initialization, multitasking, and the user interface. All other features—including WiFi configuration and system updates—are modular applications. Key features include:

*   **Android-like UI:** An LVGL-based interface supporting touchscreens, gestures, widgets, and themes.
*   **App Ecosystem:** An integrated AppStore for easy installation of tools like camera apps, image viewers, and motion sensor visualizers.
*   **Maintenance:** Supports Over-The-Air (OTA) firmware updates and built-in WiFi management.
*   **Performance:** Optimized for fast boot times and lightweight operation on low-power devices.

While primarily targeting ESP32 microcontrollers (such as the ESP32-S3-Touch-LCD-2), MicroPythonOS is cross-platform. It can run on any device supporting MicroPython, including the Raspberry Pi RP2350, as well as Windows, Linux, and macOS for development and evaluation purposes.

The OS is designed for a variety of applications, including smart home controllers, robotics, wearables, and educational tools. It currently supports a wide range of hardware, including cameras, IMUs, Bluetooth, and various I/O expanders. Developers can access the source code on GitHub and use a web installer for quick deployment on ESP32 targets.

---

## 5. 阿米加 Unix (Amix)

**原文标题**: Amiga Unix (Amix)

**原文链接**: [https://www.amigaunix.com/doku.php/home](https://www.amigaunix.com/doku.php/home)

**Amiga Unix**，或称 **Amix**，是 Commodore 公司于 1990 年将 AT&T System V Release 4 移植到 Amiga 平台的产物。该操作系统主要与 Amiga 2500UX 和 3000UX 型号相关，可运行于任何兼容的 Amiga 硬件，或通过 WinUAE 模拟器（2.7.0 及更高版本）运行。

Amiga Unix 维基作为历史档案和技术资源，面向“SVR4 发烧友”及业余爱好者。它提供了有关安装、硬件兼容性、网络以及软件补丁（包括关键的 Y2K 千禧年和 DST 夏令时修复）的文档。

然而，文中对现代用户发出了强烈的“买家自负”警告。Amix 被描述为一个冷酷无情、“苦涩且暗淡”的环境，其安装和管理难度极大。由于其内核和许多组件均为闭源，开发工作在 Commodore 倒闭后便已停止，导致系统遗留了损坏的软件包系统和重大的安全漏洞。它缺乏 Linux 或 FreeBSD 等现代类 Unix 系统的功能与用户友好性。

归根结底，文章认为现今运行 Amix 的唯一理由是好奇心和历史研究。它为人们了解 20 世纪 90 年代初的系统编程和 System V Unix 的遗产提供了独特视角。对于那些愿意勇闯“m68k-cbm-sysv4 地牢”的人来说，Amix 代表了计算机历史上一次迷人但并不实用的尝试；而对于其他人，该网站建议坚持使用现代操作系统。

---

## 6. PF之书（第4版）

**原文标题**: The Book of PF, 4th edition

**原文链接**: [https://nostarch.com/book-of-pf-4th-edition](https://nostarch.com/book-of-pf-4th-edition)

《The Book of PF（第 4 版）》是一本精通 Packet Filter (PF) 的全面指南。PF 是 OpenBSD 及其他类 Unix 平台所使用的强大防火墙系统。目录概述了从基础概念到高级网络管理的循序渐进过程。

本书分为以下几个关键领域：
* **基础：** 初始章节涵盖了网络构建和基础 PF 配置。
* **实际应用：** 探讨了实际部署，包括保障无线网络安全以及管理复杂或高流量的架构。
* **高级优化：** 详细介绍了主动防御技术、通过队列和优先级进行的流量整形，以及通过冗余确保高可用性。
* **维护：** 最后几章侧重于日志记录、监控以及为实现最佳性能而进行的配置微调。

该指南还包括关于硬件支持和额外资源的附录。值得注意的是，提供的目录表明这是一个**抢先体验（Early Access）**版本，这意味着目前的 PDF 版本仅包含选定的章节（在原文中已突出显示）。总的来说，对于寻求使用 PF 实现强健安全性和高效流量控制的管理员来说，本书是一份权威的路线图。

---

## 7. FOSDEM 2026 – 布鲁塞尔开源大会 – 第一日回顾

**原文标题**: FOSDEM 2026 – Open-Source Conference in Brussels – Day#1 Recap

**原文链接**: [https://gyptazy.com/blog/fosdem-2026-opensource-conference-brussels/](https://gyptazy.com/blog/fosdem-2026-opensource-conference-brussels/)

2026 年布鲁塞尔 FOSDEM 大会以**数字主权**和欧洲技术独立为核心主题。会议反映出技术领域正经历显著转型，即从中心化平台转向自托管、高韧性且由社区治理的基础设施。

技术亮点包括：
*   **极简主义与安全**：关于 **SmolBSD** 的讨论强调了系统的简洁性与可审计性，而 **Rust-VMM** 则展示了内存安全的虚拟化技术。
*   **基础设施**：关于 **Garage S3** 的演讲分享了对象存储的运营见解，而 **Kubernetes** 相关议题则探讨了云原生环境中虚拟机的迁移。
*   **社区网络**：**FlipFlap** 项目演示了通过 **DN42** 实现的去中心化组网，**BoxyBSD** 则因降低了 BSD 新用户的准入门槛而受到关注。
*   **应用层**：Michael Meeks 在关于 **Collabora Online** 的演讲中强调了维持开源办公套件竞争力所需的巨大技术与战略投入。

除会议议程外，作者还提到了在 **Proxmox** 和 **Vates (XCP-ng)** 等展位进行线下交流的价值，以及 Mozilla 互动派发饼干等活动所营造的独特社区氛围。

然而，回顾报告也指出了一个关键转折点：**过度拥挤**。FOSDEM 的规模正趋于物理极限，人满为患的会议室和高压环境威胁到了大会传统的自发性和包容性。作者观察到，虽然转向“紧迫”的政治与战略议题确有必要，但这可能会挤占小型、分众化实验项目的空间。

最终，尽管作者曾动过居家观看直播的念头，但仍认为线下体验——与全球好友重逢并参与即兴辩论——是无可取代的。FOSDEM 2026 证明，虽然开源的重要性已达到巅峰，但该盛会必须在物流组织上寻求变革，以延续其包容精神。

---

## 8. Anciente map of Fairyland. Places from nursery rhymes, fairy tales etc.

**原文标题**: Anciente map of Fairyland. Places from nursery rhymes, fairy tales etc.

**原文链接**: [https://collections.leventhalmap.org/search/commonwealth:3f463773q](https://collections.leventhalmap.org/search/commonwealth:3f463773q)

生成摘要时出错

---

## 9. Mobile carriers can get your GPS location

**原文标题**: Mobile carriers can get your GPS location

**原文链接**: [https://an.dywa.ng/carrier-gnss.html](https://an.dywa.ng/carrier-gnss.html)

生成摘要时出错

---

## 10. VisualJJ – Jujutsu in Visual Studio Code

**原文标题**: VisualJJ – Jujutsu in Visual Studio Code

**原文链接**: [https://www.visualjj.com/](https://www.visualjj.com/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 2 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 3 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 4 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 5 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 6 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 7 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 8 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 9 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 10 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 11 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 12 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 13 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 14 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 15 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 16 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 17 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 18 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 19 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 20 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 21 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 22 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 23 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 24 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 25 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 26 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 27 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 28 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 29 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 30 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 31 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 32 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 33 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 34 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 35 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 36 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 37 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 38 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 39 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 40 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 41 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 42 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 43 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 44 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 45 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 46 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 47 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 48 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 49 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 50 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 51 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 52 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 53 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 54 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 55 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 56 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 57 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 58 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 59 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 60 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 61 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 62 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 63 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 64 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 65 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 66 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 67 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 68 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 69 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 70 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 71 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 72 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 73 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 74 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 75 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 76 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 77 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 78 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 79 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 80 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 81 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 82 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 83 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 84 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 85 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 86 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 87 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 88 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 89 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 90 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 91 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 92 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 93 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 94 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 95 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 96 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 97 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 98 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 99 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 100 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 101 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 102 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 103 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 104 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 105 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 106 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 107 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 108 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 109 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 110 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 111 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 112 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 113 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 114 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 115 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 116 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 117 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 118 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 119 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 120 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 121 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 122 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 123 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 124 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 125 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 126 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 127 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 128 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 129 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 130 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 131 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 132 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 133 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 134 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 135 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 136 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 137 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 138 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 139 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 140 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 141 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 142 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 143 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 144 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 145 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 146 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 147 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 148 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 149 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 150 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 151 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 152 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 153 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 154 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 155 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 156 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 157 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 158 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 159 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 160 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 161 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 162 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 163 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 164 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 165 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 166 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 167 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 168 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 169 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 170 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 171 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 172 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 173 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 174 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 175 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 176 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 177 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 178 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 179 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 180 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 181 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 182 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 183 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 184 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 185 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 186 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 187 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 188 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 189 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 190 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 191 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 192 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 193 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 194 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 195 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 196 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 197 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 198 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 199 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 200 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 201 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 202 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 203 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 204 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 205 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 206 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 207 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 208 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 209 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 210 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 211 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 212 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 213 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 214 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 215 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 216 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 217 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 218 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 219 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 220 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 221 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 222 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 223 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 224 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 225 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 226 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 227 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 228 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 229 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 230 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 231 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 232 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 233 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 234 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 235 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 236 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 237 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 238 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 239 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 240 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 241 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 242 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 243 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 244 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 245 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 246 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 247 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 248 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 249 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 250 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 251 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 252 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 253 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 254 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 255 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 256 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 257 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 258 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 259 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 260 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 261 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 262 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 263 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 264 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 265 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 266 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 267 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 268 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 269 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 270 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 271 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 272 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 273 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 274 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 275 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 276 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 277 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 278 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 279 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 280 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 281 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 282 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 283 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 284 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 285 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 286 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 287 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 288 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 289 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 290 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 291 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 292 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 293 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 294 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 295 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 296 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 297 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 298 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 299 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 300 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 301 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 302 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 303 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 304 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 305 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 306 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 307 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 308 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 309 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 310 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 311 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 312 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 313 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 314 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 315 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 316 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 317 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 318 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
