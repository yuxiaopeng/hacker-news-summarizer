# Hacker News 热门文章摘要 (2025-11-08)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 股票代码：别死于心脏病

**原文标题**: Ticker: Don't Die of Heart Disease

**原文链接**: [https://myticker.com/](https://myticker.com/)

贾里德·赫克特的文章《定时炸弹：别死于心脏病》指出，心脏病是一种可预防的主要死因，却常常被标准医疗手段忽视。赫克特分享了他通过私人定制医疗服务提供的高级检测发现早期心脏病的个人经历，这与他通过使用标准血脂检查从初级保健医生那里得到的“完全正常”的评估形成对比。

核心信息是，个人必须为自己的心脏健康负责。赫克特强调，标准医疗实践往往会遗漏ApoB和Lp(a)等关键生物标志物，而经济实惠且易于获得的检测（每年约300美元）可以检测到早期预警信号。这些检测，再加上生活方式的改变和药物治疗，可以显著降低心脏病发作的风险。

赫克特为掌控心脏健康提供了一个路线图，敦促读者要求他们的医生进行全面的检查并理解结果。他的目标是普及通常为富人保留的知识和实践，使30多岁和40多岁的人能够积极地管理自己的心脏健康，避免成为统计数据中的一员。他认为需要一家专注于心脏病预防的面向消费者的公司，并希望这份指南能够激发人们的兴趣和行动。

---

## 2. Zig很酷，C更酷。

**原文标题**: Zig is so cool, C is cooler

**原文链接**: [https://github.com/little-book-of/c/blob/main/articles/zig-is-cool-c-is-cooler.md](https://github.com/little-book-of/c/blob/main/articles/zig-is-cool-c-is-cooler.md)

这看起来像是托管在某个平台（可能是 GitHub 或类似平台）上的一个名为 "little-book-of/c" 的项目的网页摘要。标题 "Zig 很酷，C 更酷" 暗示了 Zig 编程语言和 C 编程语言之间的趣味比较。"little-book-of/c" 可能指的是一个关于 C 编程语言的小型入门资源或教程项目。

要点：

*   **项目名称：** little-book-of/c（暗示一个关于 C 的小型入门资源）
*   **主题：** Zig 和 C 之间的比较（标题暗示倾向于 C）
*   **受众：** 对学习 C 或将 C 与 Zig 进行比较的人。
*   **互动：** 分叉数相对较低（16），但星数相当可观（332），表明具有一定的受欢迎程度和关注度。

---

## 3. Cloudflare 清理了顶级域名列表中的 Aisuru 僵尸网络

**原文标题**: Cloudflare Scrubs Aisuru Botnet from Top Domains List

**原文链接**: [https://krebsonsecurity.com/2025/11/cloudflare-scrubs-aisuru-botnet-from-top-domains-list/](https://krebsonsecurity.com/2025/11/cloudflare-scrubs-aisuru-botnet-from-top-domains-list/)

Cloudflare正应对Aisuru僵尸网络，该网络由大量受感染的物联网设备组成，并且增长迅速。起因是其域名意外地在Cloudflare最常被请求的网站排名中名列前茅。这个能够发起大规模DDoS攻击的僵尸网络最初使用Google的DNS服务器，但随后切换到Cloudflare的（1.1.1.1），导致其域名在Cloudflare的排名中占据主导地位。

Aisuru域名激增引发了对安全性、品牌混淆（由于模仿主要云提供商）和隐私（一个域名是一个街道地址）的担忧。Cloudflare的回应是编辑了恶意域名，并添加了关于恶意行为影响排名的声明。首席执行官Matthew Prince解释说，排名系统是基于DNS查询量，Aisuru正在操纵该查询量，既攻击Cloudflare的DNS服务，又可能影响排名。

专家们对Cloudflare处理此事的方式存在分歧。一些人，如Renee Burton，承认基于DNS查询对域名进行排名的复杂性。另一些人，如Alex Greenland，批评Cloudflare损害了其排名的完整性，认为该系统应该反映真实的人类使用情况，而不是自动化流量。他建议完全分离恶意域名，因为Cloudflare的排名被广泛用于信任和安全判断。

虽然Cloudflare已经开始从其网站列表中隐藏Aisuru域名，但它们仍然出现在下载的电子表格中。对这些域名的大部分DNS查询来自美国，这与之前关于Aisuru依赖于托管在美国ISP上的受感染物联网设备的发现相符。专家建议阻止以“.su”（前苏联顶级域名）结尾的域名，作为检测潜在Aisuru僵尸网络活动的一种简单方法，因为它经常被用于网络犯罪。

---

## 4. Btop：一款优于 htop 且具有游戏化界面的现代替代品

**原文标题**: Btop: A better modern alternative of htop with a gamified interface

**原文链接**: [https://github.com/aristocratos/btop](https://github.com/aristocratos/btop)

Btop：一款现代C++资源监视器，是htop的替代品，提供游戏风格的菜单系统和完整的鼠标支持。它显示处理器、内存、磁盘、网络和进程的使用情况和统计信息。

主要功能包括响应式UI、进程过滤、轻松排序、树状视图、信号发送、UI配置菜单、自适应缩放网络图、磁盘IO活动、电池电量显示和自定义预设。

该软件支持主题，并在特定目录中搜索主题。它鼓励用户贡献新的主题。欢迎赞助和捐赠。

Btop需要支持真彩色的终端、UTF8区域设置以及支持Unicode盲文图案、几何形状、框线绘制和块元素的字体。Linux（NVIDIA、AMD、INTEL）提供可选的GPU监控依赖项。

提供了适用于各种Linux发行版（openSUSE、Fedora、RHEL/Rocky/AlmaLinux）、FreeBSD、NetBSD、macOS（通过Homebrew）和Linux（通过Homebrew）的安装说明。详细说明了Linux和macOS的编译说明，包括GPU支持和静态链接的选项。对于Linux，用户可以使用Make或CMake进行编译。

---

## 5. 用于符号表达式操作的代数语言（1958）[pdf]

**原文标题**: An Algebraic Language for the Manipulation of Symbolic Expressions (1958) [pdf]

**原文链接**: [https://softwarepreservation.computerhistory.org/LISP/MIT/AIM-001.pdf](https://softwarepreservation.computerhistory.org/LISP/MIT/AIM-001.pdf)

该文档是一个PDF文件，包含“用于操作符号表达式的代数语言”（1958）。然而，所提供的内容主要是PDF元数据和压缩数据流，而非文章的实际文本。存在大量的二进制数据，似乎与字体定义、图像数据和其他PDF格式化元素有关。还有一些看起来像是被压缩的图像数据，以二进制形式存储。

由于文章的核心文本被编码在这些数据流中，因此无法辨别论文的实际内容、论点或结论。从提供的片段中唯一容易提取的信息是标题和文章的撰写年份。

---

## 6. AI 基准测试是个糟糕的笑话——而大语言模型厂商正在暗自发笑

**原文标题**: AI benchmarks are a bad joke – and LLM makers are the ones laughing

**原文链接**: [https://www.theregister.com/2025/11/07/measuring_ai_models_hampered_by/](https://www.theregister.com/2025/11/07/measuring_ai_models_hampered_by/)

生成摘要时出错

---

## 7. 从零开始的C++移动语义 (2022)

**原文标题**: C++ move semantics from scratch (2022)

**原文链接**: [https://cbarrete.com/move-from-scratch.html](https://cbarrete.com/move-from-scratch.html)

本文从头开始解释 C++ 移动语义，首先设想一种不存在移动语义的场景。 旨在提供清晰的理解，并在最初的解释中弱化 `std::move` 的作用。

核心概念是右值引用 (`&&`) 本质上是常规左值引用 (`&`) 的“着色”版本。 它们的行为相同但互不兼容，从而允许函数重载来区分它们。 这种区分实现了一种特定的优化策略：无需复制大型数据结构（如 vectors），可以通过转移所有权来“移动”或“窃取”数据。 这涉及复制元数据并指向现有的堆分配数据，然后将原始容器置为空以防止错误。

本文介绍了这个想法的演变，最终使用右值引用来表示“移动”数据而不是复制的意图。 创建特殊的构造函数和赋值运算符来接受右值引用。 在其中，编写算法以从一个对象“窃取”数据并将数据传输到另一个对象。

然后，文章讨论了资源管理应用程序，例如 `std::shared_ptr` 和 `std::unique_ptr`，其中移动可以避免昂贵的引用计数更新或强制执行独占所有权。

最后，文章解释了 `std::move` 仅仅是一个到右值引用的强制转换。 它调用函数的特定重载或构造函数，按照惯例，该函数或构造函数实现“移动”操作，如果移动不适用，则回退到复制。 关键在于，移动语义是由旨在不同地处理右值引用的函数重载驱动的，而不是由任何固有的魔力驱动的。

---

## 8. Zig 为什么这么酷？

**原文标题**: Why is Zig so cool?

**原文链接**: [https://nilostolte.github.io/tech/articles/ZigCool.html](https://nilostolte.github.io/tech/articles/ZigCool.html)

本文介绍了 Zig 编程语言，它因能够编译 C 代码并交叉编译到不同的架构而备受赞誉。文章强调了 Zig 独特的编程方法，超越了简单地替代 C/C++。

文章指导初学者安装 Zig 编译器并构建一个基本的 "Hello World!" 程序。然后深入探讨 Zig 的核心概念和命令，包括变量声明、结构体、匿名结构体、测试块和位域。文章重点介绍了 Zig 的循环和数组语法，强调自动类型推断和高效的内存管理。

讨论的一个关键特性是 Zig 的“测试块”，它允许在模块内进行测试，而无需单独的可执行文件，从而方便原型设计和验证。文章还介绍了 Zig 使用带有函数的结构体实现的面向对象编程功能，并解释了如何构建和执行 Zig 程序。

调试部分介绍了使用 `@breakpoint` 内置函数，这是一种用于调试没有符号的优化代码的“hack”方法，使开发人员能够使用 `std.debug.print` 在特定点检查变量值。

最后，文章简要介绍了 Zig 在底层编程方面的能力。

---

## 9. Valdi – 提供原生性能的跨平台UI框架

**原文标题**: Valdi – A cross-platform UI framework that delivers native performance

**原文链接**: [https://github.com/Snapchat/Valdi](https://github.com/Snapchat/Valdi)

Valdi：为原生性能和开发者效率而生的跨平台UI框架。目前正处于beta阶段，但已在Snap的生产应用中使用8年。与其他依赖Web视图的跨平台框架不同，Valdi将声明式的TypeScript UI代码直接编译成iOS、Android和macOS的原生视图，消除了JavaScript桥接。

主要优势包括：通过自动视图回收、优化组件渲染、优化的布局引擎和视口感知渲染等功能实现真正的原生性能。Valdi强调开发者体验，提供即时热重载、完整的VSCode调试和熟悉的TSX语法。其灵活的采用模式允许将Valdi组件嵌入到现有的原生应用程序中，反之亦然。它支持使用C++、Swift、Kotlin或Objective-C编写性能关键代码，并具有与TypeScript的类型安全绑定。

Valdi通过自动代码生成绑定、直接访问原生API、TypeScript和原生代码之间的双向通信以及原生protobuf支持，提供深入的原生集成。该框架为Snap应用中的关键功能提供支持，包括高级动画和复杂手势。

它具有Flexbox布局系统、工作线程、原生动画、高级手势识别、内置测试框架和Bazel集成。可通过Discord获得支持，该项目采用MIT许可证。

---

## 10. 使民主运作：修复和简化平等Paxos

**原文标题**: Making Democracy Work: Fixing and Simplifying Egalitarian Paxos

**原文链接**: [https://arxiv.org/abs/2511.02743](https://arxiv.org/abs/2511.02743)

本文 arXiv 文章“使民主发挥作用：修复和简化平等 Paxos”（EPaxos*）介绍了一种经过纠正和简化的平等 Paxos (EPaxos) 状态机复制协议。作者 Fedor Ryabinin、Alexey Gotsman 和 Pierre Sutra 解决了原始 EPaxos 中存在的复杂性、模糊规范和错误。

EPaxos 是一种无领导者共识协议，旨在克服与基于领导者的协议（如 Paxos）相关的单点故障和延迟问题。它允许副本协同排序命令，即使在 *n* = 2*f*+1 个进程中最多发生 *f* 个进程崩溃，也能保持吞吐量。在更有利的故障条件下（不超过 *e* = ⌈(f+1)/2⌉ 个故障和可交换命令），EPaxos 仅需两次消息延迟即可实现快速命令执行。

EPaxos* 的主要贡献是一种更简单且经过严格证明是正确的故障恢复算法。此外，该协议将 EPaxos 推广到支持更广泛的故障阈值，特别是 *n* ≥ max{2*e*+*f*-1, 2*f*+1}，作者声称这是最优的。本文的扩展版本已在 OPODIS'25 上发表。

---

## 11. 我和我的朋友们不小心伪造了锐龙7 9700X3D的泄露信息。

**原文标题**: My friends and I accidentally faked the Ryzen 7 9700X3D leaks

**原文链接**: [https://old.reddit.com/r/pcmasterrace/comments/1orc6jl/my_friends_and_i_accidentally_faked_the_ryzen_7/](https://old.reddit.com/r/pcmasterrace/comments/1orc6jl/my_friends_and_i_accidentally_faked_the_ryzen_7/)

Reddit帖子讲述了作者和他们的朋友如何无意中制造了关于Ryzen 7 9700X3D处理器的虚假泄露。事情起初只是一个玩笑：他们编辑了一张CPU-Z的截图，显示了一个虚构的Ryzen处理器的捏造规格，包括核心数量、时钟速度和L3缓存大小。然后他们在他们的朋友圈内分享了这张伪造的图片。

其中一位朋友，没有意识到这只是个玩笑，并信以为真，将修改后的截图发布到了网上，很可能是在一个科技论坛或社交媒体平台上。这张图片迅速传播开来，获得了关注，并被各种科技新闻媒体和YouTube用户报道为真实的泄露信息。

作者和他们的朋友对他们捏造的信息传播如此之快和广泛感到惊讶和有些惊慌。他们承认自己行为的不负责任，即使他们并没有打算让这张图片在这种情况下公开。这篇文章强调了虚假信息在网上传播的容易程度，尤其是在科技领域，泄露信息经常被分享和讨论。作者还对他们的行为可能对AMD的声誉产生的潜在影响表示担忧，即使是间接的，并希望澄清有助于纠正记录。这篇文章是对在网上散布未经证实的信息的危险性的警示。

---

## 12. 52年旧磁带或含Unix历史

**原文标题**: 52 Year old data tape could contain Unix history

**原文链接**: [https://www.theregister.com/2025/11/07/unix_fourth_edition_tape_rediscovered/](https://www.theregister.com/2025/11/07/unix_fourth_edition_tape_rediscovered/)

在犹他大学发现了一盘可能具有重大意义的Unix历史磁带，标签为“UNIX Original From Bell Labs V4”。 这盘磁带可以追溯到1973年左右，可能包含用C语言编写的第一个版本的UNIX，由于已知存在的UNIX V4版本很少，这使得它成为一项极具价值的发现。

这盘磁带是在清理储藏室时被发现的，并被Robert Ricci教授确认为带有他已故导师Jay Lepreau的笔迹。 历史背景表明，这盘磁带是由马丁·纽厄尔收到的，他以发明计算机图形学中无处不在的物体——犹他茶壶而闻名。

由于磁带的年代久远且可能很脆弱，因此正在小心地将其运送到位于加利福尼亚州山景城的计算机历史博物馆 (CHM)。 CHM的软件管理员Al Kossow计划使用专门的设备，包括高速模数转换器和分析软件，尝试进行数据恢复。 鉴于这一潜在发现的稀有性，Kossow正在优先考虑恢复工作。 成功检索数据可以为UNIX的早期开发以及向C编程语言的过渡提供宝贵的见解。

---

## 13. Ruby 中的友善属性模式

**原文标题**: Friendly attributes pattern in Ruby

**原文链接**: [https://brunosutic.com/blog/ruby-friendly-attributes-pattern](https://brunosutic.com/blog/ruby-friendly-attributes-pattern)

本文介绍了 Ruby 中的“友善属性模式”，这是一种简化属性定义并使其更具可读性和简洁性的技术。作者在开发 RailsBilling 时，为了减少代码重复并改善创建账单计划的体验而开发了这种模式。

其核心思想是基于预定义的规则，将各种数据类型（整数、符号、持续时间）转换为标准的属性键值对。例如，整数被解释为金额，符号被解释为名称，持续时间被解释为间隔。这允许更具表现力且更短的代码，例如 `Billing::Plan.find_or_create_all_by_attrs!(1.month => {standard: 10, pro: 50, enterprise: 100})`，而不是多次使用冗余属性键的 `find_or_create_by!` 调用。

该模式支持灵活的输入格式，包括数组、哈希，甚至单个值，这些都会被转换为标准属性。它还允许将友善属性与传统的键值属性混合使用，并且向后兼容。作者还描述了一种树状结构实现，用于处理嵌套属性以减少重复。

在承认潜在缺点的同时，作者认为该模式的灵活性和可读性超过了风险。他们强调，友善属性主要供人使用，不应用于 API 设计或数据存储。最后，他们提供了一个概念性的例子，说明该模式如何应用于物联网门锁系统。

---

## 14. 空中旅行规划的计算复杂度 (2003) [pdf]

**原文标题**: Computational Complexity of Air Travel Planning (2003) [pdf]

**原文链接**: [http://www.ai.mit.edu/courses/6.034f/psets/ps1/airtravel.pdf](http://www.ai.mit.edu/courses/6.034f/psets/ps1/airtravel.pdf)

由于提供的内容无法提供对文章“航空旅行规划的计算复杂性（2003）”的摘要。 此文本似乎是原始的、编码的PDF文件，而不是文章的实际文本。 它仅包含PDF格式信息和编码流，不包含文章的摘要、引言、方法、结果或结论。 因此，我无法确定文章的主题、范围、发现或撰写摘要所需的任何其他信息。 我需要文章的实际文本才能对其进行总结。

---

## 15. 逆向工程解析神经网络解决二进制加法的巧妙方案 (2023)

**原文标题**: Reverse engineering a neural network's clever solution to binary addition (2023)

**原文链接**: [https://cprimozic.net/blog/reverse-engineering-a-small-neural-network/](https://cprimozic.net/blog/reverse-engineering-a-small-neural-network/)

凯西·普里莫奇逆向工程了一个小型神经网络（422个参数），该网络经过训练可在 8 位无符号整数上执行二进制加法。 他惊讶于它学习得如此之好，原本预计一个更大的网络会模仿二进制加法器电路。

该网络巧妙地利用输入层的权重将二进制输入转换为模拟信号，模仿数模转换器 (DAC)。 然后，它在第一层中使用一种名为“Ameo”的自定义激活函数（或者，正弦函数），将模拟信号映射为具有不同周期的周期性正弦波状信号。 这些周期与二进制数字（1、2、4、8 等）的切换周期直接相关，有效地编码了加法结果。

随后的层细化这些信号，将它们“饱和”成更接近目标输出值 -1 和 1 的方波状形状。 后面的层主要关注第一层输出的路由和组合。 该网络甚至学会了通过组合来自具有不同周期的神经元的输出来创建移位信号。

普里莫奇的研究突出了神经网络可以设计出的出乎意料且高效的解决方案，这与预期的基于逻辑门的方法大相径庭。 他最后思考是否可以使用自定义架构使更大的模型更有效率，同时承认了“痛苦的教训”，即缩放和通用方法的至高无上地位。 他仍然对梯度下降的力量以及这些模式从随机性中持续涌现出来印象深刻。

---

## 16. 八哥：为符号密集型编程语言设计的等宽字体

**原文标题**: Myna: Monospace typeface designed for symbol-heavy programming languages

**原文链接**: [https://github.com/sayyadirfanali/Myna](https://github.com/sayyadirfanali/Myna)

Myna：一款为编程设计的新等宽字体，解决了许多现有字体中符号显得像事后诸葛亮的问题。其核心理念是“符号优先设计”，优先考虑编程语言中常用 ASCII 符号的清晰度和视觉重量。这使得多字符符号（如 `->` 和 `>>=`）实现近乎完美的对齐，符号和字母数字字符之间实现平衡的视觉重量，标点符号采用简约形式，并且清晰区分易混淆的字符（如 `1 l I |` 和 `0 O o`）。

Myna 具有语言感知能力，为 Perl、Haskell 和 C 等语言提供定制字形。当前版本侧重于单一字重，但未来可能会根据社区需求扩展连字。

该字体可通过克隆 GitHub 存储库或下载发布版安装在 Linux、macOS 和 Windows 上。它采用 SIL 开放字体许可证 1.1 版授权。Myna 的开发灵感来自多种备受推崇的等宽字体，包括 Source Code Pro、Fira Mono、Inconsolata、Plex Mono、Office Code Pro 和 Anonymous Pro。

作者积极征求社区的反馈和贡献，特别是关于错误报告和扩展字体字符集和功能的特性请求。提供联系信息以便直接沟通。

---

## 17. 使用 ZFS Jail 在 FreeBSD 上实现不可变软件部署

**原文标题**: Immutable Software Deploys Using ZFS Jails on FreeBSD

**原文链接**: [https://conradresearch.com/articles/immutable-software-deploy-zfs-jails](https://conradresearch.com/articles/immutable-software-deploy-zfs-jails)

本文详细介绍了如何在FreeBSD上使用ZFS jails和Caddy反向代理来实现不可变软件部署。核心思想是基于基础镜像的ZFS快照为每次部署创建一个新的、隔离的jail，从而确保干净且可重现的环境。

该过程始于为jails设置一个专用的环回网络接口，并启用ZFS和jail服务。下载、提取并配置一个基础FreeBSD镜像作为模板。对于每次部署，都会创建一个模板的ZFS克隆，形成一个新的jail。然后，应用程序部署在此jail内部。

Caddy充当反向代理，根据健康检查端点（例如 `/up`）将流量路由到当前健康的jail。在新jail通过健康检查后，Caddy会被重新配置，将流量导向它，从而实现零停机升级。

关键步骤包括：

*   为jails创建ZFS数据集，并为媒体、模板和容器创建子数据集。
*   构建基础镜像模板并使用必要的配置进行快照。
*   克隆基础镜像模板，为每次部署创建一个新的jail，并以Git提交SHA命名。
*   使用环回接口上的专用IP地址和一个应用程序的服务定义来配置jail。
*   设置Caddy以执行健康检查并将流量路由到健康的jail。

本文强调了这种方法的好处，包括零停机部署、即时回滚以及一致且可重现的环境，最终带来更高的可靠性和更轻松的管理。

---

## 18. 本地日光黑暗模式 (2021)

**原文标题**: Dark mode by local sunlight (2021)

**原文链接**: [https://www.ctnicholas.dev/articles/dark-mode-by-sunlight](https://www.ctnicholas.dev/articles/dark-mode-by-sunlight)

克里斯·尼古拉斯的这篇文章探讨了如何根据用户的位置和当地的日照情况自动启用网站的暗黑模式。作者认为，使用日照水平来决定主题是一种用户友好的方法。

文章概述了该过程：首先，使用Geolocation API（或后端API）确定用户的位置。然后，使用SunCalc NPM包根据用户的位置和一年中的时间计算当地的日出和日落时间。这是必要的，因为日出和日落时间会根据地点和一年中的时间而显著变化。

计算出的日出和日落时间随后会与用户的当前时间进行比较，以确定是否激活暗黑或亮色模式。作者还建议基于黎明、黄昏、黄金时段结束和黄金时段添加一个“暮光模式”，以提供更渐进的过渡。

文章强调，应优先考虑可访问性。用户可能有特定的配色方案偏好，例如患有散光的人可能会在深色背景上的浅色文本中遇到光晕。作者建议尊重用户偏好的配色方案，这可以使用CSS和JavaScript媒体查询来检测。最后，文章提倡即使在实现了自动切换时，也要包含一个手动暗黑模式开关。

---

## 19. 我怎么会在这里？

**原文标题**: How did I get here?

**原文链接**: [https://how-did-i-get-here.net/](https://how-did-i-get-here.net/)

本文解释了网站 "how-did-i-get-here.net" 的运作方式，重点介绍其路由追踪功能。它解析了互联网路由的复杂性以及如何将其可视化呈现给用户。

该网站使用一个名为 "ktr" 的自定义路由追踪程序，追踪数据包从服务器到用户 IP 地址的路径（一种“反向路由追踪”）。Ktr 利用 ICMP 数据包及其“生存时间”(TTL) 字段来识别路径上的路由器。通过发送 TTL 递增的数据包，该程序会收到来自每个路由器的错误消息，从而揭示它们的 IP 地址。

本文详细介绍了幕后流程：服务器接收 HTTP 请求，启动路由追踪，然后在路由追踪进行时，以块的形式流式传输网页内容。采用了一种巧妙的 CSS 技巧，使路由追踪看起来像是在实时加载，而无需 JavaScript。

文章解释了自治系统 (ASes) 的概念，即由公司拥有的网络。 文章强调了边界网关协议 (BGP) 在使这些网络能够通信方面的作用。BGP 允许边界路由器共享路由表，从而确定数据包到达其目的地的最佳路径。这些路由是通过 ASes 之间的对等安排建立的。作者承认 AS 所有者对互联网的固有控制权。

作者对现有的互联网结构资源表示不满，并希望该网站能够启发人们，进一步强调该项目的开源性质。

---

## 20. 我为什么热爱 OCaml (2023)

**原文标题**: Why I love OCaml (2023)

**原文链接**: [https://mccd.space/posts/ocaml-the-worlds-best/](https://mccd.space/posts/ocaml-the-worlds-best/)

作者在体验过 Haskell 和 Go 之后，表达了对 OCaml 的喜爱。作者作为一名函数式编程爱好者，最初欣赏 Haskell 强大的静态保证和分解复杂问题的能力，但发现其复杂性和缓慢的编译时间令人沮丧。Go 提供了简洁性、快速的性能、良好的工具和快速的编译，但作者不喜欢其冗长、脆弱的错误处理以及缺乏函数式编程特性。

作者认为，OCaml 实现了平衡。它通过 sum types 和模式匹配提供了强大的静态保证，一个类似于 Go 的更简单的运行时（用于系统编程的垃圾回收），以及非常快的编译时间。OCaml 的单二进制编译简化了部署，其出色的文档工具（odig、utop、接口/实现分离）增强了代码探索。作者还欣赏自动类型推断和模块化的代码组织。

作者总结说，OCaml 代表了简单性和表达性之间的正确平衡，再加上出色的文档和工具，使其成为一种非常令人愉快和高效的语言，尽管它已经存在了一段时间，并且有一些可能不必要的功能。

---

## 21. 哈姆扎·埃尔·丁的努比亚童谣翻译

**原文标题**: Nubeian Translation for Childhood Songs by Hamza El Din

**原文链接**: [https://nubianfoundation.org/translations/](https://nubianfoundation.org/translations/)

本文呈现了汉姆扎·艾尔·丁的两首努比亚童年歌曲“Nabra”和“童年”的英文翻译和音译。 除了英文翻译和音译之外，还提供了努比亚语的原始歌词，并包含努比亚语的阿拉伯语版本。

“Nabra”围绕着记忆、爱和渴望的主题展开。 歌者不断地询问Nabra，问她是否还记得他和他们的过去。 这首歌运用了黄金、美好的一天和爱的意象。 后半部分侧重于观察一个美丽的女孩("Too buru lim ajbikisa")以及与之相关的爱和渴望之情。 这首歌以对消失的反思和祈祷结束，质疑过去的缺席，并表达悲伤。

“童年”是对围绕在枣椰树中玩耍、采集枣子和尼罗河的童年记忆的怀旧回忆。 它使用了白色衣服“kissoola”像绵羊和蜂蜜的甜美（“Inna silsoot”）的生动意象，发誓永远不会忘记这些经历。 这首歌也触及了与那田园诗般的过去分离的主题 ("Mingai ai forakai goka")。

这些翻译归功于Nabra Nelson和Dore Kolod，突出了在保存和分享这些努比亚歌曲方面的合作努力。 该文档还引导读者浏览“阿斯旺的努比亚音乐”上提供的更多翻译。

---

## 22. 最初理想客户画像工作表

**原文标题**: The Initial Ideal Customer Profile Worksheet

**原文链接**: [https://www.reifyworks.com/writing/2023-01-30-iicp](https://www.reifyworks.com/writing/2023-01-30-iicp)

迈克尔·伯恩斯坦的这篇文章介绍了“初始理想客户画像（IICP）工作表”，作为一种工具，帮助企业在启动以客户画像驱动的营销时，选择最有效的买家角色进行重点关注。核心思想是优先确定一个客户画像，并以此为基础进行构建。

该工作表基于三个关键支柱评估潜在的客户画像：

*   **产品优势：** 产品与客户画像的契合程度。
*   **市场规模：** 客户画像所代表的细分市场规模是否合适（既不太小众也不太宽泛）。
*   **分销策略：** 企业能够有效且真实地触达客户画像的程度。

文章建议列出最多三个不同的客户画像，并使用问卷调查（以Google Doc格式提供）来评估每个客户画像在这三个标准下的表现。团队成员也可以参与评估。

文章提供了一个李克特量表评分系统（从-2到+2），用于量化每个问题的置信度，从而促进数据驱动的决策。然而，文章最终强调选择企业最了解的客户画像。这有助于更有效地进行信息传递、定位，以及自信地评估产品与市场的契合度。

最后，文章强调了客户画像选择与市场进入策略之间的联系，告诫企业不要选择需要企业不擅长的策略的客户画像。文章敦促企业诚实地评估分销策略，并鼓励企业可视化针对所选客户画像量身定制的营销内容。选择客户画像后的下一步是开发引人注目的价值故事。

---

## 23. Mullvad：关闭我们的搜索代理Leta

**原文标题**: Mullvad: Shutting down our search proxy Leta

**原文链接**: [https://mullvad.net/en/blog/shutting-down-our-search-proxy-leta](https://mullvad.net/en/blog/shutting-down-our-search-proxy-leta)

Mullvad将于2025年11月27日关闭其搜索代理Leta。Leta的主要目的是通过汇集和缓存众多用户的请求来增强搜索隐私。然而，Mullvad认为，不断发展的搜索行业将使Leta在未来效果降低。他们建议，现在可以通过将VPN与注重隐私的浏览器相结合来实现类似的隐私优势。因此，Mullvad将停止Leta，并将重点放在通过自身的研究、开发以及与合作伙伴的协作来推进VPN和浏览器隐私。本质上，Mullvad正在将其重点从专用的搜索代理转向更全面的VPN和基于浏览器的隐私解决方案。

---

## 24. Cerebras Code 现在支持 GLM 4.6，速度达 1000 tokens/秒

**原文标题**: Cerebras Code now supports GLM 4.6 at 1000 tokens/sec

**原文链接**: [https://www.cerebras.ai/code](https://www.cerebras.ai/code)

Cerebras Code现已提供GLM 4.6访问权限，这是一款顶级开源编码模型，速度超过每秒1000个token。GLM 4.6擅长工具调用，在伯克利函数调用排行榜上名列前茅，并且在web开发性能方面与Sonnet 4.5相媲美。用户可以通过API密钥将Cerebras Code Pro与任何AI友好的代码编辑器集成，包括Cline、RooCode、OpenCode和Crush，无需切换工具。

Cerebras提供三个访问级别：

*   **免费：** 限制token和请求，仅供演示。
*   **Pro（$50）：** 快速、高上下文补全，每天最多2400万个token，适合独立开发者和简单的agentic工作流程。
*   **Max（$200）：** 每天访问1.2亿个token，非常适合全职开发、IDE集成、代码重构和多代理系统。

该平台强调速度和集成，使开发人员能够在现有工作流程中利用GLM 4.6的编码能力。

---

## 25. 纽约电影节被当局叫停

**原文标题**: Authorities Shut Down Film Festival in New York

**原文链接**: [https://www.hrw.org/news/2025/11/07/china-authorities-shut-down-film-festival-in-new-york](https://www.hrw.org/news/2025/11/07/china-authorities-shut-down-film-festival-in-new-york)

人权观察报告称，纽约首届独立中国电影节因中国政府骚扰参展导演、制片人及其在中国的家人，导致他们撤回影片而被“暂停”。原定于2025年11月8日至15日举行的电影节由朱日坤组织。

据中国艺术家和活动家蒋思涛称，几乎所有在中国的参展导演都面临恐吓，甚至海外导演也报告说，他们在中国的亲友接到了警方的威胁电话。截至11月4日，超过三分之二的影片已取消放映。朱日坤表示，暂停电影节的决定是为了保护与电影节相关的人免受进一步骚扰。

文章强调，过去十年，中国对独立电影节的打压日益加强，并指出云之南纪录影像展、中国独立影像展和北京独立影像节已被关闭。文章还提到，批评政府的电影制作人，如沈勇平、陈品霖受到起诉和监禁，艺术家郭振明的设备被没收。

文章还指出，香港当局以“国家安全”为由禁止了13部电影，中国的跨国镇压已经超越了电影领域，影响到维吾尔族、藏族和香港社群的艺术展览和艺术家。人权观察敦促各国政府和艺术机构抵制中国日益增长的对海外自由表达的影响，并就中国官员的虐待行为质问他们。

---

## 26. YouTube移除Windows 11绕过教程，称存在“人身伤害风险”

**原文标题**: YouTube Removes Windows 11 Bypass Tutorials, Claims 'Risk of Physical Harm'

**原文链接**: [https://news.itsfoss.com/youtube-removes-windows-11-bypass-tutorials/](https://news.itsfoss.com/youtube-removes-windows-11-bypass-tutorials/)

YouTube以下架Windows 11教程视频引发争议：内容审核机制遭质疑

---

## 27. Ruby 已经解决了我的问题。

**原文标题**: Ruby already solved my problem

**原文链接**: [https://newsletter.masilotti.com/p/ruby-already-solved-my-problem](https://newsletter.masilotti.com/p/ruby-already-solved-my-problem)

生成摘要时出错

---

## 28. 苹果正在跨越乔布斯的红线

**原文标题**: Apple is crossing a Steve Jobs red line

**原文链接**: [https://kensegall.com/2025/11/07/apple-is-crossing-a-steve-jobs-red-line/](https://kensegall.com/2025/11/07/apple-is-crossing-a-steve-jobs-red-line/)

肯·西格尔的文章认为，在蒂姆·库克领导下的苹果公司正在侵蚀以用户体验为中心的原则，而这些原则曾是史蒂夫·乔布斯不可逾越的“红线”，特别是通过在其产品和服务中引入广告。

作者回顾了 20 世纪 90 年代末的一个故事，当时苹果公司曾考虑提供广告支持的 Mac OS 版本，甚至提供付费的无广告选项，但乔布斯最终拒绝了这个想法。乔布斯认为这会降低 Mac 用户所珍视的“纯粹、优雅、简洁的界面”，从而保护苹果的核心价值观。

西格尔认为，最近在 App Store 中引入广告以及预计在 Apple Maps 中引入广告，都代表着对这种理念的背离。他认为这种转变是由增加收入的愿望驱动的，并质疑这种决定是否将利润置于客户满意度之上。

作者推测乔布斯会反对这一举动，即使以牺牲潜在收入为代价，也会优先考虑用户体验。他认为，蒂姆·库克接受广告反映了苹果公司优先事项的根本性改变，即将收入置于客户体验之上。

---

## 29. 苹果的“公证”——阻碍开发者和用户的软件自由

**原文标题**: Apple's "notarisation" – blocking software freedom of developers and users

**原文链接**: [https://fsfe.org/news/2025/news-20251105-01.en.html](https://fsfe.org/news/2025/news-20251105-01.en.html)

本文批评了苹果公司针对iOS应用程序的“公证”流程，认为其违反了欧盟《数字市场法》（DMA）的精神和目标。核心论点是，无论分发渠道如何，所有应用程序都需要经过苹果的审查和重新签名，这种“公证”赋予了苹果公司对软件安装的过度控制，扼杀了竞争并阻碍了软件自由。

本文重点介绍了一项针对苹果公司的公民社会投诉，该投诉认为，“公证”以及对替代应用商店的高额财务要求（如100万欧元的信用证）非法限制了侧载，阻止了第三方应用商店的有效运营，并限制了互操作性。

对于自由软件开发者来说，“公证”需要接受限制性条款、不透明的流程以及应用DRM，从而损害了用户自由验证和重新分发软件的权利。本文将此与像F-Droid这样的去中心化软件管理模式进行对比，在F-Droid中，信任通过透明的验证流程和社区审计进行分配。

该投诉敦促欧盟委员会执行DMA，处以罚款，并寻找替代苹果控制的方案，以促进去中心化的软件管理。本文最后总结说，苹果公司的安全声明是为看门行为掩盖的，而真正的DMA合规需要真正的开放性，赋予用户在其设备上安装和共享软件的自由。

---

## 30. 天使投资人实战指南

**原文标题**: Angel Investors, a Field Guide

**原文链接**: [https://www.jeanyang.com/posts/angel-investors-a-field-guide/](https://www.jeanyang.com/posts/angel-investors-a-field-guide/)

天使投资人实战指南：一位成功创业者的视角。作者强调，战略性天使投资人不仅能提供资金，还能对初创企业的成功产生重大影响。

文章区分了不同类型的天使投资人：提供早期启动资金的天使（如导师），提供互补专业知识和人脉的战略天使，提供社会声望的虚荣天使（名人），以及亲友。作者倡导选择能弥补专业知识和人脉缺口的天使，而非纯粹为了社会影响力。

有效利用天使投资人需要建立关系，通过每月更新（包括具体需求和感谢）保持沟通，并了解他们与机构投资者的独特之处。天使不会争夺未来的所有权，因此可以自由地将创始人介绍给其他风险投资家，并产生更广泛的兴趣。

作者以天使投资人的视角（通过与 a16z 的合作关系）强调了对公司所解决问题的热情以及相信自己能够提供帮助的重要性。他们偏爱 B2B SaaS、产品主导型增长和开发者工具，专注于理解公司解决的问题和团队的执行力。

总之，文章建议创始人明智地选择天使投资人，认识到股权空间的限制和信号的重要性。精心选择的一组天使可以显著提升初创企业的轨迹。

---

## 31. 七集合维恩图

**原文标题**: Venn Diagram for 7 Sets

**原文链接**: [https://moebio.com/research/sevensets/](https://moebio.com/research/sevensets/)

本文介绍了一个七集合维恩图。虽然在没有实际可交互或可视元素的情况下无法访问具体内容（“您的浏览器不支持Canvas”消息表明缺少视觉元素），但我们可以推断出主要主题：

核心在于呈现一个维恩图，它可以表示并直观地展示七个不同集合之间的关系。传统的维恩图对于2个或3个集合来说相对容易构建，但随着集合数量的增加，它们变得越来越复杂，难以清晰地表示。一个七集合维恩图将是一个非常复杂的表示。

本文可能探讨了一种特定的视觉布局，旨在有效地显示这七个集合及其各种可能的交集。它可能讨论：

*   **用于表示集合的圆形/形状的具体形状或排列。** 标准的重叠圆圈通常变得难以管理，因此可能会使用替代形状和排列。
*   **图表的可读性和清晰度。** 一个关键挑战是确保各种交集易于识别和理解。
*   **七集合维恩图的潜在应用。** 这可能涉及数据分析、逻辑、集合论等领域，或任何可视化多个重叠组之间关系很重要的领域。
*   **可能涉及数学基础，解释如何构建图表以满足图中所有可能的2^7 - 1个区域。**

---

## 32. FSF40编程马拉松

**原文标题**: FSF40 Hackathon

**原文链接**: [https://www.fsf.org/events/fsf40-hackathon](https://www.fsf.org/events/fsf40-hackathon)

自由软件基金会(FSF)将于2025年11月21日至23日举办全球在线黑客马拉松，作为其40周年庆典的一部分。本次黑客马拉松旨在改进自由软件项目，并突出自由软件开发者的工作。参与者可以个人或以最多四人的团队形式为自由软件目录、GNU Boot、GNU Guix、Lewa、LibreVR、op-mattermost 和 Org Mode 等项目做出贡献。

本次活动欢迎所有技能水平的参与者，为开发者和非开发者都提供可参与的任务。黑客马拉松也注重技能发展和学习。JavaScript、Python、Emacs Lisp和DIY硬件知识等特定技能对某些项目有益。

注册是免费的，鼓励捐款以支持FSF和GNU。奖品将颁发给首次贡献者、多元化团队以及最具影响力的贡献。证书将颁发给参与者以表彰他们的工作。在指定日期之间提交的作品将被考虑授予奖励，时区差异可根据要求进行例外处理。

FSF还在寻找赞助商和志愿者来管理黑客马拉松频道。鼓励个人和组织使用#HackFSF40分享活动。本次黑客马拉松是FSF 40周年纪念日的一系列举措之一。

---

## 33. Show HN: 查找与任何十六进制颜色匹配的丙烯颜料

**原文标题**: Show HN: Find matching acrylic paints for any HEX color

**原文链接**: [https://acrylicmatch.com/](https://acrylicmatch.com/)

此“Show HN”帖子介绍“Acrylic Match”，一个用于查找与任何给定HEX颜色代码最匹配的丙烯颜料的工具。该工具可能通过将用户输入的HEX代码与已知丙烯颜料及其相应颜色值的数据库进行比较来工作。用户可以输入一个HEX颜色代码，该工具将建议最接近的可商购丙烯颜料，这些颜料与该颜色匹配或非常相似。

帖子包含各种CSS颜色的可视化表示，表明这些是用户可选择的选项，以便快速找到与这些预定义颜色匹配的丙烯颜料。 完整的颜色名称列表暗示了该工具可以搜索的相对广泛的丙烯颜料数据库。 总体目的是通过自动将HEX代码与现成的颜料选项进行匹配，来简化艺术家和爱好者寻找合适的丙烯颜料的过程。

---

## 34. 在 Quadra 650 上运行 68060 CPU

**原文标题**: Running a 68060 CPU in Quadra 650

**原文链接**: [https://github.com/ZigZagJoe/Macintosh-Q650-68060](https://github.com/ZigZagJoe/Macintosh-Q650-68060)

该项目详细介绍了一项实验性尝试，旨在通过 ROM 修改，在 Macintosh Quadra 650/800 或 Centris 650 中运行 68060 CPU。该项目是一个概念验证，目前仅允许启动到未经修改的 System 7.1。功能有限，需要进一步开发才能实现实际可用性，而作者不打算完成这项任务。

作者警告用户该项目具有高度实验性，不建议复制，除非他们具备先进的技术知识，因为存在潜在问题。他们对使用该代码造成的任何损害或意外结果不承担任何责任。

该项目感谢 Jockelill、Aprezbios 和 Reinauer 的贡献。构建过程涉及使用 Retro68 或标准的 m68K GCC 工具链，然后将生成的镜像刷入与 Quadra 兼容的 ROM SIMM 中。

作者以授予无限制使用权的许可发布所有材料。他们强调了引用内容时注明原始创作者的重要性。

---

## 35. 成为一名编译器工程师

**原文标题**: Becoming a compiler engineer

**原文链接**: [https://rona.substack.com/p/becoming-a-compiler-engineer](https://rona.substack.com/p/becoming-a-compiler-engineer)

无法访问文章链接。

---

## 36. Ribir: Rust/WASM 的非侵入式 GUI 框架

**原文标题**: Ribir: Non-intrusive GUI framework for Rust/WASM

**原文链接**: [https://github.com/RibirX/Ribir](https://github.com/RibirX/Ribir)

Ribir 是一个非侵入式的 Rust GUI 框架，旨在通过单一代码库构建多平台应用程序。它专注于数据结构设计，通过数据变化自动触发 UI 更新，以此与众不同。

主要特性包括：

*   **声明式 UI:** 利用 Rust 宏进行 UI 定义，但不会强制使用新的语言。
*   **组件组合系统:** 通过函数组件、`Render` 和 `ComposeChild` 提供灵活的组件创建。
*   **非侵入式状态:** 将数据转换为可监听状态，并根据变化更新视图。
*   **Flutter 启发的布局:** 一种亚线性布局系统，用于高效的 UI 排列。
*   **组合事件系统:** 支持事件冒泡和捕获。
*   **主题系统:** 允许为子树设置不同的主题并进行运行时修改。
*   **GPU 渲染:** 利用 `wgpu` 通过路径细分进行 GPU 加速渲染。
*   **文本支持:** 基本的文本排版和 IME 输入。
*   **基础组件库:** 包含超过 20 个基础组件。

目前，Ribir 支持 Linux、Windows、macOS 和 Web，并在这些平台上进行积极的开发和测试。虽然它可以编译到移动平台（iOS 和 Android），但针对移动平台的专用 UI 适配计划在稍后阶段进行。

该项目鼓励通过改进文档、增加测试覆盖率和报告错误来进行贡献。Ribir 采用 MIT 许可证。

---

## 37. 随时准备离开 (即使你从未离开)

**原文标题**: Always Be Ready to Leave (Even If You Never Do)

**原文链接**: [https://andreacanton.dev/posts/2025-11-08-always-ready-to-leave/](https://andreacanton.dev/posts/2025-11-08-always-ready-to-leave/)

安德烈的文章强调，“准备离职”不仅仅是制定退出策略，而是培养对你有利的职业习惯，无论你留下还是离开。 在她之前公司工作七年后，安德烈概述了她如何通过以下方式顺利离职：

*   **与决策者公开沟通：** 她没有向同事抱怨，而是坦诚地与她的主管和人力资源部门讨论她的顾虑，让他们有机会解决问题，并建立在诚实基础上的关系。
*   **记录一切：** 她积极记录她的工作流程，不是作为一种退出策略，而是作为一种日常实践来理清她的思路，减轻她的认知负担，并促进更好的协作和更容易的入职。
*   **有策略地选择战斗：** 她优先考虑那些能够提升她的技能并促进她的职业发展的职责，避免那些消耗她的精力而又对她的成长没有贡献的任务。

矛盾的是，这些习惯甚至在她还在Terranova公司工作期间就改善了她的工作生活，减轻了压力，使她能够专注于有意义的工作。 她强调，“准备离职”意味着以专业的态度工作，并对你的职业生涯做出有意识的选择，而不是感到被困住。

当离职时机到来时，安德烈建议了解你的法律义务，在宣布你的离职时遵循正确的指挥链，通过促进过渡在你的最后一天仍然发挥作用，并表达真诚的感激之情。 最终，好好离职的最佳方式是一贯地好好工作，从第一天起就养成这些习惯。 她打算将这些实践延续到她的新岗位上。

---

## 38. 本地优先 Htmx

**原文标题**: Local First Htmx

**原文链接**: [https://elijahm.com/posts/local_first_htmx/](https://elijahm.com/posts/local_first_htmx/)

本文介绍了“本地优先 HTMX”的概念，这是一种构建响应式 Web 应用程序的范例。文章认为，传统的服务器端渲染 (SSR) 虽然常见，但由于每次交互都需要往返时间，可能导致性能下降。“本地优先”设计将 UI 和数据共同定位，并异步同步更改，从而提供了一种性能更高的替代方案。

核心思想是利用 HTMX（一种旨在简化前端开发的“梗”，同时也是一个严肃的工具）、WebAssembly (WASM) 和 service worker。所提出的架构涉及将 SSR 代码编译为 WASM，并在 service worker 中运行它。此 service worker 拦截所有由 HTMX 元素触发的 `fetch` 请求，在本地处理请求，渲染 HTML，并将其直接返回到浏览器。在后台，service worker 会与服务器同步数据。

这种方法旨在通过将渲染卸载到浏览器，同时保持服务器同步，从而以更少的 Javascript 代码实现基于 Javascript 的单页应用程序 (SPA) 的流畅性。作者承诺在后续文章中详细介绍“本地优先 HTMX”方法的实现、挑战和潜在的未来发展。本文提倡采用本地优先架构，以获得卓越的性能和用户体验。

---

## 39. 能否用图像代替文本，节省LLM Token？

**原文标题**: Can you save on LLM tokens using images instead of text?

**原文链接**: [https://pagewatch.ai/blog/post/llm-text-as-image-tokens/](https://pagewatch.ai/blog/post/llm-text-as-image-tokens/)

本文探讨了使用文本图像而非直接文本是否能节省LLM token。作者的灵感来自于观察到OpenAI的API对图像输入的收费token数量几乎与文本相同，尽管图像可能包含更多信息。

为了验证这一点，作者比较了使用Karpathy的博客文章的文本和图像版本所消耗的token以及成本，并提示GPT模型总结卫生习惯的技巧。该博客文章被转换为两张768x768的图像，以满足OpenAI的最佳图像尺寸要求，并确保可读性。

结果表明，虽然使用图像确实减少了prompt tokens，尤其是在GPT-5中（减少超过40%），但通常会增加completion tokens。只有GPT-5-chat模型在使用图像时产生了节省。由于completion tokens通常比prompt tokens更昂贵，因此只有使用GPT-5-chat模型才能通过此策略实现节省。

因此，文章得出结论，虽然通过使用图像代替文本来节省token是可能的，但这取决于所使用的模型，并且可能不值得权衡，例如图像准备的复杂性增加和处理时间更长。

---

## 40. VLC创始人让-巴蒂斯特·肯普夫荣获2025年欧洲自由软件奖

**原文标题**: VLC's Jean-Baptiste Kempf Receives the European SFS Award 2025

**原文链接**: [https://fsfe.org/news/2025/news-20251107-01.en.html](https://fsfe.org/news/2025/news-20251107-01.en.html)

VideoLAN主席兼VLC Media Player首席开发者让-巴蒂斯特·肯普夫因其长期致力于自由软件运动而荣获2025年欧洲SFS奖。该奖项由FSFE和LUGBZ颁发，旨在表彰他为使VLC成为无处不在且不可或缺的媒体播放器所做出的重大而持久的贡献。

VLC最初是1996年的一个学生项目，在其最初的开发者毕业后面临被放弃的可能。肯普夫介入其中，重组了代码，并激励了新的贡献者，将VLC转变为全球数十亿人使用的不可或缺的媒体播放器。他还创立了VideoLabs和VideoLAN非营利组织，以确保该软件保持免费且由社区驱动。

该奖项旨在表彰肯普夫对软件自由的承诺，抵制公司收购，并将用户自由置于利润之上。他因培养了一个充满活力的志愿者社区以及使VLC可在各种操作系统上使用而受到称赞。他的奉献精神此前曾在2018年获得法国国家功绩骑士勋章的认可。

肯普夫感谢VideoLAN和FFmpeg团队的辛勤工作和奉献精神。欧洲SFS奖旨在表彰那些在欧洲推进自由软件，促进社区建设和道德技术的个人。之前的获奖者包括Frank Karlitschek (Nextcloud) 和Bram Moolenaar (Vim)。

---

## 41. 传感器：构成、抽象、性能 (2018)

**原文标题**: Transducer: Composition, abstraction, performance (2018)

**原文链接**: [https://funktionale-programmierung.de/en/2018/03/22/transducer.html](https://funktionale-programmierung.de/en/2018/03/22/transducer.html)

Marco Schneider 的这篇文章探讨了 Clojure 中的 transducers，重点介绍了它们相比传统列表处理的组合性、抽象性和性能优势。其核心思想是 `map`、`filter` 和类似的 higher-order 函数可以使用 `reduce` 重新定义，并通过参数化累积步骤（示例中的 `conj`）进一步抽象。这种抽象允许这些操作在无需修改的情况下，作用于列表之外的数据结构，如通道。

这篇文章通过将 `map` 和 `filter` 重新定义为作用于步骤的“进程修饰符”来演示这一点，从而实现了转换逻辑和底层数据结构之间的关注点分离。通过引入 arity overloading（接受不同数量参数的函数），transducers 获得了独立于数据结构处理进程“开始”和“结束”的能力。

一个实际例子展示了使用 transducers（通过 Clojure 的内置函数 `transduce`）计算硕士研究生的平均成绩，比传统的 `filter-map-reduce` 方法快得多。 这种加速归因于避免了中间列表的创建，从而提高了吞吐量。

最后，文章通过将相同的转换过程应用于流经 Clojure 异步通道的数据，说明了 transducers 的多功能性，证明了它们在不同数据结构中的可重用性。结论强调，transducers 是传统列表函数的一种强大、可组合且高性能的替代方案，通过一致的抽象提供了显著优势。

---

## 42. 丹麦政府计划禁止15岁以下儿童访问社交媒体。

**原文标题**: Denmark's government aims to ban access to social media for children under 15

**原文链接**: [https://apnews.com/article/denmark-social-media-ban-children-7862d2a8cc590b4969c8931a01adc7f4](https://apnews.com/article/denmark-social-media-ban-children-7862d2a8cc590b4969c8931a01adc7f4)

丹麦政府拟禁止15岁以下儿童访问社交媒体，理由是担心有害内容、商业剥削以及儿童上网时长。 数字事务部长卡罗琳·斯凯表示，很大比例的13岁以下丹麦儿童已经在使用社交媒体，使他们接触到暴力和自残内容。

虽然科技平台通常有年龄限制，但这些并不总是有效。 拟议的立法旨在赋予家长在特定评估后允许13岁及以上儿童访问的权利。 政府计划在未来几个月内通过必要的立法，确保科技公司不存在漏洞可钻。 丹麦正在开发一款年龄验证应用程序，可能与其现有的国家电子身份证系统结合使用，以执行该禁令。 如果科技巨头未能实施适当的年龄验证，他们将面临高达其全球收入6%的罚款风险。

此前澳大利亚也实施了类似的禁令，将最低年龄设定为16岁，并对违规行为处以巨额罚款。 丹麦政府强调，其目的并非将儿童排除在所有数字活动之外，而是希望保护他们免受有害内容的影响。 社交媒体平台TikTok已做出回应，表示认可丹麦此举的重要性，并列举了其安全功能和家长工具。 其他科技公司尚未回应置评请求。

---

## 43. 开发板工作原理（以及如何自制）

**原文标题**: How a devboard works (and how to make your own)

**原文链接**: [https://kaipereira.com/journal/build-a-devboard](https://kaipereira.com/journal/build-a-devboard)

本教程介绍如何使用KiCad设计基于RP2040 SoC (片上系统) 的定制开发板。作者解释了PCB的基本组成部分以及如何在原理图编辑器中进行连接。

本教程涵盖五个主要元素：电源、闪存、晶体振荡器、I/O 和 RP2040 本身。它强调良好的原理图实践，例如一致的电源/地标签方向和清晰标记的组件。

文章详细介绍了如何使用电容实现电源去耦，包括为每个电源引脚使用 0.1uF 电容，以及为每条电源线（1.1V 和 3.3V）使用 1uF 电容，以滤除噪声并提供稳定的电源。 然后，它指导读者连接 USB-C 插座以进行电源和编程。 这包括接地 SHIELD/GND，通过 27 欧姆终端电阻将 D+/D- 数据线连接到 RP2040，使用 5.1K 电阻下拉 CC1 和 CC2 引脚，以及使用 NCP1117（或 MCP1700）LDO (低压差稳压器) 将 5V USB-C 输入降至 3.3V，LDO 两侧各使用 10uF 旁路电容。

本教程还介绍了晶体振荡器对于精确计时的重要性，解释了如何将其与适当的电容 (15pF/33pF) 和阻尼电阻 (1K) 连接在 PCB 上靠近 MCU 的位置。 最后，它解释了由于 RP2040 没有内置闪存，因此外部闪存的必要性，解释了 SPI 和 Quad SPI 通信协议，并通过其 QSPI 引脚将 W25Q128JVS 闪存 IC 连接到 RP2040，并使用一个 0.1uF 去耦电容进行噪声滤波。 下一步是添加一个按钮。

---

## 44. 离开Meta和PyTorch

**原文标题**: Leaving Meta and PyTorch

**原文链接**: [https://soumith.ch/blog/2025-11-06-leaving-meta-and-pytorch.md.html](https://soumith.ch/blog/2025-11-06-leaving-meta-and-pytorch.md.html)

在Meta工作十一年后，Soumith Chintala即将离职，标志着他领导PyTorch八年的结束。他表示，PyTorch从一个小项目成长为被广泛采用的AI框架，为百亿亿次级训练、基础模型提供动力，并在全球学术界和工业界得到应用，对此他感到无比自豪。尽管他承认PyTorch仍需不断发展，但他相信其最初设定的可访问性和降低准入门槛的目标已基本实现。

Soumith解释说，他离开的原因是渴望新的、小型的项目，需要探索在Meta所担任的重要职位之外的机会。他强调，考虑到他的影响力以及与人工智能行业关键人物的接触，这个决定并非轻易做出。

他对PyTorch的未来充满信心，认为强大的领导团队已经准备好指导该项目。他明确提到了Edward、Suo、Alban、Greg、John、Joe和Jana，以及他们与PyTorch最初愿景的价值一致性。他相信即使没有他的直接参与，PyTorch也会继续蓬勃发展。

Soumith深情地回忆了他在Meta的FAIR（Facebook AI Research）部门的时光，强调了协作和创新的环境。他感谢Meta的关键人物，包括马克·扎克伯格、迈克·施洛普弗、杨立昆、罗伯·弗格斯和阿帕纳·拉马尼，感谢他们对开源原则的支持和信任。他还感谢PyTorch团队和社区的无数成员的贡献。他计划继续作为用户参与其中，提供反馈和提交问题。

---

## 45. 科技股抛售潮达1万亿美元，市场对人工智能日益怀疑

**原文标题**: $1T in Tech Stocks Sold Off as Market Grows Skeptical of AI

**原文链接**: [https://gizmodo.com/1-trillion-in-tech-stocks-sold-off-as-market-grows-skeptical-of-ai-2000683226](https://gizmodo.com/1-trillion-in-tech-stocks-sold-off-as-market-grows-skeptical-of-ai-2000683226)

科技股下跌：AI投资巨头市值蒸发万亿，经济前景堪忧

---

## 46. 我在做一个小型RPG游戏，需要一些关于性能的反馈。

**原文标题**: I'm making a small RPG and I need feeback regarding performance

**原文链接**: [https://jslegenddev.substack.com/p/im-making-a-small-rpg-and-i-need](https://jslegenddev.substack.com/p/im-making-a-small-rpg-and-i-need)

无法访问文章链接。

---

## 47. 受害者信号的声誉后果：受害降低地位

**原文标题**: Reputational consequences of victim signaling: Victimhood decreases status

**原文链接**: [https://www.sciencedirect.com/science/article/pii/S0191886925004775](https://www.sciencedirect.com/science/article/pii/S0191886925004775)

无法访问文章链接。

---

## 48. GPT-OSS 120B 在 Cerebras 上运行速度达 3000 tokens/秒

**原文标题**: GPT-OSS 120B Runs at 3000 tokens/sec on Cerebras

**原文链接**: [https://www.cerebras.ai/blog/openai-gpt-oss-120b-runs-fastest-on-cerebras](https://www.cerebras.ai/blog/openai-gpt-oss-120b-runs-fastest-on-cerebras)

本文宣布OpenAI的GPT OSS 120B（一款强大的开放权重推理模型）在Cerebras系统上可用。主要结论是，Cerebras提供的性能明显快于基于GPU的解决方案。

GPT OSS 120B是一个拥有1200亿参数的模型，在推理基准测试中，其准确性可与OpenAI的o4-mini相媲美，并在编码、数学和健康相关查询等任务中表现出色。其开放权重的特性使其具有透明性和微调灵活性。

据称，Cerebras拥有高达每秒3,000个token的推理速度，比领先的GPU云快15倍。他们还声称首个token的时间仅为280毫秒，输出速度为2,700个token/秒。这种速度使其适用于需要快速响应时间的代理和编码应用程序。

此外，Cerebras声称在AIME 2025数学评估中并列第一，并具有强大的性价比优势，以不到两倍的成本提供中位数GPU云16倍的速度。该模型可在Cerebras推理云上以及通过HuggingFace、OpenRouter和Vercel等合作伙伴获得。

---

## 49. 理解交通

**原文标题**: Understanding traffic

**原文链接**: [https://dr2chase.wordpress.com/](https://dr2chase.wordpress.com/)

本文深入探讨了交通拥堵的复杂性，指出简单增加车道并非可行的解决方案。文章区分了道路速度和通行能力，强调交通堵塞会显著降低通行能力。作者强调，由于空间限制和反应时间要求，汽车在运送人员方面效率低下，导致车道容量有限。瓶颈，尤其是交叉路口，是主要原因，而解决一个瓶颈只会暴露下一个。

文章介绍了“边际驾驶者”的概念，即那些愿意忍受交通拥堵的人，从而决定了整体拥堵程度。文章还讨论了“潜在需求”，指的是那些因交通拥堵而避免开车的人，如果交通状况改善，他们就会开车。这突出了诱导需求现象，即改善的道路状况会吸引更多的驾驶者，从而可能抵消扩建带来的好处。

作者还指出，过境交通是造成拥堵的重要原因，并且路线之间相互竞争，有时会导致违反直觉的情况，例如布雷斯悖论，即移除一条道路实际上可以改善交通流量。

作者提倡具有吸引力的替代驾驶方案，例如更好、更频繁的公交，并与其他交通方式无缝衔接。他们还建议在交通中优先考虑公交，提供安全的自行车道和停车场，并支持使用电动自行车。解决那些阻碍非汽车出行方式的小问题也有助于减少交通。

最后，文章还谈到了当前自行车网络的不完善，特别是对于那些使用货运自行车或拖车的人来说，以及基础设施需要以更广阔的视野进行设计，以鼓励更多的人选择骑自行车。

---

## 50. 依依惜别

**原文标题**: A Fond Farewell

**原文链接**: [https://www.farmersalmanac.com/fond-farewell-from-farmers-almanac](https://www.farmersalmanac.com/fond-farewell-from-farmers-almanac)

《农民年鉴》宣布2026年版将是最后一版，标志着超过200年出版历程的结束。在告别信中，编辑桑迪·邓肯和彼得·盖格向他们忠实的读者、贡献者和合作伙伴表示感谢。他们承认年鉴在许多家庭中长期存在，人们利用它做各种事情，从根据月相制定的种植指南到确定各种活动的“最佳日子”。

虽然年鉴在2025年12月之后将不再提供印刷版或在线版本，但编辑们鼓励读者通过传承其智慧和传统来保持其精神的延续。他们建议将年鉴启发下的知识，如水仙花开时种植豌豆或解读夜晚红色的天空，分享给后代。

最后一版2026年版可在FarmersAlmanac.com、Amazon.com和部分当地商店购买。会员请查看收件箱以获取订阅信息。

---

## 51. 文本大小写改变二维码尺寸

**原文标题**: Text case changes the size of QR codes

**原文链接**: [https://www.johndcook.com/blog/2025/10/31/smaller-qr-codes/](https://www.johndcook.com/blog/2025/10/31/smaller-qr-codes/)

本文解释了用于生成二维码的文本的大小写如何影响二维码的大小。生成二维码时，算法将大小写混合的文本解释为二进制数据（ISO/IEC 8859-1），每个字符需要 8 位。但是，如果文本完全是大写字母，并且位于二维码的字母数字字符集（45 个字符）内，则会使用更高效的字母数字模式进行编码，即用 11 位编码两个字符（每个字符 5.5 位）。

这种更高效的编码意味着大写文本生成较小的二维码，因为它需要更少的位来表示相同的信息。给出的示例演示了在创建二维码之前将文本转换为大写时，从 33x33 像素网格减少到 29x29 像素网格。

然后，本文将此原理应用于比特币地址。Bech32 编码使用 32 个字符的单字母表，虽然比 Base58 编码（58 个字符）需要更多字符，但由于单字母表的性质以及转换为大写后字母数字编码的效率，最终会产生更小的二维码。因此，Bech32 编码需要更少的二维码像素来表示与 Base58 编码相同的数据。

---

## 52. LTO-10为何在速度和向后兼容性方面表现不佳

**原文标题**: Why LTO-10 fell short on speed and backward compatibility

**原文链接**: [https://blocksandfiles.com/2025/07/29/tape-engineering-changes-from-lto-9-to-lto-10/](https://blocksandfiles.com/2025/07/29/tape-engineering-changes-from-lto-9-to-lto-10/)

本文分析了LTO-10磁带在增加容量的同时，未能提高I/O速度并丧失与LTO-9向后兼容性的原因。LTO-9采用线性蛇形记录、叠瓦式记录和伺服带进行精确磁头定位。容量的增加传统上来自更宽/更长的磁带、更窄的磁道或更小的位区域，而I/O的改进则来自更快的磁带速度和更多的读写磁头元件。

LTO-10保持了400 MBps的原始数据速率，因为磁带材料的厚度存在物理限制，无法在不冒损坏风险的情况下提高速度。线性密度（位长度）也难以轻松提高，因此容量的增加主要来自大幅提高磁道密度。

虽然技术上可行使用64磁道读写头（可能将I/O提高到1,000 MBps），但这提出了巨大的工程挑战，因为所需的电缆数量将大幅增加。

放弃向后兼容性的决定主要由两个因素驱动。首先，客户通常会跳过几代产品，直接从LTO-7/8迁移到LTO-10。其次，LTO-10使用不同的伺服格式，采用36°角来提高磁头组件的定位分辨率。这种改变，加上改进的磁带尺寸稳定性、介质初始化以及引入的磁头倾斜跟踪控制，以处理增加的磁道密度，使得向后兼容性无法实现。本质上，对更高磁道密度的追求迫使伺服系统和磁头定位机制发生重大变化，牺牲了兼容性以换取性能潜力。

---

## 53. 1973年Wordle的实现由DEC于2022年发布。

**原文标题**: 1973 implementation of Wordle was published by DEC (2022)

**原文链接**: [https://troypress.com/1973-implementation-of-wordle-was-published-by-dec/](https://troypress.com/1973-implementation-of-wordle-was-published-by-dec/)

本文追溯了类Wordle游戏的历史渊源，将其追溯到1973年数字设备公司（DEC）发布的BASIC程序WORD。与1955年的游戏Jotto不同，WORD提供了字母位置的提示，与Wordle类似。WORD由查尔斯·里德编写，收录在畅销书《BASIC电脑游戏》中。

然后，本文扩大了范围，探索了早期计算机中猜谜游戏的历史，重点介绍了启发了许多其他游戏的FOCAL程序GUESS。这些游戏通常足够简单，可以在早期内存有限的计算机上运行，包括计算机隐藏信息，玩家必须推断出来。其他例子包括HI-LO、NUMBER、STARS、TRAP、BAGELS和HURKLE，并描述了它们独特的机制。

本文还涉及以战斗为主题的猜谜游戏，如TARGET、Bombardment、Depth Charge和Salvo，并探讨了更复杂的反向猜谜游戏，即计算机试图猜测人类的想法。例子包括ANIMAL、SALVO、DIGITS和NICOMA。

最终，本文强调了早期计算机猜谜游戏丰富多彩的历史，突出了其简单性和独创性，使得这些游戏即使在技术资源有限的情况下也能蓬勃发展。本文还提供了在浏览器中玩这些经典游戏的链接，表明了重新发现和振兴这些游戏以吸引现代观众的潜力。

---

## 54. 我为什么喜欢我的Boox Palma电子阅读器

**原文标题**: Why I love my Boox Palma e-reader

**原文链接**: [https://minimal.bearblog.dev/why-i-love-my-boox-palma-e-reader/](https://minimal.bearblog.dev/why-i-love-my-boox-palma-e-reader/)

这篇博文详细描述了作者对文石Palma电子阅读器的喜爱，以及它如何取代Kindle Paperwhite成为作者首选的阅读设备。作者强调了自己重新发现阅读这一爱好，并赞赏电子墨水技术，列举了背光、字体一致性、阳光下的对比度和便携性等关键优点。

虽然作者仍然使用Kindle，但他们也指出了导致他们寻找替代方案的几个问题。这些问题包括Kindle的尺寸使其便携性降低、亚马逊限制性的图书所有权政策、导入非亚马逊图书的困难，以及无处不在的广告带来的烦恼。

二手购买的文石Palma解决了这些问题。它小巧的尺寸和轻巧的设计使其易于放入口袋且握持舒适。完整的Android操作系统允许访问任何阅读应用程序，从而使用户摆脱了亚马逊的生态系统。屏幕质量与Kindle相当或更好，可自定义的锁屏壁纸增添了个性化色彩。此外，缺乏内置互联网鼓励了专注阅读。物理翻页按钮的加入是一项额外的好处。

作者将文石Palma与他们的Kindle进行了比较，讨论了他们首选的TPU保护套，并分享了设备的使用照片。总之，作者推荐文石Palma给那些重视极致便携性和无干扰阅读体验的人。他们表达了希望有一个自定义ROM来改进Android软件的小小愿望。

---

## 55. 研究表明人类可能拥有类似鹬鸟的远程触觉“第七感”

**原文标题**: Research first to show humans have remote touch "seventh sense" like sandpipers

**原文链接**: [https://www.qmul.ac.uk/media/news/2025/science-and-engineering/se/research-first-to-show-humans-have-remote-touch-seventh-sense-like-sandpipers.html](https://www.qmul.ac.uk/media/news/2025/science-and-engineering/se/research-first-to-show-humans-have-remote-touch-seventh-sense-like-sandpipers.html)

伦敦玛丽女王大学和伦敦大学学院的研究人员发现，人类拥有一种“远程触觉”，类似于鹬等滨鸟用来探测埋藏猎物的方式。这是人类首次被记录到拥有这种感觉。

这项研究涉及参与者在不直接接触的情况下，用手指在沙子中定位一个隐藏的立方体。结果表明，人类可以通过感知沙子中的微小位移来探测埋藏物体的存在，接近机械反射探测的理论极限。

人类和机器人性能的比较显示，在预期范围内，人类探测物体的精度达到70.7%，而机器人触觉传感器尽管从稍远的距离感知物体，但精度仅为40%。

这一发现扩展了对人类触觉认知的理解，并为开发先进的机器人触觉传感系统提供了宝贵的见解。这项研究突出了在考古学和探索火星土壤或海底等具有挑战性地形等领域的潜在应用，提高了在视觉受限任务中的安全性和效率。

研究人员强调了这项研究的多学科性质，突出了心理学、机器人学和人工智能之间的合作。玛丽女王大学的伊丽莎白塔·范思哲指出，这改变了我们对人类感知的概念，而郑启辰讨论了在辅助技术和机器人工具中的潜在应用。伦敦大学学院的洛伦佐·贾莫内强调了人类和机器人研究之间的协同作用，说明了多学科合作的力量。

---

## 56. 我用 Zig 构建 Bytebeat 播放器的经验

**原文标题**: My Experience of building Bytebeat player in Zig

**原文链接**: [https://blog.karanjanthe.me/posts/zig-beat/](https://blog.karanjanthe.me/posts/zig-beat/)

用 Zig 构建 Bytebeat 播放器 Zigbeat 的经验

这篇博文详细介绍了作者在工作间隙使用 Zig 语言构建名为 Zigbeat 的 bytebeat 播放器的经验。Bytebeat 是一种算法音乐形式，它通过使用位运算生成 8 位音频样本的短程序来产生音乐。

作者之所以选择 Zig 进行这个项目，是因为它具有类似 C 语言的风格，但没有借用检查器和复杂的语法。开发过程（包括为本机和浏览器 (wasm) 编译设置 Raylib-Zig 项目）提供了对 Zig 的内存管理和字符串处理的宝贵见解。一个重要的障碍是优化性能，这通过实现 Arena Allocator 来有效地管理 AST（抽象语法树）的内存分配来解决。最初，作者在每个样本上都为 AST 分配内存，这导致了性能问题，尤其是在浏览器中。

作者的目标是创造一种复古的 8 位合成器美学，类似于带有可视化器的旧合成器。最初使用 Raylib 的原始绘图 API 的尝试被证明很麻烦，导致探索基于精灵的设计，但作者缺乏设计经验带来了挑战。

作者得出结论，选择 Zig 而不是 JavaScript 是有益的，这导致了对 Pratt 解析和词法分析器修改等解析和评估技术的更深入理解。他们对学习经历表示满意，并鼓励读者在 GitHub 上探索 Zigbeat 项目。

---

## 57. WinObjC – iOS的Windows桥梁

**原文标题**: WinObjC – The Windows Bridge for iOS

**原文链接**: [https://github.com/microsoft/WinObjC](https://github.com/microsoft/WinObjC)

The Windows Bridge for iOS (WinObjC) is a Microsoft open-source project that allows developers to create Universal Windows Platform (UWP) apps from existing Objective-C iOS code. This enables code reuse and integration with Windows 10 features.

To use WinObjC, you need Windows 10 (build 10586 or higher) and Visual Studio 2017 with specific components selected during installation, including UWP development tools, .NET Mobile Development with Xamarin (due to Nugetizer Bug), and various SDKs and toolsets.

To import an Xcode project, install Chocolatey (a Windows package manager) and the `winobjc-tools` command-line tool using PowerShell with administrator privileges. Then, navigate to your Xcode project directory in PowerShell and run `vsimporter.exe` to generate a Visual Studio solution.

The WOCCatalog sample app in the bridge SDK is recommended for learning the bridge's features. Clone the repo, navigate to the WOCCatalog directory, open the solution in Visual Studio, set the WOCCatalog project as the startup project, and run the app.

Resources include a wiki, development roadmap, Windows Dev Center website, a quick start challenge, an FAQ, and a samples repo. Contributions are welcome through bug reports, code reviews, pull requests, and participation on Twitter and StackOverflow.

Advanced installation steps are provided for contributors who wish to build the bridge from source, including the need for Git LFS.


---

## 58. Meta预计2024年收入的10%来自诈骗。

**原文标题**: Meta projected 10% of 2024 revenue came from scams

**原文链接**: [https://sherwood.news/tech/meta-projected-10-of-2024-revenue-came-from-scams-and-banned-goods-reuters/](https://sherwood.news/tech/meta-projected-10-of-2024-revenue-came-from-scams-and-banned-goods-reuters/)

根据路透社基于Meta内部文件的报道，该公司预计其2024年收入的10%，约160亿美元，将来自诈骗广告和违禁商品销售。这些内部文件还显示，Meta意识到因未能遏制这种欺诈行为而可能面临巨额罚款。该公司策略性地优先在处罚最严厉的地区开展执法工作，权衡打击诈骗带来的收入损失与潜在的监管罚款。

虽然这些文件表明Meta旨在减少欺诈行为，但对其审核团队的削减导致大多数用户举报的违规行为被忽视或驳回。针对该报道，Meta发言人安迪·斯通声称这些文件呈现了内部执法的“选择性视角”，并断言Meta积极打击欺诈和诈骗。尽管Meta提出了上述声明，该报告凸显了该公司从欺诈广告和违禁商品中获得的巨大利益，引发了人们对其有效解决这一问题的承诺的质疑。

---

## 59. 詹姆斯·沃森去世

**原文标题**: James Watson has died

**原文链接**: [https://www.nytimes.com/2025/11/07/science/james-watson-dead.html](https://www.nytimes.com/2025/11/07/science/james-watson-dead.html)

无法访问文章链接。

---

## 60. 贝壳岩窟：英格兰神秘的地下贝壳室

**原文标题**: Shell Grotto: England's mysterious underground seashell chamber

**原文链接**: [https://boingboing.net/2025/09/05/shell-grotto-englands-mysterious-underground-seashell-chamber.html](https://boingboing.net/2025/09/05/shell-grotto-englands-mysterious-underground-seashell-chamber.html)

无法访问文章链接。

---

## 61. You should write an agent

**原文标题**: You should write an agent

**原文链接**: [https://fly.io/blog/everyone-write-an-agent/](https://fly.io/blog/everyone-write-an-agent/)

生成摘要时出错

---

## 62. A rats to riches story: Larry the Downing Street cat finds place in TV spotlight

**原文标题**: A rats to riches story: Larry the Downing Street cat finds place in TV spotlight

**原文链接**: [https://www.theguardian.com/politics/2025/nov/08/a-rats-to-riches-story-larry-the-downing-street-cat-finds-place-in-tv-spotlight](https://www.theguardian.com/politics/2025/nov/08/a-rats-to-riches-story-larry-the-downing-street-cat-finds-place-in-tv-spotlight)

住在唐宁街10号的内阁办公厅首席捕鼠官，猫咪拉里，是第四频道一部新纪录片的主题，该片旨在庆祝英国人对猫的喜爱。自2011年入住唐宁街10号以来，拉里已经经历了五位首相，并成为政治变革中备受欢迎的稳定象征。

拉里从巴特西猫狗之家被领养来解决鼠患问题，如今已成为唐宁街的常客，以其魅力征服了巴拉克·奥巴马和弗拉基米尔·泽连斯基等世界领导人。他以在镜头前的放松姿态、在正式访问期间的外交亮相以及完美地为摄影师摆姿势的能力而闻名。

尽管拉里很受欢迎，但他还是面临批评，包括被指责懒惰和过度喂养。然而，与拉里关系密切的消息人士坚称，他没有接受公共资金，唐宁街的工作人员承担了他的费用。

他的日常包括迎接客人、检查安保、在古董家具上小憩以及思考如何控制老鼠。虽然他有过竞争对手，比如来自外交部的帕默斯顿，但拉里持久的魅力是不可否认的，这体现在庞大的社交媒体粉丝群和来自世界各地的粉丝来信中。他在唐宁街10号的存在为英国政坛提供了连续性、无党派吸引力以及一丝轻松。

---

## 63. 使用Web Monetization API进行娱乐和盈利

**原文标题**: Using the Web Monetization API for fun and profit

**原文链接**: [https://blog.tomayac.com/2025/11/07/using-the-web-monetization-api-for-fun-and-profit/](https://blog.tomayac.com/2025/11/07/using-the-web-monetization-api-for-fun-and-profit/)

本文探讨了Web Monetization，一项允许发布者通过“按浏览付费”模式直接从用户处获得收入的拟议标准。作者最近在JSConf Mexico上发表了演讲，并与Interledger Foundation进行了互动，他鼓励读者亲自尝试Web Monetization。

要开始使用，用户需要安装Web Monetization扩展程序，获取一个钱包（如支持欧元和美元的GateHub），并将钱包连接到扩展程序。 尽管这些钱包通常用于加密货币，但交易使用法定货币。 访问已货币化的网站时，扩展程序会显示一个绿色复选标记。 用户可以调整每小时的付款费率并发送一次性付款，资金每分钟都会进行流式传输。

发布者可以通过将包含其个性化付款指针（从其钱包获得）的付款链接添加到其网站代码中来实现Web Monetization。 这使他们能够接收流式传输和一次性付款。

JavaScript API允许基于货币化事件进行动态内容调整。 发布者可以检测到用户何时在付款，例如，删除广告、解锁内容或显示感谢消息。

作者对Web Monetization在为各种规模的网络发布者创造财务可持续的未来方面的潜力持乐观态度。 他鼓励其他人尝试它并分享他们的经验。

---

## 64. 为什么山姆·奥特曼不会为OpenAI的消费狂潮负责

**原文标题**: Why Sam Altman Won't Be on the Hook for OpenAI's Spending Spree

**原文链接**: [https://www.forbes.com/sites/rashishrivastava/2025/11/07/why-sam-altman-wont-be-on-the-hook-for-openais-massive-spending-spree/](https://www.forbes.com/sites/rashishrivastava/2025/11/07/why-sam-altman-wont-be-on-the-hook-for-openais-massive-spending-spree/)

OpenAI豪掷1.4万亿美元豪赌数据中心，谁来买单？

---

## 65. Kimi K2 思考，一个 SOTA 开源万亿参数推理模型

**原文标题**: Kimi K2 Thinking, a SOTA open-source trillion-parameter reasoning model

**原文链接**: [https://moonshotai.github.io/Kimi-K2/thinking.html](https://moonshotai.github.io/Kimi-K2/thinking.html)

Kimi K2 Thinking：参数达万亿的最先进开源推理模型

---

## 66. 华盛顿邮报成为Oracle EBS零日攻击的受害者之一

**原文标题**: Washington Post among breach victims in Oracle EBS zero-day attacks

**原文链接**: [https://www.scworld.com/news/washington-post-latest-victim-of-oracle-ebs-zero-day-attacks](https://www.scworld.com/news/washington-post-latest-victim-of-oracle-ebs-zero-day-attacks)

《华盛顿邮报》成为利用Oracle电子商务套件(EBS)零日漏洞攻击的受害者之一。网络安全公司Onapsis披露，一个老练的威胁行为者（可能出于经济动机）一直在积极攻击使用过时且未打补丁的Oracle EBS系统，以获取未经授权的访问权限、窃取敏感数据并可能中断运营。该漏洞被确定影响多个Oracle EBS版本，允许攻击者绕过身份验证并执行任意代码。

据信，攻击者在公开披露前至少两年就开始利用该漏洞，表明存在一段长时间的未被发现的活动。这些攻击的特点是精确性和复杂性，表明威胁行为者对Oracle EBS架构有深入的了解。Onapsis指出，这些攻击涉及部署webshell以维持对受损系统的持久访问。

虽然Oracle已经发布了该漏洞的补丁，但包括《华盛顿邮报》在内的许多组织显然未能及时应用这些补丁，使其暴露在外。该事件突显了及时打补丁和主动安全措施对于像Oracle EBS这样的企业资源规划(ERP)系统至关重要，这些系统通常包含高度敏感的业务数据。这篇文章强调，各组织需要优先考虑安全更新，并定期监控其系统是否存在被入侵的迹象，以降低此类攻击的风险。

---

## 67. 贺建奎博士论文：生物系统中等级结构的自发涌现 (2010)

**原文标题**: He Jiankui PhD Thesis: Spontaneous Emergence of Hierarchy in Biological Systems (2010)

**原文链接**: [https://repository.rice.edu/server/api/core/bitstreams/85449216-b2ec-4519-87cf-83eafe4534e7/content](https://repository.rice.edu/server/api/core/bitstreams/85449216-b2ec-4519-87cf-83eafe4534e7/content)

无法访问文章链接。

---

## 68. Copy button added to Stack Overflow

**原文标题**: Copy button added to Stack Overflow

**原文链接**: [https://meta.stackexchange.com/questions/414573/results-of-the-october-2025-community-asks-sprint-copy-button-for-code-blocks](https://meta.stackexchange.com/questions/414573/results-of-the-october-2025-community-asks-sprint-copy-button-for-code-blocks)

生成摘要时出错

---

## 69. Comparison Traits – Understanding Equality and Ordering in Rust

**原文标题**: Comparison Traits – Understanding Equality and Ordering in Rust

**原文链接**: [https://itsfoxstudio.substack.com/p/comparison-traits-understanding-equality](https://itsfoxstudio.substack.com/p/comparison-traits-understanding-equality)

生成摘要时出错

---

## 70. Growing rice in the UK 'not so crazy' as climate warms

**原文标题**: Growing rice in the UK 'not so crazy' as climate warms

**原文链接**: [https://www.purdueexponent.org/news/national/growing-rice-in-the-uk-not-so-crazy-as-climate-warms/article_bb71319a-4f91-5f03-90b0-249d497ecc34.html](https://www.purdueexponent.org/news/national/growing-rice-in-the-uk-not-so-crazy-as-climate-warms/article_bb71319a-4f91-5f03-90b0-249d497ecc34.html)

生成摘要时出错

---

## 71. OpenMW 0.50.0 Released – open-source Morrowind reimplementation

**原文标题**: OpenMW 0.50.0 Released – open-source Morrowind reimplementation

**原文链接**: [https://openmw.org/2025/openmw-0-50-0-released/](https://openmw.org/2025/openmw-0-50-0-released/)

生成摘要时出错

---

## 72. Two billion email addresses were exposed

**原文标题**: Two billion email addresses were exposed

**原文链接**: [https://www.troyhunt.com/2-billion-email-addresses-were-exposed-and-we-indexed-them-all-in-have-i-been-pwned/](https://www.troyhunt.com/2-billion-email-addresses-were-exposed-and-we-indexed-them-all-in-have-i-been-pwned/)

生成摘要时出错

---

## 73. FAA to restrict commercial rocket launches to overnight hours

**原文标题**: FAA to restrict commercial rocket launches to overnight hours

**原文链接**: [https://www.space.com/space-exploration/launches-spacecraft/faa-restricts-commercial-rocket-launches-indefinitely-due-to-air-traffic-risks-from-government-shutdown](https://www.space.com/space-exploration/launches-spacecraft/faa-restricts-commercial-rocket-launches-indefinitely-due-to-air-traffic-risks-from-government-shutdown)

生成摘要时出错

---

## 74. We chose OCaml to write Stategraph

**原文标题**: We chose OCaml to write Stategraph

**原文链接**: [https://stategraph.dev/blog/why-we-chose-ocaml](https://stategraph.dev/blog/why-we-chose-ocaml)

生成摘要时出错

---

## 75. Make yourself a Voxel Engine THIS weekend

**原文标题**: Make yourself a Voxel Engine THIS weekend

**原文链接**: [https://daymare.net/blogs/voxel-engine-in-a-weekend/](https://daymare.net/blogs/voxel-engine-in-a-weekend/)

生成摘要时出错

---

## 76. Skeena Indigenous Typeface

**原文标题**: Skeena Indigenous Typeface

**原文链接**: [https://microsoft.github.io/Skeena-Indigenous-Typeface/](https://microsoft.github.io/Skeena-Indigenous-Typeface/)

生成摘要时出错

---

## 77. Analysis of Hedy Lamarr's Contribution to Spread-Spectrum Communication

**原文标题**: Analysis of Hedy Lamarr's Contribution to Spread-Spectrum Communication

**原文链接**: [https://researchers.one/articles/24.01.00001v4](https://researchers.one/articles/24.01.00001v4)

生成摘要时出错

---

## 78. From Memorization to Reasoning in the Spectrum of Loss Curvature

**原文标题**: From Memorization to Reasoning in the Spectrum of Loss Curvature

**原文链接**: [https://arxiv.org/abs/2510.24256](https://arxiv.org/abs/2510.24256)

生成摘要时出错

---

## 79. Gmail AI gets more intrusive

**原文标题**: Gmail AI gets more intrusive

**原文链接**: [https://daveverse.org/2025/11/07/gmail-ai-gets-even-more-intrusive/](https://daveverse.org/2025/11/07/gmail-ai-gets-even-more-intrusive/)

生成摘要时出错

---

## 80. "Green Llama" did not just beat Cascade Platinum Plus

**原文标题**: "Green Llama" did not just beat Cascade Platinum Plus

**原文链接**: [https://foxchapelresearch.substack.com/p/draft-no-green-llama-did-not-just](https://foxchapelresearch.substack.com/p/draft-no-green-llama-did-not-just)

生成摘要时出错

---

## 81. Oddest ChatGPT leaks yet: Cringey chat logs found in Google Analytics tool

**原文标题**: Oddest ChatGPT leaks yet: Cringey chat logs found in Google Analytics tool

**原文链接**: [https://arstechnica.com/tech-policy/2025/11/oddest-chatgpt-leaks-yet-cringey-chat-logs-found-in-google-analytics-tool/](https://arstechnica.com/tech-policy/2025/11/oddest-chatgpt-leaks-yet-cringey-chat-logs-found-in-google-analytics-tool/)

生成摘要时出错

---

## 82. Mind captioning: Evolving descriptive text of mental content of brain activity

**原文标题**: Mind captioning: Evolving descriptive text of mental content of brain activity

**原文链接**: [https://www.science.org/doi/10.1126/sciadv.adw1464](https://www.science.org/doi/10.1126/sciadv.adw1464)

生成摘要时出错

---

## 83. 'Black Hole Sun' by Soundgarden

**原文标题**: 'Black Hole Sun' by Soundgarden

**原文链接**: [https://faroutmagazine.co.uk/the-story-behind-soundgarden-black-hole-sun/](https://faroutmagazine.co.uk/the-story-behind-soundgarden-black-hole-sun/)

生成摘要时出错

---

## 84. Google Threat Intel Group AI Threat Tracker:Advances in Threat Actor AI Tool Use

**原文标题**: Google Threat Intel Group AI Threat Tracker:Advances in Threat Actor AI Tool Use

**原文链接**: [https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)

生成摘要时出错

---

## 85. As CO2 Levels Rise, Old Amazon Trees Are Getting Bigger

**原文标题**: As CO2 Levels Rise, Old Amazon Trees Are Getting Bigger

**原文链接**: [https://eos.org/articles/as-co2-levels-rise-old-amazon-trees-are-getting-bigger](https://eos.org/articles/as-co2-levels-rise-old-amazon-trees-are-getting-bigger)

生成摘要时出错

---

## 86. Show HN: I scraped 3B Goodreads reviews to train a better recommendation model

**原文标题**: Show HN: I scraped 3B Goodreads reviews to train a better recommendation model

**原文链接**: [https://book.sv](https://book.sv)

生成摘要时出错

---

## 87. Multi-objective optimization by quantum annealing

**原文标题**: Multi-objective optimization by quantum annealing

**原文链接**: [https://arxiv.org/abs/2511.01762](https://arxiv.org/abs/2511.01762)

生成摘要时出错

---

## 88. Helion: A high-level DSL for performant and portable ML kernels

**原文标题**: Helion: A high-level DSL for performant and portable ML kernels

**原文链接**: [https://pytorch.org/blog/helion/](https://pytorch.org/blog/helion/)

生成摘要时出错

---

## 89. Game design is simple

**原文标题**: Game design is simple

**原文链接**: [https://www.raphkoster.com/2025/11/03/game-design-is-simple-actually/](https://www.raphkoster.com/2025/11/03/game-design-is-simple-actually/)

生成摘要时出错

---

## 90. LLMs encode how difficult problems are

**原文标题**: LLMs encode how difficult problems are

**原文链接**: [https://arxiv.org/abs/2510.18147](https://arxiv.org/abs/2510.18147)

生成摘要时出错

---

## 91. Show HN: Three Emojis, a daily word puzzle for language learners

**原文标题**: Show HN: Three Emojis, a daily word puzzle for language learners

**原文链接**: [https://threeemojis.com/en-US/play/hex/en-US/2025-11-07](https://threeemojis.com/en-US/play/hex/en-US/2025-11-07)

生成摘要时出错

---

## 92. Hashtable vs. A-list in Scheme, which to choose?

**原文标题**: Hashtable vs. A-list in Scheme, which to choose?

**原文链接**: [https://nalaginrut.com/archives/2025/11/02/hashtable_vs_alist](https://nalaginrut.com/archives/2025/11/02/hashtable_vs_alist)

生成摘要时出错

---

## 93. Blood, Brick and Legend: The Chemistry of Dracula's Castle

**原文标题**: Blood, Brick and Legend: The Chemistry of Dracula's Castle

**原文链接**: [https://news.research.gatech.edu/2025/10/31/blood-brick-and-legend-chemistry-draculas-castle](https://news.research.gatech.edu/2025/10/31/blood-brick-and-legend-chemistry-draculas-castle)

生成摘要时出错

---

## 94. Cryptography 101 with Alfred Menezes

**原文标题**: Cryptography 101 with Alfred Menezes

**原文链接**: [https://cryptography101.ca](https://cryptography101.ca)

生成摘要时出错

---

## 95. Inside Cursor

**原文标题**: Inside Cursor

**原文链接**: [https://joincolossus.com/article/inside-cursor/](https://joincolossus.com/article/inside-cursor/)

生成摘要时出错

---

## 96. The Silent Scientist: When Software Research Fails to Reach Its Audience

**原文标题**: The Silent Scientist: When Software Research Fails to Reach Its Audience

**原文链接**: [https://cacm.acm.org/opinion/the-silent-scientist-when-software-research-fails-to-reach-its-audience/](https://cacm.acm.org/opinion/the-silent-scientist-when-software-research-fails-to-reach-its-audience/)

生成摘要时出错

---

## 97. Toxic Salton Sea dust triggers changes in lung microbiome after just one week

**原文标题**: Toxic Salton Sea dust triggers changes in lung microbiome after just one week

**原文链接**: [https://phys.org/news/2025-10-toxic-salton-sea-triggers-lung.html](https://phys.org/news/2025-10-toxic-salton-sea-triggers-lung.html)

生成摘要时出错

---

## 98. Ratatui – App Showcase

**原文标题**: Ratatui – App Showcase

**原文链接**: [https://ratatui.rs/showcase/apps/](https://ratatui.rs/showcase/apps/)

生成摘要时出错

---

## 99. Dead Framework Theory

**原文标题**: Dead Framework Theory

**原文链接**: [https://aifoc.us/dead-framework-theory/](https://aifoc.us/dead-framework-theory/)

生成摘要时出错

---

## 100. Solarpunk is happening in Africa

**原文标题**: Solarpunk is happening in Africa

**原文链接**: [https://climatedrift.substack.com/p/why-solarpunk-is-already-happening](https://climatedrift.substack.com/p/why-solarpunk-is-already-happening)

生成摘要时出错

---

