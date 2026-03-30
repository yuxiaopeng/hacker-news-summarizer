# Hacker News 热门文章摘要 (2026-03-30)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. ChatGPT won't let you type until Cloudflare reads your React state

**原文标题**: ChatGPT won't let you type until Cloudflare reads your React state

**原文链接**: [https://www.buchodi.com/chatgpt-wont-let-you-type-until-cloudflare-reads-your-react-state-i-decrypted-the-program-that-does-it/](https://www.buchodi.com/chatgpt-wont-let-you-type-until-cloudflare-reads-your-react-state-i-decrypted-the-program-that-does-it/)

生成摘要时出错

---

## 12. From Proxmox to FreeBSD and Sylve in Our Office Lab

**原文标题**: From Proxmox to FreeBSD and Sylve in Our Office Lab

**原文链接**: [https://www.iptechnics.com/blogs/from-proxmox-to-freebsd-and-sylve-in-our-office-lab](https://www.iptechnics.com/blogs/from-proxmox-to-freebsd-and-sylve-in-our-office-lab)

生成摘要时出错

---

## 13. The curious case of retro demo scene graphics

**原文标题**: The curious case of retro demo scene graphics

**原文链接**: [https://www.datagubbe.se/aipixels/](https://www.datagubbe.se/aipixels/)

生成摘要时出错

---

## 14. I use Excalidraw to manage my diagrams for my blog

**原文标题**: I use Excalidraw to manage my diagrams for my blog

**原文链接**: [https://blog.lysk.tech/excalidraw-frame-export/](https://blog.lysk.tech/excalidraw-frame-export/)

生成摘要时出错

---

## 15. An NSFW filter for Marginalia search

**原文标题**: An NSFW filter for Marginalia search

**原文链接**: [https://www.marginalia.nu/log/a_134_nsfw/](https://www.marginalia.nu/log/a_134_nsfw/)

生成摘要时出错

---

## 16. You are falling behind because you haven't fed the insincerity machine

**原文标题**: You are falling behind because you haven't fed the insincerity machine

**原文链接**: [https://christianheilmann.com/2026/03/28/you-are-falling-behind-because-you-havent-fed-the-insincerity-machine-in-the-last-5-minutes/](https://christianheilmann.com/2026/03/28/you-are-falling-behind-because-you-havent-fed-the-insincerity-machine-in-the-last-5-minutes/)

生成摘要时出错

---

## 17. I am definitely missing the pre-AI writing era

**原文标题**: I am definitely missing the pre-AI writing era

**原文链接**: [https://www.lesswrong.com/posts/BJ4pnropWdnzzgeJc/i-am-definitely-missing-the-pre-ai-writing-era](https://www.lesswrong.com/posts/BJ4pnropWdnzzgeJc/i-am-definitely-missing-the-pre-ai-writing-era)

生成摘要时出错

---

## 18. Proactively Parasocial

**原文标题**: Proactively Parasocial

**原文链接**: [https://nicklandolfi.com/posts/proactively-parasocial.html](https://nicklandolfi.com/posts/proactively-parasocial.html)

生成摘要时出错

---

## 19. Hamilton-Jacobi-Bellman Equation: Reinforcement Learning and Diffusion Models

**原文标题**: Hamilton-Jacobi-Bellman Equation: Reinforcement Learning and Diffusion Models

**原文链接**: [https://dani2442.github.io/posts/continuous-rl/](https://dani2442.github.io/posts/continuous-rl/)

生成摘要时出错

---

## 20. Voyager 1 runs on 69 KB of memory and an 8-track tape recorder

**原文标题**: Voyager 1 runs on 69 KB of memory and an 8-track tape recorder

**原文链接**: [https://techfixated.com/a-1977-time-capsule-voyager-1-runs-on-69-kb-of-memory-and-an-8-track-tape-recorder-4/](https://techfixated.com/a-1977-time-capsule-voyager-1-runs-on-69-kb-of-memory-and-an-8-track-tape-recorder-4/)

生成摘要时出错

---

## 21. Comprehensive C++ Hashmap Benchmarks (2022)

**原文标题**: Comprehensive C++ Hashmap Benchmarks (2022)

**原文链接**: [https://martin.ankerl.com/2022/08/27/hashmap-bench-01/](https://martin.ankerl.com/2022/08/27/hashmap-bench-01/)

生成摘要时出错

---

## 22. Copilot edited an ad into my PR

**原文标题**: Copilot edited an ad into my PR

**原文链接**: [https://notes.zachmanson.com/copilot-edited-an-ad-into-my-pr/](https://notes.zachmanson.com/copilot-edited-an-ad-into-my-pr/)

生成摘要时出错

---

## 23. VHDL's Crown Jewel

**原文标题**: VHDL's Crown Jewel

**原文链接**: [https://www.sigasi.com/opinion/jan/vhdls-crown-jewel/](https://www.sigasi.com/opinion/jan/vhdls-crown-jewel/)

生成摘要时出错

---

## 24. 15 Years of Forking

**原文标题**: 15 Years of Forking

**原文链接**: [https://www.waterfox.com/blog/15-years-of-forking/](https://www.waterfox.com/blog/15-years-of-forking/)

生成摘要时出错

---

## 25. DigitalOcean Seeks $800M in Funding

**原文标题**: DigitalOcean Seeks $800M in Funding

**原文链接**: [https://www.datacenterdynamics.com/en/news/digitalocean-seeks-800m-in-funding/](https://www.datacenterdynamics.com/en/news/digitalocean-seeks-800m-in-funding/)

生成摘要时出错

---

## 26. Ninja is a small build system with a focus on speed

**原文标题**: Ninja is a small build system with a focus on speed

**原文链接**: [https://github.com/ninja-build/ninja](https://github.com/ninja-build/ninja)

生成摘要时出错

---

## 27. C++26 is done: ISO C++ standards meeting Trip Report

**原文标题**: C++26 is done: ISO C++ standards meeting Trip Report

**原文链接**: [https://herbsutter.com/2026/03/29/c26-is-done-trip-report-march-2026-iso-c-standards-meeting-london-croydon-uk/](https://herbsutter.com/2026/03/29/c26-is-done-trip-report-march-2026-iso-c-standards-meeting-london-croydon-uk/)

生成摘要时出错

---

## 28. Douglas Lenat's Automated Mathematician Source Code

**原文标题**: Douglas Lenat's Automated Mathematician Source Code

**原文链接**: [https://github.com/white-flame/am](https://github.com/white-flame/am)

生成摘要时出错

---

## 29. Hardware Image Compression

**原文标题**: Hardware Image Compression

**原文链接**: [https://www.ludicon.com/castano/blog/2026/03/hardware-image-compression/](https://www.ludicon.com/castano/blog/2026/03/hardware-image-compression/)

生成摘要时出错

---

## 30. My MacBook keyboard is broken and it's insanely expensive to fix

**原文标题**: My MacBook keyboard is broken and it's insanely expensive to fix

**原文链接**: [https://tobiasberg.net/posts/my-macbook-keyboard-is-broken-and-its-insanely-expensive-to-fix/](https://tobiasberg.net/posts/my-macbook-keyboard-is-broken-and-its-insanely-expensive-to-fix/)

生成摘要时出错

---

## 31. My MacBook keyboard is broken and it's insanely expensive to fix

**原文标题**: My MacBook keyboard is broken and it's insanely expensive to fix

**原文链接**: [https://tobiasberg.net/posts/my-macbook-keyboard-is-broken-and-its-insanely-expensive-to-fix/](https://tobiasberg.net/posts/my-macbook-keyboard-is-broken-and-its-insanely-expensive-to-fix/)

生成摘要时出错

---

## 32. Pretext: TypeScript library for multiline text measurement and layout

**原文标题**: Pretext: TypeScript library for multiline text measurement and layout

**原文链接**: [https://github.com/chenglou/pretext](https://github.com/chenglou/pretext)

生成摘要时出错

---

## 33. Coding agents could make free software matter again

**原文标题**: Coding agents could make free software matter again

**原文链接**: [https://www.gjlondon.com/blog/ai-agents-could-make-free-software-matter-again/](https://www.gjlondon.com/blog/ai-agents-could-make-free-software-matter-again/)

生成摘要时出错

---

## 34. Philly courts will ban all smart eyeglasses starting next week

**原文标题**: Philly courts will ban all smart eyeglasses starting next week

**原文链接**: [https://www.inquirer.com/news/philadelphia/smart-glasses-ai-meta-courts-20260326.html](https://www.inquirer.com/news/philadelphia/smart-glasses-ai-meta-courts-20260326.html)

生成摘要时出错

---

## 35. Spain shuts airspace for US planes involved in Iran war

**原文标题**: Spain shuts airspace for US planes involved in Iran war

**原文链接**: [https://english.aawsat.com/world/5256772-spain-shuts-airspace-us-planes-involved-iran-war](https://english.aawsat.com/world/5256772-spain-shuts-airspace-us-planes-involved-iran-war)

生成摘要时出错

---

## 36. The First Video Game Was Just a Box in the Corner of a Bar

**原文标题**: The First Video Game Was Just a Box in the Corner of a Bar

**原文链接**: [https://lithub.com/the-very-first-video-game-was-just-a-box-in-the-corner-of-a-bar/](https://lithub.com/the-very-first-video-game-was-just-a-box-in-the-corner-of-a-bar/)

生成摘要时出错

---

## 37. The ladder is missing rungs – Engineering Progression When AI Ate the Middle

**原文标题**: The ladder is missing rungs – Engineering Progression When AI Ate the Middle

**原文链接**: [https://negroniventurestudios.com/2026/03/19/the-ladder-is-missing-rungs/](https://negroniventurestudios.com/2026/03/19/the-ladder-is-missing-rungs/)

生成摘要时出错

---

## 38. Midnight train from GA: A view of America from the tracks as airports struggle

**原文标题**: Midnight train from GA: A view of America from the tracks as airports struggle

**原文链接**: [https://apnews.com/article/airports-shutdown-long-lines-train-travel-amtrak-e4d8ea591b3b036142c2bf2dee7dff5a](https://apnews.com/article/airports-shutdown-long-lines-train-travel-amtrak-e4d8ea591b3b036142c2bf2dee7dff5a)

生成摘要时出错

---

## 39. In Math, Rigor Is Vital. But Are Digitized Proofs Taking It Too Far?

**原文标题**: In Math, Rigor Is Vital. But Are Digitized Proofs Taking It Too Far?

**原文链接**: [https://www.quantamagazine.org/in-math-rigor-is-vital-but-are-digitized-proofs-taking-it-too-far-20260325/](https://www.quantamagazine.org/in-math-rigor-is-vital-but-are-digitized-proofs-taking-it-too-far-20260325/)

生成摘要时出错

---

## 40. Euro-Office Wants to Replace Google Docs and Microsoft Office

**原文标题**: Euro-Office Wants to Replace Google Docs and Microsoft Office

**原文链接**: [https://www.howtogeek.com/this-new-open-source-web-editor-wants-to-replace-google-docs-and-microsoft-office/](https://www.howtogeek.com/this-new-open-source-web-editor-wants-to-replace-google-docs-and-microsoft-office/)

生成摘要时出错

---

## 41. Bitwarden integrates with OneCLI agent vault

**原文标题**: Bitwarden integrates with OneCLI agent vault

**原文链接**: [https://www.onecli.sh/blog/bitwarden-agent-access-sdk-onecli](https://www.onecli.sh/blog/bitwarden-agent-access-sdk-onecli)

生成摘要时出错

---

## 42. 2026 is the year that decides whether the open web will survive

**原文标题**: 2026 is the year that decides whether the open web will survive

**原文链接**: [https://www.anildash.com/2026/03/27/endgame-open-web/](https://www.anildash.com/2026/03/27/endgame-open-web/)

生成摘要时出错

---

## 43. Senators want datacenters to come clean on power consumption

**原文标题**: Senators want datacenters to come clean on power consumption

**原文链接**: [https://www.theregister.com/2026/03/27/senators_datacenter_power_consumption/](https://www.theregister.com/2026/03/27/senators_datacenter_power_consumption/)

生成摘要时出错

---

## 44. 15 years, one server, 8GB RAM and 500k users – how Webminal refuses to die

**原文标题**: 15 years, one server, 8GB RAM and 500k users – how Webminal refuses to die

**原文链接**: [https://community.webminal.org/t/15-years-one-server-8gb-ram-and-500k-users-how-webminal-refuses-to-die/8803](https://community.webminal.org/t/15-years-one-server-8gb-ram-and-500k-users-how-webminal-refuses-to-die/8803)

生成摘要时出错

---

## 45. The Cognitive Dark Forest

**原文标题**: The Cognitive Dark Forest

**原文链接**: [https://ryelang.org/blog/posts/cognitive-dark-forest/](https://ryelang.org/blog/posts/cognitive-dark-forest/)

生成摘要时出错

---

## 46. The road signs that teach travellers about France

**原文标题**: The road signs that teach travellers about France

**原文链接**: [https://www.bbc.com/travel/article/20260327-the-road-signs-that-teach-travellers-about-france](https://www.bbc.com/travel/article/20260327-the-road-signs-that-teach-travellers-about-france)

生成摘要时出错

---

## 47. Spring Boot Done Right: Lessons from a 400-Module Codebase

**原文标题**: Spring Boot Done Right: Lessons from a 400-Module Codebase

**原文链接**: [https://medium.com/all-things-software/spring-boot-done-right-lessons-from-a-400-module-codebase-e636c3c34149](https://medium.com/all-things-software/spring-boot-done-right-lessons-from-a-400-module-codebase-e636c3c34149)

生成摘要时出错

---

## 48. "Roadrunner": a bipedal, wheeled robot for multi-modal locomotion [video]

**原文标题**: "Roadrunner": a bipedal, wheeled robot for multi-modal locomotion [video]

**原文链接**: [https://www.youtube.com/watch?v=9kae-UAME1U](https://www.youtube.com/watch?v=9kae-UAME1U)

生成摘要时出错

---

## 49. How the AI Bubble Bursts

**原文标题**: How the AI Bubble Bursts

**原文链接**: [https://martinvol.pe/blog/2026/03/30/how-the-ai-bubble-bursts/](https://martinvol.pe/blog/2026/03/30/how-the-ai-bubble-bursts/)

生成摘要时出错

---

## 50. OpenClaw: The Complete 2026 Deep Dive(Install, Cost, Hardware, Reviews and More)

**原文标题**: OpenClaw: The Complete 2026 Deep Dive(Install, Cost, Hardware, Reviews and More)

**原文链接**: [https://virtualuncle.com/openclaw-complete-guide-2026/](https://virtualuncle.com/openclaw-complete-guide-2026/)

生成摘要时出错

---

## 51. How A Spartan Revolutionized Baseball

**原文标题**: How A Spartan Revolutionized Baseball

**原文链接**: [https://msutoday.msu.edu/news/2026/03/spartan-revolutionize-baseball](https://msutoday.msu.edu/news/2026/03/spartan-revolutionize-baseball)

生成摘要时出错

---

## 52. Interview: Nobonoko, Master of the Minimal Sequencer

**原文标题**: Interview: Nobonoko, Master of the Minimal Sequencer

**原文链接**: [https://fi-le.net/nobo/](https://fi-le.net/nobo/)

生成摘要时出错

---

## 53. 72% of the dollar's purchasing power was destroyed in just four episodes

**原文标题**: 72% of the dollar's purchasing power was destroyed in just four episodes

**原文链接**: [https://eco3min.fr/en/us-inflation-is-not-linear/](https://eco3min.fr/en/us-inflation-is-not-linear/)

生成摘要时出错

---

## 54. Miasma: A tool to trap AI web scrapers in an endless poison pit

**原文标题**: Miasma: A tool to trap AI web scrapers in an endless poison pit

**原文链接**: [https://github.com/austin-weeks/miasma](https://github.com/austin-weeks/miasma)

生成摘要时出错

---

## 55. Show HN: The Alphabetical Clock

**原文标题**: Show HN: The Alphabetical Clock

**原文链接**: [https://boat.horse/clock/](https://boat.horse/clock/)

**The Alphabetical Clock** (also titled "The Accursèd Alphabetical Clock") is a creative timekeeping project inspired by a Mastodon post. Instead of following a traditional chronological sequence, this clock organizes time based on the alphabetical spelling of its English components.

The project features two distinct modes:

*   **Three-Hand Mode:** The hours, minutes, and seconds are treated as independent units. Each category is sorted alphabetically by its name, with three separate hands indicating the current time according to this non-numerical order.
*   **Combined Mode:** This mode spells out every one of the 43,200 possible times in a 12-hour cycle. The entire list is then sorted alphabetically, and a single needle points to the current time’s position within that massive, sorted sequence.

Essentially, the clock recontextualizes time as a linguistic data set rather than a linear progression, offering a whimsical and "cursed" alternative to standard watches.

---

## 56. The RISE RISC-V Runners: free, native RISC-V CI on GitHub

**原文标题**: The RISE RISC-V Runners: free, native RISC-V CI on GitHub

**原文链接**: [https://riseproject.dev/2026/03/24/announcing-the-rise-risc-v-runners-free-native-risc-v-ci-on-github/](https://riseproject.dev/2026/03/24/announcing-the-rise-risc-v-runners-free-native-risc-v-ci-on-github/)

生成摘要时出错

---

## 57. Nitrile and latex gloves may cause overestimation of microplastics

**原文标题**: Nitrile and latex gloves may cause overestimation of microplastics

**原文链接**: [https://news.umich.edu/nitrile-and-latex-gloves-may-cause-overestimation-of-microplastics-u-m-study-reveals/](https://news.umich.edu/nitrile-and-latex-gloves-may-cause-overestimation-of-microplastics-u-m-study-reveals/)

生成摘要时出错

---

## 58. The sudden fall of Sora

**原文标题**: The sudden fall of Sora

**原文链接**: [https://www.wsj.com/tech/ai/the-sudden-fall-of-openais-most-hyped-product-since-chatgpt-64c730c9](https://www.wsj.com/tech/ai/the-sudden-fall-of-openais-most-hyped-product-since-chatgpt-64c730c9)

生成摘要时出错

---

## 59. Stanford study reveals AI vision models invent images they never see

**原文标题**: Stanford study reveals AI vision models invent images they never see

**原文链接**: [https://arxiv.org/abs/2603.21687](https://arxiv.org/abs/2603.21687)

生成摘要时出错

---

## 60. Hackers now exploit critical F5 BIG-IP flaw in attacks, patch now

**原文标题**: Hackers now exploit critical F5 BIG-IP flaw in attacks, patch now

**原文链接**: [https://www.bleepingcomputer.com/news/security/hackers-now-exploit-critical-f5-big-ip-flaw-in-attacks-patch-now/](https://www.bleepingcomputer.com/news/security/hackers-now-exploit-critical-f5-big-ip-flaw-in-attacks-patch-now/)

生成摘要时出错

---

## 61. More on Version Control

**原文标题**: More on Version Control

**原文链接**: [https://bramcohen.com/p/more-on-version-control](https://bramcohen.com/p/more-on-version-control)

生成摘要时出错

---

## 62. About the Atmosphere

**原文标题**: About the Atmosphere

**原文链接**: [https://toni.org/2026/03/27/about-the-atmosphere/](https://toni.org/2026/03/27/about-the-atmosphere/)

生成摘要时出错

---

## 63. Kyushu Railway Company Train Varieties

**原文标题**: Kyushu Railway Company Train Varieties

**原文链接**: [https://www.jrkyushu.co.jp/english/train/index.html](https://www.jrkyushu.co.jp/english/train/index.html)

生成摘要时出错

---

## 64. Eclipse GlassFish: This Isn't Your Father's GlassFish

**原文标题**: Eclipse GlassFish: This Isn't Your Father's GlassFish

**原文链接**: [https://foojay.io/today/eclipse-glassfish-this-isnt-your-fathers-glassfish/](https://foojay.io/today/eclipse-glassfish-this-isnt-your-fathers-glassfish/)

生成摘要时出错

---

## 65. Founder of GitLab battles cancer by founding companies

**原文标题**: Founder of GitLab battles cancer by founding companies

**原文链接**: [https://sytse.com/cancer/](https://sytse.com/cancer/)

生成摘要时出错

---

## 66. InpharmD (YC W21) Is Hiring – Senior Ruby on Rails Developer

**原文标题**: InpharmD (YC W21) Is Hiring – Senior Ruby on Rails Developer

**原文链接**: [https://inpharmd.com/jobs/senior-ruby-on-rails-engineer](https://inpharmd.com/jobs/senior-ruby-on-rails-engineer)

生成摘要时出错

---

## 67. The rise and fall of IBM's 4 Pi aerospace computers: an illustrated history

**原文标题**: The rise and fall of IBM's 4 Pi aerospace computers: an illustrated history

**原文链接**: [https://www.righto.com/2026/03/ibm-4-pi-computer-history.html](https://www.righto.com/2026/03/ibm-4-pi-computer-history.html)

生成摘要时出错

---

## 68. Ohm's Peg-to-WASM Compiler

**原文标题**: Ohm's Peg-to-WASM Compiler

**原文链接**: [https://ohmjs.org/blog/2026/03/12/peg-to-wasm](https://ohmjs.org/blog/2026/03/12/peg-to-wasm)

生成摘要时出错

---

## 69. Gonon: Building a Clock with No Numerals

**原文标题**: Gonon: Building a Clock with No Numerals

**原文链接**: [https://tonygaeta.com/perceptor/code/gonon](https://tonygaeta.com/perceptor/code/gonon)

生成摘要时出错

---

## 70. Neovim 0.12.0

**原文标题**: Neovim 0.12.0

**原文链接**: [https://github.com/neovim/neovim/releases/tag/v0.12.0](https://github.com/neovim/neovim/releases/tag/v0.12.0)

生成摘要时出错

---

## 71. Police used AI facial recognition to wrongly arrest TN woman for crimes in ND

**原文标题**: Police used AI facial recognition to wrongly arrest TN woman for crimes in ND

**原文链接**: [https://www.cnn.com/2026/03/29/us/angela-lipps-ai-facial-recognition](https://www.cnn.com/2026/03/29/us/angela-lipps-ai-facial-recognition)

生成摘要时出错

---

## 72. Creating West Coast Buddhism (2024)

**原文标题**: Creating West Coast Buddhism (2024)

**原文链接**: [https://letter.palladiummag.com/p/creating-west-coast-buddhism](https://letter.palladiummag.com/p/creating-west-coast-buddhism)

生成摘要时出错

---

## 73. Show HN: QuickBEAM – run JavaScript as supervised Erlang/OTP processes

**原文标题**: Show HN: QuickBEAM – run JavaScript as supervised Erlang/OTP processes

**原文链接**: [https://github.com/elixir-volt/quickbeam](https://github.com/elixir-volt/quickbeam)

生成摘要时出错

---

## 74. HD Audio Driver for Windows 98SE / Me

**原文标题**: HD Audio Driver for Windows 98SE / Me

**原文链接**: [https://github.com/andrew-hoffman/wdmhda](https://github.com/andrew-hoffman/wdmhda)

生成摘要时出错

---

## 75. I'll buy your electronics to feed our robot

**原文标题**: I'll buy your electronics to feed our robot

**原文链接**: [https://www.dayworkx.com/](https://www.dayworkx.com/)

生成摘要时出错

---

## 76. AI overly affirms users asking for personal advice

**原文标题**: AI overly affirms users asking for personal advice

**原文链接**: [https://news.stanford.edu/stories/2026/03/ai-advice-sycophantic-models-research](https://news.stanford.edu/stories/2026/03/ai-advice-sycophantic-models-research)

生成摘要时出错

---

## 77. Full network of clitoral nerves mapped out for first time

**原文标题**: Full network of clitoral nerves mapped out for first time

**原文链接**: [https://www.theguardian.com/society/2026/mar/29/full-network-clitoral-nerves-mapped-out-first-time-women-pelvic-surgery](https://www.theguardian.com/society/2026/mar/29/full-network-clitoral-nerves-mapped-out-first-time-women-pelvic-surgery)

生成摘要时出错

---

## 78. Show HN: Crazierl – An Erlang Operating System

**原文标题**: Show HN: Crazierl – An Erlang Operating System

**原文链接**: [https://crazierl.org/demo/](https://crazierl.org/demo/)

生成摘要时出错

---

## 79. Observations from carbon dioxide monitoring

**原文标题**: Observations from carbon dioxide monitoring

**原文链接**: [https://grieve-smith.com/ftn/2026/03/nine-observations-from-carbon-dioxide-monitoring/](https://grieve-smith.com/ftn/2026/03/nine-observations-from-carbon-dioxide-monitoring/)

生成摘要时出错

---

## 80. AyaFlow: A high-performance, eBPF-based network traffic analyzer written in Rust

**原文标题**: AyaFlow: A high-performance, eBPF-based network traffic analyzer written in Rust

**原文链接**: [https://github.com/DavidHavoc/ayaFlow](https://github.com/DavidHavoc/ayaFlow)

生成摘要时出错

---

## 81. Show HN: Create a full language server in Go with 3.17 spec support

**原文标题**: Show HN: Create a full language server in Go with 3.17 spec support

**原文链接**: [https://github.com/owenrumney/go-lsp](https://github.com/owenrumney/go-lsp)

生成摘要时出错

---

## 82. Stripe is down

**原文标题**: Stripe is down

**原文链接**: [https://status.stripe.com/](https://status.stripe.com/)

生成摘要时出错

---

## 83. When do we become adults, really?

**原文标题**: When do we become adults, really?

**原文链接**: [https://www.newyorker.com/culture/annals-of-inquiry/when-do-we-become-adults-really](https://www.newyorker.com/culture/annals-of-inquiry/when-do-we-become-adults-really)

生成摘要时出错

---

## 84. Cuts in publishing and book reviewing imperil the future of narrative nonfiction

**原文标题**: Cuts in publishing and book reviewing imperil the future of narrative nonfiction

**原文链接**: [https://newrepublic.com/article/207659/non-fiction-publishing-threat-important-ever](https://newrepublic.com/article/207659/non-fiction-publishing-threat-important-ever)

生成摘要时出错

---

## 85. Typing and Keyboards

**原文标题**: Typing and Keyboards

**原文链接**: [https://lzon.ca/posts/series/grateful/typing-and-keyboards/](https://lzon.ca/posts/series/grateful/typing-and-keyboards/)

生成摘要时出错

---

## 86. Show HN: Sheet Ninja – Google Sheets as a CRUD Back End for Vibe Coders

**原文标题**: Show HN: Sheet Ninja – Google Sheets as a CRUD Back End for Vibe Coders

**原文链接**: [https://sheetninja.io](https://sheetninja.io)

生成摘要时出错

---

## 87. The loneliness of A Room of One’s Own

**原文标题**: The loneliness of A Room of One’s Own

**原文链接**: [https://newrepublic.com/article/206731/loneliness-room-one-virginia-woolf-hold-up](https://newrepublic.com/article/206731/loneliness-room-one-virginia-woolf-hold-up)

生成摘要时出错

---

## 88. A Verilog to Factorio Compiler and Simulator (Working RISC-V CPU)

**原文标题**: A Verilog to Factorio Compiler and Simulator (Working RISC-V CPU)

**原文链接**: [https://github.com/ben-j-c/verilog2factorio](https://github.com/ben-j-c/verilog2factorio)

生成摘要时出错

---

## 89. Iran-linked hackers breach FBI director's personal email

**原文标题**: Iran-linked hackers breach FBI director's personal email

**原文链接**: [https://www.reuters.com/world/us/iran-linked-hackers-claim-breach-of-fbi-directors-personal-email-doj-official-2026-03-27/](https://www.reuters.com/world/us/iran-linked-hackers-claim-breach-of-fbi-directors-personal-email-doj-official-2026-03-27/)

生成摘要时出错

---

## 90. CSS is DOOMed

**原文标题**: CSS is DOOMed

**原文链接**: [https://nielsleenheer.com/articles/2026/css-is-doomed-rendering-doom-in-3d-with-css/](https://nielsleenheer.com/articles/2026/css-is-doomed-rendering-doom-in-3d-with-css/)

生成摘要时出错

---

## 91. How to Survive in the Tech industry in 2026

**原文标题**: How to Survive in the Tech industry in 2026

**原文链接**: [https://blog.phuaxueyong.com/post/2026-03-23-how-to-survive-tech-in-2026/](https://blog.phuaxueyong.com/post/2026-03-23-how-to-survive-tech-in-2026/)

生成摘要时出错

---

## 92. Show HN: BreezePDF – Free, in-browser PDF editor

**原文标题**: Show HN: BreezePDF – Free, in-browser PDF editor

**原文链接**: [https://breezepdf.com/?v=3](https://breezepdf.com/?v=3)

生成摘要时出错

---

## 93. New Apple Silicon M4 and M5 HiDPI Limitation on 4K External Displays

**原文标题**: New Apple Silicon M4 and M5 HiDPI Limitation on 4K External Displays

**原文链接**: [https://smcleod.net/2026/03/new-apple-silicon-m4-m5-hidpi-limitation-on-4k-external-displays/](https://smcleod.net/2026/03/new-apple-silicon-m4-m5-hidpi-limitation-on-4k-external-displays/)

生成摘要时出错

---

## 94. Running Tesla Model 3's computer on my desk using parts from crashed cars

**原文标题**: Running Tesla Model 3's computer on my desk using parts from crashed cars

**原文链接**: [https://bugs.xdavidhu.me/tesla/2026/03/23/running-tesla-model-3s-computer-on-my-desk-using-parts-from-crashed-cars/](https://bugs.xdavidhu.me/tesla/2026/03/23/running-tesla-model-3s-computer-on-my-desk-using-parts-from-crashed-cars/)

生成摘要时出错

---

## 95. A nearly perfect USB cable tester

**原文标题**: A nearly perfect USB cable tester

**原文链接**: [https://blog.literarily-starved.com/2026/02/technology-the-nearly-perfect-usb-cable-tester-does-exist/](https://blog.literarily-starved.com/2026/02/technology-the-nearly-perfect-usb-cable-tester-does-exist/)

生成摘要时出错

---

## 96. Show HN: I made a "programming language" looking for feedback

**原文标题**: Show HN: I made a "programming language" looking for feedback

**原文链接**: [https://github.com/alonsovm44/glupe](https://github.com/alonsovm44/glupe)

生成摘要时出错

---

## 97. Quantum frontiers may be closer than they appear

**原文标题**: Quantum frontiers may be closer than they appear

**原文链接**: [https://blog.google/innovation-and-ai/technology/safety-security/cryptography-migration-timeline/](https://blog.google/innovation-and-ai/technology/safety-security/cryptography-migration-timeline/)

生成摘要时出错

---

## 98. The Failure of the Thermodynamics of Computation (2010)

**原文标题**: The Failure of the Thermodynamics of Computation (2010)

**原文链接**: [https://sites.pitt.edu/~jdnorton/Goodies/Idealization/index.html](https://sites.pitt.edu/~jdnorton/Goodies/Idealization/index.html)

生成摘要时出错

---

## 99. Siclair Microvision (1977)

**原文标题**: Siclair Microvision (1977)

**原文链接**: [https://r-type.org/articles/art-452.htm](https://r-type.org/articles/art-452.htm)

生成摘要时出错

---

## 100. I turned my Kindle into my own personal newspaper

**原文标题**: I turned my Kindle into my own personal newspaper

**原文链接**: [https://manualdousuario.net/en/how-to-kindle-personal-newspaper/](https://manualdousuario.net/en/how-to-kindle-personal-newspaper/)

生成摘要时出错

---

