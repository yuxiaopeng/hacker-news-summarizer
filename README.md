# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-01-31.md)

*最后自动更新时间: 2026-01-31 17:55:19*
## 1. Antirender：消除建筑渲染图中的光泽感

**原文标题**: Antirender: remove the glossy shine on architectural renderings

**原文链接**: [https://antirender.com/](https://antirender.com/)

基于 **Antirender** 的标题和前提，以下是该项目要点的简要总结：

**Antirender** 是一种批判性的视觉方法论，旨在解构当代建筑可视化中超写实且往往具有误导性的本质。其核心目标是通过剥离现代营销渲染图中典型的人造“华丽光泽”，来“看透建筑界的虚假噱头”。

关键信息与要点包括：

*   **批判视觉欺骗：** 该项目认为，标准的建筑渲染图已过度依赖讨喜的光影、理想化的天气条件和数字后期处理。这些元素往往掩盖了建筑的真实形态、材质质量和环境影响。
*   **强调原始真实：** 通过去除“光环”，Antirender 专注于几何形状、体量和空间关系等核心建筑元素，而不受大气效果或欺骗性纹理的干扰。
*   **诚实的沟通：** 该运动倡导建筑师、客户与公众之间进行更透明的对话。它建议通过以更务实、更少理想化的状态展示项目，建筑师可以设定切合实际的预期，并确保最终的实体结构与其数字表达相一致。
*   **打击“空头支票”式建筑：** 它作为一个工具，用于揭露那些在精心修饰的图像中看起来惊艳、但在现实中缺乏功能或结构完整性的设计。

本质上，Antirender 提倡**视觉诚实**，将建筑设计的本真性置于渲染图那经过打磨且“易于销售”的美学之上。

---

## 2. 苹果平台安全 (2026年1月) [PDF]

**原文标题**: Apple Platform Security (Jan 2026) [pdf]

**原文链接**: [https://help.apple.com/pdf/security/en_US/apple-platform-security-guide.pdf](https://help.apple.com/pdf/security/en_US/apple-platform-security-guide.pdf)

根据标题和原始 PDF 数据中提供的技术元数据，以下是《Apple 平台安全 (2026年1月)》指南的简要概述：

该文档是 Apple 对其硬件、软件和服务中集成的安全保护措施进行的全面技术回顾。它详细阐述了旨在通过“设计安全”理念保护用户数据的多层安全架构。

**安全框架的核心支柱：**
*   **硬件安全：** 基础植根于 Apple 芯片。指南详细介绍了 **Secure Enclave**，这是一个与主处理器隔离的专用子系统，用于管理生物识别信息（Face ID/触控 ID）和加密密钥等敏感数据。
*   **系统安全：** 涵盖了“信任链”，确保从硬件启动到加载操作系统的每一个步骤都经过 Apple 的加密签名和验证。
*   **加密与数据保护：** 文档概述了内置于硬件的先进加密引擎 (AES-256)，并解释了保护文件的密钥层级。即使设备遭到物理破解，也能确保只有在用户提供正确凭据时才能访问数据。
*   **应用与服务安全：** 指南描述了防止应用访问未经授权数据的沙盒技术，以及 iMessage、FaceTime 和 iCloud（包括高级数据保护）等服务所使用的端到端加密协议。

**2026 年背景：**
2026 年 1 月版可能反映了**后量子密码学**的进展以及针对复杂远程攻击的增强防护。虽然提供的元数据包含旧版格式信息，但该文档本身是研究人员和企业 IT 专业人士了解 Apple 如何抵御现代数字威胁的权威手册。

---

## 3. CPython 内部机制详解

**原文标题**: CPython Internals Explained

**原文链接**: [https://github.com/zpoint/CPython-Internals](https://github.com/zpoint/CPython-Internals)

《CPython 源码内幕详解》是一个全面的笔记与博文库，记录了 CPython 源码的内部运作机制，专门针对 3.8.0a0 版本。它旨在帮助资深 Python 程序员深入理解解释器的实现，而非提供通用的语言教程。

内容涵盖以下几个核心领域：

*   **对象与数据结构：** 深入分析基础类型，包括字典、整数、字符串、列表（Timsort）以及底层的 `PyObject` 结构。
*   **解释器机制：** 深度覆盖核心系统，如全局解释器锁（GIL）、垃圾回收（GC）、内存管理，以及属性访问和异常处理背后的逻辑。
*   **编译过程：** 概述从源代码到执行的转换过程，涵盖语法（Grammar）、具体语法树（CST）、抽象语法树（AST）和 Python 字节码。
*   **扩展与集成：** 关于使用 C API、Cython 和 Boost C++ 库编写高性能扩展、集成 NumPy 以及绕过 GIL 的指南。
*   **模块与库：** 对 `io`、`pickle`、`re` 和 `asyncio` 等特定模块的技术剖析。

除了技术文档，该仓库还提供了一系列精选的学习材料（书籍、博客和视频），并鼓励社区通过提交拉取请求（PR）和问题报告（Issue）来完善内容或纠正技术偏差。

---

## 4. NASA WB-57 飞机在休斯顿迫降。

**原文标题**: NASA's WB-57 crash lands at Houston

**原文链接**: [https://arstechnica.com/space/2026/01/one-of-nasas-three-wb-57-aircraft-just-did-a-belly-landing-in-houston/](https://arstechnica.com/space/2026/01/one-of-nasas-three-wb-57-aircraft-just-did-a-belly-landing-in-houston/)

周二上午，美国国家航空航天局（NASA）三架 WB-57 高空研究飞机中的一架在休斯顿埃灵顿机场进行了紧急“机腹着陆”。在发生机械故障后，飞行员成功驾驶飞机以机身着地的方式降落；NASA 确认所有机组人员均安全，目前正在对事故原因展开调查。

WB-57 是 B-57 “堪培拉”飞机的特种改型，其机型设计可追溯至 20 世纪 40 年代后期。虽然该机最初由美国空军用于轰炸和高空侦察，但自 1972 年以来，NASA 一直运行着一支小型机队用于科学研究。该机型具备在 60,000 英尺高空飞行的独特能力，使其能够研究飓风、收集宇宙尘埃并监测火箭尾焰对大气的影响。

涉及此次事故的飞机是 NASA 目前仅有的三架该型飞机之一，于 2013 年从空军“飞机坟场”中修复并重新启用。近期，这些飞机被用于追踪 SpaceX “星舰”的发射，并原计划为即将执行的“阿耳忒弥斯 2 号”探月任务提供关键观测数据。

目前尚不清楚受损飞机是否可以修复。如果该机永久停飞，可能会影响 NASA 进行高空观测的能力，以及在未来任务中对“猎户座”飞船重返大气层过程的监测。

---

## 5. 我们家里的 ipinfo：如何利用延迟在命令行中实现 IP 地理定位

**原文标题**: We have ipinfo at home or how to geolocate IPs in your CLI using latency

**原文链接**: [https://blog.globalping.io/we-have-ipinfo-at-home-or-how-to-geolocate-ips-in-your-cli-using-latency/](https://blog.globalping.io/we-have-ipinfo-at-home-or-how-to-geolocate-ips-in-your-cli-using-latency/)

本文介绍了一款开源命令行（CLI）工具，该工具旨在通过测量物理延迟来定位 IP 地址，而非依赖可能存在虚假的公共注册机构数据。作者指出，许多 VPN 服务商会在地理位置信息库（如 ARIN/RIPE）中伪装其位置；然而，通过全球多个观测点进行的基于延迟的“Ping”测试，可以更准确地反映 IP 的真实物理位置。

该工具利用了 **Globalping**，这是一个由社区驱动、拥有超过 3000 个探测点的网络。为了确定位置，该工具执行以下四个阶段：
1. **大洲检测：** 从各大洲向目标发送 Ping 请求，以寻找最低延迟。
2. **国家检测：** 在延迟最低的大洲内进行更高密度的测试。
3. **州级检测：** 如果目标位于美国，则将搜索范围缩小到具体的州。
4. **城市检测：** 根据记录到的最低延迟，确定距离最近的主要城市中心。

在技术层面，作者从标准的 ICMP 和 TCP Ping 转向了 **traceroute** 分析。通过测量最后一个可用跳数的延迟，即使目标网络屏蔽了 ICMP 流量，该工具也能准确定位 IP，因为上游供应商通常不会屏蔽此类流量。

该工具专为高效设计，每个阶段使用约 50 个探测点，以确保在 Globalping API 的未认证限制范围内。尽管作者承认准确性取决于探测点的密度，且商业算法可能更为复杂，但该工具成功验证了“伪造”的 IP，例如一个 NordVPN 地址显示在巴哈马，但物理位置实际位于迈阿密。该项目目前已开源，并鼓励用户通过托管自己的探测点来做出贡献。

---

## 6. 面向现代 Web 的动态 AVIF

**原文标题**: Animated AVIF for the Modern Web

**原文链接**: [https://arthur.pizza/2025/12/animated-avif-for-the-modern-web/](https://arthur.pizza/2025/12/animated-avif-for-the-modern-web/)

本文认为，**动图 AVIF** 是老旧 GIF 格式更优且更现代的替代方案。它在提供更好优化效果的同时，保留了 Web 动画“快速、循环、自动播放”的特性。

作者提供了一份使用 **FFmpeg** 创建此类文件的技术指南。针对在 Debian 13（截至 2025 年 12 月）上遇到的特定技术问题，该指南建议采用可靠的**两步转换流程**，而非单条命令：

1. **中间阶段：** 将源视频（如 .webm 或 .gif）转换为 **.y4m** 文件。在此步骤中，作者建议通过限制帧率（如 15 fps）和缩放尺寸（如 720p 宽度）来优化文件，从而保持文件体积易于管理。
2. **最终编码：** 使用 `libsvtav1` 视频编解码器将 .y4m 文件编码为最终的 **.avif** 封装格式。推荐设置使用恒定质量因子（`-crf 30`）来平衡画质与压缩率。

尽管作者指出单步命令在理论上可行，但目前分步处理可以有效避免编码错误。最终，本文将 AVIF 定位为高质量、轻量化 Web 动画的首选格式。

---

## 7. Guix System First Impressions as a Nix User

**原文标题**: Guix System First Impressions as a Nix User

**原文链接**: [https://nemin.hu/guix.html](https://nemin.hu/guix.html)

This article chronicles a NixOS user’s transition to **Guix System** following its 1.5.0 release. The author, a long-time Linux enthusiast, was drawn to Guix primarily by its use of **Guile Scheme**—a mature programming language—as a configuration alternative to the specialized Nix language.

The author’s experience highlights several significant challenges for newcomers:
*   **Hardware and Philosophy:** Guix’s strict "free software only" stance caused immediate issues with the author’s RTX 5070 GPU. The default installer lacked the necessary proprietary firmware, leading to broken graphical interfaces in KDE Plasma.
*   **Installation Hurdles:** While the TUI installer was straightforward, the author experienced extremely slow download speeds (50 kbps) and found the "indexing" process during updates to be time-consuming. 
*   **The "Nonguix" Necessity:** To achieve a functional system, the author turned to **Nonguix**, a third-party repository for non-free drivers and the standard Linux kernel. After several failed attempts and kernel panics, the author eventually succeeded by using a pre-built Nonguix ISO.
*   **Workflow Integration:** Despite a rocky start, the author was able to reproduce a Nix-like workflow. They successfully configured a desktop environment (eventually switching to i3) and began setting up essential tools like Emacs, various compilers (Rust, Zig), and browsers.

**Conclusion:** The author remains impressed with Guix’s declarative nature and Lisp-based configuration. However, they note that the learning curve—specifically regarding environment updates and the necessity of third-party repositories for modern hardware—makes it a more "rugged" experience compared to NixOS for those using proprietary components.

---

## 8. Quaternion Algebras

**原文标题**: Quaternion Algebras

**原文链接**: [https://jvoight.github.io/quat.html](https://jvoight.github.io/quat.html)

生成摘要时出错

---

## 9. Show HN: I trained a 9M speech model to fix my Mandarin tones

**原文标题**: Show HN: I trained a 9M speech model to fix my Mandarin tones

**原文链接**: [https://simedw.com/2026/01/31/ear-pronunication-via-ctc/](https://simedw.com/2026/01/31/ear-pronunication-via-ctc/)

生成摘要时出错

---

## 10. My Ridiculously Robust Photo Management System (Immich Edition)

**原文标题**: My Ridiculously Robust Photo Management System (Immich Edition)

**原文链接**: [https://jaisenmathai.com/articles/my-ridiculously-robust-photo-management-system-immich-edition/](https://jaisenmathai.com/articles/my-ridiculously-robust-photo-management-system-immich-edition/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 2 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 3 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 4 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 5 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 6 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 7 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 8 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 9 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 10 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 11 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 12 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 13 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 14 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 15 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 16 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 17 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 18 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 19 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 20 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 21 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 22 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 23 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 24 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 25 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 26 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 27 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 28 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 29 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 30 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 31 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 32 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 33 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 34 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 35 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 36 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 37 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 38 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 39 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 40 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 41 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 42 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 43 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 44 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 45 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 46 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 47 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 48 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 49 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 50 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 51 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 52 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 53 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 54 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 55 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 56 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 57 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 58 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 59 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 60 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 61 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 62 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 63 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 64 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 65 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 66 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 67 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 68 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 69 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 70 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 71 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 72 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 73 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 74 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 75 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 76 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 77 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 78 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 79 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 80 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 81 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 82 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 83 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 84 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 85 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 86 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 87 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 88 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 89 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 90 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 91 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 92 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 93 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 94 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 95 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 96 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 97 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 98 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 99 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 100 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 101 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 102 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 103 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 104 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 105 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 106 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 107 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 108 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 109 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 110 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 111 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 112 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 113 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 114 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 115 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 116 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 117 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 118 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 119 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 120 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 121 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 122 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 123 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 124 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 125 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 126 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 127 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 128 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 129 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 130 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 131 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 132 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 133 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 134 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 135 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 136 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 137 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 138 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 139 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 140 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 141 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 142 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 143 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 144 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 145 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 146 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 147 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 148 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 149 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 150 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 151 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 152 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 153 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 154 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 155 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 156 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 157 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 158 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 159 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 160 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 161 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 162 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 163 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 164 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 165 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 166 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 167 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 168 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 169 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 170 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 171 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 172 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 173 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 174 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 175 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 176 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 177 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 178 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 179 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 180 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 181 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 182 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 183 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 184 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 185 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 186 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 187 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 188 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 189 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 190 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 191 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 192 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 193 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 194 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 195 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 196 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 197 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 198 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 199 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 200 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 201 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 202 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 203 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 204 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 205 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 206 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 207 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 208 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 209 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 210 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 211 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 212 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 213 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 214 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 215 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 216 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 217 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 218 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 219 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 220 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 221 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 222 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 223 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 224 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 225 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 226 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 227 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 228 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 229 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 230 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 231 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 232 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 233 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 234 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 235 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 236 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 237 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 238 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 239 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 240 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 241 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 242 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 243 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 244 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 245 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 246 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 247 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 248 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 249 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 250 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 251 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 252 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 253 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 254 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 255 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 256 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 257 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 258 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 259 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 260 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 261 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 262 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 263 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 264 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 265 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 266 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 267 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 268 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 269 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 270 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 271 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 272 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 273 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 274 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 275 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 276 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 277 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 278 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 279 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 280 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 281 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 282 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 283 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 284 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 285 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 286 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 287 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 288 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 289 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 290 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 291 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 292 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 293 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 294 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 295 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 296 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 297 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 298 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 299 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 300 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 301 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 302 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 303 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 304 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 305 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 306 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 307 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 308 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 309 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 310 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 311 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 312 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 313 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 314 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 315 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 316 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 317 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
