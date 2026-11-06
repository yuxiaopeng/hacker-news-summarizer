# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-11-06.md)

*最后自动更新时间: 2026-11-06 22:21:21*
## 1. 一个能向 Opus 寻求帮助的 Jev，能以 1/4 的成本实现 Opus 级别的准确度。

**原文标题**: A Jev that can ask Opus for help gives Opus accuracy at 4x lower cost

**原文链接**: [https://hightouch.com/blog/llm-judges-identity-resolution](https://hightouch.com/blog/llm-judges-identity-resolution)

本文探讨了如何以高性价比的方式实现**身份解析 (IDR)** 评分的自动化。身份解析是指将数据记录映射到现实世界中唯一个体的过程。文章特别关注于检测“过度合并”现象，即不同人的记录被错误地合并在一起。

研究人员对比了高端的“前沿模型”（Claude Opus 5.5）与更便宜、更快速的“决策模型”（Jev 和 GPT-6 Luna）。虽然前沿模型的准确率最高，但其价格显著更高且速度较慢。相比之下，决策模型的价格便宜多达 90 倍，速度快 10 倍，但在困难任务上的准确率落后约 6 个百分点。

核心发现是**置信度校准**的重要性。虽然 Luna 在简单案例上的开箱即用表现更好，但它在出错时往往过度自信。而 Jev 的校准效果更好，其错误通常与低置信度评分相关。这使得 Jev 在**混合模型框架**中更具优势：
1. Jev 处理所有记录。
2. 如果 Jev 的置信度低于特定阈值（如 30–90%），该案例将自动路由至 Claude Opus 进行二次复核。

**主要结果：**
*   **准确率：** 混合型 Jev 方案达到了前沿模型的准确率水平（简单测试为 98.8%，困难测试为 95.3%）。
*   **成本：** 在简单数据上，该混合方案的成本比单独使用 Opus **低 4 倍以上**；在困难数据上，成本降低了近 2 倍。
*   **可扩展性：** 混合系统根据任务难度自动调整支出；仅在数据存在噪声或复杂时，才会将更多案例路由给昂贵的模型。

文章总结指出，对于像 IDR 评分这样的复杂任务，将校准良好的廉价模型与前沿模型相结合，可以提供一种可扩展、高准确率的解决方案，其性价比优于任何单一模型。

---

## 2. 人工智能正在大幅加速人工智能研究。

**原文标题**: AI is dramatically accelerating AI research

**原文链接**: [https://www.planned-obsolescence.org/p/ai-is-dramatically-accelerating-ai](https://www.planned-obsolescence.org/p/ai-is-dramatically-accelerating-ai)

Ajeya Cotra 的这篇文章讨论了 METR 的一份报告，指出 AI 研究正以“惊人”的速度加速，在 Anthropic 尤为明显。截至 2026 年底，有证据表明 AI 能力的进步速度是历史常规水平的两倍，触及了 Anthropic《负责任扩展政策》（Responsible Scaling Policy）中定义的关键阈值。

核心观点包括：

*   **AI 驱动的自动化：** 这种加速主要归功于 AI 对研发（R&D）任务的自动化，而非算力或人力的增加。虽然整体进展翻倍，但个体研究人员的生产力实现了 10 到 12 倍的巨大提升，为开发带来了“时间扭曲”般的效果。
*   **复合式进展：** Cotra 认为，如果这种加速持续产生复合效应，简单的线性推演预示着在一年内即可实现超人工智能。随着 AI 不断改进用于构建 AI 的工具，进步的翻倍时间可能会从数月缩短至数周。
*   **生存风险与准备不足：** 作者警告称，该行业尚未为迫在眉睫的“智能爆炸”做好准备。目前各大实验室的安保水平被认为不足以保护模型权重免受国家级力量的侵害，且稳健的对齐和治理框架尚未就绪。如果这些系统出现对齐偏差或被窃取，快速发展的超人工智能可能导致人类灭绝。
*   **缺乏透明度：** METR 报告中的许多证据已被删减。Cotra 强调，透明数据的缺失使外部科学家无法验证这些时间线，增加了世界应对这一转型的难度。

最后，本文发出了警示：AI 驱动研究的反馈回路正在显著缩短开发周期，而建立必要安全与防御措施的窗口期正在关闭。

---

## 3. Firecracker 虚拟机逃逸：PwnEscape 第 2 部分

**原文标题**: Firecracker VM Escape: PwnEscape Part 2

**原文链接**: [https://pwn.ai/blog/firecracker-escape](https://pwn.ai/blog/firecracker-escape)

生成摘要时出错

---

## 4. 美国联邦航空管理局表示将在2028年前从空中交通管制系统中逐步淘汰软盘。

**原文标题**: US FAA says it will phase out floppy disks from air traffic control by 2028

**原文链接**: [https://www.reuters.com/world/us/us-faa-says-it-will-phase-out-floppy-disks-air-traffic-control-by-2028-2026-11-05/](https://www.reuters.com/world/us/us-faa-says-it-will-phase-out-floppy-disks-air-traffic-control-by-2028-2026-11-05/)

无法访问文章链接。

---

## 5. 特斯拉将逐步缩减 Cybertruck 产量

**原文标题**: Tesla to wind down Cybertruck production

**原文链接**: [https://www.nbcnews.com/tech/tech-news/tesla-wind-cybertruck-production-years-poor-sales-markets-rcna607817](https://www.nbcnews.com/tech/tech-news/tesla-wind-cybertruck-production-years-poor-sales-markets-rcna607817)

Tesla CEO Elon Musk has announced that production of the Cybertruck at the Texas gigafactory will wind down by mid-2027. The decision follows years of disappointing sales for the futuristic pickup, which failed to meet Musk’s original target of 250,000 annual units. According to reports, Tesla sold only 20,237 Cybertrucks in 2025, a 48% drop from the previous year.

The primary reason for the wind-down is a strategic shift toward the **Cybercab**, Tesla’s dedicated robotaxi. Musk intends to repurpose the Austin facility’s production capacity to support his goal of transforming Tesla into an AI and robotics-focused company. The Cybercab, which lacks a steering wheel and pedals, is currently being tested in small pilot fleets in Austin.

Experts and analysts point to several factors that hindered the Cybertruck's success:
*   **Regulatory Barriers:** Its heavy, sharp-edged stainless-steel design made it impossible to gain safety approval in markets like Europe due to pedestrian impact regulations.
*   **Niche Appeal:** While touted as a rival to legacy pickups from Ford and GM, its unconventional design failed to capture the broader US market, where electric pickups have generally struggled.
*   **Manufacturing Complexity:** The Austin plant is the only facility equipped to handle the model's specialized components, making a relocation of production unlikely.

Musk described the move as the "end of an era" while maintaining that the Cybertruck was the "best vehicle Tesla has ever made." Lead engineer Wes Morrill added that the pickup served as a vital "technology development platform" that will live on through the innovations integrated into the Cybercab.

---

## 6. UEFI 裸机编程入门

**原文标题**: First steps in bare-metal programming using UEFI

**原文链接**: [https://kevinboone.me/efitest_index.html](https://kevinboone.me/efitest_index.html)

生成摘要时出错

---

## 7. 餐饮外卖支付侧录攻击活动

**原文标题**: Restaurant Delivery Payment-Skimming Campaign

**原文链接**: [https://www.infohawk.com/news/2026-11-05-scamwich-restaurant-skimming](https://www.infohawk.com/news/2026-11-05-scamwich-restaurant-skimming)

2026年11月，InfoHawk的研究人员揭露了一场大规模的支付信息窃取活动。该活动涉及820个可疑域名，模仿了包括Jimmy John’s、Jersey Mike’s、Chipotle和Firehouse Subs在内的35家美国主要连锁餐厅。

该行动采用了先进的“反向代理”技术。攻击者并非制作粗糙的仿制品，而是实时镜像合法网站的原始代码和界面。这使得欺诈网站的外观和行为与真实网站完全一致，且无需入侵餐厅的实际基础设施。

其主要目标是财务窃取。当客户尝试支付订单时，会看到一个恶意的结账表单。该表单会捕捉信用卡信息，并提示用户输入银行发送的短信验证码。通过同时获取卡片详情和一次性验证码，攻击者可以绕过安全协议，授权欺诈性交易。

该活动的关键细节包括：
*   **规模：** 已识别出820个域名，其中808个使用了 **.delivery** 顶级域名。
*   **主要目标：** Jimmy John’s 是受攻击最严重的品牌，关联的仿冒域名达404个。
*   **用户体验：** 这些网站与真实平台几乎难辨真伪，利用了消费者对在线订餐流程的熟悉程度。

这一活动凸显了一种不断演变的威胁：犯罪分子利用高仿真克隆网站在支付的关键时刻欺骗客户，使得即使是精通技术的用户也难以察觉此类欺诈。

---

## 8. Blender 的 UI 与运行时：远快于 GPUI

**原文标题**: Blender's UI and Runtime: Much Faster Than GPUI

**原文链接**: [https://github.com/ppmpreetham/BUI](https://github.com/ppmpreetham/BUI)

**BUI (Blender UI)** 是一款高性能、独立的 UI 库。它将 Blender 的界面与其 3D 软件解耦，允许开发者在自己的产品中使用其控件绘制和交互规则。该库采用轻量级 C 语言核心编写，为使用 Python、Rust、JavaScript (React/Svelte)、C 和 C++ 的开发者提供“Blender 式体验”——包括精准滑块、支持数学运算的输入框以及模糊搜索。

**核心亮点：**

*   **性能与效率：** BUI 旨在实现低能耗和低内存占用。它利用“局部重绘”（仅重新绘制更改区域）并提供可选的 GPU 渲染器。基准测试显示，其速度比 GPUI 快 2–4 倍，启动时间低于 100 毫秒，内存占用低至 19 MB。
*   **多语言灵活性：** 
    *   **Python：** 支持现有的 `tkinter` 和 `ttk` 代码、Qt 风格语法以及 45 个以上的原生 Blender 组件。
    *   **Rust & JavaScript：** 允许使用 HTML、CSS (Flexbox, Grid) 和 Tailwind 构建 UI，且无需浏览器引擎或 Webview。
    *   **Dear ImGui：** 为 ImGui 应用程序提供 Blender 主题皮肤和交互模型。
*   **丰富的功能特性：** 包含节点编辑器、拾色器和饼形菜单等原生 Blender 控件。它还具备先进的图像/视频处理能力（支持内存预算化缓存），并支持滤镜和动画等现代 CSS 特效。
*   **原生且轻量：** BUI 可生成小巧的独立可执行文件（6–7 MB），并支持 Windows (Win32)、Linux (X11/Wayland) 和 macOS 的原生窗口系统。

总之，BUI 为 Electron 或基于浏览器的框架提供了一个“精简”且快速的替代方案，让任何应用程序都能拥有 Blender 屡获殊荣的界面美学与高效体验。

---

## 9. Memorilla: Latent Semantic Memory for LLMs

**原文标题**: Memorilla: Latent Semantic Memory for LLMs

**原文链接**: [https://arxiv.org/abs/2610.21375](https://arxiv.org/abs/2610.21375)

生成摘要时出错

---

## 10. Replit 使用 microVM 重构了其沙箱引擎

**原文标题**: Replit rebuilt its sandbox engine with microVMs

**原文链接**: [https://frontier.replit.com/sandbox-engine-microvms-part-1/](https://frontier.replit.com/sandbox-engine-microvms-part-1/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-11-06](output/hacker_news_summary_2026-11-06.md) |
| 2 | [2026-11-05](output/hacker_news_summary_2026-11-05.md) |
| 3 | [2026-11-04](output/hacker_news_summary_2026-11-04.md) |
| 4 | [2026-10-29](output/hacker_news_summary_2026-10-29.md) |
| 5 | [2026-10-30](output/hacker_news_summary_2026-10-30.md) |
| 6 | [2026-11-03](output/hacker_news_summary_2026-11-03.md) |
| 7 | [2026-10-28](output/hacker_news_summary_2026-10-28.md) |
| 8 | [2026-10-31](output/hacker_news_summary_2026-10-31.md) |
| 9 | [2026-11-01](output/hacker_news_summary_2026-11-01.md) |
| 10 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 11 | [2026-10-22](output/hacker_news_summary_2026-10-22.md) |
| 12 | [2026-10-25](output/hacker_news_summary_2026-10-25.md) |
| 13 | [2026-10-27](output/hacker_news_summary_2026-10-27.md) |
| 14 | [2026-10-24](output/hacker_news_summary_2026-10-24.md) |
| 15 | [2026-10-26](output/hacker_news_summary_2026-10-26.md) |
| 16 | [2026-10-23](output/hacker_news_summary_2026-10-23.md) |
| 17 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 18 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 19 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 20 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 21 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 22 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 23 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 24 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 25 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 26 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 27 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 28 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 29 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 30 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 31 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 32 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 33 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 34 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 35 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 36 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 37 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 38 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 39 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 40 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 41 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 42 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 43 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 44 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 45 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 46 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 47 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 48 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 49 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 50 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 51 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 52 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 53 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 54 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 55 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 56 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 57 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 58 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 59 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 60 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 61 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 62 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 63 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 64 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 65 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 66 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 67 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 68 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 69 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 70 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 71 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 72 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 73 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 74 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 75 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 76 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 77 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 78 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 79 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 80 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 81 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 82 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 83 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 84 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 85 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 86 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 87 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 88 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 89 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 90 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 91 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 92 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 93 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 94 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 95 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 96 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 97 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 98 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 99 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 100 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 101 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 102 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 103 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 104 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 105 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 106 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 107 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 108 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 109 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 110 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 111 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 112 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 113 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 114 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 115 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 116 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 117 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 118 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 119 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 120 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 121 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 122 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 123 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 124 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 125 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 126 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 127 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 128 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 129 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 130 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 131 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 132 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 133 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 134 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 135 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 136 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 137 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 138 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 139 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 140 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 141 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 142 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 143 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 144 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 145 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 146 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 147 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 148 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 149 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 150 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 151 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 152 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 153 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 154 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 155 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 156 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 157 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 158 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 159 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 160 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 161 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 162 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 163 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 164 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 165 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 166 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 167 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 168 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 169 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 170 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 171 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 172 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 173 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 174 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 175 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 176 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 177 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 178 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 179 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 180 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 181 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 182 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 183 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 184 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 185 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 186 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 187 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 188 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 189 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 190 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 191 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 192 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 193 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 194 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 195 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 196 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 197 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 198 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 199 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 200 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 201 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 202 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 203 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 204 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 205 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 206 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 207 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 208 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 209 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 210 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 211 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 212 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 213 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 214 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 215 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 216 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 217 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 218 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 219 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 220 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 221 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 222 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 223 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 224 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 225 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 226 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 227 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 228 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 229 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 230 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 231 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 232 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 233 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 234 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 235 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 236 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 237 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 238 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 239 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 240 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 241 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 242 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 243 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 244 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 245 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 246 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 247 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 248 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 249 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 250 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 251 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 252 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 253 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 254 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 255 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 256 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 257 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 258 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 259 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 260 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 261 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 262 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 263 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 264 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 265 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 266 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 267 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 268 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 269 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 270 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 271 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 272 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 273 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 274 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 275 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 276 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 277 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 278 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 279 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 280 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 281 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 282 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 283 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 284 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 285 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 286 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 287 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 288 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 289 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 290 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 291 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 292 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 293 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 294 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 295 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 296 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 297 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 298 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 299 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 300 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 301 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 302 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 303 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 304 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 305 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 306 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 307 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 308 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 309 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 310 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 311 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 312 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 313 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 314 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 315 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 316 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 317 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 318 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 319 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 320 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 321 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 322 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 323 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 324 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 325 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 326 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 327 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 328 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 329 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 330 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 331 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 332 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 333 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 334 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 335 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 336 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 337 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 338 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 339 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 340 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 341 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 342 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 343 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 344 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 345 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 346 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 347 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 348 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 349 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 350 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 351 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 352 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 353 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 354 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 355 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 356 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 357 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 358 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 359 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 360 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 361 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 362 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 363 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 364 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 365 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 366 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 367 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 368 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 369 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 370 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 371 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 372 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 373 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 374 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 375 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 376 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 377 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 378 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 379 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 380 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 381 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 382 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 383 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 384 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 385 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 386 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 387 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 388 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 389 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 390 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 391 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 392 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 393 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 394 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 395 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 396 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 397 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 398 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 399 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 400 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 401 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 402 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 403 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 404 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 405 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 406 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 407 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 408 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 409 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 410 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 411 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 412 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 413 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 414 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 415 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 416 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 417 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 418 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 419 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 420 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 421 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 422 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 423 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 424 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 425 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 426 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 427 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 428 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 429 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 430 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 431 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 432 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 433 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 434 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 435 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 436 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 437 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 438 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 439 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 440 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 441 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 442 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 443 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 444 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 445 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 446 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 447 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 448 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 449 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 450 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 451 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 452 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 453 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 454 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 455 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 456 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 457 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 458 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 459 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 460 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 461 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 462 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 463 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 464 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 465 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 466 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 467 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 468 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 469 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 470 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 471 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 472 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 473 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 474 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 475 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 476 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 477 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 478 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 479 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 480 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 481 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 482 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 483 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 484 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 485 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 486 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 487 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 488 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 489 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 490 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 491 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 492 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 493 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 494 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 495 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 496 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 497 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 498 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 499 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 500 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 501 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 502 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 503 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 504 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 505 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 506 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 507 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 508 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 509 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 510 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 511 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 512 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 513 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 514 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 515 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 516 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 517 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 518 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 519 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 520 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 521 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 522 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 523 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 524 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 525 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 526 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 527 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 528 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 529 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 530 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 531 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 532 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 533 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 534 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 535 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 536 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 537 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 538 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 539 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 540 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 541 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 542 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 543 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 544 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 545 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 546 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 547 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 548 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 549 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 550 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 551 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 552 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 553 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 554 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 555 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 556 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 557 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 558 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 559 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 560 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 561 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 562 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 563 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 564 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 565 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 566 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 567 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 568 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 569 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 570 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 571 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 572 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 573 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 574 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 575 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 576 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 577 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 578 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 579 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 580 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 581 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 582 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 583 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 584 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 585 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 586 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 587 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 588 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 589 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 590 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 591 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 592 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 593 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
