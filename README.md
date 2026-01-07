# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-01-07.md)

*最后自动更新时间: 2026-01-07 17:54:32*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 2 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 3 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 4 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 5 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 6 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 7 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 8 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 9 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 10 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 11 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 12 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 13 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 14 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 15 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 16 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 17 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 18 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 19 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 20 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 21 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 22 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 23 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 24 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 25 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 26 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 27 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 28 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 29 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 30 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 31 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 32 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 33 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 34 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 35 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 36 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 37 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 38 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 39 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 40 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 41 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 42 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 43 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 44 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 45 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 46 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 47 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 48 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 49 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 50 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 51 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 52 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 53 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 54 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 55 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 56 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 57 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 58 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 59 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 60 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 61 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 62 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 63 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 64 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 65 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 66 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 67 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 68 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 69 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 70 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 71 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 72 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 73 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 74 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 75 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 76 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 77 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 78 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 79 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 80 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 81 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 82 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 83 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 84 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 85 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 86 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 87 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 88 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 89 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 90 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 91 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 92 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 93 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 94 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 95 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 96 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 97 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 98 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 99 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 100 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 101 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 102 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 103 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 104 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 105 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 106 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 107 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 108 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 109 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 110 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 111 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 112 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 113 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 114 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 115 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 116 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 117 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 118 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 119 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 120 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 121 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 122 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 123 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 124 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 125 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 126 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 127 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 128 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 129 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 130 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 131 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 132 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 133 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 134 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 135 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 136 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 137 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 138 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 139 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 140 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 141 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 142 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 143 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 144 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 145 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 146 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 147 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 148 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 149 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 150 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 151 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 152 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 153 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 154 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 155 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 156 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 157 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 158 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 159 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 160 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 161 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 162 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 163 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 164 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 165 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 166 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 167 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 168 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 169 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 170 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 171 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 172 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 173 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 174 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 175 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 176 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 177 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 178 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 179 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 180 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 181 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 182 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 183 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 184 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 185 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 186 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 187 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 188 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 189 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 190 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 191 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 192 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 193 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 194 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 195 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 196 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 197 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 198 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 199 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 200 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 201 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 202 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 203 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 204 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 205 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 206 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 207 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 208 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 209 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 210 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 211 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 212 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 213 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 214 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 215 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 216 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 217 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 218 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 219 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 220 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 221 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 222 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 223 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 224 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 225 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 226 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 227 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 228 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 229 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 230 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 231 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 232 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 233 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 234 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 235 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 236 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 237 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 238 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 239 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 240 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 241 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 242 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 243 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 244 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 245 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 246 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 247 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 248 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 249 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 250 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 251 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 252 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 253 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 254 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 255 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 256 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 257 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 258 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 259 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 260 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 261 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 262 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 263 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 264 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 265 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 266 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 267 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 268 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 269 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 270 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 271 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 272 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 273 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 274 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 275 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 276 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 277 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 278 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 279 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 280 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 281 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 282 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 283 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 284 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 285 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 286 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 287 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 288 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 289 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 290 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 291 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 292 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 293 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
