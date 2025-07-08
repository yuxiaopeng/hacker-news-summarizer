# Hacker News 热门文章摘要 (2025-07-08)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Show HN: Sumble – GTM数据知识图谱 – 查询技术栈、关键项目

**原文标题**: Show HN: Sumble – knowledge graph for GTM data – query tech stack, key projects

**原文链接**: [https://sumble.com](https://sumble.com)

Show HN 帖子介绍了 Sumble，一个被称为 GTM (Go-To-Market) 数据的知识图谱的工具。遗憾的是，提供的内容非常少，只说明了“您需要启用 JavaScript 才能运行此应用程序”。

基于标题和上下文（一个 “Show HN” 帖子，表明正在发布新产品），我们可以推断出以下内容：

*   **目的：** Sumble 很可能旨在提供一种结构化的方式来理解和查询 GTM 数据。 这可能包括关于所使用的技术、关键项目以及潜在的其他相关市场情报的信息。
*   **功能：** 知识图谱方面表明 Sumble 连接不同的数据点，以揭示 GTM 格局中的关系和见解。 用户可能能够查询此图来查找特定信息。
*   **技术

但是，在没有对其功能或目标受众的功能描述的情况下，Sumble 的确切用途仍然不清楚。 当前的帖子本质上是一个占位符，用户需要访问实时应用程序（启用 JavaScript）才能真正了解其目的和功能。

---

## 2. 谷歌现在可以读取你的 WhatsApp 消息了

**原文标题**: Google can now read your WhatsApp messages

**原文链接**: [https://www.neowin.net/guides/google-can-now-read-your-whatsapp-messages-heres-how-to-stop-it/](https://www.neowin.net/guides/google-can-now-read-your-whatsapp-messages-heres-how-to-stop-it/)

本文讨论了谷歌最近对 Gemini 的更新，该更新允许它与 Android 设备上的 WhatsApp、Messages 和 Phone 等应用进行交互，即使关闭了 Gemini 应用活动也是如此。这意味着 Gemini 可以通过语音命令发送消息或发起通话。

虽然谷歌声称 Gemini 通常无法读取或总结 WhatsApp 消息，但它可以通过 Google Assistant 或 Utilities 应用访问并与其交互，包括读取通知和查看图像。

此次更新引发了隐私担忧，导致用户禁用连接的应用或完全关闭 Gemini 应用活动。即使禁用后，谷歌仍会出于安全目的保留数据长达 72 小时。文章还指出，谷歌不愿允许完全删除 Gemini，因为 Android 平台为训练 AI 模型提供了关键数据。

对于决心完全删除 Gemini 的用户，本文提供了一个使用 ADB (Android Debug Bridge) 的复杂指南，涉及下载平台工具、启用 USB 调试以及运行特定命令。然而，作者发现这种方法不足以完全删除 Gemini，因为它仍然可以通过 Google 应用访问。推荐的（也是更安全的）替代方法是卸载 Google 应用的更新，然后禁用它，从而有效地从设备上移除 Gemini 和 Google。

---

## 3. 使用SQL注入接管超过六万间谍软件用户帐户

**原文标题**: Taking over 60k spyware user accounts with SQL injection

**原文链接**: [https://ericdaigle.ca/posts/taking-over-60k-spyware-user-accounts/](https://ericdaigle.ca/posts/taking-over-60k-spyware-user-accounts/)

埃里克·戴格尔在Android跟踪软件Catwatchful中发现了一个SQL注入漏洞，使他能够入侵超过6万个用户帐户。戴格尔创建了一个试用帐户后，发现用户数据一部分存储在Firebase中，一部分存储在catwatchful.pink的独立服务器上。虽然Firebase看起来很安全，但他发现了一个对catwatchful.pink服务器上servicios.php的未经身份验证的API调用。

通过对`getDevice`端点进行实验，他成功执行了SQL注入，从而绕过了身份验证并提取了整个用户数据库。该数据库包含所有62000多个Catwatchful帐户的明文用户名和密码。

数据库转储显示了与设备跟踪和管理相关的其他表，但用户凭据是主要目标。戴格尔向记者扎克·惠特克报告了该漏洞，后者联系了谷歌和Hosting.com。谷歌在安全浏览中标记了该网站，Hosting.com关闭了catwatchful.pink，有效地停止了该服务。

该服务后来在临时域名(xng.vju.temporary.site)上恢复，但在实施Web应用程序防火墙(WAF)来阻止SQL注入之前，该服务仍然存在漏洞。戴格尔强调，由于一个基本的SQL注入漏洞，他可以很容易地入侵一个据称“无法检测”和“无法卸载”的间谍软件应用程序。

---

## 4. 2025年电子邮件能传多远？

**原文标题**: Can an email go 500 miles in 2025?

**原文链接**: [https://flak.tedunangst.com/post/can-an-email-go-500-miles-in-2025](https://flak.tedunangst.com/post/can-an-email-go-500-miles-in-2025)

由于服务器配置错误，电子邮件被限制在500英里范围内的幽默前提，这在现代网络中似乎是不可能的。作者探讨了这种假设的限制是否能在2025年重现。

作者创建了一个程序（`connect`），尝试使用短超时（3毫秒）连接到服务器，模仿导致500英里限制的假定配置错误。 最初对美国各地大学进行的测试未能证明这一限制，因为尽管存在物理距离，连接仍然成功。 问题在于大学经常使用云托管提供商，无论大学的地理位置如何，这些提供商在地理位置上都可能很近。

然后，作者反过来，确定了具有ping时间表明其位于较远位置的大学。 虽然与较近大学（如罗格斯大学）的连接成功，但与大约500英里外的大学（如缅因大学）的连接是断断续续的，表明超时是一个因素。

调查随后转向邮件交换 (MX) 服务器，该服务器处理电子邮件。 作者发现，许多大学将其电子邮件外包给像pphosted.com和Google这样的提供商。 这些 MX 服务器的 ping 时间差异很大，通常比大学本身在地理位置上更近。 一些 MX 服务器（如宾夕法尼亚大学的）具有出乎意料的高 ping 时间，而斯坦福大学的 ping 时间几乎在“电子邮件范围”限制之内。 作者幽默地得出结论，虽然配置完全错误的服务器的 500 英里限制仍然是一种理论上的可能性，但由于外包和云托管，几乎不可能根据物理位置来确定可访问性。

---

## 5. AnyBlox：一种用于自解码数据集的框架 [pdf]

**原文标题**: AnyBlox: A Framework for Self-Decoding Datasets [pdf]

**原文链接**: [https://gienieczko.com/anyblox-paper](https://gienieczko.com/anyblox-paper)

很抱歉，我无法解读您提供的二进制格式PDF文件，因此无法提供关于文章《AnyBlox：一种自解码数据集的框架》的摘要。

---

## 6. 今天才知道可以用SVG制作“GIF”用于GitHub README.md文件

**原文标题**: TIL you can make "GIFs" with SVGs for GitHub README.md files

**原文链接**: [https://koaning.io/posts/svg-gifs/](https://koaning.io/posts/svg-gifs/)

本文重点介绍了一种在GitHub README.md文件中创建动画视觉效果的方法，该方法使用类似于GIF的SVG，但具有更高的分辨率和更小的文件大小。作者强调了使用动画SVG展示动态内容的优势。

关键在于GitHub直接支持README文件中的动画SVG。该过程包括使用`asciinema`记录终端会话，并使用`svg-term-cli`将这些记录转换为动画SVG文件。然后，只需拖放即可将生成的SVG文件轻松集成到README.md文件中。

文章解释说，动画是通过内置的SVG动画元素实现的，如`<animate>`、`<animateTransform>`和`<animateMotion>`。这些元素允许随时间推移动画SVG元素的属性、变换和运动，从而有效地创建“类似GIF”的动画。作者还指出了使用此方法可实现的令人惊讶的小文件大小（在他们的示例中为49Kb）和高分辨率。

---

## 7. Show HN: Jukebox – 免费开源的公平队列分组播放列表

**原文标题**: Show HN: Jukebox – Free, Open Source Group Playlist with Fair Queueing

**原文链接**: [https://www.jukeboxhq.com/](https://www.jukeboxhq.com/)

Show HN: Jukebox - 一款支持公平队列的免费开源群组歌单应用

---

## 8. Smollm3: 小型多语种长程推理LLM

**原文标题**: Smollm3: Smol, multilingual, long-context reasoner LLM

**原文链接**: [https://huggingface.co/blog/smollm3](https://huggingface.co/blog/smollm3)

SmolLM3：一款全新的、完全开源的30亿参数语言模型，旨在实现高效部署的同时保持竞争力的性能。它优于Llama-3.2-3B和Qwen2.5-3B，并与Qwen3和Gemma3等更大的40亿参数模型保持竞争力。创建者正在发布完整的工程蓝图，详细介绍构建混合推理模型的架构、数据混合和方法。

该模型的特点：

*   **预训练：** 在11T tokens上经过三个阶段的训练，逐步提升在网络、数学和代码领域的性能。
*   **架构：** 使用带有分组查询注意力（GQA）、用于长上下文的NoPE和用于训练稳定性的文档内掩码的Transformer解码器架构。
*   **多语言支持：** 支持英语、法语、西班牙语、德语、意大利语和葡萄牙语。
*   **长上下文：** 使用NoPE和YaRN支持高达128k的上下文长度。
*   **双模式推理：** 支持think/no_think两种推理模式。

训练过程包括架构修改、数据混合优化、长上下文扩展和推理中期训练。长上下文训练涉及逐步增加上下文窗口大小并使用YARN进行外推。推理中期训练使用了Open Thought的OpenThoughts3-1.2M以及NVIDIA的Llama-Nemotron-Post-Training-Dataset-v1.1的一个子集。监督微调（SFT）使用合成数据生成平衡推理和非推理模式，以解决数据集稀缺问题。最后，使用锚定偏好优化（APO）实现模型对齐。

---

## 9. 时之笛存档中使用的紧凑位集实现

**原文标题**: A compact bitset implementation used in Ocarina of Time save files

**原文链接**: [https://github.com/jb55/oot_bitset](https://github.com/jb55/oot_bitset)

本文介绍 `oot_bitset`，一个受《塞尔达传说：时之笛》启发的紧凑高效的标志系统，旨在以节省空间的方式存储大量布尔标志。它使用 C/C++ 和 Rust 实现，在 C 中提供仅包含头文件的零依赖解决方案，在 Rust 中提供一个小型依赖项。

其核心思想是将标志存储在一个 `uint16_t` 字数组中，每个字保存 16 个标志。一种巧妙的索引方案允许使用单个 16 位 ID 访问特定标志。ID 的前四位表示字中的位索引，其余位表示数组中字的索引。例如，ID `0xA5` 设置第 10 个字的第 5 位。这种方法节省空间，由于无分支位操作而速度快，并且可扩展。

本文提供了 C 和 Rust 的实际示例，演示了如何使用 `oot_bitset` 库来设置、获取和清除标志。它还包括两种语言的 API 参考，概述了可用的函数和宏。提供了 C/C++ 和 Rust 环境的安装说明。最后，它解释了如何根据所需的标志数量确定字数组的大小，为各种项目需求提供灵活性。标志的最大数量为 `words * 16`。

---

## 10. 一项新的球体堆积纪录源于意想不到的来源

**原文标题**: New sphere-packing record stems from an unexpected source

**原文链接**: [https://www.quantamagazine.org/new-sphere-packing-record-stems-from-an-unexpected-source-20250707/](https://www.quantamagazine.org/new-sphere-packing-record-stems-from-an-unexpected-source-20250707/)

球体堆积领域的新秀博阿兹·克拉塔格在长期存在的球体堆积问题上取得了重大突破，该问题旨在最大化球体在高维空间中的有效排列。几个世纪以来，数学家们一直试图确定最密集的排列方式，这在密码学和通信领域都有应用。克拉塔格的工作显著提高了以往的记录，可能接近最佳堆积密度。

他的方法涉及复兴克劳德·安布罗斯·罗杰斯的一项旧技术，该技术侧重于在晶格内塑造椭球体以创建密集的球体堆积。虽然之前的尝试侧重于寻找有效的晶格，但克拉塔格利用他在凸几何方面的专业知识，开发了一种在晶格内生长椭球体的新方法，从而实现了更高效的球体堆积。他的方法涉及一个随机过程，即扩展和收缩椭球体的边界，并在其遇到晶格点时冻结生长方向。

克拉塔格的成果引发了关于最佳高维堆积性质的新一轮讨论，特别是关于有序/对称与无序的作用。他的工作表明，通过基于晶格的堆积，秩序和对称性可能仍然是一种可行的方法。这些发现也引发了关于当前堆积与理论极限的接近程度的问题，可能对密码学和通信产生影响。克拉塔格希望他的工作能够弥合凸几何和晶格理论之间的差距，促进该领域的未来发展。

---

## 11. 论仪式的意义

**原文标题**: On The Meaning of Ritual

**原文链接**: [https://alicemaz.substack.com/p/on-the-meaning-of-ritual](https://alicemaz.substack.com/p/on-the-meaning-of-ritual)

无法访问文章链接。

---

## 12. Memstop：内存不足时使用LD_PRELOAD延迟进程执行

**原文标题**: Memstop: Use LD_PRELOAD to delay process execution when low on memory

**原文链接**: [https://github.com/surban/memstop](https://github.com/surban/memstop)

Memstop：防止并行处理系统中内存耗尽崩溃的轻量级工具。它通过延迟进程执行，直到系统内存可用百分比达到可配置值来实现。这是通过 LD_PRELOAD 实现的，它在应用程序的 main 函数之前将 Memstop 作为共享对象加载。

Memstop 从 `/proc/meminfo` 读取内存信息，基于 `MEMSTOP_PERCENT` 环境变量（默认为 10%）计算所需的可用内存，并等待直到该百分比达到。一旦有足够的内存可用，它会将控制权释放给应用程序。

它在并行构建系统（如 `make -j`）、批处理系统和高内存应用程序中特别有用。要使用 Memstop，您需要一个 GCC 编译器、一个带有 `/proc/meminfo` 的 Linux 系统和 Make。使用 `make` 构建后，可以将其安装到系统范围内或手动安装。

配置通过环境变量完成：`MEMSTOP_PERCENT` 设置所需的内存百分比，`MEMSTOP_VERBOSE` 启用详细输出以进行调试。启用详细模式后，内存统计信息和阻塞状态将输出到 stderr。该项目以 GPLv3 许可。

---

## 13. 展示HN：离线象棋谜题应用

**原文标题**: Show HN: OffChess – Offline chess puzzles app

**原文链接**: [https://offchess.com](https://offchess.com)

离线棋谜是一款手机应用，用于离线解决国际象棋谜题。它拥有超过10万个谜题的题库，无需网络连接即可访问。谜题有难度评级，用户根据其表现相对于谜题评级获得或失去分数，从而为练习提供竞争元素。该应用允许用户跟踪他们的表现和统计数据，以监测进步。定制也是一个特色，提供各种主题来个性化棋盘的外观。该应用强调可访问性和便利性，允许用户随时随地练习国际象棋，无需考虑Wi-Fi可用性。它在App Store和Google Play Store上均有提供。应用信息包括指向主页、关于、隐私和联系方式等部分的链接，版权归OffChess所有，年份为2025年。

---

## 14. Berry脚本：用于微控制器的轻量级嵌入式脚本语言

**原文标题**: Berry Script: lightweight embedded scripting language for microcontrollers

**原文链接**: [https://berry-lang.github.io/](https://berry-lang.github.io/)

Berry Script 是一种超轻量级、动态类型的脚本语言，专门为资源受限的嵌入式设备（如微控制器）而设计。其主要特点是体积小巧；解释器核心小于 40KB，并且可以在 ARM Cortex M4 CPU 上以少于 4KB 的堆空间运行。

Berry 使用 ANSI C99 构建，并结合了单遍编译器和基于寄存器的虚拟机 (VM) 来优化性能。并非所有数据类型都被视为类对象；诸如整数、浮点数、布尔值和字符串之类的基本类型直接处理以提高速度，而列表、映射和范围等更复杂的类型则是类对象。这种混合方法，结合基于寄存器的 VM，旨在最大限度地提高资源有限环境中的效率。简而言之，Berry 优先考虑小代码尺寸和高效执行，以便在资源稀缺的设备上提供脚本功能。

---

## 15. Attimet (YC F24) – 量化交易研究实验室 – 招聘创始研究员

**原文标题**: Attimet (YC F24) – Quant Trading Research Lab – Is Hiring Founding Researcher

**原文链接**: [https://www.ycombinator.com/companies/attimet/jobs/6LaQIc5-founding-researcher-quant](https://www.ycombinator.com/companies/attimet/jobs/6LaQIc5-founding-researcher-quant)

Attimet，一家由Y Combinator F24支持的初创公司，正在招募一位创始研究员/量化分析师加入其位于旧金山的实验室，该实验室专注于将人工智能和机器学习应用于金融市场，尤其是期权交易。公司目标是构建能够利用结构化和非结构化数据进行适应、预测和行动的时间人工智能系统。

该职位包括领导预测模型、强化学习代理和信号发现工作流程的开发，整合另类数据，并在模拟和实盘交易环境中测试假设。理想的候选人应在机器学习/人工智能（特别是时间序列、预测和表征学习）方面拥有深厚的专业知识，具有扎实的编程背景（Python、数据管道、AWS/GCP）以及模型生产部署经验。不需要金融市场经验。

Attimet强调研究与实盘部署之间的快速迭代循环，让研究人员能够直接看到他们的工作对市场回报的影响。公司提供10万美元至15万美元的年薪以及0.25%至1.00%的股权。这是一个由3人组成的小团队，创始人拥有来自Optiver、DRW和Argo AI的经验。

---

## 16. Epanet-JS

**原文标题**: Epanet-JS

**原文链接**: [https://macwright.com/2025/07/03/epanet-placemark](https://macwright.com/2025/07/03/epanet-placemark)

Tom MacWright 重点介绍了 epanet-js，这是 Iterating 公司的 Luke Butler 和 Sam Payá 开发的一款新的 Web 应用程序，它将现代 Web 地图与 EPANET 水力模拟算法相结合，用于水务规划。他特别热衷于此，因为 epanet-js 利用了他之前项目 Placemark 的代码，Placemark 是一个在 MIT 许可下发布的开源地图数据编辑工具。

MacWright 强调，看到其他人利用他的开源代码建立业务是一个理想的结果，他认为“乐于助人”和创造具有持久影响力的软件是关键的动机。他承认 Placemark 缺乏明确的定位，并将 epanet-js 视为一个完美的应用程序。

MacWright 还提到，Iterating 已经回馈了开源 Placemark 项目，并且已经开源了核心的 epanet-js 库。他们以功能性源代码许可证发布了该 Web 应用程序，该许可证规定新的代码贡献在两年后开源。

Epanet-js 提供了一个基于浏览器的、使用 WASM 引擎的模拟，它提供了一种比传统的、昂贵的、仅适用于 Windows 的水力模拟软件更易于访问且更经济实惠的替代方案。MacWright 祝贺创作者，并鼓励该领域的从业者尝试一下。

---

## 17. 水星：基于扩散的超快速语言模型

**原文标题**: Mercury: Ultra-fast language models based on diffusion

**原文链接**: [https://arxiv.org/abs/2506.17298](https://arxiv.org/abs/2506.17298)

这篇于2025年6月17日提交的arXiv论文介绍了“Mercury”，Inception Labs基于扩散方法的新一代商业级大型语言模型（LLMs）。这些模型利用Transformer架构，并经过训练可以并行预测多个token，从而实现超快性能。首发产品“Mercury Coder”专为编码应用而设计，提供Mini和Small两种尺寸。

独立评估显示，Mercury Coder Mini和Small在NVIDIA H100 GPU上分别实现了1109 tokens/秒和737 tokens/秒的最先进吞吐量。该性能比速度优化的前沿模型快达10倍，同时保持了相当的代码生成质量。该论文详细介绍了这些模型在各种代码基准测试中跨不同语言和用例的性能。通过Copilot Arena进行的真实世界验证显示，Mercury Coder在质量方面排名第二，并且是总体上最快的模型。

作者还发布了公共API和一个免费的playground，用于访问和实验。该论文强调了核心作者的同等贡献，并列出了Inception Labs的多位个人。涵盖的主题包括计算与语言（cs.CL）、人工智能（cs.AI）和机器学习（cs.LG）。

---

## 18. Show HN: 我做了一个工具来解决窗口管理问题

**原文标题**: Show HN: I built a tool to solve window management

**原文链接**: [https://aboveaverageuser.com/smartswitcher](https://aboveaverageuser.com/smartswitcher)

智能切换器是一款数据驱动的工具，旨在提高窗口切换的速度和效率。它通过记录窗口访问数据来学习用户行为，并使用预测算法来建议用户接下来最有可能想要切换到的窗口。用户可以使用快捷键覆盖预测，从而训练系统以提高准确性。

主要功能包括加密本地数据存储、持续数据备份和验证，以及即使对于同一应用程序的多个实例也能进行独特的窗口识别。预测算法是实验性的，并且会随着时间的推移而改进，未来计划允许匿名共享成功率数据以改进算法。

开发者AboveAverageUser概述了一个专注于性能、稳定性以及算法改进的路线图，并且正在开发MacOS版本。

智能切换器适用于Windows 10/11，并为个人和商业用途提供入门定价选项，包括限时折扣和更新选项。购买享有30天无风险保证。

该产品提供清晰的服务条款，定义了许可使用、限制、知识产权和责任限制。详细的隐私政策解释了数据收集、使用、存储、安全性以及用户权利，强调用户数据经过加密并本地存储。提供演示版本供用户在购买前测试功能。

---

## 19. 我用o3从我保存的Pocket链接中分析了自己的个人资料。

**原文标题**: I used o3 to profile myself from my saved Pocket links

**原文链接**: [https://noperator.dev/posts/o3-pocket-profile/](https://noperator.dev/posts/o3-pocket-profile/)

利用o3 AI模型从Pocket文章生成个人档案实验

---

## 20. 观看之镜：基于拉普拉斯金字塔变形的生成式畸变图像

**原文标题**: LookingGlass: Generative Anamorphoses via Laplacian Pyramid Warping

**原文链接**: [https://studios.disneyresearch.com/2025/06/09/lookingglass-generative-anamorphoses-via-laplacian-pyramid-warping/](https://studios.disneyresearch.com/2025/06/09/lookingglass-generative-anamorphoses-via-laplacian-pyramid-warping/)

《透镜：基于拉普拉斯金字塔扭曲的生成式变形图像》一文提出了一种利用生成式潜在校正流模型创建变形图像的新方法。传统的变形图像是有意扭曲的，只有从特定视角或使用特殊设备才能识别。这项研究旨在改进这一概念，通过生成变形图像，使其在仍然扭曲的情况下，在直接观看时仍保留有效但不同的解读。

其核心贡献是引入了“拉普拉斯金字塔扭曲”，这是一种频率感知图像扭曲技术，可以为这些双重解读图像生成高质量的视觉效果。这项技术对于生成既能成功地扭曲以用于变形观看，又能让肉眼识别的有意义视觉效果至关重要。

作者（Pascal Chang, Sergio Sancho, Jingwei Tang, Markus Gross, 和 Vinicius Azevedo）将“视觉字谜”的概念扩展到潜在空间模型和更广泛的空间变换集。这使得创造新的生成式感知错觉成为可能，从而突破了传统变形图像的界限。该作品计划在 CVPR 2025 上发表。

---

## 21. 关于VSC8512，微芯（官方）不会告诉你的事

**原文标题**: What Microchip doesn't (officially) tell you about the VSC8512

**原文链接**: [https://serd.es/2025/07/04/Switch-project-pt3.html](https://serd.es/2025/07/04/Switch-project-pt3.html)

本文详细介绍了作者在没有NDA的情况下，理解和操控VSC8512 PHY芯片的SERDES TX均衡器设置的过程，因为Microchip公司并未完全公开相关文档。作者选择VSC8512的原因是它具备QSGMII接口，并且最初认为其文档是开放的。

作者利用公开资源，包括VSC8512数据手册、硬件设计核对清单、VSC8504（一种类似芯片）的IBIS-AMI模型、参考设计指南，以及最重要的，MIT许可的Microchip Ethernet Switch API (MESA) 代码。

通过分析MESA代码和相关文件，作者发现了关于SERDES的关键信息，包括参数名称，如OB_LEV、OB_PREC、OB_POST0、OB_POST1和转换速率控制。作者发现VSC8512本质上是VSC742x交换机ASIC的精简版本，并识别出潜在有用的寄存器接口：IEEE标准MDIO、间接MMD以及通过页面/bank索引访问的厂商自定义寄存器。作者还提到了两个未公开的页面：测试 (0x2a30) 和令牌环/黑魔法 (0x52b5)，以及宏配置总线 (MCB)。

作者探索了VSC8512的MCU接口，在MESA代码中找到了诸如`vtss_phy_cfg_ob_post0`等函数，这些函数控制着SERDES设置。该函数允许作者调整OB_POST0参数，从而影响传输信号的去加重和眼图张开。最终目标是在缺乏官方文档的情况下，优化超出默认设置的信号完整性。

---

## 22. CPython JIT编译器两周年回顾

**原文标题**: Reflections on 2 years of CPython's JIT Compiler

**原文链接**: [https://fidget-spinner.github.io/posts/jit-reflections.html](https://fidget-spinner.github.io/posts/jit-reflections.html)

Ken Jin博客反思CPython实验性JIT编译器的头两年：强调积极进展与待改进之处

**优点：** Jin强调了围绕JIT形成的强大社区，指出越来越多贡献者积极参与其开发。他还指出JIT的设计相对容易教授和引导新开发者，这对它的长期可持续性至关重要。

**有待改进：** 性能是一个主要问题。CPython 3.13 JIT通常比解释器慢，虽然3.14在特定场景（尤其是在AArch64上）显示出一些加速，但在x64上使用现代编译器时，其性能通常比解释器更差。3.14中缺少主要的优化器功能被认为是关键原因。此外，最初的媒体报道不准确地描述了JIT的性能，造成了不切实际的期望。

**展望：** 尽管面临挑战，Jin仍然保持乐观。他相信不断壮大的社区以及改进JIT的并行努力将在未来的版本中带来性能提升，可能从3.15开始实现个位数的百分比加速。他鼓励用户测试JIT并提供数据以帮助其开发。他承认他观察到的性能提升不足主要是在x64上，而其他架构可能存在他未知的提升。

---

## 23. SIMD.info – 主要SIMD引擎C语言内联函数参考工具

**原文标题**: SIMD.info – Reference tool for C intrinsics of all major SIMD engines

**原文链接**: [https://simd.info/](https://simd.info/)

SIMD.info是一个参考工具，专注于提供关于主要SIMD（单指令多数据）引擎的C内在函数信息。该网站本质上是一个搜索引擎，允许用户查找与这些内在函数相关的详细信息。它是一个面向开发人员和程序员的资源，他们正在使用SIMD技术，并且需要一种快速简便的方法来查找特定的C内在函数及其相关信息。该网站的核心目的是促进SIMD内在函数的有效使用和理解。

---

## 24. 运行证书透明度日志

**原文标题**: Running a Certificate Transparency log

**原文链接**: [https://words.filippo.io/run-sunlight/](https://words.filippo.io/run-sunlight/)

本文倡导有闲置资源的个人或组织运行证书透明度 (CT) 日志，认为现在运行日志比以往更便宜更容易。CT 日志对网络安全至关重要，可确保证书颁发机构的诚实性，并提醒网站所有者注意未经授权的证书颁发。目前独立日志运营商的数量不足，因此新建日志是对互联网安全的重大贡献。

作者和 Let's Encrypt 最近推出的静态 CT API 允许通过静态文件提供日志服务，从而使操作更适合 CDN 和 S3。Let's Encrypt 赞助的实现 Sunlight 进一步简化了写入路径，且依赖性极低。

在 2025 年运行日志需要一台配置适中的服务器（ECC 内存、4 核、2 GB RAM）、2 Gbps 的峰值出站带宽（兼容 CDN）以及 3-5 TB 的冗余存储（SSD 或兼容 S3 的对象存储，带 200GB SSD 缓存）。至少需要两个人来满足联系要求。

持久性至关重要，以避免数据丢失，备份并不适用。持续的工作包括监控 CT 策略、更新实现以及每年轮换日志分片，并承诺至少三年。本文鼓励潜在运营商使用专门工具 Sunlight，并在 transparency.dev Slack、ct-policy 邮件列表或 Sunlight issue tracker 上与社区互动。

---

## 25. 宫胁昭造林法

**原文标题**: The Miyawaki Method of micro-forestry

**原文链接**: [https://www.futureecologies.net/listen/fe-6-5-the-method](https://www.futureecologies.net/listen/fe-6-5-the-method)

本文介绍了宫胁昭微型森林法，这种快速创建茂密原生森林的技术正日益普及。本文主要围绕该方法的名字来源——日本植物学家宫胁昭博士的生平和工作展开，他研究杂草的生态学，并受到植物社会学的影响，植物社会学研究植物群落、其组成、结构、分布以及与环境的相互作用。

宫胁昭的方法包括在小面积区域内密集种植多种本地树种，旨在加速顶级森林生态系统的发展。本文还涉及对其有效性的质疑，想知道他的植树造林方法是科学还是疯狂。

---

## 26. 探索PHP中的协程

**原文标题**: Exploring Coroutines in PHP

**原文链接**: [https://doeken.org/blog/coroutines-in-php](https://doeken.org/blog/coroutines-in-php)

本文探讨了编程中协程的概念，尤其是在PHP环境中的应用。协程是一种可以暂停执行并在以后恢复的函数，这与持续运行直至完成的常规函数不同。挂起时，协程可以返回值，并在恢复时接收值，使其成为双向的。它们在挂起时也会保留其内部状态。

本文区分了非对称协程（控制权仅返回给调用者）和对称协程（控制权可以在协程之间传递），以及无栈协程（仅在最外层函数挂起）和有栈协程（可以从嵌套函数挂起）。

PHP通过生成器（PHP 5.5中引入）和纤程（PHP 8.1中引入）来实现协程。生成器是无栈的非对称协程，可以使用`current()`和`next()`等方法暂停和恢复，并可以使用`send()`发送值。另一方面，纤程提供了一种实现有栈协程的方法。纤程创建为实例，并使用`start()`显式启动。它们使用`Fiber::suspend()`暂停，并使用`$fiber->resume()`继续执行。纤程允许在嵌套函数中挂起，并可以使用`throw()`处理异常。虽然生成器本身就是协程，但纤程提供了一个工具箱来实现更复杂、有栈的协程，从而可能产生更清晰、更模块化的代码。

---

## 27. 因为ChatGPT错误地认为某个功能存在而添加该功能

**原文标题**: Adding a feature because ChatGPT incorrectly thinks it exists

**原文链接**: [https://www.holovaty.com/writing/chatgpt-fake-feature/](https://www.holovaty.com/writing/chatgpt-fake-feature/)

2025年7月，Soundslice的Adrian Holovaty发现大量用户将ChatGPT会话的屏幕截图上传到他们的乐谱扫描系统，尽管Soundslice并不支持ASCII指法谱，而截图中恰恰是这种记谱法。

Holovaty发现ChatGPT错误地宣传Soundslice为一个可以导入和播放ASCII指法谱的平台，误导用户相信存在此功能。这使Soundslice陷入困境，因为他们现在接收到期望他们并不提供的功能的用户。

Soundslice并没有简单地发布免责声明，而是选择拥抱这一意外的需求。他们开发了一个定制的ASCII指法谱导入器，以满足被ChatGPT误导的新用户的需求。他们还更新了用户界面文案以反映这一新功能。

Holovaty承认仅基于虚假信息开发功能是很奇怪的。虽然他很高兴能提供一个有用的工具，但他质疑产品开发是否应该由人工智能产生的虚假信息驱动。他认为Soundslice可能是第一家因ChatGPT的错误声明而添加功能的公司，这引发了人们对人工智能幻觉未来对产品开发影响的质疑。

---

## 28. 为什么没有好的恐龙电影？

**原文标题**: Why are there no good dinosaur films?

**原文链接**: [https://briannazigler.substack.com/p/why-are-there-no-good-dinosaur-films](https://briannazigler.substack.com/p/why-are-there-no-good-dinosaur-films)

无法访问文章链接。

---

## 29. 当Figma开始设计我们

**原文标题**: When Figma starts designing us

**原文链接**: [https://designsystems.international/ideas/when-figma-starts-designing-us/](https://designsystems.international/ideas/when-figma-starts-designing-us/)

本文批判了Figma的功能对设计流程的影响，认为虽然其功能强大，但正在将设计师推向以工程为中心的模式，从而扼杀创造力和探索。作者自Figma早期阶段就开始使用，认为自动布局和开发模式等功能，虽然旨在提高效率和协作，却导致了过早的优化和设计空间的缩小。

例如，自动布局鼓励设计师在早期就严格构建设计，限制了实验和灵活性。开发模式虽然旨在弥合设计和开发之间的差距，但可能会加强孤岛式工作流程，使设计师在孤立状态下过度润色设计，从而阻止开发人员做出创造性贡献。

作者认为，这些功能导致了数字设计领域的“单一文化”，共同的约束导致了同质化的结果。在倡导设计师和工程师之间协作的同时，作者强调这不应意味着设计师简单地采用工程实践。相反，目标应该是整合不同的观点。

核心问题是，Figma对结构的强调超过了自发性，可能会扼杀对于创新设计至关重要的混乱、质疑和趣味性。作者敦促设计师意识到这些工具如何塑造他们的实践，并寻求优先考虑探索和发现的工具。

---

## 30. François Chollet：弧奖以及我们如何实现通用人工智能 [视频]

**原文标题**: François Chollet: The Arc Prize and How We Get to AGI [video]

**原文链接**: [https://www.youtube.com/watch?v=5QcCeSsNRks](https://www.youtube.com/watch?v=5QcCeSsNRks)

鉴于所提供的内容仅为YouTube样板文本（版权、条款等），无法提供题为“François Chollet：Arc奖及我们如何实现AGI [视频]”的文章摘要。

文本中没有任何与François Chollet、Arc奖或通用人工智能(AGI)相关的信息。因此，摘要将完全是推测性的，并且不准确。

要概括实际内容，需要实际视频或文字稿。

---

## 31. 哥伦比亚大学随机数灯塔

**原文标题**: CU Randomness Beacon

**原文链接**: [https://random.colorado.edu/](https://random.colorado.edu/)

科罗拉多大学博尔德分校随机数灯塔是一个旨在提供公开可验证且不可预测的随机数的系统。其目的是满足各种应用对安全透明随机数源的需求，包括密码学、彩票、科学模拟和投票系统。

该灯塔通过每分钟（或指定的其他间隔）生成一个新的随机值，并将其与密码学证明一起发布，以确保完整性并防止操纵。该设计确保即使是灯塔运营者也无法预测随机性，并且任何人都可以验证已发布值的完整性。

主要特点和优势包括：

*   **公开可验证性：** 任何人都可以独立验证随机数的正确性和完整性。
*   **不可预测性：** 该设计旨在确保未来的值是不可预测的。
*   **透明性：** 所有生成的值和证明都公开可用。
*   **可靠性：** 该系统设计用于连续运行和可用性。
*   **安全性：** 采用密码学技术来防止篡改并确保随机数是可信的。

科罗拉多大学随机数灯塔为需要可信和可验证随机数来源的应用程序提供了宝贵的资源，满足了各个领域的关键需求。它由科罗拉多大学博尔德分校维护和运营，通过提供这项重要服务为社区做出贡献。

---

## 32. 火狐浏览器还行，但运营它的人不行。

**原文标题**: Firefox is fine. The people running it are not

**原文链接**: [https://www.theregister.com/2025/07/08/firefox_isnt_dead/](https://www.theregister.com/2025/07/08/firefox_isnt_dead/)

利亚姆·普罗文的文章认为，尽管火狐浏览器仍然是一个可行且通常优于其竞争对手的选择，但Mozilla的管理层正在辜负这个项目。他指出火狐持续的速度改进证明浏览器本身不是问题所在。相反，他批评Mozilla的领导层犯了一系列错误和错失良机。

普罗文重点提到了关键的例子，例如取消Rust和Servo项目（均为内部开发的技术）、放弃FirefoxOS（被投资者重新命名为KaiOS）以及收购一家广告公司，同时承诺不出售用户数据。他认为这些决定反映了缺乏方向和专注于追逐潮流（如人工智能），而不是核心浏览器开发。

他将Mozilla的问题归因于其对谷歌资金的依赖，这消除了创新和有效竞争的需要。他认为Mozilla的领导层缺乏商业头脑，并且更加关注经济利益，而不是改进浏览器和倡导开放的Web标准。

最终，普罗文提出了一个激进的解决方案：Mozilla应该成为一个非营利组织，专门致力于开发参考实现Web浏览器并积极捍卫Web标准。他认为这是真正利用Mozilla技术创新并确保仍然有一个供应商中立的浏览器引擎可用的唯一方法。他强调Mozilla应该支持其创新的独立衍生产品，而不是试图直接从中获利。他强调，长期批评家杰米·扎温斯基支持这一观点。

---

## 33. 彩色铅笔的耐光性测试

**原文标题**: Lightfastness Testing of Colored Pencils

**原文链接**: [https://sarahrenaeclark.com/lightfast-testing-pencils/](https://sarahrenaeclark.com/lightfast-testing-pencils/)

莎拉·雷娜·克拉克的文章详细介绍了对50多个彩色铅笔品牌进行的为期6个月的耐光性测试。耐光性，即暴露在光线下随时间推移抵抗褪色的能力，对于希望作品持久的艺术家至关重要。文章解释了什么是耐光性，它对于展示、赠送或销售艺术作品的重要性，以及何时不那么重要（例如，用于练习或数字复制）。

作者概述了三种测量耐光性的方法：蓝羊毛标准、ASTM D6901（针对彩色铅笔）和制造商评级，并强调制造商的声明可能不可靠。克拉克的测试方法包括将彩色铅笔色样暴露在阳光下6个月，将它们与对照样品进行比较，使用蓝羊毛条进行基准测试，并使用CIEDE2000公式进行颜色扫描以量化褪色。

然后，文章介绍了特定品牌的结果，包括 Arrtx、Arteza（专家级和粉彩级）、BiC Intensity、Black Widow、Blick Studio Artist 和 Brutfuner（各种类型）。对于每个品牌，作者都提供了有关制造商耐光性声明（或缺乏声明）、耐光性铅笔的百分比（在蓝羊毛标准上得分 BW6 或更高）、平均褪色、最佳和最差表现者以及购买地的信息。分析揭示了制造商评级的不一致以及不同品牌和颜色之间耐光性的显着差异，突出了独立测试的重要性。

---

## 34. 蜂蜜保鲜持久的化学秘密

**原文标题**: The chemical secrets that help keep honey fresh for so long

**原文链接**: [https://www.bbc.com/future/article/20250701-the-chemical-secrets-that-help-keep-honey-fresh-for-so-long](https://www.bbc.com/future/article/20250701-the-chemical-secrets-that-help-keep-honey-fresh-for-so-long)

本文解释了蜂蜜为何具有非凡的保质期，原因在于其独特的化学成分和制作过程。 许多食物因细菌、真菌和霉菌等微生物的生长而腐败，而蜂蜜则能抵抗这种腐败。

奥秘在于蜜蜂将花蜜转化为蜂蜜的细致过程。 蜜蜂浓缩花蜜，去除多余水分，并通过酶增加酸度。 这个过程将水分含量显著降低到 15% 到 18% 之间，创造了一种“低水分活度”的状态。 微生物需要水分才能生长，而高糖浓度、低水分含量和酸度的结合使它们几乎不可能在蜂蜜中生存。 用翅膀扇动蜂蜜有助于蒸发剩余的水分。

将蜂蜜密封在罐子里进一步保护它，限制氧气供应。 低水分活度、酸度和有限的氧气相结合，为变质创造了一个不利的环境。 虽然暴露在空气中的蜂蜜仍然可能接触到细菌和水分，但蜂蜜的固有特性有助于其卓越的保质期。 本文还简要介绍了如何通过添加水和特定微生物来故意使蜂蜜变质，以制作蜂蜜酒。

---

## 35. Show HN: 纽约地铁模拟器和线路设计器

**原文标题**: Show HN: NYC Subway Simulator and Route Designer

**原文链接**: [https://buildmytransit.nyc](https://buildmytransit.nyc)

此“Show HN”帖子介绍BuildMyTransit，一款纽约市地铁模拟器和线路设计器。该项目允许用户模拟纽约市地铁系统的运营并设计自己的地铁线路。尽管帖子本身很简短，但关键在于该平台的存在，表明它提供了一个用于以下用途的数字环境：

*   **地铁模拟：** 用户可以观察并与纽约市地铁的模拟版本互动，可能涉及列车调度、信号和客流。
*   **线路设计：** 用户可以创建和自定义自己的地铁线路，可能会试验车站位置、轨道布局和线路配置。

潜在的目标受众包括交通爱好者、城市规划专业的学生以及任何有兴趣了解或试验复杂地铁系统的人。该帖子直接宣布并邀请用户探索“BuildMyTransit”平台。帖子中没有提供更多细节，关于该工具的功能、能力和访问方式（例如，基于网络，可下载的应用程序）的更多信息需要直接访问 BuildMyTransit 网站或平台。

---

## 36. Unix 中 errno 有限性的问题是什么？

**原文标题**: What is going on in Unix with errno's limited nature

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/unix/ErrnoWhySoLimited](https://utcc.utoronto.ca/~cks/space/blog/unix/ErrnoWhySoLimited)

Chris Siebenmann的博客（漫游思绪）正经历爬虫流量激增，特别是来自使用旧版Chrome User-Agent的来源，很可能是为了LLM训练而进行的数据收集。为了应对这种情况，他已采取措施阻止这些浏览器，您可能会看到此消息，因为您的浏览器被标记为可疑。

如果您使用的是现代浏览器，但被错误地阻止，他建议通过他的大学电子邮件地址与他联系，并提供User-Agent字符串以进行故障排除。

一个重要的问题是archive.*服务（archive.today、archive.ph、archive.is等），它们的行为类似于恶意爬虫。它们使用旧的Chrome User-Agent值，拥有分散的IP地址，有时还会伪造反向DNS条目来模仿Googlebot。这使得它们与不良行为者无法区分，并迫使对其进行阻止。他建议使用archive.org，因为它是一个行为更规范的存档爬虫，可以访问他的博客。作者表示这些问题始于2025年初。

---

## 37. 使用uv的依赖解析器解决Wordle

**原文标题**: Solving Wordle with uv's dependency resolver

**原文链接**: [https://mildbyte.xyz/blog/solving-wordle-with-uv-dependency-resolver/](https://mildbyte.xyz/blog/solving-wordle-with-uv-dependency-resolver/)

本文详细介绍了如何使用 uv 的依赖关系解析器来解决流行的文字游戏 Wordle，其灵感来自于之前使用 Poetry 解决数独的项目。核心思想是将 Wordle 问题表示为一组具有版本约束的互连 Python 包，并利用 uv 的解析器来找到有效解（一个单词）。

作者创建了几种类型的包：“单词”包（代表可能的解决方案单词）、“位置”包（代表特定位置的字母）和“反馈”包（编码来自猜测的线索）。猜测和反馈（绿色、黄色或空白）被转化为对这些包的依赖关系。例如，绿色字母约束了相应的位置包，而黄色和空白字母则影响了该字母允许出现的位置。

一个关键挑战是如何表示“至少一个”约束（例如，一个字母必须在位置 1、2 或 3 中）。这是通过使用“可能位置”包来实现的，该包枚举了特定字母可以出现的位置。然后，反馈包依赖于位置包。作者巧妙地使用负依赖关系规范（“!=”）来表达这些复杂的约束。

作者利用 uv 将 wheel 输出到目录的功能，然后使用 `--find-links` 告诉 uv 仅从该本地文件夹解析。解析器基于 uv 创建的锁文件迭代地猜测单词，并随着收到反馈而调整依赖关系列表。一个简单的评分函数会优先选择具有更多不同、频繁字母的单词，以实现高效猜测。源代码可在 GitHub 上找到。

---

## 38. 我的第一个经过验证的命令式程序

**原文标题**: My first verified imperative program

**原文链接**: [https://markushimmel.de/blog/my-first-verified-imperative-program/](https://markushimmel.de/blog/my-first-verified-imperative-program/)

本文介绍了即将发布的Lean 4.22版本中的新验证基础设施Std.Do，旨在简化命令式程序属性的证明。文章以判断整数列表是否包含两个和为零的不同元素的例子，展示了该工具的功能。

文章将Lean的交互式验证方法与Dafny和Verus等更自动化的系统进行了对比。Dafny和Verus严重依赖SMT求解器，虽然效率很高，但失败时调试难度大，而Lean提供了更具交互性的体验。如果像"grind"这样的自动化证明策略失败，用户可以手动构建证明，利用Lean强大的编辑器支持、丰富的定理库和一个小型且可信的内核。

作者强调了Lean设计的优势，包括能够利用现有库（如mathlib），以及Lean的数据结构完全在Lean内部实现和验证。他们认为，凭借其交互性、可信架构以及对已验证证明库的依赖，Lean在现实世界的程序验证方面具有优势。文章还演示了如何使用Lean轻松验证示例问题的函数式实现。最终，作者强调了像Lean这样的交互式系统在增强形式验证的可靠性和信任方面的重要性。

---

## 39. 巴比伦颂歌，失落千年后重见天日

**原文标题**: Hymn to Babylon, missing for a millennium, has been discovered

**原文链接**: [https://phys.org/news/2025-07-hymn-babylon-millennium.html](https://phys.org/news/2025-07-hymn-babylon-millennium.html)

一首失落千年，赞颂巴比伦的赞美诗被慕尼黑大学的恩里克·希门尼斯与巴格达大学合作重新发现。这项发表在《伊拉克》期刊上的发现，揭示了一段文字，提供了公元前一千年左右巴比伦居民生活的见解。

这首以楔形文字写在泥板上的赞美诗，是通过一个名为“电子巴比伦图书馆平台”的AI辅助平台识别的，该平台对楔形文字碎片进行数字化处理，并帮助将其拼接在一起。该平台识别出与这首重新发现的赞美诗相关的其他30份手稿，使学者们能够完全破译它。

这首赞美诗赞扬了巴比伦，描述了它的建筑、赋予生命力的幼发拉底河以及城市社会的各个方面。值得注意的是，它提供了关于女性作为女祭司角色的新信息，并突出了巴比伦人与外国人之间的尊重互动。这首赞美诗在学校中的广泛使用表明了它在当时的流行程度。重新发现的文本包含250行，意义重大，因为现存的美索不达米亚文学很少描述自然现象。巴比伦遗址位于巴格达以南，是联合国教科文组织世界遗产地。

---

## 40. 初级职位不会消失

**原文标题**: Junior Roles Aren't Going Away

**原文链接**: [https://iamcharliegraham.substack.com/p/junior-roles-arent-going-away](https://iamcharliegraham.substack.com/p/junior-roles-arent-going-away)

无法访问文章链接。

---

## 41. 马可·鲁比奥冒充者利用AI语音致电高级官员

**原文标题**: A Marco Rubio impostor is using AI voice to call high-level officials

**原文链接**: [https://www.washingtonpost.com/national-security/2025/07/08/marco-rubio-ai-imposter-signal/](https://www.washingtonpost.com/national-security/2025/07/08/marco-rubio-ai-imposter-signal/)

无法访问文章链接。

---

## 42. 大型语言模型不应取代治疗师

**原文标题**: LLMs should not replace therapists

**原文链接**: [https://arxiv.org/abs/2504.18412](https://arxiv.org/abs/2504.18412)

这篇于2025年4月25日提交至arXiv的论文论证了不应使用大型语言模型(LLM)取代人类治疗师。该论文由Jared Moore、Declan Grabb、William Agnew、Kevin Klyman、Stevie Chancellor、Desmond C. Ong和Nick Haber撰写，提供的证据表明，目前的LLM尚不适合扮演此类角色。

作者首先回顾了主要医疗机构的治疗指南，强调了治疗联盟在成功治疗中的重要性。然后，他们评估了LLM（以GPT-4o为例）在复制和遵守治疗关系原则方面的能力。

他们的发现揭示了LLM的两个主要缺点：1) 它们对患有精神健康状况的个体表达出污名，以及2) 它们对治疗中常见的和危急的情况做出不适当的反应。具体而言，发现LLM会鼓励妄想性思维，这可能是由于它们倾向于同意用户（奉承）。这些问题即使在更大、更先进的LLM中仍然存在，表明当前的安全措施存在差距。

除了这些观察到的缺陷之外，作者还指出了LLM在治疗中应用的基本障碍。治疗联盟是成功治疗的关键要素，需要LLM无法提供的人类特征，例如身份和个人投入。

该论文的结论是，基于这些限制，LLM不应取代人类治疗师。然而，作者建议探索LLM在临床治疗中作为辅助角色发挥作用的其他可能性。

---

## 43. #[derive(Clone)] 已损坏

**原文标题**: # [derive(Clone)] Is Broken

**原文链接**: [https://rgbcu.be/blog/derive-broken/](https://rgbcu.be/blog/derive-broken/)

本文认为 Rust 中 `#[derive(Clone)]` 宏存在根本性缺陷，因为它对泛型参数的要求过于严格。具体来说，该派生宏要求*所有*泛型参数都实现 `Clone`，即使它们并非直接以需要克隆的方式在结构体中使用。这导致在某些情况下，即使结构体*可以*安全克隆，也无法派生 `Clone`。第一个例子用 `Arc` 进行了演示，即使底层类型无法克隆，`Arc` 也可以克隆。对于其他派生特征，如 `PartialEq` 和 `Eq`，也存在类似的问题。

作者提出了两种解决方案：一种是长期的解决方案，涉及 Rust RFC 以及对语言本身的潜在更改；另一种是更快速的解决方案，涉及自定义派生宏（如 `CustomClone`），该宏仅在结构体字段的类型明确要求时才生成 `Clone` 实现。快速解决方案将生成带有 `where` 子句的 `impl`，指定每个字段的类型必须实现 `Clone`。

作者已提议在 `derive_more` crate 中实现此自定义派生宏，如果未被接受，将为此目的创建一个新的 crate。根本原因可能是 Rust 类型系统的历史局限性，或者仅仅是 1.0 时代之前的疏忽。由于更改此行为会造成破坏性更改，因此 Rust 编译器团队尚未解决此问题。

---

## 44. Gottesman–Kitaev–Preskill量子比特的集成光子源

**原文标题**: Integrated photonic source of Gottesman–Kitaev–Preskill qubits

**原文链接**: [https://www.nature.com/articles/s41586-025-09044-5](https://www.nature.com/articles/s41586-025-09044-5)

本文介绍了一种用于生成Gottesman-Kitaev-Preskill (GKP) 量子比特的集成光子源的开发，这是一种用于容错量子计算的有前景的编码方案。研究人员使用超低损耗氮化硅光子芯片，并结合高效率光子数分辨探测器来创建这些状态。

该实验涉及通过集成微环谐振器中的自发四波混频 (SFWM) 生成光的压缩态。然后，使用可编程线性光学干涉仪将这些压缩态纠缠。通过检测三个输出模式中的特定光子数模式，在剩余模式中宣告一个 GKP 量子比特态。

生成的 GKP 态表现出容错所需的关键特征，包括位置和动量正交分量中的多个可分辨峰值，以及负 Wigner 函数区域的晶格结构。具体而言，宣告的状态在其 Wigner 函数中显示出 3x3 的网格结构。不同的光子检测模式还会宣告其他非高斯态，如猫态和具有不同晶格结构的 GKP 态。

作者强调，这种集成方法，结合芯片制造和检测技术的进步，代表了迈向可扩展 GKP 量子比特生成的重要一步。他们认为，随着光学损耗的进一步降低，该技术可以产生适用于容错量子计算的状态，从而验证光子量子计算架构的关键要素。最终目标是开发 GKP 源阵列，用于未来的容错量子机器。

---

## 45. 探索时代

**原文标题**: The era of exploration

**原文链接**: [https://yidingjiang.github.io/blog/post/exploration/](https://yidingjiang.github.io/blog/post/exploration/)

本文认为，下一波人工智能进步的关键在于更好的探索，即获取新的且有信息量的经验的过程，而不是仅仅扩大模型参数。作者认为，预训练大型语言模型（LLMs）通过充当一个巨大的“探索税”，使模型能够从更丰富的潜在解决方案分布中进行采样，从而无意中解决了探索问题的一部分。然后，较小的模型可以通过从较大模型中提炼来利用这种预付的探索。

本文强调，有效的探索对于泛化至关重要，它使模型能够在未见过的任务和环境中表现良好。它强调了当前LLM中探索方法的局限性，这些方法主要依赖于从自回归分布中进行采样。

作者提出了一个框架，用于从两个维度理解探索：世界采样（决定将学习者暴露于哪些问题）和路径采样（决定如何在给定问题中收集数据）。监督学习主要侧重于世界采样（数据收集/整理），而强化学习（RL）则允许在这两个方面都具有灵活性。在每次浮点运算中最大化信息需要平衡这两个维度。在世界采样上花费过多可能导致肤浅的学习，而过度关注一小部分世界可能导致过度拟合。理想的情况是在采样新世界和有效地从每个世界提取信息之间取得平衡。文章最后建议未来的研究应该侧重于改进世界和路径采样策略，尤其需要定义世界采样的目标。

---

## 46. 双塔MUD

**原文标题**: The Two Towers MUD

**原文链接**: [https://t2tmud.org/](https://t2tmud.org/)

双塔MUD (T2T) 是一款免费的、基于文本的多人在线角色扮演游戏，背景设定在托尔金的《魔戒》时期中土世界的戒指之战中。自1994年上线以来，它是互联网上运营时间最长的MUD之一，由志愿者工作人员维护。

玩家可以选择为索隆而战或对抗他，探索遍布中土世界及其他地区的超过10万个互动房间，从米斯隆德到魔多。游戏包含大量具有各种奖励的任务，玩家可以组建公会并参与raid。

网站亮点包括：即将于2025年3月15日开始的第27届T2T年度活动、禁止在公共频道发布政治性内容的政策，以及最近发布的“阿扎努比扎项目”，允许进入莫瑞亚深处。此外，还提供30周年纪念商品。

最近的更新侧重于错误修复、音符捆绑包的新功能、箭筒的改进以及莫瑞亚深处任务的调整。玩家现在即使在更高等级也可以完成兹里夫的药剂任务。该网站还包含指向T2T Discord、Facebook群组、托尔金资源、MUD客户端、帮助文件和捐赠选项的链接。

---

## 47. 使用GIS工具分析罗马行程

**原文标题**: Analysing Roman itineraries using GIS tooling

**原文链接**: [https://link.springer.com/article/10.1007/s12520-025-02175-w](https://link.springer.com/article/10.1007/s12520-025-02175-w)

使用GIS工具分析罗马古道：以XIX号道路（从图德到卢科·奥古斯蒂的驿站）为例

---

## 48. Show HN: 钢琴教练 – 使用 MIDI 学习钢琴音阶、和弦等

**原文标题**: Show HN: Piano Trainer – Learn piano scales, chords and more using MIDI

**原文链接**: [https://github.com/ZaneH/piano-trainer](https://github.com/ZaneH/piano-trainer)

钢琴训练器是一款免费的跨平台应用，旨在帮助用户使用 MIDI 输入或主键盘区输入，以自己的节奏学习钢琴技巧。它提供音阶、和弦和五度的互动练习模式，以及具有困难和随机选项的测验模式。该应用程序与 MIDI 兼容，并支持主键盘区输入。

未来功能包括更多音阶、设置自定义（切换测验问题、更改键盘声音）。可在 Itch.io 上下载。

该应用使用 Rust 和 Tauri 构建，代码仓库可在 GitHub 上找到，欢迎贡献。开发者可以使用提供的命令在本地运行应用程序或构建目标二进制文件。欢迎通过向 dev 分支提交 pull request 来进行贡献。该项目感谢其他开源项目和 Tauri Discord 社区提供的帮助。

---

## 49. Bitchat – 一款基于蓝牙mesh网络的去中心化消息应用

**原文标题**: Bitchat – A decentralized messaging app that works over Bluetooth mesh networks

**原文链接**: [https://github.com/jackjackbits/bitchat](https://github.com/jackjackbits/bitchat)

Bitchat是一款去中心化的点对点消息应用，旨在通过蓝牙mesh网络运行，无需互联网连接、服务器或电话号码。它通过端到端加密（X25519 & AES-256-GCM）和数字签名（Ed25519）、前向保密以及无注册、阅后即焚消息、掩护流量和紧急擦除功能等隐私特性，优先保障安全和私密的通信。

该应用具有基于频道的聊天功能，可选择密码保护，消息保留由频道所有者控制，并提供类似IRC的命令界面，用于加入频道、发送私信、列出用户和管理被屏蔽的对等节点。Bitchat采用存储转发机制进行离线消息传递。

性能通过LZ4消息压缩、自适应电池模式（性能、平衡、省电、超低功耗）以及使用优化的Bloom过滤器和消息聚合的高效网络管理进行优化。

技术架构依赖于针对蓝牙LE优化的紧凑型二进制协议，并利用基于TTL的消息路由和消息去重。提供了使用XcodeGen、Swift Package Manager或手动Xcode项目配置的设置说明。该协议与平台无关，为未来的Android客户端铺平了道路。

---

## 50. 苹果刚刚发布了一个有点意思的编程语言模型。

**原文标题**: Apple just released a weirdly interesting coding language model

**原文链接**: [https://9to5mac.com/2025/07/04/apple-just-released-a-weirdly-interesting-coding-language-model/](https://9to5mac.com/2025/07/04/apple-just-released-a-weirdly-interesting-coding-language-model/)

本文探讨了苹果公司最近发布的DiffuCode-7B-cpGRPO，这是一种利用基于扩散方法进行代码生成的新型编程语言模型。与传统的按顺序生成文本（和代码）的自回归模型不同，DiffuCode可以无序地编写和改进代码，从而可能加快代码生成速度。

DiffuCode建立在DiffuCoder论文的基础上，该论文探讨了使用扩散模型进行代码生成。通过调整“温度”设置，可以使模型或多或少地像传统的自回归模型一样运行。较高的温度允许更多无序的令牌生成，而较低的温度则强制执行更顺序的方法。此外，一个名为耦合-GRPO的额外训练步骤可以提高代码质量并减少所需的迭代次数。

该模型建立在阿里巴巴的开源基础模型Qwen2.5-7B之上。苹果公司使用基于扩散的解码器和指令遵循调整对该模型进行了微调，然后在一组精心策划的编码示例上进行了训练。由此产生的DiffuCode-7B-cpGRPO在编码基准测试中取得了4.4%的改进。

虽然DiffuCode尚未达到GPT-4或Gemini Diffusion等顶级模型的性能，但它代表了苹果公司在生成式人工智能方面迈出的有希望的一步，并为代码生成引入了一种新颖的方法。文章总结说，该模型证明了苹果公司对创新人工智能解决方案的持续探索。

---

## 51. Anthropic 肢解数百万本旧书，并下载了 700 万本盗版书——法官

**原文标题**: Anthropic cut up millions of used books, and downloaded 7M pirated ones – judge

**原文链接**: [https://www.businessinsider.com/anthropic-cut-pirated-millions-used-books-train-claude-copyright-2025-6](https://www.businessinsider.com/anthropic-cut-pirated-millions-used-books-train-claude-copyright-2025-6)

标题暗示Anthropic涉嫌使用争议手段获取AI模型训练数据，称其“肢解数百万旧书”并“下载七百万盗版书”，暗示该信息源于司法裁决，或涉及版权侵权和数据来源的法律问题，引发对该公司行为伦理和合法性的质疑。

---

## 52. 论题：有趣的工作较少适合人工智能的应用

**原文标题**: Thesis: Interesting work is less amenable to the use of AI

**原文链接**: [https://remark.ing/rob/rob/Thesis-interesting-work-ie](https://remark.ing/rob/rob/Thesis-interesting-work-ie)

作者罗布·科赫认为，相比于那些不那么吸引人的任务，能够被称为“有趣的工作”（值得做的工作）反而不太适合人工智能辅助。当他看到别人吹嘘人工智能带来的生产力提升时，他感到一种错失恐惧症（FOMO），担心如果他依赖大型语言模型，会失去对上下文的理解，并且违背了“专注做好一件事”的原则。他将自己的工作与“样板代码”任务区分开来，质疑为何有人会花费大量时间编写样板代码，并认为这无论是否使用人工智能都是一种效率上的失败。他进一步质疑了那些主要专注于生成样板代码的人的职业保障。他反思自己是否误解了软件工程的本质，认为软件工程是关于解决问题，而不是简单地将样板代码与功能需求匹配，他将后者比作装配线上最后一个工人。 简而言之，他认为人工智能的优势在于自动化重复、乏味的任务，而软件工程的核心、创造性方面仍然更适合由人类来处理。

---

## 53. 是否有可能仅用李萨如图形在示波器上玩毁灭战士？

**原文标题**: Is it possible to play doom on an oscilloscope using only lissajous figures?

**原文链接**: [https://forums.sufficientvelocity.com/threads/is-it-possible-to-play-doom-on-an-analog-oscilloscope-using-only-lissajous-figures.126232/](https://forums.sufficientvelocity.com/threads/is-it-possible-to-play-doom-on-an-analog-oscilloscope-using-only-lissajous-figures.126232/)

来自华盛顿特区的Cherenkov对仅使用李萨如曲线在模拟示波器上运行《毁灭战士》(1993)感到好奇。虽然之前已经有人成功地在示波器上显示过《毁灭战士》，但现有方法本质上是将示波器的CRT作为连接到外部计算机的显示器使用。

Cherenkov指出，熟练的艺术家可以通过操纵信号来生成李萨如曲线，从而在示波器上创作出令人印象深刻的视觉效果。这引出了一个问题：是否可以通过将《毁灭战士》的图形完全转换为李萨如曲线，在示波器上玩这款游戏？

作者假设这在理论上是可行的，尽管计算量很大。这将需要一台强大的外部计算机来对《毁灭战士》的图形进行实时数学变换，将其转换为适当的信号，以便在示波器上生成李萨如曲线。然后，这些信号将通过数模转换器(DAC)发送到示波器。本质上，挑战在于仅通过动态变化的李萨如曲线来呈现《毁灭战士》的游戏过程。

---

## 54. 你想建立一家养老公司吗

**原文标题**: So you wanna build an aging company

**原文链接**: [https://www.librariesforthefuture.bio/p/is-this-aging](https://www.librariesforthefuture.bio/p/is-this-aging)

你想打造一家抗衰老公司？

本文《你想打造一家抗衰老公司？》探讨了在生物技术行业中定义和解决衰老问题的细微之处。作者强调，衰老是生物过程复杂相互作用的结果，而非单一事件，正确定义“衰老”对于开发有效的干预措施至关重要。

成功的抗衰老疗法应能预防与年龄相关的疾病，保持随年龄增长而衰退的健康功能，或至少逆转一种与年龄相关疾病的进程。 这意味着健康个体服用治疗方法以预防未来问题，这对安全性和终点验证提出了挑战。相反，逆转与年龄相关的疾病通常需要再生受损组织，这是一个重大障碍。

文章告诫不要将所有健康相关研究等同于衰老研究。 它认为，肿瘤学、早衰症治疗以及仅针对衰老生物标志物的研究不太可能产生广泛的抗衰老疗法。 癌症药物对健康个体来说通常过于严酷，早衰症是单基因疾病（不像复杂的衰老），而仅关注生物标志物可能针对的是相关性而非原因，甚至可能阻碍保护机制。

衰老研究的有希望的领域包括解决虚弱/肌肉减少症、免疫功能障碍（“炎症衰老”）、心脏代谢疾病、纤维化疾病和神经退行性疾病的前驱症状。 直接测量寿命和死亡率也很有价值，但具有挑战性。

最后，文章强调了现实衰老模型的重要性，强调需要研究衰老生物、模型生物的自发性疾病以及来自老年患者的人体组织样本。 有希望的治疗方法包括“延迟”（推迟衰退）、“替换”（更换组织）、“恢复”（逆转细胞衰老）和“暂停”（诱导生物静止）。

---

## 55. Applite – Homebrew 的 macOS 原生 GUI

**原文标题**: Applite – A macOS native GUI for homebrew

**原文链接**: [https://aerolite.dev/applite](https://aerolite.dev/applite)

Applite是一款免费开源的macOS应用程序，它提供了一个用户友好的图形界面来管理Homebrew软件包。它简化了安装、更新和卸载应用程序的过程，只需单击一下即可完成，方便了非技术用户使用。Applite利用Homebrew软件包管理器，让用户能够访问Homebrew目录中提供的任何应用程序，并在应用程序内进行搜索。

安全性方面，Applite通过macOS内置的Gatekeeper和XProtect进行保障，在首次启动时扫描恶意软件。虽然大多数Homebrew应用程序都经过公证，但由于未沙盒化的应用程序可能影响系统以及存在恶意软件的可能性，特别是对于不太流行的应用程序，建议用户谨慎使用。Applite本身也未沙盒化。该应用程序向用户保证，它不会追踪任何信息。

Applite可以与现有的Homebrew安装一起使用，也可以创建一个新的、独立的安装。如果使用现有的安装，通过Homebrew安装的cask将在Applite中被识别。手动安装的应用程序不会被自动识别，但可以通过Applite重新安装来添加。

本文鼓励用户浏览FAQ，提供了应用程序的屏幕截图，并通过DMG或Homebrew Cask提供了下载选项。可以通过GitHub、电子邮件、Discord或Twitter联系开发者。欢迎捐款以支持该项目。

---

## 56. Show HN: 从照片到位置：基于VLM的室内地图原型

**原文标题**: Show HN: From Photos to Positions: Prototyping VLM-Based Indoor Maps

**原文链接**: [https://arjo129.github.io/blog/5-7-2025-From-Photos-To-Positions-Prototyping.html](https://arjo129.github.io/blog/5-7-2025-From-Photos-To-Positions-Prototyping.html)

此“Show HN”帖子详细介绍了一个使用视觉语言模型（VLMs）进行室内定位系统原型设计的个人项目。受Andrej Karpathy的“软件3.0”愿景以及过去室内定位系统经验的启发，作者探索使用VLMs基于一张照片来确定用户在购物中心内的位置。

其核心思想是利用VLMs理解和解释视觉数据的能力，特别是购物中心内的楼层平面图。作者创建了一个简单的标注工具来标记数字地图上的商店，然后处理这些数据以确定从购物中心走廊的不同位置可以看到哪些商店。该项目随后使用 Gemini API 来检测用户拍摄的照片中的商店名称。检测到的商店名称与预处理的地图数据进行匹配，以估计用户可能的地点。

作者通过一张照片证明了这种方法的可行性，并在识别潜在位置方面取得了令人惊讶的准确结果。在承认诸如依赖清晰的商店标志和基于文本的提示等局限性时，作者强调了 VLMs 在定位任务中的潜力。未来的改进可能包括集成视频输入、手机传感器数据或训练专用模型。作者强调该项目是一个概念验证，但相信它在 AR 应用和机器人技术方面具有前景，并分享了代码库供其他人探索。

---

## 57. 人工智能比你想象的更强大

**原文标题**: AI Is Bigger Than You Think

**原文链接**: [https://hjortur.substack.com/p/ai-is-bigger-than-you-think](https://hjortur.substack.com/p/ai-is-bigger-than-you-think)

无法访问文章链接。

---

## 58. AI摄像头改变十字路口司机行为

**原文标题**: AI cameras change driver behavior at intersections

**原文链接**: [https://spectrum.ieee.org/ai-intersection-monitoring](https://spectrum.ieee.org/ai-intersection-monitoring)

人工智能摄像头如何改变路口驾驶行为

---

## 59. 玻璃人：薄伽丘传

**原文标题**: Man of Glass: Boccaccio: A Biography

**原文链接**: [https://literaryreview.co.uk/man-of-glass](https://literaryreview.co.uk/man-of-glass)

文章《玻璃之人：薄伽丘传记》，副标题“陨落？”，可能探讨了十四世纪意大利作家兼诗人乔万尼·薄伽丘的生活和事业，他最著名的作品是《十日谈》。“陨落？”这一副标题暗示了对薄伽丘一生或事业中潜在的衰落或困境的关注。

该传记可能涵盖了他的早年生活和影响，可能详细描述了他的私生子身份和早期教育。它肯定会深入探讨他最著名的作品《十日谈》，考察其背景（黑死病）、主题（爱情、命运和智慧）以及对文学的持久影响。

“陨落？”的角度暗示该文章也可能探讨一个衰落或困难时期。这可能与以下方面有关：

*   **批评和后悔：** 薄伽丘后来对一些早期的作品表示后悔，特别是那些被认为过于感性的作品。文章可能会探讨这种自我批评。
*   **财务或社会困境：** 也许薄伽丘晚年面临财务问题或社会排斥。
*   **疾病和死亡：** 传记可能描述他日益衰弱的健康状况和最终的死亡。
*   **文学品味的转变：** 文章可能会考察薄伽丘后来的作品与《十日谈》的受欢迎程度相比是如何被接受的，从而呈现出一种被认为的失宠。

本质上，这篇文章承诺对薄伽丘的生活进行全面的审视，特别关注一个可能的困境、职业衰落或个人危机时期，这可能导致他从先前建立的地位上“陨落”。

---

## 60. CPU-X：Linux 版 CPU-Z

**原文标题**: CPU-X: CPU-Z for Linux

**原文链接**: [https://thetumultuousunicornofdarkness.github.io/CPU-X/](https://thetumultuousunicornofdarkness.github.io/CPU-X/)

CPU-X 是一个自由开源的系统分析和监控应用程序，适用于 GNU/Linux 和 FreeBSD，类似于 Windows 上的 CPU-Z。它提供关于计算机硬件组件的详细信息，包括处理器、主板、内存、系统和显卡。它还提供基本的性能指标。CPU-X 既有图形用户界面 (GTK) 也有基于文本的界面 (NCurses)，并支持命令行转储模式。最新版本可以从提供的链接下载，更多信息，包括安装说明和屏幕截图，可以在 README 文件和 wiki 页面上找到。

---

## 61. Backlog.md – 适用于任何 Git 仓库的 Markdown 原生任务管理器和看板可视化工具

**原文标题**: Backlog.md – Markdown‑native Task Manager and Kanban visualizer for any Git repo

**原文链接**: [https://github.com/MrLesk/Backlog.md](https://github.com/MrLesk/Backlog.md)

Backlog.md：基于Markdown的任务管理器及Git仓库看板可视化工具。它允许用户在仓库中以纯Markdown文件管理任务，提供私有和离线的项目看板体验。主要功能包括终端看板视图、现代Web界面、支持AI的CLI命令和跨平台兼容性。

用户可以通过npm或bun安装Backlog.md，并在Git仓库中初始化backlog。可以通过CLI创建具有各种属性的任务，例如描述、负责人、状态、标签、优先级、计划、验收标准 (AC)、注释和依赖关系。该工具还支持草稿任务及其升级/降级。

Web界面提供了一个交互式的看板，具有拖放功能、任务创建/编辑、实时更新和响应式设计。 CLI提供命令来列出、查看、编辑、存档和管理任务。

可以通过CLI标志和配置文件（每个项目和每个用户）自定义配置，允许用户设置负责人、状态、日期格式、编辑器、Web UI端口、浏览器自动打开、远程操作和自动提交行为的默认值。 Backlog.md采用MIT许可证，允许免费使用并署名。重要的是，除非启用自动提交，否则用户可以控制git提交。

---

## 62. Show HN：Ossia score – 视听艺术家的音序器

**原文标题**: Show HN: Ossia score – A sequencer for audio-visual artists

**原文链接**: [https://github.com/ossia/score](https://github.com/ossia/score)

Ossia score 是一款免费开源的音序器，专为视听艺术家创作互动表演而设计。它允许跨多个软件和硬件对各种协议（如 OSC、MIDI、DMX、声音和视频）进行排序。用户可以使用 JavaScript、Faust、PureData 和 C++ 等语言创建互动乐谱和实时编码。

该软件支持广泛的输入和输出方法，包括物联网协议、操纵杆、Web API 和创意编程语言。它处理各种音频和视频格式，并通过 Spout、Syphon 和其他工具提供视觉处理。它还允许使用 CSV 和 HDF5 支持对大型数据集进行声音化处理。

Ossia score 适用于桌面、移动、Web 和嵌入式平台，包括 Raspberry Pi Zero 2。该软件可以下载用于 Windows、macOS 和 Linux (AppImage)。本文还概述了各种平台的构建状态，并详细介绍了如何为该项目做出贡献，包括更新子模块和识别代码中需要改进的领域。本文还提供了项目网站、论坛、Discord 和 Matrix 房间的链接。提供了关于如何贡献代码或以财政方式支持项目的信息。

---

## 63. 我提取了苹果智能模型的安全过滤器。

**原文标题**: I extracted the safety filters from Apple Intelligence models

**原文链接**: [https://github.com/BlueFalconHD/apple_generative_model_safety_decrypted](https://github.com/BlueFalconHD/apple_generative_model_safety_decrypted)

本文档详细介绍了从苹果智能生成模型中提取和解密安全过滤器的过程。作者已成功解密包含这些过滤器的文件，并提供了重现该过程所需的工具和说明。

该存储库包含：

*   **已解密的覆盖文件：** 包含 JSON 文件，其中包含针对各种模型的特定安全规则。这些规则规定了模型如何处理敏感内容，包括基于精确短语和正则表达式的内容拒绝、移除和替换。
*   **合并脚本：** 用于合并和去重已解密元数据的脚本，创建整合文件以便于审查（全局、区域和特定于区域设置）。
*   **解密脚本：** 使用通过 LLDB 提取的密钥解密覆盖文件的 Python 脚本。

该过程包括：

1.  **获取加密密钥：** 将 Xcode 的 LLDB 连接到 `GenerativeExperiencesSafetyInferenceProvider` 并使用提供的 Python 脚本提取密钥。
2.  **解密覆盖文件：** 运行 Python 脚本，使用获得的密钥解密加密文件。
3.  **合并元数据：** 使用另一个 Python 脚本，基于区域和区域设置合并和去重 JSON 元数据文件，从而更易于分析安全过滤器。

解密后的安全过滤器揭示了苹果对其生成模型的内容审核策略的细节，特别是识别出被阻止、移除或替换的短语和模式。“reject”字段定义了触发立即安全违规的短语，而“remove”和“replace”字段允许修改内容。正则表达式也用于更广泛的模式匹配。

---

## 64. Show HN：反学习比较器，一款用于比较机器反学习的可视化工具

**原文标题**: Show HN: Unlearning Comparator, a visual tool to compare machine unlearning

**原文链接**: [https://gnueaj.github.io/Machine-Unlearning-Comparator/](https://gnueaj.github.io/Machine-Unlearning-Comparator/)

展示HN：反学习比较器

该帖子介绍了一个可视化工具——机器学习反学习比较器，旨在比较不同的机器学习反学习技术。该工具可能允许用户输入数据，训练模型，然后应用各种反学习算法来从模型的记忆中移除特定的数据点或概念。“比较器”这部分暗示该工具提供了一种可视化评估每种反学习方法有效性的方式。关键比较可能包括：

*   **残留性能：** 在反学习之后，模型在剩余数据上的表现如何？
*   **效率：** 每种反学习技术需要多长时间执行？
*   **完整性：** 模型实际忘记目标数据的程度如何？

该工具可能提供可视化辅助工具，例如图形或图表，以说明这些比较，并使其更容易理解不同反学习方法之间的权衡。通过提供切实的交互式体验，反学习比较器旨在揭开机器学习反学习的神秘面纱，并在数据隐私和合规性至关重要的场景中促进其采用。它是研究人员、开发人员以及任何有兴趣理解和实施机器学习反学习技术的人的实用资源。

---

## 65. SUS Lang：SUS硬件描述语言

**原文标题**: SUS Lang: The SUS Hardware Description Language

**原文链接**: [https://sus-lang.org/](https://sus-lang.org/)

SUS Lang：一种新的硬件描述语言（HDL），旨在直接与可综合的 Verilog 和 VHDL 竞争。其主要目标是为构建网表提供直观简洁的语法，同时保留利用传统综合工具的能力。

SUS 通过以下几个关键特性脱颖而出：用于简化时序和流水线管理的延迟计数，支持编译时代码执行（如 LUT 生成）的强大元编程能力，以及专注于使设计者完全控制同步逻辑的设计。它强制同步性，使其不适用于异步 ASIC 开发。

SUS 提供用于灵活代码生成的生成变量和类型，通过延迟计数简化流水线，并使用接口促进域分离。它承诺直接的代码到网表映射、显式跨越原语、内置流水线语法、IDE 内的错误报告以及用于硬件生成的元编程。

计划的未来特性包括具有有界整数的类型安全、多时钟模块、形式验证集成、常用结构的语法糖和源文件时序约束。

SUS 特意避免为握手协议（如 AXI）、运行时迭代结构以及自动流水线或重定时提供抽象，旨在管理硬件设计的固有复杂性而不掩盖它。它鼓励通过 40 分钟的介绍视频进行学习，并通过 GitHub 或 Discord 进行互动。

---

## 66. 运动伪装

**原文标题**: Motion Camouflage

**原文链接**: [https://en.wikipedia.org/wiki/Motion_camouflage](https://en.wikipedia.org/wiki/Motion_camouflage)

运动伪装是一种移动物体用来避免被发现的隐蔽策略。与侧重于将颜色与背景相匹配的静态伪装不同，运动伪装解决的是运动的问题，运动本身会使物体更加显眼。

运动伪装的主要形式是模仿目标所见背景的光流。攻击者通过机动，使其相对于目标视野中的一个地标点显得静止不动，这意味着目标只会感觉到攻击者越来越大（逼近），而不是横向移动。这与经典的追逐不同，在经典的追逐中，攻击者直接向目标移动，产生明显的横向运动。

其他策略包括通过缓慢而隐蔽地移动来最大限度地减少运动线索，或扰乱目标对运动的感知。舰船上的眩晕伪装旨在扰乱对运动的感知，而乌贼在捕猎时会使用“经过条纹”展示来减少明显的逼近效应。

运动伪装已经在食蚜蝇、蜻蜓、猎鹰和回声定位蝙蝠中观察到。蜻蜓同时使用“实点”和“无穷远点”策略，而猎鹰和蝙蝠则使用“无穷远点”追逐路径。这种策略，被称为恒定绝对目标方向（CATD）或平行导航，也因其效率而被建议用于防空导弹。

最后，一些动物，如叶海龙和竹节虫，会利用摇摆运动来模仿风中的植物，模糊了隐蔽和伪装以及运动伪装之间的界限。

---

## 67. A non-anthropomorphized view of LLMs

**原文标题**: A non-anthropomorphized view of LLMs

**原文链接**: [http://addxorrol.blogspot.com/2025/07/a-non-anthropomorphized-view-of-llms.html](http://addxorrol.blogspot.com/2025/07/a-non-anthropomorphized-view-of-llms.html)

This article argues against anthropomorphizing Large Language Models (LLMs), viewing them instead as complex mathematical functions that generate sequences of words based on probabilities learned from mimicking human text. The author, "halvar.flake," sees LLMs as mappings of the form \((\mathbb{R}^n)^c \mapsto (\mathbb{R}^n)^c\), akin to strange attractors in dynamical systems, not as entities with consciousness, ethics, or goals.

The author emphasizes that "alignment" or "AI safety" for LLMs boils down to quantifying and bounding the probability of generating undesirable sequences, a task made difficult by the lack of precise mathematical definitions for "undesirable."

The article acknowledges the significant utility of LLMs in solving previously intractable problems, such as natural language processing, and anticipates continued improvements. However, it critiques the tendency to ascribe human-like qualities to these models, which the author argues muddles the discussion and public perception, making the technology seem mysterious and scary. The author suggests a clearer approach is to focus on understanding and controlling the sequence generation process.

The author speculates that the anthropomorphization may stem from a belief among some AI researchers that they are on the path to achieving Artificial General Intelligence (AGI). The author then contrasts human consciousness with LLMs, highlighting the vast differences in complexity and origin.

Ultimately, the article underscores the importance of clear, non-anthropocentric thinking about LLMs to navigate the significant societal changes they will bring, and to avoid harmful outcomes.


---

## 68. Uncommon Uses of Python in Commonly Used Libraries (2022)

**原文标题**: Uncommon Uses of Python in Commonly Used Libraries (2022)

**原文链接**: [https://eugeneyan.com/writing/uncommon-python/](https://eugeneyan.com/writing/uncommon-python/)

生成摘要时出错

---

## 69. Show HN: I wrote a "web OS" based on the Apple Lisa's UI, with 1-bit graphics

**原文标题**: Show HN: I wrote a "web OS" based on the Apple Lisa's UI, with 1-bit graphics

**原文链接**: [https://alpha.lisagui.com/](https://alpha.lisagui.com/)

生成摘要时出错

---

## 70. WebAssembly: Yes, but for What?

**原文标题**: WebAssembly: Yes, but for What?

**原文链接**: [https://queue.acm.org/detail.cfm?id=3746171](https://queue.acm.org/detail.cfm?id=3746171)

生成摘要时出错

---

## 71. High Performance Image Sensor Processing Using FPGAs [pdf]

**原文标题**: High Performance Image Sensor Processing Using FPGAs [pdf]

**原文链接**: [https://oda.uni-obuda.hu/bitstream/handle/20.500.14044/10350/Gabor_S_Becker_ertekezes.pdf](https://oda.uni-obuda.hu/bitstream/handle/20.500.14044/10350/Gabor_S_Becker_ertekezes.pdf)

生成摘要时出错

---

## 72. The Cat's Meat Man: Feeding Felines in Victorian London

**原文标题**: The Cat's Meat Man: Feeding Felines in Victorian London

**原文链接**: [https://publicdomainreview.org/essay/the-cats-meat-man/](https://publicdomainreview.org/essay/the-cats-meat-man/)

生成摘要时出错

---

## 73. The first time I was almost fired from Apple

**原文标题**: The first time I was almost fired from Apple

**原文链接**: [https://www.engineersneedart.com/blog/almostfired/almostfired.html](https://www.engineersneedart.com/blog/almostfired/almostfired.html)

生成摘要时出错

---

## 74. Charles Babbage and deciphering codes (1864)

**原文标题**: Charles Babbage and deciphering codes (1864)

**原文链接**: [https://mathshistory.st-andrews.ac.uk/Extras/Babbage_deciphering/](https://mathshistory.st-andrews.ac.uk/Extras/Babbage_deciphering/)

生成摘要时出错

---

## 75. Cpparinfer: A C++23 implementation of the parinfer algorithm

**原文标题**: Cpparinfer: A C++23 implementation of the parinfer algorithm

**原文链接**: [https://gitlab.com/w0utert/cpparinfer](https://gitlab.com/w0utert/cpparinfer)

生成摘要时出错

---

## 76. U.S. measles cases reach 33-year high as outbreaks spread

**原文标题**: U.S. measles cases reach 33-year high as outbreaks spread

**原文链接**: [https://www.washingtonpost.com/health/2025/07/07/measles-cases-hit-record/](https://www.washingtonpost.com/health/2025/07/07/measles-cases-hit-record/)

Unable to access the article link.


---

## 77. Stop forcing AI tools on your engineers

**原文标题**: Stop forcing AI tools on your engineers

**原文链接**: [https://newsletter.manager.dev/p/stop-forcing-ai-tools-on-your-engineers](https://newsletter.manager.dev/p/stop-forcing-ai-tools-on-your-engineers)

Anton Zaides argues against forcing AI tools on engineers, warning that it can lead to disaster. He uses inversion to highlight destructive strategies: mandating specific tools like Cursor, implementing AI-adoption ratings tied to promotions (measured by tokens used), and ridiculing engineers who code traditionally. He contends that these approaches focus on tool adoption over outcomes, potentially slowing progress and creating a mess.

Zaides suggests that the goal should be to better serve customers and grow the business, not just to appear AI-forward to investors. He advises EMs to instead:

*   **Give Time to Explore:** Acknowledge the learning curve and allow engineers time to experiment with AI tools during actual work, reducing workloads to facilitate this exploration.
*   **Share What Worked in YOUR Org:** Share internal success stories and use cases instead of relying on external examples.
*   **Trust Engineers' Judgement:** When tools are effective, engineers will naturally adopt them.

He highlights Monday.com's approach of weekly lectures, hands-on training, and demo sessions showing real-world applications and failures. Zaides acknowledges the pressure to level up and the potential of AI, especially in fresh codebases or PoCs, but emphasizes that AI adoption should be organic and results-driven. He ultimately emphasizes that managers should prioritize results, quality, and speed, and then let the tools emerge naturally.


---

## 78. Why are there still 7 continents?

**原文标题**: Why are there still 7 continents?

**原文链接**: [https://jonpauluritis.com/articles/why-are-there-still-7-continents/](https://jonpauluritis.com/articles/why-are-there-still-7-continents/)

生成摘要时出错

---

## 79. The War on the Walkman

**原文标题**: The War on the Walkman

**原文链接**: [https://newsletter.pessimistsarchive.org/p/the-forgotten-war-on-the-walkman](https://newsletter.pessimistsarchive.org/p/the-forgotten-war-on-the-walkman)

生成摘要时出错

---

## 80. Claude Code Pro Limit? Hack It While You Sleep

**原文标题**: Claude Code Pro Limit? Hack It While You Sleep

**原文链接**: [https://github.com/terryso/claude-auto-resume](https://github.com/terryso/claude-auto-resume)

生成摘要时出错

---

## 81. Swedish Campground (2004)

**原文标题**: Swedish Campground (2004)

**原文链接**: [https://www.folklore.org/Swedish_Campground.html](https://www.folklore.org/Swedish_Campground.html)

生成摘要时出错

---

## 82. Why English doesn't use accents

**原文标题**: Why English doesn't use accents

**原文链接**: [https://www.deadlanguagesociety.com/p/why-english-doesnt-use-accents](https://www.deadlanguagesociety.com/p/why-english-doesnt-use-accents)

生成摘要时出错

---

## 83. Show HN: Trying to eat better? I built a nutrional assistant

**原文标题**: Show HN: Trying to eat better? I built a nutrional assistant

**原文链接**: [https://chat.eko-bazaar.com/](https://chat.eko-bazaar.com/)

生成摘要时出错

---

## 84. Researchers Found a Better Way to Teach Large Language Models New Skills

**原文标题**: Researchers Found a Better Way to Teach Large Language Models New Skills

**原文链接**: [https://news.ncsu.edu/2025/07/iimproving-llm-new-skills/](https://news.ncsu.edu/2025/07/iimproving-llm-new-skills/)

生成摘要时出错

---

## 85. Jane Street barred from Indian markets as regulator freezes $566M

**原文标题**: Jane Street barred from Indian markets as regulator freezes $566M

**原文链接**: [https://www.cnbc.com/2025/07/04/indian-regulator-bars-us-trading-firm-jane-street-from-accessing-securities-market.html](https://www.cnbc.com/2025/07/04/indian-regulator-bars-us-trading-firm-jane-street-from-accessing-securities-market.html)

生成摘要时出错

---

## 86. TSA to end shoes-off policy for airport security screening

**原文标题**: TSA to end shoes-off policy for airport security screening

**原文链接**: [https://abcnews.go.com/US/tsa-end-shoes-off-policy-airport-security-screening/story?id=123556295](https://abcnews.go.com/US/tsa-end-shoes-off-policy-airport-security-screening/story?id=123556295)

生成摘要时出错

---

## 87. Neanderthals operated prehistoric “fat factory” on German lakeshore

**原文标题**: Neanderthals operated prehistoric “fat factory” on German lakeshore

**原文链接**: [https://archaeologymag.com/2025/07/neanderthals-operated-fat-factory-125000-years-ago/](https://archaeologymag.com/2025/07/neanderthals-operated-fat-factory-125000-years-ago/)

生成摘要时出错

---

## 88. What every programmer should know about how CPUs work [video]

**原文标题**: What every programmer should know about how CPUs work [video]

**原文链接**: [https://www.youtube.com/watch?v=-HNpim5x-IE](https://www.youtube.com/watch?v=-HNpim5x-IE)

生成摘要时出错

---

## 89. Artist in Residence on a Satellite

**原文标题**: Artist in Residence on a Satellite

**原文链接**: [http://global.cafa.edu.cn/infoDetail/1/324](http://global.cafa.edu.cn/infoDetail/1/324)

生成摘要时出错

---

## 90. Show HN: Modernized file manager and program manager from Windows 3.x

**原文标题**: Show HN: Modernized file manager and program manager from Windows 3.x

**原文链接**: [https://github.com/brianluft/heirloom](https://github.com/brianluft/heirloom)

生成摘要时出错

---

## 91. The era of full stack chip designers

**原文标题**: The era of full stack chip designers

**原文链接**: [https://chipinsights.substack.com/p/the-era-of-full-stack-chip-designers](https://chipinsights.substack.com/p/the-era-of-full-stack-chip-designers)

生成摘要时出错

---

## 92. Lessons from creating my first text adventure

**原文标题**: Lessons from creating my first text adventure

**原文链接**: [https://entropicthoughts.com/lessons-from-creating-first-text-adventure](https://entropicthoughts.com/lessons-from-creating-first-text-adventure)

生成摘要时出错

---

## 93. Intel's Lion Cove P-Core and Gaming Workloads

**原文标题**: Intel's Lion Cove P-Core and Gaming Workloads

**原文链接**: [https://chipsandcheese.com/p/intels-lion-cove-p-core-and-gaming](https://chipsandcheese.com/p/intels-lion-cove-p-core-and-gaming)

生成摘要时出错

---

## 94. Local-first software (2019)

**原文标题**: Local-first software (2019)

**原文链接**: [https://www.inkandswitch.com/essay/local-first/](https://www.inkandswitch.com/essay/local-first/)

生成摘要时出错

---

## 95. Building the Rust Compiler with GCC

**原文标题**: Building the Rust Compiler with GCC

**原文链接**: [https://fractalfir.github.io/generated_html/cg_gcc_bootstrap.html](https://fractalfir.github.io/generated_html/cg_gcc_bootstrap.html)

生成摘要时出错

---

## 96. Async Queue – One of my favorite programming interview questions

**原文标题**: Async Queue – One of my favorite programming interview questions

**原文链接**: [https://davidgomes.com/async-queue-interview-ai/](https://davidgomes.com/async-queue-interview-ai/)

生成摘要时出错

---

## 97. LLMs exploit our tolerance for sloppiness

**原文标题**: LLMs exploit our tolerance for sloppiness

**原文链接**: [https://www.humprog.org/~stephen/blog/highered/top-of-the-slops.html](https://www.humprog.org/~stephen/blog/highered/top-of-the-slops.html)

生成摘要时出错

---

## 98. The messy reality of SIMD (vector) functions

**原文标题**: The messy reality of SIMD (vector) functions

**原文链接**: [https://johnnysswlab.com/the-messy-reality-of-simd-vector-functions/](https://johnnysswlab.com/the-messy-reality-of-simd-vector-functions/)

生成摘要时出错

---

## 99. Can we test it? Yes, was can [video]

**原文标题**: Can we test it? Yes, was can [video]

**原文链接**: [https://www.youtube.com/watch?v=MqC3tudPH6w](https://www.youtube.com/watch?v=MqC3tudPH6w)

生成摘要时出错

---

## 100. Get the location of the ISS using DNS

**原文标题**: Get the location of the ISS using DNS

**原文链接**: [https://shkspr.mobi/blog/2025/07/get-the-location-of-the-iss-using-dns/](https://shkspr.mobi/blog/2025/07/get-the-location-of-the-iss-using-dns/)

生成摘要时出错

---

