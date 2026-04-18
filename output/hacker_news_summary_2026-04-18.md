# Hacker News 热门文章摘要 (2026-04-18)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 80386 Memory Pipeline

**原文标题**: 80386 Memory Pipeline

**原文链接**: [https://nand2mario.github.io/posts/2026/80386_memory_pipeline/](https://nand2mario.github.io/posts/2026/80386_memory_pipeline/)

生成摘要时出错

---

## 12. Amiga Graphics Archive

**原文标题**: Amiga Graphics Archive

**原文链接**: [https://amiga.lychesis.net/](https://amiga.lychesis.net/)

生成摘要时出错

---

## 13. Claude Design

**原文标题**: Claude Design

**原文链接**: [https://www.anthropic.com/news/claude-design-anthropic-labs](https://www.anthropic.com/news/claude-design-anthropic-labs)

生成摘要时出错

---

## 14. Category Theory Illustrated – Orders

**原文标题**: Category Theory Illustrated – Orders

**原文链接**: [https://abuseofnotation.github.io/category-theory-illustrated/04_order/](https://abuseofnotation.github.io/category-theory-illustrated/04_order/)

生成摘要时出错

---

## 15. Amazon is discontinuing Kindle for PC on June 30th

**原文标题**: Amazon is discontinuing Kindle for PC on June 30th

**原文链接**: [https://goodereader.com/blog/kindle/amazon-is-discontinuing-kindle-for-pc-on-june-30th](https://goodereader.com/blog/kindle/amazon-is-discontinuing-kindle-for-pc-on-june-30th)

生成摘要时出错

---

## 16. Why Japan has such good railways

**原文标题**: Why Japan has such good railways

**原文链接**: [https://worksinprogress.co/issue/why-japan-has-such-good-railways/](https://worksinprogress.co/issue/why-japan-has-such-good-railways/)

生成摘要时出错

---

## 17. It's OK to compare floating-points for equality

**原文标题**: It's OK to compare floating-points for equality

**原文链接**: [https://lisyarus.github.io/blog/posts/its-ok-to-compare-floating-points-for-equality.html](https://lisyarus.github.io/blog/posts/its-ok-to-compare-floating-points-for-equality.html)

生成摘要时出错

---

## 18. Understanding the FFT Algorithm (2013)

**原文标题**: Understanding the FFT Algorithm (2013)

**原文链接**: [https://jakevdp.github.io/blog/2013/08/28/understanding-the-fft/](https://jakevdp.github.io/blog/2013/08/28/understanding-the-fft/)

生成摘要时出错

---

## 19. Show HN: I made a calculator that works over disjoint sets of intervals

**原文标题**: Show HN: I made a calculator that works over disjoint sets of intervals

**原文链接**: [https://victorpoughon.github.io/interval-calculator/](https://victorpoughon.github.io/interval-calculator/)

生成摘要时出错

---

## 20. Measuring Claude 4.7's tokenizer costs

**原文标题**: Measuring Claude 4.7's tokenizer costs

**原文链接**: [https://www.claudecodecamp.com/p/i-measured-claude-4-7-s-new-tokenizer-here-s-what-it-costs-you](https://www.claudecodecamp.com/p/i-measured-claude-4-7-s-new-tokenizer-here-s-what-it-costs-you)

生成摘要时出错

---

## 21. A Dumb Introduction to Z3 (2025)

**原文标题**: A Dumb Introduction to Z3 (2025)

**原文链接**: [https://ar-ms.me/thoughts/a-gentle-introduction-to-z3/](https://ar-ms.me/thoughts/a-gentle-introduction-to-z3/)

生成摘要时出错

---

## 22. All 12 moonwalkers had "lunar hay fever" from dust smelling like gunpowder (2018)

**原文标题**: All 12 moonwalkers had "lunar hay fever" from dust smelling like gunpowder (2018)

**原文链接**: [https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/The_toxic_side_of_the_Moon](https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/The_toxic_side_of_the_Moon)

生成摘要时出错

---

## 23. The quiet disappearance of the free-range childhood

**原文标题**: The quiet disappearance of the free-range childhood

**原文链接**: [https://bigthink.com/mind-behavior/the-quiet-disappearance-of-the-free-range-childhood/](https://bigthink.com/mind-behavior/the-quiet-disappearance-of-the-free-range-childhood/)

生成摘要时出错

---

## 24. I’m spending months coding the old way

**原文标题**: I’m spending months coding the old way

**原文链接**: [https://miguelconner.substack.com/p/im-coding-by-hand](https://miguelconner.substack.com/p/im-coding-by-hand)

生成摘要时出错

---

## 25. The USDA's gardening zones have shifted. (Interactive app and map)

**原文标题**: The USDA's gardening zones have shifted. (Interactive app and map)

**原文链接**: [https://apps.npr.org/plant-hardiness-garden-map/](https://apps.npr.org/plant-hardiness-garden-map/)

生成摘要时出错

---

## 26. Towards trust in Emacs

**原文标题**: Towards trust in Emacs

**原文链接**: [https://eshelyaron.com/posts/2026-04-15-towards-trust-in-emacs.html](https://eshelyaron.com/posts/2026-04-15-towards-trust-in-emacs.html)

生成摘要时出错

---

## 27. The simple geometry behind any road

**原文标题**: The simple geometry behind any road

**原文链接**: [https://sandboxspirit.com/blog/simple-geometry-of-roads/](https://sandboxspirit.com/blog/simple-geometry-of-roads/)

生成摘要时出错

---

## 28. Brunost: The Nynorsk Programming Language

**原文标题**: Brunost: The Nynorsk Programming Language

**原文链接**: [https://lindbakk.com/blog/introducing-brunost](https://lindbakk.com/blog/introducing-brunost)

生成摘要时出错

---

## 29. Are the costs of AI agents also rising exponentially? (2025)

**原文标题**: Are the costs of AI agents also rising exponentially? (2025)

**原文链接**: [https://www.tobyord.com/writing/hourly-costs-for-ai-agents](https://www.tobyord.com/writing/hourly-costs-for-ai-agents)

生成摘要时出错

---

## 30. Show HN: Smol machines – subsecond coldstart, portable virtual machines

**原文标题**: Show HN: Smol machines – subsecond coldstart, portable virtual machines

**原文链接**: [https://github.com/smol-machines/smolvm](https://github.com/smol-machines/smolvm)

生成摘要时出错

---

## 31. "cat readme.txt" is not safe if you use iTerm2

**原文标题**: "cat readme.txt" is not safe if you use iTerm2

**原文链接**: [https://blog.calif.io/p/mad-bugs-even-cat-readmetxt-is-not](https://blog.calif.io/p/mad-bugs-even-cat-readmetxt-is-not)

生成摘要时出错

---

## 32. A simplified model of Fil-C

**原文标题**: A simplified model of Fil-C

**原文链接**: [https://www.corsix.org/content/simplified-model-of-fil-c](https://www.corsix.org/content/simplified-model-of-fil-c)

生成摘要时出错

---

## 33. Hyperscalers have already outspent most famous US megaprojects

**原文标题**: Hyperscalers have already outspent most famous US megaprojects

**原文链接**: [https://twitter.com/finmoorhouse/status/2044933442236776794](https://twitter.com/finmoorhouse/status/2044933442236776794)

生成摘要时出错

---

## 34. Slop Cop

**原文标题**: Slop Cop

**原文链接**: [https://awnist.com/slop-cop](https://awnist.com/slop-cop)

生成摘要时出错

---

## 35. Show HN: PanicLock – Close your MacBook lid disable TouchID –> password unlock

**原文标题**: Show HN: PanicLock – Close your MacBook lid disable TouchID –> password unlock

**原文链接**: [https://github.com/paniclock/paniclock/](https://github.com/paniclock/paniclock/)

生成摘要时出错

---

## 36. Respect to the Man Chasing AI Immortality, While Freeloading Off Our Platform

**原文标题**: Respect to the Man Chasing AI Immortality, While Freeloading Off Our Platform

**原文链接**: [https://blog.mulerun.com/p/ai-immortality-postmortem/](https://blog.mulerun.com/p/ai-immortality-postmortem/)

生成摘要时出错

---

## 37. Sherry Turkle: "We're losing the raw human part of being with each other" (2013)

**原文标题**: Sherry Turkle: "We're losing the raw human part of being with each other" (2013)

**原文链接**: [https://www.theguardian.com/science/2013/may/05/rational-heroes-sherry-turkle-mit](https://www.theguardian.com/science/2013/may/05/rational-heroes-sherry-turkle-mit)

生成摘要时出错

---

## 38. Middle schooler finds coin from Troy in Berlin

**原文标题**: Middle schooler finds coin from Troy in Berlin

**原文链接**: [https://www.thehistoryblog.com/archives/75848](https://www.thehistoryblog.com/archives/75848)

生成摘要时出错

---

## 39. Rewriting Every Syscall in a Linux Binary at Load Time

**原文标题**: Rewriting Every Syscall in a Linux Binary at Load Time

**原文链接**: [https://amitlimaye1.substack.com/p/rewriting-every-syscall-in-a-linux](https://amitlimaye1.substack.com/p/rewriting-every-syscall-in-a-linux)

生成摘要时出错

---

## 40. NASA Force

**原文标题**: NASA Force

**原文链接**: [https://nasaforce.gov/](https://nasaforce.gov/)

生成摘要时出错

---

## 41. Landmark ancient-genome study shows surprise acceleration of human evolution

**原文标题**: Landmark ancient-genome study shows surprise acceleration of human evolution

**原文链接**: [https://www.nature.com/articles/d41586-026-01204-5](https://www.nature.com/articles/d41586-026-01204-5)

生成摘要时出错

---

## 42. NIST gives up enriching most CVEs

**原文标题**: NIST gives up enriching most CVEs

**原文链接**: [https://risky.biz/risky-bulletin-nist-gives-up-enriching-most-cves/](https://risky.biz/risky-bulletin-nist-gives-up-enriching-most-cves/)

生成摘要时出错

---

## 43. Matt Mullenweg Says "The Wheels Have Fallen Off" in WordPress

**原文标题**: Matt Mullenweg Says "The Wheels Have Fallen Off" in WordPress

**原文链接**: [https://www.therepository.email/matt-mullenweg-says-the-wheels-have-fallen-off-in-wide-ranging-wordpress-critique](https://www.therepository.email/matt-mullenweg-says-the-wheels-have-fallen-off-in-wide-ranging-wordpress-critique)

生成摘要时出错

---

## 44. Show HN: Sfsym – Export Apple SF Symbols as Vector SVG/PDF/PNG

**原文标题**: Show HN: Sfsym – Export Apple SF Symbols as Vector SVG/PDF/PNG

**原文链接**: [https://github.com/yapstudios/sfsym](https://github.com/yapstudios/sfsym)

生成摘要时出错

---

## 45. Introducing: ShaderPad

**原文标题**: Introducing: ShaderPad

**原文链接**: [https://rileyjshaw.com/blog/introducing-shaderpad/](https://rileyjshaw.com/blog/introducing-shaderpad/)

生成摘要时出错

---

## 46. Casus Belli Engineering

**原文标题**: Casus Belli Engineering

**原文链接**: [https://marcosmagueta.com/blog/casus-belli-engineering/](https://marcosmagueta.com/blog/casus-belli-engineering/)

生成摘要时出错

---

## 47. Ban the sale of precise geolocation

**原文标题**: Ban the sale of precise geolocation

**原文链接**: [https://www.lawfaremedia.org/article/it-is-time-to-ban-the-sale-of-precise-geolocation](https://www.lawfaremedia.org/article/it-is-time-to-ban-the-sale-of-precise-geolocation)

生成摘要时出错

---

## 48. The Unix executable as a Smalltalk method (2025) [video]

**原文标题**: The Unix executable as a Smalltalk method (2025) [video]

**原文链接**: [https://www.youtube.com/watch?v=sZjPQ7vtLNA](https://www.youtube.com/watch?v=sZjPQ7vtLNA)

生成摘要时出错

---

## 49. The GNU libc atanh is correctly rounded

**原文标题**: The GNU libc atanh is correctly rounded

**原文链接**: [https://inria.hal.science/hal-05591661](https://inria.hal.science/hal-05591661)

生成摘要时出错

---

## 50. The AI Doomers Who Are Playing with Fire

**原文标题**: The AI Doomers Who Are Playing with Fire

**原文链接**: [https://gizmodo.com/the-ai-doomers-who-are-playing-with-fire-2000747606](https://gizmodo.com/the-ai-doomers-who-are-playing-with-fire-2000747606)

生成摘要时出错

---

## 51. Isaac Asimov: The Last Question (1956)

**原文标题**: Isaac Asimov: The Last Question (1956)

**原文链接**: [https://hex.ooo/library/last_question.html](https://hex.ooo/library/last_question.html)

生成摘要时出错

---

## 52. Fits on a Floppy – A Manifesto for Small Software

**原文标题**: Fits on a Floppy – A Manifesto for Small Software

**原文链接**: [https://fitsonafloppy.com](https://fitsonafloppy.com)

生成摘要时出错

---

## 53. Ada, its design, and the language that built the languages

**原文标题**: Ada, its design, and the language that built the languages

**原文链接**: [https://www.iqiipi.com/the-quiet-colossus.html](https://www.iqiipi.com/the-quiet-colossus.html)

生成摘要时出错

---

## 54. Healthchecks.io now uses self-hosted object storage

**原文标题**: Healthchecks.io now uses self-hosted object storage

**原文链接**: [https://blog.healthchecks.io/2026/04/healthchecks-io-now-uses-self-hosted-object-storage/](https://blog.healthchecks.io/2026/04/healthchecks-io-now-uses-self-hosted-object-storage/)

生成摘要时出错

---

## 55. Loonies for Loongsons

**原文标题**: Loonies for Loongsons

**原文链接**: [https://www.leadedsolder.com/2026/04/14/loongson-ls3a5000-debian-linux.html](https://www.leadedsolder.com/2026/04/14/loongson-ls3a5000-debian-linux.html)

生成摘要时出错

---

## 56. Connie Converse was a folk-music genius. Then she vanished

**原文标题**: Connie Converse was a folk-music genius. Then she vanished

**原文链接**: [https://www.bbc.com/culture/article/20260413-the-mystery-of-a-missing-folk-music-pioneer](https://www.bbc.com/culture/article/20260413-the-mystery-of-a-missing-folk-music-pioneer)

生成摘要时出错

---

## 57. Why scientists are nervous about fungi

**原文标题**: Why scientists are nervous about fungi

**原文链接**: [https://text.npr.org/g-s1-117632](https://text.npr.org/g-s1-117632)

生成摘要时出错

---

## 58. I built a 3D printing business and ran it for 8 months

**原文标题**: I built a 3D printing business and ran it for 8 months

**原文链接**: [https://www.wespiser.com/posts/2026-04-12-3D-Printing-Biz.html](https://www.wespiser.com/posts/2026-04-12-3D-Printing-Biz.html)

生成摘要时出错

---

## 59. Amazon won't release Fire Sticks that support sideloading anymore

**原文标题**: Amazon won't release Fire Sticks that support sideloading anymore

**原文链接**: [https://arstechnica.com/gadgets/2026/04/amazon-wont-release-fire-sticks-that-support-sideloading-anymore/](https://arstechnica.com/gadgets/2026/04/amazon-wont-release-fire-sticks-that-support-sideloading-anymore/)

生成摘要时出错

---

## 60. Experiment with ICEYE Open Data

**原文标题**: Experiment with ICEYE Open Data

**原文链接**: [https://www.iceye.com/open-data-initiative](https://www.iceye.com/open-data-initiative)

生成摘要时出错

---

## 61. Generating a color spectrum for an image

**原文标题**: Generating a color spectrum for an image

**原文链接**: [https://amandahinton.com/blog/generating-a-color-spectrum-for-an-image](https://amandahinton.com/blog/generating-a-color-spectrum-for-an-image)

生成摘要时出错

---

## 62. Detecting DOSBox from Within the Box

**原文标题**: Detecting DOSBox from Within the Box

**原文链接**: [https://datagirl.xyz/posts/dos_inside_the_box.html](https://datagirl.xyz/posts/dos_inside_the_box.html)

生成摘要时出错

---

## 63. Working hurts less than procrastinating, we fear the twinge of starting (2011)

**原文标题**: Working hurts less than procrastinating, we fear the twinge of starting (2011)

**原文链接**: [https://www.lesswrong.com/posts/9o3QBg2xJXcRCxGjS/working-hurts-less-than-procrastinating-we-fear-the-twinge](https://www.lesswrong.com/posts/9o3QBg2xJXcRCxGjS/working-hurts-less-than-procrastinating-we-fear-the-twinge)

生成摘要时出错

---

## 64. List of people imprisoned for editing Wikipedia

**原文标题**: List of people imprisoned for editing Wikipedia

**原文链接**: [https://en.wikipedia.org/wiki/List_of_people_imprisoned_for_editing_Wikipedia](https://en.wikipedia.org/wiki/List_of_people_imprisoned_for_editing_Wikipedia)

生成摘要时出错

---

## 65. Average is all you need

**原文标题**: Average is all you need

**原文链接**: [https://rawquery.dev/blog/average-is-all-you-need](https://rawquery.dev/blog/average-is-all-you-need)

生成摘要时出错

---

## 66. The Gregorio project – GPL tools for typesetting Gregorian chant

**原文标题**: The Gregorio project – GPL tools for typesetting Gregorian chant

**原文链接**: [https://gregorio-project.github.io/index.html](https://gregorio-project.github.io/index.html)

生成摘要时出错

---

## 67. Webloc: Analysis of Penlink's Ad-Based Geolocation Surveillance Tech

**原文标题**: Webloc: Analysis of Penlink's Ad-Based Geolocation Surveillance Tech

**原文链接**: [https://citizenlab.ca/research/analysis-of-penlinks-ad-based-geolocation-surveillance-tech/](https://citizenlab.ca/research/analysis-of-penlinks-ad-based-geolocation-surveillance-tech/)

生成摘要时出错

---

## 68. Teddy Roosevelt and Abraham Lincoln in the same photo (2010)

**原文标题**: Teddy Roosevelt and Abraham Lincoln in the same photo (2010)

**原文链接**: [https://prologue.blogs.archives.gov/2010/11/09/teddy-roosevelt-and-abraham-lincoln-in-the-same-photo/](https://prologue.blogs.archives.gov/2010/11/09/teddy-roosevelt-and-abraham-lincoln-in-the-same-photo/)

生成摘要时出错

---

## 69. Solitaire simulator for finding the best strategy: Current record is 8.590%

**原文标题**: Solitaire simulator for finding the best strategy: Current record is 8.590%

**原文链接**: [https://github.com/dacracot/Klondike3-Simulator](https://github.com/dacracot/Klondike3-Simulator)

生成摘要时出错

---

## 70. FIM – Linux framebuffer image viewer

**原文标题**: FIM – Linux framebuffer image viewer

**原文链接**: [https://www.nongnu.org/fbi-improved/](https://www.nongnu.org/fbi-improved/)

生成摘要时出错

---

## 71. Using a USB switch as a full KVM

**原文标题**: Using a USB switch as a full KVM

**原文链接**: [https://luke.hsiao.dev/blog/display-switch/](https://luke.hsiao.dev/blog/display-switch/)

生成摘要时出错

---

## 72. "Liberation Day" at OpenAI as multiple senior executives announce leaving

**原文标题**: "Liberation Day" at OpenAI as multiple senior executives announce leaving

**原文链接**: [https://mas.to/@carnage4life/116422881496195720](https://mas.to/@carnage4life/116422881496195720)

生成摘要时出错

---

## 73. A Python Interpreter Written in Python

**原文标题**: A Python Interpreter Written in Python

**原文链接**: [https://aosabook.org/en/500L/a-python-interpreter-written-in-python.html](https://aosabook.org/en/500L/a-python-interpreter-written-in-python.html)

生成摘要时出错

---

## 74. The big business of survival bunkers

**原文标题**: The big business of survival bunkers

**原文链接**: [https://www.economist.com/united-states/2026/04/16/the-big-business-of-survival-bunkers](https://www.economist.com/united-states/2026/04/16/the-big-business-of-survival-bunkers)

生成摘要时出错

---

## 75. Show HN: Stage – Putting humans back in control of code review

**原文标题**: Show HN: Stage – Putting humans back in control of code review

**原文链接**: [https://stagereview.app/](https://stagereview.app/)

生成摘要时出错

---

## 76. Designing the Transport Typeface

**原文标题**: Designing the Transport Typeface

**原文链接**: [https://www.thamesandhudson.com/blogs/all-news-features/designing-the-transport-typeface-margaret-calvert-on-the-making-of-britain-s-road-signs](https://www.thamesandhudson.com/blogs/all-news-features/designing-the-transport-typeface-margaret-calvert-on-the-making-of-britain-s-road-signs)

生成摘要时出错

---

## 77. Random musings: 80s hardware, cyberdecks

**原文标题**: Random musings: 80s hardware, cyberdecks

**原文链接**: [https://strangelyentangled.com/blog/musings-80s-hardware/](https://strangelyentangled.com/blog/musings-80s-hardware/)

生成摘要时出错

---

## 78. Binary Encodings for JSON and Variant

**原文标题**: Binary Encodings for JSON and Variant

**原文链接**: [https://jincongho.com/posts/designing-binary-encodings-for-json-and-variant/](https://jincongho.com/posts/designing-binary-encodings-for-json-and-variant/)

生成摘要时出错

---

## 79. Ben Lerner's Big Feelings

**原文标题**: Ben Lerner's Big Feelings

**原文链接**: [https://www.vulture.com/article/ben-lerner-transcription-interview.html](https://www.vulture.com/article/ben-lerner-transcription-interview.html)

生成摘要时出错

---

## 80. Fulu bounty for Ring Camera jailbreak reaches $23k

**原文标题**: Fulu bounty for Ring Camera jailbreak reaches $23k

**原文链接**: [https://bounties.fulu.org/bounties/ring-video-doorbells](https://bounties.fulu.org/bounties/ring-video-doorbells)

生成摘要时出错

---

## 81. Human Accelerated Region 1

**原文标题**: Human Accelerated Region 1

**原文链接**: [https://en.wikipedia.org/wiki/Human_accelerated_region_1](https://en.wikipedia.org/wiki/Human_accelerated_region_1)

生成摘要时出错

---

## 82. Remember? "Sideloading" is here to stay, and won't go away, they said?

**原文标题**: Remember? "Sideloading" is here to stay, and won't go away, they said?

**原文链接**: [https://floss.social/@IzzyOnDroid/116415766636505917](https://floss.social/@IzzyOnDroid/116415766636505917)

生成摘要时出错

---

## 83. Show HN: I can't write Python. It works anyway

**原文标题**: Show HN: I can't write Python. It works anyway

**原文链接**: [https://github.com/Wewoc/Garmin_Local_Archive](https://github.com/Wewoc/Garmin_Local_Archive)

生成摘要时出错

---

## 84. The beginning of scarcity in AI

**原文标题**: The beginning of scarcity in AI

**原文链接**: [https://tomtunguz.com/ai-compute-crisis-2026/](https://tomtunguz.com/ai-compute-crisis-2026/)

生成摘要时出错

---

## 85. Reflections on 30 years of HPC programming

**原文标题**: Reflections on 30 years of HPC programming

**原文链接**: [https://chapel-lang.org/blog/posts/30years/](https://chapel-lang.org/blog/posts/30years/)

生成摘要时出错

---

## 86. Traders place $760M bet on falling oil ahead of Hormuz announcement

**原文标题**: Traders place $760M bet on falling oil ahead of Hormuz announcement

**原文链接**: [https://www.reuters.com/sustainability/boards-policy-regulation/traders-place-760-million-bet-falling-oil-ahead-hormuz-announcement-2026-04-17/](https://www.reuters.com/sustainability/boards-policy-regulation/traders-place-760-million-bet-falling-oil-ahead-hormuz-announcement-2026-04-17/)

生成摘要时出错

---

## 87. The missing catalogue: why finding books in translation is still so hard

**原文标题**: The missing catalogue: why finding books in translation is still so hard

**原文链接**: [https://blogs.lse.ac.uk/impactofsocialsciences/2026/04/13/the-missing-catalogue-why-finding-books-in-translation-is-still-so-hard/](https://blogs.lse.ac.uk/impactofsocialsciences/2026/04/13/the-missing-catalogue-why-finding-books-in-translation-is-still-so-hard/)

生成摘要时出错

---

## 88. How to Host a Blog on a Subdirectory Instead of a Subdomain (2025)

**原文标题**: How to Host a Blog on a Subdirectory Instead of a Subdomain (2025)

**原文链接**: [https://www.davidma.org/blog/2025-11-14-host-your-blog-on-a-subdirectory/](https://www.davidma.org/blog/2025-11-14-host-your-blog-on-a-subdirectory/)

生成摘要时出错

---

## 89. Launch HN: Kampala (YC W26) – Reverse-Engineer Apps into APIs

**原文标题**: Launch HN: Kampala (YC W26) – Reverse-Engineer Apps into APIs

**原文链接**: [https://www.zatanna.ai/kampala](https://www.zatanna.ai/kampala)

生成摘要时出错

---

## 90. A better R programming experience thanks to Tree-sitter

**原文标题**: A better R programming experience thanks to Tree-sitter

**原文链接**: [https://ropensci.org/blog/2026/04/02/tree-sitter-overview/](https://ropensci.org/blog/2026/04/02/tree-sitter-overview/)

生成摘要时出错

---

## 91. It is incorrect to "normalize" // in HTTP URL paths

**原文标题**: It is incorrect to "normalize" // in HTTP URL paths

**原文链接**: [https://runxiyu.org/comp/doubleslash/](https://runxiyu.org/comp/doubleslash/)

生成摘要时出错

---

## 92. Trump deal with IRS could see him given $14B in taxpayer money

**原文标题**: Trump deal with IRS could see him given $14B in taxpayer money

**原文链接**: [https://www.9news.com.au/world/donald-trump-irs-lawsuit-suing-10-billion-dollars-tax-office-usa-politics-news/929663f2-f255-4936-8084-1d986ee08d65](https://www.9news.com.au/world/donald-trump-irs-lawsuit-suing-10-billion-dollars-tax-office-usa-politics-news/929663f2-f255-4936-8084-1d986ee08d65)

生成摘要时出错

---

## 93. CadQuery is an open-source Python library for building 3D CAD models

**原文标题**: CadQuery is an open-source Python library for building 3D CAD models

**原文链接**: [https://cadquery.github.io/](https://cadquery.github.io/)

生成摘要时出错

---

## 94. Artifacts: Versioned storage that speaks Git

**原文标题**: Artifacts: Versioned storage that speaks Git

**原文链接**: [https://blog.cloudflare.com/artifacts-git-for-agents-beta/](https://blog.cloudflare.com/artifacts-git-for-agents-beta/)

生成摘要时出错

---

## 95. Making Wax Sealed Letters at Scale

**原文标题**: Making Wax Sealed Letters at Scale

**原文链接**: [https://waxletter.com/](https://waxletter.com/)

生成摘要时出错

---

## 96. Show HN: MacMind – A transformer neural network in HyperCard on a 1989 Macintosh

**原文标题**: Show HN: MacMind – A transformer neural network in HyperCard on a 1989 Macintosh

**原文链接**: [https://github.com/SeanFDZ/macmind](https://github.com/SeanFDZ/macmind)

生成摘要时出错

---

## 97. Claude Opus 4.7

**原文标题**: Claude Opus 4.7

**原文链接**: [https://www.anthropic.com/news/claude-opus-4-7](https://www.anthropic.com/news/claude-opus-4-7)

生成摘要时出错

---

## 98. The FBI Director Is MIA

**原文标题**: The FBI Director Is MIA

**原文链接**: [https://www.theatlantic.com/politics/2026/04/kash-patel-fbi-director-drinking-absences/686839/](https://www.theatlantic.com/politics/2026/04/kash-patel-fbi-director-drinking-absences/686839/)

生成摘要时出错

---

## 99. Qwen3.6-35B-A3B on my laptop drew me a better pelican than Claude Opus 4.7

**原文标题**: Qwen3.6-35B-A3B on my laptop drew me a better pelican than Claude Opus 4.7

**原文链接**: [https://simonwillison.net/2026/Apr/16/qwen-beats-opus/](https://simonwillison.net/2026/Apr/16/qwen-beats-opus/)

生成摘要时出错

---

## 100. Official Clojure Documentary page with Video, Shownotes, and Links

**原文标题**: Official Clojure Documentary page with Video, Shownotes, and Links

**原文链接**: [https://clojure.org/about/documentary](https://clojure.org/about/documentary)

生成摘要时出错

---

