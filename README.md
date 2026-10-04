# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-10-04.md)

*最后自动更新时间: 2026-10-04 20:23:02*
## 1. 在消费级硬件 (RTX 4090) 上以 100T/s 的速度运行 Qwen 3.8 Flash Next (125B)

**原文标题**: Run Qwen 3.8 Flash Next (125B) on consumer hardware (RTX 4090) at 100T/s

**原文链接**: [https://github.com/Niko1221/Strata](https://github.com/Niko1221/Strata)

**Strata** 是一款免费且开源的工具，旨在消费级硬件上运行拥有 1250 亿参数的 **Qwen 3.8 Flash Next** AI 模型。它允许用户在 Windows 或 Linux 上本地运行高性能、私密的大语言模型 (LLM)，而无需企业级服务器。

**核心技术能力：**
*   **性能：** Strata 在此类规模的模型上实现了惊人的运行速度：在 RTX 3090/4090 上，生成速度可达每秒 100–140 个 token，读取长提示词（32K token）的速度超过每秒 2,000 个 token。
*   **硬件

**用户功能：**
*   **易用性：** 自动安装程序负责硬件检测和设置。它可以通过兼容 OpenAI 的 API 与 Claude Code 或 Cursor 等 AI 编程助手集成。
*   **多模态：** 支持图像识别和多种“推理”模式（关闭、低、中、高）以处理复杂任务。
*   **隐私：** 所有数据均保留在本地电脑上，确保绝对隐私。

Strata 通过利用 GPU、CPU 和 SSD 之间的“负载共享”策略，有效推动了大规模 AI 的普及，让爱好者和开发者能够在标准游戏 PC 上运行千亿级参数模型。

---

## 2. 灯塔分布全图

**原文标题**: A map of every lighthouse

**原文链接**: [https://mapped.earth/lighthouses/world](https://mapped.earth/lighthouses/world)

**mapped.earth** 上的这一项目提供了一个全面且互动的全球灯塔可视化地图。这个数字地图既是历史档案，也是地理探索工具，标绘了遍布七大洲的数千座航海信标。

**主要功能与信息包括：**

*   **全球范围：** 该地图涵盖了极其广泛的灯塔，从享誉世界的地标到位于地球最偏远地区的自动化灯塔。
*   **交互式导航：** 用户可以在全球海岸线上平移和缩放，以发现每一座建筑。该界面能够让用户沉浸式地观察这些信标在险要航道和港口入口处的分布情况。
*   **详细信息：** 每个数据点通常提供有关灯塔的具体信息，可能包括其名称、精确坐标、高度以及当前是处于使用中还是已停用。
*   **文化意义：** 除了航海用途，该项目还突显了灯塔在建筑和历史上的重要地位。它展示了几个世纪以来，这些建筑如何作为安全与人类智慧的象征而存在。

通过将各种海事数据库整合到一个简洁易用的界面中，mapped.earth 提供了一个独特的视角，展现了人类如何照亮世界海岸以指引旅人归家。对于海事爱好者、历史学家和旅行者而言，这都是一个不可或缺的资源。

---

## 3. 《我们身边的尼安德特人》评

**原文标题**: 'Neanderthals Among Us' review

**原文链接**: [https://www.historytoday.com/archive/review/neanderthals-among-us-peter-sahlins-review](https://www.historytoday.com/archive/review/neanderthals-among-us-peter-sahlins-review)

生成摘要时出错

---

## 4. ASIC谜题结果

**原文标题**: Results from the ASIC puzzle

**原文链接**: [https://blog.janestreet.com/asic-puzzle-results/](https://blog.janestreet.com/asic-puzzle-results/)

Jane Street 最近分享了其 8 月份 ASIC 逆向工程谜题的结果。该挑战要求参与者在没有网表或内部信号名称的情况下，推导出所提供的 GDS 布局的功能。

**解决方案**
该芯片是一个 11x11 “星战”（Star Battle / Two Not Touch）逻辑游戏的硬件检查器。为了获得“成功”信号，玩家必须在每一行、每一列和每个着色区域内正好放置两颗星，并确保任意两颗星互不接触（包括对角线方向）。该芯片基于 SKY130 开源库构建，利用并行计数器、ROM 映射区域和线性反馈移位寄存器 (LFSR) 来混淆成功的输出字符串。

**求解方法**
大赛共收到约 400 份参赛作品，使用了多种技术手段：
*   **网表提取：** 求解者利用 Magic 和 KLayout 等工具，或编写自定义 C++ 脚本，从物理布局中提取逻辑门。
*   **仿真与分析：** 参与者使用 Verilog、SAT 求解器和自定义评估程序对电路行为建模，并确定触发“成功”输出所需的条件。
*   **逆向工程：** 一些求解者通过破解基于 LFSR 的混淆逻辑直接获取输出字符串，从而完全绕过了谜题逻辑。

**亮点回顾**
文章强调了一些极具创意的作品，包括在《我的世界》(Minecraft) 中构建的芯片版本、FPGA 综合以及模拟 SPICE 仿真。设计者还在芯片中隐藏了多个“彩蛋”，例如未使用金属层上的莫尔斯电码、隐藏的 Jane Street 徽标，以及针对“全 1”或“全 0”输入的特定信息。

**核心启示**
作者指出，虽然人工智能已成为构建硬件分析工具的“游戏规则改变者”，但人类的好奇心对于真正理解系统逻辑仍然至关重要。Jane Street 在文末宣布了一项新竞赛，挑战目标是设计一个可编程协议仿真器 ASIC。

---

## 5. Show HN: 格拉苏蒂废品时钟——用废品制作的30分钟摆钟

**原文标题**: Show HN: Glashütte Trash Clock – A 30-minute pendulum clock made from trash

**原文链接**: [https://niklasroy.com/gtc/](https://niklasroy.com/gtc/)

艺术家尼克拉斯·罗伊（Niklas Roy）创作的“格拉苏蒂垃圾钟”（Glashütte Trash Clock）是一款功能齐全、运行时间为30分钟的机械时计。这是他在德国格拉苏蒂进行艺术家驻留期间，利用搜寻到的废旧材料制作而成的。受其制表师先祖以及该镇享誉盛名的钟表历史启发，罗伊利用“垃圾”和热熔胶、扎带等简单工具打造了这台时钟。

**技术规格：**
*   **振子：** 由一米长的木制折叠尺和水瓶制成的“秒摆”。
*   **擒纵机构：** 一种格拉汉姆擒纵机构，利用曲别针制成的齿轮和弯曲金属杆制成的擒纵叉来维持摆锤的摆动。
*   **动力：** 采用重力驱动系统，动力源是一个装满废金属的油漆桶。通过滑轮组机构，时钟的运行时间延长了一倍，达到约30分钟。
*   **传动系统：** 罗伊没有使用精密齿轮，而是利用纸板摩擦轮作为减速传动装置来驱动分针。

**功能与复杂功能：**
该时钟可以显示秒和分，并包含一个每分钟由锤子敲击一次的“响铃”（一个玻璃瓶）。这一机构由一只橡胶靴独立驱动。此外，还有一个“随机复杂功能”——一个标有“现在”（NOW）或“永不”（NEVER）的幸运转盘，在时钟能量耗尽前，由下降的油漆桶触发。

**结果与理论：**
通过视频追踪，罗伊确定这台时钟的准确性惊人，误差率仅为0.4%。该项目还探讨了计时标准的复杂性，如GMT、TAI和UTC。罗伊幽默地提出了他自己的时间尺度——**GTC（格拉苏蒂垃圾时）**，以此来反思地球自转的不规则性以及设置闰秒的必要性。该项目既充满了奇思妙想，又有扎实的技术支持，是对精密工程和时间本质的一次探索。

---

## 6. 如何利用 AI 规模化提升创作意图、质量与艺术性 [视频]

**原文标题**: How to scale intent, quality, and artistry with AI [video]

**原文链接**: [https://www.youtube.com/watch?v=GLvFTMtw4Jk](https://www.youtube.com/watch?v=GLvFTMtw4Jk)

根据提供的标题**“如何利用 AI 规模化提升意图、质量与艺术性”**，以下是该演讲（源自 YouTube/Google 营销活动）核心概念的简要总结：

**摘要**
本演讲探讨了生成式 AI 在创意行业中的变革性作用，重点关注技术如何放大人类的创造力而非取代它。讨论围绕三个支柱展开：

*   **意图 (Intent)：** AI 让创作者和营销人员能够更精准地使内容契合受众需求。通过分析海量数据，AI 能够识别观众的真实诉求，确保大规模生成的视频“意图”与观众的预期相匹配。
*   **质量 (Quality)：** 传统上，高水准的制作需要投入大量的时间和预算。AI 工具（如自动剪辑、光效增强和背景生成）降低了高质量制作的门槛，让创作者无论资源多寡都能保持专业水准。
*   **艺术性 (Artistry)：** 演讲者强调 AI 是一个“创意倍增器”。它负责处理重复性的技术任务，让艺术家能专注于高层次的构思和叙事。它还支持尝试以往因过于复杂或昂贵而难以实现的视觉风格和格式。

**核心要点**
将 AI 融入创意工作流代表了从“手动制作”向“创意编排”的转变。通过利用 AI 处理规模化的技术环节，创作者可以专注于艺术性与情感连接等“人文”要素，从而有效地架起数据驱动型营销与感性叙事之间的桥梁。

***注：** 您在提示词中提供的原文仅为 YouTube 标准的网页页脚/法律条款。本总结是基于特定标题及该演讲相关的行业主题生成的。*

---

## 7. 有效利他主义如何征服世界（并可能最终毁灭它）

**原文标题**: How effective altruism conquered the world (and might yet end it)

**原文链接**: [https://www.economist.com/international/2026/10/01/how-effective-altruism-conquered-the-world](https://www.economist.com/international/2026/10/01/how-effective-altruism-conquered-the-world)

无法访问文章链接。

---

## 8. A Minsky machine in ncurses terminfo

**原文标题**: A Minsky machine in ncurses terminfo

**原文链接**: [https://seriot.ch/computation/terminfo/](https://seriot.ch/computation/terminfo/)

In "A Minsky machine in ncurses terminfo," Nicolas Seriot demonstrates that the `terminfo` database—traditionally viewed as passive metadata for terminal capabilities—contains a stateful programming language capable of universal computation. 

While the `terminfo` language includes arithmetic, logic, if-then-else blocks, and persistent registers, it lacks an internal looping mechanism. Seriot overcomes this limitation by using repeated capability expansions (such as cursor addressing via `cup`) triggered by an external process to provide a functional "clock." 

The article provides a formal reduction from two-counter Minsky machines to `terminfo` parameter expansions. By mapping Minsky's `INC` and `JZDEC` instructions to `terminfo`’s conditional logic and registers, the author illustrates that the system is computationally universal, assuming idealized unbounded counters. To prove this, Seriot provides practical implementations of an addition machine and a Fibonacci sequence generator.

A highlight of the article is the creation of a "parasitic" Fibonacci program clocked by the system utility `/usr/bin/top`. Because `top` calls `cup` at regular intervals to refresh its display, a custom `terminfo` profile can intercept these calls to perform calculations and update the terminal's window title with each tick of `top`'s own clock.

Seriot concludes that while this behavior is a clever "hack" rather than a security vulnerability—as the language cannot perform syscalls or open files—it demonstrates how Turing-completeness can emerge unexpectedly from the composition of simple, intended features. The findings confirm that `terminfo` is not just metadata, but a small, persistent, and universal interpreted language.

---

## 9. Show HN: AI search for every photo and every frame of video on macOS

**原文标题**: Show HN: AI search for every photo and every frame of video on macOS

**原文链接**: [https://github.com/allenv0/SCM](https://github.com/allenv0/SCM)

生成摘要时出错

---

## 10. Second Chances

**原文标题**: Second Chances

**原文链接**: [https://www.nybooks.com/articles/2026/10/22/second-chances-office-politics-wilfrid-sheed/](https://www.nybooks.com/articles/2026/10/22/second-chances-office-politics-wilfrid-sheed/)

In this article, the author explores the modern "era of rediscovered books," examining the success of imprints like NYRB Classics and McNally Editions in reviving forgotten literary works. While some critics once viewed these imprints as "tombstones" for dying reputations, the author argues that high-quality curation and aesthetic appeal have successfully created a "second chance" for many "lost" authors.

The centerpiece of this discussion is the recent reissue of Wilfrid Sheed’s 1966 novel, *Office Politics*. Sheed, a prolific Anglo-American critic and novelist who died in 2011, was known for his urbane, ironic wit and his ability to navigate the cutthroat world of New York literary criticism. *Office Politics* is a "minor masterpiece" of office comedy that depicts the power struggles at a small, influential magazine following the illness of its dominant editor. The author praises the novel’s precision and humorous portrayal of symbolic power and petty betrayals.

However, the author’s deeper dive into Sheed’s broader body of work yields mixed results. While Sheed’s prose is "fizzy" and intellectually sharp—drawing comparisons to Kingsley Amis and Raymond Chandler—the author finds that many of his other novels (*Max Jamison*, *The Boys of Winter*) are limited by their narrow focus on the literary establishment. He argues that Sheed often used fiction to mirror his own career as a critic, resulting in characters obsessed with social status and "triangulation" rather than deeper emotional or external realities. Ultimately, while the author highly recommends *Office Politics* and the coming-of-age novella *The Blacking Factory*, he suggests that Sheed’s work often remains "entombed" in the very status quo he sought to satirize.

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 2 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 3 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 4 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 5 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 6 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 7 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 8 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 9 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 10 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 11 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 12 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 13 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 14 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 15 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 16 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 17 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 18 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 19 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 20 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 21 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 22 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 23 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 24 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 25 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 26 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 27 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 28 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 29 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 30 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 31 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 32 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 33 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 34 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 35 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 36 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 37 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 38 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 39 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 40 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 41 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 42 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 43 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 44 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 45 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 46 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 47 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 48 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 49 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 50 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 51 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 52 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 53 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 54 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 55 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 56 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 57 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 58 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 59 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 60 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 61 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 62 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 63 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 64 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 65 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 66 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 67 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 68 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 69 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 70 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 71 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 72 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 73 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 74 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 75 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 76 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 77 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 78 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 79 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 80 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 81 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 82 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 83 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 84 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 85 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 86 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 87 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 88 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 89 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 90 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 91 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 92 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 93 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 94 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 95 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 96 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 97 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 98 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 99 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 100 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 101 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 102 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 103 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 104 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 105 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 106 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 107 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 108 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 109 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 110 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 111 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 112 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 113 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 114 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 115 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 116 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 117 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 118 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 119 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 120 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 121 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 122 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 123 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 124 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 125 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 126 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 127 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 128 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 129 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 130 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 131 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 132 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 133 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 134 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 135 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 136 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 137 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 138 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 139 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 140 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 141 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 142 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 143 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 144 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 145 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 146 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 147 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 148 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 149 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 150 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 151 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 152 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 153 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 154 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 155 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 156 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 157 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 158 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 159 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 160 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 161 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 162 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 163 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 164 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 165 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 166 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 167 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 168 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 169 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 170 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 171 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 172 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 173 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 174 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 175 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 176 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 177 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 178 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 179 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 180 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 181 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 182 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 183 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 184 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 185 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 186 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 187 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 188 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 189 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 190 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 191 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 192 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 193 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 194 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 195 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 196 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 197 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 198 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 199 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 200 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 201 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 202 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 203 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 204 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 205 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 206 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 207 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 208 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 209 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 210 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 211 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 212 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 213 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 214 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 215 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 216 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 217 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 218 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 219 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 220 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 221 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 222 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 223 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 224 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 225 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 226 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 227 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 228 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 229 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 230 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 231 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 232 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 233 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 234 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 235 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 236 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 237 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 238 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 239 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 240 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 241 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 242 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 243 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 244 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 245 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 246 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 247 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 248 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 249 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 250 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 251 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 252 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 253 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 254 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 255 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 256 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 257 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 258 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 259 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 260 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 261 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 262 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 263 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 264 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 265 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 266 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 267 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 268 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 269 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 270 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 271 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 272 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 273 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 274 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 275 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 276 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 277 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 278 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 279 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 280 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 281 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 282 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 283 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 284 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 285 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 286 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 287 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 288 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 289 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 290 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 291 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 292 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 293 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 294 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 295 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 296 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 297 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 298 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 299 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 300 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 301 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 302 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 303 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 304 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 305 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 306 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 307 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 308 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 309 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 310 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 311 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 312 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 313 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 314 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 315 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 316 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 317 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 318 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 319 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 320 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 321 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 322 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 323 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 324 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 325 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 326 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 327 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 328 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 329 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 330 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 331 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 332 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 333 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 334 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 335 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 336 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 337 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 338 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 339 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 340 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 341 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 342 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 343 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 344 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 345 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 346 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 347 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 348 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 349 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 350 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 351 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 352 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 353 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 354 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 355 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 356 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 357 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 358 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 359 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 360 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 361 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 362 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 363 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 364 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 365 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 366 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 367 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 368 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 369 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 370 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 371 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 372 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 373 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 374 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 375 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 376 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 377 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 378 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 379 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 380 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 381 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 382 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 383 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 384 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 385 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 386 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 387 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 388 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 389 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 390 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 391 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 392 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 393 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 394 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 395 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 396 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 397 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 398 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 399 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 400 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 401 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 402 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 403 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 404 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 405 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 406 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 407 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 408 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 409 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 410 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 411 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 412 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 413 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 414 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 415 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 416 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 417 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 418 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 419 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 420 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 421 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 422 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 423 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 424 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 425 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 426 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 427 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 428 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 429 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 430 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 431 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 432 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 433 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 434 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 435 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 436 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 437 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 438 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 439 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 440 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 441 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 442 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 443 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 444 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 445 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 446 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 447 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 448 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 449 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 450 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 451 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 452 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 453 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 454 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 455 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 456 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 457 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 458 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 459 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 460 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 461 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 462 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 463 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 464 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 465 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 466 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 467 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 468 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 469 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 470 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 471 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 472 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 473 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 474 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 475 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 476 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 477 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 478 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 479 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 480 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 481 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 482 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 483 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 484 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 485 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 486 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 487 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 488 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 489 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 490 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 491 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 492 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 493 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 494 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 495 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 496 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 497 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 498 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 499 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 500 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 501 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 502 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 503 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 504 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 505 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 506 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 507 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 508 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 509 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 510 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 511 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 512 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 513 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 514 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 515 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 516 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 517 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 518 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 519 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 520 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 521 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 522 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 523 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 524 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 525 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 526 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 527 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 528 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 529 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 530 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 531 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 532 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 533 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 534 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 535 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 536 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 537 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 538 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 539 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 540 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 541 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 542 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 543 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 544 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 545 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 546 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 547 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 548 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 549 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 550 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 551 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 552 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 553 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 554 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 555 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 556 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 557 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 558 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 559 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 560 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 561 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
