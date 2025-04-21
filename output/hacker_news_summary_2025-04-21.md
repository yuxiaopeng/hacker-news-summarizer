# Hacker News 热门文章摘要 (2025-04-21)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 被微软分叉

**原文标题**: Getting Forked by Microsoft

**原文链接**: [https://philiplaine.com/posts/getting-forked-by-microsoft/](https://philiplaine.com/posts/getting-forked-by-microsoft/)

本文详细描述了一位独立开源维护者（“我”）的经历，他的 Kubernetes 镜像镜像项目 Spegel 被微软实际性地 Fork 了，从而创建了 Peerd。作者开发 Spegel 是为了解决客户环境中因镜像仓库中断导致的停机问题，它提供了一种无状态且操作轻便的替代传统镜像方案。

微软最初对 Spegel 表示了兴趣，双方进行了讨论，作者还协助微软工程师进行实施。然而，沟通中断，后来，作者发现微软开发了 Peerd，一个类似的项目，甚至在其文档中引用了 Spegel。作者随后发现 Peerd 中直接复制了 Spegel 的代码，包括函数签名和注释，以及引用 Spegel 和作者雇主的测试用例。

虽然 Spegel 采用的是允许 Fork 和修改的宽松 MIT 许可，但作者认为微软在某些地方没有正确地署名原始来源。这种情况在用户中造成了混乱，由于微软的品牌知名度，这使得与微软的 Peerd 一起推广 Spegel 变得具有挑战性。作者感到沮丧，质疑继续开发 Spegel 的价值。尽管如此，Spegel 仍然存在，并获得了重要的社区采用。作者现在正在努力思考独立开源维护者如何在不被利用的情况下与大型公司合作。作者还在考虑将 Spegel 的许可证更改为更严格的许可证，并启用了 GitHub 赞助商来支持该项目的开发。

---

## 2. 为什么LLM驱动的编程更像是机甲战衣而非人造人

**原文标题**: Why LLM-Powered Programming Is More Mech Suit Than Artificial Human

**原文链接**: [https://matthewsinclair.com/blog/0178-why-llm-powered-programming-is-more-mech-suit-than-artificial-human](https://matthewsinclair.com/blog/0178-why-llm-powered-programming-is-more-mech-suit-than-artificial-human)

在他的文章《为什么LLM驱动的编程更像是机甲战衣而非人工智能人》中，Matthew Sinclair 认为像Claude Code这样的LLM并没有取代程序员，而是增强了他们的能力，就像《异形》中里普利的动力装甲一样。他讲述了使用 Claude Code 构建两个应用程序，生成 3 万行代码的经历，并强调了持续警惕和人工监督的必要性。

虽然LLM大幅缩短了编码时间，尤其是在实现阶段（“我该怎么做？”），但至关重要的“为什么”和“是什么”阶段仍然至关重要，甚至变得更加重要。程序员必须愿意无情地放弃与项目架构目标不符的AI生成的代码。

Sinclair 强调经验仍然至关重要。 熟练的开发人员可以识别 AI 生成的胡说八道，并防止它导致问题。他将这种情况比作“人机混合国际象棋”，在其中，人类与 AI 的团队表现优于人类或 AI 单独的表现。人类提供战略方向和判断，而 AI 提供计算能力。

与 LLM 的有效协作需要在委托和控制之间取得平衡。未来青睐那些能够掌握这些工具的开发者，既认识到它们的潜力，也认识到它们的局限性，并利用它们来增强而非取代软件开发中的人类技能。 关键在于，在这种新的范式中，架构思维、模式识别和技术判断变得更有价值。

---

## 3. Show HN: Dia，一个用于生成逼真对话的开放权重TTS模型

**原文标题**: Show HN: Dia, an open-weights TTS model for generating realistic dialogue

**原文链接**: [https://github.com/nari-labs/dia](https://github.com/nari-labs/dia)

南瑞实验室推出Dia：16亿参数开源文本转语音模型，可生成逼真对话，并通过音频调节控制情感和语气。Dia还能生成笑声和咳嗽等非语言提示。模型权重和推理代码已在Hugging Face上提供，以加速研究。演示对比了Dia与ElevenLabs Studio和Sesame CSM-1B。

用户可以通过克隆GitHub仓库并运行`app.py`脚本来打开Gradio UI，从而快速上手Dia。该模型也可以作为Python库使用，PyPI软件包和CLI工具即将推出。

Dia需要GPU（PyTorch 2.0+，CUDA 12.6）才能获得最佳性能，并且需要大约10GB的VRAM。虽然在企业级GPU上可以实现实时音频生成，但较旧的GPU会体验到较慢的推理速度。计划在未来提供量化和CPU支持。

Dia在Apache 2.0许可下授权，但附带严格的使用限制。它仅用于研究和教育目的，不得用于身份滥用、欺骗性内容创作或非法活动。

未来的工作包括Docker支持、推理速度优化以及通过量化提高内存效率。南瑞实验室欢迎贡献，并感谢Google TPU Research Cloud计划、SoundStorm、Parakeet和Descript Audio Codec提供的灵感。

---

## 4. 为Tcl过程添加关键字参数

**原文标题**: Adding keyword parameters to Tcl procs

**原文链接**: [https://world-playground-deceit.net/blog/2025/04/adding-keyword-parameters-to-tcl-procs.html](https://world-playground-deceit.net/blog/2025/04/adding-keyword-parameters-to-tcl-procs.html)

该博文详细介绍了作者为Tcl过程实现的关键字参数，作者认为尽管标准Tcl命令中存在这种特性，但该语言仍然缺乏它。作者实现了一个`proc*`命令，扩展了标准的`proc`命令，允许使用可选的、命名的且顺序无关的参数，类似于Unix命令行选项。

`proc*`命令预处理参数列表，识别标志和选项，并生成代码来解析输入参数并设置相应的变量。该实现还包括根据参数数量来区分位置参数和选项的逻辑。

作者使用自定义的准引用机制`quasiquote`，通过字符串操作和正则表达式构建，来生成proc的最终Tcl代码。`quasiquote`命令允许在字符串中进行选择性替换和拼接，从而实现动态代码生成。作者承认通过正则表达式进行元编程的复杂性和潜在缺点，但最终认为该解决方案是有效的。

---

## 5. 拨云见日

**原文标题**: Out of the Fog

**原文链接**: [https://www.theverge.com/cs/features/651701/vietnam-operation-babylift-adoption-transnational](https://www.theverge.com/cs/features/651701/vietnam-operation-babylift-adoption-transnational)

卡米尔·布罗姆利的《走出迷雾》探讨了“婴儿空运行动”的复杂遗产。该行动是指1975年西贡陷落期间，将越南儿童大规模撤离并被西方国家（主要是美国）收养的事件。文章揭示了许多被收养者所经历的各种问题，与最初将其定义为从战争恐怖中拯救脆弱儿童的人道主义“慈悲行动”的说法相悖。

文章强调，许多儿童实际上并非孤儿，而是在混乱中与家人分离。收养机构有时优先考虑将儿童安置在西方家庭，而不是确保儿童的福祉和与亲生家庭的潜在团聚，Anh Thi Hoang Doan的故事就是一个例证。

叙事从最初的“拯救”故事转变为被收养者在国外长大所面临的挑战。这些挑战包括与身份认同、种族主义、虐待和心理健康问题作斗争。许多被收养者感到孤立和不完整，与他们的传统脱节，并努力寻找归属感。

文章强调了被收养者群体的重要性，例如“跨国被收养者之声”和“国际越南被收养者”，这些群体提供重要的支持、资源和共同身份感。这些团体帮助被收养者理清他们的过去，寻找亲生家庭，并解决政府对跨国被收养者缺乏支持的问题。文章认为，最初将“婴儿空运行动”描述为简单的慈善行为，忽略了对参与其中的儿童生活的长期而深刻的影响。

---

## 6. Spark AI (YC W24) 正在旧金山招聘全栈工程师

**原文标题**: Spark AI (YC W24) is hiring a full-stack engineer in San Francisco

**原文链接**: [https://www.ycombinator.com/companies/spark/jobs/kDeJlPK-software-engineer-full-stack](https://www.ycombinator.com/companies/spark/jobs/kDeJlPK-software-engineer-full-stack)

Spark AI（YC W24初创公司）正在旧金山招聘全栈工程师，以帮助清洁能源领域构建人工智能驱动的工作流程。Spark AI开发了一种人工智能研究工具，通过引导当地法规，协助能源开发商建设太阳能发电场和电池厂。Colliers Engineering & Design等行业领导者正在使用该工具，并获得了AI Grant以及Brex、Plaid和Helioscope创始人的资助。

理想的候选人拥有3年以上经验，精通Typescript、NextJS、NodeJS和Postgres，并喜欢面对面工作。该职位包括设计和构建核心API、AI基础设施和数据管道，端到端地负责功能，并与创始人紧密合作以制定产品路线图。该职位提供了了解能源行业并塑造公司工程文化的机会。薪资范围为15万美元至20万美元。

Spark AI强调速度和影响力胜于完美，并且重视了解技术决策对业务影响的工程师。该公司由Tae和Julia创立，他们曾是特斯拉、Brex和Apple的产品和工程负责人。他们拥有一支由3人组成的小团队，并且正在迅速发展。

---

## 7. Python 的新型 t 字符串

**原文标题**: Python's new t-strings

**原文链接**: [https://davepeck.org/2025/04/11/pythons-new-t-strings/](https://davepeck.org/2025/04/11/pythons-new-t-strings/)

本文介绍了 t-strings，这是 Python 3.14（预计于 2025 年末发布）中的一项新特性，旨在增强字符串处理的安全性和灵活性。T-strings 类似于 JavaScript 的标记模板，在处理用户输入时比 f-strings 更安全，因为它们不会立即求值为字符串。相反，它们创建 `Template` 对象，允许开发者或库在字符串转换之前安全地处理和转义动态内容，从而防止 SQL 注入和跨站脚本等漏洞。

本文解释了如何使用 t-strings，重点介绍了 `.strings` 和 `.values` 属性，分别用于访问字符串片段和插值。 它还详细介绍了如何迭代 `Template` 并访问详细的插值信息，如转换和格式化规范。

一个简单的例子演示了如何使用自定义函数将替换的单词转换为猪拉丁语，该函数迭代 `Template` 的组件。 作者认为 t-strings 的用途不仅限于安全性，还能实现灵活的字符串处理，其中函数可以返回不同的类型或接受有用的替换。

文章最后表达了希望 Python 生态系统能够拥抱 t-strings，尤其是在处理用户输入的库和框架中，并且 Black 和 Ruff 等工具将支持格式化 t-string 内容。

---

## 8. 表格编程：一种表达性计算的新范式

**原文标题**: Tabular Programming: A New Paradigm for Expressive Computing

**原文链接**: [https://sam.elborai.me/articles/tabular-programming/](https://sam.elborai.me/articles/tabular-programming/)

本文介绍表格化编程，这是一种新的编程范式，其设计灵感来自m8 Dirtywave音序器，旨在实现极简、便携的硬件接口。核心思想是将代码组织成具有固定列（名称、输入、表达式1-表达式5和输出）的结构化表格，这些列代表函数及其执行逻辑。有限的表达式单元格鼓励函数分解，从而提高代码的可维护性。

拟议的硬件将配备Teensy 4.1微控制器、小型显示器和8个用于导航和编辑的按钮。“选择而非键入”的方法旨在减少错误并改善数据流可视化。

作者通过等离子和隧道效应等演示场景示例来展示该概念，突出显示了如何在表格结构和表达式限制内创建复杂的视觉效果。他们解释了基于堆栈的虚拟机将如何执行代码，隐式地连接行内的操作，而函数调用则管理它们之间的数据流。

除了演示之外，作者还设想了像素艺术编辑器或音乐工具等应用程序，这些应用程序是围绕硬件的约束而设计的，以获得更直观的体验。受m8的“视图”和上下文相关菜单启发的层级组织模型将解决可扩展性和易用性问题。关键是创建一个集成的硬件/软件系统，使约束增强而不是限制创造性表达。现有一个可用的Web原型来验证核心概念。

---

## 9. 汤汀咖啡馆 (2018)

**原文标题**: The Tontine Coffee-House (2018)

**原文链接**: [https://tontinecoffeehouse.com/2018/10/15/the-tontine-coffee-house/](https://tontinecoffeehouse.com/2018/10/15/the-tontine-coffee-house/)

本文探讨了纽约通廷咖啡馆的历史及其在纽约证券交易所发展中的作用。该咖啡馆成立于1793-94年，由一种名为“通廷”的古老年金式投资计划资助，该计划将退休规划与彩票相结合。投资者购买股份并在去世前获得股息，已故投资者的股份重新分配给幸存者，使寿命较长的人受益。

通廷咖啡馆是经纪人、交易员、承销商和商人的中心聚会场所。它促进了交易和新闻传播，最终演变成纽约证券交易所的前身。文章强调，资助咖啡馆的通廷出售了203股，提供了4万美元的启动资金，相当于今天的100多万美元。

咖啡馆位于华尔街和水街的拐角处。虽然该建筑最终被拆除并重建，但交易转移到了其他地点，最终形成了纽约证券交易所现在的所在地。通廷于1870年结束，剩余的七名受益人，主要来自富裕家庭，从他们的长期投资中获得了可观的收益。文章最后反思了纽约证券业务的简陋开端，并提出了对18世纪退休规划的一种可能的欣赏。

---

## 10. 修改30行Linux代码可减少高达30%的功耗

**原文标题**: Reworking 30 lines of Linux code could cut power use by up to 30 percent

**原文链接**: [https://spectrum.ieee.org/data-center-energy-consumption](https://spectrum.ieee.org/data-center-energy-consumption)

滑铁卢大学计算机科学教授马丁·卡斯滕和他的合作者发现，只需修改Linux代码中的30行，数据中心的功耗便有望降低高达30%。现有代码中的低效率已被发现并得到纠正，从而实现了显著的节能效果。这个简单的修复可能会对数据中心的能源足迹产生重大影响，提供了一种经济高效且易于实施的解决方案，以减少其环境影响。文章强调了通过相对较小的代码调整实现显著节能的潜力。

---

## 11. 用 Haskell 改造我的 Python

**原文标题**: Haskelling My Python

**原文链接**: [https://unnamed.website/posts/haskelling-my-python/](https://unnamed.website/posts/haskelling-my-python/)

本文演示了如何使用 Python 生成器实现 Haskell 风格的惰性无限列表。它首先定义了一个用于生成正整数的递归生成器 (`ints()`) 以及一个 `take()` 函数，用于从生成器中检索有限数量的元素。

核心概念围绕使用积分将泰勒级数定义为无限生成器。作者定义了一个 `integrate()` 函数，该函数可以移动和划分泰勒级数的各项，然后利用函数与其积分之间的关系，递归地定义 `expSeries()` (e^x)、`sine()` 和 `cosine()`。这之所以可行，是因为生成器以惰性的方式生成元素，仅在请求时才生成。

文章随后提供了一个 `evalAt()` 函数，用于在特定点评估泰勒级数，并将结果与 Python 的标准库函数（例如，`math.exp()`、`math.sin()`）进行比较。

最后，本文讨论了 Python 生成器由于缺乏记忆化（与 Haskell 列表相比）和潜在的递归限制而导致的性能问题。它引入了一个 `memoize` 装饰器来缓存生成器的结果，从而显著提高性能。作者还指出，该方法适用于 Python 的 `fractions` 模块，以获得有理数结果。

---

## 12. 逆向工程混淆的TikTok虚拟机

**原文标题**: Reverse engineering the obfuscated TikTok VM

**原文链接**: [https://github.com/LukasOgunfeitimi/TikTok-ReverseEngineering](https://github.com/LukasOgunfeitimi/TikTok-ReverseEngineering)

本文详细介绍了对 TikTok 混淆后的虚拟机 (VM) 的逆向工程，该虚拟机具体存在于 `webmssdk.js` 中，用于安全和混淆。作者概述了解混淆过程，首先解码字符串数组，并将方括号表示法转换为点表示法，以提高可读性。然后，他们通过 Babel 使用 AST 转换，将数组索引函数调用替换为标准函数调用，从而解决了函数调用的混淆问题。

文章讨论了 VM 字节码的解构，该字节码最初经过 XOR 加密和 gZip 压缩。作者描述了解密字节码并反编译 VM 指令的过程，最初依赖于 AI 辅助。

一个关键方面是通过使用 Tampermonkey 和 CSP disabler 等浏览器扩展替换原始的 `webmssdk.js` 来调试解混淆后的代码。这允许实时编辑和测试。

作者随后深入研究了请求签名的逆向工程，重点关注向 TikTok 服务器发出请求所需的 `X-Bogus` 和 `_signature` 标头。`X-Bogus` 的生成通过 `window.frontierSign` 实现，而 `_signature` 需要更深入地研究 VM。他们逆向工程了 VM 函数，如 VM86、VM113 (X-Bogus) 和 VM189 (_signature)，并实现了一个能够生成有效签名的签名器，从而能够执行发布评论等操作。文章承认存在客户端 Bot 保护措施，例如鼠标跟踪，这些措施未经服务器验证，可以忽略以进行签名生成。最后，作者指出 TikTok VM 不断发展，需要持续的反编译工作。

---

## 13. 为Cortex-A53编写Neon内核

**原文标题**: Coding Neon Kernels for the Cortex-A53

**原文链接**: [https://destevez.net/2025/02/coding-neon-kernels-for-the-cortex-a53/](https://destevez.net/2025/02/coding-neon-kernels-for-the-cortex-a53/)

本文深入探讨了针对ARM Cortex-A53处理器优化NEON内核的复杂性，重点在于为简单的线性数学运算`y[n] = ax[n] + b`实现最佳性能。作者强调了因缺乏关于A53指令时序的公开文档而带来的挑战，转而依赖社区来源的信息和微基准测试。

文章讨论了A53的关键方面，包括其按序执行、部分双发射能力以及其加载（64位）和存储（128位）数据路径的不对称性。文章强调，理解这些特性对于手动优化汇编代码至关重要，因为CPU对排序不良的指令非常敏感。作者还警告说，由于`llvm-mca`的CPU模型不准确，不应依赖它进行A53优化。

文章分析了计算`y[n] = ax[n] + b`的两种方法：使用单独的`fmul`和`fadd`指令，以及使用`fmla`指令。两种方法的性能相似。理论分析估计最大吞吐量为每个时钟周期计算一次`y[n]`（2 FLOPs/cycle）。作者然后演示了一种实用的方法，使用64位NEON寄存器来匹配加载数据路径的宽度，从而允许加载/存储和数学运算的双发射，最终努力实现理论性能极限。关键是通过操作64位向量而不是128位向量，将内存操作与计算重叠。

---

## 14. 去中心化方案

**原文标题**: Decentralizing Schemes

**原文链接**: [https://www.tbray.org/ongoing/When/202x/2025/04/16/Decentralized-Schemes](https://www.tbray.org/ongoing/When/202x/2025/04/16/Decentralized-Schemes)

Tim Bray 认为，像 Fediverse 和 Bluesky 这样的去中心化社交媒体平台因其去中心化特性而面临可用性挑战。 具体来说，他指出了“分享难题”，即用户难以与不同实例或不同客户端上的内容互动；“客户端难题”，即点击链接打开错误的应用程序；以及“帖子可移植性难题”，即托管在已失效服务器上的内容无法访问。

Bray 建议利用 URI 方案（如 `https:` 或 `mailto:`）来解决这些问题。 他建议定义诸如 `fedi:` 用于 Fediverse 和 `at:` 用于 ATproto 的方案，允许操作系统和浏览器将链接路由到适当的客户端应用程序。 这将解决分享和客户端难题，确保用户无论使用哪个实例或客户端，都能无缝地与内容互动。

此外，Bray 设想 URI 方案能够实现帖子可移植性。 通过使用 `fedi:` URI，Fediverse 软件可以跟踪帐户迁移并从旧服务器检索帖子，即使这些服务器不再活跃。 虽然承认现有挑战，如浏览器支持不足，但 Bray 强调 URI 方案是为协议支持和多种实现而设计的基础 Web 技术，使其成为改善去中心化社交媒体用户体验的一个有希望的解决方案。 他还指出，Android 已经对处理新的 URI 方案提供了一些支持。

---

## 15. 手写比打字更能激活大脑网络。

**原文标题**: Handwriting activates broader brain networks than typing

**原文链接**: [https://www.psypost.org/handwriting-activates-broader-brain-networks-than-typing-study-shows/](https://www.psypost.org/handwriting-activates-broader-brain-networks-than-typing-study-shows/)

手写比打字更能激活大脑网络：一项关于记忆和学习的新发现

---

## 16. Show HN: Nerdlog – 快速、多主机 TUI 日志查看器，带时间线直方图

**原文标题**: Show HN: Nerdlog – Fast, multi-host TUI log viewer with timeline histogram

**原文链接**: [https://github.com/dimonomid/nerdlog](https://github.com/dimonomid/nerdlog)

Nerdlog 是一个快速的、远程优先的、基于终端 (TUI) 的日志查看器，旨在高效地分析来自多个远程机器的日志，无需中央服务器。它受到 Graylog 和 Kibana 等工具的启发，追求速度和最简设置。 它通过 SSH 连接到远程主机，远程分析日志，并且只下载一小部分日志消息（每个主机每个查询最多 250 条）和时间线直方图数据。数据在传输过程中会进行 gzip 压缩以节省带宽。

主要功能包括按时间范围和模式过滤日志，以及用于可视化日志活动的时间线直方图。它主要设计用于系统日志，但也支持其他格式。

安装需要 Go。 使用涉及指定 logstream（user@host 或 user@host:port:/logfile），可以选择使用 SSH 配置和专用的 logstreams.yaml 文件进行自定义配置。 用户界面提供查询编辑表单、用于过滤的 awk 模式输入、时间线直方图和显示结果的日志表。 支持类似 Vim 的导航和命令行界面，命令如 `:xclip` 用于共享查询，`:back` 和 `:fwd` 用于导航，`:set` 用于配置选项，如 `numlines` 和 `timezone`。

要求包括 SSH 访问权限、运行的 SSH 代理以及远程主机上的 Gawk (GNU awk)。

---

## 17. 计算机革命尚未发生 (1997) [视频]

**原文标题**: The Computer Revolution Hasn't Happened Yet (1997) [video]

**原文链接**: [https://www.youtube.com/watch?v=aYT2se94eU0](https://www.youtube.com/watch?v=aYT2se94eU0)

这篇题为“计算机革命尚未发生（1997）[视频]”的“文章”根据语境判断似乎是一个YouTube视频。然而，提供的内容仅包含标准的YouTube页脚信息和版权声明，*没有提供关于视频论点或内容的任何实际信息*。

因此，无法进行概括。 给定的文本仅表明该视频存在于YouTube上，并包含与该平台相关的标准法律和联系信息。 我们对作者在1997年为什么认为计算机革命尚未发生的具体主张一无所知。 要概括该视频，我们需要访问它的实际内容。

---

## 18. 流水线可能是我的最喜欢的编程语言特性。

**原文标题**: Pipelining might be my favorite programming language feature

**原文链接**: [https://herecomesthemoon.net/2025/04/pipelining/](https://herecomesthemoon.net/2025/04/pipelining/)

本文推崇“管道化”（或方法链）作为一种卓越的编程语言特性，因为它在可读性、可编辑性和代码发现方面表现出色。作者将管道化定义为通过隐式传递前一个操作的结果来省略参数的能力。

作者将管道化的代码与嵌套函数调用进行对比，认为管道化允许更自然的逐行阅读流程，更易于注释，并避免了对中间变量的需求。文章通过大量代码示例论证了管道化的优势，包括其在成员访问（例如，`x.y`）、SQL中的数据处理以及建造者设计模式中的应用。

文章强调的一个显著优势是通过 IDE 自动完成进行的代码发现，即在对象后按“.”可以提供上下文相关的建议方法。作者认为，这是类型系统与管道化结合的一个主要附加价值。

文章讨论了潜在的反驳观点，例如 SQL 查询中 `SELECT` 语句的位置，但总体上提倡采用管道化。它通过 Haskell 示例说明了管道化的优势，展示了 `&` 运算符如何通过实现更传统的顺序数据流来增强可读性。

---

## 19. 颠覆非洲互联网注册机构的行动

**原文标题**: The campaign to subvert Africa's internet registry

**原文链接**: [https://www.capeindependent.com/article/the-campaign-to-subvert-africas-internet-registry](https://www.capeindependent.com/article/the-campaign-to-subvert-africas-internet-registry)

本文详细描述了一起颠覆非洲互联网注册管理机构AFRINIC的活动，重点关注中国公民陆恒为牟利而将IP地址私有化和商品化的行为。陆恒通过其公司Larus和Cloud Innovation从AFRINIC获得了大量IPv4地址。AFRINIC后来收回了这些地址，因为认定它们未按照注册协议的规定使用，主要惠及非洲以外的利益，包括儿童色情和赌博网站。

陆恒在毛里求斯发起了多起诉讼，试图重新控制这些IP地址并削弱AFRINIC。这些诉讼借助单方面命令，冻结了AFRINIC的账户并暂停了董事会选举，严重影响了其运营。一位国家任命的接管人Vasoodayven Virasami接管了AFRINIC。值得注意的是，陆恒的同伙Paul Wollner被接管人聘为“IT顾问”。

本文强调了IPv4地址日益稀缺和有价值，以及陆恒如何试图瓦解现有的区域互联网注册管理机构（RIR）结构，以允许不受限制地交易这些资源，此举将主要使那些从IP地址销售中获利的人受益。本文还提到了AFRINIC过去的腐败行为，其中数百万个IP地址被盗并在黑市上出售，表明目前的情况是如何利用该组织内部的漏洞的。其他RIR也曾遇到过陆先生的行为问题。

---

## 20. Zig编译时不能做的事情

**原文标题**: Things Zig comptime won't do

**原文链接**: [https://matklad.github.io/2025/04/19/things-zig-comptime-wont-do.html](https://matklad.github.io/2025/04/19/things-zig-comptime-wont-do.html)

Zig `comptime` 功能的局限性：它 *不会* 做什么

主要局限性包括：

*   **无宿主泄漏：** `comptime` 代码不访问宿主架构细节，确保跨不同编译目标（交叉编译）的一致行为。这可以防止对用于编译的机器的意外依赖。

*   **无 `#eval`：** Zig 不允许通过在编译期间注入任意字符串来动态生成源代码。相反，它使用部分求值/特化，如果某些参数是 `comptime` 已知的，则可以在编译时部分求值函数或控制流表达式。

*   **无 DSL：** Zig 缺乏用于自定义语法的扩展点。一切都基于 Zig 值运行，尽管自定义语法仍然可以作为 `comptime` 字符串传递（例如在 `printf` 中）。

*   **无 RTTI：** 虽然 `comptime` 允许基于类型的特化（类似于动态语言），但 Zig 不保留运行时类型信息。如果需要运行时类型信息，则必须显式创建并作为运行时值传递。

*   **无新 API：** 虽然 `comptime` 可以生成新类型，但它不能向这些类型添加方法。API 必须手动编写，尽管它们可以在内部使用 `comptime` 反射。库不能自动向用户定义的类型添加方法（例如，`.to_json`）。

*   **无 IO：** `comptime` 代码不能执行任何输入/输出操作。这保证了封闭的、可重现的、安全的和可缓存的编译时求值。如果需要数据库交互，应由构建系统 (`build.zig`) 处理以生成 Zig 代码。

作者总结说，这些限制虽然具有约束性，但会带来更清晰、更易于管理的元编程系统，在强大功能和易于推理之间取得平衡。

---

## 21. 裁判屁股与灌篮：拍摄NBA比赛是什么感觉

**原文标题**: Ref Butts and Slam Dunks: What It's Like Photographing an NBA Game

**原文链接**: [https://petapixel.com/2025/04/09/ref-butts-and-slam-dunks-what-its-like-photographing-an-nba-game/](https://petapixel.com/2025/04/09/ref-butts-and-slam-dunks-what-its-like-photographing-an-nba-game/)

本文深入幕后，探讨成为一名NBA摄影师的挑战与回报，重点关注《商业呼吁报》的摄影记者克里斯·戴（Chris Day）报道孟菲斯灰熊队的经历。

戴强调摄影师与比赛近距离接触，导致诸如“裁判屁股”挡住镜头等障碍。他讨论了了解球场边后勤工作的重要性，包括指定的座位，以及与球员和裁判发生意外互动的可能性。

在设备方面，戴依赖两台配备各种镜头（16-35mm、70-200mm、300mm）的相机来捕捉比赛动态和观众反应。他强调摄影师之间协作和支持的环境，大家乐于提供建议和帮助。

摄影师的主要目标是通过捕捉关键时刻、反应和转折点来讲述比赛的故事，这需要预判和对故事情节的心理清单。戴在一场灰熊队对阵凯尔特人队的比赛中，通过关注临时教练和凯尔特人队球星杰森·塔图姆的本地联系来体现这一点。

文章还提到了出于安全原因，球场边摄影师的数量随着时间的推移而减少，以及对被球员撞伤的摄影师缺乏同情，突出了捕捉完美NBA镜头所涉及的挑战和风险。戴与受伤的灰熊队球员河村勇辉坐在他旁边的经历进一步说明了球场边摄影的不可预测性。

---

## 22. 实验首先是一个过程。

**原文标题**: Experimenting is above all a process

**原文链接**: [https://www.205.tf/articles/experimenting-is-above-all-a-process](https://www.205.tf/articles/experimenting-is-above-all-a-process)

《实验首重流程》一文强调，实验应被视为一个结构化的、有条理的流程，而非一系列孤立的测试。该文章于2025年1月4日发表，归类为案例研究，由Rémi Forte撰写，共1973字，可能深入探讨了进行有效实验的复杂性和最佳实践。

根据标题，该文章可能论述实验的成功很大程度上取决于明确、完善流程的建立和遵循。这个流程可能包括以下阶段：

*   **定义明确的目标和假设：** 确定实验旨在实现的目标，并制定可验证的预测。
*   **设计严谨的方法论：** 确保实验结构能够隔离变量、控制偏差并收集可靠数据。
*   **有效执行实验：** 一致且准确地实施设计好的方法论。
*   **全面分析结果：** 解释收集的数据，识别重要发现，并得出有意义的结论。
*   **根据发现进行迭代：** 利用结果改进流程、调整假设并规划未来的实验。

因此，该文章的核心信息很可能是，以流程为导向的心态进行实验对于获得有效、可靠和可操作的结果至关重要。案例研究的形式表明它将提供真实的案例和见解来支持这一论点。

---

## 23. 教宗方济各去世了

**原文标题**: Pope Francis has died

**原文链接**: [https://www.reuters.com/world/pope-francis-has-died-vatican-says-video-statement-2025-04-21/](https://www.reuters.com/world/pope-francis-has-died-vatican-says-video-statement-2025-04-21/)

无法访问文章链接。

---

## 24. Gemma 3 QAT 模型：将 AI 带入消费级 GPU

**原文标题**: Gemma 3 QAT Models: Bringing AI to Consumer GPUs

**原文链接**: [https://developers.googleblog.com/en/gemma-3-quantized-aware-trained-state-of-the-art-ai-to-consumer-gpus/](https://developers.googleblog.com/en/gemma-3-quantized-aware-trained-state-of-the-art-ai-to-consumer-gpus/)

Google开发者博客宣布发布Gemma 3开放模型的量化感知训练（QAT）优化版本。这些新版本显著降低了内存需求，使其能够在NVIDIA RTX 3090等消费级GPU上运行，从而将最先进的AI带到更易获得的硬件上。

文章强调了可访问性的重要性，指出虽然高端硬件非常适合云部署，但许多用户希望在现有硬件上利用Gemma 3的强大功能。QAT通过降低模型参数的精度（量化）来实现这一点，从而缩小模型大小并降低VRAM需求。例如，Gemma 3 27B模型的VRAM需求从54GB (BF16) 降至14.1GB (int4)。

该博文解释了QAT的工作原理，强调它在训练过程中集成了量化过程，以最大限度地减少性能下降。博文随后详细介绍了如何利用QAT在各种设备上运行Gemma 3模型，包括台式机、笔记本电脑，甚至手机。文章还强调了与Ollama、LM Studio、MLX、Gemma.cpp和llama.cpp等流行工具的集成。

文章还提到了社区提供的训练后量化（PTQ）替代方案。该博文最后鼓励开发者探索量化模型并开始构建，并提供了Hugging Face、Kaggle和Google AI Edge等资源的链接。

---

## 25. 停用脸书和照片墙对用户情绪状态的影响

**原文标题**: The effect of deactivating Facebook and Instagram on users' emotional state

**原文链接**: [https://www.nber.org/papers/w33697](https://www.nber.org/papers/w33697)

停用 Facebook 和 Instagram 对用户情绪状态的影响：一项 NBER 工作论文调查了社交媒体停用对用户心理健康的影響。研究人员在 2020 年美国大选前进行了两项大型随机实验，检验了停用 Facebook 和 Instagram 六周的效果。

研究发现，与仅停用一周的对照组相比，停用 Facebook 六周使衡量幸福感、抑郁和焦虑的指标提高了 0.060 个标准差，具有统计学意义。 同样，停用 Instagram 相同的时间段也使同一指标提高了 0.041 个标准差。

进一步的探索性分析揭示了潜在的人口统计学差异： Facebook 停用的积极影响主要在 35 岁以上的人群中观察到，而 Instagram 停用的积极影响在 25 岁以下的女性中更为明显。

该论文承认了潜在的利益冲突，列出了许多作者曾从 Meta (Facebook) 或相关公司获得资金、旅行或咨询费、持有 Meta 股票或曾是 Meta 员工。 该研究提供了数据附录和随机对照试验注册条目的链接，以供进一步审查。

---

## 26. 展示一下：我做了一个AI，可以将GitHub代码库转化为简易教程

**原文标题**: Show HN: I built an AI that turns GitHub codebases into easy tutorials

**原文链接**: [https://github.com/The-Pocket/Tutorial-Codebase-Knowledge](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge)

这个“Show HN”帖子介绍了一个AI代理，它可以分析GitHub代码库并生成初学者友好的教程，通过Pocket Flow框架进行讲解。Pocket Flow是一个100行的LLM框架，它会抓取代码库，构建知识库，识别核心抽象，并将复杂的代码转化为易于理解的可视化教程。

该帖子展示了AutoGen、Browser Use和FastAPI等流行的GitHub代码库的示例结果，证明了该AI完全可以通过抓取代码来创建教程的能力。

该帖子包含了入门指南：克隆代码库、安装依赖项、使用API凭证设置LLM以及运行主脚本。用户可以分析GitHub代码库或本地目录，指定包含和排除的文件，设置最大文件大小，甚至可以选择输出语言。

创建者强调了“代理式编码”和Pocket Flow的使用，它们通过让AI代理（如Cursor AI）根据人类设计处理编码过程，从而实现更快的开发。帖子还提供了YouTube开发教程和一个Substack帖子的链接，以便更深入地解释该过程。

---

## 27. 乌鸦能识别几何规律

**原文标题**: Crows can recognize geometric regularity

**原文链接**: [https://phys.org/news/2025-04-crows-geometric-regularity.html](https://phys.org/news/2025-04-crows-geometric-regularity.html)

乌鸦能识别几何规律：一项发表于《科学进展》的研究显示

---

## 28. 找出奇特的磁盘

**原文标题**: Find the Odd Disk

**原文链接**: [https://colors2.alessandroroussel.com/](https://colors2.alessandroroussel.com/)

这款游戏名为“找出不同颜色的圆盘”，是一个简单的在线颜色实验。玩家需要在众多圆盘中找出颜色不同的那个。请依靠您的视觉，并关闭屏幕上的任何蓝光过滤功能，以确保颜色感知的准确性。

游戏包含多个“回合”（示例显示的是第1回合，共20回合）。 完成所有回合，或未能找到不同颜色的圆盘，游戏会显示“游戏结束！”信息。

游戏中还包含英文、法文和西班牙文的鼓励语，感谢玩家的参与并邀请他们再次游戏，强调更多的数据可以改善实验。为此，游戏提供了一个“Play Again（再玩一次）”按钮。 本质上，这款游戏旨在收集有关人类颜色感知和辨别能力的数据。

---

## 29. TikZJax：在HTML中嵌入LaTeX绘图

**原文标题**: TikZJax: Embedding LaTeX Drawings in HTML

**原文链接**: [https://tikzjax.com/](https://tikzjax.com/)

TikZJax是一个JavaScript库，允许将LaTeX TikZ图形直接嵌入到HTML页面中，并将其转换为SVG。它完全在浏览器内运行。要使用它，需要在HTML的`<head>`中包含来自TikZJax网站的必要CSS和JavaScript文件。然后，可以将TikZ代码放置在`<body>`中的`<script type="text/tikz">`标签内。TikZJax会自动编译这些代码，并将脚本标签替换为生成的SVG图像。本文通过创建圆形和交换图的例子来演示这一点。

TikZJax的核心技术包括使用web2js将TeX的Pascal源代码编译为WebAssembly。加载一个最小的LaTeX格式，然后执行一个特定的TikZ LaTeX preamble。生成的内核被转储、压缩，然后在浏览器中重新加载，从而可以快速执行TikZ代码。使用PGF的SVG驱动程序，以及dvi2html，DVI输出被转换为SVG图像，所有这些都在客户端发生。

---

## 30. 电影加密原理

**原文标题**: How encryption for Cinema Movies works

**原文链接**: [https://serverless.industries/2024/05/31/digital-cinema.en.html](https://serverless.industries/2024/05/31/digital-cinema.en.html)

本文概述了电影加密的工作原理，重点介绍了DCI（数字电影倡议）标准。DCI标准定义了电影行业中使用的文件格式、加密和放映系统。

作者探讨了发行过程，从制片人创建DCP（数字电影包）和一个包含用发行商证书加密的AES密钥的DKDM（发行密钥传递消息）开始。然后，发行商验证投影机，为电影院创建一个KDM（密钥传递消息），并将DCP和KDM发送到电影院。投影机使用KDM解密DCP以进行播放。

本文描述了放映系统的组件（服务器、媒体块、音频处理器、投影机），并解释说DCP被加密存储，并由投影机的媒体块实时解密。DCP的结构得到了详细说明，包括文件夹命名约定、用于视频和音频的MXF文件和字幕格式。补充DCP（VF）允许替换音频或字幕轨道，而无需复制整个图像数据。

发行过程依赖于证书链和可信设备列表。DCP的AES密钥在使用投影机的公钥的KDM中进行加密。本文概述了解密KDM和验证其内容所涉及的步骤。

作者还谈到了构建定制DCI投影机的挑战，指出发行商依赖“可信设备列表”和授权安装来防止未经授权的播放。最后，本文深入探讨了MXF文件格式，重点介绍了BER编码和单个电影帧三元组的结构。

---

## 31. 锯齿状AGI：o3、Gemini 2.5及之后的一切

**原文标题**: Jagged AGI: o3, Gemini 2.5, and everything after

**原文链接**: [https://www.oneusefulthing.org/p/on-jagged-agi-o3-gemini-25-and-everything](https://www.oneusefulthing.org/p/on-jagged-agi-o3-gemini-25-and-everything)

伊森·莫里克的文章《锯齿状AGI：o3、Gemini 2.5及未来》探讨了人工智能的最新进展，特别是o3和Gemini 2.5 Pro等模型的发布，以及它们对通用人工智能（AGI）的影响。莫里克指出，由于现有针对人类设计的测试的局限性，定义和衡量AGI存在困难。

文章重点介绍了泰勒·科文声称o3是AGI的观点，并引用了其增强的能力，例如生成全面的营销计划、通过网络搜索进行地理位置猜测以及分析复杂数据集。虽然印象深刻，莫里克引入了“锯齿状AGI”的概念来描述这些AI系统的不均衡能力，它们可以在复杂的任务中表现出色，但在简单的任务中失败，例如谜语解答的例子。

莫里克质疑这些模型是否真正代表AGI，因为存在定义问题以及它们在某些领域的不可靠性。尽管如此，他承认它们由于在特定任务中具有“超人”能力，因此有可能对工作和生活产生重大影响。他还探讨了AGI是否只是技术的逐步改进。

文章最后考虑了人工智能在社会中的采用和整合速度。尽管历史趋势表明扩散过程缓慢，但莫里克提出了o3等模型的代理能力可能会加速这一过程的可能性。最终，莫里克认为，驾驭人工智能能力的“锯齿状景观”对于适应未来人工智能的任何进步至关重要。

---

## 32. Bluesky上的新型验证方式

**原文标题**: A New Form of Verification on Bluesky

**原文链接**: [https://bsky.social/about/blog/04-21-2025-verification](https://bsky.social/about/blog/04-21-2025-verification)

Bluesky推出全新多层验证系统，以增强平台用户信任度。除了现有的域名即用户名验证方法（已被超过27万个账号使用）外，Bluesky现新增由Bluesky主动验证的、在真实且知名账号名称旁显示的蓝色勾选标记。

此外，Bluesky授权精选的独立组织作为“可信验证者”。这些组织可以直接向其信任的账号（例如《纽约时报》验证其记者）颁发蓝色勾选标记（以扇形设计区分）。 Bluesky审核团队仍会审查这些验证的真实性。用户可以通过点击蓝色勾选标记查看验证该账号的组织。

用户还可以通过设置隐藏应用程序中的所有验证标识。

目前，Bluesky暂不接受直接申请新的蓝色勾选验证。但他们鼓励组织和个人通过将域名设置为用户名来进行自验证。 Bluesky计划在新系统稳定后推出验证和可信验证者申请表。目标是通过平台验证和社区验证相结合的方式建立信任。

---

## 33. 在ArXiv内部

**原文标题**: Inside ArXiv

**原文链接**: [https://www.wired.com/story/inside-arxiv-most-transformative-code-science/](https://www.wired.com/story/inside-arxiv-most-transformative-code-science/)

本文探讨了由物理学家保罗·金斯帕格创建的数字存储库arXiv的历史和影响。arXiv彻底改变了科学出版，它允许研究人员以预印本的形式即时分享他们的研究成果，绕过了传统学术期刊中由营利性出版商主导的漫长同行评审过程。它已成为数学、物理学和计算机科学领域科学家的不可或缺的工具，促进了知识的快速传播和合作。

本文详细介绍了金斯帕格的历程，从最初在他NeXT机器上用shell脚本创建arXiv，到如今成为托管数百万篇论文的关键基础设施。文章重点介绍了关键时刻，例如埃德·威滕等有影响力人物的早期采用，以及确保非独家发行权的战略决策，从而防止出版商将其关闭。

尽管取得了成功，arXiv也面临着挑战，包括规模扩展问题、低质量提交的审核以及官僚障碍。金斯帕格被描述为一个才华横溢但非常规的人物，他仍然深度参与其中，不断寻求改进平台的方法，包括使用人工智能开发“民科过滤器”。本文强调了arXiv在加速科学进步方面的关键作用，尤其是在像新冠疫情这样的危机期间，以及它作为前沿研究的主要来源的持续重要性。

---

## 34. X射线防御

**原文标题**: X-Ray Defence

**原文链接**: [https://lichess.org/@/Mcie/blog/x-ray-defence-hidden-resource-sudden-lifeline/HERaZrZg](https://lichess.org/@/Mcie/blog/x-ray-defence-hidden-resource-sudden-lifeline/HERaZrZg)

X射线防御：隐藏的资源，突现的生机

本文“X射线防御：隐藏的资源，突现的生机”探讨了X射线主题在国际象棋中的防御应用。它是之前一篇关于X射线攻击文章的后续，重点关注棋子如何通过另一棋子的身体间接防御一个格子或棋子。

作者认为防御战术常常被忽视，但对于提高棋艺至关重要。他们提供了六个难度递增的例子，其中X射线防御是挽救原本失败局面的关键。这些例子说明了看似不在行动范围内的棋子如何通过穿透另一棋子来观察关键格子，从而做出防御贡献。

文章强调了识别间接视线和考虑所有可能的走法（即使是看似后退或非常规的走法）的重要性。它还涉及防御性X射线有时如何导致反击和赢得优势。

作者鼓励读者重温本文和之前关于X射线攻击的文章，以便更好地内化这种主题。他们还建议探索相关的战术主题，如交叉牵制和空格上的隐藏棋步。文章最后邀请读者访问作者的国际象棋博客，以获取更多战术和战略课程。

---

## 35. 信号嘉年华

**原文标题**: Signal Carnival

**原文链接**: [https://www.quiss.org/signal_carnival/](https://www.quiss.org/signal_carnival/)

C64上的“信号嘉年华”巧妙地交换了音频和视频线，从视频信号产生有意义的音频，并从音频信号产生视频，这是一种新颖的方法。

音频由VIC芯片的频率（7.9Mhz）驱动，并通过6502处理器以246kHz写入值。该演示利用两个定时器创建一个波形，每帧调整一次，并将产生的亮度值写入屏幕颜色寄存器（$d020）。这占用了所有四个定时器，因此使用光笔电路进行视频稳定。音乐是单音，但频繁切换以创造复音效果。

视频是使用SID芯片生成的。音量寄存器（$d418）提供即时输出，非常适合视频生成。然而，信号会通过一个模拟带通滤波器，产生模糊、宽大的像素。该演示通过使用x轴来呈现诸如可以容忍模糊的纹理等元素来适应这一点。采用原始的视频位操作，并使用精确的水平同步时间来避免与垂直同步混淆。水平频率被调整（64个周期），而不是标准的63个周期。

该演示还具有一个自定义加载器，可以在加载、解压缩和数据传输期间保持音频，并执行即时GCR解码。该加载器是一次性的，缺乏从更高磁道加载或校验和等功能。一个求解器生成解码表，作者计划发布此工具。

---

## 36. Ubuntu 25.04 “快乐海鹦” 起飞

**原文标题**: Ubuntu 25.04 "Plucky Puffin" Takes Flight

**原文链接**: [https://techstrong.it/featured/ubuntu-25-04-plucky-puffin-takes-flight/](https://techstrong.it/featured/ubuntu-25-04-plucky-puffin-takes-flight/)

Ubuntu 25.04 “Plucky Puffin” 正式发布，为这款流行的 Linux 发行版带来了一系列改进和新功能。主要亮点包括采用 Mutter 中动态三重缓冲实现的更流畅动画的 GNOME 48 桌面环境，以及“健康面板”和“保持电池健康”模式。Nautilus 文件管理器也更快，尤其是在处理大型文件夹时。

在底层，Ubuntu 25.04 使用 Linux kernel 6.14，增强了硬件支持、能源效率和安全性。通过 Wine/Proton 的 NTSYNC 驱动程序，游戏性能得到提升。安装程序提供了更无缝的体验，尤其是在与 Windows 双启动时。

虽然 Ubuntu 仍然提供最少的默认应用程序，但现在包含了 Papers PDF 阅读器。网络和身份管理方面的改进包括使用网络时间安全协议（NTS）的安全时间同步以及更好的 Active Directory 集成。

一个重要的补充是“devpacks”，它是针对 Go 和 Spring 等流行框架的 snap 软件包，以及针对 Python、Rust、.NET、LLVM 和 OpenJDK 的更新工具链。

Kubuntu、Xubuntu 和 Ubuntu MATE 等官方 Ubuntu 衍生版本也已更新。对 25.04 版本的支持将持续九个月，长期支持可通过 Ubuntu 24.04 获得。文章最后提供了硬件建议和一个简化的安装指南。

---

## 37. 可启动容器时代 Linux 主题的乐趣

**原文标题**: The Joy of Linux Theming in the Age of Bootable Containers

**原文链接**: [https://blues.win/posts/joy-of-linux-theming/](https://blues.win/posts/joy-of-linux-theming/)

在“可启动容器时代 Linux 主题美化的乐趣”一文中，作者探讨了使用可启动容器，特别是 bootc，进行 Linux 主题美化和定制的好处。作者对传统方法的不稳定性感到沮丧，发现 bootc 将操作系统定义为 Containerfile，提供了一种可靠且易于恢复的方式来试验主题和配置。更改在容器中进行、构建，然后切换到该容器，从而实现安全测试并在必要时轻松回滚。

虽然存在替代方法，例如 shell 脚本、systemd-sysext 和 Nix，但 bootc 因其灵活性、工具支持、安全性和可靠性而备受赞誉，使得破坏 /usr 目录变得困难。开发模式通过提供临时的可写 overlayfs 来进行快速测试，从而进一步增强了工作流程。

作者随后深入探讨了在可启动容器时代，构成“Linux 发行版”的界限变得模糊的问题，并以他们自己的 Blue95 项目为例。像 Project Bluefin 和 Bazzite 这样基于 bootc 构建的项目通常被称为发行版，但这种区别正变得越来越模糊。最终，作者认为，创建可启动容器，即使是像主题这样简单的定制，也能带来乐趣，并实现个性化和创造性的计算体验。

---

## 38. 分解事务系统

**原文标题**: Decomposing Transactional Systems

**原文链接**: [https://transactional.blog/blog/2025-decomposing-transactional-systems](https://transactional.blog/blog/2025-decomposing-transactional-systems)

本文通过将事务系统分解为执行、排序、验证和持久化四个基本步骤，剖析了事务系统。它强调，虽然所有事务系统都执行这些步骤，但它们的执行顺序和并发性会导致不同的权衡和架构设计。

作者随后考察了三个真实世界的数据库系统：FoundationDB、Spanner 和 TAPIR，以说明这些步骤如何在实践中体现。FoundationDB 被描述为一个经典的乐观并发控制数据库，事务被执行，获取提交版本，检查冲突，最后，事务变得持久。

Spanner 被描述为一个悲观并发控制数据库。它将执行和验证与事务执行期间获取的读锁交织在一起。写入被缓冲，并使用两阶段提交在参与者之间进行验证，然后确定最终的提交版本并使事务持久。然后释放锁。尽管很复杂，但 Spanner 被认为在根本上类似于 SERIALIZABLE MySQL。

TAPIR 旨在提高延迟和吞吐量，它被描述为执行事务，提出提交时间戳，对副本执行并发验证，然后根据副本的共识提交或中止。

文章最后表明，即使是复杂的分布式数据库，也可以通过将其事务处理分解为执行、排序、验证和持久化这些核心要素来理解，从而更清楚地了解它们的架构和设计选择。

---

## 39. 健康的土壤是隐藏的要素。

**原文标题**: Healthy soil is the hidden ingredient

**原文链接**: [https://www.nature.com/articles/d41586-025-01026-x](https://www.nature.com/articles/d41586-025-01026-x)

本文强调了健康土壤的关键重要性，尤其是在欧盟，那里60-70%的土壤被认为是不健康的，导致了巨大的经济和健康成本。西班牙面临严重的土壤退化，是一个重点关注的国家。本文介绍了赫苏斯·罗德里戈·科米诺，一位研究西班牙葡萄园可持续土壤管理实践的地理学家。他利用地理测绘系统和人工智能来帮助农民就灌溉、覆盖作物和耕作做出明智的决策，以防止土壤侵蚀。

罗德里戈·科米诺参与了SOILCRATES项目，该项目是欧盟“欧洲土壤协议”倡议的一部分，旨在创建合作田间试验点，科学家、农民和政策制定者可以在这里试验和推广可持续土壤实践。该项目强调教育公众了解健康土壤的重要作用。

气候变化通过气温升高、降水减少和更频繁的极端降雨事件加剧了土壤退化。这些变化正在影响西班牙的葡萄园，导致更早的开花和土壤侵蚀加剧。虽然关于气候变化对葡萄园影响的具体数据仍在收集，但趋势已经很明显，这促使人们需要立即采取全面行动来保护和改善土壤健康。

---

## 40. Show HN: 热插拔代码，让你的PyTorch模型留在VRAM中

**原文标题**: Show HN: Keep your PyTorch model in VRAM by hot swapping code

**原文链接**: [https://github.com/valine/training-hot-swap/](https://github.com/valine/training-hot-swap/)

这个"Show HN"帖子介绍了一种热插拔PyTorch训练代码的方法，无需从VRAM卸载大型模型，从而显著缩短开发时间。加载大型语言模型可能需要相当长的时间（例如，30秒），导致迭代开发速度缓慢。该解决方案涉及使用Python的`eval()`在单独的后台进程中运行训练代码。即使主训练脚本退出，此后台进程仍然存在，使模型保留在VRAM中。当再次运行训练脚本时，模型可以立即使用。

该系统采用客户端-服务器架构。`model_server.py`脚本托管模型并执行由`client.py`脚本发送的代码。这实现了远程代码执行，可能解决了像IntelliJ中远程SSH解释器的问题。服务器还支持集成DearImgui Python绑定，允许用户构建UI来监控训练进度和评估模型，这些UI在脚本运行时会立即加载。

该帖子提供了将标准`.from_pretrained`调用替换为服务器管理的全局变量'model'引用的说明。必须先启动服务器，然后再通过客户端向其提交训练代码。

作者警告说，由于执行任意代码，这种方法存在安全风险，并建议不要将服务器直接暴露于互联网。

---

## 41. Falsify：受假设启发的 Haskell 收缩 (2023)

**原文标题**: Falsify: Hypothesis-Inspired Shrinking for Haskell (2023)

**原文链接**: [https://www.well-typed.com/blog/2023/04/falsify/](https://www.well-typed.com/blog/2023/04/falsify/)

本文介绍 Falsify，一个受 Hypothesis 启发的新 Haskell 属性测试库，重点介绍其独特的缩减方法。与单元测试不同，属性测试使用随机生成的输入并验证属性。缩减对于在测试失败时找到最小的、相关的反例至关重要。

Falsify 不同于 QuickCheck 的地方在于，它遵循 Hypothesis 的做法，缩减的是随机样本流，而不是生成的实际值。然而，falsify 使用无限样本树，而不是 Hypothesis 的线性样本流。这意味着，falsify 执行单次遍历，缩减树中的单个样本，而不是像 Hypothesis 那样进行多次缩减。这种选择带来了更可预测的缩减行为。由于单子绑定会分割样本树，因此 int 保证不受 list 行为的影响。这与 Hypothesis 风格的缩减不同。

在 Falsify 中使用样本树有两个关键后果：样本树如何缩减（使用偏序和单次遍历），以及样本如何通过与 applicative <*> 或 monadic >>= 组合期间的树分裂分发给解析器。

Falsify 的设计避免了集成缩减（QuickCheck 和 Hedgehog 使用）在单子绑定方面的限制，允许 `(>>=)` 操作两侧的生成器进行独立缩减。这使得 falsify 可以在返回并缩减列表长度之前缩减列表中的元素值。与基于流的方法相比，这种方法带来了更可预测和可理解的缩减行为，最终有助于调试。

---

## 42. Python中的正则表达式导数 [pdf] [视频]

**原文标题**: Regular Expression Derivatives in Python [pdf] [video]

**原文链接**: [https://archive.fosdem.org/2018/schedule/event/python_regex_derivatives/attachments/slides/2363/export/events/attachments/python_regex_derivatives/slides/2363/fosdem2018.pdf](https://archive.fosdem.org/2018/schedule/event/python_regex_derivatives/attachments/slides/2363/export/events/attachments/python_regex_derivatives/slides/2363/fosdem2018.pdf)

此文档似乎是已损坏或错误编码的PDF文件，可能与“Python中的正则表达式导数”有关。乱码字符表明内容在处理或保存时出现问题。因此，无法得出任何有意义的内容摘要。它可能包含以下信息：

*   正则表达式（regex）
*   正则表达式的导数（形式语言理论中的一个特定概念）
*   正则表达式导数的Python实现。
*   可能是一个教程或演示文稿。

但如果没有正确呈现的PDF，则无法进行适当的摘要。该文档很可能包含与使用导数方法构建正则表达式匹配系统相关的代码示例、数学符号和解释。

---

## 43. 更好的错误处理

**原文标题**: Better Error Handling

**原文链接**: [https://meowbark.dev/Better-error-handling](https://meowbark.dev/Better-error-handling)

本文探讨了 TypeScript 和 JavaScript 中错误处理的挑战，强调了传统 `try/catch` 方法的局限性，尤其是在复杂应用程序中。尽管 `try/catch` 很常用，但它缺乏类型安全（捕获的错误通常被类型化为 `unknown`）以及与类型系统的集成，这使得难以保证正确的错误处理，并识别潜在问题，例如第 43 行上的错误，该错误抛出的错误没有 `.message` 属性。

本文提出了两种现代方法：Go 风格的返回元组和 Monadic 风格的 Result 类型。

*   **Go 风格的元组** 返回结果或错误，提供了简单性，但需要积极的错误处理并可能导致代码冗长。
*   **Monadic Result 类型**（例如，使用像 neverthrow 这样的库）将错误视为容器中的值，允许链式调用和延迟评估，但引入了更陡峭的学习曲线和更复杂的 API。

作者承认，`try/catch` 对于较简单的前端应用程序可能足够，尤其是在像 tanstack/query 或 apolloClient 这样的库处理网络错误的情况下。然而，Go 风格和 Monadic 方法为更复杂的场景提供了更好的类型安全性和控制流管理。

本文还强调了采用像 Effect 这样改变范式的库的认知负担，告诫组织要完全投入并为类似于采用新编程语言的学习曲线做好准备。

最后，它提出了将错误作为值返回使得难以使用堆栈跟踪来识别错误可能来自何处的问题。

---

## 44. 通过线性定理突破LLM量化的极限

**原文标题**: Pushing the Limits of LLM Quantization via the Linearity Theorem

**原文链接**: [https://arxiv.org/abs/2411.17525](https://arxiv.org/abs/2411.17525)

本文介绍了一种基于“线性定理”的大语言模型（LLM）量化新方法，该定理建立了层级重建误差（特别是 $\ell_2$ 误差）与量化引起的模型困惑度增加之间的直接关系。该定理为分层量化策略提供了理论依据，摆脱了当前方法中普遍存在的经验方法。

作者利用该定理开发了两个关键应用：

1. **HIGGS（用于量化的 Hadamard 启发网格）：** 一种使用 Hadamard 旋转和 MSE 最优网格的无数据量化方法。HIGGS 优于现有的无数据量化技术，包括广泛使用的 NF4 格式。

2. **最优非均匀量化：** 一种用于寻找满足中等位宽范围内的给定压缩约束的最优非均匀逐层量化级别的解决方案。该解决方案通过将问题简化为动态规划获得。

本文通过对 Llama-3.1、Llama-3.2 和 Qwen 模型进行的实验证明了这些方法的有效性。结果表明，与以往的方法相比，精度-压缩权衡有所改善。此外，作者强调了其方法的高效 GPU 内核支持，从而促进了 LLM 的无数据和非均匀量化。总而言之，这项工作为 LLM 量化提供了理论基础和实践进步，从而实现了更好的压缩和性能。

---

## 45. 图灵绘画

**原文标题**: Turing-Drawings

**原文链接**: [https://github.com/maximecb/Turing-Drawings](https://github.com/maximecb/Turing-Drawings)

图灵绘图：利用图灵机生成图像及动画的演示项目，采用JavaScript和HTML5实现，遵循修改后的BSD许可协议，可在http://maximecb.github.io/Turing-Drawings/在线体验。其核心概念是利用图灵机的计算能力生成视觉输出，包括分形、扫描模式、矩阵式显示、运动、复杂计算、几何形状（四边形、鳍、叶片）、混沌图案以及其他抽象和动态视觉效果。作者还撰写了一篇博文，更详细地介绍了该项目。本质上，图灵绘图是对图灵机这一基本计算模型生成算法艺术的一次迷人探索。

---

## 46. 新证明解决了关于连接网络的数十年之久的赌局

**原文标题**: New Proof Settles Decades-Old Bet About Connected Networks

**原文链接**: [https://www.quantamagazine.org/new-proof-settles-decades-old-bet-about-connected-networks-20250418/](https://www.quantamagazine.org/new-proof-settles-decades-old-bet-about-connected-networks-20250418/)

本文讲述了数学家Noga Alon和Peter Sarnak之间关于最优扩展图，即拉马努金图，在更广泛的正则图类别中普遍性的数十年之久的赌注。Alon认为拉马努金图在随机图中会很常见，而Sarnak则认为它们会很稀有，需要复杂的构造。

本文解释了扩展图的重要意义，它们在各种系统建模中的应用，以及“Alon-Boppana界”在定义最优扩展器中的重要性。然后详细介绍了Sarnak及其合作者如何利用数论构建拉马努金图。

经过数十年的争论，数学家黄家阳、Theo McKenzie和姚鸿泽最终解决了这个赌注。通过将普适性猜想（最初由物理学家尤金·维格纳针对随机矩阵提出）扩展到随机正则图的邻接矩阵的特征值，他们精确地确定了特征值的分布。他们的计算表明，大约69%的随机正则图是拉马努金图，这意味着Alon和Sarnak的观点都不是完全正确的。本文强调了问题的难度，与物理学的意外联系，以及该证明对我们理解随机矩阵和图论的影响。

---

## 47. 西斯复仇中的穿帮谜团

**原文标题**: The movie mistake mystery from "Revenge of the Sith"

**原文链接**: [https://fxrant.blogspot.com/2025/04/the-movie-mistake-mystery-from-revenge.html](https://fxrant.blogspot.com/2025/04/the-movie-mistake-mystery-from-revenge.html)

托德·瓦齐里在他的博文中深入探讨了《西斯的复仇》中一闪而过的“原力幽灵”之谜。他探讨了电影失误现象，这些透过电影幕布的窥视揭示了电影制作中的艺术和工艺，并列举了《光荣战役》、《好家伙》、《异形》、《决斗》、《蝙蝠侠：黑暗骑士》和《深渊》等电影的例子。他还对在电影修复项目中消除这些失误的趋势表示遗憾，认为这构成了一种修正主义历史。

文章的核心集中在穆斯塔法决斗场景中阿纳金·天行者身后短暂出现的“原力幽灵”。曾在工业光魔（ILM）工作并参与了该片制作的瓦齐里回忆了互联网是如何被这种异常现象迷住的。出于好奇心和持续的在线讨论，瓦齐里开始了个人调查，深入研究了ILM的存档素材。

在检索了原始绿幕素材后，他发现“原力幽灵”实际上是一位穿着奇特衬衫的特技装备员，正在手动操作熔岩飞艇。在合成过程中，当艺术家正在完善绿幕提取的边缘时，装备员的图像溜了进去。尽管经过了多层审查，这个错误直到多年后才被眼尖的观众发现。瓦齐里总结说，这个“错误”证明了视觉效果的手工性质，也是ILM历史上令人喜爱的一部分。他强调“完美是优秀的敌人”，这些小瑕疵为电影的魅力做出了贡献。

---

## 48. 泰国当局如何利用网络人肉搜索压制异议

**原文标题**: How Thai authorities use online doxxing to suppress dissent

**原文链接**: [https://citizenlab.ca/2025/04/how-thai-authorities-use-online-doxxing-to-suppress-dissent/](https://citizenlab.ca/2025/04/how-thai-authorities-use-online-doxxing-to-suppress-dissent/)

本文详细介绍了“JUICYJAM”，这是一个持续性的、有组织的社交媒体骚扰和人肉搜索活动，自 2020 年 8 月以来一直针对泰国民主运动。研究人员根据 2025 年 3 月泄露的机密文件，将该活动归因于泰国皇家武装部队和/或泰国皇家警察。该行动利用虚假身份“Juk Khlong Sam 女士”，在 X 和 Facebook 等平台上识别和曝光亲民主抗议者的个人信息，敦促关注者骚扰他们并向警方举报。

JUICYJAM 以其庞大的粉丝数量和参与度脱颖而出，成为一项成功的国家赞助的影响力行动。它在更大的背景下运作，即针对泰国异议人士的线上和线下压制策略，类似于香港的情况。该报告强调了社交媒体平台在解决旨在压制公民社会的有组织的人肉搜索活动方面的不足，特别是考虑到国家赞助和动荡的背景。

本文详细介绍了 JUICYJAM 的时间线，从 2020 年 8 月的两个博客开始，随后扩展到包括 X、Facebook（群组和页面）、Instagram、TikTok、Telegram 和 Threads 等多个平台。虽然核心活动侧重于 X 个人资料和 Facebook 群组，但“非官方”的 Facebook 页面会放大相同的骚扰内容。泄露的文件显示，JUICYJAM 是通过激进手段压制抗议团体和叙事的深思熟虑策略的一部分。

---

## 49. 一个80年代的玩具机械臂启发了现代机器人技术。

**原文标题**: A 1980s toy robot arm inspired modern robotics

**原文链接**: [https://www.technologyreview.com/2025/04/17/1114456/toy-armatron-modern-robotics-ai-nostalgia/](https://www.technologyreview.com/2025/04/17/1114456/toy-armatron-modern-robotics-ai-nostalgia/)

本文探讨了20世纪80年代玩具机械臂阿玛创（Armatron）的遗产，以及它对现代机器人技术的惊人影响。作者回忆起童年时期对该玩具的迷恋，并联系了它的发明者渡边博幸，一位来自多美（现为Takara Tomy）的退休工程师。

渡边透露，阿玛创尽管功能强大，但完全是机械的，是复杂齿轮箱设计的壮举。受报纸剪报和无线电遥控直升机的启发，渡边的发明提供了由双操纵杆控制的六个自由度。

阿玛创出乎意料地获得了机器人工程师和大学研究人员的认可。文章重点介绍了波士顿动力公司的机械设计工程师亚当·博雷尔和加州大学伯克利分校的电气工程和计算机科学教授埃里克·保卢斯，他们小时候都受到了该玩具的启发。博雷尔对机械齿轮传动装置着迷，而保卢斯则沉迷于探索捡起东西并移动它们的过程。

文章将阿玛创带来的机械挑战与当前人工智能驱动的机器人研究（如物体操作和抓取技术）进行了比较。最终，阿玛创鼓励孩子们探索模拟力学，渡边表示很高兴看到新一代粉丝不断重新发现和改进它。文章最后强调，虽然人工智能可能正在接管机器人领域，但该领域仍然需要能够在物理世界中解决问题的工程师。

---

## 50. 新冠疫情期间的数字盗版

**原文标题**: Digital piracy in times of Covid-19

**原文链接**: [https://link.springer.com/article/10.1007/s10824-025-09538-0](https://link.springer.com/article/10.1007/s10824-025-09538-0)

新冠疫情期间的数字盗版

---

## 51. 对抗感染的分子也会影响大脑

**原文标题**: Molecules that fight infection also act on the brain

**原文链接**: [https://news.mit.edu/2025/molecules-fighting-infection-act-in-brain-inducing-anxiety-or-sociability-0407](https://news.mit.edu/2025/molecules-fighting-infection-act-in-brain-inducing-anxiety-or-sociability-0407)

麻省理工学院和哈佛医学院的两项新研究表明，免疫分子IL-17作用于大脑，影响疾病期间的行为。研究人员发现，IL-17影响两个不同的脑区：杏仁核和体感皮层，导致不同的影响。在杏仁核中，IL-17通过增加神经元兴奋性来诱发焦虑，而在体感皮层，特别是S1DZ区域，它通过降低神经元兴奋性来促进社交行为。

这些发现表明免疫系统和神经系统之间存在紧密的相互联系。IL-17最初被认为仅具有免疫功能，但现在看来它在大脑中充当神经调节剂，调节神经元活动。这种作用可能进化得更早，后来被免疫系统所利用。

该研究还发现，阻断杏仁核中的IL-17受体反而会增加IL-17C的水平，这可能解释了在银屑病治疗的临床试验中观察到的不良精神健康影响。这表明IL-17对感染期间焦虑的影响可能是一种有益的反应，旨在促进隔离并防止疾病传播。

研究人员强调，发现IL-17在不同脑区具有多样化的影响，可能通过靶向免疫系统来影响大脑功能，从而为自闭症和抑郁症等神经系统疾病带来新的治疗方法。

---

## 52. 走向旧金山

**原文标题**: Slouching towards San Francisco

**原文链接**: [https://rachdele.substack.com/p/slouching-towards-san-francisco](https://rachdele.substack.com/p/slouching-towards-san-francisco)

无法访问文章链接。

---

## 53. 哪一年：猜猜每张照片拍摄于哪一年

**原文标题**: Which year: guess which year each photo was taken

**原文链接**: [https://whichyr.com/](https://whichyr.com/)

哪年：照片猜年份游戏。玩家通过识别历史照片来猜测拍摄年份。目标是通过时间轴滑块（1850-2025）猜测年份，并根据猜测的准确性获得积分。猜测越接近实际年份，获得的积分越多，完全猜中可获得最高分。

游戏包含“数字提示”功能，帮助玩家在卡住时获得提示。此功能会揭示正确年份的一个数字，但每张照片在每局游戏中只能使用一次。

“每日挑战”每天提供一组新的照片，让玩家测试知识、与他人比较分数并跟踪进度。该游戏旨在促进视觉记忆、教育，且具有高度的吸引力。

---

## 54. 展示：JuryNow – 从12位真人处获得匿名即时判决

**原文标题**: Show HN: JuryNow – Get an anonymous instant verdict from 12 real people

**原文链接**: [https://jurynow.app/](https://jurynow.app/)

JuryNow是一项服务，它提供来自12位真实人士小组的即时、匿名裁决。“Show HN”帖子表明这是向Hacker News社区发布或演示该服务。本质上，JuryNow旨在提供一种快速且易于访问的方式来衡量公众对特定问题或情景的看法，模拟陪审团体验，但置于数字化的、按需的环境中。

其核心卖点是能够随时随地接收来自12个不同角度的、匿名的对某情况的看法。这表明该平台设计为用户友好型，并且易于在移动设备上访问（“放在你的口袋里”）。目标受众可能包括个人或组织，他们希望了解一群公正的人可能对特定事件、论点，甚至是产品创意作何反应。这是一种获取潜在公众情绪快照的简化方式。

---

## 55. 树莓派激光雷达扫描仪

**原文标题**: Raspberry Pi Lidar Scanner

**原文链接**: [https://github.com/PiLiDAR/PiLiDAR](https://github.com/PiLiDAR/PiLiDAR)

PiLiDAR项目：围绕Raspberry Pi构建的DIY 360° 3D全景扫描仪。它使用LDRobot LD06、LD19或STL27L激光雷达进行距离测量，并使用带鱼眼镜头的Raspberry Pi HQ摄像头捕捉全景图像。一个由A4988驱动器控制的NEMA17步进电机旋转扫描仪。

主要功能包括带有CRC校验的自定义激光雷达串口驱动、硬件PWM校准、2D实时可视化、使用Hugin的6K 360°全景拼接，以及使用Open3D可视化和导出的2D平面3D场景组装。它还允许使用全局注册和ICP对齐多个扫描。

该项目概述了硬件规格、接线图，以及电源按钮、加速度计、CPU风扇、扫描按钮和UART等组件的详细设置说明。它涵盖了硬件PWM、全景拼接、远程Jupyter访问和USB存储转储的软件安装和配置。该指南还解决了常见问题，如Windows串口驱动问题、RPi.GPIO错误、VS Code性能和pye57安装。最后，提供了相关项目、教程和演示数据的参考。

---

## 56. 令人困惑的书本式Emacs

**原文标题**: Perplexingly Book-Learned Emacs

**原文链接**: [https://lars.ingebrigtsen.no/2025/04/17/perplexingly-book-learned-emacs/](https://lars.ingebrigtsen.no/2025/04/17/perplexingly-book-learned-emacs/)

作者探索使用Perplexity AI LLM来识别喜爱作者的新书，解决区分新作与再版或版本的问题。他们创建了一个简单的Emacs库`perplexity.el`来与Perplexity API交互。虽然Perplexity成功列出了作者的书籍，但其响应不一致，有时甚至出现幻觉。

作者尝试使用诸如列出“缺失书籍”（他们没有拥有的作者书籍）之类的提示，结果好坏参半；Amy Hempel的书籍被准确识别，而Megan Whalen Turner的书籍则不然。响应时间也各不相同。尽管存在这些限制，作者发现该工具足够有用，在测试期间冲动购买了十五本书，并集成了在Bookshop.org上浏览书籍并在Goodreads上验证其存在的命令。

作者随后尝试查询Perplexity，以查找近年来多位追踪作者发布的新书，但遇到了Perplexity愿意在单个请求中执行的搜索数量的限制。他们计划单独循环处理每个作者以汇总结果。

最后，作者比较了Perplexity与Gemini和OpenAI在列出David Sedaris的缺失书籍方面的表现，发现其他LLM没有显着改善。作者的结论是，尽管存在缺陷和限制，但该LLM在跟踪喜爱作者的新发布方面显示出潜力。

---

## 57. 使用Joplin做笔记

**原文标题**: Taking Notes with Joplin

**原文链接**: [https://lwn.net/Articles/1016400/](https://lwn.net/Articles/1016400/)

本文评测Joplin，一款开源、跨平台笔记应用程序。Joplin支持Markdown和富文本编辑，多媒体附件，并通过Nextcloud、WebDAV、Dropbox、OneDrive或Joplin Cloud（付费）等服务提供端到端加密的跨设备同步功能。它还允许本地文件系统同步。

界面采用三窗格布局，包含笔记本、笔记列表和编辑器/查看器。Joplin具有任务管理功能，多窗口支持（自v3.2起），可自定义主题，以及用于扩展的插件系统，包括绘图和OCR功能。

然而，Joplin基于Electron，可能存在较高的资源消耗。同步性能各异，冲突解决能力有限。所见即所得编辑器可能与Markdown不一致，且表格编辑受到限制。该项目开发活跃，定期发布版本，并有社区参与。文章指出Joplin的OCR对于表格等复杂格式效果不佳，并指出需要改进手写文本识别能力。

---

## 58. 数学和故事的注意力跨度 (2019)

**原文标题**: Attention Spans for Math and Stories (2019)

**原文链接**: [https://www.jeremykun.com/2019/03/26/attention-spans-for-math-and-stories/](https://www.jeremykun.com/2019/03/26/attention-spans-for-math-and-stories/)

本文认为，讲故事对于激发儿童（和成人）对数学的兴趣至关重要。作者认为，幼儿虽然聪明，但往往缺乏数学推理和坚持所需的内在好奇心。讲故事通过提供一种无需理由且引人入胜的框架来弥合这一差距，从而理解抽象概念。

作者用轶事来说明这一点，包括一位5岁的匈牙利女孩在听了关于保罗·埃尔德什的故事后，理解了素数的概念。他们还讲述了如何通过讲故事来激励夏令营的孩子们，创造精心设计的秘密特工故事，这些故事融入了数学概念，并鼓励孩子们参与活动。

本文强调了故事如何使数学正常化，使其不再那么可怕，也更容易理解。分享关于数学的积极故事或将其融入睡前故事可以抵消数学焦虑。最终，作者建议最好的方法是从简单、故事驱动的例子开始，并随着学习者逐渐适应，逐渐过渡到更以数学为中心的内容。他们倡导在基本的数字感知和本科水平的数学之间加入更多以故事为中心的内容，并以Numberphile和Beast Academy为例。核心思想是，当呈现出能引起好奇心的模式时，数学可以自然地从故事中产生。

---

## 59. 加拿大各地的家庭画廊隐匿于市井之中

**原文标题**: Home galleries are hiding in plain sight across Canada

**原文链接**: [https://www.cbc.ca/arts/home-galleries-are-hiding-in-plain-sight-across-canada-1.7503886](https://www.cbc.ca/arts/home-galleries-are-hiding-in-plain-sight-across-canada-1.7503886)

在加拿大各地，家庭画廊的趋势日益增长，艺术家和策展人将住宅空间转变为展览场所。受生活成本上涨和创造易于接触的艺术体验的愿望驱动，这些非传统的画廊形式多样，从后院、公寓到车库，甚至是鸡舍。

多伦多艾琳·斯托勒斯的“花园杂物”（Garden Variety）就是这种趋势的例证，她在疫情期间将后院变成了一个临时的艺术空间。同样，玛丽·塞戈莱恩·布劳特在蒙特利尔的阁楼里经营着“莫里斯空间”（Espace Maurice），丹妮卡·品特里奇则在多伦多一间翻新的车库里运营着“欢乐”（Joys）。这些空间促进了社区参与，并为新兴艺术家提供了机会。

其他例子包括多伦多艺术家丽莎·内伯和卡洛·切斯塔家中的画廊“美容用品”（Beauty Supply），邦妮·潘在多伦多公寓中的“条件”（Conditions），位于汉密尔顿车库的兰花当代艺术馆（Orchid Contemporary），甚至还有一个鸡舍被改造成了画廊。这些举措优先考虑代表性不足的艺术家，并为艺术爱好者创造了温馨的环境。杰伊·艾萨克在罗利（新不伦瑞克省）的新项目空间“13棵雪松”（13 Cedars）正在为该地区蓬勃发展的当代艺术景象增添光彩。

虽然在某些地方，如安大略省乡村的亚历山大·朗多（Alexander Rondeau）的“雉鸡之间当代艺术”（Between Pheasants Contemporary）或布雷顿角岛的La Shed，客流量可能有限，但这些家庭画廊培养了当地的艺术氛围，并在网上与更广泛的观众建立联系。它们为艺术家和策展人提供了自主权，降低了成本，并培养了一种社区意识，丰富了加拿大的艺术景象。

---

## 60. 首款无激素男性避孕药进入人体试验

**原文标题**: First hormone-free male birth control pill enters human trials

**原文链接**: [https://scitechdaily.com/99-effective-first-hormone-free-male-birth-control-pill-enters-human-trials/](https://scitechdaily.com/99-effective-first-hormone-free-male-birth-control-pill-enters-human-trials/)

以下是根据标题对文章的总结：

该文章讨论了一种新型男性避孕药，与现有的实验性选择不同，该药不含激素，并且正在进入人体临床试验。这种方法的主要优势在于，它避免了与激素操纵相关的潜在副作用，例如情绪波动、体重增加和性欲改变，这些副作用阻碍了有效且被广泛接受的男性激素避孕药的开发。

据报道，该药在临床前研究（可能指动物试验）中有效率高达99%，其作用机制是靶向并抑制一种名为α-受体的蛋白质，该蛋白质对于精子受精至关重要。通过阻断这种蛋白质，该药可以暂时使精子无法使卵子受精。这种效果旨在是可逆的，允许男性在停止用药后恢复生育能力。人体试验将评估该药物在预防怀孕方面的安全性、耐受性和有效性。这些试验的成功可能代表男性避孕方面的一个重大突破，为男性提供一种非激素和可逆的选择来管理他们的生育能力，并更平等地分担计划生育的责任。该文章可能强调了男性对除避孕套和输精管结扎术之外的避孕选择的未满足需求，并强调了这种新型避孕药对全球生殖健康的潜在影响。

---

## 61. 人群尺度下刺激单个感光细胞实现新型颜色

**原文标题**: Novel color via stimulation of individual photoreceptors at population scale

**原文链接**: [https://www.science.org/doi/10.1126/sciadv.adu1052](https://www.science.org/doi/10.1126/sciadv.adu1052)

无法访问文章链接。

---

## 62. 独特的声响缓解晕动症

**原文标题**: A unique sound alleviates motion sickness

**原文链接**: [https://www.nagoya-u.ac.jp/researchinfo/result-en/2025/04/20250408-01.html](https://www.nagoya-u.ac.jp/researchinfo/result-en/2025/04/20250408-01.html)

名古屋大学研究人员发现，一种独特的声刺激技术，特别是被称为“声音香料®”的100赫兹音频，可以缓解晕动症。在阅读行驶中的车辆、使用驾驶模拟器或荡秋千等诱发晕动症的条件下，参与者只需暴露于该声音一分钟，就能减轻恶心、眩晕和步履蹒跚等症状。

该研究表明，这种声音通过刺激内耳的椭圆囊和球囊器官（负责平衡和空间定向）发挥作用。这种刺激激活了前庭系统，并改善了交感神经活动，而交感神经活动在患有晕动症的个体中通常失调。

研究人员发现，所使用的声音强度在日常环境噪音范围内，使其成为一种潜在安全有效的治疗方法。他们通过监测姿势控制、心电图读数以及使用晕动症评估问卷的主观报告来评估该声音的有效性。结果表明，暴露于这种独特声音后，晕动症症状显著减轻。

在香川匠和加藤正志的带领下，研究团队计划进一步开发该技术，以便在包括航空和海运旅行在内的各种旅行场景中实际应用，为数百万晕动症患者提供潜在的解决方案。

---

## 63. Rust 中优美的状态机模式 (2016)

**原文标题**: Pretty State Machine Patterns in Rust (2016)

**原文链接**: [https://hoverbear.org/blog/rust-state-machine-pattern/](https://hoverbear.org/blog/rust-state-machine-pattern/)

本文探讨如何在 Rust 中实现状态机，目标是找到一种模式，可以在编译时强制执行有效的状态转换，避免堆分配，并有效地利用 Rust 的类型系统。

作者首先将状态机定义为具有不同的状态和转换，并强调强制执行有效转换的重要性。最初使用枚举的尝试存在缺陷，因为它允许无效的状态转换，并且需要冗长的 `match` 语句。

接下来，探讨了使用结构体表示状态，并使用 trait 来实现共享功能。这种方法提供了编译时转换强制执行，并避免了 `match` 语句，但存在代码重复和共享状态不明确的问题。Rust 的 `From` 和 `Into` trait 被引入，作为定义状态转换的一种更简洁的方式。

首选解决方案利用了泛型。一个 `BottleFillingMachine<S>` 结构体保存了共享状态和一个泛型 `state` 字段，类型为 `S`，其中 `S` 代表当前状态。不同的结构体，例如 `Waiting`、`Filling` 和 `Done`，代表了状态。`From` trait 被用于特定的状态转换的实现（例如，`From<BottleFillingMachine<Waiting>> for BottleFillingMachine<Filling>>`）。

这种泛型方法实现了状态转换的编译时验证，清晰的错误消息指示有效的转换，以及一个用于管理共享状态的中心结构，从而实现了本文最初的目标，即在 Rust 中找到一种有效的状态机模式。

---

## 64. 让我们给PRO/VENIX配上一个勉强够用、C89标准之前的TCP/IP协议栈，采用Slirp-CK。

**原文标题**: Let's give PRO/VENIX a barely adequate, pre-C89 TCP/IP stack, featuring Slirp-CK

**原文链接**: [http://oldvcr.blogspot.com/2025/04/lets-give-provenix-barely-adequate-pre.html](http://oldvcr.blogspot.com/2025/04/lets-give-provenix-barely-adequate-pre.html)

本文详细介绍了一个为运行PRO/VENIX V2.0（一个基于System V的Unix移植版本）的DEC Professional 380创建最小TCP/IP协议栈的项目。该项目的目标是使用Pro的串行端口和SLIP连接，在一个官方缺少网络支持的平台上实现基本的网络功能。

作者强调了其历史背景，突出了Pro的不兼容性以及DECnet之外缺乏标准网络选项的情况。他们回顾了Venix的历史，Venix最初是为PDP-11开发的，后来移植到了IBM PC和DEC Rainbow，最终演变为PRO/VENIX。

本文概述了TCP/IP协议栈的设计选择。考虑到硬件的限制以及对简单性的追求，重点是使用单个串行连接的客户端应用程序，优先考虑易于实现性和可移植性。具体目标任务包括网络连通性检查（ICMP）、DNS解析（UDP）、设置系统时间（NTP，UDP）以及使用简单的基于TCP的协议（如HTTP/1.x，使用代理进行HTTPS）获取数据。该方法涉及由各个客户端处理原始数据包并使用RFC 1055 SLIP进行串行通信。

代码将有意地进行约束，使用最少的C标准库函数和字节操作。作者使用两个通过零调制解调器连接的USB串行转换器进行初始测试。

---

## 65. 图书馆员是危险的

**原文标题**: Librarians are dangerous

**原文链接**: [https://bradmontague.substack.com/p/librarians-are-dangerous](https://bradmontague.substack.com/p/librarians-are-dangerous)

我无法访问外部URL，包括您提供的那个。因此，我无法总结Brad Montague的《图书馆员是危险的》这篇文章。

---

## 66. OAuth在MCP安全中的作用

**原文标题**: OAuth's Role in MCP Security

**原文链接**: [https://defensiblesystems.substack.com/p/oauths-role-in-mcp-security](https://defensiblesystems.substack.com/p/oauths-role-in-mcp-security)

无法访问文章链接。

---

## 67. 不要强迫孩子学数学

**原文标题**: Don't force your kids to do math

**原文链接**: [https://blog.avocados.ovh/posts/how-to-force-your-kids-to-do-math/](https://blog.avocados.ovh/posts/how-to-force-your-kids-to-do-math/)

本文反对强迫儿童学习数学，提倡一种寓教于乐、探索性的方法。作者分享了通过游戏和日常活动向儿子介绍数学的个人经历，强调使其愉快而非成为负担的重要性。核心原则是，如果孩子表现出抵触情绪，立即停止，优先考虑他们天生的好奇心。

作者重点介绍了几个策略：将数学融入日常生活（计数、测量、购物时的计算），利用游戏使学习变得有趣（使用积木、纸牌游戏），并将数学融入故事创作引人入胜的情景。重复也被强调为建立理解的关键组成部分。

尽管承认分享热情的愿望，作者告诫不要强加于人，强调尊重孩子不断变化的兴趣并识别细微的不适迹象的重要性。他们强调需要在热情和压力之间取得平衡，并自我反思是在分享还是强加自己的兴趣。

最终，目标不仅仅是获得数学能力，而是培养孩子内在的好奇心，培养终身热爱学习和探索的精神。随着儿子兴趣的变化，作者放弃了结构化的数学游戏，转而赞赏孩子对无穷等数学概念的自主探索，而不是专注于正式的教学。重点是培养孩子天生的学习和求知欲。

---

## 68. 递归式LLM提示

**原文标题**: Recursive LLM prompts

**原文链接**: [https://github.com/andyk/recursive_llm](https://github.com/andyk/recursive_llm)

本文探讨了“递归 LLM 提示”的概念，其中 LLM（如 GPT-3.5）被用作基于英语的“程序”的运行时环境，这些“程序”以提示的形式编写。核心思想是创建一个提示，当 LLM 处理它时，会返回一个略微修改的版本，从而有效地实现递归。这些提示包含状态变量，这些状态变量在每次递归迭代中都会更新，从而更接近定义的 goal 或基本情况，这与传统编程中的递归类似。

作者使用斐波那契数列示例来说明这一概念，其中提示指示 LLM 更新变量以计算下一个斐波那契数。然后，本文深入研究如何使用递归 Python 函数来自动化此过程，该函数使用连续的提示重复调用 OpenAI API。

更大的目标是利用 LLM 记忆的知识和推理能力将问题分解为子步骤，从而从目标条件强化学习和通用问题求解器 (GPS) 系统中汲取灵感。类比类似于人类执行数学运算的方式，即使用通过记忆学习的代数和原子规则。

确定的一个关键挑战是 LLM 偶尔会生成不正确的事实，这突显了对更可靠的知识检索方法（例如，维基百科搜索、代码生成）和自我事实检查机制的需求。

本文还涉及 ACT-R 和 ReAct 等相关研究，并介绍了 LLM 提示中非尾递归的概念，其中提示需要维护中间状态的“堆栈”。

---

## 69. 正则表达式并不难 (2023)

**原文标题**: Regex Isn't Hard (2023)

**原文链接**: [https://timkellogg.me/blog/2023/07/11/regex](https://timkellogg.me/blog/2023/07/11/regex)

本文认为，如果专注于核心子集并避免复杂的快捷方式，正则表达式（regex）并不像通常认为的那么难。作者提倡使用冗长而不是复杂性，强调掌握一个较小且可移植的正则表达式子集，在不同编程语言的文本处理中具有重要的价值。

需要掌握的核心概念：

*   **字符集:** 匹配单个字符或范围 (例如, `a`, `[abc]`, `[a-z]`)。 字符集内的否定 (使用 `^`)。
*   **重复:** 使用 `?` (零或一), `*` (零或多个), 和 `+` (一个或多个) 来重复字符集或组。
*   **组:** 使用括号 `()` 创建子正则表达式，用于重复模式、替换 (使用 `$1` 或 `\1`)，以及提取文本。
*   **|, ^, 和 $ 操作符:** `|` 用于 OR，`^` 用于匹配字符串的开头 (或者字符集内的否定)，以及 `$` 用于匹配字符串的结尾。

本文建议忽略像 `\w`、`\s` 和 `.` 这样的快捷方式，因为它们在不同语言中的行为不一致，以及非贪婪匹配和重复范围。它还建议避免使用像 `(?:` 这样的高级组操作符。

作者强调了该核心子集在现代编程语言中的可移植性，并指出少量的正则表达式知识对于各种文本处理任务都非常有益。

---

## 70. Go中的分层设计

**原文标题**: Layered Design in Go

**原文链接**: [https://jerf.org/iri/post/2025/go_layered_design/](https://jerf.org/iri/post/2025/go_layered_design/)

本文概述了Go程序的分层设计方法，旨在解决该语言对循环包依赖的限制。作者强调，这种分层并非强制性的设计选择，而是Go包导入规则的自然结果。基础层包含没有内部依赖的基本包，后续层在此基础上构建。高层包利用低层包，通过组合它们来实现所需的应用程序功能。

作者反对在Go固有的分层结构之上强加死板的架构。相反，他们提倡将分层结构本身作为一种有效的设计方法来利用，通过可净化的子组件来提升模块化和可测试性。主要优势包括每个包的依赖范围有限，使代码更易于理解和维护，并鼓励只使用必要的组件，降低循环依赖的可能性。

本文提供了一个解决循环依赖问题的实用指南，首先要进行彻底的分析以查明具体原因。解决方案包括将有问题的函数移动到正确的包中，为共享元素创建一个新包（即使它最初看起来很小），使用接口来解耦依赖关系，以及利用依赖注入来实现可配置的行为。作者根据这些解决方案对代码清晰度和设计强度的影响来确定其优先级。

---

## 71. 冰岛选举制度 (2024)

**原文标题**: The Icelandic Voting System (2024)

**原文链接**: [https://smarimccarthy.is/posts/2024-11-25-voting-system/](https://smarimccarthy.is/posts/2024-11-25-voting-system/)

本文阐述了冰岛的双比例代表制投票系统，该系统使用同时包含选区议席（CS）和调整议席（AS）的选区。该系统的目标是平衡基于人口的代表性，最大限度地减少各选区之间投票权的不平等。

议席分配过程涉及一个除数规则，冰岛采用的是洪德法，该规则根据政党的选票和之前分配的议席来决定议席分配。选区议席在每个选区内分配，然后调整议席在全国范围内分配，以纠正比例失调，确保各政党获得的议席能够反映其总体得票份额。5%的门槛将低于该水平的政党排除在调整议席分配之外，但他们保留已赢得的任何选区议席。

作者指出，冰岛对调整议席的分配使用了一种近似方法，而不是 Balinski & DeMange 描述的数学上合理的熵最小化方法，这导致偶尔会出现单调性失效的情况，即一个政党尽管获得了更多选票却失去了一个议席。使用这种不正确的方法的原因是难以用法律术语解释线性优化。

作者建议进行改进，例如大幅增加调整议席的数量，以减少投票的不平等和地方主义。他还建议探索诸如多数裁决之类的评分系统，该系统可以避免阿罗不可能定理，并且更易于理解和实施。作者最后提到了他帮助开发的投票模拟器，用于比较不同的投票系统。

---

## 72. Claude Code: 智能体编程最佳实践

**原文标题**: Claude Code: Best practices for agentic coding

**原文链接**: [https://www.anthropic.com/engineering/claude-code-best-practices](https://www.anthropic.com/engineering/claude-code-best-practices)

我阅读了Anthropic Engineering网站上发表的“Claude Code：Agentic Coding最佳实践”一文，以下是摘要：

这篇文章概述了利用Claude作为agentic编码助手（即利用它自主执行复杂编码任务）的最佳实践。它强调，仔细的提示和结构化的交互对于获得最佳结果至关重要。

主要建议包括：

*   **详细的任务分解：** 将大型编码项目分解为更小、更易于管理的子任务。为每个子任务提供明确的指令，指定输入、输出和所需的功能。

*   **迭代改进：** 鼓励Claude以迭代方式工作。从基本实现开始，然后根据反馈和测试逐步改进。这有助于及早发现并纠正错误。

*   **上下文管理：** 维护清晰的对话历史记录，为Claude提供上下文。明确地提醒Claude之前的步骤、决定和目标，以防止它失去方向。

*   **代码审查和测试：** 始终审查和测试Claude生成的代码。这对于确保正确性、安全性以及符合编码标准至关重要。

*   **反馈和错误处理：** 当Claude犯错时，提供具体且可操作的反馈。鼓励它从错误中学习，并提高其未来的表现。使用调试技术并提供相关的错误消息。

*   **结构化输入/输出格式：** 使用JSON等结构化格式进行输入和输出，以改善沟通和数据处理。

*   **工具使用：** 通过提供明确的指令和示例，教Claude使用外部工具、库和API。

文章强调，遵循这些最佳实践可以显著提高Claude生成高质量代码的能力，减少错误，并简化软件开发流程。本质上，将Claude视为协作助手，为其提供清晰的指令、反馈和上下文，是最大化其潜力的关键。

---

## 73. 揭秘装饰器：它们不必晦涩难懂

**原文标题**: Demystifying decorators: They don't need to be cryptic

**原文链接**: [https://www.thepythoncodingstack.com/p/demystifying-python-decorators](https://www.thepythoncodingstack.com/p/demystifying-python-decorators)

本文是系列文章的第一篇，通过将概念分解为易于管理的部分，揭开了 Python 装饰器的神秘面纱。它首先介绍闭包，作为理解装饰器的基本构建块。

作者通过一个跟踪传递给 `print()` 函数的所有参数的例子来解释闭包。使用局部和全局变量的最初尝试被证明是不够的。解决方案是创建一个闭包：一个嵌套在外部函数中的内部函数。这个内部函数可以访问外部函数作用域（封闭作用域）中的变量，即使这些变量不是内部函数的局部变量。这允许在多次调用内部函数时保持数据持久性。

文章随后过渡到装饰器。外部函数 `print_with_memory()` 被重构为 `store_arguments()`，使其更通用，并适用于 `print()` 以外的函数。函数 `store_arguments()` 现在接受一个函数作为参数，并返回该函数的修改版本（内部函数）。

重构过程包括允许 `store_arguments()` 接受任何函数，而不仅仅是 `print()`。内部函数调用传入的函数（由 `func` 参数表示）。此外，还提到通常会在全局作用域中覆盖原始函数的名称。文章将在下一节对此进行进一步探讨。

---

## 74. 我本以为我买了一台相机，但实际上大疆卖给我的是它的使用许可 [视频]

**原文标题**: I thought I bought a camera, but no DJI sold me a license to use it [video]

**原文链接**: [https://www.youtube.com/watch?v=aUOnQ_boqCw](https://www.youtube.com/watch?v=aUOnQ_boqCw)

这个YouTube视频名为“我以为我买了一台相机，但DJI卖给我的只是使用许可”，可能探讨了与DJI相机产品相关的产权问题。标题表明创作者感觉他们购买的是相机的*使用*许可，而不是完全拥有它，暗示了对设备使用方式的潜在限制。

提供的YouTube页脚内容（“YouTube关于新闻版权联系我们创作者广告开发者条款隐私权政策与安全YouTube 的运作方式测试新功能NFL Sunday Ticket© 2025 Google LLC”）没有提供关于视频具体论点的直接见解。然而，包含这些内容突出了视频*在*YouTube上的存在，并将其与平台的条款、政策和服务联系起来。

在没有观看视频本身的情况下，无法准确指出创作者对许可问题的具体担忧原因。但是，潜在的问题可能包括：

*   **软件限制或约束：** 创作者可能担心DJI通过软件更新控制相机功能，或者需要订阅服务才能使用某些功能。
*   **使用权：** 创作者可能担心对拍摄的镜头或图像的使用方式的限制，尤其是在商业用途方面。
*   **数据隐私问题：** 创作者可能担心DJI收集和使用相机生成的数据。
*   **对DJI生态系统的依赖：** 创作者可能发现相机严重依赖DJI的软件和服务，实际上将他们锁定在DJI生态系统中。

该视频可能更深入地探讨这些或其它相关问题，认为用户对所购买相机的控制更像是许可协议，而不是完全所有权。

---

## 75. 使用 Linux 内核助我快速破解可执行文件

**原文标题**: Using the Linux kernel to help me crack an executable quickly

**原文链接**: [https://blog.maowtm.org/linux-ick/en.html](https://blog.maowtm.org/linux-ick/en.html)

通过修改Linux内核来自动化输入测试和内存恢复，破解混淆Linux可执行文件的独特方法。挑战在于一个程序能迅速判断提供的数字是否正确，正确则打印flag。由于程序初始化开销，传统的暴力破解方法太慢。

作者的解决方案是让内核直接操控目标进程，注入不同的输入数字，并在每次尝试后恢复程序的内存和寄存器状态。这消除了重复启动程序的需要，大幅加速了破解过程。

文章概述了所涉及的步骤：建立一个适合内核黑客的虚拟机环境，识别内核中的目标进程，修补`read`系统调用以注入猜测，以及`write`系统调用以触发状态恢复。它解决了诸如保存和恢复寄存器和内存、理解fork的工作原理、使用kgdb调试以及写保护内存页等挑战。作者通过修改内核来隐藏调试器的存在，从而绕过程序使用的反调试技术。通过trace-cmd和对系统调用时序的分析，性能得到了提高，重点关注输入和输出之间的短时间间隔。最终，这些修改将输入验证变成了一个极快的内核级循环。

---

## 76. Show HN: 我做了个服务器宕机短信提醒工具

**原文标题**: Show HN: I built a tool that texts you if your server goes down

**原文链接**: [https://www.yourserverisdown.com](https://www.yourserverisdown.com)

YourServerIsDown是一款服务器监控工具，可在服务器宕机时发送短信警报，旨在帮助企业避免因服务器停机而流失客户。该工具提供即时短信通知以便快速修复，防止销售损失和客户流失。它强调一个简单的工作流程：服务器故障触发短信，从而能够及时干预以避免危机并维持客户满意度。该服务拥有30秒快速设置的优势，并曾在FAZIER上得到推荐，荣获当日产品第三名。 简而言之，YourServerIsDown承诺提供一种快速有效的服务器正常运行时间监控方式，并在中断影响客户群之前做出响应。

---

## 77. 行星数学

**原文标题**: PlanetMath

**原文链接**: [https://planetmath.org/](https://planetmath.org/)

PlanetMath是一个协作式在线数学百科全书，旨在使数学知识更容易获取。其内容由成员根据知识共享署名-相同方式共享许可协议创建、编写和审查，从而保障所有贡献者的权利。条目用LaTeX编写，并使用LaTeXML渲染到网页上，NNexus将文章链接在一起。自2018年以来，源文件可以通过Github编辑，编辑会合并可接受的pull requests。PlanetMath已将传统的论坛过渡到针对每个数学主题类别的Gitter讨论频道，以鼓励实时讨论。该网站由滑铁卢大学数学学院托管，PlanetMath.org, Ltd.是一家位于弗吉尼亚州亚历山大市的501(c)3非营利组织。

---

## 78. OpenAI为何收购Windsurf？

**原文标题**: Why is OpenAI buying Windsurf?

**原文链接**: [https://theahura.substack.com/p/tech-things-openai-buys-windsurf](https://theahura.substack.com/p/tech-things-openai-buys-windsurf)

好的，我已阅读提供的URL中的文章《OpenAI为何收购Windsurf？》。以下是摘要：

该文章讨论了OpenAI收购Windsurf的事件，Windsurf是一家专注于*可观测性基础设施*的公司，特别是针对AI系统。作者认为此次收购的主要驱动力是OpenAI需要提高其*监控、调试和优化其日益复杂和大规模的AI模型及基础设施性能*的能力。

要点包括：

*   **可观测性对AI至关重要：** 随着AI模型变得越来越复杂，传统的监控方法已经不足。可观测性提供了对这些系统内部运作的更深入了解，从而可以更好地理解性能瓶颈、意外行为和潜在漏洞。

*   **解决AI基础设施复杂性：** OpenAI在管理其大规模计算基础设施以及AI模型中的复杂交互方面面临着重大挑战。Windsurf的技术可以通过提供对系统行为更全面的视图来帮助简化此过程。

*   **提高模型性能和可靠性：** 可观测性使OpenAI能够识别和解决可能影响其AI模型的准确性、速度或稳定性的问题。这对于维持用户信任并确保模型按预期运行至关重要。

*   **OpenAI API开发者的潜在利益：** 这次收购还可以通过为开发人员提供更好的工具来排除故障和优化他们的应用程序，从而改善在OpenAI平台上构建应用程序的开发人员的体验。

*   **竞争优势：** 通过投资可观测性，OpenAI正在定位自己，以在快速发展的AI领域保持竞争优势。增强的基础设施可以实现更快的迭代、更大的可扩展性和更可靠的AI服务。

本质上，作者认为收购Windsurf是OpenAI加强其AI基础设施、提高模型性能并最终提供更可靠和有效的AI解决方案的战略举措。这次收购与其说是收购某个特定产品，不如说是收购AI未来关键领域的专业知识和人才。

---

## 79. Show HN: Undercutf1 – 带有车手追踪和可变延迟的F1实时数据TUI界面

**原文标题**: Show HN: Undercutf1 – F1 Live Timing TUI with Driver Tracker, Variable Delay

**原文链接**: [https://github.com/JustAman62/undercut-f1](https://github.com/JustAman62/undercut-f1)

UndercutF1 是一款开源的、基于终端 (TUI) 的应用程序，用于查看一级方程式赛车的实时数据，其灵感来自 FastF1。它允许用户监控实时比赛数据、回放过去的比赛，并分析车手表现。

主要功能包括：实时计时塔，显示分段用时、轮胎信息和差距；进站策略概览；赛事控制消息；以及赛道地图上的车手追踪器（兼容 iTerm2 和 Kitty Graphics Protocol）。用户还可以查看逐圈计时历史记录，并使用本地 Whisper ML 模型收听/转录车队无线电。

该应用程序允许调整延迟，以与直播同步。数据会被记录下来，以便在 `~/undercut-f1/data/<session-name>` 中进行回放，包括 `live.txt` 和 `subscribe.txt`。用户可以使用 `undercutf1 import` 命令导入历史 F1 数据。

安装选项包括：将其安装为 .NET 工具、使用独立可执行文件（可在 GitHub 发布页面上找到）、使用 Docker 运行（需要挂载卷以存储数据）或直接从源代码运行。可以通过 `config.json` 文件、命令行参数或环境变量进行配置，以控制数据目录、详细程度、API 和通知。日志存储在内存中（可通过 TUI 访问）和文件中。

---

## 80. 安卓手机闲置三天后将自动重启

**原文标题**: Android phones will soon reboot themselves after sitting unused for three days

**原文链接**: [https://arstechnica.com/gadgets/2025/04/android-phones-will-soon-reboot-themselves-after-sitting-unused-for-3-days/](https://arstechnica.com/gadgets/2025/04/android-phones-will-soon-reboot-themselves-after-sitting-unused-for-3-days/)

本文详细介绍了一项新的 Google Play 服务更新 (v25.14)，该更新将在 Android 手机锁定后三天无活动时自动重启，从而增强设备安全性。 此更新已于 4 月 14 日发布，但正在逐步推出，旨在通过确保手机保持在更安全、加密的“首次解锁前” (BFU) 状态来保护个人数据。

在 BFU 状态下，生物识别和基于位置的解锁将被禁用，需要密码或 PIN 码才能访问。 至关重要的是，所有数据仍然加密，即使使用高级数据恢复工具也难以提取。 此功能类似于 Apple iPhone 上的“不活动重启”功能，该功能让执法部门感到沮丧。

此更新不需要用户操作，并且会以静默方式出现在 Android 设备上，绕过传统的系统更新过程。 谷歌通过 Play 服务推送安全增强功能的能力突显了其对 Android 生态系统日益增强的控制，从而可以快速向庞大的用户群部署安全性。 尽管谷歌的影响力引发了担忧，但这项特定更新直接解决了与长时间不活动相关的安全漏洞，最大限度地减少了未经授权访问数据的机会。

---

## 81. 一日三罪 (2013)

**原文标题**: Three Felonies a Day (2013)

**原文链接**: [https://kottke.org/13/06/you-commit-three-felonies-a-day](https://kottke.org/13/06/you-commit-three-felonies-a-day)

本文讨论了哈维·西尔弗格莱特的著作《一天三项重罪》，该书认为美国联邦刑法的巨大扩张和模糊性使得普通公民极有可能在不知情的情况下每天犯下多项重罪。西尔弗格莱特认为，这种过度扩张赋予了检察官过大的权力，可以针对他们不喜欢的人，无论其社会阶层或职业。

本文以QWest前首席执行官约瑟夫·P·纳乔的案件为例。约翰·吉尔莫声称，纳乔在拒绝遵守美国国家安全局窃听QWest所有客户的要求后，因内幕交易而被盯上并被监禁。本文暗示，纳乔的起诉是对他拒绝的回应，表明政府如何利用模糊的法律来惩罚那些抵制其要求的人。

文章认为，过于宽泛的刑法和广泛的政府监控相结合，构成了一个政府可以轻易指控任何美国公民犯下重罪的体系。文章最后表达了对个人自由和宪政民主的影响的担忧。更新提到《华尔街日报》也在调查不断扩张的联邦刑法。

---

## 82. 为了让语言模型更好地工作，研究人员避开了语言本身

**原文标题**: To Make Language Models Work Better, Researchers Sidestep Language

**原文链接**: [https://www.quantamagazine.org/to-make-language-models-work-better-researchers-sidestep-language-20250414/](https://www.quantamagazine.org/to-make-language-models-work-better-researchers-sidestep-language-20250414/)

文章《研究人员绕过语言，让语言模型更好地工作》探讨了研究人员如何通过使大型语言模型（LLM）能够在“潜在空间”（一种信息的数学表示）中进行推理，而不是不断地将概念转换为语言和从语言转换，来改进它们。

传统的LLM将文本转换为数值嵌入，执行数学运算，然后将结果转换回文本标记，这在计算上是昂贵的，并且可能导致信息丢失。研究人员正在探索使模型在潜在空间中保持更长时间推理的方法，从而绕过不断翻译成语言的需要。

文章重点介绍了两种方法：
1. **Coconut (郝世博团队):** 该模型将隐藏状态（最终的嵌入集）直接循环回输入，允许在生成文本之前进行连续的数学处理。 与标准GPT-2相比，Coconut在某些逻辑推理任务上证明了更高效和准确。
2. **Tom Goldstein团队的LLM:** 该模型使用一个可以多次使用的“循环块”层，有效地按需增加模型的深度。 该模型学会了为更复杂的任务分配更多的计算资源（更多次通过循环块），并且是从头开始训练的。 在编码和数学推理等任务上，它优于更大的模型。

虽然前景广阔，但文章指出，由于对传统LLM架构的现有投资，潜在空间推理可能不会很快被采用。 同时也存在这样的担忧：在没有语言的情况下进行推理可能会导致模型以与人类理解不一致的方式进行思考。 尽管存在这些保留意见，但该研究标志着人工智能推理和问题解决的一个潜在的变革方向。

---

## 83. 网络已毁 – 僵尸网络（第二部分）

**原文标题**: The Web Is Broken – Botnet Part 2

**原文链接**: [https://jan.wildeboer.net/2025/04/Web-is-Broken-Botnet-Part-2/](https://jan.wildeboer.net/2025/04/Web-is-Broken-Botnet-Part-2/)

AI模型训练数据需求催生的僵尸网络问题日益严重。作者指出，一种令人担忧的趋势是，公司招募应用程序开发者将“网络共享”SDK集成到其应用中，从而有效地创建僵尸网络。这些SDK将用户的网络带宽出售给客户，而这些客户又将其用于网络抓取、暴力破解和其他恶意活动。

作者以Infatica等公司为例，说明了这种阴暗的市场，应用开发者通过包含这些SDK来获得报酬，这些SDK会将用户变成这些僵尸网络不知情的参与者。作者认为，这种做法导致了许多网站管理员由于激进的AI爬虫而遭受的DDoS攻击。

文章引用了趋势科技的一项研究，该研究支持了这些怀疑，并强调了普通用户和网站管理员难以检测到这些隐藏的SDK及其产生的网络流量。作者主张苹果、微软和谷歌等平台采取行动反对这种做法，称其为恶意软件分发。

最后，作者认为，由于这些公司的行为以及AI炒作的影响，所有形式的网络抓取都应被视为滥用行为。作者敦促网站管理员阻止抓取，并希望提高人们对这一问题的认识及其对网络的破坏性影响。

---

## 84. 一百年解一道积分题 (2020)

**原文标题**: 100 Years to Solve an Integral (2020)

**原文链接**: [https://liorsinai.github.io/mathematics/2020/08/27/secant-mercator.html](https://liorsinai.github.io/mathematics/2020/08/27/secant-mercator.html)

利奥尔·西奈的文章《解开一个积分用了一百年》探讨了正割函数积分的历史及其与墨卡托投影地图的联系。该积分最初由杰拉杜斯·墨卡托在1569年为地图制作提出，但其精确解近一个世纪以来一直难以捉摸。文章将历史背景与数学概念联系起来，需要读者熟悉代数、三角学和基础微积分。

文章解释了积分与墨卡托地图的相关性，该地图保留了角度以供导航。它详细介绍了墨卡托投影的构建，解释了它如何在南北方向上拉伸地图以保持形状，这对于沿恒向线的精确方位测量至关重要。墨卡托近似计算了每个纬度的拉伸因子以创建他的地图。

文章还强调了计算器时代之前数学表格的重要性。爱德华·赖特在1599年发表了墨卡托地图方程的表格，约翰·纳皮尔在1614年引入了对数。作者指出，积分的解是以一种偶然的方式被发现的，并非通过标准微积分，而是一位教师在这些数学表格的背景下进行数值计算时发现的，这展示了一种独特的数学发现方法。文章强调，突破常常来自意想不到的地方，数学史充满了以看似不寻常的方式发现的见解。

---

## 85. 如何从零开始用张量核心编写快速矩阵乘法 (2024)

**原文标题**: How to Write a Fast Matrix Multiplication from Scratch with Tensor Cores (2024)

**原文链接**: [https://alexarmbr.github.io/2024/08/10/How-To-Write-A-Fast-Matrix-Multiplication-From-Scratch-With-Tensor-Cores.html](https://alexarmbr.github.io/2024/08/10/How-To-Write-A-Fast-Matrix-Multiplication-From-Scratch-With-Tensor-Cores.html)

本文详细介绍了作者在 NVIDIA Tesla T4 GPU 上使用 Tensor Cores 优化矩阵乘法内核（HGEMM）的历程，旨在接近 NVIDIA cuBLAS 实现的性能。核心挑战是最大化 Tensor Core 的利用率，这需要高效的内存管理和计算与数据移动的重叠，以应对内存墙问题。

作者引入了屋顶线模型作为理解性能瓶颈的工具，对比了内存带宽和峰值浮点吞吐量。他们强调了相比标准数学单元 (FFMA)，高效利用 Tensor Core 需要更高的算术强度。文章强调了利用 GPU 的内存层次结构（共享内存、L2 缓存、全局内存）来克服带宽限制的重要性。

作者迭代优化了六个内核。这些优化涉及分层分块、向量化内存复制、循环展开、共享内存交错（以避免 bank conflicts）、异步内存复制和调整分块尺寸等技术。后期的优化提高了 L2 缓存的局部性并减少了索引计算。最终，最终内核在 8192x8192 矩阵上实现了 cuBLAS 吞吐量的 96%。作者指出，更新的 GPU（如 Hopper）包含硬件功能，可以简化在 Turing 等较旧架构上所需的一些优化。不同内核的代码可在 GitHub 上找到。

---

## 86. 秘鲁古老的灌溉系统因文化将沙漠变成了农田。

**原文标题**: Peru's ancient irrigation systems turned deserts into farms because of culture

**原文链接**: [https://theconversation.com/perus-ancient-irrigation-systems-succeeded-in-turning-deserts-into-farms-because-of-the-culture-without-it-the-systems-failed-251199](https://theconversation.com/perus-ancient-irrigation-systems-succeeded-in-turning-deserts-into-farms-because-of-the-culture-without-it-the-systems-failed-251199)

本文探讨了古代秘鲁灌溉系统将沙漠转化为肥沃农田的成功之处，并将其与现代农业工业实践的困境进行了对比。作者认为，莫奇和奇穆文化在西班牙殖民前的灌溉系统之所以成功，不仅在于其基础设施，更在于其技术与文化深度融合，包括他们的信仰、行为和劳动制度。这些系统优先考虑高效用水，结合洪水改道，并促进多功能性，从而创造了一个适应该地区极端环境的弹性农业系统。

相比之下，西班牙殖民者和现代农业工业的方法，虽然也使用类似的运河技术，但往往由于缺乏对古代系统有效性的文化背景的理解而失败。作者批评了当前秘鲁政府对大型项目的关注，例如查维莫奇克项目，该项目依赖于日渐减少的冰川融水，并忽视了土著社区开发的可持续土地管理实践。这些项目可能提供短期收益，但存在长期脆弱性的风险。

文章总结认为，为了使现代气候适应工作取得成功，不仅要考虑古代解决方案的技术方面，还要考虑使这些解决方案能够繁荣数千年的文化知识，包括土著语言和考古遗址的保护。理解和整合这些文化因素对于在秘鲁和其他地方建设真正具有气候韧性的未来至关重要。

---

## 87. 大家都知道你的位置，第二部分：亲自尝试并分享结果

**原文标题**: Everyone knows your location, Part 2: try it yourself and share the results

**原文链接**: [https://timsh.org/everyone-knows-your-location-part-2-try-it-yourself/](https://timsh.org/everyone-knows-your-location-part-2-try-it-yourself/)

本文是关于应用位置数据共享的先前文章的后续。作者分享了一个指南和一个Python笔记本，以帮助其他人分析应用流量的数据收集行为。目标是众包关于哪些应用收集和共享哪些数据的信息。

作者提供了一个TL;DR：一个包含指南和Python笔记本的GitHub仓库，用于记录和分析移动应用流量（初始设置：10-30分钟，分析：约10分钟/应用）。提供了一个Google表格，用户可以在其中查看是否有人分析过某个应用，记录他们的发现，并填写一份详细说明有趣数据点的表格。作者鼓励读者手动检查应用流量，以避免盲目信任在线表格。

文章包括跨应用流量的广告技术域名使用情况的可视化，突出了Unity的优势。提供了一个使用mitmproxy拦截应用流量并使用提供的Python笔记本分析数据的分步指南。该笔记本可以帮助根据“IP”、“geo”、“IDFA”等关键字过滤请求，并允许用户检查匹配的请求/响应。

作者承认分析的原始性，并强调手动审查的重要性。文章最后呼吁大家分析应用并为众包工作做出贡献。关于Apple的gs-loc端点及其对用户隐私的影响的简短讨论结束了这篇文章，暗示了后续文章。

---

## 88. 硅谷人行道按钮疑似遭黑客入侵，模仿马斯克、扎克伯格声音

**原文标题**: Silicon Valley crosswalk buttons apparently hacked to imitate Musk, Zuck voices

**原文链接**: [https://www.paloaltoonline.com/technology/2025/04/12/silicon-valley-crosswalk-buttons-apparently-hacked-to-imitate-musk-zuckerberg-voices/](https://www.paloaltoonline.com/technology/2025/04/12/silicon-valley-crosswalk-buttons-apparently-hacked-to-imitate-musk-zuckerberg-voices/)

红木城、门洛帕克和帕洛阿托人行横道按钮近期遭黑客入侵，播放冒充马克·扎克伯格和埃隆·马斯克的语音。网上流传的视频显示，模仿的声音传递着信息，扎克伯格的模仿者讨论人工智能整合，而马斯克的模仿者则发表古怪言论。

受影响的城市和加州交通运输部已采取行动禁用语音播报功能，并正在努力修复系统。帕洛阿托禁用了12个路口的语音功能，而红木城则在四个地点禁用了未经授权的消息。门洛帕克人行横道由州政府运营，加州交通运输部已停用音频。所有地点现在都依靠计时器运行。

市政府官员提醒公众，篡改城市基础设施是违法的，并且存在安全风险。

---

## 89. 使用单个进程服务网页的吸引力

**原文标题**: The appeal of serving your web pages with a single process

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/web/SingleProcessServingAppeal](https://utcc.utoronto.ca/~cks/space/blog/web/SingleProcessServingAppeal)

克里斯·西本曼的博客“漫游思绪”正在实施反爬虫措施，以应对大量高流量爬虫的涌入，尤其是那些使用过时浏览器用户代理（特别是旧版Chrome）收集数据用于LLM训练的爬虫。这些爬虫正在给网站造成显著的负载。

如果您看到此页面，您可能正在使用一个过时的浏览器，该浏览器已被反爬虫系统标记为可疑。如果这是一个错误，并且您正在使用最新的浏览器，您可以通过他的大学邮箱地址联系作者，并提供您的浏览器详细信息（尤其是User-Agent字符串）。

作者还对诸如archive.today、archive.ph和archive.is等存档服务的用户发表了看法。这些存档服务存在问题，因为它们的爬取行为与恶意机器人无法区分。它们使用旧的Chrome User-Agent值，从广泛分布且未明确识别的IP地址爬取，有时还会使用伪造的反向DNS条目来模仿Googlebot IP地址。西本曼建议改用archive.org，因为它是一个行为更好的存档爬虫。

---

## 90. 物种倾源

**原文标题**: The Pour-igin of Species

**原文链接**: [https://pudding.cool/2025/04/wine-animals/](https://pudding.cool/2025/04/wine-animals/)

物种“倾”源：葡萄酒标签动物与价格评分趣味分析

---

## 91. Eccfrog512ck2：一种增强型512位Weierstrass椭圆曲线[pdf]

**原文标题**: Eccfrog512ck2: An Enhanced 512-Bit Weierstrass Elliptic Curve [pdf]

**原文链接**: [https://arxiv.org/abs/2504.09584](https://arxiv.org/abs/2504.09584)

这篇于2025年4月13日提交的arXiv文章介绍了Eccfrog512ck2，一种新的512位Weierstrass椭圆曲线，其设计旨在提供比NIST P-521更高的安全性和性能。该论文由Víctor Duarte Melo和William J. Buchanan撰写，认为虽然NIST P256和secp256k1提供128位安全性，NIST P-521、Curve 448和Brainpool-P512提供256位安全性，但仍有改进的需求。

Eccfrog512ck2旨在填补这一空白，在提供256位安全性的同时，拥有比NIST P-521更快的性能。作者声称Eccfrog512ck2具有抗侧信道攻击能力，并且在设计上避免了MOV攻击等弱点。在性能方面，该论文表明，与NIST P-521相比，标量乘法速度提高了61.5%，点生成速度提高了33.3%。该论文属于计算机科学领域的“密码学与安全”类别。

---

## 92. 汇编语言艺术 (2010)

**原文标题**: The Art of Assembly Language (2010)

**原文链接**: [https://www.plantation-productions.com/Webster/www.artofasm.com/Linux/HTML/AoATOC.html](https://www.plantation-productions.com/Webster/www.artofasm.com/Linux/HTML/AoATOC.html)

汇编语言艺术 (2010)：一本使用高级汇编语言(HLA)的汇编语言编程综合指南。本书涵盖广泛的主题，从基本概念开始，逐步过渡到高级主题。

最初，它介绍了HLA，其在Windows和Linux上的安装，程序结构，数据声明和基本控制结构。然后，它深入研究了计算机科学的基础概念，例如数字系统，数据组织（位，字节，字），十六进制，算术运算和逻辑运算。

本书探讨了数据表示形式，包括浮点数，BCD，ASCII，UNICODE和其他多媒体数据格式。它涵盖了系统架构，寻址方式，内存组织，堆栈和堆管理以及布尔代数。详细检查了CPU设计，指令集架构，内存层次结构（缓存，虚拟内存）和I / O机制（中断，DMA）。

高级主题包括复合数据类型，如字符串，字符集，数组，记录，联合以及日期/时间处理。还讨论了过程，程序组织（单元，包含，makefile）和库。本书解释了80x86整数和浮点算术指令，并强调了优化技术和HLA标准库。还涵盖了使用TRY..ENDTRY块的异常处理。

---

## 93. Xilinx ISE 安装程序在说谎

**原文标题**: The Xilinx ISE Installer Lies

**原文链接**: [https://stefanabikaram.com/writing/xilinx-ise-installer/](https://stefanabikaram.com/writing/xilinx-ise-installer/)

作者详细描述了其优化 Xilinx ISE 安装程序（一个 6.1 GB 的大型 tar 文件）的令人沮丧的经历，目的是为了更轻松地创建 Docker 镜像并在 GitHub 上托管。核心问题是安装程序的大小，这使得 Docker 镜像构建速度缓慢，并且需要拆分文件以进行 GitHub 存储。

最初尝试使用 gzip 压缩 tar 文件失败。深入研究后，作者发现安装程序包含许多 `.zip.xz` 文件。对看似多余的压缩感到好奇，他们假设 Xilinx 可能没有使用最高的压缩设置。

作者随后意识到这些 `.zip.xz` 文件实际上是受密码保护的 7zip 文件。找到密码后，他们计划提取并使用更高的压缩设置重新压缩这些 7zip 档案，旨在减小整个安装程序的大小。

由于空间限制，最初尝试在磁盘上重新压缩文件失败。随后尝试使用 Python 在内存中完成所有操作导致笔记本电脑因内存不足而崩溃。初步结果显示，某些文件产生了较小的压缩改进（高达 6%）。

尽管遭遇了这些挫折，作者仍然决心减小安装程序的大小，考虑探索基于 Rust 的 7zip 库，以实现潜在的 zstd 压缩和更高的性能。作者总结说，即使是像安装程序这样简单的东西，Xilinx 的软件仍然令人惊讶地存在问题。

---

## 94. ChatGPT 等是否正在损害人类智能？

**原文标题**: Are ChatGPT and co harming human intelligence?

**原文链接**: [https://www.theguardian.com/technology/2025/apr/19/dont-ask-what-ai-can-do-for-us-ask-what-it-is-doing-to-us-are-chatgpt-and-co-harming-human-intelligence](https://www.theguardian.com/technology/2025/apr/19/dont-ask-what-ai-can-do-for-us-ask-what-it-is-doing-to-us-are-chatgpt-and-co-harming-human-intelligence)

人工智能对人类智能的潜在负面影响：批判性思维和创造力面临的挑战

---

## 95. 是时候应对耐药性真菌感染了

**原文标题**: High time to tackle drug-resistant fungal infections

**原文链接**: [https://www.nature.com/articles/d41586-025-01177-x](https://www.nature.com/articles/d41586-025-01177-x)

自然文章强调耐药性真菌感染（尤其是耳念珠菌）日益增长的威胁，以及采取行动的紧迫性。真菌感染导致全球死亡人数不断增加，但在抗菌素耐药性讨论中却往往被忽视。文章强调，后期研发中的新型抗真菌药物匮乏，并呼吁增加对研究、政策变革和协作努力的投资。

主要挑战包括真菌感染诊断的困难，尤其是在中低收入国家，以及由于真菌细胞与人类细胞的相似性而导致开发抗真菌药物的内在困难。文章提倡对真菌遗传学和细胞通路进行基础研究，以识别潜在的药物靶点，并改进对新兴耐药菌株的检测。文章还建议建立临床试验网络，以促进新疗法的开发。

一个重要的担忧是农业杀菌剂的使用可能导致感染人类的真菌产生耐药性。文章呼吁采取多方利益相关者参与的方法来解决这个问题，建议采取诸如禁止在植物保护中使用某些抗生素，以及在杀菌剂评估中纳入耐药性风险等措施。这篇文章还强调了杀菌剂的使用对唑类药物（用于治疗曲霉菌感染的一类药物）构成的威胁。最终，文章敦促行业、政府和慈善基金提供者进行合作，并提供必要的资源来解决开放的研究问题，并对抗新兴的耐药性真菌威胁。

---

## 96. 感觉编码不是低质量工作的借口

**原文标题**: Vibe Coding is not an excuse for low-quality work

**原文链接**: [https://addyo.substack.com/p/vibe-coding-is-not-an-excuse-for](https://addyo.substack.com/p/vibe-coding-is-not-an-excuse-for)

好的，我已阅读提供的URL中的文章。以下是摘要：

文章《氛围编程不是低质量工作的借口》探讨了开发者使用“氛围编程”为产生不合格代码辩解的日益增长的趋势。作者Addy Osmani认为，虽然创造力和直觉理解（即“氛围”）在软件开发中可能有所帮助，但绝不应该用它们来代替基本的软件工程原则和最佳实践。

核心观点是，“氛围编程”，被定义为仅仅依赖感觉和直觉，而缺乏适当的计划、测试或文档，通常会导致脆弱、难以维护且充满错误的代码。Osmani强调了通过以下技术构建健壮且结构良好的软件的重要性：

*   **测试:** 编写单元测试和集成测试以确保代码正确性。
*   **文档:** 清楚地记录代码，以便未来的维护和理解。
*   **计划与设计:** 花时间正确设计和规划软件架构。
*   **代码审查:** 让同行审查代码，以发现潜在问题并提高质量。
*   **遵循最佳实践:** 遵循既定的编码标准和设计模式。

Osmani承认，有时快速原型设计或探索可能涉及更多“氛围驱动”的方法，但强调这之后必须进行重构和严格应用软件工程原则，以创建可用于生产的产品。他最后敦促开发者拥抱创造力和纪律，确保“氛围”能够增强而非取代可靠的工程实践。“氛围编程”绝不应成为交付低质量软件的借口。

---

## 97. 介于生死之间的动物

**原文标题**: The Animals That Exist Between Life and Death

**原文链接**: [https://nautil.us/the-animals-that-exist-between-life-and-death-1202592/](https://nautil.us/the-animals-that-exist-between-life-and-death-1202592/)

这篇《鹦鹉螺》杂志的文章探讨了动物（尤其是轮虫）通过脱水似乎能在“生死之间”存在的哲学和科学意义。文章从安东尼·范·列文虎克发现轮虫及其在干燥后复苏的能力开始，挑战了传统对生死二元对立的理解。

文章详细描述了这些生物进入一种被称为“隐生”的状态，大卫·凯林将其定义为一种没有明显生命迹象且无法检测到代谢活动的状态。在脱水过程中，轮虫收缩成“tun”或“xerosome”，并采用独特的生存机制，如LEA蛋白，它可以取代细胞中的水分并防止膜塌陷，而不是其他极端微生物使用的海藻糖。

这个过程并非没有后果；轮虫在脱水过程中会经历显著的DNA损伤，需要在补水后进行高级DNA修复。有趣的是，轮虫已经整合了来自真菌、植物和酵母的外源DNA，这些DNA在它们的脱水生存中发挥作用。这种基因异常引发了关于事件顺序的问题：是生存脱水的能力导致了外源DNA的整合，还是反之亦然？

文章总结说，轮虫似乎能够“死而复生”的能力继续困扰着科学家和哲学家，这表明简单的生死二元对立未能完全捕捉到这些独特生物的复杂现实。它们修复DNA和整合外源遗传物质的能力进一步突显了它们非凡而神秘的存在。

---

## 98. 体验时代欢迎您 [pdf]

**原文标题**: Welcome to the Era of Experience [pdf]

**原文链接**: [https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf](https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf)

此文档似乎是名为“欢迎来到体验时代”的PDF文件的代码。由于文件格式为原始代码，并且存在大量非人类可读字符和压缩技术（FlateDecode），因此无法提取有意义的文本内容或关于文档目的和体验主题的上下文，所以我无法总结这篇文章。

---

## 99. 航空旅行规划的计算复杂度 [pdf] (2003)

**原文标题**: Computational Complexity of Air Travel Planning [pdf] (2003)

**原文链接**: [http://www.demarcken.org/carl/papers/ITA-software-travel-complexity/ITA-software-travel-complexity.pdf](http://www.demarcken.org/carl/papers/ITA-software-travel-complexity/ITA-software-travel-complexity.pdf)

基于标题“航空旅行规划的计算复杂度”和PDF内容（虽然无法直接阅读），我们可以推断该文章可能探讨了使用计算机解决航空旅行规划问题所固有的难度。“计算复杂度”指的是随着问题规模增长，解决问题所需的资源（时间、内存）。

该文章可能探索航空旅行规划问题的不同表达形式，例如寻找最便宜的路线、最小化旅行时间，或考虑各种约束，如中转时间、航空公司联盟和机票可用性。它可能从理论计算机科学的角度分析这些问题，试图将它们归类到诸如P（可在多项式时间内解决的问题）或NP-hard（可能无法在多项式时间内解决的问题）之类的复杂度类中。

由于现实世界航空旅行规划中涉及的众多约束和变量，文章很可能证明了许多现实版本的该问题都是NP-hard。这意味着寻找大规模航空旅行规划的最优解在计算上是难处理的，这为旅游网站和航空公司使用的近似算法和启发式方法提供了理由。发表年份（2003年）表明，该文章提供了与更复杂的航空旅行规划工具的持续开发相关的基础分析。

---

## 100. 谷歌人...前谷歌人

**原文标题**: Googler... ex-Googler

**原文链接**: [https://nerdy.dev/ex-googler](https://nerdy.dev/ex-googler)

前谷歌员工亚当·阿盖尔讲述了他突然且意外的裁员经历。他对在Chrome团队被突然解雇感到震惊、悲伤和愤怒。尽管他被告知裁员并非基于绩效，并且可以寻找其他职位，但他立即被切断了所有Google系统，包括电子邮件、文档和代码，这让他感到被背叛和不受欢迎。

他强调了讽刺的时间点，因为当时他正在积极参与Chrome团队的团建活动，集思广益改进开发者使用的网络。阿盖尔详细描述了他现在失去的众多责任和机会，包括Google I/O视频录制、舞台亮相、运营展位、为开发者主题演讲做贡献、CSS工作组成员资格、开发者办公时间、代码访问权限以及各种CSS项目。

他感叹失去了多年来建立的关系，并表示感觉自己像一个大型企业中可有可无的“齿轮”。他分享了他的失眠、羞愧和沮丧之感。他邀请那些希望联系他的人通过Bluesky或他的个人电子邮件地址联系他，同时也承认由于情况的复杂性，他可能会回复较慢。最后，他强调了事件带来的痛苦和情感冲击。

---

