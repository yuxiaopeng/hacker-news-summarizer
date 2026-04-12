# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-12.md)

*最后自动更新时间: 2026-04-12 18:07:10*
## 1. 回归惯用设计

**原文标题**: Bring Back Idiomatic Design

**原文链接**: [https://essays.johnloeber.com/p/4-bring-back-idiomatic-design](https://essays.johnloeber.com/p/4-bring-back-idiomatic-design)

在《回归惯用设计》（Bring Back Idiomatic Design）一文中，John Loeber 主张回归标准化、具有“惯用性”的用户界面——即那些如复选框一般普及，以至于用户无需思考即可交互的设计模式。

Loeber 将当前碎片化的网页设计现状与桌面软件时代（Windows 95–7）进行了对比。在桌面时代，操作系统的约束强制执行**同质化界面**。标准化的菜单（文件、编辑、查看）、带有下划线的键盘快捷键以及统一的状态栏，让用户能够在不同应用程序间保持“高效的工作流”。

相比之下，现代浏览器时代被**异质化界面**所定义。即便是 Figma 和 Linear 这样的高质量应用，它们之间也极少共享设计惯例，迫使用户在寻找基础功能时不得不反复“摸索”。Loeber 将这种一致性的缺失归因于两个因素：
1. **向移动端的转型：** 设计师经常将触屏优先的模式（如汉堡菜单）套用到桌面环境，造成了尴尬的混合体验。
2. **技术变迁：** 现代框架和 WebAssembly 允许开发者绕过标准的 HTML/CSS，这破坏了诸如“后退”按钮或原生链接行为等浏览器层面的惯用模式。

Loeber 将苹果和 Substack 视为当代的成功案例，它们通过坚持且一致的设计系统，营造出一种“自然易用”的效果。最后，他为产品开发者提供了一份旨在恢复可用性的指南：
* **坚持使用基础 HTML/CSS：** 使用 `<button>` 和 `<a>` 标签等原生元素，而非通过 JavaScript 重新实现。
* **尊重浏览器惯例：** 确保后退按钮、CTRL+点击以及 URL 分享功能符合预期。
* **清晰度重于美观：** 使用文字而非模棱两可的图标，并确保按钮在视觉上清晰可见。

归根结底，Loeber 认为尽管 Web 仍处于快速创新后的“冷却期”，但开发者应当优先考虑直观、可预测的界面，而非那些独特却令人困惑的设计。

---

## 2. 我为纽约的每一列火车都配了一件乐器。

**原文标题**: I gave every train in New York an instrument

**原文链接**: [https://www.trainjazz.com/](https://www.trainjazz.com/)

“我给纽约的每辆列车都配了一件乐器”描述了一个生成式音乐项目，它将纽约市地铁的实时数据转化为一场持续不断的爵士乐表演。通过将约800辆运行中的列车映射到一个爵士乐队——包括走步贝斯、钢琴、萨克斯、颤音琴和鼓刷——这一体验揭示了轨道交通系统中“噪音里的音乐”。

乐曲的构思受城市物理运动的支配：
*   **映射：** 列车在运行线路上的具体位置决定了它所演奏的音符。
*   **时间动态：** 音乐反映了城市的脉搏。高峰时段会产生带有长音的密集音墙，而到了凌晨三点，乐曲则变得稀疏，留白也更长。
*   **独特性：** 由于800辆列车的运动轨迹从未完全相同，音乐也是瞬息万变、不断演化且永不重复的。

该体验还包含一个互动元素，用户可以分享自己的位置。这会使音频发生偏移，让距离用户最近的列车声音变得更大，从而为用户所在地创造出一份个性化的“声音肖像”。最终，该项目将城市的工业喧嚣重新构想为一场由城市景观本身演奏的、跨越世纪的生命交响乐。

---

## 3. Show HN：Oberon System 3 原生运行于树莓派 3（提供现成的 SD 卡镜像）

**原文标题**: Show HN: Oberon System 3 runs natively on Raspberry Pi 3 (with ready SD card)

**原文链接**: [https://github.com/rochus-keller/OberonSystem3Native/releases](https://github.com/rochus-keller/OberonSystem3Native/releases)

Rochus Keller 发布了适用于 Raspberry Pi 3b 的 Oberon System 3 原生移植版，该版本同时支持 Raspberry Pi 2b (v1.2+) 和 Pi Zero 2。这一里程碑标志着该系统已从早期的 i386 和 ARMv7 QEMU 版本正式转向功能完备的裸机硬件运行。

**核心技术细节：**
该移植版包含了 Oberon 系统的完整内外核心，涵盖内核 (Kernel)、实数处理 (Reals) 和文件系统 (AosFs)。它集成了针对特定平台的显示、USB 和数学驱动程序。该项目的一个显著亮点是其构建效率：利用自定义的基于 C99 的工具链，在现代 Linux 机器上从零开始构建整个系统（包括模块编译和驱动生成）仅需不到一分钟。

**资源与获取：**
为了方便用户试用，开发者提供了：
*   可直接烧录的 SD 卡镜像 (`oberon-rpi3.img`)。
*   预编译的 Linux x64 工具链及构建脚本。
*   使用 `dd` 或标准镜像工具进行烧录的操作说明。

**硬件选择与未来计划：**
Keller 选择这些特定的树莓派型号是因为其架构相似且能保证长期供应（Pi 3b 和 Zero 2 的生产预计将分别持续至 2028 年和 2030 年）。作者指出，该系统运行稳定，可配合原装树莓派显示器以及 Oberon 传统的三键鼠标和键盘组合使用。未来的开发目标包括将系统迁移至 Raspberry Pi 4，并实现以太网等网络驱动程序。

---

## 4. 目前已有七个国家实现100%可再生能源发电。

**原文标题**: Seven countries now generate 100% of their electricity from renewable energy

**原文链接**: [https://www.the-independent.com/tech/renewable-energy-solar-nepal-bhutan-iceland-b2533699.html](https://www.the-independent.com/tech/renewable-energy-solar-nepal-bhutan-iceland-b2533699.html)

根据国际能源署（IEA）和国际可再生能源署（IRENA）的数据，目前已有七个国家超过 99.7% 的电力来自可再生能源。这些国家——阿尔巴尼亚、不丹、尼泊尔、巴拉圭、冰岛、埃塞俄比亚和刚果民主共和国——主要依赖地热、水力、太阳能和风能。

报告强调了更广泛的全球转型趋势，指出另有 40 个国家目前至少 50% 的电力来自可再生能源。其中值得关注的包括：英国在 2022 年达到了 41.5%；苏格兰同年的可再生能源发电量则相当于其电力消耗总量的 113%。

斯坦福大学教授马克·雅各布森（Mark Jacobson）认为，绿色转型并不需要所谓的“奇迹技术”。相反，他主张通过风能、水能和太阳能（WWS）技术实现“全面电气化”。

尽管风能在许多地区目前发挥着重要作用，但埃克塞特大学和伦敦大学学院的研究人员预测，太阳能将很快主导全球市场。他们认为，由于商业成本下降以及高效钙钛矿太阳能电池等技术进步，太阳能已达到“不可逆转的临界点”。这些研究人员得出结论，向清洁能源的转型已势不可挡，预计到 2050 年，太阳能将成为全球主要的能源来源。

---

## 5. JVM 参数探索器

**原文标题**: JVM Options Explorer

**原文链接**: [https://chriswhocodes.com/vm-options-explorer.html](https://chriswhocodes.com/vm-options-explorer.html)

**JVM Options Explorer** 是由 Chris Newland 创建的一个全面的 Web 工具，旨在帮助 Java 开发人员和系统管理员在庞大且通常缺乏文档说明的 Java 虚拟机（JVM）命令行参数中查找所需信息。

该网站作为一个交互式、可搜索的数据库，涵盖了各种 OpenJDK 发行版以及 GraalVM 和 OpenJ9 等替代虚拟机的数千个选项。用户可以根据特定的 Java 版本（从旧版本到最新的早期访问构建）、操作系统和 CPU 架构来筛选这些选项。

该工具的主要功能包括：

*   **详细的元数据：** 对于每一个参数，该工具都提供了数据类型（如 bool、int、ccstr）、类别（如实验性 Experimental、诊断性 Diagnostic 或可管理性 Manageable）以及其默认值。
*   **版本对比：** 强大的对比功能允许用户查看不同 JVM 版本之间确切增加了、删除了或修改了哪些参数。这对于排查迁移问题或识别已弃用的选项特别有用。
*   **搜索与发现：** 界面支持快速筛选，使用户更容易找到标准文档中通常未列出的性能调优参数或调试工具。

其数据是通过程序化解析 HotSpot JVM 的 C++ 源代码生成的。通过直接从源码中提取信息，该工具提供了比往往滞后于代码更改的手动文档更准确、更及时的参考。总之，对于任何想要优化 Java 应用程序性能或了解 JVM 内部配置的人来说，它都是一个不可或缺的资源。

---

## 6. EasyPost (YC S13) 正在招聘

**原文标题**: EasyPost (YC S13) Is Hiring

**原文链接**: [https://www.easypost.com/careers](https://www.easypost.com/careers)

EasyPost 是一家由 Y Combinator 支持（S13 届）的初创公司，目前正在招聘。公司专注于高性能运输物流，旨在通过创新技术推动行业现代化。

公司营造了协作的工作环境，鼓励各部门的“问题解决者”共同应对挑战并探索新方案。其企业文化强调问责制、透明度和持续改进。欢迎感兴趣的候选人查看其多样化的职位空缺，共同助力全球运输流程的简化。

---

## 7. 六小时内的永恒：智慧生命的星系际扩张 (2013)

**原文标题**: Eternity in six hours: Intergalactic spreading of intelligent life (2013)

**原文链接**: [https://www.researchgate.net/publication/256935390_Eternity_in_six_hours_Intergalactic_spreading_of_intelligent_life_and_sharpening_the_Fermi_paradox](https://www.researchgate.net/publication/256935390_Eternity_in_six_hours_Intergalactic_spreading_of_intelligent_life_and_sharpening_the_Fermi_paradox)

In "Eternity in Six Hours: Intergalactic Spreading of Intelligent Life," Stuart Armstrong and Anders Sandberg argue that intergalactic colonization is not only possible but surprisingly feasible using known physics and extrapolated technology.

The authors outline a colonization "pipeline" consisting of three main components:
1.  **Energy Harvesting:** Building Dyson swarms around the home star to capture massive amounts of energy.
2.  **Resource Acquisition:** Dismantling "dead" planets (like Mercury) to provide materials for spacecraft.
3.  **Self-Replicating Probes:** Launching von Neumann probes at relativistic speeds ($0.1c$ to $0.5c$).

By combining these methods, a civilization could initiate a wave of expansion that grows exponentially. The authors calculate that even with conservative estimates, a civilization could reach and colonize the entire reachable universe (including the Virgo Supercluster) within a few billion years—a timeframe much shorter than the age of the universe. The title "Eternity in Six Hours" refers to the hypothetical timeframe in which a sufficiently advanced Dyson swarm could provide the energy required to launch the entire colonization project.

The paper’s primary purpose is to "sharpen" the Fermi Paradox. If intergalactic travel is technically achievable and requires no "miracle" physics, the absence of any visible alien engineering (such as altered star spectra or occupied galaxies) becomes much more difficult to explain. 

The authors conclude that social explanations—such as the idea that all civilizations choose to remain "green" or stay home—are statistically unlikely, as it would only take one expansionist culture to fill the universe. Therefore, the "Great Silence" suggests that either the birth of intelligent life is an incredibly rare event or that there is a significant "Great Filter" in our future that prevents civilizations from reaching this stage of development.

---

## 8. Happy Map

**原文标题**: Happy Map

**原文链接**: [https://pudding.cool/2026/02/happy-map/](https://pudding.cool/2026/02/happy-map/)

生成摘要时出错

---

## 9. Phyphox – Physical Experiments Using a Smartphone

**原文标题**: Phyphox – Physical Experiments Using a Smartphone

**原文链接**: [https://phyphox.org/](https://phyphox.org/)

生成摘要时出错

---

## 10. Building a SaaS in 2026 Using Only EU Infrastructure

**原文标题**: Building a SaaS in 2026 Using Only EU Infrastructure

**原文链接**: [https://eualternative.eu/guides/building-saas-eu-stack/](https://eualternative.eu/guides/building-saas-eu-stack/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 2 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 3 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 4 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 5 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 6 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 7 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 8 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 9 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 10 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 11 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 12 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 13 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 14 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 15 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 16 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 17 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 18 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 19 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 20 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 21 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 22 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 23 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 24 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 25 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 26 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 27 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 28 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 29 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 30 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 31 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 32 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 33 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 34 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 35 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 36 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 37 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 38 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 39 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 40 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 41 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 42 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 43 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 44 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 45 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 46 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 47 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 48 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 49 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 50 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 51 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 52 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 53 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 54 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 55 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 56 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 57 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 58 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 59 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 60 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 61 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 62 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 63 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 64 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 65 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 66 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 67 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 68 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 69 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 70 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 71 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 72 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 73 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 74 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 75 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 76 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 77 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 78 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 79 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 80 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 81 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 82 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 83 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 84 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 85 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 86 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 87 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 88 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 89 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 90 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 91 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 92 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 93 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 94 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 95 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 96 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 97 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 98 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 99 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 100 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 101 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 102 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 103 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 104 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 105 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 106 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 107 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 108 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 109 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 110 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 111 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 112 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 113 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 114 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 115 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 116 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 117 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 118 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 119 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 120 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 121 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 122 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 123 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 124 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 125 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 126 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 127 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 128 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 129 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 130 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 131 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 132 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 133 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 134 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 135 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 136 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 137 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 138 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 139 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 140 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 141 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 142 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 143 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 144 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 145 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 146 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 147 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 148 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 149 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 150 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 151 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 152 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 153 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 154 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 155 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 156 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 157 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 158 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 159 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 160 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 161 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 162 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 163 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 164 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 165 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 166 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 167 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 168 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 169 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 170 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 171 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 172 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 173 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 174 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 175 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 176 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 177 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 178 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 179 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 180 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 181 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 182 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 183 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 184 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 185 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 186 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 187 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 188 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 189 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 190 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 191 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 192 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 193 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 194 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 195 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 196 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 197 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 198 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 199 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 200 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 201 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 202 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 203 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 204 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 205 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 206 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 207 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 208 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 209 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 210 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 211 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 212 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 213 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 214 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 215 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 216 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 217 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 218 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 219 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 220 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 221 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 222 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 223 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 224 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 225 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 226 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 227 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 228 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 229 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 230 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 231 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 232 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 233 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 234 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 235 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 236 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 237 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 238 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 239 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 240 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 241 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 242 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 243 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 244 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 245 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 246 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 247 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 248 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 249 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 250 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 251 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 252 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 253 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 254 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 255 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 256 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 257 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 258 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 259 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 260 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 261 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 262 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 263 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 264 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 265 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 266 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 267 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 268 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 269 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 270 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 271 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 272 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 273 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 274 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 275 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 276 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 277 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 278 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 279 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 280 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 281 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 282 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 283 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 284 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 285 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 286 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 287 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 288 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 289 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 290 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 291 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 292 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 293 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 294 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 295 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 296 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 297 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 298 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 299 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 300 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 301 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 302 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 303 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 304 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 305 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 306 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 307 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 308 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 309 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 310 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 311 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 312 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 313 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 314 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 315 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 316 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 317 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 318 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 319 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 320 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 321 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 322 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 323 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 324 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 325 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 326 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 327 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 328 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 329 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 330 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 331 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 332 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 333 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 334 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 335 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 336 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 337 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 338 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 339 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 340 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 341 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 342 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 343 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 344 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 345 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 346 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 347 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 348 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 349 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 350 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 351 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 352 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 353 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 354 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 355 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 356 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 357 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 358 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 359 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 360 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 361 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 362 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 363 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 364 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 365 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 366 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 367 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 368 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 369 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 370 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 371 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 372 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 373 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 374 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 375 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 376 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 377 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 378 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 379 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 380 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 381 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 382 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 383 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 384 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 385 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 386 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 387 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 388 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
