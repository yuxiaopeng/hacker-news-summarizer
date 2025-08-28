# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-08-28.md)

*最后自动更新时间: 2025-08-28 17:47:22*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 2 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 3 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 4 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 5 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 6 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 7 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 8 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 9 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 10 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 11 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 12 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 13 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 14 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 15 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 16 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 17 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 18 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 19 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 20 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 21 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 22 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 23 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 24 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 25 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 26 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 27 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 28 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 29 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 30 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 31 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 32 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 33 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 34 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 35 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 36 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 37 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 38 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 39 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 40 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 41 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 42 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 43 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 44 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 45 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 46 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 47 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 48 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 49 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 50 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 51 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 52 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 53 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 54 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 55 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 56 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 57 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 58 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 59 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 60 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 61 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 62 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 63 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 64 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 65 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 66 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 67 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 68 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 69 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 70 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 71 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 72 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 73 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 74 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 75 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 76 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 77 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 78 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 79 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 80 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 81 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 82 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 83 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 84 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 85 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 86 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 87 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 88 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 89 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 90 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 91 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 92 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 93 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 94 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 95 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 96 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 97 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 98 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 99 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 100 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 101 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 102 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 103 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 104 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 105 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 106 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 107 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 108 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 109 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 110 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 111 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 112 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 113 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 114 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 115 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 116 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 117 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 118 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 119 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 120 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 121 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 122 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 123 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 124 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 125 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 126 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 127 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 128 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 129 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 130 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 131 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 132 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 133 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 134 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 135 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 136 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 137 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 138 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 139 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 140 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 141 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 142 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 143 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 144 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 145 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 146 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 147 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 148 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 149 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 150 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 151 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 152 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 153 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 154 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 155 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 156 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 157 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 158 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 159 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 160 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 161 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 162 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
