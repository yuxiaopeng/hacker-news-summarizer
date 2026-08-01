# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-08-01.md)

*最后自动更新时间: 2026-08-01 18:23:40*
## 1. Cursor 从使用页面和 CSV 导出中移除了成本信息。

**原文标题**: Cursor removed cost information from the usage page and CSV export

**原文链接**: [https://forum.cursor.com/t/usage-page-to-token-amount-what/167153](https://forum.cursor.com/t/usage-page-to-token-amount-what/167153)

本摘要基于 Cursor 论坛题为“Usage page to token amount - what?”（使用页面变为 Token 数量——怎么回事？）的讨论帖。

讨论的核心是 Cursor 使用情况仪表板最近的一项变化：此前用于显示 AI 使用金额的“Cost”（成本）列已从 Web 界面和可下载的 CSV 导出文件中移除。

**关键点：**

*   **移除货币指标：** 用户注意到，使用页面不再显示请求所花费的美元金额。该信息已被 Token 计数或请求量取代，在某些情况下，导出数据中则完全省略了此项内容。
*   **对 API 用户的影响：** 这一变化对于使用自带 API 密钥（如 OpenAI 或 Anthropic）的用户来说尤为不便。没有了成本列，这些用户很难直接在 Cursor 界面内追踪实际支出并管理预算。
*   **缺乏透明度：** 论坛成员对缺乏透明度表示不满，指出他们现在必须根据 Token 计数和当前模型定价手动计算成本，这一过程既繁琐又容易出错。
*   **业务与团队审计：** 对于管理团队账户或专业项目的用户而言，成本数据的移除使审计使用情况以及将费用分配给特定客户或部门的过程变得复杂化。
*   **用户诉求：** 社区呼吁恢复成本列，或者至少提供更详细的 Token 细分数据，以匹配供应商对输入、输出和缓存 Token 的计费方式。

总之，虽然 Cursor 似乎正在将重心转向使用量（Token/请求数），但直接成本信息的缺失给依赖该平台进行 AI 支出精确财务追踪的用户带来了显著困扰。

---

## 2. 64位汇编艺术

**原文标题**: The Art of 64-bit Assembly

**原文链接**: [https://nostarch.com/art-64-bit-assembly-v2](https://nostarch.com/art-64-bit-assembly-v2)

《64位汇编语言艺术》是一本专注于使用64位汇编语言（特别是针对微软宏汇编器 MASM）进行高级底层编程技术的技术指南。本书并非侧重于基础语法，而是深入探讨了如何在机器层面直接实现复杂的高级编程概念。

核心内容分为以下几个关键领域：

*   **高级工程：** 涵盖了复杂的结构，如高级宏、专门的过程以及复杂的参数实现。
*   **数据与数学：** 介绍了如何在汇编中处理 Unicode 字符串并执行超越函数（如三角函数或对数等复杂数学运算）。
*   **现代编程范式：** 大量篇幅致力于在底层环境中实现高级概念，包括面向对象编程 (OOP)、异常处理和并发编程。
*   **高级控制流：** 作者探讨了复杂的执行模型，如 thunk、闭包、迭代器、协程、生成器和纤程 (fibers)。

本书还包括用于搭建 Visual Studio 环境的实用附录，以及 ASCII 字符集和术语表等快速参考资料。总而言之，本书为希望在高性能 64 位汇编语言环境中应用现代软件工程原则（如模块化和抽象化）的开发者提供了沟通的桥梁。

---

## 3. Kaisel – 路由即值。基于 Dart 3 的 Flutter 原生路由。

**原文标题**: Kaisel – Routes as Values. Dart 3 Native Router for Flutter

**原文链接**: [https://kaisel.dev/](https://kaisel.dev/)

**Kaisel** 是一个专为 Dart 3 构建的原生 Flutter 路由库，它引入了“**路由即值**（Routes as Values）”的概念。通过利用现代 Dart 特性——特别是**密封类（sealed classes）**和**穷举匹配（exhaustive switches）**——它提供了一种类型安全的导航方式，确保应用逻辑涵盖了所有定义的路由。

该库专注于开发效率和代码可靠性。其配置过程非常快捷，使开发者能够在几分钟内完成从安装（`flutter pub add kaisel`）到使用全类型路由进行导航的过渡。通过将路由视为值而非简单的字符串，Kaisel 减少了样板代码，并最大限度地降低了传统路由方法中常见的运行时错误。

总之，Kaisel 提供了一种精简且“Dart 原生”的 Flutter 导航处理方式，强调类型安全和快速集成。

---

## 4. RipGrep musl binaries occasionally segfault during very-large searches

**原文标题**: RipGrep musl binaries occasionally segfault during very-large searches

**原文链接**: [https://github.com/BurntSushi/ripgrep/issues/3494](https://github.com/BurntSushi/ripgrep/issues/3494)

生成摘要时出错

---

## 5. 探索性建模：在 K 个猜测的最佳结果上进行训练

**原文标题**: Explorative modeling: Train on the best of K guesses

**原文链接**: [https://alexiglad.github.io/blog/2026/explorative_modeling/](https://alexiglad.github.io/blog/2026/explorative_modeling/)

探索性建模（XM）是生成式建模的一种新范式，旨在解决“多解”问题：即模型在通过直接回归训练时，往往会预测所有有效输出的平均值（例如，产生“模糊”图像而非清晰图像）。虽然大语言模型（LLM）和扩散模型（Diffusion）等现有模型通过将生成过程分解为多个小步骤（即“生成分解”）来解决这一问题，但这种方法会导致曝光偏差并阻碍端到端训练。

相比之下，XM 通过让模型对单个输入产生 $K$ 个猜测来实现“训练分解”。在该过程中，只有最佳猜测会获得梯度，这一机制被称为**模态强制（Mode Forcing）**。这使得模型能够专注于特定的数据点，而非它们的平均值。作者将这种能力定义为**生成表达力（generative expressivity）**，并认为它是继参数和数据之后，衡量预训练能力的第三个关键维度。

**核心结果：**
*   **效率：** 与现有最先进的基准相比，XM 的样本效率提升了 6.2 倍，FLOP（浮点运算）效率提升了 4.1 倍，参数效率提升了 47%。
*   **扩展性：** 探索带来的收益随规模增长而增加：随着数据量增加，收益从 7% 升至 36%；随着参数量增加，收益从 13% 升至 23%。
*   **性能：** XM 在 ImageNet 256 数据集上达到了 1.43 FID 的领先水平。同时，它在视频和语言建模领域也展现出持续的改进。
*   **推理：** 作为一种端到端模型，XM 在控制任务上的表现与扩散模型相当，但由于其采用单步生成方式，所需的推理计算量最高可降低 256 倍。

通过将复杂性从生成过程转移到训练循环中，XM 使模型能够保持端到端特性（即训练方式与推理运行完全一致），同时为在各个生成领域实现更高保真度提供了一条可扩展的路径。

---

## 6. Pgtestdb 基于模板克隆的测试方法速度很快。

**原文标题**: Pgtestdb's template cloning approach to testing is fast

**原文链接**: [https://brandur.org/fragments/pgtestdb](https://brandur.org/fragments/pgtestdb)

在本文中，Brandur 探讨了 **pgtestdb**，这是一个利用 Postgres 内置模板数据库特性的 Go/Postgres 测试包。通过使用 `CREATE DATABASE ... TEMPLATE` 命令，该工具以 8 kB 数据块的形式复制物理文件，从而克隆已预迁移的数据库。相比于从头运行迁移或使用笨重的 Docker 设置，这提供了一个更快的替代方案。

Brandur 将 `pgtestdb` 与他在其项目 **River** 中使用的基于 schema 的测试方法进行了对比。尽管他此前认为创建新数据库会很慢，但结果显示，两种方法的启动时间相近，每个测试大约只需 **100 毫秒**。这使得 `pgtestdb` 成为开发者的一个可行选择，特别是当需要测试数据库全局特性（如 `LISTEN/NOTIFY`）或传统测试事务无法处理的多事务交互时。

然而，对比也揭示了在总耗时上的显著差异：River 的测试套件在 14.5 秒内完成，而 `pgtestdb` 的实现则耗时 51 秒。这一差距源于**重用**。River 对其测试 schema 进行了池化，通过清理并重用它们来执行后续测试，而不是每次都重新创建。

Brandur 总结道，虽然他为了验证特定配置将继续在 River 中使用 schema，但他强烈推荐将 `pgtestdb` 用于端到端测试。他指出，如果 `pgtestdb` 或其用户实现类似的池化/重用策略，启动时间可能会降至 10–20 毫秒，使完整数据库隔离的速度接近测试事务的水平。

---

## 7. A Surveillance Treaty in Disguise: Canada Signs UN Cybercrime Convention

**原文标题**: A Surveillance Treaty in Disguise: Canada Signs UN Cybercrime Convention

**原文链接**: [https://www.michaelgeist.ca/2026/07/a-surveillance-treaty-in-disguise-the-trouble-with-canadas-quiet-decision-to-sign-the-un-cybercrime-convention/](https://www.michaelgeist.ca/2026/07/a-surveillance-treaty-in-disguise-the-trouble-with-canadas-quiet-decision-to-sign-the-un-cybercrime-convention/)

生成摘要时出错

---

## 8. RSS 爱好者名录

**原文标题**: A directory of people who love RSS

**原文链接**: [https://andrewshell.org/2026/07/i-%e2%99%a5-rss/](https://andrewshell.org/2026/07/i-%e2%99%a5-rss/)

2026年7月30日，作者宣布推出 **I ♥ RSS**，这是一个专为 RSS 爱好者打造的新目录。该平台允许用户提交自己的网站，并在首页展示由 FeedLand 驱动的实时博客列表。作者已在自己的网站上集成了该目录的徽章，并鼓励广大 RSS 爱好者探索该目录，将自己的网站也加入其中。

---

## 9. Register deprivation: spills and runtime under forced register scarcity

**原文标题**: Register deprivation: spills and runtime under forced register scarcity

**原文链接**: [https://rjp.io/blog/2026-07-19-register-deprivation](https://rjp.io/blog/2026-07-19-register-deprivation)

生成摘要时出错

---

## 10. Charlie Stross – On the non-use of AI in my writing process

**原文标题**: Charlie Stross – On the non-use of AI in my writing process

**原文链接**: [https://www.antipope.org/charlie/blog-static/2026/08/on-the-non-use-of-ai-in-my-wri.html](https://www.antipope.org/charlie/blog-static/2026/08/on-the-non-use-of-ai-in-my-wri.html)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 2 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 3 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 4 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 5 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 6 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 7 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 8 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 9 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 10 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 11 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 12 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 13 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 14 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 15 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 16 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 17 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 18 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 19 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 20 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 21 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 22 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 23 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 24 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 25 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 26 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 27 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 28 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 29 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 30 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 31 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 32 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 33 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 34 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 35 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 36 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 37 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 38 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 39 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 40 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 41 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 42 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 43 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 44 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 45 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 46 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 47 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 48 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 49 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 50 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 51 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 52 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 53 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 54 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 55 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 56 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 57 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 58 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 59 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 60 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 61 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 62 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 63 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 64 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 65 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 66 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 67 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 68 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 69 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 70 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 71 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 72 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 73 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 74 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 75 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 76 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 77 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 78 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 79 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 80 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 81 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 82 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 83 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 84 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 85 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 86 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 87 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 88 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 89 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 90 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 91 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 92 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 93 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 94 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 95 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 96 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 97 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 98 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 99 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 100 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 101 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 102 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 103 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 104 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 105 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 106 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 107 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 108 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 109 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 110 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 111 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 112 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 113 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 114 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 115 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 116 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 117 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 118 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 119 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 120 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 121 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 122 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 123 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 124 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 125 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 126 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 127 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 128 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 129 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 130 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 131 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 132 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 133 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 134 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 135 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 136 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 137 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 138 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 139 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 140 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 141 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 142 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 143 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 144 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 145 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 146 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 147 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 148 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 149 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 150 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 151 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 152 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 153 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 154 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 155 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 156 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 157 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 158 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 159 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 160 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 161 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 162 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 163 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 164 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 165 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 166 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 167 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 168 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 169 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 170 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 171 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 172 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 173 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 174 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 175 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 176 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 177 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 178 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 179 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 180 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 181 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 182 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 183 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 184 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 185 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 186 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 187 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 188 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 189 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 190 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 191 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 192 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 193 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 194 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 195 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 196 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 197 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 198 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 199 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 200 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 201 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 202 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 203 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 204 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 205 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 206 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 207 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 208 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 209 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 210 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 211 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 212 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 213 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 214 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 215 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 216 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 217 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 218 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 219 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 220 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 221 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 222 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 223 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 224 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 225 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 226 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 227 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 228 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 229 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 230 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 231 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 232 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 233 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 234 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 235 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 236 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 237 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 238 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 239 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 240 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 241 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 242 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 243 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 244 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 245 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 246 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 247 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 248 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 249 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 250 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 251 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 252 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 253 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 254 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 255 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 256 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 257 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 258 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 259 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 260 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 261 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 262 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 263 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 264 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 265 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 266 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 267 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 268 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 269 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 270 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 271 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 272 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 273 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 274 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 275 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 276 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 277 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 278 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 279 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 280 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 281 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 282 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 283 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 284 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 285 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 286 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 287 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 288 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 289 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 290 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 291 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 292 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 293 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 294 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 295 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 296 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 297 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 298 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 299 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 300 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 301 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 302 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 303 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 304 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 305 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 306 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 307 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 308 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 309 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 310 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 311 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 312 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 313 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 314 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 315 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 316 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 317 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 318 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 319 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 320 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 321 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 322 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 323 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 324 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 325 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 326 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 327 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 328 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 329 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 330 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 331 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 332 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 333 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 334 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 335 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 336 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 337 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 338 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 339 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 340 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 341 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 342 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 343 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 344 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 345 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 346 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 347 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 348 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 349 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 350 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 351 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 352 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 353 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 354 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 355 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 356 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 357 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 358 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 359 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 360 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 361 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 362 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 363 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 364 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 365 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 366 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 367 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 368 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 369 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 370 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 371 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 372 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 373 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 374 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 375 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 376 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 377 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 378 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 379 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 380 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 381 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 382 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 383 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 384 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 385 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 386 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 387 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 388 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 389 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 390 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 391 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 392 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 393 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 394 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 395 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 396 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 397 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 398 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 399 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 400 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 401 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 402 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 403 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 404 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 405 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 406 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 407 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 408 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 409 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 410 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 411 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 412 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 413 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 414 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 415 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 416 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 417 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 418 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 419 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 420 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 421 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 422 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 423 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 424 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 425 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 426 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 427 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 428 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 429 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 430 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 431 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 432 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 433 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 434 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 435 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 436 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 437 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 438 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 439 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 440 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 441 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 442 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 443 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 444 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 445 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 446 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 447 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 448 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 449 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 450 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 451 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 452 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 453 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 454 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 455 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 456 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 457 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 458 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 459 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 460 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 461 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 462 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 463 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 464 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 465 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 466 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 467 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 468 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 469 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 470 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 471 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 472 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 473 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 474 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 475 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 476 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 477 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 478 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 479 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 480 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 481 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 482 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 483 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 484 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 485 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 486 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 487 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 488 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 489 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 490 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 491 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 492 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 493 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 494 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 495 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 496 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 497 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 498 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 499 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
