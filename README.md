# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-07-13.md)

*最后自动更新时间: 2025-07-13 17:46:46*
## 1. 屏幕是如何工作的？

**原文标题**: How does a screen even work?

**原文链接**: [https://www.makingsoftware.com/chapters/how-a-screen-works](https://www.makingsoftware.com/chapters/how-a-screen-works)

由于提供的内容仅为“加载中...╌╌ END ╌╌”，因此没有可供总结的文章。我无法提供摘要，因为没有关于屏幕工作原理的信息。提示表明一篇文章正在加载，但加载过程已结束，没有任何实际内容。

---

## 2. 2025年首次阅读《神经漫游者》

**原文标题**: Reading Neuromancer for the first time in 2025

**原文链接**: [https://mbh4h.substack.com/p/neuromancer-2025-review-william-gibson](https://mbh4h.substack.com/p/neuromancer-2025-review-william-gibson)

无法访问文章链接。

---

## 3. Show HN: Linux 平台可兼容 Raycast 的启动器

**原文标题**: Show HN: A Raycast-compatible launcher for Linux

**原文链接**: [https://github.com/ByteAtATime/raycast-linux](https://github.com/ByteAtATime/raycast-linux)

这个“Show HN”帖子介绍了一款开源的、受 Raycast 启发的 Linux 启动器，旨在复刻这款流行的 macOS 应用的核心功能。主要功能包括可扩展的命令面板、扩展支持（包括从 Raycast 商店浏览和安装）、由 SoulverCore 驱动的强大计算器、剪贴板历史记录、带有动态占位符的片段以及通过 OpenRouter 实现的 AI 集成。

在努力实现兼容性的同时，该启动器也承认了由于 macOS 特定的 API、原生二进制文件以及无法直接转换到 Linux 的假定权限而造成的限制。

安装步骤包括下载 AppImage、使其可执行并运行它。它需要 glibc 版本 2.38。 Wayland 用户需要一个 udev 规则来实现全局片段扩展。

该帖子提供了从源代码构建的说明，需要 Rust、Node.js、Tauri 前提条件和一个 Swift 工具链。它使用 pnpm 进行包管理。感谢 Raycast 团队和 Acqualia（对 SoulverCore 的贡献）。该项目采用 MIT 许可证。

---

## 4. 绕过谷歌大型反广告拦截更新

**原文标题**: Bypassing Google's big anti-adblock update

**原文链接**: [https://0x44.xyz/blog/web-request-blocking/](https://0x44.xyz/blog/web-request-blocking/)

2025年7月，Derin Eryılmaz讨论了2023年发现的一个漏洞，该漏洞绕过了谷歌在Chrome Manifest Version 3 (MV3) 中的反广告拦截更新。MV3移除了`webRequestBlocking`权限，该权限对于广告拦截器动态阻止请求至关重要。

该漏洞利用了Chrome扩展的JavaScript API调用与浏览器C++后端交互的方式。 历史上，Chrome将JavaScript文件（“扩展绑定模块”）注入到页面中，以初始化和验证这些API函数。由于用户控制的网站可能进行操纵，这导致了过去的安全问题。虽然大多数API绑定都已移至C++，但`chrome.webRequest`保留了一些JavaScript绑定。

该漏洞源于`chrome.webRequest.onBeforeRequest`事件。 Eryılmaz发现可以使用该事件包装类的公共构造函数创建自定义事件。 这些自定义事件可以被操纵。 具体来说，`opt_webViewInstanceId`参数，最初用于Chrome平台应用程序管理嵌入式网站，允许跳过`webRequestBlocking`权限检查。 通过在自定义事件中欺骗WebView ID，扩展可以重新获得阻止功能。

Eryılmaz向谷歌报告了该漏洞，谷歌在Chrome 118中通过验证使用`opt_webViewInstanceId`的扩展的WebView权限对其进行了修补。 尽管有可能创建一个正常运行的MV3广告拦截器，但谷歌认为这不是安全问题，也没有奖励。 作者发现这很有趣，因为它表明一小段旧代码也可能存在漏洞。

---

## 5. Show HN: 以LeetCode风格学习LLM

**原文标题**: Show HN: Learn LLMs LeetCode Style

**原文链接**: [https://github.com/Exorust/TorchLeet](https://github.com/Exorust/TorchLeet)

此篇“Show HN”帖子介绍TorchLeet，一个旨在帮助用户通过LeetCode风格学习和实践PyTorch和大语言模型（LLMs）的资源。它包含两套题库：一套侧重于通用的PyTorch技能，难度从基础到困难不等；另一套专门针对从零开始实现LLM。LLM题库涵盖注意力机制、嵌入以及各种解码和训练技术等主题。

目标是通过独立解决问题来学习，避免使用GPT，并提供解决方案以供比较。内容按难度等级（基础、简单、中等、困难）组织，适用于两套题库。每个问题都包含带有TODO的不完整代码块来引导用户。

该帖子提供了关于如何安装依赖项、浏览项目结构以及使用问题的说明。它还鼓励社区贡献，欢迎提出新问题和改进现有问题。 TorchLeet旨在提供引导式的、动手实践，以加深对PyTorch和LLM的理解。

---

## 6. 基于 FreeBSD 知识的本地聊天机器人 RAG

**原文标题**: Local Chatbot RAG with FreeBSD Knowledge

**原文链接**: [https://hackacad.net/post/2025-07-12-local-chatbot-rag-with-freebsd-knowledge/](https://hackacad.net/post/2025-07-12-local-chatbot-rag-with-freebsd-knowledge/)

本文介绍如何创建一个本地聊天机器人，专门用于提供FreeBSD信息，对用户、管理员和开发者均有帮助。它强调本地聊天机器人定制化的优点，并且不提倡使用官方的chat.freebsd.org。

本指南侧重于配备Apple Silicon的macOS，但也适用于其他操作系统。步骤包括：

1.  **安装Ollama**: 使用`brew`安装Ollama，一个用于多种LLM（如gemma3:latest或deepseek-r1:70b）的API，并拉取一个基础模型。
2.  **安装Open-WebUI**: 安装Open-WebUI，一个带有内置向量数据库的UI，使用`uv`来管理Python环境。用户可以通过本地主机地址访问该UI。
3.  **知识输入**:
    *   **下载FreeBSD文档**: 安装必要的依赖项（Hugo, Ruby, git, bmake, gems like rouge and asciidoctor）后，克隆并构建FreeBSD文档。
    *   **上传文档到Open-WebUI**: 在Open-WebUI中创建一个知识库（"FreeBSD Official Docs"），并添加包含FreeBSD文档的目录。
4.  **创建模型工作区**: 在Open-WebUI中创建一个名为"FreeBSD Helper"的新工作区，设置基础模型（例如gemma3:latest），提供一个系统提示，指示机器人仅使用提供的知识来提供准确的、FreeBSD特定的技术回应，并链接"FreeBSD Official Docs"知识库。

最后，该指南指示用户启动一个新的聊天窗口，并选择"FreeBSD Helper"模型。它还建议谨慎添加可能降低LLM性能的非结构化数据。降低温度设置可以提供更精确的响应。成功聊天机器人的关键很大程度上取决于源数据的质量。

---

## 7. Infisical (YC W23) 正在招聘开发者关系工程师

**原文标题**: Infisical (YC W23) Is Hiring DevRel Engineers

**原文链接**: [https://www.ycombinator.com/companies/infisical/jobs/qCrLiJb-developer-relations](https://www.ycombinator.com/companies/infisical/jobs/qCrLiJb-developer-relations)

Infisical (YC W23) 正在招聘开发者关系工程师，助力构建 AI 时代的安全性基础设施栈。该职位包括创作引人入胜的技术内容（博客文章、视频、直播），帮助开发者发现、采用 Infisical 并取得成功。职责包括在 Reddit、X 和 Slack 等平台上与开发者社区互动，策划开发者新闻通讯，塑造技术特性定位，并在会议和网络研讨会上代表 Infisical。

理想的候选人拥有计算机科学学士学位或 2 年以上 DevRel 经验，对软件工程和开发者工具有深入的了解，具备出色的沟通技巧，以及跨多种格式的内容创作经验。需要位于旧金山或愿意搬迁。具备软件工程经验、社区管理经验或在开发者社区中已有影响力者优先考虑。

这是一个基础性的 DevRel 职位，提供机会塑造 Infisical 在安全性基础设施领域的影响力。Infisical 拥有一支强大的团队，成员来自 Figma、AWS 和 Red Hat 等公司，提供具有竞争力的薪酬、股权和额外福利。他们已从 Y Combinator、Google 和 Elad Gil 处筹集了 1900 万美元，客户包括 Hugging Face、Lucid 和 LG。

---

## 8. Axon的Draft One AI警察报告生成器旨在对抗透明化

**原文标题**: Axon's Draft One AI Police Report Generator Is Designed to Defy Transparency

**原文链接**: [https://www.eff.org/deeplinks/2025/07/axons-draft-one-designed-defy-transparency](https://www.eff.org/deeplinks/2025/07/axons-draft-one-designed-defy-transparency)

电子前哨基金会（EFF）调查显示，Axon公司的AI警务报告生成器Draft One旨在阻碍透明度和问责制。Draft One使用ChatGPT变体从执法记录仪音频生成报告，供警官编辑。然而，原始AI生成的草稿不会被保存，导致无法确定报告的哪些部分是由AI编写的，哪些部分是由警官编写的。

这种缺乏可审计性引发了对警务报告中存在的偏见、不准确和潜在虚假信息的严重担忧，因为很难评估错误是源于AI还是警官。EFF发现，该系统缺少基本的监督功能，例如无法轻松跟踪哪些警官正在使用Draft One或生成由AI创建的报告列表。

Axon公司故意设计该系统以避免给客户带来披露方面的麻烦，将便利性置于透明度之上。EFF强调，与文字处理器不同，Draft One涉及两方（Axon和警官），因此每个草稿都应被视为记录。

虽然Axon声称Draft One具有审计功能，但这些功能有限且使用起来很麻烦。加利福尼亚州正在考虑一项立法（SB 524），要求披露在报告中使用AI的情况并保留原始草稿。由于Draft One不保留草稿，如果该法案通过，它将违反该法案。最终，EFF认为Draft One缺乏透明度对司法结果构成重大威胁，并阻碍公众评估该技术的有效性和潜在危险的能力。

---

## 9. 强化学习的GPT-3时刻

**原文标题**: The upcoming GPT-3 moment for RL

**原文链接**: [https://www.mechanize.work/blog/the-upcoming-gpt-3-moment-for-rl/](https://www.mechanize.work/blog/the-upcoming-gpt-3-moment-for-rl/)

本文认为，强化学习(RL)正处于其“GPT-3时刻”的开端，即将转向跨多种环境的大规模训练，以实现强大的少样本、任务无关能力。目前的强化学习方法，类似于GPT-3之前的语言模型，依赖于在狭窄任务上的微调，导致泛化能力较差。

作者提出了一种名为“复制训练”的新范式来解决这一局限性。这涉及训练人工智能来复制现有的软件产品或功能，使用详细的规范和参考实现。这种方法简化了评估，因为成功可以通过行为匹配进行客观衡量。复制训练有助于人工智能模型准确阅读详细的指令、精确地执行它们、从错误中恢复、长期维持性能并展示韧性。

所需的训练规模估计与预训练大型语言模型相当，约为1万年模型面对任务的时间。尽管编写测试可能并非易事，并且复制任务有些人为性，但作者认为这种范式为生成强化学习泛化所需的海量数据集提供了一种可扩展的方法。即使不能完全实现劳动力自动化，复制训练也可以作为通往下一个范式的桥梁。作者强调，扩展强化学习训练在经济上是高效的，因为计算支出在总训练费用中占主导地位。

---

## 10. 格雷厄姆ANSI Common Lisp笔记 (2024)

**原文标题**: Notes on Graham's ANSI Common Lisp (2024)

**原文链接**: [https://courses.cs.northwestern.edu/325/readings/graham/graham-notes.html](https://courses.cs.northwestern.edu/325/readings/graham/graham-notes.html)

本文档记录了有关 Paul Graham 的 ANSI Common Lisp 的笔记，特别关注 Graham 的编码风格偏离典型实践并可能影响可维护性的领域。虽然总体上赞扬了代码的可维护性、可移植性和动机充分的函数定义，但这些笔记突出了以下方面的担忧：

*   **命名：** Graham 偏好简短、可能隐晦的名称。
*   **条件语句：** 过度使用 `if` 而不是 `cond`，导致嵌套结构。
*   **循环：** 厌恶 `loop` 结构，即使在它可能是最清晰的解决方案的情况下。
*   **递归：** 偏好递归而不是迭代，即使列表可能很长，可能导致堆栈溢出。

然后，本文档继续对特定章节（第 2 至 11 章，第 15、16 章）、“数据驱动的光线追踪器”、“面向对象的光线追踪器”以及附录 A 和 D 进行详细评论，建议对本书的代码和编码风格进行逐章审查。 本质上，这些笔记可作为理解和潜在地调整 Graham 编码风格的指南，并针对改进命名约定、条件结构、循环使用以及考虑大型数据集的迭代方法提出了具体建议。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 2 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 3 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 4 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 5 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 6 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 7 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 8 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 9 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 10 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 11 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 12 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 13 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 14 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 15 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 16 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 17 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 18 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 19 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 20 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 21 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 22 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 23 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 24 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 25 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 26 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 27 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 28 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 29 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 30 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 31 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 32 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 33 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 34 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 35 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 36 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 37 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 38 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 39 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 40 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 41 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 42 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 43 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 44 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 45 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 46 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 47 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 48 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 49 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 50 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 51 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 52 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 53 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 54 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 55 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 56 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 57 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 58 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 59 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 60 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 61 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 62 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 63 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 64 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 65 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 66 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 67 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 68 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 69 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 70 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 71 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 72 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 73 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 74 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 75 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 76 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 77 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 78 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 79 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 80 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 81 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 82 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 83 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 84 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 85 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 86 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 87 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 88 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 89 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 90 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 91 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 92 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 93 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 94 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 95 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 96 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 97 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 98 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 99 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 100 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 101 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 102 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 103 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 104 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 105 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 106 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 107 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 108 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 109 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 110 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 111 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 112 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 113 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 114 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 115 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 116 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
