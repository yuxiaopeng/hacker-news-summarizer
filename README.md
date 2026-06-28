# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-06-28.md)

*最后自动更新时间: 2026-06-28 18:34:25*
## 1. 我用 Claude Code 获取了关于我 MRI 的第二意见。

**原文标题**: I used Claude Code to get a second opinion on my MRI

**原文链接**: [https://antoine.fi/mri-analysis-using-claude-code-opus](https://antoine.fi/mri-analysis-using-claude-code-opus)

在本文中，作者详细介绍了一项利用 Claude Code (Opus 4.8) 获取肩部核磁共振（MRI）第二诊疗意见的实验。在遭受持续疼痛后，一名人类骨科医生诊断作者患有肩胛下肌腱“III 级部分撕裂”。然而，当 ChatGPT 5.5 Pro 指出诊所建议的即时治疗方案——冲击波疗法和 Traumeel 注射——可能不合适或针对该特定病情缺乏适应症时，作者产生了怀疑。

为了进一步探究，作者使用 Claude Code 分析了 MRI 的原始 DICOM 文件。与标准的聊天机器人不同，该界面允许 AI 安装软件包并运行代码，从而对数据进行系统性的审查。结果令人震惊：Opus 4.8 得出结论称肌腱“完好无损”，这与人类放射科医生关于严重撕裂的诊断直接矛盾。

为了解决这一分歧，作者启动了一个“仲裁”流程，由 Claude 调用多个子代理进行双盲、公正的审查。这项二次 AI 分析以极高的置信度确认，并没有明显的撕裂，仅存在轻度的肌腱病。

作者总结道，虽然 AI 能够针对潜在的“重干预性”或不成熟的人类诊断提供严谨且极具参考价值的复核，但它也会让患者陷入一种“悬而不决”的状态。尽管 AI 的发现表明医生可能“操之过急”，但作者指出，AI 目前尚不能取代医疗专业人员。这项实验预示了一个 AI 可能会常规化审计医疗诊断的未来，尽管在当下，它也给夹在冲突专家意见之间的患者带来了新的不确定性。

---

## 2. 1880-1920年间5000份餐厅菜单

**原文标题**: 5k Restaurant Menus, Years 1880-1920

**原文链接**: [https://pudding.cool/2026/06/menu-collection/](https://pudding.cool/2026/06/menu-collection/)

本文介绍了一个数字档案馆，其中收录了1880年至1920年间的**5,000份餐厅菜单**。这一历史数据库全面展示了19世纪末至20世纪初的烹饪趋势、饮食习惯和食品价格。

该馆藏的主要特色包括：

*   **按年代浏览：** 用户可以按年份检索馆藏，从而对比研究菜单在40年间的演变。
*   **AI增强信息：** 为帮助现代读者理解晦涩或陈旧的烹饪术语，平台利用**AI生成的菜品定义**提供背景支持。这些信息有助于弥合历史术语与当代理解之间的鸿沟。
*   **交互式界面：** 数字展厅包含“返回”、“下一页”和“展开”等标准导航工具，方便用户探索高分辨率的菜单图像。

对于关注全球历史变革时期美食演化和餐饮业的历史学家、社会学家及美食爱好者而言，这一资源是一项重要的研究工具。

---

## 3. 在龙梦逸珑笔记本和 OpenBSD 上与“龙”共舞

**原文标题**: Working around dragons with the Lemote Yeeloong laptop and OpenBSD

**原文链接**: [http://oldvcr.blogspot.com/2026/06/working-around-dragons-with-lemote.html](http://oldvcr.blogspot.com/2026/06/working-around-dragons-with-lemote.html)

本文探讨了龙梦逸珑（Lemote Yeeloong）的历史与技术演进。这是一款独特的中国国产笔记本电脑，搭载了兼容 MIPS64 的龙芯（Loongson，原称 Godson）处理器。作者的兴趣源于该设备在自由软件社区中的声望——理查德·斯托曼（Richard Stallman）曾使用过它——因为它无需私有二进制块或固件即可运行，是运行 OpenBSD 的理想平台。

该处理器的起源可追溯至中国的“863计划”，该计划于 1986 年启动，旨在培育本土高科技产业并减少对外国芯片的依赖。2001 年，中国科学院计算技术研究所开始设计“龙芯”系列 CPU。虽然最初为了规避专利冲突而采用了类似 32 位 MIPS II 的架构，但该项目经历了多次迭代：

*   **龙芯1号 (2002)：** 一款低功耗 32 位芯片，早期曾面临与 MIPS 公司的商标和许可争议。
*   **龙芯2号系列：** 向 MIPS III 兼容迈进的 64 位扩展版本。**龙芯2E** (2006) 通过与意法半导体（STMicroelectronics）合作，主频达到了 1GHz。
*   **龙芯2F (2007)：** 首个获得 MIPS “正式”授权的版本，集成了北桥并提升了能效。

这些芯片的商业化促成了龙梦（Lemote）公司的成立。这家合资企业推出了福珑（Fuloong）台式机，并于 2008 年 10 月发布了**逸珑（Yeeloong）笔记本电脑**。逸珑作为全球首款基于龙芯的笔记本电脑上市，将 2F 处理器与 AMD 南桥和瑞昱（Realtek）网卡等通用组件相结合。

最后，本文将逸珑定义为中国计算机史上的重要里程碑，也是令技术极客们趋之若鹜的“极客杀手”。对于那些寻求高度便携、完全自由且架构独特，以便在 OpenBSD 等替代操作系统上进行实验的爱好者来说，它是一款理想的机器。

---

## 4. 台杉：日本“树中生树”的培育技艺 (2020)

**原文标题**: Daisugi, the Japanese technique of trees out of trees (2020)

**原文链接**: [https://www.openculture.com/2020/10/daisugi.html](https://www.openculture.com/2020/10/daisugi.html)

起源于15世纪的京都，“台杉”（Daisugi，意为“平台杉”）是一项精妙的日本林业技术，其核心在于让树木从现有的树木之上生长。作为对土地和树苗短缺的一种应对方案，该方法的原理类似于巨型盆栽。通过修剪基底杉树，使其形状如同张开的手掌，林业工作者可以从单一树干上培育出多根垂直向上生长的侧枝。

在16世纪，受茶道大师千利休的需求以及“数寄屋造”建筑风格盛行的推动，这项技术声名大噪。当时，贵族和武士渴望在宅邸中使用高品质的北山杉，但原材料供应紧缺。台杉提供了一种巧妙的解决方案，既能产出木材，又无需占用大量土地或面临森林砍伐的风险。

由此产出的木材被称为“垂木”（Taruki），因其兼具美学价值和卓越的结构性能而备受推崇。由于这种特殊的培育方式，该木材的韧性是普通杉木的140%，密度和强度则是其200%。这些特性使得木材极为笔直、纤细且抗风能力强，是传统日本茶室椽子和屋顶用材的理想选择。

在其诞生六个世纪后的今天，台杉依然是可持续工艺的典范，这种产出高品质材料的方法至今仍令世界惊叹。

---

## 5. 人工智能时代的软件工程思考

**原文标题**: Reflections on Software Engineering in the Age of AI

**原文链接**: [https://adiamond.me/2026/06/software-engineering-in-the-age-of-ai/](https://adiamond.me/2026/06/software-engineering-in-the-age-of-ai/)

In "Reflections on Software Engineering in the Age of AI," the author—a software engineer and novelist—explores how generative AI is fundamentally altering the nature of creative work. While AI can efficiently produce "pretty good" code, it has shifted the developer’s role from a creator to a supervisor or editor. 

The author argues that this shift destroys the "flow state"—the deep, immersive engagement described by psychologist Mihaly Csikszentmihalyi. By offloading the "hard thinking" to AI, developers suffer from skill atrophy, becoming "lazier and stupider" as they lose the drive to solve complex problems manually. 

A significant systemic concern raised is the "pipeline problem." Because companies are replacing junior developers with AI, the industry is failing to train the next generation of senior engineers. Without "doing the work," new engineers will lack the institutional and systems-level knowledge required to manage the massive, complex codebases that AI cannot fully grasp. The author uses a U.S. Navy analogy: just as the Navy must build ships they don't need simply to preserve the craftsmanship, the software industry must write code to maintain its expertise.

Ultimately, the author warns of a future filled with "digital plastic"—vast amounts of AI-generated content and code that "just works" for now but is poorly understood and difficult to maintain. He concludes that while software development has been reduced to a reactive task, individuals must reclaim their "flow" through non-automated pursuits like writing, reading, and human connection to preserve their capacity for original thought and imagination.

---

## 6. Examining circuit boards from the Space Shuttle's I/O Processor

**原文标题**: Examining circuit boards from the Space Shuttle's I/O Processor

**原文链接**: [https://www.righto.com/2026/06/space-shuttle-io-processor-boards.html](https://www.righto.com/2026/06/space-shuttle-io-processor-boards.html)

生成摘要时出错

---

## 7. Tokenmaxxing is dead, long live Tokenmaxxing

**原文标题**: Tokenmaxxing is dead, long live Tokenmaxxing

**原文链接**: [https://12gramsofcarbon.com/p/agentics-tech-things-tokenmaxxing](https://12gramsofcarbon.com/p/agentics-tech-things-tokenmaxxing)

生成摘要时出错

---

## 8. Show HN: Zanagrams

**原文标题**: Show HN: Zanagrams

**原文链接**: [https://zanagrams.com/](https://zanagrams.com/)

生成摘要时出错

---

## 9. The curious case of the disappearing Polish S (2015)

**原文标题**: The curious case of the disappearing Polish S (2015)

**原文链接**: [https://aresluna.org/the-curious-case-of-the-disappearing-polish-s/](https://aresluna.org/the-curious-case-of-the-disappearing-polish-s/)

生成摘要时出错

---

## 10. The Boeing 747 Begins Its Final Descent

**原文标题**: The Boeing 747 Begins Its Final Descent

**原文链接**: [https://www.theatlantic.com/magazine/2026/07/boeing-747-retirement/687304/](https://www.theatlantic.com/magazine/2026/07/boeing-747-retirement/687304/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 2 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 3 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 4 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 5 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 6 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 7 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 8 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 9 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 10 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 11 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 12 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 13 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 14 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 15 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 16 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 17 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 18 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 19 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 20 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 21 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 22 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 23 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 24 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 25 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 26 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 27 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 28 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 29 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 30 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 31 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 32 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 33 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 34 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 35 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 36 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 37 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 38 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 39 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 40 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 41 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 42 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 43 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 44 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 45 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 46 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 47 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 48 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 49 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 50 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 51 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 52 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 53 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 54 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 55 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 56 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 57 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 58 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 59 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 60 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 61 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 62 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 63 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 64 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 65 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 66 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 67 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 68 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 69 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 70 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 71 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 72 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 73 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 74 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 75 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 76 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 77 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 78 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 79 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 80 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 81 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 82 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 83 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 84 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 85 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 86 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 87 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 88 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 89 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 90 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 91 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 92 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 93 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 94 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 95 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 96 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 97 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 98 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 99 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 100 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 101 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 102 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 103 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 104 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 105 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 106 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 107 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 108 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 109 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 110 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 111 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 112 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 113 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 114 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 115 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 116 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 117 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 118 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 119 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 120 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 121 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 122 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 123 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 124 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 125 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 126 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 127 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 128 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 129 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 130 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 131 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 132 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 133 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 134 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 135 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 136 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 137 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 138 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 139 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 140 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 141 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 142 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 143 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 144 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 145 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 146 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 147 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 148 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 149 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 150 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 151 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 152 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 153 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 154 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 155 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 156 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 157 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 158 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 159 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 160 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 161 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 162 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 163 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 164 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 165 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 166 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 167 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 168 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 169 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 170 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 171 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 172 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 173 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 174 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 175 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 176 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 177 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 178 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 179 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 180 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 181 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 182 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 183 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 184 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 185 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 186 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 187 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 188 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 189 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 190 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 191 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 192 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 193 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 194 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 195 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 196 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 197 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 198 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 199 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 200 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 201 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 202 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 203 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 204 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 205 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 206 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 207 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 208 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 209 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 210 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 211 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 212 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 213 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 214 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 215 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 216 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 217 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 218 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 219 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 220 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 221 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 222 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 223 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 224 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 225 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 226 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 227 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 228 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 229 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 230 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 231 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 232 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 233 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 234 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 235 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 236 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 237 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 238 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 239 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 240 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 241 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 242 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 243 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 244 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 245 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 246 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 247 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 248 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 249 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 250 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 251 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 252 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 253 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 254 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 255 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 256 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 257 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 258 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 259 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 260 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 261 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 262 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 263 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 264 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 265 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 266 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 267 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 268 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 269 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 270 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 271 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 272 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 273 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 274 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 275 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 276 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 277 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 278 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 279 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 280 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 281 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 282 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 283 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 284 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 285 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 286 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 287 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 288 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 289 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 290 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 291 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 292 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 293 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 294 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 295 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 296 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 297 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 298 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 299 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 300 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 301 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 302 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 303 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 304 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 305 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 306 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 307 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 308 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 309 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 310 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 311 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 312 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 313 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 314 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 315 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 316 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 317 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 318 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 319 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 320 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 321 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 322 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 323 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 324 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 325 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 326 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 327 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 328 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 329 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 330 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 331 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 332 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 333 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 334 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 335 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 336 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 337 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 338 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 339 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 340 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 341 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 342 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 343 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 344 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 345 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 346 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 347 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 348 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 349 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 350 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 351 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 352 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 353 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 354 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 355 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 356 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 357 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 358 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 359 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 360 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 361 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 362 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 363 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 364 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 365 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 366 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 367 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 368 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 369 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 370 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 371 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 372 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 373 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 374 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 375 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 376 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 377 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 378 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 379 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 380 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 381 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 382 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 383 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 384 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 385 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 386 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 387 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 388 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 389 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 390 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 391 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 392 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 393 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 394 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 395 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 396 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 397 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 398 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 399 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 400 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 401 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 402 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 403 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 404 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 405 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 406 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 407 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 408 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 409 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 410 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 411 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 412 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 413 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 414 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 415 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 416 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 417 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 418 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 419 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 420 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 421 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 422 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 423 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 424 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 425 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 426 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 427 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 428 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 429 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 430 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 431 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 432 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 433 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 434 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 435 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 436 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 437 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 438 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 439 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 440 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 441 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 442 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 443 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 444 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 445 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 446 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 447 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 448 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 449 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 450 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 451 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 452 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 453 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 454 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 455 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 456 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 457 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 458 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 459 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 460 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 461 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 462 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 463 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 464 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 465 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
