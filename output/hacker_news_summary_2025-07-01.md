# Hacker News 热门文章摘要 (2025-07-01)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 美联储称这是一个价值一百万美元的立方体，他们算错了，差了五十万。

**原文标题**: The Fed says this is a cube of $1M. They're off by half a million

**原文链接**: [https://calvin.sh/blog/fed-lie/](https://calvin.sh/blog/fed-lie/)

作者幽默地讲述了其调查芝加哥联邦储备银行货币博物馆中“百万美元”立方体展示的经历。作者怀疑标牌上声称该立方体包含整整1,000,000美元的说法，试图清点钞票堆，但发现极具挑战性。由于缺乏现成的图像对象计数工具，作者创建了一个名为“Dot Counter”的简单Web应用程序。

利用Dot Counter，作者仔细数了立方体照片中可见的钞票堆，并根据每捆100张钞票的假设计算了其价值。结果令人惊讶，为1,550,400美元，比声称的数额高出惊人的550,400美元。

文章风趣地探讨了造成差异的各种解释，考虑了立方体是空心的，或是经过策略性填充以显得更有价值等情况。然后，文章深入探讨了由于钞票的尺寸，使用美国货币创建一个真正的立方体的难度，并提出了另一种配置方案。

最终，作者得出结论，该立方体要么包含100万美元，要么包含155万美元，要么就是一个幻觉。主要的收获是以幽默的方式展示了质疑声明和验证信息的重要性，即使这些信息是由官方机构提供的，并且使用了作者新开发的Dot Counter。作者鼓励读者使用该工具来满足他们自己的计数需求。

---

## 2. 探访赛德娜任务可行性研究 - 核动力推进与太阳帆

**原文标题**: Feasibility study of a mission to Sedna - Nuclear propulsion and solar sailing

**原文链接**: [https://arxiv.org/abs/2506.17732](https://arxiv.org/abs/2506.17732)

2025年arXiv论文《前往赛德娜的任务可行性研究——核动力推进与先进太阳帆概念》探讨了使用先进推进方法抵达赛德娜的可行性。作者Elena Ancona、Roman Ya. Kezerashvili和Savino Longo对比了直接聚变驱动（DFD）火箭发动机和利用热脱附的太阳帆。

该研究提出了一项单向地球到赛德娜的任务，其中DFD用于轨道插入，太阳帆则设想用于飞掠。它评估了有效载荷能力、旅行时间和两种推进系统的潜在科学回报等关键参数。DFD被建模为具有恒定推力的1.6兆瓦系统，而太阳帆则结合了热脱附和木星引力辅助。

任务分析分为四个阶段：出发、行星际加速、行星际滑行和交会。由于赛德娜在2075-2076年接近近日点，因此时间安排至关重要。结果表明，DFD可以在大约10年内到达赛德娜，其中推进时间为1.5年。借助木星的辅助，太阳帆可以在7年内完成旅程。

该论文还探讨了容纳科学载荷、电力可用性和通信约束的可行性。该研究提供了一项比较分析，以帮助未来的深空任务规划。

---

## 3. Show HN: Spegel，一款使用LLM重写网页的终端浏览器

**原文标题**: Show HN: Spegel, a Terminal Browser That Uses LLMs to Rewrite Webpages

**原文链接**: [https://simedw.com/2025/06/23/introducing-spegel/](https://simedw.com/2025/06/23/introducing-spegel/)

Spegel：一个使用LLM重写网页并在终端中以Markdown渲染的概念验证终端Web浏览器。作为一个周末项目开发，并受到谷歌更快的Gemini 2.5 Pro Lite发布的推动，Spegel旨在通过自定义提示将其适配到个人需求，从而提供个性化的网页内容视图。

其核心思想是解决在终端中查看现代网站时存在的混乱和干扰。 Spegel获取HTML，通过LLM使用用户在配置文件中定义的提示对其进行处理，并通过Textual库输出渲染的Markdown。 用户可以创建单个页面的多个“视图”，例如简化内容 (ELI5) 或突出显示关键操作，并且可以在浏览会话期间调整提示。

作者分享了一个提取食谱基本部分的示例配置，展示了转换内容以适应特定需求的能力。 该浏览器目前仅支持GET请求，但未来的计划包括处理表单和POST请求。 虽然承认存在其他终端浏览器，如Lynx和Browsh，但Spegel通过利用LLM更紧密地根据用户需求定制内容而脱颖而出。

Spegel可通过pip安装 (`pip install spegel`)，并且需要一个配置文件。 源代码可在GitHub上获取，欢迎贡献。

---

## 4. 将数学软件包转换为C++20模块的经验 [PDF]

**原文标题**: Experience converting a mathematical software package to C++20 modules [PDF]

**原文链接**: [https://arxiv.org/abs/2506.21654](https://arxiv.org/abs/2506.21654)

将大型C++数学软件包转换为C++20模块的经验
        
这篇arXiv论文，题为“将大型C++数学软件包转换为C++20模块的经验”，探讨了将一个重要的C++数学软件库，特别是deal.II（约80万行代码），迁移到C++20模块系统的过程。作者Wolfgang Bangerth详细介绍了一种同时支持传统基于头文件的接口和新的基于模块的方法。

该论文讨论了转换过程中遇到的挑战，并深入了解了C++20模块在实际场景中的运作方式。作者基于编译时间和易用性等人为因素等技术指标评估了该模块系统。

该研究的结论是，将大型C++代码库转换为模块是可行的，但需要付出相当大的努力。虽然转换后的库本身的编译时间有所改善，但下游项目在编译时间变化方面没有显示出一致的趋势。该论文最后提出了长期战略，以便在未来几年内将数学软件生态系统更广泛地过渡到C++20模块。这项工作为考虑在大型项目中采用C++20模块的开发人员贡献了实践经验和见解。

---

## 5. 我做了个东西，改变了我们朋友圈的社交结构。

**原文标题**: I built something that changed my friend group's social fabric

**原文链接**: [https://blog.danpetrolito.xyz/i-built-something-that-changed-my-friend-gro-social-fabric/](https://blog.danpetrolito.xyz/i-built-something-that-changed-my-friend-gro-social-fabric/)

2022年，作者的朋友们分散在世界各地，他们使用混乱的Signal群聊努力保持联系和组织游戏。为了解决这个问题，作者构建了一个Discord机器人，每当有人加入Discord服务器中的语音频道时，该机器人就会向指定的文本频道发送通知。这个简单的解决方案就像一个“蝙蝠信号”，提醒所有人何时有人可以聊天或玩游戏。

最初，该机器人褒贬不一，但很快就改变了群体的社交动态。它减少了群聊中不断协调的需求，并鼓励了自发的社交互动，许多成员仅仅为了快速聊天而加入Discord，让人想起过去的电话。作者多年来追踪Discord的使用情况，发现活动量持续增加，即使是那些现在30多岁并有家庭责任的朋友也是如此。该机器人促进了快速的问候，并在忙碌的生活中提供了一种连接感。

作者现在为他们的年度圣诞派对制作一个“Discord年度回顾”，分享个性化的统计数据和排行榜，以回顾一年的在线活动。未来的计划包括添加成就、跟踪在Discord中花费的时间，并可能创建一个带有颜色编码灯的物联网设备，以指示特定朋友何时加入Discord语音频道。作者正在考虑将该设备变成真正的产品。

---

## 6. Cua (YC X25) 招聘创始工程师

**原文标题**: Cua (YC X25) Is Hiring a Founding Engineer

**原文链接**: [https://www.ycombinator.com/companies/cua/jobs/dIskIB1-founding-engineer-cua-yc-x25](https://www.ycombinator.com/companies/cua/jobs/dIskIB1-founding-engineer-cua-yc-x25)

Cua (YC X25) 招聘创始工程师，该公司致力于构建人工智能代理安全且可扩展地使用计算机和应用程序的基础设施。他们提供开源框架、用于代理执行的云容器平台以及生产级代理系统的蓝图。

创始工程师将负责交付驱动代理工作负载的基础设施、塑造开源社区、贡献于产品战略并推广该平台。

理想的候选人应具有扎实的系统背景、扩展基础设施和保护容器的经验，以及对设计简单API的热情。要求包括计算机科学学士学位（或同等学历），以及2年以上后端系统经验（Python、Go、TypeScript或Rust）、熟悉LLM生成的代码以及应对不确定性的能力。Docker/KVM/OS虚拟化经验、多云经验、PostgreSQL优化经验以及开源贡献将是加分项。

该职位位于旧金山（混合办公优先，支持远程办公），基本工资为 10 万美元至 15 万美元，股权为 0.5% 至 0.75%。Cua 获得了 Y Combinator 和顶级投资者的支持。申请人应提供他们的 GitHub 个人资料，并附注他们解决的具有挑战性的基础设施问题，为 Cua 开源项目做出贡献者优先。

---

## 7. Show HN：人脉求职：在领英人脉中找工作

**原文标题**: Show HN: Jobs by Referral: Find jobs in your LinkedIn network

**原文链接**: [https://jobsbyreferral.com/](https://jobsbyreferral.com/)

JobsByReferral是一个工具，帮助用户在LinkedIn等平台上，通过职业人脉网络寻找职位空缺。它分析用户的联系人数据，识别出用户拥有人脉的公司，从而增加他们获得内推和面试的机会。

该过程包括三个步骤：首先，用户必须提供他们的联系人数据，可以通过上传数据存档（例如LinkedIn的ZIP文件）或符合特定格式的CSV文件（需要包括名字、姓氏、公司、职位）来实现。其次，该工具会分析人脉网络，找出拥有最多联系人的公司。第三，用户可以搜索相关职位并查看结果，利用他们的人脉进行内推。

该平台提供了一个演示CSV文件，供希望在上传自己的数据之前测试服务的用户使用，让他们体验该功能并了解其工作原理。

---

## 8. Show HN: HackerNewt - iOS 平台的广度优先 HN 探索客户端

**原文标题**: Show HN: HackerNewt - Breadth-first exploring HN client for iOS

**原文链接**: [https://apps.apple.com/us/app/hackernewt-for-hacker-news/id6448201970](https://apps.apple.com/us/app/hackernewt-for-hacker-news/id6448201970)

HackerNewt：一款旨在改善 Hacker News 阅读体验的 iOS 应用。它以广度优先的方式呈现评论，避免了传统界面中评论宽度逐渐变窄的问题。用户可以通过滑动和滚动轻松浏览讨论，保持上下文，并跳过不感兴趣的子树。

主要功能包括自定义版块、搜索（包括线程内搜索）、锚点、阅读列表和最近项目。该应用免费，但提供应用内购买，用于打赏和购买高级版本。

用户评价大多为正面，平均评分为 4.6 星（满分 5 星）。最近一条负面评论指出该应用无法加载，开发者迅速解决了该问题，并且还积极回应了一位不确定如何在帖子中发表评论的用户。

开发者声称该应用不收集任何数据。它需要 iOS 15.0 或更高版本，并且与 iPhone 和 iPod Touch 兼容。该应用被归类为新闻类，并且由于可能接触到成人主题、亵渎性语言以及毒品/酒精内容，因此评级为 17+。

---

## 9. 大自然何时焕发绚丽色彩？

**原文标题**: When Did Nature Burst into Vivid Color?

**原文链接**: [https://www.quantamagazine.org/when-did-nature-burst-into-vivid-color-20250627/](https://www.quantamagazine.org/when-did-nature-burst-into-vivid-color-20250627/)

《量子杂志》文章“自然界何时迸发出鲜艳的色彩？”探讨了自然界中色彩视觉和鲜艳色彩信号的进化时间线。进化生物学家 Zachary Emberts 和 John Wiens 重建了 5 亿年的进化历史，结合化石记录和系统发育树，以研究色彩视觉是在鲜艳色彩信号（例如，鲜亮的水果、花朵、求偶色）之前还是之后进化而来。

他们的研究表明，色彩视觉的进化早于鲜艳色彩信号，可能在 4 亿到 5 亿年前，发生在节肢动物和脊椎动物中。鲜艳色彩信号的出现紧随其后：大约在 3 亿年前，水果和种子中出现了独特的颜色，随后是色彩鲜艳的花朵、警戒色（大约在 1.3 亿年前），最后是动物的性信号（大约在 1 亿年前）。

文章承认了重建如此久远的进化历史所固有的不确定性，指出颜色不易形成化石，且进化树本质上具有推测性。尽管存在这些局限性，该研究仍为色彩视觉和依赖于它的信号之间的进化关系提供了宝贵的见解，表明色彩视觉最初可能具有不同的用途，之后才在检测这些信号中发挥作用。科学家们提出，早期的用途可能包括识别物体、导航，甚至改善在弱光水生环境中的视觉。

---

## 10. OpenFLOW – 在本地快速制作精美的基础设施图表

**原文标题**: OpenFLOW – Quickly make beautiful infrastructure diagrams local to your machine

**原文链接**: [https://github.com/stan-smith/OpenFLOW](https://github.com/stan-smith/OpenFLOW)

OpenFLOW是一款开源的渐进式Web应用(PWA)，使用React和Isoflow库构建，允许用户直接在Web浏览器中快速创建美观的等距基础设施图。它优先考虑用户隐私，将所有数据存储在本地，并提供离线支持以保证工作不中断。

主要功能包括等距图绘制、自动保存功能（每5秒一次）、将图表导入/导出为JSON文件以及全面的离线支持。用户可以通过拖放添加和连接组件，自定义其外观，并轻松导航画布。

图表会自动保存到浏览器的本地存储中。该应用程序还提供快速保存、保存副本、加载现有图表和管理存储空间等选项。

要在本地运行OpenFLOW，用户需要克隆GitHub存储库，使用npm安装依赖项，然后启动开发服务器。可以创建生产版本，以便部署到静态托管服务，例如GitHub Pages、Netlify和AWS S3。 PWA功能需要HTTPS。

该应用依赖于React来实现UI，TypeScript来实现类型安全，以及Isoflow库来实现等距图绘制。 欢迎贡献，该项目根据Unlicense许可发布。 Isoflow库本身根据MIT许可证发布。

---

## 11. Show HN: 我做了个我一直想用的Stripe跨国迁移工具

**原文标题**: Show HN: I built the tool I wished existed for moving Stripe between countries

**原文链接**: [https://www.stripemove.com/](https://www.stripemove.com/)

Stripe Move旨在解决Stripe账户跨国迁移的难题，这一过程对企业来说可能既复杂又具破坏性。切换Stripe账户通常涉及手动流程，如重新创建订阅、更新支付方式以及处理Webhook配置，这可能导致客户流失和收入损失。

Stripe Move能够自动化处理大部分流程，使企业能够在不同国家切换到新的Stripe账户，而不会中断其运营。它可以处理诸如迁移客户数据、订阅、支付方式和产品信息等任务，从而确保平稳过渡。

其主要优势在于消除了手动数据传输并减少了潜在错误，最终最大限度地减少了客户中断，并在迁移期间防止收入损失。通过简化Stripe迁移过程，Stripe Move旨在使企业能够更轻松地进行国际扩张或重组其运营，而无需担心复杂的支付系统转换。 本质上，它是一种精简的解决方案，用于切换Stripe账户，同时保留现有的客户关系和订阅模式。

---

## 12. 伊索寓言单音节版

**原文标题**: Aesop in Words of One Syllable

**原文链接**: [https://blog.pgdp.net/2025/07/01/aesop-in-words-of-one-syllable/](https://blog.pgdp.net/2025/07/01/aesop-in-words-of-one-syllable/)

本文探讨了19世纪专为儿童设计的独特版本的伊索寓言《单音节伊索寓言》。它突出了儿童文学从纯粹的道德教诲向融入想象力的转变。文章解释说，虽然历史上伊索是否存在尚有争议，但他的寓言一直广受欢迎且具有影响力，从成人读物演变为插图儿童读物。

这个特别版本与众不同之处在于，它几乎完全使用单音节词编写，是玛丽·戈多尔芬（露西·艾金）旨在使儿童更容易阅读的系列作品的一部分。1895年版收录了99个寓言故事，包括“狼来了”和“狐狸与葡萄”等著名故事，尽管“龟兔赛跑”等一些故事缺失。文章感谢Distributed Proofreaders和Project Gutenberg为使这个版本易于访问所做的工作。

---

## 13. 图论在电子游戏中的应用

**原文标题**: Graph Theory Applications in Video Games

**原文链接**: [https://utk.claranguyen.me/talks.php?id=videogames](https://utk.claranguyen.me/talks.php?id=videogames)

克拉拉·阮的《图论在视频游戏中的应用》一文探讨了图论在视频游戏开发中的实际应用。文章涵盖了各个方面，首先介绍了图在3D图形中的基本应用，包括顶点、边以及基于三角形的渲染，如背面剔除和绘制模式（三角形列表、条带和扇形）。

文章的很大一部分重点是赛车游戏和圈数计算。文章提出使用形成哈密顿回路的“检查点”系统，玩家必须通过所有检查点才能完成一圈。文章展示了如何将赛道表示为图，通过将2D问题转化为1D减法，简化玩家之间的距离计算。

文章批判了《马里奥赛车Wii》中的“超级捷径”漏洞，强调了其有缺陷的检查点系统如何允许玩家跳过赛道的重要部分。这突显了使用图论原理确保正确完成圈数并防止漏洞的重要性。

最后，文章深入研究了使用不相交集数据结构和并查集算法生成迷宫的方法。文章解释了如何最初将每个单元格视为一个单独的集合，然后使用“并”操作连接单元格（打破墙壁）可以有效地生成复杂的迷宫，形成最小生成树结构。暗示了“查”操作优化将在稍后讨论。文章强调迷宫可以表示为图，并可以使用DFS和BFS等算法解决。

---

## 14. 我用C语言编写类型安全的泛型数据结构。

**原文标题**: I write type-safe generic data structures in C

**原文链接**: [https://danielchasehooper.com/posts/typechecked-generic-c-data-structures/](https://danielchasehooper.com/posts/typechecked-generic-c-data-structures/)

Daniel Hooper的文章探讨了C语言中类型安全的泛型数据结构，重点介绍了一种使用联合体将类型信息与泛型结构关联起来的新方法。文章以链表为例，将此方法与常见的C语言泛型编程技术进行了对比，概述了它们的局限性和优点。

以下是所介绍技术的分解：

*   **泛型级别0（泛型头文件）：** 涉及使用宏在头文件中定义类型，然后为每个特定类型多次包含该头文件。虽然具有泛型和类型安全，但这种方法存在代码膨胀、难以定位定义以及需要类型前缀函数名称的问题。
*   **泛型级别1（void \*）：** 使用`void *`来表示泛型数据。它缺乏类型安全，但实现简单。此外，将节点与其数据分离需要多次分配，这可能会影响性能。
*   **泛型级别2（内联存储）：** 通过使用灵活数组成员将数据直接存储在节点中，从而改进了`void *`方法。这减少了内存开销并提高了缓存性能，但需要显式传递数据大小。
*   **泛型级别3（使用联合体进行类型检查）：** 本文的核心介绍了一种类型安全的解决方案。它使用包含ListNode指针和参数化类型指针(`payload`)的联合体。宏利用三元运算符在函数调用期间强制类型匹配，为类型不匹配触发编译时错误，并避免运行时类型转换。此外，该方法可用于包含多个关联类型的结构体。

文章最后给出了处理类型返回和结构体匹配的编译器问题的示例。它强调了该技术对各种数据结构（包括哈希表）的适应性。

---

## 15. 一流模型：缺失的生产力革命

**原文标题**: First-Class Models: The Missing Productivity Revolution

**原文链接**: [https://frest.substack.com/p/first-class-models-the-missing-productivity](https://frest.substack.com/p/first-class-models-the-missing-productivity)

无法访问文章链接。

---

## 16. 基因密码使斑马鱼能够修复受损器官

**原文标题**: Genetic code enables zebrafish to mend damaged organs

**原文链接**: [https://www.caltech.edu/about/news/genetic-code-enables-zebrafish-to-mend-damaged-organs](https://www.caltech.edu/about/news/genetic-code-enables-zebrafish-to-mend-damaged-organs)

斑马鱼拥有非凡的心脏再生能力，这一过程由一组特定基因控制。加州理工学院和加州大学伯克利分校的研究已经确定了这个基因回路，可能为人类心脏修复提供见解。该研究重点关注神经嵴细胞，这是一种干细胞，有助于形成心脏内的各种细胞类型。这些细胞在协调斑马鱼心脏的再生过程中起着至关重要的作用。当这些细胞被移除时，斑马鱼失去了再生心脏的能力。

该研究确定了一个在再生过程中激活的复杂基因网络。这些对胚胎发育至关重要的基因通常在成年期失活，但在损伤后会重新激活以促进组织再生。研究人员目前正在研究触发损伤后基因重新激活的信号。

Martik团队正在使用CRISPR技术来探索这些基因是否可以在人类心脏细胞中重新激活。最终目标是确定人类是否可以激活类似的基因来修复受损的心脏，例如在心脏病发作后或先天性心脏缺陷的情况下。这项研究为未来治疗人类心脏疾病提供了一条潜在途径。

---

## 17. 所有优秀的编辑都是海盗：纪念刘易斯·H·拉帕姆

**原文标题**: All Good Editors Are Pirates: In Memory of Lewis H. Lapham

**原文链接**: [https://www.laphamsquarterly.org/roundtable/all-good-editors-are-pirates](https://www.laphamsquarterly.org/roundtable/all-good-editors-are-pirates)

基拉·布鲁纳·唐的《优秀的编辑都是海盗》深情回忆了刘易斯·H·拉帕姆，着重描述了她担任《拉帕姆季刊》执行主编的时光，这份杂志是他结束在《哈泼斯杂志》的长期任职后创办的。唐描绘了杂志创刊初期景象，人手严重不足，几乎到了滑稽的地步，但却被拉帕姆的求知欲和不知疲倦的职业道德所驱动。

这篇文章突出了拉帕姆对质量的执着，以及他乐于征求所有人的意见，从实习生到出版商。唐强调了他对声音力量的信念，以及与作者进行深入讨论以获得最佳结果的重要性。在承认他缺点的同时，她强调了他自由放任的管理风格，对创造力的鼓励，以及对他员工坚定不移的支持。

唐还回顾了拉帕姆所处的充满活力的纽约文学场景，其特点是深夜晚餐和激烈的学术辩论。她解释了拉帕姆的榜样和指导如何直接影响了她共同创办《陌生人指南》的决定，并强调她和她的联合创始人正是以他的模式建立了这份杂志。最后，这篇文章反思了纽约文学界不断变化的面貌，并赞扬了拉帕姆对它产生的独特影响，以他标志性的鼓励语“前进，亲爱的”结尾。

---

## 18. 人工智能领域的新技能不是提示工程，而是上下文工程。

**原文标题**: The new skill in AI is not prompting, it's context engineering

**原文链接**: [https://www.philschmid.de/context-engineering](https://www.philschmid.de/context-engineering)

本文认为，“上下文工程”正成为人工智能开发的关键技能，超越了“提示词工程”。上下文工程被定义为设计系统，以在正确的时间，以正确的格式，动态地为大型语言模型（LLM）提供正确的信息和工具，从而完成任务。

文章强调，人工智能代理的失败越来越多地归因于不良的上下文，而非模型本身的局限性。它将“上下文”的定义扩展到单个提示词之外，包括指令、用户提示、短期记忆（对话历史）、长期记忆（持久知识）、检索信息（RAG）、可用工具和结构化输出格式。

作者通过对比“廉价演示”代理和“神奇”代理来阐明上下文的影响。“神奇”代理由丰富的上下文（日历数据、过去的电子邮件、联系人列表、工具）驱动，产生的响应比仅能看到直接用户请求的“廉价演示”代理更有用和相关。

上下文工程被认为是一个动态系统，而非静态提示词。它涉及确保模型可以访问关键细节，并以简洁明了的方式呈现该信息。重点从编写巧妙的代码转移到收集和格式化LLM成功所需的信息。作者总结说，构建可靠的人工智能代理越来越在于有效地组织信息，以使LLM能够完成任务，这涵盖了业务理解、输出定义和数据结构。

---

## 19. Grammarly 收购 Superhuman

**原文标题**: Grammarly acquires Superhuman

**原文链接**: [https://www.reuters.com/business/grammarly-acquires-email-startup-superhuman-ai-platform-push-2025-07-01/](https://www.reuters.com/business/grammarly-acquires-email-startup-superhuman-ai-platform-push-2025-07-01/)

**摘要：**

在假定 Grammarly 收购 Superhuman 的情景下，以下为基于提供标题和发布日期的总结：

人工智能写作助手公司 Grammarly 已收购以速度、效率和设计至上的界面著称的高端邮件初创公司 Superhuman。 这项收购于 2025 年 7 月 1 日报道，标志着 Grammarly 正扩大其业务范围，成为一个全面的 AI 通信平台，而不仅仅局限于语法和拼写。

此次收购的目的很可能是将 Superhuman 先进的邮件管理功能与 Grammarly 的 AI 写作工具集成。 这可能会产生一些功能，这些功能可以直接在邮件撰写过程中提供实时的写作辅助和语气建议，从而提高邮件沟通的整体质量和效果。

分析师认为，Grammarly 的目标是成为所有书面沟通形式的中心枢纽，而收购 Superhuman 为其在邮件市场提供了强大的立足点。 Superhuman 对用户体验和生产力的关注与 Grammarly 在 AI 驱动的写作增强方面的优势相辅相成。

初步报告中未披露此次收购的财务条款，但该交易使 Grammarly 能够更好地与提供集成通信套件的大型科技公司竞争。 集成路线图和未来的产品供应仍有待观察，但预计此次收购将为两个平台的用户带来邮件生产力和写作质量的显著进步。

---

## 20. 模拟揭示增强碳纤维强度的秘密

**原文标题**: Simulations reveal the secret to strengthening carbon fiber

**原文链接**: [https://www.ornl.gov/news/simulations-reveal-secret-strengthening-carbon-fiber](https://www.ornl.gov/news/simulations-reveal-secret-strengthening-carbon-fiber)

橡树岭国家实验室研究人员发现了一种通过加入聚丙烯腈（PAN）纳米纤维薄增强层来显著增强碳纤维复合材料的方法。他们利用前沿超级计算机模拟了500万个原子，以了解这些比人类头发细100倍的纳米纤维如何在原子层面提高材料的强度。

模拟表明，直径约为6纳米的PAN纳米纤维性能最佳，它们在碳纤维和聚合物基体之间的界面处均匀排列，从而改善应力传递和整体强度。 这种方法解决了碳纤维复合材料中的常见失效点，该失效点通常发生在碳纤维和聚合物之间的界面处。

该团队使用大规模原子/分子并行模拟器（LAMMPS）对原子的行为进行建模，使用石墨烯片拉动材料以识别薄弱点。 模拟表明，使用纳米纤维使碳纤维复合材料的抗拉强度提高了一倍。

这项发表在《先进功能材料》上的研究为制造用于各种应用的超耐用、轻质材料铺平了道路，这些应用包括飞机、车辆和一般制造业。 该团队计划继续在前沿超级计算机上进行研究，整合人工智能以探索更广泛的先进复合材料。 最终，他们的目标是开发不仅更坚固，而且更智能、更高效的材料。

---

## 21. 高通/骁龙设备USB端口中的隐藏JTAG

**原文标题**: The hidden JTAG in a Qualcomm/Snapdragon device’s USB port

**原文链接**: [https://www.linaro.org/blog/hidden-jtag-qualcomm-snapdragon-usb/](https://www.linaro.org/blog/hidden-jtag-qualcomm-snapdragon-usb/)

本文探讨了高通公司发布的可与EUD（嵌入式USB调试）交互的源代码。EUD是一种自2018年左右以来内置于大多数高通SoC中的调试接口，它通过USB连接提供对CPU和协处理器调试功能的访问，从而公开一个SWD接口，无需外部工具或焊接即可进行类似JTAG的调试。

此次发布使开发者能够使用OpenOCD（一种开源片上调试器）直接通过USB调试高通设备。作者详细介绍了构建代码的过程，包括修复错误和重新构建OpenOCD。他们强调了EUD在调试U-Boot、TF-A和OP-TEE方面的优势，尤其是在垂直集成的BSP中。

文章还提到了EUD中存在的COM（UART）和跟踪外设，暗示了高级封闭案例调试场景的潜力。作者鼓励社区贡献力量，将EUD支持扩展到更多SoC，并解决诸如粘滞复位位之类的怪异问题。

尽管EUD提供了强大的调试功能，但它在控制生产设备上更高执行级别方面似乎受到限制。尽管如此，作者总结认为，EUD的发布是向前迈出的一大步，降低了高通平台低级调试的入门门槛，节省了成本，缩短了设置时间，并促进了远程调试。他们强调了高通致力于改善开发者体验并使其平台更加开放。

---

## 22. 适用于JVM的Embabel代理框架

**原文标题**: Embabel Agent Framework for the JVM

**原文链接**: [https://github.com/embabel/embabel-agent](https://github.com/embabel/embabel-agent)

Embabel：用于构建智能代理流程的JVM框架，它融合了LLM交互与代码和领域模型。它支持复杂的规划，通过在条件和领域模型的指导下执行动作来达成目标。与简单的状态机不同，Embabel使用非LLM的AI算法进行动态规划，适应新信息并实现超出初始编程的任务。这促进了可扩展性和重用性；添加新的领域对象、动作、目标和条件可以增强系统功能，而无需更改现有代码。

主要特性包括强类型、平台抽象、LLM混合以实现成本效益，以及与Spring和JVM的集成以实现企业功能。Embabel允许通过注解或Kotlin DSL进行代理创作，两者都由丰富的领域模型支持。其规划步骤是可插拔的，默认使用GOAP。

执行模式包括专注型（代码驱动）、封闭型（基于意图选择代理）和开放型（平台寻找合适的目标并构建自定义代理）。开放模式功能强大但确定性较低，允许采用新颖的路径。未来的模式设想了不断发展的流程以及与其他代理系统的联邦。

Embabel通过提供更高级别的API（类似于Spring MVC与Servlet API），解决了现有代理框架的局限性，从而促进了测试、可组合性、健壮性和安全性。它旨在利用JVM现有的代码和基础设施资产。该项目实践“极限实践”，使用AI代理来自动化开发任务并改进平台本身。快速入门选项包括使用Java或Kotlin GitHub模板或项目创建工具。

---

## 23. 展示HN：可自托管的IRS直接报税系统延续版

**原文标题**: Show HN: A continuation of IRS Direct File that can be self-hosted

**原文链接**: [https://github.com/openfiletax/openfile](https://github.com/openfiletax/openfile)

OpenFile：免费自托管报税工具

OpenFile 是一个免费、可自托管的报税工具，它从美国国税局的 Direct File 项目衍生而来。它允许用户直接申报税务，并且其源代码可供修改和独立托管。

要运行 OpenFile，用户需要 Docker。该工具可以使用单个命令部署：`docker compose up -d`。部署完成后，OpenFile 客户端可以通过 `localhost:3000/df/file` 访问。

`https://docs.openfile.tax/en/latest/direct-file.html` 上的文档提供了有关该项目及其功能的更多信息。本质上，OpenFile 旨在为税务申报提供一个免费且开源的替代方案，建立在美国国税局 Direct File 项目奠定的基础上。

---

## 24. Cloudflare将为AI机器人引入按次爬取付费模式

**原文标题**: Cloudflare to introduce pay-per-crawl for AI bots

**原文链接**: [https://blog.cloudflare.com/introducing-pay-per-crawl/](https://blog.cloudflare.com/introducing-pay-per-crawl/)

Cloudflare推出“按爬取付费”机制，内容创作者可向访问其内容的人工智能爬虫收费。这解决了许多发布者面临的二元选择：要么允许免费访问，要么创建围墙花园。“按爬取付费”提供了第三种选择：以互联网规模的有偿访问，利用HTTP响应代码402。

发布者获得了精细的控制权，可以为整个站点定义统一的、按请求收费的价格，并可选择允许免费访问、收取配置的价格或阻止访问。即使是被阻止的爬虫也会收到“收费”通知，预示着未来潜在的关系。发布者可以灵活地绕过对特定爬虫的收费，以适应系统之外的合作关系。

该系统使用Web Bot Auth提案来实现安全的爬虫识别和收费。爬虫生成密钥对，向Cloudflare注册，并在每个请求中使用HTTP消息签名。

爬虫可以通过被动（先发现，遇到402错误并重试以支付）或主动（先声明意图，指定最高价格）流程访问内容。Cloudflare负责财务结算，汇总事件、向爬虫收费，并将收益分配给发布者。

Cloudflare设想“按爬取付费”未来将发展为支持动态定价、精细化许可和智能代理的程序化协商。他们强调了人工智能代理根据预定义预算访问和合成信息的潜力。

“按爬取付费”目前处于私有测试阶段，Cloudflare鼓励感兴趣的爬虫和内容创作者注册。

---

## 25. Proton加入针对苹果损害开发者和消费者利益行为的诉讼

**原文标题**: Proton joins suit against Apple for practices that harm developers and consumers

**原文链接**: [https://proton.me/blog/apple-lawsuit](https://proton.me/blog/apple-lawsuit)

在2025年6月，Proton在美国加入了一项针对苹果的集体诉讼，指控其应用商店存在损害开发者和消费者的反竞争行为。Proton认为苹果的政策违反了美国反垄断法，并旨在确保美国开发者和消费者不会像在欧盟那样处于不利地位，因为苹果已经在欧盟面临处罚。

Proton强调了几个担忧：苹果的应用商店政策通过其30%的应用商店费用不成比例地影响了注重隐私的公司，从而助长了监视资本主义；苹果应专制政权的要求进行的审查行为扼杀了自由和民主；限制性的订阅管理系统导致更差的用户体验，并且苹果有意削弱第三方应用程序；苹果的应用商店费用相当于对互联网商业征收人为税，导致价格上涨。

Proton寻求结束应用商店中的反竞争行为，并确保苹果的实践发生真正的改变。Proton收到的任何金钱赔偿将捐赠给为民主和人权而战的组织。他们认为结果将使该市场中的所有应用程序开发者和用户受益，而不仅仅是他们自己，并希望树立一个先例，即自由的人民，而不是垄断企业，来决定互联网的未来。Proton由Quinn Emanuel Urquhart & Sullivan LLP和Cohen Milstein Sellers & Toll PLLC代理。

---

## 26. RP2350pc 开源一体机

**原文标题**: RP2350pc Open Source Hardware all in one computer

**原文链接**: [https://olimex.wordpress.com/2025/07/01/rp2350pc-open-source-hardware-all-in-one-computer-with-rp2350b-8mb-psram-16mb-flash-four-usb-host-dvi-hdmi-output-and-audio-codec-for-retro-computer-emulation-and-education/](https://olimex.wordpress.com/2025/07/01/rp2350pc-open-source-hardware-all-in-one-computer-with-rp2350b-8mb-psram-16mb-flash-four-usb-host-dvi-hdmi-output-and-audio-codec-for-retro-computer-emulation-and-education/)

本文介绍RP2350pc，一款专为复古电脑模拟和教育设计的开源硬件一体机。它搭载RP2350B处理器，一款双核ARM/RISC-V芯片，配备520KB RAM、8MB PSRAM和16MB Flash。

主要特性包括四个USB端口、两个UEXT连接器、DVI/HDMI输出、带麦克风输入和耳机输出（外加外置扬声器放大器）的音频编解码器、SD卡槽、用于电池供电的LiPo UPS，以及两个USB-C端口（一个用于供电，一个用于编程）。此外还包括一个电源开关。

RP2350pc旨在创建具有键盘和电视输出的复古风格ARM/RISC-V计算机，使其适用于游戏和教育用途。Veselin Sladkov正在开发对该平台的Reload模拟器支持，旨在实现对Apple ][、Oric Atmos和Puldin 601等系统的模拟。Paul Robson也在开发RP2350pc API，以方便创建具有统一BIOS的编译器和操作系统。

---

## 27. Show HN: ToplingDB - 用于外部存储的持久化键值存储

**原文标题**: Show HN: ToplingDB - A Persistent Key-Value Store for External Storage

**原文链接**: [https://github.com/topling/toplingdb](https://github.com/topling/toplingdb)

生成摘要时出错

---

## 28. 抽象边界即优化边界

**原文标题**: Abstraction boundaries are optimization boundaries

**原文链接**: [https://blog.snork.dev/posts/abstraction-boundaries-are-optimization-boundaries.html](https://blog.snork.dev/posts/abstraction-boundaries-are-optimization-boundaries.html)

本文论证了抽象边界充当优化边界，并以 N+1 查询问题为例。N+1 查询问题，即应用程序发出多个冗余 SQL 查询，通常源于泄露的 ORM 抽象，无法自动将多个单行获取优化为单个批量查询。

作者建议，与其降低抽象边界并手动优化查询，不如提升抽象边界，将 ORM 纳入语言本身。这将使编译器能够理解 ORM 的操作并应用重写规则来优化查询，例如将 N 个查询合并为一个。

作者还以 Haskell 通过流融合对列表操作的重写规则为例。这种优化之所以可行，是因为 Haskell 的声明式特性抽象掉了底层操作语义，从而允许编译器级别的优化。

核心思想是通过提升抽象边界，我们可以同时扩大优化范围。本质上，编译器优化代码的能力直接受到其理解能力的限制；提升抽象边界以包含更多功能，使编译器能够获得更深入的洞察力和更大的优化潜力。

---

## 29. Claude Code 现在支持 hooks 了

**原文标题**: Claude Code now supports hooks

**原文链接**: [https://docs.anthropic.com/en/docs/claude-code/hooks](https://docs.anthropic.com/en/docs/claude-code/hooks)

本文介绍 Claude Code 钩子，这是一种用户自定义的 Shell 命令，可在 Claude Code 生命周期的各个阶段执行，从而对其行为提供确定性的控制。 钩子可用于通知、自动格式化、日志记录、反馈和自定义权限。

钩子在设置文件（用户、项目、本地项目）中配置，并按匹配器组织，这些匹配器定义钩子的运行时间。 本文详细介绍了使用 JSON 的钩子配置结构，包括“EventName”、“matcher”和“hooks”字段。 它概述了不同的钩子事件：PreToolUse（工具调用之前）、PostToolUse（工具完成之后）、Notification 和 Stop，每个事件都有特定的用例和可用的匹配器。

钩子通过 stdin 接收 JSON 数据，其中包含会话信息和特定于事件的数据。 它们可以使用退出代码（0 表示成功，2 表示阻塞错误，其他表示非阻塞错误）或通过在 stdout 中返回结构化的 JSON 来与 Claude Code 通信。 JSON 输出允许控制 Claude 的继续、决策（批准/阻止）以及提供反馈。

本文还介绍了如何使用具有特定命名模式的模型上下文协议 (MCP) 工具，并提供了代码格式化和自定义通知的示例。 它强调了安全注意事项，突出了执行任意 Shell 命令的风险，并提供了编写安全钩子的最佳实践。 主要建议是输入验证、正确引用、路径遍历预防和使用绝对路径。 本文还详细介绍了执行限制、环境和调试信息。

---

## 30. Claude Code 现在支持 hooks 了

**原文标题**: Claude Code now supports hooks

**原文链接**: [https://docs.anthropic.com/en/docs/claude-code/hooks](https://docs.anthropic.com/en/docs/claude-code/hooks)

本文介绍了 Claude Code 钩子，这是一种用户自定义的 Shell 命令，可在 Claude Code 生命周期中的不同阶段执行，以提供确定性控制并扩展其行为。 钩子可以实现自动化，用于通知、代码格式化、日志记录、反馈和自定义权限等任务。

钩子在 JSON 设置文件（用户、项目和本地）中配置，并按“事件”（PreToolUse、PostToolUse、Notification、Stop）和“匹配器”（工具名称或模式）进行组织。 它们通过 stdin 接收 JSON 数据，并可以返回输出（退出代码或结构化 JSON）以影响 Claude Code 的行为，包括阻止操作和提供反馈。

PreToolUse 钩子在工具调用之前运行，允许进行验证和修改。 PostToolUse 钩子在工具成功执行后运行。 Notification 钩子用于自定义通知，而 Stop 钩子用于控制 Claude Code 何时完成响应。 本文档详细介绍了每种钩子类型的特定输入/输出格式，包括如何使用 JSON 来批准或阻止操作并提供原因。 提供了代码格式化和通知自定义的示例。

本文档强调了安全注意事项，强调用户对其钩子的安全负责，并提供了编写安全钩子的最佳实践，例如输入验证、正确引用和防止路径遍历。 它还详细介绍了钩子执行细节，如超时、并行化、环境和调试技术。 最后，它解释了钩子如何与模型上下文协议 (MCP) 工具集成。

---

## 31. 布莱切利园的普通棋手与英国的人工智能研究

**原文标题**: The average chess players of Bletchley Park and AI research in Britain

**原文链接**: [https://blogs.bl.uk/science/2025/06/the-average-chess-players-of-bletchley-park-and-ai-research-in-britain.html](https://blogs.bl.uk/science/2025/06/the-average-chess-players-of-bletchley-park-and-ai-research-in-britain.html)

无法访问文章链接。

---

## 32. Xfinity利用家中WiFi信号探测动作

**原文标题**: Xfinity using WiFi signals in your house to detect motion

**原文链接**: [https://www.xfinity.com/support/articles/wifi-motion](https://www.xfinity.com/support/articles/wifi-motion)

这篇Xfinity支持页面片段主要介绍Xfinity的“WiFi Motion”功能。它暗示Xfinity利用家中现有的WiFi信号来检测运动。该页面可能解释了如何通过Xfinity应用程序使用此功能。然而，由于片段的不完整性，关于其功能、隐私影响、设置过程和潜在局限性的详细信息缺失。该片段还强调需要启用JavaScript才能使Xfinity支持网站的全部功能生效。版权声明表明信息截至2025年仍然有效。

---

## 33. PlanetScale 的 Postgres 支持

**原文标题**: PlanetScale for Postgres

**原文链接**: [https://planetscale.com/blog/planetscale-for-postgres](https://planetscale.com/blog/planetscale-for-postgres)

PlanetScale推出PlanetScale for Postgres私有预览版，这是在PlanetScale Metal发布后，应客户需求推出的全新Postgres托管平台。许多公司要求支持Postgres，促使PlanetScale开发了这项新产品。

PlanetScale旨在提供优于现有Postgres托管解决方案的性能和可靠性，理由是客户抱怨现有平台的停机、性能不佳和高成本。他们的内部基准测试表明，即使资源分配较少，PlanetScale for Postgres的性能也优于竞争对手，这得益于真实的Postgres和PlanetScale Metal的本地连接NVMe SSD。

主要功能包括真正的具有自动故障转移的高可用性、查询缓冲、通过PSBouncer的连接池、Postgres v17支持、从Postgres v13+的在线导入以及无需停机的自动版本更新。

虽然PlanetScale在MySQL的数据库扩展方面表现出色，但他们正在从第一性原理构建一个新系统，以便为Postgres带来类似的扩展能力，并根据Postgres的优势量身定制。他们计划发布更多关于这个新系统的信息并提供早期访问。

PlanetScale鼓励大规模运行Postgres的有兴趣的公司联系他们。该公告最后邀请大家注册私有预览等候名单。

---

## 34. GPEmu: 用于快速、低成本深度学习原型设计的GPU模拟器 [pdf]

**原文标题**: GPEmu: A GPU emulator for rapid, low-cost deep learning prototyping [pdf]

**原文链接**: [https://vldb.org/pvldb/vol18/p1919-wang.pdf](https://vldb.org/pvldb/vol18/p1919-wang.pdf)

GPEmu：用于快速、低成本深度学习原型设计的GPU模拟器。本文讨论了深度学习研究和原型设计中访问和利用GPU所面临的挑战，包括与云端GPU服务相关的高成本、有限可用性和配额限制。提出的解决方案是GPEmu，一种旨在实现快速、低成本深度学习模型原型设计的GPU模拟器。GPEmu提供了一种在通用硬件上模拟GPU行为和性能的方法，使研究人员和开发人员无需昂贵的GPU或云资源，即可试验不同的模型架构、训练策略和优化技术。本文档包含许多内部和外部超链接。

---

## 35. 一个时代的终结

**原文标题**: End of an Era

**原文链接**: [https://www.erasmatazz.com/personal/self/end-of-an-era.html](https://www.erasmatazz.com/personal/self/end-of-an-era.html)

本文写于2025年6月29日，反思了作者数十年来通过电脑游戏和故事讲述工具创作“互动艺术”的追求。他回忆了他在雅达利公司的早期工作，包括游戏《八卦》，以及他后来试图创作亚瑟王游戏的经历，但因雅达利的倒闭而搁浅。

在他的艺术 vision 的驱动下，他开发了“Erasmatron”，后来又开发了“Storytron”，这些软件开发环境旨在授权其他人创作互动故事世界。尽管它们具有创新功能，包括“Deikto”玩具语言，但这些工具未能获得认可，对于目标受众来说过于复杂。

作者随后将精力投入到“Siboot”中，试图展示 Storytron 的功能，但最终认为它失败了。灰心丧气之后，他最终回到了最初的雄心壮志：创作亚瑟王游戏。这最终促成了《亚瑟之死》的诞生，他认为这是成功的，最终实现了他创作真正的互动艺术的目标。

尽管玩家参与度有限，但他仍然为自己的创作感到自豪。他最后一次尝试在 Narrascope 上与互动小说社区分享他的技术失败了，原因是技术问题和缺乏后续兴趣。作者的结论是，他在推进互动故事讲述的更广泛目标上失败了，并且承认世界还没有准备好接受他的 vision，将自己比作查尔斯·巴贝奇。他认为他的游戏《亚瑟之死》是一部隐喻性的自传，反映了亚瑟未能拯救他的人民，但激励了后代。

---

## 36. 冥王星是一种独特的Lua方言，专注于通用编程。

**原文标题**: Pluto is a unique dialect of Lua with a focus on general-purpose programming

**原文链接**: [https://github.com/PlutoLang/Pluto](https://github.com/PlutoLang/Pluto)

Pluto是一种Lua方言，旨在用于通用编程，在保持Lua兼容性的前提下，优先考虑加速开发和增强功能。它提供了丰富的标准库，并新增了如switch语句和三元表达式等语法。

Pluto在很大程度上与Lua 5.4源代码兼容，潜在冲突可能来自新增关键字。这些冲突可以使用“兼容模式”来缓解。它还可以执行Lua 5.4字节码，并且大多数Pluto功能都会生成兼容的字节码。有一部分Pluto功能不兼容，但有文档记录，以便在需要字节码兼容性时可以避免使用。Pluto项目积极跟进Lua主仓库的更新，目标是在Lua 5.5发布后进行更新。

Pluto网站（也是开源的）提供了全面的文档，涵盖入门、工具和功能改进。用户可以通过交互式Web Playground快速体验Pluto，或者使用预构建的二进制文件。工具包括Pluto语法高亮显示和专用的语言服务器。

---

## 37. 人们不停地发明概率树

**原文标题**: People Keep Inventing Prolly Trees

**原文链接**: [https://www.dolthub.com/blog/2025-06-03-people-keep-inventing-prolly-trees/](https://www.dolthub.com/blog/2025-06-03-people-keep-inventing-prolly-trees/)

多次发现现象：Dolt关键数据结构 Prolly Trees 的独立发明史

本文探讨了多次发现现象，即同一发明在同一时期被多个个人或团体独立构思出来。作者认为，对于Dolt至关重要的数据结构 Prolly Trees 就是一个典型的例子，它至少被以不同的名称独立发明了四次。

作者追溯了 Prolly Trees 的历史，始于2009年 Avery Pennarun 的 bup，这是一个用于文件系统备份的工具，它使用了 Prolly Trees 的核心原理，但没有命名它们。文章随后重点介绍了 Noms 在 2015 年对“Prolly Trees”的正式定义，以及 2019 年 Inria 研究人员独立发现的“Merkle Search Trees”，以及 2020 年 DePaul 大学独立发现的“Content-Defined Merkle Trees”。每项发明的出现都是为了应对不同的需求，从分布式 CRDT 到高效的容器交付，并且每个发明都有独特的实现细节。

文章强调，Prolly Trees 建立在内容定义分块、滚动哈希函数和 Merkle 树等现有概念之上，使得它们的最终发现几乎是不可避免的。作者最后提出了一个问题，即哪个名称——Prolly Tree、Merkle Search Tree 或 Content-Defined Merkle Tree——最终会成为标准，同时由于其先例和 DoltHub 对该术语的现有投资，作者主张使用“Prolly Tree”。 最终，这篇文章赞扬了 prolly trees 在各个领域的力量和影响。

---

## 38. Hacker News 上的 AI 创业点子

**原文标题**: HN Slop: AI Startup Ideas from Hacker News

**原文链接**: [https://www.josh.ing/hn-slop](https://www.josh.ing/hn-slop)

本文题为“HN Slop：来自 Hacker News 的 AI 创业点子”，旨在提供由人工智能生成的创业点子，这些点子来源于 Hacker News 首页的最新讨论。标题“HN Slop”颇具玩味，暗示其中既有潜在价值，也有不太成熟的想法。文章的主要功能似乎是自动分析 Hacker News 上的热门话题，然后利用人工智能进行头脑风暴，提出相关的创业概念。这种自动化流程意味着专注于根据当前科技趋势和 Hacker News 社区内的讨论来识别机会。简短的文本表明，该流程目前正在运行中，人工智能正在分析当前的 HN 帖子以生成创业点子。

---

## 39. 墨尔本男子在房屋下发现大型火车模型网络

**原文标题**: Melbourne man discovers extensive model train network underneath house

**原文链接**: [https://www.sbs.com.au/news/article/i-was-shocked-melbourne-mans-unbelievable-find-after-buying-house/m4sksfer8](https://www.sbs.com.au/news/article/i-was-shocked-melbourne-mans-unbelievable-find-after-buying-house/m4sksfer8)

火车迷丹尼尔·徐在墨尔本购房后，做出了一个惊人的发现：他在房子底下找到了一个庞大的火车模型网络，而购买过程中对此只字未提。

这个精心设计的装置，有着复杂的铁路线和微缩景观，是由前房主的父亲在20世纪60年代建造的。多年来，这个网络几乎未被触及，积满了灰尘和蜘蛛网。

对徐来说，这个发现简直是梦想成真，与他毕生对火车的 passion 完美契合。他受到一部关于打击犯罪火车的日本卡通片的启发。

尽管这个项目出乎意料，但徐致力于修复这个老式火车模型网络。他计划清理轨道，评估哪些还能运行，并升级控制技术，与新一代人分享他对火车的喜爱。即使没有通电，这套火车模型也已经迷住了邻里儿童。

---

## 40. 与衰老相关的炎症并非普遍存在于所有人类群体中。

**原文标题**: Aging-related inflammation is not universal across human populations

**原文链接**: [https://www.publichealth.columbia.edu/news/aging-related-inflammation-not-universal-across-human-populations](https://www.publichealth.columbia.edu/news/aging-related-inflammation-not-universal-across-human-populations)

这项发表在《自然衰老》上的哥伦比亚大学研究挑战了炎症是衰老普遍标志的观点。研究人员发现，“炎症衰老”，即与年龄相关的慢性、低度炎症，在工业化人群中更为普遍，可能是其生活方式的副产品。

该研究比较了两个工业化群体（意大利和新加坡）与两个土著、非工业化群体（玻利维亚的奇马内人和马来西亚的奥朗阿斯利人）的炎症水平。虽然工业化人群显示炎症与衰老之间存在明显联系，但在土著群体中并非如此，他们的炎症主要由感染驱动。有趣的是，尽管土著群体中的炎症水平很高，但他们并没有经历与工业化社会中炎症衰老相关的相同慢性疾病。

该研究表明，炎症是“情境依赖性的”，受环境暴露、生活方式和感染负担的严重影响。该研究使用了一组19种细胞因子来评估炎症模式，这些模式与工业化人群的衰老相关，但在土著群体中则不然。

作者呼吁重新评估如何在不同人群中衡量衰老和炎症，强调需要标准化、具有情境意识的工具。他们提出，身体活动、饮食和感染等因素可能会相互作用，影响免疫系统衰老的方式，这可以为更有效的全球健康策略提供信息。

---

## 41. 索尼DTC-700音频DAT播放录音机

**原文标题**: Sony DTC-700 audio DAT player/recorder

**原文链接**: [https://kevinboone.me/dtc-700.html](https://kevinboone.me/dtc-700.html)

本文是对索尼DTC-700 DAT（数字音频磁带）播放器/录音机以及DAT格式的回顾。作者认为，DAT提供了优于卡带的音质，可与CD媲美，并具有录音功能。DAT允许直接从CD和模拟源进行数字录音。

尽管有其优点，但DAT未能取得主流成功，原因有几个。播放器的高成本，加上缺乏商业发行的DAT音乐，阻碍了其普及。录音行业对数字复制的担忧，导致对DAT设备的法律限制和税收，进一步促成了其衰落。DTC-700也采用了防复制措施。

在技术上，DAT很复杂，它使用类似于VHS录像机的旋转磁头，以便在窄磁带上实现高数据带宽。这种复杂性导致了可靠性问题，DTC-700中使用塑料部件加剧了这一问题。作者认为，市场饱和，该格式几乎没有改进或创新的机会，最终决定了DAT的命运。虽然像黑胶唱片和卡带这样的其他复古音频格式已经复兴，但作者怀疑DAT是否会享受同样的复兴。虽然有现代的录音替代方案，例如带有声卡的计算机，但DAT曾经占据的利基市场不再需要了。

---

## 42. Pbf2sqlite：将OpenStreetMap数据读取到SQLite数据库

**原文标题**: Pbf2sqlite: Reading OpenStreetMap into a SQLite Database

**原文链接**: [https://github.com/osmzoso/pbf2sqlite](https://github.com/osmzoso/pbf2sqlite)

`pbf2sqlite` 是一个命令行工具，用于将 OpenStreetMap (.osm.pbf) 数据导入到 SQLite 数据库中。它的主要功能是将 OSM PBF 格式转换为结构化的 SQLite 数据库格式。

基本用法是 `pbf2sqlite DATABASE [OPTION ...]`，其中 `DATABASE` 是要创建或修改的 SQLite 数据库的名称。

主要选项包括：

*   `read FILE`: 指定要读取并导入到数据库中的 .osm 或 .osm.pbf 文件。
*   `rtree`: 添加 R*Tree 索引以提高空间查询性能。
*   `addr`: 创建地址表来存储从 OSM 数据中提取的地址信息。
*   `graph`: 生成图表，可能代表 OpenStreetMap 数据的网络结构，用于路由或网络分析。

该工具可用于创建数据库并使用 OSM PBF 文件中的数据填充它，如示例 `pbf2sqlite test.db read country.osm.pbf` 所示。 可以从 Geofabrik 等提供商处获取适合导入的 OSM 数据。 文章还提到下载最新版本（工具），但没有提供链接或有关在哪里获取的其他信息。

---

## 43. 二手电脑的CarFax；惠普希望让旧笔记本电脑焕发新生

**原文标题**: A CarFax for Used PCs; Hewlett Packard wants to give old laptops new life

**原文链接**: [https://spectrum.ieee.org/carmax-used-pcs](https://spectrum.ieee.org/carmax-used-pcs)

惠普计划打造二手电脑界的“CarFax”，为旧笔记本电脑赋予新生。本文由惠普的Abu Baker、Sal Vasi、Barbara Spitzer和John Hong撰写，概述了惠普旨在提高二手电脑市场透明度和信任度的战略。

核心理念是提供一份标准化的报告，类似于车辆的CarFax，详细说明二手笔记本电脑的历史和状况。该报告可能包括原始规格、维修历史、组件更换以及对其当前性能的详细诊断评估等信息。

该计划旨在解决二手电脑市场买家的常见担忧，例如对笔记本电脑实际状况的不确定性以及潜在的隐藏问题。通过提供可靠和经过验证的信息，惠普旨在增强消费者的信心，鼓励购买翻新笔记本电脑，从而促进可持续性并减少电子垃圾。最终，惠普设想建立一个更加透明和值得信赖的二手电脑买卖生态系统。

---

## 44. YouTube 无需翻译

**原文标题**: YouTube No Translation

**原文链接**: [https://addons.mozilla.org/en-GB/firefox/addon/youtube-no-translation/](https://addons.mozilla.org/en-GB/firefox/addon/youtube-no-translation/)

"YouTube No Translation" Firefox 扩展程序可阻止 YouTube 上的自动翻译，确保更原汁原味的观看体验。它保留视频标题和描述的原始语言，并默认使用原始音轨，即使在 Shorts 上也是如此。用户可以选择自己喜欢的字幕语言，如果所选语言不可用，则会自动禁用（始终忽略自动生成的字幕）。

主要功能包括防止翻译视频标题和描述，强制使用原始音轨，以及控制字幕语言。

该扩展程序是开源的，开发者鼓励用户通过 Ko-fi 支持其开发。用户可以在 GitHub 上报告问题或请求功能。它需要访问 youtube.com 和 youtube-nocookie.com 域上的数据，并提供可选权限以增强功能。最新版本 2.5.0 添加了对标题和搜索描述的 YouTube Data API v3 支持。

---

## 45. 原LZEXE (又名 Kosinski) 压缩器源代码已发布。

**原文标题**: The original LZEXE (A.K.A. Kosinski) compressor source code has been released

**原文链接**: [https://clownacy.wordpress.com/2025/05/24/the-original-lzexe-a-k-a-kosinski-compressor-source-code-has-been-released/](https://clownacy.wordpress.com/2025/05/24/the-original-lzexe-a-k-a-kosinski-compressor-source-code-has-been-released/)

本文宣布发布LZEXE的原始源代码，LZEXE是由Fabrice Bellard在90年代初开发的DOS可执行文件压缩器，之前被称为“Kosinski”格式，曾用于一些Mega Drive游戏中。0.91版本的源代码已在MIT许可下发布，允许免费使用和修改。

作者Clownacy解释了他们之前对Kosinski压缩器的逆向工程工作，并指出Mega Drive Sonic游戏中发现的压缩数据与Mega CD BIOS之间存在差异，这表明可能使用了具有不同错误或优化的不同压缩器版本。

虽然发布的源代码可能与Sonic游戏中使用的压缩器并不完全匹配，但可以与现有可执行文件的反汇编二进制文件进行比较。该源代码的发布代表了在理解Mega Drive上使用的“KENS”压缩格式方面的一个重大进展，现在已经有了Kosinski和Saxman的源代码。然而，由于Enigma和Nemesis的定制性质以及可能由世嘉内部开发，作者并不乐观能够找到剩余的“KENS”格式的源代码。本文包含一个指向Devon提取核心压缩逻辑的工作的链接，并鼓励读者在社交媒体上分享这一消息。

---

## 46. 实验游乐场

**原文标题**: Experimental Playgrounds

**原文链接**: [https://mssv.net/2025/01/26/experimental-playgrounds/](https://mssv.net/2025/01/26/experimental-playgrounds/)

实验性游乐场：战争创伤的回应及现代启示

---

## 47. 吉姆·博迪在贝尔实验室共同开发了首个成功的DSP。

**原文标题**: Jim Boddie codeveloped the first successful DSP at Bell Labs

**原文链接**: [https://spectrum.ieee.org/dsp-pioneer-jim-boddie](https://spectrum.ieee.org/dsp-pioneer-jim-boddie)

本文纪念吉姆·博迪，一位数字信号处理(DSP)领域的先驱，他在贝尔实验室共同开发了首个成功的DSP。博迪曾在位于新泽西州霍姆德尔的AT&T贝尔实验室工作，在那里他帮助设计了这款开创性的半导体。本文重点介绍了他在该领域的重要贡献，并引用了史蒂夫·沃尔特斯（与博迪在贝尔实验室DSP1上合作，设计I/O电路和DSP开发系统）和帕特·海斯（贝尔实验室计算机芯片的主要开发人员）的见解。本文强调了博迪作为架构师和设计师，对这项关键技术发展所产生的重大影响。

---

## 48. 小型语言模型是自主人工智能的未来。

**原文标题**: Small language models are the future of agentic AI

**原文链接**: [https://arxiv.org/abs/2506.02153](https://arxiv.org/abs/2506.02153)

这篇于2025年6月2日提交的arXiv论文认为，小型语言模型(SLM)是自主型人工智能的未来。虽然大型语言模型(LLM)因其通用能力而受到赞誉，但作者认为，对于自主系统中常见的重复性、专业化任务而言，SLM 既足够强大，也更适合，并且更经济。

作者Peter Belcak等人基于SLM的现有能力、自主系统的架构以及SLM部署的成本效益来支持他们的观点。他们认为，对于需要更广泛对话能力的情况，异构自主系统（使用多个模型的智能体）是最佳解决方案。

该论文指出了SLM应用可能面临的障碍，并提出了一种通用的LLM到SLM智能体转换算法。其核心论点是一个价值陈述，强调在人工智能智能体行业中，即使是部分地从LLM转向SLM，也能带来显著的运营和经济效益。

作者旨在引发关于高效人工智能资源利用和降低人工智能成本的讨论。他们欢迎对其立场的反馈，并承诺在提供的URL上公开所有通信。该论文归类于人工智能（cs.AI）领域。

---

## 49. 废弃物变建材：再生资源地质聚合物

**原文标题**: Waste into Construction Materials: Geopolymers from Recycled Sources

**原文链接**: [https://www.mdpi.com/2313-4321/10/3/118](https://www.mdpi.com/2313-4321/10/3/118)

我无法访问外部链接，因此无法总结文章。我的回复是：

无法访问文章链接。

---

## 50. 展示HN：卓越的免费模板、组件库和样板代码

**原文标题**: Show HN: Exceptional free templates, component libraries and boilerplates

**原文链接**: [https://htmlrev.com/](https://htmlrev.com/)

HTMLrev 展示了面向 Web 开发人员的大量免费模板、组件库和样板代码。这些资源涵盖了广泛的框架和技术，满足各种项目需求。

列出的框架和技术包括：HTML、Bootstrap、Tailwind、Shadcn、Material、Bulma、Angular、React、Next.js、Vue、Nuxt、Svelte、Gatsby、Astro、Laravel、Django、Jekyll、Hugo 和 BCMS。对于每个框架，都重点介绍了多个免费模板，涵盖各种类别，例如企业网站、着陆页、管理仪表板、作品集和文档站点。

针对每个类别都给出了具体示例，例如 HTML 的“Solid”，Bootstrap 的“Boldo”，Tailwind 的“Landing Page”以及 Shadcn 模板的“Shadcn Landing Page”。同样，还展示了其他框架的免费模板，每个模板都对其设计和功能进行了简要描述。

该页面还设有赞助商位，重点介绍了网站构建器、管理仪表板模板提供商、UI 组件库和编码工具，例如 Unicorn Platform、WrapPixel、BCMS、ThemeSelection、CodedThemes、Shadcnblocks 和 Superflex。这些赞助商提供免费和高级 Web 开发资源。除了特定模板外，还提到了几个 UI 工具包和设计系统。

---

## 51. 在可调整大小的窗口中镜像外部显示器的微型macOS实用工具

**原文标题**: Tiny macOS utility that mirrors an external monitor in a resizable window

**原文链接**: [https://www.beeno.app/](https://www.beeno.app/)

Beeno：一款在主屏幕可调整大小的窗口中镜像外部显示器显示的轻量级 macOS 实用工具。它尤其适用于检查演示文稿、演示或共享内容，无需复杂的桌面重新排列。该工具专为 Capture One 用户设计，方便数码操作员轻松地将放大图像或实时视图投影到另一个屏幕上，供客户或摄影师查看。

使用 Beeno：下载并解压该应用程序，将其移动到“应用程序”文件夹（可选），首次启动时绕过 Gatekeeper（右键单击 -> 打开 -> 打开），并授予其“屏幕录制”和“系统音频录制”权限。运行后，菜单栏中会显示一个蜜蜂图标。左键单击该图标可切换预览窗口的显示/隐藏，右键单击可在镜像显示器之间切换，右键单击还提供退出选项。快捷键 ⌥B 也能显示/隐藏预览窗口。Beeno 以 .zip 文件形式提供下载，并采用 CC BY-NC-ND 4.0 许可。

---

## 52. 公共信号备份测试

**原文标题**: Public Signal Backups Testing

**原文链接**: [https://community.signalusers.org/t/public-signal-backups-testing/69984](https://community.signalusers.org/t/public-signal-backups-testing/69984)

Signal正在安卓平台上通过staging build发布其全新端到端加密备份系统的公开测试版。该备份系统提供以下几个用户呼声很高的功能：

*   **托管备份：** Signal托管备份，即使本地备份丢失也能保护数据。
*   **动态媒体卸载：** 通过允许在需要时动态下载媒体来优化存储。
*   **跨平台兼容性：** 备份格式可被所有客户端读取，支持在Android和iOS之间进行恢复。
*   **免费和付费层级：** 免费层级备份所有文本内容和最近45天的媒体。付费层级提供100GB的媒体存储空间。

安全和隐私至关重要：备份是端到端加密的，默认禁用，并旨在防止Signal将备份或付款与特定用户关联。

目前测试仅在Android上通过自更新APK提供。我们鼓励测试人员探索用户界面，测试极端情况（例如在备份期间或备份前后发送媒体），并提供关于错误、令人困惑的描述、缺失的功能以及性能问题的反馈。该帖子概述了如何为了测试目的而覆盖免费/付费层级设置。

本地备份仍然存在，并且正在通过新的跨平台格式和基于差异的写入来改进，以实现更快的备份。该帖子还解决了关于阅后即焚消息的问题，强调大多数消息将被备份（除了那些接近过期或一次性查看的消息），并提供了未来发布的计划时间表。

---

## 53. 修复ZX Spectrum+ Toastrack

**原文标题**: Restoring a ZX Spectrum+ Toastrack

**原文链接**: [https://celso.io/posts/2025/06/28/toastrack/](https://celso.io/posts/2025/06/28/toastrack/)

本文详细介绍了ZX Spectrum+ 128K“烤面包架”电脑的修复和改进过程。作者是一位复古计算爱好者，回忆了童年时期的Spectrum电脑，并描述了修复过程。

初步评估显示，机器状况相对良好，但需要一些基本维修。作者重焊了主集成电路上的焊点，以解决启动问题，并解决了7805电压调节器过热问题，将其更换为更凉爽的DD2712SA降压转换器（后来考虑到潜在的噪声问题，又考虑了更好的替代方案）。 添加了一个带有电容器的滤波器来减轻噪声问题。 清理并重新焊接了边缘连接器，以改善外围设备的连接。

实施了多项视频质量改进，包括TEA2000芯片上的色度滤波器，以及从复合和RGB信号中移除调制音频。 作者还将复合视频信号路由到RCA连接器。 这些改装显着改善了复合视频输出。

更换了臭名昭著的不可靠的薄膜键盘，并彻底清洁了外壳和按键。 更换了单声道音频插孔，作者讨论了一种用于连接现代音频设备的立体声转单声道电缆，还提到了潜在的音频平衡问题以及他未应用的解决方案。

最后，作者利用128K的RGB视频输出与RGB2HDMI适配器连接，实现了清晰的HDMI显示。 然后使用游戏和演示测试了修复后的“烤面包架”，展示了其恢复的全部功能，最后推广了Backbit卡带。

---

## 54. 混合物的熵

**原文标题**: Entropy of a Mixture

**原文链接**: [https://cgad.ski/blog/entropy-of-a-mixture.html](https://cgad.ski/blog/entropy-of-a-mixture.html)

本文探讨了混合分布 pλ = (1 - λ)p0 + λp1 的熵，以及其形状如何揭示关于分量分布 p0 和 p1 之间关系的信息。作者强调，熵的凹性导致 H(pλ) 相对于 λ 的图表中出现“向上凸起”。

关键一点是，“凸起”对应于从 pλ 中抽取的样本与指示样本来源（p0 或 p1）的伯努利变量 A 之间的互信息 I(X;A)。此互信息可以使用 p0、p1 和 pλ 之间的 KL 散度来表达。

本文介绍了“倾向性”的概念，Pc(p1, p0)，它衡量将少量 p1 混入 p0 时熵的初始变化。它将倾向性与熵、KL 散度以及相对于温度的交叉熵变化联系起来。

对于小的 λ，互信息近似于 λKL(p1∥p0)，它作为一个上界。这个界限可以用预测惊异度来解释：它表示使用 p0 预测 X 而不是知道 A 的额外成本。作者还涉及测试罕见情况的贝叶斯情景，并在此背景下解释互信息。

最后，本文考察了 I(X;A) 的泰勒级数展开式中的高阶项，揭示了与 Neyman χ2 散度的联系。本质上，H(pλ) 的形状概括了 p0 和 p1 之间的几个关键散度度量，为它们的关系提供了丰富的视角。

---

## 55. LLM记忆

**原文标题**: LLM Memory

**原文链接**: [https://grantslatton.com/llm-memory](https://grantslatton.com/llm-memory)

本文探讨了为大型语言模型构建记忆系统的复杂性，特别是对于故事生成等任务。作者强调了有限上下文窗口的挑战，以及对一致的世界构建、角色发展和事实存储的需求。

讨论的关键概念包括：

*   **参照系：** 所有知识都存在于特定的上下文中（时间、地点，甚至是虚构的宇宙），这使得简单的键值存储不足以胜任。
*   **向量嵌入：** 虽然向量嵌入在语义相似性方面很有用，但它们在情景记忆方面存在困难，并且缺乏可解释性。
*   **知识图谱：** 一个相互连接的记忆网络，其中节点代表信息，边代表关系。作者倾向于采用基于文档的方法，使用未标记的边和低成本的代理来爬取图谱。语义边对于时间排序等任务可能有用。
*   **元文档：** 创建先前查询的摘要和分析，可以提高效率，类似于回忆上次回忆起某个记忆的时间。
*   **连接创建与遗忘：** 讨论了在文档之间创建连接的策略，以及剪除未使用的连接以避免图谱过载的需求，可能使用大型语言模型来判断和删除不必要的链接。
*   **情景记忆：** 通过感官输入和每日“睡眠”周期模拟人类般的记忆回溯，以综合学习和元文档。
*   **遍历代理：** 一个用于在知识图谱中搜索查询答案的系统。讨论了将所有信息投入上下文或采用优先级队列类型的不同技术。
*   **数据库：** 指出使用SQLite等数据库可能是大型语言模型存储记忆的合适模型。

---

## 56. Nimtable: 用于浏览和管理 Apache Iceberg 表的开源 Web UI

**原文标题**: Nimtable: Open-source web UI to browse and manage Apache Iceberg tables

**原文链接**: [https://github.com/nimtable/nimtable](https://github.com/nimtable/nimtable)

Nimtable：简化的 Iceberg 数据湖管理和探索平台。

Nimtable 是一个开源 Web UI，旨在简化 Apache Iceberg 目录和数据湖的管理与探索。它提供了一个用户友好的平台，用于浏览表、运行查询、分析文件分布以及优化存储布局。

主要功能包括多目录支持（REST、AWS Glue、S3 Tables、PostgreSQL）、无缝对象存储集成（S3、Cloudflare R2、Minio）、交互式查询、AI 辅助以及表优化工具（如文件压缩和快照过期）。Nimtable 还可以作为标准的 Iceberg REST Catalog 使用，将底层目录适配为 RESTful API。

该应用程序可以使用 Docker 轻松部署。配置通过 Web UI 或 YAML 文件管理，支持不同的目录类型和 AWS 凭证选项。

路线图包括优化的压缩策略、增强的监控和分析、数据库缓存、更广泛的查询引擎集成、改进的元数据管理、强大的安全性和访问控制、数据沿袭跟踪以及高级 AI Copilot 支持。欢迎贡献，该项目采用 Apache License 2.0 许可证。

---

## 57. 森喜刚国度2与开放式巴士

**原文标题**: Donkey Kong Country 2 and Open Bus

**原文链接**: [https://jsgroth.dev/blog/posts/dkc2-open-bus/](https://jsgroth.dev/blog/posts/dkc2-open-bus/)

本文调查了ZSNES模拟器中存在已久的、影响《森喜刚2》的漏洞，该漏洞表现为旋转木桶不受控制地旋转。作者jsgroth解释说，此漏洞源于ZSNES缺乏正确的“开放总线”模拟，即读取无效内存地址时会返回数据总线上最后一个值。

作者深入研究了SNES中使用的65816 CPU架构，解释了内存库和寻址。他们确定了负责木桶旋转的特定代码，并对其进行反汇编以理解其逻辑。代码读取木桶方向，增加旋转量，然后使用按位异或和与操作来确定木桶是否已到达基点或序点方向。如果已到达，则木桶将被舍入到该方向，并且旋转停止。

至关重要的是，该代码错误地使用了绝对寻址模式 `and $2000`，从而触发了从库$B3中地址$2000的开放总线读取，在实际硬件上会返回0x2020。但是，由于常量0x2020，这能正常工作。如果没有开放总线模拟，则AND结果始终为零，导致木桶持续旋转。

作者假设 `and $2000` 指令是一个错字，本应是 `and #$2000` (立即寻址)，实际上是使用常量0x2000。 通过更改ROM中的这个单字节，即使没有开放总线模拟，该漏洞也能被修复。 作者得出结论，这是一种出于好奇心驱动的学术练习，因为该问题仅在过时的ZSNES模拟器中普遍存在。

---

## 58. 我不是供应商 (2022)

**原文标题**: I am not a supplier (2022)

**原文链接**: [https://www.softwaremaxims.com/blog/not-a-supplier](https://www.softwaremaxims.com/blog/not-a-supplier)

托马斯·德皮埃尔的文章《我不是供应商》对将“软件供应链”概念应用于自由及开源软件（FOSS）提出了质疑。他认为，FOSS开发者和维护者并非传统意义上的供应商，因为在使用他们的代码时，不存在正式的商业关系或交易。

德皮埃尔解释说，“供应链”一词起源于制造业，在该领域，公司依靠供应商网络来生产商品，从而建立深入的关系以降低风险。然而，软件行业采用了这个术语来描述对FOSS库的依赖，常常没有考虑到其含义。

核心论点是，FOSS许可证明确声明“按原样”提供，这意味着开发者在不提供任何保证或承担任何责任的情况下提供他们的代码。用户可以自行承担风险自由使用这些库。他断言，对FOSS开发者施加“软件供应链”规则，例如严格的测试、安全协议和访问控制措施，是不恰当的，因为他们是志愿者，他们无偿地为社区做出贡献。他认为，许多人已经不堪重负，难以维护他们的项目，而这些项目已经支撑了数字经济的很大一部分。

德皮埃尔建议，如果公司需要特定的开发实践或保证，他们应该通过在不同的许可协议下提供公平的报酬来聘请FOSS开发者作为供应商。在此之前，将FOSS开发者视为要求合规的无偿供应商是不合理的；公司本质上是从公共渠道获得的“免费代码”中受益。文章最后强调，FOSS是“按原样”提供的，强化了缺乏供应商-客户关系这一事实。

---

## 59. 预印制电路：融合3D打印与电子学

**原文标题**: Printegrated Circuits: Merging 3D Printing and Electronics

**原文链接**: [https://spectrum.ieee.org/3d-printing-smart-objects](https://spectrum.ieee.org/3d-printing-smart-objects)

本文介绍了“印刷集成电路”这一新型制造方法，它将电子元件直接集成到3D打印物体中。Oliver Child正在开发简化此过程的技术，使其更容易在3D打印过程中嵌入印刷电路板和导电元件。文章认为，这种方法有望通过将结构元素与电子功能无缝结合，彻底改变智能、功能性3D打印物品的制造。这可能对消费电子产品和其他行业产生重大影响。作者Alfred Poor曾是Health Tech Insider的编辑，也是IEEE Spectrum的撰稿人，这增加了该技术及其潜在影响的可信度。总而言之，本文重点介绍了一项将3D打印和电子技术融合以增强产品功能的有前景的进步。

---

## 60. 农作物释放的形成云的异戊二烯和萜烯可能显著改善气候。

**原文标题**: Cloud-forming isoprene and terpenes from crops may drastically improve climate

**原文链接**: [https://www.smithsonianmag.com/science-nature/scientists-are-just-beginning-to-understand-how-life-makes-clouds-and-their-discoveries-may-drastically-improve-climate-science-180986872/](https://www.smithsonianmag.com/science-nature/scientists-are-just-beginning-to-understand-how-life-makes-clouds-and-their-discoveries-may-drastically-improve-climate-science-180986872/)

生物过程在云形成和气候调节中的重要作用

本文探讨了生物过程，特别是植物和浮游生物排放的气体，在云形成和气候调节中的重要作用。科学家们正在发现，这些“生物源”挥发物对云形成的贡献比之前认为的更大，从而影响气候模型预测未来气候情景的准确性。

CLAW假说提出，海洋藻类释放形成云的气体，这些云随后遮蔽海洋并调节藻类生长。研究人员后来观察到，海洋直接将生物颗粒喷射到大气中，有助于冰晶形成和在较高温度下形成云。

在陆地上，欧洲核子研究中心的（CERN）研究已经确定了来自树木的特定分子，如单萜和异戊二烯，它们有助于气溶胶的形成和云的形成。即使在低浓度下，异戊二烯也会以高速率产生气溶胶颗粒，然后下降并形成云。

将这些生物因素纳入气候模型非常复杂，并导致不同的预测结果。准确的气候模拟需要巨大的计算机能力，从而限制了可以纳入的细节水平。

尽管存在这些挑战，但在模拟云物理和纳入海浪产生的有机物方面正在取得进展。改进的气候模型，得益于更清晰的云科学，对于应对危险的气候情景和评估地球工程解决方案至关重要。

研究表明，由于植物蒸气形成的气溶胶和云所产生的冷却效应，恢复森林可能比以前认为的具有更大的气候缓解潜力。随着空气污染的减少，这些生物源因素对云形成的影响对于理解和应对气候变化变得越来越重要。

---

## 61. 批量出售DB-19连接器

**原文标题**: Bulk Lots of DB-19s for Sale

**原文链接**: [https://www.bigmessowires.com/2025/06/30/bulk-lots-of-db-19s-for-sale/](https://www.bigmessowires.com/2025/06/30/bulk-lots-of-db-19s-for-sale/)

在2025年6月30日的博文中，史蒂夫宣布出售大批DB-19连接器。他解释说，由于DB-19连接器稀缺，他于2016年委托一家工厂为他的BMOW Floppy Emu磁盘模拟器制造这些连接器后，无意中成为了世界上最大的DB-19连接器持有者。DB-19是一种19针连接器，常见于老式Apple、Atari和NeXT计算机，在20世纪90年代停止生产，导致复古计算社区出现短缺。

史蒂夫此前一直不愿出售库存，现在正以1000个为一批提供DB-19连接器，首先从eBay拍卖开始。起拍价相当于每个连接器0.44美元，远低于它们上市时的市场价值。他明确表示，他不会出售单个连接器或小批量连接器，希望有人批量购买并以较小的数量转售。超出拍卖数量的更大数量可以协商。

这些连接器是2024年新生产的，与BMOW产品中使用的连接器相同。它们是带有焊接杯端子和全金属外壳的DB-19公头连接器，适用于电缆制造或PCB上的边缘安装。它们以每盘50个的方式包装，每箱20盘。他提供了一个指向eBay拍卖列表的链接，该列表将于7月8日结束。一位评论者Roy询问史蒂夫拥有的总数量以及最初生产运行的最小订购数量。

---

## 62. 科学海盗女王获发行模因币：Sci-Hub探索新融资方式

**原文标题**: Science's Pirate Queen Gets a Memecoin: Sci-Hub Explores New Funding

**原文链接**: [https://www.forbes.com/sites/digital-assets/2025/06/30/sciences-pirate-queen-gets-a-memecoin-sci-hub-explores-new-funding/](https://www.forbes.com/sites/digital-assets/2025/06/30/sciences-pirate-queen-gets-a-memecoin-sci-hub-explores-new-funding/)

这篇福布斯文章探讨了亚历山德拉·埃尔巴基扬的Sci-Hub，该网站提供免费访问数百万被锁定在付费墙后的学术论文，以及其非常规的加密货币资助实验。面对来自爱思唯尔等出版商的法律诉讼，埃尔巴基扬被誉为“科学海盗女王”，一直依靠捐款来维持Sci-Hub的运营。

2024年，支持者推出了$SCIHUB迷因币，旨在资助Sci-Hub，市值一度达到2000万美元。然而，该项目面临挑战，包括缺乏支持者的信任，以及当埃尔巴基扬将项目迁移到一个由Sci-Hub直接控制的新代币地址时，被指控为“rug pull”（卷款跑路）。

文章认为，加密货币的吸引力在于其能够在传统权力结构之外运作，吸引了投机者和那些为开放科学等事业寻求替代融资模式的人。埃尔巴基扬的反建制立场和共产主义理想与这场运动产生了共鸣。

文章强调了代际差异，指出加密货币对面临经济困境和不信任传统机构的年轻一代具有吸引力。埃尔巴基扬从苦苦挣扎的研究人员到加密货币先驱的旅程，象征着个人通过技术挑战机构权力的潜力。

最终，文章表明，$SCIHUB实验反映了知识、金钱和权力在数字时代运作方式的更广泛变革，尤其是考虑到人工智能训练对开放获取学术文献的需求日益增长。

---

## 63. 所以你想序列化一些DER数据？

**原文标题**: So you want to serialize some DER?

**原文链接**: [https://alexgaynor.net/2025/jun/20/serialize-some-der/](https://alexgaynor.net/2025/jun/20/serialize-some-der/)

本文详细介绍了作者使用 Claude AI 模型优化其 Rust 库 rust-asn1 中 DER 序列化的过程，以提高整数长度计算的效率。 最初，作者试图优化序列化前整数长度的预计算，发现了现有代码和生成的汇编代码中的效率低下问题。

经过一些尝试和错误，Claude 生成的代码看起来不错，并使用形式验证工具 Alive2 验证为正确。 这导致发现了 LLVM（底层虚拟机）中一个遗漏的优化，LLVM 是一个编译器基础设施项目。

最初犹豫不决的作者随后让 Claude 直接在 LLVM 中实现优化。 该模型成功地添加了一个测试用例并实现了必要的更改，甚至在代码审查期间整合了来自 LLVM 维护者的反馈。

作者得出结论，大型语言模型 (LLM) 与验证工具结合使用时，在复杂的编码任务中可能出人意料地有效，尤其是在定义了明确的成功标准时。 他们强调了人工审查在确保 AI 生成代码的质量和正确性方面的重要性。 本文还强调了未被发现的编译器优化的存在，以及在 AI 的帮助下，相对容易地为 LLVM 等项目贡献这些改进。

---

## 64. 对人和机构的更高信任度与更高的幸福感相关。

**原文标题**: Higher levels of trust in people and institutions linked to greater well-being

**原文链接**: [https://phys.org/news/2025-06-higher-people-linked-greater.html](https://phys.org/news/2025-06-higher-people-linked-greater.html)

发表于《心理学通报》并由美国心理学协会总结的文章探讨了信任与幸福感之间的联系。一项对来自全球超过250万名参与者的近1000项研究的荟萃分析发现，更高水平的信任（人际、机构和普遍信任）与更高的主观幸福感之间存在很强的相关性。

主观幸福感被定义为人们对自己生活的感受，包括情感体验（快乐、悲伤、焦虑、抑郁症状）和反思性判断（生活满意度），研究发现，在那些表示对他人和机构有更大信任的个体中，主观幸福感更高。

该研究还表明了一种互惠关系：信任可以提升幸福感，而增强的幸福感随着时间的推移会增加信任。支持性的、健康的关系对幸福感至关重要，而这有赖于信任，这或许可以解释观察到的联系。

包括乌特勒支大学的Catrin Finkenauer和Marlies Maes在内的作者强调了在一个虚假信息可能侵蚀信任的世界中培养信任的重要性。他们提倡媒体素养、公平的规章制度以及人们可以相互依赖的环境，强调家庭、学校和政府在建立信任以支持心理健康和更强大的社区方面的责任。

---

## 65. 利用随机物品制作公平骰子

**原文标题**: Creating fair dice from random objects

**原文链接**: [https://arstechnica.com/science/2025/05/your-next-gaming-dice-could-be-shaped-like-a-dragon-or-armadillo/](https://arstechnica.com/science/2025/05/your-next-gaming-dice-could-be-shaped-like-a-dragon-or-armadillo/)

研究人员开发出一种设计“公平”骰子的方法，几乎可以设计成任何形状，包括小猫、龙和犰狳。这与传统的骰子形状（立方体和多面体）不同，并允许设计具有非均匀概率分布的骰子。这项由Hossein Baktash和Keenan Crane领导的研究，侧重于使用解析几何来预测刚性物体被抛掷时的静止构型，而不是依赖于动态模拟。

该团队将骰子的角、边和面映射到一个球体上，并模拟重力影响来估计每个静止构型的概率。他们通过3D打印七种不同寻常的骰子设计并进行数千次试验投掷来验证他们的计算机模拟，并调整形状以使实验结果与预测的概率一致。

由此产生的骰子包括模拟两个六面骰子滚动、抛硬币以及由动物形状代表的具有三个等概率结果的单个骰子的设计。该算法甚至可以预测像“Pass the Pigs”游戏中猪的静止构型。

虽然该方法存在局限性——忽略了摩擦和弹跳等因素——但它被认为足以创造出有趣且引人入胜的桌面游戏骰子。研究人员还设想了在水下建筑等领域的应用，在这些领域中，物体的精确方向至关重要。这些设计的STL文件已被提供用于3D打印。尽管存在通过计算机实现的更精确的随机数生成器，但该研究强调了骰子滚动的触觉和娱乐性。

---

## 66. 编写代码从来都不是瓶颈

**原文标题**: Writing Code Was Never the Bottleneck

**原文链接**: [https://ordep.dev/posts/writing-code-was-never-the-bottleneck](https://ordep.dev/posts/writing-code-was-never-the-bottleneck)

大型语言模型降低了代码编写的时间和成本，但并未解决软件工程的真正瓶颈：理解、测试和维护代码。

---

## 67. 日本大米价格跌破每5公斤4000日元

**原文标题**: Price of rice in Japan falls below ¥4k per 5kg

**原文链接**: [https://www.japantimes.co.jp/news/2025/06/24/japan/japan-rice-price-falls-below-4000/](https://www.japantimes.co.jp/news/2025/06/24/japan/japan-rice-price-falls-below-4000/)

日本大米价格自3月初以来首次跌破每5公斤4000日元，截至6月15日当周达到3920日元。这次下跌是自2022年3月以来最大的一次，原因是政府根据自由裁量合同释放了储备大米。首相石破茂曾希望在6月中旬前达到这个价格范围。

虽然价格下降是重要一步，但农业大臣小泉提醒不要自满，指出价格仍比一年前高出很多（1772日元）。主要零售商一直以每5公斤约2000日元的价格出售政府储备大米，小型零售商的加入进一步扩大了政府控制大米价格上涨的影响。该文章强调了政府遏制异常高昂大米价格的决心，并承认已取得的进展，同时强调需要继续保持警惕。

---

## 68. Rust CLI with Clap

**原文标题**: Rust CLI with Clap

**原文链接**: [https://tucson-josh.com/posts/rust-clap-cli/](https://tucson-josh.com/posts/rust-clap-cli/)

生成摘要时出错

---

## 69. Meta Joins Kotlin Foundation

**原文标题**: Meta Joins Kotlin Foundation

**原文链接**: [https://engineering.fb.com/2025/06/30/android/meta-joins-kotlin-foundation/](https://engineering.fb.com/2025/06/30/android/meta-joins-kotlin-foundation/)

生成摘要时出错

---

## 70. Show HN: TokenDagger – A tokenizer faster than OpenAI's Tiktoken

**原文标题**: Show HN: TokenDagger – A tokenizer faster than OpenAI's Tiktoken

**原文链接**: [https://github.com/M4THYOU/TokenDagger](https://github.com/M4THYOU/TokenDagger)

生成摘要时出错

---

## 71. Why email startups fail

**原文标题**: Why email startups fail

**原文链接**: [https://forwardemail.net/en/blog/docs/email-startup-graveyard-why-80-percent-email-companies-fail](https://forwardemail.net/en/blog/docs/email-startup-graveyard-why-80-percent-email-companies-fail)

生成摘要时出错

---

## 72. Show HN: Open-Source International Space Station Tracker ESP32/Arduino for $20

**原文标题**: Show HN: Open-Source International Space Station Tracker ESP32/Arduino for $20

**原文链接**: [https://github.com/GuitarML/SpaceStationTracker](https://github.com/GuitarML/SpaceStationTracker)

生成摘要时出错

---

## 73. Transformers Are Graph Neural Networks

**原文标题**: Transformers Are Graph Neural Networks

**原文链接**: [https://arxiv.org/abs/2506.22084](https://arxiv.org/abs/2506.22084)

生成摘要时出错

---

## 74. High-Severity Vulnerability in Notepad++

**原文标题**: High-Severity Vulnerability in Notepad++

**原文链接**: [https://www.csa.gov.sg/alerts-and-advisories/alerts/al-2025-063](https://www.csa.gov.sg/alerts-and-advisories/alerts/al-2025-063)

生成摘要时出错

---

## 75. There are no new ideas in AI, only new datasets

**原文标题**: There are no new ideas in AI, only new datasets

**原文链接**: [https://blog.jxmo.io/p/there-are-no-new-ideas-in-ai-only](https://blog.jxmo.io/p/there-are-no-new-ideas-in-ai-only)

生成摘要时出错

---

## 76. The provenance memory model for C

**原文标题**: The provenance memory model for C

**原文链接**: [https://gustedt.wordpress.com/2025/06/30/the-provenance-memory-model-for-c/](https://gustedt.wordpress.com/2025/06/30/the-provenance-memory-model-for-c/)

生成摘要时出错

---

## 77. Gridfinity: The modular, open-source grid storage system

**原文标题**: Gridfinity: The modular, open-source grid storage system

**原文链接**: [https://gridfinity.xyz/](https://gridfinity.xyz/)

生成摘要时出错

---

## 78. Show HN: Local LLM Notepad – run a GPT-style model from a USB stick

**原文标题**: Show HN: Local LLM Notepad – run a GPT-style model from a USB stick

**原文链接**: [https://github.com/runzhouye/Local_LLM_Notepad](https://github.com/runzhouye/Local_LLM_Notepad)

生成摘要时出错

---

## 79. Researching LED Displays for the Time Circuits

**原文标题**: Researching LED Displays for the Time Circuits

**原文链接**: [https://www.partsnotincluded.com/researching-time-circuit-led-displays/](https://www.partsnotincluded.com/researching-time-circuit-led-displays/)

生成摘要时出错

---

## 80. Show HN: New Ensō – first public beta

**原文标题**: Show HN: New Ensō – first public beta

**原文链接**: [https://untested.sonnet.io/notes/new-enso-first-public-beta/](https://untested.sonnet.io/notes/new-enso-first-public-beta/)

生成摘要时出错

---

## 81. Data Centers, Temperature, and Power

**原文标题**: Data Centers, Temperature, and Power

**原文链接**: [https://www.backblaze.com/blog/data-centers-temperature-and-power/](https://www.backblaze.com/blog/data-centers-temperature-and-power/)

生成摘要时出错

---

## 82. 'The Most Humbling Thing I've Ever Seen': Ford CEO on China's Car Industry

**原文标题**: 'The Most Humbling Thing I've Ever Seen': Ford CEO on China's Car Industry

**原文链接**: [https://insideevs.com/news/764318/ford-ceo-china-evs-humbled/](https://insideevs.com/news/764318/ford-ceo-china-evs-humbled/)

生成摘要时出错

---

## 83. Reverse Engineering Vercel's BotID

**原文标题**: Reverse Engineering Vercel's BotID

**原文链接**: [https://www.nullpt.rs/reversing-botid](https://www.nullpt.rs/reversing-botid)

生成摘要时出错

---

## 84. Virtue garnish: A mental hack to short-circuit bad habits

**原文标题**: Virtue garnish: A mental hack to short-circuit bad habits

**原文链接**: [https://ledgeroflife.blog/virtue-garnishes-the-3-second-mental-hack-that-short-circuits-bad-habits/](https://ledgeroflife.blog/virtue-garnishes-the-3-second-mental-hack-that-short-circuits-bad-habits/)

生成摘要时出错

---

## 85. Ultrasound toothbrush promises painless checks for hidden gum problems

**原文标题**: Ultrasound toothbrush promises painless checks for hidden gum problems

**原文链接**: [https://phys.org/news/2025-06-ultrasound-toothbrush-painless-hidden-gum.html](https://phys.org/news/2025-06-ultrasound-toothbrush-painless-hidden-gum.html)

生成摘要时出错

---

## 86. Jacobi Ellipsoid

**原文标题**: Jacobi Ellipsoid

**原文链接**: [https://en.wikipedia.org/wiki/Jacobi_ellipsoid](https://en.wikipedia.org/wiki/Jacobi_ellipsoid)

生成摘要时出错

---

## 87. 机械舌鼓手敲出所有氛围节奏

**原文标题**: Robotic tongue drummer bangs out all the ambient hits

**原文链接**: [https://blog.arduino.cc/2025/06/07/this-robotic-tongue-drummer-bangs-out-all-the-ambient-hits/](https://blog.arduino.cc/2025/06/07/this-robotic-tongue-drummer-bangs-out-all-the-ambient-hits/)

生成摘要时出错

---

## 88. Ted Chiang on Superintelligence in "The Hampdenshire Wonder"

**原文标题**: Ted Chiang on Superintelligence in "The Hampdenshire Wonder"

**原文链接**: [https://lithub.com/ted-chiang-on-superintelligence-and-its-discontents-in-j-d-beresfords-innovative-work-of-early-20th-century-science-fiction/](https://lithub.com/ted-chiang-on-superintelligence-and-its-discontents-in-j-d-beresfords-innovative-work-of-early-20th-century-science-fiction/)

生成摘要时出错

---

## 89. The Plot of the Phantom, a text adventure that took 40 years to finish

**原文标题**: The Plot of the Phantom, a text adventure that took 40 years to finish

**原文链接**: [https://scottandrew.com/blog/2025/06/you-can-now-play-plot-of-the-phantom-the-text-adventure-game/](https://scottandrew.com/blog/2025/06/you-can-now-play-plot-of-the-phantom-the-text-adventure-game/)

生成摘要时出错

---

## 90. New proof dramatically compresses space needed for computation

**原文标题**: New proof dramatically compresses space needed for computation

**原文链接**: [https://www.scientificamerican.com/article/new-proof-dramatically-compresses-space-needed-for-computation/](https://www.scientificamerican.com/article/new-proof-dramatically-compresses-space-needed-for-computation/)

生成摘要时出错

---

## 91. I made my VM think it has a CPU fan

**原文标题**: I made my VM think it has a CPU fan

**原文链接**: [https://wbenny.github.io/2025/06/29/i-made-my-vm-think-it-has-a-cpu-fan.html](https://wbenny.github.io/2025/06/29/i-made-my-vm-think-it-has-a-cpu-fan.html)

生成摘要时出错

---

## 92. Drug cartel hacked FBI official's phone to track and kill informants

**原文标题**: Drug cartel hacked FBI official's phone to track and kill informants

**原文链接**: [https://arstechnica.com/security/2025/06/mexican-drug-cartel-hacked-fbi-officials-phone-to-track-informant-report-says/](https://arstechnica.com/security/2025/06/mexican-drug-cartel-hacked-fbi-officials-phone-to-track-informant-report-says/)

生成摘要时出错

---

## 93. phkmalloc

**原文标题**: phkmalloc

**原文链接**: [https://phk.freebsd.dk/sagas/phkmalloc/](https://phk.freebsd.dk/sagas/phkmalloc/)

生成摘要时出错

---

## 94. CertMate – SSL Certificate Management System

**原文标题**: CertMate – SSL Certificate Management System

**原文链接**: [https://github.com/fabriziosalmi/certmate](https://github.com/fabriziosalmi/certmate)

生成摘要时出错

---

## 95. Jane Austen's Boldest Novel Is Also Her Least Understood

**原文标题**: Jane Austen's Boldest Novel Is Also Her Least Understood

**原文链接**: [https://www.nytimes.com/2025/06/27/books/review/jane-austen-mansfield-park.html](https://www.nytimes.com/2025/06/27/books/review/jane-austen-mansfield-park.html)

生成摘要时出错

---

## 96. Asynchronous Error Handling Is Hard

**原文标题**: Asynchronous Error Handling Is Hard

**原文链接**: [https://parallelprogrammer.substack.com/p/asynchronous-error-handling-is-hard](https://parallelprogrammer.substack.com/p/asynchronous-error-handling-is-hard)

生成摘要时出错

---

## 97. The Medley Interlisp Project: Reviving a Historical Software System [pdf]

**原文标题**: The Medley Interlisp Project: Reviving a Historical Software System [pdf]

**原文链接**: [https://interlisp.org/documentation/young-ccece2025.pdf](https://interlisp.org/documentation/young-ccece2025.pdf)

生成摘要时出错

---

## 98. Datadog's $65M/year customer mystery solved

**原文标题**: Datadog's $65M/year customer mystery solved

**原文链接**: [https://blog.pragmaticengineer.com/datadog-65m-year-customer-mystery/](https://blog.pragmaticengineer.com/datadog-65m-year-customer-mystery/)

生成摘要时出错

---

## 99. TikTok moderators in Turkey fight trauma, burnout, union-busting

**原文标题**: TikTok moderators in Turkey fight trauma, burnout, union-busting

**原文链接**: [https://restofworld.org/2025/tiktok-moderators-turkey/](https://restofworld.org/2025/tiktok-moderators-turkey/)

生成摘要时出错

---

## 100. Cross-Compiling Common Lisp for Windows

**原文标题**: Cross-Compiling Common Lisp for Windows

**原文链接**: [https://www.fosskers.ca/en/blog/cl-windows](https://www.fosskers.ca/en/blog/cl-windows)

生成摘要时出错

---

