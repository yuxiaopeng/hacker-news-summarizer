# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-11-01.md)

*最后自动更新时间: 2026-11-01 21:21:54*
## 1. Show HN: HackerBooks – 类似于 HackerTube，但针对的是 HN 上提到的书籍

**原文标题**: Show HN: HackerBooks – HackerTube, but for books mentioned on HN

**原文链接**: [https://hackerbooks.org](https://hackerbooks.org)

**HackerBooks** 是一个发现平台，旨在搜集、整理并排名 Hacker News (HN) 讨论帖中频繁提及或讨论的书籍。受类似项目“HackerTube”的启发，它为技术和创业社区提供了一个专门的搜索引擎和图书馆。

该网站的核心功能是扫描 HN 的评论和文章以识别推荐书籍。随后，它将这些书目整理成一个可搜索的数据库，并根据受欢迎程度和提及频率进行排名。这使得用户无需在成千上万条存档帖子中手动搜寻，即可找到经同行认可的阅读材料。

**主要功能与信息包括：**

*   **排名系统**：用户可以按不同时间范围（包括“历史总榜”、年度和月度排名）筛选书籍，以了解当前的流行趋势或社区长青经典。
*   **分门别类**：平台将书籍划分为工程、计算机科学、商业、传记、哲学和小说等相关领域。
*   **上下文关联**：对于列出的每本书，网站都提供了返回原始 HN 讨论帖的链接。这让用户能够直接获取社区对该书的具体评价、书评及辩论。
*   **高效发现**：每个条目通常包含书目简介，以及指向 Amazon 和 Goodreads 等购买或评论网站的直接链接。

本质上，HackerBooks 实现了从技术社区自动收集书籍推荐的过程，将碎片化的讨论转化为有序、高价值的资源，助力专业发展与个人成长。

---

## 2. HackerTube：基于 HN 推荐视频构建的 YouTube

**原文标题**: HackerTube: YouTube built from videos recommended by HN

**原文链接**: [https://karpathy.bearblog.dev/hacker-tube/](https://karpathy.bearblog.dev/hacker-tube/)

由于对 YouTube 日益“劣化”的算法和低质量内容感到失望，作者创建了 **HackerTube**。这是一个自定义视频发现平台，仅展示由 Hacker News (HN) 社区推荐的视频。

利用 **Claude Opus 5.5** 和 **Claude Code** 桌面应用，作者在大约两小时内构建了该网站。开发过程几乎完全自动化：AI 爬取并过滤了 2007 年至 2026 年的 HN 评论，从中识别出涵盖 150 个主题的 6,454 个高质量视频。作者没有进行传统的工程开发，而是充当“编排者”，仅提供了 YouTube API 密钥、域名和 VPS。AI 处理了所有的编码、部署、安全加固及优化工作。

**HackerTube 的核心功能包括：**
*   **精选内容：** 一个经 HN 社区审核的视频库。
*   **隐私优先的推荐：** “为你推荐”建议在浏览器会话中本地生成，无需用户账号。
*   **减少诱导点击：** UI 采用视频中间帧作为缩略图，而非上传者提供的标题党封面。
*   **用户工具：** 提供键盘快捷键和开放的数据导出功能，方便用户通过 AI 代理创建自己的版本。

该项目凸显了软件开发领域的重大转变：先进的 AI 模型使个人能够通过对话而非手动编程，构建并部署复杂的数据驱动型应用。

---

## 3. 数学已经改变，我们也该有所行动。

**原文标题**: Mathematics has changed. Let's act like it

**原文链接**: [https://terrytao.wordpress.com/2026/11/01/mathematics-has-changed-lets-act-like-it/](https://terrytao.wordpress.com/2026/11/01/mathematics-has-changed-lets-act-like-it/)

以下是基于 Ben Eastaugh 和 Chris Sternal-Johnson 的文章《数学已然改变，让我们顺势而为》（Mathematics has changed. Let's act like it）所做的简洁摘要：

作者认为，验证数学知识的传统方法——人类同行评审——已不再适用于现代。随着数学证明变得日益冗长、专业且复杂，验证的“社会化过程”正趋于极限。

核心观点包括：

*   **复杂性危机：** 作者强调，一些现代证明规模宏大（跨越数篇论文，长达数千页），以至于没有任何一位数学家能完全掌握。他们以“有限单群分类”和托马斯·黑尔斯（Thomas Hales）对“开普勒猜想”的证明为例，说明传统同行评审在提供绝对确定性方面已显得力不从心。
*   **人类评审的局限性：** 在开普勒猜想的案例中，评审人员耗时多年研究证明过程，最终却只能得出“99% 确定”其正确性的结论。作者认为，这种程度的不确定性与数学所宣称的基础严谨性是相悖的。
*   **形式化验证：** 提出的解决方案是转向使用交互式定理证明器（如 Lean）进行**形式化**。通过将数学转化为计算机可读的代码，证明可以经过机械化验证，从而获得绝对的逻辑确定性。
*   **文化转变：** 作者呼吁数学界接纳这些数字工具，不应仅将其视为一种小众兴趣，而应将其作为该领域的新标准。他们认为，形式化能够促进更好的协作，构建可搜索的已验证数学库，并为未来的研究奠定更可靠的基础。

最后，文章断言，虽然数学真理的**本质**并未改变，但该领域的**规模**已经改变，数学家必须采用计算工具来维护这一学科的严谨性。

---

## 4. Nibnib：极速解压的图像压缩

**原文标题**: Nibnib: Image compression with extreme decompression speed

**原文链接**: [https://github.com/raphlinus/nibnib](https://github.com/raphlinus/nibnib)

**Nibnib** 是一种专为极速解压设计的专用图像压缩格式，特别针对 RP2350 等微控制器的 DVI 输出进行了优化。它的处理预算被严格限制在每像素约六个周期，非常适合需要高速图像渲染的低功耗设备。

**主要技术特性：**
*   **解码效率：** Nibnib 通过从单个 8 位输入字节中解码出两个 16 位 RGB 565 像素，实现了 4bpp（每像素位数）的压缩率。
*   **增量调色板机制：** 该格式的核心是使用一个包含 256 个条目的调色板。与存储绝对颜色的传统调色板不同，Nibnib 存储的是**增量值**。解码时，将前一个像素值翻倍并加上调色板中的 32 位增量，从而生成一对新像素。这种方法显著提升了柔和渐变的显示质量。
*   **非对称设计：** 虽然解码过程简单且确定，但编码是一个计算密集型的搜索过程。目前的编码器在像素对之间使用 Floyd-Steinberg 误差扩散算法以减少视觉伪影，并采用由结构化“增量立方体”与高斯随机值混合构成的调色板。

**现状与未来发展：**
该格式目前处于基础可用状态。文件结构极简，由图像尺寸、调色板和原始行数据组成。未来的改进目标是通过自适应调色板选择和更深层次的编码搜索来优化图像质量。由于该格式是由其解码器定义的，因此可以在不改变高速解码逻辑的情况下实现这些增强功能。

Nibnib 是开源的，采用 **Apache 2.0 和 MIT** 双重许可协议。

---

## 5. Copper – A minimal low-level programming language with OOP and generics

**原文标题**: Copper – A minimal low-level programming language with OOP and generics

**原文链接**: [https://tibleiz.net/copper/](https://tibleiz.net/copper/)

**Copper** 是一种极简的底层编程语言，旨在作为 C 语言的现代替代方案。其核心设计理念是**极简主义**，目标是使其足够简单且明确，以便单个开发者能够完全理解，同时保持足够强大的性能进行系统编程。

Copper 与 C 的主要区别包括：
*   **面向对象编程：** 支持类型继承和基于类的结构。
*   **现代易用性：** 拥有受 Ruby 启发的语法、泛型、多返回值和 Option 类型。
*   **简化的工具链：** 采用直观的导入系统，无需头文件，并支持乱序定义。
*   **性能与安全：** 提供快速编译、用于资源管理的延迟语句（deferred statements）和简单的迭代器，同时保持大多数构造的明确性。
*   **命名空间管理：** 通过保持定义的局部化来避免全局命名空间污染。

该语言专为需要底层控制权但追求现代语言可读性和功能集的开发者设计。Copper 采用 **BSD 许可证**发布，其生态系统包括标准库、完善的文档和编译器——所有这些在设计上都遵循相同的极简原则。

---

## 6. 提升 AFL++ 模糊测试效率的技巧

**原文标题**: Tips for more effective fuzz testing with AFL++

**原文链接**: [https://nullprogram.com/blog/2025/02/05/](https://nullprogram.com/blog/2025/02/05/)

本文针对 C 和 C++ 目标，提供了一套使用 AFL++ 优化模糊测试的全方位高级策略。作者结合对 1,000 多个项目的模糊测试经验，指出大多数软件中都存在未被发现的“浅层漏洞”，而通过更好的模糊测试技术可以揭示这些漏洞。

**主要建议包括：**

*   **激进的净化设置：** 始终使用 ASan 和 UBSan。作者建议强化 `ASAN_OPTIONS` 配置以检测“栈内存返回后使用”（stack-use-after-return）错误，并最大化 `max_malloc_fill_size`，以确保未初始化的内存缺陷不会被默认限制所掩盖。
*   **持久模式：** 使用 AFL++ 的持久模式（Persistent Mode）可实现数量级的速度提升。作者提供了一个模板，用于正确实现 `__AFL_LOOP` 并规避常见陷阱。
*   **直接包含源文件：** 与其使用复杂的构建配置，不如将 `.c` 文件直接包含进模糊测试驱动（harness）中。这使得测试内部 `static` 函数成为可能，并且更容易在每次运行间重置全局变量。
*   **严格隔离：** 确保每次测试迭代都是独立的。一个关键技巧是将**模糊测试缓冲区复制**到特定大小的内存块中（使用 `realloc`/`memcpy`），而不是直接测试 AFL++ 缓冲区；这能让 ASan 捕获到那些原本会被忽略的读取越界。
*   **内存文件描述符：** 对于需要文件路径的程序，使用 `memfd_create` 和 `/proc/self/fd/` 接口。这可以在不产生 SSD 损耗或临时文件管理开销的情况下，实现高速并行模糊测试。
*   **缩小缓冲区：** 手动缩小源代码中的大型固定缓冲区（例如，从 64KB 缩小到 16 字节），从而更快地触发边界情况和溢出。

通过优先考虑执行速度和灵敏的错误检测，这些技术能让开发者发现标准模糊测试配置所遗漏的缺陷。

---

## 7. 利用 JEPA 证明并改进柏拉图式表征假设

**原文标题**: Proving and improving the Platonic Representation Hypothesis with JEPAs

**原文链接**: [https://arxiv.org/abs/2610.39302](https://arxiv.org/abs/2610.39302)

Randall Balestriero 与 Yann LeCun 的这篇论文对“柏拉图表征假设”（Platonic Representation Hypothesis, PRH）进行了形式化阐述与推进。该理论认为，在不同模态（如文本和视觉）上训练的 AI 模型最终会收敛于一种单一且通用的现实表征。

作者提出了三大主要发现：

1. **柏拉图表征定理**：他们通过数学证明，表明在不同模态上训练的联合嵌入预测架构（JEPA）将学习到相同的表征（仅相差一个旋转变换）。只要训练数据由“优质视图”（即对同一底层场景的不同观测）组成，这一结论便成立。
2. **对大语言模型“劣质视图”的批判**：研究指出，下一个标记（next-token）预测本质上是一种使用“劣质视图”（即单一文档的连续片段）的 JEPA。这解释了为何传统语言模型需要极大的规模才能与视觉对齐，而 JEPA 实现对齐的效率要高得多。
3. **实证验证与效率**：通过对 9.4 亿张网络图像的大规模数据集进行测试，作者证明了“优质视图”的样本效率比下一个标记预测高出 42 倍。值得注意的是，一个仅有 1.09 亿参数的小型文本 JEPA 在与 DINOv2 等图像模型的对齐表现上，超越了参数量高达 720 亿的大型语言模型以及 CLIP 的文本编码器。

其实际意义非常重大：通过应用单一的旋转变换，独立训练的编码器在无需配对数据的情况下，即可转化为实用的图像描述生成器或零样本分类器。论文总结指出，构建通用的、柏拉图式的世界表征，其核心杠杆在于“优质视图”，而非单纯的规模。

---

## 8. 一位意大利农民在阁楼里发现了一些未知的种子，并将其种了下来。

**原文标题**: An Italian farmer found some unknown seeds in his attic and planted them

**原文链接**: [https://www.smithsonianmag.com/science-nature/italian-farmer-found-unknown-seeds-attic-with-nothing-lose-planted-them-result-biblical-180989644/](https://www.smithsonianmag.com/science-nature/italian-farmer-found-unknown-seeds-attic-with-nothing-lose-planted-them-result-biblical-180989644/)

生成摘要时出错

---

## 9. Bidirectional charging during grid outages

**原文标题**: Bidirectional charging during grid outages

**原文链接**: [https://www.jefftk.com/p/bidirectional-charging-during-grid-outages](https://www.jefftk.com/p/bidirectional-charging-during-grid-outages)

生成摘要时出错

---

## 10. Lenovo's 'encrypted' fingerprint USB is just an unencrypted SD card in a case

**原文标题**: Lenovo's 'encrypted' fingerprint USB is just an unencrypted SD card in a case

**原文链接**: [https://www.reddit.com/r/technology/comments/1xl2pr3/lenovos_encrypted_fingerprint_usb_drive_is_just/](https://www.reddit.com/r/technology/comments/1xl2pr3/lenovos_encrypted_fingerprint_usb_drive_is_just/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-11-01](output/hacker_news_summary_2026-11-01.md) |
| 2 | [2026-10-29](output/hacker_news_summary_2026-10-29.md) |
| 3 | [2026-10-30](output/hacker_news_summary_2026-10-30.md) |
| 4 | [2026-10-27](output/hacker_news_summary_2026-10-27.md) |
| 5 | [2026-10-28](output/hacker_news_summary_2026-10-28.md) |
| 6 | [2026-10-31](output/hacker_news_summary_2026-10-31.md) |
| 7 | [2026-10-26](output/hacker_news_summary_2026-10-26.md) |
| 8 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 9 | [2026-10-22](output/hacker_news_summary_2026-10-22.md) |
| 10 | [2026-10-25](output/hacker_news_summary_2026-10-25.md) |
| 11 | [2026-10-24](output/hacker_news_summary_2026-10-24.md) |
| 12 | [2026-10-23](output/hacker_news_summary_2026-10-23.md) |
| 13 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 14 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 15 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 16 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 17 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 18 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 19 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 20 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 21 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 22 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 23 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 24 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 25 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 26 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 27 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 28 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 29 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 30 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 31 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 32 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 33 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 34 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 35 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 36 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 37 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 38 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 39 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 40 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 41 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 42 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 43 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 44 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 45 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 46 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 47 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 48 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 49 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 50 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 51 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 52 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 53 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 54 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 55 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 56 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 57 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 58 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 59 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 60 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 61 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 62 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 63 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 64 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 65 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 66 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 67 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 68 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 69 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 70 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 71 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 72 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 73 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 74 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 75 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 76 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 77 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 78 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 79 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 80 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 81 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 82 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 83 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 84 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 85 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 86 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 87 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 88 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 89 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 90 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 91 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 92 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 93 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 94 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 95 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 96 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 97 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 98 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 99 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 100 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 101 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 102 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 103 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 104 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 105 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 106 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 107 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 108 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 109 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 110 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 111 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 112 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 113 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 114 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 115 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 116 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 117 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 118 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 119 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 120 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 121 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 122 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 123 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 124 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 125 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 126 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 127 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 128 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 129 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 130 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 131 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 132 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 133 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 134 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 135 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 136 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 137 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 138 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 139 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 140 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 141 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 142 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 143 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 144 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 145 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 146 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 147 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 148 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 149 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 150 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 151 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 152 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 153 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 154 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 155 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 156 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 157 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 158 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 159 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 160 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 161 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 162 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 163 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 164 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 165 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 166 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 167 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 168 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 169 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 170 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 171 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 172 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 173 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 174 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 175 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 176 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 177 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 178 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 179 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 180 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 181 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 182 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 183 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 184 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 185 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 186 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 187 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 188 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 189 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 190 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 191 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 192 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 193 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 194 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 195 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 196 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 197 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 198 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 199 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 200 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 201 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 202 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 203 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 204 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 205 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 206 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 207 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 208 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 209 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 210 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 211 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 212 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 213 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 214 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 215 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 216 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 217 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 218 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 219 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 220 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 221 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 222 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 223 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 224 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 225 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 226 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 227 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 228 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 229 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 230 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 231 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 232 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 233 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 234 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 235 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 236 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 237 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 238 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 239 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 240 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 241 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 242 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 243 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 244 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 245 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 246 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 247 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 248 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 249 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 250 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 251 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 252 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 253 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 254 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 255 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 256 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 257 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 258 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 259 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 260 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 261 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 262 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 263 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 264 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 265 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 266 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 267 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 268 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 269 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 270 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 271 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 272 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 273 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 274 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 275 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 276 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 277 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 278 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 279 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 280 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 281 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 282 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 283 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 284 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 285 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 286 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 287 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 288 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 289 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 290 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 291 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 292 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 293 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 294 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 295 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 296 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 297 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 298 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 299 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 300 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 301 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 302 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 303 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 304 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 305 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 306 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 307 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 308 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 309 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 310 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 311 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 312 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 313 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 314 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 315 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 316 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 317 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 318 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 319 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 320 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 321 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 322 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 323 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 324 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 325 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 326 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 327 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 328 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 329 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 330 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 331 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 332 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 333 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 334 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 335 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 336 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 337 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 338 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 339 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 340 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 341 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 342 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 343 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 344 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 345 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 346 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 347 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 348 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 349 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 350 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 351 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 352 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 353 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 354 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 355 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 356 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 357 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 358 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 359 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 360 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 361 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 362 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 363 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 364 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 365 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 366 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 367 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 368 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 369 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 370 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 371 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 372 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 373 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 374 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 375 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 376 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 377 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 378 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 379 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 380 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 381 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 382 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 383 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 384 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 385 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 386 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 387 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 388 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 389 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 390 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 391 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 392 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 393 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 394 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 395 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 396 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 397 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 398 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 399 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 400 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 401 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 402 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 403 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 404 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 405 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 406 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 407 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 408 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 409 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 410 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 411 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 412 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 413 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 414 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 415 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 416 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 417 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 418 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 419 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 420 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 421 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 422 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 423 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 424 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 425 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 426 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 427 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 428 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 429 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 430 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 431 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 432 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 433 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 434 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 435 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 436 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 437 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 438 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 439 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 440 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 441 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 442 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 443 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 444 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 445 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 446 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 447 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 448 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 449 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 450 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 451 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 452 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 453 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 454 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 455 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 456 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 457 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 458 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 459 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 460 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 461 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 462 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 463 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 464 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 465 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 466 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 467 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 468 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 469 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 470 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 471 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 472 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 473 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 474 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 475 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 476 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 477 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 478 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 479 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 480 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 481 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 482 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 483 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 484 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 485 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 486 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 487 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 488 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 489 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 490 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 491 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 492 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 493 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 494 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 495 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 496 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 497 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 498 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 499 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 500 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 501 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 502 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 503 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 504 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 505 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 506 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 507 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 508 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 509 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 510 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 511 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 512 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 513 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 514 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 515 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 516 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 517 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 518 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 519 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 520 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 521 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 522 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 523 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 524 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 525 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 526 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 527 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 528 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 529 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 530 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 531 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 532 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 533 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 534 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 535 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 536 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 537 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 538 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 539 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 540 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 541 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 542 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 543 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 544 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 545 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 546 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 547 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 548 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 549 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 550 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 551 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 552 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 553 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 554 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 555 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 556 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 557 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 558 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 559 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 560 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 561 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 562 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 563 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 564 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 565 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 566 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 567 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 568 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 569 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 570 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 571 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 572 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 573 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 574 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 575 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 576 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 577 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 578 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 579 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 580 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 581 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 582 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 583 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 584 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 585 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 586 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 587 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 588 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 589 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
