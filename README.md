# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-08-20.md)

*最后自动更新时间: 2025-08-20 17:48:16*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 2 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 3 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 4 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 5 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 6 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 7 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 8 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 9 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 10 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 11 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 12 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 13 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 14 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 15 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 16 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 17 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 18 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 19 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 20 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 21 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 22 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 23 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 24 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 25 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 26 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 27 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 28 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 29 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 30 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 31 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 32 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 33 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 34 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 35 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 36 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 37 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 38 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 39 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 40 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 41 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 42 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 43 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 44 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 45 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 46 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 47 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 48 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 49 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 50 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 51 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 52 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 53 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 54 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 55 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 56 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 57 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 58 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 59 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 60 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 61 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 62 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 63 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 64 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 65 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 66 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 67 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 68 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 69 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 70 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 71 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 72 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 73 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 74 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 75 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 76 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 77 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 78 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 79 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 80 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 81 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 82 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 83 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 84 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 85 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 86 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 87 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 88 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 89 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 90 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 91 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 92 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 93 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 94 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 95 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 96 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 97 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 98 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 99 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 100 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 101 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 102 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 103 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 104 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 105 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 106 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 107 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 108 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 109 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 110 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 111 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 112 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 113 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 114 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 115 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 116 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 117 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 118 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 119 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 120 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 121 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 122 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 123 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 124 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 125 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 126 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 127 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 128 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 129 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 130 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 131 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 132 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 133 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 134 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 135 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 136 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 137 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 138 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 139 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 140 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 141 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 142 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 143 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 144 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 145 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 146 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 147 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 148 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 149 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 150 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 151 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 152 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 153 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 154 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
