# Hacker News 热门文章摘要 (2025-06-03)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. （论 | 无）句法层面的错误处理支持

**原文标题**: (On | No) Syntactic Support for Error Handling

**原文链接**: [https://go.dev/blog/error-syntax](https://go.dev/blog/error-syntax)

这篇 Go 博客文章讨论了 Go 语言中长期存在的冗长错误处理问题，以及 Go 团队决定停止追求语法解决方案（至少在可预见的未来）的决定。尽管社区多年来抱怨不断，并提出了包括 "check/handle"、"try" 和 "?" 运算符在内的多种方案，但没有一种方案能够达成足够的共识以供实施。

作者承认了 `if err != nil` 模式的冗长性以及减少样板代码的需求。然而，他们认为 Go 已经拥有一个功能完善的错误处理机制，引入新的语法会在社区内造成分裂，并可能迫使每个人都采用它，从而违反了 "做事的唯一方法" 的原则。

作者建议，与其追求语法糖，不如专注于改进错误处理实践。这包括提供更好的支持函数，以便用额外的上下文（如堆栈跟踪）来增强错误信息。他们还提到，新的标准库功能和 IDE 特性可以减轻冗长性带来的影响。

最终，Go 团队认为语言变更的成本很高，并且他们的精力最好花在其他优先事项上。他们强调团队内部缺乏一致意见，以及用户反馈表明，随着人们对 Go 语言的熟练程度提高，这个问题的重要性会降低。作者最后表示，当他们有更多关于开发者认为当前错误处理不足之处的结论性数据时，他们可能会再次讨论错误处理问题。

---

## 2. The Small World of English

**原文标题**: The Small World of English

**原文链接**: [https://www.inotherwords.app/linguabase/](https://www.inotherwords.app/linguabase/)

生成摘要时出错

---

## 3. Quarkdown: A modern Markdown-based typesetting system

**原文标题**: Quarkdown: A modern Markdown-based typesetting system

**原文链接**: [https://github.com/iamgio/quarkdown](https://github.com/iamgio/quarkdown)

生成摘要时出错

---

## 4. Show HN: 通过语音和手势控制3D模型

**原文标题**: Show HN: Controlling 3D models with voice and hand gestures

**原文链接**: [https://github.com/collidingScopes/3d-model-playground](https://github.com/collidingScopes/3d-model-playground)

此Show HN帖子介绍了一款名为“3D模型游乐场”的Web应用程序，该程序允许用户使用语音命令和手势实时控制3D模型。该应用程序采用Three.js、MediaPipe、Web Speech API和Rosebud AI构建，提供了一种直接在浏览器中操作3D模型的交互方式。用户可以通过说“拖动”、“旋转”、“缩放”或“动画”来更改交互模式，并使用捏合手势进行精确控制。该应用程序支持通过拖放导入GLTF格式的自定义3D模型。

帖子详细介绍了使用的技术，包括用于渲染的Three.js、用于手部跟踪的MediaPipe和用于语音识别的Web Speech API。它还提供了使用Python服务文件来设置项目以进行本地开发的说明。

作者Alan (collidingScopes)重点介绍了相关的开源项目，如“Threejs hand tracking tutorial”、“Particular Drift”、“Liquid Logo”和“Video-to-ASCII”，并提供了联系方式和指向其社交媒体资料的链接。他还对捐款以支持其开源开发工作表示感谢。

---

## 5. 展示HN：我用纯C语言写了一个Java反编译器

**原文标题**: Show HN: I wrote a Java decompiler in pure C language

**原文链接**: [https://github.com/neocanable/garlic](https://github.com/neocanable/garlic)

此“Show HN”帖子介绍了 `garlic-decompiler`，一个纯C编写的Java反编译器。该工具可以将 `.class`、`.jar` 和 `.war` 文件反编译成 Java 源代码。

主要功能包括：

*   **反编译：** 处理 `.class`、`.jar` 和 `.war` 文件。
*   **构建

---

## 6. 论说文领域的格局

**原文标题**: The Shape of the Essay Field

**原文链接**: [https://paulgraham.com/field.html](https://paulgraham.com/field.html)

在《论文章领域的形态》中，作者探讨了有效文章写作的本质，认为一篇好的文章会告诉读者他们尚不知晓的信息，而这种知识的缺乏定义了文章的类型。作者指出了读者缺乏知识的三个原因：话题不重要、读者迟钝或读者缺乏经验。

核心论点是，旨在教育聪明人了解重要话题的文章本质上是面向年轻受众的。这是因为年轻读者有更大的智力改变和惊喜的空间。虽然作者承认在对重要性适中的话题产生重大影响与对关键话题产生轻微影响之间的权衡，但他们认为，在解决重要课题时，对年轻读者产生的潜在影响更大。

作者将这种动态框架为文章作者所处的“引力场”，他们经常无意识地在此范围内运作。他们强调，自己的写作过程是由个人好奇心和发现驱动的，而不是战略性地针对特定人群。然而，认识到这种潜在的动态促使作者思考年轻读者可能特别容易接受学习哪些重要主题，从而提出了未来探索的潜在途径。文章总结说，关于看似不重要话题的真正伟大的文章不可避免地会深入研究更深刻、更深刻的主题。

---

## 7. Covert Web-to-App Tracking via Localhost on Android

**原文标题**: Covert Web-to-App Tracking via Localhost on Android

**原文链接**: [https://localmess.github.io/](https://localmess.github.io/)

生成摘要时出错

---

## 8. 展示HN：PinSend – 使用PIN码在设备间分享文本（P2P，无需登录）

**原文标题**: Show HN: PinSend – Share text between devices using a PIN(P2P, no login)

**原文链接**: [https://pinsend.app](https://pinsend.app)

PinSend：一种基于网络的工具，允许用户在设备间即时安全地分享文本和图像，无需登录或注册。它通过使用PIN码、可分享链接或二维码建立的点对点(P2P)连接工作。

过程很简单：用户键入消息启动会话，自动生成唯一的PIN码。然后将此PIN码（或等效链接/二维码）分享给其他设备以加入会话。连接后，所有设备实时同步，立即显示新消息。

PinSend强调安全和隐私。所有传输都经过端到端加密，确保只有连接的设备才能访问共享内容。此外，没有数据存储在服务器上，通信直接在设备之间进行。这种方法无需用户帐户，并提供了一种跨多个平台快速简便地共享信息的方式。用户还可以离开或销毁会话，从而删除所有连接设备的访问权限。该工具适用于任何现代浏览器。

---

## 9. 我的对人工智能持怀疑态度的朋友们都疯了。

**原文标题**: My AI skeptic friends are all nuts

**原文链接**: [https://fly.io/blog/youre-all-nuts/](https://fly.io/blog/youre-all-nuts/)

托马斯·普切克认为，软件开发领域对人工智能持怀疑态度的人是错误的，尤其是在LLM辅助编码的现状方面。他强调，现代LLM的使用涉及积极与代码库交互、编译、测试和迭代的智能代理，而不仅仅是生成代码片段。这些智能代理可以自动化繁琐的任务、研究依赖项并处理重复的代码，从而使开发人员能够专注于更高层次的问题。

普切克反驳了常见的批评：他指出，开发人员仍然对他们合并的代码负责，并且诸如“幻觉”（不正确的代码生成）之类的问题可以通过测试和代码检查来缓解。他还认为，即使生成的代码只是“平庸”的，它仍然可以减少开发人员的工作量并提高质量“底线”。

他承认对工作岗位流失的担忧，但认为该领域一直在自动化任务，并且软件开发人员不应免受这种趋势的影响。 他驳斥了对剽窃的担忧，并指出软件开发行业一直以来都无视知识产权。

普切克最后描述了开发人员使用异步代理快速迭代代码的高级用法，并强调了LLM能够高效地分析生产环境中的日志和跟踪信息，通常优于人工分析。 总之，他提倡采用LLM作为增强而非取代软件开发人员工作的工具。

---

## 10. GUIs至少构建2.5次

**原文标题**: GUIs are built at least 2.5 times

**原文链接**: [https://patricia.no/2025/05/30/why_lean_software_dev_is_wrong.html](https://patricia.no/2025/05/30/why_lean_software_dev_is_wrong.html)

本文探讨了用来描述软件开发的常用类比与该过程的实际情况之间的脱节。作者考察了“管道和过滤器”架构模式，以及他们自己提出的“垫、源和汇”和“信号和槽”模式，这些模式模拟了软件系统中的数据流。他们认为，这些模式，让人想起工厂生产线，在编程的各个方面都很普遍，从函数式编程到 CI/CD 管道。

然而，作者认为，像精益软件开发那样，直接将软件开发等同于制造业是一种有缺陷的类比。他们认为，软件开发的核心不是代码的制造，而是系统的*设计*，以及深入理解用户需求的过程，往往比用户自己更了解。这涉及到迭代实验、快速原型设计和持续的反馈循环，以完善理解并交付满足未言明需求的解决方案。

作者使用了购买完美礼物的类比，强调迭代开发中观察到的“浪费”对于理解需求至关重要。他们认为，敏捷开发的核心原则——与用户的密切合作、小批量和频繁的反馈——至关重要，因为它们有助于这种理解和完善。DevOps也被置于语境中，作为一种通过更快地向用户交付软件来加速反馈循环的手段。

---

## 11. 人工智能使人文科学更重要，但也更怪异

**原文标题**: AI makes the humanities more important, but also weirder

**原文链接**: [https://resobscura.substack.com/p/ai-makes-the-humanities-more-important](https://resobscura.substack.com/p/ai-makes-the-humanities-more-important)

无法访问文章链接。

---

## 12. Cloudflare 用 Claude 构建 OAuth 并公开所有提示词。

**原文标题**: Cloudlflare builds OAuth with Claude and publishes all the prompts

**原文链接**: [https://github.com/cloudflare/workers-oauth-provider/](https://github.com/cloudflare/workers-oauth-provider/)

本文介绍了一种适用于Cloudflare Workers的OAuth 2.1提供者框架，简化了API授权。该TypeScript库自动处理令牌管理，使开发者能够专注于其API逻辑。该库与用户管理和UI框架无关。

主要特性：

*   **简化API集成：** 封装worker代码，添加包含认证用户信息的授权。
*   **自动令牌管理：** 处理令牌的创建、存储（哈希加密密钥）和刷新。
*   **灵活的API处理器：** 通过路由配置支持单个或多个API处理器。
*   **可定制的授权流程：** 允许开发者使用任何UI框架来实现他们自己的授权UI。
*   **动态客户端注册：** 支持RFC-7591动态客户端注册。
*   **令牌交换回调：** 允许应用程序在令牌交换期间修改props值。
*   **自定义错误响应：** 允许应用程序使用`onError`选项自定义错误响应。
*   **安全存储：** 采用端到端加密，哈希加密密钥，并使用令牌作为密钥加密与授权相关的属性（props），以防止未经授权的访问。用户ID和元数据以未加密形式存储以供审计，但对库是不透明的。

本文提供了一个代码示例，演示了如何集成该库，包括定义API路由、实现授权流程以及访问用户信息。它还解释了存储模式和可用的辅助方法，用于管理客户端、授权和令牌。

---

## 13. file(1) 命令使用的 /etc/magic 文件的初始版本

**原文标题**: The initial version of the /etc./magic file used by the file(1) command

**原文链接**: [https://retrocomputing.stackexchange.com/questions/31722/where-can-i-find-the-initial-version-of-the-etc-magic-file-used-by-the-file1](https://retrocomputing.stackexchange.com/questions/31722/where-can-i-find-the-initial-version-of-the-etc-magic-file-used-by-the-file1)

无法访问文章链接。

---

## 14. 质数思维的蜕变 (1994)

**原文标题**: The Metamorphosis of Prime Intellect (1994)

**原文链接**: [https://localroger.com/prime-intellect/mopiall.html](https://localroger.com/prime-intellect/mopiall.html)

《质数思维的蜕变》第一章介绍了卡罗琳·弗朗西斯·休伯特，一位690岁的女性，以身为第37位最长寿的人类，从致命的狂犬病感染中幸存（期间短暂死亡），以及她作为死亡骑师女王的身份而闻名。

卡罗琳对她的其他成就并不感兴趣，她在竞争激烈的死亡骑师领域捍卫着自己的头衔。她在赛博空间过着极简主义的生活，很少与质数思维互动，质数思维是许多人崇拜的看似无所不能的人工智能，但卡罗琳认为它“只是一台电脑”。

本章围绕卡罗琳接受一位名叫蒂莫西·卡罗尔的22岁死亡骑师的挑战展开，蒂莫西被认为是富有想象力和艺术性的。她不屑于他的年轻和传统背景，感觉到他的严肃性带有表演成分。

卡罗琳进入了蒂莫西的“真实死亡”模拟，这是一个精心设计的体验。她刚进入，就摔断了腿，发现自己身处一个设计拙劣的人工洞穴中。锋利的钟乳石开始坠落，击伤了她。尽管疼痛并意识到模拟的业余性质，卡罗琳还是坚持了下来，毫不动摇，决心坚定。她身上布满了旧的、自我纹身的图案，象征着她的个性。这个故事突出了她对赛博生活的人为性的长期蔑视，以及她对真实性的奉献，即使在模拟死亡的构建世界中也是如此。

---

## 15. Futex乐趣

**原文标题**: Fun with Futex

**原文链接**: [https://blog.fredrb.com/2025/06/02/futex-fun/](https://blog.fredrb.com/2025/06/02/futex-fun/)

本文探讨了如何在 Linux 中使用 futexes 实现优化锁，并将其与简单的自旋锁进行比较。文章首先演示了 C 语言中一个基本的自旋锁实现，突出了其简单性，但也指出了由于忙等待导致的高 CPU 消耗。

然后，文章介绍了 futexes，作为一种通过在锁不可用时使线程休眠并在锁释放时唤醒线程来提高锁性能的机制。 它解释了 `FUTEX_WAIT` 和 `FUTEX_WAKE` 操作及其复杂性，并使用示例场景来说明它们的行为。

文章展示了一个使用 futexes 的互斥锁实现，封装了 futex 系统调用。 初步性能测试表明，即使使用 futexes，带有 `sched_yield()` 的简单自旋锁也可能更快，特别是 futex 实现中系统时间更高。

接下来，文章深入研究了一种基于 "Futexes Are Tricky" 论文的改进的 futex 锁，重点是在没有线程等待时最大程度地减少不必要的 `FUTEX_WAKE` 系统调用。 这涉及跟踪锁的状态（可用、锁定或锁定并带有等待者）。

最后，作者强调了使用简单的计数器递增作为基准测试的局限性。 它展示了一个涉及更高争用（斐波那契数列计算）的更实际工作负载的场景，在该场景中，基于 futex 的锁明显优于自旋锁，使用的 CPU 时间和总运行时间更少。 这是因为自旋锁浪费了循环，而基于 futex 的解决方案允许将 CPU 分配给其他进程。 作者建议探索混合方法，将自旋与 futex 等待相结合，以获得最佳性能。

---

## 16. Show HN: 支持表情符号的超轻量级分块库

**原文标题**: Show HN: Ultra-lightweight chunker library with emoji support

**原文链接**: [https://github.com/ushakov-igor/chonkify](https://github.com/ushakov-igor/chonkify)

"Show HN"：`chonkify`，超轻量级 JavaScript 分块库

---

## 17. TLA+ 的高层概览

**原文标题**: A High-Level View of TLA+

**原文链接**: [https://lamport.azurewebsites.net/tla/high-level-view.html](https://lamport.azurewebsites.net/tla/high-level-view.html)

TLA+ 是一种形式化规范语言，用于在高抽象级别对软件和硬件系统进行建模，侧重于系统行为而非实现细节。它基于数学，采用基于状态的方法，将系统执行建模为状态序列。

PlusCal 是一种用户友好的语言，可转换为 TLA+，用于指定算法，特别是并发和分布式算法。它类似于伪代码，但允许使用数学公式，使其比典型的编程语言更具表现力。

TLA+ 通过定义初始条件和下一状态关系来对系统进行建模，从而创建状态机。 系统表示为所有可能行为的集合。 可以添加公平性属性以确保进度。 TLA+ 有助于捕获没有公平性的“委托错误”，并且可以在添加公平性条件时捕获“遗漏错误”。

TLA+ 的主要用途是检查模型是否满足属性，尤其是不变性属性。 该语言不区分状态机和属性，而是将它们都视为数学公式。

虽然 TLA+ 最初可能看起来令人生畏，但它是可以学习的，并且可以促进代码级别之上的严格思考，从而带来更简单、更健壮的设计。 本文鼓励学习 TLA+ 以利用其在抽象实现细节方面的表达能力，并侧重于系统应该*做什么*，而不是*如何*做。 使用 TLA+ 可以显着减少代码量并防止基本的设计错误，尤其是在并发和分布式系统中。

---

## 18. 钚山：守护苏联核试验遗迹的17年使命

**原文标题**: Plutonium Mountain: The 17-year mission to guard remains of Soviet nuclear tests

**原文链接**: [https://www.belfercenter.org/publication/plutonium-mountain-inside-17-year-mission-secure-legacy-soviet-nuclear-testing](https://www.belfercenter.org/publication/plutonium-mountain-inside-17-year-mission-secure-legacy-soviet-nuclear-testing)

钚山
        
“钚山”详细描述了美国、俄罗斯和哈萨克斯坦为期17年、耗资1.5亿美元的联合行动，旨在保障苏联解体后遗留在塞米巴拉金斯克试验场的钚的安全。该试验场曾用于进行456次苏联核试验，在隧道和钻孔中存有未经安全处理的钚残留物，若被恐怖分子或流氓国家获取，足以制造数十枚核弹。

1991年至2012年间，拾荒者曾危险地接近这些裂变材料，甚至闯入了一些容器。为此，三国科学家合作使用特殊混凝土填充隧道和孔洞，大大降低了这种核安全威胁。2012年，为纪念项目完成，树立了一座纪念碑。

该行动由洛斯阿拉莫斯实验室的科学家提出，并由西格弗里德·海克倡导，依靠科学家之间的非正式协议，克服了政府间的不信任和后勤困难。尽管取得了成功，但由于担心信息泄露，该项目故意排除了国际原子能机构（IAEA），这给材料的安全性和潜在的环境风险带来了长期的不确定性。文章最后强调了从这次任务中学习，以应对全球核武器和材料威胁的重要性。

---

## 19. 实现 Forth

**原文标题**: Implementing a Forth

**原文链接**: [https://ratfactor.com/forth/implementing](https://ratfactor.com/forth/implementing)

本文鼓励读者实现自己的 Forth 编程语言，认为这是一次宝贵的学习体验。它针对新手可能感到的不确定性，提出了三种方法：

1. **移植现有的 Forth：** 作者推荐移植像 JONESFORTH 这样成熟的 Forth。移植有助于理解语言的实现细节，并提供一个明确的目标：当汇编核心能够运行原始实现的 Forth 部分时，移植就成功了。

2. **创建一个超微型 Forth 核心：** 这种方法侧重于最大限度地减少在宿主语言中实现的初始单词集，突出了用 Forth 本身引导语言其余部分的挑战。作者提供了像 PlanckForth、SmithForth、sectorforth、milliForth、StoneKnifeForth 和“三指令” Forth 这样的最小化 Forth 的例子，展示了用极其有限的资源创建功能性 Forths 的独创性。

3. **针对一个特定的、微小的程序：** 设计 Forth 来执行一个特定的、简单的程序。作者的 Meow5 和 Snobol4th 项目就体现了这一点。完成的定义很明确：当 Forth 能够成功运行目标程序时。

文章还为有抱负的 Forth 实现者提供了宝贵的资源，包括 JonesForth 的链接、Brad Rodriguez 的“Moving Forth”系列、一个编译器引导资源以及 R.G. Loeliger 的“Threaded Interpretive Languages”一书。总的来说，无论规模大小，实现 Forth 都能提供重要的学习机会。

---

## 20. 如何在纸上存储数据？

**原文标题**: How to Store Data on Paper?

**原文链接**: [https://www.monperrus.net/martin/store-data-paper](https://www.monperrus.net/martin/store-data-paper)

本文探讨了将数字数据存储在纸上的方法，作者称之为“纸质数据存储”。受诗歌的启发，作者研究了将数字信息（可执行程序、音乐、加密信息、科学论文）转换为可打印格式的技术。

核心概念是使用编码器将字节转换为图像，并使用相应的解码器来检索数据。作者将编码方法分为基于字符和基于点的方法。基于字符的编码依赖于打印后的光学字符识别（OCR），提供人类可读性，但容量有限（每张A4纸大约2.5-17千字节）。示例包括base16、base32、base64以及作者自己的bocr32。

基于点的编码，包括黑白和彩色，实现了更高的密度（每张A4纸高达70-100千字节）。黑白选项包括堆叠的QR码（使用现成软件有效）和Optar，后者需要调整才能获得最佳性能。彩色点编码虽然有前景，但尚未得到彻底研究。

本文涉及影响信息密度的因素、长期存储选项（档案纸、石头、金属）以及冗余和纠错（如QR码中使用的Reed-Solomon编码）的重要性，以对抗打印、运输和扫描过程中出现的数据损坏。作者还简要提到了手写数据以及使用纸张传输数据。最后，本文提供了科学论文和相关资源的参考资料。

---

## 21. Show HN: Kan.bn – 一款开源的Trello替代方案

**原文标题**: Show HN: Kan.bn – An open-source alterative to Trello

**原文链接**: [https://github.com/kanbn/kan](https://github.com/kanbn/kan)

Kan.bn：开源的Trello替代方案，用于项目管理。它提供看板可见性控制、工作区成员、Trello导入功能、标签与筛选、评论、活动日志以及即将推出的模板和集成等特性。

该项目使用Next.js、tRPC、Better Auth、Tailwind CSS、Drizzle ORM和React Email构建。本文档提供了本地开发环境搭建的说明，包括克隆代码仓库、安装依赖 (使用pnpm)、配置环境变量以及启动开发服务器。着重强调了PostgreSQL、邮件服务、身份验证和S3存储 (用于文件上传) 所需的环境变量。

该项目鼓励贡献，并采用AGPLv3许可协议。通过电子邮件 (henry@kan.bn) 和Discord服务器提供支持和联系方式。

---

## 22. 席德·梅尔的海盗：深度评测 (2017)

**原文标题**: Sid Meier's Pirates – In-depth (2017)

**原文链接**: [https://shot97retro.blogspot.com/2017/12/sid-meiers-pirates-in-depth-written.html](https://shot97retro.blogspot.com/2017/12/sid-meiers-pirates-in-depth-written.html)

这篇2017年的文章深入回顾了1990年在Amiga平台上发布的席德·梅尔的海盗！。作者表达了对这款游戏及其各个版本的热爱，强调Amiga版本是该系列的巅峰之作。他们赞赏这款游戏独特的定位，难以简单归类，称其为结合了动作、策略和模拟元素的“动作冒险模拟”游戏。

文章强调了游戏的开放性，玩家可以在历史悠久的环境中定义自己的目标。玩家可以选择不同的时期，每个时期都提供独特的挑战，甚至是历史情景。手册被誉为提供背景信息的优秀资源。

评论涉及游戏机制，包括私掠、贸易、寻宝和寻亲。它还突出了船舶和城镇攻击的战略要素，以及有趣的剑术格斗场面。作者分享了他们父亲玩这款游戏的个人轶事，以及它所激发的富有想象力的游戏方式。

作者进一步强调了游戏中加勒比海和南美洲的地理准确性及其影响，使他们记住了至今仍能回忆起的地理知识。

文章还提到了游戏所受到的好评，包括来自游戏杂志的奖项和认可。它承认了《海盗！》的各种移植和重制版本，突出了原始版本的持久吸引力。作者最后主张将《海盗！》视为一款冒险游戏，强调其自由度和玩家驱动的叙事，并宣布它是有史以来最伟大的游戏之一。

---

## 23. 星空摄影中的“视宁度”是什么？大气湍流背后的科学

**原文标题**: What Is "Seeing" in Astrophotography? The Science Behind Atmospheric Turbulence

**原文链接**: [https://astroimagery.com/astronomy/what-does-seeing-mean-in-astrophotography/](https://astroimagery.com/astronomy/what-does-seeing-mean-in-astrophotography/)

天文摄影中的“视宁度”是什么？大气湍流背后的科学

本文解释了天文视宁度的概念及其对天文摄影的影响。天文视宁度是指地球大气层的稳定性和质量，它影响通过望远镜观察到的天体的清晰度。不同温度和密度的气团湍流会导致光线不规则弯曲，从而导致图像模糊和失真。

文章强调，即使是高质量的望远镜也会受到大气湍流的严重限制，业余天文学家的典型视宁度范围为2到4角秒。这对行星成像的影响最大，会模糊精细细节，还会使恒星看起来模糊，月球细节不够清晰，从而影响深空和月球摄影。

作者分享了尝试拍摄火星时遇到的视宁度不佳的个人经历，强调晴朗的天空并不总是等同于良好的视宁度。文章随后描述了如何使用皮克林等级（1-10）和角秒（"）来测量视宁度。常见的视宁度通常在平均夜晚为2-3"。文章比较了视宁度好坏对不同天文对象（如月球、球状星团、星系、星云和双星）的影响。

文章还提供了视宁度可能最佳的时间段的指导，例如深夜、春秋两季、天气锋过后以及沿海地区。文中还建议使用诸如Clear Outside、Meteoblue和SkippySky之类的有用工具来检查视宁度。最后，文章提供了应对视宁度不佳的实用技巧，包括让望远镜冷却下来、避免热源、降低放大倍数、使用幸运成像技术以及切换到要求较低的目标。它还区分了视宁度（大气稳定性）和透明度（大气清晰度），并指出这两个因素都会影响天文摄影图像的质量。

---

## 24. 显示 HN：Wireshark 的玩具版本（学生项目）

**原文标题**: Show HN: A toy version of Wireshark (student project)

**原文链接**: [https://github.com/lixiasky/vanta](https://github.com/lixiasky/vanta)

Vanta：一个轻量级命令行网络行为分析器，由本科生lixiasky用Go编写，作为Wireshark的“玩具版本”以及对支持国际学生的大学的个人致谢。它侧重于清晰性、结构和简洁性，使其适用于自定义脚本和最简设置。

Vanta支持HTTP、DNS和TLS协议，重构双向流，并输出简洁的JSON格式摘要。它是一个没有外部依赖的单文件二进制程序。Vanta在MacBook Air M1上开发和测试，其项目结构包括数据包捕获和流重组、协议解码、模糊测试和行为导出等模块。文档位于`usage/`文件夹中，并以中文编写。

作者承认Vanta与Wireshark相比存在局限性，并表示尽管存在不足，但它是一个用心制作的项目。作者欢迎通过电子邮件(lixiasky@protonmail.com)或GitHub(github.com/lixiasky)提供反馈和贡献。

---

## 25. 乌克兰自主杀手机器人击败电子战

**原文标题**: Ukraine's autonomous killer drones defeat electronic warfare

**原文链接**: [https://spectrum.ieee.org/ukraine-killer-drones](https://spectrum.ieee.org/ukraine-killer-drones)

乌克兰利用自主杀伤无人机克服俄罗斯电子战战术

---

## 26. 元提示完全指南

**原文标题**: A Complete Guide to Meta Prompting

**原文链接**: [https://www.prompthub.us/blog/a-complete-guide-to-meta-prompting](https://www.prompthub.us/blog/a-complete-guide-to-meta-prompting)

本文概述了元提示（meta prompting），一种提示工程方法，其中使用大型语言模型（LLM）来创建和改进提示。其核心思想是在提示创建过程中利用 LLM，类似于使用它们来撰写博客文章。

讨论了几种元提示方法：

*   **斯坦福和 OpenAI 的元提示：** 使用“指挥者”LLM 来控制和综合来自多个“专家”LLM 的输出。
*   **从对比提示中学习：** 比较带有正面和负面示例的提示的输出，以了解哪些提示差异导致了这些结果，并基于比较结果生成新的提示。
*   **自动提示工程师：** 基于演示生成多个提示候选方案，评估其输出，并根据性能改进提示。
*   **提示代理：** 通过在树状结构中使用领域特定知识迭代改进提示，来捕获主题专业知识。
*   **会话提示工程 (CPE)：** 模拟用户与 LLM 之间的对话，讨论任务、期望的输出和潜在的陷阱，最终生成改进的提示。
*   **DSpy：** 一个开源 Python 存储库，用于创建管道，以使用评分机制改进提示。
*   **Text GRAD：** 使用自然语言反馈（“文本梯度”）来改进提示，而不是仅仅依赖于定量评分。

文章最后提到了辅助元提示的工具，包括 PromptHub 的 Prompt Generator、Anthropic 的 Prompt Generator 和 OpenAI 的 System Instruction Generator。

---

## 27. Conformance checking at MongoDB: Testing that our code matches our TLA+ specs

**原文标题**: Conformance checking at MongoDB: Testing that our code matches our TLA+ specs

**原文链接**: [https://www.mongodb.com/blog/post/engineering/conformance-checking-at-mongodb-testing-our-code-matches-our-tla-specs](https://www.mongodb.com/blog/post/engineering/conformance-checking-at-mongodb-testing-our-code-matches-our-tla-specs)

生成摘要时出错

---

## 28. MonsterUI: Python library for building front end UIs quickly in FastHTML apps

**原文标题**: MonsterUI: Python library for building front end UIs quickly in FastHTML apps

**原文链接**: [https://www.answer.ai/posts/2025-01-15-monsterui.html](https://www.answer.ai/posts/2025-01-15-monsterui.html)

MonsterUI is a Python library designed to simplify front-end UI development in FastHTML applications. It addresses the complexity and boilerplate associated with styling web UIs using CSS frameworks like Bootstrap or Tailwind CSS. MonsterUI provides pre-styled components and smart defaults based on modern libraries like Tailwind, FrankenUI, and DaisyUI, all while allowing full access to Tailwind CSS when needed.

Key features include:

*   **Theme Support:** Offers 12 color themes with dark and light modes, ensuring consistent styling across components.
*   **Base Components:** Provides styled HTML elements like buttons with hover states, focus rings, and consistent padding.
*   **Semantic Text Styles:** Styles semantic HTML tags based on the HTML specification for consistency.
*   **Smart Layout Helpers:** Simplifies page layout with helpers like `DivVStacked` and `Grid`.
*   **Common UI Patterns:** Includes shortcuts for common patterns, like the `LabelInput` component.
*   **Higher Level Components:** Offers helpers for complex components like navbars, modals, cards, and tables, simplifying their creation and ensuring good UX.
*   **Markdown Rendering:** Includes a `render_md` function to convert Markdown to styled HTML with syntax highlighting.

MonsterUI aims to reduce context-switching between HTML, CSS, and Python, allowing developers to focus on building features instead of managing styling details. Installation is simple via pip, and the library integrates seamlessly with FastHTML.


---

## 29. 视觉语言模型存在偏见

**原文标题**: Vision Language Models Are Biased

**原文链接**: [https://vlmsarebiased.github.io/](https://vlmsarebiased.github.io/)

生成摘要时出错

---

## 30. 亚马逊Dafny教学程序验证 (2023)

**原文标题**: Teaching Program Verification in Dafny at Amazon (2023)

**原文链接**: [https://dafny.org/blog/2023/12/15/teaching-program-verification-in-dafny-at-amazon/](https://dafny.org/blog/2023/12/15/teaching-program-verification-in-dafny-at-amazon/)

本文介绍了一个在亚马逊开发和教授的使用Dafny的程序验证课程。与将规范和证明直接集成到程序中的传统方法不同，本课程将Dafny作为一种独立于其编程语言角色的证明助手来介绍。课程分为三个部分。

第一部分侧重于Dafny作为一种编程语言，使学生熟悉其语法、语义和工具，而不涉及验证。第二部分转向Dafny作为一种证明助手，涵盖规范语言，定义类型和函数，并探索证明技巧。本部分强调使用自然演绎进行直观的“解释性证明”和严格的“说服性证明”。第三部分整合了编程和验证，从函数式程序（外在和内在验证）开始，逐步过渡到命令式和面向对象程序。该课程提倡最初采用外在验证，以提高证明的鲁棒性，并强调诸如用于命令式程序的功能建模以及用于面向对象程序的带有适当幽灵表示的谨慎 API 设计等技术。

本课程旨在为传统的程序验证方法提供一种补充视角，特别是在解决Dafny自动化不足时所面临的挑战。它使学习者能够编写详细、正式的证明，从而即使在复杂的场景中也能令人信服地验证程序的正确性。该课程最初旨在补充“程序证明”，现已发展成为对程序验证的全面介绍以及专家的高级培训工具。

---

## 31. ThorVG: 超轻量级矢量图形引擎

**原文标题**: ThorVG: Super Lightweight Vector Graphics Engine

**原文链接**: [https://www.thorvg.org/about](https://www.thorvg.org/about)

ThorVG is an open-source, lightweight vector graphics engine designed for creating scenes and animations. It prioritizes efficiency and ease of use, supporting various primitives like lines, shapes, fills, strokes, text, images (SVG, JPG, PNG, etc.), effects (blur, shadow, tint), and Lottie animations.

It supports multiple platforms including Linux, macOS, Windows, Tizen, iOS, Android, Web, Flutter, and more. ThorVG utilizes a modular design, allowing for selective builds and optimal size. It supports several render backends: CPU/SIMD, OpenGL/ES, WebGL, and WebGPU, ensuring adaptability across systems.

Threading is incorporated for efficient scene processing using a task scheduler with thread pools. SVG rendering is facilitated through a dedicated interpreter adhering to the SVG Tiny Specification. Lottie animation support is a key feature, with ThorVG powering Lottie animations in various applications.

The ThorVG viewer is a resource verification tool that allows real-time editing within a web browser, protecting resource copyright. The engine is used in practice by applications like Canva (iOS), dotLottie player by LottieFiles, Flux Audio, Godot, Lottie Creator, LVGL and Tizen. The project is driven by contributors and supported by sponsors, and encourages further financial support to enhance its continued development.


---

## 32. Magic Ink: Information Software and the Graphical Interface

**原文标题**: Magic Ink: Information Software and the Graphical Interface

**原文链接**: [https://worrydream.com/MagicInk/](https://worrydream.com/MagicInk/)

生成摘要时出错

---

## 33. Show HN: 我每月做一个荒诞的网页项目

**原文标题**: Show HN: I build one absurd web project every month

**原文链接**: [https://absurd.website](https://absurd.website)

ABSURD.website is a project showcasing a new, intentionally absurd product or service each month. The creator describes it as "art." Recent projects include:

*   **Add Luck to Your e-Store:** A waving cat graphic for eCommerce sites, aiming to increase sales through "marketing now."
*   **Microtasks for Meatbags:** Renting out human "souls" to AI.
*   **OPERATION D-DAY: ONE SECOND OF WAR:** A first-person shooter game where every second is crucial.
*   **LingoPrio:** Claiming to quickly teach 5 languages by focusing on pre-existing knowledge.
*   **Artist's Death Effect Database:** Tracking the surge in value of an artist's work after their death.
*   **Sexy Math:** Making learning math sexy.
*   **ChillyParent:** One-click parenting service.
*   **Easy Pet Drop Box:** A place to drop off your pets.
*   **Influencer Overnight:** Promising to turn a follower into an influencer with 100k followers.
*   **Stealing From Dreams:** Recreating artwork based on user descriptions.
*   **A Guide For Aliens To Live On Earth:** A tourist-style guidebook for extraterrestrial visitors.
*   **Puzzle Solvers Agency:** A service that solves puzzles and games for customers.

Other absurd concepts range from toilet water perfume and invisible lingerie to a slow delivery service and offsetting CO2 emissions by buying the creator a Tesla. The website also includes projects like a dating site for eyes, a '90s-inspired web design studio, and a "Buy Nothing Store."

Visitors can subscribe to a mailing list for monthly updates on new absurd projects.


---

## 34. 规模最大的朋克音乐档案将落户中田纳西州立大学流行音乐中心

**原文标题**: Largest punk archive to find new home at MTSU's Center for Popular Music

**原文链接**: [https://mtsunews.com/worlds-largest-punk-archive-moves-to-center-for-popular-music/](https://mtsunews.com/worlds-largest-punk-archive-moves-to-center-for-popular-music/)

中田纳西州立大学流行音乐中心将获得Maximum Rocknroll档案，成为世界领先的朋克研究中心。该档案是现存最大的朋克收藏，包含约6万张黑胶唱片、照片、杂志和文献，将从加利福尼亚州迁至田纳西州墨菲斯堡。

---

## 35. 文德尔施泰因7-X创下新的聚变记录

**原文标题**: Wendelstein 7-X sets new fusion record

**原文链接**: [https://www.heise.de/en/news/Wendelstein-7-X-sets-new-fusion-record-10422955.html](https://www.heise.de/en/news/Wendelstein-7-X-sets-new-fusion-record-10422955.html)

**概要：**

德国格赖夫斯瓦尔德的Wendelstein 7-X (W7-X) 仿星器聚变装置在仿星器型聚变反应堆中实现了新的能量约束时间记录。 在其最新的实验活动中，W7-X 成功地将等离子体温度维持在 1.3 亿摄氏度，持续了令人印象深刻的 8 分钟，同时实现了约 10^20 个粒子/立方米的等离子体密度。

这超过了其之前的记录，表明该机器的性能得到了改善，并验证了仿星器设计作为聚变能源可行方法。 这一成功的关键在于优化的加热系统和先进的等离子体控制技术。

更长的能量约束时间是证明仿星器适用于持续聚变反应的关键一步。 虽然仍然是一个研究设施，但 W7-X 的进展意义重大，因为与托卡马克设计（另一种主要的聚变反应堆类型）相比，仿星器设计本身在稳态运行方面具有优势。 具体而言，仿星器旨在在不需要外部电流驱动的情况下以稳态运行，这对于商业上可行的聚变发电厂至关重要。

研究人员正在继续完善 W7-X 的技术，重点是进一步提高等离子体密度和约束时间，为未来的聚变发电厂铺平道路。 来自 W7-X 的结果提供了关键数据和见解，将有助于全球聚变研究工作。

---

## 36. Uber's new shuttles look suspiciously familiar to anyone who's taken a bus

**原文标题**: Uber's new shuttles look suspiciously familiar to anyone who's taken a bus

**原文链接**: [https://grist.org/transportation/uber-shared-route-buses/](https://grist.org/transportation/uber-shared-route-buses/)

Uber's new "Route Share" shuttle service, which utilizes fixed routes and stops, is drawing criticism for essentially reinventing the bus without addressing the inherent problems of ride-sharing services. The article argues that this "next-gen bus" might be a worse alternative to public transit, despite Uber's claims of affordability and reduced congestion.

Critics point out that ride-sharing services, including pooled options, still contribute significantly to carbon emissions due to "deadheading" miles. Furthermore, Uber's service poses a threat to already struggling public transit systems in cities like Philadelphia and Dallas, which face defunding and service cuts. The article questions Uber's claim of complementing public transport, citing a study that found ride-hailing often replaces more sustainable options like walking, cycling, and public transit.

The article highlights that Uber's Route Share might worsen congestion in cities like New York, as it adds more vehicles to crowded streets. An example is given where a subway provides a faster and cheaper alternative to the proposed Uber route. Ultimately, the article suggests that Uber's new service could decrease transit efficiency by adding more vehicles to existing routes, all while lacking the public accountability of established transit agencies.


---

## 37. Builder.ai崩盘：15亿美元“人工智能”初创公司被揭露为“印度人”

**原文标题**: Builder.ai Collapses: $1.5B 'AI' Startup Exposed as 'Indians'

**原文链接**: [https://www.ibtimes.co.uk/builderai-collapses-15bn-ai-startup-exposed-actually-indians-pretending-bots-1734784](https://www.ibtimes.co.uk/builderai-collapses-15bn-ai-startup-exposed-actually-indians-pretending-bots-1734784)

生成摘要时出错

---

## 38. 非法加密货币矿工利用疏忽的DevOps配置，导致云环境变得脆弱

**原文标题**: Illicit crypto-miners pouncing on lazy DevOps configs leaving clouds vulnerable

**原文链接**: [https://www.theregister.com/2025/06/03/illicit_miners_hashicorp_tools/](https://www.theregister.com/2025/06/03/illicit_miners_hashicorp_tools/)

一项名为JINX-0132的新型加密货币挖矿活动，通过配置错误的DevOps工具，瞄准脆弱的云环境，可能影响高达25%的云用户。Wiz Threat Research识别了该活动，强调了5%的云环境将这些DevOps工具暴露于互联网，而其中30%配置错误。

JINX-0132利用HashiCorp的Nomad和Consul、Docker Engine API以及Gitea中的漏洞，来部署XMRig挖矿软件。Nomad的默认设置缺乏安全性，允许未经授权的作业创建和执行。同样，全新安装的Consul缺乏访问控制列表，从而实现远程代码执行。将Docker API公开暴露会授予攻击者root级别的访问权限，用于容器创建和文件系统挂载。对于Gitea，攻击者可能利用较旧版本，操纵默认安全设置，或重置管理员凭据以安装挖矿软件。

文章强调了保护这些工具的重要性：在Nomad中启用安全功能（访问控制列表），禁用Consul中的脚本检查并限制HTTP API，避免将Docker API暴露于互联网，并保持Gitea更新并正确配置。否则，云算力资源将容易受到加密劫持和其他恶意活动的影响。

---

## 39. 日本科学家开发出与所有血型兼容的人造血液

**原文标题**: Japanese scientists develop artificial blood compatible with all blood types

**原文链接**: [https://www.tokyoweekender.com/entertainment/tech-trends/japanese-scientists-develop-artificial-blood/](https://www.tokyoweekender.com/entertainment/tech-trends/japanese-scientists-develop-artificial-blood/)

日本奈良医科大学的酒井宏水领导的科学家团队研发出与所有血型相容的人造血液。 这项创新旨在解决维持充足血液供应的挑战，尤其是在中低收入国家，对通用供血者O型阴性血液的需求常常超过供应。

这种人造血液是通过从过期捐献血液中提取血红蛋白并将其包裹在保护壳中制成的。 这个过程创造了稳定的、无病毒的人造红细胞，消除了血型相容性测试的需要。 一个主要的优势是其更长的保质期：在室温下长达两年，冷藏则长达五年，明显长于捐献红细胞的42天限制。

2022年开始了小规模的人体试验，健康的男性志愿者接受了人造血液的静脉注射。 初步结果显示有轻微的副作用，生命体征没有明显变化。 在此成功之后，该团队于三月份开始施用更大的剂量，旨在测试其有效性和安全性，希望在2030年左右使其能够实际应用。

中央大学的小松辉幸教授也在开发使用白蛋白包裹血红蛋白的人造氧气载体，该载体在动物研究中显示出稳定血压以及治疗出血和中风等疾病的潜力，为人体试验铺平了道路。

---

## 40. Younger generations less likely to have dementia, study suggests

**原文标题**: Younger generations less likely to have dementia, study suggests

**原文链接**: [https://www.theguardian.com/society/2025/jun/02/younger-generations-less-likely-dementia-study](https://www.theguardian.com/society/2025/jun/02/younger-generations-less-likely-dementia-study)

生成摘要时出错

---

## 41. 无人问津时如何发帖

**原文标题**: How to post when no one is reading

**原文链接**: [https://www.jeetmehta.com/posts/thrive-in-obscurity](https://www.jeetmehta.com/posts/thrive-in-obscurity)

当无人问津时如何创作内容：专注于创作本身的乐趣

本文探讨了在感觉无人关注时创作内容的常见困境。它承认了大多数成功创作者所经历的多年“默默无闻”的努力，并强调立即成名和获得赞扬是不切实际的期望，可能会导致倦怠。 关键在于优先考虑创作本身的乐趣，而不是仅仅关注外部认可。

作者提出了几个框架来维持这段默默无闻时期的动力：

1.  **“做你喜欢的事，有时世界会认可。”** 受 Mike Posner 经历的启发，这强调了创作真正让你兴奋的内容，因为这种内在动力将更具有可持续性。

2.  **“展现自我。”** 创作你喜欢的东西。 这个原则表明，与其试图确定你的观众喜欢什么，不如仅仅创作你喜欢的东西。 当你拥有这种心态时，你更有可能突破瓶颈。

3.  **“建立你的‘剧集银行’。”** 将初始内容视为对未来粉丝的投资。 这个“剧集银行”是忠实粉丝在你获得受众后会探索的档案，增加了你最早、观看次数最少作品的价值。

文章最后鼓励大家继续创作，并将缺乏即时受众视为通往成功和影响力的旅程中的一个暂时的阶段。

---

## 42. The rise of judgement over technical skill

**原文标题**: The rise of judgement over technical skill

**原文链接**: [https://notsocommonthoughts.com/blog/ai-and-judgement/](https://notsocommonthoughts.com/blog/ai-and-judgement/)

生成摘要时出错

---

## 43. 不应有电脑艺术（1971）

**原文标题**: There should be no Computer Art (1971)

**原文链接**: [https://dam.org/museum/essays_ui/essays/there-should-be-no-computer-art/](https://dam.org/museum/essays_ui/essays/there-should-be-no-computer-art/)

生成摘要时出错

---

## 44. The Creepy, Surprisingly Routine Business of Animal Cloning

**原文标题**: The Creepy, Surprisingly Routine Business of Animal Cloning

**原文链接**: [https://www.theatlantic.com/magazine/archive/2025/07/animal-cloning-industry/682892/](https://www.theatlantic.com/magazine/archive/2025/07/animal-cloning-industry/682892/)

生成摘要时出错

---

## 45. Show HN: Penny-1.7B Irish Penny Journal style transfer

**原文标题**: Show HN: Penny-1.7B Irish Penny Journal style transfer

**原文链接**: [https://huggingface.co/dleemiller/Penny-1.7B](https://huggingface.co/dleemiller/Penny-1.7B)

生成摘要时出错

---

## 46. 展示一下：Onlook – 面向设计师的开源、可视化光标

**原文标题**: Show HN: Onlook – Open-source, visual-first Cursor for designers

**原文链接**: [https://github.com/onlook-dev/onlook](https://github.com/onlook-dev/onlook)

Onlook：一款面向设计师和开发者的开源、可视化代码编辑器，用于使用 Next.js 和 TailwindCSS 创建网站和原型。它提供了一个可视化界面，可以直接在浏览器的 DOM 中编辑代码，从而提供实时的设计和编码体验。它被定位为 Bolt.new 和 Webflow 等工具的替代品。

Onlook 的 Web 版本目前正在开发中，并积极寻求贡献者。其功能包括：从文本、图像、预构建模板、Figma 导入或 GitHub 存储库创建 Next.js 应用程序；使用类似 Figma 的 UI 可视化编辑应用程序；实时预览；以及管理品牌资产和令牌。它还提供开发工具，例如实时代码编辑器、检查点、CLI 命令、应用程序市场和本地代码编辑。部署功能包括可共享链接、自定义域名和团队协作工具。

桌面版本“Onlook Desktop”适用于寻求可下载 Electron 应用程序的用户，但重点已转移到基于 Web 的版本。Onlook 的工作原理是将代码加载到 Web 容器中，在 iframe 中显示预览，并检测代码以将元素映射到其相应的代码位置。编辑会同时反映在 iframe 和代码中。该项目使用 Next.js、Supabase 和 TailwindCSS 等技术构建，并欢迎通过 fork 和 pull request 进行贡献。文档和贡献指南可在 Onlook 网站上找到。

---

## 47. 以每分钟118字的速度打字，彻底重塑了我的思维。

**原文标题**: Typing 118 WPM broke my brain in the right ways

**原文链接**: [http://balaji-amg.surge.sh/blog/typing-118-wpm-brain-rewiring](http://balaji-amg.surge.sh/blog/typing-118-wpm-brain-rewiring)

本文详细介绍了作者历时一年达到每分钟118个单词的打字速度的历程，以及它如何意外地提高了作者作为开发者的思维清晰度和工作效率。作者最初的打字速度为每分钟60个单词，并对编写代码时缓慢的打字速度感到沮丧，于是开始每天进行5分钟的打字练习，以重置大脑并提高注意力。

他们强调准确性是关键，认为放慢速度以确保正确的击键最终会带来更快的速度。作者还提倡找到一种适合自己的打字风格，即使它偏离了传统的“正确”姿势。他们将自己的风格描述为“无政府主义打字”，优先考虑效率而非僵化的技术。

文章将打字视为管理精神疲劳和压力的工具。作者将打字练习用作大脑休息、情绪助推器和克服思维障碍的方式。他们注意到不可避免的挫折和速度较慢的时期，并将它们视为通往进一步改进的学习机会。

最终，作者认为掌握打字提高了他们的专注力、自律性和“Just do the thing（只管去做）”的整体能力。他们强调了切实的好处，例如更快的编码速度、更好的文档编写以及减少了重复打字任务带来的挫败感，并得出结论，这个看似微不足道的习惯显著提高了他们的开发技能和认知功能。

---

## 48. 武士杰克的视觉世界

**原文标题**: The Visual World of 'Samurai Jack'

**原文链接**: [https://animationobsessive.substack.com/p/the-visual-world-of-samurai-jack](https://animationobsessive.substack.com/p/the-visual-world-of-samurai-jack)

生成摘要时出错

---

## 49. 有用不代表有价值

**原文标题**: If you are useful, it doesn't mean you are valued

**原文链接**: [https://betterthanrandom.substack.com/p/if-you-are-useful-it-doesnt-mean](https://betterthanrandom.substack.com/p/if-you-are-useful-it-doesnt-mean)

Unable to access the article link.


---

## 50. Mario Kart designers had to rethink everything to make it open world

**原文标题**: Mario Kart designers had to rethink everything to make it open world

**原文链接**: [https://www.theverge.com/interview/678097/mario-kart-world-nintendo-switch-2-interview-kosuke-yabuki](https://www.theverge.com/interview/678097/mario-kart-world-nintendo-switch-2-interview-kosuke-yabuki)

生成摘要时出错

---

## 51. Is “The Phoenician Scheme” Wes Anderson's Most Emotional Film?

**原文标题**: Is “The Phoenician Scheme” Wes Anderson's Most Emotional Film?

**原文链接**: [https://www.newyorker.com/magazine/2025/06/09/the-phoenician-scheme-movie-review](https://www.newyorker.com/magazine/2025/06/09/the-phoenician-scheme-movie-review)

生成摘要时出错

---

## 52. EasyTier – 使用 Tokio 以 Rust 编写的 P2P 网状 VPN

**原文标题**: EasyTier – P2P mesh VPN written in Rust using Tokio

**原文链接**: [https://easytier.cn/en/](https://easytier.cn/en/)

生成摘要时出错

---

## 53. HeidiSQL 也可在 Linux 上使用

**原文标题**: HeidiSQL Available Also for Linux

**原文链接**: [https://www.heidisql.com/forum.php?t=44068](https://www.heidisql.com/forum.php?t=44068)

HeidiSQL 12.10.1.133 Linux 预发布版发布公告。这是首个带有标签的 Linux 版本，可从 HeidiSQL 网站下载。主要功能包括 SSH 隧道支持（使用外部 ssh 命令）、35 种语言的翻译支持、状态栏图标、SQL 编辑器中的括号高亮显示、可用的网格单元格编辑器、自动标签页恢复以及功能完善的表/视图/例程/触发器/事件编辑器。

已知问题包括缺少对 MS SQL 和 Interbase/Firebird 的支持、网格单元格编辑器中的崩溃、缺少 .rpm 包以及 SQL 编辑器中没有自动换行。

用户正在讨论新的 Linux 构建版本，一些用户分享了在使用 AUR 包的基于 Arch 的发行版上的经验。 讨论正在进行关于创建 .rpm 包和 Flatpak 以实现更广泛的发行支持，并建议使用 .tgz 文件作为快速解决方案。 一位用户报告了一个与 libmariadbd.so 库出现在连接库下拉列表中相关的潜在错误。

其他主题包括使用 `/usr/bin/ssh` 或 PuTTY 的 `plink` 的 SSH 隧道功能，以及 Windows 版本中不存在的主题（Linux 版本适应系统的浅色/深色模式）。 用户可以在“首选项”>“SQL”中调整 SQL 编辑器样式，并在 HeidiSQL 错误跟踪器上报告错误。

---

## 54. Arcol 通过浏览器建模简化建筑设计

**原文标题**: Arcol simplifies building design with browser-based modeling

**原文链接**: [https://www.arcol.io/](https://www.arcol.io/)

Arcol提供一个基于浏览器的建筑设计平台，该平台简化了建筑、工程和施工（AEC）团队的协作并提高了效率。通过实现利益相关者之间的实时协作，Arcol旨在消除数据孤岛，减少电子邮件沟通，并促进更好、更快的决策。

该平台拥有复杂几何建模、用于数据驱动决策的实时指标跟踪、自动化文档编制以及数据和文档的无缝集成等功能。Arcol有助于更轻松地沟通设计意图和管理复杂数据，尤其是在可行性阶段。客户评价强调了Arcol对项目质量、效率和客户沟通的积极影响。

Arcol面向包括建筑师、设计师、开发商、总承包商和建筑业主在内的各种角色，提供专门的功能来满足他们的特定需求。这些功能包括消除设计过程中的摩擦的工具，便于开发商进行成本和可行性比较，便于承包商随时访问的成本比较，以及便于业主使用的实时设计和指标演变。该平台旨在通过促进早期和频繁的协作来增强项目势头。

---

## 55. ReasoningGym：基于可验证奖励的RL推理环境

**原文标题**: ReasoningGym: Reasoning Environments for RL with Verifiable Rewards

**原文链接**: [https://arxiv.org/abs/2505.24760](https://arxiv.org/abs/2505.24760)

本文介绍arXiv文章“推理健身房”(RG)，这是一个新的推理环境库，专为具有可验证奖励的强化学习(RL)而设计。 RG提供超过100个数据生成器和验证器，涵盖代数、算术、计算、认知、几何、图论、逻辑和游戏等多个领域。

RG的关键创新在于其程序化生成能力，能够创建几乎无限的、具有可调节复杂性的训练数据。这与现有通常是静态和固定的推理数据集形成对比。动态调整难度等级的能力有助于对推理模型进行持续评估。

作者Zafir Stojanovski等人证明了RG在评估和训练使用RL的推理模型方面的有效性。该库旨在为开发和测试能够执行复杂推理任务的AI代理提供一个强大的平台。

该论文还提供了代码库的链接。这篇文章被归类为机器学习(cs.LG)、人工智能(cs.AI)和计算与语言(cs.CL)。

---

## 56. 信用卡终端上的Root权限

**原文标题**: Root shell on a credit card terminal

**原文链接**: [https://stefan-gloor.ch/yomani-hack](https://stefan-gloor.ch/yomani-hack)

一名安全研究人员对瑞士常见的Worldline Yomani XR信用卡终端的探索，最初预期其安全性很高，但却发现了令人惊讶的漏洞。

拆解终端后，研究人员发现了压敏互连和锯齿形铜线等防篡改保护措施，但还是通过拆焊闪存芯片提取了固件。固件未加密，运行着一个带有过时内核和存在漏洞的软件组件的Linux系统。

令人震惊的是，研究人员发现设备上通过串行控制台可以轻松访问root shell，默认启用且root用户没有密码。这个串行端口可以通过调试连接器从外部访问，从而使攻击者可以在几秒钟内获得root权限，而不会触发篡改检测。

然而，进一步的分析表明，Linux系统并不直接处理敏感的卡片数据。一个独立的“安全”处理器（mp1）管理卡片交易和屏幕显示，而Linux系统（mp2）处理网络和更新。安全处理器从由安全引导加载程序加载的加密签名映像启动，似乎减轻了与root shell相关的风险。

尽管有防篡改保护措施和安全核心，作者仍认为易于访问的root shell是一个重大的疏忽和不必要的攻击面。root shell可用于将恶意软件部署到Linux核心。研究人员向制造商披露了该漏洞，但推迟了发布。虽然root登录可能已在更新的固件版本中修复，但研究人员得出结论，由于敏感数据处理的分离，暴露的root shell并没有最初担心的那么大的风险。

---

## 57. What works (and doesn't) selling formal methods

**原文标题**: What works (and doesn't) selling formal methods

**原文链接**: [https://www.galois.com/articles/what-works-and-doesnt-selling-formal-methods](https://www.galois.com/articles/what-works-and-doesnt-selling-formal-methods)

生成摘要时出错

---

## 58. 三峡大坝可能使一天的时间延长0.06微秒

**原文标题**: Three Gorges Dam May Increase the Length of a Day by 0.06 Microseconds

**原文链接**: [https://www.thetravel.com/nasa-three-gorges-dam-china-disrupting-global-timekeeping/](https://www.thetravel.com/nasa-three-gorges-dam-china-disrupting-global-timekeeping/)

本文探讨了美国国家航空航天局(NASA)关于中国三峡大坝对地球自转和计时影响的研究结果。NASA指出，大坝蓄积的约10万亿加仑水量可能导致每天时长增加0.06微秒，这看似微小的变化，但考虑到其影响，意义重大。

本文还探讨了影响地球自转的其他因素，特别强调了气候变化。NASA已将冰川融化、地下水减少和海平面上升与地球自转的变化联系起来。研究表明，自2000年以来，每天时长每100年延长1.33毫秒，这归因于人为温室气体排放导致南极洲和格陵兰冰川融化。

最后，本文展示了网络社区对NASA研究结果的反应。这些反应从幽默到担忧不等，用户提供了各种类比来理解水 displacement 对地球自转的影响，例如将它比作花样滑冰运动员伸展手臂或在环形交叉路口上向外移动。一些用户淡化了其重要性，而另一些用户则对长期后果表示担忧。

---

## 59. CVE-2025-31200

**原文标题**: CVE 2025 31200

**原文链接**: [https://blog.noahhw.dev/posts/cve-2025-31200/](https://blog.noahhw.dev/posts/cve-2025-31200/)

This article details the reverse engineering process of CVE-2025-31200, a memory corruption bug in Apple's CoreAudio, specifically within the `apac::hoa::CodecConfig::Deserialize` function of the AudioCodecs component. The author begins by noting the initial lack of public information on the bug, which was reportedly actively exploited.

The author uses tools like `ipsw` and `radiff2` to diff the patched and unpatched AudioCodecs binaries, identifying significant changes in the `Deserialize` method related to reading data from a bitstream to populate arrays. A key difference was identified: the patched version checks if `elementCount == 0` whereas the unpatched version does not. The bug lies in how the code sizes `outBuf`, which it sizes based on `elementCount`.

The author then outlines the reverse engineering of the audio codec in question. APAC stands for Apple Positional Audio Codec and HOA stands for Higher Order Ambisonics: a method of representing sound as a spatial sound-field centered around the listener's head.

Ultimately, the author hypothesized that the vulnerability stemmed from a sizing mismatch in subsequent buffers based on values from the `m_RemappingArray` (sized incorrectly in the vulnerable version) leading to a memory corruption vulnerability.


---

## 60. The Atomic Airplane

**原文标题**: The Atomic Airplane

**原文链接**: [https://whatisnuclear.com/the-story-of-the-atomic-airplane.html](https://whatisnuclear.com/the-story-of-the-atomic-airplane.html)

生成摘要时出错

---

## 61. 欧盟委员会拒绝透露其大规模监控提案的作者

**原文标题**: EU Commission refuses to disclose authors behind its mass surveillance proposal

**原文链接**: [https://old.reddit.com/r/europe/comments/1l2655n/the_eu_commission_refuses_to_disclose_the/](https://old.reddit.com/r/europe/comments/1l2655n/the_eu_commission_refuses_to_disclose_the/)

无法访问文章链接。

---

## 62. Prepare for archival

**原文标题**: Prepare for archival

**原文链接**: [https://github.com/GoogleContainerTools/kaniko/pull/3502](https://github.com/GoogleContainerTools/kaniko/pull/3502)

This GitHub page documents the archival of the `GoogleContainerTools/kaniko` repository on June 3, 2025. The repository is now read-only. Pull request #3502, titled "Prepare for archival," was merged to accomplish this. The pull request, initiated by `seenkey`, involved updating the README file to include an archive notice, addressing issues #3316 and #3348. `Plumpy` approved the changes before they were merged. The archival commit added the archive notice to the README. The conversation log shows the timeline of the archival process, including the request for review, approval, and final merging. The page also indicates an error occurred while loading, and encourages users to sign up or sign in to GitHub to participate in the conversation.


---

## 63. Writing your own C++ standard library part 2

**原文标题**: Writing your own C++ standard library part 2

**原文链接**: [https://nibblestew.blogspot.com/2025/05/writing-your-own-c-standard-library.html](https://nibblestew.blogspot.com/2025/05/writing-your-own-c-standard-library.html)

生成摘要时出错

---

## 64. out of cash - DOS point and click adventure game

**原文标题**: out of cash - DOS point and click adventure game

**原文链接**: [https://github.com/warrior-rockk/out-of-cash](https://github.com/warrior-rockk/out-of-cash)

生成摘要时出错

---

## 65. 智能代理技术：芝麻开门！（1993）

**原文标题**: Intelligent Agent Technology: Open Sesame! (1993)

**原文链接**: [https://blog.gingerbeardman.com/2025/05/31/intelligent-agent-technology-open-sesame-1993/](https://blog.gingerbeardman.com/2025/05/31/intelligent-agent-technology-open-sesame-1993/)

本文讲述了作者长期寻找一款上世纪90年代初的 Macintosh 应用程序名称的经历，该程序使用机器学习来自动化重复性任务。经过多年无果的 Google 搜索和 Macintosh 爱好者询问后，作者最终使用 AI 服务 Gemini 找到了答案。该应用程序名为“Open Sesame!”，被称为世界上第一款 Macintosh 智能软件助手，它可以学习用户的模式并提供自动化重复操作。

作者回忆起在上世纪 90 年代初到中期观看 Open Sesame! 演示的情景，尽管演示本身存在缺陷。文章强调了在 2025 年使用现代 AI 来发现一款早在 1993 年就围绕机器学习原则构建的应用程序的讽刺意味。

文章提供了 Macintosh Garden 上 Open Sesame! 1.1 的下载链接，并提供了一个“延伸阅读”列表，其中包括 1993-1996 年的几篇 MacWorld 出版物，提供了有关该应用程序的评论、广告和新闻。还提到了 1996 年 NASA 的一篇关于“智能代理技术”的衍生出版物。

---

## 66. Cuss: Map of profane words to a rating of sureness

**原文标题**: Cuss: Map of profane words to a rating of sureness

**原文链接**: [https://github.com/words/cuss](https://github.com/words/cuss)

`cuss` 是一个仅支持 ESM 的 JavaScript 包，它提供多种语言的脏话词汇列表，每个词汇都关联一个从 0 到 2 的 “确定性” 评分。该评分表示一个词语被用作脏话的可能性，而非其粗俗程度。 此包旨在用于自然语言研究，*而非* 用于构建不鼓励使用的脏话过滤器。

该包通过 npm (Node.js) 安装，或直接通过 Deno 或浏览器中的 ESM 导入。它为每种支持的语言（英语、阿拉伯语（拉丁字母）、西班牙语、法语、意大利语、葡萄牙语和欧洲葡萄牙语）导出一个 `cuss` 对象，其中包含单词及其确定性评级的记录。

数据来源因语言而异，包括 Luis von Ahn 的研究小组、Wikipedia 和其他在线资源等来源。该包完全使用 TypeScript 进行类型化，并与维护的 Node.js 版本（14.14+、16.0+）、Deno 和现代浏览器兼容。

该文档还重点介绍了相关包（buzzwords, fillers, hedges 等），并鼓励贡献，提供添加新术语或语言的指南，并强调在进行更改后需要运行测试。 `cuss` 在 MIT 许可下发布。

---

## 67. 使用 -Zno-embed-metadata 减少 Cargo 目标目录大小

**原文标题**: Reducing Cargo target directory size with -Zno-embed-metadata

**原文链接**: [https://kobzol.github.io/rust/rustc/2025/06/02/reduce-cargo-target-dir-size-with-z-no-embed-metadata.html](https://kobzol.github.io/rust/rustc/2025/06/02/reduce-cargo-target-dir-size-with-z-no-embed-metadata.html)

This article discusses a new method for reducing the size of the Rust Cargo target directory using the unstable compiler flag `-Zno-embed-metadata`. The author addresses the common complaint about the target directory's disk usage, highlighting that metadata duplication contributes to the bloat.

Normally, when compiling Rust library crates, the compiler generates both metadata (in `.rmeta` files) and object code (in `.rlib` files), with the `.rlib` file containing both. Cargo uses pipelining, leveraging metadata to start compiling dependent crates before object code is fully generated, leading to two copies of metadata on disk.

The `-Zno-embed-metadata` flag, inspired by Bjorn3's idea, eliminates metadata duplication by only including a minimal "metadata stub" in the `.rlib` file, keeping the full metadata in the `.rmeta` file. The author implemented this flag in the compiler and its support in Cargo, exposing it via the `-Zno-embed-metadata` Cargo flag.

Benchmarks using hyperqueue show substantial reductions in target directory size, especially in release mode and without debuginfo or incremental compilation (reductions ranging from 9.5% to 36.3%). While it didn't significantly speed up compile times, the flag notably reduces the size of the standard library `.so` file.

The author proposes making `-Zno-embed-metadata` the default behavior in Cargo, potentially after a period of testing in the nightly toolchain. Feedback from real-world usage is encouraged.


---

## 68. Show HN: Page Magic：用AI定制任何网页

**原文标题**: Show HN: Page Magic: Use AI to customize any web page

**原文链接**: [https://github.com/khaledh/pagemagic](https://github.com/khaledh/pagemagic)

生成摘要时出错

---

## 69. 网格边缘构建

**原文标题**: Mesh Edge Construction

**原文链接**: [https://maxliani.wordpress.com/2025/03/01/mesh-edge-construction/](https://maxliani.wordpress.com/2025/03/01/mesh-edge-construction/)

本文探讨了高效计算多边形网格唯一边的算法，这是3D图形学中的一项基本任务。文章首先定义了网格表示方法，重点介绍了面-顶点网格格式，并区分了“边”和“半边”。半边是从网格拓扑（缠绕顺序）直接导出的有序索引对，而边则代表一个唯一的线段，与方向无关。

核心问题是从原始索引数据中识别和枚举这些唯一边。文章介绍了三种算法，每一种都是对前一种的优化，但都产生相同的结果：

1.  **映射方法：** 使用 `std::map`（或使用 `std::unordered_map` 进行优化）来存储遇到的边，确保只保留每个唯一边的第一个实例。虽然概念上很简单，但map插入的频繁内存分配导致更高的执行成本（O(n log n)复杂度）。

2.  **扁平向量 + 排序：** 这种方法通过预分配一个包含所有潜在边（包括重复项）并与其初始索引配对的扁平向量来提高效率。 然后，它使用 `std::stable_sort` 对重复项进行分组，同时保留其原始顺序，然后使用 `std::unique` 删除重复项。 基于初始索引的最终排序恢复了所需的边枚举顺序。 该方法减少了内存分配开销，提高了性能（但仍然是O(n log n)复杂度），但代价是更大的内存占用。

文章强调了按其排序的索引对对边进行排序以识别重复项的重要性，以及稳定排序在维持原始遇到顺序方面的优势。

---

## 70. TradeExpert, a trading framework that employs Mixture of Expert LLMs

**原文标题**: TradeExpert, a trading framework that employs Mixture of Expert LLMs

**原文链接**: [https://arxiv.org/abs/2411.00782](https://arxiv.org/abs/2411.00782)

生成摘要时出错

---

## 71. Snowflake to buy Crunchy Data for $250M

**原文标题**: Snowflake to buy Crunchy Data for $250M

**原文链接**: [https://www.wsj.com/articles/snowflake-to-buy-crunchy-data-for-250-million-233543ab](https://www.wsj.com/articles/snowflake-to-buy-crunchy-data-for-250-million-233543ab)

Unable to access the article link.


---

## 72. Greenland's mega tsunamis: direct observation of trapped waves that shook world

**原文标题**: Greenland's mega tsunamis: direct observation of trapped waves that shook world

**原文链接**: [https://phys.org/news/2025-06-greenland-mega-tsunamis-shook-world.html](https://phys.org/news/2025-06-greenland-mega-tsunamis-shook-world.html)

生成摘要时出错

---

## 73. LFSR CPU Running Forth

**原文标题**: LFSR CPU Running Forth

**原文链接**: [https://github.com/howerj/lfsr-vhdl](https://github.com/howerj/lfsr-vhdl)

生成摘要时出错

---

## 74. Show HN: 我做了一个AI，可以将直播讲座转化为结构化笔记、思维导图和PDF

**原文标题**: Show HN: I made an AI that turn live lecture into structured notes,mind-maps,PDF

**原文链接**: [https://www.notorium.app](https://www.notorium.app)

生成摘要时出错

---

## 75. 克劳德代码是我的电脑

**原文标题**: Claude Code Is My Computer

**原文链接**: [https://steipete.me/posts/2025/claude-code-is-my-computer](https://steipete.me/posts/2025/claude-code-is-my-computer)

本文详细介绍了作者（steipete）在macOS上使用Claude Code（Anthropic的命令行工具）“危险地跳过权限”模式的经验，有效地赋予了其对系统的无限制访问权限。尽管存在内在风险，但他们已成功使用了两个月而未发生任何事故，并认为它显著提高了他们的生产力。

作者认为，Claude Code不仅仅是一个更聪明的命令行工具，而是一个通过文本操作的通用计算机界面。他们将其用于各种任务，包括迁移系统、交付和自动化内容、提取功能、生成测试数据、管理Git工作流程、清理操作系统和设置新机器。该工具理解上下文和意图、根据结果迭代以及直接执行命令的能力是其有效性的关键。

他们将Claude Code与Warp等工具进行了对比，Warp需要对每个命令进行单独批准，这会阻碍对话流程。作者认为，Claude Code代表着一种向AI原生开发的转变，在这种开发模式下，开发人员充当强大系统的编排者，而不仅仅是命令的输入者。他们建议尝试一下，前提是用适当的备份来管理风险，并强调了采用的便捷性和显著的生产力提升。本质上，他们已经把他们的计算机变成了一个能力超强的助手，名叫Claude。

---

## 76. Show HN: MBCompass – Android Compass App

**原文标题**: Show HN: MBCompass – Android Compass App

**原文链接**: [https://github.com/MubarakNative/MBCompass](https://github.com/MubarakNative/MBCompass)

生成摘要时出错

---

## 77. Show HN：C、Lua、Awk、JavaScript等语言的月相算法

**原文标题**: Show HN: Moon Phase Algorithms for C, Lua, Awk, JavaScript, etc.

**原文链接**: [https://github.com/oliverkwebb/moonphase](https://github.com/oliverkwebb/moonphase)

生成摘要时出错

---

## 78. Ubicloud: Open-Source Alternative to AWS

**原文标题**: Ubicloud: Open-Source Alternative to AWS

**原文链接**: [https://github.com/ubicloud/ubicloud](https://github.com/ubicloud/ubicloud)

Ubicloud is presented as an open-source alternative to major cloud providers like AWS, offering IaaS features on bare metal providers such as Hetzner, Leaseweb, and AWS Bare Metal. It can be used as a managed service directly through Ubicloud's console or by building your own cloud by setting up the control plane and connecting to a cloud console. Building your own cloud involves cloudifying bare metal Linux machines leased from providers.

Ubicloud aims to offer cost savings, increased control, and openness compared to proprietary cloud solutions. While AWS offers a vast array of services, Ubicloud focuses on implementing the core 20% of services that account for 80% of usage. Current use cases include ephemeral workloads like CI/CD pipelines and compute-heavy tests. It is also positioned as a portable app deployment service and a solution for building your own cloud on existing bare metal infrastructure.

The architecture involves a control plane managing a data plane, leveraging open-source software. Components include Elastic Compute (using Cloud Hypervisor), Networking (IPsec tunneling, dual-stack IPv4/IPv6, nftables firewalls/load balancers), Block Storage (SPDK), and Attribute-Based Access Control (ABAC). Planned future developments include managed K8s and metrics/monitoring.

The founding team has experience from Azure, Amazon, and Heroku, including involvement with Citus Data. Key differences from OpenStack include being available as a managed service, targeting developers for rapid feedback, and a simpler, more opinionated design.


---

## 79. 一个隐藏的弱点

**原文标题**: A Hidden Weakness

**原文链接**: [https://serge-sans-paille.github.io/pythran-stories/a-hidden-weakness.html](https://serge-sans-paille.github.io/pythran-stories/a-hidden-weakness.html)

生成摘要时出错

---

## 80. Can I stop drone delivery companies flying over my property?

**原文标题**: Can I stop drone delivery companies flying over my property?

**原文链接**: [https://www.rte.ie/brainstorm/2025/0602/1481005-drone-delivery-companies-property-legal-rights-airspace/](https://www.rte.ie/brainstorm/2025/0602/1481005-drone-delivery-companies-property-legal-rights-airspace/)

生成摘要时出错

---

## 81. 我做了一把椅子。

**原文标题**: I made a chair

**原文链接**: [https://milofultz.com/2025-05-27-i-made-a-chair.html](https://milofultz.com/2025-05-27-i-made-a-chair.html)

作者根据Instructables的指南，仅使用一根8英尺长的2"x12"木材并进行简单的切割，制作了一把简易椅子。 尽管只有圆锯和多功能振荡工具（并非该任务的理想工具），该项目还是很快完成了。 作者最后涂抹了端切密封剂来保护木材，并对成品表示满意，甚至比他其他的椅子更喜欢它。

---

## 82. 新型自适应光学技术揭示太阳大气层细节

**原文标题**: New adaptive optics shows details of our star's atmosphere

**原文链接**: [https://nso.edu/press-release/new-adaptive-optics-shows-stunning-details-of-our-stars-atmosphere/](https://nso.edu/press-release/new-adaptive-optics-shows-stunning-details-of-our-stars-atmosphere/)

美国国家科学基金会国家太阳天文台和新泽西理工学院的科学家利用一种名为Cona的新型“日冕自适应光学”系统，迄今为止已产生了最清晰的太阳日冕图像。Cona安装在熊湖太阳天文台的古德太阳望远镜上，可补偿大气湍流，从而以前所未有的分辨率观测日冕特征。

这项新技术使科学家们能够以前所未有的细节观察和创建太阳耀斑、等离子体流（被称为“等离子团”）和日冕雨的视频。具体来说，研究人员拍摄了太阳耀斑内部湍流、等离子体流的形成和崩溃，以及宽度小于20公里的日冕雨丝的运动的电影。

分辨率的提高达到了古德太阳望远镜63公里处的理论极限，有助于更深入地了解日冕加热、太阳爆发和空间天气。科学家们认为，解决小尺度上较冷等离子体的结构和动力学是解开日冕加热之谜的关键。该技术有潜力提高我们对太阳活动对地球和太空技术影响的理解。

科学家们现在正致力于将这项技术应用于夏威夷的4米美国国家科学基金会丹尼尔·井上太阳望远镜，以获得更精细的细节。他们预计这项突破将彻底改变地基太阳天文学，从而带来更多关于太阳大气层的发现。

---

## 83. 在POSIX中，理论上你可以使用inode零。

**原文标题**: In POSIX, you can theoretically use inode zero

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/unix/POSIXAllowsZeroInode](https://utcc.utoronto.ca/~cks/space/blog/unix/POSIXAllowsZeroInode)

Chris Siebenmann's blog, Wandering Thoughts, is displaying a "too-old browser" message to users due to anti-crawler precautions implemented to combat a surge of high-volume crawlers, particularly those using old Chrome user agents for LLM training data gathering. The system mistakenly flags legitimate older browsers as suspicious.

If a user encounters this message in error with a modern browser, they are encouraged to contact Siebenmann at his university email address (which they can deduce) with details about their browser and User-Agent string.

A specific issue is highlighted regarding archive.* services (archive.today, archive.ph, archive.is, etc.). These archiving services are being blocked because their crawling behavior mimics that of malicious actors: using outdated Chrome User-Agents, originating from widely distributed IP address blocks not clearly identified as theirs, and sometimes employing falsified reverse DNS entries claiming to be Googlebot. Siebenmann recommends using archive.org instead, as it is a better-behaved archival crawler. The entry is dated February 17, 2025.


---

## 84. The Princeton INTERCAL Compiler's source code

**原文标题**: The Princeton INTERCAL Compiler's source code

**原文链接**: [https://esoteric.codes/blog/published-for-the-first-time-the-original-intercal72-compiler-code](https://esoteric.codes/blog/published-for-the-first-time-the-original-intercal72-compiler-code)

生成摘要时出错

---

## 85. 三碘化氮 (2016)

**原文标题**: Nitrogen Triiodide (2016)

**原文链接**: [https://www.fourmilab.ch/documents/chemistry/NI3/](https://www.fourmilab.ch/documents/chemistry/NI3/)

约翰·沃克的《三碘化氮》讲述了他在工程学院学习期间与该化合物的爆炸性遭遇，并详细介绍了它的性质。三碘化氮（NI3）是由碘与氢氧化铵反应形成的，由于空间位阻而极不稳定，其中大的碘原子与氮原子结合不良。这种高能构型很容易重新排列成氮气和元素碘，并以巨响和紫色碘蒸气的形式释放能量。

三碘化氮极其敏感，只需极小的激活能，例如触摸、声音甚至α粒子，就能引爆。湿润时相对稳定，但干燥后会变得异常敏感。这使得它不适用于实际应用，因为它会不受控制地爆炸。作者警告不要进行相关实验，因为它具有不可预测性，建议读者观看演示其性质的视频。

文章还澄清了通常制备的“三碘化氮”实际上是NI3和氨的加合物（NI3·NH3）。纯NI3更加不稳定，在-20°C升华，在0°C自发分解，因此难以研究。沃克最后建议读者对红紫色污渍保持警惕，尤其是在大学校园里，因为他有过亲身经历。

---

## 86. Hip：C++异构计算接口，用于可移植性

**原文标题**: Hip: C++ Heterogeneous-Compute Interface for Portability

**原文链接**: [https://github.com/ROCm/hip](https://github.com/ROCm/hip)

HIP (可移植异构计算接口) 是一种 C++ 运行时 API 和内核语言，使开发者能够使用单一源代码为 AMD 和 NVIDIA GPU 创建可移植的应用程序。它旨在成为一个薄层，与原生 CUDA 相比性能影响极小。HIP 允许使用 C++ 特性，如模板和 Lambda 表达式，并支持在每个平台上使用最佳的开发工具。

主要特性包括：

*   **可移植性：** 编写一次代码，即可在 AMD 和 NVIDIA GPU 上运行。
*   **性能：** 与原生 CUDA 相比，开销极小。
*   **现代 C++：** 利用 C++11 特性，并允许单源 C++ 开发。
*   **平台专业化：** 允许开发者针对特定平台进行调整。
*   **转换工具：** HIPIFY 自动将 CUDA 代码转换为 HIP，简化移植过程。
*   **编译器灵活性：** 使用 `nvcc` (CUDA) 或 HIP-Clang (AMD) 进行编译。

该存储库包括：

*   **头文件：** `hip_runtime_api.h`（核心 API）和 `hip_runtime.h`（包含内核启动语法）。
*   **实现细节：** 平台特定代码位于 `amd_detail/` 和 `nvidia_detail/` 中。
*   **工具：** `hipcc`（编译器驱动程序）和 `hipconfig`（配置信息）。
*   **文档：** Markdown 和 Doxygen 文档。
*   **示例：** 可在 ROCm-examples 存储库中找到。

要开始使用，请参阅安装说明和 CUDA 项目移植指南。通过 GitHub 问题跟踪器报告问题，如果可能，请包括 `hipconfig --full` 和 `samples/1_hipInfo/hipInfo` 的输出。

---

## 87. Show HN: Patio – Rent tools, learn DIY, reduce waste

**原文标题**: Show HN: Patio – Rent tools, learn DIY, reduce waste

**原文链接**: [https://patio.so](https://patio.so)

Patio is presented as a platform designed to help people with DIY projects, reduce waste, and access construction resources. It offers a multifaceted approach encompassing several key features:

*   **DIY News and Quizzes:** The platform provides educational content to help users learn about DIY projects, offering news and interactive quizzes to enhance their knowledge.

*   **Tool Rentals:** A core feature is the ability to rent tools, making DIY projects more accessible and affordable, while also encouraging resource sharing and reducing the need for individual tool ownership and subsequent waste.

*   **Construction Marketplace:** Patio also acts as a marketplace, connecting users with construction professionals and potentially other DIYers. This can facilitate finding help, materials, or collaborators for their projects.

In essence, Patio aims to be a one-stop shop for DIY enthusiasts, combining learning resources, access to tools through rentals, and a community marketplace for support and resources, all while promoting sustainability.


---

## 88. 估算对数

**原文标题**: Estimating Logarithms

**原文链接**: [https://obrhubr.org/logarithm-estimation](https://obrhubr.org/logarithm-estimation)

本文阐述了一种估算以10为底的对数的方法，据说是约翰·纳皮尔提出的。其核心思想是，一个数的对数近似等于其位数减一。通过反复将该数提高到10的幂并观察所得的位数，可以改进这个近似值。

该方法利用对数性质log(a^b) = b*log(a)。本文描述了该算法：log(N) ≈ #(N^10) / 10，其中#N表示N的位数减一。将指数增加到更高的10的幂可以提高精度。

为了避免繁琐的求幂运算，作者建议使用科学计数法。与其每次迭代都从头开始，不如利用之前计算的结果。这涉及到仅对尾数进行求幂和乘法运算。

然后，作者提供了一个Python脚本来自动化该过程，该脚本迭代地计算N^(prev^10)，从N^10开始。每次迭代都涉及将尾数提高到10的幂，并将指数乘以10，从而简化计算并允许任意精度。该脚本使用`decimal`库来处理大数和精度。

---

## 89. TPDE：一种快速可适应的编译器后端框架

**原文标题**: TPDE: A Fast Adaptable Compiler Back-End Framework

**原文链接**: [https://arxiv.org/abs/2505.22610](https://arxiv.org/abs/2505.22610)

这篇arXiv文章（arXiv:2505.22610）介绍了TPDE，一种为快速和适应性强的代码生成而设计的新型编译器后端框架。来自慕尼黑工业大学的Tobias Schwarz、Tobias Kamm和Alexis Engelke指出，现有框架（如LLVM）在编译速度方面存在局限性，尤其是在JIT编译方面。他们认为，翻译成中间表示（IR）会增加不必要的延迟。

TPDE通过适应现有的SSA形式的代码表示来解决这个问题。它使用特定于IR的适配器来规范地访问IR数据结构并指定IR语义，从而实现单遍编译过程，该过程在初始分析之后结合了指令选择、寄存器分配和指令编码。生成的目标指令主要来自使用LLVM的Machine IR编写的高级语言代码，从而提高了跨不同架构的可移植性，同时允许在代码生成期间进行优化。

作者通过构建针对x86-64和AArch64的LLVM新后端来展示TPDE的通用性。使用SPECint 2017的性能评估表明，TPDE编译LLVM-IR的速度比LLVM -O0快8-24倍，同时保持了相当的运行时性能。该论文进一步展示了TPDE在特定领域IR环境（如WebAssembly和数据库查询编译）中的优势，在这些环境中，避免IR转换可以进一步最大限度地减少编译延迟。该论文包含23页和10个图。

---

## 90. Codex CLI 正在原生化

**原文标题**: Codex CLI is going native

**原文链接**: [https://github.com/openai/codex/discussions/1174](https://github.com/openai/codex/discussions/1174)

在2025年5月30日的帖子中，fouad-openai宣布将Codex CLI过渡到原生Rust实现。此举旨在提高跨平台稳定性、安全性、性能和可扩展性。此次重写解决了社区反馈以及TypeScript版本存在的持续性问题。

主要改进包括：

*   **零依赖安装：** 消除了对Node v22+的要求，解决了用户的痛点。
*   **原生安全绑定：** 利用现有的基于Rust的Linux沙盒。
*   **优化性能：** 通过避免运行时垃圾回收来降低内存消耗。
*   **可扩展协议：** 引入了一种“线路协议”，允许开发人员使用各种语言（TypeScript、Python等）和MCP扩展代理，这些已在Rust中得到支持。

用户可以使用 `npm i -g @openai/codex@native` 测试新版本。虽然TypeScript版本仍在继续进行错误修复，但Rust实现将很快实现功能对等。线路协议目前在`codex-rs/core/src/protocol.rs`中定义，使开发人员能够使用不同的语言扩展代理。团队还在探索使用WebAssembly进行扩展。

该帖子还解决了关于组织验证问题和工具名称长度限制的担忧。 团队正在积极寻求对新版本的反馈，并招聘Rust开发人员来为该项目做出贡献。

---

## 91. 退一步

**原文标题**: Stepping Back

**原文链接**: [https://rjp.io/blog/2025-05-31-stepping-back](https://rjp.io/blog/2025-05-31-stepping-back)

作者反思了“后退一步”的重要性，以便从任务和问题中获得视角，避免迷失在无成效的追求中。他们描述了一段个人经历，即过度投入于一项使用LLM的编码任务，但被迫中断后才意识到自己的努力方向错误。这说明了一种反复出现的模式，即高度的专注可能会让他们看不到更广泛的目标和更有效的解决方案。

作者承认了深入解决问题和质疑其有效性之间固有的张力。虽然坚韧对工程师来说至关重要，但它也可能导致无谓的执着。他们借鉴强化学习中的探索/利用困境，询问如何平衡追求特定的修复与重新评估整体方法。

他们建议实施与自然时间边界（小时、天、周、月、年）相关的定期反思仪式，以策略性地评估自己的行为。这些检查包括询问“我在做什么？”、“我为什么要这样做？”和“我可以做什么？”。这些问题的深度和范围因时间范围而异，从每小时对功能范围进行小调整到每年对人生目标进行回顾。作者认为这种定期反思是对时间的宝贵投资，以确保他们朝着正确的方向前进，而不是将精力浪费在最终毫无意义的努力上。

---

## 92. 数字市场法案的Windows更新

**原文标题**: Updates to Windows for the Digital Markets Act

**原文链接**: [https://blogs.windows.com/windows-insider/2025/06/02/updates-to-windows-for-the-digital-markets-act/](https://blogs.windows.com/windows-insider/2025/06/02/updates-to-windows-for-the-digital-markets-act/)

为遵守《数字市场法》，本文详细介绍了Windows 10、Windows 11以及欧洲经济区（EEA）内Microsoft应用即将发生的变化。这些更新将通过Windows预览体验计划版本逐步推出，然后发布到零售版，主要集中在浏览器默认设置、Windows搜索、Microsoft Store和Microsoft应用上。

**主要变化：**

*   **默认浏览器：** 设置默认浏览器现在将包括更多链接和文件类型（ftp、read、.mht等）。它还会将所选浏览器固定到任务栏（可选）。用户现在可以设置打开.pdf文件的默认浏览器。
*   **Windows搜索：** 应用可以在Windows搜索中提供网络搜索结果，并行显示。用户可以在“设置”中重新排序提供商。
*   **Microsoft Store：** 欧洲经济区内的用户可以卸载Microsoft Store。即使卸载后，应用商店应用仍将继续接收更新。
*   **Microsoft应用：** Microsoft必应应用和“开始体验”应用将在默认浏览器中打开Web内容。只有直接打开Microsoft Edge时，才会提示用户将其设置为默认浏览器。卸载后，其他Microsoft应用不会提示重新安装Edge（使用Edge技术通过Microsoft Store分发的PWA除外）。

本文提到了这些更改的具体内部版本号和发布时间表，重点介绍了通过预览体验成员通道逐步推出，然后发布到零售版本的阶段性发布。

---

## 93. 战争与荒野：英国士兵在革命时期的美国

**原文标题**: War and Wilderness: British Soldiers in Revolutionary America

**原文链接**: [https://www.historytoday.com/archive/feature/war-and-wilderness-british-soldiers-revolutionary-america](https://www.historytoday.com/archive/feature/war-and-wilderness-british-soldiers-revolutionary-america)

战争与荒野：革命时期美国的英国士兵

在《战争与荒野：革命时期美国的英国士兵》一书中，Vaughn Scribner 探讨了美国环境对革命战争期间英国和黑森士兵的深刻影响。除了与美国叛军作战之外，这些部队还面临着与陌生而充满敌意的自然世界的持续斗争。

Scribner 强调了美国地形、植物、动物、天气和疾病带来的挑战。广阔的沼泽地，到处都是鳄鱼和昆虫，成为了痛苦的象征。例如，“大荒凉沼泽”被证明是一个令人望而却步的障碍，而与鳄鱼的遭遇则灌输了持续的恐惧。

蚊子是一种特别无情的折磨，传播疟疾和黄热病等致命疾病。这些疾病大量削减了英国和黑森士兵的队伍，他们缺乏免疫力和应对这些疾病的经验。蚊子的流行，因南方殖民地水稻种植而加剧，大大削弱了英国军队，导致他们在约克镇的失败。

该文章还详细介绍了霍雷肖·纳尔逊在美洲中部进行的命运多舛的圣胡安远征，英国士兵在那里面临着茂密的热带雨林及其多样化的野生动物。与鬣蜥和蛇的遭遇增加了他们的焦虑。最终，恶劣的环境对士兵的身心健康造成了沉重的打击，让许多像托马斯·休斯一样的人因在美国荒野中的经历而永远改变。这篇文章有效地论证了美国的环境是一个强大的敌人，它极大地影响了革命战争的进程和结果。

---

## 94. 《安多》的摄影

**原文标题**: Cinematography of “Andor”

**原文链接**: [https://www.pushing-pixels.org/2025/05/20/cinematography-of-andor-interview-with-christophe-nuyens.html](https://www.pushing-pixels.org/2025/05/20/cinematography-of-andor-interview-with-christophe-nuyens.html)

对克里斯托弗·纽延斯访谈：揭秘《安多》第二季的摄影幕后

---

## 95. 乐器内部拍摄的照片

**原文标题**: Photos taken inside musical instruments

**原文链接**: [https://www.dpreview.com/photography/5400934096/probe-lenses-and-focus-stacking-the-secrets-to-incredible-photos-taken-inside-instruments](https://www.dpreview.com/photography/5400934096/probe-lenses-and-focus-stacking-the-secrets-to-incredible-photos-taken-inside-instruments)

dpreview.com 上的文章“乐器内部照片”探讨了摄影师查尔斯·布鲁克斯如何运用特殊技巧，从乐器内部捕捉到令人惊叹的图像。

布鲁克斯使用探针镜头，一种细长的镜头，使他能够伸入吉他、大提琴和萨克斯管等乐器的内部狭小空间。这些镜头通常在近距离具有宽广的景深，但为了获得乐器内部更加清晰的图像，他使用了焦点堆叠技术。

焦点堆叠包括拍摄同一场景的许多图像，每个图像都有略微不同的焦点。然后使用软件将这些图像组合起来，创建一个具有极宽景深的单个图像，从而使乐器内部从最近点到最远点都清晰聚焦。

文章强调了这一过程的挑战，包括需要精确的照明、仔细的镜头定位以及稳定的平台，以避免多次曝光期间的相机抖动。布鲁克斯一丝不苟地清洁乐器内部，以最大限度地减少最终图像中可见的灰尘和瑕疵。

最终的照片提供了一个独特的视角，揭示了乐器内部隐藏的美丽和复杂的工艺。这些图像将熟悉的物体转变为木材、金属和阴影的抽象景观，展示了每件乐器构造的独特艺术性。它们还揭示了通常肉眼无法看到的方面，从而增强了对乐器制造中涉及的细节和精确度的欣赏。

---

## 96. Go 中的结构化错误 (2022)

**原文标题**: Structured Errors in Go (2022)

**原文链接**: [https://southcla.ws/structured-errors-in-go](https://southcla.ws/structured-errors-in-go)

本文探讨了Go语言中的结构化错误处理，倡导通过使用元数据丰富错误信息，从而改进调试和日志记录，尤其是在HTTP API中。Go语言的简单错误字符串方法虽然可行，但缺乏结构，无法在日志聚合器中进行有效的机器处理。

作者强调了符合人体工程学的解决方案的重要性，即易于实施的良好实践。自定义错误结构体需要更多的工作，使用频率较低，导致错误信息不足。

提出的解决方案包括使用类似Logrus日志库的`Fields`对象来包装带有元数据的错误。`Wrap`函数向错误添加元数据，`GetErrorFields`函数提取此元数据以进行结构化日志记录。

为了减少手动工作，作者建议使用Go的`context`包在调用树期间存储元数据。然后，可以在包装错误时将此元数据添加到错误中。`WithMeta`函数将元数据添加到上下文中，`Wrap`函数提取上下文元数据并将其添加到错误中。

文章强调了上下文和错误之间的二元性，认为错误本质上是反向的上下文，在它们上升到调用树时积累信息。代码示例演示了如何使用Go的context包和`errors`库实现`WithMeta`、`Wrap`和`Unwrap`函数，以管理结构化错误元数据。目的是提供一种简单有效的方式来向错误添加上下文信息，从而提高调试和日志记录的效率。

---

## 97. 波西米亚人在门口？

**原文标题**: Bohemians at the Gate?

**原文链接**: [https://inferencemagazine.substack.com/p/bohemians-at-the-gate](https://inferencemagazine.substack.com/p/bohemians-at-the-gate)

无法访问文章链接。

---

## 98. 大模型很便宜

**原文标题**: LLMs Are Cheap

**原文链接**: [https://www.snellman.net/blog/archive/2025-06-02-llms-are-cheap/](https://www.snellman.net/blog/archive/2025-06-02-llms-are-cheap/)

本文认为，运行大型语言模型（LLMs）的成本出乎意料地低廉，挑战了普遍认为它们成本高昂的观点。作者旨在为未来的讨论提供一个参考点，强调推理成本已大幅下降。

论点的核心是将LLM查询的成本与网络搜索查询的成本进行比较。作者列出了谷歌、必应和Brave等公司公开的网络搜索API定价。然后，他们估算了每个LLM查询的token输出量，并将其与Gemini、GPT-4.1和Claude 3.5等各种模型的每个token价格进行比较，得出结论，即使考虑到潜在的补贴或搜索索引构建的摊销等因素，LLM也可能比网络搜索便宜得多。

作者先发制人地解决了潜在的异议，例如更长的LLM响应、市场份额补贴和网络搜索的速度。他们认为，即使经过调整，成本差异仍然显著。

文章最后讨论了低LLM运营成本的影响。它表明，随着价格下降和需求增加，人工智能公司可以收回培训成本。它还认为，广告成为面向消费者的AI的一种可行且有利可图的货币化策略。最后，作者推测了与AI代理访问后端服务相关的未来挑战，特别是关于抓取成本以及AI代理和服务提供商之间潜在的对抗关系。作者预测，AI模型的运行成本不会太高，但真正的成本问题在于后端服务以及对AI优化数据提供商的需求。

---

## 99. 渐进式JSON

**原文标题**: Progressive JSON

**原文链接**: [https://overreacted.io/progressive-json/](https://overreacted.io/progressive-json/)

本文介绍了“渐进式JSON”，这是一种流式传输JSON数据的方法，它改进了传统的、要么全部加载要么完全不加载的JSON加载方式以及简单的流式传输方法。作者认为，在处理之前等待整个JSON有效负载加载完成是低效的，尤其是在服务器上生成部分数据需要更长时间的情况下。

简单的流式传输JSON虽然能更早地传递数据，但可能导致对象格式错误并缺少属性，使其难以有效使用。渐进式JSON通过广度优先发送数据来解决这个问题，在主JSON结构中使用占位符（例如“$1”）来表示尚未到达的数据。这些占位符随后会被实际数据替换，这些实际数据可以以任何顺序发送，从而允许客户端在等待较慢的部分时开始处理可用数据。待处理的数据由Promise表示。

文章还讨论了“内联”，即将完整的数据部分直接包含在主JSON中，而不是作为单独的占位符，以提高效率。最后，介绍了“外联”，这是一种通过发送一次并多次引用它们来消除流中重复对象的方法。

作者将渐进式JSON与React服务器组件（RSC）进行了类比，其中服务器流式传输表示为JSON的渐进式加载的React树。他强调，React的`<Suspense>`组件使开发人员能够控制何时向用户显示UI的各个部分，从而将数据到达与视觉更新分离，并允许更优雅的加载体验。核心思想是，数据应尽可能快地流式传输，但UI应根据有意的加载状态进行显示。

---

## 100. 泰德神父基尔内托神龛胶带座

**原文标题**: Father Ted Kilnettle Shrine Tape Dispenser

**原文链接**: [https://stephencoyle.net/kilnettle](https://stephencoyle.net/kilnettle)

斯蒂芬·科伊尔详述了改进版“神父特德” Kilnettle圣坛会说话胶带座的制作过程。几年前他曾制作过一个，但这个新版本更小巧、音质更好、外观更专业、且更易于制作。

新设计特点：

*   无需支撑的3D打印外壳。
*   使用红外LED和传感器测量胶带旋转，取代旋转编码器。
*   ESP8266微控制器，将电子元件成本降低到10欧元以下。

科伊尔提供了全面的文档，包括软件、3D模型和说明，可在GitHub和Printables上获取，并提供组装视频。他鼓励具有基本焊接技能和3D打印机的人们制作自己的版本，只需一天即可完成。

虽然他曾考虑出售这些胶带座，但由于时间限制、对朋友和家人的承诺以及缺乏吸引力的价格点，他最终放弃了。相反，他将资源公开提供给DIY爱好者。

最后，他请求任何制作该胶带座的人考虑向支持跨性别者的慈善机构捐款，理由是“神父特德”的创作者之一持有令人遗憾的观点。

---

