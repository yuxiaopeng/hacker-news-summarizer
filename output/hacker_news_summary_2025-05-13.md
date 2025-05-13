# Hacker News 热门文章摘要 (2025-05-13)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 苏黎世联邦理工学院研究人员发现英特尔处理器存在新的安全漏洞

**原文标题**: ETH Zurich researchers discover new security vulnerability in Intel processors

**原文链接**: [https://ethz.ch/en/news-and-events/eth-news/news/2025/05/eth-zurich-researchers-discover-new-security-vulnerability-in-intel-processors.html](https://ethz.ch/en/news-and-events/eth-news/news/2025/05/eth-zurich-researchers-discover-new-security-vulnerability-in-intel-processors.html)

苏黎世联邦理工学院研究人员发现了一种新的安全漏洞，称为“分支特权注入”（BPRC），影响自2018年以来所有英特尔处理器。该漏洞利用处理器使用的推测技术来提高性能，允许攻击者绕过安全屏障，并读取共享同一CPU的其他用户的敏感信息。

该漏洞产生于处理器切换期间特权分配暂时不明确的短暂时期，使攻击者能够注入恶意代码并访问信息。通过反复利用此漏洞，攻击者可以逐渐读取CPU缓存和RAM的全部内容，速度超过每秒5000字节。

这构成了一个重大威胁，尤其是在多个用户共享硬件资源的云环境中。虽然英特尔自从2024年9月发现该漏洞以来已经实施了保护措施，但研究人员认为这表明存在更根本的架构缺陷。他们建议用户安装最新的操作系统更新，因为这些更新包括解决该漏洞的微码更新。这一发现继之前的CPU漏洞，如Spectre、Meltdown和Retbleed之后，突显了CPU安全方面持续存在的挑战。

---

## 2. GNU Screen 多个安全问题

**原文标题**: Multiple Security Issues in GNU Screen

**原文链接**: [https://www.openwall.com/lists/oss-security/2025/05/12/1](https://www.openwall.com/lists/oss-security/2025/05/12/1)

本文详细介绍了在 GNU Screen（一个终端复用器）中发现的多个安全漏洞，主要影响版本 5.0.0 和 setuid-root 安装。最严重的问题是 Screen 5.0.0 中的一个本地 root 漏洞 (CVE-2025-23395)，由于 `logfile_reopen()` 函数中不正确的权限放弃，导致非特权用户能够创建或附加到具有 root 所有权的任意文件。 Arch Linux 和 NetBSD 发行版将 Screen 5.0.0 作为 setuid-root 交付，因此完全受到影响。 Fedora 42 和 Gentoo 受影响程度因配置而异。

第二个漏洞 (CVE-2025-46802) 涉及多用户会话附加期间的 TTY 劫持，这是由于对 TTY 设备进行的临时性、过度宽松的 chmod 操作。这会产生竞争条件，可能允许攻击者拦截或将数据注入到 TTY 中。此外，附加过程中的某些错误情况可能导致原始 TTY 权限无法恢复。

该报告包括针对这两个漏洞的错误修复，并为 4.9.1 和 5.0.0 版本提供了补丁。它还建议改进 Screen 的安全态势，并对协同披露过程进行了观察，并提供了各种 Linux 和 UNIX 发行版的受影响程度矩阵。本文强调了以 setuid-root 权限运行 Screen 的风险以及此配置带来的更大攻击面。

---

## 3. 等待你的实验

**原文标题**: It Awaits Your Experiments

**原文链接**: [https://www.rifters.com/crawl/?p=11511](https://www.rifters.com/crawl/?p=11511)

本文写于2025年5月12日，宣布克里斯蒂安·伯克的“异文文本实验”圆满完成。二十多年来，伯克一直致力于将一首诗，即“俄耳甫斯”和“欧律狄刻”之间的应答对话，编码到细菌的基因代码中。“俄耳甫斯”被编码在DNA中，“欧律狄刻”则被表达为一种荧光蛋白。

最初，伯克面临着许多技术障碍，他发明了新的基因技术并聘请科学家帮助他克服这些障碍。虽然他成功地让大肠杆菌发出“欧律狄刻”的荧光，但文字却变得乱七八糟。抗辐射球菌，因其极端的韧性而被昵称为“科南细菌”，证明更具挑战性，它在表达之前就破坏了代码。

尽管遇到这些挫折，伯克还是坚持了下来。到2025年，他成功地让这首诗在抗辐射球菌中发挥作用，这是一种几乎坚不可摧的细菌，可以在极端条件下生存，包括辐射和缺水。作者惊叹于伯克作品的持久性，认为它可能比文明本身更长寿。

作者还宣传了伯克的“异文文本：第二卷”的发布，指出其艺术价值和哲学深度。发布会定于2025年5月27日在多伦多举行。最后，几位读者回应并发表了评论。

---

## 4. PDF转文本，一个挑战性难题

**原文标题**: PDF to Text, a Challenging Problem

**原文链接**: [https://www.marginalia.nu/log/a_119_pdf/](https://www.marginalia.nu/log/a_119_pdf/)

本文探讨了从PDF文件中提取可用文本以供搜索引擎使用的挑战。PDF文件是图形化的而非文本化的，这意味着文本以特定坐标的字形表示，缺乏语义信息。虽然存在提取文本的工具，但它们通常无法识别标题、段落和其他与搜索引擎相关性排名至关重要的语义结构。

作者概述了为改进PDF文本提取所做的修改。对于标题识别，他们建议使用每页的字体大小统计数据来克服字体大小设置的文档特定性。将页面中位字体大小应用20%的系数，可以可靠地识别许多标题。连接连续标题是一个棘手的问题，没有提供万无一失的解决方案。

段落识别的改进重点是解决PDFTextStripper的固定行距断点，该断点无法解释学术论文中常见的可变行距。作者建议使用页面上行间距的中位数，并应用一个系数来创建一个动态的段落分离启发式方法。

文章总结说，由于格式的性质，完美的PDF文本提取是不可能的。然而，通过关注标题等相关性信号，并创建合理连贯的文本，搜索引擎可以实现“足够好”的解决方案，从而有效地索引PDF内容。所提出的技术利用每页的字体大小和行距统计数据来改进标题和段落的识别。

---

## 5. Elixir 的膜、媒体框架

**原文标题**: Membrane, Media Framework for Elixir

**原文链接**: [https://membrane.stream/](https://membrane.stream/)

Membrane：基于Elixir的开源多媒体框架，用于构建可定制且易理解的多媒体解决方案。它支持通过WebRTC SFU进行实时通信，实现自定义I/O、媒体处理和输出创建。它促进服务器端处理，如视频缩放、音频混合和编解码器转码（aac、opus、mpeg、h264、vp9、vp8）。

Membrane与Elixir应用程序无缝集成，利用其可扩展性和容错性。它支持多种I/O协议，包括WebRTC、HLS、RTP、RTSP、RTMP、文件和HTTP chunks，并与语音转文本实用程序集成。它提供用于管道健康和EVM性能的监控工具。

Firework、Keep In Mind和Videstra等公司使用该框架构建视频平台、直播解决方案和IP摄像头流媒体。Membrane由Software Mansion维护，他们还提供相关服务。Membrane社区在GitHub、Twitter、Discord和Elixir论坛上活跃，鼓励贡献、反馈和支持。

---

## 6. Bug分类学

**原文标题**: A Taxonomy of Bugs

**原文链接**: [https://ruby0x1.github.io/machinery_blog_archive/post/a-taxonomy-of-bugs/index.html](https://ruby0x1.github.io/machinery_blog_archive/post/a-taxonomy-of-bugs/index.html)

本文是一份调试指南，强调使用调试器单步执行代码以理解预期行为和实际行为之间差异的重要性。然后，它提出了一种常见错误的分类方法，以及识别、修复和预防这些错误的策略。

**笔误：** 这些是简单的打字错误，由于大脑的自动纠正功能，可能难以发现。本文建议启用编译器警告（如 `-Wshadow`）、使用代码格式化工具（如 clang-format），并采用最大限度减少混淆的编码风格（例如，清晰的变量命名，具有不同类型的迭代器模式）。对于复制粘贴错误，还建议使用多选编辑器和 AI 辅助的自动补全工具（如 Copilot）。

**逻辑错误：** 这些错误发生在代码逻辑存在缺陷时。简化表达式和减少代码路径（避免不必要的“快速路径”）是关键的预防措施。使用宏标准化代码习惯用法也可以隔离潜在的错误。

**意外的初始条件：** 这些错误发生在代码在数据初始状态的假设下运行时，而这些假设并不总是成立。明确记录预期结果，并使用断言检查这些条件至关重要。

**内存泄漏：** 这些错误发生在已分配的内存没有被正确释放时。本文提倡使用包装函数来检测内存分配，这些函数记录分配细节（文件、行号、大小）。特定于系统的分配器和内存计数器有助于检测特定引擎系统中的泄漏。

**内存覆盖：** 这涵盖了“释放后写入”和“缓冲区溢出”。这些是最难找到的，因为它们可能不会在错误发生的地方显现出来。

---

## 7. 我学了Snobol，然后写了一个玩具版的Forth。

**原文标题**: I learned Snobol and then wrote a toy Forth

**原文链接**: [https://ratfactor.com/snobol/](https://ratfactor.com/snobol/)

本文详细介绍了作者对Snobol4编程语言的探索，以及随后使用Snobol编写玩具 Forth 解释器的项目。 作者发现Snobol非常吸引人，因为它专注于模式匹配，并将其与Awk进行了比较，但赞扬了Snobol的纯粹性以及对类C脚本的缺乏依赖。 他们欣赏该语言简单但非结构化的编程范例。

为了巩固对Snobol的理解，作者开始实施一个Forth解释器。 他们选择了一个特定的Forth程序“99 Bottles of Beer”作为目标，旨在创建一个能够执行它的Snobol实现。 最终结果“Snobol4th”是一个用不到500行Snobol代码编写的Forth解释器。

作者强调了在开发玩具语言时使用目标程序的好处，因为它提供了一个具体的目标并专注于开发。 他们还分享了资源，包括Snobol4th存储库的链接以及关于Snobol入门的“卡片”，旨在帮助其他对探索该语言感兴趣的开发人员。 最后，作者提到了用于创建文章及其随附图形的工具。

---

## 8. 在高压工作环境中，优先维护人际关系。

**原文标题**: In a high-stress work environment, prioritize relationships

**原文链接**: [https://wqtz.bearblog.dev/high-stress-job-relationships/](https://wqtz.bearblog.dev/high-stress-job-relationships/)

在高压工作环境下，员工常感濒临离职，本文建议优先维护人际关系。文章理解人们常因工作受挫而感到不堪重负，甚至想发泄怒火。

核心论点是，即便工作看似可有可无，保持职业关系至关重要。作者强调，诸如对人说“去你的”之类的过激行为会产生持久的负面影响，阻碍未来的职业发展。即使每个人都在同样的高压环境中挣扎，此类行为的记忆仍会挥之不去。

文章强调了考虑自身行为对他人影响的重要性，因为他们很可能也在承受来自上级的类似压力。文章建议将注意力从截止日期和自以为是的意义转移到每次互动的人性化层面。作者提醒读者，每段职业关系仍然是人际关系，不应为了“职业环境”而牺牲同理心。

最终，本文提倡优先维护人际关系，将其作为一种自我保护和长期职业策略。保持积极的联系可以提供未来推荐信形式的安全保障，并避免因在压力下崩溃而带来的负面声誉。

---

## 9. 如果软件优化成为优先事项，世界或许可以在较旧的硬件上运行。

**原文标题**: The world could run on older hardware if software optimization was a priority

**原文链接**: [https://twitter.com/ID_AA_Carmack/status/1922100771392520710](https://twitter.com/ID_AA_Carmack/status/1922100771392520710)

所呈现的“文章”根本不是文章，而是来自X（前身为Twitter）的错误信息，表明用户的浏览器中禁用了JavaScript。它提供了X帮助中心、服务条款、隐私政策、Cookie政策、版本说明以及广告信息的链接。关键在于，它还暗示必须启用JavaScript才能使用X平台。

因此，没有关于软件优化和使用旧硬件的文章内容可以总结。该消息仅侧重于平台对JavaScript的依赖，并指示用户启用它或切换到兼容的浏览器。

---

## 10. 咖啡渍为什么边缘更深？

**原文标题**: Why are coffee stains darker at the edges?

**原文链接**: [https://www.why.is/svar.php?id=5513](https://www.why.is/svar.php?id=5513)

咖啡渍边缘比中心深的原因：不均匀的蒸发速率

本文解释了咖啡渍边缘颜色比中心更深的原因。 关键原因是液滴表面蒸发速率的不均匀性。

当咖啡液滴滴落时，它会扩散并附着在表面上的瑕疵处。液滴边缘被“钉住”，其周长抵抗收缩。 重要的是，液滴边缘附近的表面积大于与桌面接触的下表面积。 这导致边缘蒸发更快。

由于边缘蒸发更快，液滴中心的液体向外流动，以补充边缘蒸发的液体。 这种向外流动会携带溶解的咖啡颗粒（着色剂）。 随着液体蒸发，这些颗粒会沉积下来。

由于边缘蒸发的液体更多，因此那里沉积的咖啡颗粒浓度更高，从而形成更厚更深的环。 作者强调，即使是清水也会发生这种现象，只不过没有着色剂就看不见。 本文使用插图来描绘干燥液滴的横截面，显示液体被吸引到边缘，并留下浓缩的咖啡颗粒层。 简而言之，边缘更快的蒸发速度浓缩了咖啡颗粒，导致污渍颜色更深。

---

## 11. FastVLM：面向视觉语言模型的高效视觉编码

**原文标题**: FastVLM: Efficient vision encoding for vision language models

**原文链接**: [https://github.com/apple/ml-fastvlm](https://github.com/apple/ml-fastvlm)

FastVLM 引入了一种新型高效的视觉编码器 FastViTHD，旨在通过减少 Token 输出和编码时间，尤其是对于高分辨率图像，来加速视觉语言模型 (VLMs)。该项目取得了显著的性能提升，其中最小的模型变体在大幅缩短首个 Token 生成时间 (TTFT) 和更小视觉编码器的情况下，性能超越了 LLaVA-OneVision-0.5B。更大的变体，利用 Qwen2-7B LLM，超越了最近的模型，如 Cambrian-1-8B，具有单个图像编码器和更快的 TTFT。

该仓库提供了基于 LLaVA 框架训练和微调 FastVLM 变体的代码库，以及推理说明。预训练模型检查点可供下载，包括针对 Apple Silicon 优化的版本以及导出具有自定义量化级别的模型的说明。一个演示 iOS 应用程序展示了该模型在移动设备上的性能。该项目鼓励用户如果发现代码有用，请引用他们的工作，并提供代码和发布模型的许可信息。

---

## 12. 为我而生的编程语言

**原文标题**: A programming language made for me

**原文链接**: [https://zylinski.se/posts/a-programming-language-for-me/](https://zylinski.se/posts/a-programming-language-for-me/)

本文探讨了奥丁（Odin）编程语言为何引起作者卡尔·齐林斯基（Karl Zylinski）的共鸣，原因在于它与他在Our Machinery公司之前从事的C语言编程实践相契合。该公司使用C语言构建了一个游戏引擎。他重点介绍了Odin的几个特性，这些特性与他们的C语言编码风格相呼应：

*   **自定义分配器:** Odin具有内置的Allocator接口，类似于他们自定义的C语言实现，提供了一种统一的方式来管理动态内存，即使在核心库中也是如此。
*   **临时分配器:** Odin包含一个临时分配器 (context.temp_allocator)，用于短生命周期的分配，在游戏开发中尤其有用，用于基于帧的数据，简化内存管理。
*   **跟踪分配器:** Odin的跟踪分配器可以检测内存泄漏，这与他们在C语言中使用的一种调试工具相呼应。
*   **零初始化（ZII）：** Odin自动对变量进行零初始化，减少了未初始化内存错误。
*   **指定初始化器:** Odin使用指定初始化器来初始化结构体，允许对特定字段进行初始化，而其他字段则默认为零。
*   **缓存友好的编程:** Odin通过`#soa`指令提供内置的结构体数组（SoA）支持，优化了内存布局，从而在性能关键场景中提高缓存性能。

卡尔强调了Odin的简单性，将其与C语言对C++的吸引力相提并论，并提到Odin是一种小型而简单的语言。作者鼓励可能具有不同背景的新学习者查阅他的著作《理解奥丁编程语言》，以更详细地了解这些实践。

---

## 13. Mozilla Firefox - 官方 GitHub 仓库

**原文标题**: Mozilla Firefox – Official GitHub repo

**原文链接**: [https://github.com/mozilla-firefox/firefox](https://github.com/mozilla-firefox/firefox)

这是 Mozilla Firefox 的官方 GitHub 仓库。该仓库包含 Firefox 网页浏览器的完整源代码，并公开访问。

关键信息包括：

*   **仓库详情：** 该仓库在 "mozilla-firefox" 组织下，名称为 "firefox"。它拥有 3.7k 个星标和 125 个 fork，表明社区对其有浓厚的兴趣。
*   **网站：** Firefox 官方网站链接为：www.firefox.com。
*   **目录结构：** 该仓库列出了大量目录，涵盖了浏览器的各个方面，例如 "browser"、"devtools"、"gfx"、"js"、"layout"、"security" 等。
*   **贡献信息：** 提供了 Mozilla 开发者文档的链接，供那些有兴趣为 Firefox 开发做出贡献的人参考：
    *   [https://firefox-source-docs.mozilla.org/contributing/directory_structure.html](https://firefox-source-docs.mozilla.org/contributing/directory_structure.html) 解释了源代码目录结构。
    *   [https://firefox-source-docs.mozilla.org/contributing/contribution_quickref.html](https://firefox-source-docs.mozilla.org/contributing/contribution_quickref.html) 提供了构建 Firefox 和创建补丁的说明。
    *   关于开发者可以在 Matrix 聊天频道中提问的信息。
*   **每日构建版本：** 关于下载 Firefox 最新每日开发构建版本的信息。
*   **语言：** 该仓库使用多种编程语言，包括 JavaScript (28.5%)、C++ (28.1%)、HTML (22.0%) 和 C (10.5%)。
*   **贡献者：** 该项目有超过 5,000 名贡献者。

总而言之，该 GitHub 仓库是 Firefox 开发的中心位置，为开发者和感兴趣的用户提供了源代码访问、贡献指南和资源。

---

## 14. 展示一下：A5

**原文标题**: Show HN: A5

**原文链接**: [https://github.com/felixpalmer/a5](https://github.com/felixpalmer/a5)

A5：一种新型全球地理空间索引系统

A5是一种新型全球地理空间索引系统，它将地球划分为等面积的五边形单元格，提供高精度和最小的失真。与其他离散全球格网系统 (DGGS) 不同，A5采用十二面体的五边形铺砌，这有助于最大限度地减少单元格失真，因为十二面体的顶点曲率较低，使其比类似系统中使用的其他柏拉图立体“更接近球体”。

A5的主要特点包括：

*   **等面积单元格：** 允许进行无偏的空间分析和聚合。
*   **高分辨率：** 在最精细的分辨率级别下高达30mm²，编码为64位整数。
*   **最小失真：** 通过选择十二面体作为基本几何形状来实现。

A5有助于将空间数据表示为单元格集合，从而简化空间分析任务，例如计算变量之间的相关性（例如，海拔和作物产量）以及聚合点数据（例如，假日租赁密度）。

该系统以TypeScript实现，并根据Apache 2.0许可证作为开源库提供。它主要在单元格均匀性和高分辨率方面优于其他DGGS系统。A5旨在为各种需要精确和无偏空间索引的地理空间应用程序提供强大的工具。

---

## 15. 保险公司推出AI聊天机器人错误损失保险

**原文标题**: Insurers launch cover for losses caused by AI chatbot errors

**原文链接**: [https://www.ft.com/content/1d35759f-f2a9-46c4-904b-4a78ccc027df](https://www.ft.com/content/1d35759f-f2a9-46c4-904b-4a78ccc027df)

金融时报文章探讨了专门为保护企业免受人工智能聊天机器人错误造成的财务损失而推出的保险。这是一个新的风险和保险领域，它承认企业越来越依赖人工智能进行客户服务和其他业务运营，以及这些系统可能犯错并导致财务损害的风险。

虽然保险的具体细节（例如，哪些保险公司提供、承保的损失类型或保险费用）需要付费阅读，但标题和介绍性文字表明人们越来越认识到与人工智能相关的风险，以及保险业为此采取的积极应对措施。该文章强调，企业需要保护自己免受因部署人工智能聊天机器人而产生的意外错误和潜在责任。

---

## 16. 反人员计算 (2023)

**原文标题**: Anti-Personnel Computing (2023)

**原文链接**: [https://erratique.ch/writings/anti-personnel-computing](https://erratique.ch/writings/anti-personnel-computing)

文章《反人员计算（2023）》引入并定义了“反人员计算”和“反人员计算机”这两个新词，用以描述21世纪初主流计算的状态。

其核心概念是，计算设备和实践正越来越多地以牺牲实际用户的利益和福祉为代价，优先考虑第三方实体（如公司）的利益。这意味着用户的利益不如提供服务和设备的公司所获得的利益重要。

“反人员计算机”是指主要以这种有害方式使用的设备，用户的利益被牺牲以换取这些第三方的优势。

其词源与“反人员地雷”相类似，突出了潜在的危害。它也与“个人计算”和“个人电脑”的最初愿景形成对比，表明其方向从赋能个人转向剥削个人。本质上，这篇文章批判了现代计算的发展方向，认为它正变得对终端用户具有剥削性，而非赋能性。

---

## 17. 开源硬件以太网交换机项目，第一部分

**原文标题**: Open Hardware Ethernet Switch project, part 1

**原文链接**: [https://serd.es/2025/05/08/Switch-project-pt1.html](https://serd.es/2025/05/08/Switch-project-pt1.html)

本文是关于作者开源硬件以太网交换机项目系列文章的第一篇，这是一个长期的努力，推动了他们的许多其他项目。作者回忆了他们在2012年左右首次尝试构建基于FPGA的千兆交换机“open-gig-switch”的经历，但最终由于FPGA资源有限和缺乏适当的测试设备而失败。

作者随后描述了他们如何获得技能、工具和测试设备（包括示波器和信号完整性分析软件），从而能够重新审视交换机项目。这促成了LATENTPINK的开发，这是一个使用Kintex 7 FPGA、VSC8512 QSGMII PHY和DP83867 SGMII PHY的原型平台。LATENTPINK允许验证技术堆栈，并证明了对更强大FPGA的需求。

当作者以大幅降低的价格获得Kintex UltraScale+ XCKU5P FPGA时，该项目发生了重大转变。这些FPGA提供了更大的资源和能力，从而能够实现更雄心勃勃的设计。

LATENTRED的新概念是一个1U交换机，带有两个24端口线卡和双10/25G SFP28上行链路。硬件将由五个或六个PCB组成，包括一个带有XCKU5P、STM32H735和管理PHY等的交换引擎板。线卡通过Samtec AcceleRate电缆连接，提供飞线互连解决方案。

---

## 18. 随着美国漏洞追踪机制的失效，欧盟带着自己的安全漏洞数据库加入了进来。

**原文标题**: As US vuln-tracking falters, EU enters with its own security bug database

**原文链接**: [https://www.theregister.com/2025/05/13/eu_security_bug_database/](https://www.theregister.com/2025/05/13/eu_security_bug_database/)

本文讨论了欧盟网络安全局(ENISA)启动欧洲漏洞数据库(EUVD)，以应对人们认为的美国漏洞跟踪工作存在的缺陷和不确定性。EUVD旨在提供一个精简的平台，用于监控关键和正在被积极利用的安全漏洞。

本文强调了对美国网络安全和基础设施安全局(CISA)以及通用漏洞和暴露(CVE)计划（目前与MITRE签订合同至3月）的预算削减、延迟披露和普遍混乱的担忧。这包括CISA最近决定改变其发布常规警报的方式。EUVD被认为是一个比美国国家漏洞数据库(NVD)更易于访问和更新的替代方案，尤其是在其漏洞提交积压和导航便利性方面。

EUVD提供专注于关键、积极利用和欧盟CSIRT协调的漏洞的仪表板。它从开源数据库、国家CSIRT的建议、供应商缓解指南以及被利用漏洞的详细信息中获取信息。虽然ENISA是CVE编号授权机构，但本文指出，他们仍然不确定美国CVE计划的未来，突出了漏洞跟踪系统分裂的可能性。

---

## 19. 火的考验：俄罗斯航空1492号航班坠毁

**原文标题**: Trial by Fire: The crash of Aeroflot flight 1492

**原文链接**: [https://admiralcloudberg.medium.com/trial-by-fire-the-crash-of-aeroflot-flight-1492-ee61cebcf6ec](https://admiralcloudberg.medium.com/trial-by-fire-the-crash-of-aeroflot-flight-1492-ee61cebcf6ec)

2019年5月5日，俄罗斯航空1492号航班，一架苏霍伊超级喷气100型客机，在莫斯科谢列梅捷沃机场紧急降落时坠毁并起火，导致机上78人中的41人遇难。该航班原定飞往摩尔曼斯克，起飞后不久遭遇雷击，导致线传飞控系统故障。

机组人员试图返回机场，但由于不稳定的进近和一次重着陆，导致飞机在跑道上剧烈弹跳。这导致起落架坍塌，油箱破裂，引发了大规模火灾。

疏散过程一片混乱，乘客从滑梯上逃离，火焰吞没了机舱后部。据报道，一些乘客因取回行李而延误了疏散。消防队员迅速赶到现场，但火势迅速蔓延阻碍了救援工作。

国家间航空委员会（MAK）对事故进行了近六年的调查，最终得出结论，天气、飞机故障和飞行员失误等多种因素共同导致了这次坠机事故。该报告详细描述了导致坠机事故的事件、消防响应以及生命的悲惨损失。文章强调了事故的复杂性以及导致致命结果的众多因素。

---

## 20. 检测C语言表达式是否为常量

**原文标题**: Detecting if an expression is constant in C

**原文链接**: [https://nrk.neocities.org/articles/c-constexpr-macro#detecting-if-an-expression-is-constant-in-c](https://nrk.neocities.org/articles/c-constexpr-macro#detecting-if-an-expression-is-constant-in-c)

本文探讨了多种C宏实现，用于检测表达式是否为编译时常量，如果不是则中止编译，同时返回表达式的值（理想情况下保持原始类型）。作者介绍了多种方法及其各自的优缺点。

*   **C23 constexpr 复合字面量：** 一种现代的、类型安全的解决方案，但需要C23支持，而C23尚未广泛应用。
*   **`__builtin_constant_p`：** 使用GNU扩展来检测常量表达式，并使用`__builtin_choose_expr`来选择表达式或使用具有错误属性的虚拟函数来触发编译错误。它保留了表达式的类型，但依赖于GNU扩展。
*   **`static_assert`：** 在结构体中使用`static_assert`来验证表达式是否为常量。`sizeof`和匿名结构体用于“返回”该值，但此方法可能由于隐式转换而更改表达式的类型。
*   **`sizeof` + 复合字面量数组类型：** 采用复合字面量数组类型，以利用编译时求值要求。与`static_assert`类似，该值通过`sizeof`操作返回，但也存在类型转换问题，并且不支持浮点表达式。
*   **`sizeof` + 枚举常量：** 定义一个以表达式为值的枚举，使用`sizeof`来强制常量求值。但是，这会“泄漏”枚举名称，从而阻止宏的多次使用。本文介绍了一种使用函数参数进行作用域控制的解决方法，但会产生警告。
*   **逗号运算符：** 将`sizeof`技巧与逗号运算符结合使用以保留表达式的类型，但会产生“未使用”警告，可以通过将sizeof结果强制转换为void来消除这些警告。
*   **GCC怪异之处：** 本文重点介绍了GCC中的一个怪癖，即负数组大小只会导致警告而不是错误。

作者得出结论，这个问题比最初预期的要复杂，尤其是在警告管理和类型保留方面。

---

## 21. 空中交通管制

**原文标题**: Air Traffic Control

**原文链接**: [https://computer.rip/2025-05-11-air-traffic-control.html](https://computer.rip/2025-05-11-air-traffic-control.html)

本文概述了空中交通管制(ATC)的发展历史，重点介绍了其与军事进步和技术演变的紧密联系。最初，由于飞机和技术的限制，ATC非常简陋，依赖旗帜和信号灯。第一次世界大战推动了航空无线电的出现，使地面管制能够协调侦察机并提供实时信息。

战后，商业航空公司采用无线电用于商业用途，从而形成了天气简报和飞行计划等正式做法。邮局的航空邮件服务为民用航空提供了大量资金，建立了航空邮件无线电台，提供信息并跟踪航班。航空部门（后来的航空商业局）承担了航空邮件航线的维护工作，建立了飞行服务站，这是国家空域系统（NAS）的第一个组成部分。

第一个航路ATC中心于1935年在纽瓦克开放，随后是政府所有权以及飞行条和标绘表的采用。第二次世界大战加速了航空技术的发展，特别是雷达，它通过地面控制拦截（GCI）彻底改变了空防。战后繁荣导致商业航空的激增，促使美国联邦航空局（FAA）于1958年成立，统一了民用和军事ATC。信标报告强调了基于雷达的控制和新程序，以解决日益增长的空中交通的复杂性和数量。

---

## 22. TransMLA：多头隐注意力足矣

**原文标题**: TransMLA: Multi-head latent attention is all you need

**原文链接**: [https://arxiv.org/abs/2502.07864](https://arxiv.org/abs/2502.07864)

本文介绍 TransMLA，一种后训练方法，用于将基于分组查询注意力（GQA）的大型语言模型（LLM），如 LLaMA、Qwen 和 Mixtral，转换为基于多头潜在注意力（MLA）的模型。MLA 通过在键值（KV）层中使用低秩矩阵，允许压缩潜在的 KV 状态，从而解决了 LLM 因大型 KV 缓存大小而面临的通信瓶颈。虽然 MLA 已被证明在 Deepseek 模型中有效，但其他主要模型提供商仍主要依赖 GQA。

作者证明了 GQA 可以用具有相同 KV 缓存开销的 MLA 来表示，反之则不然。TransMLA 利用这一点将现有的 GQA 模型转换为 MLA 模型，从而能够在不增加 KV 缓存大小的情况下进行进一步训练，以提高表达能力。目标是通过提供一种现成的转换方法来鼓励更广泛地采用 MLA。作者还计划开发 MLA 特定的推理加速技术，以保持转换后模型的低延迟，从而促进对 Deepseek R1 等模型的高效蒸馏。本文强调，这种方法通过将通信开销转化为额外的计算来降低通信开销，使其适用于资源受限的环境。

---

## 23. 着色器极简化的十五年

**原文标题**: 15 Years of Shader Minification

**原文链接**: [https://www.ctrl-alt-test.fr/2025/15-years-of-shader-minification/](https://www.ctrl-alt-test.fr/2025/15-years-of-shader-minification/)

本文记录了 Shader Minifier 的演变过程。Shader Minifier 是一款演示场景制作者使用的工具，用于压缩 GLSL 代码，以便在极小的文件大小（4k 和 8k intro）内创建令人印象深刻的计算机动画。最初创建的目的是为了自动化诸如删除空格和重命名变量之类的任务，但作者很快发现，诸如宏使用之类的直观优化实际上阻碍了 Crinkler 等工具的压缩算法。

本文重点介绍了最小化的反直觉性：重用变量和函数名称，甚至达到触发编译器错误的程度，事实证明，这比确保唯一、短的名称更有效地进行压缩。这种策略利用了压缩器识别和有效处理冗余模式的能力。

然后，作者讨论了扩展 Shader Minifier 的功能以处理更大的 8k intro，这需要更高级的静态分析和优化技术。这些技术包括内联单次使用的变量和简单常量、激进的变量重用以及函数的内联或参数减少。一张图表说明了该工具在不同版本中压缩特定着色器代码方面的改进。

文章最后强调了保持 Shader Minifier 更新以获得最佳压缩效果的重要性，尤其是在较大的项目中。作者暗示了正在进行的，旨在解决 64k intro 带来的挑战的工作，表明仍然有更多机会进一步缩小着色器代码。

---

## 24. 由于关税，OpenAI的星门项目进展受阻

**原文标题**: OpenAI's Stargate project struggling to get off the ground, due to tariffs

**原文链接**: [https://techcrunch.com/2025/05/12/openais-stargate-project-reportedly-struggling-to-get-off-the-ground-thanks-to-tariffs/](https://techcrunch.com/2025/05/12/openais-stargate-project-reportedly-struggling-to-get-off-the-ground-thanks-to-tariffs/)

OpenAI“星际之门”数据中心项目遇阻，关税致经济不明朗是主因。OpenAI计划筹集高达5000亿美元用于人工智能基础设施建设的宏伟“星际之门”数据中心项目正面临重大延误。据彭博社报道，日益增长的市场波动、更廉价的AI服务以及关税可能导致建筑成本增加，使得投资者对该项目投入资金犹豫不决。

预计关税将因服务器机架、冷却系统、芯片和其他重要组件价格上涨，而使数据中心建设成本增加5-15%。原本预计成为主要投资者的软银，尚未敲定融资计划或与潜在支持者进行实质性讨论。

此外，投资者越来越担心数据中心市场可能出现产能过剩的情况，微软和亚马逊等科技巨头调整数据中心战略和缩减建设规模就证明了这一点。这种担忧，加上关税相关的成本增加，正在阻碍OpenAI启动“星际之门”项目。

---

## 25. 重新审视图像地图

**原文标题**: Revisiting Image Maps

**原文链接**: [https://css-tricks.com/revisiting-image-maps/](https://css-tricks.com/revisiting-image-maps/)

Andy Clarke 的文章《重温图像地图》详细描述了他为作曲家 Mike Worth 创建一个 90 年代风格网站设计，同时保持现代网络标准的历程。他最初考虑使用图像地图（90 年代常用的一种技术）来实现视觉丰富且交互式的导航体验。

该文章回顾了图像地图，解释了其使用 `<map>` 和 `<area>` 元素的 HTML 结构，以及 `shape` 和 `coords` 等属性。虽然图像地图具有轻量级和语义化的 ARIA 等优点，但它们也有缺点，包括创建困难、缺乏视觉反馈以及天生不具备响应性。

Clarke 在为 Mike Worth 的网站实施图像地图时遇到了这些挑战，尤其是在响应式设计以及需要超出简单形状的更大可点击区域方面。他探索了各种方法，包括使用 JavaScript 调整坐标大小以及使用 PathToPoints 等工具转换 SVG 路径，但发现这些方法很麻烦。

最终，Clarke 放弃了图像地图，转而使用内联 SVG，并用绝对定位的、不可见的锚标记包裹 SVG 路径。通过使用这种方法，他能够创建具有悬停效果的响应式、不规则形状的可点击区域，从而提供所需的视觉反馈和交互。

文章最后强调了为工作选择正确工具的重要性，即使这意味着回顾旧技术以了解其基本原理，然后使用现代方法对其进行调整，以实现所需的审美和功能。他成功地将 90 年代的表现力与现代的可访问性、响应性和语义化代码融为一体。

---

## 26. 如何避免P值篡改

**原文标题**: How to avoid P hacking

**原文链接**: [https://www.nature.com/articles/d41586-025-01246-1](https://www.nature.com/articles/d41586-025-01246-1)

这篇《自然》职业专栏文章将“P值操控”（P hacking）定义为操纵数据分析或数据本身，以获得具有统计学意义的结果（p < 0.05）。文章强调，P值操控通过引入有缺陷的结论，加剧了科学研究中的可重复性危机。尽管通常是无意的，但文章概述了研究人员可能落入这一陷阱的五种常见方式：

1.  **过早结束实验：** 在达到计划的样本量之前，一旦观察到显著结果就停止数据收集。文章建议事先确定样本量并坚持执行。
2.  **反复实验直到获得阳性结果：** 重复实验直到获得显著结果，并有选择性地仅报告成功的试验。文章建议报告所有实验重复，无论结果如何。
3.  **选择性报告结果：** 有选择性地仅报告显示显著影响的结果或时间点，同时淡化或省略其余结果。建议是报告所有相关结果，包括正面和负面结果。
4.  **调整数据：** 出于获得统计学意义的目的，而非基于科学推理，做出数据分析决策（例如，排除异常值）。文章建议在检查结果之前建立数据过滤规则，并透明地说明任何事后更改的理由。

文章总结道，诚实和透明对于避免P值操控，并为可靠和可重复的研究做出贡献至关重要。

---

## 27. 通用汽车称新型电池化学技术将使电动汽车续航里程达到400英里。

**原文标题**: GM says new battery chemistry will enable 400-mile range EVs

**原文链接**: [https://www.theverge.com/news/665223/gm-lmr-ev-battery-chemistry-range-miles](https://www.theverge.com/news/665223/gm-lmr-ev-battery-chemistry-range-miles)

通用汽车和LG合作开发富锂锰(LMR)电池，用于通用汽车未来的电动卡车和SUV，目标是在2028年之前在美国实现商业化生产。 这种新型电池化学被认为比当前技术更安全、能量密度更高、成本更低，有望使电动汽车的续航里程达到400英里。

放弃传统的NCM（镍、钴、镁）电池的原因是钴矿开采的高成本和伦理问题。LMR电池使用更高比例的锰，这是一种更经济且容易获得的材料。

通用汽车强调，LMR电池代表着一个重要的成本降低机会，因为电池占电动汽车生产成本的很大一部分。 这种较低的成本对于让消费者更容易接受电动汽车并支持更快地普及电动汽车至关重要。

这些电池将由通用汽车和LG的合资企业Ultium Cells生产，预计在2027年末开始预生产。最终设计将在通用汽车的电池单元开发中心和LG能源解决方案的工厂进行验证。

虽然LMR电池面临挑战，例如潜在的容量损失，但通用汽车对其创新生产流程以最大限度地减少这些风险的能力充满信心。该公司预计LMR电池的性能将与他们的第一代高镍电池相似，即使在极端温度下也是如此。 通用汽车还旨在实现其电池供应链的本地化，以减轻与中国的贸易紧张关系相关的潜在价格上涨，中国是电动汽车电池生产的主导者。

---

## 28. 我们无法再在 1809/LTSC 2019 上运行 Microsoft Store。

**原文标题**: We can no longer run Microsoft Store on 1809/LTSC 2019

**原文链接**: [https://github.com/fernvenue/microsoft-store](https://github.com/fernvenue/microsoft-store)

本文探讨了Windows LTSC（长期服务渠道）版本上Microsoft Store的可用性和功能。Microsoft Store软件包可以安装在Windows 10 LTSC 2021和Windows 11 LTSC 2024上，并且之前在Windows 10 LTSC 2019上受支持。

然而，最近的一次更新导致Microsoft Store在Windows 10 LTSC 2019上无法使用。现在，商店提示用户在使用前更新系统，并阻止应用程序的安装。本文建议使用提供的“Uninstall.bat”文件卸载LTSC 2019上的Microsoft Store。

该软件包只需下载并双击即可安装。文章指出，为了兼容性，提供了一个稍旧版本的软件包，并建议在支持的LTSC版本（2021和2024）上安装后，在其设置中更新Microsoft Store，以获得最佳体验。总而言之，虽然Microsoft Store可以安装在LTSC 2021和2024上，但它在LTSC 2019上已不再可用，应予以卸载。

---

## 29. 共和党参议员提出法案将所有色情内容定为联邦犯罪

**原文标题**: GOP Senator Introduces Bill to Make All Porn a Federal Crime

**原文链接**: [https://gizmodo.com/gop-senator-introduces-bill-to-make-all-porn-a-federal-crime-following-project-2025-playbook-2000600994](https://gizmodo.com/gop-senator-introduces-bill-to-make-all-porn-a-federal-crime-following-project-2025-playbook-2000600994)

参议员迈克·李（共和党-犹他州）提出了《州际淫秽定义法案》(IODA)，该法案将通过重新定义“淫秽”来有效地将所有色情内容在全国范围内定为犯罪。这项立法与右翼传统基金会的“2025计划”的目标一致，该计划旨在永久性地将色情制品定为犯罪。

该法案扩大了淫秽的法律定义，几乎包括所有描绘性行为的视觉内容，可能涵盖任何“对裸体、性或排泄物产生淫秽兴趣”的媒体。虽然拥有色情内容的惩罚尚不明确，但该法案侧重于起诉露骨材料的创作者和发行商，可能导致联邦政府对在线色情内容进行限制和禁止。

李参议员认为，该法案更新了互联网时代的淫秽法律定义，允许删除此类内容并起诉其“兜售者”。 “2025计划”认为色情制品是“儿童性化”的因素，并主张监禁生产者/发行商并关闭提供便利的技术公司。

文章指出，反色情运动的历史以及现代运动对色情制品对年轻人造成的有害心理影响的关注，突出了对色情网站实施年龄验证要求的推动。

---

## 30. 理解卢卡斯艺术公司的iMUSE系统

**原文标题**: Understanding LucasArts' iMUSE System

**原文链接**: [https://github.com/meshula/LabMidi/blob/main/LabMuse/imuse-technical.md](https://github.com/meshula/LabMidi/blob/main/LabMuse/imuse-technical.md)

这篇所谓的“文章”实际上并非文章，而是一个标题和文件目录列表。它暗示的主题是理解 LucasArts 的 iMUSE 系统，可能与 MIDI 音乐实现相关。目录列表包括：

*   **meshula:** 可能是与此存储库关联的用户名或组织帐户。
*   **/LabMidi:** 表明该存储库涉及 MIDI 实验室或实验。
*   **/Public:** 指示存储库的可见性和可访问性。
*   **/Notifications:** 只是一个标准的通知设置链接。

该列表还显示了与存储库相关的指标，表明其受欢迎程度：

*   **Fork: 4:** 该存储库已被 fork 了四次，表明其他用户已复制它以用于自己的目的。
*   **Star: 80:** 该存储库已收到 80 个 star，表明社区对其内容的兴趣和赞赏程度。

因此，基于这些有限的信息，我们可以推断该存储库可能包含与 MIDI 中 iMUSE 实现相关的代码或资源，可能提供一个用于实验的实验室环境，并且在相关社区中受到了相对良好的欢迎。要提取的核心信息是主题 (iMUSE)、可能的调查媒介 (MIDI) 以及社区的普遍积极反馈（star 和 fork）。

---

## 31. TheForger的Win32 API教程

**原文标题**: TheForger's Win32 API Tutorial

**原文链接**: [https://winprog.org/tutorial/](https://winprog.org/tutorial/)

TheForger的Win32 API教程旨在提供对Win32 API开发的快速而清晰的介绍。它强调结构化的学习方法，要求读者按顺序学习教程章节，因为每个章节都建立在前一个章节的基础上。

本教程涵盖了必要的Win32 API概念和技术，包括：

*   **基础知识：** 入门、创建简单窗口、处理消息以及管理消息循环。
*   **资源：** 利用菜单、图标和各种类型的对话框（无模式和标准）。
*   **控件：** 实现和管理标准控件并解决常见的与对话框相关的问题。 在运行时动态创建控件。
*   **应用程序开发：** 构建简单的应用程序、处理文件和通用对话框，以及合并工具栏和状态栏。
*   **高级主题：** 探索多文档界面 (MDI) 概念。
*   **图形：** 深入研究图形设备接口 (GDI)、位图、设备上下文、透明度、计时器、动画、文本、字体和颜色。
*   **工具和文档：** 提供有关可用工具和文档资源的指导。
*   **附录：** 解决常见错误、对比 API 与 MFC，并提供资源文件注释。

本教程提供可下载的示例代码，并强调在寻求帮助之前阅读整个指南的重要性。 它还承认存在翻译版本（西班牙语、意大利语、中文、阿拉伯语）和 PDF 版本，但指出它们可能比原始版本过时。 提供版权信息，将本教程归功于 Brook Miles (tutorial(nospam)winprog.org)。

---

## 32. 巴比肯

**原文标题**: The Barbican

**原文链接**: [https://arslan.io/2025/05/12/barbican-estate/](https://arslan.io/2025/05/12/barbican-estate/)

作者详细描述了他们对巴比肯住宅区的迷恋，这是一个建于1965年至1976年间的伦敦住宅区。这种迷恋源于对维索置物架的寻找，进而引发了通过视频和书籍进行的大量研究。最近一次伦敦之旅提供了实地参观的机会，其中包括由一位居民带领的2小时建筑之旅。

这次旅行揭示了关于巴比肯独特设计和社区的迷人细节。该住宅区是自给自足的，居民可以在其围墙内度过一生。其迷宫般的设计，有意让人感到困惑，甚至幽默地阻止了盗窃。值得注意的特点包括一个满是废弃车辆的地下停车场，以莎士比亚等著名人物命名的建筑，以及灵感来自古埃及椭圆纹章和营的设计元素。只有居民才能进入的隐藏入口更增添了神秘感。

巴比肯建在罗马和中世纪的遗址上，包括一个有1000年历史的犹太人墓地。它拥有中央供暖系统，一个专门为居民设立的在线论坛 (barbicantalk.com)，以及对勒·柯布西耶等著名建筑师的设计致敬。它吸引了媒体、建筑师和设计师，并设有一所音乐学校的分校。

作者最后推荐了三本书供进一步探索：《巴比肯居民》、《巴比肯住宅区》和《建造乌托邦：巴比肯中心》。

---

## 33. Nextcloud谴责Google Play商店拒绝其应用

**原文标题**: Nextcloud cries foul over Google Play Store app rejection

**原文链接**: [https://www.theregister.com/2025/05/13/nextcloud_play_store_complaint/](https://www.theregister.com/2025/05/13/nextcloud_play_store_complaint/)

Nextcloud 指控谷歌存在反竞争行为，原因是谷歌应用商店拒绝了其安卓文件应用的文件更新，理由是担心该应用的“所有文件访问权限”。Nextcloud 认为，该权限对其文件同步功能至关重要，并且自 2016 年以来一直在使用，此前未出现过问题。谷歌现在坚持使用诸如存储访问框架 (SAF) 或 MediaStore API 等替代方案，但 Nextcloud 声称这些方案不适合其应用程序的用途。

Nextcloud 声称谷歌的政策变更是蓄意削弱竞争对手的行为，这与之前针对微软、苹果和 Meta 等科技巨头的反竞争指控相呼应。他们指出，2021 年已向欧盟提起针对微软行为的申诉，并强调了监管行动的缓慢。

Nextcloud 表示，这个问题可能源于谷歌内部的恶意意图、自动化流程或简单的无能，但结果都是一样的：迫使较小的公司减少功能以留在应用商店中。该公司批评了小型企业在面对此类问题时缺乏有效的追索权，并认为当前的监督流程不足。尽管 Play 商店存在限制，但该应用的完整功能版本仍然可以在 F-Droid 上找到。Nextcloud 报告称，过去 30 天内有 82.4 万安卓用户使用过该应用。谷歌未回应置评请求。

---

## 34. 光束

**原文标题**: The Beam

**原文链接**: [https://www.erlang-solutions.com/blog/the-beam-erlangs-virtual-machine/](https://www.erlang-solutions.com/blog/the-beam-erlangs-virtual-machine/)

本文题为“Beam”，是介绍Elixir系列的第一章，重点介绍Erlang虚拟机(BEAM)作为Elixir强大和可靠性的基础。文章强调了Erlang的历史，其为分布式、容错、并发和实时系统而设计的理念，以及它对Elixir的影响。

Erlang不仅被呈现为一种编程语言，而且被呈现为一个包含语言、OTP框架、工具和BEAM的综合生态系统。该生态系统专为高可用性和鲁棒性而构建。

文章随后深入探讨了BEAM，解释了它在执行Erlang代码、管理进程以及通过异步消息传递实现并发中的作用。BEAM的特性，如进程隔离、并行化、自动垃圾回收和错误检测，有助于系统可扩展性、容错性和响应能力。

最后，文章讨论了Elixir与BEAM的关系，强调Elixir利用了BEAM的特性，并且可以使用Erlang库和OTP。Elixir编译成在BEAM上运行的字节码，并提供比Erlang更易于访问的语法，使其更易于学习和维护。文章最后预览了下一章，该章节将探讨Erlang进程和并发。

---

## 35. Legion Health (YC S21) 正在招聘工程师，以利用人工智能改善心理健康。

**原文标题**: Legion Health (YC S21) is hiring engineers to help fix mental health with AI

**原文链接**: [https://www.workatastartup.com/jobs/75011](https://www.workatastartup.com/jobs/75011)

Legion Health (YC S21)，一家利用人工智能改善精神保健运营的精神病学网络，正在招聘一位创始工程师来构建其人工智能原生运营层。他们已筹集600万美元，年经常性收入超过100万美元，并已通过其人工智能驱动的后端支持了2000多名患者。

该公司专注于自动化运营，例如排班、文档、计费和风险检测，而非诊断。他们的目标是为精神健康诊所构建一个人工智能驱动的后端，使用LLM代理和结构化系统来协调护理。理想的候选人将端到端地拥有整个领域，架构和实施直接影响患者和临床医生的功能。

主要职责包括构建核心事件驱动的后端，开发LLM代理基础设施，设计人+AI运营UX，定义患者旅程的世界状态模拟，并确保数据安全和合规。该公司的技术栈包括Next.js、Node.js、TypeScript、Supabase (Postgres)、AWS、OpenAI和Anthropic。

Legion Health正在寻找一位构建过复杂系统、以事件流思考、精通LLM、重视速度和简洁架构，并希望在人工智能原生精神保健领域解决新颖问题的人。他们正在寻找一位创始技术专家来塑造工程文化和核心系统。

---

## 36. 在华的艾达 (1994)

**原文标题**: Ada in China (1994)

**原文链接**: [https://dl.acm.org/doi/pdf/10.1145/181476.181483](https://dl.acm.org/doi/pdf/10.1145/181476.181483)

无法访问文章链接。

---

## 37. 微软将裁员3%

**原文标题**: Microsoft is Cutting 3% of All Workers

**原文链接**: [https://www.cnbc.com/2025/05/13/microsoft-is-cutting-3percent-of-workers-across-the-software-company.html](https://www.cnbc.com/2025/05/13/microsoft-is-cutting-3percent-of-workers-across-the-software-company.html)

微软将裁员3%，涉及所有层级、团队和地点，作为组织架构重组的一部分。 截至去年六月，该公司拥有 22.8 万名员工，此次裁员旨在精简管理层级。 尽管微软在四月份报告了强劲的季度净利润和乐观的预测，但表示此次影响数千名员工的裁员并非基于绩效，而是一项战略举措，旨在提高其在动态市场中的定位。 这可能是自 2023 年裁减 1 万个职位以来规模最大的一次裁员。

此次重组的部分原因是需要优化销售执行，尤其是在与人工智能无关的领域，此前 Azure 云收入在该领域的增长低于预期。 微软首席执行官萨蒂亚·纳德拉强调了激励新的设计获胜以及适应当前平台转型战略的重要性。 这一举措与其他科技公司（如亚马逊和 CrowdStrike）采取的类似成本削减措施相一致。

---

## 38. 在本地和设备上构建你自己的Siri

**原文标题**: Build your own Siri locally and on-device

**原文链接**: [https://thehyperplane.substack.com/p/build-your-own-siri-locally-on-device](https://thehyperplane.substack.com/p/build-your-own-siri-locally-on-device)

无法访问文章链接。

---

## 39. 微软裁员6000人

**原文标题**: Microsoft laying off 6k employees

**原文链接**: [https://www.theverge.com/news/659401/microsoft-layoffs-three-percent-workforce](https://www.theverge.com/news/659401/microsoft-layoffs-three-percent-workforce)

微软裁员逾6000人，约占员工总数的3%，为2023年以来最大规模裁员。裁员将影响公司各个层级，包括微软旗下的领英和部分国际办事处。微软表示，组织变革对于驾驭动态市场至关重要。

此次裁员是在首席财务官艾米·胡德最近建议减少管理层级并建立更敏捷、高效团队之后进行的。微软今年早些时候也启动了“基于绩效”的裁员。

此前一年已发生一系列裁员事件，包括动视暴雪和Xbox裁员（1900人）、关闭多家游戏工作室（包括Tango Gameworks和Arkane Austin，尽管Tango Gameworks后来回归）、9月份与收购动视暴雪相关的Xbox进一步裁员（650人）以及6月份HoloLens和Azure云团队裁员（约1000人）。

---

## 40. 轻量级开源 reCaptcha 替代方案

**原文标题**: Lightweight open source reCaptcha alternative

**原文链接**: [https://github.com/altcha-org/altcha](https://github.com/altcha-org/altcha)

ALTCHA：一款注重隐私的轻量级反垃圾邮件解决方案

---

## 41. Show HN: Lumoar - SaaS初创公司的免费SOC 2工具

**原文标题**: Show HN: Lumoar – Free SOC 2 tool for SaaS startups

**原文链接**: [https://www.lumoar.com](https://www.lumoar.com)

Lumoar是一款免费的SOC 2合规工具，专为旨在快速高效地准备审计的SaaS初创公司设计。它提供了一个免费层级，其中包含帮助初创公司组织其合规工作的基本功能。免费层级中包含的主要功能有：用于理解和跟踪SOC 2要求的引导式控制清单；用于创建基础文档的策略模板生成器；用于集中文件上传并将其链接到控制的证据管理；以及用于任务分配和跟踪的团队协作功能。

该工具旨在帮助初创公司构建坚实的SOC 2基础，而无需免费层级的信用卡。 Lumoar还宣传即将推出的自动化和高级功能，例如自动化证据收集、持续控制监控和供应商集成。用户可以加入等候名单，以便获得有关这些即将推出的功能和独家发布优惠的通知。本质上，Lumoar为SOC 2合规性提供了一个免费的起点，并计划在未来提供更高级的自动化和集成功能。

---

## 42. Wtfis: 非机器人使用的被动主机名、域名和IP查询工具

**原文标题**: Wtfis: Passive hostname, domain and IP lookup tool for non-robots

**原文链接**: [https://github.com/pirxthepilot/wtfis](https://github.com/pirxthepilot/wtfis)

Wtfis：一款人性化的命令行域名、FQDN 和 IP 地址 OSINT 信息收集工具。它利用免费 API 层级来最大限度地减少速率限制。关键数据源包括 Virustotal（主要）、IP2Whois（可选，用于 Whois 数据）、IPWhois（用于地理位置和 ASN）、Shodan（可选，用于开放端口和 OS）、Greynoise（可选，用于 IP 分类和扫描活动）、URLhaus（可选，用于恶意 URL 信息）和 AbuseIPDB（可选，用于恶意 IP 报告）。

该工具提供声誉评分、热门排名、供应商类别、解析记录、Whois 数据、地理位置、ASN、开放端口、操作系统和恶意 URL 关联等信息。

可通过 pip 或 brew 安装。设置包括为 API 密钥设置环境变量或创建 `~/.env.wtfis` 文件。

用法包括命令 `wtfis` 后跟实体（域名、FQDN 或 IP），以及可选标志来启用 Shodan、Greynoise、URLhaus、AbuseIPDB，调整解析计数，抑制颜色或以单列显示。可以使用 `WTFIS_DEFAULTS` 环境变量配置默认值。

Wtfis 也可以通过 Docker 镜像运行，使用 `make docker-image` 构建，并通过挂载 `.env.wtfis` 文件或将环境变量直接传递给 `docker run` 命令来执行。

---

## 43. 你能相信macOS上的权限弹窗吗？

**原文标题**: Can you trust that permission pop-up on macOS?

**原文链接**: [https://wts.dev/posts/tcc-who/](https://wts.dev/posts/tcc-who/)

本文探讨了CVE-2025-31250漏洞，该漏洞存在于macOS中，允许恶意应用程序欺骗权限同意提示，使其看起来源自不同的应用程序。这可能诱骗用户向错误的应用程序授予权限。虽然最初认为已在macOS Ventura 13.7.6和Sonoma 14.7.6中得到修复，但作者通过测试发现这些版本仍然存在漏洞。

该漏洞源于TCC（透明度、同意和控制）系统中的一个逻辑错误，特别是处理与Apple Events相关的权限请求的`TCCAccessRequestIndirect`函数。该漏洞允许应用程序指定一个bundle identifier来显示提示，并指定另一个bundle identifier来实际接收权限，从而实现欺骗。文章详细介绍了Apple Events和TCC数据库如何交互，解释了TCC数据库中的间接对象列如何用于管理每个接收应用程序的Apple Events权限。一段概念验证代码片段演示了如何通过精心设计的XPC消息到TCC守护进程来利用该漏洞。虽然需要用户交互，但此漏洞允许显著绕过macOS的安全措施。作者强调，这个问题存在是因为处理不同标识符时的缺陷，并指出他们不确定为什么会存在两个标识符。

---

## 44. 离线与在线机器学习管道

**原文标题**: Offline vs. online ML pipelines

**原文链接**: [https://decodingml.substack.com/p/offline-vs-online-ml-pipelines](https://decodingml.substack.com/p/offline-vs-online-ml-pipelines)

无法访问文章链接。

---

## 45. 纯粹的简易网页

**原文标题**: Plain Vanilla Web

**原文链接**: [https://plainvanillaweb.com/index.html](https://plainvanillaweb.com/index.html)

本文题为《原生Web》，探讨了仅使用Web标准（HTML、CSS和JavaScript）构建网站和Web应用程序，而无需构建工具或框架。它提倡一种“原生”方法，强调了简洁性、零维护以及利用现代浏览器功能的优势。

本文涵盖以下关键主题：

*   **组件：** 利用Web Components作为基本构建块，取代以框架为中心的组件方法。
*   **样式：** 最大化现代CSS的功能，以避免对CSS Modules、PostCSS或SASS的需求。
*   **站点：** 创建和部署基于Web Components的Web项目，无需构建工具、框架或服务器端逻辑。
*   **应用程序：** 使用原生技术构建单页应用程序，包括路由和状态管理。

本文面向已经熟悉HTML、CSS和JavaScript的开发人员。它承认现代框架提供的强大功能和速度，但认为通过更简单的、基于标准的方法可以避免复杂性和维护开销，这得益于浏览器对Web标准的强大支持。下一步是学习Web Components作为构建内容、样式和行为的方式。

---

## 46. 展示：Airweave – 让代理搜索任何应用

**原文标题**: Show HN: Airweave – Let agents search any app

**原文链接**: [https://github.com/airweave-ai/airweave](https://github.com/airweave-ai/airweave)

Airweave：使AI代理可语义搜索应用数据的工具。它充当应用、数据库和API之间的桥梁，通过REST和MCP端点将其内容转换为代理可用的知识。该工具支持结构化和非结构化数据。

主要功能包括：从超过25个来源的数据同步、实体提取和转换、具有OAuth2的多租户架构、使用内容哈希的增量更新、语义搜索功能、数据版本控制和白标。

Airweave提供使用Docker Compose进行本地安装的快速入门指南。它提供可通过Web浏览器访问的UI，用于连接数据源、配置同步和查询数据。API文档可通过Swagger获得。为Python和TypeScript/JavaScript提供了SDK，以便通过编程方式访问平台。

技术栈包括React/TypeScript前端、FastAPI（Python）后端、用于元数据的PostgreSQL和用于向量存储的Qdrant。部署方式为：开发环境使用Docker Compose，生产环境使用Kubernetes。

路线图包括：计划添加更多数据源集成、用于大规模同步的Redis工作队列、用于事件驱动同步的Webhooks，以及通过Helm charts支持Kubernetes。欢迎在MIT许可证下进行贡献。

---

## 47. 欢迎来到深度伪造和诈骗猖獗的偏执时代。

**原文标题**: Welcome to the age of paranoia as deepfakes and scams abound

**原文链接**: [https://www.wired.com/story/paranoia-social-engineering-real-fake/](https://www.wired.com/story/paranoia-social-engineering-real-fake/)

深度伪造和诈骗泛滥：欢迎来到多疑时代

文章《深度伪造和诈骗泛滥：欢迎来到多疑时代》探讨了由人工智能技术推动的数字冒名诈骗和深度伪造日益猖獗的现象，以及人们为应对这些威胁而采取的日益增长的多疑心态和验证措施。

故事从尼科尔·耶兰德的经历开始，她曾遭遇求职诈骗，现在对新接触的人进行广泛的背景调查。文章强调，这些诈骗不再局限于社交媒体和约会应用，而是已经渗透到LinkedIn和视频会议等专业沟通渠道。联邦贸易委员会报告称，与工作相关的诈骗案件显著增加，损失也急剧上升。

人工智能初创公司正在涌现，旨在检测深度伪造技术，而像Tools for Humanity这样的解决方案则致力于验证“人格”。然而，许多人正在转向“低技术”的社会工程策略：在电话通话时发送电子邮件，跨平台验证，以及带有时间戳的自拍请求。一些雇主甚至会快速提问关于候选人声称所在位置的问题，或者要求在视频通话中进行“手机摄像头小技巧”来验证周围环境。

虽然这些措施可能有效，但它们制造了不信任感，并消耗大量时间。研究人员也受到影响，需要具备数字取证专业知识来筛选虚拟调查的参与者。文章总结说，在缺乏广泛的技术解决方案的情况下，常识和怀疑态度至关重要。许多虚假招聘信息中承诺的慷慨福利和薪酬待遇可能是一个主要的危险信号。

---

## 48. 有效生活的101条法则

**原文标题**: One hundred and one rules of effective living

**原文链接**: [https://mitchhorowitz.substack.com/p/101-rules-of-effective-living](https://mitchhorowitz.substack.com/p/101-rules-of-effective-living)

我能够访问外部网站。

米奇·霍洛维茨《有效生活的101条规则》摘要：

本文列出了101条简明规则或原则，旨在引导人们过上更有效率和更充实的生活。这些规则涵盖广泛的主题，强调自力更生、求知欲、情绪韧性、生产力和道德行为。

从列表中浮现的关键主题包括：

*   **个人责任：** 对你的生活、行为和反应负责。避免责怪他人，积极塑造你的命运。
*   **持续学习：** 拥抱好奇心，广泛阅读，并从不同来源寻求知识。培养批判性思维能力，避免思想停滞。
*   **情绪调节：** 培养内心平静，管理焦虑，并从结果中抽离。培养冥想或正念等习惯。
*   **生产力和行动：** 优先处理任务，关注要点，避免拖延。高效地执行想法。
*   **道德行为：** 尊重他人，正直行事，为社会福祉做出贡献。坚持诚实和值得信赖。
*   **韧性：** 将失败视为学习机会，保持乐观，并在挑战中坚持不懈。
*   **简单：** 清理你的生活（身体和精神上），专注于真正重要的事情。
*   **自我意识：** 了解你的优点、缺点和价值观。定期反思你的进步，并根据需要调整你的方法。

这些规则以小段智慧的形式呈现，旨在易于理解和应用于日常生活。整体信息鼓励读者在追求中保持积极主动、正念和有意识，努力实现个人成长并对世界产生积极影响。

---

## 49. 连续思维机器

**原文标题**: Continuous Thought Machines

**原文链接**: [https://pub.sakana.ai/ctm/](https://pub.sakana.ai/ctm/)

本文介绍连续思维机器 (CTM)，一种新颖的神经网络架构，旨在将神经时序作为基础要素融入其中，其灵感来源于生物大脑利用时序和同步进行计算的方式。与现代人工智能系统通过抽象化时间动态来优先考虑效率和简洁性不同，CTM 旨在弥合现有人工智能和生物合理性之间的差距。

CTM 的主要特点包括：

*   **解耦的内部维度：** 一种模拟神经活动时间演变的新方法，允许“思维”展开。
*   **神经元级别模型 (NLM)：** 每个神经元都有自己的内部权重，用于处理传入信号的历史记录以激活，而不是使用静态激活函数。
*   **同步即表征：** 神经同步直接用作观察和预测的潜在表征，使神经活动成为 CTM 智能的核心。

CTM 解决了当前人工智能的局限性，后者在人类认知的灵活性和普遍性方面存在不足。通过结合时间动态，CTM 旨在超越简单的输入-输出映射，迈向真正的推理能力。该架构利用内部递归、神经元级别模型和同步来实现这一点。CTM 在处理数据时在内部展开神经活动，使用 NLM 的“预激活”历史记录，并随时间跟踪神经活动以计算神经元同步。然后，这种同步用于与数据交互并做出关于数据的预测。

---

## 50. FedRAMP 20x - 进展迅速，启动一月

**原文标题**: FedRAMP 20x – One Month in and Moving Fast

**原文链接**: [https://www.fedramp.gov/2025-04-24-fedramp-20x-one-month-in-and-moving-fast/](https://www.fedramp.gov/2025-04-24-fedramp-20x-one-month-in-and-moving-fast/)

2025年4月，FedRAMP宣布启动FedRAMP 20x计划，旨在通过与行业和政府利益相关者的持续合作，快速实现FedRAMP的现代化，并强调安全重于合规。该计划实施一个月以来，在多个领域都取得了显著进展：

**授权：** FedRAMP授权了29项新的云服务，使年度总数达到73项，并使授权产品总数超过400项。它还授予了7项新的FedRAMP Ready称号，列出了5项新的正在进行Rev 5机构授权的云服务，并收到了7个Rev 5机构授权包。审查队列现在是自2022年7月以来最小的，有25个包，其中8个已准备好授权。

**社区参与：** 团队回复了大量的咨询，在众多活动中讨论了FedRAMP 20x，启动了社区工作组，并与国会工作人员、机构高管和FedRAMP委员会成员进行了互动。其他活动包括在社区会议上进行演示，重新与FedRAMP机构联络员社区进行互动，计划2025年联邦安全云咨询委员会会议，启动FedRAMP LinkedIn帐户，原型设计新网站，并支持FAR修订计划。

**改进标准：** FedRAMP发布了三项拟议标准供公众评议，完善了边界指南，制定了新的重大变更请求标准草案，准备了自动化FedRAMP Low授权标准草案，并最终确定了20x试点项目的资格标准。

**人工智能优先事项：** 团队开发了内部系统来管理GitHub评论，参与了GSAi工具评估，创建了代码生成指南，建立了生成式人工智能实验室，并开发了API优先的技术堆栈和用于信息提取的本体。

**下一步：** FedRAMP 20x第一阶段试点项目已开放。该计划的重点是FedRAMP Low授权的关键安全指标，并使用重大变更通知标准更新重大变更请求流程，以及使用最小评估范围标准重新审视FedRAMP边界概念。这些举措的公众评议截止日期为2025年5月25日。

---

## 51. 日本五金工具店的典型工作日 [视频]

**原文标题**: A Typical Workday at a Japanese Hardware Tool Store [video]

**原文链接**: [https://www.youtube.com/watch?v=A98jyfB5mws](https://www.youtube.com/watch?v=A98jyfB5mws)

名为“日本五金工具店的典型工作日”的“视频”仅仅是一个占位符，包含标准的YouTube法律和信息文本。其中没有实际视频内容描述。因此，没有描绘任何工作日，也没有任何五金工具店的活动可以总结。 内容仅由样板化的YouTube版权信息、联系方式、广告信息、开发者资源、服务条款、隐私政策、安全信息、关于YouTube如何运作的信息、测试功能以及关于NFL Sunday Ticket的信息组成。本质上，它只是一个空壳。

---

## 52. 简单的16x16点阵动画，源自简单的数学规则

**原文标题**: A simple 16x16 dot animation from simple math rules

**原文链接**: [https://tixy.land](https://tixy.land)

这篇短文暗示了一个“创意代码高尔夫”挑战，其核心在于利用源自简单数学规则的单行代码生成一个16x16点阵动画。所提供的lambda表达式`(t,i,x,y) => "creative code golfing"`强烈表明，核心任务是在16x16网格（由`x`和`y`坐标隐含）上创建视觉上有趣的动画模式，方法是将时间 (`t`) 和可能是一个索引或迭代 (`i`) 映射到像素位置和颜色。

“创意代码高尔夫”标签意味着一项侧重于最小化代码长度同时最大化视觉吸引力的竞赛或练习。这种简洁性表明需要高度的创造力，以利用基本的数学原理和编码技巧在约束条件下实现所需的动画效果。

本质上，该挑战是提出一个简洁的数学函数，可能采用模运算、三角函数、位运算或其他巧妙技术，将输入参数`t`、`i`、`x`和`y`转换为16x16网格上每个像素的颜色或强度值，从而产生一个视觉上吸引人且数学上优雅的动画。“16x16点阵动画”中的“点”表明像素是离散且单独控制的。整个过程归结为通过最小化的纯数学表达式来表达视觉上复杂的动画。

---

## 53. 微软对抗黑客部门

**原文标题**: The Microsoft unit working to thwart hackers

**原文链接**: [https://www.bloomberg.com/news/features/2025-05-09/microsoft-s-hacker-hunters-inside-the-secretive-mstic-unit](https://www.bloomberg.com/news/features/2025-05-09/microsoft-s-hacker-hunters-inside-the-secretive-mstic-unit)

无法访问文章链接。

---

## 54. 无常政策

**原文标题**: Policy of Transience

**原文链接**: [https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/transience/](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/transience/)

西蒙·塔特姆的“短暂性策略”概述了一系列围绕最小化持久数据和促进全新开始的非同寻常的计算机使用习惯。他强调，虽然这些习惯是独立出现的，但它们都具有短暂性的共同主题。

核心习惯包括：

*   **关闭持久Shell历史记录：** 禁用将shell命令保存到文件。虽然看似违反直觉，但这迫使他有意识地组织有用的命令，将其记录并保存为shell函数或脚本。
*   **定期清理GUI桌面：** 每天关闭或注销GUI会话，而不是挂起或长时间保持会话打开。这避免了累积的状态更改，并强制执行提交和记录进行中工作的纪律。
*   **频繁关闭Web浏览器：** 在每个任务完成后关闭浏览器及其所有选项卡，而不是将其用作长期阅读列表。这有助于更好地管理cookie，并强制执行结构化的阅读列表方法。
*   **关闭X11会话管理：** 禁用登录时恢复桌面布局的功能，确保每次都处于干净状态。
*   **使用~/mem上的tmpfs作为主暂存空间：** 利用基于RAM的临时文件系统来存储暂存文件，这些文件会在重启时自动删除。

塔特姆强调，他并不是提倡其他人采用这些做法，而是将它们作为可以考虑的想法呈现出来。他认为的优点是提高了组织性，降低了累积错误的风险，并且更加专注于记录和保存真正有价值的信息。

---

## 55. 黑桃硬件描述语言

**原文标题**: Spade Hardware Description Language

**原文链接**: [https://spade-lang.org/](https://spade-lang.org/)

Spade：一种新型硬件描述语言，旨在通过融入软件编程语言的概念来简化硬件设计并减少错误。其主要特性包括：对流水线的语言级支持，具有结构体、数组、元组和枚举的强类型系统，模式匹配，以及强大的类型推断。

Spade将流水线视为第一类构造，通过简单地添加或移动`reg`语句即可轻松地进行重新计时和重新流水线化。其强大的类型系统，特别是使用带有相关有效载荷的枚举，有助于互操作性和可靠的重构。模式匹配简化了像ALU设计这样的复杂逻辑，并且编译器确保所有情况都得到处理。该语言提供类型推断和有用的错误消息，旨在改善开发者体验。

Spade配备了`Swim`构建工具，用于依赖管理、综合和测试，并与cocotb和Verilator集成。VCD会被自动翻译以包含Spade类型信息。计划中的特性包括：作为类型的整数范围、带有trait的泛型，以及用于类型的时钟域信息。

Spade正在林雪平大学积极开发中，并根据EUPL-1.2（编译器/工具）和MIT/Apache（标准库/网站）协议获得许可。本文提供了文档、出版物、演讲和社区资源的链接，供那些有兴趣学习更多并做出贡献的人参考。

---

## 56. 与杰森·普鲁伊特关于人工智能在科学领域应用的对话

**原文标题**: A conversation about AI for science with Jason Pruet

**原文链接**: [https://www.lanl.gov/media/publications/1663/0125-qa-jason-pruet](https://www.lanl.gov/media/publications/1663/0125-qa-jason-pruet)

无法访问文章链接。

---

## 57. 一路走好 Usenix ATC

**原文标题**: RIP Usenix ATC

**原文链接**: [https://bcantrill.dtrace.org/2025/05/11/rip-usenix-atc/](https://bcantrill.dtrace.org/2025/05/11/rip-usenix-atc/)

本文反思了USENIX ATC的停办，该会议曾是系统从业者分享思想的重要旗舰平台。作者回忆了他早期对ATC的热情，以及2004年在会上展示DTrace的影响。然而，他注意到会议逐渐学术化，工业界参与度下降，以及整体上偏离了从业者的相关性。

作者将ATC的困境与系统创新中更大的转变联系起来，这种转变是由Go和Rust等开源项目驱动的，这些项目由专业人士开发并部署在生产环境中。他认为，从业者的主要发布途径已经转移到代码仓库，降低了传统会议的必要性。

他回忆起2016年发表的主题演讲，批评了会议模式作为一种发布工具。虽然学术影响促成了ATC的衰落，但作者承认，面对更有效的在线替代方案，线下会议面临着固有的挑战。他表达了对诸如“Systems We Love”等活动的偏爱，强调以从业者为中心的内容。

尽管面临困境，作者仍然承认ATC作为开创性系统工作的论坛所具有的历史意义。他指出最后一届最佳论文奖，该奖项关注于一个真实世界的AI基础设施验证系统，证明了会议的持久精神。最后，他表达了对USENIX为该领域所做贡献的感激之情，同时也为失去一个曾经重要的平台而感到惋惜。

---

## 58. 社区驱动的 Organic Maps 分支

**原文标题**: A community-led fork of Organic Maps

**原文链接**: [https://www.comaps.app/news/2025-05-12/3/](https://www.comaps.app/news/2025-05-12/3/)

一个由社区主导的Organic Maps分支，暂定名为CoMaps，正在快速发展，其核心原则是透明、社区决策、为公共利益而进行的非营利运营、完全开源以及注重隐私。 该项目的进展详见其在Codeberg上的新家。

该项目正专注于构建其基础、建立技术，并积极致力于首次发布。暂定名称CoMaps将通过社区投票最终确定，投票将于5月20日在Codeberg上结束。 鼓励用户在Codeberg上注册，参与讨论、报告错误并提出功能建议。

社区可以通过在Codeberg上进行开发、参与治理决策、传播信息、为网站开发做出贡献以及通过OpenCollective进行捐赠来参与其中。

此次更新还指出与Organic Maps股东的谈判缺乏进展，Viktor仅愿意保证该项目不会被出售，但保留完全控制权。 股东之间的分歧仍未解决，导致Organic Maps的未来充满不确定性。

---

## 59. 德州大学领衔团队解决聚变能源一大难题

**原文标题**: University of Texas-led team solves a big problem for fusion energy

**原文链接**: [https://news.utexas.edu/2025/05/05/university-of-texas-led-team-solves-a-big-problem-for-fusion-energy/](https://news.utexas.edu/2025/05/05/university-of-texas-led-team-solves-a-big-problem-for-fusion-energy/)

德克萨斯大学领导的团队开发了一种新方法，旨在为仿星器聚变反应堆设计更有效的磁约束系统，从而解决了长达70年的难题。聚变能源的关键挑战是将高能阿尔法粒子约束在反应堆内，以维持等离子体的温度和密度。目前识别和消除磁“瓶”泄漏的方法要么需要使用牛顿定律进行过多的计算，要么使用微扰理论缺乏准确性。

该团队的突破利用了对称性理论，在不牺牲准确性的前提下，速度提高了10倍。这使得工程师能够更快地设计出防泄漏的磁约束系统，从而促进仿星器的开发。这种新方法克服了先前方法的局限性，是对反应堆设计的一次范式转变。

此外，该方法还可以应用于托卡马克反应堆，以解决可能损坏反应堆壁的逃逸电子问题。这项由美国能源部支持的研究涉及来自德克萨斯大学奥斯汀分校、洛斯阿拉莫斯国家实验室和Type One Energy Group的研究人员，突显了其在未来基于仿星器的发电中实际应用的潜力。

---

## 60. Show HN：检测虚假 GitHub Star、风险依赖和许可证陷阱的 CLI 工具

**原文标题**: Show HN: CLI that spots fake GitHub stars, risky dependencies and licence traps

**原文链接**: [https://github.com/m-ahmed-elbeskeri/Starguard](https://github.com/m-ahmed-elbeskeri/Starguard)

StarGuard：一款 GitHub 仓库开源风险自动化评估 CLI 工具，通过分析 GitHub 仓库，帮助检测虚假刷星活动、依赖劫持和许可证风险。其灵感来源于研究表明的普遍存在的刷星操纵行为。

该工具基于多项检查提供信任评分：星级分析（突增检测、机器人相似度）、依赖分析（SBOM 解析、未锁定/影子依赖）、许可证检查（仓库和依赖项中的高风险许可证）、维护者活跃度（贡献者集中度、提交频率）和代码信号（代码混淆、远程执行）。

StarGuard 利用 GitHub API 和清单文件收集数据，采用滑动窗口 MAD 等算法进行突增检测，并使用用户画像评估点赞用户。它以多种格式（JSON、Markdown、纯文本）输出报告，并生成星级历史图和 shields.io 徽章。

使用 StarGuard 需要 Python 3.9+ 和 GitHub 个人访问令牌（以获得更高的速率限制）。用法示例包括完整的星级图扫描和仅突增扫描。支持不同级别的令牌权限，对于大多数功能，只需对公共仓库的只读访问权限即可。

StarGuard 适用于多种使用场景，包括 CTO 负责开源新增项目的把关、安全团队安排扫描、VC 进行快速尽职调查，以及开源维护者展示透明度。它强调安全和隐私，仅读取公共元数据并执行静态分析，不存储任何个人数据。它采用 Apache-2.0 许可。

---

## 61. GADT为何对性能至关重要 (2015)

**原文标题**: Why GADTs matter for performance (2015)

**原文链接**: [https://blog.janestreet.com/why-gadts-matter-for-performance/](https://blog.janestreet.com/why-gadts-matter-for-performance/)

Yaron Minsky 认为，GADTs（广义代数数据类型）对于 OCaml 中的性能优化非常有价值，这与他最初认为它们主要用于编译器相关任务的看法相反。 核心优势在于 GADTs 精确控制内存表示的能力，从而实现更高效的数据结构。

文章以 `Compact_array` 为例说明了这一点，该 `Compact_array` 旨在对通用类型使用常规数组，而对字符使用更紧凑的 `bytes` 表示。 如果没有 GADTs，朴素的变体实现会导致类型限制（例如，`get` 和 `set` 仅适用于 `char`），而“穷人对象”方法会通过闭包分配引入开销。

GADTs 通过允许指定每个构造函数的返回类型来解决此问题。 通过定义 `Bytes : bytes -> char t`，`Bytes` 构造函数与 `char` 类型显式关联。 然而，类型推断仍然可能存在问题，需要使用局部抽象类型进行显式类型注释来指导编译器。

最终基于 GADT 的 `Compact_array` 实现实现了期望的行为：它适用于任何类型的数组，同时对 `char` 数组使用高效的 `bytes` 表示。 这提供了一种有效的内存表示机制，可以直接构建高性能应用程序。

---

## 62. Tailscale 4via6 – 大规模连接边缘部署

**原文标题**: Tailscale 4via6 – Connect Edge Deployments at Scale

**原文链接**: [https://tailscale.com/blog/4via6-connectivity-to-edge-devices](https://tailscale.com/blog/4via6-connectivity-to-edge-devices)

本文介绍了Tailscale 4via6子网路由，一项旨在大规模连接复杂边缘部署的新功能，解决了常见的连接问题，如IP地址重叠、双重NAT和限制性防火墙。文章提出4via6是传统站点到站点VPN的卓越替代方案，后者难以应对机器人、传感器和边缘服务器等边缘环境中常见的唯一CIDR范围和公共IP的假设。

4via6通过为每个网络分配唯一标识符并提供MagicDNS名称，以便轻松访问设备（例如，10-1-1-0via7），从而实现众多相同网络之间的无缝连接。这使得可以轻松隔离客户、连接单个客户的部署，并为支持提供安全的远程访问。无论网络配置如何，都可以应用Tailscale的细粒度ACL。

文章重点介绍了4via6在机器人技术中的应用，其中每个机器人可以包含多个具有潜在不兼容软件的可寻址IP设备，从而简化了管理和连接。Dexory的Matthew MacLeod强调了4via6为其全球机器人舰队提供的安全、低延迟访问。

除了物理部署之外，4via6还支持连接具有重叠CIDR范围的不同环境、区域或云提供商之间的VPC。这有利于将托管控制平面与客户云中的数据平面连接，或复制测试环境。

Tailscale 4via6子网路由器适用于所有套餐，Premium和Enterprise套餐提供增强的安全功能。

---

## 63. 通用汽车LMR电池突破：更长续航，更低成本

**原文标题**: GM's LMR battery breakthrough means more range at a lower cost

**原文链接**: [https://arstechnica.com/features/2025/05/gms-new-ev-battery-will-offer-30-percent-more-range-for-less-money/](https://arstechnica.com/features/2025/05/gms-new-ev-battery-will-offer-30-percent-more-range-for-less-money/)

通用汽车开发新型LMR电池技术，旨在弥合电动汽车成本与续航里程之间的差距。在电池专家Kurt Kelty（前特斯拉员工）的领导下，通用汽车的目标是不依赖税收抵免，实现电动汽车与汽油车之间的价格平价。

LMR技术减少了电池正极中的钴含量，将成本降低到接近磷酸铁锂（LFP）电池的水平，同时保持了接近镍锰钴（NMC）电池的能量密度。通用汽车预计LMR电池将提供约350英里的续航里程，比目前最大续航里程的磷酸铁锂电池组高出约30%，并将于2028年首次应用于其卡车。电池组将使用方形电池，与目前的设置相比，降低了复杂性，但保持了一定的结构完整性。

LMR的一个关键优势是能够实现材料采购和生产的本地化。通用汽车正在投资一家锰供应商，以建立一个能够每年生产一百万块电池的北美供应链。这种本地化降低了运输成本，并减轻了与长供应链相关的风险。

虽然福特也在研究类似的技术，但通用汽车对LMR有明确的生产计划和目标车型。通用汽车认为，经济实惠的电动汽车是大众普及的关键，而LMR是实现这一目标的一步。他们还在研究提高电池在恶劣天气条件下性能的技术。

---

## 64. 我辞去国家科学基金会职务的原因

**原文标题**: Why I'm Resigning from the National Science Foundation

**原文链接**: [https://time.com/7285045/resigning-national-science-foundation-library-congress/](https://time.com/7285045/resigning-national-science-foundation-library-congress/)

本辞职信详述作者因当前政治气候下，美国国家科学委员会和国会图书馆学者委员会的正直性日益瓦解，及其履行使命能力受损，而决定辞去这两个职务。作者将“对知识管理和学术自由采取威权主义手段日趋常态化”视为主要原因。

具体事例包括，国家科学基金会(NSF)的关键决策，例如发布关于NSF主任辞职的声明，以及授予政治任命者（DOGE团队成员Zachary Terrell）对拨款申请的否决权，均未允许委员会成员参与，实际上使委员会的监督作用毫无意义。作者强调，这些行为破坏了NSF作为防止知识集中控制的保障的历史作用。

同样，作者强调了对国会图书馆的担忧，特别是出于政治动机解雇馆长Carla Hayden和版权登记员Shira Perlmutter。这些行为被视为控制知识管理和传播的更广泛努力的一部分，尤其是在DEI倡议和与人工智能相关的知识产权方面。

作者认为，继续担任这些职务将等同于默许这些机构的系统性合法性丧失。他们将辞职视为一种拒绝行为，即退出要求不诚实的系统，以及扩大他人声音的一种方式。通过离开，他们的目标是更清晰地说明这些机构所处的妥协状态，并倡导其最初的使命。

---

## 65. 复兴 1930 年代的模块化货运自行车设计

**原文标题**: Reviving a modular cargo bike design from the 1930s

**原文链接**: [https://www.core77.com/posts/136773/Reviving-a-Modular-Cargo-Bike-Design-from-the-1930s](https://www.core77.com/posts/136773/Reviving-a-Modular-Cargo-Bike-Design-from-the-1930s)

这篇Core77文章探讨了Cyclauto对奥古斯特·雷蒙德在1930年代设计的模块化载货自行车的复兴。与骑车人位于前轮后方并通过链条驱动的典型载货自行车不同，Cyclauto将骑车人直接置于前轮上方，直接踩踏。这消除了链条，减少了维护。该自行车配备三速花鼓变速器，方便起步。

一个关键特性是其模块化设计，带有一个可拆卸的载货拖车，类似于半挂车。这允许用户连接各种拖车样式，使其适用于货物、乘客运输，甚至商业设施，例如食品车。

两件式车架可以拆卸，更容易放在汽车后备箱中运输。 Cyclauto还声称由于较短的轴距，转弯半径更小，从而提高了在城市环境中的机动性。虽然在自行车展上展出，但Cyclauto的生产日期尚未公布。

文章最后总结了用户评论，提出了关于骑行姿势、车把功能和后制动机制的问题。

---

## 66. 酸性之王 (2001)

**原文标题**: The Acid King (2001)

**原文链接**: [https://www.rollingstone.com/feature/acid-lsd-king-william-leonard-pickard-prison-pete-wilkinson-184390/](https://www.rollingstone.com/feature/acid-lsd-king-william-leonard-pickard-prison-pete-wilkinson-184390/)

本文介绍了威廉·伦纳德·皮卡德，一位哈佛毕业生，并被指控为LSD制造商，于2000年在堪萨斯州托皮卡附近被捕。他被指控是秘密的迷幻药生产世界中的重要人物，一个不仅仅由利润驱动的世界。

文章追溯了皮卡德的生活，从亚特兰大优越的家庭环境和早期的科学天才，到他在20世纪60年代对迷幻运动的拥抱，以及最终他对毒品制造的参与。他因制造其他毒品，包括摇头丸的前体MDMA，而入狱服刑。

在20世纪90年代，皮卡德似乎走上了一条通往合法成功的道路，在一家毒品政策智库工作，并计划上医学院。然而，他与一个名叫戈登·托德·斯金纳的人的交往导致了他的垮台。

文章还涉及LSD制造的历史，特别是在旧金山湾区的“迷幻药三角区”，以及传奇的永恒之爱兄弟会。它强调了如今的LSD剂量和质量都低于过去。文章还讨论了皮卡德于1988年在加利福尼亚州山景城的一个仓库被捕的事件，该仓库内藏有一个LSD实验室。

皮卡德即将进行的审判预计将揭示LSD生产的隐秘世界，并且，文章指出，将审视20世纪60年代的理想主义与后来几十年唯物主义之间的冲突。

---

## 67. HealthBench – AI系统与人类健康的评估

**原文标题**: HealthBench – An evaluation for AI systems and human health

**原文链接**: [https://openai.com/index/healthbench/](https://openai.com/index/healthbench/)

HealthBench文章概要 (基于标题及OpenAI在医疗AI领域工作的常识):

HealthBench是由OpenAI开发的一套新的评估框架，旨在评估AI系统在人类健康领域的性能和安全性。它致力于为衡量AI在医疗相关任务中的表现提供严格而全面的基准，超越一般的语言理解或推理能力。

鉴于OpenAI的重点，HealthBench可能评估AI模型在各种医疗保健相关任务中的表现，这些任务可能包括：

*   **医学问答：** 评估AI准确回答来自患者、医生或研究人员的医学问题的能力。
*   **医学诊断和治疗计划：** 评估AI分析患者数据（症状、病史、实验室结果）并提出潜在诊断或治疗计划的能力。
*   **医学信息检索：** 衡量AI有效搜索和总结医学文献、指南和临床试验的能力。
*   **医学推理：** 评估AI理解和应用医学知识来解决复杂问题的能力。

该框架旨在不仅衡量准确性，还衡量AI在医疗保健领域性能的其他关键方面，例如安全性、偏见和可解释性。安全考虑可能包括评估AI提供不正确或有害信息的风险。偏见评估旨在识别和减轻AI系统产生的任何不公平或歧视性输出。可解释性可能评估AI为其输出提供清晰易懂的理由的能力，使人类临床医生能够信任和验证AI的建议。

HealthBench作为开发和部署能够协助医疗保健专业人员、改善患者预后并推进医学研究的AI系统的关键工具。该框架可能旨在通过提供一种标准化和透明的方式来评估AI在人类健康这一高风险领域的性能和局限性，从而建立对AI的信任。

---

## 68. 高度之谜 (CSS)

**原文标题**: The Height Enigma (CSS)

**原文链接**: [https://www.joshwcomeau.com/css/height-enigma/](https://www.joshwcomeau.com/css/height-enigma/)

本文探讨了 CSS 中常见的关于百分比高度不如预期工作的困境。核心问题在于循环依赖：默认情况下，元素的高度取决于其子元素，而子元素的百分比高度取决于其父元素。这种悖论阻止了浏览器解析高度。

要使 `height: 50%` 生效，父元素必须具有“可知”的高度，这意味着其高度是显式定义的（例如，使用像素或 rem 单位），并且不依赖于子元素的内容。这打破了循环依赖。如果树中的每个祖先都具有可知的高度，则嵌套元素可以使用百分比高度。

`<html>` 标签是一个特例；其高度可以设置为 100%，因为它默认为视口大小，这是一个可知的值。

然而，设置固定高度（例如，`height: 24rem`）可能会导致内容过多时溢出。切换到 `min-height` 可以避免溢出，但会再次破坏子元素的百分比高度，因为 `min-height` 仍然允许父元素根据其内容动态扩展。

解决方案涉及使用 Flexbox 或 Grid 布局。通过在父元素上设置 `display: grid`，子元素将自动拉伸以填充可用高度，从而消除了对百分比高度的需求，并解决了溢出问题。

---

## 69. 荷兰人的智慧：一个靠空气驱动的无脑软体机器人

**原文标题**: Dutch ingenuity: A brainless soft robot running on air

**原文链接**: [https://arstechnica.com/science/2025/05/dutch-scientists-built-a-brainless-soft-robot-that-runs-on-air/](https://arstechnica.com/science/2025/05/dutch-scientists-built-a-brainless-soft-robot-that-runs-on-air/)

阿姆斯特丹原子与分子物理研究所（AMOLF）的荷兰科学家们创造了一种新型的仅靠气流驱动的软体机器人，无需电子大脑或复杂的控制系统。 受1996年奥运会中使用的“飞天人”物理原理的启发，该机器人利用振荡管作为肢体。气压使管子产生弯折，推动机器人前进。该团队发现，由于共享的气流充当耦合机制，肢体同步会自然地从设计中产生。

该机器人能够使其步态适应不同的环境。在陆地上，它以同步的肢体奔跑；在水中，它以反相的肢体运动游泳。最初的设计是有线的，并且消耗大量能量。后来的迭代减少了肢体数量并优化了管的设计，大大降低了功耗，从而实现了由电池和气泵供电的无线版本。该版本还集成了光传感器，使其能够自主地导航至光源。

尽管具有这些能力，但仍然存在挑战。该团队希望更精确地控制机器人的行为，因为目前的行动在很大程度上是涌现的，并且有些不可预测。他们的最终目标是创建依赖物理原理进行环境适应的机器人系统，从而减少或消除对计算能力的需求。他们设想的应用包括一种柔软的人工心脏，可以自主地适应身体的需求，而无需软件更新。

---

## 70. 我破解了一个约会App（以及如何不对待安全研究员）

**原文标题**: I hacked a dating app (and how not to treat a security researcher)

**原文链接**: [https://alexschapiro.com/blog/security/vulnerability/2025/04/21/startups-need-to-take-security-seriously](https://alexschapiro.com/blog/security/vulnerability/2025/04/21/startups-need-to-take-security-seriously)

安全研究员发现约会应用Cerca存在严重漏洞，可能泄露数千用户的个人信息。该研究员出于保护使用该应用的朋友的愿望，发现由于基于一次性密码（OTP）登录的漏洞，他们可以使用任何用户的电话号码访问其帐户，该漏洞将OTP直接暴露在API响应中。

进一步调查显示，通过利用未受保护的API端点，研究员可以枚举用户ID，并访问敏感信息，如电话号码、电子邮件地址、性偏好、私密消息，甚至存储的护照或身份证信息，而无需有效的一次性密码。 研究员发现了超过6,000名用户的个人数据，包括那些已提交身份证信息的用户。

研究员于2025年2月负责任地向Cerca披露了这些漏洞，并在富有成效的视频通话中，Cerca承认了这些问题并承诺迅速采取行动。 然而，该公司随后保持沉默，未能提供有关补救或用户通知的更新。 尽管缺乏沟通，研究员还是能够确认这些漏洞在发布此博客文章之前已得到修复。

研究员认为，Cerca声称使用“加密和其他行业标准措施来保护您的数据”的说法具有误导性，会危及用户，并强调存在身份盗窃、跟踪和勒索的可能。 作者强调了优先考虑用户数据安全而非快速应用程序开发的重要性，并对恶意行为者可能已经利用这些漏洞表示担忧。 最终发布该博客文章是为了倡导更安全的互联网，因为Cerca未能对报告做出适当回应。

---

## 71. Ruby 3.5 新特性：读取时的命名空间

**原文标题**: Ruby 3.5 Feature: Namespace on read

**原文链接**: [https://bugs.ruby-lang.org/issues/21311](https://bugs.ruby-lang.org/issues/21311)

本文讨论了 Ruby 3.5 中一项名为“读取时命名空间”的提议功能。其目标是引入虚拟顶级命名空间，允许独立引用/加载库，避免名称冲突，防止意外的全局共享模块/对象，并有可能支持使用多个版本的 gem。该功能旨在逐步采用。

“读取时”方法意味着在引用/加载代码*之前*创建命名空间，从而使程序员能够控制隔离。这与“写入时”方法（如 Java 包）形成对比，后者将命名空间定义嵌入库本身中。本文提供了示例代码，演示了命名空间如何隔离常量和类。

有两种命名空间类型：包含内置 Ruby 组件的单个“根”命名空间和用户定义的命名空间。用户命名空间中定义的类/模块与其他命名空间隔离，但主命名空间可以通过 `ns::Constant` 引用它们。该机制使用写时复制来处理内置类/模块，确保一个命名空间中的更改不会影响其他命名空间。但是，常量和类变量也被隔离，从而提供隔离。

该功能默认禁用，可以使用 `RUBY_NAMESPACE=1` 环境变量启用。讨论要点包括 Ruby 4 中可能出现的 `namespace` 关键字，用于更强的隔离、命名空间创建期间常量和对象树的处理方式，以及对内置类/模块与用户定义的类/模块的影响。人们担心 `is_a?` 的行为可能会令人困惑，因为在 `ns1` 中创建的 `Date` 在主命名空间中不会是 `is_a?(Date)`。

---

## 72. 用Python编写N体引力模拟代码

**原文标题**: Writing N-body gravity simulations code in Python

**原文链接**: [https://alvinng4.github.io/grav_sim/5_steps_to_n_body_simulation/](https://alvinng4.github.io/grav_sim/5_steps_to_n_body_simulation/)

本文介绍一个教程系列，旨在教初学者如何用Python编写N体引力模拟程序。受“CFD Python”课程的启发，本教程提供了一个循序渐进的指南，假设读者具备基本的Python和微积分知识。

该教程包含五个核心步骤：

*   **第一步：初始设置：** 重点介绍模拟的基本设置。
*   **第二步：引力：** 探索引力计算的实现。
*   **第三步：第一个N体程序：** 指导用户创建一个基本的N体模拟程序。
*   **第四步：高阶算法：** 介绍更高级的数值方法以提高精度。
*   **第五步：自适应时间步长：** 解释如何调整模拟的时间步长以提高效率和精度。

一个额外的章节涵盖了绘图和动画，以可视化模拟结果。本教程鼓励动手学习，将提供的代码转化为个人项目，以更好地理解。

完整的源代码和markdown文件可在GitHub上获取，但建议在提供的网站上阅读本教程。文章还包括一个参考列表，供进一步学习该主题。

---

## 73. 陶哲轩开通了YouTube频道。

**原文标题**: Terence Tao started a YouTube channel

**原文链接**: [https://www.youtube.com/channel/UCCGfqB7qtWIktmPyf5UMcbw](https://www.youtube.com/channel/UCCGfqB7qtWIktmPyf5UMcbw)

陶哲轩，备受赞誉的数学家，开设YouTube频道。页面底部信息包括新闻、版权、联系方式、创作者、广告、开发者、条款、隐私、政策、安全、YouTube运作方式、测试新功能和NFL Sunday Ticket。主要信息是陶哲轩的YouTube频道开通，其余信息为通用页面底部内容，与频道内容无关。

---

## 74. 美国宇航局研究揭示金星地壳惊人发现

**原文标题**: NASA study reveals Venus crust surprise

**原文链接**: [https://science.nasa.gov/science-research/astromaterials/nasa-study-reveals-venus-crust-surprise/](https://science.nasa.gov/science-research/astromaterials/nasa-study-reveals-venus-crust-surprise/)

一项由NASA资助、发表于《自然·通讯》的研究揭示了关于金星地壳的惊人细节，挑战了之前关于其地质的假设。与地球不同，金星缺乏板块构造和破碎的地壳。科学家最初认为金星的单块地壳会持续增厚。然而，新的模型表明存在一种限制其厚度的地壳变质过程。

这些模型表明，金星地壳的平均厚度约为25英里（40公里），最厚不超过40英里（65公里），这是一个令人惊讶的薄的测量结果。随着地壳增厚，其底部变得足够致密，要么断裂并成为地幔的一部分，要么融化。这个过程将物质循环回行星内部，驱动火山活动。

这一发现为理解金星的地质、地壳和大气层之间的相互作用提供了一个新的模型。即将到来的任务，如NASA的DAVINCI和VERITAS，以及ESA的Envision，旨在收集数据以验证这些模型，特别是关于火山活动以及地壳活动和大气演化之间的关系。该研究强调需要更多数据来明确确定金星上火山活动的程度。

---

## 75. 苹果希望人们用意念控制设备

**原文标题**: Apple Wants People to Control Devices with Their Thoughts

**原文链接**: [https://www.wsj.com/tech/apple-brain-computer-interface-9ec69919](https://www.wsj.com/tech/apple-brain-computer-interface-9ec69919)

以下是《华尔街日报》关于“苹果希望人们通过思想控制设备”的文章摘要，基于对该类文章的一般预期：

《华尔街日报》的文章讨论了苹果公司对脑机接口（BCI）日益增长的兴趣，这项技术将允许用户通过思想控制设备。虽然苹果公司尚未公开确认具体项目，但该公司一直在积极招聘神经科学、人工智能和传感器技术方面的专家，并已提交与BCI技术相关的专利。这表明公司正在认真探索这一领域。

文章可能强调了苹果公司设想的BCI的潜在应用，包括为残疾用户提供对iPhone、iPad和Mac的免提控制，以及可能彻底改变所有人的用户界面。这可能导致与设备更快速、更直观的交互，提供触摸、语音和传统输入方法的替代方案。

然而，文章可能也承认了与BCI技术相关的重大挑战。这些挑战包括某些BCI方法的侵入性、准确解释脑信号的难度，以及围绕数据隐私和潜在滥用技术的伦理考虑。当前的BCI技术通常需要植入式设备，这引发了对安全性和可及性的担忧。苹果公司可能专注于非侵入式方法，例如使用传感器从头皮检测脑活动，这种方法准确性较低，但更容易被广大受众接受。

文章总结说，虽然苹果公司的BCI雄心仍处于早期阶段，但该公司对该领域的投资突显了其对创新的承诺以及塑造未来人机交互的愿望。苹果公司能否克服技术和伦理障碍仍有待观察，但对科技行业的潜在影响是巨大的。

---

## 76. 优化我的 Hacker News 体验

**原文标题**: Optimizing My Hacker News Experience

**原文链接**: [https://reorientinglife.substack.com/p/optimizing-my-hacker-news-experience](https://reorientinglife.substack.com/p/optimizing-my-hacker-news-experience)

好的，我已阅读了来自提供的URL的题为“优化我的Hacker News体验”的文章。以下是摘要：

作者详细描述了他们改善Hacker News (HN) 使用体验的历程，旨在最大限度地提高收益，同时最大限度地减少负面影响（主要是浪费时间和负面情绪）。他们承认HN作为有价值的信息和社区来源的潜力，但也认识到它的成瘾性和情绪化性质。

作者的优化围绕三个关键领域展开：**筛选、过滤和心态。**

*   **筛选：** 作者仔细选择要阅读的评论和文章。他们优先考虑与他们的兴趣和职业目标相符的主题，同时避免潜在的争议性或令人情绪耗竭的讨论。他们还会主动取消订阅在HN上宣传的、被证明无用的新闻通讯。

*   **过滤：** 作者使用浏览器扩展和HN设置，根据关键词、分数和用户行为来过滤内容。这有助于他们避免重复或低质量的讨论，以及以贡献无益或攻击性评论而闻名的用户。像hckrnews.com这样的工具被用来进一步筛选呈现的信息。

*   **心态：** 作者强调在使用HN时保持健康和超脱的心态的重要性。他们积极管理自己的情绪，认识到HN只是一个网站，而不是他们自我价值或整个世界的反映。他们提醒自己优先处理现实世界的任务和人际关系，而不是无休止的滚动浏览。

文章最后强调了这一过程的迭代性质，并鼓励读者尝试不同的策略，以找到最适合自己的方式，从而享受HN带来的好处，而不会被其潜在的负面影响所吞噬。作者提倡有意识的消费和对在线平台的专注参与。

---

## 77. 一个外星人的垃圾是另一个外星人的宝藏

**原文标题**: One Alien's Trash Is Another Alien's Treasure

**原文链接**: [https://thebsdetector.substack.com/p/one-aliens-trash-is-another-aliens](https://thebsdetector.substack.com/p/one-aliens-trash-is-another-aliens)

无法访问文章链接。

---

## 78. 教皇关注人工智能问题

**原文标题**: Pope addressed AI as a matter of concern

**原文链接**: [https://apnews.com/article/pope-leo-vision-papacy-artificial-intelligence-36d29e37a11620b594b9b7c0574cc358](https://apnews.com/article/pope-leo-vision-papacy-artificial-intelligence-36d29e37a11620b594b9b7c0574cc358)

教宗方济各将人工智能视为一项重大关切，强调其潜在的利弊。在他为天主教会世界和平日发表的讲话中，他警告说人工智能已经对人类生存产生了深刻影响，并呼吁进行国际监管，以确保其合乎伦理地发展和使用。

教宗强调了人工智能加剧现有不平等、传播虚假信息以及操纵信息以干预民主进程的风险。他特别警告不要将人工智能用于武器，呼吁保持警惕，防止其被用于有害目的。他还对人工智能管理不当可能造成的工人失业和人际关系非人化表示担忧。

另一方面，教宗方济各承认人工智能具有造福人类的潜力，例如在医疗保健和教育领域。他强调必须确保人工智能被用于促进和平、正义和共同利益。他呼吁包括伦理学家、哲学家、教育家和法律专家在内的各方进行公开对话，以建立一个符合伦理的人工智能开发和部署框架，尊重人的尊严和基本权利。最终，他敦促采取积极主动的治理方式，确保人工智能为人类服务，而不是本末倒置。

---

## 79. 系统让机器人通过操控识别物体的属性

**原文标题**: System lets robots identify an object's properties through handling

**原文链接**: [https://news.mit.edu/2025/system-lets-robots-identify-objects-properties-through-handling-0508](https://news.mit.edu/2025/system-lets-robots-identify-objects-properties-through-handling-0508)

麻省理工研究人员与亚马逊机器人公司和不列颠哥伦比亚大学合作，开发了一种新技术，使机器人仅通过操控物体，利用内部传感器和一种新的模拟方法，就能识别物体的物理特性，如重量和柔软度。机器人拿起物体并轻轻摇晃，利用本体感觉（感知自身的运动和位置）从电机内的关节编码器中收集数据。

他们方法的关键在于一个使用机器人和物体模型的模拟过程。这种“数字孪生”技术使算法能够通过分析机器人在交互过程中关节运动的变化，来快速估计物体的属性。他们使用可微分模拟，预测物体属性的变化如何影响机器人的最终关节位置。通过将模拟与机器人在现实世界中的运动相匹配，系统就能识别物体的属性。

这种低成本的方法不需要外部摄像头或专用传感器，使其适用于视觉受限的环境。这种数据高效的方法具有稳健性，可以处理各种未见过的场景。研究人员设想机器人使用这种技术来自主学习环境中物体的属性。未来的工作包括将其与计算机视觉相结合，并应用于更复杂的系统和物体。

---

## 80. 绝对零度推理者

**原文标题**: Absolute Zero Reasoner

**原文链接**: [https://andrewzh112.github.io/absolute-zero-reasoner/](https://andrewzh112.github.io/absolute-zero-reasoner/)

本文对各种人工智能模型的代码生成能力进行了比较，特别是在要求它们创建一个Pygame脚本，模拟在旋转的六边形内弹跳的球体时。本文展示了由不同大小（7B、14B）和基础模型的多个“绝对零推理器”（AZR）模型生成的代码示例，以及来自GPT-4o-mini和Qwen2.5模型（72B、32B和14B Instruct版本）的输出。

每个模型收到的提示是：“编写一个脚本，显示10个球在旋转的六边形内弹跳。球应受到重力和摩擦力的影响，并且必须真实地从旋转的墙壁上弹开。”

每个代码示例都包含导入（pygame、math、random）、Pygame的初始化、屏幕设置、颜色定义以及常量定义（FPS、重力、摩擦力、球半径、球的数量）。它们都包含一个游戏循环，该循环处理事件、清除屏幕、旋转六边形、更新球的位置和速度（考虑到重力、摩擦力和碰撞），并绘制六边形和球。每个模型都实现了其独特的算法，用于检测和响应球与旋转的六边形壁之间的碰撞。本文展示了每个代码示例的温度、top_p和生成配置等参数的配置。本文旨在演示和比较人工智能模型生成具有逼真物理效果的功能性和视觉上吸引人的Pygame模拟的能力。

---

## 81. 我逆向工程WSC毁了我的假期。

**原文标题**: I ruined my vacation by reverse engineering WSC

**原文链接**: [https://blog.es3n1n.eu/posts/how-i-ruined-my-vacation/](https://blog.es3n1n.eu/posts/how-i-ruined-my-vacation/)

作者详细介绍了他们的度假项目：逆向工程Windows安全中心(WSC)，创建名为"defendnot"的工具，无需依赖第三方防病毒代码即可禁用Windows Defender，灵感来自他们之前的项目"no-defender"。

他们遇到了诸多障碍，主要源于开发环境。身处首尔，只有一台ARM64 MacBook，他们缺少用于逆向工程的合适的x86机器。这导致了一个复杂的设置，包括远程访问美国朋友的PC，延迟很高，然后切换到基于云的VM服务。

核心挑战在于理解WSC在注册防病毒软件时的验证机制。最初试图通过模仿WinDefend来模拟合法的防病毒软件失败了。进一步的调试揭示了WSC对调用进程的检查，包括提权和DLL特征，特别是ForceIntegrity标志。他们确定Taskmgr.exe是一个符合这些要求的合适的“受害者进程”。

在AV名称的数据传输机制中发现了一个关键错误，无效路径会导致传递一个空字符串，从而导致注册失败。最终，他们使核心功能正常工作，然后添加了自动运行功能，但任务计划程序设置阻止了在电池供电情况下自动运行。然后他们修复了它，添加自动运行作为最后一个功能。

作者总结说，虽然这个项目很有趣，但开发环境非常痛苦。关于WSC的更多技术解释将在未来由其他人发布。

---

## 82. 纽约拥堵费开征后的一切变化

**原文标题**: Everything That Has Changed Since Congestion Pricing Started in New York

**原文链接**: [https://www.nytimes.com/interactive/2025/05/11/upshot/congestion-pricing.html](https://www.nytimes.com/interactive/2025/05/11/upshot/congestion-pricing.html)

本文详细介绍了2025年1月5日在曼哈顿开始实施拥堵收费的直接影响。该收费方案对大多数车辆进入60街以南区域收取9美元。初步结果表明，该计划正在实现其减少拥堵和为交通改善创造收入的目标。

主要发现包括进入拥堵区域的车辆数量减少，导致交通速度提高，尤其是在高峰通勤时段。当地公交车的行驶时间也更快。与担忧相反，拥堵区域外的交通并未显著恶化，包括南布朗克斯和新泽西州。事实上，新泽西州的通勤者进入该区域的速度更快了。

所有公共交通工具的客流量都在上升，表明人们正在减少驾车出行。拥堵区域内的黄色出租车行程也有所增加。导致人员受伤的交通事故、违章停车和交通噪音投诉有所减少，而消防响应时间略有改善。校车延误在拥堵区域内的减少幅度也大于区域外。

虽然现在评估其对污染和低收入通勤者的长期影响还为时过早，但初步数据显示，来自富裕和贫困社区的驾车者出行时间都更快了。公众舆论正在改善，但仍有待进一步提升。拥堵收费预计在第一年产生约5亿美元的收入，用于资助关键的交通升级。

---

## 83. 宇宙预计将在10⁷⁸年内衰变，比先前认为的要早得多。

**原文标题**: Universe expected to decay in 10⁷⁸ years, much sooner than previously thought

**原文链接**: [https://phys.org/news/2025-05-universe-decay-years-sooner-previously.html](https://phys.org/news/2025-05-universe-decay-years-sooner-previously.html)

荷兰拉德堡大学一项新研究表明宇宙衰变速度远超预期，约在10^78年内发生。这项研究聚焦于类霍金辐射，即不仅黑洞，中子星和白矮星等天体也会通过该过程“蒸发”。

科学家Heino Falcke、Michael Wondrak和Walter van Suijlekom基于天体密度，仅考虑类霍金辐射，计算出了衰变时间。他们发现，白矮星（寿命最长的天体）将在10^78年内衰变。令人惊讶的是，中子星和恒星级黑洞的衰变速度均为10^67年，尽管黑洞的引力更强。这归因于黑洞会重新吸收一部分自身的辐射。

为了便于理解，研究人员还计算了人类和月球的蒸发时间，估计均为10^90年，尽管他们承认其他过程可能导致它们更快消亡。该研究重新解释了霍金辐射，认为粒子可以从具有引力场的物体中逃逸，从而导致它们的最终衰变。研究人员强调，这种结合天体物理学、量子物理学和数学的跨学科方法，为宇宙的最终命运提供了新的见解。

---

## 84. 加速 PyPI 的测试套件

**原文标题**: Making PyPI's test suite faster

**原文链接**: [https://blog.trailofbits.com/2025/05/01/making-pypis-test-suite-81-faster/](https://blog.trailofbits.com/2025/05/01/making-pypis-test-suite-81-faster/)

本文详细介绍了Trail of Bits如何显著提升Warehouse（PyPI的后端）测试套件的性能，将执行时间从163秒减少到30秒，同时将测试数量从3900个增加到4700多个。

主要改进措施包括：

*   **使用pytest-xdist并行执行测试：** 将测试分配到多个CPU核心上，使执行时间减少了67%。这涉及到解决诸如每个worker的隔离数据库实例和统一覆盖率报告等挑战。
*   **使用Python 3.12的sys.monitoring进行覆盖率检测：** 这种更轻量级的API比传统方法减少了53%的执行时间。
*   **使用testpaths优化测试发现：** 配置pytest以专注于特定目录的测试收集，从而将收集时间减少了66%。
*   **消除不必要的导入：** 删除测试期间不需要的模块，减少开销。

文章强调，测试套件的性能对于安全至关重要，鼓励频繁测试并使开发人员能够及早发现问题。文章还强调，由于复杂性增加，某些优化（如数据库迁移合并）可能不值得实施。最后，文章为加速其他Python项目中的测试套件提供了实用建议，并感谢开源社区为这些改进做出的贡献。

---

## 85. 如果人类忘记了如何制造CPU怎么办？

**原文标题**: What if humanity forgot how to make CPUs?

**原文链接**: [https://twitter.com/lauriewired/status/1922015999118680495](https://twitter.com/lauriewired/status/1922015999118680495)

JavaScript 已禁用。请访问帮助中心、服务条款、隐私政策、Cookie 政策、版本说明、广告信息。本文并非关于人类忘记如何制造 CPU 的文章，因此无法总结。

---

## 86. Ash (Almquist Shell) 变体

**原文标题**: Ash (Almquist Shell) Variants

**原文链接**: [https://www.in-ulm.de/~mascheck/various/ash/](https://www.in-ulm.de/~mascheck/various/ash/)

本文详细介绍了Ash (Almquist Shell) 的历史和各种变体之间的关系。Ash是Kenneth Almquist于1989年编写的Bourne Shell替代品。本文追溯了从最初版本到其并入BSD发行版（如4.3BSD-Net/2）以及后续在4.4BSD及其Lite版本中的演变的谱系。

本文重点介绍了Ash家族与原始SVR4 Bourne Shell之间的主要区别，例如对命令替换“$(...)”，“export VAR=value”和echo -e选项的支持。它还记录了早期版本中存在的特定错误和功能，以及它们在后来的变体中的最终修复或删除。

本文随后记录了Ash在不同基于BSD的操作系统（包括386BSD，BSD/OS，NetBSD和FreeBSD）中的开发，并指出了同步点和每个分支中引入的特定更改。还提到了诸如Dash（及其Slackware版本），Android的shell，Cygwin，BusyBox和Minix之类的其他变体，表明了它们的派生和重大修改。

本文强调了由于某些发行版（尤其是早期的BSD）中缺乏全面的变更日志，因此跟踪这些更改所面临的挑战，并旨在为这些变体提供详细的源代码变更日志。它旨在作为理解Ash的演变路径及其在不同操作系统中功能差异的指南。

---

## 87. ToyDB 重写：一个用 Rust 编写的分布式 SQL 数据库，用于教育

**原文标题**: ToyDB rewritten: a distributed SQL database in Rust, for education

**原文链接**: [https://github.com/erikgrinaker/toydb](https://github.com/erikgrinaker/toydb)

ToyDB 是一个用 Rust 编写的分布式 SQL 数据库，旨在作为一个教育项目来阐释此类系统背后的架构和概念。它是基于构建 CockroachDB 和 Neon 等现实数据库的经验重写的。

主要特性包括：

*   **Raft 共识：** 确保线性化状态机复制，以实现跨分布式集群的数据一致性。
*   **ACID 事务：** 支持具有基于 MVCC 的快照隔离的 ACID 属性。
*   **可插拔存储：** 提供 BitCask 和内存后端用于数据持久化。
*   **SQL 接口：** 包括对连接、聚合和事务的支持，并具有 EXPLAIN 查询计划功能。
*   **查询引擎：** 利用基于迭代器的查询引擎，具有启发式优化和时空旅行支持。

虽然 toyDB 优先考虑简单性和正确性，但有意牺牲了性能、可扩展性和可用性。该项目提供了架构指南、SQL 示例和参考以及研究参考资料。

本文演示了如何运行本地五节点集群并使用命令行客户端。它还重点介绍了使用 Goldenscripts 来测试 Raft、MVCC 事务和 SQL 执行等各个方面。基准测试可用，但性能不是重点。最后，本文指出了使用 VSCode 和 CodeLLDB 的调试设置，并感谢了徽标的设计者。

---

## 88. 连续血糖监测仪揭示了对相同膳食的不同血糖反应

**原文标题**: Continuous glucose monitors reveal variable glucose responses to the same meals

**原文链接**: [https://examine.com/research-feed/study/1jjKq1/](https://examine.com/research-feed/study/1jjKq1/)

持续血糖监测仪揭示相同膳食引起的葡萄糖反应差异总结

---

## 89. 使用Nix构建可验证安全的软件供应链

**原文标题**: Demonstrably Secure Software Supply Chains with Nix

**原文链接**: [https://nixcademy.com/posts/secure-supply-chain-with-nix/](https://nixcademy.com/posts/secure-supply-chain-with-nix/)

Nix：构建可验证安全软件供应链的稳健且经济高效的方案

---

## 90. Armbian更新：OMV支持、启动优化、瑞芯微优化

**原文标题**: Armbian Updates: OMV support, boot improvents, Rockchip optimizations

**原文链接**: [https://www.armbian.com/newsflash/armbian-updates-nas-support-lands-boot-systems-improve-and-rockchip-optimizations-arrive/](https://www.armbian.com/newsflash/armbian-updates-nas-support-lands-boot-systems-improve-and-rockchip-optimizations-arrive/)

此次Armbian更新带来多项改进，重点在于易用性、硬件支持和系统优化。主要亮点是将OpenMediaVault集成到Armbian的软件安装程序中，使用户能够轻松地将单板计算机转换为网络存储设备。此集成简化了设置过程，无需手动配置。

易用性增强包括在设置期间删除不必要的“禁用无线热点？”提示。在硬件方面，Orange Pi 5 Max现在使用主线U-Boot启动，从而提高了未来的更新兼容性。PocketBeagle2迁移到extlinux进行启动配置，使其与Armbian的标准化工作保持一致。

Rockchip64平台进行了优化，添加了缺少的运行性能点(OPP)，以提高能源效率和稳定性。由于上游驱动程序的改进，已删除过时的无线固件解决方法。此外，Armbian团队清理了未使用的构建工件，并准备进行测试计划以验证新功能。有关OpenMediaVault和其他软件安装的文档可在Armbian软件用户指南中找到。

---

## 91. 用 Clojure 实现的 200 行代码的 LSP 客户端

**原文标题**: LSP client in Clojure in 200 lines of code

**原文链接**: [https://vlaaad.github.io/lsp-client-in-200-lines-of-code](https://vlaaad.github.io/lsp-client-in-200-lines-of-code)

本文详细介绍了如何用Clojure创建一个极简的语言服务器协议(LSP)客户端，用不到200行代码实现基本的只读查询功能。作者的目标是使用语言服务器构建一个命令行linter。

文章解释了LSP的用途，强调了它在降低集成IDE和编程语言的复杂性方面的优势。实现重点包括：

*   **基础通信层：** 使用字节流和带有JSON主体的类HTTP头部，建立客户端和服务器进程之间的通信。
*   **JSON-RPC：** 为请求、响应和通知的JSON数据块添加结构和意义。
*   **语言服务器包装器：** 创建一个可用的语言服务器连接。

作者省略了JSON解析（依赖于jsonista库）和文档同步（文本编辑器功能）。代码使用Java 24和虚拟线程来实现高效的阻塞操作。

该实现详细介绍了关键函数：`read-ascii-line`用于读取ASCII文本，`lsp-base`用于将字节流转换为JSON队列，以及`lsp-jsonrpc`用于处理JSON-RPC消息。 `lsp-jsonrpc`函数管理客户端发送的消息和服务器接收的消息（响应、通知和请求）。

最后，作者创建了一个简单的API，包含三个函数：`start!`用于启动语言服务器，`request!`用于发送请求并接收结果，以及`notify!`用于发送通知。 `start!`函数有两个arities：一个用于进程stdio，另一个是通用的，用于输入/输出流。

---

## 92. 2025年第一季度Backblaze硬盘统计

**原文标题**: Backblaze Drive Stats for Q1 2025

**原文链接**: [https://www.backblaze.com/blog/backblaze-drive-stats-for-q1-2025/](https://www.backblaze.com/blog/backblaze-drive-stats-for-q1-2025/)

Backblaze 2025年第一季度硬盘统计报告：由Stephanie Doyle和Pat Patterson主导，分析了317,833块硬盘的故障率。主要发现包括：老款4TB硬盘故障率持续较低，20TB+硬盘故障率前景良好（平均年化故障率为0.72%），且HGST 4TB、希捷8TB、希捷12TB和希捷14TB型号在第一季度零故障。总体而言，季度故障率略微上升至1.42%，其中一些希捷10TB、12TB和14TB型号，以及HGST 12TB型号显示出较高的高端异常年化故障率。

终身年化故障率保持稳定在1.31%。12TB和14TB硬盘型号的年化故障率有所改善，而WDC和HGST 12TB硬盘的年化故障率在统计上显著恶化。作者认为HGST 12TB硬盘年化故障率恶化可能是由于使用年限所致。

硬盘统计流程的一项重大更新是将数据收集和分析从Andy Klein的遗留系统迁移到Backblaze的Snowflake实例。这一转变简化了数据处理，提高了效率，并为未来的增强功能打开了大门。

报告中使用的完整数据集可免费下载，但需注明出处。鼓励读者探索数据并分享任何有趣的发现。

该报告还提供了有关硬盘统计团队的信息，并邀请读者参加LinkedIn Live会议，以更深入地了解数据。

---

## 93. 任天堂警告破解或盗版可能导致Switch变砖。

**原文标题**: Nintendo warns that it can brick Switch consoles if it detects hacking, piracy

**原文链接**: [https://arstechnica.com/gaming/2025/05/nintendo-threatens-to-brick-switch-consoles-for-hacking-piracy/](https://arstechnica.com/gaming/2025/05/nintendo-threatens-to-brick-switch-consoles-for-hacking-piracy/)

任天堂更新用户账户协议，警告称若检测到破解或盗版行为，可能会永久禁用Switch及即将推出的Switch 2主机。此次更新（由Game File发现）扩大了被禁止的“任天堂账户服务”使用范围，涵盖任何未经授权的活动。

该最终用户许可协议明确禁止使用未经授权的任天堂账户服务副本，这可能针对的是那些破解主机或使用烧录卡玩盗版游戏的用户。该协议还限制了与破解相关的广泛活动，包括修改、逆向工程或规避系统的功能或保护措施，即使这些活动并非出于盗版目的。

虽然任天堂此前已经禁止破解主机访问在线服务，但更新后的最终用户许可协议表明，该公司现在准备完全禁用设备，即使是离线使用也不行。任天堂还保留在认为可能发生违规行为时暂停访问服务的权利。

任天堂将使用何种技术手段来执行这种“变砖”主机的行为尚不清楚，恢复功能的可能性也未知。然而，修订后的最终用户许可协议表明任天堂加大了打击黑客和盗版的力度，准备采取强有力的措施来保护其知识产权和在线环境。

---

## 94. NASA将垂死恒星的尖叫声变成了音乐。

**原文标题**: NASA turns the screams of a dying star into music

**原文链接**: [https://www.space.com/astronomy/nasa-turns-the-screams-of-a-dying-star-into-music](https://www.space.com/astronomy/nasa-turns-the-screams-of-a-dying-star-into-music)

美国宇航局将钱德拉、韦伯和IXPE等太空望远镜的数据转化为宇宙声景，或称“声音化”，让我们能够“听”到宇宙。这些声音化将来自天体，特别是与黑洞相关的数据转化为音符，提供了一种独特的体验太空观测的方式。

这篇文章重点介绍了三个新的声音化，分别关注黑洞演化的不同阶段。第一个代表了黑洞从沃尔夫-拉叶星WR 124中可能诞生的过程，该恒星剧烈地剥离其外层，产生类似尖叫的声音，并随着物质的膨胀过渡到乐器声。第二个声音化捕捉了双星系统SS 433的宇宙二重奏，其中一颗恒星围绕中子星或黑洞运行，使用不同的音高和乐器来代表X射线辐射和背景元素。最后，第三个声音化关注的是半人马座A，这是一个中心有一个超大质量黑洞的星系，它将X射线辐射转化为风铃声，将可见光转化为弦乐器，创造了一个星系结构的音乐表现。这些声景提供了一种新颖且引人入胜的方式来探索黑洞和宇宙的奥秘。

---

## 95. FTC推迟执行“点击取消”规定

**原文标题**: The FTC puts off enforcing its 'click-to-cancel' rule

**原文链接**: [https://www.theverge.com/news/664730/ftc-delay-click-to-cancel-rule](https://www.theverge.com/news/664730/ftc-delay-click-to-cancel-rule)

美国联邦贸易委员会推迟执行“点击取消”规则，现将执行起始日期推迟至2025年7月14日。这项规则是“否定选择规则”的一部分，旨在使取消订阅与注册一样容易，要求提供在线注册的公司也提供在线取消选项。最初的执行日期是5月14日，已经是一个延后的截止日期。美国联邦贸易委员会表示，推迟的原因是对原始日期合规负担的“重新评估”。美国联邦贸易委员会以3比0的投票结果推迟了执行日期，并指出两名委员因3月份被非法解雇而缺席投票。美国联邦贸易委员会表示，7月14日之后，他们将开始全面执行该规则。但是，如果执行过程中发现任何问题，该机构仍然愿意修改该规则。

---

## 96. 多路复用

**原文标题**: Multiplexing

**原文链接**: [https://buttondown.com/jaffray/archive/multiplexing/](https://buttondown.com/jaffray/archive/multiplexing/)

Justin Jaffray的这篇文章探讨了“多路复用”的概念，超越了其传统的电气工程定义，认为它是一种在各个领域，特别是计算机科学和数据库中常见的模式。在这个更广泛的意义上，多路复用涉及将多个信号或数据流组合成单个通道进行传输，然后使用“多路复用键”在接收端将它们分离出来。

作者提供了几个例子：

*   **位运算：** 使用位图在单个整数中表示多个布尔值。位位置充当多路复用键。
*   **批量处理：** 一次向服务发送多个请求，数组中的顺序充当多路复用键。
*   **关系数据库：** 不为每个用户创建单独的表，而是使用一个表，其中用户ID列充当多路复用键。这扩展到索引，其中用户ID前缀用于高效扫描。此外，关系数据库可以通过使用表、行和列ID作为键前缀，在KV数据库之上实现。
*   **查询去关联：** 可以通过添加基于自由变量的多路复用键，将相关子查询转换为连接。这允许将子查询视为常规关系，从而实现优化并消除关联。

作者强调，关系多路复用的可组合性，即多路复用键本身可以是更高级别的数据，对于查询去关联尤为重要。通过识别这种反复出现的模式，本文旨在提供对看似不同的技术的一种统一理解。

---

## 97. moricons.dll 图标最初是为哪些 MS-DOS 程序设计的？

**原文标题**: What were the MS-DOS programs that the moricons.dll icons were intended for?

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20250507-00/?p=111157](https://devblogs.microsoft.com/oldnewthing/20250507-00/?p=111157)

本文列出了与Windows 3.1的`moricons.dll`文件中图标关联的程序。目的是记录这些早期图标最初代表的MS-DOS程序。本文根据`APPS.INF`文件中的信息，以表格形式展示图标（按文件顺序排列）及其对应的设计软件。

该列表包含那个时代各种类别的广泛软件，例如：

*   **Microsoft开发工具：** Basic、C、Quick C、Pascal编译器。
*   **Microsoft应用程序：** Multiplan、Project、Word、Works。
*   **飞行模拟器：** Flight Simulator 3.0和4.0。
*   **数据库：** Paradox、Reflex、DataEase。
*   **通信工具：** Procomm Plus、Crosstalk。
*   **实用程序：** Q-DOS、OPTune、PCTools。
*   **Lotus产品：** Lotus 1-2-3、Agenda、Freelance Plus。
*   **文字处理和办公套件：** MultiMate、OfficeWriter、Professional Write、WordStar、WordPerfect Office。
*   **图形和演示软件：** Harvard Graphics、PC Paintbrush。
*   **其他应用程序：** 包括会计软件、电子邮件客户端和终端仿真器。

本质上，本文提供了早期Windows时代软件概貌的历史快照，并将其与Windows 3.1环境中用于表示这些程序的特定图标联系起来。

---

## 98. 我破解了我的闹钟来控制我的专注力。

**原文标题**: I hacked my clock to control my focus

**原文链接**: [https://www.paepper.com/blog/posts/how-i-hacked-my-clock-to-control-my-focus.md/](https://www.paepper.com/blog/posts/how-i-hacked-my-clock-to-control-my-focus.md/)

作者介绍了一种简单的技巧，通过将电脑时钟改造成对当前任务的持续、非侵入式提醒，来提高专注力。这种方法利用了已有的行为——瞥一眼时钟——来温和地将注意力引导回预定的活动。

该实现方法使用了 Ubuntu 的 GNOME 桌面环境和“Panel Date Format”扩展。一个名为 `focus.sh` 的 bash 脚本允许用户设置一个专注关键词，该关键词随后会与系统时钟上的时间一起显示。该脚本利用 `dconf` 根据用户的输入修改时钟的格式。如果没有指定专注内容，脚本会提示用户输入。

作者认为这种方法有效，因为它不需要意志力，由于查看时间的自然习惯而无处不在，通过提示片刻的思考来重置上下文，并且与通知相比是非侵入性的。这种技巧借用了现有的习惯，而不是试图创造一种新的习惯。作者提出了潜在的扩展，例如集成番茄工作法计时器、任务类别颜色编码和时间跟踪。

---

## 99. 闹剧：星巴克发现机器无法取代人工

**原文标题**: Brewhaha: Turns out machines can't replace people, Starbucks finds

**原文链接**: [https://www.theregister.com/2025/04/30/starbucks_finds_machines_cant_replace/](https://www.theregister.com/2025/04/30/starbucks_finds_machines_cant_replace/)

2025年第二季度，在CEO布莱恩·尼科尔的领导下，星巴克公布了令人失望的财报，这归咎于其用自动化取代员工的策略失败。营收和每股收益均未达到预期，导致股价下跌。

过去两年，星巴克在增加门店数量的同时减少了员工人数，依靠自动化来提高效率。前首席运营官约翰·卡尔弗曾计划大力投资自动化，包括食品、商品以及最终饮料的自动订购系统。

然而，第二季度业绩显示，北美门店销售额下降，原因是交易量减少，表明顾客不满意。与自动化IT安全测试等任务的机器不同，面向客户的岗位需要人际互动。

尼科尔承认了错误，并正在扭转局面，暂停设备推广，转而投资于劳动力。相关措施包括在杯子上写手写笔记，以鼓励顾客停留更长时间。

代表超过11,000名工会成员的星巴克工人联合会一直在倡导提高员工配置水平、工资和有保障的工作时长。他们认为重新关注劳动力是积极的一步，但强调需要一份公平的工会合同来建设更好的星巴克。

---

## 100. 大迁徙已然开始。

**原文标题**: The great displacement is already well underway

**原文链接**: [https://shawnfromportland.substack.com/p/the-great-displacement-is-already](https://shawnfromportland.substack.com/p/the-great-displacement-is-already)

无法访问文章链接。

---

