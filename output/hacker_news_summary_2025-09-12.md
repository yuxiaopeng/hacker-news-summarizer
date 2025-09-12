# Hacker News 热门文章摘要 (2025-09-12)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 展示 HN：DWS OS，一个受 Plan 9 启发的 Web “操作系统”

**原文标题**: Show HN: DWS OS, a Plan 9 Inspired Web "OS"

**原文链接**: [https://dws.rip](https://dws.rip)

“Show HN”帖子介绍了 DWS OS，称其为受 Plan 9 启发的 Web “操作系统”。这表明它是一个基于 Web 的操作系统，模仿了贝尔实验室 Plan 9 的设计原则和功能。鉴于 Plan 9 以其以文件为中心的理念、分布式计算和命名空间虚拟化而闻名，DWS OS 很可能试图在 Web 浏览器环境中复制这些概念。

该帖子本身非常简短，几乎没有提供关于 DWS OS 的具体功能、实现或用途的明确信息。“Show HN”标签表明作者正在寻求 Hacker News 社区对其项目的反馈。因此，潜在用户可能需要进一步探索该项目（可能通过链接的网站或存储库，未包含在本文中）以了解其功能和潜在应用。仍未解答的关键问题包括：它如何模拟 Plan 9 的文件系统？它使用什么语言构建？它的预期用例是什么？ 该帖子的重点仅仅是宣布 DWS OS 的存在并激起读者的兴趣。

---

## 12. 使用MCP-Agent构建深度研究智能体

**原文标题**: Building a Deep Research Agent Using MCP-Agent

**原文链接**: [https://thealliance.ai/blog/building-a-deep-research-agent-using-mcp-agent](https://thealliance.ai/blog/building-a-deep-research-agent-using-mcp-agent)

萨尔马德·卡德里详述了他构建一个由MCP（模型控制平面）服务器驱动的深度研究代理的历程，强调了将LLM连接到MCP并使用简单设计模式足以完成复杂任务的理念。他回顾了三个迭代版本：

**第一版：编排器** - 基于Anthropic的模式，使用规划、执行和合成层。它适用于具有前期计划的任务，但在幻觉、token效率低下和固定计划方面表现不佳。

**第二版：自适应工作流** - 旨在改进第一版，具有动态子代理、FIFO TODO队列、外部记忆、预算管理和“野兽模式”。 然而，由于导航问题、性能问题和复杂性开销，它在实际场景中表现不佳。

**第三版：深度编排器** - 成功的迭代版本。它结合了原始编排器的简单性和自适应工作流的经验。 主要功能包括：
*   使用TODO队列进行初始完整计划生成。
*   通过任务依赖规范进行记忆和知识提取。
*   执行前的确定性计划验证（依赖性、服务器和代理验证）。
*   使用XML标签的Prompt工程。
*   用于决策（继续、重新计划、停止或强制完成）的简单策略引擎。

主要经验：简单的架构更优越，MCP足以完成各种任务，并且小细节会显著影响代理的性能。 未来计划包括通过MCP进行远程执行、智能工具选择、将记忆表示为MCP资源以及动态模型选择。

---

## 13. 欧盟聊天控制面临少数派阻挠

**原文标题**: Chat Control faces blocking minority in the EU

**原文链接**: [https://twitter.com/TutaPrivacy/status/1966384776883142661](https://twitter.com/TutaPrivacy/status/1966384776883142661)

提供的内容实际上并不包含文章。它看起来像是X（前身为Twitter）的一个片段，表明JavaScript已被禁用，阻止用户访问该网站的内容。该片段中没有关于“欧盟中聊天控制面临少数人反对”的信息。因此，我无法提供关于该假设文章的摘要。该片段仅传达了一个阻止访问X的技术问题。

---

## 14. 我不喜欢曲面屏。

**原文标题**: I don't like curved displays

**原文链接**: [https://blog.danielh.cc/blog/curved](https://blog.danielh.cc/blog/curved)

本文表达了对曲面屏幕的厌恶，认为它们扭曲了大多数媒体的预期观看体验。作者的主要理由围绕着媒体创作中直线透镜的普遍使用。这些透镜将 3D 场景中的直线投影到平坦的 2D 平面上。在平面屏幕上观看此图像可以保留原始直线，并准确地再现预期的视角。

然而，根据作者的说法，曲面屏幕会引入失真。根据直线原理在平面上忠实再现的直线，在曲面上显示时不再是直线。这种偏差改变了预期的视角，最终降低了观看体验。因此，作者更喜欢平面屏幕，因为它们能准确地呈现直线透镜投射的直线，从而带来更忠实于原始图像捕捉的观看体验。

---

## 15. Racintosh Plus – 机架式 Mac Plus

**原文标题**: Racintosh Plus – Rackmount Mac Plus

**原文链接**: [http://www.identity4.com/2025-racintosh-plus/](http://www.identity4.com/2025-racintosh-plus/)

“Racintosh Plus”项目是将1986年 Macintosh Plus 定制成机架式版本，旨在完美融入音乐工作室机架。 创作者的目标是解决原电脑的笨重、老化、发热以及潜在的组件故障问题。

该项目涉及将备用 Macintosh Plus 的逻辑板移植到 1U 机架机箱中。 主要修改包括将电线直接焊接到逻辑板上以降低高度，使用带 Raspberry Pi Zero 的 RGBtoHDMI 转换器以实现现代显示输出，以及采用 BlueSCSI V2 进行内部硬盘驱动器模拟，配置了 2GB 系统驱动器和 512MB 实用程序驱动器。 Floppy Emu 通过 microSD 卡处理软盘模拟，显示器和控制装置位于前面板上。 其他功能包括 CMOS 电池的电池更换套件和一个新的扬声器。

原有的模拟板和 CRT 被移除，并替换为 Mean Well RT-65B 电源。 在 Sketchup 中创建了机架机箱和组件的 3D 模型，以规划布局和安装。 使用 Dremel 工具手动修改了机箱，并 3D 打印了定制的安装硬件。 前面板和后面板最初计划进行激光蚀刻，但由于蚀刻问题，改为使用贴花。

Racintosh Plus 从 SCSI 驱动器映像运行 System 7.1，并使用运行 Mini VMac 的虚拟机进行软件测试和映像创建。 BlueSCSI 提供 Wi-Fi 连接（虽然信号强度有限），并使用 DateFix 补丁来纠正 2020 年的日期错误。 该项目展示了复古计算和现代技术的创造性融合。

---

## 16. D3D12十年

**原文标题**: Ten Years of D3D12

**原文链接**: [https://therealmjp.github.io/posts/ten-years-of-d3d12/](https://therealmjp.github.io/posts/ten-years-of-d3d12/)

本文庆祝 Direct3D 12 (D3D12) 十周年，重点介绍其持续发展，尽管没有重大版本更新，但仍不断推出新的接口、功能和着色器模型。然后深入探讨过去十年中对核心 D3D12 API 的具体补充。

讨论的关键特性包括：

*   **可编程采样点：** 允许自定义 MSAA 子采样位置，适用于软件 VRS 等特定情况。
*   **视图实例化：** 专为 VR 中的立体渲染设计，允许着色器应用特定于视图的矩阵，但可能不如手动实例化。
*   **深度边界测试：** 一项较早的功能，允许在指定边界内进行深度测试，可能适用于延迟渲染或阴影技术。
*   **可变速率着色 (VRS)：** 通过改变每次绘制、图元或图块的着色率来减少像素着色器的工作负载。但是，性能提升可能有限，并且可能需要空间过滤/时间重建。
*   **放宽格式转换：** 通过放宽格式兼容性规则来简化资源视图的创建，从而改进驱动程序优化。
*   **直接写入块压缩格式：** 允许 GPU 直接写入 BC 纹理，无需中间副本。
*   **可写 R9G9B9E5 纹理：** 允许 GPU 写入此共享指数 RGB 格式，可能提供更好的精度。
*   **WriteBufferImmediate 和 OpenExistingHeapFromAddress：** API 通过在命令列表中插入“面包屑”来支持 GPU 调试。
*   **GPU 上传堆：** 允许 CPU 直接访问 VRAM 资源，从而简化数据更新，但仅在启用 ReBAR 的 Windows 11 上可用。
*   **ExecuteIndirect 递增常量：** 提供一个隐式常量缓冲区值，每次绘制/调度都会递增，近似于“DrawID”。
*   **采样器反馈：** 提供有关访问的纹素的信息，适用于稀疏虚拟纹理，但 API 复杂。

---

## 17. Ankit Gupta 加入 YC 担任普通合伙人

**原文标题**: Ankit Gupta Joins YC as General Partner

**原文链接**: [https://www.ycombinator.com/blog/welcome-ankit/](https://www.ycombinator.com/blog/welcome-ankit/)

Y Combinator (YC) 宣布 Ankit Gupta 成为其最新普通合伙人。Gupta 兼具深厚的机器学习专业知识和创业经验，非常适合指导致力于人工智能创新的创始人。他将主要在马萨诸塞州剑桥市办公，重新建立 YC 在该地区的存在。

Gupta 与 YC 的联系始于 2018 年冬季，当时他是 Reverie Labs 的联合创始人，Reverie Labs 是一家利用机器学习进行药物发现的生物技术公司。Reverie 开发了用于小分子设计的机器学习模型，与制药公司合作，并在 2024 年被 Ginkgo Bioworks 收购之前，创建了自己的药物。在 Reverie 之前，Gupta 在哈佛大学学习计算机科学，获得了学士和硕士学位，并发表了关于深度学习的研究。

YC 总裁兼首席执行官 Garry Tan 强调，Gupta 集研究和创始人经验于一身，这是一种罕见的优势，将帮助未来的 AI 初创公司取得成功。YC 很高兴欢迎他，并相信他的专业知识将为 YC 创始人旅程的各个阶段提供宝贵的支持。

---

## 18. Crates.io 网络钓鱼尝试

**原文标题**: Crates.io phishing attempt

**原文链接**: [https://fasterthanli.me/articles/crates-io-phishing-attempt](https://fasterthanli.me/articles/crates-io-phishing-attempt)

针对 crates.io 的网络钓鱼攻击报告

---

## 19. 为什么我们的网站看起来像操作系统

**原文标题**: Why our website looks like an operating system

**原文链接**: [https://posthog.com/blog/why-os](https://posthog.com/blog/why-os)

Cory Watilo 探讨了 PostHog.com 的重新设计，并解释了其不寻常的操作系统式界面。他对许多网站典型的标签页爆炸和重度滚动设计感到沮丧，因此寻求一种更高效、更具吸引力的方式让用户消费内容。新的 PostHog.com 允许同时处理多个文章、演示视频，甚至可以同时访问游戏，实现多任务处理。

重新设计包含了熟悉的操作系统元素，如窗口对齐、键盘快捷键、受 Windows 文件资源管理器启发的周边商店、PowerPoint 风格的产品页面、文档编辑器、Outlook Express 主题的论坛、QuickTime 克隆、电子表格格式的页面、屏幕保护程序和桌面背景。

Watilo 强调了该项目的技术方面，包括将视觉层与内容分离，产品页面由 JSON 文件驱动，这些文件决定布局、内容、竞争对手比较和屏幕截图。最终，这将连接到 PostHog 应用程序，以实现统一的数据源。他还讨论了管理浅色和深色模式的主题和配色方案。

创建了一个参考客户数据库，将客户与产品、报价和徽标联系起来，以便在整个网站上进行动态展示。 Watilo 使用 Typescript 和 Tailwind 直接在生产环境中进行原型设计，从而促进了迭代开发。他最后承认重新设计的 MVP 性质，并邀请用户探索新的 PostHog.com。

---

## 20. 超过100艘船舶使用挪威Ro Marine的假保险航行。

**原文标题**: Over 100 ships have sailed with fake insurance from the Norwegian Ro Marine

**原文链接**: [https://www.nrk.no/vestland/xl/over-100-ships-have-sailed-without-legitimate-insurance-from-the-norwegian-company-ro-marine-1.17565216](https://www.nrk.no/vestland/xl/over-100-ships-have-sailed-without-legitimate-insurance-from-the-norwegian-company-ro-marine-1.17565216)

挪威公司Ro Marine被曝光向100多艘船只提供虚假保险，这些船只主要运送货物，包括俄罗斯石油和武器出境。这种欺诈行为使这些船只能够规避西方制裁，更自由地运营。该计划涉及伪造文件，包括来自巴拿马和挪威金融监管局等船旗国的参考资料和批准。

挪威广播公司（NRK）和文件中心（Dossier Center）进行的调查显示，Ro Marine实际上是在帮助俄罗斯维持石油出口，这对于资助乌克兰战争至关重要。制裁专家大卫·坦南鲍姆（David Tannenbaum）将Ro Marine 描述为服务于从事非法活动和逃避制裁的“影子舰队”的“最坏中的最坏”。与受制裁实体有关的船只，包括俄罗斯天然气巨头诺瓦泰克（Novatek）和伊朗石油工业，都是Ro Marine的客户。

该骗局的幕后主使是安德烈·莫恰林（Andrey Mochalin），一位俄罗斯公民，此前曾在一家合法的挪威保险公司工作。他与两名挪威人和一名保加利亚人一起，被指控犯有伪造罪和经营非法保险业务罪。调查发现了一条通往莫恰林在圣彼得堡的公司的资金线索。虽然Ro Marine 已在挪威被强制解散并受到英国的制裁，但圣彼得堡公司仍然活跃，并且虚假保险证书继续出现。

---

## 21. 浮点数漏洞

**原文标题**: Float Exposed

**原文链接**: [https://float.exposed/](https://float.exposed/)

Bartosz Ciechanowski 的文章《浮点数揭秘》探讨了浮点数 (float) 以及半精度浮点数 (half-float)、Bfloat 和双精度浮点数 (double) 等相关数据类型的复杂性。它以可视化的方式呈现并解释了这些数据类型的结构，可能侧重于如何通过尾数-指数范围内的位模式来表示值。

这篇文章可能解释了这些位模式如何使用以 2 为基数（二进制）的评估转化为数值，然后演示了该二进制表示如何等同于以 10 为基数（十进制）的值。其目的是可视化底层位表示与最终可理解的数字之间通常不透明的关系。

此外，《浮点数揭秘》可能还考察了浮点数表示的局限性，特别是精度的概念。它强调了“精确的十进制值”与表示值之间的差异，可能演示了潜在的舍入误差。通过“到下一个/上一个可表示值的差值”进一步强调了这一点，它说明了围绕给定值的可表示数字的粒度和间距，展示了浮点运算中固有的不精确性。

本质上，这篇文章作为一个互动和教育工具，解构了浮点数的内部工作原理，使位模式、尾数、指数及其对精度的影响等抽象概念更易于理解和掌握。

---

## 22. 天体物理源代码库

**原文标题**: Astrophysics Source Code Library

**原文链接**: [http://ascl.net/](http://ascl.net/)

天体物理源代码库 (ASCL.net) 是一个免费的在线注册库和存储库，用于存储同行评审研究中使用的天体物理源代码。它索引代码并提供唯一的、可引用的 ID，这些 ID 链接到代码条目。

该库的最新添加包括：

*   **adstex:** 通过从 NASA 天体物理数据系统 (ADS) 获取参考信息，从 TeX 源代码自动构建参考书目文件。
*   **IAR\_Model:** 用于拟合来自不规则自回归 (IAR) 模型的不等间距时间序列的 Python 和 R 函数。
*   **fm4ar:** 使用流动匹配后验估计从光谱推断系外行星的大气属性。
*   **AGNI:** 模拟具有岩浆海洋的岩石系外行星的大气结构，确保辐射对流平衡。
*   **FiCUS:** 拟合河外紫外 (UV) 光谱的恒星连续谱以估计星系属性。
*   **pyStarburst99:** Starburst99 星族合成代码的 Python 版本。
*   **SIGWAY:** 计算早期宇宙中曲率扰动发出的二阶标量诱导引力波信号。
*   **sMV:** 提供用于串行多视图相位平面估计的工作流程。
*   **DeepSSM:** 使用神经网络模拟引力波 (GW) 频谱。
*   **HipFT:** 在太阳表面实施平流、扩散和数据同化，并构成开源通量输运 (OFT) 软件套件的计算核心。

---

## 23. 显示 HN：一个 MCP 网关，用于阻止致命的三重威胁

**原文标题**: Show HN: An MCP Gateway to block the lethal trifecta

**原文链接**: [https://github.com/Edison-Watch/open-edison](https://github.com/Edison-Watch/open-edison)

OpenEdison是一个安全的MCP（托管计算提供商）网关，旨在防止在将AI连接到敏感数据和软件时发生的数据泄露和代理劫持。它解决了AI风险的“致命三要素”：私有数据访问、不受信任的内容暴露和外部通信。

主要特性包括：

*   **数据泄露拦截器：** 自动拦截数据泄露，即使AI已被越狱。
*   **确定性执行：** 保证数据泄露预防。
*   **轻松配置：** 简化MCP服务器的管理。
*   **可见性：** 通过MCP调用跟踪AI代理与连接系统的交互。
*   **简单API和Docker支持：** 用于管理的REST API和容器化部署。

Edison使用基于访问控制级别（ACL）的可配置安全分类来监视和控制对工具、资源和提示的访问。它跟踪每个会话的最高ACL级别，并阻止写入较低ACL级别的操作。

该系统利用 `tool_permissions.json`、`resource_permissions.json` 和 `prompt_permissions.json` 来定义安全分类，并允许使用通配符模式进行更广泛的定义。

`get_security_status` 工具允许监控会话风险级别。当所有三个“致命三要素”风险标志都被设置时，潜在的危险操作将被阻止。

该产品可通过多种安装方法获得，包括直接脚本执行、PyPI和Docker，并提供设置说明。还提供全面的文档和GPL-3.0许可。

---

## 24. Debian 13、Postgres 和美国时区

**原文标题**: Debian 13, Postgres, and the US time zones

**原文链接**: [https://rachelbythebay.com/w/2025/09/11/debtz/](https://rachelbythebay.com/w/2025/09/11/debtz/)

好的，我阅读了来自 rachelbythebay.com 的文章《Debian 13、Postgres 和美国时区》。

以下是摘要：

该文章讨论了 Debian 13 中与处理美国时区名称相关的潜在问题，特别是与 PostgreSQL 相关的问题。作者预计 Debian 13 可能会更改时区的命名和表示方式，从而可能导致与 PostgreSQL 存储和检索时区信息的方式不一致。

核心问题在于使用完整、长格式的时区名称（如“America/Los_Angeles”）与较短、通常含糊不清的缩写（如“PST”或“PDT”）之间的差异。PostgreSQL 通常依赖于长格式名称。作者担心 Debian 13 对 `tzdata` 包（包含时区信息）的更改可能会无意中导致 PostgreSQL 误解或无法识别数据库中现有的时区数据，如果系统默认使用缩写或其他命名约定。

这种潜在的不兼容性可能导致数据损坏、不正确的日期/时间计算，以及依赖于 PostgreSQL 中准确时区处理的应用程序发生故障。作者提前提出这个问题，希望提醒 Debian 和 PostgreSQL 开发人员注意潜在问题，以便他们可以在 Debian 13 发布之前进行调查并实施缓解策略。文章建议需要仔细考虑和测试，以确保平稳过渡并避免破坏现有的 PostgreSQL 安装和依赖于准确时区信息的应用程序。简而言之，这篇文章是对 Debian 13 的 Postgres 用户可能面临的时区末日的警告。

---

## 25. 公司正试图（但现在失败了）对美国公民隐藏职位空缺。

**原文标题**: Corporations are trying, and now failing, to hide job openings from US citizens

**原文链接**: [https://thehill.com/opinion/finance/5498346-corporate-america-has-been-trying-to-hide-job-openings-now-it-is-failing/](https://thehill.com/opinion/finance/5498346-corporate-america-has-been-trying-to-hide-job-openings-now-it-is-failing/)

《国会山报》的文章认为，公司一直在试图向美国公民隐藏职位空缺，以便用H-1B签证雇佣外国工人来填补这些职位，而且通常工资较低。作者认为，这种策略使公司能够压低工资并削弱美国工人的议价能力。

文章指出，公司现在发现越来越难以隐藏这些职位空缺。 这是因为对职位发布的审查力度加大和追踪技术的改进，揭露了专门针对外国工人或发布有效排除合格美国申请人的要求的做法。 作者认为，这种更高的透明度使得公司更难证明聘用外国工人而非合格的美国公民是合理的。

文章还认为，这种做法通过压低工资和取代国内工人来损害美国经济。 作者暗示，需要更高的透明度和更严格的移民法执行力度，以确保美国公民能够公平地获得就业机会，并防止公司利用H-1B签证计划人为地降低劳动力成本。 该文章倡导优先考虑美国工人并保护他们免受不公平竞争的政策。

---

## 26. VaultGemma：最强大的差分隐私LLM

**原文标题**: VaultGemma: The most capable differentially private LLM

**原文链接**: [https://research.google/blog/vaultgemma-the-worlds-most-capable-differentially-private-llm/](https://research.google/blog/vaultgemma-the-worlds-most-capable-differentially-private-llm/)

VaultGemma 是一款 10 亿参数的开源语言模型，从头开始使用差分隐私 (DP) 训练而成，是同类模型中规模最大的。它由 Google Research 与 Google DeepMind 合作开发。该模型的发布旨在推进隐私保护型人工智能的发展。

VaultGemma 背后的研究建立了 DP 语言模型的全新“缩放法则”，这些法则对计算、隐私和效用之间的权衡进行了建模。一个关键发现是，对于 DP 模型而言，更小的模型尺寸和更大的批处理规模比传统的非 DP 训练方法更有效。

VaultGemma 演示了这些缩放法则的实际应用。它使用这些原则和先进的算法进行训练，包括“可扩展的 DP-SGD”，以应对泊松抽样带来的挑战，而泊松抽样是 DP-SGD 的关键组成部分。

性能基准测试表明，VaultGemma 实现了与大约五年前的非私有模型相当的效用，突显了当前隐私所需的资源投入。该模型提供序列级别的 DP 保证（ε ≤ 2.0，δ ≤ 1.1e-10），这意味着包含在单个 1024 个 token 序列中的信息对模型输出的影响有可证明的限制。实证测试表明，VaultGemma 没有表现出对其训练数据的可检测记忆。研究人员希望 VaultGemma 及其缩放法则能够推动安全、负责任和私有 AI 的进一步发展。

---

## 27. Nyquist 和 Lisp 编程入门

**原文标题**: Introduction to Nyquist and Lisp Programming

**原文链接**: [https://manual.audacityteam.org/man/introduction_to_nyquist_and_lisp_programming.html](https://manual.audacityteam.org/man/introduction_to_nyquist_and_lisp_programming.html)

本文介绍Nyquist和Lisp编程，特别是在Audacity插件开发背景下。 Nyquist专为音频合成和分析设计，使用Lisp语法（新版Audacity中可以选择使用SAL）。

本文强调Lisp的S-表达式结构，其中一切都是带括号的标记列表，函数名位于最前面。它解释了如何使用`defun`定义函数，使用`setf`赋值，以及如何使用前缀表示法进行数学运算。在使用列表时，使用`'`进行引用以防止求值至关重要。列表操作涵盖了诸如`first`、`rest`和`list`等函数。

本文提供了一个常见的Lisp/SAL函数表，包括数学函数（+, -, *, /, truncate, float, rem, min, max, abs, random, rrandom, sin, cos, tan, expt, sqrt, 比较运算符），列表函数（first, rest, reverse, list, append, length, maplist）和条件表达式（if, when, unless, cond, case）。示例演示了如何在Lisp和SAL语法中使用这些函数。

本文引导读者查阅可用的Nyquist手册，特别指出基于Lisp的2.37版本和以SAL为重点的3.1x版本。它可以作为在Audacity中开发Nyquist插件的起点。

---

## 28. 经典 GTK1 GUI 库

**原文标题**: Classic GTK1 GUI Library

**原文链接**: [https://gitlab.com/robinrowe/gtk1](https://gitlab.com/robinrowe/gtk1)

文章《经典GTK1 GUI库》正在加载中，因此无法提供有意义的摘要。由于文章的实际内容不可用，摘要需要理解文章文本中的主要观点、关键信息和论点，而这些目前都不存在。

---

## 29. Show HN: 我用 ClojureScript 做了一个生成式在线鼓机

**原文标题**: Show HN: I made a generative online drum machine with ClojureScript

**原文链接**: [https://dopeloop.ai/beat-maker/](https://dopeloop.ai/beat-maker/)

“Show HN”：Beat Maker – dopeloop.ai出品的在线鼓机

---

## 30. OpenAI 格罗夫

**原文标题**: OpenAI Grove

**原文链接**: [https://openai.com/index/openai-grove/](https://openai.com/index/openai-grove/)

OpenAI Grove是一个致力于理解和改善人工智能长期社会影响的项目。它涉及创建一个模拟的、交互式的环境，供研究人员探索人工智能与人类系统和机构之间复杂的相互作用。其目标是在潜在风险、意外后果和先进人工智能的有益应用在现实世界中显现之前就识别出来。

该环境允许研究人员试验不同的人工智能模型和政策，观察它们对经济、信息生态系统和社会动态等各种社会方面的影响。这使得能够采取积极的缓解策略，并就人工智能的开发和部署做出明智的决策。

Grove旨在促进跨学科合作，汇集来自人工智能、经济学、政治学和社会学领域的专家，以促进对人工智能影响的整体理解。通过提供一个共享的实验和分析平台，Grove力求加速负责任和有益的人工智能技术的发展。

关键特性包括模块化设计，允许研究人员专注于特定的兴趣领域；由真实世界数据和见解驱动的数据驱动型模拟；以及对结果的透明度和可重复性的强调。最终，OpenAI Grove代表着朝着确保人工智能通过以受控和严谨的方式预测和解决潜在挑战，从而使整个社会受益迈出的重要一步。

---

## 31. Lumina-DiMOO：一种开源的离散多模态扩散模型

**原文标题**: Lumina-DiMOO: An open-source discrete multimodal diffusion model

**原文链接**: [https://synbol.github.io/Lumina-DiMOO/](https://synbol.github.io/Lumina-DiMOO/)

Lumina-DiMOO：用于多模态生成和理解的新型开源基础模型

---

## 32. 使用Emacs Org-Mode连接数据库入门指南

**原文标题**: Using Emacs Org-Mode With Databases: A getting-started guide

**原文链接**: [https://gitlab.com/ryanprior/emacs-org-data-starter](https://gitlab.com/ryanprior/emacs-org-data-starter)

文章标题“使用 Emacs Org-Mode 连接数据库：入门指南”正在加载中，目前没有内容可供总结。

---

## 33. 《LaTeX Companion》（第三版）书中的示例

**原文标题**: Examples from The LaTeX Companion book (3rd edition)

**原文链接**: [https://ctan.org/pkg/tlc3-examples](https://ctan.org/pkg/tlc3-examples)

本文介绍了CTAN上的“tlc3-examples”软件包。该软件包包含《The LaTeX Companion》第三版（第一部分和第二部分）一书中所有示例的LaTeX源代码和必要的支持文件，该书由Addison-Wesley于2023年出版（ISBN-13: 978-0-13-816648-9, ISBN-10: 0-13-816648-X）。它还包括用于专色和裁剪的PDF文件。该软件包由Frank Mittelbach维护，并根据LaTeX Project Public License 1.3c获得许可。可以下载zip压缩包（82.4M），并且也包含在TeX Live中。本文提供了软件包的错误跟踪器和存储库的链接，并推荐了包含其他LaTeX书籍示例的相关软件包。总而言之，该软件包为《The LaTeX Companion》的读者提供了一个实践性的资源，可以用来实验和学习书中的示例。

---

## 34. Claude的记忆架构与ChatGPT相反。

**原文标题**: Claude’s memory architecture is the opposite of ChatGPT’s

**原文链接**: [https://www.shloked.com/writing/claude-memory](https://www.shloked.com/writing/claude-memory)

本文对比了Claude和ChatGPT的记忆架构，突出了它们截然相反的方法。Claude采用了一种白板方法，只有在通过“我们讨论了什么”等命令显式调用时才会激活记忆。它通过使用两种工具：`conversation_search`（基于关键词/主题）和`recent_chats`（基于时间）来搜索原始、未概括的对话历史记录，从而检索信息。这种方法赋予用户直接的控制和可预测性，并将准确性置于便利性之上。

相反，ChatGPT会自动加载所有记忆组件，从而创建即时个性化。它无需用户显式输入即可构建详细的用户档案并学习偏好。这旨在实现无缝、"神奇"的用户体验。

这种差异反映了不同的目标受众。ChatGPT面向寻求易用性和个性化体验的广泛消费者群体。Claude面向技术用户，如开发者和研究人员，他们重视在专业工作流程中的控制、透明性和可预测性，并且愿意为此牺牲一些便利性。

作者强调，设计AI记忆没有唯一的“正确”方法，理想的方法在很大程度上取决于用户的需求和优先级。AI记忆设计空间广阔，目前的方法仅仅是一个不断发展的领域的开端。作者计划继续剖析不同的记忆架构，并在该领域发展时分享更新，并指出Anthropic已更新其功能，使其更接近ChatGPT的记忆特性。

---

## 35. 按门铃恶作剧骚扰公寓居民的元凶竟是一只蛞蝓

**原文标题**: Doorbell prankster that tormented residents of apartments turns out to be a slug

**原文链接**: [https://www.theguardian.com/world/2025/sep/08/doorbell-prankster-that-tormented-residents-of-german-apartments-turns-out-to-be-a-slug](https://www.theguardian.com/world/2025/sep/08/doorbell-prankster-that-tormented-residents-of-german-apartments-turns-out-to-be-a-slug)

德国巴伐利亚一栋公寓楼的居民一直饱受深夜门铃骚扰之苦。起初他们怀疑是青少年恶作剧，即所谓的“klingelstreich”（按门铃逃跑），于是报警调查。令他们惊讶的是，罪魁祸首不是人，而是一只蛞蝓。

这只蛞蝓在金属门铃面板上滑动，反复触发门铃。持续不断的铃声扰乱了居民的睡眠，引起了极大的 frustration。即使警察赶到后，发现门前没有人，运动探测器也没有反应，铃声仍然继续，这使得他们最终发现了蛞蝓以及它在门铃面板上的黏液痕迹。

一位居民丽莎回忆说，门铃在晚上10点后开始响，她楼上的嫂子也遇到了同样的问题。他们无法确定铃声的来源，这让他们感到不安，于是报警。警方确认罪魁祸首是蛞蝓。据警方发言人称，这只蛞蝓随后被“制服，接受了关于其领地边界的教育，并被放置在附近的一片草地上”，从而有效地结束了它的门铃恐怖统治。

---

## 36. 成为那个做事的人

**原文标题**: Becoming the person who does the thing

**原文链接**: [https://www.fredrivett.com/2025/09/10/becoming-the-person-who-does-the-thing/](https://www.fredrivett.com/2025/09/10/becoming-the-person-who-does-the-thing/)

无法访问文章链接。

---

## 37. 英国启动“章鱼计划”，向乌克兰交付拦截无人机。

**原文标题**: UK launches Project Octopus to deliver interceptor drones to Ukraine

**原文链接**: [https://www.shephardmedia.com/news/air-warfare/dsei-2025-uk-launches-project-octopus-to-deliver-thousands-of-interceptor-drones-to-ukraine/](https://www.shephardmedia.com/news/air-warfare/dsei-2025-uk-launches-project-octopus-to-deliver-thousands-of-interceptor-drones-to-ukraine/)

英国启动“章鱼计划”大规模生产乌克兰拦截无人机并供应乌克兰对抗俄罗斯无人机。该项目在2025年英国国防与安全装备展上发布，是一项合作计划，乌克兰将其高效、低成本拦截无人机的技术分享给英国。作为回报，英国将迅速开发并大规模生产这些无人机，每月向乌克兰运送数千架。

据英国国防大臣约翰·希利称，这些乌克兰设计的无人机在对抗伊朗制造的“沙赫德”无人机方面非常有效，成本仅为被摧毁的俄罗斯系统价值的不到10%。

此前，乌克兰无人机制造商UKRSPECSYSTEMS已向英国的两个新设施投资了2亿英镑。此外，其他英乌无人机合作项目也在涌现，包括Prevail Partners（英国）和Skyeton（乌克兰）之间的合资企业，用于生产Raybird无人机，可能用于英国的“渡鸦计划”以取代“守望者”无人机。

---

## 38. 司法部宣布打击朝鲜远程IT工作者的行动

**原文标题**: Justice Department Announces Actions to Combat North Korean Remote IT Workers

**原文链接**: [https://www.justice.gov/opa/pr/justice-department-announces-coordinated-nationwide-actions-combat-north-korean-remote](https://www.justice.gov/opa/pr/justice-department-announces-coordinated-nationwide-actions-combat-north-korean-remote)

司法部宣布了一项协调一致的全国行动，打击朝鲜利用远程IT工作者为朝鲜政权非法创收、资助其武器项目的阴谋。这些行动包括起诉、逮捕、认罪协议、搜查16个州的“笔记本电脑农场”以及查封金融账户和欺诈网站。

朝鲜个人在美国境内人士、中国、阿联酋和台湾地区人士的协助下，使用盗用和虚假身份，以欺诈手段获得美国公司的工作。一些美国境内人士创建幌子公司并设立“笔记本电脑农场”来促成此事。一旦受雇，朝鲜IT工作者就会获得薪水、访问敏感数据，有时还会窃取数据，包括受出口管制的军事技术和虚拟货币。其中一项阴谋涉及从一家位于佐治亚州的区块链公司窃取超过90万美元的虚拟货币。

行动包括在新泽西州逮捕王振星（Zhenxing "Danny" Wang），他实施了一项多年欺诈计划，获利超过500万美元。四名朝鲜国民在佐治亚州被指控盗窃和洗钱虚拟货币。联邦调查局搜查了14个州的21个可疑“笔记本电脑农场”，查获约137台笔记本电脑。

司法部已多次宣布关于“朝鲜创收：国内促成者倡议”（DPRK RevGen: Domestic Enabler Initiative）的消息。联邦调查局和其他机构已发布关于朝鲜IT工作者以欺诈手段获得工作的公共服务公告和建议。

---

## 39. 美国目前在监控软件投资方面领先世界。

**原文标题**: America now leads the world in surveillanceware investment

**原文链接**: [https://www.theregister.com/2025/09/11/us_surveillanceware_investment/](https://www.theregister.com/2025/09/11/us_surveillanceware_investment/)

美国已成为监控软件投资的世界领导者，这是一个在伦理上存疑但利润丰厚的计算机监控软件领域。大西洋理事会的一份报告显示，美国的投资激增，超过了所有其他国家。这种增长令人担忧，因为它破坏了美国政府通过“帕尔马尔进程”等举措来监管间谍软件市场的努力。

该报告强调了总部位于美国的实体在投资和转售监控软件方面的增长，甚至涉及先前受到制裁或限制的公司。例如，在一家拥有美国移民及海关执法局（ICE）间谍软件合同的公司Paragon Solutions被一家美国公司收购后，停工令被解除，允许合同恢复。同样，一家美国公司收购了Saito Tech Ltd，该公司开发Candiru监控软件工具，尽管该公司已被列入美国商务部的实体清单。

大西洋理事会强调了一个矛盾：美国政府限制间谍软件市场的努力正在被国内对同一技术的投资所破坏。经销商的日益使用进一步使监管复杂化。该报告警告说，这种矛盾正在削弱美国在该问题上的领导地位，并敦促美国政府解决政策与行业投资之间的这种不平衡。

---

## 40. 搭建我的童年梦想电脑

**原文标题**: Building my childhood dream PC

**原文链接**: [https://fabiensanglard.net/2168/](https://fabiensanglard.net/2168/)

Fabien Sanglard追忆童年梦想：拥有一台1993年的顶级PC——IBM PS/1 2168，这源于他对当时拥有的低端Cyrix 486SLC的失望。因无力负担昂贵的IBM，他在2024年踏上了一段寻觅并修复它的旅程。

文章详细描述了他对IBM PS/1 2168设计的赞赏，突出了其迷你塔式机箱带把手、圆角、巧妙隐藏的驱动器以及通常附带的高品质Model M键盘等特点。他还提到，与兼容机相比，PS/1拥有全面的文档和可升级性。

Sanglard描述了寻找一台功能完好的2168的困难，尤其是要找到一台33Mhz型号以获得最佳性能。他最终在芬兰找到了一台DX2-66Mhz版本，连同原装包装盒和说明书，并协商达成购买协议。文章结尾充满了对开箱过程的期待，并预告了未来的文章将记录这台复古PC的修复和升级过程，最终目标是流畅运行DOOM。文章的剩余内容将在系列博文中提供。

---

## 41. 如果以色列参赛，荷兰将与爱尔兰一起抵制2026年欧洲歌唱大赛。

**原文标题**: Netherlands joins Ireland will boycott 2026 Eurovision if Israel participates

**原文链接**: [https://nltimes.nl/2025/09/12/netherlands-will-boycott-2026-eurovision-israel-participates-says-broadcaster](https://nltimes.nl/2025/09/12/netherlands-will-boycott-2026-eurovision-israel-participates-says-broadcaster)

荷兰广播公司AVROTROS宣布，如果以色列参加，荷兰将抵制在维也纳举行的2026年欧洲歌唱大赛。这使得荷兰成为继冰岛、斯洛文尼亚、西班牙和爱尔兰之后，第五个宣布计划抵制的国家。

AVROTROS将原因归咎于“加沙持续而严重的人道苦难”，并表示他们无法再为以色列在当前局势下的参与辩护。该公司还对“新闻自由的严重侵蚀”表示担忧，并提到了据称以色列政府干预上届赛事的情况。

该广播公司强调，他们已经与欧洲广播联盟（EBU）讨论了此事。多年来，以色列的参与一直备受争议。值得注意的是，这并非荷兰首次威胁退出欧洲歌唱大赛；AVROTROS曾考虑退出2025年的比赛，原因是2024年赛事中存在不安全环境的报道，这导致了Joost Klein被取消资格。

---

## 42. 幼儿机器人：开源人形机器人

**原文标题**: Toddlerbot: Open-Source Humanoid Robot

**原文链接**: [https://toddlerbot.github.io/](https://toddlerbot.github.io/)

ToddlerBot项目：低成本开源人形机器人平台，旨在促进可扩展策略学习，并推进机器人和人工智能领域的研究。其开源特性使研究人员和开发者能够访问和修改设计，从而促进合作并加速创新。该机器人的经济性使其能够被更广泛的研究人员使用，从而可能实现机器人研究的民主化并进行更大规模的实验。对可扩展策略学习的关注表明，ToddlerBot旨在为开发和测试能够推广并适应新情况的AI算法提供物理平台。这对于创建能够学习复杂任务并与现实世界有效互动的机器人至关重要。最终，ToddlerBot的目标是通过提供一种易于获取和适应性强的探索和实验工具，为机器人和人工智能的进步做出贡献。

---

## 43. 中国将于2027年起禁止默认单踏板模式

**原文标题**: China bans one-pedal driving in default modes by 2027

**原文链接**: [http://www.asiaict.com/icv/10236.html](http://www.asiaict.com/icv/10236.html)

本文探讨了中国即将于2027年1月1日生效的关于电动汽车“单踏板模式”的法规。这项新的国家标准规定，在默认操作条件下，松开加速踏板不能使车辆完全停止，从而有效地限制了单踏板模式。虽然并非完全禁止，但该法规要求用户主动选择单踏板模式，并且车辆在激活此模式时必须提供清晰的视觉警告。

本文解释了A型和B型再生制动之间的区别，并阐明该法规主要针对单踏板模式的动能回收方面，该方面可以在不使用制动踏板的情况下使汽车完全停止。

这些法规是对安全问题的回应，包括驾驶员将加速踏板误认为制动踏板的报告，以及研究表明习惯于单踏板驾驶的驾驶员的反应时间增加。推广该模式的特斯拉，也因此问题面临审查和召回。

除了单踏板驾驶之外，新标准还规定，当再生制动减速度超过1.3米/秒²时，制动灯必须亮起，从而提高后方车辆的安全性。此外，所有新认证的乘用车车型都必须强制安装ABS（防抱死制动系统）。这些法规旨在平衡动能回收的益处与增强驾驶员和道路安全。

---

## 44. Bun 安装幕后

**原文标题**: Behind the scenes of Bun Install

**原文链接**: [https://bun.com/blog/behind-the-scenes-of-bun-install](https://bun.com/blog/behind-the-scenes-of-bun-install)

本文深入探讨了 Bun 相比 npm、pnpm 和 yarn 在软件包安装速度上显著更快的背后原因。它认为，现代硬件能力已经超越了传统基于 Node.js 的软件包管理器以 I/O 为中心的优化。现在的瓶颈在于系统调用，即程序与操作系统内核之间的通信。

Bun 通过将软件包安装视为一个系统编程问题来解决这个问题。Bun 使用 Zig 编写，绕过了 Node.js 软件包管理器中固有的 JavaScript 引擎开销，从而能够直接进行系统调用。 这大大减少了系统调用，并消除了 Node.js 中涉及 libuv 和线程池的复杂文件读取管道。 基准测试表明 Bun 具有卓越的文件处理速度。

此外，Bun 还采用了诸如在 macOS 上使用 Apple 的私有 API 进行异步 DNS 解析和二进制清单缓存等优化。 Bun 不像传统方法那样将清单存储为 JSON，每次安装都需要解析，而是使用二进制格式，从而通过避免重复字符串存储来减少解析开销和内存使用。 这带来了更快的比较速度和整体性能的提高。 futex 调用次数的减少也表明线程同步更加高效，避免了延迟。 最终，软件包管理器利用了特定于操作系统的优化并最大限度地减少了系统调用，从而实现了更快的安装时间。

---

## 45. Adam (YC W25) 招贤纳士，共筑CAD未来

**原文标题**: Adam (YC W25) Is Hiring to Build the Future of CAD

**原文链接**: [https://www.ycombinator.com/companies/adam/jobs/q6td4uk-founding-engineer](https://www.ycombinator.com/companies/adam/jobs/q6td4uk-founding-engineer)

Adam (Y Combinator W25 公司) 正在招聘一位创始工程师，利用人工智能构建 CAD 的未来。他们的目标是通过人工智能彻底改变工程师与 CAD 的交互方式，使他们能够将物理对象变为现实。

该职位涉及开发新的 AI 驱动的 CAD 界面，设计和部署完整功能，并与产品团队合作创造无缝的应用体验。Adam 正在寻找具有卓越工程技能、对模型和设计充满热情，并且能够端到端解决问题的人。

面试过程包括编码挑战、与 CEO 和创始工程师的对话，以及现场带薪工作试用。

Adam 正在构建最先进的文本到 CAD 界面，此前他们成功地推出了 YC 产品，并推出了首款通过 AI 使 CAD 易于访问的产品。现在，他们专注于增强工程师创建与行业标准软件兼容的复杂模型的能力。公司由一支由工程师、设计师和研究人员组成的小团队组成，他们对 CAD 和构建事物充满热情。创始人经验丰富，拥有加州大学伯克利分校和主要人工智能初创公司的背景。

该职位为全职，位于旧金山，提供 16 万美元至 25 万美元的薪资，以及 1.00% 至 2.00% 的股权。所需的技能包括 Next.js、JavaScript、React、TypeScript、Python 和 SQL。Adam 正在寻找具有至少 1 年经验的美国公民/签证持有者。

---

## 46. 34岁男子牙齿植入眼球恢复视力

**原文标题**: Man, 34, has tooth implanted in eye to restore his vision

**原文链接**: [https://www.today.com/health/men-s-health/tooth-in-eye-surgery-restores-vision-rcna230395](https://www.today.com/health/men-s-health/tooth-in-eye-surgery-restores-vision-rcna230395)

34岁的布伦特·查普曼通过一种罕见的“牙齿入眼”手术，矫正了严重的角膜盲症，重获视力。 查普曼在13岁时因服用布洛芬后患上史蒂文斯-约翰逊综合征，导致右眼失明。 由于损伤严重，多次角膜移植均告失败。

牙齿入眼手术，即骨牙角膜移植术，包括取出患者的牙齿（查普曼的情况是上犬齿），进行塑形，并在其中植入晶体。 然后，将这种牙齿-晶体结构植入患者的面颊下约3个月，以便组织在其周围生长。 最后，将该结构通过手术连接到受损的眼睛，为视网膜提供一个清晰的窗口。 身体会接受这颗牙齿，因为它将其识别为自身的组织，从而防止排斥。

手术后，查普曼的视力提高到20/40或20/30。 他现在可以阅读、不用拐杖走路，并再次打篮球。 这项手术被认为改变了他的人生，使他20年来首次可以进行眼神交流。 虽然他在30年后保持目前视力水平的几率为50%，但研究表明，从长远来看，晶体保持功能的成功率很高。 查普曼是加拿大首批接受这种手术的人之一。 迈阿密的巴斯科姆·帕尔默眼科研究所是美国唯一一家进行该手术的中心。

---

## 47. 在 SQLite 上运行 Rails：导致服务中断的新方法

**原文标题**: Rails on SQLite: new ways to cause outages

**原文链接**: [https://andre.arko.net/2025/09/11/rails-on-sqlite-exciting-new-ways-to-cause-outages/](https://andre.arko.net/2025/09/11/rails-on-sqlite-exciting-new-ways-to-cause-outages/)

André Arko 的演讲《Rails on SQLite：引发故障的新方式》探讨了在现代 Rails 应用程序中使用 SQLite 的优势和陷阱。借助 Rails 8 的 Solid Cable、Cache 和 Queue，SQLite 通过消除对独立数据库、Redis 和文件存储服务的需求来简化部署。

核心区别在于 SQLite 是进程内的——数据库是一个由 Web 服务器直接访问的单个文件，消除了连接错误。然而，这带来了挑战：数据库必须驻留在持久存储（EBS、卷）中，以避免重启期间的数据丢失。所有数据（模型、缓存、作业）都驻留在这个单个文件中，简化了管理，但也可能导致争用。

扩展需要纵向扩展（更大的服务器），而不是横向扩展（更多的 VM）。SQLite 的默认锁定机制会创建队列，这可以通过预写日志 (WAL) 来解决，但 WAL 引入了需要协调备份的多个文件。为 ActiveRecord、缓存、作业，甚至 ActiveStorage 使用单独的 SQLite 数据库可以缓解争用。极端的碎片化（每个客户一个数据库）也是一种可能性。

单服务器架构意味着如果服务器发生故障会停机，并且需要基于代理的负载平衡。Sequel 和 DuckDB 等工具可以促进数据库迁移。存在地理限制，尽管 CDN 仍然可以改善内容交付。

对于备份和复制，Litestream 将预写日志条目流式传输到与 S3 兼容的存储，从而实现数据库恢复。LiteFS 提供使用基于 FUSE 的文件系统的完整复制，但引入了诸如陈旧读取和潜在数据丢失等注意事项。

---

## 48. 防弹主机斯塔克工业避开欧盟制裁

**原文标题**: Bulletproof host Stark Industries evades EU sanctions

**原文链接**: [https://krebsonsecurity.com/2025/09/bulletproof-host-stark-industries-evades-eu-sanctions/](https://krebsonsecurity.com/2025/09/bulletproof-host-stark-industries-evades-eu-sanctions/)

本文详细介绍了防弹主机提供商斯塔克工业（Stark Industries）如何规避欧盟于2025年5月实施的制裁。斯塔克工业是与克里姆林宫有关联的网络攻击和虚假信息的已知来源。欧盟制裁了PQ Hosting及其所有者Neculiti兄弟，他们是斯塔克工业连接互联网的主要渠道，因为他们支持俄罗斯的混合战争。

然而，斯塔克工业预料到了制裁，并更名为the[.]hosting，由荷兰实体WorkTitans BV管理。Neculiti兄弟还将资产转移到了PQ Hosting Plus S.R.L.，这是一家与他们有关联的摩尔多瓦新公司。

该报告强调了MIRhosting的参与，MIRhosting是另一家位于荷兰的主机提供商，由Andrey Nesterenko运营。MIRhosting在2024年被确定为斯塔克网络的重要支柱，并且似乎是斯塔克工业的新家。MIRhosting的员工管理着the[.]hosting和WorkTitans。

WorkTitans BV以Misfits Media和WT Hosting的名义开展业务，由Youssef Zinad创立，通过LinkedIn活动和之前与Nesterenko的沟通，Youssef Zinad与MIRhosting有关联。Zinad也被列为the[.]hosting的创始人，该网站由PQ Hosting Plus S.R.L.托管。

文章总结称，欧盟的制裁并未奏效，因为斯塔克的基础设施仍然在运行，服务在新的品牌下迅速重建，并且所有权被混淆。

---

## 49. D3D12十年

**原文标题**: Ten Years of D3D12

**原文链接**: [https://therealmjp.github.io/posts/ten-years-of-d3d12/](https://therealmjp.github.io/posts/ten-years-of-d3d12/)

本文回顾了Windows 10发布以来Direct3D 12 (D3D12)的十年历程。D3D12是历时最长的主版本，并获得了多次更新，包括DXR和Work Graphs等重要功能，以及较小的增强功能和HLSL更新。

接下来，本文深入探讨了D3D12 API的核心新增功能：

*   **可编程采样点:** 允许自定义MSAA子采样位置，适用于特殊情况和软件VRS。
*   **视口实例化:** 通过实例化绘制并向着色器提供视图ID，从而促进VR/3D的立体渲染。
*   **深度范围测试:** 允许设置像素深度测试的深度范围，适用于较旧的延迟渲染技术。
*   **可变速率着色 (VRS):** 通过改变每个绘制、图元或瓦片的着色率来减少像素着色器线程数。
*   **放宽格式转换:** 创建纹理的多个兼容视图时，不再需要TYPELESS格式。
*   **直接写入块压缩格式:** 允许通过UAV直接写入BC格式纹理，从而消除中间复制。
*   **可写R9G9B9E5纹理:** 允许GPU通过RTV或类型化的UAV直接写入R9G9B9E5格式，在特定情况下可能提供比R11G11B10更高的精度。
*   **WriteBufferImmediate和OpenExistingHeapFromAddress:** 用于在GPU崩溃时收集调试信息（“面包屑”）的API。
*   **GPU上传堆:** 利用Resizable BAR，允许CPU直接更新VRAM中的资源，而无需GPU复制。
*   **ExecuteIndirect递增常量:** 为每次绘制或分派向着色器提供隐式递增的常量缓冲区值。
*   **采样器反馈:** 允许开发者确定访问了哪些纹素，适用于稀疏虚拟纹理。

文章指出了一些功能的复杂性和局限性，以及不同硬件厂商对这些功能的支持情况。

---

## 50. 基因编辑的胰腺细胞移植到一名1型糖尿病患者体内

**原文标题**: Gene-edited pancreatic cells transplanted into a patient with type 1 diabetes

**原文链接**: [https://www.wired.com/story/no-more-injections-crispr-offers-new-hope-for-treating-diabetes/](https://www.wired.com/story/no-more-injections-crispr-offers-new-hope-for-treating-diabetes/)

基因编辑胰腺细胞植入为1型糖尿病治疗带来希望

---

## 51. 从一次性手机到纸牌：纽约青少年适应智能手机禁令

**原文标题**: From burner phones to decks of cards: NYC teens adjusting to the smartphone ban

**原文链接**: [https://gothamist.com/news/from-burner-phones-to-decks-of-cards-nyc-teens-are-adjusting-to-the-smartphone-ban](https://gothamist.com/news/from-burner-phones-to-decks-of-cards-nyc-teens-are-adjusting-to-the-smartphone-ban)

纽约青少年如何适应学校智能手机禁令：学生们正寻找应对“失联”的创造性方法，包括使用拍立得相机、对讲机、纸牌甚至晶体管收音机。一些人开始使用旧技术如“数码相机”和MP3播放器。禁令似乎鼓励了更多的社交和面对面交流，走廊和餐厅也变得更加热闹。

尽管有禁令，一些学生仍在寻找替代方案，例如使用“假手机”、通过Google Docs交流以及在校外休息时使用手机。市长亚当斯认为这些努力是青少年“创造精神”的一部分。

学校正在采取各种策略，例如收缴手机或使用磁性袋，但这导致了排长队和学生上课迟到等问题。虽然一些学生担心禁令会影响大学申请等活动，但另一些人则认识到它在减少手机成瘾和提高参与度方面的潜在好处。总的来说，本文描绘了对禁令的复杂反应，学生和教育工作者都观察到了积极和消极的后果，并以不同的方式进行适应。

---

## 52. XFN – XHTML 朋友网络 (2003)

**原文标题**: XFN – XHTML Friends Network (2003)

**原文链接**: [https://gmpg.org/xfn/](https://gmpg.org/xfn/)

XFN (XHTML 友人网络) 是一种直接的方法，于2003年引入，用于通过网络上的超链接表示人际关系。 XFN 主要用于博客链接，允许网站作者通过向 `<a href>` 标签添加 "rel" 属性来定义与链接个人的关系，例如 `<a href="http://jeff.example.org" rel="friend met">`。

XFN 网站提供了关于使用和实施此系统的信息，包括带有示例的介绍、样式建议和未来潜在的用例。 它还提供了一个四步入门 XFN 指南、一个定义 "rel" 属性中使用的值的配置文件，以及概述 XFN 开发期间的设计选择的背景信息。

其他资源包括常见问题解答、XFN 工具（如 XFN Creator）的集合，以及关于将 XFN 与社交网络和其他技术集成的指南。 该网站还重点介绍了 XFN 使用示例，提出了为项目做出贡献的方法，并列出了引用 XFN 的新闻文章。 最后，它对贡献者表示感谢，并邀请用户提供反馈。 XFN 的版权归 GMPG 所有，保留部分权利。

---

## 53. 康卡斯特高管警告员工不要对查理·柯克发表不当言论

**原文标题**: Comcast Executives Warn Workers to Not Say the Wrong Thing About Charlie Kirk

**原文链接**: [https://www.404media.co/comcast-nbcuniversal-email-charlie-kirk/](https://www.404media.co/comcast-nbcuniversal-email-charlie-kirk/)

404 Media的这篇文章报道了康卡斯特高管在右翼评论员查理·柯克去世后，向NBC环球员工发送的一封公司内部邮件。这封由布莱恩·罗伯茨、迈克·卡瓦纳和马克·拉扎勒斯署名的邮件对柯克的去世表示哀悼，称他为“公开辩论的倡导者”，并强调了团结的重要性。

该邮件还暗示了MSNBC政治分析师马修·道德被解雇一事，道德曾在节目中对柯克的遗产发表批评性评论，将他的言论与仇恨行为联系起来。高管们强调，这种报道“与促进文明对话背道而驰”，并警告员工要尊重不同的观点。他们表示，员工应通过尊重、倾听和善待他人，在工作和社区中体现公司的价值观。

文章批评了主流媒体试图“美化”柯克遗产的做法，文章将其定义为包括骚扰和将剥夺人们基本人权的正常化。作者山姆·科尔正在寻求有关其他公司如何在柯克去世后处理政治言论问题的信息。

---

## 54. Revanced团队收到Spotify的DMCA通知

**原文标题**: Revanced Team Gets DMCA from Spotify

**原文链接**: [https://revanced.app/announcements/15-spotify-dmca-notice-seeking-legal-help](https://revanced.app/announcements/15-spotify-dmca-notice-seeking-legal-help)

ReVanced团队，即热门Android应用自定义工具ReVanced补丁的开发者，收到了来自Spotify的DMCA移除通知。该通知特别针对通过ReVanced对Spotify应用进行的修改和补丁。

公告称，Spotify的法律团队声称这些修改侵犯了他们的版权。公告中并未详细说明涉嫌侵权的细节，但通常这类声明都集中在规避Spotify的DRM（数字版权管理）、修改应用的预期功能（例如，广告拦截）或在未订阅的情况下访问高级功能。

由于DMCA通知，ReVanced团队已从其平台上删除了所有与Spotify相关的补丁和修改，以遵守法律并避免潜在的法律影响。他们正在积极寻求法律援助和指导，以了解DMCA通知的全部含义并探索潜在的解决方案。

该团队强调他们致力于尊重知识产权，但也强调了社区对定制和个性化的兴趣。在法律审查和与Spotify的潜在谈判之前，ReVanced与Spotify的兼容性的未来仍然不确定。该团队正在不断更新社区的进展，并征求任何相关的法律专业知识。

---

## 55. 康威生命游戏，但具音乐性

**原文标题**: Conway's Game of Life, but musical

**原文链接**: [https://www.hudsong.dev/digital-darwin](https://www.hudsong.dev/digital-darwin)

本文探讨了音乐进化与生物系统之间引人入胜的相似之处，并以康威生命游戏作为核心类比。作者描述了如何构建一个“旋律繁殖器”，一种允许用户通过选择和繁殖他们最喜欢的旋律来进化音乐的数字工具，这与理查德·道金斯的“模因”概念以及Savage等人关于音乐进化中可预测模式的研究相呼应。

然后，作者展示了康威生命游戏的音乐诠释，其中细胞的诞生和死亡分别触发和谐与互补的音调，从而创造出不断进化且不可预测的音乐。这表明简单的规则如何产生复杂的结构，类似于生物系统和音乐作品的出现方式。

本文将这种类比扩展到像Labubu玩具热潮这样的文化现象，展示了它的传播如何反映流行病学模型，暗示了信息传播中的普遍模式。作者使用Google Trends数据来可视化这一点。借鉴达尔文“最美丽的无尽形式”的概念以及博伊德和理查森将文化视为共享创新池的观点，本文认为，文化进化，无论是音乐还是模因，都依赖于那些能够抓住我们注意力的模式而蓬勃发展。作者最后强调了代码在将抽象想法转化为有形的、互动式体验方面的赋权作用。

---

## 56. Show HN: 小额转账 – SaaS服务每次请求收费0.000001美元起

**原文标题**: Show HN: Small Transfers – charge from 0.000001 USD per request for your SaaS

**原文链接**: [https://smalltransfers.com/](https://smalltransfers.com/)

这个“Show HN”帖子介绍“Small Transfers”服务，该服务允许SaaS企业对每次API请求或服务使用收取极小金额（低至0.000001美元）。这为微计费模式开辟了可能性，用户只需为他们消费的内容付费，避免了订阅费或大额前期成本。

强调的关键优势是定价的精细度。企业可以精确地为每次请求所提供的价值收费，而不是提供分级定价方案，这可能会吸引那些因传统定价结构而望而却步的用户。

“加载中……”的内容表明该帖子可能包含有关该服务实施、API、用例的更多详细信息，以及可能指向网站或文档的链接。它还可能包含有关支持如此小额交易的底层技术的信息，例如支付处理器或区块链解决方案。在没有完整内容的情况下，具体的的技术细节和实施方案是未知的，但核心产品是明确的：针对SaaS服务的极其精细的、基于使用量的定价。

---

## 57. NT操作系统内核信息泄露漏洞

**原文标题**: NT OS Kernel Information Disclosure Vulnerability

**原文链接**: [https://www.crowdfense.com/nt-os-kernel-information-disclosure-vulnerability-cve-2025-53136/](https://www.crowdfense.com/nt-os-kernel-information-disclosure-vulnerability-cve-2025-53136/)

本文详细介绍了一个新发现的内核信息泄露漏洞，CVE-2025-53136，存在于NT OS中，尤其影响Windows 24H2及更高版本。该漏洞允许攻击者泄露内核地址，即便微软先前通过`NtQuerySystemInformation`缓解了此类泄露，也使得利用变得更容易。

作者hieu.q在分析CVE-2024-43511（一个TOCTOU竞争条件漏洞）的补丁时发现了该漏洞。 新漏洞出现在`RtlSidHashInitialize`函数中，该函数将来自`TOKEN`结构的指针（内核地址）临时存储在用户可控的缓冲区中。 通过赢得读取用户缓冲区和函数覆盖它之间的竞争条件，攻击者可以泄露内核地址。该漏洞通过使用`TokenAccessInformation`类的`NtQueryInformationToken`系统调用触发。

这种泄露意义重大，因为较新Windows版本中已修补了先前泄露内核地址的方法。 该漏洞可以从低完整性级别（Low IL）或AppContainer上下文中利用。当与“任意地址写”漏洞链接以覆盖`TOKEN`对象的`Privileges`字段时，它可能导致完整的本地权限提升（LPE）。作者已成功在来自低完整性级别和AppContainer上下文的Windows Insider Preview版本上演示了该漏洞的利用。

本文还概述了与微软的披露时间线，包括最初错误地将该漏洞归类为重复漏洞，之后最终被承认并分配了CVE-2025-53136。 作者强调了彻底的补丁分析和谨慎的代码修改对于防止引入新漏洞的重要性。

---

## 58. Zig 的 Web 框架

**原文标题**: A Web Framework for Zig

**原文链接**: [https://www.jetzig.dev/](https://www.jetzig.dev/)

Jetzig 是一个使用 Zig 编写的全新、MIT 许可的 Web 框架，专为构建 RESTful API 和 Web 应用程序而设计，注重速度和易用性。它提供基于文件的路由，直接映射到 Zig 函数，并支持使用 Zmpl 的 HTML 模板，提供布局、局部模板、继承和静态内容渲染。默认情况下，端点渲染 JSON，从而简化 API 开发。

主要功能包括：

*   **性能：** 构建于 `http.zig` 之上，实现高效且可扩展的运行。
*   **工具：** CLI 工具，用于项目创建和组件管理。
*   **中间件：** 可定制的中间件链，用于请求/响应处理，包括对 htmx 的内置支持。
*   **会话：** 开箱即用的 cookie、用户会话和标头管理支持。
*   **数据库层：** JetQuery 提供强大而灵活的数据库交互层。

Jetzig 是开源且社区驱动的，拥有活跃的 Discord 服务器提供支持。文档和示例可帮助用户快速入门。

---

## 59. “强盗蜂”入侵养蜂人商店，企图盗取蜂蜜

**原文标题**: ‘Robber bees’ invade apiarist’s shop in attempted honey heist

**原文链接**: [https://www.cbc.ca/news/canada/british-columbia/robber-bees-terrace-bc-apiary-1.7627532](https://www.cbc.ca/news/canada/british-columbia/robber-bees-terrace-bc-apiary-1.7627532)

在卑诗省特勒斯，Rushing River Apiaries的养蜂人克里斯汀·麦克唐纳在八月末经历了一场罕见的“抢劫”——数千只“盗蜂”入侵了她的商店，因自然资源匮乏而寻觅蜂蜜。这是麦克唐纳首次看到盗蜂以她室内商店为目标，最初的情况让她感到害怕。这些蜜蜂在夏末和初秋因资源稀缺而驱使，通常会攻击较弱的蜂箱以窃取蜂蜜。

这些蜜蜂通过商店门上的裂缝进入，在找到食物来源后，可能使用了“摇摆舞”来告知其他蜜蜂。麦克唐纳通过用防水布和盖子盖住大部分蜂蜜和设备来保护它们。然后，她巧妙地利用光作为诱饵将蜜蜂困在浴室里，之后将它们释放，但它们花了几天时间才停止返回。

蜜蜂科学家艾莉森·麦卡菲解释说，当产蜜花朵变得稀少，蜜蜂数量达到顶峰时，盗蜂行为很常见，导致一些蜂群入侵较弱的蜂群。她还强调，黄蜂也可能以蜜蜂的蜂群为目标，寻找含糖物质。麦克唐纳认为，由于持续的高温，今年蜜蜂的迫切程度更高。她建议其他养蜂人确保他们的蜜蜂得到充分喂养，以防止抢劫行为。

---

## 60. GrapheneOS 获取了安卓安全补丁，但不允许发布源代码。

**原文标题**: GrapheneOS accessed Android security patches but not allowed to publish sources

**原文链接**: [https://grapheneos.social/@GrapheneOS/115164133992525834](https://grapheneos.social/@GrapheneOS/115164133992525834)

GrapheneOS的Mastodon帖子称他们可以提前访问安卓安全公告。这暗示GrapheneOS在公开披露前，从谷歌收到安全补丁和漏洞信息。然而，标题提到他们“不允许发布源代码”，这表明对GrapheneOS如何利用或分享这些信息存在限制。这可能意味着虽然他们可以将安全补丁整合到他们的操作系统中，但他们被禁止在谷歌正式发布之前公开与这些补丁相关的源代码。这种安排使GrapheneOS能够及时解决安全漏洞，但需要在与谷歌关于信息披露的协议框架内进行。

---

## 61. Show HN: C++ 编译器支持页面

**原文标题**: Show HN: C++ Compiler Support Page

**原文链接**: [https://cppstat.dev](https://cppstat.dev)

cppstat 是一个致力于追踪不同编译器和标准库对 C++ 特性支持情况的网站。它提供了一个可搜索的表格，指示特定 C++ 特性是否被 GCC、Clang、MSVC 和 Xcode 完全支持（绿色）、部分支持（橙色）或尚未支持（红色）。该网站区分语言和库特性，允许用户进行相应筛选。点击编译器名称可显示关于发布日期和部分支持原因的更多详细信息。

信息定期更新，最新更新时间为 2025 年 9 月 12 日。鼓励用户报告不准确或缺失的信息。

主要内容是一个表格，列出了计划用于 C++26 的特性及其对应的论文编号，以及每个编译器的支持状态。该表格涵盖了广泛的特性，包括反射功能、标准库强化、constexpr 增强、对 `<simd>` 头的添加、异常处理的改进以及新的库特性，如 `std::mdspan`、`std::observable` 以及对格式化和字符串处理的增强。该表格全面概述了不同工具链中已提议的 C++26 特性的当前实现状态。

---

## 62. 丹麦连锁超市设立“应急商店”

**原文标题**: Danish supermarket chain is setting up "Emergency Stores"

**原文链接**: [https://swiss.social/@swaldorff/115186445638788782](https://swiss.social/@swaldorff/115186445638788782)

关于文章“丹麦连锁超市开设‘应急商店’”的摘要信息不完整。提供的文本仅包含标题和 Svend Waldorff 在 Mastodon 上发布的帖子开头，提到了一个有趣的动态，即丹麦连锁超市正在开设“应急商店”。由于“settin...”之后的内容缺失，因此无法理解这些“应急商店”的目的、概念或具体细节，也无法了解涉及的连锁超市。文本的其余部分提到了 Mastodon 网站对 Javascript 的要求，并建议使用 Mastodon 应用程序。因此，在没有更多上下文的情况下，无法提供完整的摘要。

---

## 63. 麻省理工软件工具将日常物品变成引人注目的动画显示器

**原文标题**: MIT software tool turns everyday objects into animated, eye-catching displays

**原文链接**: [https://news.mit.edu/2025/fabobscura-turns-everyday-objects-into-animated-displays-0910](https://news.mit.edu/2025/fabobscura-turns-everyday-objects-into-animated-displays-0910)

麻省理工学院研究人员开发了FabObscura，这是一种无需电子设备即可简化栅栏网格动画（扫描动画）创建的软件工具。这些动画通过滑动图案化的片材穿过特殊准备的图像来产生运动错觉，使日常物品变成动态显示器。

FabObscura允许用户通过输入数学函数来设计非常规的栅栏图案（锯齿形、圆形等），与主要关注直线的现有工具相比，提供了更大的创作自由。该软件支持各种用户交互，包括视角依赖型显示和由滑动或旋转栅栏触发的动画。用户可以上传动画帧或从预设序列中选择，然后使用标准2D打印机打印栅栏和图像。

该系统还允许“嵌套动画”，其中栅栏的不同运动会显示不同的动画序列。虽然嵌套动画提供了增强的动态性，但研究人员承认它们可能会损害视觉质量。他们提供了设计指南来缓解这些问题，例如使用较少的帧和高对比度图像。

FabObscura的潜在应用包括增强家居用品、创作动态艺术品和开发可重构的标牌。未来的计划包括扩展系统以支持视频上传，并探索创建3D栅栏网格动画。该研究突出了动画创作大众化的潜力，使用户能够将普通物品转化为引人入胜的低功耗显示器。

---

## 64. 食用牡蛎对抗气候灾难

**原文标题**: Eating Oysters against the climate catastrophy

**原文链接**: [https://www.pnas.org/doi/10.1073/pnas.2504004122](https://www.pnas.org/doi/10.1073/pnas.2504004122)

无法访问该文章链接。

---

## 65. Reshaped 现在开源了

**原文标题**: Reshaped is now open source

**原文链接**: [https://reshaped.so/blog/reshaped-oss](https://reshaped.so/blog/reshaped-oss)

季马·别利亚耶夫宣布用于 React 和 Figma 的组件库 Reshaped 现已完全开源。别利亚耶夫最初创建 Reshaped 是为了解决 Web 开发的常见需求，重点在于对齐设计和工程，同时应对主题和暗黑模式等 UI 挑战。此前，Reshaped 采用付费许可模式，从而能够提供专注的支持和开发。两年前，React 包已免费。

现在，完整的 React 库源代码可在 GitHub 上获取，Figma 库可在 Figma Community 中获取。别利亚耶夫希望此举能够促进设计和工程社区之间的知识共享。他还计划分享关于新功能实现的幕后见解，特别是关于与新 Figma 或 React 版本集成的幕后见解。

现有许可证持有者将继续获得对更新的完全访问权限。展望未来，别利亚耶夫正在考虑向核心库添加复杂的高级组件，重点关注高级 CSS 和 React 逻辑，同时保持 Reshaped 帮助用户构建精美产品和设计系统的核心价值。作者表达了对社区的热情和感激之情。

---

## 66. 英特尔人才流失持续，至强芯片架构师离职。

**原文标题**: Intel talent bleed continues as Xeon chip architect heads for the escape hatch

**原文链接**: [https://www.theregister.com/2025/09/11/intel_loses_chief_architect/](https://www.theregister.com/2025/09/11/intel_loses_chief_architect/)

英特尔至强服务器CPU首席架构师Ronak Singhal将在效力近30年后离开英特尔。他为英特尔的处理器架构做出了重大贡献，包括Haswell和Broadwell，以及酷睿和凌动系列。

在他离职之际，英特尔至强部门正面临来自AMD和基于Arm的CPU日益激烈的竞争。尽管英特尔近年来通过推出Granite Rapids缩小了与AMD的差距，但Singhal的离职标志着英特尔数据中心集团又失去了一位经验丰富的人才。

最近，其他几位关键人物也离开了英特尔，包括Sailesh Kottapalli（加入高通）、Lisa Spelman（加入Cornelis Networks）、Justin Hotard（加入诺基亚）和Michelle Johnston Holthaus。这种高流动率甚至蔓延到了高管层面，英特尔宣布了一项更广泛的高管改组，其中包括其数据中心工程和客户端计算集团的新领导层。英特尔确认了Singhal的离职，但未作进一步评论。

---

## 67. The Influencer FBI

**原文标题**: The Influencer FBI

**原文链接**: [https://www.theatlantic.com/ideas/archive/2025/09/charlie-kirk-fbi-investigation/684184/](https://www.theatlantic.com/ideas/archive/2025/09/charlie-kirk-fbi-investigation/684184/)

The article "The Influencer FBI" details the unusual and concerning circumstances surrounding the FBI's investigation into the assassination of right-wing influencer Charlie Kirk. It focuses on FBI Director Kash Patel, a former pro-Trump influencer, and his social media activity immediately following the murder.

Patel's rapid, and ultimately inaccurate, updates on X (formerly Twitter) regarding a suspect being apprehended and then released drew criticism from both right-wing figures and former law enforcement officials, who accused him of prioritizing "click-bait" over proper procedure. Critics believe this behavior undermines the FBI's credibility and distracts from the investigation.

The article highlights a broader issue of political violence and the role of influencers in shaping public perception following such events. It discusses how Kirk's murder became instantly consumed by influencer culture, with graphic videos and baseless conspiracy theories spreading online.

The author argues that Patel's background as an influencer is ill-suited for leading the FBI, contrasting the need for restraint and reliable information from law enforcement with the influencer's tendency to theorize and create content. The article also points out the challenges the FBI faces, including resource constraints and personnel shifts, potentially hindering its effectiveness in solving the case. It concludes with concern that the politicized leadership is compromising the FBI's ability to perform its duties effectively.


---

## 68. Making io_uring pervasive in QEMU [pdf]

**原文标题**: Making io_uring pervasive in QEMU [pdf]

**原文链接**: [https://vmsplice.net/~stefan/stefanha-kvm-forum-2025.pdf](https://vmsplice.net/~stefan/stefanha-kvm-forum-2025.pdf)

生成摘要时出错

---

## 69. The challenge of maintaining curl

**原文标题**: The challenge of maintaining curl

**原文链接**: [https://lwn.net/Articles/1034966/](https://lwn.net/Articles/1034966/)

生成摘要时出错

---

## 70. AirPods live translation blocked for EU users with EU Apple accounts

**原文标题**: AirPods live translation blocked for EU users with EU Apple accounts

**原文链接**: [https://www.macrumors.com/2025/09/11/airpods-live-translation-eu-restricted/](https://www.macrumors.com/2025/09/11/airpods-live-translation-eu-restricted/)

生成摘要时出错

---

## 71. An engineering history of the Manhattan Project

**原文标题**: An engineering history of the Manhattan Project

**原文链接**: [https://www.construction-physics.com/p/an-engineering-history-of-the-manhattan](https://www.construction-physics.com/p/an-engineering-history-of-the-manhattan)

生成摘要时出错

---

## 72. Removing yellow stains from fabric with blue light

**原文标题**: Removing yellow stains from fabric with blue light

**原文链接**: [https://phys.org/news/2025-09-yellow-fabric-blue.html](https://phys.org/news/2025-09-yellow-fabric-blue.html)

生成摘要时出错

---

## 73. Swiss government look to undercut privacy tech stoking fear of mass surveillance

**原文标题**: Swiss government look to undercut privacy tech stoking fear of mass surveillance

**原文链接**: [https://therecord.media/switzerland-digital-privacy-law-proton-privacy-surveillance](https://therecord.media/switzerland-digital-privacy-law-proton-privacy-surveillance)

生成摘要时出错

---

## 74. Center for the Alignment of AI Alignment Centers

**原文标题**: Center for the Alignment of AI Alignment Centers

**原文链接**: [https://alignmentalignment.ai](https://alignmentalignment.ai)

生成摘要时出错

---

## 75. FAA Launches Process to Select Prime Integrator for Brand New ATC System

**原文标题**: FAA Launches Process to Select Prime Integrator for Brand New ATC System

**原文链接**: [https://www.faa.gov/newsroom/us-transportation-secretary-duffy-faa-launch-process-select-prime-integrator-brand-new-air](https://www.faa.gov/newsroom/us-transportation-secretary-duffy-faa-launch-process-select-prime-integrator-brand-new-air)

生成摘要时出错

---

## 76. Full Moon: Seestar S50 vs. Samsung S25

**原文标题**: Full Moon: Seestar S50 vs. Samsung S25

**原文链接**: [https://www.4rknova.com//blog/2025/09/08/moon-photos](https://www.4rknova.com//blog/2025/09/08/moon-photos)

生成摘要时出错

---

## 77. Nano Banana image examples

**原文标题**: Nano Banana image examples

**原文链接**: [https://github.com/PicoTrex/Awesome-Nano-Banana-images/blob/main/README_en.md](https://github.com/PicoTrex/Awesome-Nano-Banana-images/blob/main/README_en.md)

生成摘要时出错

---

## 78. Logging in Go with Slog: A Practitioner's Guide

**原文标题**: Logging in Go with Slog: A Practitioner's Guide

**原文链接**: [https://www.dash0.com/guides/logging-in-go-with-slog](https://www.dash0.com/guides/logging-in-go-with-slog)

生成摘要时出错

---

## 79. Jef Raskin's cul-de-sac and the quest for the humane computer

**原文标题**: Jef Raskin's cul-de-sac and the quest for the humane computer

**原文链接**: [https://arstechnica.com/gadgets/2025/09/jef-raskins-cul-de-sac-and-the-quest-for-the-humane-computer/](https://arstechnica.com/gadgets/2025/09/jef-raskins-cul-de-sac-and-the-quest-for-the-humane-computer/)

生成摘要时出错

---

## 80. Apple's iPhone security feature makes life more difficult for spyware makers

**原文标题**: Apple's iPhone security feature makes life more difficult for spyware makers

**原文链接**: [https://techcrunch.com/2025/09/11/apples-latest-iphone-security-feature-just-made-life-more-difficult-for-spyware-makers/](https://techcrunch.com/2025/09/11/apples-latest-iphone-security-feature-just-made-life-more-difficult-for-spyware-makers/)

生成摘要时出错

---

## 81. Backprompting: Leveraging synthetic production data for health advice guardrails

**原文标题**: Backprompting: Leveraging synthetic production data for health advice guardrails

**原文链接**: [https://arxiv.org/abs/2508.18384](https://arxiv.org/abs/2508.18384)

生成摘要时出错

---

## 82. US to split profits with Tokyo from Japan-funded projects till $550B is recouped

**原文标题**: US to split profits with Tokyo from Japan-funded projects till $550B is recouped

**原文链接**: [https://www.cnbc.com/2025/09/11/japan-us-tariff-550-billion-investment-trump-lutnick.html](https://www.cnbc.com/2025/09/11/japan-us-tariff-550-billion-investment-trump-lutnick.html)

生成摘要时出错

---

## 83. Samsung taking market share from Apple in U.S. as foldable phones gain momentum

**原文标题**: Samsung taking market share from Apple in U.S. as foldable phones gain momentum

**原文链接**: [https://www.cnbc.com/2025/08/16/samsungs-us-market-share-apple-rivalry-foldable-phones.html](https://www.cnbc.com/2025/08/16/samsungs-us-market-share-apple-rivalry-foldable-phones.html)

生成摘要时出错

---

## 84. GrapheneOS and forensic extraction of data (2024)

**原文标题**: GrapheneOS and forensic extraction of data (2024)

**原文链接**: [https://discuss.grapheneos.org/d/13107-grapheneos-and-forensic-extraction-of-data](https://discuss.grapheneos.org/d/13107-grapheneos-and-forensic-extraction-of-data)

生成摘要时出错

---

## 85. Disposable Code Is Here to Stay, but Durable Code Is What Runs the World

**原文标题**: Disposable Code Is Here to Stay, but Durable Code Is What Runs the World

**原文链接**: [https://www.honeycomb.io/blog/disposable-code-is-here-to-stay](https://www.honeycomb.io/blog/disposable-code-is-here-to-stay)

生成摘要时出错

---

## 86. Show HN: Making a cross-platform game in Go using WebRTC Datachannels

**原文标题**: Show HN: Making a cross-platform game in Go using WebRTC Datachannels

**原文链接**: [https://pion.ly/blog/making-a-game-with-pion/](https://pion.ly/blog/making-a-game-with-pion/)

生成摘要时出错

---

## 87. PgEdge Goes Open Source

**原文标题**: PgEdge Goes Open Source

**原文链接**: [https://www.pgedge.com/blog/pgedge-goes-open-source](https://www.pgedge.com/blog/pgedge-goes-open-source)

生成摘要时出错

---

## 88. Learning lessons from the loss of the Norwegian frigate Helge Ingstad

**原文标题**: Learning lessons from the loss of the Norwegian frigate Helge Ingstad

**原文链接**: [https://www.navylookout.com/learning-the-lessons-the-loss-the-norwegian-frigate-helge-ingstad/](https://www.navylookout.com/learning-the-lessons-the-loss-the-norwegian-frigate-helge-ingstad/)

生成摘要时出错

---

## 89. The Helix Text Editor (2024)

**原文标题**: The Helix Text Editor (2024)

**原文链接**: [https://jonathan-frere.com/posts/helix/](https://jonathan-frere.com/posts/helix/)

生成摘要时出错

---

## 90. How Palantir is mapping the nation’s data

**原文标题**: How Palantir is mapping the nation’s data

**原文链接**: [https://theconversation.com/when-the-government-can-see-everything-how-one-company-palantir-is-mapping-the-nations-data-263178](https://theconversation.com/when-the-government-can-see-everything-how-one-company-palantir-is-mapping-the-nations-data-263178)

生成摘要时出错

---

## 91. Hashed sorting is typically faster than hash tables

**原文标题**: Hashed sorting is typically faster than hash tables

**原文链接**: [https://reiner.org/hashed-sorting](https://reiner.org/hashed-sorting)

生成摘要时出错

---

## 92. A tech-law measurement and analysis of event listeners for wiretapping

**原文标题**: A tech-law measurement and analysis of event listeners for wiretapping

**原文链接**: [https://arxiv.org/abs/2508.19825](https://arxiv.org/abs/2508.19825)

生成摘要时出错

---

## 93. Where did the Smurfs get their hats (2018)

**原文标题**: Where did the Smurfs get their hats (2018)

**原文链接**: [https://www.pipelinecomics.com/beginning-bd-smurfs-hats-origin/](https://www.pipelinecomics.com/beginning-bd-smurfs-hats-origin/)

生成摘要时出错

---

## 94. Gregg Kellogg has died

**原文标题**: Gregg Kellogg has died

**原文链接**: [https://lists.w3.org/Archives/Public/public-json-ld-wg/2025Sep/0012.html](https://lists.w3.org/Archives/Public/public-json-ld-wg/2025Sep/0012.html)

生成摘要时出错

---

## 95. The HackberryPi CM5 handheld computer

**原文标题**: The HackberryPi CM5 handheld computer

**原文链接**: [https://github.com/ZitaoTech/HackberryPiCM5](https://github.com/ZitaoTech/HackberryPiCM5)

生成摘要时出错

---

## 96. Adjacency Matrix and std:mdspan, C++23

**原文标题**: Adjacency Matrix and std:mdspan, C++23

**原文链接**: [https://www.cppstories.com/2025/cpp23_mdspan_adj/](https://www.cppstories.com/2025/cpp23_mdspan_adj/)

生成摘要时出错

---

## 97. Public Suffix List

**原文标题**: Public Suffix List

**原文链接**: [https://publicsuffix.org/](https://publicsuffix.org/)

生成摘要时出错

---

## 98. The effects of algorithms on the public discourse

**原文标题**: The effects of algorithms on the public discourse

**原文链接**: [https://tekhne.dev/internet-resist/](https://tekhne.dev/internet-resist/)

生成摘要时出错

---

## 99. Reverse-engineering Roadsearch Plus, or, roadgeeking with an 8-bit CPU

**原文标题**: Reverse-engineering Roadsearch Plus, or, roadgeeking with an 8-bit CPU

**原文链接**: [http://oldvcr.blogspot.com/2025/08/make-your-apple-ii-or-commodore-64.html](http://oldvcr.blogspot.com/2025/08/make-your-apple-ii-or-commodore-64.html)

生成摘要时出错

---

## 100. Beyond package management: How Nix refactored my digital life

**原文标题**: Beyond package management: How Nix refactored my digital life

**原文链接**: [https://www.jimmyff.co.uk/blog/beyond-package-management-how-nix-refactored-my-digital-life/](https://www.jimmyff.co.uk/blog/beyond-package-management-how-nix-refactored-my-digital-life/)

生成摘要时出错

---

