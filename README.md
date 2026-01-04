# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-01-04.md)

*最后自动更新时间: 2026-01-04 17:46:28*
## 1. 在谷歌工作14年的感悟

**原文标题**: Lessons from 14 Years at Google

**原文链接**: [https://addyosmani.com/blog/21-lessons/](https://addyosmani.com/blog/21-lessons/)

《谷歌十四年教给我的事》指出，软件工程的长期成功与其说取决于技术精湛，不如说取决于如何应对人际系统、优先考虑用户需求以及保持简洁。作者强调，虽然代码是工具，但真正的工作涉及管理人员、达成共识和处理模糊性。

**核心洞察包括：**

*   **以用户为中心：** 卓越的工程师专注于解决用户问题，而非应用流行技术。最优雅的解决方案往往是代码量最少的方案。
*   **清晰胜过精巧：** 软件开发是一项长期协作。代码的可读性和可维护性应优先于“精巧”的方案，并将新技术视为需谨慎使用的“创新令牌”。
*   **行动与动量：** 避免因过度分析而陷入瘫痪，应倾向于采取行动。发布一个不完美的最小可行性产品（MVP），比数周的理论争论能带来更多实际的学习心得。
*   **社交与组织协同：** 仅仅“正确”是不够的，“共同达成正确”才是推动项目的动力。由于代码不会为自己代言，工程师必须向领导层展示其影响力，并将“粘合工作”（协调与文档）视为对职业生涯的刻意贡献。
*   **规模化的效率：** 在高层级，性能提升源于消除不必要的工作，而非优化现有流程。同理，大多数“缓慢”的团队是因为目标不一致，而非执行力不足。
*   **心态与可持续性：** 通过坦诚自己的盲点来培养心理安全感，并将教学作为加深自我理解的“利己”捷径。最后，将职业生涯视为复利——投资于人际关系和学习——同时谨记时间是最不可再生的资源。

归根结底，文章认为成功的职业生涯建立在好奇心、谦逊以及对“工程本质上是人类活动”的深刻认知之上。

---

## 2. 《街头霸王II：天下斗士》(2021)

**原文标题**: Street Fighter II, the World Warrier (2021)

**原文链接**: [https://fabiensanglard.net/sf2_warrier/](https://fabiensanglard.net/sf2_warrier/)

在这篇文章中，Fabien Sanglard 详细介绍了一个巧妙的技术“奇招”，用于修复《街头霸王 II》原始街机版中的一个重大拼写错误。就在出货前夕，首席设计师 Akiman 发现游戏的副标题被误拼成了 **“World Warrier”**。

由于图形 (GFX) ROM 已经定稿并烧录，美术资源已无法重绘。然而，负责控制图块显示方式的指令 ROM 仍可修改。Akiman 的解决方案包含两个变通步骤：

1. **图块替换：** 他用从“World”一词中借用的“or”图块替换了“ier”图块。这虽然纠正了拼写，却产生了新的视觉问题：借用的图块让 Logo 看起来变成了“World Warrlor”。
2. **像素操作：** 为了将“l”变成“i”，Akiman 寻找了一种“擦除”部分图块的方法。他在角色古烈 (Guile) 的精灵图块中找到了一个仅包含单个可见像素的特定图块（图块 0x96）。通过指令让硬件调用 Logo 的调色板，在“l”上方多次绘制这个单像素图块，他实际上将其当作一支“铅笔”，画出一条线切断了字母，从而营造出“i”上方那个点的视觉效果。

这解释了为什么原始版本中“Warrior”里的“i”看起来有些不规则。虽然在《冠军版》(Champion Edition) 等后续版本中图形得到了正式修正，但副标题已被完全更改，这使得这次原始的修复成为了该游戏初期生产中一个独特的历史印记。

---

## 3. Show HN：浏览器工作原理交互式指南

**原文标题**: Show HN: An interactive guide to how browsers work

**原文链接**: [https://howbrowserswork.com/](https://howbrowserswork.com/)

本交互式指南简明扼要地分步骤介绍了浏览器如何将 URL 转化为功能齐全的网页。本指南专为工程师和对此感兴趣的用户设计，旨在通过交互式示例，帮助读者建立对底层处理机制的直觉认知。

旅程始于 **URL 处理**，浏览器会将地址栏输入的内容规范化为完整的 URL 或搜索查询。为了与服务器通信，浏览器必须首先使用 **DNS** 系统将域名解析为 IP 地址。

一旦确定了 IP，浏览器就会通过 **TCP 三次握手**（SYN, SYN-ACK, ACK）建立可靠连接。该协议确保了数据的可靠性和有序性。连接建立后，浏览器发送 **HTTP 请求**，并等待包含网站数据的 **HTTP 响应**。

随后，指南将重点转向渲染过程：
*   **解析 (Parsing)：** 浏览器将原始 HTML 字节转换为 **DOM（文档对象模型）树**。这一过程是流式的且具有容错性，意味着浏览器在文件完全下载之前就开始构建页面。
*   **渲染流水线：** 为了显示页面，浏览器执行三个主要步骤：
    1.  **布局 (Layout/Reflow)：** 计算元素的几何属性（大小和位置）。
    2.  **绘制 (Paint)：** 填充像素并创建图层。
    3.  **合成 (Composite)：** 利用 GPU 将各图层合并以进行最终显示。

作者指出，虽然像颜色更新这类更改仅需要“绘制”步骤，但元素大小的更改会触发“布局”步骤，而后者的计算开销更高。理解这些阶段有助于开发者优化 Web 性能，并对现代 Web 构建起更完善的心智模型。

---

## 4. 理解 bin, sbin, usr/bin, usr/sbin 的目录划分 (2010)

**原文标题**: Understanding the bin, sbin, usr/bin, usr/sbin split (2010)

**原文链接**: [https://lists.busybox.net/pipermail/busybox/2010-December/074114.html](https://lists.busybox.net/pipermail/busybox/2010-December/074114.html)

在这封 2010 年的邮件中，Rob Landley 解释了类 Unix 系统中 `/bin`、`/sbin`、`/usr/bin` 和 `/usr/sbin` 目录之间的划分纯属历史偶然，而非现代技术之必然。

**历史起源**
这种划分起源于 1971 年，当时 Ken Thompson 和 Dennis Ritchie 正在 PDP-11 上开发 Unix。该系统使用了两个 RK05 磁碟包，每个容量仅为 1.5MB。当操作系统的大小超过了第一个磁盘（根文件系统）的容量时，它“溢出”到了第二个磁盘上，而第二个磁盘最初是存放用户主目录的地方（因此得名 `/usr`）。为了确保系统能够启动，挂载第二个磁盘所需的关键工具保留在 `/bin` 中，而所有其他二进制文件则被移至 `/usr/bin`。

**为什么这种划分已经过时**
Landley 认为，尽管在技术上已无必要，但这个 20 世纪 70 年代的实现细节仍被“官僚主义者”维持了数十年，主要原因有三点：
1. **现代启动方式：** `initrd` 和 `initramfs` 等机制现在负责处理系统早期启动，解决了挂载驱动器的“先有鸡还是先有蛋”的问题。
2. **共享库：** 现代系统依赖共享库，这使得 `/lib` 和 `/usr` 之间产生了相互依赖。与 70 年代的静态链接二进制文件不同，这些分区已无法再独立管理。
3. **存储容量：** 迫使系统进行这种划分的物理存储限制，早在几十年前随着大容量、廉价硬盘的出现而消失了。

**结论**
Landley 总结道，虽然各种发行版发明了各种随意的规则来为这种划分辩解——例如区分“上游”文件和“本地”文件——但这种区别本质上仍是一个历史遗留的残余。他指出，许多开发者（尤其是嵌入式领域的开发者）通过将这些目录建立符号链接到一起来简化系统结构。

---

## 5. 咖啡馆独坐的不能承受之欢愉

**原文标题**: The Unbearable Joy of Sitting Alone in a Café

**原文链接**: [https://candost.blog/the-unbearable-joy-of-sitting-alone-in-a-cafe/](https://candost.blog/the-unbearable-joy-of-sitting-alone-in-a-cafe/)

在《独自坐在咖啡馆里那难以承受的喜悦》一文中，作者探讨了在为期四周的“居家度假”期间，刻意独处与“慢生活”所带来的蜕变力量。作者摒弃了典型的快节奏生活和数字连接，养成了一种习惯：只带着狗去社区咖啡馆，并刻意将所有电子设备留在家里。

文章详细描述了从最初的“数字戒断”焦虑到深层自由感的转变。通过消除网络带来的分心，作者体验到了一种时间变慢的“宁静永恒”。这种专注让作者能够进行深度的自我反思，并增强对周围环境的感知。作者对咖啡的看法也发生了变化，从将其视为功能性的咖啡因输送系统，转变为一种盛在瓷杯里的感官享受，并开始观察咖啡馆精妙的运作机制以及陌生人眼中流露出的细微情感——尤其是忧虑。

文章还触及了在为社交设计的空间里独自一人的社会悖论。不带笔记本电脑或手机端坐被定义为一种“可怕但强大”的行为，挑战了社会规范。虽然这可能让作者在他人眼中显得像个“怪人”，但它也揭示了一个由同样追求“当下感”的人们所组成的沉默亚文化。

最终，作者得出结论：这种孤独并非为了隔绝，而是为了从持续在线的“纷扰”中夺回自己的思想。这一体验在手写这一行为中达到顶峰——这是一种刻意的选择，旨在强迫思想以一种更慢、更具实体感的速度流动。这篇散文是对活在当下的价值、接受无法左右他人看法的事实，以及在无所事事中发现的恬静喜悦的一场冥想。

---

## 6. 也许注释应该解释“是什么” (2017)

**原文标题**: Maybe comments should explain 'what' (2017)

**原文链接**: [https://www.hillelwayne.com/post/what-comments/](https://www.hillelwayne.com/post/what-comments/)

在《也许注释应该解释“是什么”（2017）》一文中，作者挑战了编程界流行的准则，即“注释应该解释‘为什么’，而不是‘是什么’”。虽然作者承认注释不能替代整洁的代码和具有描述性的变量名，但他认为，“是什么”类型的注释通常是必要的，以防止不必要的“上下文切换”。

核心论点是，信息应该恰好出现在最需要它的地方。作者指出，“为什么”类的信息（例如对漏洞修复的解释）往往被埋没在提交记录中，而查找这些记录十分繁琐。更具争议性的是，作者批评了由 Bob Martin（Uncle Bob）推广的“提取到极致”哲学。这种重构风格将一个完整的内聚函数拆分为大量微小的、名称具有描述性的方法。

作者认为，虽然这缩短了主方法，但它实际上降低了可读性，因为它迫使开发者在多个不同函数之间反复跳转，才能理解程序的完整逻辑。这种频繁的跳转造成了极高的认知负担，并增加了做出危险假设的风险。

作为替代方案，作者建议将逻辑代码块保持在一起，并使用“是什么”注释来引导读者，这往往比过度重构更有效。通过在代码内部提供清晰的路线图，“是什么”注释让开发者无需脱离当前位置即可理解程序流。文章最后总结道，虽然注释不应被用来为糟糕的代码辩护，但如果它们能提高即时理解力，就不应被一概排斥。

---

## 7. Trellis AI (YC W24) 正在招聘工程师，开发用于提升医疗服务可及性的 AI 智能体。

**原文标题**: Trellis AI (YC W24) is hiring engineers to build AI agents for healthcare access

**原文链接**: [https://www.ycombinator.com/companies/trellis-ai/jobs/ngvfeaq-member-of-technical-staff-full-time](https://www.ycombinator.com/companies/trellis-ai/jobs/ngvfeaq-member-of-technical-staff-full-time)

Trellis AI（YC W24 入选初创公司，斯坦福人工智能实验室孵化项目）正在招聘技术参谋 (MTS)，负责开发旨在实现医疗行政自动化的 AI 智能体。Trellis 总部位于旧金山，致力于通过自动化文档录入、预授权和申诉流程，消除医疗领域中的“文书工作”瓶颈。

**关键信息：**
*   **使命：** Trellis 通过使用“计算机操作型”AI 智能体来处理医疗转诊和保险索赔，旨在解决美国医疗行政成本过高的问题（占总支出的 20% 以上）。据报道，其技术可将治疗等待时间缩短 90% 以上。
*   **职责：** 作为 MTS，你将构建生产级的智能体框架和“24/7 AI 协同工作伙伴”，用于处理复杂的报销逻辑。这是一个全栈职位，要求精通 Python、Go 以及 PyTorch 或 TensorFlow 等机器学习库。
*   **薪酬：** 年薪 10 万至 22.5 万美元，外加 0.10% 至 1.50% 的股权。
*   **

该职位提供了加入由行业专家和工程师组成的高水平团队的机会，站在前沿 AI 与关键医疗基础设施的交汇点。

---

## 8. Neural Networks: Zero to Hero

**原文标题**: Neural Networks: Zero to Hero

**原文链接**: [https://karpathy.ai/zero-to-hero.html](https://karpathy.ai/zero-to-hero.html)

生成摘要时出错

---

## 9. FreeBSD Home NAS, part 3: WireGuard VPN, routing, and Linux peers

**原文标题**: FreeBSD Home NAS, part 3: WireGuard VPN, routing, and Linux peers

**原文链接**: [https://rtfm.co.ua/en/freebsd-home-nas-part-3-wireguard-vpn-linux-peer-and-routing/](https://rtfm.co.ua/en/freebsd-home-nas-part-3-wireguard-vpn-linux-peer-and-routing/)

生成摘要时出错

---

## 10. Cold-Blooded Software (2023)

**原文标题**: Cold-Blooded Software (2023)

**原文链接**: [https://dubroy.com/blog/cold-blooded-software/](https://dubroy.com/blog/cold-blooded-software/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 2 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 3 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 4 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 5 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 6 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 7 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 8 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 9 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 10 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 11 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 12 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 13 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 14 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 15 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 16 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 17 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 18 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 19 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 20 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 21 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 22 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 23 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 24 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 25 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 26 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 27 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 28 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 29 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 30 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 31 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 32 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 33 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 34 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 35 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 36 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 37 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 38 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 39 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 40 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 41 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 42 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 43 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 44 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 45 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 46 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 47 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 48 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 49 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 50 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 51 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 52 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 53 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 54 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 55 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 56 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 57 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 58 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 59 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 60 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 61 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 62 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 63 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 64 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 65 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 66 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 67 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 68 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 69 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 70 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 71 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 72 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 73 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 74 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 75 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 76 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 77 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 78 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 79 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 80 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 81 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 82 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 83 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 84 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 85 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 86 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 87 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 88 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 89 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 90 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 91 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 92 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 93 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 94 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 95 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 96 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 97 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 98 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 99 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 100 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 101 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 102 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 103 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 104 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 105 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 106 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 107 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 108 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 109 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 110 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 111 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 112 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 113 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 114 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 115 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 116 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 117 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 118 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 119 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 120 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 121 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 122 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 123 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 124 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 125 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 126 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 127 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 128 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 129 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 130 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 131 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 132 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 133 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 134 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 135 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 136 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 137 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 138 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 139 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 140 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 141 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 142 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 143 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 144 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 145 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 146 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 147 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 148 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 149 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 150 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 151 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 152 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 153 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 154 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 155 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 156 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 157 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 158 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 159 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 160 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 161 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 162 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 163 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 164 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 165 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 166 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 167 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 168 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 169 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 170 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 171 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 172 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 173 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 174 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 175 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 176 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 177 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 178 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 179 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 180 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 181 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 182 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 183 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 184 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 185 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 186 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 187 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 188 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 189 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 190 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 191 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 192 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 193 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 194 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 195 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 196 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 197 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 198 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 199 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 200 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 201 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 202 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 203 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 204 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 205 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 206 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 207 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 208 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 209 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 210 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 211 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 212 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 213 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 214 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 215 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 216 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 217 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 218 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 219 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 220 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 221 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 222 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 223 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 224 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 225 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 226 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 227 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 228 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 229 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 230 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 231 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 232 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 233 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 234 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 235 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 236 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 237 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 238 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 239 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 240 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 241 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 242 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 243 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 244 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 245 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 246 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 247 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 248 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 249 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 250 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 251 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 252 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 253 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 254 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 255 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 256 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 257 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 258 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 259 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 260 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 261 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 262 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 263 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 264 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 265 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 266 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 267 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 268 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 269 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 270 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 271 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 272 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 273 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 274 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 275 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 276 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 277 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 278 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 279 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 280 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 281 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 282 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 283 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 284 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 285 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 286 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 287 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 288 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 289 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 290 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
