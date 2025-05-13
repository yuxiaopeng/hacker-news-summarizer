# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-05-13.md)

*最后自动更新时间: 2025-05-13 17:50:20*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 2 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 3 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 4 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 5 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 6 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 7 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 8 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 9 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 10 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 11 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 12 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 13 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 14 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 15 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 16 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 17 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 18 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 19 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 20 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 21 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 22 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 23 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 24 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 25 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 26 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 27 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 28 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 29 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 30 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 31 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 32 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 33 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 34 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 35 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 36 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 37 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 38 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 39 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 40 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 41 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 42 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 43 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 44 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 45 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 46 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 47 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 48 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 49 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 50 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 51 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 52 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 53 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 54 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 55 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
