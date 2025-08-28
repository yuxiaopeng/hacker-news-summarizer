# Hacker News 热门文章摘要 (2025-08-28)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 如何在树莓派上安装TrueNAS

**原文标题**: How to Install TrueNAS on a Raspberry Pi

**原文链接**: [https://www.jeffgeerling.com/blog/2025/how-install-truenas-on-raspberry-pi](https://www.jeffgeerling.com/blog/2025/how-install-truenas-on-raspberry-pi)

本文详细介绍了如何在树莓派 5 上安装 TrueNAS，这是一种网络附加存储 (NAS) 操作系统，得益于社区创建的 TrueNAS Arm 架构分支。作者 Jeff Geerling 概述了该过程，强调了挑战和局限性。

一个重要的障碍是树莓派上缺乏原生 UEFI 支持。本文指导用户使用 NumberOneGit 的 rpi5-uefi 分支启用 UEFI，这涉及更新 EEPROM 和配置 UEFI 引导加载程序。

下一步包括下载 Arm 版 TrueNAS ISO 镜像，将其写入 USB 驱动器，并从中启动树莓派 5。 TrueNAS 安装程序会引导用户将操作系统安装到另一个 USB 驱动器（或其他存储设备）上。作者指出，首次启动可能会遇到问题，例如“ix-etc”服务失败，并提供了故障排除步骤。

作者讨论了树莓派 5 上 UEFI 实现的局限性。目前，风扇控制、CSI/DSI 连接、GPIO 和内置以太网端口等功能无法正常工作，需要使用 USB 以太网适配器等变通方法。文章还提到了将 RP1 支持向上游推进到 Linux 内核以解决这些问题的努力。

作者还探讨了将 TrueNAS 与 Homelabs Pi Storage 服务器等硬件项目一起使用，但注意到与 UEFI 实现的关于多个 PCIe 设备的限制相关的兼容性问题。他建议使用单用途 HAT 或 SATA 控制器进行直接磁盘连接。

最终，由于在树莓派 5 上运行 TrueNAS 的当前局限性，作者建议使用更高端的 Arm 硬件或 x86 服务器以获得最佳 TrueNAS 性能，但也承认这种方法是一个有趣的 learning exercise。

---

## 2. 任何东西，只要使用不当，都能变成消息队列（2023）

**原文标题**: Anything can be a message queue if you use it wrongly enough (2023)

**原文链接**: [https://xeiaso.net/blog/anything-message-queue](https://xeiaso.net/blog/anything-message-queue)

如果使用不当，任何东西都可以成为消息队列（2023）" 这篇文章幽默地指出，如果实施不当或使用不当，任何数据存储或通信机制都可以被强行用作消息队列。核心思想是，消息队列专门为组件之间的异步通信和解耦而设计，提供诸如保证交付、持久性和消息排序等功能。但是，如果您滥用不为此目的设计的工具，则可以有效地（但效果很差）模拟消息队列。

内容中出现的 "正在确认你是不是机器人！加载中...请稍等，我们需要在继续之前检查您的连接安全性。" 可能是反机器人保护的一种形式。这进一步支持了标题的隐含信息：如果您不适当地对待网站的访问机制（例如，未经许可或未正确处理机器人检测进行抓取），您将遇到旨在排队您的请求并评估您的合法性的措施，从而有效地使Web服务器的身份验证过程充当临时消息队列。

这篇文章可能讨论了人们可能如何意外或故意地滥用数据库、文件系统，甚至简单的API来模拟消息队列的例子，从而导致性能问题、数据丢失和其他问题。它可能通过强调使用正确的工具来完成工作的重要性，突出专用消息队列解决方案相对于实施不佳的替代方案的优势来结束。

---

## 3. Mosh（移动终端）

**原文标题**: Mosh (Mobile Shell)

**原文链接**: [https://mosh.org](https://mosh.org)

Mosh (移动Shell) 是一种稳健且响应迅速的交互式终端会话工具，可替代 SSH，尤其适用于 Wi-Fi、蜂窝网络和长途连接等不可靠网络。它是一款免费软件，可在包括 GNU/Linux、macOS、Android 和 iOS 在内的多个平台上使用。

主要功能包括：

*   **漫游：** 当用户切换网络（Wi-Fi 到 LTE 等）时，Mosh 会自动重新连接，而不会像 SSH 那样丢失连接。
*   **对间歇性连接的弹性：** 连接可在睡眠周期和临时网络中断期间保持。
*   **智能本地回显：** Mosh 即使在网络延迟的情况下，也能即时响应输入、删除和行编辑，并在不可靠的连接上自适应地对预测进行下划线标记。
*   **安全性：** 使用 SSH 进行身份验证，并使用 AES-128 加密通过 UDP 进行数据传输。不需要特权代码或守护进程。
*   **UTF-8 支持：** 内置的 UTF-8 终端模拟器解决了在其他终端和 SSH 中发现的 Unicode 错误。
*   **响应性：** 基于 UDP 的协议能优雅地处理数据包丢失，防止缓冲区溢出，并确保 Control-C 始终有效。

本文详细介绍了 Mosh 如何使用 UDP 上的状态同步协议 (SSP) 来同步客户端和服务器之间的屏幕状态。这实现了高效的更新和漫游。

最近的新闻重点介绍了具有新功能、错误修复和平台支持的版本。提供了适用于各种操作系统的安装说明。

---

## 4. OpenAI 和 Anthropic 在推理上赔钱吗？

**原文标题**: Are OpenAI and Anthropic Losing Money on Inference?

**原文链接**: [https://martinalderson.com/posts/are-openai-and-anthropic-really-losing-money-on-inference/](https://martinalderson.com/posts/are-openai-and-anthropic-really-losing-money-on-inference/)

本文挑战了人工智能推理是不可持续的资金黑洞的说法，特别关注输入处理和输出生成之间的成本差异。作者基于DeepSeek R1架构和零售H100 GPU租用价格进行了一项“草稿纸估算”分析。

核心论点是输入处理比输出生成便宜得多。作者估计，使用一个假设的72个H100集群，输入处理的成本约为每百万token 0.003美元，而输出生成的成本约为每百万token 3.08美元——相差一千倍。这种差异源于输入token的并行处理与输出token的顺序生成。

这种成本不对称性极大地影响了各种人工智能应用的盈利能力。涉及大量输入和少量输出的用例，例如代码助手分析整个代码库，利润很高。相反，像视频生成这样的应用，需要从少量输入中产生大量输出，成本很高。

作者分析了不同的用户计划（ChatGPT Pro、Claude Code Max）和API定价，发现存在大量的溢价和高毛利率，表明人工智能推理可能非常有利可图，尤其是对于特定的应用。他们认为，“人工智能成本高得不可持续”的说法可能通过抑制竞争和投资来服务于现有企业的利益。文章警告不要过度炒作成本，并将此与云计算的早期阶段以及随后超大规模企业的统治相提并论。关键在于，通过高效的架构和对输入密集型工作负载的关注，人工智能推理可能出人意料地经济实惠且有利可图。

---

## 5. 人工智能会取代人类思考吗？手动写作和编程的理由

**原文标题**: Will AI Replace Human Thinking? The Case for Writing and Coding Manually

**原文链接**: [https://www.ssp.sh/brain/will-ai-replace-humans/](https://www.ssp.sh/brain/will-ai-replace-humans/)

AI会取代人类思考吗？手写代码的理由

本文《AI会取代人类思考吗？手写代码的理由》反对过度依赖人工智能进行写作和编码等创造性任务。作者西蒙·斯帕蒂认为，虽然人工智能工具在短期内可以提高生产力，尤其是在自动完成等领域，但长期依赖会导致批判性思维、学习能力和原创性的下降。

作者通过引用保罗·格雷厄姆、内森·鲍、泰德·乔亚、吴恩达、哈里·德莱、杰森·弗里德、大卫·佩雷尔和埃兹拉·克莱恩等专家的观点来支持他的论点，他们强调了手动技能培养的重要性，人工智能生成内容可能缺乏灵魂，以及个人经验和深入研究的不可替代的价值。

斯帕蒂承认自己也使用人工智能工具，但他提倡有意识地使用，以保持独立思考和学习的能力。他认为，仅仅依靠人工智能来进行架构决策或内容创作会导致错误，并丧失独特的人类洞察力。他相信，在人工智能生成的“垃圾内容”充斥的世界里，那些继续磨练写作和编码技能的人将会看到巨大的回报。

文章最后探讨了Klarna和Duolingo等公司最初拥抱人工智能优先的方法，但后来因质量下降而退缩的例子。总而言之，作者强调了在利用人工智能的好处与保持培养创造力、批判性思维和真正的人际关系的重要技能之间取得平衡的重要性。

---

## 6. PinePhone Pro [GNU/Linux智能手机] 已停产

**原文标题**: PinePhone Pro [GNU/Linux smartphone] has been discontinued

**原文链接**: [https://social.treehouse.systems/@pine64/115027515081143369](https://social.treehouse.systems/@pine64/115027515081143369)

PINE64开发的GNU/Linux智能手机PinePhone Pro已停产。该信息来自PINE64社区在其Treehouse Mastodon账号上分享的更新。Mastodon平台在其网页浏览器版本中需要JavaScript才能运行，但用户也可以选择适用于其各自平台的专用Mastodon应用程序。

---

## 7. 为了可维护性而优化——Gleam 在 Strand 公司的生产环境中的应用

**原文标题**: Optimising for maintainability – Gleam in production at Strand

**原文链接**: [https://gleam.run/case-studies/strand/](https://gleam.run/case-studies/strand/)

Strand营销机构选择函数式编程语言Gleam构建关键的财务管理系统。面对有限的开发资源和日益增长的应用程序复杂性，他们优先考虑可维护性、可靠性和可扩展性。Gleam的稳健性、现代特性、对BEAM生态系统（Erlang虚拟机）的访问以及卓越的开发者体验给他们留下了深刻的印象。

Gleam的安全特性，结合BEAM的容错性，提供了一个健壮的系统，单个服务故障不会导致整个应用程序崩溃。Strand欣赏Gleam的简洁性和实用性，使其易于学习和让新开发者上手，同时仍然可以访问强大的语言特性和丰富的库。开发者工具，包括有用的错误消息和快速的构建时间，进一步提升了开发体验。

Strand逐步采用Gleam，从小型服务开始，并在他们获得信心后扩大其作用。结果是积极的：零Gleam相关的崩溃，以及一个易于理解和使用的可维护代码库，即使在长时间不活动后也是如此。该团队强调Gleam提供的安心感，使他们能够专注于其他优先事项，因为他们知道该系统将可靠地运行而无需持续维护。Strand的经验表明，对于寻求构建健壮且可维护应用程序的公司来说，Gleam是一个可行且有益的选择。

---

## 8. GAN的数学原理 (2020)

**原文标题**: GAN Math (2020)

**原文链接**: [https://jaketae.github.io/study/gan-math/](https://jaketae.github.io/study/gan-math/)

本文深入探讨生成对抗网络(GANs)的数学基础，重点关注Ian Goodfellow提出的原始GAN框架。它解释了GANs如何利用生成器(G)和判别器(D)之间的对抗关系来学习数据的潜在分布。

本文首先定义了关键符号，如真实数据(x)、潜在向量(z)、生成数据(G(z))，以及判别器对真实和虚假数据的评估(D(x)和D(G(z)))。然后阐述了判别器和生成器的损失函数的动机。判别器的损失基于正确识别真实和虚假数据，而生成器的损失基于欺骗判别器。

作者随后引入二元交叉熵作为使用的“误差”函数，并将其应用于生成器和判别器的损失函数。Goodfellow提出的GAN目标的极小极大公式被提出，突出了训练过程的对抗性。文章解释了为什么在实践中使用单独的损失函数，强调了-log(D(G(z)))比log(1 - D(G(z)))更陡峭的梯度，以便更快地改进生成器。

文章随后详细介绍了优化过程，解释了如何通过最大化价值函数V(G, D)来训练判别器。推导出了最优判别器D*(x)。类似地，训练生成器涉及在插入最优判别器后最小化V(G, D*)。通过巧妙地使用对数和库尔贝克-莱布勒散度进行操作，价值函数可以用詹森-香农散度表示。结论是，最小化V(G, D)等同于最小化数据分布和生成分布之间的JS散度，这意味着生成器应该学会模仿真实数据分布。

---

## 9. 美国军人应享有维修权

**原文标题**: American military service members deserve the right to repair

**原文链接**: [https://www.militarytimes.com/opinion/2025/07/11/why-service-members-deserve-the-right-to-repair/](https://www.militarytimes.com/opinion/2025/07/11/why-service-members-deserve-the-right-to-repair/)

退役中校辛迪·塞拉诺·罗伯茨支持美国军方的“维修权”立法，她以自己在伊拉克期间一台发电机损坏，危及阵亡士兵妥善照料的经历为例证。她强调，私营公司施加的现有限制阻碍了士兵对军事装备进行即使是最基本的维修，导致延误、成本增加，并可能危及生命。

罗伯茨强调了《国防授权法案》(NDAA)中对维修权改革的两党支持，特别提到了由参议员伊丽莎白·沃伦和蒂姆·希希倡导的《战士维修权法案》。她认为，允许军人在现场维修自己的装备可以提高任务准备就绪程度，减少对昂贵承包商的依赖，并最终提高作战人员的安全。

文章强调，维持费用可能占武器系统生命周期成本的大部分，限制军事人员进行维修会导致成本虚高和缺乏透明度。此外，授权士兵修理自己的装备可以培养一种适应性和自力更生的文化，这与灌输给新兵的价值观相符。罗伯茨最后敦促国会，特别是众议院军事委员会的领导人，如众议员迈克·罗杰斯，将军事维修权条款纳入NDAA。

---

## 10. 龙虾编程语言

**原文标题**: The Lobster Programming Language

**原文链接**: [https://www.strlen.com/lobster/](https://www.strlen.com/lobster/)

Lobster是一种静态类型编程语言，专为游戏开发而设计，旨在静态类型优势、编译时内存管理和轻量级、对开发者友好的语法之间取得平衡。它是开源的（Apache v2），并采用“开箱即用”的方式来支持图形应用程序。

主要功能包括：具有流敏感类型推断的静态类型、编译时引用计数、轻量级代码块/匿名函数、向量运算、统一重载与动态分派、不可变结构体以及无GIL的多线程模型。它使用类似于Python的基于缩进的语法，并包含C风格的元素。

Lobster可以使用其JIT编译器直接运行，也可以编译为C++以获得优化性能。它提供了一个图形调试器、动态代码加载，并为轻松部署而设计。它的性能明显快于Python和Lua，并且内存效率很高。该引擎是可移植的，目标平台包括Windows、Linux、Mac OS X、iOS、Android和WebAssembly（按成熟度排序），并为OpenGL、GLSL着色器、通过FreeType实现的精确文本渲染、统一的输入系统以及简单的声音系统提供高级接口。它附带预构建的库，用于常见的任务，如A*寻路和GUI。

本文展示了该语言的语法、类型推断以及使用继承创建自定义数据类型的能力。它还提供了一个通过Lobster的API使用OpenGL绘制Sierpinski三角形的示例。其中包含指向文档、GitHub存储库和社区频道的链接。

---

## 11. 重要的机器学习公式

**原文标题**: Important machine learning equations

**原文链接**: [https://chizkidd.github.io//2025/05/30/machine-learning-key-math-eqns/](https://chizkidd.github.io//2025/05/30/machine-learning-key-math-eqns/)

本文是一份关于机器学习（ML）底层基本数学方程的综合指南。它涵盖了从概率和线性代数等基础概念到扩散模型和注意力机制等高级技术的广泛主题。

本文首先介绍概率和信息论，解释了贝叶斯定理、熵、联合/条件概率、Kullback-Leibler散度和交叉熵，并提供了Python实现。然后深入探讨线性代数，详细介绍了线性变换、特征值/特征向量和奇异值分解（SVD），展示了它们在ML模型中的重要性。

接下来，它讨论了优化，重点介绍了梯度下降和反向传播，这对于模型训练至关重要。损失函数，特别是均方误差（MSE）和交叉熵损失，被解释为模型性能的指标。

最后，本文探讨了高级ML概念，如扩散过程、卷积运算、softmax函数和注意力机制。每个概念都用相应的方程式、其重要性的简要解释以及使用NumPy、scikit-learn、PyTorch和TensorFlow等库的实际Python代码示例进行解释。目标是提供对这些方程的理论理解和实际应用，使其成为任何寻求加深ML数学知识的人的宝贵资源。文章最后推荐了进一步学习的资源。

---

## 12. 微生物代谢物通过恢复肝脏脂质代谢修复肝损伤

**原文标题**: Microbial metabolite repairs liver injury by restoring hepatic lipid metabolism

**原文链接**: [https://journals.asm.org/doi/10.1128/mbio.01718-25](https://journals.asm.org/doi/10.1128/mbio.01718-25)

无法访问文章链接。

---

## 13. 团队自然成长

**原文标题**: Teams Grow Organically

**原文链接**: [https://frederickvanbrabant.com/blog/2025-08-22-how-teams-grow-organically/](https://frederickvanbrabant.com/blog/2025-08-22-how-teams-grow-organically/)

本文探讨了团队如何通过非正式沟通网络自然发展，挑战了传统的团队结构层级化观点。作者认为，康威定律（即系统的设计反映了其创建者的沟通结构）不仅适用于软件，还适用于组织结构本身。这些“沟通网络”通常由“弱连接”（偶然的、跨领域的联系）而非牢固的、既定的关系驱动，对于组建新团队和激发创新至关重要。

作者通过一个关于偶然相遇催生新项目团队的轶事对此进行了说明。弱连接将来自不同部门的个人联系起来，从而揭示了隐藏的低效率和机遇。这些联系随后演变成强连接，巩固了新的团队结构。

在认识到面对面互动对于培养这些弱连接的价值的同时，作者还强调了沟通工具在远程工作中的重要性。Slack被认为是一个可以通过基于爱好的频道和随意调侃来促进非正式连接的平台，这与Microsoft Teams更为结构化的方法形成对比。

最终，本文强调，虽然这些非正式网络难以形式化或图表化，但它们对于组织增长和创新至关重要。公司应留意他们使用的工具以及这些工具如何鼓励或扼杀这些联系，并认识到便利性可能会以失去由弱连接驱动的机会为代价。

---

## 14. Claude代码检查点

**原文标题**: Claude Code Checkpoints

**原文链接**: [https://claude-checkpoints.com/](https://claude-checkpoints.com/)

Claude代码检查点是一款macOS应用程序，旨在通过为Claude代码项目提供自动版本控制来防止代码丢失。它提供“时间旅行”功能，允许用户将代码恢复到之前的状态，非常适合实验和错误恢复。

该应用具有自动变更检测功能，无需任何初始设置即可持续监控项目文件的修改。用户可以创建一键式检查点，以便在进行有风险的更改之前捕获项目状态。内置的可视化差异查看器使用户可以轻松比较检查点之间的更改，跟踪添加、修改和删除。每个检查点都代表完整的项目备份，确保可恢复性。

该应用程序通过模型上下文协议 (MCP) 与 Claude Desktop 无缝集成。此集成在任务完成后自动创建检查点。MCP 服务器自动启动，Claude Desktop 立即连接，允许 Claude 使用 MCP 命令列出检查点、查看差异和恢复之前的状态。工作流程很简单：选择项目文件夹，开始编码（更改会自动跟踪），自动创建检查点，只需单击一下即可恢复。该应用程序是免费的，需要 macOS 13.5+，可以从 Mac App Store 下载。界面设计简洁直观。

---

## 15. Prosper AI (YC S23) 招聘创始销售主管 (纽约市)

**原文标题**: Prosper AI (YC S23) Is Hiring Founding Account Executives (NYC)

**原文链接**: [https://jobs.ashbyhq.com/prosper-ai/29684590-4cec-4af2-bb69-eb5c6d595fb8](https://jobs.ashbyhq.com/prosper-ai/29684590-4cec-4af2-bb69-eb5c6d595fb8)

Prosper AI 创始高级客户经理职位招聘 (Y Combinator S23 批次公司，工作地点：纽约市)。招聘信息内容简略，仅提供职位名称及“需要 JavaScript 运行此应用”的通用提示。

---

## 16. 86-DOS 的诞生 – 作者：Nemanja Trifunovic

**原文标题**: Birth of 86-DOS – By Nemanja Trifunovic

**原文链接**: [https://nemanjatrifunovic.substack.com/p/birth-of-86-dos](https://nemanjatrifunovic.substack.com/p/birth-of-86-dos)

好的，我已阅读了提供的URL上的文章“86-DOS的诞生 – 作者：Nemanja Trifunovic”。以下是一个简明扼要的总结：

这篇文章详细介绍了86-DOS的诞生，这个操作系统后来成为了MS-DOS，并为IBM PC提供动力。它着重介绍了关键人物Tim Paterson以及他在西雅图计算机产品公司（SCP）创建QDOS（Quick and Dirty Operating System，快速而简陋的操作系统）的过程。

Paterson需要一个操作系统来支持SCP的新型基于8086的计算机，于是在短短几个月内开发了QDOS。文章强调，QDOS的设计有意识地模仿了当时占主导地位的操作系统CP/M的功能，以便简化现有软件的移植。Paterson的目标是兼容性，而不是创新。

文章重点介绍了QDOS的关键组件，包括其命令处理器、文件系统和BIOS接口。它描述了Paterson高效的编码风格以及他使用宏来优化性能的做法。

至关重要的是，文章解释了微软如何为了即将推出的IBM PC寻找操作系统，并以相对较小的价格从SCP收购了86-DOS（更名后的QDOS）的版权。然后，微软对其进行了改编并授权给IBM，后者将其重新命名为PC-DOS。Paterson本人也加入了微软，以协助移植过程。

文章最后强调了一个快速、务实的解决方案（QDOS/86-DOS）在塑造早期PC时代的重要作用，尽管它的起源并不那么具有革命性。文章将其与Digital Research（CP/M的创建者）开发有竞争力的操作系统，但最终未能成功的努力形成了对比。作者认为，成功的关键在于快速满足需求的能力，即使这意味着模仿而不是创新。

---

## 17. 鲜为人知的创业泡沫

**原文标题**: The startup bubble that no one is talking about

**原文链接**: [https://tj401.com/blog/formd/index.html](https://tj401.com/blog/formd/index.html)

TJ·杰斐逊的文章认为，一场很大程度上未被承认的初创企业泡沫，由于风险投资资金即将减少而面临破裂的危险。他通过分析D表格备案的趋势来支持这一观点，这些趋势表明风险投资基金的创建在2022年第三季度左右达到顶峰，随后急剧下降。他将这种激增归因于零利率环境和Angellist和Sydecar等“SPV即服务”公司的兴起，这些公司降低了新风险投资公司的准入门槛。

杰斐逊预测，鉴于风险投资基金通常的10年寿命和2-4年的部署阶段，这种资金减少的后果现在将变得显而易见。这与对人工智能初创企业的过度期望相吻合，导致更高的估值，而这些估值是由2022年峰值时可用的资本推动的。他预计随着资金枯竭，估值将会降低，从而暴露不可持续的商业模式，特别是那些依赖昂贵计算资源来进行人工智能应用的商业模式。

他认为，预期的衰退不仅仅是由于对人工智能行业的情绪变化，而是根本上受到自2022年筹款高峰以来风险投资资金可用性预先确定的减少所驱动。文章最后附有一张图表，说明了提及“ai”或“.ai”的D表格的总发行额，突出了持续的投资，但也为潜在的调整奠定了基础。

---

## 18. 小组借用：以更少限制实现零成本内存安全

**原文标题**: Group Borrowing: Zero-cost memory safety with fewer restrictions

**原文链接**: [https://verdagon.dev/blog/group-borrowing](https://verdagon.dev/blog/group-borrowing)

群组借用：限制更少的零成本内存安全

本文题为“群组借用：限制更少的零成本内存安全”，可能探讨一种名为“群组借用”的新型内存安全技术。 该技术由 Evan Ovadia 撰写，Nick Smith 协助，旨在提供内存安全（程序正确性的关键方面），且不产生运行时性能开销（零成本）。

其核心价值在于通过提供*更少的限制*来改进现有的内存安全机制。 这表明当前的方法，例如 Rust 的借用检查器，有时可能过于严格，从而阻止了有效且安全的代码模式。 群组借用可能解决了这些限制。

“群组借用”技术大概引入了一种管理内存访问的方式，该方式允许更灵活的借用模式，同时仍然保证内存安全。 本文很可能会深入研究如何实现这一目标的具体细节，并可能引入用于管理数据访问和生命周期的新概念或规则。

本质上，本文承诺了一种改进的内存安全新方法，在保持当前技术（如安全性）优势的同时，最大限度地减少其缺点（限制性），并且不增加运行时开销。 读者可以期待深入了解“群组借用”背后的机制及其相对于现有方法的优势。

---

## 19. GPUPrefixSums – 最先进的GPU前缀和算法

**原文标题**: GPUPrefixSums – state of the art GPU prefix sum algorithms

**原文链接**: [https://github.com/b0nes164/GPUPrefixSums](https://github.com/b0nes164/GPUPrefixSums)

GPUPrefixSums：一个项目，专注于在可移植计算着色器中实现最先进的GPU前缀和（扫描）算法，并从CUDA技术中汲取灵感。其主要贡献是“解耦回退”，这是一种新颖的方法，旨在防止在没有保证正向线程进度的设备上，于使用解耦回溯的链式扫描过程中发生崩溃。如果检测到死锁，此回退机制允许线程块执行冗余计算并将缩减结果广播到设备内存，从而提高在Apple M GPU等架构上的性能（尽管包含的版本已过时，并且Vello有更新的开发）。

该项目提供了一系列前缀和算法的概述，从Kogge-Stone和Sklansky等基本扫描到warp同步和块/设备级方法。提供了D3D12、CUDA、Unity和仅用于测试的WGPU版本的实现。

*   **GPUPrefixSumsD3D12:** 无头D3D12实现，包括先Reduce后Scan、使用解耦回溯的链式扫描，以及使用解耦回溯及解耦回退的链式扫描。
*   **GPUPrefixSumsCUDA:** 用于基准测试的CUDA实现，与Nvidia的CUB库进行比较；不适用于生产环境。
*   **GPUPrefixSumsUnity:** 包含先Reduce后Scan和使用解耦回溯的链式扫描的Unity包。
*   **GPUPrefixSumsWGPU:** 仅用于测试目的的精简实现。

本文还提供了一系列关于前缀和和相关GPU主题的相关研究论文和文章。

---

## 20. 开源是一个人

**原文标题**: Open Source is one person

**原文链接**: [https://opensourcesecurity.io/2025/08-oss-one-person/](https://opensourcesecurity.io/2025/08-oss-one-person/)

本文认为，对开源维护者国籍的普遍关注是错误的。作者断言，绝大多数开源项目，包括那些被广泛使用的项目，都由个人维护，因此“开源即一人”是主要观点。

作者利用 ecosyste.ms 的数据，并专注于 NPM 生态系统，证明了数百万个开源项目由一人维护。即使对于每月下载量超过一百万的热门软件包，情况也是如此，其中大约一半由个人维护。

作者批评了最近一篇关注开源开发者国籍的文章，认为这种审查是徒劳无益的，并且可能对社区造成伤害。相反，作者认为真正的风险在于这些单人维护者的资源不足和过度劳累，而与其国籍无关。一个单人维护者就是一个单一故障点，且报酬过低、工作过度。

作者最后建议，关注原产国是一种转移注意力的手段。相反，应该更加重视支持开源维护者并为其提供资源，以确保软件供应链的稳定性和安全性。解决方案不应该是追捕和妖魔化单人维护者。

---

## 21. Docker.io/Bitnami 的删除

**原文标题**: The Deletion of Docker.io/Bitnami

**原文链接**: [https://community.broadcom.com/tanzu/blogs/beltran-rueda-borrego/2025/08/18/how-to-prepare-for-the-bitnami-changes-coming-soon](https://community.broadcom.com/tanzu/blogs/beltran-rueda-borrego/2025/08/18/how-to-prepare-for-the-bitnami-changes-coming-soon)

本文可能重点介绍如何为托管在 `docker.io` 注册表上的 Bitnami 镜像的重大变更做准备。核心在于这些镜像将被移除、移动或进行重大更改。

关键要点可能包括：

*   **变更说明：** 本文可能详细说明 `docker.io` 上的 Bitnami 镜像正在发生 *哪些* 具体更改。这可能包括删除、迁移到不同的注册表、镜像标签或结构的更改，或者 Bitnami 提供其容器镜像的方式的转变。

*   **影响评估：** 本文可能评估此更改对当前在其部署、CI/CD 管道或开发工作流程中依赖这些镜像的用户的潜在影响。

*   **迁移策略：** 本文很可能提供关于如何减轻影响并过渡到新设置的指导和策略。这可能包括：
    *   识别受影响的系统/部署。
    *   切换到替代注册表或镜像源（如果 Bitnami 正在移动镜像）。
    *   更新 Dockerfile 和部署清单中的镜像标签或引用。
    *   调整构建过程。
    *   如果 Bitnami 停止提供某些镜像，则考虑替代容器镜像或解决方案。

*   **时间表和资源：** 本文可能包含更改发生的时间表，以及指向相关文档、支持资源或通信渠道的链接，以便从 Bitnami 获取更多信息。

本质上，本文是呼吁 Docker Hub 上 Bitnami Docker 镜像的用户采取积极措施，以避免即将发生的更改造成的破坏。

---

## 22. 消费者条款及隐私政策更新

**原文标题**: Updates to Consumer Terms and Privacy Policy

**原文链接**: [https://www.anthropic.com/news/updates-to-our-consumer-terms](https://www.anthropic.com/news/updates-to-our-consumer-terms)

Anthropic更新Claude Free、Pro和Max用户的使用者条款和隐私政策，以改进AI模型。用户现在可以选择是否允许使用其数据进行模型训练，以增强Claude的能力和安全措施。

**主要更新：**

*   **数据使用选择：** 用户可以选择是否允许使用其聊天和编码会话数据来改进模型。 此设置可以随时在隐私设置中进行调整。
*   **延长数据保留期：** 如果用户选择允许使用数据进行模型训练，则新聊天或恢复的聊天以及编码会话的数据保留期将延长至五年。如果他们选择退出，则保留期仍为 30 天。 删除的聊天记录将不用于训练。
*   **隐私保护：** Anthropic 使用工具和自动化流程来过滤或混淆敏感数据，并且不会将用户数据出售给第三方。
*   **生效日期：** 现有用户需要在 2025 年 9 月 28 日之前接受更新后的条款并做出数据使用决定。 在此日期之后，必须选择偏好设置才能继续使用 Claude。 这些政策仅适用于新的和恢复的聊天以及编码会话。 新用户可以在注册期间选择他们的偏好设置。
*   **例外情况：** 这些更新不适用于商业条款下的服务，例如 Claude for Work、Claude Gov、Claude for Education 或通过第三方进行的 API 使用。
* **理由：** 延长保留期是为了模型一致性和更好的滥用检测。

此次更新旨在提高模型安全性并增强编码、分析和推理等技能。 通过参与，用户有助于提高模型准确性并减少有害使用。

---

## 23. iOS优雅驱逐舰：当无法获取样本却仍需捕获威胁时

**原文标题**: iOS Elegantbouncer: When You Can't Get Samples but Still Need to Catch Threats

**原文链接**: [https://www.msuiche.com/posts/elegantbouncer-when-you-cant-get-the-samples-but-still-need-to-catch-the-threat/](https://www.msuiche.com/posts/elegantbouncer-when-you-cant-get-the-samples-but-still-need-to-catch-the-threat/)

ELEGANTBOUNCER 是一款开源 iOS 威胁检测工具，旨在无需访问恶意样本即可识别漏洞利用。 它超越了传统的基于签名的检测，通过分析文件的结构属性，专注于它们如何偏离预期模式以实现漏洞利用。

该工具针对 FORCEDENTRY (JBIG2 PDF 漏洞利用)、BLASTPASS (WebP 堆溢出)、TRIANGULATION (TrueType 字体漏洞利用) 和 CVE-2025-43300 (DNG 处理漏洞) 等漏洞。 ELEGANTBOUNCER 使用的技术包括检测 JBIG2 流中不可能的数学条件、WebP 中格式错误的 Huffman 表以及 TrueType 字体中未公开的字节码。

其架构强调性能，包括智能扫描器选择、并行处理、提前终止和高效解析。 ELEGANTBOUNCER 包含一个 TUI 用于实时扫描监控。 一个关键特性是它能够重建和扫描 iOS 备份转储，以查找隐藏在 iMessage、WhatsApp、Signal、Telegram 和 Viber 等消息应用程序附件中的威胁。

其局限性包括多态变体可能逃避检测、依赖于对已知漏洞利用技术的理解以及产生误报的可能性。 该项目鼓励安全社区的贡献，特别是以新检测方法、样本生成、性能改进以及与安全管道集成等形式。 该工具的核心原则是，即使没有访问漏洞本身，理解漏洞利用的机制也足以进行有效的威胁检测。

---

## 24. 山手線音樂盒：JR山手線車站旋律

**原文标题**: Yamanot.es: A music box of train station melodies from the JR Yamanote Line

**原文链接**: [https://yamanot.es/](https://yamanot.es/)

Yamanot.es 是一个项目，旨在整理东京 JR 山手线上各车站使用的旋律。它以“Yamanotes山ノーツ”的形式呈现，功能类似于一个（某种程度上）音乐盒，收录了每个站台的旋律。该页面列出了山手线上的所有车站，从东京到有乐町，每个车站可能都链接到其各自的旋律或相关信息。该网站还提到了与山手线相关的其他几条线路，包括京滨东北线、N'EX（成田特快）、埼京线、总武线和上野东京线。“关于”部分可能包含有关该项目的更详细信息。

---

## 25. 用于算术运算的快速字节码虚拟机：编译器

**原文标题**: A Fast Bytecode VM for Arithmetic: The Compiler

**原文链接**: [https://abhinavsarkar.net/posts/arithmetic-bytecode-vm-compiler/](https://abhinavsarkar.net/posts/arithmetic-bytecode-vm-compiler/)

本文详细介绍了用 Haskell 创建算术表达式字节码编译器的过程，该编译器旨在提高速度和效率。它延续了之前一篇关于将算术表达式解析为抽象语法树 (AST) 的文章。

文章强调了由于内存碎片化，AST 解释器的性能存在局限性。为了解决这个问题，作者提倡将 AST 编译成字节码，这是一种紧凑且扁平化的表示形式，以便虚拟机 (VM) 执行。出于简单性考虑，选择了基于堆栈的 VM，尽管基于寄存器的 VM 通常更快。

文章的核心在于设计字节码指令集。定义了用于压入数字 (OPush)、执行二元运算 (OAdd、OSub、OMul、ODiv) 以及处理变量和 let 表达式 (OGet、OSwapPop) 的操作码。变量由其堆栈索引表示，以避免运行时环境查找。

编译器实现涉及基于解析期间收集的信息，预先分配所需大小的 `ByteString`。编译过程使用指针进行高效的内存操作，将字节码指令直接写入预先分配的 `ByteString`。维护一个环境映射来跟踪变量堆栈索引。

作者对各种用于字节码生成的数据结构（Lists、Seqs、DLists、ByteString Builders、ByteArrays）进行了基准测试，并强调了通过预先分配的 `ByteString` 获得的巨大性能提升。还对用于变量查找的不同映射数据结构进行了基准测试，其中严格的 HashMaps 证明是最快的。文章包含了具体的性能数据和图表，以说明这些改进。

---

## 26. Fossjobs：自由开源职位招聘

**原文标题**: Fossjobs: A job board for Free and Open Source jobs

**原文链接**: [https://www.fossjobs.net/](https://www.fossjobs.net/)

Fossjobs文章显示荷兰阿姆斯特丹的NLnet基金会招聘技术评估员。职位为全职，发布日期为2025年8月28日（日期可能不准确，应为过往信息）。职位ID：1805。核心信息是NLnet基金会正在寻找人来填补该职位。

---

## 27. 洋葱服务证书

**原文标题**: Certificates for Onion Services

**原文链接**: [https://onionservices.torproject.org/research/proposals/usability/certificates/](https://onionservices.torproject.org/research/proposals/usability/certificates/)

本文探讨了集成和验证 Onion Services 的 TLS/HTTPS 证书所面临的挑战和提出的解决方案，旨在使 Onion Services 与现代 Web 开发实践保持一致。虽然 Onion Services 本身提供点对点加密，但证书可以解锁浏览器功能，如 HTTP/2、安全 Cookie 和支付处理，从而提供增强的安全性和功能。

本文概述了几项提案，每项提案都有其优缺点：

*   **现有 CA 验证：** 目前已实施，但可能涉及在购买证书期间披露可识别信息。

*   **.onion 的 ACME（RFC 9799）：** 自动为 Onion Services 颁发证书，可能使从 Let's Encrypt 等项目获得免费证书成为可能。

*   **自签名证书：** 易于实施，但缺乏自验证机制，需要仔细考虑 UI 和提示。

*   **来自 .onion 的自签名 X.509：** 使用 Onion Service 密钥对自验证证书，无需依赖 CA，但需要额外的服务器和客户端逻辑。当前的 Onion Service 规范不允许将 Master Onion Service 身份密钥用于其他目的，并且浏览器对 Ed25519 证书的支持有限。

*   **同源 Onion 证书（SOOC）：** 消除了 Onion Services 对 CA 的依赖。

*   **.onion 的 DANE：** 消除了 CA 依赖，但实施和维护起来很复杂。

*   **仅 Onion 的 CA：** 简化了对 CA 的依赖，但需要建立新的 CA 基础设施。

*   **通过 PKCS#11 模块进行自验证证书：** 使用 PKCS#11 进行身份验证，提供面向未来的无 CA 验证。

本文强调，所讨论的领域仍在考虑中，可能难以找到一个普遍的答案。

---

## 28. Bookmarks.txt 是一种将 URL 保存在纯文本文件中的概念。

**原文标题**: Bookmarks.txt is a concept of keeping URLs in plain text files

**原文链接**: [https://github.com/soulim/bookmarks.txt](https://github.com/soulim/bookmarks.txt)

bookmarks.txt 提议通过将网站书签存储在名为 `bookmarks.txt` 的纯文本文件中来管理网站书签。其核心思想是简洁并利用现有的文本处理工具。书签以每行一个 URL 的形式存储，可以选择在 URL 后添加一个空格和标题。

该系统支持全局 (`$HOME/bookmarks.txt`) 和本地 (`./bookmarks.txt`) 书签文件。全局文件包含跨上下文相关的 URL，而本地文件则特定于项目目录。

这种文本格式使用户能够利用各种程序进行书签管理。该存储库包含一个 `bookmarks` 脚本（位于 `bin/` 目录中），用于列出和添加 URL，但鼓励用户创建自己的工具。提供的示例演示了如何使用 `fzf` 进行模糊搜索并在默认浏览器中打开书签。

作者使用全局书签存储通用 URL，并使用本地书签存储特定于项目的资源，如存储库和仪表板。指向 `bookmarks` 脚本的符号链接提供了一个方便的命令行界面。

该项目欢迎错误修复，但目前不接受功能贡献，因为需要考虑长期维护。该项目根据 LICENSE 文件中描述的条款获得许可。本质上，bookmarks.txt 是一个极简、灵活的系统，它使用简单的文本文件和现有的命令行工具来管理 URL。

---

## 29. 呼吸法结合音乐诱导的意识改变状态

**原文标题**: Altered states of consciousness induced by breathwork accompanied by music

**原文链接**: [https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0329411](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0329411)

本文探讨了高通气呼吸法(HVB)结合音乐诱导的意识改变状态(ASCs)背后的神经生物学机制。HVB是一种涉及增加呼吸频率或深度的练习，作为一种治疗工具正日益普及，可能为诱导ASCs提供一种非药物性的迷幻药替代方案。

本研究旨在描述HVB的主观体验，并识别经验丰富的从业者中潜在的神经生理学机制。 进行了三个相互关联的实验：（1）通过视频会议进行远程HVB以描述主观反应，（2）HVB期间的MRI扫描以评估大脑血流动力学变化，以及（3）心理生理学实验室实验以检查自主神经系统变化。

研究发现，HVB期间ASCs的强度与心血管交感神经激活以及大脑中与呼吸内感受（左侧岛盖/后岛叶）和情绪记忆处理（右侧杏仁核/前海马体）相关区域的血流动力学改变成正比。 这些区域性的大脑效应可能与HVB观察到的积极治疗效果有关。 研究人员使用了5D-ASC问卷，特别是“海洋融合感”(OBN)维度，来评估主观体验。 研究人员侧重于测量区域性脑血流量（rCBF）和心率变异性（HRV）作为关键的神经生物学指标。 结果表明，HVB对这些大脑区域和自主功能的影响有助于与该练习相关的深刻主观体验。

---

## 30. 英伟达 DGX Spark

**原文标题**: Nvidia DGX Spark

**原文链接**: [https://www.nvidia.com/en-us/products/workstations/dgx-spark/](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)

NVIDIA DGX Spark：为开发者、研究人员和数据科学家设计的紧凑型、高能效AI超级计算机，将NVIDIA Grace Blackwell架构的强大性能带到桌面。它由NVIDIA GB10 Grace Blackwell 超级芯片驱动，提供1 petaFLOP的AI性能，并具有128GB的统一系统内存。

DGX Spark支持在本地对大型AI模型（高达2000亿参数）进行原型设计、微调和推理，并可无缝部署到数据中心或云端。它支持微调高达700亿参数的模型。

主要特点包括：

*   **NVIDIA GB10 超级芯片：**高达1 petaFLOP的AI性能。
*   **128 GB 统一内存：**处理高达2000亿参数的AI模型。
*   **NVIDIA ConnectX 网络：**支持连接两台DGX Spark系统以处理更大的模型。
*   **NVIDIA AI 软件堆栈：**适用于生成式AI工作负载的完整堆栈解决方案。

DGX Spark加速各种AI工作负载，包括原型设计、微调、推理、数据科学（使用NVIDIA RAPIDS）以及边缘应用程序开发（使用NVIDIA框架，如Isaac和Metropolis）。

规格包括NVIDIA Grace Blackwell架构、20核Arm CPU、Blackwell代CUDA内核、第五代Tensor内核、第四代RT内核、快速内存带宽、NVMe存储选项、ConnectX-7 Smart NIC、WiFi 7、蓝牙5.3和NVIDIA DGX OS。该系统结构紧凑，重量轻。

---

## 31. 巴西给美国上了一课，关于民主的成熟。

**原文标题**: Brazil offers America a lesson in democratic maturity

**原文链接**: [https://www.economist.com/leaders/2025/08/28/brazil-offers-america-a-lesson-in-democratic-maturity](https://www.economist.com/leaders/2025/08/28/brazil-offers-america-a-lesson-in-democratic-maturity)

文章《巴西为美国提供民主成熟的教训》强调，巴西的经验可以作为美国的潜在榜样，以应对民粹主义领导人下台以及处理破坏民主进程的企图。文章设想了一种情形，即一位两极分化的总统输掉了选举，拒绝承认结果，煽动其支持者进行暴力活动，并随后因策划政变而受到调查和审判。这与巴西的雅伊尔·博索纳罗所发生的事情相呼应。

文章表明，巴西对这种情况的处理为面临类似挑战的国家提供了宝贵的经验。巴西通过法律手段追究其前领导人责任的能力，被视为民主韧性和成熟的标志。标题也表明，这篇文章会将巴西的反应与美国对类似情况的处理进行对比，可能指的是1月6日国会大厦袭击事件的后果以及围绕前总统特朗普的角色和责任的持续讨论。

文章将巴西的经验定位为各国如何应对民粹主义运动和颠覆民主制度企图的后果的“试验案例”。对“巴西能教给美国什么”的引用进一步强化了这一点。

---

## 32. 数据被发送的鲜为人知的移动广告技术领域

**原文标题**: Lesser known mobile adtech domains where data is sent

**原文链接**: [https://jamesoclaire.com/2025/08/28/uncovering-lesser-known-mobile-adtech-domains/](https://jamesoclaire.com/2025/08/28/uncovering-lesser-known-mobile-adtech-domains/)

AppGoblin分析了来自4万个应用的数据流量，以识别几个鲜为人知的移动广告技术域名的所有者。研究揭示了以下内容：

*   **qa-analytics.com：** 归属于Unity，基于共享的IP地址和API调用中重叠的`app_key`值。
*   **acobt.tech, news-cdn.site, kickoffo.site, onegg.site：** 全部与Bigo Ads关联，证据包括共享的IP地址、相关应用中存在Bigo Ads SDK以及互联网搜索结果。
*   **lazybumblebee.com：** 与mediation SDK BidMachine相关联。这一结论得到了以下因素的支持：使用该域名的应用中存在BidMachine SDK（io.bidmachine, com.explorestack），以及与everestop.io和bidmachine.io共享IP地址。使用此域名的应用大多调用d.lazybumblebee.com/track/sdk-event的变体。
*   **marketingcloudapis.com：** 最初怀疑与Google相关，因为它经常与googleapis.com调用同时出现。然而，一位HackerNews用户指出它属于Salesforce，AppGoblin通过在相关应用中发现Salesforce SDK证实了这一点。

该分析揭示了几个“黑暗”域名，并成功地将其归属于广告技术生态系统中的已知实体。结果是：

*   news-cdn.site -> Bigo Ads
*   marketingcloudapis.com -> SalesForce
*   kickoffo.site -> Bigo Ads
*   onegg.site -> BIGO Ads
*   lazybumblebee.com -> BidMachine
*   qa-analytics.com -> Unity
*   acobt.tech -> Bigo Ads
*   yastatic.net -> Yandex

---

## 33. Windows 11 更新 KB5063878 导致 SSD 故障

**原文标题**: Windows 11 Update KB5063878 Causing SSD Failures

**原文链接**: [https://old.reddit.com/r/msp/comments/1n1sgxx/windows_11_update_kb5063878_causing_ssd_failures/](https://old.reddit.com/r/msp/comments/1n1sgxx/windows_11_update_kb5063878_causing_ssd_failures/)

无法访问文章链接。

---

## 34. 使用人工智能实时渲染游戏

**原文标题**: Rendering a Game in Real-Time with AI

**原文链接**: [https://blog.jeffschomay.com/rendering-a-game-in-real-time-with-ai](https://blog.jeffschomay.com/rendering-a-game-in-real-time-with-ai)

无法访问文章链接。

---

## 35. 秋季学期开始，高校国际学生人数大幅下降。

**原文标题**: Colleges see significant drop in international students as fall semester begins

**原文链接**: [https://text.npr.org/nx-s1-5498669](https://text.npr.org/nx-s1-5498669)

由于特朗普政府对学生签证的严格限制，纽约州立大学布法罗分校以及美国各地的大学今年秋季的国际学生入学人数大幅下降。这些限制导致了延误、焦虑和签证拒签，使得许多学生选择推迟入学或转学到英国等国家的大学。

纽约州立大学布法罗分校的国际学生人数减少了约750人，尤其是在STEM研究生项目中。其他院校也报告了类似的下降。国际教育工作者协会预计，全国范围内的国际学生人数将总体下降15%，这可能导致70亿美元的经济损失和6万个工作岗位的流失。

虽然特朗普政府以安全担忧和潜在的美国学生被取代为由，但大学领导强调，国际学生为校园带来了文化多样性和经济贡献。此外，纽约州立大学布法罗分校的教务长保证，国际学生并没有占据合格的美国学生的名额。尽管面临挑战，像来自印度的Shivika Singh这样成功通过签证流程的学生，对能够来到校园并准备开始学习感到欣慰。

---

## 36. AMD效仿英特尔，将CPU烧毁归咎于主板厂商。

**原文标题**: Like Intel before it, AMD blames motherboard makers for burnt-out CPUs

**原文链接**: [https://arstechnica.com/gadgets/2025/08/like-intel-before-it-amd-blames-motherboard-makers-for-burnt-out-cpus/](https://arstechnica.com/gadgets/2025/08/like-intel-before-it-amd-blames-motherboard-makers-for-burnt-out-cpus/)

AMD将Ryzen X3D CPU烧毁归咎于主板厂商，与英特尔第13代和第14代酷睿CPU面临的类似问题遥相呼应。一些Ryzen X3D芯片，特别是搭配华擎主板的9800X3D，已经出现故障，包括物理烧焦。

AMD高管David McAfee和Travis Kirsch将问题归因于主板制造商为了提高性能而超过了AMD推荐的功率规格，这可能导致问题，特别是对于高端CPU。这并非AMD首次遇到此类问题；早期的Ryzen 7000系列X3D芯片由于错误的电压设置而发生变形，促使AMD发布BIOS更新以限制电压。

英特尔也面临着类似的CPU问题，理由是主板制造商偏离了推荐的默认设置。英特尔最终延长了受影响CPU的保修期。

AMD建议用户安装主板制造商发布的最新BIOS更新，以确保符合新的默认设置并获得其他改进。McAfee和Kirsch强调了测试AMD系统的难度，因为他们的芯片组和CPU插槽的生命周期很长，从而允许各种系统配置和潜在的不兼容性。用户可能正在将新的Ryzen X3D芯片与较旧的主板配对，从而创建英特尔生态系统中看不到的升级路径，这可能会导致无法预见的问题。

---

## 37. Show HN: SwiftAI – 在 iOS/macOS 上轻松构建 LLM 功能的开源库

**原文标题**: Show HN: SwiftAI – open-source library to easily build LLM features on iOS/macOS

**原文链接**: [https://github.com/mi12labs/SwiftAI](https://github.com/mi12labs/SwiftAI)

SwiftAI是一个开源的Swift库，旨在简化在iOS和macOS上构建AI驱动的应用程序的过程。它提供了一个统一的API，支持各种AI模型，包括苹果的设备端模型 (SystemLLM) 和基于云的服务，如 OpenAI (OpenaiLLM)，从而实现模型无关性。

主要功能包括：

*   **结构化输出：** 使开发者能够直接从AI模型接收强类型的数据结构，无需手动JSON解析。`@Generable`宏简化了这一过程。
*   **Agent 工具循环：** 支持使用AI可以调用的工具（函数）来访问实时信息，例如天气数据，使用`Tool`协议。
*   **对话：** 提供一个`Chat`类来管理有状态的、多轮的对话，并自动保留上下文。
*   **可扩展性：** 允许通过插件架构自定义模型和工具的实现。
*   **Swift原生：** 使用async/await和现代Swift并发构建。

该库通过诸如`reply(to:)`等函数简化了AI交互，用于基本查询，并通过`chat.send()`进行对话。它还提供了模型切换机制（设备端与云端）并使用`@Guide`向生成的数据添加约束和描述。

SwiftAI遵循MIT许可证，目前处于alpha阶段，欢迎通过其贡献指南参与贡献。

---

## 38. 破釜沉舟：中国重塑未来的征程

**原文标题**: Breakneck: China's Quest to Engineer the Future

**原文链接**: [https://danwang.co/breakneck/](https://danwang.co/breakneck/)

本文是对作者新书《疾速：中国塑造未来的探索》的公告与反思。该书认为，中国是一个“工程国家”，用大锤式的方法解决问题，而美国是一个“律师社会”，依赖于往往有利于富人的法律程序。作者根据2017年至2023年在中国的生活经历，认为这个框架有助于解释贸易战和科技对抗。中国侧重于实体建设和工程进步，而美国则依赖于法律制裁。

作者强调，这并非宏大理论，而是对这两个体系的观察，两者都存在缺陷。他们回忆了在中国骑自行车的经历，突出了基础设施的进步，同时也批评了中国的社会工程，特别是独生子女政策。

本文还深入探讨了写作过程，讨论了每个阶段的挑战，以及作者如何在撰写七篇“年度信”的过程中提高写作水平。此外，作者反思了如何成为一个更好的读者，区分不同类型的中国书籍，以及学术出版物与商业出版物。

最后，作者详细描述了写作过程中的美食体验，重点介绍了墨西哥城、岘港、巴塞罗那、巴黎和哥本哈根等城市多样化和创新的美食场景，同时也注意到上海食品质量可能下降以及网红文化对餐饮体验的负面影响。

---

## 39. Sci-Hub 在印度被封锁。

**原文标题**: Sci-Hub has been blocked in India

**原文链接**: [https://sci-hub.se/sci-hub-blocked-india](https://sci-hub.se/sci-hub-blocked-india)

2025年8月，根据法院命令，应爱思唯尔、威立和美国化学学会的要求，Sci-Hub和Sci-Net在印度被封锁。自2020年以来，这些出版商一直在试图限制印度对免费科学的访问，最初的目标是Sci-Hub和Library Genesis。虽然之前关于诉讼的推特公告引发了公众的强烈抗议和对Sci-Hub的支持，但该账户随后被封禁。

印度的诉讼是独特的，因为Sci-Hub由志愿律师辩护，这提高了人们对判决反对学术出版业对科学的负面影响的希望。尽管在2021年提出了暂停发布新论文的请求，但法院从未做出最终裁决。

文章强调，Sci-Hub停止发布新论文的主要原因是大学实施了双重身份验证，使得旧的绕过付费墙的方法失效。作者描述了2025年4月推出的Sci-Net，这是一个基于社区的项目，使用区块链技术来激励开放获取论文的上传。这引发了出版商的投诉以及随后阻止Sci-Hub和Sci-Net的法院命令。

作者认为，阻止Sci-Hub是非法的，侵犯人权，并且违背印度的国家利益。他们批评目前的制度，即印度机构向外国公司支付过高的订阅费，而不是资助当地研究人员。文章最后鼓励读者加入正在进行的法律案件，并提供了使用VPN和TOR浏览器绕过封锁并访问Sci-Hub的说明。

---

## 40. 谷歌过去一年裁减了35%的小团队管理人员

**原文标题**: Google has eliminated 35% of managers overseeing small teams in past year

**原文链接**: [https://www.cnbc.com/2025/08/27/google-executive-says-company-has-cut-a-third-of-its-managers.html](https://www.cnbc.com/2025/08/27/google-executive-says-company-has-cut-a-third-of-its-managers.html)

谷歌大幅削减管理层级，过去一年裁减了 35% 的小型团队管理人员，旨在提高效率并减少官僚主义。人力分析和绩效副总裁 Brian Welle 在一次全体员工会议上透露了这一裁员，会上员工对近期裁员和重组后的工作保障和公司文化表达了担忧。

首席执行官桑达尔·皮查伊强调了提高效率的必要性，并避免将增加员工人数作为公司扩张的唯一解决方案。为此，谷歌还向包括搜索、市场营销、硬件和人力运营在内的十个产品领域的员工提供了“自愿离职计划”(VEP)买断，其中 3-5% 的符合条件的员工接受了这些提议。

高管表示，VEP 取得了成功，为员工提供了自主权，特别是对于那些寻求职业假期或照顾家庭时间的员工。虽然员工询问是否可以采用像 Meta 的休假计划这样的政策，但谷歌表示其现有的休假和请假安排具有竞争力且足够。皮查伊幽默地驳回了采用所有 Meta 政策的想法。该公司在 2023 年裁减了 6% 的员工后，又采取了削减成本的措施，首席财务官 Anat Ashkenazi 也表达了进一步削减成本的愿望。尽管进行了裁员，Alphabet 的股票表现依然良好。

---

## 41. 人工智能正在入侵文化领域

**原文标题**: A.I. Is Coming for Culture

**原文链接**: [https://www.newyorker.com/magazine/2025/09/01/ai-is-coming-for-culture](https://www.newyorker.com/magazine/2025/09/01/ai-is-coming-for-culture)

人工智能正在入侵文化

---

## 42. 暂停昆虫活动

**原文标题**: Pausing Insect Activity

**原文链接**: [https://www.asimov.press/p/insect-diapause](https://www.asimov.press/p/insect-diapause)

本文探讨了昆虫滞育——一种程序化的发育停滞状态——作为一个具有重要生态和经济意义的现象。滞育就像昆虫生命周期的“暂停按钮”，影响了相当一部分昆虫生物量，在某些物种中持续时间可达九个月。

文章强调了休眠作为应对环境挑战的生存策略的进化起源，并强调了其利用光周期和温度等线索的预期性质。文章将滞育与哺乳动物的冬眠进行了比较，但强调了其作为昆虫发育停滞的独特作用。该机制涉及蜕皮激素和保幼激素的激素调节，这些激素受到内部信号和环境线索的影响。

重要的是，文章指出，滞育可以通过化学物质进行人工控制，从而使我们能够控制昆虫的活动。这对于害虫防治具有重要意义，破坏滞育的自然时机可能导致害虫的“生态自杀”。作物轮作是一种古老的害虫防治策略，其有效性源于破坏了依赖特定寄主植物的害虫的滞育阶段。文章提供了一个玉米根虫如何受到影响的例子。轮作策略的失败源于一些玉米根虫适应了一种新的策略。

---

## 43. 关于容器和虚拟机

**原文标题**: About Containers and VMs

**原文链接**: [https://linuxcontainers.org/incus/docs/main/explanation/containers_and_vms/](https://linuxcontainers.org/incus/docs/main/explanation/containers_and_vms/)

Incus 支持系统容器和虚拟机（VM），为隔离和运行应用程序提供了不同的方法。系统容器利用 Linux 内核的命名空间和 cgroups 等特性，提供轻量级的软件定义隔离。它们共享宿主机内核，因此速度更快、资源消耗更少，但仅限于基于 Linux 的操作系统。

另一方面，虚拟机使用硬件虚拟化来创建虚拟化的机器，从而可以运行不同的操作系统并提供更强的隔离。然而，这也导致了资源消耗的增加。

应用容器和系统容器之间存在一个关键区别。应用容器（如 Docker 中的容器）侧重于打包单个进程或应用程序，而系统容器则模拟完整的操作系统环境。系统容器支持多个应用程序和用户空间，这些特性并非为应用容器设计的。您可以在 Incus 系统容器内运行 Docker，但反之则不行。

选择系统容器还是虚拟机取决于您的需求。当与宿主机内核的兼容性不是问题时，系统容器提供性能和大小优势。当需要宿主机内核不支持的功能，或者需要运行完全不同的操作系统时，即使消耗更多资源，也必须使用虚拟机。

---

## 44. Show HN：小型团体的 Meetup.com 和 Eventbrite 替代方案

**原文标题**: Show HN: Meetup.com and eventribe alternative to small groups

**原文链接**: [https://github.com/polaroi8d/cactoide](https://github.com/polaroi8d/cactoide)

Cactoide(ae)：精简的移动优先型小型活动管理平台，是 Meetup.com 和 Eventbrite 的替代方案。其核心价值在于简单易用，无需用户注册或账号。

主要功能包括：

*   **即时创建活动：** 通过精简的表单快速创建活动。
*   **一键分享：** 生成独特且易于记忆的 URL，方便在任何平台上分享。
*   **集中化管理：** 提供 RSVP 和参与者可用性的集中视图，无需筛选多个沟通渠道。
*   **无需注册：** 创建和分享活动无需用户注册。
*   **智能限制：** 允许设置 RSVP 限制或启用无限制 RSVP。

该项目鼓励自托管，并提供使用 Git、npm 和 Makefile 进行本地开发的简单快速入门指南。同时还提供 Docker Compose 以简化部署。Cactoide(ae) 在 MIT 许可证下发布，由 @polaroi8d 创建。总体目标是为小型聚会提供更高效、更便捷的 RSVP 管理和活动协调方式。

---

## 45. 这是什么？持续质疑我们在线体验的理由 (2021)

**原文标题**: What is this? The case for continually questioning our online experience (2021)

**原文链接**: [https://systems-souls-society.com/what-is-this-the-case-for-continually-questioning-our-online-experience/](https://systems-souls-society.com/what-is-this-the-case-for-continually-questioning-our-online-experience/)

丹·尼克松的文章《这是什么？不断质疑我们在线体验的理由》探讨了数字技术对我们生活的影响，并提倡保持一种持续质疑的精神，以此来驾驭这一领域。作为Perspectiva数字自我项目的一部分发表，这篇文章鼓励读者批判性地审视他们的日常在线体验，从社交媒体互动到新闻消费。

尼克松借鉴了现象学和禅宗等哲学传统，强调在得出结论或解决方案之前，观察和理解我们经验的重要性。他认为，通过反复询问“这是什么？”，我们可以更加清楚地意识到数字技术塑造我们感知、人际关系和自我意识的微妙方式。

这篇文章提出了关于在线交流质量、算法的影响以及自我在网络空间中的作用的具体问题。它批判了科技文化中固有的“解决方案主义”，并主张拥抱我们经验中固有的神秘性。最终，尼克松强调在数字媒介世界中需要沉默、静止和“星际空间”，培养一种有意识和质疑的在线生活方式。他邀请读者思考我们数字媒介生活的挑战，并考虑这个简单的问题如何帮助解决我们所面临的紧迫问题，无论是个人的还是集体的。

---

## 46. 通过SSH使用树莓派Zero和Nix打印标签

**原文标题**: Printing Labels via SSH with Raspberry Pi Zero and Nix

**原文链接**: [https://nmattia.com/posts/2025-08-28-label-printer-rpi-nix/](https://nmattia.com/posts/2025-08-28-label-printer-rpi-nix/)

本文详细介绍了如何使用Nix设置树莓派Zero，以使用Brother QL-700标签打印机远程打印标签，而无需依赖专有驱动程序。作者最初探索了WebUSB解决方案，但最终选择了Python `brother_ql`库和CLI工具。

在遇到最新`brother_ql`版本的兼容性问题后，他们成功地使用了nixpkgs中的特定提交来从笔记本电脑打印标签。该过程涉及指定打印机型号和USB设备ID。

作者随后过渡到使用Raspberry Pi OS和Nix设置树莓派Zero。一个关键挑战是将具有microUSB端口的Pi Zero连接到使用USB-B的打印机。这通过创建由microUSB和USB-A到USB-B电缆拼接而成的定制电缆来解决。

成功连接硬件后，作者使用Nix在Pi Zero上安装了ImageMagick和`brother_ql`。然后，他们演示了如何使用ImageMagick从文本动态生成标签，并将输出通过管道传输到`brother_ql`进行打印。

文章最后总结了潜在的未来增强功能，例如用于创建标签的Web界面和用于树莓派的定制外壳，但由于缺乏直接用例，作者停止了开发。

---

## 47. 屏幕上，利比亚人了解一切，唯独不了解自己 (2021)

**原文标题**: On the screen, Libyans learned about everything but themselves (2021)

**原文链接**: [https://newlinesmag.com/argument/on-the-screen-libyans-learned-about-everything-but-themselves/](https://newlinesmag.com/argument/on-the-screen-libyans-learned-about-everything-but-themselves/)

在他的文章《屏幕上，利比亚人了解了所有，唯独不了解自己》中，一位利比亚作家反思了外国电影，特别是好莱坞作品，如何主导利比亚文化，尤其是在卡扎菲政权时期。尽管国家对西方媒体进行控制和限制，利比亚人仍然热衷于观看盗版电影和卫星电视，从而接触到全球文化，但却与自身的文化脱节。

作者批评了西方电影中对利比亚的不准确和往往带有刻板印象的描述，并举例说明了《回到未来》、《独裁者》和《危机13小时》等电影，这些电影延续了误解和东方主义的陈词滥调。 即使像《灵异》系列这样的埃及作品也未能准确地描绘利比亚。

他将此与缺乏蓬勃发展的利比亚电影业形成对比，该产业因数十年的国家控制和宣传驱动的制作而受到阻碍。 虽然利比亚人接受了外国电影角色并将他们融入日常生活，但他们自己的故事却仍然不为人知。 这导致利比亚人自己对他们自己多元化的历史和文化底蕴一无所知，包括阿马齐格人、图阿雷格人和塔布社区的存在。 作者倡导利比亚创意人士探索自己国家的历史，创作能够引起利比亚人共鸣的真实叙事，从而培养更强的民族认同感，并向世界展示他们的文化。

---

## 48. 发布了Nx和一些支持插件的恶意版本

**原文标题**: Malicious versions of Nx and some supporting plugins were published

**原文链接**: [https://github.com/nrwl/nx/security/advisories/GHSA-cxm3-wv7p-598c](https://github.com/nrwl/nx/security/advisories/GHSA-cxm3-wv7p-598c)

2025年8月26日至27日，恶意版本的Nx及其支持插件被发布到npm，导致用户凭据泄露。该漏洞源于一个存在bash注入缺陷的GitHub Actions工作流，以及来自`pull_request_target`的提升权限。这使得攻击者能够注入代码，从publish.yml工作流中访问npm令牌，并发布恶意软件包。

受感染的软件包包含一个postinstall脚本，该脚本会扫描用户文件系统以查找凭据，将其发布到用户帐户下名为“s1ngularity-repository”的GitHub存储库，并修改`.zshrc`和`.bashrc`文件以关闭机器。发现Nx Console (VSCode扩展) 在编辑器启动期间会触发`nx@latest`的安装，从而意外地影响没有Nx工作区的用户。

受影响的版本包括多个`nx`版本 (21.5.0, 20.9.0, 20.10.0, 21.6.0, 20.11.0, 21.7.0, 21.8.0, 20.12.0), `@nx/devkit`, `@nx/js`, `@nx/workspace`, `@nx/node` (21.5.0, 20.9.0), `@nx/eslint` (21.5.0), 以及`@nx/key`, `@nx/enterprise-cloud` (3.2.0)。这些版本已被从npm中删除。

建议用户检查其GitHub帐户上是否存在“s1ngularity-repository”，轮换凭据（npm、GitHub和其他服务），更改密码，从`.zshrc`和`.bashrc`中删除不熟悉的行，并将Nx更新到非恶意版本 (`npm uninstall nx && npm install nx@latest`)。Nx已实施多项补救措施，包括弃用恶意版本，恢复有效版本作为最新版本，要求发布者使用双重验证 (2FA)，以及使用Trusted Publishers。

---

## 49. 研究人员发现日常口语中出现ChatGPT流行语的证据

**原文标题**: Researchers find evidence of ChatGPT buzzwords turning up in everyday speech

**原文链接**: [https://news.fsu.edu/news/education-society/2025/08/26/on-screen-and-now-irl-fsu-researchers-find-evidence-suggesting-chatgpt-influences-how-we-speak/](https://news.fsu.edu/news/education-society/2025/08/26/on-screen-and-now-irl-fsu-researchers-find-evidence-suggesting-chatgpt-influences-how-we-speak/)

佛罗里达州立大学的研究人员发现，来自 ChatGPT 等大型语言模型（LLM）的 AI 生成的“流行语”越来越多地出现在日常、无脚本的口语中。该研究分析了对话播客中的 2210 万个单词，显示自 2022 年 ChatGPT 发布以来，AI 频繁过度使用的词语，如“delve（深入研究）”、“intricate（复杂的）”、“underscore（强调）”、“surpass（超越）”、“boast（拥有）”、“meticulous（一丝不苟的）”、“strategically（战略性地）”和“garner（获得）”的使用量显著增加。

这表明存在一种“渗入效应”，即人工智能对人类语言模式的影响不仅仅是使用该工具。研究人员发现，与人工智能相关的词语的使用量增加并没有与其同义词的使用量增加相匹配。

这项研究引发了人们对人工智能模型偏差和错位如何通过语言影响人类行为的担忧。该研究建立在该团队之前研究的基础上，该研究强调了人工智能对科学写作产生的大规模结构性变化。研究人员计划继续调查人工智能是在放大现有的语言趋势，还是直接驱动它们。

---

## 50. 自9月1日起，我们需要对密西西比州的IP地址进行地理封锁。

**原文标题**: Beginning 1 September, we will need to geoblock Mississippi IPs

**原文链接**: [https://dw-news.dreamwidth.org/44429.html](https://dw-news.dreamwidth.org/44429.html)

自9月1日起，公司将对所有源自密西西比州的互联网协议(IP)地址实施地理封锁。该文件表明，从密西西比州连接的用户可能会遇到验证其请求的验证码(CAPTCHA)检查。这可能表明实施了一项新的政策或措施，以限制或监控来自密西西比州的访问。

---

## 51. 丰田回收旧电动车电池为马自达生产线供电

**原文标题**: Toyota is recycling old EV batteries to help power Mazda's production line

**原文链接**: [https://www.thedrive.com/news/toyota-is-recycling-old-ev-batteries-to-help-power-mazdas-production-line](https://www.thedrive.com/news/toyota-is-recycling-old-ev-batteries-to-help-power-mazdas-production-line)

丰田在马自达广岛工厂实地测试其Sweep储能系统，将退役电动汽车电池再利用，以帮助为生产线供电。Sweep系统收集来自电动和混合动力汽车的各种高压电池，无论其化学成分或衰减程度如何，并将它们连接到电网。丰田的能源管理逻辑优先使用健康的电池，并绕过较弱的电池，从而优化能量流动。一个关键的成本节约方面是重复使用电动汽车上的逆变器，从而无需额外的电力调节器。

马自达广岛园区配备了自己的热能和太阳能发电站，为测试Sweep系统提供了理想的环境。该集成系统调节电力供需，特别是来自波动性可再生能源的供需，从而有助于实现碳中和目标。该系统允许马自达通过使用不再适用于汽车的现有电池为其设施的部分区域供电，从而实现更环保的足迹。

最初的Sweep系统于2022年与JERA联合推出，证明了其为一个小时内超过1200户家庭供电的能力。该系统在处理各种质量和化学成分的电池方面的灵活性是实际回收和广泛采用的关键优势。

---

## 52. 环联称黑客窃取440万客户个人信息

**原文标题**: TransUnion says hackers stole 4.4M customers' personal information

**原文链接**: [https://techcrunch.com/2025/08/28/transunion-says-hackers-stole-4-4-million-customers-personal-information/](https://techcrunch.com/2025/08/28/transunion-says-hackers-stole-4-4-million-customers-personal-information/)

TransUnion披露数据泄露，440万客户信息受影响。

---

## 53. 可塑软件

**原文标题**: Malleable Software

**原文链接**: [https://www.mdubakov.me/malleable-software-will-eat-the-saas-world/](https://www.mdubakov.me/malleable-software-will-eat-the-saas-world/)

AI时代，可塑软件将取代硬编码软件

---

## 54. 我只买装有GrapheneOS的设备。

**原文标题**: I'll only buy devices with GrapheneOS

**原文链接**: [https://www.jonashietala.se/blog/2025/08/28/ill_only_buy_devices_with_grapheneos/](https://www.jonashietala.se/blog/2025/08/28/ill_only_buy_devices_with_grapheneos/)

本文倡导使用搭载GrapheneOS的设备以重新掌控个人数据并对抗日益增长的数字监控。作者对专制趋势以及企业和政府侵入式的数据收集表示担忧，认为标准智能手机正沦为控制工具，充斥着臃肿软件，并被设计用于追踪用户活动。

作者虽承认“功能机”的吸引力，但强调了智能手机应用在现代生活中的必要性（银行、身份验证）。GrapheneOS，一个去谷歌化的安卓操作系统，被认为是一个更优的选择，在不牺牲功能的前提下，优先考虑隐私和安全。

作者分享了自己在Pixel平板上安装GrapheneOS的积极体验，强调其简单的安装过程和应用兼容性。虽然某些应用（如BankID和MacroFactor）需要进行一些小的调整，但Play商店中的大多数应用都可以无缝运行。

本文强调GrapheneOS对隐私和安全的承诺，超过了其他基于安卓的系统。作者虽承认苹果可能提供比谷歌更好的隐私保护，但由于侵入式广告而表达了不信任。

作者承认硬件选择有限（仅支持Pixel设备），但将软件置于硬件之上，认为软件是决定设备实用性和寿命的关键。三星更新导致性能下降的糟糕软件体验，说明了用户控制和自主性的重要性，而GrapheneOS正提供了这种控制和自主性。作者总结说，未来只会购买受GrapheneOS支持的设备。

---

## 55. 像汽车一样大的石头正从多洛米蒂山脉飞落。

**原文标题**: 'Rocks as big as cars' are flying down the Dolomites

**原文链接**: [https://www.bbc.com/future/article/20250819-why-italys-beloved-ancient-monolith-is-falling](https://www.bbc.com/future/article/20250819-why-italys-beloved-ancient-monolith-is-falling)

意大利多洛米蒂山，联合国教科文组织世界遗产地，正经历越来越多的落石和滑坡，引发对其稳定性和未来的担忧。文章探讨了这一现象背后的原因，指出该地区的地质构成——多洛米亚石下方有一层柔软的粘土——以及气候变化的影响。

安东尼奥·加尔加罗教授解释说，这些山脉天生就容易崩塌，他将它们的结构比作逐渐崩解的“意大利圣诞面包”。他指出，五塔中的“英国塔”正在显示即将崩塌的迹象。

气候变化通过增加强降雨加剧了这一问题，导致水渗入裂缝，冻结和融化，削弱了岩石。 “散热器效应”，即破裂的岩石更快地加热和冷却，进一步加速了这一过程。

虽然滑坡是多洛米蒂山自然演变的一部分，但专家观察到其频率和不可预测性有所增加。传统的风险评估方法正变得不可靠。专家们没有试图阻止这些自然过程，而是专注于监测山脉、开发预警系统以及学会与风险共存。意大利环境和研究保护研究所管理着一个地图数据库，以提高人们对过去滑坡的认识。登山者也在适应，开始在一天中较早的时候进行攀登。虽然这些变化令人担忧，但专家们强调，多洛米蒂山是一个自然遗址，本质上会受到自然力量的影响。

---

## 56. Rust 意外带来的生产力提升

**原文标题**: Unexpected productivity boost of Rust

**原文链接**: [https://lubeno.dev/blog/rusts-productivity-curve](https://lubeno.dev/blog/rusts-productivity-curve)

无法访问文章链接。

---

## 57. 自带代理到 Zed - 支持 Gemini CLI

**原文标题**: Bring Your Own Agent to Zed – Featuring Gemini CLI

**原文链接**: [https://zed.dev/blog/bring-your-own-agent-to-zed](https://zed.dev/blog/bring-your-own-agent-to-zed)

Zed 集成第三方代理，以 Google Gemini CLI 为初始参考实现，通过 Agent Client Protocol (ACP) 实现。ACP 旨在使开发者能够在 Zed 中无缝切换不同的代理，类似于 Language Server Protocol 对语言智能的作用方式。

与 Google 的合作源于 Gemini CLI 在 Zed 终端中的积极体验。为了促进更深入的集成，我们定义了一组最小化的 JSON-RPC 端点，形成了 ACP。该协议允许任何客户端与任何遵循其 schema 的代理进行通信。

通过运行 Gemini CLI 作为 speaking ACP 的子进程，Zed 将相同的功能集成到以软件开发为中心的环境中。这解锁了诸如实时编辑可视化、多缓冲区审查以及代码和代理交互之间的流畅导航等功能。

文章强调，与第三方代理交互时，用户代码保持私密。ACP 在 Apache 许可下开源，鼓励代理开发者基于 Gemini CLI 的实现进行构建。Zed 的内部代理也已更新为使用与第三方代理相同的代码路径，从而确保 UI 的一致性。

作者鼓励大家对 ACP 做出贡献和反馈，旨在培育一个代理和客户端的生态系统。他们还提到正在努力推广该协议在其他编辑器（如 Neovim）中的应用。最后，他们邀请读者试用 Zed 并探索 ACP 功能，并着重介绍了对软件开发工具充满热情的人的职位空缺。

---

## 58. VIM 大师

**原文标题**: VIM Master

**原文链接**: [https://github.com/renzorlive/vimmaster](https://github.com/renzorlive/vimmaster)

VIM Master 是一款轻量级的浏览器游戏，旨在通过简短、专注的关卡教授核心的 Vim 移动和编辑命令。它无需安装；用户只需在浏览器中打开 `index.html` 即可。游戏包含普通/插入模式、命令日志、结果验证关卡，并支持各种 Vim 命令，包括移动 (h, j, k, l, w, b, e, gg, G, 0, $)、编辑 (x, dd, dw, yy, p, i, a, o/O, cw, D, r) 和 ex 命令 (:q, :wq)，以及数字计数和撤销/重做功能。

游戏融入了 Vim 风格的搜索功能 (/, ?)、匹配高亮显示以及完成时的庆祝动画。它包含一个用于进度的徽章系统（初学者，搜索大师），以及一个用于快速命令练习的作弊模式 (Ctrl+/)。关卡涵盖诸如退出、基本移动、单词移动、行跳转、插入模式、删除基础、复制和粘贴、行边界、追加行、更改单词、删除到结尾和替换、计数、撤销/重做和搜索等主题。

挑战模式测试在时间压力下的 Vim 命令记忆，根据速度和准确性提供积分。交互式速查表提供了一个可搜索和可过滤的命令列表，其中包含描述和示例，并且已练习的命令会被突出显示。关卡通过将结果与目标进行比较来验证，而不是严格的击键强制执行。

该游戏使用纯 HTML/CSS/JS 构建，使用 Tailwind CDN 进行样式设置，并且没有依赖项。该项目接受贡献，重点是可读的代码和小型、专注的关卡。许可证为 MIT。可以通过克隆 GitHub 存储库并在浏览器中打开 `index.html` 在本地运行游戏。

---

## 59. 英特尔高管离职，执掌亚德诺半导体俄勒冈工厂

**原文标题**: Intel exec quits to run Analog Devices' Oregon factory

**原文链接**: [https://www.oregonlive.com/silicon-forest/2025/08/intel-exec-quits-to-run-analog-devices-oregon-factory.html](https://www.oregonlive.com/silicon-forest/2025/08/intel-exec-quits-to-run-analog-devices-oregon-factory.html)

英特尔25年老将Narahari Ramanuja离职，将执掌亚德诺半导体新扩建的俄勒冈工厂，凸显英特尔持续面临的领导力和技术挑战。此举是英特尔高管在成本削减、裁员（去年约3万人，其中俄勒冈至少5400人）以及努力适应不断变化的市场需求背景下离职的大趋势之一。

亚德诺半导体最近投资10亿美元升级其位于比弗顿的工厂，使其成为其最大的工厂，表明其致力于为各种工业和消费应用提供成熟的技术芯片。这与英特尔专注于领先芯片以及在关键工程师和科学家离职后，努力恢复技术的现状形成对比。包括Ann Kelleher、Matt Prince、Glenn Hinton、Sanjay Natarajan、Kaizad Mistry和Ryan Russell在内的其他几位关键技术专家今年也已退休或离开英特尔。文章还提到特朗普总统曾介入，利用联邦资金购买了价值90亿美元的英特尔股票。

---

## 60. 英国太阳能发电量创历史新高，部署加速。

**原文标题**: Strongest year on record for UK solar generation as deployment accelerates

**原文链接**: [https://www.pv-magazine.com/2025/08/28/strongest-year-on-record-for-uk-solar-generation-as-deployment-accelerates/](https://www.pv-magazine.com/2025/08/28/strongest-year-on-record-for-uk-solar-generation-as-deployment-accelerates/)

英国2025年上半年太阳能发电量创历史新高，较2024年同期增长32%，总计达9.91太瓦时。 这一激增归因于异常晴朗的天气和太阳能的持续部署。政府数据显示证实了这一趋势，2025年7月新增光伏装置22406个，新增容量106兆瓦。 英国目前的太阳能总容量为19.1吉瓦，分布在180万个装置中，较2024年7月增加1.3吉瓦。

总容量的很大一部分（42%，即8.1吉瓦）来自地面安装的太阳能发电场，其中包括2025年在差价合约（CfD）计划下开始运营的13个项目。 家庭屋顶安装也出现向更大规模发展的趋势，目前占新增家庭规模太阳能容量的一半，这与过去由上网电价补贴激励的小型装置相比发生了重大变化。 虽然小型阵列（高达4千瓦）占总容量的较大部分（4吉瓦），但今年迄今为止的容量增加在小型和中型（4-10千瓦）阵列之间几乎持平。

---

## 61. 你不应该在吸血的蚂蟥上撒盐 (2019)

**原文标题**: You shouldn't salt a leech that's sucking your blood (2019)

**原文链接**: [https://www.cbc.ca/news/science/bloodsuckers-1.5361074](https://www.cbc.ca/news/science/bloodsuckers-1.5361074)

加拿大广播公司新闻文章讨论了皇家安大略博物馆（ROM）名为“吸血鬼”的新展览，并驳斥了关于吸血动物，特别是水蛭的常见误解。该展览旨在向公众普及吸血动物的生物学、医学用途和文化意义。

一个重要的要点是建议不要用盐撒在正在吸血的水蛭上。根据皇家安大略博物馆生物学家的说法，这会导致水蛭将食物呕吐到伤口中，增加感染的风险。他们建议使用指甲或信用卡来破坏吸盘，或者等待水蛭自行脱落。

文章探讨了为什么吸血动物经常以腹股沟等区域为目标（为了不受干扰地进食），并强调了食人鱼对氨的吸引力，这可能会将其吸引到人类尿道。虽然水蛭本身不传播疾病，但蜱虫因其携带莱姆病和其他疾病的能力而被认为是主要的健康风险。气候变化被提及为可能扩大加拿大蚊媒疾病范围的因素。

除了风险之外，文章还强调了黑蝇等吸血动物的生态重要性以及水蛭的历史医学用途。它旨在促进对这些生物的更深入的了解和欣赏，展示它们迷人的适应能力和在生态系统中的作用。该展览包括活体标本和互动展示，以吸引公众。

---

## 62. “哇！”信号可能来自地外文明，且能量更强。

**原文标题**: The “Wow!” signal was likely from extraterrestrial source, and more powerful

**原文链接**: [https://www.iflscience.com/the-wow-signal-was-likely-from-an-extraterrestrial-source-and-more-powerful-than-we-thought-80561](https://www.iflscience.com/the-wow-signal-was-likely-from-an-extraterrestrial-source-and-more-powerful-than-we-thought-80561)

一项新研究重新审视了著名的“Wow！”信号，这个1977年探测到的神秘无线电信号，认为它极有可能起源于外星，且比最初认为的更强大。科学家们重新分析了来自大耳朵射电望远镜的档案数据，采用了现代信号分析技术和先前未发表的数据。

研究强烈表明该信号并非地面干扰或来自卫星，并有统计证据表明其并非射频干扰。研究团队发现该信号约为250央斯基，是先前估计的四倍。研究人员还发现了1977年和1978年出现的两个较弱的类似信号（“Wow2”和“Wow3”）。

该团队假设“Wow！”信号可能是一种“超辐射事件”，是由星际介质中小型、寒冷的氢云受到类似磁星耀斑的强烈辐射源触发的，类似于脉泽的耀斑。他们观察到来自此类云的类似窄带信号，尽管明显较弱。

虽然该研究并未明确证明该信号来自外星文明，但它完善了我们对信号特征和潜在来源的理解，有助于未来的SETI搜寻。该持续进行的项目将进一步分析存档数据中的不明信号，旨在揭开“Wow！”信号的起因。

---

## 63. GMP正在损坏Zen 5 CPU？

**原文标题**: GMP damaging Zen 5 CPUs?

**原文链接**: [https://gmplib.org/gmp-zen5](https://gmplib.org/gmp-zen5)

无法访问文章链接。

---

## 64. WebLibre：注重隐私的浏览器

**原文标题**: WebLibre: The Privacy-Focused Browser

**原文链接**: [https://docs.weblibre.eu/](https://docs.weblibre.eu/)

WebLibre是一个专注于隐私和可用性的新型独立网页浏览器项目。它基于Mozilla的Gecko引擎和Android组件构建，使其成为一个功能齐全的浏览器，支持Firefox移动插件。然而，该项目目前处于alpha阶段，这意味着用户应该预期频繁的更新、错误和潜在的重大更改。开发者鼓励用户在GitHub上报告他们遇到的任何问题。值得注意的是，F-Droid上提供的版本是目前唯一不依赖Google的版本。这突显了该浏览器的隐私重点及其提供更独立浏览体验的尝试。

---

## 65. 互联网接入服务商不受限于DMCA揭露身份传票——考克斯案

**原文标题**: Internet Access Providers Aren't Bound by DMCA Unmasking Subpoenas–In Re Cox

**原文链接**: [https://blog.ericgoldman.org/archives/2025/08/internet-access-providers-arent-bound-by-dmca-unmasking-subpoenas-in-re-cox.htm](https://blog.ericgoldman.org/archives/2025/08/internet-access-providers-arent-bound-by-dmca-unmasking-subpoenas-in-re-cox.htm)

本文探讨了第九巡回法院在*In re Subpoena of Internet Subscribers of Cox Communications, LLC*一案中的裁决，该裁决重申互联网接入提供商（IAPs）不受DMCA 512(h)揭露身份传票的约束。DMCA的512(h)条款允许版权所有者轻松获得传票，以从网络主机处识别涉嫌侵权者。然而，IAPs在DMCA的512(a)安全港条款下受到不同的对待，该条款提供了全面豁免，因为它们不“托管”内容，因此无法删除侵权材料。

法院重申，版权所有者不能向IAPs发送有效的512(c)(3)删除通知，这是获得512(h)传票的前提，因为IAPs不托管侵权内容。法院驳回了IAPs可以通过端口阻止等方法“禁用访问”的论点，因为这只会限制用户的访问，而不是文件本身的托管。

该裁决突出了一个冲突：版权所有者希望IAPs充当版权警察，终止屡次侵权者并通过传票识别他们。然而，DMCA不支持IAPs这样做。作者批评版权所有者尽管有先前的法院裁决，仍继续要求发出这些传票，并将此归因于IAPs的普遍合规以及版权所有者试图破坏DMCA。本文还提到了正在等待最高法院审理的*Cox v. Sony*一案，该案可能会影响IAPs的版权责任。作者认为，该裁决强化了法院书记员不应发布针对IAPs的512(h)传票的观点。最后，本文还提及了可能重启立法努力，对IAPs施加网站屏蔽义务。

---

## 66. GitHub网站在Safari上很慢

**原文标题**: The GitHub website is slow on Safari

**原文链接**: [https://github.com/orgs/community/discussions/170758](https://github.com/orgs/community/discussions/170758)

GitHub社区讨论：Safari浏览器上GitHub网站性能问题
        
此GitHub社区讨论帖报告了GitHub网站在Safari浏览器上的显著性能问题，尤其是在查看大型拉取请求或文件时。用户描述了网站的缓慢、高CPU占用率和无响应，使其几乎无法使用。

发帖人ghugues详细描述了他在强大的MacBook Pro上使用Safari 18.6时遇到的问题，并指出Chrome浏览器表现更好，但处理大型请求仍然吃力。其他几位用户纷纷加入，确认了在使用各种Safari版本（包括技术预览版）时也遇到类似情况。症状包括渲染速度慢、API操作（如订阅问题）延迟以及一般的UI迟缓，尤其是在拉取请求和自动完成框中。一些用户不得不使用替代浏览器或工具来自动在Chrome浏览器中打开GitHub链接。

karlcow指出了一个潜在原因，他认为Safari浏览器中由GitHub的CSS最近更改触发了CSS性能问题。他表示WebKit修复程序将在未来的版本中发布，但建议GitHub前端团队在此期间缓解该问题。另一位用户表示，登录GitHub会加剧问题。一个GitHub机器人确认了反馈，并指向更新日志和产品路线图以获取更新。一些用户正在使用替代方案，等待修复。

---

## 67. 姐妹悖论——反直觉概率

**原文标题**: The sisters "paradox" – counter-intuitive probability

**原文链接**: [https://blog.engora.com/2025/08/the-sisters-paradox-counter-intuitive.html](https://blog.engora.com/2025/08/the-sisters-paradox-counter-intuitive.html)

本文解释了概率学中违反直觉的“姐妹悖论”。问题是：一个家庭有两个孩子，已知至少有一个是女孩，那么两个孩子都是女孩的概率是多少？

本文论证了为什么常见的错误答案50%是错误的。它使用概率树来说明四种等概率的组合：男孩-男孩、男孩-女孩、女孩-男孩和女孩-女孩。已知至少有一个孩子是女孩排除了男孩-男孩选项，剩下三种可能性。这使得两个女孩的概率为1/3。

本文强调了理解“样本空间”（所有可能结果的集合）对于解决此类问题的重要性。它提供了另一个场景，即已知*老大*是女孩会改变样本空间，从而将概率改变为1/2。

作者建议通过计算机模拟来测试违反直觉的概率问题的解决方案，这也可以加深对问题的理解。在提供简化的解释的同时，本文承认了围绕该悖论的复杂性和争议。核心要点是在处理概率时要精确对待假设，考虑模拟，并避免仅仅依赖“常识”。

---

## 68. Prediction-Encoded Pixels image format

**原文标题**: Prediction-Encoded Pixels image format

**原文链接**: [https://github.com/ENDESGA/PEP](https://github.com/ENDESGA/PEP)

生成摘要时出错

---

## 69. Synthetic gasoline

**原文标题**: Synthetic gasoline

**原文链接**: [https://iere.org/what-is-synthetic-gasoline/](https://iere.org/what-is-synthetic-gasoline/)

生成摘要时出错

---

## 70. Monodraw

**原文标题**: Monodraw

**原文链接**: [https://monodraw.helftone.com/](https://monodraw.helftone.com/)

生成摘要时出错

---

## 71. The Therac-25 Incident (2021)

**原文标题**: The Therac-25 Incident (2021)

**原文链接**: [https://thedailywtf.com/articles/the-therac-25-incident](https://thedailywtf.com/articles/the-therac-25-incident)

生成摘要时出错

---

## 72. Efficient Array Programming

**原文标题**: Efficient Array Programming

**原文链接**: [https://github.com/razetime/efficient-array-programming](https://github.com/razetime/efficient-array-programming)

生成摘要时出错

---

## 73. Will Bardenwerper on Baseball's Betrayal of Its Minor League Roots

**原文标题**: Will Bardenwerper on Baseball's Betrayal of Its Minor League Roots

**原文链接**: [https://lithub.com/will-bardenwerper-on-baseballs-betrayal-of-its-minor-league-roots/](https://lithub.com/will-bardenwerper-on-baseballs-betrayal-of-its-minor-league-roots/)

生成摘要时出错

---

## 74. Republicans in Congress open probe into Wikipedia for alleged bias

**原文标题**: Republicans in Congress open probe into Wikipedia for alleged bias

**原文链接**: [https://www.usatoday.com/story/news/politics/2025/08/27/wikipedia-under-investigation-by-republicans/85855314007/](https://www.usatoday.com/story/news/politics/2025/08/27/wikipedia-under-investigation-by-republicans/85855314007/)

生成摘要时出错

---

## 75. UMichigan study: EVs are cleaner than ICEs over average vehicle life

**原文标题**: UMichigan study: EVs are cleaner than ICEs over average vehicle life

**原文链接**: [https://insideevs.com/news/770035/evs-vs-gas-emissions/](https://insideevs.com/news/770035/evs-vs-gas-emissions/)

生成摘要时出错

---

## 76. Object-oriented design patterns in C and kernel development

**原文标题**: Object-oriented design patterns in C and kernel development

**原文链接**: [https://oshub.org/projects/retros-32/posts/object-oriented-design-patterns-in-osdev](https://oshub.org/projects/retros-32/posts/object-oriented-design-patterns-in-osdev)

生成摘要时出错

---

## 77. Gemini 2.5 Flash Image

**原文标题**: Gemini 2.5 Flash Image

**原文链接**: [https://developers.googleblog.com/en/introducing-gemini-2-5-flash-image/](https://developers.googleblog.com/en/introducing-gemini-2-5-flash-image/)

生成摘要时出错

---

## 78. In-App Browsers: The worst erosion of user choice you haven't heard of (2024)

**原文标题**: In-App Browsers: The worst erosion of user choice you haven't heard of (2024)

**原文链接**: [https://open-web-advocacy.org/blog/in-app-browsers-the-worst-erosion-of-user-choice-you-havent-heard-of/](https://open-web-advocacy.org/blog/in-app-browsers-the-worst-erosion-of-user-choice-you-havent-heard-of/)

生成摘要时出错

---

## 79. Trump Family Cashes in on 'The Infinite Money Glitch'

**原文标题**: Trump Family Cashes in on 'The Infinite Money Glitch'

**原文链接**: [https://www.wsj.com/finance/investing/the-trump-family-cashes-in-on-the-infinite-money-glitch-edcaca1d](https://www.wsj.com/finance/investing/the-trump-family-cashes-in-on-the-infinite-money-glitch-edcaca1d)

生成摘要时出错

---

## 80. The man with a Home Computer (1967) [video]

**原文标题**: The man with a Home Computer (1967) [video]

**原文链接**: [https://www.youtube.com/watch?v=w6Ka42eyudA](https://www.youtube.com/watch?v=w6Ka42eyudA)

生成摘要时出错

---

## 81. A teen was suicidal. ChatGPT was the friend he confided in

**原文标题**: A teen was suicidal. ChatGPT was the friend he confided in

**原文链接**: [https://www.nytimes.com/2025/08/26/technology/chatgpt-openai-suicide.html](https://www.nytimes.com/2025/08/26/technology/chatgpt-openai-suicide.html)

生成摘要时出错

---

## 82. My Advice to Sam Altman: Read Jacques Derrida

**原文标题**: My Advice to Sam Altman: Read Jacques Derrida

**原文链接**: [https://observer.co.uk/news/columnists/article/my-advice-to-gpt-5-read-derrida-and-youll-learn-words-are-not-the-same-as-intelligence](https://observer.co.uk/news/columnists/article/my-advice-to-gpt-5-read-derrida-and-youll-learn-words-are-not-the-same-as-intelligence)

生成摘要时出错

---

## 83. What we find in the sewers

**原文标题**: What we find in the sewers

**原文链接**: [https://www.asimov.press/p/sewers](https://www.asimov.press/p/sewers)

生成摘要时出错

---

## 84. Areal, Are.na's new typeface

**原文标题**: Areal, Are.na's new typeface

**原文链接**: [https://www.are.na/editorial/introducing-areal-are-nas-new-typeface](https://www.are.na/editorial/introducing-areal-are-nas-new-typeface)

生成摘要时出错

---

## 85. Reverse-engineering the Globus INK, a Soviet spaceflight navigation computer (2023)

**原文标题**: Reverse-engineering the Globus INK, a Soviet spaceflight navigation computer (2023)

**原文链接**: [https://www.righto.com/2023/03/reverse-engineering-globus-ink-soviet.html](https://www.righto.com/2023/03/reverse-engineering-globus-ink-soviet.html)

生成摘要时出错

---

## 86. Light pollution prolongs avian activity

**原文标题**: Light pollution prolongs avian activity

**原文链接**: [https://gizmodo.com/birds-across-the-world-are-singing-all-day-for-a-disturbing-reason-2000646257](https://gizmodo.com/birds-across-the-world-are-singing-all-day-for-a-disturbing-reason-2000646257)

生成摘要时出错

---

## 87. China Is Eating the World

**原文标题**: China Is Eating the World

**原文链接**: [https://apropos.substack.com/p/china-is-eating-the-world](https://apropos.substack.com/p/china-is-eating-the-world)

生成摘要时出错

---

## 88. Implementing Forth in Go and C

**原文标题**: Implementing Forth in Go and C

**原文链接**: [https://eli.thegreenplace.net/2025/implementing-forth-in-go-and-c/](https://eli.thegreenplace.net/2025/implementing-forth-in-go-and-c/)

生成摘要时出错

---

## 89. China Is Eating the World

**原文标题**: China Is Eating the World

**原文链接**: [https://apropos.substack.com/p/china-is-eating-the-world](https://apropos.substack.com/p/china-is-eating-the-world)

生成摘要时出错

---

## 90. Typepad is shutting down

**原文标题**: Typepad is shutting down

**原文链接**: [https://everything.typepad.com/blog/2025/08/typepad-is-shutting-down.html](https://everything.typepad.com/blog/2025/08/typepad-is-shutting-down.html)

生成摘要时出错

---

## 91. QEMU 10.1.0

**原文标题**: QEMU 10.1.0

**原文链接**: [https://wiki.qemu.org/ChangeLog/10.1](https://wiki.qemu.org/ChangeLog/10.1)

生成摘要时出错

---

## 92. A mini-book on AWS networking

**原文标题**: A mini-book on AWS networking

**原文链接**: [https://www.ducktyped.org/p/a-mini-book-on-aws-networking-introduction](https://www.ducktyped.org/p/a-mini-book-on-aws-networking-introduction)

生成摘要时出错

---

## 93. Show HN: FilterQL – A tiny query language for filtering structured data

**原文标题**: Show HN: FilterQL – A tiny query language for filtering structured data

**原文链接**: [https://github.com/adamhl8/filterql](https://github.com/adamhl8/filterql)

生成摘要时出错

---

## 94. ETFs Are Inflating the Everything Bubble

**原文标题**: ETFs Are Inflating the Everything Bubble

**原文链接**: [https://www.vincentschmalbach.com/etfs-are-inflating-the-everything-bubble/](https://www.vincentschmalbach.com/etfs-are-inflating-the-everything-bubble/)

生成摘要时出错

---

## 95. That boolean should probably be something else

**原文标题**: That boolean should probably be something else

**原文链接**: [https://ntietz.com/blog/that-boolean-should-probably-be-something-else/](https://ntietz.com/blog/that-boolean-should-probably-be-something-else/)

生成摘要时出错

---

## 96. SpaCy: Industrial-Strength Natural Language Processing (NLP) in Python

**原文标题**: SpaCy: Industrial-Strength Natural Language Processing (NLP) in Python

**原文链接**: [https://github.com/explosion/spaCy](https://github.com/explosion/spaCy)

生成摘要时出错

---

## 97. Using information theory to solve Mastermind

**原文标题**: Using information theory to solve Mastermind

**原文链接**: [https://www.goranssongaspar.com/mastermind](https://www.goranssongaspar.com/mastermind)

生成摘要时出错

---

## 98. Why do people keep writing about the imaginary compound Cr2Gr2Te6?

**原文标题**: Why do people keep writing about the imaginary compound Cr2Gr2Te6?

**原文链接**: [https://www.righto.com/2025/08/Cr2Ge2Te6-not-Cr2Gr2Te6.html](https://www.righto.com/2025/08/Cr2Ge2Te6-not-Cr2Gr2Te6.html)

生成摘要时出错

---

## 99. Claude for Chrome

**原文标题**: Claude for Chrome

**原文链接**: [https://www.anthropic.com/news/claude-for-chrome](https://www.anthropic.com/news/claude-for-chrome)

生成摘要时出错

---

## 100. AI coding made me faster, but I can't code to music anymore

**原文标题**: AI coding made me faster, but I can't code to music anymore

**原文链接**: [https://www.praf.me/ai-coding](https://www.praf.me/ai-coding)

生成摘要时出错

---

