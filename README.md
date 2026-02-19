# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-02-19.md)

*最后自动更新时间: 2026-02-19 18:20:08*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 2 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 3 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 4 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 5 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 6 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 7 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 8 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 9 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 10 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 11 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 12 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 13 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 14 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 15 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 16 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 17 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 18 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 19 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 20 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 21 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 22 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 23 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 24 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 25 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 26 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 27 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 28 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 29 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 30 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 31 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 32 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 33 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 34 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 35 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 36 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 37 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 38 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 39 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 40 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 41 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 42 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 43 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 44 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 45 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 46 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 47 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 48 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 49 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 50 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 51 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 52 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 53 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 54 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 55 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 56 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 57 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 58 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 59 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 60 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 61 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 62 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 63 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 64 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 65 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 66 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 67 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 68 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 69 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 70 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 71 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 72 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 73 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 74 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 75 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 76 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 77 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 78 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 79 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 80 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 81 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 82 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 83 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 84 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 85 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 86 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 87 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 88 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 89 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 90 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 91 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 92 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 93 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 94 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 95 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 96 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 97 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 98 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 99 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 100 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 101 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 102 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 103 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 104 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 105 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 106 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 107 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 108 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 109 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 110 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 111 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 112 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 113 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 114 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 115 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 116 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 117 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 118 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 119 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 120 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 121 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 122 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 123 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 124 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 125 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 126 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 127 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 128 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 129 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 130 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 131 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 132 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 133 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 134 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 135 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 136 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 137 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 138 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 139 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 140 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 141 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 142 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 143 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 144 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 145 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 146 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 147 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 148 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 149 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 150 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 151 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 152 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 153 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 154 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 155 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 156 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 157 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 158 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 159 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 160 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 161 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 162 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 163 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 164 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 165 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 166 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 167 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 168 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 169 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 170 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 171 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 172 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 173 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 174 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 175 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 176 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 177 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 178 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 179 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 180 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 181 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 182 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 183 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 184 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 185 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 186 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 187 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 188 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 189 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 190 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 191 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 192 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 193 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 194 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 195 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 196 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 197 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 198 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 199 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 200 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 201 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 202 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 203 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 204 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 205 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 206 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 207 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 208 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 209 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 210 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 211 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 212 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 213 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 214 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 215 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 216 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 217 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 218 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 219 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 220 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 221 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 222 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 223 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 224 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 225 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 226 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 227 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 228 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 229 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 230 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 231 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 232 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 233 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 234 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 235 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 236 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 237 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 238 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 239 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 240 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 241 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 242 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 243 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 244 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 245 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 246 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 247 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 248 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 249 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 250 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 251 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 252 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 253 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 254 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 255 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 256 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 257 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 258 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 259 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 260 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 261 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 262 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 263 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 264 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 265 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 266 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 267 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 268 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 269 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 270 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 271 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 272 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 273 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 274 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 275 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 276 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 277 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 278 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 279 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 280 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 281 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 282 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 283 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 284 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 285 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 286 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 287 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 288 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 289 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 290 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 291 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 292 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 293 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 294 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 295 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 296 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 297 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 298 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 299 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 300 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 301 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 302 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 303 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 304 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 305 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 306 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 307 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 308 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 309 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 310 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 311 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 312 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 313 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 314 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 315 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 316 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 317 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 318 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 319 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 320 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 321 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 322 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 323 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 324 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 325 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 326 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 327 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 328 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 329 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 330 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 331 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 332 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 333 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 334 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 335 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 336 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
