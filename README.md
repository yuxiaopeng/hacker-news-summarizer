# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-06-13.md)

*最后自动更新时间: 2026-06-13 18:35:21*
## 1. 美国禁止在人口普查数据中使用差分隐私。

**原文标题**: US bans differential privacy in Census data

**原文链接**: [https://desfontain.es/blog/banning-noise.html](https://desfontain.es/blog/banning-noise.html)

美国商务部最近发布了一项禁令，禁止人口普查局和经济分析局发布的统计产品使用“噪声注入”（特别是差分隐私）。这标志着政府在权衡公共数据效用与个人隐私保护方面发生了重大转变。

2020年人口普查采用了差分隐私技术，因为研究人员发现此前采用的“数据交换”等方法可能会导致个人记录被重构，从而违反联邦保密法。虽然差分隐私因其量化和缓解隐私风险的能力被科学家视为“金标准”，但它引入的透明“噪声”降低了数据的准确性。这令人口统计学家、社会科学家以及利用精确数据进行选区划分等任务的政治操盘手感到沮丧。

新指令要求回归“粗化”（数据泛化）和“抑制”（不公开小型数据集）等手段。作者认为这些工具既生硬又过时。对于人口普查等复杂数据集，这些技术往往会导致“双输”局面：要么破坏了数据的效用（尤其是对少数群体而言），要么使个人面临重新识别攻击的风险。如果没有噪声注入所提供的数学不确定性，攻击者想要破解个人身份将变得轻而易举。

该禁令背后的动机尚不明确。这可能是在尝试为政治目的提供重新识别的便利，也可能是为了隐瞒人口差异数据，或者仅仅是官僚机构试图忽视数据准确性与隐私之间固有的权衡。无论意图如何，作者警告称，这一决定可能导致未来发布的统计数据要么“极其危险”，要么“毫无用处”。

---

## 2. 治疗胰腺肿瘤可能已揭示癌症的总开关

**原文标题**: Treating pancreatic tumours may have revealed cancer's master switch

**原文链接**: [https://economist.com/science-and-technology/2026/06/12/treating-pancreatic-tumours-may-have-revealed-cancers-master-switch](https://economist.com/science-and-technology/2026/06/12/treating-pancreatic-tumours-may-have-revealed-cancers-master-switch)

无法访问文章链接。

---

## 3. 每一帧都完美

**原文标题**: Every Frame Perfect

**原文链接**: [https://tonsky.me/blog/every-frame-perfect/](https://tonsky.me/blog/every-frame-perfect/)

生成摘要时出错

---

## 4. 领略 Exif

**原文标题**: Appreciating Exif

**原文链接**: [https://brentfitzgerald.com/posts/appreciating-exif/](https://brentfitzgerald.com/posts/appreciating-exif/)

《深入理解 Exif》对**可交换图像文件格式 (Exif)** 进行了技术与实践层面的概述，该格式是数字图像中嵌入元数据的标准。Exif 创立于 1995 年，允许相机直接在图像文件中存储关键数据，如时间戳、GPS 坐标、相机设置和方向。

文章强调了几个关键技术方面：
*   **结构：** Exif 是一种嵌套在其他文件格式中的 TIFF 型数据结构。在 JPEG 文件中，它通常位于文件开头附近的 **APP1 标记段**。
*   **方向：** Exif 最关键的用途之一是**方向标签 (Orientation tag)**（取值为 1–8）。大多数相机不会旋转实际的像素矩阵，而是写入一个标签告知查看器如何显示像素。开发者在处理像素前应进行“归一化”或“自动旋转”，以避免显示错误。
*   **工具：** 作者将 **exiftool** 视为检查、编辑和清除元数据的行业标准，并指出它能够揭示厂商注释 (MakerNotes) 和嵌入缩略图等隐藏细节。
*   **更广泛的背景：** Exif 有别于其他元数据标准，如 **XMP**（Adobe 工作流）、**IPTC**（新闻摄影）、**ICC 配置文件**（色彩管理）以及较新的 **C2PA**（来源/AI 签名）。
*   **隐私与安全：** 操作系统或浏览器很少会自动清除元数据。如果用户和开发者希望保护位置或设备隐私，必须主动将其删除。

作者总结道，虽然 Exif 是一个带有一些局限性的“老旧”标准，但它仍然是一个稳健且必要的解决方案，确保图像携带必要的上下文信息，以便现代软件能对其进行正确的显示和组织。

---

## 5. Show HN: Verso – A $14.99 Mac word processor with no subscription

**原文标题**: Show HN: Verso – A $14.99 Mac word processor with no subscription

**原文链接**: [https://www.versowriter.app](https://www.versowriter.app)

**Verso** is a native macOS word processor designed as a lightweight, subscription-free alternative to bloated software like Microsoft Word. Available for a one-time purchase of **$14.99** (with a 7-day free trial), it targets writers who want a fast, "no-nonsense" experience without recurring fees or tracking.

**Key Features:**
*   **Focus & UI:** A "Focus Mode" that fades out everything except the current paragraph, alongside five page colors (including dark mode) and a customizable toolbar.
*   **Compatibility:** Full support for opening and saving `.docx` files without formatting breaks. It also handles `.odt`, `.rtf`, and `.pdf` exports.
*   **Editing Tools:** Includes a "Track Changes" system with a sidebar for managing edits, comments, footnotes, auto-generated Tables of Contents, and LaTeX math support.
*   **Developer-Friendly:** Unique "round-trip" Markdown support allows users to edit `.md` files as rich text. It includes syntax highlighting for 22 programming languages and live-rendering for Mermaid diagrams.
*   **Performance:** Built specifically for Mac (macOS 14+), the app features instant launch times, offline functionality, and native localization in 16 languages.

Created by developer Tomasz, Verso positions itself between over-engineered office suites and overly simplistic text editors. By offering a permanent license for a fraction of the cost of competitors like Ulysses or iA Writer, Verso aims to provide a high-value, privacy-conscious tool for the modern Mac writer.

---

## 6. 阿拉伯语排版渲染经验与技术债简介

**原文标题**: Introduction to the experience of rendering Arabic typography&its technical debt

**原文链接**: [https://lr0.org/blog/p/arabic/](https://lr0.org/blog/p/arabic/)

本文探讨了在数字平台上渲染阿拉伯语排版的巨大技术与历史挑战，强调了将复杂的文字系统强行套入为拉丁文字设计的标准所造成的“技术债”。

作者指出了数字阿拉伯语渲染中的三个核心问题：

1. **对齐逻辑：** 拉丁文字通过拉伸单词间的间距来实现两端对齐，而古典阿拉伯语排版则使用“喀希达”（kashida，又称 tatwīl）——即拉伸字母本身的笔画。现代网络标准（CSS）往往不支持这一特性，导致文本边缘参差不齐，或者出现视觉上虽通顺但在传统上错误的词间距。
2. **塑形引擎：** 阿拉伯语天生具有连写性；字母会根据相邻字符改变形状（分为词首、词中、词尾或独立形式）。这意味着阿拉伯语文本是在渲染时由“塑形引擎”实时生成的。当软件缺乏这种引擎时（常见于旧版 PDF 库或简单的图形工具），字母会呈现断开状态，无法阅读。
3. **遗留编码与技术债：** 作者解释了由 Unicode “阿拉伯语表现形式”（Arabic Presentation Forms）引起的一种常见数据库“漏洞”。这些是 20 世纪 90 年代遗留下来的旧码位，编码的是具体的字母形状而非抽象字母。虽然它们在外观上与现代 Unicode 相同，但数字签名不同，除非经过适当的标准化（NFKC）处理，否则会导致搜索失败和数据不匹配。

阿拉伯语书法根植于由伊本·穆格莱（Ibn Muqla）等书法家制定的、拥有千年历史的比例系统（al-khaṭṭ al-mansūb），该系统将对齐视为一种“塑形”问题而非“间距”问题。作者总结道，阿拉伯语在网络上呈现出的“破碎”状态——从字母无法连接到错误的对齐方式——本质上是数百年的书法传统与并未考虑其独特逻辑的数字工具之间碰撞的结果。

---

## 7. 基于废旧手机的低碳计算平台

**原文标题**: A low-carbon computing platform from your retired phones

**原文链接**: [https://research.google/blog/a-low-carbon-computing-platform-from-your-retired-phones/](https://research.google/blog/a-low-carbon-computing-platform-from-your-retired-phones/)

为了应对硬件制造对环境的影响——特别是“隐含碳”排放——加州大学圣迭戈分校的研究人员在谷歌的支持下，正在开发一个“手机集群计算”平台。该项目将退役智能手机改造为低碳、低成本的云计算基础设施。

由于消费者通常每四年更换一次手机，许多拥有高性能且完好处理器的设备被过早弃用。研究人员发现，现代智能手机核心的单线程性能往往可以与服务器级处理器相媲美。通过提取占设备隐含碳约50%的主板，并拆除电池和屏幕等不必要或危险的组件，团队能够构建出高效的计算集群。

该项目的关键技术点包括：
*   **操作系统：** 采用通用Linux发行版取代面向移动端的安卓系统，以提高可编程性并消除针对消费者的特定限制。
*   **编排：** 使用Kubernetes管理跨集群的容器化应用。
*   **规模：** 基准测试表明，25至50部手机即可提供相当于一台现代服务器的算力。

加州大学圣迭戈分校计划在2026年秋季前部署一个包含2,000部手机的数据中心，提供相当于50台传统服务器的算力。该平台将为计算机科学专业的学生和研究人员提供支持，用于自动评分和托管Jupyter Notebook等任务。一个20部手机集群的早期实验成功处理了超过75名学生班级的峰值作业提交，性能达到甚至超过了传统的云端后端。该项目既是一个实用的计算资源，也是测试消费级硬件在持续运行的数据中心环境中可靠性的试验场。

---

## 8. Intel 8087 浮点芯片的核心加法器

**原文标题**: The adder at the heart of Intel's 8087 floating-point chip

**原文链接**: [https://www.righto.com/2026/06/intel-8087-adder-reverse-engineered.html](https://www.righto.com/2026/06/intel-8087-adder-reverse-engineered.html)

生成摘要时出错

---

## 9. GLM 5.2 Is Out

**原文标题**: GLM 5.2 Is Out

**原文链接**: [https://digg.com/tech/ii9xibgn](https://digg.com/tech/ii9xibgn)

Z.ai has announced the launch of **GLM-5.2**, its new flagship AI model designed to provide open and accessible intelligence for developers. 

Key details of the release include:

*   **Immediate Availability:** The model is currently accessible to all GLM Coding Plan users, including those on Lite, Pro, Max, and Team plans.
*   **Technical Capabilities:** GLM-5.2 features advanced coding power, a massive **1-million-token context window**, and high performance in complex, long-horizon tasks.
*   **Upcoming Services:** API access and dedicated chatbot services are scheduled to launch next week.
*   **Open Source Commitment:** In line with Z.ai’s mission to democratize AI, the model will be officially open-sourced next week under the **MIT License**.

This release positions GLM-5.2 as a major tool for the global developer community, emphasizing high-capacity performance and an open-source philosophy.

---

## 10. AI OSS tool repo goes archived over night after raising $7.3M Seed

**原文标题**: AI OSS tool repo goes archived over night after raising $7.3M Seed

**原文链接**: [https://github.com/tensorzero/tensorzero](https://github.com/tensorzero/tensorzero)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 2 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 3 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 4 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 5 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 6 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 7 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 8 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 9 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 10 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 11 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 12 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 13 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 14 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 15 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 16 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 17 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 18 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 19 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 20 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 21 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 22 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 23 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 24 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 25 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 26 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 27 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 28 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 29 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 30 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 31 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 32 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 33 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 34 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 35 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 36 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 37 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 38 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 39 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 40 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 41 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 42 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 43 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 44 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 45 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 46 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 47 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 48 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 49 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 50 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 51 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 52 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 53 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 54 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 55 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 56 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 57 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 58 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 59 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 60 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 61 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 62 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 63 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 64 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 65 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 66 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 67 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 68 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 69 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 70 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 71 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 72 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 73 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 74 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 75 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 76 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 77 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 78 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 79 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 80 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 81 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 82 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 83 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 84 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 85 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 86 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 87 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 88 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 89 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 90 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 91 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 92 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 93 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 94 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 95 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 96 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 97 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 98 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 99 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 100 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 101 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 102 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 103 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 104 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 105 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 106 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 107 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 108 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 109 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 110 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 111 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 112 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 113 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 114 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 115 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 116 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 117 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 118 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 119 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 120 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 121 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 122 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 123 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 124 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 125 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 126 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 127 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 128 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 129 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 130 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 131 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 132 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 133 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 134 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 135 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 136 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 137 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 138 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 139 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 140 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 141 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 142 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 143 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 144 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 145 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 146 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 147 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 148 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 149 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 150 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 151 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 152 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 153 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 154 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 155 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 156 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 157 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 158 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 159 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 160 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 161 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 162 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 163 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 164 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 165 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 166 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 167 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 168 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 169 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 170 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 171 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 172 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 173 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 174 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 175 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 176 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 177 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 178 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 179 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 180 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 181 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 182 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 183 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 184 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 185 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 186 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 187 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 188 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 189 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 190 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 191 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 192 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 193 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 194 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 195 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 196 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 197 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 198 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 199 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 200 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 201 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 202 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 203 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 204 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 205 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 206 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 207 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 208 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 209 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 210 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 211 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 212 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 213 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 214 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 215 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 216 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 217 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 218 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 219 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 220 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 221 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 222 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 223 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 224 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 225 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 226 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 227 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 228 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 229 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 230 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 231 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 232 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 233 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 234 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 235 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 236 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 237 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 238 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 239 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 240 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 241 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 242 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 243 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 244 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 245 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 246 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 247 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 248 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 249 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 250 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 251 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 252 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 253 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 254 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 255 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 256 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 257 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 258 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 259 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 260 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 261 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 262 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 263 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 264 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 265 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 266 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 267 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 268 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 269 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 270 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 271 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 272 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 273 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 274 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 275 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 276 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 277 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 278 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 279 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 280 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 281 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 282 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 283 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 284 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 285 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 286 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 287 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 288 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 289 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 290 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 291 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 292 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 293 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 294 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 295 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 296 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 297 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 298 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 299 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 300 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 301 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 302 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 303 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 304 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 305 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 306 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 307 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 308 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 309 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 310 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 311 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 312 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 313 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 314 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 315 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 316 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 317 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 318 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 319 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 320 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 321 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 322 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 323 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 324 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 325 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 326 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 327 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 328 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 329 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 330 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 331 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 332 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 333 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 334 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 335 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 336 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 337 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 338 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 339 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 340 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 341 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 342 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 343 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 344 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 345 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 346 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 347 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 348 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 349 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 350 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 351 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 352 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 353 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 354 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 355 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 356 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 357 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 358 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 359 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 360 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 361 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 362 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 363 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 364 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 365 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 366 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 367 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 368 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 369 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 370 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 371 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 372 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 373 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 374 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 375 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 376 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 377 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 378 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 379 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 380 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 381 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 382 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 383 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 384 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 385 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 386 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 387 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 388 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 389 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 390 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 391 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 392 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 393 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 394 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 395 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 396 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 397 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 398 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 399 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 400 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 401 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 402 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 403 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 404 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 405 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 406 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 407 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 408 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 409 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 410 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 411 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 412 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 413 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 414 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 415 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 416 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 417 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 418 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 419 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 420 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 421 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 422 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 423 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 424 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 425 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 426 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 427 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 428 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 429 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 430 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 431 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 432 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 433 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 434 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 435 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 436 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 437 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 438 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 439 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 440 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 441 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 442 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 443 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 444 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 445 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 446 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 447 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 448 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 449 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 450 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
