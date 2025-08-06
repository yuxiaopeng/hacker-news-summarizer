# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-08-06.md)

*最后自动更新时间: 2025-08-06 17:54:23*
## 1. 编写 Rust GPU 内核驱动：GPU 驱动工作原理简介

**原文标题**: Writing a Rust GPU kernel driver: a brief introduction on how GPU drivers work

**原文链接**: [https://www.collabora.com/news-and-blog/blog/2025/08/06/writing-a-rust-gpu-kernel-driver-a-brief-introduction-on-how-gpu-drivers-work/](https://www.collabora.com/news-and-blog/blog/2025/08/06/writing-a-rust-gpu-kernel-driver-a-brief-introduction-on-how-gpu-drivers-work/)

这篇 Collabora 博客文章是关于开发 Tyr（一个用于 Arm Mali GPU 的 Rust GPU 内核驱动程序）系列文章的第二篇，它介绍了 GPU 驱动程序是如何工作的。文章以一个简单的 Vulkan 应用程序 VkCube 为例，解释了用户模式驱动程序 (UMD) 和内核模式驱动程序 (KMD) 的作用。

UMD（例如 Mesa 的 panvk）处理更高级别的 API 调用，例如 Vulkan，将其转换为 GPU 可以理解的较低级别的命令。KMD (Tyr) 充当 UMD 和 GPU 硬件之间的接口。UMD 管理诸如几何体、纹理和着色器之类的资源，并请求 KMD 分配 GPU 内存并设置绘制调用。

文章重点介绍了 KMD 的职责：内存分配和映射、将工作提交到硬件队列以及通知 UMD 作业完成。文章还强调了调度和设备初始化的重要性。

该文章随后定义了 Tyr 公开的接口，其中包括用于设备信息检索、VM 管理、调度组管理、作业提交和分块堆管理的 ioctl。该接口设计得相对紧凑，UMD 处理与绘图命令相关的大部分复杂性。

下一篇文章将深入探讨 CSF 架构以及启动微控制器单元 (MCU) 所需的步骤。

---

## 2. Claude 代码 IDE Emacs 集成

**原文标题**: Claude Code IDE integration for Emacs

**原文链接**: [https://github.com/manzaltu/claude-code-ide.el](https://github.com/manzaltu/claude-code-ide.el)

本文档介绍了`claude-code-ide.el`，一个使用模型上下文协议(MCP)将Claude Code CLI与Emacs集成的Emacs包。这种集成超越了简单的终端封装，使Claude能够利用Emacs的LSP、项目管理和Elisp函数等特性。

主要功能包括自动项目检测、终端集成（vterm或eat）、MCP实现、文件操作和工作区信息的工具支持、与Flycheck/Flymake的诊断集成、高级差异视图和选项卡栏支持。Claude可以访问Emacs的功能，如LSP进行代码导航（通过xref）、Tree-sitter进行AST分析以及Imenu进行符号列表。自定义的Emacs命令可以作为MCP工具公开，从而实现项目范围内的搜索、重构和自定义Elisp函数的执行。

本文档详细介绍了安装说明（需要Emacs 28.1+、Claude Code CLI和vterm/eat）、通过瞬态菜单访问的基本命令、多项目支持和窗口管理选项。它还涵盖了广泛的配置选项，如设置CLI路径、缓冲区命名函数、调试模式、终端后端、窗口放置、自定义系统提示和MCP服务器设置。 解释了调试技巧，通过Git工作树使用多个Claude实例以及定义自定义MCP工具。内置的MCP工具包括`xref-find-references`、`xref-find-apropos`、`treesit-info`、`imenu-list-symbols`和`project-info`。

---

## 3. 配置文件过于私密和个人化，不适合分享。

**原文标题**: Dotfiles feel too intimate and personal to share

**原文链接**: [https://hamatti.org/posts/dotfiles-feel-too-intimate-and-personal-to-share/](https://hamatti.org/posts/dotfiles-feel-too-intimate-and-personal-to-share/)

将点文件公开分享感觉太私密和个人化

文章《将点文件公开分享感觉太私密和个人化》的作者Hamatti探讨了其对于公开分享点文件的不安，尽管这在软件开发社区中是一种常见的做法。点文件是配置文件（通常是隐藏的，因此带有前导点），用于控制各种工具和操作系统本身的行为和外观。

作者认为，点文件是高度个人化的，反映了个人的工作流程、偏好，甚至是因特定硬件或软件怪癖而做出的妥协。它们代表了多年积累的知识、适应以及解决作者独特计算环境中遇到的问题的最终结果。

分享这些配置感觉就像暴露日记或个人工作空间，不仅揭示了技术选择，还可能揭示了作者并不引以为傲的低效技巧或变通方法。对判断的恐惧或维护和解释这些个性化配置的期望进一步加剧了犹豫。

文章还提到了点文件可能包含敏感信息的可能性，如果不进行适当的清理，可能会无意中泄露 API 密钥、用户名或其他凭据。作者承认分享和学习他人经验的好处，但最终认为，点文件的个人性质，加上潜在的风险和责任，使他们不愿意公开自己的点文件。他们更喜欢从他人公开的点文件中学习，但保持自己的配置私密。

---

## 4. 打破有向单源最短路径的排序壁垒

**原文标题**: Breaking the sorting barrier for directed single-source shortest paths

**原文链接**: [https://www.quantamagazine.org/new-method-is-the-fastest-way-to-find-the-best-routes-20250806/](https://www.quantamagazine.org/new-method-is-the-fastest-way-to-find-the-best-routes-20250806/)

这篇《量子杂志》的文章讨论了一种突破性的新算法，它超越了传统方法在计算机科学中解决单源最短路径问题的局限性。几十年来，依赖于按距离排序路径的Dijkstra算法一直是标准，其“排序障碍”限制了它的速度。

段然和他的团队开发了一种新的算法，通过完全避免排序来打破这一障碍。他们的方法将探索路径前沿上的相邻节点聚类，使算法能够更有效地探索，并有可能按照非严格的距离顺序探索节点。

该团队最初为无向图开发了一个解决方案，但在将其应用于有向图时面临挑战。他们融入了Bellman-Ford算法的元素，并战略性地使用它来搜索有影响力的节点。毛啸贡献了一种非随机化方法，进一步完善了该算法。最终的算法对图进行分层，并战略性地使用Bellman-Ford算法来精确定位重要节点，从而在无需排序的情况下找到最短路径。

这种新算法优于Dijkstra算法，并且虽然复杂，但不依赖于特别复杂的数学。研究人员现在正寻求进一步优化该算法，因为对于它潜在的运行速度没有已知的根本限制。这一发现代表了图论的一个重大进步，并对许多需要高效寻路的应用具有重要意义。

---

## 5. Show HN: Kitten TTS – 25MB CPU-Only, Open-Source TTS Model

Show HN：Kitten TTS – 25MB CPU单核开源TTS模型

**原文标题**: Show HN: Kitten TTS – 25MB CPU-Only, Open-Source TTS Model

**原文链接**: [https://github.com/KittenML/KittenTTS](https://github.com/KittenML/KittenTTS)

Kitten TTS：一种新型开源、轻量级的文本转语音（TTS）模型，专为仅限 CPU 系统上的高质量语音合成而设计。其主要特点包括：超小模型尺寸（小于 25MB）、针对 CPU 的优化使其能够在无需 GPU 的任何设备上部署、多种高质量语音选项，以及用于实时语音合成的快速推理。

该模型目前提供开发者预览版。用户可以通过 pip 使用指向 wheel 文件的直接链接来安装它。提供的代码片段演示了基本用法，展示了如何初始化模型、使用指定的语音从文本生成音频，并将输出保存为 WAV 文件。该代码还列出了可用的语音选项。

该模型因其仅限 CPU 的特性而与几乎任何系统兼容。开发路线图包括发布完全训练的模型权重、移动 SDK 和 Web 版本。

---

## 6. Zig错误模式

**原文标题**: Zig-Error-Patterns

**原文链接**: [https://glfmn.io/posts/zig-error-patterns/](https://glfmn.io/posts/zig-error-patterns/)

本文探讨了Zig中改进的调试模式，重点关注错误处理和测试驱动开发。文章利用`errdefer`来解决冗长的打印调试问题，仅在测试失败时打印调试信息，避免不必要的输出。

文章接着讨论了在`seergdb`或`gdb`等调试器中运行测试的问题。文章强调，标准的测试运行器能优雅地处理错误，除非发生断点或panic，否则调试器不会激活。为了解决这个问题，作者建议使用Zig的构建选项有条件地添加`@breakpoint()`调用。

build.zig脚本被修改以包含一个布尔选项“debugger”，允许开发者在测试执行期间启用或禁用断点。当debugger选项启用时（使用`zig build -Ddebugger test`），`@breakpoint()`调用会在测试失败时触发，从而实现有针对性的调试。文章还展示了如何将此构建选项与启动调试器关联起来。

最终的构建脚本包含一个条件语句，根据“debugger”选项的值运行标准测试运行器或调试器，从而简化了调试过程。这使得开发者可以轻松地在常规测试执行和发生错误时触发断点的调试会话之间切换，从而提高效率。提供的代码片段允许您应用这些策略并利用这些错误模式。

---

## 7. 303Gen – 303酸性循环生成器

**原文标题**: 303Gen – 303 acid loops generator

**原文链接**: [https://303-gen-06a668.netlify.app/](https://303-gen-06a668.netlify.app/)

303Gen是一款用于生成303风格酸性循环乐段的软件或在线工具。它可能提供用户界面，用于创建和操作让人联想到Roland TB-303贝斯合成器的声音，TB-303是酸性浩室音乐中的关键乐器。根据名称判断，其主要功能是以303风格创建音频循环乐段。

---

## 8. NautilusTrader：开源算法交易平台

**原文标题**: NautilusTrader: Open-source algorithmic trading platform

**原文链接**: [https://nautilustrader.io/](https://nautilustrader.io/)

NautilusTrader：快速、可靠、多功能的开源量化交易平台。它支持在单一平台交易包括加密货币、期货、股票、外汇和博彩市场等多种资产类别。该平台可使用历史数据进行事件驱动的回测，并支持无需修改代码的实盘交易。

主要功能包括：

*   **数据集成：** 加载任何自定义市场数据的能力。
*   **Python API：** 允许快速策略开发（高达 500 万行/秒）。
*   **纳秒级分辨率：** 用于精确的回测和模拟。
*   **快速迭代：** 促进策略和参数的快速优化。
*   **低延迟执行：** 由 Rust 组件驱动，保证速度。
*   **复杂策略：** 使用诸如 Clock、Cache、MessageBus 和 Portfolio 等模块化组件构建。
*   **高级订单：** 支持各种订单类型和应急策略。
*   **易于集成：** 简化新交易所和数据提供商的集成。
*   **可定制组件：** 支持表达任何策略构想。
*   **配置驱动：** 简化跨不同工具和交易所的策略复用。

NautilusTrader 提供了一种更简单的方式来集成新的交易所，允许用户在一个平台交易多个市场。使用 Python 可以快速无缝地完成安装。该平台还提供云平台解决方案。

---

## 9. Show HN: Sinkzone DNS转发器，阻止所有内容，但允许列表除外

**原文标题**: Show HN: Sinkzone DNS forwarder that blocks everything except your allowlist

**原文链接**: [https://github.com/berbyte/sinkzone](https://github.com/berbyte/sinkzone)

Sinkzone 是一款本地 DNS 解析器，旨在通过默认屏蔽所有域名来增强专注力，只允许显式加入白名单的域名进行解析。 这种方法颠覆了传统的“黑名单”方式，因为它认识到互联网浩瀚且不断变化，因此使用白名单对于专注工作来说更易于管理。

主要功能包括 DNS 级别的屏蔽、用于定时屏蔽会话的“专注模式”、用于灵活域名匹配的通配符支持（例如，`*github*`）、用于控制和监控的 HTTP API，以及用于实时流量查看和白名单管理的基于终端的 UI (TUI)。它具有跨平台性，支持 macOS、Linux 和 Windows。

该软件由解析器、HTTP API 服务器和 CLI/TUI 组成，它们相互通信以管理 DNS 查询和专注模式。 配置存储在 `~/.sinkzone/` 目录中，包括 `sinkzone.yaml` 和 `allowlist.txt`。

提供了适用于各种平台的安装说明，包括软件包管理器和直接下载。 该文档涵盖了常用命令、通配符模式和 TUI 导航。 它还详细介绍了如何从源代码构建应用程序、测试 API，并欢迎贡献。它提供 TUI 和 CLI 两种界面。

Sinkzone 旨在为无干扰的工作会话提供系统级解决方案，适用于编码、写作或一般的儿童安全。 它避免依赖浏览器扩展程序或云服务，确保隐私和本地控制。

---

## 10. 1090兆赫之谜：解读模式S和ADS-B信号指南

**原文标题**: The 1090 Megahertz Riddle: A Guide to Decoding Mode S and ADS-B Signals

**原文链接**: [https://books.open.tudelft.nl/home/catalog/book/11](https://books.open.tudelft.nl/home/catalog/book/11)

孙君子的《1090兆赫谜题：解码模式S和ADS-B信号指南》一书旨在填补模式S和ADS-B数据解码相关文献的空白。这些技术对于现代飞机监视至关重要，使飞机能够通过1090 MHz应答器自动广播身份、位置和速度等信息。本书旨在为研究人员、工程师和爱好者提供一个全面指南，以理解和利用开放的ADS-B和模式S数据。

本书首先介绍雷达系统、模式A/C、模式S和ADS-B的基础知识，包括信号采集所需的硬件和软件设置。核心内容侧重于对各种ADS-B和常见模式S信号类型的详细检查。本书大量使用Python代码示例来演示解码过程。最后一章总结全文，并提出了超越基本解码的进一步研究课题。

本书还提供了作者简介、参考文献、许可信息以及下载PDF、订购纸质副本或访问源文件的选项。对于任何有兴趣理解和使用开放的ADS-B和模式S数据进行航空运输研究和开发的人来说，本书都是一个宝贵的资源。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 2 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 3 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 4 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 5 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 6 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 7 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 8 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 9 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 10 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 11 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 12 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 13 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 14 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 15 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 16 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 17 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 18 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 19 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 20 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 21 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 22 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 23 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 24 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 25 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 26 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 27 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 28 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 29 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 30 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 31 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 32 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 33 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 34 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 35 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 36 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 37 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 38 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 39 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 40 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 41 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 42 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 43 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 44 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 45 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 46 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 47 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 48 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 49 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 50 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 51 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 52 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 53 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 54 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 55 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 56 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 57 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 58 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 59 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 60 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 61 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 62 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 63 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 64 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 65 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 66 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 67 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 68 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 69 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 70 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 71 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 72 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 73 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 74 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 75 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 76 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 77 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 78 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 79 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 80 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 81 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 82 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 83 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 84 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 85 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 86 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 87 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 88 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 89 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 90 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 91 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 92 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 93 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 94 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 95 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 96 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 97 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 98 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 99 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 100 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 101 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 102 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 103 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 104 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 105 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 106 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 107 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 108 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 109 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 110 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 111 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 112 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 113 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 114 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 115 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 116 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 117 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 118 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 119 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 120 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 121 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 122 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 123 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 124 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 125 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 126 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 127 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 128 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 129 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 130 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 131 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 132 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 133 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 134 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 135 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 136 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 137 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 138 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 139 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 140 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
