# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-11-01.md)

*最后自动更新时间: 2025-11-01 17:44:18*
## 1. 由于大型语言模型（LLM）的出现，arXiv不再接受计算机科学领域的职位或评论文章。

**原文标题**: arXiv No Longer Accepts Computer Science Position or Review Papers Due to LLMs

**原文链接**: [https://blog.arxiv.org/2025/10/31/attention-authors-updated-practice-for-review-articles-and-position-papers-in-arxiv-cs-category/](https://blog.arxiv.org/2025/10/31/attention-authors-updated-practice-for-review-articles-and-position-papers-in-arxiv-cs-category/)

arXiv计算机科学(CS)类别收紧对综述文章和立场论文的审核，原因是提交量激增，尤其是借助LLM生成的文章。虽然这些类型的论文从未被正式接受，但之前如果质量高且对社区有益，则由审核人员酌情允许发表。

现在，综述文章和立场论文要被考虑提交，*必须*首先被期刊或会议接受，并成功通过同行评审。作者在向arXiv提交时必须提供此同行评审的证明文件。缺乏此证明文件的提交很可能会被拒绝。

此项更改旨在应对由LLM推动的大量低质量综述文章（通常是简单的带注释的参考书目）的涌入，这些文章使审核人员不堪重负。新流程使arXiv能够依靠已建立的同行评审场所的质量控制。目标是确保只共享有价值的、专家撰写的综述文章和立场论文，从而解放审核人员，使其能够专注于核心研究论文的提交，并保持科学发现的步伐。研究科学和技术对社会影响的科学研究论文不受此政策限制。如果其他arXiv类别也遇到类似的大量LLM生成的内容，则可能会采取类似措施。

---

## 2. GHC 现在可以在浏览器中运行了

**原文标题**: GHC now runs in the browser

**原文链接**: [https://discourse.haskell.org/t/ghc-now-runs-in-your-browser/13169](https://discourse.haskell.org/t/ghc-now-runs-in-your-browser/13169)

GHC (Glasgow Haskell 编译器) 现已可以直接在 Web 浏览器中运行，完全在客户端进行。这得益于 GHC WebAssembly (wasm) 后端方面的重大进展。一个展示此功能的演示已作为 Haskell 游乐场提供。更多细节和技术解释将在稍后由作者提供。作者强调了 GHC wasm 后端令人印象深刻的进展，使其客户端执行成为可能。

---

## 3. SQLite 并发及为何你应该关心它

**原文标题**: SQLite concurrency and why you should care about it

**原文链接**: [https://jellyfin.org/posts/SQLite-locking/](https://jellyfin.org/posts/SQLite-locking/)

JPVenson的这篇博文讨论了Jellyfin中遇到的SQLite并发问题，并提出了相应的解决方案。由于SQLite基于文件的特性以及潜在的写操作冲突，Jellyfin经历了数据库锁定错误，尤其是在高负载或事务期间。旧版本Jellyfin中的一个错误加剧了这个问题，该错误导致过多的并行写请求。

为了缓解这些问题，Jellyfin使用EF Core拦截器实现了一种锁定机制，提供了三种策略：

*   **无锁 (No-Lock):** 默认行为，正常操作时不进行锁定，优先考虑性能。
*   **乐观锁 (Optimistic Locking):** 使用重试机制（通过Polly库）来处理锁定冲突，重试因锁定而失败的写操作。
*   **悲观锁 (Pessimistic Locking):** 采用`ReaderWriterLockSlim`来确保一次只能发生一个写操作，在写入期间阻止所有其他读写操作，从而最大限度地提高稳定性，但可能会牺牲性能。

该文章建议未来可能采用一种“智能锁定 (Smart Locking)”行为，该行为结合了乐观锁和悲观锁的优点。初步测试证实，两种锁定模式都有效地解决了潜在的并发问题。作者强调，Jellyfin的锁定实现旨在易于集成到其他面临类似SQLite锁定问题的EF Core应用程序中。

---

## 4. 网络上的弃用软件：你知道有HTML表格API吗？

**原文标题**: Abandonware of the web: do you know that there is an HTML tables API?

**原文链接**: [https://christianheilmann.com/2025/10/08/abandonware-of-the-web-do-you-know-that-there-is-an-html-tables-api/](https://christianheilmann.com/2025/10/08/abandonware-of-the-web-do-you-know-that-there-is-an-html-tables-api/)

本文强调了常被忽视的HTML表格API，作为创建和操作HTML表格时常用JavaScript方法的替代方案。作者提倡使用表格专用API（提供诸如`insertRow()`和`insertCell()`等方法），而非通过字符串连接或使用`createElement()`直接进行DOM操作来构建表格。此API允许开发者直接访问和修改表格元素（行、单元格、表头、表尾、标题），而无需重新渲染整个表格，从而可能提高性能和代码可读性。

文章提供了示例，演示了如何使用该API从嵌套数组创建表格，以及如何使用索引访问和修改单个单元格（例如，`t.rows[1].cells[1]`）。文章还指出了该API的一些怪癖，例如使用`-1`将行添加到表格末尾，以及无法直接创建`<th>`元素。

作者认为，如果像HTML表单一样，通过新功能来振兴和扩展HTML表格API，可以将表格的地位从单纯的布局工具提升为Web上合法的数据结构。文章鼓励重新审视和增强这种“废弃软件”，以提高Web开发效率和可访问性。最后，作者还提供了指向其新闻通讯和其他资源的链接。

---

## 5. CharlotteOS – 一款实验性的现代操作系统

**原文标题**: CharlotteOS – An Experimental Modern Operating System

**原文链接**: [https://github.com/charlotte-os/Catten](https://github.com/charlotte-os/Catten)

CharlotteOS：一个实验性现代操作系统，其核心为“Catten”，一个主要用Rust编写并包含部分汇编的单内核。Catten的目标是灵活性，灵感来源于外内核、Plan 9和Fuchsia，提供了一个类型安全的系统命名空间，可通过URI在网络上访问，并使用能力和强制访问控制进行保护。

该内核正处于积极开发阶段，并通过其代码仓库、Discord和Matrix寻求贡献者。目前，它以带有UEFI和ACPI固件的x86_64架构为目标。最低系统要求包括128MB RAM、4GB存储，以及对NVMe、USB大容量存储和带有UEFI图形输出协议的显示适配器等设备的支持。同时支持通过NS16550 UART和USB CDC ACM进行的串行通信。输入选项包括PS/2、USB HID和串口。网络功能包括USB CDC网络控制模型。

虽然允许在维护者批准的情况下使用C依赖，但严格禁止使用Rust、C和汇编以外的语言。该内核采用GNU通用公共许可证版本3.0（或更高版本）授权，且贡献受相同许可条款约束。

---

## 6. 展示HN：奇异吸引子

**原文标题**: Show HN: Strange Attractors

**原文链接**: [https://blog.shashanktomar.com/posts/strange-attractors](https://blog.shashanktomar.com/posts/strange-attractors)

这个“Show HN”帖子介绍了奇异吸引子，这种复杂的数学系统能够生成美丽的混沌图案，并通过Three.js可视化进行探索。作者详细描述了他们如何迷上这些系统，这源于秩序从随机性中涌现出来。

帖子解释了动力系统的基础知识，动力系统使用“相空间”（系统所有可能的状态）和“动力学”（支配状态转换的规则）的概念来模拟事物随时间的变化。然后，它深入研究了混沌理论，这是动力系统的一个分支，专注于表现出随机性和不可预测性，但仍遵循确定性规则的系统。“蝴蝶效应”，即微小的初始变化导致截然不同的结果，被重点强调。

奇异吸引子被定义为系统倾向于稳定下来的一组状态，通常表现出分形结构、对初始条件的敏感性以及不可预测的非周期性轨迹。该帖子使用托马斯吸引子作为示例来演示蝴蝶效应，展示了参数变化如何显著改变粒子轨迹。

实现部分描述了如何使用Three.js的乒乓渲染来高效地在GPU上渲染大量粒子。这涉及到在两个帧缓冲区对象（FBO）之间交替，一个用于当前粒子状态，另一个用于计算下一个状态，从而最大限度地减少CPU和GPU之间的数据传输。着色器程序用于将吸引子动力学应用于每个粒子。最后，作者提供了几个有用的资源和链接，供进一步探索。

---

## 7. 弗兰克·加斯金谈论保存“遗失”游戏

**原文标题**: Frank Gasking on preserving «lost» games

**原文链接**: [https://spillhistorie.no/2025/10/24/frank-gasking-on-preserving-lost-games/](https://spillhistorie.no/2025/10/24/frank-gasking-on-preserving-lost-games/)

本文采访了 Games That Weren’t (GTW) 的创始人弗兰克·加斯金。 GTW 是一个非营利数字档案馆，致力于保存和记录遗失、未发布和未完成的电子游戏。 加斯金的迷恋始于童年时代，当时他拥有一台 Commodore 64 电脑，并且在 Commodore Force 杂志上读到了一篇关于未发布游戏的令人振奋的文章。

GTW 最初是一个 Commodore 64 档案馆，后来扩展到涵盖 Amiga、PC、NES 等多个平台。 该档案馆包括已恢复的游戏、预览、屏幕截图、开发者资源以及有关被放弃或取消发行的游戏的详细信息。 加斯金强调了与开发者、收藏家和爱好者的合作的重要性。

加斯金特别强调了 GTW 在 Commodore 64 上的代表作《达菲鸭：主演油漆大劫案》，并强调了在 Hi-Tec 公司倒闭后，经过 18 年的寻找才得以恢复该游戏。

关于游戏发行商，加斯金提到偶尔会拒绝发布某些游戏，但也提到 GTW 通过提供已恢复的源代码和旧游戏的数字副本，为发行商提供帮助的情况。 他指出，虽然一些发行商积极主动地进行保护工作，但许多发行商才刚刚开始认真对待这个问题。

本文讨论了《THE GAMES THAT WEREN’T》一书，这是加斯金工作的实体化体现，提供了新鲜的内容、详细的研究以及游戏开发者的见解，涵盖了众多平台和几十年。 这本书超越了网站的内容，涵盖了广为人知和以前不为人知的游戏。

---

## 8. 自五月起，更严格的Rust需求

**原文标题**: Hard Rust requirements from May onward

**原文链接**: [https://lists.debian.org/debian-devel/2025/10/msg00285.html](https://lists.debian.org/debian-devel/2025/10/msg00285.html)

Julian Andres Klode宣布计划不早于2026年5月在APT软件包管理器中引入强制性Rust依赖项，包括Rust编译器、标准库和Sequoia生态系统。Klode列举了内存安全语言和改进的单元测试的优势，适用于.deb、.ar、.tar解析以及HTTP签名验证等关键组件。

该声明明确针对缺乏功能性Rust工具链的Debian移植维护者，敦促他们在未来六个月内实施该工具链，或者考虑停止对该移植的维护。给出的理由是Debian项目需要采用现代工具和技术，避免受到旧硬件架构的限制。

该邮件包含PGP签名，指定了首选的回复渠道（链上和链下），并列出了将收到回复通知的个人。它还包括后续消息，用于进行持续讨论。

---

## 9. 对Substrate的调查研究

**原文标题**: An investigation into Substrate

**原文链接**: [https://substack.com/inbox/post/177604037](https://substack.com/inbox/post/177604037)

无法访问文章链接。

---

## 10. 研究越来越多地发现空气污染物与痴呆症之间的联系

**原文标题**: Studies increasingly find links between air pollutants and dementia

**原文链接**: [https://www.nytimes.com/2025/11/01/health/alzheimers-dementia-air-pollution.html](https://www.nytimes.com/2025/11/01/health/alzheimers-dementia-air-pollution.html)

无法访问文章链接。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 2 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 3 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 4 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 5 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 6 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 7 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 8 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 9 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 10 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 11 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 12 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 13 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 14 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 15 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 16 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 17 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 18 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 19 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 20 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 21 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 22 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 23 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 24 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 25 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 26 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 27 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 28 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 29 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 30 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 31 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 32 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 33 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 34 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 35 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 36 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 37 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 38 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 39 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 40 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 41 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 42 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 43 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 44 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 45 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 46 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 47 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 48 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 49 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 50 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 51 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 52 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 53 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 54 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 55 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 56 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 57 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 58 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 59 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 60 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 61 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 62 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 63 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 64 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 65 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 66 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 67 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 68 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 69 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 70 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 71 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 72 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 73 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 74 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 75 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 76 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 77 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 78 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 79 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 80 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 81 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 82 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 83 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 84 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 85 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 86 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 87 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 88 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 89 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 90 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 91 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 92 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 93 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 94 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 95 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 96 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 97 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 98 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 99 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 100 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 101 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 102 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 103 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 104 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 105 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 106 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 107 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 108 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 109 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 110 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 111 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 112 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 113 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 114 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 115 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 116 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 117 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 118 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 119 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 120 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 121 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 122 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 123 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 124 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 125 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 126 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 127 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 128 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 129 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 130 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 131 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 132 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 133 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 134 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 135 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 136 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 137 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 138 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 139 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 140 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 141 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 142 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 143 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 144 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 145 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 146 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 147 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 148 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 149 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 150 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 151 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 152 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 153 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 154 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 155 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 156 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 157 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 158 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 159 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 160 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 161 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 162 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 163 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 164 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 165 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 166 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 167 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 168 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 169 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 170 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 171 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 172 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 173 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 174 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 175 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 176 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 177 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 178 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 179 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 180 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 181 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 182 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 183 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 184 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 185 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 186 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 187 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 188 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 189 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 190 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 191 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 192 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 193 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 194 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 195 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 196 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 197 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 198 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 199 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 200 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 201 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 202 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 203 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 204 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 205 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 206 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 207 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 208 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 209 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 210 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 211 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 212 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 213 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 214 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 215 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 216 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 217 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 218 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 219 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 220 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 221 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 222 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 223 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 224 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 225 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 226 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
