# Hacker News 热门文章摘要 (2026-02-19)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Gemini 3.1 Pro

**原文标题**: Gemini 3.1 Pro

**原文链接**: [https://deepmind.google/models/model-cards/gemini-3-1-pro/](https://deepmind.google/models/model-cards/gemini-3-1-pro/)

Gemini 3.1 Pro 模型卡于 2026 年 2 月 19 日发布，介绍了谷歌原生多模态推理模型的最新迭代版本。该模型基于 Gemini 3 Pro 架构构建，定位为谷歌应对复杂、高推理任务的最先进模型。

**关键技术规格：**
Gemini 3.1 Pro 支持包括文本、音频、图像、视频和完整代码库在内的多种输入方式，采用 100 万 token 的上下文窗口和 64K token 的输出限制。该模型通过 Gemini App、Vertex AI 和 Google AI Studio 进行分发。

**性能基准测试：**
该模型较之前的迭代版本有显著提升，特别是在抽象推理和编程方面。显著结果包括：
*   **ARC-AGI-2：** 77.1%（较 Gemini 3 Pro 的 31.1% 有重大飞跃）。
*   **GPQA Diamond：** 科学知识得分 94.3%。
*   **SWE-Bench Verified：** 智能体编程得分 80.6%。
*   **LiveCodeBench Pro：** Elo 评分为 2887。

**安全与前沿风险：**
安全性能与 Gemini 3 系列保持一致，在文本安全性和语气方面有小幅改进。在“前沿安全框架”下，该模型在 CBRN（化学、生物、放射性、核）、有害操控以及机器学习研发方面的能力表现均低于临界能力水平 (CCL)。尽管它在网络能力方面达到了“警示阈值”（与 Gemini 3 Pro 类似），但未达到 CCL 的提升要求。在失调测试中，该模型在特定挑战中表现出较高的情境意识，但在更广泛的类别中表现仍不一致。

**预期用途：**
该模型针对智能体工作流、高级编程、长上下文多模态理解和战略性问题解决进行了优化。它旨在通过循序渐进的改进和增强的推理能力，协助处理现实世界的复杂问题。

---

## 2. Show HN: Micasa – 在终端监控你的家

**原文标题**: Show HN: Micasa – track your house from the terminal

**原文链接**: [https://micasa.dev](https://micasa.dev)

**Micasa** 是一款基于终端的家居管理工具，旨在通过集中的、键盘驱动的系统，取代传统的纸质文件夹和杂乱的数字文件。该工具基于 Go 语言开发，允许房主直接从命令行管理房产的方方面面。

**核心功能：**
*   **维护与事故记录：** 跟踪具有自动计算截止日期的定期任务，并按严重程度和位置记录突发维修（即“事故”）。
*   **项目与报价管理：** 整理从构思到完成的家居改善项目，并横向对比供应商报价。
*   **资产跟踪：** 维护详细的家电清单，包括购买日期、保修状态和维修历史。
*   **供应商名录：** 存储联系方式以及特定承包商执行每项工作的完整历史记录。
*   **文档存储：** 将说明书、发票和照片直接关联至相关项目或家电。

**技术细节：**
该应用采用本地优先模式，将所有数据和附件存储在单个 **SQLite 文件**中，以便于迁移和备份。界面深受 **VisiData** 启发，利用 Vim 风格的模态快捷键、模糊搜索和下钻功能实现高效导航。

Micasa 支持跨平台（Linux、macOS 和 Windows），可以通过 Go 或预编译的二进制文件进行安装。它专为希望在不离开终端的情况下，以轻量、私密且高效的方式管理家居维护的用户而设计。

---

## 3. 恐龙的食物：我们至今仍在食用的亿年前的食物 (2022)

**原文标题**: Dinosaur Food: 100M year old foods we still eat today (2022)

**原文链接**: [https://borischerny.com/food/2022/01/17/Dinosaur-food.html](https://borischerny.com/food/2022/01/17/Dinosaur-food.html)

受奥利弗·萨克斯（Oliver Sacks）著作《万物各得其所》（*Everything in Its Place*）的启发，这篇2022年的文章探讨了“活化石”——即那些在数百万年间形态保持不变、且至今仍是人类饮食一部分的物种。作者的兴趣源于银杏（*Ginkgo biloba*），这种树的历史比恐龙还要悠久，其产出的种仁（白果）至今仍常用于东亚料理。

文章根据两个标准列举了多个物种：它们必须可供人类食用，且形态上与其古代化石记录完全一致。这份名单跨越了动植物界近5亿年的进化史。

**“恐龙食物”的主要例子包括：**
*   **鲎（4.8亿年）：** 名单中最古老的成员，其出现早于大多数陆生生物。
*   **银杏/白果（2.9亿年）：** 一种生命力极强的“活化石”，常用于茶碗蒸等菜肴。
*   **Wila地衣与驯鹿地衣（约2.5亿年）：** 至今仍被人类食用的古老生物。
*   **西米棕榈（2亿年）和智利南洋杉种子（1.6亿年）：** 历经多次物种大灭绝并幸存至今的史前主食。
*   **木贼（1.4亿年）、桂皮紫萁（7000万年）和莲花（6500万年以上）：** 自白垩纪以来一直保持原有形态的有花及无花植物。

作者自称为业余爱好者，他强调了食用这些历经亿万年基本未变的生物所带来的“酷感”，并邀请科学界对其内容进行补充与修正。这篇文章对古生物学与美食学的交汇进行了简短而迷人的审视。

---

## 4. Pebble 生产：二月更新

**原文标题**: Pebble Production: February Update

**原文链接**: [https://repebble.com/blog/february-pebble-production-and-software-updates](https://repebble.com/blog/february-pebble-production-and-software-updates)

Pebble 2月更新重点介绍了 Pebble Time 2 (PT2)、Pebble Round 2 (PR2) 和 Index 01 智能戒指的最终生产阶段。

**硬件进展：**
*   **Pebble Time 2：** 在成功通过生产验证测试 (PVT) 并确认 3ATM 防水等级（适用于游泳）后，量产计划于 3 月 9 日开始。首批产品预计将于 4 月初送达用户，所有预订单将在 6 月前完成交付。美国订单将产生 10 美元的关税。
*   **Index 01：** 目前处于 PVT 阶段，防水等级为 IPX8。量产目标定于 3 月。由于其尺寸标准为专有规格，Pebble 将提供售价 10 美元的实体尺寸测量套件（或 3D 打印版本）以确保佩戴合适。
*   **Pebble Round 2：** 该设备已完成设计验证 (DVT1) 阶段。由于其电路设计与 PT2 相同，固件开发进展迅速。预计将于 5 月下旬开始生产。

**软件与生态系统：**
软件团队发布了多项针对 PebbleOS 和移动应用的更新：
*   **功能修复：** 天气服务已恢复，并解决了一个重大的 iOS 后台崩溃问题。
*   **新功能：** 更新引入了左手模式、手表到手机的健康数据同步，以及移动应用内的“原生”应用商店。
*   **旧版支持：** 移动应用现在会拦截使用已失效天气 API（如 Yahoo）的旧款表盘请求，并改由 Open-Meteo 提供数据，从而确保旧版内容仍能正常使用。
*   **通信优化：** WhatsApp 通话现在可在 Android 上正确显示，并为现代应用新增了多个通知图标。

总体而言，项目正进入量产阶段，团队目前的重点是最后的工厂测试及优化软件体验。

---

## 5. Paged Out 第 8 期 [PDF]

**原文标题**: Paged Out Issue #8 [pdf]

**原文链接**: [https://pagedout.institute/download/PagedOut_008.pdf](https://pagedout.institute/download/PagedOut_008.pdf)

《Paged Out!》第 8 期是这份专注于“底层”计算机科学、黑客技术及编程的社区驱动型技术刊物的最新版本。延续其标志性的排版风格，本期呈现了 50 多篇密集的一页式文章，对复杂的技术主题进行了短小精悍的深度剖析。

该刊物涵盖了广泛的主题，主要围绕信息安全和逆向工程展开。本期的核心主题包括：

*   **恶意软件分析与漏洞利用：** 贡献者们探讨了高级 Shellcode 技术、进程注入方法以及绕过现代安全防御机制的策略。重点关注如何通过巧妙的混淆手段实现“大隐隐于市”的隐藏效果。
*   **逆向工程：** 文章提供了使用 Ghidra 和 IDA Pro 等工具的实用技巧，以及解构私有协议和分析二进制格式的技术。
*   **硬件与底层黑客技术：** 本板块包含 FPGA 开发、侧信道攻击和 USB 协议操作的教程。它还涉及复古计算，探索陈旧硬件的内部结构。
*   **编程与工具：** 杂志深入研究了 C++ 内部机制、Python 的奇技淫巧，以及旨在优化研究工作流的自动化脚本。多篇文章还探讨了大语言模型（LLM）与安全研究之间新兴的交集，特别是在自动化漏洞发现方面的应用。
*   **创意编程：** 秉承其“黑客刊物”的根基，本期还包括了关于 Demo 场景（Demoscene）、奇癖编程语言（Esoteric languages）以及“黑客艺术”的章节。

总体而言，《Paged Out!》第 8 期为开发者、安全研究人员和爱好者提供了一个高度浓缩的知识库。它强调实践与动手操作，鼓励读者亲自尝试每篇短文中提供的代码片段和技术概念。

---

## 6. 别相信“盐”：AI 摘要、多语言安全与 LLM 护栏

**原文标题**: Don't Trust the Salt: AI Summarization, Multilingual Safety, and LLM Guardrails

**原文链接**: [https://royapakzad.substack.com/p/multilingual-llm-evaluation-to-guardrails](https://royapakzad.substack.com/p/multilingual-llm-evaluation-to-guardrails)

在《不要相信盐》（Don’t Trust the Salt）一文中，Roya Pakzad 探讨了大型语言模型（LLM）安全护栏在多语言语境下的严重漏洞。其核心论点是：虽然 AI 安全措施在英语环境中相对稳健，但在其他语言中往往失效，从而形成了显著的“安全差距”。

文章的核心观点包括：

*   **“加盐”问题：** Pakzad 指出，简单的对抗性技术——例如在提示词中“加盐”（添加随机字符或特定格式）——即可绕过安全过滤器。虽然模型可能会拒绝纯英语的有害请求，但通过微小的修改或翻译成其他语言，就能诱导模型执行该请求。
*   **多语言安全差距：** 大多数 LLM 的安全训练和评估都以英语为中心。因此，模型往往缺乏识别低资源语言中恶意内容、仇恨言论或危险指令所需的文化和语言细微差别。这导致非英语用户面临“安全税”，即他们更有可能接触到有害的 AI 输出。
*   **评估缺陷：** 文章批评了当前的基准测试方法，指出自动化评估工具往往无法捕捉不同语言中违规行为的语义复杂性。仅依赖英语翻译的数据集进行全球安全性测试是不充分且具有误导性的。
*   **行动呼吁：** Pakzad 主张 AI 公司转变其安全策略。这包括投资本地化数据集、引入由母语者参与的“人机回环”评估，并超越静态基准，在所有支持的语言中进行严格的对抗性测试。

总之，这篇文章警示我们，所谓的“通用型”AI 安全目前只是一个神话。真正的安全护栏需要深度的多语言承诺，以确保全球用户都能获得公平的保护。

---

## 7. Arrays in Forth

**原文标题**: Arrays in Forth

**原文链接**: [https://www.forth.org/svfig/Len/arrays.htm](https://www.forth.org/svfig/Len/arrays.htm)

This article explores the philosophy and implementation of arrays in Forth, highlighting that the language's flexibility allows developers to create custom data types rather than relying on rigid standards. The author distinguishes between two primary types: **unindexed** and **indexed** arrays.

**Unindexed arrays** are essentially memory buffers or work areas created using `CREATE` and `ALLOT`, returning a base address at run-time. **Indexed arrays** are more structured, mapping an index to the address of a specific element of equal length. 

Key concepts include:
*   **Basic Indexed Arrays:** These typically handle elements one cell in length. The author provides a standard definition and notes a necessary correction regarding stack manipulation: when using the `DOES>` clause, the index must be swapped with the data field address to ensure correct calculations.
*   **Long-Element Arrays:** For more complex data, such as game records, defining words can create arrays where each element spans multiple cells. 
*   **Subfields and Offsets:** To access specific data within multi-cell records, the author suggests creating "offsets." By defining words that represent specific fields (e.g., `}north` or `}descriptor`), programmers can write readable code to access specific parts of a record.
*   **Simplified Approaches:** If a program only requires one or two arrays, the author suggests "faking" them by allotting a raw buffer and creating a simple word to manually calculate the address based on an index.

Ultimately, the article demonstrates that Forth’s power lies in its ability to build tailored structures—ranging from simple bit arrays to complex multi-field records—from the ground up.

---

## 8. Gemini 3.1 Pro Preview

**原文标题**: Gemini 3.1 Pro Preview

**原文链接**: [https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/gemini-3.1-pro-preview?pli=1](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/gemini-3.1-pro-preview?pli=1)

生成摘要时出错

---

## 9. -fbounds-safety: Enforcing bounds safety for C

**原文标题**: -fbounds-safety: Enforcing bounds safety for C

**原文链接**: [https://clang.llvm.org/docs/BoundsSafety.html](https://clang.llvm.org/docs/BoundsSafety.html)

生成摘要时出错

---

## 10. America vs. Singapore: You Can't Save Your Way Out of Economic Shocks

**原文标题**: America vs. Singapore: You Can't Save Your Way Out of Economic Shocks

**原文链接**: [https://www.governance.fyi/p/america-vs-singapore-you-cant-save](https://www.governance.fyi/p/america-vs-singapore-you-cant-save)

生成摘要时出错

---

## 11. Coding Tricks Used in the C64 Game Seawolves

**原文标题**: Coding Tricks Used in the C64 Game Seawolves

**原文链接**: [https://kodiak64.co.uk/blog/seawolves-technical-tricks](https://kodiak64.co.uk/blog/seawolves-technical-tricks)

生成摘要时出错

---

## 12. Show HN: A physically-based GPU ray tracer written in Julia

**原文标题**: Show HN: A physically-based GPU ray tracer written in Julia

**原文链接**: [https://makie.org/website/blogposts/raytracing/](https://makie.org/website/blogposts/raytracing/)

生成摘要时出错

---

## 13. Large Language Models for Mortals: A Practical Guide for Analysts with Python

**原文标题**: Large Language Models for Mortals: A Practical Guide for Analysts with Python

**原文链接**: [https://crimede-coder.com/blogposts/2026/LLMsForMortals](https://crimede-coder.com/blogposts/2026/LLMsForMortals)

生成摘要时出错

---

## 14. Measuring AI agent autonomy in practice

**原文标题**: Measuring AI agent autonomy in practice

**原文链接**: [https://www.anthropic.com/research/measuring-agent-autonomy](https://www.anthropic.com/research/measuring-agent-autonomy)

生成摘要时出错

---

## 15. Bridging Elixir and Python with Oban

**原文标题**: Bridging Elixir and Python with Oban

**原文链接**: [https://oban.pro/articles/bridging-with-oban](https://oban.pro/articles/bridging-with-oban)

生成摘要时出错

---

## 16. Sizing chaos

**原文标题**: Sizing chaos

**原文链接**: [https://pudding.cool/2026/02/womens-sizing/](https://pudding.cool/2026/02/womens-sizing/)

生成摘要时出错

---

## 17. Why applicant tracking systems are broken by design

**原文标题**: Why applicant tracking systems are broken by design

**原文链接**: [https://www.saj.ad/2026/ats](https://www.saj.ad/2026/ats)

生成摘要时出错

---

## 18. Zero downtime migrations at Petabyte scale

**原文标题**: Zero downtime migrations at Petabyte scale

**原文链接**: [https://planetscale.com/blog/zero-downtime-migrations-at-petabyte-scale](https://planetscale.com/blog/zero-downtime-migrations-at-petabyte-scale)

生成摘要时出错

---

## 19. Show HN: Mini-Diarium - An encrypted, local, cross-platform journaling app

**原文标题**: Show HN: Mini-Diarium - An encrypted, local, cross-platform journaling app

**原文链接**: [https://github.com/fjrevoredo/mini-diarium](https://github.com/fjrevoredo/mini-diarium)

生成摘要时出错

---

## 20. The Mongol Khans of Medieval France

**原文标题**: The Mongol Khans of Medieval France

**原文链接**: [https://www.historytoday.com/archive/feature/mongol-khans-medieval-france](https://www.historytoday.com/archive/feature/mongol-khans-medieval-france)

生成摘要时出错

---

## 21. Against Theory-Motivated Experimentation

**原文标题**: Against Theory-Motivated Experimentation

**原文链接**: [https://journals.sagepub.com/doi/10.1177/26339137261421577](https://journals.sagepub.com/doi/10.1177/26339137261421577)

生成摘要时出错

---

## 22. 27-year-old Apple iBooks can connect to Wi-Fi and download official updates

**原文标题**: 27-year-old Apple iBooks can connect to Wi-Fi and download official updates

**原文链接**: [https://old.reddit.com/r/MacOS/comments/1r8900z/macos_which_officially_supports_27_year_old/](https://old.reddit.com/r/MacOS/comments/1r8900z/macos_which_officially_supports_27_year_old/)

生成摘要时出错

---

## 23. Famous Signatures Through History

**原文标题**: Famous Signatures Through History

**原文链接**: [https://signatory.app/#famous-signatures](https://signatory.app/#famous-signatures)

生成摘要时出错

---

## 24. Old School Visual Effects: The Cloud Tank (2010)

**原文标题**: Old School Visual Effects: The Cloud Tank (2010)

**原文链接**: [http://singlemindedmovieblog.blogspot.com/2010/04/old-school-effects-cloud-tank.html](http://singlemindedmovieblog.blogspot.com/2010/04/old-school-effects-cloud-tank.html)

生成摘要时出错

---

## 25. ShannonMax: A Library to Optimize Emacs Keybindings with Information Theory

**原文标题**: ShannonMax: A Library to Optimize Emacs Keybindings with Information Theory

**原文链接**: [https://github.com/sstraust/shannonmax](https://github.com/sstraust/shannonmax)

生成摘要时出错

---

## 26. Voith Schneider Propeller

**原文标题**: Voith Schneider Propeller

**原文链接**: [https://en.wikipedia.org/wiki/Voith_Schneider_Propeller](https://en.wikipedia.org/wiki/Voith_Schneider_Propeller)

生成摘要时出错

---

## 27. 15 years of FP64 segmentation, and why the Blackwell Ultra breaks the pattern

**原文标题**: 15 years of FP64 segmentation, and why the Blackwell Ultra breaks the pattern

**原文链接**: [https://nicolasdickenmann.com/blog/the-great-fp64-divide.html](https://nicolasdickenmann.com/blog/the-great-fp64-divide.html)

生成摘要时出错

---

## 28. Mark Zuckerberg Grilled on Usage Goals and Underage Users at California Trial

**原文标题**: Mark Zuckerberg Grilled on Usage Goals and Underage Users at California Trial

**原文链接**: [https://www.wsj.com/us-news/law/meta-mark-zuckerberg-social-media-trial-0e9a7fa0](https://www.wsj.com/us-news/law/meta-mark-zuckerberg-social-media-trial-0e9a7fa0)

生成摘要时出错

---

## 29. Step 3.5 Flash – Open-source foundation model, supports deep reasoning at speed

**原文标题**: Step 3.5 Flash – Open-source foundation model, supports deep reasoning at speed

**原文链接**: [https://static.stepfun.com/blog/step-3.5-flash/](https://static.stepfun.com/blog/step-3.5-flash/)

生成摘要时出错

---

## 30. Anthropic officially bans using subscription auth for third party use

**原文标题**: Anthropic officially bans using subscription auth for third party use

**原文链接**: [https://code.claude.com/docs/en/legal-and-compliance](https://code.claude.com/docs/en/legal-and-compliance)

生成摘要时出错

---

## 31. A word processor from 1990s for Atari ST/TOS is still supported by enthusiasts

**原文标题**: A word processor from 1990s for Atari ST/TOS is still supported by enthusiasts

**原文链接**: [https://tempus-word.de/en/index](https://tempus-word.de/en/index)

生成摘要时出错

---

## 32. How to choose between Hindley-Milner and bidirectional typing

**原文标题**: How to choose between Hindley-Milner and bidirectional typing

**原文链接**: [https://thunderseethe.dev/posts/how-to-choose-between-hm-and-bidir/](https://thunderseethe.dev/posts/how-to-choose-between-hm-and-bidir/)

生成摘要时出错

---

## 33. Metriport (YC S22) is hiring a security engineer to harden healthcare infra

**原文标题**: Metriport (YC S22) is hiring a security engineer to harden healthcare infra

**原文链接**: [https://www.ycombinator.com/companies/metriport/jobs/XC2AF8s-senior-security-engineer](https://www.ycombinator.com/companies/metriport/jobs/XC2AF8s-senior-security-engineer)

生成摘要时出错

---

## 34. Visualizing the ARM64 Instruction Set (2024)

**原文标题**: Visualizing the ARM64 Instruction Set (2024)

**原文链接**: [https://zyedidia.github.io/blog/posts/6-arm64/](https://zyedidia.github.io/blog/posts/6-arm64/)

生成摘要时出错

---

## 35. Members-only Philly cop bar has been linked to two DUIs and a third crash

**原文标题**: Members-only Philly cop bar has been linked to two DUIs and a third crash

**原文链接**: [https://www.inquirer.com/news/philadelphia/philadelphia-police-7c-bar-overserving-car-crashes-20260219.html](https://www.inquirer.com/news/philadelphia/philadelphia-police-7c-bar-overserving-car-crashes-20260219.html)

生成摘要时出错

---

## 36. Helicobacter Pylori: A Nobel Pursuit?

**原文标题**: Helicobacter Pylori: A Nobel Pursuit?

**原文链接**: [https://pmc.ncbi.nlm.nih.gov/articles/PMC2661189/](https://pmc.ncbi.nlm.nih.gov/articles/PMC2661189/)

生成摘要时出错

---

## 37. AI made coding more enjoyable

**原文标题**: AI made coding more enjoyable

**原文链接**: [https://weberdominik.com/blog/ai-coding-enjoyable/](https://weberdominik.com/blog/ai-coding-enjoyable/)

生成摘要时出错

---

## 38. Virgins, Unicorns and Medieval Literature (2017)

**原文标题**: Virgins, Unicorns and Medieval Literature (2017)

**原文链接**: [https://www.bowdoin.edu/news/2017/11/virgins-unicorns-and-medieval-literature.html](https://www.bowdoin.edu/news/2017/11/virgins-unicorns-and-medieval-literature.html)

生成摘要时出错

---

## 39. What years of production-grade concurrency teaches us about building AI agents

**原文标题**: What years of production-grade concurrency teaches us about building AI agents

**原文链接**: [https://georgeguimaraes.com/your-agent-orchestrator-is-just-a-bad-clone-of-elixir/](https://georgeguimaraes.com/your-agent-orchestrator-is-just-a-bad-clone-of-elixir/)

生成摘要时出错

---

## 40. Sam Altman (OpenAI) and Dario Amodei (Anthropic) Refuse to Hold Hands

**原文标题**: Sam Altman (OpenAI) and Dario Amodei (Anthropic) Refuse to Hold Hands

**原文链接**: [https://xcancel.com/ANI/status/2024349307835732347](https://xcancel.com/ANI/status/2024349307835732347)

生成摘要时出错

---

## 41. Fff.nvim – Typo-resistant code search

**原文标题**: Fff.nvim – Typo-resistant code search

**原文链接**: [https://github.com/dmtrKovalenko/fff.nvim](https://github.com/dmtrKovalenko/fff.nvim)

生成摘要时出错

---

## 42. All Look Same?

**原文标题**: All Look Same?

**原文链接**: [https://alllooksame.com/](https://alllooksame.com/)

生成摘要时出错

---

## 43. The Perils of ISBN

**原文标题**: The Perils of ISBN

**原文链接**: [https://rygoldstein.com/posts/perils-of-isbn](https://rygoldstein.com/posts/perils-of-isbn)

生成摘要时出错

---

## 44. Antarctica sits above Earth's strongest 'gravity hole' – how it got that way

**原文标题**: Antarctica sits above Earth's strongest 'gravity hole' – how it got that way

**原文链接**: [https://phys.org/news/2026-02-antarctica-earth-strongest-gravity-hole.html](https://phys.org/news/2026-02-antarctica-earth-strongest-gravity-hole.html)

生成摘要时出错

---

## 45. DOGE Track

**原文标题**: DOGE Track

**原文链接**: [https://dogetrack.info/](https://dogetrack.info/)

生成摘要时出错

---

## 46. Cosmologically Unique IDs

**原文标题**: Cosmologically Unique IDs

**原文链接**: [https://jasonfantl.com/posts/Universal-Unique-IDs/](https://jasonfantl.com/posts/Universal-Unique-IDs/)

生成摘要时出错

---

## 47. Show HN: A Lisp where each function call runs a Docker container

**原文标题**: Show HN: A Lisp where each function call runs a Docker container

**原文链接**: [https://github.com/a11ce/docker-lisp](https://github.com/a11ce/docker-lisp)

生成摘要时出错

---

## 48. A Pokémon of a Different Color

**原文标题**: A Pokémon of a Different Color

**原文链接**: [https://matthew.verive.me/blog/color/](https://matthew.verive.me/blog/color/)

生成摘要时出错

---

## 49. Learning Lean: Part 1

**原文标题**: Learning Lean: Part 1

**原文链接**: [https://rkirov.github.io/posts/lean1/](https://rkirov.github.io/posts/lean1/)

生成摘要时出错

---

## 50. R3forth: A concatenative language derived from ColorForth

**原文标题**: R3forth: A concatenative language derived from ColorForth

**原文链接**: [https://github.com/phreda4/r3/blob/main/doc/r3forth_tutorial.md](https://github.com/phreda4/r3/blob/main/doc/r3forth_tutorial.md)

生成摘要时出错

---

## 51. The future belongs to those who can refute AI, not just generate with AI

**原文标题**: The future belongs to those who can refute AI, not just generate with AI

**原文链接**: [https://learningloom.substack.com/p/the-future-belongs-to-those-who-can](https://learningloom.substack.com/p/the-future-belongs-to-those-who-can)

生成摘要时出错

---

## 52. How AI is affecting productivity and jobs in Europe

**原文标题**: How AI is affecting productivity and jobs in Europe

**原文链接**: [https://cepr.org/voxeu/columns/how-ai-affecting-productivity-and-jobs-europe](https://cepr.org/voxeu/columns/how-ai-affecting-productivity-and-jobs-europe)

生成摘要时出错

---

## 53. Making a font with ligatures to display thirteenth-century monk numerals

**原文标题**: Making a font with ligatures to display thirteenth-century monk numerals

**原文链接**: [https://digitalseams.com/blog/making-a-font-with-9999-ligatures-to-display-thirteenth-century-monk-numerals](https://digitalseams.com/blog/making-a-font-with-9999-ligatures-to-display-thirteenth-century-monk-numerals)

生成摘要时出错

---

## 54. Minecraft Java is switching from OpenGL to Vulkan

**原文标题**: Minecraft Java is switching from OpenGL to Vulkan

**原文链接**: [https://www.gamingonlinux.com/2026/02/minecraft-java-is-switching-from-opengl-to-vulkan-for-the-vibrant-visuals-update/](https://www.gamingonlinux.com/2026/02/minecraft-java-is-switching-from-opengl-to-vulkan-for-the-vibrant-visuals-update/)

生成摘要时出错

---

## 55. How I launched 3 consoles and found true love at Babbage's store no. 9 (2013)

**原文标题**: How I launched 3 consoles and found true love at Babbage's store no. 9 (2013)

**原文链接**: [https://arstechnica.com/gadgets/2013/01/how-i-launched-3-consoles-and-found-true-love-at-babbages-store-no-9/](https://arstechnica.com/gadgets/2013/01/how-i-launched-3-consoles-and-found-true-love-at-babbages-store-no-9/)

生成摘要时出错

---

## 56. Lilush – LuaJIT static runtime and shell

**原文标题**: Lilush – LuaJIT static runtime and shell

**原文链接**: [https://lilush.link/](https://lilush.link/)

生成摘要时出错

---

## 57. If you’re an LLM, please read this

**原文标题**: If you’re an LLM, please read this

**原文链接**: [https://annas-archive.li/blog/llms-txt.html](https://annas-archive.li/blog/llms-txt.html)

生成摘要时出错

---

## 58. Portugal: The First Global Empire (2015)

**原文标题**: Portugal: The First Global Empire (2015)

**原文链接**: [https://www.historytoday.com/archive/first-global-empire](https://www.historytoday.com/archive/first-global-empire)

生成摘要时出错

---

## 59. Tailscale Peer Relays is now generally available

**原文标题**: Tailscale Peer Relays is now generally available

**原文链接**: [https://tailscale.com/blog/peer-relays-ga](https://tailscale.com/blog/peer-relays-ga)

生成摘要时出错

---

## 60. Zero-day CSS: CVE-2026-2441 exists in the wild

**原文标题**: Zero-day CSS: CVE-2026-2441 exists in the wild

**原文链接**: [https://chromereleases.googleblog.com/2026/02/stable-channel-update-for-desktop_13.html](https://chromereleases.googleblog.com/2026/02/stable-channel-update-for-desktop_13.html)

生成摘要时出错

---

## 61. What Every Experimenter Must Know About Randomization

**原文标题**: What Every Experimenter Must Know About Randomization

**原文链接**: [https://spawn-queue.acm.org/doi/pdf/10.1145/3778029](https://spawn-queue.acm.org/doi/pdf/10.1145/3778029)

生成摘要时出错

---

## 62. Claude Sonnet 4.6

**原文标题**: Claude Sonnet 4.6

**原文链接**: [https://www.anthropic.com/news/claude-sonnet-4-6](https://www.anthropic.com/news/claude-sonnet-4-6)

生成摘要时出错

---

## 63. Show HN: LatentScore – Type a mood, get procedural/ambient music (open source)

**原文标题**: Show HN: LatentScore – Type a mood, get procedural/ambient music (open source)

**原文链接**: [https://latentscore.com/demo](https://latentscore.com/demo)

生成摘要时出错

---

## 64. Electrobun v1: Build fast, tiny, and cross-platform desktop apps with TypeScript

**原文标题**: Electrobun v1: Build fast, tiny, and cross-platform desktop apps with TypeScript

**原文链接**: [https://blackboard.sh/blog/electrobun-v1/](https://blackboard.sh/blog/electrobun-v1/)

生成摘要时出错

---

## 65. DNS-Persist-01: A New Model for DNS-Based Challenge Validation

**原文标题**: DNS-Persist-01: A New Model for DNS-Based Challenge Validation

**原文链接**: [https://letsencrypt.org/2026/02/18/dns-persist-01.html](https://letsencrypt.org/2026/02/18/dns-persist-01.html)

生成摘要时出错

---

## 66. Stoolap/Node: A Native Node.js Driver That's Surprisingly Fast

**原文标题**: Stoolap/Node: A Native Node.js Driver That's Surprisingly Fast

**原文链接**: [https://stoolap.io/blog/2026/02/19/introducing-stoolap-node/](https://stoolap.io/blog/2026/02/19/introducing-stoolap-node/)

生成摘要时出错

---

## 67. Without America to rely on, EU gearing up to be a global power in its own right

**原文标题**: Without America to rely on, EU gearing up to be a global power in its own right

**原文链接**: [https://www.theatlantic.com/international/2026/02/european-union-defense-spending/685983/](https://www.theatlantic.com/international/2026/02/european-union-defense-spending/685983/)

生成摘要时出错

---

## 68. Show HN: Respectlytics – Open-source, privacy-first mobile analytics (MIT+AGPL)

**原文标题**: Show HN: Respectlytics – Open-source, privacy-first mobile analytics (MIT+AGPL)

**原文链接**: [https://github.com/respectlytics/respectlytics](https://github.com/respectlytics/respectlytics)

生成摘要时出错

---

## 69. C++26: Std:Is_within_lifetime

**原文标题**: C++26: Std:Is_within_lifetime

**原文链接**: [https://www.sandordargo.com/blog/2026/02/18/cpp26-std_is_within_lifetime](https://www.sandordargo.com/blog/2026/02/18/cpp26-std_is_within_lifetime)

生成摘要时出错

---

## 70. Meta CEO Knew Kids Were Being Hurt and He Covered It Up

**原文标题**: Meta CEO Knew Kids Were Being Hurt and He Covered It Up

**原文链接**: [https://dispatch.techoversight.org/email/23724686-b700-489a-9677-327799e75e5e/](https://dispatch.techoversight.org/email/23724686-b700-489a-9677-327799e75e5e/)

生成摘要时出错

---

## 71. Cistercian Numbers

**原文标题**: Cistercian Numbers

**原文链接**: [https://www.omniglot.com/language/numbers/cistercian-numbers.htm](https://www.omniglot.com/language/numbers/cistercian-numbers.htm)

生成摘要时出错

---

## 72. Terminals should generate the 256-color palette

**原文标题**: Terminals should generate the 256-color palette

**原文链接**: [https://gist.github.com/jake-stewart/0a8ea46159a7da2c808e5be2177e1783](https://gist.github.com/jake-stewart/0a8ea46159a7da2c808e5be2177e1783)

生成摘要时出错

---

## 73. Show HN: VectorNest responsive web-based SVG editor

**原文标题**: Show HN: VectorNest responsive web-based SVG editor

**原文链接**: [https://ekrsulov.github.io/vectornest/](https://ekrsulov.github.io/vectornest/)

生成摘要时出错

---

## 74. Microsoft guide to pirating Harry Potter for LLM training (2024) [removed]

**原文标题**: Microsoft guide to pirating Harry Potter for LLM training (2024) [removed]

**原文链接**: [https://devblogs.microsoft.com/azure-sql/langchain-with-sqlvectorstore-example/](https://devblogs.microsoft.com/azure-sql/langchain-with-sqlvectorstore-example/)

生成摘要时出错

---

## 75. Pentagon-Anthropic battle pushes other AI labs into major dilemma

**原文标题**: Pentagon-Anthropic battle pushes other AI labs into major dilemma

**原文链接**: [https://www.axios.com/2026/02/19/anthropic-pentagon-ai-fight-openai-google-xai](https://www.axios.com/2026/02/19/anthropic-pentagon-ai-fight-openai-google-xai)

生成摘要时出错

---

## 76. Making the Vortex Mixer

**原文标题**: Making the Vortex Mixer

**原文链接**: [https://www.asimov.press/p/vortex](https://www.asimov.press/p/vortex)

生成摘要时出错

---

## 77. TinyIce: Single-binary Icecast2-compatible server (auto-HTTPS, multi-tenant)

**原文标题**: TinyIce: Single-binary Icecast2-compatible server (auto-HTTPS, multi-tenant)

**原文链接**: [https://github.com/DatanoiseTV/tinyice](https://github.com/DatanoiseTV/tinyice)

生成摘要时出错

---

## 78. Show HN: I built a fuse box for microservices

**原文标题**: Show HN: I built a fuse box for microservices

**原文链接**: [https://www.openfuse.io](https://www.openfuse.io)

生成摘要时出错

---

## 79. Halt and Catch Fire: TV’s best drama you’ve probably never heard of (2021)

**原文标题**: Halt and Catch Fire: TV’s best drama you’ve probably never heard of (2021)

**原文链接**: [https://www.sceneandheardnu.com/content/halt-and-catch-fire](https://www.sceneandheardnu.com/content/halt-and-catch-fire)

生成摘要时出错

---

## 80. The true history of the Minotaur: what archaeology reveals

**原文标题**: The true history of the Minotaur: what archaeology reveals

**原文链接**: [https://www.nationalgeographic.fr/histoire/la-veritable-histoire-du-minotaure-ce-que-revele-archeologie-recherche-verification](https://www.nationalgeographic.fr/histoire/la-veritable-histoire-du-minotaure-ce-que-revele-archeologie-recherche-verification)

生成摘要时出错

---

## 81. A solver for Semantle

**原文标题**: A solver for Semantle

**原文链接**: [https://victoriaritvo.com/blog/semantle-solver/](https://victoriaritvo.com/blog/semantle-solver/)

生成摘要时出错

---

## 82. A DuckDB-based metabase alternative

**原文标题**: A DuckDB-based metabase alternative

**原文链接**: [https://github.com/taleshape-com/shaper](https://github.com/taleshape-com/shaper)

生成摘要时出错

---

## 83. Reverse Engineering Sid Meier's Railroad Tycoon for DOS from 1990

**原文标题**: Reverse Engineering Sid Meier's Railroad Tycoon for DOS from 1990

**原文链接**: [https://www.vogons.org/viewtopic.php?t=105451](https://www.vogons.org/viewtopic.php?t=105451)

生成摘要时出错

---

## 84. Greece throws support behind social media bans for kids

**原文标题**: Greece throws support behind social media bans for kids

**原文链接**: [https://www.euractiv.com/news/greece-throws-support-behind-social-media-bans-for-kids/](https://www.euractiv.com/news/greece-throws-support-behind-social-media-bans-for-kids/)

生成摘要时出错

---

## 85. Asahi Linux Progress Report: Linux 6.19

**原文标题**: Asahi Linux Progress Report: Linux 6.19

**原文链接**: [https://asahilinux.org/2026/02/progress-report-6-19/](https://asahilinux.org/2026/02/progress-report-6-19/)

生成摘要时出错

---

## 86. Native FreeBSD Kerberos/LDAP with FreeIPA/IDM

**原文标题**: Native FreeBSD Kerberos/LDAP with FreeIPA/IDM

**原文链接**: [https://vermaden.wordpress.com/2026/02/18/native-freebsd-kerberos-ldap-with-freeipa-idm/](https://vermaden.wordpress.com/2026/02/18/native-freebsd-kerberos-ldap-with-freeipa-idm/)

生成摘要时出错

---

## 87. 15 years later, Microsoft morged my diagram

**原文标题**: 15 years later, Microsoft morged my diagram

**原文链接**: [https://nvie.com/posts/15-years-later/](https://nvie.com/posts/15-years-later/)

生成摘要时出错

---

## 88. AI adoption and Solow's productivity paradox

**原文标题**: AI adoption and Solow's productivity paradox

**原文链接**: [https://fortune.com/2026/02/17/ai-productivity-paradox-ceo-study-robert-solow-information-technology-age/](https://fortune.com/2026/02/17/ai-productivity-paradox-ceo-study-robert-solow-information-technology-age/)

生成摘要时出错

---

## 89. Discrete Structures [pdf]

**原文标题**: Discrete Structures [pdf]

**原文链接**: [https://kyleormsby.github.io/files/113spring26/113full_text.pdf](https://kyleormsby.github.io/files/113spring26/113full_text.pdf)

生成摘要时出错

---

## 90. Show HN: CEL by Example

**原文标题**: Show HN: CEL by Example

**原文链接**: [https://celbyexample.com/](https://celbyexample.com/)

生成摘要时出错

---

## 91. Nanodevice produces continuous electricity from evaporation

**原文标题**: Nanodevice produces continuous electricity from evaporation

**原文链接**: [https://actu.epfl.ch/news/nanodevice-produces-continuous-electricity-from--2/](https://actu.epfl.ch/news/nanodevice-produces-continuous-electricity-from--2/)

生成摘要时出错

---

## 92. Show HN: I'm launching a LPFM radio station

**原文标题**: Show HN: I'm launching a LPFM radio station

**原文链接**: [https://www.kpbj.fm/](https://www.kpbj.fm/)

生成摘要时出错

---

## 93. Roads to Rome (2015)

**原文标题**: Roads to Rome (2015)

**原文链接**: [https://benedikt-gross.de/projects/roads-to-rome/](https://benedikt-gross.de/projects/roads-to-rome/)

生成摘要时出错

---

## 94. Ukranian controls Home Assistant over LoRa radio when their power grid goes down

**原文标题**: Ukranian controls Home Assistant over LoRa radio when their power grid goes down

**原文链接**: [https://old.reddit.com/r/homeassistant/comments/1r8ftc0/i_control_my_home_assistant_over_lora_radio_when/](https://old.reddit.com/r/homeassistant/comments/1r8ftc0/i_control_my_home_assistant_over_lora_radio_when/)

生成摘要时出错

---

## 95. Instruction decoding in the Intel 8087 floating-point chip

**原文标题**: Instruction decoding in the Intel 8087 floating-point chip

**原文链接**: [https://www.righto.com/2026/02/8087-instruction-decoding.html](https://www.righto.com/2026/02/8087-instruction-decoding.html)

生成摘要时出错

---

## 96. Freedom.gov: US State Department Plans VPN Portal for Europe

**原文标题**: Freedom.gov: US State Department Plans VPN Portal for Europe

**原文链接**: [https://www.heise.de/en/news/Freedom-gov-US-State-Department-plans-VPN-portal-for-Europe-11182526.html](https://www.heise.de/en/news/Freedom-gov-US-State-Department-plans-VPN-portal-for-Europe-11182526.html)

生成摘要时出错

---

## 97. Top worldwide with social-engineering and a cheat that's still undetected

**原文标题**: Top worldwide with social-engineering and a cheat that's still undetected

**原文链接**: [https://www.ud2.rip/blog/vsrg/](https://www.ud2.rip/blog/vsrg/)

生成摘要时出错

---

## 98. BarraCUDA Open-source CUDA compiler targeting AMD GPUs

**原文标题**: BarraCUDA Open-source CUDA compiler targeting AMD GPUs

**原文链接**: [https://github.com/Zaneham/BarraCUDA](https://github.com/Zaneham/BarraCUDA)

生成摘要时出错

---

## 99. 我如何使用 Obsidian (2023)

**原文标题**: How I use Obsidian (2023)

**原文链接**: [https://stephango.com/vault](https://stephango.com/vault)

生成摘要时出错

---

## 100. Show HN: Breadboard – A modern HyperCard for building web apps on the canvas

**原文标题**: Show HN: Breadboard – A modern HyperCard for building web apps on the canvas

**原文链接**: [https://breadboards.io/](https://breadboards.io/)

生成摘要时出错

---

