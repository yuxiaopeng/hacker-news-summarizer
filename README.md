# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-07-12.md)

*最后自动更新时间: 2026-07-12 18:24:02*
## 1. 借助现代编程代理构建新旧应用 —— 陶哲轩

**原文标题**: Old and new apps, via modern coding agents by Terry Tao

**原文链接**: [https://terrytao.wordpress.com/2026/07/11/old-and-new-apps-via-modern-coding-agents/](https://terrytao.wordpress.com/2026/07/11/old-and-new-apps-via-modern-coding-agents/)

在这篇博文中，世界著名数学家陶哲轩（Terry Tao）探讨了 AI 编程助手——特别是 GitHub Copilot Workspace——对软件开发的变革性影响。他展示了这些工具如何显著降低创建或更新软件所需的“激活能”。

陶哲轩重点介绍了两项主要实验：

1.  **旧代码现代化**：陶哲轩成功将一个拥有 30 年历史的 C++ 应用程序（一个二维波动方程模拟器）移植为现代化的、基于浏览器的 JavaScript/HTML5 应用。AI 助手承担了重构旧逻辑和生成功能性 Web 界面的繁琐工作，而这类任务在以前需要耗费大量时间进行手动转换。
2.  **快速原型设计**：他还从零开始创建了一个“置换群计算器”。通过使用自然语言提示词描述数学需求，陶哲轩在极短的时间内生成了一个完善且功能齐全的实用程序，而手动编写 UI 和逻辑通常需要更长的时间。

**核心洞察：**
*   **角色转变**：陶哲轩观察到，开发者的角色正在从编写语法转向担任高层级的“架构师和评审员”。人类在提供数学直觉和捕捉 AI 可能忽略的细微逻辑错误方面仍然不可或缺。
*   **效率提升**：这些工具实现了一种“低摩擦”的工作流，使创意几乎可以瞬间转化为可运行的软件。
*   **可及性**：陶哲轩指出，这些助手推动了软件创作的民主化，让研究人员和非专业人士能够为特定任务构建定制化工具，而无需精通现代 Web 框架。

陶哲轩总结道，虽然这项技术尚未完美，但它代表了一种范式转变，即概念构思与功能应用之间的障碍已大幅减少。

---

## 2. 难道你不是指灭绝吗？

**原文标题**: Don't You Mean Extinct?

**原文链接**: [https://fabiensanglard.net/extinct/index.html](https://fabiensanglard.net/extinct/index.html)

在《你的意思是灭绝吗？》（Don’t You Mean Extinct?）一文中，Fabien Sanglard 借用 1993 年《侏罗纪公园》从定格动画向 CGI 转型的案例，回应了软件工程师对 AI 日益增长的焦虑。当定格动画大师 Phil Tippett 看到早期的 CGI 测试时，曾留下一句名言：“我觉得自己要灭绝了。”然而，Tippett 并没有消失，而是选择了进化。他将自己在生物运动方面的专长应用于数字领域，并最终赢得了奥斯卡奖。

Sanglard 认为，程序员目前正面临着类似的“变革性进化”。为了避免被淘汰，开发者必须将大语言模型（LLM）视为强大的工具，而非替代品。虽然 AI 可以生成大量代码，但开发者的核心价值依然在于**解决问题、架构设计和质量控制**。

为了应对这一转型，Sanglard 提出了几项实用策略：
*   **投入学习：** 通过 Andrej Karpathy 的教程等资源，深入理解 LLM 的运行机制。
*   **维持代码质量：** 避免“凭感觉编程”（vibe-coding）——即放任 AI 不受约束地运行。使用系统特定的指令文件（如 `CLAUDE.md`）来强制执行个人编码风格，例如避免“箭头型反模式”并优先采用提前返回原则。
*   **提高评审标准：** 既然 AI 承担了体力劳动，对代码评审的要求就应当更高。这包括要求更佳的提交信息、全面的单元测试，以及更小、更易读的拉取请求。
*   **利用效率优势：** 利用 LLM 消化复杂的研究论文、梳理陌生的代码库，并赋能规模更小、产出更快的团队。

最终，Sanglard 断言，虽然作为手动输入语法的“编程”行为正在发生变化，但对精准度和优雅设计的需求依然存在。通过与技术同步进化——正如 Phil Tippett 当年所做的那样——程序员可以驾驭这股“新浪潮”，并在不断变化的格局中重拾动力。

---

## 3. 缺乏理解的自动化

**原文标题**: Automation Without Understanding

**原文链接**: [https://arxiv.org/abs/2607.06377](https://arxiv.org/abs/2607.06377)

**《理解力缺失的自动化》摘要**

在论文《理解力缺失的自动化》（arXiv:2607.06377）中，朴俊勇（Jun-Yong Park）指出，美国在人工智能系统于数学领域取得前所未有的突破之际，却忽视了人类的数学教育，这正在犯下一个严重的战略错误。朴俊勇将他的论点建立在两项近期发展之上：一是2026年5月人工智能证伪了长期存在的“埃尔德什平面单位距离猜想”，二是联邦政府对数学科学支持的同步下降。

作者的核心论点是，“数学能力”——即经过训练的验证、解读和挑战复杂推理的能力——不仅仅是定理产出的副产品，更是一种至关重要的国家基础设施。朴俊勇将数学专业知识比作半导体制造，将其描述为一种需要数代人积累的战略资产，一旦人才培养链条断裂，便无法按需重建。

朴俊勇警告称，未来人工智能可能会产生“不透明的劝服”（opaque persuasion）——即由于人类缺乏审计专业知识，只能基于信任而盲目接受其结果。为应对这一挑战，他提议在监管和技术层面进行转变：要求执行高风险推理的人工智能系统必须以正式的、机器可校验的格式公开其逻辑。这将使人工智能的输出转化为可审计的结构，确保自动化的“证明”仍能受到严格验证。

最后，文章呼吁重新对培养数学家的人才机构进行投资。朴俊勇总结道，如果只追求知识生产的自动化，而不维持人类理解知识的能力，将会产生一种危险的依赖，从而破坏监督和引导人工智能所需的智力基础设施。

---

## 4. 如何阅读更多书籍

**原文标题**: How to Read More Books

**原文链接**: [https://scotto.me/blog/2026-07-12-how-to-read-more-books/](https://scotto.me/blog/2026-07-12-how-to-read-more-books/)

在《如何阅读更多的书》中，作者分享了成为高效阅读者的实用指南，介绍了如何将阅读量从每年不足十本提升到几乎每周一本。其核心理念是**用阅读时间取代屏幕时间**。通过卸载社交媒体应用并随身携带书籍，读者可以利用通勤、排队甚至做饭等零碎的空闲时间来稳步推进阅读进度。

关键策略包括：

*   **工具与形式：** 利用电子阅读器的便携性及内置词典等功能，同时结合纸质书以保持与文本的触觉联系。
*   **阅读习惯：** 同时阅读不同体裁的多本书以防厌倦。作者推崇“读你所爱，直到爱上阅读”的准则，强调个人兴趣是建立持久习惯的最佳方式。
*   **放弃的权利：** 不要觉得有义务读完每一本书。如果书的内容乏味或阅读时机不对，就直接换下一本。
*   **记忆与追踪：** 使用 Goodreads 等平台设定年度目标并追踪进度，但要将理解力置于速度之上。撰写书评和记笔记对于长期记忆和深度理解至关重要。
*   **寻找内容：** 参考 YouTube 评论者（如 *Better Than Food*）和 Goodreads 的推荐来建立“待读清单”。

最后，作者建议**避免使用“速成法”**，如速读、摘要或有声书。他认为真正的阅读需要对文本全神贯注，阅读习惯应当通过自律和好奇心自然养成，而非投机取巧。

---

## 5. Show HN: Shirei, cross-platform GUI framework in native Go

**原文标题**: Show HN: Shirei, cross-platform GUI framework in native Go

**原文链接**: [https://github.com/hasenj/go-shirei/](https://github.com/hasenj/go-shirei/)

生成摘要时出错

---

## 6. 深入理解 Odin 编程语言

**原文标题**: Understanding the Odin Programming Language

**原文链接**: [https://odinbook.com/](https://odinbook.com/)

**《深入理解 Odin 编程语言》**是由资深游戏引擎程序员卡尔·齐林斯基（Karl Zylinski）编写的一本全面指南。卡尔是首款基于 Odin 开发的商业游戏《猫与洋葱》（*CAT & ONION*）的创作者。本书旨在通过教授 Odin 设计背后的“实现方式”与“设计初衷”，揭开底层编程的神秘面纱。

**核心内容与目标读者**
本书涵盖了从基础过程到高级概念的广泛主题，包括手动内存管理、参数化多态以及面向数据设计。虽然 Odin 是一门简单的语言，但本书专为具有编程经验的人士量身定制，特别是那些希望从带有垃圾回收机制的语言（如 Go）转向手动内存管理的人。本书得到了 Odin 创始人 Bill Hall（"gingerBill"）的高度认可。

**作者背景**
卡尔·齐林斯基为本书带来了深厚的行业专业知识，他曾先后在 Bitsquid、Autodesk 和 Our Machinery 担任游戏引擎程序员，并作为游戏程序员参与了《逃出生天》（*A Way Out*）等作品的开发。

**格式与获取途径**
本书提供多种格式：
*   **HTML：** 经过优化且具备导航功能的便携式文件，适合在电脑上阅读。
*   **电子书 (eBook)：** 适用于电子阅读器、Kindle 和 Google 图书。
*   通过 **store.zylinski.se** 或 **Itch** 购买即可获得上述两种格式。

**更新与维护**
本书会定期更新，以保持与不断发展的 Odin 生态系统同步。最新版本 (1.10) 引入了关于“固定容量动态数组”的变更，而之前的版本 (1.8–1.9) 则重构了字符串处理，并适配了 Odin 核心包（如 `core:os`）的重大变化。购书者可以从原始购买渠道免费下载这些更新。

---

## 7. 为什么要研究丢番图方程？

**原文标题**: Why study Diophantine equations?

**原文链接**: [https://hidden-phenomena.com/articles/modular](https://hidden-phenomena.com/articles/modular)

This article explores how the study of Diophantine equations—finding integer solutions to polynomial equations—serves as a primary tool for uncovering the "hidden structures" of mathematics. Using a progression of examples, the author demonstrates how these equations have historically led to fundamental discoveries in number theory.

The article outlines several key developments:
*   **Divisibility and Modular Arithmetic:** Simple equations like $Ax = B$ introduce the concepts of remainders and divisibility, which are systematically managed through modular arithmetic.
*   **Unique Prime Factorization:** Equations of the form $Ax + By = C$ are solved using the Euclidean algorithm. This process is essentially equivalent to discovering unique prime factorization, the principle that every whole number has a unique set of prime building blocks.
*   **The Chinese Remainder Theorem:** Building on prime factorization, this theorem allows mathematicians to simplify complex modular equations by breaking them down into systems of equations focused on individual prime powers.
*   **The Langlands Program:** The author identifies the Langlands program as a modern pinnacle of this field. By studying equations of the form $f(x) = Ny$, mathematicians have revealed some of the most intricate and profound structures in the integers ever observed.

Ultimately, the author argues that Diophantine equations are not merely abstract puzzles but are the gateway to understanding the deep, underlying patterns of the numerical world.

---

## 8. Theo de Raadt：“你准是抽了什么致幻的东西” (2007)

**原文标题**: Theo de Raadt: "You've been smoking something mind altering" (2007)

**原文链接**: [https://marc.info/?l=openbsd-misc&m=119318909016582](https://marc.info/?l=openbsd-misc&m=119318909016582)

在这一封2007年来自OpenBSD邮件列表的邮件中，创始人Theo de Raadt严厉驳斥了x86虚拟化（如Xen）具有安全优势的说法。

他的批评集中在以下三个要点：

1.  **复杂性增加：** De Raadt认为，虚拟化在硬件和操作系统之间增加了一个庞大且多余的软件层——本质上是第二个内核。他主张这一层不可避免地“充满了新漏洞”，从而扩大了而非缩小了攻击面。
2.  **硬件缺陷：** 他指出底层的x86架构本身就存在问题，并以其糟糕的页面保护实现为例，指出这是安全计算的一个薄弱基础。
3.  **人的局限性：** 他强调了行业中一个根本性的讽刺：如果全球软件工程师都难以编写出安全的操作系统和应用程序，那就没有理由相信他们能突然开发出无漏洞的虚拟化层。

最终，De Raadt将围绕虚拟化的炒作斥为营销噱头（“漂亮的花招”）而非真正的安全改进，并称那种认为虚拟化是安全的想法是“被蒙蔽了”。

---

## 9. The power of collaboration: How we can reduce traffic congestion

**原文标题**: The power of collaboration: How we can reduce traffic congestion

**原文链接**: [https://research.google/blog/the-power-of-collaboration-how-we-can-reduce-traffic-congestion/](https://research.google/blog/the-power-of-collaboration-how-we-can-reduce-traffic-congestion/)

生成摘要时出错

---

## 10. Ghostel.el: Terminal emulator powered by libghostty

**原文标题**: Ghostel.el: Terminal emulator powered by libghostty

**原文链接**: [https://dakra.github.io/ghostel/](https://dakra.github.io/ghostel/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 2 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 3 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 4 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 5 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 6 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 7 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 8 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 9 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 10 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 11 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 12 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 13 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 14 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 15 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 16 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 17 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 18 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 19 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 20 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 21 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 22 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 23 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 24 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 25 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 26 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 27 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 28 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 29 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 30 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 31 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 32 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 33 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 34 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 35 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 36 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 37 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 38 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 39 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 40 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 41 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 42 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 43 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 44 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 45 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 46 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 47 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 48 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 49 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 50 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 51 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 52 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 53 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 54 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 55 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 56 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 57 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 58 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 59 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 60 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 61 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 62 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 63 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 64 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 65 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 66 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 67 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 68 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 69 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 70 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 71 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 72 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 73 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 74 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 75 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 76 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 77 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 78 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 79 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 80 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 81 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 82 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 83 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 84 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 85 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 86 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 87 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 88 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 89 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 90 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 91 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 92 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 93 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 94 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 95 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 96 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 97 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 98 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 99 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 100 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 101 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 102 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 103 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 104 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 105 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 106 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 107 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 108 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 109 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 110 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 111 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 112 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 113 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 114 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 115 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 116 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 117 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 118 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 119 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 120 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 121 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 122 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 123 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 124 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 125 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 126 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 127 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 128 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 129 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 130 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 131 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 132 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 133 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 134 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 135 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 136 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 137 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 138 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 139 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 140 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 141 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 142 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 143 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 144 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 145 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 146 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 147 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 148 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 149 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 150 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 151 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 152 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 153 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 154 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 155 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 156 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 157 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 158 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 159 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 160 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 161 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 162 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 163 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 164 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 165 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 166 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 167 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 168 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 169 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 170 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 171 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 172 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 173 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 174 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 175 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 176 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 177 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 178 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 179 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 180 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 181 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 182 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 183 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 184 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 185 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 186 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 187 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 188 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 189 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 190 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 191 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 192 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 193 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 194 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 195 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 196 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 197 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 198 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 199 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 200 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 201 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 202 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 203 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 204 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 205 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 206 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 207 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 208 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 209 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 210 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 211 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 212 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 213 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 214 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 215 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 216 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 217 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 218 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 219 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 220 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 221 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 222 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 223 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 224 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 225 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 226 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 227 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 228 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 229 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 230 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 231 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 232 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 233 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 234 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 235 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 236 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 237 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 238 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 239 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 240 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 241 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 242 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 243 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 244 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 245 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 246 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 247 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 248 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 249 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 250 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 251 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 252 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 253 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 254 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 255 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 256 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 257 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 258 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 259 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 260 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 261 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 262 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 263 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 264 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 265 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 266 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 267 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 268 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 269 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 270 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 271 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 272 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 273 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 274 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 275 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 276 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 277 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 278 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 279 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 280 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 281 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 282 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 283 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 284 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 285 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 286 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 287 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 288 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 289 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 290 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 291 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 292 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 293 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 294 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 295 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 296 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 297 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 298 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 299 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 300 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 301 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 302 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 303 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 304 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 305 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 306 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 307 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 308 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 309 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 310 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 311 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 312 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 313 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 314 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 315 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 316 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 317 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 318 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 319 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 320 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 321 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 322 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 323 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 324 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 325 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 326 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 327 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 328 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 329 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 330 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 331 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 332 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 333 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 334 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 335 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 336 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 337 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 338 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 339 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 340 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 341 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 342 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 343 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 344 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 345 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 346 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 347 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 348 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 349 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 350 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 351 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 352 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 353 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 354 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 355 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 356 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 357 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 358 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 359 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 360 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 361 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 362 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 363 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 364 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 365 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 366 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 367 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 368 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 369 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 370 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 371 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 372 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 373 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 374 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 375 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 376 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 377 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 378 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 379 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 380 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 381 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 382 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 383 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 384 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 385 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 386 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 387 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 388 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 389 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 390 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 391 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 392 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 393 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 394 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 395 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 396 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 397 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 398 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 399 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 400 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 401 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 402 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 403 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 404 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 405 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 406 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 407 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 408 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 409 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 410 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 411 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 412 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 413 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 414 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 415 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 416 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 417 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 418 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 419 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 420 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 421 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 422 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 423 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 424 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 425 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 426 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 427 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 428 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 429 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 430 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 431 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 432 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 433 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 434 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 435 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 436 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 437 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 438 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 439 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 440 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 441 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 442 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 443 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 444 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 445 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 446 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 447 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 448 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 449 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 450 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 451 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 452 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 453 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 454 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 455 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 456 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 457 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 458 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 459 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 460 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 461 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 462 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 463 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 464 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 465 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 466 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 467 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 468 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 469 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 470 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 471 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 472 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 473 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 474 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 475 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 476 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 477 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 478 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 479 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
