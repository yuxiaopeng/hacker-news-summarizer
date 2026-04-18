# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-18.md)

*最后自动更新时间: 2026-04-18 18:06:05*
## 1. Opus 4.7 较 4.6 的膨胀率约为 45%

**原文标题**: Opus 4.7 to 4.6 Inflation is ~45%

**原文链接**: [https://tokens.billchambers.me/leaderboard](https://tokens.billchambers.me/leaderboard)

本文介绍了一个托管在 billchambers.me 上的 **代币经济学计算器 (Tokenomics Calculator)**，旨在比较 Anthropic 的 Opus 模型在 **4.6 和 4.7** 两个版本之间的代币成本及使用情况。

其核心结论是：从 4.6 版本过渡到 4.7 版本，代币成本出现了 **45% 的“膨胀”**。这意味着对于相同的输入提示词，新版本 (4.7) 会生成或消耗显著更多的代币，从而导致用户的运营支出大幅增加。

**该工具的主要特点：**
*   **社区驱动的数据：** 该计算器利用社区平均值和基于真实输入的匿名请求代币对比，展示了模型在实际应用中的差异。
*   **透明度：** 它允许用户提交自己的提示词以查看对比结果，旨在清晰展示模型迭代更新对计费的影响。
*   **独立且开源：** 该项目是开源的，并强调其不隶属于 Anthropic，也不受其认可或管理。

总之，该文根据众包性能数据向开发者和企业发出警告：与 4.6 版本相比，过渡到 Opus 4.7 可能会导致代币相关成本增加近 50%。

---

## 2. B-52轰炸机星敏感器内部的机电式角度计算机

**原文标题**: The electromechanical angle computer inside the B-52 bomber's star tracker

**原文链接**: [https://www.righto.com/2026/04/B-52-star-tracker-angle-computer.html](https://www.righto.com/2026/04/B-52-star-tracker-angle-computer.html)

在GPS问世之前，B-52轰炸机利用“星光罗盘”（Astro Compass）来实现高精度的航向和定位。这是一种研制于20世纪60年代的自动化天文导航系统，它将传统上缓慢且复杂的人工天文导航过程自动化，提供了一个可靠且抗干扰的导航源。

该系统的核心是“角度计算机”（Angle Computer），一台复杂的机电模拟计算机。由于当时数字计算机尚不适用于飞机，角度计算机通过对“天球”进行物理建模来执行复杂的三角函数计算。利用由齿轮、支臂和自整角机组成的精密机构，它通过解算“导航三角形”，将全球星历坐标转换为飞机的本地坐标系。

导航过程包含以下几个核心组件：
*   **星体跟踪仪（The Astro Tracker）：** 安装在机身上的增稳望远镜，利用光电倍增管锁定特定恒星。
*   **航空天文年历（The Air Almanac）：** 导航员用来查找特定时间所需天文数据（如恒星时角和赤纬）的参考资料。
*   **坐标转换（Coordinate Conversion）：** 导航员通过主控制面板将数据输入系统。随后，角度计算机根据飞机的纬度和地球自转（地方时角）对这些数值进行调整，以确定恒星的预期方位角（罗盘方向）和高度角（地平线以上的角度）。

通过机械模拟恒星相对于地球的运动，角度计算机提供了精度达十分之一度的航向。这一“机械奇迹”使B-52能够在不依赖地面基础设施的情况下实现全球远距离航行。

---

## 3. Migrating from DigitalOcean to Hetzner

**原文标题**: Migrating from DigitalOcean to Hetzner

**原文链接**: [https://isayeter.com/posts/digitalocean-to-hetzner-migration/](https://isayeter.com/posts/digitalocean-to-hetzner-migration/)

生成摘要时出错

---

## 4. Kdenlive 现状

**原文标题**: State of Kdenlive

**原文链接**: [https://kdenlive.org/news/2026/state-2026/](https://kdenlive.org/news/2026/state-2026/)

《Kdenlive 现状 - 2026》报告概述了这款开源视频编辑器在过去一年中取得的显著增长与技术磨砺。在整个 2025 年，该项目致力于平衡新功能与稳定性及性能，并发布了三个主要版本（25.04、25.08 和 25.12）。

**核心技术亮点：**
*   **AI 与性能：** 引入了用于背景移除的对象分割工具 (SAM2)，并将音频波形生成的性能提升了 300%。
*   **工作流改进：** 通过 C++ 重写 OpenTimelineIO 提升了跨应用兼容性，同时引入了全新的灵活停靠系统和重新设计的音频混音器，优化了用户界面。
*   **路线图：** 2026 年计划推出的功能包括监视器镜像、动画过渡预览，以及由 NGI Zero 资助的用于高级关键帧管理的“Dopesheet”。长期目标包括支持 10/12 位色彩和 OpenFX 集成。

**社区与影响力：**
该项目在全球范围内得到了广泛采用，2025 年下载量超过 1150 万次，其中美国、印度和巴西的使用量最高。开发团队规模虽小但十分活跃，由 8 名核心成员和 38 名代码贡献者组成。在阿姆斯特丹和柏林举行的技术冲刺活动促进了与 Blender 基金会的合作，并优化了软件架构。

**资金与未来：**
尽管 Kdenlive 在 2025 年收到了超过 9300 欧元的捐款（用于支持首席维护者和基础设施建设），但团队仍在呼吁加强社区支持。其目标是筹集足够资金聘请更多开发人员，以加速开发进程并进一步提升软件稳定性。此外，Kdenlive 进驻 Microsoft Store 的工作已接近尾声，这将进一步提升 Windows 用户的获取便捷性。

---

## 5. Fuzix 操作系统

**原文标题**: Fuzix OS

**原文链接**: [https://www.fuzix.org/](https://www.fuzix.org/)

Fuzix OS version 0.4 is a significant update to the multi-platform operating system, focusing on architectural refinements, streamlined building processes, and expanded hardware support. 

**Key Technical Changes**  
The kernel features a reworked modular networking layer designed for future memory-space isolation on 8-bit machines. Executable formats have been unified: 8080, 8085, and Z80 binaries are now compatible, as are 6803 and 68HC11 formats. 32-bit systems have transitioned to a stable *a.out* format. While toolchains remain complex, the build system now includes a "make diskimage" target to simplify creating bootable media.

**Naming and Branding**  
The release completes the rebranding of the N8VEM project to "Retrobrew." It also clarifies nomenclature by distinguishing between official "RC2014" products and the broader "RCbus" standard.

**Processor and System Support**  
Fuzix 0.4 supports an extensive array of processors, including:
*   **8-bit:** 6502 family, 6800/6809/68HC11, 8080, 8085 (now using the full instruction set), and the Z80/Z180 series.
*   **16/32-bit:** 68000 series, ARM (Raspberry Pi Pico and TM4C), ESP8266, and the new NS32K port.
*   **Experimental:** Early-stage support is included for RiscV 32, ESP32, Z280, and others.

**Hardware Platforms**  
The OS runs on a vast range of legacy and modern retro-hardware. Supported systems include classic home computers like the Amstrad NC100/200, Tandy COCO 2/3, MSX, and Sam Coupe, alongside modern SBCs such as the RC2014, Small Computer Central (SC) series, and various Retrobrew/N8VEM boards. Notably, the Pentagon and Scorpion systems have been dropped due to a lack of testers, and several ports like the P112 remain untested on actual hardware. 

Source code and install images are available on GitHub under the '0.4' tag.

---

## 6. 墨田水族馆发布2026版企鹅关系图，上演复杂纠葛与分手戏码。

**原文标题**: Sumida Aquarium Posts 2026 Penguin Relationship Chart, with Drama and Breakups

**原文链接**: [https://www.sumida-aquarium.com/special/sokanzu/en/2026/](https://www.sumida-aquarium.com/special/sokanzu/en/2026/)

无法访问文章链接。

---

## 7. UpCodes (YC S17) 招聘 SDR，助力提升建筑业生产力

**原文标题**: UpCodes (YC S17) Is Hiring SDRs to Help Make Construction More Productive

**原文链接**: [https://up.codes/careers?utm_source=HN](https://up.codes/careers?utm_source=HN)

UpCodes 是一家由 Y Combinator 支持的初创公司（2017 年夏季批次），目前正在招聘销售开发代表 (SDR)，以支持其提高建筑行业生产力和效率的使命。

该公司提供一个全面的、可搜索的建筑规范数据库，旨在帮助建筑师、工程师和承包商应对复杂的法规环境。通过将规范查询数字化和流程化，UpCodes 帮助行业专业人士避免代价高昂的项目延误和合规错误。

**核心亮点：**
*   **职位：** 销售开发代表 (SDR)。
*   **使命：** 通过提供“建筑规范界的谷歌”，推动规模达 1.3 万亿美元的建筑行业实现现代化。
*   **影响力：** SDR 将负责通过识别新业务机会，并向潜在客户介绍该平台如何自动化手动调研任务，从而推动公司增长。
*   **公司背景：** 作为 YC 校友企业，UpCodes 是一家处于建筑与法律技术 (ConTech) 交叉领域的高增长科技公司。

此次招聘计划反映了公司的扩张态势，其正致力于扩大运营规模，成为建筑法规和合规管理的首选资源。

---

## 8. Scientists discover "cleaner ants" that groom giant ants in Arizona desert

**原文标题**: Scientists discover "cleaner ants" that groom giant ants in Arizona desert

**原文链接**: [https://www.sciencedaily.com/releases/2026/04/260414075641.htm](https://www.sciencedaily.com/releases/2026/04/260414075641.htm)

生成摘要时出错

---

## 9. Show HN: MDV – 支持数据的文档、仪表盘和幻灯片的 Markdown 超集

**原文标题**: Show HN: MDV – a Markdown superset for docs, dashboards, and slides with data

**原文链接**: [https://github.com/drasimwagan/mdv](https://github.com/drasimwagan/mdv)

**MDV (Markdown Data & Visualization)** 是一种 Markdown 超集，专为创建数据驱动的文档、仪表板和幻灯片而设计。它在严格的 CommonMark 基础上增加了四项特定扩展：用于配置的 YAML 前置内容（front-matter）、用于可视化的围栏代码块、用于布局/样式的 “:::” 容器，以及自动生成的目录。

该项目的核心理念是简洁性与便携性。与其他需要复杂 CSS 选择器或嵌入式 JavaScript 的工具不同，MDV 使用命名样式和主题来处理呈现效果。其主要优势在于输出结果：它能渲染成**自包含的 HTML**，其中图表以行内 SVG 形式生成。这意味着生成的文档在查看时无需 JavaScript 运行时。它还支持直接导出为 PDF。

**核心特性包括：**
*   **数据集成：** 支持行内 CSV/JSON 或引用外部数据文件。
*   **可视化：** 通过简单的代码块轻松创建图表（柱状图、折线图等）和 KPI “数值卡”。
*   **布局工具：** 内置对分栏、呼出框（callouts）和样式化区域的支持。
*   **工具链：** 提供用于渲染和实时预览的 CLI 工具，以及用于双栏实时编辑的 VS Code 扩展。

MDV 目前处于预发布状态（v1），运行环境要求为 Node.js 20 或更高版本。它被定位为一种精简的替代方案，适用于需要在叙述性文本中结合可视化数据分析，且不希望承担传统仪表板软件或复杂 Web 开发框架开销的专业人士。

---

## 10. Michael Rabin has died

**原文标题**: Michael Rabin has died

**原文链接**: [https://en.wikipedia.org/wiki/Michael_O._Rabin](https://en.wikipedia.org/wiki/Michael_O._Rabin)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 2 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 3 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 4 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 5 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 6 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 7 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 8 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 9 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 10 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 11 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 12 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 13 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 14 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 15 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 16 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 17 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 18 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 19 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 20 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 21 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 22 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 23 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 24 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 25 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 26 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 27 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 28 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 29 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 30 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 31 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 32 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 33 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 34 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 35 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 36 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 37 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 38 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 39 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 40 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 41 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 42 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 43 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 44 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 45 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 46 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 47 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 48 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 49 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 50 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 51 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 52 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 53 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 54 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 55 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 56 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 57 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 58 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 59 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 60 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 61 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 62 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 63 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 64 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 65 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 66 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 67 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 68 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 69 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 70 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 71 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 72 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 73 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 74 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 75 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 76 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 77 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 78 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 79 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 80 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 81 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 82 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 83 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 84 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 85 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 86 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 87 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 88 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 89 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 90 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 91 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 92 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 93 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 94 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 95 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 96 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 97 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 98 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 99 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 100 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 101 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 102 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 103 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 104 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 105 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 106 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 107 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 108 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 109 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 110 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 111 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 112 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 113 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 114 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 115 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 116 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 117 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 118 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 119 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 120 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 121 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 122 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 123 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 124 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 125 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 126 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 127 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 128 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 129 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 130 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 131 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 132 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 133 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 134 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 135 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 136 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 137 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 138 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 139 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 140 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 141 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 142 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 143 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 144 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 145 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 146 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 147 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 148 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 149 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 150 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 151 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 152 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 153 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 154 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 155 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 156 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 157 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 158 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 159 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 160 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 161 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 162 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 163 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 164 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 165 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 166 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 167 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 168 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 169 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 170 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 171 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 172 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 173 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 174 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 175 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 176 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 177 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 178 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 179 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 180 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 181 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 182 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 183 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 184 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 185 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 186 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 187 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 188 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 189 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 190 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 191 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 192 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 193 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 194 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 195 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 196 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 197 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 198 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 199 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 200 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 201 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 202 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 203 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 204 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 205 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 206 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 207 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 208 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 209 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 210 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 211 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 212 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 213 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 214 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 215 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 216 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 217 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 218 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 219 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 220 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 221 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 222 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 223 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 224 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 225 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 226 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 227 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 228 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 229 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 230 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 231 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 232 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 233 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 234 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 235 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 236 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 237 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 238 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 239 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 240 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 241 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 242 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 243 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 244 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 245 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 246 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 247 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 248 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 249 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 250 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 251 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 252 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 253 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 254 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 255 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 256 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 257 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 258 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 259 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 260 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 261 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 262 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 263 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 264 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 265 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 266 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 267 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 268 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 269 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 270 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 271 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 272 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 273 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 274 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 275 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 276 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 277 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 278 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 279 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 280 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 281 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 282 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 283 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 284 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 285 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 286 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 287 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 288 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 289 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 290 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 291 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 292 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 293 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 294 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 295 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 296 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 297 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 298 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 299 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 300 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 301 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 302 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 303 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 304 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 305 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 306 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 307 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 308 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 309 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 310 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 311 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 312 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 313 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 314 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 315 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 316 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 317 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 318 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 319 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 320 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 321 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 322 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 323 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 324 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 325 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 326 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 327 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 328 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 329 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 330 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 331 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 332 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 333 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 334 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 335 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 336 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 337 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 338 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 339 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 340 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 341 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 342 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 343 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 344 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 345 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 346 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 347 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 348 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 349 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 350 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 351 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 352 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 353 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 354 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 355 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 356 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 357 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 358 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 359 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 360 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 361 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 362 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 363 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 364 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 365 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 366 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 367 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 368 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 369 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 370 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 371 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 372 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 373 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 374 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 375 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 376 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 377 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 378 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 379 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 380 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 381 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 382 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 383 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 384 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 385 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 386 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 387 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 388 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 389 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 390 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 391 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 392 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 393 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 394 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
