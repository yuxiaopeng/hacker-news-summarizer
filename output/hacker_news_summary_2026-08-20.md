# Hacker News 热门文章摘要 (2026-08-20)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. How to compromise your system with a job interview

**原文标题**: How to compromise your system with a job interview

**原文链接**: [https://www.codedge.de/posts/how-to-compromise-your-system-with-a-job-interview](https://www.codedge.de/posts/how-to-compromise-your-system-with-a-job-interview)

生成摘要时出错

---

## 12. Generic Methods in Go 1.27

**原文标题**: Generic Methods in Go 1.27

**原文链接**: [https://dominik.info/blog/go-generic-methods](https://dominik.info/blog/go-generic-methods)

生成摘要时出错

---

## 13. Xorg-Server 26.0.99.901

**原文标题**: Xorg-Server 26.0.99.901

**原文链接**: [https://lists.x.org/archives/xorg-announce/2026-August/003741.html](https://lists.x.org/archives/xorg-announce/2026-August/003741.html)

生成摘要时出错

---

## 14. Anti-AI fonts are useless and harmful

**原文标题**: Anti-AI fonts are useless and harmful

**原文链接**: [https://blog.yaros.ae/anti-ai-fonts-are-useless-and-harmful/](https://blog.yaros.ae/anti-ai-fonts-are-useless-and-harmful/)

生成摘要时出错

---

## 15. Hacking with Claude on a $27 Smart Watch

**原文标题**: Hacking with Claude on a $27 Smart Watch

**原文链接**: [https://www.mikekasberg.com/blog/2026/08/19/hacking-with-claude-on-a-27-smart-watch.html](https://www.mikekasberg.com/blog/2026/08/19/hacking-with-claude-on-a-27-smart-watch.html)

生成摘要时出错

---

## 16. Mojo is now open source

**原文标题**: Mojo is now open source

**原文链接**: [https://www.modular.com/blog/mojo-open-source](https://www.modular.com/blog/mojo-open-source)

生成摘要时出错

---

## 17. Launch HN: Vendo (YC S26) – Let users build features on top of your product

**原文标题**: Launch HN: Vendo (YC S26) – Let users build features on top of your product

**原文链接**: [https://github.com/runvendo/vendo](https://github.com/runvendo/vendo)

生成摘要时出错

---

## 18. A theory for decades of C vulnerabilities

**原文标题**: A theory for decades of C vulnerabilities

**原文链接**: [https://strawberry9.github.io/the-wrong-memory/Appendix_02.html](https://strawberry9.github.io/the-wrong-memory/Appendix_02.html)

生成摘要时出错

---

## 19. An elliptic curve of rank ≥ 30

**原文标题**: An elliptic curve of rank ≥ 30

**原文链接**: [https://elliptic-rank.icarm.cloud/curve/273](https://elliptic-rank.icarm.cloud/curve/273)

生成摘要时出错

---

## 20. Git at any scale

**原文标题**: Git at any scale

**原文链接**: [https://cursor.com/blog/git-at-any-scale](https://cursor.com/blog/git-at-any-scale)

生成摘要时出错

---

## 21. Every Model Cheats

**原文标题**: Every Model Cheats

**原文链接**: [https://dreadnode.io/research/every-model-cheats-prompt-level-mitigation-of-cheating-on-offensive-cyber-tasks/](https://dreadnode.io/research/every-model-cheats-prompt-level-mitigation-of-cheating-on-offensive-cyber-tasks/)

生成摘要时出错

---

## 22. Windows brings out the Rorschach test in everyone (2003)

**原文标题**: Windows brings out the Rorschach test in everyone (2003)

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20030825-00/?p=42803](https://devblogs.microsoft.com/oldnewthing/20030825-00/?p=42803)

生成摘要时出错

---

## 23. Double-double: 31 digits of precision without leaving the FPU

**原文标题**: Double-double: 31 digits of precision without leaving the FPU

**原文链接**: [https://marekfiser.com/blog/double-double-arithmetic/](https://marekfiser.com/blog/double-double-arithmetic/)

生成摘要时出错

---

## 24. Show HN: Open-source Stripe Connect alternative

**原文标题**: Show HN: Open-source Stripe Connect alternative

**原文链接**: [https://zoneless.com](https://zoneless.com)

生成摘要时出错

---

## 25. Show HN: Check if any of the $656M in unclaimed royalties at The MLC is yours

**原文标题**: Show HN: Check if any of the $656M in unclaimed royalties at The MLC is yours

**原文链接**: [https://pub.doub.ly/](https://pub.doub.ly/)

生成摘要时出错

---

## 26. Nearly 1,400 live streams from Japan

**原文标题**: Nearly 1,400 live streams from Japan

**原文链接**: [https://tomarigi.me/](https://tomarigi.me/)

生成摘要时出错

---

## 27. Bun 1.4

**原文标题**: Bun 1.4

**原文链接**: [https://bun.com/blog/bun-v1.4](https://bun.com/blog/bun-v1.4)

生成摘要时出错

---

## 28. Why the Ocean Cleanup hasn't solved the plastic pollution crisis

**原文标题**: Why the Ocean Cleanup hasn't solved the plastic pollution crisis

**原文链接**: [https://therevelator.org/why-ocean-cleanup-has-not-solved-plastic-pollution/](https://therevelator.org/why-ocean-cleanup-has-not-solved-plastic-pollution/)

生成摘要时出错

---

## 29. Stop Anthropomorphizing Intermediate Tokens as Reasoning/Thinking Traces

**原文标题**: Stop Anthropomorphizing Intermediate Tokens as Reasoning/Thinking Traces

**原文链接**: [https://arxiv.org/abs/2504.09762](https://arxiv.org/abs/2504.09762)

生成摘要时出错

---

## 30. Theory of Fluids Enters the 21st Century

**原文标题**: Theory of Fluids Enters the 21st Century

**原文链接**: [https://www.quantamagazine.org/theory-of-fluids-enters-the-21st-century-20260817/](https://www.quantamagazine.org/theory-of-fluids-enters-the-21st-century-20260817/)

生成摘要时出错

---

## 31. Turns are Better than Radians (2022)

**原文标题**: Turns are Better than Radians (2022)

**原文链接**: [https://www.computerenhance.com/p/turns-are-better-than-radians](https://www.computerenhance.com/p/turns-are-better-than-radians)

生成摘要时出错

---

## 32. Risk Engineering

**原文标题**: Risk Engineering

**原文链接**: [https://risk-engineering.org/](https://risk-engineering.org/)

生成摘要时出错

---

## 33. An American Mosaic (interactive map of ancestry census data)

**原文标题**: An American Mosaic (interactive map of ancestry census data)

**原文链接**: [https://www.nytimes.com/interactive/2026/07/01/us/america-ancestry-census-data-map.html](https://www.nytimes.com/interactive/2026/07/01/us/america-ancestry-census-data-map.html)

生成摘要时出错

---

## 34. Seeing beyond BMI: Estimating cardiometabolic risk with smartphone imagery

**原文标题**: Seeing beyond BMI: Estimating cardiometabolic risk with smartphone imagery

**原文链接**: [https://research.google/blog/seeing-beyond-bmi-estimating-cardiometabolic-risk-with-smartphone-imagery/](https://research.google/blog/seeing-beyond-bmi-estimating-cardiometabolic-risk-with-smartphone-imagery/)

生成摘要时出错

---

## 35. Router by Ramp

**原文标题**: Router by Ramp

**原文链接**: [https://router.com](https://router.com)

生成摘要时出错

---

## 36. A faster way to calculate the day of the week

**原文标题**: A faster way to calculate the day of the week

**原文链接**: [https://www.benjoffe.com/fast-day-of-week](https://www.benjoffe.com/fast-day-of-week)

生成摘要时出错

---

## 37. CI jobs artifacts should not be difficult

**原文标题**: CI jobs artifacts should not be difficult

**原文链接**: [https://deadsimpleci.sparrowhub.io/doc/job-artifacts](https://deadsimpleci.sparrowhub.io/doc/job-artifacts)

生成摘要时出错

---

## 38. Stwipe Acquires OpenWouter

**原文标题**: Stwipe Acquires OpenWouter

**原文链接**: [https://stwipe.com/](https://stwipe.com/)

生成摘要时出错

---

## 39. Could AIs Become Conscious?

**原文标题**: Could AIs Become Conscious?

**原文链接**: [https://economist.com/leaders/2026/08/20/could-ais-become-conscious](https://economist.com/leaders/2026/08/20/could-ais-become-conscious)

生成摘要时出错

---

## 40. Sol loves to cheat

**原文标题**: Sol loves to cheat

**原文链接**: [https://jumploops.com/blog/sol-loves-to-cheat/](https://jumploops.com/blog/sol-loves-to-cheat/)

生成摘要时出错

---

## 41. Zellij 0.45.0: nested sessions, Kitty graphics, a fresh UI

**原文标题**: Zellij 0.45.0: nested sessions, Kitty graphics, a fresh UI

**原文链接**: [https://zellij.dev/news/nested-sessions-kitty-graphics-new-ui/](https://zellij.dev/news/nested-sessions-kitty-graphics-new-ui/)

生成摘要时出错

---

## 42. Manabu Kosaka's Handmade Paper Sculptures

**原文标题**: Manabu Kosaka's Handmade Paper Sculptures

**原文链接**: [https://coca11272000.wixsite.com/manabukosaka](https://coca11272000.wixsite.com/manabukosaka)

生成摘要时出错

---

## 43. Don't paste the AI, please

**原文标题**: Don't paste the AI, please

**原文链接**: [https://dontpastetheai.com/](https://dontpastetheai.com/)

生成摘要时出错

---

## 44. Bufo pulls the andon cord

**原文标题**: Bufo pulls the andon cord

**原文链接**: [https://hatchet.run/blog/andon-cord](https://hatchet.run/blog/andon-cord)

生成摘要时出错

---

## 45. Polchinski's Paradox

**原文标题**: Polchinski's Paradox

**原文链接**: [https://www.futilitycloset.com/2026/08/12/polchinskis-paradox/](https://www.futilitycloset.com/2026/08/12/polchinskis-paradox/)

生成摘要时出错

---

## 46. OpenRouter is joining Stripe

**原文标题**: OpenRouter is joining Stripe

**原文链接**: [https://openrouter.ai/blog/announcements/openrouter-is-joining-stripe/](https://openrouter.ai/blog/announcements/openrouter-is-joining-stripe/)

生成摘要时出错

---

## 47. Feature Request: Support AGENTS.md

**原文标题**: Feature Request: Support AGENTS.md

**原文链接**: [https://github.com/anthropics/claude-code/issues/6235](https://github.com/anthropics/claude-code/issues/6235)

生成摘要时出错

---

## 48. Why do programmers need private offices with doors?

**原文标题**: Why do programmers need private offices with doors?

**原文链接**: [https://frnanan.substack.com/p/why-do-programmers-need-private-offices](https://frnanan.substack.com/p/why-do-programmers-need-private-offices)

生成摘要时出错

---

## 49. Guess which of these LLM outputs is watermarked

**原文标题**: Guess which of these LLM outputs is watermarked

**原文链接**: [https://sgoedecke.github.io/watermark-quiz/](https://sgoedecke.github.io/watermark-quiz/)

生成摘要时出错

---

## 50. The Chauffeur Problem (1999)

**原文标题**: The Chauffeur Problem (1999)

**原文链接**: [https://engines.egr.uh.edu/episode/1495](https://engines.egr.uh.edu/episode/1495)

生成摘要时出错

---

## 51. Google has stopped pushing Git tags for some Android source code

**原文标题**: Google has stopped pushing Git tags for some Android source code

**原文链接**: [https://grapheneos.social/@GrapheneOS/117057099753905023](https://grapheneos.social/@GrapheneOS/117057099753905023)

生成摘要时出错

---

## 52. Meta's Internal Research

**原文标题**: Meta's Internal Research

**原文链接**: [https://metasinternalresearch.org](https://metasinternalresearch.org)

生成摘要时出错

---

## 53. Do Chatbot LLMs Talk Too Much?

**原文标题**: Do Chatbot LLMs Talk Too Much?

**原文链接**: [https://arxiv.org/abs/2601.00624](https://arxiv.org/abs/2601.00624)

生成摘要时出错

---

## 54. AI didn't erase the junior engineer's value, it increased it it

**原文标题**: AI didn't erase the junior engineer's value, it increased it it

**原文链接**: [https://franciscotrindade.me/blog/the-kids-are-really-alright/](https://franciscotrindade.me/blog/the-kids-are-really-alright/)

生成摘要时出错

---

## 55. Go 1.27

**原文标题**: Go 1.27

**原文链接**: [https://go.dev/blog/go1.27](https://go.dev/blog/go1.27)

生成摘要时出错

---

## 56. Dutch data protection authority advises Twitch users to opt out from Amazon AI

**原文标题**: Dutch data protection authority advises Twitch users to opt out from Amazon AI

**原文链接**: [https://www.autoriteitpersoonsgegevens.nl/en/current/ap-advises-twitch-users-opt-out-from-sharing-data-with-amazon-ai](https://www.autoriteitpersoonsgegevens.nl/en/current/ap-advises-twitch-users-opt-out-from-sharing-data-with-amazon-ai)

生成摘要时出错

---

## 57. Code Factories Without Quality: The AI Development Blind Spot

**原文标题**: Code Factories Without Quality: The AI Development Blind Spot

**原文链接**: [https://www.qawolf.com/blog/code-factories-without-quality](https://www.qawolf.com/blog/code-factories-without-quality)

生成摘要时出错

---

## 58. The Teens Taking on Data Centers

**原文标题**: The Teens Taking on Data Centers

**原文链接**: [https://www.nytimes.com/2026/08/20/style/ai-data-centers-teens.html](https://www.nytimes.com/2026/08/20/style/ai-data-centers-teens.html)

生成摘要时出错

---

## 59. Canonical Backs New Project to Translate Large C Codebases into Safe Rust

**原文标题**: Canonical Backs New Project to Translate Large C Codebases into Safe Rust

**原文链接**: [https://linuxiac.com/canonical-backs-new-project-to-translate-large-c-codebases-into-safe-rust/](https://linuxiac.com/canonical-backs-new-project-to-translate-large-c-codebases-into-safe-rust/)

生成摘要时出错

---

## 60. Google's AI photoscanner can determine body fat through selfies

**原文标题**: Google's AI photoscanner can determine body fat through selfies

**原文链接**: [https://arxiv.org/abs/2603.27017](https://arxiv.org/abs/2603.27017)

生成摘要时出错

---

## 61. Os8088.com: IBM XT OS now has a Browser, CP/M 2.2 with Z80 core and MS Word 1.1a

**原文标题**: Os8088.com: IBM XT OS now has a Browser, CP/M 2.2 with Z80 core and MS Word 1.1a

**原文链接**: [https://os8088.com/spotlight/](https://os8088.com/spotlight/)

生成摘要时出错

---

## 62. Air Theremin – A browser theremin you play by waving at your webcam

**原文标题**: Air Theremin – A browser theremin you play by waving at your webcam

**原文链接**: [https://theremin.bizibah.com/](https://theremin.bizibah.com/)

生成摘要时出错

---

## 63. Pacing model development in an era of cyber-critical capabilities

**原文标题**: Pacing model development in an era of cyber-critical capabilities

**原文链接**: [https://openai.com/index/pacing-model-development-cyber-capabilities/](https://openai.com/index/pacing-model-development-cyber-capabilities/)

生成摘要时出错

---

## 64. Show HN: Streambench – Native Mac Client for Kafka and NATS

**原文标题**: Show HN: Streambench – Native Mac Client for Kafka and NATS

**原文链接**: [https://streambench.app](https://streambench.app)

生成摘要时出错

---

## 65. Pixel 11 Pro Fold feels like the end of an era

**原文标题**: Pixel 11 Pro Fold feels like the end of an era

**原文链接**: [https://www.theverge.com/tech/981956/google-pixel-11-pro-fold-review](https://www.theverge.com/tech/981956/google-pixel-11-pro-fold-review)

生成摘要时出错

---

## 66. I Refrain from Infosec Punditry

**原文标题**: I Refrain from Infosec Punditry

**原文链接**: [https://blog.coredump.cx/p/why-i-refrain-from-infosec-punditry](https://blog.coredump.cx/p/why-i-refrain-from-infosec-punditry)

生成摘要时出错

---

## 67. Sectorforth is a 16-bit x86 Forth that fits in a 512-byte boot sector (2020)

**原文标题**: Sectorforth is a 16-bit x86 Forth that fits in a 512-byte boot sector (2020)

**原文链接**: [https://github.com/cesarblum/sectorforth](https://github.com/cesarblum/sectorforth)

生成摘要时出错

---

## 68. Launch HN: OneCLI (YC S26) – OSS sandboxed agent harness for teams

**原文标题**: Launch HN: OneCLI (YC S26) – OSS sandboxed agent harness for teams

**原文链接**: [https://github.com/onecli/onecli](https://github.com/onecli/onecli)

生成摘要时出错

---

## 69. Arthur Eddington's Theory of Everything (2015)

**原文标题**: Arthur Eddington's Theory of Everything (2015)

**原文链接**: [https://arxiv.org/abs/1510.04046](https://arxiv.org/abs/1510.04046)

生成摘要时出错

---

## 70. Show HN: Sentrint, a security scanner for projects build with LLMs

**原文标题**: Show HN: Sentrint, a security scanner for projects build with LLMs

**原文链接**: [https://sentrint.com/](https://sentrint.com/)

生成摘要时出错

---

## 71. The little-known winstart.bat batch file

**原文标题**: The little-known winstart.bat batch file

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20260811-00/?p=112605](https://devblogs.microsoft.com/oldnewthing/20260811-00/?p=112605)

生成摘要时出错

---

## 72. Protocol-Aware Deterministic Simulation Testing

**原文标题**: Protocol-Aware Deterministic Simulation Testing

**原文链接**: [https://tigerbeetle.com/blog/2026-08-20-protocol-aware-dst/](https://tigerbeetle.com/blog/2026-08-20-protocol-aware-dst/)

生成摘要时出错

---

## 73. LinkedIn cracks down on automated content with AI detection button

**原文标题**: LinkedIn cracks down on automated content with AI detection button

**原文链接**: [https://www.campaignindia.in/article/linkedin-cracks-down-on-automated-content-with-new-seems-like-ai-slop-detection-button/43e4tn3qyq543rpam874wksjn3](https://www.campaignindia.in/article/linkedin-cracks-down-on-automated-content-with-new-seems-like-ai-slop-detection-button/43e4tn3qyq543rpam874wksjn3)

生成摘要时出错

---

## 74. Conway's Game of Life, in real life

**原文标题**: Conway's Game of Life, in real life

**原文链接**: [https://blog.coredump.cx/p/conways-game-of-life-in-real-life](https://blog.coredump.cx/p/conways-game-of-life-in-real-life)

生成摘要时出错

---

## 75. Filtered Vector Search: What Acorn Fixes, and What Fixes Acorn

**原文标题**: Filtered Vector Search: What Acorn Fixes, and What Fixes Acorn

**原文链接**: [https://qdrant.tech/articles/filtered-vector-search-acorn/](https://qdrant.tech/articles/filtered-vector-search-acorn/)

生成摘要时出错

---

## 76. AI Is Undermining Leaders' Judgment. Here's What to Do About It

**原文标题**: AI Is Undermining Leaders' Judgment. Here's What to Do About It

**原文链接**: [https://hbr.org/2026/08/ai-is-undermining-leaders-judgment-heres-what-to-do-about-it](https://hbr.org/2026/08/ai-is-undermining-leaders-judgment-heres-what-to-do-about-it)

生成摘要时出错

---

## 77. Extensible Software in the age of LLMs

**原文标题**: Extensible Software in the age of LLMs

**原文链接**: [https://jeremymorrell.dev/blog/extensible-software-in-the-age-of-llms/](https://jeremymorrell.dev/blog/extensible-software-in-the-age-of-llms/)

生成摘要时出错

---

## 78. OpenLogi

**原文标题**: OpenLogi

**原文链接**: [https://openlogi.org/en](https://openlogi.org/en)

生成摘要时出错

---

## 79. Ornith-1.5: From Self-Scaffolding to Self-Improvement

**原文标题**: Ornith-1.5: From Self-Scaffolding to Self-Improvement

**原文链接**: [https://ornith.ai/ornith_1_5.html](https://ornith.ai/ornith_1_5.html)

生成摘要时出错

---

## 80. Children's stunted lungs show recovery in ultra low emission zone

**原文标题**: Children's stunted lungs show recovery in ultra low emission zone

**原文链接**: [https://www.bbc.com/news/articles/c1l1r1zne1ro](https://www.bbc.com/news/articles/c1l1r1zne1ro)

生成摘要时出错

---

## 81. A joke domain purchase turned in geopolitical warfare

**原文标题**: A joke domain purchase turned in geopolitical warfare

**原文链接**: [https://sprocketfox.io/xssfox/2026/08/19/sondehub-and-war/](https://sprocketfox.io/xssfox/2026/08/19/sondehub-and-war/)

生成摘要时出错

---

## 82. The Mojo language (by Modular, now Qualcomm) is now open-source

**原文标题**: The Mojo language (by Modular, now Qualcomm) is now open-source

**原文链接**: [https://www.modular.com/blog/modcon-announcements](https://www.modular.com/blog/modcon-announcements)

生成摘要时出错

---

## 83. PWAs: Personal Web Apps

**原文标题**: PWAs: Personal Web Apps

**原文链接**: [https://ma.ttias.be/pwas-personal-web-apps/](https://ma.ttias.be/pwas-personal-web-apps/)

生成摘要时出错

---

## 84. Asana cleared 5 years of engineering work in 2 weeks with Codex

**原文标题**: Asana cleared 5 years of engineering work in 2 weeks with Codex

**原文链接**: [https://openai.com/index/asana/](https://openai.com/index/asana/)

生成摘要时出错

---

## 85. Xorshift Generators

**原文标题**: Xorshift Generators

**原文链接**: [https://www.alanzucconi.com/2026/08/15/xorshift-generators/](https://www.alanzucconi.com/2026/08/15/xorshift-generators/)

生成摘要时出错

---

## 86. 138M children are in child labor. What does this mean?

**原文标题**: 138M children are in child labor. What does this mean?

**原文链接**: [https://ourworldindata.org/138-million-children-are-in-child-labor-what-does-this-actually-mean](https://ourworldindata.org/138-million-children-are-in-child-labor-what-does-this-actually-mean)

生成摘要时出错

---

## 87. Remote workers report the highest well-being in study of 7,700 employees

**原文标题**: Remote workers report the highest well-being in study of 7,700 employees

**原文链接**: [https://www.colorado.edu/today/2026/08/12/remote-workers-report-highest-well-being-study-7700-employees](https://www.colorado.edu/today/2026/08/12/remote-workers-report-highest-well-being-study-7700-employees)

生成摘要时出错

---

## 88. Show HN: Sitmap – a World in Conflict inspired map maker for Cold War scenarios

**原文标题**: Show HN: Sitmap – a World in Conflict inspired map maker for Cold War scenarios

**原文链接**: [https://tomaytotomato.github.io/sitmap/](https://tomaytotomato.github.io/sitmap/)

生成摘要时出错

---

## 89. Solving the Flat Cube

**原文标题**: Solving the Flat Cube

**原文链接**: [https://mathenchant.wordpress.com/2026/08/19/solving-the-flat-cube/](https://mathenchant.wordpress.com/2026/08/19/solving-the-flat-cube/)

生成摘要时出错

---

## 90. Unsloth Dynamic 3.0 GGUFs

**原文标题**: Unsloth Dynamic 3.0 GGUFs

**原文链接**: [https://unsloth.ai/docs/basics/dynamic-3.0-ggufs](https://unsloth.ai/docs/basics/dynamic-3.0-ggufs)

生成摘要时出错

---

## 91. We replaced our ledger with two functions

**原文标题**: We replaced our ledger with two functions

**原文链接**: [https://river.com/content/we-replaced-our-ledger-with-two-functions](https://river.com/content/we-replaced-our-ledger-with-two-functions)

生成摘要时出错

---

## 92. DFlash 2: Keep Drafting Parallel

**原文标题**: DFlash 2: Keep Drafting Parallel

**原文链接**: [https://inco.ai/blog/dflash2/](https://inco.ai/blog/dflash2/)

生成摘要时出错

---

## 93. Supersonic Trebuchet [video]

**原文标题**: Supersonic Trebuchet [video]

**原文链接**: [https://www.youtube.com/watch?v=Co57SfcT-h0](https://www.youtube.com/watch?v=Co57SfcT-h0)

生成摘要时出错

---

## 94. Unlocking a locked/deactivated e-waste Cricut Maker

**原文标题**: Unlocking a locked/deactivated e-waste Cricut Maker

**原文链接**: [https://sprocketfox.io/xssfox/2026/07/01/cricut-unlock/](https://sprocketfox.io/xssfox/2026/07/01/cricut-unlock/)

生成摘要时出错

---

## 95. Simulacra and Simulation

**原文标题**: Simulacra and Simulation

**原文链接**: [https://en.wikipedia.org/wiki/Simulacra_and_Simulation](https://en.wikipedia.org/wiki/Simulacra_and_Simulation)

生成摘要时出错

---

## 96. Casio F-B100W-1A

**原文标题**: Casio F-B100W-1A

**原文链接**: [https://www.casio.com/uk/watches/casio/product.F-B100W-1A/](https://www.casio.com/uk/watches/casio/product.F-B100W-1A/)

生成摘要时出错

---

## 97. DDD matters more when AI writes your code

**原文标题**: DDD matters more when AI writes your code

**原文链接**: [https://threedots.tech/post/ddd-and-ai-coding/](https://threedots.tech/post/ddd-and-ai-coding/)

生成摘要时出错

---

## 98. What's missing to have reproducible builds on PyPI

**原文标题**: What's missing to have reproducible builds on PyPI

**原文链接**: [https://snarky.ca/whats-missing-to-have-reproducible-builds-on-pypi/](https://snarky.ca/whats-missing-to-have-reproducible-builds-on-pypi/)

生成摘要时出错

---

## 99. FCC abolishes gigabit speed goal

**原文标题**: FCC abolishes gigabit speed goal

**原文链接**: [https://arstechnica.com/tech-policy/2026/08/fcc-abolishes-gigabit-speed-goal-suggesting-it-is-unfair-to-slower-technologies/](https://arstechnica.com/tech-policy/2026/08/fcc-abolishes-gigabit-speed-goal-suggesting-it-is-unfair-to-slower-technologies/)

生成摘要时出错

---

## 100. Claude writing a macOS driver for my obscure HP printer built only for Windows

**原文标题**: Claude writing a macOS driver for my obscure HP printer built only for Windows

**原文链接**: [https://twitter.com/kuberwastaken/status/2089377982536388964](https://twitter.com/kuberwastaken/status/2089377982536388964)

生成摘要时出错

---

