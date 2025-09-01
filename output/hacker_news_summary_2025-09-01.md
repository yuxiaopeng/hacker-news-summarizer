# Hacker News 热门文章摘要 (2025-09-01)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Cloudflare 雷达：人工智能洞察

**原文标题**: Cloudflare Radar: AI Insights

**原文链接**: [https://radar.cloudflare.com/ai-insights](https://radar.cloudflare.com/ai-insights)

无法访问文章链接。

---

## 2. 将Minecraft球体化

**原文标题**: Making Minecraft Spherical

**原文链接**: [https://www.bowerbyte.com/posts/blocky-planet/](https://www.bowerbyte.com/posts/blocky-planet/)

本文详细介绍了在Unity中创建技术演示“方块星球”的过程，该演示将Minecraft风格的立方体体素映射到一个球形星球上。作者探讨了从平面、基于网格的世界过渡到球形世界时出现的独特挑战，重点关注如何使方块与重力对齐，并在固有的变形下保持合理的方块形状。

讨论的关键解决方案包括使用四边形球体来最小化将平面网格映射到球体时的变形，以及预先扭曲正方形网格以进一步减少四边形拉伸和挤压。为了处理深度，作者实现了一个基于壳层的系统，其中每层的方块数量在你从星球核心向外移动时增加四倍，确保边缘对齐，同时减轻尺寸差异。

文章还解释了星球的结构，将其分为六个扇区（基于四边形球体），每个扇区又细分为壳层，再细分为固定大小的区块，以便进行高效处理。 引入了一个“方块地址”系统，用于精确定位此结构中每个方块的位置，该位置基于扇区、壳层、区块和方块索引。作者提供了一些关于如何从相对世界位置获取地址的技术见解。

---

## 3. 以四分之一的成本实现GPT-4 93%的性能：基于弱盗匪反馈的LLM路由

**原文标题**: 93% of GPT-4 performance at 1/4 cost: LLM routing with weak bandit feedback

**原文链接**: [https://arxiv.org/abs/2508.21141](https://arxiv.org/abs/2508.21141)

该arXiv文章(2508.21141)提出了一种新的LLM路由方法，称为预算约束下的自适应LLM路由。作者Panda、Magazine、Devaguptapu、Takemori和Sharma解决了在LLM具有不同能力和成本时，为给定查询选择最合适的LLM的挑战。他们没有依赖于具有完整查询-LLM配对的监督学习，而是将LLM路由构建为一个上下文老虎机问题，允许使用老虎机反馈进行自适应决策。

其核心创新在于创建查询和LLM的共享嵌入空间，对齐嵌入以反映亲和力，最初在人类偏好数据上训练，并使用在线老虎机反馈进行改进。他们引入了PILOT（Preference-prior Informed Linucb fOr adaptive rouTing），它是LinUCB的扩展，用于实例化这个想法。

此外，该论文通过引入一个建模为多选背包问题的在线成本策略来解决管理用户预算的挑战。这确保了根据用户约束进行资源高效的LLM路由。该论文已被EMNLP 2025（findings）接收，并为机器学习领域（cs.LG）做出了贡献。

---

## 4. 有效学习：知识构建规则 (1999)

**原文标题**: Effective learning: Rules of formulating knowledge (1999)

**原文链接**: [https://www.supermemo.com/en/blog/twenty-rules-of-formulating-knowledge](https://www.supermemo.com/en/blog/twenty-rules-of-formulating-knowledge)

这篇题为《有效学习：知识构建规则（1999）》的文章，可能探讨了最大化学习效率的策略，可能是在SuperMemo方法的背景下。虽然现有信息有限，但反复提及的“学习优化：SuperMemo方法视角下的记忆生理学与生物化学”表明，其核心论点围绕着利用对记忆生物学和生物化学功能的理解来优化SuperMemo间隔重复技术。

该文章可能解释了，在结合SuperMemo时，遵循特定规则有效地构建知识，可以极大地提高记忆保留和回忆能力。这可能包括将复杂主题分解为更小、更易于管理的部分的指南，如何措辞问题和答案以实现最佳编码，以及如何优先考虑最相关的信息。

1990年2月11日与“使用SuperMemo学习”一同出现，暗示了该方法的早期迭代，或者是在那时确立的基本原则。该文章很可能建立在这些基本原则之上，从而更细致地理解知识构建，以便在20世纪90年代末最大限度地提高SuperMemo的益处。本质上，该文章侧重于在SuperMemo框架内，基于记忆的科学原理，改进“输入”（知识构建）以优化“输出”（长期记忆）。

---

## 5. Bear现在开源可用

**原文标题**: Bear is now source-available

**原文链接**: [https://herman.bearblog.dev/license/](https://herman.bearblog.dev/license/)

2025年9月1日，Bear的创建者宣布将软件许可从MIT变更为Elastic License。此举源于创建者对他人分叉该项目以创建竞争服务的不满，这损害了原始开发者的生计和对平台的投入。虽然MIT许可的初衷是允许用户学习和审计代码以保障隐私和安全，但它已被以损害项目可持续性的方式利用。

Elastic License与MIT许可类似，但禁止使用该软件提供托管或管理服务。此次变更旨在防止“免费搭车竞争”，这是开源社区日益关注的问题。创建者承认，许多其他开源项目也进行了类似的许可变更，以保护自己免受竞争对手利用其代码而不做出贡献的侵害。

作者认为，鉴于使用人工智能编码工具创建竞争服务的难度越来越低，这一步是必要的。虽然代码很有价值，但创建者强调，Bear真正的优势在于其用户群以及对长期维护和开发的投入。作者优先考虑确保平台的长期发展，即使这意味着限制他人使用代码的方式。

---

## 6. Optery (YC W22) 招聘工程、法律、销售、市场人员 (美国、拉美)

**原文标题**: Optery (YC W22) Is Hiring in Engineering, Legal, Sales, Marketing (U.S., Latam)

**原文链接**: [https://www.optery.com/careers/](https://www.optery.com/careers/)

Optery (YC W22) 正在招聘多个部门的职位：工程、法律、销售和市场营销。该公司欢迎位于美国和拉丁美洲的候选人。这表明 Optery 可能正在扩充团队，并且需要各种角色的人才。“招聘”一词仅突出表明该信息与公司职位空缺有关。核心要点是 Optery 正在积极招聘不同职能和地区的职位。

---

## 7. AI 进入资助游戏，挑选赢家

**原文标题**: AI enters the grant game, picking winners

**原文链接**: [https://www.science.org/content/article/ai-enters-grant-game-picking-winners](https://www.science.org/content/article/ai-enters-grant-game-picking-winners)

无法访问文章链接。

---

## 8. CocoaPods trunk 只读计划

**原文标题**: CocoaPods trunk read-only plan

**原文链接**: [https://blog.cocoapods.org/CocoaPods-Specs-Repo/](https://blog.cocoapods.org/CocoaPods-Specs-Repo/)

CocoaPods博客文章《CocoaPods trunk 只读计划》宣布，主要的 CocoaPods Specs 仓库，即“trunk”，将转换为只读状态。这意味着新的 pod 规范 (podspec) 以及现有规范的更新将不再直接被接受进入 trunk 仓库。

此项变更的主要动机是提高 CocoaPods 生态系统的可靠性和可维护性。随着社区的巨大增长，管理和验证不断更新的 trunk 仓库变得越来越具有挑战性。转向只读模式可以实现更严格的质量控制，并防止格式不正确或恶意 podspecs 引起的潜在问题影响整个社区。

开发者现在将被鼓励创建自己的私有或社区管理的 spec 仓库，而不是直接推送到 trunk。CocoaPods 仍将支持跨多个 spec 仓库进行搜索，从而允许用户继续发现和集成库。正在开发工具和文档，以方便创建和管理这些自定义仓库。

此项变更旨在分散 pod 规范管理流程，分担维护 pod 定义的责任，并最终通过培育更强大和可持续的 pod 规范管理模型来加强 CocoaPods 生态系统。虽然这最初可能需要习惯于直接发布到 trunk 的开发者进行一些调整，但就稳定性和安全性而言，长期效益预计将超过最初的不便。该博客文章鼓励用户探索文档和提供的工具，以适应新的工作流程。

---

## 9. 谷歌AI概述编造了一个关于我的离奇故事。

**原文标题**: Google AI Overview made up an elaborate story about me

**原文链接**: [https://bsky.app/profile/bennjordan.bsky.social/post/3lxojrbessk2z](https://bsky.app/profile/bennjordan.bsky.social/post/3lxojrbessk2z)

Benn Jordan（@bennjordan.bsky.social，Bluesky）抱怨收到消息和标签，要求他澄清对以色列的立场。他对此感到奇怪，因为他认为自己一直公开反对种族灭绝，并支持巴勒斯坦建国。隐含的问题似乎是他被错误地描述或歪曲为持有不同观点，导致困惑并促使他人质疑他。"SO messed up" 的情绪表明这种歪曲对他来说意义重大且令人不安。他暗示这种歪曲的根源是传播不准确或捏造的信息。标题暗示来源可能是 Google AI Overview。

---

## 10. 孤立（任何）

**原文标题**: Isolated(any)

**原文链接**: [https://nshipster.com/isolated-any/](https://nshipster.com/isolated-any/)

本文深入探讨了Swift并发中的`@isolated(any)`属性，解释其目的、用法和含义。文章首先强调了Swift中async函数的灵活性，特别是`await`如何实现隔离切换。`@isolated(any)`解决的核心问题是当将函数作为参数传递时，隔离信息的丢失，尤其是在像`dispatchResponder`这样接受async函数的场景中。

`@isolated(any)`捕获了函数的隔离性，允许访问其`isolation`属性，指示其隔离到的actor（或非隔离）。文章用`callAsFunction`类比来说明这个概念。

至关重要的是，`@isolated(any)`需要一个`await`调用，即使对于同步函数也是如此，这为隔离切换提供了机会。虽然看似矛盾，但这使得特定的调度行为成为可能。

作者强调，虽然`@isolated(any)`在`Task`等基础API中很常见，但它很少影响API的使用者。其主要好处在于通过允许API基于函数参数的隔离做出明智的决策，从而实现“智能调度”。文章使用在MainActor上创建任务的例子来说明`@isolated(any)`如何在特定情况下保持顺序，并借鉴了GCD来更好地展示效果。

文章简要讨论了`isolated(all)`作为未来增强功能以保持一致性的可能性，并提及了`any`参数，为未来复杂的actor类型特性保留了可能性。主要的结论是，虽然`@isolated(any)`可能看起来很复杂，但大多数开发者可以安全地忽略它，除非处理隔离函数的精确调度。

---

## 11. 2025年第二季度搜索引擎引荐报告

**原文标题**: Search engine referral report for 2025 Q2

**原文链接**: [https://radar.cloudflare.com/reports/search-engine-market-share-2025-q2](https://radar.cloudflare.com/reports/search-engine-market-share-2025-q2)

无法访问文章链接。

---

## 12. 独特的、高科技的（家用）电脑

**原文标题**: A Unique, High-Tech (Family) Computer

**原文链接**: [https://nicole.express/2025/a-computer-in-your-home.html](https://nicole.express/2025/a-computer-in-your-home.html)

本文探索了一款2003年产的独特“教育电脑”，它是一款伪装成Windows风格学习设备的FC克隆机。作者从Goodwill.com购得，表明其在美国的稀有性，尽管在其他地方可能更常见。

该套装包含电脑本体、两个手柄、一个鼠标、一把光枪和一个欧式插头电源。电脑配有键盘、FC卡带插槽、DB-9端口、RCA接口（其中一个是RF调制器）以及看似重复利用的塑料部件。

在内部，作者发现了一个标准的键盘薄膜机制和一个带有环氧树脂封装CPU的FC克隆机PCB，可能是一个V.R. Technology芯片。一个奇怪的特性是手柄上A和B按键位置的互换。

该系统没有内置游戏；取而代之的是一张“48合1”卡带，提供教育程序和游戏。用户界面类似于Windows，包含诸如Super Hero、Solitaire以及简化版的Duck Hunt和Track & Field等标题。尽管盒子上宣传有魂斗罗，但实际上并没有。该卡带包含32KB的SRAM，可能由于内存限制用于存储体切换。

最令人惊讶的是，它包含任天堂和Hudson的Family BASIC，完整地包括了音乐板和Game Basic (V3)，利用了额外的RAM。然而，G BASIC版本缺乏保存功能。虽然物理Family BASIC卡带兼容，但键盘矩阵被重新映射。作者总结道，这款教育电脑虽然简陋，但为了解计算历史提供了一个有趣的视角，尤其是在那些较少接触先进技术的地区。

---

## 13. 汽车不是未来：关于机动自由的神话

**原文标题**: The car is not the future: On the myth of motorized freedom

**原文链接**: [https://blog.scaramuzza.me/articles/the_car_is_not_the_future.html](https://blog.scaramuzza.me/articles/the_car_is_not_the_future.html)

本文挑战了一种被广泛持有的观点，即拥有汽车对于成年生活和自由至关重要，认为这是一种由以汽车为中心的城市设计和社会期望所制造出来的必要性。作者追溯了汽车制造商如何通过宣传和政策影响，重塑公共空间，将共享街道变成汽车主导区域，并将事故归咎于行人。这种转变导致了基础设施的改变，如高速公路建设和公共交通资金的减少，从而加强了对汽车的依赖。

本文强调了一些例子，例如移除交通信号灯和瑞典的Dagen H实验，表明减少控制可以提高道路上的谨慎和安全。它批判了汽车文化的隐性成本，包括环境破坏、健康后果和使汽车所有权显得人为可负担的经济补贴。作者借鉴了哲学家安德烈·高兹的观点，认为汽车虽然被宣传为自由的象征，但可以通过债务、孤立和依赖来奴役个人，将生活分割成一个个独立的消费活动。

然而，本文表达了乐观情绪，认为Z世代对汽车的依赖程度低于前几代人，将汽车视为工具而非身份的象征。最近的一些政策变化，例如一些城市将乱穿马路非罪化，表明人们越来越意识到法律和城市规划中以汽车为中心的偏见。作者最后质疑为什么社会在城市设计中继续优先考虑机器而不是人，并敦促重新评估那些使汽车主导地位永久化的政策。

---

## 14. Nim 2 评测：优缺点及示例代码

**原文标题**: A review of Nim 2: The good and bad with example code

**原文链接**: [https://miguel-martin.com/blog/nim2-review](https://miguel-martin.com/blog/nim2-review)

本文回顾了 Nim 2 编程语言，通过示例代码突出了其优点和缺点。作者作为 Nim 语言 1-2 年的用户，认为 Nim 是一种被低估的语言，它结合了简洁性、灵活性和高性能。

其“优点”包括：具有高级脚本语言感觉的系统编程能力，卓越的具有编译时执行能力的元编程能力，以及与 C/C++ 的互操作性。 Nim 的内存管理、编译选项（C、C++、Objective-C、JavaScript）、语言设计（UFCS、泛型、迭代器、异步）以及诸如 fieldPairs 和自定义编译指示之类的元编程特性也受到了赞扬。文章提供了一个使用 `fieldPairs` 和过程重载的简单键/值文件格式的示例。

然而，本文也承认了 Nim 的缺点。主要问题与工具相关：LSP 速度较慢，由于名称改编导致的调试困难，以及无法调试 NimScript。编译器和语言设计方面的不足包括可能令人困惑的迭代器行为和宏编写的挑战。文章还指出缺少原生 WASM 支持以及需要重新设计标准库。

尽管存在这些缺点，作者还是得出结论，Nim 是一种出色的系统编程语言，它使开发人员能够编写简洁、通用的代码。他们指出“clige”库是小型但专注的 Nim 社区中可用的高质量资源的示例。

---

## 15. iPhone闹钟应用上的时间选择器不是环形的，而是一个长列表。

**原文标题**: The time picker on the iPhone's alarm app isn't circular, it's just a long list

**原文链接**: [https://old.reddit.com/r/interestingasfuck/comments/1n5lztw/the_time_picker_on_the_iphones_alarm_app_isnt/](https://old.reddit.com/r/interestingasfuck/comments/1n5lztw/the_time_picker_on_the_iphones_alarm_app_isnt/)

Reddit帖子揭示iPhone闹钟时间选择器的设计假象：“iPhone闹钟应用的时间选择器不是环形的，而是一个长长的列表”一文揭示了iOS闹钟应用时间选择界面中一个违反直觉的设计选择。与用户认为小时和分钟选择轮是环形且可以连续循环的认知相反，该帖子揭示了它们实际上只是非常长的列表。

该帖子和相关评论解释说，看似环形的滚动行为实际上是通过在用户到达滚轮的表观“边缘”时，将选择快速跳回列表的开头（或结尾）来实现的。 这解释了为什么在滚动到特定限制时，可能会出现细微的“跳跃”或动量变化，而不是平滑的连续旋转。

评论深入探讨了这种设计决策的潜在原因。一种解释认为，实现长列表比实现真正的圆形选择器更简单，特别是考虑到底层iOS框架的限制。另一种解释认为，这可能是一种有意的选择，以防止意外地无限滚动并在设置遥远的未来时间时迷失方向。

本质上，该帖子揭示了一种设计错觉，它欺骗用户相信时间选择器是一个连续旋转的滚轮，而实际上，它的运行原理是一个更简单但不太直观的长列表。这一发现揭示了UI/UX设计的复杂性，以及感知的功能与底层实现之间的差异。

---

## 16. 俄罗斯方块即使只有O(1)行或列也是NP难的 (2020) [pdf]

**原文标题**: Tetris is NP-hard even with O(1) rows or columns (2020) [pdf]

**原文链接**: [https://martindemaine.org/papers/ThinTetris_JIP/paper.pdf](https://martindemaine.org/papers/ThinTetris_JIP/paper.pdf)

此文档似乎是2020年发表的名为“俄罗斯方块即使在O(1)行或列的情况下也是NP-hard”的研究论文的PDF文件。然而，该PDF文件的内容是表示压缩文档结构以及嵌入的字体、图像和文本的二进制数据。由于PDF格式和编码的原因，无法直接提取文本以了解文章内容并提供摘要。我无法根据提供的数据确定该论文的主要观点、论证或发现。

---

## 17. 在并发Go应用中保持顺序：三种方法的比较

**原文标题**: Preserving Order in Concurrent Go Apps: Three Approaches Compared

**原文链接**: [https://destel.dev/blog/preserving-order-in-concurrent-go](https://destel.dev/blog/preserving-order-in-concurrent-go)

本文探讨了在并发 Go 应用程序中保持顺序的三种方法，旨在解决利用并发的速度优势时保持数据序列的挑战。作者介绍了顺序至关重要的场景，例如实时日志增强和时间序列数据处理。

核心问题是并发 goroutine 以不同的速度处理任务，从而扰乱了自然顺序。作者强调了“背压优先”的设计理念，限制缓冲以防止不受控制的内存增长。

文中展示了三种 `OrderedMap` 函数，并针对不保留顺序的基准 `Map` 函数进行了基准测试：

1. **回复通道 (ReplyTo Channels):** 这种 Go 原生方法为每个输入项使用唯一的回复通道，由 worker goroutine 处理并按顺序解包。它会产生一些每个项目的分配开销，但在高并发情况下可能优于无序的 `Map`。
2. **使用 sync.Cond 进行轮流 (sync.Cond for Turn-Taking):** 此方法使用共享索引和 `sync.Cond` 来确保每个 worker 按正确的顺序写入结果。虽然消除了每个项目的分配，但由于“惊群效应”，随着 goroutine 数量的增加，性能会下降。
3. **许可传递链 (Permission Passing Chain):** 这种新颖的方法将作业链接在一起，将写入权限从一个作业传递到下一个作业。这消除了“惊群效应”并创建了高效的点对点信令，证明它是三种方法中对于更高并发级别最有效的方法。

文章详细介绍了每种方法的代码示例和基准测试结果，突出了内存效率和性能之间的权衡。

---

## 18. Show HN: 简易现代化的 .NET NuGet 服务器发布 RC 版

**原文标题**: Show HN: Simple modenized .NET NuGet server reached RC

**原文链接**: [https://github.com/kekyo/nuget-server](https://github.com/kekyo/nuget-server)

这个"Show HN"帖子介绍了`nuget-server`，一个基于Node.js构建的现代化、简洁的NuGet服务器实现。它提供了必要的NuGet v3 API端点和一个现代化的Web UI，用于包管理、用户账户控制和发布。

主要特性包括易于设置、NuGet V3 API兼容性、基于文件系统的存储（无需数据库）、通过HTTP POST进行灵活的包发布、基本身份验证、反向代理支持、多包上传、用户管理、API密码重置以及从现有NuGet服务器导入包。还提供了一个Docker镜像。

该服务器可以通过npm全局安装。它支持通过命令行选项、环境变量和JSON文件进行配置。可以仅为发布启用身份验证，也可以为所有操作启用身份验证，并通过`--auth-init`选项进行初始用户创建。UI和API使用单独的密码。密码强度已强制执行。

可以通过CLI从其他NuGet服务器导入包。服务器支持反向代理，需要正确的基本URL配置。有适用于多种架构的Docker镜像。该帖子提供了配置、使用、包发布、身份验证和Docker部署的示例。

---

## 19. 音乐人的 Git – 使用版本控制进行音乐制作 (2023)

**原文标题**: Git for Music – Using Version Control for Music Production (2023)

**原文链接**: [https://grechin.org/2023/05/06/git-and-reaper.html](https://grechin.org/2023/05/06/git-and-reaper.html)

使用Git进行音乐制作
        
        本文探讨了如何将Git（一种通常用于软件开发的版本控制系统）应用于音乐制作。作者作为一名音乐家和软件工程师，指出了管理音乐项目多个版本的问题，这通常会导致文件结构混乱（例如，“song-mix-final-v5.rpp”）。Git提供了一种解决方案，允许制作人跟踪项目文件（在Reaper中为.rpp文件）的更改，而无需创建大量副本。

        作者详细介绍了其基于Git的工作流程：在项目文件夹中初始化存储库，创建`.gitignore`文件以排除媒体文件（WAV、采样），并使用描述性消息提交更改（例如，“bass eq adjusted”）。这使他们能够恢复到以前的版本，创建分支进行实验，并有效地管理其项目历史记录。

        虽然Git对于大型二进制文件（WAV）来说并不理想，但作者认为这不是问题，因为他们很少删除媒体文件。由于项目文件的不透明性以及协作人员需要具有相同的DAW设置和插件，因此使用Git进行协作被认为不太可行。

        文章最后建议通过将文本文件存储在Git存储库中作为个人问题跟踪器，来跟踪音乐项目的TODO项。这允许随时记录想法，并可以通过GitHub从任何设备访问。总的来说，作者认为Git是管理音乐项目版本的一个有用工具，尽管存在局限性。

---

## 20. Zfsbackrest：ZFS文件系统的Pgbackrest风格加密备份

**原文标题**: Zfsbackrest: Pgbackrest style encrypted backups for ZFS filesystems

**原文链接**: [https://github.com/gargakshit/zfsbackrest](https://github.com/gargakshit/zfsbackrest)

Zfsbackrest 是一个实验性工具，用于创建 pgbackrest 风格的 ZFS 文件系统加密备份，利用 ZFS 快照。务必认识到它的实验性质，避免将其作为唯一的备份方法。它强制使用 `age` 进行加密。

该工具需要通过 `go install` 安装，并通过 `/etc/zfsbackrest.toml` 进行配置，指定包含的数据集（使用 glob 模式）、S3 端点详细信息（仅限 HTTPS）、备份过期策略（full、diff、incr）和上传并发设置。

`zfsbackrest init` 使用 age 公钥创建存储库。`zfsbackrest backup` 创建完整 (full)、差异 (diff) 或增量 (incr) 备份，每个备份都有依赖关系：diff 依赖于 full，incr 依赖于 diff。完整备份是独立的且体积较大，而差异和增量备份是增量的且体积较小。

`zfsbackrest detail` 显示备份和孤立项。`zfsbackrest cleanup` 删除孤立或过期的备份，并提供 dry-run 选项进行测试。

恢复使用 `zfsbackrest restore`，需要 age 身份文件（私钥）。用户指定源数据集、可选的备份 ID 和目标数据集（目标数据集不能已存在）。

Zfsbackrest 广泛使用 ZFS 快照，但不修改现有数据集，确保安全。它使用 `zfs snapshot`、`zfs hold`、`zfs send`、`zfs release`、`zfs destroy` 和 `zfs recv`。

---

## 21. 我们应该有能力在自己拥有的硬件上运行任何我们想运行的代码。

**原文标题**: We should have the ability to run any code we want on hardware we own

**原文链接**: [https://hugotunius.se/2025/08/31/what-every-argument-about-sideloading-gets-wrong.html](https://hugotunius.se/2025/08/31/what-every-argument-about-sideloading-gets-wrong.html)

本文探讨了关于侧载限制的争论，认为核心问题并非仅仅是在自有硬件上运行任何代码，而是控制操作系统本身的能力。作者认为，谷歌和苹果等公司不一定是限制硬件的使用，而是在控制运行在该硬件上的软件环境（操作系统）。

作者认为，重点应该从批评操作系统限制转向要求在任何硬件上安装替代操作系统的能力。他们建议，法律应要求制造商提供必要的技术支持和文档，以便用户和开发者构建和安装自定义操作系统。

作者用实例来说明这一点：谷歌限制安卓应用程序的安装，苹果将iOS与iPhone硬件紧密结合，索尼限制PS5的使用。关键在于，虽然公司有权控制其预装软件环境中的体验，但用户也应该有完全自由地用自己选择的系统替换该环境的权利。作者主张通过安装替代操作系统来重新利用硬件的权利，从而有效地将iPhone或PlayStation等设备转变为不同的工具，摆脱原始制造商的限制。

---

## 22. 编写兼容系统的探险之旅

**原文标题**: An adventure in writing compatible systems

**原文链接**: [https://turso.tech/blog/an-adventure-in-writing-compatible-systems](https://turso.tech/blog/an-adventure-in-writing-compatible-systems)

无法访问文章链接。

---

## 23. 印度价值十亿美元的电子垃圾帝国

**原文标题**: India's billion-dollar e-waste empire

**原文链接**: [https://restofworld.org/2025/india-e-waste-recycling-electronics/](https://restofworld.org/2025/india-e-waste-recycling-electronics/)

亚什拉杰·沙玛的文章《印度价值十亿美元的电子垃圾帝国》探讨了印度蓬勃发展但问题重重的电子垃圾回收产业。受国内电子产业增长和来自其他国家的进口推动，印度是电子垃圾处理的主要参与者，估计价值达15亿美元。

然而，该行业在很大程度上是非正规的，95%的工人在不受监管且往往危险的条件下工作。像拉希德·汗和穆罕默德·伊克拉尔这样的工人，面临着微薄的工资和接触有毒物质的风险，他们在像卡塔这样的地区拆卸电子产品，卡塔是德里一个巨大的电子垃圾倾倒场，由像阿西夫·马利克这样的权势人物控制。妇女则被分配到收入最低、风险最高的岗位，正如努尔那样，她辛勤地提取铜线。

文章将这种非正规部门与像Recyclekaro这样的正规回收公司进行了对比，在这些公司里，工人有防护设备，运营也受到监管。印度政府正在推动通过新规使该行业正规化，要求制造商使用经过认证的回收商。这让像Recyclekaro这样的公司受益，但也由于成本增加而面临着来自科技制造商的抵制。

文章强调了迫切需要在经济机会与环境和工人保护之间取得平衡的必要性，因为印度的电子垃圾挑战代表了全球不可持续的电子产品消费问题。

---

## 24. 象棋的复杂性是什么？

**原文标题**: What Is Complexity in Chess?

**原文链接**: [https://lichess.org/@/Toadofsky/blog/what-is-complexity/pKo1swFh](https://lichess.org/@/Toadofsky/blog/what-is-complexity/pKo1swFh)

Toadofsky评论了一篇研究论文（FM David Peng的《国际象棋复杂性度量》），该论文试图定义和量化国际象棋的复杂性，并认为它可以通过生成非战术谜题、创建具有人类个性的国际象棋引擎以及识别玩家的关键改进概念来彻底改变国际象棋网站。

评论的重点是Peng的观点，即复杂性是基于百分格损失（Stockfish评估）的一维指标，并且可以实时用于确定位置难度。Toadofsky质疑了从这些观点中得出的一些结论的逻辑有效性，发现大多数都需要进一步研究，除了复杂性信息可以丰富顶级国际象棋比赛的观看体验。

主要批评包括神经网络国际象棋引擎（如Stockfish-NNUE）的快速发展使得原始研究的某些方面已经过时，需要对Stockfish评估进行适当的标准化，以及质疑棋盘表示模型。

尽管存在批评，Toadofsky承认对这项研究印象深刻，特别是发现某些位置普遍困难，而另一些位置对较低等级的玩家更具挑战性。他建议进行改进，例如纳入分段的Stockfish评估、WDL统计、对将军和剩余时间进行建模，以及纳入人机对战。最终，Toadofsky希望在作弊者利用复杂性指标之前，就能实现它。

---

## 25. 蒂尔伯里变电站英国最大电池储能设施

**原文标题**: UK's largest battery storage facility at Tilbury substation

**原文链接**: [https://www.nationalgrid.com/national-grid-connects-uks-largest-battery-storage-facility-tilbury-substation](https://www.nationalgrid.com/national-grid-connects-uks-largest-battery-storage-facility-tilbury-substation)

英国国家电网已将英国最大的电池储能系统（BESS），即300兆瓦的瑟罗克储能项目，连接到其位于埃塞克斯郡蒂尔伯里变电站的输电网络。该600兆瓦时的电池由Statera Energy开发，可为多达68万户家庭供电，并通过存储多余的可再生能源并在需要时释放，帮助平衡电力供需。

此次连接标志着蒂尔伯里地区从煤炭到清洁能源的转型，该地区此前为蒂尔伯里A和B燃煤电厂提供服务。国家电网加强了变电站的保护和控制系统，以适应电池的负荷。

英国国家电网的John Twomey强调了电池储能在英国清洁能源转型中的重要作用。Statera Energy首席执行官Tom Vernon强调了BESS容量对于在可再生能源发电量低或波动时支持电网的重要性。

国家电网还在努力连接450兆瓦的瑟罗克灵活发电设施，这是Statera的另一个项目，也在蒂尔伯里变电站。在此连接之前，肯特郡的373兆瓦克莱夫山太阳能发电园最近已投入使用，进一步展示了国家电网对支持可再生能源并网的承诺。

---

## 26. 脑部手术让我领悟到意识的脆弱与珍贵

**原文标题**: What brain surgery taught me about the fragile gift of consciousness

**原文链接**: [https://bigthink.com/business/brain-surgery-fragile-gift-of-consciousness/](https://bigthink.com/business/brain-surgery-fragile-gift-of-consciousness/)

在《脑部手术教给我的关于意识脆弱礼物》中，埃里克·马科维茨反思了他面对潜在致命脑部病变的经历，以及它对他的意识和生命理解产生的深刻影响。

在手术前夕，面对死亡的可能性，马科维茨体验到了一种强烈的意识和与当下时刻的连接。这种高度的意识状态，不同于神经学或哲学的定义，让他深刻地意识到存在的奇迹和荒谬。

在成功的手术和康复后，马科维茨经历了“幸存者的欣快感”，一种重新觉醒，使他将生命视为一个脆弱的、相互关联的系统。他将注意力从成就转移到对齐、时机以及维持生命的关怀体系的重要性上。他意识到，真正的生存是一种积极的选择，一种注意、爱和选择生命的实践，即使在痛苦中也是如此。

马科维茨强调，意识不仅仅是神经元的功能，也是关怀、爱和愿意被我们所见所改变的意愿的功能。他珍视存在感胜过生产力，努力注意、倾听和感受。他总结说，善良需要意识和关怀，而这最终是意识的礼物。他的经历让他更加欣赏生命的脆弱性、连接的重要性以及有意识的觉知的力量。

---

## 27. 永恒的斗争

**原文标题**: Eternal Struggle

**原文链接**: [https://yoavg.github.io/eternal/](https://yoavg.github.io/eternal/)

文章标题为《永恒的挣扎》，极其简短，仅包含标题和一条“更换背景”的备注。因此，无法提供内容摘要。标题暗示了冲突或持续不断的斗争的主题，但没有任何支持文本，这纯粹是猜测。唯一具体的信息是更换背景的指示，这表明该文章要么不完整，要么充当占位符。

---

## 28. 任天堂Switch 2底座USB-C兼容性

**原文标题**: Nintendo Switch 2 Dock USB-C Compatibility

**原文链接**: [https://www.lttlabs.com/blog/2025/08/30/nintendo-switch-2-dock](https://www.lttlabs.com/blog/2025/08/30/nintendo-switch-2-dock)

USB-C PD与任天堂Switch 2兼容性研究：VDM及测试分析

本文探讨USB-C Power Delivery (PD) 及其与任天堂Switch 2及其底座的兼容性。文章解释了USB-C PD基础知识、协商过程和厂商自定义消息 (VDM)，并重点介绍了任天堂可能对VDM的非标准使用。

本文展示了Switch 2、其底座、第三方适配器和显示器的各项测试数据。 主要发现包括：

*   无论电源如何，Nintendo Switch 2的最大充电功率为15W。
*   Switch 2底座连接后总是请求20V/3A的电压电流，即使不需要。
*   像Antank S3 Max这样的第三方底座更节能，仅在需要时才请求额外电量。
*   将Switch 2充电至90%大约需要两小时，充电至100%大约需要三小时。
*   为了优化电池使用，建议充电至75%（约1.5小时）以避免涓流充电。
*   底座的兼容性问题可能源于不良的USB-C实施，而不是任天堂的有意限制。
*   涉及USB-C显示器的测试表明，设备甚至没有开始交换厂商自定义消息。

作者提供测试数据的可下载文件，供进一步分析。

---

## 29. 反建制对威权民粹主义及对强人的支持

**原文标题**: Anti-establishment versus authoritarian populists and support for the strongman

**原文链接**: [https://www.frontiersin.org/articles/10.3389/fpos.2025.1605460](https://www.frontiersin.org/articles/10.3389/fpos.2025.1605460)

本文研究了不同类型的民粹主义态度如何影响对强人领导者的支持。作者认为，民粹主义态度并非铁板一块，应区分为两个不同的类别：反建制民粹主义（侧重于反精英主义和以人民为中心）和威权民粹主义（反映多数主义、对强人统治的支持、精英主义和排他性民族主义）。

该研究分析了来自九个国家（法国、意大利、西班牙、匈牙利、波兰、加拿大、美国、巴西和阿根廷）的调查数据，以确定这些态度对民粹主义领导人选举支持的影响。 通过因子分析，研究人员证实了每个国家都存在反建制和威权民粹主义态度。

研究结果表明，意大利、西班牙、巴西、阿根廷、匈牙利和波兰对民粹主义领导人的支持主要受威权民粹主义态度的驱动。 相比之下，反建制民粹主义是法国和加拿大的主要因素，而这两个维度均未显着影响美国对民粹主义的支持。

作者的结论是，民粹主义强人的吸引力源于对威权统治的诱惑，而不是民主理想。 他们认为，民粹主义选民支持右翼民粹主义领导人，是因为他们欣赏这些领导人愿意绕过制度约束并压制民主言论，这凸显了民主稳定的令人不安的趋势。 该研究通过强调在民粹主义态度中考虑强人领导力的吸引力，挑战了民粹主义的观念方法。

---

## 30. Bash 提示符合集

**原文标题**: Bash Prompts Collection

**原文链接**: [https://www.gilesorr.com/bashprompt/prompts/](https://www.gilesorr.com/bashprompt/prompts/)

本网页汇集了来自 Bash Prompt HOWTO 以及其他贡献者的 Bash 提示符，包括来自现已解散的 BashPrompt Themes Project 的提示符。作者旨在提供各种提示符示例，以激发用户灵感，并为用户自定义 Bash 提示符提供思路。

这些提示符大致按照复杂度递增的顺序排列，每个提示符都链接到其相应的代码。该集合从基本的提示符开始，例如“Stock RedHat 5.1 Prompt”和“Stock Suse Prompt”，它们显示用户、主机名和当前目录。

该集合包括显示各种信息的提示符。“Dan's Prompt”显示历史记录编号、tty 编号和上一个进程的返回值。其他提示符跟踪挂起的作业、显示系统负载并指示剩余的笔记本电脑电池电量。还有一些提示符具有视觉元素，如彩色文本、ASCII 艺术，甚至时钟显示。

更复杂的提示符，如“Termwide Prompt”、“Sergio's Prompt”和“My Root Prompt”，旨在提供广泛的信息、终端标题栏，甚至尝试利用未使用的屏幕空间。“Flexible Prompt”被认为是作者最全面和可定制的设计，尽管被认为可能存在错误。

作者警告不要使用一些更复杂的提示符，因为存在性能问题（例如，“Power Prompt 2”）或可用性问题（例如，“Mountain Prompt”）。该集合提供了广泛的选择，从简单且信息丰富到视觉上吸引人且功能丰富。

---

## 31. 编译晚餐

**原文标题**: Compiling Dinner

**原文链接**: [https://gist.github.com/breadchris/5877d1ab8381526bb81b551ffd5d1768](https://gist.github.com/breadchris/5877d1ab8381526bb81b551ffd5d1768)

编译晚餐：用烹饪类比解释编译器概念及大语言模型如何普及编译器创建。文章指出，菜谱本质上是程序：食材是输入，烹饪动作是指令，成品是输出。这一过程与编译器将代码翻译成可执行动作的过程类似。

传统上，创建编译器需要专业知识。然而，大语言模型使个人能够通过简单地用自然语言描述规则，轻松地为各种领域勾勒出编译器。这使得非专业人士可以尝试为食品、健身或金融等领域创建编译器。

作者强调，识别结构化意图中的模式，例如锻炼计划或业务流程，使用户能够理解控制我们世界的规则、语法和流程。

文章最后强调，虽然大语言模型简化了编译器创建的初始阶段，但它们并没有取代对人类判断的需求。人类仍然必须决定编译器应优化的价值观和优先级，例如速度、营养或公平。大语言模型使任何人都能想象和创建编译器，将日常系统变成可编程的环境。

---

## 32. 战争中的贸易

**原文标题**: Trade in War

**原文链接**: [https://news.mit.edu/2025/why-countries-trade-each-other-while-fighting-mariya-grinberg-book-0828](https://news.mit.edu/2025/why-countries-trade-each-other-while-fighting-mariya-grinberg-book-0828)

玛丽亚·格林伯格的《战争中的贸易》一书探讨了交战国之间经济贸易这种令人惊讶的现象。文章强调，各国常常与其敌人进行贸易，权衡军事利益与经济成本。格林伯格的研究，源于她的博士论文，揭示了这种战时贸易受到商品类型、战争持续时间和对国家长期经济安全潜在影响等因素的影响。

英国在两次世界大战期间与德国的贸易，以及印度和巴基斯坦在冲突期间的贸易等例子，说明了这种做法的普遍性。格林伯格认为，当贸易没有显著帮助敌人的战争努力，并且结束贸易会损害国家的长期经济稳定时，贸易是被允许的。这种衡量标准包括评估商品转化为军事用途的速度，以及优先考虑长期的经济健康，即使在冲突期间也是如此。

文章强调，各国常常误判战争的长度，从而影响其贸易决策。格林伯格的研究表明，贸易关系不一定能阻止冲突，并呼吁进一步研究交战国之间的经济关系。她正在进行的研究探讨了为什么各国常常在没有准备的情况下进入战争，认为战争将是短暂的，这种观点与历史证据相悖。

---

## 33. 刘易斯与克拉克用泻药标记他们的路线。

**原文标题**: Lewis and Clark marked their trail with laxatives

**原文链接**: [https://offbeatoregon.com/2501d1006d_biliousPills-686.077.html](https://offbeatoregon.com/2501d1006d_biliousPills-686.077.html)

本文幽默地描述了路易斯和克拉克探险队（Corps of Discovery）如何在不知不觉中，利用本杰明·拉什医生提供的泻药“雷鸣者”（thunder-clappers）为未来的考古学家留下线索。这种药丸的主要成分是甘汞（氯化亚汞），即使在探险结束后很久，仍可在厕所坑中检测到。

文章解释说，由于探险队员以肉类为主、缺乏纤维的饮食导致慢性便秘，因此这种药丸至关重要。文章还揭示甘汞被用来治疗一些队员感染的梅毒。

文章详细介绍了拉什医生的“英雄医学”方法，该方法基于古老的“体液”理论，认为疾病源于体液失衡。拉什坚信放血和强效泻药等激进疗法可以恢复平衡。虽然杰斐逊认为他是一位杰出的医生，但拉什的方法备受争议，一些人认为，如果没有一个可能过度使用激进疗法的受过正规训练的医生，探险队的情况会更好。

药丸中的汞主要在消化过程中排出，且非常稳定，这使得考古学家能够通过识别具有高汞含量的厕所坑来定位营地，从而帮助绘制探险队的旅程。

---

## 34. C++：强先行发生？

**原文标题**: C++: Strongly Happens Before?

**原文链接**: [https://nekrozqliphort.github.io/posts/happens-b4/](https://nekrozqliphort.github.io/posts/happens-b4/)

本文深入探讨了 C++20 中的 "强先行发生"(strongly happens before) 概念，它是 "先行发生"(happens before) 关系的细化，对于理解内存序至关重要，尤其是在 `std::atomic` 的使用中。作者使用代码示例演示了一种情景，在这种情景下，执行在基本的 "先行发生" 规则下看似有效，但违反了顺序一致性和 `memory_order::seq_cst` 操作所需的单一总顺序的约束。

问题的核心在于，某些架构（如 Power）允许的执行在 C++20 之前的标准中被认为是无效的。作者通过剖析 Power 架构的内存模型及其一致性规则来解释这种差异，展示了一个线程的写入可能无法及时传播到另一个线程，从而无法满足预期的顺序。

"强先行发生" 关系通过添加更严格的约束来解决这个问题，尤其是在涉及顺序一致的原子操作时。关键的区别在于，如果 A 与 D 同步，并且两者都是顺序一致的，则 A *强*先行发生于 D。这种更严格的定义可以防止执行图中的循环，否则可能导致顺序一致操作的无效总顺序。文章认为，如果没有这个修复，某些有效的 Power 执行将被视为无效，并且 C++ 委员会选择修改标准（通过添加 "强先行发生"），而不是对获取/释放同步施加性能惩罚。文章最后指出，"强先行发生" 确保 C++ 内存模型与 Power 等真实世界架构更紧密地对齐。

---

## 35. 移除谷歌身份验证器TOTP代码

**原文标题**: De-Googling TOTP Authenticator Codes

**原文链接**: [https://imrannazar.com/articles/degoogle-otp](https://imrannazar.com/articles/degoogle-otp)

本文详细介绍了一个将基于时间的单次密码 (TOTP) 代码从 Google Authenticator 迁移到名为 `oathtool` 的命令行界面 (CLI) 工具的过程，从而有效地“摆脱 Google”的 TOTP 身份验证。作者旨在直接从其 MacOS 或 Linux 终端生成 OTP，避免依赖 Google Authenticator 应用程序。

该过程包括：(1) 使用应用程序的 QR 码迁移功能从 Google Authenticator 导出 TOTP 代码；(2) 解码 QR 码的内容，这是一个包含 Base64 编码数据的 URL。事实证明，此数据是 Protobuf 编码的，需要来自 `otpauth_migrate` 的特定 Python 脚本来提取密钥和服务名称；(3) 最后，将这些密钥与 `oathtool` 结合使用，以在命令行上生成 OTP。

作者使用诸如 `qrtool` 之类的工具进行 QR 码解码，并提供了一个示例包装脚本 (`otp`) 来访问存储在本地文件 (`~/.otpkeys`) 中的密钥。该脚本使用服务名称来获取相应的密钥以生成代码。

本文承认将密钥存储在磁盘上的安全风险，并建议使用带有 gpg 的对称加密来增强安全性，并引用了另一个资源以获取实施细节。最后，作者寻求在不使用 Google 服务的情况下，获取地图上交通数据的替代解决方案。

---

## 36. 使用一台大型服务器 (2022)

**原文标题**: Use One Big Server (2022)

**原文链接**: [https://specbranch.com/posts/one-big-server/](https://specbranch.com/posts/one-big-server/)

本文提倡对许多应用使用“单体服务器”而非微服务等复杂分布式系统。文章指出，现代服务器性能极其强大且常常未被充分利用，能以远低于云原生架构的成本处理大量工作负载。

作者详细描述了典型现代服务器的配置，强调其充足的CPU核心、内存和I/O能力。然后，作者展示了基准测试，证明单台服务器能够以惊人的速度处理诸如视频服务、运行数据库和编译代码等任务。

成本比较表明，租用云虚拟机带有显著的“云溢价”，可能比租用或购买专用服务器贵5-30倍。作者认为，这种溢价很大程度上是因为为云供应商的峰值负载容量付费，而这可能并非对所有工作负载都有益。

文章建议，对于大多数QPS低于1万的Web服务，单台服务器就已足够。在承认可用性的重要性之后，作者建议使用位于不同数据中心的primary和backup服务器，而非复杂的云架构。他们还告诫不要盲目采用云供应商推动的“云原生”架构，因为这些架构通常对供应商的利益大于用户。

作者还解决了使用单体服务器的常见反对意见，例如对系统管理员和安全更新的需求，并辩称即使在云环境中，这些任务仍然存在。

---

## 37. Procmon Sysinternals 工具的 Linux 版本

**原文标题**: A Linux version of the Procmon Sysinternals tool

**原文链接**: [https://github.com/microsoft/ProcMon-for-Linux](https://github.com/microsoft/ProcMon-for-Linux)

本文介绍Procmon for Linux，一个受Windows Sysinternals Procmon启发的工具，旨在追踪Linux系统上的系统调用活动。目前处于预览阶段，需要Ubuntu 18.04 LTS、cmake和libsqlite3-dev。

本文提供了安装和构建Procmon的说明，并指导用户查阅专门文档以了解详细过程。接着，详细介绍了其用法，解释了可用的命令行选项：`-h/--help`、`-p/--pids`（用于指定进程ID）、`-e/--events`（用于指定系统调用）、`-c/--collect`（用于无头模式并输出到文件）、`-f/--file`（用于打开跟踪文件）和`-l/--log`（用于调试日志记录）。一些示例演示了如何使用这些选项来监视特定进程和系统调用，或打开现有的跟踪文件。

最后，本文鼓励用户通过Stack Overflow（标签为`ProcmonForLinux`）、GitHub功能请求和错误报告提供反馈。它欢迎贡献，并指向一份“如何贡献”文档，其中详细说明了开发工作流程、编码指南和拉取请求提交流程。该工具根据MIT许可证获得许可，并由Microsoft Corporation拥有版权。

---

## 38. 编年史 – 用于 Go 的惯用、类型安全的事件溯源框架

**原文标题**: Chronicle – Idiomatic, type safe event sourcing framework for Go

**原文链接**: [https://github.com/DeluxeOwl/chronicle](https://github.com/DeluxeOwl/chronicle)

本文是一篇关于使用 Chronicle（一个 Go 语言的事件溯源框架）的综合指南。它介绍了事件溯源作为一种模式，即应用程序状态的所有更改都存储为不可变的事件，形成单一的真理来源。可以通过重放这些事件来重建当前状态。

本文将事件溯源与传统数据库存储进行对比，强调其在审计和历史分析方面的优势。它解释了投影作为专门的读取模型的角色，这些读取模型通过监听事件流并提供最终一致性来构建，并针对查询进行了优化。

本文然后提供了一个快速入门指南，其中包含一个详细的银行帐户示例。它涵盖了如何定义聚合、事件和命令。它演示了如何重放事件以重建聚合状态，在命令中执行业务规则，以及使用事件日志和存储库来持久化事件。

代码示例展示了如何设置内存事件日志，创建事件溯源存储库，开设帐户，存取款以及保存聚合。它展示了该框架的类型安全性，确保事件被正确地反序列化和应用。

最后，它涉及诸如乐观并发、快照、共享事件元数据、事件排序、存储后端、事件转换器、不同类型的投影及其实现以及事务性事件日志等主题。

---

## 39. 乒乓时钟

**原文标题**: Pong Clock

**原文链接**: [https://bigjobby.com/pong/?v=2.0/](https://bigjobby.com/pong/?v=2.0/)

该页面介绍了一款“乒乓时钟”，它被展示为一个复古画布时钟。 主要功能包括：

*   移动设备友好。
*   具有4:3的宽高比。
*   超清晰。

该页面还包含一个捐赠请求，以支持创作者，其中包含预设金额以及各种货币的自定义金额选项。 捐赠过程通过PayPal安全处理。

最后，它包括标准的网站元素，例如链接到隐私政策的Cookie同意通知，以及时钟需要JavaScript才能运行的免责声明。

---

## 40. 宇宙裂缝

**原文标题**: A Crack in the Cosmos

**原文链接**: [https://drb.ie/articles/a-crack-in-the-cosmos/](https://drb.ie/articles/a-crack-in-the-cosmos/)

本文探讨了前苏格拉底时期希腊哲学家阿那克萨戈拉的开创性科学贡献，以及它们如何彻底改变了古希腊对宇宙的理解。文章重点介绍了公元前466年埃戈斯波塔米陨石的影响，它被解读为阿那克萨戈拉理论的证据，即天体与地球由相同的物质构成。

文章对比了古希腊的世界观与我们现代的理解，强调虽然我们看到遥远的太阳和运行的球体，但希腊人则在天空中感知到神灵和神话生物。阿那克萨戈拉追随米利都的泰勒斯，通过寻求对天体现象的自然解释来挑战这种超自然观点。

讨论的关键人物是巴门尼德斯，他发现月亮反射阳光（日光反射），从而促成了对月球作为球体的理解，并为地球是球体的概念铺平了道路。阿那克萨戈拉通过解释日食和月食是地球和月球投下的阴影，进一步发展了这些思想，摆脱了超自然的解释。

文章强调，虽然阿那克萨戈拉的观点在今天看来可能很基本，但在当时却是革命性的。他预测埃戈斯波塔米陨石的能力进一步巩固了他作为天才的声誉，并从根本上改变了对宇宙的理解，表明天体是固体、物质物体，而不是神圣实体。他成功预测了日食，并被雅典人称为“努斯”（心灵）。最终，这些发现标志着迈向科学探究和对宇宙的理性理解的重要一步。

---

## 41. 夸尔敏

**原文标题**: The Qweremin

**原文链接**: [https://www.linusakesson.net/qweremin/index.php](https://www.linusakesson.net/qweremin/index.php)

林纳斯·奥克松的“Qweremin”详细介绍了他的新乐器发明，这是一种基于QWERTY键盘的热敏电子琴。 由于对传统热敏电子琴的难度以及他之前的键盘乐器（Sixtyforgan，Qwertuoso等）的基本音符开/关性质感到沮丧，他将这两个概念结合了起来。

Qweremin允许对音量和音高进行富有表现力的控制，同时能够快速演奏旋律和和弦。 该文章重点介绍了SID芯片限制内的音量控制挑战。 奥克松最初的解决方案涉及带有包络发生器的反馈回路，但事实证明这对于精确的乐句来说太慢了。

为了解决这个问题，他加入了一个外部DAC来实现更快速的音量控制。 C64仍然在解码来自555定时器的脉冲并将音量级别传递给DAC方面发挥作用。

一个重要的事件是遇到了热敏电子琴演奏家Bass Cadet，他指出音量响应缓慢是一个主要的缺点。 后来，在X派对上，游戏音乐作曲家Rob Hubbard在C64热敏电子琴的夹子上签名，为该项目增添了一丝名人色彩。 Qweremin代表了奥克松迄今为止最具表现力的8位乐器。

---

## 42. C++模块怎么用？

**原文标题**: What to do with C++ modules?

**原文链接**: [https://nibblestew.blogspot.com/2025/08/we-need-to-seriously-think-about-what.html](https://nibblestew.blogspot.com/2025/08/we-need-to-seriously-think-about-what.html)

无法访问文章链接。

---

## 43. 大英帝国残余日薄西山之时

**原文标题**: When the sun will literally set on what's left of the British Empire

**原文链接**: [https://oikofuge.com/sun-sets-on-british-empire/](https://oikofuge.com/sun-sets-on-british-empire/)

本文探讨了英国印度洋领地（BIOT），特别是查戈斯群岛，可能丧失给毛里求斯的影响，以及这对英国“日不落帝国”主张的意义。目前，BIOT和皮特凯恩群岛确保至少有一块英国领土始终处于白昼。

英国政府曾计划将查戈斯群岛的主权移交给毛里求斯，尽管目前这一计划存在争议。情况因迪戈加西亚岛（BIOT的一部分）上存在大型美国军事基地而进一步复杂化，这使得美国在此事中拥有利益。本文强调了查戈斯人的困境，他们为了给基地让路而被驱逐，并且没有被纳入谈判。

如果BIOT被割让，位于塞浦路斯的英属基地区（SBAs）将成为最东端的英国领土。英属基地区是1960年塞浦路斯独立时的遗留物，其复杂的边界反映了需要包含英国军事设施，同时避开塞浦路斯居民点的需求。

美国此前曾说服英国保留英属基地区，因为它们在信号情报和空中行动方面具有战略价值。虽然可以考虑对迪戈加西亚岛采取类似的安排，但毛里求斯似乎不太可能同意。

如果没有BIOT，将会出现短暂的时期，尤其是在六月，皮特凯恩群岛和英属基地区都将处于黑暗之中。这意味着太阳的确会同时在所有英国领土上落下，象征着帝国永恒白昼的终结。文章最后指出皮特凯恩群岛的日落和英属基地区的日出时间非常接近，强调了“日不落”主张的岌岌可危。

---

## 44. 贝叶斯，比特与大脑

**原文标题**: Bayes, Bits and Brains

**原文链接**: [https://bayesbitsbrains.github.io/](https://bayesbitsbrains.github.io/)

贝叶斯、比特与大脑：本迷你课程探索概率论、信息论和机器学习之间的联系。本站利用引人入胜的谜题来激发读者的兴趣并阐释关键概念。这些谜题，例如预测维基百科片段中的下一个字母、分析股市回报、估算维基百科的信息量，以及理解XKCD笑话，为理论基础的探索提供了实践背景。

本课程旨在通过回答以下问题，为机器学习提供坚实的理论基础：什么是KL散度、熵和交叉熵？最大似然法和最大熵法从何而来？为什么logits、softmax和高斯分布如此普遍？我们如何设置损失函数？以及压缩是如何与大型语言模型相关的？

作者鼓励读者积极参与所提供的谜题，并承诺随着课程的进行，能更深入地理解这些概念。最后的邀请是让读者继续保持他们现有的理解，或者深入本课程以探索该学科的深度。

---

## 45. 学者称以色列在加沙的行动符合种族灭绝的定义。

**原文标题**: Israeli campaign in Gaza meets definition of genocide, say scholars

**原文链接**: [https://www.ft.com/content/470b61ff-aa1c-487f-a9ae-477b5c142a53](https://www.ft.com/content/470b61ff-aa1c-487f-a9ae-477b5c142a53)

学者称以色列在加沙的军事行动构成种族灭绝，《金融时报》(FT)文章如是说。

该文章需付费阅读，需要订阅才能访问完整内容。提供的选项包括不同的订阅层级，提供不同级别的FT数字内容访问权限，包括全球新闻、专家意见、新闻通讯和播客。订阅选项还提供FT投资专栏、报纸数字版和印刷版等功能。该文章强调了FT对高质量新闻的承诺及其在广大读者中的受欢迎程度。文章还提到了通过大学或组织机构获得数字访问权限的可能性。

---

## 46. Show HN: Spotilyrics - 在 VS Code 中查看同步 Spotify 歌词

**原文标题**: Show HN: Spotilyrics – See synchronized Spotify lyrics inside VS Code

**原文链接**: [https://github.com/therepanic/spotilyrics](https://github.com/therepanic/spotilyrics)

Spotilyrics是一款VS Code扩展，可在编辑器中直接显示您当前播放的Spotify歌曲的同步歌词。它允许开发者在编码时在侧面板中查看歌词，从而增强他们的聆听体验。主要功能包括与Spotify实时同步歌词、基于专辑封面自动进行歌词颜色主题化、简洁的侧面板设计以及简单的一次性身份验证过程。

要使用Spotilyrics，用户需要在Spotify开发者仪表板上创建一个Spotify应用，获取一个Client ID，并将Redirect URI设置为`http://127.0.0.1:8000/callback`。安装扩展并运行“Show Spotify Lyrics via Spotilyrics”命令后，用户将Client ID粘贴到面板中以登录。该扩展使用Spotify Web API、LRClib（用于同步歌词）和colorthief（用于主题提取），并使用TypeScript和VS Code WebView构建。提供了两个主要命令：一个用于显示歌词面板，另一个用于注销并清除会话。该项目未获得许可，鼓励用户自由使用、修改和分发，不提供任何保证。

---

## 47. 研究发现，科学研究在Bluesky上的互动比X更多。

**原文标题**: Science research gets more engagement on Bluesky than X, study finds

**原文链接**: [https://www.theguardian.com/technology/2025/sep/01/science-research-gets-more-engagement-on-bluesky-than-x-study-finds](https://www.theguardian.com/technology/2025/sep/01/science-research-gets-more-engagement-on-bluesky-than-x-study-finds)

最新研究表明，与X（原推特）相比，在Bluesky上，科学研究获得更高的参与度和更具原创性的审视。该研究分析了260万条引用超过50万篇学术文章的Bluesky帖子，发现在Bluesky上，互动水平（包括点赞、转发、回复和引用）显著更高。研究还发现，科学帖子的文本原创性也更高。

在埃隆·马斯克收购X以及唐纳德·特朗普重返白宫后，Bluesky的用户数量经历了最初的激增后出现波动，而这一发现恰好出现。然而，科学界似乎正在积极使用和参与该平台，近一半的科学帖子至少获得10个赞，三分之一被转发10次或更多。

由于X上参与度下降以及机器人和网络喷子的增加，科学家们被Bluesky所吸引。Bluesky被认为更有利于有意义的对话和跟进新研究，研究人员和期刊的集中度更高。此举是主要科学传播者为重建此前在推特上蓬勃发展的科学界而做出的共同努力。虽然用户基础小于X，但Bluesky在科学家之间培养了高水平的参与和讨论，使其成为一个可靠的科学传播平台。

---

## 48. 此电报在传达给任何人之前，必须严密改述。

**原文标题**: “This telegram must be closely paraphrased before being communicated to anyone”

**原文链接**: [https://history.stackexchange.com/questions/79371/this-telegram-must-be-closely-paraphrased-before-being-communicated-to-anyone](https://history.stackexchange.com/questions/79371/this-telegram-must-be-closely-paraphrased-before-being-communicated-to-anyone)

本文探讨了二战时期发往美国的一些电报上发现的一个奇怪指令：“此电报在传达给任何人之前必须进行严密意译。” 作者质疑为什么需要意译而不是直接引用，并探讨了“严密”在这种语境下的潜在含义。

一种解释认为，该指令是美国军方的一种通信原则，旨在避免使用不同的加密方法发送同一信息两次。重复信息，即使使用不同的加密方式，也可能帮助敌人破解密码。“意译”是当时改变信息以避免这种风险的专业术语。

一份1950年解密的美国陆军密码学手册将“意译”定义为重写信息，尽可能改变其措辞而不改变其含义。这包括改变句子的结构，通过同义词改变用词，以及尽可能删除单词。目的是防止敌人将明文与密文进行比较，从而破解密码。该解答强调，这种策略对于盟军破译德国恩尼格玛密码至关重要，他们利用了德国人未能遵守程序漏洞的缺陷。意译有助于避免“已知明文攻击”，即对手知道同一信息的加密版本和未加密版本。

---

## 49. 蛤蟆：Will McGugan (Rich/Textual) 的 Agentinc 编码通用 TUI

**原文标题**: Toad: Universal TUI for Agentinc Coding from Will McGugan (Rich/Textual)

**原文链接**: [https://elite-ai-assisted-coding.dev/p/toad-will-mcgugan](https://elite-ai-assisted-coding.dev/p/toad-will-mcgugan)

Rich和Textual的创建者Will McGugan推出了Toad，一个旨在改善AI编码助手用户体验的通用终端UI。他批评现有的AI终端工具存在闪烁、交互有限和基础提示编辑器等用户体验缺陷。Toad通过使用终端的备用缓冲区实现无闪烁渲染，允许交互式浏览整个对话历史记录，从而解决了这些问题。

主要功能包括具有语法高亮和文件导航的高级提示编辑，使用户能够在提示、shell命令和文件浏览之间无缝切换。受notebook启发，Toad旨在创建一个“实时文档”，保留AI交互的价值，而不仅仅是最终代码。

Toad构建于Textual框架之上，开发速度很快，其用户体验超越了主要科技公司现有的工具。McGugan设想Toad是一个通用前端，允许任何AI后端通过定义的协议插入，从而促进专业AI工具的发展。

Toad将开源，鼓励社区参与，并有可能被大型公司采用。McGugan认为Toad是目前为每个AI编码工具重新发明终端界面的趋势的更好替代方案，类似于Web开发，开发者不会为每个应用程序构建新的浏览器。Toad旨在成为基于终端的AI交互的标准、更高效和用户友好的界面。

---

## 50. 我们管理过疾控中心：肯尼迪正在危害每一个美国人的健康

**原文标题**: We Ran the CDC: Kennedy Is Endangering Every American's Health

**原文链接**: [https://www.nytimes.com/2025/09/01/opinion/cdc-leaders-kennedy.html](https://www.nytimes.com/2025/09/01/opinion/cdc-leaders-kennedy.html)

无法访问文章链接。

---

## 51. 塑胶之前的塑胶：古塔胶如何塑造19世纪

**原文标题**: Plastic Before Plastic: How gutta-percha shaped the 19th century

**原文链接**: [https://worldhistory.substack.com/p/plastic-before-plastic](https://worldhistory.substack.com/p/plastic-before-plastic)

好的，这是一篇基于文章标题和该主题相关典型内容的摘要，由于我无法访问提供的链接：

古塔胶，一种源自东南亚原生树木的天然乳胶，在19世纪发挥了重要作用，有效地成为了现代塑料的前身。文章可能详细介绍了其独特的性能——耐久性、柔韧性以及加热时可塑性——使其用途广泛且极具价值。

该摘要可能强调了古塔胶在海底电报电缆发展中的关键作用。其防水和绝缘的特性能够保护用于跨洋传输信息的脆弱铜线，从而彻底改变了全球通信。文章可能讨论了这种应用如何刺激了对古塔胶的巨大需求，导致其在许多地区的过度开采和最终枯竭。

除了电缆绝缘之外，文章可能还会解释古塔胶如何被用于制造各种其他商品，包括家具、工具手柄、牙科填充物、高尔夫球（“古塔球”）甚至早期形式的假肢。它被视为一种神奇材料，可以替代象牙和角等昂贵且稀缺的材料。

最后，文章可能还会涉及古塔胶繁荣对环境的影响。需求的增加导致了不可持续的采伐行为，破坏了东南亚的森林，并引发了人们对资源长期可用性的担忧。这个早期资源枯竭的例子是一个警示故事，突出了在没有适当管理的情况下开发自然资源可能产生的负面后果。本质上，古塔胶的故事为合成材料的兴起以及与工业化相关的环境挑战提供了一个有价值的历史视角。

---

## 52. 用钢丝钳升级大型机 (2010)

**原文标题**: Mainframe upgrade done with wire cutters (2010)

**原文链接**: [https://alt.folklore.computers.narkive.com/nZagiUHj/mainframe-upgrade-done-with-wire-cutters](https://alt.folklore.computers.narkive.com/nZagiUHj/mainframe-upgrade-done-with-wire-cutters)

Al Grant 在 2010 年发帖询问他听过的一个关于大型机升级的传说。该传说称，一些大型机在出厂时配备了未激活的硬件组件（处理器、内存等），客户工程师 (CE) 只需在支付升级费用后剪断一根电线即可激活这些组件。Grant 正在寻找关于这种做法的可引用参考资料，最好是已知的第一个实例。他特别记得那根电线是紫色的。该帖子本质上是请求提供关于大型机硬件升级中一种历史做法的信息和确认。

---

## 53. 英特尔专利“软件定义超级核心”

**原文标题**: Intel Patents 'Software Defined Supercore'

**原文链接**: [https://www.tomshardware.com/pc-components/cpus/intel-patents-software-defined-supercore-mimicking-ultra-wide-execution-using-multiple-cores](https://www.tomshardware.com/pc-components/cpus/intel-patents-software-defined-supercore-mimicking-ultra-wide-execution-using-multiple-cores)

本文探讨了英特尔名为“软件定义超级核”(SDC)的专利技术，该技术旨在通过将多个物理核心融合成一个虚拟的“超级核”来提高单线程CPU性能。该技术将单个线程的指令分成块，并在多个核心上并行执行它们，使用同步和数据传输指令来维护程序顺序。这被认为是构建更宽、功耗更高的单片核心的替代方案。

在支持SDC的系统中，每个核心都有一个硬件模块来管理同步、寄存器传输和内存排序。软件通过JIT/静态编译器或二进制检测将程序分割成段，以便在多个核心上分配，并注入特殊的指令来控制和数据流。操作系统支持对于动态地将线程切换进/出“超级核”模式至关重要。

文章提到，现有的x86 CPU通常可以达到2-4 IPC（每时钟周期指令数），而苹果基于Arm的核心则实现了更高的IPC。虽然构建更宽的x86核心是可能的，但它面临着瓶颈和收益递减。这项技术尚未得到证实，性能提升也只是暗示。

评论区提供了额外的背景信息，指出以前已经探索过类似的概念，并强调了关于各种CPU架构的解码宽度和IPC性能的最新信息。评论员对这种软件定义方法的可行性和潜在的性能优势表示怀疑。

---

## 54. 福特与T型车的诞生

**原文标题**: Ford and the Birth of the Model T

**原文链接**: [https://www.construction-physics.com/p/ford-and-the-birth-of-the-model-t](https://www.construction-physics.com/p/ford-and-the-birth-of-the-model-t)

本文详细介绍了福特T型车如何革新汽车制造，奠定大规模生产和低价的基础。福特从N型车开始，使用钒钢和可互换零件实现高产量和低价格。T型车在此基础上发展，更加强调机械加工精度和创新技术，如冲压钢部件。

关键创新包括将发动机缸体铸造成一个整体，并使用压制钢，这是比铸造更便宜的替代方案。福特不断追求工艺改进，重新设计T型车以降低成本和提高效率。1913年引入流水线是一个重大转折点，最初是在飞轮磁电机部门，这大大缩短了组装时间和库存。随后，流水线被扩展到汽车的其他部分，包括发动机和底盘。

海兰帕克工厂的设计旨在优化物料流动，使用专用机床并不断改进流程以减少生产步骤。汽车的设计也为了简单和降低成本而不断调整。因此，T型车的价格在短短六年内从850美元暴跌至360美元，而销量却一路飙升。

本文认为，福特的成功是反馈循环的结果：高精度机械加工带来了更好、更便宜的汽车，从而刺激了需求，进而促使进一步的工艺改进和成本降低。高产量证明了在专用机械、专用装配厂和优化的工厂设计方面的大量固定成本是合理的，最终使T型车成为“效率引擎”。

---

## 55. 在ARM SBC上安装UEFI固件

**原文标题**: Installing UEFI Firmware on ARM SBCs

**原文链接**: [https://interfacinglinux.com/2025/08/25/edk2-uefi-for-the-rock-5-itx/](https://interfacinglinux.com/2025/08/25/edk2-uefi-for-the-rock-5-itx/)

本文详细介绍了作者在 Radxa ROCK 5 ITX+ 单板计算机 (SBC) 上安装 EDK2 (UEFI) 固件，从而能够从 USB 启动通用 ARM Linux 镜像的经验。 主要动机是为了避免在机架式设置中，访问 microSD 卡槽进行操作系统安装的不便。

作者克服了多个挑战，包括 ROCK 5 ITX+ 最初无法从 microSD 或 eMMC 启动 EDK2。 解决方案包括使用 Armbian 将 UEFI 镜像刷入 SPI Flash。 经过一番小小的慌乱后，他们成功显示了 UEFI 启动画面。 然后，作者探索了 UEFI 设置，重点关注 ACPI/设备树配置。

作者测试了 Fedora Rawhide 和 Ubuntu 25.10，这两个都是前沿发行版，以满足硬件加速图形所需的 6.15+ 内核要求。 Fedora 需要进行配置调整才能正确显示，并且最初有一个无法工作的 GNOME 桌面，需要等待一段时间才能完成设置。 另一方面，Ubuntu 25.10 则开箱即用，运行流畅，包括声音。 Vulkan 支持在这两个发行版上都可用。 简要测试 NetBSD 也显示成功启动和网络连接。

作者得出结论，虽然 EDK2 + RK3588 尚未完全成熟，但前景广阔，尤其适用于无头服务器设置。 内核 6.15 要求是硬件加速的一个障碍。 该实验成功实现了从 USB 启动通用 ARM Linux 镜像的目标，绕过了 microSD 卡的限制。

---

## 56. 人人可练的柔术

**原文标题**: Jujutsu for everyone

**原文链接**: [https://jj-for-everyone.github.io/](https://jj-for-everyone.github.io/)

本文档是Jujutsu版本控制系统教程，面向零基础新手，无需任何Git或VCS经验。它认为Jujutsu更易于学习、更强大，并且与Git完全兼容，是新用户的更佳选择。

本教程分层结构，从基本用法到高级技能（如历史重写和协作）逐步进阶。它强调动手实践，建议各层级之间休息，巩固学习。它还包含一个脚本，可将进度重置到特定章节。

本教程涵盖以下层级：
*   **层级1：** 单人工作的最基本入门。
*   **层级2：** 协作工作的最低要求。
*   **层级3：** 基本问题解决。
*   **层级4：** 历史重写。
*   **层级5：** 生产力提升和高级工作流。
*   **层级6：** 针对特定情况的补充主题。

它鼓励用户报告问题并提出改进建议。它还探讨了首先学习Jujutsu的潜在缺点，例如以Git为中心的术语以及Jujutsu的相对新颖性。它强调了Jujutsu相对于Git的优势，包括更简单的界面和面向高级用户的功能。作者计划使本教程与最新的Jujutsu版本保持同步。

---

## 57. 具有 Fiber 原生支持的全新 Ruby Curl 绑定

**原文标题**: New Ruby Curl bindings with Fiber native support

**原文链接**: [https://github.com/taf2/curb/blob/master/ChangeLog.md](https://github.com/taf2/curb/blob/master/ChangeLog.md)

关于具有原生 Fiber 支持的新 Ruby Curl 绑定 `curb` 的公告。该项目似乎托管在 GitHub 上，用户名是 "taf2"。项目对公众开放，鼓励用户通过 Fork 仓库进行贡献。项目拥有 228 个 Fork 和 1.3k 个 Star，表明其受欢迎程度以及 Ruby 开发社区内的高度兴趣和参与度。该公告可能强调使用 `curb` 和 Fiber 的好处，可能是为了提高网络相关任务中的并发性或性能。原生 Fiber 支持表明 `curb` 利用 Ruby 的 Fiber 功能有效地处理多个并发请求，使其与旧的、非 Fiber 感知的解决方案相比，可能更具响应性和可扩展性。主要信息是 `curb` 提供了一个现代化的 Ruby Curl 绑定，其主要特点是原生 Fiber 支持，可能解决了异步网络编程中的当代挑战。

---

## 58. ADHD管理笔记

**原文标题**: Notes on Managing ADHD

**原文链接**: [https://borretti.me/article/notes-on-managing-adhd](https://borretti.me/article/notes-on-managing-adhd)

本文介绍了管理多动症的策略和战术，强调药物治疗是至关重要的第一步。作者认为，药物治疗能够解锁实施生产力系统和技巧的能力，从而帮助管理多动症症状。

“策略”部分侧重于高层次的建议。它强调了药物治疗的重要性，并将个人成长视为内部改变（药物治疗、心理治疗）和外部改变（待办事项清单、日历）之间的平衡。通过待办事项清单（Todoist）来辅助记忆，将其作为一种外部认知辅助工具，用于记住任务、对其进行排序和分解。能量水平在一天中会波动，影响任务难度；在能量最高的早上优先处理高要求任务。拖延症被分为与多动症相关、与焦虑相关和决策瘫痪，每种情况都需要不同的处理方法。最后，作者建议通过日记进行内省，检测适应不良的模式，并跟踪进展，使用具有每日、每周、每月和年度条目的分层日记系统。

“战术”部分仅被提及但未详细描述，将提供微观层面的改进或自我管理的“策略”。本文强调，管理多动症涉及药物治疗、生产力系统和通过内省实现的自我意识的结合。

---

## 59. Builder.ai 几个月内估值从15亿美元跌至零。

**原文标题**: Builder.ai went from a value of $1.5B to zero in a few months

**原文链接**: [https://www.nytimes.com/2025/08/31/technology/builder-ai-collapse.html](https://www.nytimes.com/2025/08/31/technology/builder-ai-collapse.html)

无法访问文章链接。

---

## 60. 万亿生物科技公司在哪里？

**原文标题**: Where are all the trillion dollar biotechs?

**原文链接**: [https://www.ladanuzhna.xyz/writing/trillion-dollar-biotechs](https://www.ladanuzhna.xyz/writing/trillion-dollar-biotechs)

为何生物科技行业尚未诞生万亿美元公司？尽管人类基因组学、药物重定向和人工智能等技术进步常被宣传为降低成本和降低研发风险的途径。

本文探讨了制药研发回报率下降的原因：自 1950 年以来，每花费十亿美元获批的新药数量每九年减少一半。虽然少数药物的年销售额超过 200 亿美元（修美乐、可瑞达、辉瑞新冠疫苗），但扭转这一趋势需要更多类似的重磅炸弹药物。

本文质疑了常见策略的有效性。虽然基因靶点最初看起来很有希望，但孟德尔变异主要针对患者群体较小的罕见疾病。在常见疾病中普遍存在的 GWAS 变异对批准率影响甚微。即使专注于罕见疾病，虽然产生了成功的药物（SMA、囊性纤维化、血友病 A），但通常也无法转化为公司的成功，例如 Bluebird Bio。 神经系统疾病适应症的基因学研究未显示对成功率有任何影响。

药物重定向虽然看似绕过了早期阶段的失败，但缺乏持续成功的确凿证据。无论是无假设还是有针对性的方法，都显示出有限的结果，新冠药物重定向的成功率仅为 1.6%。人工智能驱动的药物重定向虽然前景广阔，但面临着与传统药物发现类似的挑战。

最终，作者认为，虽然这些策略提供了一些增量改进，但它们并未从根本上改变生物科技行业面临的经济挑战。

---

## 61. 新加坡国父：空调是成功的秘诀 (2015)

**原文标题**: Singapore founding father: air conditioning was the secret to success (2015)

**原文链接**: [https://www.vox.com/2015/3/23/8278085/singapore-lee-kuan-yew-air-conditioning](https://www.vox.com/2015/3/23/8278085/singapore-lee-kuan-yew-air-conditioning)

这篇2015年的文章纪念了新加坡国父李光耀的逝世，并探讨了一个他认为对国家成功至关重要的、令人惊讶的因素：空调。李光耀以其务实，但有时也带有威权主义的领导风格而闻名，他将新加坡从一个资源匮乏的岛屿转变为全球经济强国，但他同时也强调了看似微小细节的重要性。

在2009年的一次采访中，李光耀表示空调对新加坡的发展至关重要。他认为，空调使得在热带气候下高效工作成为可能，使公务员能够全天舒适地工作，从而提高了公共效率。他甚至声称，空调是历史上最重要的发明之一，因为它使得在热带地区的发展成为可能。

这篇文章强调，李光耀对空调的重视体现了他更广泛的哲学：确保“繁荣的基本条件”是通往成功的关键。这种方法也体现在他通过支付公务员高薪来打击腐败的努力中，这使得他们不太可能受到贿赂的诱惑。这些细节使新加坡成为世界上最清廉的国家之一。

---

## 62. 认知负荷才是关键

**原文标题**: Cognitive load is what matters

**原文链接**: [https://github.com/zakirullin/cognitive-load](https://github.com/zakirullin/cognitive-load)

降低认知负荷对高效软件开发至关重要。认知负荷，定义为完成任务所需的脑力，是人类的基本限制，尤其是在阅读和理解代码时。作者强调减少*外在*认知负荷，它源于信息的呈现方式，而不是*内在*负荷，后者是任务本身固有的。

本文提供了外在认知负荷如何体现以及如何缓解它的实际例子：

*   **复杂条件语句：** 使用具有意义名称的中间变量来分解复杂的逻辑表达式。
*   **嵌套 If 语句：** 倾向于提前返回以专注于“快乐路径”，并消除工作记忆中的先决条件。
*   **继承噩梦：** 提倡组合优于深度继承层次结构。
*   **过多的小模块：** 警告不要过度细化、浅层的模块，它们需要大量的上下文切换和交互映射。 具有简单接口的深层模块是首选。
*   **误解单一职责原则：** 强调模块应该对一个用户或利益相关者负责，而不是必须只做一件事。
*   **过多的浅层微服务：** 建议转向更大、更深的微服务（“宏服务”），以避免分布式单体并减少认知开销。
*   **功能丰富的语言：** 告诫不要过度使用语言特性，因为它们会通过呈现过多的选择来增加认知负担。
*   **HTTP 状态代码中的业务逻辑：** 建议在响应正文中使用自描述字符串，而不是依赖数字 HTTP 状态代码来传达业务特定信息。

总的来说，文章强调在代码中优先考虑清晰性、简洁性和信息隐藏，以最大限度地减少开发人员理解和维护代码所需的脑力。 文章倡导一种务实的方法，强调对抽象原则的遵守应根据其对认知负荷的影响进行评估。

---

## 63. Ultrassembler速度为何如此之快？

**原文标题**: How is Ultrassembler so fast?

**原文链接**: [https://jghuff.com/articles/ultrassembler-so-fast/](https://jghuff.com/articles/ultrassembler-so-fast/)

本文详细介绍了高性能 RISC-V 汇编器库 Ultrassembler 的开发，旨在比现有的解决方案（如 GNU as 和 llvm-mc）更快、集成度更高。作者强调了对进程内汇编器的需求，以避免在 C++ 代码中使用 `system()` 调用外部汇编器二进制文件所带来的开销，尤其是在资源受限的嵌入式系统中。

Ultrassembler 通过精心的优化实现了其速度，在基准测试中超越 GNU as 达 10 倍，超越 llvm-mc 达 20 倍。本文重点介绍了关键的优化技术：

1. **异常处理：** 利用 C++ 异常进行错误报告，因为它们在汇编的正常、无错误执行流程中具有零性能开销。
2. **高效的数据结构：** 设计紧凑的数据结构来表示 RISC-V 寄存器和指令，最大限度地减少内存占用并提高缓存利用率。文章描述了 `rvregister` 和 `rvinstruction` 结构体，重点关注字节级存储，避免使用昂贵的字符串。 特殊指令属性使用位域进行编码。
3. **预分配内存池：** 实施自定义内存分配器，以规避与堆分配相关的性能瓶颈，堆分配涉及系统调用并可能导致缓存未命中。 本文提供了代码片段，演示了全局内存池的创建和使用，该内存池避免了汇编期间的动态内存管理。

作者最后展示了这些优化如何使该库能够实现高性能的 RISC-V 脚本编写和 JIT 编译，为游戏和其他应用程序开辟了可能性。

---

## 64. PHP中从发射器角度的双向信号

**原文标题**: Bidirectional Signals from the Emitter's Perspective in PHP

**原文链接**: [https://medium.com/@MortezaPoussane/a-new-observer-pattern-bidirectional-signals-from-the-emitters-perspective-in-php-d8a555939e15](https://medium.com/@MortezaPoussane/a-new-observer-pattern-bidirectional-signals-from-the-emitters-perspective-in-php-d8a555939e15)

本文介绍了一种使用 `php-repos/observer` 扩展包在 PHP 中实现观察者模式的新颖方法，将重点从观察者转移到*发射器*。发射器不仅可以简单地广播事件，还可以分派信号，从处理器Solicitor响应（反向信号），从而影响发射器的流程。这创建了一个更反映真实业务交互的双向通信通道。

该扩展包定义了七种信号类型：`Signal`（基本类型）、`Event`、`Plan`、`Inquiry`、`Message`、`Command`，以及用于可观察性的内部信号。处理器是订阅特定信号并可以返回反向信号的可调用对象。

主要功能包括：双向信号处理，允许基于处理器响应动态调整发射器的操作；通过适用于 CLI 或 Web 应用程序的查询实现灵活的输入处理；动态配置功能，允许库基于接收到的反向信号进行调整。内部信号支持调试和日志记录。

本文重点介绍了业务工作流程管理（例如，订单取消）、跨平台输入、动态配置（例如，数据库选择）和审计等用例。与传统观察者模式的核心区别在于以发射器为中心的设计，从而实现更具交互性和业务驱动的应用程序。该扩展包可在 https://github.com/php-repos/observer.git 获取。

---

## 65. 一个20年前的算法能帮助我们理解Transformer嵌入

**原文标题**: A 20-Year-Old Algorithm Can Help Us Understand Transformer Embeddings

**原文链接**: [http://ai.stanford.edu/blog/db-ksvd/](http://ai.stanford.edu/blog/db-ksvd/)

本文探讨了使用一种有20年历史的字典学习算法KSVD来理解大型语言模型(LLM)的内部运作。目标是将复杂的LLM嵌入分解为人类可解释的概念向量，从而解决LLM正在思考什么“概念”的问题。

尽管最近的工作主要集中于在此背景下使用稀疏自编码器(SAE)进行字典学习，但作者认为，像KSVD这样的传统方法同样有效，并具有理论优势。他们引入了双批次KSVD (DB-KSVD)，这是一种高度优化的实现，与朴素方法相比，速度提高了10,000倍，使得在几分钟内分析LLM嵌入成为可能。

作者使用SAEBench基准测试证明了DB-KSVD的性能，在与嵌入重建、特征解耦和可解释性相关的指标上取得了具有竞争力的结果。这表明经典的字典学习方法对于大规模问题仍然适用。

本文还讨论了字典学习的理论限制，强调了数据集大小、嵌入维度和字典不相干性的重要性。这些因素决定了从叠加表示中恢复概念向量的可行性。作者最后强调了字典学习在语言模型以外的各个领域的潜力，例如机器人和视觉，这些领域存在信息丰富的嵌入。

---

## 66. Bitwig Studio 6 详情公布，编辑功能大幅提升

**原文标题**: Bitwig Studio 6 details revealed, and editing gets a big boost

**原文链接**: [https://cdm.link/bitwig-studio-6-details/](https://cdm.link/bitwig-studio-6-details/)

Bitwig Studio 6 is set to deliver significant enhancements to editing and workflow, focusing on improvements engineers and users want. The update bypasses current trends like AI and stem separation, instead prioritizing refined editing tools and an updated UI. A beta is available for those with an active Upgrade Plan, with a full release planned for the fall.

Key features include:

*   **Automation Mode:** Allows users to overlay a single automation lane on each track for focused editing.
*   **Improved Editing Gestures:** Easier grabbing, dragging, and overwriting of automation.
*   **Automation Behaviors:** Spread, hold, and curvature options for automation.
*   **New Tools:** Spray Can for automation, Audition tool, and optimized Pencil with previews.
*   **Automation Clips:** Create automation clips that exist alongside audio/MIDI clips, functioning similarly to "dummy clips."
*   **Expression Editing:** Direct editing of note expression parameters like gain and pressure.
*   **Multi-Clip Editing:** Edit multiple clips simultaneously within the Detail Editor Panel.
*   **Clip Aliases:** Master templates for clips, where changes to the template affect all linked clips.
*   **Project-Wide Key Signatures:** Key signatures that apply across the project, impacting Piano Roll, Snap to Key, and note FX.
*   **Updated Interface:** A new palette of editing tools, grid adjustments, arranger auto-zoom, and dynamic track headers.

The update also includes project backups for older versions and adds Grid modules for pitch and key manipulation (Scale, Scale Steps, Root Key). While themes are still absent, the overall focus is on enhancing editing efficiency and creative control.


---

## 67. Tau² 基准测试实战：初步结果与主要结论

**原文标题**: Tau² Benchmark in Action: Early Results and Key Takeaways

**原文链接**: [https://quesma.com/blog/tau2-from-llm-benchmark-to-blueprint-for-testing-ai-agents/](https://quesma.com/blog/tau2-from-llm-benchmark-to-blueprint-for-testing-ai-agents/)

本文探讨了 Tau² 基准测试，该测试最近被用于展示 GPT-5 的 Agentic 工具调用能力，重点介绍了其用于测试 AI Agentic 系统的方法。Tau² 不仅限于简单的 LLM 比较，还提供了一种新颖的方法来评估 AI Agent 在真实的、工具驱动的场景中的表现。

该基准测试包含电信、零售和航空等领域，每个领域包含多个测试用例。在一个测试用例中，Agent（AI 驱动的系统）与 User（模拟人）交互以解决特定问题，并使用外部工具（API、数据库）进行辅助。User 和 Agent 均由 LLM 提供支持，生成动态的、非脚本化的对话。

评估涉及多个层次：数据库检查、动作检查（正确的工具调用）、字符串存在性检查以及由单独的 LLM 评判器评估的“NL 断言”，以评估 Agent 的行为是否符合人类的期望和业务规则。

运行该基准测试需要 Python 环境、LLM API 密钥和 Tau² 工具。虽然具有启发性，但测试资源密集且耗时。

作者强调了测试的非确定性性质，指出了“假阴性”的实例，以及模糊性如何导致意想不到的结果。这种不稳定性被视为类人交互的特征，而不是错误，因此需要与传统的集成测试不同的方法。

作者的结论是，Tau² 为测试基于 AI 的系统提供了一种清晰的方法，通过将定量措施应用于非确定性操作，推动开发朝着软件工程领域的新最佳实践发展。

---

## 68. Lunar soil machine developed to build bricks using sunlight

**原文标题**: Lunar soil machine developed to build bricks using sunlight

**原文链接**: [https://www.moondaily.com/reports/Lunar_soil_machine_developed_to_build_bricks_using_sunlight_999.html](https://www.moondaily.com/reports/Lunar_soil_machine_developed_to_build_bricks_using_sunlight_999.html)

A Chinese research team at the Deep Space Exploration Laboratory (DSEL) has developed a prototype machine capable of transforming lunar soil (regolith) into construction bricks using concentrated solar energy. The machine uses a parabolic reflector and fiber optics to focus sunlight, achieving temperatures exceeding 1,300°C to melt the lunar soil without additives. The resulting bricks are dense and robust, suitable for building shelters, roads, and platforms on the Moon.

While the bricks cannot independently withstand the moon's vacuum and low gravity, they are designed to serve as protective layers for pressure-retaining habitat modules. This development is significant for China's International Lunar Research Station (ILRS) project, a joint venture aiming to establish a lunar base by 2035.

As part of preparations, simulated lunar bricks will be tested in space for thermal durability, mechanical integrity, and radiation shielding. The ultimate goal is to enable full-scale lunar surface construction supported by automated robots and the brick-making device, contributing to the establishment of a sustainable lunar base.


---

## 69. TPDE-LLVM：更快的LLVM -O0后端

**原文标题**: TPDE-LLVM: Faster LLVM -O0 Back-End

**原文链接**: [https://discourse.llvm.org/t/tpde-llvm-10-20x-faster-llvm-o0-back-end/86664](https://discourse.llvm.org/t/tpde-llvm-10-20x-faster-llvm-o0-back-end/86664)

TPDE has open-sourced TPDE-LLVM, a fast LLVM back-end significantly faster than LLVM's -O0 back-end (10-20x). While producing code with similar runtime performance to LLVM -O0, it results in 10-30% larger code size. It currently supports a subset of LLVM-IR and targets x86-64 and AArch64. Performance data on SPEC CPU 2017 shows substantial compile-time speedups compared to LLVM 19 -O0.

The back-end works through IR cleanup, analysis (loop+liveness), and a combined codegen pass for lowering, regalloc, and machine code encoding. Current goals focus on supporting typical Clang O0/O1 IR, with future plans including DWARF support and improved register allocation.

The authors addressed why not make LLVM faster, noting recent LLVM improvements but suggesting deeper changes are needed for a 10x speedup. They identify problematic LLVM-IR features like ConstantExprs, arbitrarily-sized struct/array values, thread-local globals, and arbitrary bit-width arithmetic as hindering performance. They also shared "fun" facts about optimizing their implementation. TPDE-LLVM is usable as a library, an llc-like tool, or integrated into Clang (with a patch).


---

## 70. Cline and LM Studio: the local coding stack with Qwen3 Coder 30B

**原文标题**: Cline and LM Studio: the local coding stack with Qwen3 Coder 30B

**原文链接**: [https://cline.bot/blog/local-models](https://cline.bot/blog/local-models)

生成摘要时出错

---

## 71. What Unix Pipelines Got Right (and How We Can Do Better)

**原文标题**: What Unix Pipelines Got Right (and How We Can Do Better)

**原文链接**: [https://programmingsimplicity.substack.com/p/what-unix-pipelines-got-right-and](https://programmingsimplicity.substack.com/p/what-unix-pipelines-got-right-and)

生成摘要时出错

---

## 72. Climate change will worsen hunger

**原文标题**: Climate change will worsen hunger

**原文链接**: [https://www.vox.com/climate/417164/crop-food-rice-wheat-climate-change-midwest](https://www.vox.com/climate/417164/crop-food-rice-wheat-climate-change-midwest)

生成摘要时出错

---

## 73. Survey: a third of senior developers say over half their code is AI-generated

**原文标题**: Survey: a third of senior developers say over half their code is AI-generated

**原文链接**: [https://www.fastly.com/blog/senior-developers-ship-more-ai-code](https://www.fastly.com/blog/senior-developers-ship-more-ai-code)

生成摘要时出错

---

## 74. Run a legal LTE network at home for $100

**原文标题**: Run a legal LTE network at home for $100

**原文链接**: [https://lantian.pub/en/article/modify-computer/legal-lte-network-at-home-for-100-bucks.lantian/](https://lantian.pub/en/article/modify-computer/legal-lte-network-at-home-for-100-bucks.lantian/)

生成摘要时出错

---

## 75. Why haven't quantum computers factored 21 yet?

**原文标题**: Why haven't quantum computers factored 21 yet?

**原文链接**: [https://algassert.com/post/2500](https://algassert.com/post/2500)

生成摘要时出错

---

## 76. A Case Study in Rewriting a Critical Service in Rust

**原文标题**: A Case Study in Rewriting a Critical Service in Rust

**原文链接**: [https://wxiaoyun.com/blog/rust-rewrite-case-study/](https://wxiaoyun.com/blog/rust-rewrite-case-study/)

生成摘要时出错

---

## 77. Hobbyist Maintainers with Thomas DePierre

**原文标题**: Hobbyist Maintainers with Thomas DePierre

**原文链接**: [https://opensourcesecurity.io/2025/2025-06-hobbyist-thomas-depierre/](https://opensourcesecurity.io/2025/2025-06-hobbyist-thomas-depierre/)

生成摘要时出错

---

## 78. How to run latest Vegas Pro 22 in Windows 7 x64

**原文标题**: How to run latest Vegas Pro 22 in Windows 7 x64

**原文链接**: [https://trackerninja.codeberg.page/post/how-to-run-latest-vegas-pro-22-in-windows-7-no-matter-what/](https://trackerninja.codeberg.page/post/how-to-run-latest-vegas-pro-22-in-windows-7-no-matter-what/)

生成摘要时出错

---

## 79. Vibe coding as a coding veteran: from 8-bit assembly to English-as-code

**原文标题**: Vibe coding as a coding veteran: from 8-bit assembly to English-as-code

**原文链接**: [https://levelup.gitconnected.com/vibe-coding-as-a-coding-veteran-cd370fe2be50](https://levelup.gitconnected.com/vibe-coding-as-a-coding-veteran-cd370fe2be50)

生成摘要时出错

---

## 80. Is it possible to allow sideloading and keep users safe?

**原文标题**: Is it possible to allow sideloading and keep users safe?

**原文链接**: [https://shkspr.mobi/blog/2025/08/is-it-possible-to-allow-sideloading-and-keep-users-safe/](https://shkspr.mobi/blog/2025/08/is-it-possible-to-allow-sideloading-and-keep-users-safe/)

生成摘要时出错

---

## 81. F-Droid site certificate expired

**原文标题**: F-Droid site certificate expired

**原文链接**: [https://gitlab.com/fdroid/fdroid-website/-/issues/883](https://gitlab.com/fdroid/fdroid-website/-/issues/883)

生成摘要时出错

---

## 82. Replacing a cache service with a database

**原文标题**: Replacing a cache service with a database

**原文链接**: [https://avi.im/blag/2025/db-cache/](https://avi.im/blag/2025/db-cache/)

生成摘要时出错

---

## 83. Intel Files Patent for "Software Defined Super Cores"

**原文标题**: Intel Files Patent for "Software Defined Super Cores"

**原文链接**: [https://videocardz.com/newz/intel-files-patent-for-software-defined-super-cores](https://videocardz.com/newz/intel-files-patent-for-software-defined-super-cores)

生成摘要时出错

---

## 84. NetSurf on ReMarkable 2

**原文标题**: NetSurf on ReMarkable 2

**原文链接**: [https://akselmo.dev/posts/netsurf-on-remarkable-2/](https://akselmo.dev/posts/netsurf-on-remarkable-2/)

生成摘要时出错

---

## 85. Red: A programming language inspired by REBOL

**原文标题**: Red: A programming language inspired by REBOL

**原文链接**: [https://github.com/red/red](https://github.com/red/red)

生成摘要时出错

---

## 86. What Are Traces and Spans in OpenTelemetry?

**原文标题**: What Are Traces and Spans in OpenTelemetry?

**原文链接**: [https://oneuptime.com/blog/post/2025-08-27-traces-and-spans-in-opentelemetry/view](https://oneuptime.com/blog/post/2025-08-27-traces-and-spans-in-opentelemetry/view)

生成摘要时出错

---

## 87. Show HN: An ncurses CUDA-based fluid simulation

**原文标题**: Show HN: An ncurses CUDA-based fluid simulation

**原文链接**: [https://github.com/seanwevans/fluid-sims](https://github.com/seanwevans/fluid-sims)

生成摘要时出错

---

## 88. The Last Vestal Virgin and the Fall of Rome

**原文标题**: The Last Vestal Virgin and the Fall of Rome

**原文链接**: [https://debramaymacleod.com/blog/the-last-vestal-virgin-and-the-fall-of-rome](https://debramaymacleod.com/blog/the-last-vestal-virgin-and-the-fall-of-rome)

生成摘要时出错

---

## 89. I Don't Have Spotify

**原文标题**: I Don't Have Spotify

**原文链接**: [https://idonthavespotify.sjdonado.com/](https://idonthavespotify.sjdonado.com/)

生成摘要时出错

---

## 90. Scientists find that ice generates electricity when bent

**原文标题**: Scientists find that ice generates electricity when bent

**原文链接**: [https://phys.org/news/2025-09-scientists-ice-generates-electricity-bent.html](https://phys.org/news/2025-09-scientists-ice-generates-electricity-bent.html)

生成摘要时出错

---

## 91. My phone is an ereader now

**原文标题**: My phone is an ereader now

**原文链接**: [https://www.davepagurek.com/blog/minimal-phone/](https://www.davepagurek.com/blog/minimal-phone/)

生成摘要时出错

---

## 92. Authenticate Thyself

**原文标题**: Authenticate Thyself

**原文链接**: [https://aeon.co/essays/the-sovereign-individual-and-the-paradox-of-the-digital-age](https://aeon.co/essays/the-sovereign-individual-and-the-paradox-of-the-digital-age)

生成摘要时出错

---

## 93. Sheafification – The optimal path to mathematical mastery: The fast track (2022)

**原文标题**: Sheafification – The optimal path to mathematical mastery: The fast track (2022)

**原文链接**: [https://sheafification.com/the-fast-track/](https://sheafification.com/the-fast-track/)

生成摘要时出错

---

## 94. My Foray into Vlang

**原文标题**: My Foray into Vlang

**原文链接**: [https://kristun.dev/posts/my-foray-into-vlang/](https://kristun.dev/posts/my-foray-into-vlang/)

生成摘要时出错

---

## 95. Show HN: Anonymous Age Verification

**原文标题**: Show HN: Anonymous Age Verification

**原文链接**: [https://gist.github.com/JWally/bf4681f79c0725eb378ec3c246cf0664](https://gist.github.com/JWally/bf4681f79c0725eb378ec3c246cf0664)

生成摘要时出错

---

## 96. Do the simplest thing that could possibly work

**原文标题**: Do the simplest thing that could possibly work

**原文链接**: [https://www.seangoedecke.com/the-simplest-thing-that-could-possibly-work/](https://www.seangoedecke.com/the-simplest-thing-that-could-possibly-work/)

生成摘要时出错

---

## 97. Nobody cares about decentralization until they do (2024)

**原文标题**: Nobody cares about decentralization until they do (2024)

**原文链接**: [https://kyefox.com/nobody-cares-about-decentralization-until-they-do/](https://kyefox.com/nobody-cares-about-decentralization-until-they-do/)

生成摘要时出错

---

## 98. Spacing Over Cards

**原文标题**: Spacing Over Cards

**原文链接**: [https://smagin.fyi/posts/padding-over-cards/](https://smagin.fyi/posts/padding-over-cards/)

生成摘要时出错

---

## 99. The Facebook crawler is hammering the internet

**原文标题**: The Facebook crawler is hammering the internet

**原文链接**: [https://twitter.com/croloris/status/1962506451718397977](https://twitter.com/croloris/status/1962506451718397977)

生成摘要时出错

---

## 100. Best practices for dealing with human waste in the great outdoors

**原文标题**: Best practices for dealing with human waste in the great outdoors

**原文链接**: [https://theconversation.com/how-to-poop-outdoors-in-a-way-that-wont-harm-the-environment-and-other-hikers-262426](https://theconversation.com/how-to-poop-outdoors-in-a-way-that-wont-harm-the-environment-and-other-hikers-262426)

生成摘要时出错

---

