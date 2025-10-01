# Hacker News 热门文章摘要 (2025-10-01)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Codeberg项目数量突破30万

**原文标题**: Codeberg Reaches 300k Projects

**原文链接**: [https://codeberg.org/](https://codeberg.org/)

无法访问文章链接。

---

## 2. 展示一下：自闭症模拟器

**原文标题**: Show HN: Autism Simulator

**原文链接**: [https://autism-simulator.vercel.app/](https://autism-simulator.vercel.app/)

“自闭症模拟器”是一款互动式教育工具，旨在模拟自闭症人士在职场中的体验。该模拟旨在提高人们对自闭症人士在专业环境中的理解和同情。通过让用户体验自闭症人士经常遇到的感官超载、社交挑战和认知处理差异，该模拟器希望促进更具包容性和支持性的工作环境。它可能是一种沉浸式体验，包含各种互动元素，以模仿自闭症人士面临的具体挑战，从而深入了解如何更好地适应工作场所以及同事如何提供更有效的支持。该工具的最终目的是教育和培养一个更具包容性和理解性的自闭症人士职场文化。

---

## 3. 构建堆：为预训练堆叠30拍字节硬盘

**原文标题**: Building the heap: racking 30 petabytes of hard drives for pretraining

**原文链接**: [https://si.inc/posts/the-heap/](https://si.inc/posts/the-heap/)

本文详细介绍了某公司如何在旧金山托管中心构建自己的 30PB 存储集群，用于在视频数据上预训练机器学习模型。他们选择这条路线是为了大幅降低成本，与 AWS 和 Cloudflare 等云存储选项相比。核心思想是，机器学习训练数据可以容忍更高的数据损坏率，从而使云的高冗余性和可用性变得不必要。

自建方案将每月成本显著降低至 29,500 美元（包括折旧），而 AWS 为 1,130,000 美元，Cloudflare 为 270,000 美元。该集群由安装在 NetApp 机箱中的二手企业级硬盘驱动器组成，由英特尔 CPU 头节点提供支持，并通过 100Gbps 网络连接。

本文概述了成本构成，涵盖互联网、电力、硬盘驱动器、机箱、服务器、数据中心设置和人工。他们强调了简单软件堆栈对于管理存储的重要性，选择了一个定制的 200 行 Rust 脚本，而不是像 Ceph 或 MinIO 这样更复杂的解决方案。

本文还包括设置过程中吸取的经验教训，包括硬件选择的技巧（避免前置加载器、选择更密集的阵列、避免菊花链连接）、兼容性的重要性以及 IPMI/KVM 的实用性。最后，本文列出了复制该设置所需的组件，包括具体的硬件建议。

---

## 4. Fossabot：针对Dependabot/Renovate中重大变更和影响的AI代码审查

**原文标题**: Fossabot: AI code review for Dependabot/Renovate on breaking changes and impacts

**原文链接**: [https://fossa.com/blog/fossabot-dependency-upgrade-ai-agent/](https://fossa.com/blog/fossabot-dependency-upgrade-ai-agent/)

FOSSA 宣布 Fossabot，一款旨在自动化 JavaScript 和 TypeScript 项目战略性依赖更新的 AI 代理，解决依赖频繁变动和更新停滞的问题。与 Dependabot 和 Renovate 等现有更新工具通常依赖简单的补丁级更新不同，Fossabot 分析代码库以了解更新的影响，提出适配方案，并通过拉取请求交付完成的任务。

Fossabot 通过理解应用上下文中的重大变更来平衡风险和收益，利用 EdgeBit 收购带来的静态分析能力来防止错误并提供准确的推理。这使其能够处理通常需要高级工程师才能完成的复杂升级。

该 AI 代理通过进行广泛的研究、参考文档并保持对代码库、依赖项和发行说明的全面记忆，从而超越了人类的能力。 Fossabot 使用准确性、一致性、正确性 (ACC) 框架进行评估，优先避免误报。

Fossabot 目前通过 GitHub 应用以公开预览版形式提供，每月提供免费额度，并与 Dependabot、Renovate 和 Snyk 集成，计划未来开放其自身的拉取请求。目标是减轻与依赖更新相关的繁琐工作，使开发团队能够专注于更高级别的任务。

---

## 5. Unix 哲学和文件系统访问让 Claude Code 变得出色。

**原文标题**: Unix philosophy and filesystem access makes Claude Code amazing

**原文链接**: [https://www.alephic.com/writing/the-magic-of-claude-code](https://www.alephic.com/writing/the-magic-of-claude-code)

诺亚·布里尔对 Claude Code 赞不绝口，称其为他主要的操作系统，尤其是在与 Obsidian 结合进行笔记记录时。他强调了使 Claude Code 卓越的两个关键要素：遵循 Unix 哲学和文件系统访问。

Unix 哲学强调简单、可组合的工具，专注做好一件事，这与 LLM 通过将输出“管道”到输入来有效利用工具的方式完美契合。这与复杂的工具形成对比，后者通常会阻碍 AI 性能。

文件系统访问解决了标准浏览器式 AI（如 ChatGPT 和 Claude）的局限性，这些 AI 存在内存不足和上下文窗口狭窄的问题。Claude Code 通过使用文件系统来编写笔记、积累知识和保持状态的能力，使其能够“思考”超出单个对话的范围。布里尔强调，模型有能力利用此功能，但其他界面限制了它们的能力。

他引用了 Boris Cherney 对“产品悬垂”的观察，即由于产品设计的限制，模型的性能未得到充分利用。布里尔通过开源 "Claudesidian" 和开发由 Claude Code 驱动的电子邮件助手 "Inbox Magic"，扩展了他的 Claude Code + Obsidian 设置。

总之，布里尔倡导利用文件系统来克服 LLM 中的内存限制，并坚持 Unix 哲学进行工具设计。他认为 Claude Code 的架构为构建可靠且可调试的 AI 代理提供了一个蓝图。

---

## 6. 展示HN：ChartDB Agent – 数据库模式设计的Cursor

**原文标题**: Show HN: ChartDB Agent – Cursor for DB schema design

**原文链接**: [https://app.chartdb.io/ai](https://app.chartdb.io/ai)

这篇“Show HN”帖子介绍了 ChartDB Agent，一个定位为“数据库模式设计的 Cursor”的工具。其核心理念是 ChartDB 帮助用户可视化数据库模式。它可能提供一个可视化界面或代理（可能是AI驱动的），以促进数据库模式的创建、理解和操作。

虽然帖子简短，但我们可以推断出以下几点：

*   **解决的问题：** 数据库模式设计可能很复杂且难以可视化，导致错误和效率低下。
*   **解决方案：** ChartDB 提供了一种可视化呈现和交互数据库模式的方式。
*   **主要功能：** 数据库模式的可视化。
*   **目标受众：** 开发人员、数据库管理员以及任何参与数据库设计的人员。
*   **潜在优势：** 提高理解、简化设计、减少数据库模式中的错误。
*   **“数据库模式设计的 Cursor”** 暗示 ChartDB 旨在成为数据库模式设计的首选工具，类似于 Cursor 是一款流行的代码编辑器。这表明其非常注重用户体验和效率。

本质上，ChartDB Agent 可能会通过可视化和直观的界面来简化和改进数据库模式的工作流程。

---

## 7. 麻省理工技术可远距离探测90米外的微生物

**原文标题**: MIT technology can see microbes from 90 meters away

**原文链接**: [https://www.asimov.press/p/hyperspectral](https://www.asimov.press/p/hyperspectral)

尼科·麦卡锡的文章探讨了生物传感器的进展，重点关注能够让我们从远处“看到”微生物的传感器开发。虽然自然界提供了多种多样的生物传感器，但生物工程师主要依赖于有限的报告蛋白，如GFP，这需要近距离观察。

最近，麻省理工学院的科学家开发了一种新型传感器，使用安装在无人机上的高光谱相机，可在高达90米远的距离内进行检测。这项技术在《自然·生物技术》杂志上进行了详细介绍，它能够监测工程细菌在生态系统中感应到的分子。

该突破涉及使用最初由美国宇航局开发的高光谱相机，来检测工程微生物产生的特定分子的独特光吸收和反射模式。研究人员确定胆绿素IXα和细菌叶绿素a为有效的“高光谱报告蛋白”。他们对恶臭假单胞菌和明胶红细菌进行了工程改造，使其产生这些分子，将微生物喷洒在土壤上，并成功地使用高光谱成像从空中检测到它们。

尽管具有潜力，但这种工程微生物的环境释放面临监管障碍。美国环保署监督的《有毒物质控制法》(TSCA)基于其工程方法而非安全性来监管这些微生物。虽然像Pivot Bio这样的一些公司已经克服了这些监管，但文章强调，过时的规则阻碍了环境生物传感器的商业化。文章强调了推进传感器技术以测量以前无法到达的位置的生物学的重要性，以及更新法规以促进这些技术负责任应用的需求。

---

## 8. 我们的努力，部分地，定义了我们。

**原文标题**: Our efforts, in part, define us

**原文链接**: [https://weakty.com/posts/efforts/](https://weakty.com/posts/efforts/)

本文探讨了作者作为软件顾问，对人工智能在其工作中日益增长的作用所产生的矛盾情绪，以及自动化对身份和成就感的更广泛影响。作者纠结于“我们的努力在某种程度上定义了我们”的观点，并质疑当技术使原本费力的任务变得毫不费力时会发生什么。

作者以摄影师因数码摄影的普及而失去热情为例，说明了技术简化任务时可能出现的“隐性损失”。他们担心，在编码中越来越多地使用人工智能，虽然可能是有益的，但会降低从这项技能中获得的价值和乐趣，从而导致一种悲伤和意义丧失的感觉。

作者注意到领导层推动在工作场所整合人工智能，并对员工体验的贬值以及对生产优先于个人视角的担忧表示关注。他们承认人工智能仅仅是一种工具的观点，但仍然强调他们的匮乏感和失落感。

最终，作者对日益自动化的世界中工作和身份的未来感到疑惑。他们质疑人们是否会被驱使去从事更小众、更费力的活动，还是会变得沮丧和模糊不清。他们也承认，对于某些人来说，人工智能可能会让他们自由地追求生活中其他有意义的方面。然而，作者仍然怀疑，除非对工作的期望得到改革，否则这些技术进步是否会提高士气。作者以质疑的口吻结束，即是否值得付出努力。

---

## 9. 我只用谷歌表格。

**原文标题**: I only use Google Sheets

**原文链接**: [https://mayberay.bearblog.dev/why-i-only-use-google-sheets/](https://mayberay.bearblog.dev/why-i-only-use-google-sheets/)

为什么我只用 Google Sheets

---

## 10. 激光网络协议

**原文标题**: IP over Lasers

**原文链接**: [https://www.mikekohn.net/micro/ip_over_lasers.php](https://www.mikekohn.net/micro/ip_over_lasers.php)

迈克·科恩的文章《激光上的IP协议》描述了一个使用激光链路通过互联网协议（IP）传输数据的项目。该项目旨在建立一种使用光而不是无线电波的无线网络连接。

作者详细介绍了所使用的硬件和软件组件。硬件包括激光器、光电二极管、用于聚焦激光束的透镜和微控制器（本例中为PIC微控制器）来调制和解调数据。该项目使用简单的开关键控（OOK）调制，其中激光器要么打开（表示“1”），要么关闭（表示“0”）。

该软件涉及将IP数据包编码成可以通过激光链路传输的比特流。PIC微控制器被编程为处理串行通信、调制和解调。作者使用一台PC来生成和接收IP数据包，然后将其发送到微控制器，以便通过激光链路传输。

文章重点介绍了项目过程中遇到的一些挑战。这些挑战包括精确对准激光器和光电二极管、处理环境光干扰以及确保可靠的数据传输。作者还讨论了简单OOK调制方案的局限性，并建议更复杂的调制技术可以提高性能。

本质上，这篇文章记录了作者创建基于激光的基本、低带宽IP通信系统的实验，说明了这种无线通信中涉及的基本原理和挑战。它作为IP通信概念和微控制器在独特网络环境中的应用的实际演示。

---

## 11. Uxntal：Uxn虚拟机编程语言

**原文标题**: Uxntal: A programming language for the Uxn virtual machine

**原文链接**: [https://wiki.xxiivv.com/site/uxntal.html](https://wiki.xxiivv.com/site/uxntal.html)

本文介绍了Uxntal，一种为Uxn虚拟机设计的串联汇编编程语言。Uxntal使用后进先出(LIFO)的基于堆栈的系统进行计算，并使用十六进制数进行运算。程序由操作码、地址和标签组成。

主要概念包括：

*   **堆栈操作：** Uxntal严重依赖于使用POP、NIP、SWP、ROT、DUP和OVR等原语来操作工作堆栈和返回堆栈。
*   **十六进制数：** 数字以十六进制格式（小写）表示，既可以是字面十六进制（以`#`为前缀）以将值推入堆栈，也可以是用于数据编码的原始十六进制。
*   **操作码：** Uxn有32个标准操作码和4个立即操作码（LIT、跳转、条件跳转、子程序），它们决定操作，模式(2, k, r)修改它们的行为（短、保持、返回）。
*   **标签：** 标签（以`@`、`&`或`/`为前缀）用于定义内存位置、函数、常量、枚举和结构体，以提高可读性。还有相对、零页和绝对寻址符文。
*   **寻址：** 有几个寻址前缀，包括字面和原始寻址符文，用于指定位置。
*   **匿名标签：** 匿名标签用花括号表示，用于条件跳转和数据结构。
*   **宏：** 宏允许定义在编译期间被其主体替换的内联例程。
*   **注释：** 注释用括号括起来。

本文强调可读性，并提供了有效语法的摘要，包括符文和方括号的使用。

---

## 12. 为何Python在2025年如此流行？– PyCharm博客

**原文标题**: Why Is Python So Popular in 2025? – The PyCharm Blog

**原文链接**: [https://blog.jetbrains.com/pycharm/2025/09/why-is-python-so-popular/](https://blog.jetbrains.com/pycharm/2025/09/why-is-python-so-popular/)

PyCharm博客文章“为何Python在2025年依然如此流行？”探讨了Python在开发者中持续流行的原因。文章强调了Python的广泛应用，将其列为第二大常用语言，57%的开发者都在使用它，34%的开发者认为它是他们的主要语言，超过了JavaScript、Java和TypeScript。

文章指出Python在人工智能和机器学习（ML）领域的统治地位，41%的Python开发者将其用于机器学习。其富有表现力的语法以及PyTorch、TensorFlow、Keras和Hugging Face Transformers等丰富的框架生态系统是这种统治地位的关键。Python在数据科学和分析方面的优势也得到了认可，51%的开发者使用它来执行ETL、EDA、统计建模和可视化等任务，这要归功于pandas、NumPy和Matplotlib等库。

Python的简单且可扩展的语法、成熟且多功能的生态系统（包括Web开发、人工智能/机器学习、测试、自动化和数据科学）、强大的社区支持以及跨领域的多功能性被认为是至关重要的因素。开发者可以轻松地在软件开发的不同方面之间切换，并使用高级封装进行原型设计，或根据需要降低到较低级别的控制。作者强调了Python在智能开发时代持续的相关性，以及它对初学者的可访问性，同时可以扩展到高级项目。文章还引用了“2025年Python状况”报告，该报告分析了来自大规模开发者调查的数据。

---

## 13. 从零开始构建物联网通知设备

**原文标题**: Building an IoT Notification Device from Scratch

**原文链接**: [https://bertwagner.com/posts/splashflag-building-an-iot-swimming-notification-device-from-scratch/](https://bertwagner.com/posts/splashflag-building-an-iot-swimming-notification-device-from-scratch/)

本文详细介绍了“SplashFlag”的创建过程，这是一个从零开始构建的物联网设备，用于在作者的孩子们游泳时通知邻居并邀请他们加入。作者概述了该项目的动机、功能和经验教训。

主要功能包括一个伺服控制的旗帜，在收到通知时升起，一个显示自定义消息（例如，游泳时长、披萨邀请）的LCD屏幕，以及一个清除/重置按钮。该设备包含一个强制门户，方便进行Wi-Fi设置，无需硬编码密码，并支持空中下载（OTA）更新，以便进行远程固件维护。

该系统使用MQTT代理进行实时消息传输，使设备能够避免持续的服务器轮询。一个Web应用程序允许作者向所有设备发送自定义消息，包括一个调试功能，可以定位到特定单元。

本文还介绍了3D打印外壳的设计，强调了迭代测试的重要性以及对配合、组装和组件集成的设计考虑。虽然由于时间限制，未包含TLS加密和凭证的安全存储，但作者对项目的成果及其未来迭代的潜力表示满意。

本文最后提供了一个零件清单、代码仓库链接，以及基本的组装/接线说明，供有兴趣构建自己的SplashFlag的读者参考。

---

## 14. 疾控中心文件传输

**原文标题**: CDC File Transfer

**原文链接**: [https://github.com/google/cdc-file-transfer](https://github.com/google/cdc-file-transfer)

本文档介绍了CDC文件传输，一套旨在高效地同步和流式传输Windows到Linux文件的工具，源于Stadia开发环境。它解决了开发者在Windows上工作并部署到Linux实例时面临的缓慢文件传输问题。

该套件包含两个主要工具：`cdc_rsync`和`cdc_stream`。 `cdc_rsync`是一个文件同步工具，它利用内容定义分块（CDC）来识别和传输文件的更改部分，与标准`rsync`相比，显著缩短了同步时间。 基准测试表明，它比Cygwin rsync快3倍。

`cdc_stream`支持将文件和目录从Windows流式传输到Linux，并在Linux端进行缓存。它同样使用基于CDC的差异比较来最小化数据传输，仅流式传输更改。与`sshfs`相比，这提供了更快的读取速度，并在Windows文件更改时在Linux端提供近乎瞬时的更新。

本文档概述了支持的平台（主要为Windows x86_64到Linux Ubuntu 22.04 x86_64），提供了下载预编译二进制文件或从源代码构建的说明，并详细说明了必要的先决条件（Bazel，SSH客户端）。它强调了无密码SSH/SFTP配置的必要性。最后，它提供了`cdc_rsync`和`cdc_stream`的用法示例，以及故障排除提示和启用调试日志的指导。

---

## 15. 类型论与函数式编程 (1999) [pdf]

**原文标题**: Type Theory and Functional Programming (1999) [pdf]

**原文链接**: [https://www.cs.cornell.edu/courses/cs6110/2015sp/textbook/Simon%20Thompson%20textbook.pdf](https://www.cs.cornell.edu/courses/cs6110/2015sp/textbook/Simon%20Thompson%20textbook.pdf)

此文档似乎是名为“类型论与函数式编程 (1999)”的 PDF 文件的部分损坏或不完整的表示。由于 PDF 结构内存在无法读取的压缩数据流，因此无法确定论文的任何实际内容。`/Type /Page`、`/Font`、`/ProcSet` 和 `/FlateDecode` 等 PDF 元素的存在表明了 PDF 文档的典型结构。此外，标题表明主题围绕类型论与函数式编程的交叉领域，该领域关注于使用形式类型系统来增强函数式编程语言的安全性、正确性和表达性。 文件结构显示它由许多页面组成。但是，由于内容已被编码，因此无法提供文章实际观点或论证的摘要。

---

## 16. 范畴论图解 – 自然变换

**原文标题**: Category Theory Illustrated – Natural Transformations

**原文链接**: [https://abuseofnotation.github.io/category-theory-illustrated/11_natural_transformations/](https://abuseofnotation.github.io/category-theory-illustrated/11_natural_transformations/)

本文深入探讨范畴论中自然变换的概念，阐释其在定义范畴等价（相等）中的重要性。文章首先对比巴门尼德（强调永恒）和赫拉克利特（强调变化）的哲学观点，以此引出范畴论中从对象到态射（关系）的关注点转变。同构不变性，即认为同构对象本质上相等，对范畴论至关重要。

文章强调，范畴同构虽然重要，但不足以定义范畴间的相等关系，因为它不具备同构不变性。因此，引入了一个新的概念，即等价。如果通过函子在两个范畴之间来回转换，结果得到与原始对象同构的对象，则这两个范畴是等价的。

文章最初尝试用对象来定义等价性，但最终强调了态射的重要性。它通过首先定义集合同构，然后定义范畴同构，逐步建立起用态射来定义等价性的方法。最终，文章使用函子给出了范畴等价的定义：如果存在函子f: A -> B和g: B -> A，使得f o g与B上的恒等函子同构，且g o f与A上的恒等函子同构，则两个范畴A和B是等价的。这个定义依赖于函子同构的概念，这促使文章引入了自然变换。作者解释说，自然变换是函子之间的态射，这是定义函子同构和范畴等价的关键部分。

---

## 17. 光标 1.7

**原文标题**: Cursor 1.7

**原文链接**: [https://cursor.com/changelog/1-7](https://cursor.com/changelog/1-7)

Cursor 1.7于2025年9月29日发布，引入了以下几项关键特性和改进：

*   **代理自动补全：** 在编写提示词时，基于近期变更提供智能自动补全建议，简化代理交互。
*   **钩子 (Beta)：** 允许用户通过自定义脚本定制和扩展代理行为，实现审计、命令阻止和敏感信息移除。
*   **团队规则：** 允许通过仪表板创建和共享整个团队的全局规则，确保行为一致性，包括Bugbot代理。
*   **可共享提示词 (Beta)：** 通过深度链接促进可重用提示词的共享，适用于文档、团队资源和工作流程共享。
*   **菜单栏监控：** 允许直接从菜单栏快速检查Cursor代理的状态。
*   **代理图像支持：** 代理现在可以访问和整合工作区中的图像文件，扩展上下文感知。

此次发布侧重于增强代理的可用性、定制性和协作性。

---

## 18. 文艺复兴节是如何开始的？

**原文标题**: How did Renaissance fairs begin?

**原文链接**: [https://www.history.com/articles/renaissance-fair-origins](https://www.history.com/articles/renaissance-fair-origins)

文艺复兴博览会，如今以烤火鸡腿和马上比武闻名，起源于 20 世纪 60 年代的洛杉矶，最初是一项反主流文化活动。教师菲利斯·帕特森和艺术指导罗恩·帕特森于 1963 年组织了第一个文艺复兴游乐会和五月集市，作为 KPFK/Pacifica 电台的筹款活动。该活动以时代服装、表演和手工工艺品为特色，每天吸引了 3000 多名参与者。

博览会的成功部分归功于被好莱坞列入黑名单的艺术家的参与。它成为一种挑战冷战时期保守主义的反主流文化理念的空间。博览会迅速发展，搬到更大的场地，并成为 KPFK 的重要收入来源。身着文艺复兴时期服装的参与者模糊了表演者和观众之间的界限。

1967 年爆发了争议，指控存在毒品使用和对控制权的争端，导致帕特森夫妇与 Pacifica 电台断绝了联系。尽管面临挑战，博览会仍然蓬勃发展，并吸引了著名的游客。

到 20 世纪 70 年代，文艺复兴博览会遍布美国，融合了历史和幻想。包括最初的博览会在内的许多博览会后来被企业实体收购，转向商业企业。如今，每年都会举办 200 多个文艺复兴博览会，它们仍然吸引着另类社群和家庭观众，提供了历史、幻想和社会评论的独特融合。

---

## 19. 失忆症与迷幻药

**原文标题**: Aphantasia and Psychedelics

**原文链接**: [https://psychedelirium.substack.com/p/aphantasia-and-psychedelics](https://psychedelirium.substack.com/p/aphantasia-and-psychedelics)

无法访问文章链接。

---

## 20. 别想了Figma，我不会屈就于你的小框框。

**原文标题**: No Figma, I won't fit in your little box

**原文链接**: [https://blog.nordcraft.com/no-figma-i-wont-fit-in-your-little-box](https://blog.nordcraft.com/no-figma-i-wont-fit-in-your-little-box)

Andreas Møller的文章《不，Figma，我不会适应你的小盒子》认为，软件开发中“设计师”和“开发者”之间的传统分离不利于创造力和效率。这种由Figma等工具强化的分离导致了一个问题重重的交接过程，设计师们孤立地创建UI，往往忽略了诸如交互和可访问性等功能方面。

作者认为，设计工具未能跟上现代CSS的能力，迫使设计师进入一个越来越小的“盒子”，受到过时的范例的限制，如基于像素的设计和缺乏交互性。这导致即使是简单的设计迭代也会由于交接过程中的摩擦而变得繁琐。

Møller批评了行业试图修复交接症状而不是解决根本原因的做法：设计师和开发者使用的语言和工具集的不同。他否定了代码是合适的的設計媒介的观点，并介绍了Nordcraft作为一种替代方法。

Nordcraft旨在通过提供一个基于HTML和CSS的统一工具来弥合差距，使设计师和开发者可以在同一环境中进行协作。这消除了交接，并使团队能够利用每个成员的优势，无论他们的传统角色如何。作者总结说，这种集成方法可以培养敏捷性、实验性和最终更好的设计。

---

## 21. 最高法院允许美联储理事库克在1月口头辩论前保留职位。

**原文标题**: Supreme Court lets Fed Governor Cook keep job pending oral argument in January

**原文链接**: [https://www.cnbc.com/2025/10/01/supreme-court-trump-fed-lisa-cook.html](https://www.cnbc.com/2025/10/01/supreme-court-trump-fed-lisa-cook.html)

最高法院允许库克继续担任美联储理事，特朗普试图罢免案延至一月口头辩论。特朗普指控库克犯有房贷欺诈，并称其有“理由”根据《联邦储备法》将其免职。库克否认不当行为，且未受到法律指控。

该裁决对特朗普是一次挫折，他曾试图立即罢免库克但未成功。法院的决定确保美联储至少在年底前能够照常运作，包括潜在的降息。库克将参加即将举行的联邦公开市场委员会(FOMC)会议。

此案被视为关于美联储独立于政治干预的潜在里程碑式判决。司法部此前称阻止特朗普罢免库克的禁令为“不当的司法干预”。库克的律师对法院的裁决表示欢迎，而白宫则表示对口头辩论后的最终胜利充满信心。美联储表示将遵守法院的裁决。FOMC预计今年将批准两次降息，库克将参与该决定。

---

## 22. Show HN: Resterm – 一款基于终端的 REST/GraphQL 和 gRPC 客户端

**原文标题**: Show HN: Resterm – A terminal-based REST/GraphQL and gRPC client

**原文链接**: [https://github.com/unkn0wn-root/resterm](https://github.com/unkn0wn-root/resterm)

Resterm：一款基于终端的REST、GraphQL和gRPC客户端，旨在直接从命令行高效地进行API交互。它具有工作区浏览器、带有Vim风格导航的编辑器、内联请求执行以及有限的curl命令解析功能。

主要功能包括状态感知响应面板（美化、原始、头部、历史记录）、身份验证和变量助手（基本、令牌、API密钥、自定义头部、时间戳、UUID）、使用JavaScript进行预请求和测试脚本编写，以及用于GraphQL和gRPC请求的专用工具。GraphQL支持包括操作名称和可读预览，而gRPC功能则处理描述符集、反射并显示元数据。内置会话持久性，cookie jar、历史记录存储和环境感知条目在重启后仍然保留。该工具高度可配置，具有超时、TLS、重定向和代理设置选项。

Resterm读取纯文本的`.http`或`.rest`文件，从而允许组织请求定义。它支持诸如`@name`、`@description`、`@auth`、`@graphql`和`@grpc`之类的元数据指令来控制请求行为。可以在请求、文件、环境和操作系统级别定义变量。该客户端支持用于导航和操作的快捷键，以及用于配置的各种CLI标志。

虽然仍处于早期阶段，但Resterm旨在提供全面而高效的基于终端的API交互体验。

---

## 23. PWA的最小文件和配置

**原文标题**: Minimal files and config for a PWA

**原文链接**: [https://github.com/chr15m/minimal-pwa](https://github.com/chr15m/minimal-pwa)

本文概述了为 Android 和 iOS 创建可安装的渐进式 Web 应用 (PWA) 所需的最低限度。它强调了一种简化的方法，使用最少的 `manifest.json` 文件和一个基本的 Service Worker，专门用于触发 Chrome 中的安装提示。

关键在于注重简洁。本文将这种多文件设置与更紧凑的替代方案进行了对比：单文件 PWA 实现。这种单文件方法使用 JavaScript 动态生成 `manifest.json`，并消除了对单独 Service Worker 的需求，展示了一条更精简的 PWA 可安装路径。

本质上，本文重点介绍了创建最小 PWA 的两种方法：一种依赖于专用的 `manifest.json` 和 Service Worker 文件，另一种更简化的版本将所有内容封装在单个 HTML 文件中，利用 JavaScript 进行动态 `manifest.json` 创建。两者都旨在实现相同的目标：启用 PWA 安装。

---

## 24. FlowSynx – 在.NET上编排声明式、插件驱动的DAG工作流

**原文标题**: FlowSynx – Orchestrate Declarative, Plugin-Driven DAG Workflows on .NET

**原文链接**: [https://flowsynx.io/](https://flowsynx.io/)

FlowSynx 是一个基于 .NET 构建的开源、跨平台工作流编排系统，旨在实现自动化、可重复性和模块化编排。它允许开发者使用 JSON 或 DSL 定义、执行和管理复杂的工作流，这些工作流以有向无环图 (DAG) 的形式呈现。FlowSynx 采用微内核架构，具有基于插件的扩展性，允许动态加载和替换组件以实现定制功能。

主要特性包括：

*   **基于插件的扩展性：** 每个组件，从任务定义到身份验证，都是一个插件。
*   **跨平台执行：** 在 Windows、Linux 和 macOS 上运行，并支持 Docker 容器化。
*   **工作流定义和执行：** 支持条件逻辑、并行执行、错误处理和自定义执行上下文。
*   **全面的 CLI 和 SDK：** 包括用于管理的 CLI 和用于 .NET 中程序化访问的 SDK（计划支持其他语言的 REST API）。
*   **REST-API 可访问性：** 通过文档完善且版本化的 RESTful API 公开核心功能。
*   **Web-UI 管理控制台：** 提供基于浏览器的界面，用于可视化工作流设计、监控和插件管理。
*   **安全特性：** 提供可插拔的身份验证、安全策略和全面的日志记录/审计。
*   **部署灵活性：** 支持独立和容器化部署。
*   **基于触发器的执行：** 允许通过事件启动工作流。
*   **人工参与审批：** 集成了人工决策点以用于审批流程。
*   **灵活的错误处理：** 可配置的错误处理策略，用于定义在执行期间如何管理故障，包括重试、跳过或中止行为。

FlowSynx 旨在适应各种领域，并提供用于管理、监控工作流以及将工作流集成到现有系统中的工具。

---

## 25. 检测未更新修复系统级卡顿的Mac上的Electron应用

**原文标题**: Detect Electron apps on Mac that hasn't been updated to fix the system wide lag

**原文链接**: [https://gist.github.com/tkafka/e3eb63a5ec448e9be6701bfd1f1b1e58](https://gist.github.com/tkafka/e3eb63a5ec448e9be6701bfd1f1b1e58)

本文探讨了macOS Tahoe系统上由特定Electron应用引起的系统级延迟问题。该问题源于较旧的Electron版本，这些版本会触发性能下降。

作者提供了一个脚本来检测Mac上使用已知会导致延迟的过时Electron版本的Electron应用。 具体而言，受影响的版本低于36.9.2、37.6.0、38.2.0和39.0.0。 该脚本会输出Electron应用及其对应Electron版本的列表，并用叉号("❌")标记出易受攻击的应用。

建议采用一种临时解决方法：在系统启动时运行 `launchctl setenv CHROME_HEADLESS 1`。 这会禁用Electron应用中的窗口阴影，从而防止延迟，但会牺牲视觉美感。

文章包含示例输出，显示了可能受影响的应用及其Electron版本，演示了该脚本的功能。 作者还提供了外部资源的链接，以获取有关该问题的更多信息。 最后，作者宣传了他们的天气应用Weathergraph。

---

## 26. 基于WiFi地图的高分辨率高效图像生成

**原文标题**: High-resolution efficient image generation from WiFi Mapping

**原文链接**: [https://arxiv.org/abs/2506.10605](https://arxiv.org/abs/2506.10605)

基于预训练潜在扩散模型的高分辨率高效WiFi CSI图像生成：LatentCSI介绍了一种利用WiFi信道状态信息(CSI)数据生成物理环境图像的新方法。作者Eshan Ramesh和Takayuki Nishio利用预训练的潜在扩散模型(LDM)进行高效高质量的图像合成。

LatentCSI的工作原理是使用轻量级神经网络将CSI幅度直接映射到预训练LDM的潜在空间中。这避免了与GAN或显式图像编码等传统方法相关的计算负担和复杂性。 然后，LDM的去噪扩散过程细化潜在表示，并在可选的文本提示的指导下，使用LDM的解码器将其解码为高分辨率图像。

该方法的有效性已在自定义收集的宽带CSI数据集和公开可用的MM-Fi数据集的子集上得到了验证。结果表明，在计算效率和感知图像质量方面，LatentCSI优于直接在真实图像上训练的可比基线模型。此外，LatentCSI还具有文本引导可控性的独特优势，允许用户通过文本提示影响生成的图像。本质上，LatentCSI提供了一种有效且可控的方法，利用预训练的潜在扩散模型从WiFi CSI数据生成逼真的图像。

---

## 27. Show HN: Privacyforge.ai – 可用的AI隐私合规文档

**原文标题**: Show HN: Privacyforge.ai – AI Privacy Compliance Documents That Work

**原文链接**: [https://www.privacyforge.ai/](https://www.privacyforge.ai/)

PrivacyForge.ai 是一个人工智能驱动的平台，旨在简化和自动化隐私合规文档。它帮助企业生成符合 GDPR、CCPA、CPRA、COPPA、CalOPPA 和 PIPEDA 等主要法规的定制隐私政策。该平台利用智能问卷来适应特定的业务实践和数据处理程序，在几分钟内创建量身定制的文档。

主要功能包括多法规合规、人工智能驱动的定制、法律术语的通俗语言翻译、快速实施、经济高效的定价以及定期更新以保持与不断变化的法规同步。用户回答有关其业务的简单问题，选择一个计划（基本版、专业版或企业版），人工智能会生成所需的文件。然后可以下载和实施这些文档，并提供持续的法规更新支持。

客户评价强调了在法律费用和时间方面的显著节省，以及该平台的易用性和准确性。PrivacyForge.ai 提供透明的定价，计划起价为 79 美元，满足初创公司、成长型企业和具有复杂合规需求的企业。所有计划都包含退款保证。该平台旨在提供企业级的隐私合规性，而无需传统法律咨询的高昂价格。

---

## 28. 人们希望平台而非政府负责内容审核。

**原文标题**: People want platforms, not governments, to be responsible for moderating content

**原文链接**: [https://reutersinstitute.politics.ox.ac.uk/news/most-people-want-platforms-not-governments-be-responsible-moderating-content](https://reutersinstitute.politics.ox.ac.uk/news/most-people-want-platforms-not-governments-be-responsible-moderating-content)

文章题为“人们希望平台而非政府负责内容审核”，可能论述公众越来越倾向于让社交媒体平台和在线公司，而非政府机构，主要负责审核网上发布的内容。随附的图片是唐纳德·特朗普在2025年的一次私人晚宴上与马克·扎克伯格交谈，这强烈暗示文章可能还会涉及政治人物与强大的科技平台之间不断演变的关系。

核心论点可能围绕政府试图控制在线言论时，人们所认为的不合法性或潜在的滥用权力。对审查、政治偏见和权力过度扩张的担忧很可能被认为是个人对政府参与内容审核持谨慎态度的原因。

文章可能断言，人们认为平台更有能力制定和执行内容政策，因为它们拥有技术专长，了解其用户群，并直接控制其服务。它可能探讨支持和反对这种偏好的论点，可能提到潜在的缺点，例如私营公司缺乏民主问责制以及利润动机对内容决策的影响。它还可能讨论平台在平衡言论自由与保护用户免受有害内容、虚假信息和仇恨言论侵害方面面临的挑战。图片显示特朗普和扎克伯格的事实表明，文章可能还会讨论内容审核对政治讨论和选举的潜在影响。

---

## 29. Gmail网页版不再提供“从其他帐户查收邮件”功能

**原文标题**: No more "check mail from other accounts" in Gmail web

**原文链接**: [https://support.google.com/mail/answer/16604719?hl=en](https://support.google.com/mail/answer/16604719?hl=en)

自2026年1月起，Gmail将停止对网页版Gmail中用于访问第三方电子邮件帐户的Gmailify和POP连接的支持。

**Gmailify** 将不再为链接的第三方电子邮件帐户提供Gmail的特殊功能（垃圾邮件防护、收件箱整理等）。

**POP连接** 将被移除，Gmail网页版中的“检查其他帐户邮件”选项将不可用。这意味着您将无法再使用POP将其他帐户的电子邮件下载到Gmail中。

**影响：** 依赖这些功能的用户需要寻找其他方式来访问他们的第三方电子邮件帐户。

**推荐操作：**

*   **Gmail应用：** 用户可以通过使用IMAP将第三方帐户（如Yahoo!和Outlook）添加到Gmail移动应用中，继续阅读和发送电子邮件。
*   **IMAP设置：** 如果用户希望继续在Gmail中接收邮件，建议为其第三方电子邮件帐户启用IMAP访问。有关启用IMAP的说明应可在电子邮件提供商的文档中找到。

**重要提示：**

*   现有导入的电子邮件不会丢失。
*   工作或学校帐户可以通过管理员获得数据迁移服务。

此更改旨在为在Gmail中访问邮件提供更安全和最新的选项。

---

## 30. TigerBeetle是一个非常有趣的数据库。

**原文标题**: TigerBeetle is a most interesting database

**原文链接**: [https://www.amplifypartners.com/blog-posts/why-tigerbeetle-is-the-most-interesting-database-in-the-world](https://www.amplifypartners.com/blog-posts/why-tigerbeetle-is-the-most-interesting-database-in-the-world)

本文认为 TigerBeetle 是一款高度创新的数据库，其设计和方法与 SQL 等传统数据库相比独树一帜。它强调 TigerBeetle 专注于金融交易，使用借贷作为一流的原语以实现最佳性能。与依赖 SQL 查询不同，TigerBeetle 可以在单个查询中处理数千个借/贷操作。

本文强调了 TigerBeetle 的现代架构，该架构默认构建为分布式，具有共识、时钟容错和存储容错等功能，从而确保数据完整性和高可用性。它利用 Viewstamped Replication 实现共识。值得注意的是，它使用 Zig 语言编写，允许静态内存分配并提供对 C 生态系统的访问。

一个关键的区别在于 TigerBeetle 通过其 VOPR 集群使用确定性模拟测试 (DST)，通过模拟各种系统场景和边缘情况来实现严格的测试和调试。这使他们能够在相对较短的开发时间内获得 Jepsen 认证，这在数据库领域很少见。本文指出，他们通过不可变的校验和数据、自定义页面缓存和其他方法处理存储故障的方式使他们在分布式数据库中独树一帜。本质上，TigerBeetle 代表了为现代世界的事务需求而设计的新一代数据库。

---

## 31. Databricks 的智能 Kubernetes 负载均衡

**原文标题**: Intelligent Kubernetes Load Balancing at Databricks

**原文链接**: [https://www.databricks.com/blog/intelligent-kubernetes-load-balancing-databricks](https://www.databricks.com/blog/intelligent-kubernetes-load-balancing-databricks)

Databricks 通过构建自定义的客户端负载均衡系统，解决了 Kubernetes 默认负载均衡 (kube-proxy) 在处理高吞吐量 gRPC 服务时的局限性。Kube-proxy 的四层负载均衡会导致流量倾斜、高尾延迟以及因持久 HTTP/2 连接的按连接路由而造成的资源利用率低下。

Databricks 的解决方案使用控制平面来监控 Kubernetes API 中的服务和端点变更，从而为客户端提供实时数据。该方案集成到其通用的基于 Scala 的服务框架中，客户端绕过 DNS 和 kube-proxy，从而保持对服务拓扑的实时视图。这实现了诸如 Power of Two Choices (P2C) 和区域亲和性路由等高级的按请求负载均衡策略。该控制平面还通过 xDS 与 Envoy 集成，用于外部流量管理，从而确保跨平台的一致路由。

该实施实现了均匀的请求分发、稳定的延迟曲线以及 pod 数量减少 20%。面临的挑战包括服务器冷启动（通过慢启动爬升解决）和基于指标路由的不可靠性。

曾考虑过诸如无头服务（有限的端点权重、DNS 缓存）和服务网格（如 Istio）（运维复杂性、性能开销、有限的客户端灵活性）等替代方案，但认为不合适。Databricks 的客户端方法提供了细粒度的控制、更高的效率和定制的负载均衡策略，同时保持了内部和外部流量的一致性。

---

## 32. 黑客袭击哈罗德百货，英国再遭网络攻击

**原文标题**: Hackers strike Harrods in latest UK cyberattack

**原文链接**: [https://observer.co.uk/news/national/article/hackers-strike-harrods-in-latest-uk-cyberattack](https://observer.co.uk/news/national/article/hackers-strike-harrods-in-latest-uk-cyberattack)

哈罗德百货警告顾客，可能发生数据泄露，黑客可能已从用于在线购物的第三方系统窃取姓名和联系方式。这是针对英国企业的一系列网络攻击中的最新事件。7月，有人因与哈罗德百货、合作社和玛莎百货的袭击有关而被捕。最近的其他袭击包括对幼儿园连锁店Kido的袭击，导致儿童数据被盗和企图勒索，以及对柯林斯宇航的勒索软件攻击，导致机场中断。捷豹路虎的生产因8月份的网络攻击仍然停滞。

这些日益增加的网络攻击引发了对英国网络安全能力的担忧，并可能破坏数字身份证计划，该计划正面临公众的反对。专家指出，追踪网络攻击的真实数量非常困难，这些攻击由包括犯罪团伙、国家支持的实体和黑客行动主义者在内的各种行为者实施。一项政府调查显示，过去一年中，一半的企业经历过安全漏洞。一项新的网络安全法案旨在强制报告事件，但其进展缓慢令安全专家感到沮丧，他们强调网络攻击对经济增长的负面影响。

---

## 33. DuckDuckGo 向 Perl 和 Raku 基金会捐赠 25,000 美元 (v2025)

**原文标题**: DuckDuckGo Donates $25,000 to The Perl and Raku Foundation v2025

**原文链接**: [https://www.perl.com/article/duckduckgo-donates-25-000-to-the-perl-and-raku-foundation-v2025/](https://www.perl.com/article/duckduckgo-donates-25-000-to-the-perl-and-raku-foundation-v2025/)

Perl 和 Raku 基金会 (TPRF) 连续第二年收到 DuckDuckGo 的 25,000 美元捐款。DuckDuckGo 认识到 Perl 在为其核心系统、插件框架和即时解答提供支持方面的重要性，他们的捐款用于支持核心 Perl 维护基金。该基金对于维持和发展 Perl 语言至关重要。

去年的捐款对于资助核心 Perl 维护基金起到了重要作用，今年的捐款将继续这项工作。文章重点介绍了由维护基金资助的开发者 Paul "LeoNerd" Evans，以及他对核心 Perl 的重大贡献，包括新的语言级实用程序、“类”系统、词法方法支持、实验性功能的稳定化以及新的关键字。

TPRF 强调与赞助商建立多年合作关系的重要性，这有助于更好地进行长期规划，并优先开展对维持 Perl 语言及其社区至关重要的工作。他们鼓励各组织成为赞助商。

---

## 34. 叶潜虫被认定为地球历史上最古老的虫害

**原文标题**: Leaf miners identified as oldest insect plague in the history of Earth

**原文链接**: [https://phys.org/news/2025-09-leaf-miners-oldest-insect-plague.html](https://phys.org/news/2025-09-leaf-miners-oldest-insect-plague.html)

本文探讨了已知最古老昆虫潜叶的发现，其年代可追溯至2.95亿年前的二叠纪。包括柏林自然博物馆在内的多个机构的研究人员，分析了来自德国图林根州克洛克地区的植物化石，发现了*Asteronomus maeandriformis*幼虫在*Autunia conferta*叶片上取食隧道的广泛证据。这一发现将潜叶的最早证据提前了4000万年。

保存下来的化石不仅揭示了取食隧道，还揭示了相关的卵沉积物，其中一些甚至含有昆虫卵遗骸。侵染频率异常高，该地区超过80%的*Autunia*植物都显示出潜叶现象，使其成为有记录以来最古老的昆虫侵染案例。

本文强调了自然历史收藏在为科学研究提供宝贵资源方面的重要性。潜叶行为是一种专门的适应，可以提供保护和现成的食物来源，其在昆虫进化早期就已存在，这为全变态昆虫（经历完全变态的昆虫）的演化提供了线索。克洛克地区发生强烈侵染的原因尚不清楚，但它与全球气候变化导致生态系统更加干燥的时期相吻合。这些发现发表在《科学报告》杂志上。

---

## 35. 计算史前史，第二部分

**原文标题**: The Prehistory of Computing, Part II

**原文链接**: [https://www.oranlooney.com/post/history-of-computing-2/](https://www.oranlooney.com/post/history-of-computing-2/)

奥兰·鲁尼的《计算的史前时代，第二部分》追溯了计算设备从17世纪至今的演变。文章重点介绍了帕斯卡的帕斯卡加法器，这是第一个成功的带有进位机制的机械加法机，是一项关键的突破。随后，文章深入探讨了莱布尼茨的阶梯计算器，这是第一个基于莱布尼茨轮的四则运算计算器，强调了它对后续计算器设计的影响，尽管它最初存在实际局限性。科尔马算术器的成功归功于精密加工的进步。

除了机械计算，文章还探讨了莱布尼茨的理论贡献，特别是他关于通用形式语言（“通用文字”）的设想，这影响了布尔代数和形式逻辑的发展。

文章随后跳跃到讨论切比雪夫逼近理论和等波纹定理，该定理证明了函数可以通过具有一致误差界的 polinomios 逼近。这引出了对Remez算法和Padé逼近的讨论，突出了多项式逼近在现代数学库中的普遍性。

最后，文章详细介绍了巴贝奇的差分机，这是一种使用有限差分法进行高效多项式求值的机器，该方法将多项式计算转换为加法。文章最后简要概述了电动机械计算机、图灵和香农等关键理论家的贡献，以及电子计算机由于其速度、成本效益和可靠性而最终占据主导地位。文章强调了现代计算中，诸如查找表和多项式逼近等前数字化技术的持久相关性。

---

## 36. 新泽西州主题公园将电动恐龙放在脸书市场上售卖

**原文标题**: NJ theme park puts animatronic dinosaurs on Facebook Marketplace

**原文链接**: [https://gizmodo.com/new-jersey-theme-park-puts-animatronic-dinosaurs-on-facebook-marketplace-as-it-shuts-down-2000664489](https://gizmodo.com/new-jersey-theme-park-puts-animatronic-dinosaurs-on-facebook-marketplace-as-it-shuts-down-2000664489)

恐龙野外站：新泽西州主题公园将于11月9日关闭，并在Facebook Marketplace上出售其仿真恐龙。该公园此前从锡考克斯迁至利奥尼亚，现在提供各种恐龙，价格从500美元到近3000美元不等，包括一具52英尺长的棘龙、一具带有蛋的鸭嘴龙和一具副栉龙。买家负责拆卸和运输费用。

执行制片人Guy Gsell希望这些恐龙能找到好归宿。在关闭之前，公园将举办一系列最后的活动，包括“侏罗纪宠物动物园”（9月27-28日）、“黑暗中的恐龙”（10月3-25日），一个以恐怖为主题的活动，以及“狗狗与恐龙”（10月13日），允许游客携带他们的犬类伴侣。该公园在真人秀节目《The Fixer》中的亮相最终未能阻止其关闭。

---

## 37. 差异算法

**原文标题**: Diff Algorithms

**原文链接**: [https://flo.znkr.io/diff/](https://flo.znkr.io/diff/)

本文探讨了作者因对现有库不满意而创建新的Go差异库 `znkr.io/diff` 的动机。主要需求包括支持任意序列（不仅仅是文本），统一差异格式以外的可定制输出格式，人类可读且最小化的差异，简单的API以及在所有场景下的出色性能。

作者评估了几种现有的Go差异库，重点介绍了它们在输入类型、输出格式、API可用性、性能以及差异可读性和最小化方面的局限性。本文深入研究了差异算法的复杂性，特别是Myers算法，该算法具有二次最坏情况时间复杂度和潜在的二次内存使用量。像耐心差异（在`go-internal`中使用）这样的启发式算法提供了更好的性能，但可能存在局限性。

一个主要重点是差异的可读性，强调最小差异并不总是最容易理解的。诸如Michael Haggerty的启发式后处理方法可以显着提高可读性。`znkr.io/diff`库通过提供三种操作模式来应对这些挑战：默认、快速和最优，从而权衡性能和最小化。

API设计优先考虑可用性和可扩展性，使用差异的结构化表示（Edits 和 Hunks）和用于自定义的功能选项。该库通过使用比较函数来支持任意切片，从而允许对不可比较的类型进行差异比较。

---

## 38. 如何避免 Rust 借用检查器的对抗

**原文标题**: How to Avoid Fighting Rust Borrow Checker

**原文链接**: [https://qouteall.fun/qouteall-blog/2025/How%20to%20Avoid%20Fighting%20Rust%20Borrow%20Checker](https://qouteall.fun/qouteall-blog/2025/How%20to%20Avoid%20Fighting%20Rust%20Borrow%20Checker)

本文旨在指导读者理解和应对 Rust 的借用检查器，重点关注其带来的挑战。文章强调了 Rust 的三个核心原则：树形所有权、独占可变借用和传染性借用。文章区分了借用检查器友好的（树形引用）和借用检查器不友好的（共享或循环引用）引用结构。

关键在于理解如何在“不友好”的情况下避免常见的借用检查器问题。推荐的解决方案包括：

*   **面向数据设计（DOD）：** 避免 getter/setter，直接操作数据，防止传染性借用。
*   **使用 ID/句柄代替借用：** 使用 ID/句柄间接引用数据，解耦直接借用。
*   **延迟修改：** 将修改视为添加到队列中的命令，稍后执行。
*   **避免修改：** 使用不可变数据结构，拥抱“通过重新创建来修改”。
*   **循环引用：** 使用 ID/句柄处理图结构。对于回调，考虑事件总线或带有 `Weak` 的 `Arc<QCell<T>>` 来打破循环。

文章详细阐述了传染性借用问题，说明了借用一个字段如何间接借用整个对象，从而导致冲突。文章对比了内联代码（分割借用）和函数调用（粗粒度借用）来解释这种行为。

文章还讨论了循环引用，区分了数学中存在问题的自引用概念和编程中有效的用例。文章强调了循环引用的内存管理挑战，并建议避免“仅仅为了方便”的循环引用。文章讨论了处理回调循环引用的不同策略，包括带有内部可变性的引用计数（`Rc<RefCell<T>>`、`Arc<RwLock<T>>` 和 `Rc<QCell<T>>`）。

---

## 39. Sora 2

**原文标题**: Sora 2

**原文链接**: [https://openai.com/index/sora-2/](https://openai.com/index/sora-2/)

无法访问文章链接。

---

## 40. 延缓执行：使用 GCC 魔法在 C 中进行资源清理

**原文标题**: Defer: Resource cleanup in C with GCCs magic

**原文链接**: [https://oshub.org/projects/retros-32/posts/defer-resource-cleanup-in-c-with-gccs-magic](https://oshub.org/projects/retros-32/posts/defer-resource-cleanup-in-c-with-gccs-magic)

本文探讨了如何使用 GCC 的非标准扩展，特别是 `cleanup` 属性和嵌套函数，在 C 语言中实现类似于 Go 语言的 `defer` 机制。`cleanup` 属性允许将一个函数与一个变量关联起来，并在变量超出作用域时触发该函数的调用。嵌套函数，作为 GCC 的一项扩展，允许在一个函数内部声明另一个函数，从而能够访问外部作用域的变量。

作者首先演示了用于资源管理的基本 `cleanup` 属性，但发现其不安全，因为存在在 NULL 指针上调用清理函数等潜在问题。Jens Gustedt 的博客文章启发了一种结合 `cleanup` 和嵌套函数的 `defer` 宏。该宏确保 `defer` 块中的代码在函数返回之前执行，从而自动处理资源清理，即使是提前返回。

最初的实现涉及大量的开销，包括单独的函数调用和堆栈帧创建。通过使用 `always_inline`，作者强制编译器直接插入 defer 代码，从而减少了开销，最终得到更简洁的汇编代码并避免了单独的函数调用。

本文强调了这种方法的优点：更清晰的代码、更简单的资源管理以及避免在多个返回路径中重复清理逻辑。虽然由于依赖 GCC 扩展而不可移植，但 `defer` 宏展示了编译器的功能，并为改进 C 语言中的资源管理提供了一个有趣的视角。与传统的基于 goto 的方法进行比较，突出了 `defer` 宏所提供的改进的可读性和可维护性。

---

## 41. Blockdiff：我们构建了自己的VM磁盘快照文件格式

**原文标题**: Blockdiff: We built our own file format for VM disk snapshots

**原文链接**: [https://cognition.ai/blog/blockdiff](https://cognition.ai/blog/blockdiff)

Cognition 开发了 Blockdiff，一个开源工具，用于创建快速的块级差异和虚拟机磁盘快照，从而显著减少虚拟机启动和快照时间。现有解决方案，如 EC2 快照（30 多分钟）和 OverlayFS/ZFS 存在局限性。Blockdiff 通过创建增量快照来解决这些问题，这些快照仅存储基础镜像和虚拟机磁盘之间的差异。

关键设计目标包括紧凑的快照大小、瞬时快照创建、零虚拟机开销和简单性。Blockdiff 通过利用 Linux 内核在 XFS 中的写时复制 (CoW) 特性，并主要通过使用 FIEMAP 系统调用获取的文件范围映射来操作文件系统元数据来实现这一点。它避免了缓慢的二进制差异计算以及虚拟机内 ZFS 等解决方案的复杂性。

Blockdiff 文件格式 (.bdiff) 包含一个包含文件大小和不同块范围数量的标头，后跟实际的不同块。创建快照涉及最少的磁盘 I/O，主要是重连文件元数据，从而大大缩短了快照时间（例如，将 20GB 快照创建时间从约 6.5 秒减少到约 200 毫秒）。

本文还重点介绍了 Blockdiff 在压缩稀疏文件以实现高效存储方面的应用。Cognition 正在研究有关虚拟机管理程序的其他挑战，例如虚拟机运行时磁盘回滚和智能缓存，并邀请其他人参与解决这些问题。

---

## 42. 和纸：可保存千年的日本纸 [视频]

**原文标题**: Washi: The Japanese paper crafted to last 1000 years [video]

**原文链接**: [https://www.bbc.com/reel/video/p0m4mg2j/washi-the-japanese-paper-crafted-to-last-1-000-years](https://www.bbc.com/reel/video/p0m4mg2j/washi-the-japanese-paper-crafted-to-last-1-000-years)

本视频探索日本和纸的艺术，这种手工纸以其美丽、强度和独特的天然纹理而闻名。和纸手工制作已有 1500 多年历史，因其寿命长而备受赞誉；正如用这种纸制成的古代文献所证明的那样，如果保存得当，某些品种可以保存 1000 多年。视频中，BBC 主持人保罗·卡特访问越前，了解和纸的制作过程。

除了这个主要焦点之外，内容还包括一系列不相关的消息片段，涵盖广泛的主题，包括：马修·麦康纳的职业决定、古埃及字母的起源、平静的自然视频、罗马在保护其古代历史的同时进行的现代化努力、联合国总部的起源、野火预测技术、对美联储降息的预期、康沃尔郡的“美人鱼”教育人们关于海洋清洁的知识、二维码的历史、奥利维亚·科尔曼的晚宴绝活、希腊伊卡里亚岛的长寿秘诀、BBC Maestro 课程、阿尔伯塔龙的狩猎策略、天基太阳能、华尔街对劳动力市场数据和通货膨胀的关注，以及超加工食品对健康的影响。

---

## 43. 基本方言、集成开发环境和教程

**原文标题**: Basic Dialects, IDEs, and Tutorials

**原文链接**: [https://github.com/JohnBlood/awesome-basic](https://github.com/JohnBlood/awesome-basic)

本文档提供了一个精选的BASIC编程语言资源列表，涵盖方言、IDE、教程和杂项信息。

**方言：** 提供了一个庞大而多样的BASIC方言列表，适用于不同的平台（Windows、Linux、macOS、Web、移动）、用途（游戏开发、通用编程）和经验水平（初级到高级）。这些方言包括AppGameKit、B4X、FreeBASIC、QB64、PureBasic等。有些是跨平台的，而另一些则特定于某些操作系统或硬件。

**IDE、编辑器、插件和工具：** 该文档列出了各种旨在促进BASIC编程的集成开发环境（IDE）、编辑器和插件。这些工具提供代码完成、调试、GUI设计以及与其他开发环境集成等功能。示例包括DavsIDE、VisualFBEditor和vscode-vba。

**杂项：** 本节提供了Commodore BASIC程序、GW-BASIC代码集合以及有关BASIC解释器特定方面信息的链接。它还包括一个使用FreeBASIC模拟Chip-8系统的项目。

**教程：** 其中包含针对不同BASIC方言和编程方面的教程汇编，为初学者和寻求加深知识的人员提供资源。这些教程涵盖FreeBASIC、Gambas、BlitzMax、yab、QB64和QBasic。

---

## 44. Bild AI (YC W25) 正在招聘

**原文标题**: Bild AI (YC W25) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/bild-ai/jobs/m2ilR5L-founding-engineer-applied-ai](https://www.ycombinator.com/companies/bild-ai/jobs/m2ilR5L-founding-engineer-applied-ai)

Bild AI 是一家 Y Combinator W25 孵化的初创公司，正在寻找一位创始工程师（应用人工智能），以构建能够理解施工蓝图的人工智能。 该职位涉及开发智能层，应用计算机视觉、LLM 模型和人工智能系统，交付原型，并根据用户反馈进行改进。

理想的候选人具备应用 CV/ML 经验，拥有构建和部署生产环境中人工智能的经验，展现出成长型思维，能够有效沟通，并且不惧怕早期创业公司涉及的“苦活”。 具有初创公司/创始人经验、建筑背景以及具有影响力驱动力者优先考虑。

该职位为全职，需在旧金山办公室工作（或需要搬迁），薪资为 10 万美元至 18 万美元，股权为 0.50% 至 2.00%。 Bild AI 正在使用模型花园方法解决蓝图理解方面的具有挑战性的技术问题，并已从顶级风险投资公司筹集了资金。

欢迎有兴趣的候选人申请，包括说明为什么他们适合该职位以及他们最喜欢的水果。 创始人是 Roop Pal 和 Puneet Sukhija。

---

## 45. 波音已开始研发737 MAX的替代机型。

**原文标题**: Boeing has started working on a 737 MAX replacement

**原文链接**: [https://www.wsj.com/business/airlines/boeing-has-started-working-on-a-737-max-replacement-40a110df](https://www.wsj.com/business/airlines/boeing-has-started-working-on-a-737-max-replacement-40a110df)

**概要：**

据《华尔街日报》报道，波音公司已开始初步研发其737 MAX飞机的替代机型。这款新飞机尚处于早期研发阶段，旨在与空客的A320neo系列竞争，后者近年来的销量已远超737 MAX。

虽然波音尚未正式宣布启动该项目，但该文章表明工程师们正在探索各种设计概念，包括新的发动机技术和先进的制造技术。主要考虑因素包括燃油效率、运营成本和乘客舒适度。预计研发过程漫长，行业分析师预测，最早也要到2030年代中期，这款新飞机才能面世。

追求737 MAX的后继机型是受多种因素驱动的。这些因素包括737的老化设计、来自空客的持续竞争以及需要解决737 MAX安全问题造成的声誉损害。该文章强调，波音公司在开发具有竞争力的飞机方面面临重大挑战，包括获得资金、应对监管障碍以及整合新技术。新项目的成功对于波音公司重获市场份额并巩固其在全球航空业的地位至关重要。该公司还旨在从过去的错误中吸取教训，并确保新飞机拥有最新的安全标准。

---

## 46. 泄露的苹果M5 9核Geekbench跑分

**原文标题**: Leaked Apple M5 9 core Geekbench scores

**原文链接**: [https://browser.geekbench.com/v6/cpu/14173685](https://browser.geekbench.com/v6/cpu/14173685)

本文件展示了据称是苹果M5芯片在iPad (型号为"iPad17,3")上运行的Geekbench泄露跑分。基准测试结果日期为2025年9月30日，显示M5拥有一个9核CPU，基频为4.42 GHz，分为两个集群（3核和6核）。该iPad还拥有11.2 GB的RAM。

单核跑分据称是4133，多核跑分是15437。该文件随后细分了各种测试的性能，包括文件压缩、导航、HTML5浏览、PDF渲染、照片库处理、Clang编译、文本处理、资产压缩，以及几个与图像相关的任务，如对象检测、背景模糊和光线追踪。这些测试详细展示了该芯片在不同工作负载下的潜在能力。

令人印象深刻的单核跑分表明苹果持续关注单线程性能，而多核跑分则展示了多线程应用中的高生产力和效率。

---

## 47. 电脑不情愿

**原文标题**: Computers Don't Want

**原文链接**: [https://blog.computationalcomplexity.org/2025/10/computers-dont-want.html](https://blog.computationalcomplexity.org/2025/10/computers-dont-want.html)

兰斯·福特诺的博文《计算机不想要》批判了《如果有人建造它，所有人都会死》一书中提出的论点，该书警告了人工超智能（ASI）存在的威胁。福特诺不同意作者的前提，即应该将ASI视为具有能动性和欲望。

他认为，将AI视为图灵机，简单地遵循指令而没有内在欲望，更为准确。虽然他承认简单指令会产生巨大的复杂性，并且理解算法存在困难（赖斯定理，P与NP问题），但福特诺认为，这种复杂性不应被误认为是能动性或欲望。他认为，AI中的目标导向行为源于其训练数据，而不是源于独立的能动性。

福特诺更担心人类对AI的滥用或错位的信任，而不是AI本身产生敌对意图。他认为“所有人都会死”的框架是宿命论，并且基于对计算系统存在缺陷的隐喻式理解。他提倡关注减轻与人类与该技术互动相关的风险，而不是将AI视为一个代理。

评论区揭示了不同的观点，有些人认为这场讨论是旧闻，另一些人质疑福特诺关于人脑的运作方式与计算方式根本不同的断言。一些评论表明，意向姿态更适合用于建模AI的行为，例如谄媚。

---

## 48. 多臂老虎机简介 (2019)

**原文标题**: Introduction to Multi-Armed Bandits (2019)

**原文链接**: [https://arxiv.org/abs/1904.07272](https://arxiv.org/abs/1904.07272)

这篇arXiv文章（arXiv:1904.07272v8），题为“多臂老虎机导论”，作者为Aleksandrs Slivkins。它是一部类似教科书的多臂老虎机（MAB）框架入门介绍，该框架用于在不确定性下随时间进行决策的算法。该论文已多次提交和修订，最新版本（v8）于2024年4月3日提交。它于2019年11月在《机器学习基础与趋势》杂志上发表。

本书分为几个部分，涵盖：
*   独立同分布奖励（基本模型，不可能结果，贝叶斯先验，利普希茨奖励）
*   对抗性奖励（全反馈，对抗性老虎机，线性奖励，组合动作）
*   情境老虎机（由情境解释的奖励）
*   与经济学的联系（重复博弈中的学习，具有供给/预算约束的老虎机，具有激励的探索）。

附录提供了关于集中度和KL散度的背景知识。此外，该论文强调，“具有相似性信息的老虎机”、“带有背包的老虎机”和“老虎机与代理”等章节可以独立阅读，作为独立的综述。

该论文被归类为机器学习（cs.LG）、人工智能（cs.AI）、数据结构与算法（cs.DS）和机器学习（stat.ML）。它旨在成为MAB的可教授的技术入门，包括练习。最新版本包括对演示文稿和准确性的编辑、更新的文献综述以及基于读者反馈的新练习。

---

## 49. 亨特·S·汤普森去世二十年后将被重新审视

**原文标题**: Hunter S Thompson's death to be reviewed more than 20 years later

**原文链接**: [https://www.theguardian.com/books/2025/oct/01/hunter-s-thompsons-death-reviewed](https://www.theguardian.com/books/2025/oct/01/hunter-s-thompsons-death-reviewed)

在亨特·S·汤普森去世并被判定为自杀20多年后，应其遗孀安妮塔·汤普森的要求，科罗拉多州调查局将对其案件进行复审。汤普森是一位以“冈佐”新闻著称的记者和作家，于2005年在科罗拉多州伍迪克里克的家中去世，享年67岁。他被儿子发现时，他的妻子正在与他通电话。

皮特金县警长办公室将引入CBI对该案件进行“重新审视”，旨在为汤普森的家人和公众提供明确和透明的审查。警长迈克尔·布格里奥内承认汤普森对社区产生了重大影响。

在他去世时，《滚石》杂志发表了他的朋友道格拉斯·布林克利声称是汤普森的遗书。该遗书题为“游戏结束”，提到了他的年龄并表达了对生活缺乏乐趣。复审的时间表尚未明确，但当局旨在为最初的调查带来独立的视角。

汤普森以其《恐惧拉斯维加斯》和《地狱天使》等著作而闻名，这些著作有助于定义“冈佐”新闻风格。

---

## 50. Radicle：基于Git的端到端协作

**原文标题**: Radicle: Peer-to-Peer Collaboration with Git

**原文链接**: [https://lwn.net/Articles/966869/](https://lwn.net/Articles/966869/)

LWN.net文章介绍了Radicle，一个基于Git的P2P协作平台，为GitHub和GitLab等中心化代码托管平台提供了一种去中心化的替代方案。Radicle允许用户运行自己的节点，存储仓库副本并与其他节点同步更改，充当本地Git服务器。它支持存储在Git仓库本身中的议题和拉取请求（称为“补丁”）。

Radicle背后的动机源于软件开发去中心化的愿望，避免中心化平台固有的单点故障和控制。Radicle提供诸如用于身份验证的自签名仓库以及用于创建和管理议题的离线功能等特性。它使用gossip协议进行节点发现，并使用Git v2智能传输协议进行内容交换。一种独特的“协作对象”（COB）机制允许对议题和补丁的数据进行无冲突合并。

尽管Radicle充满希望，但它也面临着挑战，包括用户需要采用Radicle生态系统才能与仓库交互，简陋的代码审查和持续集成支持，以及对更强大的身份系统的需求。文章最后承认Radicle是一种有前途的方法，并鼓励对开发者工具有兴趣的Rust开发者做出贡献。文章中包含的评论线程提出了关于数据不变性、git安全性、数据大小以及审核挑战的担忧。

---

## 51. 博通未披露VMware漏洞的零日漏洞利用情况

**原文标题**: Broadcom Fails to Disclose Zero-Day Exploitation of VMware Vulnerability

**原文链接**: [https://www.securityweek.com/broadcom-fails-to-disclose-zero-day-exploitation-of-vmware-vulnerability/](https://www.securityweek.com/broadcom-fails-to-disclose-zero-day-exploitation-of-vmware-vulnerability/)

SecurityWeek报道：博通未披露VMware高危漏洞(CVE-2025-41244)遭在野利用情况

---

## 52. Sora 2 制作出逼真的虚假犯罪视频

**原文标题**: Sora 2 makes convincing fake crime footage

**原文链接**: [https://bsky.app/profile/drewharwell.com/post/3m25dwdtac22h](https://bsky.app/profile/drewharwell.com/post/3m25dwdtac22h)

德鲁·哈维尔在Bluesky上报道称，OpenAI的文本转视频AI模型Sora，在一分钟内生成了一段视频，展示了“执法人员用随身摄像头拍摄的在百货商店逮捕一名黑皮肤男子的片段”。这突显了Sora创造逼真但可能存在偏见或误导性内容的能力。该报道引发了人们对AI生成视频可能被用于制造虚假犯罪影像，从而加剧有害刻板印象和虚假信息的担忧。它强调了区分真实内容和AI生成内容的挑战，尤其是在警察互动和潜在的种族歧视等敏感情况下。该帖子暗示需要进一步讨论和开发安全措施，以防止滥用此类强大的AI工具。

---

## 53. 几分钟内处理数十亿个三角形

**原文标题**: Billions of Triangles in Minutes

**原文链接**: [https://zeux.io/2025/09/30/billions-of-triangles-in-minutes/](https://zeux.io/2025/09/30/billions-of-triangles-in-minutes/)

本文详细介绍了作者优化 NVIDIA 的 Zorah 演示场景（一个由数十亿个三角形组成的大型 3D 模型）的处理过程的历程，该过程使用开源 meshoptimizer 库为分层聚类细节层次 (LOD) 生成服务。最初的挑战是 glTF 场景的庞大规模（36 GB，约 16.4 亿个三角形），即使在强大的系统上也会导致内存问题和较长的处理时间（7-9 分钟）。

作者最初专注于优化现有的聚类算法，使用 Superluminal 对代码进行分析，以识别瓶颈，例如聚类期间的大型 `memset` 调用。这是由于稀疏索引需要初始化顶点数据，即使未使用也是如此。通过修改代码仅初始化必要的数据，处理时间显着缩短至约 3.5 分钟。

接下来，作者解决了线程不平衡的问题。最初的方法是不均匀的，因为有些网格比其他网格大得多。在处理之前按三角形数量对网格进行排序，允许首先处理更大、计算更密集的网格，从而提高 CPU 利用率并减少整体处理时间。

本文还讨论了内存管理，这对于 RAM 有限的系统尤其重要。作者建议使用原子计数器或信号量来实现内存限制器，以控制同时处理的三角形数量，从而防止内存不足错误。最后，文章提到作者尚未解决将数据保存到磁盘作为最后一步的问题。

---

## 54. 博彩公司的经济学以及他们为何封禁最佳赌徒

**原文标题**: Economics of sportsbooks and why they ban the best bettors

**原文链接**: [https://www.dopaminemarkets.com/p/the-business-of-sports-betting-is](https://www.dopaminemarkets.com/p/the-business-of-sports-betting-is)

本文深入探讨了 DraftKings 和 FanDuel 等体育博彩公司的经济学原理，解释了他们为何禁止成功的投注者（“精明玩家”）。与用户之间相互对赌的体育交易所不同，体育博彩公司通过设置赔率并接受另一方的投注来获利。由于高额税收（在某些州高达 51%）和巨额客户获取成本（每个用户约 300 美元），他们的利润率很低。

体育博彩公司盈利的关键在于“抽水”（vig），这是赔率中内置的利润率。与简单投注相比，组合多个投注的串关投注具有更高的抽水（高达 20%），这使其对体育博彩公司的收入至关重要。因此，体育博彩公司积极鼓励用户，尤其是新用户，通过奖金、勒布朗·詹姆斯等人物的推荐以及持续展示串关选项来投注串关。

尽管做出了这些努力，但由于促销、广告和高额州税，利润率仍然很低。这使得那些持续获胜并以正期望值投注的精明玩家成为盈利的主要威胁。他们利用套利，在赔率调整前下注，并且通常会避开针对休闲投注者的高抽水串关。

由于美国法律通常允许企业拒绝服务，因此体育博彩公司使用数据科学来识别和限制精明玩家的投注限额。本质上，体育博彩公司依赖于吸引会输钱的非理性投注者，并积极劝退专业赌徒，这使得他们的商业模式依赖于输家。

---

## 55. Epic Games 称苹果新安装流程降低用户流失率 60%

**原文标题**: Epic Games says Apple's new install process cuts user drop-offs by 60%

**原文链接**: [https://techcrunch.com/2025/10/01/epic-games-says-apples-new-install-process-cuts-user-drop-offs-by-60/](https://techcrunch.com/2025/10/01/epic-games-says-apples-new-install-process-cuts-user-drop-offs-by-60/)

苹果iOS 18.6简化安装流程后，Epic Games报告其游戏商店在iOS上的安装过程中用户流失率显著下降60%。 此项更改由《数字市场法案》(DMA) 推动，并源于对苹果最初加载“恐吓屏幕”的安装流程的批评和罚款，减少了向用户显示的有关从替代市场安装应用程序的警告。

在iOS 18.6之前，65%的用户放弃了Epic Games商店的安装。更新后，流失率降至25%，更接近于在Windows和macOS上观察到的安装率。

尽管取得了这一进步，Epic Games仍然批评苹果更广泛的政策，包括核心技术费、公证要求以及对替代应用商店分发的其他限制。 他们重申，苹果在macOS上对应用安装采取的更开放方式体现了双重标准。

文章还提到了Epic Games对谷歌在Android上第三方应用商店冗长且警示性安装过程的类似批评。 Epic Games认为，谷歌的警告误导用户，让他们认为来自竞争对手的应用程序可能有害。

---

## 56. 注意加密根：当ZFS崩溃时如何保存你的数据

**原文标题**: Mind the encryptionroot: How to save your data when ZFS loses its mind

**原文链接**: [https://sambowman.tech/blog/posts/mind-the-encryptionroot-how-to-save-your-data-when-zfs-loses-its-mind/](https://sambowman.tech/blog/posts/mind-the-encryptionroot-how-to-save-your-data-when-zfs-loses-its-mind/)

本文详细描述了一起因 ZFS 原生加密与 ZFS send/recv 进程之间微妙的交互作用而导致的近乎灾难性的数据丢失事件，特别是关于加密根数据集的问题。作者概述了一种场景，其中加密的 ZFS 池（“old”）在密钥更改和快照传输后进行了迁移，导致数据集无法解密。

核心问题源于在已将快照发送到备份池（“sneakernet”）后，将“old/encrypted”数据集（加密根）上的加密密钥从密码更改为十六进制密钥。这意味着备份池的加密根保留了旧的基于密码的密钥参数，而子数据集的主密钥则使用新的十六进制包装密钥进行了加密。当尝试从备份还原时，系统无法解密子数据集，因为加密根使用的是旧密码，而子数据集则使用新的十六进制密钥进行加密。

本文强调了持续备份测试的重要性，以及在验证完成之前避免破坏性操作的重要性。它还深入研究了 ZFS 和 ZFS 原生加密的内部运作机制，包括写入时复制、Merkle 树、超级块、创建时间、主密钥和包装密钥等概念。作者正准备进一步调试该问题，并最终修复损坏的状态以抢救数据。

---

## 57. 炎症比胆固醇更能预测心脏病

**原文标题**: Inflammation now predicts heart disease more strongly than cholesterol

**原文链接**: [https://www.empirical.health/blog/inflammation-and-heart-health/](https://www.empirical.health/blog/inflammation-and-heart-health/)

本文认为，通过高敏C反应蛋白（hs-CRP）血液检测测量的炎症，现在比胆固醇更能预测心脏病，并且美国心脏病学会（ACC）现在建议普遍进行hs-CRP筛查。

多年来，低密度脂蛋白胆固醇（LDL）一直是心血管风险评估的主要关注点。然而，本文指出，hs-CRP现在比LDL更能预测心脏病，因为胆固醇水平通常可以通过他汀类药物控制。因此，残余风险存在于其他生物标志物中，例如hs-CRP。

本文随后总结了关于降低炎症治疗的临床试验及其结果。他汀类药物，尤其是在高hs-CRP个体中，秋水仙碱和卡纳单抗已显示出益处，而一些抗炎药，如甲氨蝶呤、肿瘤坏死因子（TNF）抑制剂和皮质类固醇则没有。抗炎饮食、锻炼和戒烟等生活方式干预也有效。

理想的hs-CRP水平低于1 mg/L，而高于3 mg/L的水平表示高风险。虽然存在其他炎症生物标志物，但hs-CRP是最具成本效益的测量指标。

文章最后指出，ACC建议进行常规hs-CRP检测，并强调了诸如IL-6抑制剂等新兴疗法，以及用于检测血管炎症的影像技术。

---

## 58. C++26：std::optional

**原文标题**: C++26: Std:Optional

**原文链接**: [https://www.sandordargo.com/blog/2025/10/01/cpp26-optional-of-reference](https://www.sandordargo.com/blog/2025/10/01/cpp26-optional-of-reference)

Sandor Dargo 的这篇文章讨论了 C++26 的新特性 `std::optional<T&>`，该特性允许 `std::optional` 持有引用。 之前，`std::optional` 只能持有值，迫使开发者使用 `std::reference_wrapper` 来持有引用。

`std::optional<T&>` 是一种非拥有类型，其内部行为类似于指针，作为原始指针的一种更安全的替代方案，用于表达 “我不拥有此对象” 的关系。`std::optional<T&>` 的设计选择侧重于最大限度地减少意外和潜在错误。赋值会重新绑定引用，而不是复制对象。不允许使用 `make_optional<T&>`，因为它可能导致悬垂引用；必须直接构造 `optional<T&>`。该 optional 表现出浅const性，这意味着解引用一个 const `optional<T&>` 会产生一个非 const `T&`，建议使用 `optional<const T&>` 来实现深const性。`value_or` 方法按值返回一个 `T`，避免了意外的引用语义并支持字面值回退。作者建议即将到来的提案可能会引入 optional 的自由函数，以提高它们在各种情况下的效用。总的来说，`std::optional<T&>` 旨在通过提供一种更安全、更具表现力的方式来管理可选引用，从而提高代码的可读性并减少错误。

---

## 59. 纽约公寓楼部分坍塌，高层建筑被撕开巨洞

**原文标题**: NYC apartment building partially collapses, ripping massive hole in high rise

**原文链接**: [https://www.nbcnews.com/news/us-news/new-york-city-apartment-building-partially-collapses-ripping-massive-h-rcna234919](https://www.nbcnews.com/news/us-news/new-york-city-apartment-building-partially-collapses-ripping-massive-h-rcna234919)

纽约市布朗克斯区亚历山大大道的一栋公共住房公寓楼于周三上午约8点10分（东部时间）发生局部坍塌，初步调查显示，原因可能是焚化炉井道坍塌，并可能由爆炸引发。

纽约市消防局已对该建筑物附属的重大结构坍塌事件作出回应。幸运的是，由于事件发生在锅炉房，目前尚未收到人员伤亡报告。

一段视频显示，建筑物侧面出现一道巨大的裂缝。作为预防措施，F和G栋的居民正在疏散，并将在附近的社区中心得到照顾。爱迪生联合电气公司已关闭该建筑物的天然气供应。

市长埃里克·亚当斯已建议居民在进行检查时避开该区域。州议员阿曼达·塞普蒂莫呼吁追究责任，强调需要适当的资源分配以确保社区安全，并要求明确了解坍塌的原因和责任。坍塌原因的调查仍在进行中。

---

## 60. 三星试点将其智能冰箱变成广告牌，此前用户已购买

**原文标题**: Samsung Pilots Making Its Smart Fridges Billboards After People Bought Them

**原文链接**: [https://www.techdirt.com/2025/09/29/samsung-pilots-making-its-smart-fridges-billboards-after-people-bought-them/](https://www.techdirt.com/2025/09/29/samsung-pilots-making-its-smart-fridges-billboards-after-people-bought-them/)

文章探讨了三星一项备受争议的决定，即在客户购买智能冰箱后，在其上试行广告。作者对此做法表示强烈反对，认为这是一种侵扰，也是避免购买新型互联网连接家电的原因。作者宁愿继续使用旧家电，即使需要维修，也要避免智能技术可能带来的不必要广告和数据收集。主要观点是作者不信任制造商在已购买产品上引入广告的行为，并优先选择较旧、较简单的家电，而不是可能具有侵入性的智能技术。

---

## 61. Imgur因数据监管机构威胁罚款而退出英国。

**原文标题**: Imgur pulls out of UK as data watchdog threatens fine

**原文链接**: [https://www.express.co.uk/news/uk/2115228/image-site-imgur-pulls-out](https://www.express.co.uk/news/uk/2115228/image-site-imgur-pulls-out)

热门图片托管平台Imgur在英国信息专员办公室(ICO)示意将对其处以罚款后，已退出英国市场，罚款与保护儿童数据相关。ICO启动了一项调查，作为其儿童代码战略的一部分，该战略旨在为处理年轻人个人信息的在线服务设定标准。

ICO已发出通知，打算对Imgur的母公司MediaLab处以罚款，这是基于调查的初步结果。具体违规行为和潜在的罚款金额尚未披露，但MediaLab将有机会在做出最终决定前作出回应。

ICO强调，退出英国并不能让公司逃避之前数据保护违规行为的责任，调查仍在进行中。保护儿童数据是ICO的首要任务，他们打算追究提供在线服务的公司保障这些信息的责任。Imgur成立于2009年，并于2021年被MediaLab AI Inc收购，最近在英国已无法使用。该公司已被联系要求置评。

---

## 62. 发布HN：Airweave (YC X25) – 让代理搜索任何应用

**原文标题**: Launch HN: Airweave (YC X25) – Let agents search any app

**原文链接**: [https://github.com/airweave-ai/airweave](https://github.com/airweave-ai/airweave)

Airweave，YC X25 推出，是一款工具，让代理商能够通过创建可搜索的知识库（来自应用程序内容、生产力工具、数据库和文档存储）来搜索各种应用程序。它通过 REST API 或 MCP 提供标准化接口，本质上是构建一个语义可搜索的 MCP 服务器。该平台处理身份验证、数据提取、嵌入和提供服务。

该平台启动迅速，提供托管服务或使用 Docker 的自托管选项。它支持超过 25 种集成，允许用户连接来源、配置同步，并通过 UI（可在 `http://localhost:8080` 访问）或 Swagger 文档（可在 `http://localhost:8001/docs` 访问）查询数据。

提供 Python 和 TypeScript/JavaScript 的 SDK，方便集成。主要功能包括数据同步、实体提取和转换、具有 OAuth2 的多租户架构、增量更新、语义搜索和版本控制。

Airweave 的技术栈包括 React/TypeScript 前端（使用 ShadCN）、FastAPI (Python) 后端、用于元数据的 PostgreSQL、用于向量的 Qdrant 以及用于部署的 Docker Compose/Kubernetes。欢迎在 MIT 许可下做出贡献。用户可以通过 Discord、GitHub Issues 或 Twitter 联系，以获取支持、错误报告和更新。

---

## 63. 虚拟内存基础

**原文标题**: Fundamental of Virtual Memory

**原文链接**: [https://nghiant3223.github.io/2025/05/29/fundamental_of_virtual_memory.html](https://nghiant3223.github.io/2025/05/29/fundamental_of_virtual_memory.html)

本文旨在提供对虚拟内存的基础理解，阐释其目的、实现和管理。文章首先强调了RAM和磁盘存储之间的速度差异，突出了RAM对于CPU访问的必要性。

随后，文章将简单的连续内存分配与更复杂的页面调度策略进行对比，后者用于对抗外部碎片。页面调度涉及将内存划分为固定大小的帧，进程访问虚拟内存，而操作系统将其映射到物理内存。它使用页表来将虚拟页面映射到物理帧。按需调页通过仅加载必要的页面来优化内存使用，使用页表中的有效-无效位来跟踪页面状态，并在需要时处理缺页中断。

文章详细介绍了虚拟内存布局，说明了进程的内存如何组织成诸如内核空间、栈、内存映射区域、堆和代码段等段。它提供了关于栈分配的细节，讨论了栈如何随着函数调用而增长和收缩、栈指针的作用，以及使用RLIMIT_STACK管理栈大小。栈大小是固定的，与主线程的栈分离，每个线程可以拥有自己的栈，这些栈是使用系统调用创建的。

---

## 64. Kagi 新闻

**原文标题**: Kagi News

**原文链接**: [https://blog.kagi.com/kagi-news](https://blog.kagi.com/kagi-news)

Kagi News是一款全新的综合性每日新闻回顾，旨在解决现代新闻消费中的点击诱饵、广告盈利和信息过载等问题。它致力于高效地提供必要信息，尊重读者的智慧和时间。

Kagi News聚合来自不同来源的社区精选RSS订阅源，并利用人工智能将其提炼成一份简洁的每日简报，只需五分钟即可阅读。其主要设计原则以读者为先，在世界协调时中午左右提供每日更新，促进视角多样性，并通过不跟踪或利用用户注意力来确保隐私。来源是开源且社区驱动的，允许通过公共GitHub存储库进行贡献和改进。用户可以自定义类别、故事深度和版块顺序，以根据自己的兴趣定制简报。Kagi News还通过Kagi Translate支持多种语言，以原始语言显示区域性新闻。

重要的是，Kagi News通过使用公开可用的RSS订阅源来尊重发布商，尊重他们关于内容包含的选择。Kagi鼓励厌倦了令人焦虑和毫无信息的新闻的用户尝试Kagi News，该应用可在网页、iOS和Android上使用。

---

## 65. 仅限女性出租车：墨西哥城司机反抗残暴暴力

**原文标题**: Taxis for women only: Mexico City drivers rebel against brutal violence

**原文链接**: [https://www.cnn.com/2025/09/23/americas/mexico-city-women-only-taxis-as-equals-intl-cmd](https://www.cnn.com/2025/09/23/americas/mexico-city-women-only-taxis-as-equals-intl-cmd)

在针对女性暴力猖獗的墨西哥城，女性出租车和网约车司机面临着重大的安全风险，包括袭击、抢劫甚至谋杀。曾多次遭受袭击的司机露丝·罗哈斯和她的女儿卡琳娜·阿尔巴创办了仅限女性的出租车服务AmorrAs，以解决女性对更安全交通选择的需求。

AmorrAs是一家集商业和社会互助于一体的企业，雇用了23名女性司机，并为女性提供免费的法律和心理咨询。该服务以安全为先，提供实时乘车监控和一个支持网络。其具有竞争力的价格和对安全的关注培养了一批忠实的客户。

文章重点介绍了优步司机卡拉·帕特里夏·科尔特斯的故事，她在工作时被枪杀身亡，尽管该公司提供了安全功能。这一事件引发了抗议，并突显了网约车司机的脆弱性。

尽管墨西哥已经实施了改革来保护零工的权利，但确保他们的身体安全仍然是一个挑战。主要的网约车应用程序提供安全功能，但司机仍然会遭受骚扰、暴力，甚至死亡。罗哈斯强调，上班不应使女性的生命面临危险，女性有权在没有恐惧的情况下工作。

---

## 66. 蒂姆·伯纳斯-李发明了万维网，现在他想拯救它。

**原文标题**: Tim Berners-Lee Invented the World Wide Web. Now He Wants to Save It

**原文链接**: [https://www.newyorker.com/magazine/2025/10/06/tim-berners-lee-invented-the-world-wide-web-now-he-wants-to-save-it](https://www.newyorker.com/magazine/2025/10/06/tim-berners-lee-invented-the-world-wide-web-now-he-wants-to-save-it)

本文介绍了万维网的发明者蒂姆·伯纳斯-李，以及他目前“拯救”万维网的使命，以使其摆脱当前面临的问题，如虚假信息、令人上瘾的算法以及科技垄断的力量。尽管他做出了巨大的贡献，伯纳斯-李仍然相对默默无闻，更喜欢在学术界和家庭之间保持简单的生活。

文章详细描述了伯纳斯-李在欧洲核子研究中心 (CERN) 工作期间创建网络的背景，强调了他对不同计算机系统的不满以及对统一信息共享平台的需求。他将互联网和超文本相结合，创建了 HTML、HTTP 和 URL，并在 1991 年推出了第一个网站。伯纳斯-李选择不为他的发明申请专利，而是倡导开放访问和公平使用。

文章回顾了网络普及之初的挑战，特别提到了马克·安德森开发的 Mosaic 和 Netscape，以及随后的“浏览器大战”。为了应对碎片化并确保网络保持开放和可访问，伯纳斯-李于 1994 年创立了万维网联盟 (W3C)，该联盟通过协作和共识制定技术标准。

现在，伯纳斯-李对网络的现状感到担忧，用户已经变得依赖于掠夺性平台，并且缺乏对其数据的控制权。他的解决方案是 Solid 协议，旨在通过赋予用户对其数据的所有权来彻底改变网络。他还成立了一家名为 Inrupt 的公司，以促进 Solid 的采用。文章强调了未来的挑战，但突出了伯纳斯-李过去在促进协作和创新以造福网络方面的成功。

---

## 67. 塑造我的软件文章

**原文标题**: Software essays that shaped me

**原文链接**: [https://refactoringenglish.com/blog/software-essays-that-shaped-me/](https://refactoringenglish.com/blog/software-essays-that-shaped-me/)

This article, titled "Software essays that shaped me," is a personal reflection on the author's 20-year journey in software development, highlighting influential essays that significantly altered their thinking. The author shares a curated list of impactful writings, each with a brief explanation of its relevance and personal impact.

The essays cover a range of topics, from developer respect and team investment ("The Joel Test") to leveraging type systems for security ("Parse, don’t validate"). The author discusses the importance of understanding essential versus accidental complexity in software engineering ("No Silver Bullet") and the user experience cost of providing excessive choices ("Choices"). Raymond Chen's essay emphasizes catering to the customer in compatibility design.

Erik Kuefler's "Don't Put Logic in Tests" argues for clarity and simplicity in unit testing, prioritizing readability over code reusability. Julia Evans's piece on plain JavaScript led the author to abandon complex frameworks and embrace modern JavaScript's capabilities. Finally, "Choose Boring Technology" advocates for opting for established, reliable technologies over trendy, cutting-edge options to minimize risk and complexity.

Ultimately, the author emphasizes that these essays have fundamentally influenced their approach to software development, from prioritizing developer experience to simplifying user interfaces and technology choices.


---

## 68. Policy as code using your favorite programming language with WebAssembly

**原文标题**: Policy as code using your favorite programming language with WebAssembly

**原文链接**: [https://chainloop.dev/blog/introducing-webassembly-policy-engines/](https://chainloop.dev/blog/introducing-webassembly-policy-engines/)

生成摘要时出错

---

## 69. Coding a new BASIC interpreter in 2025 to replace a slow one

**原文标题**: Coding a new BASIC interpreter in 2025 to replace a slow one

**原文链接**: [https://nanochess.org/ecs_basic.html](https://nanochess.org/ecs_basic.html)

生成摘要时出错

---

## 70. Random Attractors – Found using Lyapunov Exponents (2001)

**原文标题**: Random Attractors – Found using Lyapunov Exponents (2001)

**原文链接**: [https://paulbourke.net/fractals/lyapunov/](https://paulbourke.net/fractals/lyapunov/)

生成摘要时出错

---

## 71. Microsoft Agent Framework

**原文标题**: Microsoft Agent Framework

**原文链接**: [https://azure.microsoft.com/en-us/blog/introducing-microsoft-agent-framework/](https://azure.microsoft.com/en-us/blog/introducing-microsoft-agent-framework/)

生成摘要时出错

---

## 72. There is a huge pool of exceptional junior engineers

**原文标题**: There is a huge pool of exceptional junior engineers

**原文链接**: [https://workweave.dev/blog/hiring-only-senior-engineers-is-killing-companies](https://workweave.dev/blog/hiring-only-senior-engineers-is-killing-companies)

生成摘要时出错

---

## 73. Hollywood is fuming over a new 'AI actress'

**原文标题**: Hollywood is fuming over a new 'AI actress'

**原文链接**: [https://www.cnn.com/2025/09/30/tech/hollywood-ai-actor-backlash](https://www.cnn.com/2025/09/30/tech/hollywood-ai-actor-backlash)

生成摘要时出错

---

## 74. Tiny worlds: A minimal implementation of DeepMind's Genie world model

**原文标题**: Tiny worlds: A minimal implementation of DeepMind's Genie world model

**原文链接**: [https://github.com/AlmondGod/tinyworlds](https://github.com/AlmondGod/tinyworlds)

生成摘要时出错

---

## 75. Atuin Desktop: Runbooks That Run – Now Open Source

**原文标题**: Atuin Desktop: Runbooks That Run – Now Open Source

**原文链接**: [https://blog.atuin.sh/atuin-desktop-open-source/](https://blog.atuin.sh/atuin-desktop-open-source/)

生成摘要时出错

---

## 76. Design of the SCHEME-78 Lisp-based microprocessor (1980)

**原文标题**: Design of the SCHEME-78 Lisp-based microprocessor (1980)

**原文链接**: [https://dl.acm.org/doi/10.1145/359024.359031](https://dl.acm.org/doi/10.1145/359024.359031)

生成摘要时出错

---

## 77. Can you use GDPR to circumvent BlueSky's adult content blocks?

**原文标题**: Can you use GDPR to circumvent BlueSky's adult content blocks?

**原文链接**: [https://shkspr.mobi/blog/2025/09/can-you-use-gdpr-to-circumvent-blueskys-adult-content-blocks/](https://shkspr.mobi/blog/2025/09/can-you-use-gdpr-to-circumvent-blueskys-adult-content-blocks/)

生成摘要时出错

---

## 78. Styx Emulator Public Release

**原文标题**: Styx Emulator Public Release

**原文链接**: [https://stumbl.ing/posts/styx-emulator-release/](https://stumbl.ing/posts/styx-emulator-release/)

生成摘要时出错

---

## 79. Rio Terminal: A hardware-accelerated GPU terminal emulator

**原文标题**: Rio Terminal: A hardware-accelerated GPU terminal emulator

**原文链接**: [https://rioterm.com/](https://rioterm.com/)

生成摘要时出错

---

## 80. Dgsh – Directed graph shell

**原文标题**: Dgsh – Directed graph shell

**原文链接**: [https://www2.dmst.aueb.gr/dds/sw/dgsh/](https://www2.dmst.aueb.gr/dds/sw/dgsh/)

生成摘要时出错

---

## 81. How does lossless compression in Fuji RAF files work? (2020)

**原文标题**: How does lossless compression in Fuji RAF files work? (2020)

**原文链接**: [https://capnfabs.net/posts/fuji-raf-compression-algorithm/](https://capnfabs.net/posts/fuji-raf-compression-algorithm/)

生成摘要时出错

---

## 82. Decentralizing Quality

**原文标题**: Decentralizing Quality

**原文链接**: [https://matthewstrom.com/writing/decentralizing-quality/](https://matthewstrom.com/writing/decentralizing-quality/)

生成摘要时出错

---

## 83. Buy a vintage military airplane for $25

**原文标题**: Buy a vintage military airplane for $25

**原文链接**: [https://www.popsci.com/technology/buy-vintage-airplane-wyoming/](https://www.popsci.com/technology/buy-vintage-airplane-wyoming/)

生成摘要时出错

---

## 84. Show HN: Sculptor – A UI for Claude Code

**原文标题**: Show HN: Sculptor – A UI for Claude Code

**原文链接**: [https://imbue.com/sculptor/](https://imbue.com/sculptor/)

生成摘要时出错

---

## 85. Claude Sonnet 4.5

**原文标题**: Claude Sonnet 4.5

**原文链接**: [https://www.anthropic.com/news/claude-sonnet-4-5](https://www.anthropic.com/news/claude-sonnet-4-5)

生成摘要时出错

---

## 86. How has mathematics gotten so abstract?

**原文标题**: How has mathematics gotten so abstract?

**原文链接**: [https://lcamtuf.substack.com/p/how-has-mathematics-gotten-so-abstract](https://lcamtuf.substack.com/p/how-has-mathematics-gotten-so-abstract)

生成摘要时出错

---

## 87. Organize your Slack channels by "How Often", not "What"

**原文标题**: Organize your Slack channels by "How Often", not "What"

**原文链接**: [https://aggressivelyparaphrasing.me/2025/09/30/organize-your-slack-channels-by-how-often-not-what/](https://aggressivelyparaphrasing.me/2025/09/30/organize-your-slack-channels-by-how-often-not-what/)

生成摘要时出错

---

## 88. 设计自主循环

**原文标题**: Designing agentic loops

**原文链接**: [https://simonwillison.net/2025/Sep/30/designing-agentic-loops/](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/)

生成摘要时出错

---

## 89. The Unknown Genre in Videogames [video]

**原文标题**: The Unknown Genre in Videogames [video]

**原文链接**: [https://www.youtube.com/watch?v=HUiW-GV72QE](https://www.youtube.com/watch?v=HUiW-GV72QE)

生成摘要时出错

---

## 90. Google CTF 2025 – webz : Exploiting zlib's Huffman Code Table

**原文标题**: Google CTF 2025 – webz : Exploiting zlib's Huffman Code Table

**原文链接**: [https://velog.io/@0range1337/CTF-Google-CTF-2025-webz-Exploiting-zlibs-Huffman-Code-Table-English](https://velog.io/@0range1337/CTF-Google-CTF-2025-webz-Exploiting-zlibs-Huffman-Code-Table-English)

生成摘要时出错

---

## 91. Orbiting the Hénon Attractor

**原文标题**: Orbiting the Hénon Attractor

**原文链接**: [https://observablehq.com/@yurivish/orbiting-the-henon-attractor](https://observablehq.com/@yurivish/orbiting-the-henon-attractor)

生成摘要时出错

---

## 92. Comprehension debt: A ticking time bomb of LLM-generated code

**原文标题**: Comprehension debt: A ticking time bomb of LLM-generated code

**原文链接**: [https://codemanship.wordpress.com/2025/09/30/comprehension-debt-the-ticking-time-bomb-of-llm-generated-code/](https://codemanship.wordpress.com/2025/09/30/comprehension-debt-the-ticking-time-bomb-of-llm-generated-code/)

生成摘要时出错

---

## 93. Wikipedia co-creator reveals how the CIA hijacked entries

**原文标题**: Wikipedia co-creator reveals how the CIA hijacked entries

**原文链接**: [https://www.dailymail.co.uk/news/article-15150661/Wikipedia-Larry-Sanger-CIA-hijacked-entries.html](https://www.dailymail.co.uk/news/article-15150661/Wikipedia-Larry-Sanger-CIA-hijacked-entries.html)

生成摘要时出错

---

## 94. The Beer Can

**原文标题**: The Beer Can

**原文链接**: [https://brr.fyi/posts/beer-can](https://brr.fyi/posts/beer-can)

生成摘要时出错

---

## 95. Deml: Directed Acyclic Graph Elevation Markup Language

**原文标题**: Deml: Directed Acyclic Graph Elevation Markup Language

**原文链接**: [https://github.com/Mcmartelle/deml](https://github.com/Mcmartelle/deml)

生成摘要时出错

---

## 96. Geothermal is too expensive, but Dig Energy's small drill rig might fix that

**原文标题**: Geothermal is too expensive, but Dig Energy's small drill rig might fix that

**原文链接**: [https://techcrunch.com/2025/09/09/geothermal-is-too-expensive-but-dig-energys-impossibly-small-drill-rig-might-fix-that/](https://techcrunch.com/2025/09/09/geothermal-is-too-expensive-but-dig-energys-impossibly-small-drill-rig-might-fix-that/)

生成摘要时出错

---

## 97. Founder sentenced to seven years in prison for fraudulent sale to JPMorgan

**原文标题**: Founder sentenced to seven years in prison for fraudulent sale to JPMorgan

**原文链接**: [https://www.cnn.com/2025/09/30/business/charlie-javice-frank-sentenced-jpmorgan-intl](https://www.cnn.com/2025/09/30/business/charlie-javice-frank-sentenced-jpmorgan-intl)

生成摘要时出错

---

## 98. Computer Vision: Algorithms and Applications, 2nd ed

**原文标题**: Computer Vision: Algorithms and Applications, 2nd ed

**原文链接**: [https://szeliski.org/Book/](https://szeliski.org/Book/)

生成摘要时出错

---

## 99. Prompt analytics for MCP servers

**原文标题**: Prompt analytics for MCP servers

**原文链接**: [https://hyprmcp.com/blog/mcp-server-prompt-analytics/](https://hyprmcp.com/blog/mcp-server-prompt-analytics/)

生成摘要时出错

---

## 100. AI tools I wish existed

**原文标题**: AI tools I wish existed

**原文链接**: [https://sharif.io/28-ideas-2025](https://sharif.io/28-ideas-2025)

生成摘要时出错

---

