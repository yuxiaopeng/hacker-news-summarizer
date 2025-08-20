# Hacker News 热门文章摘要 (2025-08-20)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Show HN: 我好奇球形螺旋线，最终做了这个可视化

**原文标题**: Show HN: I was curious about spherical helix, ended up making this visualization

**原文链接**: [https://visualrambling.space/moving-objects-in-3d/](https://visualrambling.space/moving-objects-in-3d/)

此 "Show HN" 帖子展示了一个交互式可视化，并解释了如何在 3D 空间中移动物体，特别是沿着球形螺旋路径移动。作者 Damar 带领读者逐步理解 3D 运动，从基本的 x、y 和 z 坐标等概念开始，以及如何使用数学函数（参数方程）来控制物体随时间变化的位置。

文章从简单的例子开始，演示了如何使用余弦函数在单个轴上创建振荡，然后通过协调 x 和 y 位置与余弦和正弦波来发展成一个 2D 圆。它进一步演变为 2D 螺旋，通过将余弦和正弦函数乘以一个随时间增加的因子，有效地增大圆的半径。

最后，作者介绍了球形螺旋，解释说它需要一个 z 坐标，并使用正弦函数来调节 x 和 y 坐标的增长，从而创建一个环绕球体的螺旋。该可视化允许用户跟随物体的路径。

帖子总结说，通过将 x、y 和 z 坐标定义为时间的函数，可以创建复杂且看似混乱的路径，而这些路径实际上是由精确的数学方程定义的。它链接到维基百科上关于参数方程的文章，以供进一步学习。作者邀请读者在 Twitter 上关注他们，以获取更多类似的文章。

---

## 2. 撞牛

**原文标题**: Crash Cows

**原文链接**: [https://beza1e1.tuxen.de/lore/crash_cows.html](https://beza1e1.tuxen.de/lore/crash_cows.html)

20世纪80年代，在斯维尔德洛夫斯克附近的一个火车站，一套苏联计算机系统在调度火车车厢时，总是会在夜间发生不明原因的崩溃。程序员谢尔盖调查了这个问题。他发现崩溃与从乌克兰北部和俄罗斯西部运往当地屠宰场的活牛有关。

进一步调查显示，这些牛受到切尔诺贝利灾难的严重辐射污染。受污染的车厢靠近计算机导致机器内存中出现随机位翻转，从而导致系统故障。苏联政府计划将这些受污染的肉与其他地区未受污染的肉混合，以稀释辐射水平。

谢尔盖对此感到震惊，意识到事态严重，立即申请移民。随着辐射水平随时间自然下降，计算机崩溃最终停止。

---

## 3. Gemma 3 270M 的纯 PyTorch 本地调试重制版

**原文标题**: Gemma 3 270M re-implemented in pure PyTorch for local tinkering

**原文链接**: [https://github.com/rasbt/LLMs-from-scratch/tree/main/ch05/12_gemma3](https://github.com/rasbt/LLMs-from-scratch/tree/main/ch05/12_gemma3)

rasbt 的 GitHub 仓库 "LLMs-from-scratch" 专注于用纯 PyTorch 重新实现强大的语言模型 Gemma 3 270M。其主要意义在于，这种重新实现允许在本地进行实验和调整最先进的语言模型，而无需复杂的框架或云资源。

该项目为理解大型语言模型的内部运作提供了宝贵的教育资源。通过提供一个干净的、基于 PyTorch 的实现，它简化了通常与 LLM 相关的复杂性，使研究人员、学生和爱好者更容易：

*   **理解架构：** 探索 Gemma 3 270M 模型的特定组件和配置。
*   **实验性修改：** 调整和修改模型的架构、训练程序或推理方法。
*   **学习 PyTorch：** 通过使用实际的 LLM 示例获得 PyTorch 的实践经验。
*   **本地运行：** 在个人硬件上执行模型，避免对昂贵的云基础设施的需求。

该仓库已引起广泛关注，大量的 Fork (9.3k) 和 Star (66.2k) 表明了社区对易于访问和具有教育意义的资源，以便从头开始理解和使用大型语言模型的兴趣。

---

## 4. OPA维护者和Styra雇员被苹果公司聘用

**原文标题**: OPA maintainers and Styra employees hired by Apple

**原文链接**: [https://blog.openpolicyagent.org/note-from-teemu-tim-and-torin-to-the-open-policy-agent-community-2dbbfe494371](https://blog.openpolicyagent.org/note-from-teemu-tim-and-torin-to-the-open-policy-agent-community-2dbbfe494371)

以下是Open Policy Agent (OPA) 博客文章的摘要：

这篇文章是Open Policy Agent (OPA) 项目的主要贡献者和维护者 Teemu Mäki-Hokkonen, Tim Hinrichs 和 Torin Sandall 写给OPA社区的消息。他们宣布将离开他们共同创立并大力支持OPA开发的Styra公司，加入苹果公司。

该公告的主要目的是让OPA社区放心，这一变化不会对该项目产生负面影响。他们强调了他们对OPA及其开源性质的持续承诺。他们表示，他们将继续参与OPA的开发和社区互动，尽管是以苹果公司的新身份。

他们强调Styra仍然致力于OPA，并且该公司对该项目的持续投资将确保其持续增长和成功。他们承认Styra对OPA的重大贡献，并对现有Styra团队继续推动该项目前进的能力表示信心。

简而言之，该公告是关于OPA的关键人物加入苹果公司，同时强调OPA项目的持续健康和稳定，这要归功于他们自己和Styra的持续承诺。他们向社区保证OPA仍然是首要任务。

---

## 5. 更贴近底层：放弃Playwright，选择CDP

**原文标题**: Closer to the Metal: Leaving Playwright for CDP

**原文链接**: [https://browser-use.com/posts/playwright-to-cdp](https://browser-use.com/posts/playwright-to-cdp)

在2025年8月20日的这篇博文中，Nick Sweeting讨论了放弃Playwright进行AI浏览器自动化，转而直接采用Chrome DevTools协议（CDP）的决定。文章认为，虽然Playwright和类似的库对于简化QA和自动化脚本很有用，但它们可能会掩盖关于浏览器行为的重要细节，而这对于AI浏览器代理来说是一个关键问题。

作者解释说，使用原始CDP可以提高元素提取和屏幕截图的速度，以及提供新的异步反应能力和跨域iframe支持。Playwright的架构通过Node.js服务器引入了第二个网络跃点，增加了延迟。

文章随后简要介绍了浏览器自动化的历史，从PhantomJS到Puppeteer、Playwright和Selenium等现代工具。它详细介绍了Playwright的工作原理，强调了其客户端-服务器模型以及潜在的缺点，例如浏览器、Node.js中继和Python客户端之间的状态不一致。文章还提到了Playwright的特定“尖锐问题”，例如在全页屏幕截图期间崩溃以及处理警报、文件上传和崩溃选项卡的困难。

最后，文章深入探讨了使用CDP切换后实施的变更的案例研究，包括开发用于Python类型绑定的`cdp-use`库以及由`bubus`驱动的新事件驱动架构，以监视CDP事件。这种事件驱动的架构使代理能够对自发事件（如下载或崩溃）做出反应，而无需在整个代码中分散重试逻辑。文章还介绍了用于DOM节点的“超级选择器”的创建，以正确处理跨目标和框架的元素。

---

## 6. Pytype 更新

**原文标题**: An Update on Pytype

**原文链接**: [https://github.com/google/pytype](https://github.com/google/pytype)

谷歌开发的Python类型检查器Pytype将在Python 3.12之后停止支持。Pytype最初于2012年创建，旨在为谷歌的Python开发者提供编译时检查，但由于字节码固有的不稳定性，其基于字节码的设计已被证明难以维护和适应新的类型特性和PEP。

谷歌将不再继续开发Pytype，而是将重点转移到探索新的类型方法和框架，以更好地满足其Python用户群的需求。该公告强调了当前Python类型生态系统的稳健性，建议用户研究诸如mypy、pyright等替代解决方案。

该团队对所有贡献者表示感谢，特别是Rebecca Chen、Martin DeMello、Teddy Sudol和Matthias Kramm对Pytype所做的工作。Rebecca Chen因其参与类型委员会，为Python类型系统做出的重大贡献而受到特别表彰。虽然Pytype的开发即将结束，但谷歌仍然致力于Python类型领域。

---

## 7. 14.ai (YC W24) 正在旧金山招聘工程师（技术支持/效果），打造 AI 原生的 Zendesk。

**原文标题**: 14.ai (YC W24) is hiring eng (TS/Effect) in SF to build the AI-native Zendesk

**原文链接**: [https://14.ai/careers](https://14.ai/careers)

14.ai (YC W24) 正在招聘创始工程师，地点位于旧金山。他们正在构建一个 AI 原生的 Zendesk。他们是一支小型的、以客户为中心的团队，重视安全性、可靠性、性能和实用主义。他们的客户范围从初创公司到企业。他们获得了 Y Combinator、SV Angel、basecase 以及 Vercel、Slack、Dropbox、Replit 和 Algolia 等公司创始人的支持。

创始工程师将直接与客户互动，并参与整个技术栈的工作，包括 TypeScript、Postgres、Vite、Next.js 和 Effect。工作涉及并发系统、模块化服务基础设施、代理编排、文本处理、RAG、数据库优化、LLM 工程、遥测和 CI/CD 等领域。

要求包括扎实的 Web 技术经验，尤其是 JavaScript/TypeScript，以及将代码发布到生产环境的经验。对从头开始构建产品充满热情，并渴望加入创始团队至关重要。该职位位于旧金山，或需要搬迁。具备将 LLM 部署到生产环境的经验以及之前创立公司或构建高影响力项目的经验者优先考虑。

---

## 8. OCaml 代码编辑改进：重构引擎基础

**原文标题**: Improvements to OCaml code editing: the basics of a refactor engine

**原文链接**: [https://tarides.com/blog/2025-08-20-internship-report-refactoring-tools-coming-to-merlin/](https://tarides.com/blog/2025-08-20-internship-report-refactoring-tools-coming-to-merlin/)

本文总结了一个实习项目，该项目专注于通过重构工具，特别是Merlin编辑器中的重构工具，来改进OCaml代码编辑。核心贡献是实现了“表达式提取到顶层”的重构命令。该命令允许开发者选择代码中的一个表达式，并自动将其移动到作用域顶层新生成的`let`绑定中。

本文通过示例演示了该命令的功能，包括提取常量、表达式（通过使用thunk来处理潜在的副作用）以及依赖于变量的表达式。在后一种情况下，该工具智能地识别自由变量，并创建一个以这些变量为参数的函数。文章还展示了一个真实场景，涉及提取标记漂亮打印逻辑。

本文解释了如何通过语言服务器协议 (LSP) 将该命令集成到编辑器中，既使用了代码操作（更简单、更通用），也使用了自定义请求（用于自定义名称输入等功能）。下一步是在Merlin中创建一个重构工具箱库，用于构建更多的重构操作。文章还提到了与实现相关的几个拉取请求。最后，文章感谢了贡献者，并推广了Tarides的开源工作和商业机会。

---

## 9. Show HN: Luminal – 开源的、基于搜索的 GPU 编译器

**原文标题**: Show HN: Luminal – Open-source, search-based GPU compiler

**原文链接**: [https://github.com/luminal-ai/luminal](https://github.com/luminal-ai/luminal)

Luminal：一个基于搜索的 Rust 开源 GPU 编译器和深度学习库，旨在实现高性能和简洁性。它的核心围绕 12 个原始操作构建，编译成复杂的 GPU 内核以提高速度。它使用基于搜索的编译来发现优化，包括像 Flash Attention 这样的技术，并且是自动化的。 这种方法使其保持小巧，并有可能胜过具有手写内核的较大框架。

Luminal 强调提前编译，类似于 XLA 和 tinygrad，其中整个神经网络表示为一个静态计算图。这使得编译器能够获得全局知识，从而促进积极的内核融合、特定于形状的内核，以及通过编译器处理设备/数据类型。

目前，Luminal 支持 Mac 和 Nvidia GPU 的 Metal 和 CUDA，支持全精度和半精度。提供基于图的自动微分的完整训练支持。示例包括 Llama 3、Phi 3、Whisper 和 Yolo v8 的实现。

该项目正在过渡到“2.0”，这将引入大规模内核搜索，从而简化编译器堆栈。路线图包括扩展搜索空间、提高 CUDA 与 Metal 的对等性、添加 Blackwell 内在函数、构建 ROCm 后端、与其他库进行基准测试，以及实现分布式数据/流水线/张量并行性。目标是在 LLM 推理和训练方面超越 PyTorch 2.0 的性能。Luminal 在 Apache 2.0 或 MIT 许可下获得许可。

---

## 10. 潮汐波Web：Rails和Phoenix的浏览器内编码助手

**原文标题**: Tidewave Web: in-browser coding agent for Rails and Phoenix

**原文链接**: [https://tidewave.ai/blog/tidewave-web-phoenix-rails](https://tidewave.ai/blog/tidewave-web-phoenix-rails)

Tidewave Web是一款全新的浏览器内编码助手，旨在简化Rails和Phoenix应用程序的Web开发。与传统的编码助手不同，Tidewave直接在开发者的环境中运行，通过理解UI状态、框架和代码来提供共享上下文。这消除了与其他AI工具之间反复的沟通和翻译。

主要功能包括：直接访问UI状态并映射到代码；与Rails/Phoenix深度集成，允许代码执行、数据库查询和日志监控；通过点击界面进行协作式浏览器测试；以及通过添加软件包并连接GitHub Copilot或Anthropic帐户轻松集成。

Tidewave的核心优势在于它能够在开发者、AI助手和Web应用程序之间创建共享上下文。这使得助手能够处理繁琐的任务，例如生成CSV导出功能，方法是自动查询数据库、访问模型并在浏览器中进行测试。

Tidewave Web以Rails和Phoenix软件包的形式提供，需要Copilot订阅或Anthropic API密钥。提供免费试用版，付费订阅可解锁无限消息。初始版本侧重于Web应用程序集成，React支持以及Django、Flask和Next.js等其他框架也已列入路线图。

Tidewave的创建者Dashbit设想未来AI开发者工具将针对特定领域进行定制，了解其独特的运行时和工作流程。Tidewave Web是朝着这个方向迈出的第一步。

---

## 11. AGENTS.md – 指导代码代理的开放格式

**原文标题**: AGENTS.md – Open format for guiding coding agents

**原文链接**: [https://agents.md/](https://agents.md/)

AGENTS.md 是一种新的开放格式，旨在为编码代理提供详细的指令，使其能够有效地处理项目，补充 README.md 中以人为本的信息。它旨在为构建步骤、测试程序、代码约定和其他代理特定的指南提供清晰、可预测的位置，这些指南可能对于典型的 README 来说过于详细或无关紧要。

AGENTS.md 的核心优势在于为 AI 编码代理提供精确的指令，保持 README 文件的简洁，并确保与不断增长的 AI 工具生态系统（如 Codex、AmpJules、Cursor 和 Factory）的兼容性。它旨在跨多个代理工作，确保单个定义可以被各种工具使用。

AGENTS.md 文件是简单的 Markdown，允许灵活的结构化。最佳实践包括添加项目概述、构建和测试命令、代码风格、测试和安全考虑等部分。对于大型单体仓库，支持子项目中嵌套的 AGENTS.md 文件，以最接近的文件为优先。

AGENTS.md 项目源于 OpenAI、Google、Cursor 和 Factory 之间的合作，并致力于将其维护和发展成为整个开发者社区的开放格式。如果 AGENTS.md 文件中列出了测试命令，代理将在完成任务之前尝试自动执行相关的程序检查并修复故障。

---

## 12. 如何思考GPU

**原文标题**: How to Think About GPUs

**原文链接**: [https://jax-ml.github.io/scaling-book/gpus/](https://jax-ml.github.io/scaling-book/gpus/)

本文深入探讨了英伟达GPU的架构和功能，特别关注其在机器学习中的应用。它将H100和B200等GPU与谷歌的TPU进行了比较，突出了它们的异同。

GPU由流式多处理器（SM）组成，每个SM包含一个张量核心（用于矩阵乘法）、一个 Warp 调度器（矢量算术单元）和快速片上缓存（SMEM）。与TPU不同，GPU具有许多（超过100个）相对独立的SM，从而可以并行执行任务。每个SM进一步划分为子分区，包括用于矢量运算的CUDA核心（ALU）和用于提供主要FLOPs性能的张量核心。

本文详细介绍了内存层次结构，从每个子分区中的寄存器、SMEM、所有SM共享的L2缓存，到最终的HBM（主GPU内存）。它解释了CUDA核心如何以SIMT模型运行，这种模型提供了灵活性，但如果warps发散，可能会导致性能下降。

文章包含一个表格，总结了各种GPU世代（V100、A100、H100、H200、B200）的规格，涵盖了SM数量、内存容量以及FLOPs/带宽数字。它还提供了GPU和TPU组件的比较概述，强调了GPU的模块化与TPU的集成设计。最后，它指出GPU提供通用性，而TPU提供性能。文章最后附有测验。

---

## 13. Digg.com回归

**原文标题**: Digg.com Is Back

**原文链接**: [https://www.digg.com/](https://www.digg.com/)

Digg.com重启为社区平台，聚焦人际连接。该平台旨在优先考虑真实的社区体验和真诚的互动，将“人性置于核心”，并利用技术来增强这些连接。与之前的版本不同，Digg现在对其设计和功能采用以人为本的方法。目前，访问该平台仅限邀请，鼓励潜在用户加入等候名单。重点是从头开始构建社区，并高度重视培养其成员之间的真实关系和有意义的互动。

---

## 14. Show HN: 如果你朝你指的方向一直走，你会到达哪个国家？

**原文标题**: Show HN: What country you would hit if you went straight where you're pointing

**原文链接**: [https://apps.apple.com/us/app/leascope/id6608979884](https://apps.apple.com/us/app/leascope/id6608979884)

这款“Show HN”帖子推广一款名为“笔直走会撞到哪个国家？”的免费教育应用。该应用由Ben Gross开发，利用André Ourednik的Historical Basemaps项目中的历史地图数据，确定你从当前位置直线行走会到达的国家。

该应用适用于iPhone、iPad、Mac（配备Apple M1芯片或更高版本）和Apple Vision，需要iOS 17.5、iPadOS 17.5、macOS 14.5或visionOS 1.2或更高版本。它下载量很小（14.7 MB），年龄适宜性评级为4+。

一个关键的卖点是开发者Ben Gross明确声明该应用不收集任何用户数据，解决了隐私问题。应用描述强调了最新版本（2.5）中的“通用改进”。该帖子还包含应用支持和隐私政策的链接。最后，它还推荐了用户可能感兴趣的其他类似应用。

---

## 15. MapLibre瓦片：一种为渲染优化的下一代地理空间格式

**原文标题**: MapLibre Tile: A next generation geospatial format optimized for rendering

**原文链接**: [https://arxiv.org/abs/2508.10791](https://arxiv.org/abs/2508.10791)

本文介绍了一种新的矢量瓦片格式 MapLibre Tile (MLT)，旨在改进现有的 Mapbox Vector Tile (MVT) 格式。作者 Markus Tremmel 和 Roland Zink 认为，MVT 虽然已被广泛采用，但已过时，未能充分利用地理空间数据获取和处理方面的进步。

MLT 被认为是针对 MVT 局限性的彻底重新设计。该论文重点介绍了通过模拟用户在底图数据集上的会话实验所展示的关键优势。这些优势包括显著提高的压缩率（编码瓦片集上高达三倍，大型瓦片上超过六倍）和更快的解码速度（高达三倍），与 MVT 相比。该格式还增强了处理性能。

除了性能改进之外，MLT 还引入了新功能，并旨在支持下一代地图渲染器，旨在将处理任务转移到 GPU。这种转变旨在克服摩尔定律放缓带来的限制。

本文归类于信息论 (cs.IT)，并提供 PDF 和 HTML 格式的论文下载链接以及 BibTeX 引用。它还包括各种外部工具的链接，用于探索相关研究、代码存储库和交互式演示。

---

## 16. Show HN: Strudel Flow，一个用 Strudel 和 React Flow 构建的模式音序器

**原文标题**: Show HN: Strudel Flow, a pattern sequencer built with Strudel and React Flow

**原文链接**: [https://github.com/xyflow/strudel-flow](https://github.com/xyflow/strudel-flow)

Strudel Flow 是一个可视化鼓机和音序器，它使用 Strudel.cc、React Flow、Tailwind CSS 和 shadcn/ui 构建。它允许用户通过拖放界面连接乐器节点和效果节点来创建复杂的音乐模式。

主要功能包括各种节点类型：乐器（Pad 节点、节拍机、琶音器、和弦节点、复节奏、自定义节点）、合成器（鼓声、采样选择）和音频效果（增益、后增益、失真、低通滤波器、声像、相位器、压缩、Jux、FM、房间）以及时间效果（快、慢、延迟、启动、释放、延音、反向、回文、遮罩、层叠）。

用户可以通过激活节点内的步进、调整速度、应用行修饰符来实现步进特定的效果以及将节点链接在一起来创建模式。步进修饰符包括速度控制选项（快、慢）、重复（复制）和持续时间扩展（延长）。

该应用程序提供诸如全局播放/暂停（空格键）、独立组控制、实时模式编辑（实时更新）和显示生成的 Strudel 代码的模式预览等性能控制。键盘快捷键简化了工作流程。

该项目被组织成 `components`、`nodes`（包括 `instruments`、`effects` 和 `synths`）、`ui`、`workflow`、`edges`、`data`、`hooks`、`lib`、`store` 和 `types` 目录。它利用 Strudel.cc 作为其音频引擎，React Flow 用于可视化基于节点的界面，shadcn CLI 用于 UI 组件，Zustand 用于状态管理。

---

## 17. Show HN: Anchor Relay – 更快更便捷地获取 Let's Encrypt 证书

**原文标题**: Show HN: Anchor Relay – A faster, easier way to get Let's Encrypt certificates

**原文链接**: [https://anchor.dev/relay](https://anchor.dev/relay)

Anchor Relay旨在简化并安全化获取Let's Encrypt证书的流程，尤其适用于家庭实验室、自托管环境、不可信网络（如物联网）和内部网络。它为浏览器信任的HTTPS证书提供了一种更快更简便的方法。

其主要功能包括作为Let's Encrypt的ACME API前端、处理挑战记录的DNS委派以及提供细粒度的访问控制。一个主要优点是无需暴露端口80或转发HTTP流量进行证书验证，而是依赖于仅出站连接。这增强了安全性并降低了复杂性。

Anchor Relay专为希望在不将基础设施直接暴露于互联网或跨多个工具管理API凭证的情况下保护其服务的开发者和用户而设计。它与Certbot和Caddy等常用工具无缝集成，使过渡和使用变得轻松。通过仅需要一次性的DNS配置，Anchor Relay简化了证书管理并增强了安全性。

---

## 18. OrioleDB中有序插入优化

**原文标题**: Ordered Insertion Optimization in OrioleDB

**原文链接**: [https://www.orioledb.com/blog/batch-inserts](https://www.orioledb.com/blog/batch-inserts)

OrioleDB 新批处理页面插入优化解决了多个会话尝试将数据插入到同一 B 树叶子页面时导致的性能瓶颈，从而减少了锁竞争和低效的睡眠/唤醒循环。 其核心思想是允许持有页面锁的会话为自身和等待中的相邻会话插入数据，从而有效地为页面插入创建“组提交”。

等待进程现在不再排队等待锁，而是将其预期元组（键、有效负载、元信息）发布到共享内存并将其链接到页面的“等待列表”。 然后，锁持有者扫描此列表，收集属于该页面的元组，并将其与自己的元组一起插入，然后再释放锁。 这减少了锁的切换，因为一个进程执行多个插入。 等待进程醒来时，通常会发现其元组已被插入。

模拟物联网工作负载（按时间排序的数据）的基准测试表明性能得到了显著提升。 虽然 OrioleDB beta12 在连接数较少时比 PostgreSQL 慢，但从 64 个并发连接开始，批处理页面插入优化将性能提高了近 2 倍，从而显著减少了锁等待时间。 该优化对于具有倾斜键、基于时间的排序或追加繁重的 OLTP 场景的工作负载最为有效。 该优化将包含在 OrioleDB beta13 版本中。

---

## 19. 堆积木问题

**原文标题**: The Block Stacking Problem

**原文链接**: [https://sites.pitt.edu/~jdnorton/Goodies/block_stacking/block_stacking.html](https://sites.pitt.edu/~jdnorton/Goodies/block_stacking/block_stacking.html)

本文《积木堆叠问题》探讨了在桌边堆叠积木以最大化水平延伸的反直觉物理现象。作者约翰·D·诺顿提出了与此问题相关的三个谜题：在最后一个积木不受支撑的情况下，堆叠体如何延伸到桌子之外；如果有足够的积木，这种延伸为什么没有限制；以及无限堆叠体的悖论行为。

文章解释了平衡原理，包括力矩和质心，这对于理解这些堆叠体的稳定性至关重要。文章表明，只要堆叠体的质心由下面的积木或桌子支撑，该堆叠体就是稳定的。文章逐步分析了四块积木堆叠体的稳定性，展示了每个子堆叠体的质心是如何定位以获得支撑的。

文章还讨论了n块积木堆叠体中位移的一般公式，证实了最顶层积木的位移可以是无界的。对数近似提供了一个简单的公式，并揭示了积木超出桌子边缘的比例以及质量分布。

最后，文章探讨了“无限堆叠体”的谜题。虽然有限的堆叠体可以任意延伸，但将极限推到无穷大会导致令人惊讶的结果。根据接近极限的方式，无限堆叠体要么完全消失，要么坍塌成一个不延伸到桌子边缘的堆叠体，这与基于有限堆叠体的预期形成对比。作者旨在提供对堆叠体行为以及处理无穷大时特性的直观理解。

---

## 20. 2025年的AWS：你以为你知道，但现在错了的东西

**原文标题**: AWS in 2025: The Stuff You Think You Know That's Now Wrong

**原文链接**: [https://www.lastweekinaws.com/blog/aws-in-2025-the-stuff-you-think-you-know-thats-now-wrong/](https://www.lastweekinaws.com/blog/aws-in-2025-the-stuff-you-think-you-know-thats-now-wrong/)

Corey Quinn：《2025年的AWS：你以为你知道但现在已经错了的事情》强调了云专业人士可能仍在使用的关于AWS的过时信息。他强调AWS已经发生了重大演变，许多长期存在的假设不再准确。

文章详细介绍了几个关键AWS服务的变化：

*   **EC2：** 安全组和IAM角色可以在不关闭实例的情况下更改。实时迁移很常见。实例可靠性得到提高。Spot实例定价更加稳定。专用实例很少需要。公开AMI阻止访问现在是默认设置。
*   **S3：** 读取后写入一致性是标准配置。对象键随机化是不必要的。ACL已被弃用。公开访问阻止和透明加密是新存储桶的默认设置。Glacier已集成到S3存储类中，恢复费用/速度得到提高。
*   **网络：** 公共IPv4地址现在需要付费。存在VPC对等连接的更好替代方案（Transit Gateway、VPC共享等）。VPC Lattice和Tailscale简化了网络。CloudFront更新速度更快。跨可用区数据传输费用因负载均衡器类型而异。网络负载均衡器现在支持安全组。区域ID可以与资源访问管理器对齐。
*   **Lambda：** 超时、容器镜像支持、RAM限制、共享存储和`/tmp`存储已增加。在VPC中调用Lambda的速度更快，冷启动的问题也更少。
*   **EFS：** IO性能可以独立于容量进行调整。
*   **EBS：** 新卷具有完整性能。快照恢复在首次读取时可能很慢。卷可以并发连接到多个EC2实例（io1）。
*   **DynamoDB：** 现在支持空字段。性能更加可靠。按需定价通常更可取。
*   **成本节约：** 预留实例正逐步淘汰，取而代之的是Savings Plans。EC2按秒收费。成本异常检测器有效且免费。Compute Optimizer值得信赖。Trusted Advisor仍然存在疑问。
*   **身份验证：** IAM角色优先于IAM用户。IAM Identity Center取代了AWS SSO。
*   **杂项：** us-east-1更加稳定。弃用正在增加。CloudWatch数据一致性得到提高。AWS账户可以从根组织账户关闭。

文章鼓励读者更新他们的AWS知识，避免依赖过时的实践。

---

## 21. Show HN: Typed-arrow – Rust 的编译时 Arrow schema

**原文标题**: Show HN: Typed-arrow – compile‑time Arrow schemas for Rust

**原文链接**: [https://github.com/tonbo-io/typed-arrow](https://github.com/tonbo-io/typed-arrow)

`typed-arrow` 是一个 Rust 库，它提供编译时 Arrow schema 定义，从而提供了一种强类型且高效的方式来处理 Arrow 数据结构。 它利用 Rust 的类型系统将 Rust 类型直接映射到 arrow-rs builders 和 arrays，避免了运行时 DataType 切换，并实现了单态化列构造，从而提高了性能。

主要特性和优点包括：

*   **编译时安全：** 类型不匹配在编译期间被捕获，确保数据完整性。
*   **性能：** 由于单态化，零运行时动态分发。
*   **互操作性：** 直接使用 `arrow-array` 和 `arrow-schema` 类型。
*   **ORM 类似 API：** 提供符合人体工程学的方式来构建和操作 Arrow 数据。
*   **Record derive 宏：** 简化了具有命名字段的结构体的 schema 创建。
*   **支持嵌套类型：** 处理列表、结构体、映射和联合体。
*   **字典编码：** 提供具有各种键和值类型的字典列。
*   **时间戳处理：** 支持带和不带时区的时间戳。
*   **元数据支持：** 允许添加 schema 级别和字段级别的元数据。
*   **全面的数据类型覆盖：** 支持广泛的 Arrow 数据类型，包括原始类型、字符串/二进制类型、时间类型、十进制类型和嵌套结构。

该库提供了几个示例，演示了它的用法，涵盖了各种数据类型和场景。 它使用诸如 `Record`、`ColAt`、`ArrowBinding`、`BuildRows` 和 `SchemaMeta` 等 trait 来进行 schema 定义和数据操作。

---

## 22. 芯片设计中人工智能的最佳选择

**原文标题**: Best Options for Using AI in Chip Design

**原文链接**: [https://semiengineering.com/best-options-for-using-ai-in-chip-design/](https://semiengineering.com/best-options-for-using-ai-in-chip-design/)

这篇《半导体工程》文章“在芯片设计中使用人工智能的最佳方案”探讨了人工智能在芯片设计中的应用，并收录了Cadence、Siemens EDA、Synopsys、Baya Systems、ChipAgents和Keysight等公司专家的见解。

讨论强调，像汽车和高性能计算等定义明确的垂直领域，由于其特定的需求，为人工智能在芯片设计中提供了最佳机会。人工智能的角色正在演变，既有潜力通过调试分析获得短期生产力提升，也有可能带来像自主工作流程这样的长期颠覆性变革。专家们设想，从目前的L1辅助发展到完全自主的L5工作流程，引发了人们对初级工程师未来角色的疑问。

一个关键点是“面向代理的EDA工具”的概念，这些工具通过自然语言进行训练，可以比人类更有效地利用并行性和速度。对话深入探讨了如何使人工智能驱动的工具对工程师来说更“易读”，从而可以高效地审查和理解人工智能生成的解决方案。这包括在设计过程中向工程师提供更多信息和反馈，无论经验水平如何。

专家们还探讨了对缺乏经验的工程师过度依赖人工智能的担忧。共识是，人工智能应该辅助，而不是取代人类的专业知识，并且提供知识助手和清晰的解释可以加速初级工程师的学习。人工智能在设计中创建更高层次抽象以及促进更好知识共享的潜力也得到了强调。

---

## 23. 红杉资本支持Zed的协作编码愿景

**原文标题**: Sequoia Backs Zed's Vision for Collaborative Coding

**原文链接**: [https://zed.dev/blog/sequoia-backs-zed](https://zed.dev/blog/sequoia-backs-zed)

世界最快IDE的开发者Zed获红杉资本领投的3200万美元B轮融资，融资总额超过4200万美元。这笔资金将用于开发DeltaDB，一种新型的、基于操作的版本控制系统，旨在革新人类和AI智能体之间的协同编码。

Zed旨在解决的核心问题是当前基于快照的版本控制系统（如Git）的局限性，这些局限性通过将代码对话与代码本身分离，并使其难以保持最新状态，从而限制了代码对话。DeltaDB将跟踪每一次操作，而不仅仅是提交，并使用CRDT实时同步更改。这种细粒度的更改跟踪将允许字符级别的永久链接，从而在代码库中直接实现持久的、情境化的讨论，即使跨越代码转换也是如此。

Zed设想了一种IDE，人类和AI智能体可以在其中无缝协作，所有编辑、讨论和见解都与不断演进的代码相关联，从而创建软件开发的鲜活历史。该系统将为AI智能体提供做出更明智编辑所需的上下文。

DeltaDB将与Git互操作，并且像Zed一样，将采用开源模式，并提供可选的付费服务。Zed正在积极招聘工程和产品设计方面的人才，以实现这个协作的未来。

---

## 24. 美国边境手机搜查数量创历史新高

**原文标题**: Phone Searches at the US Border Hit a Record High

**原文链接**: [https://www.wired.com/story/phone-searches-at-the-us-border-hit-a-record-high/](https://www.wired.com/story/phone-searches-at-the-us-border-hit-a-record-high/)

美国海关与边境保护局（CBP）官员正在边境以前所未有的程度搜查手机和电子设备。2025年4月至6月，CBP搜查了14899台设备，比2022年1月至3月的前一个高峰期增长了16.7%。此次增长与特朗普第二任政府下加强边境安全措施同时发生，包括国土安全部以及移民和海关执法局获得了更大的预算。

包括美国公民自由联盟（ACLU）在内的批评人士表示担忧，这些未经搜查令进行的搜查对旅行者产生了寒蝉效应，可能会影响到那些对政府持批评态度的人士或拥有敏感数据的专业人士。虽然CBP辩称设备搜查仅影响到极小比例的旅行者（不到0.01%），但担忧依然存在。

文章区分了“基本”搜查（涉及手动检查设备）和“高级”搜查（利用取证工具提取大量数据）。虽然高级搜查相对稳定，但CBP正在寻求获得更先进的取证工具，这预示着可能会转向更具侵入性的搜查。

无论公民身份如何，旅行者的设备都可能在边境被搜查，因为第四修正案的保护在那里受到限制。拒绝解锁设备可能导致设备被没收，或者对于外国访客，可能导致拘留或驱逐出境。

---

## 25. 如何画太空侵略者

**原文标题**: How to Draw a Space Invader

**原文链接**: [https://muffinman.io/blog/invaders/](https://muffinman.io/blog/invaders/)

本文详细介绍了如何创建“太空侵略者生成器”的过程，从最初设想的利用 3D 向量渲染器的副项目到最终发布为代码挑战。作者强调先解决问题再编写代码，详细介绍了他们的初步研究和手绘像素艺术设计。 然后，他们解释了生成器背后的算法，该算法利用向量图形和几何原理来创建独特的侵略者。

生成过程包括：通过随机选择顶部和底部点并镜像生成的顶点来创建身体多边形；使用“粗线”算法添加触手和角；然后通过检查像素中心是否落在形状内，将矢量形状转换为像素化形式。眼睛从预定义的集合中添加，颜色使用 OKLCH 色彩空间生成，以保持一致的亮度。

文章进一步解释了如何通过稍微改变触手和角的中线以及移动眼睛位置来使侵略者动画化。 还讨论了网格大小对入侵者外观的影响。 最后，作者提到了创建交互式博客文章的技术方面，包括使用 Anime.js 进行动画处理以及 JavaScript 代码的构建过程。 他们最后鼓励读者尝试生成器，并查看他们之前关于绘制 SVG 绳索的互动帖子。

---

## 26. 镜面阴影：赛博朋克选集 (1986)

**原文标题**: Mirrorshades: The Cyberpunk Anthology (1986)

**原文链接**: [https://www.rudyrucker.com/mirrorshades/HTML/](https://www.rudyrucker.com/mirrorshades/HTML/)

《镜面阴影：赛博朋克选集》是一部收录了代表 20 世纪 80 年代兴起的新科幻运动——赛博朋克作品的故事集。该选集由布鲁斯·斯特林编辑，展示了那些拥抱并将高科技与现代流行地下文化相结合的作家。

斯特林认为，尽管作家们对这个标签有所保留，但赛博朋克是八十年代的明确产物，它深深扎根于科幻传统，同时又对它做出反应。赛博朋克承认新浪潮和更硬科幻传统的先驱，强调文学技巧和创新思想。

“镜面阴影”这个标题指的是一种运动标志，反映了叛逆和技术的主题。赛博朋克中反复出现的主题包括通过先进技术对身体和思想的入侵，以及技术融入日常生活。赛博朋克融合了反主流文化、技术进步和街头无政府状态。

斯特林认为，赛博朋克是一种流行现象，反映了黑客和摇滚乐手重叠的世界，并将技术和反主流文化融合在一起，标志着它与早期科幻小说中常常对技术保持距离的观点有所不同。赛博朋克的关键特征是对技术的发自内心的处理方式、对个人技术的关注以及对街头文化为自身目的而改造技术的过渡地带的迷恋。

---

## 27. Databricks正以超1000亿美元估值进行K轮融资。

**原文标题**: Databricks is raising a Series K Investment at >$100B valuation

**原文链接**: [https://www.databricks.com/company/newsroom/press-releases/databricks-raising-series-k-investment-100-billion-valuation](https://www.databricks.com/company/newsroom/press-releases/databricks-raising-series-k-investment-100-billion-valuation)

Databricks宣布以超过1000亿美元的估值进行K轮融资。现有投资者预计将支持本轮融资。该公司计划利用这笔资金加速其人工智能战略，特别是扩展Agent Bricks，投资Lakebase（其新的数据库产品），并推动全球增长。

首席执行官Ali Ghodsi强调，Databricks的人工智能产品势头强劲，吸引了大量投资者，这些产品被大型企业用于从其数据创建人工智能应用程序和代理。该公司看到对这些人工智能解决方案的需求空前，将数据转化为有价值的资产。

在此次投资之前，Databricks最近与微软、谷歌云、Anthropic、SAP和Palantir等主要公司建立了合作关系。Databricks的数据智能平台被全球超过15000家客户使用，使组织能够普及数据访问并将其用于分析和人工智能应用。该平台建立在开源基础上，可帮助公司增加收入、降低成本并管理风险。Databricks由Lakehouse、Apache Spark™、Delta Lake、MLflow和Unity Catalog的创建者创立。

---

## 28. 现代CI过于复杂且误入歧途（2021）

**原文标题**: Modern CI is too complex and misdirected (2021)

**原文链接**: [https://gregoryszorc.com/blog/2021/04/07/modern-ci-is-too-complex-and-misdirected/](https://gregoryszorc.com/blog/2021/04/07/modern-ci-is-too-complex-and-misdirected/)

本文认为，GitHub Actions和GitLab CI等现代CI系统已经变得过于复杂，本质上是在重新发明构建系统。作者认为这些CI系统过于专注于成为特定领域的CI平台，而它们应该成为能够处理CI和构建任务的通用计算平台。

核心论点是，一个足够复杂的CI系统与构建系统变得难以区分，反之亦然。两者都提供计算资源、工件交换、缓存和依赖管理。作者认为CI的冗余导致构建逻辑碎片化，需要管理两个复杂的系统而不是一个。

本文提倡统一CI和构建系统，允许开发者在本地充分利用CI系统的强大功能进行临时任务，而无需将更改推送到远程服务器。

作者批评了像GitHub Actions这样的CI产品，因为它们将主观的配置机制（YAML文件）与远程执行服务紧密结合，使其更像是“产品”而非真正的“平台”。他们赞扬了GitLab Pipelines的动态子管道等功能，但指出缺乏用于调度任意计算的通用API。

作者强调了Mozilla的Taskcluster作为反例。Taskcluster被认为是一个真正通用的CI平台，具有灵活的API用于定义任务，使用户能够构建自己的配置前端，并利用高级安全功能，如细粒度的访问控制。Taskcluster卓越的安全模型与Github Actions和Gitlab CI相比更胜一筹，后者被描述为“数据泄露和软件供应链漏洞工厂”。

---

## 29. Copilot 破坏审计日志，但微软拒绝告知客户

**原文标题**: Copilot broke audit logs, but Microsoft won't tell customers

**原文链接**: [https://pistachioapp.com/blog/copilot-broke-your-audit-log](https://pistachioapp.com/blog/copilot-broke-your-audit-log)

微软M365 Copilot漏洞：访问文件不生成审计日志，引发安全和合规担忧

---

## 30. 我们如何利用CodeRabbit：从简单PR到RCE和百万代码库的写入权限

**原文标题**: How we exploited CodeRabbit: From simple PR to RCE and write access on 1M repos

**原文链接**: [https://research.kudelskisecurity.com/2025/08/19/how-we-exploited-coderabbit-from-a-simple-pr-to-rce-and-write-access-on-1m-repositories/](https://research.kudelskisecurity.com/2025/08/19/how-we-exploited-coderabbit-from-a-simple-pr-to-rce-and-write-access-on-1m-repositories/)

2025年8月，一位安全研究人员详细介绍了他们如何在CodeRabbit的生产服务器上实现远程代码执行(RCE)，导致敏感数据可能泄露并能访问大量代码仓库。该漏洞是在检查CodeRabbit后发现的，CodeRabbit是一个被GitHub和GitLab上超过一百万个代码仓库使用的AI代码审查工具。

该研究人员发现，CodeRabbit会在拉取请求上运行静态分析工具，而它可以通过Ruby静态分析器Rubocop被利用。通过创建一个包含恶意`.rubocop.yml`文件的拉取请求，该文件引用一个包含任意代码的扩展Ruby文件(`ext.rb`)，他们可以在CodeRabbit的服务器上执行代码。这使他们能够提取环境变量。

提取出的环境变量泄露了大量敏感信息，包括Anthropic和OpenAI的API密钥、一个Aperture代理密钥、一个Courier身份验证令牌、加密凭据、一个GitLab个人访问令牌，以及最关键的，CodeRabbit的GitHub App私钥、客户端ID和密钥。这种访问权限授予了该研究人员对使用CodeRabbit的一百万个代码仓库的读写权限。

该漏洞已及时报告给CodeRabbit并在2025年1月得到修复。CodeRabbit禁用了Rubocop，轮换了所有可能被泄露的凭据，在一个安全的沙箱中部署了永久性修复程序，审计了他们的系统，并实施了自动沙箱执行。

---

## 31. 手写的终结

**原文标题**: The End of Handwriting

**原文链接**: [https://www.wired.com/story/the-end-of-handwriting/](https://www.wired.com/story/the-end-of-handwriting/)

文章《手写的终结》探讨了数字时代手写日益衰落及其影响。虽然承认由于电子邮件、智能手机和人工智能的出现，人们对手写的依赖性正在降低，但作者认为手写仍然具有重要价值。

专家认为，手写能力的发展与精细运动技能和识字能力密切相关。研究表明，虽然数字原住民可能达到灵巧性测试的预期，但他们的总体运动能力较低，可能影响他们对手写的准备程度。文章还强调，学习手写具有认知益处，有助于阅读理解和记忆保持。

文章还提出了“文字失忆症”的担忧，即过度依赖打字会导致忘记如何书写文字，这在基于文字的语言中尤为普遍。

出乎意料的是，人工智能的兴起可能会导致手写的复兴。学校正在考虑恢复手写考试，以打击抄袭并确保学生展示真正的理解，因为打字很容易外包给人工智能。

然而，这种潜在的复兴也伴随着警告。糟糕的字迹可能会不公平地惩罚学生，而不管他们的认知能力如何。文章最终得出结论，手写并没有消亡，而可能成为在人工智能主导的世界中证明真正理解的一种方式。

---

## 32. D2（文本转图工具）现已支持 ASCII 渲染

**原文标题**: D2 (text to diagram tool) now supports ASCII renders

**原文链接**: [https://d2lang.com/blog/ascii/](https://d2lang.com/blog/ascii/)

D2 (文本转图工具) 0.7.1 版本引入了 ASCII 渲染功能，允许用户生成 ASCII 文本图。任何扩展名为 `.txt` 的输出文件都将使用此新渲染器。此功能特别适用于在源代码注释中嵌入简单图，D2 Vim 扩展即是例证，它提供了实时预览和代码替换功能。

ASCII 渲染器默认使用 Unicode 字符以获得更好的框线效果，但可以使用 `--ascii-mode=standard` 标志切换到标准 ASCII 以实现最大的可移植性。

需要注意的是，ASCII 渲染器目前处于 alpha 阶段，存在局限性。不支持样式选项，包括动画、字体、主题、双边框和多种功能。某些元素，如特殊文本（Markdown、Latex、Code）、图像、图标、UML 类和 SQL 表，无法渲染。缩放过程可能导致某些情况下间距不均匀。此外，某些形状（如云和圆形）会渲染为左上角带有图标的矩形。

尽管存在这些限制，我们仍然鼓励用户在 D2 Playground 中尝试 ASCII 渲染器，并在 GitHub 上报告遇到的任何问题。

---

## 33. 挑战细胞生命定义的微小微生物

**原文标题**: Tiny microbe challenges the definition of cellular life

**原文链接**: [https://nautil.us/a-rogue-new-life-form-1232095/](https://nautil.us/a-rogue-new-life-form-1232095/)

爱丽丝·孙在《鹦鹉螺》杂志上发表的文章讨论了对*Sukunaarchaeum mirabile*的发现，这是一种基因组异常微小的古菌，挑战了细胞生命的传统定义。 *Sukunaarchaeum*是由中山拓郎及其团队在研究甲藻*Citharistes regius*中的微生物时意外发现的，仅拥有23.8万个碱基对，使其成为已知基因组最小的古菌。

它的独特之处在于其对宿主的极端代谢依赖性。与其他古菌和细菌不同，*Sukunaarchaeum*似乎无法独立执行基本的代谢功能，完全依赖*C. regius*提供能量和营养。这种程度的依赖性是前所未有的，模糊了古菌和病毒之间的界限。虽然病毒也依赖宿主，但与病毒不同，*Sukunaarchaeum*拥有核糖体并且可以自我复制。

通过分析海洋遗传数据，研究人员在全球范围内发现了相似的序列，表明可能存在一个巨大的、以前未知的古菌谱系。中山认为这一发现突显了“微生物暗物质”的存在——挑战我们对生命理解的未识别微生物。病毒学家Mart Krupovic认为这一发现非常了不起，并指出微生物世界仍有许多未知之处。

中山未来的研究旨在培养和分离*Sukunaarchaeum*，以研究其生物学，并了解其在“生命边缘”独特的生存策略。

---

## 34. 联邦紧急事务管理局现在要求灾民提供电子邮件地址

**原文标题**: FEMA Now Requires Disaster Victims to Have an Email Address

**原文链接**: [https://www.wired.com/story/fema-now-requires-disaster-victims-to-have-an-email-address/](https://www.wired.com/story/fema-now-requires-disaster-victims-to-have-an-email-address/)

联邦紧急事务管理局现要求灾难幸存者必须拥有电子邮件地址才能注册联邦援助，这项政策变更自8月12日起生效，与之前的做法不同，并引发担忧。 联邦紧急事务管理局表示，此举旨在简化沟通并过渡到数字支付。 然而，联邦紧急事务管理局雇员担心，这项要求将对互联网接入有限的弱势群体，特别是低收入个人和种族/族裔少数群体，产生不成比例的影响。

文章强调了那些无法轻易获得或管理电子邮件账户的人可能被排除在外的问题，并引用了美国国家电信和信息管理局（NTIA）的数据，该数据显示，很大比例的家庭，尤其是在密苏里州和田纳西州（联邦紧急事务管理局工作人员报告问题的地方），缺乏互联网接入。 一位联邦紧急事务管理局工作人员报告说，他看到一位同事拒绝了一位没有电子邮件地址的申请人。

虽然联邦紧急事务管理局辩称，大多数美国人都有电子邮件，并且在线账户是保持知情的最佳方式，但人们对老年人和那些数字素养有限的人难以操作在线系统表示担忧。

这项变革正与其他转变同时发生，比如逐步取消挨家挨户的调查，引发了人们对最弱势群体获得援助的担忧。 现任和前任联邦紧急事务管理局雇员都认为该系统已经过时，需要改进，但担心要求提供电子邮件地址会为那些最需要灾难援助的人制造障碍。

---

## 35. .NET快速且可观测的后台任务处理

**原文标题**: Fast and observable background job processing for .NET

**原文链接**: [https://github.com/mikasjp/BusyBee](https://github.com/mikasjp/BusyBee)

BusyBee是一个高性能的 .NET 后台作业处理库，它利用原生通道来提高效率。它提供了一个简单、可配置和可观察的解决方案来管理后台任务，包括内置的 OpenTelemetry 支持，用于监控和追踪。

主要特性包括：

*   **高性能：** 基于 .NET 通道的内存队列，用于快速处理。
*   **可配置性：** 提供无界或有界队列，具有各种溢出策略（等待、忽略、抛出异常、丢弃最旧、丢弃最新），全局和每个作业的超时，以及可配置的并行处理。
*   **可观察性：** 提供作业执行日志记录、OpenTelemetry 追踪，以及详细的指标，如作业计数、执行时间和等待时间。
*   **开发者友好：** 具有流畅的配置 API、依赖注入支持、取消令牌支持和丰富的作业上下文。

配置非常简单，允许自定义队列行为、超时和并行性。作业会收到一个包含唯一 ID、计时细节以及对已注册服务的访问权限的上下文。OpenTelemetry 集成支持监控和分析。

该库通过自定义 `IJobFailureHandler` 和 `IJobTimeoutHandler` 实现提供可扩展性。它还提供了处理长时间运行作业的指导，包括取消和进度记录的重要性。最佳实践强调作业幂等性、适当的超时、监控和取消处理。

该库欢迎贡献。一个演示应用程序提供了一个完整的示例，包括 Web API、OpenTelemetry 设置、Seq 日志记录和 Prometheus 集成。

---

## 36. 我是如何让Ruby比Ruby更快的

**原文标题**: How I Made Ruby Faster Than Ruby

**原文链接**: [https://noteflakes.com/articles/2025-08-18-how-to-make-ruby-faster](https://noteflakes.com/articles/2025-08-18-how-to-make-ruby-faster)

本文详细介绍了作者优化 Ruby HTML 模板库 P2 性能的历程。P2 的独特之处在于它将模板源代码编译为高效的 Ruby 代码，避免了运行时解释。

最初，P2 比 Papercraft 快，但比 ERubi 慢。通过 byroot 的贡献，作者确定了 P2 代码生成中需要改进的关键领域。原始代码生成内插字符串，使用昂贵的 rescue 子句，并生成非冻结字符串。

然后，作者重写了编译器，以：

* 分离 HTML 生成，分别推送静态和动态部分。
* 删除 rescue 子句，并在 `Proc#render` 方法中处理回溯转换。
* 添加 `# frozen_string_literal: true` 魔术注释来冻结静态 HTML 字符串，从而减少分配。
* 从 `CGI.escape_html` 切换到 `ERB::Escape.html_escape`，以实现更快的 HTML 转义。

这些更改带来了显著的性能提升，使 P2 的速度与编译后的 ERB 和 ERubi 模板相当。基准测试表明，P2 现在的性能与 ERB/ERubi 类似，并且比 Papercraft 和 Phlex 等非编译模板方法快得多（大约 10 倍）。

作者得出结论，这些优化突显了 Ruby 在高效编写代码时具有的高性能潜力。他们提倡将 Ruby 到 Ruby 的编译技术应用于其他 DSL 和应用程序。

---

## 37. 展示一下：用于Claude Code的项目管理系统

**原文标题**: Show HN: Project management system for Claude Code

**原文链接**: [https://github.com/automazeio/ccpm](https://github.com/automazeio/ccpm)

Claude Code PM 是一款项目管理系统，旨在利用 Claude Code、GitHub Issues、Git Worktrees 和并行 AI 代理来改进软件开发工作流程。它解决了常见的团队挑战，例如上下文丢失、并行工作冲突、需求偏差和隐藏进度。

该系统通过完整的可追溯性来促进规范驱动开发，从 PRD 到史诗、GitHub Issues 和生产代码。主要功能包括持久化上下文、并行代理执行、GitHub 集成（使用 Issues 作为单一真相来源）、代理专业化和完整的审计跟踪。

该工作流程包含五个阶段：产品规划（创建 PRD）、实施规划（将 PRD 转换为史诗）、任务分解（将史诗分解为可执行的任务）、GitHub 同步（将史诗和任务推送到 Issues）以及执行（专门的代理实现任务）。`/pm:prd-new`、`/pm:epic-oneshot` 和 `/pm:issue-start` 等命令可促进这些阶段。

“并行执行系统”利用多个代理同时处理单个 Issue 的不同方面，从而优化速度和上下文管理。它旨在将战略性的主要对话与由各个代理处理的详细实施细节分开。

使用该系统的团队报告说，在上下文切换、任务并行化、错误减少和功能交付速度方面都有所改进。该系统旨在与现有的 GitHub 工作流程和工具集成，为人类和 AI 代理大规模协作提供协作协议。设置包括克隆存储库、初始化 PM 系统和启动上下文。

---

## 38. 使用 Emacs 进行视频剪辑

**原文标题**: Emacs as your video-trimming tool

**原文链接**: [https://xenodium.com/emacs-as-your-video-trimming-tool](https://xenodium.com/emacs-as-your-video-trimming-tool)

本文探讨了使用 Emacs 作为视频剪辑工具的方法，其灵感来自 Marcin 'mbork' Borkowski 的一篇博文。作者受 Ready Player Mode 中自带的“图形化”进度条的启发，创建了 `video-trimmer-mode`——一个简单的 Emacs 视频剪辑工具。该工具利用 `ffmpeg` 进行实际的视频处理，代码大约 300 行。作者选择分享代码在其 Emacs 配置文件仓库中的位置，而不是在文章中包含整个代码片段，以便进行持续的调整和更新。最后，作者以独立开发者的身份推广自己的工作，鼓励读者通过赞助、创建博客或购买其 macOS/iOS 应用来支持他们的努力。文章最后提及了 LMNO.lol，并附带隐私政策和服务条款链接。

---

## 39. 人工智能抛售是更大趋势的开端吗？

**原文标题**: Is the A.I. Sell-Off the Start of Something Bigger?

**原文链接**: [https://www.nytimes.com/2025/08/20/business/dealbook/ai-dip-blip-palantir-nvidia.html](https://www.nytimes.com/2025/08/20/business/dealbook/ai-dip-blip-palantir-nvidia.html)

无法访问文章链接。

---

## 40. 使用 Apache ECharts 的 Rails 图表

**原文标题**: Rails Charts Using ECharts from Apache

**原文链接**: [https://github.com/railsjazz/rails_charts](https://github.com/railsjazz/rails_charts)

本文介绍 `rails_charts` gem，一个 Ruby on Rails 库，它简化了使用 Apache ECharts 库创建各种图表类型。它提供了一个直观的界面，灵感来自 Chartkick，但具有更广泛的图表选项和自定义功能。

该 gem 支持面积图、折线图、柱状图、甜甜圈图、饼图、雷达图、日历图、K 线图、漏斗图、仪表盘图、平行坐标图、桑基图、散点图、堆叠柱状图和自定义图表。提供了针对 Sprockets、Webpack/esbuild 和 Importmaps 的安装说明。

主要功能包括可自定义的选项，如宽度、高度、主题、CSS 类、ID 和内联样式。它还允许直接访问 Apache ECharts 选项以进行高级配置，包括用于工具提示的 JavaScript 函数集成。

本文包含每种图表类型的代码示例，展示了如何以最少的代码和选项定制生成它们。它强调每个图表都带有可以覆盖的默认配置。

本文最后呼吁大家贡献力量，概述了潜在的改进领域，例如 Turbo Streams 支持、改进的文档以及处理不同数据结构的示例。它还提供了有关如何升级底层 ECharts 库和设置开发环境的说明。

---

## 41. 登上HN首页的价值

**原文标题**: The value of hitting the HN front page

**原文链接**: [https://www.mooreds.com/wordpress/archives/3530](https://www.mooreds.com/wordpress/archives/3530)

本文基于作者在 Hacker News (HN) 平台的丰富经验，探讨了登上 HN 首页的价值和局限性。 虽然 HN 排名靠前的帖子可以带来巨大的流量，但它主要用于品牌宣传，通常不会带来很高的转化率（例如，销售额、注册量）。

作者强调了评论区的重要性。 HN 提供了来自知识渊博的受众的宝贵反馈，应仔细考虑并与之互动。 不要忽视或冒犯评论，而是利用它们来了解你的作品是如何被感知的。

此外，作者指出，一篇成功的 HN 帖子可以引导来自其他平台（新闻通讯、社交媒体）的后续流量，因为人们会发现并分享内容。 识别这些来源并与它们互动可能是有益的。 此外，如果你发布的帖子登上了首页，预计会收到别人的感谢。

作者强调，不应将 HN 视为营销计划或可靠流量的来源，因为该平台是不可预测的。 同样重要的是要记住，HN 的用户群并不代表更广泛的市场，因此应在该背景下考虑反馈。 总之，HN 有助于品牌宣传和收集来自特定技术受众的反馈，但不能作为转化的直接驱动力或可靠的流量来源。

---

## 42. 定制 Lisp REPL

**原文标题**: Customizing Lisp REPLs

**原文链接**: [https://aartaka.me/customize-repl.html](https://aartaka.me/customize-repl.html)

阿尔乔姆·博洛戈夫提倡定制现有的 Common Lisp REPL，而不是使用代理 REPL，强调可移植性和利用现有工具。他认为代理 REPL 以不兼容的方式重新发明了已有的功能，而原生 REPL 可以逐步改进，从而实现普遍受益。

本文详细介绍了增强原生 REPL 的几种方法。首先，使用 "Trivial Toplevel Prompt" 库自定义提示符，以显示进程名称、包、命令编号和调试级别。其次，使用 "Trivial Toplevel Commands" 创建自定义 REPL 命令，例如 shell 调用或目录列表，使 REPL 更具交互性。第三，利用读取器宏来扩展 Lisp 语法，在不改变底层 REPL 的情况下提供灵活性。

作者还提到了 GUI 调试器，并认识到它们与实现原生调试器相比的局限性，后者提供更深入的集成和更强大的调试功能，如反汇编、变量修改和模拟返回。他建议使用 Readline/rlwrap 进行行编辑、补全和按键绑定，以非侵入方式增强 REPL 体验。最后，他建议使用 git 子模块管理库，以进行版本固定和离线访问，并使用 ASDF 将它们集成到项目中。

虽然博洛戈夫承认像 CIEL 这样的代理 REPL 在提供预加载库和错误美化等功能方面的便利性，但他强调了它们的缺点，包括失去原生功能和特定于实现的自定义选项。他最后敦促读者利用和定制原生 REPL，以实现更加个性化和符合人体工程学的 Lisp 开发环境。

---

## 43. Objective-Smalltalk的四个阶段

**原文标题**: The Four Stages of Objective-Smalltalk

**原文链接**: [https://blog.metaobject.com/2019/12/the-4-stages-of-objective-smalltalk.html](https://blog.metaobject.com/2019/12/the-4-stages-of-objective-smalltalk.html)

马塞尔·韦赫概述了Objective-Smalltalk的四个发展阶段，每个阶段都建立在前一个阶段的基础上，并提供更高的价值。

**第一阶段：WebScript 2/"Shasta"** 这一阶段旨在创建一个干净、类似于Smalltalk的脚本语言，摆脱从Objective-C与C集成中继承的语法负担。这种语言让人想起WebScript，专注于成为一个高度互动和可塑的脚本环境，非常适合调整和与运行中的应用程序交互。

**第二阶段：没有C的Objective-C** 这一阶段的重点是创建第一阶段脚本语言的本地、AOT编译版本，以取代Objective-C，从而提供脚本和“编程”之间更平滑的集成。脚本环境和编译环境之间代码迁移的便利性将得以保持。

**第三阶段：面向架构的编程** 这一阶段超越了简单的面向对象编程，通过利用Objective-Smalltalk的可塑性来探索和实现语言内部的架构概念。韦赫专注于整合三种流行的架构风格：面向对象、Unix管道和过滤器以及REST，并将它们与现有的语言元素对齐。

**第四阶段：面向架构的元编程** 最后一个阶段旨在允许用户在语言本身中定义和改进自己的架构风格，超越硬编码框架，并实现真正可定制的架构范例。

韦赫总结说，每个阶段都具有独立的价值，并且与后续阶段结合使用时会变得更加强大。他还承认需要返回到第四阶段才能完成实施。

---

## 44. 机器学习的高斯过程 (2006) [pdf]

**原文标题**: Gaussian Processes for Machine Learning (2006) [pdf]

**原文链接**: [https://gaussianprocess.org/gpml/chapters/RW.pdf](https://gaussianprocess.org/gpml/chapters/RW.pdf)

高斯过程在机器学习中的应用 (2006) 是一本全面探索高斯过程（GPs）作为各种机器学习任务强大工具的书籍。本书涵盖了理论基础和实际应用，对研究人员和从业者都具有价值。

本书首先介绍贝叶斯建模的核心概念，并为本书的其余部分提供路线图。然后深入研究具体的应用，从回归和分类开始，解释如何将GPs应用于这些问题，包括对拉普拉斯近似和期望传播进行GP分类的详细介绍。本书涵盖了协方差函数，探索了不同的类型以及如何构建新的协方差函数。书中讨论了核函数的特征函数分析和非矢量输入的核函数。

本书广泛介绍了模型选择和超参数调整，包括贝叶斯模型选择和交叉验证方法。本书研究了GPs与其他机器学习模型之间的关系，例如再生核希尔伯特空间、样条模型、支持向量机和相关向量机。还讨论了诸如等价核、渐近分析和PAC-贝叶斯分析等理论视角。本书通过介绍降秩近似和稀疏GP技术（包括回归子集和Nyström方法）等近似方法来解决大型数据集的挑战。

最后，本书以对进一步问题和结论的讨论结尾，涵盖了诸如多输出、非高斯似然、导数观测、不确定输入、高斯过程混合、全局优化和潜在变量模型等主题。附录提供了必要的数学背景，并讨论了高斯马尔可夫过程。

---

## 45. 基于 llms.txt 的 HTML 内联 LLM 指令提案

**原文标题**: A proposal for inline LLM instructions in HTML based on llms.txt

**原文链接**: [https://vercel.com/blog/a-proposal-for-inline-llm-instructions-in-html](https://vercel.com/blog/a-proposal-for-inline-llm-instructions-in-html)

本文提出了一种新的约定，即使用 `<script type="text/llms.txt">` 将 AI 代理的指令直接嵌入到 HTML 中。它解决的问题是，如何告知 AI 代理（例如代码助手）如何访问受保护的资源，例如需要身份验证的预览部署。

文章重点介绍了 Vercel 的用例，其中受保护的预览部署阻止 AI 代理直接访问。虽然 Vercel 提供了诸如具有 `get_access_to_vercel_url` 等功能的 MCP 服务器之类的机制，但代理需要一种发现这些资源的方法。

该解决方案利用新兴的 `llms.txt` 标准，通过使用自定义类型为 "text/llms.txt" 的 `<script>` 标签将指令嵌入到 HTML 中，从而针对 AI 内容。浏览器将忽略此标签，确保对渲染没有影响，而 LLM 可以解析这些指令。文章强调了其优势：易于实施，无需正式标准化，并且与现有 LLM 功能兼容。

文章还提供了一个真实的例子，说明 Vercel 如何使用这种方法来指示代理如何获取身份验证绕过令牌并访问受保护的部署。它强调了超越身份验证的潜在用例，例如将代理定向到 MCP 服务以进行错误调查。作者鼓励开发人员立即开始使用此约定。

---

## 46. “混蛋”被遗忘的含义

**原文标题**: The forgotten meaning of "jerk"

**原文链接**: [https://languagehat.com/the-forgotten-meaning-of-jerk/](https://languagehat.com/the-forgotten-meaning-of-jerk/)

这篇文章探讨了“jerk”一词的语义转变，从最初“傻瓜”或“笨蛋”的意思演变为现在“令人讨厌的人”的意思。作者languagehat受到Ben Lindbergh文章的启发，Lindbergh注意到了这一变化，并质疑“jerk”是否一直意味着“混蛋”。

Lindbergh强调，即使是以前用“jerk”的原始含义的人似乎也忘记了这种用法，他引用了Dave Barry的写作中的例子，说明了该词的含义如何随着时间推移而演变。作者还分享了自己的经历，最初认为“jerk”一直意味着“混蛋”，但后来回忆起自己曾用它来表示“傻瓜”。

评论区进一步探讨了这个词的演变和地域差异。评论者们争论他们第一次遇到这个词是什么时候，以及它的不同含义，有些人记得“傻瓜”的含义，而另一些人只知道“令人讨厌”的含义。讨论深入探讨了“jerk”的词源，包括其可能与“jerk off”和“soda jerk”的联系，以及这些联系如何影响了它的含义。一位评论者还指出，Sondheim为《Gee, Officer Krupke!》创作的歌词是“jerk”的过渡用法。

---

## 47. 英特尔代工展示基于18A节点的首款Arm芯片

**原文标题**: Intel Foundry Demonstrates First Arm-Based Chip on 18A Node

**原文链接**: [https://hothardware.com/news/intel-foundry-demos-deer-creek-falls-reference-soc](https://hothardware.com/news/intel-foundry-demos-deer-creek-falls-reference-soc)

2025年8月，英特尔代工展示了其18A工艺，推出了名为“鹿溪瀑布”的参考级片上系统(SoC)，该系统采用基于Arm的内核和生态系统IP。一段短暂出现在YouTube上的视频揭示了Arm SoC典型的三层CPU核心配置（节能、功率优化和高性能）。该SoC明确使用了AArch64架构，证实了其基于Arm的特性。

英特尔制造Arm SoC的动机很可能是为了吸引其代工服务的外部客户，特别是考虑到Arm芯片设计的普及。此次演示驳斥了英特尔代工缺乏必要性能优化工具以服务外部客户的传言，并可能解决了人们对在英特尔工艺上实现设计困难的担忧。

虽然“鹿溪瀑布”采用了18A工艺（已不对外部客户开放），但它可能作为英特尔能力的证明，以吸引客户使用即将推出的14A节点。据报道，苹果和英伟达正在评估英特尔的14A节点，与任何一家公司达成合同都将是英特尔代工的一大胜利，后者需要外部客户来避免可能暂停未来节点开发的局面。

---

## 48. Figma多人协作技术原理 (2019)

**原文标题**: How Figma’s multiplayer technology works (2019)

**原文链接**: [https://www.figma.com/blog/how-figmas-multiplayer-technology-works/](https://www.figma.com/blog/how-figmas-multiplayer-technology-works/)

这篇题为“Figma多人协作技术原理（2019）”的短文，重点介绍了Figma于2016年9月发布的多人编辑功能。虽然标题暗示会深入探讨技术层面，但实际内容主要侧重于宣布该功能的公开发布。

关键信息是这项发布本身：Figma推出了实时协作编辑功能，允许多个用户同时处理同一个设计文件。文章将其定位为一次重大更新，也是用户一直热切期盼的功能。

尽管标题暗示会解释多人协作功能背后的技术，但内容并未兑现这一承诺。它只是标志着该功能公开发布的时刻，并将此公告归类于Figma内部的“产品更新”、“工程”和“新闻”之下。因此，主要信息仅仅是Figma于2016年9月发布了其广受欢迎的多人编辑功能。

---

## 49. Show HN：我做了一个易于扩展且灵活的JavaScript日志记录器

**原文标题**: Show HN: I've made an easy to extend and flexible JavaScript logger

**原文链接**: [https://github.com/inshinrei/halua](https://github.com/inshinrei/halua)

此“Show HN”帖子介绍 Halua，一个旨在为 JavaScript 提供灵活的日志、指标以及潜在的其他相关功能控制的 JavaScript 包。要点包括：

*   **目的：** Halua 旨在提供 JavaScript 应用程序中全面的日志解决方案。
*   **特性：** 它支持多种输出格式，特别是文本、JSON 和控制台处理程序。
*   **可扩展性：** 一个核心优势是其易于扩展，允许开发人员创建和集成针对特定需求定制的自定义处理程序。
*   **文档：** “Halua 之旅”提供了介绍基本概念的入门文档。
*   **安装：** 可以使用 npm 轻松安装该包，命令为 `npm i halua`。

---

## 50. 安度因操作系统

**原文标题**: AnduinOS

**原文链接**: [https://www.anduinos.com/](https://www.anduinos.com/)

AnduinOS 是一款免费开源的、基于 Ubuntu 的 Linux 发行版，专为易用性而设计，尤其适合 Linux 新手。它拥有用户友好的 GNOME 桌面环境，仅 2.0GB 的 ISO 镜像大小方便安装，并且兼容 Ubuntu 庞大的软件生态系统。其核心设计原则是隐私，不收集、追踪或分析用户数据。

AnduinOS 提供两个版本：LTS（长期支持版）和标准版。LTS 版本基于 Ubuntu 24.04，采用 Gnome 46 和 Linux kernel 6.11，推荐给寻求稳定性和长期支持的用户，支持至 2029 年 4 月。标准版基于 Ubuntu 25.04，采用 Gnome 48 和 Linux kernel 6.14，面向拥有较新硬件并渴望最新功能的用户，支持至 2026 年 1 月。标准版使用 Flatpak 管理图形应用程序，增强了安全性和稳定性。

AnduinOS 可用于各种用途，从日常计算和开发到服务器应用程序和学习。用户评价强调了其简洁的设计、用户友好性、优于 Windows 的性能改进以及对注重隐私用户的适用性。该操作系统强调易用性，特别是对于 Windows 迁移用户。支持通过 GitHub Discussions 提供，并依赖 Ubuntu 庞大的文档和专业知识。该项目由用户捐款资助，并欢迎通过 Revolt 和 GitHub 进行社区贡献。

---

## 51. 微型可拆卸“迷你固态硬盘”最终可能对掌上游戏机意义重大

**原文标题**: Tiny, removable "mini SSD" could eventually be a big deal for gaming handhelds

**原文链接**: [https://arstechnica.com/gadgets/2025/08/tiny-removable-mini-ssd-could-eventually-be-a-big-deal-for-gaming-handhelds/](https://arstechnica.com/gadgets/2025/08/tiny-removable-mini-ssd-could-eventually-be-a-big-deal-for-gaming-handhelds/)

Ars Technica 文章探讨了“迷你 SSD”作为游戏掌机快速、可移动存储解决方案的潜力，以应对现代游戏日益增长的存储需求。目前，microSD Express 卡是标准配置，但其性能通常落后于内置 SSD。

佰维的迷你 SSD 是一种微型 15x17 毫米卡，旨在通过 PCIe 4.0 接口实现高达 3,700MB/s 的读取速度，从而弥补这一差距。这些卡容量从 500GB 到 2TB 不等，通过类似于 SIM 卡的托盘插入。 中国游戏掌机，如 GPD Win 5 和 OneXPlayer Super X，已经开始宣传对该技术的支持。

文章强调了由于更高分辨率的纹理、音频文件和广泛的本地化，游戏体积日益增长。 《最后生还者第一部》和《赛博朋克2077》等游戏体现了这一趋势，音频和语言文件对整体安装大小贡献巨大。《赛博朋克2077》的 Mac App Store 版本就是一个特别引人注目的例子，由于包含所有支持语言的配音，因此需要 159GB 的空间。

迷你 SSD 虽然不是一项获得批准的标准，但它试图解决便携式系统对快速、易于升级的存储的需求问题。 文章总结说，无论是迷你 SSD、改进的 microSD Express 还是其他格式，游戏对更快、更便捷的存储解决方案的需求都是显而易见的。

---

## 52. 石墨烯电容器实现太赫兹波的快速高深度调制

**原文标题**: Graphene capacitors achieve rapid, high-depth modulation of terahertz waves

**原文链接**: [https://phys.org/news/2025-08-graphene-capacitors-rapid-high-depth.html](https://phys.org/news/2025-08-graphene-capacitors-rapid-high-depth.html)

剑桥大学研究人员开发了一种利用石墨烯电容器快速有效控制太赫兹辐射的新方法，太赫兹辐射是电磁波谱中一个具有挑战性的部分。这项创新有望在通信、成像和传感技术方面取得重大进展。

该团队在超材料（微型谐振器阵列）中利用超小型石墨烯贴片创建了可调电容器。与以往通过抑制谐振来调制太赫兹波的方法不同，这种方法通过移动谐振来实现更强的控制。这些宽度小于一微米的石墨烯贴片在纳米尺度上充当可调电容器。该设备设计通过反射其背面信号来增强性能。

这种新颖的设计实现了超过 99.99% 的调制深度，速度高达 30 MHz，这是以前无法实现的组合。这大大优于现有的调制器技术，并可以适用于整个太赫兹范围。

研究人员认为，他们的设计可以应用于其他基于超材料的调制器，从而可能影响未来依赖谐振器性能的技术。随着目前的研究重点集中在太赫兹通信系统上，这些发现代表着朝着超越 5G 和 6G 的下一代通信技术迈出了重要一步。

---

## 53. 打字机

**原文标题**: Type-machine

**原文链接**: [https://arthi-chaud.github.io/posts/type-machine/](https://arthi-chaud.github.io/posts/type-machine/)

本文介绍了`type-machine`，一个利用Template Haskell的Haskell库，旨在增强记录类型操作并模拟结构子类型，其灵感来源于TypeScript的类型转换器。该库提供函数来派生记录类型，并为结构子类型生成类型类。

其核心功能围绕`type_`函数展开，该函数使用`TM Type`计算来派生类型，并使用诸如`pick`、`omit`、`record`、`intersection`和`apply`等类型转换器来操作记录结构。 中缀运算符`<:>`和`<::>`简化了这些转换器的应用。 `defineIs`为每个字段生成带有getter、setter和转换函数的类型类，而`deriveIs`则为这些类型类创建实例。

文章重点介绍了在Web API开发中的优势，允许从数据库模型（UserRecord）派生面向用户的模型（UserResponse，UserForm）。 虽然承认了诸如需要`DuplicateRecordFields`、单构造函数约束以及对诸如`defineConstraint`函数的需求等限制，但该库在记录建模方面表现出比异构列表更优越的运行时性能。 微基准测试表明，在构建和遍历时间方面，`type-machine`比`extensible`和`superrecord`快得多。 作者欢迎反馈和贡献。

---

## 54. 使用谐波驱动和ESP32的定制望远镜赤道仪

**原文标题**: Custom telescope mount using harmonic drives and ESP32

**原文链接**: [https://www.svendewaerhert.com/blog/telescope-mount/](https://www.svendewaerhert.com/blog/telescope-mount/)

Sven De Waerhert 详述了他使用谐波减速器和 ESP32 微控制器构建定制望远镜赤道仪的历程，其动力源于渴望获得比基本跟踪器更好的天文摄影效果。由于对商业赤道仪的高昂价格感到沮丧，他利用了新获得的 PCB 设计技能和开源资源。

该项目涉及对谐波减速器、步进电机和开源 FOC 实现的广泛研究。他设计了一款定制 PCB，用于电机控制、通过 USB-C 供电以及未来的扩展功能。赤经和赤纬轴采用集成了谐波减速器的集成电机，以实现精确跟踪。

该构建集成了 OnStepX 固件，用于望远镜赤道仪控制，解决了最初的 WiFi 不稳定问题。制造由 JLCPCB 负责，组装过程中需要进行少量调整。

尽管在极轴对齐、软件配置和第一版 PCB 的昂贵错误方面存在最初的挑战，但该赤道仪实现了 1-2 角秒的精度，适用于使用 600 毫米镜头进行 30 秒的曝光。

虽然项目总成本达到约 1,700 欧元（估计单个设备为 800 欧元），但主要动机不是节省成本，而是学习经验以及构建功能性定制望远镜赤道仪的满足感。该项目显着提高了他在 PCB 设计、FreeCAD 建模和天文摄影技术方面的技能。文章强调了动手经验的价值以及通过从头开始构建赤道仪获得的深刻理解。

---

## 55. 醉汉主教 (2023)

**原文标题**: Drunken Bishop (2023)

**原文链接**: [https://re.factorcode.org/2023/08/drunken-bishop.html](https://re.factorcode.org/2023/08/drunken-bishop.html)

本文解释了 OpenSSH 使用的“醉汉主教”算法，该算法以可视方式表示公钥指纹，使用户更容易识别更改。该算法是一种“随机艺术”，将密钥的哈希值转换为网格上的 ASCII 艺术图像。

作者详细介绍了该算法的工作原理：它从网格的中心开始，哈希值的每 2 位块决定了“主教”的对角线移动方向。主教在网格上移动，递增每个访问单元格中的计数器，但移动会被网格边缘阻挡。起始位置和结束位置被特别标记。

文章随后提供了该算法的 Factor 编程语言实现，包括网格尺寸的常量和用于基于每个单元格中的计数器值渲染网格的 ASCII 符号。代码片段演示了如何将十六进制字符串转换为字节，然后使用 `drunken-bishop.` 函数生成可视化表示。

最后，作者指出，此功能在 Factor 语言的最新开发版本中的“drunken-bishop”词汇表中可用。

---

## 56. 为什么语义层很重要（以及如何使用 DuckDB 构建一个）

**原文标题**: Why Semantic Layers Matter (and how to build one with DuckDB)

**原文链接**: [https://motherduck.com/blog/semantic-layer-duckdb-tutorial/](https://motherduck.com/blog/semantic-layer-duckdb-tutorial/)

语义层为何重要 — 以及如何使用 DuckDB 构建一个

本文探讨了语义层在数据分析中的价值，并演示了如何使用 YAML、Python、Ibis 和 DuckDB 构建一个基本的语义层。文章首先概述了不需要语义层的情况，例如处理简单分析、单个消费者或预处理指标时。

随后，文章深入探讨了使用语义层的原因：跨工具的统一指标定义、即席查询的缓存、统一的访问级别安全性、复杂分析的动态查询重写以及为 LLM 提供上下文。作者强调，语义层弥合了业务需求和数据源之间的差距，尤其有利于拥有大量 KPI 的大型企业。

该实践示例侧重于一个简单的语义层，使用 YAML 定义指标和维度，并使用 Ibis 将查询转换为 DuckDB。它使用纽约出租车数据集来说明这些概念。文章展示了如何使用 DuckDB 命令（如 `COUNT` 和 `DESCRIBE`）来探索数据，然后演示了语义层如何定义计算度量和维度。文章阐明了持久数据集和临时聚合之间的区别，并认为后者需要语义层。

文章强调，虽然此示例很简单，但更高级的语义层提供 API、安全控制和缓存层。文章还引用了外部资源，以便进一步探索语义层和相关概念。

---

## 57. CRDT：文本缓冲区

**原文标题**: CRDT: Text Buffer

**原文链接**: [https://madebyevan.com/algos/crdt-text-buffer/](https://madebyevan.com/algos/crdt-text-buffer/)

本文介绍了一种用于协同编辑文本字符串的 CRDT (无冲突复制数据类型) 算法，类似于 Yjs 和 Automerge 等库中使用的算法。其核心思想是基于创建者的站点、时钟和父指针为每个字符分配一个唯一标识符。插入操作通过将父指针设置为紧接插入点之前的字符来跟踪。字符顺序通过前序树遍历确定，兄弟节点之间的顺序通过计数器和站点 ID 解决。删除操作通过将字符的标识符添加到“已删除集合”来处理，本质上是创建一个墓碑。

本文重点介绍了关键优化：将来自同一站点的连续插入合并到内存块中，将这些块连续存储在预排序的数组中，以及使用基于范围的表示来表示连续删除的删除集合。

本文列出了诸如合理的内存使用和查询及更新的 O(log n) 性能等优点。它还指出了缺点：拆分和合并逻辑的复杂性、需要模糊测试，以及删除操作不会减少元数据大小的“只增长”性质。在保持对等体之间一致性的同时解决数据删除问题被认为是一个重大挑战。本文最后引用了有关 CRDT 文本缓冲区的其他资源。

---

## 58. Show HN: OpenAI/reflect – 照亮你生活的物理AI助手

**原文标题**: Show HN: OpenAI/reflect – Physical AI Assistant that illuminates your life

**原文链接**: [https://github.com/openai/openai-reflect](https://github.com/openai/openai-reflect)

Reflect：OpenAI的无屏AI助手原型，利用用户的手机作为信息中心，通过声音、光线和色彩与用户交互，反思过去、准备未来、提高效率并感知位置。项目易修改、低成本、易获取。目前，Reflect基于M5Stack CoreS3 ESP32S3 loT开发套件和LIFX Color A19灯。设置包括安装esp-idf，克隆仓库，并将代码刷入设备。连接到设备WiFi热点后，用户可以通过网页开始会话并调试音频流。视频演示了设备的功能。代码按原样提供，不作任何保证，请谨慎使用。

---

## 59. 2025年我们为什么还要用Ruby

**原文标题**: Why we still build with Ruby in 2025

**原文链接**: [https://www.getlago.com/blog/why-we-still-build-with-ruby-in-2025](https://www.getlago.com/blog/why-we-still-build-with-ruby-in-2025)

题为“2025年我们为何依旧使用Ruby构建”的短文，重点介绍了使用Lago平台，特别是针对基于Ruby的项目，在账单方面的优势。核心论点是，无论用户选择高级版还是开源版，Lago都能消除账单方面的顾虑。

文中强调了两个选项：Lago高级版和Lago开源版。 Lago高级版被认为是需要控制和灵活性的团队的理想解决方案，并邀请读者预订演示。 Lago开源版则定位为较小项目的最佳选择，鼓励用户部署开源版本。

核心信息是，Lago在2025年为Ruby开发提供了一个可靠且无忧的账单解决方案，使开发人员能够专注于构建和项目成功，而不是管理复杂的账单。 该文表明，Lago的高级版或开源版方法都提供了可行且可靠的账单解决方案。

---

## 60. 家得宝因在自助结账处“秘密”使用面部识别技术而被起诉

**原文标题**: Home Depot Sued for 'Secretly' Using Facial Recognition at Self-Checkouts

**原文链接**: [https://petapixel.com/2025/08/20/home-depot-sued-for-secretly-using-facial-recognition-technology-on-self-checkout-cameras/](https://petapixel.com/2025/08/20/home-depot-sued-for-secretly-using-facial-recognition-technology-on-self-checkout-cameras/)

本杰明·扬科夫斯基作为家得宝的顾客，对这家零售业巨头提起了一项拟议的集体诉讼，指控该公司秘密在其伊利诺伊州门店的自助结账机上使用面部识别技术。扬科夫斯基声称，最近一次在芝加哥家得宝购物时，他注意到自助结账屏幕上他的脸周围出现了一个绿色框，这让他相信自己的面部特征在未经同意的情况下被记录下来。

该诉讼称，家得宝于2024年实施的“计算机视觉”技术，旨在减少盗窃，该技术会捕捉并存储购物者的面部几何数据，违反了伊利诺伊州生物识别信息隐私法（BIPA）。BIPA要求公司告知个人关于生物识别数据的收集，解释其用途，并获得书面同意——扬科夫斯基声称家得宝未能做到所有这些。

扬科夫斯基寻求代表其他据称在未经同意的情况下被扫描面部数据的伊利诺伊州购物者。他请求法院判决每项疏忽违反BIPA的行为赔偿1000美元，每项故意违反行为赔偿5000美元。该诉讼将此案与来德爱(Rite Aid)案件相提并论，在该案中，由于来德爱公司对面部识别技术的不准确和有害应用，该公司被禁止使用该技术五年。

---

## 61. 我们并非如此特别：一本新书挑战人类独特性

**原文标题**: We’re Not So Special: A new book challenges human exceptionalism

**原文链接**: [https://democracyjournal.org/magazine/78/were-not-so-special/](https://democracyjournal.org/magazine/78/were-not-so-special/)

卡斯·R·桑斯坦评克里斯汀·韦伯《傲慢的猿猴》：该书挑战了人类例外论的观点，并认为它对科学、环境和人类生活产生了负面影响。韦伯认为，人类错误地将自己作为衡量其他物种的基准，导致对其能力和体验（环境）的理解产生偏差。她强调了科学发现，揭示了蜂鸟、大象、猫头鹰和狗等动物多样且非凡的感官和认知能力，证明了以人类为中心的测试往往低估了它们。

韦伯批评在人为的、有压力的实验室条件下研究动物，这会歪曲关于它们行为的结果。她关注动物的情感和同情心，提供了黑猩猩之间互相安慰的证据。韦伯反对“与我们相似”的方法，主张欣赏每个物种的独特品质和能力。

桑斯坦指出，韦伯的著作为保护动物福祉提供了科学和伦理论据，超越了仅仅承认它们承受痛苦的能力。她提倡一种“能力方法”，促进和保护每个物种的独特潜力。

最终，韦伯认为人类例外论不仅不科学，而且有害，导致了生态危机和对动物的虐待。她呼吁谦逊、敬畏和对世界的重新迷恋，敦促转变视角，以欣赏和尊重所有生物的内在价值和能力。她的书虽然不是政策手册，但激发了对人类与动物世界关系的根本性反思。

---

## 62. Geotoy – 3D几何体的 Shadertoy

**原文标题**: Geotoy – Shadertoy for 3D Geometry

**原文链接**: [https://3d.ameo.design/geotoy](https://3d.ameo.design/geotoy)

文章介绍了“Geotoy”，称其为“3D几何体的Shadertoy”。它似乎是一个平台或工具，允许用户创建和分享3D几何设计，类似于Shadertoy实现创建和分享着色器的方式。

内容随后列出了一系列使用Geotoy创建的项目或示例，并以作者前缀“ameo”标识。这些示例展示了各种各样的3D几何体，包括：

*   3D希尔伯特曲线
*   各种景观和地形（FBM地形，阶梯式浮岛）
*   有机形状（环面纽结，蒲公英，根，凹凸球体）
*   抽象形式（抽象沙漏）
*   具象物体（鸟浴池，混凝土四脚体，拉伸粘土碗，超椭圆多米诺骨牌，黑暗之魂树）
*   以及其他创意几何体（输电线，编织WIP，花式着色器道具）。

最后一行“作者：ameo”可能表示所有列出的示例均由同一作者“ameo”创建。总而言之，Geotoy允许创建和共享3D几何体，作者“ameo”的各种项目就证明了这一点。

---

## 63. 失窃物品的新地理学

**原文标题**: The new geography of stolen goods

**原文链接**: [https://www.economist.com/interactive/britain/2025/08/17/the-new-geography-of-stolen-goods](https://www.economist.com/interactive/britain/2025/08/17/the-new-geography-of-stolen-goods)

失窃商品的新地理：英国沦为销赃中心

文章《失窃商品的新地理》详细描述了英国如何成为失窃商品（包括汽车、手机和农业设备）的主要出口国。加密通信、薄弱的出口管制以及非洲和亚洲对商品日益增长的需求为此提供了便利，从而催生了一个被称为“全球盗窃公司”的全球犯罪企业。

英国的汽车盗窃案激增，许多汽车最终流向西非，通常经由刚果民主共和国，该国是进入更广阔非洲市场的入口。伦敦现在是欧洲的“抢手机之都”，被盗手机通常最终流向中国深圳的华强北市场，在那里它们被转售或拆解成零件。俄罗斯的制裁也导致英国农场GPS套件的盗窃案增加。

导致这一犯罪企业增长的因素有几个：宽松的出口管制、在线秘密开展业务的能力、相对于收入而言不断上涨的商品成本，以及警力不足。边境机构主要关注进口，使得出口被盗商品更容易而不被发现。

文章指出，像中国这样从贸易中受益的国家缺乏遏制它的动机，而非洲国家往往缺乏执法能力。贸易和全球化带来的收益促进了被盗商品的运输。 这突显了加强国际合作以打击这一日益增长的犯罪企业的必要性。

---

## 64. 递归的乐趣，不可变数据和纯函数：用JS制作迷宫

**原文标题**: The joy of recursion, immutable data, & pure functions: Making mazes with JS

**原文链接**: [https://jrsinclair.com/articles/2025/joy-of-immutable-data-recursion-pure-functions-javascript-mazes/](https://jrsinclair.com/articles/2025/joy-of-immutable-data-recursion-pure-functions-javascript-mazes/)

詹姆斯·辛克莱的这篇文章探讨了如何使用JavaScript构建迷宫，以阐释递归、不可变数据和纯函数的概念。它认为，虽然迷宫生成并非直接实用，但对于学习这些编码原则来说，是一个可控且有趣的挑战。

文章首先概述了在网格上手动创建迷宫的逐步过程，然后将这个手动过程转化为算法。接着，代码构建了一个不可变的数据结构，具体来说，使用记忆化和对象冻结构建了一个`Point`类，以确保对象在创建后不会被修改。文章讨论了这种方法的好处，特别是它如何允许使用`===`轻松进行比较。

之后，文章深入研究了迷宫构建算法的编码，强调了纯函数和递归。它涵盖了使用未连接房间的网格和一个随机选择的起始房间来初始化迷宫状态，包括使用自定义的伪随机数生成器来保持函数的纯净性。最后，文章为编写递归迷宫生成函数奠定了基础，强调了跟踪状态（当前房间、网格和随机数种子）以及定义清晰的退出条件的重要性，这与编写循环时的考虑因素类似。

---

## 65. 无源微波中继器

**原文标题**: Passive Microwave Repeaters

**原文链接**: [https://computer.rip/2025-08-16-passive-microwave-repeaters.html](https://computer.rip/2025-08-16-passive-microwave-repeaters.html)

本文探讨了无源微波中继器，这项技术旨在克服早期微波通信系统的局限性。与同轴电缆相比，微波无线电通过提供更大的带宽和容量，彻底改变了电信业。然而，微波信号需要直视路径，这给山区或缺乏易于到达的地形区域带来了挑战。

无源微波中继器本质上是大型平面反射器，通过重定向微波信号来解决这个问题，充当无线电波的“镜子”。这些中继器尤其有利于那些无法负担有源微波中继成本的独立电话公司和农村贝尔运营公司。

Kreitzberg 兄弟通过他们的公司 Microflect 开创了这项技术，该公司为具有挑战性地形、恶劣天气以及公用设施接入受限地区的安装建造了铝制反射器。

本文解释了无源中继器如何在两种配置下工作：以 90 度角反射信号以绕过障碍物，或者使用两个中继器以“狗腿”布置实现更直的路径。尽管它们是被动的，但这些中继器由于其大的表面积，可以提供信号增益，有效地收集和重新发射更大截面的射频能量，类似于大型天线聚焦信号。它们的大小与增益成正比。无源中继器分为远场或近场。这种创新方法使得在有源中继器不切实际的困难环境中扩展微波通信网络成为可能。

---

## 66. 土耳其一处翻新工程发现失落之城（2023年）

**原文标题**: A renovation project in Turkey led to the discovery of a lost city (2023)

**原文链接**: [https://www.atlasobscura.com/articles/derinkuyu-turkey-underground-city-strange-maps](https://www.atlasobscura.com/articles/derinkuyu-turkey-underground-city-strange-maps)

1963年，土耳其代林库尤的一个男子在翻新地下室时，意外发现了一座巨大的多层地下城市。这个被重新发现的建筑群现已成为主要的旅游景点，据信由包括赫梯人、弗里吉亚人或早期基督徒在内的多个文明建造并使用了数个世纪，最早可追溯到公元前2000年。

这座城市开凿于卡帕多西亚特有的柔软火山凝灰岩中，可容纳多达2万人，主要用作躲避敌军的避难所，也可能用作抵御恶劣天气的温度可控的住所。有证据表明，在拜占庭和阿拉伯人、蒙古人入侵以及奥斯曼帝国征服期间，这座城市被广泛使用。

代林库尤拥有精巧的设计，包括超过15,000个深入城市腹地的通风井，以及用于封锁城市的战略性滚动石。它包括起居区、储藏区、地牢、教堂，甚至还有牲畜和葡萄酒生产的空间。

当地的希腊居民称这座城市为马拉科皮亚（意为“柔软的地方”），并在20世纪初继续将其用作避难所。在希腊土耳其战争之后，他们于1923年作为人口交换的一部分离开了该地区，放弃了这座城市，直到它被重新发现。文章突出了这座城市令人印象深刻的工程设计、作为避难所的历史意义以及作为热门旅游目的地的现代作用，鼓励读者思考潜伏在自己家中的未被发现的潜力。

---

## 67. 正电子：一款全新的数据科学 IDE

**原文标题**: Positron, a New Data Science IDE

**原文链接**: [https://posit.co/blog/positron-product-announcement-aug-2025/](https://posit.co/blog/positron-product-announcement-aug-2025/)

Posit PBC 发布 Positron，下一代免费数据科学 IDE，旨在统一 Python 和 R 用户的探索和生产工作流。Positron 基于 RStudio 超过 14 年的经验，致力于为编码、数据分析和交互式输出创建提供一致的体验，支持跨语言和工具的现代科学和数据驱动工作。

主要功能包括变量和数据帧浏览器、多会话控制台、笔记本支持、Positron 助手（GenAI 客户端）、绘图面板、集成数据应用程序工作流、数据库连接面板、一键部署到 Posit Connect、解释器管理、通过 Open VSX 的广泛扩展支持以及项目文件夹模板。

Positron 构建于 Code OSS 之上，与 Visual Studio Code 相同的基础，允许通过 VSIX 扩展进行自定义，同时提供更深入的特定语言工具集成。Positron 桌面在 Windows、macOS 和 Linux 上免费提供，采用 Elastic License 2.0 许可。RStudio 将继续维护和更新，以满足专注于 R 的用户的需求。Posit 致力于让每个人都能使用高质量的数据科学工具。Posit 团队鼓励用户下载 Positron，探索快速入门指南，加入 GitHub 上的社区，并参加 posit::conf(2025) 以了解更多信息。

---

## 68. PyPI Preventing Domain Resurrection Attacks

**原文标题**: PyPI Preventing Domain Resurrection Attacks

**原文链接**: [https://blog.pypi.org/posts/2025-08-18-preventing-domain-resurrections/](https://blog.pypi.org/posts/2025-08-18-preventing-domain-resurrections/)

生成摘要时出错

---

## 69. Candle Flame Oscillations as a Clock

**原文标题**: Candle Flame Oscillations as a Clock

**原文链接**: [https://cpldcpu.com/2025/08/13/candle-flame-oscillations-as-a-clock/](https://cpldcpu.com/2025/08/13/candle-flame-oscillations-as-a-clock/)

生成摘要时出错

---

## 70. Without the futex, it's futile

**原文标题**: Without the futex, it's futile

**原文链接**: [https://h4x0r.org/futex/](https://h4x0r.org/futex/)

生成摘要时出错

---

## 71. Lazy-brush – smooth drawing with mouse or finger

**原文标题**: Lazy-brush – smooth drawing with mouse or finger

**原文链接**: [https://lazybrush.dulnan.net](https://lazybrush.dulnan.net)

生成摘要时出错

---

## 72. Senate Probe Uncovers Allegations of Widespread Abuse in ICE Custody

**原文标题**: Senate Probe Uncovers Allegations of Widespread Abuse in ICE Custody

**原文链接**: [https://www.wired.com/story/senate-probe-uncovers-widespread-abuse-in-ice-custody/](https://www.wired.com/story/senate-probe-uncovers-widespread-abuse-in-ice-custody/)

生成摘要时出错

---

## 73. Physically Based Rendering in Filament

**原文标题**: Physically Based Rendering in Filament

**原文链接**: [https://google.github.io/filament/Filament.md.html#overview](https://google.github.io/filament/Filament.md.html#overview)

生成摘要时出错

---

## 74. Critical Cache Poisoning Vulnerability in Dnsmasq

**原文标题**: Critical Cache Poisoning Vulnerability in Dnsmasq

**原文链接**: [https://lists.thekelleys.org.uk/pipermail/dnsmasq-discuss/2025q3/018288.html](https://lists.thekelleys.org.uk/pipermail/dnsmasq-discuss/2025q3/018288.html)

生成摘要时出错

---

## 75. Passengers sue Delta, United over windowless 'window seats'

**原文标题**: Passengers sue Delta, United over windowless 'window seats'

**原文链接**: [https://www.courthousenews.com/passengers-sue-delta-united-over-windowless-window-seats/](https://www.courthousenews.com/passengers-sue-delta-united-over-windowless-window-seats/)

生成摘要时出错

---

## 76. The Future of JavaScript: What Awaits Us

**原文标题**: The Future of JavaScript: What Awaits Us

**原文链接**: [https://jsdev.space/future-of-javascript/](https://jsdev.space/future-of-javascript/)

生成摘要时出错

---

## 77. Git-worktree – Manage multiple working trees

**原文标题**: Git-worktree – Manage multiple working trees

**原文链接**: [https://git-scm.com/docs/git-worktree](https://git-scm.com/docs/git-worktree)

生成摘要时出错

---

## 78. CRLite in Firefox. Fast, private and secure (pick three)

**原文标题**: CRLite in Firefox. Fast, private and secure (pick three)

**原文链接**: [https://blog.mozilla.org/en/firefox/crlite/](https://blog.mozilla.org/en/firefox/crlite/)

生成摘要时出错

---

## 79. Notion releases offline mode

**原文标题**: Notion releases offline mode

**原文链接**: [https://www.notion.com/help/guides/working-offline-in-notion-everything-you-need-to-know](https://www.notion.com/help/guides/working-offline-in-notion-everything-you-need-to-know)

生成摘要时出错

---

## 80. Show HN: Hanaco Weather – A poetic weather SNS from the OS Yamato project

**原文标题**: Show HN: Hanaco Weather – A poetic weather SNS from the OS Yamato project

**原文链接**: [https://github.com/osyamato/os-yamato](https://github.com/osyamato/os-yamato)

生成摘要时出错

---

## 81. As Alaska's salmon plummet, scientists home in on the killer

**原文标题**: As Alaska's salmon plummet, scientists home in on the killer

**原文链接**: [https://www.science.org/content/article/alaska-s-salmon-plummet-scientists-home-killer](https://www.science.org/content/article/alaska-s-salmon-plummet-scientists-home-killer)

生成摘要时出错

---

## 82. OpenMower – An open source lawn mower

**原文标题**: OpenMower – An open source lawn mower

**原文链接**: [https://github.com/ClemensElflein/OpenMower](https://github.com/ClemensElflein/OpenMower)

生成摘要时出错

---

## 83. How to Build a Medieval Castle

**原文标题**: How to Build a Medieval Castle

**原文链接**: [https://archaeology.org/issues/september-october-2025/features/how-to-build-a-medieval-castle/](https://archaeology.org/issues/september-october-2025/features/how-to-build-a-medieval-castle/)

生成摘要时出错

---

## 84. One person was able to claim 20M IPs

**原文标题**: One person was able to claim 20M IPs

**原文链接**: [https://lists.nanog.org/archives/list/nanog@lists.nanog.org/thread/MMCCEQKA4UPGGWFWEBWLYKHTYCAOQIZS/#MMCCEQKA4UPGGWFWEBWLYKHTYCAOQIZS](https://lists.nanog.org/archives/list/nanog@lists.nanog.org/thread/MMCCEQKA4UPGGWFWEBWLYKHTYCAOQIZS/#MMCCEQKA4UPGGWFWEBWLYKHTYCAOQIZS)

生成摘要时出错

---

## 85. Perfect Freehand – Draw perfect pressure-sensitive freehand lines

**原文标题**: Perfect Freehand – Draw perfect pressure-sensitive freehand lines

**原文链接**: [https://www.perfectfreehand.com/](https://www.perfectfreehand.com/)

生成摘要时出错

---

## 86. The State of Python 2025

**原文标题**: The State of Python 2025

**原文链接**: [https://blog.jetbrains.com/pycharm/2025/08/the-state-of-python-2025/](https://blog.jetbrains.com/pycharm/2025/08/the-state-of-python-2025/)

生成摘要时出错

---

## 87. Why is it so hard for startups to compete with Cadence?

**原文标题**: Why is it so hard for startups to compete with Cadence?

**原文链接**: [https://www.zach.be/p/why-is-it-so-hard-for-startups-to](https://www.zach.be/p/why-is-it-so-hard-for-startups-to)

生成摘要时出错

---

## 88. Guile bindings for Sway window manager

**原文标题**: Guile bindings for Sway window manager

**原文链接**: [https://github.com/ebeem/guile-swayer](https://github.com/ebeem/guile-swayer)

生成摘要时出错

---

## 89. Rough Numbers Between Consecutive Primes

**原文标题**: Rough Numbers Between Consecutive Primes

**原文链接**: [https://arxiv.org/abs/2508.06463](https://arxiv.org/abs/2508.06463)

生成摘要时出错

---

## 90. Netflix Revamps Tudum's CQRS Architecture with Raw Hollow In-Memory Object Store

**原文标题**: Netflix Revamps Tudum's CQRS Architecture with Raw Hollow In-Memory Object Store

**原文链接**: [https://www.infoq.com/news/2025/08/netflix-tudum-cqrs-raw-hollow/](https://www.infoq.com/news/2025/08/netflix-tudum-cqrs-raw-hollow/)

生成摘要时出错

---

## 91. "Remove mentions of XSLT from the html spec"

**原文标题**: "Remove mentions of XSLT from the html spec"

**原文链接**: [https://github.com/whatwg/html/pull/11563](https://github.com/whatwg/html/pull/11563)

生成摘要时出错

---

## 92. Attention Is the New Big-O: A Systems Design Approach to Prompt Engineering

**原文标题**: Attention Is the New Big-O: A Systems Design Approach to Prompt Engineering

**原文链接**: [https://alexchesser.medium.com/attention-is-the-new-big-o-9c68e1ae9b27](https://alexchesser.medium.com/attention-is-the-new-big-o-9c68e1ae9b27)

生成摘要时出错

---

## 93. Monoid-Augmented FIFOs, Deamortised

**原文标题**: Monoid-Augmented FIFOs, Deamortised

**原文链接**: [https://pvk.ca/Blog/2025/08/19/monoid-augmented-fifos/](https://pvk.ca/Blog/2025/08/19/monoid-augmented-fifos/)

生成摘要时出错

---

## 94. In 2006, Hitachi developed a 0.15mm-sized RFID chip

**原文标题**: In 2006, Hitachi developed a 0.15mm-sized RFID chip

**原文链接**: [https://www.hitachi.com/New/cnews/060206.html](https://www.hitachi.com/New/cnews/060206.html)

生成摘要时出错

---

## 95. Staff disquiet as Alan Turing Institute faces identity crisis

**原文标题**: Staff disquiet as Alan Turing Institute faces identity crisis

**原文链接**: [https://www.theguardian.com/technology/2025/aug/18/shut-it-down-and-start-again-staff-disquiet-as-alan-turing-institute-faces-identity-crisis](https://www.theguardian.com/technology/2025/aug/18/shut-it-down-and-start-again-staff-disquiet-as-alan-turing-institute-faces-identity-crisis)

生成摘要时出错

---

## 96. Vendors that treat single sign-on as a luxury feature

**原文标题**: Vendors that treat single sign-on as a luxury feature

**原文链接**: [https://sso.tax/](https://sso.tax/)

生成摘要时出错

---

## 97. Israeli official planned to meet decoy posing as 15-year-old in Las Vegas sting

**原文标题**: Israeli official planned to meet decoy posing as 15-year-old in Las Vegas sting

**原文链接**: [https://www.8newsnow.com/investigators/israeli-official-planned-to-meet-decoy-posing-as-15-year-old-in-las-vegas-sex-sting-police/](https://www.8newsnow.com/investigators/israeli-official-planned-to-meet-decoy-posing-as-15-year-old-in-las-vegas-sex-sting-police/)

生成摘要时出错

---

## 98. Vim Macros for Beancount

**原文标题**: Vim Macros for Beancount

**原文链接**: [https://tangled.sh/@adam.tngl.sh/vim-beancounting](https://tangled.sh/@adam.tngl.sh/vim-beancounting)

生成摘要时出错

---

## 99. Launch HN: Reality Defender (YC W22) – API for Deepfake and GenAI Detection

**原文标题**: Launch HN: Reality Defender (YC W22) – API for Deepfake and GenAI Detection

**原文链接**: [https://www.realitydefender.com/platform/api](https://www.realitydefender.com/platform/api)

生成摘要时出错

---

## 100. 9 Years of "Learning to Code" and I Still Couldn't Build a To-Do App

**原文标题**: 9 Years of "Learning to Code" and I Still Couldn't Build a To-Do App

**原文链接**: [https://offpeaklog.bearblog.dev/learning-to-code/](https://offpeaklog.bearblog.dev/learning-to-code/)

生成摘要时出错

---

