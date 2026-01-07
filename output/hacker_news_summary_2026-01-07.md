# Hacker News 热门文章摘要 (2026-01-07)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 糖业干预研究并将心血管疾病归咎于脂肪 (2016)

**原文标题**: Sugar industry influenced researchers and blamed fat for CVD (2016)

**原文链接**: [https://www.ucsf.edu/news/2016/09/404081/sugar-papers-reveal-industry-role-shifting-national-heart-disease-focus](https://www.ucsf.edu/news/2016/09/404081/sugar-papers-reveal-industry-role-shifting-national-heart-disease-focus)

加州大学旧金山分校（UC San Francisco）研究人员在2016年的一项分析揭示，糖业从20世纪60年代起就开始操纵营养科学，将冠心病（CHD）的责任从糖转移到饮食脂肪上。通过利用行业内部文件，研究人员发现一个糖业贸易组织资助了“226号项目”，这是1967年发表在《新英格兰医学杂志》（NEJM）上的一篇由哈佛大学科学家撰写的文献综述。

糖业向研究人员支付了相当于5万美元（按2016年币值计算）的酬劳来完成该综述。文件显示，该行业主动设定了研究目标，挑选了纳入的文章，并在发表前审阅了草案。最终的综述淡化了蔗糖与心脏病关联的证据，同时夸大了饱和脂肪和胆固醇的风险。至关重要的是，该行业的资助和影响从未在《新英格兰医学杂志》上披露。

这种操纵对公共卫生产生了深远而长期的影响，塑造了数十年来优先考虑低脂饮食而非减糖的饮食指南和科学观点。第一作者克里斯廷·卡恩斯（Cristin Kearns）和资深作者斯坦顿·格兰茨（Stanton Glantz）指出，这一案例说明了相关行业如何通过微妙手段操纵结果以符合其自身利益。

加州大学旧金山分校的研究强调，营养科学领域迫切需要透明、独立的科学审查以及全面的财务信息披露。尽管现代证据已明确将添加糖与高血压和心血管疾病联系起来，但作者指出，在经历了数十年受行业影响的研究后，健康政策的调整一直进展缓慢。

---

## 2. LaTeX 咖啡渍 [pdf] (2021)

**原文标题**: LaTeX Coffee Stains [pdf] (2021)

**原文链接**: [https://ctan.math.illinois.edu/graphics/pgf/contrib/coffeestains/coffeestains-en.pdf](https://ctan.math.illinois.edu/graphics/pgf/contrib/coffeestains/coffeestains-en.pdf)

所提供的文本是“LaTeX Coffee Stains”的原始 PDF 流。这是一个由 Hanno Rein 设计的知名且搞怪的 LaTeX 宏包（具体为 `coffee4` 迭代版本）。

该文章及宏包具有独特的审美用途：允许用户通过编程方式在排版文档中添加**逼真的咖啡污渍**。其核心要点和关键信息包括：

*   **功能：** 该宏包提供了在 PDF 页面上叠加图形化咖啡圆环和飞溅墨点的命令。它主要用于幽默、艺术效果，或为数字文档增添一种“实体感”或“生活气息”。
*   **定制化：** 用户可以选择多种不同类型的污渍，从轻微的飞溅到厚重的深色圆环。该宏包允许精确控制每种污渍的**缩放、旋转、透明度（alpha）和位置**（X 和 Y 坐标）。
*   **技术实现：** 该宏包利用 `TikZ` 和 `eso-pic` 宏包来处理图形叠加。由于污渍是以矢量图形或高质量叠加层生成的，因此它们不会干扰底层的文本布局或搜索功能。
*   **历史背景：** 2021 版本是对 LaTeX 社区中这一“小众经典”工具的精炼更新。它反映了排版界俏皮的一面，即利用技术上的精确性来模拟现实世界物体的凌乱随机性。

总之，“LaTeX Coffee Stains”是一款创意工具，适用于希望通过高度可定制的透明咖啡主题图形，为专业文档增添一丝模拟“偶然”真实感的用户。

---

## 3. 全球航运地图

**原文标题**: Shipmap.org

**原文链接**: [https://www.shipmap.org/](https://www.shipmap.org/)

**Shipmap.org** 是由设计工作室 Kiln 和伦敦大学学院（UCL）能源研究所共同开发的一款交互式可视化工具。它追踪了 2012 年全年全球商船队的航行轨迹，深入展示了国际航运的规模及其对环境的影响。

**主要功能与数据**
该地图在海底地形图上展示了航线、港口名称以及动态的船舶位置。用户可以按五类船舶筛选数据：**集装箱船、干散货船、油轮、液化气船和车辆运输船**。平台还设有实时计数器，显示选定时间段内预计的二氧化碳排放量和最大载货量（以 TEU 或千吨等单位衡量）。

**研究方法**
该项目利用来自 **exactEarth** 的 AIS（自动识别系统）数据获取位置和速度信息，并结合了 **Clarksons Research** 提供的船舶技术规格。通过交叉引用这些来源，UCL 的研究人员根据国际海事组织（IMO）的标准，结合发动机类型和船体参数计算出每小时的二氧化碳排放量。最终的可视化系统基于 WebGL 构建，以实现高性能运行。

**用户交互**
用户可以通过时间轴导航地图、缩放特定区域，并通过切换航线和船型等图层来自定义显示内容。地图支持嵌入外部网站，创作者还提供用于印刷或定制安装的高分辨率版本。

该项目由欧洲气候基金会资助，背景音乐采用了巴赫的《哥德堡变奏曲》。

---

## 4. 吃真正的食物——推介全新膳食金字塔

**原文标题**: Eat Real Food – Introducing the New Pyramid

**原文链接**: [https://realfood.gov](https://realfood.gov)

本文介绍了“新金字塔”，这是美国饮食指南为了应对国家健康危机而做出的根本性转变。鉴于50%的美国人患有糖尿病或糖尿病前期，且90%的医疗支出与慢性病相关，该指南告别了数十年来偏重加工食品的建议，转而以“真实食物”为核心基础。

“真实食物”被定义为完整、营养密集且加工极少的食物。新金字塔优先考虑以下三大类别：

*   **蛋白质、乳制品和健康脂肪：** 强调动物和植物来源的高质量蛋白质（如肉类、鸡蛋、海鲜和全脂乳制品），以支持代谢和肌肉健康。建议每日目标为每公斤体重1.2-1.6克。
*   **蔬菜和水果：** 指南建议摄入多样化的新鲜全食农产品，具体为每天三份蔬菜和两份水果。
*   **全谷物：** 鼓励摄入富含纤维、经传统方式加工的谷物（如燕麦和酸种面包），同时严格限制精制碳水化合物。

该框架的一个关键组成部分是彻底剔除添加糖和工业油。与死板的饮食方案不同，新金字塔是一个灵活且基于科学的框架，旨在通过透明度和个人责任感帮助美国人重获健康。它提倡将水作为主要的补水来源，并强调健康应始于全食物营养，而非医疗干预。

---

## 5. A4纸的故事

**原文标题**: A4 Paper Stories

**原文链接**: [https://susam.net/a4-paper-stories.html](https://susam.net/a4-paper-stories.html)

在《A4纸的故事》中，Susam Pal 探讨了随处可见的 A4 纸的实用价值与数学之美。虽然作者承认 A4 纸并非标准测量工具，但在没有正式直尺时，他经常将其作为一种可靠且“足够好用”的尺子。

文章详述了 ISO 纸张标准背后的几何原理，解释了 A 系列纸张的长宽比被设计为 $\sqrt{2}:1$。这一独特的比例确保了当纸张平行于短边对半切开时，所得的两部分能保持与原纸张完全相同的比例。该系统始于 A0，其定义面积恰好为 $1\text{ m}^2$。经过四次对分后，便得到了 $21.0\text{ cm} \times 29.7\text{ cm}$ 的 A4 尺寸。

作者通过一个个人轶事展示了这一技巧：一群“技术宅”在争论电脑显示器的尺寸，而 Pal 仅凭一张 A4 纸，通过对齐纸张边缘并将其折叠成 A5 作为更小单位的参考，测量出了屏幕的宽度和高度。通过对他估算的数值（宽 $60\text{ cm}$，高 $34\text{ cm}$）应用勾股定理，并按每英寸 $2.54\text{ cm}$ 的比例进行换算，他成功计算出对角线长度约为 27 英寸。

归根结底，这篇文章是对数学常数的一次幽默赞美。相比于测量应用等现代替代方案，Pal 更青睐这些“铭刻于心”的尺寸，凸显了一个简单的标准化物品如何通过基础几何学解决日常问题。

---

## 6. 支持 Nushell 的理由 (2023)

**原文标题**: The Case for Nushell (2023)

**原文链接**: [https://www.sophiajt.com/case-for-nushell/](https://www.sophiajt.com/case-for-nushell/)

在《选择 Nushell 的理由 (2023)》一文中，作者认为 Bash 和 Zsh 等传统 Shell 是 POSIX 时代的陈旧产物，缺乏应对当今复杂环境所需的现代编程特性。尽管 Fish 等 Shell 改善了用户体验，PowerShell 引入了面向对象的管道，但作者主张 Nushell 代表了一种必要的范式转变。

论点的核心是从**基于文本到结构化数据**的转变。在传统的 Unix 管道中，命令通过纯文本进行通信，要求用户学习“标志语言”和复杂的解析逻辑来处理输出。相反，Nushell 通过管道传递结构化的表格和记录。这使得单个命令（如 `where`）无需手动解析即可过滤来自各种来源的数据，无论是文件系统、进程列表还是 CSV 文件。

Nushell 被呈现为三种组件的混合体：
1. **类型化脚本语言：** 它具有易读的语法、模式匹配和早期错误报告功能，能在脚本运行前捕获错误。
2. **交互式 Shell：** 它提供现代 IDE 支持，包括自动补全和悬停文档。
3. **数据处理系统：** 它通过数据帧（dataframes）和插件系统处理大型数据集。

作者承认坚持使用 POSIX 等普及标准的“惯性”，但批评它们已经过时（并引用了 `fi` 和 `esac` 等例子）。通过从诞生起就支持跨平台并将一切视为数据，Nushell 旨在推动开发者社区迈向一个更高效、起点更高的自动化新阶段。最终，作者将 Nushell 定义为不仅是一个 Shell，更是一个旨在满足 21 世纪计算需求的、以数据为中心的脚本引擎。

---

## 7. WebDAV 的重重陷阱：用 Go 编写客户端/服务端

**原文标题**: Many Hells of WebDAV: Writing a Client/Server in Go

**原文链接**: [https://candid.dev/blog/many-hells-of-webdav](https://candid.dev/blog/many-hells-of-webdav)

《WebDAV 的重重地狱》叙述了 Candid Development 为其产品 Homechart 开发基于 Go 语言的 WebDAV/CalDAV 客户端和服务器的艰辛历程。尽管这是一个已有数十年历史的标准，但作者发现，由于文档零散且行业采用标准不一，实现该标准的过程充满了挫败感。

项目伊始，团队试图遵循官方 RFC 规范，但很快发现这些规范晦涩难懂，且充斥着陈旧冗余的内容。为了取得进展，他们转向对 Apple、Google 和 Thunderbird 等主流实现进行逆向工程，利用 HTTP 代理和 Wireshark 梳理出实际的请求/响应行为。他们还遇到了 Go 原生 XML 库的技术障碍，最终构建了一个自定义包装器，以更有效地处理 WebDAV 的非结构化架构。

文章指出的核心挑战在于，对于行业巨头而言，“标准仅仅是建议”。像 Apple 和 Google 这样的大型供应商经常忽略部分 RFC 规范，或者虚标其并不支持的功能。与此同时，客户端的表现也高度不一致；例如，尽管许多客户端支持高效的集合同步，但 Apple 日历仍依赖于 `ctags` 和 `etags` 等旧有方法。

作者总结道，由于小型开发者缺乏科技巨头的市场影响力，他们被迫针对主流供应商的种种怪癖开发复杂的变通方案，而这些供应商并没有动力去严格遵守规范。最终，这篇文章为他人敲响了警钟：构建 WebDAV 库是一个极其磨人的过程，需要在一个充斥着不规范行为和技术债的环境中艰难前行。

---

## 8. Meditation as Wakeful Relaxation: Unclenching Smooth Muscle

**原文标题**: Meditation as Wakeful Relaxation: Unclenching Smooth Muscle

**原文链接**: [https://psychotechnology.substack.com/p/meditation-as-wakeful-relaxation](https://psychotechnology.substack.com/p/meditation-as-wakeful-relaxation)

生成摘要时出错

---

## 9. Health care data breach affects over 600k patients, Illinois agency says

**原文标题**: Health care data breach affects over 600k patients, Illinois agency says

**原文链接**: [https://www.nprillinois.org/illinois/2026-01-06/health-care-data-breach-affects-600-000-patients-illinois-agency-says](https://www.nprillinois.org/illinois/2026-01-06/health-care-data-breach-affects-600-000-patients-illinois-agency-says)

生成摘要时出错

---

## 10. BillG the Manager

**原文标题**: BillG the Manager

**原文链接**: [https://hardcoresoftware.learningbyshipping.com/p/019-billg-the-manager](https://hardcoresoftware.learningbyshipping.com/p/019-billg-the-manager)

生成摘要时出错

---

## 11. “Stop Designing Languages. Write Libraries Instead” (2016)

**原文标题**: “Stop Designing Languages. Write Libraries Instead” (2016)

**原文链接**: [https://lbstanza.org/purpose_of_programming_languages.html](https://lbstanza.org/purpose_of_programming_languages.html)

生成摘要时出错

---

## 12. Becoming a Centenarian

**原文标题**: Becoming a Centenarian

**原文链接**: [https://www.newyorker.com/magazine/2025/12/22/becoming-a-centenarian](https://www.newyorker.com/magazine/2025/12/22/becoming-a-centenarian)

生成摘要时出错

---

## 13. Creators of Tailwind laid off 75% of their engineering team

**原文标题**: Creators of Tailwind laid off 75% of their engineering team

**原文链接**: [https://github.com/tailwindlabs/tailwindcss.com/pull/2388](https://github.com/tailwindlabs/tailwindcss.com/pull/2388)

生成摘要时出错

---

## 14. The $14 Burrito: Why San Francisco Inflation Feels Higher Than 2.5%

**原文标题**: The $14 Burrito: Why San Francisco Inflation Feels Higher Than 2.5%

**原文链接**: [https://www.foglinesf.com/p/the-14-burrito-why-san-francisco-inflation-feels-higher-than-2-5](https://www.foglinesf.com/p/the-14-burrito-why-san-francisco-inflation-feels-higher-than-2-5)

生成摘要时出错

---

## 15. Show HN: I built a "Do not disturb" Device for my home office

**原文标题**: Show HN: I built a "Do not disturb" Device for my home office

**原文链接**: [https://apoorv.page/blogs/over-engineered-dnd](https://apoorv.page/blogs/over-engineered-dnd)

生成摘要时出错

---

## 16. Sergey Brin's Unretirement

**原文标题**: Sergey Brin's Unretirement

**原文链接**: [https://www.inc.com/jessica-stillman/google-co-founder-sergey-brins-unretirement-is-a-lesson-for-the-rest-of-us/91280208](https://www.inc.com/jessica-stillman/google-co-founder-sergey-brins-unretirement-is-a-lesson-for-the-rest-of-us/91280208)

生成摘要时出错

---

## 17. Optery (YC W22) Hiring a CISO and Web Scraping Engineers (Node) (US and Latam)

**原文标题**: Optery (YC W22) Hiring a CISO and Web Scraping Engineers (Node) (US and Latam)

**原文链接**: [https://www.optery.com/careers/](https://www.optery.com/careers/)

生成摘要时出错

---

## 18. Quake Brutalist Jam III

**原文标题**: Quake Brutalist Jam III

**原文链接**: [https://www.slipseer.com/index.php?resources/quake-brutalist-jam-iii.549/](https://www.slipseer.com/index.php?resources/quake-brutalist-jam-iii.549/)

生成摘要时出错

---

## 19. US Job Openings Decline to Lowest Level in More Than a Year

**原文标题**: US Job Openings Decline to Lowest Level in More Than a Year

**原文链接**: [https://www.bloomberg.com/news/articles/2026-01-07/us-job-openings-decline-to-lowest-level-in-more-than-a-year](https://www.bloomberg.com/news/articles/2026-01-07/us-job-openings-decline-to-lowest-level-in-more-than-a-year)

生成摘要时出错

---

## 20. Dell's CES 2026 chat was the most pleasingly un-AI briefing I've had in 5 years

**原文标题**: Dell's CES 2026 chat was the most pleasingly un-AI briefing I've had in 5 years

**原文链接**: [https://www.pcgamer.com/hardware/dells-ces-2026-chat-was-the-most-pleasingly-un-ai-briefing-ive-had-in-maybe-5-years/](https://www.pcgamer.com/hardware/dells-ces-2026-chat-was-the-most-pleasingly-un-ai-briefing-ive-had-in-maybe-5-years/)

生成摘要时出错

---

## 21. Show HN: KeelTest – AI-driven VS Code unit test generator with bug discovery

**原文标题**: Show HN: KeelTest – AI-driven VS Code unit test generator with bug discovery

**原文链接**: [https://keelcode.dev/keeltest](https://keelcode.dev/keeltest)

生成摘要时出错

---

## 22. Formal methods only solve half my problems

**原文标题**: Formal methods only solve half my problems

**原文链接**: [https://brooker.co.za/blog/2022/06/02/formal.html](https://brooker.co.za/blog/2022/06/02/formal.html)

生成摘要时出错

---

## 23. Target has their own forensic lab to investigate shoplifters

**原文标题**: Target has their own forensic lab to investigate shoplifters

**原文链接**: [https://thehorizonsun.com/features/2024/04/11/the-target-forensics-lab/](https://thehorizonsun.com/features/2024/04/11/the-target-forensics-lab/)

生成摘要时出错

---

## 24. Vector graphics on GPU

**原文标题**: Vector graphics on GPU

**原文链接**: [https://gasiulis.name/vector-graphics-on-gpu/](https://gasiulis.name/vector-graphics-on-gpu/)

生成摘要时出错

---

## 25. Stop Doom Scrolling, Start Doom Coding: Build via the terminal from your phone

**原文标题**: Stop Doom Scrolling, Start Doom Coding: Build via the terminal from your phone

**原文链接**: [https://github.com/rberg27/doom-coding](https://github.com/rberg27/doom-coding)

生成摘要时出错

---

## 26. Opus 4.5 is not the normal AI agent experience that I have had thus far

**原文标题**: Opus 4.5 is not the normal AI agent experience that I have had thus far

**原文链接**: [https://burkeholland.github.io/posts/opus-4-5-change-everything/](https://burkeholland.github.io/posts/opus-4-5-change-everything/)

生成摘要时出错

---

## 27. LLM Problems Observed in Humans

**原文标题**: LLM Problems Observed in Humans

**原文链接**: [https://embd.cc/llm-problems-observed-in-humans](https://embd.cc/llm-problems-observed-in-humans)

生成摘要时出错

---

## 28. Electronic nose for indoor mold detection and identification

**原文标题**: Electronic nose for indoor mold detection and identification

**原文链接**: [https://advanced.onlinelibrary.wiley.com/doi/10.1002/adsr.202500124](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adsr.202500124)

生成摘要时出错

---

## 29. A 30B Qwen model walks into a Raspberry Pi and runs in real time

**原文标题**: A 30B Qwen model walks into a Raspberry Pi and runs in real time

**原文链接**: [https://byteshape.com/blogs/Qwen3-30B-A3B-Instruct-2507/](https://byteshape.com/blogs/Qwen3-30B-A3B-Instruct-2507/)

生成摘要时出错

---

## 30. Show HN: Comet MCP – Give Claude Code a browser that can click

**原文标题**: Show HN: Comet MCP – Give Claude Code a browser that can click

**原文链接**: [https://github.com/hanzili/comet-mcp](https://github.com/hanzili/comet-mcp)

生成摘要时出错

---

## 31. The Eric and Wendy Schmidt Observatory System

**原文标题**: The Eric and Wendy Schmidt Observatory System

**原文链接**: [https://www.schmidtsciences.org/schmidt-observatory-system/](https://www.schmidtsciences.org/schmidt-observatory-system/)

生成摘要时出错

---

## 32. Commodore 64 floppy drive has the power to be a computer and runs BASIC

**原文标题**: Commodore 64 floppy drive has the power to be a computer and runs BASIC

**原文链接**: [https://www.tomshardware.com/pc-components/cpus/commodore-64-floppy-drive-has-the-power-to-be-a-computer-bulky-1982-commodore-1541-5-25-inch-drive-packs-a-1-mhz-mos-6502-cpu](https://www.tomshardware.com/pc-components/cpus/commodore-64-floppy-drive-has-the-power-to-be-a-computer-bulky-1982-commodore-1541-5-25-inch-drive-packs-a-1-mhz-mos-6502-cpu)

生成摘要时出错

---

## 33. Show HN: SMTP Tunnel – A SOCKS5 proxy disguised as email traffic to bypass DPI

**原文标题**: Show HN: SMTP Tunnel – A SOCKS5 proxy disguised as email traffic to bypass DPI

**原文链接**: [https://github.com/x011/smtp-tunnel-proxy](https://github.com/x011/smtp-tunnel-proxy)

生成摘要时出错

---

## 34. The creator of Claude Code's Claude setup

**原文标题**: The creator of Claude Code's Claude setup

**原文链接**: [https://twitter.com/bcherny/status/2007179832300581177](https://twitter.com/bcherny/status/2007179832300581177)

生成摘要时出错

---

## 35. Vietnam bans unskippable ads

**原文标题**: Vietnam bans unskippable ads

**原文链接**: [https://saigoneer.com/vietnam-news/28652-vienam-bans-unskippable-ads,-requires-skip-button-to-appear-after-5-seconds](https://saigoneer.com/vietnam-news/28652-vienam-bans-unskippable-ads,-requires-skip-button-to-appear-after-5-seconds)

生成摘要时出错

---

## 36. I wanted a camera that doesn't exist, so I built it

**原文标题**: I wanted a camera that doesn't exist, so I built it

**原文链接**: [https://medium.com/@cristi.baluta/i-wanted-a-camera-that-doesnt-exist-so-i-built-it-5f9864533eb7](https://medium.com/@cristi.baluta/i-wanted-a-camera-that-doesnt-exist-so-i-built-it-5f9864533eb7)

生成摘要时出错

---

## 37. Animal Diversity Web

**原文标题**: Animal Diversity Web

**原文链接**: [https://animaldiversity.org/](https://animaldiversity.org/)

生成摘要时出错

---

## 38. Texas A&M bans part of Plato's Symposium

**原文标题**: Texas A&M bans part of Plato's Symposium

**原文链接**: [https://dailynous.com/2026/01/06/texas-am-bans-plato/](https://dailynous.com/2026/01/06/texas-am-bans-plato/)

生成摘要时出错

---

## 39. On the slow death of scaling

**原文标题**: On the slow death of scaling

**原文链接**: [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5877662](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5877662)

生成摘要时出错

---

## 40. Oral microbiome sequencing after taking probiotics

**原文标题**: Oral microbiome sequencing after taking probiotics

**原文链接**: [https://blog.booleanbiotech.com/oral-microbiome-biogaia](https://blog.booleanbiotech.com/oral-microbiome-biogaia)

生成摘要时出错

---

## 41. We recreated Steve Jobs's 1975 Atari horoscope program

**原文标题**: We recreated Steve Jobs's 1975 Atari horoscope program

**原文链接**: [https://blog.adafruit.com/2026/01/06/we-recreated-steve-jobss-1975-atari-horoscope-program-and-you-can-run-it/](https://blog.adafruit.com/2026/01/06/we-recreated-steve-jobss-1975-atari-horoscope-program-and-you-can-run-it/)

生成摘要时出错

---

## 42. 排查与修复一个棘手的克隆 Bug

**原文标题**: Investigating and fixing a nasty clone bug

**原文链接**: [https://kobzol.github.io/rust/2025/12/30/investigating-and-fixing-a-nasty-clone-bug.html](https://kobzol.github.io/rust/2025/12/30/investigating-and-fixing-a-nasty-clone-bug.html)

生成摘要时出错

---

## 43. What *is* code? (2015)

**原文标题**: What *is* code? (2015)

**原文链接**: [https://www.bloomberg.com/graphics/2015-paul-ford-what-is-code/](https://www.bloomberg.com/graphics/2015-paul-ford-what-is-code/)

生成摘要时出错

---

## 44. High-Performance DBMSs with io_uring: When and How to use it

**原文标题**: High-Performance DBMSs with io_uring: When and How to use it

**原文链接**: [https://arxiv.org/abs/2512.04859](https://arxiv.org/abs/2512.04859)

生成摘要时出错

---

## 45. CES 2026: Taking the Lids Off AMD's Venice and MI400 SoCs

**原文标题**: CES 2026: Taking the Lids Off AMD's Venice and MI400 SoCs

**原文链接**: [https://chipsandcheese.com/p/ces-2026-taking-the-lids-off-amds](https://chipsandcheese.com/p/ces-2026-taking-the-lids-off-amds)

生成摘要时出错

---

## 46. Locating a Photo of a Vehicle in 30 Seconds with GeoSpy

**原文标题**: Locating a Photo of a Vehicle in 30 Seconds with GeoSpy

**原文链接**: [https://geospy.ai/blog/locating-a-photo-of-a-vehicle-in-30-seconds-with-geospy](https://geospy.ai/blog/locating-a-photo-of-a-vehicle-in-30-seconds-with-geospy)

生成摘要时出错

---

## 47. Two ways to crack a walnut, per Grothendieck (2025)

**原文标题**: Two ways to crack a walnut, per Grothendieck (2025)

**原文链接**: [https://shreevatsa.net/post/grothendieck-approaches/](https://shreevatsa.net/post/grothendieck-approaches/)

生成摘要时出错

---

## 48. Comparing AI agents to cybersecurity professionals in real-world pen testing

**原文标题**: Comparing AI agents to cybersecurity professionals in real-world pen testing

**原文链接**: [https://arxiv.org/abs/2512.09882](https://arxiv.org/abs/2512.09882)

生成摘要时出错

---

## 49. Calling All Hackers: How money works (2024)

**原文标题**: Calling All Hackers: How money works (2024)

**原文链接**: [https://phrack.org/issues/71/17](https://phrack.org/issues/71/17)

生成摘要时出错

---

## 50. The ISEE Trajectories

**原文标题**: The ISEE Trajectories

**原文链接**: [https://www.drmindle.com/isee/](https://www.drmindle.com/isee/)

生成摘要时出错

---

## 51. Show HN: VaultSandbox – Test your real MailGun/SES/etc. integration

**原文标题**: Show HN: VaultSandbox – Test your real MailGun/SES/etc. integration

**原文链接**: [https://vaultsandbox.com/](https://vaultsandbox.com/)

生成摘要时出错

---

## 52. enclose.horse

**原文标题**: enclose.horse

**原文链接**: [https://enclose.horse/](https://enclose.horse/)

生成摘要时出错

---

## 53. Passing of Joe Mancuso

**原文标题**: Passing of Joe Mancuso

**原文链接**: [https://github.com/MasoniteFramework/masonite/discussions/853](https://github.com/MasoniteFramework/masonite/discussions/853)

生成摘要时出错

---

## 54. My Snapdragon Dev Kit was healthy and working fine until a Windows update failed

**原文标题**: My Snapdragon Dev Kit was healthy and working fine until a Windows update failed

**原文链接**: [https://jasoneckert.github.io/myblog/how-microsoft-killed-my-snapdragon-devkit/](https://jasoneckert.github.io/myblog/how-microsoft-killed-my-snapdragon-devkit/)

生成摘要时出错

---

## 55. Netflix Migrates to Amazon Aurora: 75% Performance Boost and 28% Cost Reduction

**原文标题**: Netflix Migrates to Amazon Aurora: 75% Performance Boost and 28% Cost Reduction

**原文链接**: [https://www.infoq.com/news/2025/12/netflix-migrates-amazon-aurora/](https://www.infoq.com/news/2025/12/netflix-migrates-amazon-aurora/)

生成摘要时出错

---

## 56. Show HN: Make audio loops online

**原文标题**: Show HN: Make audio loops online

**原文链接**: [https://makeloops.online/](https://makeloops.online/)

生成摘要时出错

---

## 57. Dude, where's my supersonic jet?

**原文标题**: Dude, where's my supersonic jet?

**原文链接**: [https://rationaloptimistsociety.substack.com/p/dude-wheres-my-supersonic-jet](https://rationaloptimistsociety.substack.com/p/dude-wheres-my-supersonic-jet)

生成摘要时出错

---

## 58. Are we tired of social media? (2025)

**原文标题**: Are we tired of social media? (2025)

**原文链接**: [https://www.danielbrendel.com/blog/24-are-we-tired-of-social-media-once-and-for-all](https://www.danielbrendel.com/blog/24-are-we-tired-of-social-media-once-and-for-all)

生成摘要时出错

---

## 59. Show HN: Mantic.sh – A structural code search engine for AI agents

**原文标题**: Show HN: Mantic.sh – A structural code search engine for AI agents

**原文链接**: [https://github.com/marcoaapfortes/Mantic.sh](https://github.com/marcoaapfortes/Mantic.sh)

生成摘要时出错

---

## 60. Why Big Companies Keep Failing: The Stack Fallacy (2016)

**原文标题**: Why Big Companies Keep Failing: The Stack Fallacy (2016)

**原文链接**: [https://techcrunch.com/2016/01/18/why-big-companies-keep-failing-the-stack-fallacy/](https://techcrunch.com/2016/01/18/why-big-companies-keep-failing-the-stack-fallacy/)

生成摘要时出错

---

## 61. AWS raises GPU prices 15% on a Saturday, hopes you weren't paying attention

**原文标题**: AWS raises GPU prices 15% on a Saturday, hopes you weren't paying attention

**原文链接**: [https://www.theregister.com/2026/01/05/aws_price_increase/](https://www.theregister.com/2026/01/05/aws_price_increase/)

生成摘要时出错

---

## 62. Repair a ship’s hull still in the river in -50˚C (2022)

**原文标题**: Repair a ship’s hull still in the river in -50˚C (2022)

**原文链接**: [https://eugene.kaspersky.com/2022/04/26/how-to-repair-the-underside-of-a-ships-hull-still-in-the-river-in-50%CB%9Ac-yakutsk/](https://eugene.kaspersky.com/2022/04/26/how-to-repair-the-underside-of-a-ships-hull-still-in-the-river-in-50%CB%9Ac-yakutsk/)

生成摘要时出错

---

## 63. Show HN: 48-digit prime numbers every git commit

**原文标题**: Show HN: 48-digit prime numbers every git commit

**原文链接**: [https://textonly.github.io/git-prime/](https://textonly.github.io/git-prime/)

生成摘要时出错

---

## 64. How HTML changes in ePub

**原文标题**: How HTML changes in ePub

**原文链接**: [https://www.htmhell.dev/adventcalendar/2025/11/](https://www.htmhell.dev/adventcalendar/2025/11/)

生成摘要时出错

---

## 65. Life Under a Clicktatorship

**原文标题**: Life Under a Clicktatorship

**原文链接**: [https://donmoynihan.substack.com/p/life-under-a-clicktatorship](https://donmoynihan.substack.com/p/life-under-a-clicktatorship)

生成摘要时出错

---

## 66. Databases in 2025: A Year in Review

**原文标题**: Databases in 2025: A Year in Review

**原文链接**: [https://www.cs.cmu.edu/~pavlo/blog/2026/01/2025-databases-retrospective.html](https://www.cs.cmu.edu/~pavlo/blog/2026/01/2025-databases-retrospective.html)

生成摘要时出错

---

## 67. Ruby Array Pack Bleed

**原文标题**: Ruby Array Pack Bleed

**原文链接**: [https://nastystereo.com/security/ruby-pack.html](https://nastystereo.com/security/ruby-pack.html)

生成摘要时出错

---

## 68. How to Be Less Awkward

**原文标题**: How to Be Less Awkward

**原文链接**: [https://www.experimental-history.com/p/how-to-be-less-awkward](https://www.experimental-history.com/p/how-to-be-less-awkward)

生成摘要时出错

---

## 69. Volkswagen Brings Back Physical Buttons

**原文标题**: Volkswagen Brings Back Physical Buttons

**原文链接**: [https://www.caranddriver.com/news/a69916699/volkswagen-interior-physical-buttons-return/](https://www.caranddriver.com/news/a69916699/volkswagen-interior-physical-buttons-return/)

生成摘要时出错

---

## 70. XPER on the Commodore 64

**原文标题**: XPER on the Commodore 64

**原文链接**: [https://stonetools.ghost.io/xper-c64/](https://stonetools.ghost.io/xper-c64/)

生成摘要时出错

---

## 71. Video Game Websites in the early 00s

**原文标题**: Video Game Websites in the early 00s

**原文链接**: [https://www.webdesignmuseum.org/exhibitions/video-game-websites-in-the-early-00s](https://www.webdesignmuseum.org/exhibitions/video-game-websites-in-the-early-00s)

生成摘要时出错

---

## 72. There were BGP anomalies during the Venezuela blackout

**原文标题**: There were BGP anomalies during the Venezuela blackout

**原文链接**: [https://loworbitsecurity.com/radar/radar16/](https://loworbitsecurity.com/radar/radar16/)

生成摘要时出错

---

## 73. High-performance header-only container library for C++23 on x86-64

**原文标题**: High-performance header-only container library for C++23 on x86-64

**原文链接**: [https://github.com/kressler/fast-containers](https://github.com/kressler/fast-containers)

生成摘要时出错

---

## 74. "Inspector Dangerfuck", ANSI art comic from 1994

**原文标题**: "Inspector Dangerfuck", ANSI art comic from 1994

**原文链接**: [https://breakintochat.com/blog/2025/12/31/ansi-art-and-webcomics-part-3-eerie-and-inspector-dangerfuck/](https://breakintochat.com/blog/2025/12/31/ansi-art-and-webcomics-part-3-eerie-and-inspector-dangerfuck/)

生成摘要时出错

---

## 75. Firefox extension to redirect x.com to xcancel.com

**原文标题**: Firefox extension to redirect x.com to xcancel.com

**原文链接**: [https://addons.mozilla.org/en-US/firefox/addon/toxcancel/](https://addons.mozilla.org/en-US/firefox/addon/toxcancel/)

生成摘要时出错

---

## 76. Why the trans flag emoji is the 5-codepoint sequence it is

**原文标题**: Why the trans flag emoji is the 5-codepoint sequence it is

**原文链接**: [https://hecate.pink/blog/2026/trans-flag-emoji/](https://hecate.pink/blog/2026/trans-flag-emoji/)

生成摘要时出错

---

## 77. Loongarch Improvements with Box64

**原文标题**: Loongarch Improvements with Box64

**原文链接**: [https://box86.org/2026/01/new-box64-v0-4-0-released/](https://box86.org/2026/01/new-box64-v0-4-0-released/)

生成摘要时出错

---

## 78. Why is the Gmail app 700 MB?

**原文标题**: Why is the Gmail app 700 MB?

**原文链接**: [https://akr.am/blog/posts/why-is-the-gmail-app-700-mb](https://akr.am/blog/posts/why-is-the-gmail-app-700-mb)

生成摘要时出错

---

## 79. 65% of Hacker News posts have negative sentiment, and they outperform

**原文标题**: 65% of Hacker News posts have negative sentiment, and they outperform

**原文链接**: [https://philippdubach.com/standalone/hn-sentiment/](https://philippdubach.com/standalone/hn-sentiment/)

生成摘要时出错

---

## 80. VR-based brain training for ADHD

**原文标题**: VR-based brain training for ADHD

**原文链接**: [https://medium.com/@6thMind/vr-based-brain-training-for-adhd-what-the-2025-research-reveals-about-attention-and-learning-9db8067f6353](https://medium.com/@6thMind/vr-based-brain-training-for-adhd-what-the-2025-research-reveals-about-attention-and-learning-9db8067f6353)

生成摘要时出错

---

## 81. Show HN: Stash – Sync Markdown Files with Apple Notes via CLI

**原文标题**: Show HN: Stash – Sync Markdown Files with Apple Notes via CLI

**原文链接**: [https://github.com/shakedlokits/stash](https://github.com/shakedlokits/stash)

生成摘要时出错

---

## 82. Everyone hates OneDrive, Microsofts cloud app that steals and deletes files

**原文标题**: Everyone hates OneDrive, Microsofts cloud app that steals and deletes files

**原文链接**: [https://boingboing.net/2026/01/05/everyone-hates-onedrive-microsofts-cloud-app-that-steals-then-deletes-all-your-files.html](https://boingboing.net/2026/01/05/everyone-hates-onedrive-microsofts-cloud-app-that-steals-then-deletes-all-your-files.html)

生成摘要时出错

---

## 83. Show HN: Prism.Tools – Free and privacy-focused developer utilities

**原文标题**: Show HN: Prism.Tools – Free and privacy-focused developer utilities

**原文链接**: [https://blgardner.github.io/prism.tools/](https://blgardner.github.io/prism.tools/)

生成摘要时出错

---

## 84. JavaScript Analyzer – Burp Suite Extension

**原文标题**: JavaScript Analyzer – Burp Suite Extension

**原文链接**: [https://github.com/jenish-sojitra/JSAnalyzer](https://github.com/jenish-sojitra/JSAnalyzer)

生成摘要时出错

---

## 85. macOS 26.2 update enables 160MHz channels on 5GHz Wi-Fi networks

**原文标题**: macOS 26.2 update enables 160MHz channels on 5GHz Wi-Fi networks

**原文链接**: [https://www.cultofmac.com/news/apple-quietly-boosts-wi-fi-speeds-newer-macs-ipads](https://www.cultofmac.com/news/apple-quietly-boosts-wi-fi-speeds-newer-macs-ipads)

生成摘要时出错

---

## 86. Strange.website

**原文标题**: Strange.website

**原文链接**: [https://strange.website/](https://strange.website/)

生成摘要时出错

---

## 87. Intel Core Ultra Series 3 Debut as First Built on Intel 18A

**原文标题**: Intel Core Ultra Series 3 Debut as First Built on Intel 18A

**原文链接**: [https://newsroom.intel.com/client-computing/ces-2026-intel-core-ultra-series-3-debut-first-built-on-intel-18a](https://newsroom.intel.com/client-computing/ces-2026-intel-core-ultra-series-3-debut-first-built-on-intel-18a)

生成摘要时出错

---

## 88. GBC Boot Animation 88×31 Web Button

**原文标题**: GBC Boot Animation 88×31 Web Button

**原文链接**: [https://zakhary.dev/blog/gbc-web-button](https://zakhary.dev/blog/gbc-web-button)

生成摘要时出错

---

## 89. Recovering video game cheat codes from a long-defunct phone hotline service

**原文标题**: Recovering video game cheat codes from a long-defunct phone hotline service

**原文链接**: [https://32bits.substack.com/p/under-the-microscope-lma-manager](https://32bits.substack.com/p/under-the-microscope-lma-manager)

生成摘要时出错

---

## 90. The Agentic Self: Parallels Between AI and Self-Improvement

**原文标题**: The Agentic Self: Parallels Between AI and Self-Improvement

**原文链接**: [http://muratbuffalo.blogspot.com/2026/01/the-agentic-self-parallels-between-ai.html](http://muratbuffalo.blogspot.com/2026/01/the-agentic-self-parallels-between-ai.html)

生成摘要时出错

---

## 91. Show HN: Tailsnitch – A security auditor for Tailscale

**原文标题**: Show HN: Tailsnitch – A security auditor for Tailscale

**原文链接**: [https://github.com/Adversis/tailsnitch](https://github.com/Adversis/tailsnitch)

生成摘要时出错

---

## 92. Pebble Round 2

**原文标题**: Pebble Round 2

**原文链接**: [https://repebble.com/blog/pebble-round-2-the-most-stylish-pebble-ever](https://repebble.com/blog/pebble-round-2-the-most-stylish-pebble-ever)

生成摘要时出错

---

## 93. State of the Fin 2026-01-06

**原文标题**: State of the Fin 2026-01-06

**原文链接**: [https://jellyfin.org/posts/state-of-the-fin-2026-01-06/](https://jellyfin.org/posts/state-of-the-fin-2026-01-06/)

生成摘要时出错

---

## 94. Why didn't AI “join the workforce” in 2025?

**原文标题**: Why didn't AI “join the workforce” in 2025?

**原文链接**: [https://calnewport.com/why-didnt-ai-join-the-workforce-in-2025/](https://calnewport.com/why-didnt-ai-join-the-workforce-in-2025/)

生成摘要时出错

---

## 95. Self hosting my media library with Jellyfin and Wireguard on Hetzner

**原文标题**: Self hosting my media library with Jellyfin and Wireguard on Hetzner

**原文链接**: [https://layandreas.github.io/personal-blog/posts/how-spotify-made-me-self-host/](https://layandreas.github.io/personal-blog/posts/how-spotify-made-me-self-host/)

生成摘要时出错

---

## 96. SCiZE's Classic Warez Collection

**原文标题**: SCiZE's Classic Warez Collection

**原文链接**: [https://scenelist.org/](https://scenelist.org/)

生成摘要时出错

---

## 97. The Kimwolf botnet is stalking your local network

**原文标题**: The Kimwolf botnet is stalking your local network

**原文链接**: [https://krebsonsecurity.com/2026/01/the-kimwolf-botnet-is-stalking-your-local-network/](https://krebsonsecurity.com/2026/01/the-kimwolf-botnet-is-stalking-your-local-network/)

生成摘要时出错

---

## 98. U.S. Forces Seize Fleeing Tanker Being Escorted by Russian Vessels

**原文标题**: U.S. Forces Seize Fleeing Tanker Being Escorted by Russian Vessels

**原文链接**: [https://www.wsj.com/world/u-s-forces-launch-operation-to-seize-fleeing-oil-tanker-0d6443ab](https://www.wsj.com/world/u-s-forces-launch-operation-to-seize-fleeing-oil-tanker-0d6443ab)

生成摘要时出错

---

## 99. Hierarchical Autoregressive Modeling for Memory-Efficient Language Generation

**原文标题**: Hierarchical Autoregressive Modeling for Memory-Efficient Language Generation

**原文链接**: [https://arxiv.org/abs/2512.20687](https://arxiv.org/abs/2512.20687)

生成摘要时出错

---

## 100. Gemini Protocol Deployment Statistics

**原文标题**: Gemini Protocol Deployment Statistics

**原文链接**: [https://www.obsessivefacts.com/gemini-proxy?uri=gemini%3A%2F%2Fgemini.bortzmeyer.org%2Fsoftware%2Flupa%2Fstats.gmi](https://www.obsessivefacts.com/gemini-proxy?uri=gemini%3A%2F%2Fgemini.bortzmeyer.org%2Fsoftware%2Flupa%2Fstats.gmi)

生成摘要时出错

---

