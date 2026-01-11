# Hacker News 热门文章摘要 (2026-01-11)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Replace the Retiring Windows XP with Linux

**原文标题**: Replace the Retiring Windows XP with Linux

**原文链接**: [https://www.linux.com/training-tutorials/replace-retiring-windows-xp-linux/](https://www.linux.com/training-tutorials/replace-retiring-windows-xp-linux/)

生成摘要时出错

---

## 12. My Home Fibre Network Disintegrated

**原文标题**: My Home Fibre Network Disintegrated

**原文链接**: [https://alienchow.dev/post/fibre_disintegration/](https://alienchow.dev/post/fibre_disintegration/)

生成摘要时出错

---

## 13. Vojtux – Unofficial Linux Distribution Aimed at Visually Impaired Users

**原文标题**: Vojtux – Unofficial Linux Distribution Aimed at Visually Impaired Users

**原文链接**: [https://github.com/vojtapolasek/vojtux](https://github.com/vojtapolasek/vojtux)

生成摘要时出错

---

## 14. You are not required to close your <p>, <li>, <img>, or <br> tags in HTML

**原文标题**: You are not required to close your <p>, <li>, <img>, or <br> tags in HTML

**原文链接**: [https://blog.novalistic.com/archives/2017/08/optional-end-tags-in-html/](https://blog.novalistic.com/archives/2017/08/optional-end-tags-in-html/)

生成摘要时出错

---

## 15. More than one hundred years of Film Sizes

**原文标题**: More than one hundred years of Film Sizes

**原文链接**: [https://wichm.home.xs4all.nl/filmsize.html](https://wichm.home.xs4all.nl/filmsize.html)

生成摘要时出错

---

## 16. HTML-only conditional lazy loading (via preload and media)

**原文标题**: HTML-only conditional lazy loading (via preload and media)

**原文链接**: [https://orga.cat/blog/html-conditional-lazy-loading/](https://orga.cat/blog/html-conditional-lazy-loading/)

生成摘要时出错

---

## 17. Finding and fixing Ghostty's largest memory leak

**原文标题**: Finding and fixing Ghostty's largest memory leak

**原文链接**: [https://mitchellh.com/writing/ghostty-memory-leak-fix](https://mitchellh.com/writing/ghostty-memory-leak-fix)

生成摘要时出错

---

## 18. Show HN: I used Claude Code to discover connections between 100 books

**原文标题**: Show HN: I used Claude Code to discover connections between 100 books

**原文链接**: [https://trails.pieterma.es/](https://trails.pieterma.es/)

生成摘要时出错

---

## 19. Code and Let Live

**原文标题**: Code and Let Live

**原文链接**: [https://fly.io/blog/code-and-let-live/](https://fly.io/blog/code-and-let-live/)

生成摘要时出错

---

## 20. Show HN: Ferrite – Markdown editor in Rust with native Mermaid diagram rendering

**原文标题**: Show HN: Ferrite – Markdown editor in Rust with native Mermaid diagram rendering

**原文链接**: [https://github.com/OlaProeis/Ferrite](https://github.com/OlaProeis/Ferrite)

生成摘要时出错

---

## 21. CPU Counters on Apple Silicon: article + tool

**原文标题**: CPU Counters on Apple Silicon: article + tool

**原文链接**: [https://blog.bugsiki.dev/posts/apple-pmu/](https://blog.bugsiki.dev/posts/apple-pmu/)

生成摘要时出错

---

## 22. Learning from Sudoku Solvers (2007)

**原文标题**: Learning from Sudoku Solvers (2007)

**原文链接**: [http://ravimohan.blogspot.com/2007/04/learning-from-sudoku-solvers.html](http://ravimohan.blogspot.com/2007/04/learning-from-sudoku-solvers.html)

生成摘要时出错

---

## 23. 'Bandersnatch': The Works That Inspired the 'Black Mirror' Interactive Feature (2019)

**原文标题**: 'Bandersnatch': The Works That Inspired the 'Black Mirror' Interactive Feature (2019)

**原文链接**: [https://www.hollywoodreporter.com/tv/tv-news/black-mirror-bandersnatch-real-life-works-influences-1173330/](https://www.hollywoodreporter.com/tv/tv-news/black-mirror-bandersnatch-real-life-works-influences-1173330/)

生成摘要时出错

---

## 24. Outward Signs of Inner Mysteries

**原文标题**: Outward Signs of Inner Mysteries

**原文链接**: [https://lareviewofbooks.org/article/outward-signs-of-inner-mysteries/](https://lareviewofbooks.org/article/outward-signs-of-inner-mysteries/)

生成摘要时出错

---

## 25. Max Payne – two decades later – Graphics Critique (2021)

**原文标题**: Max Payne – two decades later – Graphics Critique (2021)

**原文链接**: [https://darkcephas.blogspot.com/2021/07/max-payne-two-decades-later-graphics.html](https://darkcephas.blogspot.com/2021/07/max-payne-two-decades-later-graphics.html)

生成摘要时出错

---

## 26. KaraDAV – Lightweight Nextcloud compatible WebDAV server

**原文标题**: KaraDAV – Lightweight Nextcloud compatible WebDAV server

**原文链接**: [https://github.com/kd2org/karadav](https://github.com/kd2org/karadav)

生成摘要时出错

---

## 27. Open Chaos: A self-evolving open-source project

**原文标题**: Open Chaos: A self-evolving open-source project

**原文链接**: [https://www.openchaos.dev/](https://www.openchaos.dev/)

生成摘要时出错

---

## 28. AI is a business model stress test

**原文标题**: AI is a business model stress test

**原文链接**: [https://dri.es/ai-is-a-business-model-stress-test](https://dri.es/ai-is-a-business-model-stress-test)

生成摘要时出错

---

## 29. Large Feeds and RFC 5005

**原文标题**: Large Feeds and RFC 5005

**原文链接**: [https://alexschroeder.ch/view/2025-09-10-large-feeds](https://alexschroeder.ch/view/2025-09-10-large-feeds)

生成摘要时出错

---

## 30. Google: Don't make "bite-sized" content for LLMs

**原文标题**: Google: Don't make "bite-sized" content for LLMs

**原文链接**: [https://arstechnica.com/google/2026/01/google-dont-make-bite-sized-content-for-llms-if-you-care-about-search-rank/](https://arstechnica.com/google/2026/01/google-dont-make-bite-sized-content-for-llms-if-you-care-about-search-rank/)

生成摘要时出错

---

## 31. Overdose deaths are falling in America because of a 'supply shock': study

**原文标题**: Overdose deaths are falling in America because of a 'supply shock': study

**原文链接**: [https://www.economist.com/united-states/2026/01/08/why-overdose-deaths-are-falling-in-america](https://www.economist.com/united-states/2026/01/08/why-overdose-deaths-are-falling-in-america)

生成摘要时出错

---

## 32. Don't fall into the anti-AI hype

**原文标题**: Don't fall into the anti-AI hype

**原文链接**: [https://antirez.com/news/158](https://antirez.com/news/158)

生成摘要时出错

---

## 33. Show HN: Play poker with LLMs, or watch them play against each other

**原文标题**: Show HN: Play poker with LLMs, or watch them play against each other

**原文链接**: [https://llmholdem.com/](https://llmholdem.com/)

生成摘要时出错

---

## 34. A Year of Work on the Arch Linux Package Management (ALPM) Project

**原文标题**: A Year of Work on the Arch Linux Package Management (ALPM) Project

**原文链接**: [https://devblog.archlinux.page/2026/a-year-of-work-on-the-alpm-project/](https://devblog.archlinux.page/2026/a-year-of-work-on-the-alpm-project/)

生成摘要时出错

---

## 35. An Experimental Approach to Printf in HLSL

**原文标题**: An Experimental Approach to Printf in HLSL

**原文链接**: [https://www.abolishcrlf.org//2025/12/31/Printf.html](https://www.abolishcrlf.org//2025/12/31/Printf.html)

生成摘要时出错

---

## 36. Iran Shuts Down Starlink Internet for First Time

**原文标题**: Iran Shuts Down Starlink Internet for First Time

**原文链接**: [https://www.forbes.com/sites/zakdoffman/2026/01/11/kill-switch-iran-shuts-down-starlink-internet-for-first-time/](https://www.forbes.com/sites/zakdoffman/2026/01/11/kill-switch-iran-shuts-down-starlink-internet-for-first-time/)

生成摘要时出错

---

## 37. China applies to put 200K satellites in space after calling Starlink crash risk

**原文标题**: China applies to put 200K satellites in space after calling Starlink crash risk

**原文链接**: [https://www.scmp.com/news/china/science/article/3339493/china-applies-put-200000-satellites-space-after-calling-starlink-crash-risk](https://www.scmp.com/news/china/science/article/3339493/china-applies-put-200000-satellites-space-after-calling-starlink-crash-risk)

生成摘要时出错

---

## 38. A battle over Canada’s mystery brain disease

**原文标题**: A battle over Canada’s mystery brain disease

**原文链接**: [https://www.bbc.com/news/articles/c623r47d67lo](https://www.bbc.com/news/articles/c623r47d67lo)

生成摘要时出错

---

## 39. ASCII-Driven Development

**原文标题**: ASCII-Driven Development

**原文链接**: [https://medium.com/@calufa/ascii-driven-development-850f66661351](https://medium.com/@calufa/ascii-driven-development-850f66661351)

生成摘要时出错

---

## 40. UpCodes (YC S17) is hiring PMs, SWEs to automate construction compliance

**原文标题**: UpCodes (YC S17) is hiring PMs, SWEs to automate construction compliance

**原文链接**: [https://up.codes/careers?utm_source=HN](https://up.codes/careers?utm_source=HN)

生成摘要时出错

---

## 41. Show HN: I built an Open Source screen timer for the m5stickc (Arduino)

**原文标题**: Show HN: I built an Open Source screen timer for the m5stickc (Arduino)

**原文链接**: [https://partridge.works/screenie-christmas-project-2025-26/](https://partridge.works/screenie-christmas-project-2025-26/)

生成摘要时出错

---

## 42. Ripple: The Elegant TypeScript UI Framework

**原文标题**: Ripple: The Elegant TypeScript UI Framework

**原文链接**: [https://jsdev.space/meet-ripple/](https://jsdev.space/meet-ripple/)

生成摘要时出错

---

## 43. Show HN: mcpc – Universal command-line client for Model Context Protocol (MCP)

**原文标题**: Show HN: mcpc – Universal command-line client for Model Context Protocol (MCP)

**原文链接**: [https://github.com/apify/mcp-cli](https://github.com/apify/mcp-cli)

生成摘要时出错

---

## 44. I replaced Windows with Linux and everything's going great

**原文标题**: I replaced Windows with Linux and everything's going great

**原文链接**: [https://www.theverge.com/tech/858910/linux-diary-gaming-desktop](https://www.theverge.com/tech/858910/linux-diary-gaming-desktop)

生成摘要时出错

---

## 45. Code Is Clay

**原文标题**: Code Is Clay

**原文链接**: [https://campedersen.com/code-is-clay](https://campedersen.com/code-is-clay)

生成摘要时出错

---

## 46. Sisyphus Now Lives in Oh My Claude

**原文标题**: Sisyphus Now Lives in Oh My Claude

**原文链接**: [https://github.com/Yeachan-Heo/oh-my-claude-sisyphus](https://github.com/Yeachan-Heo/oh-my-claude-sisyphus)

生成摘要时出错

---

## 47. NASA announces unprecedented return of sick ISS astronaut and crew

**原文标题**: NASA announces unprecedented return of sick ISS astronaut and crew

**原文链接**: [https://www.livescience.com/space/space-exploration/nasa-cancels-spacewalk-and-considers-early-crew-return-from-iss-due-to-medical-issues](https://www.livescience.com/space/space-exploration/nasa-cancels-spacewalk-and-considers-early-crew-return-from-iss-due-to-medical-issues)

生成摘要时出错

---

## 48. Visual regression tests for personal blogs

**原文标题**: Visual regression tests for personal blogs

**原文链接**: [https://marending.dev/notes/visual-testing/](https://marending.dev/notes/visual-testing/)

生成摘要时出错

---

## 49. Eulogy for Dark Sky, a data visualization masterpiece (2023)

**原文标题**: Eulogy for Dark Sky, a data visualization masterpiece (2023)

**原文链接**: [https://nightingaledvs.com/dark-sky-weather-data-viz/](https://nightingaledvs.com/dark-sky-weather-data-viz/)

生成摘要时出错

---

## 50. Why Selling WhatsApp to Facebook Would Be the Biggest Mistake (2012)

**原文标题**: Why Selling WhatsApp to Facebook Would Be the Biggest Mistake (2012)

**原文链接**: [https://www.forbes.com/sites/ericjackson/2012/12/03/why-selling-whatsapp-to-facebook-would-be-the-biggest-mistake-of-jan-koums-and-brian-actons-lives/](https://www.forbes.com/sites/ericjackson/2012/12/03/why-selling-whatsapp-to-facebook-would-be-the-biggest-mistake-of-jan-koums-and-brian-actons-lives/)

生成摘要时出错

---

## 51. Side-by-side comparison of how AI models answer moral dilemmas

**原文标题**: Side-by-side comparison of how AI models answer moral dilemmas

**原文链接**: [https://civai.org/p/ai-values](https://civai.org/p/ai-values)

生成摘要时出错

---

## 52. Show HN: Yellopages – New tab Chrome extension

**原文标题**: Show HN: Yellopages – New tab Chrome extension

**原文链接**: [https://yellopages.kawaicheung.io/](https://yellopages.kawaicheung.io/)

生成摘要时出错

---

## 53. Workers at Redmond SpaceX lab exposed to toxic chemicals

**原文标题**: Workers at Redmond SpaceX lab exposed to toxic chemicals

**原文链接**: [https://www.fox13seattle.com/video/fmc-w1ga4pk97gxq0hj5](https://www.fox13seattle.com/video/fmc-w1ga4pk97gxq0hj5)

生成摘要时出错

---

## 54. Extracting books from production language models (2026)

**原文标题**: Extracting books from production language models (2026)

**原文链接**: [https://arxiv.org/abs/2601.02671](https://arxiv.org/abs/2601.02671)

生成摘要时出错

---

## 55. Rats caught on camera hunting flying bats (2025)

**原文标题**: Rats caught on camera hunting flying bats (2025)

**原文链接**: [https://scienceclock.com/rats-caught-on-camera-hunting-flying-bats-for-the-first-time/](https://scienceclock.com/rats-caught-on-camera-hunting-flying-bats-for-the-first-time/)

生成摘要时出错

---

## 56. Kodbox: Open-source cloud desktop with multi-storage fusion and web IDE

**原文标题**: Kodbox: Open-source cloud desktop with multi-storage fusion and web IDE

**原文链接**: [https://github.com/kalcaddle/kodbox](https://github.com/kalcaddle/kodbox)

生成摘要时出错

---

## 57. Verifiable Brute Force Strength

**原文标题**: Verifiable Brute Force Strength

**原文链接**: [https://gist.github.com/atoponce/a7715930ae6eb7d6b487f2f76b57a68d](https://gist.github.com/atoponce/a7715930ae6eb7d6b487f2f76b57a68d)

生成摘要时出错

---

## 58. Tux Paint

**原文标题**: Tux Paint

**原文链接**: [https://tuxpaint.org/](https://tuxpaint.org/)

生成摘要时出错

---

## 59. How to code Claude Code in 200 lines of code

**原文标题**: How to code Claude Code in 200 lines of code

**原文链接**: [https://www.mihaileric.com/The-Emperor-Has-No-Clothes/](https://www.mihaileric.com/The-Emperor-Has-No-Clothes/)

生成摘要时出错

---

## 60. LLM poetry and the "greatness" question: Experiments by Gwern and Mercor

**原文标题**: LLM poetry and the "greatness" question: Experiments by Gwern and Mercor

**原文链接**: [https://hollisrobbinsanecdotal.substack.com/p/llm-poetry-and-the-greatness-question](https://hollisrobbinsanecdotal.substack.com/p/llm-poetry-and-the-greatness-question)

生成摘要时出错

---

## 61. Show HN: VAM Seek – 2D video navigation grid, 15KB, zero server load

**原文标题**: Show HN: VAM Seek – 2D video navigation grid, 15KB, zero server load

**原文链接**: [https://github.com/unhaya/vam-seek](https://github.com/unhaya/vam-seek)

生成摘要时出错

---

## 62. Distributed Denial of Secrets

**原文标题**: Distributed Denial of Secrets

**原文链接**: [https://ddosecrets.com/](https://ddosecrets.com/)

生成摘要时出错

---

## 63. Private equity firms acquired more than 500 autism centers in past decade: study

**原文标题**: Private equity firms acquired more than 500 autism centers in past decade: study

**原文链接**: [https://www.brown.edu/news/2026-01-07/private-equity-autism-centers](https://www.brown.edu/news/2026-01-07/private-equity-autism-centers)

生成摘要时出错

---

## 64. Allow me to introduce, the Citroen C15

**原文标题**: Allow me to introduce, the Citroen C15

**原文链接**: [https://eupolicy.social/@jmaris/115860595238097654](https://eupolicy.social/@jmaris/115860595238097654)

生成摘要时出错

---

## 65. Httpz – Zero-Allocation HTTP/1.1 Parser for OxCaml

**原文标题**: Httpz – Zero-Allocation HTTP/1.1 Parser for OxCaml

**原文链接**: [https://github.com/avsm/httpz](https://github.com/avsm/httpz)

生成摘要时出错

---

## 66. Bindless Oriented Graphics Programming

**原文标题**: Bindless Oriented Graphics Programming

**原文链接**: [https://alextardif.com/BindlessProgramming.html](https://alextardif.com/BindlessProgramming.html)

生成摘要时出错

---

## 67. How your high school affects your chances of UC Admission

**原文标题**: How your high school affects your chances of UC Admission

**原文链接**: [https://sfeducation.substack.com/p/how-your-high-school-affects-your](https://sfeducation.substack.com/p/how-your-high-school-affects-your)

生成摘要时出错

---

## 68. ChatGPT Health is a marketplace, guess who is the product?

**原文标题**: ChatGPT Health is a marketplace, guess who is the product?

**原文链接**: [https://consciousdigital.org/chatgpt-health-is-a-marketplace-guess-who-is-the-product/](https://consciousdigital.org/chatgpt-health-is-a-marketplace-guess-who-is-the-product/)

生成摘要时出错

---

## 69. Self-driving cars aren't nearly a solved problem

**原文标题**: Self-driving cars aren't nearly a solved problem

**原文链接**: [https://strangecosmos.substack.com/p/self-driving-cars-arent-nearly-a](https://strangecosmos.substack.com/p/self-driving-cars-arent-nearly-a)

生成摘要时出错

---

## 70. Creating Embroidered Charts with R and ImageMagick

**原文标题**: Creating Embroidered Charts with R and ImageMagick

**原文链接**: [https://aman.bh/blog/2025/creating-embroidered-charts-with-r-and-imagemagick](https://aman.bh/blog/2025/creating-embroidered-charts-with-r-and-imagemagick)

生成摘要时出错

---

## 71. Org Mode Syntax Is One of the Most Reasonable Markup Languages for Text (2017)

**原文标题**: Org Mode Syntax Is One of the Most Reasonable Markup Languages for Text (2017)

**原文链接**: [https://karl-voit.at/2017/09/23/orgmode-as-markup-only/](https://karl-voit.at/2017/09/23/orgmode-as-markup-only/)

生成摘要时出错

---

## 72. UK government exempting itself from cyber law inspires little confidence

**原文标题**: UK government exempting itself from cyber law inspires little confidence

**原文链接**: [https://www.theregister.com/2026/01/10/csr_bill_analysis/](https://www.theregister.com/2026/01/10/csr_bill_analysis/)

生成摘要时出错

---

## 73. Linus is vibe coding

**原文标题**: Linus is vibe coding

**原文链接**: [https://github.com/torvalds/AudioNoise](https://github.com/torvalds/AudioNoise)

生成摘要时出错

---

## 74. “Erdos problem #728 was solved more or less autonomously by AI”

**原文标题**: “Erdos problem #728 was solved more or less autonomously by AI”

**原文链接**: [https://mathstodon.xyz/@tao/115855840223258103](https://mathstodon.xyz/@tao/115855840223258103)

生成摘要时出错

---

## 75. New information extracted from Snowden PDFs through metadata version analysis

**原文标题**: New information extracted from Snowden PDFs through metadata version analysis

**原文链接**: [https://libroot.org/posts/going-through-snowden-documents-part-4/](https://libroot.org/posts/going-through-snowden-documents-part-4/)

生成摘要时出错

---

## 76. Drones that recharge directly on transmission lines

**原文标题**: Drones that recharge directly on transmission lines

**原文链接**: [https://www.ycombinator.com/companies/voltair](https://www.ycombinator.com/companies/voltair)

生成摘要时出错

---

## 77. My Beef with the iOS 26 Tab Bar

**原文标题**: My Beef with the iOS 26 Tab Bar

**原文链接**: [https://ryanashcraft.com/ios-26-tab-bar-beef/](https://ryanashcraft.com/ios-26-tab-bar-beef/)

生成摘要时出错

---

## 78. A child in the state of nature

**原文标题**: A child in the state of nature

**原文链接**: [https://lareviewofbooks.org/article/a-child-in-the-state-of-nature/](https://lareviewofbooks.org/article/a-child-in-the-state-of-nature/)

生成摘要时出错

---

## 79. Bob Weir has died

**原文标题**: Bob Weir has died

**原文链接**: [https://www.rollingstone.com/music/music-news/bob-weir-grateful-dead-dead-obituary-1234810106/](https://www.rollingstone.com/music/music-news/bob-weir-grateful-dead-dead-obituary-1234810106/)

生成摘要时出错

---

## 80. Sigmund Freud's Begonia

**原文标题**: Sigmund Freud's Begonia

**原文链接**: [https://observer.co.uk/news/first-person/article/emma-freud-sigmund-freuds-begonia](https://observer.co.uk/news/first-person/article/emma-freud-sigmund-freuds-begonia)

生成摘要时出错

---

## 81. Show HN: Umaro – An interactive music theory suite for guitarists

**原文标题**: Show HN: Umaro – An interactive music theory suite for guitarists

**原文链接**: [https://www.umaro.app/](https://www.umaro.app/)

生成摘要时出错

---

## 82. Brands upset Buy For Me is featuring their products on Amazon without permission

**原文标题**: Brands upset Buy For Me is featuring their products on Amazon without permission

**原文链接**: [https://www.modernretail.co/technology/brands-are-upset-that-buy-for-me-is-featuring-their-products-on-amazon-without-permission/](https://www.modernretail.co/technology/brands-are-upset-that-buy-for-me-is-featuring-their-products-on-amazon-without-permission/)

生成摘要时出错

---

## 83. Show HN: Marten – Elegant Go web framework (nothing in the way)

**原文标题**: Show HN: Marten – Elegant Go web framework (nothing in the way)

**原文链接**: [https://github.com/gomarten/marten](https://github.com/gomarten/marten)

生成摘要时出错

---

## 84. Changes to Android Open Source Project

**原文标题**: Changes to Android Open Source Project

**原文链接**: [https://source.android.com/](https://source.android.com/)

生成摘要时出错

---

## 85. I build products to get "unplugged" from the internet

**原文标题**: I build products to get "unplugged" from the internet

**原文链接**: [https://getunplugged.io/I-build-products-to-get-unplugged](https://getunplugged.io/I-build-products-to-get-unplugged)

生成摘要时出错

---

## 86. How to store a chess position in 26 bytes (2022)

**原文标题**: How to store a chess position in 26 bytes (2022)

**原文链接**: [https://ezzeriesa.notion.site/How-to-store-a-chess-position-in-26-bytes-using-bit-level-magic-df1fdb5364eb42fdac11eb23b25e9605](https://ezzeriesa.notion.site/How-to-store-a-chess-position-in-26-bytes-using-bit-level-magic-df1fdb5364eb42fdac11eb23b25e9605)

生成摘要时出错

---

## 87. UK Orders Ofcom to Explore Encryption Backdoors

**原文标题**: UK Orders Ofcom to Explore Encryption Backdoors

**原文链接**: [https://reclaimthenet.org/uk-orders-ofcom-to-explore-encryption-backdoors](https://reclaimthenet.org/uk-orders-ofcom-to-explore-encryption-backdoors)

生成摘要时出错

---

## 88. RTX 5090 and Raspberry Pi: Can it game?

**原文标题**: RTX 5090 and Raspberry Pi: Can it game?

**原文链接**: [https://scottjg.com/posts/2026-01-08-crappy-computer-showdown/](https://scottjg.com/posts/2026-01-08-crappy-computer-showdown/)

生成摘要时出错

---

## 89. Bichon: A lightweight, high-performance Rust email archiver with WebUI

**原文标题**: Bichon: A lightweight, high-performance Rust email archiver with WebUI

**原文链接**: [https://github.com/rustmailer/bichon](https://github.com/rustmailer/bichon)

生成摘要时出错

---

## 90. GPU memory snapshots: sub-second startup (2025)

**原文标题**: GPU memory snapshots: sub-second startup (2025)

**原文链接**: [https://modal.com/blog/gpu-mem-snapshots](https://modal.com/blog/gpu-mem-snapshots)

生成摘要时出错

---

## 91. Flock Hardcoded the Password for America's Surveillance Infrastructure 53 Times

**原文标题**: Flock Hardcoded the Password for America's Surveillance Infrastructure 53 Times

**原文链接**: [https://nexanet.ai/blog/53-times-flocksafety-hardcoded-the-password-for-americas-surveillance-infrastructure](https://nexanet.ai/blog/53-times-flocksafety-hardcoded-the-password-for-americas-surveillance-infrastructure)

生成摘要时出错

---

## 92. OpenAI is reportedly asking contractors to upload real work from past jobs

**原文标题**: OpenAI is reportedly asking contractors to upload real work from past jobs

**原文链接**: [https://techcrunch.com/2026/01/10/openai-is-reportedly-asking-contractors-to-upload-real-work-from-past-jobs/](https://techcrunch.com/2026/01/10/openai-is-reportedly-asking-contractors-to-upload-real-work-from-past-jobs/)

生成摘要时出错

---

## 93. Why Is Greenland Part of the Kingdom of Denmark? A Short History

**原文标题**: Why Is Greenland Part of the Kingdom of Denmark? A Short History

**原文链接**: [https://www.diis.dk/en/research/why-is-greenland-part-of-the-kingdom-of-denmark-a-short-history](https://www.diis.dk/en/research/why-is-greenland-part-of-the-kingdom-of-denmark-a-short-history)

生成摘要时出错

---

## 94. Worst of breed software

**原文标题**: Worst of breed software

**原文链接**: [https://worstofbreed.net/](https://worstofbreed.net/)

生成摘要时出错

---

## 95. Oh My Zsh adds bloat

**原文标题**: Oh My Zsh adds bloat

**原文链接**: [https://rushter.com/blog/zsh-shell/](https://rushter.com/blog/zsh-shell/)

生成摘要时出错

---

## 96. JavaScript Demos in 140 Characters

**原文标题**: JavaScript Demos in 140 Characters

**原文链接**: [https://beta.dwitter.net](https://beta.dwitter.net)

生成摘要时出错

---

## 97. Things I've quit doing at my desk

**原文标题**: Things I've quit doing at my desk

**原文链接**: [https://justinjackson.ca/i-quit-my-desk](https://justinjackson.ca/i-quit-my-desk)

生成摘要时出错

---

## 98. Kubernetes Was Overkill. We Moved to Docker Compose and Saved 60 Hours

**原文标题**: Kubernetes Was Overkill. We Moved to Docker Compose and Saved 60 Hours

**原文链接**: [https://medium.com/engineering-playbook/kubernetes-was-overkill-we-moved-to-docker-compose-and-saved-60-hours-3e7811122135](https://medium.com/engineering-playbook/kubernetes-was-overkill-we-moved-to-docker-compose-and-saved-60-hours-3e7811122135)

生成摘要时出错

---

## 99. Greenland sharks maintain vision for centuries through DNA repair mechanism

**原文标题**: Greenland sharks maintain vision for centuries through DNA repair mechanism

**原文链接**: [https://phys.org/news/2026-01-eye-greenland-sharks-vision-centuries.html](https://phys.org/news/2026-01-eye-greenland-sharks-vision-centuries.html)

生成摘要时出错

---

## 100. Show HN: I made a memory game to teach you to play piano by ear

**原文标题**: Show HN: I made a memory game to teach you to play piano by ear

**原文链接**: [https://lend-me-your-ears.specr.net](https://lend-me-your-ears.specr.net)

生成摘要时出错

---

