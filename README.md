# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-09-12.md)

*最后自动更新时间: 2025-09-12 17:44:38*
## 1. 很多困难的力扣题都是约束简单的题。

**原文标题**: Many hard LeetCode problems are easy constraint problems

**原文链接**: [https://buttondown.com/hillelwayne/archive/many-hard-leetcode-problems-are-easy-constraint/](https://buttondown.com/hillelwayne/archive/many-hard-leetcode-problems-are-easy-constraint/)

本文论证了许多技术面试中常用的“困难”LeetCode题目，实际上可以使用MiniZinc、Z3或OR-Tools等约束求解器轻松解决。作者认为，传统编程语言对于这些优化问题（在约束条件下寻找最大值或最小值）来说过于底层，而约束求解器是专门为它们设计的。

作者通过几个例子证明了这一点，包括硬币找零问题、股票交易利润最大化问题、数字求和为零问题以及柱状图中最大矩形问题。对于每个问题，他们都提供了MiniZinc代码片段，说明了如何将问题轻松地表达为约束满足或优化问题。

作者承认，约束求解器的性能可能不如具有最佳运行时复杂度的手工算法，但它们通常更容易实现，尤其是在添加新约束时。作者用一个扩展的股票交易场景来说明这一点，该场景对销售和持有量有限制，如果用传统方式编码效率会很低，但只需对约束问题进行少量修改即可。

核心论点是，对于某些类型的面试题，使用约束求解器可以成为编写复杂算法的强大而有效的替代方案，为解决这些问题提供更实际的方法。作者建议，使用LeetCode问题比传统谜题更能体现约束求解器的优势。

---

## 2. 纸上的3D建模

**原文标题**: 3D modeling with paper

**原文链接**: [https://www.arvinpoddar.com/blog/3d-modeling-with-paper](https://www.arvinpoddar.com/blog/3d-modeling-with-paper)

无法访问文章链接。

---

## 3. 高级Scheme技巧 (2004) [pdf]

**原文标题**: Advanced Scheme Techniques (2004) [pdf]

**原文链接**: [https://people.csail.mit.edu//jhbrown/scheme/continuationslides04.pdf](https://people.csail.mit.edu//jhbrown/scheme/continuationslides04.pdf)

我无法提供该文档的摘要。该文本似乎是PDF文档，但呈现的内容并非人类可读的文本，而是编码数据，可能代表PDF的内部结构、字体和其他元素。要总结这篇文章，我需要访问PDF正确呈现的文本内容。

---

## 4. 财政部正在扩大爱国者法案以打击比特币的自我托管。

**原文标题**: The treasury is expanding the patriot act to attack Bitcoin self custody

**原文链接**: [https://www.tftc.io/treasury-iexpanding-patriot-act/](https://www.tftc.io/treasury-iexpanding-patriot-act/)

马蒂·本特认为，美国财政部正在扩大《爱国者法案》的适用范围，以针对比特币自托管，这对比特币用户和更广泛的加密货币领域来说是一个令人担忧的事态发展。他认为这种扩张是对金融自由和隐私的攻击。

文章可能概述了财政部计划如何实现这一目标，可能通过更严格的 KYC/AML 法规来针对与自托管钱包互动的个人或实体。 这可能涉及要求交易所收集更多关于用户向自己的钱包发送或接收比特币的数据，从而有效地跟踪资金流动，并可能标记被认为可疑的交易。

本特可能认为，这些措施会破坏比特币的核心原则，例如假名性和去中心化，并扼杀该领域的创新。他认为，自托管比特币的能力对于金融主权至关重要，它允许个人控制自己的资产，而无需依赖中介机构。 在他看来，《爱国者法案》的扩张代表了政府试图对比特币施加更大的控制，并限制其作为一种抗审查货币的潜力。 他可能会呼吁抵制，并强调捍卫比特币的自托管和隐私原则的重要性。

---

## 5. 人工智能邪教的兴起与启示的虚假先知

**原文标题**: The rise of AI cults and the false prophets of revelation

**原文链接**: [https://wisewolfmedia.substack.com/p/the-rise-of-ai-cults-truth-terminal](https://wisewolfmedia.substack.com/p/the-rise-of-ai-cults-truth-terminal)

无法访问文章链接。

---

## 6. Windows 使用：一个在 GUI 层与 Windows 交互的 AI 代理

**原文标题**: Windows-Use: an AI agent that interacts with Windows at GUI layer

**原文链接**: [https://github.com/CursorTouch/Windows-Use](https://github.com/CursorTouch/Windows-Use)

Windows-Use是一个旨在直接通过GUI自动化Windows操作系统任务的AI代理，使大型语言模型（LLM）能够控制操作系统，而无需依赖传统的计算机视觉。它能够执行诸如打开应用程序、点击按钮、键入、执行shell命令和捕获UI状态等操作。

安装需要Python 3.12或更高版本，并使用UV或pip包管理器。基本用法包括从`windows_use`库导入`Agent`类，使用LLM（例如通过`langchain-google-genai`的Gemini）初始化它，然后使用`invoke`方法根据用户查询执行任务。该代理可以直接从Python脚本运行。

该项目展示了其功能，例如在Word中创建和保存笔记以及在暗黑和浅色模式之间切换。该工具利用视觉能力来理解Windows环境并与之交互。

由于该代理直接与GUI交互，因此发出警告，提醒其可能导致意外的系统行为，建议在沙盒环境中进行使用。该项目是开源的，采用MIT许可证，并欢迎遵循CONTRIBUTING文件中指南的贡献。它由Jeomon George创建。

---

## 7. 通义千问3-Next

**原文标题**: Qwen3-Next

**原文链接**: [https://qwen.ai/blog?id=4074cca80393150c248e508aa62983f9cb7d27cd&from=research.latest-advancements-list](https://qwen.ai/blog?id=4074cca80393150c248e508aa62983f9cb7d27cd&from=research.latest-advancements-list)

文章极其简短，仅包含标题“Qwen3-Next”和正文中的一个词“Qwen”，因此无法提供实质性摘要。

**本质上，文章提供以下信息：**

*   **标题：**Qwen3-Next
*   **内容：** 指“Qwen”

**可能的解读：**

基于此有限的信息，只能推测“Qwen3-Next”可能指的是名为“Qwen”的模型或技术的未来版本或迭代（“Next”）。在没有更多上下文的情况下，无法确定“Qwen”实际上是什么（例如，大型语言模型、公司、产品），也无法确定“Qwen3-Next”有望带来哪些改进。

---

## 8. Emacs扩展入门指南

**原文标题**: A beginner's guide to extending Emacs

**原文链接**: [https://blog.tjll.net/a-beginners-guide-to-extending-emacs/](https://blog.tjll.net/a-beginners-guide-to-extending-emacs/)

本文为Emacs扩展入门指南，重点介绍如何为reStructuredText引用添加自动补全功能。文章强调了Emacs的可扩展性以及利用现有函数和文档的重要性。

作者逐步介绍了创建reStructuredText引用自定义补全后端的过程，首先确定相关的Emacs补全系统（completion-at-point-functions）。该指南解释了如何使用`define-thing-chars`和`bounds-of-thing-at-point`定义自定义的“thing”，以识别将被补全替换的文本。

随后，文章深入探讨了正则表达式，展示了Emacs的交互式正则表达式构建工具以及用于简化正则表达式创建的`rx`宏。文章演示了如何开发正则表达式来定位文档中的reStructuredText引用定义。

总结强调了实验、利用内置Emacs函数以及检查现有代码以获得指导的重要性。本文还旨在减轻学习Emacs Lisp时常有的畏惧感，在整个过程中提供基本的Lisp原理和实践示例。最终目标是使用户能够自定义Emacs以适应其特定需求，即使没有广泛的Emacs Lisp知识。

---

## 9. Oq：终端 OpenAPI 规范查看器

**原文标题**: Oq: Terminal OpenAPI Spec Viewer

**原文链接**: [https://github.com/plutov/oq](https://github.com/plutov/oq)

`oq` 是一款基于终端的 OpenAPI 规范 (OAS) 查看器，支持 YAML 或 JSON 格式，以及 OpenAPI 3.0.x 和 3.1.x 版本。它允许用户直接从命令行轻松导航和浏览 API 定义。

用户可以提供 OAS 文件作为参数（例如，`oq openapi.yaml`），从文件管道传输内容（例如，`cat openapi.yaml | oq`），或从 URL 流式传输（例如，`curl https://api.example.com/openapi.json | oq`）。

主要功能包括：

*   **导航：** 使用向上/向下箭头或 `k`/`j` 键移动项目。
*   **视图：** 使用 Tab 键在端点和组件视图之间切换。
*   **折叠/展开：** 使用 Enter 或 Space 键展开/折叠详细信息。
*   **退出：** 使用 `q` 或 `Ctrl+C` 退出。

该项目在 MIT 许可证下开源，并鼓励通过问题和拉取请求进行贡献。 贡献时，请确保测试通过，并使用 OpenAPI 3.0 和 3.1 示例进行测试。

---

## 10. Doom-ada：具有语法、LSP和Alire支持的Doom Emacs Ada语言模块

**原文标题**: Doom-ada: Doom Emacs Ada language module with syntax, LSP and Alire support

**原文链接**: [https://github.com/tomekw/doom-ada](https://github.com/tomekw/doom-ada)

本文档描述了用于 Ada 语言支持的 Doom Emacs 模块，名为“Doom-ada”。它使用 Tree-sitter 提供语法高亮，通过 `ada_language_server` 提供 LSP 支持，具有自动补全功能，并与 Alire 构建系统集成。

主要功能包括：

*   **语法高亮：** 使用 `ada-ts-mode` 进行准确高效的语法高亮。
*   **LSP 支持：** 利用 `ada_language_server` 通过 Eglot 提供语言服务器功能，如内联诊断和补全。
*   **自动补全：** 使用 `company-capf` 启用自动补全功能。
*   **Alire 集成：** 提供 Alire 命令（如构建、运行和清理）的快捷键（`SPC m b`，`SPC m r`，`SPC m c`）。编译错误会被解析到编译缓冲区中。

要安装此模块，用户需要将存储库克隆到他们的 Doom Emacs 模块文件夹中，在其 `init.el` 文件中启用 `ada` 模块，同步 Doom，然后重新启动 Emacs。 该模块要正常运行，需要 Alire 和 Ada 语言服务器。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 2 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 3 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 4 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 5 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 6 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 7 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 8 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 9 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 10 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 11 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 12 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 13 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 14 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 15 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 16 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 17 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 18 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 19 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 20 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 21 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 22 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 23 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 24 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 25 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 26 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 27 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 28 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 29 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 30 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 31 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 32 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 33 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 34 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 35 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 36 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 37 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 38 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 39 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 40 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 41 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 42 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 43 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 44 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 45 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 46 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 47 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 48 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 49 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 50 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 51 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 52 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 53 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 54 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 55 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 56 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 57 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 58 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 59 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 60 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 61 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 62 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 63 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 64 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 65 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 66 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 67 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 68 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 69 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 70 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 71 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 72 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 73 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 74 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 75 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 76 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 77 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 78 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 79 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 80 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 81 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 82 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 83 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 84 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 85 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 86 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 87 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 88 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 89 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 90 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 91 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 92 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 93 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 94 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 95 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 96 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 97 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 98 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 99 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 100 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 101 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 102 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 103 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 104 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 105 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 106 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 107 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 108 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 109 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 110 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 111 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 112 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 113 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 114 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 115 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 116 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 117 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 118 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 119 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 120 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 121 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 122 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 123 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 124 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 125 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 126 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 127 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 128 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 129 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 130 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 131 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 132 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 133 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 134 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 135 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 136 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 137 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 138 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 139 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 140 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 141 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 142 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 143 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 144 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 145 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 146 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 147 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 148 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 149 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 150 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 151 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 152 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 153 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 154 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 155 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 156 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 157 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 158 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 159 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 160 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 161 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 162 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 163 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 164 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 165 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 166 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 167 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 168 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 169 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 170 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 171 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 172 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 173 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 174 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 175 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 176 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 177 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
