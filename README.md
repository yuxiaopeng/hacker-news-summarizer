# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-02-22.md)

*最后自动更新时间: 2026-02-22 17:59:35*
## 1. 注意力媒体 ≠ 社交网络

**原文标题**: Attention Media ≠ Social Networks

**原文链接**: [https://susam.net/attention-media-vs-social-networks.html](https://susam.net/attention-media-vs-social-networks.html)

在《注意力媒体 ≠ 社交网络》一文中，Susam Pal 探讨了数字社交空间的退化，指出现代平台已从真实的连接转变为剥削性的“注意力媒体”。

Pal 回顾了 Web 2.0 早期时代，当时的社交网络专注于有意义的互动以及来自选定联系人的按时间顺序排列的更新。他认为 2012 年至 2016 年间是一个负面的转折点，当时平台引入了无限滚动和“虚假”通知等功能——这些信号的设计初衷并非为了提高用户相关性，而是为了劫持注意力并最大化参与度。最终，由朋友组成的精选动态被来自陌生人的算法内容流所取代，这种体验让人感觉像是“站在一个大喇叭前”。

作者根据初衷将这些现代服务与真正的社交网络区分开来：前者服务于用户的选择，而后者则将用户的注意力变现。Pal 对主流媒体中无意识的滚动感到幻灭，他强调 Mastodon 是向社交网络本源的回归。与现代主流平台不同，Mastodon 提供了一个冷静、可预测的环境，用户只能看到他们明确选择关注的人的动态。通过移除算法操纵和无关通知，Mastodon 恢复了社交网络的最初承诺——一个由个人选择而非强迫性消费驱动的空间。

---

## 2. 修复你的工具

**原文标题**: Fix Your Tools

**原文链接**: [https://ochagavia.nl/blog/fix-your-tools/](https://ochagavia.nl/blog/fix-your-tools/)

在《修理你的工具》一文中，作者分享了一段为开发者提供重要启示的调试经历。在排查一个开源库的复杂漏洞时，作者发现调试器无法触发断点。作者起初并未着手解决工具故障，而是陷入了“解决问题模式”，试图通过繁琐的手动日志记录来诊断问题。

在对这些低效的权宜之计感到沮丧后，作者意识到这种“隧道视野”阻碍了进度。通过停下来修复调试器——这仅仅涉及一行简单的配置更改——作者便获得了迅速解决原漏洞所需的关键洞察。

作者总结道，开发者经常面临一个悖论：解决问题的迫切渴望往往使人忽视了那些本该提供帮助的工具。本文提醒我们要优先维护开发环境，因为功能完备的工具是实现高效解决问题的基石。

---

## 3. Show HN: 用 CSS 构建的 3D 麻将

**原文标题**: Show HN: 3D Mahjong, Built in CSS

**原文链接**: [https://voxjong.com](https://voxjong.com)

**VoxJong** 是一款基于 Web 的麻将消消乐（Mahjong Solitaire）实现，其独特之处在于完全使用 **CSS** 来渲染 3D 图形。该项目最初作为“Show HN”作品发布，是一个技术演示，展示了如何利用现代样式语言创建复杂的 3D 视觉效果，而无需依赖传统的 3D 引擎或沉重的框架。

该项目的主要特点包括：

*   **3D 美学：** 游戏采用“类体素”设计，牌面具有深度感并以 3D 堆叠方式排列。
*   **可调视角：** 用户可以在具有 3D 效果的**等距视角**与传统的**顶视图**之间自由切换。
*   **交互式控制：** 界面内置缩放功能，允许玩家调整棋盘比例以获得更好的视觉清晰度。
*   **技术巧思：** 通过使用 CSS 构建游戏，开发者展示了一种轻量级的网页游戏开发方案，避免了 WebGL 或 Canvas 渲染带来的性能开销。

总的来说，VoxJong 既是一款功能完备的益智游戏，也是前端开发能力的一次创意展示，为经典的消消乐玩法提供了一种清爽且极简的诠释。

---

## 4. 什么是数据库事务？

**原文标题**: What Is a Database Transaction?

**原文链接**: [https://planetscale.com/blog/database-transactions](https://planetscale.com/blog/database-transactions)

本文探讨了数据库事务的机制，即被视为单个原子单元的一系列操作。通过使用 `BEGIN`、`COMMIT` 和 `ROLLBACK` 等命令，事务可确保即使在系统故障或用户并发访问时，数据也能保持一致性。

数据库管理中的一个核心挑战是提供“一致性读”。两种最流行的 SQL 数据库对此有不同的处理方式：
*   **Postgres** 使用多版本并发控制 (MVCC)，通过元数据（`xmin`/`xmax`）创建行的新版本。它需要 `VACUUM` 进程来定期清理过期的行版本。
*   **MySQL** 直接覆盖行，但维护一个“回滚日志”（undo log）来为并发事务重构先前的版本，从而避免了清理的需求。

本文详细介绍了四种在性能与数据完整性之间进行权衡的标准隔离级别：
1.  **可串行化 (Serializable)**：最严格的级别；事务的表现如同顺序执行。
2.  **可重复读 (Repeatable Read)**：防止大多数不一致，但可能允许“幻读”（事务过程中出现新插入的数据）。
3.  **读已提交 (Read Committed)**：防止“脏读”，但允许“不可重复读”（事务过程中现有数据发生变化）。
4.  **读未提交 (Read Uncommitted)**：性能最高但最危险的级别；允许对未提交数据进行“脏读”。

对于“可串行化”模式下的并发写入，两者的实现再次分道扬镳。MySQL 采用**行级锁**（共享锁和排他锁），这可能导致死锁。Postgres 则使用**可串行化快照隔离 (SSI)**，这是一种乐观方法，通过谓词锁跟踪数据依赖关系，并终止冲突的事务而非对其进行阻塞。

最后，作者强调，理解这些隔离级别和内部机制对于开发人员构建能够保持数据可靠性的高效、高性能应用程序至关重要。

---

## 5. Xweather Live – 交互式全球矢量天气地图

**原文标题**: Xweather Live – Interactive global vector weather map

**原文链接**: [https://live.xweather.com/](https://live.xweather.com/)

**Xweather Live** 是一款先进的气象可视化平台，为用户提供高性能的交互式全球地图。该工具采用先进的矢量地图技术，提供流畅且响应迅速的体验，支持通过平滑缩放和快速数据渲染对天气模式进行深入探索。

该平台的核心功能是提供全球范围内的实时气象数据。主要特点包括：

*   **矢量化视觉效果：** 与传统的栅格地图不同，矢量地图在任何缩放级别下都能保持高分辨率和清晰度，确保地理和气象细节始终清晰锐利。
*   **全面的数据图层：** 用户可以切换不同的图层，以监测降水、风速、温度波动、气压以及极端天气警报。
*   **全球覆盖：** 地图覆盖全球范围，是国际企业、开发者和气象爱好者的宝贵资源。
*   **实时更新：** 系统旨在高效处理海量数据集，提供即时更新和精准预测。

通过将高保真可视化效果与专业级数据相结合，Xweather Live 成为追踪当前天气状况并精准预测未来天气事件的强大工具。

---

## 6. 我们在约 40MB 的二进制文件中隐藏了后门，并尝试利用 AI + Ghidra 找出它们。

**原文标题**: We hid backdoors in ~40MB binaries and asked AI + Ghidra to find them

**原文链接**: [https://quesma.com/blog/introducing-binaryaudit/](https://quesma.com/blog/introducing-binaryaudit/)

研究人员利用 Ghidra 和 Radare2 等逆向工程工具，测试了 AI 智能体（特别是 Claude 模型）在约 40MB 二进制可执行文件中检测后门的能力。通过创建名为 **BinaryAudit** 的基准测试，研究团队在 lighttpd、dnsmasq 等流行开源项目中植入了恶意代码，以观察 AI 在没有源代码的情况下能否识别出漏洞。

**核心发现：**
*   **性能表现：** 即使是最先进的模型 Claude Opus 4.6，其后门检测率也仅为 49%。
*   **高误报率：** 模型在 28% 的情况下会将干净的二进制文件误报为存在漏洞。在专业安全领域，这种“AI 废料”使得该工具目前在生产环境中并不实用。
*   **策略性失败：** 尽管 AI 能够成功追踪特定的函数调用（如 `popen()` 或 `system()`），但它缺乏高层次的直觉。它经常陷入“大海捞针”的困境，将上下文窗口浪费在良性代码上，或为明显的威胁寻找“合理化借口”。例如，在一次测试中，AI 发现了一个明显的 Shell 执行后门，却错误地将其判定为合法的系统函数。

**技术挑战：**
二进制分析比源代码分析困难得多，因为编译过程会剥离变量名和结构，仅留下底层机器代码。尽管 AI 在理解反编译器生成的伪 C 代码方面表现出惊人的能力，但它仍难以在恶意意图与复杂的优化逻辑之间做出准确区分。

**结论：**
虽然 AI 智能体展示了专业的逆向工程能力，但在恶意软件检测方面尚未达到生产就绪水平。由于缺乏战略重点且存在幻觉倾向，它们目前还无法取代人类专家来识别复杂的供应链攻击或固件漏洞。

---

## 7. Back to FreeBSD: Part 1

**原文标题**: Back to FreeBSD: Part 1

**原文链接**: [https://hypha.pub/back-to-freebsd-part-1](https://hypha.pub/back-to-freebsd-part-1)

In the article "Back to FreeBSD: Part 1," the author explains their decision to return to FreeBSD as their primary desktop operating system after several years of using Linux distributions like Fedora.

The author’s move is driven by a preference for FreeBSD’s architectural philosophy. Unlike Linux, which is a kernel paired with various independent packages, FreeBSD is developed as a complete, cohesive operating system where the kernel and base userland are built together. This creates a sense of stability and consistency that the author finds lacking in the rapid update cycles of modern Linux.

Key highlights of the transition include:

*   **ZFS Integration:** The author praises the deep integration of the ZFS file system, which is a first-class citizen in FreeBSD, offering robust data integrity and boot environments.
*   **Documentation:** The FreeBSD Handbook is cited as a major asset, providing high-quality, centralized documentation that makes system management predictable.
*   **The "Base System" vs. Ports:** The author appreciates the clear distinction between the core operating system and third-party applications managed via `pkg` or `ports`.
*   **Hardware Compatibility:** Using a ThinkPad T480s, the author notes that while setup requires more manual effort than a "turnkey" Linux distro—specifically regarding the graphical environment—the result is a leaner, more deliberate system without unnecessary bloat.

Ultimately, the article serves as a reflection on the "Unix way" of doing things. While acknowledging that FreeBSD requires more configuration work upfront, the author concludes that the resulting system feels more stable, transparent, and rewarding for their specific workflow.

---

## 8. Iran students stage first large anti-government protests since deadly crackdown

**原文标题**: Iran students stage first large anti-government protests since deadly crackdown

**原文链接**: [https://www.bbc.com/news/articles/c5yj2kzkrj0o](https://www.bbc.com/news/articles/c5yj2kzkrj0o)

生成摘要时出错

---

## 9. How Taalas “prints” LLM onto a chip?

**原文标题**: How Taalas “prints” LLM onto a chip?

**原文链接**: [https://www.anuragk.com/blog/posts/Taalas.html](https://www.anuragk.com/blog/posts/Taalas.html)

生成摘要时出错

---

## 10. Man accidentally gains control of 7k robot vacuums

**原文标题**: Man accidentally gains control of 7k robot vacuums

**原文链接**: [https://www.popsci.com/technology/robot-vacuum-army/](https://www.popsci.com/technology/robot-vacuum-army/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 2 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 3 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 4 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 5 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 6 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 7 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 8 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 9 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 10 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 11 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 12 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 13 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 14 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 15 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 16 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 17 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 18 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 19 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 20 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 21 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 22 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 23 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 24 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 25 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 26 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 27 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 28 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 29 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 30 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 31 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 32 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 33 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 34 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 35 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 36 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 37 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 38 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 39 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 40 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 41 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 42 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 43 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 44 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 45 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 46 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 47 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 48 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 49 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 50 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 51 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 52 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 53 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 54 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 55 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 56 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 57 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 58 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 59 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 60 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 61 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 62 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 63 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 64 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 65 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 66 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 67 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 68 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 69 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 70 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 71 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 72 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 73 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 74 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 75 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 76 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 77 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 78 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 79 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 80 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 81 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 82 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 83 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 84 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 85 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 86 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 87 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 88 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 89 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 90 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 91 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 92 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 93 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 94 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 95 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 96 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 97 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 98 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 99 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 100 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 101 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 102 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 103 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 104 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 105 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 106 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 107 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 108 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 109 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 110 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 111 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 112 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 113 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 114 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 115 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 116 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 117 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 118 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 119 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 120 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 121 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 122 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 123 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 124 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 125 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 126 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 127 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 128 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 129 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 130 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 131 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 132 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 133 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 134 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 135 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 136 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 137 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 138 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 139 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 140 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 141 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 142 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 143 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 144 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 145 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 146 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 147 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 148 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 149 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 150 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 151 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 152 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 153 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 154 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 155 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 156 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 157 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 158 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 159 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 160 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 161 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 162 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 163 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 164 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 165 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 166 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 167 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 168 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 169 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 170 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 171 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 172 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 173 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 174 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 175 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 176 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 177 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 178 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 179 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 180 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 181 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 182 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 183 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 184 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 185 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 186 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 187 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 188 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 189 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 190 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 191 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 192 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 193 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 194 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 195 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 196 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 197 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 198 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 199 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 200 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 201 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 202 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 203 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 204 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 205 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 206 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 207 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 208 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 209 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 210 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 211 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 212 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 213 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 214 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 215 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 216 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 217 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 218 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 219 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 220 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 221 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 222 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 223 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 224 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 225 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 226 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 227 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 228 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 229 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 230 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 231 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 232 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 233 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 234 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 235 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 236 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 237 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 238 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 239 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 240 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 241 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 242 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 243 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 244 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 245 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 246 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 247 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 248 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 249 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 250 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 251 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 252 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 253 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 254 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 255 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 256 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 257 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 258 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 259 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 260 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 261 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 262 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 263 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 264 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 265 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 266 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 267 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 268 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 269 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 270 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 271 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 272 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 273 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 274 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 275 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 276 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 277 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 278 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 279 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 280 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 281 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 282 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 283 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 284 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 285 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 286 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 287 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 288 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 289 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 290 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 291 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 292 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 293 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 294 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 295 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 296 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 297 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 298 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 299 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 300 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 301 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 302 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 303 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 304 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 305 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 306 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 307 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 308 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 309 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 310 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 311 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 312 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 313 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 314 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 315 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 316 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 317 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 318 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 319 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 320 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 321 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 322 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 323 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 324 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 325 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 326 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 327 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 328 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 329 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 330 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 331 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 332 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 333 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 334 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 335 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 336 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 337 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 338 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 339 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
