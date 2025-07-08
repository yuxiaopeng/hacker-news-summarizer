# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-07-08.md)

*最后自动更新时间: 2025-07-08 17:50:13*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 2 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 3 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 4 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 5 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 6 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 7 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 8 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 9 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 10 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 11 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 12 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 13 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 14 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 15 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 16 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 17 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 18 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 19 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 20 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 21 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 22 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 23 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 24 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 25 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 26 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 27 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 28 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 29 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 30 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 31 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 32 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 33 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 34 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 35 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 36 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 37 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 38 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 39 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 40 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 41 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 42 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 43 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 44 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 45 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 46 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 47 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 48 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 49 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 50 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 51 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 52 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 53 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 54 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 55 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 56 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 57 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 58 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 59 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 60 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 61 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 62 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 63 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 64 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 65 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 66 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 67 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 68 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 69 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 70 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 71 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 72 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 73 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 74 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 75 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 76 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 77 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 78 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 79 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 80 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 81 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 82 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 83 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 84 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 85 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 86 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 87 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 88 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 89 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 90 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 91 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 92 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 93 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 94 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 95 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 96 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 97 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 98 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 99 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 100 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 101 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 102 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 103 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 104 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 105 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 106 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 107 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 108 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 109 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 110 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 111 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
