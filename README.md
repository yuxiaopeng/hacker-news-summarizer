# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-07-20.md)

*最后自动更新时间: 2026-07-20 19:30:53*
## 1. 中国的 AI 开源权重战略正在胜出

**原文标题**: China's open-weights AI strategy is winning

**原文链接**: [https://werd.io/american-ai-is-locked-down-and-proprietary-its-losing/](https://werd.io/american-ai-is-locked-down-and-proprietary-its-losing/)

本文认为，中国正通过采用“权重开放”（open-weights）战略，成功挑战美国在人工智能领域的主导地位。相比 OpenAI 和 Anthropic 等美国领军企业依靠封闭的专有模型获取利润，中国企业则通过发布便携、无需许可的模型来培育全球生态系统。

核心观点包括：

*   **护城河问题：** AI 模型本身几乎没有竞争“护城河”，因为它们极易被替代。真正的价值在于企业服务和基础设施。通过开放权重，中国将美国公司试图获利的层级变成了通用商品。
*   **化劣势为优势：** 美国对 GPU 的出口管制和数据法规阻碍了中国提供中心化的全球云服务。作为应对，中国转向了开放分发模式，使其技术能够无门槛地集成到全球制造业和研究领域。
*   **缩小差距：** 阿里巴巴和月之暗面（Moonshot）等中国公司的模型，目前正以更低的成本与美国前沿模型的性能平起平坐。报告显示，绝大多数 AI 初创公司已经在使用中国模型。
*   **战略讽刺：** 尽管中国常被视为“封闭”社会，但其对开源理念的利用比美国更有效。目前，美国公司受激励机制影响，倾向于通过封闭系统追求短期利润，作者认为这在长期战略上注定会失败。

作者总结指出，美国的领先优势正在迅速缩小。为了保持竞争力和保护国家利益，美国必须转变战略，从单纯的限制性措施转向支持开放、具有公益性质的 AI 基础设施。

---

## 2. 黑客抹除罗马尼亚土地登记数据库

**原文标题**: Hacker wipes Romania's land registry database

**原文链接**: [https://news.risky.biz/risky-bulletin-hacker-wipes-romanias-entire-land-registry-database/](https://news.risky.biz/risky-bulletin-hacker-wipes-romanias-entire-land-registry-database/)

生成摘要时出错

---

## 3. 超过30%的ArXiv新提交论文读起来像是AI写的

**原文标题**: Over 30% of new ArXiv submissions now read as AI-written

**原文链接**: [https://unslop.run/blog/measuring-ai-writing-on-arxiv](https://unslop.run/blog/measuring-ai-writing-on-arxiv)

一项针对 12,750 篇 arXiv 论文的研究显示，目前超过 30% 的新提交论文似乎是由机器撰写的。研究人员使用了一个误报率校准为 0.4% 的检测器（以 ChatGPT 问世前即 2021–2022 年的论文作为对照组），发现类 AI 文风在 2023 年后急剧上升，到 2026 年中期已达到约 32%。

AI 生成内容的普及程度在不同学科间存在显著差异：
*   **计算机科学：** 采用率最高，达 65%。
*   **定量生物学：** 56.3%。
*   **电气工程：** 51.3%。
*   **数学：** 最低，仅为 0.7%。

研究人员分析了正文全文而非仅看摘要，并指出摘要往往会掩盖 AI 的存在。他们强调了几个关键局限性：
1.  **下限值：** 报告的百分比可能是实际采用率的下限，因为检测器可能无法识别所有的生成模型或提示词。
2.  **学科盲点：** 数学领域接近于零的比例可能是由于“检测器盲点”造成的，因为该学科包含大量符号文本和定理证明结构，这与检测工具训练时所用的科学英语显著不同。
3.  **风格 vs. 署名：** “标记”仅表示文本读起来像是机器撰写的；它无法区分是整篇文档全由 AI 生成，还是仅经过了深度的 AI 辅助润色。

该研究得出结论，类机器写作风格的兴起是学术生产方式的真实转变，而非检测工具的误差，被标记论文的比例在 2026 年初达到了近 39% 的峰值。

---

## 4. Hyprland 0.55 宣布配置文件切换至 Lua

**原文标题**: Hyprland 0.55 announced the switch to Lua for its config files

**原文链接**: [https://hypr.land/news/update55/](https://hypr.land/news/update55/)

Hyprland 0.55 版本现已发布。作为该 Wayland 合成器的一个重要里程碑，本版本在配置架构和功能特性方面带来了重大变革。

**核心亮点：**
*   **Lua 配置：** 最显著的变化是配置文件转向 **Lua**。虽然旧的 Hyprlang 格式在未来几个版本中仍将获得支持，但建议用户尽快迁移。此次更新还引入了全新的 **Layout API**，允许用户直接在配置中定义自定义窗口布局。
*   **色彩管理与渲染：** 引入了**分屏 ICC 配置文件支持**，并将渲染器默认精度设为 **FP16**。这些改进提升了色彩准确度、HDR 处理能力以及屏幕共享性能。
*   **滚动与手势：** 默认支持对全屏窗口进行滚动。新增了原生触控板手势 (`scroll_move`)，以及针对光标的实时捏合缩放手势。
*   **视觉与功能增项：** 新增了“发光 (glow)”窗口装饰、设备标签、`confine_pointer` 窗口规则，以及多个用于窗口分组和布局操作的新调度器。
*   **破坏性变更：** 移除或重定位了部分配置选项。特别地，`dwindle:pseudotile` 和 `decoration:shadow:ignore_window` 已被移除，`misc:vfr` 则被移至 debug 分组。

这是该项目迄今为止规模最大的更新之一，涵盖了海量的代码改动与贡献者投入，并对官方 Wiki 进行了全面翻新，以适配全新的 Lua 生态系统。

---

## 5. Kimi 办公

**原文标题**: Kimi Work

**原文链接**: [https://www.kimi.com/products/kimi-work](https://www.kimi.com/products/kimi-work)

**Kimi Work** 是一款基于内置 Cron 引擎的自动化解决方案，旨在实现全天候的高效生产力。它通过在后台自动执行重复性任务，实现了“一经设置，无需干预”的工作流程，确保任务在没有人工介入的情况下精准按时运行。

核心功能包括：定时调用大语言模型（LLM）智能体以完成每日简报撰写，以及运行 Python 脚本进行大规模数据处理。通过自主处理这些操作，Kimi Work 能够全天候保持工作流的持续高效。

---

## 6. Jelly UI: Soft-body physics for native HTML form controls

**原文标题**: Jelly UI: Soft-body physics for native HTML form controls

**原文链接**: [https://jelly-ui.com/](https://jelly-ui.com/)

**Jelly UI** is a dependency-free Web Components library designed to create soft, tactile, and interactive user interfaces using soft-body physics. It bridges the gap between functional native HTML form controls and playful, physics-based animations.

The library is lightweight and developer-friendly, requiring only a single script tag to implement. It offers over 40 custom elements that integrate seamlessly into standard HTML. Key technical and design features include:

*   **Accessibility:** Built-in WCAG AA color tokens to ensure high contrast and readability.
*   **Internationalization:** Native support for right-to-left (RTL) layouts.
*   **Visual Modes:** Automatic and manual support for dark mode.
*   **Performance:** Zero external dependencies, ensuring a small footprint and fast load times.

By combining tactile physics with essential modern UI features, Jelly UI provides a unique framework for building expressive yet accessible web applications.

---

## 7. 角落并非如此：关于屏幕空间环境光遮蔽 (2012)

**原文标题**: Corners Don't Look Like That: Regarding Screenspace Ambient Occlusion (2012)

**原文链接**: [https://nothings.org/gamedev/ssao/](https://nothings.org/gamedev/ssao/)

生成摘要时出错

---

## 8. 机场模拟器

**原文标题**: Airport Simulator

**原文链接**: [https://airport.apunen.com/](https://airport.apunen.com/)

由于提供的内容仅包含标题，以下是通常与“机场模拟器”（Airport Simulator）类软件及游戏相关的通用概念和核心功能概述：

**概览**
机场模拟器属于经营模拟类游戏，玩家需要负责商业航空枢纽的设计、建设和日常运营。其主要目标是在保持财务盈利和乘客满意度的同时，建立一个高效的交通网络。

**核心功能与机制**
*   **基础设施建设：** 玩家负责建造核心设施，包括跑道、滑行道、航站楼和控制塔。合理的战略布局对于缩短飞机滑行时间和防止地面拥堵至关重要。
*   **物流与运营：** 核心玩法涉及管理复杂的起降时刻表。这包括监管各项地面服务，如飞机加油、行李搬运、餐饮供应和机舱清洁，以确保快速的过站周转。
*   **乘客体验：** 游戏高度重视“客流”管理。玩家必须优化值机柜台、安检点和登机口，同时提供座椅、餐厅和商店等配套设施，以获取额外收入。
*   **员工与资源管理：** 成功运营需要招聘和培训多元化的员工团队，包括空中交通管制员、安检人员和保洁人员。在工资成本与运营需求之间取得平衡是一项持续的挑战。
*   **危机管理：** 模拟器通常会引入随机变量，如极端天气、技术故障或安全威胁，迫使玩家实时调整策略以避免延误或事故。

**结语**
机场模拟器让玩家能够全面了解航空管理的微观与宏观层面，挑战玩家在高压环境下平衡航空公司、乘客和员工等多方需求。

---

## 9. Firefox Merges Support for Vulkan Video Decoding

**原文标题**: Firefox Merges Support for Vulkan Video Decoding

**原文链接**: [https://github.com/search](https://github.com/search)

生成摘要时出错

---

## 10. Perfection Is Not Over-Engineering

**原文标题**: Perfection Is Not Over-Engineering

**原文链接**: [https://var0.xyz/posts/perfection-is-not-over-engineering.html](https://var0.xyz/posts/perfection-is-not-over-engineering.html)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 2 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 3 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 4 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 5 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 6 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 7 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 8 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 9 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 10 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 11 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 12 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 13 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 14 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 15 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 16 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 17 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 18 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 19 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 20 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 21 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 22 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 23 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 24 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 25 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 26 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 27 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 28 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 29 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 30 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 31 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 32 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 33 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 34 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 35 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 36 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 37 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 38 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 39 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 40 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 41 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 42 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 43 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 44 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 45 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 46 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 47 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 48 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 49 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 50 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 51 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 52 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 53 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 54 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 55 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 56 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 57 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 58 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 59 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 60 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 61 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 62 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 63 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 64 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 65 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 66 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 67 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 68 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 69 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 70 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 71 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 72 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 73 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 74 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 75 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 76 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 77 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 78 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 79 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 80 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 81 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 82 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 83 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 84 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 85 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 86 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 87 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 88 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 89 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 90 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 91 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 92 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 93 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 94 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 95 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 96 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 97 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 98 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 99 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 100 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 101 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 102 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 103 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 104 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 105 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 106 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 107 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 108 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 109 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 110 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 111 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 112 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 113 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 114 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 115 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 116 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 117 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 118 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 119 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 120 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 121 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 122 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 123 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 124 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 125 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 126 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 127 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 128 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 129 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 130 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 131 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 132 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 133 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 134 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 135 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 136 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 137 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 138 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 139 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 140 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 141 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 142 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 143 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 144 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 145 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 146 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 147 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 148 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 149 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 150 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 151 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 152 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 153 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 154 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 155 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 156 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 157 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 158 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 159 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 160 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 161 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 162 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 163 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 164 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 165 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 166 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 167 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 168 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 169 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 170 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 171 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 172 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 173 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 174 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 175 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 176 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 177 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 178 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 179 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 180 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 181 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 182 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 183 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 184 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 185 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 186 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 187 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 188 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 189 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 190 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 191 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 192 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 193 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 194 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 195 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 196 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 197 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 198 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 199 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 200 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 201 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 202 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 203 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 204 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 205 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 206 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 207 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 208 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 209 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 210 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 211 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 212 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 213 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 214 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 215 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 216 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 217 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 218 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 219 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 220 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 221 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 222 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 223 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 224 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 225 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 226 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 227 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 228 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 229 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 230 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 231 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 232 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 233 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 234 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 235 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 236 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 237 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 238 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 239 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 240 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 241 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 242 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 243 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 244 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 245 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 246 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 247 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 248 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 249 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 250 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 251 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 252 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 253 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 254 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 255 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 256 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 257 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 258 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 259 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 260 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 261 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 262 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 263 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 264 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 265 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 266 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 267 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 268 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 269 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 270 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 271 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 272 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 273 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 274 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 275 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 276 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 277 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 278 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 279 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 280 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 281 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 282 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 283 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 284 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 285 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 286 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 287 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 288 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 289 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 290 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 291 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 292 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 293 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 294 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 295 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 296 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 297 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 298 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 299 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 300 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 301 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 302 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 303 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 304 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 305 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 306 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 307 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 308 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 309 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 310 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 311 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 312 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 313 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 314 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 315 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 316 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 317 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 318 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 319 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 320 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 321 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 322 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 323 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 324 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 325 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 326 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 327 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 328 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 329 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 330 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 331 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 332 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 333 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 334 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 335 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 336 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 337 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 338 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 339 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 340 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 341 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 342 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 343 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 344 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 345 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 346 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 347 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 348 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 349 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 350 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 351 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 352 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 353 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 354 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 355 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 356 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 357 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 358 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 359 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 360 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 361 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 362 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 363 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 364 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 365 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 366 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 367 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 368 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 369 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 370 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 371 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 372 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 373 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 374 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 375 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 376 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 377 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 378 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 379 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 380 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 381 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 382 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 383 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 384 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 385 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 386 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 387 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 388 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 389 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 390 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 391 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 392 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 393 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 394 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 395 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 396 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 397 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 398 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 399 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 400 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 401 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 402 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 403 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 404 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 405 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 406 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 407 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 408 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 409 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 410 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 411 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 412 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 413 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 414 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 415 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 416 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 417 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 418 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 419 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 420 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 421 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 422 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 423 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 424 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 425 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 426 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 427 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 428 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 429 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 430 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 431 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 432 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 433 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 434 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 435 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 436 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 437 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 438 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 439 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 440 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 441 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 442 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 443 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 444 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 445 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 446 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 447 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 448 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 449 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 450 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 451 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 452 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 453 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 454 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 455 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 456 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 457 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 458 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 459 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 460 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 461 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 462 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 463 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 464 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 465 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 466 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 467 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 468 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 469 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 470 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 471 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 472 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 473 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 474 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 475 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 476 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 477 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 478 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 479 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 480 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 481 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 482 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 483 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 484 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 485 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 486 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 487 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
