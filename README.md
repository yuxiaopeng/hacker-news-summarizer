# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-06-07.md)

*最后自动更新时间: 2026-06-07 18:34:12*
## 1. 孕期维生素D3与10岁时的认知表现

**原文标题**: Vitamin D3 During Pregnancy and Cognitive Performance at 10 Years

**原文链接**: [https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2849122](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2849122)

本研究是COPSAC2010随机临床试验的随访研究，旨在探讨孕期补充高剂量维生素D3是否能改善儿童的长期认知发育。虽然已知维生素D对大脑发育至关重要，但此前关于产前高剂量补充对神经发育益处的证据尚无定论。

该试验将妊娠24周的孕妇随机分配到高剂量组（2,800 IU/d）或标准剂量组（400 IU/d）接受维生素D3补充。在子女10岁时，研究人员采用韦氏儿童智力量表第五版（WISC-V）对496名后代的认知表现进行了评估。该评估涵盖全量表智商（FSIQ）及五个特定认知领域：言语理解、视觉空间、流体推理、工作记忆和加工速度。

结果显示，高剂量组（平均智商103.3）与标准剂量组（平均智商103.5）儿童的全量表智商无显著差异。此外，在五个特定认知指标上均未观察到显著差异。亚组分析（综合考虑了母亲基线维生素D水平、儿童性别及出生季节等因素）同样表明，更高剂量并未带来额外获益。

综上所述，研究发现，在孕中晚期增加维生素D3摄入量至超过标准推荐剂量，并不能进一步提升儿童10岁时的认知表现。这些发现表明，现行的产前维生素D推荐标准足以支持儿童长期的神经发育。

---

## 2. 克隆森海塞尔 BA2015 电池组

**原文标题**: Cloning a Sennheiser BA2015 battery pack

