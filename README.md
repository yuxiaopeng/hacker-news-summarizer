# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-12-26.md)

*最后自动更新时间: 2025-12-26 17:46:01*
## 1. 包管理器总把 Git 当作数据库，但这从来行不通。

**原文标题**: Package managers keep using Git as a database, it never works out

**原文链接**: [https://nesbitt.io/2025/12/24/package-managers-keep-using-git-as-a-database.html](https://nesbitt.io/2025/12/24/package-managers-keep-using-git-as-a-database.html)

文章指出，将 Git 用作软件包注册表的数据库是一个反复出现的错误，随着项目规模的扩大，这种做法必然会失败。虽然由于内置版本控制、GitHub 的免费托管以及熟悉的工作流程，这种方式最初极具吸引力，但基于 Git 的索引最终会成为性能瓶颈。

作者重点介绍了几个“从 Git 到 HTTP”演进的典型案例：
* **Cargo、Homebrew 和 CocoaPods：** 最初都依赖于通过克隆 Git 仓库来获取索引。随着这些项目的增长，用户面临着海量的下载和缓慢的“增量解析”。这三者最终都转向了稀疏 HTTP 协议、JSON 下载或 CDN，以实现按需提供元数据。
* **Go：** 转向了 `GOPROXY`，以避免 `go get` 为了查找单个元数据文件而不得不克隆整个仓库，这也解决了有关版本控制工具的安全考量。
* **Nixpkgs 和 vcpkg：** 它们目前仍与 Git 深度绑定。Nixpkgs 由于体积庞大，正处于对 GitHub 基础设施的压力测试中；而 vcpkg 的架构依赖于特定的 Git 树哈希进行版本控制，因此很难摆脱完整克隆。

根本问题在于**文件系统作为数据库的表现极差**。Git 继承了文件系统的局限性，例如目录大小限制（被迫进行手动分片）、路径长度限制以及大小写敏感性问题。此外，Git 缺乏原生数据库的功能，如用于快速查询的索引、CHECK 约束和高效的锁定机制。

文章总结道，虽然 Git 非常适合分布式源代码协作，但它并不适合作为软件包注册表的工具。包管理器需要针对元数据的快速点查询，而 Git 提供的是全文档同步协议。作者敦促开发人员从一开始就使用真正的数据库或基于 HTTP 的解决方案，以避免基于 Git 索引所带来的必然的技术债。

---

## 2. C/C++ 嵌入式文件

**原文标题**: C/C++ Embedded Files

**原文链接**: [https://www.4rknova.com//blog/2013/01/27/cpp-embedded-files](https://www.4rknova.com//blog/2013/01/27/cpp-embedded-files)

本文概述了将资源文件直接嵌入 C/C++ 二进制程序的三种主要方法。该技术通过消除外部文件依赖，简化了软件的分发。

**1. 外部转换工具**
最常用的方法是使用命令行工具将原始文件转换为包含字节数组的 C 头文件。
*   **ImageMagick：** 适用于将图像转换为兼容头文件的格式。
*   **xxd：** 一款通用工具，可将任何类型的文件生成十六进制转储并存入 C 风格数组中。
虽然这种方法很有效，但它在构建过程中增加了额外的依赖项。

**2. 预处理器法**
该方法特别适用于 ASCII 文件（如着色器），它使用 `STRINGIFY` 宏将文件内容转换为字符串字面量。通过将外部文件内容包裹在宏中并使用 `#include` 指令，预处理器即可处理嵌入过程。其主要缺点是必须手动编辑资源文件以添加宏包装器。

**3. 汇编法 (ASM)**
开发人员可以使用带有 `.incbin` 指令的内联汇编，将数据直接放置在二进制文件的 `.rodata` 段中。这种方法允许程序员为数据的起始和结束点定义全局符号，从而便于在运行时计算文件大小并访问字节。虽然这种方法避免了外部转换工具和手动文件编辑，但它具有平台特定性，缺乏其他方法的移植性。

**结论**
每种方法都各有利弊：外部工具具有通用性，但会使构建链复杂化；预处理器技巧简单，但仅限于文本；而汇编法虽然高效，但受限于特定的架构或编译器。

---

## 3. Learnix 操作系统

**原文标题**: LearnixOS

**原文链接**: [https://www.learnix-os.com](https://www.learnix-os.com)

**LearnixOS** 是一个教育项目及书籍，致力于使用 Rust 编程语言从零开始构建一个符合 POSIX 标准的操作系统。作者秉持“只有能深入浅出地解释复杂话题，才算真正理解”的哲学，记录了从最初构思到最终实现的整个开发过程。

该项目强调自力更生，除了用于减少少量模板代码的库之外，尽量避免使用外部库。虽然内容具有技术性，但其设计初衷是让具备基础编程背景的读者也能读懂。读者仅需对汇编（基础算术和移动操作）以及内存概念（如指针和地址）有初步了解。本书不要求预先精通 Rust，因为相关语言特性会在开发过程中得到详细讲解。

**开发路线图遵循以下逻辑演进：**
1.  **基础：** 编译独立二进制文件，处理引导加载（bootloading）和 CPU 模式。
2.  **内存与中断：** 实现分页、创建自定义 `malloc` 函数，并利用中断描述符表 (IDT)。
3.  **系统与存储：** 开发文件系统、磁盘驱动程序和进程管理。
4.  **用户界面：** 编写 Shell 并运行首个程序 (Doom)。
5.  **未来目标：** 探索虚拟化及加载其他操作系统。

作者还强调了代码段使用了自定义语法高亮，并鼓励社区通过提交 Issue 和反馈进行互动，以确保内容的清晰与准确。

---

## 4. Show HN：具备模拟受众功能的私密博客与日记

**原文标题**: Show HN: Private blogging and journaling with a simulated audience

**原文链接**: [https://tempblog-psi.vercel.app/](https://tempblog-psi.vercel.app/)

本文介绍了一款专为私人博客和日志设计的全新开源工具，其核心特色是**模拟受众**。该项目旨在提供面向读者写作的心理益处，同时确保内容保持完全私密。

该项目的核心要点包括：

*   **模拟受众**：该平台营造了一个让用户仿佛在公共空间发帖的环境，但其“受众”是虚构的，从而在无需公开暴露的情况下实现创意表达。
*   **隐私与控制**：该工具强调数据所有权。它采用**自托管**设计，赋予用户对其实例和信息的完全控制权。
*   **现代技术栈**：该应用基于全栈 React 框架 **TanStack Start** 构建，可作为对该生态系统感兴趣的开发者的入门模板。
*   **可用性**：项目已开源并托管在 GitHub 上，允许他人查看代码、参与贡献或部署自己的版本。

总之，这是一款专注于隐私的日志解决方案，它将日记的私密性与博客的互动感结合在一起，并由现代 Web 技术提供动力。

---

## 5. Show HN: 用 Rust/WASM 编写的 AutoLISP 解释器 —— 一个诞生于 33 年前的 CAD 工作流

**原文标题**: Show HN: AutoLISP interpreter in Rust/WASM – a CAD workflow invented 33 yrs ago

**原文链接**: [https://acadlisp.de/noscript.html](https://acadlisp.de/noscript.html)

**acadlisp** 是一个采用 Rust 编写并编译为 WebAssembly (WASM) 的新型 AutoLISP 解释器，使用户无需安装 AutoCAD 即可直接在网页浏览器中运行 AutoLISP 代码。

该项目的灵感源自开发者于 1991 年为巴伐利亚一家电气公司开发的工作流。通过结合 CSV 文件、模板和 LISP 代码，作者实现了复杂电气原理图生成的自动化。该系统利用了 LISP 独特的“同质像性”（homoiconic）——即代码与数据共享相同的结构——使程序能够在绘图过程中有效地实现自我编写和修改。

**核心技术细节：**
*   **语言与移植性：** 使用 Rust 和 WASM 构建，确保高性能与浏览器兼容性。
*   **输出格式：** 支持生成 SVG 和 DXF (AutoCAD R12/AC1009) 文件。
*   **功能：** 支持标准 AutoLISP 函数，包括 `defun`、`setq`、`while` 以及各种数学和符号处理命令。

创作者将该项目视为情怀与数字保存的结合，确保这项 30 多年前发明的专用 CAD 工作流在现代计算环境中依然能够运行。目前已提供交互式演示和完整源代码，供用户探索这种早期形式的“符号 AI”和 CAD 自动化。

---

## 6. 琼·狄迪恩与库尔特·冯内古特曾有话要说，我们存有录音。

**原文标题**: Joan Didion and Kurt Vonnegut had something to say. We have it on tape

**原文链接**: [https://www.nytimes.com/2025/12/19/books/james-baldwin-joan-didion-92ny-recordings.html](https://www.nytimes.com/2025/12/19/books/james-baldwin-joan-didion-92ny-recordings.html)

位于曼哈顿的第92街Y（92NY）正与美国国会图书馆合作，对其庞大的文学档案进行保护与数字化处理。该馆藏记录了昂特伯格诗歌中心（Unterberg Poetry Center）80多年来极具历史价值的朗诵会和对话。此次合作将妥善保存约1500份可追溯至1939年的录音资料。

该档案囊括了20世纪文学界的“名人录”，包括琼·迪迪安、库尔特·冯内古特、詹姆斯·鲍德温、T.S. 艾略特、兰斯顿·休斯和托妮·莫里森等传奇人物。与标准的有声读物不同，这些录音捕捉到了现场活动中原始且未经修饰的氛围，包括观众的反应、即兴的幽默以及充满智慧的问答环节。其中的亮点包括迪迪安探讨她的写作过程，以及鲍德温对艺术家社会角色的反思。

由于许多录音存储在开盘式磁带和盒式磁带等老化且脆弱的媒介上，面临损毁风险，因此该项目是一项至关重要的保护行动。通过将这些实物资料移交给美国国会图书馆，该馆藏将获得永久的归宿和专业级的修复。

最终，这一计划为人们建立了与已故作家之间最直观的联系，完整保留了他们独特的语调、个性和表演时的历史语境。这种数字化的回归确保了这些重要的文化里程碑能够惠及未来世世代代的学者和公众。

---

## 7. Unix "find" 表达式编译为字节码

**原文标题**: Unix "find" expressions compiled to bytecode

**原文链接**: [https://nullprogram.com/blog/2025/12/23/](https://nullprogram.com/blog/2025/12/23/)

在这篇文章中，作者详细介绍了一种将 Unix `find` 表达式编译为字节码的方法，该策略旨在最小化遍历大型文件系统时处理每个元素的工作量。虽然大多数标准实现（GNU、BSD、BusyBox）使用树遍历解释器，但作者发现基于字节码的方法实现起来却出奇地简单。

**字节码设计**
所提议的系统使用一个单寄存器机器（跟踪 1 位结果），具有五个主要操作码：
*   **`halt`**：停止程序。
*   **`not`**：寄存器取反。
*   **`braf` / `brat`**：“假跳转”和“真跳转”，用于短路逻辑。
*   **`action`**：执行特定的过滤器（例如 `-name` 或 `-type`）并设置寄存器。

**编译过程**
名为 `findc` 的编译器分两个阶段工作：
1.  **解析**：它使用调度场算法（Shunting-yard algorithm）将中缀表达式（如 `-type f -a -executable`）转换为后缀表达式。此阶段处理隐式运算符，移除括号，并在必要时确保添加默认操作（如 `-print`）。
2.  **生成**：一个基于栈的编译器将后缀标记转换为位置无关的字节码片段。逻辑运算符被转换为跳转指令：`-a`（与）在条件为假时使用 `braf` 跳过后续检查，而 `-o`（或）在条件为真时使用 `brat` 跳过。

**优化**
作者指出，虽然初步的编译器可以工作，但可以使用窥孔优化（peephole optimization）进一步完善输出。这包括扫描字节码以消除冗余的 `not-not` 序列，重定向跳转到其他跳转的指令，以及移除无副作用的指令。

最终，作者认为这种字节码方法是传统解释方式的高效且优雅的替代方案，能为复杂的文件搜索操作提供潜在的性能提升。

---

## 8. Maybe the default settings are too high

**原文标题**: Maybe the default settings are too high

**原文链接**: [https://www.raptitude.com/2025/12/maybe-the-default-settings-are-too-high/](https://www.raptitude.com/2025/12/maybe-the-default-settings-are-too-high/)

生成摘要时出错

---

## 9. High School Student Discovers 1.5M Potential New Astronomical Objects

**原文标题**: High School Student Discovers 1.5M Potential New Astronomical Objects

**原文链接**: [https://www.smithsonianmag.com/smart-news/high-school-student-discovers-1-5-million-potential-new-astronomical-objects-by-developing-an-ai-algorithm-180986429/](https://www.smithsonianmag.com/smart-news/high-school-student-discovers-1-5-million-potential-new-astronomical-objects-by-developing-an-ai-algorithm-180986429/)

生成摘要时出错

---

## 10. Show HN: Xcc700: Self-hosting mini C compiler for ESP32 (Xtensa) in 700 lines

**原文标题**: Show HN: Xcc700: Self-hosting mini C compiler for ESP32 (Xtensa) in 700 lines

**原文链接**: [https://github.com/valdanylchuk/xcc700](https://github.com/valdanylchuk/xcc700)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 2 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 3 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 4 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 5 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 6 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 7 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 8 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 9 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 10 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 11 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 12 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 13 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 14 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 15 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 16 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 17 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 18 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 19 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 20 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 21 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 22 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 23 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 24 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 25 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 26 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 27 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 28 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 29 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 30 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 31 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 32 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 33 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 34 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 35 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 36 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 37 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 38 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 39 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 40 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 41 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 42 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 43 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 44 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 45 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 46 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 47 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 48 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 49 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 50 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 51 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 52 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 53 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 54 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 55 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 56 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 57 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 58 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 59 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 60 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 61 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 62 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 63 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 64 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 65 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 66 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 67 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 68 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 69 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 70 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 71 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 72 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 73 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 74 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 75 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 76 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 77 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 78 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 79 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 80 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 81 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 82 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 83 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 84 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 85 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 86 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 87 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 88 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 89 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 90 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 91 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 92 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 93 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 94 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 95 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 96 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 97 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 98 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 99 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 100 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 101 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 102 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 103 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 104 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 105 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 106 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 107 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 108 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 109 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 110 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 111 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 112 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 113 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 114 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 115 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 116 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 117 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 118 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 119 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 120 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 121 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 122 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 123 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 124 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 125 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 126 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 127 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 128 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 129 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 130 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 131 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 132 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 133 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 134 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 135 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 136 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 137 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 138 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 139 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 140 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 141 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 142 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 143 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 144 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 145 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 146 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 147 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 148 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 149 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 150 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 151 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 152 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 153 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 154 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 155 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 156 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 157 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 158 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 159 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 160 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 161 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 162 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 163 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 164 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 165 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 166 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 167 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 168 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 169 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 170 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 171 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 172 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 173 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 174 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 175 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 176 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 177 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 178 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 179 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 180 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 181 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 182 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 183 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 184 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 185 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 186 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 187 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 188 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 189 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 190 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 191 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 192 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 193 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 194 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 195 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 196 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 197 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 198 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 199 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 200 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 201 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 202 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 203 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 204 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 205 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 206 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 207 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 208 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 209 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 210 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 211 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 212 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 213 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 214 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 215 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 216 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 217 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 218 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 219 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 220 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 221 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 222 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 223 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 224 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 225 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 226 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 227 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 228 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 229 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 230 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 231 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 232 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 233 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 234 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 235 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 236 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 237 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 238 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 239 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 240 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 241 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 242 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 243 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 244 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 245 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 246 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 247 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 248 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 249 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 250 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 251 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 252 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 253 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 254 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 255 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 256 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 257 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 258 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 259 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 260 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 261 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 262 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 263 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 264 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 265 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 266 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 267 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 268 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 269 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 270 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 271 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 272 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 273 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 274 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 275 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 276 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 277 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 278 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 279 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 280 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 281 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
