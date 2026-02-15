# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-02-15.md)

*最后自动更新时间: 2026-02-15 18:11:11*
## 1. 我修复了 Windows 原生开发

**原文标题**: I Fixed Windows Native Development

**原文链接**: [https://marler8997.github.io/blog/fixed-windows/](https://marler8997.github.io/blog/fixed-windows/)

《我修复了 Windows 原生开发》一文探讨了使用 Visual Studio Installer 进行 C++ 开发时常见的挫败感。作者指出，“安装 Visual Studio” 并不是管理依赖的好方法，因为该 IDE 是一个数 GB 的庞然大物，将编辑器与编译器、SDK 强行捆绑在一起。这导致了长达数小时的安装过程、注册表膨胀、难以复现的“在我机器上能跑”类 Bug，以及使用 `vcvarsall.bat` 时脆弱的环境配置。

为解决这一问题，作者开发了 **msvcup**。这是一个开源的命令行工具，它将 MSVC 工具链视为现代、版本化且隔离的依赖项。

**核心功能与优势：**
*   **定向安装：** 通过解析微软官方的 JSON 清单，`msvcup` 直接从微软 CDN 仅下载必要的组件（编译器、链接器和 SDK）。
*   **隔离与便携性：** 工具安装在版本化的目录中（例如 `C:\msvcup\`），避免了注册表污染，并允许不同版本共存。
*   **声明式构建：** 支持锁定文件，确保所有开发者和 CI 系统使用完全一致的工具链版本，实现可复现的构建。
*   **自动环境管理：** `autoenv` 功能可创建包装执行文件，自动设置所需的环境变量，无需修改全局环境变量或手动执行批处理脚本。
*   **高效快捷：** 几分钟内即可完成完整构建环境的搭建，而后续检查仅需几毫秒。

作者通过简单的脚本展示了该工具在构建 Raylib、LLVM 和 WebRTC（在 Tuple 公司）等复杂项目中的效用。虽然 `msvcup` 并非为了取代那些需要图形界面的 Visual Studio IDE 用户，但它为 Windows 原生构建流程提供了一个轻量、可脚本化且可靠的替代方案。

---

## 2. LT6502：基于6502的自制笔记本电脑

**原文标题**: LT6502: A 6502-based homebrew laptop

**原文链接**: [https://github.com/TechPaula/LT6502](https://github.com/TechPaula/LT6502)

**LT6502**是一款基于65C02处理器构建的自制笔记本电脑项目，旨在作为作者此前“塔式”6502计算机的便携式替代方案。该系统运行频率为8MHz，配备46K RAM和12K ROM，内置**EhBASIC**和**eWoz**监控程序。

**硬件规格：**
*   **核心：** 65C02 CPU，配备用于I/O和定时器的65C22 VIA。
*   **显示：** 9英寸屏幕（采用RA8875控制器），支持内置字体和图形显示。
*   **存储与电源：** 采用CF卡存储文件，配备10,000mAh电池并支持USB-C充电。
*   **连接性：** 内置键盘（通过MEGA644P控制）、串口控制台及一个内部扩展槽。

**架构与软件：**
内存映射分配为：0x0000–0xBEAF用于RAM，0xBE00–0xBFFF用于外设（包括显示器、CF卡和蜂鸣器），0xC000–0xFFFF用于ROM。为了充分利用硬件性能，开发者增加了以下自定义EhBASIC命令：
*   **图形：** CLS（清屏）、CIRCLE（圆）、LINE（线）、PLOT（描点）、SQUARE（方块）和ELIPSE（椭圆）。
*   **系统与存储：** 用于CF卡管理的DIR、LOAD和SAVE，以及WOZMON跳转命令。
*   **硬件控制：** 用于发声的BEEP和用于切换文本/图形模式的MODE。

**开发状态：**
项目进展迅速，从2025年底的初步PCB设计到2026年2月已完成整机组装并实现功能运行。近期更新包括成功的电池供电运行及集成的键盘固件。后续工作将侧重于优化键盘扫描代码，并可能升级至10.1英寸1024x600分辨率的显示屏。

---

## 3. 欧盟禁止销毁未售出的服装、配饰及鞋类。

**原文标题**: EU bans the destruction of unsold apparel, clothing, accessories and footwear

**原文链接**: [https://environment.ec.europa.eu/news/new-eu-rules-stop-destruction-unsold-clothes-and-shoes-2026-02-09_en](https://environment.ec.europa.eu/news/new-eu-rules-stop-destruction-unsold-clothes-and-shoes-2026-02-09_en)

欧盟委员会根据《可持续产品生态设计法规》（ESPR）采取了新措施，禁止销毁未售出的服装、服饰配件和鞋类。该倡议旨在减少环境破坏并促进循环经济，以应对欧洲目前 4% 至 9% 的未售出纺织品在投入使用前即被销毁的现状——这种做法产生的二氧化碳排放量相当于瑞典全国的净排放总量。

新规的核心内容包括：

*   **禁止销毁**：大型企业必须在 2026 年 7 月 19 日前停止销毁未售出的服装和鞋类。中型企业的过渡期则截止至 2030 年。
*   **强制披露**：企业必须公开其丢弃的未售出商品数量。大型企业自 2027 年 2 月起需按标准化格式进行此类报告。
*   **豁免条款**：针对特定情况允许有限的例外，例如产品受损或存在安全风险。
*   **循环替代方案**：委员会鼓励企业摒弃废弃处理，转而采取库存管理、转售、再制造和捐赠等方式。

通过提高产品的耐用性、可重复使用性和可回收性，ESPR 旨在消除由过度生产和在线退货驱动的浪费行为。这些措施旨在为可持续企业创造公平的竞争环境，同时显著减少纺织行业的环境足迹。欧盟委员杰西卡·罗斯沃尔（Jessika Roswall）强调，这些举措将赋能行业向可持续实践转型，同时提升竞争力和减少资源依赖。

---

## 4. 世嘉历代游戏机设计者佐藤秀树逝世

**原文标题**: Hideki Sato, designer of all Sega's consoles, has died

**原文链接**: [https://www.videogameschronicle.com/news/hideki-sato-designer-of-segas-consoles-dies-age-75/](https://www.videogameschronicle.com/news/hideki-sato-designer-of-segas-consoles-dies-age-75/)

世嘉（Sega）几乎所有游戏机背后的传奇硬件设计师、前社长佐藤秀树（Hideki Sato）逝世，享年77岁。

佐藤于1971年加入世嘉，并在公司度过了近四十载时光，在2008年离职前，曾于2001年至2003年出任社长。作为研发团队的领军人物，他在世嘉最负盛名的家用机及街机硬件开发中起到了至关重要的作用，其中包括SC-3000、Master System、Genesis/Mega Drive、Saturn以及Dreamcast。

他的设计理念深深植根于世嘉的街机传承。佐藤极力主张将尖端的街机技术引入家用市场，这一策略促成了成功的16位游戏机Mega Drive的诞生。在后来的访谈中，佐藤曾反思Dreamcast对“游戏与交流”的重视，其标志性设计包括内置调制解调器和可联动的VMU存储卡。他还坦诚地回忆了20世纪90年代的“位数战争”，提到世嘉当年如何为了满足消费者对强悍规格的需求，将Dreamcast作为128位系统进行营销，尽管该硬件本身采用的是更为复杂的架构。

佐藤逝世的消息由日本媒体《Beep21》报道，该媒体近期对他进行了一系列深度专访，回顾了他在游戏史上所发挥的关键作用。将街机的创新精神转化为家用机体验的能力，是他留给世人的宝贵遗产。

---

## 5. 我非常喜欢 ArchWiki 维护者的工作。

**原文标题**: I love the work of the ArchWiki maintainers

**原文链接**: [https://k7r.eu/i-love-the-work-of-the-archwiki-maintainers/](https://k7r.eu/i-love-the-work-of-the-archwiki-maintainers/)

为了庆祝“我爱自由软件日”，作者向 ArchWiki 的维护者们表达了深切的谢意，并强调文档贡献者所获得的认可往往太少。

作者提到近期在 FOSDEM 2026 与 Arch 项目负责人 Levente 及 ArchWiki 维护者 Ferdinand 的会面，并将 ArchWiki 誉为“互联网的瑰宝”。该网站被称赞为一项至关重要的资源，不仅服务于 Arch Linux 用户，也造福于所有自由软件使用者。它提供了清晰的配置技巧，以及对邮件程序、编辑器和窗口管理器等工具的深度解析，而这些内容在官方软件手册中往往难以寻觅。

文章引用了爱德华·斯诺登的话，以凸显在搜索引擎质量下滑的时代，该 Wiki 的可靠性。作者在结尾向维护这一重要社会资源的贡献者们致谢，并鼓励读者表达自己的感激之情，通过捐赠来支持 Arch 项目。

---

## 6. 一名奴隶园丁将碧根果转化为了经济作物

**原文标题**: An Enslaved Gardener Transformed the Pecan into a Cash Crop

**原文链接**: [https://lithub.com/how-an-enslaved-gardener-transformed-the-pecan-into-a-cash-crop/](https://lithub.com/how-an-enslaved-gardener-transformed-the-pecan-into-a-cash-crop/)

在《当树木作证》（*When Trees Testify*）的这段摘录中，生物学家贝隆达·L·蒙哥马利（Beronda L. Montgomery）强调了黑人和原住民对美国生物学做出的、长期被忽视的贡献，并重点介绍了一位名叫安托万（Antoine）的被奴役园丁。

尽管美洲原住民利用山核桃已有数百年历史——将其用于营养补给、医药和神圣仪式——但这种坚果长期以来难以实现商业化。早期建立果园的尝试均以失败告终，因为由种子长成的树木成熟缓慢，且产出的坚果质量参差不齐。这种不稳定性使得大规模生产在19世纪中叶安托万取得突破之前一直无法实现。

安托万通过“并接”（即嫁接）实现了一项里程碑式的农业壮举。通过成功地将接穗（嫩枝）与砧木结合，他培育出了“百年”（Centennial）品种，这种品种能产出规格统一且高品质的坚果。蒙哥马利强调了这一过程的技术难度，指出安托万在没有现代科学家所拥有的无菌环境或先进工具的情况下取得了成功。他的创新使山核桃转变为一种可复制的经济作物，为如今每年产值达数亿美元的产业奠定了基础。

尽管影响深远，安托万的遗产却几近湮灭；他最初栽种的树木最终为了改种甘蔗而被砍伐，而他的专业造诣在历史记录中也鲜被承认。蒙哥马利批判了科学文献和历史研究中一种普遍的倾向，即淡化被奴役者和原住民的主观能动性。她指出，即使是像珍·古道尔（Jane Goodall）这样德高望重的人物，在历史上也将被奴役者仅仅视为“劳工”，而非植物学专家。通过聚焦安托万的成就以及她自己家族传承的植物知识，蒙哥马利旨在重申黑人植物学专长的历史，并认可那些被剥夺名誉的人所做出的卓越科学贡献。

---

## 7. Flashpoint Archive – Over 200k web games and animations preserved

**原文标题**: Flashpoint Archive – Over 200k web games and animations preserved

**原文链接**: [https://flashpointarchive.org](https://flashpointarchive.org)

**Flashpoint Archive** is a community-driven, non-profit project dedicated to preserving web-based games and animations that are at risk of disappearing as internet technologies evolve and become obsolete. Since its inception in December 2017 by BlueMaxima, the project has expanded into a global collaborative effort, successfully archiving over **200,000 items** across hundreds of different browser plugins and web standards.

The project provides an open-source software suite designed to make these archived materials functional and accessible. This includes:
*   **A feature-rich launcher** for browsing the collection.
*   **A proxy server** that tricks legacy content into believing it is still running on the original live internet.
*   **A secure sandbox system** for safely running outdated plugins.

Flashpoint’s mission is to safeguard the history and culture of the web. As a non-profit organization, it relies on international contributors and community donations to maintain its operations. Users are encouraged to explore the collection, request new content for preservation, and support the project via their Open Collective page.

---

## 8. Reversed engineered game Starflight (1986)

**原文标题**: Reversed engineered game Starflight (1986)

**原文链接**: [https://github.com/s-macke/starflight-reverse](https://github.com/s-macke/starflight-reverse)

生成摘要时出错

---

## 9. Gwtar: A static efficient single-file HTML format

**原文标题**: Gwtar: A static efficient single-file HTML format

**原文链接**: [https://gwern.net/gwtar](https://gwern.net/gwtar)

生成摘要时出错

---

## 10. Oat – Ultra-lightweight, semantic, zero-dependency HTML UI component library

**原文标题**: Oat – Ultra-lightweight, semantic, zero-dependency HTML UI component library

**原文链接**: [https://oat.ink/](https://oat.ink/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 2 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 3 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 4 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 5 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 6 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 7 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 8 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 9 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 10 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 11 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 12 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 13 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 14 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 15 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 16 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 17 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 18 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 19 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 20 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 21 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 22 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 23 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 24 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 25 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 26 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 27 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 28 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 29 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 30 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 31 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 32 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 33 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 34 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 35 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 36 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 37 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 38 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 39 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 40 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 41 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 42 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 43 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 44 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 45 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 46 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 47 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 48 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 49 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 50 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 51 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 52 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 53 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 54 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 55 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 56 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 57 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 58 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 59 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 60 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 61 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 62 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 63 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 64 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 65 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 66 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 67 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 68 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 69 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 70 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 71 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 72 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 73 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 74 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 75 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 76 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 77 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 78 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 79 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 80 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 81 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 82 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 83 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 84 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 85 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 86 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 87 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 88 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 89 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 90 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 91 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 92 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 93 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 94 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 95 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 96 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 97 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 98 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 99 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 100 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 101 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 102 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 103 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 104 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 105 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 106 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 107 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 108 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 109 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 110 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 111 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 112 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 113 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 114 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 115 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 116 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 117 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 118 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 119 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 120 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 121 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 122 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 123 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 124 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 125 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 126 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 127 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 128 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 129 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 130 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 131 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 132 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 133 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 134 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 135 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 136 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 137 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 138 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 139 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 140 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 141 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 142 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 143 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 144 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 145 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 146 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 147 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 148 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 149 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 150 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 151 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 152 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 153 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 154 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 155 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 156 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 157 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 158 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 159 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 160 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 161 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 162 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 163 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 164 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 165 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 166 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 167 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 168 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 169 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 170 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 171 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 172 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 173 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 174 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 175 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 176 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 177 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 178 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 179 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 180 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 181 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 182 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 183 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 184 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 185 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 186 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 187 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 188 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 189 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 190 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 191 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 192 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 193 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 194 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 195 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 196 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 197 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 198 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 199 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 200 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 201 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 202 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 203 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 204 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 205 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 206 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 207 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 208 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 209 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 210 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 211 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 212 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 213 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 214 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 215 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 216 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 217 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 218 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 219 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 220 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 221 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 222 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 223 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 224 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 225 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 226 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 227 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 228 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 229 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 230 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 231 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 232 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 233 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 234 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 235 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 236 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 237 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 238 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 239 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 240 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 241 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 242 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 243 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 244 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 245 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 246 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 247 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 248 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 249 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 250 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 251 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 252 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 253 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 254 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 255 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 256 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 257 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 258 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 259 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 260 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 261 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 262 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 263 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 264 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 265 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 266 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 267 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 268 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 269 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 270 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 271 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 272 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 273 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 274 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 275 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 276 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 277 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 278 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 279 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 280 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 281 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 282 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 283 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 284 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 285 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 286 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 287 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 288 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 289 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 290 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 291 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 292 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 293 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 294 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 295 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 296 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 297 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 298 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 299 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 300 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 301 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 302 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 303 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 304 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 305 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 306 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 307 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 308 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 309 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 310 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 311 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 312 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 313 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 314 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 315 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 316 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 317 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 318 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 319 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 320 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 321 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 322 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 323 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 324 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 325 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 326 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 327 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 328 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 329 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 330 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 331 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 332 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