**原文链接**: [https://blog.brixit.nl/cloning-a-sennheiser-ba2015-accu-pack/](https://blog.brixit.nl/cloning-a-sennheiser-ba2015-accu-pack/)

本文探讨了森海塞尔 BA2015 电池包的高昂成本及其逆向工程。这种专用电池包广泛用于多种无线麦克风，虽然森海塞尔的售价高达 80 至 100 美元，但作者揭示其本质仅为两节标准镍氢 AA 电池和一个装在塑料外壳内的廉价 NTC 温度传感器。

森海塞尔所宣传的“集成传感器”实际上只是一个基础的 10kΩ NTC 电阻（成本约为 0.02 美元）。该传感器起到了识别开关的作用：它向麦克风内部的充电电路发出信号，确认已插入兼容的电池包，从而允许在底座上充电——为了防止给碱性电池误充电，使用标准 AA 电池时该功能会被禁用。

作者通过逆向工程分析尺寸，并使用 OpenSCAD 3D 打印定制外壳，成功“克隆”了该电池包。这个 DIY 作品使用了松下电池、一小块用来模拟纽扣式触点的磁铁，以及一根弯曲的曲别针作为内部接线。虽然总组件成本仅约 5 美元，但作者指出制作过程非常繁琐，且 3D 打印外壳的耐用性不及官方或第三方替代品。

最终，该项目凸显了官方配件极高的利润空间。尽管作者得出的结论是购买第三方替代品对大多数用户而言更切实际，但此次拆解证明，这些昂贵电池包内部所谓的“专利”技术其实异常简单，且复制成本极低。

---

## 3. 为1948年的IBM 604电子计算器模块上电

**原文标题**: Powering up a module from the IBM 604: an electronic calculator from 1948

**原文链接**: [https://www.righto.com/2026/06/ibm-604-thyraton-tube-module.html](https://www.righto.com/2026/06/ibm-604-thyraton-tube-module.html)

本文探讨了1948年问世的**IBM 604电子计算穿孔机**的历史意义与技术设计。作为机电制表机与通用电子计算机时代之间的过渡产物，604是一款利用电子管每秒执行60次运算的可编程计算器。尽管它缺乏存储程序——而是依赖物理插接板进行编程——但凭借出色的性价比和运算速度，其产量超过5,600台，在商业上取得了巨大成功。

604的一项重大创新是**可插拔模块**。不同于早期构建在扁平金属底座上的电子设备，IBM的模块是紧凑的三维单元，包含一个电子管及其相关的电阻和电容。这种标准化设计实现了大规模生产并简化了维护工作，因为故障模块可以被备件快速替换。

作者通过为特定的**闸流管模块**（2D21型）通电演示了这些原理。闸流管不同于标准的三极管，因为它们含有少量氙气，使其能够充当高电流开关。在604中，这些模块被用于驱动继电器线圈和穿孔磁铁等重型机械部件。一旦被微弱信号触发，管内气体就会电离，电子管将保持“导通”状态，直到电源被物理切断——作者在视频中使用灯泡电路复现了这一特性。

最终，IBM 604成为了IBM至关重要的跨越基石。从其电子管电路和模块化设计中积累的专业经验，直接推动了700系列以及**IBM 650**的研发，后者也成为了20世纪50年代应用最广泛的通用计算机。

---

## 4. LLM 正在侵蚀我的软件工程职业生涯，我不知该如何是好

**原文标题**: LLMs are eroding my software engineering career and I don't know what to do

**原文链接**: [https://human-in-the-loop.bearblog.dev/llms-are-eroding-my-software-engineering-career-and-i-dont-know-what-to-do/](https://human-in-the-loop.bearblog.dev/llms-are-eroding-my-software-engineering-career-and-i-dont-know-what-to-do/)

这篇撰写于2026年6月的推测性文章，探讨了一位资深软件工程师在LLM（大语言模型）和代理工作流（agentic workflows）瓦解传统职业价值支柱时所面临的生存危机。凭借在复杂的金融和支付处理领域积累的十年经验，作者指出了人类专业知识正逐渐过时的三个具体领域：

1.  **领域知识：** 诸如PCI合规性、幂等性、账本逻辑等专业知识曾是核心竞争优势。如今，先进的LLM能够瞬间综合这些信息，生成架构设计文档和实施方案，将深厚的行业知识转化为一种“可通过提示词获取”的商品。
2.  **调试与分布式系统：** 作者此前将解决复杂调试难题视为终极的“就业保障”。然而，随着“代理工作流”和模型上下文协议（MCP）的出现，AI能够“一次性”解决90%的Bug——包括竞态条件和未记录的API边缘情况，而这些在以前需要耗费人类数天的努力。
3.  **代码质量与架构：** 尽管LLM生成的代码依然杂乱，但行业标准正在发生变化。高层架构和“整洁代码”正被贬低为仅仅是个人“品味”。随着代码库越来越多地由机器编写并服务于机器，人类可读的“优等”代码已不再是企业的首要任务。

作者总结道，软件工程市场正迫使所有人转向通用型角色，随着供过于求，劳动力的经济价值随之下降。领域专长在招聘中不再具有差异化优势，这让作者担心自己十年的“汗水与泪水”已变得毫无用处。面对连AI研究都可能被自动化的未来，作者考虑彻底离开该领域，转行从事木工等体力活。

---

## 5. 第29届国际C语言混乱代码大赛 (IOCCC) 2025 获奖名单

**原文标题**: The 29th International Obfuscated C Code Contest (IOCCC) 2025 Winners

**原文链接**: [https://www.ioccc.org/2025/](https://www.ioccc.org/2025/)

第29届国际C语言混乱代码大赛（IOCCC）已公布2025年获奖名单。本届比赛的投稿量接近历史新高且代码质量极佳。这是该赛事在中断四年后的第二次回归，得益于现代化的评审流程以及对官方规则和指南的大幅重写。

**亮点与瞩目获奖者**
本届大赛上演了“帽子戏法的帽子戏法”，共有三位作者——远藤侑介（Yusuke Endoh）、Nick Craig-Wood和Don Yang——每人均获得了三个独立奖项。此外，大赛还迎来了首位来自台湾的获奖作者 jingp49。备受瞩目的作品包括：
*   **ncw1：** 一个GameBoy模拟器。
*   **cable：** 一台Subleq计算机。
*   **tompng：** 一个海洋声音发生器。
*   **endoh3：** 一个补丁/差异Quine（自产生程序）。
*   **uellenberg：** “Quine乒乓游戏”。

**新特性与社区互动**
针对2025年的作品，评委在“评审评注”中引入了“趣味挑战”。鼓励读者通过GitHub拉取请求（Pull Request）来解决这些挑战或提供改进建议。获奖程序也正通过YouTube频道“Our Favorite Universe”的系列短片进行展示。

**未来展望**
评委对所有参赛者付出的心血表示赞赏，并鼓励未获奖的选手完善作品并在下一届比赛中重新提交。第30届IOCCC计划于2026年底开启，预计截稿日期为2027年第一季度。

目前，2025年所有获奖作品的文档、源码和编译说明已发布在IOCCC官网上，提供网页格式和压缩包下载。在处理完初期的反馈后，评委们计划在开启下一届筹备工作前进入一段“IOCCC假期”。

---

## 6. Show HN: Lathe – 使用大模型学习新领域，而非直接跳过它

**原文标题**: Show HN: Lathe – Use LLMs to learn a new domain, not skip past it

**原文链接**: [https://github.com/devenjarvis/lathe](https://github.com/devenjarvis/lathe)

**Lathe** 是一款实验性工具，旨在将大语言模型（LLM）定位为个人教师，而非自动代码生成器。它专注于“从零到一”的技术学习，能够根据用户提示生成多章节的动手实践教程，并通过专门且简洁的本地 UI 进行浏览。与追求交付速度的典型 AI 工作流不同，Lathe 鼓励用户手动完成内容，以确保真正的理解。

该系统由一个提供本地 Web 界面的 Golang CLI，以及一套适配 Claude Code、Cursor 和 Codex 等交互式 LLM 环境的“技能”组成。用户可以通过触发 `/lathe` 生成系列教程、`/lathe-extend` 扩展新章节，并使用 `/lathe-verify` 验证生成的代码是否能够实际运行。

核心功能包括：
*   **专用 UI：** 一个用于阅读教程的本地环境，具备目录导航、辅助深度思考的边注以及练习环节。
*   **可定制的“语气”：** 用户可以选择不同的叙述风格，如“平白直叙”或第一人称的“伴学伙伴”，甚至可以自定义风格。
*   **溯源与透明度：** 每份教程都会记录所使用的具体模型、引用的研究来源以及“语气”规范，以保持清晰的创作边界。
*   **离线管理：** 以 JSON 和 Markdown 格式存储的可搜索本地库。

开发者创建 Lathe 是为了找回 2000 年代编程教程中那种“豁然开朗”的时刻，特别是针对那些人类编写资源稀缺的冷门或新兴领域。虽然承认 LLM 存在幻觉风险，但 Lathe 认为手动参与——亲自输入代码——能让用户更容易发现并从错误中学习，最终实现对复杂技术概念的深度内化。

---

## 7. Anthropic，请发布官方 Linux 版 Claude Desktop。

**原文标题**: Anthropic, please ship an official Claude Desktop for Linux

**原文链接**: [https://github.com/anthropics/claude-code/issues/65697](https://github.com/anthropics/claude-code/issues/65697)

This GitHub issue (dated June 2026) formalizes a request for Anthropic to release an official Claude Desktop build for Linux, specifically targeting Ubuntu LTS and Debian. The petitioner argues that while the Claude Code CLI is available, the absence of a desktop GUI prevents Linux users from accessing critical features like "Computer Use," "Cowork," and the ability to develop and test desktop extensions.

The request outlines several core justifications:

*   **Technical Feasibility:** The author notes that Anthropic already maintains Linux distribution infrastructure for its CLI. Furthermore, technical analysis reveals that the "Cowork" feature on macOS and Windows actually operates within a Linux VM, meaning a Linux execution path already exists within the product.
*   **Security Concerns:** Because no official version exists, the community has turned to third-party repackages (such as `claude-desktop-debian`). The author argues that forcing users to entrust credentials and filesystem access to unvetted, unofficial builds creates a significant structural security risk.
*   **Market Demand:** Citing 2025 developer surveys, the author points out that nearly 28% of professional developers use Linux as their primary operating system. The lack of support creates unnecessary friction for a large segment of the developer community.
*   **Developer Ecosystem:** Developers building Claude Code plugins currently cannot test them as desktop extensions on Linux, discouraging contribution to the ecosystem from Linux-based workstations.

The proposed solution is the distribution of an official, signed `.deb` package via Anthropic’s existing repositories. If a build is not immediately possible, the author requests a public statement explaining the roadmap to provide clarity and security guidance to the community. The issue emphasizes that a "reasoned no" is preferable to the current silence.

---

## 8. Proliferate (YC S25) is hiring to building open source Codex

**原文标题**: Proliferate (YC S25) is hiring to building open source Codex

**原文链接**: [https://www.ycombinator.com/companies/proliferate/jobs/L3copvK-founding-engineer](https://www.ycombinator.com/companies/proliferate/jobs/L3copvK-founding-engineer)

生成摘要时出错

---

## 9. The gamers taking on the industry to stop it switching off games

**原文标题**: The gamers taking on the industry to stop it switching off games

**原文链接**: [https://www.bbc.com/news/articles/c8e8e7g0r82o](https://www.bbc.com/news/articles/c8e8e7g0r82o)

生成摘要时出错

---

## 10. Backrest – a web UI and orchestrator for restic backup

**原文标题**: Backrest – a web UI and orchestrator for restic backup

**原文链接**: [https://github.com/garethgeorge/backrest](https://github.com/garethgeorge/backrest)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 2 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 3 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 4 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 5 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 6 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 7 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 8 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 9 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 10 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 11 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 12 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 13 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 14 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 15 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 16 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 17 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 18 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 19 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 20 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 21 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 22 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 23 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 24 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 25 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 26 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 27 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 28 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 29 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 30 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 31 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 32 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 33 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 34 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 35 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 36 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 37 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 38 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 39 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 40 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 41 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 42 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 43 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 44 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 45 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 46 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 47 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 48 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 49 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 50 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 51 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 52 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 53 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 54 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 55 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 56 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 57 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 58 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 59 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 60 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 61 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 62 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 63 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 64 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 65 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 66 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 67 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 68 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 69 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 70 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 71 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 72 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 73 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 74 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 75 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 76 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 77 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 78 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 79 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 80 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 81 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 82 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 83 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 84 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 85 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 86 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 87 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 88 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 89 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 90 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 91 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 92 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 93 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 94 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 95 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 96 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 97 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 98 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 99 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 100 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 101 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 102 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 103 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 104 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 105 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 106 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 107 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 108 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 109 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 110 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 111 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 112 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 113 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 114 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 115 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 116 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 117 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 118 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 119 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 120 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 121 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 122 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 123 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 124 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 125 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 126 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 127 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 128 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 129 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 130 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 131 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 132 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 133 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 134 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 135 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 136 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 137 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 138 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 139 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 140 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 141 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 142 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 143 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 144 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 145 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 146 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 147 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 148 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 149 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 150 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 151 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 152 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 153 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 154 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 155 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 156 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 157 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 158 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 159 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 160 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 161 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 162 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 163 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 164 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 165 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 166 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 167 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 168 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 169 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 170 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 171 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 172 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 173 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 174 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 175 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 176 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 177 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 178 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 179 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 180 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 181 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 182 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 183 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 184 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 185 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 186 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 187 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 188 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 189 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 190 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 191 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 192 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 193 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 194 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 195 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 196 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 197 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 198 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 199 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 200 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 201 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 202 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 203 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 204 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 205 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 206 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 207 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 208 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 209 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 210 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 211 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 212 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 213 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 214 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 215 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 216 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 217 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 218 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 219 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 220 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 221 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 222 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 223 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 224 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 225 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 226 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 227 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 228 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 229 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 230 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 231 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 232 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 233 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 234 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 235 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 236 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 237 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 238 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 239 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 240 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 241 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 242 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 243 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 244 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 245 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 246 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 247 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 248 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 249 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 250 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 251 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 252 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 253 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 254 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 255 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 256 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 257 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 258 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 259 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 260 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 261 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 262 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 263 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 264 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 265 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 266 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 267 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 268 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 269 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 270 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 271 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 272 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 273 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 274 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 275 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 276 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 277 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 278 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 279 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 280 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 281 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 282 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 283 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 284 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 285 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 286 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 287 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 288 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 289 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 290 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 291 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 292 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 293 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 294 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 295 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 296 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 297 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 298 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 299 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 300 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 301 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 302 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 303 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 304 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 305 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 306 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 307 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 308 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 309 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 310 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 311 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 312 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 313 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 314 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 315 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 316 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 317 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 318 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 319 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 320 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 321 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 322 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 323 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 324 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 325 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 326 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 327 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 328 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 329 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 330 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 331 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 332 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 333 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 334 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 335 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 336 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 337 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 338 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 339 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 340 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 341 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 342 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 343 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 344 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 345 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 346 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 347 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 348 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 349 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 350 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 351 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 352 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 353 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 354 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 355 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 356 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 357 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 358 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 359 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 360 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 361 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 362 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 363 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 364 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 365 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 366 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 367 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 368 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 369 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 370 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 371 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 372 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 373 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 374 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 375 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 376 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 377 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 378 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 379 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 380 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 381 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 382 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 383 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 384 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 385 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 386 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 387 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 388 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 389 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 390 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 391 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 392 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 393 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 394 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 395 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 396 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 397 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 398 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 399 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 400 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 401 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 402 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 403 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 404 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 405 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 406 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 407 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 408 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 409 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 410 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 411 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 412 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 413 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 414 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 415 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 416 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 417 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 418 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 419 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 420 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 421 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 422 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 423 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 424 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 425 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 426 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 427 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 428 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 429 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 430 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 431 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 432 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 433 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 434 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 435 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 436 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 437 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 438 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 439 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 440 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 441 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 442 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 443 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 444 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
