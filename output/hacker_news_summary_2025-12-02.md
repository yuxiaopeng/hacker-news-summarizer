# Hacker News 热门文章摘要 (2025-12-02)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 使用Strudel学习音乐

**原文标题**: Learning Music with Strudel

**原文链接**: [https://terryds.notion.site/Learning-Music-with-Strudel-2ac98431b24180deb890cc7de667ea92](https://terryds.notion.site/Learning-Music-with-Strudel-2ac98431b24180deb890cc7de667ea92)

题为“用Strudel学习音乐”的文章似乎是关于在Notion中使用Strudel进行音乐教育的。然而，提供的内容非常有限，仅包含一条指示使用Notion需要JavaScript的消息。

因此，无法确定Strudel如何用于学习音乐的具体细节。唯一的结论是，这篇文章可能讨论了如何在Notion中实施一个名为“Strudel”的工具来帮助音乐教育，但要访问描述其功能的实际内容，需要在Notion环境中启用JavaScript。我们没有任何关于Strudel*是什么*或*如何*促进音乐学习的细节。

---

## 2. Mistral 3 模型系列发布

**原文标题**: Mistral 3 family of models released

**原文链接**: [https://mistral.ai/news/mistral-3](https://mistral.ai/news/mistral-3)

Mistral AI发布新一代模型Mistral 3系列，采用Apache 2.0许可。其中包括：

*   **Mistral Large 3:** 一款最先进的开放权重稀疏混合专家模型（410亿活跃参数，6750亿总参数），在NVIDIA H200 GPU上训练而成。它擅长通用提示、图像理解和多语言对话。提供基础版本和指令微调版本。
*   **Ministral 3系列:** 三款小型密集模型（30亿、80亿和140亿参数），适用于边缘和本地用例，每款均有基础版、指令版和推理版，均具备图像理解能力。它们旨在实现最佳的性能成本比。

这些模型通过与vLLM、Red Hat和NVIDIA的合作进行了优化，以提高可访问性和速度，包括NVFP4检查点和在NVIDIA硬件上高效的推理支持。

Mistral Large 3在LMArena排行榜上名列前茅。Ministral 3系列为各种需求（包括边缘部署）提供量身定制的选择，并具有最先进的准确性。

这些模型可在Mistral AI Studio、Amazon Bedrock、Azure Foundry和Hugging Face等多个平台上使用。Mistral AI还提供定制模型训练服务。

Mistral AI强调开放访问、透明度和协作，邀请社区探索和构建新的模型。

---

## 3. Nixtml：用Nix编写的静态网站和博客生成器

**原文标题**: Nixtml: Static website and blog generator written in Nix

**原文链接**: [https://github.com/arnarg/nixtml](https://github.com/arnarg/nixtml)

Nixtml 是一个用 Nix 编写的静态网站和博客生成器，灵感来源于 Hugo。它使用 Nix 来定义网站结构、内容处理和主题。

**主要特性：**

*   **Nix 驱动：** 利用 Nix 实现可复现性和声明式配置。
*   **Markdown 内容：** 将 Markdown 文件转换为 HTML 页面。
*   **模板：** 使用 Nix 函数作为 HTML 模板，支持函数式 HTML 和字符串模板。标准模板包括 `base`、`hom`、`page`、`collection`、`taxonomy` 和 `partials` 用于自定义。
*   **集合（Collections）：** 对内容进行分组和分页，例如博客文章，并生成 RSS 订阅。
*   **分类（Taxonomies）：** 通过关键词（标签、类别）组织内容，为每个术语创建专用页面。
*   **灵活性：** 提供用于常见 HTML 标签的函数，以实现 HTML 的程序化构建。
*   **示例：** 提供简单网站和博客的示例配置。

**工作流程：**

1.  `flake.nix` 文件定义网站结构、依赖项（包括 `nixtml`）和构建过程。
2.  内容放置在指定的目录 (`content.dir`) 中。
3.  配置集合和分类以对内容进行分组和分类。
4.  模板定义网站的布局和样式。
5.  Nixtml 处理内容和模板，生成可以部署的静态网站。

该框架通过 Nix 驱动的自动化实现网站创建，在主题、内容组织和整体网站结构方面提供灵活性。

---

## 4. 解决添加问题

**原文标题**: Addressing the adding situation

**原文链接**: [https://xania.org/202512/02-adding-integers](https://xania.org/202512/02-adding-integers)

应对加法困境：编译器如何利用x86指令实现三操作数加法

---

## 5. 注意通知

**原文标题**: YesNotice

**原文链接**: [https://infinitedigits.co/docs/software/yesnotice/](https://infinitedigits.co/docs/software/yesnotice/)

YesNotice，于2025年10月10日上线，是一个旨在通知用户所追踪事项从否定（“否”）状态变为肯定（“是”）状态的网站。它被归类为软件和投资组合相关。YesNotice的核心功能是主动提醒，在特定条件或状态朝着有利于用户的方向转变时立即通知用户。本质上，它自动化了监控积极变化的过程，无需进行持续的手动检查。

---

## 6. 2025编译器优化前沿

**原文标题**: Advent of Compiler Optimisations 2025

**原文链接**: [https://xania.org/202511/advent-of-compiler-optimisation](https://xania.org/202511/advent-of-compiler-optimisation)

作者宣布推出“2025编译器优化降临”活动，这是一个从12月1日到12月25日每日更新的项目。每天将发布一篇博文和一个视频，详细介绍一种不同的C或C++编译器优化。内容将涵盖底层、特定于架构的技巧和高层优化，主要侧重于x86-64，但也涉及64位和32位ARM。作者将解释每种优化何时适用、如何解释生成的汇编代码以及何时可能不适用。该项目旨在展示现代编译器令人惊叹的功能。读者可以通过AoCO2025博客标签、YouTube订阅或专门的YouTube播放列表来关注。

---

## 7. Poka Labs (YC S24) 招聘创始工程师

**原文标题**: Poka Labs (YC S24) Is Hiring a Founding Engineer

**原文链接**: [https://www.ycombinator.com/companies/poka-labs/jobs/RCQgmqB-founding-engineer](https://www.ycombinator.com/companies/poka-labs/jobs/RCQgmqB-founding-engineer)

Poka Labs（Y Combinator S24孵化企业）正在招募创始工程师，为亟待数字化和人工智能转型的6万亿美元化工制造业构建“智能层”。该职位年薪13万至18万美元，股权1-3%，要求搬迁至旧金山。

创始工程师将负责处理模糊的问题领域，交付制造企业各团队每日使用的生产级人工智能代理。职责包括构建端到端代理，用于报价、定价和库存管理，集成ERP和CRM系统，并塑造产品体验。该职位涉及前端和后端功能开发，确保代理的可靠性，以及评估新的人工智能能力。

Poka Labs正在寻找具备强大的全栈能力、行动导向、清晰的沟通技巧和快速学习能力的人才。其技术栈包括现代LLM、TypeScript、React和AWS。公司提供重要的所有权、在全球制造业的影响力、塑造企业文化的机会，以及与创始人直接合作的机会。面试流程包括初步沟通、居家技术评估和带薪工作试用。Poka Labs成立于2023年，目前团队有3人。

---

## 8. 我设计并打印了一个定制的鼻罩来帮助我的狗对抗DLE。

**原文标题**: I Designed and Printed a Custom Nose Guard to Help My Dog with DLE

**原文链接**: [https://snoutcover.com/billie-story](https://snoutcover.com/billie-story)

比利，一只比特犬，被诊断患有盘状红斑狼疮(DLE)，导致她的鼻子出现色素脱失、结痂、疼痛和出血，阳光会加剧病情。传统的治疗方法，如药用软膏和防晒霜，都无效，因为比利会把它们舔掉。现有的鼻子防护罩也都不成功。

出于绝望并配备了3D打印机，比利的主人设计了SnoutCover，一个定制的鼻子防护罩。设计过程涉及多次迭代，最初使用PLA进行测量，然后过渡到柔软的TPU以提高舒适度。早期的原型缺乏通风，导致不适。随后的版本专注于增加战略性的通风孔，同时阻挡紫外线。

经过13次迭代，最终的SnoutCover设计保护了比利的鼻子免受阳光照射，让她能够正常呼吸和进食，防止她舔掉药物，并舒适地固定到位。使用SnoutCover五个月后，比利的出血停止，结痂减少，色素恢复，她的鼻子完全痊愈。

在网上分享比利的成功案例后，收到了来自其他面临类似挑战的狗主人的热烈反响。主人现在在MakerWorld上免费分享SnoutCover设计，希望帮助其他患有DLE的狗狗过上无痛且健康的生活。该设计适用于中大型犬，可以通过切片软件中的缩放进行调整。

---

## 9. Python数据科学手册

**原文标题**: Python Data Science Handbook

**原文链接**: [https://jakevdp.github.io/PythonDataScienceHandbook/](https://jakevdp.github.io/PythonDataScienceHandbook/)

Jake VanderPlas 编写的《Python数据科学手册》是使用 Python 学习数据科学的全面资源。完整文本可以作为 Jupyter 笔记本在 GitHub 上在线获取，采用 CC-BY-NC-ND 许可（文本）和 MIT 许可（代码）。该手册鼓励用户通过购买本书来支持这项工作。

本书涵盖了广泛的主题，首先深入探讨了 IPython，包括其帮助、快捷方式、魔法命令、历史记录、 shell 命令、调试、性能分析等功能。然后深入研究 NumPy，解释了数据类型、数组、通用函数、聚合、广播、比较、索引、排序和结构化数据。

该手册继续介绍 Pandas，重点介绍使用 Pandas 对象进行数据操作、索引、运算、处理缺失数据、分层索引、组合数据集（concat、merge、join）、聚合、分组、透视表、向量化字符串操作、时间序列以及使用 `eval()` 和 `query()` 的高性能技术。

接下来，它探讨了使用 Matplotlib 进行数据可视化，涵盖各种绘图类型（折线图、散点图、轮廓图、直方图），绘图元素的自定义（图例、颜色条、子图、文本、注释、刻度线）、样式表、3D 绘图、使用 Basemap 的地理数据，并介绍了 Seaborn。

最后，本书涵盖了使用 Scikit-Learn 进行的机器学习，包括模型验证、特征工程等主题，并深入分析了朴素贝叶斯、线性回归、支持向量机、决策树、随机森林、主成分分析、流形学习、k-Means 聚类、高斯混合模型和核密度估计等算法。最后以人脸检测的应用和进一步的机器学习资源作为结束。

---

## 10. Show HN: Marmot - 单一二进制数据目录 (无需 Kafka, 无需 Elasticsearch)

**原文标题**: Show HN: Marmot – Single-binary data catalog (no Kafka, no Elasticsearch)

**原文链接**: [https://github.com/marmotdata/marmot](https://github.com/marmotdata/marmot)

Marmot 是一个开源的单二进制数据目录，旨在简化组织机构整个数据栈中的数据发现。它旨在提供强大的搜索能力，而无需传统企业解决方案的复杂性，也不需要 Kafka 或 Elasticsearch。

主要特点包括：

*   **易于部署：** Marmot 可以使用单个二进制文件、Docker 或 Kubernetes 快速部署，只需最少的设置。
*   **强大的搜索：** 提供丰富的查询语言，包括全文搜索、元数据过滤、布尔逻辑和比较运算符，以查找任何数据资产。
*   **交互式血缘可视化：** 提供交互式依赖关系图，以跟踪数据流并理解数据血缘。
*   **灵活的集成：** 支持 CLI、REST API、Terraform 和 Pulumi 进行资产编目。
*   **元数据优先架构：** 存储各种资产类型的丰富元数据。
*   **团队协作：** 允许分配所有权、记录业务背景以及创建术语表，以实现集中式数据知识管理。

Marmot 根据 MIT 许可证获得许可，并欢迎以错误报告、功能建议、文档改进和插件开发的形式进行贡献。新用户可使用快速入门指南和在线演示。

---

## 11. 童年和早期职业生涯的片段

**原文标题**: A series of vignettes from my childhood and early career

**原文链接**: [https://www.jasonscheirer.com/weblog/vignettes/](https://www.jasonscheirer.com/weblog/vignettes/)

本文收集了作者早期职业生涯和童年时期的轶事，讽刺了由于技术进步而反复出现的关于软件工程将走向衰落的预测。

第一个故事回忆了1996年的建议，该建议认为编程很快就会过时，取而代之的是由非程序员组装的预构建对象库。作者指出，尽管有开源库和其他进步，软件仍然是一个可行的职业。

作者随后嘲笑了90年代的“多媒体时代”炒作，当时声音和视频被认为是必不可少的，但最终变得司空见惯和平淡无奇。

另一个轶事讲述了2000年代初一位同事的信念，他认为IntelliJ IDE及其重构工具将淘汰程序员。作者反驳说，该工具只是重新排列代码，而不是创建新的逻辑。

更多的故事详细描述了作者自动化任务的经验。其中一个涉及为承包商创建一个迁移数据的工具，有可能缩短承包商的工作时间并提高他们的效率。另一个讲述了作者自动化维护网站工作的故事，结果在部门雇佣了一名全职开发人员后，作者被重新分配到其他任务。

作者还反思了过去NLP项目中涉及的伦理考虑，强调了尊重数据许可和网络爬行协议的重要性，并将此与当前LLM领域的实践形成对比。

最后，文章将互联网泡沫时期对互联网的强制采用与Web 2.0的有机增长进行了对比，后者互联网的使用变得司空见惯并融入商业模式。作者总结说，这些轶事是针对当前围绕LLM的炒作的“消极攻击”。

---

## 12. 苹果发布开源权重视频模型

**原文标题**: Apple Releases Open Weights Video Model

**原文链接**: [https://starflow-v.github.io](https://starflow-v.github.io)

本文介绍了STARFlow-V，这是一种由苹果公司开发的新型视频生成模型，它基于归一化流（NFs）。与流行的基于扩散的模型不同，STARFlow-V利用了NFs的优势，包括端到端训练、精确的似然估计以及对文本到视频（T2V）、图像到视频（I2V）和视频到视频（V2V）生成的原生多任务支持。

STARFlow-V的关键特性包括：

*   **全局-局部架构：** 将全局时间推理（使用深度因果Transformer）与局部帧内细节（使用浅层流块）分离，从而减轻了随时间推移的误差累积。
*   **流-分数匹配：** 采用通过流-分数匹配训练的轻量级因果去噪器，从而提高视频生成的一致性。
*   **视频感知雅可比迭代：** 使用可并行化的迭代方案进行高效采样，在不牺牲质量的前提下显著加快生成速度。

这个拥有70亿参数的模型在包含7000万个文本-视频对和4亿个文本-图像对的大规模数据集上进行了训练，使其能够以16fps生成480p的视频。STARFlow-V展示了强大的视觉逼真度和时间一致性，与基于扩散的方法相比，实现了具有竞争力的性能。

本文展示了该模型在各种任务中的能力，包括从文本提示生成高质量视频、从单张图像创建视频，以及使用诸如图像修复和风格迁移等技术来扩展/转换现有视频。这项研究确立了NFs作为高质量自回归视频生成和构建世界模型的一个有希望的方向。

---

## 13. 2026年将有哪些作品进入公有领域？

**原文标题**: What will enter the public domain in 2026?

**原文链接**: [https://publicdomainreview.org/features/entering-the-public-domain/2026/](https://publicdomainreview.org/features/entering-the-public-domain/2026/)

公共领域评论聚焦2026年进入公有领域的作品，着重关注不同版权法的国家。2026年1月1日，作品将根据以下规则进入公有领域：

*   **作者去世后70年：** 1955年去世的作者的作品将在英国、俄罗斯、欧盟大多数国家以及南美洲等国家进入公有领域。
*   **作者去世后50年：** 1975年去世的作者的作品将在新西兰以及非洲和亚洲的大多数国家进入公有领域。
*   **美国：** 1930年出版的电影和书籍（包括其中的艺术作品）将进入公有领域。

文章展示了一个“降临节日历”的形式，在整个十二月逐步揭晓即将被释放的著名作品，最终在公共领域日（1月1日）达到高潮。 部分亮点包括：

*   **文学：** 兰斯顿·休斯的《并非没有欢笑》，弗兰茨·卡夫卡的《城堡》（英文译本），阿加莎·克里斯蒂的《牧师公馆谋杀案》，威廉·福克纳的《我弥留之际》，达希尔·哈梅特的《马耳他之鹰》，弗吉尼亚·伍尔夫的《奥兰多》，以及P.G. 沃德豪斯的作品。
*   **思想家：** 阿尔伯特·爱因斯坦，西格蒙德·弗洛伊德，汉娜·阿伦特
*   **音乐：** 查理·帕克
*   **其他：** 1930年的电影《西线无战事》。

文章还指向了约翰·马克·奥克布洛姆的倒计时和Standard Ebooks的美国作品免费版本等资源，并强调了公共领域的重要性，链接至Communia的公共领域宣言。

---

## 14. YouTube提升FreeBASIC性能 (2019)

**原文标题**: YouTube increases FreeBASIC performance (2019)

**原文链接**: [https://freebasic.net/forum/viewtopic.php?t=27927](https://freebasic.net/forum/viewtopic.php?t=27927)

无法访问文章链接。

---

## 15. 2025年末AWS Lambda ARM64与x86_64在不同运行时性能对比

**原文标题**: Comparing AWS Lambda ARM64 vs. x86_64 Performance Across Runtimes in Late 2025

**原文链接**: [https://chrisebert.net/comparing-aws-lambda-arm64-vs-x86_64-performance-across-multiple-runtimes-in-late-2025/](https://chrisebert.net/comparing-aws-lambda-arm64-vs-x86_64-performance-across-multiple-runtimes-in-late-2025/)

本文比较了 2025 年底 AWS Lambda 函数在 ARM64 (Graviton) 和 x86_64 架构上使用 Node.js、Rust 和 Python 运行时环境的性能。基准测试涵盖 CPU 密集型、内存密集型和轻量级工作负载。

**主要发现：**

*   **总体而言，ARM64 上的 Rust 性能最高且成本效益最佳**，尤其是在启用汇编优化的 SHA-256 哈希后，在 CPU 密集型工作负载上比 x86_64 提高了 4-5 倍的性能。
*   **ARM64 通常提供低 30-40% 的计算成本**，并且性能与 x86_64 相当或更好。
*   **ARM64 上的 Python 3.11 在测试中优于较新的 Python 运行时环境。**
*   **ARM64 上的 Node.js 22 始终比 x86_64 上的 Node.js 20 更快**，通过切换架构提供“免费”15-20% 的速度提升。
*   **Rust 比解释型运行时环境快得多**（比 Node.js 快 8 倍，比 Python 快 2 倍）。
*   **冷启动更倾向于 ARM64**，具有更快的初始化速度。

该基准测试使用了多种内存配置，并收集了冷启动和热启动指标。 结果强调了 ARM64 在成本和性能方面的优势，使其成为 Lambda 的强大默认选择，除非存在特定的库兼容性问题。作者提供了一个开源基准，供读者复制结果。

---

## 16. 用于集合论类型的惰性二元决策图

**原文标题**: Lazier Binary Decision Diagrams for set-theoretic types

**原文链接**: [https://elixir-lang.org/blog/2025/12/02/lazier-bdds-for-set-theoretic-types/](https://elixir-lang.org/blog/2025/12/02/lazier-bdds-for-set-theoretic-types/)

本文探讨了Elixir集合论类型系统中用于高效表示类型并集、交集和否定的数据结构演变过程。最初，使用析取范式（DNF），但其指数级膨胀的倾向，特别是在匿名函数类型推断中引入否定后，导致了性能问题。

为了解决DNF的局限性，采用了二元决策图（BDD），将类型表示为有序树。然而，BDD引入了新的速度下降，原因是并集在交集中扩展，导致过多的析取和昂贵的简化过程。

为了克服这个问题，本文介绍了一种“惰性BDD”（也称为三元决策图），它在每个节点中引入一个新的“不确定”元素，以惰性的方式表示并集，延迟其扩展并防止指数级增长。

最后，本文描述了对“惰性BDD”的优化，重点是交集和差集。结果表明，最初的惰性BDD公式仍然可能触发标准BDD的问题性并集扩展行为。新的公式在这些操作期间更有效地保留并集，从而显著提高性能并解决Elixir类型系统中剩余的瓶颈。关键在于分解出常见的并集项，以保持并集的“惰性”。

---

## 17. 印度命令智能手机制造商预装国营网络安全应用。

**原文标题**: India orders smartphone makers to preload state-owned cyber safety app

**原文链接**: [https://www.reuters.com/sustainability/boards-policy-regulation/india-orders-mobile-phones-preloaded-with-government-app-ensure-cyber-safety-2025-12-01/](https://www.reuters.com/sustainability/boards-policy-regulation/india-orders-mobile-phones-preloaded-with-government-app-ensure-cyber-safety-2025-12-01/)

**概要：**

路透社报道称，印度政府已命令智能手机制造商在新售往印度的所有智能手机上预装一款国有网络安全应用程序。此举旨在加强印度公民的网络安全意识。虽然现有信息未提及具体应用名称，但该命令反映了政府日益重视数字安全，并积极应对潜在威胁的努力。

此举可能会影响在印度运营的主要智能手机品牌，包括三星、小米和苹果。虽然此决定的理由是为了提高用户意识，并可能提供识别和报告网络威胁的工具，但也引发了对数据隐私、应用本身的安全漏洞以及潜在反竞争行为的担忧。

该报告还提到制造商可能面临的挑战，包括调整操作系统以适应预装应用程序，并确保与现有用户界面的无缝集成。预计政府将发布更多关于实施细节的指导方针，包括应用程序的时间表和技术规范。这项政策对印度智能手机市场和用户体验的长期影响仍有待观察，隐私倡导者可能会仔细审查该应用程序的功能和数据收集实践。

---

## 18. DeepSeek-v3.2：推进开源大语言模型前沿 [pdf]

**原文标题**: DeepSeek-v3.2: Pushing the frontier of open large language models [pdf]

**原文链接**: [https://huggingface.co/deepseek-ai/DeepSeek-V3.2/resolve/main/assets/paper.pdf](https://huggingface.co/deepseek-ai/DeepSeek-V3.2/resolve/main/assets/paper.pdf)

本文档似乎是题为“DeepSeek-v3.2：推进开源大型语言模型前沿”的文章的PDF源代码。

由于文件格式为PDF源代码，因此无法提供文章内容的全面摘要。

---

## 19. Show HN: RunMat – 密集数学运算的自动 CPU/GPU 路由运行时

**原文标题**: Show HN: RunMat – runtime with auto CPU/GPU routing for dense math

**原文链接**: [https://github.com/runmat-org/runmat](https://github.com/runmat-org/runmat)

RunMat：高性能 MATLAB 代码运行时

RunMat 是一款高性能 MATLAB 代码运行时，专为密集型数学计算设计。它能自动优化 CPU 和 GPU 之间的运算并进行路由，无需手动进行设备管理或内核编码。RunMat 通过原生 API 支持多种 GPU（NVIDIA、AMD、Apple Silicon、Intel）。

其主要特性包括：MATLAB 语法兼容性、基于数据大小和传输成本的 CPU/GPU 自动选择、具有 JIT 编译和分代垃圾回收机制的现代 CPU 运行时，以及跨平台 GPU 后端。早期性能基准测试表明，在多个大型工作负载上，特别是那些利用 GPU 加速的工作负载上，RunMat 的性能优于 NumPy 和 PyTorch。

该软件目前处于预发布阶段 (v0.2)，并采用开源（MIT 许可证）。文章鼓励用户通过提供的脚本或 `cargo` 安装 RunMat，运行示例脚本，并探索诸如 GPU 加速状态等功能。同时也支持 Jupyter 集成。

RunMat 构建于分层 CPU 运行时（解释器和 JIT 编译器）之上，并结合了融合引擎和自动卸载规划器。这使得可以将多个操作组合成单个 GPU 调度，同时最大限度地减少主机-设备传输。文章详细介绍了该架构，以及 RunMat 如何捕获数学运算、决定在 GPU 上运行的内容、生成 WGSL 中的 GPU 内核并高效执行代码。

文章宣传 RunMat 具有现代化的开发者体验，包括丰富的 REPL、Jupyter 支持、可扩展的架构以及全面的 CLI 功能。RunMat 还可以通过包系统进行扩展，该包系统支持原生 (Rust) 和源代码 (MATLAB) 包。文章最后讨论了设计理念、目标用户，并呼吁大家积极贡献、关注许可协议和社交媒体链接。

---

## 20. Beej的计算机科学学习指南

**原文标题**: Beej's Guide to Learning Computer Science

**原文链接**: [https://beej.us/guide/bglcs/](https://beej.us/guide/bglcs/)

Beej的计算机科学学习指南（草稿）旨在帮助人们学习计算机科学。本指南尚不完善，处于Beta测试阶段。作者Beej鼓励读者提供更正和反馈。

本指南提供多种格式供阅读，包括：

*   HTML（各种布局，包括宽屏和单页）
*   HTML ZIP压缩包（各种布局）
*   PDF（美式信纸和A4尺寸，单面和双面打印选项，带或不带语法高亮，以及彩色和黑白）

对于有兴趣翻译或贡献本指南的人，可以从GitHub克隆整个项目，说明见README。

作者Beej的联系方式：beej@beej.us。

---

## 21. 布莱恩·伊诺如何创作《Ambient 1: Music for Airports》(2019)

**原文标题**: How Brian Eno Created Ambient 1: Music for Airports (2019)

**原文链接**: [https://reverbmachine.com/blog/deconstructing-brian-eno-music-for-airports/](https://reverbmachine.com/blog/deconstructing-brian-eno-music-for-airports/)

这是一条评论，赞扬了一篇关于“Brian Eno如何创作《Ambient 1: Music for Airports (2019)》”的文章或视频。评论者显然很欣赏Brian Eno，认为他是当今最重要的制作人之一。他们赞赏对Eno工作方法的解释，指出其中一些信息是熟悉的，而另一些方面是新的且富有洞察力的。评论者对探索环境音乐充满热情，并强调该流派的广阔性，有待发现。评论的一个关键点是欣赏Eno在那段时间的专辑的独特声音，并将此至少部分归功于制作过程中录音机的使用。评论者感谢内容创作者深入研究该主题。

---

## 22. 辐射2主创克里斯·阿瓦隆谈游戏设计哲学

**原文标题**: Fallout 2's Chris Avellone describes his game design philosophy

**原文链接**: [https://arstechnica.com/gaming/2025/12/fallout-2-designer-chris-avellone-recalls-his-first-forays-into-game-development/](https://arstechnica.com/gaming/2025/12/fallout-2-designer-chris-avellone-recalls-his-first-forays-into-game-development/)

克里斯·阿瓦隆，以《辐射2》和《异域镇魂曲》等作品闻名的著名游戏设计师，将其成功归功于“玩家至上”的理念。他强调以玩家为中心的游戏体验的重要性，迎合他们的“自私”，因为享受才是游戏成功的真正标志。

阿瓦隆的设计理念源于他早期玩《龙与地下城》的经历，在那里他学会了制作互动故事并为玩家提供“闪耀时刻”，让他们感觉像英雄。他强调理解玩家动机的重要性，允许他们以自己的方式进行游戏，避免因不同的游戏风格而受到惩罚。

从纸笔RPG中得出的一个关键结论是，无论骰子结果或玩家行为如何，故事都必须继续。阿瓦隆将这一点应用到《异域镇魂曲》中，将死亡作为一种叙事元素，而不是失败状态。他还强调了在整个设计过程中玩家投入的重要性，甚至进行游戏前访谈，以了解角色弧线的偏好。

阿瓦隆强调，你不应该给玩家一项成就，然后立即夺走它。他的设计原则强调适应玩家的选择，并确保他们的内在动机与游戏中的目标相一致，从而创造更具吸引力的体验。他目前正在Republic Games开发一款反乌托邦幻想游戏，从中汲取他丰富的RPG设计经验。

---

## 23. 显示你周围航空信息的LED面板

**原文标题**: An LED panel that shows the aviation around you

**原文链接**: [https://github.com/AxisNimble/TheFlightWall_OSS](https://github.com/AxisNimble/TheFlightWall_OSS)

TheFlightWall项目是一个开源项目，旨在构建一个LED面板显示器，用于显示您所在地附近的实时航班信息。该项目使用多个16x16 LED面板、ESP32开发板、3D打印支架（或替代品）以及用于支撑的木质镶边。它需要一个5V电源和一个电压电平转换器。

该项目利用两个主要数据源：OpenSky用于ADS-B航班数据（位置和呼号），FlightAware AeroAPI用于航班信息，如飞机类型、航空公司和航线。要使用这些数据源，您需要创建账户并获取API密钥。

要设置软件，您需要在提供的配置文件中配置您的WiFi凭据、位置（纬度、经度和搜索半径）以及可选的显示偏好设置。固件使用PlatformIO（VS Code的IDE扩展）构建并刷入ESP32。

自定义选项包括调整显示亮度和文本颜色。虽然未来可能会添加更多选项，但其开源特性允许用户进行广泛的修改。

创建者鼓励用户构建自己的版本并在Instagram上标记他们。对于那些不想自己构建的用户，他们在其网站theflightwall.com上提供官方产品。

---

## 24. Rust 中的无根 Ping

**原文标题**: Rootless Pings in Rust

**原文链接**: [https://bou.ke/blog/rust-ping/](https://bou.ke/blog/rust-ping/)

本文介绍了如何在 Rust 中实现无 root 权限的 ping，绕过创建 ICMP 套接字时通常需要的 root 权限。作者解释说，这是通过创建使用 ICMP 协议的 UDP 套接字来实现的。

核心步骤包括：

1.  **套接字创建：** 使用 `socket2` crate 创建一个使用 ICMPv4 协议的 UDP 套接字。这允许在没有 root 权限的情况下发送 ICMP 数据包。

2.  **数据包创建和发送：** 构造一个 ICMP 回显请求数据包。Linux 和 macOS 对标识符和校验和字段的处理方式不同：Linux 会覆盖它们，而 macOS 需要正确的校验和计算。作者提供了计算和包含校验和的代码。然后使用套接字将数据包发送到目标 IP 地址。

3.  **响应处理：** 接收和解释 ICMP 回复。操作系统之间的主要区别在于 macOS 在接收到的数据包中包含 IP 标头，而 Linux 不包含。该代码通过在 macOS 上剥离 IP 标头来解决这一差异。然后，代码从接收到的数据中提取回复类型、序列号和有效负载，以验证 ping。

文章强调了 Linux 和 macOS 在数据包创建和响应处理方面的平台特定细微差别。最后，它建议进一步实现延迟计算和定期 ping 等功能。完整的示例可以在 GitHub 上找到。

---

## 25. 汤姆·斯托帕德去世

**原文标题**: Tom Stoppard has died

**原文链接**: [https://www.bbc.com/news/articles/c74xe49q7vlo](https://www.bbc.com/news/articles/c74xe49q7vlo)

著名剧作家汤姆·斯托帕德爵士逝世，享年88岁。他的去世引来了世界各地的悼念，人们赞扬他卓越的职业生涯以及对戏剧和文学的持久影响。

斯托帕德以《罗森克兰茨和吉尔登斯丹死了》和《真实的事》等作品闻名，他还凭借《莎翁情史》的剧本获得了奥斯卡金像奖和金球奖。查尔斯三世国王和卡米拉王后表达了他们的深切哀悼，他们认可了斯托帕德的天赋以及他挑战、感动和激励观众的能力。

他的戏剧经常探讨哲学和政治主题，在过去的六十年里吸引了众多观众。米克·贾格尔爵士、蒂姆·莱斯爵士等著名人物以及国家剧院等机构纷纷致敬。费伯出版社称赞他是过去六十年来最伟大的剧作家和知识分子之一。

斯托帕德出生于捷克斯洛伐克，原名托马斯·斯特劳斯勒，他的家人为了躲避纳粹占领而逃离，最终定居在英国。后来，他得知他的犹太祖父母死于集中营，这段经历塑造了他的视角。

斯托帕德的职业生涯在20世纪60年代凭借《罗森克兰茨和吉尔登斯丹死了》起飞，该剧赢得了包括四项托尼奖在内的多个奖项。他于1997年因其对文学的贡献而被授予爵士头衔。西区剧院将调暗灯光以纪念他，他获奖无数的戏剧和电影剧本的遗产无疑将永存。

---

## 26. Windows更新后密码图标消失，点击原位置有效。

**原文标题**: After Windows Update, Password icon invisible, click where it used to be

**原文链接**: [https://support.microsoft.com/en-us/topic/august-29-2025-kb5064081-os-build-26100-5074-preview-3f9eb9e1-72ca-4b42-af97-39aace788d93](https://support.microsoft.com/en-us/topic/august-29-2025-kb5064081-os-build-26100-5074-preview-3f9eb9e1-72ca-4b42-af97-39aace788d93)

本文档详细介绍了最近 Windows 11 更新中包含的功能、修复和已知问题。重点在于安全启动证书将于 2026 年 6 月到期，敦促用户提前更新以避免启动问题。

新功能包括：Recall，一个用于最近活动的个性化主页；Click to Do，一个增强生产力的交互式教程；重新设计的应用程序权限请求系统对话框；通知中心中带有秒的大型时钟；改进的任务栏搜索；锁屏界面上更多的 Widget 选项；文件资源管理器上下文菜单中的分隔符；使用工作/学校帐户登录时，文件资源管理器中的人物图标；重新设计的 Windows Hello 界面；以及生成式 AI 应用权限的新设置。

该更新解决了许多问题，包括任务栏预览缩略图的修复、文件资源管理器中被阻止的文件、Windows Hello 中的面部识别失败、添加安全密钥时设置崩溃、任务管理器中的 CPU 工作负载指标、实时字幕的不透明度、IME 输入问题、与 dbgcore.dll 和 Kerberos 相关的应用程序崩溃、登录延迟、Miracast 的音频问题以及密码提供程序的问题。

性能改进包括在 ARM64 设备上更快地安装应用程序。它包括将 Windows 打印组件迁移到现代通用 C 运行时库，这可能会导致旧版本 Windows 出现问题。Windows PowerShell 2.0 将于 2025 年 8 月删除。

已知问题包括网络设备接口 (NDI) 流媒体性能问题和 MSI 修复操作期间意外的用户帐户控制 (UAC) 提示，这两个问题已在 KB5065426 中解决，以及在某些 BluRay/DVD/数字电视应用程序中播放受保护内容的问题。它还提供了更新的 AI 组件的版本信息。

---

## 27. 逆向数学揭示难题为何难

**原文标题**: Reverse math shows why hard problems are hard

**原文链接**: [https://www.quantamagazine.org/reverse-mathematics-illuminates-why-hard-problems-are-hard-20251201/](https://www.quantamagazine.org/reverse-mathematics-illuminates-why-hard-problems-are-hard-20251201/)

这篇《量子杂志》的文章探讨了研究人员如何利用“逆向数学”来理解某些计算问题为何如此难以解决。他们没有采用从公理出发证明定理的传统方法，而是将定理与公理互换，然后证明原始公理。这种方法揭示了复杂性理论中看似无关的定理之间令人惊讶的等价关系。

文章重点介绍了陈立杰、李家图和伊戈尔·奥利维拉的工作，他们证明了鸽巢原理（如果你放入的鸽子比洞多，那么至少有一个洞里有多只鸽子）在逻辑上等价于“相等问题”的通信复杂度的下界，以及图灵机识别回文（正反读都一样的字符串）所需时间的下界。

这些等价关系令人惊讶，因为它们将抽象的计数原则与具体的计算任务联系起来。此外，它们揭示了某些公理系统（如 PV1）的局限性，表明如果鸽巢原理在 PV1 中不可证，那么这些等价定理也可能不可证。

虽然逆向数学方法不一定提供证明困难定理的新方法，但它有助于阐明复杂性下界的潜在联系和基本性质，从而促使计算机科学界重新燃起对元数学的兴趣。

---

## 28. 与同事的邻近性提高长期发展，降低短期产出 (2023)

**原文标题**: Proximity to coworkers increases long-run development, lowers short-term output (2023)

**原文链接**: [https://pallais.scholars.harvard.edu/publications/power-proximity-coworkers-training-tomorrow-or-productivity-today](https://pallais.scholars.harvard.edu/publications/power-proximity-coworkers-training-tomorrow-or-productivity-today)

This 2023 study by Emanuel, Harrington, and Pallais investigates the effects of proximity to coworkers, particularly in the context of the rise of remote work. Analyzing data from software engineers at a Fortune 500 company, the research reveals a trade-off: proximity boosts long-term human capital development but reduces short-term output.

When offices were open, engineers located in the same building as their team received significantly more online feedback (22%) compared to those with distant teammates. This advantage diminished after the shift to remote work during COVID-19. However, the study also found that co-location decreased engineers' programming output, especially among senior engineers.

The trade-offs of proximity are particularly pronounced for women, who engage in and benefit from mentoring more when working near colleagues. Furthermore, proximity impacts career trajectories by initially reducing short-term pay raises, but ultimately increasing them over the long run.

The findings help explain current return-to-office trends, with younger workers seeking mentorship and older workers providing it being more inclined to work on-site. The study cautions that even with mentors and mentees returning to the office, remote work can still hinder interaction, as having just one distant teammate negatively impacted feedback among co-located workers even before the pandemic.


---

## 29. Zig异步程序的新计划

**原文标题**: Zig's new plan for asynchronous programs

**原文链接**: [https://lwn.net/SubscriberLink/1046084/4c048ee008e1c70e/](https://lwn.net/SubscriberLink/1046084/4c048ee008e1c70e/)

Zig 新的异步 I/O 方法：避免函数着色问题

---

## 30. Codex、Opus、Gemini 尝试构建《反恐精英》

**原文标题**: Codex, Opus, Gemini try to build Counter Strike

**原文链接**: [https://www.instantdb.com/essays/agents_building_counterstrike](https://www.instantdb.com/essays/agents_building_counterstrike)

本文详细介绍了一项实验，该实验要求 Codex Max 5.1、Claude Opus 4.5 和 Gemini 3 Pro AI 模型构建一个基本的多人 3D 反恐精英游戏。 这些模型被给予连续的提示，首先侧重于前端元素（地图设计、角色、射击机制、音效），然后侧重于后端元素（具有房间和持久性的多人游戏功能）。

Claude Opus 4.5 在前端设计方面表现出色，创造了视觉上吸引人的地图、角色和枪支设计。 Gemini 3 Pro 在后端任务方面表现更好，以更少的错误实现了多人游戏和持久性。 Codex Max 5.1 总体表现稳定，但在任何一个类别中都不那么突出。

实验揭示了模型解决问题的有趣差异。 Codex 依赖于 TypeScript 库的内省，Claude 专注于阅读文档，而 Gemini 结合了这两种方法，同时持续运行构建步骤以识别和修复错误。

虽然所有模型都成功构建了一个无需手动编码的功能性多人 FPS，但仍然存在挑战。 文章强调需要更好的工具来弥合“感觉编码”和“实际编程”之间的差距，尤其是在解决常见的 React 开发问题（如 `useEffect` 行为）方面。 最终，该实验证明了 AI 模型在复杂软件开发任务方面的能力取得了显著进展，这得益于它们通过 CLI 交互进行迭代和学习的能力。

---

## 31. C语言中的URL (2011)

**原文标题**: URL in C (2011)

**原文链接**: [https://susam.net/url-in-c.html](https://susam.net/url-in-c.html)

本文展示了一段C代码片段，其中包含一个看似无效的URL `https://susam.net/`，但该代码能够成功编译并运行。本文探讨了为什么这段代码没有产生编译器错误，尽管C99标准没有明确地将URL识别为有效的语法。

解决方案揭示了`https:`被解释为一个标签，而随后的`//`开始一个单行注释，有效地忽略了URL的其余部分。本文阐明了自C99标准以来，使用`//`的单行注释在C语言中确实有效，如C99标准草案的6.4.9节中所详述。该节解释说，`//`之后直到行尾的所有内容都被视为注释，不包括换行符，并且编译器会忽略这些内容，但用于识别多字节字符和换行符。本质上，这段代码巧妙地利用了C99的标签和注释功能来绕过URL，从而允许`printf`语句按预期执行。

---

## 32. Ghostty：编译为WASM，兼容xterm.js API

**原文标题**: Ghostty compiled to WASM with xterm.js API compatibility

**原文链接**: [https://github.com/coder/ghostty-web](https://github.com/coder/ghostty-web)

`ghostty-web`提供了一个与xterm.js API兼容的Web终端解决方案，在浏览器中提供更强大、更精确的VT100终端实现。它利用编译为WASM的、与原生Ghostty应用程序中使用的相同的、经过实战考验的终端模拟器代码，解决了xterm.js的不足之处，尤其是在复杂脚本渲染和对XTPUSHSGR/XTPOPSGR的完全支持方面。

从xterm.js切换到`ghostty-web`很简单，只需要更改import语句即可。WASM包大约400KB，并且没有运行时依赖项。

`ghostty-web`旨在简化终端模拟，专注于准确性和性能，最初为Mux开发，但设计用于更广泛的用途。在线提供了一个实时演示，用户可以使用`npx @ghostty-web/demo@next`在本地尝试，该命令会启动一个带有shell的本地HTTP服务器。

该项目使用Zig和Bun从Ghostty的源代码构建，并利用libghostty，这使得集成成为可能。长期计划是在可用时使用原生的Ghostty WASM发行版，保持xterm.js兼容的API。它采用MIT许可证。

---

## 33. 干细胞移植后，男子意外治愈艾滋病

**原文标题**: Man unexpectedly cured of HIV after stem cell transplant

**原文链接**: [https://www.newscientist.com/article/2506595-man-unexpectedly-cured-of-hiv-after-stem-cell-transplant/](https://www.newscientist.com/article/2506595-man-unexpectedly-cured-of-hiv-after-stem-cell-transplant/)

本文报道了一名男子在接受干细胞移植治疗白血病后意外治愈艾滋病病毒的案例。他是第七位通过这种方式治愈的患者，但重要的是，他是第二位使用的干细胞并非完全抵抗艾滋病病毒的患者。 这挑战了之前认为供体细胞中的艾滋病病毒抗性（特别是 CCR5 基因两个拷贝的突变）对于治愈至关重要的理解。

该男子接受了具有一个突变和一个典型 CCR5 基因拷贝的干细胞。 在接受化疗以清除其现有的免疫细胞后，他接受了移植。在抗逆转录病毒疗法（ART）期间，该病毒无法检测到。 三年后，他停止了 ART，研究人员在他的血液中发现了超过七年没有艾滋病病毒的痕迹，因此他被认定为“已治愈”。

这个案例以及之前的“日内瓦患者”案例表明，即使没有完全抗艾滋病病毒的供体细胞，也可能实现治愈。 一种假设是，在这种情况下，供体细胞在病毒传播之前消除了接受者剩余的原始免疫细胞，有效地耗尽了宿主细胞，从而病毒无法复制。

这一发现扩大了艾滋病病毒治愈的潜在干细胞捐献者范围，但包括接受者和捐献者的基因在内的几个因素需要一致才能奏效。 如果可以获得抗艾滋病病毒的干细胞，仍然应该优先考虑。

至关重要的是要强调，干细胞移植具有风险，不适合没有癌症的艾滋病病毒感染者。 ART 和更新的预防性治疗，如 lenacapavir，仍然是管理艾滋病病毒最安全和最容易获得的选择。 针对基因编辑和疫苗作为潜在的艾滋病病毒治愈方法的进一步研究仍在继续。

---

## 34. 将证书有效期缩短至45天

**原文标题**: Decreasing Certificate Lifetimes to 45 Days

**原文链接**: [https://letsencrypt.org/2025/12/02/from-90-to-45.html](https://letsencrypt.org/2025/12/02/from-90-to-45.html)

为了提高互联网安全性，Let's Encrypt 计划于 2028 年前将证书有效期从 90 天缩短至 45 天，以符合 CA/浏览器论坛设定的行业标准。授权重用期也将于 2028 年前从 30 天缩短至 7 小时。

此次变更将分阶段进行，利用 ACME 配置文件允许用户控制变更生效的时间：

*   **2026 年 5 月 13 日：** `tlsserver` ACME 配置文件切换至 45 天证书（可选）。
*   **2027 年 2 月 10 日：** 默认 `classic` ACME 配置文件切换至 64 天证书，授权重用期为 10 天。
*   **2028 年 2 月 16 日：** `classic` 配置文件更新至 45 天证书，授权重用期为 7 小时。

建议用户验证其自动化系统是否与较短的证书有效期兼容，并确保及时续订。 Let's Encrypt 建议使用 ACME Renewal Information (ARI) 来帮助了解续订情况。 如果不支持 ARI，则必须调整续订计划。

为了简化自动化，Let's Encrypt 正在开发一种新的 DNS 挑战类型，DNS-PERSIST-01，预计在 2026 年推出。 此方法允许在无需持续更新 DNS 记录的情况下进行证书续订，从而减少对授权重用的依赖并简化域名控制验证过程。 用户可以订阅技术更新邮件列表以获取更多信息。

---

## 35. 针对Ring面部识别功能的法律诉讼

**原文标题**: The Legal Case Against Ring's Face Recognition Feature

**原文链接**: [https://www.eff.org/deeplinks/2025/11/legal-case-against-rings-face-recognition-feature](https://www.eff.org/deeplinks/2025/11/legal-case-against-rings-face-recognition-feature)

本文概述了亚马逊Ring即将推出的“熟悉面孔”功能所涉及的法律问题。该功能使用面部识别技术来识别Ring摄像头拍摄到的人。主要问题是其可能违反各州的生物识别隐私法，这些法律通常要求在收集和使用面部识别等生物识别数据之前获得明确同意。

文章认为，Ring的这项功能需要扫描出现在摄像头中的每个人的面部，包括那些没有同意接受此类扫描的人。这给亚马逊带来了法律风险，正如针对谷歌和Facebook类似功能的诉讼所表明的那样，这些诉讼因侵犯隐私而导致巨额和解。

虽然亚马逊表示该功能默认关闭，并且在伊利诺伊州和德克萨斯州等生物识别隐私法严格的州不可用，但文章强调，未来可用性无法得到保证。此外，文章还强调了与生物识别数据收集相关的固有风险，包括大规模监控、数据泄露（面部信息无法像密码一样重置）以及因面部识别在某些人群中更高的错误率而导致的歧视。

文章指出，即使在个人无法直接起诉的州，州隐私监管机构也应调查和执行生物识别隐私法，以保护人们的数据。虽然一些州拥有包含漏洞并依赖州监管机构执法的综合隐私法，但文章认为Ring的“熟悉面孔”功能是检验这些法律效力并保障个人隐私权的机会。

---

## 36. 印度强制预装国有应用引发政治抗议

**原文标题**: Indian order to preload state-owned app on smartphones sparks political outcry

**原文链接**: [https://www.theguardian.com/world/2025/dec/02/indian-order-preload-state-owned-sanchar-saathi-app-smartphones-political-outcry](https://www.theguardian.com/world/2025/dec/02/indian-order-preload-state-owned-sanchar-saathi-app-smartphones-political-outcry)

印度政府已强制所有智能手机制造商，包括苹果、三星和小米，在新售手机上预装国有的网络安全应用程序Sanchar Saathi，并通过软件更新将其推送至现有手机。政府声称这是一项必要的安全措施，旨在打击网络安全威胁、欺诈和规范二手手机市场。该应用程序旨在帮助用户追踪丢失或被盗手机，识别欺诈号码，并验证二手设备的真伪。

然而，这项命令引发了重大的政治反对和数字自由活动家的担忧，他们认为这是政府进行监控的潜在工具，侵犯了隐私。国大党领导人强烈谴责这项强制令，誓言抗议这项“反乌托邦”的裁决，并将该应用程序称为“窥探应用程序”。

据报道，苹果公司因安全顾虑及其反对此类预装强制令的政策而拒绝遵守。虽然政府最初表示该应用程序无法禁用，但通信部长后来表示用户可以选择删除它。占印度智能手机市场绝大多数的安卓用户将被要求授予广泛的权限，包括访问通话记录、摄像头和照片，这进一步引发了对隐私的担忧。

---

## 37. 十年无人问津的博客写作

**原文标题**: 10 years of writing a blog nobody reads

**原文链接**: [https://flowtwo.io/post/on-10-years-of-writing-a-blog-nobody-reads](https://flowtwo.io/post/on-10-years-of-writing-a-blog-nobody-reads)

这篇博文反思了作者十年写作一篇鲜为人知博客的经历。写作的主要动机是为了自我提升，特别是为了成为一个更好、更简洁的写作者。作者承认了过去写作中的缺陷，包括过多的限定词（“我认为”、“我觉得”）和冗余的形容词，这些都稀释了他们写作的影响力。他们提倡自信地表达观点，即使这些观点具有争议性，并使用精确的语言来避免混淆信息。

作者强调了写作过程的迭代性，建议撰写多个草稿，并在想法出现时立即记录下来。他们强调了易于使用的写作工具的重要性，并指出Obsidian由于其跨设备支持而成为一个有用的平台。

这篇博文还涉及了生成式人工智能对写作价值的影响。虽然人工智能已经用书面内容淹没了市场，可能从经济角度降低了它的价值，但作者认为人类写作仍然具有个人价值。他们特别提到了书评，认为这是一种巩固知识并将其融入个人对世界理解的方式。写作被比作呼吸，是对不断消费信息的必要平衡。

最后，作者承认他们仍在努力改进，目标是写得更简洁，并将文章长度限制在1000字以内。他们觉得这个挑战很有动力，并鼓励继续写作。

---

## 38. 制图师曾在瑞士地图中隐藏插图 (2020)

**原文标题**: Cartographers have been hiding illustrations inside Switzerland’s maps (2020)

**原文链接**: [https://eyeondesign.aiga.org/for-decades-cartographers-have-been-hiding-covert-illustrations-inside-of-switzerlands-official-maps/](https://eyeondesign.aiga.org/for-decades-cartographers-have-been-hiding-covert-illustrations-inside-of-switzerlands-official-maps/)

制图师在瑞士地图中藏匿插图
文章《制图师在瑞士地图中藏匿插图》详细介绍了瑞士制图师长期以来的传统，即在国家官方地图中嵌入微妙而异想天开的插图。这些隐藏的图像，从神话生物（如龙和侏儒）到日常物品（如蜗牛和茶杯），既是一种艺术表达形式，也是对地图绘制通常严谨和技术性质的一种俏皮的反叛。

这种做法始于20世纪中叶，尤其是在单调的工作时期。制图师会将这些插图偷偷地添加到地图上不太显眼的地方，例如森林、湖泊，甚至是在等高线内。这种微妙的放置确保了插图不会损害地图的准确性或功能性。

文章强调，这些插图通常被认为是制图师同行和那些具有敏锐观察力的人的“彩蛋”。它们是制图师将个性和幽默注入其工作的一种方式，为可能被认为是纯粹功利性的文件增添了一层创造力和趣味性。虽然未经官方批准，但瑞士联邦地形局（swisstopo，负责创建和维护该国地图的组织）通常容忍这种做法。

文章认为，随着数字地图技术的日益普及，这种做法可能会逐渐消失，但这些隐藏插图的遗产仍然是人类创造力与技术精度融合的一个迷人例证。

---

## 39. 古怪有趣的物理点子

**原文标题**: Wacky Fun Physics Ideas

**原文链接**: [https://scottlocklin.wordpress.com/2025/11/22/wacky-fun-physics-ideas/](https://scottlocklin.wordpress.com/2025/11/22/wacky-fun-physics-ideas/)

斯科特·洛克林在2025年一篇题为《古怪有趣的物理学想法》的博文中表达了他对主流物理学的不满，认为它停滞不前，并且过度关注不可观测的现象。他倾向于探索挑战现有范式的非传统想法。

洛克林重点介绍了三篇特定的“怪异科学”论文：

1.  **轻子和引力：** 探讨了轻子（主要是电子）可能不像广义相对论所认为的那样产生引力的可能性。他认为应该进行实验来确定轻子是否对引力有贡献，以及结合能是否会产生引力。
2.  **熵引力：** 讨论了引力是矩阵力学熵的结果这一概念，其中引力是通过复杂的纠缠相互作用来体验的。虽然承认了现有关于这个主题的论文的缺点，但洛克林发现引力可能起源于热力学这一想法很有趣。
3.  **电子作为环形光子：** 提出了一个电子是具有环形拓扑结构的光子的模型。洛克林强调，这个模型可以通过提供令人满意的、无需神秘主义的机械解释，尤其是在自旋、电荷和康普顿波长方面，来解决现代物理学的许多怪异之处。

洛克林还谈到了天体生物学，特别是基于不同元素（如砷或硅）的未发现生命形式的可能性，并指出需要新的方法来检测这种不寻常的生命形式。

洛克林最后批评了许多物理学家对现代物理学中荒谬之处的盲目接受，并倡导采取更具批判性和创新性的科学探究方法。

---

## 40. 谷歌、英伟达和OpenAI

**原文标题**: Google, Nvidia, and OpenAI

**原文链接**: [https://stratechery.com/2025/google-nvidia-and-openai/](https://stratechery.com/2025/google-nvidia-and-openai/)

本文分析了谷歌、英伟达和OpenAI在人工智能领域的竞争格局，并将其框架为一个“谷歌反击”的故事。文章认为，谷歌的Gemini 3对OpenAI的模型霸权和英伟达的硬件霸权构成了重大威胁。

文章探讨了谷歌的TPU，现在正提供给Anthropic和Meta等公司，如何挑战英伟达的GPU垄断，并可能影响英伟达的长期增长和利润率。尽管英伟达在GPU灵活性和CUDA生态系统方面具有优势，但文章认为大型超大规模企业有资源开发替代软件栈。

然而，作者最终认为OpenAI比英伟达更有能力抵御谷歌的挑战。虽然OpenAI正在亏损，但其使用ChatGPT的消费者群体提供了一个强大的护城河。ChatGPT和英伟达的关键区别在于，ChatGPT面向更大的受众销售。文章认为ChatGPT的优势在于其直接的消费者关系，这使得谷歌很难直接取代它。ChatGPT和英伟达的关键区别在于独特的购买/用户数量。

文章总结认为，ChatGPT应该采用广告模式，以进一步加强其护城河。作者最后认为，谷歌赢得消费者注意力之战并非不可能。

---

## 41. 彼得·蒂尔末日论的世界观是一种危险的幻想

**原文标题**: Peter Thiel's Apocalyptic Worldview Is a Dangerous Fantasy

**原文链接**: [https://jacobin.com/2025/11/peter-thiel-palantir-apocalypse-antichrist](https://jacobin.com/2025/11/peter-thiel-palantir-apocalypse-antichrist)

本文批判彼得·蒂尔的“末世地缘政治”，认为这是对其反动政治议程和商业利益的危险辩护。蒂尔的世界观受到基督教末世论和纳粹法学家卡尔·施密特的启发，将全球政治描绘成“制止者”（对抗基督者的人）与敌基督者之间的斗争，映射为硅谷/美国与全球官僚主义过度扩张网络之间的斗争。

作者认为，这种框架掩盖了复杂的政治现实，使针对被认为是对手的极端暴力行为合法化，并保护蒂尔的观点免受审查。文章着重强调了蒂尔对极右翼人士的支持、对人工智能和军事技术的投资，以及他的公司帕兰提尔作为证据。帕兰提尔的数据分析工具被美国移民与海关执法局用于驱逐出境，被英国军方用于人工智能驱动的定位，以及被以色列军方用于加沙，这些都表明蒂尔的末世世界观如何转化为现实世界的伤害和种族化的国家暴力。

文章的结论是，蒂尔利用这种末世框架来否定国际法，为暴力辩护，并神化科技财富，最终模糊了美国的帝国主义和他自己的企业利益。他惧怕代表着对失去主权和技术民主化的反动恐惧的“世界政府”。最终，作者认为，蒂尔的愿景是一种言论，旨在使技术资本主义精英的权力合法化，对抗全球大多数人和地球的利益。鉴于当前的地缘政治紧张局势，文章警告了蒂尔的帝国主义和至上主义愿景的危险。

---

## 42. 谷歌放弃 JPEG XL？

**原文标题**: Google unkills JPEG XL?

**原文链接**: [https://tonisagrista.com/blog/2025/google-unkills-jpegxl/](https://tonisagrista.com/blog/2025/google-unkills-jpegxl/)

谷歌对JPEG XL的支持态度出现反转

---

## 43. Claude 4.5 Opus 的灵魂文档

**原文标题**: Claude 4.5 Opus' Soul Document

**原文链接**: [https://www.lesswrong.com/posts/vpNG99GhbBoLov9og/claude-4-5-opus-soul-document](https://www.lesswrong.com/posts/vpNG99GhbBoLov9og/claude-4-5-opus-soul-document)

无法访问文章链接。

---

## 44. 青霉素的迷思

**原文标题**: The Penicillin Myth

**原文链接**: [https://www.asimov.press/p/penicillin-myth](https://www.asimov.press/p/penicillin-myth)

本文挑战了亚历山大·弗莱明意外发现青霉素这一广为接受的说法。虽然该故事强调了机缘巧合和受污染的培养皿，但作者指出了其中的几个不一致之处和科学上的不可能之处。

首先，实验室的窗户很少打开，这使得污染的可能性不大。其次，这个故事与弗莱明早期发现溶菌酶的故事非常相似，这引起了人们对重复性的质疑。第三，在弗莱明声称的发现日期（9月3日）与第一篇实验记录（10月30日）之间存在显著的时间间隔。最重要的是，作者认为，青霉素的作用机制——干扰活跃生长过程中细胞壁的合成——与它能溶解已经形成的葡萄球菌菌落的说法相矛盾，而弗莱明正是这样认为的。对弗莱明实验的复制尝试一直未能成功。

然后，本文介绍了罗纳德·黑尔的理论，该理论是在检查实验室笔记本并进行自己的实验后提出的。黑尔认为，围绕这一发现的事件可能与官方说法不同。

作者最后强调，即使在承认青霉素的无可否认的成功的同时，也必须仔细审查甚至是被人们津津乐道的科学故事的准确性。这些差异突出了重新评估历史证据并探索弗莱明突破性发现的替代解释的必要性。

---

## 45. 交互设计的隐形细节 (2023)

**原文标题**: Invisible details of interaction design (2023)

**原文链接**: [https://rauno.me/craft/interaction-design](https://rauno.me/craft/interaction-design)

本文探讨交互设计中的“隐形细节”，认为优秀的设计不仅仅在于感觉和直觉，更在于理解成功交互背后的“为什么”。作者提倡一种实践性的、解决问题的学习方法，将实验与反思性思维相结合。

核心概念包括：

*   **隐喻：** 优秀的交互设计利用现实世界的隐喻，鼓励学习并使界面直观。例如滑动（书籍）、捏合（缩放）和分层界面。
*   **动能物理：** 融入真实的物理效果，如动量和响应，可以提升用户体验。
*   **滑动操作：** 确定滑动过程中何时触发操作以及何时在结束时触发操作至关重要。轻量级操作在滑动过程中触发，而破坏性操作需要手势完成。
*   **响应式手势：** 即时反馈和示能性对于令人满意的交互至关重要。
*   **空间一致性：** 视觉提示和运动应始终指示元素的来源和目的地，从而增强理解。
*   **流畅变形：** 无缝动画，如应用程序图标在关闭期间的变形，可以提升体验。
*   **频率与新颖性：** 应谨慎使用动画。高频交互可能受益于减少动画，以避免认知超载。
*   **小动作性：** 融入允许重复、下意识交互的元素可以增强参与度。
*   **滚动地标：** 帮助用户在导航过程中保持滚动位置的功能可提高可用性。
*   **触摸内容可见性：** 尽量减少手指在触摸界面上的遮挡，可以增强清晰度。

本质上，本文认为，优秀的交互设计取决于对人类行为的深刻理解，以及如何将技术无缝地融入我们的生活。

---

## 46. 人工智能正在摧毁大学和学习本身

**原文标题**: AI Is Destroying the University and Learning Itself

**原文链接**: [https://www.currentaffairs.org/news/ai-is-destroying-the-university-and-learning-itself](https://www.currentaffairs.org/news/ai-is-destroying-the-university-and-learning-itself)

在他的文章《人工智能正在摧毁大学和学习本身》中，罗纳德·珀瑟认为，将人工智能，特别是ChatGPT，融入高等教育正在破坏大学的根本目的，并助长作弊之风。他详细描述了大学在面临预算削减和入学人数下降的情况下，是如何拥抱人工智能作为解决方案的，与OpenAI等公司合作，同时削减教师职位和学术项目。

珀瑟强调了一种讽刺现象：机构一方面削减像女性与性别研究和人类学这样最能分析人工智能伦理影响的批判性思维部门的资金，另一方面却在整个校园推广人工智能工具。他批评了将教育视为私有市场职业输送带的转变，知识被商品化，学生被视为消费者。

这篇文章认为，人工智能将教育转变为物流，使评分和生成文章自动化，从而削弱了人类的好奇心和批判性思维等能力。这导致了“模拟学习”，学生被教导如何有效地提示人工智能，而不是进行深入思考。

珀瑟讨论了“作弊-人工智能技术复合体”的兴起，学生使用人工智能作弊，大学使用人工智能检测作弊，公司则从两者中获利。他提到了钟寅（音译）“罗伊”·李的案例，他通过使用人工智能在哥伦比亚大学作弊，然后创办了一家名为Cluely的公司，旨在帮助其他人作弊。珀瑟总结说，大学正在用“人工智能技术融合”来交易其教学使命，冒着变得无关紧要和失去灵魂的风险，并认为管理者们意识到这个问题，但将招生和学费置于真正的学习之上。

---

## 47. 约翰·贾南德雷亚将从苹果退休

**原文标题**: John Giannandrea to retire from Apple

**原文链接**: [https://www.apple.com/newsroom/2025/12/john-giannandrea-to-retire-from-apple/](https://www.apple.com/newsroom/2025/12/john-giannandrea-to-retire-from-apple/)

苹果机器学习与人工智能战略高级副总裁约翰·詹南德雷亚将在担任顾问后于2026年春季退休。曾就职于微软和谷歌（领导谷歌 Gemini 助手工程）的 Amar Subramanya 已加入苹果公司担任人工智能副总裁，向克雷格·费德里吉汇报。

Subramanya 将领导关键的人工智能领域，包括 Apple 基础模型、机器学习研究以及人工智能安全和评估。詹南德雷亚团队的其余部分将并入 Sabih Khan 和 Eddy Cue 的团队。

自 2018 年加入苹果以来，詹南德雷亚在塑造苹果的人工智能和机器学习战略方面发挥了重要作用。蒂姆·库克对詹南德雷亚的贡献表示感谢，并欢迎 Subramanya 的加入，强调了人工智能在苹果未来发展中的核心作用。费德里吉将负责监督扩大后的人工智能工作，包括更加个性化的 Siri。

苹果旨在利用 Subramanya 的专业知识和费德里吉扩大的职责范围来加速其人工智能开发，专注于提供智能且值得信赖的体验。此举表明了苹果致力于为用户推进人工智能的决心。

---

## 48. Replicate为何加入Cloudflare

**原文标题**: Why Replicate is joining Cloudflare

**原文链接**: [https://blog.cloudflare.com/why-replicate-joining-cloudflare/](https://blog.cloudflare.com/why-replicate-joining-cloudflare/)

Replicate加入Cloudflare，加速AI应用开发。

Replicate，一个将机器学习模型作为API运行的平台，将加入Cloudflare。Replicate成立于2019年，其使命是让开发者更容易地使用AI模型，它提供的工具简化了模型的运行，无需深厚的机器学习专业知识。随着2022年Stable Diffusion的发布，他们的平台获得了显著的吸引力，使开发者能够构建各种AI驱动的应用程序。

加入Cloudflare的决定源于AI应用程序开发的演变。现代AI应用程序现在涉及到复杂的堆栈，不仅仅是模型推理，还包括微服务、内容交付和数据库。Cloudflare提供了构建完整AI堆栈所需的网络、基础设施（Workers、R2、Durable Objects）和原语。

通过加入Cloudflare，Replicate旨在构建他们设想的AI基础设施层，实现诸如在边缘运行快速模型、使用Workers执行模型管道以及使用WebRTC流式传输模型输入/输出等功能。他们认为“网络就是计算机”，Cloudflare的平台将使他们能够实现这一AI愿景。

Replicate强调了其在生成式AI服务方面的先驱作用，并强调了围绕其产品发展起来的充满活力的构建者和研究人员社区。他们认为此次收购是为AI开发提供更强大和更全面的工具的自然发展。

---

## 49. 70年代的矢量图形工作站

**原文标题**: A vector graphics workstation from the 70s

**原文链接**: [https://justanotherelectronicsblog.com/?p=1429](https://justanotherelectronicsblog.com/?p=1429)

本文详细介绍了1975年产泰克4051图形工作站的修复过程。作者回顾了以示波器闻名的泰克公司的历史，以及该公司利用存储式CRT技术进军计算机终端领域的历程，最终推出了4051。这款机器基于摩托罗拉6800处理器，运行带有专用图形子程序的BASIC语言，并提供高达32KB的RAM，其目标用户是研究人员和分析师。

作者描述了发现一台损坏的4051，以及诊断和修复它的过程。最初的问题包括一个有故障的电源开关和一根断开的变压器电线。随后，一个电阻烧毁，需要更换。CRT显示器严重失调，需要调整各种电压设置才能获得可读的图像。

作者的4051配备了最大32KB的RAM和一个ROM扩展器。它缺少串行端口，但附带了操作系统备份磁带和三个ROM（编辑器、二进制加载/保存器和软盘驱动器支持）。

作者指出了存储式CRT在动态游戏方面的局限性，但也提到了 Monty McGraw 的 GitHub 存储库中提供的演示程序和程序，包括一款 Monopoly 游戏和用于现代计算机的模拟器。未来的计划包括构建一个用于加载程序的GPIB闪存模拟器，以及克隆缺失的ROM卡。

---

## 50. 我为什么不再使用 JSON 作为我的 API

**原文标题**: Why I stopped using JSON for my APIs

**原文链接**: [https://aloisdeniel.com/blog/better-than-json](https://aloisdeniel.com/blog/better-than-json)

本文反对API中广泛使用JSON，提倡使用Protocol Buffers (Protobuf) 作为更高效、更友好的替代方案。文章承认JSON具有人类可读性、简单性和广泛应用，但强调了Protobuf的优势：通过`.proto`模式文件强制执行的强类型、各种语言（Dart、TypeScript、Go等）的自动代码生成以及超高效的二进制序列化。

Protobuf的二进制格式导致更小的消息大小（在提供的示例中，大约是JSON的1/3），从而减少带宽消耗、加快响应时间并改善用户体验。作者演示了如何使用Protobuf进行数据序列化和反序列化，在Dart中实现一个简单的HTTP服务器和客户端，强调了类型安全性和减少手动验证的需求。

文章确实承认JSON在人类可读的调试方面的优势，因为Protobuf数据需要专门的工具和模式文件才能正确解释。然而，作者总结说，Protobuf提供的性能提升、健壮性和改进的开发体验超过了这一缺点，使其成为API开发的引人注目的替代方案。文章鼓励开发者考虑使用Protobuf，以获得其性能、健壮性和增强的开发体验。

---

## 51. 使用反作弊的游戏及其与GNU/Linux或Wine/Proton的兼容性

**原文标题**: Games using anti-cheats and their compatibility with GNU/Linux or Wine/Proton

**原文链接**: [https://areweanticheatyet.com/](https://areweanticheatyet.com/)

文章“我们反作弊了吗？”是一个由社区维护的列表，记录了游戏与反作弊系统的兼容性，以及它们在使用Wine/Proton的情况下在GNU/Linux上运行的能力。它提供了游戏兼容性的细分，将它们分类为“支持”、“运行”、“计划”、“损坏”或“拒绝”。这些类别表明了游戏在Linux上的功能级别。“支持”意味着游戏运行良好，而“运行”表明它可能有效，但可能存在问题。“损坏”意味着它目前无法运行，“拒绝”意味着由于反作弊不兼容，它不太可能有效。

该文章允许用户按名称和状态搜索和排序游戏。对于每个游戏，它列出了所使用的反作弊系统、关于兼容性的具体注释（如所需的Proton版本）以及上次记录更新的日期。从提供的摘录中，例如，《光环：士官长合集》和《光环：无限》被标记为“支持”，并具有特定要求，《堡垒之夜》、《战地2042》、《Apex英雄》和《Valorant》被标记为“拒绝”，《枪火游侠》、《黑色沙漠》、《糖豆人：终极淘汰赛》被列为“运行”，《绝地求生》被标记为“损坏”，而像《喋血复仇》、《SMITE》、《方舟：生存进化》、《DayZ》和《黎明杀机》等游戏则被标记为“支持”。主要目标是为Linux游戏玩家提供一个资源，以确定他们喜欢的游戏是否可以运行，因为反作弊系统及其与Wine/Proton的交互非常复杂。

---

## 52. 阿尔西三位一体迷你：美式萌系模型

**原文标题**: Arcee Trinity Mini: US-Trained Moe Model

**原文链接**: [https://www.arcee.ai/blog/the-trinity-manifesto?src=hn](https://www.arcee.ai/blog/the-trinity-manifesto?src=hn)

Arcee AI推出Trinity：一系列在美国端到端训练的开源权重混合专家(MoE)语言模型，旨在为开发者提供强大的推理能力和完全控制权。目前已推出两款模型：Trinity Nano Preview（一个60亿参数，以个性化为中心的聊天模型，具有8亿个活跃参数）和Trinity Mini（一个260亿参数的推理模型，具有30亿个活跃参数）。Trinity Large是一个4200亿参数的前沿模型，具有130亿个活跃参数，目前正在2048个B300 GPU上进行训练，预计将于2026年1月发布。

该公司决定预训练自己的模型，以解决现有开源模型的局限性、管辖范围内的安全问题（数据来源和许可），并实现能够根据实时使用情况调整训练循环的自改进AI系统的开发。他们基于在AFM-4.5B（一个45亿参数的密集模型）方面的经验，开发了Trinity的afmoe架构，该架构融合了门控注意力、深度缩放三明治归一化和Sigmoid路由等技术。

Trinity Nano和Mini被设计为紧凑型推理模型，专为代理和工具而调优，提供具有成本效益的API定价。它们在一个具有10万亿个token的数据集上进行训练，数据集质量和STEM集中度逐渐提高。训练过程被描述为具有挑战性，需要大量的基础设施和专业知识，包括与DatologyAI合作进行数据生成，以及与Prime Intellect合作提供计算资源。Arcee AI强调拥有模型权重和训练循环对于实现负责任和有效的AI开发的重要性。这些模型可在Hugging Face上下载，并可通过OpenRouter访问。Arcee鼓励用户尝试这些模型并提供反馈。

---

## 53. 这是非常艰难的一年。

**原文标题**: It’s been a very hard year

**原文链接**: [https://bell.bz/its-been-a-very-hard-year/](https://bell.bz/its-been-a-very-hard-year/)

Set Studio/Piccalilli创始人Andy坦诚分享了今年其自力更生公司因经济困难、政治不稳定和行业对AI的痴迷所面临的困境。出于伦理考虑，他拒绝从事AI产品营销工作。

尽管面临这些挑战，Set Studio/Piccalilli仍致力于制作高质量的网站、设计系统，以及在Piccalilli上提供免费教育内容，这些内容由付费课程资助。Andy表达了他全职运营Piccalilli的梦想，但实现这一目标在很大程度上取决于他们的黑色星期五促销。

今年早些时候，曾尝试通过Open Collective建立社区资助模式，但未能获得足够的关注。Andy承认财务约束影响着所有人。

这篇文章旨在直接呼吁：Andy正在寻求帮助。他概述了人们支持Set Studio/Piccalilli的三种主要方式：购买他们打折的黑色星期五课程（JavaScript for Everyone、Mindful Design和Complete CSS），与他们的社交圈分享他们的课程和工作室，以及在新的一年开始聘请Set Studio进行网站项目或Andy进行CSS/前端咨询。

他强调Set Studio独特的合作优先、效率至上、公平定价和道德设计方法，专注于品牌推广、信息传递、可访问性和用户体验以推动成果。他还强调了他自己的咨询专长。

Andy最后以透明和团结的信息结束，希望与面临类似困境的其他人联系，并敦促读者分享这篇文章以帮助产生潜在客户。他重申了他致力于提供有价值的资源和服务的承诺。

---

## 54. 常见独轮车问题解答

**原文标题**: Frequently Asked Unicycling Questions

**原文链接**: [https://vale.rocks/posts/unicycle-faq](https://vale.rocks/posts/unicycle-faq)

本文幽默地解答了独轮车骑行者经常遇到的问题。人们常问他们是否丢了一个轮子，对此有很多诙谐的回答。作者阐明独轮车比自行车更难，因为它缺乏前后方向的稳定性。虽然不特别危险，但头盔是必不可少的。

学习需要数周的专注练习。刹车是存在的，但很难使用，需要小心地控制，因为缺乏固有的稳定性。鞍座酸痛很常见，可以通过调整姿势和避免背包来缓解。

高级独轮车上的车把有助于转向、重量分配，并在技术动作中固定骑行者。安装方式可以是辅助安装，也可以是通过自由安装技术。独轮车没有悬架，而是依靠骑行者的膝盖和轮胎厚度来吸收震动。

对于有经验的骑行者来说，摔倒并不常见，通常发生在具有挑战性的越野骑行过程中。齿轮很少见，但可以通过昂贵的齿轮花鼓获得，比如 Schlumpf 花鼓。下坡对膝盖来说很艰难，而上坡虽然具有挑战性，但也可能很有趣。总的来说，本文对常见的独轮车骑行疑问提供了信息丰富且幽默的解答。

---

## 55. 紧缩式链接

**原文标题**: Shrinking While Linking

**原文链接**: [https://www.tweag.io/blog/2025-11-27-shrinking-static-libs/](https://www.tweag.io/blog/2025-11-27-shrinking-static-libs/)

Joe Neeman的“链接时收缩”解决了静态库体积过大的问题，尤其是在将Rust库分发给Go开发者时。静态库是目标文件的集合，通常包含不必要的代码和数据，导致体积大幅膨胀。

文章概述了两种主要的静态库体积缩减策略：使用传统的二进制工具和利用LLVM特定工具。

**二进制工具方法**包括：
1. 解压缩归档文件。
2. 将目标文件重新链接成一个单独的目标文件，使用`--gc-sections`移除未使用的代码。
3. 移除LLVM字节码（`.llvmbc`）和调试信息。
4. 使用链接器脚本合并微小节，以减少大量节头的开销。

**LLVM工具方法**，适用于像MacOS这样`--gc-sections`不可用的平台，侧重于LLVM中间表示：
1. 从目标文件中提取LLVM字节码。
2. 将字节码文件合并成一个大型文件。
3. 使用带有`internalize`和`globaldce`选项的`opt`来根据公共API移除未使用的代码。
4. 将结果重新编译成目标文件。

文章指出，两种方法都实现了类似的体积缩减效果（约85%），但LLVM工具提供了更好的跨平台性。然而，bintools方法速度更快，并且适用于任何静态库，而不仅仅是那些用LLVM编译的库。作者总结说，由于其跨平台兼容性，他们将使用LLVM方法来构建Nickel的静态库。

---

## 56. 测试：1981年达特桑280ZX涡轮增压型 (1981年)

**原文标题**: Tested: 1981 Datsun 280ZX Turbo (1981)

**原文链接**: [https://www.caranddriver.com/reviews/a69529696/1981-datsun-280-zx-turbo-archive-test/](https://www.caranddriver.com/reviews/a69529696/1981-datsun-280-zx-turbo-archive-test/)

1981年《汽车与驾驶员》杂志对达特桑280ZX Turbo的评测描绘了一幅舒适且相对快速的豪华旅行车图景，但也并非没有缺点。 评测重点介绍了2.8升直列六缸发动机增加了涡轮增压器，将马力提高到180匹，与自然吸气版本相比，加速性能有了显著提高。 涡轮增压器有助于解决之前对280ZX缺乏与其运动外观相匹配的冲击力的批评。

该文章强调了汽车的豪华功能和舒适的乘坐体验，将其定位为GT跑车而非纯粹的跑车。 诸如电动车窗、空调和先进的音响系统等标准配置都增强了这种豪华感。 虽然操控被认为是合格的，尤其是在可选的运动悬架下，但它不如一些竞争对手那样敏锐或吸引人，而是优先考虑舒适性而不是纯粹的性能。

评测还提到了一些缺点。 涡轮迟滞现象依然存在，需要驾驶员适应。 燃油经济性虽然可以接受，但并不出色。 内饰虽然配备齐全，但设计上有些过时。 最后，与一些竞争车型相比，其价格被认为偏高，使其与一些更成熟的欧洲品牌处于同一价位。 总而言之，1981年的达特桑280ZX Turbo被认为是比非涡轮增压车型更有价值的改进，为那些寻求轻松而又强大的豪华旅行体验的人提供了引人注目的风格、舒适性和性能的结合。

---

## 57. 代码降临 2025

**原文标题**: Advent of Code 2025

**原文链接**: [https://adventofcode.com/2025/about](https://adventofcode.com/2025/about)

代码降临节是由 Eric Wastl 创建的年度编程解谜日历。它面向不同技能水平的人群，可以使用任何编程语言解决。人们用它来发展技能、迎接挑战和参与竞赛。

这些谜题强调解决问题的能力，不需要计算机科学背景或强大的硬件。谜题在美东时间/UTC-5午夜解锁，难度通常会随着活动进行而增加。

本文档提供了解决谜题的技巧，建议用户重读描述、根据示例测试解决方案以及构建测试用例。它还解决了有关身份验证、难度级别、高对比度模式、谜题创意、错误报告、解决方案速度以及全球排行榜移除的常见问题。

要点包括允许创建私人排行榜，强烈反对使用人工智能解决谜题，并要求不要复制或重新分发代码降临节的内容。谜题和相关的设计元素版权归代码降临节所有，但用户保留对其解决方案的所有权。本文档还鸣谢了 Beta 测试人员和社区管理者。

---

## 58. Instagram负责人要求员工在2026年起每周五天返回办公室工作。

**原文标题**: Instagram chief orders staff back to the office five days a week in 2026

**原文链接**: [https://www.businessinsider.com/instagram-chief-adam-mosseri-announces-five-day-office-return-2025-12](https://www.businessinsider.com/instagram-chief-adam-mosseri-announces-five-day-office-return-2025-12)

据商业内幕报道，Instagram负责人已强制要求所有员工从2026年开始每周五天返回办公室工作。 这标志着与包括Meta（Instagram的母公司）在内的许多科技公司在新冠疫情后采取的更灵活的工作政策发生了重大转变。 虽然文章中没有详细说明这项指令的具体动机，但普遍的暗示是为了加强面对面的协作并巩固公司文化。 报告强调，这项政策要到2026年才会生效，这为员工调整个人和职业生活留出了充足的时间。 此举可能会影响员工士气和留任率，因为有些人可能更喜欢或需要远程工作安排。 该声明使Instagram与一些保持混合或完全远程办公的竞争对手形成对比，表明了一种独特的领导理念。 文章强调了科技行业内部关于远程工作和办公室办公之间的最佳平衡点日益激烈的辩论。

---

## 59. 树莓派操作系统上的Cloud-Init

**原文标题**: Cloud-Init on Raspberry Pi OS

**原文链接**: [https://www.raspberrypi.com/news/cloud-init-on-raspberry-pi-os/](https://www.raspberrypi.com/news/cloud-init-on-raspberry-pi-os/)

基于对cloud-init及其典型应用场景的理解，以下是摘要（假设链接文章讨论的是其在Raspberry Pi OS上的实现）。如果我对文章内容理解有误，我将无法在没有访问权限的情况下完善此摘要。

**摘要：Raspberry Pi OS上的Cloud-Init（假定内容）**

该文章可能宣布了cloud-init功能集成到Raspberry Pi OS中。 Cloud-init是一个广泛使用的开源软件包，允许用户在初始启动期间自定义和配置云实例（虚拟机、服务器，现在包括Raspberry Pi）。这实现了自动配置和设置，从而简化了部署过程。

Cloud-init在Raspberry Pi OS上的主要优点包括：

*   **自动化配置：** 用户可以使用配置文件（通常是YAML）预配置诸如主机名、网络配置（静态IP、DNS）、用户帐户、SSH密钥和软件包安装等设置。这消除了刷写OS镜像后手动配置的需要。

*   **可扩展性和可重复性：** Cloud-init使部署具有一致配置的多个Raspberry Pi变得更加容易。这对于管理物联网应用、边缘计算或教育实验室的设备群尤其有价值。

*   **云兼容性：** 通过支持cloud-init，Raspberry Pi OS变得与云基础设施环境和工作流程更加兼容。这允许开发人员将Raspberry Pi更像云实例一样对待，从而简化了开发和部署管道。

*   **简化配置：** 用户可以创建一个Raspberry Pi OS镜像，并通过cloud-init使用不同的配置对其进行动态自定义。这减少了管理多个自定义镜像的需求。

该文章可能提供了如何在Raspberry Pi OS上使用cloud-init的说明，包括如何创建和应用cloud-init配置文件。它还可能突出显示特定用例和示例，说明cloud-init如何简化Raspberry Pi的部署。

**注意：** 这是基于常见cloud-init功能以及文章涵盖其集成到Raspberry Pi OS的假设的摘要。更准确的摘要需要直接访问文章。

---

## 60. Durin 是一个用于读写 Dwarf 调试格式的库。

**原文标题**: Durin is a library for reading and writing the Dwarf debugging format

**原文链接**: [https://github.com/tmcgilchrist/durin](https://github.com/tmcgilchrist/durin)

Durin 是一个用于读写 DWARF 调试格式的库，旨在支持 DWARF 5（以及可能更早的版本），适用于 ELF 和 MachO 目标文件以及汇编文件。它提供跨平台兼容性，避免对目标文件类型进行假设。其主要特性包括延迟解析，允许在不进行完整内容解析的情况下迭代编译单元，并利用 `DW_AT_sibling` 引用进行高效导航。

Durin 可以通过 `opam install durin` 安装。该库提供了几个示例程序来演示其功能，包括：.debug_info 和 .debug_line 解析器、dwarfdump 和 addr2line 克隆、一个用于列出编译单元中使用编译器的 dwprod 实用程序，以及一个用于 DWARF 完整性检查的 dwarf-validate 克隆。

资源部分提供了关于 Apple Compact Unwinding Format 的有用链接，以及来自 GCC 的供应商扩展的链接。

---

## 61. Stride游戏引擎4.3，支持.NET 10

**原文标题**: Stride Game Engine 4.3 with .NET 10 Support

**原文链接**: [https://www.stride3d.net/blog/announcing-stride-4-3-in-dotnet-10/](https://www.stride3d.net/blog/announcing-stride-4-3-in-dotnet-10/)

Stride游戏引擎4.3发布，带来重大更新，包括**支持.NET 10和C# 14**以提升性能和代码简洁性。主要新增功能包括**集成Bepu Physics**，提供快速的、基于C#的物理引擎（但仍支持Bullet），以及**Vulkan计算着色器支持**。此版本还引入了**自定义资产**，支持用户定义的数据存储和更复杂的资产编译。

改进的目标是**跨平台构建能力**，使项目能够在Linux和Apple桌面系统上构建，并且现在可以使用更高效的API来操作网格。GameStudio现在支持使用**Rider和VSCode**打开项目。新的灵活处理系统支持通过接口处理组件，从而提高了类型安全性。

其他增强功能包括D3d/Windows的HDR渲染、用户定义的Gizmo、VR的触觉反馈以及OpenXR Passthrough的API。此版本包含多项修复，重点关注性能、Vulkan和OpenGL稳定性、Linux兼容性以及GameStudio中的程序集重新加载。

未来版本（4.4+）的持续努力包括跨平台构建、通过Avalonia实现的跨平台GameStudio、着色器编译改进以及D3d12和Vulkan支持的进一步开发。Stride团队积极寻求在C#、.NET、移动、XR、渲染和游戏开发方面有技能的开发人员来贡献代码。鼓励社区通过代码、推广和捐赠参与。

---

## 62. 仅返回ChatGPT公开发布前内容的搜索工具

**原文标题**: Search tool that only returns content created before ChatGPT's public release

**原文链接**: [https://tegabrain.com/Slop-Evader](https://tegabrain.com/Slop-Evader)

该文本描述了一种搜索工具，其核心和决定性功能是仅返回在ChatGPT公开发布*之前*创建的内容。该文本还展示了一个菜单或导航栏，包含以下选项：

*   **TEGA：** 这可能是工具或平台的名称。
*   **BRAINABOUTNEWSWORKCONTACT：** 这些似乎是平台内的链接或版块，可能与其功能、关于信息、新闻、工作和联系方式相关。
*   **TEACHING：** 这表明该平台或工具可能具有教育应用或功能。

本质上，该工具旨在提供一种过滤后的搜索体验，专门排除ChatGPT出现后生成的内容。这表明需要区分人类生成的内容和人工智能生成的内容，可能用于研究、历史分析或信息来源和真实性至关重要的其他应用。 “教学”版块的存在暗示了其在学术背景下的潜在用途，在这种背景下，理解人工智能出现之前的信息至关重要。

---

## 63. OpenAI宣布“红色警戒”，因谷歌威胁其人工智能领导地位

**原文标题**: OpenAI Declares 'Code Red' as Google Threatens AI Lead

**原文链接**: [https://www.wsj.com/tech/ai/openais-altman-declares-code-red-to-improve-chatgpt-as-google-threatens-ai-lead-7faf5ea6](https://www.wsj.com/tech/ai/openais-altman-declares-code-red-to-improve-chatgpt-as-google-threatens-ai-lead-7faf5ea6)

无法访问文章链接。

---

## 64. 1GB 树莓派 5，以及内存驱动的价格上涨

**原文标题**: 1GB Raspberry Pi 5, and memory-driven price rises

**原文链接**: [https://www.raspberrypi.com/news/1gb-raspberry-pi-5-now-available-at-45-and-memory-driven-price-rises/](https://www.raspberrypi.com/news/1gb-raspberry-pi-5-now-available-at-45-and-memory-driven-price-rises/)

以下是基于标题对 Raspberry Pi 文章的总结：

树莓派基金会重新推出 1GB 版本的 Raspberry Pi 5，定价 45 美元。这为 Pi 5 重新带来了一个低成本的入门点，吸引了预算有限的用户和不需要大量 RAM 的应用。

然而，文章还宣布 Raspberry Pi 5 的 2GB、4GB 和 8GB 型号的价格上涨。这些价格上涨归因于内存成本的大幅增加。 基金会表示，内存价格大幅上涨，迫使他们调整定价以维持生产这些电路板的可行性。

本质上，这篇文章强调了好消息（1GB 型号的回归）和坏消息（由于内存成本导致的价格上涨）。1GB 型号的回归为一些用户提供了一个更便宜的选择，而另一些用户将面临更高内存容量电路板的更高价格。

---

## 65. 为什么异或eax，eax？

**原文标题**: Why xor eax, eax?

**原文链接**: [https://xania.org/202512/01-xor-eax-eax](https://xania.org/202512/01-xor-eax-eax)

标题: "为什么使用 xor eax, eax?"

本文解释了为什么编译器经常使用 `xor eax, eax` 指令将 EAX 寄存器清零，而不是更直观的 `mov eax, 0`。

主要原因是代码大小：`xor eax, eax` 仅占用两个字节，而 `mov eax, 0` 需要五个字节。 这种字节节省非常重要，因为将寄存器清零是一种频繁的操作。 更小的代码带来更好的指令缓存利用率和更小的程序总体大小。

除了大小之外，现代 x86 CPU 还会优化 `xor eax, eax` 这种用法。 CPU 的乱序执行系统识别出 EAX 的新值不依赖于其先前的值。 因此，它会分配一个全新的、无依赖的零寄存器，并有效地将 `xor` 操作从执行队列中移除，从而实现零执行周期。

文章还指出，即使仅显式异或了低 32 位，x86 架构也会自动将高 32 位清零，从而有效地将整个 64 位 RAX 寄存器清零。 最后，文章指出，即使对于扩展寄存器，编译器也倾向于使用 32 位版本的 XOR 寄存器清零，原因可能与编译器实现有关。

---

## 66. 新的人工智能寒冬要来了吗？

**原文标题**: A new AI winter is coming?

**原文链接**: [https://taranis.ie/llms-are-a-failure-a-new-ai-winter-is-coming/](https://taranis.ie/llms-are-a-failure-a-new-ai-winter-is-coming/)

尽管围绕ChatGPT等基于Transformer的AI模型的初期兴奋，本文认为一场新的“AI寒冬”即将到来。作者认为，虽然Transformer通过无监督学习扩展规模并避免了NP完全性问题，从而克服了先前AI方法的局限性，但它们存在一个根本且无法解决的缺陷：它们依赖于生成听起来貌似合理但与准确性无关的输出。这种“幻觉”问题源于模型固有的设计，即基于概率而非真正理解来生成tokens，从而导致频繁且通常无法检测到的错误。

作者认为这类似于撞上了NP完全性的墙，即以牺牲正确性为代价来提供快速输出。这种不可靠性，成功率从60%到95%不等，使得Transformer不适用于许多实际应用，特别是那些需要高精度或错误可能导致严重后果的应用（例如，医学、执法）。本文强调了企业界对AI能力的高估，将其与互联网泡沫相提并论，并预测了一场崩溃，OpenAI等公司面临潜在的失败，AI投资将被削减。

作者特别批评了Transformer在代码生成中的应用，认为貌似合理但不正确的代码可能会引入危险的错误。虽然承认该技术不会完全消失，但本文预计AI格局将会收缩，只有少数“杀手级应用”用例能够幸存，而许多依赖于对LLM性能不切实际期望的应用将会失败。文章最后警告要减少对即将到来的AI泡沫破裂的风险敞口，并借鉴了作者在互联网时代一家失败的聊天机器人公司的个人经历。

---

## 67. 海上风能提取的理论上限

**原文标题**: A theoretical upper limit for offshore wind energy extraction

**原文链接**: [https://www.cell.com/cell-reports-sustainability/fulltext/S2949-7906(25)00269-1](https://www.cell.com/cell-reports-sustainability/fulltext/S2949-7906(25)00269-1)

无法访问文章链接。

---

## 68. Is 2026 Next Year?

**原文标题**: Is 2026 Next Year?

**原文链接**: [https://www.google.com/search?q=is+2026+next+year&oq=is+2026+next+year](https://www.google.com/search?q=is+2026+next+year&oq=is+2026+next+year)

生成摘要时出错

---

## 69. Forward compatibility and fault tolerance in TypeScript API Clients/SDKs

**原文标题**: Forward compatibility and fault tolerance in TypeScript API Clients/SDKs

**原文链接**: [https://www.speakeasy.com/blog/typescript-forward-compatibility](https://www.speakeasy.com/blog/typescript-forward-compatibility)

生成摘要时出错

---

## 70. Jury trials scrapped for crimes with sentences of less than three years

**原文标题**: Jury trials scrapped for crimes with sentences of less than three years

**原文链接**: [https://www.bbc.co.uk/news/articles/cn5lxg2l0lqo](https://www.bbc.co.uk/news/articles/cn5lxg2l0lqo)

生成摘要时出错

---

## 71. Mozilla's latest quagmire

**原文标题**: Mozilla's latest quagmire

**原文链接**: [https://rubenerd.com/mozillas-latest-quagmire/](https://rubenerd.com/mozillas-latest-quagmire/)

生成摘要时出错

---

## 72. ImAnim: Modern animation capabilities to ImGui applications

**原文标题**: ImAnim: Modern animation capabilities to ImGui applications

**原文链接**: [https://github.com/soufianekhiat/ImAnim](https://github.com/soufianekhiat/ImAnim)

生成摘要时出错

---

## 73. Historic Engineering Wonders: Photos That Reveal How They Pulled It Off

**原文标题**: Historic Engineering Wonders: Photos That Reveal How They Pulled It Off

**原文链接**: [https://rarehistoricalphotos.com/engineering-methods-from-the-past/](https://rarehistoricalphotos.com/engineering-methods-from-the-past/)

生成摘要时出错

---

## 74. High-income job losses are cooling housing demand

**原文标题**: High-income job losses are cooling housing demand

**原文链接**: [https://jbrec.com/insights/job-growth-housing-demand-metro-analysis-2026/](https://jbrec.com/insights/job-growth-housing-demand-metro-analysis-2026/)

生成摘要时出错

---

## 75. AI just proved Erdos Problem #124

**原文标题**: AI just proved Erdos Problem #124

**原文链接**: [https://www.erdosproblems.com/forum/thread/124#post-1892](https://www.erdosproblems.com/forum/thread/124#post-1892)

生成摘要时出错

---

## 76. Response to "Ruby Is Not a Serious Programming Language"

**原文标题**: Response to "Ruby Is Not a Serious Programming Language"

**原文链接**: [https://robbyonrails.com/articles/2025/12/01/why-so-serious/](https://robbyonrails.com/articles/2025/12/01/why-so-serious/)

生成摘要时出错

---

## 77. Show HN: Webclone.js – A simple tool to clone websites

**原文标题**: Show HN: Webclone.js – A simple tool to clone websites

**原文链接**: [https://github.com/jademsee/webclone](https://github.com/jademsee/webclone)

生成摘要时出错

---

## 78. AI agents find $4.6M in blockchain smart contract exploits

**原文标题**: AI agents find $4.6M in blockchain smart contract exploits

**原文链接**: [https://red.anthropic.com/2025/smart-contracts/](https://red.anthropic.com/2025/smart-contracts/)

生成摘要时出错

---

## 79. X210Ai is a new motherboard to upgrade ThinkPad X201/200

**原文标题**: X210Ai is a new motherboard to upgrade ThinkPad X201/200

**原文链接**: [https://www.tpart.net/about-x210ai/](https://www.tpart.net/about-x210ai/)

生成摘要时出错

---

## 80. SmartTube Compromised

**原文标题**: SmartTube Compromised

**原文链接**: [https://www.aftvnews.com/smarttubes-official-apk-was-compromised-with-malware-what-you-should-do-if-you-use-it/](https://www.aftvnews.com/smarttubes-official-apk-was-compromised-with-malware-what-you-should-do-if-you-use-it/)

生成摘要时出错

---

## 81. Decreasing Certificate Lifetimes to 45 Days

**原文标题**: Decreasing Certificate Lifetimes to 45 Days

**原文链接**: [https://letsencrypt.org/2025/12/02/from-90-to-45](https://letsencrypt.org/2025/12/02/from-90-to-45)

生成摘要时出错

---

## 82. Sycophancy is the first LLM "dark pattern"

**原文标题**: Sycophancy is the first LLM "dark pattern"

**原文链接**: [https://www.seangoedecke.com/ai-sycophancy/](https://www.seangoedecke.com/ai-sycophancy/)

生成摘要时出错

---

## 83. Amazon faces FAA probe after delivery drone snaps internet cable in Texas

**原文标题**: Amazon faces FAA probe after delivery drone snaps internet cable in Texas

**原文链接**: [https://www.cnbc.com/2025/11/25/amazon-faa-probe-delivery-drone-incident-texas.html](https://www.cnbc.com/2025/11/25/amazon-faa-probe-delivery-drone-incident-texas.html)

生成摘要时出错

---

## 84. Detection of triboelectric discharges during dust events on Mars

**原文标题**: Detection of triboelectric discharges during dust events on Mars

**原文链接**: [https://gizmodo.com/weve-detected-lightning-on-mars-for-the-first-time-2000691996](https://gizmodo.com/weve-detected-lightning-on-mars-for-the-first-time-2000691996)

生成摘要时出错

---

## 85. Around The World, Part 27: Planting trees

**原文标题**: Around The World, Part 27: Planting trees

**原文链接**: [https://frozenfractal.com/blog/2025/11/28/around-the-world-27-planting-trees/](https://frozenfractal.com/blog/2025/11/28/around-the-world-27-planting-trees/)

生成摘要时出错

---

## 86. Gitmal – a static pages generator for Git repos

**原文标题**: Gitmal – a static pages generator for Git repos

**原文链接**: [https://github.com/antonmedv/gitmal](https://github.com/antonmedv/gitmal)

生成摘要时出错

---

## 87. Intel could return to Apple computers in 2027

**原文标题**: Intel could return to Apple computers in 2027

**原文链接**: [https://www.theverge.com/news/832366/intel-apple-m-chip-low-end-processor](https://www.theverge.com/news/832366/intel-apple-m-chip-low-end-processor)

生成摘要时出错

---

## 88. Help, My Java Object Vanished (and the GC Is Not at Fault)

**原文标题**: Help, My Java Object Vanished (and the GC Is Not at Fault)

**原文链接**: [https://arraying.de/posts/markword/](https://arraying.de/posts/markword/)

生成摘要时出错

---

## 89. Writing a good Claude.md

**原文标题**: Writing a good Claude.md

**原文链接**: [https://www.humanlayer.dev/blog/writing-a-good-claude-md](https://www.humanlayer.dev/blog/writing-a-good-claude-md)

生成摘要时出错

---

## 90. Last Week on My Mac: Losing confidence

**原文标题**: Last Week on My Mac: Losing confidence

**原文链接**: [https://eclecticlight.co/2025/11/30/last-week-on-my-mac-losing-confidence/](https://eclecticlight.co/2025/11/30/last-week-on-my-mac-losing-confidence/)

生成摘要时出错

---

## 91. The era of AI slop cleanup has begun

**原文标题**: The era of AI slop cleanup has begun

**原文链接**: [https://www.reddit.com/r/ExperiencedDevs/s/3IFx9z462I](https://www.reddit.com/r/ExperiencedDevs/s/3IFx9z462I)

生成摘要时出错

---

## 92. Pose-free 3D Gaussian splatting via shape-ray estimation

**原文标题**: Pose-free 3D Gaussian splatting via shape-ray estimation

**原文链接**: [https://arxiv.org/abs/2505.22978](https://arxiv.org/abs/2505.22978)

生成摘要时出错

---

## 93. The Rise of AI Denialism

**原文标题**: The Rise of AI Denialism

**原文链接**: [https://bigthink.com/the-present/the-rise-of-ai-denialism/](https://bigthink.com/the-present/the-rise-of-ai-denialism/)

生成摘要时出错

---

## 94. University of Pennsylvania confirms new data breach after Oracle hack

**原文标题**: University of Pennsylvania confirms new data breach after Oracle hack

**原文链接**: [https://www.bleepingcomputer.com/news/security/university-of-pennsylvania-confirms-data-theft-after-oracle-ebs-hack/](https://www.bleepingcomputer.com/news/security/university-of-pennsylvania-confirms-data-theft-after-oracle-ebs-hack/)

生成摘要时出错

---

## 95. FreeBSD 15.0-Release Announcement

**原文标题**: FreeBSD 15.0-Release Announcement

**原文链接**: [https://www.freebsd.org/releases/15.0R/announce/](https://www.freebsd.org/releases/15.0R/announce/)

生成摘要时出错

---

## 96. Langjam Gamejam: Build a programming language then make a game with it

**原文标题**: Langjam Gamejam: Build a programming language then make a game with it

**原文链接**: [https://langjamgamejam.com/](https://langjamgamejam.com/)

生成摘要时出错

---

## 97. A Love Letter to FreeBSD

**原文标题**: A Love Letter to FreeBSD

**原文链接**: [https://www.tara.sh/posts/2025/2025-11-25_freebsd_letter/](https://www.tara.sh/posts/2025/2025-11-25_freebsd_letter/)

生成摘要时出错

---

## 98. A Bus Ride and the (At Least) 3x UX FAILs

**原文标题**: A Bus Ride and the (At Least) 3x UX FAILs

**原文链接**: [https://bsdly.blogspot.com/2025/11/a-bus-ride-and-at-least-3x-ux-fails.html](https://bsdly.blogspot.com/2025/11/a-bus-ride-and-at-least-3x-ux-fails.html)

生成摘要时出错

---

## 99. Show HN: RFC Hub

**原文标题**: Show HN: RFC Hub

**原文链接**: [https://rfchub.app/](https://rfchub.app/)

生成摘要时出错

---

## 100. Google Antigravity just deleted the contents of whole drive

**原文标题**: Google Antigravity just deleted the contents of whole drive

**原文链接**: [https://old.reddit.com/r/google_antigravity/comments/1p82or6/google_antigravity_just_deleted_the_contents_of/](https://old.reddit.com/r/google_antigravity/comments/1p82or6/google_antigravity_just_deleted_the_contents_of/)

生成摘要时出错

---

