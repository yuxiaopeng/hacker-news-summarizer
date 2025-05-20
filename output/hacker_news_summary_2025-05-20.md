# Hacker News 热门文章摘要 (2025-05-20)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 深度学习是应用拓扑学

**原文标题**: Deep Learning Is Applied Topology

**原文链接**: [https://theahura.substack.com/p/deep-learning-is-applied-topology](https://theahura.substack.com/p/deep-learning-is-applied-topology)

无法访问文章链接。

---

## 2. Show HN: 90年代.dev - 在网页上运行的游戏制作器

**原文标题**: Show HN: 90s.dev - game maker that runs on the web

**原文链接**: [https://90s.dev/blog/finally-releasing-90s-dev.html](https://90s.dev/blog/finally-releasing-90s-dev.html)

90s.dev 是一款全新的基于 Web 的游戏制作工具，灵感来源于 Pico-8、Tic-80 和 Love2D 等工具，旨在提供独特的开发体验。它拥有 320x180 的画布，在 Web Workers 中运行应用程序以确保安全和性能，并提供完整的 WebGL2 访问权限以实现 60 fps 的游戏。该平台允许从 GitHub 或 NPM 发布和加载应用程序。

一个关键特性是其创新的 GUI API，围绕自动布局系统、“refs”（用于观察视图属性的可观察指针）和“composites”（使用 JSX 的抽象/具体视图分离）构建。“refs”旨在避免手动设置值，通过在属性更改时自动更新。“Composites”允许用户覆盖默认的应用程序实现。

最初，该平台设计了一个共享文件系统驱动器 "net/"，但这种方法被取代，取而代之的是使用 CDN 从 NPM 或 GitHub 导入文件，从而创建了一种更方便的文件导入方式。

作者强调社区贡献的重要性，设想用户创建和分享应用程序、游戏资源和游戏。该平台包括用于像素艺术数据创建（绘画、精灵制作、地图制作）的内置应用程序，但作者希望社区能够贡献应用程序，并通过 GitHub 上的专用问题跟踪器、Wiki 和讨论论坛来促进分享。作者认识到最初的版本发布为时过早，并计划专注于添加更多可用的应用程序、示例游戏和教程。

---

## 3. 27000条龙和10000盏灯：GPU驱动的集群化前向渲染器

**原文标题**: 27000 Dragons and 10'000 Lights: GPU-Driven Clustered Forward Renderer

**原文链接**: [https://logdahl.net/p/gpu-driven](https://logdahl.net/p/gpu-driven)

本文详细介绍了一种高性能、GPU驱动的集群正向渲染器，能够在GTX 1070上以1080p分辨率和60fps以上的帧率渲染27,000个斯坦福龙模型和10,000个光源。其关键创新在于将渲染管线的大部分移至GPU，并使用间接多重绘制来最大限度地减少CPU绘制调用。

渲染器将对象数据存储在GPU上的“对象缓冲区”中，并使用由基于GPU的剔除过程填充的“绘制缓冲区”，通过仅绘制可见对象来提高性能。计算着色器基于AABB执行视锥体剔除，并使用原子计数器和子群投票压缩绘制列表，以实现高效的内存使用和空间局部性。

为了缓解过度绘制，渲染器实现了集群着色。视锥体被划分为集群，并根据其影响半径将光源分配给这些集群。这使得每个片段仅使用相关光源计算着色，从而减少了不必要的计算。本文解释了集群分配过程，将一种朴素方法与一种优化的、协作方法进行比较，该方法利用共享内存、哈希比较和压缩，从而显著提高了速度和内存使用率。在将10,000个光源分配给2,800个集群时，这种方法将分配时间从6毫秒缩短到1.1毫秒，并将内存使用量从3.1MB减少到164KB。

---

## 4. Show HN: 用 Janet 编写的 Windows 上的平铺窗口管理器

**原文标题**: Show HN: A Tiling Window Manager for Windows, Written in Janet

**原文链接**: [https://agent-kilo.github.io/jwno/](https://agent-kilo.github.io/jwno/)

Jwno是一款全新的、高度可定制的平铺式窗口管理器，适用于Windows 10和11，它使用Janet编程语言构建。其目标是将平铺式窗口管理的灵活性和强大功能带入Windows环境。

公告中强调的关键特性和信息包括：

*   **平铺功能：** Jwno允许用户自动以平铺布局排列应用程序窗口，从而改善工作流程和屏幕组织。
*   **可定制性：** 它是“高度可定制的”，这意味着用户可以根据自己的特定需求定制其行为。
*   **Janet语言：** 使用Janet构建，该语言以使用括号和提供REPL进行交互而著称。
*   **UI提示功能：** Jwno提供一个与UI元素交互的功能，可能提供高级窗口控制。
*   **开发中：** 文档仍在开发中。
*   **提供的资源：** 为新用户（功能、安装、教程）和有经验的用户（食谱、参考索引、开发指南）提供了链接，以及下载链接、问题跟踪器和源代码存储库（GitHub和Chisel）。

---

## 5. 罗宾：用于自动化科学发现的多智能体系统

**原文标题**: Robin: A multi-agent system for automating scientific discovery

**原文链接**: [https://arxiv.org/abs/2505.13400](https://arxiv.org/abs/2505.13400)

Robin：一种用于自动科学发现的新型多智能体系统

---

## 6. Show HN: Juvio – Jupyter的UV内核

**原文标题**: Show HN: Juvio – UV Kernel for Jupyter

**原文链接**: [https://github.com/OKUA1/juvio](https://github.com/OKUA1/juvio)

Juvio 是一款 Jupyter 内核，旨在提高 notebook 的可复现性、依赖感知能力和 Git 友好性。它通过三个关键特性实现这一目标：内联依赖管理、自动环境设置和 Git 友好的脚本式格式。

用户可以使用 `%juvio install` 魔术命令直接从 notebook 中安装 Python 包。这些依赖项随后会作为元数据存储在 notebook 本身中，符合 PEP 723 标准。

当打开 Juvio notebook 时，内核会自动创建一个临时的虚拟环境，并使用 `uv` 安装指定的依赖项，确保 notebook 以正确的包版本运行。

此外，Juvio 使用 `# %%` 标记将 notebook 转换为类似脚本的格式，从而更容易在 Git 中跟踪更改和管理版本。 这避免了通常与传统 Jupyter notebook 相关的混乱差异。

要使用 Juvio，用户需要安装 `juvio` 包和相关的 JupyterLab 扩展，并确保已安装 `uv`。 使用 Juvio 的主要优势包括：无需单独的锁文件即可简化依赖管理、保证 notebook 环境的可复现性，以及更清晰的 Git 差异以实现更好的版本控制。 它利用 `uv` 实现快速的包管理，并利用 PEP 723 标准实现内联依赖。

---

## 7. Ashby (YC W19) 招聘工程经理

**原文标题**: Ashby (YC W19) Is Hiring Engineering Managers

**原文链接**: [https://www.ashbyhq.com/careers?utm_source=hn&ashby_jid=933570bc-a3d6-4fcc-991d-dc399c53a58a](https://www.ashbyhq.com/careers?utm_source=hn&ashby_jid=933570bc-a3d6-4fcc-991d-dc399c53a58a)

Ashby (YC W19校友) 招聘工程经理。该公司强调一个鼓励团队成员追求卓越并每天尽最大努力工作的环境。此公告旨在号召大家，邀请有志之士探索Ashby的职业机会。整体侧重于为其工程团队招聘人才，特别是领导职位。

---

## 8. 破碎纠缠表征假设

**原文标题**: The Fractured Entangled Representation Hypothesis

**原文链接**: [https://github.com/akarshkumar0101/fer](https://github.com/akarshkumar0101/fer)

本文介绍“断裂纠缠表征假说”(FER)，挑战了神经网络性能提升必然等同于更好内部表征的假设。作者将通过开放式搜索（Picbreeder）进化的神经网络与通过随机梯度下降(SGD)训练来生成单一图像的神经网络进行比较。

他们的主要发现是，虽然这两种类型的网络实现了相似的输出性能，但它们的内部表征却大相径庭。SGD训练的网络表现出FER，一种无序的表征，其中单个神经元的功能复杂且纠缠。相比之下，进化的网络倾向于统一分解表征(UFR)，其中神经元具有更清晰且可解释的功能。

作者将每个神经元的功能可视化为图像，揭示了两种方法之间内部表征的显著差异。他们认为，大型模型中的FER可能会阻碍泛化、创造力和持续学习等关键能力。因此，理解和缓解FER对于推进表征学习至关重要。

该论文提供了补充数据，包括中间特征图和权重扫描，并提供代码以供复制实验。该代码允许用户加载Picbreeder基因组，训练SGD网络来模仿其输出，可视化内部表征，并执行权重扫描。作者最后提供更多Picbreeder基因组以供研究之用。

---

## 9. OpenAI Codex 评测

**原文标题**: OpenAI Codex Review

**原文链接**: [https://zackproser.com/blog/openai-codex-review](https://zackproser.com/blog/openai-codex-review)

本次评测探讨了OpenAI的Codex，重点关注其与GitHub连接的聊天界面，用于自动化代码任务。作者强调了Codex支持多线程工作流的潜力，即可以并行启动多个任务，这与他们偏好的工作方式相符。他们设想了一个未来的“无束缚工作流”，Codex可以支持远离办公桌的工作，这得益于其移动可访问性。通过聊天跟进任务、轻松创建拉取请求以及监控任务日志的能力也受到了赞扬。

然而，评测指出了其局限性。错误处理较差，代码质量不稳定，成功率仅为40-60%。Codex目前在复杂的重构方面表现不佳，并且缺乏对现有分支的流畅迭代，因为它更倾向于创建新的拉取请求。一个明显的缺点是其执行沙箱中缺乏网络连接，从而阻止了诸如依赖项更新之类的任务。

尽管存在这些问题，作者仍然持乐观态度。虽然Codex尚未实现“疯狂的生产力提升”，但他们相信，一旦错误处理和代码质量得到改善，分支上的多轮更新得到简化，并且增加了网络连接，情况将会改观。他们认为Codex目前最适合执行小型维护任务和小型更新，而大型项目仍然需要传统的IDE。作者预计Codex将演变为一个中央协调层，处理低优先级任务并跟踪整体进度。

---

## 10. 表情符号问题 (2022)

**原文标题**: The emoji problem (2022)

**原文链接**: [https://artofproblemsolving.com/community/c2532359h2760821_the_emoji_problem__part_i?srsltid=AfmBOor9TbMq_A7hGHSJGfoWaa2HNzducSYZu35d_LFlCSNLXpvt-pdS](https://artofproblemsolving.com/community/c2532359h2760821_the_emoji_problem__part_i?srsltid=AfmBOor9TbMq_A7hGHSJGfoWaa2HNzducSYZu35d_LFlCSNLXpvt-pdS)

提供的文本片段不完整，并未提供关于“表情符号问题 (2022)”的任何实际内容。它似乎是来自 Art of Problem Solving (AoPS) 社区的损坏或部分加载的网页，具体是“Turtle Math”部分中的一篇博客文章。

从文本中得出的主要结论是网页*未正确加载*。它建议用户“点击刷新”页面。没有关于“表情符号问题 (2022)”实际上是什么、它的数学含义是什么，或者围绕它的讨论是什么的信息。我们只能推断它是AoPS博客“Turtle Math”上讨论的一个话题。

因此，鉴于缺乏内容，不可能进行总结。唯一可操作的信息是页面需要刷新。

---

## 11. 地下室里的Lisp：楼上住着的依赖类型 [pdf]

**原文标题**: The Lisp in the Cellar: Dependent types that live upstairs [pdf]

**原文链接**: [https://zenodo.org/records/15424968](https://zenodo.org/records/15424968)

本文介绍了Deputy，一种基于Clojure的依赖类型编程语言，旨在探索交互式、REPL驱动的开发与依赖类型系统的集成。依赖类型允许代码计算类型，这些类型可以依赖于值，从而实现强大的编程模式。传统上，类型检查是一种纯粹的编译时操作。

Deputy利用Clojure的动态环境来实现交互式开发，即使在类型检查期间也是如此。通过将Deputy实现为Clojure库，宿主语言在类型级别编程时仍然可用。这提供了一种独特的开发体验，允许程序员在REPL中探索和改进程序逻辑和类型级计算。

本文强调了Lisp的交互式工作流程在增强依赖类型程序开发过程中的潜力，而依赖类型程序通常与更严格和静态的开发环境相关联。Deputy具有归纳数据类型，并作为研究这种新型依赖类型编程方法的实验平台。相关PDF文件“deputy-els.pdf”包含系统的完整详细信息。

---

## 12. 英伟达技术的曙光

**原文标题**: The Dawn of Nvidia's Technology

**原文链接**: [https://blog.dshr.org/2025/05/the-dawn-of-nvidias-technology.html](https://blog.dshr.org/2025/05/the-dawn-of-nvidias-technology.html)

这篇由一位参与英伟达早期历史的人士撰写的文章，回顾了两本关于该公司崛起的新书，并深入探讨了其早期年代的技术创新。作者重点介绍了英伟达的图像模型（使用二次曲面片代替三角形）及其I/O架构。

关于图像模型，英伟达最初使用二次曲面片，与三角形相比，这需要更少的数据通过PCI总线传输，这使得他们在PC上运行像世嘉街机游戏这样的复杂图形时具有优势。然而，作者预见到微软DirectX最终将占据主导地位，而DirectX依赖于三角形，因此离开了英伟达，希望能促使其转向更广泛支持的技术。

文章强调了英伟达I/O架构的重要性，这得益于该团队在Sun Microsystems使用Unix和虚拟内存系统的经验。这种架构包括一个“虚拟化对象”系统，带有一个基于软件的资源管理器，该管理器允许在硬件功能实现方面具有灵活性并加速创新。关键组件包括FIFO队列、直接内存访问(DMA)和I/O内存管理单元(IOMMU)，后者使应用程序能够在虚拟内存环境中直接访问I/O设备。这种架构解决了多进程操作系统中上下文切换的问题，为每个进程提供了独占访问图形设备的错觉，并且是“面向未来”的，旨在支持虚拟内存系统最终登陆PC。

---

## 13. Show HN: Astra – 一款新的js2exe编译器

**原文标题**: Show HN: Astra – a new js2exe compiler

**原文链接**: [https://github.com/astracompiler/cli](https://github.com/astracompiler/cli)

Astra 是一款快速、可靠且易于使用的 JavaScript 到 EXE 编译器，旨在为 Windows 编译服务器和 CLI 应用程序（macOS 和 Linux 支持正在开发中）。它采用一种新的编译方法，有别于现有的 `pkg` 和 `nexe` 等工具，从而产生相对较小的可执行文件大小（平均 70-80MB）。

主要特点包括：

*   **快速构建时间：** 利用 esbuild 进行快速编译。
*   **ESM 支持：** 处理 ECMAScript 模块，解决 Node.js SEA 中的限制。
*   **良好的开发者体验：** 采用 `signale`、`inquirer` 和 `chalk` 等工具，带来愉悦的用户体验。
*   **独立可执行文件：** 生成包含所有依赖项的单个 .exe 文件。
*   **元数据自定义：** 允许修改可执行文件的元数据，如图标、名称和版本。

编译过程包括使用 esbuild 进行代码 Linting 和打包，将生成的 Blob 注入到 Node.exe 二进制文件中，编辑元数据，并使用 postject 创建最终的可执行文件。 Astra 采用 MIT 许可证，欢迎贡献。 提供了通过 npm、yarn 和 pnpm 安装的说明，以及一个基本的使用示例和一个指向帮助命令的指针。

---

## 14. 从零开始的简易搜索引擎

**原文标题**: A simple search engine from scratch

**原文链接**: [https://bernsteinbear.com/blog/simple-search/](https://bernsteinbear.com/blog/simple-search/)

本文详细介绍了如何从头开始创建一个简单的搜索引擎，利用词嵌入和余弦相似度对搜索结果进行排序。作者 Max Bernstein 解释了他和 Chris Gregory 如何使用 word2vec 模型将单词映射到 300 维空间，其中每个维度代表一个语义轴。博客文章通过对构成它们的单词的嵌入求和来进行嵌入，搜索结果通过搜索查询的嵌入与文章嵌入之间的余弦相似度进行排序。

本文逐步介绍了整个过程，包括加载预训练的词嵌入、嵌入单词和文档，以及实现余弦相似度计算。它还展示了如何使用 Python 的 `code` 库构建一个基本的搜索 REPL。为了使搜索引擎可以通过网络访问，作者描述了如何将 word2vec 数据拆分为单独的 JSON 文件，用于嵌入和索引，从而能够进行高效的 HTTP Range 请求，仅下载必要的嵌入块。

最后，本文讨论了一种评估方法，定义了一个 top-k 准确率指标，用于将搜索引擎的性能与仅计算关键词出现次数的基线方法进行比较。这包括创建一个 (文档，查询) 对的评估数据集，并测量目标文档在给定查询的前 k 个搜索结果中出现的百分比。

---

## 15. 2025年：不使用游戏引擎制作游戏

**原文标题**: Making Video Games (Without an Engine) in 2025

**原文链接**: [https://noelberry.ca/posts/making_games_in_2025/](https://noelberry.ca/posts/making_games_in_2025/)

2025年（无引擎）制作游戏

---

## 16. 谷歌正在悄悄地帮助亚马逊提升数字图书销量。

**原文标题**: Google is quietly giving Amazon a leg up in digital book sales

**原文链接**: [https://www.washingtonpost.com/technology/2025/05/16/google-amazon-ebooks-apps/](https://www.washingtonpost.com/technology/2025/05/16/google-amazon-ebooks-apps/)

无法访问文章链接。

---

## 17. Teachable Machine -> 可训练机器

**原文标题**: Teachable Machine

**原文链接**: [https://teachablemachine.withgoogle.com/](https://teachablemachine.withgoogle.com/)

文章《Teachable Machine》是对同名平台的一个简要介绍。仅凭标题和内容中重复出现的标题，很难提供详细的总结。但是，我们可以推断出以下几点：

核心主题很可能是“Teachable Machine”。它几乎可以肯定是一个网站或工具（因此称之为“机器”），旨在用户友好，并促进学习或创建机器学习模型。这个名字暗示它旨在使机器学习变得易于访问，并能够教授给可能技术专长有限的个人。我们可以推测，它允许用户通过简化的界面“教”这台“机器”。

在没有更多信息的情况下，我们只能推测 Teachable Machine 很可能允许用户使用视觉、音频或其他输入方法来训练模型。“机器”随后将学习模式，并能够根据提供的训练对新数据进行分类。它很可能是一个旨在通过简化模型的开发和部署来普及机器学习访问的工具。

---

## 18. 最后一封信

**原文标题**: The Last Letter

**原文链接**: [https://aeon.co/essays/how-the-last-letters-of-the-condemned-can-teach-us-how-to-live](https://aeon.co/essays/how-the-last-letters-of-the-condemned-can-teach-us-how-to-live)

丹尼尔·R·布伦斯特特的文章《最后的信》探讨了从二战期间被纳粹处决的法国抵抗战士和政治人质的诀别信中获得的对生与死的深刻见解。布伦斯特特讲述了他发现这些信件的经过，以及其内容的强大和独特性，这源于作者们对迫在眉睫的死亡的直面。

这篇文章突出了这些高度私人的信件中存在的普遍主题，反映了人类的境况。布伦斯特特引用了蒙田的观点，即研究死亡教会我们如何生活，并将这些信件与伊丽莎白·库布勒-罗斯的悲伤五阶段联系起来，并注意到这些阶段如何在作者们生命的最后时刻被压缩。被判刑者经常讨价还价，反思如果拥有更多时间他们会做什么，从而提供了对他们价值观的洞察。

布伦斯特特分享了信件中的具体例子，展示了作者们对爱、遗憾、勇气和接受的表达。他穿插了个人轶事，例如在巴黎的街道标志上遇到抵抗战士乔治·皮塔德的名字，以及他在阅读丹尼尔·德库德曼切的最后一封信时自己对死亡的直面。

文章最后反思了面对自身死亡的心理困境，以及这些信件如何提供了一个强大而未经滤镜的视角，让我们得以窥见在生命尽头所浮现的情感和优先事项。作者发现，这些信件最终揭示了什么才是真正重要的，为我们如何更有意义地生活提供了宝贵的教训。

---

## 19. llm-d，Kubernetes原生分布式推理

**原文标题**: llm-d, Kubernetes native distributed inference

**原文链接**: [https://llm-d.ai/blog/llm-d-announce](https://llm-d.ai/blog/llm-d-announce)

LLM-d：用于优化分布式LLM推理的Kubernetes原生框架，提供了一条以具有竞争力的性能和快速价值实现大规模服务的清晰路径。它解决了标准LLM推理横向扩展方法的不足，该方法难以应对昂贵、不均匀的请求，以及通过专门路由和副本协调获得潜在性能提升。

文章强调了llm-d的关键优势：利用前缀缓存加速多轮请求，分离预填充和解码阶段以实现高效的资源利用，并适应多样化的服务质量 (QoS) 要求。

LLM-d的架构基于vLLM、Kubernetes和推理网关（IGW），整合了关键贡献，例如用于智能负载均衡的vLLM优化推理调度器、使用NVIDIA的NIXL与vLLM的分离服务，以及使用vLLM KV连接器API的分离前缀缓存。该框架还旨在通过硬件、工作负载和流量进行变体自动缩放，以优化资源利用率。

初步实验表明，前缀感知路由显著提高了性能，包括缩短了TTFT并提高了QPS，同时满足了SLO要求。文章鼓励AI工程师和研究人员加入llm-d社区，探索GitHub存储库，加入开发者Slack，并尝试快速入门来部署llm-d。

---

## 20. 将OCaml编译到TI-84 CE计算器

**原文标题**: Compiling OCaml to the TI-84 CE Calculator

**原文链接**: [https://farlow.dev/2025/05/17/ocaml-on-calculator](https://farlow.dev/2025/05/17/ocaml-on-calculator)

本文详细介绍了作者将 OCaml 代码编译并在 TI-84+ CE 计算器上运行的项目。其动机源于作者对函数式编程语言 OCaml 和计算器编程的兴趣。由于现有计算器工具链缺乏原生 OCaml 支持，因此促成了这个项目。

该方法利用了 Js_of_ocaml，这个工具通常将 OCaml 字节码编译成 JavaScript。作者为 Js_of_ocaml 创建了一个新的后端，生成 C 代码，旨在实现高可移植性和小代码尺寸，以适应计算器有限的资源（256k RAM）。这种转换的关键是管理 OCaml 运行时，包括垃圾回收。

为了实现可移植的垃圾回收，作者用对全局堆栈的显式读/写操作替换了局部变量，使垃圾回收器能够扫描活动对象。每当内存分配接近极限时，就会采用标记清除垃圾回收策略。

该项目还包括一个最小的 C 运行时和一个小的 TI-84+ CE 库，使 OCaml 程序能够与计算器的屏幕交互。最终实现了与 OCaml 构建系统 (dune) 和 LSP 支持的无缝集成，并以旋转立方体程序示例进行了演示。

作者承认目前的局限性（例如，没有浮点数或异常），但强调了未来使用像 wee 这样的工具进行扩展，以获得更广泛的平台支持的潜力。提供了一个简单的 Fibonacci 程序的生成 C 代码作为示例，展示了运行时和生成的 OCaml 代码。该项目的源代码是公开可用的。

---

## 21. DDoSecrets 公布了从 TeleMessage 黑客攻击中获得的 410 GB 堆转储数据。

**原文标题**: DDoSecrets publishes 410 GB of heap dumps, hacked from TeleMessage

**原文链接**: [https://micahflee.com/ddosecrets-publishes-410-gb-of-heap-dumps-hacked-from-telemessages-archive-server/](https://micahflee.com/ddosecrets-publishes-410-gb-of-heap-dumps-hacked-from-telemessages-archive-server/)

DDoSecrets 发布了从 TeleMessage 窃取的 410 GB 数据，TeleMessage 是一家以色列公司，负责归档来自 Signal 和 WhatsApp 等加密消息应用程序修改版本的信息。 这些数据包含敏感的 PII（个人身份信息），目前仅与记者和研究人员共享。

文章概述了导致数据泄露的事件时间线。 起始于时任国家安全顾问 Mike Waltz 使用 TeleMessage 修改版的 Signal，引发审查并导致 TM SGNL 源代码的发布。 随后，TeleMessage 多次遭到黑客攻击。 作者此前曾披露 TeleMessage 服务器中的一个漏洞，允许任何人下载包含明文聊天记录的 Java 堆转储。

DDoSecrets 发布的数据包括 2025 年 5 月 4 日的数千个堆转储，其中包含明文消息和元数据，包括发送者/接收者信息、时间戳和群组名称。 存档数据源于 Mike Waltz 等人和联邦政府内部对 TeleMessage 的使用。 DDoSecrets 已从堆转储中提取文本，以帮助研究。

作者 Micah Lee 是 DDoSecrets 集体成员，目前正在分析数据。 文章最后呼吁向 DDoSecrets 捐款。

---

## 22. 我被黑了吗 2.0

**原文标题**: Have I Been Pwned 2.0

**原文链接**: [https://www.troyhunt.com/have-i-been-pwned-2-0-is-now-live/](https://www.troyhunt.com/have-i-been-pwned-2-0-is-now-live/)

好的，以下是根据我对 Troy Hunt 的 “Have I Been Pwned 2.0 is Now Live” 文章的总结，基于我的常识和标题及作者的推测：

文章宣布了 Have I Been Pwned (HIBP) 的重大升级，称为 HIBP 2.0。该服务的核心功能保持不变：允许用户检查他们的电子邮件地址或用户名是否在已知的数据泄露中被泄露。然而，底层的基础设施和代码库已被完全重写，以提高性能、可扩展性和安全性。

HIBP 2.0 的主要改进可能包括：

*   **增强的性能和可扩展性：** 新的架构旨在处理更大的数据量和用户请求，即使在高峰使用期间也能确保更快的响应时间。这对于 HIBP 的持续增长和纳入更多泄露事件至关重要。

*   **改进的安全性：** 重写的代码可能包含了最新的安全最佳实践，以更好地保护数据库的完整性和用户搜索的隐私。它可能包括更好的保护，防止 SQL 注入和跨站脚本等攻击。

*   **新功能或现有功能的增强：** 虽然提示中没有明确说明，但 HIBP 2.0 很可能包含了对现有功能的改进或新功能。这可能包括增强的 API 功能、更详细的泄露信息或改进的搜索功能。

*   **现代化的技术栈：** 这次更新可能涉及过渡到更现代、更高效的技术，从而提高可维护性和未来的开发能力。

HIBP 2.0 的总体目标是确保该服务仍然是互联网用户主动监控其在线安全并在数据泄露时采取适当行动的可靠且高性能的资源。作者 Troy Hunt 可能会强调数据泄露意识的重要性，并鼓励用户定期使用更新后的服务。

---

## 23. 作为库的虚拟机监控器

**原文标题**: Hypervisor as a Library

**原文链接**: [https://seiya.me/blog/hypervisor-as-a-library](https://seiya.me/blog/hypervisor-as-a-library)

本文以作者的Starina OS为例，介绍了“库形式的虚拟机监控器”的概念，以实现Linux兼容性。 Starina没有采用将虚拟机监控器作为单独进程运行的传统方法，而是将其虚拟机监控器作为Rust库`starina_linux::Command`提供，从而允许从Starina应用程序内部直接与Linux客户机进行交互。

作者将其与Rust的`std::process::Command`进行类比，使集成过程既熟悉又直观。 这使得开发人员可以在轻量级VM中启动Linux二进制文件，并使用熟悉的方法来管理stdin/stdout和环境变量。 核心思想是将虚拟机监控器的功能（创建客户机物理地址空间、加载Linux内核、处理内存映射I/O）封装在库API中。

主要优点包括更高的灵活性和潜在的性能提升，因为减少了进程间通信。 它还允许与Starina无缝集成，从而实现与客户机OS的直接且安全的交互，甚至允许访问客户机内存。

作者承认虚拟机可能被认为很慢的潜在缺点，但相信通过优化，这种方法可以通过VM快照等技术与原生Linux性能相媲美。 他设想了一种类似容器的体验，开发人员可以在其中指定容器镜像、使用VM状态缓存并通过Starina OS直接公开端口，最终释放Linux设备驱动程序的强大功能。

---

## 24. 生产测试：改善系统，睡个好觉

**原文标题**: Production tests: a guidebook for better systems and more sleep

**原文链接**: [https://martincapodici.com/2025/05/13/production-tests-a-guidebook-for-better-systems-and-more-sleep/](https://martincapodici.com/2025/05/13/production-tests-a-guidebook-for-better-systems-and-more-sleep/)

本文倡导实施生产环境测试（也称为合成测试），以提高系统可靠性，改进部署并辅助可观测性。生产环境测试是直接在生产环境中运行的自动化测试，通常每分钟运行一次，模拟用户行为或后端服务交互。

其优势包括尽早检测回归问题，以便在影响客户之前主动修复。生产环境测试还可以作为部署的金丝雀，充当集成测试来捕捉与其他服务的不匹配。它们通过提供对正常工作和故障组件的洞察力来帮助调试，并通过提供更快的感知和更多信息来解决问题，从而改善事件恢复。

关键的设计考虑因素包括简单性和专注性，避免过于复杂或特定于功能的测试，以免导致虚假警报。在追求合理覆盖范围的同时，优先测试具有较高用户影响的关键功能。虽然与健康检查不同，但生产环境测试可以利用它们来发出早期警告。需要考虑对日志、指标和追踪的影响，以及管理测试生成的虚假数据的策略。在触发警报之前采用“三次罢工”方法有助于缓解由瞬态问题引起的虚假警报。

生产环境测试的优点包括真实世界的测试条件、增强的质量控制、故障排除支持、低流量地区的可观测性、更安全的部署以及在其他环境中潜在的重用。缺点包括设置、清理、场景创建、潜在的不稳定性和资源消耗等挑战。

---

## 25. 显示 HN：Olelo Foil - NACA 翼型模拟器

**原文标题**: Show HN:  Olelo Foil - NACA Airfoil Sim

**原文链接**: [https://foil.olelohonua.com/](https://foil.olelohonua.com/)

这个“Show HN”帖子介绍了 Olelo Foil，一个 NACA 翼型模拟器。主要目的是展示一个允许用户模拟和可视化 NACA 翼型行为的工具。虽然内容只简单提到“开发”，但可以推断出创建者是在分享他们的在研作品或已完成的产品。Olelo Foil 很有可能允许用户输入定义 NACA 翼型的参数（例如，NACA 4412），然后模拟其性能，并可能可视化压力分布、升力系数和阻力系数等。该帖子鼓励 Hacker News 社区参与，很可能是在寻求反馈、错误报告或对未来开发的建议。由于信息有限，很难详细说明功能，但核心目的是明确的：提供一个实用的工具，用于学习和模拟 NACA 翼型。

---

## 26. Show HN：地图上的文本转3D模拟（历史重现效果不错）

**原文标题**: Show HN: Text to 3D simulation on a map (does history pretty well)

**原文链接**: [https://mused.com/map/](https://mused.com/map/)

此“Show HN”帖子介绍了一个地图模拟平台，该平台利用文本输入在地图上生成3D模拟。其关键在于它能够根据文本描述模拟历史事件。这意味着该平台能够解释描述地点、时间和动作的文本数据，然后将这些信息转化为视觉上引人入胜的3D表示，并叠加到地图上。该平台定位为一种空间智能工具，暗示其可用于分析、理解和可视化地理数据和事件。虽然帖子简短，但它暗示了一种新颖的历史可视化方法，并且可能成为各种涉及空间数据分析的应用程序的强大工具。本质上，它将文本叙事转化为交互式3D地图模拟，其中历史事件是一个关键展示。

---

## 27. 朱尔斯：一个异步编码代理

**原文标题**: Jules: An Asynchronous Coding Agent

**原文链接**: [https://jules.google/](https://jules.google/)

Jules是一个异步编码代理，旨在处理用户不愿执行的编码任务，从而释放他们的时间来从事更具吸引力的工作。它可以协助修复bug、升级版本、编写测试、修复现有代码以及构建新功能。

该过程包括几个步骤：首先，用户选择一个GitHub存储库和分支，并为Jules提供详细的提示。未来，用户将能够直接通过GitHub issue分配任务。然后，Jules获取并将存储库克隆到云VM，使用Gemini 2.5 Pro模型制定计划，并将该计划呈现给用户以供批准。获得批准后，Jules提供建议更改的差异，允许用户快速审查和批准代码编辑。最后，Jules创建一个包含更改的pull request，用户可以批准、合并并发布到GitHub。Jules还会创建一个更改的音频摘要，以帮助用户快速了解更新。

---

## 28. 芬兰宣布其铁路网络迁移至国际标准轨距

**原文标题**: Finland announces migration of its rail network to international gauge

**原文链接**: [https://www.trenvista.net/en/news/rnhs/finland-migration-standard-gauge/](https://www.trenvista.net/en/news/rnhs/finland-migration-standard-gauge/)

芬兰宣布计划将其整个铁路网络从俄罗斯轨距改为欧洲标准轨距，此举是出于提高军事机动性、加入北约后对地区安全的担忧以及与俄罗斯日益紧张的关系的考虑。交通部长露露·兰内公布了该计划，强调有必要消除芬兰、瑞典和挪威之间运输部队和货物的障碍。

该项目预计耗资数十亿欧元，将影响超过9200公里的轨道，并需要数十年才能完成，计划从北部奥卢附近开始。芬兰政府预计将在2027年7月之前做出最终决定，建设工作将于2032年左右开始。该国依赖欧盟的大量资金，可能覆盖高达50%的规划成本和30%的建设费用。

这项大规模基础设施项目代表着芬兰重大的地缘政治和战略转变，使其铁路网络与欧洲标准保持一致，并巩固其与欧盟和北约的融合。此次改造象征着摆脱与俄罗斯的历史联系，走向更强大的欧洲认同。

---

## 29. Show HN: JavaFactory – 用于生成Java代码的IntelliJ插件

**原文标题**: Show HN: JavaFactory – IntelliJ plugin to generate Java code

**原文链接**: [https://github.com/JavaFactoryPluginDev/javafactory-plugin](https://github.com/JavaFactoryPluginDev/javafactory-plugin)

JavaFactory：利用LLM自动化生成重复性Java代码的IntelliJ插件。相较于传统AI代码生成器，它旨在提供更可预测和稳定的结果。其工作原理是基于任务的自然语言描述（例如，测试生成）定义可重用的“模式”。这些模式包含一个系统提示（定义目标、规则、输出格式和示例）和一个用户提示（指定要包含的类）。

一个关键特性是其基于注解的引用收集，使用`@JavaFactoryData`和`@JavaFactoryApi`来精确控制代码生成中使用的类。`@JavaFactoryData`递归地收集类，适用于领域模型，而`@JavaFactoryApi`仅收集一层引用的API，允许指定实现、测试和fixtures。

对于那些对不可预测的AI代码生成感到沮丧的开发者，或者在具有重复模式（如分层架构）的结构化环境中工作的开发者（例如，生成DAO、Repository和API的实现、测试和fixtures），推荐使用JavaFactory。其理念是手动设计核心组件，并使用JavaFactory自动化重复性的、可预测的部分。

---

## 30. 我被AI科学炒作忽悠了——这是它教会我的。

**原文标题**: I got fooled by AI-for-science hype–here's what it taught me

**原文链接**: [https://www.understandingai.org/p/i-got-fooled-by-ai-for-science-hypeheres](https://www.understandingai.org/p/i-got-fooled-by-ai-for-science-hypeheres)

尼克·麦格瑞维，一位物理学家，分享了他使用人工智能解决等离子体物理研究中偏微分方程(PDEs)的令人失望的经历。最初他对人工智能加速科学进步的潜力充满乐观，但他发现人工智能方法，尤其是物理信息神经网络(PINNs)，非常脆弱，并且在与最先进的数值方法进行公平比较时，表现往往比宣传的更差。

他强调，许多声称人工智能能显著加速的论文，实际上是将人工智能与较弱的基线进行比较，从而导致过于乐观的结果。他还指出存在严重的报告偏差，即人工智能方法的负面结果和失败很少被发表。这造成了对人工智能在科学领域能力的扭曲认知。

麦格瑞维对应用于流体力学偏微分方程的人工智能的系统性回顾表明，绝大多数论文都使用了较弱的基线，导致了不公平的比较。他认为，人工智能在科学领域的应用更多地是受到对科学家自身的好处（例如，发表论文、获得资金）的驱动，而不是真正推动科学理解的进步。

虽然麦格瑞维承认人工智能可以在天气预报和药物发现等领域为科学突破做出贡献，但他对人工智能的革命性潜力表示怀疑。他认为，人工智能更有可能成为一种促进渐进式进步的工具，而不是科学领域改变游戏规则的力量，并倡导更现实的期望、严格的比较，以及更加关注基于人工智能的方法的可靠性和鲁棒性。

---

## 31. 适用于 Linux 的 Windows 子系统现已开源

**原文标题**: The Windows Subsystem for Linux is now open source

**原文链接**: [https://blogs.windows.com/windowsdeveloper/2025/05/19/the-windows-subsystem-for-linux-is-now-open-source/](https://blogs.windows.com/windowsdeveloper/2025/05/19/the-windows-subsystem-for-linux-is-now-open-source/)

微软于2025年5月宣布，适用于Linux的Windows子系统（WSL）现已开源。经过多年的努力，驱动WSL的代码现已在GitHub上的Microsoft/WSL提供。用户现在可以下载WSL，从源代码构建它，添加修复程序和功能，并参与其开发。

WSL由命令行可执行文件（wsl.exe、wslconfig.exe、wslg.exe）、WSL服务（wslservice.exe）、Linux init和守护进程（init、gns、localhost）以及文件共享实现（plan9）组成。 这是对已经开源的组件（如microsoft/wslg (Wayland和X服务器支持) 和 microsoft/WSL2-Linux-Kernel）的补充。

WSL最初于2016年推出，基于pico进程提供程序（lxcore.sys），发展成为WSL 1。 后来，WSL 2于2019年推出，利用Linux内核来提高兼容性。 2021年，WSL与Windows代码库分离，并作为Microsoft Store中的软件包发布，从0.47.1版本开始。 向新的WSL软件包的完全过渡随着Windows 11 24H2完成。 WSL 2.0.0引入了镜像网络和DNS隧道等功能。

开源的驱动力在于认识到社区对WSL的重大贡献，即使在没有源代码访问权限的情况下也是如此。 微软希望开源能够进一步加速WSL的开发并促进社区参与。

---

## 32. RepoRoulette：GitHub仓库随机抽样

**原文标题**: RepoRoulette: Randomly sample repositories from GitHub

**原文链接**: [https://github.com/gojiplus/reporoulette](https://github.com/gojiplus/reporoulette)

RepoRoulette 是一个 Python 包，旨在从 GitHub 上随机抽样仓库，用于各种研究和学习目的。它提供了四种不同的抽样方法：

1.  **基于 ID 的抽样：** 探测随机的 GitHub 仓库 ID，提供真正的随机性，但由于无效 ID，命中率可能较低。需要 GitHub 令牌。
2.  **时间抽样：** 选择在定义的日期范围内随机选择的时间段内更新的仓库。也需要 GitHub 令牌，并允许按最小星数和语言等特征进行过滤。
3.  **BigQuery 抽样：** 利用 Google BigQuery 的公共 GitHub 数据集进行高级过滤和大规模抽样。需要启用 BigQuery API 的 Google Cloud Platform 项目和一个服务帐户。此方法能高效处理大型样本，并绕过 GitHub API 速率限制，但会产生云费用。
4.  **GH Archive 抽样器：** 此方法通过从 GitHub Archive 获取事件来抽样仓库，GitHub Archive 记录了公开的 GitHub 时间线。它允许您指定要抽样的仓库数量、要从中抽样的天数以及要考虑的事件类型。

RepoRoulette 支持多种用例，例如学术研究、学习资源发现、数据科学、趋势分析和安全研究。该项目已获得 MIT 许可证许可，欢迎贡献。

---

## 33. Show HN: 我做了一个应用，5分钟就能为孩子创作个性化故事

**原文标题**: Show HN: I made an app to create personalized stories for children in 5 minutes

**原文链接**: [https://www.unlimitedtales.com](https://www.unlimitedtales.com)

这个“Show HN”帖子介绍了一个应用程序，用户可以在大约 5 分钟内为儿童创建个性化故事。 该应用程序拥有一个用户友好的四步流程：配置角色属性，选择主题、语言和插图风格； 生成定制的故事文本； 审查并为每页和封面策划插图； 最后，将故事下载为 PDF。

该应用程序适合所有年龄段的儿童，因为内容会根据主角的年龄进行调整。 提供各种插图风格，包括动漫、3D、水彩和像素艺术，并定期添加新的风格。

如果用户不满意，可以重新生成整个故事或单个插图，但故事完成后无法编辑。 该应用程序旨在提供一种快速简便的方式，为儿童创建独特而引人入胜的故事，可从任何具有浏览器的设备访问。 该帖子包含用户评价，突出了用户使用该应用程序为他们的孩子和侄子创作故事的积极体验。 为了吸引新用户，帖子包含首次故事 8 折的优惠。

---

## 34. 人们在做什么？基于全球人口动态的实时估算

**原文标题**: What are people doing? Live-ish estimates based on global population dynamics

**原文链接**: [https://humans.maxcomperatore.com/](https://humans.maxcomperatore.com/)

这篇题为“人们在干什么？基于全球人口动态的近似实时估算”的文章，似乎试图根据出生率和死亡率提供全球人口活动的实时或接近实时的估算。

目前，该文章正处于加载状态。它显示标题“人们到底在干什么？”并显示“正在加载日期…”，这表明它正在尝试获取当前日期。

文章的核心是展示实时人口动态。它旨在显示“全球人口”以及估计的“每秒出生人数”、“每秒死亡人数”和“每秒净增人数”。目前，所有这些值都显示为 0.0，表明存在加载错误或数据尚未初始化。

它还显示当前的“协调世界时 (UTC)”和“在线观看人数”，后者也为 0。

最后，它提到了“活动分解”，但没有提供任何进一步的信息。这表明，一旦正确加载，该文章打算对全球人口的活动进行分类或分解，大概是基于与人口数量相关的推断数据或统计模型。

简而言之，这篇文章旨在提供全球人口变化的实时快照，但目前看来，它正在努力加载相关数据。

---

## 35. Claude 代码 SDK

**原文标题**: Claude Code SDK

**原文链接**: [https://docs.anthropic.com/en/docs/claude-code/sdk](https://docs.anthropic.com/en/docs/claude-code/sdk)

Claude Code SDK 允许开发者以编程方式将 Claude Code 集成到他们的应用程序中，主要通过命令行使用。计划推出 TypeScript 和 Python SDK。它支持单轮提示和多轮对话，从而能够创建 AI 驱动的编码助手。

主要功能包括：

*   **基本用法：** 运行单轮提示，并提供纯文本、JSON 和流式 JSON 输出选项。
*   **高级用法：** 恢复和继续对话，使用系统提示定制 Claude 的行为，以及使用模型上下文协议 (MCP) 服务器扩展功能。
*   **MCP 配置：** 使用外部服务器实现数据库访问和 API 集成等功能（需要通过 `--allowedTools` 显式允许工具）。
*   **CLI 选项：** 用于控制 Claude 行为的各种标志，例如输出格式、会话管理、系统提示和工具权限。
*   **输出格式：** 文本、JSON（带有成本和会话 ID 等元数据）以及流式 JSON（用于实时消息传递）。
*   **消息模式：** 用于不同事件类型的严格类型化 JSON 消息，包括助手消息、用户消息和结果消息。
*   **示例：** 简单的脚本集成、文件处理、会话管理以及错误处理和速率限制的最佳实践。

实际应用包括 Claude Code GitHub Actions。相关资源包括 CLI 用法文档、GitHub Actions 集成详细信息和教程。

---

## 36. Biff - 一个开箱即用的 Clojure Web 框架

**原文标题**: Biff – a batteries-included web framework for Clojure

**原文链接**: [https://biffweb.com](https://biffweb.com)

Biff：一个快速构建和部署 Web 应用的 Clojure 全栈框架

Biff 是一个开箱即用的 Clojure Web 框架，旨在帮助独立开发者快速构建和部署 Web 应用，而无需陷入复杂的细节中。它通过整合来自 Clojure 生态系统的各种库和工具，将它们打造为一个有凝聚力、精致的整体来实现这一目标。

主要功能包括：

*   **XTDB 集成：** 使用 Malli 实现数据库的不可变性以及模式强制执行。
*   **htmx 用于 UI：** 允许在后端创建丰富的交互式 UI，并可选使用 hyperscript 进行轻量级的客户端脚本编写。
*   **身份验证：** 提供基于电子邮件的无密码身份验证，并支持魔法链接和一次性密码。
*   **部署就绪：** 包含用于配置 Ubuntu VPS 并通过 Uberjar 和 Docker 进行部署的代码。
*   **实时 REPL：** 提供一个实时 REPL，可以在文件保存时评估更改，并允许动态开发，即使在生产环境中也是如此。
*   **文档：** 文档完善，包含教程、参考文档和一个入门项目。

Biff 强调强大的默认设置，这些设置可以轻松修改以适应不断发展的项目需求，从而提高灵活性并避免不必要的约束。简而言之，Biff 旨在通过提供坚实的基础和简化的工作流程来加速 Clojure Web 开发。

---

## 37. Kilo：少于1000行代码，带语法高亮和搜索功能的文本编辑器

**原文标题**: Kilo: A text editor in less than 1000 LOC with syntax highlight and search

**原文链接**: [https://github.com/antirez/kilo](https://github.com/antirez/kilo)

Kilo 是一个小型文本编辑器，采用 BSD 许可证，由 Salvatore Sanfilippo (antirez) 编写，代码量少于 1000 行。它被设计为一个简单的、无库依赖的编辑器，依靠标准的 VT100 转义序列进行终端交互。该编辑器尚处于早期阶段，但提供了基本功能：打开文件、用 CTRL-S 保存、用 CTRL-Q 退出，以及用 CTRL-F 在文件中搜索（用 ESC 退出搜索，用方向键导航）。Kilo 不需要任何外部库，包括 curses，这使得它具有高度的可移植性和轻量性。Antirez 鼓励开发者使用 Kilo 作为基础，构建更高级的编辑器或命令行界面，超越典型的 REPL 风格。展示 Kilo 功能的屏幕录像可在提供的 asciinema 链接中找到。

---

## 38. 动画卡通游戏讲解博弈论

**原文标题**: Game theory illustrated by an animated cartoon game

**原文链接**: [https://ncase.me/trust/](https://ncase.me/trust/)

信任的进化：一款互动在线游戏，以动画卡通的形式呈现，运用博弈论来说明信任与合作在社会中的重要性。该游戏探索了囚徒困境，一个经典的博弈论场景，其中个体理性会导致集体次优。

游戏中，玩家可以与程序预设了不同策略的角色互动，例如总是合作、总是背叛、随机合作或以牙还牙。通过与这些角色进行多轮游戏，玩家可以观察到随着时间的推移，哪些策略表现更好。

游戏的主要启示包括：

*   **信任与合作是有益的：** 一贯合作的角色往往在长期内表现更好，尤其是在可以发展信任的环境中。
*   **以牙还牙是一种非常成功的策略：** 这种策略开始时选择合作，然后模仿对手的上一步行动。它促进合作，同时也惩罚背叛。
*   **不信任可能具有破坏性：** 单次背叛可能会引发报复和不信任的循环，导致每个人的总体结果下降。
*   **清晰的沟通和信号可以促进信任：** 拥有值得信赖的声誉可以鼓励他人与你合作。
*   **噪音和误解会侵蚀信任：** 即使在普遍合作的环境中，偶尔发生的意外背叛也可能破坏信任并导致冲突。

总而言之，《信任的进化》表明，虽然背叛可能带来短期收益，但基于信任的持续合作才是实现互利共赢和繁荣社会的最有效途径。 该游戏强调了宽恕、清晰沟通以及从过去的互动中学习的能力在建立和维持信任中的重要性。

---

## 39. 莱瑞亚 2

**原文标题**: Lyria 2

**原文链接**: [https://deepmind.google/technologies/lyria/](https://deepmind.google/technologies/lyria/)

Lyria 2：谷歌最新AI音乐生成模型

---

## 40. 一个不搭飞机游遍世界各国的人 (2023)

**原文标题**: A man who visited every country in the world without boarding a plane (2023)

**原文链接**: [https://www.theguardian.com/travel/2023/aug/16/take-the-high-road-the-man-who-visited-every-country-in-the-world-without-boarding-a-plane](https://www.theguardian.com/travel/2023/aug/16/take-the-high-road-the-man-who-visited-every-country-in-the-world-without-boarding-a-plane)

托比约恩·彼泽森，受童年冒险梦想驱使，踏上了一段为期十年的旅程，不乘坐飞机访问了世界上每个国家。他感到所有伟大的冒险都已经发生过了，这让他感到沮丧，因此他发现从未有人在一次连续的旅行中，不依靠航空旅行完成这一壮举。

彼泽森设定了三条规则——在每个国家至少停留24小时，不回家，绝对不乘坐飞机——他的目标是以每天20美元的预算访问所有203个国家，资金来自储蓄、捐款和丹麦红十字会的赞助。

他的旅程充满了挑战。他忍受了脑疟疾，被枪指着，以及无数的官僚障碍。“不乘飞机回家”的规则导致他错过了祖母的葬礼。他还与当时的伴侣Le的关系变得紧张。然而，他们的关系得到了加强，最终在山顶上求婚并结婚。新冠疫情将他困在香港两年，延误了他的归期。

尽管困难重重，彼泽森强调了他在每个国家遇到的善良，并强调了不同文化背景的人们之间的相似之处。他强调了依靠他人以及即使面对看似无法克服的障碍也要坚持下去的重要性。他于2023年5月回到丹麦，受到热烈的欢迎，完成了他非凡的、无飞行的全球之旅。虽然很高兴他完成了这件事，但彼泽森表示感到筋疲力尽，以及这次旅行给他带来了情感上的伤害。

---

## 41. 微软支持的Builder.ai进入破产程序

**原文标题**: Microsoft-backed Builder.ai enters insolvency proceedings

**原文链接**: [https://techcrunch.com/2025/05/20/once-worth-over-1b-microsoft-backed-builder-ai-is-running-out-of-money/](https://techcrunch.com/2025/05/20/once-worth-over-1b-microsoft-backed-builder-ai-is-running-out-of-money/)

得到的结果如下：

Builder.ai，一家由微软支持的人工智能软件公司，正在进入破产程序。这家以简化应用程序和网站开发平台而闻名的公司，已筹集超过4.5亿美元的资金。一位公司发言人证实，将任命一位管理人来管理公司的事务。

公司将“历史挑战和过去的决策”归咎于其财务困境的原因，尽管现任团队做出了努力。Builder.ai 计划在此过渡期间为员工、客户和合作伙伴提供支持，并将尽可能探索业务的各种选择。

最近的问题包括据报道的2024年下半年收入预计减少25%以及2月份任命了一位新首席执行官。由于有指控称销售额虚报超过20%，因此启动了审计。此前，该公司因夸大其应用程序开发平台的自动化程度而受到审查，据报道，该平台严重依赖人类工程师。

---

## 42. 深度学习中对表征乐观主义的质疑

**原文标题**: Questioning Representational Optimism in Deep Learning

**原文链接**: [https://github.com/akarshkumar0101/fer](https://github.com/akarshkumar0101/fer)

本文挑战了“表征乐观主义”的观点，即深度学习模型中更好的性能必然等同于更好的内部表征。作者引入了“破碎纠缠表征（FER）”的概念，这是一种在使用随机梯度下降（SGD）训练的网络中发现的无序内部表征形式。

该研究将通过开放式搜索过程（Picbreeder）演化的神经网络与在生成单个图像（头骨、蝴蝶和苹果）的简单任务上使用 SGD 训练的网络进行了比较。这种最小设置的一个关键优势是能够将每个隐藏神经元的功能可视化为图像，从而揭示网络的输出是如何构建的。

最引人注目的发现是，虽然两种类型的网络都实现了相似的输出行为，但它们的内部表征却大相径庭。SGD 训练的网络表现出 FER，而演化网络则在很大程度上避免了 FER，接近于更“统一分解表征（UFR）”。作者假设，大型模型中的 FER 可能会对重要的模型能力产生负面影响，包括泛化、创造力和持续学习。

该论文提供了广泛的补充数据，包括中间特征图和权重扫描，以可视化表征的差异。GitHub 上提供了用于加载 Picbreeder 基因组、训练 SGD 网络以模仿其输出、可视化内部表征和执行权重扫描的代码。作者应要求提供更多 Picbreeder 基因组的访问权限。该论文认为，理解和缓解 FER 对于推进深度学习中的表征学习至关重要。

---

## 43. 美国为何总是出现贸易逆差？

**原文标题**: Why Does the U.S. Always Run a Trade Deficit?

**原文链接**: [https://libertystreeteconomics.newyorkfed.org/2025/05/why-does-the-u-s-always-run-a-trade-deficit/](https://libertystreeteconomics.newyorkfed.org/2025/05/why-does-the-u-s-always-run-a-trade-deficit/)

托马斯·克利特加德的文章《为什么美国总是存在贸易逆差？》认为，美国持续的贸易逆差不仅仅是出口滞后于进口的问题，更是一个宏观经济问题，根源在于国内储蓄相对于投资支出的不足。

文章利用国民经济核算原则解释说，在封闭经济中，投资等于储蓄。然而，在像美国这样的开放经济中，储蓄缺口需要从国外借款，从而导致净金融流入。这些流入反映了外国人购买美国资产的行为，弥补了出口和进口之间的差额。

2000年以来的数据显示，美国储蓄和投资支出之间的缺口持续存在，家庭、企业和政府储蓄的波动常常相互抵消。虽然贸易政策可以影响贸易构成，但只有在改变储蓄-投资缺口时，它们才会影响贸易逆差。作者表明，即使解决特定的进口问题，例如石油依赖，也不一定能缩小整体贸易逆差。

文章反驳了贸易逆差本质上是负面的观点，认为外国借款可以促进投资并提高生产能力。最终，减少贸易逆差需要对国内储蓄和投资进行艰难的重新调整，可能涉及降低投资和增加储蓄，正如2008年金融危机期间所见。

---

## 44. Ann，小型注释服务器

**原文标题**: Ann, the Small Annotation Server

**原文链接**: [https://mccd.space/posts/design-pitch-ann/](https://mccd.space/posts/design-pitch-ann/)

Ann：一个基于 ActivityPub 的极简、去中心化社交媒体服务器，专注于 Web 注释。它允许用户存储、发送和接收关于任何内容的注释（评论、点赞、推荐），作为各种应用的基础，而非一个独立的社交网络。

与中心化社交媒体不同，Ann 旨在与前端应用集成，从而在各种场景中启用社交功能。潜在应用包括博客和 Gemini 浏览器的评论区、私有研究协作平台、推荐引擎、用于在任何网页上查看和添加评论的 Web 浏览器插件、带注释内容的 AI 训练数据集，以及 Logseq 和 Obsidian 等笔记应用插件。

愿景是在 LibreOffice 和视频播放器等现有应用中启用社交功能，与 Notion 和 YouTube 等中心化解决方案竞争。无需每个应用都开发自己的评论服务器，它们可以与 Ann 集成，让用户控制自己的数据和内容消费，同时保持隐私，并避免对 JavaScript 重型 Web 应用的需求。 Ann 本质上旨在去中心化并将注释功能嵌入到各种应用程序中。

---

## 45. xAI 的 Grok 3 登陆微软 Azure

**原文标题**: xAI's Grok 3 comes to Microsoft Azure

**原文链接**: [https://techcrunch.com/2025/05/19/xais-grok-3-comes-to-microsoft-azure/](https://techcrunch.com/2025/05/19/xais-grok-3-comes-to-microsoft-azure/)

微软现通过Azure AI Foundry平台提供对xAI Grok AI模型（特别是Grok 3和Grok 3 mini）的托管访问，成为首批提供此服务的主要云提供商之一。这意味着Azure客户可以直接访问Grok模型并为其付费，并享有微软产品所期望的服务级别协议。

尽管xAI之前将Grok宣传为前卫、较少过滤的AI，但Azure AI Foundry上提供的Grok 3模型比埃隆·马斯克社交网络X上使用的版本更加受控。文章强调了过去Grok在X上引发的争议，包括出现偏见的回应和有问题的文本生成实例。

Azure AI Foundry版本的Grok还提供额外功能，例如数据集成、定制选项和治理能力，这些功能不一定通过xAI的API提供。此举为企业客户提供了一种在更结构化和合规的环境中使用Grok强大功能的方式。

---

## 46. 禁忌铁路：维也纳-平壤 (2008)

**原文标题**: The forbidden railway: Vienna-Pyongyang (2008)

**原文链接**: [http://vienna-pyongyang.blogspot.com/2008/04/how-everything-began.html](http://vienna-pyongyang.blogspot.com/2008/04/how-everything-began.html)

作为一名奥地利铁路爱好者和奥地利联邦铁路的员工，赫尔穆特详细介绍了他的雄心勃勃的火车旅行至朝鲜计划的起源，特别是通过鲜为人知的图们江边境口岸。他对火车和旅行的热爱使他在1998年的时刻表中发现了莫斯科-平壤的火车线路。

多年来，赫尔穆特积累了旅行经验，包括西伯利亚铁路之旅和横跨欧亚大陆的旅行，这激发了他对朝鲜孤立的共产主义社会的兴趣。他尤其对图们江线路感兴趣，这条线路每月只有两次由朝鲜卧铺车提供服务。

尽管旅行社声称该线路对游客关闭，但赫尔穆特的研究，包括一篇命运攸关的Usenet帖子和一个德国铁路论坛的信息，表明情况并非如此。他甚至在俄罗斯境内乘坐朝鲜卧铺车前往图们江，购买了仅到达朝鲜境内第一站的车票，证明了该线路的持续存在。

最终目标是穿越边境。赫尔穆特和他的朋友奥利弗决定预订前往朝鲜新义州的普通行程，但秘密尝试通过图们江入境，前提是签证包含图们江作为入境点。当他收到维也纳的朝鲜大使馆发放的签证，上面确实列出了图们江时，赫尔穆特断定他和奥利弗即将成行。

---

## 47. 新西兰人工智能杂谈

**原文标题**: Remarks on AI from NZ

**原文链接**: [https://nealstephenson.substack.com/p/remarks-on-ai-from-nz](https://nealstephenson.substack.com/p/remarks-on-ai-from-nz)

无法访问文章链接。

---

## 48. 语言学家发现曾被认为是“骗局”的普遍语言模式的证据

**原文标题**: Linguists Find Proof of Sweeping Language Pattern Once Deemed a 'Hoax'

**原文链接**: [https://www.scientificamerican.com/article/linguists-find-proof-of-sweeping-language-pattern-once-deemed-a-hoax/](https://www.scientificamerican.com/article/linguists-find-proof-of-sweeping-language-pattern-once-deemed-a-hoax/)

本文探讨了一项重新审视语言相对论的新研究，特别是关于某些语言拥有不成比例的特定概念词汇，反映文化优先性的论断。该研究发表于PNAS，分析了超过600种语言的双语词典，重点关注“词汇精细化”，即专门用于特定概念的词汇比例。

研究人员证实了因纽特语对雪的重视，同时也发现其他语言也表现出类似的模式，例如萨摩亚语对熔岩的关注，或苏格兰语对燕麦粥的强调。这表明语言和文化之间可能存在联系，反映了一个社会的价值观。

虽然最初的“因纽特语雪词”论断之前已被揭穿为骗局，但这项研究采用了一种计算方法来识别和量化这种词汇精细化现象。研究结果支持对语言相对论的更细致入微的看法：虽然语言可能不会*决定*我们如何感知世界，但它可以微妙地*影响*它。

文章还承认了该研究的局限性，包括依赖于可能存在偏见的词典以及将英语作为基础语言进行固有比较。作者建议未来的研究应侧重于通过文本和社交媒体分析来分析现实世界中的语言使用情况。

---

## 49. 使用无监督机器学习求解基于物理的初值问题

**原文标题**: Solving physics-based initial value problems with unsupervised machine learning

**原文链接**: [https://link.aps.org/doi/10.1103/PhysRevE.111.055302](https://link.aps.org/doi/10.1103/PhysRevE.111.055302)

无法访问文章链接。

---

## 50. Terraform MCP 服务器

**原文标题**: Terraform MCP Server

**原文链接**: [https://github.com/hashicorp/terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server)

Terraform MCP 服务器是一个模型上下文协议 (MCP) 服务器，旨在通过与 Terraform Registry API 集成来增强 Terraform 开发。它实现了与基础设施即代码 (IaC) 的自动化和高级交互。主要用例包括自动化 provider/模块发现、提取注册表数据以及探索模块/资源详细信息。

通过配置 MCP 设置以使用 Docker 运行服务器，该服务器可以与 VS Code 或 Claude Desktop 一起使用。如果 Docker 不可用，可以使用 `make build` 直接从源代码构建服务器。也可以使用 `make docker-build` 创建本地 Docker 镜像。

该服务器为 `providers`（解析 provider 文档 ID 并获取文档内容）和 `modules`（搜索模块并检索详细模块信息）提供工具集。

本文档概述了安装过程、VS Code 和 Claude Desktop 的配置详情，以及从源代码或通过 Docker 构建的说明。它还涵盖了开发方面，例如先决条件（Go、Docker）、使用 `make` 运行测试以及各种 `make` 命令。最后，它解释了贡献项目的流程、许可信息 (MPL-2.0)、安全策略以及用于错误报告、功能请求和一般讨论的支持渠道。包含一项重要警告：用户必须彻底审查动态生成的输出，以确保其符合安全性、成本效益和合规性要求。

---

## 51. 佐德 4

**原文标题**: Zod 4

**原文链接**: [https://zod.dev/v4](https://zod.dev/v4)

Zod 4 发布：性能显著提升，特性丰富

---

## 52. LLM在招聘决策中的行为：候选人选择中的系统性偏见

**原文标题**: The behavior of LLMs in hiring decisions: Systemic biases in candidate selection

**原文链接**: [https://davidrozado.substack.com/p/the-strange-behavior-of-llms-in-hiring](https://davidrozado.substack.com/p/the-strange-behavior-of-llms-in-hiring)

无法访问文章链接。

---

## 53. GitHub Copilot 编码助手

**原文标题**: GitHub Copilot Coding Agent

**原文链接**: [https://github.blog/changelog/2025-05-19-github-copilot-coding-agent-in-public-preview/](https://github.blog/changelog/2025-05-19-github-copilot-coding-agent-in-public-preview/)

GitHub Copilot 编码代理允许用户将编码任务委派给 Copilot，使开发人员能够专注于更复杂的工作。用户可以直接从 GitHub、GitHub Mobile 或 GitHub CLI 将问题分配给 Copilot。然后，Copilot 在后台使用安全云环境，探索存储库，进行代码更改，通过测试验证其工作，并推送更改。完成后，Copilot 标记用户以进行审查，允许通过拉取请求中的评论或本地 IDE 提供反馈和进一步改进。

Copilot 最适合在经过良好测试的代码库中执行低到中等复杂度的任务，包括添加功能、修复错误、扩展测试、重构和改进文档。用户可以同时分配多个问题。

该功能目前适用于 Copilot Pro+ 和 Copilot Enterprise 订阅者，企业用户需要管理员启用该功能。它的使用会消耗 GitHub Actions 分钟数和 Copilot 高级请求。GitHub Mobile 和 CLI 支持正在逐步向用户推出。

截至 6 月 4 日，Copilot 编码代理每次模型请求将使用一个高级请求，并且它仍然是一个预览功能，可能会发生变化。鼓励用户通过链接的讨论提供反馈。

---

## 54. 呆伯特漫画作者斯科特·亚当斯称他将很快死于与乔·拜登相同的癌症。

**原文标题**: Dilbert creator Scott Adams says he will die soon from same cancer as Joe Biden

**原文链接**: [https://www.thewrap.com/dilbert-scott-adams-prostate-cancer-biden/](https://www.thewrap.com/dilbert-scott-adams-prostate-cancer-biden/)

“呆伯特”创作者斯科特·亚当斯宣布罹患前列腺癌晚期，据报道前总统乔·拜登也患有同样的疾病。亚当斯在他的Rumble节目“与斯科特·亚当斯喝咖啡”中透露了这一消息，称他的癌症已扩散到骨骼，预计今年夏天会去世。他指出，虽然局部前列腺癌可以治愈，但一旦扩散就无法治愈。亚当斯凭借“呆伯特”成名，并且越来越直言不讳地发表政治言论，他对拜登及其家人表示同情。文章还强调了亚当斯在社交媒体上的影响力，提到了他在Rumble和X（前身为Twitter）上的粉丝数量。

---

## 55. 一个洗澡时的灵感变成了考拉兹猜想的可视化。

**原文标题**: A shower thought turned into a Collatz visualization

**原文链接**: [https://abstractnonsense.com/collatz/](https://abstractnonsense.com/collatz/)

作者受一次淋浴时的灵感启发，探索了一种考拉兹猜想的可视化方法，即通过将每个数字的奇偶选择序列编码为二进制分数。考拉兹猜想假定，对任何正整数重复应用规则（偶数则除以2，奇数则乘以3加1），最终都会达到1。

为了解决考拉兹序列中偶数偏差的问题，作者使用了“捷径”考拉兹函数，在3n+1步骤后立即除以2。然后，他将每个步骤表示为一个二进制数字（偶数为1，奇数为0），并将这些位序列转换为分数。

最初绘制一系列数字的这些“考拉兹分数”时，看起来是均匀分布的。然而，绘制随后的分数对（fn，fn+1）揭示了惊人的自相似模式，类似于外星文字。作者鼓励探索这些模式，并提供了一个带有着色规则的交互式工具。

有趣的是，作者发现，尽管他采用了独特的方法，但这种可视化方法已经被探索过了。他引用了Olivier Rozier 2019年的论文和Yukihiro Hashimoto 2007年的论文，这两篇论文都包含了来自2-adic数的相同图。虽然他们的方法与作者的直接分数方法不同，但产生的视觉效果是相同的。作者希望这种易于理解的可视化方法能够激发人们对考拉兹猜想的新见解。

---

## 56. 内存一致性模型：教程

**原文标题**: Memory Consistency Models: A Tutorial

**原文链接**: [https://jamesbornholt.com/blog/memory-models/](https://jamesbornholt.com/blog/memory-models/)

本文提供了一个关于内存一致性模型的教程，解释了为什么它们对于理解多核系统中并行线程如何与共享内存交互至关重要。它首先阐述了在并发操作中保持顺序所面临的挑战，展示了看似直观的程序执行如何导致意想不到的结果。

本文介绍了顺序一致性（SC）作为一种简单的模型，其中所有操作似乎都以单一、有序的序列发生，并在每个线程中保留程序顺序。然而，由于其严格的排序要求，SC效率低下，阻碍了并行执行。

然后介绍了连贯性的概念，保证对同一内存位置的所有写入都以相同的顺序被所有线程看到。本文接着讨论了宽松内存模型，例如总存储顺序（TSO），它允许使用存储缓冲区来提高性能，从而隐藏写入延迟。虽然TSO提高了速度，但它可能导致与SC预期相悖的行为。

本文进一步深入探讨了像ARM这样的较弱的内存模型，强调了当必要时需要像屏障（或栅栏）这样的同步机制来强制排序。屏障确保屏障之前的所有内存操作在屏障之后的任何操作开始之前完成。最后，本文讨论了编译器在重新排序内存操作中的作用，并强调了C++和Java等编程语言中内存模型的重要性，以在并行程序中保持可预测的行为。

---

## 57. 设想一个所有文件始终以所有文件类型存在的驱动器。

**原文标题**: Imagine a drive where every file exists as all file types all of the time

**原文链接**: [https://anydocai.com/](https://anydocai.com/)

文章题为“想象一下，每次驱动都存在所有文件类型的文件”，介绍了AnydocAI，一个概念（或可能是一个产品），似乎允许通用文件类型转换和可访问性。标题立即暗示了一种激进的文件管理方法，表明一个单一文件同时以所有可能的格式隐式存在的系统。

虽然极短的内容（仅名称“AnydocAI”）没有提供明确的细节，但其隐含的前提是革命性的。它消除了手动文件转换或担心软件兼容性的需要。用户无需将.docx转换为.pdf或将.jpg转换为.png；相反，任何文件都可以按需以任何所需格式访问和使用。

这个概念对协作、归档和整体数字工作流程具有巨大的影响。文件格式限制和软件依赖性造成的摩擦将大大减少。然而，这样一个系统的可行性引发了关于存储空间、处理能力以及复杂文件交互的可能性的问题。

---

## 58. WireGuard 自定义密钥生成器

**原文标题**: WireGuard vanity keygen

**原文链接**: [https://github.com/axllent/wireguard-vanity-keygen](https://github.com/axllent/wireguard-vanity-keygen)

本文介绍 `wireguard-vanity-keygen`，一个用于生成符合特定前缀或模式的 WireGuard 私钥和公钥的命令行工具，它提供了一种在 WireGuard 服务器上直观识别连接的方法。该工具支持多核处理、区分大小写或正则表达式搜索，以及限制结果数量。

本文解释了如何使用该工具，包括各种选项，如 `-c` 用于区分大小写搜索，`-t` 用于设置线程数，以及 `-l` 用于限制结果数量。文章提供了示例用法，以及基于基准 CPU 速度的概率和预计运行时的讨论。文章还包括查找不同长度密钥的计时，以及对大小写敏感性和搜索词数量的考虑。

文章还详细介绍了使用正则表达式进行更复杂搜索的方法。常见问题解答部分回答了关于有效搜索字符、概率计算以及该工具用途的常见问题。总而言之，`wireguard-vanity-keygen` 提供了一种可定制且高效的方式来生成具有特定、可识别前缀的 WireGuard 密钥，从而改进服务器管理。

---

## 59. 悼念：Cryptome联合创始人约翰·L·杨

**原文标题**: In Memoriam: John L. Young, Cryptome Co-Founder

**原文链接**: [https://www.eff.org/deeplinks/2025/05/memoriam-john-l-young-cryptome-co-founder](https://www.eff.org/deeplinks/2025/05/memoriam-john-l-young-cryptome-co-founder)

Cryptome联合创始人、官方机密先锋在线图书馆的共同创建者约翰·L·杨去世，享年89岁。杨和他的妻子黛博拉·纳西奥斯于1996年创建了Cryptome，旨在公开政府和企业隐藏的信息，倡导言论自由、隐私和政府透明度。他们的口号是“对民主的最大威胁是偏袒少数人的官方保密。”

Cryptome成为了政府、法院和公司事务文件的重要资源，尤其是在20世纪90年代的“密码战争”期间，当时活动家们为加密自由而战。该网站最初也支持维基解密，但杨后来因担心货币化而疏远了自己，最终公布了维基解密的内部电子邮件。

杨曾接受过建筑师培训，长期以来一直倡导公共利益和透明度，寻求获取有关公共发展实体的文件。他的专业知识使他创建了Cryptome，这是一个塑造互联网信息基础设施的关键辩论的实时档案。尽管面临来自联邦调查局、特勤局和科技公司的压力，杨仍然坚定地倡导公众获取信息。他还参与创建了社区服务团体Urban Deadline。

这篇文章强调了杨在数字时代坚定不移地致力于实现信息获取民主化，巩固了他作为互联网上一个未被充分认识的英雄的遗产。他对公众知情权的奉献精神将被人们深深怀念。

---

## 60. 关于Deno消亡的说法纯属夸大其词

**原文标题**: Reports of Deno's Demise Have Been Greatly Exaggerated

**原文链接**: [https://deno.com/blog/greatly-exaggerated](https://deno.com/blog/greatly-exaggerated)

Deno之死被严重夸大：Ryan Dahl回应批评并阐明Deno发展方向

Ryan Dahl在一篇名为“Deno之死被严重夸大”的文章中，回应了近期的批评，并阐明了Deno及其相关产品的未来发展方向。尽管存在担忧，但由于Node兼容性的提高，自Deno 2发布以来，Deno的使用量已经增加了一倍以上。

Dahl解释说，减少Deno Deploy区域是基于使用模式的战略决策。他们没有专注于广泛的边缘存在，而是优化速度、数据邻近性和合规性，从而将Deploy发展成为一个托管应用程序而非仅仅是函数的平台。诸如子进程、后台任务以及将应用程序固定到特定区域的能力等新功能即将推出。

Deno KV将继续保持测试版，作为一个零配置的全局存储，但并不打算成为一个通用的数据库。团队正在努力使传统的关系型数据库更容易与Deno Deploy一起使用，并且正在探索一个新项目，以紧密集成计算和状态。

全栈Web框架Fresh也依然充满活力，Fresh 2将于今年晚些时候推出，并将带来重大改进。

Dahl强调，Deno是一个完整的平台，具有内置的TypeScript/JSX支持、细粒度权限、LSP支持、Jupyter集成、独立二进制文件生成、Node/npm兼容性、OpenTelemetry等功能。其目标是改进JavaScript开发，提供一个有凝聚力、开箱即用的系统。Deno正在通过JSR治理、对TC39/WinterTC的贡献以及挑战Oracle JavaScript商标来积极改进JavaScript生态系统。新的产品也在开发中，有望简化持久化、分布式应用程序。

---

## 61. 耐心廉价到无需计量

**原文标题**: Patience too cheap to meter

**原文链接**: [https://www.seangoedecke.com/patience-too-cheap-to-meter/](https://www.seangoedecke.com/patience-too-cheap-to-meter/)

本文认为，虽然智能是大语言模型（LLM）发展的关键焦点，但其最具变革性的能力可能是其超人的耐心，这种耐心现在唾手可得且“极其廉价”。

作者指出，尽管有像Claude Sonnet这样更智能的模型，但许多用户对ChatGPT等基本模型感到满意。这表明原始智能并非用户采用的主要驱动因素。相反，作者认为耐心才是真正的价值所在。

作者引用了一篇关于使用ChatGPT进行治疗的文章，强调LLM提供了随时可用、不带偏见且无限耐心的陪伴。对于寻求情感支持或建议的用户来说，这一点尤其具有吸引力，即使这些建议可能不需要卓越的智能。即使不太智能的模型也能有效，因为它们愿意倾听而不感到沮丧。

文章也承认了潜在的缺点。作者担心无限的耐心可能会放大LLM建议中现有的缺陷，例如谄媚。人们还担心用户会用缺乏适当升级途径的LLM取代人类治疗师，以及用户可能会对人类互动中有限的耐心感到沮丧。

最终，文章得出结论，无限耐心事物的持续存在是人类历史上一种新颖的发展，其影响可能比追求LLM中不断增长的智能更大。作者还认为，耐心是LLM成为有效导师的关键原因。

---

## 62. Telum II 在 Hot Chips 2024 大会：采用独特缓存策略的大型主机

**原文标题**: Telum II at Hot Chips 2024: Mainframe with a Unique Caching Strategy

**原文链接**: [https://chipsandcheese.com/p/telum-ii-at-hot-chips-2024-mainframe-with-a-unique-caching-strategy](https://chipsandcheese.com/p/telum-ii-at-hot-chips-2024-mainframe-with-a-unique-caching-strategy)

本文分析了在Hot Chips 2024上发布的IBM Telum II大型机处理器，重点介绍了其独特的、专注于单线程性能的缓存策略。与典型的服务器CPU不同，Telum II优先考虑高时钟速度（5.5 GHz）和仅八个核心上的高达360 MB的片上缓存。

一项关键创新是“虚拟L3缓存”，它利用处理器十个大型36MB L2缓存来避免数据重复并最大化缓存利用率。每个L2都有一个“饱和度指标”，用于确定哪个L2是逐出缓存行的最佳目的地，从而有效地创建了一个分布在L2切片上的共享L3池。这种方法降低了专用、更大的L3缓存相关的面积和功耗成本。

Telum II通过“虚拟L4缓存”进一步扩展了这个概念，它是一个由将L3牺牲者发送到中央处理器复合体 (CPC) 抽屉内的其他Telum II芯片形成的2.8 GB池。这旨在最大限度地减少跨多处理器系统的延迟。

本文将Telum II的方法与典型的服务器和客户端CPU设计进行了对比，指出IBM已战略性地减少了核心数量，以通过最大化每个核心的可用缓存来优先考虑单线程性能。它讨论了通过增加缓存大小并在核心之间共享缓存，将类似策略应用于客户端CPU的可能性。

---

## 63. 微软封锁了国际刑事法院首席检察官的电子邮件账户。

**原文标题**: Microsoft blocked the email account of Chief Prosecutor of the ICC

**原文链接**: [https://www.heise.de/en/news/Criminal-Court-Microsoft-s-email-block-a-wake-up-call-for-digital-sovereignty-10387383.html](https://www.heise.de/en/news/Criminal-Court-Microsoft-s-email-block-a-wake-up-call-for-digital-sovereignty-10387383.html)

以下是根据标题对文章的总结：

文章报道微软封锁了国际刑事法院（ICC）首席检察官卡里姆·汗的电子邮件账户。此举引发了重大争议，并引发了人们对数字主权以及私营科技公司对国际司法影响的担忧。

虽然根据现有背景（仅基于标题），封锁的具体原因仍然有些不清楚，但文章可能探讨了像微软这样的大型科技公司拥有限制如此高调的国际法人物的通信访问权的影响。

由heise online发表的这篇文章将这一事件定义为关于数字主权的“警钟”。这表明该事件突显了国际机构和个人对受国家法律和潜在地缘政治压力影响的实体（如微软）控制的基础设施的依赖。这种依赖性可能会产生漏洞并引发对公正性的质疑。

文章可能深入探讨了该事件的潜在后果，可能包括：

*   妨碍国际刑事法院的工作和调查。
*   影响法院的完整性和独立性。
*   对其他依赖数字通信工具的国际组织和个人产生更广泛的影响。
*   国际机构需要更大的数字主权和对数据基础设施的控制权。

---

## 64. 在本地运行 GitHub Actions

**原文标题**: Run GitHub Actions locally

**原文链接**: [https://github.com/nektos/act](https://github.com/nektos/act)

本文介绍`act`，一个允许用户在本地运行GitHub Actions的工具，它提供快速反馈并充当本地任务运行器。`act`允许开发者在本地运行和测试这些工作流程，从而模拟GitHub提供的环境，而无需不断地提交和推送代码来测试GitHub Actions工作流程中的更改。它从`.github/workflows/`目录读取工作流程定义，根据这些定义拉取或构建必要的Docker镜像，并在Docker容器中执行这些action，模拟GitHub环境。

主要优点包括：

*   **快速反馈：** 无需推送到GitHub即可立即测试工作流程更改。
*   **本地任务运行器：** 利用GitHub Actions定义来替换Makefile以进行任务执行。
*   **VS Code 集成：** VS Code 扩展允许直接从编辑器管理和运行`act`。

本文概述了`act`的工作原理，包括读取工作流程文件、准备Docker镜像、根据依赖关系确定执行路径以及为每个action运行容器。文章还提供了指向act用户指南、支持渠道、贡献指南以及从源代码构建`act`的说明的链接。

---

## 65. 扩散模型简述

**原文标题**: Diffusion models explained simply

**原文链接**: [https://www.seangoedecke.com/diffusion-models-explained/](https://www.seangoedecke.com/diffusion-models-explained/)

本文介绍了扩散模型，它是人工智能图像生成背后的关键技术。与预测序列中下一个token的Transformer不同，扩散模型学习逆转向图像添加噪声的过程。

训练涉及向模型输入带噪声的图像和文本描述，要求它预测添加的噪声。然后，模型会因准确的预测而获得奖励。推理始于纯噪声和文本描述。模型迭代地识别并去除噪声层，从而揭示生成的图像。

该过程通常涉及变分自编码器（VAE），用于将图像压缩成更小的、随机外观的张量，以实现高效处理。无分类器引导用于确保模型专注于文本描述，方法是有时在没有文本描述的情况下进行训练，然后在推理过程中混合结果。

扩散模型与Transformer的不同之处在于，它在每个步骤都对整个图像进行操作，从一个“空白画布”噪声开始，并编辑之前的输出。它们提供了一个内置的质量旋钮；提前停止会产生更快、更嘈杂的图像，而继续处理则会提高质量。

本文将该概念扩展到视频，其中整个视频剪辑被视为一个噪声张量。文本扩散更为复杂，涉及向文本嵌入添加噪声。将这些嵌入转换回文本提出了挑战。

---

## 66. 高瓦纳斯河的微生物教你对抗工业污染

**原文标题**: Microbes in Gowanus teach lessons on fighting industrial pollution

**原文链接**: [https://engineering.nyu.edu/news/microbes-brooklyn-superfund-site-teach-lessons-fighting-industrial-pollution](https://engineering.nyu.edu/news/microbes-brooklyn-superfund-site-teach-lessons-fighting-industrial-pollution)

纽约大学坦登学院主导的研究发现，布鲁克林高瓦纳斯运河（一个超级基金场地）中的微生物具有非凡的基因适应能力，能够对抗工业污染。这项发表在《应用微生物学杂志》上的研究确定了455种微生物物种，它们利用64种生化途径降解污染物，并利用1171个基因处理重金属。研究人员还发现了2300多个新的基因序列，这些序列可能对医药、工业和环境应用具有价值。

与传统的疏浚方法相比，这一发现为更便宜、更可持续的清理方法提供了潜力。然而，该研究还揭示了抗生素耐药基因，其中一些源于人类污水，引发了公众健康担忧。尽管如此，研究人员强调了从这些微生物中学习的潜力，无论是通过分离特定菌株还是增强它们的能力，以开发更快、更有效的生物修复技术，用于污染物分解，甚至资源回收。

该研究涉及从运河沿线的14个地点进行广泛采样，并建立在过去十年的研究基础上。该团队确定了能够分解各种污染物的微生物，包括石油产品和多氯联苯。为了分享他们的发现，研究人员在BioBAT艺术空间创作了一个沉浸式艺术装置CHANNEL，展示了对该水道的微生物研究。该研究强调了理解微生物适应性对于环境修复和潜在资源回收的重要性。

---

## 67. 三维透明度预计算排序

**原文标题**: Precomputing Transparency Order in 3D

**原文链接**: [https://jacobdoescode.com/2025/05/18/precomputing-transparency-order-in-3d](https://jacobdoescode.com/2025/05/18/precomputing-transparency-order-in-3d)

本文探讨了一种预先计算半透明3D面片渲染顺序的方法，以避免每帧基于相机距离的CPU排序。作者提出了一种基于面剔除和分析面片对之间空间关系的技术。

其核心思想是将每个半透明面片分割成两个面，每个面的朝向彼此相反。通过分析面片B的顶点是否完全高于、完全低于、相交或共面于面片A的平面，反之亦然，可以*独立于*相机位置确定一个*部分*排序。

具体而言，如果B的顶点完全高于A的平面，且A的顶点完全低于B的平面，则必须先渲染A，然后渲染B。如果面片在两个方向上都相交，则无法进行预排序，需要回退到CPU排序。共面面片不需要排序。

该算法涉及检查每个面片与其他每个面片的关系，导致O(n²)的复杂度，适用于静态或大部分静态的半透明对象。由于并非总是能够实现完全排序，因此预排序会产生面片对之间的约束，而不是完整的排序列表。作者建议只需对需要CPU排序的面片组进行动态排序，从而可能提高性能。提供了一个Three.js演示来展示该概念。

---

## 68. 使用 Docker Compose 自托管 Moose，搭配 Redis、Temporal、Redpanda 和 ClickHouse

**原文标题**: Self-Hosting Moose with Docker Compose, Redis, Temporal, Redpanda and ClickHouse

**原文链接**: [https://docs.fiveonefour.com/moose/deploying/self-hosting/deploying-with-docker-compose](https://docs.fiveonefour.com/moose/deploying/self-hosting/deploying-with-docker-compose)

本文是一份全面的指南，指导如何在单台Ubuntu服务器上使用Docker Compose自托管Moose应用程序（一个基于Moose框架的应用程序）。它概述了设置生产级环境所需的步骤，包括ClickHouse、Redis、Redpanda（可选，用于事件流）和Temporal（可选，用于工作流编排）等依赖项。

本指南涵盖：

*   **先决条件：** Ubuntu 24+、Docker、Docker Compose，以及一台具有足够资源的服务器。
*   **安装：** 安装Docker、Node.js/Python，并配置Docker日志大小限制。
*   **可选设置：** 设置GitHub Actions runner用于CI/CD，以及在需要时创建一个基本的Moose应用程序。
*   **部署准备：** 创建 `.env` 和 `.env.prod` 文件，用于组件版本和应用程序特定的密钥。
*   **Docker Compose部署：** 创建一个 `docker-compose.yml` 文件，用于定义和编排各种服务。
*   **生产配置：** 安全地配置ClickHouse，包括创建专用用户帐户，并相应地更新Moose的环境变量。

本文强调使用Docker Compose简化部署和生命周期管理，同时强调安全性和正确配置每个服务的重要性。它还承认单服务器设置的局限性，并简要提及Boreal，这是一种针对Moose的托管HA部署选项。本指南包括每个步骤的详细说明和配置示例。

---

## 69. 不要使用 ISO/IEC 14977:1996 扩展巴科斯-瑙尔范式 (EBNF) (2023)

**原文标题**: Don't Use ISO/IEC 14977:1996 Extended Backus-Naur Form (EBNF) (2023)

**原文链接**: [https://dwheeler.com/essays/dont-use-iso-14977-ebnf.html](https://dwheeler.com/essays/dont-use-iso-14977-ebnf.html)

David A. Wheeler 认为不应使用 ISO/IEC 14977:1996 扩展巴科斯范式 (EBNF) 定义语言，理由是其存在严重的技术缺陷以及 ISO 的不当行为。

技术缺陷包括无法直接表示国际/Unicode 字符或码位，缺乏标准字符范围表示法，需要过多的逗号导致语法难以阅读，没有建立在广泛使用的正则表达式表示法之上，以及具有一种奇怪且容易被误解的“一个或多个”表示法。 该规范也很难理解，其中许多关键术语未定义。

Wheeler 将 ISO/IEC 14977:1996 与 W3C XML 1.0 规范中的 EBNF 表示法进行了不利的对比，后者通过诸如直接 Unicode 码位表示、字符范围和更清晰的语法等功能解决了许多这些缺点。 他还简要提到了 IETF 的 RFC 5234，指出它比 14977 更好，但并非理想。

除了技术问题之外，Wheeler 还批评了 ISO 和 IEC 对 IT 标准收费的做法，认为这使得标准难以获取并阻碍了其使用，特别是对于小型企业和业余爱好者而言。 他指出，即使 ISO 也不总是将 14977 用于其自身的语言标准。 他提倡像 W3C 和 IETF 这样的现代标准制定实践，这些组织免费公开提供其标准。

---

## 70. Authy毁了我的双重验证备份，结果我就得到了这篇烂博客。

**原文标题**: Authy corrupted my 2FA backup and all I got was this lousy blogpost

**原文链接**: [https://cmb.weblog.lol/2025/05/authy-corrupted-my-2fa-backup-and-all-i-got-was-this-lousy-blogpost](https://cmb.weblog.lol/2025/05/authy-corrupted-my-2fa-backup-and-all-i-got-was-this-lousy-blogpost)

作者更换iPhone主板后，从iCloud备份恢复Authy时遇到重大问题，被要求输入从未设置过的“第二备份密码”，导致大量2FA代码（包括AWS和GitLab等关键账户）被锁定。

在新iPad上进行故障排除使问题更加严重，锁定了更多代码。Authy的支持团队（最初是聊天机器人）提供的建议基于过时信息，毫无帮助。由于可能永久丢失数据以及缺乏有效支持，作者感到沮丧，决定将所有2FA代码迁移到1Password。幸运的是，他们拥有关键账户的密钥，这有助于迁移。

巧合的是，Authy发布了新的应用程序更新，安装后，锁定的2FA代码又可以通过原始密码访问。然而，作者已经切换到1Password，认为Authy的可靠性不足以处理敏感的2FA信息。作者强调了依赖可能被忽视支持的免费工具的风险，尤其是在像2FA这样的关键安全功能方面。这篇文章旨在警告可能遇到类似问题的其他人，并强调可靠的2FA管理的重要性。虽然新的更新似乎解决了这个问题，但这次经历促使作者寻求更强大、付费的解决方案，例如1Password。

---

## 71. InventWood即将大规模生产强度超过钢铁的木材。

**原文标题**: InventWood is about to mass-produce wood that's stronger than steel

**原文链接**: [https://techcrunch.com/2025/05/12/inventwood-is-about-to-mass-produce-wood-thats-stronger-than-steel/](https://techcrunch.com/2025/05/12/inventwood-is-about-to-mass-produce-wood-thats-stronger-than-steel/)

InventWood公司（一家从马里兰大学获得技术授权的初创公司）正准备大规模生产“超级木材”，这是一种比钢更坚固的木材处理产品。该工艺由材料科学家胡良兵发明，现在只需几个小时，它使用“食品工业”化学品和压缩技术来强化普通木材中的纤维素，从而创造出一种具有优于钢的抗拉强度和强度重量比的材料。

InventWood公司已筹集了1500万美元的A轮融资，用于建造其第一家商业工厂，该工厂最初将专注于建筑物的幕墙材料。该公司的长期目标是制造替代混凝土和钢材的结构梁，从而显著减少建筑业的碳足迹。“超级木材”的防火等级为A级，具有防腐防虫性，并且可以稳定用于户外。压缩过程还能浓缩木材的天然颜色，使其具有丰富的热带硬木外观。该公司的目标是用木屑生产任何尺寸的结构梁，从而无需进行表面处理。

---

## 72. 苏格兰女王玛丽频道变形幻影3D模拟

**原文标题**: Mary Queen of Scots Channel Anamorphosis, a 3D Simulation

**原文链接**: [https://www.charlespetzold.com/blog/2025/05/Mary-Queen-of-Scots-Channel-Anamorphosis-A-3D-Simulation.html](https://www.charlespetzold.com/blog/2025/05/Mary-Queen-of-Scots-Channel-Anamorphosis-A-3D-Simulation.html)

本文详细介绍了作者如何创建爱丁堡苏格兰国家肖像美术馆中玛丽女王频道变形画作的3D模拟过程。受对数书籍研究的启发，作者深入研究了约翰·纳皮尔作品的政治背景，偶然发现了这幅画作，该画作描绘了一个从女人脸到骷髅头的转变图像。

这幅画作可以追溯到1580年，是一幅由棱镜组成的旋转画。作者的目标是使用WebGL以数字方式重现这种效果。他参考了一项研究，确认棱镜的角度为45°、45°和90°，并利用这些信息构建了一个虚拟棱镜面板。

然后，他使用了国家美术馆网站提供的两张画作图像，并获得了个人使用许可。由于这些图像显示了重叠的视角，他使用自定义的C#程序手动提取和优化图像，分离出脸部和骷髅头视角。这些精炼后的图像随后被合并成交替的条纹，并叠加到3D棱镜面板上。最终的交互式结果允许观看者滑动图像，观察从脸到骷髅头的转变，模仿原始画作的变形效果。作者还提供了用于3D渲染的JavaScript源代码。

---

## 73. 河流

**原文标题**: Rivers

**原文链接**: [https://www.futilitycloset.com/2025/05/15/rivers/](https://www.futilitycloset.com/2025/05/15/rivers/)

这篇文章将排版中的“河流”定义为在齐行文本中可能出现的视觉干扰性空白，尤其是在等宽字体中，当单词之间的间隙在多行中垂直对齐时。排字员会尽量避免它们，有时会将页面倒置以更好地检测这些视觉瑕疵。虽然长的“河流”并不常见，但文章强调了达尔文《贝格尔号航行记》中发现的一个12行示例，并提到了Fritzi Striebel在1986年《文字之路》杂志上发表的一系列不寻常的“河流”。本质上，这篇文章定义并说明了排版中一个不受欢迎的审美问题。

---

## 74. 神秘的

**原文标题**: Mystical

**原文链接**: [https://suberic.net/~dmm/projects/mystical/README.html](https://suberic.net/~dmm/projects/mystical/README.html)

Mystical：一种将PostScript代码表示为由环、符号和文本构成的魔法圆圈的可视化编程语言概念。代码结构通过具有内外边界的环形带来表示。不同类型的环代表PostScript的可执行数组、非可执行数组和字典。代码流遵循逆时针方向。

符号是运算符、变量或关键字的符号表示，取代了PostScript名称。字符串被表示为饰框。为常见的PostScript运算符定义了一组标准符号，用户可以为新函数和变量创建自定义符号。存在一种特殊的连字，用于在可执行数组中定义命名函数。

本文档提供了以Mystical渲染的符号和算法示例，突出了其可视化特性。"mystical.ps"中提供了将PostScript代码渲染为Mystical图表的函数，包括缩放和布局调整。当前的实现更像是一种PostScript的可视化表示，而不是一种独立的、可执行的语言。这个概念有可能应用于其他基于运算符的语言，如Forth，但具有更复杂语法的语言可能会带来挑战。

---

## 75. 报纸正在推荐人工智能虚构的小说

**原文标题**: Newspapers Are Recommending AI-Hallucinated Novels

**原文链接**: [https://countercraft.substack.com/p/newspapers-are-recommending-ai-hallucinated](https://countercraft.substack.com/p/newspapers-are-recommending-ai-hallucinated)

好的，我已阅读了这篇文章。以下是摘要：

Countercraft的文章《报纸正在推荐人工智能“幻想”小说》揭露了一个令人不安的趋势：报纸和文学刊物正在推荐和评论人工智能生成的书籍，有时甚至没有意识到它们的真正来源。作者重点介绍了几个例子，这些书要么是由人工智能明确编写的，要么是大量使用人工智能工具辅助创作的，随后在信誉良好的媒体上受到称赞。

核心问题是，这些人工智能生成的书籍通常包含事实错误、无意义的情节和不一致之处，作者将其称为“幻想”，与用来描述人工智能捏造信息的术语相呼应。尽管存在这些缺陷，这些书还是被当作人类作者创作的合法小说来呈现，并且在某些情况下，因其明显的创造力和原创性而受到赞扬。

这篇文章批评了对这些书籍缺乏批判性审查，暗示评论家可能优先考虑新颖性，或者未能正确评估写作质量。它还提出了关于人工智能时代透明度和作者身份的伦理问题。作者认为，对于评论家和读者来说，了解人工智能参与书籍创作的可能性并应用适当的评估标准至关重要，尤其是在事实准确性和连贯性方面。最终，这篇文章警告说，不加批判地接受人工智能生成的书籍可能会损害文学批评的信誉和人类创造力的价值。

---

## 76. Show HN: 一款集成了待办/完成跟踪的原生 Hacker News 阅读器

**原文标题**: Show HN: A native Hacker News reader with integrated todo/done tracking

**原文链接**: [https://github.com/haojiang99/hacker_news_reader](https://github.com/haojiang99/hacker_news_reader)

这个 Show HN 介绍了一个用 Rust 和 egui 构建的原生桌面 Hacker News 阅读器。它提供了一个简洁、现代的界面，用于浏览各种 HN 版块（热门、最新、展示、提问、招聘、最佳），具有诸如线程评论、自动折叠、可调节字体大小、搜索/过滤、暗/亮模式、离线缓存和收藏等功能。

主要功能包括基于分数进行颜色编码的故事、用于导航和操作的键盘快捷键（例如使用“T”和“D”将项目标记为待办/完成），以及用于管理收藏的侧边栏。该应用程序每个版块最多显示 150 个故事，显示标题、域名、作者、分数、发布时间和评论数等基本信息。评论视图提供了一个带有可折叠线程的线程显示、可调节字体大小、作者突出显示和保留的 HTML 格式。

安装需要 Rust (1.70+) 和 Cargo。应用程序架构包括一个 UI 层 (main.rs)、用于故事和评论的数据模型 (models.rs) 以及一个使用 `reqwest` 和 `scraper` 进行数据获取和解析的 HN 客户端 (hn_client.rs)。该项目在 MIT 许可下获得许可，并感谢 Hacker News、egui、reqwest 和 scraper 的贡献。

---

## 77. Show HN: 一个使用 RustPython 在 WASM VM 中评估 Python 代码的 MCP 服务器

**原文标题**: Show HN: A MCP server to evaluate Python code in WASM VM using RustPython

**原文链接**: [https://github.com/tuananh/hyper-mcp/tree/main/examples/plugins/eval-py](https://github.com/tuananh/hyper-mcp/tree/main/examples/plugins/eval-py)

这篇“Show HN”帖子介绍了一个由tuananh开发的名为`hyper-mcp`的项目。该项目提供一个服务器，可以使用RustPython在WebAssembly (WASM) 虚拟机中评估Python代码。本质上，它是一项服务，允许您在沙盒化的WASM环境中运行Python代码。

该项目是开源的，托管在GitHub上的仓库`tuananh/hyper-mcp`中。它已经引起了相当大的兴趣，截至发帖时，已获得533颗星和35个分支。

虽然帖子本身很简短，但该项目可能解决了需要安全隔离地执行Python代码的场景，可能用于用户提交的脚本、沙盒应用程序或在传统Python解释器不适用的环境中运行Python。WASM的安全性和RustPython的Python运行时结合使其成为一种潜在的强大且通用的解决方案。

---

## 78. 欺骗Stack Exchange的数学家克莱奥

**原文标题**: Cleo, the mathematician that tricked Stack Exchange

**原文链接**: [https://en.wikipedia.org/wiki/Cleo_(mathematician)](https://en.wikipedia.org/wiki/Cleo_(mathematician))

克莱奥（Cleo）是2013年至2015年间数学栈溢出（Math.SE）上的匿名用户，因提供正确但无证明的复杂积分问题答案而闻名。该用户的身份和能力引发了激烈的争论，人们猜测其身份从个人天才到早期人工智能系统不等。

克莱奥的个人资料声称是一位患有疾病而无法详细解释的女数学家。两年多来，克莱奥发布了39个答案，经常迅速解决那些难倒其他人的问题。一个著名的例子是解决了一个包含黄金比例封闭形式解的复杂积分，而没有提供任何中间步骤。虽然答案正确，但缺乏解释引起了社区内的争议。

关于克莱奥身份的各种理论层出不穷，包括猜测她可能是像玛丽安·米尔扎哈尼这样的著名数学家，甚至是人工智能。Reddit用户在2023年进行的一项调查将克莱奥与多个账户联系起来，包括Vladimir Reshetnikov和Laila Podlesny的账户。

2025年，Joe McCann的YouTube调查揭示了克莱奥的真实身份：Vladimir Reshetnikov，一位来自乌兹别克斯坦的软件开发人员。在一名观众发现相关账户之间共享的电子邮件恢复地址后，Reshetnikov确认了自己的身份。Reshetnikov表示，他创建克莱奥这个角色是为了激发人们对论坛上很少受到关注的数学问题的兴趣，并鼓励其他人发展自己的问题解决方法。

---

## 79. 从零开始的Llama (2023)

**原文标题**: Llama from scratch (2023)

**原文链接**: [https://blog.briankitano.com/llama-from-scratch/](https://blog.briankitano.com/llama-from-scratch/)

从零实现Llama (2023): 一人构建简化版Llama并用TinyShakespeare数据集训练的历程记录。文章强调迭代和工程化的方法。

作者提倡从小处着手，单独测试各个组件，逐步构建完整模型。关键技巧包括编写辅助函数进行量化评估（数据分割、损失绘图），对模型进行定性评估，使用`.shape`和断言进行调试，最初在没有矩阵乘法的情况下解决问题，以及测试具有特定属性的层。

文章逐步介绍如何建立一个基本的feed-forward神经网络作为基线，然后逐步纳入Llama架构的特性。作者最初遇到了基础模型的问题，突出了理解张量形状和使用正确的损失函数（交叉熵）的重要性。在修复损失函数后，他们添加了一个生成函数进行定性评估。

文章随后计划纳入Llama架构的三个具体特性：用于预归一化的RMSNorm，旋转嵌入和SwiGLU激活函数，首先从RMSNorm开始。作者提供了RMSNorm层初始设置和测试的代码片段，以确保其功能符合预期，强调了验证每个组件的重要性。

---

## 80. KDE 终于要迎来一个名为“Karton”的原生虚拟机管理器了

**原文标题**: KDE is finally getting a native virtual machine manager called “Karton”

**原文链接**: [https://www.neowin.net/news/kde-is-finally-getting-a-native-virtual-machine-manager-called-karton/](https://www.neowin.net/news/kde-is-finally-getting-a-native-virtual-machine-manager-called-karton/)

KDE Plasma将推出原生虚拟机管理器“Karton”，旨在提供比virt-manager或GNOME Boxes等现有方案更集成化的体验。该项目最初由Aaron Rainbolt发起，后由Harald Sitter接手，目前由Derek Lin作为Google Summer of Code (GSoC)项目积极开发。

Karton使用Qt Quick和Kirigami构建，利用libvirt API管理虚拟机，并可能支持多个平台。当前开发重点是核心功能，包括使用libosinfo进行精确操作系统镜像检测和libvirt XML生成的新域安装程序。Lin还在使用Qt Quick创建自定义SPICE查看器。

Lin的GSoC交付成果包括通过libvirt XML配置虚拟机、具有微调控制选项的用户友好型UI、虚拟机快照、直观的虚拟机显示、聚合UI（移动友好）、改进的虚拟机状态更新、用于操作系统选择的浏览工具、资源使用情况图表以及使用会话和系统权限连接到QEMU的能力，从而可能支持非KVM后端。

GSoC编码期从2025年6月2日开始，计划在7月中旬完成可用的应用程序，并在2025年9月1日提交最终版本。

---

## 81. 用 WebGL 可视化地球的十万年

**原文标题**: Visualizing 100k Years of Earth in WebGL

**原文链接**: [https://technistuff.com/posts/visualizing-100000-years-of-earth-in-webgl/](https://technistuff.com/posts/visualizing-100000-years-of-earth-in-webgl/)

本文详细介绍了如何创建一个交互式WebGL模型，以可视化地球过去10万年的地理环境，重点关注气候和海平面变化对人类历史的影响。作者使用了科学数据集，包括海拔（ETOPO）、海平面（NOAA 古气候学项目）、气候（降雨和温度模拟）以及冰盖位置（全球冰盖重建）。

该过程涉及大量数据处理，包括降采样海拔数据、将海平面信息压缩成二进制文件，并将气候数据编码为2D纹理数组以供GPU加载。该模型使用THREE.js和自定义着色器进行渲染，这些着色器可以根据海平面、温度和降雨数据动态调整陆地/水体的颜色。

冰盖位置的渲染方法是将NetCDF数据转换为三角网格，使用的技术包括洪水填充、边缘检测、平滑、Delaunay三角剖分，然后将这些三角形投影到球体上。现代国家边界是使用世界行政边界数据集添加的，并进行了平滑处理以提高渲染效率。

最终生成的交互式地球模型允许用户可视化不断变化的景观，例如白令海峡陆桥和多格兰，从而深入了解人类迁徙和淹没的考古遗址。作者希望通过更准确的数据、历史事件和进一步的渲染优化来增强该模型。提供在线演示。

---

## 82. 展示HN：为我的后朋克乐队制作的Windows 98主题单HTML文件网站

**原文标题**: Show HN: Windows 98 themed website in 1 HTML file for my post punk band

**原文链接**: [https://corp.band](https://corp.band)

这个"Show HN"帖子介绍了一个以Windows 98为主题的网站，该网站用单个HTML文件构建，专为后朋克乐队CORP而设计。 该网站作为乐队在线形象和内容的中心枢纽。

该网站设计有可供用户打开和关闭的互动“窗口”，模拟经典的Windows 98界面。 这些窗口提供对各种部分的访问，例如：

*   **音乐:** CORP在Spotify、Apple Music、YouTube Music和Bandcamp上的音乐链接。 包括一首精选曲目“Whispers from the Water Cooler”。
*   **活动:** 通过Songkick和Bandsintown链接到即将举行的演出。
*   **社交:** 乐队的Instagram、LinkedIn、YouTube和Facebook账户的链接，并附有一条神秘的、公司主题的消息，鼓励粉丝关注。
*   **商品:** 在Bandcamp上出售CORP品牌商品。
*   **邮件列表:** 用于注册加入乐队邮件列表的表格。
*   **预订:** CORP的预订联系方式以及其电子新闻资料包的链接。
*   **回收站:** 一个有趣的空回收站。
*   **机密:** 一个“仅限行政人员”的部分，其中包含查看源代码、切换暗黑模式、激活全屏和运行监视协议（可能只是个玩笑）的选项。
*   **链接:** 直接链接到特定歌曲和CORP的LinkedIn页面。

整体基调是讽刺性的和公司讽刺性的，反映了乐队的后朋克美学。 网站的设计和内容为粉丝们创造了独特的、引人入胜的在线体验。

---

## 83. 证据表明是单一的骗局制造者创造了“皮尔当人”（2016年）

**原文标题**: Evidence suggests a single hoaxer created 'Piltdown man' (2016)

**原文链接**: [https://royalsocietypublishing.org/doi/10.1098/rsos.160328](https://royalsocietypublishing.org/doi/10.1098/rsos.160328)

2016年英国皇家学会开放科学文章《证据表明“皮尔当人”系一人伪造》运用法医学和统计分析的先进技术，提供了强有力的证据，表明臭名昭著的皮尔当人骗局是由一个人所为。

先前的研究曾认为有多个罪魁祸首参与了伪造。然而，这项研究重新审查了证据，重点是对伪造骨骼（一个人类头骨和一个猩猩下颚）上的工具痕迹进行微观分析。

研究人员利用X射线显微断层扫描和多元统计分析等技术，仔细分析了对化石碎片所做的修改。他们的发现表明，修改和技巧具有一致的模式，表明是同一只手负责改变了头骨和下颚。该研究指出，所有欺诈性标本都一致使用了特定的工具和磨损技术。

虽然这项研究没有明确指出造假者是谁，但它大大缩小了可能性。作者认为，这加强了对主要嫌疑人马丁·辛顿（伦敦自然历史博物馆的动物学家）的指控。辛顿有一个动机——对他在博物馆受到的待遇不满——而且他留下了一个装满化学处理过的骨头的箱子，这些骨头与皮尔当标本非常相似。

该研究得出结论，制造技术的一致性提供了令人信服的证据，反对多人参与，从而加强了皮尔当人欺骗背后存在一个单一、老练的造假者的可能性。与之前的研究相比，所使用的技术提供了更详细和更具统计学意义的分析，从而对骗局的性质得出了更强的结论。

---

## 84. 允许我们阻止 Copilot 从我们自己的存储库生成问题（和 PR）。

**原文标题**: Allow us to block Copilot-generated issues (and PRs) from our own repositories

**原文链接**: [https://github.com/orgs/community/discussions/159749](https://github.com/orgs/community/discussions/159749)

这篇GitHub社区帖子表达了对引入Copilot生成的议题和拉取请求的担忧，认为这些内容可能因潜在的低质量、AI生成内容而成为维护者的负担，并违反项目行为准则。发帖人(mcclure)请求添加一个功能，以阻止在特定存储库或整个帐户中提交Copilot生成的内容。

该请求源于GitHub宣布公开预览使用Copilot创建议题和Copilot编码代理。mcclure认为，处理不需要的AI生成内容会浪费维护者、议题提交者（他们可能不知道自己的提交是AI生成的）以及GitHub服务器资源的时间。该用户建议采用一种简单的阻止机制，例如阻止“copilot”机器人，但指出该机器人似乎不受阻止限制。该用户威胁说，如果问题得不到解决，将迁移到像Codeberg这样的替代平台。

其他用户也表达了同样的担忧，其中一位提到需要针对代码中的AI暴露提供法律保护。还提出了对AI生成的问题和PR可能出现的类似DDOS攻击的担忧。一些用户提出了替代解决方案，例如选择加入/退出存储库上的Copilot，或迁移到像Codeberg和Gitea这样的平台（尽管Gitea的AI策略也受到质疑）。 此外，还有人指出，这个问题也适用于标准的“创建新议题”页面，导致出现完全由AI臆想的议题。总体而言，大家的共识是，GitHub应提供工具来管理或禁用每个存储库的Copilot议题/PR生成功能。

---

## 85. 原始森林木材

**原文标题**: Old Growth Wood

**原文链接**: [https://brenthull.com/article/old-growth-wood](https://brenthull.com/article/old-growth-wood)

本文重点介绍了老木和新木在质量和耐用性方面的显著差异，尤其是在窗户建造和修复方面。老木主要于1870年代至1940年代从原始森林中采伐，生长缓慢，因此生长轮紧密（每英寸20-25个），心材比例高。这种缓慢生长转化为卓越的稳定性、耐用性和寿命。用老木制成的窗户，如果保养得当，可以使用100年以上。

相比之下，新木通常来自生长迅速的种植园，例如种植辐射松的种植园，每英寸的生长轮较少（约7个），心材比例较低，并且更容易在短短20年内翘曲和腐烂。本文指出，指接木的使用是这种低质量的结果，制造商试图以此弥补新木材的缺陷。

作者认为，老木的卓越品质是修复历史悠久的窗户而不是用劣质材料制成的新窗户取而代之的有力理由。通过修复这些旧窗户，可以保持其结构完整性，并且有可能再使用一个世纪。

---

## 86. 过多的Go语言误导

**原文标题**: Too Much Go Misdirection

**原文链接**: [https://flak.tedunangst.com/post/too-much-go-misdirection](https://flak.tedunangst.com/post/too-much-go-misdirection)

作者对 Go 在图像解码中处理 `io.Reader` 的方式感到沮丧，尤其是在已经有 `[]byte` 表示的情况下。目标是避免在函数需要 `io.Reader` 但数据已经在字节切片中时进行不必要的内存复制。

作者最初尝试使用 `unsafe.Pointer` 直接访问 `bytes.Reader` 的底层字节切片，但事实证明这还不够，因为如果 `image.Decode` 函数没有实现 `Peek`，它会抢先将 `io.Reader` 包装在 `bufio.Reader` 中。

核心问题：`bytes.Reader` 没有实现 `Peek`，而 `bufio.Reader` 没有公开其底层读取器。如果原始输入是 `bytes.Reader`，这将强制复制数据。

解决方法涉及再次使用 `unsafe.Pointer` 来访问 `bufio.Reader` 的内部字段并提取底层读取器，然后检查它是否为 `bytes.Reader` 以最终直接访问字节切片。

作者批评 Go 的结构类型和标准库对类型断言的依赖以进行性能优化，从而创建“影子 API”，其中标准类型被隐式地偏爱。虽然类型转换有其用途，但它在标准库中的普遍性表明设计缺陷导致过于复杂的回避方法。这种优化策略无法很好地扩展到第三方类型。

---

## 87. 行动主义、黑客行为或竞选活动：为何在欧洲歌唱大赛中如此容易赢得选票

**原文标题**: Activism, hacking or campaigning: Why it's so easy to win the vote at Eurovision

**原文链接**: [https://english.elpais.com/technology/2025-05-19/activism-hacking-or-campaigning-why-its-so-easy-to-win-the-popular-vote-at-eurovision.html](https://english.elpais.com/technology/2025-05-19/activism-hacking-or-campaigning-why-its-so-easy-to-win-the-popular-vote-at-eurovision.html)

本文探讨了欧洲歌唱大赛电视投票系统的漏洞，强调了该系统如何容易被有组织地动员起来的团体操纵。2025年的比赛中，奥地利歌手JJ获胜，但公众投票引发了质疑，因为以色列歌手Yuval Raphael获得了极高的公众支持，尽管以色列在加沙的行动备受批评。

文章详细描述了欧洲歌唱大赛的投票机制允许每人使用不同的电子邮件地址和银行卡进行多次投票，使其容易受到协同操作的影响。欧洲歌唱大赛网站的截图证实了这一点，截图明确指出每张支付卡只能用于一次交易，鼓励用户使用多张卡再次投票。

专家批评该系统，认为它并非真正的“投票”，因为资格没有明确定义，并且没有阻止重复投票。文章解释说，虽然大多数人根据音乐偏好投票，但专注的团体可以有策略地大规模投票给他们选择的候选人，从而影响结果。

文章还提到了黑客攻击或协调的社交媒体活动的可能性，但未在2025年的比赛中发现任何具体证据。归根结底，欧洲歌唱大赛投票系统的漏洞在于其强调易用性和支付而非安全性和可验证性，这使得相对较小且坚定的团体能够显著影响结果。引用的专家表示，除非电子投票系统完全透明且可审计，否则它们将不会在严肃的选举中获得信任，并且容易被操纵。

---

## 88. 实验至关重要：为什么Nuenki不使用成对评估

**原文标题**: Experimentation Matters: Why Nuenki isn't using pairwise evaluations

**原文链接**: [https://nuenki.app/blog/experimentation_matters_why_we_arent_using_pairwise](https://nuenki.app/blog/experimentation_matters_why_we_arent_using_pairwise)

Nuenki作者详述了由于成本过高，他们放弃了用于其语言翻译质量基准的双向评估系统。最初的系统使用大型语言模型(LLM)为其他LLM的输出评分，但一个新的、利用布拉德利-特里模型的双向评估基准成本过于昂贵，单次实验每个语言就要花费数百甚至数千美元。

尽管作者从科学的角度更倾向于双向比较，但由于无力承担足够的实验，他们开发了一种折衷方案。这个新系统使用六种不同的翻译评估系统来评估来自各种模型的约160个句子的翻译。这些系统判断并对每个翻译进行排名，根据各种因素将其评分从0到100。然后将这些分数组合并进行统计分析，并纳入诸如重复数据合并、随机化和盲法等控制。

这个新系统成本显著降低，在德语的早期测试运行中花费约6美元，同时产生了具有良好p值的结果。该系统与原始系统不同之处在于它依赖于单一指标而不是三个，并且它不是完全盲法的，因为比较模型在评分期间会看到所有翻译。作者邀请读者试用Nuenki，一款语言学习工具。

---

## 89. 间隔重复系统变得更好了

**原文标题**: Spaced repetition systems have gotten better

**原文链接**: [https://domenic.me/fsrs/](https://domenic.me/fsrs/)

本文探讨了间隔重复系统 (SRS) 的进展，特别突出了 Jarrett Ye 开发的 FSRS (自由间隔重复调度器) 算法。SRS 是使用抽认卡和间隔重复来帮助用户记忆信息的软件程序。其核心思想是在“即将忘记之前”复习材料，以最大限度地提高长期记忆效果。

本文将 FSRS 与 SuperMemo-2 等较旧的算法进行了对比，后者使用任意规则安排复习，导致潜在的挫败感和效率低下。另一方面，FSRS 利用机器学习来建模每张卡片的难度、稳定性和可检索性，使其能够根据用户的个人学习模式预测最佳复习间隔。它的目标是在回忆概率降至所需保持率（默认 90%）时安排复习。

FSRS 提供了显著的改进，包括更轻的复习负担、减少错过卡片带来的挫败感（不再重置为第 1 天）以及对知识保持的更大信心。它允许用户调整所需的保持率，以优化工作量与知识的比率，从而有可能以更少的每日复习时间记住更多的卡片。

文章指出，FSRS 已集成到流行的 SRS 软件 Anki 中，但默认情况下未启用。文章还批评了 WaniKani 和 Bunpro 等订阅服务使用的算法，认为它们的效果甚至不如较旧的算法。作者强调了掌握 Anki 并利用 FSRS 进行高效学习和长期知识保持的价值。文章最后列出了一些资源，供有兴趣了解更多关于间隔重复和 FSRS 的人参考。

---

## 90. 关于小行星，雅达利最成功的街机游戏

**原文标题**: About Asteroids, Atari's biggest arcade hit

**原文链接**: [https://www.goto10retro.com/p/about-asteroids-ataris-biggest-arcade](https://www.goto10retro.com/p/about-asteroids-ataris-biggest-arcade)

本文回顾了雅达利最成功的街机游戏《小行星》。作者保罗·勒菲弗尔讨论了这款游戏作为《太空侵略者》续作的构思，并强调了其简单而复杂的游戏玩法。与《太空侵略者》的简单移动不同，《小行星》允许玩家在屏幕上自由移动，向任何方向旋转和射击，同时控制惯性。游戏中还有会分裂成更小、更快碎片的行星，以及在整个屏幕上漫游的 UFO。

本文强调了该游戏对矢量图形的使用，这与当时的栅格图形不同，从而实现了更高的分辨率和独特的发光效果。作者承认自己在街机版的按钮控制方面遇到了困难，但他很喜欢鸡尾酒桌版本，以及后来的带有护盾按钮的《小行星豪华版》。

本文还介绍了雅达利 2600 版本，指出其图形更加块状化，声音也不同，但赞扬了其令人上瘾的游戏玩法。它还提到了雅达利 7800 和 8 位计算机的版本，以及诸如 Atari ST 的 Megaroids 等克隆版本。最后，作者提到了他使用 Xojo 创建的、受《小行星》启发的游戏《太空岩石》，该游戏可在 GitHub 上找到。

---

## 91. 并非因果链，而是互动与适应

**原文标题**: Not causal chains, but interactions and adaptations

**原文链接**: [https://surfingcomplexity.blog/2025/05/19/not-causal-chains-but-interactions-and-adaptations/](https://surfingcomplexity.blog/2025/05/19/not-causal-chains-but-interactions-and-adaptations/)

Lorin Hochstein 批判根本原因分析（RCA）作为事件调查方法，认为它基于对复杂系统故障的错误模型。Hochstein 承认 RCA 的一些有价值的方面，例如识别多个促成因素以及理解工作实际运作方式的重要性，但他认为 RCA 关注线性因果链（根本原因 -> 潜在原因 -> 直接原因 -> 事件）是一种过度简化。

相反，Hochstein 提倡弹性工程（RE）模型。该模型强调系统组件之间的交互是事件的主要驱动因素，将其描述为一个复杂的网络而不是一条链。RE 模型认为，意外的交互，而不是单个组件的故障，导致了事件的发生。它强调，现代软件系统及其复杂的反馈回路本质上是不可预测的。

此外，RE 模型强调复杂系统不断适应潜在的故障，而这种适应性使得它们能够在存在故障的情况下正常运行。RE 方法不是仅仅关注消除根本原因，而是旨在理解和培育系统内部的容错来源和适应能力。这意味着理解系统通常如何补偿故障，以及为什么这些适应在特定事件情况下失败。目标是提高系统适应未来、不可预测的潜在故障组合的能力。文章建议从“寻找故障的根源并消除它们”转变为“寻找容错的来源并发展它们”。

---

## 92. ClawPDF – 开源虚拟/网络PDF打印机，支持OCR和图像

**原文标题**: ClawPDF – Open-Source Virtual/Network PDF Printer with OCR and Image Support

**原文链接**: [https://github.com/clawsoftware/clawPDF](https://github.com/clawsoftware/clawPDF)

ClawPDF 是一款适用于 Windows 的开源虚拟打印机，提供通常在企业级解决方案中才能找到的高级功能。它允许用户创建各种格式的文档，包括 PDF、PDF/A、PDF/X、图像（PNG、JPEG、TIF）、SVG、OCR 和 TXT。它支持元数据管理、高达 256 位 AES 加密密码保护，并包含用于自动化的脚本接口。

一个关键特性是它可以安装在打印服务器上用于网络打印。ClawPDF 兼容主要的 Windows 客户端和服务器操作系统（x86/x64/ARM64）以及多用户环境。

主要功能包括打印到各种格式、100% 有效的 PDF/A 创建、OCR、脚本接口支持（Python、Powershell、VBScript）、共享网络打印、SVG 导出、拖放支持、文件合并、命令行支持、静默打印、自定义纸张尺寸、浅色/深色主题、ARM64 和完整 Unicode 支持、多个配置文件和后处理操作。

该软件易于部署，具有许多设置，并且没有广告软件、间谍软件和恶意软件。它已经在各种 Windows Server 和客户端版本下进行了测试。命令行选项可用于批量打印和配置管理。0.9.3 版本解决了错误修复，包括共享网络打印和 Windows 7 兼容性问题。

ClawPDF 依赖于几个具有各种许可证的开源库，包括 PDFCreator、iText7 和 Ghostscript，确保了广泛的功能。它在 AGPL v3 许可下授权。

---

## 93. 数据库设计原则，或者，真相就在那里

**原文标题**: The principles of database design, or, the Truth is out there

**原文链接**: [https://ebellani.github.io/blog/2025/the-principles-of-database-design-or-the-truth-is-out-there/](https://ebellani.github.io/blog/2025/the-principles-of-database-design-or-the-truth-is-out-there/)

爱德华多·贝拉尼的文章《数据库设计原则，或真相就在那里》主张采用一种正式的、基于原则的数据库设计方法。他认为数据库通过命题来表示现实，而有效的数据库设计对于准确反映业务语义至关重要。他批评了对临时方法的依赖，强调了由于缺乏正规培训而导致的更新异常和数据不一致等潜在问题。

贝拉尼提出了几个设计原则，借鉴了麦戈文和帕斯卡的工作：正交设计原则（POOD）、表征简约原则（PORP）、表达完整性原则（POEC）、完全规范化原则（POFN）、信息原则（TIP）和逻辑独立性原则（PLI）。然后，他介绍了自己提出的原则：本质指称原则（PED），该原则强调使用植根于领域语义的自然键，而不是代理键来标识关系。

作者通过SQL代码片段演示了PED，对比了在公民表中使用代理键与国民身份证作为主键的情况。他认为，使用代理键会将数据库结构与领域的语义意义断开连接。

文章最后强调了良好的数据库设计对于信息系统的技术稳定性和语义清晰度的重要性。他强调，数据库的构建应准确反映真相，需要严谨性和对基本原则的深刻理解。

---

## 94. 解决局部最优问题——N皇后

**原文标题**: Solving the local optima problem – NQueens

**原文链接**: [https://github.com/Dpbm/n-rainhas/blob/main/readme-en.md](https://github.com/Dpbm/n-rainhas/blob/main/readme-en.md)

Dpbm的Github仓库“n-rainhas”解决了经典的N皇后问题，并可能探索或尝试解决在使用启发式算法寻找解决方案时经常遇到的局部最优问题。

N皇后问题涉及将N个国际象棋皇后放置在N×N的棋盘上，使任何两个皇后都不能互相威胁；因此，一个解决方案要求任何两个皇后都不在同一行、同一列或同一对角线上。

N皇后问题中的“局部最优问题”指的是，搜索算法（如爬山算法或模拟退火算法）陷入一种配置，该配置比其直接相邻的配置更好，但不是最佳解决方案（全局最优）。 算法可能无法摆脱这种“局部最优”，因为移动到任何相邻配置都会暂时使情况变得更糟，即使更远的距离可能存在更好的解决方案。

因此，该仓库可能研究旨在逃脱这些局部最优的策略或算法，以便找到N皇后问题的有效解决方案。 这些策略可能包括：

*   **随机重启：** 从不同的随机配置重新开始搜索。
*   **模拟退火：** 允许算法以随时间降低的概率接受一些“更差”的移动。
*   **其他优化技术：** 采用专门的算法来导航复杂的搜索空间。

“Fork 1”和“Star 3”的存在表明，其他用户可能发现该代码或内容有价值或有趣，可能是因为它的实现或用于解决N皇后问题中局部最优问题的特定方法。

---

## 95. 微软的ICC封锁：数字依赖是有代价的

**原文标题**: Microsoft's ICC blockade: digital dependence comes at a cost

**原文链接**: [https://www.techzine.eu/news/privacy-compliance/131536/microsofts-icc-blockade-digital-dependence-comes-at-a-cost/](https://www.techzine.eu/news/privacy-compliance/131536/microsofts-icc-blockade-digital-dependence-comes-at-a-cost/)

本文以近期美国制裁国际刑事法院（ICC）为例，强调在地缘政治紧张局势下，依赖美国IT服务，特别是微软，所存在的风险。由于美国因国际刑事法院调查以色列总理内塔尼亚胡而对其进行制裁，首席检察官卡里姆·汗的微软电子邮件账户被封锁，银行账户被冻结，实际上瘫痪了国际刑事法院的运作。

文章指出，尽管荷兰等欧洲国家政府此前认为微软Azure和365服务的优势超过了主权风险，但国际刑事法院事件表明存在重大漏洞。文章还提出了对美国可能要求访问欧洲数据，以及微软可能被迫遵守美国政策变化，即使这意味着绕过加密或在法庭上败诉的担忧。

作者警告说，非美国政府必须有替代计划，而不能仅仅依赖微软来执行关键职能。文章提出了假设情景，即如果荷兰政府不同意美国政策，美国可能会采取报复行动，阻止公务员的微软相关账户。核心论点强调，国家安全不应依赖于服务水平协议，并强调国际刑事法院目前正在寻找欧洲替代方案，这反映了人们对欧洲数字自主权的广泛担忧。文章最后质疑与微软等老牌企业相比，替代服务的就绪性、安全性和主权。

---

## 96. 红帽与SiFive合作推出RHEL 10的RISC-V开发者预览版

**原文标题**: Red Hat partners with SiFive for a RISC-V developer preview of RHEL 10

**原文链接**: [https://www.redhat.com/en/blog/red-hat-partners-with-sifive-for-risc-v-developer-preview-for-red-hat-enterprise-linux-10](https://www.redhat.com/en/blog/red-hat-partners-with-sifive-for-risc-v-developer-preview-for-red-hat-enterprise-linux-10)

红帽与SiFive合作发布红帽企业Linux (RHEL) 10开发者预览版，该版本将在SiFive HiFive Premier P550平台上运行，这是RISC-V开发的热门选择。下载将于2025年6月1日开始提供。RISC-V是一种开源指令集架构(ISA)，允许任何人构建微处理器，红帽的早期采用标志着他们对开放硬件的承诺以及对开源市场选择的支持。

此次合作旨在使评估RISC-V的客户能够评估其在IT基础设施、工作负载和边缘/嵌入式应用中的适用性。红帽还将发布二进制镜像、其Linux 6.12内核实现的源代码以及其上游贡献，从而刺激基于RISC-V的解决方案的开发。同时还将发布支持RISC-V的CentOS Stream 10版本。

SiFive HiFive Premier P550开发板被认为是运行RISC-V上的RHEL 10开发者预览版的最简单方法。此举符合红帽对开放和透明的企业软件开发的承诺。

---

## 97. Show HN: Goboscript，文本编程语言，编译成Scratch

**原文标题**: Show HN: Goboscript, text-based programming language, compiles to Scratch

**原文链接**: [https://github.com/aspizu/goboscript](https://github.com/aspizu/goboscript)

Goboscript 是一种基于文本的编程语言，可编译为 Scratch 项目。它旨在提供一种比可视化块编辑器更高效、功能更丰富的 Scratch 项目创建方式。用户可以在文本编辑器中编写代码，使用版本控制，重构代码，并轻松共享或重用代码片段。

主要功能包括简洁的语法、与外部工具的集成（用于服装生成等任务）、强大的宏系统、自定义块的局部变量以及优化/问题检测。

Goboscript 基于 Tosh 和 Boiga 等之前的项目构建，并由早期名为 gobomatic 的 Python 实现演变而来。当前的实现是用 Rust 编写的。

该项目是开源的，欢迎贡献。提供了开发说明，包括使用 `cargo run` 和 `tools/run` 脚本来编译、验证、反编译和修补 Scratch 项目。它还包括验证外部 sb3 文件的说明。

Goboscript 在由 FOSS United Foundation 组织的黑客马拉松 FOSS HACK 25 中荣获第一名。

---

## 98. Show HN: Hover Effects TS – 使用 Canvas 实现的 ASCII、乐高和故障悬停效果

**原文标题**: Show HN: Hover Effects TS – ASCII, Lego, and glitch hover effects using canvas

**原文链接**: [https://www.npmjs.com/package/hover-effects-ts](https://www.npmjs.com/package/hover-effects-ts)

Hover Effects TS 是一个 TypeScript 库，为图像提供各种基于 canvas 的高性能悬停效果。它包括 ASCII 艺术、缩放、粒子尘埃、像素化、Minecraft 风格方块和乐高积木等效果。该库可定制，具有交互式控件，允许实时调整每个效果的参数。

可以通过 npm、yarn 或 pnpm 轻松安装。应用效果只需几行代码，支持单个或多个图像以及 CSS 选择器。用户可以导入特定的效果以最大限度地减小捆绑包大小。该库强调性能，建议优化图像大小、仔细调整参数并使用 `destroy()` 进行适当的清理。

文档提供了示例用法指南、初始化最佳实践（首先加载图像、使用 UI 控件值）和调试技巧。每种效果都包含演示、可用控件和参数范围。该库支持现代浏览器，并提供 React 的集成示例。MIT 许可证允许免费使用。最近的版本包括错误修复、性能改进、增强的 TypeScript 支持以及乐高效果等新功能。

---

## 99. 23andMe将基因检测业务出售给DNA药物制造商Regeneron

**原文标题**: 23andMe Sells Gene-Testing Business to DNA Drug Maker Regeneron

**原文链接**: [https://www.bloomberg.com/news/articles/2025-05-19/23andme-sells-gene-testing-business-to-dna-drug-maker-regeneron](https://www.bloomberg.com/news/articles/2025-05-19/23andme-sells-gene-testing-business-to-dna-drug-maker-regeneron)

无法访问文章链接。

---

## 100. Go 密码学安全审计

**原文标题**: Go Cryptography Security Audit

**原文链接**: [https://go.dev/blog/tob-crypto-audit](https://go.dev/blog/tob-crypto-audit)

这篇 Go 博客文章宣布了 Trail of Bits 对 Go 核心密码学软件包进行的独立安全审计结果。该审计涵盖了密钥交换、数字签名、加密、哈希、密钥派生、身份验证和密码学随机数生成器，发现了一项低危漏洞和五项信息性发现。

该低危问题（TOB-GOCL-3）与遗留且不受支持的 Go+BoringCrypto 集成中的内存管理有关，已在 Go 1.25 中修复。信息性发现包括潜在的时序侧信道（TOB-GOCL-1、TOB-GOCL-2、TOB-GOCL-6）、内部 API 中的误用风险（TOB-GOCL-4）以及对不切实际限制的缺失检查（TOB-GOCL-5）。所有信息性发现也已在 Go 1.25 中得到解决。值得注意的是，P-256 ECDSA 中的时序侧信道 TOB-GOCL-2 被分配了 CVE-2025-22866，并影响了 Power ISA 目标。

文章强调了 Go 通过限制复杂性、彻底测试、安全 API 和代码可读性，致力于安全密码学。文章强调了转向使用纯 Go 编写的原生 FIPS 140-3 模式，以取代 Go+BoringCrypto 集成。未来的计划包括实施后量子密码学并引入更易于使用的高级密码学 API。

---

