# Hacker News 热门文章摘要 (2025-05-16)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Show HN：受 Node-RED 启发的 Erlang 可视化流程编程

**原文标题**: Show HN: Visual flow-based programming for Erlang, inspired by Node-RED

**原文链接**: [https://github.com/gorenje/erlang-red](https://github.com/gorenje/erlang-red)

Erlang-RED 是一个实验性项目，旨在用 Erlang 等效后端替代 Node-RED 的 NodeJS 后端，将基于可视流程的编程引入 Erlang 的消息传递和并发能力。其目标是将 Node-RED 的易用性与 Erlang 的性能和并发性相结合，但同时承认由于 Javascript 函数节点限制，完全 100% 兼容现有 Node-RED 流程的可能性不大。

该项目专注于流程驱动开发，并使用大量的测试流程来确保节点功能与现有 Node-RED 行为相匹配。由于用于测试和功能的节点相互关联，因此架构非常复杂。

一系列 Node-RED 节点得到了部分或完全的支持，其功能级别各不相同，包括 HTTP、MQTT、文件处理、逻辑和模板节点。目前不支持上下文。Elixir 代码可以集成到节点开发中，但核心逻辑首选 Erlang 语法。

该项目强调在 Node-RED 编辑器中进行可视化单元测试，使用“Assert Failed”和断言节点来验证流程行为。这些测试旨在确保 Erlang 后端正确实现节点功能。

该项目欢迎以 Erlang 代码、Node-RED 测试流程或 Elixir 代码（在指定存储库中）的形式提供的贡献。开发遵循持续集成方法，频繁推送到主分支。 提供 Docker、Fly.io 和 Heroku 部署选项。

---

## 2. X X^t 可以更快

**原文标题**: X X^t can be faster

**原文链接**: [https://arxiv.org/abs/2505.09814](https://arxiv.org/abs/2505.09814)

这篇题为“XX^t 可以更快”的arXiv预印本介绍了一种新的算法RXTX，用于计算矩阵与其转置的乘积 (XX^t)。该论文由Dmitry Rybin、Yushun Zhang和Zhi-Quan Luo撰写，声称与最先进的方法相比，RXTX在所需的乘法和加法次数上减少了5%。 这使得即使对于相对较小的矩阵尺寸也能实现加速。

作者强调，RXTX算法是通过基于机器学习的搜索方法和组合优化技术的结合发现的。该论文被归类于数据结构与算法 (cs.DS) 类别下，并额外分类于人工智能 (cs.AI)、机器学习 (cs.LG) 和符号计算 (cs.SC) 类别。它提供了访问论文的PDF和TeX源代码的链接。提交历史记录表明该论文于2025年5月14日提交。该论文还包括相关研究和书目工具的链接。

---

## 3. Codex研究预览

**原文标题**: A Research Preview of Codex

**原文链接**: [https://openai.com/index/introducing-codex/](https://openai.com/index/introducing-codex/)

以下是基于所提供URL的OpenAI Codex文章的摘要：

OpenAI发布的《Introducing Codex》文章宣布了Codex的首次发布，Codex是一种将自然语言翻译成编程代码的新型AI模型。Codex被描述为GPT-3的后代，但经过专门训练，使用了公开的源代码数据集，包括来自5400万个GitHub存储库的代码。这种专门的训练使Codex能够擅长理解和生成代码，尤其是在Python中，但也在其他语言中，如JavaScript、Go、PHP、Ruby、Swift、TypeScript、SQL，甚至Shell。

文章强调了Codex的能力不仅仅是简单的代码补全。它可以解释用简单英语编写的高级指令，并将它们翻译成可执行代码。这使得开发人员能够通过用自然语言表达他们的意图，而不是手动编写每一行代码，从而更快更高效地编写代码。它还展示了非程序员创建软件或自动化任务的潜力。

文章强调，Codex最初以私有测试版API的形式发布给选定的开发人员，以收集反馈并改进模型。这种受控的发布将使OpenAI能够了解Codex在实际用例中的优势和劣势，并解决潜在的安全问题。

文章最后表达了OpenAI对Codex的愿景，即降低编程的入门门槛，并赋能任何人创建软件。最终目标是使软件开发对专业开发人员和编程经验有限的个人都更易于访问和高效。

---

## 4. 展示HN：Rv，R语言的包管理器

**原文标题**: Show HN: Rv, a Package Manager for R

**原文链接**: [https://github.com/A2-ai/rv](https://github.com/A2-ai/rv)

Rv：可复现、快速且声明式的R包管理器。Rv是一个新的R包管理器，旨在实现可复现、快速且声明式的包管理。它仍在开发中，提供了一种配置驱动的方法，使用配置文件（可能是`rproject.toml`）来定义所需的项目状态，包括R版本、仓库和依赖项。主要命令有`rv plan`（预览更改）和`rv sync`（同步库、锁定文件和配置文件）。

配置文件允许指定仓库（带有别名和URL）和依赖项（带有安装建议包等选项）。`rv sync`会根据配置安装指定的包及其依赖项。有示例项目展示了更多配置。

安装和使用说明在单独的文档中提供。

要为Rv的开发做出贡献，需要Rust，Just是可选的。可以使用`just run <args>`或`cargo run`构建项目。可以使用`just install`或`cargo install`将其安装为二进制文件。可以使用`just test`或`cargo test`运行单元测试。快照测试需要R版本4.4.x。

---

## 5. 自由线程Python元年

**原文标题**: The first year of free-threaded Python

**原文链接**: [https://labs.quansight.org/blog/free-threaded-one-year-recap](https://labs.quansight.org/blog/free-threaded-one-year-recap)

本文总结了支持自由线程Python的第一年工作，重点介绍了Quansight和Meta为实现其实验性使用所做的工作。自由线程Python旨在通过移除全局解释器锁（GIL）来释放现代多核CPU和GPU的全部潜力，该锁阻碍了标准构建中的并行扩展。

这种转变需要大量工作，因为许多带有编译代码的Python包需要进行审计和修改，以确保线程安全，尤其是在使用全局状态方面。主要成就包括对打包工具、绑定生成器以及NumPy、SciPy和pandas等基础PyData包的贡献。CPython核心也取得了重大改进，包括warnings模块、asyncio和ctypes中的线程安全，以及垃圾收集器和自适应专门化解释器的性能增强。

虽然最初生态系统因自由线程构建而中断，但在修复构建问题方面已取得重大进展。作者强调需要更多的实际测试，以识别性能瓶颈和线程安全问题。在支持维护资源有限的大型遗留软件包方面仍然存在挑战。作者鼓励社区通过贡献指南、专门的Discord频道以及PyCon 2025上的演示来参与。作者认为自由线程Python是未来，并对其改善大量开发者性能的潜力持乐观态度。

---

## 6. 铸造厂（YC F24）招聘 – 创始工程师（机器学习 × 软件工程师）

**原文标题**: Foundry (YC F24) Is Hiring – Founding Engineer (ML × SWE)

**原文链接**: [https://www.ycombinator.com/companies/foundry/jobs/uwi8b6I-founding-engineer-ml-x-swe](https://www.ycombinator.com/companies/foundry/jobs/uwi8b6I-founding-engineer-ml-x-swe)

Foundry (YC F24) 招聘创始工程师 (机器学习 × 软件工程)，构建浏览器代理的基础设施，超越简单的 GPT 封装。他们的目标是创建一个“世界模型”，以可靠地自动化基于浏览器的 Workflow，这些 Workflow 对于现有的 AI 系统来说过于脆弱。该公司正在构建核心 AI 技术栈，包括超真实的 Web 模拟、全面的标注框架、可靠的基准以及强大的 RL 训练环境。

Foundry 寻求一位具有扎实软件工程技能（Python、TypeScript）和机器学习经验（训练模型、构建基础设施、运行实验）的工程师。该职位涉及构建浏览器代理 Gym，并在生产环境中解决困难的机器学习问题。 拥有 RL 代理、浏览器自动化 (Puppeteer、Playwright) 或评估工具经验者优先。

公司提供早期股权、有竞争力的薪酬以及巨大的发展前景。该职位的优势在于有机会构建其他人以后将依赖的核心机器学习基础设施。

Foundry 正在构建一个用于 Web 代理评估和训练的端到端平台，专注于确定性 Web 模拟、实时 Web 评估、自动标注和标记以及 RL 驱动的代理优化。 这使团队能够为真实环境构建更可靠的 Web 代理。 创始人来自 Scale AI 和 Meta。

---

## 7. 确保研究记录的准确性

**原文标题**: Assuring an Accurate Research Record

**原文链接**: [https://economics.mit.edu/news/assuring-accurate-research-record](https://economics.mit.edu/news/assuring-accurate-research-record)

麻省理工学院公开回应关于一篇预印本论文诚信问题的关切，该论文题为“人工智能、科学发现和产品创新”，最初于2024年11月发表在arXiv上。在收到指控并进行内部审查后，麻省理工学院已要求arXiv和《经济学季刊》撤回该论文。

纪律委员会（COD）告知arXiv，麻省理工学院“对论文中数据的来源、可靠性或有效性没有信心，并且对研究的真实性没有信心”，并指出该论文的存在可能违反该平台的行为准则。尽管麻省理工学院已指示作者（一位前博士生）要求撤回论文，但作者并未采取行动，因此麻省理工学院直接提出了撤回请求。

论文中致谢的Daron Acemoglu教授和David Autor教授也发表声明，表达了类似的担忧。他们明确表示，“对数据的来源、可靠性或有效性以及研究的真实性没有信心”。他们公开表达担忧是因为该论文虽然是预印本，但正在影响关于人工智能对科学影响的讨论，他们认为不应依赖其研究结果。

麻省理工学院强调其对研究诚信的承诺，并强调已制定政策和流程来解决此类问题。该作者已不再隶属于麻省理工学院。采取这一行动是为了确保准确的研究记录并减轻潜在不当行为的影响。

---

## 8. 解释风帆时代英国海军的霸主地位

**原文标题**: Explaining British Naval Dominance During the Age of Sail

**原文链接**: [https://www.lesswrong.com/posts/YE4XsvSFJiZkWFtFE/explaining-british-naval-dominance-during-the-age-of-sail](https://www.lesswrong.com/posts/YE4XsvSFJiZkWFtFE/explaining-british-naval-dominance-during-the-age-of-sail)

本文从经济学的角度，以监测和激励舰长的挑战为重点，解释了英国在风帆时代（1670-1827年）的海军霸权。尽管没有拥有优越的技术（法国船只可能更好），但英国海军的表现始终优于其竞争对手，其证据是伤亡率显著降低，并且在捕获或摧毁敌舰方面取得了更大的成功。

作者认为，由于海洋的广阔、通讯的缓慢以及机遇（天气）的作用，监测海军舰长存在固有的困难，导致激励机制错位。舰长们优先考虑捕获商船以获取个人利润，有时会逃避战斗。

为了解决这个问题，英国海军实施了几项机制来鼓励战斗：慷慨的补偿，包括奖金和带有半薪的“效率工资”制度；基于资历的晋升保障，以阻止逃避；诸如“战列线”队形和占据上风等战术，从而加强了对舰长行为的监控。中尉和航海长保留了详细的航海日志，作为对舰长的制约，并且《战争条约》规定必须与规模相似的敌舰交战，对未能尽力而为者处以严厉的惩罚，包括死刑。

对这些规则的严厉执行，以海军上将约翰·宾的处决为例，表明英国海军认真对待逃避问题。19世纪蒸汽船的引入使得这些机制变得过时，因为监控变得更容易，并且引入了《海军纪律法》，从而结束了英国风帆海军霸权的时代。

---

## 9. Show HN：SQL-tString：Python 中的 t-string SQL 构建器

**原文标题**: Show HN: SQL-tString a t-string SQL builder in Python

**原文链接**: [https://github.com/pgjones/sql-tstring](https://github.com/pgjones/sql-tstring)

SQL-tString 是一个 Python 库，它允许使用 t-strings（Python 3.14 引入）安全且方便地构建 SQL 查询。它通过将 t-string 中的变量转换为 SQL 占位符来防止 SQL 注入。

主要特性包括：

*   **安全参数化：** `{}` 中的变量会自动转换为占位符，防止注入漏洞。
*   **上下文验证：** `sql_context` 允许定义允许的列名和表名，如果 t-string 包含无效标识符，则会引发错误。
*   **条件查询修改：** `Absent` 值会从查询中删除参数，适用于可选更新。`IsNull` 和 `IsNotNull` 能够正确处理 `NULL` 比较。
*   **方言支持：** 支持 `qmark` (默认) 和 `$`/`asyncpg` 参数样式。
*   **兼容 Pre-Python 3.14：** 可以通过将 `locals()` 字典作为第二个参数传递给 `sql()` 在 Python 3.12 和 3.13 中使用。

本质上，SQL-tString 简化了 SQL 查询的创建，增强了安全性，并通过条件逻辑和方言支持提供了灵活性。

---

## 10. 塔防：缓存控制

**原文标题**: Tower Defense: Cache Control

**原文链接**: [https://www.jasonthorsness.com/26](https://www.jasonthorsness.com/26)

Jason Thorsness 的文章《塔防：缓存控制》探讨了通过缓存策略来防御网站免受高流量冲击，同时最小化成本。文章提出了三个难度级别，分别代表不同类型的网站及其缓存需求。

**简单（主要为静态网站）：** 利用内容哈希资源和 CDN。 内容哈希确保浏览器和 CDN 缓存静态文件，而无需担心过时问题。 CDN 将资源缓存在更靠近用户的全球各地，使用 "Etag" 标头通过 "304 Not Modified" 响应进行高效更新，从而最大限度地减少延迟和源服务器负载。 动态部分在客户端处理，以保留静态缓存的优势。

**中等（数据驱动的动态网站）：** 采用短期缓存控制标头，如 `stale-while-revalidate` 用于 CDN 缓存，在后台异步刷新内容的同时，提供陈旧内容，保持低延迟。 后端缓存至关重要，使用内存缓存来存储频繁访问的数据，使用单例模式来合并相同的请求，并使用磁盘缓存 (SQLite) 进行持久、大容量存储，并根据内容年龄设置过期函数。

**困难（经过身份验证的每个用户网站）：** 由于个性化内容，缓存变得更具挑战性。 该策略包括隔离和缓存非每用户内容（如静态站点），并使用浏览器缓存和服务器端（源）每用户缓存，以及之前提到的内存和磁盘缓存，以及单例模式。 客户端计算也有助于减少对服务器的依赖。

结论强调了缓存对于性能和成本管理的重要性，尤其是在使用计量 API 和无服务器托管的情况下。 有效的缓存架构可以通过仔细的缓存策略来扩展有限的资源，参考历史数据，并以更少的资源实现更好的负载处理。

---

## 11. Rust 编译器错误的演变

**原文标题**: Evolution of Rust Compiler Errors

**原文链接**: [https://kobzol.github.io/rust/rustc/2025/05/16/evolution-of-rustc-errors.html](https://kobzol.github.io/rust/rustc/2025/05/16/evolution-of-rustc-errors.html)

本文探讨了 Rust 编译器错误信息自 Rust 1.0.0 以来的演变，强调了使其异常有用的持续努力和设计。作者编写了一个脚本，下载并针对一组包含错误的小程序运行每个稳定的 Rust 版本，并捕获生成的编译器输出。

主要结论包括：

*   Rust 的错误信息一开始就很好，并且随着时间的推移只会变得更好。
*   数字错误代码在 Rust 1.2.0 中引入，彩色错误信息在 Rust 1.26.0 中引入。
*   “rustc --explain”提示已在 Rust 1.26.0 中添加。
*   作者注意到不同版本的错误信息中存在细微的不一致或反复变化。
*   错误跨度也得到了改进。
*   作者强调，这些高质量的错误信息并非自动产生，而是众多贡献者付出巨大努力的结果。

本文强调了编译器背后以人为本的开发过程，突出了设计、实施、审查和测试对出色错误报告的贡献。作者鼓励读者检查提供的脚本并分享他们最喜欢的 Rust 编译器错误信息。

---

## 12. 生命与死亡的深刻化学转化

**原文标题**: Transformer: The Deep Chemistry of Life and Death

**原文链接**: [https://nick-lane.net/books/transformer-the-deep-chemistry-of-life-and-death/](https://nick-lane.net/books/transformer-the-deep-chemistry-of-life-and-death/)

尼克·莱恩《转化：生与死的深层化学》一书深入探讨了区分活细胞与非生物物质的根本问题，挑战了将遗传学视为生命唯一驱动力的传统观点。莱恩认为，一个反应循环，特别是克雷布斯循环，是理解生物学深层连贯性的关键。这个循环将无机分子转化为生命的基石，然后再转化回去，它将生命的不同方面联系起来，从第一批光合细菌到人类意识以及死亡的必然性。

这本书探讨了这种化学现象如何成为生命本身的根本，将生命的出现与个体之间的细微差异联系起来。它被许多作者誉为里程碑式的作品，通过能量流动、通量和变化的视角，改变了我们对生命的理解，将化学呈现为一种鲜活的力量。莱恩的作品因其雄心勃勃的范围、引人入胜的风格、科学细节以及对生命生物物理学发人深省的见解而备受赞誉，为地球上的生命提供了一个新的视角。该书可通过各大书店购买。

---

## 13. Material 3 表现力

**原文标题**: Material 3 Expressive

**原文链接**: [https://design.google/library/expressive-material-design-google-research](https://design.google/library/expressive-material-design-google-research)

Material 3 Expressive是谷歌基于研究的Material Design的演进，旨在实现更具情感和以用户为中心的UX。它源于对Google应用感觉过于相似和乏味的观察，专注于利用颜色、形状、大小、动效和包含关系来激发情感和提升可用性。

涉及全球超过18,000名参与者的眼动追踪、调查、可用性测试和实验等大量研究证实，人们，尤其是年轻群体，更喜欢富有表现力的设计。这些设计被认为更“充满活力”、“情感丰富”、“富有创意”和“友好”。

重要的是，富有表现力的设计不仅仅是美学上的改进；它还能提升用户体验。测试表明，M3 Expressive设计中的关键UI元素能被更快地发现，从而更快地完成任务。它还为年龄较大的用户创造了公平的环境，消除了与年龄相关的可用性差异。

然而，情境至关重要。文章强调优先考虑功能并遵守可访问性标准。为了视觉效果而打破既定的UI模式可能会对可用性产生负面影响。鼓励设计师在Figma中使用更新后的Material 3设计工具包进行实验，根据用户旅程定制UI，并根据研究不断迭代，以在新鲜感和熟悉度之间取得平衡。虽然充满活力、富有表现力的设计受到了广泛欢迎，但仍有相当一部分用户更喜欢更平静、更柔和的版本。始终从用户的需求出发。文章强调了不要为了情感而牺牲清晰度的重要性。

---

## 14. 科学网络

**原文标题**: Sci-Net

**原文链接**: [https://sci-hub.se/sci-net](https://sci-hub.se/sci-net)

Sci-Net：一个促进科研论文共享的新型社交网络平台，旨在弥补 Sci-Hub 数据库暂停更新所造成的空白。与 Sci-Hub 的自动化系统不同，Sci-Net 允许用户请求和上传论文，从而促进了一种协同获取研究成果的方式。

该平台拥有用户友好的界面，用户可以通过 DOI 请求论文。 Sci-Net 在允许用户创建请求之前，会检查开放获取可用性和 Sci-Hub 是否已收录。 一项关键功能是上传 PDF 的能力，即使带有水印，Sci-Net 也可以将其移除以保护上传者的匿名性。上传的文章可以通过专门的 Sci-Net URL 公开访问。

Sci-Net 的一个独特之处在于它使用“Sci-Hub meme 币”来激励知识共享。 请求者可以为上传者指定代币奖励，经验证上传论文后即可转账。 虽然注册需要持有最少数量的代币（1000 个代币），但这被定义为一种象征性的入门费，远小于出版商的付费墙。

重要的是，与传统出版商不同，Sci-Net 将付款直接支付给其他研究人员。 此外，只有在上传时才需要支付一次费用，之后该文章将对所有人免费，包括非注册用户。 这种模式直接促进了公共领域知识的增长。 Sci-Net 旨在促进开放知识，并通过增加 Sci-Hub 代币的价值来间接支持 Sci-Hub。 尽管对于加密货币新手来说，获取这些代币可能具有挑战性，但该平台被认为是研究人员促进知识开放获取的关键工具。

---

## 15. 地面控制中心呼叫特里尔少校

**原文标题**: Ground control to Major Trial

**原文链接**: [https://virtualize.sh/blog/ground-control-to-major-trial/](https://virtualize.sh/blog/ground-control-to-major-trial/)

Vates揭露一家年收入1.3亿美元的半官方航天公司滥用Xen Orchestra免费试用十年

---

## 16. moricons.dll 图标最初用于哪些 MS-DOS 程序？

**原文标题**: What were the MS-DOS programs that the moricons.dll icons were intended for?

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20250507-00/?p=111157](https://devblogs.microsoft.com/oldnewthing/20250507-00/?p=111157)

本文探讨了Windows 3.1的`moricons.dll`文件中存储的图标的用途。它提供了一个全面的列表，列出了这些图标旨在代表的Windows环境中的程序。这些图标根据`APPS.INF`文件中的信息映射到特定的可执行文件。

该列表展示了各种MS-DOS应用程序，包括编译器（Microsoft Basic、C、Quick C），飞行模拟器（Flight Simulator 3.0、4.0），MS-DOS和Microsoft应用程序的学习资源（Works、Word），数据库程序（Paradox、Reflex），通信工具（Procomm Plus、Crosstalk），实用程序（OPTune、Q-DOS），电子表格和办公套件（Lotus 1-2-3、Microsoft Works、WordPerfect Office），图形应用程序（PC Paintbrush、Harvard Graphics）和编程环境（Turbo Pascal、Borland C++ IDE）。此外，该列表还包括多个FTP实用程序，表明即使在那个时代也存在网络应用程序。

本文是对MS-DOS时代多样化软件环境的怀旧回顾，突出了许多现已过时的应用程序，这些应用程序曾经是用户必不可少的工具。对于任何对Windows历史以及塑造早期PC计算的应用程序感兴趣的人来说，它都是一个有用的资源。

---

## 17. 最快的Postgres插入方法

**原文标题**: The fastest Postgres inserts

**原文链接**: [https://docs.hatchet.run/blog/fastest-postgres-inserts](https://docs.hatchet.run/blog/fastest-postgres-inserts)

优化Postgres插入性能：从应用侧入手

本文详细介绍了如何优化Postgres插入性能，重点在于应用侧的实用调整。作者首先进行了一个简单的单连接插入测试，达到约2千次写入/秒，然后发现网络延迟是一个重要的瓶颈。

讨论的关键优化包括：

1.  **降低网络延迟：** 尽量缩短应用程序和数据库之间的距离。
2.  **利用连接池：** 重用连接进行并行写入，最初可提高吞吐量。
3.  **避免过度连接：** 认识到过多的连接会引入开销（CPU、锁、I/O），从而降低性能增益。“连接风暴”会使轻量级锁管理器饱和。
4.  **采用批量插入：** 将行分组到单个查询中以减少查询开销，从而使吞吐量提高10倍以上。使用内存缓冲区实现。
5.  **使用COPY…FROM：** 仅写入数据时，利用COPY命令可提供明显更好的性能，这归功于Postgres内部优化（在本测试案例中达到6.3万次写入/秒）。
6.  **优化批量大小：** 找到最佳批量大小，以平衡吞吐量和延迟，避免过大的批量减慢I/O速度。

作者证明，通过这些优化，吞吐量从2千次写入/秒增加到9.2万次写入/秒。在优化吞吐量的同时，监控延迟也很重要。文章还建议继续关注第二部分，其中将涵盖更高级的优化技术，例如处理外键、UNNEST、未记录表和更新插入数据。

---

## 18. Ollama 多模态模型新引擎

**原文标题**: Ollama's new engine for multimodal models

**原文链接**: [https://ollama.com/blog/multimodal-models](https://ollama.com/blog/multimodal-models)

Ollama 发布新型引擎，支持多模态模型

关键改进包括：

*   **多模态模型支持：** Ollama 现在支持 Llama 4、Gemma 3、Qwen 2.5 VL 和 Mistral Small 3.1 等模型，用于视觉和通用理解。
*   **模型模块化：** 每个模型都是独立的，简化了集成，并减少了模型创建和更新过程中的错误。
*   **准确性增强：** 该引擎通过管理 token 大小以及在模型处理期间使用元数据来管理位置信息，从而确保准确处理大型图像。
*   **内存管理：** 图像缓存和 KV 缓存优化提高了性能，并且与硬件合作伙伴的密切合作确保了基于设备元数据的优化内存使用。
*   **注意力层优化：** 针对特定模型实现了特定的注意力机制（如滑动窗口和分块注意力），以获得最佳性能。
*   **未来计划：** Ollama 旨在未来支持更长的上下文大小、推理能力、带流式响应的工具调用以及计算机利用。

新型引擎解决了仅依赖 ggml/llama.cpp 进行多模态支持的不足，允许 Ollama 的合作伙伴直接为 GGML 张量库做出贡献。最终，它有望为多模态模型提供更好的本地推理，并为扩展功能奠定基础。

---

## 19. Show HN: Workflow Use – 确定性的、自愈的浏览器自动化 (RPA 2.0)

**原文标题**: Show HN: Workflow Use – Deterministic, self-healing browser automation (RPA 2.0)

**原文链接**: [https://github.com/browser-use/workflow-use](https://github.com/browser-use/workflow-use)

Workflow Use 被认为是“RPA 2.0”解决方案，用于确定性、自愈式浏览器自动化。其核心思想是录制一次浏览器工作流程，然后无限期地可靠地重放它。它旨在通过将录制转换为结构化的、可执行的工作流程来改进传统RPA，这些工作流程能够自动提取变量并智能地过滤噪声，从而无需进行大量的提示。如果某个步骤失败，它会智能地尝试解决，如果无法解决，则会使用Browser Use（推测是同一开发者开发的另一个工具）作为备用方案。

该项目目前处于早期开发阶段，不建议用于生产环境。主要功能包括录制重用、消除重复提示、自动变量提取、智能噪声过滤以及企业可扩展性考虑。项目路线图侧重于改进LLM回退、实施自愈能力、增强LLM步骤支持、启用步骤间数据传递、将工作流程公开为MCP工具以及利用Browser Use进行工作流程创建。还计划改进CLI、扩展程序、步骤编辑器和代理，更广泛的愿景是完全自动化任务，无需人工干预。本质上，只需向计算机演示一次，它就会永远自动且可靠地执行。

---

## 20. 可怕的德语 (1880)

**原文标题**: The Awful German Language (1880)

**原文链接**: [https://faculty.georgetown.edu/jod/texts/twain.german.html](https://faculty.georgetown.edu/jod/texts/twain.german.html)

马克·吐温的《可怕的德语》是一篇幽默讽刺的文章，详细描述了他学习德语复杂性时所遇到的困难。吐温认为德语不合逻辑、前后矛盾，且学习起来毫无必要地困难。

他强调了语法规则的随意性，并指出大量例外使任何掌握感都无效，令人沮丧。他嘲笑“格”，尤其是像“wegen”这样的介词如何出乎意料地将名词转变为属格，而不管逻辑如何。

吐温还讽刺了德国报纸上复杂迂回的句子结构，其特点是冗长、多层次的句子，充斥着括号短语和复合词，最终将动词置于句子开头很远的地方。他批判了“可分离动词”，其中动词部分被分离并放置在句子的两端，甚至跨越章节。

此外，吐温幽默地探讨了像“sie”这样的人称代词的歧义，以及形容词根据性别、数量和格进行的大量变格。他嘲笑名词的任意性别分配，认为萝卜是阴性而年轻女士是中性是荒谬的。总而言之，吐温利用夸张和诙谐的观察来表达他对德语的明显荒谬和不必要复杂性的恼火。

---

## 21. 超越文本：按需生成用户界面，打造更佳对话体验

**原文标题**: Beyond Text: On-Demand UI Generation for Better Conversational Experiences

**原文链接**: [https://blog.fka.dev/blog/2025-05-16-beyond-text-only-ai-on-demand-ui-generation-for-better-conversational-experiences/](https://blog.fka.dev/blog/2025-05-16-beyond-text-only-ai-on-demand-ui-generation-for-better-conversational-experiences/)

本文探讨了一种通过使大型语言模型 (LLM) 能够按需动态生成用户界面 (UI) 组件来改善对话式 AI 体验的新方法。它解决了纯文本 AI 交互的局限性，例如认知负荷、模糊性和可访问性障碍，尤其是在企业和客户服务场景中。

所提出的解决方案允许 AI 根据用户请求创建上下文相关的 UI 元素，如表单、按钮、表格和复杂复合组件。这弥合了自然语言对话和结构化输入之间的差距，从而提供更高效和用户友好的体验。

本文详细介绍了 LLM-UI 生成的过程，包括请求解释、组件选择、JSON 规范生成、渲染和交互处理。它还讨论了将此方法与 MCP（元宇宙通信协议）服务集成的好处，从而标准化通信并增强复杂功能的可访问性。

文章提供了 UI 组件类型的具体示例，包括表单、选择组件和数据可视化组件，以及 JSON 示例。一个来自航运公司的真实案例说明了该原型在实际中的应用。

文章最后概述了实施注意事项，包括系统提示和客户端渲染，并阐述了该技术的挑战和未来发展方向，强调了潜在的研究领域，如自动化 UI 测试、个性化界面和增强的 MCP 集成。作者还为开发者提出了开始实施 AI 生成 UI 的步骤。

---

## 22. LPython：新型快速可重定向Python编译器（2023）

**原文标题**: LPython: Novel, Fast, Retargetable Python Compiler (2023)

**原文链接**: [https://lpython.org/blog/2023/07/lpython-novel-fast-retargetable-python-compiler/](https://lpython.org/blog/2023/07/lpython-novel-fast-retargetable-python-compiler/)

本文介绍 LPython，一种为速度和可重定向性设计的新型 Python 编译器。LPython 将类型注解的 Python 代码编译为使用 LLVM、C、C++、WASM、Julia 和 x86 等后端的优化机器代码。它具有快速的编译和运行时性能，以及即时 (JIT) 编译和与 CPython 的互操作性。

LPython 与 LFortran 共享一个抽象语义表示 (ASR)，从而实现共享优化。编译涉及将代码转换为 AST，然后转换为 ASR，随后进行 ASR 到 ASR 的传递以进行优化（例如，循环转换）。用户可以查看生成的 C 或 LLVM 代码。

该编译器提供与机器无关的优化，如循环展开、向量化、死代码消除和函数内联，这些优化通过命令行参数激活。提前 (AoT) 编译允许直接编译为二进制文件，而 JIT 编译则使用 `@lpython` 装饰器启用。通过 `@pythoncall` 装饰器实现与 CPython 的互操作性。

基准测试展示了 LPython 在 JIT 编译场景中与 Numba 的性能比较，包括数组求和、逐点乘法、插入排序和 Dijkstra 算法。LPython 通常比 Numba 表现出更快的执行时间，尽管编译时间可能有所不同。本文重点介绍了 LPython 的 alpha 版本发布，并鼓励用户报告错误。

---

## 23. 墨西哥正在发生的纳瓦特尔语和玛雅语复兴

**原文标题**: Náhuatl and Mayan Language Renaissance Occurring in Mexico

**原文链接**: [https://yucatanmagazine.com/mayan-language-renaissance/](https://yucatanmagazine.com/mayan-language-renaissance/)

墨西哥正积极致力于振兴其68种官方认可的本土语言，包括玛雅语和纳瓦特尔语，这些语言正因城市化、全球化以及西班牙语和英语的主导地位而面临衰落。墨西哥政府已启动诸如本土语言课程和双语课程等举措，以保护该国丰富的语言遗产。在尤卡坦州，75个自治市的35,000名学生现在可以从小学习尤卡坦玛雅语。墨西哥城学校也正在开设纳瓦特尔语课程，以应对该语言的逐渐消失，尤其是在年轻一代中。

这些举措旨在保护的不仅是语言，还有相关的文化和历史意义，正如《土著人民语言权利总法》所强调的那样。除了学校，在INDEMAYA和尤卡坦自治大学等机构还提供成人玛雅语课程。

尽管面临诸如资源有限和方言差异等挑战，人们对本土语言的热情日益增长，为其生存提供了充满希望的未来。文章还承认墨西哥本土语言使用者面临的歧视，这种歧视源于历史殖民和持续存在的社会偏见。保护这些语言不仅被视为一项语言事业，而且被视为一场为本土人民争取身份、尊严和在墨西哥社会中地位的斗争。

---

## 24. 首例定制基因编辑疗法治愈婴儿

**原文标题**: Baby is healed with first personalized gene-editing treatment

**原文链接**: [https://www.nytimes.com/2025/05/15/health/gene-editing-personalized-rare-disorders.html](https://www.nytimes.com/2025/05/15/health/gene-editing-personalized-rare-disorders.html)

患有罕见遗传病CPS1缺陷（影响130万分之一的婴儿）的婴儿KJ Muldoon，作为首位接受定制基因编辑治疗的患者，创造了医学史。KJ出生仅一周就被诊断出患有此病，由于死亡率高，且若存活则可能出现严重的生长发育迟缓，最终需要肝移植，因此医生建议进行舒缓疗护。

他的父母选择为他而战，促成了在费城儿童医院进行的开创性个性化治疗。该治疗涉及一种定制的输注疗法，旨在修复KJ特定的基因突变。现在9个半月大的KJ显示出发展进步，表明治疗正在起作用。这标志着个性化医学的重大进展，为患有罕见遗传病的其他个体开启了类似疗法的大门。

---

## 25. BuyMeACoffee悄然停止支持多国（2024）

**原文标题**: BuyMeACoffee silently dropped support for many countries (2024)

**原文链接**: [https://zverok.space/blog/2024-08-08-bmac-snafu.html](https://zverok.space/blog/2024-08-08-bmac-snafu.html)

本文详细描述了BuyMeACoffee (BMAC) 悄然移除Payoneer作为收款选项所引发的争议，此举严重影响了乌克兰等Stripe无法使用的国家的创作者。作者强调了对此变更缺乏沟通的问题，并将其与BMAC持续塑造的正面公众形象形成对比。

乌克兰创作者报告了收款问题，最初得到的是通用的支持回复。这项变更于2024年2月至5月之间的某个时间实施，实际上切断了许多人的资金来源。作者强调了BMAC对乌克兰创作者的重要性，并列举了该平台支持他们重要工作的例子。

作者批评了BMAC对此事的处理方式，指出了事先没有通知、回避性的支持以及提供的信息不一致。文章包含了BMAC变更日志的截图以及Twitter上的用户报告。

更新显示，BMAC在Twitter上迟来且不足的“官方”回复，作者对其进行了剖析，质疑退款声明并要求更透明。随后的更新分享了一封直接支持邮件，揭示移除Payoneer的原因是与未来的功能不兼容。尽管提供了基于证据的批评，作者最终因涉嫌传播虚假信息而被BMAC在Twitter上封锁。即便在此之前，BMAC的支持人员私下告知一位乌克兰用户，Payoneer将运作到11月，这与之前要求所有资金必须在8月之前提取的指示相矛盾，封锁仍然发生。文章最后质疑了BMAC的信誉，并强调了该平台糟糕的沟通。

---

## 26. 用胶带拯救阿波罗13号宇航员的埃德·斯迈利去世，享年95岁

**原文标题**: Ed Smylie, Who Saved the Apollo 13 Crew with Duct Tape, Dies at 95

**原文链接**: [https://www.nytimes.com/2025/05/16/science/space/ed-smylie-dead.html](https://www.nytimes.com/2025/05/16/science/space/ed-smylie-dead.html)

领导NASA团队在1970年阿波罗13号飞船爆炸后，设计出临时解决方案以拯救宇航员的罗伯特“艾德”斯迈利于4月21日去世，享年95岁。斯迈利和他的团队利用纸板、塑料袋和胶带制作了一个装置，用于去除登月舱中过量的二氧化碳，该登月舱原本设计只能支持两名宇航员，但在爆炸后必须容纳三名宇航员。

文章详细介绍了斯迈利在得知危机后，立即前往休斯顿载人航天中心。登月舱原本计划搭载两名宇航员前往月球，但舱内的三名宇航员正在产生致命剂量的二氧化碳，这促使斯迈利和他的团队迅速设计出一个替代方案。

理查德·尼克松总统授予斯迈利和他的副手詹姆斯·V·科雷尔总统自由勋章，以表彰他们在阿波罗13号任务成功中发挥的关键作用，并认可他们“临时搭建但有效的装置”拯救了宇航员的生命。

---

## 27. 青色 – Lua 的静态类型方言

**原文标题**: Teal – A statically-typed dialect of Lua

**原文链接**: [https://teal-language.org/](https://teal-language.org/)

Teal是一种静态类型的Lua方言，旨在为Lua开发增加类型安全和结构，同时保持其最小化和可移植性的核心原则。它使用`tl`编译器将`.tl`文件转换为`.lua`文件。 Teal提供了数组、映射、记录、接口、联合类型和泛型等类型注释功能。

安装很简单，可以通过LuaRocks (`luarocks install tl`)或预编译的二进制文件进行安装。对于较大的项目，建议使用Cyan作为构建工具。 IDE支持通过Visual Studio Code的`vscode-teal`和NeoVim的`teal-language-server`等扩展提供。

文档已在线提供，该项目已在多个讨论其历史、动机和未来方向的讲座中被提及。

Teal社区在GitHub上非常活跃，拥有一个社区论坛和一个Matrix聊天频道。 Teal由一个不断增长的贡献者社区开发，并且是用Teal自身编写的。该项目是免费和开源的，采用MIT许可证。 Teal Playground也可用于在浏览器中试用该语言。

---

## 28. Cracked – 链式调用/CSS选择器风格的Web音频库

**原文标题**: Cracked – Method chaining/CSS-style selector web audio library

**原文链接**: [https://github.com/billorcutt/i_dropped_my_phone_the_screen_cracked](https://github.com/billorcutt/i_dropped_my_phone_the_screen_cracked)

"我不小心摔了手机，屏幕碎了" (Cracked) 是一个 Web 音频库，旨在简化浏览器中音频节点的创建、配置和连接，它使用方法链和 CSS 样式的选择器。这使得开发者可以轻松构建复杂的音频结构。

该库提供简洁的语法。例如，`__().sine().dac().play()` 创建、连接并启动一个正弦波振荡器到音频输出。涉及振荡器、滤波器、压缩器和其他节点的更复杂的设置可以使用类似的链式调用创建和连接。

Cracked 使用 CSS 样式的选择器来定位和操作特定的音频节点。节点可以通过它们的类型（例如，“sine”）、ID（例如，“#lp1”）或其他属性进行选择，从而允许有针对性的参数更改。

该库还支持宏，允许用户将音频节点链封装为可重用的单元，类似于模块化合成器的打补丁。然后，这些宏可以进一步打包成工厂函数来创建插件，从而实现可重用、可定制音频组件的创建。

Cracked 的主要目标是促进简洁和直观的音频编码，让用户专注于创意声音设计。了解更多信息的资源包括文档、概述页面和用于实验的桌面应用程序。欢迎通过评论、问题报告或拉取请求进行贡献。

---

## 29. 风帆冲浪 SWE-1：我们的首款前沿型号

**原文标题**: Windsurf SWE-1: Our First Frontier Models

**原文链接**: [https://windsurf.com/blog/windsurf-wave-9-swe-1](https://windsurf.com/blog/windsurf-wave-9-swe-1)

简讯：风帆冲浪SWE-1发布，敬请关注后续报道

---

## 30. 锌微型电容器：两全其美

**原文标题**: Zinc Microcapacitors Are the Best of Both Worlds

**原文链接**: [https://spectrum.ieee.org/zinc-microcapacitor](https://spectrum.ieee.org/zinc-microcapacitor)

研究人员开发出锌离子微型电容器，为小型应用提供了一种介于电池和超级电容器之间的有前景的折衷方案。这项由Liam Critchley在EnergyNews报道、Yujia Fan、Nibagani Naresh等人于ACS Nano详细介绍的新技术，旨在将电池的高能量密度与超级电容器的快速充放电速率和长寿命相结合。这对于需要在紧凑外形中实现快速功率输出和可观的能量存储容量的应用尤为重要。该文章强调了这些微型电容器填补现有储能解决方案尚未满足的空白的潜力。

---

## 31. 无锁 Rust：如何在着火时建造过山车

**原文标题**: Lock-Free Rust: How to Build a Rollercoaster While It's on Fire

**原文链接**: [https://yeet.cx/blog/lock-free-rust/](https://yeet.cx/blog/lock-free-rust/)

Julian Goldstein 的文章《无锁 Rust：如何在着火的过山车上建造它》深入探讨了 Rust 中无锁编程的复杂性和危险性，特别关注于构建 `LockFreeArray<T, N>`。这种数据结构提供了一个固定大小的无锁数组，用于存储堆分配的值，从而能够在不使用传统锁的情况下并发地插入和删除数据。

该文章强调，无锁编程优先考虑速度而非安全性，需要开发人员手动管理线程安全。使用的关键组件是 `AtomicPtr<T>`、`AtomicUsize` 和 `compare_exchange`，以及对内存排序（`Ordering::{Acquire, Release, AcqRel, Relaxed}`）的仔细考虑。

`LockFreeArray` 的实现涉及一个空闲列表（freelist），这是一个可用槽位的链表，用于有效地管理数组的容量。`try_insert` 函数演示了使用 `compare_exchange` 原子性地声明空闲槽位的核心逻辑。选择正确的内存排序对于防止数据竞争和内存损坏至关重要。`Ordering::AcqRel` 确保在更新空闲列表头部之前，写入对其他线程可见。`take` 函数移除给定索引处的值 `T`。

该文章强调了无锁数据结构的性能优势，展示了在生产者-消费者场景中 `LockFreeArray` 明显优于 `Mutex<Vec<Option<T>>>` 实现的基准测试。它还警告说，无锁编程本质上是危险的，如果未正确实现，可能会导致内存泄漏、数据竞争和未定义行为。它最后建议，无锁技术通常是最后的手段，仅适用于性能至关重要且风险已充分理解的情况。

---

## 32. 疫情初期（2020年）平均工作日时长增加

**原文标题**: The average workday increased during the pandemic’s early weeks (2020)

**原文链接**: [https://www.library.hbs.edu/working-knowledge/you-re-right-you-are-working-longer-and-attending-more-meetings](https://www.library.hbs.edu/working-knowledge/you-re-right-you-are-working-longer-and-attending-more-meetings)

这项哈佛商学院的研究分析了全球16个城市310万人的数据，证实疫情初期平均工作日延长了8.2%（48.5分钟）。研究人员调查了封锁前后电子邮件和会议邀请，发现员工发送的电子邮件更多（增加5.2%），收件人更多（增加2.9%），且下班后活动更多（增加8.3%）。会议出席率也上升了13%，但每次会议时间缩短了（减少20%或12分钟）。

向远程工作的转变模糊了工作与生活的界限，导致工作日更长，因为员工需要适应异步工作并应对干扰。 Raffaella Sadun 认为员工采用了更灵活的时间安排。 虽然该研究无法评估互动的质量或对幸福感的影响，但 Sadun 对知识型员工的后续研究表明，员工的体验各不相同，家庭环境发挥了重要作用。

建议管理者理解员工的个人情况，关注产出而非追踪时间，并预期生产力差异。 文章还强调了视频会议疲劳是导致会议时间缩短的一个因素，并指出持续专注于屏幕的不自然和令人疲惫的方面。

---

## 33. Tek – 适用于24位Unicode终端的音乐制作程序

**原文标题**: Tek – A music making program for 24-bit Unicode terminals

**原文链接**: [https://codeberg.org/unspeaker/tek](https://codeberg.org/unspeaker/tek)

无法访问文章链接。

---

## 34. 三步搞定闰年检测

**原文标题**: A leap year check in three instructions

**原文链接**: [https://hueffner.de/falk/blog/a-leap-year-check-in-three-instructions.html](https://hueffner.de/falk/blog/a-leap-year-check-in-three-instructions.html)

本文详细介绍了一种非常规的闰年计算方法，利用位操作技巧仅用三条CPU指令即可实现闰年检测。文章首先概述了标准的闰年计算方法（能被4整除，但不能被100整除，除非也能被400整除），然后对其进行速度优化，用位掩码和乘法代替模运算。其核心思想是使用魔术常量来近似除法的分数部分，从而避免代价高昂的模运算。

文章接着介绍了一种位操作解决方案，该方案使用一个魔术常量乘数 (`f`)、一个掩码 (`m`) 和一个阈值 (`t`)，通过表达式 `((y * f) & m) <= t` 来确定闰年。作者解释了如何使用 z3 求解器找到这些常量，这些常量通过巧妙的位运算有效地编码了标准的闰年规则。文章分析了这些常量的二进制表示，揭示了它们本质上执行了一系列对乘积 `y * f` 中位范围的比较，模拟了被 4、25 和 16 整除的条件。

文章进一步探讨了所选常量的数学原理，以及如何将此方法扩展到其他位宽，然后对它的效率进行了基准测试。虽然标准方法在通常情况下更正确，但对于特定年份范围，位操作技巧提供了速度提升。

---

## 35. 基于坚固碳纳米管/BiSbTe泡沫的热电器件

**原文标题**: Thermoelectric generator based on a robust carbon nanotube/BiSbTe foam

**原文链接**: [https://onlinelibrary.wiley.com/doi/10.1002/cey2.650](https://onlinelibrary.wiley.com/doi/10.1002/cey2.650)

无法访问文章链接。

---

## 36. GTK克雷尔监视器

**原文标题**: GTK Krell Monitors

**原文链接**: [https://gkrellm.srcbox.net/](https://gkrellm.srcbox.net/)

GKrellM 是一款系统监视器程序，可显示 CPU 使用率、内存、磁盘活动、网络流量等。它支持主题定制，并具有诸如主机名显示、时钟/日历、SMP CPU 监控、温度/风扇/电压传感器监控、进程监控、磁盘监控、互联网连接监控、网络接口监控、内存/交换空间使用计量器、文件系统计量器、邮箱监视器、APM 电池计量器和运行时间显示等内置功能。它被设计为轻量级，由单个进程管理多个监视器。

GKrellM 可以在客户端模式下运行，以从远程 gkrellmd 服务器收集数据。两者都具有插件功能，可以扩展功能。

它需要 Gtk+ 2.24 或更高版本，而 gkrellmd 仅需要 GLib 2.32 或更高版本。 它支持 Linux、FreeBSD、Mac OS X、NetBSD/OpenBSD，并且单独提供 Windows 版本。

该文章提供适用于各种操作系统的软件包下载、源代码仓库链接、以及用户和开发者的联系方式，包括邮件列表、Matrix 房间、IRC 频道以及用于提交错误报告或功能请求的问题单。它还包括主题、教程和其他相关项目的链接。 GKrellM 在 GNU 通用公共许可证下发布。

---

## 37. Ollama违反llama.cpp许可协议已超过一年

**原文标题**: Ollama violating llama.cpp license for over a year

**原文链接**: [https://github.com/ollama/ollama/issues/3185](https://github.com/ollama/ollama/issues/3185)

此问题报告声称 Ollama 违反了其静态链接的依赖项 llama.cpp 的 MIT 许可证，因为它未在其发布制品（二进制文件）中分发“Georgi Gerganov”（llama.cpp 的作者）的版权声明。MIT 许可证要求版权声明以源代码和二进制形式存在。

报告者 jart 表示，他们搜索了他们的 Linux 和 Windows Ollama 安装文件夹，但未找到所需的版权声明。他们期望在二进制制品中找到依赖项目的版权声明，尽管他们指出有些人认为在 README 中提及 llama.cpp 也是合适的，尽管许可证并没有严格要求。

报告表明此违规行为已持续一年多。该报告包括用于搜索版权声明的命令，并将该问题标记为一个 bug。它还表明某些事情没有按预期工作。

---

## 38. 韭菜与泄露

**原文标题**: Leeks and Leaks

**原文链接**: [https://daniel.haxx.se/blog/2025/05/16/leeks-and-leaks/](https://daniel.haxx.se/blog/2025/05/16/leeks-and-leaks/)

本文探讨了在curl等软件中处理.onion域名（一种Tor专用域名）的复杂性。通过标准DNS解析这些域名可能会泄露用户访问Tor服务的意图，这是一种安全风险。为了解决这个问题，RFC 7686发布，建议软件拒绝直接解析.onion域名。

Curl在2023年实施了这一建议，阻止了.onion地址的直接解析。其目的是让Tor用户使用SOCKS代理，以便Tor服务器安全地处理域名解析。

然而，这与拥有自定义网络配置的用户产生了冲突，在这些配置中，对.onion的标准DNS解析被认为是安全的。提出了覆盖curl阻止行为的建议，但由于API方面的考虑，这些建议并未实施。

最近发布的oniux（一个隔离第三方应用程序的Tor项目工具）突显了这个问题。Oniux的示例命令行包含一个curl命令，该命令试图直接解析一个.onion地址，由于curl实施的阻止，该命令在新版本的curl中会失败。这种情况导致curl增强隐私的努力与新的Tor工具产生冲突，从而导致用户感到沮丧，并且需要一个解决方案。文章最后提出了如何解决这个冲突的问题，并承认了平衡安全性和用户灵活性的内在困难。

---

## 39. TLA⁺ 当前的开发状态

**原文标题**: The current state of TLA⁺ development

**原文链接**: [https://ahelwer.ca/post/2025-05-15-tla-dev-status/](https://ahelwer.ca/post/2025-05-15-tla-dev-status/)

本文探讨了TLA⁺开发的现状，重点关注使TLA⁺语言工具更易于开发的重要性。文章强调了现有工具，包括解析器（SANY、TLAPM、tree-sitter-tlaplus）、解释器（TLC、Spectacle）、模型检查器（TLC、Apalache、Spectacle）以及其他工具，如TLAPM、Snowcat类型检查器、格式化程序和一个LSP服务器。

作者强调了维护SANY和TLC等遗留代码库的挑战，这些代码库难以测试，并且当前贡献者缺乏全面的知识。他提出了三种策略来克服这一挑战：开发标准化的、与实现无关的测试套件；通过指南和教程改进开发者入门；以及获得资助和津贴来资助全职贡献。

作者对TLA⁺的未来表示乐观，强调了工具生态系统的优势和社区对改进的渴望。他强调了将代码库视为需要学习的固定工件的重要性，并指出需要一个学习大纲。他还提到了潜在的未来发展，如生成式测试和语法简化。最后，他强调TLA⁺开发者面临的挑战与其他编程语言的开发者面临的挑战类似。

---

## 40. 大型语言模型智能体循环与工具使用的不合理有效性

**原文标题**: The unreasonable effectiveness of an LLM agent loop with tool use

**原文链接**: [https://sketch.dev/blog/agent-loop](https://sketch.dev/blog/agent-loop)

Philip Zeyliger 探讨了简单LLM代理循环与工具使用所带来的惊人效果，尤其是在名为 Sketch 的编程助手的情境下。其核心循环包括将用户输入提供给 LLM，接收输出和潜在的工具调用，执行工具（在此案例中主要是 bash），然后将结果反馈给 LLM。

文章强调，当前的 LLM，例如 Claude 3.7 Sonnet，仅凭此循环以及访问像 bash 这样的通用工具，便能有效地解决许多复杂的问题。示例包括自动化 git 操作、处理合并以及调试类型检查器错误。该代理循环展现出适应性，例如安装缺失的工具或调整到不同的命令行选项。

虽然 bash 是主要工具，但文章提到，专门的工具，特别是那些用于精确文本编辑的工具，可以进一步提高性能。作者认为，代理循环将自动化以前被认为过于特定或不稳定而无法使用传统自动化方法的任务，例如将堆栈跟踪与 git 提交相关联。他设想开发者们会为各种工作流程创建自定义的、临时的代理循环，并鼓励读者们尝试这项技术。

---

## 41. 《轮中之脑》为心智科学奠定了新的基础。

**原文标题**: “The Mind in the Wheel” lays out a new foundation for the science of mind

**原文链接**: [https://www.experimental-history.com/p/new-paradigm-for-psychology-just](https://www.experimental-history.com/p/new-paradigm-for-psychology-just)

亚当·马斯特罗亚尼探讨了心理学领域对新范式的需求，并从“黏菌时间模具”的《轮中之脑》一书中汲取灵感。他认为，由于缺乏明确的范式（他将其定义为一套控制研究领域的单元和规则），心理学发展停滞不前。他区分了“科学”（对单元和规则进行推测和验证）、“朴素研究”（在没有明确框架下进行实验）和“印象派研究”（研究定义不清的抽象概念）。

他批评了当前心理学研究，认为其常常落入后两者范畴，导致实际进展甚微。他告诫人们不要将心理学简化为神经科学，认为虽然神经科学是基础，但它并不是理解大脑功能的最有效层面，就像试图仅从原子的角度设计纽约地铁系统一样。

马斯特罗亚尼提出了“控制论心理学”作为一种潜在的新范式。该范式认为，大脑由“控制系统”（类似于恒温器）组成，这些系统监控变量并减少误差。在此框架下，“情绪”是这些控制系统的误差信号（例如，营养控制系统发出的饥饿感）。他强调，“幸福”本身不是一种情绪，而是成功纠正错误的结果。挑战在于通过严谨的方法，而非随意的定义，来识别和理解这些控制系统及其功能。

---

## 42. 美国国家航空航天局用孤注一掷的推进器修复术，让古老的旅行者1号宇宙飞船重获新生

**原文标题**: NASA keeps ancient Voyager 1 spacecraft alive with Hail Mary thruster fix

**原文链接**: [https://www.theregister.com/2025/05/15/voyager_1_survives_with_thruster_fix/](https://www.theregister.com/2025/05/15/voyager_1_survives_with_thruster_fix/)

NASA成功复活旅行者1号休眠推进器，避免失联风险。

---

## 43. Coinbase称黑客贿赂员工窃取客户数据，勒索2000万美元。

**原文标题**: Coinbase says hackers bribed staff to steal customer data, demanding $20M ransom

**原文链接**: [https://www.cnbc.com/2025/05/15/coinbase-says-hackers-bribed-staff-to-steal-customer-data-and-are-demanding-20-million-ransom.html](https://www.cnbc.com/2025/05/15/coinbase-says-hackers-bribed-staff-to-steal-customer-data-and-are-demanding-20-million-ransom.html)

Coinbase报告称，网络罪犯贿赂海外客服人员窃取敏感客户数据，用于社交工程攻击，可能导致公司损失高达4亿美元。黑客索要2000万美元赎金，Coinbase拒绝支付。

被盗数据包括姓名、地址、电话号码、电子邮件、屏蔽后的银行账户信息、部分社会安全号码、政府身份证件图像和账户余额。重要的是，密码和私钥没有泄露，Coinbase Prime账户未受影响。

Coinbase检测到此次违规行为，解雇了涉事员工，警告了受影响的客户，并加强了欺诈监控。该公司正在与执法部门合作，并设立了2000万美元的奖励基金，用于提供信息以逮捕和定罪罪犯。

尽管发生了这起事件，Coinbase对其未来仍然充满信心，其近期收购旨在全球扩张，并即将被纳入标准普尔500指数，均证明了这一点。首席执行官Brian Armstrong重申了他的目标，即在未来十年内将Coinbase打造成领先的金融服务应用程序。

---

## 44. Dr. Dobb's Journal杂志对杰夫·拉斯金的采访 (1986年)

**原文标题**: Dr. Dobb's Journal interviews Jef Raskin (1986)

**原文链接**: [https://computeradsfromthepast.substack.com/p/dr-dobbs-journal-interviews-jef-raskin](https://computeradsfromthepast.substack.com/p/dr-dobbs-journal-interviews-jef-raskin)

无法访问文章链接。

---

## 45. 在美国，旋转爆震火箭发动机首次试飞

**原文标题**: In the US, a rotating detonation rocket engine takes flight

**原文链接**: [https://arstechnica.com/space/2025/05/venus-aerospace-flies-its-rotating-detonation-rocket-engine-for-the-first-time/](https://arstechnica.com/space/2025/05/venus-aerospace-flies-its-rotating-detonation-rocket-engine-for-the-first-time/)

维纳斯航空公司成功完成了其旋转爆震火箭发动机的短程飞行测试，地点位于新墨西哥州美国太空港，这标志着他们认为的美国首次此类技术的飞行测试。该发动机推力达2000磅，为一枚小型火箭提供了约半分钟的动力，但未突破音障。

与传统火箭发动机相比，旋转爆震发动机通过在环形通道内使用超音速冲击波，具有潜在的燃油效率改进。虽然这一概念已在其他国家进行探索，但这对美国的发展而言是一个重要的里程碑。

维纳斯航空公司由Sassie和Andrew Duggleby创立，设想利用该技术开发一种能够在两小时内将乘客运送到全球各地的超音速飞机。虽然这一目标是长期的，但该公司目前正专注于商业和国防应用中经济实惠的超音速飞行的近期机遇。他们正积极与美国国防和国家安全机构以及商业伙伴合作，探索其在物流、航空航天和未来交通运输中的应用。该公司强调政府持续资助对于维持美国在超音速领域的竞争力至关重要。

---

## 46. 在复杂系统上的工作：我在谷歌学到的东西

**原文标题**: Working on complex systems: What I learned working at Google

**原文链接**: [https://www.thecoder.cafe/p/complex-systems](https://www.thecoder.cafe/p/complex-systems)

Teiva Harsanyi的文章《处理复杂系统：我在谷歌的工作经验》区分了复杂问题和复杂系统，认为复杂系统需要独特的、适应性强的解决方案，这与遵循结构化和可重复流程的复杂问题不同。

文章指出了复杂系统的关键特征：涌现行为、延迟后果、局部与全局优化冲突、滞后效应和非线性。这些特征使得使用传统方法难以预测和管理复杂系统。

为了有效地驾驭这些系统，Harsanyi提出了几个模式：倾向于可逆的决策（双向门）、超越即时指标思考，考虑整体系统健康状况、拥抱创新以寻求非常规的解决方案、使用受控的发布技术（特性开关、金丝雀发布、渐进式发布、影子测试）、优先考虑可观察性以了解系统状态、利用模拟进行测试、利用机器学习进行自适应决策以及培养强大的团队协作。

作者强调，认识到系统的复杂性对于选择正确的解决问题方法至关重要。许多系统是复杂和复杂元素的混合体，需要在某些领域具有适应性，而在其他领域则需要结构化的解决方案。最终，这篇文章鼓励工程师识别复杂系统，理解它们的特征，并应用适当的策略来成功地管理它们。

---

## 47. 滚动公路

**原文标题**: Rolling Highway

**原文链接**: [https://en.wikipedia.org/wiki/Rolling_highway](https://en.wikipedia.org/wiki/Rolling_highway)

“滚装高速公路”（Ro-La）是一种联合运输方式，即将公路卡车通过铁路运输，属于驮背运输的一种形式。这在装载限界空间有限的地区，例如欧洲，尤其有用。在欧洲，使用诸如“Modalohr”、“CargoBeamer”和“Niederflurwagen”之类的特殊车厢来降低拖车的高度，使其符合高度限制。卡车司机可以随车同行，乘坐客车或卧铺车厢。

滚装高速公路通常用于过境路线，尤其是穿越阿尔卑斯山等山区和整个欧洲的路线。奥地利是一个重要的过境国，滚装高速公路将卡车从巴伐利亚运往意大利和东欧。印度科康铁路推出了一种成功的滚装滚卸 (RORO) 服务，用平板车运输卡车。瑞士通过戈塔德和洛奇堡-辛普朗线路运营穿越阿尔卑斯山的滚装高速公路。

法国目前有两条使用Modalohr技术并以VIIA品牌运营的滚装高速公路：阿尔卑斯山铁路高速公路（连接萨瓦省至都灵）和卡车铁路（连接卢森堡至佩皮尼昂）。已经提出了几条新的线路，尽管有些线路面临财务挑战。目前在法国提供的线路有VIIA（加莱 – 勒布卢、加莱 – 马孔、加莱 – 奥尔巴萨诺、马孔 – 勒布卢、贝滕堡 – 勒布卢、艾顿 – 奥尔巴萨诺）和Cargobeamer（加莱 – 佩皮尼昂、加莱 – 多莫多索拉）。

---

## 48. 建筑套装 (2005–2006)

**原文标题**: Archisuits (2005–2006)

**原文链接**: [https://insecurespaces.net/archisuits-2005-2006/](https://insecurespaces.net/archisuits-2005-2006/)

建筑服 (2005-2006) 是一个艺术项目，包含四套休闲慢跑服，专为与洛杉矶的建筑结构互动而设计。这些服装融入了建筑结构的负空间，使穿着者能够舒适地占据他们通常被排除在外的空间。该项目的核心评论围绕着建筑作为一种社会控制工具，特别强调了建筑环境如何被用来规范和控制种族、阶级和性别化的身体。“建筑服”通过创造能够与这些空间进行放松互动的服装，提出了一种抵抗形式。该作品表明，仅仅是存在，尤其是舒适和悠闲地存在，就可以挑战这些建筑设计的排他性。该项目鼓励观众思考建筑如何参与社会分层，并提出了一种有趣而有效的方法来打破这种动态。

---

## 49. Show HN: 用于 LLM 应用的免费 AI 风险评估工具

**原文标题**: Show HN: A free AI risk assessment tool for LLM applications

**原文链接**: [https://www.gettavo.com/app](https://www.gettavo.com/app)

TavoAI：免费的LLM应用AI风险评估工具（GitHub登录）

---

## 50. 大型语言模型应用OWASP Top 10

**原文标题**: OWASP Top for Large Language Model Applications

**原文链接**: [https://owasp.org/www-project-top-10-for-large-language-model-applications/](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

OWASP大型语言模型应用十大安全风险项目旨在普及部署和管理大型语言模型和生成式人工智能应用时的安全风险。该项目提供资源，包括大型语言模型应用十大安全风险列表，重点关注诸如提示词注入、数据泄露和不安全输出处理等关键漏洞。该项目目标是提高意识、建议补救措施并提升大型语言模型应用安全性。

2025年列表以及诸如面向管理生成式人工智能部署的首席信息安全官的安全与治理检查清单和准备及应对深度伪造指南等资源均可下载。欢迎通过OWASP Slack频道（#project-top10-for-llm）贡献。

OWASP十大安全风险（v1.1）详细列出了以下漏洞：提示词注入、不安全输出处理、训练数据投毒、模型拒绝服务、供应链漏洞、敏感信息泄露、不安全插件设计、过度代理、过度依赖和模型盗窃。

该项目鼓励通过新闻通讯、LinkedIn、代码仓库和维基等方式参与社区。个人可以贡献、订阅更新，甚至赞助该项目。OWASP基金会通过其全球网络和开源倡议支持该项目。

---

## 51. 逗号3X：初步印象

**原文标题**: Comma 3X: Initial Impressions

**原文链接**: [https://beesbuzz.biz/blog/14719-Comma-3X-Initial-impressions](https://beesbuzz.biz/blog/14719-Comma-3X-Initial-impressions)

无法访问文章链接。

---

## 52. 寻路

**原文标题**: Pathfinding

**原文链接**: [https://juhrjuhr.itch.io/deep-space-exploitation/devlog/945428/9-pathfinding](https://juhrjuhr.itch.io/deep-space-exploitation/devlog/945428/9-pathfinding)

JuhrJuhr 详述了其游戏《深空探索》寻路系统的开发，重点介绍了挑战和解决方案。该寻路系统需要处理动态、可破坏的环境，优先选择远离障碍物的安全路径，并适应游戏中类似《小行星》的环绕特性。

所选方法采用 A* 搜索和空间分割树来实现高效的世界查询。该树划分游戏区域，可以快速识别被阻挡或未被阻挡的区域，从而最大限度地减少昂贵的碰撞检测。为了处理实时的环境变化，该算法缓存节点阻塞状态，但会定期（每 500 毫秒）使其失效以进行更新。

为了创建更自然的路径，会根据每个节点到物体的距离为其分配一个“邻近度评分”，从而增加靠近障碍物的节点的遍历成本。对于环绕路径，边界节点与其在网格对面的对应节点相连。NPC 路径跟随通过添加屏幕外节点来解决，以引导 NPC 环绕屏幕，并在环绕期间使用最近的 NPC 位置进行计算。

为了优化性能，如果寻路过程超过性能阈值，则将其拆分到多个游戏帧中执行。作者优先选择自主开发的解决方案而不是预先存在的方法，以便学习并享受解决问题的过程。最终结果是一个性能良好且能生成合理且美观路径的系统。未来的工作可能涉及基于世界变化的更精确的缓存失效。

---

## 53. 用生成式人工智能将3D可购产品上线

**原文标题**: Bringing 3D shoppable products online with generative AI

**原文链接**: [https://research.google/blog/bringing-3d-shoppable-products-online-with-generative-ai/](https://research.google/blog/bringing-3d-shoppable-products-online-with-generative-ai/)

利用生成式AI打造互动式3D商品可视化，革新在线购物体验

本文探讨了利用生成式AI创建互动式3D商品可视化，以革新在线购物体验的演进历程。 目标是模拟线下购物体验，让顾客能够在线上虚拟地检查商品。

第一代技术采用神经辐射场（NeRFs）从多张图像生成360°视图。最初在Google搜索上的鞋类商品上取得了成功，但在处理复杂几何形状时遇到了困难。

第二代技术引入了视角条件扩散先验，使模型即使在输入图像有限的情况下也能预测商品从不同角度的外观。这种方法具有良好的可扩展性，目前用于在Google购物上生成鞋类商品的360°视图。

最新的突破是利用Google最先进的视频生成模型Veo，它擅长捕捉复杂的照明和材料互动。 通过在3D合成资产的数据集上对Veo进行微调，他们只需三张图像即可生成逼真的360°商品旋转视图，并能很好地推广到家具和电子产品等多种商品类别。 这种方法还简化了流程，无需精确的相机姿态估计。

文章最后强调了3D生成式AI所取得的进展，并表达了对未来将提升在线购物体验的进步的期待。

---

## 54. C++中的初始化简直是疯了 (2017)

**原文标题**: Initialization in C++ is bonkers (2017)

**原文链接**: [https://blog.tartanllama.xyz/initialization-is-bonkers/](https://blog.tartanllama.xyz/initialization-is-bonkers/)

本文重点介绍了 C++ 中初始化的复杂性和潜在陷阱，特别是默认初始化、值初始化和零初始化之间的差异。它演示了构造函数定义中的细微变化如何因未初始化的变量而导致未定义的行为。

作者首先用一个测验来说明这个问题：在结构体定义中声明了 `= default` 构造函数的 `foo` 结构体，会导致其成员进行零初始化，而 `= default` 构造函数在结构体外部定义的 `bar` 结构体，则会使其成员保持未初始化。这种差异源于编译器是否将构造函数视为“用户提供的”。

文章解释了不同的初始化类型：
*   **默认初始化：** 调用类的默认构造函数，初始化数组元素，或对其他类型不执行任何操作。
*   **值初始化：** 默认初始化类（如果在默认构造函数不是用户提供/删除的情况下，先进行零初始化），值初始化数组元素，或零初始化其他类型。
*   **零初始化：** 将标量类型初始化为 0，通过零初始化成员和基类来初始化类，并通过零初始化元素来初始化数组。

关键在于，用户提供的构造函数（在类定义外部定义）会影响在值初始化期间是否发生零初始化。这个看似微小的细节可能会导致未初始化的变量和未定义的行为。

作者强调了显式初始化变量以避免这些问题的重要性，并建议如果默认构造对于类来说不是有效的操作，则完全删除默认构造函数。文章最后指出 C++ 中存在许多不同的初始化形式，强调需要谨慎和显式初始化，以防止出现意外行为。

---

## 55. 用大语言模型写了几个月代码后，我决定回归用脑子了。

**原文标题**: After months of coding with LLMs, I'm going back to using my brain

**原文链接**: [https://albertofortin.com/writing/coding-with-ai](https://albertofortin.com/writing/coding-with-ai)

一位经验丰富的软件工程师讲述了他们使用LLM（特别是Claude和Cursor）为他们的SaaS业务构建新基础设施的经验，涉及Go和Clickhouse。最初，他们对AI辅助编码的速度和潜力感到兴奋，并将大量的代码生成委托给LLM，更多地扮演产品经理的角色。

然而，经过几周的开发，问题开始浮出水面。调试变得越来越困难，代码库显示出不一致、重复的代码，以及缺乏整体架构的连贯性——就像多个不协调的初级开发人员的工作。尽管向LLM提供了充分的上下文和规范，但它未能生成干净、一致的代码。

作者意识到他们过度依赖AI，忽略了自己的技能和批判性思维。他们决定退一步，学习Go和Clickhouse的最佳实践，并重写有问题的代码段。他们现在使用LLM进行更简单的任务，如代码重命名或转换伪代码，但避免要求它从头开始生成整个功能或计划。

作者担心AI可能会降低思维敏锐度和编码能力，尤其是对于那些可能被诱导进行“感觉编码”的非编码人员，而没有理解其基本原理。他们批评当前AI编码工具的状态为“好，但不够好”，并且可能会让我们变得更笨。他们对围绕AI代理的炒作表示怀疑，并对模型性能的不一致表示担忧，突出了使用当前LLM构建复杂应用程序的难度。作者提倡一种平衡的方法，将AI作为助手而不是取代人类的专业知识。

---

## 56. Show HN：实时高斯溅射

**原文标题**: Show HN: Real-Time Gaussian Splatting

**原文链接**: [https://github.com/axbycc/LiveSplat](https://github.com/axbycc/LiveSplat)

LiveSplat是由Mark Liu开发的闭源算法，用于使用RGBD相机流进行实时高斯溅射。它从一个更大的VR遥操作机器人项目中衍生出来，现在公开发布以供实验。该应用程序目前处于Alpha阶段，支持Windows和Ubuntu系统，使用x86_64 CPU和Nvidia显卡，需要Python 3.12+。用户可以通过pip安装，使用适用于其操作系统的特定URL。

要使用LiveSplat，用户需要创建一个Python集成脚本来向查看器提供RGBD数据。提供了一个示例脚本`livesplat_realsense.py`用于Intel Realsense相机。作者承认测试有限，并请求关于安装问题的反馈。虽然代码不是开源的，但作者愿意通过电子邮件mark@axby.cc接受用于商业目的的许可和集成咨询。 还有一个演示视频展示了LiveSplat的输出。

---

## 57. 在本地运行你的 GitHub Actions

**原文标题**: Run your GitHub Actions locally

**原文链接**: [https://github.com/nektos/act](https://github.com/nektos/act)

本文介绍了`act`，一个允许您在本地运行GitHub Actions的工具。其主要优点是：

*   **快速反馈：** 通过直接在您的机器上测试工作流更改，避免提交/推送循环。这加速了`.github/workflows/`文件和嵌入式GitHub Actions的开发和调试。
*   **本地任务运行器：** 通过利用您现有的GitHub Actions定义进行本地任务自动化，替换或增强Makefile，减少冗余。

`act`的工作原理是解析`.github/workflows/`目录，识别必要的Docker镜像，并根据定义的依赖关系确定执行路径。 然后，它使用Docker API为每个action运行容器，通过配置环境变量和适当的文件系统来模拟GitHub环境。 提供了一个VS Code扩展程序，用于无缝集成。 本文鼓励用户查阅act用户指南以获取更多文档，并通过Gitter提供支持。 它还包括贡献指南和从源代码手动构建工具的说明。

---

## 58. 我不喜欢NumPy

**原文标题**: I don't like NumPy

**原文链接**: [https://dynomight.net/numpy/](https://dynomight.net/numpy/)

在一篇对NumPy的批判性分析中，作者表达了对这个流行的Python数组计算库的深刻厌恶。虽然承认它在简单操作上的易用性，但作者认为，在处理更复杂、多维数组操作时，NumPy变得笨拙且令人困惑。

核心问题在于NumPy的广播机制，作者认为它隐式、难以理解，并且在对齐维度进行操作时容易出错。作者强调了将操作应用于数组特定维度的困难，导致使用维度对齐技巧和像`np.tensordot`这样的函数，这些函数难以理解和调试，代码变得复杂。索引也因其复杂的规则和不可预测的行为而受到批评，甚至导致AI模型难以确定数组的形状。

作者将NumPy的方法与使用循环的清晰度进行了对比（虽然承认循环的性能限制），并赞扬了`np.einsum`的显式且强大的基于索引的方法。最终，文章认为NumPy的设计，特别是其对广播的依赖，未能提供一种连贯且直观的方式来处理数组，导致代码难以编写、阅读和维护。作者认为NumPy的设计不允许基本的编程抽象——解决简单问题，然后将解决方案用作构建更复杂问题的构建块。自注意力示例突出了需要以复杂的方式重写代码以进行矢量化操作。

---

## 59. 用于 Elixir 的 Lua

**原文标题**: Lua for Elixir

**原文链接**: [https://davelucia.com/blog/lua-elixir](https://davelucia.com/blog/lua-elixir)

Lua Elixir 库首个稳定版本发布 (v0.1.0)

本文宣布 Lua Elixir 库的首个稳定版本 (v0.1.0) 已在 hex.pm 上发布。该库允许直接在 BEAM VM 上执行沙盒化的 Lua 程序，利用底层 Luerl 库（一个用 Erlang 实现的 Lua 解析器、编译器和运行时）。与嵌入 C Lua 运行时不同，这是一个完整的 Lua 5.3 实现。

Lua Elixir 库通过改进的错误消息和完善的文档增强了 Luerl。主要功能包括使用 `deflua` 宏以 Elixir API 扩展 Lua 的能力、使用 `~LUA` sigil 进行编译时语法验证以及全面的文档。

该库最初由 TV Labs 开发，用于执行任意代码，以便针对流媒体设备进行集成测试。它作为他们的拖放式自动化构建器的编译目标，无需外部虚拟机即可实现基于视觉的测试。

本文还介绍了 Robert Virding 创建 Luerl 的背景，他将其作为在 BEAM 上实现命令式语言的实验。未来的计划包括将 Elixir Lua 库合并回 Luerl，以创建 2.0.0 版本，其中包含改进的错误消息、文档和堆栈跟踪，以及增强的沙盒和生态系统集成。欢迎感兴趣的开发者做出贡献。

---

## 60. Git: 将文件从一个仓库移动到另一个仓库并保留历史记录 (2021)

**原文标题**: Git: Move files from one repo to another with history (2021)

**原文链接**: [https://vivekdhami.com/posts/git-move-repo-files-with-history/](https://vivekdhami.com/posts/git-move-repo-files-with-history/)

本文介绍了如何使用`git filter-repo`命令将文件或文件夹从一个Git仓库移动到另一个Git仓库，同时保留其提交历史的指南。作者强调了旧方法（如`git filter-branch`和打补丁）的缺点，并提倡使用`git filter-repo`作为一种更简洁高效的替代方案。

该过程包括三个主要步骤：

1. **清理源仓库：** 使用`git filter-repo`，您可以使用`--path`选项仅包含所需的文件/文件夹，或者使用`--path`和`--invert-paths`排除特定的文件/文件夹。此步骤应在本地分支上完成，以避免影响原始仓库。

2. **将源仓库作为远程仓库添加到目标仓库：** 在目标仓库中，使用`git remote add`将源仓库添加为远程仓库。然后，使用`git fetch`从远程源获取更改，并创建一个指向远程分支的新分支。最后，将新创建的分支与所需的目标分支合并，由于仓库具有不同的历史记录，因此使用`--allow-unrelated-histories`标志。

3. **清理：** 使用`git remote rm`删除与源仓库的远程连接，并使用`git branch -d`删除临时合并分支。

本文还提到需要单独安装`git filter-repo`，并引导读者访问该项目的GitHub仓库以获取安装说明，尤其是在Windows上。提供的代码片段说明了每个步骤中使用的命令。

---

## 61. 改进海军舰艇采购

**原文标题**: Improving Naval Ship Acquisition

**原文链接**: [https://www.construction-physics.com/p/fixing-naval-ship-acquisition](https://www.construction-physics.com/p/fixing-naval-ship-acquisition)

本文提出对美国海军舰艇采购流程的改革，以解决成本超支和工期延误问题。作者认为，海军目前复杂的多用途舰艇设计和外包设计流程效率低下，并导致诸多问题。

主要建议包括：

1.  **专注于更简单的舰艇：** 从复杂的多用途舰艇转向具有更窄、更集中的用例的更简单设计。 例如，精简版护卫舰、专用导弹驱逐舰和专门的弹道导弹防御平台。 这将提高可生产性并降低成本。
2.  **内部设计：** 通过大幅扩充NAVSEA的海军建筑师队伍，将舰艇设计带回内部。 将设计外包给第三方承包商会导致专业知识流失和效率低下。 从历史上看，内部设计更成功。
3.  **生产前完成设计：** 避免在设计基本完成之前开始舰艇建造，以防止因建造过程中的设计变更而导致成本高昂的返工。

文章认为，这些改变将带来更经济实惠、建造速度更快、能力更强的海军舰艇。 他们指出了过去更简单的舰艇设计的成功案例，例如佩里级护卫舰和T-AGOS级监视船。 通过采用更简单的设计和内部专业知识，海军可以提高其造船效率并维持一支强大的舰队。

---

## 62. 当加密完美运行却依然失败时

**原文标题**: When encryption works perfectly and still fails

**原文链接**: [https://digitalseams.com/blog/when-encryption-works-perfectly-and-still-fails](https://digitalseams.com/blog/when-encryption-works-perfectly-and-still-fails)

博比·陈的文章《当加密完美运行却依然失败》认为，尽管现代密码学能有效保护数据，但安全问题往往因密钥管理不善而失败。文章承认了常见的密码学威胁，如可能破解加密算法的数学突破、密码分析以及侧信道攻击等实现层面的攻击。

然而，核心论点是，与密钥管理方面的失败相比，这些技术挑战并不那么重要。作者以国家安全顾问迈克·沃尔兹意外地将一名记者添加到加密群聊为例来说明这一点。即使采用强大的端到端加密，授予未经授权的密钥访问权限也会损害安全性。

作者介绍了“基斯纳定律”，该定律指出密码学将问题转化为密钥管理问题，而密钥管理问题更难解决。文章强调了密钥管理问题，例如在授予访问权限前验证身份、控制密钥生成以及通过撤销或轮换处理密钥泄露。这些问题经常被忽视，并且比密码学本身更容易被利用。现实中的违规行为通常涉及利用密钥管理漏洞，例如网络钓鱼攻击，而不是直接破解加密。

陈总结说，密钥管理不如密码学成熟，并且与上下文有关。因此，安全团队应该关注谁管理加密密钥，而不是仅仅依赖于加密本身的强度。

---

## 63. Show HN: Undetectag，用AirTag追踪被盗物品

**原文标题**: Show HN: Undetectag, track stolen items with AirTag

**原文链接**: [https://undetectag.com/](https://undetectag.com/)

Undetectag：一款旨在更有效地追踪被盗物品的Apple AirTag配件。其核心承诺是显著降低小偷发现并移除AirTag的可能性，声称可降低95%。广告强调Undetectag可用于保护汽车、船只、自行车、摩托车、行李箱和背包等贵重物品免遭盗窃。着陆页引导用户“发现”更多关于该产品的信息，并提供联系方式。本质上，它是AirTag配件的营销材料，旨在提高其隐蔽性和追踪被盗物品的效率。

---

## 64. 重构 Clojure

**原文标题**: Refactoring Clojure

**原文链接**: [https://www.orsolabs.com/post/refactoring-clojure-1/](https://www.orsolabs.com/post/refactoring-clojure-1/)

本文演示了一个用于生成马尔可夫文本的Clojure代码的重构过程。起点是`markov-data`和`sentence`函数的一个简洁但难以阅读的实现。

重构优先考虑可读性和可维护性，同时保留原始功能。作者强调了特征测试的重要性，以确保在重构过程中行为不变，并参考了Michael Feathers的《修改代码的艺术》。

本文提供了几个用于`markov-data`的特征测试，`markov-data`将文本字符串转换为表示马尔可夫链概率的映射。然后，使用`reduce`重写原始的`markov-data`，以便更清晰地处理句子和单词，从而产生更模块化的`process-sentence`函数。

类似地，为`sentence`函数编写了特征测试，包括处理从马尔可夫数据生成句子时固有的随机性。原始的`sentence`函数从`loop`结构重构为具有多个元数的递归函数。这通过使用更长的变量名和惯用的Clojure向量操作实践来提高可读性。

重构后的代码稍长，但被认为更具可读性和可维护性，代表了一次成功的重构结果。作者还提供了相关资源的链接，包括Adam Bard的《编写更友好的Clojure》和关于马尔可夫文本生成器的信息。

---

## 65. 人

**原文标题**: Human

**原文链接**: [https://quarter--mile.com/Human](https://quarter--mile.com/Human)

这篇题为“Human”的“文章”，本质上是一个网页页眉或导航元素。它非常简洁，包括：

*   **标题：**“Human”
*   **导航链接：**“写作”，“订阅”和“联系方式”。
*   **分隔符：** 一行星号，表示页面上的划分。

没有实际的文章内容可供总结。它仅仅是一个标题和基本的导航，暗示该页面可能包含写作（可能是文章或博客帖子）、订阅选项和联系方式，所有这些都围绕着“Human”这个广泛的主题。

---

## 66. 停止使用REST进行状态同步 (2024)

**原文标题**: Stop using REST for state synchronization (2024)

**原文链接**: [https://www.mbid.me/posts/stop-using-rest-for-state-synchronization/](https://www.mbid.me/posts/stop-using-rest-for-state-synchronization/)

本文认为，REST并不适合现代Web应用的状态同步需求，导致了大量的样板代码、潜在的bug以及繁琐的开发流程。作者通过一个常见场景——一个文本输入框更新数据库——来说明这个问题。使用REST需要管理数据获取、错误处理、加载指示器，并确保数据一致性，从而导致代码复杂。

作者指出了使用REST实现此目的的几个问题：当多个请求同时进行时可能出现的竞态条件（可能用旧值覆盖数据），不正确的加载指示器逻辑，以及跨应用多个实例缺乏自动更新。

虽然存在诸如在请求期间禁用提交按钮或对请求进行排队等解决方案，但它们会对用户体验产生负面影响或引入延迟。服务器发送事件可以解决多实例问题，但需要大量的服务器端工作。

作者强调，核心问题是将*状态转移*协议（REST）用于*状态同步*问题。用其他状态转移协议（如gRPC）替换REST并不能解决根本问题。

本文重点介绍了新兴技术，如Automerge、Yjs、Braid和Electric SQL，它们旨在提供适当的状态同步机制，通常基于CRDT。作者希望状态同步技术能够成熟到开发者不再需要在REST之上构建临时的、充满bug的解决方案。即使在具有合理互联网连接的常见客户端-服务器设置中，适当的状态同步机制也将非常有用。

---

## 67. 互联网遗迹

**原文标题**: Internet Artifacts

**原文链接**: [https://neal.fun/internet-artifacts/](https://neal.fun/internet-artifacts/)

无法访问文章链接。

---

## 68. Jetrelay：500行代码实现的高性能ATproto Relay

**原文标题**: Jetrelay: A high-performance ATproto relay in 500 LOC

**原文链接**: [https://www.asayers.com/jetrelay/](https://www.asayers.com/jetrelay/)

本文详细介绍了“jetrelay”的创建过程，这是一个用大约 500 行代码构建的高性能 ATproto relay，旨在高效地将 Bluesky 的“firehose”（网络状态变化的流）重新广播给大量客户端。挑战在于处理高事件速率（300-500 个事件/秒）和大量的并发客户端。

作者利用了两个关键技术：多播和回填。由于所有客户端都发送相同的数据，因此该解决方案采用文件和游标设计，使用 `sendfile()` 将数据直接从内核的页面缓存传输到客户端套接字，绕过用户空间并实现高效的写入批处理。

为了在不使用过多线程的情况下处理大量客户端，本文使用了 `io_uring`，这是一种 Linux 机制，允许在单个系统调用中向内核提交多个 `sendfile()` 操作（用 `splice()` 模拟），完成事件指示传输完成。 这将系统调用的数量与客户端数量分离，从而最大限度地提高效率。

该 relay 还通过维护一个将时间戳映射到文件偏移量的 `BTreeMap` 索引来处理新的客户端连接，使客户端能够指定其在 feed 中的初始位置。 最后，旧数据通过 `fallocate()` 从文件中“打孔”来丢弃，释放磁盘空间而不会中断已连接的客户端，只需要删除相关的索引条目并可能断开滞后的客户端的连接。

在环回上的测试实现了 24 Gbps 的吞吐量，可服务 2 万个客户端。 在 Linode VM 上的真实网络测试饱和了 10 Gbps 的连接，同时服务了近 9000 个客户端。

---

## 69. 用SQL计算MRR

**原文标题**: Calculating MRR in SQL

**原文链接**: [https://www.definite.app/blog/stripe-mrr-calculation](https://www.definite.app/blog/stripe-mrr-calculation)

本文概述了一种从原始Stripe数据计算每月经常性收入(MRR)的方法，重点介绍了沿途遇到的挑战和解决方案。 首先解释了使用派生的Singer Stripe tap提取数据并将数据加载到DuckDB数据仓库的过程。

然后，作者详细介绍了直接从Stripe数据计算MRR时常见的陷阱，包括：

1.  Subscriptions对象仅提供最新状态，不提供历史变更。 解决方案是使用历史发票。
2.  不可靠的发票期间开始和结束日期。 解决方案是使用发票明细项目的期间日期。
3.  发票明细项目包含非经常性费用。 解决方案是筛选`type = subscription`的明细项目。
4.  折扣未计入发票明细项目金额。 解决方案是关联折扣并将其扣除。
5.  非每月计费的订阅需要标准化。 解决方案是将收入分摊到整个账单周期。

本文然后提供了分步SQL转换过程：

1.  收集相关的发票明细项目并扣除折扣。
2.  通过将收入分摊到各个月来标准化季度和年度计划。
3.  将标准化的每月收入与时间序列数据集连接，以解决订阅中的空白。
4.  计算MRR指标，例如新增MRR、流失、扩展、收缩和重新激活。

作者最后指出，这种方法特定于他们的用例，但可以进行调整，并建议使用他们的产品“Definite”来避免手动计算MRR的复杂性。

---

## 70. AlphaEvolve：基于Gemini的用于设计高级算法的编码代理

**原文标题**: AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms

**原文链接**: [https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/](https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)

AlphaEvolve：利用进化编码革新算法设计的新型人工智能代理

AlphaEvolve是一种由Gemini模型驱动的新型人工智能代理，通过一种进化编码方法革新了算法设计。它结合了大型语言模型的创造性问题解决能力和自动化评估器，使其能够发现和优化各种应用领域的算法。

AlphaEvolve已经在谷歌的基础设施中产生了重大影响，包括改进数据中心调度、协助TPU硬件设计以及增强AI训练和推理。其数据中心调度启发式算法回收了谷歌0.7%的计算资源。它还优化了底层GPU指令，使FlashAttention内核的实现速度提高了32.5%。

除了实际应用之外，AlphaEvolve还在推动数学和算法发现的边界。它发现了新的矩阵乘法算法，其中包括一个用于4x4复值矩阵的算法，超越了1969年的基准。它还解决了50多个未解决的数学问题，在大多数情况下重新发现了最先进的解决方案，并在20%的情况下改进了现有解决方案，包括为11维空间中的亲吻数问题建立了新的下限。

谷歌计划为学术用户推出早期访问计划，并正在探索更广泛的可用性。由于其通用性，AlphaEvolve可以应用于更广泛的领域，包括材料科学、药物发现和可持续性。

---

## 71. Show HN: Muscle-Mem，AI 代理的行为缓存

**原文标题**: Show HN: Muscle-Mem, a behavior cache for AI agents

**原文链接**: [https://github.com/pig-dot-dev/muscle-mem](https://github.com/pig-dot-dev/muscle-mem)

Muscle-Mem：一个用于优化AI Agent性能的Python SDK，通过缓存和重放工具调用模式来处理重复性任务。这种“行为缓存”允许Agent绕过LLM调用来处理先前遇到的场景，从而提高速度、减少变异性并降低Token成本。

该SDK不依赖于特定的Agent框架；相反，它封装了一个现有的Agent，拦截工具调用并将它们记录为轨迹。当接收到任务时，引擎会检查是否之前见过该环境。如果“缓存命中”，则会重放存储的轨迹；如果“缓存未命中”，则会调用原始Agent，并收集工具调用事件以更新缓存。

Muscle-Mem的核心在于使用“检查”进行缓存验证。这些检查包括捕获和比较回调，它们提取相关的环境特征并确定当前环境是否与缓存的环境匹配，从而确保执行给定操作的安全性。可以使用`@engine.tool`装饰器将检查实现为附加到工具的预检查或后检查。

本文提供了一个基本代码示例，展示了Engine、Tool装饰器和Check功能，以及GitHub上提供的更实用的计算机使用Agent实现。作者鼓励提供反馈，并邀请读者加入Muscle Mem Discord，测试该存储库并为其点亮星星。

---

## 72. Logitloom：探索指令和基础模型上的token轨迹树

**原文标题**: Logitloom: Explore token trajectory trees on instruct and base models

**原文链接**: [https://github.com/vgel/logitloom](https://github.com/vgel/logitloom)

Logitloom：用于探索指令和基础模型上的令牌轨迹树（looming）的工具。它允许用户可视化和交互模型从给定提示中可能生成的令牌序列。

要使用Logitloom，用户需要支持模型的API密钥，例如deepseek-v3（聊天模型）或Hyperbolic的405-base（基础模型）。这些API需要支持助手预填充（对于聊天模型）和对数概率。该工具可在vgel.me/logitloom上找到。

用户可以使用诸如“深度”（要扩展的令牌数量）和“最大子节点数”（要考虑的令牌选项数量）之类的设置来控制树的扩展。“Top P”通过仅考虑达到一定概率的子节点来限制分支。

树节点显示令牌、其概率和对数概率。用户可以“添加到预填充”以从特定路径继续生成，或“从此处扩展”以探索更多分支。

Logitloom在UTF-8编码方面存在已知问题。该工具目前未授权。开发使用Bun完成，文档提供了有关服务和捆绑应用程序的说明，包括针对供应商OpenAI库的解决方法。

---

## 73. 图着色的最快方法

**原文标题**: The Fastest Way yet to Color Graphs

**原文链接**: [https://www.quantamagazine.org/the-fastest-way-yet-to-color-graphs-20250512/](https://www.quantamagazine.org/the-fastest-way-yet-to-color-graphs-20250512/)

一种近乎最优的图着色算法：数十年停滞后迎来突破

---

## 74. 并行函数式数组语言比较：编程与性能

**原文标题**: Comparing Parallel Functional Array Languages: Programming and Performance

**原文链接**: [https://arxiv.org/abs/2505.08906](https://arxiv.org/abs/2505.08906)

这篇题为“并行函数式数组语言比较：编程与性能”的 arXiv 文章，比较了五种函数式数组语言——Accelerate、APL、DaCe、Futhark 和 SaC——在设计、实现、表达能力和性能方面的表现。作者研究了这些语言如何在实现良好性能和可移植性的同时，促进低成本的并行编程。

该研究使用四个具有挑战性的基准测试——N 体模拟、多重网格、快速凸包和 Flash Attention——来展示这些语言在各种应用领域和并行计算模型中的表达能力。作者认为，通过抽象掉特定于架构的细节，函数式数组代码相比于手工优化的实现，具有简洁性和清晰性。这允许单源代码生成用于多核 CPU 和 GPU 的可执行文件。

性能评估是在一个 32 核 AMD EPYC 7313 和一个 NVIDIA A30 GPU 上，针对四个基准测试的 39 个实例进行的。作者深入研究了每种语言在每种架构上的性能优势和劣势的原因。结果表明，成熟的函数式数组语言有可能与传统的、高度优化的技术相媲美。此外，作者强调，与传统方法相比，函数式数组代码可以更容易地移植和优化到新的并行架构上。

---

## 75. 一个小型的玻尔兹曼机

**原文标题**: A Tiny Boltzmann Machine

**原文链接**: [https://eoinmurray.info/boltzmann-machine](https://eoinmurray.info/boltzmann-machine)

本文介绍了玻尔兹曼机 (BMs)，一种用于无监督学习的生成式人工智能模型。 玻尔兹曼机无需明确指令即可从数据中学习模式，并能生成与训练数据相似的新数据。 玻尔兹曼机是一种具有可见（输入/输出）神经元和隐藏神经元的神经网络，这些神经元通过可以是正或负的权重连接。

本文将所有神经元相互连接的通用玻尔兹曼机与受限玻尔兹曼机 (RBM) 进行了对比。 由于RBM限制了可见层和隐藏层内的连接，因此训练速度更快。

玻尔兹曼机是一种基于能量的模型。 能量函数 E(v,h) 根据权重 (w) 和偏差 (b 和 c) 定义可见 (v) 和隐藏 (h) 单元配置的能量。 在训练过程中，调整权重以降低训练样本的能量，从而有效地学习概率分布 P(v)。 然后使用吉布斯采样从这种学习到的分布中生成新数据。

RBM 的训练过程利用对比散度。 它涉及将可见单元钳制到数据、采样隐藏单元、再次采样可见单元（重建）、重新采样隐藏单元，最后更新权重。 本文提供了对比散度算法的数学推导，包括权重和偏差更新规则。 提供了一个模拟器来演示 RBM 训练过程和收敛。

---

## 76. 小波树：简介 (2011)

**原文标题**: Wavelet Trees: An Introduction (2011)

**原文链接**: [https://www.alexbowe.com/wavelet-trees/](https://www.alexbowe.com/wavelet-trees/)

本文介绍了小波树，一种用于高效回答大型字母表序列上的秩查询的数据结构。小波树将字符串组织成位向量的层次结构，允许在 O(log₂A) 时间内回答秩查询，其中 A 是字母表大小。

本文解释了如何通过递归地将字符串的字母表编码成位向量来构建小波树。树的每一层都将字母表分成两半，将前半部分编码为 0，后半部分编码为 1。对于每个子树，重复此过程，直到只剩下一个或两个符号。生成的位向量可以有效地存储，甚至可以使用像 RRR 序列这样的技术进行压缩。

本文还描述了如何在小波树上执行秩查询。通过在每一层的位向量上使用二元秩查询，该算法遍历树以找到直到给定位置的特定符号的正确计数。作者将*为什么*这样有效的原因解释留给读者作为练习。

作者强调了小波树在基于后缀数组的模式搜索中的潜在应用，并提到了现成的实现，如 Francisco Claude 的 libcds。最后，它为那些寻求更深入了解小波树的人提供了进一步阅读的列表。

---

## 77. 更了解风险区域危险性的人更可能接受收购。

**原文标题**: People understanding the dangers of risky areas more likely to accept buyouts

**原文链接**: [https://phys.org/news/2025-05-people-health-dangers-high-areas.html](https://phys.org/news/2025-05-people-health-dangers-high-areas.html)

本文探讨了一项在德克萨斯州盖莱纳帕克进行的研究，该镇拥有大型石化联合企业。研究考察了居民接受房屋回购作为解决环境健康风险方案的意愿。这项由德克萨斯农工大学研究人员主导的研究，重点关注居住在工业场所附近、面临因污染而增加的癌症和呼吸道疾病风险的以西班牙裔为主的低收入人群。

研究发现居民对环境健康风险的理解与他们接受回购的意愿之间存在相关性。居住在高风险地区、有洪水历史且对污染高度关注的居民更可能考虑回购。这表明对环境危害的认知是影响他们决策的主要因素。

房屋回购计划涉及政府购买房产并资助高风险地区居民搬迁。虽然传统上用于自然灾害区域，但它们越来越多地被考虑用于具有极端环境危害的地区。该研究强调了这些计划作为解决环境健康风险的一种方式的潜力，尤其是在受影响严重的不成比例的社区中。

该研究还强调了社区参与在解决环境问题中的重要性。虽然承认样本量小和单点时间数据收集等局限性，但该研究为影响居民接受回购意愿的因素提供了有价值的见解，并强调需要进一步研究搬迁准备和长期结果。

---

## 78. 揭秘 Ruby：一切皆线程 (2024)

**原文标题**: Demystifying Ruby: It's all about threads (2024)

**原文链接**: [https://blog.papey.fr/post/07-demystifying-ruby-01/](https://blog.papey.fr/post/07-demystifying-ruby-01/)

本文揭秘 Ruby 的并发模型：进程、Ractor、线程和纤程。它解释了 Ruby 代码如何在进程 -> Ractor -> 线程 -> 纤程的嵌套结构中运行。

**进程**提供完全的内存隔离和真正的并行性，由操作系统管理，但资源消耗大且需要进程间通信。

**Ractor**是 Ruby 3 中引入的实验性特性，在单个 Ruby 进程中提供并行性。它们具有内存隔离（每个 Ractor 都有自己的 GIL），并使用消息传递进行通信，从而实现更安全的 CPU 密集型任务并行执行。

**线程**比进程更轻量级，在进程内共享内存，但受到 MRI Ruby 中的全局解释器锁 (GIL) 的限制，将真正的并行性限制为并发。它们适用于 I/O 密集型任务，但如果未仔细同步，则容易出现竞争条件。

**纤程**是最轻量级的并发机制，在单个线程中提供协同多任务处理。控制在纤程之间手动让出，使其成为构建生成器和协程的理想选择。

本文强调 Ractor 和纤程都是底层 API，并建议避免编写大量依赖于它们的代码。最后，概述了每种并发模型的权衡，突出了 Puma（线程）和 Unicorn（进程）Web 服务器方法之间的差异。

---

## 79. 浮点数比较 (2012)

**原文标题**: Comparing floating-point numbers (2012)

**原文链接**: [https://randomascii.wordpress.com/2012/02/25/comparing-floating-point-numbers-2012-edition/](https://randomascii.wordpress.com/2012/02/25/comparing-floating-point-numbers-2012-edition/)

本文《浮点数比较，2012版》探讨了比较浮点数是否相等时的复杂性和陷阱。作者 Bruce Dawson 强调，浮点运算本质上是不精确的，由于舍入误差以及编译器和 CPU 的差异，直接的相等性检查是不可靠的。

文章探讨了使用固定 epsilon 值（如 `FLT_EPSILON`）进行比较的局限性，因为它的有效性随着被比较数字的大小而变化很大。文章介绍了一种更好的替代方案“相对 epsilon 比较”，即将数字之间的差异与它们的大小进行比较。

文章的核心介绍了一种更强大的技术，即使用“最后一位单位”（ULP）。通过比较浮点数的整数表示，ULP 差异揭示了两个数字之间有多少个可表示的浮点数。 这种方法提供了对浮点值之间差异的更直观的理解。提供了 `AlmostEqualUlps` 函数的代码。

然后，作者深入研究了基于 ULP 的比较的细微之处，强调了它与相对 epsilon 比较的异同。 最后，Dawson 探讨了 ULP 的边缘情况，其中单个 ULP 差异可能代表很大的相对差异，例如将 FLT_MAX 与无穷大或零与最小的非正规数进行比较时。

---

## 80. AWS称英国需要更多核能以满足人工智能数据中心激增的需求。

**原文标题**: AWS says Britain needs more nuclear power to feed AI datacenter surge

**原文链接**: [https://www.theregister.com/2025/05/16/amazon_nuclear_power_britain/](https://www.theregister.com/2025/05/16/amazon_nuclear_power_britain/)

亚马逊云服务 (AWS) 首席执行官 Matt Garman 表示，英国需要投资更多核能，以为该国不断增长的人工智能数据中心供电。他警告说，如果不增加发电能力，这些数据中心的能源需求将使电网不堪重负。

包括 AWS、谷歌和微软在内的几家科技巨头正在扩大其在英国的数据中心规模，以支持人工智能发展，这得益于政府旨在加速数据中心建设的《人工智能机遇行动计划》。这种扩张引发了人们对人工智能基础设施日益增长的能源消耗的担忧。

国际能源署 (IEA) 预测，到 2030 年，全球数据中心能源消耗将增加一倍以上，而英国国家电网估计，未来十年英国的能源消耗将增加 500%。作为回应，政府成立了人工智能能源委员会，以解决能源基础设施挑战。

虽然电网升级是重点，但 Garman 认为，核能是数据中心的“绝佳解决方案”，因为它具有零碳排放和 24/7 全天候供电的优势。然而，与天然气发电厂相比，新建核电站需要更长的时间。 欣克利角 C 核电站于 2017 年开工建设，预计到 2030 年才能投入运营。Canalys 分析师 Elsa Nightingale 指出，人工智能的能源需求是迫切的，而核电项目则需要很长的准备时间。

一些公司正在探索小型模块化反应堆 (SMR)，但预计这项技术在 2030 年之前还无法准备就绪。英国政府能源安全和净零部门 (DESNZ) 表示，其清洁能源行动计划旨在支持像数据中心这样的能源密集型产业，并改革电网连接流程。

---

## 81. 预订可用会议室的恶意服从

**原文标题**: Malicious compliance by booking an available meeting room

**原文链接**: [https://www.clientserver.dev/p/malicious-compliance-by-booking-an](https://www.clientserver.dev/p/malicious-compliance-by-booking-an)

本文讲述了拉里·佩奇在2011年试图改革谷歌会议文化的尝试，旨在提高效率并减少时间浪费。佩奇实施了多项规则，包括限制会议规模、强调参与者贡献以及将一小时会议缩短至50分钟以便休息。谷歌日历团队随后实施了25分钟和50分钟会议的默认设置。

然而，该政策在实践中基本失败，人们经常超时进行超过50分钟的会议。纽约办事处的一个工程团队利用了这种情况。他们注意到由于默认的50分钟预订，会议室通常在每个小时结束时有10分钟的空隙，因此他们开始预订这些10分钟的空隙用于他们的站立会议。

这导致了尴尬的对抗，站立团队会打断正在进行的会议，并引用日历预订作为他们有权在最后10分钟使用会议室的证据。本文将其强调为“恶意服从”的一个例子，即员工在技术上遵守了新的会议政策，但以破坏性的方式使用它。作者对参与这种做法的团队的动机表示钦佩和好奇。

---

## 82. 常见的MVP错误：如何在不过度构建的情况下巧妙构建

**原文标题**: Common MVP mistakes: How to build smart without overbuilding

**原文链接**: [https://www.erlang-solutions.com/blog/common-mvp-mistakes-how-to-build-smart-without-overbuilding/](https://www.erlang-solutions.com/blog/common-mvp-mistakes-how-to-build-smart-without-overbuilding/)

本文强调了战略性地构建最小可行产品 (MVP) 的重要性，以便在不过度构建的情况下验证想法。文章指出，MVP 应该提供真正的价值，从而能够基于用户反馈进行快速学习和调整，同时向投资者展示效率。

文章警告了一些常见的 MVP 错误，例如过度构建（预先添加太多功能）、选择错误的技术堆栈以及忽视安全性和代码质量。过度构建会减慢开发速度、增加成本并让用户感到困惑。错误的技术堆栈会阻碍迭代和可扩展性。忽视安全性和代码质量，尤其过度依赖人工智能生成的代码（“感觉编码”），会产生技术债务、不稳定性和漏洞。

一个聪明的 MVP 是快速、专注和灵活的。它优先解决一个问题，传递清晰的价值，并根据反馈进行迭代。它还必须是稳定的、安全的，并建立在允许未来增长的基础上。文章总结说，将速度与策略相结合可以更快地学习、改进和实现更强的增长，最终有效地验证想法、吸引投资者和收集反馈。

---

## 83. 标量选择反模式

**原文标题**: The Scalar Select Anti-Pattern

**原文链接**: [https://matklad.github.io/2025/05/14/scalar-select-aniti-pattern.html](https://matklad.github.io/2025/05/14/scalar-select-aniti-pattern.html)

本文描述了异步事件驱动服务中的“标量选择反模式”，并以 LSP 服务器为例进行了说明。 其核心问题是使用单个 `select` 操作（或使用 `merge` 的等效操作）来一次选择并处理来自多个输入流（例如，文件系统更改、编译器输出、LSP 请求）的事件。

作者认为，这种方法忽略了在处理单个事件时，可能会有多个事件变得可用。 这种疏忽阻碍了潜在的优化，例如：

*   **优先级排序：** 以特定顺序处理事件（例如，先写后读）。
*   **选择性反压：** 丢弃某些类型的请求以管理负载。
*   **消除：** 丢弃过时或冗余的请求。
*   **合并：** 将多个类似请求合并为单个、更高效的操作（例如，合并增量文件修改）。

解决方案是在处理之前批量处理传入事件。 服务不应一次处理一个事件，而应将所有可用事件收集到一个批次中，然后在处理该批次之前应用优化。 提供的 `batch_stream` 函数说明了如何实现这一点，即等待至少一个事件，然后立即拉取所有其他可用事件。 这种方法允许系统更有效地处理不断增加的负载。 作者提倡在消息传递系统中采用批处理而不是单次处理。

---

## 84. HDR 到底是什么？

**原文标题**: What is HDR, anyway?

**原文链接**: [https://www.lux.camera/what-is-hdr/](https://www.lux.camera/what-is-hdr/)

这篇文章实质上只是一个标题：“HDR到底是什么？”以及在内容中对这个问题的重复。

因此，总结如下：

这篇文章提出了问题“HDR到底是什么？”。它没有提供任何关于HDR的信息或解释。这篇文章的唯一目的似乎是介绍高动态范围（HDR）这个话题，并引发用户对其定义和功能的好奇。

---

## 85. Dia – 早期评测

**原文标题**: Dia – An Early Review

**原文链接**: [https://www.fldr.zip/blog/dia-review](https://www.fldr.zip/blog/dia-review)

对Dia的早期评测：BCNY的AI原生浏览器

---

## 86. Linux交换表代码显示性能提升的潜力

**原文标题**: Linux Swap Table Code Shows the Potential for Performance Gains

**原文链接**: [https://www.phoronix.com/news/Linux-Swap-Table-Patches](https://www.phoronix.com/news/Linux-Swap-Table-Patches)

腾讯工程师宋凯锐提出的名为“Swap Table”的Linux内核补丁系列旨在显著提升交换子系统的性能和效率。此前，内核开发者已就集成交换缓存和交换映射功能进行了讨论。

Swap Table的主要目标是相比现有交换代码，实现更低的内存占用、更高的性能、动态的交换分配和增长以及更大的可扩展性。补丁系列的初步结果令人鼓舞，显示出在各种工作负载下，4K和mTHP页都能获得20-30%的潜在性能提升。此外，空闲内存占用已经降低，并且随着开发的进行，平均内存消耗还有可能进一步降低。这些补丁还解决了并清理了现有SWAP子系统中的历史遗留问题。

这个包含27个补丁的系列目前正在审查中，它代表了Linux内存管理方面一个潜在的重大进步。希望Swap Table或其改进版本能在不久的将来被集成到主线Linux内核中。

---

## 87. 大型语言模型在多轮对话中迷失方向

**原文标题**: LLMs get lost in multi-turn conversation

**原文链接**: [https://arxiv.org/abs/2505.06120](https://arxiv.org/abs/2505.06120)

Laban等人于2025年5月提交的arXiv论文(arXiv:2505.06120)“LLMs在多轮对话中迷失方向”研究了大型语言模型(LLMs)在多轮对话环境下的表现，并将其与单轮任务进行了比较。作者强调，虽然LLMs通常在单个、完全指定的指令上进行评估，但现实世界的互动涉及多轮对话，用户在其中完善他们的请求。

研究发现，在多轮对话中，LLMs在六项生成任务中的表现显著下降（平均下降39%），这影响了开放权重和封闭权重模型。通过对超过20万次模拟对话的分析，性能下降归因于能力的小幅下降以及可靠性的显著增加。 identified 的核心问题是，LLMs倾向于做出过早的假设并生成早期解决方案，随后当这些初始解决方案被证明不正确时，就会“迷失方向”，无法在对话中有效地恢复。

本质上，该论文表明，LLMs难以在整个多轮对话中保持上下文并有效地调整其策略，从而导致与更简单的单轮互动相比，性能下降。

---

## 88. 重新思考我处理命令行参数的方式 (替代 getopt)

**原文标题**: Rethinking How I Deal With CLI Arguments (replacing getopt)

**原文链接**: [https://xnacly.me/posts/2025/rethinking-cli-arguments-and-substituting-getopt/](https://xnacly.me/posts/2025/rethinking-cli-arguments-and-substituting-getopt/)

本文详细描述了作者在使用 `getopt.h` 在字节码解释器项目中进行命令行参数解析时遇到的挫折，并提出了一个自定义解决方案 `6cl` 来解决这些缺陷。

作者批评 `getopt.h` 需要手动创建帮助/使用页面、冗余的标志定义、通过全局状态访问的无类型参数、缺少默认值以及硬编码的选项前缀。

`6cl` 旨在通过以下方式克服这些问题：

*   自动生成帮助和使用页面。
*   使用单个标志定义。
*   对标志选项进行类型化（字符串、布尔值、字符、整数、长整数、浮点数、双精度浮点数），并进行验证和设置默认值。
*   允许自定义选项前缀。

本文介绍了 `6cl` 的 API，其灵感来自 Go 的 `flag` 包和 Google 的 `gflag`，重点在于人体工程学和类型安全。它详细说明了如何在一个结构体中定义带有名称、短名称、类型、描述和默认值的标志。`SixParse` 函数处理实际的解析，并且本文提供了一个如何在掷骰子程序中使用 `6cl` 的示例。

作者还演示了如何生成帮助和使用页面，重点介绍了使用 `print_flag` 来格式化输出，并展示了长短标志名称的示例。本质上，本文提出了一个问题、一个解决方案以及该解决方案的实际演示。

---

## 89. 无人问津之地 (2016)

**原文标题**: Welcome to the land that no country wants (2016)

**原文链接**: [https://www.theguardian.com/world/2016/mar/03/welcome-to-the-land-that-no-country-wants-bir-tawil](https://www.theguardian.com/world/2016/mar/03/welcome-to-the-land-that-no-country-wants-bir-tawil)

在《欢迎来到无人之境》一书中，杰克·申克讲述了他和电影制作人奥马尔试图到达并可能声称比尔泰维勒的经历，比尔泰维勒是埃及和苏丹之间一小块两国都未声明主权的土地。受其“无人区”地位的启发，他们设想将其变成激进思想的避风港、颠覆者的发射台，以及关于边界和主权的概念性博览会。

然而，他们准备不足的冒险充满了不幸。他们缺乏调查研究导致了财务困境、被苏丹情报部门逮捕，并最终依赖于一位名叫奥拜及其侄子杰多的可疑的狩猎者来提供交通。申克将他们的经历与耶利米·希顿的经历进行了对比，后者是一位成功的美国父亲，他前往比尔泰维勒并插上了一面旗帜，以使他的女儿成为“公主”，并突出了希顿因被认为是新殖民主义而面临的争议。

申克强调了边界的微妙性和篡改边界可能产生的意外后果。虽然他们最初的目标是批判武断的边界，但他们自己“声称”比尔泰维勒的尝试揭示了此类行动的复杂性和潜在陷阱，说明即使是看似无人认领的领土也嵌入了复杂的政治和历史动态之中。最终，这篇文章是对无人之境浪漫魅力的反思，以及逃脱历史和权力结构重量的挑战。

---

## 90. 昂菲姆的世界：历史上的儿童艺术家

**原文标题**: Onfim's world: Child artists in history

**原文链接**: [https://resobscura.substack.com/p/onfims-world-medieval-child-artists](https://resobscura.substack.com/p/onfims-world-medieval-child-artists)

无法访问文章链接。

---

## 91. Show HN: 将技术文档进行 Min.js 风格压缩，用于 LLM 上下文

**原文标题**: Show HN: Min.js style compression of tech docs for LLM context

**原文链接**: [https://github.com/marv1nnnnn/llm-min.txt](https://github.com/marv1nnnnn/llm-min.txt)

本文介绍了一种名为`llm-min.txt`的新方法，用于压缩技术文档，以便在AI编码助手中与大型语言模型（LLM）一起使用。它通过提供库信息的高度结构化、精简的摘要，解决了AI的“知识截止”问题，其灵感来自`min.js`文件压缩概念。

`llm-min.txt`使用结构化知识格式（SKF），将信息组织成三个关键部分：DEFINITIONS（定义）、INTERACTIONS（交互）和USAGE_PATTERNS（使用模式）。与完整文档（`llm-full.txt`）相比，这种格式优先考虑机器可读性和高效解析，而不是人类可读性，从而显著减少token数量。文章声称可以实现90-95%的token减少。

该指南包括通过命令行或编程Python实现进行安装和使用的快速入门说明。它解释了设置Gemini API密钥以及使用推荐的Gemini模型（`gemini-2.5-flash-preview-04-17`）以获得最佳压缩的重要性。输出目录结构包含`llm-full.txt`、`llm-min.txt`以及至关重要的`llm-min-guideline.md`文件，该文件提供了SKF格式的解码说明。文章强调，指导文件对于AI正确解释压缩文档至关重要。

该工具旨在提高代码生成成功率，特别是对于当前LLM难以处理的库。它的工作原理是收集、清理和分割文档，然后使用多步骤AI分析管道来生成SKF清单。

---

## 92. 我潜入了企业等级制度（你也可以，但你会讨厌它）

**原文标题**: I Infiltrated the Corporate Caste System (and You Can Too, but You'll Hate It)

**原文链接**: [https://sonicdoomofthesouth.bearblog.dev/i-infiltrated-the-corporate-caste-system-and-you-can-too-but-youll-hate-it/](https://sonicdoomofthesouth.bearblog.dev/i-infiltrated-the-corporate-caste-system-and-you-can-too-but-youll-hate-it/)

作者讲述了他们在企业界，尤其是在科技行业中摸爬滚打的经历，他们发现这是一个令人沮丧且常常毫无意义的“等级制度”。他们用一些轶事来说明这一点，从他们因来自密西西比而被评判的旅社经历开始。他们观察到企业环境中也存在类似的偏见和肤浅，晋升似乎更多地取决于人脉、使用企业术语以及与正确的社交圈子保持一致，而不是实际能力。

作者批评了头衔膨胀、不必要的中层管理以及优先考虑外表和形象而非实际结果的普遍现象。他们感叹像他们未婚妻的家政服务这样真正的辛勤工作常常被低估，而肤浅的成就却在企业环境中得到回报。

他们强调了领导层逃避责任并窃取他人劳动成果的虚伪。他们看到尽管表现不佳却仍然获得晋升，这进一步巩固了他们对企业界是重视印象而非本质的看法。

最终，作者建议读者，如果他们真的想在这个世界取得成功，那就拥抱企业文化的表面现象——玩游戏，使用行话，并打造完美的在线形象。然而，他们也暗示这种成功是有代价的，牺牲了真实性和真正的技能来换取顺从和社交手腕。作者以一丝讽刺结束，表明他们也会玩这个游戏，即使他们觉得它很荒谬。

---

## 93. 哈佛法学院花27美元买了一份大宪章，是真迹。

**原文标题**: Harvard Law paid $27 for a copy of Magna Carta. It's an original

**原文链接**: [https://www.nytimes.com/2025/05/15/world/europe/harvard-law-magna-carta-original.html](https://www.nytimes.com/2025/05/15/world/europe/harvard-law-magna-carta-original.html)

二战后哈佛法学院以27.5美元购得的一份带水渍的手稿，已被确认为1300年《大宪章》的原始版本，而非之前认为的副本。 这一发现由两位英国学者大卫·卡彭特和尼古拉斯·文森特做出，卡彭特于2023年12月偶然发现了它。 这使其成为现存仅有的七份此类文件之一。

该手稿通过光谱成像技术进行鉴定，以增强肉眼无法察觉的细节。 目前的价值难以评估，但2007年一份类似的1300年《大宪章》以2130万美元的价格售出，突显了哈佛获得的惊人划算。 文森特教授还指出，该文件在哈佛面临巨大压力之际重新出现，增添了一层历史意义。

---

## 94. 为什么计算属于社会科学 (2020)

**原文标题**: Why Computing Belongs Within the Social Sciences (2020)

**原文链接**: [https://cacm.acm.org/research/why-computing-belongs-within-the-social-sciences/](https://cacm.acm.org/research/why-computing-belongs-within-the-social-sciences/)

本文认为，鉴于计算技术与人类及社会生活的日益紧密交织，它应被视为一门社会科学，而非纯粹的工程学科。作者以金融危机和Facebook的道歉时刻为例，指出与计算相关的问题不仅仅是技术性的，而是源于狭隘的世界观。

作者批评了计算领域内“凯旋主义”心态，在这种心态下，计算思维通常被视为一种普遍优越的方法，导致对既定的社会科学理论和方法的忽视。文章认为，这种心态导致了当前计算技术与社会之间紧张的关系。

作者提出，计算正在朝着社会科学的方法论和理论多元化方向发展，尤其是在数据科学和计算社会科学等领域，但学术界尚未充分认识到这种转变。文章强调了计算技术在权力关系中的作用，通过算法塑造社会规范和分配知识，从而使其具有内在的政治性。

文章最后建议学术界对计算进行三项转变：（1）拥抱来自其他学科的见解，（2）认识到伦理影响，以及（3）发展合作项目。这些变革旨在拓宽计算专业人员的视野，并更好地帮助他们应对技术带来的社会挑战。核心思想是转变心态，使其成为一门与社会科学有更多关联的领域。

---

## 95. 展示一下：我做了一个物联网设备，让我的家人知道我是否在开会

**原文标题**: Show HN: I’ve built an IoT device to let my family know when I’m in a meeting

**原文链接**: [https://nullonerror.org/2025/05/11/i-have-built-an-iot-device-to-let-my-family-know-when-i-am-in-a-meeting/](https://nullonerror.org/2025/05/11/i-have-built-an-iot-device-to-let-my-family-know-when-i-am-in-a-meeting/)

这个“Show HN”帖子介绍了Tabajara，一款物联网设备，旨在指示作者在家工作时是否正在开会。该设备通过在摄像头启用时点亮红色或蓝色LED面板，来防止被打扰。

Tabajara由一个运行Arduino框架的ESP32微控制器组成，该控制器连接到Wi-Fi，并利用mDNS通过“.local”主机名（esp32.local）轻松访问。ESP32托管一个HTTP服务器，该服务器接受对`/camera`端点的PATCH请求。这些请求携带一个JSON有效负载，指示摄像头是“on”还是“off”，从而触发LED面板相应地改变颜色。

为了自动化该过程，作者创建了一个Python守护程序，该程序定期查询Apple的API，以检测是否有任何摄像头处于活动状态。根据API响应，守护程序向ESP32设备发送PATCH请求，更新LED面板状态。

该设备简单而有效，利用mDNS、一个基本的HTTP服务器和一个Python守护程序，为家庭成员提供了一个方便的视觉提示。帖子中包含一个演示视频的链接以及GitHub上的源代码链接。

---

## 96. 新鲜事更新

**原文标题**: An Update on Fresh

**原文链接**: [https://deno.com/blog/an-update-on-fresh](https://deno.com/blog/an-update-on-fresh)

Fresh 2 更新：改进 Deno 平台和 JSR 导致延迟，目标 2025 年第三季度发布稳定版。Fresh 2 目前为 alpha 版本，已在 deno.com 和 Deno Deploy 生产环境中运行。 主要改进包括 Express/Hono 风格的 API、真正的异步组件以及用于自定义中间件的新插件系统。用户可使用 `deno run -Ar jsr:@fresh/init@2.0.0-alpha.33` 创建新项目，或使用 `deno run -Ar jsr:@fresh/update@2.0.0-alpha.33` 升级现有项目。

---

## 97. 澳大利亚首枚轨道级火箭顶部脱落，发射延期。

**原文标题**: The top fell off Australia's first orbital-class rocket, delaying its launch

**原文链接**: [https://arstechnica.com/space/2025/05/the-top-fell-off-australias-first-orbital-class-rocket-delaying-its-launch/](https://arstechnica.com/space/2025/05/the-top-fell-off-australias-first-orbital-class-rocket-delaying-its-launch/)

吉尔摩航天计划发射澳大利亚首枚轨道级火箭“埃里斯”号的计划被推迟，原因是有效载荷整流罩（即鼻锥）在最终发射准备期间因电气故障意外脱落。该事件发生在燃料加注之前，火箭和发射台均未出现人员伤亡或明显损坏。

“埃里斯”号火箭旨在将有效载荷运送到近地轨道，原定从昆士兰的一个私有航天发射场进行首次试飞。对于在发射过程中保护卫星的整流罩过早展开的原因正在调查中。吉尔摩公司已准备好替换整流罩，并计划在确定问题原因后进行安装。

此次发射本应标志着一个重要的里程碑，使“埃里斯”号成为首个进入轨道的全澳火箭发射器。该公司计划进行一次短暂而稳定的飞行，以收集测试期间的性能数据。此次延误是在此前因监管审批延误而造成的挫折之后发生的。吉尔摩公司表示失望，但仍对解决问题并尽快返回发射台持乐观态度。

---

## 98. SoCal Python社区重要成员"Goodwill"去世

**原文标题**: "Goodwill", key member of the SoCal Python Community has passed away

**原文链接**: [https://socalpython.org/in-memoriam-michael/](https://socalpython.org/in-memoriam-michael/)

本文是纪念迈克尔·里亚布什金（Michael Ryabushkin）的悼文集，他以“goodwill”为人所知，是南加州Python社区的关键成员和组织者，于2025年5月初去世。这些悼文突出了他对Python和开源社区，尤其是在南加州产生的重大影响。

人们铭记迈克尔是一位慷慨、乐于助人且支持他人的人，他投入了无数时间来组织活动、联系人们并指导有抱负的开发者。许多贡献者认为是他启动了他们在科技领域的职业生涯，提供了机会，并推动他们超越舒适区。他积极寻求帮助他人，经常将自己的时间、资源以及公司的赞助提供给各种活动和项目。

多位贡献者分享了个人轶事，阐述了他的善良、帮助陌生人的意愿，以及他独特、有时非常规的指导方式。他很擅长发现他人的潜力，并培养归属感。他以幽默、对教学的热情以及将人们团结在一起的能力而闻名。社区哀悼失去了一位领导者、导师和朋友，他留下了善良、慷慨和联系的持久遗产。

---

## 99. 大规模的迁徙已经开始了？

**原文标题**: The great displacement is already well underway?

**原文链接**: [https://shawnfromportland.substack.com/p/the-great-displacement-is-already](https://shawnfromportland.substack.com/p/the-great-displacement-is-already)

无法访问文章链接。

---

## 100. Ash框架 – 塑造你的领域，衍生其余

**原文标题**: Ash Framework – Model your domain, derive the rest

**原文链接**: [https://ash-hq.org/](https://ash-hq.org/)

Ash框架是一个Elixir后端框架，专注于提升开发者效率，它允许开发者对领域建模并派生出应用程序的其余部分。它提供了声明式工具，无需重复发明常见功能。它可以与Phoenix LiveView集成用于Web应用程序，或者为各种前端快速构建API。

Ash提供多种预设以启动项目，包括Web框架（Phoenix）、API格式（GraphQL、JSON:API）、数据层（PostgreSQL、SQLite、CSV）、身份验证方法（密码、魔法链接、API密钥、OAuth2）、AI集成（Tidewave、Ash AI）等选项，涵盖金融、自动化、安全、管理、UI和可观察性等领域。虽然许多功能是Ash的一部分，但有些依赖于外部软件包。

该框架强调PostgreSQL作为其首选数据库，因为它易于安装且具有广泛的支持。它鼓励用户从简入手，建议初学者单独尝试PostgreSQL或直接使用Phoenix LiveView。使用GraphQL或JSON:API可以快速构建API原型。提供了一个安装脚本，可以快速创建新项目。

最后，它重点介绍了Ash核心团队将出席的即将举行的活动，鼓励社区参与。

---

