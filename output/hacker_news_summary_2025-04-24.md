# Hacker News 热门文章摘要 (2025-04-24)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 为何21厘米是我们宇宙的“神奇长度”

**原文标题**: Why 21 cm is our Universe's "magic length"

**原文链接**: [https://bigthink.com/starts-with-a-bang/21cm-magic-length/](https://bigthink.com/starts-with-a-bang/21cm-magic-length/)

为何氢的21厘米波长是宇宙中的“魔力长度”

---

## 2. 我写信给GPLv2许可声明中的地址（2022）。

**原文标题**: I wrote to the address in the GPLv2 license notice (2022)

**原文链接**: [https://code.mendhak.com/gpl-v2-address-letter/](https://code.mendhak.com/gpl-v2-address-letter/)

2022年，作者对GPLv2许可证声明中的物理地址感到好奇，决定写信给位于波士顿富兰克林街51号的自由软件基金会（FSF），想看看会发生什么。考虑到在线访问GPLv2的便利性，他们很好奇为什么使用物理地址而不是URL。

从Stack Exchange了解到该地址很可能存在是因为1991年GPLv2发布时互联网访问受限后，作者开始了一场寄信之旅。这包括从eBay上购买美国邮票，使他们短暂地陷入了集邮及其相关术语的兔子洞。

作者准备了一封信，附带一个写好地址的回邮信封和一张美国邮票。几周后，他们收到了来自FSF的回信，信中包含了完整的许可证文本。然而，回复的却是印在美式信纸上的GPLv3，而不是所请求的GPLv2。

虽然作者意识到自己没有明确要求GPLv2，但他们想知道许可证声明中地址的存在是否应该足以作为线索。最终，他们决定不再跟进以获取正确的版本，并对这个意想不到的结果和经历感到满意。他们以一句玩笑话结束，声称在这次邮寄探险之后需要休息一下。

---

## 3. SIMD ISA 的三大根本缺陷 (2023)

**原文标题**: Three Fundamental Flaws of SIMD ISAs (2023)

**原文链接**: [https://www.bitsnbites.eu/three-fundamental-flaws-of-simd/](https://www.bitsnbites.eu/three-fundamental-flaws-of-simd/)

本文批判了现代CPU中常见的紧凑型SIMD ISA（单指令多数据流），并指出了三个根本缺陷。

**缺陷1：固定寄存器宽度：** SIMD的固定寄存器大小需要新的指令和寄存器才能扩展到更高的硬件并行性（例如，MMX、SSE、AVX）。 这需要ABI更新、操作系统内核、编译器和调试器的支持，导致操作码耗尽、指令长度增加以及每代软件重写。 先前的SIMD代数在很大程度上变得冗余，浪费了指令。

**缺陷2：流水线：** SIMD操作通常采用流水线方式，需要多个时钟周期。 这意味着一条SIMD指令的结果不能立即获得，需要循环展开以避免停顿。 循环展开增加了代码大小（损害了指令缓存性能）和寄存器压力。

**缺陷3：尾部处理：** 当数组元素的数量不是SIMD寄存器大小的倍数时，需要额外的代码来处理数组的“尾部”。 这涉及到增加控制逻辑和可能的标量指令，从而增加代码复杂性和开销，对指令缓存效率产生负面影响。

本文将紧凑型SIMD与向量处理器进行了对比，向量处理器通过在硬件中处理展开和尾部操作来解决这些缺陷。文中提供了MRISC32、RISC-V RVV、ARM SVE 和 My 66000 的实现示例，以展示这些替代架构如何更有效地执行 "saxpy" 例程。 总之，本文提倡将向量处理器作为紧凑型 SIMD ISA 的更好替代方案。

---

## 4. DuckDB UI 中输入时即时 SQL 结果

**原文标题**: Instant SQL for results as you type in DuckDB UI

**原文链接**: [https://motherduck.com/blog/introducing-instant-sql/](https://motherduck.com/blog/introducing-instant-sql/)

本文宣布推出 Instant SQL，这是 MotherDuck 和 DuckDB Local UI 中的一项新功能，旨在通过在您键入时提供实时结果预览，来加速 SQL 查询的构建和调试。

Instant SQL 旨在解决编写 SQL 时缓慢而繁琐的过程，传统上用户需要迭代地编写、运行、等待和修复查询。它提供以下功能：

*   **实时结果集预览：** 随着您的键入更新结果，从而实现即时反馈和更流畅的分析流程。
*   **CTEs 检查：** 允许您通过点击并立即查看结果来快速可视化和调试 CTE（公共表表达式），从而节省数小时的调试时间。
*   **复杂列表达式分解：** 允许您剖析列表达式，通过即时反映每次编辑的数据流来识别逻辑或数据中的问题。
*   **多功能查询：** 适用于 DuckDB 表、MotherDuck 数据、外部文件（Parquet、S3）以及 DuckDB 支持的其他数据库系统。
*   **更快的实验：** 可以自由测试和改进查询逻辑，而无需等待，只有在对最终结果满意时才运行。
*   **AI 集成：** 通过显示实时结果集应用来补充 AI 驱动的编辑建议，从而消除猜测。

本文重点介绍了实现 Instant SQL 所需的技术

---

## 5. 查询数据的原则性方法——类型安全的搜索DSL

**原文标题**: A Principled Approach to Querying Data – A Type-Safe Search DSL

**原文链接**: [https://www.claudiu-ivan.com/writing/search-dsl](https://www.claudiu-ivan.com/writing/search-dsl)

本文介绍了一种构建类型安全搜索系统的原则性方法，该方法使用领域特定语言（DSL），尤其适用于本地优先的Web应用程序，但也适用于服务器端系统。该DSL允许用户使用熟悉的领域术语表达搜索意图，从而提供可控的复杂性、领域对齐和增强的可用性。

该系统围绕搜索“问题”展开，问题由TypeScript接口定义。使用`Either`类型表示解析操作的成功或失败，实现了强大的错误处理。解析器组合子，一种函数式编程技术，被用于以模块化和可组合的方式构建解析器。这些组合子解析输入字符串并生成抽象语法树（AST），一种查询的结构化表示，它将语法与评估分离。

然后，AST被转换为谓词函数，该函数根据查询过滤数据集。本文包括解析器、AST节点定义、谓词函数和执行函数的代码示例。

对包含100万个问题的模拟数据集的性能评估表明，性能可以接受，但本文承认线性扫描的局限性，并强调了索引对于更大数据集的必要性。为了提高可扩展性，建议采用查询优化、查询计划和在各个级别（解析的查询、谓词和查询结果）缓存等优化策略。

文章最后强调了类型安全、函数式编程和关注点分离在创建健壮、可维护和可扩展的搜索系统中的优势。

---

## 6. 对雇主的忠诚

**原文标题**: On loyalty to Your Employer

**原文链接**: [https://www.talentstuff.com/blog/on-loyalty-to-your-employer](https://www.talentstuff.com/blog/on-loyalty-to-your-employer)

史蒂薇·巴克利的《关于忠于你的雇主》一文挑战了盲目忠诚的观念，这种观念在科技行业尤为盛行，而科技行业跳槽现象十分普遍。巴克利是一位招聘人员，她受到父亲在同一家公司工作30年的经历启发，质疑了LinkedIn上常见的雇主赞扬的真诚性。

她概述了评估潜在雇主的四个关键标准：合理的薪资、善待员工（通过Glassdoor和社交媒体验证）、财务安全（通过公共记录和直接询问“跑道”来评估）以及对新想法的开放性（这在她担任招聘职位时尤为重要）。满足这些标准使她能够诚实透明地向潜在的求职者推荐一家公司。

巴克利告诫大家不要被福利和积极的公司文化蒙蔽双眼，她强调，雇佣关系最终是一场交易。公司会优先考虑自己的利益，而不是员工的福祉，尤其是在财务困难或违反政策的情况下。她强烈建议不要为了取悦雇主而牺牲个人关系、心理健康、伦理或个人价值观。

她的核心信息是，要出色地履行你的工作职责，但始终要把家庭、朋友和个人福祉放在首位。如果雇主通过提供公平的薪酬、支持员工健康和投资于员工成长来回报你，那么积极的反馈才是合理的。文章以她父亲的感言结尾，即人生的遗憾通常不是因为工作不够努力，而是因为没有花足够的时间陪伴所爱的人。

---

## 7. Bild AI (YC W25) 正在旧金山招聘创始工程师

**原文标题**: Bild AI (YC W25) is hiring a founding engineer in SF

**原文链接**: [https://www.ycombinator.com/companies/bild-ai/jobs/m2ilR5L-founding-engineer](https://www.ycombinator.com/companies/bild-ai/jobs/m2ilR5L-founding-engineer)

位于旧金山的 Y Combinator W25 期创业公司 Bild AI 正在招聘一名创始工程师加入其团队。Bild AI 正在通过开发能够理解建筑蓝图的人工智能来革新建筑行业，从而自动化成本估算和许可申请等任务。

理想的候选人将与联合创始人 Roop Pal 和 Puneet Sukhija 密切合作，专注于其产品的智能层。 这包括设计用于理解蓝图的算法和系统，应用计算机视觉和 LLM 模型，以及根据用户反馈交付原型。 该职位提供 10 万美元至 18 万美元的薪水以及 0.50% 至 2.00% 的股权。

Bild AI 正在寻找具有构建全栈产品经验（尤其是在 infra/frontend 方面）、专注于 AI 学习的成长型思维模式，以及愿意搬到旧金山进行面对面协作的人才。 强大的沟通能力和“不嫌任务太小”的态度至关重要。 额外加分项包括创业经验、计算机视觉/机器学习经验、建筑/建筑/房地产知识以及对积极影响的热情。

鼓励有兴趣的候选人发送包含简历/LinkedIn 个人资料、GitHub/作品集以及他们对 Bild AI 感兴趣的原因的电子邮件至 jobs[at]bild.ai。该公司强调其快节奏的环境，并鼓励立即申请。 他们获得了 Khosla Ventures 的资助，并正在以模型花园的方式构建蓝图理解。

---

## 8. 关于Vision Transformer，每个人都应该知道的三件事

**原文标题**: Three things everyone should know about Vision Transformers

**原文链接**: [https://arxiv.org/abs/2203.09795](https://arxiv.org/abs/2203.09795)

Touvron等人arXiv论文“关于Vision Transformers，每个人都应该了解的三件事”探讨了Vision Transformers (ViTs) 在计算机视觉任务中高效且有效的适配方法。 它提供了三个关键见解：

1.  **残差层的并行处理：** 该论文表明，ViTs中残差层的顺序处理可以在不显著影响准确性的情况下进行部分并行化。 这带来了训练和推理中潜在的加速。

2.  **注意力层的高效微调：** 作者发现，*仅*微调注意力层就足以使ViTs适应更高分辨率的图像和不同的分类任务。 这种方法大大降低了微调过程中的计算成本和内存消耗，并实现了跨多个任务的权重共享。

3.  **通过MLP预处理改进自监督训练：** 添加基于MLP的patch预处理层可提高ViTs的类BERT自监督训练的性能，其中图像patches被掩盖，并且模型经过训练以预测被掩盖的区域。

该论文使用ImageNet-1k数据集验证了这些发现，并在ImageNet-v2上证实了它们。 还在六个较小的数据集上评估了迁移性能。 该研究表明，这些设计选择可以使ViTs对于更广泛的计算机视觉应用更易于访问和高效。

---

## 9. 展示HN: Zev – 记住 (或发现) 终端命令

**原文标题**: Show HN: Zev – Remember (or discover) terminal commands

**原文链接**: [https://github.com/dtnewman/zev](https://github.com/dtnewman/zev)

Zev：通过自然语言查找和记忆终端命令的命令行工具

**主要特性：**

*   **自然语言查询：** 用户可以使用简单的英语搜索命令。
*   **交互模式：** 用户可以启动类似shell的界面与Zev进行交互。
*   **OpenAI集成：** Zev利用OpenAI API来理解自然语言并将其转换为终端命令（需要OpenAI账户和API密钥）。
*   **Ollama支持：** 作为OpenAI的替代方案，Zev可以配置为使用Ollama，从而实现本地命令生成，无需依赖外部API。
*   **配置：** 用户可以通过运行`zev --setup`来更新他们的OpenAI API密钥、OpenAI基础URL或OpenAI模型。

**用法：**

Zev可以通过`pip install zev`安装，可以通过简单地运行`zev`进入交互模式，也可以直接使用`zev '<你想要做什么>'`进行查询。 该工具支持各种命令类别，包括文件操作、系统信息、网络命令和Git操作。
该项目是开源的（MIT许可证），欢迎贡献。

---

## 10. IBM Z17内部探秘

**原文标题**: A Tour Inside the IBM Z17

**原文链接**: [https://community.ibm.com/community/user/ibmz-and-linuxone/blogs/elizabeth-k-joseph1/2025/04/23/a-tour-inside-the-ibm-z17?communityKey=e7b7d299-8509-4572-8cf1-c1112684644f](https://community.ibm.com/community/user/ibmz-and-linuxone/blogs/elizabeth-k-joseph1/2025/04/23/a-tour-inside-the-ibm-z17?communityKey=e7b7d299-8509-4572-8cf1-c1112684644f)

在没有访问实际“IBM z17内部之旅”文章的情况下，我可以根据一般知识和此类文章的预期内容提供一个摘要。该摘要将侧重于现代IBM Z大型机（z17）之旅可能涵盖的组件和架构。

**可能的摘要：**

“IBM z17内部之旅”可能探索了使z17成为强大且可靠的企业计算平台的先进工程和组件。该文章可能会深入探讨z17的架构，强调其高性能处理器，可能展示每个处理器芯片的内核数量和时钟速度。它可能会突出该系统的大容量内存及其处理海量工作负载的能力。

一个关键特性几乎肯定会涵盖I/O子系统，强调其高带宽以及连接各种存储和网络设备的能力。该文章可能会讨论系统的内置安全功能，包括基于硬件的加密和安全启动过程，这对于敏感数据处理至关重要。

该之旅也可能涉及系统的虚拟化功能，展示其同时运行多个操作系统和工作负载的能力。冗余和容错，这对于大型机的正常运行时间至关重要，将是另一个重点，其中将解释系统如何处理组件故障。

最后，该文章可能会简要介绍冷却系统和电源管理策略，这些策略用于保持z17在要求苛刻的数据中心环境中高效可靠地运行。总体信息可能是z17的复杂设计，它结合了尖端的硬件和软件，为关键任务应用程序提供无与伦比的性能、安全性和可用性。

---

## 11. 马克·扎克伯格称社交媒体已过时

**原文标题**: Mark Zuckerberg Says Social Media Is Over

**原文链接**: [https://www.newyorker.com/culture/infinite-scroll/mark-zuckerberg-says-social-media-is-over](https://www.newyorker.com/culture/infinite-scroll/mark-zuckerberg-says-social-media-is-over)

本文探讨了联邦贸易委员会（FTC）对Meta的反垄断诉讼，认为该公司在“个人社交网络服务”领域维持着非法垄断。作者强调了马克·扎克伯格的证词，他实际上承认了2010年代存在的社交媒体已经结束，Facebook和Instagram等平台正在演变为娱乐和内容消费中心。Meta辩称，这种转变意味着没有单一公司垄断当前的格局，并列举了来自TikTok、YouTube，甚至iMessage的竞争。

FTC的案件面临挑战，因为它重新评估了多年前批准的交易，当时数字世界截然不同。由于Meta的平台是免费的，证明“消费者损害”非常困难。FTC声称Meta的行为扼杀了创新并减少了选择，但考虑到WhatsApp在Meta旗下的增长，这一论点难以成立。

文章讨论了FTC可能强制Meta分拆的可能性，并探讨了政治因素，包括扎克伯格最近与特朗普政府的互动。随着人工智能的出现和新的社交网络即将出现，作者认为FTC可能专注于一个已经过时的问题。

---

## 12. 创建你自己的联邦式微博

**原文标题**: Creating your own federated microblog

**原文链接**: [https://fedify.dev/tutorial/microblog](https://fedify.dev/tutorial/microblog)

本文指导用户使用ActivityPub服务器框架Fedify创建联邦式微博，侧重于实际操作而非理论理解。目标读者是对HTML、HTTP、命令行、SQL、JSON和JavaScript等Web应用程序基础知识较为熟悉的开发者。

目标是构建一个单用户微博，它可以通过ActivityPub与其他联邦服务交互，具有用户创建、关注/取消关注其他帐户、帖子创建和查看 feed 的功能。 为了简化本教程，有意省略了诸如个人资料自定义、帖子编辑/删除、安全性和社交互动（喜欢、评论）等某些功能。

本文详细介绍了开发环境的设置，包括安装 Node.js（v20.0.0 或更高版本）并通过 npm 安装 `@fedify/cli` 命令。它逐步介绍了使用特定选项（Node.js、npm、Hono、In-memory、In-process）初始化 Fedify 项目并验证生成的演示代码是否正确运行。

本指南还鼓励使用带有推荐的 Biome 扩展的 Visual Studio Code 进行 TypeScript 开发。 为不熟悉这些技术的读者提供了 TypeScript 和 JSX 的简要概述。 最后，它开始构建帐户创建页面，首先是使用 Pico CSS 框架进行样式设置的基本布局组件。

---

## 13. 搜索市场中的非对称内容审核：以成人网站为例

**原文标题**: Asymmetric Content Moderation in Search Markets: The Case of Adult Websites

**原文链接**: [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5106235](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5106235)

搜索引擎市场中的非对称内容审核：以成人网站为例

本研究论文《搜索引擎市场中的非对称内容审核：以成人网站为例》调查了主要在线平台的内容审核对市场竞争的影响。该研究重点关注一个外生冲击，即最大的成人内容平台因一项要求内容验证的政策变更而删除了其80%的视频库。

作者使用差异中的差异方法和每日网站流量数据发现，该政策导致该平台在一个月内流量下降了41%，表明用户对被删除内容有强烈的偏好。然而，这些流量并没有简单地消失，而是主要被竞争对手平台吸收，包括主流网站和监管较少的“边缘”网站。在六个月内，边缘网站的访问量增加了55%，明显高于主流竞争对手10%的增长。

研究人员强调了搜索引擎在这种转变中的关键作用，注意到来自搜索引擎推荐的流量涌入边缘平台。他们还记录了搜索竞争的加剧，领先平台战略性地使用DMCA备案来删除竞争对手的侵权内容。

该论文的结论是，非对称的内容审核可以显著地重塑市场竞争，将用户推向监管较少的在线空间，并改变平台替代的动态。研究结果突出了内容审核政策的意外后果及其对更广泛的数字生态系统的影响。

---

## 14. 小企业成功需要顾客

**原文标题**: You Need Customers to Succeed in Small Business

**原文链接**: [https://goodenough.us/blog/2025-04-24-you-need-customers-to-succeed-in-small-business/](https://goodenough.us/blog/2025-04-24-you-need-customers-to-succeed-in-small-business/)

巴里·赫斯认为，客户关系对小型企业的成功至关重要。他强调，与大型公司不同，小型企业通过直接、人性化的互动来建立信任和培养回头客。他批评小型企业模仿公司做法的趋势，尤其是在使客户难以沟通以及使用不必要地复杂的软件方面。

赫斯强调小型企业在经济中扮演的重要角色，引用统计数据说明其普遍性、就业贡献和GDP影响，以及其作为创新中心的作用。他强调，虽然许多小型企业渴望经济上的舒适，但其核心成功取决于通过有效沟通来获取和保持客户。

他断言，以友善、清晰和快速的方式回应客户咨询至关重要。他进一步建议，主动与客户进行提问可以加强关系。赫斯强调，这些互动应该是个人化和真诚的，而不是自动化的，突出了健康客户关系的重要性。

最后，赫斯以他的公司Good Enough为例，说明他们致力于提供人工客户支持，并强调他们的团队致力于用有用的解决方案来回应所有客户咨询，以及他们的软件Jelly支持并促进这些人工互动。他总结道，优先考虑真诚的客户对话对于小型企业的成功至关重要。

---

## 15. 人工智能无人驾驶汽车

**原文标题**: AI Horseless Carriages

**原文链接**: [https://koomen.dev/essays/horseless-carriages/](https://koomen.dev/essays/horseless-carriages/)

由于无法访问“AI 无马马车 | koomen.dev”文章的实际内容，我只能根据标题提供一个概括性的摘要。此摘要假定该文章讨论了自动驾驶汽车的演变，并将此演变与历史上从马拉马车到汽车的过渡进行了类比。

该文章很可能探讨了人工智能驱动的自动驾驶汽车的现状和未来潜力。它可能会将汽车（当时被称为“无马马车”）在采用初期所面临的怀疑和挑战，与当前围绕自动驾驶汽车技术的担忧进行比较。

该文章可能讨论：

*   **历史类比：** 将最初人们认为汽车危险且不可靠的看法，与当前对自动驾驶汽车的保留态度进行对比。
*   **人工智能技术：** 解释使自动导航成为可能的人工智能算法、传感器（如激光雷达和摄像头）以及机器学习技术。
*   **挑战和障碍：** 解决广泛采用的障碍，例如安全问题、伦理困境（例如，电车难题）、监管框架以及处理不可预测情况的技术局限性。
*   **未来影响：** 考察自动驾驶汽车对社会的潜在影响，包括交通、城市规划、就业和环境可持续性的变化。

作者 Koomen 可能会对人工智能在交通运输领域的发展轨迹提供见解和观点，或许会倡导负责任地开发和部署这项技术，同时承认从“无马马车”的出现中吸取的历史教训。这篇文章很可能以对人工智能驱动的交通运输普及化和具有潜在变革意义的未来愿景作为结尾。

---

## 16. 展示HN：我自己从零开始写的、能运行DOOM的操作系统内核

**原文标题**: Show HN: My from-scratch OS kernel that runs DOOM

**原文链接**: [https://github.com/UnmappedStack/TacOS](https://github.com/UnmappedStack/TacOS)

这个"Show HN"帖子介绍了 TacOS，一个用 C 和汇编语言从零开始编写的业余操作系统内核。作者强调 TacOS 是一个类 UNIX 操作系统，能够运行 DOOM 以及较小的用户空间程序。它包括 VFS、调度器、TempFS、设备、上下文切换、虚拟内存管理和物理页面帧分配等功能。

该操作系统旨在在真实硬件（已在作者的笔记本电脑上测试）和 Qemu 模拟器中运行。虽然它是一个功能齐全的玩具操作系统，但作者承认它不完整，并且包含已知的错误，并强调它不适合在现实世界中使用。

该帖子提供了一个快速入门指南，包括克隆存储库和构建操作系统的命令，并指出需要 Qemu、NASM 和 Clang。作者还提到了一个用于其类似项目 PotatOS 的 Discord 服务器，更新会在那里分享，用户可以讨论操作系统开发。最后，该项目根据 Mozilla Public License 2.0 获得许可。

---

## 17. 你不会盗用字体。

**原文标题**: You wouldn't steal a font

**原文链接**: [https://fedi.rib.gay/notes/a6xqityngfubsz0f](https://fedi.rib.gay/notes/a6xqityngfubsz0f)

这不是一篇文章，而是一个关于 Mastodon 实例的非常简短的帖子。主旨是隐含的，借鉴了著名的反盗版口号“你不会偷一辆车”。

标题“你不会偷一个字体”引用了这场反盗版活动，暗示该帖子是关于未经适当许可或付费使用字体的道德或合法性。

帖子本身只是用户名为“@Rib”及其 Mastodon 账号和域名，后面跟着“Please turn on your JavaScriptLoading...” 这表明用户要么未登录，要么禁用了 Javascript，导致 Mastodon 帖子无法完全加载。因此，帖子实际上除了用户账号和标题暗示的字体盗版之外，没有包含任何内容。在看到完整帖子之前，不可能知道 Rib 想表达什么关于字体盗版的内容。

---

## 18. 日常使用 Linux 手机，为什么？

**原文标题**: Daily driving a Linux phone, but why?

**原文链接**: [https://thefoggiest.dev/2025/04/24/daily-driving-a-linux-phone-but-why](https://thefoggiest.dev/2025/04/24/daily-driving-a-linux-phone-but-why)

本文探讨了作者将Linux手机作为日常主力机的动机，尽管作者承认Android系统的便捷性和速度优势。作者强调，这一决定源于质疑社会规范、学习不同的生活方式以及提高安全性和隐私的愿望。 尽管有些人可能认为Linux手机由于潜在的漏洞而安全性较低，但作者强调了其开源特性以及缺乏基于监视的商业模式，这些都是显著的隐私优势。

作者承认PinePhone Pro的硬件速度较慢，但认为它足以满足视频播放和应用程序导航等基本任务。他们还强调了PinePhone Pro的物理优势，例如其较小的尺寸、较轻的重量以及存在的功能性3.5毫米耳机插孔。

作者计划使用他们解锁并打算刷入PostmarketOS系统的旧LGv40 Thinq，而不是PinePhone Pro。 他们更喜欢这款手机，因为它更小、更快、拥有更大的屏幕、3.5毫米插孔，并且包含无线充电、出色的摄像头和指纹识别器等功能。 主要目标是看看他们是否可以成功地在LGv40上启动Linux系统。

---

## 19. 有多少数学是可以被知道的？[视频]

**原文标题**: How much math is knowable? [video]

**原文链接**: [https://www.youtube.com/watch?v=VplMHWSZf5c](https://www.youtube.com/watch?v=VplMHWSZf5c)

提供的内容并非文章，而是YouTube网页上常见的标准页脚信息。它包括以下内容：

*   **YouTube服务条款、隐私政策和安全准则的链接。** 这些部分详细说明了使用该平台的规则、用户数据的处理方式以及采取的安全措施。
*   **版权信息。** 这明确了YouTube上内容的版权所有权和使用权。
*   **新闻咨询和版权相关问题的联系方式。** 这使得用户和组织能够出于特定目的联系YouTube。
*   **面向创作者、广告商和开发者的链接。** 这些部分提供了为不同用户群体量身定制的资源和信息，这些用户群体使用YouTube来创作内容、投放广告或构建应用程序。
*   **关于Google LLC的信息。** 这标识了负责YouTube的母公司。
*   **关于NFL Sunday Ticket的信息。** 这标识了通过YouTube提供的服务或内容。

本质上，它是YouTube的法律和运营细则，而不是关于数学的实质性文章。因此，它没有提供任何关于多少数学是可以被了解的信息。

---

## 20. YAGRI: 你读定了

**原文标题**: YAGRI: You are gonna read it

**原文链接**: [https://www.scottantipa.com/yagri](https://www.scottantipa.com/yagri)

本文介绍“YAGRI”（你会读到它），作为对常见软件工程原则“YAGNI”（你不需要它）的对立观点。YAGNI建议不要过度设计，而YAGRI则建议工程师应主动存储他们极有可能需要的数据，以用于调试、内部分析或仅仅是为了理解行为的上下文。

作者认为，将数据存储限制为仅UI立即需要的范围可能目光短浅。一个常见的例子是删除数据；简单地删除数据库行可能满足初始要求，但它会丢失关于谁删除的、如何删除的、何时删除的以及为什么删除的宝贵信息。

本文倡导维护良好的数据标准，包括`created_at`、`updated_at`、`deleted_at`、`created_by`以及CRUD操作期间使用的权限等字段。虽然并非每个字段都会被用到，但作者认为，即使只有一次需要这些额外数据来回答关键问题，也会使这项工作变得值得。

核心论点是，工程师是数据的管理者，大多数应用程序都围绕着跟踪事实展开。虽然不鼓励过度日志记录，但作者认为额外的时间戳很少会令人后悔。

---

## 21. 谷歌合同阻止摩托罗拉将Perplexity设置为默认助手。

**原文标题**: Google contract prevented Motorola from setting Perplexity as default assistant

**原文链接**: [https://www.bloomberg.com/news/articles/2025-04-23/perplexity-executive-says-google-blocked-motorola-s-use-of-ai-assistant](https://www.bloomberg.com/news/articles/2025-04-23/perplexity-executive-says-google-blocked-motorola-s-use-of-ai-assistant)

以下是根据彭博社文章标题的摘要：

据彭博社报道，一份谷歌合同阻止了摩托罗拉将其设备上的默认助手设置为Perplexity AI。 据报道，此消息来自一位Perplexity高管。 本质上，谷歌利用其与摩托罗拉等硬件制造商的合同协议来限制竞争对手AI助手（特别是Perplexity AI）的采用。 这凸显了谷歌通过阻碍将替代服务集成到流行设备中，来维持其在AI助手市场的主导地位的策略。 该文章表明，谷歌与设备制造商签订的合同包含限制预装或将竞争对手服务设置为默认服务的条款，从而使Google Assistant具有显著优势。 这种限制的影响是，它限制了消费者的选择，并可能扼杀AI助手领域的创新。

---

## 22. 我尝试购买一桶原油 (2015)

**原文标题**: I Tried to Buy an Actual Barrel of Crude Oil (2015)

**原文链接**: [https://www.bloomberg.com/news/articles/2015-11-03/that-time-i-tried-to-buy-some-crude-oil](https://www.bloomberg.com/news/articles/2015-11-03/that-time-i-tried-to-buy-some-crude-oil)

无法访问文章链接。

---

## 23. Show HN: Colanode，开源且本地优先的Slack和Notion替代品

**原文标题**: Show HN: Colanode, open-source and local-first Slack and Notion alternative

**原文链接**: [https://github.com/colanode/colanode](https://github.com/colanode/colanode)

Colanode：一款开源、本地优先的 Slack 和 Notion 替代方案，专为重视数据隐私和控制的团队及个人设计，通过自托管实现。它提供实时聊天、富文本页面创建（类似 Notion）、可定制数据库和文件管理。

该平台通过桌面应用程序连接到自托管服务器，允许用户管理多个工作区。其“本地优先”架构将更改保存到本地 SQLite 数据库，并在后台同步，从而实现离线工作和快速数据访问。Colanode 利用无冲突复制数据类型 (CRDT) 来处理页面和数据库记录上的并发编辑，确保无缝协作。

用户可以通过下载桌面应用程序并连接到免费测试版云服务器（欧盟和美国）开始使用。对于自托管，Colanode 提供了一个 Docker Compose 文件，需要带有 pgvector 的 Postgres、Redis（或 Valkey）以及 S3 兼容的存储。所有必要的环境变量都可以在 Docker Compose 文件中找到。Colanode 在 Apache 2.0 许可下发布。

---

## 24. CubeCL: 用于 CUDA、ROCm 和 WGPU 的 Rust GPU 内核

**原文标题**: CubeCL: GPU Kernels in Rust for CUDA, ROCm, and WGPU

**原文链接**: [https://github.com/tracel-ai/cubecl](https://github.com/tracel-ai/cubecl)

CubeCL: 简化多平台高性能 GPU 内核开发的 Rust 扩展

CubeCL 是一个 Rust 扩展，旨在简化 CUDA、ROCm/HIP (开发中) 和 WGPU (Vulkan、Metal、DirectX、WebGPU) 的高性能、多平台 GPU 内核编写。 它采用即时 (JIT) 编译器，具有自动向量化、编译时 (comptime) 优化和自动调优功能，以实现最佳性能。

主要功能包括：

*   **基于 Rust 的 GPU 编程：** 使用熟悉的 Rust 语法编写 GPU 内核。
*   **多平台支持：** 从单个代码库针对各种 GPU 运行时。
*   **自动向量化：** 编译器自动向量化代码以用于 SIMD 指令，从而优化跨不同硬件的性能。
*   **编译时 (Comptime)：** 在运行时自定义编译器 IR，用于指令专业化、循环展开和形状专业化，而无需编写多个内核变体。
*   **自动调优：** 评估不同的内核配置，以选择特定硬件的最佳性能配置，并为后续运行进行缓存。
*   **内存管理：** 采用优化的内存管理策略，大量重用缓冲区。
*   **生态系统重点：** 旨在在 Rust 中构建高性能和科学计算生态系统，包括优化矩阵乘法等线性代数组件。

CubeCL 使用 Rust 的 proc 宏来解析内核代码并生成负责创建中间表示 (IR) 的 Rust 函数。 它的设计围绕立方体拓扑展开，提供了一种一致的方式来映射到不同 API 中的硬件概念。

该项目目前处于 alpha 阶段，欢迎贡献以扩展其功能。

---

## 25. AI编码的隐性成本

**原文标题**: The hidden cost of AI coding

**原文链接**: [https://terriblesoftware.org/2025/04/23/the-hidden-cost-of-ai-coding/](https://terriblesoftware.org/2025/04/23/the-hidden-cost-of-ai-coding/)

人工智能编码的隐性成本：本文探讨了软件开发中人工智能使用增加的潜在弊端：即编码过程本身所带来的乐趣和成就感的丧失。作者反思了“心流”状态——一种深度沉浸且令人满足的精神状态，在这种状态下创造力和生产力蓬勃发展——以及传统编码如何培养这种体验。

借助 Cursor 等人工智能工具，作者发现编码变得更高效，但也更被动。他们感觉自己更像是一位策展人，提示和评估人工智能生成的代码，而不是直接编写代码。这种转变引发了人们对长期以来主要依靠人工智能生成代码的开发人员的幸福感和参与度的担忧。

文章提出的核心问题是，将编程的核心创造性问题解决方面外包给人工智能，是否也会外包获得满足感的机会。作者认为，虽然人工智能可以提高生产力，但该行业需要考虑如何保留“心流”空间和手动编码，即使这不是最有效的方法。文章最后质疑，如果以牺牲最初吸引许多人从事这个职业的乐趣为代价，优化是否值得，并建议重新思考如何在人工智能增强的开发世界中找到幸福感，或许是在更高层次的设计或软件开发的人文方面。

---

## 26. 发布 HN：Cua (YC X25) – 用于计算机使用代理的开源 Docker 容器

**原文标题**: Launch HN: Cua (YC X25) – Open-Source Docker Container for Computer-Use Agents

**原文链接**: [https://github.com/trycua/cua](https://github.com/trycua/cua)

Cua（发音“酷-啊”）是一个开源框架 (YC X25)，它使 AI 代理能够在 Apple Silicon Mac 上的虚拟容器内控制完整的操作系统，实现高达 97% 的原生速度。它结合了高性能虚拟化和计算机使用界面，允许代理在 macOS 或 Linux 环境中与应用程序交互、浏览网页、编写代码和执行复杂的工作流程。

主要优势包括：通过在 VM 中运行代理来增强安全性和隔离，接近原生性能，选择操作系统的灵活性，工作流程的可重复性，以及内置的 LLM 集成。

要开始使用，用户可以选择仅安装用于 VM 管理的 Lume CLI，或者安装包含 CLI 和 Python 库的完整套件以获得代理功能。Cua 提供不同的安装选项，包括使用预构建镜像或从源代码构建以获取 nightly 功能和进行贡献。

该单体仓库包含多个库：Lume (用于 VM 管理的 CLI)，Computer (计算机使用界面) 和 Agent (AI 代理框架)。还提供 Core、PyLume、Computer Server 和 SOM 等辅助库。提供了大量文档和 notebook 示例用于入门。演示展示了 Cua 的实际应用，包括将其与 Claude Desktop、Tableau 一起使用以及在 Cursor 中修复 GitHub 问题的示例。

Cua 欢迎贡献，并根据 MIT 许可证授权，OmniParser 根据 CC-BY-4.0 授权。该项目强调它不隶属于 Apple、Canonical 或 Microsoft，后者的商标被提及。

---

## 27. 教授LLM如何进行实体建模

**原文标题**: Teaching LLMs how to solid model

**原文链接**: [https://willpatrick.xyz/technology/2025/04/23/teaching-llms-how-to-solid-model.html](https://willpatrick.xyz/technology/2025/04/23/teaching-llms-how-to-solid-model.html)

本文探讨了大型语言模型（LLMs）生成CAD模型的新兴能力，特别关注于使用LLMs编写开源程序化CAD工具OpenSCAD代码。作者强调了LLMs作为AI机械工程师的潜力，它们能够通过利用其代码生成技能来设计和改进CAD模型。

作者创建了一个评估流程，以测试各种LLMs通过OpenSCAD生成实体模型的性能，将生成的代码转换为STL文件，并将其与参考模型进行比较。该评估使用体积、边界框和倒角距离等几何检查来确定通过/失败分数。

对包括Gemini和Sonnet在内的几个模型的评估结果表明，最近的LLMs，尤其是推理模型，在生成有效的OpenSCAD代码和通过几何检查方面取得了显著改进。作者指出，虽然LLMs擅长生成可编译的代码，但空间推理和复杂的多步骤任务仍然具有挑战性。

文章还提到了AdamCad和Zoo.dev等提供文本到CAD产品的初创公司的推出。作者测试了Zoo.dev的API，该API直接输出STL文件，发现其性能与LLMs生成OpenSCAD相当。

最后，作者提出了使该方法更实用的潜在改进方案，包括用于迭代改进的更好UI/UX、草图等视觉输入方法以及参数滑块。作者总结说，文本到CAD具有巨大的潜力，估计在未来6-24个月内可能成为机械工程师常用的工具，这取决于进一步的模型改进和产品改进。

---

## 28. 无人机首次成功触发和引导闪电

**原文标题**: First Successful Lightning Triggering and Guiding Using a Drone

**原文链接**: [https://group.ntt/en/newsrelease/2025/04/18/250418a.html](https://group.ntt/en/newsrelease/2025/04/18/250418a.html)

NTT公司宣布世界首次成功利用无人机触发和引导闪电。该实验于2024年12月至2025年1月在日本进行，成功触发了一次指向无人机的闪电，证明了无人机的防雷技术和基于电场的闪电触发方法的有效性。

关键创新包括用于保护无人机的防雷笼，可将高电流从内部组件转移走，以及基于电场的闪电触发技术，该技术使用连接无人机和地面的导线以及高压开关来快速增加电场并引发闪电。防雷笼承受了高达150kA的人工闪电冲击，大大超过了平均自然闪电冲击。

NTT设想使用“闪电无人机”通过主动在安全地点触发闪电来保护城市和基础设施，从而减轻不可预测的雷击造成的损害。未来的研究将侧重于提高闪电位置预测，理解闪电机制，以及探索利用闪电能量的潜力。最终目标是创建一个免受雷击损害的社会，并有可能捕获和储存闪电能量以供未来使用。

---

## 29. AMD 发布 GPU 虚拟化开源驱动，Radeon “已在规划中”

**原文标题**: AMD Publishes Open-Source Driver for GPU Virtualization, Radeon "In the Roadmap"

**原文链接**: [https://www.phoronix.com/news/AMD-GIM-Open-Source](https://www.phoronix.com/news/AMD-GIM-Open-Source)

AMD发布开源“GPU-IOV模块”(GIM)用于GPU虚拟化，专门针对Instinct加速器。该模块专为Linux内核和KVM虚拟机管理程序设计，可实现基于SR-IOV的硬件虚拟化，提供虚拟功能配置、GPU调度、挂起检测和PF/VF握手等功能。初始版本适用于Instinct MI300X硬件，并在Ubuntu 22.04 LTS (ROCm 6.4) 上进行了测试。代码可在GitHub上找到，但AMD将驱动程序向上游合并到主线Linux内核的计划目前尚不明确。

重要的是，AMD已表示将GIM/SR-IOV支持引入其Radeon客户端独立显卡“已在路线图上”。对于Radeon用户来说，这是一个备受期待的功能。虽然没有给出具体的时间表，但AMD工程师Anush Elangovan在X（前身为Twitter）上确认了这些计划的存在，这燃起了人们对在不久的将来实现此功能的希望。GIM针对Instinct加速器的发布以及计划扩展到Radeon GPU表明AMD越来越关注其产品线中的GPU虚拟化能力。

---

## 30. Common Lisp 中的图形实时编程

**原文标题**: Graphics livecoding in Common Lisp

**原文链接**: [https://kevingal.com/blog/cl-livecoding.html](https://kevingal.com/blog/cl-livecoding.html)

本文探讨了Common Lisp中的“实时编码”概念，它允许开发者修改和重新编译一个正在运行的程序而无需停止它。作者将此与传统的“停止-修改-重新编译-重启”工作流程进行对比，突出了开发中更高的流畅性和交互性所带来的好处。

本文介绍了Common Lisp的Sketch图形框架，并将其与Processing进行了类比。文章提供了一个绘制红色圆圈的简单例子，以演示Sketch的基本功能。

本文的核心是通过从头开始构建Boids算法来演示实时编码。该过程涉及迭代地定义boid类，实现三个核心规则（分离、凝聚和对齐），并更新boid的位置。作者展示了如何在运行时重新编译函数，从而实现即时视觉反馈和错误纠正，而无需中断正在运行的程序。文章给出了一个修复缺失函数`draw-boids`而无需重启程序的具体例子。

作者强调Common Lisp的条件系统是另一个增强实时编码的强大功能，它允许错误恢复和程序行为的动态修改。文章最后提倡更具交互性的开发工作流程，并鼓励读者探索其他语言中的类似功能，或通过自动重启或脚本语言集成等技术来实现它们。

---

## 31. 有毒的鸣鹃鵙，为数不多的有毒鸟类之一

**原文标题**: Hooded pitohui, one of the only toxic birds

**原文链接**: [https://www.australiangeographic.com.au/blogs/creatura-blog/2014/06/hooded-pitohui-bird/](https://www.australiangeographic.com.au/blogs/creatura-blog/2014/06/hooded-pitohui-bird/)

这并不是一篇真正*关于*毒鸟鹟鹟的文章。虽然标题暗示了这一点，但实际内容却是为2024年日历和记事本做的广告，这些产品以精美的艺术作品为特色。

广告重点：

*   **产品：** 2024年日历和记事本。
*   **益处：** 能够全年用“精美艺术作品”装饰墙壁。
*   **行动号召：** 鼓励读者立即购买日历和记事本（“立即订购”），并附有“立即购买”按钮。

虽然标题提到了毒鸟鹟鹟是为数不多的有毒鸟类之一，但实际内容并没有对此进行扩展。标题很可能被用来吸引注意力，但文本的核心目的是推销日历和记事本。

---

## 32. 格伦转移正在吞噬互联网。

**原文标题**: The Gruen Transfer is consuming the internet

**原文链接**: [https://sebs.website/blog/the%20gruen-transfer-is-consuming-the-internet](https://sebs.website/blog/the%20gruen-transfer-is-consuming-the-internet)

塞巴斯蒂安·大卫·里斯的博文探讨了“格鲁恩转移”现象，即故意使用户迷惑的布局和用户界面让消费者迷失方向，导致他们偏离最初的意图并进行冲动行为。里斯认为，最初在超市等实体零售场所观察到的格鲁恩转移现象现在已在线上普遍存在，尤其是在 Facebook 等社交媒体平台上。他描述了 Facebook 的信息流如何设计为让用户保持参与度，却变得充斥着广告、表情包和营销内容，使用户难以专注于与亲友联系。

文章将这一概念扩展到社交媒体之外，强调了许多网站采用类似的策略来鼓励冲动行为。例子包括维基百科的兔子洞以及主要在线服务上删除帐户或取消订阅的故意模糊的过程。里斯认为，这些黑暗用户体验模式引入的过度摩擦和复杂性最终可能会损害用户体验，暗示了一种“网页设计的拉弗曲线”。

他赞扬了欧盟要求取消订阅与订阅一样容易的立法，提倡将“复杂性”作为一种潜在的立法措施。里斯最后幽默地希望类似的法规也能适用于实体零售场所。文章最终批判了在线上越来越多地使用的操纵性设计实践，并呼吁更多地考虑用户体验和道德设计原则。

---

## 33. 粗心的人

**原文标题**: Careless People

**原文链接**: [https://pluralistic.net/2025/04/23/zuckerstreisand/#zdgaf](https://pluralistic.net/2025/04/23/zuckerstreisand/#zdgaf)

本文评述了莎拉·温-威廉姆斯的回忆录《草率之人》，该书详细描述了她在Facebook（现为Meta）从事全球政策工作的经历。评论重点介绍了温-威廉姆斯从新西兰外交机构的小职员到Facebook全球扩张的关键人物的历程。

作者将这本书描述为一本揭露内幕的书，揭示了马克·扎克伯格、谢丽尔·桑德伯格和乔尔·卡普兰等关键人物的“可耻秘密”和应受谴责的行为。例子包括扎克伯格幼稚的要求、桑德伯格的特权意识以及卡普兰的无能和对温-威廉姆斯的骚扰。

评论强调了Facebook最初对美国以外国家的不感兴趣，认为这归因于美国缺乏隐私保护以及其作为利润丰厚的市场的地位。然而，随着Facebook在美国市场的饱和，该公司转向全球扩张，这使得温-威廉姆斯成为一项关键资产。

作者认为，Facebook对增长的无情追求不仅源于扎克伯格支配一切的需求，也源于维持高市盈率的物质压力。这种增长对于Facebook超越竞争对手和收购其他公司至关重要。

最终，温-威廉姆斯对Facebook感到失望，原因是该公司“令人作呕、冷酷无情和残忍的行为”，包括卡普兰的性骚扰以及该公司通过承诺监视和审查来进入中国市场的企图。

---

## 34. GTA圣安地列斯20年老Bug如何在Windows 11 24H2中浮出水面

**原文标题**: How a 20 year old bug in GTA San Andreas surfaced in Windows 11 24H2

**原文链接**: [https://cookieplmonster.github.io/2025/04/23/gta-san-andreas-win11-24h2-bug/](https://cookieplmonster.github.io/2025/04/23/gta-san-andreas-win11-24h2-bug/)

GTA San Andreas 20年老Bug调查：Windows 11 24H2特有

该文章详细介绍了在Windows 11 24H2中浮现的GTA San Andreas一个存在了20年的bug的发现和调查。该bug会导致Skimmer水上飞机从游戏中消失，或者，当通过脚本生成时，会发射到游戏世界的遥远区域，导致冻结或图形异常。

调查显示，该问题源于`CFileLoader::LoadVehicleObject`函数中的一个未初始化的变量。此函数解析`vehicles.ide`文件，该文件定义了车辆参数。 Skimmer在此文件中的条目缺少前后轮比例参数，这个错误源于它最初在罪恶都市中被定义为船只。 游戏未能验证数据的完整性，导致这些参数未初始化。

作者发现，游戏代码假定所有参数都存在，导致未初始化的值被用于后续与Skimmer碰撞模型和悬架相关的计算中。这些损坏的值导致飞机以错误的姿态生成，从而导致了上述问题。

该bug仅在Windows 11 24H2中出现的原因被确定与未初始化的变量继承了先前解析的车辆 Topfun 的值有关。 先前使用的值，即 0.7 的车轮比例，被写入堆栈，然后被 Skimmer 使用。 这碰巧有效，直到一些操作系统更新导致堆栈上的更改，并且这些值变得无效。

作者通过在 `CFileLoader::LoadVehicleObject` 中的 `sscanf` 调用中为缺少的车轮比例参数提供默认值，从而使用 SilentPatch 修复了此问题。

---

## 35. MCP 的未来

**原文标题**: The Future of MCPs

**原文链接**: [https://iamcharliegraham.substack.com/publish/post/161906169](https://iamcharliegraham.substack.com/publish/post/161906169)

无法访问文章链接。

---

## 36. 帆具调整模拟器

**原文标题**: Sail-Trim Simulator

**原文链接**: [https://simulator.atterwind.info/](https://simulator.atterwind.info/)

本文介绍一款“帆调整模拟器”，旨在帮助用户理解和提高帆调整技能，尤其是在高性能帆船运动中。该模拟器侧重于可视化和理解风梯度、视在风以及不同速度和航向下的帆扭曲等概念。其核心目的是增强对船只加速如何影响视在风以及随后最佳帆调整的理解。

该模拟器通过展示DNA F1x（一种A级水翼双体船）上使用的调整设置，提供了一个真实的比较。这使得用户能够将模拟环境与实际应用联系起来。

模拟器的导航和交互方式多样，支持鼠标、键盘、触摸，甚至可共享的Web链接。

最后，本文提到，对于那些有兴趣深入研究或进一步开发的人，模拟器的源代码和更多文档可在Github上找到。其目的是提供一个实用的工具，用于学习风的基本知识和改进帆调整技术，尤其是在视在风不断变化的情况下，这与高性能帆船运动场景相关。

---

## 37. 韩国81998家酒吧最短步行路线

**原文标题**: Shortest-possible walking tour to 81,998 bars in South Korea

**原文链接**: [https://www.math.uwaterloo.ca/tsp/korea/index.html](https://www.math.uwaterloo.ca/tsp/korea/index.html)

本文详细介绍了解决韩国境内81,998家酒吧的旅行商问题（TSP）的方案。研究人员成功计算出了访问所有酒吧的最短步行路线，这一壮举超越了以往在道路地图上的旅行商问题记录。

该解决方案使用开源路径规划引擎（OSRM）计算所有酒吧对之间的旅行时间，创建了一个庞大的数据集。计算结果产生了一条可证明的最优路线，这意味着重新安排站点也无法减少15,386,177秒（178天）的步行时间。

本文强调了所需的计算能力，并挑战了即使是小型旅行商问题实例也无法解决的常见误解。该团队采用LKH代码来生成良好的解决方案，并采用Concorde代码，使用“切割平面法”来保证质量。这种方法涉及为路线分配分数，并迭代添加约束，以达到每条道路的最佳决策。

交互式地图允许用户探索该路线，突出显示特定区域并显示站点标记或路线边缘。该研究展示了数学优化在资源分配中的应用，参考了相关学会，并感谢了IBM CPLEX Optimizer的使用。

研究团队还感谢Oum Sang-il博士提供酒吧位置数据，并感谢OpenStreetMap和其他地图工具的使用。最后，本文提供了相关资源的链接，包括其他已解决的旅行商问题、旅行商问题历史和解决方案的阅读材料，以及关于P与NP问题的讨论。

---

## 38. 汽车与钥匙扣：汽车遥控器的攻击

**原文标题**: Cars and Key Fobs: Attacks on Car Remotes

**原文链接**: [https://web.stanford.edu/class/ee26n/Assignments/Assignment5.html](https://web.stanford.edu/class/ee26n/Assignments/Assignment5.html)

本EE26N讲义着重探讨汽车钥匙遥控器和无源钥匙进入及启动(PKES)系统的安全漏洞。首先解释了钥匙遥控器如何使用在特定频率下运行并利用滚动码来防止重放攻击的无线电遥控系统(RKS)。然而，它强调这些系统并非总是安全，并且可能被利用。

讲义概述了几种攻击方法，包括重放攻击（记录和重放钥匙遥控器信号）、重传设备（干扰和重建信号）以及对PKES系统的攻击（放大信号以欺骗汽车认为钥匙遥控器就在附近）。 它提到了诸如RTL-SDR、基于TI CC111X的USB加密狗、Flipper Zero和基于Raspberry Pi的发射器等工具，用于执行这些攻击。

文章还讨论了滚动密钥系统本身的漏洞。 它引用了大众汽车使用通用加密密钥用于数百万辆汽车的例子，允许攻击者在对ECU固件进行逆向工程后克隆钥匙遥控器。 作者暗示在后续讲座中将探讨更令人震惊的漏洞。

最后，它包括一个每周作业，有几个选项，包括研究斯巴鲁RKS系统，调查Flipper Zero争议，探索对工业机器的黑客攻击，以及寻找其他有趣的汽车黑客故事。 教授还要求对课程提出反馈意见。

---

## 39. 芬兰用反光漆涂鹿角 (2014)

**原文标题**: Finland is painting deer antlers with reflective paint (2014)

**原文链接**: [https://www.smithsonianmag.com/smart-news/avoid-deer-strikes-finland-painting-deer-antlers-reflective-paint-180949792/](https://www.smithsonianmag.com/smart-news/avoid-deer-strikes-finland-painting-deer-antlers-reflective-paint-180949792/)

2014年，芬兰驯鹿牧民协会开始在驯鹿角上测试反光涂料，以减少交通事故。芬兰道路上每年约有4000只驯鹿被撞死，造成1500万欧元的损失。此举旨在让反光涂料使驯鹿对驾驶员来说更可见，尤其是在碰撞最频繁的11月和12月的黑暗月份，以及蚊子驱使驯鹿更多移动的7月和8月。该倡议的重点是使动物本身更可见，而不是仅仅关注道路安全改善。涂料正在皮毛上进行测试，但据信在鹿角上效果更好，因为鹿角可以从各个角度看到。该实验旨在减少芬兰驯鹿与车辆碰撞造成的经济和动物福利影响。

---

## 40. 解剖英国战时夜视坦克潜望镜 [视频]

**原文标题**: Dissecting a British wartime night vision tank periscope [video]

**原文链接**: [https://www.youtube.com/watch?v=KlguQYJqs-E](https://www.youtube.com/watch?v=KlguQYJqs-E)

提供的信息极其稀少，仅知视频标题为“解剖英国战时夜视坦克潜望镜”，内容描述为YouTube标准的版权、广告、隐私和运营声明。

因此，总结如下：

名为“解剖英国战时夜视坦克潜望镜”的YouTube视频可能检查并探索了二战时期英国坦克使用的夜视潜望镜的内部运作原理。提供的内容描述仅包含标准的YouTube版权和政策信息，没有提供关于视频具体内容或发现的进一步细节。我们可以推断该视频可能涉及对潜望镜夜视技术的近距离检查和解释。

---

## 41. 基于MCPEngine的AWS Lambda上的MCP

**原文标题**: MCP on AWS Lambda with MCPEngine

**原文链接**: [https://www.featureform.com/post/deploy-mcp-on-aws-lambda-with-mcpengine](https://www.featureform.com/post/deploy-mcp-on-aws-lambda-with-mcpengine)

本文演示了如何使用 MCPEngine 在 AWS Lambda 上部署模型上下文协议 (MCP) 服务器，从而使大型语言模型 (LLM) 能够在生产就绪的无服务器环境中与外部工具交互。文章重点介绍了现有依赖于有状态连接的 MCP 实现的局限性，并介绍了 MCPEngine，它是一个支持可流式传输的 HTTP、身份验证和生产部署打包的开源解决方案。

本文通过三个例子进行讲解：

1.  **无状态天气 API：** 一个简单的 MCP 服务器，包含一个用于检索天气信息的工具，展示了使用 Docker 和 Terraform 部署到 Lambda 的基本方法。
2.  **有状态类 Slack API：** 扩展了之前的例子，包含了使用 Amazon RDS 的状态管理和一个上下文处理程序来持久化和检索消息，演示了如何在 Lambda 上将数据库与 MCP 服务器集成。
3.  **使用 Google SSO 进行身份验证的 API：** 使用 OpenID Connect (OIDC) 和 Google 作为身份提供商来保护 API，展示了基于令牌的身份验证以及如何从请求上下文中访问用户信息。

这些示例提供了分步说明，包括代码片段、Dockerfile 配置和 Terraform 脚本，以指导读者完成部署过程。MCPEngine 能够创建可扩展、安全且符合 MCP 规范的工具，这些工具可以与各种 LLM 和编排器集成，从而为代理系统和自动化工作流程开辟可能性。关键结论是，MCPEngine 允许您在 Lambda 上构建有状态且安全的 MCP 服务器，而无需传统的服务器管理。

---

## 42. 在技术变革面前，保持你的创作动力

**原文标题**: Sustain your creative drive in the face of technological change

**原文链接**: [https://thecreativeindependent.com/people/multi-disciplinary-artist-jack-rusher-on-the-need-to-sustain-your-creative-drive-in-the-face-of-technological-change/](https://thecreativeindependent.com/people/multi-disciplinary-artist-jack-rusher-on-the-need-to-sustain-your-creative-drive-in-the-face-of-technological-change/)

对拥有深厚技术背景的跨领域艺术家杰克·拉舍尔的访谈，探讨了艺术与科技的交汇、创造力的本质，以及如何在面对技术变革（特别是人工智能）时保持创作动力。

拉舍尔强调了交互式编程语言对生成艺术的重要性，因为它允许实时操作和探索。他认为科学家和艺术家本质上是相似的，并提倡一种培养技术和艺术技能的整体教育方法。他将创造力定义为一种基本的人类特质，对解决问题和沟通至关重要。

关于人工智能的影响，拉舍尔警告说，不要仅仅依赖人工智能生成的内容，因为它会导致平庸，并阻碍通过艺术创作过程实现的个人成长。他强调通过艺术创作实现人类转变的重要性。在承认人工智能作为工具的潜力同时，他重视人类在创造性活动中的能动性和技能发展。

拉舍尔强调了每日创作实践的重要性，以保持创作状态，并让你的潜意识在你不断做的事情上取得进展。他还强调了分享你的作品以找到观众并建立事业的重要性，即使在当前社交媒体环境的挑战中也是如此。

最后，他讨论了他在贝尔实验室的经历，强调了支持性环境和杰出同事对促进创新的重要性，但也注意到研究支持的转变，这种转变优先考虑不同的结果。

---

## 43. Yaakov Kirschen的另一项遗产

**原文标题**: Yaakov Kirschen’s other legacy

**原文链接**: [https://www.jns.org/yaakov-kirschens-other-legacy/](https://www.jns.org/yaakov-kirschens-other-legacy/)

无法访问文章链接。

---

## 44. 临床试验：新型营养配方治疗肠道菌群过度生长

**原文标题**: Clinical trial: novel nutritional formula treats gut microbial overgrowth

**原文链接**: [https://medicalxpress.com/news/2025-04-clinical-trial-nutritional-formula-effectively.html](https://medicalxpress.com/news/2025-04-clinical-trial-nutritional-formula-effectively.html)

本文报道了一项评估新型可口元素饮食(PED) mBiota Elemental在治疗小肠细菌过度生长(SIBO)和肠道产甲烷菌过度生长(IMO)的临床试验。西达-赛奈的研究人员进行了一项开放标签试验，招募了30名诊断为SIBO和/或IMO的成年人，他们连续两周食用mBiota Elemental，随后进行为期两周的食物再引入期。

结果显示出显著的改善。73%的参与者呼吸测试恢复正常，83%的人报告症状得到充分缓解。呼出的甲烷和氢气水平显著下降。粪便微生物组分析显示，关键微生物群（如Prevotella_9和Fusobacterium）减少，且92%的受试者体内的Methanobrevibacter smithii减少或消除。在PED阶段，腹胀、腹部膨胀、腹部不适、便秘和肠胃胀气等症状有所改善，在食物再引入阶段，其他症状进一步改善。

重要的是，没有报告严重的不良事件，并且标准血液检查结果保持在正常范围内。研究人员认为，mBiota Elemental与之前的元素饮食相比，其口感有所改善，因此依从性很高。他们得出结论，短期疗程的mBiota Elemental可能是一种有效的非抗生素饮食方法，用于管理SIBO和IMO，值得进一步进行对照试验以评估长期结果和潜在机制。该研究发表在《临床胃肠病学与肝脏病学》上。

---

## 45. 毁灭之路

**原文标题**: The Race That Turned to Ruin

**原文链接**: [https://longreads.com/2025/04/03/balloon-race-belarus-disaster/](https://longreads.com/2025/04/03/balloon-race-belarus-disaster/)

在2025年3月的文章《竞速变为废墟》中，尼克·戴维森讲述了1995年戈登·班尼特航空杯的故事，这是一场著名的国际热气球比赛。比赛在瑞士维尔开始，共有来自七个国家的15个气球参赛，竞争飞行最远距离。参赛者包括美国的迈克·华莱士和凯文·布里尔曼驾驶的“斯普林菲尔德精神号”，以及他们的朋友艾伦·弗兰克尔和约翰·斯图亚特-杰维斯驾驶的“D-加勒比号”。

随着比赛进入第三天，“斯普林菲尔德精神号”和“D-加勒比号”发现自己处于领先地位，向东南方向的白俄罗斯前进。比赛已获得允许参赛者飞越白俄罗斯和乌克兰的许可，但俄罗斯是严格禁止进入的。第四天，两支队伍都旨在扩大领先优势，并有可能创造新的距离记录。

然而，他们的旅程发生了黑暗的转折。一名白俄罗斯边防警卫发现了“斯普林菲尔德精神号”，并认为其具有潜在威胁，随即向防空司令部发出警报。不久之后，一架装备有机枪和大炮的俄罗斯米-24雌鹿直升机开始对气球进行具有攻击性的盘旋。华莱士向他的地面支援队报告了这次遭遇，但在传输过程中无线电中断。文章以悬念结尾，让华莱士和布里尔曼的命运悬而未决，并承诺在《The Atavist》杂志上刊登完整的故事。

---

## 46. 更多，一切，永远

**原文标题**: More Everything Forever

**原文链接**: [https://www.nytimes.com/2025/04/23/books/review/more-everything-forever-adam-becker.html](https://www.nytimes.com/2025/04/23/books/review/more-everything-forever-adam-becker.html)

亚当·贝克尔的著作《更多一切，永无止境》批判了驱动亿万富翁科技企业家“拯救人类”宏大项目的“技术救世主义”。贝克尔认为，像埃隆·马斯克的火星殖民计划是不切实际且被误导的，并强调了在火星上生存的极端挑战，例如辐射、有毒尘埃以及对地球持续资源运输的需求。他认为火星上的生活将会是一种痛苦的生存。

这本书审视了其他奇幻的设想，例如人工智能和太空殖民，揭露了这些冒险背后的核心原则。贝克尔指出了这种意识形态的三个关键特征：还原论（简化复杂问题）、盈利性（与科技行业的发展需求保持一致）以及超越的承诺（通过想象的终极目标来证明超越限制的合理性）。最终，贝克尔质疑这些技术驱动型解决方案的实用性和伦理影响，认为它们优先考虑的是永久增长和虚构的未来，而不是解决当前地球上的问题。

---

## 47. DOGE矿工代码支持美国劳工关系委员会举报人

**原文标题**: DOGE worker’s code supports NLRB whistleblower

**原文链接**: [https://krebsonsecurity.com/2025/04/doge-workers-code-supports-nlrb-whistleblower/](https://krebsonsecurity.com/2025/04/doge-workers-code-supports-nlrb-whistleblower/)

全国劳资关系委员会(NLRB)的举报人丹尼尔·贝鲁利斯声称，埃隆·马斯克的政府效率部(DOGE)在3月初非法访问并下载了NLRB的敏感案件文件。贝鲁利斯称，DOGE官员要求获得具有不受限制访问权限和网络日志记录豁免的“租户管理员”账户，允许他们读取、复制、更改甚至删除NLRB数据库中的活动日志。

举报人发现DOGE账户从GitHub下载了三个外部代码库，其中包括DOGE员工马尔科·埃莱兹创建的类似于“async-ip-rotator”的程序。该程序旨在绕过基于IP的速率限制，用于网络抓取和暴力攻击，引发了对其可能用于访问敏感数据的担忧。埃莱兹曾因涉及歧视性社交媒体帖子和违反财政部安全政策而备受争议，他曾在多家马斯克公司工作。

贝鲁利斯声称，超过10GB的数据从NLRB的案件文件中被下载，包括寻求加入工会的员工信息和专有商业文件。他担心这种未经授权的传输可能会给正在进行的劳资纠纷中的被告带来不公平的优势。其他下载的GitHub存档包括用于逆向工程API和自动化基于Web的任务的工具。

网上发布了一篇对埃莱兹代码的批评，称其“不安全、不可扩展且存在根本性的工程缺陷”。自文章发表以来，埃莱兹的代码仓库已被删除。

---

## 48. 1983年春：旨在提出全新在线互动方式的协议草案

**原文标题**: Spring 83: a draft protocol intended to suggest new ways of relating online

**原文链接**: [https://github.com/robinsloan/spring-83](https://github.com/robinsloan/spring-83)

“Spring 83”是一项旨在探索新型在线互动方式的协议草案。它被呈现为一个推测性的软件项目，意在激发“共同研究者”的反思和想象力探索，而非传统的用户。作者强调这是一个历史性的产物，但希望它仍然能鼓励读者思考创新的在线关系模型。

该文档提供了协议规范、先前草案以及各种编程语言（如JavaScript、Go和Python）中已知实现的链接。这些实现范围从客户端到Web组件，甚至还有OpenCL中的GPU实现。作者鼓励任何创建了与“Spring 83”相关软件（无论完成状态如何）的人与其联系，以便将其纳入列表。该作品以Creative Commons Attribution-ShareAlike许可协议共享。作者还建议阅读一篇叙事性描述以及关于与他人一起运行该协议的夏天的笔记，以便更深入地理解。

---

## 49. 我在意大利参加创业周末竞赛的经历

**原文标题**: My experience of participating to a startup weekend competition in Italy

**原文链接**: [https://danielpetrica.com/my-experience-of-participating-to-a-startup-weekend-competition-in-italy/](https://danielpetrica.com/my-experience-of-participating-to-a-startup-weekend-competition-in-italy/)

无法访问文章链接。

---

## 50. 重拾Minitel，COMPUTEL 交互式文图BBS回归

**原文标题**: Get your Minitel back, the COMPUTEL videotex BBS is back

**原文链接**: [https://cq94.medium.com/get-your-minitels-back-the-computel-videotex-bbs-is-back-1d8c42f1ea17](https://cq94.medium.com/get-your-minitels-back-the-computel-videotex-bbs-is-back-1d8c42f1ea17)

克里斯蒂安·奎斯特详细介绍了复兴他20世纪80年代基于Apple IIe的COMPUTEL电视资讯BBS的历程。他回顾了法国Minitel的早期岁月，他创建Cristel软件以实现自定义电视资讯服务器，以及AMISERV微服务器协会的成立。他还讨论了他的公司JCA，该公司将Cristel商业化并扩展了COMPUTEL服务器。

文章随后跳转到2012年，在Télétel自助服务终端正式关闭后，概述了作者重新燃起对复活服务器的兴趣。快进到2017年，他成功地使用修复后的Apple II硬件和软盘模拟器恢复了COMPUTEL系统，克服了诸如寻找可用的硬件和可读备份等挑战。

一个关键障碍是建立可靠的电话线，通过使用配置为最佳调制解调器调制的VOIP适配器解决了这个问题。复活后的COMPUTEL服务器现在可以通过+33 1 8421 8116访问。作者强调了保护Minitel时代技术和知识的重要性。

最后，奎斯特概述了潜在的未来项目，包括升级Cristel，恢复基于Macintosh的Dragster服务器，开发Python版本的Cristel，甚至在法国建立Minitel博物馆。他希望鼓励微服务器的复兴，利用Raspberry Pi和经济实惠的VOIP线路等现代技术。

---

## 51. 苹果和Meta因违反欧盟法律被处以数百万美元罚款

**原文标题**: Apple and Meta fined millions for breaching EU law

**原文链接**: [https://ca.finance.yahoo.com/news/apple-fined-570-million-meta-094701712.html](https://ca.finance.yahoo.com/news/apple-fined-570-million-meta-094701712.html)

欧盟因违反《数字市场法案》(DMA) 对苹果公司处以 5 亿欧元罚款，对 Meta 公司处以 2 亿欧元罚款。该法案旨在遏制大型科技公司的权力，标志着 DMA 下的首批制裁，并引来美国批评，白宫称之为“经济勒索”。

罚款源于一项为期一年的调查，调查内容是这些公司是否允许规模较小的竞争对手进入其主导的市场。尽管美国总统特朗普誓言捍卫美国公司，欧盟仍在强制执行新规。谷歌和 X 也面临欧盟潜在的罚款。

苹果公司因限制应用程序开发者引导用户访问 App Store 以外的更优惠交易，以及阻止用户侧载应用程序而被罚款。苹果公司计划对罚款提出质疑，认为欧盟不公平地针对他们，并迫使他们免费提供技术。

Meta 的“付费或同意”模式，即向用户提供付费的无广告服务或带有定向广告的免费服务，被认为是违反了 DMA 的行为。Meta 正在与欧盟讨论该模式的修订版本。Meta 也批评了欧盟的决定，称其对美国企业不公平。

虽然与欧盟过去的反垄断处罚相比，这些罚款被认为是适度的，但这些公司有两个月的时间来遵守规定，否则将面临每日罚款的风险。欧盟还结束了一项对苹果浏览器选项的调查，此前苹果公司做出了更改，允许用户更轻松地切换到竞争对手的浏览器或搜索引擎。

---

## 52. 我是如何使用 Obsidian、Hugo、GitHub 和 Cloudflare 写博客的

**原文标题**: How I blog with Obsidian, Hugo, GitHub, and Cloudflare

**原文链接**: [https://ingau.me/blog/how-i-write-my-blogs-in-obsidian-and-publish-instantly/](https://ingau.me/blog/how-i-write-my-blogs-in-obsidian-and-publish-instantly/)

本文概述了一个使用Obsidian、Hugo、GitHub和Cloudflare Pages进行博客写作的工作流程，提供了一个快速、免费且可移植的发布过程。作者强调了这种设置的优势：在Obsidian中进行本地优先写作、完全控制内容以及没有供应商锁定。

该过程包括设置静态站点生成器Hugo，并通过将Obsidian的库指向Hugo的content/blog目录，将其连接到Obsidian。这允许直接写入正确的文件夹以供Hugo处理。作者详细介绍了在Obsidian中设置Front Matter模板（包括关键的`draft`标志），使用Hugo的服务器在本地预览文章，并将本地Hugo站点连接到GitHub仓库。

最后，该指南解释了如何使用Cloudflare Pages部署博客，Cloudflare Pages会在每次将更改推送到GitHub仓库时自动构建和部署站点。指定了Cloudflare Pages中的构建设置：构建命令为`hugo --minify`，构建输出目录为`public`。

发布工作流程简化为只需更改Obsidian笔记的Front Matter中的`draft`标志，提交更改并将其推送到GitHub，从而触发Cloudflare Pages的自动重建和部署。作者最后强调，最初的设置投入是值得的，因为它可以带来无摩擦、无费用且完全可控的长期博客体验。

---

## 53. 人工智能胜过病毒专家，引发生物危害担忧

**原文标题**: AI Bests Virus Experts, Raising Biohazard Fears

**原文链接**: [https://time.com/7279010/ai-virus-lab-biohazard-study/](https://time.com/7279010/ai-virus-lab-biohazard-study/)

人工智能模型在解决复杂湿实验室问题上超越病毒学博士，引发生物安全担忧

---

## 54. 帆船时代的船上啤酒 (2017)

**原文标题**: Beer on Board in the Age of Sail (2017)

**原文链接**: [https://blog.library.si.edu/blog/2017/08/02/beer-board-age-sail/](https://blog.library.si.edu/blog/2017/08/02/beer-board-age-sail/)

茱莉亚·布莱克利的《风帆时代船上的啤酒》探讨了啤酒作为水手主食的历史意义。文章追溯了啤酒从古代美索不达米亚起源到被航海文化，特别是英国皇家海军所采用的历史。

啤酒不仅是营养和热量的来源，而且是通常受污染的水的更安全替代品。文章重点介绍了塞缪尔·佩皮斯详细的口粮，以及啤酒作为一种健康饮料的观念，并引用了约翰·普林格尔爵士关于饮用啤酒预防坏血病的观察。虽然16世纪的荷兰水手发现啤酒和水果可以预防坏血病，但詹姆斯·林德的研究使这一概念被广泛接受。

文章讨论了啤酒在北欧的使用，以及在温暖气候下向葡萄酒和朗姆酒的过渡。它提到了美国海军最终禁止酒精。文章还深入探讨了美国的背景，注意到新英格兰和新阿姆斯特丹早期的酿酒活动。

文章的重要部分集中于在船上酿造云杉啤酒，特别是在探险期间，强调了它在预防坏血病方面的作用，这种做法源于美洲原住民的传统。文章以路易斯·巴斯德关于啤酒发酵的研究及其对在长途航行中保存啤酒的影响作结。

最后，文章还涉及了一些英语短语的航海起源，并提到了史密森尼图书馆与海事和啤酒历史相关的丰富馆藏。

---

## 55. Lucene大学

**原文标题**: Lucene University

**原文链接**: [https://github.com/msfroh/lucene-university](https://github.com/msfroh/lucene-university)

Lucene大学：一个自包含的Apache Lucene示例库，专为学习和实验而设计。它在Markdown中提供详细的代码注释，便于理解Lucene的功能。目标是提供实用的代码示例，可通过多种方式使用：阅读源代码、使用IDE调试或访问使用Docco生成的网页。

该库依赖于Lucene 10，需要JDK 21或更高版本。入门包括克隆存储库、使用Gradle构建或导入IntelliJ。欢迎贡献，准则强调使用仅包含Lucene和Java类的自包含代码示例、演示该功能的`main`方法以及总结该示例的头部注释。所有代码均在Apache License 2.0许可下发布。

---

## 56. Show HN: Index – 新的开源浏览器代理

**原文标题**: Show HN: Index – New Open Source browser agent

**原文链接**: [https://github.com/lmnr-ai/index](https://github.com/lmnr-ai/index)

Index是一款新型开源浏览器代理，旨在利用具备视觉能力的推理LLM在网络上自主执行复杂任务。它支持Gemini 2.5 Pro/Flash、Claude 3.7 Sonnet和OpenAI o4-mini等模型。

用户可以通过`pip install lmnr-index`安装Index，并通过交互式CLI (`index run`)与之交互。它也可以作为由Laminar管理的无服务器API使用，用于生产环境，提供远程浏览器会话、代理基础设施和可观察性。Laminar提供了一个追踪代理行为和记录浏览器会话的平台。

文档详细介绍了各种用例：使用API、快速本地设置、流式输出、启用浏览器可观察性、使用远程CDP URL运行以及自定义浏览器窗口大小。本地设置需要安装依赖项(`pip install lmnr-index`和`playwright install chromium`)，在`.env`文件中设置API密钥，然后运行`index run`。提供了示例代码片段，说明如何以编程方式使用Index、流式传输代理的输出以及集成Laminar以实现可观察性。代理可以使用特定的LLM进行配置，并且可以自定义浏览器配置，例如CDP URL和视口大小。

---

## 57. 为何选择C#？

**原文标题**: Why C#?

**原文链接**: [https://newsletter.techworld-with-milan.com/p/why-csharp](https://newsletter.techworld-with-milan.com/p/why-csharp)

米兰·米兰诺维奇博士的《为什么选择 C#？》一文探讨了 C# 作为一种编程语言，其持久流行和多功能性背后的原因。文章首先强调了 C# 从 Java 竞争者到现代多范式语言的演变。

文章详细介绍了 C# 的核心特征：其现代性、类型安全、多范式方法（面向对象、命令式、声明式和函数式）、面向组件的设计、跨平台能力、多功能性、开源性以及可读性。它讨论了从 C# 1.0 到 C# 13.0 的 C# 时间线。

文章深入探讨了 C# 的关键特性，包括其面向对象的基础（封装、继承、多态）、高级类型系统（泛型、可空类型）、用于函数式编程的 Lambda 表达式以及用于声明式数据查询和操作的 LINQ（语言集成查询）。它进一步解释了 async/await 对于简化异步编程的重要性，使非阻塞操作更易于管理。

文章还涉及 .NET 生态系统、工具（Visual Studio、VS Code、Rider、.NET CLI）、库（标准 .NET 库和 NuGet 包）、文档和社区。最后，它简要地将 C# 与其他语言（如 Java、Python、F# 和 JavaScript/TypeScript）进行比较，并讨论了 C# 的未来发展和微软的愿景。结论重申了 C# 适用于各种开发场景。

---

## 58. 基于进化算法的自动化天线设计 [pdf] (2006)

**原文标题**: Automated Antenna Design with Evolutionary Algorithms [pdf] (2006)

**原文链接**: [https://ntrs.nasa.gov/api/citations/20060024675/downloads/20060024675.pdf](https://ntrs.nasa.gov/api/citations/20060024675/downloads/20060024675.pdf)

**《基于演化算法的自动天线设计》（2006）摘要**

这份 NASA 技术备忘录探讨了使用演化算法（EA），特别是遗传算法（GA），进行天线的自动设计和优化。论文针对天线设计日益增长的复杂性以及传统人工驱动方法的局限性进行了阐述。作者认为，演化算法提供了一种强大的替代方案，它能够在无需大量先验知识或依赖人类直觉的情况下，探索复杂的设计空间。

论文概述了遗传算法的基本原理及其在天线设计中的应用。该过程包括将天线几何形状表示为参数字符串（基因），使用电磁（EM）仿真软件（例如 NEC、HFSS）评估每个天线设计的性能，然后使用 GA 算子（如选择、交叉和变异）迭代改进设计种群。用于选择的适应度函数基于所需的天线性能指标，例如增益、带宽、阻抗匹配和辐射方向图特性。

论文展示了几个案例研究，以证明该方法的有效性。这些例子涵盖了不同类型的天线，包括微带天线、线天线和反射面天线。结果表明，演化算法可以成功设计出满足特定性能要求的天线，通常能够达到或甚至超过通过传统方法获得的设计性能。论文强调了演化算法发现人类设计师可能无法构思的新颖和意想不到的天线几何形状的能力。

最后，论文讨论了使用演化算法进行自动天线设计所面临的挑战和未来方向。这些挑战包括电磁仿真的计算成本、对高效编码方案的需求，以及开发更强大和自适应的 GA 算子。作者总结说，演化算法通过自动化流程、缩短设计时间并支持创新天线概念的探索，为革新天线设计提供了巨大的潜力。

---

## 59. 像素是一种长度和面积单位。

**原文标题**: Pixel is a unit of length and area

**原文链接**: [https://www.nayuki.io/page/pixel-is-a-unit-of-length-and-area](https://www.nayuki.io/page/pixel-is-a-unit-of-length-and-area)

本文探讨了数字图像中“像素”作为长度单位和面积单位的冲突用法。从数学角度讲，像素长度相乘得到平方像素（像素²），这与标准量纲分析一致。然而，口语化的用法将像素视为面积的直接度量（例如，百万像素），这意味着像素² = 像素，从而导致像素 = 1 这一荒谬的结论。

作者提出了两种解决这种矛盾的不完美方案：

1. **将像素定义为正方形：** 像素的物理尺寸取决于设备/标准，“像素边长”（或 √像素）代表线性单位。这承认了像素固有的面积。
2. **坚持像素是长度单位：** 所有面积必须用“平方像素”来表示，避免非正式地使用“百万像素”，并面临表示大量像素计数的挑战，或诉诸诸如“平方千像素”之类笨拙的术语。

尽管存在逻辑上的不一致，但作者承认实际影响有限，因为像素不是一个公制单位，并且除了“每米像素”之类的比率之外，不会在复杂的计算中使用。本文强调了单位定义中数学严谨性与常见用法之间的差异，类似于英制单位“磅”中质量和力的混淆。

---

## 60. MinC 不是 Cygwin

**原文标题**: MinC Is Not Cygwin

**原文链接**: [https://minc.commandlinerevolution.nl/english/home.html](https://minc.commandlinerevolution.nl/english/home.html)

MinC：一款用于Windows的Unix模拟器，专为教育目的而设计，旨在帮助儿童学习Linux，无需虚拟化。 与Cygwin不同，MinC基于OpenBSD操作系统。 它兼容Windows NT及更高版本（2003/XP/Vista/7/8/10/11）。 MinC具有非常小的内核（285Kb），可以直接在Windows上运行。 系统的其余软件直接来源于OpenBSD 6.1版本。 这使得用户可以在他们的Windows电脑上以原生速度体验OpenBSD。

---

## 61. ZGC如何为Java堆分配内存

**原文标题**: How ZGC allocates memory for the Java heap

**原文链接**: [https://joelsiks.com/posts/zgc-heap-memory-allocation/](https://joelsiks.com/posts/zgc-heap-memory-allocation/)

本文深入探讨了OpenJDK中垃圾回收器ZGC如何为Java堆分配内存。ZGC将内存组织成三种大小的页：小页（2MB）、中页（32MB）和大页（动态大小，>4MB）。页分配器管理堆，维护一个或多个分区。在启用NUMA的NUMA系统上，使用多个分区，映射到NUMA节点以提高内存访问速度。否则，单个分区管理整个堆。

ZGC分离物理内存和虚拟内存以对抗碎片化。虚拟内存被过度预留（高达最大堆大小的16倍或32倍），增加了找到连续内存的机会。大页在释放时通过将物理内存重新映射到较低的内存区域来进行碎片整理。

映射缓存使用侵入式存储将未使用的、已提交的和已映射的内存范围存储在自平衡树中，避免了动态内存分配。它通过合并相邻的虚拟内存来维护尽可能大的连续范围，并使用大小类来加速搜索。分配内存首先涉及声明容量。它首先尝试直接从映射缓存中获取连续内存，这是小页最常见的快速路径。如果失败，ZGC会通过提交新的物理内存来增加容量。作为最后的手段，ZGC会从缓存中收集较小的内存范围。

---

## 62. 回声播放器：回声 – 开源硬件音乐播放器

**原文标题**: Echoplayer: Echo – Open Hardware Music Player

**原文链接**: [https://github.com/amachronic/echoplayer](https://github.com/amachronic/echoplayer)

Echo：一个开源硬件音乐播放器项目，旨在利用自由软件（主要是 Rockbox）实现高质量音频回放。该项目采用 KiCAD 8.0 进行电路设计和 PCB 布局，计划使用 FreeCAD 设计 3D 打印外壳。所有设计均采用 CERN-OHL-S v2 许可。

当前版本 Echo R1 采用紧凑型设计 (60x100x15mm)，配有方向键、多功能按钮、专用音量和电源按钮以及锁定开关。它包括两个 3.5 毫米耳机插孔（支持麦克风输入和线控）和一个专用线路输出。 它支持通过可移动存储卡扩展至高达 2 TiB 的存储空间，并使用 USB-C 进行充电和文件传输 (USB 2.0)。 设备由可更换的 BL-5C 电池供电。

硬件规格包括 STM32H743 CPU、32 MiB SDRAM、TLV320AIC3104 音频芯片、320x240 2.3 英寸 LCD 以及带唤醒闹钟的 RTC。

Rev1 原型 PCB 已完成，但存在已知问题，包括无法禁用的背光（电流限制设置过低）和杂乱无章的原理图参考指示符。开发重点是移植 Rockbox 和设计可用的外壳。 下一个版本将解决已发现的问题。该项目版权归 Aidan MacDonald 所有，并采用 CERN-OHL-S v2 许可。

---

## 63. 考拉兹蚂蚁

**原文标题**: Collatz's Ant

**原文链接**: [https://gbragafibra.github.io/2025/01/08/collatz_ant2.html](https://gbragafibra.github.io/2025/01/08/collatz_ant2.html)

本文探讨了柯拉茨序列的可视化，并类比于兰顿蚂蚁。柯拉茨蚂蚁遵循柯拉茨函数：如果一个数字是偶数，则除以2，蚂蚁顺时针旋转90º；如果为奇数，则乘以3，加1，蚂蚁逆时针旋转90º。蚂蚁每步前进一个单位，并且它落脚的单元格可以翻转其状态或仅增加其计数。

本文展示了不同起始数字的蚂蚁轨迹，突出了相似景观与停止时间之间的相关性。然而，它指出逆命题并不总是成立：序列可能具有相同的停止时间，但不会产生相似的景观。作者通过示例展示了这一点，并使用Python代码测量柯拉茨序列之间共享元素的数量来量化轨迹相似性。

此外，本文还研究了子轨迹的早期收敛如何影响蚂蚁的景观。它观察到，以较小的步差收敛的轨迹表现出相似的景观，通常彼此相对旋转。随着步差的增加，景观变得越来越不相似，仅保留较大规模的特征。这种可视化方法和观察结果提供了一种可视化的方式来比较和理解柯拉茨序列的行为。

---

## 64. 循环节与倒数

**原文标题**: Reptends and Reciprocals

**原文链接**: [https://www.gregegan.net/SCIENCE/Reptends/Reptends.html](https://www.gregegan.net/SCIENCE/Reptends/Reptends.html)

格雷格·伊根的《循环节与倒数》探讨了一个引人入胜的问题：是否存在这样一些整数，它们的倒数具有这样的十进制表示，其循环节包含给定进制的所有数字恰好一次，称为“非冗余全数字循环节”？

文章展示了通过计算机搜索在2、4、6、10、12、14、18、20、22、24、26和30进制下找到的此类整数的几个例子。它提供了已知（或目前已知）的对于每个进制来说，其倒数具有这种性质的最小整数。

随后，伊根深入研究了数论，给出了部分解答，证明除了3进制之外，对于奇数进制不存在解，同时表明3进制也没有这样的倒数。该证明涉及模算术和可除性规则。

对于偶数进制，文章描述了一种计算机搜索方法，该方法对一个关键方程的右侧进行因式分解，该方程是从重复小数的几何级数表示中推导出来的。这种方法允许枚举循环节的可能值，并检查它们是否是非冗余全数字整数。文章利用这种方法表明，8、16、32和64进制没有这样的解。

文章最后指出，尽管发现了这些结果，但识别所有允许具有非冗余全数字循环节的倒数的进制这一总体问题仍然是一个未解决的问题。

---

## 65. Show HN: Rowboat – 多智能体系统的开源IDE

**原文标题**: Show HN: Rowboat – Open-source IDE for multi-agent systems

**原文链接**: [https://github.com/rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat)

Rowboat：开源IDE，用于快速构建和部署多智能体系统。它利用OpenAI Agents SDK，提供了一种创建人工智能驱动型工作流程的简化方法。用户可以使用自然语言提示描述所需的代理，Rowboat的副驾驶将自动生成多智能体工作流程，包括必要的工具。

主要功能包括：

*   **轻松创建工作流程：** 从自然语言提示创建多智能体工作流程。
*   **MCP服务器连接：** 集成现有的MCP（多智能体协作平台）服务器及其工具。
*   **集成灵活性：** 提供HTTP API和Python SDK，可无缝集成到现有应用程序中。
*   **开源：** 允许自定义和社区贡献。

该文章提供了一个快速入门指南，包括设置OpenAI API密钥、克隆存储库以及使用Docker运行应用程序的说明。它通过HTTP API（使用`curl`）和Python SDK的代码示例演示了集成选项。SDK允许与代理进行有状态（推荐）和无状态交互。最后，该文章鼓励用户查阅文档，以获取有关使用Rowboat构建代理的更多说明。

---

## 66. 地理编码API对比：定价、免费额度和使用条款

**原文标题**: Geocoding APIs compared: Pricing, free tiers and terms of use

**原文链接**: [https://www.bitoff.org/geocoding-apis-comparison/](https://www.bitoff.org/geocoding-apis-comparison/)

本文对比了流行的地理编码API（HERE、Google Maps、Azure Maps、OpenCage、TomTom Maps、LocationIQ和Nominatim），基于定价、免费额度和使用条款。旨在通过概述不同使用量相关的成本，帮助用户为其项目选择最合适的API。

比较涵盖：

*   **定价：** 每1000次API请求的成本以及提供的不同定价等级。
*   **免费额度：** 每月或每日可用的免费请求数量，适用于测试或低预算项目。
*   **数据使用条款：** 数据使用限制，包括署名要求和商业用途限制。

文章还提到准确性和性能将在后续文章中介绍。

主要结论：

*   Azure Maps和Google Maps Platform是最昂贵的选项，但Google Maps提供慷慨的免费额度以及较高的每秒请求速率限制。然而，Google Maps需要署名并限制数据在其平台上的使用。
*   OpenCage和LocationIQ提供每月固定价格计划，LocationIQ提供更慷慨的免费额度。LocationIQ的最大计划支持高容量。
*   TomTom Maps提供适用于商业用途的慷慨免费额度。
*   HERE适用于极高容量的使用。
*   Nominatim是免费且开源的，非常适合小型非商业项目。

文章最后对小型、中型和高使用场景进行了定价比较。指出最佳选择取决于个人项目需求和使用模式。作者还提供了更多资源，用于进一步比较和测试地理编码提供商。

---

## 67. 为什么我的eBPF程序在一个内核上工作但在另一个内核上失败？

**原文标题**: Why Does My eBPF Program Work on One Kernel but Fail on Another?

**原文链接**: [https://ebpfchirp.substack.com/p/why-does-my-ebpf-program-work-on](https://ebpfchirp.substack.com/p/why-does-my-ebpf-program-work-on)

无法访问文章链接。

---

## 68. 最高分填字游戏棋盘的计算证明

**原文标题**: A Computational Proof of the Highest-Scoring Boggle Board

**原文链接**: [https://www.danvk.org/2025/04/23/boggle-solved.html](https://www.danvk.org/2025/04/23/boggle-solved.html)

Dan Van der Kamp完成了最高分4x4拼字游戏盘的计算证明，结束了长达20年的探索。最佳棋盘“plsteaiertnrsges”使用ENABLE2K词汇表获得3625分，超过了所有其他可能的字母组合。这是一项重大成就，因为之前的高分棋盘是通过爬山法确定的，这种方法可能会陷入局部最优，而不能保证全局最大值。

该证明是通过采用“分支定界”技术的穷举搜索实现的。这种方法将大量可能的拼字游戏盘（超过5*10^21）划分为“棋盘类”，计算每个类的得分上限。上限低于3625的类被丢弃，大大缩小了搜索空间。定制的“和/选择”树结构有助于高效地计算上限和分割类。

该计算在拥有192个核心的Google Cloud实例上耗时五天。结果产生了一个超过3500分的32个棋盘的列表，证实了通过早期爬山法找到的顶级棋盘确实是全局最优解。作者指出，该算法的有效性突显了深度爬山法可以在拼字游戏中找到全局最优解，并探讨了有关人工智能参与、真实拼字游戏骰子排列以及替代词汇表的影响的问题。他认为该方法可以应用于其他语言，但承认更大的拼字游戏盘（5x5, 6x6）对未来提出了巨大的计算挑战。

---

## 69. Dauug之家 - Dauug|36小型计算机文档

**原文标题**: The Dauug House - Dauug|36 minicomputer documentation

**原文链接**: [https://dauug.cs.wright.edu/](https://dauug.cs.wright.edu/)

Dauug|36 迷你计算机是一种 36 位开源架构，专为自制 CPU 和控制器而设计。与传统计算机不同，它无需微处理器或半导体代工厂即可实现，只需基本组件和焊接。它具有分页虚拟内存、抢占式多任务处理和丰富的指令集等功能。

Dauug|36 优先考虑用户控制和安全性。用户拥有完全的访问权限和可见性，可以检查和电气验证每个组件。其设计通过排除 DRAM、内存缓存、推测执行和乱序执行，避免了常见的漏洞，如 Rowhammer、Spectre 和 Meltdown。堆栈是隔离的，防止堆栈粉碎攻击，并且算术溢出/下溢由持久标志处理。它通过无缝处理有符号/无符号变量来简化编程。

一个关键的设计理念是在不依赖持续更新的情况下实现长期的可靠性和安全性。该架构最大限度地降低了复杂性，避免了常见的安全隐患，并公开其设计。其目标是创建一个从一开始就具有固有安全性，而非依赖于未来补丁的计算机，从而在整个生命周期内保持安全。这使其适用于需要长期稳定性的关键应用。

---

## 70. MOS 6502非法操作码工作原理 (2008)

**原文标题**: How MOS 6502 Illegal Opcodes Work (2008)

**原文链接**: [https://www.pagetable.com/?p=39](https://www.pagetable.com/?p=39)

本文解释了MOS 6502处理器最初的NMOS版本中未记录的“非法操作码”的起源和行为。与一些依赖微代码的CPU不同，6502使用可编程逻辑阵列（PLA）或解码ROM来根据操作码和当前时钟周期（T1-T7）解释指令。

PLA由检查特定操作码和周期组合的线路组成。当一条线路匹配时，它会触发控制信号来管理各种CPU组件，从而导致特定操作。操作码表的设计具有模式，允许线路为多个相似的操作码触发。

非法操作码的出现是因为未定义的操作码仍然可以触发现有的PLA线路，因为它们与定义的操作码相似。本文用“$AF”操作码“LAX absolute”为例来说明这一点，它类似于“LDA abs”和“LDX abs”的组合。由于$AF在特定的时钟周期与LDA和LDX共享PLA线路，因此它可以有效地同时执行这两种操作，将该值加载到累加器（A）和X寄存器中。

本文还解释了“KIL”操作码，这些操作码会暂停CPU。这些操作码阻止T位域（表示当前时钟周期）在指令结束时被重置。因此，CPU陷入循环中，禁用中断和NMI，因为它们依赖于T位域在被确认之前被重置。缺乏重置导致处理器变得无响应，并且处理器需要完全重置才能恢复。

---

## 71. QEMU 10.0.0 版本发布

**原文标题**: QEMU Version 10.0.0 Released

**原文链接**: [https://www.qemu.org/2025/04/23/qemu-10-0-0/](https://www.qemu.org/2025/04/23/qemu-10-0-0/)

QEMU 10.0.0版本发布，包含211位贡献者的超过2800个提交。此版本的主要亮点包括：

*   **块设备 (Block):** Virtio-scsi 多队列支持，允许不同的 I/O 线程处理每个队列的请求。
*   **VFIO:** 改进了对 Intel Gen 11/12 设备上 IGD 直通的支持。
*   **文档 (Documentation):** 对 QEMU 机器协议文档进行了重大改进和彻底修改，以提高清晰度和组织性。
*   **ARM:** 支持 EL2 物理和虚拟定时器、FEAT_AFP、FEAT_RPRES 和 FEAT_XS 架构特性的仿真，以及 NPCM8445 评估和 i.MX 8M Plus EVK 板的新板模型。
*   **HPPA:** 新 SeaBIOS-hppa 版本 18，翻译速度和虚拟 CPU 重置改进，以及 Diva GSP BMC 板的仿真支持。
*   **LoongArch:** 支持 CPU 热插拔、半虚拟化 IPI、KVM 窃取时间计算和虚拟 'extioi' 中断路由。
*   **RISC-V:** 支持各种特性的 ISA/扩展，以及 Ascalon 和 RV64 Xiangshan Nanhu CPU 以及 Microblaze V 板的仿真。
*   **s390x:** 支持第 17 代大型机 CPU 的 CPU 模型。
*   **s930x:** 支持 virtio-mem 以及绕过 IOMMU。
*   **x86:** 支持 Clearwater Forest 和 Sierra Forest v2 的 CPU 模型，以及更快地仿真字符串指令。

此次发布还感谢开发人员、错误报告者、文档编写者、测试人员以及提供 CI 资源的人员的贡献。

---

## 72. 給人們一些值得觀看的東西 (2021)

**原文标题**: Give People Something to Look At (2021)

**原文链接**: [https://staysaasy.com/communication/2021/10/30/look.html](https://staysaasy.com/communication/2021/10/30/look.html)

当人们除了共同的兴趣爱好之外，还有一个共同关注的对象或活动时，对话会变得更加轻松，本文探讨了这一现象。作者最初认为，拥有一个活动或共同的兴趣是这种轻松感的主要驱动力，但现在认为，有东西可看起着至关重要的作用。

如果没有焦点，由于直接的眼神接触和过度分析对方的反应所带来的压力，对话可能会变得尴尬。共同的视觉焦点，比如散步时的小路、游戏板或电视屏幕，可以缓解这种压力，从而可以进行更自然的停顿，减少焦虑。作者引用了遛狗者和体育酒吧等例子来说明这一原则。

然后，他们描述了如何在工作环境中将他们的假设付诸实践。通过在面试期间让某人写在白板上，或在小组会议期间在屏幕上展示笔记，他们创造了一个共同的视觉焦点，从而减少焦虑并促进协作。同样，在单人会议期间展示笔记可以提供一个焦点，并确保准确的记录。文章最后提出，“给人们一些东西看”是在个人和职业环境中实现更轻松、更富有成效的对话的捷径。

---

## 73. 操作 Petabyte 级 ClickHouse 集群的经验教训：第二部分

**原文标题**: Lessons learned operating petabyte-scale ClickHouse clusters: Part II

**原文链接**: [https://www.tinybird.co/blog-posts/what-i-learned-operating-clickhouse-part-ii](https://www.tinybird.co/blog-posts/what-i-learned-operating-clickhouse-part-ii)

本文是系列文章的第二篇，重点介绍运营PB级ClickHouse集群所面临的挑战，特别是读取性能和运营方面的考虑。 它强调了读写之间的相互依赖性，并强调由于表中part的数量，导入模式会影响读取性能。

涵盖的主要主题包括：

*   **处理不同流量：** 管理实时、长时间运行和回填查询的策略，包括使用负载均衡器和应用程序逻辑将查询定向到适当的副本。
*   **查询设计：** 查询优化的重要性，特别是设置 `max_threads`、`max_memory` 和 `max_bytes_before_external_group_by`。 优先对排序键列进行过滤，使用 `PREWHERE` 进行高选择性过滤，并推迟复杂的运算，如 `JOINs` 和 `GROUP BYs`。
*   **回填：** 建议不要使用 `POPULATE` 回填物化视图，因为它可能导致数据重复。 建议使用 Null 表，并在回填期间增加每个块的行数。
*   **集群运营和监控：** 强调了除了基本的 CPU 和内存之外，还需要监控的关键指标，如查询计数、ZooKeeper 延迟、S3 错误、复制延迟和队列长度。 强调掌握 ClickHouse 系统表（如 `system.query_log`、`system.processes` 和 `system.part_log`）对于故障排除的重要性。
*   **其他注意事项：** 小心表删除、物化视图、某些列类型（如具有高基数的 `uniqExactState`）和 `ON CLUSTER` 操作。 对于低延迟用例，预热缓存并监控 `mark_cache` 的可用内存。

文章最后强调，虽然存在挑战，但 ClickHouse 仍然是一个强大的数据库，并且经验对于大规模处理它至关重要。 建议将 Altinity 的知识库作为宝贵资源。

---

## 74. π0.5：具有开放世界泛化能力的VLA

**原文标题**: π0.5: A VLA with open-world generalization

**原文链接**: [https://pi.website/blog/pi05](https://pi.website/blog/pi05)

本文介绍π0.5，一种新型视觉-语言-动作(VLA)模型，专为机器人开放世界泛化而设计，尤其是在像家庭这样的非结构化环境中。与之前难以适应新环境的模型不同，π0.5在泛化到未见环境方面表现出显著的提升，使其能够在新的家庭中执行诸如清洁厨房和卧室之类的任务。

π0.5背后的关键创新是其在异构数据上的协同训练方法。通过在各种数据源上训练模型，包括来自不同机器人类型的机器人动作数据、多模态网络数据、口头指令、目标检测数据和子任务命令，π0.5学习理解任务的语义上下文，推断高级任务结构，并迁移物理行为。这种多样化的训练使其能够在多个层面进行泛化，从物理灵巧性到视觉理解和语义推理。

实验表明，π0.5在新环境中实现了高成功率和语言跟随率。消融研究表明，网络数据对于识别新对象至关重要，而来自其他机器人的数据显著提高了整体性能。缩放研究表明，性能随着训练环境数量的增加而提高，最终接近直接在测试环境中训练的模型的性能。

π0.5采用分层方法，以文本形式做出高级动作决策，然后通过流匹配生成低级电机命令。这使得机器人能够在新的环境中执行复杂的、长时程的任务，展现出灵活性和足智多谋。

---

## 75. Vim语言、移动和模式详解 (2023)

**原文标题**: Vim Language, Motions, and Modes Explained (2023)

**原文链接**: [https://www.ssp.sh/blog/why-using-neovim-data-engineer-and-writer-2023/](https://www.ssp.sh/blog/why-using-neovim-data-engineer-and-writer-2023/)

本文提倡学习 Vim，强调其效率和可定制性，尽管初始学习曲线陡峭。作者是一位曾使用其他编辑器的开发者，发现 Vim 显著提高了他们的工作流程速度和生产力。Vim 威力的核心在于其“Vim 语言”，一种动词、主语和宾语的语法结构，可以将少量命令组合成数百种组合。作者将 Vim 移动描述为在编辑器内导航的方式。Vim 的模态编辑，包括普通模式、插入模式、可视模式和命令模式，允许用户通过优化的击键在编码、编辑和操作文本及文件之间切换。

本文讨论了不同的 Vim 选择，包括 Vim、Neovim 和 LunarVim，偏爱 Neovim，因为它拥有插件生态系统和 Lua 配置。作者详细介绍了 Vim 如何改进他们的数据工程和写作工作流程，重点介绍了特定的插件和配置。作者指出，学习 Vim 可以扩展到编辑器本身之外，从而提高终端使用和 Linux 技能。他们建议在完全深入 Vim 之前，在当前编辑器中激活 Vim 模式，以简化过渡。最终，作者认为 Vim 对于任何花费大量时间写作或编码的人来说都是一个强大的工具，可以实现“以思维的速度”进行编辑。

---

## 76. 喜欢独自游戏？育碧仍在关注你

**原文标题**: Like to play alone? Ubisoft is still watching you

**原文链接**: [https://noyb.eu/en/play-alone-ubisoft-still-watching-you](https://noyb.eu/en/play-alone-ubisoft-still-watching-you)

Noyb针对育碧提起GDPR申诉，指控其强制用户连接互联网才能玩单人游戏，即使这些游戏不具备在线功能。这使得育碧得以收集玩家行为数据，包括游戏启动/停止时间和游戏时长，而未获得GDPR第6条第1款规定的有效法律依据。

该申诉源于一位在Steam上购买了《孤岛惊魂：原始杀戮》的用户，他被强制登录育碧账户才能进行游戏。该用户的调查显示，游戏在10分钟内连接外部服务器150次，向Google、Amazon和Datadog发送数据。育碧的客户支持声称这是为了验证所有权，但也引用了最终用户许可协议（EULA）和隐私政策，其中声明数据收集是为了改善游戏体验和第三方分析。

Noyb认为这种数据收集是不必要的，因为所有权已经通过Steam验证，并且育碧提供了一个隐藏的离线模式。他们认为，如果育碧想要数据来改善游戏，应该请求用户同意或提交错误报告，而不是默认实施持续跟踪。他们要求奥地利数据保护局（DSB）宣布育碧违反GDPR第6条第1款，命令删除非法处理的个人数据，停止非法处理行为，并根据育碧的收入处以高达9200万欧元的罚款。

---

## 77. 御嶽山

**原文标题**: Mt Ontake

**原文链接**: [https://www.emgoto.com/mt-ontake/](https://www.emgoto.com/mt-ontake/)

本文详细介绍了攀登御岳山（日本百名山之一）的经历，重点介绍了实际信息以及这座山悲惨的历史。本文于2025年4月更新，将御岳山描述为一座交通便利的3067米高峰，可以从东京出发进行一日徒步旅行（约5小时），可以选择从王滝或御岳索道起点徒步。

作者于2024年10月攀登了御岳山，重点介绍了这座山荒凉的火山地貌、紧急避难所和因其活跃火山状态而设置的标牌。文章回顾了2014年造成63名徒步者死亡的毁灭性火山爆发，强调了安全措施（如头盔）的重要性。

实用信息包括通过公共交通和汽车的交通方式，并建议从东京出发自驾更容易。文章还提供了从木曽福岛站到两个起点的巴士时刻表信息，以及两个可供过夜的山间小屋的信息。

除了徒步旅行本身，文章还强调了灾难的情感冲击，分享了受影响者的故事，并敦促徒步旅行者记住遇难者。文章最后提供了徒步旅行的详细信息，包括路线长度和时间，以及住宿建议，例如起点附近的泷见馆旅馆。

---

## 78. 鲸鸣预警：AI系统提醒船舶避让鲸鱼

**原文标题**: Ping, You've Got Whale: AI detection system alerts ships of whales in their path

**原文链接**: [https://www.biographic.com/ping-youve-got-whale/](https://www.biographic.com/ping-youve-got-whale/)

本文介绍了鲸鱼观察者（WhaleSpotter），一种人工智能驱动的鲸鱼探测系统，旨在防止船舶与鲸鱼相撞。该系统由伍兹霍尔海洋研究所的丹尼尔·齐特巴特开发，利用热感摄像机和神经网络实时识别鲸鱼喷出的水柱。人工智能系统会向远程专家发出警报，专家随后进行验证并将警告转发给船舶，以便船长改变航向。

鲸鱼观察者已经在包括渡轮、研究船和游轮在内的各种船只上进行了测试，自 2019 年以来，其探测能力显著提高。虽然较小的船只已经收到警报，但现在的重点正在转向集装箱船，由于其体积和机动性，集装箱船对鲸鱼构成重大威胁。

为集装箱船调整这项技术涉及使用远程摄像机和专门的稳定装置，利用船舶的高度来发现长达 6 公里外的鲸鱼。马森航运公司正在与齐特巴特合作，测试和改进该系统，以应用于其船队。

海洋生物学家约翰·卡拉姆博基迪斯虽然承认改变航线和降低速度的重要性，但强调了实时探测的潜力，尤其是在热感摄像机最有效的夜间。鲸鱼观察者的目标是通过包括人工验证来最大限度地减少误报，确保船长收到准确且可操作的警报。齐特巴特设想建立一个船舶网络，共享实时信息，以保护鲸鱼并拯救像北大西洋露脊鲸这样的濒危物种。

---

## 79. “蒙眼打击犯罪”：欧洲正盯上加密技术

**原文标题**: 'Fighting crime blindfolded': Europe is coming after encryption

**原文链接**: [https://www.politico.eu/article/encryption-crime-denmark-peter-hummelgaard-europe-privacy/](https://www.politico.eu/article/encryption-crime-denmark-peter-hummelgaard-europe-privacy/)

欧洲正在加紧努力破坏端到端加密，原因是担心犯罪分子利用它来促进毒品贩运、儿童色情和招募未成年人等活动。政界人士和执法官员认为，加密阻碍了他们打击犯罪的能力，将其比作“蒙着眼睛打击犯罪”。包括法国、北欧国家、西班牙和英国在内的几个国家正在寻求立法或法律行动，以削弱或禁止加密。

即将到来的丹麦欧盟理事会主席国任期可能会进一步讨论欧盟的儿童性虐待材料法案（CSAM），该法案可能强制执行全面内容扫描，即使在加密平台上也是如此。欧盟委员会还在制定一项新的内部安全战略，其中包括探索执法部门的合法数据访问权限以及消息服务的潜在数据保留法律。

这些努力遭到了隐私活动家、网络安全专家和科技公司的强烈反对，他们认为削弱加密将损害所有用户的安全和隐私，并将犯罪分子推向更安全的平台。领先的加密消息应用程序 Signal 威胁要离开那些强迫其削弱安全性的国家。核心问题在于创建“后门”的内在困难，该后门只能允许执法部门访问，而不会为恶意行为者创建漏洞。欧洲正处于十字路口，可能会在加强警方访问权限和为所有人维护强大的加密之间做出选择。

---

## 80. 我本也该爱上生物学的。

**原文标题**: I should have loved biology too

**原文链接**: [https://nehalslearnings.substack.com/p/i-should-have-loved-biology-too](https://nehalslearnings.substack.com/p/i-should-have-loved-biology-too)

无法访问文章链接。

---

## 81. 展示HN：Morphik – 开源RAG，可理解PDF图像，本地运行

**原文标题**: Show HN: Morphik – Open-source RAG that understands PDF images, runs locally

**原文链接**: [https://github.com/morphik-org/morphik-core](https://github.com/morphik-org/morphik-core)

Morphik是一款开源的检索增强生成(RAG)替代方案，旨在理解技术和视觉文档，提供多模态搜索、知识图谱生成和元数据提取等功能。它支持使用ColPali等技术，从单个端点搜索图像、PDF和视频。

用户可以选择托管的免费层级服务或自托管开源版本（通过直接安装或Docker）。托管服务免费提供前200页和100个查询，之后采用基于使用量的定价。自托管提供有限支持。

Morphik提供Python SDK和REST API用于数据摄取和查询。一个代码示例展示了摄取PDF文件和查询其内容的便捷性。付费版本还提供基于Web的Morphik控制台，用于交互式数据管理和查询。也支持通过MCP访问。

欢迎通过错误报告、功能请求和拉取请求进行贡献，重点是提高速度、集成和识别相关研究。Morphik控制台等关键功能是付费版本独有的，而开源组件则采用MIT许可证。

---

## 82. 北美航空公司1965年关于20世纪70年代载人行星飞越的计划

**原文标题**: North American Aviation's 1965 Plan for Piloted Planetary Flybys in the 1970s

**原文链接**: [https://spaceflighthistory.blogspot.com/2019/01/apollo-to-mars-venus-north-american.html](https://spaceflighthistory.blogspot.com/2019/01/apollo-to-mars-venus-north-american.html)

1965年，北美航空公司(NAA)提出了一项计划，利用阿波罗计划的技术，在1970年代进行载人火星和金星飞越任务。这些飞越旨在弥合阿波罗地球轨道空间站与未来火星/金星轨道器和着陆器之间的差距。该概念涉及宇航员在飞越期间释放自动探测器，从而提高数据质量和探测器的复杂性。

NAA提出了一个分为两个阶段的项目：1973年金星飞越和1975年火星飞越，后者将延伸到小行星带。航天器将由改进的阿波罗指令和服务舱（CSM）、用于乘员生活和工作空间的任务舱（MM）以及用于自动探测器的探测器舱（PC）组成。火星飞越是NAA的重点，需要多达四次土星五号火箭发射。

该计划的关键在于1967年的“启动”日期，以赶上发射窗口机会。关键的开发里程碑包括升级后的隔热罩测试和地球轨道航天器测试。航天器将使用S-IIB轨道发射级（一种改进的土星五号第二级）从地球轨道助推，需要用液氧进行轨道加油。

NAA主张配备四人火星飞越团队，以应对行星近距离飞掠期间增加的工作量，这需要对指令舱进行修改。阿波罗CSM的单引擎将被三个登月舱下降引擎取代。总而言之，NAA的计划为将阿波罗计划的遗产扩展到载人行星探测领域提出了一个全面的愿景。

---

## 83. 停用脸书和照片墙对用户情绪状态的影响

**原文标题**: The effect of deactivating Facebook and Instagram on users' emotional state

**原文链接**: [https://www.nber.org/papers/w33697](https://www.nber.org/papers/w33697)

国家经济研究局 (NBER) 2025 年 4 月发表的这份工作报告，调查了停用 Facebook 和 Instagram 对用户情绪福祉的影响。该研究采用 2020 年美国大选前进行的两个大型随机实验，发现与仅停用一周的对照组相比，停用 Facebook 六周的参与者在衡量幸福感、抑郁和焦虑的综合指数中，经历了 0.060 个标准差的统计学显著改善。同样，停用 Instagram 六周导致同一情绪指数改善 0.041 个标准差。

探索性分析表明，不同的人口群体推动了每个平台的效果。Facebook 的影响在 35 岁以上的人群中更为明显，而 Instagram 的影响主要在 25 岁以下的女性中观察到。

很大一部分作者披露了潜在的利益冲突，包括曾在 Meta (Facebook 的母公司) 任职、收到 Meta 或相关公司的研究资金、收到 Meta 的酬金、参加 Meta 赞助的含付费旅行和住宿的活动，以及拥有 Meta 股票。

---

## 84. Atuin Desktop: 可执行的行动手册

**原文标题**: Atuin Desktop: Runbooks That Run

**原文链接**: [https://blog.atuin.sh/atuin-desktop-runbooks-that-run/](https://blog.atuin.sh/atuin-desktop-runbooks-that-run/)

Atuin Desktop 旨在解决基础设施工作流程碎片化和不可靠的问题，即关键命令和流程通常分散在 Slack 线程、过时的文档和个人 shell 历史记录等不同位置。虽然 Atuin CLI 通过同步和搜索 shell 历史记录解决了部分问题，但 Atuin Desktop 提供了更完整的解决方案：可执行的 Runbook。

Atuin Desktop 是一款本地优先的可执行 Runbook 编辑器，专为基于终端的工作流程而设计。它旨在通过将文档与实时执行相结合，使这些工作流程可重复、可共享和可靠。它在单个环境中包含脚本块、嵌入式终端、数据库客户端和 Prometheus 图表，从而消除上下文切换。

主要功能包括：直接执行 Runbook 步骤以确保文档准确性、通过 Jinja 风格的模板实现可重用的自动化、从 shell 历史记录中自动完成以加快回忆，以及具有 CRDT 驱动同步的本地优先架构。用户还可以通过 Atuin Hub 与他们的团队同步和共享 Runbook。

该视频重点介绍了实际用例，例如发布 Atuin CLI、迁移基础设施、管理数据库查询和启动环境。未来的计划包括用于协作的团队帐户和从 shell 历史记录自动生成 Runbook。对于那些对从各种来源复制粘贴感到沮丧并希望获得更精简和可靠的工作流程的人，早期访问列表已开放。

---

## 85. FontDiffuser: 文本到字体

**原文标题**: FontDiffuser: Text to Font

**原文链接**: [https://yeungchenwa.github.io/fontdiffuser-homepage/](https://yeungchenwa.github.io/fontdiffuser-homepage/)

本文介绍了一种新的自动字体生成方法FontDiffuser，旨在克服现有技术的局限性，尤其是在处理复杂字符和显著风格变化时。FontDiffuser将问题定义为一个噪声到去噪的扩散过程，提供了一种新颖的图像到图像的单样本字体生成方法。

FontDiffuser的核心创新包括：

*   **多尺度内容聚合 (MCA) 块：** 该组件有效地整合了各种尺度的全局和局部内容信息，从而改善了对细节笔画的保留，尤其是在复杂字符中。
*   **风格对比提炼 (SCR) 模块：** 这种新架构有助于实现卓越的风格表示学习。它使用风格提取器从输入图像中解耦风格信息，并使用自定义的风格对比损失来引导扩散模型。这使得能够更有效地处理较大的风格变化。

作者通过大量的实验证明，FontDiffuser实现了最先进的性能，在生成多样化的字符和风格方面超越了以前的方法，尤其是在处理复杂的字符和显著的风格变化时。结果表明，FontDiffuser在模仿字体风格的同时，准确再现字符内容方面非常有效。

---

## 86. 原生 visionOS 平台支持

**原文标题**: Native visionOS platform support

**原文链接**: [https://github.com/godotengine/godot/pull/105628](https://github.com/godotengine/godot/pull/105628)

该 GitHub 议题讨论了向 Godot 游戏引擎添加原生支持 Apple visionOS 平台的提议，使 Godot 游戏能够在 Vision Pro 上运行。 此贡献直接来自 Apple visionOS 工程团队。

目标是允许现有的 Godot 游戏以平面窗口模式原生运行在 visionOS 上，并支持使用新的 visionOS VR 插件创建沉浸式体验。 该工作分为三个增量拉取请求（PR）：第一个 PR 添加了原生 visionOS 平台，尽可能地复用现有 iOS 平台的代码。 后续 PR 将添加 Swift 支持和 Vision Pro VR 插件。

此初始 PR 包括重构特定于平台的逻辑，以在 iOS 和 visionOS 之间共享代码，同时引入针对 visionOS 特定需求（例如缺少 OpenGL 支持）的更改。 Apple 团队已经使用 Metal 渲染驱动在 iOS 和 visionOS 上测试了这些更改，特别是 Platformer 演示。

该团队正在征求社区对共享导出设置的文档的反馈，并帮助测试插件嵌入、存档/IPA 导出以及通过 `ios_deploy` 直接设备部署等功能。 一些 visionOS 特定的功能，如动态 DPI 指标和 visionOS 图标资源目录生成，仍在开发中或需要社区的协助。 作者团队正在向 Godot 社区征求对拟议更改的反馈。

---

## 87. 奋勇作战

**原文标题**: Fight Fiercely

**原文链接**: [https://scottaaronson.blog/?p=8820](https://scottaaronson.blog/?p=8820)

在他的文章《奋力抗争》中，斯科特·阿伦森讨论了他最近对哈佛大学和麻省理工学院的访问，他在哈佛大学做了叶氏讲座。他表达了他对哈佛大学的支持，因为他认为哈佛大学正面临一场重大危机。他敦促该大学“奋力抗争”，抵御MAGA运动对大学的攻击，并认为需要对高等教育的价值进行广泛的、无党派的捍卫。

阿伦森强调了学术界人士，尤其是国际学者，由于政府审查的加强以及被驱逐出境或无限期监禁的可能性而产生的恐惧。他引用了土耳其学生吕梅伊萨·厄兹图尔克（Rümeysa Öztürk）的案例，她因合著一篇呼吁抵制以色列的社论而被监禁，以此说明这种过度行为。

他将此与哈佛希勒尔执行主任贾森·鲁宾斯坦（Jason Rubenstein）的声明进行对比，鲁宾斯坦承认大学需要解决反犹主义问题，但批评政府采取的严厉手段。

阿伦森哀叹失去了一位左翼学术界朋友，原因是他们在“帐篷起义”运动中就反犹主义问题存在分歧，他强调自己拒绝那些优先考虑“弱者”而非对反犹主义的担忧的论点。

最后，他表达了在大学的面对面访问中，在同事中找到理智和理性的欣慰，并将这与他在网上体验到的两极分化和争端不断的氛围进行了对比。他回应了对哈佛大学处理反犹主义问题的批评，并解释了他对以色列两国方案的支持。

---

## 88. 让电脑杂志广告变得精彩的浣熊们

**原文标题**: The raccoons who made computer magazine ads great

**原文链接**: [https://technologizer.com/home/2025/04/22/pc-connection-ads-raccoons/](https://technologizer.com/home/2025/04/22/pc-connection-ads-raccoons/)

本文记录了PC Connection的崛起及其独特的营销方法。PC Connection是一家邮购计算机产品公司，凭借其以拟人化浣熊为特色的独特杂志广告，在 20 世纪 80 年代和 90 年代声名鹊起。PC Connection 由 Patricia Gallup 和 David Hall 于 1982 年创立，通过专注于客户服务和打造令人难忘的品牌，使其与竞争对手区分开来。

他们与广告公司 Church and Main 合作构思的关键营销策略包括委托插画家 Erick Ingraham 创作细致的、诺曼·洛克威尔式的场景，描绘浣熊从事日常活动，从烘焙和耕种到上大学和结婚。文案撰稿人 David Blistein 以异想天开的文字补充了 Ingraham 的艺术作品，强调了 PC Connection 在新罕布什尔州小镇的根基和友好的态度。

浣熊吉祥物，灵感来自《柳林风声》，旨在消除计算机的神秘感，并创造“高科技的人情味”。这些广告虽然仍然包含产品清单，但优先考虑浣熊的形象，浣熊形象成为计算机杂志中令人难忘的元素。PC Connection 还向消费一定金额的客户提供以浣熊为主题的免费赠品，进一步巩固了他们的品牌形象。虽然浣熊的形象在 21 世纪初逐渐减少，但它们仍然是 PC Connection 成功且非常规营销策略的独特且令人怀旧的象征。

---

## 89. 利用 DuckDB-WASM 通过 SQL 绘制 3D 图形（勉强算）

**原文标题**: Abusing DuckDB-WASM by making SQL draw 3D graphics (Sort Of)

**原文链接**: [https://www.hey.earth/posts/duckdb-doom](https://www.hey.earth/posts/duckdb-doom)

本文详细介绍了一项实验，作者尝试使用 DuckDB-WASM 构建一个简易的 3D 游戏引擎，具体来说是一个基于文本的 Doom 克隆版，其中 SQL 处理了大部分游戏逻辑和渲染。与传统的 JavaScript 游戏循环和 Canvas 渲染不同，游戏世界、玩家/敌人位置和游戏状态都存储在 DuckDB 表中。移动、碰撞检测和敌人交互通过 SQL UPDATE 和 DELETE 语句进行管理。

3D 渲染的核心是一个名为 `render_3d_frame` 的 SQL VIEW，它使用递归 CTE 来执行光线投射、计算到墙壁的距离，并使用字符串聚合生成基于文本的帧。JavaScript 处理键盘输入，协调游戏循环，从 SQL 获取数据，并通过 Z 缓冲区检查管理精灵渲染（结合 SQL 墙壁距离和 JS 计算）。

作者遇到了几个挑战，包括初始化 DuckDB-WASM、SQL 方言差异（AUTOINCREMENT vs. SEQUENCE）、查询计划器限制、async/setInterval 竞争条件以及使用 Z 缓冲区检查实现精灵渲染。解决方案包括使用推荐的初始化模式、适应 DuckDB 的 SQL 方言、重构视图逻辑、实现锁以防止竞争条件，以及结合 SQL 和 JavaScript 进行 Z 缓冲区检查。尽管采用了非常规的方法，该游戏仍实现了可玩的 6-7 FPS，展示了使用分析型数据库进行游戏开发的惊人能力和局限性。

---

## 90. 旋转能否解决哈勃难题？

**原文标题**: Can rotation solve the Hubble Puzzle?

**原文链接**: [https://academic.oup.com/mnras/article/538/4/3038/8090496?login=false](https://academic.oup.com/mnras/article/538/4/3038/8090496?login=false)

好的，我已阅读并总结了发表于《英国皇家天文学会月刊》的文章“旋转能否解决哈勃难题？”。

**摘要：**

该文章探讨了引入宇宙旋转的概念是否有助于解决哈勃张力，即使用不同方法测量的哈勃常数（H0）值之间的差异。传统上，H0是使用宇宙微波背景（CMB）和距离阶梯法（使用超新星和造父变星）测量的，但得出的值差异显著。

作者研究了一种宇宙在大尺度上旋转的模型，尽管旋转速度非常小。他们构建并分析了包含旋转的宇宙学模型，并将他们的预测与包括CMB、重子声学振荡（BAO）和Ia型超新星在内的观测数据进行比较。

关键发现是，将旋转引入宇宙学模型*可以*缓解哈勃张力。旋转在宇宙中引入了方向性，这会影响光的传播和距离的解释。通过仔细选择参数，旋转模型可以将CMB推断出的H0值移近通过距离阶梯获得的值。

然而，作者强调，所需的旋转量非常小，并且与现有对各向异性的观测约束相符。此外，该模型并非没有挑战。作者指出需要进一步探索和潜在地调整模型，以充分协调所有观测数据集。论文得出结论，旋转仍然是哈勃张力至少一部分的可行，尽管是推测性的解释，值得使用更精细的数据和模型进一步研究。

---

## 91. C++26：核心语言中更多的constexpr

**原文标题**: C++26: more constexpr in the core language

**原文链接**: [https://www.sandordargo.com/blog/2025/04/23/cpp26-constexpr-language-changes](https://www.sandordargo.com/blog/2025/04/23/cpp26-constexpr-language-changes)

C++26 constexpr 功能扩展：核心语言变更概览

本文概述了 C++26 中 `constexpr` 功能的扩展，重点介绍核心语言变更。文章着重介绍了三个关键特性：

1. **`constexpr` 从 `void*` 转换 (P2738R1):** C++26 允许在常量表达式中将 `void*` 转换为 `T` 类型的指针，前提是该地址处的对象恰好是 `T` 类型。这通过促进将 `void*` 用作编译防火墙技术，从而在标准库中实现更多 `constexpr` 支持。

2. **`constexpr` 定位 new (P2747R2):** 定位 new 可以在常量表达式中使用，从而允许超出 `std::construct_at` 提供的简单值初始化的初始化。这得益于 P2738R1。

3. **`constexpr` 结构化绑定和对 `constexpr` 变量的引用 (P2686R5):** 结构化绑定现在可以声明为 `constexpr`。对 `constexpr` 引用的限制放宽，允许包含具有自动存储期限的变量，前提是它们的地址相对于堆栈帧是常量。这不包括在 `constexpr` lambda 中捕获来自封闭函数的变量，因为被捕获变量的地址在编译时未知。

文章最后提到，`constexpr` 异常将在另一篇文章中探讨，并暗示将有一篇后续文章详细介绍标准库中 `constexpr` 的改进。

---

## 92. 多项式特征是万恶之源吗？(2024)

**原文标题**: Are polynomial features the root of all evil? (2024)

**原文链接**: [https://alexshtf.github.io/2024/01/21/Bernstein.html](https://alexshtf.github.io/2024/01/21/Bernstein.html)

本文挑战了一种常见的观念，即高阶多项式特征本质上对机器学习不利，认为它们可以通过诸如正则化等标准机器学习工具进行有效控制。作者将这种负面认知归因于两个误解：标准多项式基的使用以及对魏尔斯特拉斯逼近定理的误解。

标准基 (1, x, x^2, ..., x^n) 被认为对于从数据中估计多项式是“糟糕的”，因为其系数难以估计且对微小扰动敏感。虽然魏尔斯特拉斯定理表明多项式可以逼近任何连续函数，但这仅在特定区间内成立，因此需要对输入数据进行归一化。

文章随后介绍了替代的多项式基，特别是切比雪夫、勒让德和伯恩斯坦多项式，并强调了切比雪夫和勒让德基在*拟合*任务中的缺点。虽然它们非常适合*插值*，但它们的系数具有“不同的单位”，使得L2正则化无效。

伯恩斯坦多项式被认为是补救措施。它们的系数都具有相同的“单位”，相当于模型的标签，因此更容易进行正则化。作者证明，经过正则化的高阶伯恩斯坦多项式可以实现出色的拟合效果，而不会出现振荡，从而有效地打破了围绕高阶多项式特征的神话。文章强调选择正确的多项式基对于成功的机器学习至关重要。

---

## 93. 展示HN：我做了一个能将GitHub代码库转换成简易教程的AI

**原文标题**: Show HN: I built an AI that turns GitHub codebases into easy tutorials

**原文链接**: [https://github.com/The-Pocket/Tutorial-Codebase-Knowledge](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge)

此“Show HN”帖子介绍了一款AI工具，它能从GitHub代码库中自动生成适合初学者的教程。该AI使用100行代码的LLM框架Pocket Flow构建，能够分析代码仓库，识别核心抽象，并将复杂的代码转换为易于理解、带有可视化的教程。

帖子强调了该AI爬取GitHub仓库、构建知识库以及为AutoGen、FastAPI和NumPy等热门仓库提供示例结果的能力。这些AI生成的教程解释了代码的工作原理。

帖子提供了使用该工具的入门指南：克隆仓库，安装依赖项，使用API密钥设置LLM，并运行主脚本。用户可以分析GitHub仓库或本地目录，指定要包含或排除的文件，并设置最大文件大小。该工具支持生成多种语言的教程。

作者强调该工具是使用“Agentic Coding”技术，并借助Pocket Flow构建的，并在一个分步YouTube教程中展示了整个开发过程。

---

## 94. 盖尔语的幽灵

**原文标题**: The Ghosts of Gaelic

**原文链接**: [https://www.historytoday.com/archive/behind-times/ghosts-gaelic](https://www.historytoday.com/archive/behind-times/ghosts-gaelic)

邓肯·斯内登在《今日历史》上发表的题为“盖尔语的幽灵”一文，考察了苏格兰盖尔语语言和文化的现状与未来前景，尤其是在即将迎来2005年《盖尔语语言法（苏格兰）》颁布20周年以及新的《苏格兰语言法案》之际。

文章强调了盖尔语和英语之间存在的历史张力，指出盖尔语曾经是苏格兰的主要语言，但现在只有少数人使用（2022年为2.5%，高于2011年的1.7%）。它将《盖尔语语言法》视为旨在将盖尔语提升到与英语同等地位的关键立法。新的《苏格兰语言法案》赋予盖尔语和苏格兰语官方地位，被视为重塑苏格兰语言政策的机会。

斯内登表示，文章将反思少数族裔盖尔语与更广泛的苏格兰民族认同之间复杂且常常矛盾的关系。他暗示，盖尔语的未来岌岌可危，新的语言法案的成功对于它能否在一个历史上由英语主导的国家真正蓬勃发展至关重要。

---

## 95. 我们诊断并修复了150亿英里外的2023年旅行者1号异常 [视频]

**原文标题**: We Diagnosed and Fixed the 2023 Voyager 1 Anomaly from 15B Miles Away [video]

**原文链接**: [https://www.youtube.com/watch?v=YcUycQoz0zg](https://www.youtube.com/watch?v=YcUycQoz0zg)

这个YouTube视频，标题为“我们诊断并修复了150亿英里外的2023年旅行者1号异常”，可能详细介绍了2023年旅行者1号探测器所受问题进行故障排除和解决的过程。 鉴于标题，关键信息是工程师成功诊断并修复了位于距离地球150亿英里的航天器上的问题。

虽然提供的文本摘录没有包含关于异常或解决方案的细节，但标题暗示了一项复杂而令人印象深刻的远程工程壮举。 该视频可能解释了问题的性质，用于从如此遥远的距离确定原因的诊断过程，以及为实施修复而采取的步骤。 它也可能强调由于信号延迟而与旅行者1号通信的挑战，以及所涉及技术的韧性。

列出的项目，如“YouTube关于新闻版权联系我们创作者广告开发者条款隐私权政策与安全YouTube 的运作方式测试新功能NFL Sunday Ticket© 2025 Google LLC”，是标准的YouTube样板，与标题中描述的视频的实际内容无关。 因此，摘要仅侧重于标题的含义。

---

## 96. Show HN: Advanced-Alchemy – SQLAlchemy 的框架无关库

**原文标题**: Show HN: Advanced-Alchemy – A framework agnostic library for SQLAlchemy

**原文链接**: [https://github.com/litestar-org/advanced-alchemy](https://github.com/litestar-org/advanced-alchemy)

高级炼金术 (Advanced Alchemy) 是一个 Python 库，旨在增强 SQLAlchemy，提供优化的 CRUD 操作、框架集成和实用工具类等功能。它提供同步和异步仓库，方便高效的批量操作、分页、排序和过滤。它支持多种数据库后端，包括 SQLite、Postgres、MySQL、Oracle、Google Spanner、DuckDB 和 SQL Server。

该库包含一个 `Service` 类，用于简化仓库的数据处理。高级炼金术与主要 Web 框架（如 Litestar（作为其官方 SQLAlchemy 集成）、Flask、FastAPI、Starlette 和 Sanic）集成，并提供框架特定的助手函数。每个框架都有示例应用程序。

主要特性包括：

*   **仓库 (Repositories):** 同步和异步，具有 CRUD 和批量操作。
*   **服务 (Services):** 简化仓库的数据处理。
*   **框架集成 (Framework Integration):** 为 Litestar、Flask、FastAPI、Starlette 和 Sanic 提供助手函数。
*   **数据库支持 (Database Support):** 范围广泛，包括 SQLite、Postgres、MySQL 等。
*   **实用工具 (Utilities):** 带有审计列、主键等的基类。
*   **自定义数据类型 (Custom Data Types):** 文件对象存储、优化 JSON、UUID6/UUID7、Nano ID。

该库欢迎贡献，并鼓励通过 Discord、GitHub 讨论和贡献指南参与社区。

---

## 97. 超木 – 开源家具

**原文标题**: Hyperwood – Open-Source Furniture

**原文链接**: [https://hyperwood.org/](https://hyperwood.org/)

Hyperwood：一个开源家具建造系统，旨在让从DIY爱好者到小型制造商的任何人都能使用简单的木条建造坚固的家具。受“小即是美”和自主设计启发，它优先考虑本地采购、最少工具和易用性。

目前，由于需要专门的工具，Hyperwood 主要面向具有编程知识的用户。它可以自动生成个性化的施工计划和优化的材料清单。这种算法方法确保了家具制造过程的可持续性、废料效率和可访问性。长远目标是开发图形用户界面（GUI），以扩大其吸引力，并使其能够被更广泛的受众使用，无论他们是否具备技术专业知识。

---

## 98. 黄石国家公园地下4公里内发现“呼吸”的岩浆盖

**原文标题**: 'Breathing' magma cap discovered less than 4km under Yellowstone National Park

**原文链接**: [https://news.sky.com/story/breathing-magma-cap-discovered-less-than-4km-under-yellowstone-national-park-13354687](https://news.sky.com/story/breathing-magma-cap-discovered-less-than-4km-under-yellowstone-national-park-13354687)

科学家发现黄石公园地表下3.8公里处存在一个“呼吸”的岩浆盖，他们认为这正在阻止潜在的火山爆发。这个富含挥发物（溶解气体）的岩浆盖不断释放压力和气体，有效地像“稳定呼吸”一样排出火山系统的气体。来自多所大学的研究人员使用了一辆可控震源车制造微小的地震和地震波，然后由600多个地震仪记录。这些波揭示了岩浆盖的深度，修正了之前将岩浆系统顶部置于3到8公里之间的估计。这一发现有助于科学家更好地了解黄石岩浆系统目前的状态，与过去爆发前的状态进行比较。岩浆盖的持续释放气体作用似乎是阻止黄石公园爆发的关键因素。

---

## 99. 某人意外地存了五十万美元。

**原文标题**: Someoen accidentally saved half a million-dollars

**原文链接**: [https://ludic.mataroa.blog/blog/i-accidentally-saved-half-a-million-dollars/](https://ludic.mataroa.blog/blog/i-accidentally-saved-half-a-million-dollars/)

一位数据工程师如何在五分钟内意外为公司节省五十万美元：一个幽默且讽刺的故事

这篇文章以幽默和讽刺的口吻讲述了作者，一位数据工程师，如何通过修复 Snowflake 数据库中的一个简单配置设置，意外地为公司节省了五十万美元。

该公司在新分析平台 (AAP) 上投入了巨额资金，聘请了顾问和庞大的团队，但未能交付一个功能完善且高效的系统。作者描述了一个混乱且低效的环境，该环境饱受技术债务、糟糕的编码习惯和缺乏常识的困扰。流程过于复杂，安全措施无效，基本错误数月未得到解决。

作者注意到他们的 Snowflake 数据库成本远高于预期，原因是每次查询后计算机闲置时间过长。尽管几个月前就提出了这个问题，但管理层延迟采取行动。最终，作者被委派了“优化成本”的任务，并在一位同事的帮助下，对空闲时间设置进行了一个简单的更改。

这一个简单的更改导致预计数据库成本减少了 50 万美元，引起了内部的混乱和关注。虽然管理层庆祝了成本节约，但他们不愿完全实施更改，以避免引起不必要的关注。作者被要求淡化修复的简单性，并创建一个 PowerPoint 演示文稿，暗示更复杂的分析过程导致了优化。尽管节省了大量成本，但作者要求加薪的要求却被忽视了。文章最后提出警告：在一个功能失调的组织中，努力工作并取得成功可能会受到惩罚。

---

## 100. 意义机器 – 可视化大型语言模型如何分解和模拟意义

**原文标题**: Meaning Machine – Visualize how LLMs break down and simulate meaning

**原文链接**: [https://meaning-machine.streamlit.app](https://meaning-machine.streamlit.app)

无法访问文章链接。

---

