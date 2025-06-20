# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-06-20.md)

*最后自动更新时间: 2025-06-20 17:51:18*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 2 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 3 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 4 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 5 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 6 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 7 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 8 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 9 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 10 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 11 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 12 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 13 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 14 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 15 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 16 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 17 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 18 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 19 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 20 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 21 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 22 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 23 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 24 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 25 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 26 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 27 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 28 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 29 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 30 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 31 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 32 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 33 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 34 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 35 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 36 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 37 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 38 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 39 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 40 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 41 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 42 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 43 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 44 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 45 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 46 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 47 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 48 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 49 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 50 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 51 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 52 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 53 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 54 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 55 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 56 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 57 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 58 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 59 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 60 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 61 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 62 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 63 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 64 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 65 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 66 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 67 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 68 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 69 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 70 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 71 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 72 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 73 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 74 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 75 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 76 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 77 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 78 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 79 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 80 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 81 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 82 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 83 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 84 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 85 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 86 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 87 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 88 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 89 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 90 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 91 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 92 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 93 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
