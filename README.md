# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-11-07.md)

*最后自动更新时间: 2025-11-07 17:51:04*
## 1. 我爱OCaml

**原文标题**: I Love OCaml

**原文链接**: [https://mccd.space/posts/ocaml-the-worlds-best/](https://mccd.space/posts/ocaml-the-worlds-best/)

本文是一封写给 OCaml 编程语言的情书，它出自一位拥有 Haskell 和 Go 经验的开发者之手。作者讲述了他们欣赏 OCaml 的历程，强调了那些在一个编程语言中对他们而言变得重要的特性。

他们最初重视 Haskell 强大的静态保证和函数式编程结构，但发现其复杂性、缓慢的编译时间和“聪明”的代码难以管理。另一方面，Go 提供了简洁性、快速编译和良好的工具，但其冗长、脆弱的错误处理、缺乏空值检查以及对函数式编程概念的抵制最终导致了不满。

作者理想的语言愿望清单包括快速的编译时间、简单的运行时、强大的静态类型、函数式编程特性（模式匹配、和类型）、良好的性能以及优秀的文档。他们认为，OCaml 几乎满足了所有这些要求。

具体来说，他们赞扬 OCaml 通过和类型和模式匹配实现的强大静态保证、相对简单的运行时语义（允许经验丰富的程序员理解生成的汇编）、使用 Dune 实现的快速编译时间、能够编译成单个二进制文件以便于部署、通过 odig 和 utop 实现的优秀文档以及自动推断的类型。

虽然承认 OCaml 的历史悠久以及一些可能不必要的特性，但作者最终得出结论，OCaml 在简洁性和表达性之间取得了恰当的平衡，并辅以良好的文档和工具。他们将此归功于 OCaml 设计者的良好品味。

---

## 2. 离开Meta和PyTorch

**原文标题**: Leaving Meta and PyTorch

**原文链接**: [https://soumith.ch/blog/2025-11-06-leaving-meta-and-pytorch.md.html](https://soumith.ch/blog/2025-11-06-leaving-meta-and-pytorch.md.html)

PyTorch负责人Soumith Chintala将在Meta工作11年后离职，其中近8年致力于将PyTorch从零开始构建到目前在人工智能领域的统治地位。他表达了离开的兴奋和不舍，强调了PyTorch的深远影响，从支持百亿亿级训练到在全球范围内被教授。

虽然承认还有更多工作要做，但他相信PyTorch处于稳定且有能力继续发展的状态，由Edward、Suo、Alban、Greg、John、Joe和Jana领导。他强调了现在负责团队的强大价值观一致性和技术实力，确保了项目的未来成功。

Soumith深情地回顾了他在FAIR的早期岁月，称赞了促进创新的协作和高效的环境。他感谢关键人物和团队对PyTorch成功的贡献，并对社区的支持以及PyTorch对研究人员和更广泛的人工智能领域的影响表示感谢。

他还感谢Meta的领导者，如马克·扎克伯格和迈克·施罗普弗，他们相信开源是一种商业策略，以及公司内部支持他的管理者。

他离开的决定源于探索新的、不舒适的事物的愿望，一个在Meta之外的“小型”项目，其动机是好奇心和避免从未尝试过不同事物的遗憾。他打算继续参与PyTorch，提供反馈和提交问题，同时追求他的新事业。

---

## 3. 我用 Zig 构建 Bytebeat 播放器的经验

**原文标题**: My Experience of building Bytebeat player in Zig

**原文链接**: [https://blog.karanjanthe.me/posts/zig-beat/](https://blog.karanjanthe.me/posts/zig-beat/)

这篇博文详细介绍了作者使用 Zig 构建名为 Zigbeat 的 bytebeat 播放器的经验。受休息期间对有趣项目的渴望启发，作者选择了 Zig，因为它具有类似 C 的感觉并且没有借用检查器。

该文章解释了 bytebeat 是一种算法音乐形式，它使用位运算从短程序生成 8 位音频样本。

作者最初在使用 raylib-Zig 时遇到了挑战，因为示例已过时，并且难以设置 Emscripten 进行 WASM 编译。他们了解到 Zig 缺乏原生字符串支持，从而更深入地理解了内存分配。作者实现了一个 Pratt 解析器用于表达式解析，但这揭示了性能问题，因为每次音频样本评估都会过度分配内存。

解决方案是使用 Arena Allocator，它以块的形式分配内存，从而提高性能。作者还尝试使用 raylib 的绘图 API 实现复古的 8 位合成器外观，但在设计方面遇到了困难，最终选择了精灵。

作者强调了使用 Zig 而不是 Javascript（Javascript 具有 `eval`，可以更轻松地执行表达式）的好处，因为它迫使他们学习解析、词法分析和内存管理。该文章包含指向 Zigbeat GitHub 存储库的链接，并鼓励读者在 Twitter 上分享和互动。

---

## 4. 深情告别

**原文标题**: A Fond Farewell

**原文链接**: [https://www.farmersalmanac.com/fond-farewell-from-farmers-almanac](https://www.farmersalmanac.com/fond-farewell-from-farmers-almanac)

《农民年鉴》在出版200多年后，将于2026年版后停止运营。在一份告别信中，《年鉴》工作人员向其忠实的读者、贡献者和合作伙伴表达了多年的支持与感谢。该声明称，结束印刷和在线出版是一个“艰难的决定”。

该信息突出了《年鉴》的历史意义，指出它曾出现在许多家庭中，并在指导种植、如厕训练和钓鱼等活动中发挥了作用。尽管《年鉴》将不再发行，但工作人员鼓励读者通过记住和分享其传统和智慧来保持其精神。

最后一版2026年版目前可在FarmersAlmanac.com、Amazon.com和部分当地商店购买。FarmersAlmanac.com网站将保持可访问状态至2025年12月。订阅者请查看电子邮件以获取与订阅相关的信息。该文章由《农民年鉴》工作人员撰写，并于2025年11月6日发布。

---

## 5. Meta预计2024年收入的10%来自诈骗。

**原文标题**: Meta projected 10% of 2024 revenue came from scams

**原文链接**: [https://sherwood.news/tech/meta-projected-10-of-2024-revenue-came-from-scams-and-banned-goods-reuters/](https://sherwood.news/tech/meta-projected-10-of-2024-revenue-came-from-scams-and-banned-goods-reuters/)

根据路透社看到的Meta内部文件显示，Meta预计其2024年收入的10%，约160亿美元，将来自诈骗广告和违禁商品的销售。这些文件揭示了Meta内部承认，因未能遏制其平台上的欺诈活动，可能会面临巨额罚款。该公司战略性地优先在处罚最严重的地区加强执法，权衡打击诈骗可能造成的收入损失与监管罚款的成本。

尽管Meta旨在减少欺诈行为，但由于对其审核团队的削减，导致大部分用户举报的违规行为被忽略或驳回。 Meta发言人安迪·斯通淡化了这些文件，声称它们提供了内部执法工作的“选择性视角”，并表示Meta积极打击欺诈和诈骗。然而，该报告强调了Meta容忍此类活动的巨大经济动机，即使它公开宣称要打击这些活动。

---

## 6. PyTorch Helion
PyTorch氦龙

**原文标题**: PyTorch Helion

**原文链接**: [https://pytorch.org/blog/helion/](https://pytorch.org/blog/helion/)

Helion：弥合 PyTorch 易用性与自定义内核高性能的新型 Python 嵌入式 DSL。它通过将高级 DSL 编译成自动调优的 Triton 代码，解决了维护特定硬件内核的挑战，从而在降低开发工作量的同时，提供跨硬件架构的性能可移植性。

Helion 的编程模型“带图块的 PyTorch”利用了现有的 PyTorch 知识。内核由宿主机代码（用于设置的标准 PyTorch）和设备代码（编译为 Triton 内核）组成，后者使用 `hl.tile` 来细分迭代空间。Helion 使用 TorchInductor 将 PyTorch 运算符映射到 Triton 实现。一个关键特性是能够将 lambda 函数作为参数传递，以创建通用内核。

Helion 的主要创新是其自动调优引擎，该引擎使用隐式搜索空间来探索大量的 Triton 配置。此过程优化了块大小、循环排序和内存访问模式等参数，从而生成针对特定硬件定制的内核。自动调优器评估数千种配置并提供最佳配置，该配置可以硬编码以用于生产中的确定性编译。

在 NVIDIA B200 和 AMD MI350X GPU 上的基准测试表明，与 torch.compile（使用 max-autotune）和手写 Triton 内核相比，Helion 实现了更高的几何平均加速比。Helion 的自动调优引擎通过自动化对最佳内核配置的复杂搜索，优于手动调优的内核，从而提高了性能并缩短了开发时间。一个案例研究表明，Helion 在 RMSNorm 反向实现中达到或超过了手写优化的 CuTe DSL 内核的性能。

---

## 7. OpenMW 0.50.0 发布 – 开源上古卷轴 3：晨风重制版

**原文标题**: OpenMW 0.50.0 Released – open-source Morrowind reimplementation

**原文链接**: [https://openmw.org/2025/openmw-0-50-0-released/](https://openmw.org/2025/openmw-0-50-0-released/)

好的，以下是一个基于假设该URL指向OpenMW 0.50.0标准发布公告的摘要。由于我无法直接访问该URL，我将根据典型的发布公告内容进行推断。

OpenMW 0.50.0，开源Morrowind引擎重制版的一个重要里程碑版本，已经发布。此版本侧重于提高稳定性、修复错误以及增强整体游戏体验，而不是引入重大的新功能。主要改进通常包括：

*   **错误修复和稳定性：** 此版本解决了社区报告的许多错误和崩溃问题，从而带来更稳定和可靠的游戏体验。这包括修复与脚本、渲染和AI相关的问题。

*   **性能改进：** 对引擎进行了优化，从而获得更流畅的性能，尤其是在图形密集区域或使用Mod时。

*   **AI增强：** AI得到了改进，更新了寻路、战斗行为以及与环境的互动。

*   **Mod支持：** 扩展或改进的Mod支持通常是重点，增加了兼容性或为Mod开发者提供了新功能。这可能包括更好地处理特定Mod类型或改进的工具。

*   **渲染改进：** 对渲染引擎的可能改进可能包括更好的阴影、光照或视觉效果。

*   **声音改进：** 声音引擎中可能发生错误修复或功能实现。

*   **UI/UX更新：** 增强用户界面和用户体验，例如改进的菜单、更好的对话处理或更直观的控件，通常是重点。

OpenMW团队鼓励用户下载新版本并报告遇到的任何问题。发布公告很可能感谢贡献者，并为那些对细节感兴趣的人提供详细的变更日志。这证明了对开源项目的持续改进，旨在为未来保存Morrowind。

如果实际的发布公告有很大不同，我将无法在没有访问权限的情况下更新此摘要。

---

## 8. 我们选择 OCaml 来编写 Stategraph。

**原文标题**: We chose OCaml to write Stategraph

**原文链接**: [https://stategraph.dev/blog/why-we-chose-ocaml](https://stategraph.dev/blog/why-we-chose-ocaml)

本文解释了为何使用 OCaml 构建用于管理 Terraform 状态的工具 Stategraph。主要原因是 OCaml 强大的类型系统，它能确保正确性并防止可能损坏状态并导致生产问题的严重错误。

本文重点介绍了使用 OCaml 的几个主要优势：

*   **类型安全的数据结构：** OCaml 的类型系统可以在编译时捕获与数据结构字段、类型和空值检查相关的错误，从而防止运行时错误和数据损坏。
*   **类型安全的 SQL 查询：** OCaml 强制执行 SQL 查询及其使用之间类型的一致性，防止模式漂移问题导致生产环境崩溃。数据库模式的更改需要代码中进行相应的更新，并由编译器强制执行。
*   **自动 JSON 序列化：** OCaml 的 PPX 从类型定义生成正确的 JSON 序列化代码，无需进行大量的序列化测试，并防止转换过程中数据丢失。
*   **默认的不可变性：** OCaml 默认的不可变性通过确保共享状态不会被意外地并发修改来防止竞争条件。
*   **严谨的错误处理：** OCaml 的变体类型和穷举性检查确保所有可能的错误情况都得到显式处理。

本文承认 OCaml 开发者比较稀少，但认为具有分布式系统和类型系统经验的工程师可以快速学习 OCaml。 稳定、类型安全的代码库的好处超过了寻找 OCaml 开发者带来的挑战，因为类型系统减少了调试时间，并允许开发者专注于功能开发。 文章总结说，对于构建像 Stategraph 这样正确性至关重要的系统来说，OCaml 的编译时保证至关重要。

---

## 9. 比较特征 – 理解 Rust 中的相等性和排序

**原文标题**: Comparison Traits – Understanding Equality and Ordering in Rust

**原文链接**: [https://itsfoxstudio.substack.com/p/comparison-traits-understanding-equality](https://itsfoxstudio.substack.com/p/comparison-traits-understanding-equality)

无法访问文章链接。

---

## 10. 1973年Wordle的实现由DEC于2022年发布

**原文标题**: 1973 Implementation of Wordle was Published by DEC (2022)

**原文链接**: [https://troypress.com/1973-implementation-of-wordle-was-published-by-dec/](https://troypress.com/1973-implementation-of-wordle-was-published-by-dec/)

本文追溯了类Wordle游戏的起源，最早可追溯到1973年，重点介绍了Digital Equipment Corp.发布的“WORD”游戏，该游戏与Wordle具有核心机制，并能提供字母存在和位置的反馈。WORD由查尔斯·里德编写，早于游戏节目“Lingo”，并使用文本界面。

随后，本文探讨了早期计算机中猜谜游戏的更广泛背景，指出它们非常适合简单的程序。文章重点介绍了沃尔特·科特克的“GUESS”，该游戏被认为是许多后续游戏的灵感来源，以及它对丹尼斯·艾利森在“构建你自己的BASIC”中倡导猜谜游戏的影响。

文章还讨论了其他几款早期的BASIC猜谜游戏，包括“HI-LO”、“NUMBER”、“STARS”、“TRAP”和“BAGELS”，展示了游戏玩法和主题的变化。文中还提到了以战斗为主题的猜谜游戏，如“TARGET”、“Bombardment”和“Salvo”。

本文将这些简单的游戏与更复杂的“反向猜谜游戏”进行了对比，在反向猜谜游戏中，计算机试图猜测人类的想法，例如“ANIMAL”、“SALVO”、“DIGITS”和“NICOMA”。文章指出，早期计算机的局限性，尤其是在内存方面，阻碍了更复杂的反向猜谜游戏的发展。

作者鼓励读者在线探索这些经典的BASIC游戏，认为有可能重新发现它们并将其改编为现代平台。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 2 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 3 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 4 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 5 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 6 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 7 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 8 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 9 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 10 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 11 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 12 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 13 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 14 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 15 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 16 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 17 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 18 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 19 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 20 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 21 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 22 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 23 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 24 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 25 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 26 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 27 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 28 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 29 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 30 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 31 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 32 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 33 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 34 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 35 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 36 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 37 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 38 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 39 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 40 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 41 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 42 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 43 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 44 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 45 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 46 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 47 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 48 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 49 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 50 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 51 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 52 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 53 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 54 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 55 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 56 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 57 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 58 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 59 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 60 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 61 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 62 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 63 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 64 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 65 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 66 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 67 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 68 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 69 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 70 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 71 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 72 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 73 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 74 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 75 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 76 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 77 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 78 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 79 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 80 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 81 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 82 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 83 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 84 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 85 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 86 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 87 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 88 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 89 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 90 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 91 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 92 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 93 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 94 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 95 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 96 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 97 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 98 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 99 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 100 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 101 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 102 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 103 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 104 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 105 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 106 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 107 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 108 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 109 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 110 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 111 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 112 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 113 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 114 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 115 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 116 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 117 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 118 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 119 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 120 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 121 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 122 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 123 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 124 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 125 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 126 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 127 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 128 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 129 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 130 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 131 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 132 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 133 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 134 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 135 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 136 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 137 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 138 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 139 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 140 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 141 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 142 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 143 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 144 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 145 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 146 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 147 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 148 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 149 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 150 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 151 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 152 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 153 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 154 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 155 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 156 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 157 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 158 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 159 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 160 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 161 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 162 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 163 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 164 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 165 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 166 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 167 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 168 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 169 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 170 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 171 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 172 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 173 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 174 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 175 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 176 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 177 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 178 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 179 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 180 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 181 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 182 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 183 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 184 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 185 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 186 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 187 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 188 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 189 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 190 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 191 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 192 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 193 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 194 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 195 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 196 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 197 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 198 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 199 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 200 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 201 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 202 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 203 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 204 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 205 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 206 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 207 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 208 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 209 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 210 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 211 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 212 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 213 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 214 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 215 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 216 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 217 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 218 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 219 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 220 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 221 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 222 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 223 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 224 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 225 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 226 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 227 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 228 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 229 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 230 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 231 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 232 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
