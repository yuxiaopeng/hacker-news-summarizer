# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-12-28.md)

*最后自动更新时间: 2025-12-28 17:46:36*
## 1. 成长于“404 Not Found”：戈壁沙漠中的中国核城

**原文标题**: Growing up in “404 Not Found”: China's nuclear city in the Gobi Desert

**原文链接**: [https://substack.com/inbox/post/182743659](https://substack.com/inbox/post/182743659)

《在“404”长大》探讨了位于甘肃戈壁滩上的秘密核基地——404城的历史与传承。该城市始建于1958年，在地图上消失了数十年，是中国核武器计划的隐秘中心，也是中国第一颗原子弹的诞生地。

在鼎盛时期，404城是一个自给自足的微型社会，容纳了包括科学家、工程师及其家属在内的近10万人口。尽管地处偏远且沙漠气候恶劣，国家仍为居民提供了高质量的生活设施，包括学校、医院、剧院，甚至还有一座带动物园的公园。文章重点讲述了在那里长大的孩子独特的童年经历：这种生活既受限于极度的保密和地理隔绝，又充满深厚的社区归属感和安全感。

随着冷战结束和核计划重心的转移，这座城市开始衰落。2000年代中期，大部分居民搬迁到了附近的嘉峪关市。如今，404城在很大程度上已成为一座“鬼城”，随处可见破败的社会主义风格建筑和荒废的游乐场。

最终，这个故事捕捉到了对中国历史上一个“迷失”时代的怀旧情怀。它向“三线”一代致敬——成千上万的建设者隐姓埋名，为提升中国的军事和科研地位做出了巨大的个人牺牲。这座城市依然是国家机密的特殊象征，也见证了国家雄心背后所付出的个人代价。

---

## 2. 用质数构成的 Hacker News

**原文标题**: Hacker News made out of prime numbers

**原文链接**: [https://dosaygo-studio.github.io/prime-news/index.html](https://dosaygo-studio.github.io/prime-news/index.html)

**Hacker News Prime** 是一个概念性恶搞项目，它从数论和数学的角度重新构思了知名科技新闻聚合网站 Hacker News 的界面。

其内容模仿了该网站熟悉的页眉和页脚布局，但将标准分类替换为与素数相关的术语。关键导航链接包括**梅森素数**、**索菲·热尔曼素数**、**费马素数**和**回文素数**等分类。典型的新闻列表被数字序列和数学符号（如 $e \leq k^2$）所取代。

页脚延续了这一主题，将标准的创业相关链接替换为数学替代方案。例如，“申请 YC”（Y Combinator）链接被替换为“申请 $\zeta$”（引用黎曼 ζ 函数），而其他链接则改为“纯数学”、“确定性”和“安全”。

总的来说，本文呈现了一个风格独特的“数学主题”版 Hacker News 平台，迎合了纯数学和素数理论爱好者的兴趣。

---

## 3. 日历

**原文标题**: Calendar

**原文链接**: [https://neatnik.net/calendar/?year=2026](https://neatnik.net/calendar/?year=2026)

本文介绍了一款由 Neatnik 设计的 2026 年极简可打印日历。该工具的核心特点是无论纸张尺寸如何，都能将全年的日期展示在单张纸上。

**关键信息与使用提示：**
*   **最佳打印效果：** 为了获得最佳视觉效果，建议用户将打印方向设置为**横向**，并禁用页眉和页脚。
*   **设计理念：** 该版式旨在提供全年的整体视图，方便用户追踪时间流逝、记录笔记并提前规划。其紧凑的设计使其易于折叠和携带。
*   **补充内容：** 页面包含了 2026 年全部 12 个月的完整日期和星期网格，并以一句简短的寄语“善待他人”作为结尾。

本质上，该页面为那些寻求实体的、单页式全年概览的用户提供了一个功能性强且简洁实用的工具。

---

## 4. tc-ematch(8) 用于 "basic"、"cgroup" 或 "flow" 过滤器的扩展匹配

**原文标题**: tc-ematch(8) extended matches for use with "basic", "cgroup" or "flow" filters

**原文链接**: [https://man7.org/linux/man-pages/man8/tc-ematch.8.html](https://man7.org/linux/man-pages/man8/tc-ematch.8.html)

**tc-ematch(8)** 手册页描述了“扩展匹配”（extended matches），这是一种用于 Linux 流量控制（`tc`）的灵活架构，旨在增强 **basic**、**cgroup** 和 **flow** 过滤器的过滤能力。这些匹配允许通过逻辑运算符（**and**、**or**、**not**）和括号组合多个条件，从而实现复杂的报文分类。

主要匹配模块包括：

*   **cmp**：在特定偏移量和层（链路层、网络层或传输层）上对报文数据进行算术比较（eq、lt、gt）。
*   **meta**：匹配报文元数据，例如 Netfilter 标记（`nf_mark`）、VLAN 标签、接口索引、系统平均负载或内核套接字缓冲区属性。
*   **nbyte**：在报文内指定的偏移量处搜索特定的字节序列或字符串。
*   **u32**：对报文数据提供基于位掩码的匹配，类似于独立的 u32 过滤器。
*   **ipset**：检查报文头（如源或目的 IP）是否属于定义的 `ipset`。
*   **ipt**：允许在 `tc` 框架内使用标准的 `xtables` (iptables) 匹配扩展。
*   **canid**：专门用于匹配控制器局域网 (CAN) 帧标识符。

**使用注意事项：**
由于 ematch 语法使用括号对表达式进行分组，用户必须在 shell 中对其进行转义，以避免命令行解析错误。该实用程序是 **iproute2** 套件的一部分，对于高级网络流量整形至关重要，它允许管理员根据报文内容和系统元数据制定极具针对性的报文处理规则。

---

## 5. Hungry Fat Cells Could Someday Starve Cancer to Death

**原文标题**: Hungry Fat Cells Could Someday Starve Cancer to Death

**原文链接**: [https://www.ucsf.edu/news/2025/01/429411/how-hungry-fat-cells-could-someday-starve-cancer-death](https://www.ucsf.edu/news/2025/01/429411/how-hungry-fat-cells-could-someday-starve-cancer-death)

生成摘要时出错

---

## 6. 用纯 HTML 替换 JavaScript

**原文标题**: Replacing JavaScript with Just HTML

**原文链接**: [https://www.htmhell.dev/adventcalendar/2025/27/](https://www.htmhell.dev/adventcalendar/2025/27/)

在《仅用 HTML 替代 JavaScript》一文中，Aaron T. Grogg 指出，虽然 JavaScript (JS) 传统上一直是实现网页交互的核心工具，但开发者现在应优先为常见 UI 组件采用原生的 HTML 和 CSS 特性。减少对 JS 的依赖可以通过降低浏览器的下载、解压和内存处理负担来提升性能。

Grogg 重点介绍了原生 HTML 可以替代 JS 的四个具体领域：

*   **手风琴/可展开内容：** `<details>` 和 `<summary>` 元素提供了内置的显示/隐藏功能。通过使用 `name` 属性，开发者可以创建“排他性手风琴”（即一次只能打开一个面板），从而模拟单选按钮的行为。
*   **自动筛选建议：** 将 `<input>` 与 `<datalist>` 结合使用，可以创建一个在用户输入时自动过滤选项的功能性下拉框。这适用于文本、数字和时间输入，无需编写自定义筛选脚本。
*   **模态框与弹出框：** 新的 `popover` 和 `popovertarget` 属性支持轻松切换元素状态。它们支持“轻量化关闭”（通过 Esc 键或点击外部关闭），并提供 `auto`、`hint` 和 `manual` 等模式来控制覆盖层之间的交互。
*   **离屏导航：** 通过结合使用 Popover API 和 CSS 变换（如 `translate`），开发者可以创建侧边菜单和抽屉组件。这种方法利用了浏览器的原生定位能力，并能方便地设置背景遮罩样式。

Grogg 总结道，虽然 JS 对于处理复杂任务仍然必不可少，但将 UI 管理交给原生 HTML 和 CSS 可以构建出更精简、更高效的网站。通过充分利用浏览器的原生能力，开发者可以用更少的代码提供更好的用户体验。

---

## 7. 开发一个 macOS 应用，用于监测 Mac 何时出现过热降频

**原文标题**: Building a macOS app to know when my Mac is thermal throttling

**原文链接**: [https://stanislas.blog/2025/12/macos-thermal-throttling-app/](https://stanislas.blog/2025/12/macos-thermal-throttling-app/)

无法访问文章链接。

---

## 8. 记录 tada 清单的一年

**原文标题**: One year of keeping a tada list

**原文链接**: [https://www.ducktyped.org/p/one-year-of-keeping-a-tada-list](https://www.ducktyped.org/p/one-year-of-keeping-a-tada-list)

In "One year of keeping a tada list," Aditya Bhargava reflects on his experience maintaining a "to-done" list—a daily log of accomplishments designed to shift focus from pending tasks to completed successes. Bhargava’s method involved daily entries on monthly pages, capped off with a summary drawing of his achievements.

**Key Benefits:**
The practice provided a psychological counterweight to the "what's next?" mentality, forcing the author to celebrate milestones he would otherwise overlook. Most importantly, the list helped him visualize the "why" behind his progress. For example, he realized that the successful creation of Minnesota landscape cards was only possible because of months spent on pigment mixing and value studies. Similarly, his software projects were built upon libraries he had developed earlier in the year. The list served as a reminder that learning new skills is a cumulative process.

**Drawbacks:**
The practice was not without stress. Bhargava noted that the list created a "pressure to perform" every day just to have something to record. Furthermore, maintaining the habit for a full year led to burnout; by the end of the year, his entries became less frequent, and he stopped creating the monthly summary drawings.

**Conclusion:**
While the tada list acts as a valuable archive of forgotten efforts and helps reinforce the value of the learning process, the author is undecided about continuing it. He concludes that the motivational benefits must be weighed against the effort required to maintain the habit.

---

## 9. Designing Predictable LLM-Verifier Systems for Formal Method Guarantee

**原文标题**: Designing Predictable LLM-Verifier Systems for Formal Method Guarantee

**原文链接**: [https://arxiv.org/abs/2512.02080](https://arxiv.org/abs/2512.02080)

生成摘要时出错

---

## 10. Floor796

**原文标题**: Floor796

**原文链接**: [https://floor796.com/](https://floor796.com/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 2 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 3 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 4 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 5 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 6 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 7 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 8 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 9 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 10 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 11 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 12 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 13 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 14 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 15 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 16 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 17 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 18 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 19 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 20 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 21 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 22 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 23 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 24 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 25 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 26 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 27 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 28 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 29 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 30 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 31 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 32 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 33 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 34 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 35 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 36 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 37 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 38 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 39 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 40 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 41 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 42 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 43 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 44 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 45 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 46 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 47 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 48 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 49 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 50 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 51 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 52 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 53 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 54 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 55 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 56 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 57 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 58 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 59 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 60 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 61 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 62 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 63 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 64 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 65 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 66 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 67 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 68 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 69 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 70 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 71 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 72 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 73 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 74 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 75 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 76 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 77 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 78 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 79 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 80 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 81 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 82 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 83 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 84 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 85 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 86 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 87 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 88 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 89 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 90 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 91 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 92 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 93 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 94 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 95 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 96 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 97 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 98 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 99 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 100 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 101 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 102 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 103 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 104 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 105 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 106 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 107 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 108 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 109 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 110 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 111 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 112 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 113 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 114 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 115 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 116 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 117 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 118 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 119 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 120 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 121 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 122 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 123 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 124 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 125 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 126 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 127 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 128 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 129 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 130 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 131 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 132 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 133 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 134 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 135 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 136 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 137 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 138 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 139 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 140 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 141 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 142 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 143 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 144 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 145 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 146 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 147 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 148 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 149 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 150 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 151 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 152 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 153 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 154 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 155 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 156 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 157 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 158 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 159 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 160 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 161 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 162 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 163 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 164 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 165 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 166 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 167 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 168 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 169 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 170 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 171 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 172 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 173 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 174 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 175 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 176 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 177 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 178 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 179 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 180 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 181 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 182 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 183 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 184 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 185 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 186 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 187 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 188 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 189 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 190 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 191 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 192 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 193 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 194 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 195 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 196 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 197 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 198 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 199 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 200 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 201 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 202 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 203 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 204 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 205 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 206 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 207 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 208 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 209 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 210 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 211 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 212 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 213 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 214 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 215 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 216 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 217 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 218 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 219 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 220 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 221 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 222 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 223 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 224 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 225 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 226 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 227 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 228 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 229 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 230 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 231 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 232 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 233 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 234 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 235 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 236 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 237 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 238 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 239 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 240 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 241 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 242 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 243 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 244 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 245 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 246 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 247 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 248 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 249 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 250 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 251 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 252 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 253 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 254 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 255 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 256 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 257 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 258 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 259 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 260 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 261 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 262 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 263 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 264 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 265 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 266 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 267 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 268 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 269 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 270 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 271 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 272 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 273 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 274 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 275 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 276 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 277 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 278 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 279 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 280 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 281 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 282 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 283 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
