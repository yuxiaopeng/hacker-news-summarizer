# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-10-10.md)

*最后自动更新时间: 2026-10-10 20:53:36*
## 1. 二维车辆

**原文标题**: 2D Vehicles

**原文链接**: [https://patkerr.co.uk/2d-vehicles/](https://patkerr.co.uk/2d-vehicles/)

本文记录了一个2D车辆物理模拟系统的历史及其30周年复刻版，该系统曾是初代《侠盗猎车手》（GTA）的基石。该原型最初于1996年在Atari ST上使用GFA BASIC开发，作者现已使用JavaScript对其进行了“重制”，以展示驱动这款经典游戏的底层机制。

该模拟在当时具有创新性，因为它采用了**2D刚体动力学**（包含扭矩和旋转），而非20世纪90年代游戏中常见的“点物理”。该系统由三个层级构建：
1.  **刚体 (The Rigid Body)：** 追踪位置、速度、角度和角速度。
2.  **外壳 (The Shell)：** 定义车辆的形状和碰撞几何。
3.  **动力学 (The Dynamics)：** 通过三种模式决定行为：“方块”模式（基础物理）、“飞船”模式（基于推力）和“赛车”模式（转向/轮胎物理）。

核心亮点是作者“刻意近似”的轮胎模型。该模拟并未采用复杂的真实摩擦力或侧滑计算，而是将速度分解为纵向和横向分量，并施加阻力来模拟抓地力。这种“够用就好”的方法营造了俯视角驾驶所需的独特操控感。此次复刻还包含一个处理碰撞的简单障碍物求解器，以及模拟初代GTA“速度缩放”和“死区”特性的镜头控制。

作者发表了自愿免责声明，表示本项目是完全独立的物理复刻，与Rockstar Games或Take-Two Interactive无关。总之，本文从技术视角展示了一个简单的周末项目是如何演变成一个顶级视频游戏系列的核心机制的。

---

## 2. 高德纳奖励支票

**原文标题**: Knuth reward check

**原文链接**: [https://www.thomas-huehn.com/knuth-reward-check/](https://www.thomas-huehn.com/knuth-reward-check/)

作者讲述了自己获得计算机科学界传奇人物高德纳（Donald Knuth）奖励支票的罕见经历。在高德纳的出版物中发现错误并获得奖励，已成为该领域的一项传统。

尽管高德纳的著作曾被无数读者悉心研读，作者依然在《计算机现代字体》（《计算机与排版》系列第五卷）中发现了一个错误。令人惊讶的是，该错误就位于第一页第一段的第一个单词。高德纳确认了这一发现，并签发了一张标有“E1”字样的支票，代表该错误所在的卷号和页码。

几年后，作者又因在后续的错误报告中提出了一项有益建议而获得0.32美元的额外奖励，使其奖励总额达到2.88美元（十六进制表示为0x$1.20）。作者提到，出于安全考虑，高德纳现在不再寄送真实支票，而是发放来自虚构“圣塞里夫银行”的“幻想证书”。这篇文章突显了作者的自豪之情，因为他发现了一个被广大学术界忽视多年且显而易见的错误。

---

## 3. Why DuckDB 2.0 is faster

**原文标题**: Why DuckDB 2.0 is faster

**原文链接**: [https://motherduck.com/blog/why-duckdb-20-is-faster/](https://motherduck.com/blog/why-duckdb-20-is-faster/)

生成摘要时出错

---

## 4. 英伟达洽谈收购美国“开放”模型初创公司 Reflection AI

**原文标题**: Nvidia in talks to acquire US 'open' model startup Reflection AI

**原文链接**: [https://www.ft.com/content/052610c5-22b4-4dd4-932e-b7f9f0628b6a](https://www.ft.com/content/052610c5-22b4-4dd4-932e-b7f9f0628b6a)

据报道，英伟达（Nvidia）正在就收购 Reflection AI 进行谈判，这是一家总部位于美国的初创公司，专注于“开放式”人工智能模型。此次潜在的收购标志着英伟达正持续发力，试图突破其在硬件领域的统治地位，在人工智能软件和服务生态系统中建立更稳固的立足点。

Reflection AI 凭借其发布的“Reflection 70B”模型在 AI 领域引起了广泛关注。该初创公司采用了一种名为“反思微调”（reflection tuning）的技术，使大语言模型能够在给出最终回复之前，识别并纠正自身的推理错误。尽管该模型最初被宣传为全球性能最强的开源大语言模型，但随后因其实际性能基准和透明度问题，遭到了研究人员的严厉审视和质疑。

对英伟达而言，此次收购将加强其“英伟达 AI 代工厂”（Nvidia AI Foundry）业务，这是一套旨在帮助企业构建和部署定制化生成式 AI 模型的工具和服务。通过将 Reflection 的纠错技术和人才引入内部，英伟达旨在为客户提供更可靠、更先进的软件解决方案，从而与其 H100 和 Blackwell 芯片形成互补。

这一举措反映了更广泛的行业趋势，即包括微软、亚马逊和谷歌在内的科技巨头正通过积极收购初创公司或“收编式招聘”（acqui-hiring）人才，来确保获取专业的人工智能技术。虽然英伟达与 Reflection AI 之间的讨论仍在进行中，但交易尚未最终敲定。如果完成，这将进一步巩固英伟达作为下一代人工智能端到端提供商的地位。

---

## 5. Talorys – 基于 Cloudflare 免费层的自托管个人 AI 智能体

**原文标题**: Talorys – A self-hosted personal AI agent on Cloudflare's free tier

**原文链接**: [https://github.com/rociiu/talorys](https://github.com/rociiu/talorys)

**Talorys** 是一款开源、自托管的个人 AI 助手，旨在完全运行于用户的 Cloudflare 账户中。通过利用 Cloudflare 的免费层服务——包括 Pages、Workers、Durable Objects（用于 SQLite 存储）和 Workers AI——它在无需外部服务器、数据库或第三方订阅的情况下，提供了一个私人助理。

核心功能包括：
*   **AI 能力：** 具有“记忆”系统的流式聊天界面，能够记录个人事实和偏好，为后续交互提供上下文。
*   **生产力工具：** 内置任务、笔记和项目管理功能，可通过 UI 或自然语言对话进行处理。
*   **自动化：** 支持一次性和循环提醒、每日任务摘要，以及利用 Durable Object 闹钟按计划运行的 AI 例行任务。
*   **隐私与安全：** 专为单用户设计，无需注册且无遥测采集。所有数据均保留在用户的 Cloudflare 基础设施内。后端 Worker 是私有的（无公共 URL），并采用本地哈希的所有者密码进行身份验证。

部署过程通过单条命令 (`npx create-talorys@latest`) 实现了简化，可自动配置资源和安全凭证。虽然该系统针对 Cloudflare 的免费配额进行了优化，但它具备良好的韧性：即使每日 AI 配额耗尽，任务和笔记等非 AI 功能仍可正常使用。用户通过内置的 JSON 备份、更新和密码管理工具拥有数据的完全所有权。总而言之，Talorys 通过让用户掌控自己的云基础设施，为中心化 AI 助手提供了一个以隐私为中心、零成本的替代方案。

---

## 6. Recent AI models struggled to match a human algorithmic innovation

**原文标题**: Recent AI models struggled to match a human algorithmic innovation

**原文链接**: [https://epoch.ai/publications/innovationeval](https://epoch.ai/publications/innovationeval)

生成摘要时出错

---

## 7. Mxc：微软执行容器 1.0.0 版

**原文标题**: Mxc: Microsoft Execution Containers version 1.0.0

**原文链接**: [https://blogs.windows.com/windowsdeveloper/2026/10/07/microsoft-execution-containers-policy-driven-containment-for-ai-agents/](https://blogs.windows.com/windowsdeveloper/2026/10/07/microsoft-execution-containers-policy-driven-containment-for-ai-agents/)

微软宣布 **Microsoft Execution Containers (MXC) 1.0.0 版本**正式发布。这是一个基于策略的隔离层，旨在确保 AI 智能体的安全。随着智能体具备了与文件、网络和应用程序交互的能力，MXC 提供了一个托管执行边界，在不牺牲生产力的前提下降低安全风险。

**核心特性与功能：**
*   **基于策略的容器化：** MXC 允许开发人员和 IT 管理员使用统一的 JSON 架构和 SDK 定义特定的资源边界（文件、网络、UI）。这些策略独立于智能体强制执行，可防止“自我授权”的权限提升。
*   **灵活的后端：** MXC 支持在 Windows、macOS 和 Linux 上实现多种隔离级别，包括：
    *   **进程容器 (Process Containers)：** 适用于所有平台的轻量级沙箱。
    *   **会话容器 (Session Containers，仅限 Windows)：** 桌面、剪贴板和 UI 的隔离。
    *   **WSL 容器：** 适用于基于 Linux 的工具链。
    *   **微型虚拟机 (MicroVMs)：** 针对高风险工作负载的硬件辅助隔离。
*   **运行模式：** 为了协助创建“最小权限”策略，MXC 提供三种模式：**强制模式 (Enforcement)**（主动拦截）、**学习模式 (Learning)**（拦截并报告活动）和**宽容模式 (Permissive)**（允许活动并报告，用于优化策略）。

**治理与身份：**
除了容器化，微软正将智能体活动整合到其更广泛的生态系统中。未来的更新将使 **Microsoft Entra** 能够区分智能体身份与用户身份，允许安全团队在不中断人工操作的情况下限制或阻断受损的智能体。此外，**Microsoft Intune** 很快将提供对 MXC 策略的集中化管理。

**生态系统采用：**
主流 AI 框架和工具——包括 GitHub Copilot、OpenAI Codex、NVIDIA 和 Anthropic Claude Code——已经开始集成或承诺支持 MXC。这为在本地或通过 Windows 365 在云端运行的智能体确保了标准化的安全模型。

---

## 8. 灯泡电脑

**原文标题**: The Lightbulb Computer

**原文链接**: [https://lightbulbcomputer.com/](https://lightbulbcomputer.com/)

在《灯泡电脑》（The Lightbulb Computer）中，前苹果设计师 Guillaume Ardaud 提议将计算范式从“佩戴式计算”（VR/AR 头显）转向基于投影的空间计算。Ardaud 认为，虽然头显是目前行业的焦点，但它们会导致社交孤立、产生物理束缚且佩戴不适。

**灯泡电脑**是一款结合了高分辨率投影仪与先进计算机视觉的构想设备。它旨在适配标准的爱迪生灯座或便携式电池底座，能将日常表面转化为交互式显示屏。其核心功能包括语音指令识别、手势追踪和实时环境分析。

Ardaud 通过真实的原型展示了几个实际应用场景：
* **厨房/家居：** 无需动手的食谱叠加显示、计时器，以及与环境融为一体的交互式家庭看板。
* **社交/协作：** 大规模地图规划和照片共享，允许多人共同交互，而无需围拢在小屏幕前。
* **智能家居：** “指点控制”交互，用户只需指向智能设备即可对其进行管理。
* **信息增强：** 即时图书扫描，并为 3D 地图等物理对象添加天气状况等实时数据。

作者强调，这种“环境计算”比基于屏幕或佩戴式的替代方案更具“亲和力”，因为它是在增强物理世界，而非取代物理世界或孤立用户。尽管 Ardaud 承认消费级硬件仍在演进中，但他指出视觉模型和投影仪体积的进步使这一愿景变得可行。他还强调隐私必须是首要考虑因素，应通过设备端处理和物理硬件防护来解决。最终，该项目倡导一种计算自然融入居住空间的未来，而非局限于令人分心的玻璃屏幕。

---

## 9. Apple/macOS 已从官方 Unix 注册表中移除

**原文标题**: Apple/macOS removed from official Unix registry

**原文链接**: [https://www.opengroup.org//openbrand/register/](https://www.opengroup.org//openbrand/register/)

The Open Group 官方 UNIX 认证产品登记簿显示，Apple/macOS 已从获准正式使用 UNIX® 商标的认证系统名单中被移除。

The Open Group 是负责维护“单一 UNIX 规范”（Single UNIX Specification）的组织。该认证为操作系统设定了全球基准，确保其在可移植性、稳定性和互操作性方面符合严苛标准。只有完全合规且通过认证的系统才被允许使用 UNIX 品牌，这不仅保证了应用开发的一致性，也保障了企业用户的投资。

根据目前的登记记录，目前仍保留认证的产品仅涉及三家供应商：

*   **IBM 公司：** z/OS 和 AIX 的多个版本。
*   **慧与 (Hewlett Packard Enterprise)：** 运行在 Integrity 服务器上的 HP-UX 11i V3。
*   **SCO Group 公司：** UnixWare 7 以及 SCO OpenServer 第 5 版和第 6 版。

从历史上看，macOS（自 Mac OS X 10.5 起）一直持有 UNIX 03 认证。其在最新名单中的缺席表明，苹果公司要么是任由认证效力过期，要么是其产品不再符合登记簿中所列当前标准（UNIX V7、03、98 或 95）的特定要求。这一变化标志着一个重大的转变，因为 macOS 此前曾是全球使用最广泛的 UNIX 认证系统之一。

---

## 10. Nix wrote half of my debugger

**原文标题**: Nix wrote half of my debugger

**原文链接**: [https://fzakaria.com/2026/10/07/nix-wrote-half-of-my-debugger](https://fzakaria.com/2026/10/07/nix-wrote-half-of-my-debugger)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 2 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 3 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 4 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 5 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 6 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 7 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 8 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 9 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 10 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 11 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 12 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 13 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 14 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 15 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 16 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 17 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 18 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 19 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 20 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 21 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 22 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 23 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 24 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 25 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 26 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 27 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 28 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 29 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 30 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 31 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 32 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 33 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 34 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 35 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 36 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 37 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 38 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 39 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 40 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 41 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 42 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 43 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 44 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 45 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 46 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 47 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 48 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 49 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 50 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 51 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 52 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 53 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 54 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 55 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 56 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 57 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 58 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 59 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 60 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 61 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 62 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 63 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 64 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 65 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 66 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 67 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 68 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 69 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 70 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 71 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 72 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 73 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 74 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 75 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 76 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 77 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 78 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 79 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 80 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 81 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 82 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 83 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 84 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 85 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 86 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 87 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 88 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 89 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 90 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 91 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 92 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 93 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 94 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 95 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 96 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 97 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 98 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 99 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 100 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 101 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 102 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 103 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 104 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 105 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 106 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 107 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 108 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 109 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 110 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 111 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 112 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 113 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 114 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 115 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 116 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 117 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 118 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 119 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 120 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 121 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 122 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 123 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 124 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 125 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 126 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 127 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 128 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 129 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 130 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 131 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 132 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 133 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 134 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 135 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 136 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 137 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 138 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 139 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 140 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 141 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 142 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 143 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 144 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 145 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 146 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 147 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 148 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 149 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 150 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 151 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 152 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 153 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 154 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 155 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 156 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 157 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 158 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 159 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 160 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 161 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 162 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 163 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 164 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 165 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 166 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 167 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 168 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 169 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 170 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 171 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 172 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 173 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 174 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 175 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 176 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 177 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 178 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 179 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 180 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 181 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 182 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 183 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 184 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 185 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 186 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 187 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 188 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 189 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 190 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 191 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 192 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 193 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 194 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 195 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 196 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 197 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 198 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 199 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 200 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 201 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 202 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 203 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 204 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 205 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 206 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 207 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 208 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 209 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 210 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 211 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 212 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 213 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 214 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 215 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 216 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 217 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 218 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 219 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 220 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 221 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 222 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 223 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 224 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 225 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 226 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 227 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 228 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 229 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 230 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 231 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 232 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 233 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 234 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 235 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 236 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 237 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 238 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 239 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 240 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 241 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 242 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 243 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 244 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 245 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 246 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 247 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 248 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 249 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 250 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 251 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 252 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 253 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 254 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 255 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 256 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 257 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 258 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 259 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 260 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 261 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 262 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 263 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 264 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 265 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 266 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 267 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 268 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 269 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 270 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 271 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 272 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 273 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 274 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 275 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 276 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 277 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 278 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 279 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 280 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 281 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 282 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 283 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 284 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 285 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 286 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 287 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 288 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 289 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 290 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 291 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 292 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 293 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 294 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 295 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 296 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 297 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 298 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 299 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 300 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 301 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 302 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 303 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 304 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 305 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 306 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 307 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 308 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 309 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 310 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 311 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 312 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 313 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 314 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 315 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 316 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 317 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 318 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 319 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 320 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 321 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 322 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 323 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 324 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 325 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 326 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 327 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 328 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 329 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 330 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 331 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 332 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 333 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 334 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 335 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 336 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 337 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 338 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 339 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 340 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 341 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 342 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 343 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 344 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 345 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 346 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 347 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 348 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 349 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 350 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 351 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 352 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 353 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 354 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 355 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 356 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 357 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 358 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 359 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 360 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 361 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 362 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 363 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 364 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 365 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 366 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 367 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 368 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 369 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 370 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 371 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 372 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 373 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 374 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 375 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 376 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 377 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 378 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 379 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 380 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 381 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 382 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 383 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 384 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 385 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 386 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 387 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 388 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 389 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 390 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 391 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 392 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 393 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 394 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 395 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 396 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 397 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 398 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 399 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 400 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 401 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 402 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 403 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 404 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 405 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 406 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 407 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 408 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 409 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 410 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 411 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 412 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 413 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 414 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 415 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 416 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 417 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 418 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 419 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 420 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 421 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 422 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 423 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 424 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 425 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 426 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 427 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 428 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 429 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 430 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 431 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 432 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 433 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 434 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 435 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 436 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 437 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 438 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 439 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 440 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 441 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 442 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 443 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 444 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 445 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 446 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 447 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 448 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 449 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 450 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 451 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 452 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 453 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 454 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 455 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 456 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 457 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 458 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 459 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 460 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 461 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 462 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 463 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 464 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 465 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 466 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 467 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 468 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 469 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 470 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 471 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 472 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 473 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 474 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 475 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 476 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 477 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 478 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 479 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 480 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 481 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 482 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 483 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 484 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 485 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 486 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 487 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 488 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 489 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 490 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 491 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 492 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 493 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 494 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 495 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 496 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 497 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 498 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 499 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 500 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 501 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 502 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 503 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 504 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 505 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 506 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 507 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 508 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 509 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 510 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 511 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 512 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 513 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 514 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 515 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 516 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 517 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 518 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 519 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 520 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 521 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 522 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 523 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 524 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 525 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 526 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 527 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 528 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 529 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 530 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 531 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 532 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 533 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 534 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 535 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 536 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 537 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 538 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 539 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 540 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 541 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 542 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 543 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 544 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 545 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 546 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 547 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 548 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 549 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 550 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 551 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 552 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 553 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 554 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 555 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 556 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 557 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 558 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 559 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 560 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 561 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 562 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 563 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 564 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 565 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 566 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 567 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
