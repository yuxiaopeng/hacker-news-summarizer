# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-07-03.md)

*最后自动更新时间: 2025-07-03 17:51:08*
## 1. 介绍 tmux-rs

**原文标题**: Introducing tmux-rs

**原文链接**: [https://richardscollin.github.io/tmux-rs/](https://richardscollin.github.io/tmux-rs/)

Collin Richards 详述了他将 tmux 从 C 移植到 Rust 的项目，命名为 tmux-rs。他回顾了最初使用 C 到 Rust 的转译器 C2Rust 的尝试，尽管它能运行，但产生了无法维护的代码。随后，他转为手动翻译代码库，逐个函数进行翻译，并在每次翻译后确保编译通过。

文章描述了构建过程，重点介绍了从将 Rust 库链接到 C 二进制文件，转变为使用 `cc` crate 将 C 库链接到 Rust 二进制文件的转变。 他讨论了在翻译过程中遇到的两个有趣的 bug，一个是由隐式的 C 函数声明引起的，另一个是由 C 和 Rust 之间不匹配的结构体定义引起的。

Richards 详细阐述了如何在 Rust 中处理 C 特有的模式，例如原始指针、`goto` 语句（他使用带标签的代码块和循环重新实现了它）以及侵入式宏。他还介绍了使用 `lalrpop` crate 将 tmux 的自定义配置语言解析器从 Yacc 重写为 Rust 的经验，这使他能够摆脱 `cc` crate。

他总结说，虽然这个项目主要是一个爱好，但它提供了在底层编程、构建系统以及 C 和 Rust 的复杂性方面的宝贵经验。

---

## 2. 穷人的后端即服务 (BaaS)，类似于 Firebase/Supabase/Pocketbase

**原文标题**: Poor Man's Back End-as-a-Service (BaaS), Similar to Firebase/Supabase/Pocketbase

**原文链接**: [https://github.com/zserge/pennybase](https://github.com/zserge/pennybase)

Pennybase：轻量级 DIY 后端即服务 (BaaS) 替代方案，使用不到 1000 行 Go 代码，仅使用标准库构建，是 Firebase、Supabase 或 Pocketbase 的替代方案。它提供核心后端功能，如数据存储、REST API、身份验证、RBAC、通过 SSE 进行的实时更新、模式验证和模板渲染。

数据存储在 CSV 文件中，每个记录都有版本控制。`_schemas.csv` 中的简单模式定义了 JSON 字段和 CSV 列之间的映射。用户凭据和角色在 `_users.csv` 中管理，需要手动编辑以添加新用户。访问控制通过在 `_permissions.csv` 中定义的基于角色的权限来处理。

Pennybase 提供了一个 REST API 用于对资源进行 CRUD 操作，以及一个事件端点用于实时更新。通过 Basic Auth 和会话 Cookie 支持身份验证。它还可以提供静态资源并呈现具有用户身份验证、资源访问和授权检查的 HTML 模板。

可以使用单个钩子函数扩展功能，该函数在创建、更新和删除操作时触发，从而允许进行验证和数据修改。该项目欢迎专注于错误修复、测试和示例的贡献，旨在根据 MIT 许可证维护其小型、清晰且正确的代码库。

---

## 3. AV1@Scale：胶片颗粒合成，觉醒

**原文标题**: AV1@Scale: Film Grain Synthesis, The Awakening

**原文链接**: [https://netflixtechblog.com/av1-scale-film-grain-synthesis-the-awakening-ee09cfdff40b](https://netflixtechblog.com/av1-scale-film-grain-synthesis-the-awakening-ee09cfdff40b)

Netflix大规模部署AV1胶片颗粒合成技术

---

## 4. 用于科学搜索的人工智能

**原文标题**: AI for Scientific Search

**原文链接**: [https://arxiv.org/abs/2507.01903](https://arxiv.org/abs/2507.01903)

该arXiv预印本（arXiv:2507.01903）发表了一篇题为“AI4Research：人工智能在科学研究中的应用综述”的调查报告。该论文由陈启光和其他15位研究人员撰写，旨在解决人工智能在科学研究中的应用这一快速发展领域缺乏全面概述的问题。

该综述的动机是人工智能的最新进展，特别是像OpenAI-o1和DeepSeek-R1这样的大型语言模型，它们展示了适用于复杂研究任务的显著能力。作者旨在对AI4Research提供一个统一的视角，解决现有理解上的差距，并促进该领域的进一步发展。

该论文做出了三个关键贡献：第一，它引入了一个系统的分类法，用于对AI4Research中的五个主流任务进行分类。第二，它确定了关键的研究差距，重点关注自动化实验的严谨性和可扩展性以及人工智能在研究中的社会影响，突出了有希望的未来方向。第三，它汇编了大量的资源，包括与AI4Research相关的多学科应用、数据语料库和工具，旨在促进访问和激发创新突破。该论文旨在为研究社区提供宝贵的资源，提供对相关资源的快速访问，并促进人工智能在科学发现中的进一步发展。该论文归类于计算与语言（cs.CL）和人工智能（cs.AI）。

---

## 5. EBAF – 基于 eBPF 的广告防火墙

**原文标题**: EBAF – eBPF Based Ad Firewall

**原文链接**: [https://github.com/Kazedaa/eBAF](https://github.com/Kazedaa/eBAF)

eBAF (eBPF广告防火墙) 是一款开源的Spotify广告拦截器，它利用eBPF在内核级别屏蔽广告，旨在改善用户体验，并挑战Spotify“免费增值”模式中对用户和艺术家潜在的剥削。该工具认为用户以时间和耐心为“免费”层级付费，而艺术家收入过低，eBAF提供了一种退出该系统的方式。

eBAF的工作原理是检查网络数据包，阻止来自与广告服务器相关的IP地址黑名单中的数据包。它通过将域名解析为IP地址来动态更新该黑名单。它还提供一个用于监控的Web仪表板，并在网络接口级别运行，以实现高性能和最小的资源占用。

该工具通过curl脚本提供简单的安装方法，可以选择启用或禁用Spotify集成。还提供了针对各种Linux发行版的开发安装说明。使用说明展示了如何在特定或所有接口上运行eBAF，启动仪表板以及配置黑名单。本文还感谢了项目中使用的Spotify广告阻止列表的创建者。最后，它鼓励用户通过在GitHub上为该仓库点亮星星来支持该项目。

---

## 6. 在 FPGA 上并行化 SHA256 计算

**原文标题**: Parallelizing SHA256 Calculation on FPGA

**原文链接**: [https://www.controlpaths.com/2025/06/29/parallelizing_sha256-calculation-fpga/](https://www.controlpaths.com/2025/06/29/parallelizing_sha256-calculation-fpga/)

本文介绍了一种在FPGA上使用连接到 Raspberry Pi 5 的 Litefury 板实现的并行 SHA-256 哈希破解器的实现方法。作者改进了先前的 SHA-256 计算器设计，通过并行计算和实例化多个哈希核心来提高吞吐量。

主要改进包括：
*   将 K 矩阵移至 SHA 核心之外以实现共享访问，从而减少核心逻辑。
*   并行初始化 W 矩阵，消除了 AXI Stream 接口。

该系统包含由 `SHA256_manager` 模块管理的 `sha256_core_pif` 模块（优化的 SHA-256 核心），该模块协调各个核心并将它们的输出与目标哈希值进行比较。该应用程序尝试通过迭代哈希候选字符串来破解 SHA-256 哈希值。如果找到匹配项，则原始字符串和匹配核心的 ID 将被发送到主机。

该设计集成了 12 个 `sha256_core_pif` 模块，时钟速度为 62.5 MHz，受时序约束限制。在 Raspberry Pi 上运行的 Python 驱动程序通过 xDMA 驱动程序控制 FPGA，写入和读取 AXI 外设的寄存器映射。该驱动程序通过读取输出寄存器并添加获胜核心的 ID 来检索破解的密码。

文章最后展示了哈希破解器的实际应用，并强调了 FPGA 在密码学和网络安全领域日益增长的重要性。所有项目文件都可以在 GitHub 上找到。

---

## 7. 铜线比光纤快 (2017) [pdf]

**原文标题**: Copper is Faster than Fiber (2017) [pdf]

**原文链接**: [https://www.arista.com/assets/data/pdf/Copper-Faster-Than-Fiber-Brief.pdf](https://www.arista.com/assets/data/pdf/Copper-Faster-Than-Fiber-Brief.pdf)

很抱歉，我无法完成该请求。提供的文档看似是PDF文件，但内容大多经过编码，无法呈现任何可读文本，因此我无法总结文章。

---

## 8. 爱丽丝可微仙境历险记

**原文标题**: Alice's Adventures in a Differentiable Wonderland

**原文链接**: [https://arxiv.org/abs/2404.17625](https://arxiv.org/abs/2404.17625)

Simone Scardapane 撰写的 arXiv 论文，题为“可微仙境爱丽丝漫游记——第一卷：仙境之旅”，是对可微编程领域的入门介绍，通过爱丽丝漫游“可微仙境”的类比进行解释。它将神经网络定位为可微原语的组合，并强调学习如何编程以及与这些模型互动。

该论文侧重于提供一个直观且独立的介绍，内容包括使用自动微分优化函数，以及探索用于处理序列、图、文本和音频数据的常见神经网络设计。它重点介绍了关键的设计技巧，包括卷积块、注意力块和循环块。

作者旨在通过提供 PyTorch 和 JAX 的实际示例来弥合理论与代码之间的差距，最终使读者能够理解大型语言模型（LLMs）和多模态架构等高级模型。配套网站提供额外的章节。

该论文已修改过一次，最新版本于 2024 年 7 月 4 日提交。该论文被归类为机器学习 (cs.LG) 和人工智能 (cs.AI)。

---

## 9. 工具：代码即一切

**原文标题**: Tools: Code Is All You Need

**原文链接**: [https://lucumr.pocoo.org/2025/7/3/tools/](https://lucumr.pocoo.org/2025/7/3/tools/)

Armin Ronacher 在他的文章《工具：代码才是你需要的》中批评了模型上下文协议 (MCP)，认为它不如代码生成有效，尤其是在代理编码和大规模自动化方面。他发现 MCP 缺乏可组合性，过度依赖推理，并且需要过多的上下文，使其效率低于 gh CLI 等工具。

Ronacher 认为，对于自动化任务，即使是在特定领域，代码生成通常更胜一筹，因为它具有可组合性、可验证性，并且较少依赖持续的推理。他以将其博客从 reStructuredText 转换为 Markdown 为例，使用 LLM 生成代码用于 AST 转换和差异比较，由于其可审查的特性，他对这个过程充满信心。

他强调了自动化重复性任务的重要性，并提倡使用代码来确保准确性，减少对验证的需求，相比之下，纯粹基于推理的方法则不然。

Ronacher 承认 MCP 的潜力，但认为其当前形式是扩展自动化的“死胡同”。他建议探索更好的抽象、沙箱和 API，以便在批量代码执行后进行“扇出/扇入”推理。他还建议生成带有上下文的代码，以便非程序员也能理解脚本的功能。

最终，Ronacher 鼓励探索 MCP 之外的方法，并利用 LLM 的强大功能来编写代码，他认为这在自动化任务方面提供了更多的控制、可验证性和可扩展性。

---

## 10. 行为局部性 (2020)

**原文标题**: Locality of Behaviour (2020)

**原文链接**: [https://htmx.org/essays/locality-of-behaviour/](https://htmx.org/essays/locality-of-behaviour/)

Carson Gross 的“行为局部性（LoB）”认为，当仅通过检查一个代码单元就能清楚地了解其行为时，代码的可维护性就会得到增强。这一原则受到 Richard Gabriel 对局部性的强调的启发，优先考虑使代码行为一目了然。

该文章对比了 htmx 和 jQuery AJAX 请求来阐释 LoB。 Htmx 将按钮的行为直接定义在元素内部，展现了良好的 LoB。 相反，jQuery 将行为分散在各个文件中，需要更广泛的知识才能理解按钮的功能，这违反了 LoB。

Gross 澄清说，LoB 不是关于内联实现细节，而是关于内联行为的*调用*或*声明*。 函数就是一个很好的例子：它们抽象了实现，但被清晰地调用。

该文章承认 LoB 可能与其他原则（如 DRY（不要重复自己）和 SoC（关注点分离））相冲突。 例如，DRY 可能导致行为被定义在远离受影响代码单元的地方，而 SoC，特别是 HTML、CSS 和 JavaScript 的分离，可能会模糊行为变更的来源。 逐渐流行的内联样式表明在某些情况下人们正在逐渐放弃严格的 SoC。

结论强调 LoB 是一种主观原则，需要与其他设计考量因素进行仔细权衡。 在可行的情况下，优先考虑 LoB 可以显著提高软件的可维护性、质量和可持续性。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 2 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 3 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 4 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 5 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 6 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 7 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 8 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 9 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 10 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 11 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 12 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 13 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 14 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 15 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 16 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 17 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 18 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 19 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 20 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 21 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 22 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 23 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 24 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 25 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 26 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 27 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 28 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 29 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 30 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 31 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 32 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 33 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 34 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 35 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 36 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 37 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 38 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 39 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 40 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 41 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 42 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 43 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 44 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 45 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 46 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 47 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 48 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 49 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 50 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 51 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 52 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 53 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 54 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 55 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 56 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 57 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 58 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 59 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 60 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 61 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 62 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 63 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 64 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 65 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 66 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 67 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 68 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 69 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 70 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 71 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 72 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 73 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 74 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 75 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 76 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 77 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 78 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 79 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 80 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 81 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 82 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 83 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 84 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 85 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 86 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 87 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 88 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 89 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 90 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 91 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 92 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 93 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 94 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 95 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 96 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 97 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 98 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 99 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 100 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 101 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 102 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 103 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 104 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 105 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 106 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
