# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-03-30.md)

*最后自动更新时间: 2026-03-30 18:20:54*
## 1. 如何将任何东西变成路由器

**原文标题**: How to turn anything into a router

**原文链接**: [https://nbailey.ca/post/router/](https://nbailey.ca/post/router/)

本文探讨了如何利用 Linux 将几乎任何计算机——包括迷你主机、旧笔记本电脑或“电子垃圾”——改造为高性能家用路由器。由于担心政府可能对消费级硬件实施监管，作者强调路由器本质上只是专用计算机，而“自制”路由器比成品型号具有更高的灵活性和更强的功能。

**硬件与软件要求**
理想的方案是使用被动散热的迷你主机，但任何至少拥有两个网络接口（板载或通过 USB 网口转换器）的设备均可。本指南采用 **Debian Linux**，并依赖以下核心软件包：
*   **hostapd**：将 Wi-Fi 网卡转换为无线访问点（AP）。
*   **dnsmasq**：管理 DNS 和 DHCP 服务。
*   **bridge-utils**：将有线和无线接口合并为单一局域网（LAN）。
*   **nftables**：处理防火墙和 NAT（网络地址转换）。

**关键设置步骤**
配置过程涉及多项技术调整：
1.  **BIOS 优化**：启用“掉电后自动开机”（Restore after AC Power Loss）并禁用 PXE 启动。
2.  **接口命名**：为稳定性创建持久的接口名称（如 `eth0`、`eth1`）。
3.  **组网配置**：在 Linux 内核中启用 IP 转发，以允许流量在 WAN（互联网）和 LAN 之间通过。
4.  **安全防护**：配置 `nftables` 以丢弃未授权的入站流量，同时允许内部路由。

**结论**
虽然作者为了简便起见专注于基础的 IPv4 设置，但由此产生的 DIY 路由器具有高度的可扩展性，能够支持 VPN、VLAN 和入侵检测。最后，本文展示了如何在保持对网络基础设施完全掌控的同时，榨干旧硬件的剩余价值。

---

## 2. 鸟脑 (2023)

**原文标题**: Bird brains (2023)

**原文链接**: [https://www.dhanishsemar.com/writing/bird-brains](https://www.dhanishsemar.com/writing/bird-brains)

《鸟类的大脑（2023）》一文探讨了鸟类卓越的智力，并指出“鸟类大脑”一词应当被视为一种赞美而非侮辱。

作者以新西兰啄羊鹦鹉（kea）为例展开论述。这种鸟学会了通过重新排列交通锥来阻挡车辆，从而向游客索要食物。这种行为促使政府建造了“啄羊鹦鹉健身房”来分散它们的注意力。各种科学测试也支持了这种问题解决能力：
*   **自我意识：** 欧亚喜鹊通过了镜子测试。
*   **问题解决：** 鸦科鸟类能成功利用工具和位移原理（伊索寓言测试）来获取食物。
*   **自我控制：** 渡鸦展现了延迟满足的能力，为了未来更好的奖励而放弃眼前的零食。
*   **交流：** 非洲灰鹦鹉（如著名的Alex）展示了理解形状、颜色和数字等抽象概念的能力。

这种智力的生物学奥秘在于**神经元密度**。2016年的研究显示，鹦鹉和鸣禽前脑容纳的神经元数量是同等体型灵长类动物的两倍。因此，微小的鸟类大脑在计算能力上可以与体型大得多的哺乳动物相媲美。

作者将鸟类的智力分为三个等级：
1.  **邪恶天才（鸦科）：** 工具制造和社会推理方面的佼佼者（如乌鸦和渡鸦）。
2.  **诈骗高手（鹦鹉）：** 交流和统计概率方面的专家（如非洲灰鹦鹉和啄羊鹦鹉）。
3.  **低调能手（鸣禽）：** 空间记忆大师（如星鸦）。

文章最后总结道，智力是由神经结构和密度而非大脑尺寸决定的。同时指出，唯一的“笨”鸟（如鸮鹦鹉）通常生活在缺乏捕食者的进化环境中，这使得高水平的认知防御变得不再必要。

---

## 3. 手写，记更好的笔记

**原文标题**: Take better notes, by hand

**原文链接**: [https://brianschrader.com/archive/take-better-notes-by-hand/](https://brianschrader.com/archive/take-better-notes-by-hand/)

在《手写，记更好的笔记》一文中，作者认为尽管数字工具非常便捷，但手写笔记仍是进行深度研究、全身心投入和加强记忆最有效的方法。虽然作者使用了一套包含数字应用（Pinboard、Books.app 和 Book Tracker）的四部分系统来保存链接和进行光学字符识别（OCR），但纸质笔记本才是其思考的核心引擎。

为了克服物理媒介的局限性——如搜索不便和空间有限——作者采用了几种具体的组织技巧：

*   **日期与页码：** 每项记录都标注日期，并手动编写页码（通常仅在右侧奇数页标注），以便于翻阅。
*   **索引：** 利用笔记本的前部或后部建立主题、书名和引用的滚动索引，方便日后快速检索。
*   **右页策略：** 主要笔记、引用和观察结果仅用钢笔记录在右侧页。
*   **左页反思：** 左侧页和边距预留给后续思考、修正或与其他页面的交叉引用，通常用铅笔书写。这种方式将原始信息与个人总结区分开来，并能识别出那些“衍生”的想法。

最终，作者发现这种结构化的物理系统减少了数字干扰，并为研究过程提供了一个实感的“进度条”。通过对不同项目使用这种布局一致的多个笔记本，作者建立了一个可扩展的个人知识库，提升了整合复杂想法和回溯信息的能力。

---

## 4. Cherri – 编译为 Apple 快捷指令的编程语言

**原文标题**: Cherri – programming language that compiles to an Apple Shortuct

**原文链接**: [https://github.com/electrikmilk/cherri](https://github.com/electrikmilk/cherri)

**Cherri**（发音同“cherry”）是一种专为直接编译成可运行的 Apple 快捷指令而设计的编程语言。其核心目标是提供一个强大的桌面端开发环境，使创建和维护大型、复杂的快捷指令项目变得切实可行。

**核心特性与能力：**
*   **开发环境：** Cherri 专为 macOS 开发，支持命令行界面 (CLI)、VSCode 扩展以及专用的 GUI 应用。它强调与快捷指令操作的 1:1 转换，以简化调试工作。
*   **现代语法：** 该语言从 Go 和 Ruby 中汲取灵感，用常量取代了“魔法变量”，并包含一套完善的带推断功能的类型系统。
*   **优化：** 编译器旨在生成体积更小的快捷指令文件，并降低运行时的内存占用。
*   **高级工具链：** 内置基于 Git 的包管理器，支持定义可重用函数、原始操作标识符以及通过 base64 嵌入文件。它还能将现有的 iCloud 链接转换回快捷指令代码。
*   **集成：** 用户可以定义导入问题、为菜单生成 VCard，并使用 macOS 本地或远程签名服务器对快捷指令进行签名。

**安装与开发初衷：**
Cherri 可以通过 **Homebrew** 或 **Nix** 安装。作者开发此语言是为了确保基于快捷指令的编程工具的长久生命力，因为许多先前的项目（如 ScPL 或 Jelly）已被放弃。通过专注于 macOS 的稳定性和专业级开发特性，Cherri 旨在为自动化爱好者提供一种高级的替代方案。

该项目始于 2022 年 10 月，得名于“Cherries”——这是原 Workflow 应用（快捷指令的前身）早期版本的一个代码名。

---

## 5. 建筑文档 OCR 无法正常工作，我们解决了。

**原文标题**: OCR for construction documents does not work, we fixed it

**原文链接**: [https://www.getanchorgrid.com/developer/docs/endpoints/drawings-doors](https://www.getanchorgrid.com/developer/docs/endpoints/drawings-doors)

本文档为 Anchorgrid AI 门检测 API 的技术说明，专门针对建筑平面图 PDF 设计。尽管标题侧重于通用 OCR，但内容详细介绍了一个专用端点（`POST /v1/drawings/detection/doors`），该端点能够识别门并以 PDF 坐标系下的边界框形式返回其位置。

**核心功能与工作流：**
*   **异步处理：** 用户首先上传 PDF 获取 `document_id`，随后将检测任务加入队列。系统返回 `job_id`，用户需通过轮询来获取最终结果。
*   **数据输出：** 任务完成后，API 提供检测到的门列表，包括唯一标识符、起始页码（从 1 开始）以及轴对齐边界框（$x_1, y_1, x_2, y_2$）。结果经过几何与中位数面积流水线的后过滤，以确保准确性。
*   **性能表现：** 免费档任务通常在 2–4 分钟内处理完成。付费档（专业版和企业版）利用专用 GPU 基础设施实现更快的响应，并支持通过 Webhook 发送自动完成通知。
*   **计费与配额：** 该服务每扫描一页扣除 2 个积分。使用受基于层级的速率限制（5 到 300 RPM）和每月积分池的约束。

该文档还列出了标准 HTTP 错误代码（401、402、404、422、429），用于处理身份验证、积分耗尽和速率限制等问题。这一专业工具旨在通过精确提取复杂建筑文档中的几何结构数据，解决标准 OCR 的局限性。

---

## 6. Build123d：一款 Python CAD 编程库

**原文标题**: Build123d: A Python CAD programming library

**原文链接**: [https://github.com/gumyr/build123d](https://github.com/gumyr/build123d)

**Build123d** is a Python-based, parametric boundary representation (BREP) modeling framework designed for 2D and 3D CAD. Built on the Open Cascade geometric kernel, it provides a "CAD-as-code" environment optimized for manufacturing processes like 3D printing, CNC machining, and laser cutting.

The library offers two primary modeling paradigms:
*   **Algebra Mode:** A stateless, explicit approach that uses standard Python operators (e.g., `+`, `-`, `*`) to combine and transform shapes, prioritizing readable and composable design logic.
*   **Builder Mode:** A stateful approach utilizing Python context managers (`with` statements) to track design history. This mode automatically manages transformations and "pending" shapes, making complex hierarchical constructions more intuitive.

**Key Features:**
*   **Geometric Hierarchy:** Provides explicit classes for 1D (Edges, Wires), 2D (Faces, Sketches), and 3D (Solids, Parts) geometry.
*   **Powerful Selectors:** Features a `ShapeList` system that allows users to filter, sort, and select specific geometric features based on properties like area, length, orientation, or geometric type.
*   **Pythonic Design:** Fully compliant with PEP 8 and rich type hints, the library integrates naturally with Python's ecosystem, allowing for easy extensibility through subclassing and functional composition.
*   **Interoperability:** Supports importing and exporting various formats, including STEP, STL, and SVG, for use with external CAD tools like FreeCAD and SolidWorks.

Licensed under Apache 2.0, Build123d is a refactored descendant of CadQuery. It is recommended for use with the `ocp_vscode` viewer and can be installed easily via pip. It is intended for developers seeking a modern, maintainable, and highly precise approach to parametric 3D modeling.

---

## 7. CodingFont: A game to help you pick a coding font

**原文标题**: CodingFont: A game to help you pick a coding font

**原文链接**: [https://www.codingfont.com/](https://www.codingfont.com/)

生成摘要时出错

---

## 8. New Washington state law bans noncompete agreements

**原文标题**: New Washington state law bans noncompete agreements

**原文链接**: [https://www.seattletimes.com/business/local-business/new-washington-law-bans-noncompete-agreements/](https://www.seattletimes.com/business/local-business/new-washington-law-bans-noncompete-agreements/)

Washington State has significantly strengthened its restrictions on noncompete agreements through newly signed legislation (SB 5935) that broadens worker protections and limits employer control. Building on a 2020 law, the updated regulations effectively ban noncompete clauses for a vast majority of the workforce.

Key provisions of the law include:

*   **Income Thresholds:** As of 2024, noncompete agreements are void for employees earning less than **$120,559.99** annually and independent contractors earning less than **$301,399.98**. These figures are adjusted yearly for inflation.
*   **Broadened Definitions:** The law expands the definition of "noncompete" to include restrictive "nonsolicitation" agreements. Employers can no longer bar former employees from doing business with *any* customer of the firm; restrictions are generally limited only to customers the employee specifically serviced.
*   **Moonlighting Protections:** Employers are prohibited from preventing workers from seeking a second job or additional income if the worker earns less than twice the state’s minimum wage.
*   **Time and Geography Limits:** Agreements lasting longer than 18 months are now presumed unreasonable and unenforceable. Additionally, the law prevents companies from requiring out-of-state workers to adjudicate disputes in the employer’s home state if they work in Washington.
*   **Retroactive Enforcement:** While the law applies to new contracts, it also allows workers to sue over noncompete clauses in contracts signed before 2020 if an employer attempts to enforce them.

The legislation reflects a growing national trend—echoed by the Federal Trade Commission—to increase labor mobility and wage growth by removing barriers that prevent workers from switching jobs or starting their own businesses. The law takes effect in June 2024.

---

## 9. 人工智能时代的数学方法与人类思维

**原文标题**: Mathematical methods and human thought in the age of AI

**原文链接**: [https://arxiv.org/abs/2603.26524](https://arxiv.org/abs/2603.26524)

生成摘要时出错

---

## 10. FTC action against Match and OkCupid for deceiving users, sharing personal data

**原文标题**: FTC action against Match and OkCupid for deceiving users, sharing personal data

**原文链接**: [https://www.ftc.gov/news-events/news/press-releases/2026/03/ftc-takes-action-against-match-okcupid-deceiving-users-sharing-personal-data-third-party](https://www.ftc.gov/news-events/news/press-releases/2026/03/ftc-takes-action-against-match-okcupid-deceiving-users-sharing-personal-data-third-party)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 2 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 3 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 4 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 5 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 6 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 7 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 8 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 9 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 10 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 11 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 12 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 13 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 14 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 15 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 16 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 17 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 18 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 19 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 20 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 21 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 22 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 23 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 24 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 25 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 26 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 27 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 28 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 29 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 30 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 31 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 32 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 33 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 34 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 35 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 36 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 37 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 38 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 39 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 40 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 41 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 42 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 43 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 44 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 45 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 46 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 47 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 48 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 49 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 50 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 51 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 52 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 53 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 54 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 55 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 56 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 57 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 58 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 59 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 60 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 61 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 62 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 63 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 64 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 65 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 66 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 67 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 68 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 69 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 70 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 71 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 72 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 73 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 74 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 75 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 76 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 77 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 78 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 79 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 80 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 81 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 82 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 83 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 84 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 85 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 86 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 87 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 88 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 89 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 90 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 91 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 92 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 93 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 94 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 95 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 96 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 97 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 98 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 99 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 100 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 101 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 102 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 103 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 104 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 105 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 106 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 107 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 108 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 109 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 110 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 111 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 112 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 113 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 114 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 115 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 116 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 117 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 118 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 119 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 120 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 121 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 122 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 123 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 124 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 125 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 126 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 127 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 128 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 129 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 130 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 131 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 132 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 133 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 134 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 135 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 136 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 137 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 138 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 139 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 140 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 141 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 142 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 143 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 144 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 145 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 146 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 147 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 148 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 149 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 150 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 151 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 152 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 153 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 154 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 155 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 156 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 157 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 158 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 159 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 160 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 161 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 162 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 163 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 164 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 165 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 166 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 167 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 168 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 169 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 170 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 171 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 172 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 173 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 174 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 175 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 176 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 177 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 178 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 179 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 180 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 181 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 182 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 183 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 184 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 185 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 186 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 187 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 188 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 189 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 190 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 191 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 192 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 193 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 194 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 195 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 196 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 197 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 198 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 199 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 200 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 201 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 202 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 203 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 204 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 205 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 206 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 207 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 208 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 209 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 210 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 211 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 212 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 213 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 214 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 215 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 216 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 217 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 218 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 219 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 220 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 221 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 222 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 223 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 224 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 225 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 226 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 227 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 228 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 229 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 230 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 231 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 232 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 233 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 234 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 235 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 236 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 237 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 238 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 239 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 240 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 241 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 242 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 243 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 244 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 245 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 246 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 247 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 248 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 249 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 250 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 251 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 252 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 253 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 254 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 255 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 256 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 257 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 258 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 259 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 260 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 261 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 262 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 263 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 264 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 265 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 266 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 267 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 268 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 269 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 270 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 271 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 272 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 273 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 274 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 275 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 276 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 277 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 278 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 279 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 280 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 281 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 282 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 283 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 284 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 285 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 286 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 287 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 288 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 289 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 290 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 291 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 292 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 293 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 294 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 295 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 296 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 297 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 298 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 299 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 300 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 301 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 302 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 303 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 304 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 305 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 306 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 307 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 308 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 309 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 310 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 311 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 312 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 313 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 314 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 315 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 316 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 317 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 318 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 319 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 320 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 321 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 322 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 323 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 324 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 325 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 326 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 327 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 328 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 329 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 330 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 331 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 332 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 333 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 334 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 335 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 336 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 337 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 338 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 339 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 340 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 341 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 342 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 343 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 344 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 345 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 346 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 347 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 348 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 349 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 350 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 351 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 352 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 353 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 354 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 355 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 356 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 357 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 358 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 359 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 360 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 361 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 362 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 363 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 364 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 365 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 366 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 367 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 368 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 369 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 370 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 371 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 372 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 373 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 374 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 375 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
