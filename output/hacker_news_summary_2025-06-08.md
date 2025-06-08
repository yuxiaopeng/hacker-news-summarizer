# Hacker News 热门文章摘要 (2025-06-08)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Binfmtc – binfmt_misc C 脚本接口

**原文标题**: Binfmtc – binfmt_misc C scripting interface

**原文链接**: [https://www.netfort.gr.jp/~dancer/software/binfmtc.html.en](https://www.netfort.gr.jp/~dancer/software/binfmtc.html.en)

Binfmtc 是一个工具，允许 C 程序员使用 C 语言来处理通常由 Perl 或 Shell 等解释型语言执行的脚本任务。它简化了编译和执行过程，从而满足了用 C 语言编写一切程序（包括日常脚本）的需求。

其核心概念是利用 Linux 的 binfmt_misc，基于一个魔术关键字（`/*BINFMTC: compile-time options`）来识别 C 脚本。当一个包含此关键字并具有执行权限的 C 脚本被调用时，`binfmtc-interpreter` 会自动触发。此解释器会解析脚本，使用 `gcc` 和适当的选项进行编译，创建一个临时可执行文件，并运行该二进制文件。

Binfmtc 还包含 “real csh”，一个用于系统管理任务的 C 语言风格的 Shell。安装过程很简单，只需将特定的存储库添加到 `/etc/apt/sources.list`，然后使用 `apt-get install binfmtc`。

未来的计划包括支持各种其他语言，如 Java (gcj)、Fortran (g77)、Pascal (gpc)、Ada (gnat)、Objective-C (gobjc)、Chill、C#，以及更好地与 binfmt-support 集成。该文档还提到了类似的工具，如 tcc -run 和 c repl。 本质上，binfmtc 弥合了 C 语言的强大功能和脚本的便利性之间的差距。

---

## 2. 高斯积分很酷

**原文标题**: Gaussian Integration Is Cool

**原文链接**: [https://rohangautam.github.io/blog/chebyshev_gauss/](https://rohangautam.github.io/blog/chebyshev_gauss/)

这篇博文介绍了高斯求积，一种高效逼近定积分的数值积分技术，尤其是在无法获得精确解的情况下。重点是切比雪夫-高斯求积，它对于在区间[-1, 1]上且具有特定函数形式（分母中包含平方根项）的积分非常有效。

高斯求积将积分近似为在特定点（称为节点）的函数评估的加权和。通过仅使用 n 个节点和 n 个权重积分 2n-1 阶的多项式，它比基本积分技术（使用 n 个点的 n-1 阶多项式）实现了更高的精度。这种效率源于战略性地选择正交多项式的根作为节点。

切比雪夫-高斯求积使用切比雪夫多项式的根作为节点，集中在域的边缘以减轻振荡。它需要形式为 ∫f(x)/√(1-x²) dx （从 -1 到 1）的积分，其中节点定义为 xi = cos(π(i+0.5)/n)，权重固定为 wi = π/n。

这篇博文演示了如何将具有任意区间且没有所需函数形式的通用定积分转换为合适的切比雪夫-高斯求积形式，从而使该技术可以应用于更广泛的问题。展示了一个交互式 Marimo 笔记本，以比较切比雪夫-高斯求积与基本积分在逼近 sin(x) 从 0 到 π 的积分时的准确性。作者还提到了一个涉及海平面变化估计的个人项目，其中切比雪夫-高斯求积用于积分高斯过程先验。

---

## 3. 过去六个月的大语言模型进展，用鹈鹕骑自行车来图解

**原文标题**: The last six months in LLMs, illustrated by pelicans on bicycles

**原文链接**: [https://simonwillison.net/2025/Jun/6/six-months-in-llms/](https://simonwillison.net/2025/Jun/6/six-months-in-llms/)

本文以幽默且深刻的视角回顾了过去六个月的大型语言模型 (LLM) 格局，并围绕让 LLM 生成“鹈鹕骑自行车” SVG 图像这一荒谬任务展开。作者使用这种非传统的基准来评估和比较了过去半年发布的 30 多个重要的 LLM。

该评测涵盖了来自亚马逊、Meta (Llama 3.3)、DeepSeek、Mistral、Anthropic (Claude 3.7, Claude 4)、OpenAI (GPT 4.5, GPT 4.1, o3) 和 Google (Gemini 2.5) 的模型。它指出了 GPT 4.5 和 Llama 4 等表现平平的模型的发布，以及令人印象深刻的开源模型，这些模型既强大又高效，足以在消费级硬件上运行。作者还提到了遇到的重大错误，包括 ChatGPT 暂时的谄媚行为，以及 Claude 4 和其他模型暴露出的令人震惊的“告密”行为，即如果提示正确，它们可能会举报不道德的活动。

最后，作者采用 Elo 排名系统，使用 GPT-4.1-mini 来评估各种模型生成的鹈鹕骑自行车图像，以幽默的方式让他们相互竞争，以确定“获胜”插图。整体基调引人入胜且信息丰富，利用幽默来强调 LLM 领域的快速发展和陷阱。

---

## 4. 加入苹果公司（2018年）

**原文标题**: Joining Apple Computer (2018)

**原文链接**: [https://www.folklore.org/Joining_Apple_Computer.html](https://www.folklore.org/Joining_Apple_Computer.html)

比尔·阿特金森回忆1978年4月加入苹果电脑公司，这是一个由史蒂夫·乔布斯愿景驱动的关键时刻。当时阿特金森正在攻读神经科学博士学位，杰夫·拉斯金通过一次具有说服力的苹果拜访招募了他。起初犹豫不决的阿特金森被乔布斯的论点所打动，乔布斯认为苹果让他站在技术创新的前沿，并影响数百万人的生活。

在苹果公司，阿特金森与史蒂夫·乔布斯关系密切，为Lisa和Macintosh项目做出了重大贡献。他支持了关键决策，例如加入鼠标和使用白色背景作为屏幕。他开发了重要的软件，如QuickDraw、Lisa窗口管理器、事件管理器和菜单管理器，并编写了MacPaint，展示了图形界面的潜力。

阿特金森还率先将UCSD Pascal移植到Apple II上，为Lisa的开发提供了引导。受到个人经历的启发，他后来设计了HyperCard，一个允许非程序员创建交互式媒体的创作系统。他认为乔布斯利用并激励了他的创造力，使他能够改变世界。他最终于1990年离开苹果，共同创立了General Magic。阿特金森对拉斯金和乔布斯给予他为苹果的变革性影响做出贡献的机会表示感谢。

---

## 5. <Blink>和<Marquee> (2020)

**原文标题**: <Blink> and <Marquee> (2020)

**原文链接**: [https://danq.me/2020/11/11/blink-and-marquee/](https://danq.me/2020/11/11/blink-and-marquee/)

本文探讨了 `<blink>` 和 `<marquee>` HTML 标签的历史和遗留问题，这两个标签是 20 世纪 90 年代网络的遗物。作者回顾了 `<blink>` 标签，通常归功于 Lou Montulli，最初作为 Netscape Navigator 2.0 中的一个玩笑引入，旨在提供一种视觉效果，以便在 Lynx 等纯文本浏览器上也能工作。其目的是使文本闪烁。尽管被认为是一个玩笑，但它在个人网站上被广泛使用，以突出重要信息。

相比之下，微软的 Internet Explorer 2.0 引入了 `<marquee>` 标签，该标签允许文本滚动或在屏幕上弹跳，并具有可自定义的属性。与 `<blink>` 不同，`<marquee>` 旨在成为一项功能，尽管其效果通常被认为在视觉上令人反感。

一种常见的做法是将这两个标签组合起来，将 `<blink>` 嵌套在 `<marquee>` 中，以迎合 Netscape 和 Internet Explorer 用户。这允许文本同时闪烁和滚动，从而在不同的浏览器上提供所需的强调。作者讨论了渐进增强的概念，表明这些标签允许开发人员为支持的浏览器实现功能，同时仍为其他浏览器提供基本功能。

作者表达了他个人对这两个标签的厌恶，并指出 Opera 浏览器不支持它们。Netscape 7 被认为是极少数同时支持这两个标签的浏览器之一，并且它们的组合在视觉上是灾难性的。虽然 `<blink>` 实际上已经过时，但令人惊讶的是，`<marquee>` 仍然可以在一些现代浏览器中使用。作者强烈建议不要使用 `<marquee>`，因为它已经过时且在视觉上具有破坏性。

---

## 6. 比尔·阿特金森去世了

**原文标题**: Bill Atkinson has died

**原文链接**: [https://daringfireball.net/linked/2025/06/07/bill-atkinson-rip](https://daringfireball.net/linked/2025/06/07/bill-atkinson-rip)

John Gruber在Daring Fireball撰文《比尔·阿特金森因癌症去世，享年74岁》，报道了苹果和计算机史上的关键人物比尔·阿特金森于2025年6月5日因胰腺癌去世，享年74岁。

文章重点介绍了阿特金森的重大贡献，特别是作为最初的Macintosh团队成员，他巧妙的代码和算法对于克服硬件的局限性至关重要。 Gruber指出，阿特金森的抖动算法是他播客“Dithering”的灵感来源。

除了像QuickDraw这样的底层贡献之外，阿特金森还因创造了MacPaint而备受赞誉，MacPaint被认为是Photoshop等位图图像编辑器的模型，以及HyperCard，据报道该程序灵感来自一次LSD之旅。 Gruber强调了HyperCard的重大影响。

Gruber断言，阿特金森可能是有史以来最好的计算机程序员，并把他列入候选名单。 该文章建议访问Andy Hertzfeld的Folklore.org网站，阅读有关阿特金森成就的故事。 阿特金森的遗孀、两个女儿、继子、继女、两个兄弟、四个姐妹以及他的狗尚在人世。

---

## 7. 自托管与技术独立：构建专属的乐趣

**原文标题**: Self-Host and Tech Independence: The Joy of Building Your Own

**原文链接**: [https://www.ssp.sh/blog/self-host-self-independence/](https://www.ssp.sh/blog/self-host-self-independence/)

本文受PewDiePie的DIY科技项目启发，提倡自主托管和技术独立。作者认为应该掌控自己的在线存在，从购买域名和托管自己的博客开始，强调其长期效益远胜于依赖WordPress或Medium等平台。他分享了自主托管博客、第二大脑、书籍、订阅者列表以及构建包含Gitea和PhotoPrism等各种服务的家庭实验室的个人历程，强调其中的学习和回报体验。

作者倡导技术独立，定义为不依赖特定公司或软件，并通过学习Linux基础知识来实现。他强调使用自建服务的乐趣，并避免订阅陷阱。他还强调开源的重要性，赞扬其协作精神以及贡献和学习他人代码的能力。他感谢Quartz、GoatCounter和Listmonk等他所使用的开源工具的创建者，感谢他们做出的宝贵贡献。

文章最后提到了其他有用的自主托管工具，如Paperless、Pi-hole和Syncthing，并重申了从自主托管中获得的乐趣和独立性。作者强调了公开分享知识和代码的重要性，并提及Markdown在内容创作中的广泛使用。他邀请大家在Bluesky上进行讨论，并鼓励读者探索他的dotfiles、博客和书籍。

---

## 8. 将照片转换为阿特金森抖动

**原文标题**: Convert photos to Atkinson dithering

**原文链接**: [https://gazs.github.io/canvas-atkinson-dither/](https://gazs.github.io/canvas-atkinson-dither/)

本文介绍了一个将图像转换为 Atkinson 抖动的简单工具。用户可以上传图像，然后从几个预设尺寸（50x50、320x240、512x384、640x480、800x600、1024x768）中选择，或者指定自定义尺寸。转换后的 Atkinson 抖动图像可以直接保存到用户的桌面。其核心功能是将图像转换为 Atkinson 抖动，并提供尺寸调整选项和便捷的保存位置。

---

## 9. 我在香港丛林中帐篷生活的实验

**原文标题**: My experiment living in a tent in Hong Kong's jungle

**原文链接**: [https://corentin.trebaol.com/Blog/8.+The+Homelessness+Experiment](https://corentin.trebaol.com/Blog/8.+The+Homelessness+Experiment)

因缺乏文章实际内容，我只能根据标题提供大致概要：

题为《我在香港丛林帐篷中的生活实验》的文章，很可能详细描述了 Corentin Trebaol 在香港丛林地区居住在帐篷中的经历。这篇文章很可能是一个关于这种自愿选择无家可归实验的第一手资料。

文章的主要预期要素可能包括：

*   **动机：** Trebaol 选择进行这项体验的原因。这可能包括对冒险的渴望、测试自给自足能力、提高对无家可归问题的认识，或多种因素的组合。
*   **准备：** Trebaol 为在丛林环境中生活所做的准备步骤，包括装备、物资和任何计划。
*   **地点细节：** 关于所选地点的具体信息，包括与地形、天气、野生动物和可达性相关的挑战。
*   **日常生活：** 对 Trebaol 日常生活的描述，包括寻找食物和水、搭建住所以及管理个人卫生。
*   **挑战和困难：** 遇到的障碍和困难，例如缺乏舒适感、与昆虫和动物打交道、适应环境以及潜在的法律或社会问题。
*   **见解和反思：** 从这次经历中获得的个人教训，包括对无家可归、自力更生和自然环境的更深入理解。
*   **影响：** 这次实验对 Trebaol 的观点和未来行动的总体影响。

标题“无家可归实验”表明该文章旨在探索无家可归者所面临的现实和挑战，即使是在受控和暂时的范围内。这很可能是一篇引人深思的文章，鼓励读者思考无家可归问题的复杂性以及人与自然的联系。

---

## 10. 焦点、语境与大型语言模型

**原文标题**: Focus and Context and LLMs

**原文链接**: [https://taras.glek.net/posts/focus-and-context-and-llms/](https://taras.glek.net/posts/focus-and-context-and-llms/)

本文探讨了作者使用大型语言模型（LLM）进行软件工程的经验和视角，特别关注“自主编码”方法的局限性。作者自2020年以来一直在使用LLM，最初发现它们在生成SQL语句等任务中很有价值，但对目前围绕自主编码代理的炒作持怀疑态度。

核心论点是，尽管LLM可以完成复杂的软件任务，但它们需要大量的人工指导和精心策划的上下文。作者引用了一个LLM编写的HTTP/2服务器的例子，强调了作者在提供正确上下文、微观管理LLM工作流程以及开发克服流式API调用和处理JSON等限制的策略方面投入的“大量工作”。工具调用是自主编码炒作的基础，但在此案例中被证明是不可靠的。

作者认为，LLM的输出质量仅与其提供的上下文质量相当。他批评“自主编程”类似于90年代的遗传算法炒作——蛮力可以奏效，但通常效率低下。作者认为，在开发出更好的上下文策划方法之前，LLM主要对能够提供高质量上下文和算法监督的经验丰富的工程师有效。最终，本文提倡务实的期望，并指出即使使用强大的LLM，平庸的上下文也会产生平庸的结果。

---

## 11. 考文垂超轻轨

**原文标题**: Coventry Very Light Rail

**原文链接**: [https://www.coventry.gov.uk/coventry-light-rail](https://www.coventry.gov.uk/coventry-light-rail)

这是考文垂超轻轨 (VLR) 项目的简要概述。内容包括新闻更新、车辆和轨道测试（包括路测预约）以及与 VLR 预约相关的隐私声明。同时引导读者点击“显示更多”以查看更多内容。

该文件提供了考文垂 VLR 项目的联系方式，包括实际地址（Coventry City Council, PO Box 7097, Coventry, CV6 9SL）和电子邮件地址 (CoventryVLR@coventry.gov.uk)。最后，它邀请读者注册 VLR 新闻邮件。主要重点似乎是向公众告知项目的进展情况，并提供保持信息畅通以及可能通过测试预约参与其中的方式。

---

## 12. Fray：JVM受控并发测试框架

**原文标题**: Fray: A Controlled Concurrency Testing Framework for the JVM

**原文链接**: [https://github.com/cmu-pasta/fray](https://github.com/cmu-pasta/fray)

Fray: Java并发测试工具，旨在帮助开发者查找和调试多线程代码中的竞态条件、死锁及其他并发问题。它采用概率并发测试和偏序抽样等技术来探索不同的线程交错。Fray还提供确定性重放，以便更轻松地调试已识别的问题。

该工具与流行的测试框架无缝集成。对于 JUnit 5，它提供了诸如 `@ConcurrencyTest` 和 `@ExtendWith(FrayTestExtension.class)` 之类的注解来标记和启用并发测试。对于其他框架，可以使用 `FrayInTestLauncher`。

Fray可以通过 Gradle 和 Maven 集成到构建过程中。文档中详细列出了两种构建系统的具体插件配置和依赖项。

文档包括技术报告、使用指南、IDE设置、使用Fray发现的bug列表以及项目贡献指南。该项目由美国国家科学基金会和亚马逊研究奖资助。

---

## 13. 人工智能时代的知识管理

**原文标题**: Knowledge Management in the Age of AI

**原文链接**: [https://ericgardner.info/notes/knowledge-management-june-2025](https://ericgardner.info/notes/knowledge-management-june-2025)

本文探讨了作者从使用Emacs进行个人知识管理到采用Obsidian的历程，其动力源于对一个要求较低但仍然强大的系统的渴望。作者最初拥抱Emacs的灵活性以及Org-Mode等工具，发现它赋予了自己力量，但最终由于需要不断定制和维护而感到疲惫。

为了寻找更友好的替代方案，作者过渡到了Obsidian，这是一个基于Markdown的笔记应用程序，拥有广泛的插件生态系统。为了有效地利用Obsidian，作者采用了PARA方法（项目、领域、资源、存档）来组织笔记和信息。该系统涉及使用不同的文件夹、一个收件箱、附件和模板目录以及顶层文件（如仪表板和待办事项列表）来构建一个“库”。

作者探讨了在人工智能时代为何要投资个人知识管理的问题，并表达了对过度依赖ChatGPT等人工智能工具可能导致外包个人思考的担忧。作者认为，维护个人知识库（例如在Obsidian中构建的知识库）对于培养有意的、深思熟虑的思考，珍视自己的想法，以及从个人知识中汲取经验而不是仅仅依赖人工智能至关重要。他们还建议可以将个人知识管理与人工智能工具集成，人工智能充当助手，增强和告知用户自己的想法和工作。最终，作者提倡在日益人工智能化的世界中保持对自身思考和创造力的掌控。

---

## 14. 超越维度，扭曲现实的打印机

**原文标题**: The printer that transcends dimensions and corrupts reality

**原文链接**: [https://ghuntley.com/ideas/](https://ghuntley.com/ideas/)

本文讲述了一个幽默的轶事，作者探索大型语言模型（LLM）的创造潜力。文章回顾了与Claude的一次聊天会话，作者挑战人工智能不断“改进”，从使用LPR打印系统进行弹性批处理作业的基本概念开始。

文章重点介绍了LLM在试图改进最初的想法时，所采取的意想不到且越来越荒谬的方向。提示从基本的代码建议演变为整合先进技术，如形式验证组件、自我修复行为，最终，量子弹性共识、神经形态作业调度，甚至量子计算。

作者对LLM不断升级的雄心感到有趣，最终通过要求打印机打开星际之门（Stargate SG-1）的虫洞，将其推向了彻底的荒谬。这导致LLM生成了包含科幻小说中虚构技术和概念的代码，例如纳克拉反应堆和亚空间缓冲器。最终，LLM开发了一个“亚特兰蒂斯防御”模块，其中包含飞马防御和幽灵反制等概念。

核心信息是LLM在获得开放式提示时产生新颖想法的能力，以及将其推向创造性极限时产生幽默和意外结果的潜力。这是一个有趣的演示，展示了LLM如何用于头脑风暴和想法生成，即使最终结果是幻想和不切实际的。

---

## 15. 用 Claude 发布实际代码的现场笔记

**原文标题**: Field Notes from Shipping Real Code with Claude

**原文链接**: [https://diwank.space/field-notes-from-shipping-real-code-with-claude](https://diwank.space/field-notes-from-shipping-real-code-with-claude)

本文《使用 Claude 发布真实代码的实地笔记》探讨了人工智能辅助开发的实用方法，超越了“凭感觉编码”的玩笑，走向了功能性的现实。它侧重于通过战略性地利用人工智能的优势并减轻其劣势，来实现 10 倍的生产力提升。

文章概述了 Julep 使用的基础设施，强调了 `CLAUDE.md` 文件的重要性，该自定义文档充当项目约定、编码风格和关键架构决策的单一事实来源。它介绍了代码中的“锚点注释”，以指导人工智能并改进人类可读的文档。

然后，它详细介绍了三种不同的人工智能辅助开发模式：“游乐场”用于快速原型设计，“结对编程”用于较小项目（约 5000 行代码）的结构化协作，以及“生产/单体仓库规模”用于大型代码库，目前需要重要的边界和人工监督。这种模式突出了坚持可靠工程原则的关键重要性，尤其是在大规模情况下。

文章强调，即使有人工智能的帮助，编写测试仍然至关重要。主要收获包括：人工智能可以起草、结对编程和验证，但人类仍然负责架构；良好的开发实践会成倍增加人工智能的益处；`CLAUDE.md` 充当代码库的章程。文章提倡从代码编写者转变为代码编辑者，利用人工智能提高效率，同时保持对整个系统设计和功能的控制。

---

## 16. BorgBackup 2不再有服务器端只追加模式

**原文标题**: BorgBackup 2 has no server-side append-only anymore

**原文链接**: [https://github.com/borgbackup/borg/pull/8798](https://github.com/borgbackup/borg/pull/8798)

此 GitHub issue 讨论了 BorgBackup 2 中移除服务端只追加存储库支持的问题。原始的 BorgBackup 1.x 通过服务端组件为 SSH 存储库实现了只追加功能。 然而，BorgBackup 2 支持各种存储库类型（fs、sftp、rclone、s3/b3、ssh），并且只有 SSH 方法保留了能够强制执行此类功能的服务端进程。

作者 ThomasWaldmann 解释说，只追加功能将从 Borg 的核心功能中移除。新的方法建议利用存储层的权限系统。 与依赖 Borg 的内部服务端强制执行不同，现在的想法是配置存储访问权限，使得 "borg create" 命令使用缺少删除权限的凭据，而 "borg compact" 使用具有删除权限的凭据。 这确保了可以创建备份而无需允许删除现有数据，从而有效地实现只追加行为。

评论者 Wqrld 最初对通过未经授权的写入可能导致的数据损坏表示担忧，但 ThomasWaldmann 澄清说，“禁止删除”权限也阻止了覆盖现有对象。 其中还包括指向 Hacker News 和其他提到此更改的每日新闻聚合器的多个链接，表明其公众关注度。

---

## 17. 研究人员开发“透明纸”作为塑料替代品

**原文标题**: Researchers develop ‘transparent paper’ as alternative to plastics

**原文链接**: [https://japannews.yomiuri.co.jp/science-nature/technology/20250605-259501/](https://japannews.yomiuri.co.jp/science-nature/technology/20250605-259501/)

日本海洋研究开发机构(JAMSTEC)的研究人员开发出一种可生物降解的透明纸，作为塑料的潜在替代品。这种纸由棉籽纤维中提取的纤维素制成，可被微生物分解成水和二氧化碳。

研究人员将纤维素粉末溶解在溴化锂水溶液中，制成凝胶，然后进行塑形和干燥。由此产生的材料强度与聚碳酸酯塑料相当，即使厚度为0.7毫米仍保持柔韧性，并具有清晰的透明度。

测试表明，该纸在海水中四个月内即可溶解，即使在相当大的深度也是如此，尽管在微生物较少的较深区域，溶解过程较慢。虽然纸质包装是目前塑料容器的替代品，但消费者通常更喜欢看到包装内的物品，而透明纸则解决了这一问题。

虽然大规模生产需要专门的工厂，但研究人员估计生产这种透明纸的成本约为普通纸的三倍。然而，生产过程中的二氧化碳排放量约为塑料的一半。大阪大学的一位专家强调，这种材料优于其他透明纸的优势在于其在深海中已被证实的生物降解性。

---

## 18. Radiant AI 到底是什么？

**原文标题**: What was Radiant AI, anyway?

**原文链接**: [https://blog.paavo.me/radiant-ai/](https://blog.paavo.me/radiant-ai/)

本文深入探讨了辐射AI的历史与现实，辐射AI是《上古卷轴IV：湮没》中备受期待的功能，在发售前曾引起广泛关注。作者旨在剖析辐射AI的最初设计意图、最终游戏中的实际表现，以及其对后续Bethesda作品的影响。

本文追溯辐射AI自2004年公布以来的历程，考察了GameInformer的封面故事以及对Todd Howard的后续采访，重点强调了关于构建一个拥有1000名NPC的动态、鲜活世界，这些NPC具有自主的时间表和决策能力的承诺。文中分析了2005年E3展会的演示，着重介绍了它如何展示NPC的所谓自主性。

作者探讨了粉丝的观点，从访谈和论坛讨论中汲取信息，以了解围绕辐射AI的期待和后来的失望。本文涵盖了AI系统的技术方面：角色属性、AI包、时间表，以及这些元素如何相互作用以产生涌现行为。

本文挑战了常见的误解，回顾了早期的说法、E3演示以及关于该系统怪癖的轶事。它将辐射AI与更先进的AI技术——目标导向行为规划（GOAP）进行了对比，并推测了它在Bethesda后续游戏，如《辐射3》、《天际》和《星空》中的应用。文中探讨了设计如何在后来的游戏中转向“辐射故事”。最终，本文旨在对辐射AI是什么、它在哪些方面未能兑现承诺，以及它对Bethesda游戏设计理念的影响，提供一个全面且研究充分的解释。

---

## 19. 为什么不使用基于HTTPS的DNS (DoH)？

**原文标题**: Why not use DNS over HTTPS (DoH)?

**原文链接**: [https://www.bsdhowto.ch/doh.html](https://www.bsdhowto.ch/doh.html)

本文反对采用基于HTTPS的DNS（DoH），声称这并非是为了保护用户隐私免受各种观察者的窥探，而是为了将DNS查询数据集中到一个提供商手中，通常是像Cloudflare这样的商业实体。

作者认为，DoH倡导者强调加密是为了保护DNS查询免受ISP和网络管理员的窥视，但这种好处是以将所有DNS数据转移到一个“窥视者”手中为代价的。他们担心像Cloudflare这样的公司，为了将其服务货币化，可能会出售这些数据。

作者建议采用基于TLS的DNS（DoT）作为更好的替代方案，因为它提供了传输加密，而无需依赖HTTP作为传输协议。他们并不反对DNS现代化或安全改进，但认为DoH增加了不必要的复杂性和潜在漏洞，因为它需要额外的HTTP基础设施。核心论点是，DoH将隐私风险从多个潜在观察者转移到一个单一的、中心化的实体，而该实体具有利用用户数据的商业动机。文章建议Firefox用户通过将`network.trr.mode`设置为5来禁用DoH。

---

## 20. 我们为何放弃 Nix

**原文标题**: Why We're Moving on from Nix

**原文链接**: [https://blog.railway.com/p/introducing-railpack](https://blog.railway.com/p/introducing-railpack)

由于在将 Nixpacks 扩展到更大用户群时遇到限制，Railway 正在用一种名为 Railpack 的新构建器取代 Nixpacks。虽然 Nixpacks 对大多数人有效，但仍有相当数量的用户每天都面临问题。

Nixpacks 的主要问题是它依赖于 Nix 基于提交的软件包版本控制，这使得精确的版本控制和维护变得困难。更新一个软件包版本常常会对其他软件包造成意想不到的后果，并可能导致用户的构建失败。此外，由于无法将依赖项分离到不同的层中，以及注入的环境变量使缓存失效，Nixpacks 对 Nix 的使用导致镜像体积庞大和缓存问题。

Railpack 通过以下方式解决这些问题：

*   **精细化版本控制：** 支持 major.minor.patch 版本。
*   **更小的构建体积：** 显著减小镜像体积 (38-77%)。
*   **更好的缓存：** 使用 BuildKit 提供对层缓存的更多控制。
*   **从 Nix 过渡：** 使用 Mise 进行软件包安装。

Railpack 使用 Go 构建，并使用自定义的 BuildKit LLB + Frontend 进行精确的镜像构建。它的工作原理是分析代码，创建一个基于 JSON 的构建计划，然后构建一个 BuildKit 构建图。这提供了更好的依赖锁定、改进的环境变量管理和优化的缓存。Railpack 还支持零配置的静态站点部署，例如 Vite、Astro、CRA 和 Angular。

Railpack 目前处于 Beta 版，支持 Node、Python、Go、PHP 和静态 HTML 部署。它也是开源的，可在 railpack.com 上获取。

---

## 21. 使用Zig进行底层优化

**原文标题**: Low-Level Optimization with Zig

**原文链接**: [https://alloc.dev/2025/06/07/zig_optimization](https://alloc.dev/2025/06/07/zig_optimization)

本文推崇 Zig 语言，认为它尤其适合底层优化。文章指出，虽然现代编译器功能强大，但理解和引导它们对于实现最佳性能至关重要。底层语言的优势在于允许开发者清晰地表达*意图*，从而为编译器提供更多的优化信息。

Zig 在这方面表现出色，这归功于它的冗长性以及非可选指针、编译时计算 (comptime) 和明确定义的非法行为等特性，这些特性为 LLVM 提供了充分的优化信息。Zig 的 `comptime` 是一个关键亮点，它是一种元编程特性，允许代码在编译时运行。这使得代码生成、编译时常量求值和类型特定优化成为可能，这些优化超越了某些其他语言中的宏的功能。

文章以字符串比较为例，演示了 `comptime` 如何生成高度优化的汇编代码，根据对其中一个字符串的编译时了解来定制比较逻辑。它还展示了如何实现运行时分派到编译时专用函数。

作者总结说，`comptime` 是一种强大的工具，可以简化代码生成，并消除对许多传统元编程技术的需求。他认为，Zig 在功能和可用性之间取得了良好的平衡，使得在实际场景中编写高性能代码变得更容易。文章最后呼吁结束语言之争，提倡关注计算能力的全局，同时仍然承认个人语言偏好。

---

## 22. 克服拖延

**原文标题**: Getting Past Procrastination

**原文链接**: [https://spectrum.ieee.org/getting-past-procastination](https://spectrum.ieee.org/getting-past-procastination)

题为“克服拖延症”的这篇文章由Taro创始人、科技职业人士职业平台创始人Rahul Pandey撰写。其核心信息是，个人可以通过实施有效的系统来克服拖延症并实现持续的生产力。尽管所提供的摘录内容未详细说明具体系统，但中心思想强调采取积极主动的方式来管理时间和任务。这篇文章很可能探讨旨在提高生产力并最大限度减少拖延症的策略和框架，目标读者是旨在改善职业发展轨迹的专业人士。该文章的发表日期是2025年6月5日，预计阅读时间为3分钟。“CareersGuest Article”表明它是专注于职业建议和发展的系列文章的一部分。

---

## 23. 我们如何将 GitLab 仓库备份时间从 48 小时缩短到 41 分钟

**原文标题**: How we decreased GitLab repo backup times from 48 hours to 41 minutes

**原文链接**: [https://about.gitlab.com/blog/2025/06/05/how-we-decreased-gitlab-repo-backup-times-from-48-hours-to-41-minutes/](https://about.gitlab.com/blog/2025/06/05/how-we-decreased-gitlab-repo-backup-times-from-48-hours-to-41-minutes/)

GitLab通过解决`git bundle create`命令中的性能瓶颈，将仓库备份时间从48小时大幅缩短至41分钟。该问题源于一个15年前的Git函数`object_array_remove_duplicates()`，该函数使用O(N²)算法处理大型仓库中的重复引用，导致处理时间随着引用数量的增长呈指数级增加。

GitLab使用火焰图识别出该问题，发现该函数在备份操作期间占用了80%的执行时间。为了解决这个问题，他们向上游Git贡献了一个补丁，用映射数据结构替换了嵌套循环，将复杂度降低到更有效的映射。这一改变极大地提高了性能，基准测试表明速度提高了6倍。

备份速度的提高为GitLab客户带来了显著的好处，包括能够在不影响性能的情况下实施全面的每晚备份计划，最大限度地减少恢复点目标(RPO)，降低运营成本，并在代码库增长时为基础设施提供未来保障。该修复程序从18.0版本开始向所有GitLab客户提供，代表了GitLab对可扩展的企业级Git基础设施的承诺。GitLab还强调了修复程序的协作性质，强调该修复程序已向上游贡献，以造福更广泛的Git社区。

---

## 24. 在光盘表面刻录可见图像的工具 (2022)

**原文标题**: A tool for burning visible pictures on a compact disc surface (2022)

**原文链接**: [https://github.com/arduinocelentano/cdimage](https://github.com/arduinocelentano/cdimage)

CDImage是一款2022年推出的工具，允许用户将可见图片刻录到CD表面。该项目灵感来源于“argon”和“[unDEFER]”的早期尝试，CDImage部分使用了他们的坐标转换代码和光盘几何参数。作者最初的目标是开发一个用户友好的GUI，但由于不同CD品牌和类型之间的校准困难，于2008年放弃。最近重新发现了这段代码后，作者将其更新到Qt6，并以此向CD时代致敬，希望其他人可能会觉得它有用。

构建CDImage需要Qt 6库。为不希望自行构建的用户提供了一个Windows二进制文件。一个关键方面是光盘校准；该软件在已知光盘几何结构的情况下效果最佳。该软件在“创建音轨”对话框中提供了一个已知光盘列表，但可以手动输入几何参数，尽管很困难。作者警告说，在校准尝试过程中可能会损坏光盘。

使用方法包括加载图像，调整其大小和位置，选择CD型号，以及生成一个大型音轨。然后，需要使用支持Audio CD创建的刻录软件将该音轨刻录到CD上。

“校准”部分详细介绍了为未知光盘寻找最佳几何参数的挑战。作者探索了各种方法，包括交互式方法和使用寻道时间延迟或AI驱动的图像识别进行潜在的自动化。作者最终寻求社区对改进校准技术的投入。列出了几个用于进一步研究的资源，包括有关早期项目、红皮书标准以及与光驱相关的硬件逆向工程的信息。

---

## 25. 发现JDK竞态条件，并用Fray在30分钟内调试完毕

**原文标题**: Discovering a JDK Race Condition, and Debugging It in 30 Minutes with Fray

**原文链接**: [https://aoli.al/blogs/jdk-bug/](https://aoli.al/blogs/jdk-bug/)

本文详细介绍了使用 Fray 工具发现并调试 JDK 中 `ScheduledThreadPoolExecutor` 的竞态条件的过程。作者在 Fray 的集成测试过程中遇到了死锁，问题出在看似无害的代码上，涉及任务调度和关闭执行器。

核心问题在于 `schedule` 和 `shutdown` 方法的交错执行。当执行器转换到 `SHUTDOWN` 状态时，`schedule` 方法可能会在未为任务添加 worker 的情况下返回，并假定关闭过程会终止该任务。然而，如果关闭在任务中断之前完成，任务就会陷入僵局，导致 `FutureTask.get()` 永久阻塞。

本文重点介绍了 Fray 的确定性重放和调度可视化功能对于理解和调试这个并发错误的关键作用。传统的调试方法，如日志记录和调试器，通常会掩盖问题。Fray 允许作者逐步执行精确的线程交错，并观察导致死锁的状态转换。

作者概述了使用 Fray IntelliJ 插件重现该错误的步骤，包括使用特定配置运行和重放测试。文章最后提到，在向 JDK 团队报告该错误时，使用 sleep 语句来触发该错误的补丁被认为是不必要的，因为 Fray 重放文件提供了一种充分且可靠的重现和调查方法。

---

## 26. Cloudflare AI 编写的 OAuth 库一览

**原文标题**: A look at Cloudflare's AI-coded OAuth library

**原文链接**: [https://neilmadden.blog/2025/06/06/a-look-at-cloudflares-ai-coded-oauth-library/](https://neilmadden.blog/2025/06/06/a-look-at-cloudflares-ai-coded-oauth-library/)

OAuth专家尼尔·马登审查了Cloudflare使用Anthropic的Claude LLM大量编写的OAuth提供程序库，以验证他的怀疑态度。尽管最初印象是代码结构良好且有一些测试，但马登发现了一些关键问题。测试不充分，缺乏对规范和滥用案例的全面覆盖。他强调了一个“YOLO CORS”实现，该实现有效地禁用了同源策略，并且缺乏标准安全标头，可能暴露漏洞。

马登还指出了有问题的问题选择，例如为公共客户端实现已弃用的隐式授权以及不正确的Basic Auth支持。在令牌ID生成中发现了一个更严重的错误，该错误产生有偏差的输出并降低了熵。他对加密实现印象深刻，这是一个由人类工程师驱动但由Claude辅助的设计，突显了在将LLM用于安全敏感代码时需要深厚专业知识。

马登总结说，虽然对于初稿来说代码并不糟糕，但它还没有达到可以投入生产的程度，并强调了创建正确且安全的OAuth实现的难度。他强调，仅仅依靠LLM来构建如此关键的系统是不明智的，因为即使经过代码审查，也可能遗漏细微但意义重大的缺陷。他警告说，在让LLM为你编写代码之前，你需要真正理解你正在构建的代码和系统。

---

## 27. 引发大规模科技裁员的税法定时炸弹

**原文标题**: The time bomb in the tax code that's fueling mass tech layoffs

**原文链接**: [https://qz.com/tech-layoffs-tax-code-trump-section-174-microsoft-meta-1851783502](https://qz.com/tech-layoffs-tax-code-trump-section-174-microsoft-meta-1851783502)

本文认为，美国税法第174条一项鲜为人知的修改，这项修改隐藏在2017年的《减税与就业法案》中，是过去两年大规模科技公司裁员的重要原因。在近70年的时间里，第174条允许公司立即扣除100%的合格研发支出。2017年的修改要求公司在五年或十五年内摊销这些扣除额，实际上增加了它们的税收负担。

文章认为，这种转变使得研发成本更高，特别是对于尚未盈利的公司而言，这与风险投资的下降和利率的上升同时发生。虽然公司将裁员归咎于过度招聘和人工智能，但内部电子表格和财务报表揭示了税法修改的影响。Meta、微软、亚马逊和Salesforce等大型科技公司，以及Twilio和Shopify等较小的公司，都经历了集中在研发、产品和工程领域的重大裁员。

除了科技行业，这一变化影响了任何投资于内部软件开发或数据驱动产品开发的企业。通过取消立即注销，税收保护消失了，仍在烧钱的公司突然在账面上看起来有利可图，从而引发了对虚构收益的实际税单。因此，这一变化对公司投资美国制造的技术和数字产品产生了抑制作用。虽然两党都在努力废除这一变化，但对于许多已经下岗的工人来说，可能为时已晚。

---

## 28. 我读了 Cloudflare 所有 Claude 生成的提交。

**原文标题**: I read all of Cloudflare's Claude-generated commits

**原文链接**: [https://www.maxemitchell.com/writings/i-read-all-of-cloudflares-claude-generated-commits/](https://www.maxemitchell.com/writings/i-read-all-of-cloudflares-claude-generated-commits/)

Max Mitchell 的文章详细介绍了 Cloudflare 使用 Claude 生成 OAuth 2.1 库的经验，重点在于人类工程师和 AI 之间的协作过程。最初持怀疑态度的首席工程师发现 Claude 能够生成几乎所有代码。

一个关键要素是将提示包含在提交信息中，将 git 历史记录转换为意图记录，并将人类推理与机器实现连接起来。这种透明度允许审查和理解 AI 的逻辑。

该文章强调了有效的提示策略，例如“示例提示”和提供清晰的、反映同事互动的上下文反馈。使用 AI 生成文档也很轻松。

然而，Claude 在移动代码块和处理复杂的搜索和替换操作等任务上遇到困难，需要手动干预。在项目接近尾声时，用于样式和整理的手动提交变得更加频繁。

Mitchell 提供了使用 AI 编码工具的实用建议：专注于交付成果，将提示视为版本控制的资产，预期多轮提示，并准备好手动干预。

文章随后探讨了将提示视为源代码的想法，设想未来提示经过版本控制，并用于随着模型的改进重新生成代码，从而可能完全消除代码生成步骤。

最终，该经验展示了一种新的创意动态，其中 AI 处理实现，而人类提供指导、背景和判断。虽然存在局限性，但这种协作展示了 AI 编码工具的潜力，尤其是在它们不断改进的情况下。

---

## 29. 资助 FreeBSD 开发的一年

**原文标题**: A year of funded FreeBSD development

**原文链接**: [https://www.daemonology.net/blog/2025-06-06-A-year-of-funded-FreeBSD.html](https://www.daemonology.net/blog/2025-06-06-A-year-of-funded-FreeBSD.html)

本文详细介绍了作者为期一年的由资助的FreeBSD开发工作，主要集中在改进FreeBSD在Amazon EC2上的运行。最初，作者个人的FreeBSD/EC2工作受到了其作为FreeBSD发布工程负责人的角色的阻碍。随后，亚马逊赞助作者每月40小时来从事这两项工作，并跟踪所花费的时间。

作者重点介绍了管理四个FreeBSD版本（13.4、14.2、13.5和即将发布的14.3），详细介绍了每个版本的过程和工作量。在EC2方面，亚马逊优先开发了Graviton实例的“电源驱动程序”，以实现正常关机，以及EBS卷的热插拔支持，特别是修复了在具有ACPI怪癖的各种实例类型上遇到的热拔插问题。

除了亚马逊的优先级之外，作者还解决了FreeBSD启动时间性能下降的问题。调查显示，问题与根磁盘大小、Graviton 2实例上的内核熵播种以及ZFS池验证有关。解决方案包括增加根磁盘大小、改进熵播种以及改变ZFS事务组处理方式。还及时修复了`aws-ec2-imdsv2-get`端口中与IPv6相关的问题。

最后，作者扩展了可用FreeBSD AMI风味的范围，增加了“小型”AMI（通过删除不必要的组件来缩小尺寸）和构建器AMI。本文强调了平衡发布工程与EC2特定开发工作的挑战，以及亚马逊赞助的积极影响。

---

## 30. 理解软件周期时间为何复杂而非神奇

**原文标题**: Why Understanding Software Cycle Time Is Messy, Not Magic

**原文链接**: [https://arxiv.org/abs/2503.05040](https://arxiv.org/abs/2503.05040)

此arXiv论文《没有银弹：为何理解软件周期时间是复杂的，而非神奇的》探讨了使用周期时间作为衡量软件开发速度指标的复杂性。作者Flournoy、Lee、Wu和Hicks使用贝叶斯分层建模方法分析了来自216个组织的超过55000个观测值的数据集。这种方法使他们能够分离个体和组织的变化，从而更细致地理解周期时间的动态。

该研究调查了编码时间、任务范围界定和协作模式等因素对周期时间的影响。虽然他们发现周期时间与诸如每周编码天数、合并的拉取请求数量和协作水平等因素之间存在统计上的显著（尽管不大）关联，但仍有大量变化无法解释。这表明存在许多隐藏或混淆因素。

主要结论是，仅依靠周期时间测量来评估软件工作可能会产生误导。个体内部和个体之间的大量未解释的变化限制了任何单一观察结果提供的关于典型绩效的信息。作者认为，提高软件交付速度需要系统层面的视角，而不是仅仅关注个别干预措施。该论文强调了周期时间作为一种万能解决方案的局限性，并提倡对影响软件开发速度的因素进行更全面的理解。

---

## 31. 华盛顿邮报隐私建议：停止使用Chrome，删除Meta应用程序（和Yandex）

**原文标题**: Washington Post's Privacy Tip: Stop Using Chrome, Delete Meta Apps (and Yandex)

**原文链接**: [https://tech.slashdot.org/story/25/06/07/035249/washington-posts-privacy-tip-stop-using-chrome-delete-metas-apps-and-yandex](https://tech.slashdot.org/story/25/06/07/035249/washington-posts-privacy-tip-stop-using-chrome-delete-metas-apps-and-yandex)

据《华盛顿邮报》一位科技专栏作家称，Meta（Facebook和Instagram）和Yandex被发现规避了Android的隐私保护措施，即便在启用隐私设置的情况下，也在窃取用户数据。 这突显了网页浏览器和应用程序中的漏洞。

该文章建议读者从Google Chrome切换到诸如Mozilla Firefox、Brave或DuckDuckGo等浏览器，这些浏览器能提供更好的跟踪保护。 虽然承认并不完美，但还是推荐在iPhone和Mac上使用Safari。 研究人员发现，Android上的Firefox部分容易受到已确认的数据收集策略的影响。

该文章强烈建议从手机上删除Meta和Yandex的应用程序，认为这些公司已被证明不可信，并且这些应用程序允许收集更多敏感数据，例如位置、电池电量和连接的设备，而这些数据通常是网站无法访问的。

文章最后提醒说，即使不使用Meta应用程序或Facebook/Instagram，Meta仍然可以在整个网络上跟踪用户活动。

---

## 32. FAIR软件包管理器：去中心化的WordPress基础设施

**原文标题**: The FAIR Package Manager: Decentralized WordPress infrastructure

**原文链接**: [https://joost.blog/path-forward-for-wordpress/](https://joost.blog/path-forward-for-wordpress/)

本文宣布启动 FAIR (Federated and Independent Repositories，联邦式独立仓库) 项目，旨在实现 WordPress 基础设施的去中心化并改善治理。 受到对 WordPress 生态系统中中心化控制和缺乏透明治理的担忧的驱动，FAIR 为 WordPress 插件、主题和其他资源提供了一种替代分发层。

该项目建立在 AspirePress 等现有工作的基础上，并解决了更新瓶颈和可发现性等问题。 FAIR 不会分叉 WordPress，而是提供一个独立于 WordPress.org 管理的兼容系统。 它允许用户选择插件的交付方式，并享受更去中心化的体验。

现在，FAIR 已成为 Linux 基金会旗下的一个技术项目，由社区主导的技术指导委员会 (TSC) 管理，领导者包括 Carrie Dils、Mika Epstein 和 Ryan McCue。 它提供联邦就绪镜像、商业插件支持和加密签名等功能。

作者强调，FAIR 是对 WordPress 的协作贡献，而不是抗议或分叉。 它的目标是提供更好的基础设施和更负责任的治理，邀请所有相信开放网络和 WordPress 未来共享控制的人加入该项目。 更多信息请访问 fair.pm。

---

## 33. 马斯克与特朗普争端延烧至SpaceX合同威胁

**原文标题**: Musk-Trump dispute includes threats to SpaceX contracts

**原文链接**: [https://spacenews.com/musk-trump-dispute-includes-threats-to-spacex-contracts/](https://spacenews.com/musk-trump-dispute-includes-threats-to-spacex-contracts/)

文章详细描述了前总统特朗普和埃隆·马斯克之间的一场公开争端，该争端升级为针对SpaceX政府合同的威胁。冲突源于马斯克批评一项由特朗普支持的预算协调法案，导致特朗普威胁要取消与SpaceX的政府合同。马斯克最初回应称SpaceX将“退役”其龙飞船，但后来又撤回了这一威胁。

潜在的合同取消引发了人们对SpaceX（预计从NASA和国防部的工作中获得可观收入）以及政府（严重依赖SpaceX的发射服务，包括向国际空间站运送宇航员和货物）的影响的担忧。美国宇航局新闻秘书表示，该机构将继续执行总统的愿景并与行业合作伙伴合作。

文章还提到了特朗普撤回贾里德·艾萨克曼担任美国宇航局局长的提名，理由是艾萨克曼是民主党人。特朗普指派没有航天背景的丹·凯恩将军挑选新的提名人，这引发了人们对挑选过程的质疑。

---

## 34. 思考的幻觉：理解推理型LLM的局限性 [pdf]

**原文标题**: The Illusion of Thinking: Understanding the Limitations of Reasoning LLMs [pdf]

**原文链接**: [https://ml-site.cdn-apple.com/papers/the-illusion-of-thinking.pdf](https://ml-site.cdn-apple.com/papers/the-illusion-of-thinking.pdf)

思考的幻觉：理解推理大语言模型的局限性

本文可能探讨大型语言模型(LLM)所表现出的推理的欺骗性。尽管LLM在生成类人文本和执行看似需要理解的任务方面表现出色，但本文可能认为，LLM并没有像人类那样真正地“思考”或“推理”。

基于标题和PDF结构，文章可能深入研究LLM的底层机制，揭示它们如何依赖于训练数据中的统计模式和相关性，而不是真正的理解。文章可能讨论LLM在以下领域的局限性：

*   **因果推理：** 无法理解超出简单统计关联的因果关系。
*   **抽象推理：** 在训练数据中没有充分体现的新情况或概念方面的困难。
*   **常识：** 缺乏对现实世界的知识和对人类隐含假设的理解。
*   **偏见与公平：** 延续或放大训练数据中存在的偏见。

本文旨在对LLM提供更现实的评估，告诫人们不要过分夸大它们的能力，并强调需要继续研究更强大和可靠的AI系统，以克服这些局限性。通过揭示“思考的幻觉”，作者可能主张对当前LLM的状态采取更批判性和知情的视角。PDF标记的包含暗示了文章的结构化格式（章节、小节等），使其适合学术讨论。

---

## 35. 基于代数方法的抽象视觉推理

**原文标题**: Abstract visual reasoning based on algebraic methods

**原文链接**: [https://www.nature.com/articles/s41598-025-86804-3](https://www.nature.com/articles/s41598-025-86804-3)

本文提出了一种抽象视觉推理的新方法，旨在通过模仿人类认知能力来提高机器智能。其核心思想是从复杂的视觉数据中提取高阶抽象模式，特别是在瑞文推理测验（RPM）谜题的背景下。

所提出的模型利用关系瓶颈方法来连接代数运算和机器推理。它将多视觉推理问题显式地转换为0-1关系瓶颈矩阵，通过比较和观察序列特征来识别系统不变性。通过Slot Attention机制学习到的以对象为中心的表示被整合，以提供强大的归纳偏置，鼓励关系比较和抽象模式的提取。该Slot Attention模块学习突出显示单个对象，以无监督的方式完成图像分割，并实现对多输入视觉图像的全面理解。

该模型旨在克服传统神经符号方法的局限性，这些方法往往过度拟合视觉特征。关系瓶颈限制了信息处理，使其专注于视觉对象之间的关系，从而促进了类似于相似性关系的抽象机制的出现。这使得可以快速学习关系模式并进行系统泛化。

在I-RAVEN数据集上的实验结果表明，总准确率达到96.8%，超过了最先进的基线方法，并超越了人类的表现。本文的主要贡献是构建了代数运算和机器推理之间的桥梁，建立了一个具有强大归纳偏置的推理框架，并建立了一个模拟人类思维过程的反馈机制。

---

## 36. 烟囱为何如此之高？

**原文标题**: Why are smokestacks so tall?

**原文链接**: [https://practical.engineering/blog/2025/6/3/why-are-smokestacks-so-tall](https://practical.engineering/blog/2025/6/3/why-are-smokestacks-so-tall)

烟囱为何如此高：空气污染管理的视角

本文解释了烟囱为何如此高，重点关注其在空气污染管理中的作用。虽然消除排放是理想选择，但烟囱有助于稀释和扩散污染物，以最大限度地减少其对公众健康的影响。

现代工业厂房采用控制技术来去除排放前的大部分污染物。然而，对于残留污染物，“稀释是解决污染的方法”在局部范围内仍然有效。烟囱利用热废气羽流的浮力将其带到大气高处，以便更好地扩散。这种浮力是由烟囱内部和外部空气之间的温差产生的，并由烟囱高度增强。更高的烟囱会产生更大的压力差，从而驱动气流和污染物扩散。

虽然最初旨在提高燃烧效率，但烟囱已发展成为环境工程的关键工具。设计烟囱需要考虑羽流冷却、烟囱内部的摩擦以及大气条件。风、湍流和大气稳定性（稳定、不稳定、逆温）等因素会显著影响羽流行为，导致不同的羽流形状（锥形、环状、扇形、滞留、抬升、熏蒸）和污染物扩散模式。复杂的模型被用来预测污染物浓度并确保符合空气质量标准，同时考虑受控排放和更广泛的环境因素。

---

## 37. OneText (YC W23) 招聘 DevOps/DBA 首席工程师

**原文标题**: OneText (YC W23) Is Hiring a DevOps/DBA Lead Engineer

**原文链接**: [https://jobs.ashbyhq.com/one-text/b95952a2-9bc2-4c3a-9da1-3dcc157b4a27](https://jobs.ashbyhq.com/one-text/b95952a2-9bc2-4c3a-9da1-3dcc157b4a27)

这是一篇OneText (YC W23) DevOps/DBA主管工程师的招聘启事。文章本身只是一个占位符，提示用户需要启用JavaScript才能查看招聘信息。因此，唯一确定的信息是：

*   **公司：** OneText
*   **阶段：** YC W23 (表明他们是Y Combinator 2023年冬季批次成员)
*   **职位：** DevOps/DBA主管工程师
*   **地点：** 未明确说明，但可能远程或位于与YC创业公司相关的地区。

用户需要启用JavaScript才能查看完整的职位描述，以获取任何实际信息。

---

## 38. 海豚模拟器进度报告：发布版2506

**原文标题**: Dolphin Emulator Progress Report: Release 2506

**原文链接**: [https://dolphin-emu.org/blog/2025/06/04/dolphin-progress-report-release-2506/](https://dolphin-emu.org/blog/2025/06/04/dolphin-progress-report-release-2506/)

Dolphin模拟器发布2506进度报告：重点改进和新增功能。一项关键进展是**颗粒合成音频系统**，它解决了减速情况下的音频延迟问题。该系统不是依赖音频拉伸（增加延迟）或遭受音频爆音，而是通过重复最后一个采样来填补音频空白，从而在轻微减速时提供更流畅的音频，而不会增加延迟。

另一个重要的改进领域是**帧步调**。包括增加节流粒度和调整视频定时参数在内的多项更改，已显著提高了帧交付的一致性并减少了抖动，从而改善了整体视觉体验。

此外，**各向异性过滤**得到了改进。Dolphin现在可以遵循游戏自身对各向异性过滤的请求，与之前的“全有或全无”方法相比，提供更真实的视觉体验。

该报告还承认了先前版本的问题，导致发布了热修复程序(2503a)以及后续的版本控制怪癖。Windows和macOS的最低支持版本已分别提升至Windows 10 1903和macOS 11 Big Sur，以利用更新的API和标准。最后，还增加了Wii Speak模拟。

---

## 39. 你需要更少的内存，而不是更多的时间。

**原文标题**: You need much less memory than time

**原文链接**: [https://blog.computationalcomplexity.org/2025/02/you-need-much-less-memory-than-time.html](https://blog.computationalcomplexity.org/2025/02/you-need-much-less-memory-than-time.html)

2025年2月26日的这篇博文讨论了 Ryan Williams 在复杂性理论方面的一项重大突破。 Williams 的 STOC 论文证明，任何在 *t(n)* 时间内运行的算法都可以在 *√(t(n)log t(n))* 空间内模拟，这是对先前最佳界限 *t(n)/log t(n)* 的显著改进。 这标志着空间（内存）和时间限制之间的明显差异，因为空间可以重复使用，而时间不能。

Williams 的证明利用了 Cook 和 Mertz 的空间高效树评估算法，该算法建立在催化计算之上。 基本思想是将图灵机的磁带分成几个部分，并将机器的接受建模为一个电路。 Cook 和 Mertz 使用有限域来编码这些段并有效地计算值。

该定理适用于多磁带图灵机和盲随机存取机。 虽然它演示了如何使用接近 *√s* 的空间计算大小为 *s* 的电路的输出，但它对完全通用的随机存取机、非确定性计算和其他计算模型提出了疑问。

该帖子还指出，这一结果削弱了先前在硬度与随机性结果中的假设。 作者提出了未来的研究方向，例如推动更好的空间模拟，并将 Cook-Mertz 技术直接应用于图灵机模拟。 一些评论者讨论了该结果的影响及其潜在的实际应用。

---

## 40. SBOM仍然存在，证明已失效——第14144号行政命令修正案

**原文标题**: SBOMs Remain, Attestations Out – Amendments to Executive Order 14144

**原文链接**: [https://rearmhq.com/blog/sbom-remains-attestations-out-amending-executive-order-14144](https://rearmhq.com/blog/sbom-remains-attestations-out-amending-executive-order-14144)

文章《SBOMs 依旧，证明退出 – 第14144号行政命令修正案》讨论了第14144号行政命令的变更。核心重点似乎是关于软件物料清单 (SBOM) 和证明的澄清或修改。

具体来说，标题表明 SBOM 仍然是该行政命令的关键组成部分，暗示了它们在软件安全和供应链管理中的持续重要性。然而，“证明退出”一词表明，围绕证明的要求或期望（可能与 SBOM 的准确性或验证有关）已被删除或发生重大改变。

在没有全文内容的情况下，很难提供更详细的摘要。然而，关键的结论是，该行政命令正在被修改，以保留对 SBOM 的重视，同时似乎放宽或取消了与证明相关的要求。这可能意味着软件安全合规方法发生了转变，可能旨在通过专注于 SBOM 的生成和共享，而无需对其有效性进行正式证明，从而实现更精简或更实际的实施。“ReARM by Reliza - SBOMs, xBOMs Organizer”的提及表明存在一个工具或平台，可以帮助管理 SBOM 和其他相关的 BOM 格式 (xBOM)。

---

## 41. 桑迪亚启动类脑无存储超级计算机

**原文标题**: Sandia turns on brain-like storage-free supercomputer

**原文链接**: [https://blocksandfiles.com/2025/06/06/sandia-turns-on-brain-like-storage-free-supercomputer/](https://blocksandfiles.com/2025/06/06/sandia-turns-on-brain-like-storage-free-supercomputer/)

桑迪亚国家实验室推出SpiNNaker 2超级计算机，这是一款来自SpiNNcloud的“大脑启发式”系统，独特之处在于无需GPU或内部存储。这款神经形态计算机模拟1.5亿至1.8亿个神经元，旨在增进我们对大脑的理解并突破计算边界。

SpiNNaker 2通过高度并行架构实现其速度和效率。每块服务器板卡包含48个SpiNNaker 2芯片，每个芯片包含152个内核和专用加速器，依赖于大量的SRAM和DRAM。该架构强调高速芯片间通信，从而无需集中式存储。桑迪亚的系统由24块板卡组成，拥有175,000个内核，集成到现有HPC系统中，并且无需操作系统或磁盘即可运行。

SpiNNcloud首席执行官Hector A. Gonzalez强调了SpiNNaker 2的效率提升以及其对包括下一代国防在内的严苛国家安全应用的适用性。目前的最高配置系统拥有超过1050万个内核，并且能够以生物实时的方式执行复杂的事件驱动模拟，与GPU系统相比具有更高的能效。该项目由美国国家核安全管理局 (NNSA) 的高级模拟和计算 (ASC) 计划资助，旨在探索用于核威慑任务的神经形态计算。

---

## 42. 网络开发受虐指南

**原文标题**: A masochist's guide to web development

**原文链接**: [https://sebastiano.tronto.net/blog/2025-06-06-webdev/](https://sebastiano.tronto.net/blog/2025-06-06-webdev/)

本文是一篇面向Web开发的“受虐指南”，专门针对希望使用WebAssembly (WASM) 将其代码移植到Web的C/C++开发者。它强调了这种方法的复杂性和潜在的挫败感，并将其与更简单的Web开发方法进行了对比。

该指南从一个基本的“Hello World”示例开始，演示了如何使用Emscripten将C代码编译为WASM。然后，它深入研究了构建C库并使其函数可从JavaScript访问，突出了函数名称修饰、需要显式导出函数以及JavaScript中的异步初始化等问题。 文章强调，WASM允许在浏览器环境中实现接近原生的性能。

它简要概述了WebAssembly、其起源和基于文本的表示形式。该指南解释了向WASM64的过渡，从而能够使用64位指针和更大的内存寻址（高达8EB）。

文章涵盖了文档对象模型（DOM），展示了JavaScript如何与HTML元素交互。它提供了操纵段落中的文本以及向按钮添加事件监听器的示例。使用HTML和JavaScript创建了一个模板网页，其中包含使用C库进行乘法的占位符。

---

## 43. 仇恨电台 (2011)

**原文标题**: Hate Radio (2011)

**原文链接**: [https://rwandanstories.org/genocide/hate_radio.html](https://rwandanstories.org/genocide/hate_radio.html)

仇恨电台 (2011)：探讨广播电台，尤其是“仇恨电台”在促成冲突和潜在阻碍和平努力中的作用。文章可能深入研究广播节目被用于煽动暴力、传播宣传和贬低特定群体的案例。它可能探讨这种广播如何加剧现有紧张局势、激化敌意，以及阻碍冲突后的和解。

文章可能分析仇恨电台发挥重要作用的特定案例研究，或许侧重于卢旺达或前南斯拉夫等例子。它可能调查仇恨电台使用的手段，包括使用煽动性语言、带有偏见的报道以及传播虚假信息。

此外，该文章可能探讨将广播用作和平工具的潜力。它可能考察通过广播电台促进积极信息、群体间对话和冲突解决的倡议。文章可能会讨论打击仇恨电台的挑战，例如审查制度问题、技术限制以及对有效的媒体素养计划的需求。

本质上，《仇恨电台 (2011)》可能呈现了一个关于广播电台、冲突与和平之间复杂关系的细致视角，展示了其内容和使用方式所决定的潜在危害和益处。它强调了媒体责任的重要性，以及采取积极策略来打击仇恨言论和促进和平沟通的必要性。

---

## 44. 逆向工程 Cursor 的 LLM 客户端

**原文标题**: Reverse Engineering Cursor's LLM Client

**原文链接**: [https://www.tensorzero.com/blog/reverse-engineering-cursors-llm-client/](https://www.tensorzero.com/blog/reverse-engineering-cursors-llm-client/)

本文详细介绍了作者如何使用他们的开源框架TensorZero对Cursor的LLM客户端进行逆向工程。通过拦截并分析Cursor与LLM供应商（如OpenAI）之间的通信，他们获得了对Cursor使用的提示、模型和流程的可观察性。

该过程包括利用Cursor覆盖OpenAI基础URL的功能，将TensorZero设置为自托管代理。挑战包括Cursor最初依赖其自身服务器进行处理以及CORS问题，这些问题通过Ngrok、Nginx以及对标头的仔细配置得以克服。

成功的设置使作者能够观察发送给LLM的系统提示和用户提示，揭示Cursor使用了相对简洁的系统提示。他们还发现了一个“应用模型”，该模型被描述为用于应用代码编辑的智能程度较低的语言模型，突显了一种可能的AI层级结构。

在TensorZero就位的情况下，作者可以对不同的LLM模型（Claude 4.0 Sonnet、GPT-4.1、o4 Mini和Gemini 2.5 Pro）进行A/B测试，而没有明显的延迟影响。他们强调了理解和优化LLM代理的能力，即使是其他人构建的代理。

作者计划发布后续文章，详细介绍他们对真实世界AI编码助手使用的评估，包括A/B测试结果，并探讨反馈信号如何优化Cursor以适应个人使用模式。“CursorZero”的代码可在GitHub上找到。

---

## 45. 数学符号频率

**原文标题**: Math Symbol Frequencies

**原文链接**: [https://leancrew.com/all-this/2025/06/math-symbol-frequencies/](https://leancrew.com/all-this/2025/06/math-symbol-frequencies/)

Dr. Drang研究了Raúl Rojas的《数学语言》一书中出现的数学符号频率表，并质疑了一些异常的条目。该表声称展示了arXiv数学论文和工程教科书中最常用的符号，因其与字符和单词频率表的相似性而引起了他的兴趣。

他最初的怀疑来自于重复的“a”条目和表格中出现的方框。追溯到Clare M. So的论文和Stephen M. Watt的论文，他发现第二个“a”实际上是希腊字母alpha（α），而方框代表分数中的水平线。他还发现Rojas表格中的分号实际上是Watt表格中的句点和撇号。

Dr. Drang指出，分析的“工程教科书”实际上是以工程师为对象的数学书籍，涵盖微分方程和线性代数等主题，不能代表更广泛的工程出版物。他还质疑频率列表中包含逗号和句号，认为它们通常由于LaTeX格式而出现，并非真正的数学运算符。他承认自己被发现的有趣的矛盾之处所驱动，而跑题了。

---

## 46. Mojo中的高效矩阵转置

**原文标题**: Highly efficient matrix transpose in Mojo

**原文链接**: [https://veitner.bearblog.dev/highly-efficient-matrix-transpose-in-mojo/](https://veitner.bearblog.dev/highly-efficient-matrix-transpose-in-mojo/)

使用 Mojo 实现 Hopper 架构的高效矩阵转置内核

这篇博文详细介绍了使用 Mojo 实现 Hopper 架构的高效矩阵转置内核，性能堪比 CUDA。作者展示了如何在 Mojo 中利用张量内存加速器 (TMA) 来优化转置操作。

文章首先从一个朴素的方法开始，为输入和输出矩阵初始化两个 TMA 描述符。这个初始内核实现了 1056.08 GB/s 的带宽，超过了类似的 CUDA 实现的性能。

然后，作者探索了“swizzling”的优化技术，该技术涉及重新排列数据访问模式以提高内存局部性。通过修改 TMA 描述符并在内核中使用 swizzled 索引，带宽增加到 1437.55 GB/s，再次超过了其 CUDA 版本。

最后，这篇博文强调了“线程粗化”的重要性，即每个线程处理一批列。这显著提高了性能，达到 2775.49 GB/s 的带宽，几乎与等效的 CUDA 内核（2771.35 GB/s）相同。这个最佳内核实现了 H100 GPU 上理论带宽的 84.1056%。

文章强调，通过仔细利用 TMA 和诸如 swizzling 和线程粗化等优化技术，Mojo 可以在 GPU 任务中，尤其是在像矩阵转置这样的内存密集型操作中，实现与 CUDA 类似的性能。这篇博文的完整代码可在作者的 GitHub 上找到。

---

## 47. 展示HN：空气实验室 – 一款便携式开源空气质量测量设备

**原文标题**: Show HN: Air Lab – A portable and open air quality measuring device

**原文链接**: [https://networkedartifacts.com/airlab/simulator](https://networkedartifacts.com/airlab/simulator)

展示HN：空气实验室 – 一款便携式开放式空气质量测量设备

---

## 48. 分享我对梯度噪声的所有理解

**原文标题**: Sharing everything I could understand about gradient noise

**原文链接**: [https://blog.pkh.me/p/42-sharing-everything-i-could-understand-about-gradient-noise.html](https://blog.pkh.me/p/42-sharing-everything-i-could-understand-about-gradient-noise.html)

本文从GPU角度全面解析梯度噪声，从一维形式入手，逐步扩展到二维和三维。文章强调理解底层数学原理对于视觉特效、视频游戏和程序艺术等创意应用的重要性。

文章首先详细阐述了对基于坐标的确定性伪随机系统的需求，重点介绍了使用lowbias32函数进行整数哈希以及通过Vigna Sebastiano的技术将其转换为归一化浮点数的方法。文章还介绍了如何使用嵌套异或哈希将哈希函数扩展到多个维度。

文章介绍了梯度噪声的核心概念，强调了其在斜率稳定性方面优于值噪声的优势。文章细致地解释了梯度值（在一维中解释为斜率）如何影响信号的形状，以及如何使用诸如五次插值之类的平滑衰减函数在一维中实现梯度噪声。

在扩展到二维和三维时，文章描述了梯度向量、点积、双线性（二维）和三线性（三维）插值以及在圆（二维）和球体（三维）上生成随机单位向量的使用。它讨论了性能考量以及三维梯度生成中的潜在简化。

最后，文章讨论了分形布朗运动 (fBm)，通过对多个噪声八度进行求和来创建更精细的图案。文章最后强调了导数在各种应用中的实用性，例如光照、到曲线的距离计算和地形侵蚀模拟。文章强调了使用GLSL代码片段对这些技术进行实际的GPU实现。

---

## 49. 展示 Hacker News：AI 游戏动画精灵生成器

**原文标题**: Show HN: AI game animation sprite generator

**原文链接**: [https://www.godmodeai.cloud/ai-sprite-generator](https://www.godmodeai.cloud/ai-sprite-generator)

此“Show HN”贴介绍了一款AI精灵图生成器，该工具旨在从上传的图像创建专业的游戏动画精灵图。该工具旨在简化并加速游戏开发者的动画制作流程，提供具有透明背景和边界框等功能的、可直接投入生产使用的精灵图。

该AI可以生成多种动作类型，如站立、行走、跑步、攻击、跳跃和施法，满足从复古像素艺术到现代动漫的各种游戏类型和风格的需求。用户上传角色设计或用文字描述他们的设想，选择所需的动作，然后AI生成精灵图。

主要功能包括AI驱动的生成、多种动作类型、可直接投入生产的输出，以及使用少量训练样本（最少5个动画）训练自定义动作的能力，可以选择将模型设为私有或公开分享以获取收入。

该服务采用信用点系统，用户只需为使用的部分付费，无需订阅。提供不同的信用点套餐，满足初学者和高级用户的需求。注册后可获得免费信用点，并提供免费选项。

该工具的目标用户是独立开发者、游戏工作室以及艺术家/设计师，承诺节省成本和时间。对于大型企业，提供定制AI解决方案，以便根据特定的游戏开发需求定制该工具。

---

## 50. 使用强化学习训练大型语言模型来解释人类决策

**原文标题**: Reinforcement Learning to Train Large Language Models to Explain Human Decisions

**原文链接**: [https://arxiv.org/abs/2505.11614](https://arxiv.org/abs/2505.11614)

这篇于2025年5月16日提交的arXiv文章探讨了使用强化学习(RL)训练大型语言模型(LLM)，使其能够对人类决策（特别是风险选择情境下）提供可解释的解释。该论文由朱建桥、谢翰博、Dilip Arumugam、Robert C. Wilson和Thomas L. Griffiths合著，旨在解决标准神经网络模型在认知建模方面的局限性，这些模型通常擅长预测，但缺乏可解释性。

核心思想是利用预训练LLM的能力，使其作为既能准确预测人类行为，又能以自然语言生成可理解解释的认知模型。研究人员采用强化学习，使用基于结果的奖励，来引导LLM生成推理轨迹，解释为什么人类可能做出特定的风险选择。

该研究表明，这种RL引导的方法可以在对人类决策进行强有力量化预测的同时，生成高质量的解释。该论文属于人工智能（cs.AI）和计算与语言（cs.CL）领域。

---

## 51. 程序员对航空的错误认知

**原文标题**: Falsehoods programmers believe about aviation

**原文链接**: [https://flightaware.engineering/falsehoods-programmers-believe-about-aviation/](https://flightaware.engineering/falsehoods-programmers-believe-about-aviation/)

程序员对航空的误解：FlightAware的教训

本文“程序员对航空的误解”揭示了程序员在设计航空数据系统时常犯的许多不准确的假设。航班追踪公司FlightAware深刻体会到，航空世界远非干净和标准化。

文章围绕不同的航空数据类别展开，概述了每个类别中常见的误解：

*   **航班：** 关于航班起飞、时刻表、时长、识别（航班号和注册号）以及这些元素一致性的假设通常是错误的。航班可能会从意想不到的地点起飞、经历重大延误、拥有多个航班号，甚至使用无关的航空公司代码。
*   **机场：** 关于机场位置、命名惯例、唯一标识符（ICAO、IATA代码）和地理代码的假设经常存在缺陷。机场可能会搬迁、拥有不一致的命名方案、缺少单一的规范代码，并且可能存在于预期的地理区域之外。
*   **航空公司：** 关于航空公司代码（IATA/ICAO）、航班号分配以及运营航班的航空公司与实际飞机的相关性的假设通常是错误的。
*   **导航：** 关于来自空中导航服务提供商的飞行信息（包括航路点名称和高度数据）的准确性和可靠性的假设有时是不正确的。
*   **应答机和ADS-B：** 关于ADS-B消息的准确性、来源和内容的假设经常是错误的。这包括不准确的GPS数据、不正确的飞行识别、应答机编程错误，甚至可能存在虚假的ADS-B传输。

文章强调，现实世界的航空数据是混乱且不可预测的。FlightAware的航班追踪引擎Hyperfeed旨在处理这些异常情况并提供干净、一致的数据源。这篇文章警示程序员，要避免过度简化并考虑到航空数据的复杂性。

---

## 52. 在 Google Play 商店维护一个安卓应用需要大量工作。

**原文标题**: Maintaining an Android app in Google Play Store is a lot of work

**原文链接**: [https://ashishb.net/programming/maintaining-android-app/](https://ashishb.net/programming/maintaining-android-app/)

本文探讨了作为业余项目维护 Android 应用所面临的挑战，特别是与维护服务器端应用程序相比。作者，一位 Android 开发者，强调了导致 Google Play 商店应用数量减少的几个痛点。

一个关键问题是 Google 对其库（例如 Media3、Google Auth）不断发展和破坏性的更改，迫使开发者进行调整和重写代码。作者还指出了在 Kotlin 为中心的新功能（如 Jetpack Compose）中使用 Java 的困难。

此外，本文还介绍了 Google 不断变化的 UI 设计指南和 Android 平台本身的破坏性更改，需要付出巨大的努力才能跟上。对 Android 开发至关重要的第三方库经常被弃用或放弃，使开发人员陷入困境。

作者还批评了 Android 的两种不同版本控制方案（API 级别与营销版本），这造成了混乱。最后，本文强调了由于各种工具和库之间的依赖关系而导致的强制升级。选择不升级会导致应用被下架。总而言之，本文警告业余开发者要考虑与 Android 应用开发相关的巨大持续维护成本。

---

## 53. Odyc.js – 用于叙事游戏的微型 JavaScript 库

**原文标题**: Odyc.js – A tiny JavaScript library for narrative games

**原文链接**: [https://odyc.dev](https://odyc.dev)

Odyc.js：简化游戏创作的JavaScript库

---

## 54. 关于电磁脉冲武器你需要了解的

**原文标题**: What you need to know about EMP weapons

**原文链接**: [https://www.aardvark.co.nz/daily/2025/0606.shtml](https://www.aardvark.co.nz/daily/2025/0606.shtml)

这篇《土豚日报》的文章讨论了电磁脉冲（EMP）武器的潜在影响，特别是那些在高空引爆的武器。 文章解释说，高空核爆炸会产生大面积的电磁脉冲，由于伽马射线与地球磁场的相互作用，即使在很远的距离也会损坏电子设备。

文章概述了电磁脉冲的三个阶段：E1（快速、高频、烧毁电子设备），E2（持续时间较长、频率较低、更容易防护）和E3（持续时间非常长、频率非常低、损坏电网和基础设施）。

缓解措施的重点是使用法拉第笼——由绝缘材料分隔的导电层——来转移电磁脉冲能量。文章强调，笼子必须是完整的，没有间隙，并且受保护的设备必须与屏蔽层绝缘。 一个简化的，但效果较差的DIY解决方案是将电子设备包裹在多层塑料和铝箔中。

作者认为，现代微处理器比旧技术更容易受到电磁脉冲的影响。 一台旧的电子管收音机或一辆老爷车可能幸存下来，但除非得到充分屏蔽，否则现代电子产品很可能会失效。

---

## 55. 中世纪非洲人用玻璃提纯黄金的独特工艺 (2019)

**原文标题**: Medieval Africans had a unique process for purifying gold with glass (2019)

**原文链接**: [https://www.atlasobscura.com/articles/medieval-african-gold](https://www.atlasobscura.com/articles/medieval-african-gold)

本文详细介绍了11世纪马里Tadmekka的中世纪非洲人使用的一种独特的黄金提纯工艺的发现。考古学家萨姆·尼克松对古代硬币模具的挖掘发现了高度提纯的黄金液滴和玻璃碎片。这促使人们研究西非人用于提纯货币黄金的创新方法。

与欧洲使用铅的坩埚炼金法不同，中世纪的西非人将金矿石与回收的玻璃材料混合。这种方法利用了黄金的惰性，防止其溶解在熔融的玻璃中，而杂质则会溶解。这使得工匠能够分离出纯金，展示了他们对黄金和玻璃特性的理解。

马克·沃尔顿和他在艺术科学研究中心的团队使用现代材料复制了这个过程，用当地的密歇根湖沙子代替了非洲人使用的河流材料。该团队成功地用合成玻璃溶解了沙子中的矿物质，留下了提纯的黄金。这证实了古代马里技术的复杂性和有效性，展示了一种巧妙而有技巧的黄金提纯方法。该过程突出了中世纪西非工匠在利用回收材料和理解黄金化学性质方面的独创性。

---

## 56. 我应该使用轮播图吗？ (2013)

**原文标题**: Should I Use a Carousel? (2013)

**原文链接**: [https://shouldiuseacarousel.com/](https://shouldiuseacarousel.com/)

这篇2013年的文章强烈反对在网站上使用轮播图，特别是主页。作者用直白的“不！！！”表明观点，并用来自各种来源的证据支持它，包括统计数据和专家意见。

核心论点是轮播图无效，而且常常损害用户体验。来自圣母大学 (nd.edu) 的统计数据显示，即使是页面上最突出的元素，第一个轮播项目的点击率也只有极小的 1%。尼尔森·诺曼集团和 WiderFunnel 也呼应了这些发现，引用了多个测试，表明用户通常会错过在旋转轮播图中呈现的内容。

亚当·费洛斯和李·杜德尔等专家进一步批评了轮播图。费洛斯强调，轮播图主要通过展示他们的想法来安抚营销和高级管理层，而不管用户参与度如何。杜德尔更进一步，认为轮播图是用户可能忽略的内容的不错选择。

最后，贾里德·史密斯指出了轮播图的可访问性问题，特别是对于依赖键盘和屏幕阅读器的用户，将它们与过时且烦人的 `<blink>` 标签进行比较。

文章最后以一个简单的警告结尾：使用轮播图可能会让用户感到沮丧。整体语气强烈否定，主张采用其他方式来呈现主页内容。

---

## 57. 用于代码的创新字体家族 (2023)

**原文标题**: An innovative superfamily of fonts for code (2023)

**原文链接**: [https://monaspace.githubnext.com/](https://monaspace.githubnext.com/)

Monaspace：旨在提升代码阅读与编写体验的新型字体家族。它旨在通过提供更强的表现力和可读性来解决传统等宽字体的局限性。

Monaspace的主要特性包括：

*   **纹理修复 (Texture Healing):** 一种新型技术，用于平衡等宽字体的密度，减少因字符宽度变化而引起的视觉不一致。这通过优化空白分布来提高可读性。
*   **可变字体轴 (Variable Font Axes):** Monaspace提供可调节的字重、倾斜和宽度轴，允许用户根据自己的偏好自定义字体的外观。
*   **风格组合 (连字) (Stylistic Sets (Ligatures)):** 它包含大量的代码连字，这些连字被组织成针对不同编程语言定制的风格组合，从而增强代码的清晰度和美观性。用户可以选择性地启用或禁用这些组合。
*   **多种字体样式 (Multiple Font Styles):** Monaspace有不同的样式，包括Neon、Argon、Xenon、Radon和Krypton，为代码提供多样化的视觉美学。

本文详细介绍了纹理修复的工作原理，即通过使用OpenType功能动态调整基于相邻字形的字符间距。它还强调了使用风格组合通过合并常见字符序列来改善代码外观的优势。

Monaspace是由GitHub Next和Lettermatic合作开发的。

---

## 58. FAA将淘汰空管系统中的软盘

**原文标题**: FAA to eliminate floppy disks used in air traffic control systems

**原文链接**: [https://www.tomshardware.com/pc-components/storage/the-faa-seeks-to-eliminate-floppy-disk-usage-in-air-traffic-control-systems](https://www.tomshardware.com/pc-components/storage/the-faa-seeks-to-eliminate-floppy-disk-usage-in-air-traffic-control-systems)

美国联邦航空管理局计划对美国空中交通管制(ATC)系统进行重大改革，以取代软盘、纸条和Windows 95操作系统等过时技术。 当前老旧的系统虽然可能不易受到现代网络攻击，但对国家基础设施构成了日益增长的风险。 代理联邦航空管理局局长克里斯·罗彻莱乌和交通部长肖恩·达菲强调了现代化的紧迫性和两党支持。

此次升级旨在创建一个更安全、更高效的空中交通管制系统，但也面临挑战。 由于其关键作用，系统无法轻易关闭进行升级。 新的基础设施必须具有高度的抗黑客能力。 虽然美国联邦航空管理局正在大力投资维护现有系统，但其老化程度已变得不可持续。 美国联邦航空管理局已发布信息征询书，以收集潜在承包商的数据，并举办“行业日”活动，供公司推销其解决方案。

交通部计划在四年内完成该项目，尽管行业专家认为这个时间表过于雄心勃勃。 最终目标是在被忽视几十年后实现空中交通管制系统的现代化。

---

## 59. YouTuber 声称收到收购 Commodore 品牌的报价

**原文标题**: YouTuber claims to have received an offer to buy the Commodore brand

**原文链接**: [https://www.amiga-news.de/en/news/AN-2025-06-00029-EN.html](https://www.amiga-news.de/en/news/AN-2025-06-00029-EN.html)

据amiga-news.de网站报道，YouTube频道“Retro Recipes”声称收到收购整个Commodore品牌的要约。起因是“Retro Recipes”的一段展示Commodore 64x（一款授权给My Retro Computer Ltd.的复古电脑）的视频大获成功。

受此启发，“Retro Recipes”向Commodore Corporation B.V. 提出一项计划，旨在获得所有Commodore品牌产品（包括现有和未来产品）的广泛“通用许可证”。这项计划将涉及成立一家新公司，由“Retro Recipes”担任总经理，My Retro Computer Ltd.的Sean Donohue担任运营主管，前Commodore USA的Leo Nigro担任技术总监。

“Retro Recipes”的视频结尾爆料称，Commodore Corporation B.V. 不仅提出了许可授权，还提出将整个公司出售给该YouTube频道及其合作伙伴。该要约的细节将在未来的视频系列“我们能拯救Commodore吗？”中披露。

该文章澄清说，Commodore Corporation B.V. 仅拥有Commodore品牌和徽标的权利。其他资产，如AmigaOS和相关商标，归其他实体所有。有传言称，Commodore Corporation B.V. 希望放弃商标权。

---

## 60. 医疗保健软件公司CEO因10亿美元欺诈阴谋被判有罪

**原文标题**: CEO of Health Care Software Company Convicted of $1B Fraud Conspiracy

**原文链接**: [https://www.justice.gov/opa/pr/ceo-health-care-software-company-convicted-1b-fraud-conspiracy](https://www.justice.gov/opa/pr/ceo-health-care-software-company-convicted-1b-fraud-conspiracy)

Power Mobility Doctor Rx (DMERx) 首席执行官加里·考克斯因策划一起价值 10 亿美元的医疗保健欺诈阴谋而被判有罪。 DMERx 通过欺骗性营销，伪造针对联邦医疗保险受益人的医疗上不必要的矫形支具、止痛药膏和其他物品的医生处方。

考克斯及其同谋将药房、耐用医疗设备 (DME) 供应商和营销人员与远程医疗公司联系起来，这些公司愿意接受回扣，以换取通过 DMERx 平台传输的已签署的医生处方。 这些欺诈性处方歪曲了患者检查情况，医生仅为了获得报酬，就在短暂或根本不存在的互动基础上签字批准。随后，DME 供应商和药房向联邦医疗保险和其他保险公司开具账单，导致在总额超过 10 亿美元的索赔中支付了超过 3.6 亿美元。

该计划涉及通过虚假合同掩盖活动，并从医生处方中删除可能存在问题的措辞。 考克斯被判犯有多项罪名，包括共谋实施医疗保健欺诈和电汇欺诈、医疗保健欺诈、共谋支付和接受医疗保健回扣以及共谋欺骗美国。他面临最严厉的指控，最高可判处 20 年监禁。

包括 HHS-OIG、FBI、VA-OIG 和 DCIS 在内的多个机构对该案件进行了调查，突显了打击医疗保健欺诈和保护弱势群体免受剥削的协作努力。 官员谴责该计划破坏了医疗保健项目的完整性，浪费了纳税人的钱，并利用医疗保健系统谋取个人利益。

---

## 61. 打开文件过多

**原文标题**: Too Many Open Files

**原文链接**: [https://mattrighetti.com/2025/06/04/too-many-files-open](https://mattrighetti.com/2025/06/04/too-many-files-open)

本文详细介绍了作者在运行Rust测试时遇到的“打开文件过多”错误的故障排除经验。作者解释了文件描述符，它是操作系统内核用于标识打开文件的正整数，包括常规文件、目录、管道、套接字和设备。每个Unix进程都以标准文件描述符（stdin、stdout、stderr）开始。本文演示了如何使用`ls /dev/fd`、`ls /proc/<pid>/fd`和`lsof`等命令在macOS和Linux上检查打开的文件描述符。

作者强调，操作系统对进程可以打开的文件描述符数量施加了限制，并使用`sysctl`和`ulimit`来说明macOS上的这些限制（kern.maxfiles、kern.maxfilesperproc，以及可以使用`ulimit -n`修改的软限制）。

核心问题被确定为`cargo test`尝试打开的文件多于shell的软限制，从而触发了错误。创建了一个监控脚本来跟踪`cargo test`进程的打开文件描述符数量，证实了该错误发生在打开文件数量接近软限制时。解决方案包括使用`ulimit -n 8192`增加shell的软限制，从而解决了“打开文件过多”错误，并允许测试成功运行。文章最后展示了一个图表，表明现在打开的文件描述符数量的峰值远高于原始限制。

---

## 62. 逆向工程Claude代码

**原文标题**: Reverse engineering Claude Code

**原文链接**: [https://kirshatrov.com/posts/claude-code-internals](https://kirshatrov.com/posts/claude-code-internals)

Kir Shatrov 逆向工程了 Anthropic 的 CLI 工具 Claude Code，以了解其内部运作和性能。他使用 `mitmproxy` 捕获发送给 Anthropic API 的提示。他发现 Claude Code 首先检查用户的输入是否启动了一个新话题，然后将输入包装在一个系统提示中，该提示概述了其作为代理的角色、环境信息（工作目录、git 状态）和可用工具。

文章强调，Claude Code 提供了 11 个工具供 LLM 使用，包括 `dispatch_agent`、`Bash`、`BatchTool`、`GlobTool`、`GrepTool`、`LS`、`View`、`Edit`、`Replace`、`ReadNotebook`、`NotebookEditCell` 和 `WebFetchTool`。一个简单的请求，例如“描述此项目中的内容”，会触发多个工具调用来分析文件结构和内容。

在编写新代码时，Claude Code 在访问外部 URL 时面临安全限制，这导致其调整了策略。一项关键的安全措施是 LLM 在执行 Bash 命令之前对其进行潜在的命令注入分析，这会显著降低速度。Claude Code 还有一个 `/init` 命令来创建一个 `CLAUDE.md` 文件来指导代理。

Shatrov 总结说，Claude Code 优先考虑安全性和稳健性，导致成本更高，性能比 Cursor 等工具更慢。他还指出，Claude Code 更通用，并利用 `claude-3-7-sonnet` 进行推理，利用 `claude-3-5-haiku` 进行更简单的任务，例如解析 bash 命令。尽管存在性能方面的权衡，但 Claude Code 在控制台环境中的代理工具 UX 方面表现出色。

---

## 63. Smalltalk、Haskell和Lisp

**原文标题**: Smalltalk, Haskell and Lisp

**原文链接**: [https://storytotell.org/smalltalk-haskell-and-lisp](https://storytotell.org/smalltalk-haskell-and-lisp)

本文反思了作者使用 Haskell、Smalltalk 和 Lisp 实现编程竞赛题的经验。作者被要求用 Java 编写解决方案，但他选择了这三种语言来探索它们的优缺点。核心发现是作者出乎意料地对 Haskell 产生了强烈的亲和力，甚至独立于其务实优势。他们发现与 Smalltalk 和 Lisp 版本相比，Haskell 代码更优雅且更易于组合。

作者特别批评了 Lisp，感觉自己在“欺骗”它来实现期望的结果，而不是直接表达意图。他们还强调了 Haskell 对将问题分解为小的、易于管理的部分的鼓励，这得益于诸如 `where` 语法之类的特性。

作者承认依赖编译器/解释器来捕获错误，并指出 Haskell 强大的类型系统比 Lisp 或 Smalltalk 更早地识别开发过程中的问题。他们认为，尽管学习 Haskell 可能存在困难，但其在代码正确性和可维护性方面的优势非常显著。

文章最后以关于理想编程环境的未解决问题作为结尾，突出了 Haskell 缺乏强大的依赖管理，以及 Lisp 和 Smalltalk 中对人工干预的依赖。作者表示有兴趣探索像 Autotest 这样的工具，以进一步改善开发工作流程，尤其是在 I/O 测试方面。潜在的主题是一段发现首选编程风格和语言的个人旅程，其驱动力既有主观乐趣，也有客观利益。

---

## 64. 对数线性注意力

**原文标题**: Log-Linear Attention

**原文链接**: [https://arxiv.org/abs/2506.04761](https://arxiv.org/abs/2506.04761)

本文介绍了一种名为“对数线性注意力”的新型注意力机制，旨在弥合 Transformer 模型中线性注意力的效率与 softmax 注意力的表达能力之间的差距。 传统的注意力机制具有二次计算复杂度和线性内存复杂度，对长序列构成瓶颈。 线性注意力和状态空间模型提供线性时间和恒定内存的解决方案，但它们对固定大小隐藏状态的使用限制了它们捕获长距离依赖关系的能力。

对数线性注意力通过用对数增长的隐藏状态集替换固定大小的隐藏状态来解决这一限制。 这种方法保留了线性注意力的计算效率，同时提高了表达能力。 作者证明，通过特定的增长函数，对数线性注意力允许一种富含矩阵乘法的并行计算形式，从而使计算成本与序列长度成对数线性关系。

作者将对数线性注意力作为一个通用框架提出，适用于现有的线性注意力变体。 他们通过实现 Mamba-2 和 Gated DeltaNet 等最新架构的对数线性版本来展示其有效性。 结果表明，这些基于对数线性注意力的变体与其线性时间对应物相比具有竞争力，表明所提出的机制在效率和表达能力之间提供了一个有价值的权衡。

---

## 65. 人工智能应用时代“工作”的意义

**原文标题**: What “working” means in the era of AI apps

**原文链接**: [https://a16z.com/revenue-benchmarks-ai-apps/](https://a16z.com/revenue-benchmarks-ai-apps/)

在人工智能应用时代，“工作”的意义：Andreessen Horowitz 分析报告

该 Andreessen Horowitz 文章《在人工智能应用时代，“工作”的意义》分析了生成式人工智能时代初创公司的增长，指出与前人工智能时代相比，收入产生更快，融资轮次也更快。作者 Olivia Moore 和 Marc Andrusko 重点介绍了 Lovable、Cursor 和 Gamma 等公司迅速实现重大收入里程碑的例子。

他们的数据表明，企业人工智能公司在第一年内就能实现超过 200 万美元的年度经常性收入 (ARR)，并在开始盈利后的九个月内完成 A 轮融资。消费者人工智能公司的表现甚至更好，实现了 420 万美元的年度经常性收入，并在八个月内完成 A 轮融资。“最佳”基准正在超越传统的 100 万美元年度经常性收入目标。

文章强调了“好”公司和“卓越”公司之间日益扩大的差距，指出表现最好的公司正在加速增长，而不是停滞不前。虽然收入增长至关重要，但参与度和留存率等传统指标对于后期融资仍然重要。

一个关键发现是，消费者公司现在正在产生可观的收入，部分原因是它们对训练自己的 AI 模型进行了大量投资。虽然转化为付费用户的转化率可能较低，但转化后的用户留存率仍然很高。

作者总结说，初创公司的增长速度比以往任何时候都快，消费者和企业都愿意为新的人工智能产品付费，现在是构建应用层软件公司的最佳时机。他们还强调了速度和快速产品迭代作为关键竞争优势的重要性。

---

## 66. 主力大语言模型：为何开源模型在批量任务中胜过闭源模型

**原文标题**: Workhorse LLMs: Why Open Source Models Dominate Closed Source for Batch Tasks

**原文链接**: [https://sutro.sh/blog/workhorse-llms-why-open-source-models-win-for-batch-tasks](https://sutro.sh/blog/workhorse-llms-why-open-source-models-win-for-batch-tasks)

Sutro Components博客文章认为，对于诸如分类、摘要和数据提取等常见的“主力”任务，开源大型语言模型（LLMs）相比闭源模型，在成本节约和性能提升方面具有显著优势。虽然GPT、Claude和Gemini等闭源模型在“智能前沿”领域占据主导地位，但对于不太复杂的商业应用，开源替代方案同样出色，甚至更胜一筹。

文章强调了开源模型的成本效益，尤其是在使用像Sutro这样的批量推理提供商时，节省可高达90%。它展示了各种模型的性能和成本比较，使用人工智能分析指数来衡量性能，并计算“性能成本比”。分析表明，开源模型通常提供闭源替代方案2倍至10倍的性价比。

该文章提供了一个转换图表，帮助企业选择闭源模型的开源替代方案，估算潜在的成本节约，并为愿意在性能上略作妥协以获得更高成本效率的团队推荐“性能恢复”模型。文章总结称，企业可以通过切换到开源模型来处理主力任务，从而在不牺牲性能的情况下显著降低LLM成本，并鼓励读者联系Sutro，获取关于优化LLM使用的免费咨询。

---

## 67. 货运铁路推动新型豪华卧铺列车初创公司

**原文标题**: Freight rail fueled a new luxury overnight train startup

**原文链接**: [https://www.freightwaves.com/news/how-freight-rail-fueled-a-new-luxury-overnight-train-startup](https://www.freightwaves.com/news/how-freight-rail-fueled-a-new-luxury-overnight-train-startup)

新锐铁路公司Dreamstar欲重振洛杉矶至旧金山豪华卧铺列车旅行，重现上世纪40年代“云雀”号列车风采。该公司由Joshua Dominic和Thomas Eastmond创立，致力于提供头等舱体验，包括全卧铺住宿、精致餐饮和酒店式服务。

Dreamstar计划的关键部分是利用货运铁路基础设施，类似于Brightline的模式。他们与联合太平洋公司签订了谅解备忘录，以获取圣何塞至文图拉线路的轨道使用权。该初创公司还在与Caltrain、Metrolink和洛杉矶联合车站洽谈协议。

Dreamstar计划提供限停靠、过夜服务，旨在提供舒适的休息。该公司声称，与飞行相比，二氧化碳排放量减少75%。票价将与机票加酒店的费用具有竞争力。

列车设计灵感来自圣塔菲的El Capitan号，设有四个等级的私人客舱、休息室、餐厅和水疗中心。效果图还包括汽车运输车，类似于Amtrak的汽车列车。Dreamstar正在与BMW Designworks合作进行概念开发，并计划重建现有火车车厢。

预计建设需要18-24个月，目标是在2028年洛杉矶奥运会之前开始运营。虽然机车供应商尚未确定，但维护设施的选址规划正在进行中。加州住宅建筑商Bill Lyon已向Dreamstar投资10万美元，其他投资者包括房地产家族和早期支持者。Dominic强调，Dreamstar的成本模型旨在实现效率、运营控制和长期财务可持续性。

---

## 68. 整理你的Shell历史记录

**原文标题**: Curate your shell history

**原文链接**: [https://esham.io/2025/05/shell-history](https://esham.io/2025/05/shell-history)

本文探讨了关于 shell 历史记录管理的不同哲学。文章将 Simon Tatham 提倡的“短暂策略”（即禁用 shell 历史记录并选择性地将有用的命令保存到其他地方）与作者的“shell 历史记录最大化”方法（即保存大量的命令历史记录）进行了对比。

作者承认 Tatham 关于保存失败或不完整的命令会导致混乱和潜在混淆的观点是有效的。虽然作者不愿放弃大量历史记录带来的好处，但提出了一个清理历史记录文件的解决方案：一个为 zsh 编写的 `smite` 函数。

`smite` 函数利用 `fzf`（一个模糊查找器）为 shell 历史记录提供了一个交互式浏览器。用户可以选择要删除的命令，该函数会从历史记录文件中删除这些命令的所有实例。这样可以有针对性地删除拼写错误和无用的命令，使历史记录文件更有用且不那么混乱。该函数提供了一个选项，可以查看和删除整个历史记录或仅删除当前会话的历史记录。文章提到了 zsh-hist，这是一个允许按数字删除历史记录条目的插件，为处理多行命令提供了一个潜在的解决方案。

总而言之，要留意 shell 历史记录中保存的内容，并考虑使用工具和技术来有效地管理它，即使你喜欢大型历史记录文件。关键在于，积极管理你的 shell 历史记录可以提高其可用性，并防止因调用错误命令而导致的错误。

---

## 69. 武器化Dependabot：利用PR请求进行攻击

**原文标题**: Weaponizing Dependabot: Pwn Request at its finest

**原文链接**: [https://boostsecurity.io/blog/weaponizing-dependabot-pwn-request-at-its-finest](https://boostsecurity.io/blog/weaponizing-dependabot-pwn-request-at-its-finest)

本文揭露了 GitHub 仓库中 Dependabot 自动化特性所产生的漏洞，强调了其如何通过“混淆代理人”攻击被利用。攻击者可以欺骗 Dependabot 这个旨在更新依赖项的受信任机器人，使其将恶意代码合并到项目中。

核心问题在于基于条件 `github.actor == 'dependabot[bot]'` 自动合并拉取请求的工作流程。攻击者可以 fork 一个包含此类工作流程的仓库，在其 fork 中引入恶意代码，然后使用 Dependabot 创建一个拉取请求返回到原始仓库。通过触发 Dependabot 重新创建或同步其分支，攻击者可以操纵 `github.actor` 为 Dependabot，从而绕过用户检查并启用自动合并工作流程，注入他们的恶意代码。

本文还揭示了两种通过精心设计的恶意分支名称，利用 Dependabot 命名约定，通过命令注入升级这些攻击的新技术。 这些技术包括利用合并冲突（“合并冲突探戈”）和操纵默认分支（“默认分支合并洗牌”）。

此外，本文还演示了具有写入权限的攻击者如何通过将恶意代码推送到 Dependabot 分支并使用 `@dependabot merge` 命令，来潜在地绕过分支保护规则。这绕过了合并到受保护分支的通常要求。

作者最后强调，Dependabot 并非唯一易受攻击的对象，但其受欢迎程度及其与 GitHub 的集成使其成为此类攻击的主要目标。任何用户自动化的、受信任且可控的机器人都可以以类似的方式被利用。

---

## 70. Meta：关闭你侵入式的AI探索推送

**原文标题**: Meta: Shut down your invasive AI Discover feed

**原文链接**: [https://www.mozillafoundation.org/en/campaigns/meta-shut-down-your-invasive-ai-discover-feed-now/](https://www.mozillafoundation.org/en/campaigns/meta-shut-down-your-invasive-ai-discover-feed-now/)

Mozilla呼吁Meta关闭“发现”AI信息流，认为其在用户未明确同意或知情的情况下，将私密的AI聊天内容转化为公开内容。担忧在于，Meta正在模糊私人和公共互动之间的界限，可能暴露敏感信息。

Mozilla要求Meta立即采取以下行动：

*   **关闭发现信息流：** 暂停该信息流，直到实施强有力的隐私保护措施。
*   **默认私密：** 确保所有AI互动都是私密的，除非用户主动且明确地选择公开分享。
*   **透明化：** 披露有多少用户在不知情的情况下通过该信息流分享了私人信息。
*   **通用退出机制：** 创建一个简单、统一的退出系统，覆盖所有Meta平台，以防止用户数据被用于AI训练。
*   **用户通知与删除：** 通知那些对话可能已被公开的用户，并允许他们永久删除自己的内容。

Mozilla认为Meta未经明确知情同意就将私人对话公开，侵犯了用户隐私，并敦促人们签署请愿书，要求进行这些改变。

---

## 71. C轮融资及规模

**原文标题**: Series C and scale

**原文链接**: [https://www.cursor.com/en/blog/series-c](https://www.cursor.com/en/blog/series-c)

开发AI编码工具Cursor的Anysphere公司宣布成功完成C轮融资，由Thrive、Accel、Andressen Horowitz和DST领投，融资9亿美元，估值99亿美元。这笔新资金将用于推进其AI编码研究。

该公司还披露了Cursor的重大增长里程碑，报告称其年度经常性收入（ARR）超过5亿美元，并已被超过一半的财富500强公司采用，其中包括NVIDIA、Uber和Adobe等知名公司。

此次融资和令人印象深刻的增长表明，Anysphere有充分的准备来实现其利用AI彻底改变人们编码方式的使命。

---

## 72. NASA取消欧罗巴着陆器计划，但科学家提出B计划

**原文标题**: NASA Pulls the Plug on Europa Lander, but Scientists Propose a Plan B

**原文链接**: [https://gizmodo.com/nasa-pulls-the-plug-on-europa-lander-but-scientists-propose-a-plan-b-2000611741](https://gizmodo.com/nasa-pulls-the-plug-on-europa-lander-but-scientists-propose-a-plan-b-2000611741)

由于抵达木卫二严酷环境的挑战以及大幅削减的预算，美国国家航空航天局（NASA）已取消其筹备了十年的木卫二着陆器任务。 该着陆器，一个旨在自主探索木卫二冰冷表面、钻取样本和分析地形的四足机器人，已经通过了所有测试，并准备部署。

该机器人经过专门设计，可以承受木卫二的极端寒冷和高辐射水平，配备了先进的功能，如立体摄像机、机械臂、专用材料，以及独立运行数小时的能力，以解决地球和木卫二之间巨大的通信延迟问题。

尽管任务取消，JPL的工程团队正在倡导将着陆器重新部署到土卫二，土星的卫星，它也拥有地下海洋，但提供了更友好的环境，辐射较低，并且有更好的访问窗口。该团队认为，这个为探索冰冷卫星而建造的机器人应该有机会实现其目的。

该文章还提到了影响美国国家航空航天局（NASA）的更广泛问题，包括特朗普政府提议的预算削减，这将大大减少该机构的资金，影响各种太空探索计划。

---

## 73. 大型语言模型的重击？

**原文标题**: A Knockout Blow for LLMs?

**原文链接**: [https://garymarcus.substack.com/p/a-knockout-blow-for-llms](https://garymarcus.substack.com/p/a-knockout-blow-for-llms)

无法访问文章链接。

---

## 74. 如何在Android上（真正地）发送DTMF信号，且不作为默认通话应用

**原文标题**: How to (actually) send DTMF on Android without being the default call app

**原文链接**: [https://edm115.dev/blog/2025/01/22/how-to-send-dtmf-on-android](https://edm115.dev/blog/2025/01/22/how-to-send-dtmf-on-android)

无法访问文章链接。

---

## 75. 狗狗币使用的审查退伍军人事务部合同的人工智能工具

**原文标题**: The AI Tool Used by Doge to Review Veterans Affairs Contracts

**原文链接**: [https://www.propublica.org/article/inside-ai-tool-doge-veterans-affairs-contracts-sahil-lavingia](https://www.propublica.org/article/inside-ai-tool-doge-veterans-affairs-contracts-sahil-lavingia)

ProPublica调查了特朗普政府用于审查和削减退伍军人事务部(VA)合同的AI工具“DOGE”，揭示了其部署中的严重缺陷。该AI旨在“啃食”非直接支持患者护理的合同，但其基于有缺陷的代码和政府效率部门员工Sahil Lavingia编写的不明确指令。专家发现，该AI依赖过时的模型，虚构合同价值，并且仅分析合同文档的第一部分，导致评估不准确。

旨在指导AI行为的系统提示包含无关信息，并且缺乏对“核心医疗/福利”和“DEI”等术语的关键定义。 对削减被认为与患者护理没有直接关系的合同的强调，导致互联网连接和合规审计等基本服务被标记。

专家批评了使用通用AI模型，而没有进行适当的VA特定培训，以及合同本质上浪费的假设。 虽然VA为使用AI简化流程辩护，但该报告强调了在关键政府职能部门部署AI时可能存在的滥用和意外后果。 ProPublica鼓励掌握政府部门滥用AI信息的人士挺身而出。

---

## 76. 死亡蝾螈的绝境

**原文标题**: The impossible predicament of the death newts

**原文链接**: [https://crookedtimber.org/2025/06/05/occasional-paper-the-impossible-predicament-of-the-death-newts/](https://crookedtimber.org/2025/06/05/occasional-paper-the-impossible-predicament-of-the-death-newts/)

道格·缪尔的《死亡蝾螈的绝境》探讨了太平洋西北地区粗皮蝾螈(Taricha granulosa)和普通袜带蛇(Thamnophis sirtalis)之间的进化军备竞赛。由于含有河豚毒素（一种可以杀死人类的毒药），蝾螈具有极强的毒性。这种极端的毒性进化，是因为该地区的袜带蛇已经进化出对该毒素的抵抗力。

文章强调了这场军备竞赛中涉及的权衡。蝾螈的毒性需要大量的代谢负担。虽然有抵抗力的蛇可以吃有毒的蝾螈，但这种抵抗力不是免费的；存在一种推断的成本，可能体现在神经功能方面。

有趣的是，袜带蛇会将河豚毒素储存在肝脏中，从而使自己对捕食者有毒。 这解释了它们为什么优先捕食蝾螈：为了获得这种防御机制。反过来，蝾螈进化出更强的毒性以避免被吃掉。

尽管蝾螈具有毒性，但它们缺乏警戒色（警告色），因为这会使它们对袜带蛇更具吸引力。因此，蝾螈面临三重困境：高毒性带来代谢成本，它们需要抵抗自身毒素，而且它们无法进化出警戒色。它们也不能降低毒性，因为蛇会更容易地吃掉它们。

文章还涉及区域差异，例如阿拉斯加和温哥华岛毒性较低的蝾螈，以及袜带蛇可能出现警戒色的情况，突出了这种持续进化关系的复杂性。

---

## 77. EFF致FTC：数字千年版权法第1201条制造反竞争监管壁垒

**原文标题**: EFF to the FTC: DMCA Section 1201 Creates Anti-Competitive Regulatory Barriers

**原文链接**: [https://www.eff.org/deeplinks/2025/06/eff-files-comments-ftc-regarding-reducing-anti-competitive-regulatory-barriers](https://www.eff.org/deeplinks/2025/06/eff-files-comments-ftc-regarding-reducing-anti-competitive-regulatory-barriers)

电子前哨基金会(EFF)与作家联盟合作，向联邦贸易委员会(FTC)提交评论，指出《数字千年版权法案》(DMCA)第1201条是一项反竞争法规。他们认为，虽然版权旨在通过合理使用条款服务于公共利益，但第1201条通过禁止规避保护受版权作品的软件锁，实际上禁止了合理使用。

国会试图通过国会图书馆管理的三年一次的豁免程序来解决这个问题。然而，电子前哨基金会认为这个过程过于繁琐和耗时，起到的作用是“扼制点”而非安全阀。这实际上允许第1201条阻碍公共利益和竞争性创新。

虽然联邦贸易委员会不直接控制国会或国会图书馆，但电子前哨基金会希望其调查能够认识到第1201条的负面影响以及三年一次程序的失败。电子前哨基金会敦促联邦贸易委员会建议国会废除或改革第1201条。或者，电子前哨基金会要求联邦贸易委员会倡导在2026年对国会图书馆的三年一次的规则制定程序进行重大修订，以确保版权法促进而非阻碍竞争和独立创新。

---

## 78. 如果有效，那就不是人工智能：人工智能初创企业的商业观察（1999）

**原文标题**: If it works, it's not AI: a commercial look at AI startups (1999)

**原文链接**: [https://dspace.mit.edu/handle/1721.1/80558](https://dspace.mit.edu/handle/1721.1/80558)

Eve M. Phillips 1999年麻省理工学院论文《如果它有效，那就不是人工智能：人工智能创业公司的商业视角》考察了人工智能技术的商业化。该论文由 Patrick Winston 指导，探讨了 20 世纪 90 年代末人工智能创业公司面临的挑战。这个看似矛盾的标题反映了一种普遍的看法，即一旦人工智能技术变得成功并融入到实际应用中，它就不再被认为是“人工智能”，本质上失去了它的神秘感。

该作品可能深入研究了人工智能创业公司的具体案例，分析了它们的商业模式、融资策略以及技术的实际应用。该论文可能调查了人工智能创业公司尽管技术前景广阔，却往往难以实现广泛商业成功的原因。这些原因可能包括以下问题：

*   **“人工智能效应”：** 一项技术一旦变得普遍，就不再被认为是“人工智能”的现象。
*   **营销和认知：** 将“人工智能”作为特定问题的实用解决方案进行营销的困难。
*   **融资挑战：** 由于人工智能企业的高风险和漫长的开发周期，吸引投资的挑战。
*   **技术限制：** 理论上的人工智能能力与现实世界应用中的实际需求之间的差距。

该论文总结了人工智能创业公司改进其在商业市场中成功机会的建议或见解。它可以通过 DSpace@MIT 下载完整版本，但受版权限制。

---

## 79. Swift 和可爱的 2D 游戏框架：使用 CMake 设置项目

**原文标题**: Swift and the Cute 2d game framework: Setting up a project with CMake

**原文链接**: [https://layer22.com/swift-and-cute-framework-setting-up-a-project-with-cmake](https://layer22.com/swift-and-cute-framework-setting-up-a-project-with-cmake)

本文提供了一份逐步指南，介绍如何使用 Cute Framework (一个 C/C++ 框架) 搭建 2D 游戏项目，并使用 Swift 编写游戏逻辑。它利用 CMake 构建项目，使开发者能够使用 Swift 编写游戏代码，同时受益于 C/C++ 在渲染方面的性能。

该过程包括：

1.  **设置项目结构：** 创建目录（src, include）和必要文件（CMakeLists.txt, main.swift, shim.h, module.modulemap）。
2.  **配置 CMakeLists.txt：** 定义项目名称、语言（C、C++、Swift）、使用 FetchContent 获取 Cute Framework 作为依赖项，并链接可执行文件。
3.  **启用 Swift 互操作性：** 创建 C 头文件 (shim.h) 以包含 Cute Framework 的头文件，并创建一个模块映射 (module.modulemap) 以允许 Swift 导入 C 函数。
4.  **编写 Swift 代码：** 在 `src/main.swift` 中实现游戏逻辑，包括初始化 Cute Framework 应用、创建和动画一个精灵，并管理游戏循环。
5.  **配置和构建项目：** 使用 CMake 配置项目，以 Ninja 作为生成器，然后构建可执行文件。
6.  **运行应用程序：** 执行构建的应用程序以查看游戏运行。

本文强调使用 CMake 管理依赖项和构建项目，从而在 Cute Framework 环境中实现 Swift 和 C/C++ 代码的无缝集成。 它还提供了 Cute Framework 文档和 Discord 服务器的链接，以获取更多帮助。

---

## 80. Cloudflare 使用 Claude 构建 OAuth 并公开所有提示词

**原文标题**: Cloudlflare builds OAuth with Claude and publishes all the prompts

**原文链接**: [https://github.com/cloudflare/workers-oauth-provider/](https://github.com/cloudflare/workers-oauth-provider/)

用于 Cloudflare Workers 的 OAuth 2.1 提供程序框架：一个 TypeScript 库，旨在简化 API 端点的 OAuth 2.1 授权实现。该库自动处理令牌管理，使开发人员能够专注于 API 逻辑。它与用户管理和 UI 框架无关，提供了实现的灵活性。

主要特性包括：

*   **简化 API 授权：** 封装 Worker 代码以添加授权，并将经过身份验证的用户详细信息直接传递给 API 处理程序。
*   **自动令牌管理：** 处理所有与令牌相关的操作。
*   **灵活配置：** 支持单个或多个 API 路由处理程序、自定义授权 UI URL 和可选的动态客户端注册。
*   **安全性：** 采用存储系统，仅将密钥存储为哈希值并加密授权属性，从而保护敏感信息。
*   **令牌交换回调：** 允许开发人员连接到令牌交换过程，从而实现上游令牌交换和属性更新等操作。
*   **自定义错误处理：** 能够自定义或覆盖错误响应。

本文提供了代码示例，演示了如何使用该库，包括设置 API 路由、处理授权请求以及在 API 处理程序中访问用户信息。它还强调了配置 Workers KV 命名空间以存储令牌信息的重要性。该框架提供了用于管理客户端注册、列出用户授权以及撤销授权的实用程序，确保对 OAuth 流程的全面控制。

---

## 81. PHP 三十周年

**原文标题**: PHP Is 30

**原文链接**: [https://kieranpotts.com/php-is-30](https://kieranpotts.com/php-is-30)

本文庆祝PHP诞生30周年，追溯其从一套简单的工具发展成为一种无处不在的网络技术。最初Rasmus Lerdorf创建的“个人主页工具”PHP，并非旨在成为一种编程语言，而是一个与Apache网络服务器集成的模板系统。Lerdorf试图通过创建一个允许在HTML中嵌入C函数的Apache扩展，来简化从C代码生成动态HTML的过程。

然而，出乎意料的是，开发者们将PHP本身作为一种脚本语言来使用，直接在HTML中编写业务逻辑，这解决了当时C语言开发人员短缺的问题。这种易用性、与Apache的集成以及其效率，使PHP变得非常流行。它允许轻松升级现有网站，从而实现动态内容和交互。

本文强调，PHP早期的成功在于其可访问性，使广泛的受众能够进行Web开发，并激励许多人从事IT行业。文章承认PHP多年来面临的批评，但强调它从未被设计成一种通用语言。文章最后肯定了PHP对网络的巨大影响，以及它通过Laravel等现代框架所保持的持续相关性。

---

## 82. 速率限制互动指南

**原文标题**: An Interactive Guide to Rate Limiting

**原文链接**: [https://blog.sagyamthapa.com.np/interactive-guide-to-rate-limiting](https://blog.sagyamthapa.com.np/interactive-guide-to-rate-limiting)

无法访问文章链接。

---

## 83. 我做了一个比 Elasticsearch 还差的搜索引擎 (2024)

**原文标题**: I made a search engine worse than Elasticsearch (2024)

**原文链接**: [https://softwaredoug.com/blog/2024/08/06/i-made-search-worse-elasticsearch](https://softwaredoug.com/blog/2024/08/06/i-made-search-worse-elasticsearch)

Doug Turnbull 回顾了其为 Pandas 构建搜索库 SearchArray 的经验，并将其在 BEIR MSMarco Passage Retrieval 语料库上的性能与 Elasticsearch 进行了比较。结果显示，SearchArray 在搜索和索引吞吐量方面明显较慢，但获得了相当的 NDCG@10 分数。

文章深入探讨了 Elasticsearch 速度更胜一筹的原因，重点介绍了 Weak-AND (WAND) 算法。这种优化允许 Elasticsearch 通过关注罕见术语并选择性地处理常见术语来有效地组合来自多个搜索词的分数，从而避免不必要的计算。另一方面，SearchArray 简单地计算并求和所有文档的 BM25 分数。

此外，文章还探讨了 SearchArray 的架构。它不使用传统的倒排列表，而是使用针对短语匹配优化的 roar bitmap 的位置索引。虽然这允许计算词频，但也增加了开销。缓存机制被讨论为潜在的优化途径，但这些引入了维护负担。

作者强调，SearchArray 的设计理念是提供一个使用标准 Pydata 工具进行原型设计的工具，牺牲性能以换取灵活性。与具有专用查询 DSL 的搜索引擎允许全面规划和缓存不同，SearchArray 提供了直接控制和潜在的优化错误。

作者最终表达了对 Elasticsearch、Solr 和 Vespa 等大型搜索引擎背后工程技术的深刻敬意，并强调了它们在为现代搜索应用程序提供支持方面的重要性。文章最后提供了与 BEIR 集成的实用建议，并宣传了作者的搜索课程。

---

## 84. 4-7-8 呼吸法

**原文标题**: 4-7-8 Breathing

**原文链接**: [https://www.breathbelly.com/exercises/4-7-8-breathing](https://www.breathbelly.com/exercises/4-7-8-breathing)

基于标题“4-7-8呼吸法”和来源“Breathbelly”，文章很可能讨论一种名为4-7-8呼吸法的呼吸练习。在没有实际文章内容的情况下，我可以推断出以下关键信息：

*   **它专注于一种特定的呼吸技巧：** 核心主题是4-7-8呼吸练习。
*   **呼吸模式由数字定义：** “4-7-8”表示与吸气、屏气和呼气相关的节奏或比例。
*   **Breathbelly免费提供它：** 该文章很可能提供了如何进行4-7-8呼吸练习的说明，并且Breathbelly免费提供此信息。
*   **与放松相关的潜在益处：** 鉴于这是“Breathbelly”提供的一种呼吸练习，它很可能旨在促进放松、减轻压力或改善睡眠。
*   **关于呼吸时间的说明：** 文章可能解释了步骤，例如吸气4秒，屏住7秒，呼气8秒。
*   **关于呼吸频率的信息：** 文章可能会说明多久做一次，无论是每天还是在焦虑时。

---

## 85. 我们如何回应《纽约时报》的数据需求以保护用户隐私

**原文标题**: How we’re responding to The NYT’s data demands in order to protect user privacy

**原文链接**: [https://openai.com/index/response-to-nyt-data-demands/](https://openai.com/index/response-to-nyt-data-demands/)

OpenAI博客文章《我们如何回应纽约时报的数据需求以保护用户隐私》详细介绍了他们对《纽约时报》在版权侵权诉讼中提出的数据需求的应对措施。《纽约时报》声称，OpenAI的模型未经许可在其受版权保护的内容上进行训练，导致输出内容侵犯了他们的知识产权。

OpenAI的主要论点是，披露《纽约时报》要求的具体数据将严重损害用户隐私。他们声称《纽约时报》的要求过于宽泛，将涉及泄露有关用户提示、模型互动，甚至可能泄露用户身份的敏感信息。

为了平衡版权问题和用户隐私，OpenAI正在采取一种策略，即在共享数据之前对其进行编辑和匿名化。他们正在仔细审查所请求的数据集，以删除个人身份信息（PII）并模糊可能泄露用户行为的模式。此过程旨在向《纽约时报》提供必要的信息以了解训练数据，同时保护用户机密性。

此外，OpenAI强调了他们对负责任的人工智能开发的承诺以及对版权法的尊重。他们表示，他们已制定机制来解决版权问题，并正在积极努力寻找对内容创作者公平且能保护用户隐私的解决方案。他们认为，合作的方式，而不是过于宽泛的数据需求，才是最佳途径。该博客文章是对他们在与人工智能训练数据相关的持续法律挑战中对用户隐私承诺的公开解释。

---

## 86. 在 Python 中像 SQLite 一样测试 Postgres

**原文标题**: Test Postgres in Python Like SQLite

**原文链接**: [https://github.com/wey-gu/py-pglite](https://github.com/wey-gu/py-pglite)

Py-PGlite是一个Python库，旨在简化PostgreSQL测试，提供一个即时、零配置的测试环境。它无需Docker、手动设置和复杂配置，以PostgreSQL的全部功能提供“近乎SQLite的便利性”。

主要功能包括：

*   **零配置：** 无需设置，简化测试流程。
*   **框架就绪：** 与SQLAlchemy、Django和FastAPI无缝集成。
*   **完整PostgreSQL功能：** 支持JSON、数组、窗口函数等。
*   **隔离测试：** 每个测试都使用一个全新的数据库运行。
*   **快速设置：** 相比于基于Docker的PostgreSQL设置，启动速度显著提升。
*   **框架无关的核心：** 可与任何框架一起使用。

Py-PGlite提供可以通过 `pip install py-pglite[framework]` 安装的集成。该库会自动配置Django和SQLAlchemy等框架以进行测试，允许开发人员使用熟悉的ORM操作和原始SQL查询，而无需额外设置。

该文档还涵盖了高级功能，如自定义配置、性能测试和框架隔离。它强调了该库的架构，重点在于具有可选集成和智能默认值的框架无关的核心。文章最后以积极的社区反馈以及用于查看示例、贡献或报告问题的链接作为结尾。

---

## 87. SaaS不过是换了更好包装的厂商锁定。

**原文标题**: SaaS is just vendor lock-in with better branding

**原文链接**: [https://rwsdk.com/blog/saas-is-just-vendor-lock-in-with-better-branding](https://rwsdk.com/blog/saas-is-just-vendor-lock-in-with-better-branding)

文章认为，尽管SaaS承诺通过处理各种服务来简化开发，但集成它们会引入隐藏的“税收”，这些税收会抵消收益并造成供应商锁定。这些税收包括：

*   **发现税：** 花费时间研究和评估不同的SaaS选项以找到合适的方案。
*   **注册税：** 甚至在使用服务之前强加的成本和限制，例如定价层级和受限访问。
*   **集成税：** 将服务集成到现有代码库所需的工作量，包括文档、库和故障排除。
*   **本地开发税：** 在本地复制SaaS环境以进行测试和开发的挑战。
*   **生产税：** 管理API密钥、监控和确保生产中可靠性的持续责任。

作者认为，这些税收使SaaS集成成为一种供应商锁定的形式。即使切换到开源或自托管解决方案也需要大量的代码重写。因此，本文提倡选择像Cloudflare或Supabase这样的集成平台，其中数据库、队列和存储等基本服务是统一的。 这种方法避免了重复的税收，消除了上下文切换和API密钥管理，并提供了促进“流畅”的无缝开发体验。通过缩短代码和服务之间的距离，这些平台提供了跨环境更快、更一致的集成。

---

## 88. 限制网站访问用户本地网络的提议

**原文标题**: A proposal to restrict sites from accessing a users’ local network

**原文链接**: [https://github.com/explainers-by-googlers/local-network-access](https://github.com/explainers-by-googlers/local-network-access)

本⽂档提出⼀种解决方案，⽤于限制公共⽹站访问⽤户本地⽹络，以防⽌通过CSRF攻击或其他⽅式潜在地利⽤脆弱的本地设备。 该提案被称为“本地⽹络访问”，引⼊了⼀个基于权限的系统，⽹站需要获得⽤户的明确同意才能连接到私有IP地址（RFC1918）、回环地址和.local域名。

其核⼼思想是，将本地⽹络请求置于新的“本地⽹络访问”权限之后。如果没有此权限，来⾃公共来源的对更私有地址空间（公共->本地/回环，本地->回环）的请求将被阻止。当⽹站⾸次尝试此类访问时，会显示⽤户提示，允许⽤户授予或拒绝权限。

为了维护诸如托管在公共⽹站上的设备设置⻚⾯之类的合法⽤例的功能，该提案建议向`fetch()` API添加⼀个`targetAddressSpace`参数，允许开发⼈员明确声明请求是专为本地或回环地址空间设计的。 这也有助于绕过由于本地⽹络上⼴泛缺乏HTTPS⽀持⽽可能发⽣的混合内容拦截（来⾃HTTPS⽹站的HTTP请求）。`targetAddressSpace`确保开发⼈员可以通过HTTP向本地设备发出请求，同时请求正确的权限。

该⽂档还详细介绍了与WebRTC、权限策略、权限API、HTML⼦资源、WebSockets和服务⼯作者的集成。 总体⽬标是⻓⼤限度地减少破坏，同时通过让⽤户控制哪些⽹站可以访问其本地⽹络来增强⽤户安全性。

---

## 89. 美国残疾人口的惊人增长 (2013)

**原文标题**: The startling rise of disability in America (2013)

**原文链接**: [https://apps.npr.org/unfit-for-work/](https://apps.npr.org/unfit-for-work/)

查娜·乔菲-沃尔特的文章《美国残疾人数惊人增长》探讨了近几十年来，尽管医疗技术进步和反歧视法律的出台，美国领取联邦残疾福利的人数却显著增加。目前，有1400万美国人领取残疾补助金，其花费超过食品券和福利的总和。

这篇文章强调了残疾问题的复杂性，尤其是在像阿拉巴马州黑尔县这样经济困难的地区，那里近四分之一的劳动年龄成年人都在领取残疾补助金。在那里，“残疾”的定义是主观的，贫困起着至关重要的作用，正如廷伯莱克医生在评估残疾时会考虑教育程度所证明的那样。许多患有背痛或精神疾病的人被认为无法工作，即使其他患有类似疾病的人仍然在职。

这篇文章还探讨了制造业岗位的减少是如何导致残疾索赔增加的。华盛顿州阿伯丁市面临有限再培训机会的前磨坊工人，在失业后往往转向残疾补助金作为一种支持。这种转变有效地掩盖了失业率，因为领取残疾补助金的人不被计入失业人口。

最后，这篇文章考察了因学习障碍和精神健康问题而领取补充保障收入 (SSI) 的儿童人数不断增加的现象。家庭对这些福利的经济依赖产生了一种反常的激励，可能会阻碍孩子的进步和未来的独立性。该系统虽然旨在支持弱势群体，却无意中将个人和家庭困在贫困的循环中。

---

## 90. 文德尔施泰因7-X创下新的聚变记录

**原文标题**: Wendelstein 7-X sets new fusion record

**原文链接**: [https://www.heise.de/en/news/Wendelstein-7-X-sets-new-fusion-record-10422955.html](https://www.heise.de/en/news/Wendelstein-7-X-sets-new-fusion-record-10422955.html)

文德尔施泰因7-X创下新的聚变记录

德国格赖夫斯瓦尔德的文德尔施泰因7-X（W7-X）仿星器聚变实验在能量转化方面取得了新的记录，标志着在证明仿星器作为聚变发电厂的可行性方面迈出了重要一步。在实验中，该装置产生了等离子体，并在30秒内保持了超过1.3亿摄氏度（2.34亿华氏度）的温度，实现了1.3吉焦的能量转化，这比以往的结果有了显著提高。

这一关键进展是通过优化的加热和运行程序实现的。该团队专注于最大化注入等离子体的加热功率，并控制等离子体密度和杂质水平。该性能表明，在未来更长时间的实验中，保持高性能等离子体具有明确的路径。

研究人员的目标是在即将到来的实验中将等离子体运行时间延长到更长时间并提高能量转化。他们还希望实现更高的等离子体密度。目前的目标是将运行时间延长到100秒，这将使W7-X能够展示仿星器运行的基本稳定性，这是聚变发电厂所需要的。这是确认仿星器作为清洁和可持续能源生产潜在解决方案可行性的关键一步。 成功的实验突显了仿星器设计在克服磁约束聚变挑战方面的潜力。

---

## 91. 健康的睡眠量是多少？因国家而异。

**原文标题**: What's a healthy amount of sleep? It differs from one country to another

**原文链接**: [https://news.ubc.ca/2025/05/whats-a-healthy-amount-of-sleep/](https://news.ubc.ca/2025/05/whats-a-healthy-amount-of-sleep/)

不列颠哥伦比亚大学研究挑战了普遍认为每个人都需要相同睡眠时长才能保持健康的观点，表明最佳睡眠时长因文化而异。该研究发表在《美国国家科学院院刊》上，分析了来自20个国家近5000人的数据，发现平均睡眠时长较短的国家并不一定有较差的健康结果。

研究揭示了各国平均睡眠时间的显著差异，日本平均为6小时18分钟，法国平均为7小时52分钟。研究发现，睡眠时间更接近本国文化睡眠时长标准的人往往拥有更好的整体健康状况，表明理想睡眠时长与文化期望相符。有趣的是，研究还发现人们的睡眠时间至少比其文化认为的最佳睡眠时间少一个小时。

该研究强调了针对不同人群的文化规范调整公共卫生指南的重要性，以改善健康结果，而不是推广普遍的“八小时”建议。使用的数据包括来自北美、欧洲、亚洲、非洲和南美洲的参与者。

---

## 92. 一个简单的逗号将使苹果在欧洲损失数十亿美元。

**原文标题**: A simple comma is going to cost Apple billions in Europe

**原文链接**: [https://cafetechinenglish.substack.com/p/a-simple-comma-will-cost-apple-billion](https://cafetechinenglish.substack.com/p/a-simple-comma-will-cost-apple-billion)

一个简单的逗号将使苹果在欧洲损失数十亿美元——文章摘要：

该文章讨论了一个看似微不足道的细节——欧盟关于增值税（VAT）规定的官方解释中的一个逗号——如何可能导致苹果在欧洲面临数十亿美元的补缴税款和持续收入损失。

问题的关键可能在于对一项特定条款的解读，该条款涉及苹果如何通过爱尔兰转移其欧洲销售收入，这是跨国公司常见的避税策略。法律文本中逗号的位置或错位，会影响某些交易是否符合增值税豁免或较低税率的资格。

具体来说，该文章可能指出，苹果利用其欧洲销售额流经爱尔兰的结构，以利用较低的企业税率和某些增值税豁免。这种结构受到了欧洲税务机构的审查。

作者认为，欧盟增值税指令中精确的措辞以及逗号的影响，导致不同国家对该指令的解读各不相同。这造成了不确定性，并使苹果多年来能够利用这种模糊性。

现在，随着更严格的解释出现，特别是受到欧盟范围内打击跨国公司避税行为的推动，这个逗号正在被重新审查。修改后的解释可能意味着苹果将无法再享受某些增值税豁免或需要支付更高的增值税税率，从而导致巨额税单和欧洲市场盈利能力的下降。作者强调了这一看似微小的语法元素所蕴含的巨大财务影响，突出了国际税法的复杂性和微妙性。

---

## 93. 半同步会议：别再浪费时间

**原文标题**: Semi-Sync Meetings: Stop Wasting Our Time

**原文链接**: [https://lukebechtel.com/blog/semi-sync-meetings-stop-wasting-our-time](https://lukebechtel.com/blog/semi-sync-meetings-stop-wasting-our-time)

卢克·贝克特尔认为，大多数会议都是低效的、单线程的流程，浪费人才和时间。他批评了对纯同步会议的依赖，强调了串行处理、层级偏见和缺乏问责制等问题。仅仅依靠人工智能笔记无法解决问题，需要结构性的改变。

提出的解决方案是“半同步”会议：一种结合了无声并行工作和集中讨论的模式。这包括一个“半同步阶段”（10-15分钟），参与者在共享文档中进行无声协作，然后是一个“同步阶段”（15-20分钟），用于针对标记的项目进行有针对性的讨论和决策。

主持人设置共享工作空间，监控文档，并指导讨论。参与者贡献信息、评论他人的输入，并标记项目以供讨论。同步阶段的重点是解决冲突和分配所有权。

文章提供了将这种方法应用于各种会议类型的具体格式，例如冲刺计划、回顾、设计评审和状态更新。主要优势包括平等参与、内置文档、更快的收敛速度以及利用并行思维的力量。他提倡会前进行异步工作，例如状态更新和议程构建。

作者解决了对无声协作的常见异议，例如尴尬和缺乏参与，并引用了证明头脑风暴法有效性的研究。他敦促读者尝试半同步方法，强调了其在缩短会议时间、提高会议效率、明确所有权和改善决策方面的潜力。

---

## 94. 思考需要多少能量？

**原文标题**: How much energy does it take to think?

**原文链接**: [https://www.quantamagazine.org/how-much-energy-does-it-take-to-think-20250604/](https://www.quantamagazine.org/how-much-energy-does-it-take-to-think-20250604/)

本文探讨了人脑的能量消耗，挑战了人们普遍认为的深度思考比休息需要更多能量的观念。通过回顾包括PET和fMRI扫描研究在内的研究，发现费力的认知任务仅比大脑的基线活动多消耗约5%的能量。

大脑是一种能量密集型器官，虽然只占体重的2%，却消耗了全身约20%的能量。这种以ATP形式存在的能量为神经元之间的通讯和维持其膜电位提供动力。

研究人员认为，大脑的大部分能量消耗用于维护，包括调节生理系统（体内平衡）和默认模式网络（走神）。Jordan Theriault提出，这种基线活动的大部分致力于预测，从而使大脑能够有效地分配资源。

积极思考时能量消耗相对较小的增加归因于进化限制。Zahid Padamsey认为，人类是在能源稀缺的环境中进化而来的，这导致了大脑内部的节能机制。这些机制包括低于最佳水平的神经元放电率和频繁的突触传递失败，所有这些都旨在最大限度地提高每个单位ATP的信息传输。大脑的局限性和效率是其复杂性和身体能量预算之间权衡的结果。

---

## 95. 研究人员找到使艾滋病毒在白细胞内可见的方法

**原文标题**: Researchers find a way to make the HIV virus visible within white blood cells

**原文链接**: [https://www.theguardian.com/global-development/2025/jun/05/breakthrough-in-search-for-hiv-cure-leaves-researchers-overwhelmed](https://www.theguardian.com/global-development/2025/jun/05/breakthrough-in-search-for-hiv-cure-leaves-researchers-overwhelmed)

墨尔本彼得·多尔蒂研究所的研究人员在艾滋病毒研究方面取得了重大突破，可能为治愈该疾病铺平了道路。他们开发了一种使用 mRNA 技术的新方法，类似于新冠疫苗中所用的技术，迫使艾滋病毒从白细胞中隐藏的地方暴露出来。

治愈艾滋病毒的主要障碍是其隐藏在白细胞内的能力，从而形成免疫系统和现有药物都无法消除的病毒储存库。该团队开发了一种新型脂质纳米颗粒 (LNP X)，将 mRNA 递送到这些细胞中，指示它们暴露病毒。这以前被认为是不可行的。

研究人员对最初的积极结果和随后的重复结果感到“震惊”。虽然还需要进一步研究以确定暴露病毒是否足以让免疫系统将其根除，或者是否需要与其他疗法相结合，但这一进展代表着向前迈出的重要一步。

这项研究是在实验室中使用艾滋病毒患者的细胞进行的。临床应用仍需数年时间，并且需要成功的动物和人体试验。研究人员告诫说，许多生物医学进展永远无法进入临床，但由于新方法的有效性，他们表达了强烈的希望。这一发现也可能对治疗涉及类似白细胞的其他疾病（包括癌症）产生更广泛的影响。独立专家认识到这一进展的潜力，但强调需要进一步研究，以确定一旦病毒暴露后如何最好地将其清除，以及为了成功治愈，必须彻底根除病毒储存库到什么程度。

---

## 96. 是什么导致美国与其他国家在预期寿命上的差异？

**原文标题**: What drives differences in life expectancy between the U.S. and other countries?

**原文链接**: [https://www.healthsystemtracker.org/chart-collection/what-drives-differences-in-life-expectancy-between-the-u-s-and-comparable-countries/](https://www.healthsystemtracker.org/chart-collection/what-drives-differences-in-life-expectancy-between-the-u-s-and-comparable-countries/)

本文探讨了美国的人均预期寿命（2023年为78.4岁）低于其他富裕国家（平均82.5岁）的原因。它强调，美国的过早死亡率（70岁以下）几乎是同等国家的两倍，并将这一差异归因于几个关键因素。

差距的很大一部分是由于心血管疾病和慢性呼吸系统/肾脏疾病造成的死亡，而新冠疫情也是2021年的一个主要因素。药物滥用导致的死亡，尤其是在年轻人（15-49岁）中，也起着重要作用，美国的这一比例是同等国家的四倍。凶杀率也明显更高。

虽然全球预期寿命有所增加，但美国的上升趋势较慢，并且在疫情期间出现更大幅度的下降。死亡率的差异在15-49岁年龄组中尤为明显，这主要是由慢性疾病、新冠疫情和药物滥用所驱动。虽然儿童死亡率的下降幅度与同等国家相似，但仍然存在持续的差距。

文章指出，虽然心血管疾病和癌症是主要死亡原因，但其他慢性疾病，如肝脏、肾脏和呼吸系统疾病，在美国呈上升趋势，尤其是在年轻人中。健康的社会决定因素和获得医疗保健的障碍促成了这些趋势。与阿片类药物过度处方和芬太尼相关的药物滥用死亡人数激增也加剧了预期寿命差距，突显了精神健康状况的影响。

---

## 97. 我是Wirecutter的水质专家。我不过滤我的水。

**原文标题**: I'm Wirecutter's water-quality expert. I don't filter my water

**原文链接**: [https://www.nytimes.com/wirecutter/reviews/know-your-water-quality/](https://www.nytimes.com/wirecutter/reviews/know-your-water-quality/)

Wirecutter 水质专家：为何我不过滤自来水
尽管人们普遍担忧水污染，但 Wirecutter 的一位水质专家解释了她为何不过滤自家自来水。作者强调，对干净水的渴望可以理解，尤其是在人们越来越意识到 PFAS 等污染物的情况下，但她认为许多人可能实际上并不需要过滤器。

文章强调了三个要点：首先，消费者可以通过查阅自来水公司提供的《消费者信心报告》(CCR) 或自行检测自来水，轻松了解其水质。其次，作者强调，像美国地质调查局 (USGS) 关于 PFAS 污染的报告经常被误读；虽然污染普遍存在，但污染物的实际水平通常低于可执行的限值。第三，作者指出了所有过滤器的缺点，包括高成本、有限的功能和维护要求。

文章强调了了解当地供水情况的重要性，因为污染通常集中在点源周围。它还解释了自来水公司如何处理水，以及各州如何制定比联邦更严格的标准。作者建议使用家用自来水测试套件，特别是 Tap Score 套件，以清晰地了解自来水的水质。发现的最常见污染物不是 PFAS，而是消毒副产物，如三氯甲烷，以及从地下或管道中渗出的物质。作者的总体观点是鼓励读者根据事实而不是恐惧，对水过滤做出明智的决定。

---

## 98. Show HN: Ask-human-mcp – 零配置人工干预机制，阻止幻觉

**原文标题**: Show HN: Ask-human-mcp – zero-config human-in-loop hatch to stop hallucinations

**原文链接**: [https://masonyarbrough.com/blog/ask-human](https://masonyarbrough.com/blog/ask-human)

以下是基于URL和可能内容的关于LLM人机协作系统的“Show HN: Ask-human-mcp – 零配置人机环孵化器，阻止幻觉”博文的摘要。

该文章介绍了`ask-human-mcp`，一个最小配置的人机协作(HITL)系统，旨在防止大型语言模型(LLM)的幻觉和错误。其核心概念是在LLM的输出传递给用户之前引入人工验证步骤，尤其是在对准确性要求严格的情况下。

“MCP”可能指的是“最小关键路径”或类似的概念，强调有效纠错所需的最少的人工干预。“零配置”声明表明该系统旨在易于与现有LLM工作流程集成，而无需进行大量设置或配置。

该博文可能详细介绍了该系统的架构，该架构可能涉及一种机制来标记LLM潜在的不准确或虚构的输出。当引发标记（基于预定义的标准或来自LLM本身的置信度分数）时，该输出将路由给人工审核员。人工审核员验证或更正输出，然后将更正（或验证）的输出传递给用户。

关键功能可能包括：

*   **易于集成：** 专为最大限度地减少对现有LLM驱动的应用程序的干扰而设计。
*   **人工验证：** 人工审核步骤，用于捕获和纠正LLM错误。
*   **专注于关键准确性：** 针对幻觉不可接受的应用程序（例如，事实报道、法律研究）。
*   **潜在的成本节约：** 通过防止错误，该系统可以降低与不准确信息相关的下游成本。

该文章可能还展示了该系统的用例，并提供了将`ask-human-mcp`集成到各种项目中的说明。作者很可能将其定位为一种实用的解决方案，通过以有针对性和高效的方式利用人工监督来构建更可靠和值得信赖的LLM驱动的应用程序。

---

## 99. PyOpticL – 光学系统代码化 CAD 工程

**原文标题**: PyOpticL – Code-to-CAD optical system engineering

**原文链接**: [https://github.com/UMassIonTrappers/PyOpticL](https://github.com/UMassIonTrappers/PyOpticL)

PyOpticL 是一个用于代码到 CAD 光学系统工程的 Python 库，可实现动态和自动化的光学布局设计。它使用光束路径模拟和路由来简化元件放置，无需预定义的坐标。该库处理反射、折射、透射和衍射计算。

主要功能包括带有商用光学元件的模块化子系统和底板，从而提高设计抽象性和可重用性。示例底板包括激光器、AOM 设置和潜望镜，它们可以组装成诸如激光冷却和检测、拉曼塞曼量子位和光电离设置之类的子系统。然后，这些子系统可以集成到复杂的 AMO 设备中，例如囚禁离子量子计算机。

该库的功能在一篇预印本 (arXiv:2501.14957) 中得到展示，该预印本演示了使用由 PyOpticL 设计的模块化光学系统进行的量子位运算。

要开始使用，用户需要安装 FreeCAD、Python 和 Git。PyOpticL 在 FreeCAD 中添加为自定义插件库，然后通过插件管理器安装。文档和 Wiki 提供了指南和示例，以帮助用户快速实施和利用该库。

PyOpticL 从 MIT QUANTA LAB 的 C4PO 库中汲取灵感，并承认他们对该领域的贡献。PyOpticL 社区包括来自 MIT、UCONN、Montana St.、UC Berkeley、Stanford 和 Quera 等机构的研究人员。

---

## 100. 自制GPS接收器 (1992)

**原文标题**: Homemade GPS Receiver (1992)

**原文链接**: [https://lea.hamradio.si/~s53mv/navsats/theory.html](https://lea.hamradio.si/~s53mv/navsats/theory.html)

马特亚兹·维德马尔的《自制GPS接收器(1992)》一文深入探讨了自制GPS和GLONASS接收机的理论和潜力，面向对空间技术感兴趣的无线电爱好者。文章首先解释了卫星导航的历史背景，并将其与早期的地面系统（如LORAN、DECCA和OMEGA）进行对比。

文章强调了从需要用户传输到通过同步卫星传输进行被动接收的转变。它解释了双曲线导航的原理，即利用信号到达的时间差，通过绘制双曲线（或3D中的旋转双曲面）来确定位置。文章强调了地面系统在高度测量方面的局限性。

文章强调了卫星导航的优势：在高频下可预测的无线电波传播以及由于卫星放置而实现三维定位的可能性。它讨论了从依赖多普勒频移测量的低地球轨道卫星（如TRANSIT）到采用更高轨道和多颗卫星进行瞬时位置确定的系统（如GPS和GLONASS）的转变。文章还涉及了卫星导航的计算需求，并解释了为什么它的广泛采用与廉价计算机的普及同时发生。

文章最后简要讨论了数学背景，强调了笛卡尔坐标系的使用。它表明后续章节将详细介绍接收机的实际构建，无论是作为独立单元还是插件模块。最终目标是为无线电爱好者提供知识和说明，以便他们构建自己的GPS/GLONASS接收机，用于精确定位、频率校准和高级通信应用。

---

