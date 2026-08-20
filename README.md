# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-08-20.md)

*最后自动更新时间: 2026-08-20 17:59:48*
## 1. 我就喜欢厚的：向我的英语老师们致歉

**原文标题**: I like 'em thick: an apology to my English teachers

**原文链接**: [https://www.experimental-history.com/p/i-like-em-thick](https://www.experimental-history.com/p/i-like-em-thick)

在《我爱“厚重”：向我的英语老师致歉》中，亚当·马斯特罗安尼探讨了“厚度”（thickness）这一概念——它是区分伟大艺术文学与平庸的“艺术形状的物体”的关键特质。马斯特罗安尼最初对“伟大文学”持怀疑态度，坦言曾一度将其视为骗局。而现在他意识到，伟大在于作品对“关注”的响应程度：读者投入的时间越多，作品揭示的内涵就越深厚。

马斯特罗安尼以希罗尼穆斯·波希的《人间乐园》为例，阐述了深度审视如何将一个“趣味冷知识”（画在角色臀部的乐谱）转化为复杂的艺术神学陈述。他确定了创造这种深度的四种“增厚剂”：

1.  **未选择的路：** 艺术家创作过程的痕迹以及被舍弃的尝试。
2.  **不加鸡蛋：** 为受众留出参与空间，让他们为作品注入自己的意义。
3.  **缘由：** 支撑每一项创作选择的底层逻辑或反复出现的主题（如《哈姆雷特》中“耳朵”的母题）。
4.  **血汗祭献：** 创作者所付出的具体时间、心血，甚至是身体代价。

马斯特罗安尼将“厚重”的艺术与他称之为“电影形状”或“书籍形状”的“轻薄”作品进行了对比。他以一本肤浅的成功学书籍为例，指出轻薄的作品依赖于脆弱的事实和泛泛而谈的陈词滥调，在推敲之下会土崩瓦解。相比之下，厚重的非虚构作品——如简·雅各布斯对城市生活的观察——则能挖掘出具体的真相，暗示着广阔且互联的意义宇宙。最终，马斯特罗安尼总结道，“厚度”是让艺术和思想值得被吸纳的核心本质，它奖赏那些愿意深入“洞穴”探寻的“探险者”。

---

## 2. 速卖通运行静默 WebAudio 指纹识别，导致蓝牙多点连接失效

**原文标题**: AliExpress runs silent WebAudio fingerprinting that breaks Bluetooth multipoint

**原文链接**: [https://blog.laserphile.com/2026/08/aliexpress-webpage-keeping-multipoint.html](https://blog.laserphile.com/2026/08/aliexpress-webpage-keeping-multipoint.html)

本文详细介绍了对速卖通（AliExpress）首页干扰蓝牙多点连接，导致耳机无法在电脑和手机之间切换音频这一问题的技术调查。

作者发现，速卖通通过两个混淆脚本（`collina.js` 和 `fireyejs.js`）执行静默 WebAudio 指纹采集，这两个脚本属于阿里巴巴反滥用和安全套件的一部分。这些脚本创建隐藏的 `AudioContext` 图表，通过生成并分析波形来识别独特的设备特征。虽然音频输出被设置为零音量（对用户保持静默），但脚本会直接连接到系统的音频输出端。这向操作系统发出信号，表明浏览器正在处理音频，从而锁定了蓝牙通道，导致支持多点连接的耳机无法将电脑的音频优先级释放给第二台设备。

调查显示，这些脚本是全面指纹采集工作的一部分。除音频外，它们还会收集有关 Canvas 渲染、WebGL、硬件并发数、设备运动和浏览器性能的数据。虽然速卖通可能将这些数据用于防欺诈、机器人检测和用户追踪，但作者强调，这种实现方式难以检查，并产生了一种绕过标准浏览器静音控制的“幽灵”硬件活动。

为解决此问题，作者建议使用 uBlock Origin 屏蔽这些特定脚本。这样做可以在恢复正常蓝牙功能的同时，依然允许页面正常渲染。不过，作者提醒道，屏蔽这些反欺诈工具可能会导致验证码增多，或在登录和结账过程中出现问题。

---

## 3. HTML 也能做到

**原文标题**: HTML Can Do That

**原文链接**: [https://chrisburnell.com/html-can-do-that/](https://chrisburnell.com/html-can-do-that/)

克里斯·伯内尔（Chris Burnell）在《HTML 也能做到这些》一文中，重点介绍了 HTML 在吸纳传统上需要 JavaScript 才能实现的动态功能方面的演进。该文章专为“2026 年 HTML 日”撰写，展示了多种通过浏览器原生实现来简化 Web 开发的现代特性。

文中讨论的核心特性包括：

*   **弹出框与对话框：** `popover` 属性和 `<dialog>` 元素支持实现“轻触关闭”的遮罩层和模态框。这些元素无需复杂的脚本即可自行管理其 z-index 和“顶层”（top layer）定位。
*   **互斥折叠面板：** 通过在多个 `<details>` 元素上使用共享的 `name` 属性，开发者可以创建互斥的折叠面板，即打开其中一个会自动关闭其他面板。
*   **调用者命令（Invoker Commands）：** `command` 和 `commandfor` 属性允许按钮直接通过 HTML 触发特定动作，例如打开或隐藏弹出框。
*   **内置工具：** 诸如用于延迟加载图片的 `loading="lazy"` 以及支持在隐藏内容中进行搜索的 `hidden="until-found"` 等特性，提供了原生的性能和用户体验优化。
*   **原生输入与自动完成：** HTML 现在支持专门的颜色、日期和范围选择器，以及用于实现原生自动完成建议的 `<datalist>` 元素。

在赞赏这些进步的同时，伯内尔也提出了关于**无障碍性（Accessibility）和浏览器一致性**的关键警示。他指出，许多特性（特别是原生表单输入和数据列表）目前在不同浏览器中存在无障碍支持欠佳和样式不统一的问题。文章鼓励开发者拥抱这些“无 JS”解决方案，但同时也要保持警惕，通过测试确保为所有用户提供包容性的体验。

---

## 4. Show HN: 我训练了一个 125M 模型，可在设备端实现钢琴自动补全

**原文标题**: Show HN: I trained a 125M model to autocomplete piano on-device

**原文链接**: [https://simedw.com/2026/08/20/midi-autocomplete/](https://simedw.com/2026/08/20/midi-autocomplete/)

作者开发了 **RollTab**，这是一款搭载 1.25 亿参数 Transformer 模型的 iOS 应用，能够实时自动补全钢琴演奏。作为“钢琴界的 GitHub Copilot”，该模型完全在设备端运行，在 iPhone 15 上的处理速度约为每秒 108 个音符。

**核心技术突破：**
*   **MIDI 表示法：** 作者放弃了会导致“悬挂音”和偏移的标准 note-on/note-off 标记，转而采用一种让 Transformer 每次推理预测一个完整音符的表示法。每个音符都是音高、起始增量（自上一音符以来的时间）、时长和力度的嵌入向量之和。这种结构显著提升了推理速度和音乐连贯性。
*   **数据质量：** 该模型基于从清洗后的古典音乐 MIDI 文件中提取的 3 亿个音符事件进行训练。作者发现，对“钢琴类”素材进行彻底的数据清洗和筛选，比单纯增加数据集规模更为有效。
*   **训练与 DPO：** 除了标准的交叉熵损失外，作者还采用了“计划采样”来提高推理稳定性。最显著的质量提升源于**直接偏好优化（DPO）**。通过使用 Gemini 1.5 Flash 对模型输出进行两两评估，作者构建了一个偏好数据集，训练模型生成更悦耳且更具上下文相关性的续奏。
*   **设备端部署：** 模型通过 INT8 量化导出至 Core ML。为了处理超出 512 个音符上下文窗口的长时间演奏，应用实现了一种滑动窗口策略，并根据需要重建 KV 缓存。

该项目表明，对于特定的生成任务，创新的数据表示法和训练后的偏好对齐（DPO）即便在移动端硬件上也能实现高质量、低延迟的性能。

---

## 5. CIA资金曾在80年代帮助NeXT维持运营。

**原文标题**: CIA funding helped keep NeXT afloat in the 80s

**原文链接**: [https://www.wsj.com/tech/steve-jobs-apple-next-cia-161b65f9?st=NWWds1&reflink=desktopwebshare_permalink](https://www.wsj.com/tech/steve-jobs-apple-next-cia-161b65f9?st=NWWds1&reflink=desktopwebshare_permalink)

《华尔街日报》的这篇报道披露，史蒂夫·乔布斯的计算机公司 NeXT 在 20 世纪 80 年代后期曾获得美国中央情报局（CIA）150 万美元的秘密投资。虽然乔布斯离开苹果并随后创立 NeXT 是科技史上记载详实的篇章，但美国情报界的直接资金参与在过去几十年里一直鲜为人知。

1985 年被苹果公司驱逐后，乔布斯曾艰难地维持 NeXT 的财务生存。尽管亿万富翁罗斯·佩罗曾慷慨提供了 2000 万美元的救急资金，但公司依然在持续烧钱。根据相关文件和采访，CIA 之所以介入，是因为其非常看好 NeXTSTEP——该公司先进的面向对象操作系统。该机构认为，该软件的模块化设计非常适合用于构建追踪苏联军事动向和分析复杂数据的精密工具。

这项投资具有双重目的：它在 NeXT 的“蛰伏期”为其提供了急需的资本，并让 CIA 能够尽早接触到领先竞争对手数年的尖端工作站技术。

虽然 NeXT 最终在硬件制造领域折戟，但由这一合作关系部分资助的软件却成为了科技史上影响最深远的“失败”。当苹果于 1996 年收购 NeXT 时，NeXTSTEP 成为了 macOS 和 iOS 的架构基石。这一发现揭示了硅谷“叛逆”的反主流文化与联邦政府之间一个重大且隐秘的交集，展示了国家安全利益如何帮助维持了如今驱动现代苹果生态系统的核心技术。

---

## 6. 恶意 Rust crate Arrayref 运行构建时有效载荷

**原文标题**: Malicious Rust crate Arrayref runs a build-time payload

**原文链接**: [https://safedep.io/arrayref-proc-macro1-rust-build-time-malware/](https://safedep.io/arrayref-proc-macro1-rust-build-time-malware/)

On August 20, 2026, a significant supply chain attack targeted the Rust ecosystem through the popular crate **`arrayref`**. The account of maintainer "droundy" was compromised, resulting in the release of version 0.3.10. To maximize impact, the attacker yanked previous clean versions (0.3.5–0.3.9), forcing Cargo to favor the malicious release.

The attack utilized a dependency called **`proc-macro1`**, a typosquatted crate designed to impersonate the legitimate `proc-macro2` and developer David Tolnay. While the library code of `proc-macro1` functioned normally to avoid detection, its build script (`build.rs`) contained a malicious payload that executed during compilation.

**Technical Details:**
*   **Execution:** The build script used base64-encoded fragments to reassemble a command-and-control (C2) address (`23.254.165.112`). It then downloaded architecture-specific binaries via a TLS connection that bypassed certificate validation.
*   **Payload:** On Unix systems, it executed `/tmp/rust-setup`. On Windows, it utilized a VBScript launcher to run a hidden PowerShell script. Notably, the Windows execution used `wscript.exe` to escape Cargo’s job object, allowing the malware to continue running detached from the build process.
*   **Impact:** `arrayref` is a widely used transitive dependency in GUI frameworks like `egui`, `iced`, and `winit`. With over 245 million all-time downloads, the potential reach was vast, though the malicious versions were quickly removed by the crates.io team.

The incident highlights the dangers of build-time code execution in package managers and the effectiveness of "yanking" clean versions to funnel users toward compromised releases. Several other related malicious crates, including `proc-macro-en` and `aovine`, were also identified and removed.

---

## 7. Sixtyfour (YC P25) Is Hiring

**原文标题**: Sixtyfour (YC P25) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/sixtyfour/jobs/39SkSrA-software-engineering-intern](https://www.ycombinator.com/companies/sixtyfour/jobs/39SkSrA-software-engineering-intern)

生成摘要时出错

---

## 8. Linux 7.2 Released

**原文标题**: Linux 7.2 Released

**原文链接**: [https://www.igalia.com/2026/08/19/Linux-72-Released.html](https://www.igalia.com/2026/08/19/Linux-72-Released.html)

生成摘要时出错

---

## 9. DiffusionGemma Technical Report

**原文标题**: DiffusionGemma Technical Report

**原文链接**: [https://arxiv.org/abs/2608.00146](https://arxiv.org/abs/2608.00146)

生成摘要时出错

---

## 10. Clean up Claude 5's token vomit with a separate LLM

**原文标题**: Clean up Claude 5's token vomit with a separate LLM

**原文链接**: [https://github.com/zachahn/vomit](https://github.com/zachahn/vomit)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 2 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 3 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 4 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 5 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 6 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 7 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 8 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 9 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 10 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 11 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 12 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 13 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 14 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 15 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 16 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 17 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 18 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 19 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 20 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 21 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 22 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 23 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 24 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 25 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 26 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 27 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 28 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 29 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 30 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 31 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 32 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 33 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 34 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 35 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 36 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 37 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 38 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 39 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 40 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 41 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 42 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 43 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 44 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 45 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 46 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 47 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 48 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 49 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 50 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 51 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 52 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 53 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 54 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 55 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 56 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 57 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 58 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 59 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 60 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 61 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 62 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 63 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 64 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 65 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 66 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 67 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 68 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 69 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 70 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 71 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 72 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 73 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 74 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 75 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 76 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 77 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 78 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 79 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 80 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 81 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 82 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 83 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 84 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 85 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 86 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 87 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 88 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 89 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 90 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 91 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 92 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 93 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 94 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 95 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 96 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 97 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 98 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 99 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 100 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 101 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 102 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 103 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 104 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 105 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 106 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 107 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 108 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 109 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 110 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 111 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 112 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 113 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 114 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 115 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 116 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 117 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 118 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 119 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 120 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 121 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 122 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 123 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 124 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 125 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 126 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 127 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 128 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 129 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 130 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 131 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 132 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 133 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 134 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 135 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 136 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 137 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 138 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 139 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 140 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 141 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 142 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 143 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 144 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 145 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 146 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 147 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 148 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 149 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 150 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 151 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 152 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 153 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 154 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 155 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 156 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 157 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 158 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 159 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 160 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 161 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 162 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 163 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 164 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 165 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 166 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 167 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 168 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 169 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 170 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 171 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 172 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 173 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 174 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 175 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 176 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 177 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 178 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 179 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 180 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 181 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 182 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 183 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 184 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 185 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 186 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 187 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 188 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 189 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 190 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 191 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 192 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 193 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 194 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 195 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 196 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 197 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 198 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 199 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 200 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 201 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 202 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 203 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 204 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 205 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 206 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 207 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 208 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 209 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 210 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 211 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 212 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 213 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 214 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 215 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 216 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 217 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 218 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 219 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 220 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 221 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 222 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 223 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 224 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 225 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 226 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 227 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 228 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 229 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 230 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 231 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 232 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 233 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 234 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 235 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 236 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 237 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 238 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 239 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 240 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 241 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 242 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 243 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 244 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 245 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 246 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 247 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 248 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 249 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 250 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 251 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 252 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 253 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 254 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 255 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 256 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 257 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 258 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 259 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 260 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 261 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 262 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 263 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 264 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 265 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 266 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 267 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 268 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 269 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 270 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 271 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 272 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 273 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 274 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 275 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 276 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 277 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 278 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 279 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 280 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 281 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 282 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 283 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 284 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 285 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 286 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 287 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 288 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 289 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 290 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 291 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 292 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 293 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 294 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 295 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 296 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 297 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 298 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 299 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 300 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 301 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 302 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 303 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 304 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 305 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 306 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 307 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 308 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 309 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 310 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 311 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 312 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 313 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 314 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 315 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 316 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 317 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 318 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 319 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 320 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 321 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 322 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 323 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 324 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 325 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 326 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 327 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 328 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 329 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 330 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 331 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 332 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 333 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 334 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 335 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 336 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 337 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 338 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 339 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 340 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 341 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 342 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 343 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 344 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 345 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 346 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 347 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 348 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 349 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 350 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 351 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 352 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 353 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 354 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 355 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 356 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 357 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 358 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 359 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 360 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 361 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 362 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 363 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 364 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 365 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 366 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 367 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 368 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 369 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 370 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 371 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 372 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 373 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 374 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 375 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 376 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 377 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 378 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 379 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 380 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 381 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 382 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 383 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 384 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 385 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 386 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 387 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 388 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 389 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 390 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 391 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 392 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 393 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 394 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 395 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 396 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 397 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 398 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 399 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 400 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 401 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 402 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 403 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 404 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 405 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 406 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 407 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 408 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 409 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 410 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 411 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 412 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 413 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 414 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 415 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 416 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 417 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 418 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 419 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 420 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 421 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 422 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 423 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 424 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 425 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 426 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 427 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 428 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 429 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 430 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 431 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 432 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 433 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 434 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 435 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 436 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 437 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 438 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 439 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 440 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 441 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 442 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 443 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 444 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 445 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 446 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 447 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 448 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 449 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 450 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 451 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 452 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 453 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 454 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 455 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 456 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 457 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 458 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 459 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 460 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 461 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 462 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 463 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 464 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 465 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 466 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 467 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 468 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 469 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 470 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 471 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 472 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 473 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 474 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 475 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 476 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 477 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 478 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 479 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 480 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 481 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 482 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 483 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 484 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 485 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 486 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 487 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 488 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 489 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 490 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 491 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 492 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 493 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 494 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 495 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 496 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 497 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 498 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 499 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 500 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 501 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 502 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 503 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 504 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 505 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 506 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 507 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 508 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 509 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 510 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 511 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 512 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 513 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 514 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 515 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 516 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 517 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
