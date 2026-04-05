# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-05.md)

*最后自动更新时间: 2026-04-05 18:05:41*
## 1. 阿耳忒弥斯2号机组人员首次瞥见月球背面 [视频]

**原文标题**: Artemis II crew see first glimpse of far side of Moon [video]

**原文链接**: [https://www.bbc.com/news/videos/ce3d5gkd2geo](https://www.bbc.com/news/videos/ce3d5gkd2geo)

所提供的文本概述了一系列重大新闻报道，主要关注阿耳忒弥斯2号任务的历史性进展以及几项重大的国内外危机。

**阿耳忒弥斯2号任务**
在执行任务的第三天，阿耳忒弥斯2号机组人员——NASA宇航员里德·怀斯曼、维克多·格洛弗、克里斯蒂娜·科赫以及加拿大航天局宇航员杰里米·汉森——成为首批亲眼目睹月球背面东海盆地的人类。截至周六晚，猎户座飞船距离地球约18万英里。机组人员称这次体验“绝对壮观”，并指出月球背面与从地球上看到的熟悉月面有着显著不同。

**航空与基础设施危机**
纽约拉瓜迪亚机场发生了一起重大悲剧，一架载有76人的加拿大航空客机在跑道上与一辆消防车相撞。这起“致命碰撞”导致了大规模的交通中断。受政府部分停摆影响，交通安全管理局（TSA）特工在无薪工作，局势进一步恶化，政府不得不部署移民海关执法局（ICE）特工到机场协助工作。

**政治与经济动荡**
头条新闻反映了一段剧烈的国内动荡和全球冲突时期：
*   **战争与经济：** 持续进行的对伊战争已导致美国汽油价格升至每加仑4美元以上，给农业部门带来了沉重的财务负担。
*   **抗议活动：** 由布鲁斯·斯普林斯汀参与的“拒绝国王”集会已在美国各地蔓延，抗议特朗普政府。
*   **政府活动：** 代理总检察长托德·布兰奇的角色正受到审查，而第一夫人梅拉尼娅·特朗普主持了一场关于人工智能与数字安全的峰会，并展示了一个人形机器人。
*   **法律裁决：** 洛杉矶的一个陪审团最近裁定，Meta和谷歌因故意创建损害青少年心理健康的成瘾性平台而承担责任。

---

## 2. Codex 将面向所有用户切换为基于 API 用量的计费模式。

**原文标题**: Codex is switching to API pricing based usage for all users

**原文链接**: [https://help.openai.com/en/articles/20001106-codex-rate-card](https://help.openai.com/en/articles/20001106-codex-rate-card)

OpenAI 已宣布 Codex 模型的免费测试期于 2023 年 3 月 23 日结束。因此，特定的 Codex 模型——`code-davinci-002` 和 `code-cushman-001`——已被弃用。

此次过渡的要点包括：

*   **模型过渡：** OpenAI 建议所有用户从旧版 Codex 模型迁移至 `gpt-3.5-turbo` 或 `gpt-4`。这些模型具备强大的代码处理能力，且与原始 Codex 模型相比，性能更优、用途更广。
*   **定价：** 虽然 Codex 测试版此前可免费使用，但替代模型将按照 OpenAI 的标准 API 定价计费。这意味着用户将根据处理的 Token 数量支付费用。
*   **研究访问：** 为支持学术界，OpenAI 提供了研究人员访问计划。如果标准定价造成负担，研究人员和教育工作者可以申请资助访问以继续其工作。
*   **功能：** 较新的聊天补全（Chat Completions）API 模型支持与 Codex 相同的编程功能，但在处理更广泛的指令和对话语境方面进行了优化。

这一变化反映了 OpenAI 整合其模型产品、并将资源集中于最先进且高效的大语言模型的策略。建议用户将其应用程序更新至较新模型，以确保服务的持续性并获得更好的效果。

---

## 3. 八年渴望，三月 AI 筑就

**原文标题**: Eight years of wanting, three months of building with AI

**原文链接**: [https://lalitm.com/post/building-syntaqlite-ai/](https://lalitm.com/post/building-syntaqlite-ai/)

在渴望更好的 SQLite 开发工具八年后，作者利用 AI 编程助手在三个月内构建了 **syntaqlite**。该项目涉及提取并适配 SQLite 复杂且缺乏文档的 C 语言解析器——这项任务此前因过于“艰巨且乏味”而被认为不适合作为业余项目。

开发过程分为两个阶段。最初，作者尝试了“凭感觉编码”（vibe-coding），将几乎所有实现工作交给 Claude Code。虽然这产生了一个可运行的原型，但生成的“面条式代码”难以维护。这促使作者用 Rust 进行了彻底重写，期间作者重新主导设计决策，并将 AI 作为“加强版自动补全”，将其融入严格的代码审查、重构和自动化测试流程中。

**AI 的主要优势：**
*   **克服惯性：** AI 提供的具体原型将令人生畏的设计任务转化为了可处理的具体问题。
*   **速度与重构：** AI 擅长编写“标准”代码，并能实现快速、大规模的重构。
*   **助教功能：** 它弥补了作者在 Rust 工具链和编辑器扩展 API 等陌生领域的知识空白。
*   **项目广度：** AI 降低了“长尾”功能（如 WASM 演练场、打包和文档）的开发成本，使得 0.1 版本的发布更加完整。

**核心代价与挑战：**
*   **“老虎机”效应：** 作者注意到提示词（prompting）具有某种成瘾性，可能导致陷入无意义的时间消耗。
*   **疲劳导致的收益递减：** 深夜时段措辞不当的提示词会产生“垃圾代码”和循环错误。
*   **上下文丢失：** 过度依赖 AI 导致作者偶尔会失去对代码库的心理建模，使深度调试变得困难。

作者总结道，虽然 AI 是该项目的关键催化剂，但其成功仍取决于保持人类的“品味”、技术领导力，以及果断舍弃低质量 AI 输出的意愿。

---

## 4. 用 (nightly) Rust 编写的尾调用解释器

**原文标题**: A tail-call interpreter in (nightly) Rust

**原文链接**: [https://www.mattkeeter.com/blog/2026-04-05-tailcall/](https://www.mattkeeter.com/blog/2026-04-05-tailcall/)

本文探讨了如何利用 `become` 关键字实现高性能的 Uxn CPU 模拟器。该关键字是 Rust nightly 版本最近新增的特性，用于显式尾调用优化（tail-call optimization）。

作者的目标是在保持 Rust 安全性的同时，达到其此前手写 ARM64 汇编代码的性能水平。尾调用解释器的工作原理是将虚拟机状态（寄存器、栈和程序计数器）作为函数参数传递，并在每条指令结束时直接跳转到下一个函数。这种被称为“线程代码”（threaded code）的技术通过替换当前栈帧而非嵌套栈帧来防止栈溢出。

关键实现细节包括：
*   **样板代码管理**：作者利用复杂的宏将现有的操作码逻辑封装为尾调用函数。
*   **调用约定**：在 x86 平台上，作者使用了 `extern "rust-preserve-none"` 来确保编译器使用足够的寄存器传递参数，从而减少开销。
*   **安全性**：整个实现保持了 100% 的安全 Rust，成功避免了作者此前汇编版本中存在的内存损坏风险。

**性能测试结果：**
*   **ARM64 (M1 MacBook)**：尾调用解释器取得了圆满成功，性能超过了原有的 Rust 虚拟机和手写汇编。
*   **x86-64**：结果喜忧参半。虽然明显快于原有的虚拟机，但仍落后于经过手动调优的汇编。对生成的机器码进行检查后发现，Rust 编译器在 x86 上引入了不必要的“寄存器重组”和栈溢出，而人工编写代码可以避免这些问题。

最终作者得出结论：Rust 的尾调用支持为编写高性能模拟器提供了一种愉悦且高效的方式，证明了在合适的架构条件下，安全的人类编写代码现已能与汇编语言相媲美。

---

## 5. 穴居人：何必多用token，少用就行。

**原文标题**: Caveman: Why use many token when few token do trick

**原文链接**: [https://github.com/JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)

**Caveman** 是一款专为 Claude Code 和 Codex 设计的插件，旨在不牺牲技术准确性的前提下，将大语言模型（LLM）的输出 Token 减少约 75%。受“穴居人说话（caveman-speak）”梗的启发，该工具强制 AI 采用极简的、电报式的风格进行交流，剔除了填充词、客套话、冠词和模棱两可的表述。

**核心特性与优势：**
*   **高效性：** 通过剔除“废话”（如“我很乐意为您提供帮助”），Caveman 将响应长度平均缩减了 65%–87%，从而显著提升了生成速度并降低了 API 成本。
*   **技术完整性：** 尽管 AI 的表达变得简单，但它保留了 100% 的技术准确性。代码块、技术术语（如“多态性”）和错误消息均保持原样。
*   **性能提升：** 该项目引用的研究表明，简洁性约束实际上可以通过迫使模型关注实质内容而非冗长辞藻，从而提高 LLM 的准确性。
*   **定向优化：** 该插件仅影响“输出”Token；AI 的内部推理和“思考”Token 则不受限制。

**使用与安装：**
Caveman 由 Julius Brussee 开发，可通过 `npx skills add JuliusBrussee/caveman` 或 Claude Code 插件市场进行安装。安装后，用户可以使用 `/caveman` 或 "caveman mode" 等命令开启该模式，并通过 "normal mode" 恢复正常。

总之，Caveman 是为那些比起对话礼貌，更看重速度、可读性和成本效益的开发者而打造的生产力工具。

---

## 6. 计算物理（第2版）

**原文标题**: Computational Physics (2nd Edition)

**原文链接**: [https://websites.umich.edu/~mejn/cp2/](https://websites.umich.edu/~mejn/cp2/)

Mark Newman 所著的《计算物理》（第2版）是一本全面的教科书及在线资源，旨在向学生介绍利用计算机解决物理问题的核心技术。本书主要围绕 Python 编程语言展开，在理论物理与实际计算应用之间架起了一座桥梁。

该书的官方网站作为一个配套中心，为学生和教师提供了丰富的资源。其主要特色包括：

*   **核心课程：** 本书涵盖了广泛的基础数值方法，包括积分、微分、线性方程组、傅里叶变换以及蒙特卡罗模拟等随机方法。此外，书中还深入探讨了对物理系统建模至关重要的常微分方程和偏微分方程的求解。
*   **强调 Python：** Newman 极力推崇 Python，得益于其出色的易读性以及 NumPy 和 Matplotlib 等强大科学库的支持。这使得没有深厚计算机科学背景的学习者也能顺利掌握相关内容。
*   **实用资源：** 网站提供了书中所有示例和程序的 Python 源代码下载。此外，还配有课后练习所需的数据文件，便于用户进行实战数据分析。
*   **教学支持：** 除代码外，网站还包含详细目录、前言及勘误表，以确保学习者获取的信息准确无误。

总体而言，该资源将计算物理定位为与实验和理论并列的科学方法第三大支柱，为现代物理研究与模拟提供了必备的工具。

---

## 7. Nanocode：200美元预算内，在TPU上基于纯JAX实现的最佳Claude Code。

**原文标题**: Nanocode: The best Claude Code that $200 can buy in pure JAX on TPUs

**原文链接**: [https://github.com/salmanmohammadi/nanocode/discussions/1](https://github.com/salmanmohammadi/nanocode/discussions/1)

Salman Mohammadi 推出了 nanocode，这是一个纯 JAX 编写的开源库，旨在 TPU 上端到端地训练智能体编码模型。受 Andrej Karpathy 的 *nanochat* 启发，该项目展示了如何以较低的预算构建一个“Claude Code”风格的助手。

**核心技术细节：**
*   **模型扩展：** 该库包含两个主要模型：一个拥有 13 亿参数（d24）的模型，训练成本约为 200 美元（在 TPU v6e-8 上运行 9 小时）；以及一个拥有 4.77 亿参数（d20）的模型，成本为 34 美元（1.5 小时）。
*   **数据与分词：** nanocode 采用了 *The Stack-V2* 和 *FineWeb-EDU* 按 1:5 比例混合的数据集。这种特定的配比使代码分词效率比标准模型提高了 50%，同时保持了与 GPT-2 XL 相当的通用推理能力。
*   **智能体框架：** 模型通过专门的工具调用接口与环境交互。它使用特定的特殊标记（tokens）来执行 `Read`、`Edit`、`Grep` 和 `Bash` 等命令，从而使其能够浏览和修改类 UNIX 文件系统。

**训练理念：**
nanocode 采用了由 Anthropic 推广的宪法 AI（Constitutional AI, CAI）方法论。这包括：
1.  **一份“SOUL”文档：** 一份定义模型性格的宪法规范——具体表现为一种随和、友好且“搞怪”的人设，且全篇仅使用小写文本。
2.  **对齐：** 训练流水线包括合成数据生成和偏好优化，以确保模型遵循其行为原则并可靠地使用工具。

该项目强调，通过优化的 JAX 基础设施和谷歌的 TPU 研究云（TRC）项目，开发者可以高效且以适度的算力成本，复现复杂的智能体编码助手。

---

## 8. Finnish sauna heat exposure induces stronger immune cell than cytokine responses

**原文标题**: Finnish sauna heat exposure induces stronger immune cell than cytokine responses

**原文链接**: [https://www.tandfonline.com/doi/full/10.1080/23328940.2026.2645467#abstract](https://www.tandfonline.com/doi/full/10.1080/23328940.2026.2645467#abstract)

生成摘要时出错

---

## 9. From birds to brains: My path to the fusiform face area (2024)

**原文标题**: From birds to brains: My path to the fusiform face area (2024)

**原文链接**: [https://www.kavliprize.org/nancy-kanwisher-autobiography](https://www.kavliprize.org/nancy-kanwisher-autobiography)

生成摘要时出错

---

## 10. Lisette a little language inspired by Rust that compiles to Go

**原文标题**: Lisette a little language inspired by Rust that compiles to Go

**原文链接**: [https://lisette.run/](https://lisette.run/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 2 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 3 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 4 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 5 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 6 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 7 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 8 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 9 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 10 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 11 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 12 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 13 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 14 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 15 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 16 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 17 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 18 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 19 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 20 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 21 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 22 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 23 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 24 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 25 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 26 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 27 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 28 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 29 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 30 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 31 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 32 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 33 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 34 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 35 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 36 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 37 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 38 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 39 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 40 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 41 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 42 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 43 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 44 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 45 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 46 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 47 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 48 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 49 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 50 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 51 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 52 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 53 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 54 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 55 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 56 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 57 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 58 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 59 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 60 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 61 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 62 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 63 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 64 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 65 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 66 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 67 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 68 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 69 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 70 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 71 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 72 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 73 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 74 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 75 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 76 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 77 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 78 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 79 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 80 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 81 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 82 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 83 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 84 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 85 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 86 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 87 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 88 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 89 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 90 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 91 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 92 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 93 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 94 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 95 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 96 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 97 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 98 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 99 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 100 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 101 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 102 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 103 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 104 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 105 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 106 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 107 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 108 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 109 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 110 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 111 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 112 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 113 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 114 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 115 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 116 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 117 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 118 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 119 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 120 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 121 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 122 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 123 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 124 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 125 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 126 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 127 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 128 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 129 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 130 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 131 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 132 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 133 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 134 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 135 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 136 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 137 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 138 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 139 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 140 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 141 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 142 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 143 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 144 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 145 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 146 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 147 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 148 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 149 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 150 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 151 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 152 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 153 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 154 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 155 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 156 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 157 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 158 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 159 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 160 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 161 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 162 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 163 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 164 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 165 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 166 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 167 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 168 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 169 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 170 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 171 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 172 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 173 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 174 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 175 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 176 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 177 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 178 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 179 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 180 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 181 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 182 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 183 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 184 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 185 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 186 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 187 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 188 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 189 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 190 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 191 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 192 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 193 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 194 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 195 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 196 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 197 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 198 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 199 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 200 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 201 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 202 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 203 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 204 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 205 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 206 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 207 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 208 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 209 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 210 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 211 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 212 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 213 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 214 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 215 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 216 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 217 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 218 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 219 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 220 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 221 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 222 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 223 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 224 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 225 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 226 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 227 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 228 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 229 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 230 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 231 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 232 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 233 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 234 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 235 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 236 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 237 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 238 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 239 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 240 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 241 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 242 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 243 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 244 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 245 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 246 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 247 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 248 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 249 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 250 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 251 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 252 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 253 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 254 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 255 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 256 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 257 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 258 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 259 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 260 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 261 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 262 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 263 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 264 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 265 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 266 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 267 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 268 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 269 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 270 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 271 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 272 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 273 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 274 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 275 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 276 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 277 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 278 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 279 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 280 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 281 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 282 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 283 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 284 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 285 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 286 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 287 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 288 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 289 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 290 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 291 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 292 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 293 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 294 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 295 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 296 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 297 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 298 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 299 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 300 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 301 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 302 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 303 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 304 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 305 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 306 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 307 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 308 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 309 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 310 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 311 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 312 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 313 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 314 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 315 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 316 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 317 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 318 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 319 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 320 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 321 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 322 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 323 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 324 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 325 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 326 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 327 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 328 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 329 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 330 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 331 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 332 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 333 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 334 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 335 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 336 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 337 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 338 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 339 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 340 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 341 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 342 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 343 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 344 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 345 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 346 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 347 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 348 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 349 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 350 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 351 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 352 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 353 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 354 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 355 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 356 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 357 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 358 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 359 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 360 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 361 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 362 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 363 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 364 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 365 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 366 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 367 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 368 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 369 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 370 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 371 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 372 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 373 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 374 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 375 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 376 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 377 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 378 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 379 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 380 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 381 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
