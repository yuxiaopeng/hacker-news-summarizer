# Hacker News 热门文章摘要 (2025-11-07)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 我爱OCaml

**原文标题**: I Love OCaml

**原文链接**: [https://mccd.space/posts/ocaml-the-worlds-best/](https://mccd.space/posts/ocaml-the-worlds-best/)

本文是一封写给 OCaml 编程语言的情书，它出自一位拥有 Haskell 和 Go 经验的开发者之手。作者讲述了他们欣赏 OCaml 的历程，强调了那些在一个编程语言中对他们而言变得重要的特性。

他们最初重视 Haskell 强大的静态保证和函数式编程结构，但发现其复杂性、缓慢的编译时间和“聪明”的代码难以管理。另一方面，Go 提供了简洁性、快速编译和良好的工具，但其冗长、脆弱的错误处理、缺乏空值检查以及对函数式编程概念的抵制最终导致了不满。

作者理想的语言愿望清单包括快速的编译时间、简单的运行时、强大的静态类型、函数式编程特性（模式匹配、和类型）、良好的性能以及优秀的文档。他们认为，OCaml 几乎满足了所有这些要求。

具体来说，他们赞扬 OCaml 通过和类型和模式匹配实现的强大静态保证、相对简单的运行时语义（允许经验丰富的程序员理解生成的汇编）、使用 Dune 实现的快速编译时间、能够编译成单个二进制文件以便于部署、通过 odig 和 utop 实现的优秀文档以及自动推断的类型。

虽然承认 OCaml 的历史悠久以及一些可能不必要的特性，但作者最终得出结论，OCaml 在简洁性和表达性之间取得了恰当的平衡，并辅以良好的文档和工具。他们将此归功于 OCaml 设计者的良好品味。

---

## 2. 离开Meta和PyTorch

**原文标题**: Leaving Meta and PyTorch

**原文链接**: [https://soumith.ch/blog/2025-11-06-leaving-meta-and-pytorch.md.html](https://soumith.ch/blog/2025-11-06-leaving-meta-and-pytorch.md.html)

PyTorch负责人Soumith Chintala将在Meta工作11年后离职，其中近8年致力于将PyTorch从零开始构建到目前在人工智能领域的统治地位。他表达了离开的兴奋和不舍，强调了PyTorch的深远影响，从支持百亿亿级训练到在全球范围内被教授。

虽然承认还有更多工作要做，但他相信PyTorch处于稳定且有能力继续发展的状态，由Edward、Suo、Alban、Greg、John、Joe和Jana领导。他强调了现在负责团队的强大价值观一致性和技术实力，确保了项目的未来成功。

Soumith深情地回顾了他在FAIR的早期岁月，称赞了促进创新的协作和高效的环境。他感谢关键人物和团队对PyTorch成功的贡献，并对社区的支持以及PyTorch对研究人员和更广泛的人工智能领域的影响表示感谢。

他还感谢Meta的领导者，如马克·扎克伯格和迈克·施罗普弗，他们相信开源是一种商业策略，以及公司内部支持他的管理者。

他离开的决定源于探索新的、不舒适的事物的愿望，一个在Meta之外的“小型”项目，其动机是好奇心和避免从未尝试过不同事物的遗憾。他打算继续参与PyTorch，提供反馈和提交问题，同时追求他的新事业。

---

## 3. 我用 Zig 构建 Bytebeat 播放器的经验

**原文标题**: My Experience of building Bytebeat player in Zig

**原文链接**: [https://blog.karanjanthe.me/posts/zig-beat/](https://blog.karanjanthe.me/posts/zig-beat/)

这篇博文详细介绍了作者使用 Zig 构建名为 Zigbeat 的 bytebeat 播放器的经验。受休息期间对有趣项目的渴望启发，作者选择了 Zig，因为它具有类似 C 的感觉并且没有借用检查器。

该文章解释了 bytebeat 是一种算法音乐形式，它使用位运算从短程序生成 8 位音频样本。

作者最初在使用 raylib-Zig 时遇到了挑战，因为示例已过时，并且难以设置 Emscripten 进行 WASM 编译。他们了解到 Zig 缺乏原生字符串支持，从而更深入地理解了内存分配。作者实现了一个 Pratt 解析器用于表达式解析，但这揭示了性能问题，因为每次音频样本评估都会过度分配内存。

解决方案是使用 Arena Allocator，它以块的形式分配内存，从而提高性能。作者还尝试使用 raylib 的绘图 API 实现复古的 8 位合成器外观，但在设计方面遇到了困难，最终选择了精灵。

作者强调了使用 Zig 而不是 Javascript（Javascript 具有 `eval`，可以更轻松地执行表达式）的好处，因为它迫使他们学习解析、词法分析和内存管理。该文章包含指向 Zigbeat GitHub 存储库的链接，并鼓励读者在 Twitter 上分享和互动。

---

## 4. 深情告别

**原文标题**: A Fond Farewell

**原文链接**: [https://www.farmersalmanac.com/fond-farewell-from-farmers-almanac](https://www.farmersalmanac.com/fond-farewell-from-farmers-almanac)

《农民年鉴》在出版200多年后，将于2026年版后停止运营。在一份告别信中，《年鉴》工作人员向其忠实的读者、贡献者和合作伙伴表达了多年的支持与感谢。该声明称，结束印刷和在线出版是一个“艰难的决定”。

该信息突出了《年鉴》的历史意义，指出它曾出现在许多家庭中，并在指导种植、如厕训练和钓鱼等活动中发挥了作用。尽管《年鉴》将不再发行，但工作人员鼓励读者通过记住和分享其传统和智慧来保持其精神。

最后一版2026年版目前可在FarmersAlmanac.com、Amazon.com和部分当地商店购买。FarmersAlmanac.com网站将保持可访问状态至2025年12月。订阅者请查看电子邮件以获取与订阅相关的信息。该文章由《农民年鉴》工作人员撰写，并于2025年11月6日发布。

---

## 5. Meta预计2024年收入的10%来自诈骗。

**原文标题**: Meta projected 10% of 2024 revenue came from scams

**原文链接**: [https://sherwood.news/tech/meta-projected-10-of-2024-revenue-came-from-scams-and-banned-goods-reuters/](https://sherwood.news/tech/meta-projected-10-of-2024-revenue-came-from-scams-and-banned-goods-reuters/)

根据路透社看到的Meta内部文件显示，Meta预计其2024年收入的10%，约160亿美元，将来自诈骗广告和违禁商品的销售。这些文件揭示了Meta内部承认，因未能遏制其平台上的欺诈活动，可能会面临巨额罚款。该公司战略性地优先在处罚最严重的地区加强执法，权衡打击诈骗可能造成的收入损失与监管罚款的成本。

尽管Meta旨在减少欺诈行为，但由于对其审核团队的削减，导致大部分用户举报的违规行为被忽略或驳回。 Meta发言人安迪·斯通淡化了这些文件，声称它们提供了内部执法工作的“选择性视角”，并表示Meta积极打击欺诈和诈骗。然而，该报告强调了Meta容忍此类活动的巨大经济动机，即使它公开宣称要打击这些活动。

---

## 6. PyTorch Helion
PyTorch氦龙

**原文标题**: PyTorch Helion

**原文链接**: [https://pytorch.org/blog/helion/](https://pytorch.org/blog/helion/)

Helion：弥合 PyTorch 易用性与自定义内核高性能的新型 Python 嵌入式 DSL。它通过将高级 DSL 编译成自动调优的 Triton 代码，解决了维护特定硬件内核的挑战，从而在降低开发工作量的同时，提供跨硬件架构的性能可移植性。

Helion 的编程模型“带图块的 PyTorch”利用了现有的 PyTorch 知识。内核由宿主机代码（用于设置的标准 PyTorch）和设备代码（编译为 Triton 内核）组成，后者使用 `hl.tile` 来细分迭代空间。Helion 使用 TorchInductor 将 PyTorch 运算符映射到 Triton 实现。一个关键特性是能够将 lambda 函数作为参数传递，以创建通用内核。

Helion 的主要创新是其自动调优引擎，该引擎使用隐式搜索空间来探索大量的 Triton 配置。此过程优化了块大小、循环排序和内存访问模式等参数，从而生成针对特定硬件定制的内核。自动调优器评估数千种配置并提供最佳配置，该配置可以硬编码以用于生产中的确定性编译。

在 NVIDIA B200 和 AMD MI350X GPU 上的基准测试表明，与 torch.compile（使用 max-autotune）和手写 Triton 内核相比，Helion 实现了更高的几何平均加速比。Helion 的自动调优引擎通过自动化对最佳内核配置的复杂搜索，优于手动调优的内核，从而提高了性能并缩短了开发时间。一个案例研究表明，Helion 在 RMSNorm 反向实现中达到或超过了手写优化的 CuTe DSL 内核的性能。

---

## 7. OpenMW 0.50.0 发布 – 开源上古卷轴 3：晨风重制版

**原文标题**: OpenMW 0.50.0 Released – open-source Morrowind reimplementation

**原文链接**: [https://openmw.org/2025/openmw-0-50-0-released/](https://openmw.org/2025/openmw-0-50-0-released/)

好的，以下是一个基于假设该URL指向OpenMW 0.50.0标准发布公告的摘要。由于我无法直接访问该URL，我将根据典型的发布公告内容进行推断。

OpenMW 0.50.0，开源Morrowind引擎重制版的一个重要里程碑版本，已经发布。此版本侧重于提高稳定性、修复错误以及增强整体游戏体验，而不是引入重大的新功能。主要改进通常包括：

*   **错误修复和稳定性：** 此版本解决了社区报告的许多错误和崩溃问题，从而带来更稳定和可靠的游戏体验。这包括修复与脚本、渲染和AI相关的问题。

*   **性能改进：** 对引擎进行了优化，从而获得更流畅的性能，尤其是在图形密集区域或使用Mod时。

*   **AI增强：** AI得到了改进，更新了寻路、战斗行为以及与环境的互动。

*   **Mod支持：** 扩展或改进的Mod支持通常是重点，增加了兼容性或为Mod开发者提供了新功能。这可能包括更好地处理特定Mod类型或改进的工具。

*   **渲染改进：** 对渲染引擎的可能改进可能包括更好的阴影、光照或视觉效果。

*   **声音改进：** 声音引擎中可能发生错误修复或功能实现。

*   **UI/UX更新：** 增强用户界面和用户体验，例如改进的菜单、更好的对话处理或更直观的控件，通常是重点。

OpenMW团队鼓励用户下载新版本并报告遇到的任何问题。发布公告很可能感谢贡献者，并为那些对细节感兴趣的人提供详细的变更日志。这证明了对开源项目的持续改进，旨在为未来保存Morrowind。

如果实际的发布公告有很大不同，我将无法在没有访问权限的情况下更新此摘要。

---

## 8. 我们选择 OCaml 来编写 Stategraph。

**原文标题**: We chose OCaml to write Stategraph

**原文链接**: [https://stategraph.dev/blog/why-we-chose-ocaml](https://stategraph.dev/blog/why-we-chose-ocaml)

本文解释了为何使用 OCaml 构建用于管理 Terraform 状态的工具 Stategraph。主要原因是 OCaml 强大的类型系统，它能确保正确性并防止可能损坏状态并导致生产问题的严重错误。

本文重点介绍了使用 OCaml 的几个主要优势：

*   **类型安全的数据结构：** OCaml 的类型系统可以在编译时捕获与数据结构字段、类型和空值检查相关的错误，从而防止运行时错误和数据损坏。
*   **类型安全的 SQL 查询：** OCaml 强制执行 SQL 查询及其使用之间类型的一致性，防止模式漂移问题导致生产环境崩溃。数据库模式的更改需要代码中进行相应的更新，并由编译器强制执行。
*   **自动 JSON 序列化：** OCaml 的 PPX 从类型定义生成正确的 JSON 序列化代码，无需进行大量的序列化测试，并防止转换过程中数据丢失。
*   **默认的不可变性：** OCaml 默认的不可变性通过确保共享状态不会被意外地并发修改来防止竞争条件。
*   **严谨的错误处理：** OCaml 的变体类型和穷举性检查确保所有可能的错误情况都得到显式处理。

本文承认 OCaml 开发者比较稀少，但认为具有分布式系统和类型系统经验的工程师可以快速学习 OCaml。 稳定、类型安全的代码库的好处超过了寻找 OCaml 开发者带来的挑战，因为类型系统减少了调试时间，并允许开发者专注于功能开发。 文章总结说，对于构建像 Stategraph 这样正确性至关重要的系统来说，OCaml 的编译时保证至关重要。

---

## 9. 比较特征 – 理解 Rust 中的相等性和排序

**原文标题**: Comparison Traits – Understanding Equality and Ordering in Rust

**原文链接**: [https://itsfoxstudio.substack.com/p/comparison-traits-understanding-equality](https://itsfoxstudio.substack.com/p/comparison-traits-understanding-equality)

无法访问文章链接。

---

## 10. 1973年Wordle的实现由DEC于2022年发布

**原文标题**: 1973 Implementation of Wordle was Published by DEC (2022)

**原文链接**: [https://troypress.com/1973-implementation-of-wordle-was-published-by-dec/](https://troypress.com/1973-implementation-of-wordle-was-published-by-dec/)

本文追溯了类Wordle游戏的起源，最早可追溯到1973年，重点介绍了Digital Equipment Corp.发布的“WORD”游戏，该游戏与Wordle具有核心机制，并能提供字母存在和位置的反馈。WORD由查尔斯·里德编写，早于游戏节目“Lingo”，并使用文本界面。

随后，本文探讨了早期计算机中猜谜游戏的更广泛背景，指出它们非常适合简单的程序。文章重点介绍了沃尔特·科特克的“GUESS”，该游戏被认为是许多后续游戏的灵感来源，以及它对丹尼斯·艾利森在“构建你自己的BASIC”中倡导猜谜游戏的影响。

文章还讨论了其他几款早期的BASIC猜谜游戏，包括“HI-LO”、“NUMBER”、“STARS”、“TRAP”和“BAGELS”，展示了游戏玩法和主题的变化。文中还提到了以战斗为主题的猜谜游戏，如“TARGET”、“Bombardment”和“Salvo”。

本文将这些简单的游戏与更复杂的“反向猜谜游戏”进行了对比，在反向猜谜游戏中，计算机试图猜测人类的想法，例如“ANIMAL”、“SALVO”、“DIGITS”和“NICOMA”。文章指出，早期计算机的局限性，尤其是在内存方面，阻碍了更复杂的反向猜谜游戏的发展。

作者鼓励读者在线探索这些经典的BASIC游戏，认为有可能重新发现它们并将其改编为现代平台。

---

## 11. 你应该编写一个代理。

**原文标题**: You should write an agent

**原文链接**: [https://fly.io/blog/everyone-write-an-agent/](https://fly.io/blog/everyone-write-an-agent/)

托马斯·帕切克在文章中指出，每个人都应该编写一个LLM Agent，不仅为了更好地理解它们，而且因为它出乎意料地简单且富有启发性。他消除了围绕Agent的神秘感，用简单的Python代码演示了如何创建具有多轮对话和工具使用等基本功能的Agent。

该论点的核心在于，Agent与其说是复杂的技术，不如说是巧妙的上下文管理。文章展示了“上下文窗口”，即对话的记忆，实际上只是一个你管理的字符串列表。他还强调，诸如ping之类的工具很容易集成，只需要JSON定义和函数调用。

帕切克强调“上下文工程”比“提示工程”更重要，将其定位为一个管理令牌限制并利用诸如子Agent等策略来处理复杂任务的有形编程问题。

作者批评了对“MCP”（插件接口）的过度强调，认为开发者应该专注于通过API构建自己的Agent，而不是依赖于预构建的插件，尤其是出于安全考虑。他强调，可以使用隔离的上下文和特定的工具来构建Agent，从而简化复杂的任务。

最终，帕切克鼓励读者尝试Agent，强调与不可预测性、将Agent置于真理中、连接Agent进行多阶段操作以及管理令牌成本相关的开放式工程问题。他认为这些挑战是可以解决的，并且适合个人创新，强调实践经验胜过理论理解。

---

## 12. 从损失曲率角度，从记忆到推理

**原文标题**: From Memorization to Reasoning in the Spectrum of Loss Curvature

**原文链接**: [https://arxiv.org/abs/2510.24256](https://arxiv.org/abs/2510.24256)

这篇题为“从记忆到推理：损失曲率谱分析”的论文，通过分析损失曲面曲率，探讨了 Transformer 模型（包括语言模型和视觉Transformer模型）中记忆与推理之间的关系。作者证明记忆反映在模型权重中，可以通过曲率分析来识别，因为记忆的数据点比非记忆的数据点表现出更尖锐的曲率。

在此基础上，他们提出了一种权重编辑程序，可以有效地抑制非目标记忆数据的背诵，同时与现有的反学习方法相比，保持较低的困惑度。该程序利用了模型权重中的共享结构反映在曲率基础中的事实。

作者研究了这种编辑程序对语言模型下游任务的影响，揭示了诸如事实检索和算术之类的任务受到了负面影响，而开放式事实检索和一般逻辑推理则得以保留。他们假设，受到负面影响的任务依赖于权重空间中专门的、狭隘使用的结构，而与单个数据点是否被记忆无关。这一点得到了支持，因为他们证明了任务数据在低曲率分量（被编辑掉）中的激活强度与任务性能的后续下降之间存在相关性。

本质上，该论文提供了一种解开神经网络中记忆的方法，为移除记忆提供了实际应用，并表明某些任务，如数学和事实检索，依赖于模型权重中特殊的结构，而不是一般的推理能力。

---

## 13. Go语言中接口隔离原则的再探讨

**原文标题**: Revisiting Interface Segregation in Go

**原文链接**: [https://rednafi.com/go/interface-segregation/](https://rednafi.com/go/interface-segregation/)

本文探讨了Go语言中SOLID原则之一的接口隔离原则(ISP)，论证了通过Go的小接口、隐式实现和消费者定义的契约等特性，其优势可以自然实现。

文章强调了使用宽泛接口的弊端，即迫使客户端依赖不需要的方法，导致不必要的耦合、更复杂的测试模拟以及不清晰的函数签名。

文章提倡定义小型、消费者端的接口，仅暴露必要的方法。这种方法使代码更易于测试，减少包之间的耦合，使代码更易于演进，并使代码的意图更清晰。Go的隐式接口满足允许现有的具体类型自动满足这些更窄的接口。

文章通过`FileStorage`和AWS SDK的`S3Client`为例，展示了如何重构代码以依赖更小的接口，例如`Saver`和`Uploader`，而不是更大的接口，例如`Storage`和`S3Client`。这种方法可以简化模拟，并防止在生产者端接口更改时，不必要的更改在代码库中传播。

核心建议是在紧密耦合的组件之间插入一个接缝，方法是放置一个消费者端的接口，该接口仅暴露调用者调用的方法。

---

## 14. 二十亿邮箱地址泄露

**原文标题**: Two billion email addresses were exposed

**原文链接**: [https://www.troyhunt.com/2-billion-email-addresses-were-exposed-and-we-indexed-them-all-in-have-i-been-pwned/](https://www.troyhunt.com/2-billion-email-addresses-were-exposed-and-we-indexed-them-all-in-have-i-been-pwned/)

特洛伊·亨特的文章讨论了一起大规模数据泄露事件，该事件暴露了超过20亿个电子邮件地址。亨特将其称为“MailChimp泄露”（尽管数据来自多个来源），其中包含营销活动和订阅列表中使用的电子邮件地址。

亨特获取了这些数据，并将所有20亿个地址索引到他的网站Have I Been Pwned (HIBP)中，允许用户检查他们的电子邮件地址是否属于被泄露的数据。他强调了将此数据添加到HIBP的重要性，因为它允许个人评估因电子邮件泄露而接收到有针对性的垃圾邮件、网络钓鱼攻击和其他恶意活动的潜在风险。

虽然此次泄露主要暴露了电子邮件地址（以及可能相关的姓名等数据），但主要担忧是针对性攻击的风险增加。有了这个庞大的数据集，恶意行为者可以精心制作更个性化和更具说服力的诈骗，从而增加网络钓鱼尝试或其他形式的在线剥削成功的可能性。亨特建议用户对收到的电子邮件格外警惕，尤其是那些要求提供敏感信息或包含可疑链接的电子邮件。添加到HIBP的功能使人们能够主动确定他们的暴露程度并采取适当的预防措施。

---

## 15. 人工智能与社交媒体助长“脑死亡”

**原文标题**: A.I. and Social Media Contribute to 'Brain Rot'

**原文链接**: [https://www.nytimes.com/2025/11/06/technology/personaltech/ai-social-media-brain-rot.html](https://www.nytimes.com/2025/11/06/technology/personaltech/ai-social-media-brain-rot.html)

无法访问文章链接。

---

## 16. Sweep (YC S23) 正在招聘，以构建 JetBrains 的自动补全功能。

**原文标题**: Sweep (YC S23) is hiring to build autocomplete for JetBrains

**原文链接**: [https://www.ycombinator.com/companies/sweep/jobs/8dUn406-founding-engineer-intern](https://www.ycombinator.com/companies/sweep/jobs/8dUn406-founding-engineer-intern)

Sweep (YC S23) 招聘创始工程师/实习生，打造用于JetBrains IDE的AI代码助手自动补全功能。该职位为全职，位于旧金山，要求每周五天现场办公，薪资范围为15万美元至22.5万美元，并提供1.00%至4.97%的股权期权。欢迎应届毕业生，并提供签证担保。

理想的候选人将直接与创始人合作，解决具有挑战性的人工智能和面向用户的问题。面试过程包括使用intellij-platform-plugin-template为JetBrains构建类似GitHub Copilot的自动补全功能。

Sweep 定位为JetBrains领先的企业级AI代码助手，强调数据隐私，将数据保留在用户的VPC内。该公司成立于2023年，是YC S23批次的一部分，团队由4人组成，并正在积极发展。他们拥有大型企业客户在生产中，并优先考虑快速迭代和交付。创始人为 Kevin Lu 和 William Zeng。 该职位列表还包括其他公司类似职位的列表。

---

## 17. 文本大小写会影响二维码的尺寸

**原文标题**: Text case changes the size of QR codes

**原文链接**: [https://www.johndcook.com/blog/2025/10/31/smaller-qr-codes/](https://www.johndcook.com/blog/2025/10/31/smaller-qr-codes/)

本文解释了用于生成二维码的文本大小写如何影响其尺寸。二维码可以以不同的模式编码数据，包括二进制和字母数字。当文本包含小写字母（大小写混合）时，它被编码为二进制数据，每个字符使用 8 位。然而，大写文本如果属于二维码的字母数字字符集（45 个字符），则可以字母数字模式编码，每个字符大约使用 5.5 位。

这种编码差异导致在使用字母数字集内的大写文本时，生成更小的二维码。本文用一个 Python 示例演示了这一点，展示了将句子转换为大写会导致更小的二维码。

然后，本文将此概念与比特币地址联系起来，特别是比较 Bech32 和 Base58 编码。虽然 Bech32 凭借其较小的 32 字符字母表，需要比 Base58 更多的字符，但由于它是单例的（转换为大写以生成二维码），因此允许字母数字编码，从而生成比 Base58 更小的二维码，Base58 是大小写混合的，因此以二进制模式编码。

---

## 18. 如何保持常胜

**原文标题**: How to Keep Winning

**原文链接**: [https://amasad.me/keep-winning](https://amasad.me/keep-winning)

持续成功的六项原则：强调长期、合乎伦理的制胜之道

1. 别死：优先考虑生存，理解并避免灾难性失败（字面意义和引申意义上的“死亡”）。关注不利情况，保持充足资源以应对挫折。失败通常是可以原谅的，允许调整和卷土重来。

2. 永不放弃：坚持是关键。避免因时机等原因过早放弃，保持持续积累。寻找其他衡量标准来追踪进展并保持动力，专注于渐进式改进和个人成长。

3. 全神贯注：培养必胜心态，并全身心投入当前任务。研究竞争对手，找出他们的弱点，并尽量减少风险以最大程度地发挥潜在优势。

4. 做难事：拥抱挑战，探索非常规道路。真正持久的竞争优势源于竞争对手避开的困难、创新的解决方案。战略性地自主研发而非购买技术，以保持控制力和适应性。

5. 遵守规则：合乎伦理的行为和遵守规则最终会带来长期的成功。不道德的捷径可能会带来短期收益，但不可持续。创新在道德行为的约束下蓬勃发展，从而培养信任和长期的护城河。

6. 回馈社会：为“人类经验池”做出贡献不仅在道德上是合理的，而且是有益的。回馈可以提升声誉，吸引人才，并通过建立善意和认可来促进制胜的循环。分享知识和路线图可能是一种优势。

---

## 19. 丹麦政府计划禁止15岁以下儿童访问社交媒体。

**原文标题**: Denmark's government aims to ban access to social media for children under 15

**原文链接**: [https://apnews.com/article/denmark-social-media-ban-children-7862d2a8cc590b4969c8931a01adc7f4](https://apnews.com/article/denmark-social-media-ban-children-7862d2a8cc590b4969c8931a01adc7f4)

Denmark's government has announced an agreement to ban social media access for children under 15, aiming to protect them from harmful content and commercial pressures. This move would allow parents, after assessment, to grant access from age 13. It follows Australia's lead, which set the minimum age at 16 with hefty fines for non-compliance by platforms like TikTok, Facebook, and Instagram.

The Danish government's statement indicates the ban will apply to "certain" social media platforms, though specifics and enforcement details are yet to be clarified. Lawmakers emphasize the need to shield children from the negative impacts of social media, citing disrupted sleep, decreased concentration, and pressure from digital relationships. They argue that the influence of tech giants is too strong for parents to manage alone.

Other regions are also grappling with similar concerns. China has limited online game and smartphone time for kids. In Paris, an investigation is underway into TikTok over content promoting suicide. The EU already prohibits children under 13 from having social media accounts and is considering raising the age to 16. The European Commission has also issued guidelines to strengthen protection of minors and is testing an age-verification app. Danish lawmaker Rasmus Lund-Nielsen described social media as the "Wild West" and highlighted the detrimental impact of social media on children's social lives, physical activity, and mental health.


---

## 20. Show HN: 我抓取了30亿Goodreads评论来训练更好的推荐模型

**原文标题**: Show HN: I scraped 3B Goodreads reviews to train a better recommendation model

**原文链接**: [https://book.sv](https://book.sv)

这个 "Show HN" 提交详细介绍了一个项目，该项目致力于使用包含 30 亿条 Goodreads 评论的巨型数据集构建图书推荐系统。作者抓取了这些数据，并可能用它来训练推荐模型。

着陆页的重点是互动元素：用户可以输入他们读过的书，模型将提供接下来要读的推荐书目。设置了受欢迎程度阈值，这意味着只有更受欢迎的书籍才会被包含在搜索和推荐中。不太受欢迎的书籍可能会在网站的其他部分使用（尽管对此没有详细说明）。

主要要点：

*   **数据来源：** 30 亿条 Goodreads 评论。
*   **目标：** 创建更好的图书推荐模型。
*   **用户界面：** 允许用户搜索和选择他们读过的书。
*   **推荐引擎：** 根据用户输入生成图书推荐。
*   **受欢迎程度过滤器：** 只有受欢迎的书籍才会被包含在核心推荐系统中。
*   **Goodreads 书架导入：** 提供导入 Goodreads 书架的选项，以简化书籍输入。

---

## 21. 3I/ATLAS彗星显示近日点爆发和径向非引力加速度

**原文标题**: 3I/ATLAS shows perihelion burst and radial-only non-gravitational acceleration

**原文链接**: [https://old.reddit.com/r/dataisbeautiful/comments/1oqfau8/3iatlas_shows_perihelion_burst_and_radialonly/](https://old.reddit.com/r/dataisbeautiful/comments/1oqfau8/3iatlas_shows_perihelion_burst_and_radialonly/)

无法访问文章链接。

---

## 22. 沉默的科学家：软件研究未能触达受众

**原文标题**: The Silent Scientist: When Software Research Fails to Reach Its Audience

**原文链接**: [https://cacm.acm.org/opinion/the-silent-scientist-when-software-research-fails-to-reach-its-audience/](https://cacm.acm.org/opinion/the-silent-scientist-when-software-research-fails-to-reach-its-audience/)

沉默的科学家：当软件研究未能触达受众时

本文《沉默的科学家：当软件研究未能触达受众时》探讨了软件研究领域内反复出现的担忧，即人们认为研究工作缺乏相关性和影响力。作者认为，讨论中一个关键的疏忽是对科学传播的重视不足。他们挑战了研究成果自然会通过发表找到受众的假设，并断言研究的影响力直接取决于其可及性。

文章强调了相关性的复杂性，它因不同的利益相关者群体和研究阶段而异。技术进步与以人为本的实证发现产生不同的共鸣，并且早期研究可能使教育工作者或其他研究人员受益，然后才能直接影响从业者。作者批评研究人员在研究过程的早期阶段没有充分地与目标受众互动，导致人为的问题空间和难以证明相关性。

核心论点是，有效的科学传播对于弥合研究与实践之间的差距至关重要。他们建议研究人员应通过各种渠道积极与从业者进行对话，例如博客文章、社交媒体讨论、研讨会和开源贡献。虽然承认学术界内部存在鼓励发表而非推广的系统性挑战，但作者鼓励研究人员扩大其传播工作，并借鉴其他具有成熟实施科学实践的科学领域。通过积极传播他们的研究结果，研究人员可以提高对其工作的认识、兴趣和理解，最终促进合作并增强软件研究的影响力。

---

## 23. 游戏设计很简单

**原文标题**: Game design is simple

**原文链接**: [https://www.raphkoster.com/2025/11/03/game-design-is-simple-actually/](https://www.raphkoster.com/2025/11/03/game-design-is-simple-actually/)

本文提出了一个理解游戏设计的“十二步计划”，重点关注其核心要素和原则。它首先将游戏设计中的“乐趣”重新定义为“精通问题”，并强调游戏应围绕解决问题展开。这些问题源于约束和规则，将玩具变成游戏就像为其发明一个目标一样简单。

不确定性是吸引玩家的关键，好的游戏问题应具有深度、不确定性，并适用于多种情况。游戏利用循环，即玩家反复遇到的问题。循环有两种类型：操作循环（与问题互动）和进展螺旋（一遍又一遍地拿起木棍，但每次情况都不相同）。玩家了解如何使用机制，并通过在不同情况下测试它来推断其运作方式。

反馈对于学习和改进至关重要，它需要玩家了解可用的行动、看到这些行动的影响，并知道状态改变是否有帮助。变化和升级，升级情境，以便可以测试、完善和放弃理论。节奏和平衡，包括改变强度并为玩家提供练习和接受测试的机会，至关重要。最后，游戏由链接或互连的循环组成，从而创建价值链或复杂的经济体系。

---

## 24. 仅一周时间，索尔顿海有毒尘埃即可引发肺部微生物群变化

**原文标题**: Toxic Salton Sea dust triggers changes in lung microbiome after just one week

**原文链接**: [https://phys.org/news/2025-10-toxic-salton-sea-triggers-lung.html](https://phys.org/news/2025-10-toxic-salton-sea-triggers-lung.html)

加州索尔顿海干涸粉尘可迅速改变小鼠肺部微生物群

---

## 25. 我正在制作一款小型RPG游戏，需要关于性能的反馈。

**原文标题**: I'm Making a Small RPG and I Need Feeback Regarding Performance

**原文链接**: [https://jslegenddev.substack.com/p/im-making-a-small-rpg-and-i-need](https://jslegenddev.substack.com/p/im-making-a-small-rpg-and-i-need)

无法访问文章链接。

---

## 26. 软件是工程学科的UFO学吗？

**原文标题**: Is Software the UFOlogy of Engineering Disciplines?

**原文链接**: [https://codemanship.wordpress.com/2025/11/07/is-software-the-ufology-of-engineering-disciplines/](https://codemanship.wordpress.com/2025/11/07/is-software-the-ufology-of-engineering-disciplines/)

本文认为，与更为成熟的工程学科相比，软件工程缺乏严谨的、基于证据的实践，其对轶事、小数据集和不可证伪的主张的依赖，使其类似于不明飞行物学。作者将不明飞行物研究和软件工程进行类比，强调了这两个领域如何经常优先考虑轶事证据和主观解释，而不是硬数据和可验证的结果。

作者以国会关于不明航空现象的听证会为例，将对证人证词的依赖与缺乏确凿的物证形成了对比。类似地，在软件方面，研究通常依赖于自我报告的数据，比如开发者声称实践TDD，但IDE活动表明并非如此。这导致了不确定的结论，并阻碍了坚实知识体系的发展。

作者强调了可证伪性在科学假设中的重要性，并批评了软件工程中提出不可检验的主张的倾向。在承认软件开发的复杂社会技术方面时，作者认为该学科甚至没有认真尝试采用更严谨、数据驱动的方法。

作者强调，大量可用数据（IDE操作、代码仓库、构建输出等）是一种浪费的机会。缺乏数据交换标准和对术语的共同理解进一步加剧了该领域的不成熟。作者最后呼吁采用更严格、基于证据的软件工程方法，倡导标准化数据收集和分析，以提高理解和可预测性。

---

## 27. 在以色列工作方面受压，微软要求员工举报违规行为。

**原文标题**: Pressured on Israel work, Microsoft asks employees to flag violations

**原文链接**: [https://www.detroitnews.com/story/business/2025/11/07/pressured-on-israel-work-microsoft-asks-employees-to-flag-violations/87144653007/](https://www.detroitnews.com/story/business/2025/11/07/pressured-on-israel-work-microsoft-asks-employees-to-flag-violations/87144653007/)

微软正在内部诚信门户网站中实施一项新的“可信技术审查”系统，允许员工提出对其技术使用的担忧，特别是关于人权方面的担忧。此前，有报道称以色列国防部，特别是8200部队，正在使用微软的Azure云服务存储巴勒斯坦平民的监控数据，引发了调查，促使了这一举措。

微软最初没有发现任何与以色列-哈马斯战争相关的滥用证据，但随后的调查证实了《卫报》和其他媒体的一些报道。因此，微软以违反公司服务条款为由，切断了向8200部队提供的特定云计算服务。

这些披露引发了多次抗议，主要来自“反对种族隔离的Azure”组织，他们要求微软切断与以色列政府的所有联系。一些参与这些抗议的员工因扰乱秩序的行为而被解雇。

新的审查系统旨在为员工提供一个安全且匿名的渠道来表达担忧。微软还计划加强其对需要进行人权尽职调查的业务的合同前审查流程。

文章还指出，亚马逊和谷歌等其他科技公司也面临着因与以色列签订的价值12亿美元的“Nimbus项目”合同而引发的类似员工抗议。《卫报》报道称，亚马逊和谷歌同意了以色列政府的某些要求，但两家公司均否认。另有报道称，微软失去Nimbus项目的部分原因是它不愿满足以色列的一些要求。

---

## 28. 分析表明宇宙的膨胀并未加速。

**原文标题**: Analysis indicates that the universe’s expansion is not accelerating

**原文链接**: [https://ras.ac.uk/news-and-press/research-highlights/universes-expansion-now-slowing-not-speeding](https://ras.ac.uk/news-and-press/research-highlights/universes-expansion-now-slowing-not-speeding)

一项发表在《皇家天文学会月刊》上的新研究挑战了长期以来关于宇宙膨胀因暗能量而加速的观点。由延世大学李永旭教授领导的研究人员发现证据表明，宇宙膨胀可能已经开始减速。

该研究重新审查了来自Ia型超新星的数据，Ia型超新星被认为是测量宇宙距离的“标准烛光”。他们发现这些超新星的前身星的年龄显著影响它们的亮度。年轻的恒星产生较暗的超新星，而年老的恒星产生较亮的超新星，这在距离测量中引入了系统性的偏差。

在校正了来自300个星系的大量样本中与年龄相关的偏差后，超新星数据不再与包含暗能量宇宙常数的标准ΛCDM宇宙学模型相符。相反，校正后的数据更符合暗能量光谱仪器（DESI）项目基于重子声学振荡（BAO）和宇宙微波背景（CMB）数据所支持的模型。

对校正后的超新星数据、BAO和CMB结果的综合分析表明，暗能量随时间减弱，宇宙目前处于减速膨胀状态，这与主流理论相悖。这一结论与仅基于BAO以及BAO+CMB分析的独立预测相一致。拥有强大数码相机的Vera C. Rubin天文台将通过提供更精确的超新星宿主星系年龄测量数据，为进一步测试这一新模型做出贡献。

---

## 29. 十年磨一剑，从网页开发者到数据库开发者

**原文标题**: From web developer to database developer in 10 years

**原文链接**: [https://notes.eatonphil.com/2025-02-15-from-web-developer-to-database-developer-in-10-years.html](https://notes.eatonphil.com/2025-02-15-from-web-developer-to-database-developer-in-10-years.html)

菲尔·伊顿的博文详细描述了他从网页开发者到数据库开发者这十年来的历程。最初专注于前端和服务器端网页开发，他认为数据结构和算法（DSA）与他的工作无关，因而避免接触。2020年出现的性能瓶颈让他接触了“Use The Index, Luke”，激发了他对数据库内部原理的兴趣，并最终构建了一个小型内存SQL数据库。

尽管缺乏正规的计算机科学教育，菲尔仍通过业余项目探索数据库和Raft实现。他与人共同创立了数据库公司TigerBeetle，专注于市场营销和社区，这提供了宝贵的学习经验。他还创建了Software Internals Discord和/r/databasedevelopment。

离开TigerBeetle后，菲尔很难找到数据库开发者的职位，经常被引导到云编排职位。他坚持了下来，投入时间于涉及Postgres和MySQL的个人项目，并创立了Software Internals读书会和NYC Systems Coffee Club。

最终，在四个月后，他收到了三个关于Postgres扩展的C和Rust开发职位邀请。他选择了EnterpriseDB，一家主要的Postgres贡献者，理由是其已建立的地位以及向经验丰富的工程师学习的机会。他强调，开发扩展可以深入了解Postgres内部原理。如今，在EnterpriseDB工作一年后，他很高兴能够回归到个人贡献，此前他在创业公司担任领导职务。

---

## 30. Kimi K2 思考，一个SOTA开源万亿参数推理模型

**原文标题**: Kimi K2 Thinking, a SOTA open-source trillion-parameter reasoning model

**原文链接**: [https://moonshotai.github.io/Kimi-K2/thinking.html](https://moonshotai.github.io/Kimi-K2/thinking.html)

文章介绍了 Kimi K2 Thinking，这是一个拥有万亿参数的先进开源推理模型。关键在于 Kimi K2 Thinking 代表了开源人工智能的重大进展，尤其是在推理能力方面。“万亿参数”的描述突显了其大规模和解决复杂问题的潜力。虽然文章非常简短，但暗示着该模型因其开源可访问性、先进的推理能力以及在开源社区中前所未有的规模而引人注目。 需要更多信息来了解该模型的具体架构、训练数据、基准和预期应用。

---

## 31. JermCAD：基于浏览器的CAD软件

**原文标题**: JermCAD: Browser-Based CAD Software

**原文链接**: [https://github.com/jeremyaboyd/jerm-cad](https://github.com/jeremyaboyd/jerm-cad)

JermCAD是一款基于浏览器的3D CAD模型渲染器，旨在通过使用YAML语法简化3D设计。 鉴于传统CAD软件的繁琐，开发者创建了JermCAD，允许用户在基于代码的环境中使用几何图元和布尔运算来定义3D模型。

主要功能包括：基于YAML的建模、支持多种形状类型（长方体、圆柱体、圆锥体、球体、圆环体、拉伸体）、布尔运算（并集、差集、交集）、可重用的参数化形状模板（称为“图章”）、用于保持一致性的属性引用、实时3D可视化以及用于3D打印的STL导出功能。它还支持Z轴向上或Y轴向上的坐标系、线框模式和可调节的渲染质量。

要开始使用，用户需要Node.js和npm。安装并运行应用程序后，用户可以在编辑器面板中编辑YAML，渲染模型，并将其导出为STL文件。该软件提供用于导航的基本相机控制。

YAML结构包括单位、公差和向上轴的设置，以及根级别参数、具有颜色和不透明度的材质，以及定义形状的实体。支持诸如中心、锚点和旋转之类的变换。“图章”允许使用带有参数的可重用组件，而属性引用允许元素之间的关系。布尔运算可以组合形状，“final”部分允许将所有可见网格合并为一个具有统一外观的实体。

---

## 32. 阿尔弗雷德·梅内泽斯密码学入门

**原文标题**: Cryptography 101 with Alfred Menezes

**原文链接**: [https://cryptography101.ca](https://cryptography101.ca)

Alfred Menezes 提供了一份全面的资源“密码学 101”，包含视频讲座、笔记和练习，涵盖应用密码学的各个方面。该资源包括 YouTube 课程以及未来日期的特定课程。

即将开设的课程包括：

*   **格基规约（2025 年 11 月）：** LLL 算法在密码分析中的介绍。
*   **Kyber 和 Dilithium（2024 年 8 月）：** 介绍基于格的 NIST 标准化量子安全密钥封装和签名方案。
*   **基于哈希的签名方案（2025 年 6 月）：** 侧重于使用哈希函数（如 LMS 和 SPHINCS+）的量子安全签名方案。
*   **基于格密码的数学原理（2025 年 1 月）：** 涵盖基于格密码的数学基础，例如 Kyber 和 Dilithium。
*   **应用密码学 101：构建模块（2024 年 11 月）：** 涵盖基本的密码学原语。
*   **应用密码学 101：实际部署（2025 年 4 月）：** 展示关于使用密码学原语保护大规模应用的案例研究。
*   **纠错码（2024 年 8 月）：** 提供代数纠错码的介绍。

该资源还包括教师材料。这表明这是一个结构化的教育项目，适合初学者和希望扩展其在应用密码学领域知识的人，并强烈强调现代和量子安全技术。

---

## 33. LLVM中的机器调度器 – 第二部分

**原文标题**: Machine Scheduler in LLVM – Part II

**原文链接**: [https://myhsu.xyz/llvm-machine-scheduler-2/](https://myhsu.xyz/llvm-machine-scheduler-2/)

本文深入探讨LLVM机器调度器的“盈利性检查”阶段，重点关注其如何通过考虑寄存器和资源压力来优化指令调度。主要目标是减少寄存器溢出并提高指令级并行性（ILP）。

**寄存器压力：** 调度器使用`PressureDiff`估算每条指令对寄存器压力的影响，该指标跟踪不同压力集（例如，标量、向量寄存器）中潜在的寄存器压力变化。调度器基于以下三个指标评估潜在的候选指令：

*   **超额压力：** 衡量超出已定义阈值的压力，从而过滤掉细微的波动。
*   **关键最大压力：** 将新的压力与调度区域中目前观察到的最大压力进行比较。
*   **当前最大压力：** 将新的压力与原始、未调度程序中的最大压力进行比较。

**资源压力：** 类似于寄存器压力，其旨在防止指令过度集中于特定的处理器资源（流水线）。目标是使资源占用率低于归一化的关键路径长度。

本文解释了LLVM如何使用延迟因子和资源因子来归一化资源占用率，这些因子基于发布宽度和每个处理器资源中的单元数量计算得出。然后，调度器优先考虑那些可以最大限度地减少资源占用率增加的候选指令，从而促进指令在可用流水线中更均匀地分布并增强ILP。

---

## 34. 纳斯达克100指数或将创下四月暴跌以来最差单周表现

**原文标题**: Nasdaq 100 set for worst week since April meltdown

**原文链接**: [https://fortune.com/2025/11/07/nasdaq-100-worst-week-since-april-bear-market-correction/](https://fortune.com/2025/11/07/nasdaq-100-worst-week-since-april-bear-market-correction/)

纳斯达克100指数受华尔街避险情绪和人工智能股票回调影响，有望创下自四月以来最糟糕的一周。由于消费者信心跌至三年低点，标普500指数也将结束其连续三周的上涨势头。对人工智能股票估值过高的担忧，以及华尔街高管对市场泡沫的警告，都加剧了下跌。

由于政府停摆阻碍了经济数据的发布，投资者依赖私人数据，这使得市场容易受到波动的影响。一项调查显示，劳动力市场解体是交易的最大风险。虽然官方的美国工资报告不可用，但私人数据显示劳动力市场正在降温，这可能会影响美联储的降息计划。

尽管目前市场低迷，但一些分析师认为经济仍处于上升轨道。美联储的关注点将是劳动力市场的健康状况，预计他们将实施降息以防止就业疲软。美国股票基金已连续八周出现资金流入，但现金吸引了最大部分。

尽管市场正在经历一段疲软期，但高盛认为风险平衡仍然有利于多头。

---

## 35. 我们构建了一个秒速启动的云GPU笔记本。

**原文标题**: We built a cloud GPU notebook that boots in seconds

**原文链接**: [https://modal.com/blog/notebooks-internals](https://modal.com/blog/notebooks-internals)

Modal联合创始人兼工程师Eric Zhang详细介绍了Modal Notebooks背后的工程设计。Modal Notebooks是一个基于云的Jupyter Notebook环境，以启动速度快、实时协作（尤其适用于GPU密集型工作负载）为特色。核心创新在于Modal Sandboxes，这是一种安全隔离的容器环境，针对包括AI任务在内的高性能计算进行了优化。这些Sandboxes使用“modal-kernelshim”守护程序将Jupyter协议消息转换为HTTP调用，从而实现带流式输出的远程内核访问。

为了实现近乎瞬时的启动，Modal采用了延迟加载容器镜像。它并非预先解压整个镜像，而是仅加载轻量级元数据索引，并通过分层缓存系统按需获取文件内容。这与跨共享CPU和GPU池的智能调度相结合，实现了高效的资源分配和空闲内核的自动暂停，从而最大限度地降低了成本。

Modal还通过VolumeFS解决了持久存储需求，VolumeFS是一个构建在分布式网络上的全局可访问的FUSE文件系统。这确保了跨区域的数据本地性和可用性，从而实现了无缝的工作流程转换。

实时协作由Rushlight（一个操作转换库）促进，通过Redis Streams和CodeMirror集成管理并发编辑。该系统将编辑状态和执行状态分离，并利用S3 Express One Zone存储更大的输出。Modal还支持协作环境中的Jupyter Widgets。

最后，Modal Notebooks集成了现代编辑器功能，例如与Pyright集成的Language Server Protocol (LSP)用于完成和高亮显示，Ruff用于自动格式化，甚至还使用了Claude 4和内部托管模型提供的AI驱动的编辑建议。这些技术的结合提供了一个无缝、高性能的开发环境，可通过用户友好的界面访问。

---

## 36. Y Combinator 孵化的创业公司将精神涣散带入开发者 IDE

**原文标题**: Y Combinator Startup brings brainrot to developers' IDEs

**原文链接**: [https://www.cladlabs.ai](https://www.cladlabs.ai)

这篇文章似乎是一个虚构的、由 Y Combinator 支持的创业公司针对开发者设计的模拟着陆页。其核心前提是，这款新产品以某种方式将“脑死亡”（大概是指像 TikTok 这样令人上瘾、毫无效率的内容）的元素直接整合到开发者的集成开发环境 (IDE) 中。

该着陆页重点突出：

*   **Y Combinator 支持：** 表明该产品已获得知名创业加速器的投资和认可。
*   **“脑死亡”集成：** 明确提及将令人上瘾、浪费时间的内容（如 TikTok）的元素引入 IDE。这很可能是讽刺，暗示该产品会分散注意力而不是提高生产力。
*   **现金返还（或类似奖励）：** 暗示存在激励计划，可能会奖励用户使用该工具，甚至在使用令人分心的内容时也能获得奖励。
*   **适用于 macOS：** 指示目标平台。
*   **演示：** 提供产品的演示。
*   **“高效工程师”的使用：** 戏谑地声称，领先机构的高效工程师正在使用这种注入“脑死亡”的 IDE。这很可能是一种讽刺性说法，突出了该产品荒谬的前提。

本质上，这篇文章是对技术在软件开发等专业环境中可能造成干扰和效率低下的潜在情况的讽刺性评论。它幽默地嘲讽了将各种功能（通常是表面上的）集成到现有工具中的趋势，即使这些功能有损其核心目的。

---

## 37. 要么减肥，要么失业，外海工人被告知

**原文标题**: Lose weight or lose your jobs, offshore workers told

**原文链接**: [https://www.bbc.com/news/articles/cx274xp00zxo](https://www.bbc.com/news/articles/cx274xp00zxo)

北海油田工人被告知需在2026年11月前减重，否则可能失业。行业机构英国离岸能源公司(OEUK)正实施新的体重限制，规定离岸工人体重不得超过124.7公斤（19.5英石），原因是出于对救援直升机绞车限重的安全考虑。目前的最大绞车负荷，包括工人、救援人员、担架和装备在内，为249公斤。

OEUK估计目前有超过2200名工人超出此限制，这是一个令人担忧的问题，因为自2008年以来，离岸工人的平均体重已显著增加。 海事和海岸警卫队 (MCA) 警告称，救援绞车无法安全地吊起体重较重的人员。

虽然OEUK希望避免失业，并鼓励雇主支持工人达到新要求，但他们承认，在最坏的情况下，失业是有可能发生的。 现场健身房和健康食品等支持措施已经到位。

一位成功减肥的离岸工人菲尔·佩里担心这项政策会导致失业。 Unite工会也对体格健壮但体型偏大、超出限制的个人表示担忧，并致力于为他们提供支持。 新政策的强制实施日期为2026年11月1日。

---

## 38. 运营盗版流媒体网站的教训

**原文标题**: Lessons from Growing a Piracy Streaming Site

**原文链接**: [https://prison.josh.mn/lessons](https://prison.josh.mn/lessons)

本文详细介绍了运营非法体育流媒体网站HeheStreams所获得的经验教训，重点在于通过口碑营销获取和留住客户。作者出于道德考量以及对更高质量用户的需求，避免了传统广告，而是强调建立信任和提供卓越的客户服务。

关键策略包括：通过弃用“noreply@”邮箱进行个性化沟通，通过签到和调查进行主动引导，对服务问题进行诚实透明的沟通，即使在充分使用后也提供慷慨的退款政策，直接参与流失用户的沟通，在适当情况下推荐竞争对手，并专注于提供高质量的体育流媒体。作者的定价高于竞争对手，以吸引那些重视该服务为“投资”的精通技术的用户。

主要的增长技巧包括使用Reddit的API来识别相关对话，即用户正在寻找官方体育流媒体服务的替代方案。然后，HeheStreams用户被激励以透明的方式用他们的推荐链接来推荐该服务。

尽管该风险投资是非法的，并最终被创意联盟/美国电影协会强制收购，但作者强调了以客户为中心的经验教训的持久价值。他们成功地将这些原则应用于随后的合法生态旅游业务，表明信任和个性化服务虽然难以扩展，但对于小型、诚实的企业来说是有效的。

---

## 39. FreeBSD上的Swift预览

**原文标题**: Swift on FreeBSD Preview

**原文链接**: [https://forums.swift.org/t/swift-on-freebsd-preview/83064](https://forums.swift.org/t/swift-on-freebsd-preview/83064)

本文宣布推出适用于 FreeBSD 14.3+ 的 Swift 工具链预览版软件包，可供下载。它允许用户在 x86_64 FreeBSD 14 系统上编译 Swift 程序。要使用此软件包，用户需要安装 zlib-ng、python3、sqlite3、libuuid 和 curl 等依赖项。

文章承认编译器仍在开发中，并列出了几个已知问题，包括 Thread Sanitizer 问题、LLDB 表达式求值问题、SwiftPM 命令插件问题、C++ 互操作问题、C 库错误地作为“Glibc”导入的问题，以及 lld/lldb 缺失依赖项的问题。每个问题都链接了特定的 GitHub issue。

未来计划包括调查 aarch64 支持，并使该软件包与 FreeBSD 14 的所有次要版本兼容。鼓励用户测试该软件包，报告他们发现的任何新错误，并为移植工作做出贡献。

---

## 40. 克劳德宕机了

**原文标题**: Claude Is Down

**原文链接**: [https://status.claude.com/incidents/tgtw1sqs9ths](https://status.claude.com/incidents/tgtw1sqs9ths)

2025年11月7日，UTC时间约14:29起，Claude在多个平台（包括claude.ai、platform.claude.com（原console.anthropic.com）以及Claude API (api.anthropic.com)）上，对Claude 4、4.5 Sonnet和4.5 Haiku的请求出现错误率升高的情况。Anthropic对此问题进行了调查，并于UTC时间14:29报告了此问题。修复方案已实施，并于UTC时间约14:44开始监测结果。到UTC时间14:56，该事件已解决。该问题涉及API、Claude.ai和Anthropic Console上针对Sonnet和Haiku的请求错误。

---

## 41. 死亡框架理论

**原文标题**: Dead Framework Theory

**原文链接**: [https://aifoc.us/dead-framework-theory/](https://aifoc.us/dead-framework-theory/)

保罗·金兰的“死框架理论”认为，React已成为主导的 Web 开发平台，这归因于 LLM 驱动的自增强循环。LLM 在现有的 Web 数据上进行训练，这些数据严重偏向 React，导致它们默认输出 React 代码。反过来，这巩固了 React 的主导地位，因为开发者使用 LLM 生成的代码，进一步增加了其在训练数据中的存在。

作者认为，即使技术上更优越的新框架、库和 Web 平台特性也面临着巨大的采用障碍。它们必须克服 LLM 训练数据的偏差（存在 12-18 个月的滞后），说服工具创建者修改其系统提示，并构建一个全面的库生态系统。此外，旨在取代框架特性的新 Web 平台 API 往往会失败，因为开发者坚持使用 LLM 和 React 生态系统中已经根深蒂固的熟悉框架模式。

金兰强调了在 Web 上构建的不同群体，并认为网站的增长来自使用 LLM 的个人和小型团队，他们不太可能了解或关心新的平台特性。

作者的结论是，React 的主导地位不是因为其技术优越性，而是其统计上的普遍性。为了克服这一点，新的框架需要采取策略来进入 LLM 训练数据和开发者的思维。平台开发者应该专注于用户空间无法构建的基本功能。工具创建者需要默认输出 React，以捕捉当前的市场需求。文章以乐观的视角结束：随着生态系统变得同质化，重点将从开发者体验转移到用户体验，激励工具输出更好的用户体验。

---

## 42. 远古时效法750周年：将历史冻结在1189年的中世纪法律

**原文标题**: Time Immemorial turns 750: The Medieval law that froze history at 1189

**原文链接**: [https://www.ianvisits.co.uk/articles/time-immemorial-turns-750-the-medieval-law-that-froze-history-at-1189-84893/](https://www.ianvisits.co.uk/articles/time-immemorial-turns-750-the-medieval-law-that-froze-history-at-1189-84893/)

本文纪念1275年威斯敏斯特法令颁布750周年，该法令确立了“远古时期”的法律概念。 虽然该术语经常被非正式使用，但它具有特定的法律含义：指1189年9月3日之前的任何时期。

该法令由爱德华一世颁布，旨在简化法律程序和税收。 在此之前，从祖父那里传承下来的口述历史可以作为土地纠纷的证据。 该法令有效地使超过祖父母证词的口述历史无效，要求官方文件来证明土地所有权和相关的纳税义务。 其理论是，在1275年，仍然有可能有人活着听到他们祖父的口头证词。

选择1189年，即狮心王理查（爱德华一世的高曾叔祖父）加冕的一年，被认为是巩固国王权威的刻意之举，通过引用他的血统并强调从口头传统到书面记录的转变。 中世纪历史学家理查德·巴伯将此行为描述为“主要是口头文化与书写至上的世界之间的分水岭”。

虽然《威斯敏斯特法令》没有使用“远古时期”一词，但后来在1832年的《时效法案》中正式确定，该法案将其定义为“人们记忆中不存在相反情况的时间”，并引入了确定土地权利的固定期限，从而无需证明远古时期。 本质上，《威斯敏斯特法令》将法律历史冻结在1189年，要求对早于该年的任何主张提供证明。

---

## 43. Show HN: 开源测试时扩散实现，可在24GB GPU上运行

**原文标题**: Show HN: OSS implementation of Test Time Diffusion that runs on a 24gb GPU

**原文链接**: [https://github.com/eamag/MMU-RAG-competition](https://github.com/eamag/MMU-RAG-competition)

TTD-RAG 是一个开源实现，用于 MMU-RAG 竞赛的测试时扩散（TTD）框架。它将报告生成概念化为一个迭代的“去噪”过程，通过有针对性的搜索、综合和修订来完善初步草稿。这种方法擅长复杂的推理任务。

主要特性包括 TTD 框架、基于检索的报告级去噪、用于增强规划和综合的组件式自演化、使用 vLLM 和 Qwen 模型的高性能服务，以及符合竞赛规则（动态和静态评估）。

该系统分三个阶段运行：规划和初步起草、迭代搜索和去噪，以及最终报告生成。它使用噪声草稿来引导搜索查询，检索和重排文档，综合答案，并迭代地修改草稿。

技术栈包括 FastAPI、vLLM、用于生成的 Qwen 模型、重排模型、FineWeb Search API 和 Docker 容器化。

README 提供了入门指南，包括配置环境变量、使用 Docker Compose 构建和运行 Docker 容器，以及使用提供的 `local_test.py` 脚本测试实现。它还描述了用于健康检查、动态评估 (/run) 和静态评估 (/evaluate) 的 API 端点。最后，它概述了将 Docker 镜像推送到竞赛 ECR 存储库以进行提交的步骤。

---

## 44. 联邦调查局试图揭露archive.is的所有者

**原文标题**: FBI tries to unmask owner of archive.is

**原文链接**: [https://www.heise.de/en/news/Archive-today-FBI-Demands-Data-from-Provider-Tucows-11066346.html](https://www.heise.de/en/news/Archive-today-FBI-Demands-Data-from-Provider-Tucows-11066346.html)

FBI试图查明archive.is网站所有者身份，该网站常被用于保存可能被删除或更改的网页。他们已向加拿大互联网服务提供商Tucows发出传票，要求提供有关该域名注册人的信息。

文章强调了archive.is的争议性。虽然它可以用于正当目的，如存档重要信息和提供证据，但它也经常被用于保存被认为有害或非法的内容，包括极端主义材料、人肉搜索信息和侵犯版权的内容。这使其成为执法部门和版权所有者的目标。

Tucows已将传票通知archive.is，并正在等待进一步指示。文章指出，archive.is历来抵制删除请求和透露其所有者身份，以某种匿名方式运营，并在过去几年中更换了不同的托管服务提供商。这张传票可能代表着识别并可能起诉所有者或破坏该网站运营的行动的重大升级。

FBI对archive.is的兴趣可能源于它被用于保存刑事调查中的证据或防止有害内容的传播。传票的结果以及archive.is的回应可能会对在线匿名、信息自由以及保存在线内容和防止有害材料传播之间的平衡产生影响。

---

## 45. 大型语言模型编码了问题的难易程度。

**原文标题**: LLMs encode how difficult problems are

**原文链接**: [https://arxiv.org/abs/2510.18147](https://arxiv.org/abs/2510.18147)

这篇题为“大型语言模型编码问题的难易程度”的论文，研究了大型语言模型（LLMs）是否在内部以一种与人类感知相符的方式表示问题难度。作者William Lugoloobi和Chris Russell，通过在60个LLM的各层和token位置上训练线性探针，并使用Easy2HardBench的数学和编程子集作为评估数据，对此进行了探索。

他们的主要发现是：人类标注的问题难度可以在LLMs内部被强线性解码，并且表现出模型大小的缩放性。然而，直接从LLM性能估计的难度较弱，且缩放性较差。有趣的是，基于人类标签将LLMs引导至与“较容易”问题相关的表示，可以减少幻觉并提高准确性。

此外，在使用基于强化学习输出的梯度偏好（GRPO）在Qwen2.5-Math-1.5B上进行训练时，人类难度探针增强并与测试准确率呈正相关。相反，LLM难度探针在训练过程中退化并与性能呈负相关。这表明，与LLM导出的难度估计相比，人类注释为强化学习提供了一个更稳定和有用的难度信号，而LLM导出的难度估计会随着模型的改进而变得具有误导性。

作者总结说，LLMs确实编码了问题难度，但与直接从LLM性能中得出的难度信号相比，人类注释提供了更优越的难度信号。他们发布了代码和评估脚本，以鼓励进一步研究。

---

## 46. 人们何时偏好组合而非继承？

**原文标题**: When did people favor composition over inheritance?

**原文链接**: [https://www.sicpers.info/2025/11/when-did-people-favor-composition-over-inheritance/](https://www.sicpers.info/2025/11/when-did-people-favor-composition-over-inheritance/)

Graham的文章深入探讨了软件设计中“组合优于继承”的原则，质疑其作为一种思想终结者的陈词滥调的地位。他将其起源追溯到“四人帮”的《设计模式》一书，该书提倡对象组合作为一种“黑盒”复用方法，并将其与继承的“白盒”方法进行对比。

文章认为，该原则的适用性具有历史局限性。虽然Smalltalk由于其对象可见性，体现了组合和继承之间的明显区别，但像Java这样的语言允许对子类型进行受控可见性。相反，Smalltalk和Python的自省特性模糊了界限，使组合对象可以访问其组成部分的内部结构。

一个关键点是，继承是静态的且在编译时定义的，使其更容易使用但更难更改。组合虽然需要更多的手动编码，但通过允许交换组成对象并避免实现依赖性，提供了更大的运行时灵活性。

文章将该原则与Barbara Liskov关于子类型的工作联系起来，强调当类型不是真正的子类型时，组合提供了自由，避免了接口兼容性的约束。Liskov早期的工作也提出了替代方法，例如在类型关系最初不明确时进行“分组”。

最终，作者认为“组合优于继承”不是唯一的选择。第一类过程（如lambda）提供了另一种选择，表明该格言的不完整性，并强调了基于特定上下文考虑各种设计方法的重要性。

---

## 47. 初创公司探索海洋储电

**原文标题**: A startup’s quest to store electricity in the ocean

**原文链接**: [https://techcrunch.com/2025/10/22/one-startups-quest-to-store-electricity-in-the-ocean/](https://techcrunch.com/2025/10/22/one-startups-quest-to-store-electricity-in-the-ocean/)

大型能源公司(Sizable Energy)由曼纽尔·奥菲耶罗共同创立，旨在通过在海洋中创建“抽水蓄能”系统来彻底改变能源存储。受传统抽水蓄能水库的启发，Sizable 提出使用两个由带有涡轮机的管道连接的柔性水库：一个漂浮在水面，另一个位于海底。

该系统的工作原理是利用多余的能量将底部水库的超咸水抽到顶部。当需要能量时，更重、更咸的水流回底部，旋转涡轮机以发电。这种方法旨在克服陆基抽水蓄能的局限性，陆基抽水蓄能需要特定的地形。

Sizable 已筹集了 800 万美元的资金来开发该技术。通过将抽水蓄能转移到海上，该公司希望大规模生产标准化系统，从而降低成本和部署复杂性。他们已经测试了小型模型，并计划在 2026 年之前部署商业项目。

预计每个涡轮机将产生 6-7 兆瓦的电力，更深的位置提供更大的存储潜力。Sizable 旨在实现每千瓦时 20 欧元的储能成本，远低于目前电网规模电池的成本。该技术可以与海上风电场相结合，以进一步降低成本。该公司认为，其解决方案对于整合可再生能源和创建更具弹性的电网至关重要，因为电池和陆基抽水蓄能等传统方法是不够的。

---

## 48. 不幸的推手：世界尚未为自主软件做好准备

**原文标题**: Agents of misfortune: The world isn't ready for autonomous software

**原文链接**: [https://www.theregister.com/2025/11/06/agents_of_misfortune_the_world/](https://www.theregister.com/2025/11/06/agents_of_misfortune_the_world/)

托马斯·克莱本的《不幸的代理人》认为，人工智能的代理时代，即软件代表用户自主行动的时代，面临着技术之外的重大障碍。文章以亚马逊和Perplexity就自动购买发生的冲突为例，突出了围绕人工智能代理的法律模糊性、竞争压力和哲学分歧。

克莱本挑战了人工智能代理只是替代人类劳动的观点，指出技术和法律上的差异导致了成本差距，并引发了关于数据使用和服务条款的问题。他认为，像亚马逊这样对其市场拥有重大控制权的公司，对可能使其失去中介地位并扰乱其客户关系和数据访问的人工智能代理持谨慎态度。

文章还提出了对人工智能代理错误责任以及缺乏明确规则管理其与第三方服务交互的担忧。克莱本认为，人工智能行业正在遵循颠覆性技术的模式：优先考虑市场主导地位，而不是寻求许可或解决潜在危害。

最后，文章指出并非所有人都对人工智能充满热情，并提到了Klarna重新雇用客户服务人员以及一个关于餐厅服务机器人的轶事，该机器人虽然有帮助，但也造成了问题并减慢了运营速度。作者认为，科技行业对人工智能代理的乐观愿景可能与面向人类系统的现实不符。

---

## 49. 鲜味 3.0

**原文标题**: Umami 3.0

**原文链接**: [https://github.com/umami-software/umami/releases/tag/v3.0.0](https://github.com/umami-software/umami/releases/tag/v3.0.0)

Umami v3 发布，注重改善用户体验并扩展跟踪功能。主要更新包括：重新设计的 UI，导航更简便，且报告有单独页面；增强的筛选功能，允许使用应用筛选器的可共享 URL；引入了分段和队列，用于高级用户分组和分析。

新增的跟踪元素“链接”和“像素”能够衡量点击率以及来自外部来源（如电子邮件或非附属网站）的流量。 专门的管理页面简化了用户、网站和团队管理。

虽然此版本具有显著改进，但计划中的“看板”功能（可自定义的仪表板）仍在开发中，将在未来的更新中发布。

值得注意的是，Umami v3不再支持 MySQL，需要迁移到 PostgreSQL。 此版本包含对 Next.js 和 Prisma 的更新。 Umami 团队感谢在此版本中做出贡献的个人。

---

## 50. 以色列试图影响ChatGPT和Claude的回复

**原文标题**: Israel is attempting to influence ChatGPT and Claude responses

**原文链接**: [https://www.haaretz.com/israel-news/security-aviation/2025-11-06/ty-article-magazine/.premium/ai-hasbara-israel-pours-millions-into-influencing-u-s-evangelicals-in-churches-chatgpt/0000019a-540e-db4c-a5fb-dfafea590000](https://www.haaretz.com/israel-news/security-aviation/2025-11-06/ty-article-magazine/.premium/ai-hasbara-israel-pours-millions-into-influencing-u-s-evangelicals-in-churches-chatgpt/0000019a-540e-db4c-a5fb-dfafea590000)

据报道，以色列正在投入大量资源，以影响 ChatGPT 和 Claude 等人工智能语言模型生成的回应，尤其侧重于塑造有关以色列和以巴冲突的叙事。这项名为“AI 公关”（公关指旨在解释和捍卫以色列的公共外交努力）的行动，涉及投入数百万美元用于旨在向主要受众，尤其是美国福音派基督徒，展示以色列正面形象的项目。

文章详细描述了这些举措如何试图训练人工智能模型，使其在与冲突相关的历史事件、地缘政治问题和时事方面提供亲以色列的观点。这包括塑造人工智能的回应，以反映以色列对耶路撒冷历史、定居点和冲突原因等话题的叙事。

文章提出的担忧是，这种操纵可能导致这些日益具有影响力的人工智能平台将有偏见或误导性的信息作为客观事实呈现。这可能会进一步加剧现有的偏见，并可能加剧围绕以巴冲突的紧张局势，尤其是在那些深受这些人工智能聊天机器人影响的弱势群体中。文章还强调了操纵人工智能模型的伦理考量，以及此类努力可能破坏对这些技术的信任。

---

## 51. 带有注释的HTML幻灯片

**原文标题**: HTML Slides with notes

**原文链接**: [https://nbd.neocities.org/slidepresentation/Slide%20presentation%20about%20slides](https://nbd.neocities.org/slidepresentation/Slide%20presentation%20about%20slides)

本文介绍了一种使用最少JavaScript创建带有同步注释的HTML幻灯片的方法。作者基于Dave Gaur的“minslides”概念，增加了在单独窗口中显示注释的功能。

核心思想是使用带有“slide”和“slidenote”类的`<div>`元素来定义幻灯片及其对应的注释。CSS用于确保幻灯片填满屏幕。然后使用JavaScript代码来处理导航和同步。

该脚本首先使用`getElementsByClassName`识别幻灯片元素。然后创建一个配对数组，其中每对包含一个幻灯片及其关联的注释（如果不存在注释，则为幻灯片本身）。`scrollIntoView()`方法用于在幻灯片/注释之间切换。

注释功能涉及一个`viewSlides`变量来确定应显示幻灯片还是注释。键盘事件（j、k用于导航，n用于注释切换）用于控制演示。为了在窗口之间同步，使用`BroadcastChannel`进行消息传递，确保幻灯片和注释在多个浏览器窗口中协调一致。

文章随后描述了缩小和精简JavaScript代码以减小尺寸的步骤，包括使用按位异或来切换视图模式和缩短变量名。最终精简的代码作为一个紧凑而实用的解决方案呈现。

---

## 52. 文档嵌入上的Word2Vec风格向量算术

**原文标题**: Word2Vec-style vector arithmetic on docs embeddings

**原文链接**: [https://technicalwriting.dev/embeddings/arithmetic/index.html](https://technicalwriting.dev/embeddings/arithmetic/index.html)

本文探讨了传统上用于单个词语的word2vec风格向量算术是否可以应用于技术文档的文档嵌入。作者使用EmbeddingGemma模型进行实验以测试这个概念。

进行了两个主要实验：

1.  **相同主题，不同领域：** `Testing Your Database`（Supabase） - `supabase` + `angular`。预期结果是接近“在Angular中测试”的向量。
2.  **不同主题，相同领域：** `Testing Your Database`（Supabase） - `testing` + `vectors`。预期结果是接近“Supabase中的向量”的向量。

每个实验运行两次：一次使用默认任务类型，一次使用自定义任务类型。验证方法包括使用余弦相似度将结果向量与来自各种文档来源的向量进行比较。

结果表明，word2vec风格的算术**可以**用于文档嵌入，尤其是在使用自定义任务类型时。在“相同主题，不同领域”的实验中，自定义任务类型正确地将“Testing”和“Testing Services”（Angular）识别为最相似的。在“不同主题，相同领域”的实验中，无论任务类型设置如何，“Vector Columns”（Supabase）始终被识别为最相似的。作者得出结论，理解和正确设置任务类型对于获得准确结果非常重要。本文还包括实验中使用的源代码（`experiments.py`）和数据（`data.json`）。

---

## 53. 伊提纳路-E – 古代道路数字地图集

**原文标题**: Itiner-E – The Digital Atlas of Ancient Roads

**原文链接**: [https://itiner-e.org/](https://itiner-e.org/)

Itiner-E 是一个致力于绘制古罗马道路的数字地图集项目。其目标是创建关于罗马帝国境内道路最全面且可自由访问的数字数据集。该项目强调其协作性质，由学者社区共同构建和维护。Itiner-E 允许用户查看、查询和下载道路数据，使其成为研究和探索罗马道路网络的宝贵资源。

---

## 54. 我对C++20协程的教程和理解 (2021)

**原文标题**: My tutorial and take on C++20 coroutines (2021)

**原文链接**: [https://www.scs.stanford.edu/~dm/blog/c++-coroutines.html](https://www.scs.stanford.edu/~dm/blog/c++-coroutines.html)

本文旨在提供一份关于 C++20 协程的教程和个人见解，力求阐明现有解释中常见的困惑之处。作者因现有资源的不足而感到沮丧，故深入研究规范，以提供更易于理解的解释。

其核心概念是，协程是可以暂停执行并在以后恢复的函数，与传统的基于大量回调的方法相比，可以实现更易于管理的事件驱动代码。关键机制是 `co_await` 运算符，它保存协程的状态，创建一个可调用对象（类似于延续）以恢复执行，并调用可等待对象上的一个方法。

本教程强调，C++20 协程附带大量的样板代码，包括定义一个具有嵌套 `R::promise_type` 的返回对象类型 (`R`)。此 promise 类型对于管理协程的状态和处理协程句柄 (`std::coroutine_handle<>`) 至关重要，该句柄就像指向堆分配的协程状态的指针。

作者提供了实际示例，演示了如何使用 `co_await` 在函数之间切换控制权，以及如何在返回对象中存储协程句柄。这些示例还强调了使用 `h.destroy()` 手动销毁协程句柄以防止内存泄漏的重要性。本教程还进一步解释了awaiter中 `await_ready`、`await_suspend` 和 `await_resume` 的作用，以及如何在协程之间来回传递数据。

---

## 55. 关于Fil-C的说明

**原文标题**: A Note on Fil-C

**原文链接**: [https://graydon2.dreamwidth.org/320265.html](https://graydon2.dreamwidth.org/320265.html)

这篇题为“关于Fil-C的注释”的短文，似乎是在告知读者他们已被选中完成验证码。文中指出，这种选择是“半随机的”，旨在验证用户的请求。 指示很明确：完成验证码并提交。 除了验证码要求之外，没有提供关于“Fil-C”本身的任何其他背景或信息，因此无法确定文章的更大目的或主题。 唯一的重点是验证码要求。

---

## 56. OpenTelemetry: 摆脱可观测性联盟的逃生舱

**原文标题**: OpenTelemetry: Escape Hatch from the Observability Cartel

**原文链接**: [https://oneuptime.com/blog/post/2025-11-03-opentelemetry-escape-from-observability-cartel/view](https://oneuptime.com/blog/post/2025-11-03-opentelemetry-escape-from-observability-cartel/view)

本文认为，OpenTelemetry (OTel) 提供了一个从云优先供应商主导的可观测性市场寡头垄断中“逃生”的途径。这些供应商常常使用专有代理、数据格式和定价结构来锁定用户。OTel 标准化了遥测数据的收集、描述和路由，从而可以轻松地将数据迁移到各种后端，无论是自托管、新供应商还是两者的混合。

OTel 的主要优势包括：

*   **厂商无关的工具化：** 标准化的 SDK 和语义约定减少了工具化的 churn，允许跨不同后端重复使用相同的 schema。
*   **Collector 作为控制平面：** OTel Collector 将控制权交给用户，从而实现任意到任意的管道、路由、采样和部署灵活性。
*   **多接收器架构：** 支持混合架构，例如用于迁移的双写、使用开源堆栈的热/热冗余以及区域数据自主性。
*   **成本控制：** 开放且高效的 OTLP 格式允许压缩、存储和供应商更换，而无需迁移成本。
*   **可移植性和自由：** OTel 提倡以可移植性为先的理念，并由社区驱动开发和 CNCF 治理。

本文建议逐步采用 OTel，首先从一项服务开始，然后在所有地方引入 collector，最后尝试使用辅助后端。通过采用 OTel，组织可以避免供应商锁定，并确保遥测数据的可移植性，从而使可观测性成为基于价值而不是被迫依赖的选择。OneUptime 销售副总裁 Nawaz Dhandala 强调了 OneUptime 对 OpenTelemetry 的原生支持及其对开源的承诺。

---

## 57. 二十年未破解的文件格式

**原文标题**: A File Format Uncracked for 20 Years

**原文链接**: [https://landaire.net/a-file-format-uncracked-for-20-years/](https://landaire.net/a-file-format-uncracked-for-20-years/)

本文详细介绍了作者对初代Xbox游戏《细胞分裂》(2002)中使用的“.lin”文件格式进行逆向工程的努力。尽管该游戏使用了虚幻引擎2，但这种特定的文件格式在20年来一直未被破解。作者出于探索剪辑内容的愿望，开始研究游戏光盘的文件结构。

用于存储地图数据的“.lin”文件包含zlib压缩块，并且似乎有一个目录表。最初的目标是根据文件表的偏移量和长度信息提取单独的文件，但文件表中的偏移量被证明是不正确的，指向文件实际大小之外的位置。

为了克服这个问题，作者使用Xbox模拟器xemu对游戏的读文件程序进行了逆向工程。这涉及识别负责创建和读取文件以及解压缩数据的函数。结果发现游戏使用的“seek”函数是一个空操作，这意味着必须线性读取数据，类似于磁带驱动器。

作者随后发现，游戏加载ini文件以识别要从“.lin”文件中使用的“.unr”文件。

---

## 58. 概型的几何 [pdf]

**原文标题**: The Geometry of Schemes [pdf]

**原文链接**: [https://webhomes.maths.ed.ac.uk/~v1ranick/papers/eisenbudharris.pdf](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/eisenbudharris.pdf)

由于存在无法读取的字符和编码问题，我无法从提供的PDF内容中提取有意义的文本。因此，我无法提供文章《概型几何》的摘要。

---

## 59. 苹果私有计算云的开源实现

**原文标题**: Open Source Implementation of Apple's Private Compute Cloud

**原文链接**: [https://github.com/openpcc/openpcc](https://github.com/openpcc/openpcc)

OpenPCC是一个开源框架，旨在复制苹果的Private Cloud Compute的功能，实现可证明的私有AI推理。它允许用户在不暴露敏感数据（如提示词、输出或日志）的情况下运行AI模型，利用加密、硬件证明和不可链接的请求来确保隐私。该项目旨在建立一个透明的、社区治理的AI数据隐私标准。

Confident Security正在基于OpenPCC标准开发一项名为CONFSEC的托管服务。

OpenPCC项目包括一个Go客户端（带有C、Python和JavaScript封装）以及用于测试的内存服务。一个单独的仓库（confidentsecurity/confidentcompute）托管着计算节点实现。该文档提供了如何使用Go客户端的示例，包括配置API密钥、定义身份策略以及使用OpenAI API格式发出推理请求。

该文档详细介绍了使用Go工具“mage”运行内存服务和测试请求的本地开发设置。这允许开发者使用OpenPCC库并为其开发做出贡献。OpenPCC的核心目标是提供一种可审计且可自托管的替代方案，以取代闭源私有计算解决方案。

---

## 60. Canonical 在 Go 中的安全 Starlark

**原文标题**: Canonical's Secure Starlark in Go

**原文链接**: [https://github.com/canonical/starlark](https://github.com/canonical/starlark)

Canonical 维护了一个安全、修补过的 Go 语言版 Google Starlark，旨在作为大部分可直接替换的方案，并增加了安全约束。 Starlark 是 Python 的一种方言，用作配置语言，以其简洁性、可读性和并行执行能力而闻名。

Canonical 的版本通过 `MemSafe`、`CPUSafe`、`TimeSafe` 和 `IOSafe` 等特性增强了 Starlark，以限制资源使用。它还包括一个安全测试框架、内存使用估计、上下文集成、溢出保护、可能失败的迭代器、递归限制，并防止线程无法取消。虽然大部分兼容，但也包含一些微不足道的破坏性更改。

该文档涵盖了语言规范、Go 实现、安全约束和破坏性更改。该项目提供了一个可通过命令行访问的解释器、一个 REPL (读取-求值-打印循环)，以及在 Go 程序中嵌入的能力。

欢迎贡献，但应事先讨论以符合 Starlark 网站的语言目标并防止重复工作。贡献者需要签署 Canonical 的贡献者许可协议 (CLA)。虽然目前可能存在破坏性更改，但该项目旨在 Bazel 团队最终确定版本 1 语言规范后实现接口稳定性。该项目支持最新的四个 Go 版本。

---

## 61. Show HN: 在 VSCode 中使用你的编码代理进行动态代码和反馈演练

**原文标题**: Show HN: Dynamic code and feedback walkthroughs with your coding Agent in VSCode

**原文链接**: [https://www.intraview.ai/hn-demo](https://www.intraview.ai/hn-demo)

Cy推出Intraview：一款旨在增强AI辅助开发时代代码理解和协作的VS Code扩展。Intraview解决的核心问题是，维护复杂软件系统的思维模型越来越困难，尤其是在AI代理生成代码日益普及的情况下。该扩展旨在提高软件开发生命周期中的理解和一致性。

Intraview的工作原理是允许用户创建代码的视觉“导览”，充当指导反馈会话。它通过本地消息控制协议 (MCP) 与现有 AI 代理（如 Claude 或 GPT5-codex）集成，使代理能够为其生成的代码提供上下文和解释。这有助于开发人员理解代码的工作原理，从而促进更好的设计决策和改进。

Cy强调，Intraview并非旨在将编码商品化，而是旨在使其更易于访问和更令人愉快。他重视塑造、测试和改进解决方案的过程，并相信Intraview可以帮助实现这一目标。安全是首要任务，仅进行最少的外部调用，用于匿名使用遥测，以便确定功能优先级。

他提供了一个演示视频，展示了如何将 Intraview 与开源存储库 (Plotly JS) 结合使用，以学习如何构建新的可视化效果并向 AI 代理提供反馈。该视频以原始、未经润色的演示形式呈现。他鼓励对工具的开发提供反馈和协作。

---

## 62. 白宫排除对人工智能的救助，因泡沫担忧加剧

**原文标题**: White House rules out bailout for AI as bubble fears grow

**原文链接**: [https://www.telegraph.co.uk/business/2025/11/07/white-house-rules-out-bailout-for-ai-as-bubble-fears-grow/](https://www.telegraph.co.uk/business/2025/11/07/white-house-rules-out-bailout-for-ai-as-bubble-fears-grow/)

无法访问文章链接。

---

## 63. 电子游戏可以改变现实。

**原文标题**: Video games can alter reality

**原文链接**: [https://particle.scitech.org.au/tech/video-games-can-alter-reality/](https://particle.scitech.org.au/tech/video-games-can-alter-reality/)

这篇文章，题为“电子游戏可以改变现实”，发表在“没你想的那么无聊”栏目下，属于更大的“科技101：编程”类别。这表明文章旨在呈现科技，特别是其与编程的联系中，一个可能令人惊讶或引人入胜的方面。标题本身暗示了电子游戏的重大影响，暗示它们具有影响或改变对现实的认知的能力。

虽然在没有完整文章的情况下无法得知确切内容，但我们可以推断文章很可能会探讨电子游戏超越简单娱乐的方式。它可能讨论：

*   **电子游戏的沉浸式本质：** 它们如何创造令人信服的虚拟世界，从而影响玩家的情绪、思想和行为。
*   **游戏的认知效应：** 由于游戏习惯，感知、注意力、问题解决能力和空间推理可能发生的改变。
*   **技术方面：** 用于创建逼真和引人入胜的游戏体验的底层代码和编程技术。
*   **哲学意义：** 探索虚拟与现实之间日益模糊的界限，以及对身份和社会互动的影响。

这篇文章很可能将电子游戏定位为不仅仅是一种休闲活动，而是一种强大的技术力量，可能对我们体验和理解周围世界的方式产生变革性影响。“编程”子类别表明文章将涉及创建这些具有影响力的虚拟现实的技术方面。

---

## 64. Show HN: 将和弦视为旗帜 – 在MuseScore上呈现顶级作曲家的视觉和谐

**原文标题**: Show HN: See chords as flags – Visual harmony of top composers on musescore

**原文链接**: [https://rawl.rocks/](https://rawl.rocks/)

这个“Show HN”帖子介绍了一个名为“视觉音乐理论”的工具，它将乐谱中的和弦以旗帜的形式进行可视化呈现。该项目似乎利用了乐谱分享和查看平台 MuseScore 的数据，来分析和可视化乐曲，特别是顶级作曲家作品中的和声结构。通过将和弦表示为旗帜，该工具旨在提供一种更直观、更具视觉吸引力的方式来理解音乐理论以及各种作品中使用的和声进行。简短的描述表明该工具使用 JavaScript，并且需要启用 JavaScript 才能运行。 本质上，它是一种视觉学习辅助工具，旨在通过展示乐曲的和声流程来简化和加强对音乐理论的理解。

---

## 65. Ratatui – 应用展示

**原文标题**: Ratatui – App Showcase

**原文链接**: [https://ratatui.rs/showcase/apps/](https://ratatui.rs/showcase/apps/)

本文展示了一系列基于终端的应用程序 (TUIs)，这些应用使用 Ratatui 构建，Ratatui 是一个用于在终端中创建用户界面的 Rust 库。 这些应用程序涵盖了广泛的功能，展示了 Ratatui 的多功能性。

应用程序类别包括：

*   **系统和网络实用工具：** `atuin` (shell 历史记录替换), `bandwhich` (网络利用率监视器), `bottom` (系统监视器), `trippy` (网络诊断工具)。
*   **文件管理：** `joshuto`, `xplr`, `yazi` (文件管理器), `dua` (磁盘空间分析器)。
*   **开发工具：** `binsider` (二进制分析), `fzf-make` (make 目标的模糊查找器), `gitui` (Git TUI), `slumber` (HTTP/REST 客户端), `steer` (AI 编码助手)。
*   **数据库工具：** `rainfrog` (数据库交互), `yozefu` (Kafka 集群探索)。
*   **效率工具：** `taskwarrior-tui` (Taskwarrior 界面), `rucola` (markdown 笔记管理器), `television` (模糊查找器)。
*   **API 探索：** `openapi-tui` (OpenAPI 文档查看器)。
*   **趣味/娱乐：** `crossword` (填字游戏), `minesweep-rs` (扫雷)。
*   **其他：** `csvlens` (CSV 查看器), `material` (终端颜色调色板), `oatmeal` (LLM 聊天应用程序), `oha` (Web 应用程序负载测试器), `oxker` (Docker 容器管理), `scope-tui` (示波器/矢量示波器/频谱分析仪)。

该展示强调了这些应用程序在各种任务中的实用性和效率，所有这些都在终端环境中完成。

---

## 66. Auraphone: A simple app to collect people's info at events

**原文标题**: Auraphone: A simple app to collect people's info at events

**原文链接**: [https://andrewarrow.dev/2025/11/simple-app-collect-peoples-info-at-events/](https://andrewarrow.dev/2025/11/simple-app-collect-peoples-info-at-events/)

安德鲁正在开发一款名为“Auraphone”的移动应用，该应用旨在通过利用蓝牙交换联系信息，从而简化活动中的人际交往。该应用允许用户自定义个人资料，选择他们想要分享的信息（姓名、照片、社交媒体等）。当用户参加活动时，该应用会自动发现并连接到附近的其它用户，交换个人资料信息。这消除了手动交换联系方式的需要，并提供了活动中遇到的所有人的数字记录。

该应用采用客户端-服务器（中心-外设）蓝牙模型运行，手机同时充当服务器和客户端，防止连接冲突。数据通过“特性”（PROFILE_CHAR 和 PHOTO_CHAR）交换，作者将这些特性比作端点。该应用优先考虑高效的数据传输，缓存图像并实施冷却期，以避免冗余连接。

安德鲁最初尝试在 Go 语言中模拟蓝牙低功耗 (BLE) 协议栈以进行测试 (auraphone-blue)，但发现使用 iOS 和 Android 设备进行实际测试以及详细的日志记录对于修复错误更有效。

由于 iOS 蓝牙限制，该应用要求用户主动在前台运行它。然而，安德鲁设想用户在交谈时拿着手机。Auraphone 在 iOS App Store 上提供，Android APK 文件可在 auraphone.apk 获取。他们目前正在 BLANKSPACES Culver City 测试该应用，并寻求关于其在真实人际交往场景中的功能和可用性的反馈。

---

## 67. 一个纯右值不是临时对象

**原文标题**: A prvalue is not a temporary

**原文链接**: [https://blog.knatten.org/2025/10/31/a-prvalue-is-not-a-temporary/](https://blog.knatten.org/2025/10/31/a-prvalue-is-not-a-temporary/)

生成摘要时出错

---

## 68. ICC 弃用 Microsoft 365，转用 openDesk

**原文标题**: ICC ditches Microsoft 365 for openDesk

**原文链接**: [https://www.binnenlandsbestuur.nl/digitaal/internationaal-strafhof-neemt-afscheid-van-microsoft-365](https://www.binnenlandsbestuur.nl/digitaal/internationaal-strafhof-neemt-afscheid-van-microsoft-365)

生成摘要时出错

---

## 69. How I am deeply integrating Emacs

**原文标题**: How I am deeply integrating Emacs

**原文链接**: [https://joshblais.com/blog/how-i-am-deeply-integrating-emacs/](https://joshblais.com/blog/how-i-am-deeply-integrating-emacs/)

生成摘要时出错

---

## 70. Show HN: qqqa – A fast, stateless LLM-powered assistant for your shell

**原文标题**: Show HN: qqqa – A fast, stateless LLM-powered assistant for your shell

**原文链接**: [https://github.com/matisojka/qqqa](https://github.com/matisojka/qqqa)

生成摘要时出错

---

## 71. The Parallel Search API

**原文标题**: The Parallel Search API

**原文链接**: [https://parallel.ai/blog/introducing-parallel-search](https://parallel.ai/blog/introducing-parallel-search)

生成摘要时出错

---

## 72. Scientists find ways to boost memory in aging brains

**原文标题**: Scientists find ways to boost memory in aging brains

**原文链接**: [https://news.vt.edu/articles/2025/10/cals-jarome-improving-memory.html](https://news.vt.edu/articles/2025/10/cals-jarome-improving-memory.html)

生成摘要时出错

---

## 73. Anti-Drug Unit Officially Shut Down by DOJ

**原文标题**: Anti-Drug Unit Officially Shut Down by DOJ

**原文链接**: [https://www.bloomberg.com/news/newsletters/2025-11-07/reagan-era-crime-unit-officially-shut-down-by-doj](https://www.bloomberg.com/news/newsletters/2025-11-07/reagan-era-crime-unit-officially-shut-down-by-doj)

生成摘要时出错

---

## 74. Sponge: A community-driven open-source Minecraft: Java Edition modding platform

**原文标题**: Sponge: A community-driven open-source Minecraft: Java Edition modding platform

**原文链接**: [https://spongepowered.org/](https://spongepowered.org/)

生成摘要时出错

---

## 75. Solarpunk is happening in Africa

**原文标题**: Solarpunk is happening in Africa

**原文链接**: [https://climatedrift.substack.com/p/why-solarpunk-is-already-happening](https://climatedrift.substack.com/p/why-solarpunk-is-already-happening)

生成摘要时出错

---

## 76. $40M 3D printing factory open for business on Guam, will produce parts for Navy

**原文标题**: $40M 3D printing factory open for business on Guam, will produce parts for Navy

**原文链接**: [https://www.guampdn.com/news/40m-3d-printing-factory-now-open-for-business-on-guam-will-produce-parts-of-navy/article_0bff0888-b760-4eb4-868a-9bcb46eb507f.html](https://www.guampdn.com/news/40m-3d-printing-factory-now-open-for-business-on-guam-will-produce-parts-of-navy/article_0bff0888-b760-4eb4-868a-9bcb46eb507f.html)

生成摘要时出错

---

## 77. Supply chain attacks are exploiting our assumptions

**原文标题**: Supply chain attacks are exploiting our assumptions

**原文链接**: [https://blog.trailofbits.com/2025/09/24/supply-chain-attacks-are-exploiting-our-assumptions/](https://blog.trailofbits.com/2025/09/24/supply-chain-attacks-are-exploiting-our-assumptions/)

生成摘要时出错

---

## 78. The surprising countries pulling off fast clean energy transitions

**原文标题**: The surprising countries pulling off fast clean energy transitions

**原文链接**: [https://www.cnn.com/2025/11/07/climate/solar-wind-renewables-transition-global-pakistan-hungary-chile](https://www.cnn.com/2025/11/07/climate/solar-wind-renewables-transition-global-pakistan-hungary-chile)

生成摘要时出错

---

## 79. Filnix Fil-C Nix

**原文标题**: Filnix Fil-C Nix

**原文链接**: [https://github.com/mbrock/filnix](https://github.com/mbrock/filnix)

生成摘要时出错

---

## 80. I Use Typst Now

**原文标题**: I Use Typst Now

**原文链接**: [https://www.christopherbiscardi.com/i-use-typst-now](https://www.christopherbiscardi.com/i-use-typst-now)

生成摘要时出错

---

## 81. Eating stinging nettles

**原文标题**: Eating stinging nettles

**原文链接**: [https://rachel.blog/2018/04/29/eating-stinging-nettles/](https://rachel.blog/2018/04/29/eating-stinging-nettles/)

生成摘要时出错

---

## 82. Show HN: TabPFN-2.5 – SOTA foundation model for tabular data

**原文标题**: Show HN: TabPFN-2.5 – SOTA foundation model for tabular data

**原文链接**: [https://priorlabs.ai/technical-reports/tabpfn-2-5-model-report](https://priorlabs.ai/technical-reports/tabpfn-2-5-model-report)

生成摘要时出错

---

## 83. The labour and resource use requirements of a good life for all

**原文标题**: The labour and resource use requirements of a good life for all

**原文链接**: [https://arxiv.org/abs/2411.06337](https://arxiv.org/abs/2411.06337)

生成摘要时出错

---

## 84. GT – Experimental multiplexing tensor framework for distributed GPU computing

**原文标题**: GT – Experimental multiplexing tensor framework for distributed GPU computing

**原文链接**: [https://github.com/bwasti/gt](https://github.com/bwasti/gt)

生成摘要时出错

---

## 85. UPS plane crashes near Louisville airport

**原文标题**: UPS plane crashes near Louisville airport

**原文链接**: [https://avherald.com/h?article=52f5748f&opt=0](https://avherald.com/h?article=52f5748f&opt=0)

生成摘要时出错

---

## 86. The Basic Laws of Human Stupidity (1987) [pdf]

**原文标题**: The Basic Laws of Human Stupidity (1987) [pdf]

**原文链接**: [https://gandalf.fee.urv.cat/professors/AntonioQuesada/Curs1920/Cipolla_laws.pdf](https://gandalf.fee.urv.cat/professors/AntonioQuesada/Curs1920/Cipolla_laws.pdf)

生成摘要时出错

---

## 87. Show HN: Ambient light sensor control of keyboard and screen brightness in Linux

**原文标题**: Show HN: Ambient light sensor control of keyboard and screen brightness in Linux

**原文链接**: [https://github.com/donjajo/als-led-backlight](https://github.com/donjajo/als-led-backlight)

生成摘要时出错

---

## 88. IKEA launches new smart home range with 21 Matter-compatible products

**原文标题**: IKEA launches new smart home range with 21 Matter-compatible products

**原文链接**: [https://www.ikea.com/global/en/newsroom/retail/the-new-smart-home-from-ikea-matter-compatible-251106/](https://www.ikea.com/global/en/newsroom/retail/the-new-smart-home-from-ikea-matter-compatible-251106/)

生成摘要时出错

---

## 89. Jeffrey Epstein Helped Israel Sell a Surveillance State to Côte D'Ivoire: Leaks

**原文标题**: Jeffrey Epstein Helped Israel Sell a Surveillance State to Côte D'Ivoire: Leaks

**原文链接**: [https://www.dropsitenews.com/p/jeffrey-epstein-israel-surveillance-state-cote-d-ivoire-ehud-barak-leaked-emails](https://www.dropsitenews.com/p/jeffrey-epstein-israel-surveillance-state-cote-d-ivoire-ehud-barak-leaked-emails)

生成摘要时出错

---

## 90. New gel restores dental enamel and could revolutionise tooth repair

**原文标题**: New gel restores dental enamel and could revolutionise tooth repair

**原文链接**: [https://www.nottingham.ac.uk/news/new-gel-restores-dental-enamel-and-could-revolutionise-tooth-repair](https://www.nottingham.ac.uk/news/new-gel-restores-dental-enamel-and-could-revolutionise-tooth-repair)

生成摘要时出错

---

## 91. I analyzed the lineups at the most popular nightclubs

**原文标题**: I analyzed the lineups at the most popular nightclubs

**原文链接**: [https://dev.karltryggvason.com/how-i-analyzed-the-lineups-at-the-worlds-most-popular-nightclubs/](https://dev.karltryggvason.com/how-i-analyzed-the-lineups-at-the-worlds-most-popular-nightclubs/)

生成摘要时出错

---

## 92. I want a good parallel language [video]

**原文标题**: I want a good parallel language [video]

**原文链接**: [https://www.youtube.com/watch?v=0-eViUyPwso](https://www.youtube.com/watch?v=0-eViUyPwso)

生成摘要时出错

---

## 93. Mathematical exploration and discovery at scale

**原文标题**: Mathematical exploration and discovery at scale

**原文链接**: [https://terrytao.wordpress.com/2025/11/05/mathematical-exploration-and-discovery-at-scale/](https://terrytao.wordpress.com/2025/11/05/mathematical-exploration-and-discovery-at-scale/)

生成摘要时出错

---

## 94. The Learning Loop and LLMs

**原文标题**: The Learning Loop and LLMs

**原文链接**: [https://martinfowler.com/articles/llm-learning-loop.html](https://martinfowler.com/articles/llm-learning-loop.html)

生成摘要时出错

---

## 95. I may have found a way to spot U.S. at-sea strikes before they're announced

**原文标题**: I may have found a way to spot U.S. at-sea strikes before they're announced

**原文链接**: [https://old.reddit.com/r/OSINT/comments/1opjjyv/i_may_have_found_a_way_to_spot_us_atsea_strikes/](https://old.reddit.com/r/OSINT/comments/1opjjyv/i_may_have_found_a_way_to_spot_us_atsea_strikes/)

生成摘要时出错

---

## 96. Dillo, a multi-platform graphical web browser

**原文标题**: Dillo, a multi-platform graphical web browser

**原文链接**: [https://github.com/dillo-browser/dillo](https://github.com/dillo-browser/dillo)

生成摘要时出错

---

## 97. Royal Navy installs quantum clock in robotic submarine

**原文标题**: Royal Navy installs quantum clock in robotic submarine

**原文链接**: [https://newatlas.com/military/royal-navy-quantum-clock-submarine/](https://newatlas.com/military/royal-navy-quantum-clock-submarine/)

生成摘要时出错

---

## 98. How often does Python allocate?

**原文标题**: How often does Python allocate?

**原文链接**: [https://zackoverflow.dev/writing/how-often-does-python-allocate/](https://zackoverflow.dev/writing/how-often-does-python-allocate/)

生成摘要时出错

---

## 99. The Pandemic Stress Test

**原文标题**: The Pandemic Stress Test

**原文链接**: [https://brajeshwar.com/2025/the-pandemic-stress-test/](https://brajeshwar.com/2025/the-pandemic-stress-test/)

生成摘要时出错

---

## 100. Absurd Workflows: Durable Execution with Just Postgres

**原文标题**: Absurd Workflows: Durable Execution with Just Postgres

**原文链接**: [https://lucumr.pocoo.org/2025/11/3/absurd-workflows/](https://lucumr.pocoo.org/2025/11/3/absurd-workflows/)

生成摘要时出错

---

