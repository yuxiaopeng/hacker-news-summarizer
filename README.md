# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-01-11.md)

*最后自动更新时间: 2026-01-11 17:46:31*
## 1. Gentoo Linux 2025 评测

**原文标题**: Gentoo Linux 2025 Review

**原文链接**: [https://www.gentoo.org/news/2026/01/05/new-year.html](https://www.gentoo.org/news/2026/01/05/new-year.html)

Gentoo Linux 2025 年度回顾重点介绍了这一年在技术改进、基础设施扩展和组织转型方面的进展。

**技术与软件包更新**
该发行版在 Portage 中完成了对 **EAPI 9** 的支持，并引入了多项重大的软件包改进。值得关注的新增功能包括：为 **GnuPG 提供商** 引入了新的 alternatives 机制、初步支持 **zlib-ng** 以及对 **NGINX** 进行了重大重构。为了简化自举（bootstrapping），Gentoo 为 **Rust** 增加了一条基于 C++ 的路径（通过 mrustc），并改进了 Ada 和 D 语言的路径。此外，该项目还引入了名为“**steve**”的全系统作业服务器，以更好地管理并行构建任务。

**架构与镜像**
Gentoo 通过发布每周更新的 **WSL 镜像** 和可启动的 **RISC-V QCOW2** 镜像扩大了其覆盖范围。然而，由于硬件稀缺，**hppa** 和 **sparc** 架构的关键字已从稳定（stable）降级为测试（testing）。

**社区与基础设施**
该项目迎来了四位新开发者，并维护着一个包含超过 31,000 个 ebuild 的庞大仓库。尽管提交和漏洞追踪活动较 2024 年略有下降，但 amd64 架构的二进制包容量已增长至 89GB。在一项重大政策转变中，Gentoo 宣布计划将其仓库镜像从 GitHub 迁移至 **Codeberg**，理由是担心 AI Copilot 的集成问题。基础设施方面也得到了加强，在德国新增了一台专用构建服务器，以加速镜像和二进制包的生成。

**治理与财务**
Gentoo 基金会继续将其财务迁移至 **Software in the Public Interest (SPI)**。该组织财务状况稳健，拥有超过 104,000 美元的资产，但仍继续敦促定期捐赠者将其捐款转移至 SPI 架构。

总体而言，2025 年的特点是现代化、对二进制便携性的关注度提升，以及对独立基础设施的坚定承诺。

---

## 2. KIM-1 50岁生日快乐

**原文标题**: Happy 50th Birthday KIM-1

**原文链接**: [https://github.com/netzherpes/KIM1-Demo](https://github.com/netzherpes/KIM1-Demo)

本文旨在庆祝 MOS KIM-1 诞生 50 周年。这款里程碑式的微型计算机于 1976 年 1 月发布。为纪念这一时刻，作者发起了“KIM-1 演示项目”（KIM-1 Demo Project），这是一个整合了来自多个代码库的各种软件组件和例程的协作倡议。

该项目向复古计算爱好者发出公开邀请，欢迎大家贡献模块、改进方案和新演示，旨在将早期计算精神延续至 2026 年。

文中很大一部分篇幅专注于一个实际的技术挑战：ANSI 终端光标定位。作者提供了一段 6502 汇编代码片段，其中包含两个关键子程序：

*   **GOTOXY：** 该程序向终端发送标准 ANSI 转义序列（`ESC[row;colH`）以定位光标。
*   **PUTDEC：** 该工具解决了将原始十六进制数据（0–99）转换为独立十进制 ASCII 字符的难题。例如，如果坐标存储为 `$20`（十进制 32），`PUTDEC` 会分别提取出“3”和“2”，以便将其传输至终端。

通过将内存值转换为屏幕坐标，这种逻辑使开发人员能够在 KIM-1 上创建矩形、圆形甚至绘图程序等视觉元素。总的来说，这篇文章既是对历史的致敬，也是复古计算社区的功能性资源。

---

## 3. 《任天堂明星大乱斗》与《星之卡比：飞天赛车》中的“食物 JPEG”

**原文标题**: "Food JPEGs" in Super Smash Bros. & Kirby Air Riders

**原文链接**: [https://sethmlarson.dev/food-jpegs-in-super-smash-bros-and-kirby-air-riders](https://sethmlarson.dev/food-jpegs-in-super-smash-bros-and-kirby-air-riders)

生成摘要时出错

---

## 4. 我弃用 Windows 11 换成了 Linux，你也应该如此

**原文标题**: I dumped Windows 11 for Linux, and you should too

**原文链接**: [https://www.notebookcheck.net/I-dumped-Windows-11-for-Linux-and-you-should-too.1190961.0.html](https://www.notebookcheck.net/I-dumped-Windows-11-for-Linux-and-you-should-too.1190961.0.html)

作者详述了从 Windows 11 切换到 Artix Linux 的心路历程，其主要动因源于对微软激进的数据遥测（特别是 Copilot 和 Recall）以及系统稳定性欠佳的不满。尽管硬件配置尚可，作者仍频繁遭遇系统崩溃，并发现 Windows 破碎的设置选项和强制更新已到了难以使用的程度。

在测试了包括 macOS（在旧硬件上感到受限）和 Linux Mint（虽然稳定但显得“臃肿”）在内的多种方案后，作者最终选择了 **Artix Linux**。Artix 是一款基于 Arch 且不含 “SystemD” 的轻量级发行版，这使其拥有极快的启动速度和极低的资源占用。

转型过程中也遇到了一些挑战：
*   **硬件兼容性：** 在 2014 年款 MacBook Air 上安装 Linux 时，需要通过有线以太网连接来手动安装 WiFi 驱动。
*   **软件排障：** 作者在切换桌面环境时遇到了图形 Bug，且必须为 Greenshot 等 Windows 专属应用寻找替代方案。
*   **游戏体验：** 尽管 Steam 对大多数作品支持良好，但某些游戏仍需 Lutris 等第三方工具才能正常运行。

尽管面临这些挑战，作者仍强调了显著的收益。令人意外的是，在 Linux 上管理 iPhone 竟然比在 Windows 上更容易，因为 Dolphin 文件管理器允许直接访问文件而无需 iTunes。此外，系统表现极其稳定，自切换以来从未发生过崩溃。

文章总结道，虽然 Linux 需要更多的技术好奇心和学习成本，但其回报是更快、更私密且高度可定制的计算体验。作者认为，无论是使用像 Mint 这样“开箱即用”的发行版，还是像 Artix 这样的 DIY 系统，切换到 Linux 都能让个人电脑的使用重拾乐趣与掌控感。

---

## 5. 据报道，Instagram 数据泄露导致 1750 万用户的个人信息曝光

**原文标题**: Instagram data breach reportedly exposed the personal info of 17.5M users

**原文链接**: [https://www.engadget.com/cybersecurity/an-instagram-data-breach-reportedly-exposed-the-personal-info-of-175-million-users-192105616.html](https://www.engadget.com/cybersecurity/an-instagram-data-breach-reportedly-exposed-the-personal-info-of-175-million-users-192105616.html)

Malwarebytes 最近报告了一起潜在的数据泄露事件，涉及 1750 万 Instagram 用户的敏感信息，包括用户名、详细地址、电话号码和电子邮件地址。这家网络安全公司声称，这些数据目前正在暗网上出售，极有可能源于 2024 年发现的 Instagram API 漏洞。

对此，Instagram 否认发生了数据泄露，并坚称其系统是安全的。不过，该平台承认并修复了一个允许外部第三方触发未经授权的密码重置邮件的问题。Instagram 建议收到此类请求的用户直接将其忽略。

尽管遭到否认，Malwarebytes 仍警告称，泄露的信息可能助长网络钓鱼和账号接管风险。为了降低风险，建议用户：
*   启用双重身份验证 (2FA)。
*   更新密码。
*   通过 Meta 的账户中心检查活跃的登录设备。

截至 2026 年 1 月，虽然安全公司的调查结果与 Instagram 的官方立场仍存在争议，但这一事件提醒人们，Meta 旗下平台正面临着持续的安全挑战。

---

## 6. BasiliskII Macintosh 68k 模拟器成功移植至 ESP32-P4 / M5Stack Tab5

**原文标题**: BasiliskII Macintosh 68k Emulator Ported to ESP32-P4 / M5Stack Tab5

**原文链接**: [https://github.com/amcchord/M5Tab-Macintosh](https://github.com/amcchord/M5Tab-Macintosh)

本文详细介绍了将 **BasiliskII Macintosh 68k 模拟器** 移植到 **ESP32-P4** 微控制器的过程，该项目专为 **M5Stack Tab5** 硬件设计。它使用户能够在便携式嵌入式设备上运行从 System 7.1 到 Mac OS 8.1 的经典 Macintosh 操作系统。

该模拟器通过优化的任务拆分设计，充分利用了 Tab5 的双核 400MHz RISC-V 架构。**核心 0** 负责视频渲染、2×2 像素缩放及 I/O 处理，而 **核心 1** 则专门用于 Motorola 68040 CPU 的模拟。系统利用设备内置的 32MB PSRAM，为模拟的 Mac 分配了 4MB 至 16MB 的内存，并设有专用的帧缓冲。

**主要特性与规格：**
*   **显示：** 640×360 虚拟显示分辨率缩放至 Tab5 的 1280×720 物理屏幕，运行帧率约为 15 FPS。
*   **输入：** 支持电容式触摸屏（充当鼠标）以及用于连接实体键盘和鼠标的 USB Type-A 主机接口。
*   **存储：** 可直接从 microSD 卡加载 ROM、硬盘镜像 (.dsk) 和 CD-ROM ISO。
*   **兼容性：** 针对 Quadra 系列 ROM（特别是 Q650）进行了优化；支持完整的 Mac 按键映射和 FPU 模拟。

该项目包含一个自定义的 Mac 风格 **启动 GUI**，允许用户在启动前配置内存设置并选择磁盘镜像。在 Claude Opus 4.5 的协助下开发，此移植版本展示了 ESP32-P4 处理复杂遗留模拟的强大性能，为办公应用和复古计算爱好者提供了功能完备、口袋大小的经典 Mac 体验。

---

## 7. C++ std::move 并不移动任何东西：深入解析值类别

**原文标题**: C++ std::move doesn't move anything: A deep dive into Value Categories

**原文链接**: [https://0xghost.dev/blog/std-move-deep-dive/](https://0xghost.dev/blog/std-move-deep-dive/)

本文深入探讨了 C++ 移动语义的技术细节，明确指出 **`std::move` 并不实际移动数据**；相反，它是一个向右值引用（特别是 **xvalue**）的 `static_cast`。它的作用是向编译器发出信号，表明该对象的资源可以被“掠夺”，从而允许选择移动构造函数而非拷贝构造函数。

**核心技术洞察：**
*   **`noexcept` 的必要性：** 诸如 `std::vector` 之类的标准容器，仅在移动构造函数被标记为 `noexcept` 时，才会在重新分配内存期间使用它。这是为了维持“强异常保证”，确保在发生错误时原始数据保持完好。
*   **值类别：** 移动语义依赖于 **lvalues**（具有持久身份的左值）、**prvalues**（纯右值）和 **xvalues**（通过 `std::move` 创建的即将过期的将亡值）之间的区别。

**三个常见陷阱：**
1.  **返回 `std::move(local_var)`：** 这是一种“负优化”，会使 **NRVO（具名返回值优化）** 失效。通过返回一个 xvalue 而不是变量名，你强制执行了移动操作，而编译器本可以实现零成本的原位构造。
2.  **移动 `const` 对象：** 由于移动操作需要修改源对象，对 `const` 变量使用 `std::move` 会导致其静默回退到调用拷贝构造函数。
3.  **移后使用 (Use-after-move)：** 对象在移动后进入“有效但未定义”的状态。它们应被视为“事实上已失效”，仅应进行重新赋值或销毁，绝不应读取。

**实现方式：**
有效的资源管理遵循**五法则 (Rule of Five)**，要求实现析构函数、拷贝/移动构造函数以及拷贝/移动赋值运算符。开发者应使用 `std::exchange` 来安全地重置源指针，并确保所有移动操作均为 `noexcept`。

---

## 8. Think of Pavlov

**原文标题**: Think of Pavlov

**原文链接**: [https://boz.com/articles/think-pavlov](https://boz.com/articles/think-pavlov)

"Think of Pavlov" argues that personal and professional interactions should be viewed as "repeat games" rather than isolated events. Every conversation acts as a conditioning exercise, training others on how to perceive us, what information to share, and what types of challenges to bring to our attention.

The article uses Pavlovian conditioning as a metaphor for human behavior: our reactions serve as reinforcements for the people around us. For example, reacting with curiosity to a difficult problem encourages future transparency and collaboration. Conversely, responding with harsh criticism or making others feel "small" leads to avoidance and hidden work. Similarly, if a leader always provides the solution, they train their team to "outsource their judgment" rather than think independently.

Ultimately, the author emphasizes that our consistency, tone, and timing define our reputation. By recognizing that every interaction "rings a bell," we can more intentionally reinforce the behaviors that lead to long-term progress and healthier working relationships. Rather than focusing on winning a singular moment, we must consider what kind of feedback loop we are creating for the future.

---

## 9. The Concise TypeScript Book

**原文标题**: The Concise TypeScript Book

**原文链接**: [https://github.com/gibbok/typescript-book](https://github.com/gibbok/typescript-book)

生成摘要时出错

---

## 10. Show HN: Porting xv6 to HiFive Unmatched board

**原文标题**: Show HN: Porting xv6 to HiFive Unmatched board

**原文链接**: [https://github.com/eyengin/xv6-riscv-unmatched](https://github.com/eyengin/xv6-riscv-unmatched)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 2 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 3 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 4 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 5 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 6 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 7 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 8 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 9 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 10 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 11 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 12 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 13 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 14 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 15 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 16 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 17 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 18 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 19 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 20 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 21 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 22 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 23 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 24 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 25 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 26 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 27 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 28 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 29 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 30 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 31 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 32 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 33 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 34 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 35 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 36 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 37 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 38 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 39 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 40 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 41 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 42 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 43 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 44 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 45 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 46 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 47 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 48 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 49 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 50 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 51 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 52 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 53 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 54 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 55 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 56 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 57 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 58 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 59 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 60 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 61 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 62 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 63 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 64 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 65 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 66 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 67 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 68 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 69 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 70 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 71 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 72 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 73 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 74 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 75 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 76 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 77 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 78 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 79 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 80 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 81 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 82 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 83 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 84 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 85 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 86 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 87 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 88 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 89 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 90 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 91 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 92 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 93 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 94 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 95 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 96 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 97 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 98 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 99 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 100 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 101 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 102 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 103 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 104 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 105 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 106 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 107 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 108 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 109 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 110 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 111 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 112 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 113 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 114 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 115 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 116 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 117 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 118 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 119 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 120 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 121 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 122 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 123 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 124 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 125 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 126 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 127 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 128 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 129 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 130 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 131 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 132 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 133 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 134 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 135 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 136 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 137 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 138 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 139 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 140 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 141 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 142 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 143 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 144 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 145 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 146 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 147 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 148 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 149 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 150 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 151 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 152 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 153 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 154 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 155 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 156 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 157 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 158 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 159 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 160 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 161 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 162 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 163 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 164 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 165 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 166 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 167 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 168 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 169 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 170 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 171 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 172 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 173 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 174 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 175 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 176 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 177 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 178 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 179 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 180 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 181 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 182 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 183 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 184 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 185 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 186 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 187 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 188 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 189 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 190 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 191 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 192 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 193 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 194 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 195 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 196 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 197 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 198 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 199 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 200 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 201 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 202 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 203 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 204 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 205 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 206 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 207 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 208 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 209 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 210 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 211 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 212 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 213 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 214 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 215 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 216 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 217 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 218 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 219 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 220 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 221 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 222 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 223 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 224 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 225 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 226 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 227 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 228 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 229 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 230 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 231 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 232 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 233 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 234 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 235 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 236 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 237 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 238 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 239 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 240 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 241 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 242 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 243 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 244 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 245 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 246 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 247 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 248 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 249 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 250 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 251 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 252 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 253 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 254 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 255 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 256 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 257 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 258 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 259 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 260 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 261 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 262 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 263 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 264 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 265 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 266 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 267 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 268 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 269 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 270 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 271 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 272 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 273 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 274 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 275 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 276 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 277 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 278 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 279 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 280 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 281 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 282 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 283 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 284 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 285 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 286 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 287 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 288 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 289 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 290 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 291 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 292 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 293 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 294 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 295 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 296 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 297 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
