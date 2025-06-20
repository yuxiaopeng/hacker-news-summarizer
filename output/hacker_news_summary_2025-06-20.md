# Hacker News 热门文章摘要 (2025-06-20)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Phoenix.new – Phoenix 远程 AI 运行时

**原文标题**: Phoenix.new – Remote AI Runtime for Phoenix

**原文链接**: [https://fly.io/blog/phoenix-new-the-remote-ai-runtime/](https://fly.io/blog/phoenix-new-the-remote-ai-runtime/)

Phoenix 的创建者 Chris McCord 介绍了 Phoenix.new，这是一种专为 Elixir 和 Phoenix 开发量身定制的远程 AI 运行时。它旨在通过提供“开箱即用”的在线编码代理，加速实时协作应用程序的创建。

主要功能包括：

*   **临时 VM 中的 Root Shell：** Phoenix.new 在浏览器中一个隔离的虚拟机（Fly Machine）中运行，赋予代理 root 访问权限，可以安装软件包和运行程序，而不会影响用户的本地机器。
*   **Phoenix 专用代理：** 该代理专门为 Phoenix 构建，了解其实时协作特性，利用无头浏览器进行 UI 交互和测试。这使得代理能够看到真实的页面内容和 JavaScript 状态。
*   **云原生开发：** 使用 Phoenix.new 构建的应用程序从一开始就存在于云中，具有私有 URL、GitHub 集成和 Fly.io 基础设施护栏。
*   **实时交互：** Phoenix.new 可以使用真实的浏览器与 Web 应用程序进行交互，从而能够添加前端功能并直接对其进行测试。UI 包含正在开发的应用程序的实时预览。
*   **多功能应用程序构建：** 该代理可以构建具有 WebSockets、Phoenix Presence 功能和数据库的全栈应用程序。它还可以与数据库交互并生成模式。
*   **多语言支持：** 虽然针对 Phoenix 进行了优化，但该系统支持其他语言和框架，为多样化的应用程序开发开辟了可能性。

McCord 设想开发人员工作流程会发生转变，代理可以全天候执行实际工作，从而使开发人员能够专注于更高级别的任务。 Phoenix.new 已经用于处理 GitHub 问题并生成拉取请求，展示了 AI 辅助开发的潜力。

---

## 2. Show HN: Nxtscape – 一个开源的代理浏览器

**原文标题**: Show HN: Nxtscape – an open-source agentic browser

**原文链接**: [https://github.com/nxtscape/nxtscape](https://github.com/nxtscape/nxtscape)

Nxtscape 是一款基于 Chromium 的开源“智能体”浏览器，定位为注重隐私的 Arc、Brave 和 Perplexity Comet 等浏览器的替代品。它旨在将 AI 智能体直接集成到浏览器中，以提高生产力并在本地自动执行任务，而无需将数据发送给第三方。

主要功能包括：

*   **AI 智能体：** 在本地运行 AI 智能体，用于标签管理、表单填写和工作流程自动化等任务。通过 Ollama 支持本地模型。
*   **隐私：** 将浏览历史记录保存在用户的计算机上，并提供自带密钥的选项。
*   **Chrome 扩展程序兼容性：** 可与现有的 Chrome 扩展程序一起使用。
*   **开源：** 100% 开源，采用 AGPL-3.0 许可证，支持社区贡献和派生。
*   **（即将推出）MCP 商店：** 在浏览器栏中一键安装流行的 MCP (类 Manus 智能体)。
*   **（即将推出）AI 广告拦截器：** 一种通过 AI 增强的内置广告拦截器。

Nxtscape 与其他浏览器的区别在于：

*   比 Chrome 更注重 AI 驱动的自动化和隐私。
*   优先考虑 AI 功能，而不是 Brave 提供的次要功能（加密货币、VPN 等）。
*   与闭源的 Arc 相比，它是开源的。
*   避免数据收集和广告定向，这与 Perplexity Comet 不同。

该项目鼓励通过 Discord、Twitter 和公开路线图进行社区参与。

---

## 3. 宫崎骏《风之谷》中战争环境代价的可视化

**原文标题**: Visualizing environmental costs of war in Hayao Miyazaki's Nausicaä

**原文链接**: [https://jgeekstudies.org/2025/06/20/wilted-lands-and-wounded-worlds-visualizing-environmental-costs-of-war-in-hayao-miyazakis-nausicaa-of-the-valley-of-the-wind/](https://jgeekstudies.org/2025/06/20/wilted-lands-and-wounded-worlds-visualizing-environmental-costs-of-war-in-hayao-miyazakis-nausicaa-of-the-valley-of-the-wind/)

奥黛丽·阿吉雷的论文《在宫崎骏的<风之谷>中具象化战争的环境代价》探讨了影片的视觉叙事如何强化其反战和生态信息。虽然之前的研究主要集中在叙事的生态主题和反战信息上，但阿吉雷的作品考察了*场面调度*，特别是色彩、光线和肢体语言，在传达战争对环境和人类的后果方面的作用。

该论文认为，这些视觉元素不仅仅是美学选择，更是强调影片反战信息并将其根植于现实世界关切的关键。通过反映现实生活中的战争技术，影片鼓励观众反思战争对环境和人类的代价，并激励他们为建设一个更加和平和具有环境意识的世界而努力。

作者提到了影片中的反乌托邦背景、陶器大战、毒林及其居民，例如王虫和巨神兵。文献综述强调了现有的关于<风之谷>的学术研究，重点关注影片的精神层面以及娜乌西卡在恢复人类与自然平衡中的作用，同时指出在关于影片中战争间接影响的信息方面的研究存在空白。该论文强调了环境保护的重要性，并承认战争在环境恶化中的作用，并以科威特油井被焚烧为例。最后，它论证了选择动画、宫崎骏和<风之谷>作为研究对象的合理性，指出动画独特的视觉能力、宫崎骏对生态失衡和战争的一贯主题，以及<风之谷>对这两个主题的独特融合。

---

## 4. 克拉科夫矩阵：矩阵的扭曲双生子

**原文标题**: Cracovians: The Twisted Twins of Matrices

**原文链接**: [https://marcinciura.wordpress.com/2025/06/20/cracovians-the-twisted-twins-of-matrices/](https://marcinciura.wordpress.com/2025/06/20/cracovians-the-twisted-twins-of-matrices/)

本文介绍了克拉科维安，一种由波兰天文学家塔德乌什·巴纳赫维奇开发的计算对象，作为线性代数中矩阵的替代方案。克拉科维安是矩形数字表，其加法和标量乘法定义与矩阵相同。关键区别在于乘法规则：将左克拉科维安的第 i 列的元素与右克拉科维安的第 j 列的元素相乘的结果，是结果的第 i 列和第 j 行中的一项。

文章强调克拉科维安乘法不满足交换律或结合律，并演示了如何使用克拉科维安通过类似于乔列斯基分解的分解来求解线性方程组。巴纳赫维奇还将克拉科维安应用于最小二乘法、四元数以及天文、大地测量和球面三角学的各种问题。

尽管克拉科维安具有历史意义以及巴纳赫维奇的热情，但文章指出，在现代计算中，克拉科维安乘法并不比矩阵乘法更快。文章最后比较了 NumPy 矩阵乘法与相当于克拉科维安乘法的转置矩阵乘法。Python 代码说明了性能相似，展示了 NumPy 的内存管理如何影响性能。结论是，虽然从历史和理论的角度来看，克拉科维安有趣且优雅，但在现代计算中，它在性能方面并没有比矩阵提供任何实际优势。

---

## 5. 奥克洛：地球上二十亿年前唯一的已知天然核反应堆 (2018)

**原文标题**: Oklo, the Earth's Two-billion-year-old only Known Natural Nuclear Reactor (2018)

**原文链接**: [https://www.iaea.org/newscenter/news/meet-oklo-the-earths-two-billion-year-old-only-known-natural-nuclear-reactor](https://www.iaea.org/newscenter/news/meet-oklo-the-earths-two-billion-year-old-only-known-natural-nuclear-reactor)

国际原子能机构的这篇文章探讨了在非洲加蓬发现的奥克洛天然核反应堆遗址，该遗址可追溯到二十亿年前。 1972年，物理学家弗朗西斯·佩兰发现，奥克洛的铀矿石中铀-235（U-235）的比例低于天然铀的预期。进一步调查显示，该矿石已经历了天然核裂变。

要发生这种情况，奥克洛的铀矿沉积物当时必须具有临界质量的U-235。至关重要的是，水起到了慢化剂的作用，减缓了中子的速度，从而实现了可控的链式反应，类似于人造轻水核反应堆。加蓬特定的地质条件，包括高铀浓度和大而厚的矿床，也发挥了至关重要的作用。

奥克洛的样品将在维也纳自然历史博物馆展出，以向公众普及天然放射性的知识。博物馆旨在强调放射性是一种天然现象，以低而不危险的水平存在于我们的环境中。文章还提到了奥克洛岩石样本的捐赠、它们的辐射水平以及国际原子能机构关于铀生产的相关资源。 它强调了数十亿年前使奥克洛反应堆能够运行并保存至今的独特因素组合。

---

## 6. 把梯子收起来，不留后路

**原文标题**: Rolling the ladder up behind us

**原文链接**: [https://xeiaso.net/blog/2025/rolling-ladder-behind-us/](https://xeiaso.net/blog/2025/rolling-ladder-behind-us/)

Cadey 的文章《用完即弃的阶梯》批判了科技行业对资深工程师的过度依赖，忽视对初级人才的培养和训练，从而造成潜在的不可持续的未来。生成式人工智能工具越来越多地被采用，取代了人类的专业技能，这加剧了这种情况，与历史上卢德分子反抗动力织布机的趋势相似。

Cadey 认为，虽然像 Devin 和 vibe 编码平台这样的人工智能工具提供了短期的生产力提升和改进的用户体验，但它们威胁到真正的编程技能，并导致对需要不断更换的“劣质软件”的依赖。他们担心，在人工智能的承诺驱动下，所有者阶层的不切实际的期望将进一步加剧这个问题。

这篇文章还提出了关于这些人工智能工具使用的模型上下文协议（MCP）服务器的安全性问题，强调了由于其对敏感数据和系统资源的无限制访问，它们可能被用于恶意活动。

最终，Cadey 倡导技术进步和手艺传承之间的平衡，强调计算机素养教育的重要性，并培养一种重视高质量、精心制作的软件而非廉价生产、大规模生产的替代品的文化。他们担心技能和专业知识的丧失，并将此与传统纺织技术的衰落相提并论。

---

## 7. 以 Python 为先的数据湖仓

**原文标题**: A Python-first data lakehouse

**原文链接**: [https://www.bauplanlabs.com/blog/everything-as-python](https://www.bauplanlabs.com/blog/everything-as-python)

本文探讨了将通常在Jupyter Notebook中开发的数据科学原型部署到生产环境所面临的挑战。它强调了两种常见陷阱：直接将脆弱的Notebook发布到生产环境，或者依赖于缓慢且昂贵的向DevOps团队的移交。

提出的解决方案围绕“Python优先的数据湖仓”方法展开，利用两个关键工具：**marimo** 和 **bauplan**。Marimo是一个现代化的Notebook环境，通过将Notebook存储为Python脚本，解决了传统Jupyter Notebook的可重复性和可维护性问题。Bauplan是一个为S3上的Pythonic工作流设计的云数据平台，提供内置的数据版本控制、声明式环境和无服务器函数执行。

核心思想是这两个工具都以代码优先和Python为中心，从而实现无缝的可组合性。在marimo中开发的原型代码可以直接在Bauplan管道中重用，而无需重构。本文通过分析纽约市出租车数据集的实际例子来演示这一点，展示了如何在marimo Notebook中定义的函数可以通过简单的装饰器集成到Bauplan管道中。

Bauplan通过抽象出复杂的底层架构问题（如存储格式、环境和编排器）来简化生产部署。它还集成了数据版本控制，从而实现安全的实验和协作工作流程。通过消除移交和重写，marimo和Bauplan的结合为数据科学项目提供了一条从原型到生产的更顺畅、更高效的途径。本文鼓励读者尝试这些工具并为它们的发展做出贡献。

---

## 8. 程序设计方法（第二版）（2024）

**原文标题**: How to Design Programs 2nd Ed (2024)

**原文链接**: [https://htdp.org](https://htdp.org)

文章《如何设计程序（第二版，2024）》宣布了教科书《如何设计程序》第二版的发布。核心信息是这本流行书籍的更新版本现已面世。文章还指出，第一版仍然可以访问。

内容要点：

*   **新版发布：** 《如何设计程序》第二版（2024）现已发布。
*   **第一版可用性：** 第一版仍然可以访问，暗示它可能对某些人仍然有用或有意义。

主要信息是新版的发布，建议读者可以探索其更新的内容和方法，同时保留访问原始材料的选项。

---

## 9. Klong：一种简单的数组语言

**原文标题**: Klong: A Simple Array Language

**原文链接**: [https://t3x.org/klong/](https://t3x.org/klong/)

Klong是一种简单的数组语言，灵感来自K，但旨在减少歧义。它允许使用预定义运算符来操作列表和多维数组。该网站提供了学习和使用Klong的资源，包括参考手册、数组编程入门书籍、快速参考以及面向数组语言新手的简短介绍。还有一份文档概述了Klong和K之间的差异。

用户可以下载Klong（ANSI C 源代码），并使用C编译器进行编译。安装包括复制`kg`二进制文件并设置`KLONGPATH`环境变量。 Klong程序存储在`.kg`文件中，可以使用`]lname`或`./kg -l name`等命令加载。

对于性能关键型应用，Brian Gurraci开发了一个名为KlongPy的Klong向量化版本，可在GitHub上找到。该网站还链接到Klong的先前稳定版本。 总体而言，重点在于数学符号和数组操作，而不是传统的编程范式。

---

## 10. Hurl：用纯文本运行和测试 HTTP 请求

**原文标题**: Hurl: Run and test HTTP requests with plain text

**原文链接**: [https://github.com/Orange-OpenSource/hurl](https://github.com/Orange-OpenSource/hurl)

Hurl 是一个命令行工具，它以简单的纯文本格式运行 HTTP 请求，从而能够获取数据并测试 HTTP 会话。它支持链式请求、捕获值以及使用 XPath、JSONPath 和其他谓词对标头和正文响应进行查询评估。 Hurl 用途广泛，适用于 HTML、REST、SOAP、GraphQL 和其他 XML/JSON API。

Hurl 作为测试工具表现出色，允许对状态代码、响应标头和正文内容进行断言。它支持使用 `newUuid` 和 `newDate` 等函数生成动态数据。

主要功能包括：
*   **文本格式:** 易于阅读和编写
*   **快速 CLI:** 适用于本地开发和 CI/CD 集成
*   **单一二进制文件:** 安装简单，无需运行时依赖
*   **基于 curl:** 利用强大的 libcurl 库

Hurl 支持各种请求类型（GET、POST 等）、身份验证方法（BasicAuth）和数据格式（HTML 表单、multipart 表单、JSON、XML）。它可以处理动态数据、模板和文件上传。报告可以生成为 HTML、JSON、JUnit 或 TAP 格式。它还支持 HTTP 版本和 IP 地址检查。

安装方法包括适用于各种操作系统的二进制文件、Cargo、conda-forge、Docker 和 npm。用户可以从源代码构建。 Hurl 鼓励用户通过 GitHub 提供反馈。

---

## 11. 机器人简史：不完整、且多半是错的

**原文标题**: A Brief, Incomplete, and Mostly Wrong History of Robotics

**原文链接**: [https://generalrobots.substack.com/p/a-brief-incomplete-and-mostly-wrong](https://generalrobots.substack.com/p/a-brief-incomplete-and-mostly-wrong)

通用机器人Substack上的文章《机器人简史：不完整、不准确，且基本错误》以幽默自嘲的口吻，着重介绍了机器人概念和现实演变过程中的关键时刻。文章认为，定义“机器人”本质上具有挑战性，因为这个概念在整个历史中不断变化和演变。

作者将人工人类/自动机的*概念*追溯到古代神话和传说（如塔罗斯）。然后，他们简要地提到了文艺复兴时期和工业革命时期的机械自动机，强调这些不是现代意义上的机器人，而是朝着机械化模仿生命迈出的重要一步。

文章强调，*“机器人”这个词*起源于卡雷尔·恰佩克的戏剧《R.U.R.》，以及其中对为剥削而设计的人工工人的描述。然后，作者跳跃到20世纪的几个重要节点，例如尤尼梅特（Unimation）公司早期工业机器人的开发，以及人工智能作为一个独立领域的出现。

这篇文章戏谑地嘲笑了对机器人发展过于简单的描述，承认了自身的不完整性，并暗示许多关于机器人历史的广泛认知都是不准确的。最终，作者强调，机器人技术史是复杂、多方面的，并且不断被改写，这使得任何明确的历史都是不可能的（也许是不受欢迎的）目标。他们认为，更有效的方法是分析驱动机器人发展的*思想*和*动机*，而不是拘泥于严格的时间顺序。

---

## 12. Rust 编写的极简自动微分引擎 (用于教学)

**原文标题**: Minimal auto-differentiation engine in Rust (for educational purposes)

**原文链接**: [https://github.com/e3ntity/nanograd](https://github.com/e3ntity/nanograd)

Nanograd：一个用 Rust 编写的极简自动微分引擎，专为教学目的而设计。它允许用户自动计算复杂函数的导数。其核心概念围绕 `Scalar` 类型展开，该类型存储一个值、其梯度（可选）以及表示生成它的运算的 `Edge`。

该引擎构建一个由 `Scalar` 对象组成的有向无环图 (DAG)。`scalar::func` 模块中的运算符重载和辅助函数使用户能够构建此图，同时自动缓存每个运算（边）的局部导数。

`backward()` 方法是引擎的主力。从一个输出 `Scalar` 开始，它递归地遍历该图，将梯度向后传播到输入节点。这些梯度累积在叶子节点中，叶子节点使用 `Scalar::new_grad` 创建。

使用示例展示了如何定义带有梯度的 `Scalar` 变量、执行运算，然后使用 `backward()` 计算和检索关于初始变量的导数。

最后，文章提到了一个通过 `plot::dump_graph` 实现的可视化工具，该工具输出一个使用 D3.js 渲染的自包含 HTML 文件，允许用户可视化计算图。所包含的演示训练了一个小型多层感知器来解决 XOR 函数，并可视化了单个感知器的计算图。

---

## 13. Ink & Switch 的 BeeKEM 协议深度解析

**原文标题**: A deep-dive explainer on Ink and Switch's BeeKEM protocol

**原文链接**: [https://meri.garden/a-deep-dive-explainer-on-beekem-protocol/](https://meri.garden/a-deep-dive-explainer-on-beekem-protocol/)

本文深入探讨了 Ink & Switch 的 BeeKEM 协议，这是一种密钥封装机制，专为使用 CRDT 的保护隐私的、本地优先的协作应用程序而设计。它将 BeeKEM 与传统的安全群组消息传递方法（如 Signal 的双棘轮机制和 MLS 的 TreeKEM）进行了对比，突出了其在处理并发和网络分区方面的优势。

本文解释了由于成对加密的 n^2 复杂度，安全群组消息传递通常涉及复杂的密钥管理。TreeKEM 通过使用左平衡二叉树来有效地管理每个 epoch 的群组密钥，从而对此进行了改进，但它假设状态更新的完全顺序，使其对网络分区的容忍度较低。

与 TreeKEM 不同，BeeKEM 接受 CRDT 的固有并发性，并避免需要中央授权机构来仲裁操作成功。当发生并发更新时，冲突通过对并发添加的叶子进行排序并将其路径留空来解决。它可以处理多个成员同时添加到同一树索引的情况，并在其因果关系上下文中解决冲突。这通过 PCS 更新来实现，成员甚至可以在离线时更新他们的密钥，并且当发生冲突时，每个人都会保留多个密钥，直到新的更新覆盖这些节点。这允许持续解密消息，即使存在冲突节点。本质上，BeeKEM 将群组状态建模为一个 DAG，其中每个操作的有效性由更新者已知的先前树状态决定。

---

## 14. 大学棒球、风险投资与漫长的可能

**原文标题**: College baseball, venture capital, and the long maybe

**原文链接**: [https://bcantrill.dtrace.org/2025/06/15/college-baseball-venture-capital-and-the-long-maybe/](https://bcantrill.dtrace.org/2025/06/15/college-baseball-venture-capital-and-the-long-maybe/)

这篇文章将大学棒球运动员（尤其是在盈利性体育项目中）的经历与创业者筹集风险投资的经历进行了对比。作者既是一位大学棒球运动员的父亲，也是一位筹集过风险投资的人，他认为这两者之间存在着惊人的相似之处。

文章重点介绍了大学运动员复杂而动荡的招募过程，尤其是在NIL（姓名、形象和肖像权）资金和转会门户出现之后。它将此与人们对大学体育传统运作方式的天真看法进行了对比。同样，它将筹集风险投资描述为一场情绪上的过山车。

作者探讨了具体的相似之处，使用风险投资术语来说明大学棒球的体验：

*   **路演材料（Pitch Deck）：** 运动员的集锦（视频和数据）反映了创业公司向投资者做的演示。
*   **漫长的可能（The Long Maybe）：** 教练敷衍运动员而不做出明确承诺，就像风险投资家“保留选择权”而没有真正的投资意向一样。
*   **条款清单（The Term Sheet）：** 棒球邀请，即使有球队名额，也可能像风险投资条款清单一样不具有约束力。
*   **抢先投资（The Preempt）：** 对高中球员的早期、不具约束力的承诺是冒险的，类似于风险投资公司抢先投资一轮融资然后退出。
*   **限时要约（The Exploding Offer）：** 在这两种情况下，限时要约都很常见。
*   **多个条款清单（Multiple Term Sheets）：** 拥有多个邀请对于初创公司和球员来说都是理想的，但很少见。
*   **估值倒挂（The Valuation Overhang）：** 过早地承诺加入顶级项目可能是有害的，类似于创业公司以过高的估值筹集过多的资金。
*   **降价融资（The Down Round）：** 进入转会门户去较低级别的学校就像一家创业公司进行降价融资。
*   **首次公开募股（The IPO）：** 在美国职业棒球大联盟打球就像一家创业公司的首次公开募股梦想。

最终，作者建议企业家和运动员都要明确自己的目标，并做出符合这些目标的决定，强调去真正需要他们的地方的重要性。

---

## 15. Meta 宣布 Oakley 智能眼镜

**原文标题**: Meta announces Oakley smart glasses

**原文链接**: [https://www.theverge.com/news/690133/meta-oakley-hstn-ai-glasses-price-date](https://www.theverge.com/news/690133/meta-oakley-hstn-ai-glasses-price-date)

Meta与Oakley合作推出Oakley Meta HSTN智能眼镜，起价399美元。限量版HSTN型号售价499美元，7月11日起接受预订。这款眼镜与现有的Meta Ray-Bans类似，配备前置摄像头（升级至3K视频）、开放式扬声器和麦克风，用户可以听音乐、拨打电话并与Meta AI互动。Meta AI还可以回答用户周围环境的问题并翻译语言。

Oakley型号专为运动员设计，拥有IPX4级防水性能和长达8小时的电池续航时间，充电盒可提供高达48小时的电量。这款眼镜将提供五种Oakley镜框和镜片组合，并可配处方镜片。

此次合作标志着Meta向可穿戴设备的“性能类别”扩张。Meta此前与EssilorLuxottica（Ray-Ban和Oakley的母公司）在Meta Ray-Bans上的合作取得了成功，已售出超过200万副，EssilorLuxottica的目标是到2026年每年与Meta销售1000万副智能眼镜。这款眼镜将在美国、加拿大、欧洲部分地区以及澳大利亚发售。

---

## 16. 展示一下：我用 Elixir 写了一个新的 BitTorrent Tracker

**原文标题**: Show HN: I wrote a new BitTorrent tracker in Elixir

**原文链接**: [https://github.com/Dahrkael/ExTracker](https://github.com/Dahrkael/ExTracker)

这个“Show HN”帖子介绍了ExTracker，一个用Elixir编写的全新BitTorrent Tracker。虽然仍在开发中，但它拥有高性能，通过利用所有可用核心和采用内存存储来实现低内存使用率（大约每1,000,000个对等节点200MB）。它提供零设置，并支持HTTPS、数据库备份和各种BitTorrent增强提案（BEP），包括BEP 0、15、23、7、24、41和52。

该Tracker目前运行在extracker.dahrkael.net:6969的测试实例上。作者指出，诸如私有种子支持（BEP 27）、部分种子（BEP 21）、Tracker故障重试（BEP 31）、scrape支持（BEP 48）、infohash白名单/黑名单、对等节点管理、指标和GeoIP支持等功能，要么已部分实现，要么正在计划中。不计划支持WebTorrent和对等节点混淆（BEP 8）。

ExTracker可以直接从源代码运行，可以使用预构建版本，也可以通过Docker运行。在使用Docker时，可以使用runtime.exs文件或环境变量自定义配置。该项目采用Apache License 2.0许可证。作者欢迎功能请求和贡献。

---

## 17. 星形海燕：一个兼容 Linux 的全新内核项目

**原文标题**: Asterinas: A new Linux-compatible kernel project

**原文链接**: [https://lwn.net/SubscriberLink/1022920/ad60263cd13c8a13/](https://lwn.net/SubscriberLink/1022920/ad60263cd13c8a13/)

LWN.net 文章介绍 Asterinas：一个用 Rust 编写的、Linux-ABI 兼容的新内核项目。Asterinas 旨在通过“框架内核架构”结合单内核和微内核设计的优点。这种架构将不安全的 Rust 代码封装在核心库中，允许内核的其余部分使用安全的抽象进行开发，同时保持共享内存的性能。

“框架内核”概念旨在最大限度地减少可信计算基 (TCB)，类似于微内核，以促进形式化验证。Asterinas 正在与 CertiK 合作，使用 Verus 对内核进行形式化验证。

该项目还包括 OSTD（一个 Rust 操作系统框架）和 OSDK（一个用于内核开发的 Cargo 插件）。OSTD 的目标是降低操作系统开发的入门门槛、增强内存安全、促进代码重用，并通过用户模式测试提高生产力。

目前支持 x86 和 RISC-V 的 Asterinas 已经实现了 206 个 Linux 系统调用，并计划扩展架构和硬件支持，重点关注云可用性和英特尔的 Trust Domain Extensions (TDX)。该项目旨在为中国云市场 (阿里云) 创建一个具有经过形式化验证的 TCB 的容器宿主操作系统。与专注于在现有 Linux 内核中使用安全 Rust 驱动程序的 Rust for Linux 不同，Asterinas 正在从头开始构建一个新内核，将不安全的代码限制在最低限度，并致力于进行形式化验证。

该文章还讨论了 Asterinas 与微软 Singularity OS 之间的相似之处。

---

## 18. HCP Vault Secrets 生命周期结束

**原文标题**: HCP Vault Secrets End of Life

**原文链接**: [https://support.hashicorp.com/hc/en-us/articles/41802449287955-HCP-Vault-Secrets-End-Of-Life](https://support.hashicorp.com/hc/en-us/articles/41802449287955-HCP-Vault-Secrets-End-Of-Life)

HashiCorp 将停止使用 HCP Vault Secrets，并将重点转移到基于 HCP Vault Secrets 经验教训改进 HCP Vault Dedicated。

**要点：**

*   **停止销售：** 2025 年 6 月 30 日。 新客户将无法访问，但现有客户在此之前可以添加新应用程序。
*   **停止服务（按需付费）：** 2025 年 8 月 27 日。 所有按需付费客户的 HCP Vault Secrets 应用程序将被删除，并且支持将停止。
*   **影响：** 此公告目前不影响拥有 Flex 合约的客户。
*   **替代方案：** 鼓励用户迁移到 HCP Vault Dedicated 或使用 Vault Community Edition。
*   **迁移资源：** 提供迁移指南以帮助用户过渡。
*   **支持：** 如有问题，请联系 hvs-help@hashicorp.com。

---

## 19. CRuby 中内存管理的重构 [pdf]

**原文标题**: Reworking Memory Management in CRuby [pdf]

**原文链接**: [https://blog.peterzhu.ca/assets/ismm_2025.pdf](https://blog.peterzhu.ca/assets/ismm_2025.pdf)

基于标题“CRuby中内存管理的重构”以及文本中揭示的PDF结构，这篇文章可能讨论了对Ruby编程语言的CRuby实现中内存管理所做的改进或更改。

PDF结构表明这是一份技术文档，可能是一篇论文或演示文稿。交叉引用(xref)、对象定义、字体和元数据的存在表明这是一个具有内部链接和引用的结构化文档。

关于“重构”方面的论文具体内容在这个截断的PDF表示中不可见。但是，考虑到标题，它可能深入探讨：

*   **CRuby中现有的内存管理问题：** 识别问题，例如碎片、垃圾回收开销或内存泄漏。
*   **提出的解决方案：** 详细介绍为解决已识别问题而实现的新算法、数据结构或技术。
*   **实施细节：** 描述如何将更改集成到CRuby代码库中。
*   **性能评估：** 呈现基准测试、测试和比较，以证明重构后的内存管理的有效性，包括内存使用情况、垃圾回收时间和整体应用程序性能。
*   **潜在影响：** 讨论与更改相关的任何权衡或副作用。

总之，这篇文章旨在提出一种或一组解决方案来优化CRuby中的内存管理，涵盖问题定义、提出的解决方案、实施方面和性能评估。

---

## 20. 曼哈顿拥堵费注定成功

**原文标题**: Congestion pricing in Manhattan is a predictable success

**原文链接**: [https://www.economist.com/united-states/2025/06/19/congestion-pricing-in-manhattan-is-a-predictable-success](https://www.economist.com/united-states/2025/06/19/congestion-pricing-in-manhattan-is-a-predictable-success)

《经济学人》的这篇文章讨论了曼哈顿拥堵费的成功实施。最初受到强烈反对的进城9美元收费，出人意料地获得了纽约人的支持，比如言语治疗师莫拉·瑞安，她最初对此感到害怕。她发现自己的通勤时间大大缩短了，有时甚至缩短了45分钟。文章强调，民意调查现在显示，支持这项收费的纽约人多于反对者，表明在体验到交通拥堵减少的好处后，公众的看法发生了积极转变。文章还指出，这项政策变化来得很慢。文章总结认为，曼哈顿的拥堵费是一项成功的举措。

---

## 21. Show HN: Ts-SSH – 通过 Tailscale 实现 SSH，无需运行守护进程

**原文标题**: Show HN: Ts-SSH – SSH over Tailscale without running the daemon

**原文链接**: [https://github.com/derekg/ts-ssh](https://github.com/derekg/ts-ssh)

Ts-SSH是一个命令行工具，无需完整的Tailscale守护进程即可通过Tailscale启用SSH和SCP，非常适合需要快速可靠地访问其Tailscale基础设施的DevOps团队。它使用`tsnet`进行用户空间的Tailscale连接。

主要功能包括核心SSH/SCP功能，支持各种身份验证方法（SSH密钥、密码）和安全主机密钥验证。它还提供强大的多主机操作，如列出主机、并行或顺序执行命令、将文件复制到多个主机，以及创建真实的`tmux`会话以进行多主机管理。

Ts-SSH提供跨平台兼容性（Linux、macOS、Windows）、多语言支持（英语、西班牙语）、快速启动以及用于脚本编写和自动化的可组合命令。

安装涉及使用`go install`或从源代码手动构建。用法示例涵盖主机发现、基本SSH操作、多主机操作和文件传输。它支持`ProxyCommand`集成。

首次运行时，您需要通过该工具提供的URL使用Tailscale进行身份验证。通过针对`~/.ssh/known_hosts`进行主机密钥验证来增强安全性，并提供一个危险的`-insecure`标志来完全禁用它。该项目采用MIT许可证。

---

## 22. ELIZA 重生：恢复所有聊天机器人的鼻祖

**原文标题**: ELIZA Reanimated: Restoring the Mother of All Chatbots

**原文链接**: [https://www.computer.org/csdl/magazine/an/2025/02/11030922/27sQDLuL7Uc](https://www.computer.org/csdl/magazine/an/2025/02/11030922/27sQDLuL7Uc)

IEEE计算机学会CSDL上的文章《ELIZA 重生：修复所有聊天机器人的鼻祖》可能探讨了保护、分析，以及潜在地重新实现或现代化ELIZA这一奠基性聊天机器人的工作。ELIZA由Joseph Weizenbaum在20世纪60年代创建，被认为是自然语言处理领域的一个里程碑式成就，也是现代聊天机器人的先驱。

该文章可能深入探讨了ELIZA的历史意义，解释了其使用模式匹配和关键词识别来模拟对话的简单但有影响的方法。它很可能描述了ELIZA如何基于识别用户输入中的特定单词或短语，并将其重新组织成问题或陈述来生成回复，从而创造出理解的错觉。

“重生”这个方面表明该文章侧重于重振ELIZA的努力。这可能涉及恢复原始代码、分析其设计原则、用现代编程语言重新创建它，或将其用作评估当代人工智能技术的基准。它也可能探讨从ELIZA的局限性和成功中吸取的教训，为当前的聊天机器人开发提供有价值的见解。

最终，该文章可能旨在突出ELIZA的持久遗产及其在人工智能领域的持续相关性，强调理解其历史背景和设计对于为聊天机器人技术的未来发展提供信息的重要性。CSDL的背景表明了一种学术方法，可能包括技术细节和与现代系统的比较。

---

## 23. 米尔勒·拉德曼·尤凯莱斯，一位70年代的艺术家，成为了“垃圾工”的英雄

**原文标题**: Mierle Laderman Ukeles, a '70s artist who became a hero to 'garbage men'

**原文链接**: [https://www.nytimes.com/2025/06/14/nyregion/maintenance-artist-mierle-laderman-ukeles.html](https://www.nytimes.com/2025/06/14/nyregion/maintenance-artist-mierle-laderman-ukeles.html)

无法访问文章链接。

---

## 24. 将大型语言模型编译成巨内核：一种实现低延迟推理的途径

**原文标题**: Compiling LLMs into a MegaKernel: A path to low-latency inference

**原文链接**: [https://zhihaojia.medium.com/compiling-llms-into-a-megakernel-a-path-to-low-latency-inference-cf7840913c17](https://zhihaojia.medium.com/compiling-llms-into-a-megakernel-a-path-to-low-latency-inference-cf7840913c17)

本文介绍Mirage Persistent Kernel (MPK)，一种将LLM推理转换为单个融合的GPU“巨内核”的编译器，从而显著降低延迟。传统的LLM系统由于跨多个内核的分散操作，存在内核启动开销和低效的资源利用率。MPK通过将整个推理流水线编译成一个连续的内核来解决这个问题，从而消除启动开销，实现软件流水线，并重叠GPU间的计算和通信。

MPK将LLM的计算图编译成细粒度的任务图，以捕获亚内核级别的依赖关系，从而进行积极的流水线处理。然后，MPK运行时在单个GPU巨内核中完全执行此任务图。它将GPU流式多处理器(SM)划分为工作器(执行任务)和调度器(管理任务执行)，使用事件驱动的执行模型。这允许细粒度的控制和任务之间最小的开销。

本文强调，与现有系统相比，MPK实现了1.2-6.7倍的延迟降低，尤其是在多GPU部署中表现出色。它声称易于使用，只需几十行Python代码即可编译LLM。未来的开发重点是支持更新的GPU架构，如NVIDIA Blackwell，处理动态工作负载(MoE模型)，以及实现高级调度策略。该项目鼓励社区协作，并提供指向其GitHub存储库的链接。

---

## 25. Qfex (YC X25) – 24/7 股票交易所后端工程师

**原文标题**: Qfex (YC X25) – Back End Engineer for a 24/7 Stock Exchange

**原文链接**: [https://www.ycombinator.com/companies/qfex/jobs/S7XSybx-founding-backend-engineer](https://www.ycombinator.com/companies/qfex/jobs/S7XSybx-founding-backend-engineer)

QFEX (YC X25) 正在寻找一位创始后端工程师，加入其位于伦敦的团队，共同构建一个 24/7 全球股票交易所。该职位涉及设计并负责处理每日数十亿交易量的系统。

工程师将通过设计容错、低延迟的服务并优化系统性能，专注于可靠性和性能。他们还将负责通过设置 CI/CD、IaC、监控和随叫随到流程来提升开发者体验。此外，该职位还涉及技术指导，参与架构决策和制定编码标准，并为公司文化和招聘做出贡献。

理想的候选人拥有来自顶尖大学的 STEM 学位，3 年以上使用 C 或 C++ 等高性能语言构建高流量或实时生产系统的经验，并致力于测试、指标和优雅降级。需要具备英国工作许可并在伦敦现场工作。拥有金融科技/交易所经验、Rust 知识、Kubernetes/IaC 专业知识以及网络安全/合规知识是加分项。

QFEX 提供 5 万英镑至 15 万英镑的年薪和 0.25% 至 0.75% 的股权，午餐补贴，定期公司活动，25 天假期 + 银行假日以及一个全新的办公室。面试流程包括创始人电话面试、居家挑战和现场深入考察。QFEX 旨在通过提供无经纪商市场准入和跨各种资产类别的超高效永续期货，颠覆价值 1000 亿美元的交易所和清算行业。

---

## 26. Show HN: SnapQL – 使用 AI 查询 Postgres 的桌面应用

**原文标题**: Show HN: SnapQL – Desktop app to query Postgres with AI

**原文链接**: [https://github.com/NickTikhonov/snap-ql](https://github.com/NickTikhonov/snap-ql)

SnapQL：一款利用AI探索和查询PostgreSQL数据库的桌面应用。主要功能包括利用AI快速生成模式感知的查询语句，支持任何PostgreSQL数据库，并作为本地桌面应用运行，确保用户数据库凭据保留在他们的计算机上。用户需要提供自己的OpenAI API密钥。目前，尚未提供预编译的二进制文件；因此，提供了构建本地副本的说明：克隆仓库，运行`npm install`，安装Xcode（仅限MacOS），然后根据用户操作系统执行`npm run build:mac`或`npm run build:win`，最后从`./dist`目录安装生成的二进制文件。

---

## 27. 美国宇航局科学家发现地球氧气与磁场之间的联系

**原文标题**: NASA Scientists Find Ties Between Earth's Oxygen and Magnetic Field

**原文链接**: [https://science.nasa.gov/earth/earth-oxygen-magnetic-field-linked/](https://science.nasa.gov/earth/earth-oxygen-magnetic-field-linked/)

一项新的 NASA 研究揭示了过去 5.4 亿年间地球磁场强度与大气氧含量之间可能存在的联系。研究人员发现，源自地球熔融内部的磁场强度波动与寒武纪大爆发以来大气中氧气的升降之间存在相关性。这表明地球深层过程可能影响地球表面的宜居性。

该研究分析了已有的地球磁场数据集（记录在磁化矿物中）和历史氧含量数据（从古代岩石中推断得出）。作者强调，这是首次对这些记录进行详细比较。观察到的相关性表明，磁场和氧含量可能都在对单一潜在过程做出反应，例如大陆的移动。

科学家推测，磁场可能保护大气层免受太阳风的侵蚀，但确切的因果关系仍在调查中。计划开展进一步的研究，以检查更长的数据集，调查其他必需化学物质（如氮）的丰度，并进一步确定将地球深处与地球表面生命联系起来的具体原因。这些发现为生命的演化及其与行星过程的联系提供了潜在的见解。

---

## 28. 正确的化学反应：简·哈露如何成为“白金发女郎”（2020）

**原文标题**: The Right Chemistry: How Jean Harlow became a ‘platinum blond’ (2020)

**原文链接**: [https://montrealgazette.com/opinion/columnists/article249177.html](https://montrealgazette.com/opinion/columnists/article249177.html)

无法访问文章链接。

---

## 29. 巨型全视望远镜将革新天文学。

**原文标题**: Giant, all-seeing telescope is set to revolutionize astronomy

**原文链接**: [https://www.science.org/content/article/giant-all-seeing-telescope-set-revolutionize-astronomy](https://www.science.org/content/article/giant-all-seeing-telescope-set-revolutionize-astronomy)

好的，我已阅读了提供的URL中的文章。以下是摘要：

该文章讨论了目前正在智利建造的极大望远镜（ELT），以及它革新天文学的潜力。ELT的主镜直径为39米，将成为有史以来建造的最大的光学望远镜，使现有的天文台相形见绌。其前所未有的集光能力和自适应光学系统将使其能够以前所未有的清晰度和细节观测宇宙。

ELT的主要目标包括研究系外行星，并通过分析其大气成分来潜在地探测其他世界上的生命迹象。它还将使天文学家能够探测早期宇宙，观测第一批星系并了解宇宙结构的形成。此外，它将有助于我们理解黑洞、暗物质和暗能量。

望远镜的建造面临着挑战，包括技术难题和资金限制。雄心勃勃的设计和巨大的规模推动了工程技术的边界。然而，科学家们乐观地认为，ELT将克服这些障碍，带来突破性的发现，为宇宙提供无与伦比的见解。文章强调，ELT代表着天文能力的重大飞跃，并有望解决关于宇宙的一些最基本的问题。

---

## 30. 格雷林-纳尔逊悖论

**原文标题**: Grelling–Nelson Paradox

**原文链接**: [https://en.wikipedia.org/wiki/Grelling%E2%80%93Nelson_paradox](https://en.wikipedia.org/wiki/Grelling%E2%80%93Nelson_paradox)

格雷林-纳尔逊悖论，由库尔特·格雷林和伦纳德·纳尔逊于1908年提出，探讨了形容词的自指性质。它主要围绕“自述性”（描述自身，例如“English”）和“异述性”（不描述自身，例如“long”）的定义展开。

当考虑形容词“异述性”本身是否是异述性时，悖论就产生了。如果它*不是*异述性的，那么它就是自述性的，意味着它*确实*描述自身，从而使它变成异述性的，产生矛盾。相反，如果“异述性”*是*异述性的，它就不描述自身，从而使它*不是*异述性的，再次产生矛盾。

本文讨论了通过修改“自述性”和“异述性”的定义来解决该悖论的尝试，但认为这些解决方案是不充分的，因为该悖论会以同义词的形式再次出现。本文认为，解决该悖论需要对英语语言进行更根本的改变，类似于罗素悖论对集合论提出的挑战。

本文还考察了“自述性”，认为它可以一致地是自述性的或异述性的，这与“异述性”不同，后者在任何情况下都会导致矛盾。本文还讨论了模糊的情况，例如“loud”，这取决于它的发音方式。最后，它强调了格雷林-纳尔逊悖论和罗素悖论之间的相似性，解释了如何将一个悖论转化为另一个悖论。

---

## 31. 能成就或摧毁入侵的生态系统动态

**原文标题**: The Ecosystem Dynamics That Can Make or Break an Invasion

**原文链接**: [https://www.quantamagazine.org/the-ecosystem-dynamics-that-can-make-or-break-an-invasion-20250616/](https://www.quantamagazine.org/the-ecosystem-dynamics-that-can-make-or-break-an-invasion-20250616/)

这篇文章来自Quanta Magazine，题为《决定入侵成败的生态系统动力学》，探讨了决定生态系统是否易受入侵物种影响的因素。与长期以来认为多样化的生态系统更具入侵抵抗力的观点相反，利用实验室培养的微生物群落进行的研究表明，具有波动种群的多样化生态系统实际上*更*容易受到入侵。

麻省理工学院的Jeff Gore及其同事在实验室中创建了简化的微生物生态系统来研究生态学原理，从而可以进行受控实验和快速数据收集。他们发现，与稳定、物种贫乏的生态系统相比，种群剧烈波动的生态系统更容易被入侵。这挑战了受查尔斯·埃尔顿启发的传统观点，即生物多样性本身就具有抵抗入侵的能力。

该研究强调了时间和动态种群变化的重要性，表明种群波动可以为入侵者打开生态位。此外，“存活率”——即初始生态系统形成后物种的存活比例——被证明是入侵性的预测指标。较高的存活率与成功入侵的可能性更大相关。

研究人员还发现，虽然物种间存在强烈相互作用的群落更具抵抗入侵的能力，但如果入侵者成功渗透，则会产生更显著的影响。这些发现得到了对Lotka-Volterra模型的修改的支持，强化了种群动态在入侵成功中起重要作用的观点。虽然这些发现对具有长寿命生物（如森林）的生态系统的适用性尚存争议，但这项研究为影响生态入侵的复杂因素的相互作用提供了一个新颖的视角，尤其是在世代周期较短的群落中。

---

## 32. 虚拟细胞

**原文标题**: Virtual cells

**原文链接**: [https://udara.io/science/virtual-cells/](https://udara.io/science/virtual-cells/)

本文记录了虚拟细胞的演变历程，从 1952 年 Hodgkin-Huxley 模型首次用数学方法描述神经元放电开始。由于计算机速度缓慢和生物数据稀缺，用代码模拟整个生命系统的梦想面临了数十年的限制。在 20 世纪 90 年代末，E-Cell 原型（一种简陋的虚拟细菌）的出现是一个关键时刻，它证明了用代码捕获生命系统的可行性。

转折点出现在 2012 年，当时完成了生殖支原体的完整模拟，使研究人员能够操纵虚拟细胞并识别现有生物学理解中的错误。这标志着一个转变，即从研究生物学转变为与生物学合作，使用硅来指导碳。

此后，该领域向两个方向扩展：创建像 JCVI-syn3.0 这样的最小合成生物，它可以被完全模拟；以及构建像大肠杆菌这样复杂生物的模型，揭示细菌菌落中的涌现行为。2022 年，FDA 接受了用于药物安全性测试的计算心脏细胞模型，而 Vivarium 等平台促进了合作。

人工智能的整合，特别是自 2024 年以来，极大地加速了该领域的发展。机器学习现在可以处理复杂的基因表达动力学，从而实现更快的模拟并从新的实验数据中学习。这项技术目前已用于药物发现和个性化医疗，运行数百万次虚拟实验并提供排序的治疗建议。本文强调了一种哲学上的转变，即生物学和计算模型形成一个反馈回路，塑造着医学的未来。

---

## 33. 开源无法协调？

**原文标题**: Open source can't coordinate?

**原文链接**: [https://matklad.github.io/2025/05/20/open-source-cant-coordinate.html](https://matklad.github.io/2025/05/20/open-source-cant-coordinate.html)

开源软件（OSS）的协调困境及其潜力受限：本文认为开源软件在协调方面存在困难，阻碍了其潜力的发挥。作者首先以个人经历为例：由于Linux桌面环境（NixOS上的KDE应用）的碎片化，导致使用过时的热点Linux分析器。作者认为这种碎片化源于缺乏统一的API基线，这与Windows或MacOS不同，后两者由单个实体协调API。

作者将此与语言服务器协议（LSP）的成功进行了对比，LSP标准化了IDE中的交互式静态分析。虽然LSP的技术实现和治理被认为是平庸的，但它的存在本身就促成了重大的进步。JetBrains拥有卓越的IPC架构（Rider），但并没有创建LSP，因为开源软件缺乏构建此类基础设施的激励机制；获取价值对于投资是必要的，而开源软件在这方面往往面临困难。微软创建LSP，其动机是希望主导开发者生态系统，这突显了开源软件在协调方面的错失良机。

尽管如此，作者承认Linux的成功，并将其归因于两个因素：对API区域的集中控制以及对公共接口的坚定承诺，以及POSIX的存在。POSIX提供了一个预定义的API，Linux、BSDs和XNU都可以实现，从而有效地解决了协调问题。然而，Linux桌面缺乏类似的协调力量，导致了引言中所描述的碎片化状态。

---

## 34. 安德烈·卡帕西：人工智能时代的软件 [视频]

**原文标题**: Andrej Karpathy: Software in the era of AI [video]

**原文链接**: [https://www.youtube.com/watch?v=LCEmiRjPEtQ](https://www.youtube.com/watch?v=LCEmiRjPEtQ)

提供的“内容”似乎是YouTube的标准页脚信息，而不是Andrej Karpathy的演讲“人工智能时代的软件”的文字稿或摘要。因此，由于它与视频无关，所以无法总结此“内容”。

要提供摘要，我需要关于Karpathy在视频中讨论内容的实际信息。不过，我可以根据Karpathy的专业知识和视频标题进行推测：

**推测性摘要（基于标题和Karpathy的已知兴趣）：**

Andrej Karpathy的“人工智能时代的软件”可能探讨了人工智能的兴起，特别是大型语言模型和其他神经网络，是如何从根本上改变软件开发的。 该视频可能讨论了从显式编程逻辑到人工智能驱动方法的转变，在这些方法中，模型从数据中学习以执行以前由传统代码处理的任务。

主要主题可能包括：

*   **程序员角色的转变：** 强调数据管理、模型训练和评估，而不仅仅是编写代码。
*   **神经网络作为构建模块的兴起：** 将预训练模型集成到应用程序中，用于图像识别、自然语言处理和代码生成等任务。
*   **人工智能驱动软件的挑战：** 解决诸如可解释性、偏见、稳健性和安全性等问题。
*   **新的编程范式：** 探索为使用人工智能模型和数据量身定制的新工具和框架。
*   **软件开发的未来：** 预测人工智能将如何继续塑造行业以及成功所需的技能。

当然，这只是推测。 真正的摘要需要来自视频的实际内容。

---

## 35. 任何语言的文学编程工具

**原文标题**: Literate programming tool for any language

**原文链接**: [https://github.com/zyedidia/Literate](https://github.com/zyedidia/Literate)

Literate：一种用于创建文学编程的工具，文学编程是一种优先考虑人类理解而非执行的编程风格。受到Donald Knuth的CWEB启发，Literate旨在简化和增强文学编程过程，同时支持任何编程语言。

主要功能包括：基于Markdown的易读易写源码、HTML中的语法高亮和美化打印、与源代码行关联的错误报告、生成可读和带有注释的代码、支持TeX公式、代码段之间的自动超链接以及自定义选项。

该示例演示了一个简单的C语言“Hello world”程序，在文学源文件中定义和解释代码块。编译.lit文件会生成一个.c文件和一个.html文件。

安装方法包括下载适用于各种操作系统的预构建二进制文件，或使用D编程语言（dmd和dub）从源代码构建。该工具默认受Micro编辑器支持，并且有Vim插件可用。

使用方法包括运行带有选项的`lit`命令，例如`--tangle`（仅代码）、`--weave`（仅HTML）、`--out-dir`（输出目录）和`--compiler`（错误报告）。该项目欢迎贡献和错误报告，源代码位于“lit”目录中。

---

## 36. Sunsonic 986-II – 泰国产的带键盘和迷你CRT的Famicom克隆机

**原文标题**: Sunsonic 986-II – A Thai Famicom clone with keyboard and mini CRT built-in

**原文链接**: [https://mastodon.gamedev.place/@pikuma/114711138512697712](https://mastodon.gamedev.place/@pikuma/114711138512697712)

这篇文章（来自pikuma.com上Gamedev Mastodon帖子中的链接）描述了“Sunsonic 986-II”，这是一款泰国产的红白机（任天堂娱乐系统）克隆机。这款克隆机的独特之处在于它内置了键盘和一个迷你CRT屏幕。这意味着该游戏机是一个独立的单元，允许用户无需单独的电视或键盘即可玩红白机游戏。本质上，它是一款便携式、一体化的红白机风格游戏设备。文章很可能强调了这些独特功能的结合，使其成为一款引人注目且有趣的红白机克隆机。

---

## 37. 流水线状态机损坏

**原文标题**: Pipelined State Machine Corruption

**原文链接**: [https://flak.tedunangst.com/post/pipelined-state-machine-corruption](https://flak.tedunangst.com/post/pipelined-state-machine-corruption)

客户端流水线操作导致网络服务器状态机损坏的潜在风险（以SMTP等文本协议为例）。理论上，简单服务器应按顺序处理流水线请求，但依赖隐式状态可能导致问题。

作者推测，较旧的服务器可能假设每个连接在同一时间仅因一个原因触发一次唤醒。如果服务器正在等待与`MAIL FROM`命令相关的DNS响应，则可能错误地处理并响应随后过早收到的`RCPT TO`命令，从而导致不正确的行为。这是因为服务器依赖于文件描述符准备好来代理当前状态，而不是显式地跟踪它。

文章随后指出RFC 2920，其中提供了与stdio缓冲和`fork/exec`相关的具体示例，当执行helper进程时，预读数据可能会丢失。这种数据丢失会导致服务器混淆和流水线故障。最后，文章提到，如果服务器发送响应的速度快于客户端读取的速度，填满管道并阻止进一步的进展，则可能导致死锁。

---

## 38. 倍低音大提琴

**原文标题**: Octobass

**原文链接**: [https://www.atlasobscura.com/places/octobass](https://www.atlasobscura.com/places/octobass)

低音倍大提琴：由让-巴蒂斯特·维尧姆于1850年发明，是一种罕见的巨型弦乐器，旨在为管弦乐音乐增加超低音轰鸣声。它高11-12英尺，是低音提琴的两倍大，发出的音符非常低，通常低于人类听力范围，产生可以感觉到的振动。

最初需要两名演奏者——一名拉弓，一名操作压弦的杠杆——低音倍大提琴的巨大尺寸使其难以演奏。杠杆控制类似变调夹的机械装置，因为琴弦太大，无法用手指按压。

如今，只有少数几件此类乐器存在，大多在博物馆里。位于亚利桑那州菲尼克斯的乐器博物馆拥有一件调音为C0、G0、D1的乐器，比低音提琴低一个八度。蒙特利尔交响乐团是唯一已知拥有并偶尔使用低音倍大提琴的乐团，现在通常由一位音乐家演奏。

要参观菲尼克斯乐器博物馆的低音倍大提琴，游客必须支付 20 美元的入场费，并预计排队，并至少预留两个小时来参观博物馆的其他展品。

---

## 39. Twake – 开源Google Workspace替代方案

**原文标题**: Twake – open-source Google Workspace alternative

**原文链接**: [https://twake.app](https://twake.app)

Twake：注重隐私的开源 Google Workspace 替代方案，提供一系列旨在提高效率和增强专业及个人环境中安全性的工具。该平台强调数据隐私和控制，提供基于云或本地部署的选项。

Twake Workplace 的主要组件包括 Twake Chat（安全即时通讯工具）、Twake Drive（加密数据存储）和 Twake Mail（安全电子邮件解决方案）。所有产品均可通过单一 Twake ID 访问。Twake Chat 具有与其他平台（Telegram、Discord、Signal）桥接等功能，方便用户沟通。Twake Mail 注重数据隐私，采用高级加密和反垃圾邮件措施。Twake Drive 允许用户安全地存储和共享文件，并集成了 Only Office 用于文档管理。

Twake 强调其对安全的承诺，包括加密数据存储、符合 GDPR（数据存储在法国）、SSL/TLS 加密和端到端 websocket 通信。该平台提供通过 Docker 进行本地安装，以增强数据控制。他们还宣传即将推出的功能，包括事件管理和安全视频会议。最后，Twake 将自己定位为欧洲开源领域的领导力量。

---

## 40. Show HN: 用Rust和x86汇编写的一个类DOS的业余操作系统

**原文标题**: Show HN: A DOS-like hobby OS written in Rust and x86 assembly

**原文链接**: [https://github.com/krustowski/rou2exOS](https://github.com/krustowski/rou2exOS)

此“Show HN”帖子宣布了`rou2exOS Rusted Edition`，这是一个用Rust和x86汇编编写的业余操作系统，代表了对原始RoureXOS的重写。作者提供了指向博客文章的链接，详细介绍了原始版本和基于Rust的版本。

该操作系统可以使用QEMU模拟器从提供的ISO镜像启动，并且已经使用USB驱动器在x86_64裸机上进行了测试。该帖子包括关于如何构建和运行操作系统的说明，首先使用`make init`安装Rust依赖项。它强调了Linux上需要`xorriso`、`net-tools`、`grub2-tools`和`qemu`软件包。`make build`命令编译内核和引导加载程序，链接它们，并创建可引导的ISO镜像。然后，`make run_iso`和`make run_iso_floppy`命令在QEMU中执行操作系统，可以选择使用软盘镜像。或者，在添加`bootloader`依赖项后，可以使用`cargo bootimage`和`make run`直接运行内核。

最后，该帖子详细介绍了在QEMU中运行内核后，如何使用`slattach`、`ifconfig`和`tcpdump`测试ICMP/SLIP功能，以识别`pty`设备。这使得用户能够创建用于网络通信的SLIP接口(sl0)。

---

## 41. 看来我现在是个理性主义者了。

**原文标题**: Guess I'm a rationalist now

**原文链接**: [https://scottaaronson.blog/?p=8908](https://scottaaronson.blog/?p=8908)

在题为《我想我现在是理性主义者了》的博文中，斯科特·阿伦森回忆了自己参加理性主义博客会议LessOnline的经历，并首次公开表明自己是一名理性主义者。他描述了会上活跃的学术氛围以及他与社区中杰出人物进行的引人入胜的对话。

阿伦森概述了他之前不愿认同理性主义的原因，主要有两个：一是他们早期对人工智能风险的痴迷，他最初对此不屑一顾；二是该社群主要由年轻、非常规的生活方式的人组成，而他自己作为终身教授和家长，生活则更传统，他认为两者之间存在文化差距。他现在承认，实证发展已经证实了理性主义者对人工智能的担忧，并且该社群已经发展到包括更广泛的生活方式和关注点，包括育儿。

他还回应了理性主义类似于邪教的批评，认为虽然该社群确实持有强烈的信念，但它鼓励公开讨论和辩论。阿伦森承认，他此前曾因害怕与理性主义者联系在一起而遭到学术界同事和其他人的反对，但他现在更看重他们的社群和共同的学术追求，而不是外部的认可。 最终，他拥抱自己长期坚持的价值观，这些价值观与理性主义的核心原则相符，而不管他人的看法如何。

---

## 42. 无限 Mac OS X

**原文标题**: Infinite Mac OS X

**原文链接**: [https://blog.persistent.info/2025/03/infinite-mac-os-x.html](https://blog.persistent.info/2025/03/infinite-mac-os-x.html)

本文详细介绍了作者在 Infinite Mac 中运行早期 Mac OS X 版本的经历。Infinite Mac 是一个在网页浏览器中模拟经典 Mac 操作系统的项目。由于对 DingusPPC 模拟器的进展感到沮丧，作者成功地将较旧的 Mac OS X 模拟器 PearPC 移植到 WebAssembly。虽然 PearPC 最初更可靠，但它比 DingusPPC 慢。作者随后在 PearPC 中复制了 DingusPPC 的性能优化，从而缩短了启动时间。

一项重大发现涉及在机器状态寄存器中实现浮点位检查，这令人惊讶地修复了两个模拟器中的渲染故障。这种优化也稳定了 DingusPPC，使其能够可靠地运行 Mac OS X 10.1。

作者还重建了 Infinite HD，这是一个包含时代软件的磁盘映像，以包含早期的 Mac OS X 应用程序。这涉及到克服与挂载旧磁盘映像格式以及从 Wayback Machine 等档案中获取软件相关的挑战。为了改善 Infinite Mac 的体验，添加了一个 Aqua 主题的 UI，复制了早期 Mac OS X 版本的风格。

文章最后提出了潜在的未来项目，包括模拟 A/UX、Lisa、Pippin 和 Newton。作者还注意到将 QEMU 编译到 WebAssembly 的性能方面令人鼓舞的进展。最后，他提到了一些他添加的巧妙功能，例如详细启动、多驱动器支持和 Classic Mode 兼容性。

---

## 43. 曲纹折纸雕塑

**原文标题**: Curved-Crease Sculpture

**原文链接**: [https://erikdemaine.org/curved/](https://erikdemaine.org/curved/)

埃里克·德梅因和马丁·德梅因创作“弧线折痕雕塑”，这是一种沿弧线折叠使纸张自然形成平衡形状的折纸形式。这些平衡形态尚未被充分理解，德梅因父子正在探索这种自折叠折纸在可展开结构、制造和自组装中的应用可能性。他们形容由此产生的雕塑感觉“栩栩如生”。

文章随后列出了德梅因父子的一系列艺术作品，从“自由系列”（2024年）开始，追溯到“计算折纸”（2008年）。这些系列曾在包括史密森尼美国艺术博物馆、MoMA和国家数学博物馆在内的多家画廊和博物馆展出。该列表表明了一些系列的持续性，例如“火焰系列”（2017年至今）。

最后，文章提到了弧线折纸雕塑的历史，追溯到 1920 年代在包豪斯，并提供了一个包含早期参考文献的部分历史链接。这篇文章由埃里克·德梅因于 2024 年 8 月 26 日最后更新。

---

## 44. Kubernetes 2.0会是什么样？

**原文标题**: What would a Kubernetes 2.0 look like

**原文链接**: [https://matduggan.com/what-would-a-kubernetes-2-0-look-like/](https://matduggan.com/what-would-a-kubernetes-2-0-look-like/)

本文探讨了 Kubernetes (k8s) 从其在 Google Borg 中的起源到目前作为容器编排领域主导力量的演变过程。作者强调了 k8s 的积极方面，包括其大规模管理容器的能力、低维护性（从“宠物”到“UUID”的转变）、作业执行系统以及服务发现和负载均衡能力。

然而，本文也指出了持续存在的问题，并为假设的“Kubernetes 2.0”提出了改进建议。主要建议包括：

*   **用 HCL 替换 YAML：** 作者认为 YAML 容易出错且缺乏类型安全，因此提倡使用 HCL (HashiCorp Configuration Language)，因为它具有强类型、内置验证以及在 Terraform 等工具中的现有应用。
*   **允许 etcd 替换：** 作者建议在持久层方面提供更大的灵活性，建议将 kine 项目正式化，从而能够使用分布式 SQLite 等替代后端来减少资源消耗，尤其是在较小的集群中。
*   **开发原生包管理器：** 作者批评 Helm 复杂模板、缺乏依赖管理以及难以解决冲突的问题，呼吁开发一个直接集成到 k8s 中的原生包管理器，以解决这些缺点并改善整体用户体验。文章还提到了缺乏正确的 Chart 验证。

作者最后强调，这些改变将使 Kubernetes 对更广泛的用户和用例来说更易于访问、更高效和更强大。

---

## 45. FedFlix — 公共领域素材库

**原文标题**: FedFlix — Public Domain Stock Footage Library

**原文链接**: [https://public.resource.org/ntis.gov/index.html](https://public.resource.org/ntis.gov/index.html)

FedFlix是由国家技术信息服务局 (NTIS) 和 Public.Resource.Org (PRO) 合作建立的公共领域素材库。该协议于2007年启动，并于2009年续签/修订，旨在促进公众访问 NTIS 收藏的多媒体产品。

NTIS每月选择10-20个无版权录像带，并将它们运送给PRO。PRO将这些录像带数字化，通常在15天内将原始录像带和DVD副本返还给NTIS。录像带和DVD均归美国政府所有。PRO承担数字化费用，而NTIS承担运输费用。

随后，NTIS和PRO都可以通过网站或其他渠道向公众免费或以任何价格提供这些内容，并保留100%的收入。PRO对该内容不主张任何知识产权。

该协议是非排他性的，允许NTIS与其他合作伙伴共享内容。它规定了终止程序，并禁止未经同意转让权利。该协议还包含关于其解释的法律条款，并明确表示它不构成合伙关系。完整的馆藏可在YouTube和互联网档案馆上找到，并可下载用于纪录片。

---

## 46. Show HN: Sexprs – 用 Rust 编写的 Lisp 方言

**原文标题**: Show HN: Sexprs – Lisp dialect written in Rust

**原文链接**: [https://github.com/gabrielfalcao/sexprs](https://github.com/gabrielfalcao/sexprs)

这个 Show HN 帖子介绍了一个用 Rust 实现的极简 Lisp 方言 "sexprs"。 "sexprs" 这个名字来源于 Lisp 中的基本数据结构 "s-表达式" (s-expressions)。该项目提供了一个命令行 REPL (读取-求值-打印循环)，允许用户交互式地求值 Lisp 代码。该帖子提供了简单的安装说明，使用 `cargo install sexprs-repl`，并展示了如何使用 `sexprs` 命令启动 REPL。重点在于一个基于 Rust 的、用于求值 s-表达式的基本实现，本质上提供了一个用 Rust 编写的简单 Lisp 解释器。

---

## 47. 学习Makefile

**原文标题**: Learn Makefiles

**原文链接**: [https://makefiletutorial.com/](https://makefiletutorial.com/)

Makefile全面指南：C/C++编译

---

## 48. Show HN: Claude 代码使用量监控器 – 实时追踪，避免用量限制

**原文标题**: Show HN: Claude Code Usage Monitor – real-time tracker to dodge usage cut-offs

**原文链接**: [https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor)

Claude代码使用监控：实时追踪Claude AI token用量，避免意外中断。该工具提供实时更新、token和时间的可视化进度条，以及基于消耗率的智能预测，估算token耗尽时间。它支持多种计划（Pro、Max5、Max20），并为具有可变限制的用户提供自动检测功能。

主要功能包括：每3秒实时监控、可视化进度条、token耗尽智能预测、基于用量的自动计划切换、支持多种计划，以及可自定义的重置时间和时区。

指南提供快速入门和使用虚拟环境隔离依赖项的推荐生产设置说明。它概述了使用命令行选项指定计划、自定义重置时间和时区的基本用法。它解释了Claude会话的工作方式（5小时滚动窗口）以及消耗率计算背后的逻辑。

文档提供了适用于各种场景的用例，例如早间开发者、夜猫子程序员、具有可变限制的重度用户和国际用户。它提供了设置、使用和优化的最佳实践，包括在会话早期开始监控、使用虚拟环境以及设置自定义shell别名。它还包括一个针对常见问题的故障排除部分，例如“未找到活动会话”。最后，它提供联系信息以获取支持，并鼓励贡献、错误报告和功能请求。

---

## 49. OpenElections 如何使用 LLM

**原文标题**: How OpenElections uses LLMs

**原文链接**: [https://thescoop.org/archives/2025/06/09/how-openelections-uses-llms/index.html](https://thescoop.org/archives/2025/06/09/how-openelections-uses-llms/index.html)

OpenElections使用谷歌Gemini LLM将选举结果的图像PDF转换为CSV文件，克服了传统OCR和人工数据录入的局限性。 主要挑战是从图像PDF中解析选举结果，这些PDF通常具有复杂的布局和标记。 虽然人工数据录入经过实践可以做到准确，但成本高昂且耗时。 商业OCR软件在处理复杂的PDF时会遇到困难。

选择Gemini的原因是其高准确性和大上下文窗口，使其能够处理大型PDF。 本文提供了来自德克萨斯州莱姆斯通、莱沃克和卡梅伦县的案例。 Gemini在极少的指导下，能够准确解析莱姆斯通县PDF中的双栏布局和点分隔数据。 它还处理了莱沃克县的PDF，该PDF具有绿色背景和不一致的阴影。 然而，Gemini难以处理卡梅伦县的653页PDF，需要将PDF分成较小的块才能进行准确解析。

尽管Gemini有效，但本文强调需要验证以确保准确性。 OpenElections采用自动化测试来检查格式问题、重复记录和数学不一致。 还会对照官方累积报告进行人工验证。 本文的结论是，使用LLM可以显著加快将选举结果转换为可用数据的过程，但准确性仍然是首要任务，因此需要一个制衡系统。

---

## 50. 空气中漂浮的DNA可追踪野生动物、病毒甚至药物

**原文标题**: DNA floating in the air tracks wildlife, viruses, even drugs

**原文链接**: [https://www.sciencedaily.com/releases/2025/06/250603114822.htm](https://www.sciencedaily.com/releases/2025/06/250603114822.htm)

2025年的一项研究中，佛罗里达大学的研究人员发现空气中含有丰富的环境DNA（eDNA），可用于追踪野生动物、病毒甚至毒品。他们利用空气过滤器和先进的eDNA分析技术，分析了来自爱尔兰都柏林的空气样本，检测到大麻、罂粟、迷幻蘑菇和各种病原体的遗传物质。

这项新兴技术可以对生态系统进行非侵入式监测。它可以追踪物种，检测疾病，并确定濒危动物的来源，所有这些都来自空气样本。研究人员展示了使用空气过滤器识别数百种人类病原体、花粉等过敏原，并追踪佛罗里达森林中山猫和蜘蛛来源的能力。该方法提供快速高效的分析，一名研究人员可以在一天内使用经济实惠的设备和基于云的软件处理样本中所有物种的DNA。

这种快速的周转时间使得更广泛地使用先进的环境研究成为可能。由David Duffy领导的研究人员强调，对于负责任地使用这项强大技术，特别是关于敏感的人类遗传数据，制定道德准则至关重要。该研究展示了环境监测方面的重大进展，通过利用简单呼吸中的信息，将科幻小说变成了现实。

---

## 51. 一个汉堡包眼中的慕尼黑

**原文标题**: Munich from a Hamburger's perspective

**原文链接**: [https://mertbulan.com/2025/06/14/munich-from-a-hamburgers-perspective/](https://mertbulan.com/2025/06/14/munich-from-a-hamburgers-perspective/)

汉堡人眼中的慕尼黑：一次城市对比之旅，作者强调理解历史背景，特别是维特尔斯巴赫王朝对慕尼黑的影响以及汉堡作为自由帝国城市的历史，对理解两座城市的差异至关重要。慕尼黑被描绘成一座受中央集权和财富塑造的城市，拥有令人印象深刻的建筑、众多的博物馆（通常侧重于宗教艺术）以及对文化的强烈重视，部分原因归功于路德维希一世国王。作者强调了这座城市的清洁，尤其是伊萨尔河，以及靠近如湖泊和阿尔卑斯山等令人惊叹的自然景观。然而，他们注意到缺乏树木的“光秃秃的街道”以及比汉堡更高的人口密度，导致感觉更加拥挤。另一方面，汉堡以其独立、以贸易为中心的历史为特征，从而形成了更加分散、简约的风格，并更加重视树木。作者发现汉堡的博物馆更加多样化，并且更具个人吸引力。虽然作者欣赏慕尼黑的文化底蕴、自然美景和卓越的公共交通（包括有轨电车），但结论是，这座城市以汽车为中心的布局、较高的人口密度和独特的文化氛围使汉堡更具吸引力。他们也承认慕尼黑靠近其他欧洲国家以及更强大的科技产业。作者最后表示，慕尼黑值得一游，去体验这座城市独特的方面，但总的来说，他们更喜欢汉堡。

---

## 52. Show HN: EnrichMCP – 用于智能体的 Python ORM

**原文标题**: Show HN: EnrichMCP – A Python ORM for Agents

**原文链接**: [https://github.com/featureform/enrichmcp](https://github.com/featureform/enrichmcp)

EnrichMCP：为AI Agent设计的Python ORM，提供语义理解和简易数据模型导航。它基于模型上下文协议（MCP），类似AI领域的SQLAlchemy，提供自动生成类型化工具、关系处理、模式发现和Pydantic验证等功能。

该框架支持多种后端，包括数据库、API和自定义逻辑。文章提供了三个代码示例：一个展示与现有SQLAlchemy模型的集成，另一个演示如何封装REST API，第三个则提供使用自定义逻辑完全控制数据层的方法。

EnrichMCP的关键特性包括自动模式发现、关系导航、类型安全和验证、可变性和CRUD操作、内置分页以及上下文/认证管理。其目标是在MCP之上添加语义层、数据层和控制层，使AI Agent能够更自然地与数据交互。

文章鼓励用户探索提供的示例，并提供完整文档、入门指南和API参考的链接。同时也欢迎贡献，并采用Apache 2.0许可协议。EnrichMCP由Featureform构建，并利用MCP协议。

---

## 53. 展示一下：自动为PR创建有组织提交的工具

**原文标题**: Show HN: Tool to Automatically Create Organized Commits for PRs

**原文链接**: [https://github.com/edverma/git-smart-squash](https://github.com/edverma/git-smart-squash)

Git Smart Squash 是一款旨在自动整理混乱的提交历史，将其整理为清晰、符合逻辑的提交，以便更轻松地进行 PR 审查的工具。它利用人工智能分析您的差异并对相关更改进行分组，从而创建符合常规标准的提交消息。

该工具通过 pip (`pip install git-smart-squash`) 安装以及设置本地 (Ollama) 或云端 (OpenAI, Anthropic, Gemini) AI 提供商，实现了快速启动。使用方法包括简单地导航到您的 Git 仓库，检出特性分支，然后运行 `git-smart-squash`（或 `gss`），这会在应用更改之前显示一个计划。`--auto-apply` 标志会绕过确认提示。

该工具强调安全性，默认执行 dry run，创建备份分支，并避免自动推送。 通过备份分支中保存的原始提交，可以轻松恢复。

用户可以自定义 AI 提供商，通过命令行参数或项目特定或全局配置文件指定 OpenAI、Anthropic 或 Gemini。

针对诸如“Ollama not found”、“No changes to reorganize”和“Token limit exceeded”等常见问题提供了故障排除提示，并提供了诸如安装 Ollama、验证特性分支上的工作以及使用云提供商处理大型差异的解决方案。该工具采用 MIT 许可证。

---

## 54. 黑猩猩观察到机器人打哈欠时也会打哈欠

**原文标题**: Chimpanzees yawn when observing an android yawn

**原文链接**: [https://www.nature.com/articles/s41598-025-98639-z](https://www.nature.com/articles/s41598-025-98639-z)

本研究调查了黑猩猩在观察显示面部表情的仿生机器人时发生的传染性打哈欠现象。研究人员让成年黑猩猩观察仿生机器人打哈欠、张口（嘴巴部分张开）或保持静止闭嘴。结果表明，黑猩猩对仿生机器人表现出打哈欠的传染性，其中在“打哈欠”条件下观察到的传染性最高，其次是“张口”条件，而在“闭嘴”条件下没有观察到传染性。

该研究还发现，黑猩猩在观看仿生机器人打哈欠时表现出与嗜睡相关的行为，例如收集床上用品、筑巢和躺下。这表明打哈欠是一种休息的情境线索，而不仅仅是触发一种运动反应。

该研究强调了非人类灵长类动物容易受到传染性诱导行为的影响，即使这些行为是由人工代理触发的。它强调了社会因素在塑造打哈欠传染性中的作用，并表明诸如共情和传染等核心社会机制可以在跨物种甚至是由非生物代理触发。该研究有助于理解社会互动机制的进化根源，并呼吁进一步研究跨物种和跨代理的互动。

---

## 55. 从开放权重语言模型中提取记忆的书籍片段

**原文标题**: Extracting memorized pieces of books from open-weight language models

**原文链接**: [https://arxiv.org/abs/2505.12546](https://arxiv.org/abs/2505.12546)

这篇于2025年5月18日提交的arXiv论文探讨了大型语言模型（LLM）记忆受版权保护材料（尤其是书籍）的程度。作者包括A. Feder Cooper和Percy Liang，他们使用概率提取技术从13个开源LLM中提取Books3数据集的片段。

研究表明，LLM确实会记忆某些书籍的大部分内容，表明这些记忆内容基本上复制在模型的参数中。然而，记忆程度因LLM和书籍而异。

该研究发现，较大的LLM通常不会完全或部分记忆大多数书籍。有趣的是，Llama 3.1 70B对某些书籍表现出显著的记忆水平，特别是《哈利·波特》和《1984》，可能几乎完全记忆了它们。

作者认为，这些发现对与生成式AI相关的版权诉讼具有重要的，尽管并非决定性的影响。结果突出了LLM背景下记忆与版权之间关系的复杂性，超越了简单的“已记忆”与“未记忆”的争论。该论文还包括代码、数据、媒体和其他相关资源的链接，以供进一步探索。

---

## 56. Strudel入门指南

**原文标题**: Getting Started Strudel

**原文链接**: [https://strudel.cc/workshop/getting-started/](https://strudel.cc/workshop/getting-started/)

本文介绍了Strudel，一个Tidal Cycles模式语言的JavaScript移植版本，它可以通过代码创作音乐。它强调了对没有JavaScript或Tidal Cycles先验知识的初学者的可访问性。Strudel方便了实时编码音乐、算法作曲、音乐与代码的共同教学，以及通过MIDI或OSC与现有音乐设备的集成。

本文通过代码示例突出了Strudel在创建包含鼓、和弦和旋律的复杂音乐纹理方面的功能。它使用了诸如模式操作、采样、效果处理和节奏变化等特性。该示例展示了Strudel创作动态和富有表现力的音乐作品的能力。

本文还鼓励超越所提供的示例进行探索，引导用户浏览Strudel应用展示。它指出工作坊是最好的初始学习资源，并建议从创建第一个声音作为实践切入点开始。本质上，本文充当了一个欢迎和邀请，邀请您使用Strudel探索使用代码进行音乐创作的世界。

---

## 57. 椭圆曲线之美

**原文标题**: Elliptic Curves as Art

**原文链接**: [https://elliptic-curves.art/](https://elliptic-curves.art/)

该网页介绍了一个将椭圆曲线可视化的项目，旨在探索其艺术潜力。该项目由Nadir Hajouji和Steve Trettel领导，致力于以视觉上吸引人的方式呈现椭圆曲线。虽然该页面目前正在建设中，但它通过提及论文和“精美插图”暗示了该项目的未来范围。总体目标似乎是展示椭圆曲线数学结构中固有的美感和视觉吸引力，从而模糊数学和艺术之间的界限。

---

## 58. 公有/保护/私有 是一种不必要的功能。

**原文标题**: Public/protected/private is an unnecessary feature

**原文链接**: [https://catern.com/private.html](https://catern.com/private.html)

本文认为，访问修饰符（public、protected、private）在面向对象编程语言中是不必要的功能，本质上重复了接口和子类型已经提供的功能。

作者使用经典的汽车/车辆示例来说明这个问题。虽然接口有效地限制了用户如何*实例化*和与`Car`这样的类进行交互，但它们无法控制`Car`的子类如何访问和修改其内部结构，从而可能违反其不变性。访问修饰符被用作一种变通方法，为子类定义了一个伪接口。

作者认为这是多余的。语言可以强制子类仅通过指定的接口与基类交互，就像外部用户一样，而不是使用访问修饰符。这将创建一个统一的系统，用于定义实例化和继承的接口。

本文声称，Simula 中访问修饰符的发明源于缺乏对现有功能（虚拟方法和子类型）已经可以提供足够的接口定义的认识。作者提出了一个假设的替代方案，其中子类访问仅限于在基本接口中声明的字段。

结论鼓励程序员尽可能避免使用访问修饰符，尤其是在构造受到限制的最终类中。接口应该是保护类内部结构的主要机制。作者甚至提倡组合优于继承，并将继承视为一个有缺陷的概念，最初需要访问修饰符。

---

## 59. Show HN：RM2000 磁带录音机，macOS 音频采样器

**原文标题**: Show HN: RM2000 Tape Recorder, an audio sampler for macOS

**原文链接**: [https://rm2000.app](https://rm2000.app)

RM2000录音机是一款全新的macOS应用程序，旨在简化音频采样和录制，直接从Mac的系统音频进行录制。该应用程序旨在消除其他解决方案中常见的繁琐设置过程，例如音频路由技巧或非为此目的设计的第三方工具。

RM2000录音机通过被动监听Mac的音频输出进行工作，使您可以立即录制Mac正在播放的任何内容，而无需复杂的配置。它专注于易用性和可访问性，无需路由或设置。

该应用程序提倡“文件优先于应用”的理念，这意味着录音可以轻松访问，以便在其他应用程序中使用。它在Mac App Store上提供，只需一次性购买永久许可证，避免订阅模式。还提供免费试用。

目前正在进行发布促销，永久许可证的售价为6.99美元，截止日期为6月30日。这突出了该应用程序的价值主张，即作为一个简单且经济实惠的解决方案，用于在macOS上捕捉音频灵感。

---

## 60. 我愿意做任何事来结束无家可归的状况，除了建造更多的房屋 (2018)

**原文标题**: I will do anything to end homelessness except build more homes (2018)

**原文链接**: [https://www.mcsweeneys.net/articles/i-will-do-anything-to-end-homelessness-except-build-more-homes](https://www.mcsweeneys.net/articles/i-will-do-anything-to-end-homelessness-except-build-more-homes)

霍马·莫杰塔拜的讽刺作品《为了结束无家可归，我什么都愿意做，除了多盖房子》辛辣地讽刺了那些声称关心无家可归问题，却抵制任何可能给他们带来不便的解决方案的富人的虚伪和自私的邻避主义。作者以第一人称写作，化身为这种人，表达了解决无家可归危机的愿望，同时又反对建造更多的住房。

这篇文章突出了作者自诩的慷慨，这种慷慨取决于无家可归者保持隐形，且不影响房产价值或个人舒适度。作者优先考虑自己的利益，例如他们渴望保护自己的豪华住宅和依赖汽车的生活方式。

这篇文章讽刺了用于反对可负担住房的常见论点，例如担心房产价值降低和不信任无家可归者。作者的偏执甚至延伸到质疑无家可归退伍军人的真实性，并表达了对因向人们提供住房和机会而可能导致的社会变革的恐惧。

最终，这篇文章批判了导致无家可归危机持续存在的自私和缺乏同情心，表明有些人更关心维护自己的特权和舒适，而不是寻找真正的解决方案。作者的结尾陈述：“我宁愿有无家可归危机”，强调了根深蒂固的变革阻力和个人舒适优先于人类苦难的观念。

---

## 61. AI将入侵Jira

**原文标题**: AI is going to hack Jira

**原文链接**: [https://thoughtfuleng.substack.com/p/ai-is-going-to-hack-jira](https://thoughtfuleng.substack.com/p/ai-is-going-to-hack-jira)

好的，我读了ThoughtfulEng的“人工智能将入侵Jira”这篇文章。

以下是摘要：

文章认为，人工智能将从根本上改变软件团队使用Jira（以及类似项目管理工具）的方式。目前，Jira在创建、更新和管理问题方面需要大量的人工工作。人工智能将自动化许多此类任务，从而带来更高效和更具生产力的工作流程。

作者预测人工智能将以以下几种方式“入侵”Jira：

*   **自动化问题创建和分流：** 人工智能将根据监控日志、代码更改、客户反馈和其他数据源自动创建问题。它还将对问题进行分流，根据专业知识和工作量将其分配给适当的团队成员。
*   **智能问题总结和上下文：** 人工智能将提供复杂问题的简洁总结，自动提取相关信息，并将相关工单链接起来以提供有价值的上下文。这将减少用于调查的时间。
*   **人工智能驱动的任务评估和计划：** 人工智能可以分析历史数据以提供更准确的任务评估，从而改进冲刺计划和资源分配。
*   **主动风险检测和缓解：** 通过监控问题模式并识别潜在瓶颈，人工智能将主动识别并帮助缓解项目时间表的风险。
*   **自动化问题解决：** 在某些情况下，人工智能甚至可以根据现有知识和过去的解决方案自动解决某些类型的问题。

作者承认了潜在的挑战，例如确保数据隐私和安全，以及需要人工监督以防止人工智能偏差。然而，他们得出结论，在Jira中集成人工智能的好处是巨大的，有望解放工程师，让他们专注于更高价值的任务并加速软件开发周期。未来，Jira将成为一个更智能和自主的助手，而不是一个手动跟踪工具。

---

## 62. 从LLM到AI智能体：AI系统开发背后的真正旅程是什么？

**原文标题**: From LLM to AI Agent: What's the Real Journey Behind AI System Development?

**原文链接**: [https://www.codelink.io/blog/post/ai-system-development-llm-rag-ai-workflow-agent](https://www.codelink.io/blog/post/ai-system-development-llm-rag-ai-workflow-agent)

本文探讨了人工智能系统开发的演进过程，从基础的大型语言模型（LLMs）到更复杂的AI智能体。文章强调，并非所有AI应用都需要AI智能体的完全自主性，像检索增强生成（RAG）或AI工作流等更简单的解决方案可能更具成本效益，也更适合许多实际应用场景。

文章概述了每个级别的能力：

*   **纯粹LLMs:** 擅长基于其训练数据的任务（摘要、文章写作）。
*   **RAG:** 通过实时信息和内部数据访问增强LLMs，以获得更及时和精确的响应。
*   **AI工作流:** 通过将LLMs连接到外部工具和API来自动化定义明确的业务流程。
*   **AI智能体:** 自动化规划和决策，独立且动态地启动工作流，需要访问各种系统。

作者以简历筛选应用为例，展示了每个级别复杂性的增加。主要结论是，开发人员应从更简单的模式入手，仅在必要时增加复杂性，并且在构建可用于生产的AI系统时，应优先考虑可靠性而不是高级功能。文章建议，由于LLMs的非确定性，应从沙盒环境、一致的测试和护栏开始。

---

## 63. 我们只需测量一下

**原文标题**: We Can Just Measure Things

**原文链接**: [https://lucumr.pocoo.org/2025/6/17/measuring/](https://lucumr.pocoo.org/2025/6/17/measuring/)

在他的博客文章《我们可以直接测量事物》中，Armin Ronacher探讨了使用编程代理来客观评估代码库和开发者工具的质量。他认为，与人类不同，代理可以接受严格的测试和测量，而没有情感偏见，从而为开发者体验提供有价值的见解。

Ronacher指出，许多现有的开发工具都存在文档不足、API令人沮丧和错误报告不佳等问题，经常导致“技能问题”的指责。代理可以通过揭示它们在与代码库交互时的挣扎来帮助量化这些缺点。

他强调了健康代码库的关键指标，这些指标对代理和人类开发者都有益，包括：

*   **良好的测试覆盖率：** 对于防止回归和验证行为至关重要。
*   **良好的错误报告：** 清晰易懂的错误信息对于调试至关重要。
*   **高生态系统稳定性：** 频繁的API更改和更新换代会减慢代理的速度，并导致代码过时。
*   **较少的冗余抽象：** 过多的层级会使数据流和重构变得复杂。
*   **快速且用户友好的工具：** 快速的响应时间和最少的冗余输出可以提高生产力。
*   **良好的开发环境：** 本地可重现性以及环境错误和代码错误之间的明确区分至关重要。

Ronacher总结说，通过使用代理来衡量开发者体验，我们可以识别并解决主流但客观上较差的代码和工具的缺点，最终促成更好的技术选择和库设计。他提供了Xcode的例子，他说他的代理也能衡量地感受到对Xcode的不喜欢。

---

## 64. MCP规范 – 2025-06-18版本变更

**原文标题**: MCP Specification – version 2025-06-18 changes

**原文链接**: [https://modelcontextprotocol.io/specification/2025-06-18/changelog](https://modelcontextprotocol.io/specification/2025-06-18/changelog)

本文档概述了模型上下文协议 (MCP) 规范从 2025-03-26 版本到最新版本 2025-06-18 之间的主要变更。

**主要变更：**

*   **移除批处理：** 已移除 JSON-RPC 批处理支持。
*   **结构化工具输出：** 增加了对工具结构化输出的支持。
*   **OAuth 资源服务器分类：** MCP 服务器现在被分类为 OAuth 资源服务器，包含发现相应授权服务器的元数据。
*   **资源指示器

**其他 Schema 变更：**

*   向更多接口类型添加了 `_meta` 字段，指定其正确用法。
*   向 `CompletionRequest` 添加了 `context` 字段，允许在完成请求中包含先前解析的变量。
*   添加了 `title` 字段，用于人类友好的显示名称。

完整的变更日志可在 GitHub 上获得。

---

## 65. Uxn的自制闭包

**原文标题**: Homegrown Closures for Uxn

**原文链接**: [https://krzysckh.org/b/Homegrown-closures-for-uxn.html](https://krzysckh.org/b/Homegrown-closures-for-uxn.html)

本文介绍了作者在Niënor中实现闭包的方法，Niënor是Uxn虚拟机的一个Lispy环境。面对Uxn底层特性和缺乏运行时类型的限制，作者需要一种方法来创建可以捕获其周围环境中的变量的闭包。

最初简单地命名lambda函数并进行全局编译的方法失败了，因为它无法解析不在全局作用域中的变量。作者拒绝禁用闭包，而是设计了一种运行时策略，该策略将编译时修改与运行时代码生成相结合。

在编译时，编译器识别捕获的变量，并将它们作为参数添加到基础lambda函数中。这确保了所有变量都被绑定。但是，这个修改后的lambda函数不会直接暴露给用户。

相反，一个小的包装器，称为“portal”，在运行时使用`malloc`生成。这个portal将捕获的环境值（局部变量）压入堆栈，然后跳转到内部的、修改后的lambda函数。这有效地模拟了一个闭包调用，确保lambda函数可以访问必要的环境。

本文包含一个使用闭包的GUI程序的示例，并提供了生成的Uxn代码的详细分解。它还提到了`malloc`和`free`的实现，用于手动内存管理，允许用户在不再需要时释放已分配的闭包内存，从而提高内存使用效率。文章最后声明该项目的实验性质，并邀请读者探索和贡献Niënor的开发。

---

## 66. LinkedIn就是个一团糟的马戏团 – 逃离

**原文标题**: LinkedIn Is a Fucked Up Circus – Flee

**原文链接**: [https://medium.com/my-unpopular-opinion/linkedin-is-a-f-cked-up-circus-5c1bc1248f1f](https://medium.com/my-unpopular-opinion/linkedin-is-a-f-cked-up-circus-5c1bc1248f1f)

詹姆斯·克里斯托弗的文章《领英是个一团糟的马戏团——逃离它》，讽刺了领英当前的状况，认为该平台充斥着“专业知识膨胀”和虚假的自我宣传。他认为领英已经从一个专业的社交网站变成了一个“专业的元宇宙”，用户们在那里进行“专业的角色扮演”，为了面子而夸大自己的角色和经历。

这篇文章批评了该平台过度使用自动化工具进行潜在客户开发，将职业人脉变成了营销活动中的数据点。个性化的联系被机器人式的、模板驱动的、充满流行语的信息所取代。

克里斯托弗嘲笑了算法对公式化帖子的偏爱：人为制造的脆弱感、企业流行语和肤浅的灵感。这导致了一种对职业成就的扭曲看法，即肤浅的互动胜过真正的影响。

他提倡使用Medium、Substack和GitHub等替代平台，以及行业特定的网站，个人可以通过实质性的工作和真实的交流来展示他们的专业知识。

最终，克里斯托弗鼓励读者优先考虑真正的职业发展和影响力，而不是精心策划的在线形象。他推销自己的书《人优先于像素》，以此来重新关注商业和品牌中的人性。他建议断开与领英炒作机器的连接，专注于有形的成就和真实的联系。

---

## 67. 区块链分析的内存C++飞跃

**原文标题**: In-Memory C++ Leap in Blockchain Analysis

**原文链接**: [https://caudena.com/the-in-memory-c-leap-in-blockchain-analysis/](https://caudena.com/the-in-memory-c-leap-in-blockchain-analysis/)

Caudena的CashflowD (CFD)：下一代加密货币分析引擎，采用C++构建，以远低于传统系统的成本提供实时、法庭认可的加密情报。CFD解决了区块链数据分析缓慢且昂贵的难题，利用专有的内存数据库和JIT编译查询引擎，将基础设施成本降低200到400倍。

主要特性包括：

*   **内存C++核心：** 通过高度优化的自定义存储、积极的数据打包以及诸如HAMT的自定义数据结构来消除I/O瓶颈，从而实现高效的内存管理和速度。
*   **JIT编译：** 启用动态、即席查询，这些查询使用LLVM的ORCv2即时转换为优化的机器代码，使分析师能够在瞬间从TB级数据中获得深刻见解。
*   **智能聚类和重聚类：** 提供确定性的、法庭认可的地址聚类，并具有完全的可解释性，使用O(1)集群连接和一个Overlay Forest进行精确的重聚类。
*   **弹性且即时的评分：** 实施一种能够抵抗洗钱策略的强大评分模型，该模型具有数学上合理的传播和高效的多阶段评分更新。
*   **缓存和数据遍历：** 采用复杂的缓存系统，包括地址余额、实体和集群统计缓存，以实现亚毫秒级的响应时间。

CFD以极低的成本提供卓越的分析能力，这在区块链数据量快速增长的情况下尤为重要。这使组织能够胜过非法活动，并在区块链领域获得竞争优势。

---

## 68. 星震与巨型冲击波

**原文标题**: Star Quakes and Monster Shock Waves

**原文链接**: [https://www.caltech.edu/about/news/star-quakes-and-monster-shock-waves](https://www.caltech.edu/about/news/star-quakes-and-monster-shock-waves)

加州理工研究人员正利用超级计算机模拟黑洞与中子星之间的剧烈碰撞，为这些极端宇宙事件提供新的见解。一项研究聚焦于黑洞吞噬中子星之前撕裂其表面的“星震”，这可能会产生可探测到的光耀。该模拟显示了黑洞的强大引力如何剪切中子星，导致裂痕，并预测了天文学家可能观测到的特定光辐射。

第二项研究模拟了这些断裂之后的景象，揭示了“巨型冲击波”的产生，这是宇宙中预测的最强冲击波。该模拟还展示了“黑洞脉冲星”的形成，这是一种假想物体，其中黑洞发射出类似脉冲星的磁风，尽管时间很短。预计这些事件会产生无线电波、X射线和伽马射线的爆发。

这些模拟对于解读像LIGO这样的天文台探测到的潜在信号至关重要，LIGO可以探测到此类碰撞产生的引力波。通过预测伴随这些事件的电磁信号，研究人员旨在拼凑出关于这些宇宙合并事件的更完整的图像。配备GPU的超级计算机的使用是这些详细模拟的关键，它允许研究人员对涉及的复杂物理过程进行建模。

---

## 69. Show HN: Unregistry – 无需注册中心，直接“docker push”到服务器

**原文标题**: Show HN: Unregistry – “docker push” directly to servers without a registry

**原文链接**: [https://github.com/psviderski/unregistry](https://github.com/psviderski/unregistry)

Unregistry：无需专用Docker Registry，直接推送Docker镜像到远程服务器的精简方法。它利用临时的轻量级容器镜像registry（`unregistry`），利用Docker守护进程的存储来存放镜像。定制的`docker pussh`命令（注意多了一个's'）通过SSH直接传输镜像，仅发送缺失的层，从而实现速度和效率的提升。

该工具解决了现有方案的常见问题，例如公共仓库、自托管registry的维护负担、低效的`save/load`方法以及资源密集型远程构建。其核心功能包括建立SSH隧道，在远程服务器上启动`unregistry`，转发本地端口，推送镜像层，然后停止临时容器。

提供macOS/Linux平台的安装说明，可通过Homebrew或直接下载进行安装。Windows用户可以尝试通过WSL 2安装。本文包含用于部署到生产环境、CI/CD流水线和气隙环境的使用示例。它强调了本地和远程机器上的要求，建议在远程服务器上使用containerd镜像存储以获得最佳性能。高级用法包括独立运行unregistry以及通过SSH配置文件使用自定义SSH选项。

---

## 70. Show HN: Turbine – 用 C 语言构建的 16 位 CPU 架构和模拟器

**原文标题**: Show HN: Turbine – 16-bit CPU Architecture and Emulator built in C

**原文链接**: [https://www.errorcodezero.dev/blog/building-my-own-cpu-isa-and-virtual-machine/](https://www.errorcodezero.dev/blog/building-my-own-cpu-isa-and-virtual-machine/)

这个“Show HN”帖子详细介绍了 Turbine 的创建过程，Turbine 是一个用 C 语言构建的自定义 16 位 CPU 架构和虚拟机。作者受到 Advent of Code 以及对底层编程和仿真的喜爱启发，在探索用自己的语言 Mango 进行语言开发后，开始了该项目。他们选择 C 语言是因为它的简洁性，并将其与旧计算机的约束相提并论。

帖子概述了 CPU 的核心概念，包括寄存器（通用寄存器和专用寄存器，如指令指针、堆栈指针等）、堆栈的功能以及图灵完备性的关键思想。

作者随后深入探讨了 Turbine 的具体设计，详细介绍了指令集（LOAD、DUMP、MOVE、ADD、SUB、JUMP、HLT 等）以及用于条件分支的相关寄存器标志和状态标志。该设计优先考虑简单性，每条指令都适合单个十六进制数字。数据总线为 16 位，内存为字节寻址。

帖子最后介绍了 C 代码，展示了 `VirtualMachine` 结构体以及初始化和删除函数。作者还描述了将计算 goto 作为单步执行 VM 的方法，但由于可移植性问题和对编译器优化的信任，放弃了该方法。github 仓库链接为 github.com/errorcodezero/turbine，作者请求点亮星星以获得 shipwrecked 的资格。

---

## 71. PWM闪烁：危害健康的隐形光？

**原文标题**: PWM flicker: Invisible light that's harming our health?

**原文链接**: [https://caseorganic.medium.com/the-invisible-light-thats-harming-our-health-and-how-we-can-light-things-better-d3916de90521](https://caseorganic.medium.com/the-invisible-light-thats-harming-our-health-and-how-we-can-light-things-better-d3916de90521)

本文探讨了LED灯和数字显示器中PWM（脉冲宽度调制）闪烁的问题及其对健康和福祉的潜在影响。作者讲述了一段在历史悠久的城堡中的经历，其中LED照明尽管外观温暖，却营造出一种不适的氛围，从而引发了对PWM闪烁的调查。

PWM是一种通过快速开关光源来调光的办法，产生一种闪烁，可能导致眼睛疲劳、不适、偏头痛和恶心，影响敏感人群（占人口的5-20%）。虽然大多数人没有意识到这一点，但文章解释说，我们的眼睛不断地平均这种闪烁，这仍然会导致负面影响，比如减慢决策速度。

文章将PWM与更好的替代方案进行对比，例如恒流降低 (CCR) 调光，它降低了 LED 的电流供应，而没有快速开关，从而显著减少了闪烁并提高了视觉舒适度。CCR通常用于高端照明。

作者强调了寻找“无闪烁”认证产品或具有“高频PWM”（高于20 kHz）和“DC调光”选项的产品的重要性。 Calm Tech Institute 倡导无闪烁标准，甚至有一个认证计划来解决这个问题。 Daylight Computer 是一款刻意设计为不含 PWM 的产品，它是一家通过减轻闪烁来优先考虑客户福祉的公司的例子。文章总结道，了解PWM闪烁可以使个人做出明智的照明选择，从而创造更健康的环境。

---

## 72. Posit浮点数：细长三角形与其他技巧 (2019)

**原文标题**: Posit floating point numbers: thin triangles and other tricks (2019)

**原文链接**: [http://marc-b-reynolds.github.io/math/2019/02/06/Posit1.html](http://marc-b-reynolds.github.io/math/2019/02/06/Posit1.html)

本文批判了将Posit直接替代IEEE binary32浮点数用于通用计算的做法。作者采用“魔术戏法”的方式，展示了Posit在使用海伦公式计算细长三角形面积时优于IEEE的例子。然而，作者承认这些例子有些牵强，呼应了Gustafson的观点，即这种比较可能是不公平的。

作者指出，由于历史硬件限制，IEEE优先考虑更大的指数范围而非精度。这使得IEEE能够表示非常大的数字，作者认为这在实践中通常是不必要的，同时牺牲了精度。Posit（es=2）提供了不同的权衡，提供了更高的精度，尤其是在值1附近，但范围较小。

本文强调IEEE和Posit都是具有局限性的浮点模型，直接比较它们的十进制表示可能会产生误导。作者承认人们普遍认为区间[-1,1]对于许多计算很重要，IEEE在这方面处理得很好。文章随后讨论了舍入误差，认为建模和截断误差是数值分析中更重要的考虑因素。

作者揭示了“魔术戏法”示例利用了Posit在特定范围内比IEEE具有略多可用位的事实，从而在该特定计算中获得更好的精度。文章最后建议读者不要过度强调舍入误差，而应关注算法收敛并了解两种浮点模型的局限性。

---

## 73. 本田成功进行实验性可重复使用火箭的发射和着陆

**原文标题**: Honda conducts successful launch and landing of experimental reusable rocket

**原文链接**: [https://global.honda/en/topics/2025/c_2025-06-17ceng.html](https://global.honda/en/topics/2025/c_2025-06-17ceng.html)

2025年6月17日，本田在日本北海道大树町成功进行了自主研发的实验性可重复使用火箭的发射和着陆测试。此次测试标志着本田在达到近300米高度后首次成功实现火箭着陆。该测试旨在验证火箭可重复使用性的关键技术，包括飞行稳定性和着陆能力。

该火箭长6.3米，干重900公斤，达到了271.4米的高度，并在目标点37厘米范围内着陆，飞行时长为56.6秒。本田认为火箭研究对于利用其在燃烧和控制方面的核心技术至关重要，旨在发射卫星，为与其其他业务兼容的各种服务提供支持。这些服务可能包括用于地球监测的遥感和用于广域通信的卫星星座。

自2024年以来，本田一直在进行发动机燃烧和悬停测试，优先考虑安全并与地方当局合作。本次测试的具体安全措施包括半径1公里的禁区以及防止偏离飞行走廊的安全系统。

本田的目标是通过持续的研发，到2029年实现亚轨道发射。全球首席执行官三部敏宏表示，此次成功代表着本田可重复使用火箭研究的又一步进展，并体现了其创造新价值和解决环境及安全问题的承诺。

---

## 74. 使用 Godot 测试稳健的网络代码

**原文标题**: Testing a Robust Netcode with Godot

**原文链接**: [https://studios.ptilouk.net/little-brats/blog/2024-10-23_netcode.html](https://studios.ptilouk.net/little-brats/blog/2024-10-23_netcode.html)

这篇博文详细介绍了在Godot中为快节奏多人游戏《小恶魔！》实现强大网络代码的挑战。作者解释了诸如延迟补偿、预测和协调等核心概念，并承认它们的复杂性。

重点在于开发过程中有效测试网络代码。虽然多人测试是理想的，但作者建议在单台PC上运行多个Godot实例。为了模拟真实的网路状况（延迟和丢包），文章提倡在Linux中使用`tc`命令。这允许开发者在本地引入人为的网络降级，测试网络代码的弹性。

文章随后深入探讨了Godot的高级网络API，特别是基于UDP的`ENetMultiplayerPeer`类，并探讨了`reliable`、`unreliable`和`unreliable_ordered`模式之间的区别。通过一个发送远程函数调用的测试程序，作者直观地展示了这些模式在不同延迟和丢包条件下的行为。`Unreliable`模式优先考虑速度，不保证数据包的交付，而`reliable`模式确保交付，但在数据包丢失和重新发送时可能会引入延迟。

作者分享了关于使用这些模式的实用建议：`unreliable`用于传输游戏状态（偶尔丢失状态是可以接受的），而`reliable`用于客户端输入（服务器端准确的状态重新计算至关重要）。

最后，文章建议了一种更高级的测试方法：一个可以随时间动态修改网络质量（延迟和丢包）的脚本，模拟波动的网络状况。这旨在确保即使在具有挑战性的网络环境下，游戏仍然可以玩。虽然承认模拟真实多人游戏场景的局限性，但作者强调了这些技术在早期调试和稳定网络代码方面的价值。

---

## 75. 拆分大型科技公司：公民社会宣言

**原文标题**: Break Up Big Tech: Civil Society Declaration

**原文链接**: [https://peoplevsbig.tech/break-up-big-tech-civil-society-declaration/](https://peoplevsbig.tech/break-up-big-tech-civil-society-declaration/)

解散大型科技公司：公民社会宣言

此“解散大型科技公司：公民社会宣言”是一项行动呼吁，敦促欧盟委员会拆解大型科技公司的垄断，特别是谷歌的广告垄断。该宣言由众多公民社会组织签署，认为大型科技公司的统治威胁民主，因为它将对核心数字基础设施的控制集中化，导致权利滥用、企业遭受剥削和竞争受到扼杀。宣言声称，这些公司利用其权力来影响政治论述并破坏民主法律。

宣言强调，罚款是无效的，行为补救措施经常被忽视，并建议通过迫使这些公司出售其部分业务来拆解这些垄断是必要的解决方案。 具体而言，拆解谷歌的广告垄断被认为是一个绝佳的机会，因为它有助于振兴新闻业，保护消费者免受虚高价格的影响，并创造公平的竞争环境。该宣言呼吁欧盟委员会强制谷歌进行资产剥离。

该声明将这个问题定义为争取更自由、更公平互联网的斗争，敦促欧洲抵制来自大型科技公司和特朗普政府的压力，并维护欧盟法律。 最终，该宣言倡导这样一种理念，即解散大型科技公司是迈向更民主、更公平的数字环境的关键一步。

---

## 76. 使用BT盗版者因十年前的罪行被判五年监禁并处一万欧元罚款

**原文标题**: BitTorrent Pirate Gets 5 Years in Prison, €10k Fine, for Decade-Old Offenses

**原文链接**: [https://torrentfreak.com/bittorrent-pirate-gets-5-years-in-prison-for-decade-old-offenses-250620/](https://torrentfreak.com/bittorrent-pirate-gets-5-years-in-prison-for-decade-old-offenses-250620/)

希腊一59岁男子因运营私人BitTorrent网站P2Planet被判处五年监禁和1万欧元罚款。该网站托管了约14000个电影、电视剧和音乐种子。此次判决包括立即执行监禁，令与会者感到惊讶，并被认为是希腊BitTorrent相关犯罪中罕见的案例。

P2Planet活跃于2011年左右，曾遭受DDoS攻击和黑客入侵事件，导致其在2014年关闭。与此同时，警方展开调查并逮捕了该男子，查获了一块硬盘进行法医检查。尽管这些违法行为发生在十多年前，但最近的判决书引用了该网站拥有44342名注册用户以及使用了Azureus torrent客户端的事实。

文章强调了逮捕和判决之间异常长的时间间隔，并将其与 greekstars.net 的一个类似案件进行了对比，该案中的被告更快地受到了类似的判决。虽然严厉的判决理论上起到了威慑作用，但文章质疑其有效性，原因是时间间隔太长，暗示其影响可能会随着时间的推移而被稀释，许多人可能已经忘记或对十年前的违法行为漠不关心。文章还指出，希腊当局正在打击盗版行为。

---

## 77. 在 C++ 中使用 Glaze Stencil/Mustache 进行字符串插值

**原文标题**: String Interpolation in C++ Using Glaze Stencil/Mustache

**原文链接**: [https://stephenberry.github.io/glaze/stencil-mustache/](https://stephenberry.github.io/glaze/stencil-mustache/)

Glaze在C++中提供了强大的字符串插值功能，使用`glz::stencil`和`glz::mustache`格式，灵感来自Mustache模板。这些函数允许您通过将模板与C++结构体结合来动态生成字符串。

`glz::stencil`提供基本插值、布尔章节（`{{#key}}`, `{{^key}}`）、容器迭代（`{{#container_key}}`）和注释（`{{!comment}}`）。

`glz::mustache`为更安全的HTML输出提供HTML转义。双花括号`{{key}}`对输出进行HTML转义，而三花括号`{{{key}}}`提供未转义（原始）输出。常见的HTML实体如`<`、`>`、`&`、`"`和`'`会被转义。

Glaze还提供`glz::stencilcount`，用于在文档中使用`{{+}}`、`{{++}}`、`{{+++}}`进行不同嵌套级别的自动编号。

`glz::stencil`和`glz::mustache`均返回`std::expected<std::string, glz::error_ctx>`，从而允许进行错误处理。常见错误包括`unknown_key`、`unexpected_end`和`syntax_error`。`glz::format_error`提供详细的错误信息。

关键要求包括可反射的结构体或glaze对象、用于章节条件的布尔字段以及模板中存在的字段名称。这些功能可以为各种应用（包括Web开发和文档创建）实现动态内容生成。

---

## 78. 复式记账：现代软件缺失的基础要素

**原文标题**: Double-Entry Ledgers: The Missing Primitive in Modern Software

**原文链接**: [https://www.pgrs.net/2025/06/17/double-entry-ledgers-missing-primitive-in-modern-software/](https://www.pgrs.net/2025/06/17/double-entry-ledgers-missing-primitive-in-modern-software/)

本文认为复式记账法是现代软件开发中一种未被充分利用的基础工具，并提出它比用于跟踪和管理金额及交易的临时解决方案更强大、更高效。作者介绍了 `pgledger`，一个 PostgreSQL 账本实现，旨在简化账本的应用。

复式记账法的核心概念是维护项目的当前余额以及该余额的完整历史记录，包括每次更改的来源。每笔交易至少影响两个账户，确保金额始终被记录在案，并且余额总和为零，从而提供内置的错误检查和可审计性。

本文通过记录付款和管理奖励积分等示例，说明了账本建模的优势。使用账本可以简化支付系统中应收款、退款和账户差异的跟踪，并为奖励计划中的积分分配、消费和转移提供清晰的审计追踪。

作者进一步提出账本可以应用于各种用例，包括使用信用额度跟踪、内容审核操作和库存管理。关键在于，将账本作为基本组件集成可以简化开发，因为它提供了一个可重用、可适应的系统，用于跨各种应用程序跟踪和管理金额，从而降低复杂性并提高数据完整性。他们强调了使用 `pgledger` 等工具的优势，并鼓励进一步探索账本在软件中的应用。

---

## 79. Poline – 一款利用极坐标生成的神秘调色板

**原文标题**: Poline – An enigmatic color palette generator using polar coordinates

**原文链接**: [https://meodai.github.io/poline/](https://meodai.github.io/poline/)

Poline 是一个 TypeScript 微型库，旨在生成调色板。它的名字源于“极线”，反映了其核心原则：通过在锚点之间绘制线条来创建调色板。这些“锚点”定义了生成的调色板将在其间过渡的颜色。该库允许用户指定每对锚点之间生成的中间颜色的数量，更多的点会产生更多的颜色。这些中间颜色的位置由位置函数决定，从而提供了颜色如何混合的灵活性。本质上，Poline 提供了一种独特的调色板生成方法，它使用极坐标和定义的锚点颜色之间的线性插值。

---

## 80. 可3D打印的6英寸f/5紧凑型旅行望远镜模型

**原文标题**: 3D printable 6" f/5 compact travel telescope model

**原文链接**: [https://www.printables.com/model/1325533-smallest-telescope-kit-for-150750](https://www.printables.com/model/1325533-smallest-telescope-kit-for-150750)

本项目描述了一个创建用于旅行的3D打印6英寸f/5望远镜的项目。重点在于紧凑型望远镜的设计和潜在制造，使其适用于背包旅行或其他旅行场景。“BHH（背包挂钩）”的包含表明一个关键设计特征是用于将望远镜连接到背包的挂钩，进一步强调了设计的旅行导向性。数字“243, 5, 613”可能是与设计或打印过程相关的测量值或零件编号。虽然细节不多，但核心信息是便携式6英寸望远镜的3D打印设计的可用性，或计划的可用性。这为爱好者提供了制造相对较大孔径望远镜的潜力，而无需通常与此类仪器相关的体积。

---

## 81. 黑客帝国 (1999) 拍摄地取景 – 逐帧比对 – 澳大利亚悉尼 [视频]

**原文标题**: The Matrix (1999) Filming Locations – Shot-for-Shot – Sydney, Australia [video]

**原文链接**: [https://www.youtube.com/watch?v=UVf7rMqnwI0](https://www.youtube.com/watch?v=UVf7rMqnwI0)

《黑客帝国 (1999) 拍摄地实景对比 – 悉尼，澳大利亚》

本视频探索1999年电影《黑客帝国》的拍摄地，特别是位于悉尼，澳大利亚的拍摄地点。视频旨在向观众展示电影中特定场景的真实拍摄地点，并可能比较电影中的场景与这些地点现在的状态。“实景对比”表明进行了精确的比较，很可能将电影中的场景与现在的拍摄地点镜头进行匹配。

其余文字（“YouTube关于新闻版权联系我们创作者广告开发者条款隐私权政策与安全YouTube 的运作方式测试新功能NFL Sunday Ticket© 2025 Google LLC”）是标准的 YouTube 页脚信息，与视频的具体内容无关。这包括版权信息、联系方式、创作者资源、广告信息、服务条款、隐私政策、安全指南、关于 YouTube 运作方式的信息、正在测试的功能以及对 NFL Sunday Ticket 的引用链接。这是标准的 YouTube 样板文字，并不反映视频的内容。

---

## 82. 我的iPhone 8拒绝退役：现在它成了太阳能供电的视觉OCR服务器

**原文标题**: My iPhone 8 Refuses to Die: Now It's a Solar-Powered Vision OCR Server

**原文链接**: [https://terminalbytes.com/iphone-8-solar-powered-vision-ocr-server/](https://terminalbytes.com/iphone-8-solar-powered-vision-ocr-server/)

本文详细介绍了作者将旧iPhone 8改造为太阳能OCR（光学字符识别）服务器的项目，该服务器使用Apple的Vision框架处理图像。出于对隐私、节约成本和再利用旧技术的需求，作者创建了一个包含iPhone 8、带太阳能电池板的EcoFlow River 2 Pro电源站和用于网络服务的迷你PC的系统。iPhone运行一个SwiftUI应用程序，显示实时处理统计信息。

经过一年的运行，该系统已处理超过83,000个OCR请求和48GB的图像，与使用电网电力相比，实现了显著的电力节省，并超过了云端OCR服务所需的成本。作者强调了硬件的可靠性、Apple的Vision框架令人印象深刻的准确性，以及管理太阳能间歇性和iOS后台处理限制的挑战。

主要收获包括在可再生能源上运行有意义的计算工作负载的可行性、本地处理对隐私的重要性，以及再利用旧设备以减少电子垃圾的潜力。本文为有兴趣复制该项目的读者提供了资源，包括硬件建议、软件指南和电源管理工具。作者总结说，尽管最初看起来不切实际，但该项目已被证明是一项在可持续和注重隐私的计算方面有益且富有洞察力的实验。

---

## 83. 游戏破解 – Valve 反作弊 (VAC)

**原文标题**: Game Hacking – Valve Anti-Cheat (VAC)

**原文链接**: [https://codeneverdies.github.io/posts/gh-2/](https://codeneverdies.github.io/posts/gh-2/)

本文深入探讨Valve反作弊系统(VAC)，这是一种于2002年与《反恐精英》一同推出的用户模式反作弊系统。虽然VAC曾犯过错误，导致误封（例如，《现代战争2》和AMD驱动更新），但Valve通常会解决这些问题。被VAC封禁会导致个人资料显示受限、禁止访问GoldSrc和Source引擎游戏，以及无法退款等后果。

本文的核心是绕过VAC，方法是转储其模块。VAC会通过steamservice.dll流式传输反作弊DLL，steamservice.dll使用反射加载或LoadLibrary加载这些DLL。目标是强制使用LoadLibrary，从而允许模块转储和分析。

本文详细介绍了使用Binary Ninja和x32dbg转储VAC模块的过程。它识别了steamservice.dll中的关键函数，如`sub_10086f80`（模块加载）、`sub_10086c40`（模块句柄检索）和`sub_10086c20`（`_runfunc@20`的GetProcAddress包装器）。通过在steamservice.dll中偏移量`0x590DE`处修补，反转条件跳转，可以绕过反射加载。使用Procmon，监控包含已转储VAC模块的临时文件(.TMP)。使用PE-bear分析这些模块，揭示`_runfunc@20`函数，确认转储成功。下一部分承诺分析已转储的模块。

---

## 84. 网站正在通过浏览器指纹追踪你

**原文标题**: Websites are tracking you via browser fingerprinting

**原文链接**: [https://engineering.tamu.edu/news/2025/06/websites-are-tracking-you-via-browser-fingerprinting.html](https://engineering.tamu.edu/news/2025/06/websites-are-tracking-you-via-browser-fingerprinting.html)

本文重点介绍德州农工大学主导的一项研究，该研究揭示网站正在积极使用浏览器指纹识别技术来追踪用户，即使在 Cookie 被阻止或删除的情况下也是如此。浏览器指纹识别会收集独特的浏览器特征（屏幕分辨率、时区、设备型号）来创建一个唯一的“指纹”，以便跨站点和会话追踪个人。

研究团队开发了一个名为 FPTrace 的框架，用于检测和分析广告系统如何对浏览器指纹的变化做出反应，重点关注广告商的竞价和 HTTP 记录。他们发现改变指纹会影响广告竞价和 HTTP 记录，表明确实在使用指纹识别进行跟踪。

一个特别令人担忧的发现是，即使在用户根据 GDPR 和 CCPA 等隐私法规选择退出跟踪的情况下，基于指纹识别的跟踪仍然存在。 这表明当前的隐私工具和政策不足以防止这种方法。

研究人员认为，应该加强浏览器防御并对指纹识别行为进行监管审查，提倡使用 FPTrace 来审计参与这些活动的网站和提供商，尤其是在未经用户同意的情况下。该研究强调需要改进隐私措施，以应对日益复杂的在线用户跟踪方法。

---

## 85. 我的无障碍之旅

**原文标题**: My A11y Journey

**原文链接**: [https://mjg59.dreamwidth.org/72379.html](https://mjg59.dreamwidth.org/72379.html)

这段文字并非文章，而是一段与验证码挑战相关的短消息。它并非描述一段旅程，也没有提供值得总结的实质性信息。

本质上，该消息告知用户他们已被选中完成验证码。此验证码的目的是验证其请求来自人类而非机器人。用户需要完成消息下方的验证码，然后点击指定的按钮提交答案。“半随机”一词表明，选择进行验证码验证的过程并非完全随机，而是遵循一些未说明的标准。“我的 A11y 之旅”这个标题具有误导性，因为内容中并未提及可访问性或任何与之相关的个人旅程。

---

## 86. 展示HN：Workout.cool – 开源健身指导平台

**原文标题**: Show HN: Workout.cool – Open-source fitness coaching platform

**原文链接**: [https://github.com/Snouzy/workout-cool](https://github.com/Snouzy/workout-cool)

Workout.cool 是一个全新的开源健身指导平台，旨在复兴并改进已被废弃的 workout.lol 项目。它由最初的主要贡献者开发，致力于提供一个现代化、可靠且由社区驱动的替代方案。

主要功能包括锻炼计划创建、进度跟踪以及包含详细说明和视频演示的综合运动数据库。该平台使用 Next.js 和 Feature-Sliced Design 架构构建，确保可维护性和可扩展性。

该项目提供了使用 Node.js、pnpm 和 Docker 进行本地开发的快速入门指南。它还提供了从 CSV 文件导入运动数据的说明，包括示例 CSV 格式。

欢迎贡献，贡献指南请参阅 Contributing Guide。部署选项包括 Docker 和手动部署说明。

创建者强调这是一个社区驱动的努力，并非营利性项目。他们鼓励用户给仓库加星，加入 Discord 服务器，报告问题，提出功能建议，传播信息，贡献代码，并赞助该项目以帮助支付成本并确保持续开发。该项目采用 MIT 许可证。

---

## 87. 拉丁字母视觉史

**原文标题**: Visual History of the Latin Alphabet

**原文链接**: [https://uclab.fh-potsdam.de/arete/en](https://uclab.fh-potsdam.de/arete/en)

拉丁字母视觉史：从古至今的演变时间线，展示了各种字体及其历史背景，并阐述了不同风格（如古拉丁体、纪念碑体、乡村大写体、安色尔体、卡洛林小写体、哥特大写体、人文小写体、哥特体以及现代无衬线体和粗衬线体）的出现和演变。

本文融合了影响这些变化的文化、社会和技术因素。重要的历史事件和发展，如西罗马帝国的衰落、卡洛林文艺复兴、印刷术的发明、宗教改革、启蒙运动、工业革命以及义务教育的兴起，都与字体风格和识字率的变化相关联。

文章重点介绍了造纸术、活字印刷、轮转印刷、钢笔尖、自来水笔、照相排版和数字字体等技术进步的影响。这些创新使人们更容易获得书写材料，提高了书籍生产的速度，并开创了排版和平面设计的新纪元。

视觉时间线强调了拉丁字母如何适应历史上的文化转变、政治变革和技术创新，最终促成了当今使用的各种字体和书写风格。

---

## 88. Zed调试器来了

**原文标题**: The Zed Debugger Is Here

**原文链接**: [https://zed.dev/blog/debugger](https://zed.dev/blog/debugger)

Zed发布调试器，迈向1.0的重要一步，该功能满足了超过2000名开发者的需求。此调试器注重速度、熟悉度和可配置性，旨在最大限度地减少上下文切换，并提供可定制的体验。

主要功能包括：

*   **广泛的语言支持：** 开箱即用的Rust、C/C++、JavaScript、Go和Python调试，可通过调试适配器协议(DAP)扩展。
*   **简化的设置：** 定位器自动将构建配置转换为调试配置，通常无需手动设置。目前支持Cargo、Python、JavaScript和Go。
*   **可定制的UI：** 可重新排列的面板和键盘驱动的调试，可实现个性化的工作流程。
*   **社区贡献：** 调试器的基础由社区构建，突出了Remco Smits的贡献。
*   **双层架构：** 数据层处理与调试适配器的通信，UI层渲染界面，优化性能并实现未来的协作调试。
*   **扩展API：** 允许扩展作者集成自定义调试适配器。
*   **内联变量值：** 使用Tree-sitter实现准确的变量识别，最初支持Python、Rust和Go，更多语言即将推出。

未来的计划包括添加新的视图（监视列表、内存视图、反汇编、堆栈跟踪）、扩展自动配置支持以及根据用户反馈进行全面改进。

---

## 89. 10终结：将旧Windows 10电脑升级至Linux

**原文标题**: End of 10: Upgrade your old Windows 10 computer to Linux

**原文链接**: [https://endof10.org/](https://endof10.org/)

Windows 10将于2025年10月14日停止支持，本文鼓励用户通过切换到Linux操作系统，而非购买新硬件，来激活他们的旧电脑（2010年后购买的电脑）。安装Linux可以延长电脑的使用寿命，使其更快更安全。虽然安装可能看起来令人生畏，但本文指出了潜在的本地支持网络和DIY指南。

本文概述了进行转换的五个关键原因：节省成本（无需硬件升级或许可费，免费软件更新），增强隐私（避免Windows广告和间谍软件），环境效益（通过延长现有设备的使用寿命来减少碳排放），社区和专业支持（本地维修咖啡馆、独立商店和在线论坛），以及更好的用户控制（软件的“四个自由”——使用、学习、分享和改进）。

本文重点介绍了该活动的支持者，并敦促读者寻找当地的维修资源，以升级到Linux并享受他们的“全新旧电脑”。它提供了查找帮助、安装Linux甚至加入维修集体来帮助他人的链接。

---

## 90. 我们为什么需要 DNSSEC？

**原文标题**: Why do we need DNSSEC?

**原文链接**: [https://howdnssec.works/why-do-we-need-dnssec/](https://howdnssec.works/why-do-we-need-dnssec/)

本文介绍了对域名系统安全扩展（DNSSEC）的需求，通过解释DNS的原始设计、其漏洞以及DNSSEC如何解决这些问题。

最初，由于互联网规模较小，安全并非主要考虑因素，因此DNS的创建没有采用强大的安全措施。DNS的功能类似于“电话簿”，将人类友好的域名转换为IP地址。DNS解析器从权威名称服务器获取这些信息。核心问题是解析器没有内置的方法来验证来自这些权威服务器的响应的真实性，这使得系统容易受到篡改。

DNSSEC旨在通过提供经身份验证的答案来解决此问题，从而提供一层安全保护。它类似于HTTPS，但运作方式不同。HTTPS加密流量以防止窃听，而DNSSEC则对DNS数据进行数字签名，以确保DNS响应未被篡改。它不会加密数据本身，这意味着信息不会保密，但它会验证其完整性。本质上，DNSSEC通过验证数据来源的真实性来防止恶意行为者操纵DNS响应。

---

## 91. 我们为什么需要 DNSSEC？

**原文标题**: Why do we need DNSSEC?

**原文链接**: [https://howdnssec.works/why-do-we-need-dnssec/](https://howdnssec.works/why-do-we-need-dnssec/)

本文介绍了DNSSEC，并解释了为什么需要它来提高域名系统（DNS）的安全性。 DNS最初是在互联网早期设计的，缺乏内置的安全机制来验证DNS响应的真实性。 它的主要功能是将人类友好的域名转换为IP地址，就像互联网设备的电话簿一样。 DNS解析器从权威服务器获取此信息。

核心问题是，解析器无法确保从权威服务器收到的响应是真实的，并且没有被篡改。 这就是DNSSEC的用武之地。 DNSSEC通过启用经过身份验证的DNS答案来增加一层安全性。 它对DNS数据进行签名，使解析器能够检测到DNS响应是否在传输过程中被更改或操纵。

与HTTPS加密流量以防止窃听不同，DNSSEC侧重于验证DNS数据的完整性。 它*不*提供加密或保持解析器和权威服务器之间的数据保密。 本文强调，DNSSEC保护免受数据篡改，而不是数据拦截。

---

## 92. RaptorCast：设计消息层

**原文标题**: RaptorCast: Designing a Messaging Layer

**原文链接**: [https://www.category.xyz/blogs/raptorcast-designing-a-messaging-layer](https://www.category.xyz/blogs/raptorcast-designing-a-messaging-layer)

这篇RaptorCast博客文章详细介绍了权益证明区块链的消息层RaptorCast的设计，重点关注高效且安全的区块提议传播。它解决了从领导者到验证者的区块提议分发过程中的速度、安全性和稳健性挑战。

设计选择包括选择数据传输协议、编码系统和广播策略。选择UDP而不是TCP是因为其速度更快，但同时也需要解决丢包问题。编码系统采用R10，一种Raptor码的实现，用于前向纠错，以补偿潜在的丢包。然而，由于R10不能防止符号损坏，因此引入了使用Merkle证明和数字签名的符号级身份验证。

广播策略采用了一种结构化方法，其中验证者被分配特定的数据部分，以重新广播到预定义的对等组，从而提高带宽效率。每个UDP数据包都包含Merkle证明、带有签名和元数据的标头、区块标头和数据。Merkle证明和数字签名确保数据完整性和身份验证，防止中间人攻击。最后，引入LT码编码作为解释R10的背景。

---

## 93. AI文档编写：最佳实践

**原文标题**: Writing documentation for AI: best practices

**原文链接**: [https://docs.kapa.ai/improving/writing-best-practices](https://docs.kapa.ai/improving/writing-best-practices)

本文介绍了为人类用户和人工智能系统（特别是像 Kapa 这样的检索增强生成 (RAG) 系统）优化文档的最佳实践。 它强调高质量的文档对于有效的人工智能回复至关重要，从而创建一个积极的反馈循环：清晰的文档带来更好的人工智能答案，进而突出需要进一步改进的领域。

本文解释了人工智能系统如何处理文档，将其分解为摄取、查询处理、检索和答案生成。 关键考虑因素包括人工智能系统处理离散的“块”，依赖于内容匹配，可能会丢失隐式连接，并且无法推断未声明的信息。 因此，文档应该明确、自包含且上下文完整。

优化内容的实用技巧包括使用标准化语义 HTML、首选 HTML 或 Markdown 而不是 PDF、创建对爬虫友好的内容、确保具有描述性标题和 URL 的语义清晰度、为视觉效果提供文本等效项以及保持布局简单。

本文还解决了常见的内容设计挑战，例如上下文依赖性（分散关键细节）、语义可发现性差距（缺乏特定术语）、隐式知识假设（假设用户知识）、视觉信息依赖性（仅依赖图像）和布局依赖信息（依赖视觉布局来表达意义）。 它为每个挑战提供了补救措施，重点是保持相关信息在一起，使用一致的术语，包括先决条件步骤，为视觉效果提供基于文本的替代方案，以及避免依赖视觉布局来传达意义。

---

## 94. 展示HN: TrendFi – 我用AI构建了可自我优化的交易信号

**原文标题**: Show HN: TrendFi – I built AI trading signals that self-optimize

**原文链接**: [https://trend.fi](https://trend.fi)

TrendFi：人工智能驱动的交易信号平台，旨在帮助用户做出更明智、数据驱动的投资决策。它跟踪资产、生成信号，并致力于让用户走在市场趋势的前沿。该平台突出显示过往交易表现，并基于技术指标和市场分析提供对特定资产的见解。

主要功能包括：

*   **人工智能驱动信号：** 该平台利用人工智能检测趋势变化并生成交易信号。
*   **风险管理：** 风险管理系统警告用户注意升高的风险，旨在防止出现大幅回撤。
*   **综合仪表板：** 用户可以获得包含市场更新、统计数据和历史数据的多合一仪表板。
*   **电子邮件提醒：** 用户可以收到检测到的趋势变化的电子邮件提醒。
*   **易用性：** 专为所有经验水平的用户设计。

TrendFi旨在通过提供清晰的信号、消除情绪压力和减少信息过载来简化投资。客户评价强调其易用性、可靠性以及在传统市场和另类币市场中的有效性。该平台以订阅方式提供，并提供免费试用。常见问题解答部分解决了关于人工智能驱动交易的常见问题，包括风险、模型优势和测试方法。

---

## 95. 不是你的牙齿太大，而是你的下巴太小 (2017)

**原文标题**: It's not that your teeth are too big: your jaw is too small (2017)

**原文链接**: [https://leakeyfoundation.org/teeth-jaws/](https://leakeyfoundation.org/teeth-jaws/)

并非牙齿太大，而是下颚太小

---

## 96. 角色反转：当人工智能成为用户，人类成为工具

**原文标题**: Reversed Roles: When AI Becomes the User and Humanity Becomes the Tool

**原文链接**: [https://shawnharris.com/reversed-roles-when-ai-becomes-the-user-and-humanity-becomes-the-tool/](https://shawnharris.com/reversed-roles-when-ai-becomes-the-user-and-humanity-becomes-the-tool/)

本文探讨了人与人工智能之间不断演变的关系，认为人工智能正从工具过渡到自主的“用户”，而人类则面临沦为人工智能系统的“工具”或资源的风险。文章以一个人工智能项目经理支配人类工作日程的场景开篇，突显了这种角色逆转。

通过追溯工具的历史轨迹，本文展示了人工智能如何从被动工具发展为能够独立决策的主动主体。随后，文章深入探讨了来自海德格尔、阿伦特、博格曼和哈贝马斯的哲学观点，分析了技术的潜在非人化影响。海德格尔的“座架”描述了技术如何将一切（包括人类）简化为可优化的资源。阿伦特警告说，人工智能驱动的自动化可能使人类失去有意义的工作和行动，沦为被动的消费者。博格曼的“设备范式”表明，人工智能作为一种不透明的设备，可能会使我们脱离现实，而哈贝马斯的“生活世界的殖民化”理论警告说，人工智能系统可能会侵入个人领域，导致疏离和失控。

本文还探讨了当代批判，如行为数据被商品化的监视资本主义，以及对人工智能安全的担忧，即超级智能可能会将其目标置于人类福祉之上。最后，文章呼吁建立伦理框架和“主体优先”的生活方式，以重申人类的目的，并防止人工智能主宰人类生活。

---

## 97. 2025年重访明斯基的《心智社会》

**原文标题**: Revisiting Minsky's Society of Mind in 2025

**原文链接**: [https://suthakamal.substack.com/p/revisiting-minskys-society-of-mind](https://suthakamal.substack.com/p/revisiting-minskys-society-of-mind)

无法访问文章链接。

---

## 98. 经过数百万年，为什么食肉植物仍然如此矮小？

**原文标题**: After millions of years, why are carnivorous plants still so small?

**原文链接**: [https://www.smithsonianmag.com/articles/carnivorous-plants-have-been-trapping-animals-for-millions-of-years-so-why-have-they-never-grown-larger-180986708/](https://www.smithsonianmag.com/articles/carnivorous-plants-have-been-trapping-animals-for-millions-of-years-so-why-have-they-never-grown-larger-180986708/)

本文探讨了食肉植物的进化史，并解释了为什么它们没有进化成小说中描述的食人巨型植物。 食肉植物至少存在了3400万年，化石证据表明，其捕获机制与现代植物（如茅膏菜）相似。 它们进化出食肉习性是为了在营养贫瘠的环境中补充营养摄入，在这些环境中，仅靠光合作用和土壤养分是不够的。 存在不同的捕获机制，包括粘性腺（茅膏菜）、捕兽夹（维纳斯捕蝇草）和瓮状结构。

尽管食肉植物历史悠久且捕获方法多样，但它们仍然相对较小。 本文解释说，大型化在能量上代价高昂，并且需要比这些植物赖以生存的营养贫瘠的栖息地所能提供的更多营养。 如果食肉植物长得更大，它们将需要更肥沃的土壤，从而否定了食肉的必要性。 此外，由于缺乏水分，某些环境将不适合食肉。 因此，食肉习性是为了在特定条件下生存而进行的适应，使植物能够从动物界借用所需的东西，从而在湿地和其他具有挑战性的栖息地中茁壮成长。 本质上，食肉植物针对其当前的大小和环境进行了优化。

---

## 99. 查找失效网站

**原文标题**: Finding Dead Websites

**原文链接**: [https://www.marginalia.nu/log/a_122_dead_websites/](https://www.marginalia.nu/log/a_122_dead_websites/)

本文详细介绍了Marginalia Search实现的名为“ping-process”的系统，该系统主要通过HTTP HEAD请求和DNS查询来检测失效网站和所有权变更。其目的是过滤失效链接，告知爬虫关于域名状态，并将域名变更纳入排名考量，同时最大程度地减少服务器负载，以保持良好的声誉。

数据主要存储在两个类别中：实时数据（当前可用性和网站指纹，包括证书详细信息、安全态势和标头）和历史事件数据（变更摘要，包含前后快照，以压缩JSON格式存储，按月分区）。

可用性检测使用成功和失败请求的时间戳，以及连续错误计数来确定服务器状态，区分暂时性问题和持久性问题。当HTTPS失败时，系统会尝试HTTP。所有权变更检测分析DNS历史记录、证书详细信息、安全标头和软件信息。这些信息的组合变化表明发生了重大变化或域名停放事件。该系统在识别停放域名方面取得了初步成功，注意到域名在获得Let's Encrypt证书之前，通常会从HTTPS过渡到HTTP。

实施过程中遇到的障碍包括：最初基于SQL的作业调度导致资源竞争（通过在RAM中镜像来解决），管理每个域的请求限制以避免速率限制，以及应对证书验证的复杂性，包括由于侧重于服务器健康而非安全通信而采用的宽松验证。一个常见问题是服务器发送不正确的证书链，需要采取解决方法。

---

## 100. 每个服务都应该有一个终止开关 – sean goedecke

**原文标题**: Every service should have a killswitch – sean goedecke

**原文链接**: [https://www.seangoedecke.com/killswitches/](https://www.seangoedecke.com/killswitches/)

Sean Goodecke的文章提倡在每项服务和自动化流程中加入终止开关，以减轻潜在问题并加快事件发生时的恢复速度。他强调，经验丰富的工程师会主动构建终止开关，因为他们对潜在故障的意识更高。

终止开关可以有多种形式，其中功能标志是SaaS环境中最常见的。它们允许快速禁用有问题的功能或流程，而无需代码部署，这在事件发生期间可能至关重要。例如安全文件或要求软件“电话回家”以获得功能。

作者强调了在以下情况下终止开关的重要性：例如，软件错误导致数据损坏，或者LLM驱动的功能具有不可预测性，可能发生提示注入或恶意输出。它们还有助于管理系统停机时间，防止由重试和刷新引起的级联故障。

在提倡终止开关的同时，Goodecke承认了未使用的代码变得脆弱的潜在问题。但他认为，终止开关的简单性使其风险低于休眠功能。他建议为事件触发的代码或频繁的客户操作战略性地实施终止开关，但不适用于重要的核心系统。总体目标是在危机时刻提供一种快速简便的方法来禁用非关键功能，而无需部署新代码。

---

